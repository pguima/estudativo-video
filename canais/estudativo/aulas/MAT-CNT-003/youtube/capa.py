"""Capas do MAT-CNT-003 (1280x720). Uso: python capa.py"""
import subprocess, sys
from pathlib import Path
RAIZ = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(RAIZ / "_ferramentas"))
import skia
import editorial as E
import motor as M
BR = "#FFFFFF"
AMARELO = "#FFD500"
COR = E.MATERIAS["Matemática"]["cor"]


def caixa(c, cx, cy, s, txt, cor_txt, borda=BR, fundo=None):
    r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - s / 2, cy - s / 2, s, s), s * 0.12, s * 0.12)
    if fundo:
        c.drawRRect(r, M.paint(fundo))
    c.drawRRect(r, M.paint(borda, 1, stroke=8))
    size = s * (0.56 if len(txt) == 1 else 0.46)
    E.centro(c, txt, cx, cy + size * 0.36, size, "g", cor_txt)


def a(c):  # o gancho: 72 tem 12 divisores, sem listar
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "quantos divisores", 84, 360, 120, "i", BR)
    E.escreve(c, "tem o 72?", 84, 600, 220, "g", BR)
    E.bola(c, 1520, 620, 250, "#FFFFFF")
    E.centro(c, "12", 1520, 620 + 80, 220, "g", COR)
    E.escreve(c, "sem listar nenhum", 84, 900, 120, "i", AMARELO)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Contar", "divisores", "sem listar")


def d(c):  # o macete: some 1 em cada expoente
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.formula(c, "72 = 2^3 · 3^2", 84, 400, 180, "g", BR)
    E.escreve(c, "some 1 em cada expoente", 84, 560, 100, "i", BR)
    caixa(c, 200, 790, 200, "4", BR, fundo="#1A1640")
    E.centro(c, "×", 375, 790 + 30, 80, "g", BR)
    caixa(c, 550, 790, 200, "3", BR, fundo="#1A1640")
    E.escreve(c, "= 12", 720, 860, 200, "g", AMARELO)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_72_tem_12", a), ("capa_B_contar_divisores", b), ("capa_C_some_1", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
