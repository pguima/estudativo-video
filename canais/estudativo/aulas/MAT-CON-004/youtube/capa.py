"""Capas do MAT-CON-004 (1280x720). Uso: python capa.py"""
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
CM = skia.FontMgr().makeFromFile("C:/Windows/Fonts/cambria.ttc", 1)  # Cambria Math: ℕ ℤ ℚ (a fonte da casa não tem)


def dupla(c, s, x, y, size, cor):
    f = skia.Font(CM, size)
    f.setEmbolden(True)
    p = M.paint(cor)
    p.setStyle(skia.Paint.kStrokeAndFill_Style); p.setStrokeWidth(size * 0.025)
    c.drawString(s, x, y, f, p)


def a(c):  # o gancho: −3 é natural? 0,4545… é fração?
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "−3", 84, 500, 260, "g", BR)
    E.escreve(c, "é natural?", 500, 470, 110, "i", BR)
    E.pilula(c, "NÃO", 1560, 420, 80, "g", fundo=AMARELO, cor=COR)
    E.escreve(c, "0,4545…", 84, 860, 175, "g", BR)
    E.escreve(c, "é fração?", 930, 840, 110, "i", BR)
    E.pilula(c, "SIM", 1560, 800, 80, "g", fundo=AMARELO, cor=COR)


def b(c):  # o modelo
    E.capa_modelo(c, "Matemática", "Naturais,", "inteiros", "e racionais")


def d(c):  # o atalho: suba a escada
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "suba a", 84, 380, 130, "i", BR)
    E.escreve(c, "escada", 76, 590, 220, "g", BR)
    for i, s in enumerate("ℕℤℚ"):
        x, y = 860 + i * 330, 980 - i * 230
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y - 170, 300, 200), 24, 24), M.paint(COR, 0.85))
        dupla(c, s, x + 85, y, 170, BR if i < 2 else AMARELO)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_menos_tres_e_natural", a), ("capa_B_naturais_inteiros_racionais", b), ("capa_C_suba_a_escada", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
