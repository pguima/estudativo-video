"""Capas do MAT-POT-009 (1280x720). Uso: python capa.py"""
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


def palco(c):
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)


def a(c):  # o gancho: o erro de somar o de dentro
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.formula(c, "r{2} + r{3} = r{5}", 84, 540, 240, cor=BR)
    E.risco(c, 60, 590, 1510, 300, 1.0, 0.0, cor="#FF5A5F", largura=24)
    E.escreve(c, "isso está errado", 84, 900, 190, "g", AMARELO)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Simplificar", "radicais", "e somar raízes")


def d(c):  # o atalho: o maior quadrado que divide
    palco(c)
    E.escreve(c, "ache o maior quadrado", 84, 340, 160, "i", BR)
    E.formula(c, "r{72}", 84, 670, 250, cor=BR)
    E.escreve(c, "=", 650, 650, 220, "g", BR)
    E.formula(c, "6r{2}", 830, 670, 250, cor=AMARELO)
    E.escreve(c, "sem fatorar", 84, 930, 180, "g", BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_nao_vira_raiz_de_5", a), ("capa_B_simplificar_radicais", b), ("capa_C_maior_quadrado", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
