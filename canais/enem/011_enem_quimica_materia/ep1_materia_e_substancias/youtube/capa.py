"""Capas — Matéria, Substâncias e Misturas, Episódio 1 (tema claro). Gera 3 variações em 1280x720."""
import importlib.util, subprocess, sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(next(d / "_ferramentas" for d in HERE.parents if (d / "_ferramentas").is_dir())))
import skia
import motor
motor.set_theme("claro")
from motor import *  # noqa

_spec = importlib.util.spec_from_file_location("visual_ep1", HERE.parent / "roteiro" / "visual.py")
V = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(V)


def boxed(c, s, x, y, size, bg_col, fg="#FFFFFF", pad=34):
    w = text_w(s, "black", size) + pad * 2
    h = size * 1.22
    shadow_rrect(c, x, y, w, h, 22, 1, 1.4)
    rrect(c, x, y, w, h, 22, bg_col)
    text_mid(c, s, x + w / 2, y + h / 2, size, "black", fg)


def selo(c):
    pill(c, "QUÍMICA DO ZERO · EPISÓDIO 1", 84, 90, BLUE, size=40, bounds=(0, 1920))


def painel(c):
    card(c, 1120, 120, 700, 840, r=36)


def capa_o2(c):
    background(c)
    selo(c)
    painel(c)
    V.mol(c, "O2", 1470, 400, 130)
    V.formula(c, "O2", 1470, 690, 200, lit=1.0)
    text(c, "2 átomos · 1 elemento", 1470, 880, 44, "black", INK2)
    text(c, "O₂ TEM 2", 80, 340, 130, "black", INK, align="left")
    text(c, "ÁTOMOS E…", 80, 480, 130, "black", INK, align="left")
    boxed(c, "NÃO É COMPOSTA?", 70, 530, 104, RED)
    text(c, "simples × composta do zero", 90, 860, 54, "extrabold", INK2, align="left")


def capa_2s(c):
    background(c)
    selo(c)
    painel(c)
    for k, (f, lit) in enumerate((("H2O", 2), ("S8", 1), ("CO2", 2), ("Fe", 1))):
        y = 260 + k * 170
        V.formula(c, f, 1360, y, 92, lit=lit, upper=True)
        k_ = V.n_el(f)
        text_mid(c, "SIMPLES" if k_ == 1 else "COMPOSTA", 1640, y, 40, "black", PURPLE)
    text(c, "SIMPLES OU", 80, 340, 128, "black", INK, align="left")
    text(c, "COMPOSTA?", 80, 480, 128, "black", INK, align="left")
    boxed(c, "EM 2 SEGUNDOS", 70, 530, 120, GREEN)
    text(c, "conte as letras, não os números", 90, 860, 52, "extrabold", INK2, align="left")


def capa_lego(c):
    background(c)
    selo(c)
    painel(c)
    for k, col in enumerate((V.EL["O"], V.EL["N"], V.EL["S"])):
        V.brick(c, 1220 + k * 170, 260, 150, 100, col)
    text_mid(c, "=", 1470, 460, 100, "black", INK2)
    V.mol(c, "H2O", 1340, 640, 70)
    V.mol(c, "CO2", 1600, 820, 50)
    text(c, "QUÍMICA É", 80, 340, 136, "black", INK, align="left")
    text(c, "COMO LEGO", 80, 480, 136, "black", INK, align="left")
    boxed(c, "MATÉRIA E SUBSTÂNCIA", 70, 530, 84, PURPLE)
    text(c, "para quem nunca estudou química", 90, 860, 52, "extrabold", INK2, align="left")


if __name__ == "__main__":
    for nome, fn in (("capa_A_o2_nao_e_composta", capa_o2), ("capa_B_2_segundos", capa_2s), ("capa_C_quimica_lego", capa_lego)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
