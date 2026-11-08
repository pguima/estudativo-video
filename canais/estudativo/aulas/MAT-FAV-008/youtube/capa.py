"""Capas do MAT-FAV-008 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: 5 situações
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "5 situações", 84, 420, 190, "g", BR)
    E.escreve(c, "|x − 1| ≤ 3", 84, 620, 110, "g", AMARELO)
    E.formula(c, "f^{−1}(x)", 760, 620, 110, "g", BR)
    E.escreve(c, "f(x + 1)", 84, 790, 110, "g", BR)
    E.escreve(c, "par ou ímpar?", 600, 790, 110, "g", AMARELO)
    E.escreve(c, "resolva antes da resposta", 84, 950, 80, "i", BR)


def b(c):  # o modelo
    E.capa_modelo(c, "Matemática", "Praticando", "funções", "modular e inversa")


def d(c):  # o ângulo do macete: cada ferramenta, uma pergunta
    palco(c)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "1 pergunta", 84, 420, 170, "g", BR)
    E.escreve(c, "por ferramenta", 84, 580, 120, "i", BR)
    for i, s in enumerate(("qual faixa?", "qual distância?", "quem vem primeiro?", "como desfazer?", "que espelho?")):
        E.escreve(c, s, 1100, 300 + i * 150, 74, "g", AMARELO if i % 2 == 0 else BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_5_situacoes", a), ("capa_B_praticando_funcoes", b), ("capa_C_uma_pergunta_por_ferramenta", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
