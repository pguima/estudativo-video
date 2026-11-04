"""Capas — Redação ENEM, Desenvolvimento, Episódio 5: o parágrafo-modelo comentado e do fraco ao bom (tema claro).
3 variações em 1280x720."""
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
    pill(c, "REDAÇÃO ENEM · DESENVOLVIMENTO · EP. 5", 84, 90, BLUE, size=40, bounds=(0, 1920))


def painel(c):
    card(c, 1120, 120, 700, 840, r=36)


def capa_fraco_bom(c):
    background(c); selo(c); painel(c)
    rows = [("VERSÃO 1", [1, 0, 0, 0, 1], RED), ("VERSÃO 2", [1, 0, 0, 0, 1], RED), ("VERSÃO 3", [1, 1, 1, 1, 1], GREEN)]
    for k, (lab, oks, col) in enumerate(rows):
        y = 250 + k * 250
        text(c, lab, 1200, y - 60, 34, "black", col, align="left", tracking=2)
        for j, key in enumerate(V.KEYS):
            x = 1200 + j * 112
            o = oks[j]
            cc = GREEN if o else RED
            rrect(c, x, y - 20, 100, 100, 18, mix("#FFFFFF", cc, 0.18))
            V.ICON_ETAPA[key](c, x + 50, y + 22, 0.62, 1.0, V.PARTE[key])
            check_icon(c, x + 82, y + 66, 16, 1.0, cc, "check" if o else "x")
    big(c, "O MESMO PARÁGRAFO", 340)
    big(c, "DO FRACO", 480)
    boxed(c, "AO BOM", 70, 530, 150, GREEN)
    text(c, "o desenvolvimento da redação, frase por frase", 90, 860, 42, "extrabold", INK2, align="left")


def capa_5_frases(c):
    background(c); selo(c); painel(c)
    ws = [520, 560, 540, 560, 420]
    for k, key in enumerate(V.KEYS):
        y = 230 + k * 150
        badge_num(c, k + 1, 1200, y + 20, 1, 34, bg=V.PARTE[key])
        rrect(c, 1250, y - 6, ws[k], 52, 26, V.PARTE[key])
        text(c, V.NOMEP[key], 1250, y + 92, 34, "black", V.PARTE[key], align="left")
    big(c, "5 FRASES,", 340)
    big(c, "5 TRABALHOS", 480)
    boxed(c, "PARÁGRAFO-MODELO", 70, 540, 84, BLUE)
    text(c, "o desenvolvimento comentado ao vivo", 90, 860, 46, "extrabold", INK2, align="left")


def capa_citacao(c):
    background(c); selo(c); painel(c)
    V.paper(c, 1170, 200, 600, 560, 1.0, lh=56, top=330)
    V.para(c, "Machado de Assis escreveu O Alienista, obra muito importante da literatura brasileira.", 1270, 340, 40,
           "bold", INK, 1.0, 470, 56)
    V.selo(c, 1470, 650, 1, "SÓ MENCIONOU", RED, -8, 64)
    big(c, "TEM CITAÇÃO", 340)
    big(c, "E AINDA É", 480)
    boxed(c, "FRACO?", 70, 530, 150, RED)
    text(c, "repetir não é explicar; mencionar não é usar", 90, 860, 46, "extrabold", INK2, align="left")


if __name__ == "__main__":
    for nome, fn in (("capa_A_fraco_ao_bom", capa_fraco_bom), ("capa_B_5_frases", capa_5_frases),
                     ("capa_C_citacao_fraca", capa_citacao)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
