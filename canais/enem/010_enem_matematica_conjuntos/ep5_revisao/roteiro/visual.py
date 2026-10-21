"""Visual — Operações e Conjuntos Numéricos, Episódio 5: Revisão geral, pegadinhas e treino (tema claro).
Cores com função: azul = definição · roxo = regra · âmbar = armadilha ("PEGADINHA") · verde = dica/acerto · vermelho = erro.
Como é revisão, reaproveita as peças dos episódios 1 a 4 (cada uma com a sua analogia):
  ep1: fila do pronto-socorro + expressão que encolhe · ep2: bonecas russas · ep3: colchete-braço + reta · ep4: Venn.
Peças novas: cronômetro nas pausas, selo PEGADINHA, índice com os 4 ícones dos episódios.
"""
import importlib.util
import json
import math
import re
import unicodedata
from functools import lru_cache
from pathlib import Path
import skia
import motor
motor.set_theme("claro")
from motor import *  # noqa
from aula import *  # noqa

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_conjuntos_ep5_revisao.mp4"
CARD_R = (140, 150, 1640, 690)
SERIE = Path(__file__).resolve().parents[2]


def _mod(nome, ep):
    spec = importlib.util.spec_from_file_location(nome, SERIE / ep / "roteiro" / "visual.py")
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    return m


E1 = _mod("vis_ep1", "ep1_ordem_e_sinais")
E2 = _mod("vis_ep2", "ep2_conjuntos_numericos")
E3 = _mod("vis_ep3", "ep3_intervalos")
E4 = _mod("vis_ep4", "ep4_venn")
motor.set_theme("claro")
ftext, fmid, ftext_w, tag, regra = E4.ftext, E4.fmid, E4.ftext_w, E4.tag, E4.regra
apenas_txt = E4.apenas_txt


# ======================================================================
# tempos das palavras (deste episódio)
# ======================================================================

def _n(s):
    s = unicodedata.normalize("NFD", s.lower())
    return re.sub(r"[^a-z0-9]", "", "".join(ch for ch in s if unicodedata.category(ch) != "Mn"))


@lru_cache(None)
def _words():
    p = Path(__file__).resolve().parents[1] / "audio" / "tempos.json"
    if not p.exists():
        return {}
    d = json.loads(p.read_text(encoding="utf-8"))
    return {s["id"]: [(_n(w["disp"]), w["t0"]) for w in s.get("tokens", [])] for s in d["scenes"]}


def WT(C, sid, palavra, k=1, depois=None):
    ws = [(w, C[sid] + t0) for w, t0 in _words().get(sid, []) if w == _n(palavra)]
    if depois is not None:
        ws = [x for x in ws if x[1] >= depois - 0.05]
    if not ws:
        return (depois if depois is not None else C[sid]) + 1.2
    return ws[k - 1 if k > 0 else k][1]


# ======================================================================
# peças novas
# ======================================================================

def cronometro(c, cx, cy, t, t0, t1, a=1.0, r=56):
    """anel que esvazia de t0 a t1 (a pausa do aluno)"""
    av = a * ep(t, t0, 0.3) * (1 - prog(t, t1, 0.3))
    if av <= 0:
        return
    f = clamp((t - t0) / max(0.1, t1 - t0))
    c.drawCircle(cx, cy, r + 10, paint("#FFFFFF", av))
    c.drawCircle(cx, cy, r, paint(LINE, av, stroke=12))
    p = skia.Path()
    p.addArc(skia.Rect.MakeXYWH(cx - r, cy - r, 2 * r, 2 * r), -90, 360 * (1 - f))
    c.drawPath(p, paint(AMBER, av, stroke=12, cap_round=True))
    fmid(c, str(max(0, math.ceil((t1 - t) - 0.01))) + "s", cx, cy, 30, "black", INK, av)
    text(c, "PAUSE", cx, cy + r + 44, 24, "black", AMBER, av)


def selo_pegadinha(c, cx, cy, a, ang=-6):
    if a <= 0:
        return
    s = 0.7 + 0.3 * ease_back(clamp(a))
    c.save(); c.translate(cx, cy); c.rotate(ang); c.scale(s, s)
    w = text_w("PEGADINHA", "black", 30) + 60
    rrect(c, -w / 2, -30, w, 60, 14, AMBER, a, shadow=True)
    text_mid(c, "PEGADINHA", 0, 0, 30, "black", INK, a)
    c.restore()


def carimbo_falso(c, cx, cy, a):
    if a <= 0:
        return
    s = 1.4 - 0.4 * ease_back(clamp(a))
    c.save(); c.translate(cx, cy); c.rotate(-8); c.scale(s, s)
    w = text_w("FALSO", "black", 70) + 70
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(-w / 2, -56, w, 112), 18, 18), paint(RED, a, stroke=7))
    text_mid(c, "FALSO", 0, 0, 70, "black", RED, a)
    c.restore()


def icone_ep(c, k, cx, cy, a, s=1.0):
    """os 4 ícones dos episódios: 0 fila/semáforo · 1 bonecas · 2 colchetes · 3 dois círculos"""
    if a <= 0:
        return
    if k == 0:
        rrect(c, cx - 26 * s, cy - 70 * s, 52 * s, 140 * s, 14 * s, INK, a)
        for j, col in enumerate(("#E5484D", "#E8A317", "#16A36A")):
            c.drawCircle(cx, cy - 42 * s + j * 42 * s, 15 * s, paint(col, a))
    elif k == 1:
        for j, (h, col) in enumerate(((130, E2.CQ), (95, E2.CZ), (65, E2.CN))):
            E2.boneca(c, cx - 50 * s + j * 50 * s, cy + 60 * s, h * s, col, a)
    elif k == 2:
        E3.notacao(c, cx, cy, 54 * s, "2", "5", 1, 0, a)
    else:
        for x, col in ((cx - 30 * s, E4.CA), (cx + 30 * s, E4.CB)):
            c.drawCircle(x, cy, 55 * s, paint(col, a * 0.12)); c.drawCircle(x, cy, 55 * s, paint(col, a, stroke=5))


EPS = ["ordem e sinais", "conjuntos numéricos", "intervalos", "Venn"]


def ep_chip(c, k, a):
    """selo no canto: qual episódio está sendo revisto"""
    if a <= 0:
        return
    rrect(c, 160, 168, 330, 64, 18, "#FFFFFF", a, shadow=True)
    icone_ep(c, k, 200, 200, a, 0.32)
    text_mid(c, f"ep. {k + 1} · {EPS[k]}", 236, 200, 22, "black", INK2, a, align="left")


# ======================================================================
# gancho, como cai, índice
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "REVISÃO · EPISÓDIO 5", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["01.a"], 0.5)
    text(c, "quase não cai SOZINHO", W / 2, 260, 44, "black", INK2, aa)
    ab = ep(t, C["01.b"], 0.5)
    for k, (area, chip) in enumerate((("FÍSICA", "−(−12)"), ("FUNÇÃO", "(−3)²"), ("ESTATÍSTICA", "√2"), ("QUALQUER QUESTÃO", "A ∩ B"))):
        ak = ab * ep(t, C["01.b"] + 0.3 * k, 0.4)
        x = 300 + k * 380
        card(c, x - 160, 330, 320, 300, ak)
        text(c, area, x, 390, 26, "black", INK2, ak)
        for j in range(3):
            rrect(c, x - 110, 420 + j * 40, 220 - 50 * (j % 2), 14, 7, LINE, ak)
        tag(c, chip, x, 580, PURPLE, ak, 28)
    regra(c, "aqui se perde ponto em questão que você SABIA", W / 2, 740, ep(t, C["01.c"], 0.5), 32, RED, w=1200)


def b_como_cai(c, t, C, B):
    head(c, t, B["start"], "COMO O ENEM COBRA", "TRÊS JEITOS", BLUE)
    for k, (cue, tit, sub) in enumerate((("02.a", "Venn com pessoas", "cai quase todo ano"),
                                         ("02.b", "contas dentro", "de outra questão"),
                                         ("02.c", "classificar e", "ordenar números"))):
        a, dy = rise(t, C[cue])
        if a <= 0:
            continue
        x = 230 + k * 500
        card(c, x, 220 + dy, 460, 500, a)
        badge_num(c, k + 1, x + 230, 290 + dy, a, 32, bg=BLUE)
        if k == 0:
            icone_ep(c, 3, x + 230, 430 + dy, a, 1.1)
        elif k == 1:
            fmid(c, "20 − 3·(−4)", x + 230, 430 + dy, 46, "black", PURPLE, a)
        else:
            fmid(c, "√3  <  7/4", x + 230, 430 + dy, 52, "black", PURPLE, a)
        text(c, tit, x + 230, 580 + dy, 34, "black", INK, a)
        text(c, sub, x + 230, 630 + dy, 30, "bold", INK2, a)


def b_indice(c, t, C, B):
    head(c, t, B["start"], "A REVISÃO", "OS QUATRO EPISÓDIOS", PURPLE)
    card(c, *CARD_R)
    for k, cue in enumerate(("03.a", "03.b", "03.c", "03.d")):
        a, dy = rise(t, C[cue])
        x = 330 + k * 420
        icone_ep(c, k, x, 380 + dy, a, 1.3)
        text(c, f"EP. {k + 1}", x, 540 + dy, 28, "black", PURPLE, a)
        text(c, EPS[k], x, 585 + dy, 30, "black", INK, a)
    ae = ep(t, C["03.e"], 0.5)
    regra(c, "eu PERGUNTO · você PAUSA e responde", W / 2, 740, ae, 34, BLUE, w=1100)


# ======================================================================
# verdadeiro ou falso
# ======================================================================

VF = {
    "vf1": dict(a="04", b="05", ep=0, stmt="−3² = 9", why="o − está colado no 3", rg="−3² = −9  ·  só (−3)² = 9"),
    "vf2": dict(a="06", b="07", ep=1, stmt="dízima periódica é irracional", why="ela nunca termina", rg="repete → tem fração → RACIONAL"),
    "vf3": dict(a="08", b="09", ep=1, stmt="todo número com raiz é irracional", why="os famosos são raízes (√2)", rg="√49 = 7 → RACIONAL"),
    "vf4": dict(a="10", b="11", ep=3, stmt="n(A ∪ B) = n(A) + n(B)", why="juntar parece somar", rg="− n(A ∩ B): o meio entrou 2×"),
    "vf5": dict(a="12", b="13", ep=2, stmt="[−∞, 5] está certo", why="o outro lado está fechado", rg="]−∞, 5]: infinito SEMPRE aberto"),
    "vf6": dict(a="14", b="15", ep=3, stmt="\"apenas A\" = círculo A inteiro", why="o número está pronto no enunciado", rg="apenas = SEM as interseções"),
}


def lembrete(c, t, C, nome, a):
    """lado esquerdo: o conceito relembrado com a analogia do episódio"""
    if a <= 0:
        return
    card(c, 160, 260, 600, 560, a)
    text(c, "RELEMBRE", 460, 320, 26, "black", BLUE, a)
    if nome == "vf1":
        E1.fila(c, 250, 350, a, 1, w=420, dy=66, titulo=False)
        text(c, "a potência vem antes do −", 460, 690, 26, "black", PURPLE, a)
    elif nome in ("vf2", "vf3"):
        E2.bonecas(c, 1e9, 470, 530, 0.42, dict(N=0, Z=0, Q=0, I=0, R=0), ex=dict(Q=[(0, "1/3")], I=[(0, "√2")]))
        if nome == "vf2":
            text(c, "acaba? repete? nem/nem?", 460, 730, 28, "black", PURPLE, a)
        else:
            fmid(c, "7 × 7 = 49", 460, 730, 40, "black", PURPLE, a)
            text(c, "quadrado perfeito", 460, 780, 24, "black", INK2, a)
    elif nome == "vf4":
        v = E4.Venn2(460, 540, 120, 140)
        v.pinta(c, "m", E4.MEIO, a * (0.5 + 0.5 * math.sin(t * 5)), 0.4)
        v.base(c, a, "noiva", "noivo")
        text(c, "o meio: contado 2×", 460, 740, 28, "black", E4.MEIO, a)
    elif nome == "vf5":
        E3.notacao(c, 460, 470, 80, "2", "5", 1, 0, a, 1.0)
    else:
        v = E4.Venn2(460, 540, 120, 140)
        v.pinta(c, "a", AMBER, a, 0.35)
        v.base(c, a, "A", "B")
        v.num(c, "a", "só A", a, AMBER, 26)
        v.num(c, "m", "os dois", a, E4.MEIO, 22)


def b_vf(nome):
    d = VF[nome]

    def f(c, t, C, B):
        sa, sb = d["a"], d["b"]
        head(c, t, B["start"], "VERDADEIRO OU FALSO?", "PAUSE E RESPONDA", AMBER)
        ep_chip(c, d["ep"], ep(t, B["start"], 0.4))
        lembrete(c, t, C, nome, ep(t, C[sa + ".t"], 0.5))
        card(c, 800, 260, 980, 560)
        aq = ep(t, C[sa + ".q"], 0.5)
        col = mix(INK, RED, ep(t, C[sb + ".r"], 0.4))
        sz = 72 if len(d["stmt"]) < 14 else 46
        apenas_txt(c, d["stmt"], 1290, 420, sz, col, aq, align="center")
        if C[sb + ".r"] > t:
            cronometro(c, 1290, 620, t, C[sa + ".p"] + 0.9, C[sb], aq)
        ar = ep(t, C[sb + ".r"], 0.35)
        if ar > 0:
            strike(c, 1290 - ftext_w(d["stmt"], "black", sz) / 2 - 10, 400, 1290 + ftext_w(d["stmt"], "black", sz) / 2 + 10, 400,
                   ar, RED, ar)
        carimbo_falso(c, 1600, 330, ar)
        aa = ep(t, C[sb + ".a"], 0.4)
        selo_pegadinha(c, 1000, 560, aa)
        ftext(c, d["why"], 1110, 570, 28, "black", INK, aa, align="left")
        regra(c, d["rg"], 1290, 720, ep(t, C[sb + ".b"], 0.5), 34, PURPLE, w=900)
    return f


# ======================================================================
# questões
# ======================================================================

def card_questao(c, t, linhas, y=275):
    card(c, 140, 170, 760, 660)
    pill(c, "QUESTÃO", 170, 210, BLUE, size=22, bounds=(0, 1920))
    for k, (tc, s, col) in enumerate(linhas):
        apenas_txt(c, s, 180, y + k * 42, 28, col, ep(t, tc, 0.4))


Q1_ALTS = [("A", "−72", "17.a", "19.a", "furou a fila"), ("B", "4", "17.b", "19.b", "esqueceu −(−12) = +12"),
           ("C", "12", "17.c", "19.c", "dois erros juntos"), ("D", "28", "17.d", None, ""),
           ("E", "36", "17.e", "19.e", "fez (−2)² = −4")]


def b_q1(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 1 · INÉDITA", "SINAIS E ORDEM", BLUE)
    card_questao(c, t, [(C["16.e1"], "Resultado da empresa (mil R$):", INK2), (C["16.e3"], "Qual é o resultado?", BLUE)])
    fmid(c, "20 − 3 · (−4) − (−2)^2", 520, 380, 44, "black", INK, ep(t, C["16.e2"], 0.5))
    E4.alternativas(c, t, C, 190, 480, 64, Q1_ALTS, ep(t, C["18.r"], 0.5), 34)
    cronometro(c, 1360, 500, t, C["17.p"] + 0.8, C["18"], ep(t, C["17.p"], 0.3))
    ar = ep(t, C["18.t"], 0.5)
    sol_card(c, 940, 170, 840, 660, ar)
    if ar <= 0:
        return
    tq = WT(C, "18", "quatro", 1, C["18.a"])
    td = WT(C, "18", "doze", 1, C["18.b"])
    tc2 = C["18.c"] + 0.6 * (C["18.r"] - C["18.c"])
    states = [dict(t=C["18.t"], s="a:20  b:−  c:3  d:·  e:(−4)  f:−  g:(−2)^2", hl="g", thl=C["18.a"]),
              dict(t=tq, s="a:20  b:−  c:3  d:·  e:(−4)  f:−  h:4", hl="c d e", thl=C["18.b"]),
              dict(t=td, s="a:20  b:−  i:(−12)  f:−  h:4", hl="b i", thl=C["18.c"]),
              dict(t=tc2, s="a:20  j:+  k:12  f:−  h:4", hl="a j k f h", thl=C["18.r"] - 0.5),
              dict(t=C["18.r"], s="l:28")]
    E1.expr(c, t, states, 1360, 380, 50, ar)
    E1.fila(c, 1150, 470, ar, E1.ativo_em(t, [(C["18.a"], 1), (C["18.b"], 2), (C["18.c"], 3)]), w=420, dy=64, titulo=False)
    pill(c, "RESPOSTA: D · 28", 1360, 790, GREEN, size=28, a=ep(t, C["18.r"], 0.5), anchor="center", bounds=(0, 1920))


NUMS = [("√25", "= 5", True, "21.n1"), ("√8", "não é exata", False, "21.n2"), ("0,1212…", "repete", True, "21.n3"),
        ("3,14", "acaba", True, "22.n4"), ("π", "nem/nem", False, "22.n5"), ("√(9/4)", "= 1,5", True, "22.n6")]
Q2_ALTS = [("A", "1", "20.a", "23.a", "raiz e dízima \"irracionais\""), ("B", "2", "20.b", "23.b", "toda raiz \"irracional\""),
           ("C", "3", "20.c", "23.c", "dízima ou 3,14 = π"), ("D", "4", "20.d", None, ""),
           ("E", "5", "20.e", "23.e", "só o π irracional")]


def b_q2(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 2 · INÉDITA", "QUANTOS SÃO RACIONAIS?", BLUE)
    card_questao(c, t, [(C["20.e1"], "Considere os números:", INK2), (C["20.e2"], "Quantos são racionais?", BLUE)])
    for k, (s, why, rac, cue) in enumerate(NUMS):
        x = 260 + (k % 3) * 210
        y = 380 + (k // 3) * 70
        fmid(c, s, x, y, 34, "black", INK, ep(t, C["20.e1"] + 0.6 * k, 0.4))
    E4.alternativas(c, t, C, 190, 560, 54, Q2_ALTS, ep(t, C["22.r"], 0.5), 30)
    cronometro(c, 1360, 500, t, C["20.p"] + 0.8, C["21"], ep(t, C["20.p"], 0.3))
    ar = ep(t, C["21.t"], 0.5)
    sol_card(c, 940, 170, 840, 660, ar)
    if ar <= 0:
        return
    text(c, "acaba? repete? nem/nem?", 1360, 260, 30, "black", PURPLE, ar)
    for k, (s, why, rac, cue) in enumerate(NUMS):
        x = 1100 + (k % 3) * 260
        y = 380 + (k // 3) * 200
        a = ep(t, C[cue], 0.4)
        fmid(c, s, x, y, 48, "black", mix(INK, GREEN if rac else RED, a), ar)
        text(c, why, x, y + 60, 24, "black", INK2, a)
        pill(c, "RACIONAL" if rac else "IRRACIONAL", x, y + 100, GREEN if rac else RED, size=20, a=a, anchor="center",
             bounds=(0, 1920))
    pill(c, "RESPOSTA: D · 4 racionais", 1360, 790, GREEN, size=28, a=ep(t, C["22.r"], 0.5), anchor="center", bounds=(0, 1920))


Q3_ALTS = [("A", "[50, 200]", "24.a", "26.a", "incluiu o 200"), ("B", "]50, 200[", "24.b", "26.b", "\"a partir\" ≠ \"acima\""),
           ("C", "[50, 200[", "24.c", None, ""), ("D", "]50, 200]", "24.d", "26.d", "trocou as pontas"),
           ("E", "[50, +∞]", "24.e", "26.e", "sem limite e ∞ fechado")]


def b_q3(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 3 · INÉDITA", "O DESCONTO DO APLICATIVO", BLUE)
    card_questao(c, t, [(C["24.e1"], "Desconto em compras", INK), (C["24.e1"] + 1.0, "A PARTIR DE R$ 50", BLUE),
                        (C["24.e1"] + 2.0, "e ABAIXO DE R$ 200.", BLUE), (C["24.e2"], "Qual intervalo?", INK2)])
    E4.alternativas(c, t, C, 190, 480, 64, Q3_ALTS, ep(t, C["25.r"], 0.5), 27)
    cronometro(c, 1360, 500, t, C["24.p"] + 0.8, C["25"], ep(t, C["24.p"], 0.3))
    ar = ep(t, C["25.t"], 0.5)
    sol_card(c, 940, 170, 840, 660, ar)
    if ar <= 0:
        return
    hugL = ep(t, C["25.t"] + 0.6, 0.7)
    hugR = 0
    E3.notacao(c, 1360, 340, 80, "50", "200", hugL, hugR, ar, ep(t, C["25.a"] + 0.6, 0.4))
    r = E3.RetaI(1040, 1680, 560, 0, 250, [(0, "0"), (50, "50"), (100, "100"), (150, "150"), (200, "200"), (250, "250")])
    r.base(c, ar)
    r.faixa(c, 50, 200, ar, ease_io(prog(t, C["25.t"] + 0.3, 0.8)))
    r.bola(c, 50, hugL, ar)
    r.bola(c, 200, 0, ar * ep(t, C["25.a"], 0.4))
    text(c, "a partir de 50: ENTRA", 1200, 680, 26, "black", GREEN, ep(t, C["25.t"] + 0.6, 0.4))
    text(c, "abaixo de 200: FORA", 1520, 680, 26, "black", RED, ep(t, C["25.a"], 0.4))
    pill(c, "RESPOSTA: C", 1360, 790, GREEN, size=28, a=ep(t, C["25.r"], 0.5), anchor="center", bounds=(0, 1920))


Q4_ALTS = [("A", "20", "27.a", "29.a", "esqueceu os 60 de fora"), ("B", "60", "27.b", "29.b", "copiou o \"nenhum\""),
           ("C", "80", "27.c", None, ""), ("D", "100", "27.d", "29.d", "é apenas academia"),
           ("E", "240", "27.e", "29.e", "é a união inteira")]


def b_q4(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 4 · INÉDITA", "ACADEMIA E PISCINA", BLUE)
    card_questao(c, t, [(C["27.e1"], "300 moradores", INK), (C["27.e1"] + 1.2, "180 academia · 140 piscina", INK),
                        (C["27.e1"] + 2.6, "60 não usam nenhuma", INK), (C["27.e2"], "Quantos usam as duas?", BLUE)])
    E4.alternativas(c, t, C, 190, 480, 64, Q4_ALTS, ep(t, C["28.r"], 0.5), 34)
    cronometro(c, 1360, 500, t, C["27.p"] + 0.8, C["28"], ep(t, C["27.p"], 0.3))
    ar = ep(t, C["28.t"], 0.5)
    sol_card(c, 940, 170, 840, 660, ar)
    if ar <= 0:
        return
    v = E4.Venn2(1360, 560, 140, 160, rect_pad=50)
    v.pinta(c, "f", E4.FORA, ep(t, C["28.a"], 0.4), 0.35)
    v.pinta(c, "U", BLUE, ep(t, C["28.b"], 0.4) * (1 - ep(t, C["28.d"], 0.3)), 0.12)
    v.pinta(c, "m", E4.MEIO, ep(t, C["28.d"], 0.4), 0.35)
    v.base(c, ar, "academia", "piscina", universo=True)
    v.num(c, "f", "60", ep(t, C["28.a"], 0.4), E4.FORA, 40)
    fmid(c, "300 − 60 = 240 nos círculos", 1360, 250, 30, "black", INK, ep(t, C["28.b"], 0.4))
    fmid(c, "180 + 140 = 320 → 320 − 240 = 80", 1360, 300, 30, "black", E4.MEIO, ep(t, C["28.c"], 0.4))
    v.num(c, "m", "80", ep(t, C["28.d"] + 0.4, 0.4), E4.MEIO, 46)
    pill(c, "RESPOSTA: C · 80", 1360, 795, GREEN, size=28, a=ep(t, C["28.r"], 0.5), anchor="center", bounds=(0, 1920))


Q5_ALTS = [("A", "11", "31.a", "34.a", "de fora para dentro"), ("B", "14", "31.b", None, ""),
           ("C", "17", "31.c", "34.c", "descontou só um par"), ("D", "22", "31.d", "34.d", "descontou só o miolo"),
           ("E", "25", "31.e", "34.e", "ignorou o apenas")]


def b_q5(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 5 · INÉDITA", "TRÊS MATÉRIAS E O \"APENAS\"", AMBER)
    card_questao(c, t, [(C["30.e1"], "50 alunos", INK), (C["30.e1"] + 1.2, "Mat 25 · Fís 20 · Quím 15", INK),
                        (C["30.e2"], "M e F 8 · M e Q 6 · F e Q 5", INK), (C["30.e2"] + 3.0, "os três: 3", INK),
                        (C["30.e3"], "Quantos gostam apenas de Mat?", BLUE)], y=270)
    E4.alternativas(c, t, C, 190, 520, 60, Q5_ALTS, ep(t, C["32.r"], 0.5), 32)
    cronometro(c, 1360, 500, t, C["31.p"] + 0.8, C["32"], ep(t, C["31.p"], 0.3))
    ar = ep(t, C["32.t"], 0.5)
    sol_card(c, 940, 170, 840, 660, ar)
    if ar <= 0:
        return
    v = E4.Venn3(1360, 505, 138)
    passos = [("m", "32.m", "3", E4.MEIO, "32.p1"), ("fv", "32.p1", "5", AMBER, "32.p2"), ("fn", "32.p2", "3", AMBER, "32.s1"),
              ("f", "32.s1", "14", AMBER, "32.r"), ("vn", "33.a", "2", AMBER, None), ("v", "33.a", "10", E4.CB, None),
              ("n", "33.a", "7", E4.CC, None)]
    for k, cue, s, col, nx in passos:
        v.pinta(c, k, col, ep(t, C[cue], 0.4), 0.45 if k == "f" else 0.30)
    v.pinta(c, "fora", E4.FORA, ep(t, C["33.b"], 0.4), 0.35)
    v.base(c, ar, ("M", "F", "Q"), universo=True)
    for k, cue, s, col, nx in passos:
        tc = C[cue] + (0.75 * (C[nx] - C[cue]) if nx else 0.8 + 0.6 * ["vn", "v", "n"].index(k))
        v.num(c, k, s, ep(t, tc, 0.4), INK, 40)
    v.num(c, "fora", "6", ep(t, C["33.b"] + 1.2, 0.4), E4.FORA, 40)
    apenas_txt(c, "apenas Mat = 25 − 5 − 3 − 3 = 14", 1360, 222, 28, INK, ep(t, C["32.s1"], 0.4), align="center")
    fmid(c, "soma 44 · nenhum 6 · total 50 ✓", 1360, 803, 30, "black", GREEN, ep(t, C["33.b"], 0.4))


# ======================================================================
# checklist, meta, ponte, CTA
# ======================================================================

CHECK = [("35.a", "Ordem das operações e −3² ≠ (−3)²", 0), ("35.b", "A fila ℕ ⊂ ℤ ⊂ ℚ ⊂ ℝ e onde ficam os irracionais", 1),
         ("36.c", "Classifico qualquer número pelo decimal", 1), ("36.d", "Reconheço raiz exata (quadrados perfeitos)", 1),
         ("36.e", "Leio intervalos · o infinito é sempre aberto", 2), ("36.f", "Venn de 2 e 3 grupos, de dentro para fora", 3),
         ("36.g", "Diferença entre \"A\" e \"apenas A\"", 3)]


def b_checklist(c, t, C, B):
    head(c, t, B["start"], "CHECKLIST DE DOMÍNIO", "SÓ O QUE VOCÊ EXPLICARIA EM VOZ ALTA", GREEN)
    card(c, *CARD_R)
    lig = ep(t, C["37.t"], 0.5)
    for k, (cue, s, epk) in enumerate(CHECK):
        a, dy = rise(t, C[cue])
        y = 220 + k * 82 + dy
        rrect(c, 200, y - 24, 44, 44, 10, "#FFFFFF", a, stroke=3, stroke_color=INK2)
        apenas_txt(c, s, 270, y + 10, 32, INK, a)
        if lig > 0:
            ak = a * ep(t, C["37." + "abcd"[epk]], 0.4)
            icone_ep(c, epk, 1560, y - 2, ak, 0.28)
            text(c, f"ep. {epk + 1}", 1640, y + 10, 26, "black", PURPLE, ak, align="left")


def b_meta(c, t, C, B):
    head(c, t, B["start"], "QUANDO O ASSUNTO ESTÁ DOMINADO?", "A META", GREEN)
    card(c, *CARD_R)
    aa = ep(t, C["38.a"], 0.5)
    fmid(c, "30 questões", 560, 330, 70, "black", INK, aa)
    fmid(c, "≥ 21 acertos", 1360, 330, 70, "black", GREEN, aa)
    x0, x1, y = 300, 1620, 470
    rrect(c, x0, y, x1 - x0, 40, 20, LINE, aa)
    pr = ease_io(prog(t, C["38.a"] + 0.6, 1.4)) * 0.7
    rrect(c, x0, y, (x1 - x0) * pr, 40, 20, GREEN, aa)
    line(c, x0 + (x1 - x0) * 0.7, y - 20, x0 + (x1 - x0) * 0.7, y + 60, INK, aa, 4)
    text(c, "70%", x0 + (x1 - x0) * 0.7, y + 100, 34, "black", INK, aa)
    regra(c, "teoria assistida não é conteúdo dominado", W / 2, 660, ep(t, C["38.b"], 0.5), 32, AMBER, w=1100)
    text(c, "só a questão prova isso", W / 2, 790, 40, "black", GREEN, ep(t, C["38.c"], 0.5))


def b_ponte(c, t, C, B):
    head(c, t, B["start"], "PRIMEIRO ASSUNTO: CONCLUÍDO", "PRÓXIMO ASSUNTO", PURPLE)
    card(c, *CARD_R)
    for k in range(4):
        icone_ep(c, k, 340 + k * 120, 260, ep(t, C["39.t"] + 0.2 * k, 0.4), 0.45)
        check_icon(c, 380 + k * 120, 300, 16, ep(t, C["39.t"] + 0.2 * k + 0.3, 0.4), GREEN)
    aa = ep(t, C["39.a"], 0.5)
    tag(c, "DIVISIBILIDADE · PRIMOS · MMC · MDC", W / 2, 470, PURPLE, aa, 40)
    ab = ep(t, C["39.b"], 0.5)
    for k, s in enumerate(("frações", "potências", "notação científica")):
        pill(c, s + ": série própria", 480 + k * 480, 680, BLUE, size=26, a=ab * ep(t, C["39.b"] + 0.3 * k, 0.4), anchor="center")


def b_cta(c, t, C, B):
    cta(c, t, C["40.like"], C["40.sub"], C["40.bell"], C["40.com"], C["40.bye"], "Quantas das 5 questões você acertou?")


BLOCKS = dict(hook=b_hook, como_cai=b_como_cai, indice=b_indice,
              vf1=b_vf("vf1"), vf2=b_vf("vf2"), vf3=b_vf("vf3"), vf4=b_vf("vf4"), vf5=b_vf("vf5"), vf6=b_vf("vf6"),
              q1=b_q1, q2=b_q2, q3=b_q3, q4=b_q4, q5=b_q5, checklist=b_checklist, meta=b_meta, ponte=b_ponte, cta=b_cta)
