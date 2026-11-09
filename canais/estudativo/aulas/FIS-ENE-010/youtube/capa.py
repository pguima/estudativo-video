"""Capas do FIS-ENE-010 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: a bala que perde 99 % da energia
    E.capa_base(c, COR); E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "bala no bloco", 84, 380, 130, "i", BR)
    E.escreve(c, "900 J → 9 J", 84, 620, 190, "g", BR)
    E.escreve(c, "onde foi parar?", 84, 840, 130, "g", AMARELO)
    claro = E.mix(COR, BR, 0.85)
    M.rrect(c, 1500, 520, 300, 260, 24, E.mix(COR, "#000000", 0.35))
    M.rrect(c, 1180, 630, 120, 40, 16, claro)
    F.seta(c, 1200, 560, 1440, 560, BR, 1.0, 14)


def b(c):  # o modelo padrão
    E.capa_base(c, COR); E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "Impulso", 76, 450, 210, "g", BR)
    E.escreve(c, "e colisões", 76, 660, 210, "g", BR)
    E.escreve(c, "exercícios", 84, 860, 150, "i", BR)
    E.simbolo(c, 1600, 780, 240, cor=E.mix(COR, BR, 0.82), forma="orbita")


def d(c):  # o macete: dividir sem vírgula
    palco(c)
    E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "divida sem vírgula", 84, 340, 110, "i", BR)
    E.formula(c, "f{13,5}{0,015} = f{13.500}{15}", 84, 640, 150, "g", BR)
    E.escreve(c, "= 900 N", 84, 940, 150, "g", E.mix(COR, BR, 0.5))


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_bala_no_bloco_900_para_9", a), ("capa_B_impulso_e_colisoes_exercicios", b), ("capa_C_dividir_sem_virgula", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
