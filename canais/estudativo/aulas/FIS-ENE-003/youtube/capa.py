"""Capas do FIS-ENE-003 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: o dobro da velocidade, quatro vezes a energia
    E.capa_base(c, COR); E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "2× a velocidade", 84, 380, 130, "i", BR)
    E.escreve(c, "4× a", 84, 600, 210, "g", BR)
    E.escreve(c, "energia", 84, 820, 210, "g", AMARELO)
    claro = E.mix(COR, BR, 0.85)
    for i, (h, s) in enumerate(((150, "40"), (600, "80"))):
        x = 1250 + i * 300
        M.rrect(c, x, 900 - h, 200, h, 16, claro)
        E.centro(c, s + " km/h", x + 100, 960, 56, "g", BR)
    M.line(c, 1200, 900, 1800, 900, BR, 1, 6)


def b(c):  # o modelo padrão
    E.capa_base(c, COR); E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "Energia", 76, 450, 210, "g", BR)
    E.escreve(c, "cinética", 76, 660, 210, "g", BR)
    E.escreve(c, "do zero", 84, 860, 170, "i", BR)
    E.simbolo(c, 1590, 760, 260, cor=E.mix(COR, BR, 0.82), forma="orbita")


def d(c):  # o macete: a frenagem vai com o quadrado
    palco(c)
    E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "o atalho da freada", 84, 340, 110, "i", BR)
    E.escreve(c, "v × 2 → d × 4", 76, 560, 170, "g", BR)
    claro = E.mix(COR, BR, 0.5)
    for i, (v, d) in enumerate(((20, 40), (40, 160))):
        y = 760 + i * 170
        E.escreve(c, f"{v} m/s", 84, y + 20, 64, "g", BR)
        F.seta(c, 420, y, 420 + d * 7, y, claro, 1.0, 20)
        E.escreve(c, f"{d} m", 440 + d * 7, y + 22, 64, "g", claro)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_dobro_da_velocidade_4x_energia", a), ("capa_B_energia_cinetica", b), ("capa_C_frenagem_vai_com_o_quadrado", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
