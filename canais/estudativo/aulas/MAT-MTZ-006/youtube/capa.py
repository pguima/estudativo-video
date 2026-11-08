"""Capas do MAT-MTZ-006 (1280x720). Uso: python capa.py"""
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


def chave(c, x, y0, y1, s, cor):
    meio, k = (y0 + y1) / 2, s * 0.32
    p = skia.Path()
    p.moveTo(x, y0); p.cubicTo(x - k, y0, x - k * 0.2, meio - k, x - k, meio)
    p.cubicTo(x - k * 0.2, meio + k, x - k, y1, x, y1)
    c.drawPath(p, M.paint(cor, 1, stroke=max(5, s * 0.07), cap_round=True))


def escada(c, x, y, w, h, cor):
    p = skia.Path()
    dx = w / 5
    p.moveTo(x, y)
    for i in range(3):
        p.lineTo(x + i * dx, y + (i + 1) * h / 3)
        if i < 2:
            p.lineTo(x + (i + 1) * dx, y + (i + 1) * h / 3)
    p.lineTo(x + w, y + h); p.lineTo(x + w, y); p.close()
    c.drawPath(p, M.paint(cor, 0.16))
    pt = M.paint(cor, 1, stroke=6)
    pt.setPathEffect(skia.DashPathEffect.Make([16, 12], 0))
    c.drawPath(p, pt)


def a(c):  # o gancho: 3 equações, 3 letras
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    s = 100
    chave(c, 150, 230, 650, s, BR)
    for i, l in enumerate(("x + y + z = 6", "x + 2y + z = 8", "x + y + 2z = 9")):
        E.escreve(c, l, 190, 330 + i * 140, s, "g", BR)
    escada(c, 1150, 230, 650, 420, AMARELO)
    E.escreve(c, "vira escada", 1170, 760, 110, "g", AMARELO)
    E.escreve(c, "3 equações, 3 letras: sem medo", 84, 960, 90, "i", BR)


def b(c):  # o modelo
    E.capa_modelo(c, "Matemática", "Sistema 3x3", "escalonado", "passo a passo")


def d(c):  # o atalho: teste os trios
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "tem alternativas?", 84, 380, 130, "i", BR)
    E.escreve(c, "teste os trios", 76, 590, 200, "g", BR)
    for n, (txt, ok) in enumerate((("(1, 2, 3)", True), ("(2, 1, 3)", False))):
        E.escreve(c, txt, 120 + n * 900, 860, 140, "g", BR)
        E.selo(c, 720 + n * 900, 815, 60, ok)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_vira_escada", a), ("capa_B_sistema_3x3", b), ("capa_C_teste_os_trios", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
