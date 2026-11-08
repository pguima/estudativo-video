"""Capas do MAT-RAZ-011 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: L × 2, A ÷ 2, R × 4
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.formula(c, "R = k · f{L}{A}", 84, 470, 230, "g", BR)
    E.pilula(c, "L × 2", 1160, 300, 80, "g", fundo=BR, cor=COR)
    E.pilula(c, "A ÷ 2", 1160, 520, 80, "g", fundo=BR, cor=COR)
    E.escreve(c, "R × 4", 1420, 470, 170, "g", "#FFD500")
    E.escreve(c, "sem nenhum número", 84, 900, 120, "i", BR)


def b(c):  # o modelo
    E.capa_modelo(c, "Matemática", "Ler uma", "fórmula", "sem fazer conta")


def d(c):  # o macete: em cima direto, embaixo inverso
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "em cima,", 84, 420, 150, "i", BR)
    E.escreve(c, "direto", 700, 420, 190, "g", BR)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(84, 520, 1500, 18), 9, 9), M.paint(CL))
    E.escreve(c, "embaixo,", 84, 760, 150, "i", BR)
    E.escreve(c, "inverso", 700, 760, 190, "g", CL)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_resistencia_vezes_4", a), ("capa_B_ler_uma_formula", b), ("capa_C_em_cima_embaixo", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
