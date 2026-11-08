"""Capas do MAT-EXP-014 (1280x720). Uso: python capa.py"""
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
VERMELHO = "#FF4D55"


def a(c):  # o gancho: pH 3 contra pH 5 não é "2 vezes"
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "pH 3", 84, 420, 200, "g", BR)
    E.escreve(c, "e pH 5", 600, 420, 200, "g", BR)
    E.escreve(c, "2 vezes?", 84, 700, 160, "g", VERMELHO)
    E.risco(c, 70, 680, 84 + E.larg("2 vezes?", "g", 160) + 20, 600, 1, 0, AMARELO, 24)
    E.escreve(c, "100 vezes", 84, 960, 200, "g", AMARELO)
    E.escreve(c, "mais ácido", 1180, 940, 100, "i", BR)


def b(c):  # o modelo
    E.capa_modelo(c, "Matemática", "Escalas", "logarítmicas", "pH, Richter e dB")


def d(c):  # o atalho: a diferença vira expoente do 10
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "o atalho:", 84, 340, 120, "i", claro)
    E.escreve(c, "a diferença", 76, 560, 180, "g", BR)
    E.escreve(c, "vira expoente", 76, 760, 180, "g", AMARELO)
    E.formula(c, "+30 dB → 10^3 = 1.000 vezes", 84, 960, 90, "g", claro)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_100_vezes", a), ("capa_B_escalas_logaritmicas", b), ("capa_C_diferenca_vira_expoente", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
