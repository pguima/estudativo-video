"""Capas da QUI-CAL-014 (1280x720). Uso: python capa.py"""
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
def a(c):  # o gancho: o mesmo 21% de oxigênio
    E.capa_base(c, COR); E.capa_rotulo(c, "Química", COR)
    E.escreve(c, "no Everest, o ar tem", 84, 360, 110, "i", BR)
    E.escreve(c, "21% de oxigênio", 84, 570, 160, "g", AMARELO)
    E.escreve(c, "e falta ar", 84, 760, 150, "g", BR)
    E.escreve(c, "o que muda é a pressão", 84, 990, 90, "i", BR)
    p = skia.Path(); p.moveTo(1300, 900); p.lineTo(1600, 380); p.lineTo(1900, 900); p.close()
    c.drawPath(p, M.paint(BR, 0.3))
    n = skia.Path(); n.moveTo(1600, 380); n.lineTo(1540, 480); n.lineTo(1600, 460); n.lineTo(1660, 480); n.close()
    c.drawPath(n, M.paint(BR, 1.0))


def b(c):
    E.capa_modelo(c, "Química", "Pressão", "parcial", "misturas gasosas")


def d(c):  # o macete: parcial = % do total
    palco(c)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "pressão parcial", 84, 330, 110, "i", BR)
    E.escreve(c, "= % do total", 76, 560, 190, "g", claro)
    E.escreve(c, "20% de 5 atm = 1 atm", 84, 800, 120, "g", BR)
    E.escreve(c, "sem fórmula nova", 84, 990, 90, "i", BR)


CAPAS = (("capa_A_everest", a), ("capa_B_pressao_parcial", b), ("capa_C_porcentagem_do_total", d))


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in CAPAS:
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
