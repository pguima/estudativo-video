"""Capas da QUI-TER-004 (1280x720). Uso: python capa.py"""
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


def escuro(c):
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Química", COR)


NOMES = ("capa_A_rapido_no_comeco", "capa_B_velocidade_media", "capa_C_achou_uma_achou_todas")


def a(c):  # o gancho: rápido no começo, devagar depois
    E.capa_base(c, COR); E.capa_rotulo(c, "Química", COR)
    E.escreve(c, "rápida no começo", 84, 360, 120, "i", BR)
    E.escreve(c, "e depois?", 84, 560, 190, "g", BR)
    E.formula(c, "v = f{Δ[ ]}{Δt}", 84, 820, 150, "g", AMARELO)
    pts = [(1150, 300), (1300, 520), (1450, 650), (1600, 720), (1780, 750)]
    for k in range(len(pts) - 1):
        M.line(c, *pts[k], *pts[k + 1], BR, 1, 14)
    M.line(c, 1150, 300, 1150, 800, BR, 0.6, 6); M.line(c, 1150, 800, 1800, 800, BR, 0.6, 6)
    E.escreve(c, "mol/L por minuto", 84, 990, 80, "i", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Química", "Velocidade", "média", "do zero")


def d(c):  # o macete: os coeficientes ligam as velocidades
    escuro(c)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "achou uma,", 84, 360, 140, "g", BR)
    E.escreve(c, "achou todas", 84, 540, 140, "g", claro)
    Q.formula(c, "2 H2O2 -> 2 H2O + O2", 84, 760, 110, BR, cores={"coef": claro}, escuro=True)
    E.formula(c, "0,030 → 0,030 → 0,015", 84, 940, 90, "g", BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in zip(NOMES, (a, b, d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
