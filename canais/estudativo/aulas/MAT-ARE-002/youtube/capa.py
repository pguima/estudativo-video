"""Capas do MAT-ARE-002 (1280x720). Uso: python capa.py"""
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


def chao(c, x, y, s, cols, lins, cor, so=lambda k, r: True, borda=BR):
    """chão com pisos de lado s"""
    c.drawRect(skia.Rect.MakeXYWH(x, y, cols * s, lins * s), M.paint(BR, 0.12))
    for r in range(lins):
        for k in range(cols):
            if so(k, r):
                M.rrect(c, x + k * s + 4, y + r * s + 4, s - 8, s - 8, 8, cor)
    c.drawRect(skia.Rect.MakeXYWH(x, y, cols * s, lins * s), M.paint(borda, 1, stroke=6))


def a(c):  # o gancho: 24 pisos cobrem só metade
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    chao(c, 110, 300, 100, 8, 6, BR, so=lambda k, r: r % 2 == 0)
    for r in range(3):
        pt = M.paint(AMARELO, 1, stroke=6); pt.setPathEffect(skia.DashPathEffect.Make([22, 16], 0))
        c.drawRect(skia.Rect.MakeXYWH(118, 300 + r * 200 + 108, 784, 84), pt)
    E.escreve(c, "24 pisos?", 1000, 470, 160, "g", BR)
    E.escreve(c, "metade do", 1010, 700, 120, "i", BR)
    E.escreve(c, "chão vazia", 1010, 850, 120, "i", AMARELO)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Área do", "retângulo", "e do quadrado")


def d(c):  # o atalho: conte pelos lados
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    claro = E.mix(COR, BR, 0.5)
    chao(c, 120, 360, 80, 8, 6, COR, so=lambda k, r: r == 5, borda=claro)
    for r in range(5):
        M.rrect(c, 124, 364 + r * 80, 72, 72, 8, claro)
    E.escreve(c, "o atalho", 900, 380, 130, "i", BR)
    E.escreve(c, "conte pelos", 890, 580, 130, "g", BR)
    E.escreve(c, "lados", 890, 740, 130, "g", BR)
    E.escreve(c, "8 × 6 = 48", 900, 920, 110, "g", claro)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_metade_do_chao", a), ("capa_B_area_retangulo", b), ("capa_C_conte_pelos_lados", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
