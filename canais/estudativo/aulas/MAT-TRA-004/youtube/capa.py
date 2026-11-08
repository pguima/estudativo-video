"""Capas do MAT-TRA-004 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: a expressão que vira só sen x
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.formula(c, "f{1 − cos^2 x}{sen x}", 84, 520, 210, "g", BR)
    E.escreve(c, "=", 860, 560, 200, "g", BR)
    E.escreve(c, "sen x", 1060, 560, 220, "g", AMARELO)
    E.escreve(c, "simplifique em 2 passos", 84, 920, 110, "i", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Secante e", "identidades", "sem decorar")


def d(c):  # o macete: o "co" uma vez em cada dupla
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "o “co” aparece uma vez", 84, 340, 110, "i", BR)
    E.formula(c, "sec = f{1}{cos}", 84, 620, 150, "g", AMARELO)
    E.formula(c, "cossec = f{1}{sen}", 84, 900, 150, "g", BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_vira_seno", a), ("capa_B_secante_identidades", b), ("capa_C_macete_do_co", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
