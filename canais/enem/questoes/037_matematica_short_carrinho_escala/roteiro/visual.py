"""Visual — Estudativo · Short 037 (vertical 1080x1920): ENEM 2025, questão 150, o carrinho de controle remoto (aula: 036).
render.py <proj> --vertical. Paleta e notação do design system de matemática (_ferramentas/matematica.py), com o layout de
Short do 027 (big(), stamp(), contagem() e a legenda de 1 a 3 palavras, importados de lá) e as telas do controle da aula
036 (tela()), em grade 3 + 2 na tela em pé. Cores: âmbar = escala, ciano = o deslocamento, menta = a resposta (tela III),
coral = a armadilha (maior desenho e maior escala)."""
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
aula = _carrega("aula036", "036_matematica_carrinho_escala")
big, stamp, contagem, CAPTION = sh.big, sh.stamp, sh.contagem, sh.CAPTION
CX, CAP_Y = sh.CX, sh.CAP_Y
tela, ROMANO, REAL = aula.tela, aula.ROMANO, aula.REAL

IDIOMAS_NO_CODIGO = True
EN = idioma.LANG == "en"
ARQUIVO_FINAL = "estudativo_short_037_carrinho_escala.mp4"
MARCA = ""

SOM = dict(intro=False, ganho_trilha=0.32, lufs=-14, bpm=118, sfx={
    "01.a": ["pop", "pop@+2.6", "pop@+2.8", "pop@+3.0", "pop@+3.2", "pop@+3.4"], "01.b": "data", "01.c": "alert",
    "02.a": "data", "02.b": "notif",
    "02.c": ["alert", "tick@+2.5", "tick@+3.3", "tick2@+4.1"],   # tiques do cronômetro 3-2-1 (02.end − 2,5 s)
    "03.a": "data", "03.b": "confirm", "03.c": "confirm", "03.d": "confirm",
    "04.a": ["impact", "deny@+2.2"], "04.b": "deny", "04.c": "lock",
    "05.a": "confirm", "05.b": ["impact", "shimmer@+0.3"],
    "06.a": "notif", "06.b": "lock"})

T = dict(   # (inglês, português)
    selo=("ENEM 2025 · MATH QUESTION", "ENEM 2025 · QUESTÃO DE MATEMÁTICA"),
    q1=("WHICH TRIP", "QUAL CARRINHO"), q1b=("WAS LONGEST?", "ANDOU MAIS?"),
    q2=("I OR V?", "I OU V?"),
    comenta=("comment before you see it ↓", "comenta antes de ver ↓"), pausa=("PAUSE AND THINK", "PAUSE E PENSE"),
    esc=("1 cm → 100 cm", "1 cm → 100 cm"), mult=("DRAWING × SCALE", "DESENHO × ESCALA"),
    armadilha=("TRAP!", "ARMADILHA!"), d1=("BIGGEST DRAWING = 9 m", "MAIOR DESENHO = 9 m"),
    d2=("BIGGEST SCALE = 20 m", "MAIOR ESCALA = 20 m"),
    r30=("30 METERS", "30 METROS"), so5=("drawing: only 5 cm", "desenho: só 5 cm"), letra=("ANSWER C", "LETRA C"),
    acertou=("DID YOU GET IT?", "VOCÊ ACERTOU?"), conta=("tell me in the comments ↓", "conta nos comentários ↓"),
    aula=("FULL LESSON", "AULA COMPLETA"), passo=("step by step on the channel", "passo a passo no canal"),
    canal=("ESTUDATIVO ENGLISH", "ESTUDATIVO"),
)
L = {k: (v[0] if EN else v[1]) for k, v in T.items()}
_EXTRA = [] if EN else [("dois mil e vinte e cinco", "2025"), ("um para cem", "1 : 100"), ("mil", "1000")]
matematica.NUMEROS_EXTRA[:] = sorted(_EXTRA, key=lambda p: -len(p[0].split()))

TW = 320                                                    # largura de cada tela na grade
POS = ((40, 560), (380, 560), (720, 560), (210, 900), (550, 900))   # 3 em cima, 2 embaixo


def OVERLAY(c, t):
    pill(c, L["selo"], CX, 150, 26, AMB, BG0, 0.95, "extrabold")


def telas(c, a, t, ks=(1,) * 5, foco=None, res=(0,) * 5, cores=None, dy=0):
    """as cinco telas; res = quanto o resultado em metros já apareceu embaixo de cada uma"""
    for i, (x, y) in enumerate(POS):
        tela(c, i, x, y + dy, TW, a * ep(ks[i], 0, 0.3), k=ks[i], foco=foco, num=False)
        al = a * ep(ks[i], 0, 0.3) * (1 - 0.6 * (foco is not None and foco != i))
        yl = y + dy + TW * 0.752 + 34
        kr = res[i]
        if kr > 0:
            cor = (cores or (CYA,) * 5)[i]
            pill(c, f"{ROMANO[i]} · {REAL[i] // 100} m", x + TW / 2, yl, 32, cor, BG0, al * ep(kr, 0, 0.3))
        else:
            text_mid(c, ROMANO[i], x + TW / 2, yl, 32, "black", WHITE, al)


def _seq(c, t, a, itens, y=330, size=100):
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
        big(c, L["q1"], 290, kq, WHITE, 96)
        big(c, L["q1b"], 410, kq, WHITE, 100, hl=L["q1b"], hl_col=MNT)
    ks = tuple(ep(t, ta + 2.6 + 0.2 * i, 0.6) for i in range(5))
    telas(c, a, t, ks=ks)


def b_opcoes(c, t, C, B):
    ta, tb, tc = (C[f"02.{k}"] for k in "abc")
    a = fade(t, B["start"], B["end"], 0.2, 0.15)
    t0 = B["end"] - 2.5   # depois do "Valendo!"
    kp = a * ep(t, t0, 0.2)
    foco = 0 if t < ta + 1.8 else (4 if t < tb else None)
    big(c, L["q2"], 290, a * (1 - kp), WHITE, 110, hl="?", hl_col=MNT)
    label(c, L["comenta"], CX, 400, a * ep(t, tb, 0.3) * (1 - kp), 46, AMB, "extrabold")
    telas(c, a * (1 - 0.75 * kp), t, foco=foco)
    if kp > 0:
        label(c, L["pausa"], CX, 290, kp, 84, AMB, "black")
        c.save(); c.translate(CX, 880); c.scale(1.5, 1.5); c.translate(-CX, -880)
        contagem(c, CX, 880, kp, t, t0, 2.4)
        c.restore()


def b_conta(c, t, C, B):
    ta, tb, tc, td = (C[f"03.{k}"] for k in "abcd")
    a = fade(t, B["start"], B["end"], 0.2, 0.2)
    _seq(c, t, a, [(L["esc"], ta + 2.4, "100 cm", AMB), (L["mult"], tb, "×", CYA)], size=96)
    # cada resultado quando é falado ("nove metros", "quinze metros", ...)
    res_t = (tb + 3.6, tb + 7.4, tc + 3.0, td + 3.2, td + 6.9)
    res = tuple(ep(t, r, 0.3) for r in res_t)
    foco = 2 if tc + 3.0 <= t < td else None
    cores = (CYA, CYA, MNT, CYA, CYA)
    telas(c, a, t, res=res, foco=foco, cores=cores)


def b_pegadinha(c, t, C, B):
    ta, tb, tc = (C[f"04.{k}"] for k in "abc")
    a = fade(t, B["start"], B["end"], 0.2, 0.2)
    stamp(c, L["armadilha"], CX, 260, RED, a * ep(t, ta + 0.2, 0.2) * (1 - ep(t, ta + 1.8, 0.2)), 76)
    _seq(c, t, a, [(L["d1"], ta + 1.8, "9 m", RED), (L["d2"], tb, "20 m", RED), (L["mult"], tc + 0.5, "×", CYA)], size=78)
    foco = 0 if t < tb else (4 if t < tc else None)
    cores = tuple(RED if i in (0, 4) else (MNT if i == 2 else CYA) for i in range(5))
    telas(c, a, t, res=(1,) * 5, foco=foco, cores=cores)


def b_resposta(c, t, C, B):
    ta, tb = C["05.a"], C["05.b"]
    a = fade(t, B["start"], B["end"], 0.2, 0.2)
    kb = ep(t, tb, 0.3)
    big(c, L["r30"], 300, a * ep(t, ta + 1.6, 0.3) * (1 - ep(t, tb - 0.25, 0.2)), MNT, 110)   # sai antes da letra entrar
    big(c, L["letra"], 300, a * kb, WHITE, 130, hl="C", hl_col=MNT)
    tela(c, 2, 90, 560, 900, a, foco=2, cor_seg=MNT, num=False)
    label(c, L["so5"], CX, 1320, a * ep(t, ta + 2.6, 0.3), 50, AMB, "extrabold")


def b_final(c, t, C, B):
    ta, tb = C["06.a"], C["06.b"]
    a = ep(t, B["start"], 0.2)
    ka = a * (1 - ep(t, tb, 0.25))
    if ka > 0:
        big(c, L["acertou"], 290, ka, WHITE, 104, hl=L["acertou"].split()[-1], hl_col=AMB)
        label(c, L["conta"], CX, 400, ka * ep(t, ta + 0.8, 0.3), 46, AMB, "extrabold")
        telas(c, ka, t, res=(1,) * 5, foco=2, cores=(CYA, CYA, MNT, CYA, CYA))
    kb = a * ep(t, tb, 0.3)
    if kb > 0:
        cartao(c, 120, 330, 840, 800, kb, CYA, L["aula"])
        tela(c, 2, 260, 420, 560, kb, foco=2, cor_seg=MNT, num=False)
        text_mid(c, L["passo"], CX, 950, 46, "extrabold", WHITE, kb)
        glow_text(c, L["canal"], CX, 1060, 96, "black", WHITE, kb * ep(t, tb + 1.0, 0.3), glow=0.14)
        w = text_w(L["canal"], "black", 96)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(CX - w / 2, 1086, w * ep(t, tb + 1.3, 0.6), 12), 6, 6), paint(AMB, kb))


BLOCKS = dict(gancho=b_gancho, opcoes=b_opcoes, conta=b_conta, pegadinha=b_pegadinha, resposta=b_resposta, final=b_final)
