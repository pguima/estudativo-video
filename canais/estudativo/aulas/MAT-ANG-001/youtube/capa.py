"""Capas do MAT-ANG-001 (1280x720). Uso: python capa.py"""
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


def hora(cx, cy, rr, h):
    a = math.radians(h * 30)
    return cx + rr * math.sin(a), cy - rr * math.cos(a)


def relogio(c, cx, cy, r, hp, fundo="#FFFFFF", tinta="#121214", numeros=(12, 3, 6, 9), meio=None):
    """mostrador com o grande no 12 e o pequeno na hora hp"""
    s = skia.Paint(AntiAlias=True, Color=M.hexc("#000000", 0.3))
    s.setMaskFilter(skia.MaskFilter.MakeBlur(skia.kNormal_BlurStyle, 22))
    c.drawCircle(cx + 10, cy + 20, r, s)
    c.drawCircle(cx, cy, r, M.paint(fundo))
    c.drawCircle(cx, cy, r, M.paint(tinta, 1, stroke=r * 0.03))
    for h in range(12):
        forte = h % 3 == 0
        M.line(c, *hora(cx, cy, r * (0.84 if forte else 0.89), h), *hora(cx, cy, r * 0.95, h), tinta, 1, r * (0.026 if forte else 0.013))
    for n in numeros:
        x, y = hora(cx, cy, r * 0.68, n % 12)
        E.centro(c, str(n), x, y + r * 0.06, r * 0.17, "g", tinta)
    if meio:
        meio()
    M.line(c, cx, cy, *hora(cx, cy, r * 0.6, 12), tinta, 1, r * 0.035)
    M.line(c, cx, cy, *hora(cx, cy, r * 0.42, hp), tinta, 1, r * 0.055)
    c.drawCircle(cx, cy, r * 0.05, M.paint(tinta))


def a(c):  # o gancho: quanto mede o canto das 3 horas?
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    cx, cy, r = 500, 640, 330
    s = r * 0.26
    relogio(c, cx, cy, r, 3, meio=lambda: (c.drawRect(skia.Rect.MakeXYWH(cx, cy - s, s, s), M.paint(AMARELO, 0.8)),
                                           c.drawRect(skia.Rect.MakeXYWH(cx, cy - s, s, s), M.paint(COR, 1, stroke=8))))
    E.escreve(c, "3 horas", 960, 470, 150, "i", BR)
    E.escreve(c, "= ?°", 950, 760, 280, "g", AMARELO)
    E.escreve(c, "quanto mede?", 960, 950, 110, "i", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Ângulos", "em graus", "do zero")


def d(c):  # o atalho do relógio
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    cx, cy, r = 450, 640, 310
    relogio(c, cx, cy, r, 4, "#15132E", BR, numeros=range(1, 13))
    claro = E.mix(COR, BR, 0.5)
    ret = skia.Rect.MakeXYWH(cx - r * 0.6, cy - r * 0.6, r * 1.2, r * 1.2)
    p = skia.Path(); p.moveTo(cx, cy); p.arcTo(ret, -90, 120, False); p.close()
    c.drawPath(p, M.paint(claro, 0.45))
    c.drawArc(ret, -90, 120, False, M.paint(claro, 1, stroke=8))
    E.escreve(c, "o atalho", 880, 380, 130, "i", BR)
    E.escreve(c, "1 hora = 30°", 870, 600, 150, "g", BR)
    E.escreve(c, "4 × 30 = 120°", 880, 820, 110, "g", claro)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_quanto_mede", a), ("capa_B_angulos_em_graus", b), ("capa_C_atalho_relogio", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
