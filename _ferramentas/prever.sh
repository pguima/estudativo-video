#!/bin/bash
# uso: prever.sh <proj> "<ids de cena separados por espaço>" [offset]
P=$1; IDS=$2; OFF=${3:-1.2}
T=$(python -c "
import json,sys;d=json.load(open('$P/audio/tempos.json',encoding='utf-8'))
ids='$IDS'.split();out=[]
for s in d['scenes']:
  if s['id'] in ids:
    for k,v in s['cues'].items(): out.append(s['start']+v+$OFF)
    out.append(s['start']+s['dur']-0.6)
print(','.join(f'{x:.2f}' for x in sorted(out)))")
rm -rf $P/trabalho/stills
python "$(dirname $0)/render.py" $P --stills "$T" > /dev/null
i=0; for f in $P/trabalho/stills/t*.png; do cp "$f" "$P/trabalho/seq_$(printf %03d $i).png"; i=$((i+1)); done
rm -f $P/trabalho/sheet_*.png
ffmpeg -v error -y -i $P/trabalho/seq_%03d.png -vf "scale=640:-1,tile=3x4" $P/trabalho/sheet_%02d.png
rm $P/trabalho/seq_*.png; ls $P/trabalho/sheet_*
