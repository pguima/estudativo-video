"""Capas da QUI-ELE-013 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: você é feito de estrela
    base(c)
    E.bola(c, 1450, 560, 260, "#FFC24A")
    E.escreve(c, "o carbono do", 84, 420, 120, "g", BR)
    E.escreve(c, "seu corpo veio", 84, 570, 120, "g", BR)
    E.escreve(c, "de uma estrela", 84, 740, 150, "g", AMARELO)
    E.escreve(c, "fissão e fusão nuclear", 84, 940, 80, "i", BR)


def b(c):
    E.capa_modelo(c, "Química", "Fissão", "e fusão", "nuclear")


def d(c):  # o macete: pesado parte, leves juntam
    palco_capa(c)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "nunca mais confunda", 84, 300, 110, "i", BR)
    E.escreve(c, "pesado → médios", 84, 520, 120, "g", BR); E.escreve(c, "fissão", 1150, 520, 120, "g", claro)
    E.escreve(c, "leves → maior", 84, 720, 120, "g", BR); E.escreve(c, "fusão", 1150, 720, 120, "g", AMARELO)
    E.escreve(c, "a usina usa fissão; o Sol, fusão", 84, 920, 72, "i", claro)


salvar((("capa_A_carbono_de_estrela", a), ("capa_B_fissao_e_fusao", b), ("capa_C_pesado_e_leves", d)))
