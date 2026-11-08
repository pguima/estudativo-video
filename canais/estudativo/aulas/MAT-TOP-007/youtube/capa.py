"""Capas do MAT-TOP-007 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: o caminho mais curto até a reta
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    k, ox, oy = 190, 1330, 700          # 1 unidade = k px; origem
    P = lambda x, y: (ox + x * k, oy - y * k)
    M.line(c, *P(-2.6, 2.2), *P(3.4, -2.3), BR, 1, 12)
    pP, F, V = P(1, 2), P(-0.2, 0.4), P(1, -0.5)
    M.line(c, *pP, *V, BR, 0.55, 10, dash=[24, 18])
    M.line(c, *pP, *F, AMARELO, 1, 16)
    c.drawCircle(*pP, 26, M.paint(BR))
    E.escreve(c, "2", (pP[0] + F[0]) / 2 - 175, (pP[1] + F[1]) / 2 + 40, 150, "g", AMARELO)
    E.escreve(c, "2,5", V[0] + 30, V[1] - 90, 90, "g", BR)
    E.escreve(c, "o caminho", 84, 470, 150, "i", BR)
    E.escreve(c, "mais curto", 84, 650, 170, "g", BR)
    E.escreve(c, "até a reta", 84, 830, 150, "i", BR)


def b(c):  # o modelo
    E.capa_modelo(c, "Matemática", "Distância de", "ponto a reta", "em uma linha")


def d(c):  # o atalho: retas paralelas
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "retas paralelas?", 84, 360, 130, "i", BR)
    E.escreve(c, "subtraia os c", 76, 560, 180, "g", BR)
    E.formula(c, "d = f{|c₁ − c₂|}{r{a^2 + b^2}}", 90, 880, 160, "g", AMARELO)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_caminho_mais_curto", a), ("capa_B_distancia_ponto_reta", b), ("capa_C_retas_paralelas", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
