"""Capa do Short (1080x1920) — divulgação da série Leitura da Proposta. Mesma cara da capa A do horizontal
(azul-noite, NOTA ZERO com um texto PERFEITO?, folha de redação com carimbo "0 NOTA FINAL"). Serve também de capa do Reels/TikTok:
o texto fica no miolo (y 250–1300), fora da interface do app e do recorte 4:5 da grade."""
import os, subprocess, sys
from pathlib import Path

os.environ["VIDEO_FORMATO"] = "vertical"   # antes do import motor: W, H = 1080, 1920
HERE = Path(__file__).parent
sys.path.insert(0, str(next(d / "_ferramentas" for d in HERE.parents if (d / "_ferramentas").is_dir())))
sys.path.insert(0, str(HERE.parents[1]))
import skia
from divulgacao_visual import *  # noqa
import divulgacao_visual as dv

M = 80   # margem esquerda


def esq(c, s, y, size, col=WHITE, maxw=920, peso="black"):
    size = fit(s, peso, size, maxw)
    glow_text(c, s, M + text_w(s, peso, size) / 2, y, size, peso, col, 1.0, glow=0.10)


def faixa(c, s, y, size, bg, fg):
    w = text_w(s, "black", size) + size * 0.7
    rr = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(M - 12, y - size * 0.98, w, size * 1.22), 22, 22)
    c.drawRRect(rr, blur_paint(bg, 0.45, 28))
    c.drawRRect(rr, paint(bg, 1))
    text(c, s, M - 12 + w / 2, y, size, "black", fg, 1)


def capa_short(c):
    c.drawImage(dv._bg(), 0, 0)
    pill(c, "REDAÇÃO ENEM · LEITURA DA PROPOSTA", W / 2, 260, 36, YEL, NAVY, 1)
    esq(c, "NOTA", 510, 170)
    faixa(c, "ZERO", 780, 235, RED, WHITE)
    esq(c, "com um texto", 960, 112)
    faixa(c, "PERFEITO?", 1160, 140, YEL, NAVY)
    s = "6 aulas do zero · grátis"
    text(c, s, M + text_w(s, "extrabold", 46) / 2, 1290, 46, "extrabold", INK2, 1)
    folha(c, W / 2 + 40, 1640, 400, 540, 1, rot=6, escrito=1.0)
    carimbo(c, "0", "NOTA FINAL", W / 2 + 35, 1660, 210, RED, 1, 1, 0, rot=-0.16)


if __name__ == "__main__":
    surf = skia.Surface(W, H)
    capa_short(surf.getCanvas())
    png = HERE / "capa_short.png"
    surf.makeImageSnapshot().save(str(png), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-q:v", "2", str(HERE / "capa_short.jpg")], check=True)
    png.unlink()
    print("capa_short.jpg")
