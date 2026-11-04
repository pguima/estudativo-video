"""Visual — Estudativo · Short 035 (vertical 1080x1920): ENEM 2025, questão 149, matrículas na escola de idiomas (aula: 034).
render.py <proj> --vertical. Paleta e notação do design system de matemática (_ferramentas/matematica.py), com o layout de
Short do 027 (big(), stamp(), contagem() e a legenda de 1 a 3 palavras, importados de lá) e as peças da aula 034 (pizza(),
barras(), grade() de 400 bolinhas), reposicionadas para a tela em pé. Cores por idioma: ciano = inglês, âmbar = espanhol,
menta = francês, cinza-azulado = alemão; coral = a armadilha."""
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
aula = _carrega("aula034", "034_matematica_escola_idiomas_matriculas")
big, stamp, contagem, CAPTION = sh.big, sh.stamp, sh.contagem, sh.CAPTION
CX, CAP_Y = sh.CX, sh.CAP_Y
aula.GC0, aula.GR0, aula.GS = 160, 640, 40   # a grade de 400 no meio da tela em pé
pizza, barras, grade = aula.pizza, aula.barras, aula.grade
QTD, NOVO, CORES = aula.QTD, aula.NOVO, aula.CORES

IDIOMAS_NO_CODIGO = True
EN = idioma.LANG == "en"
ARQUIVO_FINAL = "estudativo_short_035_escola_idiomas.mp4"
MARCA = ""

SOM = dict(intro=False, ganho_trilha=0.32, lufs=-14, bpm=118, sfx={
    "01.a": ["pop", "data@+2.4"], "01.b": "data", "01.c": "data",
    "02.a": ["pop", "pop@+0.3", "pop@+0.6", "pop@+0.9", "pop@+1.2"], "02.b": "notif",
    "02.c": ["alert", "tick@+2.5", "tick@+3.3", "tick2@+4.1"],   # tiques do cronômetro 3-2-1 (02.end − 2,5 s)
    "03.a": "data", "03.b": "confirm", "03.c": ["data", "confirm@+4.3"], "03.d": ["data", "confirm@+6.1"],
    "04.a": ["impact", "deny@+2.8"], "04.b": "deny", "04.c": "deny",
    "05.a": "confirm", "05.b": ["impact", "shimmer@+0.3"],
    "06.a": "notif", "06.b": "lock"})

T = dict(   # (inglês, português)
    selo=("ENEM 2025 · MATH QUESTION", "ENEM 2025 · QUESTÃO DE MATEMÁTICA"),
    quantos=("HOW MANY STUDENTS", "QUANTOS ALUNOS"), fr=("IN FRENCH?", "NO FRANCÊS?"),
    q2=("FRENCH IN 2025?", "FRANCÊS EM 2025?"),
    comenta=("comment before you see it ↓", "comenta antes de ver ↓"), pausa=("PAUSE AND THINK", "PAUSE E PENSE"),
    soma=("280 + 80 + 20 + 20", "280 + 80 + 20 + 20"), t400=("= 400 STUDENTS", "= 400 ALUNOS"),
    pct=("10% OF 400 = 40", "10% DE 400 = 40"), conf=("240 + 100 + 40 + 20 = 400 ✓", "240 + 100 + 40 + 20 = 400 ✓"),
    armadilha=("TRAP!", "ARMADILHA!"), b20=("20 = 2024, NOT 2025", "20 = 2024, NÃO 2025"), d2=("10% OF 20 = 2 ✗", "10% DE 20 = 2 ✗"),
    r40=("40 STUDENTS", "40 ALUNOS"), dobro=("× 2", "× 2"), letra=("ANSWER E", "LETRA E"),
    acertou=("DID YOU GET IT?", "VOCÊ ACERTOU?"), conta=("tell me in the comments ↓", "conta nos comentários ↓"),
    aula=("FULL LESSON", "AULA COMPLETA"), passo=("step by step on the channel", "passo a passo no canal"),
    canal=("ESTUDATIVO ENGLISH", "ESTUDATIVO"),
)
L = {k: (v[0] if EN else v[1]) for k, v in T.items()}
_EXTRA = [] if EN else [
    ("dois mil e vinte e cinco", "2025"), ("dois mil e vinte e quatro", "2024"), ("dois mil e vinte e três", "2023"),
    ("sessenta por cento", "60%"), ("vinte e cinco por cento", "25%"), ("dez por cento", "10%"), ("cinco por cento", "5%")]
matematica.NUMEROS_EXTRA[:] = sorted(_EXTRA, key=lambda p: -len(p[0].split()))
OPC = (("A", "2"), ("B", "12"), ("C", "20"), ("D", "22"), ("E", "40"))


def OVERLAY(c, t):
    pill(c, L["selo"], CX, 150, 26, AMB, BG0, 0.95, "extrabold")


def graficos(c, a, t, kp=1.0, kb=1.0, foco_b=None, cores_b=None):
    """a pizza de 2023 em cima e as barras de 2024 embaixo"""
    pizza(c, CX, 800, 180, a * ep(kp, 0, 0.3), t, ks=(kp,) * 4, title="2023")
    barras(c, 220, 1400, a * ep(kb, 0, 0.3), ks=(kb,) * 4, kh=1.3, w=100, gap=180, foco=foco_b, cores=cores_b, lab=30)
    label(c, "2024", 900, 1060, a * ep(kb, 0, 0.3), 34, WHITE, "black")


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
        big(c, L["quantos"], 290, kq, WHITE, 92)
        big(c, L["fr"], 410, kq, WHITE, 100, hl=L["fr"], hl_col=MNT)
    graficos(c, a, t, kp=ep(t, tb, 0.8), kb=ep(t, tc + 0.8, 0.8))


def b_opcoes(c, t, C, B):
    ta, tb, tc = (C[f"02.{k}"] for k in "abc")
    a = fade(t, B["start"], B["end"], 0.2, 0.15)
    t0 = B["end"] - 2.5   # depois do "Valendo!"
    kp = a * ep(t, t0, 0.2)
    big(c, L["q2"], 290, a * (1 - kp), WHITE, 100, hl="?", hl_col=MNT)
    label(c, L["comenta"], CX, 400, a * ep(t, tb, 0.3) * (1 - kp), 46, AMB, "extrabold")
    graficos(c, a * (1 - 0.75 * kp), t)
    for j, (le, v) in enumerate(OPC):   # as cinco alternativas
        k = pop(t, ta + j * 0.3, 0.35)
        if k <= 0:
            continue
        x = CX - 360 + j * 180
        c.save(); c.translate(x, 455); c.scale(k, k)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(-75, -45, 150, 90), 22, 22), paint(BG1, 0.95 * a * (1 - 0.7 * kp)))
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(-75, -45, 150, 90), 22, 22), paint(CYA, a * (1 - 0.7 * kp), stroke=4))
        text_mid(c, f"{le} · {v}", 0, 0, 38, "black", WHITE, a * (1 - 0.7 * kp))
        c.restore()
    if kp > 0:
        label(c, L["pausa"], CX, 290, kp, 84, AMB, "black")
        c.save(); c.translate(CX, 880); c.scale(1.5, 1.5); c.translate(-CX, -880)
        contagem(c, CX, 880, kp, t, t0, 2.4)
        c.restore()


def b_conta(c, t, C, B):
    ta, tb, tc, td = (C[f"03.{k}"] for k in "abcd")
    a = fade(t, B["start"], B["end"], 0.2, 0.2)
    _seq(c, t, a, [(L["soma"], ta + 2.4, None, CYA), (L["t400"], tb, "400", CYA), (L["pct"], tc + 2.8, "40", MNT),
                   (L["conf"], td + 6.0, "400 ✓", MNT)], size=96)
    tr = tc + 1.0   # a grade passa para as porcentagens de 2023
    if t < tr:
        grade(c, a, t, [(q, cor, t0) for q, cor, t0 in zip(QTD, CORES, (ta + 2.45, ta + 3.45, ta + 4.15, ta + 4.65))])
    else:
        grade(c, a, t, [(q, cor, t0) for q, cor, t0 in zip(NOVO, CORES, (tr, tr + 0.2, tr + 0.4, tr + 0.6))],
              destaque=2 if t < td else None)
    label(c, "10%", CX, 520, a * ep(t, tc + 2.0, 0.3) * (1 - ep(t, td, 0.3)), 60, MNT, "black")


def b_pegadinha(c, t, C, B):
    ta, tb, tc = (C[f"04.{k}"] for k in "abc")
    a = fade(t, B["start"], B["end"], 0.2, 0.2)
    stamp(c, L["armadilha"], CX, 260, RED, a * ep(t, ta + 0.4, 0.2) * (1 - ep(t, tb, 0.2)), 76)
    _seq(c, t, a, [(L["b20"], tb, "2024", RED), (L["d2"], tc + 1.0, "2", RED)], size=84)
    kr = ep(t, ta + 2.6, 0.3)
    graficos(c, a, t, foco_b=2 if kr > 0 else None, cores_b=(CYA, AMB, aula._mix_cor(MNT, RED, kr), INK2))


def b_resposta(c, t, C, B):
    ta, tb = C["05.a"], C["05.b"]
    a = fade(t, B["start"], B["end"], 0.2, 0.2)
    kb = ep(t, tb, 0.3)
    big(c, L["r40"], 300, a * ep(t, ta + 0.8, 0.3) * (1 - kb), MNT, 110)
    big(c, L["letra"], 300, a * kb, WHITE, 130, hl="E", hl_col=MNT)
    yb, kh = 1300, 14.0
    for j, (ano, v, t0) in enumerate((("2024", 20, ta), ("2025", 40, ta + 0.8))):
        k = a * ep(t, t0, 0.3)
        x = CX - 200 + j * 400
        h = v * kh * ep(t, t0, 0.6)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeLTRB(x - 100, yb - h, x + 100, yb), 14, 14), paint(MNT, (0.45 + 0.5 * j) * k))
        text_mid(c, str(v), x, yb - h - 44, 64, "black", WHITE, k)
        text_mid(c, ano, x, yb + 50, 40, "extrabold", WHITE, k)
    c.drawLine(CX - 400, yb, CX + 400, yb, paint(WHITE, 0.8 * a, stroke=3))
    popill(c, L["dobro"], CX, 640, 56, AMB, BG0, a * ep(t, ta + 2.3, 0.3), t, ta + 2.3)


def b_final(c, t, C, B):
    ta, tb = C["06.a"], C["06.b"]
    a = ep(t, B["start"], 0.2)
    ka = a * (1 - ep(t, tb, 0.25))
    if ka > 0:
        big(c, L["acertou"], 290, ka, WHITE, 104, hl=L["acertou"].split()[-1], hl_col=AMB)
        label(c, L["conta"], CX, 400, ka * ep(t, ta + 0.8, 0.3), 46, AMB, "extrabold")
        pizza(c, CX, 860, 300, ka, t, rot=[str(v) for v in NOVO], foco=2)
    kb = a * ep(t, tb, 0.3)
    if kb > 0:
        cartao(c, 120, 330, 840, 800, kb, CYA, L["aula"])
        pizza(c, CX, 620, 200, kb, t, rot=[str(v) for v in NOVO], foco=2)
        text_mid(c, L["passo"], CX, 950, 46, "extrabold", WHITE, kb)
        glow_text(c, L["canal"], CX, 1060, 96, "black", WHITE, kb * ep(t, tb + 1.0, 0.3), glow=0.14)
        w = text_w(L["canal"], "black", 96)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(CX - w / 2, 1086, w * ep(t, tb + 1.3, 0.6), 12), 6, 6), paint(AMB, kb))


BLOCKS = dict(gancho=b_gancho, opcoes=b_opcoes, conta=b_conta, pegadinha=b_pegadinha, resposta=b_resposta, final=b_final)
