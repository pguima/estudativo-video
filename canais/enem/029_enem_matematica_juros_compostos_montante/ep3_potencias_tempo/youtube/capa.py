"""Capas — Juros Compostos, Episódio 3: potências sem calculadora e descobrir o tempo (tema claro). 3 variações em 1280x720.
Formatos: A = duelo de fichas "1,34 × 1,34" (certo) contra "2 × 1,34" (riscado), título no alto;
B = radar verde grande à direita e a pergunta "dobra em quanto tempo?" empilhada à esquerda;
C = a potência gigante "1,05¹² = ?" no centro com o selo SEM CALCULADORA e as 3 saídas embaixo."""
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
    s = "MATEMÁTICA ENEM · JUROS COMPOSTOS · EP. 3"
    if cx is None:
        pill(c, s, 84, 90, BLUE, size=34, bounds=(0, 1920))
    else:
        pill(c, s, cx, 90, BLUE, size=34, anchor="center", bounds=(0, 1920))


def capa_duelo(c):
    background(c); selo_topo(c, W / 2)
    s = "DOBROU O TEMPO?"
    text(c, s, W / 2, 290, fit(s, 150, 1780), "black", INK)
    s2 = "NÃO DOBRE O FATOR"
    text(c, s2, W / 2, 420, fit(s2, 110, 1780), "black", RED)
    for k, (expr_, col, ok) in enumerate((("1,34 · 1,34", GREEN, True), ("2 · 1,34", RED, False))):
        x = 200 + k * 820
        shadow_rrect(c, x, 520, 700, 420, 40, 1, 1.4)
        rrect(c, x, 520, 700, 420, 40, mix("#FFFFFF", col, 0.08))
        V.m(c, expr_, x + 350, 700, 120, 1.0, col)
        check_icon(c, x + 350, 860, 46, 1.0, col, "check" if ok else "x")
        if not ok:
            V.strike(c, x + 120, 700, x + 580, 700, 1.0, RED)


def capa_radar(c):
    background(c); selo_topo(c)
    text(c, "DOBRA EM", 84, 340, 130, "black", INK, align="left")
    text(c, "QUANTO", 84, 490, 130, "black", INK, align="left")
    text(c, "TEMPO?", 84, 640, 130, "black", AMBER, align="left")
    pill(c, "72 ÷ taxa", 84, 820, GREEN, size=80, bounds=(0, 1920))
    V.radar(c, 1420, 560, 380, 1.0, 0.55)
    c.drawCircle(1420 - 150, 560 - 120, 34, paint(GREEN, 0.35))
    c.drawCircle(1420 - 150, 560 - 120, 22, paint(GREEN, 1.0))
    pill(c, "≈ 7 anos?", 1420 - 150, 560 - 210, GREEN, size=50, anchor="center", bounds=(0, 1920))
    text(c, "REGRA DO 72", 1420, 1010, 70, "black", GREEN)


def capa_potencia(c):
    background(c); selo_topo(c, W / 2)
    shadow_rrect(c, 260, 200, 1400, 520, 50, 1, 1.4)
    rrect(c, 260, 200, 1400, 520, 50, "#FFFFFF")
    V.m(c, "1,05^{12} = ?", W / 2, 450, 230, 1.0, PURPLE)
    V.selo(c, 1440, 690, 1.0, "SEM CALCULADORA", RED, -6, 56)
    for k, (s, col) in enumerate((("QUEBRAR", PURPLE), ("TENTAR", BLUE), ("REGRA DO 72", GREEN))):
        cx = 420 + k * 540
        w = text_w(s, "black", 64) + 80
        rrect(c, cx - w / 2, 830, w, 140, 30, mix("#FFFFFF", col, 0.16))
        text_mid(c, s, cx, 900, 64, "black", col)


if __name__ == "__main__":
    for nome, fn in (("capa_A_nao_dobre_o_fator", capa_duelo), ("capa_B_regra_do_72", capa_radar),
                     ("capa_C_sem_calculadora", capa_potencia)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
