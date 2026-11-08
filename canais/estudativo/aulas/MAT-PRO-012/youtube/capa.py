"""Capas do MAT-PRO-012 (1280x720). Uso: python capa.py"""
import subprocess, sys
from pathlib import Path
RAIZ = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(RAIZ / "_ferramentas"))
import skia
import editorial as E
import motor as M
BR = "#FFFFFF"
AM = "#FFD500"
COR = E.MATERIAS["Matemática"]["cor"]


def a(c):  # o gancho: a armadilha do remédio
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "800 mg, meia-vida 6 h", 84, 360, 120, "g", BR)
    E.escreve(c, "quanto resta em 24 h?", 84, 520, 110, "i", BR)
    E.escreve(c, "200", 120, 880, 230, "g", E.mix(COR, BR, 0.55))
    E.risco(c, 110, 900, 560, 690, 9, 0, AM, 30)
    E.escreve(c, "50", 760, 880, 260, "g", AM)


def b(c):  # o modelo
    E.capa_modelo(c, "Matemática", "Praticando", "PG", "5 problemas")


def d(c):  # o ângulo das ferramentas
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "qual ferramenta?", 84, 330, 140, "i", BR)
    for i, (l, r_) in enumerate((("uma posição", "termo geral"), ("dois vizinhos", "termo do meio"), ("um total", "soma"), ("a bola", "soma infinita"))):
        y = 520 + i * 135
        E.escreve(c, l, 84, y, 90, "g", BR)
        E.escreve(c, "→ " + r_, 760, y, 90, "g", AM)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_remedio_200_ou_50", a), ("capa_B_praticando_pg", b), ("capa_C_qual_ferramenta", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
