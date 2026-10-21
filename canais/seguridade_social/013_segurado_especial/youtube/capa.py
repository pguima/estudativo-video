"""Capas do vídeo Seguridade 013 — Segurado especial (tema 'seguridade'). Gera 3 variações em 1280x720."""
import subprocess, sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(next(d / "_ferramentas" for d in HERE.parents if (d / "_ferramentas").is_dir())))
import skia
import motor
motor.set_theme("seguridade")
from motor import *  # noqa

PREST, ASSIST, GEST, ESP = "#0F766E", "#E8A317", "#4F46E5", "#16A36A"


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


def capa_joao(c):
    background(c); selo(c); painel(c)
    text(c, "o caso do João", 1470, 220, 46, "black", GRAY)
    for k, s in enumerate(("3 módulos fiscais", "5 na safra × 20 dias", "Bolsa Família", "vereador")):
        text(c, s, 1190, 340 + k * 120, 44, "black", INK, align="left")
        text_mid(c, "?", 1740, 325 + k * 120, 50, "black", ASSIST)
    rrect(c, 1170, 780, 600, 120, 22, ASSIST)
    text_mid(c, "PERDEU OU NÃO?", 1470, 840, 44, "black", INK)
    text(c, "ELE AINDA É", 80, 330, 124, "black", INK, align="left")
    text(c, "SEGURADO", 80, 460, 124, "black", INK, align="left")
    boxed(c, "ESPECIAL?", 70, 510, 140, ESP)
    text(c, "o rural que mais cai na prova do INSS", 90, 820, 52, "extrabold", INK2, align="left")


def capa_numeros(c):
    background(c); selo(c); painel(c)
    nums = (("4", "módulos fiscais", ESP), ("16", "anos do filho", PREST), ("3 × 120", "safra · trabalho · turismo", ASSIST),
            ("50%", "cessão do imóvel", GEST))
    for k, (n, sub, col) in enumerate(nums):
        y = 160 + k * 195
        rrect(c, 1170, y, 600, 170, 24, col)
        text_mid(c, n, 1470, y + 70, 78, "black", "#FFFFFF")
        text_mid(c, sub, 1470, y + 138, 30, "bold", "#FFFFFF")
    text(c, "DECORE", 80, 330, 124, "black", INK, align="left")
    text(c, "ESTES", 80, 460, 124, "black", INK, align="left")
    boxed(c, "NÚMEROS", 70, 510, 140, ASSIST, INK)
    text(c, "segurado especial · art. 11, VII", 90, 820, 54, "extrabold", INK2, align="left")


def capa_vereador(c):
    background(c); selo(c); painel(c)
    linha_ok(c, "vereador", 260, True)
    linha_ok(c, "dirigente sindical", 400, True)
    linha_ok(c, "Bolsa Família", 540, True)
    linha_ok(c, "prefeito", 680, False)
    linha_ok(c, "empregado permanente", 820, False, 38)
    text(c, "VEREADOR SIM,", 80, 330, 112, "black", INK, align="left")
    text(c, "PREFEITO", 80, 460, 124, "black", INK, align="left")
    boxed(c, "NÃO", 70, 510, 140, RED)
    text(c, "o que tira (e o que não tira) o segurado especial", 90, 820, 44, "extrabold", INK2, align="left")


if __name__ == "__main__":
    for nome, fn in (("capa_A_caso_joao", capa_joao), ("capa_B_numeros", capa_numeros),
                     ("capa_C_vereador_prefeito", capa_vereador)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
