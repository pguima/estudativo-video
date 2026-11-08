"""Capas do MAT-FUN-005 (1280x720). Uso: python capa.py"""
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
VERMELHO = "#FF4D55"


def a(c):  # o gancho: x = 2 dá erro
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.formula(c, "f{1}{x − 2}", 84, 520, 230, "g", BR)
    E.escreve(c, "x = 2?", 84, 900, 170, "g", AMARELO)
    M.rrect(c, 1060, 360, 720, 420, 50, "#121214")
    M.rrect(c, 1110, 410, 620, 200, 24, "#1E2A1E")
    E.centro(c, "ERRO", 1420, 565, 170, "g", VERMELHO)
    for i in range(4):
        M.rrect(c, 1110 + i * 160, 650, 140, 90, 18, "#3C3C46")


def b(c):  # o modelo
    E.capa_modelo(c, "Matemática", "Domínio", "pela fórmula", "do zero")


def d(c):  # o atalho
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "os 2 vilões", 76, 430, 180, "g", BR)
    E.escreve(c, "do domínio", 84, 600, 130, "i", claro)
    for x, simb, regra in ((140, "f{1}{x}", "≠ 0"), (980, "r{x}", "≥ 0")):
        M.rrect(c, x, 700, 760, 260, 40, "#1C1C24")
        E.formula(c, simb, x + 170, 870, 150, "g", VERMELHO, 1, "center")
        E.formula(c, regra, x + 360, 870, 150, "g", BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_x_igual_2_da_erro", a), ("capa_B_dominio_pela_formula", b), ("capa_C_os_dois_viloes", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
