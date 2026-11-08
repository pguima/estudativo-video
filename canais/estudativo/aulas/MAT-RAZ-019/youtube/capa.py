"""Capas do MAT-RAZ-019 (1280x720). Uso: python capa.py"""
import subprocess, sys
from pathlib import Path
RAIZ = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(RAIZ / "_ferramentas"))
import skia
import editorial as E
import motor as M
BR = "#FFFFFF"
COR = E.MATERIAS["Matemática"]["cor"]


def a(c):  # o gancho: a armadilha da média das velocidades
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "30 e 45 km/h", 84, 380, 150, "g", BR)
    E.escreve(c, "média:", 84, 600, 130, "i", BR)
    E.escreve(c, "37,5?", 500, 610, 190, "g", BR)
    E.risco(c, 480, 640, 1060, 470, 9, 0, "#FFD500", 30)
    E.escreve(c, "36 km/h", 1130, 630, 170, "g", BR)
    E.escreve(c, "5 situações para treinar", 84, 960, 100, "i", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Praticando", "proporção", "5 situações de prova")


def d(c):  # o ângulo do macete: produto sobre soma, sem dobro
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "torneiras ou viagem?", 84, 340, 110, "i", BR)
    cl = E.mix(COR, BR, 0.55)
    E.formula(c, "f{a × b}{a + b}", 480, 700, 190, "g", BR, 1, "center")
    E.formula(c, "f{2 × a × b}{a + b}", 1380, 700, 190, "g", cl, 1, "center")
    E.centro(c, "torneiras", 480, 960, 90, "i", BR)
    E.centro(c, "ida e volta", 1380, 960, 90, "i", cl)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_armadilha_media", a), ("capa_B_praticando", b), ("capa_C_com_ou_sem_dobro", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
