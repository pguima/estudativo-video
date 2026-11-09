"""Capas do FIS-MOD-010 (1280x720). Uso: python capa.py"""
import math, subprocess, sys
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
E.usar("Física")


def pacote(c, x, y, cor, a=1.0, n=3, amp=40, lam=70, largura=12):
    """fóton: trecho de onda com envelope e ponta em seta, andando para a direita"""
    L = n * lam
    path = skia.Path()
    for i in range(61):
        s = -L / 2 + L * i / 60
        d = amp * math.sin(math.pi * i / 60) * math.sin(2 * math.pi * s / lam)
        path.moveTo(x + s, y - d) if i == 0 else path.lineTo(x + s, y - d)
    c.drawPath(path, M.paint(cor, a, stroke=largura, cap_round=True))
    F._cabeca(c, x + L / 2 + 34, y, 1, 0, 40, cor, a)


def escuro(c):
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Física", COR)


def a(c):  # o gancho: a luz vem em pacotes
    E.capa_base(c, COR); E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "a luz vem", 84, 400, 150, "i", BR)
    E.escreve(c, "em pacotes", 76, 620, 230, "g", BR)
    for i, y in enumerate((800, 900, 1000)):
        pacote(c, 330 + 330 * i, y - 20, BR if i != 1 else AMARELO, 1.0)
import random


def galaxia(c, cx, cy, r, giro=-20):
    c.save(); c.translate(cx, cy); c.rotate(giro); c.scale(1, 0.4)
    p = skia.Paint(AntiAlias=True)
    p.setShader(skia.GradientShader.MakeRadial(skia.Point(0, 0), r, [M.hexc(BR, 0.95), M.hexc("#E8D9FF", 0.6), M.hexc("#E8D9FF", 0.0)], [0.0, 0.35, 1.0]))
    c.drawCircle(0, 0, r, p)
    c.restore()


def buraco(c, cx, cy, r):
    p = skia.Paint(AntiAlias=True)
    p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r * 2.3, [M.hexc(AMARELO, 0.0), M.hexc(AMARELO, 0.0), M.hexc(AMARELO, 0.8), M.hexc(AMARELO, 0.0)], [0.0, 0.4, 0.55, 1.0]))
    c.drawCircle(cx, cy, r * 2.3, p)
    E.arco(c, cx, cy, r * 1.25, 20, 300, "#FFB000", r * 0.18)
    c.drawCircle(cx, cy, r, M.paint("#000000"))


def a(c):  # o gancho: 5 questões de astronomia
    E.capa_base(c, COR); E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "5 questões", 76, 400, 200, "g", BR)
    E.escreve(c, "de astronomia", 84, 560, 120, "i", BR)
    E.escreve(c, "quase sem conta", 84, 760, 120, "g", AMARELO)
    M.rrect(c, 1180, 180, 660, 620, 50, "#0B0B16")
    rnd = random.Random(5)
    for _ in range(60):
        c.drawCircle(1200 + rnd.random() * 620, 200 + rnd.random() * 580, rnd.choice((2, 3, 4)), M.paint(BR, rnd.uniform(0.4, 0.9)))
    galaxia(c, 1420, 360, 180)
    buraco(c, 1660, 640, 70)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Física", "Estrelas e", "Big Bang", "na prática")


def d(c):  # o macete: duas pegadinhas
    escuro(c)
    E.escreve(c, "as 2 pegadinhas", 84, 330, 120, "i", BR)
    E.escreve(c, "o Sol não vira", 84, 540, 120, "g", BR)
    E.escreve(c, "buraco negro", 84, 680, 120, "g", AMARELO)
    E.escreve(c, "o Big Bang não tem centro", 84, 880, 90, "g", BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_5_questoes_de_astronomia", a), ("capa_B_estrelas_e_big_bang", b), ("capa_C_duas_pegadinhas", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
