"""Capas do FIS-DIN-009 (1280x720). Uso: python capa.py"""
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


def mesa_capa(c, cor):
    M.rrect(c, 1100, 560, 560, 30, 8, cor)
    M.rrect(c, 1250, 410, 220, 150, 16, cor)
    M.line(c, 1470, 480, 1700, 480, cor, 1.0, 8)
    c.drawCircle(1700, 520, 42, M.paint(cor, 1.0, stroke=12))
    M.line(c, 1742, 520, 1742, 720, cor, 1.0, 8)
    M.rrect(c, 1660, 720, 165, 150, 16, AMARELO)


def a(c):  # o gancho: a aceleração numa linha
    E.capa_base(c, COR); E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "Blocos e", 84, 400, 170, "g", BR)
    E.escreve(c, "polias", 84, 590, 170, "g", AMARELO)
    E.escreve(c, "numa linha", 84, 780, 150, "g", BR)
    E.escreve(c, "o atalho do corpo só", 84, 940, 90, "i", BR)
    mesa_capa(c, BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Física", "Blocos e", "polias", "um corpo só")


def d(c):  # o macete: a = (a favor − contra) / massas
    palco(c)
    E.escreve(c, "o atalho dos blocos ligados", 84, 330, 100, "i", BR)
    E.escreve(c, "a =", 84, 640, 200, "g", BR)
    E.formula(c, "f{a favor − contra}{soma das massas}", 420, 640, 130, "g", BR)
    E.escreve(c, "e a tração some da conta", 84, 930, 90, "i", E.mix(COR, BR, 0.5))


CAPAS = (("capa_A_blocos_e_polias_numa_linha", a), ("capa_B_blocos_ligados_e_polias", b), ("capa_C_corpo_so", d))


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in CAPAS:
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
