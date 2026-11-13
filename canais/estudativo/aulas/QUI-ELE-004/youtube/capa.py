"""Capas da QUI-ELE-004 (1280x720). Uso: python capa.py"""
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


def palco_capa(c):
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Química", COR)


def base(c):
    E.capa_base(c, COR); E.capa_rotulo(c, "Química", COR)


def salvar(capas):
    pasta = Path(__file__).parent
    s = skia.Surface(E.W, E.H)
    for nome, fn in capas:
        fn(s.getCanvas())
        tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
        tmp.unlink()


def a(c):  # o gancho: de onde vem o 1,10 V?
    base(c)
    E.bola(c, 1420, 560, 300, "#22232B")
    c.drawCircle(1420, 560, 300, M.paint(BR, 1, stroke=14))
    E.centro(c, "1,10 V", 1420, 620, 170, "g", BR)
    E.escreve(c, "de onde", 84, 440, 150, "g", BR)
    E.escreve(c, "vem esse", 84, 610, 150, "g", BR)
    E.escreve(c, "número?", 84, 780, 150, "g", AMARELO)
    E.escreve(c, "a ddp da pilha", 84, 950, 80, "i", BR)


def b(c):
    E.capa_modelo(c, "Química", "Calcular", "a ddp", "da pilha")


def d(c):  # o macete: maior menos menor
    palco_capa(c)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "a conta em 5 segundos", 84, 300, 110, "i", BR)
    E.escreve(c, "maior − menor", 84, 520, 160, "g", BR)
    E.formula(c, "0,34 − (−0,76)", 84, 740, 120, "g", claro)
    E.formula(c, "= 1,10 V", 84, 920, 140, "g", AMARELO)


salvar((("capa_A_de_onde_vem_o_1_10", a), ("capa_B_calcular_a_ddp", b), ("capa_C_maior_menos_menor", d)))
