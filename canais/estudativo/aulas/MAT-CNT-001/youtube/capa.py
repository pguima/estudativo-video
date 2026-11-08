"""Capas do MAT-CNT-001 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: 3 camisas e 4 calças não dão 7
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "3 camisas", 84, 360, 120, "i", BR)
    E.escreve(c, "4 calças", 84, 500, 120, "i", BR)
    E.escreve(c, "3 + 4 = 7", 84, 760, 190, "g", BR)
    E.risco(c, 60, 700, 870, 690, 9, 0, AMARELO, 30)
    E.escreve(c, "são", 960, 740, 130, "i", BR)
    E.bola(c, 1480, 690, 260, "#FFFFFF")
    E.centro(c, "12", 1480, 690 + 80, 230, "g", COR)
    E.escreve(c, "roupas diferentes", 84, 990, 110, "i", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Contar", "sem listar", "árvore e casinhas")


def d(c):  # o atalho: casinhas iguais viram potência
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "senha de 4 dígitos", 84, 330, 110, "i", BR)
    for i in range(4):
        x = 190 + i * 300
        caixa(c, x, 580, 190, "10", BR, fundo="#1A1640")
        if i:
            E.centro(c, "×", x - 150, 580 + 27, 68, "g", BR)
    E.escreve(c, "=", 1260, 640, 160, "g", BR)
    E.formula(c, "10^4", 1400, 660, 220, "g", AMARELO)
    E.escreve(c, "10.000 senhas", 84, 940, 140, "g", BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_nao_da_7", a), ("capa_B_contar_sem_listar", b), ("capa_C_casinhas_potencia", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
