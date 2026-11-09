"""Capas do FIS-ELE-026 (1280x720). Uso: python capa.py"""
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


def palco_capa(c):
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)


def a(c):  # o gancho: corrente negativa não é erro
    E.capa_base(c, COR); E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "deu", 84, 380, 130, "i", BR)
    E.escreve(c, "−2 A", 300, 400, 200, "g", BR)
    E.escreve(c, "errei?", 84, 600, 170, "g", BR)
    M.rrect(c, 70, 680, 1000, 200, 30, BR)
    E.escreve(c, "não: é o sentido", 110, 820, 100, "g", COR)
    claro = E.mix(COR, BR, 0.85)
    F.seta(c, 1560, 260, 1560, 820, claro, 1.0, 26)
    F.seta(c, 1760, 820, 1760, 260, BR, 0.35, 20)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Física", "Kirchhoff", "na prática", "4 questões")


def d(c):  # o macete: três jeitos de cair na prova
    palco_capa(c)
    E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "Kirchhoff cai de", 84, 360, 120, "i", BR)
    E.escreve(c, "três jeitos", 84, 560, 170, "g", BR)
    claro = E.mix(COR, BR, 0.35)
    for k, s in enumerate(("um nó", "uma malha", "duas malhas")):
        y = 690 + k * 130
        E.bola(c, 1240, y - 26, 50)
        E.centro(c, str(k + 1), 1240, y, 60, "g", BR)
        E.escreve(c, s, 1320, y, 80, "g", claro)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_corrente_negativa", a), ("capa_B_kirchhoff_na_pratica", b), ("capa_C_tres_jeitos", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
