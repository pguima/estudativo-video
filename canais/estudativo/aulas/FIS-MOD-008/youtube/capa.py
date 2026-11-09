"""Capas do FIS-MOD-008 (1280x720). Uso: python capa.py"""
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
def buraco(c, cx, cy, r):
    p = skia.Paint(AntiAlias=True)
    p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r * 2.3, [M.hexc(AMARELO, 0.0), M.hexc(AMARELO, 0.0), M.hexc(AMARELO, 0.8), M.hexc(AMARELO, 0.0)], [0.0, 0.4, 0.55, 1.0]))
    c.drawCircle(cx, cy, r * 2.3, p)
    E.arco(c, cx, cy, r * 1.25, 20, 300, "#FFB000", r * 0.18)
    c.drawCircle(cx, cy, r, M.paint("#000000"))


def a(c):  # o gancho: nem a luz sai
    E.capa_base(c, COR); E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "nem a luz", 76, 400, 190, "g", BR)
    E.escreve(c, "escapa", 76, 600, 190, "g", AMARELO)
    E.escreve(c, "o buraco negro e a vida das estrelas", 84, 860, 60, "i", BR)
    M.rrect(c, 1180, 160, 640, 640, 50, "#0B0B16")
    import random
    rnd = random.Random(4)
    for _ in range(60):
        c.drawCircle(1200 + rnd.random() * 600, 180 + rnd.random() * 600, rnd.choice((2, 3, 4)), M.paint(BR, rnd.uniform(0.4, 0.9)))
    buraco(c, 1500, 480, 130)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Física", "Buraco", "negro", "e a vida das estrelas")


def d(c):  # o macete: a massa decide
    escuro(c)
    E.escreve(c, "o fim de uma estrela?", 84, 330, 110, "i", BR)
    E.escreve(c, "a massa", 84, 560, 200, "g", BR)
    E.escreve(c, "decide", 84, 760, 200, "g", AMARELO)
    for i, (cor, r) in enumerate((("#DDEBFF", 40), ("#5AA9FF", 55), ("#000000", 70))):
        if cor == "#000000":
            buraco(c, 1300 + 230 * i, 700, r)
        else:
            E.bola(c, 1300 + 230 * i, 700, r, cor)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_nem_a_luz_escapa", a), ("capa_B_estrelas_e_buracos_negros", b), ("capa_C_a_massa_decide", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
