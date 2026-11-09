"""Capas do FIS-CIN-007 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: o que é segundo ao quadrado?
    E.capa_base(c, COR); E.capa_rotulo(c, "Física", COR)
    claro = E.mix(COR, BR, 0.55)
    E.formula(c, "m/s^2", 84, 470, 260, "g", BR)
    E.escreve(c, "segundo ao quadrado?", 84, 680, 110, "g", AMARELO)
    E.escreve(c, "a aceleração sem mistério", 84, 840, 80, "i", claro)
    F.cronometro(c, 1560, 560, 230, 15, 1.0, "", cor=AMARELO)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Física", "Aceleração", "e o MUV", "do zero")


def d(c):  # o macete: sinais de v e a
    palco(c)
    E.escreve(c, "acelerado ou retardado?", 84, 330, 110, "i", BR)
    E.escreve(c, "olhe os sinais", 76, 520, 150, "g", BR)
    claro = E.mix(COR, BR, 0.5)
    for i, (sv, sa, r) in enumerate((("+", "+", "acelerado"), ("−", "−", "acelerado"), ("+", "−", "retardado"))):
        y = 700 + i * 130
        E.escreve(c, f"{sv}  {sa}", 120, y, 110, "g", BR)
        E.escreve(c, r, 420, y, 100, "g", claro if i == 2 else COR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_segundo_ao_quadrado", a), ("capa_B_aceleracao_e_muv", b), ("capa_C_olhe_os_sinais", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
