"""Capas do MAT-CNT-010 (1280x720). Uso: python capa.py"""
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


def pilula(c, s, cx, cy, size, fundo, cor):
    w, h = E.larg(s, "g", size) + size * 1.1, size * 1.6
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2, cy - h / 2, w, h), h / 2, h / 2), M.paint(fundo))
    E.centro(c, s, cx, cy + size * 0.36, size, "g", cor)


def a(c):  # o gancho: as 4 decisões
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "qual conta você faz?", 84, 340, 110, "i", BR)
    for i, op in enumerate(("multiplico", "permuto", "arranjo", "combino?")):
        x, y = 84 + (i % 2) * 820, 520 + (i // 2) * 230
        forte = op == "combino?"
        w = E.larg(op, "g", 120) + 132
        pilula(c, op, x + w / 2, y, 120, AMARELO if forte else BR, COR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Praticando", "contagem", "5 situações resolvidas")


def d(c):  # o macete: decida antes da conta
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "a ordem muda o resultado?", 84, 370, 110, "i", BR)
    E.escreve(c, "sim:", 84, 600, 150, "i", BR)
    E.escreve(c, "arranjo", 380, 600, 170, "g", AMARELO)
    E.escreve(c, "não:", 84, 850, 150, "i", BR)
    E.escreve(c, "combinação", 380, 850, 170, "g", AMARELO)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_qual_conta", a), ("capa_B_praticando", b), ("capa_C_ordem_muda", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
