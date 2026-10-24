"""Capas — Escalas, Plantas e Mapas, Episódio 3: plantas e maquetes, n² e n³ (tema claro). 3 variações em 1280x720."""
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
    pill(c, "MATEMÁTICA ENEM · ESCALAS · EP. 3", 84, 90, BLUE, size=36, bounds=(0, 1920))


def painel(c):
    card(c, 1120, 120, 700, 840, r=36)


def capa_maquete(c):
    background(c); selo(c); painel(c)
    text(c, "maquete 1 : 20", 1470, 230, 50, "black", PURPLE)
    V.tanque(c, 1260, 560, 110, 110, 1.0, 0.85, "5 L", 34)
    arrow(c, 1340, 640, 1430, 600, INK2, 1.0, 6, 18)
    V.tanque(c, 1620, 360, 280, 380, 1.0, 0.85, "?", 90)
    text(c, "a caixa de verdade", 1620, 900, 34, "black", INK2)
    big(c, "5 LITROS NA", 330)
    big(c, "MAQUETE...", 470)
    boxed(c, "E NA VIDA REAL?", 70, 520, 140, AMBER)
    text(c, "o erro mais caro de escala: esquecer o cubo", 90, 860, 44, "extrabold", INK2, align="left")


def capa_planta(c):
    background(c); selo(c); painel(c)
    V.planta_baixa(c, 1240, 380, 52, 1.0, cotas=True, foco="sala", foco_a=1.0)
    pill(c, "planta 1 : 100", 1470, 800, PURPLE, size=40, anchor="center", bounds=(0, 1920))
    big(c, "QUANTOS m²", 330)
    big(c, "TEM ESSA", 470)
    boxed(c, "SALA?", 70, 520, 160, BLUE)
    text(c, "planta baixa: converta os lados primeiro", 90, 860, 42, "extrabold", INK2, align="left")


def capa_fatores(c):
    background(c); selo(c); painel(c)
    rows = [("comprimento", "1 : n", BLUE, 1), ("área", "1 : n²", PURPLE, 2), ("volume", "1 : n³", AMBER, 3)]
    for k, (s, f, col, dim) in enumerate(rows):
        y = 320 + k * 220
        ix = 1220
        if dim == 1:
            line(c, ix - 50, y, ix + 50, y, col, 1.0, 10)
        elif dim == 2:
            rrect(c, ix - 50, y - 50, 100, 100, 4, mix("#FFFFFF", col, 0.35))
            c.drawRect(skia.Rect.MakeXYWH(ix - 50, y - 50, 100, 100), paint(col, 1.0, stroke=4))
        else:
            V.caixa_iso(c, ix, y - 46, 70, 1, 1, 1, 1.0, div=0)
        text(c, s, 1300, y - 10, 40, "black", INK2, align="left")
        text(c, f, 1300, y + 58, 70, "black", col, align="left")
    big(c, "UMA ESCALA,", 330)
    big(c, "TRÊS", 470)
    boxed(c, "FATORES", 70, 520, 160, PURPLE)
    text(c, "planta e maquete: o quadrado e o cubo", 90, 860, 42, "extrabold", INK2, align="left")


if __name__ == "__main__":
    for nome, fn in (("capa_A_cinco_litros_na_maquete", capa_maquete), ("capa_B_quantos_m2_essa_sala", capa_planta),
                     ("capa_C_tres_fatores", capa_fatores)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
