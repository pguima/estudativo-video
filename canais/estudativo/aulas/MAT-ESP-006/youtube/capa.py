"""Capas do MAT-ESP-006 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: a tinta cobre a casca, não enche a caixa
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    pts = E.paralelepipedo(c, 99, 0, 120, 860, 560, 380, 220, escuro=True, cor=BR, preenche=0.0, largura=8)
    for idx in ((0, 1, 2, 3), (3, 2, 6, 7), (1, 2, 6, 5)):
        p = skia.Path(); p.addPoly([pts[i] for i in idx], True)
        c.drawPath(p, M.paint(AMARELO, 0.85))
    E.paralelepipedo(c, 99, 0, 120, 860, 560, 380, 220, escuro=True, cor=BR, preenche=0.0, largura=8)
    E.escreve(c, "3 × 2 × 1", 900, 380, 120, "g", BR)
    E.escreve(c, "quanta tinta?", 900, 520, 100, "i", BR)
    E.escreve(c, "22 m²", 890, 760, 230, "g", AMARELO)
    E.escreve(c, "e não", 900, 920, 100, "i", BR); E.escreve(c, "6 m³", 1130, 920, 96, "g", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Área e", "diagonal", "cubo e bloco")


def d(c):  # o atalho: quadrado raiz de 2, cubo raiz de 3
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "o atalho da diagonal", 84, 340, 100, "i", BR)
    E.formula(c, "quadrado: r{2}", 80, 560, 130, "g", BR)
    E.formula(c, "cubo: r{3}", 80, 760, 170, "g", AMARELO)
    E.formula(c, "d = a r{3}", 84, 950, 110, "g", BR)
    pts = E.cubo(c, 99, 0, 1300, 900, 330, escuro=True, cor=BR, preenche=0.12, largura=8)
    M.line(c, *pts[0], *pts[6], AMARELO, 1, 16)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_quanta_tinta", a), ("capa_B_area_e_diagonal", b), ("capa_C_raiz_de_tres", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
