"""Capas da QUI-SOL-010 (1280x720). Uso: python capa.py"""
import importlib.util, subprocess, sys
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
_s = importlib.util.spec_from_file_location("v", Path(__file__).parents[1] / "roteiro" / "visual.py")
V = importlib.util.module_from_spec(_s); _s.loader.exec_module(V)
E.usar("Química")


def escuro(c):
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Química", COR)


def salvar(capas):
    pasta = Path(__file__).parent
    s = skia.Surface(E.W, E.H)
    for nome, fn in capas:
        fn(s.getCanvas())
        tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
        tmp.unlink()


def a(c):  # o gancho: o sal tira a água dos micróbios
    E.capa_base(c, COR); E.capa_rotulo(c, "Química", COR)
    E.escreve(c, "o sal não", 84, 380, 140, "i", BR)
    E.escreve(c, "envenena:", 84, 540, 140, "i", BR)
    E.escreve(c, "tira a água", 84, 760, 180, "g", AMARELO)
    V.carne(c, 1450, 500, 560, 300)
    V.micro(c, 1450, 850, 90, 0.6)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Química", "Osmose", "do zero", "e pressão osmótica")


def d(c):  # o macete: a água corre atrás do soluto
    escuro(c)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "o macete da osmose", 84, 330, 100, "i", BR)
    E.escreve(c, "a água corre", 84, 560, 140, "g", BR)
    E.escreve(c, "atrás do soluto", 84, 740, 140, "g", claro)
    V.tubo_u(c, 0.0, 1280, 300, 520, 560, 0.35, 0.75, 0, 9)


salvar((("capa_A_tira_a_agua", a), ("capa_B_osmose", b), ("capa_C_agua_corre_atras", d)))
