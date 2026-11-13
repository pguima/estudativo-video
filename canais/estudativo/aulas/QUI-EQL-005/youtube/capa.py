"""Capas da QUI-EQL-005 (1280x720). Uso: python capa.py"""
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


def escuro(c):
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Química", COR)


NOMES = ("capa_A_tres_sais_tres_resultados", "capa_B_hidrolise_salina", "capa_C_forte_vence")


def a(c):  # o gancho: três sais, três pH
    E.capa_base(c, COR); E.capa_rotulo(c, "Química", COR)
    E.escreve(c, "sal na água:", 84, 340, 110, "i", BR)
    for k, (f, r) in enumerate((("NaCl", "neutro"), ("NH4Cl", "ácido"), ("NaHCO3", "básico"))):
        Q.formula(c, f, 84, 520 + k * 170, 120, BR)
        E.escreve(c, r, 700, 520 + k * 170, 120, "g", AMARELO if k == 2 else BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Química", "Hidrólise", "salina", "do zero")


def d(c):  # o macete: o forte vence
    escuro(c)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "o macete", 84, 320, 120, "i", BR)
    E.escreve(c, "o forte", 84, 560, 220, "g", BR)
    E.escreve(c, "vence", 84, 790, 220, "g", claro)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in zip(NOMES, (a, b, d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
