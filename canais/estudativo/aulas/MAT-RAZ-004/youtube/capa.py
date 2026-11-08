"""Capas do MAT-RAZ-004 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: anda junto ou ao contrário?
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "+ quilos", 84, 340, 130, "g", BR)
    E.escreve(c, "+ R$", 760, 340, 130, "g", AMARELO)
    E.escreve(c, "+ velocidade", 84, 560, 130, "g", BR)
    E.escreve(c, "− tempo", 1020, 560, 130, "g", AMARELO)
    E.escreve(c, "qual é proporcional?", 84, 900, 130, "i", BR)


def b(c):  # o modelo
    E.capa_modelo(c, "Matemática", "Direta", "ou inversa?", "grandezas")


def d(c):  # o atalho: direta, divisão
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    cl = E.mix(COR, BR, 0.55)
    E.escreve(c, "o macete do d:", 84, 330, 130, "i", BR)
    E.escreve(c, "direta → divisão", 84, 560, 160, "g", BR)
    E.escreve(c, "inversa → multiplicação", 84, 780, 130, "g", cl)
    for x in (84, 84 + E.larg("direta → ", "g", 160)):
        c.drawCircle(x + E.larg("d", "g", 160) / 2, 560 - 58, 80, M.paint(AMARELO, 1, stroke=10))


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_qual_e_proporcional", a), ("capa_B_direta_ou_inversa", b), ("capa_C_macete_do_d", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
