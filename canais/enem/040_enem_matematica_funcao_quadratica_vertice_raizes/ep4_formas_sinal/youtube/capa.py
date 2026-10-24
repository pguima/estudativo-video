"""Capas — Função Quadrática, Episódio 4: três formas da mesma função e estudo do sinal (tema claro). 3 variações em 1280x720.
A = "x² > 4x" gigante com a divisão por x riscada e "x > 4?" em âmbar: "DIVIDIU POR x?" (sem dar a solução certa);
B = as três "fotos" da mesma parábola (geral, fatorada, canônica) com câmeras: "3 FOTOS DA MESMA PARÁBOLA";
C = a parábola sorrindo sobre o eixo, com "?" entre as raízes e "+ ou −?" no meio: "ENTRE AS RAÍZES: + OU −?".
Nenhuma mostra gabarito (x < 0 ou x > 4, a regra do sinal e as respostas das questões não aparecem)."""
import importlib.util, subprocess, sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(next(d / "_ferramentas" for d in HERE.parents if (d / "_ferramentas").is_dir())))
import skia
import motor
motor.set_theme("claro")
from motor import *  # noqa

_spec = importlib.util.spec_from_file_location("visual_ep4", HERE.parent / "roteiro" / "visual.py")
V = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(V)
motor.set_theme("claro")


def fit(s, size, maxw, peso="black"):
    while text_w(s, peso, size) > maxw:
        size -= 4
    return size


def selo_topo(c, cx=None):
    s = "MATEMÁTICA ENEM · FUNÇÃO QUADRÁTICA · EP. 4"
    if cx is None:
        pill(c, s, 84, 90, BLUE, size=34, bounds=(0, 1920))
    else:
        pill(c, s, cx, 90, BLUE, size=34, anchor="center", bounds=(0, 1920))


def capa_divide(c):
    background(c); selo_topo(c)
    shadow_rrect(c, 70, 190, 1050, 800, 40, 1, 1.4)
    rrect(c, 70, 190, 1050, 800, 40, "#FFFFFF")
    V.linha(c, [("x² > 4x", INK)], 595, 380, 210, 1.0)
    rrect(c, 250, 520, 690, 110, 30, AMBER)
    text_mid(c, "dividiu por x", 595, 575, 72, "black", "#FFFFFF")
    V.linha(c, [("x > 4 ?", AMBER)], 595, 800, 190, 1.0)
    s1, s2 = "PERDEU", "METADE?"
    text(c, s1, 1520, 470, fit(s1, 190, 700), "black", INK)
    sz = fit(s2, 170, 700)
    w = text_w(s2, "black", sz) + 70
    shadow_rrect(c, 1520 - w / 2, 540, w, 210, 30, 1, 1.4)
    rrect(c, 1520 - w / 2, 540, w, 210, 30, RED)
    text_mid(c, s2, 1520, 645, sz, "black", "#FFFFFF")
    V.selo(c, 1520, 890, 1.0, "NUNCA DIVIDA POR x", RED, -5, 56)


def capa_fotos(c):
    background(c); selo_topo(c, W / 2)
    s = "3 FOTOS DA MESMA PARÁBOLA"
    text(c, s, W / 2, 300, fit(s, 140, 1800), "black", INK)
    fotos = [("GERAL", "2x² − 8x + 6", "o c", BLUE), ("FATORADA", "2(x − 1)(x − 3)", "as raízes", PURPLE),
             ("CANÔNICA", "2(x − 2)² − 2", "o vértice", V.TEAL)]
    for k, (tit, lei, mostra, col) in enumerate(fotos):
        x = 340 + k * 620
        shadow_rrect(c, x - 290, 390, 580, 520, 40, 1, 1.4)
        rrect(c, x - 290, 390, 580, 520, 40, "#FFFFFF")
        rrect(c, x - 290, 390, 580, 120, 40, col, 0.92)
        text_mid(c, tit, x, 450, 64, "black", "#FFFFFF")
        V.camera(c, x, 600, 120, col, 1.0)
        V.ftext(c, lei, x, 780, fit(lei, 66, 520), "black", INK)
        text(c, "mostra " + mostra, x, 870, 46, "extrabold", col)
    rrect(c, 0, 960, W, 120, 0, PURPLE)
    text_mid(c, "qual usar em cada pergunta?", W / 2, 1020, 64, "black", "#FFFFFF")


def capa_sinal(c):
    background(c); selo_topo(c, W / 2)
    s = "ENTRE AS RAÍZES:"
    text(c, s, W / 2, 290, fit(s, 150, 1700), "black", INK)
    g = V.Graf(360, 380, 1200, 500, -0.8, 4.8, -2.2, 6)
    f = lambda x: x * x - 4 * x + 3
    line(c, 300, g.P(0, 0)[1], 1620, g.P(0, 0)[1], INK2, 1, 8)
    g.curva(c, f, 1.0, BLUE, 1.0, 14, xa=-0.6, xb=4.6)
    for r_ in (1, 3):
        g.ponto(c, r_, 0, 1.0, INK, 24)
    px, py = g.P(2, -0.4)
    c.drawCircle(px, py - 190, 150, paint(AMBER, 1))
    text_mid(c, "+ ou −?", px, py - 190, 62, "black", "#FFFFFF")
    rrect(c, 0, 960, W, 120, 0, GREEN)
    text_mid(c, "a regra que cabe numa frase", W / 2, 1020, 64, "black", "#FFFFFF")


if __name__ == "__main__":
    for nome, fn in (("capa_A_perdeu_metade", capa_divide), ("capa_B_tres_fotos", capa_fotos),
                     ("capa_C_entre_as_raizes", capa_sinal)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
