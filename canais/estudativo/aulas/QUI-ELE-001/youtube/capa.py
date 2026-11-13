"""Capas da QUI-ELE-001 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: de onde sai o +6?
    E.capa_base(c, COR); E.capa_rotulo(c, "Química", COR)
    Q.formula(c, "H2SO4", 84, 640, 320, BR)
    G = Q.grupos("H2SO4", 84, 640, 320)
    g = G[1]
    E.bola(c, g["cx"], g["topo"] - 100, 100, AMARELO)
    E.centro(c, "+6", g["cx"], g["topo"] - 100 + 40, 110, "g", "#1A1A1A")
    E.escreve(c, "de onde sai", 1240, 500, 110, "i", BR)
    E.escreve(c, "esse 6?", 1240, 650, 150, "g", AMARELO)
    E.escreve(c, "o número de oxidação", 84, 900, 92, "i", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Química", "Número", "de oxidação", "do zero")


def d(c):  # o macete: complete a soma até zero
    palco_capa(c)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "Nox de cabeça", 84, 300, 130, "i", BR)
    E.escreve(c, "em 5 segundos", 84, 480, 160, "g", BR)
    Q.formula(c, "KMnO4", 84, 760, 230, BR, cores={"Mn": claro}, escuro=True)
    E.formula(c, "+1 − 8 = −7", 84, 980, 100, "g", claro)
    E.bola(c, 1500, 700, 150, COR)
    E.centro(c, "+7", 1500, 760, 160, "g", BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_de_onde_sai_o_seis", a), ("capa_B_numero_de_oxidacao", b), ("capa_C_nox_de_cabeca", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
