"""Capas do FIS-DIN-010 (1280x720). Uso: python capa.py"""
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


def curva_capa(c, cx, cy, r, cor):
    import math
    pt = M.paint(cor, 0.8, stroke=10)
    pt.setPathEffect(skia.DashPathEffect.Make([30, 22], 0))
    c.drawCircle(cx, cy, r, pt)
    c.drawCircle(cx, cy, 18, M.paint(cor))
    a = math.radians(140)
    P = (cx + r * math.cos(a), cy - r * math.sin(a))
    E.bola(c, *P, 60, AMARELO)
    F.seta(c, *P, P[0] + (cx - P[0]) * 0.65, P[1] + (cy - P[1]) * 0.65, cor, 1.0, 26, cabeca=80)


def a(c):  # o gancho: não existe força para fora
    E.capa_base(c, COR); E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "Na curva,", 84, 400, 160, "g", BR)
    E.escreve(c, "a força é", 84, 580, 160, "g", BR)
    E.escreve(c, "para dentro", 84, 770, 160, "g", AMARELO)
    E.escreve(c, "a centrífuga não existe", 84, 930, 90, "i", BR)
    curva_capa(c, 1500, 560, 300, BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Física", "Força", "centrípeta", "a que busca o centro")


def d(c):  # o macete: v × 2 → F × 4
    palco(c)
    E.escreve(c, "dobrou a velocidade?", 84, 330, 110, "i", BR)
    E.escreve(c, "v × 2", 84, 600, 220, "g", BR)
    E.escreve(c, "→ F × 4", 640, 600, 220, "g", E.mix(COR, BR, 0.5))
    E.escreve(c, "a velocidade está ao quadrado", 84, 850, 90, "i", BR)


CAPAS = (("capa_A_a_forca_e_para_dentro", a), ("capa_B_forca_centripeta", b), ("capa_C_v_dobra_forca_quadruplica", d))


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in CAPAS:
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
