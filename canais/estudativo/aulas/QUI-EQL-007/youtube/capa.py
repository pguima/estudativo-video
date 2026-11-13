"""Capas da QUI-EQL-007 (1280x720). Uso: python capa.py"""
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


NOMES = ("capa_A_quase_nada_se_dissolve", "capa_B_kps", "capa_C_s2_ou_4s3")


def a(c):  # o gancho: o bário do raio X
    E.capa_base(c, COR); E.capa_rotulo(c, "Química", COR)
    Q.formula(c, "BaSO4", 84, 400, 170, BR)
    E.escreve(c, "quase nada", 84, 620, 190, "g", AMARELO)
    E.escreve(c, "se dissolve", 84, 820, 170, "g", BR)
    E.escreve(c, "o Kps explica o raio X", 84, 990, 84, "i", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Química", "Produto de", "solubilidade", "o Kps")


def d(c):  # o macete: dois formatos
    escuro(c)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "decore 2 formatos", 84, 320, 120, "i", BR)
    E.formula(c, "AB: Kps = s^2", 84, 580, 160, "g", BR)
    E.formula(c, "AB₂: Kps = 4s^3", 84, 820, 160, "g", claro)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in zip(NOMES, (a, b, d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
