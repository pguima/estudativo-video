"""Capas do FIS-DIN-003 (1280x720). Uso: python capa.py"""
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


def seta2(c, y, cor):
    F.seta(c, 1500, y, 1800, y, cor, 1.0, 30, cabeca=90)
    F.seta(c, 1460, y + 150, 1160, y + 150, cor, 1.0, 30, cabeca=90)


def a(c):  # o gancho: se a carroça puxa o cavalo de volta, como andam?
    E.capa_base(c, COR); E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "Ação e reação", 84, 400, 150, "g", BR)
    E.escreve(c, "se anulam?", 84, 590, 170, "g", AMARELO)
    E.escreve(c, "então como o cavalo anda?", 84, 800, 90, "i", BR)
    seta2(c, 520, BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Física", "Ação e", "reação", "a 3ª lei")


def d(c):  # o macete: troque os nomes
    palco(c)
    E.escreve(c, "o macete: troque os nomes", 84, 330, 100, "i", BR)
    E.escreve(c, "A empurra B", 84, 560, 170, "g", BR)
    E.escreve(c, "B empurra A", 84, 760, 170, "g", E.mix(COR, BR, 0.5))
    E.escreve(c, "o par está sempre em outro corpo", 84, 930, 76, "i", BR)
    E.selo(c, 1650, 560, 150, True)


CAPAS = (("capa_A_acao_e_reacao_se_anulam", a), ("capa_B_terceira_lei_acao_e_reacao", b), ("capa_C_troque_os_nomes", d))


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in CAPAS:
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
