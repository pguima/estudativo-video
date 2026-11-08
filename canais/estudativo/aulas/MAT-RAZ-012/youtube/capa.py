"""Capas do MAT-RAZ-012 (1280x720). Uso: python capa.py"""
import subprocess, sys
from pathlib import Path
RAIZ = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(RAIZ / "_ferramentas"))
import skia
import editorial as E
import motor as M
BR = "#FFFFFF"
COR = E.MATERIAS["Matemática"]["cor"]
CL = E.mix(COR, BR, 0.55)


def a(c):  # o gancho: 10 kg custa R$ 100? não, R$ 70
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "5 kg: R$ 50", 84, 380, 140, "g", BR)
    E.escreve(c, "10 kg: R$ 100?", 84, 580, 140, "g", BR)
    E.risco(c, 74, 600, 1080, 470, 9, 0, "#FFD500", 26)
    E.escreve(c, "R$ 70", 1180, 600, 200, "g", "#FFD500")
    E.escreve(c, "que tipo de relação é essa?", 84, 880, 110, "i", BR)


def b(c):  # o modelo
    E.capa_modelo(c, "Matemática", "Regra de", "três", "5 situações")


def d(c):  # o macete: direta, inversa ou nenhuma
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "primeiro, o tipo:", 84, 340, 130, "i", BR)
    E.escreve(c, "direta", 84, 560, 170, "g", BR)
    E.escreve(c, "inversa", 84, 750, 170, "g", CL)
    E.escreve(c, "ou nenhuma?", 84, 940, 170, "g", BR)
    for i, n in enumerate("12345"):
        E.bola(c, 1500 + (i % 2) * 190, 360 + i * 130, 62, COR)
        E.centro(c, n, 1500 + (i % 2) * 190, 360 + i * 130 + 26, 72, "g", BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_10kg_70_reais", a), ("capa_B_cinco_situacoes", b), ("capa_C_direta_inversa_nenhuma", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
