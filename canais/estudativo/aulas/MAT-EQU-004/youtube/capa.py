"""Capas do MAT-EQU-004 (1280x720). Uso: python capa.py"""
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


def palco(c):
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)




def a(c):  # o gancho: 5 − (x − 3) não é 5 − x − 3
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.formula(c, "5 − (x − 3)", 84, 400, 220, cor=BR)
    E.formula(c, "5 − x − 3", 84, 680, 170, cor=BR)
    E.risco(c, 70, 710, 820, 540, 9, 0, AMARELO, 28)
    E.formula(c, "8 − x", 1060, 680, 210, cor=AMARELO)
    E.escreve(c, "errou um sinal?", 84, 950, 130, "i", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Abrir", "parênteses", "sem errar o sinal")


def d(c):  # o atalho: menos sozinho troca todos os sinais
    palco(c)
    E.escreve(c, "o atalho", 84, 330, 150, "i", BR)
    E.escreve(c, "menos sozinho", 76, 540, 170, "g", BR)
    E.escreve(c, "troca todos os sinais", 84, 710, 130, "i", BR)
    E.formula(c, "−(x − 3) = −x + 3", 84, 940, 150, cor=AMARELO)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_errou_um_sinal", a), ("capa_B_abrir_parenteses", b), ("capa_C_menos_troca_sinais", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
