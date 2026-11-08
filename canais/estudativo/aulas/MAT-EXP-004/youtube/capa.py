"""Capas do MAT-EXP-004 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: 9^x = 27 sem número inteiro
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.formula(c, "9^x = 27", 84, 470, 250, "g", BR)
    E.escreve(c, "nenhum inteiro serve...", 84, 680, 84, "i", BR)
    E.formula(c, "x = f{3}{2}", 1180, 540, 220, "g", AMARELO)


def b(c):  # o modelo
    E.capa_modelo(c, "Matemática", "Equação", "exponencial", "igualar as bases")


def d(c):  # o atalho: desça até o primo
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "o atalho:", 84, 360, 120, "i", claro)
    E.escreve(c, "desça até", 76, 580, 190, "g", BR)
    E.escreve(c, "o primo", 76, 790, 190, "g", AMARELO)
    E.formula(c, "9 = 3^2", 1250, 520, 110, "g", BR)
    E.formula(c, "27 = 3^3", 1250, 720, 110, "g", BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_9x_27", a), ("capa_B_equacao_exponencial", b), ("capa_C_desca_ate_o_primo", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
