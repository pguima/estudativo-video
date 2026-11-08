"""Capas do MAT-RAZ-015 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: 2 h 30 min não é 2,3 h
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "180 km em 2 h 30 min", 84, 360, 110, "i", BR)
    E.escreve(c, "2,3 h?", 76, 640, 260, "g", BR)
    E.risco(c, 60, 680, 860, 430, 9, 0, AMARELO, 32)
    E.escreve(c, "= 2,5 h", 1000, 640, 200, "g", AMARELO)
    E.escreve(c, "o erro antes da conta", 84, 880, 100, "i", BR)


def b(c):  # o modelo
    E.capa_modelo(c, "Matemática", "Velocidade", "média", "e taxas, sem erro")


def d(c):  # o atalho: meia hora? dobre tudo
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "tem meia hora?", 84, 360, 140, "i", BR)
    E.escreve(c, "dobre tudo", 76, 590, 230, "g", BR)
    E.formula(c, "f{180}{2,5} = f{360}{5} = 72 km/h", 84, 860, 110, "g", E.mix(COR, BR, 0.6))


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_2h30_nao_e_2_3", a), ("capa_B_velocidade_media", b), ("capa_C_dobre_tudo", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
