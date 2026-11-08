"""Capas do MAT-LEI-004 (1280x720). Uso: python capa.py"""
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


def coracao(c, cx, cy, s, cor):
    p = skia.Path()
    p.moveTo(cx, cy + 0.62 * s)
    p.cubicTo(cx - 1.25 * s, cy - 0.15 * s, cx - 0.62 * s, cy - 1.05 * s, cx, cy - 0.45 * s)
    p.cubicTo(cx + 0.62 * s, cy - 1.05 * s, cx + 1.25 * s, cy - 0.15 * s, cx, cy + 0.62 * s)
    p.close()
    c.drawPath(p, M.paint(cor))


def a(c):  # o gancho: quantas vezes o coração bate em 70 anos
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    coracao(c, 1530, 560, 330, "#E5484D")
    E.escreve(c, "seu coração", 84, 380, 130, "i", BR)
    E.escreve(c, "já bateu", 84, 560, 170, "g", BR)
    E.escreve(c, "quantas vezes?", 84, 730, 150, "g", AMARELO)
    E.escreve(c, "≈ 2,5 bilhões", 84, 930, 130, "g", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Estimar", "sem conta", "comprida")


def d(c):  # o atalho: um sobe, o outro desce
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "um sobe,", 84, 360, 170, "g", BR)
    E.escreve(c, "o outro desce", 84, 560, 170, "g", BR)
    E.escreve(c, "48 × 21", 84, 830, 130, "g", E.mix(COR, BR, 0.55))
    E.escreve(c, "≈ 50 × 20 = 1.000", 620, 830, 130, "g", AMARELO)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_coracao_bateu", a), ("capa_B_estimar_sem_conta", b), ("capa_C_um_sobe_outro_desce", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
