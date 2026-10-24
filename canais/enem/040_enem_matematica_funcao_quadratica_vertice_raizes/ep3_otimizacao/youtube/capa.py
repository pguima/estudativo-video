"""Capas — Função Quadrática, Episódio 3: otimização, área máxima e receita máxima (tema claro). 3 variações em 1280x720.
A = o muro com dois cercados (o quadrado 20 × 20 e um retângulo comprido), os dois com "? m²", e "QUAL CERCA MAIS?";
B = a etiqueta de preço subindo e os 4 cartões AUMENTO · PREÇO · VENDAS · RECEITA com "?" e "QUAL ELE PEDIU?";
C = a parábola com o ponto no topo e "ONDE FICA O MÁXIMO?" numa faixa roxa.
Nenhuma mostra gabarito (800 m², R$ 45,00, 200 m² e 450 m² não aparecem)."""
import importlib.util, subprocess, sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(next(d / "_ferramentas" for d in HERE.parents if (d / "_ferramentas").is_dir())))
import skia
import motor
motor.set_theme("claro")
from motor import *  # noqa

_spec = importlib.util.spec_from_file_location("visual_ep3", HERE.parent / "roteiro" / "visual.py")
V = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(V)
motor.set_theme("claro")


def fit(s, size, maxw, peso="black"):
    while text_w(s, peso, size) > maxw:
        size -= 4
    return size


def selo_topo(c, cx=None):
    s = "MATEMÁTICA ENEM · FUNÇÃO QUADRÁTICA · EP. 3"
    if cx is None:
        pill(c, s, 84, 90, BLUE, size=34, bounds=(0, 1920))
    else:
        pill(c, s, cx, 90, BLUE, size=34, anchor="center", bounds=(0, 1920))


def capa_cercados(c):
    background(c); selo_topo(c, W / 2)
    s = "QUAL CERCA MAIS?"
    text(c, s, W / 2, 300, fit(s, 170, 1780), "black", INK)
    V.muro(c, W / 2, 440, 1700, 1)
    V.cercado(c, 520, 440, 20, 20, 19, 1, RED, medidas=False, area_col=RED, fill=0.14)
    V.cercado(c, 1330, 440, 15, 30, 19, 1, GREEN, medidas=False)
    for cx, lat, fr in ((520, 20, 20), (1330, 15, 30)):
        text_mid(c, "? m²", cx, 440 + lat * 19 / 2, 110, "black", INK)
        text(c, f"{lat} × {fr}", cx, 440 + lat * 19 + 90, 64, "black", INK2)
    rrect(c, 0, 960, W, 120, 0, AMBER)
    text_mid(c, "a mesma tela: 60 metros", W / 2, 1020, 64, "black", "#FFFFFF")


def capa_comando(c):
    background(c); selo_topo(c)
    V.etiqueta(c, 420, 400, "R$ 20 → ?", 1, AMBER, 96)
    s1, s2 = "QUAL", "ELE PEDIU?"
    text(c, s1, 1400, 330, fit(s1, 190, 800), "black", INK)
    sz = fit(s2, 130, 820)
    w = text_w(s2, "black", sz) + 70
    shadow_rrect(c, 1400 - w / 2, 390, w, 200, 30, 1, 1.4)
    rrect(c, 1400 - w / 2, 390, w, 200, 30, PURPLE)
    text_mid(c, s2, 1400, 490, sz, "black", "#FFFFFF")
    for k, (rot, col) in enumerate((("AUMENTO", INK), ("PREÇO", AMBER), ("VENDAS", BLUE), ("RECEITA", GREEN))):
        x = 270 + k * 460
        shadow_rrect(c, x - 200, 700, 400, 300, 34, 1, 1.4)
        rrect(c, x - 200, 700, 400, 300, 34, "#FFFFFF")
        text(c, rot, x, 790, 54, "black", INK2)
        text_mid(c, "?", x, 900, 130, "black", col)


def capa_topo(c):
    background(c); selo_topo(c)
    pl = V.Plano(160, 900, 900, 640, 30, 500)
    line(c, 130, 900, 1100, 900, INK2, 1, 8)
    pl.curva(c, lambda x: x * (60 - 2 * x), 0, 30, PURPLE, 1, 1, 16)
    px, py = pl.P(15, 450)
    line(c, px, py, px, 900, AMBER, 1, 6)
    c.drawCircle(px, py, 38, paint(AMBER, 1)); c.drawCircle(px, py, 38, paint(INK, 1, stroke=8))
    text(c, "MÁXIMO", px, py - 70, 70, "black", AMBER)
    s1, s2 = "ONDE FICA", "O TOPO?"
    text(c, s1, 1480, 420, fit(s1, 150, 780), "black", INK)
    sz = fit(s2, 150, 760)
    w = text_w(s2, "black", sz) + 70
    shadow_rrect(c, 1480 - w / 2, 480, w, 210, 30, 1, 1.4)
    rrect(c, 1480 - w / 2, 480, w, 210, 30, GREEN)
    text_mid(c, s2, 1480, 585, sz, "black", "#FFFFFF")
    V.selo(c, 1480, 820, 1.0, "ÁREA E RECEITA MÁXIMAS", PURPLE, -4, 50)


if __name__ == "__main__":
    for nome, fn in (("capa_A_qual_cerca_mais", capa_cercados), ("capa_B_qual_ele_pediu", capa_comando),
                     ("capa_C_onde_fica_o_topo", capa_topo)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
