"""Visual — Estudativo · MAT-EQU-015: resolver inequação do 1º grau.
−2x < 6 → x > −3 (bolinha aberta, pinta à direita); 3x − 2 ≤ 7 → x ≤ 3 (fechada, à esquerda); questão −4x + 2 ≥ 10 → x ≤ −2.
Instantes: cues C[...] e, para números ditos no meio da frase, pal(cena, palavra) lê o instante da palavra na voz real."""
import json
from pathlib import Path

import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_out, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Equações do 1º Grau")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-EQU-015_resolver_inequacao.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("oque", "porque", "resolver", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
MENOS = lambda v: str(v).replace("-", "−")

# as contas da aula
assert -2 * 0 < 6 and not (0 < -3) and 3 * 3 - 2 == 7 and (7 + 2) / 3 == 3
assert -2 < 3 and -2 > -3 and 6 / -3 == -2 and 9 / -3 == -3 and 2 + 10 < 3 + 10 and 2 * 10 < 3 * 10
assert 6 / -2 == -3 and -2 * -3 == 6 and not (6 < 6) and -12 / 3 == -4 and not (3 * 0 < -12)
assert (10 - 2) / -4 == -2 and -4 * 0 + 2 == 2 and not (2 >= 10) and -4 * -2 + 2 == 10


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- instante de uma palavra na voz ----------------
_T = json.loads((Path(__file__).resolve().parents[1] / "audio" / "tempos.json").read_text(encoding="utf-8"))
_TOK = {s["id"]: (s["start"], s["tokens"]) for s in _T["scenes"]}


def pal(sid, palavra, n=1):
    """instante em que a n-ésima ocorrência de `palavra` começa na cena sid"""
    st, toks = _TOK[sid]
    k = 0
    for tk in toks:
        if tk["disp"].lower().strip(".,:;!?") == palavra:
            k += 1
            if k == n:
                return st + tk["t0"]
    raise KeyError((sid, palavra, n))


# ---------------- peças desta aula ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def cen(c, t, t0, s, cx, y, size, cor=None, est="g"):
    E.foco(c, t, t0, 0.5, lambda a: centro(c, s, cx, y, size, est, cor or TINTA, a))


def fcen(c, t, t0, s, cx, y, size, cor=None):
    E.formula_em(c, t, t0, s, cx, y, size, "g", cor, "center")


def relacao(c, a, esq, sig, dir_, y, size, cor=None, xm=W / 2, cor_sig=None):
    """equação ou inequação alinhada pelo sinal em xm"""
    g = size * 0.5
    E.formula(c, esq, xm - g, y, size, "g", cor, a, "right")
    centro(c, sig, xm, y, size, "g", cor_sig or cor, a)
    E.formula(c, dir_, xm + g, y, size, "g", cor, a)


def pilha(c, t, linhas, ops, xm, y0, dy, size, sinal_novo=None):
    """resolução em linhas: linhas = [(t0, esq, sinal, dir)], ops = [(t0, op)] escrita sob os dois lados, entre a linha k e a k+1.
    A linha antiga fica cinza quando a nova chega; a última fica na cor da matéria. sinal_novo = índice da linha cujo sinal virou (em vermelho)."""
    g = size * 0.5
    for k, (t0, esq, sig, dir_) in enumerate(linhas):
        y = y0 + k * dy
        ult = k == len(linhas) - 1
        velha = not ult and t >= linhas[k + 1][0]
        cor = COR if ult else (CINZA if velha else TINTA)
        cs = ERRADO if k == sinal_novo else None
        E.foco(c, t, t0, 0.5, lambda a, esq=esq, sig=sig, dir_=dir_, y=y, cor=cor, cs=cs: relacao(c, a, esq, sig, dir_, y, size, cor, xm, cs))
        if k < len(ops):
            to, op = ops[k]
            we = E.formula(c, esq, 0, 0, size, a=0)
            wd = E.formula(c, dir_, 0, 0, size, a=0)
            cop = CINZA if velha else COR
            yo = y + size * 0.72
            for cx in (xm - g - we / 2, xm + g + wd / 2):
                E.foco(c, t, to, 0.45, lambda a, cx=cx, cop=cop: E.formula(c, op, cx, yo, size * 0.52, "b", cop, a, "center"), sobe=8)


def bolinha(c, t, t0, x, y, fecha, cor=None, r=19):
    """bolinha da reta: cheia = o número entra; aberta = fica de fora"""
    cor = cor or COR
    k = ease_back(prog(t, t0, 0.5))
    if k <= 0:
        return
    rr = r * k
    c.drawCircle(x, y, rr, M.paint(cor if fecha else E.PAPEL))
    c.drawCircle(x, y, rr, M.paint(cor, 1.0, stroke=7))


def pinta(c, t, t0, x_ini, x_fim, y, cor=None, d=0.9):
    """trecho pintado da reta, crescendo de x_ini para x_fim, com ponta de seta no fim"""
    p = ease_out(prog(t, t0, d))
    if p <= 0:
        return
    cor = cor or COR
    xm = lerp(x_ini, x_fim, p)
    M.line(c, x_ini, y, xm, y, cor, 1.0, 12, cap_round=False)
    if p >= 0.99:
        lado = 1 if x_fim > x_ini else -1
        M.line(c, x_fim, y, x_fim - lado * 26, y - 18, cor, 1.0, 8)
        M.line(c, x_fim, y, x_fim - lado * 26, y + 18, cor, 1.0, 8)


def ponto(c, t, t0, x, y, cor, r=16):
    E.foco(c, t, t0, 0.4, lambda a: c.drawCircle(x, y, r, M.paint(cor, a)), blur=4)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    ka, kb, kc, kd = C["s01.a"], C["s01.b"], C["s01.c"], C["s01.d"]

    def erro():
        fcen(c, t, ka, "−2x < 6", 520, 300, 140)
        E.ponte(c, t, pal("s01", "divide"), 800, 1110, 255, "÷ (−2)", None, 56)
        fcen(c, t, kb, "x < −3", 1380, 300, 140)
        E.risco(c, 1150, 330, 1620, 230, t, pal("s01", "alguma"), ERRADO, 14)
        E.frase(c, t, pal("s01", "teste"), ps("teste o", "i", 84) + [("zero", "g", 90, COR)], W / 2, 520, "center", 0.12)
        fcen(c, t, kc, "−2 × 0 = 0", 520, 690, 100)
        fcen(c, t, pal("s01", "zero", 4), "0 < 6", 470, 860, 110)
        E.foco(c, t, pal("s01", "serve"), 0.5, lambda a: E.selo(c, 720, 822, 52, True, a))
        fcen(c, t, kd, "0 < −3", 1330, 860, 110)
        E.foco(c, t, pal("s01", "não"), 0.5, lambda a: E.selo(c, 1620, 822, 52, False, a))
    E.saida(c, t, C["s02"] - 0.1, erro)
    if t < C["s02"]:
        return
    ta, tb, tc = C["s02.a"], C["s02.b"], C["s02.c"]
    E.foco(c, t, tc - 0.2, 0.7, lambda a: E.bola(c, 1560, 560, 220 * ease_back(prog(t, tc - 0.2, 0.7))), blur=0)
    E.frase(c, t, ta, ps("até o fim desta aula", "i", 90), XE, 300, passo=0.14)
    E.frase(c, t, pal("s02", "resolve"), ps("resolver", "i", 90) + [("−2x < 6", "g", 100, COR)], XE, 450, passo=0.14)
    E.frase(c, t, tb - 0.3, ps("entender", "i", 90) + [("por que o sinal vira", "g", 84)], XE, 600, passo=0.14)
    E.foco(c, t, tc + 0.1, 0.5, lambda a: (centro(c, "e marcar", 1560, 545, 72, "i", E.SOBRE, a),
                                           centro(c, "na reta", 1560, 630, 80, "g", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"] + 0.3, ps("você precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "2", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 240, 700, 120, "i", TINTA, a))
    x, w = 940, 820
    itens = (("s03.b", "resolver equação fazendo", "o mesmo nos dois lados"), ("s03.c", "a reta numérica:", "à direita é maior"))
    for i, (k, l1, l2) in enumerate(itens):
        y = 240 + i * 260
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 196, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 62)], x + 44, y + 84)
        E.frase(c, t, C[k] + 0.3, [(l2, "g", 60, COR)], x + 44, y + 160)
    py = lerp(410, 670, ease_io(prog(t, C["s03.c"] - 0.35, 0.5)))
    E.cursor(c, x + w - 30, py, ep(t, C["s03.b"], 0.4))
    E.frase(c, t, pal("s03", "se"), ps("faltou alguma?", "i", 62, COR) + ps("procure no canal", "i", 62), 940, 800, "left", 0.12)


# ---------------- o que é ----------------
def b_oque(c, t, C, b):
    def sinais():
        ka, kb, kc, kd = C["s04.a"], C["s04.b"], C["s04.c"], C["s04.d"]
        E.frase(c, t, ka, [("inequação", "g", 140, COR)], W / 2, 220, "center")
        E.frase(c, t, pal("s04", "como"), ps("como uma equação, mas no lugar do", "i", 72) + [("=", "g", 90)], W / 2, 350, "center", 0.09)
        for i, (s, nome, k) in enumerate(((">", "maior", kb), ("<", "menor", pal("s04", "menor")),
                                          ("≥", "maior ou igual", kc), ("≤", "menor ou igual", pal("s04", "menor", 2)))):
            x = 330 + i * 420
            cen(c, t, k, s, x, 590, 170, COR)
            cen(c, t, k + 0.1, nome, x, 690, 56, TINTA, "i")
        E.frase(c, t, kd, ps("a resposta", "i", 76) + [("não é um número só:", "g", 76)], W / 2, 860, "center", 0.1)
        E.frase(c, t, pal("s04", "monte"), ps("é um", "i", 84) + [("monte de números", "g", 90, COR)], W / 2, 980, "center", 0.12)
    E.saida(c, t, C["s05"] - 0.1, sinais)

    def balanca_():
        ka, kb, kc, kd, ke = C["s05.a"], C["s05.b"], C["s05.c"], C["s05.d"], C["s05.e"]
        linhas = ((ka, "3x − 2", "≤", "7"), (kc, "3x", "≤", "9"), (ke, "x", "≤", "3"))
        ops = ((kb, "+ 2"), (kd, "÷ 3"))
        pilha(c, t, linhas, ops, 520, 300, 240, 120)
        tb = pal("s05", "balança")
        E.foco(c, t, tb, 0.6, lambda a: E.balanca(c, 1400, 600, "3x − 2", "7", 0.45 * ease_out(prog(t, tb + 0.3, 0.8)), a, size=72, larg_braco=520), blur=6)
        E.frase(c, t, tb + 0.5, ps("o lado do 7 pesa", "i", 56, TINTA2) + [("mais ou igual", "g", 56, TINTA2)], 1400, 960, "center", 0.08)
    if C["s05"] - 0.1 <= t:
        E.saida(c, t, C["s06"] - 0.1, balanca_)
    if t < C["s06"]:
        return
    ka, kb, kc, kd = C["s06.a"], C["s06.b"], C["s06.c"], C["s06.d"]
    fcen(c, t, C["s06"], "x ≤ 3", W / 2, 190, 130, COR)
    E.frase(c, t, ka, ps("todo número", "i", 76) + [("à esquerda do 3", "g", 76)] + ps("serve", "i", 76), W / 2, 330, "center", 0.11)
    E.frase(c, t, pal("s06", "próprio"), ps("e o próprio", "i", 70) + [("3", "g", 76, COR)] + ps("também:", "i", 70), 720, 450, "center", 0.11)
    fcen(c, t, kb, "3 × 3 − 2 = 7", 1300, 450, 76)
    x0, x1, y = 220, 1700, 680
    vx = E.reta(c, t, ka - 0.4, x0, x1, y, -2, 6, range(-2, 7), MENOS, size=56)
    pinta(c, t, kd, vx(3), 90, y)
    bolinha(c, t, kc, vx(3), y, True)
    E.frase(c, t, kc + 0.2, ps("bolinha", "i", 70) + [("fechada:", "g", 72, COR)] + ps("o 3", "i", 70) + [("entra", "g", 72, COR)], W / 2, 900, "center", 0.11)


# ---------------- por que vira ----------------
def b_porque(c, t, C, b):
    x0, x1, yr = 260, 1660, 640
    vx = lambda v: x0 + (v + 4) / 8 * (x1 - x0)

    def troca():
        ka, kb, kc = C["s07.a"], C["s07.b"], C["s07.c"]
        a8, b8, c8 = C["s08.a"], C["s08.b"], C["s08.c"]
        E.frase(c, t, ka - 0.3, ps("o problema:", "i", 72) + [("número negativo", "g", 76, ERRADO)], W / 2, 140, "center", 0.11)
        fcen(c, t, kb, "2 < 3", 520, 330, 130)
        E.ponte(c, t, pal("s07", "ponha"), 760, 1040, 285, "com menos", None, 50)
        fcen(c, t, kc, "−2", 1210, 330, 130)
        fcen(c, t, pal("s07", "menos", 3), "−3", 1550, 330, 130)
        E.foco(c, t, kc + 0.3, 0.5, lambda a: centro(c, "?" if t < b8 else ">", 1380, 330, 130, "g", CINZA if t < b8 else ERRADO, a))
        E.reta(c, t, kb + 0.2, x0, x1, yr, -4, 4, range(-4, 5), MENOS, size=52)
        ponto(c, t, kb + 0.3, vx(2), yr, TINTA2)
        ponto(c, t, kb + 0.5, vx(3), yr, TINTA2)
        ponto(c, t, kc, vx(-2), yr, COR)
        ponto(c, t, pal("s07", "menos", 3), vx(-3), yr, COR)
        if t >= a8:
            M.arrow(c, vx(-3), yr - 70, vx(-2) + 6, yr - 70, COR, ep(t, a8, 0.4), 6, 20, ep(t, a8, 0.5))
        E.frase(c, t, a8, ps("−2 fica", "i", 60) + [("mais à direita", "g", 60, COR)], vx(-2.5), yr - 110, "center", 0.1)
        E.frase(c, t, b8, ps("então", "i", 76) + [("−2 > −3", "g", 84, COR)], W / 2, 850, "center", 0.12)
        E.frase(c, t, c8, ps("o sinal de", "i", 72) + [("<", "g", 84)] + ps("virou", "i", 72) + [(">", "g", 84, ERRADO)], W / 2, 980, "center", 0.12)
    E.saida(c, t, C["s09"] - 0.1, troca)
    if t < C["s09"] - 0.1:
        return
    ka, kb, kc, kd, ke, kf, kg, kh = (C[f"s09.{k}"] for k in "abcdefgh")

    def divide():
        E.frase(c, t, ka - 1.2, ps("pôr o menos é", "i", 76) + [("multiplicar por −1", "g", 80, COR)], W / 2, 170, "center", 0.12)
        fcen(c, t, kb, "6 < 9", 520, 420, 130)
        E.ponte(c, t, pal("s09", "divida"), 760, 1060, 375, "÷ (−3)", None, 56)
        fcen(c, t, pal("s09", "seis", 2), "−2", 1220, 420, 130)
        fcen(c, t, pal("s09", "nove", 2), "−3", 1560, 420, 130)
        E.foco(c, t, kc, 0.5, lambda a: centro(c, ">", 1390, 420, 130, "g", ERRADO, a))
        E.foco(c, t, kd, 0.5, lambda a: E.bola(c, XE + 50, 670, 50, a=a))
        E.frase(c, t, kd, ps("multiplicou ou dividiu por", "i", 80) + [("negativo:", "g", 84, COR)], XE + 130, 695, "left", 0.1)
        E.frase(c, t, kd + 1.5, [("vira o sinal", "g", 130, COR)], XE + 130, 860)
    E.saida(c, t, ke - 0.1, divide)
    if t < ke:
        return
    E.frase(c, t, ke, ps("vira só com negativo.", "i", 72, TINTA2) + [("não vira:", "g", 76)], W / 2, 160, "center", 0.11)
    for x, k, tit, k2, l1, l2, l3, t1, t2, t3 in (
            (520, ke, "somar e tirar", kf, "2 + 10 = 12", "3 + 10 = 13", "12 < 13", pal("s09", "dois", 3), pal("s09", "três", 4), pal("s09", "doze", 2)),
            (1400, kg, "× ou ÷ por positivo", kh, "2 × 10 = 20", "3 × 10 = 30", "20 < 30", kh, pal("s09", "três", 5), pal("s09", "vinte", 2))):
        E.foco(c, t, k, 0.5, lambda a, x=x: E.caixa_pontilhada(c, x - 380, 240, 760, 760, a, prog_=a))
        cen(c, t, k + 0.1, tit, x, 340, 72, COR)
        fcen(c, t, t1, l1, x, 510, 96)
        fcen(c, t, t2, l2, x, 650, 96)
        fcen(c, t, t3, l3, x - 50, 840, 110, CERTO)
        E.foco(c, t, t3 + 0.6, 0.5, lambda a, x=x: E.selo(c, x + 280, 805, 42, True, a))


# ---------------- resolvendo ----------------
def b_resolver(c, t, C, b):
    def resolve():
        ka, kb, kc, kd = C["s10.a"], C["s10.b"], C["s10.c"], C["s10.d"]
        linhas = ((ka, "−2x", "<", "6"), (kd, "x", ">", "−3"))
        pilha(c, t, linhas, ((kb, "÷ (−2)"),), W / 2, 280, 260, 130, sinal_novo=1)
        E.foco(c, t, kc, 0.5, lambda a: E.pilula(c, "dividiu por negativo: vira o sinal", W / 2, 700, 60, "g", a=a, cor=E.SOBRE))
        a1 = C["s11.a"]
        E.frase(c, t, C["s11"] + 0.3, ps("teste o", "i", 76) + [("zero:", "g", 80, COR)], 640, 870, "center", 0.12)
        fcen(c, t, a1, "0 > −3", 1100, 870, 110)
        E.foco(c, t, pal("s11", "agora"), 0.5, lambda a: E.selo(c, 1400, 832, 52, True, a))
        E.frase(c, t, pal("s11", "aceita"), ps("a resposta aceita o zero, como a original", "i", 60, CERTO), W / 2, 1000, "center", 0.07)
    E.saida(c, t, C["s12"] - 0.1, resolve)
    if t < C["s12"]:
        return
    ka, kb, kc, kd, ke, kf = (C[f"s12.{k}"] for k in "abcdef")
    fcen(c, t, C["s12"], "x > −3", W / 2, 170, 120, COR)
    x0, x1, y = 220, 1700, 560
    vx = E.reta(c, t, C["s12"] + 0.1, x0, x1, y, -6, 2, range(-6, 3), MENOS, size=56)
    pinta(c, t, ka, vx(-3), W - 90, y)
    fcen(c, t, kb, "−2 × (−3) = 6", 640, 380, 80)
    fcen(c, t, kc, "6 < 6", 1250, 380, 80)
    E.foco(c, t, kc + 0.3, 0.5, lambda a: E.selo(c, 1440, 352, 40, False, a))
    bolinha(c, t, kd, vx(-3), y, False)
    E.frase(c, t, kd + 0.2, ps("bolinha", "i", 64) + [("aberta:", "g", 66, COR)] + ps("o −3", "i", 64) + [("fica de fora", "g", 66, COR)], W / 2, 770, "center", 0.1)
    for x, k, fecha, s1, s2 in ((560, ke, True, "fechada:", "entra"), (1240, kf, False, "aberta:", "fica de fora")):
        bolinha(c, t, k, x - 60, 900, fecha, r=22)
        E.frase(c, t, k + 0.1, ps(s1, "i", 64) + [(s2, "g", 66)], x, 922, "left", 0.1)


# ---------------- o erro ----------------
def b_erro(c, t, C, b):
    ka, kb, kc, kd, ke, kf = (C[f"s13.{k}"] for k in "abcdef")
    E.frase(c, t, C["s13"] + 0.4, ps("cuidado com o", "i", 72) + [("erro oposto:", "g", 76, ERRADO)] + ps("virar sem precisar", "i", 72), W / 2, 140, "center", 0.1)
    fcen(c, t, kb, "3x < −12", 500, 330, 120)
    E.ponte(c, t, pal("s13", "divide"), 790, 1090, 290, "÷ 3", None, 56)
    E.frase(c, t, kc, [("positivo", "g", 52, CERTO)], 940, 380, "center")
    fcen(c, t, kd, "x < −4", 1380, 330, 120, COR)
    E.frase(c, t, pal("s13", "sem"), ps("sem virar", "i", 56, CERTO), 1380, 420, "center", 0.1)
    E.frase(c, t, ke, ps("quem manda é o número que", "i", 72) + [("divide", "g", 76, COR)], W / 2, 560, "center", 0.1)
    E.frase(c, t, pal("s13", "não"), ps("e não o", "i", 66, TINTA2) + [("−12", "g", 70, TINTA2)] + ps("do outro lado", "i", 66, TINTA2), W / 2, 660, "center", 0.1)
    E.frase(c, t, kf, ps("quem vira:", "i", 64, ERRADO), 380, 790, "center")
    fcen(c, t, pal("s13", "escreve"), "x > −4", 380, 900, 110, ERRADO)
    E.frase(c, t, pal("s13", "zero"), ps("o zero entraria", "i", 52, ERRADO), 380, 990, "center", 0.08)
    fcen(c, t, pal("s13", "três", 3), "3 × 0 = 0", 960, 900, 96)
    fcen(c, t, pal("s13", "zero", 4) - 0.2, "0 < −12", 1450, 900, 96)
    E.foco(c, t, pal("s13", "não", 2), 0.5, lambda a: E.selo(c, 1700, 865, 46, False, a))
    E.risco(c, 220, 930, 540, 850, t, pal("s13", "menos", 5), ERRADO, 12)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def regra():
        ka, kb, kc = C["s14.a"], C["s14.b"], C["s14.c"]
        E.frase(c, t, C["s14"] + 0.3, ps("agora, o atalho", "i", 76, CLARO), W / 2, 150, "center", 0.11)
        E.frase(c, t, ka, ps("teste um número fácil, como o", "i", 84, CLARO) + [("0", "g", 130, BR)], W / 2, 340, "center", 0.11)
        E.frase(c, t, pal("s14", "na"), ps("na inequação", "i", 76, CLARO) + [("original", "g", 80, BR)], W / 2, 460, "center", 0.12)
        E.foco(c, t, kb, 0.5, lambda a: E.selo(c, 330, 610, 50, True, a))
        E.frase(c, t, kb + 0.1, ps("serve lá?", "i", 76, CLARO) + [("tem que servir na resposta", "g", 76, BR)], 410, 635, "left", 0.1)
        E.foco(c, t, pal("s14", "se", 2), 0.5, lambda a: E.selo(c, 330, 780, 50, False, a))
        E.frase(c, t, pal("s14", "se", 2) + 0.1, ps("não bateu?", "i", 76, CLARO), 410, 805, "left", 0.1)
        E.frase(c, t, kc, [("o sinal está do lado errado", "g", 84, CLARO)], W / 2, 960, "center")
    E.saida(c, t, C["s15"] - 0.1, regra)
    if t < C["s15"]:
        return
    ka, kb, kc = C["s15.a"], C["s15.b"], C["s15.c"]
    E.frase(c, t, ka - 0.6, ps("a resposta é", "i", 76, CLARO) + [("o grupo de números que servem", "g", 76, BR)], W / 2, 190, "center", 0.1)
    E.frase(c, t, pal("s15", "com"), ps("com o sinal errado, ela pega", "i", 68, CLARO) + [("os que não servem", "g", 70, BR)], W / 2, 310, "center", 0.1)
    E.foco(c, t, kb, 0.5, lambda a: E.selo(c, 300, 480, 50, False, a))
    E.frase(c, t, kb + 0.1, ps("não compensa: o zero", "i", 72, CLARO) + [("na fronteira", "g", 76, BR)], 380, 505, "left", 0.1)
    fcen(c, t, pal("s15", "como"), "x > 0", 560, 690, 110, BR)
    E.frase(c, t, pal("s15", "aí"), ps("o zero dá o mesmo resultado", "i", 60, CLARO), 1240, 650, "center", 0.08)
    E.frase(c, t, pal("s15", "aí") + 1.3, ps("com o sinal certo e com o errado", "i", 60, CLARO), 1240, 730, "center", 0.08)
    E.frase(c, t, kc - 0.6, ps("teste outro número, como o", "i", 84, CLARO) + [("1", "g", 130, BR)], W / 2, 930, "center", 0.12)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    ka, kb, kc = C["s16.a"], C["s16.b"], C["s16.c"]
    E.frase(c, t, C["s16"] + 0.3, ps("hora de testar", "i", 72, COR), XE, 170, passo=0.12)
    E.frase(c, t, ka - 0.4, ps("resolva", "i", 76), XE, 310)
    E.formula_em(c, t, ka, "−4x + 2 ≥ 10", XE, 470, 140, "g", COR)
    E.frase(c, t, kb, ps("a bolinha é", "i", 76) + [("aberta", "g", 80)] + ps("ou", "i", 76) + [("fechada?", "g", 80)], XE, 680, passo=0.1)
    E.frase(c, t, kc, ps("pinta para", "i", 76) + [("que lado?", "g", 80)], XE, 820, passo=0.1)
    E.relogio(c, t, C["s17.a"], 1520, 360, 170)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    def resolve():
        ka, kb, kc, kd, ke = C["s18.a"], C["s18.b"], C["s18.c"], C["s18.d"], C["s18.e"]
        linhas = ((C["s18"] + 0.2, "−4x + 2", "≥", "10"), (kb, "−4x", "≥", "8"), (ke, "x", "≤", "−2"))
        ops = ((ka, "− 2"), (kc, "÷ (−4)"))
        pilha(c, t, linhas, ops, 820, 250, 250, 120, sinal_novo=2)
        E.foco(c, t, kd, 0.5, lambda a: E.pilula(c, "negativo: vira o sinal", 1460, 520, 56, "g", a=a, cor=E.SOBRE))
    E.saida(c, t, C["s19"] - 0.1, resolve)
    if t < C["s19"]:
        return
    ka, kb, kc, kd, ke = (C[f"s19.{k}"] for k in "abcde")
    fcen(c, t, C["s19"], "x ≤ −2", W / 2, 170, 120, COR)
    x0, x1, y = 220, 1700, 480
    vx = E.reta(c, t, C["s19"] + 0.1, x0, x1, y, -5, 3, range(-5, 4), MENOS, size=56)
    bolinha(c, t, ka, vx(-2), y, True)
    E.frase(c, t, ka + 0.2, ps("tem o igual:", "i", 56) + [("fechada", "g", 60, COR)], vx(-2), 360, "center", 0.1)
    pinta(c, t, kb, vx(-2), 90, y)
    fcen(c, t, kc, "−4 × 0 + 2 = 2", 640, 760, 96)
    fcen(c, t, pal("s19", "dois", 4), "2 ≥ 10", 1300, 760, 96)
    E.foco(c, t, pal("s19", "não"), 0.5, lambda a: E.selo(c, 1550, 725, 46, False, a))
    E.foco(c, t, kd, 0.5, lambda a: c.drawCircle(vx(0), y, 44, M.paint(ERRADO, a, stroke=7)), blur=4)
    E.frase(c, t, kd + 0.1, ps("o zero", "i", 56, ERRADO) + [("fora", "g", 60, ERRADO)], vx(0), y + 150, "center", 0.1)
    E.foco(c, t, ke, 0.5, lambda a: E.selo(c, 820, 930, 60, True, a))
    E.frase(c, t, ke + 0.1, [("bateu!", "g", 100, CERTO)], 910, 965)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s20"] + 0.3, [("resumindo", "i", 92, COR)], W / 2, 210, "center")
        for i, (k, s) in enumerate((("s20.a", "resolva como equação"), ("s20.b", "× ou ÷ por negativo: vira o sinal"), ("s20.c", "confira com um número"))):
            y = 390 + i * 190
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 260, y - 30, 56, a=a),
                                                         centro(c, str(i + 1), 260, y - 7, 64, "g", E.SOBRE, a)))
            E.frase(c, t, C[k] + 0.1, [(s, "g", 80)], 350, y)
    E.saida(c, t, C["s21"] - 0.1, resumo)
    if t < C["s21"]:
        return
    ka, kb, kc, kd = (C[f"s21.{k}"] for k in "abcd")
    E.frase(c, t, C["s21"] + 0.2, ps("na próxima aula", "i", 84), XE, 240, passo=0.14)
    E.frase(c, t, ka, ps("inequações com", "i", 84) + [("duas condições", "g", 96, COR)], XE, 390, passo=0.14)
    E.frase(c, t, kb, ps("a partir de quantos minutos", "i", 72) + [("um plano fica mais barato", "g", 72, COR)], XE, 520, passo=0.09)
    E.foco(c, t, kc, 0.5, lambda a: E.pilula(c, "Inscreva-se", 1440, 750, 76, estilo="g", a=a, cor=E.SOBRE))
    p = ease_io(prog(t, kc + 0.3, 0.8))
    E.cursor(c, lerp(1770, 1570, p), lerp(990, 775, p), ep(t, kc + 0.2, 0.4))
    E.frase(c, t, kd, [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 930, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, oque=b_oque, porque=b_porque, resolver=b_resolver, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
