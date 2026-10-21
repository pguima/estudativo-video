"""Capas — Compreensão Global e Tese, Episódio 5: As pistas que entregam a tese (tema claro). 3 variações em 1280x720."""
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


def big(c, s, y, maxw=1000, size=140):
    while text_w(s, "black", size) > maxw:
        size -= 4
    text(c, s, 80, y, size, "black", INK, align="left")


def boxed(c, s, x, y, size, bg_col, fg="#FFFFFF", pad=34):
    w = text_w(s, "black", size) + pad * 2
    h = size * 1.22
    shadow_rrect(c, x, y, w, h, 22, 1, 1.4)
    rrect(c, x, y, w, h, 22, bg_col)
    text_mid(c, s, x + w / 2, y + h / 2, size, "black", fg)


def selo(c):
    pill(c, "LINGUAGENS ENEM · EPISÓDIO 5", 84, 90, BLUE, size=40, bounds=(0, 1920))


def painel(c):
    card(c, 1120, 120, 700, 840, r=36)


def capa_placas(c):
    background(c); selo(c); painel(c)
    for k, kind in enumerate(("curva", "chegada", "opiniao")):
        y = 250 + k * 240
        V.placa(c, 1260, y, kind, 1, 0.9, label=False, poste=False)
        text(c, V.PLACAS[kind][0], 1360, y - 6, 44, "black", GREEN, align="left")
        text(c, V.PLACAS[kind][1].split(" · ")[0] + " · " + V.PLACAS[kind][1].split(" · ")[1], 1360, y + 44, 30, "bold", INK2, align="left")
    big(c, "O TEXTO AVISA", 340)
    big(c, "ONDE ESTÁ A", 470)
    boxed(c, "TESE", 70, 520, 160, BLUE)
    text(c, "as placas que quase ninguém vê", 90, 860, 50, "extrabold", INK2, align="left")


def capa_titulo(c):
    background(c); selo(c); painel(c)
    rrect(c, 1180, 220, 580, 260, 20, "#FFFFFF", 1, shadow=True)
    text(c, "O fim do livro?", 1470, 330, 52, "black", INK)
    for j in range(3):
        line(c, 1230, 380 + j * 26, 1700 - j * 60, 380 + j * 26, LINE, 1, 9)
    V.selo(c, 1470, 600, 1, "SÓ HIPÓTESE", AMBER, -5, 40)
    text(c, "confirme no texto", 1470, 780, 44, "black", GREEN)
    check_icon(c, 1470, 870, 40, 1, GREEN)
    big(c, "NÃO CONFIE", 340)
    big(c, "SÓ NO", 470)
    boxed(c, "TÍTULO", 70, 520, 160, AMBER, INK)
    text(c, "título, parágrafos e palavras-sinal", 90, 860, 50, "extrabold", INK2, align="left")


def capa_paragrafo(c):
    background(c); selo(c); painel(c)
    for k, (s, col) in enumerate((("apresenta o problema", BLUE), ("explica por quê", INK2), ("propõe solução", PURPLE))):
        y = 220 + k * 230
        rrect(c, 1180, y, 580, 170, 16, "#FFFFFF", 1, shadow=True)
        for j in range(3):
            line(c, 1220, y + 40 + j * 30, 1720 - j * 60, y + 40 + j * 30, LINE, 1, 10)
        pill(c, s, 1470, y + 150, col, size=30, anchor="center", bounds=(0, 1920))
    big(c, "PARA QUE", 340)
    big(c, "SERVE ESTE", 470)
    boxed(c, "PARÁGRAFO?", 70, 530, 126, PURPLE)
    text(c, "as questões de organização do texto", 90, 860, 50, "extrabold", INK2, align="left")


if __name__ == "__main__":
    for nome, fn in (("capa_A_placas", capa_placas), ("capa_B_titulo_hipotese", capa_titulo), ("capa_C_funcao_paragrafo", capa_paragrafo)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
