"""Capas do MAT-TOP-008 (1280x720). Uso: python capa.py"""
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


def det(c, linhas, x0, y0, cw, ch, size, cor=BR):
    for xb in (x0 - 20, x0 + len(linhas[0]) * cw + 20):
        M.line(c, xb, y0 - ch * 0.2, xb, y0 + len(linhas) * ch - ch * 0.1, cor, 1, 10)
    for i, lin in enumerate(linhas):
        for j, v in enumerate(lin):
            E.centro(c, str(v), x0 + j * cw + cw / 2, y0 + i * ch + ch * 0.6, size, "g", cor)


def a(c):  # o gancho: determinante zero = alinhados
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    det(c, [(1, 1, 1), (2, 3, 1), (3, 5, 1)], 140, 250, 190, 190, 150)
    E.escreve(c, "= 0", 780, 590, 220, "g", AMARELO)
    E.escreve(c, "3 pontos", 1250, 480, 130, "g", BR)
    E.escreve(c, "alinhados", 1250, 640, 130, "g", AMARELO)
    E.escreve(c, "numa conta só", 1250, 780, 90, "i", BR)


def b(c):  # o modelo
    E.capa_modelo(c, "Matemática", "Pontos", "alinhados?", "pelo determinante")


def d(c):  # o atalho: leve um ponto à origem
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "o atalho:", 84, 360, 140, "i", BR)
    E.escreve(c, "3 × 3 vira 2 × 2", 76, 570, 170, "g", BR)
    det(c, [(1, 2), (2, 4)], 160, 680, 170, 150, 120)
    E.escreve(c, "= 1·4 − 2·2 = 0", 620, 880, 120, "g", AMARELO)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_determinante_zero", a), ("capa_B_alinhamento", b), ("capa_C_vira_2x2", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
