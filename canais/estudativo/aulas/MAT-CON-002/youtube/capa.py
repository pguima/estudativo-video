"""Capas do MAT-CON-002 (1280x720). Uso: python capa.py"""
import subprocess, sys
from pathlib import Path
RAIZ = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(RAIZ / "_ferramentas"))
import skia
import editorial as E
import motor as M
BR = "#FFFFFF"
COR = E.MATERIAS["Matemática"]["cor"]
AMARELO = "#FFD500"


def venn(c, cx, cy, r, pinta_meio, cor_linha=BR):
    """dois círculos brancos; pinta_meio = só a interseção em amarelo, senão tudo"""
    a, b = (cx - r * 0.62, cy), (cx + r * 0.62, cy)
    if pinta_meio:
        pa, pb = skia.Path(), skia.Path()
        pa.addCircle(*a, r); pb.addCircle(*b, r)
        c.drawPath(skia.Op(pa, pb, skia.PathOp.kIntersect_PathOp), M.paint(AMARELO))
    else:
        for x, y in (a, b):
            c.drawCircle(x, y, r, M.paint(AMARELO, 0.9))
    for x, y in (a, b):
        c.drawCircle(x, y, r, M.paint(cor_linha, 1.0, stroke=12))


def a(c):  # o gancho: café ou chá, quem toma os dois entra
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "café", 84, 420, 170, "g", BR)
    E.escreve(c, "ou", 84, 600, 190, "g", AMARELO)
    E.escreve(c, "chá?", 84, 790, 170, "g", BR)
    E.escreve(c, "quem toma os dois entra", 84, 980, 80, "i", BR)
    venn(c, 1430, 560, 250, True)
    E.centro(c, "os dois", 1430, 575, 38, "g", COR)


def b(c):  # o modelo
    E.capa_modelo(c, "Matemática", "União e", "interseção", "sem confundir")


def d(c):  # o atalho
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "comece pela", 84, 400, 130, "i", BR)
    E.escreve(c, "interseção", 76, 620, 200, "g", BR)
    E.escreve(c, "o resto sai sozinho", 84, 860, 100, "i", E.mix(COR, BR, 0.6))
    venn(c, 1500, 840, 180, True)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_cafe_ou_cha", a), ("capa_B_uniao_e_intersecao", b), ("capa_C_comece_pela_intersecao", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
