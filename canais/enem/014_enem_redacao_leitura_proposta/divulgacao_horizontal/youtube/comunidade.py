"""Imagem do post da Comunidade do YouTube — divulgação da série Leitura da Proposta. Quadrada (1080x1080), mesma
cara da capa A (azul-noite, folha de redação, carimbo "0 NOTA FINAL")."""
import subprocess, sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(next(d / "_ferramentas" for d in HERE.parents if (d / "_ferramentas").is_dir())))
sys.path.insert(0, str(HERE.parents[1]))
import skia
from divulgacao_visual import *  # noqa
import divulgacao_visual as dv

S = 1080
M = 70   # margem esquerda


def esq(c, s, y, size, col=WHITE, maxw=900, peso="black"):
    size = fit(s, peso, size, maxw)
    glow_text(c, s, M + text_w(s, peso, size) / 2, y, size, peso, col, 1.0, glow=0.10)


def faixa(c, s, y, size, bg, fg):
    w = text_w(s, "black", size) + size * 0.7
    rr = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(M - 10, y - size * 0.98, w, size * 1.22), 18, 18)
    c.drawRRect(rr, blur_paint(bg, 0.45, 24))
    c.drawRRect(rr, paint(bg, 1))
    text(c, s, M - 10 + w / 2, y, size, "black", fg, 1)


def post(c):
    bg = dv._bg()   # 1920x1080: recorta o centro-direita (onde fica o brilho azul)
    c.drawImageRect(bg, skia.Rect.MakeXYWH(700, 0, 1080, 1080), skia.Rect.MakeWH(S, S), SAMP)
    selo = "REDAÇÃO ENEM · SÉRIE LEITURA DA PROPOSTA"
    pill(c, selo, S / 2, 95, 30, YEL, NAVY, 1)
    esq(c, "NOTA", 290, 130)
    faixa(c, "ZERO", 495, 190, RED, WHITE)
    esq(c, "com um texto", 640, 80, maxw=520)
    faixa(c, "PERFEITO?", 800, 100, YEL, NAVY)
    folha(c, 890, 770, 330, 460, 1, rot=7, escrito=1.0)   # por cima do texto: o carimbo fica inteiro
    carimbo(c, "0", "NOTA FINAL", 885, 790, 180, RED, 1, 1, 0, rot=-0.16)
    text(c, "6 aulas do zero · grátis no canal", M + text_w("6 aulas do zero · grátis no canal", "extrabold", 40) / 2,
         985, 40, "extrabold", INK2, 1)


if __name__ == "__main__":
    surf = skia.Surface(S, S)
    post(surf.getCanvas())
    png = HERE / "comunidade_post.png"
    surf.makeImageSnapshot().save(str(png), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-q:v", "2", str(HERE / "comunidade_post.jpg")], check=True)
    png.unlink()
    print("comunidade_post.jpg")
