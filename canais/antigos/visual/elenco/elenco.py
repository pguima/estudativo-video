"""Catálogo do elenco do canal (personagens e objetos reutilizáveis): python elenco.py → elenco_*.png
Peças em _ferramentas/antigos_elenco.py; a Lume em _ferramentas/antigos.py."""
import sys
from pathlib import Path
import skia
AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parents[3] / "_ferramentas"))
from antigos import *  # noqa: E402,F403
from antigos_elenco import *  # noqa: E402,F403


def folha(nome, fn, w=1920, h=1080, cima="#1f3196", baixo="#14206b"):
    surf = skia.Surface(w, h)
    c = surf.getCanvas()
    c.drawRect(skia.Rect.MakeWH(w, h), linear(0, 0, 0, h, [cima, baixo]))
    fn(c)
    surf.makeImageSnapshot().save(str(AQUI / f"elenco_{nome}.png"), skia.kPNG)


def legenda(c, s, x, y):
    text(c, s, x, y, 22, "mono", 500, DUST, 1, "center")


def antigos_(c):
    lume(c, 150, 470, 1.15, lume_viva(0.5, dict(look=(0.8, 0.0), arm_r=0.5)))
    legenda(c, "LUME (REFERÊNCIA)", 150, 520)
    cores = [CORAL, SKY, AMBER, CYAN, PINK, "#2e47c9", "#7be36b"]
    for i, est in enumerate(ESTILOS):
        x = 370 + i * 225
        antigo(c, x, 470, 1.25, antigo_vivo(0.3, i, roupa=cores[i], pele=PELE[i % 5], cabelo=CABELOS[i % 6], estilo=est))
        legenda(c, est.upper(), x, 520)
    for i, ex in enumerate(EXPRESSOES):
        x = 160 + i * 265
        cel = "d" if ex == "hipnotizado" else None
        p = antigo_pose(roupa=cores[i], pele=PELE[(i + 2) % 5], cabelo=CABELOS[(i + 1) % 4], estilo=ESTILOS[i % 6],
                        celular=cel, braco_d=1.25 if cel else 0.1, **expressao(ex))
        antigo(c, x, 990, 1.55, p)
        legenda(c, ex.upper(), x, 1040)


def maos_(c):
    mao(c, 330, 900, 1.4, "aponta", manga=SKY)
    legenda(c, "APONTA", 330, 1050)
    celular_aceso(c, 960, 470, 2.2, 1.0, 1.0, feed=1.0)
    mao(c, 1000, 1080, 1.7, "toque", ang=-8, manga=CORAL, aperta=1.0)
    legenda(c, "TOQUE NA TELA", 960, 1050)
    mao(c, 1600, 900, 1.3, "aberta", ang=10, manga=AMBER, pele=PELE[2])
    legenda(c, "ABERTA", 1600, 1050)


def bichos_(c):
    rato(c, 300, 520, 2.0, 1.0)
    legenda(c, "RATO", 300, 600)
    rato(c, 300, 960, 2.0, 1.0, dorme=1.0)
    legenda(c, "RATO DORMINDO", 300, 1040)
    rato(c, 820, 960, 2.0, 1.0, aperta=1.0)
    legenda(c, "RATO APERTANDO", 820, 1040)
    cerebro(c, 1380, 380, 1.6)
    legenda(c, "CÉREBRO", 1380, 600)
    cerebro(c, 1380, 830, 1.2, flash=1.0)
    legenda(c, "CÉREBRO + DOPAMINA", 1380, 1040)
    celular_aceso(c, 820, 330, 1.3, 1.0, 1.0, badge=1.0)
    legenda(c, "CELULAR (PEÇA 002)", 820, 600)


def objetos_(c):
    mesa(c, 120, 620, 300, 520)
    celular_aceso(c, 370, 282, 0.3, 0, 0.0, ang=90)
    legenda(c, "MESA", 370, 580)
    caixa_madeira(c, 760, 330, 300, 170, tampa_h=26)
    legenda(c, "CAIXA / GAVETA", 910, 580)
    caca_niquel(c, 1500, 330, 1.3)
    legenda(c, "CAÇA-NÍQUEL", 1500, 640)
    olho(c, 160, 820, 2.0, look=0.4)
    legenda(c, "OLHO", 160, 1000)
    sino(c, 420, 820, 1.6)
    sino(c, 640, 820, 1.6, "#8a93c8", riscado=True)
    legenda(c, "SINO / SILENCIADO", 530, 1000)
    coracao(c, 880, 820, 70)
    legenda(c, "CORAÇÃO", 880, 1000)
    moeda(c, 1060, 820, 2.0)
    legenda(c, "MOEDA", 1060, 1000)
    ampulheta(c, 1260, 830, 0.7, 0.6)
    legenda(c, "AMPULHETA", 1260, 1000)
    for k in range(4):
        simbolo(c, k + 1, 1460 + k * 110, 820, 90, FESTA[k])
    legenda(c, "SÍMBOLOS", 1620, 1000)


if __name__ == "__main__":
    folha("objetos", objetos_, cima="#ffb3c8", baixo="#ffd99a")
    folha("antigos", antigos_)
    folha("maos", maos_, cima="#7ec8ff", baixo="#d6f0ff")
    folha("bichos", bichos_)
    print("ok")
