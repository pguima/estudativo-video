"""Capas do MAT-PLN-010 (1280x720). Uso: python capa.py"""
import subprocess, sys
from pathlib import Path
RAIZ = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(RAIZ / "_ferramentas"))
import skia
import editorial as E
import motor as M
BR = "#FFFFFF"
AMARELO = "#FFD500"
COR = E.MATERIAS["Matemática"]["cor"]


def palco(c):
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)



def a(c):  # o gancho: todas as raízes, reais e complexas
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.formula(c, "x^4 − 16 = 0", 84, 420, 200, cor=BR)
    E.escreve(c, "ache todas as raízes", 84, 600, 110, "i", BR)
    for k, s_ in enumerate(("2", "−2", "2i", "−2i")):
        cx = 230 + 330 * k
        E.bola(c, cx, 840, 130, AMARELO if "i" in s_ else BR)
        E.formula(c, s_, cx, 885, 110, cor=COR, align="center")


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Raízes", "complexas", "praticando")


def d(c):  # o atalho: conte as raízes
    palco(c)
    E.escreve(c, "antes de começar,", 84, 330, 120, "i", BR)
    E.escreve(c, "conte as raízes", 84, 560, 190, "g", AMARELO)
    E.escreve(c, "grau 4 = 4 raízes", 84, 780, 130, "g", BR)
    E.escreve(c, "as com i vêm em pares", 84, 960, 100, "i", "#C9C3FF")


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_todas_as_raizes", a), ("capa_B_raizes_complexas", b), ("capa_C_conte_as_raizes", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
