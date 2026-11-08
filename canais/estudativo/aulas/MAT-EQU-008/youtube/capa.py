"""Capas do MAT-EQU-008 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: x dos dois lados
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.formula(c, "5x − 2 = 3x + 8", 84, 480, 190, "g", BR)
    for x in (84, 84 + E.formula(c, "5x − 2 = ", 0, 0, 190, a=0)):
        M.rrect(c, x - 10, 515, E.larg("5x", "g", 190) + 28, 14, 7, AMARELO)
    E.escreve(c, "x dos dois lados?", 84, 740, 150, "g", AMARELO)
    E.escreve(c, "a regra é a mesma", 84, 930, 120, "i", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Equação", "com x", "dos dois lados")


def d(c):  # o atalho: passa para o outro lado
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "o atalho", 84, 340, 140, "i", BR)
    E.escreve(c, "passa para o", 76, 520, 150, "g", BR)
    E.escreve(c, "outro lado?", 76, 680, 150, "g", BR)
    E.escreve(c, "2x + 3 = 11", 84, 940, 150, "g", E.mix(COR, BR, 0.55))
    E.escreve(c, "→ 2x = 11 − 3", 880, 940, 120, "g", BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_x_dos_dois_lados", a), ("capa_B_letra_dos_dois_lados", b), ("capa_C_passa_para_o_outro_lado", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
