"""Capas da QUI-MIS-008 (1280x720). Uso: python capa.py"""
import importlib.util
import subprocess, sys
from pathlib import Path
RAIZ = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(RAIZ / "_ferramentas"))
import skia
import editorial as E
import motor as M
BR = "#FFFFFF"
AMARELO = "#FFD500"
COR = E.MATERIAS["Química"]["cor"]
E.usar("Química")
_s = importlib.util.spec_from_file_location("visual_aula", Path(__file__).parents[1] / "roteiro" / "visual.py")
V = importlib.util.module_from_spec(_s); _s.loader.exec_module(V)


def a(c):  # o gancho: o álcool para nos 96%
    E.capa_base(c, COR); E.capa_rotulo(c, "Química", COR)
    E.escreve(c, "por que o álcool", 84, 340, 110, "i", BR)
    E.escreve(c, "para nos", 84, 520, 150, "g", BR)
    E.escreve(c, "96%?", 84, 760, 260, "g", AMARELO)
    E.escreve(c, "destilação simples e fracionada", 84, 980, 74, "i", BR)
    V.torre(c, 10, 0, 1060, 140, 220, 820, None)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Química", "Destilação", "fracionada", "do zero")


def d(c):  # o macete: o que você quer guardar?
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Química", COR)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "qual destilação?", 84, 330, 110, "i", BR)
    E.escreve(c, "o que quer", 76, 520, 160, "g", BR)
    E.escreve(c, "guardar?", 76, 700, 160, "g", claro)
    for k, (q, r) in enumerate((("o sólido", "evaporação"), ("o líquido", "simples"), ("2 líquidos", "fracionada"))):
        y = 360 + 200 * k
        E.escreve(c, q, 1180, y, 60, "b", BR)
        E.escreve(c, "→ " + r, 1180, y + 80, 64, "g", claro)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_alcool_para_nos_96", a), ("capa_B_destilacao_fracionada", b), ("capa_C_o_que_quer_guardar", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
