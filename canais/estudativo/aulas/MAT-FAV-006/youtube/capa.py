"""Capas do MAT-FAV-006 (1280x720). Uso: python capa.py"""
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


def palco(c):
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)


def espelho(c, x0, y0, k):
    """f(x) = 2x + 3 e a inversa, com a diagonal; (x0, y0) = origem, k = px por unidade"""
    P = lambda x, y: (x0 + x * k, y0 - y * k)
    M.arrow(c, *P(-2, 0), *P(8.3, 0), BR, 0.6, 6, 24)
    M.arrow(c, *P(0, -2), *P(0, 8.3), BR, 0.6, 6, 24)
    M.line(c, *P(-2, -2), *P(8, 8), BR, 0.7, 6, dash=[24, 16])
    M.line(c, *P(-2.5, -2), *P(2.5, 8), BR, 1, 16)
    M.line(c, *P(-2, -2.5), *P(8, 2.5), AMARELO, 1, 16)


def a(c):  # o gancho: saiu 13, qual foi a entrada?
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "saiu 13:", 84, 390, 160, "i", BR)
    E.escreve(c, "qual entrou?", 84, 600, 170, "g", BR)
    E.formula(c, "f^{−1}(13) = 5", 84, 830, 130, "g", AMARELO)
    espelho(c, 1340, 820, 62)


def b(c):  # o modelo
    E.capa_modelo(c, "Matemática", "Função", "inversa", "em 3 passos")


def d(c):  # o atalho: de trás para frente
    palco(c)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "desfaça", 84, 380, 170, "g", BR)
    E.escreve(c, "de trás para frente", 84, 560, 120, "i", BR)
    E.escreve(c, "× 2, + 3", 84, 760, 110, "g", BR)
    E.escreve(c, "→  − 3, ÷ 2", 560, 760, 110, "g", AMARELO)
    E.formula(c, "f^{−1}(x) = f{x − 3}{2}", 84, 960, 100, "g", BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_saiu_13", a), ("capa_B_funcao_inversa", b), ("capa_C_de_tras_para_frente", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
