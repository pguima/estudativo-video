"""Capas do FIS-CAL-008 (1280x720). Uso: python capa.py"""
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
CLARO = E.mix(COR, BR, 0.82)
E.usar("Física")


def palco_capa(c):
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Física", COR)


def a(c):  # o gancho: 5 situações
    E.capa_base(c, COR); E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "5", 84, 560, 420, "g", AMARELO)
    E.escreve(c, "situações", 420, 470, 130, "i", BR)
    E.escreve(c, "de calor", 420, 600, 130, "g", BR)
    E.escreve(c, "escalas · dilatação · gelo", 84, 860, 80, "i", BR)
    E.escreve(c, "você resolve antes", 84, 980, 80, "g", BR)
    E.simbolo(c, 1600, 560, 230, cor=CLARO, forma="orbita")


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Física", "Praticando", "calor", "5 situações")


def d(c):  # o macete: compare antes da conta
    palco_capa(c)
    E.escreve(c, "com gelo,", 84, 340, 130, "i", BR)
    E.escreve(c, "compare antes", 84, 540, 170, "g", BR)
    claro = E.mix(COR, BR, 0.5)
    M.rrect(c, 300, 620, 200, 380, 20, COR)
    M.rrect(c, 600, 760, 200, 240, 20, "#1F6FEB")
    E.escreve(c, "disponível", 250, 1045, 46, "i", claro)
    E.escreve(c, "necessário", 580, 1045, 46, "i", claro)
    E.escreve(c, "sobra: derrete tudo", 980, 820, 70, "g", BR)
    E.escreve(c, "falta: para em 0 °C", 980, 940, 70, "g", claro)


CAPAS = (("capa_A_cinco_situacoes", a), ("capa_B_praticando_calorimetria", b), ("capa_C_compare_antes", d))


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in CAPAS:
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
