"""Visual — Estudativo · FIS-ELE-026: praticando leis de Kirchhoff (aula de prática, quatro questões). Última aula da trilha.

Segue a LINGUAGEM VISUAL DA FÍSICA (FIS-CIN-001), a da ELETRICIDADE (FIS-ELE-001) e a do módulo LEIS DE KIRCHHOFF
(FIS-ELE-024: `no_correntes`, `percurso`, termo que soma em laranja e que subtrai em azul; FIS-ELE-025: `circ3`, `seta_i`,
correntes i₁, i₂, i₃ com índice Unicode). O formato da prática é o da FIS-ELE-023 (`enunciado`, `passos`): pílula "questão N",
dados à esquerda, desenho à direita que dá lugar ao relógio no "pause e tente", passos da resposta descendo um por cue.
Corrente com sinal de menos: a seta do chute fica cinza tracejada e a seta real (invertida) entra em azul (F.NEG).
Todo instante vem de C[...] (marcadores do roteiro), para acompanhar a voz real quando ela chegar."""
import math

import editorial as E
import fisica as F
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Física", "Eletricidade")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_FIS-ELE-026_praticando_leis_de_kirchhoff.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("metodo", "q1", "q2", "q3", "q4", "fim"))
BR = "#FFFFFF"
NEG = F.NEG

# todas as contas da aula
assert 3 + 4 == 5 + 2
assert (12 + 6 - 3) / 5 == 3
i1, i2, i3 = 1, 2, 3
assert i3 == i1 + i2 and 8 == 2 * i1 + 2 * i3 and 14 == 4 * i2 + 2 * i3
assert 8 == 4 * i1 + 2 * i2 and 14 == 2 * i1 + 6 * i2 and i2 == 4 - 2 * i1 and 2 * i1 + 6 * (4 - 2 * i1) == 24 - 10 * i1 == 14
assert (8 - 6) / 2 + (14 - 6) / 4 == 6 / 2  # atalho: U = 6 V
U = 8
assert 4 * (12 - U) + 4 * (6 - U) == U and 72 - 8 * U == U and (12 - U) / 1 == 4 and (6 - U) / 1 == -2 and U / 4 == 2 and 4 + (-2) == 2
assert 6 * 2 == 12 and 1 * 2 ** 2 == 4 and U * 2 == 12 + 4


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças da trilha (copiadas da FIS-CIN-001 / FIS-ELE-001 / FIS-ELE-019) ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def troca(c, t, itens, fn):
    """um de cada vez: itens = [(instante, arg)], cada um sai quando o próximo chega; fn(arg, a) desenha"""
    for k, (ti, s) in enumerate(itens):
        fim = itens[k + 1][0] - 0.1 if k + 1 < len(itens) else 1e9
        if t >= ti - 0.01:
            E.saida(c, t, fim, lambda s=s, ti=ti: E.foco(c, t, ti, 0.45, lambda a: fn(s, a)), d=0.25)


def bola_txt(c, t, t0, s, cx, cy, r_, size, cor=None):
    """resposta na esfera: "20 m/s" com a unidade menor"""
    v, _, u = s.partition(" ")
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r_ * ease_back(prog(t, t0, 0.5)), cor, a),
                                     F.medida(c, v, u, cx, cy + size * 0.36, size, E.SOBRE, a, "center", cor_u=E.SOBRE)))


def lembrete(c, t, C, cena, itens):
    """lembrete de n coisas: itens = [(cue, linha fina, linha forte)]; a linha forte aceita fórmula"""
    n = len(itens)
    E.frase(c, t, C[cena] + 0.2, ps("você precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C[cena + ".a"], 0.5, lambda a: E.escreve(c, str(n), XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C[cena + ".a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 820, 1000
    hb, gap = (230, 290) if n == 2 else (200, 225)
    y0 = 230 if n == 2 else 170
    for k, (cue, l1, l2) in enumerate(itens):
        y = y0 + k * gap
        p = ep(t, C[cue], 0.5)
        E.caixa_pontilhada(c, x, y, w, hb, p, prog_=p)
        E.frase(c, t, C[cue] + 0.1, [(l1, "i", 56)], x + 44, y + hb * 0.4)
        E.formula_em(c, t, C[cue] + 0.3, l2, x + 44, y + hb * 0.8, 62, "g", COR)
    E.frase(c, t, lerp(C[itens[-1][0]], C[cena + ".end"], 0.6), ps("faltou alguma?", "i", 52, COR) + ps("procure no canal", "i", 52),
            820, 1000 if n == 3 else 920, "left", 0.12)


def promessa(c, t, C, cena, itens):
    """promessa do gancho: a órbita da Física à direita e os itens numerados. itens = [(cue, texto, atraso)]"""
    tb = C[cena + ".a"] + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1520, 560, 300 * ease_back(prog(t, tb, 0.8)), giro=12 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, C[cena + ".a"], ps("até o fim da aula", "i", 88), XE, 280, passo=0.14)
    for k, (cue, s, dt) in enumerate(itens):
        y = 460 + k * 170
        E.foco(c, t, C[cue] + dt, 0.5, lambda a, k=k, y=y: (E.bola(c, XE + 40, y - 26, 38, a=a), centro(c, str(k + 1), XE + 40, y - 4, 48, "g", BR, a)))
        E.frase(c, t, C[cue] + dt + 0.1, [(s, "g", 76, COR if k == 0 else TINTA)], XE + 110, y)


def inscreva(c, t, tc, td, x=1520, y=420):
    E.foco(c, t, tc, 0.5, lambda a: E.pilula(c, "Inscreva-se", x, y, 76, estilo="g", a=a))
    p = ease_io(prog(t, tc + 0.3, 0.8))
    E.cursor(c, lerp(x + 300, x + 130, p), lerp(y + 300, y + 25, p), ep(t, tc + 0.2, 0.4))
    E.frase(c, t, td, [("bons", "i", 104), ("estudos!", "i", 104, COR)], x + 50, 990, "center")


def resumo(c, t, C, cena, itens):
    """resumo numerado: itens = [(cue, partes)]"""
    E.frase(c, t, C[cena], [("resumindo", "i", 92, COR)], W / 2, 180, "center")
    for k, (cue, partes) in enumerate(itens):
        y = 360 + k * 190
        E.foco(c, t, C[cue], 0.5, lambda a, k=k, y=y: (E.bola(c, 300, y - 24, 50, a=a), centro(c, str(k + 1), 300, y - 2, 58, "g", BR, a)))
        E.frase(c, t, C[cue] + 0.1, partes, 400, y, passo=0.12)


def caixa_tracejada(c, x, y, w, h, a, cor=TINTA2):
    if a <= 0:
        return
    pt = M.paint(cor, a, stroke=4)
    pt.setPathEffect(skia.DashPathEffect.Make(E.TRACO, 0))
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 30, 30), pt)


def gerador_real(c, t, t0, A, B, rot_e="ε", rot_r="r", tr=None, calor=None, polos=True):
    """gerador real na horizontal, de A (polo −) a B (polo +): pilha (fem) e resistência interna numa caixa tracejada.
    tr = instante da resistência interna (senão, junto); calor = instante em que r acende (perda que vira calor)"""
    tr = t0 if tr is None else tr
    xm = lerp(A[0], B[0], 0.45)
    y = A[1]
    E.foco(c, t, t0, 0.5, lambda a: caixa_tracejada(c, A[0] + 40, y - 120, B[0] - A[0] - 80, 240, a))
    F.pilha(c, t, t0, A, (xm, y), rot_e)
    if calor is not None and t >= calor:
        q = ep(t, calor, 0.6)
        g = skia.Paint(AntiAlias=True)
        cx = (xm + B[0]) / 2
        g.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, y), 150, [M.hexc(CALOR, 0.55 * q), M.hexc(CALOR, 0)], [0, 1]))
        c.drawCircle(cx, y, 150, g)
    F.resistor(c, t, tr, (xm, y), B, rot_r, cor=CALOR if calor is not None and t >= calor else None)
    if polos:
        for P, s in ((A, "−"), (B, "+")):
            E.foco(c, t, t0 + 0.3, 0.4, lambda a, P=P, s=s: (F.no(c, P, a), centro(c, s, P[0], P[1] + 80, 60, "g", F.NEG if s == "−" else E.COR, a)))


def paralelo2(c, t, t0, A, B, rot1, rot2, dy=95):
    """dois resistores em paralelo entre A (direita) e B (esquerda), na horizontal"""
    xa, xb, y = A[0], B[0], A[1]
    xi, xf = xa - 90, xb + 90
    F.fio(c, t, t0, [A, (xi, y), (xi, y - dy)])
    F.fio(c, t, t0, [(xi, y), (xi, y + dy)])
    F.fio(c, t, t0, [B, (xf, y), (xf, y - dy)])
    F.fio(c, t, t0, [(xf, y), (xf, y + dy)])
    F.resistor(c, t, t0 + 0.3, (xi, y - dy), (xf, y - dy), rot1, lado=-1)
    F.resistor(c, t, t0 + 0.4, (xi, y + dy), (xf, y + dy), rot2)
    if t >= t0 + 0.3:
        F.no(c, (xi, y)); F.no(c, (xf, y))


def circuito(c, t, t0, x0, x1, yt, yb, rot_e="ε", rot_r="r", carga="R", tc=None, calor=None, corrente=None, tr=None):
    """a volta padrão: gerador real em cima (− à esquerda, + à direita) e a carga embaixo. carga = rótulo de um resistor ou
    função fn(A, B) que desenha a carga entre A (direita) e B (esquerda). corrente = instante das setinhas (sentido horário)"""
    A, B = (x0 + 110, yt), (x1 - 110, yt)
    F.fio(c, t, t0, [(x0, yb), (x0, yt), A])
    F.fio(c, t, t0, [B, (x1, yt), (x1, yb)])
    gerador_real(c, t, t0, A, B, rot_e, rot_r, tr=tr, calor=calor)
    tc = t0 + 0.3 if tc is None else tc
    if callable(carga):
        carga((x1, yb), (x0, yb))
    else:
        F.resistor(c, t, tc, (x1, yb), (x0, yb), carga)
    if corrente is not None:
        k = 60
        F.corrente(c, t, corrente, [(B[0], yt + k), (x1 - k, yt + k), (x1 - k, yb - k), (x0 + k, yb - k), (x0 + k, yt + k), (A[0], yt + k)],
                   fecha=False, espaco=170)


def tabela(c, t, cols, linhas, x, y, wc, dy=110, size=64, destaque=None, td=None):
    """tabela: cols = cabeçalhos; linhas = [(instante, [células])]; destaque = índice da linha que acende em td"""
    E.foco(c, t, linhas[0][0] - 0.4, 0.4, lambda a: [E.formula(c, s, x + k * wc, y, 50, "b", TINTA2, a) for k, s in enumerate(cols)])
    if t >= linhas[0][0] - 0.4:
        M.line(c, x - 20, y + 26, x + wc * len(cols) - 40, y + 26, TINTA2, ep(t, linhas[0][0] - 0.4, 0.4), 3)
    for j, (ti, cel) in enumerate(linhas):
        yy = y + (j + 1) * dy
        if destaque == j and td is not None and t >= td:
            q = ep(t, td, 0.4)
            M.rrect(c, x - 30, yy - size * 0.95, wc * len(cols) - 10, size * 1.35, 20, E.COR, 0.16 * q)
        for k, s in enumerate(cel):
            E.foco(c, t, ti + 0.25 * k, 0.4, lambda a, s=s, k=k, yy=yy, j=j: E.formula(
                c, s, x + k * wc, yy, size, "g", COR if (destaque == j and td is not None and t >= td) else TINTA, a))


def motor_simb(c, cx, cy, r_, a=1.0):
    """motor: círculo com M"""
    if a <= 0:
        return
    c.drawCircle(cx, cy, r_, M.paint("#FFFFFF", a))
    c.drawCircle(cx, cy, r_, M.paint(TINTA, a, stroke=6))
    centro(c, "M", cx, cy + r_ * 0.36, r_, "g", E.COR, a)


def no_correntes(c, t, P, setas, L=230, size=56):
    """nó em P com setas: setas = [(ângulo em graus, rótulo, chega?, t0, cor)]; ângulo da Física (0 = direita, 90 = cima)"""
    for ang, rot, chega, t0, cor in setas:
        ux, uy = math.cos(math.radians(ang)), -math.sin(math.radians(ang))
        far = (P[0] + ux * L, P[1] + uy * L)
        near = (P[0] + ux * 34, P[1] + uy * 34)
        A, B = (far, near) if chega else (near, far)
        q = ease_out(prog(t, t0, 0.5))
        if q > 0:
            M.line(c, *P, *far, TINTA, q, 6)
            F.seta(c, *A, *B, cor or E.COR, 1.0, 10, None, q)
            E.foco(c, t, t0 + 0.3, 0.4, lambda a, far=far, ux=ux, uy=uy, rot=rot, cor=cor: E._meio(
                c, rot, far[0] + ux * 70 - uy * 0, far[1] + uy * 70, size, "g", cor or COR, a))
    if any(t >= s[3] for s in setas):
        c.drawCircle(*P, 18, M.paint(TINTA, 1.0))


def circ3(c, t, te, td, tm, e1, R1, e2, R2, R3, xs=(1080, 1410, 1740), yt=250, yb=820, escuro=False, nos=True):
    """três ramos entre A (em cima) e B (embaixo): esquerda = e1 + R1, meio = R3, direita = e2 + R2; te/td/tm = instante de cada ramo"""
    x0, x1, x2 = xs
    ym = (yt + yb) / 2 + 40
    t0 = min(te, td, tm)
    F.fio(c, t, t0, [(x0, yt), (x2, yt)], escuro=escuro)
    F.fio(c, t, t0, [(x0, yb), (x2, yb)], escuro=escuro)
    F.pilha(c, t, te, (x0, yb), (x0, ym), e1, escuro=escuro)
    F.resistor(c, t, te + 0.2, (x0, ym), (x0, yt), R1, escuro=escuro)
    F.pilha(c, t, td, (x2, yb), (x2, ym), e2, escuro=escuro, lado=-1)
    F.resistor(c, t, td + 0.2, (x2, ym), (x2, yt), R2, escuro=escuro, lado=-1)
    F.resistor(c, t, tm, (x1, yt), (x1, yb), R3, escuro=escuro)
    if nos and t >= t0 + 0.4:
        F.no(c, (x1, yt), escuro=escuro); F.no(c, (x1, yb), escuro=escuro)


def nomes_nos(c, t, t0, xs=(1080, 1410, 1740), yt=250, yb=820, escuro=False):
    tinta = BR if escuro else TINTA
    E.foco(c, t, t0, 0.4, lambda a: (centro(c, "A", xs[1], yt - 30, 56, "g", tinta, a), centro(c, "B", xs[1], yb + 76, 56, "g", tinta, a)))


def seta_i(c, t, t0, x, y0, y1, nome, lado=1, valor=None, tv=None, cor=None):
    """corrente de um ramo: seta de y0 a y1 ao lado do fio x; o nome (e, a partir de tv, o valor) fica junto da ponta"""
    cor = cor or E.COR
    q = ease_out(prog(t, t0, 0.5))
    if q <= 0:
        return
    xx = x + 60 * lado
    F.seta(c, xx, y0, xx, y1, cor, 1.0, 9, None, q)
    al = "left" if lado > 0 else "right"
    yn = y1 + (50 if y1 < y0 else -10)
    E.foco(c, t, t0 + 0.2, 0.4, lambda a: E.formula(c, nome, xx + 20 * lado, yn, 58, "g", cor, a, al))
    if valor is not None and tv is not None:
        E.foco(c, t, tv, 0.4, lambda a: E.formula(c, valor, xx + 20 * lado, yn + 56, 46, "b", cor, a, al))


def correntes(c, t, ta, tb, tc, xs=(1080, 1410, 1740), yt=250, yb=820, valores=None, tv=None):
    """as três correntes: i₁ sobe pela esquerda, i₂ sobe pela direita, i₃ desce pelo meio"""
    v = valores or (None, None, None)
    seta_i(c, t, ta, xs[0], yb - 120, yt + 160, "i₁", 1, v[0], tv)
    seta_i(c, t, tb, xs[2], yb - 120, yt + 160, "i₂", -1, v[1], tv)
    seta_i(c, t, tc, xs[1], yt + 140, yb - 160, "i₃", -1, v[2], tv)




def enunciado(c, t, C, cena, n, linhas, desenho, tp, resp):
    """questão n: linhas = [(instante, partes)] à esquerda; desenho(a) à direita até tp (pause), depois o relógio; some em resp"""
    E.foco(c, t, C[cena], 0.4, lambda a: E.pilula(c, f"questão {n}", XE + 120, 150, 46, "g", fundo=E.COR, a=a))
    if t >= resp:
        return

    def tudo():
        for k, (ti, partes) in enumerate(linhas):
            E.frase(c, t, ti, partes, XE, 320 + k * 120, passo=0.1)
        if t < tp:
            E.foco(c, t, C[cena] + 0.3, 0.6, desenho)
        else:
            E.relogio(c, t, tp, cx=1500, cy=440, r=190)
    E.saida(c, t, resp - 0.1, tudo)


def passos(c, t, itens, x=XE, y0=320, dy=125, size=66):
    """passos da resposta: itens = [(instante, fórmula, cor)]"""
    for k, (ti, s, cor) in enumerate(itens):
        E.foco(c, t, ti, 0.5, lambda a, s=s, k=k, cor=cor: E.formula(c, s, x, y0 + k * dy, size, "g", cor or TINTA, a))


def ohm(v):
    return f"{v} Ω"


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    for k, (cue, s) in enumerate((("s01.b", "um nó"), ("s01.c", "uma malha"), ("s01.d", "duas malhas"))):
        E.foco(c, t, C[cue], 0.5, lambda a, k=k, s=s: (E.bola(c, 1140 + 0 * k, 300 + k * 170, 50, a=a), centro(c, str(k + 1), 1140, 322 + k * 170, 60, "g", BR, a),
                                                        E.escreve(c, s, 1230, 322 + k * 170, 70, "g", COR if k == 2 else TINTA, a)))
    E.frase(c, t, C["s01.a"], ps("na prova,", "i", 80) + [("Kirchhoff", "g", 80, COR)], XE, 280, passo=0.14)
    E.frase(c, t, C["s01.a"] + 1.2, ps("aparece de três jeitos", "i", 70), XE, 390, passo=0.12)
    E.frase(c, t, C["s01.e"], ps("uma questão de cada", "g", 66), XE, 700, passo=0.12)
    E.frase(c, t, C["s01.f"], ps("+ uma com", "i", 70) + [("surpresa", "g", 66, COR)] + ps("no sinal", "i", 70), XE, 820, passo=0.12)


# ---------------- método ----------------
def b_metodo(c, t, C, b):
    E.frase(c, t, C["s02"], ps("antes, o", "i", 80) + [("método", "g", 80, COR)], XE, 190, passo=0.14)
    itens = (("s02.a", "nome e sentido em cada corrente", None),
             ("s02.b", "nó: o que chega = o que sai", None),
             ("s02.c", "malha: entrou pelo −, + ε;  a favor de i, − R · i", None),
             ("s02.d", "dois nós: a tensão U entre eles", None))
    for k, (cue, s, _) in enumerate(itens):
        y = 360 + k * 160
        E.foco(c, t, C[cue], 0.5, lambda a, k=k, y=y: (E.bola(c, XE + 36, y - 22, 36, a=a), centro(c, str(k + 1), XE + 36, y - 2, 44, "g", BR, a)))
        E.foco(c, t, C[cue] + 0.1, 0.5, lambda a, s=s, y=y, k=k: E.formula(c, s, XE + 100, y, 60, "g", COR if k == 2 else TINTA, a))


# ---------------- questão 1: um nó ----------------
def b_q1(c, t, C, b):
    P = (1450, 560)
    enunciado(c, t, C, "s03", 1, [(C["s03.a"], ps("chegam:", "i", 64) + [("3", "g", 64), ("A", "b", 48, F.UNID), ("e", "i", 64), ("i", "g", 64, COR)]),
                                  (C["s03.b"], ps("saem:", "i", 64) + [("5", "g", 64), ("A", "b", 48, F.UNID), ("e", "i", 64), ("2", "g", 64), ("A", "b", 48, F.UNID)]),
                                  (C["s03.c"], ps("quanto vale", "i", 64) + [("i?", "g", 64, COR)])],
              lambda a: no_correntes(c, 1e9, P, [(150, "3 A", True, 0, None), (210, "i", True, 0, TINTA), (30, "5 A", False, 0, None), (-30, "2 A", False, 0, None)]),
              C["s03.d"], C["s04"])
    if t < C["s04"]:
        return
    no_correntes(c, t, P, [(150, "3 A", True, C["s04"], None), (210, "4 A" if t >= C["s04.d"] else "i", True, C["s04"], CERTO if t >= C["s04.d"] else TINTA),
                           (30, "5 A", False, C["s04"], None), (-30, "2 A", False, C["s04"], None)])
    passos(c, t, [(C["s04.a"], "chega = sai", COR), (C["s04.b"], "3 + i = 5 + 2", None), (C["s04.c"], "3 + i = 7", None)], y0=340, dy=150, size=80)
    bola_txt(c, t, C["s04.d"], "4 A", XE + 200, 840, 95, 68, CERTO)


# ---------------- questão 2: uma malha ----------------
def malha3(c, t, t0, x0, x1, yt, yb):
    """malha com 12 V e 6 V a favor (horário) e 3 V contra; resistências somando 5 Ω"""
    xm = (x0 + x1) / 2
    F.pilha(c, t, t0, (x0, yb), (x0, (yt + yb) / 2), "12 V")
    F.pilha(c, t, t0, (x0, (yt + yb) / 2), (x0, yt), "6 V")
    F.resistor(c, t, t0, (x0, yt), (x1, yt), "2 Ω")
    F.pilha(c, t, t0, (x1, yb), (x1, yt), "3 V", lado=-1)
    F.resistor(c, t, t0, (x1, yb), (x0, yb), "3 Ω")


def b_q2(c, t, C, b):
    x0, x1, yt, yb = 1150, 1700, 280, 820
    enunciado(c, t, C, "s05", 2, [(C["s05.a"], ps("três geradores", "i", 64)),
                                  (C["s05.b"], [("12", "g", 64), ("V", "b", 48, F.UNID), ("e", "i", 64), ("6", "g", 64), ("V", "b", 48, F.UNID)] + ps("num sentido", "i", 64)),
                                  (C["s05.c"], [("3", "g", 64), ("V", "b", 48, F.UNID)] + ps("no outro", "i", 64)),
                                  (C["s05.d"], ps("resistências:", "i", 64) + [("5", "g", 64), ("Ω", "b", 48, F.UNID)]),
                                  (C["s05.e"], ps("corrente?", "g", 66, COR))],
              lambda a: malha3(c, 1e9, 0, x0, x1, yt, yb), C["s05.f"], C["s06"])
    if t < C["s06"]:
        return
    malha3(c, t, C["s06"], x0, x1, yt, yb)
    F.corrente(c, t, C["s06.e"], [(x0 + 60, yb - 60), (x0 + 60, yt + 60), (x1 - 60, yt + 60), (x1 - 60, yb - 60)], espaco=200)
    E.frase(c, t, C["s06.a"], ps("uma malha só:", "i", 66) + [("o", "g", 64), ("atalho", "g", 64, COR)], XE, 320, passo=0.12)
    E.foco(c, t, C["s06.b"], 0.5, lambda a: E.formula(c, "a favor: 12 + 6 = 18", XE, 470, 64, "g", COR, a))
    E.foco(c, t, C["s06.c"], 0.5, lambda a: E.formula(c, "contra: 3", XE, 580, 64, "g", NEG, a))
    E.foco(c, t, C["s06.d"], 0.5, lambda a: E.formula(c, "i = f{18 − 3}{5} = f{15}{5}", XE, 740, 76, "g", TINTA, a))
    bola_txt(c, t, C["s06.e"], "3 A", XE + 700, 720, 90, 66, CERTO)


# ---------------- questão 3: duas malhas ----------------
def b_q3(c, t, C, b):
    xs, yt, yb = (1130, 1430, 1730), 280, 820
    enunciado(c, t, C, "s07", 3, [(C["s07.a"], [("esquerda:", "i", 60), ("8 V e 2 Ω", "g", 60)]),
                                  (C["s07.b"], [("direita:", "i", 60), ("14 V e 4 Ω", "g", 60)]),
                                  (C["s07.c"], [("meio:", "i", 60), ("2 Ω", "g", 60)]),
                                  (C["s07.c"] + 1.0, ps("os dois com o", "i", 60) + [("+", "g", 60, COR)] + ps("para cima", "i", 60)),
                                  (C["s07.d"], ps("monte o sistema", "g", 62, COR))],
              lambda a: circ3(c, 1e9, 0, 0, 0, "8 V", "2 Ω", "14 V", "4 Ω", "2 Ω", xs, yt, yb), C["s07.e"], C["s08"])
    if t < C["s08"]:
        return
    xs2 = (1110, 1410, 1740)
    circ3(c, t, C["s08"], C["s08"], C["s08"], "8 V", "2 Ω", "14 V", "4 Ω", "2 Ω", xs2, 300, 820)
    correntes(c, t, C["s08.a"], C["s08.a"] + 0.4, C["s08.a"] + 0.8, xs2, 300, 820, ("1 A", "2 A", "3 A"), C["s09.f"])

    def s08():
        E.formula_em(c, t, C["s08.b"], "i₃ = i₁ + i₂", XE, 330, 64, "g", TINTA)
        E.formula_em(c, t, C["s08.c"], "8 = 2i₁ + 2i₃", XE, 470, 64, "g", TINTA)
        E.formula_em(c, t, C["s08.d"], "14 = 4i₂ + 2i₃", XE, 610, 64, "g", TINTA)
    E.saida(c, t, C["s09"] - 0.1, s08)
    if t < C["s09"]:
        return
    E.sistema(c, t, C["s09.a"], ["8 = 4i₁ + 2i₂", "14 = 2i₁ + 6i₂"], XE + 30, 330, 62, tl=[C["s09.a"], C["s09.b"]])
    passos(c, t, [(C["s09.c"], "i₂ = 4 − 2i₁", COR), (C["s09.d"], "14 = 24 − 10i₁", None), (C["s09.e"], "10i₁ = 10", None)], y0=580, dy=115, size=60)
    E.foco(c, t, C["s09.f"], 0.5, lambda a: E.formula(c, "i₁ = 1 A   i₂ = 2 A   i₃ = 3 A", XE, 960, 56, "g", CERTO, a))


# ---------------- questão 4: a surpresa no sinal ----------------
def b_q4(c, t, C, b):
    xs, yt, yb = (1130, 1430, 1730), 280, 820
    enunciado(c, t, C, "s10", 4, [(C["s10.a"], [("esquerda:", "i", 60), ("12 V e 1 Ω", "g", 60)]),
                                  (C["s10.b"], [("direita:", "i", 60), ("bateria", "i", 60), ("6 V e 1 Ω", "g", 60)]),
                                  (C["s10.c"], [("meio:", "i", 60), ("4 Ω", "g", 60)]),
                                  (C["s10.d"], ps("a bateria de 6 V", "i", 60)),
                                  (C["s10.d"] + 1.2, ps("fornece ou é carregada?", "g", 60, COR))],
              lambda a: circ3(c, 1e9, 0, 0, 0, "12 V", "1 Ω", "6 V", "1 Ω", "4 Ω", xs, yt, yb), C["s10.e"], C["s11"])
    if t < C["s11"]:
        return
    xs2 = (1110, 1410, 1740)
    circ3(c, t, C["s11"], C["s11"], C["s11"], "12 V", "1 Ω", "6 V", "1 Ω", "4 Ω", xs2, 300, 820)
    nomes_nos(c, t, C["s11"], xs2, 300, 820)
    seta_i(c, t, C["s11"], xs2[0], 700, 460, "i₁", 1, "4 A", C["s12.f"])
    seta_i(c, t, C["s11"], xs2[1], 440, 660, "i₃", -1, "2 A", C["s12.f"])
    real = t >= C["s12.c"]
    if not real:
        seta_i(c, t, C["s11"], xs2[2], 700, 460, "i₂", -1)
    else:
        seta_i(c, t, C["s12.c"], xs2[2], 460, 700, "2 A", -1, None, None, cor=NEG)
    if C["s11"] <= t < C["s12"]:
        E.frase(c, t, C["s11.a"], ps("dois nós:", "i", 64) + [("U", "g", 64, COR)] + ps("entre eles", "i", 64), XE, 320, passo=0.12)
        E.formula_em(c, t, C["s11.b"], "f{12 − U}{1} + f{6 − U}{1} = f{U}{4}", XE, 500, 72, "g", TINTA)
        E.formula_em(c, t, C["s11.c"], "72 − 8U = U", XE, 690, 72, "g", TINTA)
        bola_txt(c, t, C["s11.d"], "8 V", XE + 640, 665, 85, 60)
        E.foco(c, t, C["s11.d"] + 0.2, 0.4, lambda a: E.formula(c, "U =", XE + 470, 688, 60, "g", TINTA, a))
    if C["s12"] <= t < C["s13"]:
        E.formula_em(c, t, C["s12.a"], "i₂ = f{6 − 8}{1} =", XE, 340, 72, "g", TINTA)
        bola_txt(c, t, C["s12.b"], "−2 A", XE + 640, 315, 85, 52, NEG)
        E.frase(c, t, C["s12.c"], [("−", "g", 66, NEG)] + ps("a corrente", "i", 64) + [("desce", "g", 62, NEG)], XE, 520, passo=0.12)
        E.frase(c, t, C["s12.d"], ps("entra pelo", "i", 64) + [("+", "g", 66, COR)], XE, 630, passo=0.12)
        E.foco(c, t, C["s12.e"], 0.5, lambda a: E.pilula(c, "sendo carregada", XE + 260, 760, 52, "g", fundo=CERTO, a=a))
        E.foco(c, t, C["s12.f"], 0.5, lambda a: E.formula(c, "nó: 4 − 2 = 2 = f{8}{4}", XE, 930, 60, "g", TINTA2, a))
    if t < C["s13"]:
        return
    E.frase(c, t, C["s13.a"], ps("potência que vira", "i", 64) + ps("energia química", "g", 62, COR), XE, 330, passo=0.12)
    E.formula_em(c, t, C["s13.b"], "ε · i = 6 × 2", XE, 500, 76, "g", TINTA)
    bola_txt(c, t, C["s13.c"], "12 W", XE + 640, 475, 85, 54, CERTO)
    E.foco(c, t, C["s13.c"] + 1.4, 0.4, lambda a: E.escreve(c, "12 joules a cada segundo", XE, 600, 50, "i", TINTA2, a))
    E.formula_em(c, t, C["s13.d"], "R · i^2 = 1 × 2^2", XE, 790, 76, "g", TINTA)
    bola_txt(c, t, C["s13.e"], "4 W", XE + 640, 765, 85, 60)
    E.foco(c, t, C["s13.e"] + 0.4, 0.4, lambda a: E.escreve(c, "calor no resistor", XE, 890, 50, "i", TINTA2, a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def r_():
        E.frase(c, t, C["s14"], [("resumindo", "i", 92, COR)], W / 2, 180, "center")
        E.frase(c, t, C["s14.a"], [("nó,", "g", 76), ("malha", "g", 76), ("e", "i", 80), ("sistema", "g", 76, COR)], W / 2, 380, "center", 0.14)
        E.frase(c, t, C["s14.a"] + 1.4, ps("sempre com a regra de sinais", "i", 64), W / 2, 480, "center", 0.1)
        E.frase(c, t, C["s14.b"], [("sinal", "i", 76), ("de", "i", 76), ("menos", "g", 72, NEG)] + ps("não é erro:", "i", 76), W / 2, 680, "center", 0.12)
        E.frase(c, t, C["s14.c"], ps("é o sentido real", "g", 76, COR), W / 2, 800, "center", 0.12)
    E.saida(c, t, C["s14.d"] - 0.1, r_)
    if t < C["s14.d"]:
        return
    E.frase(c, t, C["s14.d"], ps("trilha de", "i", 84) + [("Eletricidade", "g", 90, COR)], XE, 330, passo=0.14)
    E.foco(c, t, C["s14.d"] + 0.8, 0.5, lambda a: E.pilula(c, "completa", XE + 200, 470, 60, "g", fundo=CERTO, a=a))
    E.foco(c, t, C["s14.d"] + 0.4, 0.8, lambda a: E.simbolo(c, 560, 780, 170 * ease_back(prog(t, C["s14.d"] + 0.4, 0.8)), giro=12 * math.sin(t * 0.4)), blur=0)
    inscreva(c, t, C["s14.e"], C["s14.f"])


BLOCKS = dict(gancho=b_gancho, metodo=b_metodo, q1=b_q1, q2=b_q2, q3=b_q3, q4=b_q4, fim=b_fim)
