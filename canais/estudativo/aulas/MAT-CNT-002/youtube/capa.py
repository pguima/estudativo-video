"""Capas do MAT-CNT-002 (1280x720). Uso: python capa.py"""
import subprocess, sys
from pathlib import Path
RAIZ = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(RAIZ / "_ferramentas"))
import skia
import editorial as E
import motor as M
BR = "#FFFFFF"
AMARELO = "#FFD500"
COR = E.MATERIAS["Matemática"]["cor"]


def caixa(c, cx, cy, s, txt, cor_txt, borda=BR, fundo=None):
    r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - s / 2, cy - s / 2, s, s), s * 0.12, s * 0.12)
    if fundo:
        c.drawRRect(r, M.paint(fundo))
    c.drawRRect(r, M.paint(borda, 1, stroke=8))
    size = s * (0.56 if len(txt) == 1 else 0.46)
    E.centro(c, txt, cx, cy + size * 0.36, size, "g", cor_txt)


def a(c):  # o gancho: 10 × 9 × 8 = 720 está errado; são 648
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "3 algarismos diferentes", 84, 330, 110, "i", BR)
    E.escreve(c, "10 × 9 × 8 = 720", 84, 580, 170, "g", BR)
    E.risco(c, 60, 520, 1330, 510, 9, 0, AMARELO, 30)
    E.escreve(c, "são", 84, 870, 140, "i", BR)
    E.bola(c, 560, 820, 200, "#FFFFFF")
    E.centro(c, "648", 560, 820 + 60, 170, "g", COR)
    E.escreve(c, "por quê?", 860, 880, 150, "g", AMARELO)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Contar", "com regras", "comece pela difícil")


def d(c):  # o atalho: conte tudo e tire o que não pode
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "conte tudo", 84, 340, 150, "g", BR)
    E.escreve(c, "e tire o proibido", 84, 500, 130, "i", BR)
    E.escreve(c, "720 − 72 =", 84, 800, 200, "g", BR)
    E.escreve(c, "648", 1110, 800, 200, "g", AMARELO)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_nao_sao_720", a), ("capa_B_contar_com_regras", b), ("capa_C_tire_o_proibido", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
