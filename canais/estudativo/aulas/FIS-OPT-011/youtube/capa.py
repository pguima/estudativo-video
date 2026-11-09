"""Capas do FIS-OPT-011 (1280x720). Uso: python capa.py"""
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
    E.escreve(c, "onde fica", 84, 400, 170, "g", BR)
    E.escreve(c, "a imagem?", 84, 590, 170, "g", AMARELO)
    E.escreve(c, "uma conta e o sinal certo", 84, 790, 84, "i", BR)
    E.formula(c, "f{1}{f} = f{1}{p} + f{1}{p'}", 1120, 600, 160, "g", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Física", "Gauss", "espelhos", "equação e aumento")


def d(c):  # o macete
    palco(c)
    E.capa_rotulo(c, "Física", COR)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "sem MMC:", 84, 330, 120, "i", BR)
    E.formula(c, "p' = f{f · p}{p − f}", 84, 640, 200, "g", BR)
    E.escreve(c, "o atalho dos espelhos", 84, 900, 90, "g", claro)
    E.orbita(c, 1600, 300, 180, E.mix(COR, BR, 0.82))


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_onde_fica_a_imagem", a), ("capa_B_equacao_dos_espelhos", b), ("capa_C_atalho_sem_mmc", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
