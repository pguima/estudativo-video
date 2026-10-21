"""Capas do vídeo Seguridade 012 — Contribuinte individual (tema 'seguridade'). Gera 3 variações em 1280x720."""
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


def capa_sindico(c):
    background(c); selo(c); painel(c)
    for k, (s, r, col) in enumerate((("síndico REMUNERADO", "CONTRIBUINTE INDIVIDUAL", CI),
                                     ("isenção da TAXA", "CONTRIBUINTE INDIVIDUAL", CI),
                                     ("NÃO remunerado", "NÃO É SEGURADO", RED))):
        y = 200 + k * 250
        text(c, s, 1470, y + 50, 46, "black", INK)
        rrect(c, 1170, y + 90, 600, 100, 22, col)
        text_mid(c, r, 1470, y + 140, 38, "black", "#FFFFFF")
    text(c, "O SÍNDICO", 80, 330, 124, "black", INK, align="left")
    text(c, "É SEGURADO", 80, 460, 124, "black", INK, align="left")
    boxed(c, "DO INSS?", 70, 510, 140, ASSIST, INK)
    text(c, "contribuinte individual · Lei 8.213", 90, 820, 54, "extrabold", INK2, align="left")


def capa_residual(c):
    background(c); selo(c); painel(c)
    rows = (("subordinação?", "EMPREGADO", PREST), ("intermediação?", "AVULSO", ASSIST), ("rural até 4 MF?", "ESPECIAL", GREEN),
            ("nenhum?", "CONTRIB. INDIVIDUAL", CI))
    for k, (q, r, col) in enumerate(rows):
        y = 190 + k * 185
        text(c, q, 1470, y + 40, 40, "black", INK2)
        rrect(c, 1200, y + 70, 540, 84, 20, col)
        text_mid(c, r, 1470, y + 112, 38, "black", "#FFFFFF")
    text(c, "QUEM NÃO", 80, 330, 124, "black", INK, align="left")
    text(c, "CABE, CAI", 80, 460, 124, "black", INK, align="left")
    boxed(c, "AQUI", 70, 510, 140, CI)
    text(c, "o contribuinte individual do INSS", 90, 820, 54, "extrabold", INK2, align="left")


def capa_recolhe(c):
    background(c); selo(c); painel(c)
    text(c, "serviço a EMPRESA", 1470, 270, 48, "black", INK)
    rrect(c, 1200, 310, 540, 110, 22, PREST)
    text_mid(c, "a EMPRESA recolhe", 1470, 365, 42, "black", "#FFFFFF")
    text(c, "conta própria", 1470, 580, 48, "black", INK)
    rrect(c, 1200, 620, 540, 110, 22, CI)
    text_mid(c, "ELE MESMO recolhe", 1470, 675, 42, "black", "#FFFFFF")
    text(c, "QUEM PAGA O", 80, 330, 124, "black", INK, align="left")
    text(c, "INSS DO", 80, 460, 124, "black", INK, align="left")
    boxed(c, "AUTÔNOMO?", 70, 510, 140, RED)
    text(c, "contribuinte individual · pegadinha da banca", 90, 820, 50, "extrabold", INK2, align="left")


if __name__ == "__main__":
    for nome, fn in (("capa_A_sindico", capa_sindico), ("capa_B_quem_nao_cabe", capa_residual),
                     ("capa_C_quem_recolhe", capa_recolhe)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
