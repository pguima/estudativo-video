"""Capas do MAT-RAZ-025 (1280x720). Uso: python capa.py"""
import subprocess, sys
from pathlib import Path
RAIZ = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(RAIZ / "_ferramentas"))
import skia
import editorial as E
import motor as M
BR = "#FFFFFF"
COR = E.MATERIAS["Matemática"]["cor"]


def gota(c, cx, cy, r, cor, a=1.0):
    p = skia.Path()
    p.moveTo(cx, cy - r * 2.1)
    p.cubicTo(cx + r * 0.3, cy - r * 1.3, cx + r, cy - r * 0.6, cx + r, cy)
    p.arcTo(skia.Rect.MakeXYWH(cx - r, cy - r, 2 * r, 2 * r), 0, 180, False)
    p.cubicTo(cx - r, cy - r * 0.6, cx - r * 0.3, cy - r * 1.3, cx, cy - r * 2.1)
    c.drawPath(p, M.paint(cor, a))


def a(c):  # o gancho: a torneira pingando joga fora mais de 40 L por mês
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "gota a gota,", 84, 400, 150, "i", BR)
    E.escreve(c, "+ de 40 L", 76, 640, 230, "g", BR)
    E.escreve(c, "por mês", 84, 830, 150, "i", BR)
    for i, (cx, cy, r) in enumerate(((1560, 420, 70), (1560, 680, 95), (1560, 980, 120))):
        gota(c, cx, cy, r, BR, 0.55 + 0.2 * i)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Unidades", "que cortam", "a conta se monta")


def d(c):  # o macete
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "a unidade", 84, 360, 150, "i", BR)
    E.escreve(c, "corta", 76, 600, 250, "g", BR)
    cl = E.mix(COR, BR, 0.55)
    # × 60 min / 1 h com o min riscado
    E.escreve(c, "×", 930, 900, 130, "g", BR)
    x0 = 1110
    E.escreve(c, "60 min", x0, 840, 130, "g", BR)
    w = E.larg("60 min", "g", 130); w60 = E.larg("60 ", "g", 130)
    c.drawRect(skia.Rect.MakeXYWH(x0 - 20, 880, w + 40, 10), M.paint(BR))
    E.centro(c, "1 h", x0 + w / 2, 1010, 130, "g", BR)
    M.line(c, x0 + w60 - 10, 850, x0 + w + 10, 740, cl, 1, 14)
    E.escreve(c, "o minuto some", 84, 1000, 90, "i", cl)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_gota_a_gota", a), ("capa_B_unidades", b), ("capa_C_unidade_corta", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
