"""Capas — Redação ENEM, Leitura da Proposta, Episódio 1: O que a prova pede (tema claro). 3 variações em 1280x720."""
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
    pill(c, "REDAÇÃO ENEM · EPISÓDIO 1", 84, 90, BLUE, size=40, bounds=(0, 1920))


def painel(c):
    card(c, 1120, 120, 700, 840, r=36)


def capa_primeira_linha(c):
    background(c); selo(c); painel(c)
    V.proposta_page(c, 1200, 170, 540, 560, 1, hl=(0, 0, 1))
    for k, (cn, cap) in enumerate((("C2", 1), ("C3", 1), ("C5", 1))):
        x = 1250 + k * 170
        rrect(c, x, 790, 140, 120, 18, mix("#FFFFFF", RED, 0.12))
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, 790, 140, 120), 18, 18), paint(RED, 1, stroke=4))
        text(c, cn, x + 70, 840, 36, "black", INK2)
        text(c, "40", x + 70, 893, 46, "black", RED)
    big(c, "A REDAÇÃO", 340)
    big(c, "COMEÇA", 470)
    boxed(c, "ANTES DA 1ª LINHA", 70, 548, 100, RED)
    text(c, "o que a prova de redação realmente pede", 90, 860, 48, "extrabold", INK2, align="left")


def capa_endereco(c):
    background(c); selo(c); painel(c)
    rows = [("CIDADE", "envelhecimento", 1, BLUE, "ASSUNTO", 1),
            ("ENDEREÇO COMPLETO", "Perspectivas acerca do envelhecimento na sociedade brasileira", 1, BLUE, "TEMA", 1)]
    V.etiqueta(c, 1160, 170, 620, 1, rows)
    V.caixa(c, 1310, 720, 320, 190, 1, open_=1.0)
    rrect(c, 1400, 650, 140, 80, 12, BLUE)
    text_mid(c, "TESE", 1470, 690, 34, "black", "#FFFFFF")
    big(c, "ASSUNTO,", 340)
    big(c, "TEMA E", 470)
    boxed(c, "TESE", 70, 520, 160, BLUE)
    text(c, "a diferença que destrava a redação do ENEM", 90, 860, 48, "extrabold", INK2, align="left")


def capa_tema_importante(c):
    background(c); selo(c); painel(c)
    V.boxed(c, 1170, 200, 600, 300, AMBER, 1, 0.12)
    for j, s in enumerate(("“O estigma...", "é um tema", "muito importante.”")):
        text(c, s, 1210, 280 + j * 72, 50, "black", INK, align="left")
    V.caixa(c, 1340, 680, 260, 190, 1, open_=1.0, label="x")
    text(c, "caixa VAZIA", 1470, 930, 44, "black", RED)
    big(c, "“É UM TEMA", 340)
    big(c, "IMPORTANTE”", 470)
    boxed(c, "NÃO É TESE", 70, 520, 140, RED)
    text(c, "o erro que trava a redação do ENEM", 90, 860, 48, "extrabold", INK2, align="left")


if __name__ == "__main__":
    for nome, fn in (("capa_A_antes_da_primeira_linha", capa_primeira_linha), ("capa_B_assunto_tema_tese", capa_endereco),
                     ("capa_C_tema_importante_nao_e_tese", capa_tema_importante)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
