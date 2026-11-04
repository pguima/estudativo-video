"""Visual — Estudativo · Short 031 (vertical 1080x1920): ENEM 2025, questão 147, o herói e os dois vilões (aula: 030).
render.py <proj> --vertical. Paleta e notação do design system de matemática (_ferramentas/matematica.py), com o layout de
Short do 027 (big(), stamp(), contagem() e a legenda de 1 a 3 palavras, importados de lá) e as peças da aula 030 (o plano
cartesiano, heroi(), vilao(), reta(), degrau()), com o plano reposicionado para a tela em pé. Cores: âmbar = os dados,
ciano = a ferramenta (mediatriz, ponto médio), menta = o herói e o caminho certo, coral = os vilões e a armadilha."""
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
aula = _carrega("aula030", "030_matematica_heroi_mediatriz")
big, stamp, contagem, CAPTION = sh.big, sh.stamp, sh.contagem, sh.CAPTION
CX, CAP_Y = sh.CX, sh.CAP_Y
aula.OX, aula.OY, aula.UN = 150, 1330, 78   # o plano no meio da tela em pé
P, plano, heroi, vilao, reta, segmento, ponto, degrau, angulo_reto, quadrado = (
    aula.P, aula.plano, aula.heroi, aula.vilao, aula.reta, aula.segmento, aula.ponto, aula.degrau, aula.angulo_reto,
    aula.quadrado)
S_, V_, T_, U_, M_ = aula.S_, aula.V_, aula.T_, aula.U_, aula.M_

IDIOMAS_NO_CODIGO = True
EN = idioma.LANG == "en"
ARQUIVO_FINAL = "estudativo_short_031_heroi_mediatriz.mp4"
MARCA = ""

SOM = dict(intro=False, ganho_trilha=0.32, lufs=-14, bpm=118, sfx={
    "01.a": ["pop", "data@+2.2"], "01.b": ["pop@+1.1", "pop@+1.7"], "01.c": "alert",
    "02.a": ["pop", "pop@+2.6", "pop@+4.4", "pop@+5.6", "pop@+5.9"], "02.b": "notif",
    "02.c": ["alert", "tick@+2.25", "tick@+3.05", "tick2@+3.85"],   # tiques do cronômetro 3-2-1 (02.end − 2,5 s)
    "03.a": "data", "03.b": ["data", "confirm@+5.0"], "03.c": ["data", "confirm@+3.7"],
    "04.a": ["impact", "alert@+2.0"], "04.b": "data", "04.c": "deny",
    "05.a": "data", "05.b": "confirm", "05.c": "confirm", "05.d": ["impact", "shimmer@+0.3"],
    "06.a": "notif", "06.b": "lock"})

T = dict(   # (inglês, português)
    selo=("ENEM 2025 · MATH QUESTION", "ENEM 2025 · QUESTÃO DE MATEMÁTICA"),
    onde=("WHERE CAN THE HERO", "POR ONDE O HERÓI"), foge=("WALK SAFELY?", "ANDA SEM APANHAR?"),
    perto=("the nearest villain attacks", "o vilão mais perto ataca"), qual=("WHICH LINE?", "QUAL RETA?"),
    comenta=("comment before you see it ↓", "comenta antes de ver ↓"), pausa=("PAUSE AND THINK", "PAUSE E PENSE"),
    mediatriz=("BISECTOR", "MEDIATRIZ"), mesma=("same distance from T and V", "mesma distância de T e de V"),
    meio=("M(5; 5)", "M(5; 5)"), incl=("SLOPE 1/3", "INCLINAÇÃO 1/3"),
    armadilha=("TRAP!", "ARMADILHA!"), perp=("PERPENDICULAR!", "PERPENDICULAR!"),
    inv=("1/3 → −3", "1/3 → −3"), troca=("flip it and CHANGE THE SIGN", "inverte e TROCA O SINAL"),
    de=("D and E: +3 ✗", "D e E: +3 ✗"), eqf=("y = −3x + 20", "y = −3x + 20"), passaS=("goes through S ✓", "passa pelo S ✓"),
    letra=("ANSWER A", "LETRA A"), acertou=("DID YOU GET IT?", "VOCÊ ACERTOU?"), conta=("tell me in the comments ↓", "conta nos comentários ↓"),
    aula=("FULL LESSON", "AULA COMPLETA"), passo=("step by step on the channel", "passo a passo no canal"),
    canal=("ESTUDATIVO ENGLISH", "ESTUDATIVO"),
)
L = {k: (v[0] if EN else v[1]) for k, v in T.items()}
_EXTRA = [] if EN else [
    ("dois mil e vinte e cinco", "2025"), ("mais perto", "mais perto"), ("oito e seis", "(8; 6)"), ("dois e quatro", "(2; 4)"),
    ("cinco e cinco", "(5; 5)"), ("ípsilon", "y"), ("três xis", "3x"), ("xis", "x"), ("um terço", "1/3")]
matematica.NUMEROS_EXTRA[:] = sorted(_EXTRA, key=lambda p: -len(p[0].split()))
OPCOES = (("A", "y = −3x + 20"), ("B", "y = −3x + 16"), ("C", "y = −3x − 20"), ("D", "y = 3x + 16"), ("E", "y = 3x − 16"))


def OVERLAY(c, t):
    pill(c, L["selo"], CX, 150, 26, AMB, BG0, 0.95, "extrabold")


def cena(c, a, t, tv=None, tt=None, quad=0.0, s=True):
    """o plano, o quadrado, o herói em S e os vilões (V em tv, T em tt; None = já estão lá)"""
    plano(c, a)
    quadrado(c, a * quad)
    if s:
        heroi(c, *S_, a, rot="S", dx=-38, dy=38)
    for q, t0, rot, dx in ((V_, tv, "V", 42), (T_, tt, "T", -42)):
        k = pop(t, t0, 0.35) if t0 is not None else 1.0
        vilao(c, *q, a, k=k, rot=rot if k > 0 else None, dx=dx, dy=-34)


def opcao_eq(c, le, s, cy, a, k=1.0, cor=CYA, dim=0.0, marca=None):
    if a <= 0 or k <= 0:
        return
    a = a * (1 - 0.7 * dim)
    c.save(); c.translate(CX, cy); c.scale(k, k)
    r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(-380, -58, 760, 116), 26, 26)
    c.drawRRect(r, paint(BG1, 0.95 * a))
    c.drawRRect(r, paint(cor, a, stroke=4))
    c.drawCircle(-300, 0, 36, paint(cor, a))
    text_mid(c, le, -300, 0, 40, "black", BG0, a)
    text_mid(c, s, 50, 0, 58, "black", WHITE, a)
    if marca is not None:
        (check if marca else cross)(c, 330, 0, 28, a)
    c.restore()


# ---------------------------------------------------------------- cenas
def b_gancho(c, t, C, B):
    ta, tb, tc = (C[f"01.{k}"] for k in "abc")
    a = 1 - prog(t, B["end"] - 0.2, 0.2)
    kq = a * ep(t, ta + 0.2, 0.2)   # a pergunta já no começo
    if kq > 0:
        k = 1 + 0.04 * math.sin(t * 8) * ep(t, tc, 0.2)
        c.save(); c.translate(CX, 340); c.scale(k, k); c.translate(-CX, -340)
        big(c, L["onde"], 290, kq, WHITE, 84)
        big(c, L["foge"], 410, kq, WHITE, 92, hl=L["foge"], hl_col=MNT)
        c.restore()
    kp = a * ep(t, ta + 2.2, 0.3)
    cena(c, kp, t, tb + 1.7, tb + 1.1, quad=ep(t, tb + 2.8, 0.5))
    label(c, L["perto"], CX, 540, kp * ep(t, ta + 3.8, 0.3), 42, RED, "extrabold")
    kc = a * ep(t, tc + 1.0, 0.3)   # as linhas de ataque: de S até cada vilão
    for q in (T_, V_):
        segmento(c, S_, q, kc * (0.6 + 0.4 * math.sin(t * 6) ** 2), RED, 4, tracej=True)


def b_opcoes(c, t, C, B):
    ta, tb, tc = (C[f"02.{k}"] for k in "abc")
    a = fade(t, B["start"], B["end"], 0.2, 0.15)
    t0 = B["end"] - 2.5   # depois do "Valendo!"
    kp = a * ep(t, t0, 0.2)
    big(c, L["qual"], 290, a * (1 - kp), WHITE, 104, hl="?", hl_col=CYA)
    label(c, L["comenta"], CX, 400, a * ep(t, tb, 0.3) * (1 - kp), 46, AMB, "extrabold")
    for j, ((le, s), dt) in enumerate(zip(OPCOES, (0.0, 2.6, 4.4, 5.6, 5.9))):
        opcao_eq(c, le, s, 560 + j * 160, a, pop(t, ta + dt, 0.35), CYA if j < 3 else AMB, dim=0.75 * ep(t, t0, 0.2))
    if kp > 0:
        label(c, L["pausa"], CX, 290, kp, 84, AMB, "black")
        c.save(); c.translate(CX, 880); c.scale(1.5, 1.5); c.translate(-CX, -880)
        contagem(c, CX, 880, kp, t, t0, 2.4)
        c.restore()


def b_conta(c, t, C, B):
    ta, tb, tc = (C[f"03.{k}"] for k in "abc")
    a = fade(t, B["start"], B["end"], 0.2, 0.2)
    tm, ti = tb + 5.0, tc + 3.7
    for s, t0, t1, hl, hc in ((L["mediatriz"], ta + 2.6, tb, L["mediatriz"], CYA), (L["meio"], tm, tc, "(5; 5)", CYA),
                              (L["incl"], ti, B["end"] + 1, "1/3", CYA)):
        k = a * ep(t, t0, 0.3) * (1 - ep(t, t1, 0.2))
        if k > 0:
            big(c, s, 330, k, WHITE, 100, hl=hl, hl_col=hc)
    cena(c, a, t, s=False)
    ka = a * ep(t, ta + 0.4, 0.3) * (1 - ep(t, tb, 0.3))   # pontos à mesma distância dos dois vilões
    for j, d in enumerate((-2.4, 0.0, 2.4)):
        q = (M_[0] - d / math.sqrt(10), M_[1] + 3 * d / math.sqrt(10))
        kk = ka * ep(t, ta + 0.6 + j * 0.4, 0.3)
        segmento(c, q, T_, kk * 0.8, AMB, 3, tracej=True)
        segmento(c, q, V_, kk * 0.8, AMB, 3, tracej=True)
        ponto(c, *q, kk, CYA)
    reta(c, *M_, -1, 3, a * ep(t, ta + 2.6, 0.3), CYA, u=ep(t, ta + 2.6, 0.8), w=5, tracej=True)
    label(c, L["mesma"], CX, 470, a * ep(t, ta + 0.6, 0.3) * (1 - ep(t, tb, 0.3)), 40, AMB, "extrabold")
    kb = a * ep(t, tb, 0.3)
    ponto(c, *T_, kb * ep(t, tb + 0.6, 0.3), AMB, "(2; 4)", dx=0, dy=56, r=0.1)
    ponto(c, *V_, kb * ep(t, tb + 2.4, 0.3), AMB, "(8; 6)", dx=0, dy=56, r=0.1)
    segmento(c, T_, V_, kb, WHITE, 4, u=ep(t, tb + 3.5, 0.6))
    ponto(c, *M_, a * ep(t, tm, 0.3), CYA, "M", dx=-34, dy=-30, k=pop(t, tm), r=13, size=36)
    degrau(c, T_, V_, a, t, tc + 2.6, tc + 1.5, "6", "2", fx=0.25)


def b_pegadinha(c, t, C, B):
    ta, tb, tc = (C[f"04.{k}"] for k in "abc")
    a = fade(t, B["start"], B["end"], 0.2, 0.2)
    stamp(c, L["armadilha"], CX, 260, RED, a * ep(t, ta + 0.4, 0.2) * (1 - ep(t, ta + 2.0, 0.2)), 76)
    big(c, L["perp"], 290, a * ep(t, ta + 2.0, 0.3) * (1 - ep(t, tb + 2.0, 0.2)), CYA, 100)
    big(c, L["inv"], 290, a * ep(t, tb + 2.0, 0.3), WHITE, 120, hl="−3", hl_col=MNT)
    label(c, L["troca"], CX, 420, a * ep(t, tb + 1.4, 0.3), 46, AMB, "black")
    cena(c, a, t, s=False)
    segmento(c, T_, V_, a, WHITE, 4)
    reta(c, *M_, -1, 3, a, MNT, u=ep(t, ta + 2.0, 0.8))
    angulo_reto(c, M_, (3, 1), (-1, 3), a * ep(t, ta + 2.6, 0.3), 26)
    ponto(c, *M_, a, CYA, r=12)
    kc = a * ep(t, tc + 1.2, 0.3)   # D e E: inclinação +3, sem trocar o sinal
    reta(c, *M_, 1, 3, kc, RED, u=ep(t, tc + 1.2, 0.8), w=5, tracej=True)
    popill(c, L["de"], 780, 650, 40, RED, BG0, kc, t, tc + 1.4)


def b_resposta(c, t, C, B):
    ta, tb, tc, td = (C[f"05.{k}"] for k in "abcd")
    a = fade(t, B["start"], B["end"], 0.2, 0.2)
    kd = ep(t, td, 0.3)
    big(c, L["eqf"], 300, a * ep(t, tb, 0.3) * (1 - kd), WHITE, 110, hl="−3x + 20", hl_col=MNT)
    big(c, L["letra"], 300, a * kd, WHITE, 130, hl="A", hl_col=MNT)
    cena(c, a, t, quad=0.6, s=False)
    reta(c, *M_, -1, 3, a, MNT, w=7)
    ponto(c, *M_, a * (1 - ep(t, tc, 0.3)), CYA, r=12)
    u = ep(t, tc + 2.6, 2.0)   # o herói sai do S pela mediatriz
    x, y = S_[0] + (U_[0] - S_[0]) * u, S_[1] + (U_[1] - S_[1]) * u
    heroi(c, x, y, a, k=1 + 0.3 * pop(t, tc + 1.8, 0.4) * (1 - u))
    popill(c, L["passaS"], 760, 1180, 40, MNT, BG0, a * ep(t, tc + 1.8, 0.3), t, tc + 1.8)


def b_final(c, t, C, B):
    ta, tb = C["06.a"], C["06.b"]
    a = ep(t, B["start"], 0.2)
    ka = a * (1 - ep(t, tb, 0.25))
    if ka > 0:
        big(c, L["acertou"], 290, ka, WHITE, 104, hl=L["acertou"].split()[-1], hl_col=AMB)
        label(c, L["conta"], CX, 400, ka * ep(t, ta + 0.8, 0.3), 46, AMB, "extrabold")
        cena(c, ka, t, quad=0.6, s=False)
        reta(c, *M_, -1, 3, ka, MNT, w=7)
        heroi(c, *U_, ka)
    kb = a * ep(t, tb, 0.3)
    if kb > 0:
        cartao(c, 120, 330, 840, 800, kb, CYA, L["aula"])
        c.save(); c.translate(CX, 0); c.scale(0.5, 0.5); c.translate(-CX, 92)
        cena(c, kb, t, quad=0.6, s=False)
        reta(c, *M_, -1, 3, kb, MNT, w=7)
        heroi(c, *U_, kb)
        c.restore()
        text_mid(c, L["passo"], CX, 950, 46, "extrabold", WHITE, kb)
        glow_text(c, L["canal"], CX, 1060, 96, "black", WHITE, kb * ep(t, tb + 1.0, 0.3), glow=0.14)
        w = text_w(L["canal"], "black", 96)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(CX - w / 2, 1086, w * ep(t, tb + 1.3, 0.6), 12), 6, 6), paint(AMB, kb))


BLOCKS = dict(gancho=b_gancho, opcoes=b_opcoes, conta=b_conta, pegadinha=b_pegadinha, resposta=b_resposta, final=b_final)
