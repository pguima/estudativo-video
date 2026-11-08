"""Capas do MAT-FUN-004 (1280x720). Uso: python capa.py"""
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


def diagrama(c, cxa, cxb, cy, A, B, flechas, img, cor_img, tinta=BR, size=70, dy=112, rw=110):
    rh = (max(len(A), len(B)) * dy + 60) / 2
    pa = {v: (cxa, cy + (i - (len(A) - 1) / 2) * dy) for i, v in enumerate(A)}
    pb = {v: (cxb, cy + (i - (len(B) - 1) / 2) * dy) for i, v in enumerate(B)}
    for v in img:
        c.drawCircle(*pb[v], 48, M.paint(cor_img, 0.9))
    for cx in (cxa, cxb):
        c.drawOval(skia.Rect.MakeXYWH(cx - rw, cy - rh, 2 * rw, 2 * rh), M.paint(tinta, 1, stroke=8))
    for d in (pa, pb):
        for v, (x, y) in d.items():
            E.centro(c, str(v), x, y + size * 0.36, size, "g", COR if (d is pb and v in img) else tinta)
    for e, s in flechas:
        (x0, y0), (x1, y1) = pa[e], pb[s]
        M.arrow(c, x0 + 46, y0, x1 - 56, y1, tinta, 1, 8, 28)


def a(c):  # o gancho: o 10 é imagem?
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "imagem", 84, 470, 200, "g", BR)
    E.escreve(c, "não é tudo", 84, 640, 130, "i", BR)
    E.escreve(c, "o 10 fica de fora", 84, 860, 90, "i", AMARELO)
    diagrama(c, 1330, 1680, 560, [1, 2, 3, 4], [2, 4, 6, 8, 10], [(1, 2), (2, 4), (3, 6), (4, 8)], [2, 4, 6, 8], AMARELO, size=60, dy=100, rw=100)
    E.arco(c, 1680, 760, 50, 0, 360, "#FF4D55", 8)


def b(c):  # o modelo
    E.capa_modelo(c, "Matemática", "Domínio", "e imagem", "do zero")


def d(c):  # o atalho
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "domínio:", 76, 420, 130, "g", claro)
    E.escreve(c, "de onde sai", 76, 560, 130, "i", BR)
    E.escreve(c, "imagem:", 76, 760, 130, "g", BR)
    E.escreve(c, "onde chega", 76, 900, 130, "i", BR)
    c.drawOval(skia.Rect.MakeXYWH(1330 - 110, 560 - 205, 220, 410), M.paint(claro, 0.55))
    diagrama(c, 1330, 1680, 560, [1, 2, 3], [2, 4, 6], [(1, 2), (2, 4), (3, 6)], [2, 4, 6], AMARELO, size=64)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_imagem_nao_e_tudo", a), ("capa_B_dominio_e_imagem", b), ("capa_C_sai_e_chega", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
