"""Capas — Razão, Proporção e Regra de Três, Episódio 1: Razão (tema claro). 3 variações em 1280x720."""
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
    pill(c, "MATEMÁTICA ENEM · RAZÃO · EP. 1", 84, 90, BLUE, size=40, bounds=(0, 1920))


def painel(c):
    card(c, 1120, 120, 700, 840, r=36)


def capa_ordem(c):
    background(c); selo(c); painel(c)
    V.copo(c, 1200, 200, 110, 160, V.SUCO)
    for k in range(3):
        V.copo(c, 1360 + k * 140, 200, 110, 160, V.AGUA)
    text(c, "1 copo PARA 3", 1470, 430, 44, "black", INK)
    K.expr(c, "1/3", 1340, 600, 130, 1.0, cores={0: GREEN})
    K.fmid(c, "≠", 1490, 600, 110, "black", RED)
    K.expr(c, "3/1", 1640, 600, 130, 1.0, cores={0: RED})
    text(c, "a ordem muda TUDO", 1470, 860, 46, "black", PURPLE)
    big(c, "O QUE VEM DEPOIS", 330)
    big(c, "DO “PARA” VAI", 470)
    boxed(c, "EMBAIXO", 70, 520, 170, PURPLE)
    text(c, "razão do zero: a ordem que derruba no ENEM", 90, 860, 44, "extrabold", INK2, align="left")


def capa_tudo(c):
    background(c); selo(c); painel(c)
    ics = [(V.ic_velocimetro, "km/h"), (V.ic_balanca, "g/cm³"), (V.ic_mapa, "1 : n"), (V.ic_bomba, "km/L"),
           (V.ic_torneira, "L/s"), (V.ic_etiqueta, "R$/kg")]
    for k, (ic, u) in enumerate(ics):
        r, col = divmod(k, 2)
        x, y = 1300 + col * 340, 250 + r * 250
        c.save(); c.translate(x, y); c.scale(1.5, 1.5); c.translate(-x, -y)
        ic(c, x, y, 1.0)
        c.restore()
        K.ftext(c, u, x, y + 130, 44, "black", PURPLE)
    big(c, "VELOCIDADE, PREÇO,", 330)
    big(c, "CONSUMO, ESCALA…", 470)
    boxed(c, "TUDO É RAZÃO", 70, 520, 150, GREEN)
    text(c, "o assunto que mais resolve questões do ENEM", 90, 860, 44, "extrabold", INK2, align="left")


def capa_total(c):
    background(c); selo(c); painel(c)
    for i in range(7):
        V.boneco(c, 1250 + i * 75, 260, 90, V.PE)
    for i in range(21):
        r, k = divmod(i, 7)
        V.boneco(c, 1250 + k * 75, 380 + r * 85, 70, V.SENT)
    K.expr(c, "7/21 = 1/3", 1470, 720, 70, 1.0, cores={2: BLUE})
    K.expr(c, "7/28 = 1/4", 1470, 860, 70, 1.0, cores={2: AMBER})
    big(c, "“PARA O OUTRO”", 330)
    big(c, "OU “PARA O", 470)
    boxed(c, "TOTAL”?", 70, 520, 170, AMBER)
    text(c, "o erro de razão que o ENEM adora cobrar", 90, 860, 44, "extrabold", INK2, align="left")


if __name__ == "__main__":
    for nome, fn in (("capa_A_depois_do_para", capa_ordem), ("capa_B_tudo_e_razao", capa_tudo),
                     ("capa_C_outro_ou_total", capa_total)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
