"""Capas do FIS-ENE-007 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: por que o airbag salva?
    E.capa_base(c, COR); E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "por que o", 84, 380, 130, "i", BR)
    E.escreve(c, "airbag", 84, 610, 230, "g", BR)
    E.escreve(c, "salva?", 84, 830, 210, "g", AMARELO)
    claro = E.mix(COR, BR, 0.85)
    M.rrect(c, 1250, 870 - 560, 50, 560, 8, E.mix(COR, "#000000", 0.35))
    M.rrect(c, 1380, 870 - 56, 420, 56, 8, claro)
    M.line(c, 1200, 870, 1840, 870, BR, 1, 6)
    E.escreve(c, "mesma área", 1380, 760, 60, "g", BR)


def b(c):  # o modelo padrão
    E.capa_base(c, COR); E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "Impulso", 76, 450, 210, "g", BR)
    E.escreve(c, "e Q = m·v", 76, 660, 190, "g", BR)
    E.escreve(c, "do zero", 84, 860, 160, "i", BR)
    E.simbolo(c, 1600, 780, 240, cor=E.mix(COR, BR, 0.82), forma="orbita")


def d(c):  # o macete: bater e voltar dá o dobro
    palco(c)
    E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "bater e voltar", 84, 340, 110, "i", BR)
    E.escreve(c, "2× o impulso", 76, 560, 190, "g", BR)
    claro = E.mix(COR, BR, 0.5)
    F.parede(c, 1700, 640, 1000, 1, 1.0, True)
    F.seta(c, 1100, 720, 1640, 720, F.VEL, 1.0, 16)
    F.seta(c, 1640, 900, 1100, 900, claro, 1.0, 16)
    E.escreve(c, "10 → −10", 84, 900, 110, "g", claro)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_por_que_o_airbag_salva", a), ("capa_B_impulso_e_quantidade_de_movimento", b), ("capa_C_bater_e_voltar_dobro", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
