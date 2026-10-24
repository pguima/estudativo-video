"""Capas — Unidades de Medida e Conversões, Episódio 5: Revisão geral (tema claro). 3 variações em 1280x720.
Evita os formatos das revisões 019–024 ("N PEGADINHAS: QUANTAS VOCÊ ACERTA?", "5 QUESTÕES ...", "VOCÊ ESTÁ PRONTO?",
"VERDADEIRO OU FALSO?", "PROPORCIONAL OU NÃO?", "QUAIS SÃO OS PESOS?", "UMA FERRAMENTA RESOLVE QUASE TUDO", "3 HÁBITOS...")
e as frases já usadas em capas de unidades ("1 m² NÃO SÃO 100 cm²", "1,6 HORA NÃO É 1 h 60").
Nenhuma entrega gabarito das 5 questões inéditas."""
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
    pill(c, "MATEMÁTICA ENEM · EPISÓDIO 5", 84, 90, BLUE, size=40, bounds=(0, 1920))


def painel(c):
    card(c, 1120, 120, 700, 840, r=36)


def capa_silencioso(c):
    background(c); selo(c); painel(c)
    erros = ["1 m³ = 1 L", "1 t = 100 kg", "2,4 h = 2 h 40"]
    for k, s in enumerate(erros):
        y = 260 + k * 190
        rrect(c, 1180, y - 70, 580, 140, 24, mix("#FFFFFF", RED, 0.08), 1)
        size = 72
        while K.ftext_w(s, "black", size) > 500:
            size -= 4
        K.fmid(c, s, 1470, y, size, "black", INK)
        w = K.ftext_w(s, "black", size)
        line(c, 1470 - w / 2 - 12, y + 8, 1470 + w / 2 + 12, y - 8, RED, 1, 8)
    text(c, "a conta fecha… e está errada", 1470, 880, 38, "black", RED)
    big(c, "O ERRO QUE", 320)
    big(c, "NÃO DÁ SINAL", 480, size=132)
    boxed(c, "DAS UNIDADES", 70, 540, 140, RED)
    text(c, "revisão completa + 5 questões novas", 90, 860, 46, "extrabold", INK2, align="left")


def capa_fatos(c):
    background(c); selo(c); painel(c)
    V.cubo(c, 1300, 230, 110, 1)
    text(c, "× 100 · × 1 000", 1610, 330, 44, "black", BLUE)
    V.caixa_leite(c, 1300, 690, 110, 240, 1)
    text(c, "1 L = 1 dm³", 1610, 600, 52, "black", PURPLE)
    K.fmid(c, "0,25 h = 15 min", 1470, 850, 52, "black", GREEN)
    big(c, "3 FATOS QUE", 340)
    big(c, "SALVAM A CONTA", 470)
    boxed(c, "DE UNIDADES", 70, 520, 150, BLUE)
    text(c, "área, litro e tempo sem errar", 90, 860, 46, "extrabold", INK2, align="left")


def capa_areas(c):
    background(c); selo(c); painel(c)
    for k, (ic, rot) in enumerate(((2, "km/h → m/s"), (3, "mL → L"), (4, "W → kW"))):
        y = 270 + k * 230
        V.area_icone(c, ic, 1290, y, 1.1, 1)
        text(c, rot, 1440, y + 18, 50, "black", (GREEN, PURPLE, AMBER)[k], align="left")
    big(c, "UNIDADES NA", 340)
    big(c, "FÍSICA, QUÍMICA", 470)
    boxed(c, "E NA CONTA DE LUZ", 70, 520, 120, PURPLE)
    text(c, "treino de conversões para o ENEM", 90, 860, 46, "extrabold", INK2, align="left")


if __name__ == "__main__":
    for nome, fn in (("capa_A_erro_sem_sinal", capa_silencioso), ("capa_B_tres_fatos", capa_fatos),
                     ("capa_C_fisica_quimica_luz", capa_areas)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
