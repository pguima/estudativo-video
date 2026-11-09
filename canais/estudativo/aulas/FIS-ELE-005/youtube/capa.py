"""Capas do FIS-ELE-005 (1280x720). Uso: python capa.py"""
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


def raio(c, pts, cor=AMARELO):
    for cr, lw in (("#121214", 30), (cor, 20)):
        p = M.paint(cr, 1.0, stroke=lw)
        p.setStrokeJoin(skia.Paint.kRound_Join)
        path = skia.Path(); path.moveTo(*pts[0])
        for P in pts[1:]:
            path.lineTo(*P)
        c.drawPath(path, p)


def a(c):  # o erro: os pneus protegem?
    E.capa_base(c, COR); E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "são os pneus?", 84, 400, 160, "g", BR)
    E.risco(c, 70, 420, 1060, 300, 9, 0, AMARELO, 30)
    E.escreve(c, "não: a lataria", 84, 640, 150, "i", BR)
    F.carrinho(c, 1420, 960, 640, cor=E.mix(COR, BR, 0.8))
    raio(c, [(1380, 0), (1300, 140), (1420, 240), (1340, 380), (1420, 520)])


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Física", "Gaiola de", "Faraday", "e poder das pontas")


def d(c):  # o macete: 3 respostas do condutor
    palco(c)
    E.escreve(c, "condutor em equilíbrio", 84, 330, 100, "i", BR)
    claro = E.mix(COR, BR, 0.5)
    for i, (l, r) in enumerate((("carga:", "superfície de fora"), ("campo dentro:", "zero"), ("potencial:", "igual"))):
        y = 520 + i * 170
        E.escreve(c, l, 90, y, 110, "g", BR)
        E.escreve(c, r, 90 + E.larg(l, "g", 110) + 40, y, 110, "i", claro)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_sao_os_pneus", a), ("capa_B_gaiola_de_faraday", b), ("capa_C_condutor_em_equilibrio", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
