"""Capas do MAT-CNT-019 (1280x720). Uso: python capa.py"""
import subprocess, sys
from pathlib import Path
RAIZ = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(RAIZ / "_ferramentas"))
import skia
import editorial as E
import motor as M
BR = "#FFFFFF"
AMARELO = "#FFD500"
COR = E.MATERIAS["Matemática"]["cor"]
OPCOES = ("conto", "complementar", "somo", "multiplico")


def a(c):  # o gancho: qual ferramenta? 4 pílulas
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "qual ferramenta?", 90, 360, 150, "g", BR)
    for i, op in enumerate(OPCOES):
        x, y = 110 + (i % 2) * 760, 560 + (i // 2) * 200
        w = E.larg(op + "?", "g", 100) + 110
        E.pilula(c, op + "?", x + w / 2, y, 100, estilo="g", fundo=AMARELO if i == 1 else BR, cor=COR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Praticando", "probabilidade", "4 situações resolvidas")


def d(c):  # o macete: a palavra da pergunta escolhe a ferramenta
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    for i, (perg, op) in enumerate((("pelo menos um?", "1 − nenhum"), ("“ou”?", "some − comum"), ("“e”?", "multiplique"))):
        y = 380 + i * 230
        E.escreve(c, perg, 84, y, 110, "i", BR)
        E.escreve(c, op, 820, y, 110, "g", AMARELO)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_qual_ferramenta", a), ("capa_B_praticando", b), ("capa_C_palavra_pista", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
