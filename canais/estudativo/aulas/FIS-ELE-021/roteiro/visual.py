"""Visual — Estudativo · FIS-ELE-021: circuito simples e lei de Pouillet.

Segue a LINGUAGEM VISUAL DA FÍSICA (docstring do visual.py da FIS-CIN-001), a da ELETRICIDADE (FIS-ELE-001) e a do módulo
GERADORES E RECEPTORES (docstring do visual.py da FIS-ELE-020): gerador real = pilha + r numa caixa tracejada (`gerador_real`),
ε em laranja, a perda r·i em cor de calor, gráficos com F.grafico. Peças novas desta aula (copie quando precisar):
- `circuito`: a volta padrão do módulo, com o gerador real em cima e a carga de fora embaixo (um resistor, ou uma função
  que desenha a carga entre dois pontos, como `paralelo2`); a corrente anda no sentido horário, saindo do + do gerador.
- `paralelo2`: dois resistores em paralelo entre dois nós, na horizontal.
- `tabela`: linhas que entram uma por cue, com a linha de destaque na cor da matéria.
- No gráfico P × i, a parábola da potência útil em laranja, com os zeros (0 e a corrente de curto) e o topo marcados.
Todo instante vem de C[...] (marcadores do roteiro), para acompanhar a voz real quando ela chegar."""
import math

import editorial as E
import fisica as F
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Física", "Eletricidade")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_FIS-ELE-021_circuito_simples_lei_de_pouillet.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("lei", "exemplo", "maxima", "parabola", "atalho", "questao", "fim"))
BR = "#FFFFFF"
CALOR = "#D9480F"

# todas as contas da aula
pou = lambda e, R, r: e / (R + r)
assert pou(12, 5, 1) == 2 and 12 / 5 == 2.4 and 5 * 2 == 10 and 10 * 10 / (10 + 10) == 5 and pou(12, 5, 1) == pou(12, 10 * 10 / 20, 1)
tab = [(R, pou(12, R, 2), R * pou(12, R, 2) ** 2) for R in (1, 2, 4)]
assert tab == [(1, 4, 16), (2, 3, 18), (4, 2, 16)]
icc = 12 / 2
assert icc == 6 and all(12 * i - 2 * i * i <= 18 for i in (0, 1, 2, 3, 4, 5, 6)) and 12 * 3 - 2 * 9 == 18
assert 2 * 3 == 6 == 12 / 2 and 6 / 12 == 0.5 and 12 ** 2 / (4 * 2) == 18 and (12 / 2) * (icc / 2) == 18
Rp = 12 * 6 / (12 + 6)
assert 12 * 6 == 72 and Rp == 4 and pou(24, Rp, 2) == 4 and 24 ** 2 == 576 and 576 / 8 == 72


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


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def um():
        circuito(c, t, C["s01.a"], 1000, 1780, 330, 760, "12 V", "", "5 Ω", calor=C["s01.d"])
        E.frase(c, t, C["s01.a"], ps("bateria de", "i", 72) + [("12", "g", 72, COR), ("V", "b", 54, F.UNID)], XE, 250, passo=0.12)
        E.frase(c, t, C["s01.a"] + 1.0, ps("resistor de", "i", 72) + [("5", "g", 72), ("Ω", "b", 54, F.UNID)], XE, 360, passo=0.12)
        E.foco(c, t, C["s01.b"], 0.5, lambda a: E.formula(c, "12 ÷ 5 = 2,4 A ?", XE, 540, 90, "g", ERRADO, a))
        if t >= C["s01.c"]:
            E.risco(c, XE - 10, 560, XE + 720, 470, t, C["s01.c"], largura=12)
        E.frase(c, t, C["s01.c"], ps("não: passam só", "i", 76) + [("2", "g", 76, CERTO), ("A", "b", 56, F.UNID)], XE, 700, passo=0.12)
        E.frase(c, t, C["s01.d"], ps("faltou", "i", 76) + [("r", "g", 76, CALOR), ("=", "g", 76, TINTA2), ("1", "g", 76, CALOR), ("Ω", "b", 58, F.UNID)],
                XE, 880, passo=0.12)
        E.foco(c, t, C["s01.d"] + 0.4, 0.5, lambda a: centro(c, "1 Ω", 1516, 272, 50, "b", CALOR, a))
    E.saida(c, t, C["s02"] - 0.1, um)
    if t >= C["s02"]:
        promessa(c, t, C, "s02", (("s02.a", "a corrente numa fração", 1.4), ("s02.b", "a potência máxima", 0)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    lembrete(c, t, C, "s03", (("s03.b", "nos polos do gerador", "U = ε − r · i"),
                              ("s03.c", "série e paralelo", "reduzir até um resistor só")))


# ---------------- a lei ----------------
def b_lei(c, t, C, b):
    circuito(c, t, C["s04.a"], 1050, 1780, 230, 520, corrente=C["s06.b"])

    def s04():
        E.frase(c, t, C["s04.b"], ps("polos do gerador =", "i", 60) + [("resistor", "g", 58, COR)], XE, 220, passo=0.1)
        E.foco(c, t, C["s04.c"], 0.5, lambda a: (E.escreve(c, "gerador:", XE, 350, 56, "i", TINTA2, a), E.formula(c, "U = ε − r · i", XE + 250, 350, 66, "g", TINTA, a)))
        E.foco(c, t, C["s04.d"], 0.5, lambda a: (E.escreve(c, "resistor:", XE, 460, 56, "i", TINTA2, a), E.formula(c, "U = R · i", XE + 250, 460, 66, "g", TINTA, a)))
    E.saida(c, t, C["s06"] - 0.1, s04)
    if t < C["s06"]:
        E.foco(c, t, C["s05.a"], 0.5, lambda a: E.formula(c, "R · i = ε − r · i", XE, 650, 76, "g", TINTA, a))
        E.foco(c, t, C["s05.b"], 0.5, lambda a: E.formula(c, "R · i + r · i = ε", XE, 780, 76, "g", TINTA, a))
        E.foco(c, t, C["s05.c"], 0.5, lambda a: E.formula(c, "i · (R + r) = ε", XE, 910, 76, "g", TINTA, a))
    E.foco(c, t, C["s05.d"], 0.5, lambda a: E.pilula(c, "lei de Pouillet", 1420, 680, 50, "g", fundo=E.COR, a=a))
    E.formula_em(c, t, C["s05.e"], "i = f{ε}{R + r}", 1420, 900, 130, "g", TINTA, "center")
    if t >= C["s06"]:
        E.frase(c, t, C["s06.a"], [("ε", "g", 70, COR)] + ps("empurra a corrente", "i", 72), XE, 680, passo=0.12)
        E.frase(c, t, C["s06.b"], ps("por todas as resistências", "i", 66) + [("da", "i", 66), ("volta", "g", 64)], XE, 790, passo=0.1)
        E.frase(c, t, C["s06.c"], [("R", "g", 66, COR)] + ps("de fora +", "i", 66) + [("r", "g", 66, CALOR)] + ps("de dentro, em série", "i", 66),
                XE, 900, passo=0.1)


# ---------------- exemplos ----------------
def b_exemplo(c, t, C, b):
    if t < C["s08"]:
        circuito(c, t, C["s07"], 1130, 1790, 280, 640, "12 V", "1 Ω", "5 Ω", corrente=C["s07.c"])

        def s07():
            E.frase(c, t, C["s07"], ps("no gancho", "i", 74, COR), XE, 220)
            E.formula_em(c, t, C["s07.a"], "i = f{12}{5 + 1}", XE, 420, 100, "g", TINTA)
            E.formula_em(c, t, C["s07.b"], "= f{12}{6}", XE + 450, 420, 100, "g", TINTA)
            bola_txt(c, t, C["s07.c"], "2 A", XE + 760, 390, 90, 64)
            E.formula_em(c, t, C["s07.d"], "U = R · i = 5 × 2", XE, 720, 80, "g", TINTA)
            bola_txt(c, t, C["s07.e"], "10 V", XE + 760, 690, 90, 58)
        E.saida(c, t, C["s08"] - 0.1, s07)
        return
    circuito(c, t, C["s08"], 1050, 1780, 280, 700, "12 V", "1 Ω",
             lambda A, B: paralelo2(c, t, C["s08.b"], A, B, "10 Ω", "10 Ω"), corrente=C["s08.d"])
    E.frase(c, t, C["s08.a"], ps("vários resistores fora:", "i", 66) + [("reduza", "g", 64, COR)], XE, 230, passo=0.12)
    E.frase(c, t, C["s08.b"], ps("dois de", "i", 70) + [("10", "g", 68), ("Ω", "b", 52, F.UNID)] + ps("em paralelo", "i", 70), XE, 420, passo=0.12)
    E.foco(c, t, C["s08.c"], 0.5, lambda a: E.formula(c, "f{10}{2} = 5 Ω", XE, 580, 90, "g", COR, a))
    E.frase(c, t, C["s08.d"], ps("o mesmo circuito:", "i", 70), XE, 800, passo=0.12)
    bola_txt(c, t, C["s08.d"] + 0.8, "2 A", XE + 650, 780, 90, 64)


# ---------------- potência máxima ----------------
def b_maxima(c, t, C, b):
    E.frase(c, t, C["s09"], ps("potência no resistor de fora =", "i", 62) + [("potência", "g", 60, COR), ("útil", "g", 60, COR)],
            XE, 180, passo=0.1)
    circuito(c, t, C["s09.b"], 1180, 1780, 380, 700, "12 V", "2 Ω", "R = ?")
    E.foco(c, t, C["s09.c"], 0.5, lambda a: E.pilula(c, "troque R", 1480, 860, 44, "g", fundo=TINTA, a=a))
    tabela(c, t, ("R (Ω)", "i (A)", "P = R · i^2"), [(C["s10.a"], ["1", "4", "16 W"]), (C["s10.b"], ["2", "3", "18 W"]), (C["s10.c"], ["4", "2", "16 W"])],
           XE + 30, 360, 290, 140, 70, destaque=1, td=C["s11.a"])
    E.frase(c, t, C["s11.b"], ps("fora = dentro:", "i", 66) + [("R", "g", 70, COR), ("=", "g", 70, TINTA2), ("r", "g", 70, COR)], XE, 900, passo=0.12)
    E.foco(c, t, C["s11.d"], 0.5, lambda a: E.pilula(c, "potência máxima", 1480, 975, 50, "g", fundo=E.COR, a=a))


# ---------------- a parábola ----------------
def b_parabola(c, t, C, b):
    P = F.grafico(c, t, C["s12"], 1080, 200, 700, 620, 0, 6.8, 0, 21, "i (A)", "P (W)", passo=1, passo_y=3,
                  marcas_x=[1, 2, 3, 4, 5, 6], marcas_y=[6, 12, 18])
    f = lambda i: 12 * i - 2 * i * i
    E.formula_em(c, t, C["s12.a"], "P = U · i", XE, 230, 80, "g", TINTA)
    E.formula_em(c, t, C["s12.b"], "P = ε · i − r · i^2", XE, 360, 80, "g", TINTA)
    E.foco(c, t, C["s12.b"] + 1.6, 0.4, lambda a: E.formula(c, "= 12 · i − 2 · i^2", XE, 460, 64, "b", TINTA2, a))
    E.curva(c, t, C["s12.c"], P, f, 0, 6, d=1.2)
    E.ponto(c, t, C["s12.d"], P, 0, 0, None)
    E.ponto(c, t, C["s12.d"] + 0.5, P, 6, 0, None)
    E.foco(c, t, C["s12.d"] + 0.8, 0.4, lambda a: E.pilula(c, "curto: 6 A", P.x(4.6), P.oy - 45, 38, "g", fundo=TINTA, a=a))
    if t >= C["s12.e"]:
        M.line(c, P.x(3), P.oy, P.x(3), P.y(18), TINTA2, ep(t, C["s12.e"], 0.5), 4, dash=E.TRACO)
    E.ponto(c, t, C["s12.f"], P, 3, 18, "18 W", guias=False)
    E.frase(c, t, C["s12.e"], ps("simétrica: o topo", "i", 60) + [("no", "i", 60), ("meio", "g", 58, COR)], XE, 570, passo=0.1)

    def s13():
        E.foco(c, t, C["s13.a"], 0.5, lambda a: E.formula(c, "i = f{6}{2} = 3 A", XE, 700, 64, "g", TINTA, a))
        E.foco(c, t, C["s13.b"], 0.5, lambda a: E.formula(c, "perda: 2 × 3 = 6 V", XE, 810, 58, "g", CALOR, a))
        E.foco(c, t, C["s13.c"], 0.5, lambda a: E.formula(c, "polos: 6 V", XE, 905, 58, "g", TINTA, a))
        E.foco(c, t, C["s13.d"], 0.5, lambda a: E.formula(c, "rendimento = f{6}{12} = 50 %", XE, 1005, 56, "g", COR, a))
    if t >= C["s13"]:
        s13()


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s14"], [("cuidado", "g", 96, ERRADO)], XE, 210)
    E.frase(c, t, C["s14.a"], ps("resistor menor", "i", 74) + ps("sempre recebe mais?", "g", 68), XE, 370, passo=0.12)
    if t >= C["s14.b"]:
        E.risco(c, XE - 10, 390, XE + 1340, 310, t, C["s14.b"], largura=12)
    tabela(c, t, ("R (Ω)", "i (A)", "P (W)"), [(C["s14.b"], ["1", "4", "16"]), (C["s14.b"] + 0.6, ["2", "3", "18"])],
           XE + 30, 520, 290, 120, 70, destaque=1, td=C["s14.b"] + 1.4)
    E.foco(c, t, C["s14.b"] + 1.0, 0.4, lambda a: E.pilula(c, "corrente maior, potência menor", 1440, 640, 44, "g", fundo=ERRADO, a=a))
    E.frase(c, t, C["s14.c"], ps("abaixo de", "i", 64) + [("r,", "g", 64, CALOR)] + ps("a tensão se perde", "i", 64) + [("dentro", "g", 62, CALOR)],
            XE, 960, passo=0.1)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def s15():
        E.frase(c, t, C["s15"], ps("o atalho da", "i", 72, CLARO) + ps("potência máxima", "g", 68, BR), W / 2, 170, "center", 0.12)
        E.formula_em(c, t, C["s15.a"], "R = r", 300, 360, 100, "g", BR)
        E.formula_em(c, t, C["s15.b"], "U = f{ε}{2}", 860, 360, 100, "g", BR)
        E.formula_em(c, t, C["s15.c"], "P máx = f{ε}{2} · f{corrente de curto}{2}", 300, 600, 76, "g", CLARO)
        E.formula_em(c, t, C["s15.d"], "= f{ε^2}{4 r}", 1360, 600, 96, "g", BR)
        E.formula_em(c, t, C["s15.e"], "f{144}{8} =", 600, 900, 96, "g", BR)
        bola_txt(c, t, C["s15.f"], "18 W", 1050, 870, 110, 66)
    E.saida(c, t, C["s16"] - 0.1, s15)
    if t < C["s16"]:
        return
    E.frase(c, t, C["s16.a"], ps("é o", "i", 72, CLARO) + ps("topo da parábola", "g", 68, BR), W / 2, 260, "center", 0.12)
    E.frase(c, t, C["s16.b"], ps("potência máxima", "g", 66, BR) + [("≠", "g", 66, ERRADO)] + ps("rendimento máximo", "g", 66, BR), W / 2, 460, "center", 0.12)
    E.frase(c, t, C["s16.c"], ps("metade vira calor:", "i", 64, CLARO) + [("50", "g", 64, BR), ("%", "g", 52, CLARO)], W / 2, 620, "center", 0.12)
    E.frase(c, t, C["s16.d"], [("não", "g", 60, ERRADO), ("serve:", "i", 64, CLARO)] + ps("pediu o maior rendimento", "i", 64, CLARO), W / 2, 820, "center", 0.1)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s17"], ps("hora de testar", "i", 72, COR), XE, 200)
    E.frase(c, t, C["s17.a"], [("24", "g", 64), ("V", "b", 48, F.UNID)] + ps("e", "i", 66) + [("2", "g", 64), ("Ω", "b", 48, F.UNID)] + ps("internos", "i", 66),
            XE, 340, passo=0.1)
    E.frase(c, t, C["s17.b"], [("12", "g", 64), ("Ω", "b", 48, F.UNID)] + ps("e", "i", 66) + [("6", "g", 64), ("Ω", "b", 48, F.UNID)] + ps("em paralelo", "i", 66),
            XE, 440, passo=0.1)
    E.frase(c, t, C["s17.c"], ps("corrente no gerador?", "g", 66), XE, 620, passo=0.12)
    E.frase(c, t, C["s17.d"], ps("que", "i", 66) + [("R", "g", 66, COR)] + ps("dá a potência máxima?", "i", 66), XE, 740, passo=0.1)
    E.frase(c, t, C["s17.d"] + 1.6, ps("de quanto?", "i", 66, COR), XE, 850)
    if t < C["s18"]:
        circuito(c, t, C["s17.a"], 1150, 1790, 330, 760, "24 V", "2 Ω", lambda A, B: paralelo2(c, t, C["s17.b"], A, B, "12 Ω", "6 Ω"))
    else:
        E.relogio(c, t, C["s18.a"], cx=1460, cy=440, r=200)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    E.foco(c, t, C["s19.a"], 0.5, lambda a: E.formula(c, "f{12 · 6}{12 + 6} = f{72}{18} =", XE, 300, 84, "g", TINTA, a))
    bola_txt(c, t, C["s19.b"], "4 Ω", XE + 800, 270, 90, 64)
    E.foco(c, t, C["s19.c"], 0.5, lambda a: E.formula(c, "i = f{24}{4 + 2} =", XE, 540, 84, "g", TINTA, a))
    bola_txt(c, t, C["s19.d"], "4 A", XE + 600, 510, 90, 64, CERTO)
    E.foco(c, t, C["s20.a"], 0.5, lambda a: E.formula(c, "R = r = 2 Ω", XE, 760, 76, "g", COR, a))
    E.foco(c, t, C["s20.b"], 0.5, lambda a: E.formula(c, "P máx = f{24^2}{4 · 2} = f{576}{8} =", XE, 930, 76, "g", TINTA, a))
    bola_txt(c, t, C["s20.c"], "72 W", XE + 1050, 900, 100, 62, CERTO)


# ---------------- fechamento ----------------
def motor_simb(c, cx, cy, r_, a=1.0):
    """motor: círculo com M"""
    if a <= 0:
        return
    c.drawCircle(cx, cy, r_, M.paint("#FFFFFF", a))
    c.drawCircle(cx, cy, r_, M.paint(TINTA, a, stroke=6))
    centro(c, "M", cx, cy + r_ * 0.36, r_, "g", E.COR, a)


def b_fim(c, t, C, b):
    def r_():
        resumo(c, t, C, "s21", (("s21.a", [("i = ", "g", 72), ("ε", "g", 72, COR), ("÷", "g", 72, TINTA2), ("todas", "i", 72), ("as", "i", 72),
                                           ("resistências", "g", 66)]),
                               ("s21.b", [("potência", "i", 66), ("máxima:", "g", 64), ("R", "g", 70, COR), ("=", "g", 70, TINTA2), ("r,", "g", 70, COR),
                                          ("50", "g", 64), ("%", "g", 52, TINTA2)])))
    E.saida(c, t, C["s22"] - 0.1, r_)
    if t < C["s22"]:
        return
    E.frase(c, t, C["s22"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C["s22.a"], [("o", "i", 100), ("motor", "g", 104, COR)], XE, 420)
    E.frase(c, t, C["s22.b"], ps("e várias", "i", 90) + [("pilhas", "g", 94, COR)], XE, 570, passo=0.14)
    E.foco(c, t, C["s22.a"] + 0.4, 0.5, lambda a: motor_simb(c, 520, 800, 110, a))
    for k in range(3):
        E.foco(c, t, C["s22.b"] + 0.3 + 0.2 * k, 0.4, lambda a, k=k: (M.rrect(c, 800 + k * 170, 760, 150, 70, 14, "#2A2A33", a),
                                                                      M.rrect(c, 890 + k * 170, 760, 60, 70, 14, E.COR, a)))
    inscreva(c, t, C["s22.c"], C["s22.d"])


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, lei=b_lei, exemplo=b_exemplo, maxima=b_maxima, parabola=b_parabola,
              erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
