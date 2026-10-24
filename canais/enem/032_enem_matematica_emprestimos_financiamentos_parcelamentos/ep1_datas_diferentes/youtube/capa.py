"""Capas — Empréstimos, Financiamentos e Parcelamentos, Episódio 1: dinheiro em datas diferentes (tema claro).
3 variações em 1280x720. Formatos: A = duas moedas gigantes (R$ e US$) com o "+" riscado, título em duas linhas no alto
"SOMAR PARCELAS = SOMAR REAL COM DÓLAR"; B = a fatura com o botão "PAGAR O MÍNIMO" à esquerda e a máquina do rotativo
× 1,12 × 1,12 × 1,12 à direita, título "PAGOU SÓ O MÍNIMO?"; C = linha do tempo larga com três moedinhas passando pelos
guichês ÷ 1,1 · ÷ 1,21 · ÷ 1,331, título "QUITAR HOJE: QUANTO?" (sem o valor)."""
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


def selo_topo(c, cx=None):
    s = "MATEMÁTICA ENEM · EMPRÉSTIMOS · EP. 1"
    if cx is None:
        pill(c, s, 84, 90, BLUE, size=34, bounds=(0, 1920))
    else:
        pill(c, s, cx, 90, BLUE, size=34, anchor="center", bounds=(0, 1920))


def capa_moedas(c):
    background(c); selo_topo(c, W / 2)
    s1, s2 = "SOMAR PARCELAS =", "SOMAR REAL COM DÓLAR"
    text(c, s1, W / 2, 270, fit(s1, 120, 1700), "black", INK)
    text(c, s2, W / 2, 400, fit(s2, 120, 1780), "black", RED)
    V.moeda(c, 560, 740, 220, "1.210", PURPLE, 1.0)
    V.moeda(c, 1360, 740, 220, "1.210", BLUE, 1.0, rs="US$")
    text_mid(c, "+", 960, 740, 220, "black", INK)
    V.strike(c, 860, 820, 1060, 660, 1.0, RED)
    V.selo(c, 960, 1000, 1.0, "DATAS DIFERENTES!", AMBER, -4, 50)


def capa_rotativo(c):
    background(c); selo_topo(c)
    text(c, "PAGOU SÓ", 84, 320, 150, "black", INK, align="left")
    text(c, "O MÍNIMO?", 84, 470, 150, "black", RED, align="left")
    rrect(c, 84, 560, 620, 400, 40, "#FFFFFF", shadow=True)
    text(c, "FATURA", 394, 650, 44, "black", INK2, tracking=3)
    text(c, "R$ 2.000", 394, 770, 110, "black", INK)
    rrect(c, 174, 830, 440, 100, 50, RED)
    text_mid(c, "PAGAR O MÍNIMO", 394, 880, 40, "black", "#FFFFFF")
    for k in range(3):
        y = 330 + k * 250
        rrect(c, 1180, y - 95, 560, 190, 36, mix("#FFFFFF", RED, 0.10), shadow=True)
        text_mid(c, "× 1,12", 1460, y, 110, "black", RED)
        text(c, f"mês {k + 1}", 1810, y + 15, 40, "black", GRAY, align="right")
    arrow(c, 760, 760, 1150, 400, RED, 1.0, 12, 40)


def capa_quitar(c):
    background(c); selo_topo(c)
    text(c, "QUITAR HOJE:", 84, 300, 140, "black", INK, align="left")
    text(c, "QUANTO?", 84, 440, 140, "black", PURPLE, align="left")
    V.selo(c, 1420, 330, 1.0, "3 × R$ 1.331", AMBER, -4, 70)
    y = 640
    line(c, 160, y, 1780, y, INK2, 1.0, 10)
    for k, rot in enumerate(("HOJE", "1 mês", "2 meses", "3 meses")):
        x = 220 + k * 500
        c.drawCircle(x, y, 22, paint(BLUE if k == 0 else INK2))
        text(c, rot, x, y + 80, 46, "black", BLUE if k == 0 else GRAY)
    for k, fat in enumerate(("1,1", "1,21", "1,331")):
        x = 720 + k * 500
        V.moeda(c, x, 900, 90, "1.331", PURPLE, 1.0)
        rrect(c, x - 250, 860, 150, 80, 16, mix("#FFFFFF", GREEN, 0.15))
        text_mid(c, "÷ " + fat, x - 175, 900, 38, "black", GREEN)
        arrow(c, x - 90, 980, x - 330, 980, GREEN, 1.0, 6, 22)


if __name__ == "__main__":
    for nome, fn in (("capa_A_real_com_dolar", capa_moedas), ("capa_B_pagou_o_minimo", capa_rotativo),
                     ("capa_C_quitar_hoje", capa_quitar)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
