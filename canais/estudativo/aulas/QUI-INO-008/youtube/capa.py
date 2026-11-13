"""Capas da QUI-INO-008 (1280x720). Uso: python capa.py"""
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




def a(c):  # o gancho: a equação desequilibrada
    E.capa_base(c, COR); E.capa_rotulo(c, "Química", COR)
    Q.formula(c, "C3H8 + O2 -> CO2 + H2O", 84, 420, 120, BR)
    E.escreve(c, "3 carbonos → 1?", 84, 640, 140, "g", AMARELO)
    E.escreve(c, "balanceie em 4 passos", 84, 860, 90, "i", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Química", "Balancear", "equações", "por tentativas")


def d(c):  # o macete: MACHO
    palco_capa(c)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "a ordem que não erra", 84, 340, 100, "i", BR)
    E.escreve(c, "MACHO", 84, 620, 260, "g", claro)
    E.escreve(c, "metal, ametal, carbono, hidrogênio, oxigênio", 84, 800, 56, "b", BR)
    Q.formula(c, "C3H8 + 5 O2 -> 3 CO2 + 4 H2O", 84, 990, 90, BR, escuro=True, cores={"coef": claro})


CAPAS = (("capa_A_equacao_desequilibrada", a), ("capa_B_balancear", b), ("capa_C_macho", d))


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in CAPAS:
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
