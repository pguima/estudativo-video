"""Capas — Comparação de Propostas e Tomada de Decisão, Episódio 1: a regra de ouro, comparar na mesma data (tema claro).
3 variações em 1280x720. Formatos: A = três sacos de dinheiro crescendo da esquerda para a direita, com os valores e as
datas, título "QUAL VOCÊ ESCOLHE?" no alto e o selo âmbar "O MAIOR?"; B = o televisor no centro entre duas etiquetas
gigantes (À VISTA R$ 2.900 × 3 × R$ 1.000), título "À VISTA OU PARCELADO?" em duas linhas; C = linha do tempo larga com
a bandeirinha DATA FOCAL fincada e o título "COMPARE NA MESMA DATA" à esquerda (sem a resposta)."""
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
motor.set_theme("claro")


def fit(s, size, maxw, peso="black"):
    while text_w(s, peso, size) > maxw:
        size -= 4
    return size


def selo_topo(c, cx=None):
    s = "MATEMÁTICA ENEM · PROPOSTAS · EP. 1"
    if cx is None:
        pill(c, s, 84, 90, BLUE, size=34, bounds=(0, 1920))
    else:
        pill(c, s, cx, 90, BLUE, size=34, anchor="center", bounds=(0, 1920))


def capa_sacos(c):
    background(c); selo_topo(c, W / 2)
    s = "QUAL VOCÊ ESCOLHE?"
    text(c, s, W / 2, 290, fit(s, 150, 1760), "black", INK)
    for k, (v, rot) in enumerate(((10000, "HOJE"), (11000, "EM 1 ANO"), (12100, "EM 2 ANOS"))):
        x = 400 + k * 560
        V.saco(c, x, 690, V._r_saco(v, 210), f"{v:,.0f}".replace(",", "."), 1.0)
        text(c, rot, x, 990, 56, "black", PURPLE if k else BLUE)
    V.selo(c, 1700, 880, 1.0, "O MAIOR?", AMBER, -6, 60)


def capa_tv(c):
    background(c); selo_topo(c)
    text(c, "À VISTA OU", 84, 300, 150, "black", INK, align="left")
    text(c, "PARCELADO?", 84, 450, 150, "black", PURPLE, align="left")
    rrect(c, 760, 560, 400, 260, 26, INK, shadow=True)
    rrect(c, 780, 580, 360, 200, 14, mix(BLUE, "#FFFFFF", 0.55))
    rrect(c, 920, 820, 80, 40, 6, INK2)
    for x, tit, val, col in ((330, "À VISTA", "R$ 2.900", BLUE), (1590, "PARCELADO", "3 × 1.000", PURPLE)):
        rrect(c, x - 290, 590, 580, 300, 36, "#FFFFFF", shadow=True)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x - 290, 590, 580, 300), 36, 36), paint(col, 1.0, stroke=10))
        text(c, tit, x, 680, 54, "black", col, tracking=3)
        text(c, val, x, 830, fit(val, 110, 520), "black", INK)
    V.selo(c, 1560, 330, 1.0, "QUAL COMPENSA?", AMBER, -5, 60)


def capa_bandeira(c):
    background(c); selo_topo(c)
    text(c, "COMPARE NA", 84, 300, 140, "black", INK, align="left")
    text(c, "MESMA DATA", 84, 440, 140, "black", GREEN, align="left")
    y = 820
    line(c, 120, y, 1800, y, INK2, 1.0, 12)
    for k, rot in enumerate(("HOJE", "1 ANO", "2 ANOS")):
        x = 260 + k * 700
        c.drawCircle(x, y, 26, paint(GREEN if k == 2 else INK2))
        text(c, rot, x, y + 100, 56, "black", GREEN if k == 2 else GRAY)
    x = 1660
    line(c, x, y, x, y - 420, INK2, 1.0, 14)
    pth = skia.Path()
    pth.moveTo(x, y - 420); pth.lineTo(x + 230, y - 360); pth.lineTo(x, y - 300); pth.close()
    c.drawPath(pth, paint(GREEN))
    pill(c, "DATA FOCAL", x, y - 470, GREEN, size=48, anchor="center", bounds=(0, 1920))
    for k, v in enumerate((10000, 11000)):
        V.saco(c, 260 + k * 700, y - 170, V._r_saco(v, 120), f"{v:,.0f}".replace(",", "."), 1.0)
        arrow(c, 400 + k * 700, y - 170, 1500, y - 170 - 0 * k, GREEN, 1.0, 10, 30) if k == 1 else None


if __name__ == "__main__":
    for nome, fn in (("capa_A_qual_voce_escolhe", capa_sacos), ("capa_B_a_vista_ou_parcelado", capa_tv),
                     ("capa_C_mesma_data", capa_bandeira)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
