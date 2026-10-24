"""Capas — Unidades e conversões, Episódio 4: análise dimensional e as unidades de fora (tema claro). 3 variações em 1280x720."""
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
    pill(c, "MATEMÁTICA ENEM · UNIDADES · EP. 4", 84, 90, BLUE, size=36, bounds=(0, 1920))


def painel(c):
    card(c, 1120, 120, 700, 840, r=36)


def capa_riscar(c):
    background(c); selo(c); painel(c)
    V.cadeia(c, 1470, 300, [("90", "km", "", "h"), ("1 000", "m", "1", "km")], 64,
             riscos={(0, "t"): 1, (1, "b"): 1}, cores={(1, "t"): GREEN})
    V.cadeia(c, 1470, 560, [("1", "h", "3 600", "s")], 64, riscos={(0, "t"): 1}, cores={(0, "b"): GREEN})
    text_mid(c, "×", 1270, 560, 60, "black", GRAY)
    V.linha(c, [("sobrou ", INK2), ("m/s", GREEN)], 1470, 820, 60, 1.0)
    big(c, "ESQUECEU O 3,6?", 330)
    big(c, "RISQUE AS", 470)
    boxed(c, "UNIDADES", 70, 520, 170, PURPLE)
    text(c, "o método que nunca falha, sem decorar", 90, 860, 44, "extrabold", INK2, align="left")


def capa_fator(c):
    background(c); selo(c); painel(c)
    V.tv(c, 1470, 360, 480, 280, 1.0, "? pol")
    for k, (u, eq) in enumerate((("polegada", "2,54 cm"), ("milha", "≈ 1,6 km"), ("galão", "≈ 3,785 L"))):
        y = 640 + k * 90
        text(c, u, 1230, y, 40, "black", PURPLE, align="left")
        text(c, eq, 1720, y, 40, "black", INK, align="right")
    big(c, "POLEGADA, MILHA,", 330)
    big(c, "GALÃO: A PROVA", 470)
    boxed(c, "DÁ O FATOR", 70, 520, 170, GREEN)
    text(c, "a habilidade é usar, e não decorar", 90, 860, 44, "extrabold", INK2, align="left")


def capa_kwh(c):
    background(c); selo(c); painel(c)
    V.chuveiro(c, 1330, 420, 1.0, 1.0)
    V.relogio_luz(c, 1640, 420, 1.0, 0.15, "kWh?")
    V.linha(c, [("kW", BLUE), (" × ", GRAY), ("h", AMBER), (" = ", GRAY), ("kWh", GREEN)], 1470, 760, 64, 1.0)
    big(c, "kWh NÃO É", 330)
    big(c, "POTÊNCIA:", 470)
    boxed(c, "É ENERGIA", 70, 520, 170, AMBER)
    text(c, "a conta de luz explicada em uma conta", 90, 860, 44, "extrabold", INK2, align="left")


if __name__ == "__main__":
    for nome, fn in (("capa_A_risque_as_unidades", capa_riscar), ("capa_B_a_prova_da_o_fator", capa_fator),
                     ("capa_C_kwh_e_energia", capa_kwh)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
