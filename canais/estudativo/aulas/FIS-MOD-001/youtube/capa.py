"""Capas do FIS-MOD-001 (1280x720). Uso: python capa.py"""
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
    E.orbita(c, 1600, 330, 230, E.mix(COR, BR, 0.82))
    E.escreve(c, "fóton", 1330, 900, 150, "g", AMARELO)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Física", "Fóton:", "E = h · f", "do zero")


def d(c):  # o macete: joule para elétron-volt
    escuro(c)
    E.escreve(c, "de joule para", 84, 330, 120, "i", BR)
    E.escreve(c, "elétron-volt", 76, 520, 190, "g", BR)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "÷", 90, 800, 200, "g", AMARELO)
    E.formula(c, "1,6 × 10^{−19}", 290, 800, 170, "g", BR)
    E.escreve(c, "e pronto", 90, 990, 110, "i", claro)
    E.selo(c, 1690, 760, 130, True)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_luz_em_pacotes", a), ("capa_B_foton_e_hf", b), ("capa_C_joule_para_eletron_volt", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
