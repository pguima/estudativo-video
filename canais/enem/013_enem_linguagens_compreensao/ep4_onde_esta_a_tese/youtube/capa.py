"""Capas — Compreensão Global e Tese, Episódio 4: Onde a tese se esconde (tema claro). 3 variações em 1280x720."""
import importlib.util, subprocess, sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(next(d / "_ferramentas" for d in HERE.parents if (d / "_ferramentas").is_dir())))
import skia
import motor
motor.set_theme("claro")
from motor import *  # noqa

_spec = importlib.util.spec_from_file_location("visual_ep4", HERE.parent / "roteiro" / "visual.py")
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
    pill(c, "LINGUAGENS ENEM · EPISÓDIO 4", 84, 90, BLUE, size=40, bounds=(0, 1920))


def painel(c):
    card(c, 1120, 120, 700, 840, r=36)


def capa_primeira(c):
    background(c); selo(c); painel(c)
    V.balao_outro(c, "Há quem diga que...", 1240, 230, 520, 1, 1.0, 40)
    V2 = V.V2
    V2.wa_bubble(c, [("Engano.", GREEN, 1), ("A tese vem DEPOIS.", BLUE, 1)], 1220, 520, 540, 1, 44)
    text(c, "a voz do outro ≠ a do autor", 1470, 880, 34, "black", INK2)
    big(c, "A 1ª FRASE", 340)
    big(c, "PODE SER A", 470)
    boxed(c, "ARMADILHA", 70, 530, 140, AMBER, INK)
    text(c, "onde a tese se esconde no texto", 90, 860, 50, "extrabold", INK2, align="left")


def capa_onde(c):
    background(c); selo(c); painel(c)
    for k, (s, col) in enumerate((("começo", 0), ("fim", 6), ("nenhum", -1))):
        x = 1240 + k * 230
        rrect(c, x - 90, 220, 180, 300, 14, "#FFFFFF", 1, shadow=True)
        for j in range(7):
            on = j == col
            line(c, x - 60, 260 + j * 38, x + 60 - (j % 3) * 20, 260 + j * 38, BLUE if on else LINE, 1, 14 if on else 9)
        if col < 0:
            text_mid(c, "?", x, 370, 110, "black", PURPLE, 0.85)
        text(c, s, x, 580, 36, "black", INK)
    pill(c, "trailer · detetive · foto", 1470, 720, BLUE, size=34, anchor="center", bounds=(0, 1920))
    big(c, "COMEÇO, FIM", 340)
    big(c, "OU EM LUGAR", 470)
    boxed(c, "NENHUM?", 70, 520, 160, PURPLE)
    text(c, "dedutivo, indutivo e implícito", 90, 860, 50, "extrabold", INK2, align="left")


def capa_mas(c):
    background(c); selo(c); painel(c)
    linhas = ["Há quem veja a feira", "como coisa do passado.", "MAS", "a feira tem valor", "e deve ficar na rua."]
    for j, s in enumerate(linhas):
        y = 260 + j * 110
        if s == "MAS":
            V.caixa(c, 1385, y - 60, 170, 84, GREEN, 1, "", 0)
            text(c, s, 1470, y, 56, "black", GREEN)
        else:
            col = INK2 if j < 2 else BLUE
            text(c, s, 1470, y, 44, "black", col)
            if j < 2:
                line(c, 1200, y - 16, 1740, y - 22, RED, 1, 6)
    big(c, "LEIA ATÉ O", 340)
    big(c, "PRIMEIRO", 470)
    boxed(c, "“MAS”", 70, 520, 160, GREEN)
    text(c, "a regra que acha a tese no ENEM", 90, 860, 50, "extrabold", INK2, align="left")


if __name__ == "__main__":
    for nome, fn in (("capa_A_primeira_frase", capa_primeira), ("capa_B_comeco_fim_nenhum", capa_onde), ("capa_C_leia_ate_o_mas", capa_mas)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
