"""Capas do MAT-FAV-002 (1280x720). Uso: python capa.py"""
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


def ve(c, cx, cy, k, cor, lw=18, eixos=True):
    """V com a ponta em (cx, cy); k = px por unidade, braços até 3 unidades"""
    if eixos:
        M.arrow(c, cx - 3.6 * k, cy, cx + 3.8 * k, cy, BR, 0.6, 6, 24)
    M.line(c, cx - 3 * k, cy - 3 * k, cx, cy, cor, 1, lw)
    M.line(c, cx, cy, cx + 3 * k, cy - 3 * k, cor, 1, lw)
    c.drawCircle(cx, cy, lw * 1.4, M.paint(cor))


def a(c):  # o gancho: |−7| = 7 e o V
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "|−7| = 7", 84, 470, 230, "g", BR)
    E.escreve(c, "e o gráfico", 84, 700, 120, "i", BR)
    E.escreve(c, "vira um V", 84, 860, 150, "g", AMARELO)
    ve(c, 1500, 900, 110, AMARELO)


def b(c):  # o modelo
    E.capa_modelo(c, "Matemática", "Módulo", "e o V", "sem decorar")


def d(c):  # o atalho: o vértice onde o de dentro zera
    palco(c)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "vértice:", 84, 330, 120, "i", BR)
    E.escreve(c, "o de dentro", 80, 520, 150, "g", BR)
    E.escreve(c, "zera", 76, 740, 220, "g", BR)
    E.escreve(c, "|x − 2| + 1 → (2, 1)", 84, 940, 90, "g", AMARELO)
    ve(c, 1530, 640, 100, AMARELO, eixos=False)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_o_grafico_em_v", a), ("capa_B_modulo_e_o_v", b), ("capa_C_onde_o_de_dentro_zera", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
