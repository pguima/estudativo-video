"""Capas — Função Logarítmica, Episódio 4: decibéis, por que 80 + 80 não dá 160 (tema claro). 3 variações em 1280x720.
A = duas máquinas de 80 dB e o medidor com "?", título "80 + 80 = 160?" (o 160 em âmbar, sem dizer o valor certo);
B = dois medidores 90 dB × 60 dB com "QUANTAS VEZES MAIS ALTO?" (exemplo do bloco d, sem a resposta);
C = o balde de intensidade com a etiqueta "? dB" e os copos, "DECIBEL NÃO SE SOMA".
Nenhuma mostra gabarito (80 dB, 10 000 vezes e 10 máquinas não aparecem)."""
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
    s = "MATEMÁTICA ENEM · FUNÇÃO LOGARÍTMICA · EP. 4"
    if cx is None:
        pill(c, s, 84, 90, BLUE, size=34, bounds=(0, 1920))
    else:
        pill(c, s, cx, 90, BLUE, size=34, anchor="center", bounds=(0, 1920))


def medidor_q(c, cx, cy, s, txt="?"):
    """medidor com interrogação no visor"""
    w, h = 1.5 * s, 1.15 * s
    rrect(c, cx - w / 2, cy - h / 2, w, h, 0.14 * s, "#2B2F3A", 1, shadow=True)
    rrect(c, cx - w / 2 + 0.1 * s, cy - h / 2 + 0.1 * s, w - 0.2 * s, 0.55 * s, 0.08 * s, "#10141C", 1)
    text_mid(c, txt, cx, cy - h / 2 + 0.38 * s, 0.46 * s, "black", AMBER)
    rrect(c, cx - w / 2 + 0.12 * s, cy + 0.22 * s, w - 0.24 * s, 0.14 * s, 0.07 * s, "#3A4050", 1)


def capa_maquinas(c):
    background(c); selo_topo(c)
    shadow_rrect(c, 70, 190, 900, 820, 40, 1, 1.4)
    rrect(c, 70, 190, 900, 820, 40, "#FFFFFF")
    V.maquina(c, 230, 760, 260, 1)
    V.maquina(c, 680, 760, 260, 1)
    text_mid(c, "80 dB", 230, 940, 64, "black", INK)
    text_mid(c, "80 dB", 680, 940, 64, "black", INK)
    medidor_q(c, 500, 410, 300)
    s1 = "80 + 80"
    text(c, s1, 1430, 420, fit(s1, 190, 820), "black", INK)
    s2 = "= 160?"
    sz = fit(s2, 170, 780)
    ww = text_w(s2, "black", sz) + 80
    shadow_rrect(c, 1430 - ww / 2, 480, ww, 220, 30, 1, 1.4)
    rrect(c, 1430 - ww / 2, 480, ww, 220, 30, AMBER)
    text_mid(c, s2, 1430, 590, sz, "black", "#FFFFFF")
    V.selo(c, 1430, 850, 1.0, "A PEGADINHA DOS DECIBÉIS", RED, -5, 50)


def capa_comparar(c):
    background(c); selo_topo(c, W / 2)
    s = "QUANTAS VEZES MAIS ALTO?"
    text(c, s, W / 2, 300, fit(s, 140, 1780), "black", INK)
    V.medidor(c, 500, 600, 340, 90, 1, rotulo=False)
    V.medidor(c, 1420, 600, 340, 60, 1, rotulo=False)
    text_mid(c, "×  ?", 960, 600, 120, "black", AMBER)
    rrect(c, 0, 900, W, 180, 0, PURPLE)
    text_mid(c, "decibéis: compare sem cair na pegadinha", W / 2, 990, 70, "black", "#FFFFFF")


def capa_balde(c):
    background(c); selo_topo(c, W / 2)
    s = "DECIBEL NÃO SE SOMA"
    text(c, s, W / 2, 290, fit(s, 140, 1780), "black", INK)
    V.balde(c, 600, 700, 380, 0.55, 1, "? dB", PURPLE)
    for k in range(3):
        V.copo(c, 1260 + k * 170, 520, 140, 1)
    text_mid(c, "+", 1430, 700, 110, "black", GREEN)
    text(c, "intensidades se somam", 1430, 800, 44, "black", GREEN)
    rrect(c, 0, 940, W, 140, 0, GREEN)
    text_mid(c, "o balde enche; a etiqueta quase não sobe", W / 2, 1010, 64, "black", "#FFFFFF")


if __name__ == "__main__":
    for nome, fn in (("capa_A_80_mais_80", capa_maquinas), ("capa_B_quantas_vezes", capa_comparar),
                     ("capa_C_balde", capa_balde)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
