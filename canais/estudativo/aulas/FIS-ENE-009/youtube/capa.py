"""Capas do FIS-ENE-009 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: por que a branca para?
    E.capa_base(c, COR); E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "na sinuca", 84, 380, 130, "i", BR)
    E.escreve(c, "a branca", 84, 600, 200, "g", BR)
    E.escreve(c, "para?", 84, 820, 210, "g", AMARELO)
    E.bola(c, 1320, 620, 120, BR)
    E.bola(c, 1640, 620, 120, E.mix(COR, "#000000", 0.25))
    F.seta(c, 1560, 420, 1840, 420, BR, 1.0, 20)


def b(c):  # o modelo padrão
    E.capa_base(c, COR); E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "Colisões", 76, 450, 210, "g", BR)
    E.escreve(c, "e restituição", 76, 640, 150, "g", BR)
    E.escreve(c, "elástica ou inelástica", 84, 840, 100, "i", BR)
    E.simbolo(c, 1620, 780, 230, cor=E.mix(COR, BR, 0.82), forma="orbita")


def d(c):  # o macete: massas iguais trocam de velocidade
    palco(c)
    E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "massas iguais, elástica", 84, 340, 110, "i", BR)
    E.escreve(c, "trocam de", 76, 560, 170, "g", BR)
    E.escreve(c, "velocidade", 76, 750, 170, "g", E.mix(COR, BR, 0.5))
    E.bola(c, 1560, 920, 90, BR)
    E.bola(c, 1770, 920, 90, COR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_por_que_a_branca_para", a), ("capa_B_colisoes_e_restituicao", b), ("capa_C_massas_iguais_trocam", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
