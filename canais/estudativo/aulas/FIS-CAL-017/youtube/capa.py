"""Capas do FIS-CAL-017 (1280x720). Uso: python capa.py"""
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
    E.capa_rotulo(c, "Física", COR)




def geladeira(c, x, y, w, h, cor_corpo, linha, interior):
    M.rrect(c, x, y, w, h, 30, cor_corpo, 1.0)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 30, 30), M.paint(linha, 1.0, stroke=10))
    M.rrect(c, x + 24, y + 24, w - 48, h - 48, 18, interior, 1.0)
    p = skia.Path()
    p.moveTo(x + w, y + 14); p.lineTo(x + w + w * 0.5, y + 50); p.lineTo(x + w + w * 0.5, y + h - 50); p.lineTo(x + w, y + h - 14); p.close()
    c.drawPath(p, M.paint(cor_corpo, 1.0))
    c.drawPath(p, M.paint(linha, 1.0, stroke=8))


def a(c):  # o gancho: porta aberta esquenta a cozinha
    E.capa_base(c, COR); E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "porta aberta", 84, 400, 160, "g", BR)
    E.escreve(c, "esquenta", 84, 580, 160, "g", AMARELO)
    E.escreve(c, "a cozinha", 84, 760, 160, "g", BR)
    geladeira(c, 1320, 260, 300, 520, BR, BR, "#A9D8F5")


def b(c):  # o modelo padrão
    E.capa_base(c, COR); E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "Geladeira", 76, 430, 200, "g", BR)
    E.escreve(c, "e entropia", 76, 620, 170, "g", BR)
    E.escreve(c, "a máquina ao contrário", 84, 840, 110, "i", BR)
    E.simbolo(c, 1640, 820, 190, cor=E.mix(COR, BR, 0.82), forma="orbita")


def d(c):  # o macete: as três setas
    palco_capa(c)
    E.escreve(c, "três setas", 84, 360, 160, "g", BR)
    E.escreve(c, "o lado quente é a soma", 84, 500, 100, "i", BR)
    claro = E.mix(COR, BR, 0.5)
    E.formula(c, "800 = 600 + 200", 84, 800, 150, "g", claro)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_porta_aberta", a), ("capa_B_geladeira_e_entropia", b), ("capa_C_tres_setas", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
