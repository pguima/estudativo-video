"""Capas — Equação do 2º Grau e Bhaskara, Episódio 6: Revisão (tema claro). 3 variações em 1280x720.
Formatos: A = mosaico 2 × 2 dos disfarces (jardim, bola, apertos de mão, lucro) em volta de uma ficha central
"ax² + bx + c = 0", com "TUDO VIRA x²"; B = a LIXEIRA gigante e duas raízes no ar ("6 ou −8?"), "QUAL RAIZ VAI PRO LIXO?";
C = a fórmula de Bhaskara enorme com três círculos âmbar numerados nas armadilhas (b², −b, 2a) e "ONDE VOCÊ ERRA?".
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
K = V.K


def fit(s, size, maxw, peso="black"):
    while text_w(s, peso, size) > maxw:
        size -= 4
    return size


def selo_topo(c, cx=None):
    s = "MATEMÁTICA ENEM · 2º GRAU · REVISÃO"
    if cx is None:
        pill(c, s, 84, 90, BLUE, size=34, bounds=(0, 1920))
    else:
        pill(c, s, cx, 90, BLUE, size=34, anchor="center", bounds=(0, 1920))


def capa_mosaico(c):
    background(c); selo_topo(c)
    s = "TUDO VIRA x²"
    text(c, s, 560, 330, fit(s, 170, 980), "black", INK, align="center")
    text(c, "jardim · bola · jogos · lucro", 560, 470, 60, "black", INK2, align="center")
    pill(c, "9 pegadinhas · 5 questões", 560, 600, AMBER, size=52, anchor="center", bounds=(0, 1920))
    # mosaico 2 x 2 à direita
    cel = [(1240, 270, GRAMA_BG, "jardim"), (1600, 270, mix("#FFFFFF", BLUE, 0.2), "bola"),
           (1240, 700, mix("#FFFFFF", AMBER, 0.25), "mao"), (1600, 700, mix("#FFFFFF", GREEN, 0.2), "lucro")]
    for x, y, col, k in cel:
        rrect(c, x - 170, y - 190, 340, 380, 30, col, 1, shadow=True)
        if k == "jardim":
            c.save(); c.translate(x, y); c.scale(1.05, 1.05); V.jardim_simples(c, 1); c.restore()
        elif k == "bola":
            V.area_icone(c, 4, x, y + 20, 1.0, 1)
        elif k == "mao":
            V.area_icone(c, 3, x, y + 30, 0.85, 1)
        else:
            text_mid(c, "R$", x, y, 170, "black", GREEN, 1)
    rrect(c, 1100, 440, 640, 120, 30, INK, 1, shadow=True)
    V.mx(c, "ax^2 + bx + c = 0", 1420, 500, 72, "#FFFFFF", 1.0, align="center")


GRAMA_BG = mix("#FFFFFF", "#7CC47F", 0.25)


def capa_lixeira(c):
    background(c); selo_topo(c, W / 2)
    s = "QUAL RAIZ VAI PRO LIXO?"
    text(c, s, W / 2, 290, fit(s, 140, 1760), "black", INK)
    V.lixeira(c, W / 2, 740, 3.2, 1)
    for x, s, ang in ((560, "x = 6", -8), (1360, "x = −8", 8)):
        c.save(); c.translate(x, 560); c.rotate(ang)
        rrect(c, -230, -95, 460, 190, 36, "#FFFFFF", 1, shadow=True)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(-230, -95, 460, 190), 36, 36), paint(AMBER, 1, stroke=10))
        text_mid(c, s, 0, 0, 100, "black", INK, 1)
        c.restore()
    text_mid(c, "?", 560, 760, 150, "black", AMBER, 1)
    text_mid(c, "?", 1360, 760, 150, "black", AMBER, 1)


def capa_bhaskara(c):
    background(c)
    rrect(c, 0, 0, W, 330, 0, mix("#FFFFFF", PURPLE, 0.14))
    selo_topo(c)
    s = "ONDE VOCÊ ERRA?"
    text(c, s, W / 2, 285, fit(s, 130, 1500), "black", PURPLE)
    rrect(c, 260, 380, 1400, 520, 40, "#FFFFFF", 1, shadow=True)
    V.mx(c, "x = {-b±√{b^2-4ac}}/2a", W / 2, 640, 170, INK, 1.0, align="center")
    for n, x, y in ((1, 1230, 440), (2, 560, 520), (3, 1110, 870)):
        c.drawCircle(x, y, 58, paint(AMBER, 1))
        text_mid(c, str(n), x, y, 70, "black", "#FFFFFF", 1)
    text(c, "3 armadilhas na mesma fórmula", W / 2, 1010, 62, "black", INK2)


if __name__ == "__main__":
    for nome, fn in (("capa_A_tudo_vira_x2", capa_mosaico), ("capa_B_qual_raiz_vai_pro_lixo", capa_lixeira),
                     ("capa_C_onde_voce_erra", capa_bhaskara)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
