"""Capas — Sistemas de Equações Lineares, Episódio 2: o método da adição e quando a pergunta já é a soma (tema claro).
3 variações em 1280x720, sem gabarito: A = as duas notas fiscais e "juntos: R$ ?" (sem calcular nenhum preço);
B = o laço "× 3" e o lado direito com "?"; C = duelo SOME × SUBTRAIA com as duas colunas."""
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


def fit(s, size, maxw, peso="black"):
    while text_w(s, peso, size) > maxw:
        size -= 4
    return size


def selo_topo(c, cx=None):
    s = "MATEMÁTICA ENEM · SISTEMAS · EP. 2"
    if cx is None:
        pill(c, s, 84, 90, PURPLE, size=34, bounds=(0, 1920))
    else:
        pill(c, s, cx, 90, PURPLE, size=34, anchor="center", bounds=(0, 1920))


def escala(c, x, y, k, fn):
    c.save(); c.translate(x, y); c.scale(k, k); c.translate(-x, -y); fn(); c.restore()


def capa_notas(c):
    background(c); selo_topo(c)
    s = "A RESPOSTA"
    text(c, s, 90, 290, fit(s, 150, 900), "black", INK, align="left")
    text(c, "SEM RESOLVER?", 90, 420, fit("SEM RESOLVER?", 130, 900), "black", GREEN, align="left")
    escala(c, 1040, 420, 1.1, lambda: (V.nota(c, 1040, 330, 2, 1, "R$ 31,00", 1.0, 360),
                                       V.nota(c, 1420, 330, 1, 2, "R$ 26,00", 1.0, 360)))
    shadow_rrect(c, 90, 560, 900, 340, 36, 1, 1.4)
    rrect(c, 90, 560, 900, 340, 36, "#FFFFFF")
    V.sanduiche(c, 300, 690, 130, 1.0)
    text_mid(c, "+", 460, 690, 110, "black", INK2)
    V.suco(c, 620, 690, 130, 1.0)
    text(c, "juntos = R$ ?", 540, 860, 76, "black", PURPLE)
    text(c, "sem o preço de nenhum dos dois", 1500, 990, 50, "extrabold", AMBER)


def capa_laco(c):
    background(c); selo_topo(c, W / 2)
    s = "MULTIPLICOU? VAI ATÉ O FIM"
    text(c, s, W / 2, 270, fit(s, 120, 1780), "black", INK)
    shadow_rrect(c, 200, 400, 1520, 300, 40, 1, 1.4)
    rrect(c, 200, 400, 1520, 300, 40, "#FFFFFF")
    x0 = 470
    cols = (0, 260, 500, 720, 950)
    for j, tk in enumerate(("2x", "+", "3y", "=", "12")):
        V.m(c, tk, x0 + cols[j], 550, 130, col=AMBER if j == 4 else INK)
    V.laco(c, 330, 460, 1330, 180, 1.0, "", PURPLE)
    V.chip(c, "× 3", 240, 550, PURPLE, 1.0, 70)
    for j, tk in enumerate(("6x", "+", "9y", "=", "?")):
        V.m(c, tk, x0 + cols[j], 870, 120, col=RED if j == 4 else PURPLE)
    text(c, "e o 12, multiplica também?", W / 2, 1010, 56, "black", RED)


def capa_duelo(c):
    background(c); selo_topo(c, W / 2)
    s = "SOMA OU SUBTRAI?"
    text(c, s, W / 2, 270, fit(s, 140, 1780), "black", INK)
    for k, (eqs, hl, col, rot) in enumerate(((["3x + 2y = 16", "5x - 2y = 16"], {(0, 1): AMBER, (0, 2): AMBER, (1, 1): AMBER,
                                                                              (1, 2): AMBER}, BLUE, "?"),
                                             (["6x + 9y = 36", "6x + 4y = 26"], {(0, 0): AMBER, (1, 0): AMBER}, PURPLE, "?"))):
        x = 140 + k * 860
        shadow_rrect(c, x, 380, 780, 560, 36, 1, 1.3)
        rrect(c, x, 380, 780, 560, 36, mix("#FFFFFF", col, 0.08))
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, 380, 780, 560), 36, 36), paint(col, 1.0, stroke=6))
        V.sistema(c, x + 170, 540, eqs, 76, 1.0, hl, col_x=(0, 130, 250, 370, 480), chave=False)
        V.traco(c, x + 170, 760, 1.0, rot, col, col_x=(0, 130, 250, 370, 480))
    text(c, "qual letra some?", W / 2, 1030, 54, "extrabold", AMBER)


if __name__ == "__main__":
    for nome, fn in (("capa_A_resposta_sem_resolver", capa_notas), ("capa_B_laco_ate_o_fim", capa_laco),
                     ("capa_C_soma_ou_subtrai", capa_duelo)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
