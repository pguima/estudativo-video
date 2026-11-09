"""Capas do FIS-DIN-002 (1280x720). Uso: python capa.py"""
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


def palco(c):
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Física", COR)


def fsub(c, base, sb, x, y, size, cor):
    """letra com subscrito (F com R embaixo); devolve a largura"""
    E.escreve(c, base, x, y, size, "g", cor)
    w = E.larg(base, "g", size)
    E.escreve(c, sb, x + w + size * 0.02, y + size * 0.2, size * 0.6, "g", cor)
    return w + E.larg(sb, "g", size * 0.6) + size * 0.06


def a(c):  # o gancho: mesma força, carrinho vazio x cheio
    E.capa_base(c, COR); E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "Mesma força,", 84, 400, 170, "g", BR)
    E.escreve(c, "outra", 84, 590, 170, "g", BR)
    E.escreve(c, "aceleração", 84, 780, 170, "g", AMARELO)
    E.escreve(c, "por quê?", 84, 940, 100, "i", BR)
    E.orbita(c, 1560, 560, 280, E.mix(COR, BR, 0.82))


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Física", "F = m·a", "2ª lei", "de Newton")


def d(c):  # o macete: proporção
    palco(c)
    E.escreve(c, "sem refazer a conta", 84, 330, 110, "i", BR)
    E.escreve(c, "massa × 2", 84, 560, 170, "g", BR)
    E.escreve(c, "→ a ÷ 2", 84, 760, 170, "g", E.mix(COR, BR, 0.5))
    E.escreve(c, "leia a fórmula como proporção", 84, 930, 80, "i", BR)
    E.selo(c, 1650, 560, 150, True)


CAPAS = (("capa_A_mesma_forca_outra_aceleracao", a), ("capa_B_segunda_lei_de_newton", b), ("capa_C_proporcao_sem_conta", d))


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in CAPAS:
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
