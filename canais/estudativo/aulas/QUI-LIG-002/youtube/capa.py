"""Capas da QUI-LIG-002 (1280x720). Uso: python capa.py"""
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

def a(c):  # o gancho: N₂, três ligações
    E.capa_base(c, COR); E.capa_rotulo(c, "Química", COR)
    Q.lewis(c, 99, 0, [("N", -0.7, 0, [180]), ("N", 0.7, 0, [0])], [(0, 1, 3)], 1350, 500, 280, 220, escuro=True, cor_e=AMARELO)
    E.escreve(c, "3 ligações", 84, 450, 150, "g", BR)
    E.escreve(c, "ao mesmo", 84, 620, 150, "g", BR)
    E.escreve(c, "tempo?", 84, 790, 150, "g", AMARELO)
    E.escreve(c, "a estrutura de Lewis", 84, 970, 90, "i", BR)


def b(c):
    E.capa_modelo(c, "Química", "Ligação", "covalente", "e Lewis")


def d(c):  # o macete: ligações = o que falta para 8
    palco_capa(c)
    E.escreve(c, "ligações =", 84, 330, 130, "g", BR)
    E.escreve(c, "o que falta para 8", 84, 480, 110, "i", CLARO)
    for k, (el, n) in enumerate((("H", 1), ("O", 2), ("N", 3), ("C", 4))):
        x = 260 + 420 * k
        Q.atomo(c, x, 720, 100, el, escuro=True)
        E.centro(c, str(n), x, 980, 150, "g", CLARO)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_tres_ligacoes", a), ("capa_B_ligacao_covalente", b), ("capa_C_falta_para_oito", d)):
    c = s.getCanvas()
    c.clear(skia.ColorWHITE)
    fn(c)
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
