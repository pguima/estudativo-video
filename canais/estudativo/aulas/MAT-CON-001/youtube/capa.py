"""Capas do MAT-CON-001 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: {1, 2, 3} tem 8 subconjuntos, não 6
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "quantos", 84, 360, 120, "i", BR)
    E.escreve(c, "subconjuntos?", 84, 520, 150, "g", BR)
    E.escreve(c, "{1, 2, 3}", 84, 800, 210, "g", BR)
    E.escreve(c, "6", 1040, 800, 260, "g", BR)
    E.risco(c, 990, 860, 1240, 560, 9, 0, AMARELO, 34)
    E.bola(c, 1640, 680, 200, AMARELO)
    E.centro(c, "8", 1640, 780, 280, "g", COR)
    E.escreve(c, "o vazio também conta", 84, 1000, 90, "i", BR)


def b(c):  # o modelo
    E.capa_modelo(c, "Matemática", "Pertence", "ou contido?", "sem trocar")


def d(c):  # o atalho
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "contar subconjuntos", 84, 360, 120, "i", BR)
    E.escreve(c, "sem listar", 76, 580, 220, "g", BR)
    E.formula(c, "2^3 = 8", 84, 900, 260, "g", E.mix(COR, BR, 0.55))


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_quantos_subconjuntos", a), ("capa_B_pertence_ou_contido", b), ("capa_C_contar_sem_listar", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
