"""Capas do MAT-FRA-014 (1280x720). Uso: python capa.py"""
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


def escuro(c):
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)


def a(c):  # o gancho: qual é maior?
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.numero(c, "0,8", 470, 590, 300, "g", AMARELO)
    E.escreve(c, "ou", 800, 560, 170, "i", BR)
    E.numero(c, "0,75", 1340, 590, 300, "g", BR)
    E.escreve(c, "qual é maior?", 84, 930, 190, "g", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Ler e", "comparar", "decimais")


def d(c):  # o macete: iguale as casas
    escuro(c)
    E.escreve(c, "iguale as", 84, 350, 150, "i", BR)
    E.escreve(c, "casas", 76, 570, 240, "g", BR)
    E.numero(c, "0,80", 1330, 400, 240, "g", BR, 1.0, {3: AMARELO})
    E.numero(c, "0,75", 1330, 640, 240, "g", BR)
    E.escreve(c, "80 é mais que 75", 84, 900, 170, "g", AMARELO)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_qual_e_maior", a), ("capa_B_ler_comparar", b), ("capa_C_iguale_as_casas", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
