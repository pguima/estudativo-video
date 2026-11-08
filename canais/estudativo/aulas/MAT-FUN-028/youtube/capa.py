"""Capas do MAT-FUN-028 (1280x720). Uso: python capa.py"""
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
VERMELHO = "#FF4D55"


def reta(c, y, x0, x1, a_, b_, fa, fb, cor, fundo, vmin=0, vmax=6, seta_fim=False):
    vx = lambda v: x0 + (v - vmin) / (vmax - vmin) * (x1 - x0)
    M.arrow(c, x0 - 30, y, x1 + 50, y, BR, 0.8, 5, 20)
    xb = x1 + 30 if seta_fim else vx(b_)
    M.line(c, vx(a_), y, xb, y, cor, 1, 14)
    if seta_fim:
        M.line(c, xb, y, xb - 28, y - 20, cor, 1, 9); M.line(c, xb, y, xb - 28, y + 20, cor, 1, 9)
    for v, fe in ((a_, fa), (None if seta_fim else b_, fb)):
        if v is None:
            continue
        c.drawCircle(vx(v), y, 20, M.paint(cor if fe else fundo)); c.drawCircle(vx(v), y, 20, M.paint(cor, 1, stroke=7))
    return vx


def a(c):  # o gancho: e, não ou
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "juntar ou", 84, 390, 150, "g", BR)
    E.escreve(c, "cruzar?", 84, 560, 150, "g", AMARELO)
    E.escreve(c, "duas inequações ao mesmo tempo", 84, 700, 60, "i", BR)
    x0, x1 = 1080, 1760
    vx = reta(c, 330, x0, x1, 1, 6, False, False, BR, COR, seta_fim=True)
    reta(c, 480, x0, x1, 2, 3, False, False, BR, COR)
    M.rrect(c, vx(2) - 10, 270, vx(3) - vx(2) + 20, 420, 18, AMARELO, 0.35)
    reta(c, 640, x0, x1, 2, 3, False, False, AMARELO, COR)
    E.pilula(c, "]2, 3[", (vx(2) + vx(3)) / 2, 760, 56, "g", fundo=AMARELO, cor=COR)


def b(c):  # o modelo
    E.capa_modelo(c, "Matemática", "Sistema de", "inequações", "empilhe as retas")


def d(c):  # o atalho: maior dos começos, menor dos fins
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "maior dos começos,", 84, 400, 110, "g", BR)
    E.escreve(c, "menor dos fins", 84, 540, 110, "g", AMARELO)
    E.escreve(c, "a interseção sem desenhar", 84, 660, 64, "i", claro)
    x0, x1 = 300, 1640
    vx = reta(c, 800, x0, x1, 1, 5, True, True, BR, "#07070F")
    reta(c, 900, x0, x1, 3, 6, False, False, BR, "#07070F", seta_fim=True)
    for v, cor in ((3, AMARELO), (5, AMARELO)):
        M.line(c, vx(v), 740, vx(v), 960, cor, 1, 5, dash=[14, 10])
    E.pilula(c, "]3, 5]", (vx(3) + vx(5)) / 2, 1000, 48, "g", fundo=AMARELO, cor="#07070F")


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_juntar_ou_cruzar", a), ("capa_B_sistema_de_inequacoes", b), ("capa_C_maior_dos_comecos", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
