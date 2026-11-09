"""Capas do FIS-CIN-021 (1280x720). Uso: python capa.py"""
import math, subprocess, sys
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


def a(c):  # o desafio: a roda-gigante
    E.capa_base(c, COR); E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "roda-gigante:", 84, 390, 120, "i", BR)
    E.escreve(c, "qual a", 84, 570, 160, "g", BR)
    E.escreve(c, "velocidade?", 84, 740, 160, "g", BR)
    E.escreve(c, "resolva antes de mim", 84, 920, 76, "i", AMARELO)
    cx, cy, R = 1520, 520, 300
    M.line(c, cx, cy, cx - R * 0.55, cy + R * 1.4, BR, 1.0, 14)
    M.line(c, cx, cy, cx + R * 0.55, cy + R * 1.4, BR, 1.0, 14)
    c.drawCircle(cx, cy, R, M.paint(BR, 1.0, stroke=12))
    for k in range(8):
        g = math.radians(20 + 45 * k)
        X, Y = cx + math.cos(g) * R, cy - math.sin(g) * R
        M.line(c, cx, cy, X, Y, BR, 0.6, 5)
        M.rrect(c, X - 34, Y, 68, 60, 12, AMARELO if k == 0 else E.mix(COR, BR, 0.7))
    c.drawCircle(cx, cy, 20, M.paint(BR))


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Física", "Praticando", "rotação", "polias e bicicleta")


def d(c):  # a pergunta-chave
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "a pergunta que", 84, 330, 120, "i", BR)
    E.escreve(c, "resolve metade:", 84, 500, 130, "g", BR)
    E.escreve(c, "como estão ligadas?", 84, 680, 120, "i", E.mix(COR, BR, 0.5))
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "borda: v igual", 84, 880, 80, "g", BR)
    E.escreve(c, "eixo: ω igual", 760, 880, 80, "g", claro)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_roda_gigante", a), ("capa_B_praticando_rotacao", b), ("capa_C_como_estao_ligadas", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
