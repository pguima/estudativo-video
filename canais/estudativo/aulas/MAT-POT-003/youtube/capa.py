"""Capas do MAT-POT-003 (1280x720). Uso: python capa.py"""
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
CLARO = E.mix(COR, BR, 0.5)


def escuro(c):
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)


def a(c):  # o gancho: por que dá 1
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.formula(c, "7^0", 84, 660, 420, cor=BR)
    E.escreve(c, "=", 600, 600, 240, "g", BR)
    E.escreve(c, "1", 850, 660, 420, "g", AMARELO)
    E.escreve(c, "?", 1120, 660, 420, "g", BR)
    E.escreve(c, "dá para provar", 84, 950, 170, "g", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Potências", "mesma base", "vezes e dividido")


def d(c):  # o macete: a escada do dois
    escuro(c)
    E.escreve(c, "a escada", 84, 370, 170, "i", BR)
    E.escreve(c, "do dois", 84, 560, 170, "g", BR)
    w = E.formula(c, "16 × 32 =", 84, 880, 220, cor=BR)
    E.formula(c, "512", 84 + w + 36, 880, 240, cor=AMARELO)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_sete_elevado_a_zero", a), ("capa_B_mesma_base", b), ("capa_C_escada_do_dois", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
