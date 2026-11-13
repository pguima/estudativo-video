"""Capas da QUI-TER-005 (1280x720). Uso: python capa.py"""
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


NOMES = ("capa_A_po_reage_antes", "capa_B_colisoes_e_fatores", "capa_C_tres_fatores")


def comp(c, cx, cy, r, po):
    import random
    if not po:
        c.drawOval(skia.Rect.MakeLTRB(cx - r, cy - r * 0.35, cx + r, cy + r * 0.35), M.paint(BR))
        return
    rnd = random.Random(3)
    for k in range(90):
        c.drawCircle(cx + rnd.uniform(-r, r), cy + rnd.uniform(-r * 0.3, r * 0.3), 9, M.paint(BR))


def a(c):  # o gancho: o mesmo remédio, o pó reage antes
    E.capa_base(c, COR); E.capa_rotulo(c, "Química", COR)
    E.escreve(c, "o mesmo remédio:", 84, 340, 110, "i", BR)
    E.escreve(c, "o pó", 84, 560, 200, "g", AMARELO)
    E.escreve(c, "reage antes", 84, 760, 160, "g", BR)
    comp(c, 1450, 440, 200, False)
    comp(c, 1450, 760, 220, True)
    E.escreve(c, "por quê?", 84, 960, 96, "i", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Química", "Colisões", "e fatores", "da velocidade")


def d(c):  # o macete: três fatores
    escuro(c)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "acelera a reação:", 84, 320, 110, "i", BR)
    for k, s in enumerate(("moer", "esquentar", "concentrar")):
        E.escreve(c, "↑ " + s, 84, 520 + k * 170, 140, "g", claro if k % 2 else BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in zip(NOMES, (a, b, d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
