"""Miniaturas do vídeo 02 (3 versões para o "Testar e comparar"), no mesmo molde das do 001 (visual/youtube.py).
python miniaturas.py → saida/youtube/*.jpg"""
import math
import skia
import visual as V
from visual import *  # noqa: F403

OUT = V.lingua.saida(V.AQUI) / "youtube"


def texto_capa(c, s, x, y, size, cor="#ffffff", contorno="#070c38"):
    """texto de miniatura: Rubik Black com contorno grosso (igual ao 001)"""
    size = min(size, size * 1780 / font("thumb", size, 900).measureText(s))
    f = font("thumb", size, 900)
    w = f.measureText(s)
    p = skia.Paint(AntiAlias=True, Color=hexc(contorno), Style=skia.Paint.kStroke_Style, StrokeWidth=size * 0.16,
                   StrokeJoin=skia.Paint.kRound_Join)
    c.drawString(s, x - w / 2, y, f, p)
    c.drawString(s, x - w / 2, y, f, paint(cor))


def palco(c, cor_fundo="#2540a8"):
    c.drawRect(skia.Rect.MakeWH(W, H), radial(W / 2, 520, 1100, [cor_fundo, "#14206b", "#0a1240"], [0, 0.6, 1]))
    for k, cor in enumerate((PINK, SKY, AMBER, CYAN)):
        x = [140, 420, 1500, 1780][k]
        c.drawRRect(rr(x - 90, 260, 180, 700, 90), paint(mix(cor, "#1d2f8f", 0.5), 0.55))
    holofote(c, W / 2, 0, 1000, 160, 820, 1.2)
    poeira(c, 3.0, (W / 2 - 380, 40, W / 2 + 380, 980), 60, seed=4, a=0.6)
    pedestal(c, W / 2, 960, 900, 200, None, 1.0)
    placa = "PEÇA Nº 002 · c. 2026 d.C."
    pw = max(540, text_w(placa, 30, "mono", 500) * 1.06 + 70)
    c.drawRRect(rr(W / 2 - pw / 2, 1000, pw, 60, 4), paint("#ffe9c2"))
    text(c, placa, W / 2, 1040, 30, "mono", 500, "#3a2c18", 1, "center", tracking=0.06)


def miniatura(nome, frase, peca, cor_frase="#ffffff"):
    surf = skia.Surface(W, H)
    c = surf.getCanvas()
    palco(c)
    c.drawOval(oval(W / 2, 955, 420, 30), paint(V.AZUL_TELA, 0.35, blur=14))
    peca(c)
    vitrine_vidro(c, W / 2, 955, 860, 560, 1.0)
    lume(c, 300, 1050, 2.4, pose(look=(1.0, -0.4), brow=0.9, brow_y=0.7, o_mouth=True, mouth=0.6))
    texto_capa(c, frase, W / 2, 250, 210 if len(frase) < 12 else 170, cor_frase)
    img = surf.makeImageSnapshot()
    s2 = skia.Surface(1280, 720)
    s2.getCanvas().drawImageRect(img, skia.Rect.MakeWH(1280, 720), skia.SamplingOptions(skia.CubicResampler.Mitchell()))
    s2.makeImageSnapshot().save(str(OUT / f"{nome}.jpg"), skia.kJPEG, 92)
    print("ok", nome)


def peca_aceso(c):
    """celular aceso com o selinho vermelho de notificação"""
    celular_aceso(c, W / 2, 700, 2.1, 0.0, 1.0, badge=1.0)


def peca_feed(c):
    celular_aceso(c, W / 2, 700, 2.1, 0.6, 1.0, feed=1.0)


def peca_maquina(c):
    c.save()
    c.translate(W / 2, 700)
    c.scale(0.95, 0.95)
    caca_niquel(c, 0, 0, 0.37)
    c.restore()


if __name__ == "__main__":
    OUT.mkdir(exist_ok=True)
    miniatura("miniatura_A_eram_o_alvo", "ERAM O ALVO", peca_aceso, AMBER)
    miniatura("miniatura_B_6h38_por_dia", "6 H 38 POR DIA", peca_feed)
    miniatura("miniatura_C_caca_niquel", "UM CAÇA-NÍQUEL?", peca_maquina)
