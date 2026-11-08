"""Capas do MAT-EST-002 (1280x720). Uso: python capa.py"""
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


def classe(c, a, b, x, y, size, cor):
    """o rótulo "a ⊢ b", com o sinal desenhado"""
    s1, s2 = str(a), str(b)
    w1 = E.larg(s1, "g", size)
    gap = size * 1.05
    E.escreve(c, s1, x, y, size, "g", cor)
    sx, sy = x + w1 + size * 0.28, y - size * 0.36
    M.line(c, sx, sy - size * 0.32, sx, sy + size * 0.32, cor, 1, size * 0.09)
    M.line(c, sx, sy, sx + gap - size * 0.56, sy, cor, 1, size * 0.09)
    E.escreve(c, s2, x + w1 + gap, y, size, "g", cor)


def ficha(c, s, cx, cy, size, fundo, cor_t):
    w = E.larg(s, "b", size) + size * 1.1
    h = size * 1.55
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2, cy - h / 2, w, h), h / 2, h / 2), M.paint(fundo))
    E.centro(c, s, cx, cy + size * 0.36, size, "b", cor_t)


def a(c):  # o gancho: da lista solta à tabela
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "lista solta?", 84, 330, 120, "i", BR)
    x, y = 84, 470
    for i, s in enumerate(("ônibus", "carro", "ônibus", "a pé", "bicicleta", "ônibus", "carro")):
        w = E.larg(s, "b", 52) + 52 * 1.1
        if x + w > 1020:
            x, y = 140, y + 120
        ficha(c, s, x + w / 2, y, 52, BR if i % 2 else AMARELO, COR)
        x += w + 24
    E.escreve(c, "vira tabela", 84, 900, 150, "g", BR)
    for j, (n, v) in enumerate((("ônibus", "8"), ("carro", "5"), ("bicicleta", "4"), ("a pé", "3"))):
        y = 360 + j * 130
        E.escreve(c, n, 1260, y, 80, "b", BR)
        E.escreve(c, v, 1700, y, 90, "g", AMARELO)
    M.line(c, 1240, 270, 1800, 270, BR, 1, 6)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Tabela de", "frequência", "e classes")


def d(c):  # o atalho: total vira 100
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "faça o total virar 100", 84, 340, 110, "i", BR)
    E.formula(c, "f{7}{20} = f{35}{100}", 84, 720, 170, "g", BR)
    E.escreve(c, "= 35%", 800, 790, 200, "g", AMARELO)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_lista_vira_tabela", a), ("capa_B_tabela_de_frequencia", b), ("capa_C_total_vira_100", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
