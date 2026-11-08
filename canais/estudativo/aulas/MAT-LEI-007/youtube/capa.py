"""Capas do MAT-LEI-007 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: 5 problemas de enunciado comprido
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    c.drawCircle(1500, 470, 250, M.paint(BR))
    for dx in (-60, 60):
        M.rrect(c, 1500 + dx - 32, 470 - 110, 64, 220, 16, COR)
    E.escreve(c, "5 problemas", 84, 400, 170, "g", BR)
    E.escreve(c, "de texto comprido", 84, 560, 120, "i", BR)
    E.escreve(c, "você resolve?", 84, 800, 160, "g", AMARELO)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Praticando", "a leitura", "5 problemas de prova")


def d(c):  # o ângulo da decisão: táxi ou aplicativo
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "táxi ou", 84, 380, 180, "g", BR)
    E.escreve(c, "aplicativo?", 84, 580, 180, "g", BR)
    E.escreve(c, "a tabela decide:", 84, 820, 100, "i", BR)
    E.escreve(c, "empate em 5 km", 84, 960, 120, "g", AMARELO)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_5_problemas", a), ("capa_B_praticando_a_leitura", b), ("capa_C_taxi_ou_aplicativo", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
