"""Capas — Redação ENEM, Desenvolvimento, Episódio 3: argumento e repertório (tema claro). 3 variações em 1280x720."""
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
    pill(c, "REDAÇÃO ENEM · DESENVOLVIMENTO · EP. 3", 84, 90, V.ARG, size=40, bounds=(0, 1920))


def painel(c):
    card(c, 1120, 120, 700, 840, r=36)


def capa_opiniao(c):
    """A: opinião × argumento — o vendedor do liquidificador"""
    background(c); selo(c); painel(c)
    V.liquidificador(c, 1470, 380, 1.5, 1.0, run=1.0)
    rows = [("“é ótimo!”", "só opinião", RED, "x"), ("“porque tem motor de 1000 W”", "argumento", GREEN, "check")]
    for k, (s, lab, col, kind) in enumerate(rows):
        y = 620 + k * 150
        rrect(c, 1160, y, 620, 130, 18, mix("#FFFFFF", col, 0.12))
        check_icon(c, 1210, y + 65, 26, 1, col, kind)
        text(c, s, 1260, y + 58, 29 if k else 36, "black", INK, align="left")
        text(c, lab, 1260, y + 104, 26, "black", col, align="left")
    big(c, "OPINIÃO NÃO É", 340)
    boxed(c, "ARGUMENTO", 70, 400, 150, V.ARG)
    text(c, "a frase que faz o leitor aceitar a sua ideia", 90, 860, 46, "extrabold", INK2, align="left")


def capa_nota(c):
    """B: a nota fiscal do repertório (nome + conteúdo + fonte certa)"""
    background(c); selo(c); painel(c)
    V.nota_fiscal(c, 1170, 210, 600, 1.0, vals=["O Alienista, de Machado de Assis", "o que acontece na obra",
                                                "autor certo"], status=[True, True, True], size=34, rowmin=150)
    big(c, "SEU REPERTÓRIO", 340)
    big(c, "TEM NOTA FISCAL?", 470)
    boxed(c, "NOME + CONTEÚDO", 70, 530, 100, V.REP)
    text(c, "como apresentar uma referência na redação", 90, 860, 46, "extrabold", INK2, align="left")


def capa_so_nome(c):
    """C: citou só o nome da obra?"""
    background(c); selo(c); painel(c)
    V.nota_fiscal(c, 1170, 210, 600, 1.0, vals=["O Alienista", "", ""], status=[True, False, None], size=34,
                  rowmin=150, lit=[0, 1, 0])
    V.selo(c, 1470, 860, 1, "SEM CONTEÚDO", RED, -6, 56)
    big(c, "CITOU SÓ", 340)
    big(c, "O NOME?", 470)
    boxed(c, "FALTOU O CONTEÚDO", 70, 530, 84, RED)
    text(c, "repertório sem conteúdo não trabalha", 90, 860, 46, "extrabold", INK2, align="left")


if __name__ == "__main__":
    for nome, fn in (("capa_A_opiniao_argumento", capa_opiniao), ("capa_B_nota_fiscal", capa_nota),
                     ("capa_C_so_o_nome", capa_so_nome)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
