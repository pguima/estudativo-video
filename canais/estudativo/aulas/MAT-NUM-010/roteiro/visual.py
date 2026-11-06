"""Visual — Estudativo · MAT-NUM-010: dividir por dois algarismos.
Identidade em _ferramentas/editorial.py. E.conta_div na forma curta; os testes do palpite ficam AO LADO da chave, nunca sob o dividendo.
Peças locais: palpite (o 6 que vira 7 e o 4 que vira 5, por cima da peça, que só conhece o final), cobre (cartão sobre o último algarismo),
desce (seta do algarismo) e resto."""
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco
import motor as M
import skia

E.usar("Matemática", "Números e Contas")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-NUM-010_dividir_por_dois_algarismos.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("estimar", "conta", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


def bola_txt(c, t, t0, s, cx, cy, r, size, cor=CERTO):
    """o resultado na esfera"""
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r, cor, a), E.centro(c, s, cx, cy + size * 0.35, size, "g", M.on(cor), a)))


def lin(c, t, t0, s, x, y, size=64, estilo="b", cor=None):
    """uma linha do painel ao lado da conta"""
    E.foco(c, t, t0, 0.4, lambda a: E.escreve(c, s, x, y, size, estilo, cor or TINTA, a))


def igual(c, t, t0, t1, s1, s2, x, y, size=66, estilo="b", cor=None, cor2=None):
    """conta em duas partes: a pergunta em t0 e o resultado só em t1, quando a voz chega nele"""
    lin(c, t, t0, s1, x, y, size, estilo, cor)
    lin(c, t, t1, s2, x + E.larg(s1 + " ", estilo, size), y, size, estilo, cor2 or cor or COR)


def lista(c, t, C, ini, ta, n, itens):
    E.frase(c, t, C[ini] + 0.7, [("você", "i", 84), ("só", "i", 84), ("precisa", "i", 84), ("de", "i", 84)], XE, 410)
    E.foco(c, t, C[ta], 0.5, lambda a: E.escreve(c, str(n), XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C[ta] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 960, 780
    y0, dy = (280, 260) if len(itens) == 2 else (190, 240)
    for i, (k, l1, l2) in enumerate(itens):
        y = y0 + i * dy
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 196, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 62)], x + 44, y + 84)
        E.frase(c, t, C[k] + 0.3, [(l2, "g", 62, COR)], x + 44, y + 160)
    px = x + w - 30
    py = y0 + 170
    for i, (k, _, _) in enumerate(itens[1:], 1):
        py = lerp(py, y0 + i * dy + 170, ease_io(prog(t, C[k] - 0.35, 0.5)))
    E.cursor(c, px, py, ep(t, C[itens[0][0]], 0.4))


def resto(c, t, t0, x, y, size, linha, col, s):
    """número na linha de baixo, no lugar em que E.conta_div escreve. linha = 0 é a primeira, col = coluna do último algarismo"""
    cl, dy = E.casa(size), size * 1.12
    for m, ch in enumerate(s):
        i = col - (len(s) - 1 - m)
        E.foco(c, t, t0, 0.4, lambda a, ch=ch, i=i: E.centro(c, ch, x + (i + 0.5) * cl, y + (linha + 1) * dy, size, "g", TINTA, a))


def centros_q(Q, D, size):
    """centro de cada algarismo do quociente, a partir do que E.conta_div devolve"""
    q = D["quociente"]
    return E._centros(q, Q["xq"] + len(q) * E.larg("0", "g", size) * 1.1 + size * 0.17, size)


def palpite(c, t, Q, D, size, i, s, t0, t1):
    """o palpite provisório no quociente, por cima de E.conta_div: entra em t0 na casa i e some em t1, logo antes de a peça escrever o certo."""
    if not t0 <= t < t1 + 0.5:
        return
    cx = centros_q(Q, D, size)[i]
    y = Q["y_q"]
    E.saida(c, t, t1 + 0.1, lambda: E.foco(c, t, t0, 0.4, lambda a: E.centro(c, s, cx, y, size, "g", ERRADO, a)))


def desce(c, t, t0, x, y, size, col, linha):
    """seta curta: o algarismo do dividendo desce até a linha de baixo, e some"""
    dy = size * 1.12
    px = x + (col + 0.5) * E.casa(size)
    p = ep(t, t0, 0.4)
    a = p * (1 - ep(t, t0 + 1.0, 0.4))
    if a > 0:
        M.arrow(c, px + size * 0.46, y - size * 0.3, px + size * 0.46, y + (linha + 1) * dy - size * 0.3, COR, a, 5, 16, p)


def cobre(c, t, t0, s, x, y, size, t_some=None):
    """número com o último algarismo coberto por um dedo de cartão: "cubra o último algarismo"."""
    w = E.larg(s, "g", size)
    wu = E.larg(s[-1], "g", size)
    E.foco(c, t, t0, 0.4, lambda a: E.escreve(c, s, x, y, size, "g", TINTA, a))
    p = ep(t, t0 + 0.4, 0.35)
    if p > 0:
        M.rrect(c, x + w - wu - 4, y - size * 0.82, (wu + 12) * p, size * 0.92, 8, E.COR, p)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def tudo():
        ka, kb, kcc = C["s01.a"], C["s01.b"], C["s01.c"]
        E.linha(c, t, [("R$ 1.035", "g", 130, COR, ka), ("para", "i", 110, TINTA, kb - 0.3), ("23 pessoas", "g", 130, TINTA, kb)], W / 2, 290, "center")
        E.frase(c, t, lerp(kb, kcc, 0.35), [("ninguém", "i", 100), ("decorou", "i", 100), ("a", "i", 100), ("tabuada", "i", 100), ("do", "i", 100), ("23", "g", 100, ERRADO)], W / 2, 500, "center", passo=0.3)
        E.frase(c, t, kcc, [("um", "i", 120), ("bom", "i", 120), ("palpite", "g", 112, COR)], W / 2, 720, "center", passo=0.2)
        E.frase(c, t, kcc + 1.0, [("e", "i", 120), ("uma", "i", 120), ("conferida", "g", 112, COR)], W / 2, 870, "center", passo=0.2)
    E.saida(c, t, C["s02"] - 0.1, tudo)
    if t >= C["s02"]:
        ta, tb = C["s02.a"], C["s02.b"]
        E.foco(c, t, tb - 0.2, 0.7, lambda a: E.bola(c, 1500, 520, 270 * ease_back(prog(t, tb - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, [("até", "i", 90), ("o", "i", 90), ("fim", "i", 90), ("desta", "i", 90), ("aula", "i", 90)], XE, 340)
        E.frase(c, t, lerp(ta, tb, 0.34), [("dividir", "g", 120)], XE, 490)
        E.frase(c, t, lerp(ta, tb, 0.42), [("por", "i", 100), ("dois", "g", 100, COR)], XE, 620, passo=0.2)
        E.frase(c, t, lerp(ta, tb, 0.47), [("algarismos", "g", 100, COR)], XE, 740)
        E.frase(c, t, lerp(ta, tb, 0.6), [("um", "i", 84), ("palpite", "g", 76), ("de", "i", 84), ("cada", "i", 84), ("vez", "i", 84)], XE, 870, passo=0.2)
        E.foco(c, t, tb + 0.2, 0.5, lambda a: (E.centro(c, "+ atalho", 1500, 505, 84, "g", E.SOBRE, a),
                                               E.centro(c, "de prova", 1500, 590, 84, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    lista(c, t, C, "s03", "s03.a", 2, (("s03.b", "dividir por um algarismo,", "com resto"), ("s03.c", "multiplicar por", "dois algarismos")))


# ---------------- estimar ----------------
def b_estimar(c, t, C, b):
    ka, kb = C["s04.a"], C["s04.b"]
    E.frase(c, t, ka - 0.5, [("o", "i", 110), ("segredo", "i", 110), ("é", "i", 110), ("estimar", "g", 150, COR)], W / 2, 280, "center", passo=0.18)
    E.frase(c, t, lerp(ka, kb, 0.15), [("calcular", "i", 84), ("por", "i", 84), ("cima", "g", 76, COR)], W / 2, 420, "center", passo=0.2)
    E.frase(c, t, lerp(ka, kb, 0.5), [("deve", "i", 84), ("dar", "i", 84), ("uns", "i", 84), ("R$ 100", "g", 76)], W / 2, 530, "center", passo=0.25)
    y = 720
    E.foco(c, t, kb, 0.5, lambda a: E.centro(c, "23", 650, y + 45, 150, "g", TINTA, a))
    q = ep(t, kb + 0.4, 0.4)
    if q > 0:
        M.arrow(c, 800, y, 1010, y, COR, q, 6, 20, q)
    E.foco(c, t, kb + 0.8, 0.5, lambda a: E.centro(c, "20", 1160, y + 45, 150, "g", COR, a))
    f = C["s04.end"]
    E.frase(c, t, lerp(kb, f, 0.3), [("o", "i", 72), ("redondo", "g", 64, COR), ("é", "i", 72), ("só", "i", 72), ("para", "i", 72), ("pensar", "i", 72)], W / 2, 860, "center", passo=0.2)
    E.frase(c, t, lerp(kb, f, 0.6), [("a", "i", 72), ("conta", "i", 72), ("continua", "i", 72), ("com", "i", 72), ("23", "g", 68)], W / 2, 955, "center", passo=0.2)


# ---------------- exemplo, palpite alto ----------------
D_1035 = E.dividir("1035", 23, 0)
XC, YC, SC, XP = 170, 360, 104, 1020


def b_conta(c, t, C, b):
    a5, b5, c5, d5 = C["s05.a"], C["s05.b"], C["s05.c"], C["s05.d"]
    k6 = {x: C["s06." + x] for x in "abcde"}
    k7 = {x: C["s07." + x] for x in "abcdef"}
    k8 = {x: C["s08." + x] for x in "abcde"}
    k9 = {x: C["s09." + x] for x in "ab"}
    E.frase(c, t, a5, [("arme", "i", 76), ("a", "i", 76), ("chave", "g", 68, COR)], W / 2, 150, "center") if t < k9["a"] else None
    if t >= k9["a"]:
        E.frase(c, t, k9["a"], [("resultado:", "i", 76), ("R$ 45", "g", 72, COR), ("para", "i", 76), ("cada", "i", 76), ("pessoa", "i", 76)], W / 2, 150, "center", passo=0.15)
    Q = E.conta_div(c, t, D_1035, (k7["e"], k8["d"]), (k8["a"] + 0.4, k8["e"]), a5, XC, YC, SC, ts=(k7["f"],))
    desce(c, t, k8["a"], XC, YC, SC, 3, 0)
    cl = E.casa(SC)
    # o primeiro pedaço: a caixa cresce até caber o divisor
    for tk, n, tf in ((b5, 1, c5), (c5, 2, d5), (d5, 3, C["s06"] - 0.1)):
        if tk <= t < tf:
            q = ep(t, tk, 0.25)
            E.caixa_pontilhada(c, XC - 6, YC - SC * 0.86, n * cl + 12, SC * 1.02, q, COR, prog_=q)

    def fala5():
        lin(c, t, lerp(a5, b5, 0.4), "o primeiro pedaço", XP, 330, 66, "i", COR)
        lin(c, t, lerp(a5, b5, 0.72), "em que o 23 caiba", XP, 420, 66, "i", COR)
        lin(c, t, b5, "1 não dá", XP, 540, 76, "b", ERRADO)
        lin(c, t, c5, "10 não dá", XP, 640, 76, "b", ERRADO)
        lin(c, t, d5, "103 dá", XP, 750, 84, "g", CERTO)
    E.saida(c, t, C["s06"] - 0.1, fala5)

    def fala6():
        lin(c, t, k6["a"], "103 = 10 notas e um troco", XP, 330, 64)
        lin(c, t, k6["b"], "20 = 2 notas", XP, 440, 64)
        igual(c, t, k6["c"], lerp(k6["c"], k6["d"], 0.65), "10 ÷ 2 =", "5", XP, 560, 76)
        y = 700
        cobre(c, t, k6["d"] + 0.8, "103", XP, y, 92)
        cobre(c, t, k6["d"] + 1.1, "20", XP + 280, y, 92)
        lin(c, t, k6["d"], "cubra o último algarismo", XP, 620 + 170, 56, "i")
        lin(c, t, k6["e"] - 0.5, "palpite:", XP, 900, 76, "i")
        lin(c, t, k6["e"], "5", XP + 260, 900, 92, "g", COR)
    if t >= C["s06"]:
        E.saida(c, t, C["s07"] - 0.1, fala6)

    def fala7():
        igual(c, t, k7["a"], lerp(k7["a"], k7["b"], 0.75), "23 × 5 =", "115", XP, 320, 76)
        lin(c, t, k7["b"], "passou de 103", XP, 430, 72, "b", ERRADO)
        lin(c, t, k7["c"] - 0.5, "palpite alto: baixe um", XP, 540, 66, "g", COR)
        igual(c, t, k7["d"], lerp(k7["d"], k7["e"], 0.5), "23 × 4 =", "92", XP, 670, 76)
        E.foco(c, t, lerp(k7["d"], k7["e"], 0.75), 0.4, lambda a: E.selo(c, XP + 590, 645, 42, True, a))
        lin(c, t, k7["e"], "4 no quociente", XP, 780, 66)
        igual(c, t, k7["f"] - 0.9, k7["f"], "103 − 92 =", "11", XP, 890, 76)
    if t >= C["s07"]:
        E.saida(c, t, C["s08"] - 0.1, fala7)

    def fala8():
        igual(c, t, k8["a"], k8["a"] + 0.4, "desça o 5:", "115", XP, 330, 76)
        cobre(c, t, k8["b"] - 0.7, "115", XP, 470, 84)
        cobre(c, t, k8["b"] - 0.4, "20", XP + 260, 470, 84)
        igual(c, t, k8["b"], lerp(k8["b"], k8["c"], 0.6), "11 ÷ 2 =", "5", XP, 590, 76)
        igual(c, t, k8["c"], lerp(k8["c"], k8["d"], 0.7), "23 × 5 =", "115", XP, 710, 76)
        lin(c, t, k8["d"], "5 no quociente", XP, 820, 66)
        lin(c, t, k8["e"], "sobra 0", XP, 920, 76, "b", CERTO)
    if t >= C["s08"]:
        E.saida(c, t, C["s09"] - 0.1, fala8)

    if t >= C["s09"]:
        bola_txt(c, t, k9["a"], "R$ 45", XP + 200, 480, 150, 92)
        lin(c, t, lerp(k9["a"], k9["b"], 0.8), "prova real", XP, 740, 72, "i", COR)
        igual(c, t, k9["b"], lerp(k9["b"], C["s09.end"], 0.6), "23 × 45 =", "1.035", XP, 850, 80)
        E.foco(c, t, lerp(k9["b"], C["s09.end"], 0.85), 0.4, lambda a: E.selo(c, XP + 660, 825, 50, True, a))


# ---------------- erro: palpite baixo ----------------
D_756 = E.dividir("756", 28, 0)


def b_erro(c, t, C, b):
    x, y, size = 190, 360, 110
    xp = 1000
    k0 = {x_: C["s10." + x_] for x_ in "abcde"}
    k1 = {x_: C["s11." + x_] for x_ in "abcd"}
    k2 = {x_: C["s12." + x_] for x_ in "abcdef"}
    k3 = {x_: C["s13." + x_] for x_ in "abc"}
    q6 = k1["b"] + 0.9  # o 6 provisório: E.conta_div só escreve o 7, na fala de s12
    E.frase(c, t, C["s10"] + 0.1, [("palpite", "i", 80), ("baixo", "g", 72, ERRADO)], W / 2, 150, "center") if t < C["s13"] else None
    if t < C["s13"]:
        Q = E.conta_div(c, t, D_756, (lerp(k0["c"], k0["d"], 0.5), k2["d"] + 0.2), (k1["a"] + 0.4, k2["e"]), k0["a"], x, y, size, ts=(k0["e"],))
        desce(c, t, k1["a"], x, y, size, 2, 0)
        palpite(c, t, Q, D_756, size, 1, "6", q6, k2["d"])
        if lerp(k0["a"], k0["b"], 0.4) <= t < C["s10.end"]:
            q = ep(t, lerp(k0["a"], k0["b"], 0.4), 0.25)
            E.caixa_pontilhada(c, x - 6, y - size * 0.86, 2 * E.casa(size) + 12, size * 1.02, q, COR, prog_=q)

    def fala10():
        lin(c, t, lerp(k0["a"], k0["b"], 0.4), "primeiro pedaço: 75", xp, 320, 62, "i", COR)
        lin(c, t, k0["b"] - 0.7, "28 fica perto de", xp, 430, 62)
        lin(c, t, k0["b"], "30", xp + 550, 430, 80, "g", COR)
        cobre(c, t, lerp(k0["b"], k0["c"], 0.6), "75", xp, 560, 84)
        cobre(c, t, lerp(k0["b"], k0["c"], 0.8), "30", xp + 200, 560, 84)
        igual(c, t, k0["c"], lerp(k0["c"], k0["d"], 0.6), "7 ÷ 3 =", "2", xp + 400, 560, 76)
        igual(c, t, k0["d"], lerp(k0["d"], k0["e"], 0.7), "28 × 2 =", "56", xp, 690, 76)
        igual(c, t, k0["e"] - 0.9, k0["e"], "75 − 56 =", "19", xp, 810, 76)
    E.saida(c, t, C["s11"] - 0.1, fala10)

    def fala11():
        igual(c, t, k1["a"], k1["a"] + 0.4, "desça o 6:", "196", xp, 330, 76)
        igual(c, t, k1["b"], q6, "19 ÷ 3 =", "6", xp, 470, 76)
        igual(c, t, k1["c"], lerp(k1["c"], k1["d"], 0.65), "28 × 6 =", "168", xp, 600, 76)
        igual(c, t, k1["d"] - 1.2, k1["d"] + 0.3, "196 − 168 =", "28", xp, 730, 76, cor2=ERRADO)
    if t >= C["s11"]:
        E.saida(c, t, C["s12"] - 0.1, fala11)

    def fala12():
        E.foco(c, t, k2["a"], 0.5, lambda a: E.escreve(c, "26, resto 28?", xp, 340, 84, "g", ERRADO, a))
        E.frase(c, t, k2["b"], [("resto", "g", 68, ERRADO), ("igual", "i", 76), ("ao", "i", 76), ("divisor", "g", 68, ERRADO)], xp, 460, passo=0.16)
        lin(c, t, lerp(k2["b"], k2["c"], 0.62), "ainda cabe mais um 28", xp, 570, 66, "i")
        lin(c, t, k2["c"] - 0.5, "palpite baixo: suba um", xp, 680, 66, "g", COR)
        lin(c, t, k2["d"], "7 no quociente", xp, 790, 66)
        lin(c, t, k2["e"], "sobra 0", xp + 490, 790, 66, "b", CERTO)
        bola_txt(c, t, k2["f"] + 0.3, "27", xp + 90, 900, 90, 84)
    if t >= C["s12"]:
        E.saida(c, t, C["s13"] - 0.1, fala12)

    if t >= C["s13"]:
        E.frase(c, t, C["s13"] + 0.1, [("as", "i", 92), ("regras", "g", 84, COR), ("em", "i", 92), ("uma", "i", 92), ("linha", "i", 92)], W / 2, 190, "center", passo=0.16)
        for y_, k, s1, s2, cr in ((370, k3["a"], "passou do número:", "baixe um", ERRADO), (530, k3["b"], "resto igual ou maior:", "suba um", CERTO)):
            lin(c, t, k, s1, 330, y_, 76, "i")
            lin(c, t, k + 1.0, s2, 1150, y_, 84, "g", cr)
        E.frase(c, t, lerp(k3["b"], k3["c"], 0.5), [("e", "i", 84), ("confira", "g", 76, COR), ("de", "i", 84), ("novo", "i", 84)], 330, 690, passo=0.2)
        E.frase(c, t, k3["c"] - 1.0, [("se", "i", 84), ("der", "i", 84), ("mais", "i", 84), ("que", "i", 84), ("9,", "g", 76)], 330, 860, passo=0.14)
        E.frase(c, t, k3["c"], [("comece", "g", 76, COR), ("do", "i", 84), ("9", "g", 76, COR)], 900, 860, passo=0.2)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def limites():
        ka, kb, kcc, kd, ke = C["s14.a"], C["s14.b"], C["s14.c"], C["s14.d"], C["s14.e"]
        E.frase(c, t, C["s14"] + 0.1, [("agora,", "i", 76, CLARO), ("o", "i", 76, CLARO), ("atalho:", "i", 76, CLARO)], W / 2, 150, "center", passo=0.1)
        E.frase(c, t, ka, [("o", "i", 100, CLARO), ("tamanho", "g", 92, BR), ("do", "i", 100, CLARO), ("resultado", "g", 92, BR)], W / 2, 280, "center", passo=0.2)
        E.frase(c, t, ka + 1.2, [("antes", "i", 84, CLARO), ("de", "i", 84, CLARO), ("dividir", "i", 84, CLARO)], W / 2, 390, "center", passo=0.16)
        E.foco(c, t, kb, 0.5, lambda a: E.escreve(c, "23 × 10 =", 220, 570, 84, "g", BR, a))
        E.foco(c, t, lerp(kb, kcc, 0.65), 0.5, lambda a: E.escreve(c, "230", 720, 570, 84, "g", CLARO, a))
        E.foco(c, t, kcc, 0.5, lambda a: E.escreve(c, "23 × 100 =", 220, 700, 84, "g", BR, a))
        E.foco(c, t, lerp(kcc, kd, 0.6), 0.5, lambda a: E.escreve(c, "2.300", 760, 700, 84, "g", CLARO, a))
        vx = E.reta(c, t, kd, 1110, 1700, 640, 230, 2300, (230, 2300), lambda v: f"{v:,}".replace(",", "."), escuro=True, size=52, tm=(kd, kd))
        E.foco(c, t, kd + 0.5, 0.5, lambda a: (c.drawCircle(vx(1035), 640, 18, M.paint(BR, a)), E.centro(c, "1.035", vx(1035), 590, 64, "g", BR, a)))
        E.frase(c, t, ke, [("mais", "i", 84, CLARO), ("de", "i", 84, CLARO), ("10", "g", 84, BR), ("e", "i", 84, CLARO), ("menos", "i", 84, CLARO), ("de", "i", 84, CLARO), ("100", "g", 84, BR), ("vezes", "i", 84, CLARO)], W / 2, 860, "center", passo=0.16)
        E.frase(c, t, lerp(ke, C["s14.end"], 0.55), [("dois", "g", 84, BR), ("algarismos", "g", 84, BR)], W / 2, 970, "center", passo=0.16)
    E.saida(c, t, C["s15"] - 0.1, limites)
    if t >= C["s15"]:
        ka, kb, kcc = C["s15.a"], C["s15.b"], C["s15.c"]
        E.frase(c, t, ka, [("vezes", "i", 100, CLARO), ("10", "g", 92, BR), ("e", "i", 100, CLARO), ("vezes", "i", 100, CLARO), ("100", "g", 92, BR), ("saem", "i", 100, CLARO), ("de", "i", 100, CLARO), ("cabeça", "i", 100, CLARO)], W / 2, 300, "center", passo=0.16)
        E.frase(c, t, lerp(ka, kb, 0.5), [("marcam", "i", 84, CLARO), ("os", "i", 84, CLARO), ("limites", "g", 76, BR)], W / 2, 420, "center", passo=0.18)
        E.foco(c, t, kb, 0.5, lambda a: E.selo(c, 300, 610, 72, True, a))
        E.frase(c, t, kb + 0.1, [("elimina", "g", 76, BR), ("alternativas", "i", 84, CLARO), ("de", "i", 84, CLARO), ("tamanho", "i", 84, CLARO), ("errado", "i", 84, CLARO)], 410, 635, passo=0.2)
        E.foco(c, t, kcc, 0.5, lambda a: E.selo(c, 300, 790, 72, False, a))
        E.frase(c, t, kcc + 0.1, [("todas", "i", 84, CLARO), ("do", "i", 84, CLARO), ("mesmo", "i", 84, CLARO), ("tamanho", "g", 76, BR)], 410, 815, passo=0.2)
        E.frase(c, t, lerp(kcc, C["s15.end"], 0.72), [("aí,", "i", 84, CLARO), ("arme", "g", 76, BR), ("a", "g", 76, BR), ("conta", "g", 76, BR)], 410, 930, passo=0.12)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s16"] + 0.1, [("hora", "i", 72, COR), ("de", "i", 72, COR), ("testar", "i", 72, COR)], XE, 200)
    E.frase(c, t, C["s16.a"] - 0.8, [("um", "i", 92), ("sítio", "i", 92), ("colheu", "i", 92)], XE, 340, passo=0.25)
    E.frase(c, t, C["s16.a"], [("1.400", "g", 104, COR), ("laranjas", "g", 92)], XE, 470, passo=0.3)
    E.frase(c, t, C["s16.b"], [("26", "g", 104, COR), ("em", "i", 92), ("cada", "i", 92), ("caixa", "i", 92)], XE, 600, passo=0.2)
    E.frase(c, t, C["s16.c"], [("quantas", "i", 92), ("caixas", "g", 84, COR), ("cheias?", "g", 84, COR)], XE, 770, passo=0.22)
    E.frase(c, t, lerp(C["s16.c"], C["s16.end"], 0.5), [("quantas", "i", 92), ("laranjas", "g", 84, COR), ("sobram?", "g", 84, COR)], XE, 880, passo=0.22)
    E.relogio(c, t, C["s17.a"], 1490, 400, 200)


# ---------------- resposta ----------------
D_1400 = E.dividir("1400", 26, 0)


def b_resposta(c, t, C, b):
    x, y, size, xp = 170, 360, 104, 1020
    k = {x_: C["s18." + x_] for x_ in "abcdefgh"}
    p = {x_: C["s19." + x_] for x_ in "abcdef"}
    q4 = lerp(k["c"], k["d"], 0.6)  # o 4 provisório: E.conta_div só escreve o 5
    E.frase(c, t, C["s18"] + 0.1, [("1.400", "g", 80, COR), ("÷", "g", 80), ("26", "g", 80)], W / 2, 150, "center", passo=0.16)
    Q = E.conta_div(c, t, D_1400, (k["g"] - 0.2, lerp(p["b"], p["c"], 0.6)), (p["a"] + 0.4, p["d"]), C["s18"] + 0.1, x, y, size, ts=(k["h"],))
    palpite(c, t, Q, D_1400, size, 0, "4", q4, k["g"] - 0.4)
    desce(c, t, p["a"], x, y, size, 3, 0)
    if k["a"] <= t < C["s18.end"]:
        q = ep(t, k["a"], 0.25)
        E.caixa_pontilhada(c, x - 6, y - size * 0.86, 3 * E.casa(size) + 12, size * 1.02, q, COR, prog_=q)

    def fala18():
        lin(c, t, k["a"], "primeiro pedaço: 140", xp, 300, 60, "i", COR)
        lin(c, t, k["b"] - 0.7, "26 fica perto de", xp, 400, 60)
        lin(c, t, k["b"], "30", xp + 530, 400, 76, "g", COR)
        igual(c, t, k["c"], q4, "14 ÷ 3 =", "4", xp, 510, 72)
        igual(c, t, k["d"], lerp(k["d"], k["e"], 0.7), "26 × 4 =", "104", xp, 610, 72)
        igual(c, t, k["e"] - 0.9, k["e"], "140 − 104 =", "36", xp, 710, 72, cor2=ERRADO)
        lin(c, t, k["f"] - 0.8, "resto maior: suba um", xp, 810, 62, "g", COR)
        igual(c, t, k["g"], lerp(k["g"], k["h"], 0.7), "26 × 5 =", "130", xp, 910, 72)
        lin(c, t, k["h"], "sobram 10", xp + 470, 910, 66, "b", COR)
    E.saida(c, t, C["s19"] - 0.1, fala18)
    if t >= C["s19"]:
        igual(c, t, p["a"], p["a"] + 0.4, "desça o 0:", "100", xp, 330, 76)
        cobre(c, t, p["b"] - 0.2, "100", xp, 460, 84)
        cobre(c, t, p["b"], "30", xp + 260, 460, 84)
        igual(c, t, p["b"], lerp(p["b"], p["c"], 0.6), "10 ÷ 3 =", "3", xp + 400, 460, 66)
        igual(c, t, p["c"], lerp(p["c"], p["d"], 0.65), "26 × 3 =", "78", xp, 580, 76)
        lin(c, t, p["d"], "sobram 22", xp, 690, 76, "b", COR)
        bola_txt(c, t, p["e"], "53", xp + 100, 860, 100, 92)
        E.frase(c, t, p["e"] + 0.3, [("caixas", "i", 76), ("cheias", "i", 76)], xp + 230, 850, passo=0.15)
        E.frase(c, t, p["f"], [("sobram", "i", 76), ("22", "g", 76, COR), ("laranjas", "i", 76)], xp + 230, 930, passo=0.15)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s20"], [("resumindo", "i", 92, COR)], W / 2, 210, "center")
        for i, (k, s) in enumerate((("s20.a", "arredonde o divisor"), ("s20.b", "dê o palpite"), ("s20.c", "confira multiplicando"))):
            y = 390 + i * 190
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 260, y - 24, 56, a=a),
                                                         E.centro(c, str(i + 1), 260, y - 1, 64, "g", E.SOBRE, a)))
            E.frase(c, t, C[k] + 0.1, [(s, "g", 80)], 350, y)
    E.saida(c, t, C["s21"] - 0.1, resumo)
    if t < C["s21"]:
        return
    E.frase(c, t, C["s21"] + 0.1, [("você", "i", 84), ("já", "i", 84), ("sabe", "i", 84), ("as", "i", 84), ("quatro", "g", 76), ("contas", "i", 84)], XE, 270, passo=0.18)
    E.frase(c, t, lerp(C["s21"], C["s21.a"], 0.72), [("próxima", "i", 84), ("aula", "i", 84)], XE, 390)
    E.frase(c, t, C["s21.a"], [("escolher", "g", 130, COR), ("a", "i", 120), ("conta", "g", 130, COR)], XE, 530, passo=0.2)
    E.frase(c, t, C["s21.a"] + 1.0, [("pelas", "i", 84), ("palavras", "g", 76), ("do", "i", 84), ("problema", "i", 84)], XE, 650, passo=0.16)
    E.foco(c, t, C["s21.b"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1440, 790, 76, estilo="g", a=a, cor=E.SOBRE))
    p = ease_io(prog(t, C["s21.b"] + 0.3, 0.8))
    E.cursor(c, lerp(1770, 1570, p), lerp(1000, 815, p), ep(t, C["s21.b"] + 0.2, 0.4))
    E.frase(c, t, C["s21.c"], [("bons", "i", 120), ("estudos!", "i", 120, COR)], XE, 900)


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, estimar=b_estimar, conta=b_conta, erro=b_erro, atalho=b_atalho,
              questao=b_questao, resposta=b_resposta, fim=b_fim)
