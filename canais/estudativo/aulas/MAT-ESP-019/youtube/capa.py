"""Capas do MAT-ESP-019 (1280x720). Uso: python capa.py"""
import math, subprocess, sys
from pathlib import Path
RAIZ = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(RAIZ / "_ferramentas"))
import skia
import editorial as E
import motor as M
BR = "#FFFFFF"
COR = E.MATERIAS["Matemática"]["cor"]
AMARELO = "#FFD500"
KC, KS = 0.5 * math.cos(math.radians(38)), 0.5 * math.sin(math.radians(38))


def bola_cubo(c, x, y, a):
    """o cubo em traço branco com a bola amarela encostada nas faces"""
    cx, cy = x + a / 2 + KC * a / 2, y - a / 2 - KS * a / 2
    E.cubo(c, 99, 0, x, y, a, escuro=True, cor=BR, preenche=0.0, largura=8)
    c.drawCircle(cx, cy, a / 2, M.paint(AMARELO, 0.92))
    c.drawCircle(cx, cy, a / 2, M.paint(BR, 1, stroke=6))
    E.cubo(c, 99, 0, x, y, a, escuro=True, cor=BR, preenche=0.0, largura=8)


def cone_cil(c, cx, cy, w, h, lw=8):
    """o corte: retângulo (cilindro) com o triângulo (cone) dentro; a sobra pintada"""
    c.drawRect(skia.Rect.MakeXYWH(cx - w / 2, cy - h / 2, w, h), M.paint(AMARELO, 0.92))
    tri = skia.Path(); tri.moveTo(cx - w / 2, cy + h / 2); tri.lineTo(cx, cy - h / 2); tri.lineTo(cx + w / 2, cy + h / 2); tri.close()
    c.drawPath(tri, M.paint("#0B0820"))
    c.drawRect(skia.Rect.MakeXYWH(cx - w / 2, cy - h / 2, w, h), M.paint(BR, 1, stroke=lw))
    c.drawPath(tri, M.paint(BR, 1, stroke=lw))


def a(c):  # o gancho: a bola no cubo deixa metade vazia
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    bola_cubo(c, 130, 930, 560)
    E.escreve(c, "quanto fica", 1000, 360, 110, "i", BR)
    E.escreve(c, "vazio?", 1000, 520, 170, "g", BR)
    E.escreve(c, "metade!", 1000, 820, 200, "g", AMARELO)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Sólidos", "inscritos", "um dentro do outro")


def d(c):  # o atalho: a fração que sobra
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "decore o que sobra", 84, 330, 110, "i", BR)
    cone_cil(c, 420, 640, 260, 340)
    E.formula(c, "f{2}{3}", 640, 720, 200, "g", AMARELO)
    c.drawRect(skia.Rect.MakeXYWH(1010, 500, 300, 300), M.paint(AMARELO, 0.92))
    c.drawCircle(1160, 650, 150, M.paint("#0B0820"))
    c.drawRect(skia.Rect.MakeXYWH(1010, 500, 300, 300), M.paint(BR, 1, stroke=8))
    c.drawCircle(1160, 650, 150, M.paint(BR, 1, stroke=8))
    E.formula(c, "f{1}{2}", 1380, 720, 200, "g", AMARELO)
    E.escreve(c, "com π = 3", 1010, 1000, 90, "g", BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_metade_vazia", a), ("capa_B_solidos_inscritos", b), ("capa_C_fracao_que_sobra", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
