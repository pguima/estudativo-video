"""Capas do MAT-FRA-013 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: o caminhão e a armadilha do restante
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "240 caixas", 84, 400, 200, "g", BR)
    E.escreve(c, "saem", 84, 630, 160, "i", BR)
    E.escreve(c, "3/8", 440, 630, 180, "g", AMARELO)
    E.escreve(c, "e", 800, 630, 160, "i", BR)
    E.escreve(c, "1/5", 900, 630, 180, "g", AMARELO)
    E.escreve(c, "do resto", 1260, 625, 150, "i", BR)
    E.escreve(c, "quantas ficam?", 84, 930, 200, "g", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Praticando", "frações", "as 4 operações")


def d(c):  # o atalho: multiplique só as sobras
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "o atalho", 84, 350, 150, "i", BR)
    E.escreve(c, "das sobras", 560, 350, 170, "g", BR)
    y, s = 680, 240
    E.fracao(c, 4, 5, 230, y, s, BR)
    E.escreve(c, "×", 370, y + 65, 180, "g", BR)
    E.fracao(c, 5, 8, 640, y, s, BR)
    E.escreve(c, "=", 790, y + 65, 180, "g", BR)
    E.fracao(c, 1, 2, 1060, y, s, AMARELO)
    E.escreve(c, "metade", 1220, y + 60, 170, "i", AMARELO)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_quantas_ficam", a), ("capa_B_praticando_operacoes", b), ("capa_C_atalho_das_sobras", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
