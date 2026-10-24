"""Capas — Equações e Inequações do 1º Grau, Episódio 5: Revisão (tema claro). 3 variações em 1280x720.
Formatos: A = a ETIQUETA gigante "x = ?" pendurada, com "9 pegadinhas · 5 questões" (a etiqueta do x da série);
B = duas cartas V e F viradas, com a frase "n > 800 → 800?" no meio; C = a corrida dos dois planos na pista, com as
placas de preço e "QUAL COMPENSA?". Nenhuma mostra gabarito."""
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
K = V.K


def fit(s, size, maxw, peso="black"):
    while text_w(s, peso, size) > maxw:
        size -= 4
    return size


def selo_topo(c, cx=None):
    s = "MATEMÁTICA ENEM · 1º GRAU · REVISÃO"
    if cx is None:
        pill(c, s, 84, 90, BLUE, size=34, bounds=(0, 1920))
    else:
        pill(c, s, cx, 90, BLUE, size=34, anchor="center", bounds=(0, 1920))


def capa_etiqueta(c):
    background(c)
    rrect(c, W * 0.52, 0, W * 0.48, H, 0, mix("#FFFFFF", AMBER, 0.18))
    selo_topo(c)
    s1, s2 = "O x NÃO É", "A RESPOSTA?"
    text(c, s1, 520, 400, fit(s1, 150, 900), "black", INK, align="center")
    text(c, s2, 520, 560, fit(s2, 150, 900), "black", RED, align="center")
    text(c, "9 pegadinhas · 5 questões", 520, 720, 64, "black", INK2, align="center")
    # a etiqueta pendurada
    line(c, 1460, 0, 1460, 250, INK2, 1, 6)
    c.save(); c.translate(1460, 560); c.rotate(-8)
    rrect(c, -330, -300, 660, 600, 50, mix("#FFFFFF", AMBER, 0.45), 1, shadow=True)
    c.drawCircle(0, -230, 30, paint("#FFFFFF", 1)); c.drawCircle(0, -230, 30, paint(INK2, 1, stroke=6))
    V.mx(c, "x = ?", 0, 40, 220, INK, 1.0, align="center")
    text_mid(c, "o que a letra significa?", 0, 210, 46, "black", INK2, 1)
    c.restore()


def capa_cartas(c):
    background(c); selo_topo(c, W / 2)
    for x, s, col, ang in ((420, "V", GREEN, -8), (1500, "F", RED, 8)):
        c.save(); c.translate(x, 560); c.rotate(ang)
        rrect(c, -230, -320, 460, 640, 40, "#FFFFFF", 1, shadow=True)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(-230, -320, 460, 640), 40, 40), paint(col, 1, stroke=14))
        text_mid(c, s, 0, 0, 380, "black", col, 1)
        c.restore()
    rrect(c, 640, 330, 640, 300, 30, INK, 1, shadow=True)
    V.mx(c, "n > 800", W / 2, 420, 110, "#FFFFFF", 1.0, align="center")
    text_mid(c, "→ 800 ?", W / 2, 560, 100, "black", AMBER, 1)
    s = "VOCÊ CAI NESTA?"
    text(c, s, W / 2, 1000, fit(s, 130, 1700), "black", INK)


def capa_corrida(c):
    background(c); selo_topo(c)
    s = "QUAL PLANO COMPENSA?"
    text(c, s, W / 2, 300, fit(s, 140, 1760), "black", INK)
    rrect(c, 120, 420, 1680, 520, 40, mix("#FFFFFF", INK2, 0.14), 1)
    line(c, 160, 680, 1760, 680, "#FFFFFF", 1, 10)
    line(c, 1720, 420, 1720, 940, AMBER, 1, 10)
    text_mid(c, "EMPATE?", 1640, 395, 54, "black", AMBER, 1)
    V.carrinho(c, 820, 590, BLUE, 1, 3.0)
    V.carrinho(c, 560, 860, GREEN, 1, 3.0)
    for x, y, s, col in ((820, 560, "A: R$ 80 + R$ 0,50/km", BLUE), (560, 830, "B: R$ 50 + R$ 0,80/km", GREEN)):
        sz = 46
        w = text_w(s, "black", sz) + 50
        rrect(c, x - w / 2 + 480, y - 40, w, 80, 18, col, 1, shadow=True)
        text_mid(c, s, x + 480, y, sz, "black", "#FFFFFF", 1)


if __name__ == "__main__":
    for nome, fn in (("capa_A_o_x_nao_e_a_resposta", capa_etiqueta), ("capa_B_voce_cai_nesta", capa_cartas),
                     ("capa_C_qual_plano_compensa", capa_corrida)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
