"""Capas — Matrizes, Episódio 2: operações casa a casa (tema claro). 3 variações em 1280x720.
A = as duas planilhas de notas da Questão 8 com "6,0 APROVA?" e "6 MÉDIAS, 1 CONTA";
B = as duas folhas transparentes (A e B) se sobrepondo, "CASA COM CASA";
C = o carimbo ×3 batendo só na 1ª linha, com "3 · A: SÓ A 1ª LINHA?".
Nenhuma mostra gabarito (a contagem 4 e a matriz M não aparecem)."""
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
    s = "MATEMÁTICA ENEM · MATRIZES · EP. 2"
    if cx is None:
        pill(c, s, 84, 90, BLUE, size=34, bounds=(0, 1920))
    else:
        pill(c, s, cx, 90, BLUE, size=34, anchor="center", bounds=(0, 1920))


def capa_media(c):
    background(c); selo_topo(c)
    c.save(); c.translate(80, 170); c.scale(1.3, 1.3)
    V.planilha(c, 215, 300, V.QA, 1, "PROVA 1", BLUE, alunos=("aluno 1", "aluno 2", "aluno 3"))
    V.planilha(c, 665, 300, V.QB, 1, "PROVA 2", PURPLE, alunos=("aluno 1", "aluno 2", "aluno 3"))
    c.restore()
    s1 = "6,0 APROVA?"
    text(c, s1, 1570, 470, fit(s1, 150, 600), "black", INK)
    ww = 600
    shadow_rrect(c, 1570 - ww / 2, 540, ww, 190, 30, 1, 1.4)
    rrect(c, 1570 - ww / 2, 540, ww, 190, 30, AMBER)
    text_mid(c, "6 médias, 1 conta", 1570, 635, fit("6 médias, 1 conta", 90, ww - 60), "black", "#FFFFFF")
    rrect(c, 0, 940, W, 140, 0, PURPLE)
    text_mid(c, "M = 0,4A + 0,6B", W / 2, 1010, 80, "black", "#FFFFFF")


def capa_folhas(c):
    background(c); selo_topo(c, W / 2)
    s = "CASA COM CASA"
    text(c, s, W / 2, 300, fit(s, 170, 1780), "black", INK)
    V.folha(c, 760, 620, 560, 460, 1, BLUE, "A")
    V.matriz(c, 760, 620, V.A_SOMA, 1, 200, 170, 90, br=BLUE)
    V.folha(c, 1160, 680, 560, 460, 0.8, PURPLE, "B")
    V.matriz(c, 1160, 680, V.B_SOMA, 1, 200, 170, 90, cores={k: PURPLE for k in V.CASAS}, br=PURPLE)
    V.selo(c, 1600, 420, 1.0, "SOMA = ?", AMBER, -8, 60)


def capa_carimbo(c):
    background(c); selo_topo(c, W / 2)
    s = "3 · A: SÓ A 1ª LINHA?"
    text(c, s, W / 2, 300, fit(s, 140, 1780), "black", INK)
    text_mid(c, "3 ·", 560, 640, 150, "black", PURPLE)
    V.matriz(c, 960, 640, V.A_SOMA, 1, 240, 200, 110)
    for j in range(2):
        V.carimbo(c, 960 - 260 + 20 + 240 * (j + 0.5) + 105, 640 - 210 + 10 + 100 - 75, 1, r=56)
    for j in range(2):
        cx = 960 - 260 + 20 + 240 * (j + 0.5)
        c.drawCircle(cx + 105, 640 + 55, 46, paint(mix("#FFFFFF", AMBER, 0.3), 1))
        text_mid(c, "?", cx + 105, 640 + 55, 64, "black", AMBER)
    V.selo(c, 1560, 640, 1.0, "E A 2ª LINHA?", RED, -8, 58)
    rrect(c, 0, 940, W, 140, 0, GREEN)
    text_mid(c, "número vezes matriz: o carimbo em cada casa", W / 2, 1010, 62, "black", "#FFFFFF")


if __name__ == "__main__":
    for nome, fn in (("capa_A_seis_aprova", capa_media), ("capa_B_casa_com_casa", capa_folhas),
                     ("capa_C_carimbo", capa_carimbo)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
