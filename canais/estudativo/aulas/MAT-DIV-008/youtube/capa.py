"""Capas do MAT-DIV-008 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: a conta certa no problema errado
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "acertou a conta,", 84, 400, 150, "i", BR)
    E.escreve(c, "errou a", 84, 640, 230, "g", BR)
    E.escreve(c, "escolha", 84, 860, 230, "g", AMARELO)
    E.escreve(c, "MMC ou MDC?", 1000, 880, 130, "i", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Exercícios", "MMC e MDC", "pause e resolva")


def d(c):  # o atalho: a régua
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "a régua", 84, 370, 190, "i", BR)
    E.escreve(c, "MDC", 84, 600, 190, "g", AMARELO)
    E.escreve(c, "nunca passa do menor", 600, 590, 100, "i", BR)
    E.escreve(c, "MMC", 84, 840, 190, "g", AMARELO)
    E.escreve(c, "nunca fica abaixo do maior", 600, 830, 100, "i", BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_errou_a_escolha", a), ("capa_B_exercicios", b), ("capa_C_regua", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
