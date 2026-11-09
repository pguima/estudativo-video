"""Capas do FIS-CIN-013 (1280x720). Uso: python capa.py"""
import subprocess, sys
from pathlib import Path
RAIZ = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(RAIZ / "_ferramentas"))
import skia
import editorial as E
import fisica as F
import motor as M
BR = "#FFFFFF"
AMARELO = "#FFD500"
COR = E.MATERIAS["Física"]["cor"]
E.usar("Física")


def a(c):  # o gancho: martelo e pena caem juntos
    E.capa_base(c, COR); E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "martelo", 84, 400, 170, "g", BR)
    E.escreve(c, "ou pena?", 84, 590, 170, "g", BR)
    E.escreve(c, "caem juntos", 84, 790, 130, "i", AMARELO)
    E.escreve(c, "sem ar", 84, 930, 100, "i", BR)
    # martelo
    M.rrect(c, 1290, 330, 34, 330, 8, "#5A3A22")
    M.rrect(c, 1200, 300, 214, 80, 12, "#2E2E36")
    # pena
    x, y, s = 1640, 300, 230
    p = skia.Path()
    p.moveTo(x, y); p.cubicTo(x + s * 0.55, y + s * 0.3, x + s * 0.45, y + s * 1.2, x, y + s * 1.5)
    p.cubicTo(x - s * 0.45, y + s * 1.2, x - s * 0.55, y + s * 0.3, x, y); p.close()
    c.drawPath(p, M.paint("#FFF4E0"))
    M.line(c, x, y + 10, x, y + s * 1.8, "#7A5A3A", 1.0, 7)
    for xx in (1307, 1640):
        F.seta(c, xx, 780, xx, 980, BR, 1.0, 16)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Física", "Queda", "livre", "tempo e velocidade")


def d(c):  # o macete: a tabela da queda
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "decore", 84, 330, 130, "i", BR)
    E.escreve(c, "a tabela", 76, 500, 170, "g", BR)
    E.escreve(c, "da queda", 76, 680, 170, "g", BR)
    claro = E.mix(COR, BR, 0.5)
    for i, (tt, h) in enumerate(((1, 5), (2, 20), (3, 45), (4, 80))):
        y = 330 + i * 170
        E.centro(c, f"{tt} s", 1240, y, 110, "g", BR)
        E.centro(c, "→", 1430, y, 90, "g", claro)
        E.centro(c, f"{h} m", 1650, y, 110, "g", claro)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_martelo_ou_pena", a), ("capa_B_queda_livre", b), ("capa_C_tabela_da_queda", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
