"""Capas da QUI-INO-003 (1280x720). Uso: python capa.py"""
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




def a(c):  # o gancho: ácido + base = água e sal
    E.capa_base(c, COR); E.capa_rotulo(c, "Química", COR)
    E.escreve(c, "ácido + base", 84, 400, 150, "g", BR)
    E.escreve(c, "= água e sal", 84, 600, 150, "g", AMARELO)
    Q.formula(c, "HCl + NaOH -> NaCl + H2O", 84, 860, 100, BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Química", "Neutralização", "e sais", "do zero")


def d(c):  # o macete: cruze as cargas
    palco_capa(c)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "cruze as cargas", 84, 360, 130, "i", BR)
    Q.formula(c, "Al^3+ + SO4^2-", 84, 600, 150, BR, escuro=True, cores={"carga": claro})
    Q.formula(c, "Al2(SO4)3", 84, 880, 190, BR, escuro=True, cores={"indice": claro})


CAPAS = (("capa_A_acido_mais_base", a), ("capa_B_neutralizacao_e_sais", b), ("capa_C_cruze_as_cargas", d))


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in CAPAS:
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
