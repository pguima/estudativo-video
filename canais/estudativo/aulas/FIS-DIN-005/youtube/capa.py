"""Capas do FIS-DIN-005 (1280x720). Uso: python capa.py"""
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


def mola_capa(c, x, y0, L, cor):
    F.mola(c, x, y0, x, y0 + L, 9, 90, cor, 1.0, 12, 40)


def a(c):  # o gancho: uma mola que mede força
    E.capa_base(c, COR); E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "Uma mola", 84, 400, 180, "g", BR)
    E.escreve(c, "que pesa", 84, 600, 180, "g", AMARELO)
    E.escreve(c, "a balança de gancho da feira", 84, 800, 84, "i", BR)
    M.line(c, 1400, 140, 1800, 140, BR, 1.0, 12)
    mola_capa(c, 1600, 140, 520, BR)
    M.rrect(c, 1490, 660, 220, 200, 24, AMARELO)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Física", "Tração", "e mola", "F = k·x")


def d(c):  # o macete: x é a deformação, não o tamanho
    palco(c)
    E.escreve(c, "o erro que derruba", 84, 330, 110, "i", BR)
    E.escreve(c, "x = 25 cm", 84, 560, 170, "g", "#E5484D")
    E.risco(c, 70, 590, 900, 420, 9, 0, AMARELO, 26)
    E.escreve(c, "x = 25 − 20", 84, 800, 170, "g", BR)
    E.escreve(c, "x é quanto a mola esticou", 84, 950, 80, "i", E.mix(COR, BR, 0.5))
    E.selo(c, 1650, 700, 150, True)


CAPAS = (("capa_A_uma_mola_que_pesa", a), ("capa_B_tracao_e_mola", b), ("capa_C_x_e_a_deformacao", d))


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in CAPAS:
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
