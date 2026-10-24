"""Capas — Função Modular e Funções por Partes, Episódio 2: faixas progressivas (tema claro).
3 variações em 1280x720. Formatos: A = a ESCADA DE CAIXINHAS à direita, com as três fatias do lucro já caídas (isento,
10%, 20%) e a pergunta "20% SOBRE TUDO?" à esquerda; B = uma linha de enunciado gigante com a palavra "EXCEDENTE"
grifada em âmbar e o selo "A PALAVRA QUE MUDA A CONTA"; C = a conta de água: o consumo de 26 m³ como barra em três
faixas (10 · 10 · 6) com "R$ ???" e o título "QUANTO CUSTA A ÁGUA?". Nenhuma mostra gabarito."""
import importlib.util, subprocess, sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(next(d / "_ferramentas" for d in HERE.parents if (d / "_ferramentas").is_dir())))
import skia
import motor
motor.set_theme("claro")
from motor import *  # noqa

_spec = importlib.util.spec_from_file_location("visual_ep2", HERE.parent / "roteiro" / "visual.py")
V = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(V)
motor.set_theme("claro")


def fit(s, size, maxw, peso="black"):
    while text_w(s, peso, size) > maxw:
        size -= 4
    return size


def selo_topo(c, cx=None):
    s = "MATEMÁTICA ENEM · FUNÇÕES POR PARTES · EP. 2"
    if cx is None:
        pill(c, s, 84, 90, BLUE, size=34, bounds=(0, 1920))
    else:
        pill(c, s, cx, 90, BLUE, size=34, anchor="center", bounds=(0, 1920))


def capa_escada(c):
    background(c); selo_topo(c)
    text(c, "IMPOSTO", 84, 330, 140, "black", INK, align="left")
    text(c, "DE 20%:", 84, 480, 140, "black", INK, align="left")
    text(c, "SOBRE TUDO?", 84, 640, fit("SOBRE TUDO?", 140, 860), "black", RED, align="left")
    text(c, "lucro de R$ 7.000", 84, 790, 56, "extrabold", INK2, align="left")
    V.barra_cortada(c, 980, 300, 860, V.F7000, 1.0, corte=1, queda=1, caixas=1, tam=1, imp=0, h=110, base=1000,
                    degrau=120, titulo="")
    xs, ws = V._geo(980, 860, V.F7000, 34)
    for k in range(3):
        text_mid(c, "?", xs[k] + ws[k] / 2, 1000 - 200 - k * 120 + 172, 64, "black", [INK2, BLUE, PURPLE][k])


def capa_palavra(c):
    background(c); selo_topo(c, W / 2)
    s1 = "R$ 9,00 por m³ que"
    text(c, s1, W / 2, 330, fit(s1, 120, 1700), "black", INK2)
    s2 = "EXCEDER"
    sz = fit(s2, 260, 1600)
    tw = text_w(s2, "black", sz)
    rrect(c, W / 2 - tw / 2 - 40, 400, tw + 80, sz * 1.05, 30, AMBER, 0.28)
    text_mid(c, s2, W / 2, 400 + sz * 0.52, sz, "black", AMBER)
    V.selo(c, W / 2, 860, 1.0, "A PALAVRA QUE MUDA A CONTA", RED, -3, 64)


def capa_agua(c):
    background(c); selo_topo(c)
    s = "QUANTO CUSTA A ÁGUA?"
    text(c, s, 84, 330, fit(s, 150, 1750), "black", INK, align="left")
    x0, y0, w = 120, 480, 1680
    partes = [(10, "10 m³", V.ISENTO, "mínima R$ 40"), (10, "10 m³", BLUE, "R$ 6 por m³"), (6, "6 m³", PURPLE, "R$ 9 por m³")]
    xx = x0
    for val, rot, col, sub in partes:
        ww = (w - 60) * val / 26
        rrect(c, xx, y0, ww, 170, 24, col, 0.95)
        text_mid(c, rot, xx + ww / 2, y0 + 85, 76, "black", "#FFFFFF")
        text(c, sub, xx + ww / 2, y0 + 240, 48, "black", col if col != V.ISENTO else INK2)
        xx += ww + 30
    pill(c, "26 m³  =  R$ ???", W / 2, 900, RED, size=72, anchor="center", bounds=(0, 1920))


if __name__ == "__main__":
    for nome, fn in (("capa_A_sobre_tudo", capa_escada), ("capa_B_palavra_excedente", capa_palavra),
                     ("capa_C_conta_de_agua", capa_agua)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
