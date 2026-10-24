"""Capas — Divisão Proporcional, Episódio 2: divisão inversa (tema claro). 3 variações em 1280x720."""
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
K = V.K


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
    pill(c, "MATEMÁTICA ENEM · DIVISÃO PROPORCIONAL · EP. 2", 84, 90, BLUE, size=36, bounds=(0, 1920))


def painel(c):
    card(c, 1120, 120, 700, 840, r=36)


def capa_fila(c):
    background(c); selo(c); painel(c)
    text(c, "inversamente a 2, 3, 4", 1470, 210, 36, "black", INK2)
    for k, n in enumerate((2, 3, 4)):
        V.caixa(c, "", 1290 + k * 180, 360, GREEN, 1.0, w=150, h=170)
        V.flip(c, n, 1290 + k * 180, 360, 110, 1.0, 1.0)
    check_icon(c, 1470, 500, 36, 1.0, GREEN)
    for k, n in enumerate((4, 3, 2)):
        V.caixa(c, str(n), 1290 + k * 180, 680, RED, 1.0, 80, 140, 140, fill="#FDECEC")
    check_icon(c, 1470, 820, 36, 1.0, RED, "x")
    text(c, "a fila virada", 1470, 905, 34, "black", RED)
    big(c, "INVERSA:", 330)
    big(c, "VIRE O NÚMERO,", 470)
    boxed(c, "NÃO A FILA", 70, 520, 160, RED)
    text(c, "o erro mais comum da divisão inversa", 90, 860, 44, "extrabold", INK2, align="left")


def capa_bonus(c):
    background(c); selo(c); painel(c)
    for k, (nome, falt, col) in enumerate(V.PESSOAS):
        x = 1250 + k * 220
        V.pessoa(c, x, 360, 160, col, 1.0)
        text(c, nome, x, 500, 40, "black", INK)
        text(c, falt, x, 555, 32, "black", col)
    text(c, "quem faltou MENOS", 1470, 700, 44, "black", INK)
    text(c, "leva MAIS", 1470, 770, 56, "black", GREEN)
    V.fmid(c, "quanto para cada um?", 1470, 870, 36, "black", AMBER)
    big(c, "BÔNUS PARA QUEM", 330)
    big(c, "FALTOU MENOS:", 470)
    boxed(c, "COMO DIVIDIR?", 70, 520, 150, BLUE)
    text(c, "divisão inversamente proporcional, do zero", 90, 860, 44, "extrabold", INK2, align="left")


def capa_mmc(c):
    background(c); selo(c); painel(c)
    K.expr(c, "1/2  1/3  1/4", 1470, 260, 96, 1.0, cores={0: INK, 1: INK, 2: INK}, gap=80)
    K.chip(c, "× 12", 1470, 420, PURPLE, 1.0, 48)
    for k, (n, col) in enumerate(((6, BLUE), (4, PURPLE), (3, AMBER))):
        y = 540 + k * 120
        text(c, str(n), 1220, y + 18, 56, "black", col)
        V.pacotes(c, 0, 1310, y, n, 1.0, None, col=mix(V.CAIXA, col, 0.25), s=56, gap=68)
    text(c, "pesos inteiros", 1470, 915, 38, "black", GREEN)
    big(c, "DIVISÃO INVERSA", 330)
    big(c, "SEM FRAÇÕES:", 470)
    boxed(c, "O ATALHO DO MMC", 70, 520, 140, GREEN)
    text(c, "multiplique os inversos e as frações somem", 90, 860, 44, "extrabold", INK2, align="left")


if __name__ == "__main__":
    for nome, fn in (("capa_A_vire_o_numero", capa_fila), ("capa_B_bonus", capa_bonus), ("capa_C_atalho_mmc", capa_mmc)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
