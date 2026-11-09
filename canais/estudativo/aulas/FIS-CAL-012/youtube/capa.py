"""Capas do FIS-CAL-012 (1280x720). Uso: python capa.py"""
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




def a(c):  # o erro: o sinal esquecido na compressão
    E.capa_base(c, COR); E.capa_rotulo(c, "Física", COR)
    E.formula(c, "−100 − 300", 84, 420, 170, "g", BR)
    E.formula(c, "= −400 J?", 84, 630, 170, "g", BR)
    E.risco(c, 70, 660, 900, 480, 9, 0, AMARELO, 30)
    E.escreve(c, "o sinal que todo mundo erra", 84, 860, 92, "i", BR)
    claro = E.mix(COR, BR, 0.75)
    M.rrect(c, 1330, 380, 380, 300, 30, claro, 1.0)
    F.seta(c, 1520, 120, 1520, 360, BR, 1.0, 22)
    E.formula(c, "τ < 0", 1560, 260, 90, "g", BR)


def b(c):  # o modelo padrão
    E.capa_base(c, COR); E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "Primeira lei", 76, 430, 190, "g", BR)
    E.escreve(c, "da termodinâmica", 76, 620, 150, "g", BR)
    E.escreve(c, "sem errar o sinal", 84, 840, 140, "i", BR)
    E.simbolo(c, 1640, 820, 190, cor=E.mix(COR, BR, 0.82), forma="orbita")


def d(c):  # o macete: a caixa
    palco_capa(c)
    E.escreve(c, "a caixa", 84, 380, 190, "g", BR)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "entra soma, sai subtrai", 84, 540, 100, "i", claro)
    M.rrect(c, 760, 640, 360, 260, 30, claro, 1.0)
    F.seta(c, 420, 770, 730, 770, BR, 1.0, 20)
    F.seta(c, 1150, 770, 1460, 770, BR, 1.0, 20)
    E.formula(c, "+", 560, 720, 110, "g", BR, 1.0, "center")
    E.formula(c, "−", 1300, 720, 110, "g", BR, 1.0, "center")


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_o_sinal_do_trabalho", a), ("capa_B_primeira_lei", b), ("capa_C_a_caixa", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
