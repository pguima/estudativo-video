"""Capas da QUI-ELE-014 (1280x720). Uso: python capa.py"""
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


def a(c):
    base(c)
    E.escreve(c, "4 questões", 84, 400, 170, "g", BR)
    E.escreve(c, "de eletrólise", 84, 580, 140, "g", AMARELO)
    E.escreve(c, "e radioatividade", 84, 740, 140, "g", AMARELO)
    E.escreve(c, "resolvidas passo a passo", 84, 930, 80, "i", BR)
    for k, s in enumerate(("Q", "e⁻", "α", "½")):
        E.bola(c, 1450 + (k % 2) * 260, 380 + (k // 2) * 300, 115, ("#22232B", "#1F6FEB", "#E07B39", "#0B5D6B")[k])
        E.centro(c, s, 1450 + (k % 2) * 260, 380 + (k // 2) * 300 + 30, 90, "g", BR)


def b(c):
    E.capa_modelo(c, "Química", "Praticando:", "eletrólise", "e radioatividade")


def d(c):
    palco_capa(c)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "a armadilha da meia-vida", 84, 300, 110, "i", BR)
    E.formula(c, "100 − 50 − 50 = 0", 84, 520, 130, "g", BR)
    E.risco(c, 70, 540, 1100, 420, 9, 0, "#E5484D", 26)
    E.formula(c, "100 → 50 → 25 → 12,5", 84, 760, 120, "g", AMARELO)
    E.escreve(c, "metade do que sobrou", 84, 940, 72, "i", claro)


salvar((("capa_A_quatro_questoes", a), ("capa_B_praticando_eletrolise", b), ("capa_C_armadilha_meia_vida", d)))
