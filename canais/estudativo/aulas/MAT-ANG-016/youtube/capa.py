"""Capas do MAT-ANG-016 (1280x720). Uso: python capa.py"""
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


def triangulo(c, R, u, b, h, tinta=BR, hip=AMARELO):
    """reto em R, base b para a direita, altura h para cima (em unidades u)"""
    P, T = (R[0] + b * u, R[1]), (R[0], R[1] - h * u)
    M.line(c, *R, *P, tinta, 1, 14)
    M.line(c, *R, *T, tinta, 1, 14)
    M.line(c, *T, *P, hip, 1, 16)
    q = 50
    M.line(c, R[0] + q, R[1], R[0] + q, R[1] - q, tinta, 1, 7)
    M.line(c, R[0], R[1] - q, R[0] + q, R[1] - q, tinta, 1, 7)
    return P, T


def a(c):  # o gancho: 30 e 40 dão 50 sem conta
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    triangulo(c, (230, 900), 15, 40, 30)
    E.escreve(c, "30", 90, 760, 100, "g", BR)
    E.escreve(c, "40", 460, 1020, 100, "g", BR)
    E.escreve(c, "50", 560, 650, 140, "g", AMARELO)
    E.escreve(c, "sem", 1080, 420, 150, "i", BR)
    E.escreve(c, "conta!", 1060, 600, 190, "g", BR)
    E.escreve(c, "3, 4, 5 × 10", 1070, 820, 110, "g", AMARELO)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Ternos", "pitagóricos", "3, 4, 5 e 5, 12, 13")


def d(c):  # o atalho: medidas com vírgula
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "escada com vírgula?", 110, 360, 100, "i", BR)
    E.escreve(c, "2,5 e 1,5", 110, 540, 150, "g", claro)
    E.escreve(c, "× 2 → 5 e 3 → 4", 110, 730, 120, "g", BR)
    E.escreve(c, "÷ 2 = 2 m", 110, 920, 150, "g", AMARELO)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_sem_conta", a), ("capa_B_ternos_pitagoricos", b), ("capa_C_virgula_vezes_dois", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
