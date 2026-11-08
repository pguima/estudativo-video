"""Capas do MAT-RAZ-016 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: 72 km/h = 20 m/s, com uma conta só
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "72 km/h", 76, 470, 230, "g", BR)
    E.escreve(c, "= 20 m/s", 76, 720, 230, "g", AMARELO)
    E.escreve(c, "com uma conta só", 84, 900, 110, "i", BR)
    E.pilula(c, "÷ 3,6", 1500, 300, 110, "g", fundo=BR, cor=COR)


def b(c):  # o modelo
    E.capa_modelo(c, "Matemática", "km/h", "em m/s", "sem errar a direção")


def d(c):  # o atalho: três pares
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "guarde", 84, 360, 150, "i", BR)
    E.escreve(c, "3 pares", 76, 590, 230, "g", BR)
    cl = E.mix(COR, BR, 0.6)
    for i, (k, m) in enumerate((("36", "10"), ("72", "20"), ("108", "30"))):
        y = 330 + i * 230
        E.escreve(c, f"{k} = {m}", 1180, y, 150, "g", cl)
    E.escreve(c, "km/h ao lado de m/s", 90, 860, 100, "i", BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_72_vira_20", a), ("capa_B_km_h_em_m_s", b), ("capa_C_tres_pares", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
