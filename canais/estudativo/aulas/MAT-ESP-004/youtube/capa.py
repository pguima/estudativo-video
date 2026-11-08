"""Capas do MAT-ESP-004 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: não se cruzam e não são paralelas
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    pts = E.paralelepipedo(c, 99, 0, 130, 900, 520, 330, 330, escuro=True, cor=BR, preenche=0.1, largura=8)
    M.line(c, *pts[0], *pts[1], AMARELO, 1, 22)
    M.line(c, *pts[4], *pts[7], AMARELO, 1, 18, dash=[22, 14])
    E.escreve(c, "não se cruzam", 860, 380, 110, "i", BR)
    E.escreve(c, "e não são", 860, 520, 110, "i", BR)
    E.escreve(c, "paralelas", 850, 720, 190, "g", AMARELO)
    E.escreve(c, "são reversas", 860, 900, 110, "i", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Retas", "no espaço", "paralelas e reversas")


def d(c):  # o atalho: 2 perguntas
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "o atalho", 84, 340, 110, "i", BR)
    E.escreve(c, "2 perguntas", 76, 560, 200, "g", BR)
    for k, (q, r) in enumerate((("se cruzam?", "concorrentes"), ("mesma direção?", "paralelas"), ("nenhuma?", "reversas"))):
        y = 720 + 120 * k
        E.escreve(c, q, 90, y, 70, "i", BR)
        E.escreve(c, "→ " + r, 700, y, 70, "g", AMARELO)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_nao_sao_paralelas", a), ("capa_B_retas_no_espaco", b), ("capa_C_duas_perguntas", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
