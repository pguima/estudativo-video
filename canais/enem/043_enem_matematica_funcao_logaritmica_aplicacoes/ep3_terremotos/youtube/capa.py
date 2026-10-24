"""Capas — Função logarítmica, Episódio 3: terremotos (tema claro). 3 variações em 1280x720.
A = o sismógrafo riscando o papel em tela cheia, com "× 100 OU × 1 000?" (as duas respostas do gancho, sem dizer qual vale
    para qual pergunta) e a faixa "TERREMOTO NO ENEM";
B = os DOIS PLACARES de "+1 GRAU": amplitude × 10 e energia "× ?";
C = a fórmula de M_w com as duas operações embaralhadas, "QUAL VEM PRIMEIRO?".
Nenhuma mostra gabarito (1 000 vezes da Q3 não aparece como resposta; 7,3 e 3,3 não aparecem)."""
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
    s = "MATEMÁTICA ENEM · FUNÇÃO LOGARÍTMICA · EP. 3"
    if cx is None:
        pill(c, s, 84, 90, BLUE, size=34, bounds=(0, 1920))
    else:
        pill(c, s, cx, 90, BLUE, size=34, anchor="center", bounds=(0, 1920))


def capa_sismografo(c):
    background(c); selo_topo(c)
    s = "DE 5 PARA 7"
    text(c, s, 84, 270, fit(s, 130, 900), "black", INK, align="left")
    V.sismografo(c, 60, 330, 1800, 420, 1.0, prog_=1.0, amp=1.05)
    for k, (s_, col) in enumerate((("× 100", BLUE), ("× 1 000", PURPLE))):
        x = 1180 + k * 470
        shadow_rrect(c, x - 190, 150, 380, 150, 30, 1, 1.4)
        rrect(c, x - 190, 150, 380, 150, 30, "#FFFFFF")
        text_mid(c, s_, x, 225, fit(s_, 96, 330), "black", col)
    text_mid(c, "OU", 1415, 225, 44, "black", INK2)
    V.selo(c, 1415, 345, 1.0, "QUAL?", AMBER, -8, 60)
    rrect(c, 0, 820, W, 260, 0, RED)
    text_mid(c, "TERREMOTO NO ENEM", W / 2, 950, fit("TERREMOTO NO ENEM", 150, 1800), "black", "#FFFFFF")


def capa_placares(c):
    background(c); selo_topo(c, W / 2)
    s = "+1 GRAU NO TERREMOTO"
    text(c, s, W / 2, 300, fit(s, 130, 1780), "black", INK)
    for k, (tit, v, col) in enumerate((("AMPLITUDE", "× 10", BLUE), ("ENERGIA", "× ?", PURPLE))):
        x = 560 + k * 800
        shadow_rrect(c, x - 340, 380, 680, 460, 40, 1, 1.4)
        rrect(c, x - 340, 380, 680, 460, 40, "#FFFFFF")
        rrect(c, x - 340, 380, 680, 110, 40, mix("#FFFFFF", col, 0.2))
        text(c, tit, x, 455, 56, "black", col, tracking=4)
        text_mid(c, v, x, 660, 190, "black", col if k == 0 else AMBER)
    V.selo(c, W / 2, 875, 1.0, "NÃO É IGUAL!", RED, -4, 52)
    rrect(c, 0, 920, W, 160, 0, PURPLE)
    text_mid(c, "amplitude × energia: os dois placares", W / 2, 1000, 66, "black", "#FFFFFF")


def capa_ordem(c):
    background(c); selo_topo(c, W / 2)
    s = "QUAL VEM PRIMEIRO?"
    text(c, s, W / 2, 300, fit(s, 150, 1780), "black", INK)
    shadow_rrect(c, 160, 380, 1600, 260, 46, 1, 1.4)
    rrect(c, 160, 380, 1600, 260, 46, mix("#FFFFFF", PURPLE, 0.10))
    V.lrow(c, V.MW, W / 2, 510, 120, 1)
    for k, (s_, col, rot) in enumerate((("× 2/3", PURPLE, -6), ("− 10,7", AMBER, 6))):
        x = 660 + k * 600
        c.save(); c.translate(x, 800); c.rotate(rot)
        shadow_rrect(c, -220, -80, 440, 160, 34, 1, 1.4)
        rrect(c, -220, -80, 440, 160, 34, "#FFFFFF")
        c.drawCircle(-150, 0, 46, paint(INK, 1))
        text_mid(c, "?", -150, 0, 60, "black", "#FFFFFF")
        text_mid(c, s_, 40, 0, 84, "black", col)
        c.restore()
    rrect(c, 0, 960, W, 120, 0, GREEN)
    text_mid(c, "magnitude de momento sem cair na ordem errada", W / 2, 1020, 56, "black", "#FFFFFF")


if __name__ == "__main__":
    for nome, fn in (("capa_A_cem_ou_mil", capa_sismografo), ("capa_B_dois_placares", capa_placares),
                     ("capa_C_qual_primeiro", capa_ordem)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
