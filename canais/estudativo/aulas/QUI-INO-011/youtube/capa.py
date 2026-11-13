"""Capas da QUI-INO-011 (1280x720). Uso: python capa.py"""
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




def a(c):  # o gancho: o pó branco
    E.capa_base(c, COR); E.capa_rotulo(c, "Química", COR)
    E.escreve(c, "duas soluções", 84, 400, 130, "g", BR)
    E.escreve(c, "transparentes...", 84, 560, 130, "g", BR)
    E.escreve(c, "pó branco!", 84, 760, 150, "g", AMARELO)
    Q.formula(c, "AgNO3 + NaCl", 84, 960, 100, BR)
    Q.bequer(c, 99, 0, 1500, 900, 380, 440, 0.7, Q.AGUA)
    for k in range(30):
        x = 1500 - 150 + (k * 37 % 100) * 3
        c.drawCircle(x, 870 - (k % 3) * 14, 12, M.paint("#FFFFFF"))


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Química", "Dupla", "troca", "do zero")


def d(c):  # o macete: sólido, gás ou água
    palco_capa(c)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "só acontece se sair", 84, 340, 100, "i", BR)
    E.escreve(c, "sólido,", 84, 560, 150, "g", BR)
    E.escreve(c, "gás", 84, 740, 150, "g", claro)
    E.escreve(c, "ou água", 84, 920, 150, "g", BR)


CAPAS = (("capa_A_po_branco", a), ("capa_B_dupla_troca", b), ("capa_C_solido_gas_agua", d))


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in CAPAS:
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
