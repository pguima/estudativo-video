"""Capas do MAT-RAZ-008 (1280x720). Uso: python capa.py"""
import subprocess, sys
from pathlib import Path
RAIZ = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(RAIZ / "_ferramentas"))
import skia
import editorial as E
import motor as M
BR = "#FFFFFF"
COR = E.MATERIAS["Matemática"]["cor"]


def tabela(c, xs, y, nomes, linhas, size, cor_n, cor_v):
    for x, nome, (v1, v2) in zip(xs, nomes, linhas):
        E.centro(c, nome, x, y, 64, "i", cor_n)
        M.line(c, x - 150, y + 30, x + 150, y + 30, cor_n, 0.6, 4)
        E.centro(c, v1, x, y + 190, size, "g", cor_v)
        E.centro(c, v2, x, y + 360, size, "g", cor_v)


def a(c):  # o erro: 200 peças, faltou uma grandeza
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    tabela(c, (300, 640, 980), 320, ("máquinas", "horas", "peças"), (("3", "5"), ("4", "6"), ("120", "200")), 160, BR, BR)
    E.risco(c, 850, 690, 1110, 585, 9, 0, "#FFD500", 26)
    E.escreve(c, "faltou", 1230, 520, 130, "i", BR)
    E.escreve(c, "uma", 1230, 680, 160, "g", BR)
    E.escreve(c, "coluna", 1230, 840, 160, "g", BR)


def b(c):  # o modelo
    E.capa_modelo(c, "Matemática", "Regra", "de três", "composta")


def d(c):  # o atalho: 1 máquina em 1 hora
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "o atalho:", 84, 340, 130, "i", BR)
    E.escreve(c, "1 máquina", 76, 540, 190, "g", BR)
    E.escreve(c, "em 1 hora", 76, 730, 190, "g", BR)
    cl = E.mix(COR, BR, 0.55)
    for r in range(3):
        for k in range(4):
            x, y = 1300 + k * 120, 760 + r * 100
            M.rrect(c, x, y, 100, 84, 14, cl)
            E.centro(c, "10", x + 50, y + 58, 48, "g", "#07070F")


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_faltou_uma_coluna", a), ("capa_B_regra_de_tres_composta", b), ("capa_C_uma_maquina_uma_hora", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
