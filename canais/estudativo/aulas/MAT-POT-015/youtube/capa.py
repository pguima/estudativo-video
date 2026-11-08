"""Capas do MAT-POT-015 (1280x720). Uso: python capa.py"""
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


def escuro(c):
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)


def a(c):  # o gancho: quanto tempo a luz do Sol leva?
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.bola(c, 1560, 470, 250, "#F7B500")
    E.escreve(c, "luz do Sol:", 84, 420, 170, "i", BR)
    E.escreve(c, "quantos", 84, 640, 220, "g", AMARELO)
    E.escreve(c, "minutos?", 84, 860, 220, "g", AMARELO)
    E.escreve(c, "até chegar em você", 84, 1000, 110, "i", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Praticando", "notação", "científica")


def d(c):  # o atalho: ande a vírgula antes de dividir
    escuro(c)
    E.escreve(c, "ande a vírgula", 84, 370, 170, "g", BR)
    E.escreve(c, "antes de dividir", 84, 550, 170, "i", BR)
    E.formula(c, "1,5 × 10^8 = 15 × 10^7", 84, 760, 130, "g", BR)
    E.escreve(c, "15 ÷ 3 = 5", 84, 960, 190, "g", AMARELO)


NOMES = (("capa_A_luz_do_sol", a), ("capa_B_praticando_notacao", b), ("capa_C_virgula_antes", d))


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in NOMES:
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()

