"""Miniaturas do Park Anything 002 (1280x720, três versões para o teste A/B): a limusine em 20° entrando na vaga entre o
sedã vermelho e o verde, a seta laranja do caminho da traseira, a placa amarela e preta e o mascote-cone.
Uso: python youtube/capa.py"""
import sys
from pathlib import Path

import numpy as np
import skia

PROJ = Path(__file__).resolve().parents[1]
sys.path[:0] = [str(PROJ.parents[2] / "_ferramentas"), str(PROJ / "roteiro")]
import visual as V  # noqa: E402
import baliza as BZ  # noqa: E402
import rua  # noqa: E402
from mundo3d import Camera, Cena  # noqa: E402
from motor import paint, hexc  # noqa: E402

B1 = V.B1
VERSOES = {
    "A_is_this_even_possible": dict(rot=("IS THIS EVEN", "POSSIBLE?"), cor2=V.VERMELHO),
    "B_40_feet": dict(rot=("IT NEEDS", "40 FEET?!"), cor2=V.VERMELHO),
    "C_20_not_45": dict(rot=("LIMO TRICK:", "20°, NOT 45°"), cor2=V.AMARELO),
}


def mundo(c):
    rl, _ = BZ.limo()
    sv = BZ.marco(rl, "B") + 1.5
    p = BZ.pose(rl, sv)
    xm = BZ.XB - BZ.VAGA / 2
    cam = Camera((xm + 12, 17.3, 15.5), (xm - 0.5, 1.0, 0.0), 42)
    B1._ceu(c)
    cena = Cena(cam)
    rua.montar_rua(cena, 0.4, vaga_k=1.0)
    rua.estacionados(cena)
    rua.limusine(cena, p["x"], p["y"], p["th"], 0.0)

    def chao(cc, cm):
        pts = [((a[0] + b[0]) / 2, (a[1] + b[1]) / 2) for a, b in
               ((V._canto(rl, v, 0), V._canto(rl, v, 1)) for v in np.linspace(sv, rl[-1][5] - 2.0, 40))]
        V.seta_chao(cc, cm, pts, a=1.0, larg=1.0)
    cena.sobre_chao.append(chao)
    cena.desenhar(c)


def main():
    for nome, cfg in VERSOES.items():
        surf = skia.Surface(1920, 1080)
        c = surf.getCanvas()
        mundo(c)
        v = skia.Paint()
        v.setShader(skia.GradientShader.MakeRadial(skia.Point(1100, 640), 1300, [hexc("#000000", 0.0), hexc("#0B1020", 0.42)],
                                                   [0.5, 1.0]))
        c.drawRect(skia.Rect.MakeWH(1920, 1080), v)
        import importlib.util
        spec = importlib.util.spec_from_file_location("capa001", PROJ.parent / "001_tractor_trailer_loading_dock" / "youtube" / "capa.py")
        m = importlib.util.module_from_spec(spec)
        sys.modules.setdefault("visual", V)
        spec.loader.exec_module(m)
        m.rotulo(c, *cfg["rot"], cfg["cor2"])
        B1.CN.cone_icone(c, 1790, 930, 1.9, olhos=True, t=1.0)
        img = surf.makeImageSnapshot()
        small = skia.Surface(1280, 720)
        small.getCanvas().drawImageRect(img, skia.Rect.MakeWH(1280, 720),
                                        skia.SamplingOptions(skia.FilterMode.kLinear, skia.MipmapMode.kLinear))
        arq = PROJ / "youtube" / f"capa_{nome}.jpg"
        small.makeImageSnapshot().save(str(arq), skia.kJPEG, 92)
        print(arq)


if __name__ == "__main__":
    main()
