"""Capas do FIS-ELE-001 (1280x720). Uso: python capa.py"""
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


def q(c, x, y, r, s, cor=None):
    cor = cor or (BR if s == "+" else F.NEG)
    tinta = COR if cor == BR else BR
    c.drawCircle(x + r * 0.08, y + r * 0.16, r, M.paint("#000000", 0.2))
    c.drawCircle(x, y, r, M.paint(cor))
    k, lw = r * 0.52, r * 0.24
    M.line(c, x - k, y, x + k, y, tinta, 1, lw)
    if s == "+":
        M.line(c, x, y - k, x, y + k, tinta, 1, lw)


def a(c):  # o erro: positivo = ganhou prótons?
    E.capa_base(c, COR); E.capa_rotulo(c, "Física", COR)
    q(c, 190, 360, 95, "+")
    E.escreve(c, "ganhou", 330, 330, 120, "i", BR)
    E.escreve(c, "prótons?", 330, 500, 190, "g", BR)
    E.risco(c, 310, 520, 1240, 380, 9, 0, AMARELO, 30)
    E.escreve(c, "não: perdeu elétrons", 90, 800, 110, "i", BR)
    for i, (x, y) in enumerate(((1450, 760), (1600, 650), (1730, 800))):
        q(c, x, y, 62, "−")


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Física", "Carga", "elétrica", "e eletrização")


def d(c):  # o macete: o sinal de cada jeito
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "o sinal de cada jeito", 84, 340, 110, "i", BR)
    claro = E.mix(COR, BR, 0.5)
    for i, (nome, ss) in enumerate((("atrito", ("+", "−")), ("contato", ("+", "+")), ("indução", ("−", "+")))):
        y = 540 + i * 170
        E.escreve(c, nome, 90, y + 40, 120, "g", BR)
        for j, s in enumerate(ss):
            c.drawCircle(1250 + j * 190, y, 72, M.paint(COR if s == "+" else F.NEG))
            k = 36
            M.line(c, 1250 + j * 190 - k, y, 1250 + j * 190 + k, y, BR, 1, 16)
            if s == "+":
                M.line(c, 1250 + j * 190, y - k, 1250 + j * 190, y + k, BR, 1, 16)
        E.escreve(c, ("opostos", "iguais", "oposto")[i], 1560, y + 30, 80, "i", claro)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_ganhou_protons", a), ("capa_B_carga_eletrica", b), ("capa_C_sinal_de_cada_jeito", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
