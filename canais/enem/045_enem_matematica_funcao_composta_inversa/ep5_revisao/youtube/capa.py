"""Capas — Função Composta e Função Inversa, Episódio 5: Revisão (tema claro). 3 variações em 1280x720.
Formatos: A = "f ∘ g" gigante riscado no topo, com as duas frases do ENEM em balões e o título "SEM O SÍMBOLO";
B = a pegadinha "f⁻¹ = 1/f ?" em fundo escuro, com o selo âmbar "VOCÊ CAI?"; C = a tabela de f e g com a pergunta
"f⁻¹(g(4)) = ?" e uma lupa sobre a linha das saídas. Nenhuma mostra gabarito.
"∘" só existe na fonte do ftext: os textos com ele usam V.fmid/V.ftext.
"""
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
    while V.ftw(s, size, peso) > maxw:
        size -= 4
    return size


def selo_topo(c, cx=None):
    s = "MATEMÁTICA ENEM · COMPOSTA E INVERSA · REVISÃO"
    if cx is None:
        pill(c, s, 84, 90, BLUE, size=34, bounds=(0, 1920))
    else:
        pill(c, s, cx, 90, BLUE, size=34, anchor="center", bounds=(0, 1920))


def capa_simbolo(c):
    background(c)
    selo_topo(c, W / 2)
    rrect(c, 610, 170, 700, 230, 115, "#FFFFFF", 1, shadow=True)
    V.fmid(c, "f ∘ g", W / 2, 285, 170, "black", INK2)
    line(c, 640, 290, 1280, 290, RED, 1, 22)
    for k, (s, col, rot) in enumerate((("“o custo depende das peças, que dependem do tempo”", BLUE, -3),
                                       ("“quanto andou, se pagou R$ 37,00?”", PURPLE, 3))):
        x = 500 + k * 920
        c.save(); c.translate(x, 600); c.rotate(rot)
        rrect(c, -420, -150, 840, 300, 40, mix("#F7F7F5", col, 0.16), 1, shadow=True)
        V.para_nb(c, s, 0, -40, 58, "black", col, 1, 760, 70, align="center")
        c.restore()
    s = "SEM O SÍMBOLO"
    text(c, s, W / 2, 990, fit(s, 150, 1700), "black", GREEN)


def capa_pegadinha(c):
    c.drawRect(skia.Rect.MakeWH(W, H), paint("#16181D", 1))
    pill(c, "MATEMÁTICA ENEM · COMPOSTA E INVERSA · REVISÃO", 84, 90, BLUE, size=34, bounds=(0, 1920))
    V.fmid(c, "f⁻¹(x) = 1/f(x) ?", W / 2, 470, 190, "black", "#FFFFFF")
    V.selo(c, 1500, 700, 1, "VOCÊ CAI?", AMBER, -8, 90)
    text(c, "9 pegadinhas · 5 questões", 120, 920, 74, "black", mix("#FFFFFF", AMBER, 0.5), align="left")


def capa_tabela(c):
    background(c)
    selo_topo(c)
    V.fmid(c, "f⁻¹(g(4)) = ?", 90, 300, 150, "black", INK, align="left")
    x0, y0, cw, rh = 140, 470, 230, 150
    rrect(c, x0, y0, cw * 5, rh * 3, 26, "#FFFFFF", 1, shadow=True)
    for j, (nome, vals, col) in enumerate((("x", V.TAB_X, INK2), ("f(x)", V.TAB_F, V.COL_F), ("g(x)", V.TAB_G, V.COL_G))):
        y = y0 + j * rh
        if j:
            line(c, x0, y, x0 + cw * 5, y, LIGHT, 1, 5)
        V.fmid(c, nome, x0 + cw / 2, y + rh / 2, 64, "black", col)
        for k, v in enumerate(vals):
            V.fmid(c, str(v), x0 + cw * (k + 1.5), y + rh / 2, 76, "black", INK)
    line(c, x0 + cw, y0, x0 + cw, y0 + rh * 3, LIGHT, 1, 5)
    # a lupa sobre a linha das saídas de f
    c.drawCircle(1560, 640, 170, paint("#FFFFFF", 0.35))
    c.drawCircle(1560, 640, 170, paint(INK, 1, stroke=22))
    line(c, 1680, 760, 1790, 870, INK, 1, 40)
    text_mid(c, "SAÍDAS?", 1560, 640, 64, "black", PURPLE)


if __name__ == "__main__":
    for nome, fn in (("capa_A_sem_o_simbolo", capa_simbolo), ("capa_B_voce_cai", capa_pegadinha),
                     ("capa_C_tabela_inversa", capa_tabela)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
