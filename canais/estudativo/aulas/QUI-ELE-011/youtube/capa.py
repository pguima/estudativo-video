"""Capas da QUI-ELE-011 (1280x720). Uso: python capa.py"""
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

def nuc(c, A, Z, s, x, y, size, cor=BR, cor_z=None):
    sn = size * 0.5
    ta, tz = str(A), str(Z)
    wn = max(E.larg(ta, "g", sn), E.larg(tz, "g", sn))
    E.escreve(c, ta, x + wn - E.larg(ta, "g", sn), y - size * 0.46, sn, "g", cor)
    E.escreve(c, tz, x + wn - E.larg(tz, "g", sn), y + size * 0.2, sn, "g", cor_z or cor)
    E.escreve(c, s, x + wn + size * 0.06, y, size, "g", cor)



def a(c):  # o gancho: do urânio ao chumbo, quantas partículas?
    base(c)
    nuc(c, 238, 92, "U", 84, 470, 200)
    E.escreve(c, "→", 520, 450, 160, "g", BR)
    nuc(c, 206, 82, "Pb", 720, 470, 200)
    E.escreve(c, "8 alfas", 84, 720, 150, "g", AMARELO)
    E.escreve(c, "6 betas", 84, 900, 150, "g", BR)
    E.escreve(c, "em 30 segundos", 700, 900, 90, "i", BR)


def b(c):
    E.capa_modelo(c, "Química", "Alfa, beta", "e gama", "do zero")


def d(c):  # o macete: conte pela massa
    palco_capa(c)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "o macete do decaimento", 84, 300, 110, "i", BR)
    E.formula(c, "238 − 206 = 32", 84, 520, 130, "g", BR)
    E.formula(c, "32 ÷ 4 = 8 alfas", 84, 720, 130, "g", AMARELO)
    E.escreve(c, "a beta não mexe na massa", 84, 920, 80, "i", claro)


salvar((("capa_A_oito_alfas_seis_betas", a), ("capa_B_alfa_beta_gama", b), ("capa_C_conte_pela_massa", d)))
