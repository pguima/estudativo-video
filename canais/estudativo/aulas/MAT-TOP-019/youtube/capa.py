"""Capas do MAT-TOP-019 (1280x720). Uso: python capa.py"""
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
SAB = ("#6B3E26", "#E0508A", "#D9CBB0", "#6BB33A")


def a(c):  # o gancho: 4 sabores, 3 doces, 20
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "3 doces, 4 sabores,", 84, 380, 120, "g", BR)
    E.escreve(c, "pode repetir", 84, 520, 120, "i", BR)
    for i, (s, x) in enumerate((("4?", 84), ("64?", 380))):
        E.escreve(c, s, x, 800, 190, "g", BR)
        E.risco(c, x - 10, 820, x + E.larg(s, "g", 190) + 10, 640, 9, 0, AMARELO, 26)
    E.escreve(c, "20", 900, 820, 260, "g", AMARELO)
    for i in range(4):
        E.bola(c, 1480 + (i % 2) * 230, 330 + (i // 2) * 230, 90, SAB[i])


def b(c):  # o modelo
    E.capa_modelo(c, "Matemática", "Escolher", "repetindo", "bolinhas e barras")


def d(c):  # o macete: bolinhas e barras
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "x + y + z = 10", 84, 380, 150, "g", BR)
    x, y = 140, 620
    for i, s in enumerate("ooo|ooooo|oo"):
        cx = x + i * 140
        if s == "o":
            E.bola(c, cx, y, 46, E.CLARO)
        else:
            M.line(c, cx, y - 90, cx, y + 90, BR, 1, 14)
    E.escreve(c, "= 66 soluções", 84, 950, 150, "g", "#3CC7D3")


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_nao_e_4_nem_64", a), ("capa_B_combinacao_com_repeticao", b), ("capa_C_bolinhas_e_barras", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
