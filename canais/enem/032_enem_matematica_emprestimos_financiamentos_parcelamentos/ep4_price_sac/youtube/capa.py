"""Capas — Empréstimos, Financiamentos e Parcelamentos, Episódio 4: o sistema Price e SAC × Price (tema claro).
3 variações em 1280x720, sem gabarito: A = as cinco caixas da Price (juros encolhendo) com a pergunta do carnê;
B = o duelo de barras SAC × PRICE com "quem paga menos?"; C = os dois totais de juros do gancho com "mesma taxa?"."""
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


def fit(s, size, maxw, peso="black"):
    while text_w(s, peso, size) > maxw:
        size -= 4
    return size


def selo_topo(c, cx=None):
    s = "MATEMÁTICA ENEM · FINANCIAMENTOS · EP. 4"
    if cx is None:
        pill(c, s, 84, 90, BLUE, size=34, bounds=(0, 1920))
    else:
        pill(c, s, cx, 90, BLUE, size=34, anchor="center", bounds=(0, 1920))


def capa_caixas(c):
    background(c); selo_topo(c)
    s1 = "PARCELA IGUAL."
    text(c, s1, 84, 280, fit(s1, 140, 1100), "black", INK, align="left")
    s2 = "E A DÍVIDA?"
    text(c, s2, 84, 420, fit(s2, 140, 1100), "black", V.ORANGE, align="left")
    for k, (am, ju) in enumerate(V.PRICE):
        V.caixa(c, 120 + k * 250, 520, 200, 440, ju, am, 1.0, rot=False)
    text(c, "juros", 1450, 600, 54, "black", V.ORANGE, align="left")
    text(c, "abate a dívida", 1450, 860, 54, "black", BLUE, align="left")
    V.selo(c, 1560, 330, 1.0, "SISTEMA PRICE", PURPLE, -6, 50)


def capa_duelo(c):
    background(c); selo_topo(c, W / 2)
    s = "SAC × PRICE: QUEM PAGA MENOS?"
    text(c, s, W / 2, 270, fit(s, 130, 1800), "black", INK)
    V.barras(c, 140, 420, 700, 480, V.SAC, 1.0, 1.0, rot_parcela=False)
    V.barras(c, 1080, 420, 700, 480, V.PRICE, 1.0, 1.0, rot_parcela=False)
    text(c, "SAC", 490, 400, 80, "black", BLUE)
    text(c, "PRICE", 1430, 400, 80, "black", PURPLE)
    text_mid(c, "?", W / 2, 680, 260, "black", AMBER)


def capa_taxa(c):
    background(c); selo_topo(c, W / 2)
    s = "MESMA TAXA. JUROS DIFERENTES?"
    text(c, s, W / 2, 280, fit(s, 130, 1800), "black", INK)
    for k, v in enumerate(("R$ 1.200,00", "R$ 1.231,35")):
        x = 150 + k * 900
        shadow_rrect(c, x, 400, 720, 460, 36, 1, 1.4)
        rrect(c, x, 400, 720, 460, 36, "#FFFFFF")
        text(c, f"SISTEMA {k + 1}", x + 360, 500, 56, "black", GRAY)
        text(c, "de juros", x + 360, 590, 46, "extrabold", INK2)
        text(c, v, x + 360, 760, fit(v, 120, 660), "black", V.ORANGE)
    text_mid(c, "?", W / 2, 640, 220, "black", AMBER)


if __name__ == "__main__":
    for nome, fn in (("capa_A_parcela_igual_divida", capa_caixas), ("capa_B_quem_paga_menos", capa_duelo),
                     ("capa_C_mesma_taxa", capa_taxa)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
