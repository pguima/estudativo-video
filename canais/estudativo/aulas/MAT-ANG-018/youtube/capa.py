"""Capas do MAT-ANG-018 (1280x720). Uso: python capa.py"""
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
U = 150
B, C = (120, 860), (120 + 5 * U, 860)
Hh = (120 + 1.8 * U, 860)
A = (Hh[0], 860 - 2.4 * U)


def figura(c, tinta=BR, alt=AMARELO, meio=False):
    for P, Q in ((B, C), (C, A), (A, B)):
        M.line(c, *P, *Q, tinta, 1, 12)
    M.line(c, *A, *Hh, alt, 1, 12)
    if meio:
        mx = (B[0] + C[0]) / 2
        M.line(c, mx, 860, mx, 860 - 2.5 * U, VERMELHO, 1, 8, dash=[22, 16])
    E.escreve(c, "3", 150, 680, 90, "g", tinta)
    E.escreve(c, "4", 640, 680, 90, "g", tinta)
    E.escreve(c, "5", (B[0] + C[0]) / 2 - 25, 970, 90, "g", tinta)


def a(c):  # o gancho: 2,5? não, 2,4
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    figura(c, meio=True)
    E.escreve(c, "h", Hh[0] + 20, 760, 100, "g", AMARELO)
    E.escreve(c, "2,5?", 1000, 430, 150, "g", LILAS)
    M.line(c, 980, 390, 1340, 330, VERMELHO, 1, 16)
    E.escreve(c, "a altura é", 1000, 640, 110, "i", BR)
    E.escreve(c, "2,4", 1000, 880, 240, "g", AMARELO)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Relações", "métricas", "a altura e os pedaços")


def d(c):  # o atalho: guarde o 2,4
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "guarde o", 110, 380, 120, "i", BR)
    E.escreve(c, "3, 4, 5 → 2,4", 110, 560, 150, "g", AMARELO)
    E.escreve(c, "6, 8, 10 → 4,8", 110, 740, 110, "g", claro)
    E.escreve(c, "30, 40, 50 → 24", 110, 900, 110, "g", claro)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_nao_e_2_e_meio", a), ("capa_B_relacoes_metricas", b), ("capa_C_guarde_o_2_4", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
