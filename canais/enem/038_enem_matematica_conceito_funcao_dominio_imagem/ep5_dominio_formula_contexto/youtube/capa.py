"""Capas — Conceito de Função, Episódio 5: domínio pela fórmula e pelo contexto (tema claro). 3 variações em 1280x720.
A = a folha 30 × 20 com quadradinhos de 12 cm e o duelo "FÓRMULA: aceita × FOLHA: não"; B = planilha #DIV/0! e
calculadora Erro com "AS 2 PROIBIÇÕES"; C = a fórmula √(x − 2)/(x − 5) gigante sobre a reta com "?" no 2 e no 5.
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
    s = "MATEMÁTICA ENEM · FUNÇÕES · EP. 5"
    if cx is None:
        pill(c, s, 84, 90, BLUE, size=34, bounds=(0, 1920))
    else:
        pill(c, s, cx, 90, BLUE, size=34, anchor="center", bounds=(0, 1920))


def capa_folha(c):
    background(c); selo_topo(c)
    V.caixa(c, 520, 600, 30, 20, 9, 26, 1.0, rotulos=True, internos=False)
    rrect(c, 300, 840, 440, 100, 50, RED)
    text_mid(c, "x = 12 cm?", 520, 890, 60, "black", "#FFFFFF")
    for k, (tit, sub, col) in enumerate((("FÓRMULA", "aceita", GREEN), ("FOLHA", "NÃO", RED))):
        y = 330 + k * 300
        shadow_rrect(c, 1060, y, 780, 240, 34, 1, 1.4)
        rrect(c, 1060, y, 780, 240, 34, "#FFFFFF")
        rrect(c, 1060, y, 26, 240, 13, col)
        text(c, tit, 1130, y + 90, 60, "black", INK2, align="left")
        text(c, sub, 1800, y + 210, fit(sub, 110, 420), "black", col, align="right")


def capa_proibicoes(c):
    background(c); selo_topo(c, W / 2)
    s = "AS 2 PROIBIÇÕES"
    text(c, s, W / 2, 300, fit(s, 160, 1780), "black", INK)
    c.save(); c.translate(-60, 0); c.scale(1.45, 1.45)
    V.planilha(c, 110, 300, 1.0)
    c.restore()
    c.save(); c.translate(1440, 690); c.scale(1.35, 1.35)
    V.calculadora(c, 0, 0, 1.0)
    c.restore()
    rrect(c, 300, 940, 1320, 110, 55, RED)
    text_mid(c, "a conta que dá ERRO derruba você", W / 2, 995, 58, "black", "#FFFFFF")


def capa_formula(c):
    background(c); selo_topo(c, W / 2)
    V.m(c, "f(x) = √{x-2}/{x-5}", W / 2, 400, 170, 1.0, PURPLE, "center")
    X = V.reta_n(c, 360, 1560, 790, 0, 7, 1.0, size=44)
    V.faixa(c, X(0), X(7), 790, 0.25, GRAY, inf_esq=True, inf_dir=True)
    for v in (2, 5):
        c.drawCircle(X(v), 790, 30, paint(AMBER))
        text_mid(c, "?", X(v), 790, 46, "black", "#FFFFFF")
        rrect(c, X(v) - 130, 640, 260, 80, 40, AMBER)
        text_mid(c, f"o {v} entra?", X(v), 680, 40, "black", "#FFFFFF")
    text(c, "domínio sem erro", W / 2, 1000, 64, "extrabold", BLUE)


if __name__ == "__main__":
    for nome, fn in (("capa_A_a_folha_nao_aceita", capa_folha), ("capa_B_duas_proibicoes", capa_proibicoes),
                     ("capa_C_o_2_entra", capa_formula)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
