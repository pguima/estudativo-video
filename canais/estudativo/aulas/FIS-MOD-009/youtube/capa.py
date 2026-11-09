"""Capas do FIS-MOD-009 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: o chuvisco da TV
    E.capa_base(c, COR); E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "luz do", 84, 390, 170, "g", BR)
    E.escreve(c, "Big Bang", 76, 590, 200, "g", AMARELO)
    E.escreve(c, "no chuvisco da TV", 84, 790, 100, "i", BR)
    M.rrect(c, 1170, 200, 680, 520, 50, "#3A3A42")
    M.rrect(c, 1210, 240, 600, 440, 24, "#22222A")
    rnd = random.Random(2)
    for _ in range(900):
        x, y = 1210 + rnd.random() * 600, 240 + rnd.random() * 440
        c.drawRect(skia.Rect.MakeXYWH(x, y, 8, 5), M.paint(rnd.choice(("#FFFFFF", "#9A9AA5", "#5A5A66"))))
    for _ in range(14):
        x, y = 1210 + rnd.random() * 600, 240 + rnd.random() * 440
        c.drawRect(skia.Rect.MakeXYWH(x, y, 12, 8), M.paint(AMARELO))


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Física", "Big Bang", "e expansão", "do zero")


def d(c):  # o macete: vermelho vai embora
    escuro(c)
    E.escreve(c, "o macete do Doppler", 84, 330, 110, "i", BR)
    E.escreve(c, "Vermelho = Vai embora", 84, 560, 120, "g", "#FF6A5F")
    E.escreve(c, "Azul = Aproxima", 84, 740, 120, "g", "#7EA6FF")
    galaxia(c, 1650, 920, 160)
    E.escreve(c, "a mesma letra", 84, 940, 80, "i", E.mix(COR, BR, 0.5))


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_luz_do_big_bang", a), ("capa_B_big_bang_e_expansao", b), ("capa_C_vermelho_vai_embora", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
