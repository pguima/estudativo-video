"""Capas — Velocidade, Densidade e Vazão, Episódio 6: Revisão geral (tema claro). 3 variações em 1280x720.
Evita os formatos das revisões 018–026 ("N PEGADINHAS", "5 QUESTÕES ...", "VERDADEIRO OU FALSO?", "3 HÁBITOS...",
"A MESMA ESCALA CAI NAS DUAS PROVAS", "AMPLIOU O MAPA") e as capas dos eps 1–5 desta série (média 60/40, 30 min = 0,30 h).
Nenhuma entrega gabarito das 5 questões inéditas."""
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


def capa_uma_conta(c):
    background(c); selo(c); painel(c)
    V.velocimetro(c, 1300, 300, 110, 1)
    V.aquario(c, 1640, 270, 0.75, 1)
    V.mapa(c, 1190, 420, 260, 170, 1)
    V.tanque(c, 1640, 520, 0.55, 1, 4, 0.5)
    K.fr(c, "quanto", "por unidade", 1470, 790, 64, PURPLE)
    big(c, "FÍSICA, QUÍMICA", 330, size=120)
    big(c, "E GEOGRAFIA", 470)
    boxed(c, "NUMA CONTA SÓ", 70, 520, 140, PURPLE)
    text(c, "revisão de velocidade, densidade e vazão", 90, 860, 44, "extrabold", INK2, align="left")


def capa_ralo(c):
    background(c); selo(c); painel(c)
    V.tanque(c, 1470, 470, 1.3, 1, 4, 0.35)
    V.torneira(c, 1380, 280, 1.1, 1)
    K.fmid(c, "+", 1250, 300, 90, "black", GREEN)
    rrect(c, 1450, 640, 40, 50, 6, INK2)
    K.fmid(c, "−", 1560, 700, 90, "black", RED)
    text(c, "o tanque enche quando?", 1470, 880, 40, "black", AMBER)
    big(c, "TORNEIRA SOMA.", 330, size=120)
    big(c, "E O RALO?", 470)
    boxed(c, "PEGADINHA DO ENEM", 70, 520, 120, RED)
    text(c, "revisão de velocidade, densidade e vazão", 90, 860, 44, "extrabold", INK2, align="left")


def capa_vinte(c):
    background(c); selo(c); painel(c)
    V.velocimetro(c, 1470, 420, 240, 1, 0.3)
    K.fmid(c, "20 m/s", 1470, 560, 96, "black", INK)
    K.fmid(c, "×", 1470, 670, 60, "black", GRAY)
    K.fmid(c, "60 km/h", 1470, 770, 96, "black", INK)
    big(c, "QUAL CARRO", 330)
    big(c, "É MAIS RÁPIDO?", 470)
    boxed(c, "NÃO É O QUE PARECE", 70, 520, 120, AMBER)
    text(c, "revisão de velocidade, densidade e vazão", 90, 860, 44, "extrabold", INK2, align="left")


if __name__ == "__main__":
    for nome, fn in (("capa_A_uma_conta_so", capa_uma_conta), ("capa_B_torneira_e_ralo", capa_ralo),
                     ("capa_C_qual_mais_rapido", capa_vinte)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
