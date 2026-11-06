"""Capas do MAT-FRA-019 (1280x720). Uso: python capa.py"""
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
    E.capa_rotulo(c, "Matemática", COR)


def a(c):  # o gancho: 3/8 não é 3,8
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.fracao(c, 3, 8, 330, 490, 280, BR)
    E.escreve(c, "=", 620, 590, 230, "g", BR)
    E.escreve(c, "3,8", 840, 610, 300, "g", AMARELO)
    M.line(c, 800, 640, 1340, 340, E.ERRADO, 1.0, 30)
    E.escreve(c, "?", 1400, 610, 300, "g", BR)
    E.escreve(c, "o erro de quase todo mundo", 84, 960, 124, "g", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Fração em", "decimal", "e o caminho de volta")


def d(c):  # o macete: faça o de baixo virar 100
    palco(c)
    E.escreve(c, "faça o de baixo", 84, 310, 150, "i", BR)
    E.escreve(c, "virar 100", 84, 520, 190, "g", AMARELO)
    E.fracao(c, 7, 20, 280, 760, 160, BR)
    E.escreve(c, "=", 470, 850, 160, "g", BR)
    E.fracao(c, 35, 100, 820, 760, 160, BR)
    E.escreve(c, "=", 1050, 850, 160, "g", BR)
    E.escreve(c, "0,35", 1210, 860, 220, "g", AMARELO)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_tres_oitavos_nao_e_tres_e_oito", a), ("capa_B_fracao_em_decimal", b), ("capa_C_virar_cem", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
