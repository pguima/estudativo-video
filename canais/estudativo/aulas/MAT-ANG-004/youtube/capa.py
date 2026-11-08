"""Capas do MAT-ANG-004 (1280x720). Uso: python capa.py"""
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


def pt(V, L, g):
    return V[0] + L * math.cos(math.radians(g)), V[1] - L * math.sin(math.radians(g))


def cunha(c, V, g1, g2, r, cor, alfa=0.6, borda=8):
    ret = skia.Rect.MakeXYWH(V[0] - r, V[1] - r, 2 * r, 2 * r)
    p = skia.Path(); p.moveTo(*V); p.arcTo(ret, -g1, -(g2 - g1), False); p.close()
    c.drawPath(p, M.paint(cor, alfa))
    c.drawArc(ret, -g1, -(g2 - g1), False, M.paint(cor, 1, stroke=borda, cap_round=True))


def peca(c, V, g1, g2, L, cor):
    """ponta de papel rasgada com o ângulo pintado"""
    P1, P2 = pt(V, L, g1), pt(V, L, g2)
    path = skia.Path(); path.moveTo(*V); path.lineTo(*P1)
    nx, ny = (P2[1] - P1[1]), -(P2[0] - P1[0])
    nn = math.hypot(nx, ny) or 1
    for i in range(1, 7):
        f, k = i / 7, (12 if i % 2 else -12)
        path.lineTo(P1[0] + (P2[0] - P1[0]) * f + nx / nn * k, P1[1] + (P2[1] - P1[1]) * f + ny / nn * k)
    path.lineTo(*P2); path.close()
    s = skia.Paint(AntiAlias=True, Color=M.hexc("#000000", 0.3))
    s.setMaskFilter(skia.MaskFilter.MakeBlur(skia.kNormal_BlurStyle, 12))
    c.save(); c.translate(8, 14); c.drawPath(path, s); c.restore()
    c.drawPath(path, M.paint(BR))
    cunha(c, V, g1, g2, L * 0.55, cor, 0.45, 7)


def a(c):  # o gancho: as três pontas sempre dão uma linha reta
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    O = (620, 820)
    M.line(c, O[0] - 520, O[1], O[0] + 520, O[1], BR, 1, 12)
    peca(c, O, 0, 60, 330, "#3B3B40")
    peca(c, O, 60, 110, 330, COR)
    peca(c, O, 110, 180, 330, "#D98A00")
    E.escreve(c, "sempre", 1200, 470, 170, "i", BR)
    E.escreve(c, "180°", 1180, 760, 300, "g", AMARELO)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Ângulos do", "triângulo", "e o externo")


def d(c):  # o atalho: externo = A + B
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    claro = E.mix(COR, BR, 0.5)
    B, C = (140, 880), (720, 880)
    A = pt(B, 580 * math.sin(math.radians(70)) / math.sin(math.radians(50)), 60)
    cunha(c, A, 240, 290, 110, claro)
    cunha(c, B, 0, 60, 110, "#8A8A90")
    cunha(c, C, 0, 60, 160, "#8A8A90")
    cunha(c, C, 60, 110, 160, claro)
    for P, Q in ((A, B), (B, C), (C, A)):
        M.line(c, *P, *Q, BR, 1, 10)
    M.line(c, *C, C[0] + 330, C[1], BR, 1, 8, dash=[22, 16])
    E.escreve(c, "externo", 1000, 520, 160, "g", BR)
    E.escreve(c, "= A + B", 1000, 740, 170, "g", AMARELO)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_sempre_180", a), ("capa_B_angulos_do_triangulo", b), ("capa_C_externo", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
