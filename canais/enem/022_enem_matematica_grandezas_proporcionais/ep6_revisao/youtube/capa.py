"""Capas — Grandezas Proporcionais, Episódio 6: Revisão geral (tema claro). 3 variações em 1280x720.
Evita os formatos já usados nas revisões 019, 020 e 021 ("N PEGADINHAS: QUANTAS VOCÊ ACERTA?", "VOCÊ ESTÁ PRONTO?",
"VERDADEIRO OU FALSO? 9 PEGADINHAS")."""
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
    pill(c, "MATEMÁTICA ENEM · EPISÓDIO 6", 84, 90, BLUE, size=40, bounds=(0, 1920))


def painel(c):
    card(c, 1120, 120, 700, 840, r=36)


def capa_proporcional(c):
    background(c); selo(c); painel(c)
    V.mini_tab(c, 1250, 200, [("2", "9"), ("4", "18"), ("6", "27")], 1, BLUE, rh=70, wc=(150, 170), size=48)
    V.mini_graf(c, 1470, 690, "fixa", 1, 420, 250, AMBER)
    K.fmid(c, "?", 1700, 300, 110, "black", AMBER)
    big(c, "PROPORCIONAL", 340)
    big(c, "OU NÃO?", 470)
    boxed(c, "EM 5 SEGUNDOS", 70, 520, 140, GREEN)
    text(c, "revisão completa: tabela, gráfico e fórmula", 90, 860, 46, "extrabold", INK2, align="left")


def capa_formatos(c):
    background(c); selo(c); painel(c)
    V.mini_tab(c, 1320, 190, [("1", "24"), ("3", "8"), ("6", "4")], 1, BLUE, rh=56, wc=(110, 130), size=40)
    V.mini_graf(c, 1470, 530, "hiper", 1, 300, 170, V.INV)
    K.expr(c, "R = k · L/A", 1470, 800, 80, 1, cores={0: INK, 1: INK, 2: PURPLE, 3: INK, 4: V.DIR})
    big(c, "TABELA, GRÁFICO", 340)
    big(c, "E FÓRMULA", 470)
    boxed(c, "COMO O ENEM COBRA", 70, 520, 120, BLUE)
    text(c, "revisão de grandezas proporcionais", 90, 860, 46, "extrabold", INK2, align="left")


def capa_cinco(c):
    background(c); selo(c); painel(c)
    itens = ["tabela", "conta de água", "máquinas", "pressão", "caixa de som"]
    for k, s in enumerate(itens):
        y = 210 + k * 150
        K.chip(c, str(k + 1), 1200, y, BLUE, 1, 44)
        K.fmid(c, s, 1260, y, 42, "black", INK, align="left")
        K.fmid(c, "?", 1730, y, 52, "black", AMBER)
    big(c, "5 QUESTÕES", 340)
    big(c, "INÉDITAS", 470)
    boxed(c, "DE PROPORÇÃO", 70, 520, 140, AMBER)
    text(c, "resolvidas passo a passo, estilo ENEM", 90, 860, 46, "extrabold", INK2, align="left")


if __name__ == "__main__":
    for nome, fn in (("capa_A_proporcional_ou_nao", capa_proporcional), ("capa_B_tabela_grafico_formula", capa_formatos),
                     ("capa_C_5_questoes_ineditas", capa_cinco)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
