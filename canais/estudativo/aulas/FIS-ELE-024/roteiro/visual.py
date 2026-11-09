"""Visual — Estudativo · FIS-ELE-024: leis de Kirchhoff, nós e malhas. Primeira aula do módulo Leis de Kirchhoff.

Segue a LINGUAGEM VISUAL DA FÍSICA (FIS-CIN-001), a da ELETRICIDADE (FIS-ELE-001) e a do módulo GERADORES E RECEPTORES
(FIS-ELE-020). Acrescenta, para o módulo LEIS DE KIRCHHOFF (FIS-ELE-025 e 026 copiam daqui):
- NÓ: bolinha grande em tinta; cada corrente é uma seta laranja com o valor ("5 A"); a que chega aponta para o nó, a que sai
  aponta para fora (`no_correntes`). Corrente desconhecida em tinta com "i".
- MALHA: o sentido de percurso é uma seta circular tracejada em cinza no meio da malha (`percurso`), e um ponto laranja
  anda pelo fio no tempo da fala (`anda`), passando por cada peça quando ela entra na conta.
- REGRA DE SINAIS: cada peça ganha uma etiqueta com o termo da conta (`etiqueta_termo`): termo que SOMA em laranja (o
  potencial sobe), termo que SUBTRAI em azul (F.NEG, o potencial cai). Gerador: F.pilha (placa longa = +).
- A equação da malha se monta à esquerda, termo a termo, na mesma ordem do percurso.
Todo instante vem de C[...] (marcadores do roteiro), para acompanhar a voz real quando ela chegar."""
import math

import editorial as E
import fisica as F
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Física", "Eletricidade")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_FIS-ELE-024_leis_de_kirchhoff_nos_e_malhas.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("nos", "malhas", "sinais", "exemplo", "atalho", "questao", "fim"))
BR = "#FFFFFF"
CALOR = "#D9480F"
NEG = F.NEG

# todas as contas da aula
assert 5 + 2 == 4 + 3
i = (20 - 8) / (2 + 4)
assert i == 2 and 20 - 2 * i - 8 - 4 * i == 0 and 20 - 8 == 12 == 6 * i
j = -2  # chute ao contrário (anti-horário): −20 − 4j + 8 − 2j = 0 → j = −2 A
assert -20 - 4 * j + 8 - 2 * j == 0 and (-20 + 8) / 6 == j
assert abs((20 + 8) / 6 - 4.6667) < 1e-3
assert (18 - 6) / (1 + 2 + 3) == 2 and 18 - 6 - 1 * 2 - 2 * 2 - 3 * 2 == 0


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


def anda(c, t, marcos, cor=None, r=17):
    """ponto que anda pelo fio: marcos = [(instante, (x, y))]; vai de um marco ao seguinte até o instante dele"""
    if t < marcos[0][0]:
        return
    pos = marcos[-1][1]
    for (t0, A), (t1, B) in zip(marcos, marcos[1:]):
        if t < t1:
            q = ease_io(prog(t, max(t0, t1 - 0.9), min(0.9, t1 - t0)))
            pos = (lerp(A[0], B[0], q), lerp(A[1], B[1], q))
            break
    c.drawCircle(*pos, r + 8, M.paint(E.COR, 0.25))
    c.drawCircle(*pos, r, M.paint(cor or E.COR, 1.0))


def etiqueta_termo(c, t, t0, s, x, y, soma=True, size=50):
    """o termo da conta junto da peça: laranja se soma, azul se subtrai"""
    E.foco(c, t, t0, 0.4, lambda a: pilula_f(c, s, x, y, size, fundo=E.COR if soma else NEG, a=a))


def pilula_f(c, s, cx, cy, size, fundo=None, cor=BR, a=1.0):
    """pílula com fórmula (aceita "=", "→", fração e potência)"""
    if a <= 0:
        return
    w, h = E.formula(None, s, 0, 0, size, "g", a=0) + size * 1.2, size * 1.9
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2, cy - h / 2, w, h), h / 2, h / 2), M.paint(fundo or E.COR, a))
    E.formula(c, s, cx, cy + size * 0.36, size, "g", cor, a, "center")


def malha(c, t, t0, x0, x1, yt, yb, e1, R1, e2, R2, te=None):
    """malha retangular: à esquerda o gerador e1 (+ em cima), em cima R1, à direita e2 com o + em cima (virado contra), embaixo R2.
    te = instantes de cada peça (4); devolve os cantos (BL, TL, TR, BR)"""
    te = te or [t0, t0 + 0.2, t0 + 0.4, t0 + 0.6]
    F.pilha(c, t, te[0], (x0, yb), (x0, yt), e1)
    F.resistor(c, t, te[1], (x0, yt), (x1, yt), R1)
    F.pilha(c, t, te[2], (x1, yb), (x1, yt), e2, lado=-1)
    F.resistor(c, t, te[3], (x1, yb), (x0, yb), R2)
    return (x0, yb), (x0, yt), (x1, yt), (x1, yb)


def ramos3(c, t, t0, xs, yt, yb, pecas):
    """circuito de três ramos verticais entre o nó de cima (yt) e o de baixo (yb); pecas[k] = função (A, B) que desenha o ramo k"""
    F.fio(c, t, t0, [(xs[0], yt), (xs[2], yt)])
    F.fio(c, t, t0, [(xs[0], yb), (xs[2], yb)])
    for k, x in enumerate(xs):
        pecas[k]((x, yb), (x, yt))
    if t >= t0 + 0.5:
        F.no(c, (xs[1], yt)); F.no(c, (xs[1], yb))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def um():
        malha(c, t, C["s01.a"], 1150, 1720, 180, 520, "", "", "", "")
        E.foco(c, t, C["s01.b"], 0.5, lambda a: centro(c, "?", 1435, 395, 120, "g", COR, a))
        no_correntes(c, t, (1435, 820), [(180, "", True, C["s01.c"], None), (20, "?", False, C["s01.c"] + 0.4, TINTA), (-30, "?", False, C["s01.c"] + 0.6, TINTA)], L=200)
        E.frase(c, t, C["s01.a"], ps("bateria virada", "i", 72) + [("contra", "g", 70, COR)], XE, 250, passo=0.12)
        E.frase(c, t, C["s01.b"], [("soma", "g", 80), ("ou", "i", 84), ("subtrai?", "g", 80, COR)], XE, 380, passo=0.14)
        E.frase(c, t, C["s01.c"], ps("num cruzamento de fios:", "i", 64), XE, 560, passo=0.1)
        E.frase(c, t, C["s01.c"] + 1.5, ps("quanto vai para cada lado?", "g", 60), XE, 660, passo=0.1)
        E.frase(c, t, C["s01.d"], ps("duas regras:", "i", 72), XE, 860)
        E.frase(c, t, C["s01.e"], ps("leis de", "i", 80) + [("Kirchhoff", "g", 84, COR)], XE, 980, passo=0.14)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t >= C["s02"]:
        promessa(c, t, C, "s02", (("s02.a", "a lei dos nós", 1.4), ("s02.b", "a lei das malhas", 0), ("s02.c", "a regra de sinais", 0)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    lembrete(c, t, C, "s03", (("s03.b", "nó: a corrente se divide ou se junta", "ramo: o caminho entre dois nós"),
                              ("s03.c", "tensão num resistor", "U = R · i"),
                              ("s03.d", "gerador e receptor", "U = ε − r · i      U = ε′ + r′ · i")))


# ---------------- lei dos nós ----------------
def cano(c, t, t0, a=1.0):
    """cano em Y com água azul que se divide"""
    q = ep(t, t0, 0.5) * a
    if q <= 0:
        return
    for pts in (((1000, 560), (1380, 560)), ((1380, 560), (1760, 420)), ((1380, 560), (1760, 700))):
        M.line(c, *pts[0], *pts[1], "#8C8C96", q, 64)
        M.line(c, *pts[0], *pts[1], "#4BA3E3", q, 40)
    for k in range(9):
        s = ((t - t0) * 0.6 + k / 9) % 1.0
        if s < 0.5:
            x, y = lerp(1000, 1380, s * 2), 560
        else:
            u = (s - 0.5) * 2
            y_ = 420 if k % 2 else 700
            x, y = lerp(1380, 1760, u), lerp(560, y_, u)
        c.drawCircle(x, y, 9, M.paint(BR, 0.8 * q))


def b_nos(c, t, C, b):
    def s04():
        E.frase(c, t, C["s04.a"], ps("1ª lei: a lei dos", "i", 76) + [("nós", "g", 80, COR)], XE, 220, passo=0.12)
        E.frase(c, t, C["s04.b"], ps("soma do que", "i", 66) + [("chega", "g", 64, COR)], XE, 380, passo=0.12)
        E.frase(c, t, C["s04.b"] + 1.4, [("=", "g", 66, TINTA2)] + ps("soma do que", "i", 66) + [("sai", "g", 64, COR)], XE, 480, passo=0.12)
        E.frase(c, t, C["s04.c"], ps("carga não some", "g", 60) + ps("nem se acumula", "g", 60), XE, 700, passo=0.1)
        cano(c, t, C["s04.d"])
        E.foco(c, t, C["s04.d"] + 0.4, 0.4, lambda a: centro(c, "água num cano que se divide", 1380, 860, 52, "i", TINTA2, a))
    E.saida(c, t, C["s05"] - 0.1, s04)
    if t < C["s05"]:
        return
    P = (1360, 560)
    no_correntes(c, t, P, [(150, "5 A", True, C["s05.a"], None), (210, "2 A", True, C["s05.a"] + 0.6, None),
                           (30, "4 A", False, C["s05.b"], None), (-30, "i", False, C["s05.b"] + 0.6, TINTA)], L=260, size=60)
    E.frase(c, t, C["s05"], [("exemplo", "i", 74, COR)], XE, 220)
    E.frase(c, t, C["s05.a"], ps("chegam:", "i", 66) + [("5", "g", 64), ("e", "i", 66), ("2", "g", 64)], XE, 380, passo=0.12)
    E.frase(c, t, C["s05.b"], ps("saem:", "i", 66) + [("4", "g", 64), ("e", "i", 66), ("i", "g", 64)], XE, 490, passo=0.12)
    E.formula_em(c, t, C["s05.c"], "5 + 2 = 4 + i", XE, 700, 96, "g", TINTA)
    bola_txt(c, t, C["s05.d"], "3 A", XE + 280, 880, 100, 70)


# ---------------- lei das malhas ----------------
def morro(c, t, t0, x0, y0, w, h):
    """trilha que sobe o morro e volta ao começo"""
    q = ease_io(prog(t, t0, 1.2))
    if q <= 0:
        return
    pts = [(x0 + w * k / 40, y0 - h * math.sin(math.pi * k / 40) ** 2) for k in range(41)]
    p = skia.Path(); p.moveTo(x0, y0)
    for P_ in pts:
        p.lineTo(*P_)
    p.lineTo(x0 + w, y0 + 40); p.lineTo(x0, y0 + 40); p.close()
    c.drawPath(p, M.paint("#CFE3C8", q))
    F.poli(c, pts, q, "#2F7A3B", 1.0, 6)
    k = int(min(40, q * 40))
    c.drawCircle(*pts[k], 18, M.paint(E.COR, 1.0))


def b_malhas(c, t, C, b):
    def s06():
        E.frase(c, t, C["s06.a"], ps("2ª lei: a lei das", "i", 76) + [("malhas", "g", 80, COR)], XE, 220, passo=0.12)
        E.frase(c, t, C["s06.b"], [("malha", "g", 66)] + ps("= caminho fechado", "i", 66), XE, 380, passo=0.12)
        malha(c, t, C["s06.b"], 1050, 1700, 260, 760, "", "", "", "")
        percurso(c, t, C["s06.c"], 1375, 510, 130, rot="volta")
        anda(c, t, [(C["s06.c"], (1050, 760)), (C["s06.c"] + 1.2, (1050, 260)), (C["s06.c"] + 2.4, (1700, 260)), (C["s06.c"] + 3.6, (1700, 760)),
                    (C["s06.c"] + 4.8, (1050, 760))])
        E.frase(c, t, C["s06.c"], ps("volta inteira:", "i", 66), XE, 600)
        E.frase(c, t, C["s06.c"] + 1.0, ps("sobe e desce", "i", 62) + [("=", "g", 62, TINTA2), ("0", "g", 76, COR)], XE, 720, passo=0.12)
    E.saida(c, t, C["s07"] - 0.1, s06)
    if t < C["s07"]:
        return
    E.frase(c, t, C["s07.a"], ps("cada ponto tem um", "i", 66) + [("potencial", "g", 64, COR)], XE, 230, passo=0.12)
    E.frase(c, t, C["s07.b"], ps("mesmo ponto,", "i", 66) + ps("mesmo potencial", "g", 64), XE, 360, passo=0.12)
    morro(c, t, C["s07.c"], 300, 880, 1300, 380)
    E.frase(c, t, C["s07.d"], ps("o que subiu,", "i", 70) + [("desceu", "g", 68, COR)], W / 2 + 200, 560, "left", 0.12)


# ---------------- regra de sinais ----------------
def b_sinais(c, t, C, b):
    E.frase(c, t, C["s08"], ps("a regra de", "i", 76) + [("sinais", "g", 76, COR)], XE, 190, passo=0.12)
    E.frase(c, t, C["s08.a"], ps("escolha o sentido da corrente e ande nele", "i", 56, TINTA2), XE, 290, passo=0.08)
    y1, y2 = 470, 800
    # gerador: do − para o + soma; do + para o − subtrai
    for k, (cue, soma) in enumerate((("s08.b", True), ("s08.d", False))):
        x0 = 220 + 760 * k
        F.pilha(c, t, C[cue], (x0, y1), (x0 + 360, y1), None)
        E.foco(c, t, C[cue] + 0.3, 0.4, lambda a, x0=x0, soma=soma: F.seta(c, x0 + (0 if soma else 360), y1 + 90, x0 + (360 if soma else 0), y1 + 90,
                                                                            TINTA2, a, 6))
        E.foco(c, t, C[cue] + 0.3, 0.4, lambda a, x0=x0, soma=soma: centro(c, "entra pelo " + ("−" if soma else "+"), x0 + 180, y1 + 170, 44, "b", TINTA2, a))
        etiqueta_termo(c, t, C["s08.c"] if soma else C["s08.d"] + 0.5, "+ ε" if soma else "− ε", x0 + 520, y1, soma, 56)
    for k, (cue, soma) in enumerate((("s09.a", False), ("s09.c", True))):
        x0 = 220 + 760 * k
        F.resistor(c, t, C[cue], (x0, y2), (x0 + 360, y2), None)
        F.seta(c, x0 + 80, y2 - 70, x0 + 280, y2 - 70, E.COR, ep(t, C[cue] + 0.2, 0.4), 8) if t >= C[cue] + 0.2 else None
        E.foco(c, t, C[cue] + 0.2, 0.4, lambda a, x0=x0: E.escreve(c, "i", x0 + 300, y2 - 60, 44, "g", COR, a))
        E.foco(c, t, C[cue] + 0.3, 0.4, lambda a, x0=x0, soma=soma: F.seta(c, x0 + (360 if soma else 0), y2 + 70, x0 + (0 if soma else 360), y2 + 70,
                                                                            TINTA2, a, 6))
        E.foco(c, t, C[cue] + 0.3, 0.4, lambda a, x0=x0, soma=soma: centro(c, "contra a corrente" if soma else "a favor da corrente", x0 + 180, y2 + 150, 44,
                                                                            "b", TINTA2, a))
        etiqueta_termo(c, t, C["s09.b"] if not soma else C["s09.c"] + 0.4, "+ R · i" if soma else "− R · i", x0 + 560, y2, soma, 52)


# ---------------- exemplo ----------------
def b_exemplo(c, t, C, b):
    x0, x1, yt, yb = 1150, 1650, 330, 780
    BL, TL, TR, BR_ = malha(c, t, C["s10"], x0, x1, yt, yb, "20 V", "2 Ω", "8 V", "4 Ω", te=[C["s10.a"], C["s10.b"], C["s10.c"], C["s10.d"]])
    horario = t < C["s13"]
    if t < C["s13"]:
        percurso(c, t, C["s11"], 1400, 555, 100, rot="i")
        F.corrente(c, t, C["s11"] + 0.3, [(x0 + 60, yb - 60), (x0 + 60, yt + 60), (x1 - 60, yt + 60), (x1 - 60, yb - 60)], espaco=200)
        anda(c, t, [(C["s11"], BL), (C["s11.a"], TL), (C["s11.b"], TR), (C["s11.c"], BR_), (C["s11.d"], BL)])
    for cue, s, soma, P in (("s11.a", "+20", True, (x0 - 110, 660)), ("s11.b", "− 2i", False, (1590, yt - 70)),
                            ("s11.c", "− 8", False, (x1 + 110, 660)), ("s11.d", "− 4i", False, (1590, yb + 75))):
        if t < C["s13"]:
            etiqueta_termo(c, t, C[cue], s, *P, soma=soma)

    def eq():
        E.frase(c, t, C["s10"], [("exemplo", "i", 74, COR)], XE, 200)
        E.foco(c, t, C["s11"] + 0.2, 0.4, lambda a: E.escreve(c, "saindo do − do gerador de 20", XE, 300, 46, "i", TINTA2, a))
        xs = E.linha(c, t, [("+20", "g", 70, COR, C["s11.a"]), ("− 2i", "g", 70, NEG, C["s11.b"]), ("− 8", "g", 70, NEG, C["s11.c"]),
                            ("− 4i", "g", 70, NEG, C["s11.d"]), ("= 0", "g", 70, TINTA, C["s11.e"])], XE, 440)
        E.foco(c, t, C["s12.a"], 0.5, lambda a: E.formula(c, "12 = 6i", XE, 600, 90, "g", TINTA, a))
        bola_txt(c, t, C["s12.b"], "2 A", XE + 480, 570, 95, 68)
        E.frase(c, t, C["s12.c"], ps("a de 8 V: a corrente entra pelo +", "i", 50), XE, 780, passo=0.08)
        E.foco(c, t, C["s12.d"], 0.5, lambda a: E.pilula(c, "receptor: está sendo carregada", XE + 360, 880, 42, "g", fundo=TINTA, a=a))
    E.saida(c, t, C["s13"] - 0.1, eq)
    if t < C["s13"]:
        return
    percurso(c, t, C["s13.a"], 1400, 555, 100, horario=False, rot="chute")
    E.frase(c, t, C["s13.a"], ps("e se o chute fosse", "i", 70) + [("ao", "g", 66), ("contrário?", "g", 66, COR)], XE, 260, passo=0.12)
    E.foco(c, t, C["s13.b"], 0.5, lambda a: E.formula(c, "i = −2 A", XE, 460, 110, "g", NEG, a))
    E.frase(c, t, C["s13.c"], [("−", "g", 76, NEG)] + ps("= o sentido real é o oposto", "i", 62), XE, 660, passo=0.12)
    E.frase(c, t, C["s13.d"], ps("o valor,", "i", 66) + [("2", "g", 66, CERTO), ("A,", "b", 50, F.UNID)] + ps("continua certo", "g", 62, CERTO), XE, 820, passo=0.12)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s14"], [("cuidado", "g", 96, ERRADO)], XE, 210)
    E.frase(c, t, C["s14.a"], ps("sinal do gerador pela", "i", 70) + [("corrente", "g", 66)], XE, 350, passo=0.12)
    if t >= C["s14.b"]:
        E.risco(c, XE - 10, 370, XE + 960, 300, t, C["s14.b"], largura=12)
    E.frase(c, t, C["s14.b"], ps("o sinal depende do", "i", 66) + [("polo", "g", 64, COR)] + ps("por onde você entra", "i", 66), XE, 500, passo=0.1)
    E.foco(c, t, C["s14.c"], 0.5, lambda a: E.formula(c, "+20 − 2i + 8 − 4i = 0", XE, 680, 76, "g", TINTA, a))
    E.foco(c, t, C["s14.c"] + 1.2, 0.5, lambda a: E.formula(c, "i = f{28}{6}", XE, 860, 80, "g", ERRADO, a))
    E.foco(c, t, C["s14.d"], 0.5, lambda a: E.formula(c, "≈ 4,7 A", XE + 330, 860, 80, "g", ERRADO, a))
    if t >= C["s14.d"] + 0.6:
        E.risco(c, XE - 10, 880, XE + 650, 780, t, C["s14.d"] + 0.6, largura=12)
    F.pilha(c, t, C["s14.c"], (1500, 820), (1500, 380), "8 V", lado=-1)
    F.seta(c, 1400, 330, 1400, 520, TINTA2, ep(t, C["s14.c"] + 0.4, 0.4), 6) if t >= C["s14.c"] + 0.4 else None
    E.foco(c, t, C["s14.c"] + 0.5, 0.4, lambda a: E.escreve(c, "entra pelo +", 1180, 300, 44, "b", TINTA2, a))
    etiqueta_termo(c, t, C["s14.c"] + 0.6, "+8 ?", 1720, 520, True, 50)
    etiqueta_termo(c, t, C["s14.d"] + 1.0, "− 8", 1720, 700, False, 50)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    E.frase(c, t, C["s15"], ps("o atalho:", "i", 72, CLARO) + ps("uma malha só", "g", 68, BR), W / 2, 170, "center", 0.12)
    E.formula_em(c, t, C["s15.a"], "i = f{ε a favor − ε contra}{soma de todas as resistências}", W / 2, 420, 84, "g", BR, "center")
    E.formula_em(c, t, C["s15.c"], "f{20 − 8}{2 + 4} = 2 A", W / 2, 680, 90, "g", CLARO, "center")
    E.frase(c, t, C["s15.d"], ps("é a lei das malhas", "i", 60, CLARO) + ps("já arrumada", "g", 58, BR), W / 2, 860, "center", 0.12)
    E.frase(c, t, C["s15.e"], [("não", "g", 56, ERRADO), ("serve:", "i", 60, CLARO)] + ps("mais de uma malha (próxima aula)", "i", 60, CLARO), W / 2, 980, "center", 0.1)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s16"], ps("hora de testar", "i", 72, COR), XE, 200)
    E.frase(c, t, C["s16.a"], ps("dois geradores", "i", 64) + [("um", "g", 62), ("contra", "g", 62, COR), ("o", "g", 62), ("outro", "g", 62)], XE, 340, passo=0.1)
    E.frase(c, t, C["s16.b"], [("18", "g", 64), ("V", "b", 48, F.UNID), ("e", "i", 64), ("6", "g", 64), ("V", "b", 48, F.UNID)], XE, 440, passo=0.1)
    E.frase(c, t, C["s16.c"], ps("resistores:", "i", 64) + [("1,", "g", 64), ("2", "g", 64), ("e", "i", 64), ("3", "g", 64), ("Ω", "b", 48, F.UNID)], XE, 540, passo=0.1)
    E.frase(c, t, C["s16.d"], ps("corrente?", "g", 66, COR), XE, 700)
    E.frase(c, t, C["s16.e"], ps("em qual gerador ela", "i", 62) + ps("entra pelo +?", "g", 60, COR), XE, 810, passo=0.1)
    if t < C["s17"]:
        x0, x1, yt, yb = 1100, 1680, 320, 780
        F.pilha(c, t, C["s16.b"], (x0, yb), (x0, yt), "18 V")
        F.resistor(c, t, C["s16.c"], (x0, yt), (x1, yt), "1 Ω")
        F.pilha(c, t, C["s16.b"] + 0.3, (x1, yb), (x1, yt), "6 V", lado=-1)
        F.fio(c, t, C["s16.c"], [(x1, yb), (1520, yb)])
        F.resistor(c, t, C["s16.c"] + 0.2, (1520, yb), (1300, yb), "2 Ω")
        F.resistor(c, t, C["s16.c"] + 0.4, (1300, yb), (x0, yb), "3 Ω")
    else:
        E.relogio(c, t, C["s17.a"], cx=1460, cy=440, r=200)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    E.frase(c, t, C["s18.a"], ps("o de", "i", 70) + [("18", "g", 70, COR), ("V", "b", 52, F.UNID)] + ps("vence", "g", 66), XE, 230, passo=0.12)
    E.foco(c, t, C["s18.b"], 0.5, lambda a: E.formula(c, "18 − 6 − 1i − 2i − 3i = 0", XE, 420, 80, "g", TINTA, a))
    E.foco(c, t, C["s18.c"], 0.5, lambda a: E.formula(c, "12 = 6i", XE, 590, 90, "g", TINTA, a))
    bola_txt(c, t, C["s18.d"], "2 A", XE + 480, 560, 95, 68, CERTO)
    E.frase(c, t, C["s19.a"], ps("no gerador de", "i", 66) + [("6", "g", 66), ("V,", "b", 50, F.UNID)] + ps("ela entra pelo +", "i", 66), XE, 800, passo=0.1)
    E.foco(c, t, C["s19.b"], 0.5, lambda a: E.pilula(c, "funciona como receptor", XE + 330, 920, 50, "g", fundo=TINTA, a=a))
    x0, x1, yt, yb = 1180, 1680, 330, 760
    F.pilha(c, t, C["s18.a"], (x0, yb), (x0, yt), "18 V")
    F.resistor(c, t, C["s18.a"], (x0, yt), (x1, yt), "1 Ω")
    F.pilha(c, t, C["s18.a"], (x1, yb), (x1, yt), "6 V", lado=-1)
    F.fio(c, t, C["s18.a"], [(x1, yb), (1560, yb)])
    F.resistor(c, t, C["s18.a"], (1560, yb), (1380, yb), "2 Ω")
    F.resistor(c, t, C["s18.a"], (1380, yb), (x0, yb), "3 Ω")
    F.corrente(c, t, C["s18.a"] + 0.4, [(x0 + 60, yb - 60), (x0 + 60, yt + 60), (x1 - 60, yt + 60), (x1 - 60, yb - 60)], espaco=200)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def r_():
        resumo(c, t, C, "s20", (("s20.a", [("nó:", "g", 66), ("chega", "i", 70), ("=", "g", 66, TINTA2), ("sai", "i", 70)]),
                               ("s20.b", [("malha:", "g", 66), ("a", "i", 70), ("volta", "i", 70), ("soma", "i", 70), ("zero", "g", 66, COR)]),
                               ("s20.c", [("sinal:", "g", 66), ("o", "i", 70), ("polo", "g", 66, COR), ("por", "i", 70), ("onde", "i", 70), ("você", "i", 70),
                                          ("entra", "i", 70)])))
    E.saida(c, t, C["s21"] - 0.1, r_)
    if t < C["s21"]:
        return
    E.frase(c, t, C["s21"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C["s21.a"], ps("duas", "i", 90) + [("malhas", "g", 94, COR)], XE, 400, passo=0.14)
    E.frase(c, t, C["s21.b"], ps("e um", "i", 80) + [("sistema", "g", 84)], XE, 530, passo=0.14)
    yt, yb = 680, 960
    ramos3(c, t, C["s21.a"] + 0.4, (300, 640, 980), yt, yb,
           [lambda A, B: F.pilha(c, t, C["s21.a"] + 0.6, A, B, None), lambda A, B: F.resistor(c, t, C["s21.a"] + 0.7, A, B, None),
            lambda A, B: F.pilha(c, t, C["s21.a"] + 0.8, A, B, None)])
    inscreva(c, t, C["s21.c"], C["s21.d"])


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, nos=b_nos, malhas=b_malhas, sinais=b_sinais, exemplo=b_exemplo,
              erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
