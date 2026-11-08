"""Capas do MAT-EST-010 (1280x720). Uso: python capa.py"""
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
VERMELHO = "#FF5A5A"


def a(c):  # o gancho: 40 e 60 km/h dão 48, não 50
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "ida a 40, volta a 60:", 84, 330, 96, "i", BR)
    E.escreve(c, "média", 84, 540, 170, "g", BR)
    E.escreve(c, "48", 84, 860, 330, "g", AMARELO)
    E.escreve(c, "50?", 1180, 700, 200, "g", BR, 0.9)
    M.line(c, 1150, 690, 1560, 540, VERMELHO, 1, 26)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Média", "geométrica", "e harmônica")


def d(c):  # o atalho: o dobro do produto pela soma
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "velocidade média", 84, 360, 110, "i", BR)
    E.escreve(c, "sem errar:", 84, 540, 140, "g", BR)
    E.formula(c, "f{2 · a · b}{a + b}", 1420, 700, 190, "g", AMARELO, 1.0, "center")
    E.escreve(c, "o atalho", 84, 840, 150, "g", AMARELO)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_48_nao_50", a), ("capa_B_media_geometrica_harmonica", b), ("capa_C_atalho_das_velocidades", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
