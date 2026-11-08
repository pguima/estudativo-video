"""Capas do MAT-EST-016 (1280x720). Uso: python capa.py"""
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


def turma(c, x0, x1, y, vals, cor=BR, r=26):
    """notas de 0 a 8 como bolinhas sobre a reta (valor repetido empilha)"""
    vx = lambda v: x0 + v * (x1 - x0) / 8
    M.line(c, x0 - 20, y, x1 + 20, y, BR, 0.8, 6)
    for v in range(9):
        M.line(c, vx(v), y - 14, vx(v), y + 14, BR, 0.8, 5)
    vistos = {}
    for v in vals:
        k = vistos.get(v, 0); vistos[v] = k + 1
        c.drawCircle(vx(v), y - r - 10 - k * 58, r, M.paint(cor))
    return vx


def a(c):  # o gancho: mesma média, turmas diferentes
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "mesma média,", 84, 330, 110, "i", BR)
    E.escreve(c, "turmas", 84, 500, 150, "g", BR)
    E.escreve(c, "diferentes", 84, 650, 150, "g", AMARELO)
    vx = turma(c, 1080, 1800, 470, [3, 4, 4, 5])
    turma(c, 1080, 1800, 860, [0, 2, 6, 8], AMARELO)
    M.line(c, vx(4), 250, vx(4), 900, BR, 0.9, 6, dash=[18, 14])
    E.centro(c, "média 4", vx(4), 230, 56, "b", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Desvio", "padrão", "e variância, do zero")


def d(c):  # o atalho: somar não muda, dobrar dobra
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "desvio padrão:", 84, 340, 110, "i", BR)
    E.escreve(c, "+1 em todos", 84, 540, 140, "g", BR)
    E.escreve(c, "não muda", 1060, 540, 120, "g", AMARELO)
    E.escreve(c, "×2 em todos", 84, 780, 140, "g", BR)
    E.escreve(c, "dobra", 1060, 780, 120, "g", AMARELO)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_mesma_media", a), ("capa_B_desvio_padrao", b), ("capa_C_somar_nao_muda", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
