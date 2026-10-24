"""Capas — Divisão Proporcional, Episódio 3: divisão composta e regra de sociedade (tema claro). 3 variações em 1280x720."""
import importlib.util, subprocess, sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(next(d / "_ferramentas" for d in HERE.parents if (d / "_ferramentas").is_dir())))
import skia
import motor
motor.set_theme("claro")
from motor import *  # noqa

_spec = importlib.util.spec_from_file_location("visual_ep3", HERE.parent / "roteiro" / "visual.py")
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
    pill(c, "MATEMÁTICA ENEM · DIVISÃO PROPORCIONAL · EP. 3", 84, 90, BLUE, size=36, bounds=(0, 1920))


def painel(c):
    card(c, 1120, 120, 700, 840, r=36)


def capa_somar(c):
    background(c); selo(c); painel(c)
    K.ftext(c, "5 + 2 = 7", 1470, 260, 84, "black", RED)
    strike(c, 1290, 232, 1650, 232, 1.0, RED, 1.0)
    V.quadros(c, 1200, 340, 5, 2, 108, 1.0, 1.0, GREEN)
    text(c, "5 pessoas × 2 dias", 1470, 620, 40, "black", INK2)
    K.ftext(c, "= 10 pessoa-dia", 1470, 720, 64, "black", GREEN)
    text(c, "multiplique, nunca some", 1470, 860, 40, "black", PURPLE)
    big(c, "PESSOAS E DIAS?", 330)
    big(c, "NÃO SOME:", 470)
    boxed(c, "MULTIPLIQUE", 70, 520, 170, GREEN)
    text(c, "divisão composta sem cair na armadilha", 90, 860, 44, "extrabold", INK2, align="left")


def capa_capital(c):
    background(c); selo(c); painel(c)
    V.area(c, 1240, 520, 20 * 13, 12 * 22, 1.0, V.AZUL_EQ, "R$ 20 mil", "12 meses", 1.0, "240 mil")
    V.area(c, 1240, 860, 30 * 13, 8 * 22, 1.0, V.LARANJA, "R$ 30 mil", "8 meses", 1.0, "240 mil")
    fmid(c, "=", 1640, 400, 110, "black", GREEN)
    text(c, "partes IGUAIS", 1640, 500, 30, "black", GREEN)
    big(c, "QUEM PÕE MAIS", 330)
    big(c, "NEM SEMPRE", 470)
    boxed(c, "LEVA MAIS", 70, 520, 170, AMBER)
    text(c, "regra de sociedade: capital × tempo", 90, 860, 44, "extrabold", INK2, align="left")


def capa_lucro(c):
    background(c); selo(c); painel(c)
    vals, rots = [30, 45, 75], ["30 mil", "45 mil", "75 mil"]
    for j, (v, r, col) in enumerate(zip(vals, rots, V.CORES_EQ)):
        h = v * 6.4
        x = 1200 + j * 200
        rrect(c, x, 700 - h, 150, h, 14, col)
        K.ftext(c, r, x + 75, 700 - h - 18, 34, "black", col)
        chip(c, ["2", "3", "5"][j], x + 75, 780, GREEN, 1.0, 48)
    text(c, "o lucro segue o capital", 1470, 890, 38, "black", PURPLE)
    big(c, "DIVIDIR O LUCRO", 330)
    big(c, "ENTRE SÓCIOS", 470)
    boxed(c, "SEM ERRO", 70, 520, 170, PURPLE)
    text(c, "regra de sociedade, do zero", 90, 860, 44, "extrabold", INK2, align="left")


fmid, chip, strike = K.fmid, K.chip, V.strike

if __name__ == "__main__":
    for nome, fn in (("capa_A_nao_some_multiplique", capa_somar), ("capa_B_quem_poe_mais", capa_capital),
                     ("capa_C_lucro_entre_socios", capa_lucro)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
