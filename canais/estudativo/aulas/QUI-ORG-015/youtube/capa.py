"""Capas da QUI-ORG-015 (1280x720). Uso: python capa.py"""
import subprocess, sys
from pathlib import Path
RAIZ = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(RAIZ / "_ferramentas"))
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "roteiro"))
import skia
import editorial as E
import quimica as Q
import motor as M
import visual as V  # as peças de estrutura da aula (alceno), desenhadas paradas
BR = "#FFFFFF"
AMARELO = "#FFD500"
COR = E.MATERIAS["Química"]["cor"]


def escuro(c):
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Química", COR)


def a(c):  # o gancho: o "trans" da gordura trans
    E.capa_base(c, COR); E.capa_rotulo(c, "Química", COR)
    E.escreve(c, "gordura", 84, 380, 190, "g", BR)
    E.escreve(c, "trans", 84, 610, 220, "g", AMARELO)
    E.escreve(c, "o que é?", 84, 800, 130, "i", BR)
    V.alceno(c, 0, None, 1420, 330, V.CIS, 120, 70, escuro=True)
    E.escreve(c, "cis", 1380, 560, 70, "g", BR)
    V.alceno(c, 0, None, 1420, 790, V.TRANS, 120, 70, escuro=True, cores={2: AMARELO, 5: AMARELO})
    E.escreve(c, "trans", 1350, 1020, 70, "g", AMARELO)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Química", "Isomeria", "cis-trans", "do zero")


def d(c):  # o macete: dois ligantes iguais, pare
    escuro(c)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "2 ligantes iguais", 84, 360, 120, "g", BR)
    E.escreve(c, "no mesmo carbono?", 84, 500, 110, "i", BR)
    E.escreve(c, "pare", 84, 720, 200, "g", AMARELO)
    E.escreve(c, "sem cis-trans", 84, 880, 90, "i", claro)
    P = V.alceno(c, 0, None, 1450, 640, ("H", "H", "H", "CH2–CH3"), 150, 84, escuro=True)
    c.drawCircle(P[2][0] - 10, (P[2][1] + P[3][1]) / 2, 185, M.paint(AMARELO, 1, stroke=10))


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_gordura_trans", a), ("capa_B_isomeria_cis_trans", b), ("capa_C_ligantes_iguais", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
