"""Visual — Estudativo · MAT-EST-011: moda e mediana.
Mesma linguagem da Estatística definida em MAT-EST-001 (docstring de lá): lista de dados = fichas brancas que acendem na cor
da matéria quando contam; tabela (quadro(), com o transporte de MAT-EST-002 nas mesmas cores); conta da vez à direita,
resposta na esfera; atalho no palco escuro.
Novo nesta aula (para copiar nas próximas):
- ORDENAR = AS FICHAS TROCAM DE LUGAR (notas()): cada ficha anda em arco até a sua posição na lista em ordem; as que vão para a
  direita passam por cima, as que vão para a esquerda, por baixo.
- MEDIANA = A FICHA DO MEIO ACESA, com colchetes "metade" de cada lado (metades()). Na fila de pessoas por altura (fila()), a
  pessoa do meio fica na cor da matéria.
- POSIÇÃO = RÉGUA DE CASAS NUMERADAS (regua()), com a casa do meio acesa.
Sem voz ainda: todo instante vem de C[...] (marcadores do roteiro), para acompanhar a voz real quando ela chegar."""
import math
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Estatística")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-EST-011_moda_e_mediana.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("mediana", "par", "moda", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
PAPEL = E.PAPEL
CATS = E._paleta(4)    # ônibus, carro, bicicleta, a pé (as cores de MAT-EST-002)
GANCHO = [7, 2, 9, 4, 5]
PAR = [3, 8, 5, 9]
MODA = [6, 7, 8, 7, 5, 7, 9, 8]
QUEST = [7, 4, 9, 6, 9, 3, 8, 10]
assert sorted(GANCHO) == [2, 4, 5, 7, 9] and sorted(PAR) == [3, 5, 8, 9] and (5 + 8) / 2 == 6.5 and (3 + 9) / 2 == 6
assert MODA.count(7) == 3 and MODA.count(8) == 2 and all(MODA.count(v) == 1 for v in (5, 6, 9))
assert sorted(QUEST) == [3, 4, 6, 7, 8, 9, 9, 10] and (8 + 1) / 2 == 4.5 and (7 + 8) / 2 == 7.5 and QUEST.count(9) == 2
assert (11 + 1) / 2 == 6 and (10 + 1) / 2 == 5.5


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças comuns ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    """uma frase, palavra a palavra (palavra com %, ², ³ ou → vai na grotesca)"""
    return [(w, "g" if any(ch in w for ch in "%²³→") else est, size * (0.92 if any(ch in w for ch in "%²³→") and est != "g" else 1), cor) for w in txt.split()]


def fcen(c, t, t0, s, cx, y, size, cor=None):
    E.formula_em(c, t, t0, s, cx, y, size, "g", cor, "center")


def bola_txt(c, t, t0, s, cx, cy, r, size, cor=None):
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r * ease_back(prog(t, t0, 0.5)), cor, a),
                                     E.formula(c, s, cx, cy + size * 0.36, size, "g", E.SOBRE, a, "center")))


def fase(c, t, t0, t1, fn):
    if t0 - 0.01 <= t < t1 + 0.4:
        E.saida(c, t, t1, fn)


def _cel(c, s, cx, y, size, estilo, cor, a):
    if callable(s):
        s(c, cx, y, size, cor, a)
    else:
        centro(c, s, cx, y, size, estilo, cor, a)


def quadro(c, t, x, y, colunas, linhas, total=None, size=58, h_lin=None, cores=None, t_fio=None):
    """tabela de dados que entra coluna a coluna. colunas = [(título, largura, t0)]; linhas = [[(texto, t0[, cor]), ...], ...];
    total = [(texto, t0[, cor]), ...] depois de um fio grosso; cores = cor de cada linha (bolinha antes da 1ª coluna)."""
    h_lin = h_lin or size * 1.55
    xs = [x]
    for _, w, _ in colunas:
        xs.append(xs[-1] + w)
    larg = xs[-1] - x
    t_cab = min(ti for _, _, ti in colunas)
    p = ease_io(prog(t, t_fio if t_fio is not None else t_cab, 0.6))
    if p > 0:
        M.line(c, x, y + 20, x + larg * p, y + 20, TINTA, 1, 3)
    for k, (tit, w, ti) in enumerate(colunas):
        cx = xs[k] + w / 2
        E.foco(c, t, ti, 0.45, lambda a, tit=tit, cx=cx: centro(c, tit, cx, y - 6, size * 0.78, "i", TINTA2, a))
    bases = []
    for j, lin in enumerate(linhas):
        yy = y + 20 + h_lin * (j + 1) - h_lin * 0.3
        bases.append(yy)
        for k, cel in enumerate(lin):
            s, ti, *cc = cel
            if s == "":
                continue
            cx = xs[k] + colunas[k][1] / 2
            if k == 0 and cores:
                E.foco(c, t, ti, 0.4, lambda a, yy=yy, j=j: c.drawCircle(xs[0] + 22, yy - size * 0.34, size * 0.24, M.paint(cores[j], a)))
                cx += 22
            E.foco(c, t, ti, 0.4, lambda a, s=s, cx=cx, yy=yy, cc=cc, k=k: _cel(c, s, cx, yy, size, "b" if k == 0 else "g", cc[0] if cc else TINTA, a))
    if total:
        yf = y + 20 + h_lin * len(linhas) + 8
        tt = min(cel[1] for cel in total if cel[0] != "")
        q = ease_io(prog(t, tt, 0.5))
        if q > 0:
            M.line(c, x, yf, x + larg * q, yf, TINTA, 1, 6)
        yy = yf + h_lin * 0.72
        bases.append(yy)
        for k, cel in enumerate(total):
            s, ti, *cc = cel
            if s == "":
                continue
            cx = xs[k] + colunas[k][1] / 2 + (22 if k == 0 and cores else 0)
            E.foco(c, t, ti, 0.4, lambda a, s=s, cx=cx, cc=cc, k=k: centro(c, s, cx, yy, size, "i" if k == 0 else "g", cc[0] if cc else TINTA, a))
    return bases


def ficha(c, s, cx, cy, size, a=1.0, cor=None, borda=None):
    """um dado da lista: pílula branca com borda fina (cor = fundo aceso)"""
    if a <= 0:
        return
    w = E.larg(s, "b", size) + size * 1.1
    h = size * 1.55
    rr = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2, cy - h / 2, w, h), h / 2, h / 2)
    c.drawRRect(rr, M.paint(cor or BR, a))
    c.drawRRect(rr, M.paint(borda or (cor or FIO), a, stroke=3))
    centro(c, s, cx, cy + size * 0.36, size, "b", (BR if cor and M.lum(cor) < 0.5 else TINTA), a)


def camisa(c, cx, cy, s, num="", a=1.0, cor=None):
    """camisa (a mesma de MAT-EST-001)"""
    if a <= 0:
        return
    k = s / 100
    p = skia.Path()
    pts = [(-40, -60), (-15, -70), (0, -58), (15, -70), (40, -60), (75, -30), (55, -5), (40, -18), (40, 70), (-40, 70), (-40, -18), (-55, -5), (-75, -30)]
    p.moveTo(cx + pts[0][0] * k, cy + pts[0][1] * k)
    for px, py in pts[1:]:
        p.lineTo(cx + px * k, cy + py * k)
    p.close()
    c.drawPath(p, M.paint(cor or E.COR, a))
    c.drawPath(p, M.paint(TINTA, a, stroke=5))
    if num:
        centro(c, num, cx, cy + 34 * k, 72 * k, "g", BR, a)


# ================= peças da mediana (copiar nas próximas aulas) =================
def notas(c, t, t0, vals, cx, y, size=76, passo=None, t_ordem=None, acesas=None, d=1.0, d_ent=0.1):
    """lista de fichas numa linha centrada em cx. t_ordem: cada ficha anda em arco até o seu lugar na lista em ordem.
    acesas = {índice original: [(t, cor), ...]} (a última com t <= agora vale; cor None apaga). Devolve slot(k) = x da k-ésima casa"""
    n = len(vals)
    passo = passo or size * 2.3
    x0 = cx - passo * (n - 1) / 2
    ordem = sorted(range(n), key=lambda i: (vals[i], i))
    lugar = {i: k for k, i in enumerate(ordem)}
    q = ease_io(prog(t, t_ordem, d)) if t_ordem is not None else 0.0
    for i, v in enumerate(vals):
        xa, xb = x0 + passo * i, x0 + passo * lugar[i]
        px = lerp(xa, xb, q)
        py = y - (1 if xb > xa else -1) * size * 1.6 * math.sin(math.pi * q) * (0 if xa == xb else 1)
        cor = None
        for ti, cc in (acesas or {}).get(i, []):
            if t >= ti:
                cor = cc
        E.foco(c, t, t0 + d_ent * i, 0.4, lambda a, s=E._num(v), px=px, py=py, cor=cor: ficha(c, s, px, py, size, a, cor), sobe=10)
    return lambda k: x0 + passo * k


def metades(c, t, t0, x0, x1, x2, x3, y, rot1="metade", rot2="metade", cor=None, size=46):
    """colchetes embaixo das fichas: de x0 a x1 e de x2 a x3, com o rótulo de cada lado"""
    p = ep(t, t0, 0.5)
    if p <= 0:
        return
    for xa, xb, s in ((x0, x1, rot1), (x2, x3, rot2)):
        E.chave(c, xa, xb, y, cor or TINTA2, p, 26, 5)
        E.foco(c, t, t0 + 0.2, 0.4, lambda a, xa=xa, xb=xb, s=s: centro(c, s, (xa + xb) / 2, y + 26 + size * 1.25, size, "i", cor or TINTA2, a))


def pessoa(c, cx, base, h, cor, a=1.0):
    """uma pessoa de altura h (cabeça e corpo), em pé na linha base"""
    if a <= 0:
        return
    r = h * 0.14
    c.drawCircle(cx, base - h + r, r, M.paint(cor, a))
    M.rrect(c, cx - h * 0.17, base - h + 2.25 * r, h * 0.34, h - 2.25 * r, h * 0.12, cor, a)


def fila(c, t, t0, alturas, cx, base, passo, t_ordem=None, meio=None, a=1.0):
    """fila de pessoas; em t_ordem trocam de lugar até ficarem da menor para a maior; meio = instante em que a do meio acende"""
    n = len(alturas)
    x0 = cx - passo * (n - 1) / 2
    ordem = sorted(range(n), key=lambda i: alturas[i])
    lugar = {i: k for k, i in enumerate(ordem)}
    q = ease_io(prog(t, t_ordem, 1.2)) if t_ordem is not None else 0.0
    for i, h in enumerate(alturas):
        px = lerp(x0 + passo * i, x0 + passo * lugar[i], q)
        k = ease_back(prog(t, t0 + 0.08 * i, 0.5))
        acesa = meio is not None and lugar[i] == n // 2 and t >= meio
        if k > 0:
            pessoa(c, px, base, h * min(1.0, k), E.COR if acesa else E.mix(TINTA2, PAPEL, 0.35), a)
    p = ep(t, t0, 0.5)
    if p > 0:
        M.line(c, x0 - passo * 0.6, base, x0 + passo * (n - 0.4), base, TINTA, p * a, 4)


def regua(c, t, t0, n, cx, y, acesas=(), t_acende=None, lado=88, escuro=True, d=0.04):
    """régua de n casas numeradas (1 a n); as casas em acesas ficam na cor da matéria a partir de t_acende. Devolve x(k) do centro da casa k (1..n)"""
    gap = 12
    x0 = cx - (n * lado + (n - 1) * gap) / 2
    tinta = BR if escuro else TINTA
    xk = lambda k: x0 + (k - 1) * (lado + gap) + lado / 2
    for k in range(1, n + 1):
        def um(a, k=k):
            acesa = k in acesas and t_acende is not None and t >= t_acende
            r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(xk(k) - lado / 2, y - lado / 2, lado, lado), 14, 14)
            if acesa:
                c.drawRRect(r, M.paint(E.COR if not escuro else CLARO, a))
            c.drawRRect(r, M.paint(tinta, a * (1 if acesa else 0.7), stroke=3))
            centro(c, str(k), xk(k), y + lado * 0.2, lado * 0.5, "g", (E.SOBRE if not escuro else "#07070F") if acesa else tinta, a)
        E.foco(c, t, t0 + d * k, 0.4, um, sobe=8)
    return xk


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    a1, b1, c1 = C["s01.a"], C["s01.b"], C["s01.c"]

    def um():
        E.frase(c, t, a1, ps("cinco notas:", "i", 70) + ps("qual é a", "i", 70) + [("do meio?", "g", 76, COR)], W / 2, 220, "center", 0.1)
        ac = {2: [(b1, ERRADO), (c1, None)], 4: [(c1 + 1.3, CERTO)]}
        slot = notas(c, t, a1 + 0.6, GANCHO, W / 2, 470, 96, 250, t_ordem=c1 + 0.2, acesas=ac)
        p = ep(t, b1, 0.4) * (1 - ep(t, c1, 0.4))
        if p > 0:
            E.cursor(c, slot(2) + 20, 560, p)
        E.foco(c, t, b1 + 0.3, 0.4, lambda a: centro(c, "o 9? armadilha", W / 2, 720, 60, "g", ERRADO, a * (1 - ep(t, c1, 0.4))))
        E.frase(c, t, c1, ps("antes de achar o meio:", "i", 64) + [("em ordem", "g", 70, COR)], W / 2, 760, "center", 0.1)
    E.saida(c, t, C["s02"] - 0.1, um)

    if t >= C["s02"]:
        ta, tb = C["s02.a"], C["s02.b"]
        E.foco(c, t, tb - 0.2, 0.7, lambda a: E.bola(c, 1560, 600, 240 * ease_back(prog(t, tb - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, ps("até o fim desta aula", "i", 88), XE, 260, passo=0.14)
        E.frase(c, t, ta + 1.4, ps("o valor do", "i", 84) + [("meio", "g", 96, COR)], XE, 410, passo=0.14)
        E.frase(c, t, ta + 2.6, ps("e o valor", "i", 84) + [("mais comum", "g", 96, COR)], XE, 550, passo=0.14)
        E.frase(c, t, ta + 4.2, ps("de qualquer lista", "i", 70, TINTA2), XE, 680, passo=0.14)
        E.foco(c, t, tb + 0.1, 0.5, lambda a: (centro(c, "+ atalho", 1560, 575, 80, "g", E.SOBRE, a),
                                               centro(c, "de prova", 1560, 660, 80, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"] + 0.3, ps("você precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "2", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 980, 820
    itens = (("s03.b", "a média aritmética:", "soma ÷ quantidade"), ("s03.c", "a frequência absoluta:", "quantas vezes aparece"))
    for i, (k, l1, l2) in enumerate(itens):
        y = 240 + i * 280
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 230, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, ps(l1, "i", 56), x + 44, y + 90, "left", 0.1)
        E.formula_em(c, t, C[k] + 0.6, l2, x + 44, y + 180, 60, "g", COR)
    alvo = [240 + i * 280 + 200 for i in range(2)]
    q1 = ease_io(prog(t, C["s03.c"] - 0.35, 0.5))
    E.cursor(c, x + w - 30, lerp(alvo[0], alvo[1], q1), ep(t, C["s03.b"], 0.4))
    E.frase(c, t, lerp(C["s03.c"], C["s03.end"], 0.72), ps("faltou?", "i", 54, COR) + ps("procure no canal", "i", 54), x, 900, "left", 0.1)


# ---------------- mediana (quantidade ímpar) ----------------
ALTURAS = [190, 150, 230, 170, 250, 135, 210]


def b_mediana(c, t, C, b):
    a4, b4, c4, d4 = (C[f"s04.{k}"] for k in "abcd")
    a5, b5, c5 = C["s05.a"], C["s05.b"], C["s05.c"]

    def um():
        E.frase(c, t, a4, [("mediana", "g", 90, COR)] + ps("= o valor do meio", "i", 76), W / 2, 200, "center", 0.1)
        E.frase(c, t, b4, ps("com os dados", "i", 56) + [("em ordem,", "g", 60, COR)] + ps("do menor para o maior", "i", 56), W / 2, 290, "center", 0.08)
        passo = 170
        fila(c, t, a4 + 0.4, ALTURAS, W / 2, 760, passo, t_ordem=b4 + 0.6, meio=c4)
        x0 = W / 2 - passo * 3
        metades(c, t, c4 + 0.3, x0 - 50, x0 + 2 * passo + 50, x0 + 4 * passo - 50, x0 + 6 * passo + 50, 790, "metade", "metade")
        E.foco(c, t, d4, 0.4, lambda a: E.pilula(c, "a altura do meio = mediana", W / 2, 960, 50, "g", a=a, cor=E.SOBRE))
        if t >= d4:
            k = ease_back(prog(t, d4, 0.4))
            M.arrow(c, W / 2, 430, W / 2, 520, E.COR, k, 6, 18, k)
    fase(c, t, C["s04"], C["s05"] - 0.1, um)
    if t < C["s05"] - 0.1:
        return
    E.frase(c, t, C["s05"] + 0.2, ps("nas notas do começo,", "i", 64) + [("em ordem", "g", 70, COR)], W / 2, 200, "center", 0.1)
    ac = {2: [(b5, E.COR)]}
    slot = notas(c, t, C["s05"] + 0.4, sorted(GANCHO), W / 2, 450, 96, 250, acesas=ac)
    E.foco(c, t, a5, 0.4, lambda a: centro(c, "3º", slot(2), 340, 60, "g", COR, a))
    metades(c, t, c5, slot(0) - 70, slot(1) + 70, slot(3) - 70, slot(4) + 70, 540, "2 abaixo", "2 acima", size=50)
    bola_txt(c, t, b5 + 0.2, "5", slot(2), 690, 80, 80)
    E.frase(c, t, lerp(c5, C["s05.end"], 0.4), ps("o 9 só estava no meio da", "i", 52, TINTA2) + [("bagunça", "g", 54, ERRADO)], W / 2, 900, "center", 0.08)


# ---------------- mediana (quantidade par) ----------------
def b_par(c, t, C, b):
    a6, b6, c6, d6, e6, f6 = (C[f"s06.{k}"] for k in "abcdef")
    E.frase(c, t, C["s06"] + 0.2, ps("e com quantidade", "i", 70) + [("par?", "g", 76, COR)], W / 2, 190, "center", 0.1)
    ac = {1: [(b6 + 1.0, E.COR)], 2: [(b6 + 1.0, E.COR)]}
    slot = notas(c, t, a6, PAR, W / 2, 340, 96, 250, t_ordem=b6, acesas=ac)
    E.frase(c, t, b6 + 1.2, ps("não sobra um no meio: sobram", "i", 50, TINTA2) + [("5 e 8", "g", 54, COR)], W / 2, 570, "center", 0.08)
    E.frase(c, t, c6, ps("mediana =", "i", 60) + [("média dos do meio", "g", 64, COR)], W / 2, 670, "center", 0.1)
    fcen(c, t, d6, "5 + 8 = 13", 620, 810, 84)
    fcen(c, t, e6, "13 ÷ 2 = 6,5", 1240, 810, 84, COR)
    E.foco(c, t, f6, 0.4, lambda a: E.pilula(c, "6,5 nem está na lista", W / 2, 950, 54, "g", a=a, cor=E.SOBRE))
    if t >= e6 + 0.3:
        p = ep(t, e6 + 0.3, 0.5)
        xm = (slot(1) + slot(2)) / 2
        M.line(c, xm, 300, xm, 420, COR, p, 5, dash=E.TRACO)
        E.foco(c, t, e6 + 0.6, 0.4, lambda a: E.pilula(c, "6,5", xm, 465, 42, "g", a=a, cor=E.SOBRE))


# ---------------- moda ----------------
def b_moda(c, t, C, b):
    a7, b7, c7, d7, e7 = (C[f"s07.{k}"] for k in "abcde")
    a8, b8, c8, d8 = (C[f"s08.{k}"] for k in "abcd")
    a9, b9, c9 = C["s09.a"], C["s09.b"], C["s09.c"]

    def um():
        E.frase(c, t, a7, [("moda", "g", 90, COR)] + ps("= o valor que", "i", 76) + [("mais aparece", "g", 80)], W / 2, 190, "center", 0.1)

        def camisas():
            E.frase(c, t, b7, ps("como a roupa que você", "i", 58) + [("mais vê na rua", "g", 62, COR)], W / 2, 330, "center", 0.08)
            for i, cor in enumerate((E.COR, TINTA2, E.COR, CATS[1], E.COR)):
                E.foco(c, t, b7 + 0.6 + 0.2 * i, 0.4, lambda a, i=i, cor=cor: camisa(c, 560 + 200 * i, 600, 150, "", a, cor), sobe=30)
        fase(c, t, b7, c7 - 0.1, camisas)
        if t < c7 - 0.1:
            return
        ac = {1: [(c7 + 0.3, E.COR)], 3: [(c7 + 0.6, E.COR)], 5: [(c7 + 0.9, E.COR)]}
        notas(c, t, c7, MODA, W / 2, 330, 64, 170, acesas=ac, d_ent=0.05)
        E.frase(c, t, c7 + 1.2, ps("o 7 aparece", "i", 52) + [("3 vezes", "g", 56, COR)], W / 2, 470, "center", 0.08)
        cols = [("valor", 200, e7), ("vezes", 220, e7 + 0.2)]
        lin = [[(str(v), e7 + 0.3 + 0.15 * i), (str(MODA.count(v)), e7 + 0.4 + 0.15 * i, COR if v == 7 else TINTA)] for i, v in enumerate((5, 6, 7, 8, 9))]
        quadro(c, t, 330, 580, cols, lin, size=46, h_lin=74)
        bola_txt(c, t, d7, "7", 1400, 720, 120, 120)
        E.foco(c, t, d7 + 0.2, 0.4, lambda a: centro(c, "moda", 1400, 560, 64, "i", COR, a))
    fase(c, t, C["s07"], C["s08"] - 0.1, um)

    def dois():
        L, R = 520, 1400
        E.frase(c, t, a8, [("duas modas", "g", 66, COR)], L, 220, "center")
        notas(c, t, a8 + 0.3, [4, 4, 6, 6, 8], L, 360, 54, 130, acesas={0: [(a8 + 1.0, E.COR)], 1: [(a8 + 1.0, E.COR)], 2: [(a8 + 1.3, CATS[2])], 3: [(a8 + 1.3, CATS[2])]}, d_ent=0.06)
        E.frase(c, t, a8 + 1.6, ps("4 e 6 empatam no topo", "i", 46, TINTA2), L, 480, "center", 0.06)
        E.frase(c, t, b8, [("sem moda", "g", 66, TINTA2)], R, 220, "center")
        notas(c, t, b8 + 0.3, [3, 5, 7, 9], R, 360, 54, 140, d_ent=0.06)
        E.frase(c, t, b8 + 1.0, ps("todos aparecem 1 vez", "i", 46, TINTA2), R, 480, "center", 0.06)
        if t >= c8 - 0.2:
            M.line(c, 260, 560, W - 260, 560, FIO, ep(t, c8 - 0.2, 0.5), 3)
        E.frase(c, t, c8, ps("serve até para dado que", "i", 58) + [("não é número", "g", 62, COR)], W / 2, 660, "center", 0.08)
        E.frase(c, t, c8 + 1.6, ps("o transporte mais usado", "i", 48, TINTA2), 520, 760, "center", 0.06)
        for i, cor in enumerate((CATS[1], E.COR, E.COR, TINTA2, E.COR, CATS[2])):
            E.foco(c, t, d8 + 0.15 * i, 0.4, lambda a, i=i, cor=cor: camisa(c, 1080 + 140 * i, 880, 92, "", a, cor), sobe=30)
        E.frase(c, t, d8, ps("a camiseta mais vendida", "i", 48, TINTA2), 1430, 760, "center", 0.06)
    fase(c, t, C["s08"], C["s09"] - 0.1, dois)
    if t < C["s09"] - 0.1:
        return
    E.frase(c, t, C["s09"] + 0.2, ps("na", "i", 64) + [("tabela de frequência", "g", 70, COR)] + ps("é mais rápido", "i", 64), W / 2, 190, "center", 0.1)
    E.frase(c, t, a9, ps("a linha com a", "i", 52) + [("maior frequência", "g", 56, COR)], W / 2, 280, "center", 0.08)
    cols = [("transporte", 340, a9 + 0.3), ("pessoas", 240, a9 + 0.5)]
    nomes = [("ônibus", 8), ("carro", 5), ("bicicleta", 4), ("a pé", 3)]
    lin = [[(n, a9 + 0.7 + 0.2 * i), (str(v), a9 + 0.8 + 0.2 * i, COR if i == 0 and t >= b9 else TINTA)] for i, (n, v) in enumerate(nomes)]
    bases = quadro(c, t, 300, 430, cols, lin, [("total", a9 + 1.6), ("20", a9 + 1.7)], size=54, cores=CATS)
    if t >= b9:
        p = ep(t, b9, 0.5)
        E.caixa_pontilhada(c, 270, bases[0] - 60, 660, 84, p, None, prog_=p)
    bola_txt(c, t, c9, "ônibus", 1430, 640, 170, 64)
    E.foco(c, t, c9 + 0.2, 0.4, lambda a: centro(c, "moda", 1430, 420, 64, "i", COR, a))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    a0, b0, c0, d0 = (C[f"s10.{k}"] for k in "abcd")
    E.frase(c, t, C["s10"] + 0.2, [("erro comum:", "g", 66, ERRADO)], W / 2, 170, "center", 0.1)
    E.frase(c, t, a0, ps("a mediana pelo", "i", 60) + [("menor e maior", "g", 64, ERRADO)], W / 2, 260, "center", 0.1)
    ac = {0: [(a0 + 0.5, ERRADO)], 3: [(a0 + 0.5, ERRADO)], 1: [(c0, E.COR)], 2: [(c0, E.COR)]}
    notas(c, t, a0, sorted(PAR), W / 2, 400, 80, 220, acesas=ac)
    fcen(c, t, b0, "(3 + 9) ÷ 2 = 6", 640, 580, 80, ERRADO)
    E.foco(c, t, b0 + 0.6, 0.5, lambda a: E.selo(c, 1010, 555, 40, False, a))
    fcen(c, t, c0, "mediana = 6,5", 1350, 580, 80, CERTO)
    E.foco(c, t, c0 + 0.6, 0.5, lambda a: E.selo(c, 1680, 555, 40, True, a))
    vx = E.reta(c, t, b0 + 0.6, 400, 1520, 800, 2, 10, [2, 3, 4, 5, 6, 7, 8, 9, 10], size=40)
    for v in sorted(PAR):
        E.foco(c, t, b0 + 0.9, 0.4, lambda a, v=v: c.drawCircle(vx(v), 800, 14, M.paint(TINTA, a)))
    E.foco(c, t, b0 + 1.2, 0.4, lambda a: (c.drawCircle(vx(6), 800, 18, M.paint(PAPEL, a)), c.drawCircle(vx(6), 800, 18, M.paint(ERRADO, a, stroke=6)),
                                           centro(c, "6", vx(6), 740, 48, "g", ERRADO, a)))
    E.foco(c, t, c0 + 0.4, 0.4, lambda a: (c.drawCircle(vx(6.5), 800, 18, M.paint(CERTO, a)), centro(c, "6,5", vx(6.5) + 30, 740, 48, "g", CERTO, a)))
    E.foco(c, t, d0, 0.5, lambda a: E.pilula(c, "a mediana olha a posição de todos", W / 2, 980, 50, "g", a=a, cor=E.SOBRE))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    a1, b1, c1, d1 = (C[f"s11.{k}"] for k in "abcd")
    a2, b2, c2, d2 = (C[f"s12.{k}"] for k in "abcd")

    def um():
        E.frase(c, t, C["s11"] + 0.2, ps("atalho para listas grandes:", "i", 64, CLARO), W / 2, 170, "center", 0.1)
        E.frase(c, t, a1, [("a posição do meio", "g", 76, BR)], W / 2, 270, "center", 0.1)
        fcen(c, t, b1, "posição = f{n + 1}{2}", W / 2, 450, 100, BR)
        E.frase(c, t, b1 + 0.6, ps("n = quantidade de dados", "i", 46, CLARO), W / 2, 570, "center", 0.08)
        fcen(c, t, c1, "f{11 + 1}{2} = f{12}{2} = 6", W / 2, 700, 76, BR)
        regua(c, t, c1 + 0.4, 11, W / 2, 860, acesas=(6,), t_acende=d1)
        E.frase(c, t, d1 + 0.2, ps("a mediana é o", "i", 54, CLARO) + [("6º valor", "g", 58, BR)], W / 2, 990, "center", 0.08)
    fase(c, t, C["s11"], C["s12"] - 0.1, um)
    if t < C["s12"] - 0.1:
        return
    xk = regua(c, t, C["s12"], 11, W / 2, 260, acesas=(6,), t_acende=C["s12"], d=0.0)
    metades(c, t, a2, xk(1) - 44, xk(5) + 44, xk(7) - 44, xk(11) + 44, 316, "5 antes", "5 depois", cor=CLARO, size=46)
    fcen(c, t, b2, "10 dados: f{10 + 1}{2} = 5,5", W / 2, 560, 76, BR)
    regua(c, t, b2 + 0.5, 10, W / 2, 710, acesas=(5, 6), t_acende=c2)
    E.frase(c, t, c2 + 0.2, ps("a mediana é a", "i", 54, CLARO) + [("média do 5º e do 6º", "g", 58, BR)], W / 2, 840, "center", 0.08)
    E.foco(c, t, d2, 0.5, lambda a: E.pilula(c, "lista curta? olhe e ache o meio", W / 2, 970, 48, "g", a=a, cor=E.SOBRE))


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    a3, b3, c3 = C["s13.a"], C["s13.b"], C["s13.c"]
    E.frase(c, t, C["s13"] + 0.1, ps("hora de testar", "i", 72, COR), XE, 180, passo=0.12)
    E.frase(c, t, a3, ps("as notas de", "i", 58) + [("8 alunos:", "g", 62, COR)], XE, 300, passo=0.1)
    notas(c, t, a3 + 0.3, QUEST, 820, 450, 70, 175, d_ent=0.06)
    E.frase(c, t, b3, [("1)", "g", 64, COR)] + ps("qual é a", "i", 64) + [("mediana?", "g", 68)], XE, 640, passo=0.1)
    E.frase(c, t, c3, [("2)", "g", 64, COR)] + ps("qual é a", "i", 64) + [("moda?", "g", 68)], XE, 760, passo=0.1)
    E.relogio(c, t, C["s14.a"], 1560, 780, 140)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    a5, b5, c5, d5 = (C[f"s15.{k}"] for k in "abcd")
    a6, b6, c6 = C["s16.a"], C["s16.b"], C["s16.c"]
    ord_ = sorted(range(8), key=lambda i: (QUEST[i], i))
    i7, i8 = ord_[3], ord_[4]
    i9 = [i for i in range(8) if QUEST[i] == 9]
    ac = {i7: [(c5, E.COR), (a6, None)], i8: [(c5, E.COR), (a6, None)], i9[0]: [(a6, CATS[2])], i9[1]: [(a6, CATS[2])]}
    slot = notas(c, t, C["s15"], QUEST, W / 2, 300, 70, 190, t_ordem=a5, acesas=ac, d_ent=0.0)
    E.foco(c, t, a5, 0.4, lambda a: E.escreve(c, "em ordem", XE - 60, 190, 48, "i", TINTA2, a))

    def um():
        fcen(c, t, b5, "8 dados: f{8 + 1}{2} = 4,5", W / 2, 520, 72)
        E.foco(c, t, c5, 0.4, lambda a: (centro(c, "4º", slot(3), 410, 46, "g", COR, a), centro(c, "5º", slot(4), 410, 46, "g", COR, a)))
        E.frase(c, t, c5 + 0.3, ps("média do 4º e do 5º:", "i", 54) + [("7 e 8", "g", 58, COR)], W / 2, 650, "center", 0.08)
        fcen(c, t, d5, "(7 + 8) ÷ 2 = 15 ÷ 2 = 7,5", 820, 820, 72)
        bola_txt(c, t, d5 + 0.8, "7,5", 1480, 800, 110, 76)
        E.foco(c, t, d5 + 1.0, 0.4, lambda a: centro(c, "mediana", 1480, 960, 52, "i", COR, a))
    fase(c, t, C["s15"], C["s16"] - 0.1, um)
    if t < C["s16"] - 0.1:
        return
    bola_txt(c, t, a6, "9", 1480, 740, 110, 110)
    E.foco(c, t, a6 + 0.2, 0.4, lambda a: centro(c, "moda", 1480, 590, 60, "i", COR, a))
    E.frase(c, t, b6, ps("a única nota que aparece", "i", 52) + [("2 vezes", "g", 56, COR)], 1480, 920, "center", 0.08)
    xm = (slot(3) + slot(4)) / 2
    if t >= c6:
        M.line(c, xm, 250, xm, 420, COR, ep(t, c6, 0.4), 5, dash=E.TRACO)
    E.foco(c, t, c6 + 0.2, 0.4, lambda a: E.pilula(c, "7,5", xm, 200, 40, "g", a=a, cor=E.SOBRE))
    metades(c, t, c6 + 0.3, slot(0) - 60, slot(3) - 20, slot(4) + 20, slot(7) + 60, 360, "4 abaixo", "4 acima", size=46)
    E.frase(c, t, c6 + 1.2, ps("metade de cada lado", "i", 52, TINTA2), 640, 600, "center", 0.08)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s17"], [("resumindo", "i", 92, COR)], W / 2, 210, "center")
        itens = (("s17.a", [("mediana:", "g", 70, COR)] + ps("ordene e pegue o meio", "i", 64)),
                 ("s17.b", [("moda:", "g", 70, COR)] + ps("o que mais aparece", "i", 64)))
        for i, (k, partes) in enumerate(itens):
            y = 460 + i * 200
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 200, y - 25, 52, a=a), centro(c, str(i + 1), 200, y - 4, 60, "g", E.SOBRE, a)))
            E.frase(c, t, C[k] + 0.1, partes, 290, y, "left", 0.1)
    E.saida(c, t, C["s18"] - 0.1, resumo)
    if t < C["s18"]:
        return
    a0, b0, c0, d0 = (C[f"s18.{k}"] for k in "abcd")
    E.frase(c, t, C["s18"] + 0.2, ps("na próxima aula", "i", 80), XE, 250, passo=0.12)
    E.frase(c, t, a0, ps("os dados numa", "i", 84) + [("tabela", "g", 110, COR)], XE, 410, passo=0.12)
    E.frase(c, t, a0 + 1.2, ps("a nota e o número de alunos", "i", 50, TINTA2), XE, 500, passo=0.08)
    E.frase(c, t, b0, [("média, mediana e moda", "g", 64, COR)], XE, 640, passo=0.1)
    E.frase(c, t, b0 + 1.0, ps("sem escrever a lista inteira", "i", 50), XE, 720, passo=0.08)
    E.foco(c, t, c0, 0.5, lambda a: E.pilula(c, "Inscreva-se", 1550, 380, 76, estilo="g", a=a, cor=E.SOBRE))
    p = ease_io(prog(t, c0 + 0.3, 0.8))
    E.cursor(c, lerp(1830, 1680, p), lerp(700, 405, p), ep(t, c0 + 0.2, 0.4))
    E.frase(c, t, d0, [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 980, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, mediana=b_mediana, par=b_par, moda=b_moda, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
