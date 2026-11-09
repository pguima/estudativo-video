"""Capas do FIS-DIN-001 (1280x720). Uso: python capa.py"""
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


def fr(c, x, y, size, cor):  # F com o R subscrito
    E.escreve(c, "F", x, y, size, "g", cor)
    E.escreve(c, "R", x + E.larg("F", "g", size) + 4, y + size * 0.2, size * 0.6, "g", cor)
    return E.larg("F", "g", size) + E.larg("R", "g", size * 0.6) + 10


def a(c):  # o gancho: o ônibus freia e ninguém te empurrou
    E.capa_base(c, COR); E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "Ninguém", 84, 420, 200, "g", BR)
    E.escreve(c, "te empurrou", 84, 620, 170, "g", BR)
    E.escreve(c, "o ônibus é que freou", 84, 820, 96, "i", BR)
    F.seta(c, 1250, 520, 1750, 520, AMARELO, 1.0, 34, cabeca=110)
    E.escreve(c, "inércia", 1300, 680, 120, "i", AMARELO)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Física", "Inércia", "e força", "resultante")


def d(c):  # o macete: velocidade constante = resultante zero
    palco(c)
    E.escreve(c, "velocidade constante?", 84, 360, 120, "i", BR)
    w = fr(c, 120, 660, 300, BR)
    E.escreve(c, "= 0", 120 + w + 20, 660, 300, "g", BR)
    E.escreve(c, "e as forças empatam", 84, 900, 110, "i", E.mix(COR, BR, 0.5))
    E.selo(c, 1650, 560, 150, True)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_ninguem_te_empurrou", a), ("capa_B_inercia_e_forca_resultante", b), ("capa_C_resultante_zero", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
