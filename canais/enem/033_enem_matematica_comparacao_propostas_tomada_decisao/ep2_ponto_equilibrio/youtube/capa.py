"""Capas — Comparação de Propostas e Tomada de Decisão, Episódio 2: planos com parte fixa e variável, o ponto de
equilíbrio (tema claro). 3 variações em 1280x720.
Formatos: A = o gráfico das duas retas ocupando a direita, o cruzamento marcado com um "?" gigante, e "EM QUE MINUTO
MUDA?" à esquerda; B = o cofrinho da "dívida" de R$ 30,00 do plano caro no centro, com "QUANDO O PLANO CARO COMPENSA?"
em cima; C = um calendário com os dias 12 e 13 destacados e as duas etiquetas "diária R$ 25" × "mês R$ 300", com
"12 OU 13 DIAS?" (as duas candidatas, sem dizer qual é a certa). Nenhuma mostra a resposta."""
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
    s = "MATEMÁTICA ENEM · PROPOSTAS · EP. 2"
    if cx is None:
        pill(c, s, 84, 90, BLUE, size=34, bounds=(0, 1920))
    else:
        pill(c, s, cx, 90, BLUE, size=34, anchor="center", bounds=(0, 1920))


def capa_grafico(c):
    background(c); selo_topo(c)
    text(c, "EM QUE", 84, 360, 140, "black", INK, align="left")
    text(c, "MINUTO", 84, 510, 140, "black", PURPLE, align="left")
    text(c, "MUDA?", 84, 660, 140, "black", PURPLE, align="left")
    text(c, "plano barato × plano caro", 84, 790, 50, "extrabold", INK2, align="left")
    x0, y0, w, h = 900, 240, 900, 700
    rrect(c, x0 - 40, y0 - 40, w + 80, h + 80, 36, "#FFFFFF", shadow=True)
    px = lambda m: x0 + w * m / 200
    py = lambda v: y0 + h - h * v / 160
    rrect(c, px(0), y0, px(100) - px(0), h, 0, BLUE, 0.10)
    rrect(c, px(100), y0, px(200) - px(100), h, 0, GREEN, 0.12)
    line(c, x0, y0 + h, x0 + w, y0 + h, INK2, 1.0, 8)
    line(c, x0, y0 + h, x0, y0, INK2, 1.0, 8)
    line(c, px(0), py(50), px(200), py(150), BLUE, 1.0, 16)
    line(c, px(0), py(80), px(200), py(120), GREEN, 1.0, 16)
    text_mid(c, "R$ 50", px(0) + 30, py(50) + 50, 44, "black", BLUE, align="left")
    text_mid(c, "R$ 80", px(0) + 30, py(80) - 50, 44, "black", GREEN, align="left")
    c.drawCircle(px(100), py(100), 80, paint("#FFFFFF", 1.0))
    c.drawCircle(px(100), py(100), 80, paint(PURPLE, 1.0, stroke=12))
    text_mid(c, "?", px(100), py(100), 120, "black", PURPLE)


def capa_cofrinho(c):
    background(c); selo_topo(c, W / 2)
    s = "QUANDO O PLANO CARO COMPENSA?"
    text(c, s, W / 2, 270, fit(s, 120, 1780), "black", INK)
    V.porco(c, 760, 680, 1.55, 1.0)
    text_mid(c, "R$ 30", 745, 690, 110, "black", RED)
    rrect(c, 1180, 470, 600, 420, 36, "#FFFFFF", shadow=True)
    text(c, "fixo a mais", 1480, 560, 52, "black", AMBER)
    text_mid(c, "pago de", 1480, 650, 50, "bold", INK2)
    text_mid(c, "R$ 0,30", 1480, 740, 96, "black", GREEN)
    text_mid(c, "em R$ 0,30", 1480, 830, 50, "bold", INK2)


def capa_calendario(c):
    background(c); selo_topo(c)
    text(c, "12 OU 13", 84, 380, 170, "black", INK, align="left")
    text(c, "DIAS?", 84, 560, 170, "black", AMBER, align="left")
    pill(c, "diária R$ 25", 84, 700, BLUE, size=50, bounds=(0, 1920))
    pill(c, "mês R$ 300", 520, 700, GREEN, size=50, bounds=(0, 1920))
    text(c, "o \"a partir de\" que derruba", 84, 840, 48, "extrabold", INK2, align="left")
    x0, y0, cw, ch = 1080, 260, 108, 108
    rrect(c, x0 - 30, y0 - 110, cw * 7 + 60, ch * 5 + 150, 34, "#FFFFFF", shadow=True)
    rrect(c, x0 - 30, y0 - 110, cw * 7 + 60, 90, 34, RED, 0.9)
    text_mid(c, "ESTACIONAMENTO", x0 + cw * 3.5, y0 - 65, 44, "black", "#FFFFFF")
    for d in range(1, 31):
        i = d - 1
        x = x0 + (i % 7) * cw
        y = y0 + (i // 7) * ch
        hot = d in (12, 13)
        if hot:
            rrect(c, x + 6, y + 6, cw - 12, ch - 12, 18, AMBER, 0.9)
        text_mid(c, str(d), x + cw / 2, y + ch / 2, 46 if hot else 36, "black", "#FFFFFF" if hot else INK2)


if __name__ == "__main__":
    for nome, fn in (("capa_A_em_que_minuto_muda", capa_grafico), ("capa_B_plano_caro_compensa", capa_cofrinho),
                     ("capa_C_12_ou_13_dias", capa_calendario)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
