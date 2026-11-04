"""Miniaturas do Park Anything 001 (1280x720, três versões para o teste A/B do YouTube), desenhadas com o mesmo mundo
3D do vídeo: o conjunto no meio da manobra (engate perto de 45°), a doca 4 destacada com cones, a seta laranja grossa da
traseira até a porta, a etiqueta amarela e preta (2 a 4 palavras, sem repetir o título) e o mascote-cone no canto.
Uso: python youtube/capa.py"""
import math
import sys
from pathlib import Path

import numpy as np
import skia

PROJ = Path(__file__).resolve().parents[1]
sys.path[:0] = [str(PROJ.parents[2] / "_ferramentas"), str(PROJ / "roteiro")]
import manobra as MB  # noqa: E402
import cenario as CN  # noqa: E402
import visual as V  # noqa: E402
from mundo3d import Camera, Cena  # noqa: E402
from motor import paint, hexc  # noqa: E402

VERSOES = {
    "A_stop_jackknifing": dict(rot=("STOP", "JACKKNIFING"), cor2=V.VERMELHO),
    "B_the_45_rule": dict(rot=("THE 45°", "RULE"), cor2=V.AMARELO),
    "C_easy_dock_trick": dict(rot=("EASY", "DOCK TRICK"), cor2=V.AMARELO),
}


def cone3d(c, cam, x, y, k=1.0):
    q = V.ponto_tela(cam, (x, y, 0.0))
    if q is None:
        return
    d = np.linalg.norm(cam.e - np.array([x, y, 0]))
    CN.cone_icone(c, q[0], q[1] - 40 * k * 26 / d, k * 26 / d)


def mundo(c, s=6.5):
    p = MB.estado(s)
    p["dshow"] = math.radians(18)
    tx, ty = CN.traseira_carreta(p)
    cam = Camera((33, -55, 18.5), (5.5, -18.5, 0.0), 40)
    V._ceu(c)
    cena = Cena(cam)
    CN.montar_mundo(cena, 0.4, alvo_k=1.0)
    CN.conjunto(cena, p)

    def chao(cc, cm):
        V.seta_chao(cc, cm, V.caminho_traseira(s, MB.comprimento() - 0.3), a=1.0, larg=2.3)
    cena.sobre_chao.append(chao)
    cena.desenhar(c)
    for x in (-1.75, 1.75):
        cone3d(c, cam, x, -1.0, 1.5)
    return cam


def rotulo(c, l1, l2, cor2):
    """etiqueta grande: linha 1 preta no amarelo, linha 2 com faixas de sinalização na borda"""
    x, y = 60, 52
    f1, f2 = V.fnt("display", 112), V.fnt("display", 124)
    w = max(f1.measureText(l1), f2.measureText(l2)) + 90
    h = 300
    sh = paint("#000000", 0.5)
    sh.setMaskFilter(skia.MaskFilter.MakeBlur(skia.kNormal_BlurStyle, 22))
    r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 22, 22)
    c.save(); c.translate(0, 14); c.drawRRect(r, sh); c.restore()
    c.save(); c.clipRRect(r, True)
    V.faixas(c, x, y, w, h, 1.0, passo=26)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x + 18, y + 18, w - 36, h - 36), 12, 12), paint(V.AMARELO))
    c.restore()
    V.txt(c, l1, x + 45, y + 95, 112, "display", V.PRETO)
    if cor2 == V.VERMELHO:
        bw = f2.measureText(l2) + 30
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x + 30, y + 150, bw, 126), 12, 12), paint(V.VERMELHO))
        V.txt(c, l2, x + 45, y + 213, 124, "display", "#FFFFFF")
    else:
        V.txt(c, l2, x + 45, y + 213, 124, "display", V.PRETO)


def main():
    out = PROJ / "youtube"
    for nome, cfg in VERSOES.items():
        surf = skia.Surface(1920, 1080)
        c = surf.getCanvas()
        mundo(c)
        # leve vinheta para destacar o centro
        v = skia.Paint()
        v.setShader(skia.GradientShader.MakeRadial(skia.Point(1100, 640), 1300, [hexc("#000000", 0.0), hexc("#0B1020", 0.42)],
                                                   [0.5, 1.0]))
        c.drawRect(skia.Rect.MakeWH(1920, 1080), v)
        rotulo(c, *cfg["rot"], cfg["cor2"])
        CN.cone_icone(c, 1790, 930, 1.9, olhos=True, t=1.0)
        img = surf.makeImageSnapshot()
        small = skia.Surface(1280, 720)
        small.getCanvas().drawImageRect(img, skia.Rect.MakeWH(1280, 720),
                                        skia.SamplingOptions(skia.FilterMode.kLinear, skia.MipmapMode.kLinear))
        arq = out / f"capa_{nome}.jpg"
        small.makeImageSnapshot().save(str(arq), skia.kJPEG, 92)
        print(arq)


if __name__ == "__main__":
    main()
