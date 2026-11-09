"""Capas do FIS-ELE-008 (1280x720). Uso: python capa.py"""
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


def palco(c):
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Física", COR)


def celular(c, cx, cy, s, texto):
    M.rrect(c, cx - s * 0.5, cy - s, s, 2 * s, s * 0.12, "#121214", 1)
    M.rrect(c, cx - s * 0.44, cy - s * 0.9, s * 0.88, s * 1.75, s * 0.06, "#2C3340", 1)
    M.rrect(c, cx - s * 0.28, cy - s * 0.45, s * 0.56, s * 0.9, 10, BR, 1)
    M.rrect(c, cx - s * 0.1, cy - s * 0.53, s * 0.2, s * 0.1, 4, BR, 1)
    M.rrect(c, cx - s * 0.22, cy - s * 0.05, s * 0.44, s * 0.44, 6, "#16A36A", 1)
    E.formula(c, texto, cx, cy + s * 0.75, s * 0.16, "g", BR, 1, "center")


def a(c):  # o erro: mAh é corrente?
    E.capa_base(c, COR); E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "mAh é", 84, 380, 170, "g", BR)
    E.escreve(c, "corrente?", 84, 580, 200, "g", BR)
    E.risco(c, 70, 600, 1000, 420, 9, 0, AMARELO, 30)
    E.escreve(c, "não: é carga", 84, 860, 150, "i", BR)
    celular(c, 1560, 560, 330, "4.000 mAh")


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Física", "Corrente", "elétrica", "do zero")


def d(c):  # o macete: quanto dura a bateria
    palco(c)
    E.escreve(c, "quanto dura a bateria?", 84, 340, 100, "i", BR)
    E.formula(c, "tempo = f{mAh}{mA}", 84, 640, 190, "g", BR)
    E.escreve(c, "3.000 ÷ 500 = 6 h", 84, 920, 110, "g", E.mix(COR, BR, 0.5))


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_mah_e_carga", a), ("capa_B_corrente_eletrica", b), ("capa_C_quanto_dura_a_bateria", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
