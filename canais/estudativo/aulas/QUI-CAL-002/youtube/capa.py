"""Capas da QUI-CAL-002 (1280x720). Uso: python capa.py"""
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


def palco(c):
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Química", COR)
def a(c):  # o gancho: 36 g de água = 1,2 × 10²⁴ moléculas
    E.capa_base(c, COR); E.capa_rotulo(c, "Química", COR)
    E.escreve(c, "36 g de água", 84, 400, 150, "g", BR)
    E.escreve(c, "=", 84, 600, 150, "g", BR)
    E.formula(c, "1,2 × 10^{24}", 220, 600, 170, "g", AMARELO)
    E.escreve(c, "moléculas", 84, 790, 150, "g", BR)
    E.escreve(c, "como contar sem contar", 84, 990, 92, "i", BR)
    Q.molecula_desenho(c, "H2O", 1560, 560, 230)


def b(c):
    E.capa_modelo(c, "Química", "O mol", "e Avogadro", "do zero")


def d(c):  # o macete: quantas vezes cabe
    palco(c)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "de gramas para mol", 84, 340, 120, "i", BR)
    E.escreve(c, "sem regra de três", 76, 530, 150, "g", BR)
    for k in range(2):
        M.rrect(c, 84 + k * 520, 640, 500, 180, 24, COR, 1.0)
        E.escreve(c, "18 g", 84 + k * 520 + 150, 765, 110, "g", BR)
    E.escreve(c, "= 2 mol", 1160, 765, 130, "g", claro)
    E.escreve(c, "36 g de água: quantas vezes cabe?", 84, 990, 70, "i", BR)


CAPAS = (("capa_A_36g_de_agua", a), ("capa_B_mol_avogadro", b), ("capa_C_quantas_vezes_cabe", d))


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in CAPAS:
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
