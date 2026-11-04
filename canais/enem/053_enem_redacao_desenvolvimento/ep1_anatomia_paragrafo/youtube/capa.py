"""Capas — Redação ENEM, Desenvolvimento, Episódio 1: as cinco partes do parágrafo (tema claro). 3 variações em 1280x720."""
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
    pill(c, "REDAÇÃO ENEM · DESENVOLVIMENTO · EP. 1", 84, 90, BLUE, size=40, bounds=(0, 1920))


def painel(c):
    card(c, 1120, 120, 700, 840, r=36)


def capa_prova(c):
    background(c); selo(c); painel(c)
    V.ficha_entrega(c, 1150, 170, 640, 1.0, rowh=128, partes=0, ok=[1] * 5, title="O PARÁGRAFO")
    big(c, "SEU PARÁGRAFO", 340)
    big(c, "PROVA A TESE", 470)
    boxed(c, "OU SÓ REPETE?", 70, 520, 120, RED)
    text(c, "as 5 partes do desenvolvimento, do zero", 90, 860, 46, "extrabold", INK2, align="left")


def capa_partes(c):
    background(c); selo(c); painel(c)
    for k, key in enumerate(V.KEYS):
        y = 230 + k * 150
        V.icone_etapa(c, key, 1230, y, 1, 1.25)
        text(c, V.NOMEP[key], 1310, y + 6, 48, "black", V.PARTE[key], align="left")
        text(c, "“" + V.PERGP[key] + "”", 1310, y + 50, 28, "bold", INK2, align="left")
    big(c, "AS 5 PARTES DO", 340)
    big(c, "PARÁGRAFO", 470)
    boxed(c, "DE DESENVOLVIMENTO", 70, 530, 84, GREEN)
    text(c, "e a pergunta que cada uma responde", 90, 860, 46, "extrabold", INK2, align="left")


def capa_caixa(c):
    background(c); selo(c); painel(c)
    V.caixa(c, 1270, 470, 400, 330, 1.0, open_=1.0)
    V.icone_etapa(c, "analise", 1470, 360, 1.0, 2.2, disc=False)
    V.selo(c, 1470, 830, 1, "ENTREGA COMPLETA", GREEN, -6, 46)
    big(c, "NÃO DEIXE A", 340)
    big(c, "CAIXA FECHADA", 470)
    boxed(c, "ENTREGUE O ITEM", 70, 530, 96, V.MOV["tese"])
    text(c, "cada parágrafo entrega um item", 90, 860, 46, "extrabold", INK2, align="left")


if __name__ == "__main__":
    for nome, fn in (("capa_A_prova_ou_repete", capa_prova), ("capa_B_5_partes", capa_partes), ("capa_C_caixa_fechada", capa_caixa)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
