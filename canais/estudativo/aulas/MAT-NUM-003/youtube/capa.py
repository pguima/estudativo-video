"""Capas do MAT-NUM-003 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: a conta que perde dinheiro
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "478 + 356", 84, 430, 270, "g", BR)
    E.escreve(c, "= 724?", 84, 680, 270, "g", AMARELO)
    E.escreve(c, "sumiram R$ 110", 84, 910, 180, "g", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Somar", "de cabeça", "e na conta armada")


def d(c):  # o atalho: complete o número redondo
    palco(c)
    E.escreve(c, "complete o", 84, 370, 170, "i", BR)
    E.escreve(c, "redondo", 84, 560, 190, "g", AMARELO)
    E.escreve(c, "199 + 47", 84, 790, 200, "g", BR)
    E.escreve(c, "= 246", 980, 790, 200, "g", AMARELO)
    E.escreve(c, "sem armar a conta", 84, 960, 130, "i", BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_sumiram_110_reais", a), ("capa_B_somar_de_cabeca", b), ("capa_C_complete_o_redondo", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
