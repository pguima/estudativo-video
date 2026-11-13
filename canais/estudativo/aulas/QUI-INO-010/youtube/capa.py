"""Capas da QUI-INO-010 (1280x720). Uso: python capa.py"""
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




def a(c):  # o gancho: zinco reage, cobre não
    E.capa_base(c, COR); E.capa_rotulo(c, "Química", COR)
    E.escreve(c, "zinco reage,", 84, 400, 140, "g", BR)
    E.escreve(c, "cobre não.", 84, 570, 140, "g", AMARELO)
    E.escreve(c, "por quê?", 84, 760, 120, "i", BR)
    Q.atomo(c, 1380, 520, 130, "Zn")
    Q.atomo(c, 1680, 520, 130, "Cu")


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Química", "Simples", "troca", "e a fila")


def d(c):  # o macete: a fila
    palco_capa(c)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "a fila decide", 84, 340, 110, "i", BR)
    for i, s in enumerate(("K", "Na", "Mg", "Zn", "Fe", "H", "Cu", "Ag", "Au")):
        x = 150 + i * 200
        if s == "H":
            E.bola(c, x, 600, 80, COR); E.centro(c, "H", x, 630, 90, "g", BR)
        else:
            Q.atomo(c, x, 600, 72, s, escuro=True)
    E.escreve(c, "antes do H: reage com ácido", 84, 900, 90, "g", claro)


CAPAS = (("capa_A_zinco_e_cobre", a), ("capa_B_simples_troca", b), ("capa_C_a_fila", d))


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in CAPAS:
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
