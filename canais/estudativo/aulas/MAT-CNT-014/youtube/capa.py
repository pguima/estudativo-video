"""Capas do MAT-CNT-014 (1280x720). Uso: python capa.py"""
import subprocess, sys
from pathlib import Path
RAIZ = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(RAIZ / "_ferramentas"))
import skia
import editorial as E
import motor as M
BR = "#FFFFFF"
AMARELO = "#FFD500"
VERM = "#D94B3D"
COR = E.MATERIAS["Matemática"]["cor"]


def copas(c, cx, cy, s, cor=VERM):
    h = s / 2
    pa = skia.Path()
    pa.moveTo(cx, cy + h)
    pa.cubicTo(cx - h * 1.9, cy - h * 0.1, cx - h * 0.9, cy - h * 1.5, cx, cy - h * 0.45)
    pa.cubicTo(cx + h * 0.9, cy - h * 1.5, cx + h * 1.9, cy - h * 0.1, cx, cy + h)
    c.drawPath(pa, M.paint(cor))


def carta(c, cx, cy, w, valor):
    h = w * 1.4
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2, cy - h / 2, w, h), w * 0.12, w * 0.12), M.paint(BR))
    E.escreve(c, valor, cx - w / 2 + w * 0.1, cy - h / 2 + w * 0.36, w * 0.34, "g", VERM)
    copas(c, cx + w * 0.06, cy + h * 0.12, w * 0.5)


def a(c):  # o gancho: rei ou copas? 17/52 riscado, é 16/52
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    carta(c, 250, 470, 230, "K")
    E.escreve(c, "rei ou", 470, 400, 150, "g", BR)
    E.escreve(c, "copas?", 470, 560, 150, "g", AMARELO)
    y = 850
    E.fracao(c, 17, 52, 300, y, 170, BR)
    E.risco(c, 160, 990, 440, 700, 9, 0, AMARELO, 30)
    E.escreve(c, "é", 560, y + 50, 150, "i", BR)
    E.bola(c, 1000, 840, 220, "#FFFFFF")
    E.fracao(c, 16, 52, 1000, 830, 170, COR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Chance", "da união", "rei ou copas?")


def d(c):  # o macete: some e tire o que repete
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "viu “ou”?", 84, 400, 130, "i", BR)
    E.escreve(c, "4 + 13 − 1", 84, 680, 220, "g", AMARELO)
    E.escreve(c, "some e tire o repetido", 84, 920, 110, "g", BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_rei_ou_copas", a), ("capa_B_chance_uniao", b), ("capa_C_tire_repetido", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
