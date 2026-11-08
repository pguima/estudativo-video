"""Capas do MAT-PRO-009 (1280x720). Uso: python capa.py"""
import subprocess, sys
from pathlib import Path
RAIZ = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(RAIZ / "_ferramentas"))
import skia
import editorial as E
import motor as M
BR = "#FFFFFF"
AM = "#FFD500"
COR = E.MATERIAS["Matemática"]["cor"]


def caixa(c, cx, cy, w, h, s, cor=BR, size=150):
    rr = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2, cy - h / 2, w, h), 26, 26)
    c.drawRRect(rr, M.paint(cor, 1, stroke=9))
    E.centro(c, s, cx, cy + size * 0.36, size, "g", cor)


def a(c):  # o gancho: 4, x, 9 — a média erra
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    for x, s, cor in ((300, "4", BR), (720, "x", AM), (1140, "9", BR)):
        caixa(c, x, 520, 280, 220, s, cor)
    E.salto(c, 9, 0, 300, 720, 400, 90, AM, "×q", size=70)
    E.salto(c, 9, 0, 720, 1140, 400, 90, AM, "×q", size=70)
    E.escreve(c, "6,5", 1400, 570, 170, "g", E.mix(COR, BR, 0.55))
    E.risco(c, 1380, 600, 1720, 430, 9, 0, AM, 26)
    E.escreve(c, "não é a média!", 84, 900, 140, "i", BR)
    E.escreve(c, "x = 6", 1300, 920, 180, "g", AM)


def b(c):  # o modelo
    E.capa_modelo(c, "Matemática", "Atalhos", "da PG", "meio e três termos")


def d(c):  # o atalho: fatore os vizinhos
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "12, x, 75", 84, 360, 150, "g", BR)
    E.escreve(c, "sem multiplicar:", 84, 540, 110, "i", BR)
    E.formula(c, "x = r{12 · 75}", 84, 780, 140, "g", E.mix(COR, BR, 0.55))
    E.escreve(c, "= 30", 84, 960, 190, "g", AM)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_nao_e_a_media", a), ("capa_B_atalhos_da_pg", b), ("capa_C_fatore_os_vizinhos", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
