"""Capas do MAT-PLN-007 (1280x720). Uso: python capa.py"""
import subprocess, sys
from pathlib import Path
RAIZ = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(RAIZ / "_ferramentas"))
import skia
import editorial as E
import motor as M
BR = "#FFFFFF"
AMARELO = "#FFD500"
COR = E.MATERIAS["Matemática"]["cor"]


def palco(c):
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)



def a(c):  # o gancho: cinco questões, uma por ferramenta
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "5 questões de", 84, 400, 140, "i", BR)
    E.escreve(c, "polinômios", 84, 600, 200, "g", BR)
    for k in range(5):
        E.bola(c, 180 + 200 * k, 830, 80, AMARELO)
        E.centro(c, str(k + 1), 180 + 200 * k, 865, 100, "g", COR)
    E.formula(c, "k = ?", 1350, 860, 150, cor=AMARELO)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Praticando", "polinômios", "raízes e Girard")


def d(c):  # o atalho: teste o 1
    palco(c)
    E.escreve(c, "antes de tudo,", 84, 330, 120, "i", BR)
    E.escreve(c, "teste o 1", 84, 560, 230, "g", AMARELO)
    E.formula(c, "1 − 7 + 14 − 8 = 0", 84, 800, 120, cor=BR)
    E.escreve(c, "soma dos coeficientes = P(1)", 84, 960, 90, "i", "#C9C3FF")


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_cinco_questoes", a), ("capa_B_praticando", b), ("capa_C_teste_o_1", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
