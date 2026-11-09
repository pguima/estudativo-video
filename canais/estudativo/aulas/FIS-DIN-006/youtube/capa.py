"""Capas do FIS-DIN-006 (1280x720). Uso: python capa.py"""
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


def fsub(c, base, sb, x, y, size, cor):
    """letra com subscrito (F com R embaixo); devolve a largura"""
    E.escreve(c, base, x, y, size, "g", cor)
    w = E.larg(base, "g", size)
    E.escreve(c, sb, x + w + size * 0.02, y + size * 0.2, size * 0.6, "g", cor)
    return w + E.larg(sb, "g", size * 0.6) + size * 0.06


def a(c):  # o gancho: 5 situações do trânsito
    E.capa_base(c, COR); E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "5", 84, 520, 400, "g", AMARELO)
    E.escreve(c, "situações", 400, 380, 150, "g", BR)
    E.escreve(c, "do trânsito", 400, 540, 130, "g", BR)
    E.escreve(c, "resolva antes da resposta", 84, 800, 90, "i", BR)
    F.carrinho(c, 1520, 980, 560, BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Física", "Leis de", "Newton", "praticando")


def d(c):  # o macete: para onde aponta a aceleração
    palco(c)
    E.escreve(c, "antes da conta", 84, 330, 110, "i", BR)
    E.escreve(c, "para onde", 84, 560, 170, "g", BR)
    E.escreve(c, "aponta a?", 84, 760, 170, "g", "#B48CFF")
    E.escreve(c, "a resultante vai junto", 84, 930, 84, "i", E.mix(COR, BR, 0.5))
    F.seta(c, 1350, 560, 1800, 560, "#B48CFF", 1.0, 30, cabeca=90)


CAPAS = (("capa_A_cinco_situacoes_do_transito", a), ("capa_B_praticando_leis_de_newton", b), ("capa_C_para_onde_aponta_a", d))


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in CAPAS:
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
