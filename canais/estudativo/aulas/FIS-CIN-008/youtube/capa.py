"""Capas do FIS-CIN-008 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: 1, 4, 9, 16
    E.capa_base(c, COR); E.capa_rotulo(c, "Física", COR)
    claro = E.mix(COR, BR, 0.55)
    E.escreve(c, "1, 4, 9, 16", 84, 430, 200, "g", BR)
    E.escreve(c, "por que os quadrados?", 84, 620, 110, "g", AMARELO)
    E.escreve(c, "a posição no movimento acelerado", 84, 780, 70, "i", claro)
    y = 960
    M.line(c, 80, y, 1840, y, BR, 1.0, 8)
    for k, x in enumerate((200, 300, 600, 1100, 1800)):
        F.carrinho(c, x, y, 190, cor=BR, a=0.3 + 0.175 * k)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Física", "Posição", "no MUV", "o sorvetão")


def d(c):  # o macete: velocidade média
    palco(c)
    E.escreve(c, "sem t ao quadrado:", 84, 330, 110, "i", BR)
    E.formula(c, "Δs = f{v₀ + v}{2} · t", 84, 640, 190, "g", BR)
    E.escreve(c, "a média das velocidades", 84, 930, 90, "g", E.mix(COR, BR, 0.5))


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_quadrados_perfeitos", a), ("capa_B_posicao_no_muv", b), ("capa_C_media_das_velocidades", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
