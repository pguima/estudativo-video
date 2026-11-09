"""Capas do FIS-ELE-010 (1280x720). Uso: python capa.py"""
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
COBRE = "#C8743A"
E.usar("Física")


def fio_cobre(c, x, cy, L, d, cor=COBRE):
    rx = max(5, d * 0.22)
    escuro, claro = E.mix(cor, "#000000", 0.3), E.mix(cor, BR, 0.4)
    c.drawOval(skia.Rect.MakeXYWH(x - rx, cy - d / 2, 2 * rx, d), M.paint(escuro))
    p = skia.Paint(AntiAlias=True)
    p.setShader(skia.GradientShader.MakeLinear([skia.Point(0, cy - d / 2), skia.Point(0, cy + d / 2)],
                                               [M.hexc(claro), M.hexc(cor), M.hexc(escuro)], [0.0, 0.45, 1.0]))
    c.drawRect(skia.Rect.MakeXYWH(x, cy - d / 2, L, d), p)
    c.drawOval(skia.Rect.MakeXYWH(x + L - rx, cy - d / 2, 2 * rx, d), M.paint(E.mix(cor, BR, 0.55)))
    c.drawOval(skia.Rect.MakeXYWH(x + L - rx, cy - d / 2, 2 * rx, d), M.paint(escuro, 1.0, stroke=3))


def a(c):  # o gancho: esticou o fio, a resistência fica 4 vezes maior
    E.capa_base(c, COR); E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "esticou o fio", 84, 330, 120, "i", BR)
    E.escreve(c, "o dobro?", 84, 520, 190, "g", BR)
    fio_cobre(c, 110, 700, 560, 110)
    F.seta(c, 720, 700, 860, 700, BR, 1.0, 14)
    fio_cobre(c, 920, 700, 900, 55)
    E.bola(c, 1560, 380, 210, BR)
    E.formula(c, "R × 4", 1560, 425, 120, "g", COR, 1.0, "center")
    E.escreve(c, "não dobra: quadruplica", 84, 960, 90, "i", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Física", "Segunda lei", "de Ohm", "do zero")


def d(c):  # o macete do fio esticado
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "esticou n vezes?", 84, 340, 130, "i", BR)
    E.formula(c, "R × n^2", 84, 600, 260, "g", BR)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "o macete do fio", 84, 800, 100, "i", claro)
    fio_cobre(c, 1080, 900, 720, 70)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_fio_esticado", a), ("capa_B_segunda_lei_de_ohm", b), ("capa_C_macete_n_ao_quadrado", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
