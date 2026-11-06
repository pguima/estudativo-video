"""Capas do MAT-DIV-006 (1280x720). Uso: python capa.py"""
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


def fita(c, x, y, w, h, n, cor):
    """fita clara com os cortes do problema"""
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 16, 16), M.paint(cor))
    for i in range(1, n):
        M.line(c, x + w * i / n, y, x + w * i / n, y + h, COR, 1, 10, cap_round=False)


def a(c):  # o gancho: as duas fitas e a pergunta
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    fita(c, 84, 210, 744, 150, 3, BR)
    E.escreve(c, "72 cm", 864, 330, 120, "g", BR)
    fita(c, 84, 410, 1240, 150, 5, BR)
    E.escreve(c, "120 cm", 1360, 530, 120, "g", BR)
    E.escreve(c, "quantos pedaços?", 84, 800, 170, "g", AMARELO)
    E.escreve(c, "sem sobrar nada", 84, 960, 130, "i", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Problemas", "de MDC", "sem chute")


def d(c):  # o atalho: a pista no texto
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "a pista no texto", 84, 350, 150, "i", BR)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "partes iguais", 84, 520, 120, "g", claro)
    E.escreve(c, "sem sobra", 84, 660, 120, "g", claro)
    E.escreve(c, "o maior possível", 84, 800, 120, "g", claro)
    E.escreve(c, "= MDC", 1120, 660, 190, "g", AMARELO)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_quantos_pedacos", a), ("capa_B_problemas_de_mdc", b), ("capa_C_pista_no_texto", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
