"""Capas do MAT-FRA-020 (1280x720). Uso: python capa.py"""
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
    E.capa_rotulo(c, "Matemática", COR)


def a(c):  # o gancho: a conta que não acaba
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "0,454545...", 84, 510, 270, "g", BR)
    E.escreve(c, "acaba", 84, 750, 210, "i", BR)
    E.escreve(c, "ou não?", 640, 750, 210, "g", AMARELO)
    E.escreve(c, "saiba antes de dividir", 84, 960, 130, "i", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Dízimas:", "prever", "sem dividir")


def d(c):  # o macete: só 2 e 5
    palco(c)
    E.escreve(c, "só", 84, 460, 220, "i", BR)
    E.escreve(c, "2 e 5", 330, 470, 280, "g", AMARELO)
    E.escreve(c, "embaixo?", 1000, 460, 190, "i", BR)
    E.escreve(c, "decimal exato", 84, 700, 200, "g", BR)
    E.escreve(c, "outro primo: dízima", 84, 920, 160, "i", BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_acaba_ou_nao", a), ("capa_B_dizimas_prever", b), ("capa_C_so_dois_e_cinco", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
