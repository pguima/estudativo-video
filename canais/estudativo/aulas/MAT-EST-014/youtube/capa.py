"""Capas do MAT-EST-014 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: 62 acertos e percentil 90
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "acertou 62 de 100", 84, 340, 110, "i", BR)
    E.escreve(c, "percentil", 84, 540, 170, "g", BR)
    E.escreve(c, "90", 84, 840, 330, "g", AMARELO)
    E.escreve(c, "foi bem?", 1150, 760, 150, "g", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Quartis e", "percentis", "sem mistério")


def d(c):  # o atalho: 100 menos o percentil
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "quantos ficaram acima?", 84, 360, 100, "i", BR)
    E.escreve(c, "100 − 90 = 10%", 84, 580, 160, "g", AMARELO)
    E.escreve(c, "entre os 10%", 84, 790, 120, "g", BR)
    E.escreve(c, "mais altos", 84, 920, 120, "g", BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_62_acertos_percentil_90", a), ("capa_B_quartis_e_percentis", b), ("capa_C_cem_menos_o_percentil", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
