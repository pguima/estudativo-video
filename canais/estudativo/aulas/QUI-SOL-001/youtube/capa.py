"""Capas da QUI-SOL-001 (1280x720). Uso: python capa.py"""
import importlib.util, subprocess, sys
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
_s = importlib.util.spec_from_file_location("v", Path(__file__).parents[1] / "roteiro" / "visual.py")
V = importlib.util.module_from_spec(_s); _s.loader.exec_module(V)
E.usar("Química")


def escuro(c):
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Química", COR)


def copo_laser(c, cx, yb, w, h, liq, tipo, brilho):
    V.frasco(c, 10, 0, cx, yb, w, h, liq, tipo)
    yy = yb - h * 0.42
    V.caneta_laser(c, cx - w / 2 - 50, yy, 1.0, comp=150)
    V.feixe(c, 10, 0, cx - w / 2 - 46, cx - w / 2, cx + w / 2 - 6, yy, brilho)


def a(c):  # o gancho: o leite parece solução, mas o laser entrega
    E.capa_base(c, COR); E.capa_rotulo(c, "Química", COR)
    E.escreve(c, "parece", 84, 400, 150, "i", BR)
    E.escreve(c, "solução?", 84, 580, 190, "g", BR)
    E.escreve(c, "a luz diz", 84, 800, 110, "i", BR)
    E.escreve(c, "que não", 84, 960, 150, "g", AMARELO)
    copo_laser(c, 1480, 900, 460, 560, V.LEITE, "col", 1.0)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Química", "Solução,", "coloide", "e suspensão")


def d(c):  # o macete: duas perguntas
    escuro(c)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "2 perguntas", 84, 330, 150, "g", BR)
    E.escreve(c, "e você acerta", 84, 480, 110, "i", BR)
    E.pilula(c, "1 · assenta?", 330, 660, 80, "g", fundo=COR)
    E.pilula(c, "2 · o feixe aparece?", 470, 860, 80, "g", fundo="#3A3B42")
    copo_laser(c, 1530, 900, 400, 480, V.TERRA, "sus", 1.0)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_parece_solucao", a), ("capa_B_solucao_coloide_suspensao", b), ("capa_C_duas_perguntas", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
