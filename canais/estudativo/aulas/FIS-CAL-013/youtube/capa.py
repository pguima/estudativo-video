"""Capas do FIS-CAL-013 (1280x720). Uso: python capa.py"""
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




def a(c):  # o erro: "isotérmica não troca calor"
    E.capa_base(c, COR); E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "isotérmica", 84, 400, 170, "g", BR)
    E.escreve(c, "não troca calor?", 84, 590, 130, "g", BR)
    E.risco(c, 70, 620, 1100, 470, 9, 0, AMARELO, 30)
    E.escreve(c, "troca, sim: Q = τ", 84, 820, 110, "g", AMARELO)
    E.escreve(c, "o erro mais comum", 84, 960, 80, "i", BR)


def b(c):  # o modelo padrão
    E.capa_base(c, COR); E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "Primeira lei", 76, 430, 190, "g", BR)
    E.escreve(c, "em cada caso", 76, 620, 170, "g", BR)
    E.escreve(c, "qual termo vira zero", 84, 840, 120, "i", BR)
    E.simbolo(c, 1640, 820, 190, cor=E.mix(COR, BR, 0.82), forma="orbita")


def d(c):  # o macete: o que não muda zera um termo
    palco_capa(c)
    E.escreve(c, "o que não muda", 84, 360, 150, "g", BR)
    E.escreve(c, "zera um termo", 84, 500, 110, "i", BR)
    claro = E.mix(COR, BR, 0.5)
    for i, (l, r) in enumerate((("T parada", "ΔU = 0"), ("V parado", "τ = 0"), ("sem calor", "Q = 0"))):
        y = 680 + i * 140
        E.formula(c, l, 84, y, 90, "g", BR)
        E.formula(c, "→ " + r, 640, y, 90, "g", claro)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_isotermica_troca_calor", a), ("capa_B_primeira_lei_em_cada_caso", b), ("capa_C_o_que_nao_muda", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
