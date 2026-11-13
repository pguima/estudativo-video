"""Capas da QUI-ELE-008 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: mais caro que o ouro
    base(c)
    Q.atomo(c, 1420, 540, 260, "Al")
    E.escreve(c, "já foi mais caro", 84, 420, 120, "g", BR)
    E.escreve(c, "que o ouro", 84, 580, 150, "g", AMARELO)
    E.escreve(c, "até a eletrólise", 84, 760, 120, "g", BR)
    E.escreve(c, "eletrólise ígnea", 84, 950, 80, "i", BR)


def b(c):
    E.capa_modelo(c, "Química", "Eletrólise", "ígnea", "do zero")


def d(c):  # o macete: cátion vai ao cátodo
    palco_capa(c)
    E.escreve(c, "o macete dos polos", 84, 300, 110, "i", BR)
    for k, (w1, w2, cor, n) in enumerate((("Cátion", "Cátodo", "#B8A1FF", 3), ("Ânion", "Ânodo", "#7EE08A", 2))):
        y = 560 + 250 * k
        E.escreve(c, w1[:n], 84, y, 170, "g", cor); E.escreve(c, w1[n:], 84 + E.larg(w1[:n], "g", 170) + 4, y, 170, "g", BR)
        E.escreve(c, "→", 700, y, 150, "g", BR)
        E.escreve(c, w2[:n], 900, y, 170, "g", cor); E.escreve(c, w2[n:], 900 + E.larg(w2[:n], "g", 170) + 4, y, 170, "g", BR)


salvar((("capa_A_mais_caro_que_o_ouro", a), ("capa_B_eletrolise_ignea", b), ("capa_C_cation_catodo", d)))
