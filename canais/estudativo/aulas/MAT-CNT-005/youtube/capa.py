"""Capas do MAT-CNT-005 (1280x720). Uso: python capa.py"""
import subprocess, sys
from pathlib import Path
RAIZ = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(RAIZ / "_ferramentas"))
import skia
import editorial as E
import motor as M
BR = "#FFFFFF"
AMARELO = "#FFD500"
COR = E.MATERIAS["Matemática"]["cor"]


def letra(c, cx, cy, s, ch, fundo=BR, tinta=None):
    r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - s / 2, cy - s / 2, s, s), s * 0.16, s * 0.16)
    c.drawRRect(r, M.paint(fundo))
    E.centro(c, ch, cx, cy + s * 0.22, s * 0.6, "g", tinta or COR)


def a(c):  # o gancho: AMOR, ROMA, RAMO, MORA... quantas?
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    for i, ch in enumerate("AMOR"):
        letra(c, 180 + i * 230, 400, 200, ch)
    E.escreve(c, "roma, ramo, mora...", 84, 680, 110, "i", BR)
    E.escreve(c, "quantas?", 84, 900, 200, "g", AMARELO)
    E.bola(c, 1560, 640, 230, "#FFFFFF")
    E.centro(c, "24", 1560, 640 + 76, 210, "g", COR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Filas e", "anagramas", "permutação simples")


def d(c):  # o macete: o bloco
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "sempre juntas?", 84, 330, 130, "i", BR)
    r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(70, 420, 420, 240), 40, 40)
    c.drawRRect(r, M.paint(COR, 0.35)); c.drawRRect(r, M.paint(AMARELO, 1, stroke=10))
    letra(c, 180, 540, 170, "A", COR, BR); letra(c, 380, 540, 170, "I", COR, BR)
    for i, ch in enumerate("BRSL"):
        letra(c, 640 + i * 200, 540, 170, ch, BR, COR)
    E.escreve(c, "cole em bloco: 5! × 2", 84, 900, 130, "g", AMARELO)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_quantas_amor", a), ("capa_B_filas_anagramas", b), ("capa_C_bloco", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
