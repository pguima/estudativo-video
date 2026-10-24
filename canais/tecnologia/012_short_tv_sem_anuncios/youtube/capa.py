"""Capas verticais (1080x1920) do Short 012. Textos em inglês (Tecnativo English); a versão em português troca os
textos por roteiro/textos.py. Gerar as duas:
    VIDEO_FORMATO=vertical python _ferramentas/idioma.py capa <proj> --lang en   -> youtube_en/
    VIDEO_FORMATO=vertical python _ferramentas/idioma.py capa <proj> --lang pt   -> youtube/
Tudo importante fica no meio (y 380–1500): o feed do Shorts às vezes corta a capa em 4:5."""
from pathlib import Path
import skia
import visual
from visual import *  # noqa

OUT = Path(__file__).resolve().parent


def fundo(c, red=0.0):
    visual.BACKGROUND(c, 3.0)
    if red:
        c.drawCircle(CX, 760, 700, blur_paint(AD, 0.16 * red, 170))


def palavra_caixa(c, s, cy, size, bg, fg="#0B0F1A", rot=-3):
    """palavra-chave numa caixa colorida, levemente inclinada"""
    while text_w(s, "black", size) > 900:
        size -= 4
    w = text_w(s, "black", size) + size * 0.7
    h = size * 1.25
    c.save(); c.translate(CX, cy); c.rotate(rot)
    r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(-w / 2, -h / 2, w, h), 18, 18)
    c.drawRRect(r, blur_paint(bg, 0.55, 26))
    c.drawRRect(r, paint(bg, 1.0))
    text_mid(c, s, 0, 0, size, "black", fg, 1.0)
    c.restore()


def linha(c, s, cy, size, col=INK, glow=0.25):
    while text_w(s, "black", size) > 980:
        size -= 4
    sh = skia.Paint(AntiAlias=True, Style=skia.Paint.kStroke_Style, StrokeWidth=size * 0.14, Color=skia.ColorBLACK)
    sh.setStrokeJoin(skia.Paint.kRound_Join)
    f = motor.font("black", size)
    w = f.measureText(s)
    c.drawString(s, CX - w / 2, cy + size * 0.36, f, sh)
    glow_text(c, s, CX, cy + size * 0.36, size, "black", col, 1.0, glow=glow)


def capa_a(c):
    """A: antes (com anúncio) em cima, depois embaixo, frase no meio"""
    fundo(c, 0.6)
    chip(c, "TECNATIVO", CX, 150, CYAN, 1.0, anchor="center", size=26, filled=True)
    x, y, w, h = tv(c, 100, 290, 880, ANTES, glow=AD, stand=False)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x + 22, y + 22, w * 0.64, h * 0.38), 12, 12), paint(AD, 1.0, stroke=8))
    stamp(c, "AD", x + w * 0.64 + 10, y + 26, AD, 1.0, 60)
    tv(c, 100, 1180, 880, DEPOIS, glow=LIME, stand=False)
    text(c, "BEFORE", 110, 262, 40, "black", AD, 1.0, align="left")
    text(c, "AFTER", 110, 1152, 40, "black", LIME, 1.0, align="left")
    linha(c, "AI KILLED", 885, 110)
    palavra_caixa(c, "THE ADS", 1010, 116, YEL)
    text(c, "Images: @gathint · cleanyour.tv", CX, 1740, 26, "medium", INK2, 0.8)


def capa_b(c):
    """B: TV com o anúncio em close + frase grande + '25 apps off'"""
    fundo(c, 1.0)
    chip(c, "TECNATIVO", CX, 150, CYAN, 1.0, anchor="center", size=26, filled=True)
    linha(c, "HE LET AN AI", 420, 112)
    palavra_caixa(c, "HACK HIS TV", 560, 116, CLAUDE, rot=-2)
    x, y, w, h = tv(c, 60, 760, 960, ANTES, zoom=1.45, fx=0.05, fy=0.15, glow=AD)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x + 20, y + 20, w * 0.88, h * 0.62), 14, 14), paint(AD, 1.0, stroke=9))
    stamp(c, "AD", x + w * 0.86, y + 24, AD, 1.0, 64)
    stamp(c, "25 APPS OFF", CX, 1440, AD, 1.0, 76, rot=-4)
    text(c, "Images: @gathint · cleanyour.tv", CX, 1700, 26, "medium", INK2, 0.8)


def salvar(fn, nome):
    s = skia.Surface(W, H)
    fn(s.getCanvas())
    s.makeImageSnapshot().save(str(OUT / nome), skia.kJPEG, 92)
    print(OUT / nome)


if __name__ == "__main__":
    salvar(capa_a, "capa_short_A_antes_depois.jpg")
    salvar(capa_b, "capa_short_B_ia_invadiu.jpg")
