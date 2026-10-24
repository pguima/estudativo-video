"""Capas — Comparação de Propostas e Tomada de Decisão, Episódio 5: Revisão geral e fechamento da Matemática Financeira
(tema claro). 3 variações em 1280x720.
Evita os formatos das revisões anteriores ("N PEGADINHAS: QUANTAS VOCÊ ACERTA?", "VOCÊ CAI NESTA?", "A POTÊNCIA VEM NO
ENUNCIADO", "PORCENTAGEM — DE QUÊ?", "A inflação caiu...", "TIRE A FANTASIA DO ANÚNCIO"...) e as capas dos eps 1–4 desta
série ("QUAL VOCÊ ESCOLHE?", "À VISTA OU PARCELADO?", "COMPARE NA MESMA DATA"...). Nenhuma entrega gabarito."""
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


def lampada(c, cx, cy, r, col, a=1.0):
    c.drawCircle(cx, cy, r, paint(mix("#FFFFFF", col, 0.35), a))
    c.drawCircle(cx, cy, r, paint(col, a, stroke=6))
    rrect(c, cx - r * 0.45, cy + r * 0.85, r * 0.9, r * 0.55, 8, INK2, a)
    for k in range(3):
        line(c, cx - r * 0.45, cy + r * (1.0 + 0.15 * k), cx + r * 0.45, cy + r * (1.0 + 0.15 * k), "#FFFFFF", a, 3)


def capa_barato(c):
    background(c); selo(c); painel(c)
    c.save(); c.translate(1470, 300); c.scale(1.35, 1.35)
    V.balanca(c, 0, 0, 1, ("PROPOSTA A", "R$ ?", BLUE), ("PROPOSTA B", "R$ ?", AMBER), 0, L=150)
    c.restore()
    K.selo(c, 1470, 690, 1, "DEPENDE DO USO", GREEN, -6, 50)
    text(c, "e da DATA", 1470, 860, 52, "black", PURPLE)
    big(c, "O MAIS", 320)
    big(c, "BARATO", 470)
    boxed(c, "NEM SEMPRE GANHA", 70, 520, 116, RED)
    text(c, "revisão + 5 questões novas de decisão", 90, 860, 46, "extrabold", INK2, align="left")


def capa_bloco(c):
    background(c); selo(c); painel(c)
    for n, s in enumerate(V.ASSUNTOS):
        y = 230 + n * 118
        col = (BLUE, BLUE, AMBER, PURPLE, RED, GREEN)[n]
        c.drawCircle(1230, y, 34, paint(col))
        check_icon(c, 1230, y, 18, 1, "#FFFFFF")
        text(c, s, 1290, y + 16, 46, "black", INK, align="left")
    big(c, "6 ASSUNTOS.", 320)
    big(c, "1 REGRA.", 470)
    boxed(c, "FATORES E DATAS", 70, 520, 120, PURPLE)
    text(c, "fechando a Matemática Financeira", 90, 860, 48, "extrabold", INK2, align="left")


def capa_lampada(c):
    background(c); selo(c); painel(c)
    lampada(c, 1300, 360, 110, GREEN)
    lampada(c, 1640, 360, 110, AMBER)
    text(c, "LED", 1300, 375, 50, "black", GREEN)
    text(c, "COMUM", 1640, 375, 44, "black", AMBER)
    text(c, "R$ 30", 1300, 610, 60, "black", INK)
    text(c, "R$ 6", 1640, 610, 60, "black", INK)
    text(c, "+ 1¢ por hora", 1300, 670, 36, "black", GREEN)
    text(c, "+ 5¢ por hora", 1640, 670, 36, "black", AMBER)
    rrect(c, 1220, 740, 500, 150, 26, mix("#FFFFFF", PURPLE, 0.10), 1)
    text(c, "horas = ?", 1470, 840, 72, "black", PURPLE)
    big(c, "QUAL LÂMPADA", 320)
    big(c, "SAI MAIS", 470)
    boxed(c, "BARATO?", 70, 520, 150, AMBER)
    text(c, "o ponto de equilíbrio no ENEM", 90, 860, 48, "extrabold", INK2, align="left")


if __name__ == "__main__":
    for nome, fn in (("capa_A_mais_barato_nem_sempre", capa_barato), ("capa_B_seis_assuntos_uma_regra", capa_bloco),
                     ("capa_C_qual_lampada", capa_lampada)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
