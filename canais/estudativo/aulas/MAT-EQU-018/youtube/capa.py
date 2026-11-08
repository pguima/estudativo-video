"""Capas do MAT-EQU-018 (1280x720). Uso: python capa.py"""
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


def escuro(c):
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)


def a(c):  # o gancho: 30 veículos, 100 rodas
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "30 veículos", 84, 430, 170, "g", BR)
    E.escreve(c, "100 rodas", 84, 640, 170, "g", AMARELO)
    E.escreve(c, "quantos carros e motos?", 84, 880, 130, "i", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Sistema", "de equações", "substituição")


def d(c):  # o macete: deixe sozinha a letra sem número
    escuro(c)
    E.escreve(c, "o atalho", 84, 340, 140, "i", BR)
    E.formula(c, "x + y = 30", 84, 600, 190, "g", BR)
    E.formula(c, "y = 30 − x", 84, 820, 190, "g", AMARELO)
    E.escreve(c, "a letra sem número na frente", 84, 990, 96, "i", BR)


NOMES = (("capa_A_carros_e_motos", a), ("capa_B_sistema_substituicao", b), ("capa_C_letra_sozinha", d))


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in NOMES:
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
