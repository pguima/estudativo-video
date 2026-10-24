"""Capas — Juros Compostos, Episódio 5: revisão, 9 pegadinhas e 5 questões inéditas (tema claro). 3 variações em 1280x720.
Formatos: A = título à esquerda e uma folha de prova à direita com a potência dada grifada a marca-texto ("a potência vem no
enunciado"); B = bola de neve gigante no centro rolando morro abaixo, com a pergunta no alto e o radar "72 ÷ ?";
C = conta errada enorme no centro ("1,34 × 2 = 2,68?") com o selo PEGADINHA e o placar de 9 frases embaixo.
Nenhuma mostra gabarito."""
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
    s = "MATEMÁTICA ENEM · JUROS COMPOSTOS · REVISÃO"
    if cx is None:
        pill(c, s, 84, 90, BLUE, size=34, bounds=(0, 1920))
    else:
        pill(c, s, cx, 90, BLUE, size=34, anchor="center", bounds=(0, 1920))


def capa_prova(c):
    background(c); selo_topo(c)
    text(c, "A POTÊNCIA", 84, 330, 140, "black", INK, align="left")
    text(c, "VEM NO", 84, 470, 140, "black", INK, align="left")
    text(c, "ENUNCIADO", 84, 610, fit("ENUNCIADO", 140, 900), "black", PURPLE, align="left")
    text(c, "você só precisa saber usar", 84, 760, 56, "extrabold", INK2, align="left")
    text(c, "9 pegadinhas · 5 questões inéditas", 84, 860, 50, "extrabold", GREEN, align="left")
    c.save(); c.translate(1470, 560); c.rotate(-4)
    shadow_rrect(c, -330, -430, 660, 860, 26, 1, 1.6)
    rrect(c, -330, -430, 660, 860, 26, "#FFFFFF")
    text(c, "QUESTÃO 2", -280, -340, 40, "black", BLUE, align="left")
    for j in range(4):
        line(c, -280, -270 + j * 50, 280 - (j == 3) * 160, -270 + j * 50, LIGHT, 1.0, 10)
    rrect(c, -300, -60, 600, 130, 18, "#FFF176", 0.85)
    text_mid(c, "Use: 1,08⁶ ≈ 1,59", 0, 5, 64, "black", INK)
    for j in range(3):
        line(c, -280, 150 + j * 50, 280 - (j == 2) * 220, 150 + j * 50, LIGHT, 1.0, 10)
    for k, L in enumerate("ABCDE"):
        c.drawCircle(-250 + k * 125, 360, 30, paint(INK2, 1.0, stroke=4))
        text_mid(c, L, -250 + k * 125, 360, 30, "black", INK2)
    c.restore()


def capa_bola(c):
    background(c); selo_topo(c, W / 2)
    s = "DOBRA EM QUANTO TEMPO?"
    text(c, s, W / 2, 270, fit(s, 130, 1780), "black", INK)
    p = skia.Path(); p.moveTo(120, 420); p.lineTo(1800, 1000); p.lineTo(120, 1000); p.close()
    c.drawPath(p, paint(mix("#FFFFFF", BLUE, 0.10), 1.0))
    for x, y, r in ((300, 520, 30), (470, 600, 50), (690, 690, 80)):
        c.drawCircle(x, y, r, paint(V.NEVE, 1.0)); c.drawCircle(x, y, r, paint(BLUE, 1.0, stroke=6))
    c.drawCircle(1110, 690, 230, paint(V.NEVE, 1.0)); c.drawCircle(1110, 690, 230, paint(BLUE, 1.0, stroke=10))
    for dx, dy in ((-60, -40), (70, 80), (90, -110), (-100, 120)):
        c.drawCircle(1110 + dx, 690 + dy, 18, paint(mix("#FFFFFF", BLUE, 0.35), 1.0))
    V.chip(c, "72 ÷ taxa = ?", 1590, 470, GREEN, 1.0, 64)
    text(c, "juros sobre juros: a bola de neve", W / 2, 1010, 54, "extrabold", PURPLE)


def capa_conta(c):
    background(c); selo_topo(c, W / 2)
    s = "VOCÊ CAI NESTA?"
    text(c, s, W / 2, 270, fit(s, 130, 1700), "black", INK)
    shadow_rrect(c, 260, 360, 1400, 300, 40, 1, 1.5)
    rrect(c, 260, 360, 1400, 300, 40, "#FFFFFF")
    text_mid(c, "1,34 × 2 = 2,68 ?", W / 2, 510, 150, "black", INK)
    V.selo(c, 1540, 380, 1.0, "PEGADINHA", AMBER, 10, 54)
    text(c, "dobrar o tempo dobra o fator?", W / 2, 760, 60, "extrabold", PURPLE)
    for k in range(9):
        x = W / 2 - 4 * 130 + k * 130
        rrect(c, x - 52, 850, 104, 120, 20, AMBER, 0.14)
        text_mid(c, "V/F", x, 912, 34, "black", INK2)


if __name__ == "__main__":
    for nome, fn in (("capa_A_potencia_no_enunciado", capa_prova), ("capa_B_bola_de_neve", capa_bola),
                     ("capa_C_voce_cai_nesta", capa_conta)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
