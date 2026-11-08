"""Capas do MAT-PLN-009 (1280x720). Uso: python capa.py"""
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



def a(c):  # o gancho: o par vem de graça
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "se é raiz...", 84, 360, 120, "i", BR)
    E.formula(c, "1 + 2i", 84, 600, 200, cor=BR)
    E.escreve(c, "então também é:", 84, 800, 100, "i", BR)
    E.bola(c, 1450, 620, 300, AMARELO)
    E.formula(c, "1 − 2i", 1450, 690, 170, cor=COR, align="center")


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Raízes", "em pares", "o conjugado")


def d(c):  # o atalho: o par já sai pronto
    palco(c)
    E.escreve(c, "o par já sai pronto", 84, 330, 120, "i", BR)
    E.formula(c, "1 ± 2i", 84, 560, 170, cor=BR)
    E.formula(c, "→  x^2 − 2x + 5", 84, 800, 170, cor=AMARELO)
    E.escreve(c, "sem abrir parênteses", 84, 980, 90, "i", "#C9C3FF")


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_o_par", a), ("capa_B_raizes_em_pares", b), ("capa_C_par_pronto", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
