"""Visual — Estudativo · MAT-EQU-016: inequação dupla e inequação em problemas.
−1 < 2x + 3 ≤ 9 → −2 < x ≤ 3. Planos: 35 + 0,3x < 0,8x → x > 70 → a partir de 71 minutos. Questão: 8 + 3x ≤ 30 → x ≤ 22/3 → 7 horas.
Instantes: cues C[...] e, para números ditos no meio da frase, pal(cena, palavra) lê o instante da palavra na voz real."""
import json
from pathlib import Path

import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_out, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Equações do 1º Grau")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-EQU-016_inequacao_dupla_e_problemas.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("dupla", "planos", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
MENOS = lambda v: str(v).replace("-", "−")

# as contas da aula
assert -1 - 3 == -4 and 9 - 3 == 6 and -4 / 2 == -2 and 6 / 2 == 3 and 2 * 3 + 3 == 9
A_, B_ = (lambda m: 35 + 0.3 * m), (lambda m: 0.8 * m)
assert round(A_(70), 2) == round(B_(70), 2) == 56 and round(A_(71), 2) == 56.3 and round(B_(71), 2) == 56.8 and 35 / 0.5 == 70
assert 30 - 8 == 22 and 3 * 7 == 21 < 22 < 24 == 3 * 8 and 8 + 24 == 32 > 30 and 8 + 21 == 29 <= 30


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


def relacao(c, a, esq, sig, dir_, y, size, cor=None, xm=W / 2):
    g = size * 0.5
    E.formula(c, esq, xm - g, y, size, "g", cor, a, "right")
    centro(c, sig, xm, y, size, "g", cor, a)
    E.formula(c, dir_, xm + g, y, size, "g", cor, a)


def pilha(c, t, linhas, ops, xm, y0, dy, size):
    """resolução em linhas: linhas = [(t0, esq, sinal, dir)], ops = [(t0, op)] sob os dois lados, entre a linha k e a k+1"""
    g = size * 0.5
    for k, (t0, esq, sig, dir_) in enumerate(linhas):
        y = y0 + k * dy
        ult = k == len(linhas) - 1
        velha = not ult and t >= linhas[k + 1][0]
        cor = COR if ult else (CINZA if velha else TINTA)
        E.foco(c, t, t0, 0.5, lambda a, esq=esq, sig=sig, dir_=dir_, y=y, cor=cor: relacao(c, a, esq, sig, dir_, y, size, cor, xm))
        if k < len(ops):
            to, op = ops[k]
            we = E.formula(c, esq, 0, 0, size, a=0)
            wd = E.formula(c, dir_, 0, 0, size, a=0)
            cop = CINZA if velha else COR
            for cx in (xm - g - we / 2, xm + g + wd / 2):
                E.foco(c, t, to, 0.45, lambda a, cx=cx, cop=cop: E.formula(c, op, cx, y + size * 0.72, size * 0.52, "b", cop, a, "center"), sobe=8)


XS = (480, 690, 960, 1230, 1440)  # colunas da inequação dupla: parte, sinal, parte, sinal, parte


def dupla(c, t, itens, y, size, cor=None):
    """inequação dupla em colunas fixas: itens = [(t0, texto)] × 5"""
    for (t0, s), x in zip(itens, XS):
        fcen(c, t, t0, s, x, y, size, cor)


def ops3(c, t, t0, op, y, size, cor=None):
    for x in XS[::2]:
        E.foco(c, t, t0, 0.45, lambda a, x=x: E.formula(c, op, x, y, size, "b", cor or COR, a, "center"), sobe=8)


def bolinha(c, t, t0, x, y, fecha, cor=None, r=19):
    cor = cor or COR
    k = ease_back(prog(t, t0, 0.5))
    if k <= 0:
        return
    rr = r * k
    c.drawCircle(x, y, rr, M.paint(cor if fecha else E.PAPEL))
    c.drawCircle(x, y, rr, M.paint(cor, 1.0, stroke=7))


def pinta(c, t, t0, x_ini, x_fim, y, cor=None, d=0.9):
    p = ease_out(prog(t, t0, d))
    if p > 0:
        M.line(c, x_ini, y, lerp(x_ini, x_fim, p), y, cor or COR, 1.0, 12, cap_round=False)


def cartao(c, x, y, w, h, a, cor=FIO):
    if a > 0:
        M.rrect(c, x, y, w, h, 30, E.VAZIO, a, stroke=4, stroke_color=cor)


def letra(c, t, t0, s, cx, cy, r, cor=None):
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r, cor, a), centro(c, s, cx, cy + r * 0.36, r * 1.0, "g", E.SOBRE, a)))


def bnum(c, t, t0, s, cx, cy, r, cor=None, size=None):
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r, cor, a), centro(c, s, cx, cy + (size or r) * 0.36, size or r, "g", E.SOBRE, a)))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    ka, kb, kc = C["s01.a"], C["s01.b"], C["s01.c"]

    def pergunta():
        E.frase(c, t, ka - 0.4, ps("os planos empatam com", "i", 76) + [("70 minutos", "g", 90, COR)], W / 2, 210, "center", 0.12)
        E.frase(c, t, pal("s01", "conta"), ps("a conta só vem com", "i", 64, TINTA2) + [("minuto inteiro", "g", 64, TINTA2)], W / 2, 320, "center", 0.1)
        E.frase(c, t, pal("s01", "partir"), [("a partir de quantos minutos", "g", 90, COR)], W / 2, 490, "center")
        E.frase(c, t, pal("s01", "plano"), ps("o plano de minuto mais barato", "i", 76) + [("passa a ganhar?", "g", 80)], W / 2, 610, "center", 0.11)
        bnum(c, t, kb, "70", 640, 830, 100, ERRADO, 100)
        E.foco(c, t, kb + 0.6, 0.5, lambda a: E.selo(c, 740, 750, 40, False, a))
        E.frase(c, t, kc - 0.9, ps("no 70, eles", "i", 72), 800, 810)
        E.frase(c, t, kc, [("ainda custam o mesmo", "g", 76, ERRADO)], 800, 900)
    E.saida(c, t, C["s02"] - 0.1, pergunta)
    if t < C["s02"]:
        return
    ta, tb, tc = C["s02.a"], C["s02.b"], C["s02.c"]
    E.foco(c, t, tc - 0.2, 0.7, lambda a: E.bola(c, 1560, 560, 220 * ease_back(prog(t, tc - 0.2, 0.7))), blur=0)
    E.frase(c, t, ta, ps("até o fim desta aula", "i", 90), XE, 300, passo=0.14)
    E.frase(c, t, pal("s02", "inequação"), ps("inequação com", "i", 84) + [("duas condições", "g", 90, COR)], XE, 450, passo=0.14)
    E.frase(c, t, tb - 0.4, ps("responder", "i", 84) + [("a partir de quantos", "g", 84)], XE, 600, passo=0.14)
    E.foco(c, t, tc + 0.2, 0.5, lambda a: (centro(c, "+ atalho", 1560, 545, 76, "g", E.SOBRE, a),
                                           centro(c, "de prova", 1560, 630, 76, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"] + 0.3, ps("você precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "2", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 240, 700, 120, "i", TINTA, a))
    x, w = 940, 820
    itens = (("s03.b", "achar com quantos minutos", "dois planos empatam"), ("s03.c", "resolver inequação,", "virando o sinal com negativo"))
    for i, (k, l1, l2) in enumerate(itens):
        y = 240 + i * 260
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 196, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 62)], x + 44, y + 84)
        E.frase(c, t, C[k] + 0.3, [(l2, "g", 58, COR)], x + 44, y + 160)
    py = lerp(410, 670, ease_io(prog(t, C["s03.c"] - 0.35, 0.5)))
    E.cursor(c, x + w - 30, py, ep(t, C["s03.b"], 0.4))
    E.frase(c, t, pal("s03", "se"), ps("faltou alguma?", "i", 62, COR) + ps("procure no canal", "i", 62), 940, 800, "left", 0.12)


# ---------------- inequação dupla ----------------
def b_dupla(c, t, C, b):
    def resolve():
        a6, b6, c6, d6 = C["s06.a"], C["s06.b"], C["s06.c"], C["s06.d"]
        a7, b7, c7 = C["s07.a"], C["s07.b"], C["s07.c"]
        E.saida(c, t, C["s05"] - 0.1, lambda: E.frase(c, t, pal("s04", "inequação"), [("inequação dupla", "g", 110, COR)], W / 2, 160, "center"))
        cinza1 = t >= d6
        cor1 = CINZA if cinza1 else TINTA
        dupla(c, t, ((C["s04.a"], "−1"), (pal("s04", "menor"), "<"), (pal("s04", "dois"), "2x + 3"), (pal("s04", "menor", 2), "≤"), (pal("s04", "nove"), "9")), 330, 120, cor1)

        def exige():
            E.foco(c, t, C["s05.d"], 0.5, lambda a: M.rrect(c, XS[2] - 220, 330 - 110, 440, 150, 26, COR, 0.12 * a), blur=4)
            E.frase(c, t, C["s05.a"], ps("duas exigências", "g", 76, COR) + ps("de uma vez", "i", 72), W / 2, 500, "center", 0.12)
            fcen(c, t, C["s05.b"], "2x + 3 > −1", 560, 650, 96)
            fcen(c, t, C["s05.c"], "2x + 3 ≤ 9", 1360, 650, 96)
            E.foco(c, t, pal("s05", "e"), 0.4, lambda a: centro(c, "e", 960, 645, 72, "i", TINTA2, a))
            E.frase(c, t, C["s05.d"], ps("a conta do meio fica", "i", 76) + [("presa entre −1 e 9", "g", 80, COR)], W / 2, 860, "center", 0.11)
        E.saida(c, t, C["s06"] - 0.1, exige)
        if t >= C["s06"]:
            for x in XS[::2]:
                w = 200 if x != XS[2] else 440
                p = ep(t, a6 + (0.15 if x == XS[2] else 0.3 if x == XS[4] else 0), 0.5)
                if t < d6 + 0.4:
                    E.saida(c, t, d6, lambda x=x, w=w, p=p: E.caixa_pontilhada(c, x - w / 2, 200, w, 170, p, prog_=p))
            E.frase(c, t, a6 - 0.3, ps("agora com", "i", 64, TINTA2) + [("três partes:", "g", 66, COR)] + ps("o que faz numa,", "i", 64, TINTA2) + [("faz nas três", "g", 66, COR)], W / 2, 110, "center", 0.12)
            ops3(c, t, c6, "− 3", 330 + 86, 60, CINZA if cinza1 else COR)
            dupla(c, t, ((d6, "−4"), (pal("s06", "menor"), "<"), (pal("s06", "dois"), "2x"), (pal("s06", "menor", 2), "≤"), (pal("s06", "seis"), "6")), 590, 120, CINZA if t >= c7 else TINTA)
            ops3(c, t, a7, "÷ 2", 590 + 86, 60, CINZA if t >= c7 else COR)
            E.foco(c, t, b7 - 1.0, 0.5, lambda a: E.pilula(c, "2 é positivo: nada vira", W / 2, 1010, 50, "g", a=a, cor=E.SOBRE))
            dupla(c, t, ((c7, "−2"), (pal("s07", "menor"), "<"), (pal("s07", "xis"), "x"), (pal("s07", "menor", 2), "≤"), (pal("s07", "três", 2), "3")), 850, 130, COR)
    E.saida(c, t, C["s08"] - 0.1, resolve)
    if t < C["s08"]:
        return
    ka, kb, kc = C["s08.a"], C["s08.b"], C["s08.c"]
    fcen(c, t, C["s08"], "−2 < x ≤ 3", W / 2, 180, 120, COR)
    x0, x1, y = 220, 1700, 560
    vx = E.reta(c, t, C["s08"] + 0.1, x0, x1, y, -4, 5, range(-4, 6), MENOS, size=56)
    pinta(c, t, kc, vx(-2), vx(3), y)
    bolinha(c, t, ka, vx(-2), y, False)
    bolinha(c, t, kb, vx(3), y, True)
    E.frase(c, t, ka + 0.2, ps("aberta:", "i", 56) + [("fica de fora", "g", 58, COR)], vx(-2), 440, "center", 0.1)
    E.frase(c, t, kb + 0.2, ps("fechada:", "i", 56) + [("entra", "g", 58, COR)] + ps("(tem o igual)", "i", 50, TINTA2), vx(3), 440, "center", 0.1)
    E.frase(c, t, kc, ps("pinte", "i", 60) + [("só o pedaço do meio", "g", 62, COR)], vx(0.5), 730, "center", 0.1)
    a9, b9 = C["s09.a"], C["s09.b"]
    E.frase(c, t, C["s09"] + 0.3, ps("conferindo a ponta fechada:", "i", 64, TINTA2), W / 2, 850, "center", 0.1)
    fcen(c, t, a9, "2 × 3 + 3 = 9", 700, 975, 96)
    fcen(c, t, pal("s09", "nove", 2), "9 ≤ 9", 1230, 975, 96)
    E.foco(c, t, b9, 0.5, lambda a: E.selo(c, 1440, 940, 46, True, a))
    E.frase(c, t, b9 + 0.1, [("serve", "g", 80, CERTO)], 1510, 970)


# ---------------- problema dos planos ----------------
def b_planos(c, t, C, b):
    def enunciado():
        ka, kb, kc, kd = C["s10.a"], C["s10.b"], C["s10.c"], C["s10.d"]
        E.frase(c, t, C["s10"] + 1.5, ps("valores inventados para a aula", "i", 48, TINTA2), W / 2, 110, "center", 0.08)
        for x, k, nome, l1, l2, t1, t2 in ((150, ka, "A", [("R$ 35", "g", 120, TINTA)] + ps("por mês", "i", 60), [("+ R$ 0,30", "g", 84, COR)] + ps("por minuto", "i", 58, COR),
                                            pal("s10", "trinta"), pal("s10", "trinta", 2)),
                                           (990, kb, "B", ps("sem mensalidade", "i", 72), [("R$ 0,80", "g", 84, COR)] + ps("por minuto", "i", 58, COR),
                                            pal("s10", "não"), pal("s10", "oitenta"))):
            y, w, h = 160, 780, 400
            E.foco(c, t, k, 0.5, lambda a, x=x: cartao(c, x, y, w, h, a), blur=4)
            letra(c, t, k + 0.1, nome, x + 90, y + 95, 52)
            E.frase(c, t, k + 0.2, ps("plano", "i", 72), x + 165, y + 120)
            E.frase(c, t, t1, l1, x + 60, y + 260, passo=0.15)
            E.frase(c, t, t2, l2, x + 60, y + 360, passo=0.15)
        E.foco(c, t, kc, 0.5, lambda a: E.pilula(c, "a conta só tem minutos inteiros", W / 2, 680, 56, "g", a=a, cor=E.SOBRE))
        E.frase(c, t, kd, [("a partir de quantos minutos", "g", 84, COR)] + ps("A fica mais barato?", "i", 80), W / 2, 880, "center", 0.11)
    E.saida(c, t, C["s11"] - 0.1, enunciado)

    def resolve():
        ka, kb, kc, kd = C["s11.a"], C["s11.b"], C["s11.c"], C["s11.d"]
        a2, b2, c2, d2, e2 = (C[f"s12.{k}"] for k in "abcde")
        E.linha(c, t, [("minutos = x", "g", 64, COR, ka), ("·", "g", 64, CINZA, kb - 0.2), ("mais barato", "i", 64, TINTA, kb), ("=", "g", 64, TINTA, kb + 0.3),
                       ("menor", "g", 64, COR, pal("s11", "menor"))], W / 2, 120, "center")
        E.frase(c, t, kc, ps("conta de A", "g", 64) + [("<", "g", 72, COR)] + ps("conta de B", "g", 64), W / 2, 230, "center", 0.12)
        linhas = ((kd, "35 + 0,3x", "<", "0,8x"), (b2, "35", "<", "0,5x"), (d2, "70", "<", "x"), (e2, "x", ">", "70"))
        pilha(c, t, linhas, ((a2, "− 0,3x"), (c2, "÷ 0,5")), 860, 400, 170, 100)
        E.frase(c, t, pal("s12", "positivo"), ps("positivo:", "i", 52, CERTO) + [("não vira", "g", 54, CERTO)], 1580, 620, "center", 0.1)
        E.foco(c, t, pal("s12", "dividir"), 0.5, lambda a: E.pilula(c, "÷ 0,5 = × 2", 1580, 700, 54, "g", a=a, cor=E.SOBRE))
    if C["s11"] - 0.1 <= t:
        E.saida(c, t, C["s13"] - 0.1, resolve)

    def inteiro():
        ka, kb = C["s13.a"], C["s13.b"]
        fcen(c, t, C["s13"], "x > 70", W / 2, 180, 120, COR)
        E.frase(c, t, pal("s13", "minuto"), ps("o minuto é", "i", 72) + [("inteiro", "g", 76, COR)], W / 2, 310, "center", 0.12)
        x0, x1, y = 300, 1620, 560
        vx = E.reta(c, t, C["s13"] + 0.2, x0, x1, y, 68, 74, range(68, 75), str, size=60)
        bolinha(c, t, pal("s13", "setenta"), vx(70), y, False, r=22)
        E.frase(c, t, pal("s13", "setenta"), ps("empate: fora", "i", 52, TINTA2), vx(70), 690, "center", 0.08)
        for i, v in enumerate((71, 72, 73)):
            E.foco(c, t, ka + 0.3 + i * 0.2, 0.4, lambda a, v=v: c.drawCircle(vx(v), y, 18, M.paint(COR, a)), blur=4)
        E.foco(c, t, ka, 0.5, lambda a: c.drawCircle(vx(71), y, 42, M.paint(CERTO, a, stroke=7)), blur=4)
        E.frase(c, t, ka, ps("o primeiro inteiro:", "i", 56) + [("71", "g", 64, CERTO)], vx(71), 450, "center", 0.1)
        E.frase(c, t, kb, ps("a partir de", "i", 96) + [("71 minutos", "g", 120, COR)], W / 2, 870, "center", 0.14)
    if C["s13"] - 0.1 <= t:
        E.saida(c, t, C["s14"] - 0.1, inteiro)
    if t < C["s14"]:
        return
    ka, kb, kc, kd = C["s14.a"], C["s14.b"], C["s14.c"], C["s14.d"]
    xs = (420, 960, 1440)
    E.foco(c, t, C["s14"] + 0.2, 0.5, lambda a: (centro(c, "minutos", xs[0], 290, 64, "i", TINTA, a),
                                                 E.formula(c, "35 + 0,3x", xs[1], 290, 72, "g", COR, a, "center"),
                                                 E.formula(c, "0,8x", xs[2], 290, 72, "g", COR, a, "center"),
                                                 centro(c, "plano A", xs[1], 190, 56, "i", TINTA2, a), centro(c, "plano B", xs[2], 190, 56, "i", TINTA2, a)))
    if t >= C["s14"] + 0.2:
        M.line(c, 220, 340, 1700, 340, TINTA, 1.0, 4, progress=ep(t, C["s14"] + 0.2, 0.6))
    cen(c, t, ka, "70", xs[0], 480, 92)
    cen(c, t, pal("s14", "cinquenta"), "R$ 56", xs[1], 480, 92, TINTA2)
    cen(c, t, pal("s14", "cinquenta") + 0.2, "R$ 56", xs[2], 480, 92, TINTA2)
    E.frase(c, t, pal("s14", "cinquenta") + 0.5, ps("empate", "i", 56, TINTA2), 1640, 460)
    cen(c, t, kb, "71", xs[0], 680, 92)
    if t >= kd:
        E.foco(c, t, kd, 0.4, lambda a: M.rrect(c, xs[1] - 200, 680 - 92, 400, 120, 24, CERTO, 0.16 * a), blur=4)
    cen(c, t, pal("s14", "cinquenta", 2), "R$ 56,30", xs[1], 680, 92, CERTO if t >= kd else TINTA)
    cen(c, t, kc, "R$ 56,80", xs[2], 680, 92)
    E.frase(c, t, kd, ps("A fica", "i", 72, CERTO) + [("mais barato", "g", 76, CERTO)], W / 2, 900, "center", 0.12)


# ---------------- o erro ----------------
def b_erro(c, t, C, b):
    ka, kb, kc, kd = C["s15.a"], C["s15.b"], C["s15.c"], C["s15.d"]
    E.frase(c, t, C["s15"] + 1.0, ps("cuidado com o erro do começo:", "i", 72) + [("responder o empate", "g", 76, ERRADO)], W / 2, 160, "center", 0.1)
    bnum(c, t, pal("s15", "setenta"), "70", 520, 360, 90, TINTA2, 90)
    E.frase(c, t, kb - 0.3, ps("preços", "i", 80) + [("iguais", "g", 84)], 650, 385, "left", 0.12)
    bnum(c, t, kc - 0.4, "71", 520, 580, 90, CERTO, 90)
    E.frase(c, t, kc, ps("o mais barato", "i", 80) + [("começa aqui", "g", 84, CERTO)], 650, 605, "left", 0.12)
    E.frase(c, t, pal("s15", "releia"), ps("releia a pergunta:", "i", 72, TINTA2), W / 2, 780, "center", 0.1)
    for i, (s, nome, k) in enumerate((("=", "igual", kd), ("<", "menor", pal("s15", "menor")), ("≤", "menor ou igual", pal("s15", "menor", 2)))):
        x = 560 + i * 400
        cen(c, t, k, s, x, 935, 110, COR)
        cen(c, t, k + 0.1, nome, x, 1010, 50, TINTA, "i")


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def regra():
        ka, kb, kc, kd = C["s16.a"], C["s16.b"], C["s16.c"], C["s16.d"]
        E.frase(c, t, C["s16"] + 0.3, ps("agora, o atalho", "i", 76, CLARO), W / 2, 150, "center", 0.11)
        E.frase(c, t, ka, ps("ache o", "i", 84, CLARO) + [("empate", "g", 90, BR)] + ps("e depois", "i", 84, CLARO) + [("escolha o lado", "g", 90, BR)], W / 2, 290, "center", 0.12)
        E.linha(c, t, [("mensalidades:", "i", 64, CLARO, kb), ("35 − 0 =", "g", 80, BR, kb + 0.3), ("R$ 35", "g", 80, CLARO, pal("s16", "trinta"))], 330, 460)
        E.linha(c, t, [("minuto:", "i", 64, CLARO, pal("s16", "minuto") - 0.2), ("0,80 − 0,30 =", "g", 80, BR, pal("s16", "minuto")),
                       ("R$ 0,50", "g", 80, CLARO, pal("s16", "cinquenta"))], 330, 590)
        E.linha(c, t, [("35 ÷ 0,5 =", "g", 110, BR, kc), ("70", "g", 140, CLARO, pal("s16", "setenta")), ("minutos", "i", 90, CLARO, pal("s16", "setenta") + 0.2)], W / 2, 790, "center")
        E.frase(c, t, pal("s16", "depois", 2), ps("depois do empate, ganha", "i", 72, CLARO) + [("o minuto mais barato", "g", 76, BR)], W / 2, 960, "center", 0.1)
    E.saida(c, t, C["s17"] - 0.1, regra)
    if t < C["s17"]:
        return
    ka, kb, kc = C["s17.a"], C["s17.b"], C["s17.c"]
    E.frase(c, t, ka - 0.3, ps("os preços só trocam de posição", "i", 80, CLARO) + [("no empate", "g", 84, BR)], W / 2, 250, "center", 0.11)
    E.foco(c, t, kb, 0.5, lambda a: E.selo(c, 290, 450, 50, False, a))
    E.frase(c, t, kb + 0.1, ps("não compensa:", "i", 72, CLARO) + [("minuto com o mesmo preço", "g", 76, BR)], 370, 475, "left", 0.1)
    E.frase(c, t, pal("s17", "aí"), ps("não existe empate:", "i", 66, CLARO), 370, 590, "left", 0.1)
    E.frase(c, t, pal("s17", "quem"), [("a mensalidade menor ganha sempre", "g", 70, BR)], 370, 690, "left")
    E.frase(c, t, kc - 0.8, ps("na dúvida,", "i", 90, CLARO) + [("monte a inequação", "g", 100, BR)], W / 2, 900, "center", 0.14)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    ka, kb, kc, kd, ke = (C[f"s18.{k}"] for k in "abcde")
    E.frase(c, t, C["s18"] + 0.3, ps("hora de testar", "i", 72, COR), XE, 150, passo=0.12)
    E.frase(c, t, pal("s18", "estacionamento"), ps("um estacionamento:", "i", 72), XE, 270)
    E.frase(c, t, ka, [("R$ 8", "g", 100, COR)] + ps("de entrada", "i", 68), XE, 400, passo=0.14)
    E.frase(c, t, kb - 0.3, [("+ R$ 3", "g", 90, TINTA)] + ps("por hora", "i", 68), XE, 520, passo=0.14)
    E.frase(c, t, kc, [("hora começada", "g", 64)] + ps("conta como hora inteira", "i", 60), XE, 640, passo=0.1)
    E.frase(c, t, kd - 0.4, ps("você tem", "i", 76) + [("R$ 30", "g", 100, COR)], XE, 790, passo=0.14)
    E.frase(c, t, ke, ps("por quantas horas,", "i", 76) + [("no máximo?", "g", 84, COR)], XE, 930, passo=0.12)
    E.relogio(c, t, C["s19.a"], 1520, 360, 170)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    def resolve():
        ka, kb, kc, kd, ke, kf = (C[f"s20.{k}"] for k in "abcdef")
        E.foco(c, t, ka, 0.5, lambda a: E.pilula(c, "horas", 640, 130, 60, "i", a=a, cor=E.SOBRE))
        E.foco(c, t, ka + 0.3, 0.5, lambda a: M.arrow(c, 760, 132, 880, 132, TINTA, a, 5, 18))
        bnum(c, t, pal("s20", "xis"), "x", 970, 128, 62, None, 84)
        E.frase(c, t, pal("s20", "o"), ps("o gasto tem que caber nos", "i", 52, TINTA2) + [("R$ 30", "g", 54, TINTA2)], 1080, 145, "left", 0.08)
        linhas = ((kb, "8 + 3x", "≤", "30"), (kd, "3x", "≤", "22"), (kf, "x", "≤", "f{22}{3}"))
        pilha(c, t, linhas, ((kc, "− 8"), (ke, "÷ 3")), 760, 340, 230, 110)
        E.foco(c, t, pal("s20", "como"), 0.5, lambda a: E.formula(c, "3 × 7 = 21", 1480, 760, 80, "g", TINTA, a, "center"))
        E.frase(c, t, pal("s20", "isso"), ps("um pouco", "i", 64) + [("mais que 7", "g", 68, COR)], 1480, 880, "center", 0.1)
    E.saida(c, t, C["s21"] - 0.1, resolve)
    if t < C["s21"]:
        return
    ka, kb, kc, kd, ke = (C[f"s21.{k}"] for k in "abcde")
    E.frase(c, t, C["s21"] + 0.3, ps("aqui, o arredondamento é", "i", 80) + [("para baixo", "g", 90, COR)], W / 2, 170, "center", 0.12)
    E.frase(c, t, pal("s21", "com"), ps("com", "i", 72) + [("8 horas:", "g", 76)], 330, 380, "left", 0.1)
    fcen(c, t, kb, "8 + 24 = R$ 32", 1080, 380, 96)
    E.foco(c, t, pal("s21", "passa"), 0.5, lambda a: E.selo(c, 1460, 345, 46, False, a))
    E.frase(c, t, pal("s21", "passa"), ps("passa dos 30", "i", 60, ERRADO), 1530, 375, "left", 0.1)
    bnum(c, t, kc, "7", 620, 590, 110, None, 130)
    E.frase(c, t, kc + 0.2, [("horas", "g", 120)], 770, 635)
    E.frase(c, t, kd - 0.8, ps("conferindo:", "i", 72), 330, 830, "left", 0.1)
    fcen(c, t, kd, "8 + 21 = R$ 29", 1080, 830, 96)
    E.foco(c, t, ke, 0.5, lambda a: E.selo(c, 1460, 795, 46, True, a))
    E.frase(c, t, ke + 0.1, [("cabe!", "g", 84, CERTO)], 1530, 830)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s22"] + 0.3, [("resumindo", "i", 92, COR)], W / 2, 210, "center")
        for i, (k, s) in enumerate((("s22.a", "dupla: o mesmo nas três partes"), ("s22.b", "a pergunta decide o sinal"), ("s22.c", "a unidade decide o arredondamento"))):
            y = 390 + i * 190
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 260, y - 30, 56, a=a),
                                                         centro(c, str(i + 1), 260, y - 7, 64, "g", E.SOBRE, a)))
            E.frase(c, t, C[k] + 0.1, [(s, "g", 80)], 350, y)
    E.saida(c, t, C["s23"] - 0.1, resumo)
    if t < C["s23"]:
        return
    ka, kb, kc, kd = (C[f"s23.{k}"] for k in "abcd")
    E.frase(c, t, C["s23"] + 0.2, ps("na próxima aula", "i", 84), XE, 240, passo=0.14)
    E.frase(c, t, ka - 0.2, ps("hora de", "i", 110) + [("praticar", "g", 130, COR)], XE, 400, passo=0.14)
    E.frase(c, t, kb, ps("problemas de", "i", 72) + [("equação e de inequação", "g", 76, COR)], XE, 530, passo=0.1)
    E.frase(c, t, pal("s23", "do"), ps("do texto até a resposta com", "i", 66) + [("a unidade certa", "g", 68)], XE, 640, passo=0.09)
    E.foco(c, t, kc, 0.5, lambda a: E.pilula(c, "Inscreva-se", 1440, 770, 76, estilo="g", a=a, cor=E.SOBRE))
    p = ease_io(prog(t, kc + 0.3, 0.8))
    E.cursor(c, lerp(1770, 1570, p), lerp(1000, 795, p), ep(t, kc + 0.2, 0.4))
    E.frase(c, t, kd, [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 950, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, dupla=b_dupla, planos=b_planos, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
