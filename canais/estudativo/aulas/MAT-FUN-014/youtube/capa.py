"""Capas do MAT-FUN-014 (1280x720). Uso: python capa.py"""
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
VERDE = "#3BE08A"


def grafico(c, x, y, w, h, claro):
    """custo (sai do alto do eixo) e receita (sai da origem) cruzando no meio; prejuízo antes, lucro depois"""
    M.arrow(c, x, y + h, x + w + 30, y + h, BR, 1, 7, 26)
    M.arrow(c, x, y + h, x, y - 30, BR, 1, 7, 26)
    cx, cy = x + w * 0.5, y + h * 0.45
    c0 = (x, y + h * 0.72)
    r0 = (x, y + h)
    c1 = (x + w, y + h * 0.18)
    r1 = (x + w, y - h * 0.1)
    for pts, cor in (((c0, (cx, cy), r0), VERMELHO), (((cx, cy), r1, c1), VERDE)):
        p = skia.Path(); p.moveTo(*pts[0]); p.lineTo(*pts[1]); p.lineTo(*pts[2]); p.close()
        c.drawPath(p, M.paint(cor, 0.85))
    M.line(c, *c0, *c1, BR, 1, 12)
    M.line(c, *r0, *r1, claro, 1, 12)
    c.drawCircle(cx, cy, 26, M.paint(AMARELO))


def a(c):  # o gancho: sobra 20 por peça e mesmo assim dá prejuízo
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "lucro", 84, 430, 190, "g", BR)
    E.escreve(c, "ou", 84, 600, 140, "i", BR)
    E.escreve(c, "prejuízo?", 76, 800, 190, "g", BR)
    grafico(c, 1180, 300, 600, 560, E.mix(COR, BR, 0.55))


def b(c):  # o modelo
    E.capa_modelo(c, "Matemática", "Custo e", "receita", "o equilíbrio")


def d(c):  # o atalho: custo fixo dividido pelo que sobra em cada peça
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "o equilíbrio", 84, 400, 130, "i", claro)
    E.escreve(c, "numa conta", 76, 600, 190, "g", BR)
    E.formula(c, "f{custo fixo}{sobra por peça}", 84, 880, 110, "g", AMARELO)
    E.formula(c, "f{2.000}{20} = 100", 1100, 880, 130, "g", BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_lucro_ou_prejuizo", a), ("capa_B_custo_e_receita", b), ("capa_C_equilibrio_numa_conta", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
