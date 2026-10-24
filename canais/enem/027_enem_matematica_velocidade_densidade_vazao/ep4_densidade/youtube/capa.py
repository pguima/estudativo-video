"""Capas — Velocidade, Densidade e Vazão, Episódio 4: densidade (tema claro). 3 variações em 1280x720.
Formatos: A = aquário ocupando a metade de baixo, com o título por cima da linha d'água; B = balança gigante no centro,
com a pergunta em volta; C = duelo prego × portão com a mesma etiqueta (sem dizer a resposta)."""
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


def fit(s, size, maxw, peso="black"):
    while text_w(s, peso, size) > maxw:
        size -= 4
    return size


def selo_topo(c, cx=None):
    s = "MATEMÁTICA ENEM · DENSIDADE · EP. 4"
    if cx is None:
        pill(c, s, 84, 90, BLUE, size=34, bounds=(0, 1920))
    else:
        pill(c, s, cx, 90, BLUE, size=34, anchor="center", bounds=(0, 1920))


def capa_aquario(c):
    background(c)
    wy = 600
    c.drawRect(skia.Rect.MakeXYWH(0, wy, W, H - wy), paint(mix("#FFFFFF", V.AGUA, 0.7)))
    c.drawRect(skia.Rect.MakeXYWH(0, wy - 40, W, 40), paint(mix("#FFFFFF", V.COR["óleo"], 0.75)))
    s = 170
    V.cubo(c, 330, wy - 40 + s * (0.92 - 0.5), s, V.COR["gelo"], 1.0)
    V.cubo(c, 820, H - 30 - s / 2, s, V.COR["ferro"], 1.0)
    V.cubo(c, 1260, H - 30 - s / 2, s, V.COR["alumínio"], 1.0)
    V.cubo(c, 1660, H - 30 - s / 2, s, V.COR["ouro"], 1.0)
    c.drawRect(skia.Rect.MakeXYWH(0, wy, W, H - wy), paint(V.AGUA, 0.25))
    line(c, 0, wy - 40, W, wy - 40, V.AGUA_ESC, 1.0, 5)
    selo_topo(c, W / 2)
    t1 = "BOIA OU AFUNDA?"
    text(c, t1, W / 2, 300, fit(t1, 190, 1760), "black", INK)
    t2 = "descubra com UMA conta"
    text(c, t2, W / 2, 430, 84, "black", PURPLE)


def capa_balanca(c):
    background(c); selo_topo(c)
    V.balanca(c, 560, 620, 760, 1.0, "156 g")
    V.cubo(c, 530, 500, 200, V.COR["ferro"], 1.0)
    pill(c, "20 cm³", 860, 360, AMBER, size=60, anchor="center")
    pill(c, "156 g", 300, 360, GREEN, size=60, anchor="center")
    t1 = "DE QUE"
    t2 = "É FEITO?"
    text(c, t1, 1440, 400, 150, "black", INK)
    sz = 150
    w = text_w(t2, "black", sz) + 70
    shadow_rrect(c, 1440 - w / 2, 450, w, 190, 30, 1, 1.4)
    rrect(c, 1440 - w / 2, 450, w, 190, 30, BLUE)
    text_mid(c, t2, 1440, 548, sz, "black", "#FFFFFF")
    text(c, "uma divisão vira laboratório", 1440, 760, 50, "extrabold", INK2)


def capa_duelo(c):
    background(c); selo_topo(c, W / 2)
    t1 = "QUAL É MAIS DENSO?"
    text(c, t1, W / 2, 290, fit(t1, 150, 1780), "black", INK)
    for k, (tit, col) in enumerate((("PREGO", AMBER), ("PORTÃO", PURPLE))):
        x = 140 + k * 860
        shadow_rrect(c, x, 360, 780, 600, 34, 1, 1.4)
        rrect(c, x, 360, 780, 600, 34, "#FFFFFF")
        rrect(c, x, 360, 780, 100, 34, col, 0.16)
        text(c, tit, x + 390, 432, 64, "black", col)
    V.prego(c, 300, 690, 460, 1.0)
    V.portao(c, 1140, 560, 500, 260, 1.0)
    text_mid(c, "VS", W / 2, 660, 110, "black", RED)
    text(c, "3,9 g", 530, 880, 60, "black", INK2)
    text(c, "78 kg", 1390, 880, 60, "black", INK2)


if __name__ == "__main__":
    for nome, fn in (("capa_A_boia_ou_afunda", capa_aquario), ("capa_B_de_que_e_feito", capa_balanca),
                     ("capa_C_prego_ou_portao", capa_duelo)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
