"""Capas do FIS-ENE-002 (1280x720). Uso: python capa.py"""
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


def a(c):  # o erro: rendimento de 125 %
    E.capa_base(c, COR); E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "rendimento", 84, 380, 130, "i", BR)
    E.escreve(c, "125 %?", 84, 640, 260, "g", BR)
    E.risco(c, 60, 680, 1000, 430, 9, 0, AMARELO, 30)
    E.escreve(c, "impossível", 84, 880, 150, "g", AMARELO)
    claro = E.mix(COR, BR, 0.82)
    M.rrect(c, 1330, 360, 300, 300, 40, claro)
    E.centro(c, "motor", 1480, 530, 70, "g", COR)
    F.seta(c, 1640, 450, 1840, 450, BR, 1.0, 30)
    F.seta(c, 1560, 670, 1560, 860, E.mix(COR, "#000000", 0.3), 1.0, 30)


def b(c):  # o modelo padrão
    E.capa_base(c, COR); E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "Potência", 76, 450, 210, "g", BR)
    E.escreve(c, "e rendimento", 84, 650, 170, "i", BR)
    E.escreve(c, "do zero", 84, 850, 130, "i", BR)
    E.simbolo(c, 1590, 760, 260, cor=E.mix(COR, BR, 0.82), forma="orbita")


def d(c):  # o macete: P = F · v
    palco(c)
    E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "o atalho da potência", 84, 340, 110, "i", BR)
    E.escreve(c, "P = F · v", 76, 600, 230, "g", BR)
    claro = E.mix(COR, BR, 0.5)
    F.chao(c, 1060, 1820, 900, 1.0, True)
    F.carrinho(c, 1420, 900, 420)
    F.seta(c, 1420, 640, 1800, 640, F.VEL, 1.0, 18)
    E.escreve(c, "v", 1560, 610, 90, "g", F.VEL)
    E.escreve(c, "watt = J/s", 84, 900, 90, "b", claro)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_rendimento_125_impossivel", a), ("capa_B_potencia_e_rendimento", b), ("capa_C_potencia_forca_vezes_velocidade", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
