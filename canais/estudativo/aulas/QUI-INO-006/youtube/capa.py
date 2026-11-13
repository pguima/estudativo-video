"""Capas da QUI-INO-006 (1280x720). Uso: python capa.py"""
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




def a(c):  # o gancho: quatro gavetas
    E.capa_base(c, COR); E.capa_rotulo(c, "Química", COR)
    E.escreve(c, "ácido, base,", 84, 400, 140, "g", BR)
    E.escreve(c, "sal ou óxido?", 84, 570, 140, "g", AMARELO)
    for i, f in enumerate(("HCl", "NaOH", "NaCl", "CaO")):
        Q.formula(c, f, 84 + i * 400, 880, 110, BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Química", "Praticando", "ácidos", "e bases")


def d(c):  # o macete: a fórmula diz a função
    palco_capa(c)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "a fórmula diz a função", 84, 340, 100, "i", BR)
    for i, (pista, fun) in enumerate((("H na frente", "ácido"), ("OH no fim", "base"), ("2 elementos com O", "óxido"))):
        E.escreve(c, pista, 84, 540 + i * 170, 90, "g", BR)
        E.escreve(c, "→ " + fun, 1100, 540 + i * 170, 90, "g", claro)


CAPAS = (("capa_A_quatro_gavetas", a), ("capa_B_praticando", b), ("capa_C_a_formula_diz", d))


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in CAPAS:
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
