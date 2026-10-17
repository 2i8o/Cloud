#!/usr/bin/env python3
"""Shot-length (rhythm) analysis of an existing cut.

Detects cuts with ffmpeg's scene-change filter (or takes your own cut times),
then reports shot durations, average shot length (ASL), variation, and an ASCII
shot-length curve so you can check the build -> peak -> release shape.

Limits: scene detection misses dissolves/whip pans and over-fires on flashes or
fast motion. Treat output as a map to check by eye, not as ground truth.
Use --cuts when you already know the cut times (from an EDL, XML, or timeline).

Usage:
  python shot_rhythm.py clip.mp4 [--threshold 0.3]
  python shot_rhythm.py clip.mp4 --cuts 1.2,2.8,3.4,6.0
  python shot_rhythm.py --cuts 1.2,2.8,3.4,6.0 --duration 9.5
"""
import argparse
import re
import shutil
import statistics
import subprocess
import sys


def detect_cuts(path, threshold):
    cmd = ["ffmpeg", "-hide_banner", "-nostats", "-i", path, "-vf",
           f"select='gt(scene,{threshold})',showinfo", "-an", "-f", "null", "-"]
    r = subprocess.run(cmd, capture_output=True, text=True, errors="replace")
    return [float(x) for x in re.findall(r"pts_time:(\d+\.?\d*)", r.stderr)]


def duration_of(path):
    r = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of",
                        "default=nw=1:nk=1", path], capture_output=True, text=True)
    return float(r.stdout.strip())


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("video", nargs="?")
    ap.add_argument("--threshold", type=float, default=0.3, help="scene-change sensitivity 0-1 (lower = more cuts)")
    ap.add_argument("--cuts", help="comma-separated cut times in seconds (skips detection)")
    ap.add_argument("--duration", type=float, help="total duration (needed with --cuts and no video)")
    a = ap.parse_args()

    if a.cuts:
        cuts = sorted(float(x) for x in a.cuts.split(",") if x.strip())
        total = a.duration or (duration_of(a.video) if a.video else None)
        if total is None:
            ap.error("--duration (or a video) is required with --cuts")
    else:
        if not a.video:
            ap.error("a video path or --cuts is required")
        if not (shutil.which("ffmpeg") and shutil.which("ffprobe")):
            print("ERROR: ffmpeg/ffprobe not found on PATH.", file=sys.stderr)
            return 2
        cuts = detect_cuts(a.video, a.threshold)
        total = duration_of(a.video)

    bounds = [0.0] + [c for c in cuts if 0 < c < total] + [total]
    shots = [round(b - a_, 3) for a_, b in zip(bounds, bounds[1:]) if b - a_ > 0]
    n = len(shots)
    if n == 0:
        print("No shots found.")
        return 1

    asl = statistics.mean(shots)
    cv = (statistics.pstdev(shots) / asl) if asl else 0
    print(f"SHOTS {n} | DURATION {total:.2f}s | ASL {asl:.2f}s | MIN {min(shots):.2f}s | MAX {max(shots):.2f}s | "
          f"VARIATION (CV) {cv:.2f}")
    print(f"CUT RATE {60.0 * (n - 1) / total:.1f} cuts/min\n")

    scale = 40.0 / max(shots)
    for i, s in enumerate(shots, 1):
        print(f"{i:>3} {bounds[i-1]:7.2f}s {s:6.2f}s {'#' * max(1, int(s * scale))}")

    print()
    notes = []
    if cv < 0.25 and n >= 5:
        notes.append("Shot lengths are nearly uniform (CV < 0.25): rhythm may read as monotone. "
                     "Check for an intended build/peak/release.")
    if n >= 6:
        h = n // 2
        first, second = statistics.mean(shots[:h]), statistics.mean(shots[h:])
        notes.append(f"First half ASL {first:.2f}s vs second half {second:.2f}s "
                     "(a climax is often preceded by shortening and followed by a longer release).")
        last3 = statistics.mean(shots[-3:])
        notes.append(f"Last 3 shots average {last3:.2f}s vs overall {asl:.2f}s "
                     "(a longer ending hold gives the payoff time to land).")
    if max(shots) > 4 * asl and n >= 4:
        notes.append("One shot is >4x the average: confirm it is a deliberate hold, not a pacing hole.")
    if not notes:
        notes.append("No automatic flags. Judge by watching.")
    for line in notes:
        print("-", line)
    print("- Detection can miss low-contrast cuts (a synthetic test missed one at 0.3 and found all at 0.1): "
          "re-run with a lower --threshold, or pass known times with --cuts.")
    print("- Thresholds here are heuristics (see references/pacing-and-continuity.md); not rules.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
