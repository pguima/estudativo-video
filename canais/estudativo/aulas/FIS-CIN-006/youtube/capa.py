"""Capas do FIS-CIN-006 (1280x720). Uso: python capa.py"""
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


def a(c):  # o erro: esquecer o trem
    E.capa_base(c, COR); E.capa_rotulo(c, "Física", COR)
    claro = E.mix(COR, BR, 0.55)
    E.escreve(c, "o trem saiu", 84, 380, 150, "g", BR)
    E.escreve(c, "do túnel?", 84, 560, 150, "g", BR)
    E.escreve(c, "ainda não", 84, 760, 140, "g", AMARELO)
    E.escreve(c, "túnel + o próprio trem", 84, 900, 70, "i", claro)
    y = 900
    M.rrect(c, 1100, y - 300, 520, 300, 16, "#3A3A40", 0.9)
    for k in range(3):
        xa = 1350 + k * 150
        M.rrect(c, xa, y - 150, 140, 120, 18, BR, 1.0)
        for j in range(2):
            M.rrect(c, xa + 18 + j * 60, y - 132, 44, 40, 6, E.mix(COR, BR, 0.4), 1.0)
    M.line(c, 1000, y, 1900, y, BR, 1.0, 8)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Física", "Encontro", "de móveis", "e ultrapassagem")


def d(c):  # o macete: velocidade relativa
    palco(c)
    E.escreve(c, "de cabeça:", 84, 330, 120, "i", BR)
    E.escreve(c, "velocidade relativa", 76, 520, 140, "g", BR)
    claro = E.mix(COR, BR, 0.5)
    F.seta(c, 120, 700, 420, 700, claro, 1.0, 18); F.seta(c, 820, 700, 520, 700, claro, 1.0, 18)
    E.escreve(c, "some", 920, 730, 100, "g", BR)
    F.seta(c, 120, 900, 420, 900, claro, 1.0, 18); F.seta(c, 520, 900, 820, 900, claro, 1.0, 18)
    E.escreve(c, "subtraia", 920, 930, 100, "g", BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_o_trem_saiu", a), ("capa_B_encontro_de_moveis", b), ("capa_C_velocidade_relativa", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
