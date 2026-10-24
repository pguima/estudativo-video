"""Capas — Função Exponencial, Episódio 4: exponencial ou afim? O teste da razão (tema claro). 3 variações em 1280x720.
A = a corrida: a tartaruga na reta e a lebre na curva, placar com "?" e "QUEM VENCE NO FIM?";
B = a tabela 80 · 120 · 180 · 270 · ? com os "÷" entre vizinhos e "AFIM OU EXPONENCIAL?";
C = dois pontos conferidos (✓ ✓) e o terceiro em dúvida, com "DOIS PONTOS BASTAM?".
Nenhuma mostra gabarito (405 e 5 semanas não aparecem)."""
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
    s = "MATEMÁTICA ENEM · FUNÇÃO EXPONENCIAL · EP. 4"
    if cx is None:
        pill(c, s, 84, 90, BLUE, size=34, bounds=(0, 1920))
    else:
        pill(c, s, cx, 90, BLUE, size=34, anchor="center", bounds=(0, 1920))


def capa_corrida(c):
    background(c); selo_topo(c)
    shadow_rrect(c, 70, 190, 1040, 820, 40, 1, 1.4)
    rrect(c, 70, 190, 1040, 820, 40, "#FFFFFF")
    pl = V.Plano(170, 300, 860, 620, (0, 8), (0, 150))
    line(c, pl.x0, pl.y0 + pl.h, pl.x0 + pl.w + 30, pl.y0 + pl.h, INK2, 1, 6)
    line(c, pl.x0, pl.y0 + pl.h, pl.x0, pl.y0 - 30, INK2, 1, 6)
    pl.curva(c, 1, V.RETA, V.TART, 1, width=14, xa=0, xb=7.4)
    pl.curva(c, 1, V.CURVA, V.LEBRE, 1, width=14, xa=0, xb=7.2)
    V.tartaruga(c, pl.px(7.4), pl.py(V.RETA(7.4)) - 50, 120, 1)
    V.lebre(c, pl.px(7.1), pl.py(V.CURVA(7.1)) - 40, 120, 1)
    text(c, "20 + 10t", pl.px(3.2), pl.py(V.RETA(3.2)) - 40, 52, "black", V.TART, align="left")
    V.potencia(c, "2", "t", pl.px(1.2), pl.py(2) - 50, 64, 1, V.LEBRE)
    s1, s2 = "QUEM VENCE", "NO FIM?"
    text(c, s1, 1500, 450, fit(s1, 150, 740), "black", INK)
    sz = fit(s2, 140, 700)
    w = text_w(s2, "black", sz) + 80
    shadow_rrect(c, 1500 - w / 2, 510, w, 200, 30, 1, 1.4)
    rrect(c, 1500 - w / 2, 510, w, 200, 30, AMBER)
    text_mid(c, s2, 1500, 610, sz, "black", "#FFFFFF")
    V.selo(c, 1500, 860, 1.0, "A RETA LARGA NA FRENTE", V.TART, -5, 46)


def capa_tabela(c):
    background(c); selo_topo(c, W / 2)
    s = "AFIM OU EXPONENCIAL?"
    text(c, s, W / 2, 300, fit(s, 150, 1780), "black", INK)
    vals = ["80", "120", "180", "270", "?"]
    for k, v in enumerate(vals):
        x = 260 + k * 350
        col = AMBER if v == "?" else PURPLE
        shadow_rrect(c, x - 140, 430, 280, 240, 36, 1, 1.4)
        rrect(c, x - 140, 430, 280, 240, 36, "#FFFFFF")
        text_mid(c, v, x, 550, 120, "black", col)
        if k:
            c.drawCircle(x - 175, 760, 58, paint(GREEN, 1))
            text_mid(c, "÷", x - 175, 760, 80, "black", "#FFFFFF")
    rrect(c, 0, 900, W, 180, 0, PURPLE)
    text_mid(c, "o teste da razão em segundos", W / 2, 990, 80, "black", "#FFFFFF")


def capa_tres(c):
    background(c); selo_topo(c, W / 2)
    s = "DOIS PONTOS BASTAM?"
    text(c, s, W / 2, 300, fit(s, 160, 1780), "black", INK)
    for k, (tt, kind, col) in enumerate((("t = 0", "check", GREEN), ("t = 1", "check", GREEN), ("t = 2", None, AMBER))):
        x = 420 + k * 540
        shadow_rrect(c, x - 220, 410, 440, 440, 40, 1, 1.4)
        rrect(c, x - 220, 410, 440, 440, 40, "#FFFFFF")
        text_mid(c, tt, x, 510, 90, "black", INK)
        if kind:
            check_icon(c, x, 700, 90, 1, col)
        else:
            c.drawCircle(x, 700, 90, paint(col, 1))
            text_mid(c, "?", x, 700, 130, "black", "#FFFFFF")
    rrect(c, 0, 940, W, 140, 0, RED)
    text_mid(c, "o 3º ponto derruba a lei errada", W / 2, 1010, 70, "black", "#FFFFFF")


if __name__ == "__main__":
    for nome, fn in (("capa_A_quem_vence_no_fim", capa_corrida), ("capa_B_afim_ou_exponencial", capa_tabela),
                     ("capa_C_dois_pontos_bastam", capa_tres)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
