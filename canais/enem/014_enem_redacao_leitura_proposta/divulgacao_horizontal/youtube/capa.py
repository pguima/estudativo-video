"""Capas — divulgação horizontal da série Leitura da Proposta (Redação ENEM). Mesmo mundo visual do vídeo
(azul-noite, folha de redação, carimbo vermelho). 2 variações em 1280x720."""
import subprocess, sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(next(d / "_ferramentas" for d in HERE.parents if (d / "_ferramentas").is_dir())))
sys.path.insert(0, str(HERE.parents[1]))
import skia
from divulgacao_visual import *  # noqa
import divulgacao_visual as dv


def esq(c, s, y, size, col=WHITE, maxw=1000, peso="black"):
    size = fit(s, peso, size, maxw)
    glow_text(c, s, 90 + text_w(s, peso, size) / 2, y, size, peso, col, 1.0, glow=0.10)


def faixa(c, s, x, y, size, bg, fg):
    w = text_w(s, "black", size) + size * 0.7
    h = size * 1.22
    rr = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y - size * 0.98, w, h), 18, 18)
    c.drawRRect(rr, blur_paint(bg, 0.45, 24))
    c.drawRRect(rr, paint(bg, 1))
    text(c, s, x + w / 2, y, size, "black", fg, 1)


def selo(c):
    pill(c, "REDAÇÃO ENEM · SÉRIE LEITURA DA PROPOSTA", 90 + text_w("REDAÇÃO ENEM · SÉRIE LEITURA DA PROPOSTA", "black", 34) * 0.5 + 20,
         110, 34, YEL, NAVY, 1)


def capa_zero(c):
    c.drawImage(dv._bg(), 0, 0)
    selo(c)
    folha(c, 1440, 560, 560, 760, 1, rot=6, escrito=1.0)
    carimbo(c, "0", "NOTA FINAL", 1430, 600, 300, RED, 1, 1, 0, rot=-0.16)
    esq(c, "NOTA", 285, 150)
    faixa(c, "ZERO", 80, 565, 230, RED, WHITE)
    esq(c, "com um texto", 740, 110)
    faixa(c, "PERFEITO?", 80, 900, 140, YEL, NAVY)


def capa_6aulas(c):
    c.drawImage(dv._bg(), 0, 0)
    selo(c)
    w, h = 400, 225
    for i in range(6):
        x = 1010 + (i % 2) * (w + 30)
        y = 210 + (i // 2) * (h + 36)
        cover(c, i, x, y, w, h, 1, r=16)
        c.drawCircle(x + w - 4, y + h - 4, 30, paint(YEL, 1))
        text_mid(c, str(i + 1), x + w - 4, y + h - 4, 36, "black", NAVY, 1)
    esq(c, "O ERRO QUE", 330, 120, maxw=860)
    esq(c, "ZERA A REDAÇÃO", 480, 120, col=RED, maxw=860)
    esq(c, "nasce antes da", 640, 84, maxw=860)
    faixa(c, "1ª LINHA", 80, 840, 150, YEL, NAVY)
    text(c, "6 aulas do zero · grátis", 90 + text_w("6 aulas do zero · grátis", "extrabold", 44) / 2, 960, 44, "extrabold", INK2, 1)


if __name__ == "__main__":
    for nome, fn in (("capa_A_nota_zero", capa_zero), ("capa_B_6_aulas", capa_6aulas)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
