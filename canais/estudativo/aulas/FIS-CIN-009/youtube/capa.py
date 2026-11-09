"""Capas do FIS-CIN-009 (1280x720). Uso: python capa.py"""
import subprocess, sys
from pathlib import Path
RAIZ = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(RAIZ / "_ferramentas"))
import skia
import editorial as E
import fisica as F
import motor as M
BR = "#FFFFFF"
AMARELO = "#FFD500"
COR = E.MATERIAS["Física"]["cor"]
E.usar("Física")


def palco(c):
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Física", COR)


def a(c):  # o gancho: o dobro da velocidade, 4 vezes a frenagem
    E.capa_base(c, COR); E.capa_rotulo(c, "Física", COR)
    claro = E.mix(COR, BR, 0.55)
    E.escreve(c, "2× a velocidade", 84, 400, 140, "g", BR)
    E.escreve(c, "4× a frenagem", 84, 590, 160, "g", AMARELO)
    E.escreve(c, "e não 2×", 84, 740, 100, "i", claro)
    y = 960
    M.line(c, 80, y, 1840, y, BR, 1.0, 8)
    M.rrect(c, 120, y + 30, 1600, 40, 20, AMARELO, 1.0)
    F.carrinho(c, 1650, y, 300, cor=BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Física", "Torricelli", "e frenagem", "sem o tempo")


def d(c):  # o macete: velocidade x n, frenagem x n²
    palco(c)
    E.escreve(c, "sem refazer a conta:", 84, 330, 110, "i", BR)
    claro = E.mix(COR, BR, 0.5)
    for i, (v, f_) in enumerate((("10 m/s", "10 m"), ("20 m/s", "40 m"), ("30 m/s", "90 m"))):
        y = 560 + i * 170
        E.escreve(c, v, 120, y, 120, "g", BR)
        E.escreve(c, "→", 680, y, 120, "g", claro)
        E.escreve(c, f_, 860, y, 120, "g", COR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_dobro_quatro_vezes", a), ("capa_B_torricelli_e_frenagem", b), ("capa_C_frenagem_sem_conta", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
