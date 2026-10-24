"""Capas — Função Afim, Episódio 2: taxa de variação, valor inicial e o zero (tema claro). 3 variações em 1280x720.
Formatos (sem o "texto à esquerda + painel à direita" das outras séries): A = vela gigante no centro, título em cima e
pergunta embaixo; B = fração Δy/Δx gigante com a invertida riscada ao lado; C = faixa roxa no alto e tanque largo embaixo.
Nenhuma mostra gabarito (nem 95 min, nem 8 h 20 min)."""
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
K = V.K


def fit(s, size, maxw, peso="black"):
    while V.ftext_w(s, peso, size) > maxw:
        size -= 4
    return size


def selo_topo(c, cx=None, cor=BLUE):
    s = "MATEMÁTICA ENEM · FUNÇÃO AFIM · EP. 2"
    if cx is None:
        pill(c, s, 84, 90, cor, size=34, bounds=(0, 1920))
    else:
        pill(c, s, cx, 90, cor, size=34, anchor="center", bounds=(0, 1920))


def capa_vela(c):
    background(c); selo_topo(c, W / 2)
    s = "A VELA ACABA QUANDO?"
    V.ftext(c, s, W / 2, 270, fit(s, 140, 1760), "black", INK)
    V.vela(c, 960, 900, 1.0, 17, 26)
    V.cronometro(c, 560, 600, 130, 1.0, 10)
    V.ftext(c, "10 min · 17 cm", 560, 820, 56, "black", INK)
    shadow_rrect(c, 1180, 470, 600, 220, 30, 1, 1.4)
    rrect(c, 1180, 470, 600, 220, 30, "#FFFFFF")
    V.ftext(c, "17 ÷ 0,2 = 85?", 1480, 600, 74, "black", AMBER)
    V.selo(c, 1480, 760, 1.0, "ERRA!", RED, -6, 64)
    V.rebobina(c, 1600, 360, 1.0, BLUE, 110)
    V.ftext(c, "volte o filme", 1600, 450, 40, "black", BLUE)


def capa_fracao(c):
    background(c); selo_topo(c)
    V.ftext(c, "A TAXA EM 1 FRAÇÃO", 84, 250, 96, "black", INK, align="left")
    K.boxed(c, 140, 330, 900, 620, PURPLE, 1.0, 0.08, 40, 8)
    K.fr(c, "Δy", "Δx", 590, 580, 150, PURPLE, 1.0)
    V.ftext(c, "SAÍDA ÷ ENTRADA", 590, 900, 54, "black", PURPLE)
    shadow_rrect(c, 1180, 380, 600, 400, 34, 1, 1.4)
    rrect(c, 1180, 380, 600, 400, 34, mix("#FFFFFF", RED, 0.08))
    K.fr(c, "Δx", "Δy", 1480, 540, 96, RED, 1.0)
    V.strike(c, 1300, 680, 1660, 420, 1.0, RED, 1)
    V.ftext(c, "INVERTIDA", 1480, 740, 50, "black", RED)
    V.selo(c, 1480, 890, 1.0, "NUNCA INVERTA", AMBER, -5, 52)


def capa_tanque(c):
    background(c)
    rrect(c, 0, 0, W, 360, 0, PURPLE)
    pill(c, "MATEMÁTICA ENEM · FUNÇÃO AFIM · EP. 2", W / 2, 80, "#FFFFFF", size=32, anchor="center", bounds=(0, 1920))
    s = "QUANDO O TANQUE SECA?"
    V.ftext(c, s, W / 2, 270, fit(s, 140, 1780), "black", "#FFFFFF")
    V.tanque(c, 160, 430, 700, 560, 1.0, 0.62)
    V.ftext(c, "500 L", 510, 760, 90, "black", "#FFFFFF")
    V.tabela(c, 940, 460, ["0", "1", "2"], ["500", "440", "380"], 1.0, cw=220, rot_x="horas", rot_y="litros",
             diffs=["−60", "−60"], a_diff=1.0)
    shadow_rrect(c, 1000, 820, 820, 150, 30, 1, 1.4)
    rrect(c, 1000, 820, 820, 150, 30, "#FFFFFF")
    V.ftext(c, "8,3 h = 8 h 30 min?", 1410, 920, 72, "black", AMBER)


if __name__ == "__main__":
    for nome, fn in (("capa_A_vela_acaba_quando", capa_vela), ("capa_B_taxa_uma_fracao", capa_fracao),
                     ("capa_C_tanque_seca", capa_tanque)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
