"""Capas — Empréstimos, Financiamentos e Parcelamentos, Episódio 5: Revisão geral (tema claro). 3 variações em 1280x720.
Evita os formatos das revisões anteriores ("N PEGADINHAS: QUANTAS VOCÊ ACERTA?", "VOCÊ CAI NESTA?", "VOCÊ ESTÁ PRONTO?",
"A POTÊNCIA VEM NO ENUNCIADO", "PORCENTAGEM — DE QUÊ?", "O ENEM ESCONDE A CONVERSÃO", "A inflação caiu...") e as capas
dos eps 1–4 desta série. Nenhuma entrega gabarito das 5 questões inéditas."""
import importlib.util, subprocess, sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(next(d / "_ferramentas" for d in HERE.parents if (d / "_ferramentas").is_dir())))
import skia
import motor
motor.set_theme("claro")
from motor import *  # noqa

_spec = importlib.util.spec_from_file_location("visual_ep5", HERE.parent / "roteiro" / "visual.py")
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
    pill(c, "MATEMÁTICA ENEM · EPISÓDIO 5", 84, 90, BLUE, size=40, bounds=(0, 1920))


def painel(c):
    card(c, 1120, 120, 700, 840, r=36)


def capa_fantasia(c):
    background(c); selo(c); painel(c)
    V.anuncio(c, 1470, 420, 1, w=600, h=360)
    K.selo(c, 1470, 690, 1, "PREÇO COM FANTASIA", AMBER, -6, 46)
    text(c, "qual é o preço real?", 1470, 870, 44, "black", RED)
    big(c, "TIRE A", 320)
    big(c, "FANTASIA", 470)
    boxed(c, "DO ANÚNCIO", 70, 520, 150, RED)
    text(c, "revisão de empréstimos + 5 questões novas", 90, 860, 44, "extrabold", INK2, align="left")


def capa_tres(c):
    background(c); selo(c); painel(c)
    for k, rot in enumerate(("SAC", "PRICE", "CARTÃO")):
        y = 280 + k * 250
        if k == 0:
            V.fatias(c, 1340, y, 1, n=5, w=280, h=60)
        elif k == 1:
            V.caixa_price(c, 1340, y, 1, n=5, w=280, h=160)
        else:
            rrect(c, 1210, y - 80, 260, 160, 18, RED, 1, shadow=True)
            rrect(c, 1210, y - 48, 260, 32, 0, INK, 0.85)
            text(c, "× 1,1 × 1,1", 1340, y + 50, 34, "black", "#FFFFFF")
        text(c, rot, 1650, y + 22, 58, "black", (BLUE, AMBER, RED)[k])
    big(c, "SAC, PRICE", 330)
    big(c, "OU CARTÃO?", 470)
    boxed(c, "QUEM COBRA MAIS", 70, 520, 120, PURPLE)
    text(c, "juros, amortização e saldo sem errar", 90, 860, 46, "extrabold", INK2, align="left")


def capa_deve(c):
    background(c); selo(c); painel(c)
    V.caixa_price(c, 1470, 380, 1, n=4, w=440, h=300)
    text(c, "juros", 1270, 590, 34, "black", V.JURO, align="left")
    text(c, "amortização", 1670, 590, 34, "black", BLUE, align="right")
    rrect(c, 1200, 680, 540, 180, 26, mix("#FFFFFF", PURPLE, 0.10), 1)
    text(c, "deve agora:", 1470, 750, 44, "black", INK2)
    text(c, "R$ ?", 1470, 830, 72, "black", PURPLE)
    big(c, "PAGOU A", 330)
    big(c, "PARCELA.", 470)
    boxed(c, "QUANTO AINDA DEVE?", 70, 520, 110, BLUE)
    text(c, "o juro não abate a dívida", 90, 860, 46, "extrabold", INK2, align="left")


if __name__ == "__main__":
    for nome, fn in (("capa_A_tire_a_fantasia", capa_fantasia), ("capa_B_sac_price_cartao", capa_tres),
                     ("capa_C_quanto_ainda_deve", capa_deve)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
