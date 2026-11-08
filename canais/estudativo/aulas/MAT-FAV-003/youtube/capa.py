"""Capas do MAT-FAV-003 (1280x720). Uso: python capa.py"""
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


def palco(c):
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)


def reta(c, y, x0, x1, fora, cor, fundo):
    """reta com as pontas −2 e 8 (bolinha vazia): entre (fora=False) ou fora"""
    vx = lambda v: x0 + (v + 4) / 14 * (x1 - x0)
    M.line(c, x0, y, x1, y, BR, 0.6, 6)
    if fora:
        M.line(c, x0, y, vx(-2), y, cor, 1, 18); M.line(c, vx(8), y, x1, y, cor, 1, 18)
    else:
        M.line(c, vx(-2), y, vx(8), y, cor, 1, 18)
    for v in (-2, 8):
        c.drawCircle(vx(v), y, 24, M.paint(fundo)); c.drawCircle(vx(v), y, 24, M.paint(cor, 1, stroke=9))
    c.drawCircle(vx(3), y, 16, M.paint(BR))


def a(c):  # o gancho: duas respostas
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "|x − 3| = 5", 84, 400, 190, "g", BR)
    E.escreve(c, "x = 8", 84, 620, 150, "g", BR)
    E.escreve(c, "e x = −2", 600, 620, 150, "g", AMARELO)
    E.escreve(c, "são duas respostas", 84, 840, 110, "i", BR)


def b(c):  # o modelo
    E.capa_modelo(c, "Matemática", "Equação", "modular", "pela distância")


def d(c):  # o atalho: menor entre, maior fora
    palco(c)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "menor:", 84, 380, 110, "i", BR)
    E.escreve(c, "entre", 84, 530, 170, "g", BR)
    E.escreve(c, "maior:", 84, 760, 110, "i", BR)
    E.escreve(c, "fora", 84, 910, 170, "g", AMARELO)
    reta(c, 470, 960, 1800, False, BR, "#07070F")
    reta(c, 850, 960, 1800, True, AMARELO, "#07070F")


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_duas_respostas", a), ("capa_B_equacao_modular", b), ("capa_C_menor_entre_maior_fora", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
