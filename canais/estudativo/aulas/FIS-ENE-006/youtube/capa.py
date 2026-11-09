"""Capas do FIS-ENE-006 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: 5 situações, siga a energia
    E.capa_base(c, COR); E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "5 situações", 84, 400, 150, "i", BR)
    E.escreve(c, "siga a", 84, 620, 200, "g", BR)
    E.escreve(c, "energia", 84, 830, 210, "g", AMARELO)
    claro = E.mix(COR, BR, 0.85)
    for i, s in enumerate(("elétrica", "potencial", "cinética", "calor")):
        y = 300 + i * 190
        E.pilula(c, s, 1500, y, 64, "g", fundo=claro, cor=COR)
        if i < 3:
            F.seta(c, 1500, y + 55, 1500, y + 135, BR, 1.0, 10)


def b(c):  # o modelo padrão
    E.capa_base(c, COR); E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "Trabalho", 76, 450, 210, "g", BR)
    E.escreve(c, "e energia", 76, 660, 210, "g", BR)
    E.escreve(c, "exercícios", 84, 860, 150, "i", BR)
    E.simbolo(c, 1600, 780, 240, cor=E.mix(COR, BR, 0.82), forma="orbita")


def d(c):  # o macete: comparação sem converter
    palco(c)
    E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "numa razão, não converta", 84, 340, 110, "i", BR)
    E.formula(c, "f{108}{72} = 1,5", 84, 640, 180, "g", BR)
    claro = E.mix(COR, BR, 0.5)
    E.formula(c, "1,5^2 = 2,25  →  40 m vira 90 m", 84, 920, 90, "g", claro)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_siga_a_energia", a), ("capa_B_trabalho_e_energia_exercicios", b), ("capa_C_razao_sem_converter", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
