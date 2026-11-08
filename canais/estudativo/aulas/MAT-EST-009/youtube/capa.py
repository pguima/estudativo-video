"""Capas do MAT-EST-009 (1280x720). Uso: python capa.py"""
import subprocess, sys
from pathlib import Path
RAIZ = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(RAIZ / "_ferramentas"))
import skia
import editorial as E
import motor as M
BR = "#FFFFFF"
COR = E.MATERIAS["Matemática"]["cor"]
AMARELO = "#FFD500"
VERMELHO = "#FF5A5A"


def cartao(c, cx, cy, w, h, s, peso, fundo, tinta):
    M.rrect(c, cx - w / 2, cy - h / 2, w, h, 24, fundo, 1)
    E.centro(c, s, cx, cy + h * 0.17, h * 0.5, "g", tinta)
    E.pilula(c, peso, cx, cy + h / 2 + 50, 44, "g", fundo=AMARELO, cor="#121214")


def a(c):  # o gancho: não é 7, é 7,2
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    cartao(c, 1100, 330, 220, 240, "6", "peso 2", BR, COR)
    cartao(c, 1400, 330, 220, 240, "8", "peso 3", BR, COR)
    E.escreve(c, "a média", 84, 360, 110, "i", BR)
    E.escreve(c, "não é 7", 84, 540, 140, "g", VERMELHO)
    E.escreve(c, "é 7,2", 84, 760, 200, "g", AMARELO)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Média", "ponderada", "notas com peso")


def d(c):  # o atalho: ande 3/5 do caminho
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "o atalho:", 84, 360, 110, "i", BR)
    E.escreve(c, "ande 3/5", 84, 560, 150, "g", BR)
    E.escreve(c, "do caminho", 84, 740, 130, "g", AMARELO)
    y, x0, x1 = 600, 1020, 1800
    M.line(c, x0, y, x1, y, BR, 1, 6)
    for i in range(6):
        x = x0 + (x1 - x0) * i / 5
        M.line(c, x, y - 22, x, y + 22, BR, 1, 5)
    M.line(c, x0, y, x0 + (x1 - x0) * 3 / 5, y, AMARELO, 1, 16)
    for x, s in ((x0, "6"), (x1, "8")):
        E.centro(c, s, x, y + 100, 72, "g", BR)
    xm = x0 + (x1 - x0) * 3 / 5
    E.pilula(c, "7,2", xm, y - 110, 64, "g", fundo=AMARELO, cor="#121214")


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_nao_e_7", a), ("capa_B_media_ponderada", b), ("capa_C_ande_tres_quintos", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
