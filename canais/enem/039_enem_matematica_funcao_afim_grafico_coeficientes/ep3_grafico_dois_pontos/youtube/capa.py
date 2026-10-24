"""Capas — Função Afim, Episódio 3: o gráfico e a lei a partir de dois pontos (tema claro). 3 variações em 1280x720.
A = os dois gráficos do gancho lado a lado (o da esquerda parece mais íngreme) e "QUAL SOBE MAIS RÁPIDO?";
B = dois pregos segurando uma régua, os pontos (2, 11) e (5, 20) e "f(x) = ?" numa faixa roxa;
C = três retas pelo mesmo ponto (sobe, deita, desce) com "SOBE, DEITA OU DESCE?" e as perguntas a > 0? a = 0? a < 0?.
Nenhuma mostra gabarito (a = 2 e a = 10, f(x) = 3x + 5 não aparecem)."""
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
    s = "MATEMÁTICA ENEM · FUNÇÃO AFIM · EP. 3"
    if cx is None:
        pill(c, s, 84, 90, BLUE, size=34, bounds=(0, 1920))
    else:
        pill(c, s, cx, 90, BLUE, size=34, anchor="center", bounds=(0, 1920))


def capa_olho(c):
    background(c); selo_topo(c, W / 2)
    s = "QUAL SOBE MAIS RÁPIDO?"
    text(c, s, W / 2, 270, fit(s, 130, 1780), "black", INK)
    PE = V.Plano(220, 400, 620, 430, (0, 5), (0, 10))
    PD = V.Plano(1140, 400, 620, 430, (0, 5), (0, 100))
    for P, yt, m in ((PE, range(0, 11, 2), 2), (PD, range(0, 101, 20), 10)):
        P.eixos(c, 1.0, xt=range(0, 6), yt=yt, size=30)
        P.reta(c, 1.0, m, 0, PURPLE, width=12)
    for x, L in ((530, "A"), (1450, "B")):
        badge_num(c, L, x, 950, 1.0, 36, bg=INK)
    rrect(c, 0, 1010, W, 70, 0, AMBER)
    text_mid(c, "OLHO ENGANA · CONTA NÃO", W / 2, 1045, 44, "black", "#FFFFFF")


def capa_pregos(c):
    background(c); selo_topo(c)
    P = V.Plano(160, 260, 760, 660, (0, 6), (0, 24))
    P.eixos(c, 1.0, xt=range(0, 7), yt=range(0, 25, 4), size=30)
    c.save(); c.clipRect(skia.Rect.MakeXYWH(P.x0, P.y0, P.w, P.h))
    line(c, P.px(0.2), P.py(3 * 0.2 + 5), P.px(5.9), P.py(3 * 5.9 + 5), mix(PURPLE, "#FFFFFF", 0.15), 1.0, 22)
    c.restore()
    for x, y in ((2, 11), (5, 20)):
        c.save(); c.translate(P.px(x), P.py(y)); c.scale(1.7, 1.7); c.translate(-P.px(x), -P.py(y))
        V.prego(c, P, x, y, 1.0, BLUE)
        c.restore()
    pill(c, "(2, 11)", P.px(2) + 40, P.py(11) + 50, BLUE, size=40, bounds=(0, 1920))
    pill(c, "(5, 20)", P.px(5) - 40, P.py(20) - 64, BLUE, size=40, anchor="right", bounds=(0, 1920))
    s1, s2 = "2 PONTOS", "BASTAM"
    text(c, s1, 1440, 420, fit(s1, 150, 860), "black", INK)
    text(c, s2, 1440, 570, fit(s2, 150, 860), "black", BLUE)
    w = 760
    shadow_rrect(c, 1440 - w / 2, 660, w, 200, 30, 1, 1.4)
    rrect(c, 1440 - w / 2, 660, w, 200, 30, PURPLE)
    text_mid(c, "f(x) = ?", 1440, 760, 130, "black", "#FFFFFF")


def capa_sinal(c):
    background(c); selo_topo(c)
    P = V.Plano(200, 240, 760, 700, (-1, 5), (-3, 7))
    P.eixos(c, 1.0, xt=range(-1, 6), yt=range(-2, 8, 2), size=30)
    for m, col in ((1.5, GREEN), (0, INK), (-1.5, RED)):
        P.reta(c, 1.0, m, 2, col, width=12)
    c.drawCircle(P.px(0), P.py(2), 20, paint("#FFFFFF"))
    c.drawCircle(P.px(0), P.py(2), 15, paint(BLUE))
    for k, (s_, col) in enumerate((("SOBE,", GREEN), ("DEITA", INK), ("OU DESCE?", RED))):
        text(c, s_, 1430, 380 + k * 170, fit(s_, 150, 860), "black", col)
    for k, (s_, col) in enumerate((("a > 0 ?", GREEN), ("a = 0 ?", INK), ("a < 0 ?", RED))):
        pill(c, s_, 1110 + k * 230, 920, col, size=40, anchor="center", bounds=(0, 1920))


if __name__ == "__main__":
    for nome, fn in (("capa_A_qual_sobe_mais_rapido", capa_olho), ("capa_B_dois_pontos_bastam", capa_pregos),
                     ("capa_C_sobe_deita_desce", capa_sinal)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
