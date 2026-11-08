"""Visual — Estudativo · MAT-NUM-019: praticando expressões e números inteiros (7 − (−4) = 11; 40 − 3 × 25 + 2 × 10 = −15;
−2 × (5 − 9) − 12 ÷ 3 = 4; −3 + 2 × [4 − (1 − 6)] = 15).
Linguagem das aulas de origem: reta numérica com saltos (MAT-NUM-015 e 016), expressão que se resolve em linhas empilhadas com o
trecho da vez aceso (E.expressao, MAT-NUM-013 e 018), blocos cortados nos mais e menos que ligam uma conta na outra, cartão de
dívida em vermelho e entradas em verde. Cada questão: título "questão n", a pergunta e o relógio de pausa; resposta final na
pílula; erro em vermelho, certo em verde.
Peças locais: ps(), cf(), resp(), lista(), titulo(), bloco() (chave sob um trecho com o valor do bloco).
Todo instante vem de C[...] (marcadores do roteiro), para acompanhar a voz real quando ela chegar."""
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Números e Contas")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-NUM-019_praticando_expressoes_e_inteiros.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("q1", "q2", "q3", "q4", "fim"))
BR = "#FFFFFF"
assert 7 - (-4) == 11 and 40 - 3 * 25 + 2 * 10 == -15 and 40 + 20 - 75 == -15 and 40 - 75 == -35
assert -2 * (5 - 9) - 12 // 3 == 4 and -2 * 4 - 4 == -12
assert -3 + 2 * (4 - (1 - 6)) == 15 and -3 + 2 * (4 - 5) == -5


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças gerais ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def cf(c, partes, x, y, size, a=1.0, align="left", est="g"):
    ws = [E.formula(None, s, 0, 0, size, est, a=0) for s, _ in partes]
    xx = x - sum(ws) / 2 if align == "center" else x - sum(ws) if align == "right" else x
    if c is not None and a > 0:
        for (s, cor), wi in zip(partes, ws):
            E.formula(c, s, xx, y, size, est, cor, a)
            xx += wi
    return sum(ws)


def cf_em(c, t, t0, partes, x, y, size, align="left"):
    E.foco(c, t, t0, 0.5, lambda a: cf(c, partes, x, y, size, a, align))


def resp(c, t, t0, partes, cx, cy, size=64, alto=1.75, cor=None):
    if isinstance(partes, str):
        partes = [(partes, BR)]

    def f(a):
        w = cf(None, partes, 0, 0, size) + size * 1.1
        h = size * alto
        M.rrect(c, cx - w / 2, cy - h / 2, w, h, h / 2, cor or E.COR, a, shadow=True)
        cf(c, partes, cx, cy + size * 0.36, size, a, "center")
    E.foco(c, t, t0, 0.5, f)


def lista(c, t, itens, x, y0, dy=130, size=58):
    for i, (t0, partes) in enumerate(itens):
        y = y0 + i * dy
        E.foco(c, t, t0, 0.5, lambda a, i=i, y=y: (E.bola(c, x + 36, y - size * 0.36, 36, a=a),
                                                   centro(c, str(i + 1), x + 36, y - size * 0.36 + 16, 46, "g", BR, a)))
        E.frase(c, t, t0 + 0.1, partes, x + 100, y, "left", 0.1)


def titulo(c, t, t0, n, nome, x=XE, y=150):
    E.frase(c, t, t0, ps("questão", "i", 64, COR) + [(str(n), "g", 72, COR)] + ps(f"· {nome}", "i", 56, TINTA2), x, y, "left", 0.1)


def trecho_x(s, trecho, cx, size):
    """x inicial e final de um trecho dentro de s escrito centrado em cx (estilo g)"""
    x = cx - E.larg(s, "g", size) / 2
    i0 = s.find(trecho)
    ate = lambda u: E.larg(u, "g", size) + (E.APERTO["g"] * size if u else 0)
    return x + ate(s[:i0]), x + ate(s[:i0]) + E.larg(trecho, "g", size)


def bloco(c, t, t0, s, trecho, cx, y, size, rot, cor=None, dy=90):
    """chave sob um trecho da expressão, com o valor do bloco embaixo"""
    x0, x1 = trecho_x(s, trecho, cx, size)
    q = ep(t, t0, 0.5)
    if q > 0:
        E.chave(c, x0, x1, y + size * 0.3, cor or COR, q, 24)
        E.foco(c, t, t0 + 0.2, 0.4, lambda a: E.formula(c, rot, (x0 + x1) / 2, y + size * 0.3 + dy, size * 0.62, "g", cor or COR, a, "center"))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    a1, b1, c1 = C["s01.a"], C["s01.b"], C["s01.c"]
    E.foco(c, t, a1, 0.5, lambda a: E.escreve(c, "4", XE - 8, 520, 340, "g", COR, a))
    E.foco(c, t, a1 + 0.15, 0.5, lambda a: E.escreve(c, "questões", XE + E.larg("4", "g", 340) + 30, 500, 110, "i", TINTA, a))
    for i, s in enumerate(("sinais", "( )  [ ]")):
        E.foco(c, t, lerp(a1 + 0.8, b1, 0.3 + 0.4 * i), 0.5, lambda a, s=s, i=i: E.pilula(c, s, 1250 + i * 380, 260, 60, "g", a=a, cor=E.SOBRE))
    E.foco(c, t, b1, 0.5, lambda a: E.divida(c, 1450, 520, 360, 220, "R$ −15", a, topo="saldo", cor=ERRADO))
    E.frase(c, t, c1, ps("em cada uma,", "i", 62) + [("pause e resolva", "g", 66, COR)], XE, 780, "left", 0.1)
    E.frase(c, t, c1 + 1.4, ps("antes de ver a resposta", "i", 62), XE, 880, "left", 0.1)
    E.frase(c, t, C["s01.end"] - 2.6, ps("errar aqui", "i", 56, TINTA2) + [("não custa nada", "g", 58, CERTO)], XE, 1000, "left", 0.1)


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    k = {x: C[f"s02.{x}"] for x in "abcde"}
    E.frase(c, t, C["s02"] + 0.1, ps("você vai usar", "i", 70, COR), XE, 180, "left", 0.1)
    lista(c, t, [(k["a"], ps("a", "i", 58) + [("ordem das operações", "g", 62)]),
                 (k["b"], [("montar a expressão", "g", 62)] + ps("de um problema", "i", 58)),
                 (k["c"], ps("a", "i", 58) + [("reta numérica", "g", 62)]),
                 (k["d"], [("dívida e pagamento", "g", 62, COR)]),
                 (k["e"], ps("a", "i", 58) + [("regra de sinais", "g", 62)])], XE, 340, 135, 58)
    E.frase(c, t, C["s02.end"] - 2.4, ps("travou?", "i", 56, COR) + ps("procure a aula no canal", "i", 56), XE, 1010, "left", 0.12)


# ---------------- questão 1: a temperatura ----------------
def termometro(c, x, y, h, nivel, cor, a):
    """termômetro simples: nivel de 0 a 1"""
    M.rrect(c, x - 22, y, 44, h, 22, BR, a, shadow=True)
    M.rrect(c, x - 22, y, 44, h, 22, TINTA, a * 0.8, stroke=4)
    hh = (h - 30) * nivel
    M.rrect(c, x - 10, y + h - 15 - hh, 20, hh, 10, cor, a)
    c.drawCircle(x, y + h + 20, 40, M.paint(cor, a))


def b_q1(c, t, C, b):
    a3, b3, c3, d3 = (C[f"s03.{k}"] for k in "abcd")
    titulo(c, t, a3, 1, "reta e subtração")
    E.foco(c, t, b3, 0.5, lambda a: termometro(c, XE + 60, 300, 360, 0.18, E.COR, a))
    E.frase(c, t, b3, ps("madrugada", "i", 60, TINTA2), XE + 160, 430, "left", 0.1)
    E.foco(c, t, b3 + 0.4, 0.5, lambda a: E.escreve(c, "−4 °C", XE + 160, 560, 110, "g", E.COR, a))
    E.foco(c, t, c3, 0.5, lambda a: termometro(c, 820, 300, 360, 0.7, ERRADO, a))
    E.frase(c, t, c3, ps("tarde", "i", 60, TINTA2), 920, 430, "left", 0.1)
    E.foco(c, t, c3 + 0.4, 0.5, lambda a: E.escreve(c, "7 °C", 920, 560, 110, "g", ERRADO, a))
    E.frase(c, t, d3, ps("quantos graus", "i", 70) + [("subiu?", "g", 78, COR)], XE, 880, "left", 0.1)
    E.relogio(c, t, C["s04.a"], 1560, 470, 170)


def b_r1(c, t, C, b):
    a5, b5, c5 = (C[f"s05.{k}"] for k in "abc")
    a6, b6, c6, d6 = (C[f"s06.{k}"] for k in "abcd")
    E.frase(c, t, a5, ps("subiu =", "i", 62) + [("final − começo", "g", 66, COR)], W / 2, 170, "center", 0.1)
    E.expressao(c, t, [("7 − (−4)", "− (−4)", b5), ("7 + 4", "7 + 4", c5 - 0.3), ("11", "11", c5 + 0.6)], [c5 - 0.3, c5 + 0.6],
                W / 2, 330, 120, t0=b5)
    resp(c, t, c5 + 1.0, "subiu 11 graus", W / 2 + 420, 300, 60, cor=CERTO)
    y, x0, x1 = 720, 260, 1660
    vx = E.reta(c, t, C["s06"] - 0.2, x0, x1, y, -5, 8, list(range(-5, 9)), fmt=lambda v: E._num(v), size=46)
    if t >= a6:
        k = ease_back(prog(t, a6, 0.4))
        c.drawCircle(vx(-4), y, 16 * k, M.paint(E.COR))
    E.salto(c, t, a6 + 0.2, vx(-4), vx(0), y, 110, E.COR, "4 passos", size=48)
    E.salto(c, t, b6, vx(0), vx(7), y, 150, ERRADO, "7 passos", size=48)
    if t >= b6 + 0.7:
        k = ease_back(prog(t, b6 + 0.7, 0.4))
        c.drawCircle(vx(7), y, 16 * k, M.paint(ERRADO))
    E.foco(c, t, c6, 0.5, lambda a: E.pilula(c, "4 + 7 = 11 passos", W / 2, 890, 56, "g", a=a, cor=E.SOBRE))
    E.frase(c, t, d6, [("3?", "g", 64, ERRADO)] + ps("é", "i", 56, ERRADO) + [("7 − 4,", "g", 60, ERRADO)] + ps("como se fizesse +4 °C", "i", 56, ERRADO),
            W / 2, 1000, "center", 0.1)


# ---------------- questão 2: o saldo ----------------
def b_q2(c, t, C, b):
    a7, b7, c7, d7, e7 = (C[f"s07.{k}"] for k in "abcde")
    titulo(c, t, a7, 2, "montar a expressão")
    E.frase(c, t, b7, ps("saldo:", "i", 62), XE, 360, "left", 0.1)
    E.foco(c, t, b7 + 0.3, 0.5, lambda a: E.escreve(c, "R$ 40", XE + 230, 365, 90, "g", TINTA, a))
    E.frase(c, t, c7, ps("paga", "i", 62) + [("3 boletos", "g", 66, ERRADO)] + ps("de R$ 25", "i", 62), XE, 520, "left", 0.1)
    E.frase(c, t, d7, ps("recebe", "i", 62) + [("2 transferências", "g", 66, CERTO)] + ps("de R$ 10", "i", 62), XE, 680, "left", 0.1)
    E.frase(c, t, e7, ps("uma", "i", 66) + [("expressão", "g", 72, COR)] + ps("só", "i", 66), XE, 860, "left", 0.1)
    E.frase(c, t, e7 + 1.0, ps("e o", "i", 66) + [("saldo final?", "g", 72, COR)], XE, 960, "left", 0.1)
    E.relogio(c, t, C["s08.a"], 1560, 470, 170)


S2 = "40 − 3 × 25 + 2 × 10"


def b_r2(c, t, C, b):
    a9, b9, c9 = (C[f"s09.{k}"] for k in "abc")
    a0, b0, c0, d0, e0 = (C[f"s10.{k}"] for k in "abcde")
    a1, b1, c1, d1 = (C[f"s11.{k}"] for k in "abcd")

    def montar():
        E.frase(c, t, a9, ps("saldo", "i", 64) + [("− o que saiu", "g", 66, ERRADO), ("+ o que entrou", "g", 66, CERTO)], W / 2, 200, "center", 0.12)
        E.formula_em(c, t, b9, S2, W / 2, 400, 120, "g", TINTA, "center")
        E.frase(c, t, c9, ps("sem parêntese:", "i", 56, TINTA2) + [("o vezes já vem antes", "g", 58, COR)], W / 2, 640, "center", 0.1)
        bloco(c, t, a0, S2, "3 × 25", W / 2, 400, 120, "75", ERRADO)
        bloco(c, t, b0, S2, "2 × 10", W / 2, 400, 120, "20", CERTO)
        E.expressao(c, t, [("40 − 75 + 20", "40 − 75", c0), ("−35 + 20", "−35 + 20", d0), ("−15", "−15", e0)], [d0 - 0.3, e0 - 0.3],
                    W / 2, 760, 110, t0=c0 - 0.4)
        resp(c, t, e0, "saldo: R$ −15", W / 2, 930, 64, cor=ERRADO)
    E.saida(c, t, C["s11"] - 0.1, montar)
    if t < C["s11"] - 0.1:
        return
    E.frase(c, t, a1, ps("o atalho:", "i", 64, COR) + [("entradas e saídas", "g", 70)], W / 2, 200, "center", 0.1)
    E.frase(c, t, b1, ps("entrou", "i", 60, CERTO), 520, 380, "center", 0.1)
    cf_em(c, t, b1 + 0.3, [("40 + 20 = 60", CERTO)], 520, 500, 90, "center")
    E.frase(c, t, c1, ps("saiu", "i", 60, ERRADO), 1400, 380, "center", 0.1)
    cf_em(c, t, c1 + 0.3, [("75", ERRADO)], 1400, 500, 90, "center")
    cf_em(c, t, d1, [("60 − 75 = −15", TINTA)], W / 2, 720, 110, "center")
    E.foco(c, t, d1 + 1.4, 0.5, lambda a: E.selo(c, W / 2, 880, 50, True, a))


# ---------------- questão 3: sinais e parênteses ----------------
S3 = "−2 × (5 − 9) − 12 ÷ 3"


def b_q3(c, t, C, b):
    a2, b2, c2 = (C[f"s12.{k}"] for k in "abc")
    titulo(c, t, a2, 3, "sinais e parênteses")
    E.frase(c, t, a2 + 0.6, ps("resolva:", "i", 66), XE, 380, "left", 0.1)
    E.formula_em(c, t, b2, "−2 × (5 − 9)", XE, 560, 120, "g", TINTA)
    E.formula_em(c, t, c2, "− 12 ÷ 3", XE + 20, 740, 120, "g", TINTA)
    E.relogio(c, t, C["s13.a"], 1560, 470, 170)


def b_r3(c, t, C, b):
    a4, b4, c4 = (C[f"s14.{k}"] for k in "abc")
    a5, b5, c5, d5 = (C[f"s15.{k}"] for k in "abcd")
    a6, b6, c6, d6 = (C[f"s16.{k}"] for k in "abcd")

    def certo():
        E.expressao(c, t, [(S3, "(5 − 9)", a4), ("−2 × (−4) − 12 ÷ 3", "−2 × (−4)", a5), ("8 − 4", "8 − 4", d5)],
                    [b4, b5], W / 2, 270, 104, empilha=230, t0=C["s14"])
        E.foco(c, t, b4, 0.5, lambda a: E.divida(c, 1650, 300, 220, 150, "−4", a, topo="deve", cor=ERRADO))
        # o corte no menos do meio
        if C["s14.c"] <= t < d5:
            s = "−2 × (−4) − 12 ÷ 3"
            x0, x1 = trecho_x(s, " − ", W / 2, 104)
            q = ep(t, c4, 0.4)
            xm = (x0 + x1) / 2
            M.line(c, xm, 500 - 110, xm, 500 + 40, COR, q, 6, dash=[14, 10])
            E.foco(c, t, c4 + 0.6, 0.4, lambda a: E.escreve(c, "sinal colado: fica no bloco", 260, 1000, 50, "i", TINTA2, a))
        bloco(c, t, b5, "−2 × (−4) − 12 ÷ 3", "−2 × (−4)", W / 2, 500, 104, "+8", CERTO, 76)
        bloco(c, t, c5, "−2 × (−4) − 12 ÷ 3", "12 ÷ 3", W / 2, 500, 104, "4", COR, 76)
        sinal_ = E.foco(c, t, d5 + 0.6, 0.4, lambda a: E.escreve(c, "=", W / 2 + 200, 730, 104, "g", TINTA, a))
        resp(c, t, d5 + 0.8, "4", W / 2 + 400, 695, 84, cor=CERTO)
    E.saida(c, t, C["s16"] - 0.1, certo)
    if t < C["s16"] - 0.1:
        return
    E.frase(c, t, a6, ps("o erro:", "i", 62) + [("5 − 9 = 4", "g", 70, ERRADO)], W / 2, 220, "center", 0.1)
    if t >= a6 + 1.0:
        x0, x1 = W / 2 - 40, W / 2 + 300
        E.risco(c, x0 + 60, 240, x1, 160, t, a6 + 1.0, largura=10)
    cf_em(c, t, b6, [("−2 × 4 = −8", ERRADO)], W / 2, 420, 96, "center")
    cf_em(c, t, c6, [("−8 − 4 = −12", ERRADO)], W / 2, 580, 96, "center")
    E.foco(c, t, c6 + 0.6, 0.5, lambda a: E.selo(c, W / 2 + 420, 550, 46, False, a))
    E.frase(c, t, d6, ps("tirou", "i", 62) + [("mais do que tem?", "g", 66, COR)], W / 2, 800, "center", 0.1)
    E.frase(c, t, d6 + 1.2, ps("o resultado é", "i", 62) + [("negativo", "g", 66, ERRADO)], W / 2, 900, "center", 0.1)


# ---------------- questão 4: colchetes ----------------
S4 = "−3 + 2 × [4 − (1 − 6)]"


def b_q4(c, t, C, b):
    a7, b7, c7, d7 = (C[f"s17.{k}"] for k in "abcd")
    titulo(c, t, a7, 4, "colchetes")
    E.frase(c, t, a7 + 0.6, ps("resolva:", "i", 66), XE, 380, "left", 0.1)
    partes = [("−3 + 2 × [", TINTA, b7), ("4 − (", COR, c7), ("1 − 6", ERRADO, d7), (")", COR, d7 + 0.3), ("]", TINTA, d7 + 0.5)]
    x = XE
    for txt, cor, ti in partes:
        E.foco(c, t, ti, 0.5, lambda a, txt=txt, cor=cor, x=x: E.formula(c, txt, x, 600, 110, "g", cor, a))
        x += E.formula(None, txt, 0, 0, 110, "g", a=0) + 18
    E.relogio(c, t, C["s18.a"], 1560, 470, 170)


def b_r4(c, t, C, b):
    a9, b9, c9 = (C[f"s19.{k}"] for k in "abc")
    a0, b0, c0, d0 = (C[f"s20.{k}"] for k in "abcd")
    a1, b1, c1, d1, e1 = (C[f"s21.{k}"] for k in "abcde")

    def certo():
        E.frase(c, t, C["s19"], ps("de dentro", "i", 60, COR) + ps("para fora", "i", 60), W / 2, 150, "center", 0.1)
        E.expressao(c, t, [(S4, "(1 − 6)", C["s19"] + 0.6), ("−3 + 2 × [4 − (−5)]", "4 − (−5)", b9), ("−3 + 2 × 9", "2 × 9", a0),
                           ("−3 + 18", "−3 + 18", b0), ("15", "15", d0)],
                    [a9, c9, a0 + 0.6, d0 - 0.2], W / 2, 290, 96, empilha=150, t0=C["s19"] + 0.2)
        E.foco(c, t, c9 - 0.4, 0.5, lambda a: E.pilula(c, "tirar dívida = ganhar", 1600, 425, 44, "g", a=a, cor=E.SOBRE))
        resp(c, t, d0 + 0.6, "15", 1500, 905, 80, cor=CERTO)
    E.saida(c, t, C["s21"] - 0.1, certo)
    if t < C["s21"] - 0.1:
        return
    E.frase(c, t, C["s21"] + 0.1, ps("a", "i", 62) + [("pegadinha", "g", 70, ERRADO)] + ps("no colchete", "i", 62), W / 2, 200, "center", 0.1)
    cf_em(c, t, a1, [("4 − (−5)", TINTA)], 620, 400, 100, "center")
    E.frase(c, t, a1 + 0.6, ps("jogou fora um menos", "i", 52, ERRADO), 620, 500, "center", 0.1)
    cf_em(c, t, b1, [("4 − 5 = −1", ERRADO)], 1300, 400, 100, "center")
    cf_em(c, t, c1, [("2 × (−1) = −2", ERRADO)], 1300, 560, 84, "center")
    cf_em(c, t, d1, [("−3 − 2 = −5", ERRADO)], 1300, 700, 84, "center")
    E.foco(c, t, d1 + 0.5, 0.5, lambda a: E.selo(c, 1650, 675, 44, False, a))
    E.foco(c, t, e1, 0.5, lambda a: E.caixa_pontilhada(c, 300, 820, 1320, 170, a, COR, prog_=ep(t, e1, 0.6)))
    E.frase(c, t, e1 + 0.1, [("− (−5)", "g", 76, COR), ("vira", "i", 66), ("+ 5", "g", 76, CERTO)], W / 2, 930, "center", 0.12)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s22"] + 0.1, [("resumindo", "i", 92, COR)], W / 2, 200, "center")
        itens = (("s22.a", "de dentro", "para fora"), ("s22.b", "vezes e dividido", "antes de mais e menos"),
                 ("s22.c", "o sinal se decide", "a cada passo"))
        for i, (k, l1, l2) in enumerate(itens):
            y = 380 + i * 200
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 230, y - 30, 56, a=a),
                                                         centro(c, str(i + 1), 230, y - 7, 64, "g", E.SOBRE, a)))
            E.frase(c, t, C[k] + 0.1, ps(l1, "i", 68) + [(l2, "g", 70, COR)], 320, y, "left", 0.1)
        E.frase(c, t, C["s22.end"] - 2.4, ps("trilha de números e contas:", "i", 56, TINTA2) + [("completa", "g", 60, CERTO)], 320, 1000, "left", 0.1)
    E.saida(c, t, C["s23"] - 0.1, resumo)
    if t < C["s23"] - 0.1:
        return
    a3, b3, c3, d3, e3 = (C[f"s23.{k}"] for k in "abcde")
    E.frase(c, t, C["s23"], ps("o próximo assunto", "i", 72), XE, 230, "left", 0.1)
    E.frase(c, t, a3, [("múltiplos e divisores", "g", 100, COR)], XE, 380, "left", 0.1)
    cf_em(c, t, b3, [("54 é múltiplo de 6?", TINTA)], XE, 560, 80)
    cf_em(c, t, c3, [("os divisores de 36", TINTA)], XE, 700, 80)
    E.foco(c, t, d3, 0.5, lambda a: E.pilula(c, "Inscreva-se", 1460, 560, 76, estilo="g", a=a, cor=E.SOBRE))
    p = ease_io(prog(t, d3 + 0.3, 0.8))
    E.cursor(c, lerp(1790, 1590, p), lerp(800, 585, p), ep(t, d3 + 0.2, 0.4))
    E.frase(c, t, e3, [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 960, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, q1=b_q1, r1=b_r1, q2=b_q2, r2=b_r2, q3=b_q3, r3=b_r3, q4=b_q4, r4=b_r4, fim=b_fim)
