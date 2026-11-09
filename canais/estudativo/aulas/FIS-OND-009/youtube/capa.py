"""Capas do FIS-OND-009 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: o erro do decibel
    E.capa_base(c, COR); E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "80 → 100 dB:", 84, 400, 150, "g", BR)
    E.escreve(c, "1,25 vez?", 84, 580, 150, "g", BR)
    E.risco(c, 70, 610, 780, 480, 9, 0, AMARELO, 30)
    E.escreve(c, "não: é 100 vezes mais intenso", 84, 820, 90, "i", BR)
    E.pilula(c, "×100", 1570, 500, 160, "g", fundo=AMARELO, cor="#1B1B1B")


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Física", "Praticando:", "som", "e Doppler")


def d(c):  # o macete: o que a questão compara
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "o que a questão compara?", 84, 330, 110, "i", BR)
    claro = E.mix(COR, BR, 0.5)
    for i, (s1, s2) in enumerate((("grave ou agudo", "frequência"), ("forte ou fraco", "decibéis"), ("instrumentos", "timbre"))):
        y = 530 + i * 170
        E.escreve(c, s1, 84, y, 80, "i", claro)
        F.seta(c, 760, y - 28, 900, y - 28, claro, 1.0, 10)
        E.escreve(c, s2, 950, y, 96, "g", BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_100_vezes_mais_intenso", a), ("capa_B_praticando_som", b), ("capa_C_o_que_a_questao_compara", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
