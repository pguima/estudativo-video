"""Capas do FIS-OPT-007 (1280x720). Uso: python capa.py"""
import subprocess, sys
from pathlib import Path
RAIZ = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(RAIZ / "_ferramentas"))
import skia
import editorial as E
import fisica as F
import motor as M
BR = "#FFFFFF"
AMARELO = "#FFD500"
COR = E.MATERIAS["Física"]["cor"]
E.usar("Física")


def palco(c):
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)


def a(c):  # o gancho
    E.capa_base(c, COR); E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "+2 graus", 84, 420, 200, "g", AMARELO)
    E.escreve(c, "= foco de 50 cm", 84, 600, 130, "g", BR)
    E.escreve(c, "o grau dos óculos é uma conta", 84, 800, 80, "i", BR)
    M.rrect(c, 1330, 300, 480, 340, 24, BR)
    E.escreve(c, "receita", 1380, 380, 50, "i", "#6B6B76")
    E.escreve(c, "+2,00", 1380, 560, 130, "g", COR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Física", "Lentes", "e o grau", "equação e dioptria")


def d(c):  # o macete
    palco(c)
    E.capa_rotulo(c, "Física", COR)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "o atalho do grau:", 84, 330, 110, "i", BR)
    E.escreve(c, "f (cm) =", 84, 540, 160, "g", BR)
    E.escreve(c, "100 ÷ grau", 84, 730, 170, "g", claro)
    E.orbita(c, 1640, 300, 170, E.mix(COR, BR, 0.82))


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_mais_dois_graus", a), ("capa_B_equacao_das_lentes", b), ("capa_C_cem_dividido_pelo_grau", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
