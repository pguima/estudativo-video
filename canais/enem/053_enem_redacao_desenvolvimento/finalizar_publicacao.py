"""Preenche o youtube/publicacao.md de cada episódio: {{CAPITULOS}} (tempos reais do audio/tempos.json + youtube/capitulos.json)
e os marcadores [TÍTULO EP N] (TITULO do cenas.py). O modelo fica em youtube/publicacao.tpl.md (criado na 1ª execução).
Uso: finalizar_publicacao.py [epN ...]  (sem argumento = todos os episódios com tempos.json)"""
import importlib.util, json, re, sys
from pathlib import Path
B = Path(__file__).parent
eps = sorted(B.glob("ep*_*"))
tit = {}
for e in eps:
    s = importlib.util.spec_from_file_location("c", e / "roteiro" / "cenas.py"); m = importlib.util.module_from_spec(s); s.loader.exec_module(m)
    tit[int(e.name[2])] = m.TITULO
for e in eps:
    if len(sys.argv) > 1 and not any(e.name.startswith(a) for a in sys.argv[1:]):
        continue
    y = e / "youtube"
    tpl = y / "publicacao.tpl.md"
    if not tpl.exists():
        tpl.write_text((y / "publicacao.md").read_text(encoding="utf-8"), encoding="utf-8")
    md = tpl.read_text(encoding="utf-8")
    st = {s["id"]: s["start"] for s in json.load(open(e / "audio" / "tempos.json"))["scenes"]}
    lin = []
    for k, (sid, nome) in enumerate(json.load(open(y / "capitulos.json"))):
        t = 0 if k == 0 else int(st[sid])
        lin.append(f"{t // 60:02d}:{t % 60:02d} {nome}")
    md = md.replace("{{CAPITULOS}}", "\n".join(lin))
    md = re.sub(r"\[TÍTULO EP (\d)\]", lambda mm: tit[int(mm.group(1))], md)
    (y / "publicacao.md").write_text(md, encoding="utf-8")
    print(e.name, len(lin), "capítulos")
