"""Capas da QUI-CAL-001 (1280x720). Uso: python capa.py"""
import subprocess, sys
from pathlib import Path
RAIZ = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(RAIZ / "_ferramentas"))
import skia
import editorial as E
import quimica as Q
import motor as M
BR = "#FFFFFF"
AMARELO = "#FFD500"
COR = E.MATERIAS["Química"]["cor"]
E.usar("Química")


def palco(c):
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Química", COR)


def a(c):  # o gancho: a glicose pesa 180 o quê?
    E.capa_base(c, COR); E.capa_rotulo(c, "Química", COR)
    Q.formula(c, "C6H12O6", 84, 470, 250, BR)
    E.escreve(c, "= 180", 84, 760, 230, "g", AMARELO)
    E.escreve(c, "u", 84 + E.larg("= 180", "g", 230) + 50, 760, 230, "g", BR)
    E.simbolo(c, 1600, 600, 230, cor=E.mix(COR, BR, 0.82), forma="hexagono")
    E.escreve(c, "180 o quê?", 84, 990, 110, "i", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Química", "Massa", "molecular", "do zero")


def d(c):  # o macete: 6 cópias de CH2O
    palco(c)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "a glicose", 84, 340, 120, "i", BR)
    E.escreve(c, "em 3 segundos", 76, 530, 170, "g", BR)
    E.escreve(c, "6 ×", 84, 800, 220, "g", claro)
    Q.formula(c, "CH2O", 480, 800, 220, BR, escuro=True)
    E.formula(c, "30 × 6 = 180", 84, 1000, 110, "g", claro)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_180_o_que", a), ("capa_B_massa_molecular", b), ("capa_C_seis_pedacos", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
