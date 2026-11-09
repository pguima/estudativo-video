"""Capas do FIS-CIN-002 (1280x720). Uso: python capa.py"""
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


def a(c):  # o erro: somar os módulos em ângulo reto
    E.capa_base(c, COR); E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "4 + 3", 84, 420, 200, "g", BR)
    E.escreve(c, "= 7?", 84, 640, 200, "g", BR)
    E.risco(c, 250, 700, 560, 470, 9, 0, AMARELO, 20)
    claro = E.mix(COR, BR, 0.55)
    O, Q, P = (1250, 900), (1250, 360), (1655, 360)
    F.seta(c, *O, *Q, BR, 1.0, 22)
    F.seta(c, *Q, *P, BR, 1.0, 22)
    F.seta(c, *O, *P, AMARELO, 1.0, 26)
    E.escreve(c, "4", 1130, 680, 110, "g", BR); E.escreve(c, "3", 1420, 320, 110, "g", BR)
    E.escreve(c, "5", 1520, 720, 150, "g", AMARELO)
    E.escreve(c, "é cinco. Por quê?", 84, 900, 96, "i", claro)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Física", "Somar", "vetores", "do zero")


def d(c):  # o macete: ternos pitagóricos
    palco(c)
    E.escreve(c, "resultante", 84, 330, 120, "i", BR)
    E.escreve(c, "sem conta", 76, 520, 190, "g", BR)
    for i, s in enumerate(("3 · 4 · 5", "6 · 8 · 10", "5 · 12 · 13")):
        x = 330 + i * 600
        M.rrect(c, x - 270, 640, 540, 210, 36, COR, 1.0)
        E.centro(c, s, x, 780, 110, "g", BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_somar_nao_da_sete", a), ("capa_B_somar_vetores", b), ("capa_C_ternos_sem_conta", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
