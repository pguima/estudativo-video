"""Capas da QUI-ORG-001 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: o zigue-zague sem letras tem 12 H escondidos
    E.capa_base(c, COR); E.capa_rotulo(c, "Química", COR)
    Q.bastao(c, 99, 0, Q.zigzag(5), 1330, 500, 200, escuro=True, largura=14)
    for x, y, s in ((905, 400, "H3"), (1125, 690, "H2"), (1330, 360, "H2"), (1535, 690, "H2"), (1755, 400, "H3")):
        Q.formula(c, s, x, y, 76, AMARELO, align="center")
    E.escreve(c, "cadê os", 84, 420, 140, "i", BR)
    E.escreve(c, "12 H?", 84, 610, 220, "g", AMARELO)
    E.escreve(c, "eles estão escondidos", 84, 1000, 84, "i", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Química", "Fórmula", "em bastão", "do zero")


def d(c):  # o macete: H = 2C + 2
    palco_capa(c)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "conte os H", 84, 330, 130, "i", BR)
    E.escreve(c, "sem desenhar", 84, 520, 150, "g", BR)
    E.formula(c, "H = 2C + 2", 84, 790, 200, "g", claro)
    E.escreve(c, "e cada dupla tira 2", 84, 990, 80, "i", BR)
    Q.bastao(c, 99, 0, Q.zigzag(4), 1560, 380, 150, duplas={(0, 1)}, escuro=True, largura=12)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_hidrogenios_escondidos", a), ("capa_B_formula_em_bastao", b), ("capa_C_dobro_mais_dois", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
