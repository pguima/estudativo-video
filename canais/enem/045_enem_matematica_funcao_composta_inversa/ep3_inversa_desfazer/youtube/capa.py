"""Capas — Função Composta e Inversa, Episódio 3: função inversa, desfazer o caminho (tema claro). 3 variações em 1280x720.
A = o termômetro de Nova York: "98,6 °F" gigante e "= ? °C" (sem dar os 37); B = a esteira de ida (×2, +1) e a de volta com
as estações "?" e "DE TRÁS PARA FRENTE"; C = "f⁻¹ = 1/f ?" tipográfico com faixa âmbar "O ⁻¹ NÃO É EXPOENTE"."""
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


def fit(s, size, maxw, peso="black"):
    while text_w(s, peso, size) > maxw:
        size -= 4
    return size


def selo_topo(c, cx=None):
    s = "MATEMÁTICA ENEM · FUNÇÃO INVERSA · EP. 3"
    if cx is None:
        pill(c, s, 84, 90, BLUE, size=34, bounds=(0, 1920))
    else:
        pill(c, s, cx, 90, BLUE, size=34, anchor="center", bounds=(0, 1920))


def capa_termometro(c):
    background(c); selo_topo(c)
    c.save(); c.translate(380, 560); c.scale(1.45, 1.45); c.translate(-380, -560)
    V.termometro(c, 380, 330, 780, 37, 1.0)
    c.restore()
    s = "98,6 °F"
    text(c, s, 1250, 470, fit(s, 230, 1150), "black", V.COL_IDA)
    s2 = "= ? °C"
    sz = fit(s2, 170, 900)
    w = text_w(s2, "black", sz) + 80
    shadow_rrect(c, 1250 - w / 2, 560, w, 210, 30, 1, 1.4)
    rrect(c, 1250 - w / 2, 560, w, 210, 30, V.COL_VOLTA)
    text_mid(c, s2, 1250, 665, sz, "black", "#FFFFFF")
    text(c, "a fórmula da VOLTA", 1250, 900, 70, "extrabold", PURPLE)


def capa_esteira(c):
    background(c); selo_topo(c, W / 2)
    s = "DE TRÁS PARA FRENTE"
    text(c, s, W / 2, 290, fit(s, 150, 1760), "black", INK)
    V.esteira(c, 120, 1800, 520, 1.0)
    V.maquina(c, 720, 430, "×2", V.COL_IDA, 1.0, 0.3, 320, 190, 100)
    V.maquina(c, 1200, 430, "+1", V.COL_IDA, 1.0, 0.3, 320, 190, 100)
    V.bola(c, 300, 430, "1", INK, 1.0, 74)
    V.bola(c, 1620, 430, "3", V.COL_IDA, 1.0, 74)
    V.esteira(c, 120, 1800, 900, 1.0)
    V.maquina(c, 1200, 810, "?", V.COL_VOLTA, 1.0, 0.3, 320, 190, 110)
    V.maquina(c, 720, 810, "?", V.COL_VOLTA, 1.0, 0.3, 320, 190, 110)
    V.bola(c, 1620, 810, "3", V.COL_IDA, 1.0, 74)
    V.bola(c, 300, 810, "1", V.COL_VOLTA, 1.0, 74)
    arrow(c, 1500, 680, 420, 680, V.COL_VOLTA, 1.0, 10)


def capa_um_sobre(c):
    background(c); selo_topo(c, W / 2)
    V.linha(c, [("f⁻¹", V.COL_VOLTA), ("  =  ", INK), ("1/f", RED)], W / 2, 470, 280, 1.0)
    text_mid(c, "?", 1700, 450, 260, "black", AMBER)
    rrect(c, 0, 800, W, 280, 0, AMBER)
    s = "O ⁻¹ NÃO É EXPOENTE"
    text(c, s, W / 2, 985, fit(s, 160, 1780), "black", "#FFFFFF")


if __name__ == "__main__":
    for nome, fn in (("capa_A_termometro_98_6", capa_termometro), ("capa_B_de_tras_para_frente", capa_esteira),
                     ("capa_C_nao_e_expoente", capa_um_sobre)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
