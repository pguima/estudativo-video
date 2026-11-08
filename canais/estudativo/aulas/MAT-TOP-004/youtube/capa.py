"""Capas do MAT-TOP-004 (1280x720). Uso: python capa.py"""
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
MESES = ["jan", "fev", "mar", "abr", "mai", "jun", "jul", "ago", "set", "out", "nov", "dez"]


def a(c):  # o gancho: 13 pessoas, certeza
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "13", 84, 600, 400, "g", AMARELO)
    E.escreve(c, "pessoas", 100, 760, 120, "i", BR)
    for i, m in enumerate(MESES):
        x, y = 860 + (i % 4) * 255, 250 + (i // 4) * 200
        on = i == 4
        M.rrect(c, x, y, 225, 165, 20, AMARELO if on else BR, 1 if on else 0.14)
        E.centro(c, m, x + 112, y + 55, 46, "b", COR if on else BR)
        if on:
            for k in range(2):
                c.drawCircle(x + 80 + k * 66, y + 115, 26, M.paint(COR))
    E.escreve(c, "2 no mesmo mês: certeza", 84, 1000, 100, "i", BR)


def b(c):  # o modelo
    E.capa_modelo(c, "Matemática", "Casa dos", "pombos", "sem mistério")


def d(c):  # o atalho: pior caso + 1
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "o atalho:", 84, 360, 140, "i", BR)
    E.escreve(c, "pior caso + 1", 76, 590, 220, "g", BR)
    E.escreve(c, "12 × 2 + 1 =", 84, 860, 150, "g", BR)
    E.escreve(c, "25", 860, 875, 190, "g", AMARELO)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_13_pessoas", a), ("capa_B_casa_dos_pombos", b), ("capa_C_pior_caso_mais_1", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
