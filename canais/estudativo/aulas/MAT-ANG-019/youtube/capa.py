"""Capas do MAT-ANG-019 (1280x720). Uso: python capa.py"""
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
LILAS = "#C9C9FF"
VERMELHO = "#FF6B6B"


def mesa(c, cor_regua=AMARELO, tinta=BR):
    x, y, l = 170, 330, 500
    c.drawRect(skia.Rect.MakeXYWH(x, y, l, l), M.paint(tinta, 1, stroke=12))
    M.line(c, x, y + l, x + l, y, LILAS, 1, 6, dash=[24, 16])
    # régua de 120 sobre diagonal de 80√2 ≈ 113: passa um pouco das pontas
    k = 120 / (80 * 2 ** 0.5)
    cx, cy = x + l / 2, y + l / 2
    dx = l / 2 * k
    P0, P1 = (cx - dx - 14, cy + dx - 14), (cx + dx - 14, cy - dx - 14)
    M.line(c, *P0, *P1, cor_regua, 1, 30)
    for P in (P0, P1):
        c.drawCircle(*P, 38, M.paint(VERMELHO, 1, stroke=9))
    E.escreve(c, "80 cm", x + l / 2 - 120, y + l + 110, 90, "g", tinta)


def a(c):  # o gancho: a régua cabe?
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    mesa(c)
    E.escreve(c, "régua de 120 cm", 900, 420, 100, "g", BR)
    E.escreve(c, "cabe?", 900, 640, 230, "g", AMARELO)
    E.escreve(c, "5 situações", 900, 840, 110, "i", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Pitágoras", "na prática", "5 situações resolvidas")


def d(c):  # o atalho: compare os quadrados
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "sem raiz:", 110, 380, 120, "i", BR)
    E.escreve(c, "compare os quadrados", 110, 540, 120, "g", BR)
    E.formula(c, "120^2 > 80^2 + 80^2", 110, 760, 120, "g", AMARELO)
    E.escreve(c, "14.400 > 12.800", 110, 930, 100, "g", claro)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_a_regua_cabe", a), ("capa_B_pitagoras_na_pratica", b), ("capa_C_compare_os_quadrados", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
