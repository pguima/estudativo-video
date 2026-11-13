"""Capas da QUI-ATO-008 (1280x720). Uso: python capa.py"""
import subprocess, sys
from pathlib import Path
RAIZ = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(RAIZ / "_ferramentas"))
import skia
import editorial as E
import quimica as Q
import motor as M
BR = "#FFFFFF"
AMARELO = "#FFD500"
COR = E.MATERIAS["Química"]["cor"]
E.usar("Química")


def tabela_branca(c, x, y, cel, familia=None, periodo=None, cor=AMARELO):
    """tabela em branco sobre a cor da matéria (capa)"""
    for s, (z, per, g) in Q._posicoes().items():
        if g is None:
            continue
        cx, cy = x + (g - 1) * cel, y + (per - 1) * cel
        marcado = g == familia or per == periodo
        M.rrect(c, cx + 2, cy + 2, cel - 4, cel - 4, cel * 0.14, cor if marcado else "#FFFFFF", 1 if marcado else 0.85)


def a(c):  # o gancho: não decore a tabela
    E.capa_base(c, COR); E.capa_rotulo(c, "Química", COR)
    E.escreve(c, "não decore", 84, 360, 150, "g", BR)
    E.escreve(c, "a tabela", 84, 520, 150, "g", AMARELO)
    E.escreve(c, "leia a distribuição", 84, 660, 80, "i", BR)
    tabela_branca(c, 1000, 300, 48, familia=17, periodo=3)
    E.formula(c, "... 3s^2 3p^5", 84, 920, 110, "g", BR)


def b(c):
    E.capa_modelo(c, "Química", "Períodos", "e famílias", "do zero")


def d(c):  # o macete: período = maior camada; família = elétrons dela
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Química", COR)
    claro = E.mix(COR, BR, 0.5)
    E.formula(c, "3s^2 3p^5", 84, 440, 200, "g", BR)
    E.escreve(c, "período 3", 84, 640, 120, "g", claro)
    E.escreve(c, "2 + 5 = família 7A", 84, 800, 110, "g", AMARELO)
    tabela_branca(c, 1100, 520, 42, familia=17, periodo=3, cor=AMARELO)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_nao_decore_a_tabela", a), ("capa_B_periodos_e_familias", b), ("capa_C_periodo_e_familia_em_1_olhada", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
