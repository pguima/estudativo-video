"""Capas do MAT-FUN-013 (1280x720). Uso: python capa.py"""
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


def eixos(c, x, y, w, h, tinta=BR):
    """eixos do primeiro quadrante: a origem no canto de baixo à esquerda"""
    M.arrow(c, x, y + h, x + w + 30, y + h, tinta, 1, 7, 26)
    M.arrow(c, x, y + h, x, y - 30, tinta, 1, 7, 26)


def reta(c, x, y, w, h, y0, y1, cor, largura=12):
    """reta de (0, y0) até (1, y1), em frações da caixa"""
    M.line(c, x, y + h - y0 * h, x + w, y + h - y1 * h, cor, 1, largura)


def a(c):  # o gancho: duas retas que sobem, só uma é proporcional
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "qual é", 84, 450, 150, "i", BR)
    E.escreve(c, "proporcional?", 76, 650, 170, "g", BR)
    E.escreve(c, "um ponto entrega", 84, 860, 110, "i", BR)
    x, y, w, h = 1240, 260, 560, 600
    eixos(c, x, y, w, h)
    reta(c, x, y, w, h, 0.0, 0.95, BR, 14)
    reta(c, x, y, w, h, 0.32, 0.8, E.mix(COR, BR, 0.55), 14)
    c.drawCircle(x, y + h, 40, M.paint(AMARELO, 1, stroke=10))


def b(c):  # o modelo
    E.capa_modelo(c, "Matemática", "Função", "linear", "y = kx")


def d(c):  # o atalho: um ponto dá o k
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "um ponto", 84, 420, 140, "i", claro)
    E.escreve(c, "dá o k", 76, 640, 220, "g", BR)
    E.formula(c, "k = f{y}{x}", 84, 900, 150, "g", AMARELO)
    x, y, w, h = 1180, 240, 600, 620
    eixos(c, x, y, w, h)
    reta(c, x, y, w, h, 0.0, 0.95, claro, 12)
    X, Y = x + w * 0.6, y + h - h * 0.57
    M.line(c, X, Y, X, y + h, BR, 0.8, 5, dash=[18, 12]); M.line(c, X, Y, x, Y, BR, 0.8, 5, dash=[18, 12])
    c.drawCircle(X, Y, 26, M.paint(AMARELO))


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_qual_e_proporcional", a), ("capa_B_funcao_linear", b), ("capa_C_um_ponto_da_o_k", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
