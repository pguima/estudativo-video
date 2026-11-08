"""Capas do MAT-ANG-015 (1280x720). Uso: python capa.py"""
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
LILAS = "#C9C9FF"
VERMELHO = "#FF6B6B"
S, K, F = (170, 930), (170 + 6 * 82, 930), (170 + 6 * 82, 930 - 8 * 82)   # 6 para a direita, 8 para cima


def caminho(c, tinta=BR, hip=AMARELO):
    M.line(c, *S, *K, tinta, 1, 14)
    M.line(c, *K, *F, tinta, 1, 14)
    M.line(c, *F, *S, hip, 1, 12, dash=[30, 20])
    q = 54
    M.line(c, K[0] - q, K[1], K[0] - q, K[1] - q, tinta, 1, 7)
    M.line(c, K[0] - q, K[1] - q, K[0], K[1] - q, tinta, 1, 7)
    for P in (S, F):
        c.drawCircle(*P, 20, M.paint(tinta))
    E.escreve(c, "6", (S[0] + K[0]) / 2 - 30, 1040, 110, "g", tinta)
    E.escreve(c, "8", K[0] + 40, 640, 110, "g", tinta)


def a(c):  # o gancho: não é 14
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    caminho(c)
    E.escreve(c, "10", 250, 560, 150, "g", AMARELO)
    E.escreve(c, "6 + 8 = 14", 1010, 400, 120, "g", LILAS)
    M.line(c, 990, 360, 1660, 340, VERMELHO, 1, 16)
    E.escreve(c, "não é", 1010, 610, 150, "i", BR)
    E.escreve(c, "14!", 1360, 610, 170, "g", BR)
    E.escreve(c, "dá 10", 1010, 850, 200, "g", AMARELO)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Teorema de", "Pitágoras", "hipotenusa e cateto")


def d(c):  # o atalho: soma vezes diferença
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "cateto sem", 110, 380, 120, "i", BR)
    E.escreve(c, "elevar ao quadrado", 110, 520, 110, "g", BR)
    w = E.formula(c, "13^2 − 5^2", 110, 730, 130, "g", claro)
    E.formula(c, "= 18 × 8", 110 + w + 40, 730, 130, "g", AMARELO)
    E.escreve(c, "soma × diferença", 110, 930, 120, "g", AMARELO)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_nao_e_14", a), ("capa_B_teorema_de_pitagoras", b), ("capa_C_soma_vezes_diferenca", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
