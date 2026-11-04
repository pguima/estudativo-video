"""Capas — Redação ENEM, Desenvolvimento, Episódio 4: análise e fechamento, o "e daí?" (tema claro). 3 variações em 1280x720."""
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


def big(c, s, y, maxw=1000, size=140):
    while text_w(s, "black", size) > maxw:
        size -= 4
    text(c, s, 80, y, size, "black", INK, align="left")


def boxed(c, s, x, y, size, bg_col, fg="#FFFFFF", pad=34):
    w = text_w(s, "black", size) + pad * 2
    h = size * 1.22
    shadow_rrect(c, x, y, w, h, 22, 1, 1.4)
    rrect(c, x, y, w, h, 22, bg_col)
    text_mid(c, s, x + w / 2, y + h / 2, size, "black", fg)


def selo(c):
    pill(c, "REDAÇÃO ENEM · DESENVOLVIMENTO · EP. 4", 84, 90, V.AN, size=40, bounds=(0, 1920))


def painel(c):
    card(c, 1120, 120, 700, 840, r=36)


def capa_escada(c):
    background(c); selo(c); painel(c)
    V.escada(c, 1230, 860, 1.0, 3, sw=180, sh=150, citou=1.0, argumentou=1.0, ps=1.0)
    V.edai(c, 1250, 230, 1.0, 64)
    big(c, "CITAR NÃO É", 340)
    boxed(c, "ARGUMENTAR", 70, 400, 130, V.AN)
    text(c, "a análise que faz a referência trabalhar", 90, 700, 46, "extrabold", INK2, align="left")
    text(c, "e o fechamento que volta para a tese", 90, 770, 46, "extrabold", INK2, align="left")


def capa_edai(c):
    background(c); selo(c); painel(c)
    rrect(c, 1170, 200, 600, 200, 20, mix("#FFFFFF", V.RP, 0.14), 1, shadow=True)
    V.icone_etapa(c, "repertorio", 1260, 300, 1, 1.1, disc=False)
    text(c, "O Alienista", 1330, 290, 50, "black", INK, align="left")
    text(c, "Machado de Assis", 1330, 345, 34, "bold", INK2, align="left")
    V.edai(c, 1220, 450, 1.0, 110)
    V.person(c, 1660, 760, V.BLUE, 1, 1.2)
    big(c, "A PERGUNTA QUE", 340)
    big(c, "FALTA NO SEU", 470)
    boxed(c, "PARÁGRAFO", 70, 520, 140, V.AN)
    text(c, "análise e fechamento na redação do ENEM", 90, 860, 46, "extrabold", INK2, align="left")


def capa_recibo(c):
    background(c); selo(c); painel(c)
    V.recibo(c, 1200, 180, 540, 720, 1.0, linhas=[("ITEM", "eixo do parágrafo"), ("LIGADO À", "tese")], assin=1.0,
             body=None)
    V.selo(c, 1470, 620, 1, "ASSINADO ✓", GREEN, -8, 64)
    big(c, "FECHOU COM", 340)
    big(c, "“ISSO É MUITO GRAVE”?", 470, 1000, 110)
    boxed(c, "ERRADO!", 70, 530, 140, RED)
    text(c, "a última frase precisa voltar para a tese", 90, 860, 46, "extrabold", INK2, align="left")


if __name__ == "__main__":
    for nome, fn in (("capa_A_citar_argumentar", capa_escada), ("capa_B_e_dai", capa_edai),
                     ("capa_C_isso_e_grave", capa_recibo)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
