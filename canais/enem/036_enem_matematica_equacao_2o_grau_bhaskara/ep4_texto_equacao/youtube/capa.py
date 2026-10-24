"""Capas — Equação do 2º Grau, Episódio 4 (tema claro). 3 variações em 1280x720.
Formatos: A = lixeira gigante à direita com o chip −10 caindo e a pergunta "O −10 VIRA 10?" à esquerda;
B = o jardim com a calçada e as setas "+x" ocupando o centro, "QUANTO MEDE A CALÇADA?" no alto (sem a resposta);
C = fundo azul cheio com a tabela do campeonato numa ficha branca e "66 JOGOS. QUANTOS TIMES?"."""
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

TAG = "MATEMÁTICA ENEM · 2º GRAU · EP. 4"


def fit(s, size, maxw, peso="black"):
    while text_w(s, peso, size) > maxw:
        size -= 4
    return size


def capa_lixeira(c):
    background(c)
    pill(c, TAG, 84, 90, BLUE, size=34, bounds=(0, 1920))
    for k, (s, col) in enumerate((("O −10", RED), ("VIRA 10?", INK))):
        text(c, s, 90, 380 + k * 200, fit(s, 190, 1000), "black", col, align="left")
    text(c, "a raiz que vai para o lixo", 90, 860, 56, "extrabold", GRAY, align="left")
    V.lixeira(c, 1450, 720, 300, 1.0, tampa=0.6)
    c.save(); c.translate(1300, 260); c.rotate(-14)
    V.chip_raiz(c, "−10", 0, 0, RED, 1.0, 120)
    c.restore()
    V.selo(c, 1500, 1000, 1.0, "DESCARTE ≠ TROCAR O SINAL", AMBER, -3, 40)


def capa_jardim(c):
    background(c)
    pill(c, TAG, W / 2, 80, BLUE, size=34, anchor="center", bounds=(0, 1920))
    s = "QUANTO MEDE A CALÇADA?"
    text(c, s, W / 2, 240, fit(s, 140, 1760), "black", INK)
    V.jardim(c, 820, 660, 62, 1.8, 1.0, rot=False, setas=1.0)
    V.fmid(c, "10 m", 820, 530, 56, "black", "#FFFFFF")
    V.fmid(c, "6 m", 560, 660, 56, "black", "#FFFFFF")
    rrect(c, 1450, 520, 400, 220, 30, INK)
    V.fmid(c, "total", 1650, 580, 44, "bold", "#C8CDD3")
    V.fmid(c, "140 m²", 1650, 665, 80, "black", "#FFFFFF")


def capa_campeonato(c):
    rrect(c, 0, 0, W, H, 0, BLUE)
    pill(c, TAG, 84, 90, INK, size=34, bounds=(0, 1920))
    for k, (s, col) in enumerate((("66 JOGOS.", "#FFFFFF"), ("QUANTOS", "#FFFFFF"), ("TIMES?", "#FFD166"))):
        text(c, s, 90, 360 + k * 190, fit(s, 180, 900), "black", col, align="left")
    text(c, "cada jogo foi contado duas vezes", 90, 980, 48, "extrabold", "#DCE6FF", align="left")
    rrect(c, 1060, 200, 760, 700, 40, "#FFFFFF", 1.0, shadow=True)
    V.tabela_camp(c, 0, 1110, 250, 128, 1.0, t_par=-10)


if __name__ == "__main__":
    for nome, fn in (("capa_A_raiz_no_lixo", capa_lixeira), ("capa_B_quanto_mede_calcada", capa_jardim),
                     ("capa_C_quantos_times", capa_campeonato)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
