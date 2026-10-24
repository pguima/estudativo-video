"""Capas — Função Quadrática, Episódio 1: a parábola e o que o Δ desenha (tema claro). 3 variações em 1280x720.
A = as duas parábolas com olhinhos (a que sorri e a triste) e "SORRI OU FICA TRISTE?" — quem decide é o a;
B = três parábolas sobre a faixa marrom do chão e "QUANTAS VEZES ENCOSTA NO CHÃO?" com o Δ = ? gigante;
C = a lei h(t) = 20t − 5t² gigante numa faixa escura com os três chips a = ? · b = ? · c = ? e "QUEM É O a?".
Nenhuma mostra gabarito (nem k > 25, nem a = −5)."""
import importlib.util, subprocess, sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(next(d / "_ferramentas" for d in HERE.parents if (d / "_ferramentas").is_dir())))
import skia
import motor
motor.set_theme("claro")
from motor import *  # noqa

_spec = importlib.util.spec_from_file_location("visual_ep1", HERE.parent / "roteiro" / "visual.py")
V = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(V)
motor.set_theme("claro")


def fit(s, size, maxw, peso="black"):
    while text_w(s, peso, size) > maxw:
        size -= 4
    return size


def selo_topo(c, cx=None, cor=BLUE):
    s = "MATEMÁTICA ENEM · FUNÇÃO QUADRÁTICA · EP. 1"
    if cx is None:
        pill(c, s, 84, 90, cor, size=34, bounds=(0, 1920))
    else:
        pill(c, s, cx, 90, cor, size=34, anchor="center", bounds=(0, 1920))


def capa_sorri(c):
    background(c); selo_topo(c, W / 2)
    s = "SORRI OU FICA TRISTE?"
    text(c, s, W / 2, 290, fit(s, 150, 1760), "black", INK)
    for k, (f, col, triste, yb) in enumerate(((lambda x: 0.6 * (x - 2) ** 2 - 1.6, GREEN, False, 0.5),
                                              (lambda x: -0.6 * (x - 2) ** 2 + 1.6, RED, True, 1.75))):
        x0 = 170 + k * 830
        shadow_rrect(c, x0, 360, 750, 560, 40, 1, 1.4)
        rrect(c, x0, 360, 750, 560, 40, "#FFFFFF")
        g = V.plano(x0 + 80, 420, 590, 430, -0.2, 4.2, -2.6, 2.6)
        V.curva(c, g, f, 1.0, col, 1.0, 16)
        X, Y = g.pt(2, yb)
        for sx in (-1, 1):
            c.drawCircle(X + sx * 80, Y - 70, 22, paint(INK, 1))
    rrect(c, 0, 960, W, 120, 0, PURPLE)
    text_mid(c, "quem decide é UM número só", W / 2, 1020, 64, "black", "#FFFFFF")


def capa_chao(c):
    background(c); selo_topo(c)
    s1, s2 = "QUANTAS VEZES", "ENCOSTA NO CHÃO?"
    text(c, s1, 84, 270, fit(s1, 120, 1100), "black", INK, align="left")
    text(c, s2, 84, 400, fit(s2, 120, 1100), "black", PURPLE, align="left")
    rrect(c, 60, 776, 1800, 26, 6, V.CHAO)
    for k, (f, x0, x1) in enumerate(((lambda x: (x - 1) * (x - 3), -0.5, 4.5), (lambda x: (x - 2) ** 2, -0.5, 4.5),
                                     (lambda x: x * x - 2 * x + 3, -1.5, 3.5))):
        g = V.plano(120 + k * 600, 480, 480, 380, x0, x1, -1.5, 6.5)
        V.curva(c, g, f, 1.0, [PURPLE, BLUE, GREEN][k], 1.0, 12)
    shadow_rrect(c, 1330, 150, 470, 250, 40, 1, 1.4)
    rrect(c, 1330, 150, 470, 250, 40, AMBER)
    text_mid(c, "Δ = ?", 1565, 275, 140, "black", "#FFFFFF")


def capa_quem(c):
    background(c)
    rrect(c, 0, 0, W, 560, 0, "#1E2230")
    pill(c, "MATEMÁTICA ENEM · FUNÇÃO QUADRÁTICA · EP. 1", W / 2, 90, BLUE, size=34, anchor="center", bounds=(0, 1920))
    V.expr(c, "h(t) = 20t − 5t^2", W / 2, 330, 190, 1.0, cores={i: "#FFFFFF" for i in range(5)})
    for k, (s_, col) in enumerate((("a = ?", PURPLE), ("b = ?", INK), ("c = ?", BLUE))):
        x = 420 + k * 540
        shadow_rrect(c, x - 220, 620, 440, 180, 36, 1, 1.4)
        rrect(c, x - 220, 620, 440, 180, 36, "#FFFFFF")
        text_mid(c, s_, x, 710, 100, "black", col)
    s = "QUEM É O a?"
    text(c, s, W / 2, 990, fit(s, 140, 1700), "black", RED)


if __name__ == "__main__":
    for nome, fn in (("capa_A_sorri_ou_triste", capa_sorri), ("capa_B_encosta_no_chao", capa_chao),
                     ("capa_C_quem_e_o_a", capa_quem)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
