"""Capas do MAT-RAZ-024 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: 40 na ida, 60 na volta: não é 50
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "ida a 40, volta a 60", 84, 360, 110, "i", BR)
    E.escreve(c, "média 50?", 76, 620, 230, "g", BR)
    E.risco(c, 60, 660, 1120, 430, 9, 0, AMARELO, 32)
    E.escreve(c, "é 48", 1240, 620, 230, "g", AMARELO)
    E.escreve(c, "a pegadinha da velocidade média", 84, 880, 92, "i", BR)


def b(c):  # o modelo
    E.capa_modelo(c, "Matemática", "Velocidade", "média", "em dois trechos")


def d(c):  # o atalho: o dobro do produto pela soma
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "ida e volta?", 84, 360, 150, "i", BR)
    E.escreve(c, "um atalho", 76, 590, 230, "g", BR)
    E.formula(c, "f{2 × 40 × 60}{40 + 60} = 48", 84, 880, 120, "g", E.mix(COR, BR, 0.6))


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_nao_e_50", a), ("capa_B_velocidade_media_trechos", b), ("capa_C_dobro_do_produto", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
