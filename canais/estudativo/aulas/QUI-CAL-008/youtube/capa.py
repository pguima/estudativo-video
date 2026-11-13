"""Capas da QUI-CAL-008 (1280x720). Uso: python capa.py"""
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


def palco(c):
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Química", COR)
def a(c):  # o gancho: deveriam sair 196 g, saem 147 g
    E.capa_base(c, COR); E.capa_rotulo(c, "Química", COR)
    E.escreve(c, "deveriam sair 196 g", 84, 360, 120, "g", BR)
    E.escreve(c, "saem 147 g", 84, 600, 200, "g", AMARELO)
    Q.formula(c, "H2SO4", 84, 820, 150, BR)
    E.escreve(c, "para onde foi o resto?", 84, 990, 90, "i", BR)
    Q.molecula_desenho(c, "H2SO4", 1560, 700, 140)


def b(c):
    E.capa_modelo(c, "Química", "Rendimento", "e etapas", "estequiometria")


def d(c):  # o macete: siga o elemento
    palco(c)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "três reações,", 84, 330, 110, "i", BR)
    E.escreve(c, "uma conta só", 76, 520, 160, "g", BR)
    Q.formula(c, "S → H2SO4", 84, 760, 170, BR, escuro=True, cores={"S": claro})
    E.escreve(c, "siga o enxofre: 1 para 1", 84, 980, 90, "i", claro)


CAPAS = (("capa_A_saem_147g", a), ("capa_B_rendimento", b), ("capa_C_siga_o_elemento", d))


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in CAPAS:
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
