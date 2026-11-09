"""Capas do FIS-CIN-003 (1280x720). Uso: python capa.py"""
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
    E.capa_rotulo(c, "Física", COR)


def a(c):  # o gancho: 20 vira 16 e 12
    E.capa_base(c, COR); E.capa_rotulo(c, "Física", COR)
    claro = E.mix(COR, BR, 0.55)
    E.escreve(c, "20 m/s", 84, 400, 190, "g", BR)
    E.escreve(c, "vira 16 e 12", 84, 600, 130, "g", BR)
    E.escreve(c, "e não é erro", 84, 790, 110, "i", claro)
    O, B = (1180, 940), (1780, 490)
    M.line(c, *B, B[0], O[1], BR, 0.7, 8, dash=[22, 16])
    M.line(c, *B, O[0], B[1], BR, 0.7, 8, dash=[22, 16])
    F.seta(c, *O, B[0], O[1], AMARELO, 1.0, 20)
    F.seta(c, *O, O[0], B[1], AMARELO, 1.0, 20)
    F.seta(c, *O, *B, BR, 1.0, 26)
    E.escreve(c, "16", 1420, 1030, 90, "g", AMARELO); E.escreve(c, "12", 1050, 740, 90, "g", AMARELO)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Física", "Decompor", "vetores", "nos eixos")


def d(c):  # o macete: 37° e o 3-4-5
    palco(c)
    E.escreve(c, "componentes a 37°", 84, 330, 110, "i", BR)
    E.escreve(c, "÷ 5, × 4, × 3", 76, 540, 170, "g", BR)
    O, P, Q = (1150, 900), (1750, 900), (1750, 450)
    F.poli(c, [O, P, Q, O], 1.0, BR, 1.0, 10)
    for s, x, y in (("4", 1420, 1010), ("3", 1800, 710), ("5", 1340, 640)):
        E.escreve(c, s, x, y, 110, "g", COR)
    E.escreve(c, "37°", 1290, 880, 60, "g", BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_vinte_vira_dezesseis_e_doze", a), ("capa_B_decompor_vetores", b), ("capa_C_trinta_e_sete_graus", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
