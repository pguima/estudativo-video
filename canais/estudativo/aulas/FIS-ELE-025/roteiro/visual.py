"""Visual — Estudativo · FIS-ELE-025: circuito com duas malhas.

Segue a LINGUAGEM VISUAL DA FÍSICA (FIS-CIN-001), a da ELETRICIDADE (FIS-ELE-001), a do módulo GERADORES E RECEPTORES
(FIS-ELE-020) e a do módulo LEIS DE KIRCHHOFF (docstring do visual.py da FIS-ELE-024: `percurso`, `etiqueta_termo`, termo que
soma em laranja e que subtrai em azul). Peças novas desta aula (copie quando precisar):
- `circ3`: o circuito de três ramos entre os nós A (em cima) e B (embaixo); nos ramos de gerador, o gerador fica embaixo
  (com o + para cima) e o resistor em cima. Funciona no palco com escuro=True.
- `seta_i`: a corrente de um ramo, seta laranja ao lado do fio com o nome (i₁, i₂, i₃, com índice Unicode) e, quando a
  conta acaba, o valor.
- O SISTEMA fica à esquerda com a chave (E.sistema); a substituição desce linha a linha, e cada corrente achada vai para a
  esfera. Na conferência, a tensão U entre A e B aparece como uma seta dupla cinza entre os nós.
Todo instante vem de C[...] (marcadores do roteiro), para acompanhar a voz real quando ela chegar."""
import math

import editorial as E
import fisica as F
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Física", "Eletricidade")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_FIS-ELE-025_circuito_com_duas_malhas.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("circuito", "sistema", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
NEG = F.NEG

# todas as contas da aula
i1, i2, i3 = 3, 1, 4
assert i3 == i1 + i2 and 10 - 2 * i1 - 1 * i3 == 0 and 6 - 2 * i2 - i3 == 0
assert 10 == 3 * i1 + i2 and 6 == i1 + 3 * i2 and 10 - 3 * i1 == i2 and 6 == 30 - 8 * i1 and i1 + 3 * (10 - 3 * i1) == 6
assert 10 - 2 * 3 + 2 * 1 - 6 == 0
U = 4
assert (10 - U) / 2 + (6 - U) / 2 == U / 1 and 16 - 2 * U == 2 * U and (10 - U) / 2 == 3 and (6 - U) / 2 == 1
q1, q2, q3 = 2, 2, 4
assert q3 == q1 + q2 and 10 == 3 * q1 + q3 and 8 == 2 * q2 + q3 and 10 == 4 * q1 + q2 and 8 == q1 + 3 * q2
assert q1 + 3 * (10 - 4 * q1) == 8 and 30 - 11 * q1 == 8 and 11 * q1 == 22
assert (10 - 4) / 3 + (8 - 4) / 2 == 4 and 2 * (10 - 4) + 3 * (8 - 4) == 6 * 4 and 44 == 11 * 4


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


def percurso(c, t, t0, cx, cy, r, horario=True, cor=TINTA2, rot=None):
    """seta circular tracejada: o sentido em que se anda a malha"""
    q = ease_io(prog(t, t0, 0.8))
    if q <= 0:
        return
    pt = M.paint(cor, 1.0, stroke=6)
    pt.setPathEffect(skia.DashPathEffect.Make([18, 12], 0))
    ini, var = (-200, 300 * q) if horario else (20, -300 * q)
    c.drawArc(skia.Rect.MakeXYWH(cx - r, cy - r, 2 * r, 2 * r), ini, var, False, pt)
    g = math.radians(ini + var)
    x, y = cx + r * math.cos(g), cy + r * math.sin(g)
    d = 1 if horario else -1
    tx, ty = -math.sin(g) * d, math.cos(g) * d
    F._cabeca(c, x + tx * 14, y + ty * 14, tx, ty, 30, cor, 1.0)
    if rot:
        E.foco(c, t, t0 + 0.5, 0.4, lambda a: centro(c, rot, cx, cy + 16, 44, "i", cor, a))


def pilula_f(c, s, cx, cy, size, fundo=None, cor=BR, a=1.0):
    """pílula com fórmula (aceita "=", "→", fração e potência)"""
    if a <= 0:
        return
    w, h = E.formula(None, s, 0, 0, size, "g", a=0) + size * 1.2, size * 1.9
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2, cy - h / 2, w, h), h / 2, h / 2), M.paint(fundo or E.COR, a))
    E.formula(c, s, cx, cy + size * 0.36, size, "g", cor, a, "center")




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


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def um():
        circ3(c, t, C["s01.a"], C["s01.a"] + 0.3, C["s01.a"] + 0.6, "", "", "", "", "")
        correntes(c, t, C["s01.a"] + 1.4, C["s01.a"] + 1.7, C["s01.a"] + 2.0)
        E.frase(c, t, C["s01.a"], [("2", "g", 90, COR)] + ps("geradores", "i", 84), XE, 260, passo=0.14)
        E.frase(c, t, C["s01.a"] + 0.7, [("3", "g", 90, COR)] + ps("ramos", "i", 84), XE, 380, passo=0.14)
        E.frase(c, t, C["s01.a"] + 1.4, [("3", "g", 90, COR)] + ps("correntes", "i", 84) + [("?", "g", 90, COR)], XE, 500, passo=0.14)
        E.frase(c, t, C["s01.c"], ps("nós + malhas", "g", 70) + [("→", "g", 70, TINTA2)], XE, 720, passo=0.12)
        E.frase(c, t, C["s01.c"] + 1.4, ps("um", "i", 84) + [("sistema", "g", 90, COR)], XE, 860, passo=0.14)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t >= C["s02"]:
        promessa(c, t, C, "s02", (("s02.a", "montar e resolver o sistema", 1.4), ("s02.b", "o atalho de uma equação", 0)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    lembrete(c, t, C, "s03", (("s03.b", "nós, malhas e a regra de sinais", "leis de Kirchhoff"),
                              ("s03.c", "sistema por substituição", "isole uma letra e leve para a outra")))


# ---------------- o circuito, as correntes, o nó e as malhas ----------------
def b_circuito(c, t, C, b):
    circ3(c, t, C["s04.a"], C["s04.b"], C["s04.c"], "10 V", "2 Ω", "6 V", "2 Ω", "1 Ω")
    nomes_nos(c, t, C["s04.d"])
    correntes(c, t, C["s05.b"], C["s05.c"], C["s05.d"])

    def s04():
        E.frase(c, t, C["s04"], ps("o circuito", "i", 76, COR), XE, 220)
        for k, (cue, nome, s) in enumerate((("s04.a", "esquerda:", "10 V e 2 Ω"), ("s04.b", "direita:", "6 V e 2 Ω"), ("s04.c", "meio:", "1 Ω"))):
            y = 380 + k * 120
            E.foco(c, t, C[cue], 0.5, lambda a, y=y, nome=nome, s=s: (E.escreve(c, nome, XE, y, 58, "i", TINTA2, a), E.formula(c, s, XE + 280, y, 62, "g", TINTA, a)))
        E.frase(c, t, C["s04.d"], ps("três ramos, os mesmos", "i", 58) + [("dois", "g", 56), ("nós", "g", 56, COR)], XE, 800, passo=0.1)
    E.saida(c, t, C["s05"] - 0.1, s04)
    if t < C["s05"]:
        return

    def s05():
        E.foco(c, t, C["s05.a"], 0.4, lambda a: E.pilula(c, "passo 1", XE + 90, 220, 40, "g", fundo=E.COR, a=a))
        E.frase(c, t, C["s05.a"] + 0.2, ps("nome e sentido em cada ramo", "i", 58), XE + 230, 236, passo=0.08)
        E.frase(c, t, C["s05.e"], ps("chute errado →", "i", 56, TINTA2) + ps("sinal de menos", "g", 54, NEG), XE, 340, passo=0.1)
    E.saida(c, t, C["s06"] - 0.1, s05)
    if t < C["s06"]:
        return
    E.foco(c, t, C["s06.a"], 0.4, lambda a: E.pilula(c, "passo 2", XE + 90, 220, 40, "g", fundo=E.COR, a=a))
    E.frase(c, t, C["s06.a"] + 0.2, ps("lei dos nós em", "i", 58) + [("A", "g", 58)], XE + 230, 236, passo=0.08)
    if t >= C["s06.b"]:
        c.drawCircle(1410, 250, 40 + 4 * math.sin(t * 5), M.paint(E.COR, ep(t, C["s06.b"], 0.4), stroke=6))
    E.formula_em(c, t, C["s06.c"], "i₃ = i₁ + i₂", XE, 360, 80, "g", TINTA)
    if t < C["s07"]:
        return
    E.foco(c, t, C["s07.a"], 0.4, lambda a: E.pilula(c, "passo 3", XE + 90, 500, 40, "g", fundo=E.COR, a=a))
    E.frase(c, t, C["s07.a"] + 0.2, ps("uma malha de cada lado", "i", 58), XE + 230, 516, passo=0.08)
    percurso(c, t, C["s07.b"], 1250, 680, 70, horario=True)
    percurso(c, t, C["s07.e"], 1580, 680, 70, horario=False)
    E.linha(c, t, [("10", "g", 64, COR, C["s07.b"]), ("− 2i₁", "g", 64, NEG, C["s07.c"]), ("− 1 · i₃", "g", 64, NEG, C["s07.d"]),
                   ("= 0", "g", 64, TINTA, C["s07.d"] + 1.0)], XE, 690)
    E.linha(c, t, [("6", "g", 64, COR, C["s07.f"]), ("− 2i₂", "g", 64, NEG, C["s07.f"] + 0.6), ("− i₃", "g", 64, NEG, C["s07.f"] + 1.2),
                   ("= 0", "g", 64, TINTA, C["s07.f"] + 1.8)], XE, 860)
    E.foco(c, t, C["s07.b"] + 0.3, 0.4, lambda a: E.escreve(c, "malha da esquerda:", XE, 610, 44, "i", TINTA2, a))
    E.foco(c, t, C["s07.e"] + 0.3, 0.4, lambda a: E.escreve(c, "malha da direita:", XE, 780, 44, "i", TINTA2, a))


# ---------------- o sistema ----------------
def b_sistema(c, t, C, b):
    xs, yt, yb = (1100, 1420, 1740), 300, 800
    if t < C["s11"]:
        circ3(c, t, C["s08"], C["s08"], C["s08"], "10 V", "2 Ω", "6 V", "2 Ω", "1 Ω", xs, yt, yb)
        correntes(c, t, C["s08"], C["s08"], C["s08"], xs, yt, yb, ("3 A", "1 A", "4 A"), C["s10.a"])

        def s0809():
            E.foco(c, t, C["s08.a"], 0.4, lambda a: E.pilula(c, "passo 4", XE + 90, 200, 40, "g", fundo=E.COR, a=a))
            E.frase(c, t, C["s08.a"] + 0.2, [("i₃", "g", 56), ("→", "g", 56, TINTA2), ("i₁ + i₂", "g", 56, COR)], XE + 230, 216, passo=0.1)
            E.sistema(c, t, C["s08.b"], ["10 = 3i₁ + i₂", "6 = i₁ + 3i₂"], XE, 380, 76, tl=[C["s08.b"], C["s08.c"]])
            E.foco(c, t, C["s08.d"], 0.4, lambda a: E.escreve(c, "duas equações, duas letras", XE, 560, 46, "i", TINTA2, a))
            E.formula_em(c, t, C["s09.b"], "i₂ = 10 − 3i₁", XE, 670, 68, "g", COR)
            E.formula_em(c, t, C["s09.c"], "6 = i₁ + 3 · (10 − 3i₁)", XE, 790, 68, "g", TINTA)
            E.formula_em(c, t, C["s09.d"], "6 = 30 − 8i₁", XE, 910, 68, "g", TINTA)
            bola_txt(c, t, C["s09.e"], "3 A", XE + 760, 885, 80, 58)
            E.foco(c, t, C["s09.e"] + 0.3, 0.4, lambda a: E.formula(c, "i₁ =", XE + 540, 905, 60, "g", TINTA, a))
        E.saida(c, t, C["s10"] - 0.1, s0809)
        if t >= C["s10"]:
            E.foco(c, t, C["s10.a"], 0.5, lambda a: E.formula(c, "i₂ = 10 − 9 =", XE, 360, 76, "g", TINTA, a))
            bola_txt(c, t, C["s10.b"], "1 A", XE + 640, 335, 85, 60)
            E.foco(c, t, C["s10.c"], 0.5, lambda a: E.formula(c, "i₃ = 3 + 1 =", XE, 560, 76, "g", TINTA, a))
            bola_txt(c, t, C["s10.d"], "4 A", XE + 640, 535, 85, 60)
            E.frase(c, t, C["s10.e"], ps("todos positivos:", "i", 60) + ps("chutes certos", "g", 58, CERTO), XE, 780, passo=0.1)
        return
    # s11: a malha de fora confere
    circ3(c, t, C["s11"], C["s11"], C["s11"], "10 V", "2 Ω", "6 V", "2 Ω", "1 Ω", xs, yt, yb)
    correntes(c, t, C["s11"], C["s11"], C["s11"], xs, yt, yb, ("3 A", "1 A", "4 A"), C["s11"])
    if t >= C["s11.a"]:
        q = ep(t, C["s11.a"], 0.6)
        pt = M.paint(TINTA2, q, stroke=5)
        pt.setPathEffect(skia.DashPathEffect.Make([18, 12], 0))
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(xs[0] - 120, yt - 80, xs[2] - xs[0] + 230, yb - yt + 160), 40, 40), pt)
    E.frase(c, t, C["s11.a"], ps("confira na malha", "i", 66) + [("de", "g", 62), ("fora", "g", 62, COR)], XE, 220, passo=0.12)
    E.linha(c, t, [("+10", "g", 66, COR, C["s11.b"]), ("− 2 · 3", "g", 66, NEG, C["s11.b"] + 0.8), ("+ 2 · 1", "g", 66, COR, C["s11.c"]),
                   ("− 6", "g", 66, NEG, C["s11.d"]), ("= 0", "g", 66, CERTO, C["s11.e"])], XE, 420)
    E.frase(c, t, C["s11.c"], ps("descendo contra", "i", 54, TINTA2) + [("i₂:", "g", 52, COR), ("+", "g", 52, COR)], XE, 560, passo=0.08)
    E.frase(c, t, C["s11.d"], ps("entra pelo + do de 6 V:", "i", 54, TINTA2) + [("−", "g", 52, NEG)], XE, 660, passo=0.08)
    E.foco(c, t, C["s11.e"] + 0.6, 0.5, lambda a: E.selo(c, XE + 120, 860, 70, True, a))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    xs, yt, yb = (1120, 1430, 1740), 300, 820
    circ3(c, t, C["s12"], C["s12"], C["s12"], "", "", "", "", "", xs, yt, yb)
    correntes(c, t, C["s12"], C["s12"], C["s12"], xs, yt, yb)
    nomes_nos(c, t, C["s12"], xs, yt, yb)
    E.frase(c, t, C["s12"], [("cuidado", "g", 96, ERRADO)], XE, 210)
    E.frase(c, t, C["s12.a"], ps("lei dos nós em A", "i", 64) + [("e", "i", 64)] + ps("em B", "i", 64), XE, 360, passo=0.1)
    E.frase(c, t, C["s12.a"] + 1.4, ps("= duas equações?", "g", 62, ERRADO), XE, 460, passo=0.1)
    if t >= C["s12.c"]:
        E.risco(c, XE - 10, 480, XE + 560, 410, t, C["s12.c"], largura=10)
    E.foco(c, t, C["s12.b"] - 0.3, 0.5, lambda a: (E.escreve(c, "A:", XE, 620, 60, "g", TINTA2, a), E.formula(c, "i₃ = i₁ + i₂", XE + 100, 620, 66, "g", TINTA, a)))
    E.foco(c, t, C["s12.b"], 0.5, lambda a: (E.escreve(c, "B:", XE, 740, 60, "g", TINTA2, a), E.formula(c, "i₁ + i₂ = i₃", XE + 100, 740, 66, "g", TINTA, a)))
    E.foco(c, t, C["s12.c"], 0.5, lambda a: E.pilula(c, "a mesma, virada", XE + 690, 690, 44, "g", fundo=ERRADO, a=a))
    E.frase(c, t, C["s12.d"], ps("a 2ª equação vem de uma", "i", 62) + [("malha", "g", 62, COR)], XE, 920, passo=0.1)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    xs, yt, yb = (1200, 1460, 1720), 300, 800
    circ3(c, t, C["s13"], C["s13"], C["s13"], "10 V", "2 Ω", "6 V", "2 Ω", "1 Ω", xs, yt, yb, escuro=True)
    nomes_nos(c, t, C["s13"], xs, yt, yb, escuro=True)
    if t >= C["s13.a"]:
        q = ep(t, C["s13.a"], 0.5)
        x = xs[1] + 120
        F.seta(c, x, (yt + yb) / 2, x, yt + 30, CLARO, q, 6)
        F.seta(c, x, (yt + yb) / 2, x, yb - 30, CLARO, q, 6)
        E.foco(c, t, C["s13.a"] + 0.3, 0.4, lambda a: E.escreve(c, "U", x + 26, (yt + yb) / 2 + 22, 64, "g", CLARO, a))

    def s13():
        E.frase(c, t, C["s13"], ps("o atalho:", "i", 70, CLARO) + ps("a tensão entre A e B", "g", 62, BR), XE, 180, passo=0.12)
        E.foco(c, t, C["s13.b"], 0.5, lambda a: E.formula(c, "meio:  i₃ = f{U}{1}", XE, 360, 64, "g", BR, a))
        E.foco(c, t, C["s13.d"], 0.5, lambda a: E.formula(c, "esquerda:  i₁ = f{10 − U}{2}", XE, 540, 64, "g", BR, a))
        E.foco(c, t, C["s13.e"], 0.5, lambda a: E.formula(c, "direita:  i₂ = f{6 − U}{2}", XE, 720, 64, "g", BR, a))
        E.frase(c, t, C["s13.c"], ps("o gerador perde no resistor", "i", 52, CLARO), XE, 450, passo=0.08)
    E.saida(c, t, C["s14"] - 0.1, s13)
    if C["s14"] <= t < C["s15"]:
        E.formula_em(c, t, C["s14.a"], "f{10 − U}{2} + f{6 − U}{2} = U", XE, 360, 76, "g", BR)
        E.formula_em(c, t, C["s14.b"], "16 − 2U = 2U", XE, 560, 76, "g", CLARO)
        bola_txt(c, t, C["s14.c"], "4 V", XE + 760, 530, 80, 58)
        E.foco(c, t, C["s14.c"] + 0.2, 0.4, lambda a: E.formula(c, "U =", XE + 520, 552, 60, "g", BR, a))
        E.foco(c, t, C["s14.d"], 0.5, lambda a: E.formula(c, "i₁ = 3 A    i₂ = 1 A    i₃ = 4 A", XE, 780, 60, "g", BR, a))
    if t < C["s15"]:
        return
    E.frase(c, t, C["s15.a"], ps("três ramos,", "i", 62, CLARO) + ps("os mesmos dois nós:", "g", 58, BR), XE, 360, passo=0.1)
    E.frase(c, t, C["s15.b"], ps("a mesma", "i", 62, CLARO) + [("U", "g", 62, BR)] + ps("para todos", "i", 62, CLARO), XE, 470, passo=0.1)
    E.frase(c, t, C["s15.c"], [("não", "g", 56, ERRADO), ("compensa:", "i", 58, CLARO)] + ps("mais de dois nós", "i", 58, CLARO), XE, 700, passo=0.1)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s16"], ps("hora de testar", "i", 72, COR), XE, 200)
    for k, (cue, nome, s) in enumerate((("s16.a", "esquerda:", "10 V e 3 Ω"), ("s16.b", "direita:", "8 V e 2 Ω"), ("s16.c", "meio:", "1 Ω"))):
        y = 340 + k * 110
        E.foco(c, t, C[cue], 0.5, lambda a, y=y, nome=nome, s=s: (E.escreve(c, nome, XE, y, 58, "i", TINTA2, a), E.formula(c, s, XE + 280, y, 62, "g", TINTA, a)))
    E.frase(c, t, C["s16.d"], ps("os dois com o", "i", 58) + [("+", "g", 58, COR)] + ps("para cima", "i", 58), XE, 700, passo=0.1)
    E.frase(c, t, C["s16.e"], ps("monte o sistema e ache", "i", 60) + [("i₁,", "g", 60, COR), ("i₂", "g", 60, COR), ("e", "i", 60), ("i₃", "g", 60, COR)],
            XE, 830, passo=0.1)
    if t < C["s17"]:
        circ3(c, t, C["s16.a"], C["s16.b"], C["s16.c"], "10 V", "3 Ω", "8 V", "2 Ω", "1 Ω", (1130, 1430, 1730), 300, 820)
        nomes_nos(c, t, C["s16.d"], (1130, 1430, 1730), 300, 820)
    else:
        E.relogio(c, t, C["s17.a"], cx=1460, cy=440, r=200)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    xs, yt, yb = (1160, 1450, 1740), 330, 800
    circ3(c, t, C["s18"], C["s18"], C["s18"], "10 V", "3 Ω", "8 V", "2 Ω", "1 Ω", xs, yt, yb)
    correntes(c, t, C["s18"], C["s18"], C["s18"], xs, yt, yb, ("2 A", "2 A", "4 A"), C["s19.d"])

    def s18():
        E.formula_em(c, t, C["s18.a"], "i₃ = i₁ + i₂", XE, 220, 64, "g", TINTA)
        E.formula_em(c, t, C["s18.b"], "10 = 3i₁ + i₃", XE, 330, 64, "g", TINTA)
        E.formula_em(c, t, C["s18.c"], "8 = 2i₂ + i₃", XE + 520, 330, 64, "g", TINTA)
        E.sistema(c, t, C["s18.d"], ["10 = 4i₁ + i₂", "8 = i₁ + 3i₂"], XE + 40, 520, 72, tl=[C["s18.d"], C["s18.e"]])
    E.saida(c, t, C["s19"] - 0.1, s18)
    if C["s19"] <= t < C["s20"]:
        E.formula_em(c, t, C["s19.a"], "i₂ = 10 − 4i₁", XE, 240, 66, "g", COR)
        E.formula_em(c, t, C["s19.b"], "8 = i₁ + 30 − 12i₁", XE, 380, 66, "g", TINTA)
        E.formula_em(c, t, C["s19.c"], "11i₁ = 22", XE, 520, 66, "g", TINTA)
        bola_txt(c, t, C["s19.d"], "2 A", XE + 560, 495, 80, 58, CERTO)
        E.foco(c, t, C["s19.e"], 0.5, lambda a: E.formula(c, "i₂ = 10 − 8 = 2 A", XE, 700, 64, "g", CERTO, a))
        E.foco(c, t, C["s19.f"], 0.5, lambda a: E.formula(c, "i₃ = 2 + 2 = 4 A", XE, 830, 64, "g", CERTO, a))
    if t < C["s20"]:
        return
    E.frase(c, t, C["s20.a"], ps("confira pelo", "i", 66) + [("atalho", "g", 62, COR)], XE, 220, passo=0.12)
    E.formula_em(c, t, C["s20.a"] + 1.0, "f{10 − U}{3} + f{8 − U}{2} = U", XE, 400, 70, "g", TINTA)
    E.formula_em(c, t, C["s20.b"], "44 = 11U", XE, 580, 70, "g", TINTA)
    bola_txt(c, t, C["s20.c"], "4 V", XE + 580, 555, 78, 56)
    E.foco(c, t, C["s20.c"] + 0.2, 0.4, lambda a: E.formula(c, "U =", XE + 350, 578, 56, "g", TINTA, a))
    E.foco(c, t, C["s20.d"], 0.5, lambda a: E.formula(c, "meio: f{4}{1} = 4 A", XE, 790, 66, "g", CERTO, a))
    E.foco(c, t, C["s20.d"] + 1.2, 0.5, lambda a: E.selo(c, XE + 640, 770, 55, True, a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def r_():
        E.frase(c, t, C["s21"], [("resumindo", "i", 92, COR)], W / 2, 180, "center")
        itens = (("s21.a", [("corrente", "g", 62), ("com", "i", 66), ("nome", "i", 66), ("e", "i", 66), ("sentido", "g", 62, COR)]),
                 ("s21.b", [("um", "i", 66), ("nó", "g", 62), ("+", "g", 62, TINTA2), ("duas", "i", 66), ("malhas", "g", 62, COR)]),
                 ("s21.d", [("sistema", "g", 62), ("por", "i", 66), ("substituição", "g", 62, COR)]),
                 ("s21.e", [("dois", "i", 66), ("nós:", "g", 62), ("a", "i", 66), ("tensão", "g", 62, COR), ("entre", "i", 66), ("eles", "i", 66)]))
        for k, (cue, partes) in enumerate(itens):
            y = 340 + k * 160
            E.foco(c, t, C[cue], 0.5, lambda a, k=k, y=y: (E.bola(c, 300, y - 24, 48, a=a), centro(c, str(k + 1), 300, y - 2, 56, "g", BR, a)))
            E.frase(c, t, C[cue] + 0.1, partes, 400, y, passo=0.12)
    E.saida(c, t, C["s22"] - 0.1, r_)
    if t < C["s22"]:
        return
    E.frase(c, t, C["s22"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C["s22.a"], [("praticar", "g", 100, COR)], XE, 400)
    E.frase(c, t, C["s22.a"] + 0.8, ps("circuitos que não se reduzem", "i", 62), XE, 520, passo=0.1)
    E.frase(c, t, C["s22.a"] + 1.8, ps("a um resistor só", "i", 62), XE, 610, passo=0.1)
    inscreva(c, t, C["s22.b"], C["s22.c"])


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, circuito=b_circuito, sistema=b_sistema, erro=b_erro, atalho=b_atalho,
              questao=b_questao, resposta=b_resposta, fim=b_fim)
