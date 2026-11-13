"""Capas da QUI-EQL-004 (1280x720). Uso: python capa.py"""
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


NOMES = ("capa_A_mesma_concentracao_ph_diferente", "capa_B_acidos_fracos_ka", "capa_C_raiz_de_ka_m")


def a(c):  # o gancho: mesma concentração, pH diferente
    E.capa_base(c, COR); E.capa_rotulo(c, "Química", COR)
    E.escreve(c, "mesma concentração", 84, 360, 110, "i", BR)
    E.escreve(c, "pH 1", 84, 600, 220, "g", BR)
    E.escreve(c, "pH 3", 760, 600, 220, "g", AMARELO)
    E.escreve(c, "forte contra fraco", 84, 800, 140, "g", BR)
    E.escreve(c, "o Ka explica", 84, 990, 84, "i", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Química", "Ácidos", "fracos", "o Ka e o pH")


def d(c):  # o macete: raiz de Ka vezes M
    escuro(c)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "o macete", 84, 320, 120, "i", BR)
    E.formula(c, "[H⁺] = r{Ka · M}", 84, 580, 190, "g", BR)
    E.formula(c, "r{10^{−6}} = 10^{−3}", 84, 850, 140, "g", claro)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in zip(NOMES, (a, b, d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
