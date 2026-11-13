"""Capas da QUI-INO-013 (1280x720). Uso: python capa.py"""
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




def a(c):  # o gancho: base sem OH
    E.capa_base(c, COR); E.capa_rotulo(c, "Química", COR)
    Q.formula(c, "NH3", 84, 440, 220, BR)
    E.escreve(c, "é base sem OH?", 84, 650, 130, "g", AMARELO)
    E.escreve(c, "quem doa e quem recebe H⁺", 84, 860, 80, "g", BR)
    Q.molecula_desenho(c, "NH3", 1480, 480, 190)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Química", "Brønsted", "e Lewis", "do zero")


def d(c):  # o macete: par conjugado = 1 H⁺ de diferença
    palco_capa(c)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "par conjugado", 84, 340, 120, "i", BR)
    E.escreve(c, "= 1 H⁺ de diferença", 84, 520, 120, "g", claro)
    Q.formula(c, "OH^-  H2O  H3O^+", 84, 800, 150, BR, escuro=True)
    E.escreve(c, "−H           +H", 300, 960, 80, "g", claro)


CAPAS = (("capa_A_base_sem_oh", a), ("capa_B_bronsted_e_lewis", b), ("capa_C_par_conjugado", d))


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in CAPAS:
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
