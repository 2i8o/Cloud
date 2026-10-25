#!/bin/bash
# encode.sh <frames-dir> <mix.wav> <out.mp4> — loudness-normalised, BT.709, all metadata and tool signatures removed
set -euo pipefail
FR=$1; MIX=$2; OUT=$3
AF="alimiter=limit=0.42:attack=4:release=80:level=disabled"
M=$(ffmpeg -hide_banner -nostats -i "$MIX" -af "$AF,loudnorm=I=-16.5:TP=-1.5:LRA=11:print_format=json" -f null - 2>&1 | sed -n '/^{/,/^}/p')
II=$(echo "$M" | python3 -c "import json,sys;d=json.load(sys.stdin);print(f\"measured_I={d['input_i']}:measured_TP={d['input_tp']}:measured_LRA={d['input_lra']}:measured_thresh={d['input_thresh']}:offset={d['target_offset']}\")")
ffmpeg -hide_banner -loglevel error -y -i "$MIX" -af "$AF,loudnorm=I=-16.5:TP=-1.5:LRA=11:$II:linear=true" -ar 48000 -c:a pcm_s24le "${OUT%.mp4}_audio.wav"
ffmpeg -hide_banner -loglevel error -y -framerate 30 -i "$FR/%05d.png" -i "${OUT%.mp4}_audio.wav" \
  -map 0:v -map 1:a -map_metadata -1 -map_chapters -1 -fflags +bitexact -flags:v +bitexact -flags:a +bitexact \
  -vf "scale=1080:1920:flags=lanczos+accurate_rnd+full_chroma_int:out_color_matrix=bt709:out_range=tv,format=yuv420p" -colorspace bt709 -color_primaries bt709 -color_trc bt709 -color_range tv \
  -c:v libx264 -profile:v high -level 4.2 -preset slow -crf 10 -tune animation -g 60 -bf 2 -bsf:v filter_units=remove_types=6 \
  -c:a aac -b:a 256k -ar 48000 -ac 2 -metadata:s:v encoder= -metadata:s:a encoder= -movflags +faststart -shortest "$OUT"
python3 - "$OUT" <<'PY'
import sys; p=sys.argv[1]; b=bytearray(open(p,'rb').read()); n=b'Lavc libx264'; i=b.find(bytes([len(n)])+n)
if i>0: b[i:i+32]=bytes(32); open(p,'wb').write(b); print('compressorname cleared')
PY
rm -f "${OUT%.mp4}_audio.wav"
