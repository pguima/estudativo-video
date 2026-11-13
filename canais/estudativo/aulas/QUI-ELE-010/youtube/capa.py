"""Capas da QUI-ELE-010 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: sem pesar nada
    base(c)
    E.pilula(c, "10 A", 300, 340, 90, "g", fundo="#1F6FEB")
    E.pilula(c, "1.930 s", 760, 340, 90, "g", fundo="#22232B")
    E.escreve(c, "quanto cobre", 84, 620, 140, "g", BR)
    E.escreve(c, "grudou?", 84, 790, 160, "g", AMARELO)
    E.bola(c, 1480, 640, 240, "#B5532A")
    E.centro(c, "6,35 g", 1480, 690, 120, "g", BR)
    E.escreve(c, "sem pesar nada", 84, 960, 80, "i", BR)


def b(c):
    E.capa_modelo(c, "Química", "Leis de", "Faraday", "do zero")


def d(c):  # o macete: a fração de 96.500
    palco_capa(c)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "o macete dos 96.500", 84, 300, 110, "i", BR)
    E.formula(c, "19.300 C = 1/5", 84, 540, 150, "g", BR)
    E.formula(c, "= 0,2 mol de e⁻", 84, 740, 130, "g", AMARELO)
    E.escreve(c, "achou a fração, achou os mols", 84, 930, 72, "i", claro)


salvar((("capa_A_sem_pesar_nada", a), ("capa_B_leis_de_faraday", b), ("capa_C_fracao_de_96500", d)))
