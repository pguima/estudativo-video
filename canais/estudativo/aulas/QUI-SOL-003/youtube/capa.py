"""Capas da QUI-SOL-003 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: 0,9% = 9 g por litro
    E.capa_base(c, COR); E.capa_rotulo(c, "Química", COR)
    E.escreve(c, "0,9%", 84, 470, 260, "g", BR)
    E.escreve(c, "quantos gramas", 84, 650, 100, "i", BR)
    E.escreve(c, "por litro?", 84, 770, 100, "i", BR)
    E.escreve(c, "9 g", 84, 990, 200, "g", AMARELO)
    V.soro(c, 1450, 560, 460, 640, "0,9%")


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Química", "g/L, %", "e ppm", "do zero")


def d(c):  # o macete: % × 10
    escuro(c)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "o macete do rótulo", 84, 330, 100, "i", BR)
    E.formula(c, "% × 10", 84, 560, 220, "g", BR)
    E.formula(c, "= g/L", 84, 790, 220, "g", claro)
    E.formula(c, "0,9% → 9 g/L", 84, 960, 90, "g", BR)
    V.soro(c, 1530, 560, 380, 540, "0,9%")


salvar((("capa_A_09_por_cento", a), ("capa_B_gl_porcentagem_ppm", b), ("capa_C_vezes_dez", d)))
