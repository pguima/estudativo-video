"""Capas do MAT-FRA-003 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: 18/24 é só 3/4 disfarçado
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.fracao(c, 18, 24, 480, 520, 300, BR)
    E.escreve(c, "=", 830, 610, 250, "g", BR)
    E.fracao(c, 3, 4, 1370, 520, 340, AMARELO)
    E.escreve(c, "é a mesma fração!", 84, 1000, 130, "i", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Simplificar", "frações", "sem mistério")


def d(c):  # o atalho
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "o teste da", 84, 340, 150, "i", BR)
    E.escreve(c, "cruz", 600, 340, 190, "g", BR)
    claro = E.mix(COR, BR, 0.5)
    s, xa, xb, y = 220, 290, 900, 680
    M.line(c, xa + 90, y - 120, xb - 150, y + 120, claro, 1, 12); M.line(c, xa + 90, y + 120, xb - 120, y - 120, claro, 1, 12)
    E.fracao(c, 2, 3, xa, y, s, BR); E.fracao(c, 8, 12, xb, y, s, BR)
    E.escreve(c, "24", 1180, 620, 150, "g", AMARELO)
    E.escreve(c, "=", 1392, 620, 150, "g", BR)
    E.escreve(c, "24", 1510, 620, 150, "g", AMARELO)
    E.escreve(c, "equivalentes", 1180, 790, 100, "i", BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_disfarce", a), ("capa_B_simplificar", b), ("capa_C_teste_da_cruz", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
