"""Capas do FIS-ENE-001 (1280x720). Uso: python capa.py"""
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


def palco(c):
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)


def mochila(c, cx, cy, w, cor):
    h = w * 1.2
    c.drawArc(skia.Rect.MakeXYWH(cx - w * 0.22, cy - h / 2 - w * 0.3, w * 0.44, w * 0.5), 180, 180, False, M.paint(BR, 1, stroke=w * 0.07))
    M.rrect(c, cx - w / 2, cy - h / 2, w, h, w * 0.1, cor)
    M.rrect(c, cx - w * 0.32, cy + h * 0.08, w * 0.64, h * 0.32, w * 0.08, E.mix(cor, "#000000", 0.2))


def a(c):  # o gancho: segurar parado = trabalho zero
    E.capa_base(c, COR); E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "segurar parado", 84, 380, 120, "i", BR)
    E.escreve(c, "trabalho", 84, 600, 190, "g", BR)
    E.escreve(c, "= zero", 84, 820, 210, "g", AMARELO)
    claro = E.mix(COR, BR, 0.8)
    mochila(c, 1520, 680, 300, claro)
    F.seta(c, 1520, 420, 1520, 150, BR, 1.0, 22)
    E.escreve(c, "?", 1700, 330, 200, "g", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Física", "Trabalho", "da força", "do zero")


def d(c):  # o macete: força perpendicular não trabalha
    palco(c)
    E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "força perpendicular", 84, 340, 110, "i", BR)
    E.escreve(c, "trabalho zero", 76, 540, 170, "g", BR)
    claro = E.mix(COR, BR, 0.5)
    for i, (ang, txt) in enumerate(((0, "+"), (180, "−"), (90, "0"))):
        cx, cy = 360 + i * 560, 830
        M.line(c, cx - 200, cy + 80, cx + 200, cy + 80, BR, 1, 6)
        M.rrect(c, cx - 70, cy - 40, 140, 120, 14, "#5A5A66")
        F.seta(c, cx - 160, cy + 140, cx + 160, cy + 140, F.VEL, 1.0, 12)
        dx, dy = math.cos(math.radians(ang)), -math.sin(math.radians(ang))
        P = (cx + 70 * dx, cy + 20 + 60 * dy) if ang != 90 else (cx, cy - 40)
        F.seta(c, P[0], P[1], P[0] + 150 * dx, P[1] + 150 * dy, claro, 1.0, 14)
        E.bola(c, cx + 200, cy - 110, 62, COR if txt != "0" else "#5A5A66")
        E.centro(c, txt, cx + 200, cy - 84, 76, "g", BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_segurar_parado_trabalho_zero", a), ("capa_B_trabalho_da_forca", b), ("capa_C_perpendicular_nao_trabalha", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
