"""Capas do MAT-TRA-007 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: senos ou cossenos? 5 questões
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "5 questões", 84, 400, 170, "g", BR)
    E.escreve(c, "de trigonometria", 84, 560, 110, "i", BR)
    E.escreve(c, "senos ou cossenos?", 84, 780, 130, "g", AMARELO)
    E.escreve(c, "pause e resolva", 84, 940, 90, "i", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Exercícios", "leis e ciclo", "pause e resolva")


def d(c):  # o resumo: as ferramentas
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "tem par completo?", 84, 360, 120, "i", BR)
    E.escreve(c, "sim: senos", 84, 600, 160, "g", AMARELO)
    E.escreve(c, "não: cossenos", 84, 840, 160, "g", BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_cinco_questoes", a), ("capa_B_exercicios", b), ("capa_C_par_completo", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
