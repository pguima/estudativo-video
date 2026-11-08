"""Capas do MAT-ANA-003 (1280x720). Uso: python capa.py"""
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
VERMELHO = "#FF6B70"


def a(c):  # o gancho: três postes parecem alinhados, mas não estão
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    k, x0, y0 = 105, 1120, 960  # px por unidade; (0, 0) do mapa
    P = lambda x, y: (x0 + x * k, y0 - y * k * 0.78)
    M.line(c, *P(0.6, 0.2), *P(5.4, 10.8), BR, 0.55, 6, dash=[18, 14])
    for i, (x, y) in enumerate(((1, 1), (3, 5), (5, 10))):
        c.drawCircle(*P(x, y), 30, M.paint(AMARELO if i == 1 else BR))
    X, Y = P(3, 5)
    c.drawCircle(X, Y, 62, M.paint(AMARELO, 1, stroke=8))
    E.escreve(c, "na mesma", 84, 400, 150, "i", BR)
    E.escreve(c, "reta?", 76, 610, 230, "g", BR)
    E.escreve(c, "NÃO", 84, 900, 190, "g", AMARELO)


def b(c):  # o modelo
    E.capa_modelo(c, "Matemática", "Coeficiente", "angular", "e alinhamento")


def d(c):  # o atalho: produto em cruz
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "alinhados?", 84, 370, 140, "i", BR)
    E.escreve(c, "em cruz", 76, 570, 190, "g", BR)
    x1, x2, cy, s = 360, 780, 830, 170
    E.fracao(c, 4, 2, x1, cy, s, BR); E.fracao(c, 5, 2, x2, cy, s, BR)
    M.line(c, x1 + 70, cy - 90, x2 - 70, cy + 100, claro, 1, 10)
    M.line(c, x1 + 70, cy + 100, x2 - 70, cy - 90, claro, 1, 10)
    E.escreve(c, "8 ≠ 10", 1060, 900, 190, "g", VERMELHO)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_na_mesma_reta", a), ("capa_B_coeficiente_angular", b), ("capa_C_em_cruz", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
