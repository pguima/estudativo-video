"""Visual — Estudativo · Short 041 (vertical 1080x1920): ENEM 2025, questão 152, a fábrica de tijolos (aula: 040).
render.py <proj> --vertical. Paleta e notação do design system de matemática (_ferramentas/matematica.py), com o layout de
Short do 027 (big(), stamp(), contagem() e a legenda, importados de lá) e a grade "funcionários × horas" da aula 040
(grade()). Cores: âmbar = dado (3 × 6, 720), ciano = horas de trabalho, menta = a resposta (1 800), coral = a armadilha."""
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
aula = _carrega("aula040", "040_matematica_fabrica_tijolos")
big, stamp, contagem, CAPTION = sh.big, sh.stamp, sh.contagem, sh.CAPTION
CX, CAP_Y = sh.CX, sh.CAP_Y
grade = aula.grade

IDIOMAS_NO_CODIGO = True
EN = idioma.LANG == "en"
ARQUIVO_FINAL = "estudativo_short_041_fabrica_tijolos.mp4"
MARCA = ""

SOM = dict(intro=False, ganho_trilha=0.32, lufs=-14, bpm=118, sfx={
    "01.a": ["pop", "data@+2.4"], "01.b": "alert",
    "02.a": ["pop", "pop@+0.8", "pop@+1.6", "pop@+2.4", "pop@+3.2"], "02.b": "notif",
    "02.c": ["alert", "tick@+2.5", "tick@+3.3", "tick2@+4.1"],   # tiques do cronômetro 3-2-1 (02.end − 2,5 s)
    "03.a": "data", "03.b": "confirm", "03.c": "confirm", "03.d": "data", "03.e": "confirm",
    "04.a": ["impact", "deny@+1.9"], "04.b": "deny", "04.c": "deny", "04.d": "lock",
    "05.a": "confirm", "05.b": ["impact", "shimmer@+0.3"],
    "06.a": "notif", "06.b": "lock"})

T = dict(   # (inglês, português)
    selo=("ENEM 2025 · MATH QUESTION", "ENEM 2025 · QUESTÃO DE MATEMÁTICA"),
    q1=("HOW MANY BRICKS", "QUANTOS TIJOLOS"), q1b=("A DAY?", "POR DIA?"),
    antes=("3 × 6 h = 720", "3 × 6 h = 720"), agora=("5 × 9 h = ?", "5 × 9 h = ?"),
    comenta=("comment before you see it ↓", "comenta antes de ver ↓"), pausa=("PAUSE AND THINK", "PAUSE E PENSE"),
    horas=("WORK HOURS", "HORAS DE TRABALHO"), h18=("3 × 6 = 18", "3 × 6 = 18"), q40=("720 ÷ 18 = 40", "720 ÷ 18 = 40"),
    h45=("5 × 9 = 45", "5 × 9 = 45"), r1800=("45 × 40 = 1 800", "45 × 40 = 1 800"),
    armadilha=("TRAP!", "ARMADILHA!"), d1=("1 200 = WORKERS ONLY", "1 200 = SÓ FUNCIONÁRIOS"),
    d2=("1 080 = HOURS ONLY", "1 080 = SÓ AS HORAS"), d3=("2 520 = + THE OLD 720", "2 520 = + OS 720 ANTIGOS"),
    d4=("BOTH AT ONCE", "AS DUAS JUNTAS"),
    r=("1 800 BRICKS", "1 800 TIJOLOS"), letra=("ANSWER D", "LETRA D"),
    acertou=("DID YOU GET IT?", "VOCÊ ACERTOU?"), conta=("tell me in the comments ↓", "conta nos comentários ↓"),
    aula=("FULL LESSON", "AULA COMPLETA"), passo=("step by step on the channel", "passo a passo no canal"),
    canal=("ESTUDATIVO ENGLISH", "ESTUDATIVO"),
)
L = {k: (v[0] if EN else v[1]) for k, v in T.items()}
_EXTRA = [] if EN else [("dois mil e vinte e cinco", "2025"), ("setecentos e vinte", "720"), ("mil e oitocentos", "1800"),
                        ("mil e duzentos", "1200"), ("mil e oitenta", "1080"), ("dois mil quinhentos e vinte", "2520"),
                        ("quarenta e cinco", "45")]
matematica.NUMEROS_EXTRA[:] = sorted(_EXTRA, key=lambda p: -len(p[0].split()))

GY = 880          # centro da grade
CEL = 92
ALTS = (("A", "800"), ("B", "1 080"), ("C", "1 200"), ("D", "1 800"), ("E", "2 520"))


def OVERLAY(c, t):
    pill(c, L["selo"], CX, 150, 26, AMB, BG0, 0.95, "extrabold")


def alternativas(c, a, y=1330, ks=(1,) * 5, certo=None, errado=()):
    for j, (le, v) in enumerate(ALTS):
        k = a * ep(ks[j], 0, 0.3)
        if k <= 0:
            continue
        x = CX - 400 + j * 200
        cor = MNT if le == certo else (RED if le in errado else INK2)
        c.drawCircle(x, y, 44, paint(cor, k))
        text_mid(c, le, x, y, 44, "black", BG0, k)
        text_mid(c, v, x, y + 86, 40, "black", cor if (le == certo or le in errado) else WHITE, k)


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
        big(c, L["q1"], 290, kq, WHITE, 96)
        big(c, L["q1b"], 410, kq, WHITE, 104, hl=L["q1b"], hl_col=MNT)
    kg = ep(t, tb + 0.4, 1.6)
    grade(c, CX, GY, 3 + 2 * kg, 6 + 3 * kg, CEL, a * ep(t, ta + 2.3, 0.4), k=ep(t, ta + 2.3, 2.0), cor=AMB,
          cor_novo=CYA, base=(3, 6))
    label(c, L["antes"], CX, 1290, a * ep(t, ta + 5.0, 0.3) * (1 - ep(t, tb, 0.2)), 60, AMB, "black")
    label(c, L["agora"], CX, 1290, a * ep(t, tb + 0.2, 0.3), 60, CYA, "black")


def b_opcoes(c, t, C, B):
    ta, tb, tc = (C[f"02.{k}"] for k in "abc")
    a = fade(t, B["start"], B["end"], 0.2, 0.15)
    t0 = B["end"] - 2.5   # depois do "Valendo!"
    kp = a * ep(t, t0, 0.2)
    big(c, L["q1"], 290, a * (1 - kp), WHITE, 90)
    label(c, L["comenta"], CX, 400, a * ep(t, tb, 0.3) * (1 - kp), 46, AMB, "extrabold")
    grade(c, CX, GY, 5, 9, CEL, a * (1 - 0.75 * kp), cor=AMB, cor_novo=CYA, base=(3, 6))
    ks = tuple(ep(t, ta + 0.1 + 0.9 * j, 0.3) for j in range(5))
    alternativas(c, a * (1 - 0.75 * kp), ks=ks)
    if kp > 0:
        label(c, L["pausa"], CX, 290, kp, 84, AMB, "black")
        c.save(); c.translate(CX, 880); c.scale(1.5, 1.5); c.translate(-CX, -880)
        contagem(c, CX, 880, kp, t, t0, 2.4)
        c.restore()


def b_conta(c, t, C, B):
    ta, tb, tc, td, te = (C[f"03.{k}"] for k in "abcde")
    a = fade(t, B["start"], B["end"], 0.2, 0.2)
    _seq(c, t, a, [(L["horas"], ta + 0.3, None, CYA), (L["h18"], tb + 1.9, "18", CYA), (L["q40"], tc + 1.8, "40", AMB),
                   (L["h45"], td + 1.6, "45", CYA), (L["r1800"], te + 1.3, "1 800", MNT)], size=92)
    kg = ep(t, td + 0.6, 1.4)
    k0 = ep(t, ta + 3.0, 0.3) * (1 / 18) + ep(t, tb + 1.0, 1.4) * (17 / 18)
    cor = MNT if t >= te + 1.3 else CYA
    grade(c, CX, GY, 3 + 2 * kg, 6 + 3 * kg, CEL, a, k=k0 if t < td else 1.0, cor=cor,
          valor="40", kv=ep(t, tc + 1.8, 0.4))


def b_pegadinha(c, t, C, B):
    ta, tb, tc, td = (C[f"04.{k}"] for k in "abcd")
    a = fade(t, B["start"], B["end"], 0.2, 0.2)
    stamp(c, L["armadilha"], CX, 260, RED, a * ep(t, ta + 0.2, 0.2) * (1 - ep(t, ta + 1.6, 0.2)), 76)
    _seq(c, t, a, [(L["d1"], ta + 1.6, "1 200", RED), (L["d2"], tb, "1 080", RED), (L["d3"], tc, "2 520", RED),
                   (L["d4"], td, None, MNT)], size=70)
    if t < tb:
        lin, col, cor, err = 5, 6, RED, ("C",)
    elif t < tc:
        lin, col, cor, err = 3, 9, RED, ("B",)
    elif t < td:
        lin, col, cor, err = 5, 9, RED, ("E",)
    else:
        lin, col, cor, err = 5, 9, MNT, ()
    grade(c, CX, GY, lin, col, CEL, a, cor=cor)
    alternativas(c, a, errado=err)


def b_resposta(c, t, C, B):
    ta, tb = C["05.a"], C["05.b"]
    a = fade(t, B["start"], B["end"], 0.2, 0.2)
    kb = ep(t, tb, 0.3)
    big(c, L["r"], 300, a * ep(t, ta + 0.4, 0.3) * (1 - ep(t, tb - 0.25, 0.2)), MNT, 104)   # sai antes da letra entrar
    big(c, L["letra"], 300, a * kb, WHITE, 130, hl="D", hl_col=MNT)
    grade(c, CX, GY, 5, 9, CEL, a, cor=MNT, valor="40", kv=1.0)
    alternativas(c, a, certo="D")


def b_final(c, t, C, B):
    ta, tb = C["06.a"], C["06.b"]
    a = ep(t, B["start"], 0.2)
    ka = a * (1 - ep(t, tb, 0.25))
    if ka > 0:
        big(c, L["acertou"], 290, ka, WHITE, 104, hl=L["acertou"].split()[-1], hl_col=AMB)
        label(c, L["conta"], CX, 400, ka * ep(t, ta + 0.8, 0.3), 46, AMB, "extrabold")
        grade(c, CX, GY, 5, 9, CEL, ka, cor=MNT, valor="40", kv=1.0)
        alternativas(c, ka, certo="D")
    kb = a * ep(t, tb, 0.3)
    if kb > 0:
        cartao(c, 120, 330, 840, 800, kb, CYA, L["aula"])
        grade(c, CX, 640, 5, 9, 66, kb, cor=MNT)
        text_mid(c, L["passo"], CX, 950, 46, "extrabold", WHITE, kb)
        glow_text(c, L["canal"], CX, 1060, 96, "black", WHITE, kb * ep(t, tb + 1.0, 0.3), glow=0.14)
        w = text_w(L["canal"], "black", 96)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(CX - w / 2, 1086, w * ep(t, tb + 1.3, 0.6), 12), 6, 6), paint(AMB, kb))


BLOCKS = dict(gancho=b_gancho, opcoes=b_opcoes, conta=b_conta, pegadinha=b_pegadinha, resposta=b_resposta, final=b_final)
