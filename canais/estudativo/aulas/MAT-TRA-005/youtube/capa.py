"""Capas do MAT-TRA-005 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: sen 75° não é sen 45° + sen 30°
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "sen 75° =", 84, 400, 170, "g", BR)
    E.escreve(c, "sen 45° + sen 30°?", 84, 610, 130, "g", AMARELO)
    E.risco(c, 70, 580, 1220, 540, 9, 0, BR, 14)
    E.formula(c, "= f{r{6} + r{2}}{4}", 84, 880, 150, "g", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Adição de", "arcos", "e arco duplo")


def d(c):  # o macete: a música
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "Minha terra tem palmeiras,", 84, 380, 100, "i", BR)
    E.escreve(c, "onde canta o sabiá", 84, 500, 100, "i", BR)
    E.formula(c, "sen a cos b + sen b cos a", 84, 760, 120, "g", AMARELO)
    E.escreve(c, "o macete do seno da soma", 84, 920, 80, "i", BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_seno_de_75", a), ("capa_B_adicao_de_arcos", b), ("capa_C_musica", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
