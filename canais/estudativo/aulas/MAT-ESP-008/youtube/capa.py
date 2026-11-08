"""Capas do MAT-ESP-008 (1280x720). Uso: python capa.py"""
import math, subprocess, sys
from pathlib import Path
RAIZ = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(RAIZ / "_ferramentas"))
import skia
import editorial as E
import motor as M
BR = "#FFFFFF"
COR = E.MATERIAS["Matemática"]["cor"]
AMARELO = "#FFD500"
SEN, COS = math.sin(math.radians(22)), math.cos(math.radians(22))


def lata(c, cx, cy, r, h, cor=None):
    """cilindro em traço branco; cor = corpo pintado"""
    ry, ct = r * SEN, cy - h * COS
    if cor:
        p = skia.Path()
        p.moveTo(cx - r, ct); p.lineTo(cx - r, cy)
        p.arcTo(skia.Rect.MakeXYWH(cx - r, cy - ry, 2 * r, 2 * ry), 180, -180, False)
        p.lineTo(cx + r, ct)
        p.arcTo(skia.Rect.MakeXYWH(cx - r, ct - ry, 2 * r, 2 * ry), 0, 180, False)
        p.close()
        c.drawPath(p, M.paint(cor, 0.9))
        c.drawOval(skia.Rect.MakeXYWH(cx - r, ct - ry, 2 * r, 2 * ry), M.paint(E.mix(cor, BR, 0.35)))
    pt = M.paint(BR, 1, stroke=8)
    c.drawOval(skia.Rect.MakeXYWH(cx - r, ct - ry, 2 * r, 2 * ry), pt)
    c.drawArc(skia.Rect.MakeXYWH(cx - r, cy - ry, 2 * r, 2 * ry), 0, 180, False, pt)
    M.line(c, cx - r, cy, cx - r, ct, BR, 1, 8); M.line(c, cx + r, cy, cx + r, ct, BR, 1, 8)


def a(c):  # o gancho: dobrar o raio quadruplica
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    lata(c, 230, 900, 100, 230)
    lata(c, 600, 900, 200, 230, AMARELO)
    E.escreve(c, "raio × 2", 900, 420, 130, "g", BR)
    E.escreve(c, "cabe", 900, 580, 110, "i", BR)
    E.escreve(c, "4 vezes", 890, 800, 220, "g", AMARELO)
    E.escreve(c, "mais", 900, 940, 110, "i", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Cilindro", "volume", "e área total")


def d(c):  # o atalho da área total
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "a área da lata em 2 contas", 84, 340, 96, "i", BR)
    E.formula(c, "2πr · (r + h)", 80, 580, 170, "g", AMARELO)
    E.escreve(c, "o atalho", 84, 780, 130, "g", BR)
    lata(c, 1600, 960, 170, 380, COR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_raio_dobrado", a), ("capa_B_cilindro_volume_e_area", b), ("capa_C_dois_pi_r", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
