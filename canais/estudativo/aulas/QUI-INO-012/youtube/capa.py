"""Capas da QUI-INO-012 (1280x720). Uso: python capa.py"""
import subprocess, sys
from pathlib import Path
RAIZ = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(RAIZ / "_ferramentas"))
import skia
import editorial as E
import quimica as Q
import motor as M
BR = "#FFFFFF"
AMARELO = "#FFD500"
COR = E.MATERIAS["Química"]["cor"]
E.usar("Química")


def palco_capa(c):
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Química", COR)




def a(c):  # o gancho: o desafio do butano
    E.capa_base(c, COR); E.capa_rotulo(c, "Química", COR)
    Q.formula(c, "C4H10 + O2 -> CO2 + H2O", 84, 420, 110, BR)
    E.escreve(c, "soma = ?", 84, 640, 160, "g", AMARELO)
    E.escreve(c, "5 questões de reações", 84, 860, 90, "i", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Química", "Praticando", "reações", "5 questões")


def d(c):  # o macete: dobre quem deu ímpar
    palco_capa(c)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "oxigênio ímpar?", 84, 340, 110, "i", BR)
    E.escreve(c, "dobre quem", 84, 560, 150, "g", BR)
    E.escreve(c, "deu ímpar", 84, 740, 150, "g", claro)
    Q.formula(c, "2 C4H10 + 13 O2 -> 8 CO2 + 10 H2O", 84, 960, 80, BR, escuro=True, cores={"coef": claro})


CAPAS = (("capa_A_desafio_do_butano", a), ("capa_B_praticando_reacoes", b), ("capa_C_dobre_o_impar", d))


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in CAPAS:
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
