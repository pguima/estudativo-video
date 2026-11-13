"""Capas da QUI-SOL-008 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: 88 °C na montanha
    E.capa_base(c, COR); E.capa_rotulo(c, "Química", COR)
    E.escreve(c, "a água ferve", 84, 380, 130, "i", BR)
    E.escreve(c, "a 88 °C?", 84, 600, 220, "g", AMARELO)
    E.escreve(c, "na montanha, sim", 84, 800, 110, "i", BR)
    V.montanha(c, 1150, 1000, 700, 640)
    V.panela(c, 2.0, 1500, 980, 260, 130, ferve=0.0)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Química", "Pressão", "de vapor", "do zero")


def d(c):  # o macete: o que mudou?
    escuro(c)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "uma pergunta resolve", 84, 330, 100, "i", BR)
    E.escreve(c, "o que", 84, 560, 200, "g", BR)
    E.escreve(c, "mudou?", 84, 760, 200, "g", claro)
    V.duelo(c, 10, 0, 1380, 900, 520, 1.0, 1.0, escuro=True, size=44)


salvar((("capa_A_88_graus", a), ("capa_B_pressao_de_vapor", b), ("capa_C_o_que_mudou", d)))
