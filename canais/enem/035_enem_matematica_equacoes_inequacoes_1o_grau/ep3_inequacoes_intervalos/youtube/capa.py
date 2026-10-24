"""Capas — Equações e Inequações do 1º Grau, Episódio 3: inequações, intervalos e resposta inteira (tema claro). 3 variações
em 1280x720. A = a reta no espelho com "2 < 5 → −2 ? −5" e a faixa "O SINAL VIRA?"; B = duelo de colchetes ]2, 5] × [2, 5] com
"QUAL É O CERTO?"; C = a reta de 798 a 803 com "n > 800" e "800 ou 801?". Nenhuma mostra a resposta."""
import importlib.util, subprocess, sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(next(d / "_ferramentas" for d in HERE.parents if (d / "_ferramentas").is_dir())))
import skia
import motor
motor.set_theme("claro")
from motor import *  # noqa

_spec = importlib.util.spec_from_file_location("visual_ep3", HERE.parent / "roteiro" / "visual.py")
V = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(V)
motor.set_theme("claro")


def fit(s, size, maxw, peso="black"):
    while text_w(s, peso, size) > maxw:
        size -= 4
    return size


def selo_topo(c, cx=None):
    s = "MATEMÁTICA ENEM · INEQUAÇÕES · EP. 3"
    if cx is None:
        pill(c, s, 84, 90, BLUE, size=34, bounds=(0, 1920))
    else:
        pill(c, s, cx, 90, BLUE, size=34, anchor="center", bounds=(0, 1920))


def capa_espelho(c):
    background(c); selo_topo(c, W / 2)
    shadow_rrect(c, 120, 170, 1680, 560, 40, 1, 1.4)
    rrect(c, 120, 170, 1680, 560, 40, "#FFFFFF")
    V.linha(c, [("2", BLUE), ("  <  ", INK), ("5", PURPLE)], 560, 330, 150, 1.0)
    arrow(c, 820, 330, 1000, 330, AMBER, 1.0, 10, 30)
    V.linha(c, [("−2", BLUE), ("  ?  ", AMBER), ("−5", PURPLE)], 1380, 330, 150, 1.0)
    X = V.reta_n(c, 300, 1620, 590, -6, 6, 1.0, size=34)
    line(c, X(0), 460, X(0), 640, PURPLE, 1.0, 5, dash=(16, 12))
    for v, col in ((-2, BLUE), (-5, PURPLE)):
        c.drawCircle(X(v), 590, 26, paint(col))
    rrect(c, 0, 790, W, 290, 0, AMBER)
    s = "O SINAL VIRA?"
    text(c, s, W / 2, 985, fit(s, 190, 1780), "black", "#FFFFFF")


def capa_colchetes(c):
    background(c); selo_topo(c)
    s = "QUAL É O CERTO?"
    text(c, s, 84, 300, fit(s, 130, 1100), "black", INK, align="left")
    for k, (itv, col) in enumerate((("]2, 5]", INK), ("[2, 5]", INK))):
        x = 120 + k * 560
        shadow_rrect(c, x, 400, 500, 420, 36, 1, 1.4)
        rrect(c, x, 400, 500, 420, 36, "#FFFFFF")
        V.fmid(c, itv, x + 250, 560, 130, "black", col, 1.0)
        X = V.reta_n(c, x + 60, x + 440, 730, 1, 6, 1.0, rot={2, 5}, size=26)
        V.faixa(c, X(2), X(5), 730, 1.0, col)
        V.bola(c, X(2), 730, 1.0, k == 0, col, 14)
        V.bola(c, X(5), 730, 1.0, False, col, 14)
    sz = 110
    shadow_rrect(c, 1280, 400, 540, 420, 36, 1, 1.4)
    rrect(c, 1280, 400, 540, 420, 36, PURPLE)
    V.fmid(c, "2 < x ≤ 5", 1550, 560, sz, "black", "#FFFFFF", 1.0)
    text(c, "bolinha aberta", 1550, 700, 46, "black", "#FFFFFF")
    text(c, "ou fechada?", 1550, 760, 46, "black", "#FFFFFF")


def capa_inteiro(c):
    background(c); selo_topo(c, W / 2)
    V.fmid(c, "n > 800", W / 2, 300, 170, "black", INK, 1.0)
    shadow_rrect(c, 160, 420, 1600, 260, 40, 1, 1.4)
    rrect(c, 160, 420, 1600, 260, 40, "#FFFFFF")
    X = V.reta_n(c, 300, 1600, 560, 798, 803, 1.0, size=40)
    for v in (800, 801):
        c.drawCircle(X(v), 560, 34, paint(AMBER))
        text_mid(c, "?", X(v), 560, 44, "black", "#FFFFFF")
    for k, (s, col) in enumerate((("800", BLUE), ("801", PURPLE))):
        x = 560 + k * 800
        shadow_rrect(c, x - 280, 740, 560, 230, 36, 1, 1.4)
        rrect(c, x - 280, 740, 560, 230, 36, col)
        text_mid(c, s, x, 855, 170, "black", "#FFFFFF")
    text_mid(c, "OU", W / 2, 855, 90, "black", INK)


if __name__ == "__main__":
    for nome, fn in (("capa_A_o_sinal_vira", capa_espelho), ("capa_B_qual_colchete", capa_colchetes),
                     ("capa_C_800_ou_801", capa_inteiro)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
