"""Capas do MAT-FUN-023 (1280x720). Uso: python capa.py"""
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
VERDE = "#2BD487"


def bolinha(c, cx, cy, s, cor, r=44):
    c.drawCircle(cx, cy, r, M.paint(cor))
    E.centro(c, s, cx, cy + 25, 76, "g", BR)


def a(c):  # o gancho: não passe multiplicando
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.formula(c, "f{(x − 1)(x + 2)}{x − 3} ≥ 0", 84, 420, 110, "g", BR)
    E.escreve(c, "× (x − 3)?", 84, 700, 150, "g", VERMELHO)
    M.line(c, 70, 730, 820, 580, VERMELHO, 1, 16)
    E.escreve(c, "o sinal pode virar", 84, 880, 80, "i", AMARELO)
    # mini quadro de sinais à direita
    x0, y0 = 1180, 300
    for i, sgs in enumerate((("−", "+", "+", "+"), ("−", "−", "+", "+"), ("−", "−", "−", "+"))):
        for j, s in enumerate(sgs):
            bolinha(c, x0 + j * 160, y0 + i * 130, s, VERDE if s == "+" else VERMELHO, 38)
    M.line(c, x0 - 60, y0 + 330, x0 + 540, y0 + 330, BR, 0.8, 4)
    for j, s in enumerate(("−", "+", "−", "+")):
        bolinha(c, x0 + j * 160, y0 + 420, s, VERDE if s == "+" else VERMELHO, 48)


def b(c):  # o modelo
    E.capa_modelo(c, "Matemática", "Quadro", "de sinais", "produto e quociente")


def d(c):  # o atalho: depois da maior raiz, tudo +; troca a cada raiz
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "sem quadro:", 84, 360, 100, "i", claro)
    E.escreve(c, "troca a cada raiz", 84, 530, 140, "g", BR)
    E.escreve(c, "depois da maior: tudo +", 84, 660, 72, "i", AMARELO)
    y, x0, x1 = 930, 160, 1760
    M.arrow(c, x0, y, x1, y, BR, 1, 6, 22)
    xs = [x0 + (x1 - x0) * k / 4 for k in (1, 2, 3)]
    for xv in xs:
        M.line(c, xv, y - 22, xv, y + 22, BR, 1, 6)
    cs = [(x0 + xs[0]) / 2, (xs[0] + xs[1]) / 2, (xs[1] + xs[2]) / 2, (xs[2] + x1) / 2]
    for cx, s in zip(cs, ("−", "+", "−", "+")):
        bolinha(c, cx, y - 80, s, VERDE if s == "+" else VERMELHO, 40)
    for j in (3, 2, 1):
        mid, r = (cs[j] + cs[j - 1]) / 2, (cs[j] - cs[j - 1]) / 2 * 0.45
        E.arco(c, mid, y - 110, r, 0, -180, AMARELO, 6)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_nao_passe_multiplicando", a), ("capa_B_quadro_de_sinais", b), ("capa_C_troca_a_cada_raiz", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
