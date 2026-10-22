"""Capas do vídeo Seguridade 014 — Facultativo, excluídos e o "quem é quem" (tema 'seguridade'). Gera 3 variações em 1280x720."""
import subprocess, sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(next(d / "_ferramentas" for d in HERE.parents if (d / "_ferramentas").is_dir())))
import skia
import motor
motor.set_theme("seguridade")
from motor import *  # noqa

PREST, ASSIST, GEST, ESP = "#0F766E", "#E8A317", "#4F46E5", "#16A36A"
FAC, RPPS, CI = "#0284C7", "#64748B", "#3A3A3C"


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


def capa_renata(c):
    background(c); selo(c); painel(c)
    text(c, "o caso da Renata", 1470, 220, 46, "black", GRAY)
    for k, (mes, s, col) in enumerate((("JAN", "facultativa", FAC), ("JUL", "carteira assinada", PREST))):
        y = 290 + k * 190
        rrect(c, 1170, y, 600, 150, 24, col)
        text_mid(c, mes, 1470, y + 50, 40, "black", "#FFFFFF")
        text_mid(c, s, 1470, y + 105, 40, "black", "#FFFFFF")
    text_mid(c, "e agora?", 1470, 720, 50, "black", INK)
    rrect(c, 1170, 780, 600, 120, 22, ASSIST)
    text_mid(c, "AS DUAS? ESCOLHE?", 1470, 840, 44, "black", INK)
    text(c, "ELA AINDA É", 80, 330, 124, "black", INK, align="left")
    text(c, "SEGURADA", 80, 460, 124, "black", INK, align="left")
    boxed(c, "FACULTATIVA?", 70, 520, 104, FAC)
    text(c, "a pegadinha da filiação no INSS", 90, 820, 52, "extrabold", INK2, align="left")


def capa_idade(c):
    background(c); selo(c); painel(c)
    for k, (n, l1, l2, col) in enumerate((("14", "LEI 8.213, ART. 13", "literalidade (1991)", RPPS),
                                          ("16", "DECRETO 3.048", "idade aplicável", FAC))):
        y = 170 + k * 330
        rrect(c, 1170, y, 600, 290, 26, col)
        text_mid(c, n, 1470, y + 110, 130, "black", "#FFFFFF")
        text_mid(c, l1, 1470, y + 210, 34, "black", "#FFFFFF")
        text_mid(c, l2, 1470, y + 252, 28, "bold", "#FFFFFF")
    text_mid(c, "na dúvida: 16", 1470, 880, 48, "black", RED)
    text(c, "14 OU 16", 80, 330, 124, "black", INK, align="left")
    text(c, "ANOS?", 80, 460, 124, "black", INK, align="left")
    boxed(c, "FACULTATIVO", 70, 515, 112, FAC)
    text(c, "a pegadinha mais sofisticada do INSS", 90, 820, 48, "extrabold", INK2, align="left")


def capa_quem(c):
    background(c); selo(c); painel(c)
    text(c, "filiação", 1470, 210, 44, "black", GRAY)
    cats = (("empregado", PREST), ("doméstico", GEST), ("contrib. individual", CI), ("avulso", ASSIST), ("especial", ESP))
    for k, (s, col) in enumerate(cats):
        y = 280 + k * 92
        c.drawCircle(1200, y - 14, 14, paint(col))
        text(c, s, 1230, y, 40, "black", INK, align="left")
        check_icon(c, 1740, y - 14, 26, 1, GREEN)
    rrect(c, 1170, 760, 600, 150, 24, FAC)
    text_mid(c, "FACULTATIVO", 1470, 805, 44, "black", "#FFFFFF")
    text_mid(c, "inscrição + 1ª contribuição", 1470, 865, 32, "bold", "#FFFFFF")
    text(c, "SÓ ELE PAGA", 80, 330, 118, "black", INK, align="left")
    text(c, "PARA", 80, 460, 124, "black", INK, align="left")
    boxed(c, "ENTRAR", 70, 510, 140, ASSIST, INK)
    text(c, "facultativo, excluídos e o quem é quem", 90, 820, 46, "extrabold", INK2, align="left")


if __name__ == "__main__":
    for nome, fn in (("capa_A_caso_renata", capa_renata), ("capa_B_14_ou_16", capa_idade),
                     ("capa_C_so_ele_paga", capa_quem)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
