"""Capas da QUI-AMB-002 (1280x720). Uso: python capa.py"""
import importlib.util
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
_s = importlib.util.spec_from_file_location("visual_aula", Path(__file__).parents[1] / "roteiro" / "visual.py")
V = importlib.util.module_from_spec(_s); _s.loader.exec_module(V)


def a(c):  # o gancho: toda chuva é ácida
    E.capa_base(c, COR); E.capa_rotulo(c, "Química", COR)
    E.escreve(c, "toda chuva", 84, 360, 150, "g", BR)
    E.escreve(c, "é ácida", 84, 560, 190, "g", AMARELO)
    E.escreve(c, "até a limpa: pH 5,6", 84, 740, 100, "b", BR)
    E.escreve(c, "então, o que é chuva ácida?", 84, 960, 80, "i", BR)
    V.estatua(c, 1500, 980, 300, 0.5)
    V.chuva(c, 0, 1200, 1800, 80, 900, 1, 18, "#FFFFFF")


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Química", "Chuva", "ácida", "do zero")


def d(c):  # o macete: some a água à fórmula
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Química", COR)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "o ácido do óxido:", 84, 330, 110, "i", BR)
    E.escreve(c, "some a água", 76, 530, 170, "g", BR)
    Q.formula(c, "SO3 + H2O", 84, 780, 150, BR, escuro=True, cores={"H2O": claro})
    Q.formula(c, "-> H2SO4", 900, 780, 150, BR, escuro=True, cores={"H2SO4": claro})
    E.escreve(c, "chuva ácida em 1 passo", 84, 960, 80, "i", BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_toda_chuva_e_acida", a), ("capa_B_chuva_acida", b), ("capa_C_some_a_agua", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
