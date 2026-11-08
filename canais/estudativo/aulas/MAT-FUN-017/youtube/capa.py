"""Capas do MAT-FUN-017 (1280x720). Uso: python capa.py"""
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


def mini(c, x, y, w, h, fn, cor, raizes=(), ymin=-2, ymax=5, largura=11):
    """eixos simples na caixa, x de −0,5 a 4,5, com a curva fn e as raízes marcadas"""
    X = lambda v: x + (v + 0.5) / 5 * w
    Y = lambda v: y + h - (v - ymin) / (ymax - ymin) * h
    M.arrow(c, x, Y(0), x + w + 26, Y(0), BR, 1, 6, 22)
    M.arrow(c, X(0), y + h, X(0), y - 26, BR, 1, 6, 22)
    pa = skia.Path()
    for i in range(201):
        v = -0.5 + 5 * i / 200
        (pa.lineTo if i else pa.moveTo)(X(v), Y(fn(v)))
    c.save(); c.clipRect(skia.Rect.MakeXYWH(x - 10, y - 10, w + 20, h + 20))
    c.drawPath(pa, M.paint(cor, 1, stroke=largura, cap_round=True))
    c.restore()
    for r in raizes:
        c.drawCircle(X(r), Y(0), 22, M.paint(AMARELO, 1, stroke=8))
    return X, Y


def a(c):  # o gancho: corta, encosta ou nem chega perto
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "corta, encosta", 84, 400, 140, "g", BR)
    E.escreve(c, "ou nem toca?", 84, 570, 140, "g", BR)
    for i, (fn, rz, rot) in enumerate(((lambda v: v * v - 4 * v + 3, (1, 3), "Δ > 0"), (lambda v: v * v - 4 * v + 4, (2,), "Δ = 0"),
                                        (lambda v: v * v - 4 * v + 5, (), "Δ < 0"))):
        x = 140 + i * 590
        mini(c, x, 680, 440, 300, fn, BR, rz)
        E.pilula(c, rot, x + 330, 720, 46, "g", fundo=AMARELO if i < 2 else VERMELHO, cor=COR if i < 2 else BR)


def b(c):  # o modelo
    E.capa_modelo(c, "Matemática", "Raízes da", "parábola", "onde corta o x")


def d(c):  # o atalho: a e c com sinais contrários
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "a e c com sinais", 84, 400, 120, "i", claro)
    E.escreve(c, "contrários", 76, 600, 190, "g", BR)
    E.escreve(c, "corta 2 vezes, sem conta", 84, 800, 90, "i", AMARELO)
    X, Y = mini(c, 1240, 230, 560, 640, lambda v: v * v - 3 * v - 1.2, claro, ((3 - 13.8 ** 0.5) / 2, (3 + 13.8 ** 0.5) / 2), ymin=-4, ymax=6)
    c.drawCircle(X(0), Y(-1.2), 22, M.paint(BR))


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_corta_encosta_ou_nem_toca", a), ("capa_B_raizes_da_parabola", b), ("capa_C_sinais_contrarios", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
