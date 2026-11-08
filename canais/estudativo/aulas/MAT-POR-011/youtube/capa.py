"""Capas do MAT-POR-011 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: caiu 20%, subir 20% não basta
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "caiu 20%", 84, 390, 170, "g", BR)
    E.escreve(c, "para voltar:", 84, 560, 110, "i", BR)
    E.escreve(c, "+20%", 84, 820, 220, "g", E.mix(COR, BR, 0.55))
    E.risco(c, 70, 840, 640, 640, 9, 0, AMARELO, 30)
    E.escreve(c, "+25%", 84 + E.larg("+20%", "g", 220) + 70, 820, 220, "g", AMARELO)
    E.escreve(c, "o salário não volta sozinho", 84, 990, 90, "i", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Voltar ao", "valor original", "depois de uma queda")


def d(c):  # o atalho: perdeu 1/5, ganha 1/4
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    CL = E.mix(COR, BR, 0.55)
    E.escreve(c, "perdeu", 120, 360, 110, "i", BR)
    E.escreve(c, "ganha", 900, 360, 110, "i", CL)
    E.fracao(c, 1, 5, 260, 560, 190, BR)
    M.arrow(c, 440, 580, 820, 580, CL, 1, 12, 36)
    E.fracao(c, 1, 4, 1040, 560, 190, CL)
    E.escreve(c, "= 25%", 1200, 640, 140, "g", BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_20_nao_volta", a), ("capa_B_voltar_ao_original", b), ("capa_C_um_quinto_um_quarto", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
