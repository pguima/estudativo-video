"""Capas do MAT-NUM-015 (1280x720). Uso: python capa.py"""
import subprocess, sys
from pathlib import Path
RAIZ = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(RAIZ / "_ferramentas"))
import skia
import editorial as E
import motor as M
BR = "#FFFFFF"
COR = E.MATERIAS["Matemática"]["cor"]
AMARELO = "#FFD500"
CLARO = E.mix(COR, BR, 0.5)


def fundo_escuro(c):
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)


def a(c):  # o gancho: qual é maior?
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "−7", 84, 560, 340, "g", BR)
    E.escreve(c, "ou", 620, 520, 170, "i", BR)
    E.escreve(c, "−2", 900, 560, 340, "g", AMARELO)
    E.escreve(c, "?", 1400, 590, 340, "g", BR)
    E.escreve(c, "qual é maior?", 84, 900, 230, "g", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Números", "negativos", "e reta numérica")


def d(c):  # o atalho: vira ao contrário
    fundo_escuro(c)
    E.escreve(c, "entre negativos", 84, 340, 150, "i", BR)
    E.escreve(c, "vira ao", 80, 570, 240, "g", BR)
    E.escreve(c, "contrário", 80, 780, 240, "g", BR)
    E.escreve(c, "7 > 2", 84, 980, 150, "g", CLARO)
    E.escreve(c, "−7 < −2", 520, 980, 150, "g", AMARELO)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_menos_7_menos_2", a), ("capa_B_negativos_reta", b), ("capa_C_vira_ao_contrario", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
