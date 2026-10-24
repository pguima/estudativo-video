"""Capas — Juros Compostos, Episódio 2: simples × compostos (tema claro). 3 variações em 1280x720.
Formatos: A = gráfico ocupando a capa inteira (reta × curva) com uma LUPA no cruzamento e a pergunta no alto à esquerda;
B = linha do tempo de pilhas de notas que dobram (1, 2, 4, ?) com a pergunta em faixa escura embaixo;
C = duas escadas gigantes lado a lado (degraus iguais × degraus que crescem), título central no alto.
Nenhuma mostra a resposta."""
import importlib.util, subprocess, sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(next(d / "_ferramentas" for d in HERE.parents if (d / "_ferramentas").is_dir())))
import skia
import motor
motor.set_theme("claro")
from motor import *  # noqa

_spec = importlib.util.spec_from_file_location("visual_ep2", HERE.parent / "roteiro" / "visual.py")
V = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(V)
motor.set_theme("claro")


def fit(s, size, maxw, peso="black"):
    while text_w(s, peso, size) > maxw:
        size -= 4
    return size


def selo_topo(c, cx=None, y=90):
    s = "MATEMÁTICA ENEM · JUROS COMPOSTOS · EP. 2"
    if cx is None:
        pill(c, s, 84, y, PURPLE, size=34, bounds=(0, 1920))
    else:
        pill(c, s, cx, y, PURPLE, size=34, anchor="center", bounds=(0, 1920))


def capa_lupa(c):
    background(c); selo_topo(c)
    text(c, "JUROS COMPOSTOS:", 84, 270, 92, "black", INK, align="left")
    text(c, "SEMPRE MAIS CAROS?", 84, 380, 92, "black", PURPLE, align="left")
    g = V.Graf(160, 470, 1400, 470, 0, 3, 98, 136)
    line(c, g.x, g.y + g.h, g.x + g.w + 40, g.y + g.h, INK2, 1.0, 5)
    line(c, g.x, g.y + g.h, g.x, g.y - 20, INK2, 1.0, 5)
    V.reta_s(c, g, 100, 0.10, 0, 3, 1.0, 1.0, 12)
    V.curva_c(c, g, 100, 0.10, 0, 3, 1.0, 1.0, 12)
    text(c, "simples", 1590, 610, 54, "black", BLUE, align="left")
    text(c, "compostos", 1590, 480, 54, "black", PURPLE, align="left")
    # lupa no começo
    x, y = g.P(0.55, 105)
    c.drawCircle(x, y, 120, paint("#FFFFFF", 0.55))
    c.drawCircle(x, y, 120, paint(AMBER, 1.0, stroke=14))
    line(c, x + 85, y + 85, x + 170, y + 170, AMBER, 1.0, 22)
    V.selo(c, 1200, 820, 1.0, "E EM 15 DIAS?", RED, -5, 60)


def capa_pilhas(c):
    background(c); selo_topo(c, W / 2)
    s = "DOBRA A CADA 7 ANOS"
    text(c, s, W / 2, 260, fit(s, 130, 1780), "black", INK)
    base = 820
    line(c, 120, base + 14, 1800, base + 14, INK2, 1.0, 6)
    for k, (rot, n) in enumerate((("hoje", 1), ("7 anos", 2), ("14 anos", 4))):
        cx = 300 + k * 450
        por = min(n, 4)
        for j in range(n):
            x = cx + (j % 4 - (por - 1) / 2) * 104
            V.pilha(c, x, base, 1.0, 6, 92, 22)
        text(c, rot, cx, base + 90, 48, "black", GRAY)
    text(c, "21 anos", 1650, base + 90, 48, "black", AMBER)
    text_mid(c, "?", 1650, 620, 300, "black", AMBER)
    rrect(c, 0, 920, 1920, 160, 0, INK, 1.0)
    s2 = "VEZES 3? NÃO É TÃO SIMPLES."
    text_mid(c, s2, W / 2, 1000, fit(s2, 80, 1760), "black", "#FFFFFF")


def capa_escadas(c):
    background(c); selo_topo(c, W / 2)
    s = "SOMA OU MULTIPLICA?"
    text(c, s, W / 2, 270, fit(s, 140, 1780), "black", INK)
    for k, (nome, col, fator, x0) in enumerate((("SIMPLES", BLUE, 1.0, 140), ("COMPOSTOS", PURPLE, 1.1, 1000))):
        yy, hh = 1000, 90
        for j in range(5):
            rrect(c, x0 + j * 150, yy - hh, 140, hh, 10, col, 0.9)
            yy -= hh
            hh *= fator
        text(c, nome, x0 + 370, 400, 64, "black", col)
    text(c, "+ 10", 600, 560, 70, "black", BLUE)
    text(c, "× 1,1", 1220, 520, 70, "black", PURPLE)


if __name__ == "__main__":
    for nome, fn in (("capa_A_sempre_mais_caros", capa_lupa), ("capa_B_dobra_7_anos", capa_pilhas),
                     ("capa_C_soma_ou_multiplica", capa_escadas)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
