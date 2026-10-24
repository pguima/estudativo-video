"""Capas — Conceito de Função, Episódio 6: Revisão (tema claro). 3 variações em 1280x720.
Formatos: A = "y = f(x)" no centro e os 4 ícones das provas em volta (Física, Química, Biologia, Geografia), com
"1 GRÁFICO · 4 PROVAS"; B = o gráfico da temperatura com as pontas marcadas e "A IMAGEM ESTÁ NAS PONTAS?";
C = três cartões âmbar de pegadinha ("Im = contradomínio?", "f(30) ou x?", "imagem no eixo x?") com "VOCÊ CAI?".
Nenhuma mostra gabarito."""
import importlib.util, subprocess, sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(next(d / "_ferramentas" for d in HERE.parents if (d / "_ferramentas").is_dir())))
import skia
import motor
motor.set_theme("claro")
from motor import *  # noqa

_spec = importlib.util.spec_from_file_location("visual_ep6", HERE.parent / "roteiro" / "visual.py")
V = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(V)
motor.set_theme("claro")


def fit(s, size, maxw, peso="black"):
    while text_w(s, peso, size) > maxw:
        size -= 4
    return size


def selo_topo(c, cx=None):
    s = "MATEMÁTICA ENEM · FUNÇÃO · REVISÃO"
    if cx is None:
        pill(c, s, 84, 90, BLUE, size=34, bounds=(0, 1920))
    else:
        pill(c, s, cx, 90, BLUE, size=34, anchor="center", bounds=(0, 1920))


def capa_provas(c):
    background(c)
    selo_topo(c, W / 2)
    s = "1 GRÁFICO · 4 PROVAS"
    text(c, s, W / 2, 290, fit(s, 140, 1700), "black", INK)
    rrect(c, W / 2 - 330, 470, 660, 230, 40, mix("#FFFFFF", PURPLE, 0.16), 1, shadow=True)
    V.fmid(c, "y = f(x)", W / 2, 585, 130, "black", PURPLE, 1)
    for k, (x, y, col, nome) in enumerate(((260, 520, BLUE, "FÍSICA"), (1660, 520, PURPLE, "QUÍMICA"),
                                          (420, 900, GREEN, "BIOLOGIA"), (1500, 900, AMBER, "GEOGRAFIA"))):
        rrect(c, x - 150, y - 150, 300, 300, 40, mix("#FFFFFF", col, 0.16), 1, shadow=True)
        V.area_icone(c, k, x, y - 20, 0.75, 1)
        text_mid(c, nome, x, y + 115, 40, "black", col, 1)
    pill(c, "pegadinhas + 5 questões", W / 2, 900, GREEN, size=56, anchor="center", bounds=(0, 1920))


def capa_pontas(c):
    background(c)
    rrect(c, 0, 0, W * 0.47, H, 0, mix("#FFFFFF", AMBER, 0.14))
    selo_topo(c)
    for j, (s, col, sz) in enumerate((("A IMAGEM", INK, 120), ("ESTÁ NAS", INK, 120), ("PONTAS?", RED, 150))):
        text(c, s, 84, 340 + j * 170, fit(s, sz, 820), "black", col, align="left")
    c.save(); c.translate(980, 160); c.scale(1.65, 1.65)
    V.grafico_temp(c, 60, 60, 470, 300, 1)
    X = lambda v: 60 + 470 * v / 24
    Y = lambda v: 60 + 300 - 300 * v / 40
    for xv, yv in ((0, 16), (24, 18)):
        c.drawCircle(X(xv), Y(yv), 14, paint(AMBER, 1))
        c.drawCircle(X(xv), Y(yv), 22, paint(AMBER, 1, stroke=4))
    c.restore()
    pill(c, "imagem · máximo · domínio", 1440, 900, BLUE, size=48, anchor="center", bounds=(0, 1920))


def capa_pegadinhas(c):
    background(c)
    selo_topo(c)
    s = "VOCÊ CAI?"
    text(c, s, 84, 330, fit(s, 190, 820), "black", INK, align="left")
    text(c, "9 pegadinhas de função", 84, 450, 64, "black", AMBER, align="left")
    cards = (("Im = contradomínio?", -6), ("dão R$ 30: calculo f(30)?", 3), ("imagem no eixo x?", -3))
    for j, (s, rot) in enumerate(cards):
        c.save(); c.translate(1420, 300 + j * 250); c.rotate(rot)
        rrect(c, -430, -95, 860, 190, 30, mix("#FFFFFF", AMBER, 0.30), 1, shadow=True)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(-430, -95, 860, 190), 30, 30), paint(AMBER, 1, stroke=6))
        V.fmid(c, s, 0, 0, fit(s, 72, 780), "black", INK, 1)
        c.restore()
    c.save(); c.translate(380, 800); c.scale(1.1, 1.1)
    V.porteiro(c, 1)
    c.restore()


if __name__ == "__main__":
    for nome, fn in (("capa_A_um_grafico_quatro_provas", capa_provas), ("capa_B_imagem_nas_pontas", capa_pontas),
                     ("capa_C_voce_cai", capa_pegadinhas)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
