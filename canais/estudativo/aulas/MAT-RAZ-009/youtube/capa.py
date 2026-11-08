"""Capas do MAT-RAZ-009 (1280x720). Uso: python capa.py"""
import subprocess, sys
from pathlib import Path
RAIZ = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(RAIZ / "_ferramentas"))
import skia
import editorial as E
import motor as M
BR = "#FFFFFF"
COR = E.MATERIAS["Matemática"]["cor"]


def tabela(c, xs, y, nomes, linhas, size, cor_n, cor_v):
    for x, nome, (v1, v2) in zip(xs, nomes, linhas):
        E.centro(c, nome, x, y, 60, "i", cor_n)
        M.line(c, x - 150, y + 30, x + 150, y + 30, cor_n, 0.6, 4)
        E.centro(c, v1, x, y + 190, size, "g", cor_v)
        E.centro(c, v2, x, y + 360, size, "g", cor_v)


def a(c):  # o erro: mais gente, mais horas e mais dias?
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    tabela(c, (290, 620, 950), 320, ("operários", "horas/dia", "dias"), (("12", "18"), ("8", "10"), ("15", "28?")), 150, BR, BR)
    E.risco(c, 820, 690, 1100, 585, 9, 0, "#FFD500", 26)
    E.escreve(c, "mais gente,", 1180, 520, 100, "i", BR)
    E.escreve(c, "mais dias?", 1180, 680, 120, "g", BR)
    E.escreve(c, "não!", 1180, 860, 160, "g", "#FFD500")


def b(c):  # o modelo
    E.capa_modelo(c, "Matemática", "Regra", "de três", "composta inversa")


def d(c):  # o atalho: homem-hora numa linha
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "o atalho", 84, 340, 140, "i", BR)
    E.escreve(c, "homem-hora", 76, 560, 210, "g", BR)
    cl = E.mix(COR, BR, 0.55)
    E.formula(c, "12 · 8 · 15 = 18 · 10 · x", 84, 800, 120, "g", cl)
    E.formula(c, "x = 8", 84, 960, 120, "g", BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_mais_dias_nao", a), ("capa_B_composta_inversa", b), ("capa_C_homem_hora", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
