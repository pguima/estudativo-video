"""Capas da QUI-LIG-010 (1280x720). Uso: python capa.py"""
import math, subprocess, sys
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


CLARO = E.mix(COR, BR, 0.5)

def a(c):  # o gancho: H₂S maior, ferve 160 graus abaixo
    E.capa_base(c, COR); E.capa_rotulo(c, "Química", COR)
    Q.formula(c, "H2O", 84, 470, 200, BR)
    E.escreve(c, "100 °C", 700, 470, 180, "g", AMARELO)
    Q.formula(c, "H2S", 84, 760, 200, BR)
    E.escreve(c, "−60 °C", 700, 760, 180, "g", BR)
    E.escreve(c, "a molécula menor ferve mais alto?", 84, 980, 80, "i", BR)


def b(c):
    E.capa_modelo(c, "Química", "Ponto de", "ebulição", "como comparar")


def d(c):  # o macete: força primeiro
    palco_capa(c)
    E.escreve(c, "força", 84, 480, 220, "g", BR)
    E.escreve(c, "primeiro,", 820, 480, 180, "i", CLARO)
    E.escreve(c, "tamanho", 84, 760, 200, "g", BR)
    E.escreve(c, "no empate", 84, 940, 150, "i", CLARO)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_agua_ferve_acima", a), ("capa_B_pontos_de_ebulicao", b), ("capa_C_forca_primeiro", d)):
    c = s.getCanvas()
    c.clear(skia.ColorWHITE)
    fn(c)
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
