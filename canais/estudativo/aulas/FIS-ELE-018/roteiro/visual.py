"""Visual — Estudativo · FIS-ELE-018: consumo em kWh e conta de luz.

Segue a linguagem visual da Física (cabeçalho do visual.py da FIS-CIN-001) e a da Eletricidade (cabeçalho do visual.py da
FIS-ELE-001: unidades em cinza-tinta; Ω e = só na fonte pesada).
Nesta aula: cada aparelho é uma LINHA DA CONTA (peça `linha_conta`: nome, potência × horas × dias = kWh), e a soma do mês
fecha numa fatura (peça `fatura`); o consumo em kWh vai em laranja, o valor em reais em verde. A energia aparece como
barra: potência × tempo = área do retângulo (peça `retangulo_energia`), que é o atalho para comparar aparelhos.
O medidor de luz (peça `medidor_luz`) mostra os dígitos em kWh.
Todo instante vem de C[...] (marcadores do roteiro)."""
import math

import editorial as E
import fisica as F
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Física", "Eletricidade")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_FIS-ELE-018_consumo_em_kwh_e_conta_de_luz.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("energia", "conta", "casa", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"

# todas as contas da aula (com tolerância de ponto flutuante)
ok = lambda a, b: abs(a - b) < 1e-9
assert 4000 / 1000 == 4 and ok(4 * 0.5, 2) and ok(2 * 30, 60) and ok(60 * 0.8, 48)
assert ok(0.1 * 5, 0.5) and ok(2 / 0.5, 4) and ok(0.1 * 5 * 30, 15) and 60 + 15 + 25 == 100 and ok(100 * 0.8, 80)
assert 1000 * 3600 == 3_600_000 and 4620 - 4520 == 100
assert 4000 * 0.5 * 30 == 60000 and ok(60000 * 0.8, 48000) and 60000 / 1000 == 60
assert ok(0.1 * 20, 2) and 4000 / 100 == 40 and 20 / 0.5 == 40
assert ok(1.5 * 2, 3) and ok(3 * 30, 90) and ok(90 * 0.8, 72)


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças da trilha ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def bola_txt(c, t, t0, s, cx, cy, r, size, cor=None):
    """resposta na esfera: "2 A" com a unidade menor"""
    v, _, u = s.partition(" ")
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r * ease_back(prog(t, t0, 0.5)), cor, a),
                                     F.medida(c, v, u, cx, cy + size * 0.36, size, E.SOBRE, a, "center", cor_u=E.SOBRE)))


def troca(c, t, itens, fn):
    """um de cada vez: itens = [(instante, arg)], cada um sai quando o próximo chega; fn(arg, a) desenha"""
    for i, (ti, s) in enumerate(itens):
        fim = itens[i + 1][0] - 0.1 if i + 1 < len(itens) else 1e9
        if t >= ti - 0.01:
            E.saida(c, t, fim, lambda s=s, ti=ti: E.foco(c, t, ti, 0.45, lambda a: fn(s, a)), d=0.25)


def pilula_em(c, t, t0, s, cx, cy, size, fundo=None, est="g"):
    E.foco(c, t, t0, 0.4, lambda a: E.pilula(c, s, cx, cy, size, est, fundo=fundo, a=a, cor=BR))


def lembrete(c, t, C, cena, itens, desenhos=()):
    """lembrete de 2 ou 3 coisas: itens = [(cue, linha fina, linha forte, linha de fórmula ou None)]"""
    n = len(itens)
    E.frase(c, t, C[cena] + 0.2, ps("você precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C[cena + ".a"], 0.5, lambda a: E.escreve(c, str(n), XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C[cena + ".a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 820, 1000
    hs = [200 + (80 if it[3] else 0) for it in itens]
    gap = 40 if n == 2 else 30
    y = 120 + (800 - sum(hs) - gap * (n - 1)) / 2
    for i, (k, l1, l2, l3) in enumerate(itens):
        h = hs[i]
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, h, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 56)], x + 44, y + 82)
        E.frase(c, t, C[k] + 0.3, [(l2, "g", 56, COR)], x + 44, y + 160)
        if l3:
            E.foco(c, t, C[k] + 0.9, 0.5, lambda a, l3=l3, y=y: fi(c, l3, x + 44, y + 245, 50, "b", TINTA2, a))
        if i < len(desenhos) and desenhos[i]:
            E.foco(c, t, C[k] + 0.6, 0.5, lambda a, i=i, y=y, h=h: desenhos[i](a, x + w - 160, y + 105))
        y += h + gap
    E.frase(c, t, lerp(C[itens[-1][0]], C[cena + ".end"], 0.7), ps("faltou alguma?", "i", 54, COR) + ps("procure no canal", "i", 54),
            820, 1000, "left", 0.12)


def tag(c, t, t0, s, cx, cy, size=40, fundo=None, est="b"):
    """pílula pequena (tensão de um resistor, corrente de um ramo, potencial de um ponto)"""
    E.foco(c, t, t0, 0.4, lambda a: E.pilula(c, s, cx, cy, size, est, fundo=fundo or TINTA2, a=a, cor=BR))


def numero(c, t, t0, i, cx, cy, r=30, cor=None):
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r, cor, a), centro(c, str(i), cx, cy + r * 0.55, r * 1.3, "g", BR, a)))


# ---------------- fórmula com índice: cópia local de E.formula que aceita "_" (R_{eq}, R_1) ----------------
def _ler_i(s, i=0, fim=None):
    nos, txt = [], ""

    def solta():
        nonlocal txt
        if txt:
            nos.append(("t", txt))
            txt = ""

    while i < len(s):
        ch = s[i]
        if ch == fim:
            solta()
            return nos, i + 1
        if ch in "^_":
            solta()
            if s[i + 1] == "{":
                dentro, i = _ler_i(s, i + 2, "}")
            else:
                dentro, i = [("t", s[i + 1])], i + 2
            nos.append(("e" if ch == "^" else "i", dentro))
        elif ch == "f" and i + 1 < len(s) and s[i + 1] == "{":
            solta()
            cima, i = _ler_i(s, i + 2, "}")
            baixo, i = _ler_i(s, i + 1, "}")
            nos.append(("f", cima, baixo))
        else:
            txt += ch
            i += 1
    solta()
    return nos, i


def _medir_i(nos, size, est):
    w = 0.0
    for n in nos:
        if n[0] == "t":
            w += E.larg(n[1], est, size) + E.APERTO[est] * size + size * 0.02
        elif n[0] == "e":
            w += _medir_i(n[1], size * 0.58, est) + size * 0.04
        elif n[0] == "i":
            w += _medir_i(n[1], size * 0.5, "b") + size * 0.04
        else:
            w += max(_medir_i(n[1], size * 0.78, est), _medir_i(n[2], size * 0.78, est)) + size * 0.22
    return w


def _desenhar_i(c, nos, x, y, size, est, cor, a):
    for n in nos:
        if n[0] == "t":
            E.escreve(c, n[1], x, y, size, est, cor, a)
            x += E.larg(n[1], est, size) + E.APERTO[est] * size + size * 0.02
        elif n[0] == "e":
            _desenhar_i(c, n[1], x + size * 0.02, y - size * 0.42, size * 0.58, est, cor, a)
            x += _medir_i(n[1], size * 0.58, est) + size * 0.04
        elif n[0] == "i":
            _desenhar_i(c, n[1], x + size * 0.01, y + size * 0.16, size * 0.5, "b", cor, a)
            x += _medir_i(n[1], size * 0.5, "b") + size * 0.04
        else:
            s_ = size * 0.78
            wc, wb = _medir_i(n[1], s_, est), _medir_i(n[2], s_, est)
            w = max(wc, wb) + size * 0.12
            _desenhar_i(c, n[1], x + (w - wc) / 2, y - size * 0.46, s_, est, cor, a)
            _desenhar_i(c, n[2], x + (w - wb) / 2, y + size * 0.46, s_, est, cor, a)
            b = max(4, size * 0.07)
            c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y - size * 0.3 - b / 2, w, b), b / 2, b / 2), M.paint(cor, a))
            x += w + size * 0.1
    return x


def fi(c, s, x, y, size, estilo="g", cor=None, a=1.0, align="left"):
    """como E.formula (expoente ^ e fração f{}{}), com índice: "R_{eq} = R_1 + R_2". Devolve a largura"""
    nos, _ = _ler_i(s)
    w = _medir_i(nos, size, estilo)
    if a > 0 and c is not None:
        xi = x - w / 2 if align == "center" else x - w if align == "right" else x
        _desenhar_i(c, nos, xi, y, size, estilo, cor or TINTA, a)
    return w


def fi_em(c, t, t0, s, x, y, size, estilo="g", cor=None, align="left"):
    E.foco(c, t, t0, 0.5, lambda a: fi(c, s, x, y, size, estilo, cor, a, align))


# ---------------- peças de circuito (as mesmas nas aulas FIS-ELE-011 a 016) ----------------
def malha(c, t, t0, x0, y0, x1, y1, pecas, pilha=None, tp=None, d=0.8, escuro=False):
    """circuito em série: pilha no lado esquerdo (+ em cima), peças no lado de cima, fios no resto.
    pecas = [(tipo, rótulo, instante[, acesa])], tipo "R" (resistor) ou "L" (lâmpada). Devolve os (A, B) de cada peça"""
    n = len(pecas)
    xs = [x0 + (x1 - x0) * k / n for k in range(n + 1)]
    F.fio(c, t, t0, [(x0, y1), (x1, y1), (x1, y0)], d, escuro=escuro)
    F.pilha(c, t, tp if tp is not None else t0, (x0, y1), (x0, y0), pilha, escuro=escuro)
    ab = []
    for k, p in enumerate(pecas):
        A, B = (xs[k], y0), (xs[k + 1], y0)
        ab.append((A, B))
        if p[0] == "R":
            F.resistor(c, t, p[2], A, B, p[1], escuro=escuro)
        else:
            F.lampada(c, t, p[2], A, B, acesa=p[3] if len(p) > 3 else None, rotulo=p[1], escuro=escuro)
    return ab


def volta(x0, y0, x1, y1):
    """o caminho da corrente na malha: sai do + (canto de cima à esquerda) e volta pelo −"""
    return [(x0, y0), (x1, y0), (x1, y1), (x0, y1)]


def escada(c, t, t0, x0, y0, y1, xs, ramos, pilha=None, tp=None, d=0.8, escuro=False, nos=True):
    """circuito em paralelo: pilha no lado esquerdo (+ em cima), trilho de cima em y0 e de baixo em y1; cada ramo é uma peça
    vertical em xs[k] ligando os dois trilhos. ramos = [(tipo, rótulo, instante)] (tipo "R" ou "L")"""
    F.fio(c, t, t0, [(x0, y0), (xs[-1], y0)], d, escuro=escuro)
    F.fio(c, t, t0, [(x0, y1), (xs[-1], y1)], d, escuro=escuro)
    F.pilha(c, t, tp if tp is not None else t0, (x0, y1), (x0, y0), pilha, escuro=escuro)
    for k, p in enumerate(ramos):
        A, B = (xs[k], y0), (xs[k], y1)
        if p[0] == "R":
            F.resistor(c, t, p[2], A, B, p[1], escuro=escuro)
        else:
            F.lampada(c, t, p[2], A, B, rotulo=p[1], escuro=escuro)
        if nos and k < len(xs) - 1:
            E.foco(c, t, p[2], 0.4, lambda a, A=A, B=B: (F.no(c, A, a, escuro), F.no(c, B, a, escuro)))


def corrente_escada(c, t, t0, x0, y0, y1, xs, ramos=None, cor=None):
    """setinhas da corrente no circuito em escada: tronco pela pilha, uma descida por ramo (ramos = índices)"""
    F.corrente(c, t, t0, [(x0, y1), (x0, y0), (xs[-1], y0)], cor, fecha=False)
    F.corrente(c, t, t0, [(xs[-1], y1), (x0, y1)], cor, fecha=False)
    for k in (ramos if ramos is not None else range(len(xs))):
        F.corrente(c, t, t0, [(xs[k], y0), (xs[k], y1)], cor, fecha=False)


# ---------------- peças desta aula ----------------
def medidor_luz(c, x, y, digitos, a=1.0, k=1.0, destaque=None):
    """mostrador do medidor de luz com os dígitos em kWh; destaque = índices dos dígitos em laranja"""
    if a <= 0:
        return
    n = len(digitos)
    w = (40 + 96 * n) * k
    M.rrect(c, x, y, w, 230 * k, 26 * k, "#1B1B20", a)
    for i, d in enumerate(digitos):
        M.rrect(c, x + (20 + 96 * i) * k, y + 40 * k, 80 * k, 110 * k, 10 * k, E.COR if destaque and i in destaque else "#FFFFFF", a)
        E.centro(c, d, x + (60 + 96 * i) * k, y + 125 * k, 80 * k, "g", BR if destaque and i in destaque else TINTA, a)
    E.escreve(c, "kWh", x + 20 * k, y + 200 * k, 40 * k, "b", BR, a)


def linha_conta(c, t, t0, y, nome, partes, kwh, tk=None, x=XE):
    """linha de um aparelho: nome · conta · = kWh (o resultado entra em tk)"""
    E.frase(c, t, t0, [(nome, "g", 56)], x, y)
    E.formula_em(c, t, t0 + 0.4, partes, x + 400, y, 56, "g", TINTA2)
    E.foco(c, t, tk if tk is not None else t0 + 1.0, 0.5, lambda a: F.medida(c, kwh, "kWh", x + 1300, y, 64, COR, a))


def retangulo_energia(c, x, yb, wp, ht, cor, a=1.0, rot_p=None, rot_t=None, area=None, escuro=False):
    """energia como área: largura = tempo, altura = potência (a base em yb)"""
    if a <= 0:
        return
    M.rrect(c, x, yb - ht, wp, ht, 10, cor, a)
    tinta = BR if escuro else TINTA
    if rot_p:
        E.formula(c, rot_p, x - 20, yb - ht / 2 + 18, 46, "b", tinta, a, "right")
    if rot_t:
        E.formula(c, rot_t, x + wp / 2, yb + 60, 46, "b", tinta, a, "center")
    if area:
        E.formula(c, area, x + wp / 2, yb - ht / 2 + 18, 50, "g", BR, a, "center")


def bola_reais(c, t, t0, s, cx, cy, r, size, cor=None):
    """valor em reais na esfera: "R$ 48" inteiro, em uma linha"""
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r * ease_back(prog(t, t0, 0.5)), cor, a),
                                     E.centro(c, s, cx, cy + size * 0.36, size, "g", E.SOBRE, a)))


def cartao(c, s, cx, y, size, fundo, a=1.0, cor=BR):
    """fórmula num cartão arredondado (E.pilula não aceita expoente)"""
    if a <= 0:
        return
    w = E.formula(None, s, 0, 0, size, "g", a=0) + size * 1.1
    h = size * 1.7
    M.rrect(c, cx - w / 2, y - size * 1.1, w, h, h / 2, fundo, a)
    E.formula(c, s, cx, y, size, "g", cor, a, "center")


def aquecedor(c, t, x, y, w, h, a=1.0):
    """aquecedor elétrico de frente: caixa clara com três barras incandescentes"""
    if a <= 0:
        return
    M.rrect(c, x, y, w, h, 24, "#E6E2DA", a)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 24, 24), M.paint(TINTA, a, stroke=5))
    for k in range(3):
        yy = y + h * (0.28 + 0.22 * k)
        g = 0.75 + 0.25 * math.sin(t * 3 + k)
        M.line(c, x + 40, yy, x + w - 40, yy, E.mix("#FFC400", E.COR, 0.5), a * g, 18)
    for k in range(3):
        xx = x + w * (0.3 + 0.2 * k)
        pts = [(xx + 10 * math.sin(t * 3 + k + i * 0.9), y - 30 - 24 * i) for i in range(5)]
        F.poli(c, pts, 1.0, E.COR, a * 0.7, 5)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def um():
        E.frase(c, t, C["s01.a"], [("chuveiro", "g", 66), ("4.000 W", "g", 66, COR)], XE, 300, passo=0.12)
        E.frase(c, t, C["s01.a"] + 1.0, ps("meia hora por dia", "i", 58, TINTA2), XE, 390, passo=0.1)
        E.frase(c, t, C["s01.b"], [("TV", "g", 66), ("100 W", "g", 66, COR)], XE, 560, passo=0.12)
        E.frase(c, t, C["s01.b"] + 1.0, ps("cinco horas por dia", "i", 58, TINTA2), XE, 650, passo=0.1)
        # as barras de energia por dia
        q1, q2 = ease_io(prog(t, C["s01.c"], 0.8)), ease_io(prog(t, C["s01.c"] + 0.3, 0.8))
        E.foco(c, t, C["s01.c"], 0.4, lambda a: E.escreve(c, "energia por dia", 1100, 300, 46, "i", TINTA2, a))
        if q1 > 0:
            M.rrect(c, 1100, 360, 640 * q1, 120, 14, E.COR)
            E.foco(c, t, C["s01.c"] + 0.8, 0.4, lambda a: F.medida(c, 2, "kWh", 1120, 445, 56, BR, a, cor_u=BR))
        if q2 > 0:
            M.rrect(c, 1100, 560, 160 * q2, 120, 14, TINTA2)
            E.foco(c, t, C["s01.c"] + 1.1, 0.4, lambda a: F.medida(c, "0,5", "kWh", 1290, 645, 56, TINTA, a))
        E.foco(c, t, C["s01.d"], 0.5, lambda a: (E.bola(c, 1600, 800, 110, a=a), E.centro(c, "× 4", 1600, 830, 80, "g", BR, a)))
        E.frase(c, t, C["s01.c"], [("o", "i", 70), ("chuveiro", "g", 66, COR)], XE, 860, passo=0.12)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t < C["s02"]:
        return
    tb = C["s02.a"] + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1520, 540, 300 * ease_back(prog(t, tb, 0.8)), giro=12 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 88), XE, 260, passo=0.14)
    for i, (k, s, dt) in enumerate((("s02.a", "o consumo em kWh", 1.2), ("s02.b", "em reais", 0), ("s02.c", "a conta do mês", 0))):
        y = 450 + i * 160
        numero(c, t, C[k] + dt, i + 1, XE + 40, y - 30, 38)
        E.frase(c, t, C[k] + dt + 0.1, [(s, "g", 76, COR if i == 0 else TINTA)], XE + 110, y)


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    lembrete(c, t, C, "s03", (("s03.b", "potência = energia ÷ tempo,", "1 kW = 1.000 W", "P = f{E}{Δt}"),
                              ("s03.c", "hora decimal:", "30 min = 0,5 h", None)))


# ---------------- energia ----------------
def b_energia(c, t, C, b):
    def s04():
        E.frase(c, t, C["s04"], ps("se potência é energia ÷ tempo,", "i", 64), XE, 230, passo=0.1)
        E.foco(c, t, C["s04.a"], 0.6, lambda a: (E.bola(c, XE + 300, 470, 150, a=a), E.formula(c, "E = P · Δt", XE + 300, 500, 76, "g", E.SOBRE, a, "center")))
        E.frase(c, t, C["s04.a"] + 0.6, ps("energia = potência × tempo", "i", 60), XE + 520, 490, passo=0.1)
        E.formula_em(c, t, C["s04.b"], "W · s = J", XE, 760, 84, "g", F.UNID)
        E.foco(c, t, C["s04.b"] + 0.4, 0.4, lambda a: E.escreve(c, "no Sistema Internacional", XE + 440, 750, 50, "i", TINTA2, a))
        E.frase(c, t, C["s04.c"], ps("chuveiro, meia hora:", "i", 58) + [("milhões", "g", 56, ERRADO), ("de", "i", 58), ("joules", "i", 58)], XE, 920, passo=0.1)
    E.saida(c, t, C["s05"] - 0.1, s04)
    if C["s05"] <= t < C["s06"]:
        def s05():
            E.frase(c, t, C["s05.a"], ps("na conta:", "i", 70) + [("quilowatt-hora", "g", 70, COR)], XE, 230, passo=0.12)
            E.foco(c, t, C["s05.a"] + 0.6, 0.4, lambda a: E.pilula(c, "kWh", XE + 1180, 210, 56, "g", fundo=E.COR, a=a))
            E.formula_em(c, t, C["s05.b"], "P em kW", XE, 420, 80, "g", TINTA)
            E.formula_em(c, t, C["s05.c"], "×  Δt em h", XE + 420, 420, 80, "g", TINTA)
            E.formula_em(c, t, C["s05.d"], "=  E em kWh", XE + 920, 420, 80, "g", COR)
            # 1 kWh: 1.000 W durante 1 h
            E.frase(c, t, C["s05.e"], [("1", "g", 66), ("kWh", "g", 66, COR), ("=", "g", 66, TINTA2)] + ps("1.000 W ligados 1 hora", "i", 64), XE, 640, passo=0.1)
            E.foco(c, t, C["s05.e"] + 1.0, 0.5, lambda a: retangulo_energia(c, 700, 960, 500, 200, E.COR, a, "1.000 W", "1 h", "1 kWh"))
        E.saida(c, t, C["s06"] - 0.1, s05)
    if t < C["s06"]:
        return
    E.frase(c, t, C["s06"], ps("em joules:", "i", 70), XE, 260)
    E.formula_em(c, t, C["s06.a"], "1 kWh = 1.000 W × 3.600 s", XE, 460, 90, "g", TINTA)
    E.formula_em(c, t, C["s06.b"], "= 3.600.000 J", XE + 600, 640, 90, "g", TINTA)
    E.foco(c, t, C["s06.c"], 0.5, lambda a: cartao(c, "3,6 × 10^6 J", XE + 900, 860, 76, E.COR, a))


# ---------------- o chuveiro ----------------
def b_conta(c, t, C, b):
    E.frase(c, t, C["s07"], ps("o chuveiro", "i", 76, COR), XE, 200)
    E.formula_em(c, t, C["s07.a"], "4.000 W = 4 kW", XE, 360, 76, "g", TINTA)
    E.formula_em(c, t, C["s07.b"], "30 min = 0,5 h", XE + 800, 360, 76, "g", TINTA)
    E.formula_em(c, t, C["s07.c"], "4 × 0,5 = 2 kWh por dia", XE, 520, 76, "g", TINTA)
    E.formula_em(c, t, C["s07.d"], "2 × 30 = ", XE, 680, 76, "g", TINTA)
    E.foco(c, t, C["s07.d"] + 0.5, 0.5, lambda a: F.medida(c, 60, "kWh", XE + 420, 680, 90, COR, a))
    E.foco(c, t, C["s07.d"] + 0.8, 0.4, lambda a: E.escreve(c, "no mês", XE + 820, 670, 50, "i", TINTA2, a))
    if t >= C["s08"]:
        E.frase(c, t, C["s08.a"], ps("conta = consumo × tarifa", "g", 56, TINTA2), XE, 830, passo=0.1)
        E.foco(c, t, C["s08.b"], 0.4, lambda a: E.pilula(c, "tarifa de exemplo: R$ 0,80 por kWh", 1350, 810, 40, "b", fundo=TINTA, a=a))
        E.formula_em(c, t, C["s08.c"], "60 × 0,8 =", XE, 960, 76, "g", TINTA)
        bola_reais(c, t, C["s08.d"], "R$ 48", XE + 640, 955, 90, 50, CERTO)
        E.frase(c, t, C["s08.d"] + 0.5, ps("por mês, só no banho", "i", 52, TINTA2), XE + 760, 975, passo=0.1)


# ---------------- a casa ----------------
def b_casa(c, t, C, b):
    def fatura():
        E.frase(c, t, C["s09.a"], ps("a casa toda:", "i", 70) + [("cada", "g", 66, COR), ("aparelho", "g", 66, COR)] + ps("e some", "i", 70), XE, 200, passo=0.12)
        linha_conta(c, t, C["s09.a"] + 0.5, 360, "chuveiro", "4 kW × 0,5 h × 30", 60, C["s09.a"] + 1.2)
        linha_conta(c, t, C["s09.b"], 480, "TV", "0,1 kW × 5 h × 30", 15, C["s09.c"])
        E.frase(c, t, C["s09.d"], [("geladeira", "g", 56)], XE, 600)
        E.foco(c, t, C["s09.d"] + 0.4, 0.4, lambda a: E.escreve(c, "liga e desliga: veja a etiqueta", XE + 400, 600, 50, "i", TINTA2, a))
        E.foco(c, t, C["s09.e"], 0.5, lambda a: F.medida(c, 25, "kWh", XE + 1300, 600, 64, COR, a))
        if t >= C["s10.a"]:
            M.line(c, XE, 660, XE + 1560, 660, TINTA, ep(t, C["s10.a"], 0.4), 4)
        E.frase(c, t, C["s10.a"], [("total", "g", 60)], XE, 760)
        E.formula_em(c, t, C["s10.a"] + 0.4, "60 + 15 + 25 =", XE + 400, 760, 60, "g", TINTA2)
        E.foco(c, t, C["s10.a"] + 0.9, 0.5, lambda a: F.medida(c, 100, "kWh", XE + 1300, 760, 72, COR, a))
        E.formula_em(c, t, C["s10.b"], "100 × 0,8 =", XE + 400, 900, 64, "g", TINTA2)
        bola_reais(c, t, C["s10.b"] + 0.6, "R$ 80", XE + 1390, 890, 90, 50, CERTO)
    E.saida(c, t, C["s11"] - 0.1, fatura)
    if t < C["s11"]:
        return
    E.frase(c, t, C["s11.a"], ps("na conta de verdade:", "i", 66) + [("o", "i", 70), ("medidor", "g", 66, COR)], XE, 230, passo=0.12)
    E.foco(c, t, C["s11.a"] + 0.6, 0.5, lambda a: medidor_luz(c, XE, 330, "04520", a, 0.9))
    E.foco(c, t, C["s11.a"] + 0.6, 0.4, lambda a: E.escreve(c, "mês passado", XE, 580, 46, "i", TINTA2, a))
    E.foco(c, t, C["s11.b"], 0.5, lambda a: medidor_luz(c, XE + 620, 330, "04620", a, 0.9, destaque=(2,)))
    E.foco(c, t, C["s11.b"], 0.4, lambda a: E.escreve(c, "este mês", XE + 620, 580, 46, "i", TINTA2, a))
    E.formula_em(c, t, C["s11.c"], "4.620 − 4.520 =", XE, 780, 84, "g", TINTA)
    E.foco(c, t, C["s11.d"], 0.5, lambda a: F.medida(c, 100, "kWh", XE + 780, 780, 96, COR, a))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s12"], [("cuidado", "g", 96, ERRADO)], XE, 200)
    E.frase(c, t, C["s12.a"], ps("esquecer de passar", "i", 66) + [("W", "g", 62), ("→", "g", 62, TINTA2), ("kW", "g", 62, COR)], XE, 340, passo=0.12)
    E.formula_em(c, t, C["s12.b"], "4.000 × 0,5 × 30 = 60.000", XE, 500, 84, "g", TINTA)
    E.formula_em(c, t, C["s12.c"], "60.000 kWh × 0,8 = R$ 48.000 ?", XE, 660, 72, "g", ERRADO)
    if t >= C["s12.d"]:
        E.risco(c, XE - 10, 680, XE + 1180, 600, t, C["s12.d"], largura=10)
    E.frase(c, t, C["s12.d"], [("60.000", "g", 66), ("é", "i", 70), ("watt-hora:", "g", 66, COR)] + ps("divida por mil", "i", 70), XE, 830, passo=0.12)
    E.foco(c, t, C["s12.e"], 0.5, lambda a: F.medida(c, 60, "kWh", XE + 1250, 830, 90, CERTO, a))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def s13():
        E.frase(c, t, C["s13"], ps("o atalho para comparar:", "i", 70, CLARO), XE, 190, passo=0.1)
        E.frase(c, t, C["s13.a"], ps("pesa a", "i", 66, CLARO) + [("potência", "g", 62, BR), ("×", "g", 62, CLARO), ("tempo", "g", 62, BR)], XE, 300, passo=0.12)
        yb = 820
        E.foco(c, t, C["s13.b"], 0.5, lambda a: retangulo_energia(c, 420, yb, 90, 400, E.COR, a, "4.000 W", "0,5 h", None, True))
        E.foco(c, t, C["s13.c"], 0.5, lambda a: retangulo_energia(c, 760, yb, 1000, 10, CLARO, a, None, "20 h", None, True))
        E.foco(c, t, C["s13.c"] + 0.3, 0.4, lambda a: E.formula(c, "100 W", 1260, yb - 40, 46, "b", BR, a, "center"))
        E.foco(c, t, C["s13.d"], 0.5, lambda a: (E.pilula(c, "2 kWh", 465, 360 + 60, 46, "g", fundo=E.COR, a=a),
                                                 E.pilula(c, "2 kWh", 1260, 640, 46, "g", fundo=E.COR, a=a)))
        E.frase(c, t, C["s13.e"], [("40×", "g", 56, BR)] + ps("a potência,", "i", 58, CLARO) + [("40×", "g", 56, BR)] + ps("menos tempo: mesmo gasto", "i", 58, CLARO),
                W / 2, 1000, "center", 0.1)
    E.saida(c, t, C["s14"] - 0.1, s13)
    if t < C["s14"]:
        return
    E.frase(c, t, C["s14.a"], [("E", "g", 70, BR)] + ps("proporcional à potência e ao tempo", "i", 70, CLARO), W / 2, 300, "center", 0.1)
    E.frase(c, t, C["s14.b"], ps("os que pesam:", "i", 62, CLARO) + [("chuveiro", "g", 60, BR), ("e", "i", 62, CLARO), ("geladeira", "g", 60, BR)], W / 2, 480, "center", 0.12)
    E.frase(c, t, C["s14.c"], [("kW", "g", 76, BR), ("=", "g", 76, CLARO), ("potência", "i", 80, CLARO)], W / 2, 700, "center", 0.12)
    E.frase(c, t, C["s14.d"], [("kWh", "g", 76, E.CLARO), ("=", "g", 76, CLARO), ("energia", "i", 80, CLARO)], W / 2, 840, "center", 0.12)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s15"], ps("hora de testar", "i", 72, COR), XE, 200)
    E.frase(c, t, C["s15.a"], [("aquecedor", "g", 66), ("1.500 W", "g", 66, COR)], XE, 360, passo=0.12)
    E.frase(c, t, C["s15.b"], [("2", "g", 64), ("horas", "i", 66), ("por", "i", 66), ("dia", "i", 66)], XE, 480, passo=0.1)
    E.frase(c, t, C["s15.c"], [("30", "g", 64), ("dias", "i", 66)], XE, 590, passo=0.1)
    E.frase(c, t, C["s15.d"], ps("tarifa:", "i", 64) + [("R$ 0,80", "g", 62), ("por", "i", 64), ("kWh", "g", 58, F.UNID)], XE, 700, passo=0.1)
    E.frase(c, t, C["s15.e"], ps("quanto custa no mês?", "g", 66, COR), XE, 860, passo=0.1)
    if t >= C["s16"]:
        E.relogio(c, t, C["s16.a"], cx=1450, cy=520, r=200)
    else:
        E.foco(c, t, C["s15.a"], 0.6, lambda a: aquecedor(c, t, 1200, 420, 520, 360, a))


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    E.formula_em(c, t, C["s17.a"], "1.500 W = 1,5 kW", XE, 280, 76, "g", TINTA)
    E.formula_em(c, t, C["s17.b"], "1,5 × 2 = 3 kWh por dia", XE, 430, 76, "g", TINTA)
    E.formula_em(c, t, C["s17.c"], "3 × 30 = ", XE, 580, 76, "g", TINTA)
    E.foco(c, t, C["s17.c"] + 0.5, 0.5, lambda a: F.medida(c, 90, "kWh", XE + 320, 580, 90, COR, a))
    E.formula_em(c, t, C["s17.d"], "90 × 0,8 =", XE, 760, 76, "g", TINTA)
    bola_reais(c, t, C["s17.e"], "R$ 72", XE + 640, 735, 110, 60, CERTO)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s18"], [("resumindo", "i", 92, COR)], W / 2, 190, "center")
        numero(c, t, C["s18.a"], 1, 400, 370, 48)
        E.formula_em(c, t, C["s18.a"] + 0.1, "E = P · Δt", 490, 396, 76, "g", TINTA)
        numero(c, t, C["s18.b"], 2, 400, 560, 48)
        E.formula_em(c, t, C["s18.b"] + 0.1, "kW × h = kWh", 490, 586, 76, "g", COR)
        numero(c, t, C["s18.c"], 3, 400, 750, 48)
        E.frase(c, t, C["s18.c"] + 0.1, [("conta", "g", 70), ("=", "g", 70, TINTA2), ("kWh", "g", 70, COR), ("×", "g", 70, TINTA2), ("tarifa", "g", 70, CERTO)],
                490, 776, passo=0.1)
    E.saida(c, t, C["s19"] - 0.1, resumo)
    if t < C["s19"]:
        return
    E.frase(c, t, C["s19"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C["s19.a"], [("chuveiro", "g", 100, COR)], XE, 390)
    E.frase(c, t, C["s19.a"] + 0.4, ps("na posição inverno", "i", 76), XE, 500, passo=0.12)
    E.frase(c, t, C["s19.b"], [("qual", "i", 76), ("lâmpada", "g", 72, COR), ("brilha", "i", 76), ("mais?", "i", 76)], XE, 650, passo=0.12)
    F.lampada(c, t, C["s19.b"] + 0.3, (260, 820), (520, 820), acesa=C["s19.b"] + 0.5, r=60)
    F.lampada(c, t, C["s19.b"] + 0.4, (600, 820), (860, 820), acesa=C["s19.b"] + 0.9, r=60)
    E.foco(c, t, C["s19.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 420, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s19.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(720, 445, p), ep(t, C["s19.c"] + 0.2, 0.4))
    E.frase(c, t, C["s19.d"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1570, 990, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, energia=b_energia, conta=b_conta, casa=b_casa, erro=b_erro, atalho=b_atalho,
              questao=b_questao, resposta=b_resposta, fim=b_fim)
