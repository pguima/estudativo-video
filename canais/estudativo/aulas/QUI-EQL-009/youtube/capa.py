"""Capas da QUI-EQL-009 (1280x720). Uso: python capa.py"""
import subprocess, sys
from pathlib import Path
RAIZ = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(RAIZ / "_ferramentas"))
import skia
import editorial as E
import quimica as Q
import motor as M
BR = "#FFFFFF"
AMARELO = "#FFD500"
COR = E.MATERIAS["Química"]["cor"]
E.usar("Química")


def escuro(c):
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Química", COR)


NOMES = ("capa_A_um_numero_so", "capa_B_calcular_kc", "capa_C_quadro_tres_linhas")


def a(c):  # o gancho: um número só e o Kc sai
    E.capa_base(c, COR); E.capa_rotulo(c, "Química", COR)
    E.escreve(c, "você mede", 84, 360, 120, "i", BR)
    E.escreve(c, "um número só", 84, 570, 180, "g", AMARELO)
    E.escreve(c, "e acha o Kc", 84, 780, 180, "g", BR)
    E.escreve(c, "o quadro de 3 linhas", 84, 990, 84, "i", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Química", "Calcular", "o Kc", "passo a passo")


def d(c):  # o macete: início, reage, equilíbrio
    escuro(c)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "o quadro", 84, 320, 120, "i", BR)
    for k, (s, v) in enumerate((("início", "1   1   0"), ("reage", "−0,8  −0,8  +1,6"), ("equilíbrio", "0,2  0,2  1,6"))):
        E.escreve(c, s, 84, 520 + k * 170, 110, "g", claro if k == 2 else BR)
        E.formula(c, v, 900, 520 + k * 170, 100, "g", claro if k == 2 else BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in zip(NOMES, (a, b, d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
