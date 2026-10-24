"""Capas — Porcentagem, Episódio 6: Revisão geral (tema claro). 3 variações em 1280x720.
Evita os formatos das revisões 019–023 ("N PEGADINHAS: QUANTAS VOCÊ ACERTA?", "5 QUESTÕES ...", "VOCÊ ESTÁ PRONTO?",
"VERDADEIRO OU FALSO?", "PROPORCIONAL OU NÃO?", "QUAIS SÃO OS PESOS?", "SOMAR OU MULTIPLICAR?") e as frases das capas
do ep3 desta série. Nenhuma entrega gabarito das 5 questões inéditas."""
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


def capa_fator(c):
    background(c); selo(c); painel(c)
    V.maquina(c, 1470, 290, "fator", 1, 20, PURPLE, w=420, h=230)
    for k, (var, fat, col) in enumerate((("+12%", "1,12", GREEN), ("−35%", "0,65", RED), ("+200%", "3", GREEN))):
        y = 540 + k * 130
        K.ftext(c, var, 1420, y + 22, 64, "black", col, align="right")
        K.ftext(c, "→ × " + fat, 1450, y + 22, 64, "black", PURPLE, align="left")
    big(c, "UMA FERRAMENTA", 340)
    big(c, "RESOLVE", 470)
    boxed(c, "QUASE TUDO", 70, 520, 150, PURPLE)
    text(c, "revisão completa de porcentagem", 90, 860, 46, "extrabold", INK2, align="left")


def capa_pontos(c):
    background(c); selo(c); painel(c)
    V.termometro(c, 1330, 470, 1, 8, 10, 1.0, s=1.9)
    text(c, "+2 p.p.", 1660, 300, 66, "black", BLUE)
    text(c, "+25%", 1660, 700, 86, "black", GREEN)
    text(c, "“subiu 2%”", 1470, 860, 56, "black", RED)
    line(c, 1270, 840, 1670, 840, RED, 1, 7)
    big(c, "DE 8% PARA 10%", 340)
    big(c, "SUBIU 2%?", 470)
    boxed(c, "NÃO É BEM ASSIM", 70, 520, 130, RED)
    text(c, "as pegadinhas de porcentagem do ENEM", 90, 860, 46, "extrabold", INK2, align="left")


def capa_habitos(c):
    background(c); selo(c); painel(c)
    itens = [("1", "FATOR", PURPLE), ("2", "USE 100", BLUE), ("3", "CONFIRA O SENTIDO", GREEN)]
    for k, (n, s, col) in enumerate(itens):
        y = 240 + k * 240
        badge_num(c, n, 1220, y, 1, 44, bg=col)
        size = 60
        while text_w(s, "black", size) > 480:
            size -= 4
        text(c, s, 1300, y + size * 0.36, size, "black", col, align="left")
    V.bola(c, 1680, 480, 60, 1, "100", 40)
    big(c, "3 HÁBITOS QUE", 340)
    big(c, "SALVAM A QUESTÃO", 470)
    boxed(c, "DE PORCENTAGEM", 70, 520, 130, GREEN)
    text(c, "estratégia de prova + questões novas", 90, 860, 46, "extrabold", INK2, align="left")


if __name__ == "__main__":
    for nome, fn in (("capa_A_uma_ferramenta", capa_fator), ("capa_B_subiu_2", capa_pontos),
                     ("capa_C_tres_habitos", capa_habitos)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
