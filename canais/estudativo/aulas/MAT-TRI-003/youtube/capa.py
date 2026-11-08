"""Capas do MAT-TRI-003 (1280x720). Uso: python capa.py"""
import math, subprocess, sys
from pathlib import Path
RAIZ = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(RAIZ / "_ferramentas"))
import skia
import editorial as E
import motor as M
BR = "#FFFFFF"
AM = "#FFD500"
COR = E.MATERIAS["Matemática"]["cor"]
VAL = (("f{1}{2}", "f{r{2}}{2}", "f{r{3}}{2}"), ("f{r{3}}{2}", "f{r{2}}{2}", "f{1}{2}"), ("f{r{3}}{3}", "1", "r{3}"))


def tabela(c, x0, y0, cw, rh, cor, linha_cor, size=80, destaque=None):
    for j in range(4):
        M.line(c, x0 + j * cw, y0 - 80, x0 + j * cw, y0 + 40 + 3 * rh, linha_cor, 1.0, 3)
    for i in range(3):
        M.line(c, x0 - 170, y0 + 40 + i * rh, x0 + 3 * cw, y0 + 40 + i * rh, linha_cor, 1.0, 3)
    for j, g in enumerate((30, 45, 60)):
        E.formula(c, f"{g}°", x0 + cw * (j + 0.5), y0, 70, "g", cor, 1.0, "center")
    for i, nome in enumerate(("sen", "cos", "tg")):
        E.escreve(c, nome, x0 - 160, y0 + 40 + (i + 0.5) * rh + 28, 76, "g", cor)
        for j in range(3):
            s = VAL[i][j]
            E.formula(c, s, x0 + cw * (j + 0.5), y0 + 40 + (i + 0.5) * rh + size * (0.3 if "f{" in s else 0.36), size, "g",
                      AM if destaque and (i, j) in destaque else cor, 1.0, "center")


def a(c):  # o gancho: a tabela inteira de cabeça
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "a tabela", 84, 340, 150, "g", BR)
    E.escreve(c, "de cabeça", 84, 500, 130, "i", AM)
    E.escreve(c, "em poucos segundos", 84, 640, 80, "i", BR)
    tabela(c, 1050, 220, 250, 230, BR, E.mix(COR, BR, 0.45), 76, {(0, 0), (1, 1), (2, 2)})


def b(c):  # o modelo
    E.capa_modelo(c, "Matemática", "Ângulos", "notáveis", "30°, 45° e 60°")


def d(c):  # o macete: √1, √2, √3 sobre 2
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "o macete", 84, 300, 130, "i", BR)
    E.escreve(c, "do seno", 84, 480, 180, "g", BR)
    for j, s in enumerate(("f{r{1}}{2}", "f{r{2}}{2}", "f{r{3}}{2}")):
        E.formula(c, s, 300 + j * 420, 900, 170, "g", AM, 1.0, "center")
    for j, g in enumerate((30, 45, 60)):
        E.formula(c, f"{g}°", 300 + j * 420, 630, 70, "g", E.mix(COR, BR, 0.6), 1.0, "center")


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_tabela_de_cabeca", a), ("capa_B_angulos_notaveis", b), ("capa_C_macete_do_seno", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
