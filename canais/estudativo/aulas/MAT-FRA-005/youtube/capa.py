"""Capas do MAT-FRA-005 (1280x720). Uso: python capa.py"""
import subprocess, sys
from pathlib import Path
RAIZ = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(RAIZ / "_ferramentas"))
import skia
import editorial as E
import motor as M
BR = "#FFFFFF"
COR = E.MATERIAS["Matemática"]["cor"]
CLARO = E.mix(COR, BR, 0.5)
AMARELO = "#FFD500"


def palco(c):
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)


def a(c):  # o gancho: o tamanho dos números engana
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.fracao(c, 2, 3, 420, 520, 340, AMARELO)
    E.escreve(c, "ou", 830, 620, 200, "i", BR)
    E.fracao(c, 3, 5, 1420, 520, 340, BR)
    E.escreve(c, "qual é maior?", 84, 1010, 170, "i", BR)


def b(c):  # o método
    E.capa_modelo(c, "Matemática", "Comparar", "e marcar", "frações na reta")


def d(c):  # o atalho: a cruz diz qual é a maior
    palco(c)
    E.escreve(c, "o teste da", 84, 340, 150, "i", BR)
    E.escreve(c, "cruz", 610, 340, 190, "g", BR)
    s, xa, xb, y = 220, 620, 1200, 660
    M.line(c, xa + 100, y - 120, xb - 100, y + 120, CLARO, 1, 12); M.line(c, xa + 100, y + 120, xb - 100, y - 120, CLARO, 1, 12)
    E.fracao(c, 2, 3, xa, y, s, BR); E.fracao(c, 3, 5, xb, y, s, BR)
    E.escreve(c, "10", 180, 730, 220, "g", AMARELO)
    E.escreve(c, "9", 1480, 730, 220, "g", AMARELO)
    E.escreve(c, "10 é maior que 9: 2/3 ganha", 84, 1000, 110, "i", BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_qual_e_maior", a), ("capa_B_comparar_fracoes", b), ("capa_C_teste_da_cruz", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
