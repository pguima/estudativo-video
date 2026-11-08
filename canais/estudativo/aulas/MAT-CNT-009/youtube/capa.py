"""Capas do MAT-CNT-009 (1280x720). Uso: python capa.py"""
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


def boneco(c, cx, cy, h, cor):
    c.drawCircle(cx, cy - h * 0.36, h * 0.17, M.paint(cor))
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - h * 0.25, cy - h * 0.14, h * 0.5, h * 0.52), h * 0.2, h * 0.2), M.paint(cor))


def caixa(c, x, y, w, h, n, txt):
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 30, 30), M.paint(BR, 1, stroke=8))
    for i in range(n):
        boneco(c, x + w / 2 + (i - (n - 1) / 2) * 95, y + 130, 90, BR)
    E.centro(c, txt, x + w / 2, y + h - 50, 64, "g", BR)


def a(c):  # o gancho: 10 + 6 = 16 errado, são 60
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    caixa(c, 84, 230, 560, 330, 5, "2 entre 5")
    caixa(c, 700, 230, 480, 330, 4, "2 entre 4")
    E.escreve(c, "10 + 6", 84, 820, 170, "g", BR)
    E.risco(c, 60, 760, 640, 750, 9, 0, AMARELO, 30)
    E.escreve(c, "não!", 700, 810, 120, "i", BR)
    E.bola(c, 1550, 720, 260, "#FFFFFF")
    E.centro(c, "60", 1550, 720 + 95, 270, "g", COR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Comissões", "com regras", "e o pelo menos um")


def d(c):  # o macete: pelo menos um = tudo menos nenhum
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "“pelo menos um”?", 84, 380, 140, "i", BR)
    E.escreve(c, "tudo", 84, 640, 220, "g", BR)
    E.escreve(c, "−", 640, 640, 220, "g", AMARELO)
    E.escreve(c, "nenhum", 840, 640, 220, "g", AMARELO)
    E.escreve(c, "84 − 10 = 74", 84, 930, 150, "g", BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_nao_e_16", a), ("capa_B_comissoes_regras", b), ("capa_C_tudo_menos_nenhum", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
