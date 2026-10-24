"""Capas — Comparação de Propostas e Tomada de Decisão, Episódio 3: investimentos líquidos e custos escondidos (tema claro).
3 variações em 1280x720.
Formatos: A = três cartazes de banco inclinados ocupando a metade de baixo (1% ao mês, 12,5% ao ano, 6% ao semestre) e
"QUAL PAGA MAIS?" enorme em cima; B = a pilha de R$ 10.000 com o rendimento em cima e o LEÃO do imposto à direita, com
"O LEÃO MORDE O QUÊ?" à esquerda; C = o banco à esquerda, o envelope de R$ 5.000 perdendo "− R$ 100" na porta e
"A TARIFA NA PORTA" com "quanto custou de verdade?". Nenhuma mostra a resposta."""
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


def fit(s, size, maxw, peso="black"):
    while text_w(s, peso, size) > maxw:
        size -= 4
    return size


def selo_topo(c, cx=None):
    s = "MATEMÁTICA ENEM · COMPARAÇÃO DE PROPOSTAS · EP. 3"
    if cx is None:
        pill(c, s, 84, 90, BLUE, size=32, bounds=(0, 1920))
    else:
        pill(c, s, cx, 90, BLUE, size=32, anchor="center", bounds=(0, 1920))


def capa_cartazes(c):
    background(c); selo_topo(c, W / 2)
    s = "QUAL PAGA MAIS?"
    text(c, s, W / 2, 330, fit(s, 190, 1760), "black", INK)
    for k, (bc, tx, per, col, rot) in enumerate((("BANCO P", "1%", "ao mês", BLUE, -4),
                                                ("BANCO Q", "12,5%", "ao ano", PURPLE, 2),
                                                ("BANCO R", "6%", "ao semestre", GREEN, -2))):
        V.cartaz(c, 360 + k * 600, 720, bc, tx, per, col, 1.0, w=520, h=420, rot=rot)


def capa_leao(c):
    background(c); selo_topo(c)
    text(c, "O LEÃO", 84, 360, 170, "black", INK, align="left")
    text(c, "MORDE", 84, 540, 170, "black", AMBER, align="left")
    text(c, "O QUÊ?", 84, 720, 170, "black", AMBER, align="left")
    text(c, "rendimento bruto × líquido", 84, 850, 54, "extrabold", INK2, align="left")
    V.pilha(c, 1300, 960, 1.0, mordida=0.0, w=520, h_base=420, h_top=150, rotulos=False)
    V.leao(c, 1740, 330, 110, 1.0, boca=1.0)


def capa_tarifa(c):
    background(c); selo_topo(c)
    text(c, "A TARIFA", 84, 330, 150, "black", INK, align="left")
    text(c, "NA PORTA", 84, 490, 150, "black", RED, align="left")
    text(c, "quanto o empréstimo custou de verdade?", 84, 600, 52, "extrabold", INK2, align="left")
    rrect(c, 120, 680, 320, 360, 24, mix("#FFFFFF", INK2, 0.12), stroke=6, stroke_color=INK2)
    text(c, "BANCO", 280, 750, 46, "black", INK2)
    V.envelope(c, 760, 900, "R$ 5.000", BLUE, 1.0, w=460, h=280)
    pill(c, "− R$ 100", 760, 715, RED, size=60, anchor="center", bounds=(0, 1920))
    text_mid(c, "4% ao mês?", 1530, 860, fit("4% ao mês?", 130, 640), "black", AMBER)


if __name__ == "__main__":
    for nome, fn in (("capa_A_qual_paga_mais", capa_cartazes), ("capa_B_leao_morde", capa_leao),
                     ("capa_C_tarifa_na_porta", capa_tarifa)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
