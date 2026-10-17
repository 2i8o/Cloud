#!/usr/bin/env python3
"""Technical QC probe for a finished or draft video.

Measures (via ffprobe/ffmpeg, no other dependencies):
  - container/stream specs: resolution, fps, duration, codecs, audio channels
  - EBU R128 loudness: integrated LUFS, loudness range, true peak
  - silence gaps, black frames, frozen frames (candidates only: confirm by eye/ear)
  - optional spec checks (--expect-*)

It reports evidence; it does not judge taste. Exit code 0 = no spec failures,
1 = at least one expectation failed, 2 = tool/file error.

Usage:
  python video_qc.py clip.mp4
  python video_qc.py clip.mp4 --expect-width 1080 --expect-height 1920 --expect-fps 30 --json
"""
import argparse
import json
import re
import shutil
import subprocess
import sys


def run(cmd):
    return subprocess.run(cmd, capture_output=True, text=True, errors="replace")


def probe(path):
    r = run(["ffprobe", "-v", "error", "-print_format", "json", "-show_format", "-show_streams", path])
    if r.returncode != 0:
        raise RuntimeError("ffprobe failed: " + r.stderr.strip())
    return json.loads(r.stdout)


def fps_of(stream):
    num, _, den = (stream.get("avg_frame_rate") or "0/1").partition("/")
    try:
        return float(num) / float(den or 1) if float(den or 1) else 0.0
    except ValueError:
        return 0.0


def loudness(path):
    r = run(["ffmpeg", "-hide_banner", "-nostats", "-i", path, "-vn", "-af", "ebur128=peak=true", "-f", "null", "-"])
    text = r.stderr
    # The summary block is printed at the end; take the last occurrences.
    def last(pattern):
        m = re.findall(pattern, text)
        return float(m[-1]) if m else None
    return {
        "integrated_lufs": last(r"I:\s+(-?\d+\.?\d*)\s+LUFS"),
        "loudness_range_lu": last(r"LRA:\s+(-?\d+\.?\d*)\s+LU"),
        "true_peak_dbtp": last(r"Peak:\s+(-?\d+\.?\d*)\s+dBFS"),
    }


def detect(path, vf=None, af=None):
    cmd = ["ffmpeg", "-hide_banner", "-nostats", "-i", path]
    if vf:
        cmd += ["-vf", vf, "-an"]
    if af:
        cmd += ["-af", af, "-vn"]
    cmd += ["-f", "null", "-"]
    return run(cmd).stderr


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("video")
    ap.add_argument("--expect-width", type=int)
    ap.add_argument("--expect-height", type=int)
    ap.add_argument("--expect-fps", type=float)
    ap.add_argument("--max-duration", type=float, help="seconds")
    ap.add_argument("--target-lufs", type=float, default=-14.0, help="reference only; confirm the platform's current target")
    ap.add_argument("--silence-db", type=float, default=-50.0)
    ap.add_argument("--silence-min", type=float, default=0.5, help="seconds")
    ap.add_argument("--freeze-min", type=float, default=2.0, help="seconds")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()

    if not (shutil.which("ffprobe") and shutil.which("ffmpeg")):
        print("ERROR: ffmpeg/ffprobe not found on PATH.", file=sys.stderr)
        return 2
    try:
        info = probe(a.video)
    except Exception as e:  # noqa: BLE001
        print("ERROR:", e, file=sys.stderr)
        return 2

    v = next((s for s in info["streams"] if s["codec_type"] == "video"), None)
    au = next((s for s in info["streams"] if s["codec_type"] == "audio"), None)
    dur = float(info["format"].get("duration", 0) or 0)

    report = {"file": a.video, "duration_s": round(dur, 3), "video": None, "audio": None,
              "loudness": None, "silence": [], "black": [], "freeze": [], "checks": []}
    if v:
        report["video"] = {"codec": v.get("codec_name"), "width": v.get("width"), "height": v.get("height"),
                           "fps": round(fps_of(v), 3), "pix_fmt": v.get("pix_fmt")}
    if au:
        report["audio"] = {"codec": au.get("codec_name"), "channels": au.get("channels"),
                           "sample_rate": au.get("sample_rate")}

    def check(name, ok, detail):
        report["checks"].append({"check": name, "pass": bool(ok), "detail": detail})

    if v:
        if a.expect_width:
            check("width", v.get("width") == a.expect_width, f"{v.get('width')} vs {a.expect_width}")
        if a.expect_height:
            check("height", v.get("height") == a.expect_height, f"{v.get('height')} vs {a.expect_height}")
        if a.expect_fps:
            check("fps", abs(fps_of(v) - a.expect_fps) < 0.05, f"{fps_of(v):.3f} vs {a.expect_fps}")
    elif a.expect_width or a.expect_height or a.expect_fps:
        check("video stream", False, "no video stream")
    if a.max_duration:
        check("duration", dur <= a.max_duration, f"{dur:.2f}s vs max {a.max_duration}s")

    if au:
        report["loudness"] = loudness(a.video)
        lo = report["loudness"]
        if lo["true_peak_dbtp"] is not None:
            check("true peak <= -1 dBTP (common guideline, verify platform)", lo["true_peak_dbtp"] <= -1.0,
                  f"{lo['true_peak_dbtp']} dBTP")
        t = detect(a.video, af=f"silencedetect=noise={a.silence_db}dB:d={a.silence_min}")
        starts = [float(x) for x in re.findall(r"silence_start:\s*(-?\d+\.?\d*)", t)]
        ends = [float(x) for x in re.findall(r"silence_end:\s*(-?\d+\.?\d*)", t)]
        for i, s in enumerate(starts):
            report["silence"].append({"start": round(s, 2),
                                      "end": round(ends[i], 2) if i < len(ends) else round(dur, 2),
                                      "to_end_of_file": i >= len(ends)})
    else:
        check("audio stream present", False, "no audio stream")

    if v:
        t = detect(a.video, vf="blackdetect=d=0.1:pix_th=0.10")
        for s, e, d in re.findall(r"black_start:(\S+)\s+black_end:(\S+)\s+black_duration:(\S+)", t):
            report["black"].append({"start": float(s), "end": float(e), "duration": float(d)})
        t = detect(a.video, vf=f"freezedetect=n=-60dB:d={a.freeze_min}")
        starts = [float(x) for x in re.findall(r"freeze_start:\s*(\S+)", t)]
        durs = [float(x) for x in re.findall(r"freeze_duration:\s*(\S+)", t)]
        for i, s in enumerate(starts):
            # ffmpeg prints freeze_duration only when the freeze ends before EOF.
            if i < len(durs):
                report["freeze"].append({"start": round(s, 2), "duration": round(durs[i], 2)})
            else:
                report["freeze"].append({"start": round(s, 2), "duration": round(max(dur - s, 0), 2),
                                         "to_end_of_file": True})

    if a.json:
        print(json.dumps(report, indent=2))
    else:
        print(f"FILE      {a.video}")
        print(f"DURATION  {dur:.2f}s")
        if report["video"]:
            vv = report["video"]
            print(f"VIDEO     {vv['width']}x{vv['height']} @ {vv['fps']} fps  {vv['codec']}  {vv['pix_fmt']}")
        if report["audio"]:
            aa = report["audio"]
            print(f"AUDIO     {aa['codec']}  {aa['channels']} ch  {aa['sample_rate']} Hz")
        if report["loudness"]:
            lo = report["loudness"]
            print(f"LOUDNESS  integrated {lo['integrated_lufs']} LUFS (ref {a.target_lufs}), "
                  f"LRA {lo['loudness_range_lu']} LU, true peak {lo['true_peak_dbtp']} dBTP")
        print(f"SILENCE   {report['silence'] or 'none'}  (>= {a.silence_min}s below {a.silence_db} dB; confirm intent)")
        print(f"BLACK     {report['black'] or 'none'}")
        print(f"FREEZE    {report['freeze'] or 'none'}  (>= {a.freeze_min}s; deliberate holds are fine)")
        for c in report["checks"]:
            print(("PASS  " if c["pass"] else "FAIL  ") + f"{c['check']}: {c['detail']}")
        print("NOTE      Flags are candidates, not verdicts. Confirm by eye and ear.")

    return 0 if all(c["pass"] for c in report["checks"]) else 1


if __name__ == "__main__":
    sys.exit(main())
