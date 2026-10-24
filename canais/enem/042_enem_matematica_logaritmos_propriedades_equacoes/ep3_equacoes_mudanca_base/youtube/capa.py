"""Capas — Logaritmos, Episódio 3: equações com log e mudança de base (tema claro). 3 variações em 1280x720.
A = o elevador: 1,05ᵗ = 2 gigante com o t numa cabine roxa "log" e a seta de descida; "DERRUBE O t";
B = o porão: log₂ 10 com o 2 caindo para baixo de uma barra de fração vazia e "QUEM FICA EM CIMA?";
C = o duelo dos prazos: "DOBRA EM 20 ANOS?" riscado (juros simples) contra "E NOS COMPOSTOS?" com uma ampulheta "? anos".
Nenhuma mostra gabarito (o 14,2, o 3,32 e as respostas das questões não aparecem)."""
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
    s = "MATEMÁTICA ENEM · LOGARITMOS · EP. 3"
    if cx is None:
        pill(c, s, 84, 90, BLUE, size=34, bounds=(0, 1920))
    else:
        pill(c, s, cx, 90, BLUE, size=34, anchor="center", bounds=(0, 1920))


def capa_elevador(c):
    background(c); selo_topo(c)
    s = "DERRUBE O t"
    text(c, s, 110, 300, fit(s, 170, 1000), "black", INK, align="left")
    text(c, "do expoente, com log", 110, 390, 60, "black", PURPLE, align="left")
    # 1,05^t = 2 com o t na cabine
    V.tx(c, "1,05", 110, 800, 230, INK, 1.0)
    wb = V.ftext_w("1,05", "black", 230)
    xt, yt = 110 + wb + 30, 660
    rrect(c, xt - 26, yt - 110, 170, 220, 22, mix("#FFFFFF", PURPLE, 0.18), 1.0)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(xt - 26, yt - 110, 170, 220), 22, 22), paint(PURPLE, 1.0, stroke=10))
    pill(c, "log", xt + 59, yt - 150, PURPLE, size=40, anchor="center", bounds=(0, 1920))
    V.tx(c, "t", xt + 22, yt, 150, AMBER, 1.0)
    arrow(c, xt + 59, yt + 140, xt + 59, 960, PURPLE, 1.0, 12, 34)
    V.tx(c, "= 2", xt + 200, 800, 230, INK, 1.0)
    rrect(c, 1320, 600, 480, 300, 36, mix("#FFFFFF", AMBER, 0.18))
    text_mid(c, "t = ?", 1560, 750, 140, "black", AMBER)


def capa_porao(c):
    background(c); selo_topo(c, W / 2)
    s = "QUEM FICA EM CIMA?"
    text(c, s, W / 2, 300, fit(s, 150, 1700), "black", INK)
    rrect(c, 360, 380, 1200, 560, 40, "#FFFFFF", 1.0, shadow=True)
    V.tx(c, "log", 520, 560, 170, PURPLE, 1.0)
    V.tx(c, "10", 900, 560, 170, INK, 1.0)
    # o 2 caindo para o porão, em movimento
    for k, a in enumerate((0.15, 0.35, 1.0)):
        V.tx(c, "2", 820, 640 + k * 90, 110, AMBER, a)
    line(c, 980, 760, 1440, 760, INK, 1.0, 12)
    text_mid(c, "?", 1210, 680, 110, "black", GRAY)
    text_mid(c, "?", 1210, 860, 110, "black", GRAY)
    pill(c, "a base vai para o porão", 960, 1012, AMBER, size=40, anchor="center", bounds=(0, 1920))


def capa_prazos(c):
    background(c); selo_topo(c)
    rrect(c, 110, 220, 820, 360, 36, "#FFFFFF", 1.0, shadow=True)
    text(c, "JUROS SIMPLES", 520, 300, 50, "black", BLUE)
    text(c, "5% ao ano", 520, 380, 54, "black", INK2)
    s = "DOBRA EM 20 ANOS"
    text(c, s, 520, 500, fit(s, 80, 740), "black", INK)
    rrect(c, 990, 220, 820, 360, 36, mix("#FFFFFF", GREEN, 0.16))
    text(c, "JUROS COMPOSTOS", 1400, 300, 50, "black", GREEN)
    text(c, "5% ao ano", 1400, 380, 54, "black", INK2)
    text(c, "DOBRA EM...", 1400, 500, 80, "black", INK)
    s = "? ANOS"
    text(c, s, W / 2, 860, fit(s, 230, 1500), "black", AMBER)
    text(c, "sem calculadora: com log", W / 2, 990, 64, "black", PURPLE)


if __name__ == "__main__":
    for nome, fn in (("capa_A_derrube_o_t", capa_elevador), ("capa_B_quem_fica_em_cima", capa_porao),
                     ("capa_C_dobra_em_quantos_anos", capa_prazos)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
