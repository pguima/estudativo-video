"""Capas do MAT-RAZ-018 (1280x720). Uso: python capa.py"""
import subprocess, sys
from pathlib import Path
RAIZ = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(RAIZ / "_ferramentas"))
import skia
import editorial as E
import motor as M
BR = "#FFFFFF"
COR = E.MATERIAS["Matemática"]["cor"]


def a(c):  # o gancho: 3 h e 6 h juntas não dão 4 h 30
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "3 h", 90, 430, 230, "g", BR)
    E.mais(c, 560, 350, 80, "#FFFFFF", sombra=False)
    E.escreve(c, "6 h", 680, 430, 230, "g", BR)
    E.escreve(c, "juntas:", 90, 680, 130, "i", BR)
    E.escreve(c, "4 h 30?", 560, 690, 170, "g", BR)
    E.risco(c, 540, 720, 1240, 560, 9, 0, "#FFD500", 30)
    E.escreve(c, "o erro das torneiras", 90, 960, 120, "i", BR)
    # caixa-d'água com torneira
    x, y, w, h = 1420, 420, 360, 420
    rr = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 22, 22)
    c.drawRRect(rr, M.paint(BR, 0.16))
    c.save(); c.clipRRect(rr, True); c.drawRect(skia.Rect.MakeXYWH(x, y + h * 0.4, w, h * 0.6), M.paint(BR, 0.9)); c.restore()
    c.drawRRect(rr, M.paint(BR, 1, stroke=8))
    s = 60
    tx = x + w * 0.3
    M.rrect(c, tx - s * 1.6, y - 40 - s * 0.95, s * 1.75, s * 0.5, s * 0.12, BR)
    M.rrect(c, tx - s * 0.25, y - 40 - s * 0.95, s * 0.5, s * 0.95, s * 0.12, BR)
    c.drawRect(skia.Rect.MakeXYWH(tx - 8, y - 40, 16, 40 + h * 0.4), M.paint(BR, 0.9))


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Vazão e", "torneiras", "juntas")


def d(c):  # o atalho
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "o atalho", 84, 340, 150, "i", BR)
    E.escreve(c, "produto", 76, 540, 200, "g", BR)
    E.escreve(c, "sobre soma", 76, 720, 170, "i", BR)
    E.formula(c, "f{3 × 6}{3 + 6} = 2 h", 1440, 930, 170, "g", E.mix(COR, BR, 0.55), 1, "center")


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_erro_torneiras", a), ("capa_B_vazao", b), ("capa_C_produto_sobre_soma", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
