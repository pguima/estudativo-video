"""Capas do MAT-FAV-004 (1280x720). Uso: python capa.py"""
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


def palco(c):
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)


def maquinas(c, x, y, ordem, cor_txt):
    """duas máquinas em fila, só com as letras"""
    for i, n in enumerate(ordem):
        cx = x + i * 300
        M.rrect(c, cx - 110, y - 90, 220, 180, 30, BR if n == "f" else "#07070F", 1)
        E.centro(c, n, cx, y + 45, 130, "g", COR if n == "f" else BR)
    M.arrow(c, x + 115, y, x + 185, y, cor_txt, 1, 8, 24)


def a(c):  # o gancho: a ordem muda tudo
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "f(g(3)) = 19", 84, 400, 160, "g", BR)
    E.escreve(c, "g(f(3)) = 49", 84, 600, 160, "g", AMARELO)
    E.escreve(c, "a ordem muda tudo", 84, 820, 110, "i", BR)
    maquinas(c, 1360, 380, "gf", BR)
    maquinas(c, 1360, 640, "fg", AMARELO)


def b(c):  # o modelo
    E.capa_modelo(c, "Matemática", "Função", "composta", "sem medo")


def d(c):  # o atalho: o de dentro vale 5
    palco(c)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "f(5)?", 84, 400, 200, "g", BR)
    E.escreve(c, "faça o de dentro", 84, 600, 120, "i", BR)
    E.escreve(c, "valer 5", 84, 790, 170, "g", AMARELO)
    E.escreve(c, "f(2x + 1) = 4x + 3", 1000, 470, 80, "g", BR)
    E.escreve(c, "2x + 1 = 5 → x = 2", 1000, 620, 80, "g", AMARELO)
    E.escreve(c, "f(5) = 11", 1000, 790, 110, "g", BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_a_ordem_muda_tudo", a), ("capa_B_funcao_composta", b), ("capa_C_o_de_dentro_vale_5", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
