"""Capas do MAT-EXP-012 (1280x720). Uso: python capa.py"""
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


def log(c, base, resto, x, y, size, cor=BR, cor_r=None, r=None):
    """log com a base pequena embaixo; devolve a largura"""
    w = E.formula(c, "log", x, y, size, "g", cor)
    E.escreve(c, base, x + w, y + size * 0.2, size * 0.6, "g", cor)
    w += E.larg(base, "g", size * 0.6) + size * 0.1
    w += E.formula(c, resto, x + w, y, size, "g", cor)
    if r:
        w += E.formula(c, r, x + w, y, size, "g", cor_r or cor)
    return w


def a(c):  # o gancho: uma das raízes é falsa
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.formula(c, "log x + log(x − 3) = 1", 84, 360, 120, "g", BR)
    E.escreve(c, "x = 5", 84, 640, 190, "g", AMARELO)
    E.escreve(c, "x = −2", 760, 640, 190, "g", BR)
    E.risco(c, 740, 650, 1360, 560, 1.0, 0.0, "#FF4D5E", 18)
    E.pilula(c, "uma raiz é falsa", 640, 860, 80, "g", fundo=AMARELO, cor=COR)


def b(c):  # o modelo
    E.capa_modelo(c, "Matemática", "Equação", "logarítmica", "e a raiz falsa")


def d(c):  # o atalho: filtre as alternativas
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "o atalho:", 84, 330, 120, "i", claro)
    E.escreve(c, "filtre as", 76, 540, 190, "g", BR)
    E.escreve(c, "alternativas", 76, 740, 190, "g", AMARELO)
    E.escreve(c, "condição primeiro: x > 3", 84, 950, 90, "g", claro)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_raiz_falsa", a), ("capa_B_equacao_logaritmica", b), ("capa_C_filtre_as_alternativas", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
