"""Identidade visual do canal Park Anything para configurar o YouTube:
- avatar_800.png      foto do perfil (800x800; o YouTube recorta em círculo): o mascote-cone sobre o amarelo de sinalização
- banner_2560x1440.jpg banner (o centro de 1546x423 aparece em todos os aparelhos; o resto só na TV/desktop largo)
- banner_guia.png     o mesmo banner com as áreas seguras desenhadas (só para conferência, não subir)
- marca_dagua_150.png marca d'água dos vídeos (150x150, fundo transparente)
- logo_horizontal.png logo para outros usos (fundo transparente)
O fundo do banner é o mesmo mundo 3D dos vídeos (canais/park_anything/001_.../roteiro).
Uso: python _marca/gerar.py"""
import math
import sys
from pathlib import Path

import numpy as np
import skia

AQUI = Path(__file__).resolve().parent
EP = AQUI.parent / "001_tractor_trailer_loading_dock"
sys.path[:0] = [str(AQUI.parents[2] / "_ferramentas"), str(EP / "roteiro")]
import mundo3d  # noqa: E402
import manobra as MB  # noqa: E402
import cenario as CN  # noqa: E402
import visual as V  # noqa: E402
from motor import paint, hexc  # noqa: E402

AMARELO, PRETO, LARANJA = CN.AMARELO, "#16181C", CN.LARANJA


def salvar(surf, arq, jpg=False):
    img = surf.makeImageSnapshot()
    img.save(str(AQUI / arq), skia.kJPEG if jpg else skia.kPNG, 92 if jpg else 100)
    print(AQUI / arq)


def logo(c, cx, cy, k=1.0, fundo=True):
    """cone + PARK ANYTHING (duas linhas) + placa amarela com borda de faixas"""
    f1, f2 = V.fnt("display", 150 * k), V.fnt("display", 150 * k)
    w_txt = max(f1.measureText("PARK"), f2.measureText("ANYTHING"))
    w = w_txt + 360 * k
    h = 380 * k
    x, y = cx - w / 2, cy - h / 2
    if fundo:
        r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 34 * k, 34 * k)
        sh = paint("#000000", 0.45)
        sh.setMaskFilter(skia.MaskFilter.MakeBlur(skia.kNormal_BlurStyle, 30 * k))
        c.save(); c.translate(0, 20 * k); c.drawRRect(r, sh); c.restore()
        c.save(); c.clipRRect(r, True)
        V.faixas(c, x, y, w, h, 1.0, passo=34 * k)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x + 24 * k, y + 24 * k, w - 48 * k, h - 48 * k), 18 * k, 18 * k),
                    paint(AMARELO))
        c.restore()
    CN.cone_icone(c, x + 160 * k, cy + 10 * k, 2.6 * k, olhos=True, t=1.0)
    V.txt(c, "PARK", x + 290 * k, cy - 78 * k, 150 * k, "display", PRETO)
    V.txt(c, "ANYTHING", x + 290 * k, cy + 82 * k, 150 * k, "display", LARANJA if not fundo else PRETO)
    return w, h


def avatar():
    s = skia.Surface(800, 800)
    c = s.getCanvas()
    c.clear(skia.ColorTRANSPARENT)
    c.drawCircle(400, 400, 400, paint(AMARELO))
    # anel de faixas de sinalização na borda (fica dentro do círculo do YouTube)
    c.save()
    anel = skia.Path()
    anel.addCircle(400, 400, 398)
    anel.addCircle(400, 400, 340)
    anel.setFillType(skia.PathFillType.kEvenOdd)
    c.clipPath(anel, True)
    for k in range(40):                      # faixas inclinadas que giram com o anel
        a0 = k * 9.0
        w = skia.Path()
        w.moveTo(400, 400)
        w.arcTo(skia.Rect.MakeXYWH(-40, -40, 880, 880), a0, 4.5, False)
        w.close()
        c.save(); c.translate(400, 400); c.skew(0, 0); c.translate(-400, -400)
        c.drawPath(w, paint(PRETO))
        c.restore()
    c.restore()
    c.drawCircle(400, 400, 340, paint(AMARELO))
    sh = paint("#000000", 0.28)
    sh.setMaskFilter(skia.MaskFilter.MakeBlur(skia.kNormal_BlurStyle, 16))
    c.drawOval(skia.Rect.MakeXYWH(240, 560, 320, 54), sh)
    CN.cone_icone(c, 400, 425, 4.0, olhos=True, t=1.0)
    salvar(s, "avatar_800.png")


def marca_dagua():
    s = skia.Surface(150, 150)
    c = s.getCanvas()
    c.clear(skia.ColorTRANSPARENT)
    c.drawCircle(75, 75, 72, paint(AMARELO))
    c.drawCircle(75, 75, 72, paint(PRETO, 1, stroke=6))
    CN.cone_icone(c, 75, 80, 0.86, olhos=True, t=1.0)
    salvar(s, "marca_dagua_150.png")


def logo_horizontal():
    s = skia.Surface(1600, 520)
    c = s.getCanvas()
    c.clear(skia.ColorTRANSPARENT)
    logo(c, 800, 260, 1.0)
    salvar(s, "logo_horizontal.png")


def banner():
    W, H = 2560, 1440
    mundo3d.W, mundo3d.H = W, H
    s = skia.Surface(W, H)
    c = s.getCanvas()
    # céu + mundo: a carreta encostada na doca 4 e um segundo conjunto chegando, com a seta da manobra
    sky = skia.Paint()
    sky.setShader(skia.GradientShader.MakeLinear([skia.Point(0, 0), skia.Point(0, H)], [hexc(CN.CEU_ALTO), hexc(CN.CEU_BAIXO)]))
    c.drawRect(skia.Rect.MakeWH(W, H), sky)
    cam = mundo3d.Camera((-44, -58, 24), (-4, -12, 0), 40)
    cena = mundo3d.Cena(cam)
    CN.montar_mundo(cena, 0.4, alvo_k=1.0)
    CN.conjunto(cena, MB.estado(15.0))

    def chao(cc, cm):
        V.seta_chao(cc, cm, V.caminho_traseira(15.0, MB.comprimento() - 0.3), a=1.0, larg=1.6)
    cena.sobre_chao.append(chao)
    cena.desenhar(c)
    # faixa central escurecida (é o que o celular mostra)
    g = skia.Paint()
    g.setShader(skia.GradientShader.MakeLinear([skia.Point(0, H / 2 - 330), skia.Point(0, H / 2 + 330)],
                                               [hexc("#0B0F17", 0.0), hexc("#0B0F17", 0.55), hexc("#0B0F17", 0.0)], [0, 0.5, 1]))
    c.drawRect(skia.Rect.MakeWH(W, H), g)
    # área segura (todos os aparelhos): 1546 x 423 no centro → x 507..2053
    w, h = logo(c, 0, -1000, 0.6)          # mede
    x0 = W / 2 - 1546 / 2 + 40
    logo(c, x0 + w / 2, H / 2, 0.6)
    tx = x0 + w + 70
    pw = max(V.tw(l, 64, "display") for l in ("IF IT HAS WHEELS,", "A HULL OR WINGS,")) + 80
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(tx - 40, H / 2 - 178, pw, 356), 26, 26), paint("#0B0F17", 0.82))
    for j, (linha, cor) in enumerate((("IF IT HAS WHEELS,", "#FFFFFF"), ("A HULL OR WINGS,", "#FFFFFF"),
                                      ("WE SHOW YOU", AMARELO), ("HOW IT FITS.", AMARELO))):
        V.txt(c, linha, tx, H / 2 - 117 + 78 * j, 64, "display", cor)
    # selo de frequência (fora da faixa do celular: aparece no desktop/TV)
    V.etiqueta(c, "NEW TUTORIAL EVERY WEEK", W / 2, H / 2 + 300, 44, PRETO, AMARELO, 1.0)
    img = s.makeImageSnapshot()
    img.save(str(AQUI / "banner_2560x1440.jpg"), skia.kJPEG, 90)
    print(AQUI / "banner_2560x1440.jpg")
    # guia com as áreas
    g2 = skia.Surface(W, H)
    cg = g2.getCanvas()
    cg.drawImage(img, 0, 0)
    for (ww, hh, cor, nome) in ((1546, 423, "#22C55E", "todos os aparelhos 1546x423"), (2560, 423, "#3B82F6", "desktop 2560x423"),
                                (1855, 423, "#F59E0B", "tablet 1855x423")):
        r = skia.Rect.MakeXYWH(W / 2 - ww / 2, H / 2 - hh / 2, ww, hh)
        cg.drawRect(r, paint(cor, 1, stroke=6))
        V.txt(cg, nome, W / 2 - ww / 2 + 16, H / 2 - hh / 2 - 26, 30, "bold", cor)
    g2.makeImageSnapshot().save(str(AQUI / "banner_guia.png"), skia.kPNG)
    print(AQUI / "banner_guia.png")


if __name__ == "__main__":
    avatar()
    marca_dagua()
    logo_horizontal()
    banner()
