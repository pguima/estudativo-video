"""Capas — Progressão Aritmética, Episódio 4: a PA disfarçada (tema claro).
3 variações em 1280x720. Formatos: A = a ESCADA do extrato à direita, com o chão de R$ 2.000 marcado "mês 0 ou mês 1?",
e a pergunta "O CAPITAL É O MÊS 1?" à esquerda; B = a folha de calendário grande à esquerda com o dia 4 (terça) e o
dia 29 marcado "?", título "QUE DIA DA SEMANA?" à direita; C = três papéis (extrato, calendário, boleto) lado a lado
sob o título "A PA ESCONDIDA", com uma lupa sobre o do meio. Nenhuma mostra gabarito."""
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
motor.set_theme("claro")


def fit(s, size, maxw, peso="black"):
    while text_w(s, peso, size) > maxw:
        size -= 4
    return size


def selo_topo(c, cx=None):
    s = "MATEMÁTICA ENEM · PROGRESSÃO ARITMÉTICA · EP. 4"
    if cx is None:
        pill(c, s, 84, 90, BLUE, size=34, bounds=(0, 1920))
    else:
        pill(c, s, cx, 90, BLUE, size=34, anchor="center", bounds=(0, 1920))


def capa_escada(c):
    background(c); selo_topo(c)
    text(c, "O CAPITAL", 84, 330, 130, "black", INK, align="left")
    text(c, "É O MÊS 1?", 84, 480, 140, "black", AMBER, align="left")
    text(c, "juros simples escondem uma PA", 84, 610, 50, "extrabold", INK2, align="left")
    itens = [("mês ?", "R$ 2.000"), ("", "R$ 2.060"), ("", "R$ 2.120"), ("", "R$ 2.180")]
    V.escada(c, 1080, 900, itens, 1.0, larg=200, passo=110, size=40)
    rrect(c, 1040, 600, 240, 100, 22, AMBER, 1.0, shadow=True)
    text_mid(c, "mês 0?", 1160, 650, 52, "black", "#FFFFFF")
    arrow(c, 1160, 700, 1170, 790, AMBER, 1.0, 8, 26)


def capa_calendario(c):
    background(c); selo_topo(c)
    V.calendario(c, 120, 330, 1.0, cel=100, acesos={4: 1.0}, cor=BLUE, marcas={29: (AMBER, 1.0)})
    s1 = "DIA 4: TERÇA"
    text(c, s1, 1380, 420, fit(s1, 110, 1000), "black", BLUE)
    s2 = "DIA 29: ?"
    text(c, s2, 1380, 620, fit(s2, 170, 1000), "black", AMBER)
    pill(c, "sem contar dia por dia", 1380, 800, GREEN, size=56, anchor="center", bounds=(0, 1920))


def capa_papeis(c):
    background(c); selo_topo(c, W / 2)
    s = "A PA ESCONDIDA"
    text(c, s, W / 2, 310, fit(s, 170, 1700), "black", INK)
    V.extrato(c, 120, 420, 1.0, w=500)
    V.calendario(c, 760, 500, 1.0, cel=58, acesos={d: 1.0 for d in (3, 10, 17, 24, 31)})
    V.boleto(c, 1300, 420, 1.0, w=500)
    cx, cy, r = 1000, 690, 150
    c.drawCircle(cx, cy, r, paint(GREEN, 0.10))
    c.drawCircle(cx, cy, r, paint(GREEN, 1.0, stroke=16))
    c.drawLine(cx + r * 0.7, cy + r * 0.7, cx + r * 1.35, cy + r * 1.35, paint(GREEN, 1.0, stroke=30, cap_round=True))


if __name__ == "__main__":
    for nome, fn in (("capa_A_capital_mes_1", capa_escada), ("capa_B_que_dia_da_semana", capa_calendario),
                     ("capa_C_pa_escondida", capa_papeis)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
