"""Capas do FIS-CIN-019 (1280x720). Uso: python capa.py"""
import math, subprocess, sys
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


def disco(c, cx, cy, R, ang, cor_linha):
    c.drawCircle(cx, cy, R, M.paint(BR, 0.18))
    c.drawCircle(cx, cy, R, M.paint(cor_linha, 1.0, stroke=8))
    g = math.radians(ang)
    M.line(c, cx, cy, cx + math.cos(g) * R, cy - math.sin(g) * R, cor_linha, 1.0, 6)
    return g


def a(c):  # o gancho: quem está na borda anda mais rápido
    E.capa_base(c, COR); E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "mesma volta,", 84, 390, 130, "i", BR)
    E.escreve(c, "quem é", 84, 580, 170, "g", BR)
    E.escreve(c, "mais rápido?", 84, 770, 170, "g", BR)
    cx, cy, R = 1520, 660, 270
    g = disco(c, cx, cy, R, 20, BR)
    for fr, L, cor in ((1.0, 280, AMARELO), (0.35, 100, BR)):
        P = (cx + math.cos(g) * R * fr, cy - math.sin(g) * R * fr)
        E.bola(c, *P, 38, E.mix(COR, BR, 0.85) if fr < 1 else AMARELO)
        tx, ty = -math.sin(g), -math.cos(g)
        F.seta(c, P[0], P[1], P[0] + tx * L, P[1] + ty * L, cor, 1.0, 16)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Física", "Velocidade", "angular", "e linear")


def d(c):  # o macete: v proporcional a R
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "dobrou o raio,", 84, 340, 120, "i", BR)
    E.escreve(c, "dobrou a", 76, 520, 170, "g", BR)
    E.escreve(c, "velocidade", 76, 700, 170, "g", BR)
    E.formula(c, "v = ω · R", 84, 900, 130, "g", E.mix(COR, BR, 0.5))
    claro = E.mix(COR, BR, 0.5)
    for i in range(3):
        x, yb = 1300 + i * 190, 900
        M.rrect(c, x, yb - 160 * (i + 1), 140, 160 * (i + 1), 16, COR if i == 2 else claro)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_quem_e_mais_rapido", a), ("capa_B_velocidade_angular_e_linear", b), ("capa_C_dobrou_o_raio", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
