"""Capas do MAT-FRA-016 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: 3,6 está errado
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "1,2 × 0,3", 84, 470, 240, "g", BR)
    E.escreve(c, "=", 84, 760, 240, "g", BR)
    E.escreve(c, "3,6", 330, 760, 280, "g", BR)
    E.risco(c, 300, 790, 840, 520, 9, 0, AMARELO, 34)
    E.escreve(c, "0,36", 980, 760, 280, "g", AMARELO)
    E.escreve(c, "conte as duas casas", 84, 980, 130, "i", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Multiplicar", "decimais", "e andar a vírgula")


def d(c):  # o macete: vezes cinco
    escuro(c)
    E.escreve(c, "o atalho do", 84, 340, 150, "i", BR)
    E.escreve(c, "vezes 5", 76, 570, 240, "g", BR)
    E.escreve(c, "× 10 e metade", 84, 770, 150, "g", AMARELO)
    E.escreve(c, "2,4 × 5 = 12", 84, 960, 170, "g", BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_1_2_vezes_0_3", a), ("capa_B_multiplicar_decimais", b), ("capa_C_atalho_vezes_5", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
