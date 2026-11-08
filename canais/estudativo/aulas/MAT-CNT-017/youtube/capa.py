"""Capas do MAT-CNT-017 (1280x720). Uso: python capa.py"""
import subprocess, sys
from pathlib import Path
RAIZ = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(RAIZ / "_ferramentas"))
import skia
import editorial as E
import motor as M
BR = "#FFFFFF"
AMARELO = "#FFD500"
AZUL, VERM = "#3D7DD8", "#D94B3D"
COR = E.MATERIAS["Matemática"]["cor"]


def a(c):  # o gancho: 2 azuis da urna, devolvendo 36%, sem devolver 30%
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(110, 260, 470, 520), 70, 70), M.paint(BR, 0.25))
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(110, 260, 470, 520), 70, 70), M.paint(BR, 1, stroke=10))
    for (x, y, cor) in ((220, 680, AZUL), (345, 680, AZUL), (470, 680, AZUL), (282, 560, VERM), (407, 560, VERM)):
        E.bola(c, x, y, 58, cor)
    E.escreve(c, "2 azuis?", 680, 380, 150, "g", BR)
    E.escreve(c, "devolvendo:", 680, 600, 100, "i", BR)
    E.escreve(c, "36%", 1250, 610, 140, "g", AMARELO)
    E.escreve(c, "sem devolver:", 680, 820, 100, "i", BR)
    E.escreve(c, "30%", 1350, 830, 140, "g", AMARELO)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Com ou sem", "reposição", "sorteios em sequência")


def d(c):  # o macete: mesma cor, desce 1 em cima e 1 embaixo
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "sem devolver, mesma cor:", 84, 380, 100, "i", BR)
    for k, (n, d_) in enumerate(((3, 5), (2, 4), (1, 3))):
        E.fracao(c, n, d_, 220 + k * 420, 640, 190, AMARELO if k else BR)
    for k in range(2):
        M.arrow(c, 340 + k * 420, 620, 520 + k * 420, 620, BR, 1, 10, 34, 1)
    E.escreve(c, "desce 1 em cima e 1 embaixo", 84, 1000, 90, "g", BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_duas_azuis", a), ("capa_B_com_sem_reposicao", b), ("capa_C_desce_um", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
