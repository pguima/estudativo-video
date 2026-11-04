"""Visual — Estudativo · Short 039 (vertical 1080x1920): ENEM 2025, questão 151, os vértices da cúpula pentagonal
giralongada (aula: 038). render.py <proj> --vertical. Paleta e notação do design system de matemática
(_ferramentas/matematica.py), com o layout de Short do 027 (big(), stamp(), contagem() e a legenda, importados de lá)
e o sólido 3D da aula 038 (poliedro.py). Cores das faces como na prova; vértices em branco; arestas em ciano;
menta = a resposta (25); coral = a armadilha (110 lados, 55 arestas)."""
import importlib.util
import sys
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
big, stamp, contagem, CAPTION = sh.big, sh.stamp, sh.contagem, sh.CAPTION
CX, CAP_Y = sh.CX, sh.CAP_Y
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "038_matematica_poliedro_vertices" / "roteiro"))
import poliedro as PL  # noqa: E402

IDIOMAS_NO_CODIGO = True
EN = idioma.LANG == "en"
ARQUIVO_FINAL = "estudativo_short_039_poliedro_vertices.mp4"
MARCA = ""

SOM = dict(intro=False, ganho_trilha=0.32, lufs=-14, bpm=118, sfx={
    "01.a": ["pop", "shimmer@+1.4"], "01.b": "alert",
    "02.a": ["pop", "pop@+0.8", "pop@+1.6", "pop@+2.4", "pop@+3.0"], "02.b": "notif",
    "02.c": ["alert", "tick@+2.5", "tick@+3.3", "tick2@+4.1"],   # tiques do cronômetro 3-2-1 (02.end − 2,5 s)
    "03.a": "data", "03.b": "data", "03.c": "confirm", "03.d": "lock", "03.e": "confirm",
    "04.a": ["impact", "deny@+2.2"], "04.b": "deny", "04.c": ["pop@+1.4", "pop@+2.2", "pop@+3.0"],
    "05.a": "confirm", "05.b": ["impact", "shimmer@+0.3"],
    "06.a": "notif", "06.b": "lock"})

T = dict(   # (inglês, português)
    selo=("ENEM 2025 · MATH QUESTION", "ENEM 2025 · QUESTÃO DE MATEMÁTICA"),
    q1=("HOW MANY", "QUANTOS"), q1b=("VERTICES?", "VÉRTICES?"),
    comenta=("comment before you see it ↓", "comenta antes de ver ↓"), pausa=("PAUSE AND THINK", "PAUSE E PENSE"),
    as_faces=("THE FACES", "AS FACES"), faces=("32 FACES", "32 FACES"), lados=("110 SIDES", "110 LADOS"), arestas=("55 EDGES", "55 ARESTAS"),
    euler=("V − E + F = 2", "V − A + F = 2"), v25=("V = 2 + 55 − 32 = 25", "V = 2 + 55 − 32 = 25"),
    armadilha=("TRAP!", "ARMADILHA!"), d1=("110 = SIDES", "110 = LADOS"), d2=("55 = EDGES", "55 = ARESTAS"),
    anel=("5 + 10 + 10", "5 + 10 + 10"),
    r25=("25 VERTICES", "25 VÉRTICES"), letra=("ANSWER B", "LETRA B"),
    acertou=("DID YOU GET IT?", "VOCÊ ACERTOU?"), conta=("tell me in the comments ↓", "conta nos comentários ↓"),
    aula=("FULL LESSON", "AULA COMPLETA"), passo=("step by step on the channel", "passo a passo no canal"),
    canal=("ESTUDATIVO ENGLISH", "ESTUDATIVO"),
)
L = {k: (v[0] if EN else v[1]) for k, v in T.items()}
_EXTRA = [] if EN else [("dois mil e vinte e cinco", "2025"), ("cento e dez", "110"), ("cinquenta e cinco", "55"),
                        ("vinte e cinco", "25"), ("trinta e duas", "32"), ("trinta e dois", "32"),
                        ("setenta e cinco", "75"), ("vinte e um", "21")]
matematica.NUMEROS_EXTRA[:] = sorted(_EXTRA, key=lambda p: -len(p[0].split()))

TRI = "#3D7BE0"
COR = dict(tri_a=TRI, tri_c=TRI, sq=AMB, pent=MNT, dec=RED)
TRIS = {"tri_a", "tri_c"}
SY = 900          # centro do sólido
ESC = 245
ALTS = (("A", "21"), ("B", "25"), ("C", "55"), ("D", "80"), ("E", "110"))


def OVERLAY(c, t):
    pill(c, L["selo"], CX, 150, 26, AMB, BG0, 0.95, "extrabold")


def solido(c, t, a, cy=SY, escala=ESC, tilt=0.42, **kw):
    return PL.desenha(c, PL.j24(), CX, cy, escala, 0.4 + 0.45 * t, tilt, a, COR, **kw)


def alternativas(c, a, y=1300, ks=(1,) * 5, certo=None, errado=()):
    for j, (le, v) in enumerate(ALTS):
        k = a * ep(ks[j], 0, 0.3)
        if k <= 0:
            continue
        x = CX - 400 + j * 200
        cor = MNT if le == certo else (RED if le in errado else INK2)
        c.drawCircle(x, y, 44, paint(cor, k))
        text_mid(c, le, x, y, 44, "black", BG0, k)
        text_mid(c, v, x, y + 86, 46, "black", cor if (le == certo or le in errado) else WHITE, k)


def _seq(c, t, a, itens, y=330, size=100):
    for j, (s, t0, hl, hc) in enumerate(itens):
        t1 = itens[j + 1][1] if j + 1 < len(itens) else 1e9
        k = a * ep(t, t0, 0.3) * (1 - ep(t, t1, 0.2))
        if k > 0:
            big(c, s, y, k, WHITE, size, hl=hl, hl_col=hc)


# ---------------------------------------------------------------- cenas
def b_gancho(c, t, C, B):
    ta, tb = C["01.a"], C["01.b"]
    a = 1 - prog(t, B["end"] - 0.2, 0.2)
    kq = a * ep(t, ta + 0.2, 0.2)   # a pergunta já no começo
    if kq > 0:
        big(c, L["q1"], 290, kq, WHITE, 104)
        big(c, L["q1b"], 410, kq, WHITE, 108, hl=L["q1b"], hl_col=MNT)
    solido(c, t, a * ep(t, ta + 0.4, 0.5), escala=ESC * (0.85 + 0.15 * ep(t, ta + 0.4, 1.2)),
           vert={0: 0.9 * ep(t, tb + 0.6, 0.4), 1: 0.9 * ep(t, tb + 0.8, 0.4), 2: 0.9 * ep(t, tb + 1.0, 0.4)})


def b_opcoes(c, t, C, B):
    ta, tb, tc = (C[f"02.{k}"] for k in "abc")
    a = fade(t, B["start"], B["end"], 0.2, 0.15)
    t0 = B["end"] - 2.5   # depois do "Valendo!"
    kp = a * ep(t, t0, 0.2)
    big(c, L["q1"] + " " + L["q1b"], 290, a * (1 - kp), WHITE, 90, hl=L["q1b"], hl_col=MNT)
    label(c, L["comenta"], CX, 400, a * ep(t, tb, 0.3) * (1 - kp), 46, AMB, "extrabold")
    solido(c, t, a * (1 - 0.75 * kp), vert={0: 0.9, 1: 0.9, 2: 0.9})
    ks = tuple(ep(t, ta + 0.1 + 0.8 * j, 0.3) for j in range(5))
    alternativas(c, a * (1 - 0.75 * kp), ks=ks)
    if kp > 0:
        label(c, L["pausa"], CX, 290, kp, 84, AMB, "black")
        c.save(); c.translate(CX, 880); c.scale(1.5, 1.5); c.translate(-CX, -880)
        contagem(c, CX, 880, kp, t, t0, 2.4)
        c.restore()


def b_conta(c, t, C, B):
    ta, tb, tc, td, te = (C[f"03.{k}"] for k in "abcde")
    a = fade(t, B["start"], B["end"], 0.2, 0.2)
    # as faces, uma de cada vez, quando são faladas
    foco = None
    for f, d in (({"dec"}, 1.2), ({"pent"}, 2.0), ({"sq"}, 2.8), (TRIS, 3.7), (None, 5.2)):
        if t >= ta + d:
            foco = f
    kb = ep(t, ta + 1.0, 0.4) * (1 - ep(t, ta + 2.0, 0.5))   # de baixo para ver o decágono
    _seq(c, t, a, [(L["as_faces"], ta + 0.3, None, AMB), (L["faces"], ta + 5.2, "32", AMB), (L["lados"], tb + 3.6, "110", WHITE),
                   (L["arestas"], tc + 1.9, "55", CYA), (L["euler"], td + 0.4, None, AMB),
                   (L["v25"], te + 0.4, "25", MNT)], size=86)
    vert = {0: ep(t, te + 2.6, 0.3), 1: ep(t, te + 2.6, 0.3), 2: ep(t, te + 2.6, 0.3)}
    solido(c, t, a, tilt=0.42 - 1.0 * kb, modo="vidro", foco=foco if t < tb else None,
           k_ar=ep(t, tc, 0.4) * (1 - ep(t, td, 0.4)), cor_ar=CYA, vert=vert, cor_vert=MNT)


def b_pegadinha(c, t, C, B):
    ta, tb, tc = (C[f"04.{k}"] for k in "abc")
    a = fade(t, B["start"], B["end"], 0.2, 0.2)
    stamp(c, L["armadilha"], CX, 260, RED, a * ep(t, ta + 0.2, 0.2) * (1 - ep(t, ta + 1.8, 0.2)), 76)
    _seq(c, t, a, [(L["d1"], ta + 2.0, "110", RED), (L["d2"], tb, "55", RED), (L["anel"], tc + 1.2, None, MNT)], size=86)
    aneis = {0: ep(t, tc + 1.4, 0.3), 1: ep(t, tc + 2.2, 0.3), 2: ep(t, tc + 3.0, 0.3)}
    solido(c, t, a, modo="vidro", k_ar=ep(t, tb, 0.4) * (1 - ep(t, tc, 0.4)), cor_ar=RED, vert=aneis)
    errado = ("E",) if t < tb else (("C",) if t < tc else ())
    alternativas(c, a, certo=None, errado=errado)


def b_resposta(c, t, C, B):
    ta, tb = C["05.a"], C["05.b"]
    a = fade(t, B["start"], B["end"], 0.2, 0.2)
    kb = ep(t, tb, 0.3)
    big(c, L["r25"], 300, a * ep(t, ta + 0.4, 0.3) * (1 - ep(t, tb - 0.25, 0.2)), MNT, 104)   # sai antes da letra entrar
    big(c, L["letra"], 300, a * kb, WHITE, 130, hl="B", hl_col=MNT)
    solido(c, t, a, modo="vidro", vert={0: 1, 1: 1, 2: 1}, cor_vert=MNT)
    alternativas(c, a, certo="B")


def b_final(c, t, C, B):
    ta, tb = C["06.a"], C["06.b"]
    a = ep(t, B["start"], 0.2)
    ka = a * (1 - ep(t, tb, 0.25))
    if ka > 0:
        big(c, L["acertou"], 290, ka, WHITE, 104, hl=L["acertou"].split()[-1], hl_col=AMB)
        label(c, L["conta"], CX, 400, ka * ep(t, ta + 0.8, 0.3), 46, AMB, "extrabold")
        solido(c, t, ka, vert={0: 1, 1: 1, 2: 1}, cor_vert=MNT)
        alternativas(c, ka, certo="B")
    kb = a * ep(t, tb, 0.3)
    if kb > 0:
        cartao(c, 120, 330, 840, 800, kb, CYA, L["aula"])
        solido(c, t, kb, cy=640, escala=180)
        text_mid(c, L["passo"], CX, 950, 46, "extrabold", WHITE, kb)
        glow_text(c, L["canal"], CX, 1060, 96, "black", WHITE, kb * ep(t, tb + 1.0, 0.3), glow=0.14)
        w = text_w(L["canal"], "black", 96)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(CX - w / 2, 1086, w * ep(t, tb + 1.3, 0.6), 12), 6, 6), paint(AMB, kb))


BLOCKS = dict(gancho=b_gancho, opcoes=b_opcoes, conta=b_conta, pegadinha=b_pegadinha, resposta=b_resposta, final=b_final)
