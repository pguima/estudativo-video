"""Capas do FIS-CAL-014 (1280x720). Uso: python capa.py"""
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


def palco_capa(c):
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Física", COR)




def barra(c, x, y, w, h, util, a_txt, b_txt):
    M.rrect(c, x, y, w * util, h, 20, BR, 1.0)
    M.rrect(c, x + w * util, y, w * (1 - util), h, 20, E.mix(COR, "#000000", 0.45), 1.0)
    E.centro(c, a_txt, x + w * util / 2, y + h / 2 + 22, 62, "g", COR)
    E.centro(c, b_txt, x + w * util + w * (1 - util) / 2, y + h / 2 + 22, 62, "g", BR)


def a(c):  # o gancho: só 1/4 vira movimento
    E.capa_base(c, COR); E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "só 1/4 vira", 84, 400, 170, "g", BR)
    E.escreve(c, "movimento", 84, 580, 170, "g", BR)
    barra(c, 84, 700, 1500, 130, 0.25, "25 %", "75 % vira calor perdido")
    E.escreve(c, "e nem o motor perfeito chega a 100 %", 84, 960, 80, "i", BR)


def b(c):  # o modelo padrão
    E.capa_base(c, COR); E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "Segunda lei", 76, 430, 190, "g", BR)
    E.escreve(c, "e máquinas térmicas", 76, 620, 140, "g", BR)
    E.escreve(c, "por que nunca 100 %", 84, 840, 120, "i", BR)
    E.simbolo(c, 1640, 820, 190, cor=E.mix(COR, BR, 0.82), forma="orbita")


def d(c):  # o macete: 1 − Qf/Qq
    palco_capa(c)
    E.escreve(c, "rendimento sem", 84, 360, 120, "i", BR)
    E.escreve(c, "calcular o trabalho", 84, 500, 120, "i", BR)
    E.formula(c, "η = 1 − f{jogado fora}{recebido}", 84, 800, 130, "g", BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_so_um_quarto", a), ("capa_B_segunda_lei", b), ("capa_C_rendimento_sem_trabalho", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
