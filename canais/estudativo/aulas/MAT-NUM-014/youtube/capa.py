"""Capas do MAT-NUM-014 (1280x720). Uso: python capa.py"""
import subprocess, sys
from pathlib import Path
RAIZ = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(RAIZ / "_ferramentas"))
import skia
import editorial as E
import motor as M
BR = "#FFFFFF"
COR = E.MATERIAS["Matemática"]["cor"]
AMARELO = "#FFD500"
CLARO = E.mix(COR, BR, 0.5)


def fundo_escuro(c):
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)


def a(c):  # o gancho: o troco maior que o dinheiro
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "pagou R$ 200", 84, 340, 150, "i", BR)
    E.escreve(c, "troco de", 84, 590, 240, "g", BR)
    E.escreve(c, "R$ 205?", 84, 880, 310, "g", AMARELO)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Montar a", "expressão", "de um problema")


def d(c):  # o atalho: a frase primeiro
    fundo_escuro(c)
    E.escreve(c, "o atalho", 84, 340, 150, "i", BR)
    E.escreve(c, "a frase", 80, 580, 260, "g", BR)
    E.escreve(c, "primeiro", 84, 800, 220, "i", BR)
    E.escreve(c, "200 − (75 + 80)", 84, 985, 150, "g", AMARELO)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_troco_205", a), ("capa_B_montar_expressao", b), ("capa_C_frase_primeiro", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
