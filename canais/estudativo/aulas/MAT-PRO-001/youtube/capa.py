"""Capas do MAT-PRO-001 (1280x720). Uso: python capa.py"""
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
    k = s * 0.46 if len(val) <= 2 else s * 0.34
    E.centro(c, val, cx, cy + k * 0.36, k, "g", cor_val or E.TINTA, 1.0)
    E.centro(c, pos, cx, cy + s / 2 + 70, 60, "b", BR, 1.0)


def a(c):  # o gancho: qual é o 100º?
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    for i, v in enumerate(("4", "7", "10", "13")):
        caixa(c, 170 + i * 230, 440, 190, v, f"{i + 1}º")
    for dx in (-30, 0, 30):
        c.drawCircle(1100 + dx, 440, 11, M.paint(BR))
    caixa(c, 1420, 440, 230, "?", "100º", cor_val=COR, fundo=AMARELO)
    E.escreve(c, "qual é o 100º?", 84, 960, 140, "g", BR)


def b(c):  # o modelo
    E.capa_modelo(c, "Matemática", "Sequências", "e a regra", "posição e valor")


def d(c):  # o atalho: o caminho de volta
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "o 100 está na lista?", 84, 340, 110, "i", claro)
    E.escreve(c, "3n + 1 = 100", 76, 580, 170, "g", BR)
    E.escreve(c, "n = 33", 76, 820, 200, "g", AMARELO)
    E.escreve(c, "está!", 760, 810, 150, "i", BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_qual_e_o_100", a), ("capa_B_sequencias", b), ("capa_C_caminho_de_volta", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
