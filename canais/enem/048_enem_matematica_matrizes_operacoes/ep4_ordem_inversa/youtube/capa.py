"""Capas — Matrizes, Episódio 4: o que muda em relação aos números e a matriz inversa (tema claro). 3 variações em 1280x720.
A = o gancho: duas matrizes não nulas cujo produto é a matriz nula, com "PRODUTO ZERO SEM FATOR ZERO?";
B = o cadeado e a chave: a matriz (3 1 / 5 2) e "A⁻¹ = ?", "A CHAVE DA MATRIZ";
C = meia e sapato com "AB ? BA": "A ORDEM IMPORTA?".
Nenhuma mostra gabarito (a inversa e as respostas das questões não aparecem)."""
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
    s = "MATEMÁTICA ENEM · MATRIZES · EP. 4"
    if cx is None:
        pill(c, s, 84, 90, BLUE, size=34, bounds=(0, 1920))
    else:
        pill(c, s, cx, 90, BLUE, size=34, anchor="center", bounds=(0, 1920))


def capa_nulo(c):
    background(c); selo_topo(c, W / 2)
    s = "PRODUTO ZERO SEM FATOR ZERO?"
    text(c, s, W / 2, 290, fit(s, 130, 1780), "black", INK)
    shadow_rrect(c, 100, 360, 1720, 470, 40, 1, 1.4)
    rrect(c, 100, 360, 1720, 470, 40, "#FFFFFF")
    xs = V.prod(c, 960, 590, [V.U_, "·", V.V_, "=", V.Z_], 110, 1, gap=50)
    V.K.boxed(c, xs[4] - 220, 425, 440, 330, GREEN, 1, 0.10, 30, 8)
    for xk in (xs[0], xs[2]):
        V.selo(c, xk, 900, 1.0, "NÃO É NULA", RED, -5, 50)
    V.selo(c, xs[4], 900, 1.0, "NULA", GREEN, 4, 50)


def capa_chave(c):
    background(c); selo_topo(c)
    shadow_rrect(c, 70, 190, 900, 820, 40, 1, 1.4)
    rrect(c, 70, 190, 900, 820, 40, "#FFFFFF")
    V.cadeado(c, 520, 560, 480, 1, 0.0)
    V.chave(c, 520, 910, 260, 1)
    s1 = "A CHAVE DA MATRIZ"
    text(c, s1, 1440, 330, fit(s1, 110, 850), "black", INK)
    V.linha(c, [("A = ", INK)], 1150, 560, 90, 1)
    V.matriz(c, 1460, 560, V.K_, 90, 1)
    s2 = "A⁻¹ = ?"
    V.K.expr(c, "A^{-1} = ?", 1440, 820, 110, 1, cores={i: V.CHAVE for i in range(20)})
    rrect(c, 1040, 920, 800, 100, 26, PURPLE)
    text_mid(c, "a inversa em 3 movimentos", 1440, 970, 52, "black", "#FFFFFF")


def capa_ordem(c):
    background(c); selo_topo(c, W / 2)
    s = "A ORDEM IMPORTA?"
    text(c, s, W / 2, 300, fit(s, 170, 1780), "black", INK)
    for k, (a_, b_, col) in enumerate((("meia", "sapato", PURPLE), ("sapato", "meia", AMBER))):
        x = 520 + k * 880
        shadow_rrect(c, x - 360, 380, 720, 420, 44, 1, 1.4)
        rrect(c, x - 360, 380, 720, 420, 44, "#FFFFFF")
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x - 360, 380, 720, 420), 44, 44), paint(col, 1, stroke=10))
        text_mid(c, "AB" if k == 0 else "BA", x, 480, 110, "black", col)
        f1, f2 = (V.meia, V.sapato) if k == 0 else (V.sapato, V.meia)
        f1(c, x - 140, 660, 170, 1); text_mid(c, "→", x, 670, 80, "black", GRAY); f2(c, x + 150, 670, 170, 1)
    text_mid(c, "=?", W / 2, 590, 110, "black", RED)
    rrect(c, 260, 860, 1400, 130, 30, RED)
    text_mid(c, "as regras dos números que FALHAM", W / 2, 925, 66, "black", "#FFFFFF")


if __name__ == "__main__":
    for nome, fn in (("capa_A_produto_zero", capa_nulo), ("capa_B_chave_inversa", capa_chave),
                     ("capa_C_ordem_importa", capa_ordem)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
