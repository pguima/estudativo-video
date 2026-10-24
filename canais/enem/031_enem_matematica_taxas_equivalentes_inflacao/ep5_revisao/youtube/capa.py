"""Capas — Taxas Equivalentes e Inflação, Episódio 5: revisão, 9 pegadinhas e 5 questões inéditas (tema claro).
3 variações em 1280x720. Formatos: A = a pergunta "A INFLAÇÃO CAIU. OS PREÇOS CAÍRAM?" à esquerda e, à direita, o gráfico
de barras em queda (6% · 4% · 2%) sobre a escada rolante; B = holerite gigante à direita com "+8%" e a etiqueta "inflação 20%",
com a pergunta "SEU SALÁRIO GANHOU OU PERDEU?" empilhada à esquerda; C = os 4 ícones dos episódios em grade 2 × 2 em volta
da ficha "FATORES". Nenhuma mostra gabarito."""
import importlib.util, subprocess, sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(next(d / "_ferramentas" for d in HERE.parents if (d / "_ferramentas").is_dir())))
import skia
import motor
motor.set_theme("claro")
from motor import *  # noqa

_spec = importlib.util.spec_from_file_location("visual_ep5", HERE.parent / "roteiro" / "visual.py")
V = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(V)
motor.set_theme("claro")


def fit(s, size, maxw, peso="black"):
    while text_w(s, peso, size) > maxw:
        size -= 4
    return size


def selo_topo(c, cx=None):
    s = "MATEMÁTICA ENEM · TAXAS E INFLAÇÃO · REVISÃO"
    if cx is None:
        pill(c, s, 84, 90, BLUE, size=34, bounds=(0, 1920))
    else:
        pill(c, s, cx, 90, BLUE, size=34, anchor="center", bounds=(0, 1920))


def capa_queda(c):
    background(c); selo_topo(c)
    text(c, "A INFLAÇÃO", 84, 330, 130, "black", INK, align="left")
    text(c, "CAIU.", 84, 470, 130, "black", RED, align="left")
    text(c, "OS PREÇOS", 84, 640, 110, "black", INK, align="left")
    text(c, "CAÍRAM?", 84, 770, 110, "black", AMBER, align="left")
    text(c, "9 pegadinhas · 5 questões estilo ENEM", 84, 920, 50, "extrabold", INK2, align="left")
    c.save(); c.translate(1470, 470); c.scale(2.2, 2.2); V.escada(c, 0.35); c.restore()
    c.save(); c.translate(1470, 700); c.scale(2.6, 2.6); V.contexto(c, 4, 1.0); c.restore()
    V.selo(c, 1180, 990, 1.0, "PEGADINHA", AMBER, -8, 50)


def capa_salario(c):
    background(c); selo_topo(c)
    text(c, "SEU SALÁRIO", 84, 330, fit("SEU SALÁRIO", 140, 1000), "black", INK, align="left")
    text(c, "GANHOU", 84, 490, 140, "black", GREEN, align="left")
    text(c, "OU PERDEU?", 84, 650, 140, "black", RED, align="left")
    text(c, "revisão de taxas e inflação", 84, 800, 56, "extrabold", INK2, align="left")
    text(c, "com 5 questões inéditas", 84, 880, 56, "extrabold", BLUE, align="left")
    c.save(); c.translate(1480, 520); c.scale(3.0, 3.0); c.rotate(3); V.contexto(c, 3, 1.0); c.restore()
    c.save(); c.translate(1480, 900); c.rotate(-5); V.etiqueta(c, 1.0, "inflação 20%", RED, 460, 120); c.restore()


def capa_fatores(c):
    background(c); selo_topo(c, W / 2)
    for k, (x, y) in enumerate(((300, 340), (1620, 340), (300, 850), (1620, 850))):
        c.save(); c.translate(x, y); c.scale(1.25, 1.25); V.icone(c, k, 0, 0, 1.0, 1.0); c.restore()
    c.save(); c.translate(W / 2, 520); c.scale(2.6, 2.6); V.fator(c, 1.0, "FATORES", PURPLE); c.restore()
    text(c, "1 ideia resolve tudo", W / 2, 720, 64, "black", INK, align="center")
    text(c, "revisão completa", W / 2, 990, 56, "extrabold", GREEN, align="center")


if __name__ == "__main__":
    for nome, fn in (("capa_A_inflacao_caiu", capa_queda), ("capa_B_salario_ganhou", capa_salario),
                     ("capa_C_fatores", capa_fatores)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
