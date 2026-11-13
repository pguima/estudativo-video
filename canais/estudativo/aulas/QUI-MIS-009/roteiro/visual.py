"""Visual — Estudativo · QUI-MIS-009: praticando, escolher o método de separação (aula de prática).

Segue a LINGUAGEM VISUAL DA QUÍMICA (cabeçalho de QUI-MIS-001/roteiro/visual.py) e as convenções da separação de misturas
(QUI-MIS-006 a 008). Nesta aula:
- COMPONENTE = ficha redonda (ficha) com o desenho do material e o nome embaixo: areia, sal, ferro, água, óleo, serragem,
  álcool. Quando sai da mistura, a ficha ganha um selo verde.
- SEQUÊNCIA = fluxo da esquerda para a direita (fluxo): bolinha com o número do passo, o método em cima, o que separa
  embaixo, seta entre os passos. A ordem da estratégia (seco → água → sólido do líquido → fogo) tem um ícone por etapa.
Peças candidatas ao kit: ficha (componente de mistura), fluxo (sequência de passos).
Todo instante vem de C[...] (marcadores do roteiro)."""
import math
import random

import editorial as E
import quimica as Q
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Química", "Matéria e Misturas")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_QUI-MIS-009_praticando_metodos_separacao.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("estrategia", "q1", "q2", "q3", "q4", "fim"))
BR = "#FFFFFF"
AREIA, OLEO = "#C99A5B", "#E8B23A"
ETAPA = {"ímã": 1, "peneira": 1, "ventilação": 1, "água": 2, "dissolução": 2, "flotação": 3, "filtração": 3, "funil": 3,
         "decantação": 3, "evaporação": 4, "destilação simples": 4, "destilação fracionada": 4}
SEQ = {1: ["ímã", "água", "filtração", "evaporação"], 2: ["filtração", "funil"], 3: ["água", "flotação", "filtração", "evaporação"],
       4: ["destilação fracionada"]}
for q, seq in SEQ.items():  # toda sequência respeita a estratégia: seco → água → sólido do líquido → fogo
    assert [ETAPA[m] for m in seq] == sorted(ETAPA[m] for m in seq), q
PE = {"álcool": 78, "água": 100}
assert PE["álcool"] < PE["água"]


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def pilula_em(c, t, t0, s, cx, cy, size, fundo=None, est="g", cor=BR):
    E.foco(c, t, t0, 0.4, lambda a: E.pilula(c, s, cx, cy, size, est, fundo=fundo, a=a, cor=cor))


def riscado(c, t, t0, s, x, y, size=56):
    E.foco(c, t, t0, 0.4, lambda a: E.escreve(c, s, x, y, size, "i", ERRADO, a))
    if t >= t0 + 0.8:
        E.risco(c, x - 10, y + 14, x + E.larg(s, "i", size) + 10, y - size * 0.6, t, t0 + 0.8, largura=8)


def desenho(c, tipo, cx, cy, s, a=1.0):
    """o material dentro da ficha"""
    rnd = random.Random(sum(map(ord, tipo)))
    if tipo == "areia":
        for _ in range(26):
            c.drawCircle(cx + (rnd.random() - 0.5) * s * 1.1, cy + (rnd.random() - 0.5) * s * 1.1, 6 + 4 * rnd.random(), M.paint(AREIA if rnd.random() < 0.6 else "#E2C08A", a))
    elif tipo == "sal":
        for _ in range(10):
            x, y = cx + (rnd.random() - 0.5) * s, cy + (rnd.random() - 0.5) * s
            c.drawRect(skia.Rect.MakeXYWH(x - 11, y - 11, 22, 22), M.paint(BR, a)); c.drawRect(skia.Rect.MakeXYWH(x - 11, y - 11, 22, 22), M.paint(CINZA, a, stroke=2))
    elif tipo == "ferro":
        for _ in range(22):
            x, y, ang = cx + (rnd.random() - 0.5) * s * 1.1, cy + (rnd.random() - 0.5) * s * 1.1, rnd.random() * math.pi
            M.line(c, x - 12 * math.cos(ang), y - 12 * math.sin(ang), x + 12 * math.cos(ang), y + 12 * math.sin(ang), "#3A3B40", a, 5)
    elif tipo == "serragem":
        for _ in range(12):
            c.save(); c.translate(cx + (rnd.random() - 0.5) * s, cy + (rnd.random() - 0.5) * s); c.rotate(rnd.random() * 90)
            c.drawRect(skia.Rect.MakeXYWH(-16, -6, 32, 12), M.paint("#B07A3E", a)); c.restore()
    else:
        cor = {"água": Q.AGUA, "óleo": OLEO, "álcool": "#E9F3F7"}[tipo]
        p = skia.Path(); p.moveTo(cx, cy - s * 0.7)
        p.cubicTo(cx + s * 0.55, cy - s * 0.05, cx + s * 0.5, cy + s * 0.55, cx, cy + s * 0.55)
        p.cubicTo(cx - s * 0.5, cy + s * 0.55, cx - s * 0.55, cy - s * 0.05, cx, cy - s * 0.7)
        c.drawPath(p, M.paint(cor, a)); c.drawPath(p, M.paint(M.mix(cor, "#000000", 0.25), a, stroke=4))


def ficha(c, t, t0, tipo, cx, cy, r=86, tsai=None):
    if t < t0:
        return
    q = ep(t, t0, 0.5)
    k = ease_back(prog(t, t0, 0.5))
    c.drawCircle(cx, cy, r * k, M.paint("#E6EAEE", q))
    c.drawCircle(cx, cy, r * k, M.paint(FIO, q, stroke=4))
    c.save(); pth = skia.Path(); pth.addCircle(cx, cy, r * k - 6); c.clipPath(pth, skia.ClipOp.kIntersect, True)
    desenho(c, tipo, cx, cy, r * 1.1 * k, q)
    c.restore()
    centro(c, tipo, cx, cy + r + 56, 46, "b", TINTA, q)
    if tsai is not None:
        E.foco(c, t, tsai, 0.4, lambda a: E.selo(c, cx + r * 0.75, cy - r * 0.75, 30, True, a))


def fluxo(c, t, passos, tl, x0, y, dx=430, size=50):
    """passos = [(método, o que separa)]; tl = instante de cada passo"""
    for k, ((met, sub), ti) in enumerate(zip(passos, tl)):
        if t < ti:
            continue
        x = x0 + dx * k
        E.foco(c, t, ti, 0.4, lambda a, x=x, k=k: (E.bola(c, x, y, 42, a=a), centro(c, str(k + 1), x, y + 20, 54, "g", E.SOBRE, a)))
        E.frase(c, t, ti + 0.1, [(met, "g", size, COR)], x - 42, y + 110)
        E.foco(c, t, ti + 0.4, 0.4, lambda a, x=x, sub=sub: E.escreve(c, sub, x - 42, y + 170, 40, "i", TINTA2, a))
        if k:
            p = ep(t, ti - 0.1, 0.4)
            M.arrow(c, x - dx + 60, y, x - 60, y, TINTA2, p, 5, 18, ease_io(prog(t, ti - 0.1, 0.4)))


def titulo_q(c, t, t0, n):
    E.frase(c, t, t0, [("questão", "i", 70, TINTA2), (str(n), "g", 80, COR)], XE, 170, passo=0.12)


def componentes(c, t, itens, y=440, x0=None, r=86):
    """itens = [(tipo, instante, instante em que sai)]"""
    n = len(itens)
    x0 = x0 if x0 is not None else W / 2 - (n - 1) * 150
    for k, (tipo, ti, ts) in enumerate(itens):
        ficha(c, t, ti, tipo, x0 + 300 * k, y, r, ts)


def pausa(c, t, C, k, texto):
    E.frase(c, t, C[k], ps(texto, "i", 56, TINTA2), XE, 290, passo=0.08)
    E.relogio(c, t, C[k + ".a"], cx=W / 2, cy=600, r=200)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def um():
        for k, tipo in enumerate(("areia", "sal", "ferro")):
            ficha(c, t, C["s01.a"] + 0.3 * k, tipo, 1150 + 260 * k, 420, 100)
        E.frase(c, t, C["s01.a"], [("três", "g", 90, COR), ("componentes", "g", 90)], XE, 300, passo=0.14)
        E.frase(c, t, C["s01.b"], ps("você conhece os métodos,", "i", 62), XE, 470, passo=0.1)
        E.frase(c, t, C["s01.b"] + 1.4, [("mas", "i", 66), ("a", "i", 66), ("ordem", "g", 66, ERRADO), ("errada", "g", 66, ERRADO), ("estraga", "i", 66), ("tudo", "i", 66)], XE, 570, passo=0.1)
        E.frase(c, t, C["s01.c"], [("4", "g", 120, COR), ("misturas,", "i", 80)], XE, 800, passo=0.12)
        E.frase(c, t, C["s01.c"] + 1.0, ps("e a sequência de cada uma", "i", 62, TINTA2), XE, 900, passo=0.1)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t < C["s02"]:
        return
    E.frase(c, t, C["s02"], ps("você vai precisar de", "i", 80, TINTA2), XE, 260, passo=0.12)
    for k, (key, s) in enumerate((("s02.a", "métodos para sólidos"), ("s02.b", "decantar e filtrar"), ("s02.c", "destilação"))):
        y = 430 + 150 * k
        E.foco(c, t, C[key], 0.4, lambda a, y=y: E.bola(c, XE + 30, y - 24, 22, a=a))
        E.frase(c, t, C[key] + 0.1, [(s, "g", 70)], XE + 90, y)
    pilula_em(c, t, C["s02.c"] + 1.2, "faltou alguma? procure no canal", 1400, 960, 44, TINTA)


# ---------------- estratégia ----------------
def icone_etapa(c, k, cx, cy, a, t):
    if k == 0:  # ímã
        p = skia.Path(); s = 36
        p.moveTo(cx - s, cy + s * 0.8); p.lineTo(cx - s, cy); p.arcTo(skia.Rect.MakeXYWH(cx - s, cy - s, 2 * s, 2 * s), 180, 180, False); p.lineTo(cx + s, cy + s * 0.8)
        c.drawPath(p, M.paint("#D93A32", a, stroke=22))
    elif k == 1:  # água
        desenho(c, "água", cx, cy, 60, a)
    elif k == 2:  # filtro
        pth = skia.Path(); pth.moveTo(cx - 50, cy - 40); pth.lineTo(cx + 50, cy - 40); pth.lineTo(cx, cy + 40); pth.close()
        c.drawPath(pth, M.paint("#F7F3EA", a)); c.drawPath(pth, M.paint(Q.VIDRO, a, stroke=5))
    else:  # fogo
        for j, (cor, f) in enumerate((("#F28C28", 1.0), ("#FFC21A", 0.6))):
            hh = 70 * f
            p = skia.Path(); p.moveTo(cx, cy + 35 - hh)
            p.cubicTo(cx + 35 * f, cy + 35 - hh * 0.4, cx + 32 * f, cy + 35, cx, cy + 35)
            p.cubicTo(cx - 32 * f, cy + 35, cx - 35 * f, cy + 35 - hh * 0.4, cx, cy + 35 - hh)
            c.drawPath(p, M.paint(cor, a))


def b_estrategia(c, t, C, b):
    E.frase(c, t, C["s03"], ps("uma estratégia que serve para todas", "i", 62, TINTA2), XE, 180, passo=0.1)
    etapas = (("s03.a", "a seco", "ímã, peneira, sopro"), ("s03.b", "água", "dissolver o que dissolve"),
              ("s03.c", "sólido do líquido", "filtro, funil"), ("s03.d", "por último, fogo", "evaporar, destilar"))
    for k, (key, nome, sub) in enumerate(etapas):
        x = 260 + 450 * k
        E.foco(c, t, C[key], 0.5, lambda a, x=x, k=k: (c.drawCircle(x, 420, 110, M.paint(BR, a)), c.drawCircle(x, 420, 110, M.paint(FIO, a, stroke=4)),
                                                      icone_etapa(c, k, x, 420, a, t), E.bola(c, x - 90, 330, 34, a=a), centro(c, str(k + 1), x - 90, 346, 44, "g", BR, a)))
        E.frase(c, t, C[key] + 0.2, [(nome, "g", 50, COR)], x, 620, "center")
        E.foco(c, t, C[key] + 0.5, 0.4, lambda a, x=x, sub=sub: centro(c, sub, x, 680, 40, "i", TINTA2, a))
        if k:
            M.arrow(c, x - 300, 420, x - 140, 420, TINTA2, ep(t, C[key], 0.4), 5, 18)
    E.frase(c, t, C["s04.a"], ps("a água estraga o seco: areia molhada gruda no ferro", "i", 50), XE, 860, passo=0.06)
    E.frase(c, t, C["s04.b"], ps("o fogo gasta energia: só para o que está dissolvido", "i", 50), XE, 960, passo=0.06)


# ---------------- Q1 ----------------
def b_q1(c, t, C, b):
    titulo_q(c, t, C["s05.a"], 1)
    if t < C["s06"]:
        componentes(c, t, [("areia", C["s05.b"], None), ("sal", C["s05.b"] + 0.4, None), ("ferro", C["s05.b"] + 0.8, None)])
        E.frase(c, t, C["s05.c"], ps("que métodos, e em que ordem?", "i", 64), W / 2, 800, "center", 0.1)
        return
    if t < C["s07"]:
        pausa(c, t, C, "s06", "areia, sal e limalha de ferro: a sequência?")
        return
    componentes(c, t, [("areia", C["s07"], C["s08.a"] + 0.6), ("sal", C["s07"], C["s08.b"] + 0.6), ("ferro", C["s07"], C["s07.b"])], y=330, r=70)
    passos = [("ímã", "tira o ferro"), ("água", "dissolve o sal"), ("filtro", "a areia fica"), ("evaporar", "o sal fica")]
    fluxo(c, t, passos, [C["s07.a"], C["s07.d"], C["s08.a"], C["s08.b"]], 260, 620)
    E.foco(c, t, C["s08.c"], 0.4, lambda a: E.escreve(c, "quer a água também? destilação simples no lugar", XE, 930, 44, "b", TINTA2, a))
    riscado(c, t, C["s08.d"], "água primeiro: ferro molhado na areia", XE, 1030, 48)


# ---------------- Q2 ----------------
def b_q2(c, t, C, b):
    titulo_q(c, t, C["s09.a"], 2)
    if t < C["s10"]:
        componentes(c, t, [("água", C["s09.b"], None), ("óleo", C["s09.b"] + 0.4, None), ("areia", C["s09.b"] + 0.8, None)])
        E.frase(c, t, C["s09.c"], ps("monte a sequência", "i", 64), W / 2, 800, "center", 0.1)
        return
    if t < C["s11"]:
        pausa(c, t, C, "s10", "água, óleo e areia: a sequência?")
        return
    componentes(c, t, [("água", C["s11"], C["s11.f"]), ("óleo", C["s11"], C["s11.f"] + 0.6), ("areia", C["s11"], C["s11.c"])], y=330, r=70)
    passos = [("filtração", "a areia fica no filtro"), ("funil de decantação", "sai a água, o óleo fica")]
    fluxo(c, t, passos, [C["s11.b"], C["s11.e"]], 460, 620, dx=620)
    E.foco(c, t, C["s11.a"], 0.4, lambda a: E.escreve(c, "o único sólido: comece por ele", XE, 1000, 50, "i", TINTA2, a))


# ---------------- Q3 ----------------
def b_q3(c, t, C, b):
    titulo_q(c, t, C["s12.a"], 3)
    if t < C["s13"]:
        componentes(c, t, [("serragem", C["s12.b"], None), ("areia", C["s12.b"] + 0.4, None), ("sal", C["s12.b"] + 0.8, None)])
        E.frase(c, t, C["s12.c"], ps("e agora?", "i", 70), W / 2, 800, "center", 0.1)
        return
    if t < C["s14"]:
        pausa(c, t, C, "s13", "serragem, areia e sal: a sequência?")
        return
    componentes(c, t, [("serragem", C["s14"], C["s15.a"] + 0.5), ("areia", C["s14"], C["s15.b"] + 0.5), ("sal", C["s14"], C["s15.c"] + 0.5)], y=330, r=70)
    E.foco(c, t, C["s14.a"], 0.4, lambda a: E.escreve(c, "a seco, daria para soprar; mas a água resolve duas coisas", XE, 520, 44, "i", TINTA2, a))
    passos = [("água", "boia, afunda, dissolve"), ("flotação", "tira a serragem"), ("filtração", "a areia fica"), ("evaporar", "o sal fica")]
    fluxo(c, t, passos, [C["s14.b"], C["s15.a"], C["s15.b"], C["s15.c"]], 260, 660)
    pilula_em(c, t, C["s15.d"], "3 componentes, 3 passos depois da água", W / 2, 1010, 44, E.COR)


# ---------------- Q4 ----------------
def b_q4(c, t, C, b):
    titulo_q(c, t, C["s16.a"], 4)
    if t < C["s17"]:
        componentes(c, t, [("água", C["s16.b"], None), ("álcool", C["s16.b"] + 0.4, None), ("sal", C["s16.b"] + 0.8, None)])
        pilula_em(c, t, C["s16.b"] + 1.4, "tudo homogêneo", W / 2, 680, 48, TINTA)
        E.frase(c, t, C["s16.c"], ps("qual é a sequência?", "i", 64), W / 2, 820, "center", 0.1)
        return
    if t < C["s18"]:
        pausa(c, t, C, "s17", "água, álcool e sal dissolvido: a sequência?")
        return
    componentes(c, t, [("álcool", C["s18"], C["s18.c"]), ("água", C["s18"], C["s18.d"]), ("sal", C["s18"], C["s18.e"])], y=330, r=70)
    riscado(c, t, C["s18.a"], "filtro: não adianta", XE, 560, 52)
    pilula_em(c, t, C["s18.b"], "uma destilação fracionada", W / 2, 640, 56, E.COR)
    for k, (key, txt) in enumerate((("s18.c", "1º sai o álcool, ~78 °C"), ("s18.d", "2º sai a água, 100 °C"), ("s18.e", "o sal fica no balão"))):
        E.foco(c, t, C[key], 0.4, lambda a, k=k, txt=txt: E.escreve(c, txt, 300 + 520 * k, 790, 46, "b", TINTA, a))
    E.foco(c, t, C["s19.a"], 0.4, lambda a: E.escreve(c, "o detalhe que a prova adora:", XE, 910, 46, "i", TINTA2, a))
    E.frase(c, t, C["s19.a"] + 0.8, [("o", "i", 56), ("álcool", "g", 56), ("sai", "i", 56), ("a", "i", 56), ("96%", "g", 56, COR)], 900, 910, passo=0.1)
    pilula_em(c, t, C["s19.b"], "álcool e água: mistura azeotrópica", W / 2, 1020, 44, TINTA, "b")


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s20"], [("resumindo", "i", 92, COR)], W / 2, 180, "center")
        etapas = (("s20.a", "a seco"), ("s20.b", "água"), ("s20.c", "sólido do líquido"), ("s20.d", "fogo"))
        for k, (key, nome) in enumerate(etapas):
            x = 260 + 450 * k
            E.foco(c, t, C[key], 0.5, lambda a, x=x, k=k: (c.drawCircle(x, 480, 110, M.paint(BR, a)), c.drawCircle(x, 480, 110, M.paint(FIO, a, stroke=4)),
                                                          icone_etapa(c, k, x, 480, a, t)))
            E.frase(c, t, C[key] + 0.2, [(f"{k + 1}", "g", 60, COR), (nome, "g", 52)], x, 700, "center", 0.1)
            if k:
                M.arrow(c, x - 300, 480, x - 140, 480, TINTA2, ep(t, C[key], 0.4), 5, 18)
    E.saida(c, t, C["s21"] - 0.1, resumo)
    if t < C["s21"]:
        return
    E.frase(c, t, C["s21"], ps("fim da trilha de substâncias e misturas", "i", 60, TINTA2), XE, 200, passo=0.08)
    E.frase(c, t, C["s21.a"], [("próxima", "i", 80), ("trilha:", "i", 80)], XE, 330, passo=0.12)
    E.frase(c, t, C["s21.b"], [("o", "i", 100), ("átomo", "g", 110, COR)], XE, 470, passo=0.12)
    E.frase(c, t, C["s21.b"] + 0.8, ps("Dalton e Thomson", "i", 76), XE, 580, passo=0.12)
    E.foco(c, t, C["s21.b"] + 1.0, 0.5, lambda a: (E.bola(c, 560, 800, 120, "#9AA0A8", a)))
    E.foco(c, t, C["s21.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1560, 420, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s21.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1860, 1690, p), lerp(720, 445, p), ep(t, C["s21.c"] + 0.2, 0.4))
    E.frase(c, t, C["s21.d"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1560, 990, "center")


BLOCKS = dict(gancho=b_gancho, estrategia=b_estrategia, q1=b_q1, q2=b_q2, q3=b_q3, q4=b_q4, fim=b_fim)
