"""Capas — Logaritmos, Episódio 4: equações logarítmicas e a condição de existência (tema claro). 3 variações em 1280x720.
A = o segurança na porta do log barrando o −5 (exemplo do bloco d, "eu faço"), com "ESSA RAIZ NÃO ENTRA";
B = a alternativa {2, −5} gigante com o selo "DESCONFIE" e "AS DUAS RAÍZES ESTÃO LÁ";
C = o roteiro de 4 passos com o quadro das condições, "EQUAÇÃO LOGARÍTMICA EM 4 PASSOS".
Nenhuma mostra gabarito (13 e {4} não aparecem)."""
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


def fit(s, size, maxw, peso="black"):
    while text_w(s, peso, size) > maxw:
        size -= 4
    return size


def selo_topo(c, cx=None):
    s = "MATEMÁTICA ENEM · LOGARITMOS · EP. 4"
    if cx is None:
        pill(c, s, 84, 90, BLUE, size=34, bounds=(0, 1920))
    else:
        pill(c, s, cx, 90, BLUE, size=34, anchor="center", bounds=(0, 1920))


def capa_porta(c):
    background(c); selo_topo(c)
    shadow_rrect(c, 70, 190, 900, 820, 40, 1, 1.4)
    rrect(c, 70, 190, 900, 820, 40, "#FFFFFF")
    # porta grande com a placa log x
    x, y, w, h = 560, 360, 280, 560
    rrect(c, x - 22, y - 22, w + 44, h + 22, 18, mix("#FFFFFF", INK, 0.18))
    rrect(c, x, y, w, h, 12, mix("#FFFFFF", PURPLE, 0.10))
    p = skia.Path()
    p.moveTo(x + w, y); p.lineTo(x + w + 80, y + 36); p.lineTo(x + w + 80, y + h - 36); p.lineTo(x + w, y + h); p.close()
    c.drawPath(p, paint(mix("#FFFFFF", PURPLE, 0.45), 1))
    rrect(c, x + w / 2 - 140, 230, 280, 100, 22, "#FFFFFF", 1, shadow=True)
    V.lrow(c, [("log", "", PURPLE), ("m", "x", PURPLE)], x + w / 2, 280, 64, 1)
    V.seguranca(c, 400, 700, 330, 1, braco=1.0)
    c.drawCircle(190, 830, 82, paint(mix("#FFFFFF", RED, 0.18), 1))
    c.drawCircle(190, 830, 82, paint(RED, 1, stroke=8))
    text_mid(c, "−5", 190, 830, 76, "black", RED)
    check_icon(c, 262, 758, 34, 1, RED, "x")
    s1, s2 = "ESSA RAIZ", "NÃO ENTRA"
    text(c, s1, 1430, 440, fit(s1, 150, 820), "black", INK)
    sz = fit(s2, 140, 780)
    ww = text_w(s2, "black", sz) + 80
    shadow_rrect(c, 1430 - ww / 2, 500, ww, 200, 30, 1, 1.4)
    rrect(c, 1430 - ww / 2, 500, ww, 200, 30, RED)
    text_mid(c, s2, 1430, 600, sz, "black", "#FFFFFF")
    V.selo(c, 1430, 850, 1.0, "A RAIZ PROIBIDA DO ENEM", AMBER, -5, 50)


def capa_duas(c):
    background(c); selo_topo(c, W / 2)
    s = "AS DUAS RAÍZES ESTÃO LÁ"
    text(c, s, W / 2, 300, fit(s, 140, 1780), "black", INK)
    shadow_rrect(c, 460, 400, 1000, 400, 50, 1, 1.4)
    rrect(c, 460, 400, 1000, 400, 50, mix("#FFFFFF", AMBER, 0.20))
    c.drawCircle(560, 480, 56, paint(INK, 1))
    text_mid(c, "C", 560, 480, 64, "black", "#FFFFFF")
    text_mid(c, "{2, −5}", 990, 620, 210, "black", AMBER)
    V.selo(c, 1480, 420, 1.0, "DESCONFIE", RED, -8, 64)
    rrect(c, 0, 900, W, 180, 0, PURPLE)
    text_mid(c, "equação logarítmica: teste o documento", W / 2, 990, 70, "black", "#FFFFFF")


def capa_passos(c):
    background(c); selo_topo(c, W / 2)
    s = "EQUAÇÃO LOGARÍTMICA"
    text(c, s, W / 2, 290, fit(s, 140, 1780), "black", INK)
    for k, s_ in enumerate(V.PASSOS):
        y = 400 + k * 130
        shadow_rrect(c, 160, y - 50, 1000, 104, 26, 1, 1.2)
        rrect(c, 160, y - 50, 1000, 104, 26, "#FFFFFF")
        c.drawCircle(230, y + 2, 36, paint(GREEN if k in (0, 3) else PURPLE, 1))
        text_mid(c, str(k + 1), 230, y + 2, 44, "black", "#FFFFFF")
        text(c, s_.upper(), 290, y + 22, 54, "black", INK, align="left")
    shadow_rrect(c, 1260, 380, 520, 420, 36, 1, 1.4)
    rrect(c, 1260, 380, 520, 420, 36, mix("#FFFFFF", BLUE, 0.12))
    text(c, "CONDIÇÕES", 1520, 460, 40, "black", BLUE, tracking=3)
    text_mid(c, "▢ > 0", 1520, 600, 130, "black", BLUE)
    text(c, "antes de tudo", 1520, 740, 40, "bold", INK2)
    rrect(c, 0, 940, W, 140, 0, GREEN)
    text_mid(c, "em 4 passos, sem raiz proibida", W / 2, 1010, 70, "black", "#FFFFFF")


if __name__ == "__main__":
    for nome, fn in (("capa_A_raiz_nao_entra", capa_porta), ("capa_B_duas_raizes", capa_duas),
                     ("capa_C_quatro_passos", capa_passos)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
