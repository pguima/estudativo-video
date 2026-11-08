"""Capas do MAT-EST-020 (1280x720). Uso: python capa.py"""
import subprocess, sys
from pathlib import Path
RAIZ = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(RAIZ / "_ferramentas"))
import skia
import editorial as E
import motor as M
BR = "#FFFFFF"
TINTA = E.TINTA
COR = E.MATERIAS["Matemática"]["cor"]
AMARELO = "#FFD500"
VERMELHO = "#FF5A5A"


def a(c):  # o gancho: +100% é de 1 para 2
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    x, y, w, h = 84, 220, 1300, 300
    c.drawRect(skia.Rect.MakeXYWH(x, y, w, h), M.paint(BR))
    c.drawRect(skia.Rect.MakeXYWH(x, y, w, 70), M.paint(TINTA))
    E.escreve(c, "MANCHETE", x + 36, y + 50, 40, "b", BR)
    E.escreve(c, "Casos sobem", x + 50, y + 170, 96, "g", TINTA)
    E.escreve(c, "100%!", x + 50 + E.larg("Casos sobem ", "g", 96), y + 170, 96, "g", VERMELHO)
    E.escreve(c, "na cidade", x + 50, y + 265, 80, "g", TINTA)
    E.escreve(c, "de 1 caso", 84, 720, 120, "i", BR)
    E.escreve(c, "para 2", 84, 890, 170, "g", AMARELO)
    for x in (1300, 1660, 1790):
        c.drawCircle(x, 820, 54, M.paint(VERMELHO))
    M.arrow(c, 1390, 820, 1570, 820, BR, 1, 9, 28)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Números", "que enganam", "amostra, base e causa")


def d(c):  # o atalho: 3 perguntas
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "3 perguntas", 84, 360, 150, "g", AMARELO)
    E.escreve(c, "antes de acreditar", 1000, 360, 90, "i", BR)
    for i, s in enumerate(("quem foi ouvido?", "por cento de quanto?", "o que mudou junto?")):
        y = 560 + i * 160
        E.bola(c, 150, y - 34, 52, COR)
        E.centro(c, str(i + 1), 150, y - 12, 64, "g", BR)
        E.escreve(c, s, 240, y, 100, "g", BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_de_1_para_2", a), ("capa_B_numeros_que_enganam", b), ("capa_C_tres_perguntas", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
