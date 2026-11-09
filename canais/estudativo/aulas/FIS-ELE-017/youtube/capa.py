"""Capas do FIS-ELE-017 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: só com a etiqueta do chuveiro, a corrente
    E.capa_base(c, COR); E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "só com a etiqueta:", 84, 330, 110, "i", BR)
    E.escreve(c, "quantos", 84, 510, 170, "g", BR)
    E.escreve(c, "ampères?", 84, 680, 170, "g", BR)
    x, y, w, h = 1150, 300, 640, 470
    M.rrect(c, x, y, w, h, 30, BR)
    M.rrect(c, x, y, w, 100, 30, "#14141C"); M.rrect(c, x, y + 60, w, 40, 0, "#14141C")
    E.escreve(c, "CHUVEIRO", x + 40, y + 72, 52, "b", BR)
    F.medida(c, "220", "V", x + 50, y + 250, 120, "#14141C")
    F.medida(c, "4.400", "W", x + 50, y + 410, 120, "#14141C")
    E.bola(c, x + w - 20, y + h + 60, 120, AMARELO)
    E.centro(c, "20 A", x + w - 20, y + h + 90, 76, "g", "#14141C")


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Física", "Potência", "elétrica", "e efeito Joule")


def d(c):  # o macete: metade da tensão, um quarto da potência
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "metade da tensão,", 84, 330, 120, "i", BR)
    E.escreve(c, "1/4 da potência", 84, 520, 150, "g", BR)
    claro = E.mix(COR, BR, 0.5)
    E.formula(c, "100 W → 25 W", 84, 730, 130, "g", claro)
    E.formula(c, "P = f{U^2}{R}", 84, 920, 100, "g", BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_quantos_amperes", a), ("capa_B_potencia_eletrica", b), ("capa_C_metade_da_tensao", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
