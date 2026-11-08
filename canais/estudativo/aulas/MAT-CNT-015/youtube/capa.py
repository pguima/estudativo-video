"""Capas do MAT-CNT-015 (1280x720). Uso: python capa.py"""
import subprocess, sys
from pathlib import Path
RAIZ = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(RAIZ / "_ferramentas"))
import skia
import editorial as E
import motor as M
BR = "#FFFFFF"
AMARELO = "#FFD500"
COR = E.MATERIAS["Matemática"]["cor"]


def oculos(c, cx, cy, s, cor=BR):
    for dx in (-s * 0.55, s * 0.55):
        c.drawCircle(cx + dx, cy, s * 0.42, M.paint(cor, 1.0, stroke=s * 0.13))
    M.line(c, cx - s * 0.13, cy - s * 0.05, cx + s * 0.13, cy - s * 0.05, cor, 1.0, s * 0.11)


def a(c):  # o gancho: sabendo que usa óculos, 10/40 riscado, é 10/16
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    oculos(c, 300, 400, 200)
    E.escreve(c, "usa óculos:", 600, 380, 120, "i", BR)
    E.escreve(c, "é mulher?", 600, 530, 150, "g", AMARELO)
    y = 840
    E.fracao(c, 10, 40, 300, y, 170, BR)
    E.risco(c, 160, 980, 440, 690, 9, 0, AMARELO, 30)
    E.escreve(c, "é", 560, y + 50, 150, "i", BR)
    E.bola(c, 1000, 830, 220, "#FFFFFF")
    E.fracao(c, 10, 16, 1000, 820, 170, COR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Probabilidade", "condicional", "sabendo que...")


def d(c):  # o macete: a pista vira o novo total
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "viu “sabendo que”?", 84, 400, 120, "i", BR)
    E.escreve(c, "a pista vira", 84, 640, 180, "g", BR)
    E.escreve(c, "o novo total", 84, 860, 180, "g", AMARELO)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_usa_oculos", a), ("capa_B_condicional", b), ("capa_C_novo_total", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
