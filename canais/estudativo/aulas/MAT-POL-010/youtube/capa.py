"""Capas do MAT-POL-010 (1280x720). Uso: python capa.py"""
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
FURO = "#1B1B24"


def papel(c, x, y, w, h, cor=BR, sombra=True):
    if sombra:
        s = skia.Paint(AntiAlias=True, Color=M.hexc("#000000", 0.3))
        s.setMaskFilter(skia.MaskFilter.MakeBlur(skia.kNormal_BlurStyle, 14))
        c.drawRect(skia.Rect.MakeXYWH(x + 8, y + 14, w, h), s)
    c.drawRect(skia.Rect.MakeXYWH(x, y, w, h), M.paint(cor))


def a(c):  # o gancho: dobre duas vezes, 1 furo vira 4
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    # a folha dobrada (4 camadas) com um furo
    for k in range(4):
        papel(c, 130 + (3 - k) * 10, 330 + (3 - k) * 10, 250, 200, BR if k % 2 == 0 else "#E4E4EE", sombra=(k == 0))
    c.drawCircle(255, 430, 34, M.paint(FURO))
    E.escreve(c, "1 furo", 150, 680, 90, "g", BR)
    M.arrow(c, 450, 440, 600, 440, AMARELO, 1, 12, 40)
    # a folha aberta com 4 furos
    x, y, w, h = 650, 230, 520, 420
    papel(c, x, y, w, h)
    M.line(c, x + w / 2, y, x + w / 2, y + h, COR, 1, 6, dash=[18, 12])
    M.line(c, x, y + h / 2, x + w, y + h / 2, COR, 1, 6, dash=[18, 12])
    for fx in (x + w / 4, x + 3 * w / 4):
        for fy in (y + h / 4, y + 3 * h / 4):
            c.drawCircle(fx, fy, 34, M.paint(FURO))
    E.escreve(c, "4 furos!", 680, 820, 150, "g", AMARELO)
    E.escreve(c, "dobradura", 1260, 400, 110, "i", BR)
    E.escreve(c, "sem", 1260, 540, 110, "i", BR)
    E.escreve(c, "desenhar", 1260, 680, 110, "g", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Simetria", "e dobradura", "eixo por eixo")


def d(c):  # o atalho: regular tem tantos eixos quanto lados
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    claro = E.mix(COR, BR, 0.5)
    cx, cy, r = 1430, 560, 330
    ini = 90 - 30
    pts = [(cx + r * math.cos(math.radians(ini + 60 * k)), cy + r * math.sin(math.radians(ini + 60 * k))) for k in range(6)]
    path = skia.Path(); path.addPoly(pts, True)
    c.drawPath(path, M.paint(BR, 0.08))
    for k in range(6):
        g = math.radians(ini + k * 30)
        dx, dy = 1.15 * r * math.cos(g), 1.15 * r * math.sin(g)
        M.line(c, cx - dx, cy - dy, cx + dx, cy + dy, AMARELO if k % 2 == 0 else claro, 1, 7, dash=[20, 12])
    pa = M.paint(BR, 1, stroke=12); pa.setStrokeJoin(skia.Paint.kRound_Join)
    c.drawPath(path, pa)
    E.escreve(c, "o atalho", 90, 360, 130, "i", BR)
    E.escreve(c, "eixos =", 90, 560, 170, "g", BR)
    E.escreve(c, "lados", 90, 740, 170, "g", AMARELO)
    E.escreve(c, "no polígono regular", 90, 900, 80, "i", claro)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_um_furo_quatro", a), ("capa_B_simetria_e_dobradura", b), ("capa_C_eixos_iguais_lados", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
