"""Capas da QUI-MIS-002 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: água mineral é pura? É mistura
    E.capa_base(c, COR); E.capa_rotulo(c, "Química", COR)
    E.escreve(c, "água mineral", 84, 360, 130, "i", BR)
    E.escreve(c, "é pura?", 84, 560, 190, "g", BR)
    E.risco(c, 70, 590, 760, 420, 10, 0, AMARELO, 30)
    E.escreve(c, "é mistura", 84, 800, 190, "g", AMARELO)
    E.escreve(c, "o que a Química chama de puro", 84, 990, 80, "i", BR)
    V.garrafa(c, 1560, 960, 360, 800, 1.0, 0.78, ("água mineral", "natural"))


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Química", "Substância", "ou mistura", "do zero")


def d(c):  # o macete: duas perguntas
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Química", COR)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "classifique tudo com", 84, 330, 110, "i", BR)
    E.escreve(c, "2 perguntas", 76, 530, 190, "g", BR)
    for k, s in enumerate(("1. uma fórmula só?", "2. vê partes diferentes?")):
        E.escreve(c, s, 84, 720 + 130 * k, 84, "b", claro)
    for k, (m, x, y, g) in enumerate((("O2", 1380, 300, 10), ("O3", 1680, 560, 0), ("H2O", 1380, 800, 0))):
        Q.molecula_desenho(c, m, x, y, 120, 1, giro=g, escuro=True)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_agua_mineral_e_mistura", a), ("capa_B_substancia_ou_mistura", b), ("capa_C_duas_perguntas", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
