"""Capas do MAT-MTZ-004 (1280x720). Uso: python capa.py"""
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


def a(c):  # o erro: inverter cada número
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.formula(c, "A^{−1}", 84, 420, 170, "g", BR)
    E.matriz(c, 9, 0, [["f{1}{2}", 1], [1, 1]], 720, 380, 120, cor=BR, escuro=True, dy=190)
    E.risco(c, 560, 560, 900, 200, 9, 0, AMARELO, 30)
    E.matriz(c, 9, 0, [[1, -1], [-1, 2]], 1450, 560, 170, cor=AMARELO, escuro=True, cores={(i, j): AMARELO for i in range(2) for j in range(2)})
    E.escreve(c, "não é inverter", 84, 860, 130, "g", BR)
    E.escreve(c, "cada número", 84, 990, 100, "i", BR)


def b(c):  # o modelo
    E.capa_modelo(c, "Matemática", "Matriz", "inversa", "em 3 passos")


def d(c):  # o atalho: olhe o determinante
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "antes de tudo:", 84, 380, 130, "i", BR)
    E.escreve(c, "olhe o det", 76, 590, 210, "g", BR)
    E.escreve(c, "det = 0", 84, 840, 150, "g", AMARELO)
    E.escreve(c, "→ não existe", 720, 840, 120, "g", E.mix(COR, BR, 0.6))


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_nao_e_inverter_cada_numero", a), ("capa_B_matriz_inversa", b), ("capa_C_olhe_o_det", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
