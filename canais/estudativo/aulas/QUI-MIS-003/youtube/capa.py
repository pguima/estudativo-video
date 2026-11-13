"""Capas da QUI-MIS-003 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: a fumaça branca não é vapor
    E.capa_base(c, COR); E.capa_rotulo(c, "Química", COR)
    E.escreve(c, "a fumaça branca", 84, 360, 120, "i", BR)
    E.escreve(c, "é vapor?", 84, 560, 190, "g", BR)
    E.risco(c, 70, 590, 830, 420, 10, 0, AMARELO, 30)
    E.escreve(c, "é líquido", 84, 800, 190, "g", AMARELO)
    E.escreve(c, "as 6 mudanças de estado", 84, 990, 80, "i", BR)
    V.chaleira(c, 1240, 820, 170, 1.0, 2.2)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Química", "Estados", "físicos", "do zero")


def d(c):  # o macete: a escada
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Química", COR)
    E.escreve(c, "absorve ou libera?", 84, 330, 110, "i", BR)
    E.escreve(c, "a escada", 76, 530, 200, "g", BR)
    E.escreve(c, "subir = absorve", 84, 740, 90, "g", "#F5A04A")
    E.escreve(c, "descer = libera", 84, 870, 90, "g", "#6FA8FF")
    for k, (nome, y) in enumerate((("sólido", 900), ("líquido", 700), ("gás", 500))):
        x0 = 1080 + k * 250
        M.rrect(c, x0, y, 250, 1000 - y, 16, "#1B1C26", 1)
        c.drawRect(skia.Rect.MakeXYWH(x0, y, 250, 10), M.paint(E.CLARO, 1))
        E.centro(c, nome, x0 + 125, y + 80, 50, "g", BR, 1)
    M.arrow(c, 1150, 860, 1700, 460, V.QUENTE, 1, 12, 40)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_fumaca_branca_e_liquido", a), ("capa_B_estados_fisicos", b), ("capa_C_a_escada", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
