"""Capas do vídeo Seguridade 011 — Empregado, doméstico e avulso (tema 'seguridade'). Gera 3 variações em 1280x720."""
import subprocess, sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(next(d / "_ferramentas" for d in HERE.parents if (d / "_ferramentas").is_dir())))
import skia
import motor
motor.set_theme("seguridade")
from motor import *  # noqa

PREST, ASSIST, GEST, CI = "#0F766E", "#E8A317", "#4F46E5", "#3A3A3C"


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


def capa_dois_dias(c):
    background(c); selo(c); painel(c)
    dias = ["S", "T", "Q", "Q", "S", "S", "D"]
    for row, (n, lab, col) in enumerate(((2, "DIARISTA", CI), (3, "DOMÉSTICA", GEST))):
        y = 230 + row * 330
        for k, d in enumerate(dias):
            rrect(c, 1170 + k * 86, y, 74, 74, 12, col if k < n else "#EDEDEA")
            text_mid(c, d, 1170 + k * 86 + 37, y + 37, 30, "black", "#FFFFFF" if k < n else GRAY)
        text(c, f"{n} dias", 1470, y + 150, 44, "black", INK2)
        rrect(c, 1250, y + 180, 440, 90, 20, col)
        text_mid(c, lab, 1470, y + 225, 46, "black", "#FFFFFF")
    text(c, "2 OU 3 DIAS?", 80, 330, 124, "black", INK, align="left")
    text(c, "MUDA TUDO", 80, 460, 124, "black", INK, align="left")
    boxed(c, "NO INSS", 70, 510, 140, GEST)
    text(c, "empregado, doméstico e avulso", 90, 820, 54, "extrabold", INK2, align="left")


def capa_perguntas(c):
    background(c); selo(c); painel(c)
    rows = (("SUBORDINAÇÃO?", "EMPREGADO", PREST), ("RESIDÊNCIA?", "DOMÉSTICO", GEST), ("INTERMEDIAÇÃO?", "AVULSO", ASSIST))
    for k, (q, r, col) in enumerate(rows):
        y = 200 + k * 250
        text(c, q, 1470, y + 50, 50, "black", INK)
        rrect(c, 1250, y + 90, 440, 100, 22, col)
        text_mid(c, r, 1470, y + 140, 50, "black", "#FFFFFF")
    text(c, "3 PERGUNTAS", 80, 330, 124, "black", INK, align="left")
    text(c, "PARA NÃO", 80, 460, 124, "black", INK, align="left")
    boxed(c, "ERRAR", 70, 510, 140, RED)
    text(c, "como enquadrar o segurado · INSS", 90, 820, 54, "extrabold", INK2, align="left")


def capa_vereador(c):
    background(c); selo(c); painel(c)
    text(c, "vereador", 1470, 300, 60, "black", INK2)
    text(c, "sem regime próprio", 1470, 370, 40, "bold", GRAY)
    text(c, "=", 1470, 500, 110, "black", INK)
    rrect(c, 1220, 560, 500, 120, 24, PREST)
    text_mid(c, "EMPREGADO", 1470, 620, 62, "black", "#FFFFFF")
    text(c, "não é contribuinte", 1470, 780, 40, "black", RED)
    text(c, "individual!", 1470, 830, 40, "black", RED)
    text(c, "O VEREADOR", 80, 330, 124, "black", INK, align="left")
    text(c, "É SEGURADO", 80, 460, 124, "black", INK, align="left")
    boxed(c, "EMPREGADO?", 70, 510, 132, PREST)
    text(c, "as pegadinhas do art. 11 · Lei 8.213", 90, 820, 54, "extrabold", INK2, align="left")


if __name__ == "__main__":
    for nome, fn in (("capa_A_dois_ou_tres_dias", capa_dois_dias), ("capa_B_tres_perguntas", capa_perguntas),
                     ("capa_C_vereador_empregado", capa_vereador)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
