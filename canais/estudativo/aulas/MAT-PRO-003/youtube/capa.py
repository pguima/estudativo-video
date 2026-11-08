"""Capas do MAT-PRO-003 (1280x720). Uso: python capa.py"""
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


def caixa(c, cx, cy, s, val, pos, cor_val=None, fundo=BR):
    M.rrect(c, cx - s / 2, cy - s / 2, s, s, 26, fundo, 1.0)
    E.centro(c, val, cx, cy + s * 0.18, s * 0.5, "g", cor_val or E.TINTA, 1.0)
    if pos:
        E.centro(c, pos, cx, cy + s / 2 + 66, 56, "b", BR, 1.0)


def a(c):  # o gancho: a letra da posição 2.026
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    for i, v in enumerate("ABCDABCD"):
        caixa(c, 150 + i * 150, 360, 130, v, None)
    for dx in (-30, 0, 30):
        c.drawCircle(1380 + dx, 360, 11, M.paint(BR))
    caixa(c, 1640, 360, 200, "?", "2.026º", cor_val=COR, fundo=AMARELO)
    E.escreve(c, "qual letra?", 84, 800, 150, "g", BR)
    E.escreve(c, "uma divisão resolve", 84, 960, 100, "i", BR)


def b(c):  # o modelo
    E.capa_modelo(c, "Matemática", "Padrões que", "se repetem", "o resto manda")


def d(c):  # o atalho: só os dois últimos algarismos
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "o atalho:", 84, 340, 120, "i", claro)
    S = 300
    E.escreve(c, "2.0", 76, 680, S, "g", E.mix(BR, "#07070F", 0.6))
    w = E.larg("2.0", "g", S)
    E.escreve(c, "26", 76 + w, 680, S, "g", AMARELO)
    E.escreve(c, "÷ 4: resto 2", 76, 930, 140, "g", BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_posicao_2026", a), ("capa_B_o_resto_manda", b), ("capa_C_dois_ultimos", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
