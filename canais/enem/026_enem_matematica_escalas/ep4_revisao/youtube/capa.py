"""Capas — Escalas, Plantas e Mapas, Episódio 4: Revisão geral (tema claro). 3 variações em 1280x720.
Evita os formatos das revisões 018–025 ("N PEGADINHAS", "5 QUESTÕES ...", "VOCÊ ESTÁ PRONTO?", "VERDADEIRO OU FALSO?",
"PROPORCIONAL OU NÃO?", "QUAIS SÃO OS PESOS?", "UMA FERRAMENTA...", "3 HÁBITOS...", "O ERRO QUE NÃO DÁ SINAL", "3 FATOS...")
e as capas de escala da Cartografia 012 ep1 (mapa gigante, escala = zoom, corte 5 zeros).
Nenhuma entrega gabarito das 5 questões inéditas."""
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
    pill(c, "MATEMÁTICA ENEM · EPISÓDIO 4", 84, 90, BLUE, size=40, bounds=(0, 1920))


def painel(c):
    card(c, 1120, 120, 700, 840, r=36)


def capa_duas_provas(c):
    background(c); selo(c); painel(c)
    V.mapa(c, 1220, 200, 500, 300, 1)
    text_mid(c, "1 : 250 000", 1470, 560, 64, "black", INK)
    chip_ = V.chip
    chip_(c, "MATEMÁTICA", 1470, 690, BLUE, 1, 52)
    chip_(c, "GEOGRAFIA", 1470, 820, AMBER, 1, 52)
    big(c, "A MESMA ESCALA", 330)
    big(c, "CAI NAS DUAS", 470)
    boxed(c, "PROVAS DO ENEM", 70, 520, 140, AMBER)
    text(c, "revisão de escalas + 5 questões novas", 90, 860, 46, "extrabold", INK2, align="left")


def capa_fotocopia(c):
    background(c); selo(c); painel(c)
    V.mapa(c, 1180, 190, 200, 130, 1, cidades=False)
    arrow(c, 1400, 260, 1460, 260, INK2, 1, 6, 18)
    V.mapa(c, 1480, 170, 300, 200, 1, cidades=False)
    K.fmid(c, "1 : 80 000", 1470, 470, 80, "black", INK)
    K.fmid(c, "?", 1720, 470, 90, "black", RED)
    V.barra_grafica(c, 1290, 610, 360, 1, "")
    text(c, "0", 1290, 690, 40, "black", INK)
    text(c, "1,6 km", 1650, 690, 40, "black", INK)
    text(c, "e agora, qual escala vale?", 1470, 840, 38, "black", AMBER)
    big(c, "AMPLIOU O MAPA.", 330, size=120)
    big(c, "E A ESCALA?", 470)
    boxed(c, "PEGADINHA DO ENEM", 70, 520, 120, RED)
    text(c, "revisão de escalas, plantas e mapas", 90, 860, 46, "extrabold", INK2, align="left")


def capa_tres_objetos(c):
    background(c); selo(c); painel(c)
    V.mapa(c, 1180, 170, 330, 190, 1)
    V.area_icone(c, 2, 1640, 420, 1.2, 1)
    V.caixa(c, 1340, 650, 110, 1, div=4)
    text(c, "n · n² · n³", 1640, 640, 56, "black", PURPLE)
    big(c, "MAPA, PLANTA", 340)
    big(c, "E MAQUETE", 470)
    boxed(c, "TUDO EM 1 AULA", 70, 520, 140, GREEN)
    text(c, "a revisão de escalas para o ENEM", 90, 860, 46, "extrabold", INK2, align="left")


if __name__ == "__main__":
    for nome, fn in (("capa_A_duas_provas", capa_duas_provas), ("capa_B_mapa_ampliado", capa_fotocopia),
                     ("capa_C_mapa_planta_maquete", capa_tres_objetos)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
