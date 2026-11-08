"""Capas do MAT-RAZ-003 (1280x720). Uso: python capa.py"""
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


def pacotes(c, n, x, y, w, h, cor, txt, tinta, size):
    for i in range(n):
        M.rrect(c, x + i * (w + 14), y, w, h, 18, cor)
        E.centro(c, txt, x + i * (w + 14) + w / 2, y + h / 2 + size * 0.36, size, "g", tinta)


def a(c):  # o gancho: razão 3 para 5, soma 64
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "3 para 5", 84, 380, 170, "g", BR)
    E.escreve(c, "somam 64?", 84, 580, 170, "g", AMARELO)
    pacotes(c, 3, 1120, 560, 110, 110, BR, "k", COR, 80)
    pacotes(c, 5, 1120, 700, 110, 110, "#0E0A3A", "k", BR, 80)
    E.escreve(c, "1 letra resolve", 84, 960, 120, "i", BR)


def b(c):  # o modelo
    E.capa_modelo(c, "Matemática", "O truque", "do k", "razão e soma")


def d(c):  # o atalho: divida pelo número de partes
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    cl = E.mix(COR, BR, 0.55)
    E.escreve(c, "o atalho:", 84, 340, 140, "i", BR)
    E.escreve(c, "total ÷ partes", 76, 540, 180, "g", BR)
    E.formula(c, "64 ÷ 8 = 8", 84, 820, 170, "g", cl)
    pacotes(c, 3, 1160, 700, 110, 110, COR, "8", BR, 64)
    pacotes(c, 5, 1160, 840, 110, 110, cl, "8", "#07070F", 64)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_3_para_5_somam_64", a), ("capa_B_truque_do_k", b), ("capa_C_total_dividido_partes", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
