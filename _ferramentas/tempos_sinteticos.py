"""tempos.json provisório (sem voz): 0,36 s por palavra + pausas [p=]. Uso: tempos_sinteticos.py <proj>"""
import sys, re, json, importlib.util
from pathlib import Path
proj = Path(sys.argv[1])
s = importlib.util.spec_from_file_location("c", proj / "roteiro" / "cenas.py"); m = importlib.util.module_from_spec(s); s.loader.exec_module(m)
WPS = 0.36
t, scenes = 0.6, []
for sc in m.SCENES:
    lt, toks, cues, bold = 0.3, [], {}, False
    for piece in re.findall(r"\{[^}]+\}|\[p=[\d.]+\]|\S+", sc["text"]):
        if piece.startswith("{"):
            cues[piece[1:-1]] = lt
        elif piece.startswith("[p="):
            lt += float(piece[3:-1])
        else:
            starts, ends = piece.startswith("*"), piece.rstrip(",.:;?!").endswith("*")
            b = bold or starts
            disp = piece.replace("*", "")
            toks.append(dict(disp=disp, bold=b, t0=round(lt, 2), t1=round(lt + WPS, 2)))
            bold = b and not ends
            lt += WPS
    dur = lt + 0.4
    scenes.append(dict(id=sc["id"], block=sc["block"], start=round(t, 2), dur=round(dur, 2), tokens=toks, cues=cues))
    t += dur
(proj / "audio" / "tempos.json").write_text(json.dumps(dict(total=round(t + 0.5, 2), scenes=scenes), ensure_ascii=False), encoding="utf-8")
for s_ in scenes: print(s_["id"], s_["block"], s_["start"], s_["dur"])
