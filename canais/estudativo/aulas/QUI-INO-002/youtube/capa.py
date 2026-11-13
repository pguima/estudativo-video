"""Capas da QUI-INO-002 (1280x720). Uso: python capa.py"""
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




def a(c):  # o gancho: o íon da soda
    E.capa_base(c, COR); E.capa_rotulo(c, "Química", COR)
    E.escreve(c, "a soda cáustica", 84, 380, 110, "i", BR)
    Q.formula(c, "NaOH -> Na^+ + OH^-", 84, 600, 160, BR, cores={"OH": AMARELO})
    E.escreve(c, "o OH sai inteiro", 84, 860, 120, "g", AMARELO)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Química", "Bases", "na água", "do zero")


def d(c):  # o macete: nº de OH = carga do metal
    palco_capa(c)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "quantos OH?", 84, 360, 120, "i", BR)
    E.escreve(c, "a carga do metal", 84, 540, 130, "g", claro)
    Q.formula(c, "Ca(OH)2", 84, 820, 170, BR, escuro=True, cores={"indice": claro})
    E.escreve(c, "família 2 = 2 OH", 84, 1000, 90, "g", BR)


CAPAS = (("capa_A_o_oh_da_soda", a), ("capa_B_bases", b), ("capa_C_carga_do_metal", d))


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in CAPAS:
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
