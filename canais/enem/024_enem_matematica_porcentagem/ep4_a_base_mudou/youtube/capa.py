"""Capas — Porcentagem, Episódio 4: a base mudou (tema claro). 3 variações em 1280x720 (nenhuma mostra gabarito das questões)."""
import importlib.util, subprocess, sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(next(d / "_ferramentas" for d in HERE.parents if (d / "_ferramentas").is_dir())))
import skia
import motor
motor.set_theme("claro")
from motor import *  # noqa
from aula import strike  # noqa

_spec = importlib.util.spec_from_file_location("visual_ep4", HERE.parent / "roteiro" / "visual.py")
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
    pill(c, "MATEMÁTICA ENEM · PORCENTAGEM · EP. 4", 84, 90, BLUE, size=36, bounds=(0, 1920))


def painel(c):
    card(c, 1120, 120, 700, 840, r=36)


def capa_volta(c):
    background(c); selo(c); painel(c)
    V.colunas(c, 0, 760, 3.4, 1.0, (1, 1, 0, 0), xs=(1220, 1410, 1600), w=140, com_selo=False)
    V.ftext(c, "?", 1600, 560, 150, "black", RED)
    V.chip(c, "+20%", 1330, 230, GREEN, 1.0, 44)
    V.chip(c, "−20%", 1560, 230, RED, 1.0, 44)
    text(c, "não volta a 100", 1470, 880, 40, "black", RED)
    big(c, "+20% E −20%", 330)
    big(c, "NÃO VOLTA", 470)
    boxed(c, "AO ORIGINAL", 70, 520, 150, RED)
    text(c, "a base mudou: entenda de uma vez", 90, 860, 44, "extrabold", INK2, align="left")


def capa_desfaz(c):
    background(c); selo(c); painel(c)
    V.chip(c, "+50%", 1470, 250, GREEN, 1.0, 56)
    V.ftext(c, "−50% ?", 1470, 420, 90, "black", RED)
    strike(c, 1330, 400, 1610, 400, 1.0, RED, 1.0)
    text(c, "volta: ÷ fator", 1470, 600, 56, "black", PURPLE)
    text(c, "ida × · volta ÷", 1470, 700, 40, "black", INK2)
    V.selo_base(c, 1470, 840, 1.0, 46)
    big(c, "QUE DESCONTO", 330)
    big(c, "DESFAZ O AUMENTO?", 470)
    boxed(c, "NÃO É O MESMO %", 70, 520, 140, AMBER)
    text(c, "volte ao valor original sem chute", 90, 860, 44, "extrabold", INK2, align="left")


def capa_etiqueta(c):
    background(c); selo(c); painel(c)
    V.etiqueta(c, 1470, 300, "R$ 150", 1.0, INK, "já com 20% de desconto", 420)
    V.ftext(c, "150 + 20% ?", 1470, 520, 72, "black", RED)
    strike(c, 1290, 500, 1650, 500, 1.0, RED, 1.0)
    text(c, "o desconto saiu do preço MAIOR", 1470, 680, 34, "black", INK2)
    text(c, "÷ fator", 1470, 800, 80, "black", GREEN)
    big(c, "QUAL ERA O PREÇO", 330)
    big(c, "ANTES DO DESCONTO?", 470)
    boxed(c, "NÃO É SOMAR 20%", 70, 520, 140, GREEN)
    text(c, "o caminho de volta, na conta certa", 90, 860, 44, "extrabold", INK2, align="left")


if __name__ == "__main__":
    for nome, fn in (("capa_A_nao_volta", capa_volta), ("capa_B_que_desconto_desfaz", capa_desfaz),
                     ("capa_C_preco_antes_do_desconto", capa_etiqueta)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
