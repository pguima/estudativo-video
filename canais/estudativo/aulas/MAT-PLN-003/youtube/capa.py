"""Capas do MAT-PLN-003 (1280x720). Uso: python capa.py"""
import subprocess, sys
from pathlib import Path
RAIZ = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(RAIZ / "_ferramentas"))
import skia
import editorial as E
import motor as M
BR = "#FFFFFF"
AMARELO = "#FFD500"
COR = E.MATERIAS["Matemática"]["cor"]


def palco(c):
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)



def tabela(c, raiz, coefs, x, y, cw, size, cor_t, cor_r, cor_resto):
    res = [coefs[0]]
    for k in coefs[1:]:
        res.append(res[-1] * raiz + k)
    M.line(c, x - 10, y - size * 0.95, x - 10, y + size * 1.9, cor_t, 1, 8)
    M.line(c, x - 10, y + size * 0.45, x + cw * len(coefs), y + size * 0.45, cor_t, 1, 8)
    E.formula(c, E._num(raiz), x - 50, y, size, cor=cor_r, align="right")
    for i, (k, r) in enumerate(zip(coefs, res)):
        E.formula(c, E._num(k), x + cw * (i + 0.5), y, size, cor=cor_t, align="center")
        E.formula(c, E._num(r), x + cw * (i + 0.5), y + size * 1.55, size, cor=cor_resto if i == len(res) - 1 else cor_t, align="center")


def a(c):  # o gancho: dividir em 20 segundos
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "dividir em", 84, 330, 130, "i", BR)
    E.escreve(c, "20 segundos", 84, 480, 150, "g", AMARELO)
    tabela(c, 1, [1, -2, -5, 6], 260, 740, 280, 150, BR, AMARELO, AMARELO)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Briot-", "Ruffini", "dividir sem a chave")


def d(c):  # o atalho: a tabela calcula P(3)
    palco(c)
    E.escreve(c, "a tabela que calcula", 84, 330, 120, "i", BR)
    E.formula(c, "P(3)", 84, 540, 200, cor=AMARELO)
    tabela(c, 3, [1, -2, -5, 6], 260, 790, 280, 130, BR, "#C9C3FF", AMARELO)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_20_segundos", a), ("capa_B_briot_ruffini", b), ("capa_C_tabela_calcula", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
