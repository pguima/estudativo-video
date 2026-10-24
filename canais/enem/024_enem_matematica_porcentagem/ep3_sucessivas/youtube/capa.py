"""Capas — Porcentagem, Episódio 3: variações sucessivas (tema claro). 3 variações em 1280x720 (nenhuma mostra gabarito)."""
import importlib.util, subprocess, sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(next(d / "_ferramentas" for d in HERE.parents if (d / "_ferramentas").is_dir())))
import skia
import motor
motor.set_theme("claro")
from motor import *  # noqa
from aula import strike  # noqa

_spec = importlib.util.spec_from_file_location("visual_ep3", HERE.parent / "roteiro" / "visual.py")
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
    pill(c, "MATEMÁTICA ENEM · PORCENTAGEM · EP. 3", 84, 90, BLUE, size=36, bounds=(0, 1920))


def painel(c):
    card(c, 1120, 120, 700, 840, r=36)


def capa_somar(c):
    background(c); selo(c); painel(c)
    V.maquina(c, 1470, 290, "1,10", 1.0, ang=12, col=GREEN, w=300, h=170)
    text(c, "depois", 1470, 450, 34, "bold", INK2)
    V.maquina(c, 1470, 590, "1,20", 1.0, ang=-8, col=GREEN, w=300, h=170)
    V.ftext(c, "+30% ?", 1470, 800, 80, "black", RED)
    strike(c, 1320, 780, 1620, 780, 1.0, RED, 1.0)
    text(c, "multiplique as máquinas", 1470, 905, 34, "black", GREEN)
    big(c, "+10% E +20%", 330)
    big(c, "NÃO SÃO +30%", 470)
    boxed(c, "MULTIPLIQUE", 70, 520, 150, GREEN)
    text(c, "variações sucessivas com uma única conta", 90, 860, 44, "extrabold", INK2, align="left")


def capa_descontos(c):
    background(c); selo(c); painel(c)
    rrect(c, 1250, 210, 440, 220, 28, RED, shadow=True)
    text_mid(c, "30% OFF", 1470, 300, 84, "black", "#FFFFFF")
    text_mid(c, "em tudo", 1470, 380, 34, "bold", "#FFFFFF")
    rrect(c, 1290, 470, 360, 140, 24, AMBER, shadow=True)
    text_mid(c, "+10% no caixa", 1470, 540, 42, "black", "#FFFFFF")
    V.ftext(c, "= 40% ?", 1470, 730, 80, "black", RED)
    strike(c, 1320, 710, 1620, 710, 1.0, RED, 1.0)
    text(c, "o 2º é sobre um preço menor", 1470, 860, 32, "black", INK2)
    big(c, "DESCONTO EM CIMA", 330)
    big(c, "DE DESCONTO", 470)
    boxed(c, "NÃO SE SOMA", 70, 520, 150, RED)
    text(c, "quanto você paga de verdade, sem armadilha", 90, 860, 44, "extrabold", INK2, align="left")


def capa_bola(c):
    background(c); selo(c); painel(c)
    V.bola(c, 1330, 330, 105, 1.0, "R$ 1 000", INK, 34)
    arrow(c, 1440, 360, 1520, 430, GREEN, 1.0, 6, 20)
    V.bola(c, 1600, 560, 135, 1.0, "R$ 1 100", GREEN, 40)
    text(c, "+20% sobre QUAL?", 1470, 800, 48, "black", AMBER)
    text(c, "a bola que já cresceu", 1470, 870, 34, "black", INK2)
    big(c, "A BOLA DE NEVE", 330)
    big(c, "DOS AUMENTOS", 470)
    boxed(c, "POR QUE NÃO SOMA", 70, 520, 140, BLUE)
    text(c, "o 2º aumento vale mais em reais", 90, 860, 44, "extrabold", INK2, align="left")


if __name__ == "__main__":
    for nome, fn in (("capa_A_nao_sao_30", capa_somar), ("capa_B_desconto_sobre_desconto", capa_descontos),
                     ("capa_C_bola_de_neve", capa_bola)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
