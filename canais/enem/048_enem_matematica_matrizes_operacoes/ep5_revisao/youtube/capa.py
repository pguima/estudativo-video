"""Capas — Matrizes, Episódio 5: Revisão (tema claro). 3 variações em 1280x720.
Formatos (sem repetir as revisões anteriores): A = os 4 disfarces (jogos, distâncias, compras, foto) em volta de uma
lupa sobre a matriz, "ACHE A MATRIZ"; B = fundo escuro com duas pegadinhas em cartas ("a₂₃ = linha 3?" e "3 · A só na
1ª linha?") e o selo "V OU F?"; C = o código secreto: a mensagem (7, 18) entrando no cadeado e "? ?" saindo,
"DECIFRE O CÓDIGO". Nenhuma mostra gabarito.
"""
import importlib.util, subprocess, sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(next(d / "_ferramentas" for d in HERE.parents if (d / "_ferramentas").is_dir())))
import skia
import motor
motor.set_theme("claro")
from motor import *  # noqa

_spec = importlib.util.spec_from_file_location("visual_ep5", HERE.parent / "roteiro" / "visual.py")
V = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(V)
motor.set_theme("claro")


def fit(s, size, maxw, peso="black"):
    while V.ftw(s, size, peso) > maxw:
        size -= 4
    return size


def selo_topo(c, cx=None, cor=BLUE):
    s = "MATEMÁTICA ENEM · MATRIZES · REVISÃO"
    if cx is None:
        pill(c, s, 84, 90, cor, size=34, bounds=(0, 1920))
    else:
        pill(c, s, cx, 90, cor, size=34, anchor="center", bounds=(0, 1920))


def capa_disfarce(c):
    background(c)
    selo_topo(c, W / 2)
    s = "ACHE A MATRIZ"
    text(c, s, W / 2, 290, fit(s, 170, 1760), "black", INK)
    for k, (rot, ic, col) in enumerate((("JOGOS", 6, BLUE), ("DISTÂNCIAS", 4, GREEN), ("COMPRAS", 9, AMBER),
                                         ("FOTO", 1, PURPLE))):
        x = 200 + (k % 2) * 1520
        y = 470 + (k // 2) * 330
        shadow_rrect(c, x - 170, y - 150, 340, 300, 30, 1, 1.3)
        rrect(c, x - 170, y - 150, 340, 300, 30, mix("#FFFFFF", col, 0.14))
        V.area_icone(c, ic, x, y - 20, 0.5, 1)
        V.fit(c, rot, x, y + 120, 40, 300, "black", col, 1, align="center")
    shadow_rrect(c, 560, 360, 800, 600, 50, 1, 1.4)
    rrect(c, 560, 360, 800, 600, 50, "#FFFFFF")
    V.matriz(c, 900, 640, V.M("12 8 15", "10 14 6", "7 11 13"), 1, 150, 110, 66)
    c.drawCircle(1160, 560, 150, paint(mix("#FFFFFF", BLUE, 0.12), 0.6))
    c.drawCircle(1160, 560, 150, paint(BLUE, 1, stroke=22))
    line(c, 1265, 665, 1380, 780, BLUE, 1, 34)
    rrect(c, 360, 985, 1200, 80, 24, PURPLE)
    text_mid(c, "o disfarce que o ENEM usa", W / 2, 1025, 48, "black", "#FFFFFF")


def capa_pegadinhas(c):
    c.drawRect(skia.Rect.MakeWH(W, H), paint("#1E2230", 1))
    selo_topo(c, W / 2, AMBER)
    s = "VOCÊ CAI NESTAS?"
    text(c, s, W / 2, 290, fit(s, 160, 1760), "black", "#FFFFFF")
    for k, (itens, rot) in enumerate(((["a₂₃ = linha 3?"], -4), (["3 ·", V.M("1 2", "0 4"), "=", V.M("3 6", "0 4"), "?"], 3))):
        x = 500 + k * 920
        c.save(); c.translate(x, 640); c.rotate(rot)
        shadow_rrect(c, -400, -230, 800, 460, 40, 1, 1.4)
        rrect(c, -400, -230, 800, 460, 40, "#FFFFFF")
        V.expr(c, itens, 0, -10, 1, 84, 92, 78, maxw=700)
        c.restore()
    V.selo(c, W / 2, 960, 1.0, "V OU F?", AMBER, -4, 70)


def capa_codigo(c):
    background(c)
    selo_topo(c)
    s1 = "DECIFRE O CÓDIGO"
    text(c, s1, 84, 300, fit(s1, 150, 1700), "black", INK, align="left")
    shadow_rrect(c, 84, 380, 1752, 600, 44, 1, 1.4)
    rrect(c, 84, 380, 1752, 600, 44, "#FFFFFF")
    V.matriz(c, 360, 680, V.M("7", "18"), 1, 160, 140, 96)
    text_mid(c, "mensagem", 360, 900, 44, "black", INK2)
    arrow(c, 520, 680, 720, 680, INK2, 1, 12, 34)
    V.icone(c, 3, 960, 660, 1.05, 1)
    arrow(c, 1200, 680, 1400, 680, GREEN, 1, 12, 34)
    V.matriz(c, 1580, 680, [["?"], ["?"]], 1, 160, 140, 110, cores={(0, 0): GREEN, (1, 0): GREEN})
    text_mid(c, "originais", 1580, 900, 44, "black", GREEN)


if __name__ == "__main__":
    for nome, fn in (("capa_A_ache_a_matriz", capa_disfarce), ("capa_B_voce_cai", capa_pegadinhas),
                     ("capa_C_decifre_codigo", capa_codigo)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
