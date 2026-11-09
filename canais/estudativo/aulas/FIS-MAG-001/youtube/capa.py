"""Capas do FIS-MAG-001 (1280x720). Uso: python capa.py"""
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


def barra(c, cx, cy, w, h, ang=0, contorno=True):
    """ímã em barra com o norte no sentido ang, letras em pé"""
    c.save(); c.translate(cx, cy); c.rotate(-ang)
    for lado, cor in ((1, COR), (-1, F.NEG)):
        x0 = 0 if lado > 0 else -w / 2
        r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x0, -h / 2, w / 2, h), 14, 14)
        c.drawRRect(r, M.paint(cor))
        if contorno:
            c.drawRRect(r, M.paint(BR, 1, stroke=6))
    c.restore()
    ux, uy = math.cos(math.radians(ang)), -math.sin(math.radians(ang))
    E._meio(c, "N", cx + ux * w / 4, cy + uy * w / 4, h * 0.6, "g", BR)
    E._meio(c, "S", cx - ux * w / 4, cy - uy * w / 4, h * 0.6, "g", BR)


def palco_capa(c):
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Física", COR)


def a(c):  # o gancho: o ímã partido vira dois ímãs
    E.capa_base(c, COR); E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "partiu o ímã?", 84, 360, 150, "i", BR)
    E.escreve(c, "2 ímãs", 84, 590, 220, "g", BR)
    E.escreve(c, "inteiros", 84, 790, 170, "g", AMARELO)
    barra(c, 1370, 380, 640, 150)
    M.line(c, 1370, 270, 1370, 490, AMARELO, 1, 10, dash=[26, 18])
    F.seta(c, 1370, 520, 1370, 600, BR, 1, 12)
    barra(c, 1190, 720, 300, 150)
    barra(c, 1550, 720, 300, 150)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Física", "Ímãs e", "campo", "magnético")


def d(c):  # o macete: a linha sai do norte e entra no sul
    palco_capa(c)
    E.escreve(c, "a linha", 84, 330, 130, "i", BR)
    E.escreve(c, "sai do N", 76, 520, 190, "g", BR)
    E.escreve(c, "entra no S", 84, 690, 130, "i", E.mix(COR, BR, 0.5))
    cx, cy, w = 1450, 600, 440
    F.linhas_campo(c, 99, 0, cx, cy, w, 3, E.mix(COR, BR, 0.5), h=120, largura=6)
    barra(c, cx, cy, w, 120, contorno=False)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_ima_partido", a), ("capa_B_imas_e_campo_magnetico", b), ("capa_C_a_linha_sai_do_norte", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
