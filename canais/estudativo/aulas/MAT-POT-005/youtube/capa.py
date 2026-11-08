"""Capas do MAT-POT-005 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: não é −8
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.formula(c, "2^{−3}", 84, 640, 380, cor=BR)
    E.escreve(c, "=", 760, 590, 240, "g", BR)
    E.escreve(c, "−8", 960, 640, 380, "g", AMARELO)
    E.escreve(c, "?", 1530, 640, 380, "g", BR)
    E.risco(c, 940, 660, 1480, 340, 9, 0, largura=26)
    E.escreve(c, "nem é negativo", 84, 950, 170, "g", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Expoente", "negativo", "e potências de 10")


def d(c):  # o macete: contar as casas
    escuro(c)
    E.escreve(c, "conte", 84, 370, 170, "i", BR)
    E.escreve(c, "as casas", 84, 560, 170, "g", BR)
    w = E.formula(c, "10^{−6} =", 84, 880, 200, cor=BR)
    E.formula(c, "0,000001", 84 + w + 36, 880, 200, cor=AMARELO)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_nao_e_negativo", a), ("capa_B_expoente_negativo", b), ("capa_C_conte_as_casas", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
