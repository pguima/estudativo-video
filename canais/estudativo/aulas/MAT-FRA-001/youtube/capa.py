"""Capas do MAT-FRA-001 (1280x720). Uso: python capa.py"""
import subprocess, sys
from pathlib import Path
RAIZ = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(RAIZ / "_ferramentas"))
import skia
import editorial as E
import motor as M
BR = "#FFFFFF"
COR = E.MATERIAS["Matemática"]["cor"]
CLARO = E.mix(COR, BR, 0.5)
AMARELO = "#FFD500"


def palco(c):
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)


def a(c):  # o gancho: frações que parecem código
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.fracao(c, 3, 4, 330, 520, 300, BR)
    E.fracao(c, 5, 12, 900, 520, 300, AMARELO)
    E.fracao(c, 12, 4, 1490, 520, 300, BR)
    E.escreve(c, "parece código?", 84, 1000, 150, "i", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "O que é", "fração?", "do zero")


def d(c):  # o atalho: a tabuada ao contrário
    palco(c)
    E.escreve(c, "a tabuada", 84, 350, 150, "i", BR)
    E.escreve(c, "ao contrário", 76, 570, 210, "g", BR)
    y = 790
    E.fracao(c, 24, 6, 300, y, 170, BR)
    E.escreve(c, "=", 480, y + 54, 150, "g", BR)
    E.bola(c, 770, y + 3, 150, CLARO)
    E.escreve(c, "4", 770 - E.larg("4", "g", 190) / 2, y + 68, 190, "g", BR)
    E.escreve(c, "6 × 4 = 24", 1000, y + 50, 130, "g", AMARELO)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_codigo", a), ("capa_B_o_que_e_fracao", b), ("capa_C_tabuada_ao_contrario", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
