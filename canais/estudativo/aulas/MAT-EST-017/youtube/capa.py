"""Capas do MAT-EST-017 (1280x720). Uso: python capa.py"""
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
VERMELHO = "#FF5A5A"


def cartao(c, x, y, titulo, dp, cor=BR, w=720, h=250):
    r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 30, 30)
    c.drawRRect(r, M.paint(cor, 1, stroke=6))
    E.centro(c, titulo, x + w / 2, y + 100, 80, "g", cor)
    E.centro(c, dp, x + w / 2, y + 200, 72, "i", cor)


def a(c):  # o gancho: o desvio maior é o mais regular
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "quem é mais", 84, 330, 110, "i", BR)
    E.escreve(c, "regular?", 84, 500, 170, "g", AMARELO)
    E.escreve(c, "o de desvio", 84, 760, 110, "g", BR)
    E.escreve(c, "maior!", 84, 890, 110, "g", BR)
    cartao(c, 1100, 230, "100 m", "DP 0,6 s", E.mix(BR, COR, 0.35))
    cartao(c, 1100, 560, "400 m", "DP 1 s", AMARELO)
    E.risco(c, 1080, 420, 1840, 260, 9, 0, VERMELHO, 22)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Desvio", "padrão", "como interpretar")


def d(c):  # o atalho: o coeficiente de variação
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "médias diferentes?", 84, 340, 110, "i", BR)
    E.escreve(c, "DP ÷ média", 84, 560, 170, "g", AMARELO)
    E.escreve(c, "0,6 ÷ 12 = 5%", 84, 800, 120, "g", E.mix(BR, COR, 0.35))
    E.escreve(c, "1 ÷ 50 = 2%", 84, 960, 120, "g", BR)
    E.escreve(c, "mais regular", 900, 960, 90, "i", AMARELO)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_quem_e_mais_regular", a), ("capa_B_interpretar_desvio_padrao", b), ("capa_C_coeficiente_de_variacao", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
