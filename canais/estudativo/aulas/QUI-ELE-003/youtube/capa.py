"""Capas da QUI-ELE-003 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: qual placa se gasta?
    base(c)
    M.rrect(c, 900, 160, 960, 820, 40, "#F4F3EF", 1)
    Q.pilha_daniell(c, 100, 0, 1380, 560, te=99, ddp="?", polos=False, w=860)
    E.escreve(c, "qual placa", 84, 420, 140, "g", BR)
    E.escreve(c, "se gasta?", 84, 580, 150, "g", AMARELO)
    E.escreve(c, "a pilha de Daniell", 84, 900, 80, "i", BR)


def b(c):
    E.capa_modelo(c, "Química", "Pilha", "de Daniell", "do zero")


def d(c):  # o macete: vogal com vogal
    palco_capa(c)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "nunca mais troque", 84, 300, 110, "i", BR)
    for k, (p1, p2, cor) in enumerate((("Ânodo", "Oxidação", "#FFB347"), ("Cátodo", "Redução", "#7FB2FF"))):
        y = 540 + 220 * k
        E.escreve(c, p1[0], 84, y, 170, "g", cor); E.escreve(c, p1[1:], 84 + E.larg(p1[0], "g", 170) + 4, y, 170, "g", BR)
        E.escreve(c, p2[0], 900, y, 170, "g", cor); E.escreve(c, p2[1:], 900 + E.larg(p2[0], "g", 170) + 4, y, 170, "g", BR)


salvar((("capa_A_qual_placa_se_gasta", a), ("capa_B_pilha_de_daniell", b), ("capa_C_vogal_com_vogal", d)))
