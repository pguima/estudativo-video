"""Capas do FIS-CAL-002 (1280x720). Uso: python capa.py"""
import subprocess, sys
from pathlib import Path
RAIZ = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(RAIZ / "_ferramentas"))
import skia
import editorial as E
import fisica as F
import motor as M
BR = "#FFFFFF"
AMARELO = "#FFD500"
COR = E.MATERIAS["Física"]["cor"]
CLARO = E.mix(COR, BR, 0.82)
E.usar("Física")


def palco_capa(c):
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Física", COR)


def a(c):  # o gancho: a fresta da ponte
    E.capa_base(c, COR); E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "sem a fresta,", 84, 380, 130, "i", BR)
    E.escreve(c, "a ponte", 84, 560, 190, "g", BR)
    E.escreve(c, "racha", 84, 760, 190, "g", AMARELO)
    x, y, w = 1080, 760, 760
    M.rrect(c, x, y, w / 2 - 16, 50, 8, BR)
    M.rrect(c, x + w / 2 + 16, y, w / 2 - 16, 50, 8, BR)
    for px in (x + w * 0.18, x + w * 0.82):
        M.rrect(c, px - 26, y + 50, 52, 220, 8, CLARO)
    c.drawCircle(x + w / 2, y + 25, 90, M.paint(AMARELO, 1.0, stroke=12))


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Física", "Dilatação", "térmica", "do zero")


def d(c):  # o macete: beta e gama
    palco_capa(c)
    E.escreve(c, "decore só", 84, 340, 130, "i", BR)
    E.escreve(c, "uma fórmula", 84, 540, 190, "g", BR)
    claro = E.mix(COR, BR, 0.5)
    E.formula(c, "β = 2α", 140, 880, 170, "g", claro)
    E.formula(c, "γ = 3α", 1000, 880, 170, "g", BR)


CAPAS = (("capa_A_a_ponte_racha", a), ("capa_B_dilatacao_do_zero", b), ("capa_C_beta_e_gama", d))


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in CAPAS:
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
