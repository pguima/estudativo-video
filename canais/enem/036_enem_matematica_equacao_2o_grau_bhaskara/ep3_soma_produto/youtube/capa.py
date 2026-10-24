"""Capas — Equação do 2º Grau e Bhaskara, Episódio 3: soma e produto (tema claro). 3 variações em 1280x720.
Formatos: A = duas cartas viradas gigantes com "?" e as pistas "soma 7" e "produto 10" em cima, título "QUE NÚMEROS SÃO?"
(sem mostrar 2 e 5); B = fundo escuro com a fórmula de Bhaskara riscada e "RAÍZES SEM BHASKARA" em duas linhas, à esquerda;
C = fundo âmbar com "−7x" e "soma +7" lado a lado e "O SINAL DO MEIO VEM TROCADO". Nenhuma mostra gabarito."""
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
SERIE = "MATEMÁTICA ENEM · 2º GRAU · EP. 3"


def fit(s, size, maxw, peso="black"):
    while text_w(s, peso, size) > maxw:
        size -= 4
    return size


def capa_cartas(c):
    background(c)
    pill(c, SERIE, W / 2, 80, BLUE, size=34, anchor="center", bounds=(0, 1920))
    s = "QUE NÚMEROS SÃO?"
    text(c, s, W / 2, 300, fit(s, 160, 1760), "black", INK)
    V.cartas(c, W / 2, 680, ("?", "?"), (0, 0), 1.0, w=300, h=420, gap=120, pistas=("soma 7", "produto 10"),
             a_pistas=(1, 1), pdx=760, psize=60)
    text(c, "as raízes de cabeça", W / 2, 1010, 56, "extrabold", GRAY)


def capa_sem_bhaskara(c):
    rrect(c, 0, 0, W, H, 0, "#1F2A44")
    pill(c, SERIE, 84, 90, BLUE, size=34, bounds=(0, 1920))
    for k, (s, col) in enumerate((("RAÍZES", "#FFFFFF"), ("SEM", AMBER), ("BHASKARA", "#FFFFFF"))):
        text(c, s, 90, 360 + k * 190, fit(s, 190, 900), "black", col, align="left")
    rrect(c, 1080, 300, 740, 420, 36, "#FFFFFF", 1.0, shadow=True)
    V.expr(c, "x = {-b±√{Δ}}/{2a}", 1450, 510, 92, 1.0)
    V.strike(c, 1140, 520, 1760, 470, 1.0, RED)
    V.strike(c, 1140, 470, 1760, 520, 1.0, RED)
    pill(c, "3 segundos de cabeça", 1450, 830, GREEN, size=50, anchor="center", bounds=(0, 1920))


def capa_sinal(c):
    rrect(c, 0, 0, W, H, 0, AMBER)
    pill(c, SERIE, W / 2, 90, INK, size=34, anchor="center", bounds=(0, 1920))
    for k, s in enumerate(("O SINAL DO MEIO", "VEM TROCADO")):
        text(c, s, W / 2, 260 + k * 150, fit(s, 140, 1760), "black", "#FFFFFF" if k == 0 else INK)
    rrect(c, 180, 520, 1560, 420, 40, "#FFFFFF", 1.0, shadow=True)
    V.expr(c, "x^2 - 7x + 10 = 0", W / 2, 640, 110, 1.0, cores={2: RED})
    V.fmid(c, "soma = ?", 640, 840, 80, "black", INK)
    V.fmid(c, "−7?  +7?", 1280, 840, 80, "black", RED)


if __name__ == "__main__":
    for nome, fn in (("capa_A_que_numeros_sao", capa_cartas), ("capa_B_sem_bhaskara", capa_sem_bhaskara),
                     ("capa_C_sinal_trocado", capa_sinal)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
