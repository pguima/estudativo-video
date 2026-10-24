"""Capas — Divisão Proporcional, Episódio 1: o valor de uma parte (tema claro). 3 variações em 1280x720.
Nenhuma capa mostra a resposta das questões do episódio."""
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
    pill(c, "MATEMÁTICA ENEM · DIVISÃO PROPORCIONAL · EP. 1", 84, 90, BLUE, size=36, bounds=(0, 1920))


def painel(c):
    card(c, 1120, 140, 700, 820, r=36)


def _fileiras(c, y0, label="k", pw=110, ph=90):
    for j, p in enumerate((2, 3, 4)):
        y = y0 + j * 125
        text(c, f"peso {p}", 1260, y + 58, 32, "black", V.DONOS[j], align="right")
        for i in range(p):
            V.pacote(c, 1290 + i * (pw + 12), y, pw, ph, V.DONOS[j], 1.0, label, 34)


def capa_linha(c):
    background(c); selo(c); painel(c)
    _fileiras(c, 200)
    rrect(c, 1170, 610, 600, 250, 24, "#F2EEFE")
    K.ftext(c, "k =", 1330, 760, 64, "black", PURPLE, align="right")
    K.fr(c, "total", "soma dos pesos", 1560, 735, 50, PURPLE)
    big(c, "DIVIDA QUALQUER", 330)
    big(c, "VALOR EM 1 LINHA", 470)
    boxed(c, "O TRUQUE DO k", 70, 520, 150, PURPLE)
    text(c, "sócios, herança, bônus: o mesmo procedimento", 90, 860, 42, "extrabold", INK2, align="left")


def capa_tres(c):
    background(c); selo(c); painel(c)
    _fileiras(c, 200, None)
    K.ftext(c, "÷ 3 pessoas?", 1470, 650, 56, "black", RED)
    line(c, 1300, 630, 1640, 630, RED, 1.0, 8)
    K.ftext(c, "2 + 3 + 4 = 9 pacotinhos", 1470, 760, 46, "black", GREEN)
    big(c, "DIVIDIU PELO", 330)
    big(c, "Nº DE PESSOAS?", 470)
    boxed(c, "ERROU", 70, 520, 170, RED)
    text(c, "o erro que derruba a divisão proporcional", 90, 860, 44, "extrabold", INK2, align="left")


def capa_caixa(c):
    background(c); selo(c); painel(c)
    V.caixa(c, 1240, 230, ["1.000", "1.500", "2.500"], "5.000", 1.0, 1.0, w=460, size=50)
    big(c, "A SOMA DAS PARTES", 330)
    big(c, "FECHOU COM O TOTAL?", 470)
    boxed(c, "FECHE O CAIXA", 70, 520, 150, GREEN)
    text(c, "a conferência de 2 segundos que pega o erro", 90, 860, 44, "extrabold", INK2, align="left")


if __name__ == "__main__":
    for nome, fn in (("capa_A_uma_linha", capa_linha), ("capa_B_nao_divida_por_3", capa_tres),
                     ("capa_C_feche_o_caixa", capa_caixa)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
