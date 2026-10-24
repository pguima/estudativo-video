"""Capas — Conceito de Função, Episódio 4 (tema claro). 3 variações em 1280x720.
Formatos: A = o gráfico gigante iluminado por duas lanternas, com as sombras azul (chão) e verde (parede) e "AS SOMBRAS
DA CURVA" (sem os intervalos); B = fundo escuro com a circunferência cortada pela régua em pé, dois pontos vermelhos e
"ISSO É FUNÇÃO?"; C = a pegadinha do gancho: a curva com a faixa âmbar de 1 a 4 na parede e "CRESCE ENTRE 1 E 4?"
num balão (sem dizer a resposta)."""
import importlib.util, math, subprocess, sys
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

TAG = "MATEMÁTICA ENEM · FUNÇÕES · EP. 4"


def fit(s, size, maxw, peso="black"):
    while text_w(s, peso, size) > maxw:
        size -= 4
    return size


def capa_sombras(c):
    background(c)
    pill(c, TAG, 84, 90, BLUE, size=34, bounds=(0, 1920))
    s = "AS SOMBRAS"
    text(c, s, 84, 270, fit(s, 170, 900), "black", INK, align="left")
    s2 = "DA CURVA"
    text(c, s2, 84, 430, fit(s2, 170, 900), "black", PURPLE, align="left")
    linha_ = [("chão = ", INK2), ("DOMÍNIO", V.CHAO)]
    V.linha(c, linha_, 84, 600, 70, 1.0, align="left")
    V.linha(c, [("parede = ", INK2), ("IMAGEM", V.PAREDE)], 84, 720, 70, 1.0, align="left")
    pl = V.Plano(1000, 330, 760, 560, (-2, 7), (-1, 5))
    pl.desenha(c, 1.0, nums=False)
    (xa, oy), (xb, _) = pl.P(-1, 0), pl.P(6, 0)
    lx, ly = (xa + xb) / 2, 230
    V.lanterna(c, lx, ly, 1.0, 90, 1.1, raio=[(lx - 30, ly + 26), (lx + 30, ly + 26), (xb + 30, oy), (xa - 30, oy)])
    V.curva(c, pl, V.PTS7, PURPLE, 1.0, 12)
    V.sombra_x(c, pl, -1, 6, 1.0)
    V.sombra_y(c, pl, 1, 4, 1.0)
    text(c, "domínio e imagem sem decorar", W / 2, 1010, 50, "extrabold", GRAY)


def capa_regua(c):
    rrect(c, 0, 0, W, H, 0, "#1C1C1E")
    pill(c, TAG, 84, 90, BLUE, size=34, bounds=(0, 1920))
    s = "ISSO É"
    text(c, s, 84, 330, fit(s, 190, 900), "black", "#FFFFFF", align="left")
    s2 = "FUNÇÃO?"
    text(c, s2, 84, 530, fit(s2, 200, 900), "black", "#FFD54A", align="left")
    text(c, "o teste da régua em pé", 84, 680, 60, "extrabold", "#C7C7CC", align="left")
    cx, cy, r = 1400, 560, 300
    c.drawCircle(cx, cy, r, paint("#6FA0FF", 1.0, stroke=16))
    xx = 160
    V.regua(c, cx + xx, cy - 400, cy + 400, 1.0, PURPLE, 48)
    yy = math.sqrt(r * r - xx * xx)
    for s_ in (1, -1):
        c.drawCircle(cx + xx, cy + s_ * yy, 30, paint(RED, 1.0))
        c.drawCircle(cx + xx, cy + s_ * yy, 30, paint("#FFFFFF", 1.0, stroke=6))
    text(c, "2 toques?", 84, 900, 90, "black", RED, align="left")


def capa_pegadinha(c):
    background(c)
    pill(c, TAG, W / 2, 90, BLUE, size=34, anchor="center", bounds=(0, 1920))
    pl = V.Plano(160, 260, 900, 640, (-2, 7), (-1, 5))
    pl.desenha(c, 1.0, nums=False)
    V.curva(c, pl, V.PTS7, PURPLE, 1.0, 12)
    V.sombra_y(c, pl, 1, 4, 1.0, col=AMBER)
    _, p1 = pl.P(0, 1)
    _, p4 = pl.P(0, 4)
    ox, _ = pl.P(0, 0)
    V.fmid(c, "1", ox - 50, p1, 64, "black", AMBER, 1.0)
    V.fmid(c, "4", ox - 50, p4, 64, "black", AMBER, 1.0)
    rrect(c, 1120, 300, 700, 420, 50, AMBER, 1.0, shadow=True)
    p = skia.Path()
    p.moveTo(1150, 600); p.lineTo(1040, 700); p.lineTo(1200, 660); p.close()
    c.drawPath(p, paint(AMBER, 1.0))
    s = "CRESCE"
    text(c, s, 1470, 450, fit(s, 130, 620), "black", "#FFFFFF")
    s2 = "ENTRE 1 E 4?"
    text(c, s2, 1470, 600, fit(s2, 110, 640), "black", INK)
    text(c, "a troca que derruba no ENEM", 1470, 900, 54, "extrabold", RED)


if __name__ == "__main__":
    for nome, fn in (("capa_A_sombras_da_curva", capa_sombras), ("capa_B_regua_em_pe", capa_regua),
                     ("capa_C_cresce_entre_1_e_4", capa_pegadinha)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
