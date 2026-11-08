"""Capas do MAT-POL-011 (1280x720). Uso: python capa.py"""
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
VERMELHO = "#FF6B6B"


def plano(c, ox, oy, u, xmin, xmax, ymin, ymax, cor=BR):
    """malha simples com os eixos; devolve valor → pixel"""
    for v in range(xmin, xmax + 1):
        M.line(c, ox + v * u, oy - ymax * u, ox + v * u, oy - ymin * u, cor, 0.18, 2)
    for v in range(ymin, ymax + 1):
        M.line(c, ox + xmin * u, oy - v * u, ox + xmax * u, oy - v * u, cor, 0.18, 2)
    M.arrow(c, ox + xmin * u - 10, oy, ox + xmax * u + 40, oy, cor, 1, 7, 26)
    M.arrow(c, ox, oy - ymin * u + 10, ox, oy - ymax * u - 40, cor, 1, 7, 26)
    return lambda x, y: (ox + x * u, oy - y * u)


def bandeira(c, f, cor, pts):
    path = skia.Path(); path.addPoly([f(*p) for p in pts[1:]], True)
    c.drawPath(path, M.paint(cor))
    M.line(c, *f(*pts[0]), *f(*pts[1]), BR, 1, 10)


def a(c):  # o gancho: (2, 3) refletido no eixo y
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    f = plano(c, 520, 700, 95, -4, 4, -4, 4)
    M.line(c, 520, 700 - 4 * 95 - 30, 520, 700 + 4 * 95 + 10, "#BFE4FF", 0.9, 16)
    bandeira(c, f, AMARELO, [(2, 1), (2, 3), (3.5, 2.5), (2, 2)])
    bandeira(c, f, E.mix(AMARELO, BR, 0.5), [(-2, 1), (-2, 3), (-3.5, 2.5), (-2, 2)])
    c.drawCircle(*f(2, -3), 20, M.paint(VERMELHO))
    E.risco(c, f(2, -3)[0] - 40, f(2, -3)[1] + 40, f(2, -3)[0] + 40, f(2, -3)[1] - 40, 9, 0, VERMELHO, 16)
    E.escreve(c, "(2, 3) no", 1010, 330, 110, "g", BR)
    E.escreve(c, "espelho y", 1010, 460, 110, "g", BR)
    E.escreve(c, "(2, −3)", 1010, 640, 130, "g", VERMELHO)
    E.risco(c, 990, 650, 1440, 540, 9, 0, VERMELHO, 22)
    E.escreve(c, "(−2, 3)", 1010, 860, 170, "g", AMARELO)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Reflexão", "e rotação", "e translação")


def d(c):  # o atalho: girar 90° = trocar e mudar o sinal
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "o atalho do giro", 90, 340, 120, "i", BR)
    E.escreve(c, "troca e", 90, 540, 170, "g", BR)
    E.escreve(c, "muda o sinal", 90, 710, 170, "g", AMARELO)
    E.escreve(c, "(2, 3) → (−3, 2)", 90, 920, 110, "g", claro)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_espelho_y", a), ("capa_B_reflexao_e_rotacao", b), ("capa_C_troca_e_muda_o_sinal", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
