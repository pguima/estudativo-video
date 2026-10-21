"""Capas — Redação ENEM, Leitura da Proposta, Episódio 5: oficina dos 6 passos (tema claro). 3 variações em 1280x720."""
import importlib.util, subprocess, sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(next(d / "_ferramentas" for d in HERE.parents if (d / "_ferramentas").is_dir())))
import skia
import motor
motor.set_theme("claro")
from motor import *  # noqa

_spec = importlib.util.spec_from_file_location("visual_ep5", HERE.parent / "roteiro" / "visual.py")
V = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(V)
motor.set_theme("claro")


def big(c, s, y, maxw=1000, size=140):
    while text_w(s, "black", size) > maxw:
        size -= 4
    text(c, s, 80, y, size, "black", INK, align="left")


def boxed(c, s, x, y, size, bg_col, fg="#FFFFFF", pad=34):
    w = text_w(s, "black", size) + pad * 2
    h = size * 1.22
    shadow_rrect(c, x, y, w, h, 22, 1, 1.4)
    rrect(c, x, y, w, h, 22, bg_col)
    text_mid(c, s, x + w / 2, y + h / 2, size, "black", fg)


def selo(c):
    pill(c, "REDAÇÃO ENEM · EPISÓDIO 5", 84, 90, BLUE, size=40, bounds=(0, 1920))


def painel(c):
    card(c, 1120, 120, 700, 840, r=36)


def capa_passos(c):
    background(c); selo(c)
    V.checklist(c, None, 1, feitos=6, x=1150, y=170, w=640)
    big(c, "6 PASSOS", 340)
    big(c, "DO TEMA", 470)
    boxed(c, "ATÉ A TESE", 70, 520, 140, GREEN)
    text(c, "oficina com um tema real do ENEM", 90, 860, 50, "extrabold", INK2, align="left")


def capa_bloco(c):
    background(c); selo(c); painel(c)
    text(c, "CONFERÊNCIA", 1470, 230, 40, "black", GREEN, tracking=2)
    rows = [("invisibilidade", True), ("registro civil", True), ("acesso à cidadania", True), ("no Brasil", False)]
    for k, (s, ok) in enumerate(rows):
        y = 340 + k * 140
        rrect(c, 1180, y - 50, 580, 100, 18, mix("#FFFFFF", GREEN if ok else RED, 0.12))
        text(c, s, 1220, y + 14, 42, "black", INK, align="left")
        check_icon(c, 1700, y, 34, 1, GREEN if ok else RED, "check" if ok else "x")
    big(c, "SUA TESE", 340)
    big(c, "ESQUECEU", 470)
    boxed(c, "UM BLOCO?", 70, 520, 140, RED)
    text(c, "confira antes de desenvolver", 90, 860, 50, "extrabold", INK2, align="left")


def capa_papel(c):
    background(c); selo(c)
    V.paper(c, 1130, 140, 700, 800, 1, lh=60, top=220)
    V.hand(c, "1. frase temática", 1240, 300, 44, V.PEN)
    V.hand(c, "2. blocos", 1240, 360, 44, V.PEN)
    V.hand(c, "3. motivadores", 1240, 420, 44, V.PEN)
    V.hand(c, "4. pergunta", 1240, 480, 44, V.PEN)
    V.hand(c, "5. tese", 1240, 540, 44, V.PEN)
    V.hand(c, "6. conferência", 1240, 600, 44, GREEN, bold=True)
    V.pen_draw(c, 1600, 820, V.PEN, 1, -35, 1.6)
    big(c, "OFICINA:", 340)
    big(c, "PEGUE PAPEL", 470)
    boxed(c, "E CANETA", 70, 520, 150, BLUE)
    text(c, "a leitura da proposta, ao vivo, até a tese", 90, 860, 46, "extrabold", INK2, align="left")


if __name__ == "__main__":
    for nome, fn in (("capa_A_esqueceu_bloco", capa_bloco), ("capa_B_seis_passos", capa_passos), ("capa_C_papel_caneta", capa_papel)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
