"""Visual — Estudativo · Short 033 (vertical 1080x1920): ENEM 2025, questão 148, estoque e demanda na livraria (aula: 032).
render.py <proj> --vertical. Paleta e notação do design system de matemática (_ferramentas/matematica.py), com o layout de
Short do 027 (big(), stamp(), contagem() e a legenda de 1 a 3 palavras, importados de lá) e o gráfico da aula 032
(grafico(), comparar()), reposicionado para a tela em pé. Cores: âmbar = autor brasileiro, menta = autor estrangeiro,
ciano = a demanda; check (menta) e cross (coral) nos vereditos."""
import importlib.util
from pathlib import Path

import idioma
import matematica
from matematica import *  # noqa


def _carrega(nome, pasta):
    spec = importlib.util.spec_from_file_location(nome, Path(__file__).resolve().parents[2] / pasta / "roteiro" / "visual.py")
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


sh = _carrega("short027", "027_matematica_short_redes_sociais_probabilidade")
aula = _carrega("aula032", "032_matematica_livraria_estoque_demanda")
big, stamp, contagem, CAPTION = sh.big, sh.stamp, sh.contagem, sh.CAPTION
CX, CAP_Y = sh.CX, sh.CAP_Y
aula.GX0, aula.GX1, aula.GY0, aula.KY = 130, 990, 1300, 3.3   # o gráfico no meio da tela em pé
aula.GC, aula.BW = (275, 485, 695, 905), 72
grafico, comparar = aula.grafico, aula.comparar
TOT, DEM = aula.TOT, aula.DEM

IDIOMAS_NO_CODIGO = True
EN = idioma.LANG == "en"
ARQUIVO_FINAL = "estudativo_short_033_livraria_estoque.mp4"
MARCA = ""

SOM = dict(intro=False, ganho_trilha=0.32, lufs=-14, bpm=118, sfx={
    "01.a": ["pop", "data@+2.2"], "01.b": "data", "01.c": "alert",
    "02.a": ["pop", "pop@+0.8", "pop@+1.6", "pop@+2.3"], "02.b": "notif",
    "02.c": ["alert", "tick@+2.0", "tick@+2.8", "tick2@+3.6"],   # tiques do cronômetro 3-2-1 (02.end − 2,5 s)
    "03.a": "data", "03.b": ["data", "confirm@+4.2"], "03.c": ["data", "deny@+5.4"],
    "04.a": ["impact", "alert@+2.0"], "04.b": ["data", "confirm@+4.8"], "04.c": ["data", "confirm@+2.5"],
    "05.a": "data", "05.b": "confirm", "05.c": ["impact", "shimmer@+0.3"],
    "06.a": "notif", "06.b": "lock"})

T = dict(   # (inglês, português)
    selo=("ENEM 2025 · MATH QUESTION", "ENEM 2025 · QUESTÃO DE MATEMÁTICA"),
    qual=("WHICH BOOK", "QUAL LIVRO"), falta=("IS RUNNING OUT?", "ESTÁ FALTANDO?"),
    leg=("bars = stock · line = demand", "barras = estoque · linha = demanda"),
    qual2=("WHICH GENRE?", "QUAL GÊNERO?"),
    comenta=("comment before you see it ↓", "comenta antes de ver ↓"), pausa=("PAUSE AND THINK", "PAUSE E PENSE"),
    soma=("ADD THE 2 BARS", "SOME AS 2 BARRAS"), armadilha=("TRAP!", "ARMADILHA!"),
    maior=("BIGGEST DEMAND ≠ SHORTAGE", "MAIOR DEMANDA ≠ FALTA"), sobra=("200 ≥ 160: there's extra", "200 ≥ 160: sobra"),
    auto=("SELF-HELP", "AUTOAJUDA"), letra=("ANSWER C", "LETRA C"),
    acertou=("DID YOU GET IT?", "VOCÊ ACERTOU?"), conta=("tell me in the comments ↓", "conta nos comentários ↓"),
    aula=("FULL LESSON", "AULA COMPLETA"), passo=("step by step on the channel", "passo a passo no canal"),
    canal=("ESTUDATIVO ENGLISH", "ESTUDATIVO"),
)
L = {k: (v[0] if EN else v[1]) for k, v in T.items()}
_EXTRA = [] if EN else [("dois mil e vinte e cinco", "2025")]
matematica.NUMEROS_EXTRA[:] = sorted(_EXTRA, key=lambda p: -len(p[0].split()))


def OVERLAY(c, t):
    pill(c, L["selo"], CX, 150, 26, AMB, BG0, 0.95, "extrabold")


def _seq(c, t, a, itens, y=330, size=100):
    """títulos grandes que se sucedem: [(texto, t0, hl, cor)]"""
    for j, (s, t0, hl, hc) in enumerate(itens):
        t1 = itens[j + 1][1] if j + 1 < len(itens) else 1e9
        k = a * ep(t, t0, 0.3) * (1 - ep(t, t1, 0.2))
        if k > 0:
            big(c, s, y, k, WHITE, size, hl=hl, hl_col=hc)


# ---------------------------------------------------------------- cenas
def b_gancho(c, t, C, B):
    ta, tb, tc = (C[f"01.{k}"] for k in "abc")
    a = 1 - prog(t, B["end"] - 0.2, 0.2)
    kq = a * ep(t, ta + 0.2, 0.2)   # a pergunta já no começo
    if kq > 0:
        k = 1 + 0.04 * math.sin(t * 8) * ep(t, tc, 0.2)
        c.save(); c.translate(CX, 340); c.scale(k, k); c.translate(-CX, -340)
        big(c, L["qual"], 290, kq, WHITE, 96)
        big(c, L["falta"], 410, kq, WHITE, 92, hl=L["falta"], hl_col=CYA)
        c.restore()
    grafico(c, a * ep(t, ta + 2.2, 0.3), t, kb=ep(t, ta + 2.2, 0.8), ke=ep(t, ta + 2.6, 0.8), kd=ep(t, tb + 2.0, 1.0))
    label(c, L["leg"], CX, 560, a * ep(t, tb + 0.3, 0.3), 40, AMB, "extrabold")


def b_opcoes(c, t, C, B):
    ta, tb, tc = (C[f"02.{k}"] for k in "abc")
    a = fade(t, B["start"], B["end"], 0.2, 0.15)
    t0 = B["end"] - 2.5   # depois do "Valendo!"
    kp = a * ep(t, t0, 0.2)
    big(c, L["qual2"], 290, a * (1 - kp), WHITE, 104, hl="?", hl_col=CYA)
    label(c, L["comenta"], CX, 400, a * ep(t, tb, 0.3) * (1 - kp), 46, AMB, "extrabold")
    grafico(c, a * (1 - 0.75 * kp), t)
    for i, dt in enumerate((-0.05, 0.75, 1.55, 2.25)):   # cada gênero acende quando é falado
        k = a * ep(t, ta + dt, 0.2) * (1 - ep(t, ta + dt + 0.8, 0.3)) * (1 - kp)
        if k > 0:
            c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(aula.GC[i] - 95, 580, 190, 760), 24, 24), paint(CYA, k, stroke=5))
    if kp > 0:
        label(c, L["pausa"], CX, 290, kp, 84, AMB, "black")
        c.save(); c.translate(CX, 880); c.scale(1.5, 1.5); c.translate(-CX, -880)
        contagem(c, CX, 880, kp, t, t0, 2.4)
        c.restore()


def b_conta(c, t, C, B):
    ta, tb, tc = (C[f"03.{k}"] for k in "abc")
    a = fade(t, B["start"], B["end"], 0.2, 0.2)
    _seq(c, t, a, [(L["soma"], ta + 0.9, "2", CYA), ("80 + 120 = 200", tb + 0.8, "200", CYA),
                   ("50 + 80 = 130", tc + 0.9, "130", CYA), ("130 < 135", tc + 5.4, "<", RED)])
    emp = {0: ep(t, tb + 1.9, 0.6), 1: ep(t, tc + 2.0, 0.6)}
    marca = {0: (True, ep(t, tb + 4.2, 0.3)), 1: (False, ep(t, tc + 5.4, 0.3))}
    foco = 1 if t >= tc else 0 if t >= tb else None
    grafico(c, a, t, emp=emp, marca=marca, foco=foco)
    comparar(c, 0, a * ep(t, tb + 3.3, 0.3) * (1 - ep(t, tc, 0.3)), ep(t, tb + 3.3, 0.6))
    comparar(c, 1, a * ep(t, tc + 3.6, 0.3), ep(t, tc + 3.6, 0.6), RED)


def b_pegadinha(c, t, C, B):
    ta, tb, tc = (C[f"04.{k}"] for k in "abc")
    a = fade(t, B["start"], B["end"], 0.2, 0.2)
    stamp(c, L["armadilha"], CX, 260, RED, a * ep(t, ta + 1.1, 0.2) * (1 - ep(t, ta + 2.0, 0.2)), 76)
    _seq(c, t, a, [(L["maior"], ta + 2.0, None, CYA), ("145 ≥ 140", tb + 2.2, "145", MNT), ("95 ≥ 80", tc + 0.9, "95", MNT)],
         size=90)
    label(c, L["sobra"], CX, 440, a * ep(t, ta + 3.9, 0.3) * (1 - ep(t, tb, 0.2)), 46, MNT, "black")
    emp = {0: 1.0, 1: 1.0, 2: ep(t, tb + 1.3, 0.6), 3: ep(t, tc + 0.9, 0.6)}
    marca = {0: (True, 1.0), 1: (False, 1.0), 2: (True, ep(t, tb + 4.8, 0.3)), 3: (True, ep(t, tc + 2.5, 0.3))}
    foco = 3 if t >= tc else 2 if t >= tb else 0
    grafico(c, a, t, emp=emp, marca=marca, foco=foco)
    for i, t0 in ((2, tb + 3.6), (3, tc + 1.5)):
        comparar(c, i, a * ep(t, t0, 0.3) * (1 - ep(t, tc if i == 2 else 1e9, 0.3)), ep(t, t0, 0.6))


def b_resposta(c, t, C, B):
    ta, tb, tc = (C[f"05.{k}"] for k in "abc")
    a = fade(t, B["start"], B["end"], 0.2, 0.2)
    kc = ep(t, tc, 0.3)
    big(c, L["auto"], 300, a * ep(t, tb + 0.3, 0.3) * (1 - kc), CYA, 110)
    big(c, L["letra"], 300, a * kc, WHITE, 130, hl="C", hl_col=MNT)
    grafico(c, a, t, emp={i: 1.0 for i in range(4)}, marca={0: (True, 1), 1: (False, 1), 2: (True, 1), 3: (True, 1)},
            foco=1 if t >= ta + 1.6 else None)
    comparar(c, 1, a * ep(t, ta + 1.6, 0.3), 1.0, RED)


def b_final(c, t, C, B):
    ta, tb = C["06.a"], C["06.b"]
    a = ep(t, B["start"], 0.2)
    ka = a * (1 - ep(t, tb, 0.25))
    marca = {0: (True, 1), 1: (False, 1), 2: (True, 1), 3: (True, 1)}
    if ka > 0:
        big(c, L["acertou"], 290, ka, WHITE, 104, hl=L["acertou"].split()[-1], hl_col=AMB)
        label(c, L["conta"], CX, 400, ka * ep(t, ta + 0.8, 0.3), 46, AMB, "extrabold")
        grafico(c, ka, t, emp={i: 1.0 for i in range(4)}, marca=marca, foco=1)
    kb = a * ep(t, tb, 0.3)
    if kb > 0:
        cartao(c, 120, 330, 840, 800, kb, CYA, L["aula"])
        c.save(); c.translate(CX, 0); c.scale(0.55, 0.55); c.translate(-CX, 80)
        grafico(c, kb, t, emp={i: 1.0 for i in range(4)}, marca=marca, foco=1)
        c.restore()
        text_mid(c, L["passo"], CX, 950, 46, "extrabold", WHITE, kb)
        glow_text(c, L["canal"], CX, 1060, 96, "black", WHITE, kb * ep(t, tb + 1.0, 0.3), glow=0.14)
        w = text_w(L["canal"], "black", 96)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(CX - w / 2, 1086, w * ep(t, tb + 1.3, 0.6), 12), 6, 6), paint(AMB, kb))


BLOCKS = dict(gancho=b_gancho, opcoes=b_opcoes, conta=b_conta, pegadinha=b_pegadinha, resposta=b_resposta, final=b_final)
