"""Capas — Redação ENEM, Desenvolvimento, Episódio 6: Oficina — o 2º parágrafo em cinco linhas (tema claro).
3 variações em 1280x720."""
import importlib.util, subprocess, sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(next(d / "_ferramentas" for d in HERE.parents if (d / "_ferramentas").is_dir())))
import skia
import motor
motor.set_theme("claro")
from motor import *  # noqa

_spec = importlib.util.spec_from_file_location("visual_ep6", HERE.parent / "roteiro" / "visual.py")
V = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(V)
motor.set_theme("claro")


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
    pill(c, "REDAÇÃO ENEM · DESENVOLVIMENTO · EP. 6", 84, 90, BLUE, size=40, bounds=(0, 1920))


def painel(c):
    card(c, 1120, 120, 700, 840, r=36)


def capa_cinco_linhas(c):
    background(c); selo(c); painel(c)
    V.lista(c, 0.0, 1.0, x=1160, y=180, w=620, ok=[1, 1, 0, 1, 1], aberto=[0, 0, 1, 0, 0], title="LISTA DE COMPRAS DO PARÁGRAFO")
    big(c, "PLANEJE EM", 340)
    big(c, "5 LINHAS", 480, size=150)
    boxed(c, "ANTES DE ESCREVER", 70, 530, 96, GREEN)
    text(c, "o 2º desenvolvimento da redação, do zero", 90, 860, 46, "extrabold", INK2, align="left")


def capa_escreva(c):
    background(c); selo(c); painel(c)
    V.paper(c, 1160, 170, 620, 740, 1.0, lh=110, top=330, rot=2)
    V.hand(c, "2º desenvolvimento", 1250, 270, 44, V.PEN, 1.0, bold=True)
    for k, (lab, _, key) in enumerate(V.RASCUNHO):
        y = 360 + k * 110
        V.hand(c, lab, 1250, y, 40, V.PARTE[key], 1.0, bold=True)
        if k == 2:
            V.hand(c, "[seu exemplo]", 1480, y, 34, AMBER, 1.0, bold=True)
        else:
            line(c, 1480, y + 4, 1720 - (k % 2) * 60, y + 4, V.PEN, 0.55, 5)
    V.pen_draw(c, 1720, 300, V.PEN, 1.0, -30, 1.1)
    big(c, "ESCREVA COMIGO", 340)
    big(c, "O 2º PARÁGRAFO", 480)
    boxed(c, "AO VIVO", 70, 530, 130, V.PARTE["analise"])
    text(c, "oficina com papel e caneta, passo a passo", 90, 860, 44, "extrabold", INK2, align="left")


def capa_linha_vazia(c):
    background(c); selo(c); painel(c)
    V.paper(c, 1160, 170, 620, 740, 1.0, lh=120, top=330, rot=0)
    for k, (lab, _, key) in enumerate(V.RASCUNHO):
        y = 330 + k * 120
        V.hand(c, lab, 1230, y, 40, V.PARTE[key], 1.0, bold=True)
        if k == 3:
            V.dashed_box(c, 1440, y - 44, 300, 64, RED, 1.0)
            text(c, "vazia!", 1466, y + 0, 34, "black", RED, 1.0, align="left")
            check_icon(c, 1700, y - 12, 22, 1.0, RED, "x")
        else:
            line(c, 1450, y + 4, 1730 - (k % 2) * 70, y + 4, V.PEN, 0.55, 5)
    big(c, "LINHA VAZIA?", 340)
    big(c, "PARÁGRAFO", 480)
    boxed(c, "NÃO ESTÁ PRONTO", 70, 530, 104, RED)
    text(c, "o teste das 5 linhas antes de escrever", 90, 860, 50, "extrabold", INK2, align="left")


if __name__ == "__main__":
    for nome, fn in (("capa_A_cinco_linhas", capa_cinco_linhas), ("capa_B_escreva_comigo", capa_escreva),
                     ("capa_C_linha_vazia", capa_linha_vazia)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
