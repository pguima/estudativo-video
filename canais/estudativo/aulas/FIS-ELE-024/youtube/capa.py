"""Capas do FIS-ELE-024 (1280x720). Uso: python capa.py"""
import subprocess, sys
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


def palco_capa(c):
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
NEG = F.NEG


def pilula(c, s, cx, cy, size, fundo, cor=BR):
    w, h = E.formula(None, s, 0, 0, size, "g", a=0) + size * 1.2, size * 1.9
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2, cy - h / 2, w, h), h / 2, h / 2), M.paint(fundo))
    E.formula(c, s, cx, cy + size * 0.36, size, "g", cor, 1.0, "center")


def a(c):  # o gancho: a bateria virada soma ou subtrai?
    E.capa_base(c, COR); E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "bateria virada:", 84, 380, 120, "i", BR)
    E.escreve(c, "soma ou", 84, 580, 190, "g", BR)
    M.rrect(c, 70, 640, 900, 230, 30, BR)
    E.escreve(c, "subtrai?", 110, 815, 170, "g", COR)
    claro = E.mix(COR, BR, 0.8)
    x0, x1, yt, yb = 1220, 1760, 300, 820
    for (xa, ya, xb, yb_) in ((x0, yt, x1, yt), (x0, yb, x1, yb), (x0, yt, x0, 500), (x0, 620, x0, yb), (x1, yt, x1, 500), (x1, 620, x1, yb)):
        M.line(c, xa, ya, xb, yb_, claro, 1, 12)
    for x in (x0, x1):
        M.line(c, x - 70, 540, x + 70, 540, BR, 1, 10, cap_round=False)
        M.line(c, x - 36, 584, x + 36, 584, BR, 1, 26, cap_round=False)
        E.centro(c, "+", x + 100, 530, 70, "g", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Física", "Leis de", "Kirchhoff", "nós e malhas")


def d(c):  # o macete: o sinal é o polo por onde você entra
    palco_capa(c)
    E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "o sinal é o polo", 84, 360, 120, "i", BR)
    E.escreve(c, "por onde você entra", 84, 540, 130, "g", BR)
    pilula(c, "entra no −:  + ε", 560, 780, 80, COR)
    pilula(c, "entra no +:  − ε", 1300, 780, 80, NEG)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_soma_ou_subtrai", a), ("capa_B_leis_de_kirchhoff", b), ("capa_C_o_sinal_e_o_polo", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
