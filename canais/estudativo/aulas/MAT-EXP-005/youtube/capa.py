"""Capas do MAT-EXP-005 (1280x720). Uso: python capa.py"""
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
VERMELHO = "#FF4D55"


def a(c):  # o gancho: (1/2)^x > 8 não dá x > -3
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.formula(c, "(f{1}{2})^x > 8", 84, 470, 200, "g", BR)
    E.escreve(c, "x > −3", 84, 800, 170, "g", VERMELHO)
    E.risco(c, 70, 760, 84 + E.larg("x > −3", "g", 170) + 20, 720, 1, 0, AMARELO, 24)
    E.escreve(c, "o sinal vira:", 1060, 600, 110, "i", BR)
    E.escreve(c, "x < −3", 1060, 800, 170, "g", AMARELO)


def b(c):  # o modelo
    E.capa_modelo(c, "Matemática", "Inequação", "exponencial", "quando o sinal vira")


def d(c):  # o atalho: fuja da base fração
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "o atalho:", 84, 360, 120, "i", claro)
    E.escreve(c, "fuja da", 76, 580, 190, "g", BR)
    E.escreve(c, "base fração", 76, 790, 190, "g", AMARELO)
    E.formula(c, "(f{1}{2})^x = 2^{−x}", 1180, 980, 90, "g", claro)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_o_sinal_vira", a), ("capa_B_inequacao_exponencial", b), ("capa_C_fuja_da_base_fracao", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
