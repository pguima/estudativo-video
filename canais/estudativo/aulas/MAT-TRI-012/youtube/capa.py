"""Capas do MAT-TRI-012 (1280x720). Uso: python capa.py"""
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
ROSA = "#FF7FC4"
AGUA = "#7FD3DA"


def partes(c, lista, x, y, size):
    for s, cor in lista:
        E.formula(c, s, x, y, size, "g", cor)
        x += E.formula(None, s, 0, 0, size, "g", a=0)


def a(c):  # o gancho: a maré sobe e desce; quando fica alta?
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "a maré", 84, 380, 150, "i", BR)
    E.escreve(c, "alta às", 84, 580, 170, "g", AMARELO)
    E.escreve(c, "que horas?", 84, 770, 170, "g", AMARELO)
    # a água com o nível em onda e a régua
    x0, x1, base = 1200, 1830, 1000
    path = skia.Path(); path.moveTo(x0, base)
    for i in range(121):
        X = x0 + (x1 - x0) * i / 120
        path.lineTo(X, 640 - 110 * math.cos(2 * math.pi * 1.5 * i / 120))
    path.lineTo(x1, base); path.close()
    c.drawPath(path, M.paint(AGUA, 0.85))
    M.line(c, x0 - 40, base, x0 - 40, 360, BR, 1.0, 6)
    for k in range(8):
        Y = base - k * 85
        M.line(c, x0 - 70, Y, x0 - 40, Y, BR, 1.0, 5)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Marés", "e ondas", "fenômenos periódicos")


def d(c):  # o atalho: πt/6 → período 12
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "o atalho", 84, 330, 120, "i", BR)
    partes(c, [("f{πt}{6}", ROSA), ("  →  período ", BR), ("12", AMARELO)], 84, 600, 150)
    partes(c, [("f{πt}{n}", ROSA), ("  →  ", BR), ("2n", AMARELO)], 84, 900, 130)
    x0, w, yc, amp = 1260, 600, 830, 110
    path = skia.Path()
    for i in range(241):
        (path.moveTo if i == 0 else path.lineTo)(x0 + w * i / 240, yc - amp * math.cos(2 * math.pi * 2 * i / 240))
    p = M.paint(AGUA, 1.0, stroke=12, cap_round=True); p.setStrokeJoin(skia.Paint.kRound_Join)
    c.drawPath(path, p)
    E.chave(c, x0, x0 + w / 2, yc - amp - 30, ROSA, 1.0, -30, 8)
    E.formula(c, "12 h", x0 + w / 4, yc - amp - 90, 80, "g", ROSA, 1.0, "center")


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_mare_alta", a), ("capa_B_mares_e_ondas", b), ("capa_C_periodo_2n", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
