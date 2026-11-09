"""Capas do FIS-MOD-003 (1280x720). Uso: python capa.py"""
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
def cor_luz(nm):
    pts = ((380, (0.55, 0.0, 0.9)), (440, (0.25, 0.1, 1.0)), (490, (0.0, 0.65, 1.0)), (510, (0.0, 0.85, 0.35)),
           (580, (1.0, 0.9, 0.0)), (620, (1.0, 0.45, 0.0)), (660, (0.95, 0.1, 0.05)), (750, (0.6, 0.0, 0.0)))
    for (a_, ca), (b_, cb) in zip(pts, pts[1:]):
        if nm <= b_:
            f = (nm - a_) / (b_ - a_)
            r, g, bb = (ca[i] + (cb[i] - ca[i]) * f for i in range(3))
            return "#%02X%02X%02X" % (int(r * 255), int(g * 255), int(bb * 255))


def faixa(c, x, y, w, h, emissao):
    M.rrect(c, x, y, w, h, 10, "#101015")
    if not emissao:
        for i in range(150):
            M.rrect(c, x + w * i / 150, y, w / 150 + 1, h, 0, cor_luz(400 + 2 * i))
    for nm in (410, 434, 486, 656):
        M.rrect(c, x + w * (nm - 400) / 300 - 7, y, 14, h, 0, cor_luz(nm) if emissao else "#101015")


def a(c):  # o gancho: o hélio no Sol
    E.capa_base(c, COR); E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "do que o Sol", 84, 390, 150, "i", BR)
    E.escreve(c, "é feito?", 76, 600, 220, "g", BR)
    faixa(c, 84, 760, 1000, 130, False)
    E.escreve(c, "a pista está nas linhas", 84, 990, 80, "g", AMARELO)
    E.orbita(c, 1560, 470, 260, E.mix(COR, BR, 0.82))


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Física", "Espectros", "e níveis", "do zero")


def d(c):  # o macete: quantas linhas
    escuro(c)
    E.escreve(c, "quantas linhas?", 84, 330, 120, "i", BR)
    E.formula(c, "f{n · (n − 1)}{2}", 120, 640, 190, "g", BR)
    for k, y in enumerate((1000, 760, 640, 580)):
        M.line(c, 1150, y, 1700, y, BR, 1.0, 8)
    for k, (y0, y1) in enumerate(((580, 640), (580, 760), (580, 1000), (640, 760), (640, 1000), (760, 1000))):
        F.seta(c, 1190 + 90 * k, y0 + 6, 1190 + 90 * k, y1 - 6, AMARELO, 1.0, 9)
    E.escreve(c, "n = 4: 6 linhas", 84, 940, 100, "g", AMARELO)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_do_que_o_sol_e_feito", a), ("capa_B_espectros_e_niveis", b), ("capa_C_quantas_linhas", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
