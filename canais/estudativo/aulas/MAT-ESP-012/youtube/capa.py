"""Capas do MAT-ESP-012 (1280x720). Uso: python capa.py"""
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
VERMELHO = "#FF5A5A"
VISTA = (-24, 18)


def piramide(c, cx, cy, lado, alt, k, face=True, apotema=True, altura=True):
    """a pirâmide de base quadrada em traço branco, a face da frente em amarelo, a apótema e a altura"""
    r, h = lado * k / math.sqrt(2), alt * k
    R, U, _ = E._vista_alta(*VISTA)
    base = E._base_regular(4, r)
    pts = [E._proj((x, 0, z), R, U, cx, cy) for x, z in base] + [E._proj((0, h, 0), R, U, cx, cy)]
    i = max(range(4), key=lambda i: pts[i][1] + pts[(i + 1) % 4][1])
    if face:
        p = skia.Path(); p.addPoly([pts[i], pts[(i + 1) % 4], pts[4]], True)
        c.drawPath(p, M.paint(AMARELO, 0.9))
    E.piramide(c, 99, 0, cx, cy, 4, r, h, vista=VISTA, escuro=True, cor=BR, preenche=0.0, largura=8)
    m = ((pts[i][0] + pts[(i + 1) % 4][0]) / 2, (pts[i][1] + pts[(i + 1) % 4][1]) / 2)
    if altura:
        M.line(c, *pts[4], cx, cy, BR, 1, 7, dash=[18, 12])
    if apotema:
        M.line(c, *pts[4], *m, COR, 1, 10, dash=[18, 12])
    return pts, m


def a(c):  # o gancho: a altura da face é 5, não 4
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    piramide(c, 420, 900, 6, 4, 95)
    E.escreve(c, "altura da face?", 960, 380, 100, "i", BR)
    E.escreve(c, "4", 960, 650, 220, "g", BR)
    M.line(c, 940, 660, 1100, 470, VERMELHO, 1, 18)
    E.escreve(c, "5", 1200, 650, 260, "g", AMARELO)
    E.escreve(c, "a apótema", 960, 860, 120, "g", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Pirâmide", "apótema", "altura e área total")


def d(c):  # o atalho da área lateral
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "o atalho da área lateral", 84, 340, 96, "i", BR)
    E.formula(c, "f{perímetro × apótema}{2}", 80, 600, 110, "g", AMARELO)
    E.escreve(c, "uma conta só", 84, 900, 130, "g", BR)
    piramide(c, 1560, 900, 6, 4, 60, face=True, altura=False)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_cinco_nao_quatro", a), ("capa_B_piramide_apotema", b), ("capa_C_perimetro_apotema", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
