"""Capas do MAT-POL-007 (1280x720). Uso: python capa.py"""
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


def figura(c, cx, cy, k, cor_linha, cor_corda, larg=12):
    """circunferência de raio 13 com a corda a 5 do centro (k px por cm)"""
    r = 13 * k
    c.drawCircle(cx, cy, r, M.paint(cor_linha, 1, stroke=larg))
    y = cy + 5 * k
    M.line(c, cx - 12 * k, y, cx + 12 * k, y, cor_corda, 1, larg + 6)
    M.line(c, cx, cy, cx, y, cor_linha, 0.85, larg - 4, dash=[18, 14])
    M.line(c, cx, cy, cx + 12 * k, y, cor_linha, 1, larg - 2)
    c.drawCircle(cx, cy, 14, M.paint(cor_linha))
    return y


def a(c):  # o gancho: a resposta não é 12
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    cx, cy, k = 470, 610, 28
    y = figura(c, cx, cy, k, BR, AMARELO)
    E.escreve(c, "13", cx + 150, cy + 30, 90, "g", BR)
    E.escreve(c, "5", cx - 90, cy + 120, 90, "g", BR)
    E.escreve(c, "corda = ?", 1000, 330, 140, "i", BR)
    E.escreve(c, "12", 1000, 600, 230, "g", BR)
    E.risco(c, 980, 610, 1290, 410, 9, 0, "#FF5A5A", 34)
    E.escreve(c, "24!", 1360, 600, 230, "g", AMARELO)
    E.escreve(c, "o erro de todo mundo", 1000, 820, 90, "i", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Tangente", "e corda", "com Pitágoras")


def d(c):  # o atalho: soma vezes diferença
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "o atalho", 90, 360, 130, "i", BR)
    E.escreve(c, "soma × diferença", 90, 560, 170, "g", BR)
    E.formula(c, "18 × 8 = 144", 90, 800, 150, "g", claro)
    E.formula(c, "r{144} = 12", 1080, 800, 150, "g", AMARELO)
    E.escreve(c, "raio 13, corda a 5 do centro:", 90, 980, 70, "i", BR)
    E.escreve(c, "corda 24", 1010, 985, 80, "g", AMARELO)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_nao_e_12", a), ("capa_B_tangente_e_corda", b), ("capa_C_soma_vezes_diferenca", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
