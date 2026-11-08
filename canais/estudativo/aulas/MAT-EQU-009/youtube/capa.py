"""Capas do MAT-EQU-009 (1280x720). Uso: python capa.py"""
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


def palco(c):
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)


def a(c):  # o gancho: o x some e sobra 1 = 3
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "o x sumiu?", 84, 400, 210, "g", BR)
    s = 190
    E.formula(c, "2x + 1 = 2x + 3", 84, 680, s, cor=BR)
    for x0 in (84, 84 + E.larg("2x + 1 = ", "g", s) + E.APERTO["g"] * s):
        E.risco(c, x0 - 10, 700, x0 + E.larg("2x", "g", s) + 10, 540, 9, 0, AMARELO, 22)
    E.formula(c, "1 = 3", 84, 940, 210, cor=AMARELO)
    E.escreve(c, "e agora?", 720, 930, 150, "i", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Equação com", "parênteses", "do jeito certo")


def d(c):  # o macete: olhe o número do x
    palco(c)
    E.escreve(c, "o atalho", 84, 360, 150, "i", BR)
    E.escreve(c, "o x vai sumir?", 76, 580, 200, "g", BR)
    E.formula(c, "2x + 1 = 2x + 3", 84, 820, 170, cor=AMARELO)
    E.escreve(c, "olhe o número do x", 84, 990, 110, "i", BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_o_x_sumiu", a), ("capa_B_equacao_parenteses", b), ("capa_C_atalho_x_some", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
