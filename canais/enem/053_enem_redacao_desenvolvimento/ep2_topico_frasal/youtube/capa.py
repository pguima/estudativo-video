"""Capas — Redação ENEM, Desenvolvimento, Episódio 2: o tópico frasal (tema claro). 3 variações em 1280x720."""
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


def big(c, s, y, maxw=1000, size=140, par=None):
    while text_w(s, "black", size) > maxw or (par and text_w(par, "black", size) > maxw):
        size -= 4
    text(c, s, 80, y, size, "black", INK, align="left")


def boxed(c, s, x, y, size, bg_col, fg="#FFFFFF", pad=34):
    w = text_w(s, "black", size) + pad * 2
    h = size * 1.22
    shadow_rrect(c, x, y, w, h, 22, 1, 1.4)
    rrect(c, x, y, w, h, 22, bg_col)
    text_mid(c, s, x + w / 2, y + h / 2, size, "black", fg)


def selo(c):
    pill(c, "REDAÇÃO ENEM · DESENVOLVIMENTO · EP. 2", 84, 90, BLUE, size=40, bounds=(0, 1920))


def painel(c):
    card(c, 1120, 120, 700, 840, r=36)


def capa_etiqueta(c):
    """vaga × boa: a etiqueta do item"""
    background(c); selo(c); painel(c)
    V.tag_shape(c, 1170, 200, 600, 230, 1.0, LIGHT)
    text(c, "coisa", 1500, 345, 90, "black", GRAY)
    V.selo(c, 1560, 410, 1, "VAGA", RED, -8, 50)
    V.etiqueta_item(c, 1145, 530, 655, 290, 1.0, title="EIXO 1",
                    fields=[("EIXO:", "desinformação", 1, V.COR_EIXO), ("PROVA:", "sustenta o estigma", 1, V.COR_AFI)])
    check_icon(c, 1740, 540, 34, 1, GREEN)
    big(c, "A 1ª FRASE QUE", 340, par="DIZ O QUE VEM")
    big(c, "DIZ O QUE VEM", 470, par="A 1ª FRASE QUE")
    boxed(c, "TÓPICO FRASAL", 70, 520, 120, V.TOP)
    text(c, "a etiqueta de cada parágrafo da redação", 90, 860, 46, "extrabold", INK2, align="left")


def capa_teste(c):
    """o teste: só a tese + os tópicos"""
    background(c); selo(c); painel(c)
    rows = [("TESE", V.MOV["tese"]), ("TÓPICO 1", V.TOP), ("TÓPICO 2", V.TOP)]
    line(c, 1250, 300, 1250, 780, GREEN, 1, 10)
    for k, (s, col) in enumerate(rows):
        y = 230 + k * 240
        c.drawCircle(1250, y + 70, 22, paint(col))
        rrect(c, 1300, y, 470, 140, 20, mix("#FFFFFF", col, 0.14), shadow=True)
        text_mid(c, s, 1535, y + 70, 54, "black", col)
    check_icon(c, 1700, 880, 40, 1, GREEN)
    text(c, "faz sentido?", 1640, 896, 40, "black", GREEN, align="right")
    big(c, "LEIA SÓ", 340, par="ESTAS 3 FRASES")
    big(c, "ESTAS 3 FRASES", 470)
    boxed(c, "TESTE DE 2 MINUTOS", 70, 520, 96, GREEN)
    text(c, "o seu desenvolvimento tem raciocínio?", 90, 860, 46, "extrabold", INK2, align="left")


def capa_vaga(c):
    """o erro: começar com frase vaga"""
    background(c); selo(c); painel(c)
    V.paper(c, 1170, 200, 600, 680, 1.0, lh=56, top=300)
    V.hand_para(c, "A saúde mental é muito importante.", 1280, 360, 52, V.PEN, 1.0, 460, 64)
    V.strike(c, 1270, 345, 1720, 345, 1, RED)
    V.strike(c, 1270, 409, 1600, 409, 1, RED)
    V.selo(c, 1480, 560, 1, "NÃO PROVA NADA", RED, -8, 50)
    V.hand_para(c, "Em primeiro lugar, a desinformação…", 1280, 700, 46, V.PARTE["topico"], 1.0, 460, 58)
    check_icon(c, 1720, 820, 34, 1, GREEN)
    big(c, "SEU PARÁGRAFO", 340, par="COMEÇA ASSIM?")
    big(c, "COMEÇA ASSIM?", 470, par="SEU PARÁGRAFO")
    boxed(c, "ETIQUETA VAGA", 70, 520, 120, RED)
    text(c, "o tópico frasal que diz o que vai provar", 90, 860, 46, "extrabold", INK2, align="left")


if __name__ == "__main__":
    for nome, fn in (("capa_A_etiqueta", capa_etiqueta), ("capa_B_teste_3_frases", capa_teste),
                     ("capa_C_etiqueta_vaga", capa_vaga)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
