"""Capas do MAT-LEI-001 (1280x720). Uso: python capa.py"""
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


def onibus(c, x, y, w, cor, frac=1.0):
    h = w * 0.5
    c.save(); c.clipRect(skia.Rect.MakeXYWH(x - 4, y - 4, w * frac + 4, h + w * 0.2))
    M.rrect(c, x, y, w, h, w * 0.08, cor)
    for i in range(4):
        M.rrect(c, x + w * 0.06 + i * w * 0.225, y + h * 0.14, w * 0.18, h * 0.34, 6, COR, 0.85)
    for fx in (0.22, 0.78):
        c.drawCircle(x + w * fx, y + h, w * 0.085, M.paint("#121214"))
    c.restore()


def a(c):  # o gancho: 7,3 ônibus não existe
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "292 ÷ 40 =", 84, 400, 170, "g", BR)
    E.escreve(c, "7,3", 1040, 400, 170, "g", AMARELO)
    E.escreve(c, "ônibus?", 1380, 400, 150, "i", BR)
    for i in range(7):
        onibus(c, 90 + i * 232, 520, 210, BR)
    onibus(c, 90 + 7 * 232, 520, 210, AMARELO, 0.3)
    E.escreve(c, "a resposta tem que", 84, 900, 110, "i", BR)
    E.escreve(c, "fazer sentido", 870, 900, 120, "g", AMARELO)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Achar a", "pergunta", "e os dados úteis")


def d(c):  # o atalho: a tabuada no lugar da divisão
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "o atalho da", 84, 350, 140, "i", BR)
    E.escreve(c, "tabuada", 76, 580, 230, "g", BR)
    y = 820
    M.line(c, 120, y, 1800, y, BR, 1, 8)
    for v, x, cor in (("280", 420, BR), ("292", 900, AMARELO), ("320", 1500, BR)):
        c.drawCircle(x, y, 22, M.paint(cor))
        E.centro(c, v, x, y + 140, 120, "g", cor)
    E.centro(c, "7 × 40", 420, y - 60, 80, "b", E.mix(COR, BR, 0.55))
    E.centro(c, "8 × 40", 1500, y - 60, 80, "b", E.mix(COR, BR, 0.55))


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_7_virgula_3_onibus", a), ("capa_B_achar_a_pergunta", b), ("capa_C_tabuada", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
