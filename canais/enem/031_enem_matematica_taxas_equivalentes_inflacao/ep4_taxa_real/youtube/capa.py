"""Capas — Taxas Equivalentes e Inflação, Episódio 4: taxa real e a armadilha da subtração (tema claro). 3 variações em
1280x720. Formatos (sem repetir a escada rolante da capa C do ep. 3): A = duelo extrato × etiqueta de preço, com a
pergunta embaixo; B = manchete de jornal ocupando a capa, com a conta sublinhada e um "?" gigante; C = sinal de menos
riscado contra o sinal de dividir, enormes. Nenhuma mostra resposta."""
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
    s = "MATEMÁTICA ENEM · TAXA REAL · EP. 4"
    if cx is None:
        pill(c, s, 84, 90, BLUE, size=34, bounds=(0, 1920))
    else:
        pill(c, s, cx, 90, BLUE, size=34, anchor="center", bounds=(0, 1920))


def capa_duelo(c):
    background(c); selo_topo(c, W / 2)
    for k, (tit, val, col, sub) in enumerate((("POUPANÇA", "+8%", GREEN, "o saldo subiu"),
                                              ("PREÇOS", "+10%", RED, "a inflação subiu mais"))):
        x = 150 + k * 860
        shadow_rrect(c, x, 190, 760, 480, 40, 1, 1.4)
        rrect(c, x, 190, 760, 480, 40, "#FFFFFF")
        rrect(c, x, 190, 760, 110, 40, col, 0.14)
        text(c, tit, x + 380, 270, 60, "black", col)
        text_mid(c, val, x + 380, 470, 230, "black", col)
        text(c, sub, x + 380, 630, 44, "extrabold", INK2)
    text_mid(c, "×", W / 2, 430, 120, "black", INK2)
    s = "VOCÊ FICOU MAIS POBRE?"
    sz = fit(s, 130, 1760)
    w = text_w(s, "black", sz) + 100
    shadow_rrect(c, W / 2 - w / 2, 740, w, 220, 30, 1, 1.4)
    rrect(c, W / 2 - w / 2, 740, w, 220, 30, PURPLE)
    text_mid(c, s, W / 2, 850, sz, "black", "#FFFFFF")


def capa_manchete(c):
    background(c)
    rrect(c, 70, 150, W - 140, 860, 20, V.PAPEL)
    selo_topo(c)
    text(c, "O DIÁRIO DA ECONOMIA", W / 2, 260, 64, "black", INK2)
    line(c, 140, 300, W - 140, 300, INK2, 1.0, 5)
    line(c, 140, 314, W - 140, 314, INK2, 1.0, 2)
    s1, s2 = "Juros de 12%, inflação de 5%:", "GANHO REAL DE 7%"
    text(c, s1, W / 2, 460, fit(s1, 110, 1640), "black", INK)
    text(c, s2, W / 2, 620, fit(s2, 150, 1640), "black", INK)
    line(c, 330, 650, 1590, 650, AMBER, 1.0, 14)
    for k in range(4):
        rrect(c, 160, 730 + k * 50, 1100 - 120 * (k % 2), 18, 9, "#DEDBD2")
    V.selo(c, 1560, 820, 1.0, "A MANCHETE ERRA?", RED, -8, 66)


def capa_dividir(c):
    background(c); selo_topo(c, W / 2)
    s = "TAXA REAL: NÃO SUBTRAIA"
    text(c, s, W / 2, 290, fit(s, 130, 1780), "black", INK)
    for k, (op, col, ok) in enumerate((("−", RED, False), ("÷", GREEN, True))):
        cx = 560 + k * 800
        shadow_rrect(c, cx - 300, 360, 600, 560, 50, 1, 1.4)
        rrect(c, cx - 300, 360, 600, 560, 50, "#FFFFFF")
        rrect(c, cx - 300, 360, 600, 560, 50, col, 0.10)
        text_mid(c, op, cx, 610, 400, "black", col)
        lab = "TAXAS" if not ok else "FATORES"
        text(c, lab, cx, 860, 64, "black", col)
        if not ok:
            line(c, cx - 230, 820, cx + 230, 420, RED, 1.0, 26)
    text_mid(c, "→", W / 2 + 0, 640, 140, "black", INK2)


if __name__ == "__main__":
    for nome, fn in (("capa_A_mais_pobre", capa_duelo), ("capa_B_manchete_erra", capa_manchete),
                     ("capa_C_nao_subtraia", capa_dividir)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
