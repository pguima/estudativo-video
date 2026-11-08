"""Capas do MAT-EST-003 (1280x720). Uso: python capa.py"""
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
VENDAS = [40, 50, 80, 100, 90]


def linha(c, x, y, w, h, vals, vmax, destaque=1, cor=BR, lw=10):
    """a linha das vendas em branco, com o trecho da maior alta em amarelo; devolve os pontos"""
    pts = [(x + w * (i + 0.5) / len(vals), y + h - v / vmax * h) for i, v in enumerate(vals)]
    M.line(c, x, y + h, x + w, y + h, cor, 0.6, 5)
    for i in range(len(pts) - 1):
        M.line(c, *pts[i], *pts[i + 1], AMARELO if i == destaque else cor, 1, lw * (1.8 if i == destaque else 1))
    for P in pts:
        c.drawCircle(P[0], P[1], lw * 1.3, M.paint(cor))
    return pts


def a(c):  # o gancho: o ponto mais alto não é a maior alta
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    pts = linha(c, 900, 260, 900, 620, VENDAS, 120)
    c.drawCircle(*pts[3], 46, M.paint(VERMELHO, 1, stroke=10))
    E.escreve(c, "maior alta?", 84, 360, 120, "i", BR)
    E.escreve(c, "não é o", 84, 560, 140, "g", BR)
    E.escreve(c, "topo", 84, 750, 190, "g", AMARELO)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Gráficos de", "barras e linhas", "e a maior alta")


def d(c):  # o atalho: o trecho mais em pé
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "maior alta =", 84, 360, 110, "i", BR)
    E.escreve(c, "trecho mais", 84, 560, 140, "g", BR)
    E.escreve(c, "em pé", 84, 740, 170, "g", AMARELO)
    linha(c, 1000, 300, 820, 600, VENDAS, 120)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_nao_e_o_topo", a), ("capa_B_graficos_barras_linhas", b), ("capa_C_trecho_mais_em_pe", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
