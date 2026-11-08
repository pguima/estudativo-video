"""Capas do MAT-ESP-010 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: o molde da lata, que sólido e quanto cabe?
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    x, y, w, h, r = 110, 430, 520, 330, 88
    c.drawRect(skia.Rect.MakeXYWH(x, y, w, h), M.paint(AMARELO))
    c.drawRect(skia.Rect.MakeXYWH(x, y, w, h), M.paint(BR, 1, stroke=8))
    for cy in (y - r, y + h + r):
        c.drawCircle(x + w * 0.16, cy, r, M.paint(E.mix(AMARELO, BR, 0.3)))
        c.drawCircle(x + w * 0.16, cy, r, M.paint(BR, 1, stroke=8))
    E.centro(c, "24 cm", x + w * 0.62, y - 24, 64, "g", BR)
    E.escreve(c, "15 cm", x + w + 24, y + h / 2 + 24, 64, "g", BR)
    E.escreve(c, "que sólido?", 900, 400, 120, "g", BR)
    E.escreve(c, "quantos mL?", 900, 560, 120, "i", BR)
    E.escreve(c, "resolva antes", 900, 820, 120, "g", AMARELO)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Praticando", "sólidos", "prismas e cilindros")


def d(c):  # as armadilhas das 4 situações
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "as 3 armadilhas", 84, 330, 110, "i", BR)
    for k, (s1, s2) in enumerate((("24", "não é o raio"), ("diâmetro", "não é o raio"), ("100 min", "não é 1,4 h"))):
        y = 530 + 190 * k
        E.escreve(c, s1, 84, y, 130, "g", AMARELO)
        E.escreve(c, s2, 84 + E.larg(s1, "g", 130) + 40, y, 110, "i", BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_que_solido", a), ("capa_B_praticando", b), ("capa_C_tres_armadilhas", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
