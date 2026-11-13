"""Capas da QUI-MIS-001 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: H₂O tem 2 átomos? São 3
    E.capa_base(c, COR); E.capa_rotulo(c, "Química", COR)
    Q.formula(c, "H2O", 84, 500, 340, BR)
    E.escreve(c, "2 átomos?", 84, 800, 150, "g", BR)
    E.risco(c, 70, 830, 790, 690, 9, 0, AMARELO, 30)
    E.escreve(c, "são 3", 860, 800, 150, "g", AMARELO)
    Q.molecula_desenho(c, "H2O", 1520, 470, 230)
    E.escreve(c, "o átomo que não aparece", 84, 990, 92, "i", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Química", "Átomos", "e fórmulas", "do zero")


def d(c):  # o macete: some os índices
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Química", COR)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "conte os átomos", 84, 340, 130, "i", BR)
    E.escreve(c, "em 3 segundos", 76, 540, 170, "g", BR)
    Q.formula(c, "C2H6O", 84, 790, 230, BR, cores={"indice": claro}, escuro=True)
    E.formula(c, "2 + 6 + 1 = 9", 84, 1010, 100, "g", claro)
    Q.molecula_desenho(c, "C2H6O", 1450, 760, 150, escuro=True)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_tres_atomos", a), ("capa_B_atomos_e_formulas", b), ("capa_C_some_os_indices", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
