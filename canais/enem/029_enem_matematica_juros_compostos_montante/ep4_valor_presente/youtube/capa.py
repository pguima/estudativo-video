"""Capas — Juros Compostos, Episódio 4: trazendo valores para hoje (tema claro). 3 variações em 1280x720.
Formatos: A = linha do tempo larga (HOJE ? ← DAQUI A 2 ANOS R$ 11.025) com a seta "÷ fator" e o palpite "−5% −5%"
riscado, pergunta no alto; B = a cadeia 100 → 110 → 99 ocupando a capa, título "TIRAR 10% NÃO DESFAZ 10%";
C = fita de filme rodando ao contrário à direita, título "O FILME AO CONTRÁRIO" à esquerda."""
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
    s = "MATEMÁTICA ENEM · JUROS COMPOSTOS · EP. 4"
    if cx is None:
        pill(c, s, 84, 90, BLUE, size=34, bounds=(0, 1920))
    else:
        pill(c, s, cx, 90, BLUE, size=34, anchor="center", bounds=(0, 1920))


def capa_linha(c):
    background(c); selo_topo(c, W / 2)
    s = "QUANTO APLICAR HOJE?"
    text(c, s, W / 2, 270, fit(s, 140, 1780), "black", INK)
    y = 760
    line(c, 260, y, 1660, y, INK2, 1.0, 10)
    for x, rot in ((260, "HOJE"), (1660, "DAQUI A 2 ANOS")):
        c.drawCircle(x, y, 26, paint(INK2))
        text(c, rot, x, y + 90, 44, "black", GRAY)
    for x, val, col in ((420, "?", BLUE), (1500, "R$ 11.025", PURPLE)):
        rrect(c, x - 260, 400, 520, 200, 36, "#FFFFFF", shadow=True)
        text_mid(c, val, x, 500, 96 if val != "?" else 140, "black", col)
    arrow(c, 1200, 650, 720, 650, PURPLE, 1.0, 12, 40)
    pill(c, "÷ fator", 960, 700, PURPLE, size=48, anchor="center", bounds=(0, 1920))
    rrect(c, 1240, 900, 560, 140, 30, mix("#FFFFFF", RED, 0.08))
    text_mid(c, "−5% −5%?", 1520, 970, 80, "black", RED)
    V.strike(c, 1280, 1000, 1760, 940, 1.0, RED)


def capa_cadeia(c):
    background(c); selo_topo(c)
    text(c, "TIRAR 10%", 84, 330, 150, "black", INK, align="left")
    text(c, "NÃO DESFAZ 10%", 84, 490, 150, "black", AMBER, align="left")
    for k, (val, op, col) in enumerate((("100", "", INK), ("110", "+10%", GREEN), ("99", "−10%", RED))):
        x = 330 + k * 630
        rrect(c, x - 230, 640, 460, 260, 40, "#FFFFFF", shadow=True)
        text_mid(c, val, x, 770, 170, "black", col)
        if op:
            arrow(c, x - 600 + 240, 770, x - 250, 770, col, 1.0, 12, 34)
            pill(c, op, x - 315, 680, col, size=44, anchor="center", bounds=(0, 1920))
    V.selo(c, 1580, 990, 1.0, "NÃO VOLTA!", RED, -6, 60)


def capa_filme(c):
    background(c); selo_topo(c)
    text(c, "O FILME", 84, 330, 150, "black", INK, align="left")
    text(c, "AO CONTRÁRIO", 84, 490, fit("AO CONTRÁRIO", 130, 1040), "black", PURPLE, align="left")
    text(c, "do futuro para hoje:", 84, 650, 60, "extrabold", INK2, align="left")
    text(c, "multiplica ou divide?", 84, 740, 60, "extrabold", AMBER, align="left")
    V.filme(c, 1540, 430, 1.0, -1, w=640, h=240)
    V.filme(c, 1540, 760, 1.0, 1, w=640, h=240)
    text(c, "voltando para HOJE", 1540, 615, 40, "black", PURPLE)


if __name__ == "__main__":
    for nome, fn in (("capa_A_quanto_aplicar_hoje", capa_linha), ("capa_B_tirar_10_nao_desfaz", capa_cadeia),
                     ("capa_C_filme_ao_contrario", capa_filme)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
