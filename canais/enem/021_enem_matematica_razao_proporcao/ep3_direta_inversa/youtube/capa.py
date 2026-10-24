"""Capas — Razão, Proporção e Regra de Três, Episódio 3: Direta ou inversa? (tema claro). 3 variações em 1280x720."""
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
K = V.K
fmid = K.fmid


def big(c, s, y, maxw=1000, size=140):
    while text_w(s, "black", size) > maxw:
        size -= 4
    text(c, s, 80, y, size, "black", INK, align="left")


def boxed(c, s, x, y, size, bg_col, fg="#FFFFFF", pad=34, maxw=1000):
    while text_w(s, "black", size) + pad * 2 > maxw:
        size -= 4
    w = text_w(s, "black", size) + pad * 2
    h = size * 1.22
    shadow_rrect(c, x, y, w, h, 22, 1, 1.4)
    rrect(c, x, y, w, h, 22, bg_col)
    text_mid(c, s, x + w / 2, y + h / 2, size, "black", fg)


def selo(c):
    pill(c, "MATEMÁTICA ENEM · EPISÓDIO 3", 84, 90, BLUE, size=40, bounds=(0, 1920))


def painel(c):
    card(c, 1120, 120, 700, 840, r=36)


def capa_dobro(c):
    background(c); selo(c); painel(c)
    rrect(c, 1170, 190, 600, 330, 26, mix("#FFFFFF", V.DIR, 0.08))
    text(c, "DIRETA", 1470, 260, 52, "black", V.DIR)
    fmid(c, "× 2  →  × 2", 1470, 350, 64, "black", AMBER)
    text(c, "dobrou também", 1470, 460, 36, "black", INK2)
    rrect(c, 1170, 560, 600, 330, 26, mix("#FFFFFF", V.INV, 0.08))
    text(c, "INVERSA", 1470, 630, 52, "black", V.INV)
    fmid(c, "× 2  →  ÷ 2", 1470, 720, 64, "black", AMBER)
    text(c, "virou metade", 1470, 830, 36, "black", INK2)
    big(c, "DIRETA OU", 340)
    big(c, "INVERSA?", 470)
    boxed(c, "O TESTE DO DOBRO", 70, 520, 120, AMBER)
    text(c, "a decisão que vale a questão de regra de três", 90, 860, 44, "extrabold", INK2, align="left")


def capa_operarios(c):
    background(c); selo(c); painel(c)
    text(c, "6 operários: 10 dias", 1470, 230, 44, "black", INK)
    text(c, "12 operários: ?", 1470, 300, 44, "black", INK)
    rrect(c, 1200, 360, 540, 120, 22, mix("#FFFFFF", RED, 0.10))
    K.expr(c, "x = 20", 1400, 420, 70, cores={2: RED})
    check_icon(c, 1640, 420, 34, 1.0, RED, "x")
    K.expr(c, "6 · 10 = 12 · x", 1470, 580, 56)
    rrect(c, 1200, 650, 540, 120, 22, mix("#FFFFFF", GREEN, 0.12))
    K.expr(c, "x = 5", 1400, 710, 70, cores={2: GREEN})
    check_icon(c, 1640, 710, 34, 1.0, GREEN)
    text(c, "mais gente, MENOS dias", 1470, 860, 36, "black", INK2)
    big(c, "MAIS OPERÁRIOS,", 340)
    big(c, "MAIS DIAS?", 470)
    boxed(c, "ERRADO", 70, 520, 150, RED)
    text(c, "regra de três direta ou inversa, sem errar", 90, 860, 44, "extrabold", INK2, align="left")


def capa_passos(c):
    background(c); selo(c); painel(c)
    passos = ["unidades", "colunas", "direta ou inversa?", "inverter?", "cruz"]
    for k, s in enumerate(passos):
        y = 220 + k * 145
        rrect(c, 1170, y, 600, 110, 22, mix("#FFFFFF", PURPLE, 0.08))
        badge_num(c, k + 1, 1230, y + 55, 1.0, 34, bg=PURPLE)
        text_mid(c, s, 1290, y + 55, 46, "black", INK, align="left")
    big(c, "REGRA DE TRÊS", 340)
    big(c, "SIMPLES EM", 470)
    boxed(c, "5 PASSOS", 70, 520, 150, PURPLE)
    text(c, "com o teste do dobro e o erro silencioso", 90, 860, 44, "extrabold", INK2, align="left")


if __name__ == "__main__":
    for nome, fn in (("capa_A_direta_ou_inversa", capa_dobro), ("capa_B_mais_operarios", capa_operarios),
                     ("capa_C_cinco_passos", capa_passos)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
