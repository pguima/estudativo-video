"""Capas do FIS-MOD-002 (1280x720). Uso: python capa.py"""
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
def eletron(c, cx, cy, r, a=1.0):
    E.bola(c, cx, cy, r, F.NEG, a)
    M.line(c, cx - r * 0.42, cy, cx + r * 0.42, cy, BR, a, max(3, r * 0.2))


def placa(c, x, y, w, h):
    M.rrect(c, x, y, w, h, 12, "#C9CED4", 1.0)
    M.rrect(c, x + 10, y + 10, w - 20, h * 0.2, 6, "#EEF1F4", 1.0)


def a(c):  # o gancho: luz fraca vence luz forte
    E.capa_base(c, COR); E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "luz fraca", 84, 400, 200, "g", BR)
    E.escreve(c, "vence a forte", 84, 600, 150, "i", BR)
    placa(c, 1180, 880, 620, 90)
    for i in range(3):
        pacote(c, 1060 + 40 * i, 470 + 140 * i, AMARELO, 1.0, n=3, amp=26, lam=44, largura=10)
    for x, y in ((1560, 560), (1700, 430), (1790, 650)):
        eletron(c, x, y, 46)
    E.escreve(c, "por quê?", 84, 900, 150, "g", AMARELO)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Física", "Efeito", "fotoelétrico", "do zero")


def d(c):  # o macete: Ec = hf − W
    escuro(c)
    E.escreve(c, "a conta do troco", 84, 330, 120, "i", BR)
    E.formula(c, "Ec = h · f − W", 76, 560, 200, "g", BR)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "a frequência decide se sai", 84, 800, 90, "g", AMARELO)
    E.escreve(c, "a intensidade, quantos", 84, 930, 90, "i", claro)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_luz_fraca_vence", a), ("capa_B_efeito_fotoeletrico", b), ("capa_C_conta_do_troco", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
