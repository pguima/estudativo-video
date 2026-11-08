"""Capas do MAT-LEI-003 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: gastou 2/5 e sobrou R$ 600; o desenho resolve
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "gastou", 84, 380, 130, "i", BR)
    E.fracao(c, 2, 5, 560, 330, 130, AMARELO)
    E.escreve(c, "sobrou R$ 600", 680, 380, 130, "g", BR)
    x, y, w, h = 84, 500, 1500, 190
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 18, 18), M.paint(BR))
    c.drawRect(skia.Rect.MakeXYWH(x + 6, y + 6, w * 2 / 5 - 6, h - 12), M.paint(E.mix(COR, BR, 0.35)))
    for k in range(1, 5):
        M.line(c, x + w * k / 5, y, x + w * k / 5, y + h, COR, 1, 8)
    for k in range(2, 5):
        E.centro(c, "200", x + w * (k + 0.5) / 5, y + h / 2 + 40, 110, "g", COR)
    E.escreve(c, "salário?", 84, 920, 150, "i", BR)
    E.escreve(c, "R$ 1.000", 760, 930, 170, "g", AMARELO)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Desenhe", "o problema", "barras e tabelas")


def d(c):  # o atalho da tabela: pule linhas
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "o atalho da", 84, 350, 130, "i", BR)
    E.escreve(c, "tabela", 76, 580, 230, "g", BR)
    x0, y0 = 1060, 250
    M.rrect(c, x0, y0, 760, 120, 20, COR)
    for k, s in enumerate(("carros", "motos", "rodas")):
        E.centro(c, s, x0 + 127 + k * 253, y0 + 82, 60, "b", BR)
    for r, (vals, cor) in enumerate(((("0", "10", "20"), BR), (("1", "9", "22"), BR), (("6", "4", "32"), AMARELO))):
        yy = y0 + 230 + r * 150 + (60 if r == 2 else 0)
        for k, s in enumerate(vals):
            E.centro(c, s, x0 + 127 + k * 253, yy, 100, "g", cor)
    E.escreve(c, "pule!", 84, 860, 150, "g", AMARELO)
    M.arrow(c, 1000, 470, 1000, 820, AMARELO, 1, 10, 34)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_sobrou_600", a), ("capa_B_desenhe_o_problema", b), ("capa_C_pule_linhas", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
