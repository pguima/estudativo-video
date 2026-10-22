"""Capas do vídeo Seguridade 016 — Filiação × inscrição (tema 'seguridade'). Gera 3 variações em 1280x720."""
import subprocess, sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(next(d / "_ferramentas" for d in HERE.parents if (d / "_ferramentas").is_dir())))
import skia
import motor
motor.set_theme("seguridade")
from motor import *  # noqa

PREST, ASSIST, GEST = "#0F766E", "#E8A317", "#4F46E5"
FIL, INS, FAC = PREST, GEST, ASSIST


def boxed(c, s, x, y, size, bg_col, fg="#FFFFFF", pad=34):
    w = text_w(s, "black", size) + pad * 2
    h = size * 1.22
    shadow_rrect(c, x, y, w, h, 22, 1, 1.4)
    rrect(c, x, y, w, h, 22, bg_col)
    text_mid(c, s, x + w / 2, y + h / 2, size, "black", fg)


def selo(c):
    pill(c, "SEGURIDADE SOCIAL · INSS", 84, 90, BLUE, size=40, bounds=(0, 1920))


def painel(c):
    card(c, 1120, 120, 700, 840, r=36)


def linha_ok(c, s, y, ok, size=44):
    text(c, s, 1190, y, size, "black", INK, align="left")
    check_icon(c, 1740, y - 15, 30, 1, GREEN if ok else RED, "check" if ok else "x")


def capa_lucas(c):
    background(c); selo(c); painel(c)
    text(c, "o caso do Lucas", 1470, 220, 46, "black", GRAY)
    linha_ok(c, "autônomo há 3 anos", 340, True)
    linha_ok(c, "nunca se inscreveu", 460, False)
    linha_ok(c, "nunca recolheu", 580, False)
    text(c, "filiado ao RGPS?", 1190, 700, 44, "black", INK, align="left")
    text_mid(c, "?", 1740, 685, 54, "black", ASSIST)
    rrect(c, 1170, 780, 600, 120, 22, ASSIST)
    text_mid(c, "SIM OU NÃO?", 1470, 840, 48, "black", INK)
    text(c, "NUNCA PAGOU", 80, 330, 120, "black", INK, align="left")
    text(c, "E ESTÁ", 80, 460, 124, "black", INK, align="left")
    boxed(c, "FILIADO?", 70, 510, 140, FIL)
    text(c, "a pegadinha nº 1 dos segurados no INSS", 90, 820, 50, "extrabold", INK2, align="left")


def capa_fato_ficha(c):
    background(c); selo(c); painel(c)
    for k, (top, big, sub, col) in enumerate((("FILIAÇÃO", "o FATO", "filia-se TRABALHANDO", FIL),
                                              ("INSCRIÇÃO", "a FICHA", "inscreve-se CADASTRANDO", INS))):
        y = 170 + k * 390
        rrect(c, 1170, y, 600, 350, 26, col)
        text_mid(c, top, 1470, y + 70, 40, "black", "#FFFFFF")
        text_mid(c, big, 1470, y + 180, 96, "black", "#FFFFFF")
        text_mid(c, sub, 1470, y + 285, 34, "bold", "#FFFFFF")
    text(c, "FILIAÇÃO", 80, 330, 124, "black", INK, align="left")
    text(c, "NÃO É", 80, 460, 124, "black", INK, align="left")
    boxed(c, "INSCRIÇÃO", 70, 510, 140, INS)
    text(c, "o fato e a ficha · art. 17 da Lei 8.213", 90, 820, 52, "extrabold", INK2, align="left")


def capa_declaratoria(c):
    background(c); selo(c); painel(c)
    text(c, "a inscrição é...", 1470, 220, 46, "black", GRAY)
    for k, (who, nat, col, fg) in enumerate((("OBRIGATÓRIO", "DECLARATÓRIA", FIL, "#FFFFFF"),
                                             ("FACULTATIVO", "CONSTITUTIVA", FAC, INK))):
        y = 290 + k * 300
        rrect(c, 1170, y, 600, 250, 26, col)
        text_mid(c, who, 1470, y + 70, 40, "black", fg)
        text_mid(c, nat, 1470, y + 160, 62, "black", fg)
    text(c, "O PONTO DE", 80, 330, 124, "black", INK, align="left")
    text(c, "OURO DA", 80, 460, 124, "black", INK, align="left")
    boxed(c, "FILIAÇÃO", 70, 510, 140, ASSIST, INK)
    text(c, "declaratória × constitutiva · INSS", 90, 820, 50, "extrabold", INK2, align="left")


if __name__ == "__main__":
    for nome, fn in (("capa_A_caso_lucas", capa_lucas), ("capa_B_fato_ficha", capa_fato_ficha),
                     ("capa_C_declaratoria_constitutiva", capa_declaratoria)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
