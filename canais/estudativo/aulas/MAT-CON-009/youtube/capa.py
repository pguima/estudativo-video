"""Capas do MAT-CON-009 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: 5 situações, pause e resolva
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "5", 70, 820, 640, "g", AMARELO)
    E.escreve(c, "situações", 520, 470, 150, "g", BR)
    E.escreve(c, "pause e resolva", 520, 640, 110, "i", BR)
    x = 540
    for s in ("Venn", "conjuntos", "0,2777…", "]−∞, 4]"):
        w = E.larg(s, "g", 54) + 54 * 1.1
        E.pilula(c, s, x + w / 2, 860, 54, "g", fundo=BR, cor=COR)
        x += w + 30


def b(c):  # o modelo
    E.capa_modelo(c, "Matemática", "Conjuntos", "e reais", "praticando")


def d(c):  # o atalho: teste um número
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "teste", 84, 380, 130, "i", BR)
    E.escreve(c, "um número", 76, 600, 220, "g", BR)
    E.escreve(c, "em cada resposta", 84, 820, 110, "i", E.mix(COR, BR, 0.6))
    E.bola(c, 1620, 860, 140, AMARELO)
    E.centro(c, "2", 1620, 930, 200, "g", COR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_cinco_situacoes", a), ("capa_B_conjuntos_e_reais", b), ("capa_C_teste_um_numero", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
