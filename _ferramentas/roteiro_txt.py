"""roteiro/roteiro_para_gravar.txt a partir do cenas.py (sem cues, pausas e asteriscos). Uso: roteiro_txt.py <proj>"""
import re, sys, importlib.util
from pathlib import Path
proj = Path(sys.argv[1])
s = importlib.util.spec_from_file_location("c", proj / "roteiro" / "cenas.py"); m = importlib.util.module_from_spec(s); s.loader.exec_module(m)
out, tot = [], 0
for sc in m.SCENES:
    t = re.sub(r"\{[^}]+\}|\[p=[\d.]+\]", "", sc["text"]).replace("*", "")
    t = re.sub(r"\s+([,.:;?!])", r"\1", re.sub(r"\s+", " ", t)).strip()
    out.append(t); tot += len(t.split())
(proj / "roteiro" / "roteiro_para_gravar.txt").write_text("\n\n".join(out) + "\n", encoding="utf-8")
print(tot, "palavras ·", round(tot / 2.5 / 60, 1), "min")
