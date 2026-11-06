"""Capas do MAT-FRA-010 (1280x720). Uso: python capa.py"""
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
CLARO = E.mix(COR, BR, 0.5)


def a(c):  # o gancho: a armadilha do "do que sobrou"
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "gastou", 84, 400, 160, "i", BR)
    E.escreve(c, "1/3", 520, 400, 180, "g", BR)
    E.escreve(c, "depois", 84, 640, 160, "i", BR)
    E.escreve(c, "1/4", 520, 640, 180, "g", AMARELO)
    E.escreve(c, "do que sobrou", 830, 630, 130, "g", AMARELO)
    E.escreve(c, "quanto restou?", 84, 960, 200, "g", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Fração", "do restante", "sem armadilha")


def d(c):  # o atalho: multiplique só as sobras
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "multiplique", 84, 380, 190, "g", BR)
    E.escreve(c, "só as sobras", 84, 570, 200, "i", BR)
    y, s = 800, 200
    E.fracao(c, 3, 4, 220, y, s, BR)
    E.escreve(c, "×", 345, y + 55, 150, "g", BR)
    E.fracao(c, 2, 3, 590, y, s, BR)
    E.escreve(c, "=", 730, y + 55, 150, "g", BR)
    E.fracao(c, 1, 2, 970, y, s, AMARELO)
    E.escreve(c, "em uma linha", 1100, y + 50, 130, "i", AMARELO)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_do_que_sobrou", a), ("capa_B_fracao_do_restante", b), ("capa_C_so_as_sobras", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
