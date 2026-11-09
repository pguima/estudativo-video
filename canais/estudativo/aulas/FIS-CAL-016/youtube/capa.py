"""Capas do FIS-CAL-016 (1280x720). Uso: python capa.py"""
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




def a(c):  # o gancho: o motor de 55 % passa no teste?
    E.capa_base(c, COR); E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "motor de 55 %", 84, 400, 160, "g", BR)
    E.escreve(c, "passa no teste?", 84, 580, 160, "g", AMARELO)
    E.escreve(c, "5 situações de calor e termodinâmica", 84, 800, 76, "i", BR)


def b(c):  # o modelo padrão
    E.capa_base(c, COR); E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "Praticando", 76, 430, 200, "g", BR)
    E.escreve(c, "termodinâmica", 76, 620, 160, "g", BR)
    E.escreve(c, "da panela ao motor", 84, 840, 120, "i", BR)
    E.simbolo(c, 1640, 820, 190, cor=E.mix(COR, BR, 0.82), forma="orbita")


def d(c):  # o macete: o roteiro de prova
    palco_capa(c)
    E.escreve(c, "4 atalhos", 84, 360, 160, "g", BR)
    claro = E.mix(COR, BR, 0.5)
    for i, s in enumerate(("precisa de matéria?", "τ = área no p × V", "a caixa: entra +, sai −", "Carnot sempre em kelvin")):
        E.formula(c, s, 84, 540 + i * 130, 84, "g", claro if i % 2 else BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_motor_de_55", a), ("capa_B_praticando_termodinamica", b), ("capa_C_quatro_atalhos", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
