"""Capas do MAT-EQU-010 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: as frações somem num passo só
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.formula(c, "f{x}{2} + f{x}{3} = 5", 84, 470, 180, "g", BR)
    E.escreve(c, "→ 3x + 2x = 30", 84, 740, 150, "g", AMARELO)
    E.escreve(c, "a fração some num passo", 84, 940, 110, "i", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Equação", "com fração", "e vírgula")


def d(c):  # o atalho: dividir por 0,5 é dobrar
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "o atalho", 84, 340, 140, "i", BR)
    E.escreve(c, "÷ 0,5", 76, 560, 210, "g", BR)
    E.escreve(c, "é dobrar", 640, 560, 170, "i", BR)
    E.escreve(c, "0,5x = 1,8", 84, 860, 140, "g", E.mix(COR, BR, 0.55))
    E.escreve(c, "→ x = 3,6", 870, 860, 140, "g", BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_fracao_some", a), ("capa_B_fracao_e_virgula", b), ("capa_C_dividir_por_meio", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
