"""Capas do MAT-EST-008 (1280x720). Uso: python capa.py"""
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


def cartao(c, cx, cy, w, h, s, fundo, tinta, borda=None):
    M.rrect(c, cx - w / 2, cy - h / 2, w, h, 24, fundo, 1)
    if borda:
        rr = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2, cy - h / 2, w, h), 24, 24)
        c.drawRRect(rr, M.paint(borda, 1, stroke=10))
    E.centro(c, s, cx, cy + h * 0.17, h * 0.5, "g", tinta)


def a(c):  # o gancho: 6, 8, 5 e o 8 que não resolve
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    for i, s in enumerate(("6", "8", "5")):
        cartao(c, 1010 + 210 * i, 330, 170, 200, s, BR, COR)
    cartao(c, 1220, 600, 220, 240, "9", AMARELO, "#121214")
    E.escreve(c, "média 7:", 84, 360, 110, "i", BR)
    E.escreve(c, "um 8 não", 84, 540, 140, "g", BR)
    E.escreve(c, "resolve", 84, 700, 140, "g", AMARELO)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Média", "aritmética", "e a nota que falta")


def d(c):  # o atalho: sobras e faltas
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "o atalho:", 84, 360, 110, "i", BR)
    E.escreve(c, "−1 +1 −2", 84, 560, 150, "g", BR)
    E.escreve(c, "falta 2", 84, 760, 170, "g", AMARELO)
    base, x0, bw = 860, 1060, 150
    y7 = base - 7 * 70
    for i, v in enumerate((6, 8, 5)):
        x = x0 + i * 230
        M.rrect(c, x, base - v * 70, bw, v * 70, 12, E.mix(COR, BR, 0.3), 1)
    for k in range(0, 760, 40):
        M.line(c, x0 - 30 + k, y7, x0 - 30 + k + 22, y7, AMARELO, 1, 8)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_um_8_nao_resolve", a), ("capa_B_media_aritmetica", b), ("capa_C_sobras_e_faltas", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
