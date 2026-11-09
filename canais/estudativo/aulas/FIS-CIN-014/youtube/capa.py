"""Capas do FIS-CIN-014 (1280x720). Uso: python capa.py"""
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


def a(c):  # o erro: no alto, a aceleração não é zero
    E.capa_base(c, COR); E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "no alto,", 84, 380, 130, "i", BR)
    E.escreve(c, "v = 0", 84, 590, 190, "g", BR)
    E.escreve(c, "a = 0?", 84, 800, 190, "g", BR)
    E.risco(c, 70, 820, 700, 640, 9, 0, AMARELO, 30)
    E.escreve(c, "a gravidade não desliga", 84, 960, 76, "i", AMARELO)
    E.bola(c, 1500, 330, 90, E.mix(COR, BR, 0.85))
    F.seta(c, 1500, 460, 1500, 860, AMARELO, 1.0, 22)
    E.escreve(c, "g", 1560, 720, 150, "g", AMARELO)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Física", "Lançamento", "para cima", "e altura máxima")


def d(c):  # o macete: subida = queda ao contrário
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "a subida é", 84, 330, 120, "i", BR)
    E.escreve(c, "a queda", 76, 510, 170, "g", BR)
    E.escreve(c, "ao contrário", 76, 690, 150, "g", BR)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "t = v₀ ÷ 10", 84, 900, 90, "g", claro)
    for i, (h, v) in enumerate(((0, 30), (25, 20), (40, 10), (45, 0))):
        y = 900 - h * 14
        E.bola(c, 1450, y, 40, E.mix(COR, BR, 0.2 + 0.25 * (i == 3)))
        if v:
            F.seta(c, 1530, y, 1530, y - v * 6, claro, 1.0, 10)
    F.seta(c, 1700, 300, 1700, 860, BR, 1.0, 14)
    E.escreve(c, "g", 1740, 620, 110, "g", BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_no_alto_a_zero", a), ("capa_B_lancamento_para_cima", b), ("capa_C_queda_ao_contrario", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
