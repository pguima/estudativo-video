"""Capas do MAT-RAZ-006 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: 3 kg = R$ 18, 7 kg = ?
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "3 kg", 84, 420, 190, "g", BR)
    E.escreve(c, "R$ 18", 620, 420, 190, "g", BR)
    E.escreve(c, "7 kg", 84, 680, 190, "g", BR)
    E.escreve(c, "R$ ?", 620, 680, 190, "g", AMARELO)
    E.escreve(c, "2 caminhos, 1 resposta", 84, 950, 110, "i", BR)


def b(c):  # o modelo
    E.capa_modelo(c, "Matemática", "Regra", "de três", "direta")


def d(c):  # o atalho: divida antes de multiplicar
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    cl = E.mix(COR, BR, 0.55)
    E.escreve(c, "o atalho:", 84, 340, 140, "i", BR)
    E.escreve(c, "divida antes", 76, 540, 190, "g", BR)
    E.escreve(c, "de multiplicar", 76, 720, 150, "i", BR)
    E.formula(c, "7 · (18 ÷ 3) = 7 · 6 = 42", 84, 950, 120, "g", cl)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_3kg_18_reais_7kg", a), ("capa_B_regra_de_tres_direta", b), ("capa_C_divida_antes", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
