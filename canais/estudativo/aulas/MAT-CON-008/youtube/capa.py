"""Capas do MAT-CON-008 (1280x720). Uso: python capa.py"""
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


def reta(c, x0, x1, y, a, b, fa, fb, vmin=0, vmax=8, cor=BR, tinta=BR, rotulos=True):
    vx = lambda v: x0 + (v - vmin) / (vmax - vmin) * (x1 - x0)
    M.line(c, x0, y, x1, y, tinta, 1.0, 6)
    if rotulos:
        for v in range(vmin, vmax + 1):
            M.line(c, vx(v), y - 16, vx(v), y + 16, tinta, 1.0, 5)
            E.centro(c, str(v), vx(v), y + 70, 50, "b", tinta)
    M.line(c, vx(a), y, vx(b), y, cor, 1.0, 16, cap_round=False)
    for v, f in ((a, fa), (b, fb)):
        c.drawCircle(vx(v), y, 22, M.paint(cor if f else COR))
        c.drawCircle(vx(v), y, 22, M.paint(cor, 1.0, stroke=8))
    return vx


def a(c):  # o gancho: o 3 não pode entrar
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "[1, 5]", 84, 360, 130, "g", BR)
    x = 84 + E.larg("[1, 5]", "g", 130) + 40
    pa = skia.Path()  # o ∩ desenhado: a fonte não tem o símbolo
    pa.moveTo(x, 355); pa.lineTo(x, 300); pa.arcTo(skia.Rect.MakeLTRB(x, 255, x + 74, 329), 180, 180, False); pa.lineTo(x + 74, 355)
    p = M.paint(AMARELO, 1.0, stroke=18); p.setStrokeCap(skia.Paint.kButt_Cap)
    c.drawPath(pa, p)
    E.escreve(c, "]3, 7[", x + 120, 360, 130, "g", BR)
    E.escreve(c, "o 3 entra?", 84, 560, 170, "g", AMARELO)
    vx = reta(c, 760, 1800, 760, 1, 5, True, True, rotulos=False)
    reta(c, 760, 1800, 880, 3, 7, False, False, rotulos=False)
    for v in range(0, 9):
        E.centro(c, str(v), vx(v), 990, 50, "b", BR)
    c.drawCircle(vx(3), 880, 50, M.paint(AMARELO, 1.0, stroke=10))


def b(c):  # o modelo
    E.capa_modelo(c, "Matemática", "União e", "interseção", "de intervalos")


def d(c):  # o atalho
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "maior começo,", 84, 400, 150, "g", BR)
    E.escreve(c, "menor fim", 84, 580, 150, "g", AMARELO)
    E.escreve(c, "a interseção sem desenhar", 84, 820, 90, "i", E.mix(COR, BR, 0.6))


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_o_3_entra", a), ("capa_B_uniao_intersecao_intervalos", b), ("capa_C_maior_comeco_menor_fim", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
