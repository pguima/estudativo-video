"""Capas da QUI-CAL-011 (1280x720). Uso: python capa.py"""
import subprocess, sys
from pathlib import Path
RAIZ = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(RAIZ / "_ferramentas"))
import skia
import editorial as E
import quimica as Q
import motor as M
BR = "#FFFFFF"
AMARELO = "#FFD500"
COR = E.MATERIAS["Química"]["cor"]
E.usar("Química")


def palco(c):
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Química", COR)
def a(c):  # o gancho: metade do espaço, o dobro da pressão
    E.capa_base(c, COR); E.capa_rotulo(c, "Química", COR)
    E.escreve(c, "metade do espaço", 84, 380, 140, "g", BR)
    E.escreve(c, "o dobro da", 84, 590, 150, "g", AMARELO)
    E.escreve(c, "pressão", 84, 780, 150, "g", AMARELO)
    E.escreve(c, "a regra dos gases", 84, 990, 90, "i", BR)
    M.rrect(c, 1420, 520, 300, 300, 10, BR, 0.25)
    pth = skia.Path(); pth.moveTo(1420, 300); pth.lineTo(1420, 820); pth.lineTo(1720, 820); pth.lineTo(1720, 300)
    c.drawPath(pth, M.paint(BR, 1.0, stroke=10))
    M.rrect(c, 1426, 500, 288, 34, 8, BR, 1.0)
    M.rrect(c, 1556, 330, 28, 170, 6, BR, 1.0)


def b(c):
    E.capa_modelo(c, "Química", "Equação", "geral", "dos gases")


def d(c):  # o macete: os fatores
    palco(c)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "sem fórmula:", 84, 330, 110, "i", BR)
    E.escreve(c, "os fatores", 76, 530, 170, "g", BR)
    E.formula(c, "10 × ½ × 1,2 = 6 L", 84, 780, 140, "g", claro)
    E.escreve(c, "pressão invertida, temperatura direta", 84, 990, 70, "i", BR)


CAPAS = (("capa_A_metade_do_espaco", a), ("capa_B_equacao_geral", b), ("capa_C_os_fatores", d))


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in CAPAS:
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
