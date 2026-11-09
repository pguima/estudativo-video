"""Capas do FIS-MAG-011 (1280x720). Uso: python capa.py"""
import math, subprocess, sys
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


def palco_capa(c):
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Física", COR)


def a(c):  # o gancho: qual usina à noite?
    E.capa_base(c, COR); E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "qual usina", 84, 420, 170, "g", BR)
    E.escreve(c, "à noite?", 84, 620, 200, "g", AMARELO)
    E.escreve(c, "5 questões de usinas", 84, 820, 100, "i", BR)
    for i, (s, ok) in enumerate((("solar", False), ("eólica", False), ("térmica", False), ("hidrelétrica", True))):
        y = 260 + i * 150
        E.pilula(c, s, 1430, y, 64, "g", fundo="#1B1B22")
        E.selo(c, 1760, y - 22, 44, ok)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Física", "Praticando", "usinas", "e matriz elétrica")


def d(c):  # o macete: comece pelo que gira a turbina
    palco_capa(c)
    E.escreve(c, "comece pelo", 84, 340, 130, "i", BR)
    E.escreve(c, "que gira", 84, 540, 180, "g", BR)
    E.escreve(c, "a turbina", 84, 720, 180, "g", E.mix(COR, BR, 0.5))
    E.escreve(c, "água, vapor ou vento", 84, 900, 90, "i", BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_qual_usina_a_noite", a), ("capa_B_praticando_usinas", b), ("capa_C_o_que_gira_a_turbina", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
