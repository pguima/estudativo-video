"""Capas do FIS-OPT-001 (1280x720). Uso: python capa.py"""
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
    E.escreve(c, "a árvore", 84, 400, 150, "g", BR)
    E.escreve(c, "de cabeça", 84, 570, 150, "g", BR)
    E.escreve(c, "para baixo", 84, 740, 150, "g", AMARELO)
    E.escreve(c, "numa caixa com um furo", 84, 900, 80, "i", BR)
    M.line(c, 1250, 330, 1250, 520, BR, 1.0, 12); M.line(c, 1250, 600, 1250, 800, BR, 1.0, 12)
    for y0, y1 in ((330, 330), (800, 800)):
        M.line(c, 1250, y0, 1760, y1, BR, 1.0, 12)
    M.line(c, 1760, 330, 1760, 800, BR, 1.0, 12)
    M.line(c, 1000, 380, 1250, 560, AMARELO, 1.0, 8); M.line(c, 1250, 560, 1760, 760, AMARELO, 1.0, 8)
    M.line(c, 1000, 760, 1250, 560, AMARELO, 1.0, 8); M.line(c, 1250, 560, 1760, 370, AMARELO, 1.0, 8)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Física", "Luz e", "sombra", "e a câmara escura")


def d(c):  # o macete
    palco(c)
    E.capa_rotulo(c, "Física", COR)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "o atalho da", 84, 330, 120, "i", BR)
    E.escreve(c, "câmara escura", 84, 500, 150, "g", BR)
    E.escreve(c, "distância ÷ profundidade", 84, 700, 96, "g", claro)
    E.escreve(c, "= quantas vezes menor", 84, 850, 90, "i", BR)
    E.orbita(c, 1600, 300, 180, E.mix(COR, BR, 0.82))


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_arvore_de_cabeca_para_baixo", a), ("capa_B_luz_sombra_camara", b), ("capa_C_atalho_da_camara", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
