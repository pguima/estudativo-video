"""Capas da QUI-ELE-012 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: a idade do osso
    base(c)
    M.rrect(c, 1300, 640, 460, 110, 55, "#EDE3C8", 1)
    for sx in (-1, 1):
        for sy in (-1, 1):
            c.drawCircle(1530 + sx * 230, 695 + sy * 60, 68, M.paint("#EDE3C8"))
    E.escreve(c, "1/4 do carbono 14", 84, 420, 120, "g", BR)
    E.escreve(c, "quantos anos", 84, 620, 150, "g", BR)
    E.escreve(c, "tem esse osso?", 84, 790, 150, "g", AMARELO)
    E.escreve(c, "meia-vida e datação", 84, 960, 80, "i", BR)


def b(c):
    E.capa_modelo(c, "Química", "Meia-vida", "e datação", "pelo carbono 14")


def d(c):  # o macete: conte as metades
    palco_capa(c)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "conte as metades", 84, 300, 110, "i", BR)
    E.formula(c, "80 → 40 → 20 → 10", 84, 540, 140, "g", BR)
    E.formula(c, "3 meias-vidas", 84, 740, 140, "g", AMARELO)
    E.escreve(c, "1/2, 1/4, 1/8: o atalho da fração", 84, 930, 72, "i", claro)


salvar((("capa_A_quantos_anos_tem_o_osso", a), ("capa_B_meia_vida", b), ("capa_C_conte_as_metades", d)))
