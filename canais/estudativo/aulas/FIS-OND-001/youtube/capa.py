"""Capas do FIS-OND-001 (1280x720). Uso: python capa.py"""
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


def pend(c, px, py, L, ang, r, rot):
    g = math.radians(ang)
    bx, by = px + L * math.sin(g), py + L * math.cos(g)
    M.line(c, px - 110, py, px + 110, py, BR, 1.0, 8)
    M.line(c, px, py, bx, by, BR, 1.0, 6)
    E.bola(c, bx, by, r, AMARELO)
    E._meio(c, rot, bx, by, r * 0.55, "g", "#1B1B1B", 1.0)


def a(c):  # o gancho: bola leve ou pesada, mesmo tempo
    E.capa_base(c, COR); E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "1 kg ou", 84, 420, 170, "g", BR)
    E.escreve(c, "10 kg?", 84, 610, 190, "g", BR)
    E.escreve(c, "o mesmo tempo", 84, 860, 110, "i", BR)
    pend(c, 1330, 150, 560, -18, 70, "1 kg")
    pend(c, 1640, 150, 560, -18, 105, "10 kg")


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Física", "Pêndulo", "e mola", "do zero")


def d(c):  # o macete: o período anda com a raiz
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "o macete do pêndulo", 84, 340, 120, "i", BR)
    E.formula(c, "T ≈ 2 · r{L}", 84, 600, 220, "g", BR)
    claro = E.mix(COR, BR, 0.5)
    E.pilula(c, "fio ×4", 1520, 470, 90, "g", fundo=COR, cor=BR)
    F.seta(c, 1520, 560, 1520, 700, claro, 1.0, 14)
    E.pilula(c, "tempo ×2", 1520, 800, 90, "g", fundo=E.CERTO, cor=BR)
    E.escreve(c, "use π = 3 se a prova mandar", 84, 960, 64, "b", claro)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_leve_ou_pesado", a), ("capa_B_pendulo_e_mola", b), ("capa_C_o_periodo_anda_com_a_raiz", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
