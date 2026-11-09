"""Capas do FIS-OND-008 (1280x720). Uso: python capa.py"""
import subprocess, sys
from pathlib import Path
RAIZ = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(RAIZ / "_ferramentas"))
import skia
import editorial as E
import fisica as F
import motor as M
BR = "#FFFFFF"
AMARELO = "#FFD500"
COR = E.MATERIAS["Física"]["cor"]
E.usar("Física")


def frentes(c, x0, y, n, passo, desloca, cor, larg=7):
    """círculos de centros que andam: apertados à direita"""
    for k in range(n):
        r = 60 + k * passo
        cx = x0 - k * desloca
        c.drawCircle(cx, y, r, M.paint(cor, 0.9 - 0.12 * k, stroke=larg))


def a(c):  # o gancho: a sirene muda de tom
    E.capa_base(c, COR); E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "a sirene", 84, 400, 160, "g", BR)
    E.escreve(c, "muda de tom?", 84, 580, 160, "g", BR)
    E.escreve(c, "o efeito Doppler", 84, 860, 110, "i", BR)
    frentes(c, 1680, 560, 5, 72, 40, AMARELO)
    E.bola(c, 1680, 560, 46, AMARELO)
    E.escreve(c, "agudo", 1660, 210, 64, "g", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Física", "Efeito", "Doppler", "do zero")


def d(c):  # o macete: aproximou sobe, afastou desce
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "o atalho dos sinais", 84, 340, 120, "i", BR)
    E.pilula(c, "aproximou ↑", 520, 560, 120, "g", fundo=COR, cor=BR)
    E.pilula(c, "afastou ↓", 1360, 560, 120, "g", fundo=F.NEG, cor=BR)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "decida antes da conta", 84, 900, 100, "b", claro)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_a_sirene_muda_de_tom", a), ("capa_B_efeito_doppler", b), ("capa_C_aproximou_sobe", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
