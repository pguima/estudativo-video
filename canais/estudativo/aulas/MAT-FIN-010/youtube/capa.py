"""Capas do MAT-FIN-010 (1280x720). Uso: python capa.py"""
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



def a(c):  # o gancho: rendeu 10% com inflação de 5%, não ficou 5% mais rico
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "rendeu 10%", 84, 390, 170, "g", BR)
    E.escreve(c, "inflação de 5%", 84, 540, 110, "i", BR)
    E.escreve(c, "ganho 5%?", 84, 800, 190, "g", E.mix(COR, BR, 0.55))
    E.risco(c, 70, 830, 960, 640, 9, 0, AMARELO, 30)
    E.centro(c, "4,8%", 1500, 820, 230, "g", AMARELO)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Taxa real", "de juros", "e a inflação")


def d(c):  # o atalho: a subtração só confere
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "o atalho para conferir", 84, 320, 110, "i", BR)
    E.escreve(c, "10% − 5% = 5%", 84, 540, 170, "g", BR)
    E.escreve(c, "real: um pouco", 84, 760, 130, "g", E.mix(COR, BR, 0.55))
    E.escreve(c, "abaixo de 5%", 84, 920, 150, "g", AMARELO)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_nao_e_5", a), ("capa_B_taxa_real", b), ("capa_C_subtracao_confere", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
