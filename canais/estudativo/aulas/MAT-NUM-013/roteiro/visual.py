"""Visual — Estudativo · MAT-NUM-013: ordem das operações e parênteses.
Identidade em _ferramentas/editorial.py. Toda expressão que se resolve passa por E.expressao, que confere se as etapas valem o mesmo.
Peças locais: envelope, degrau, monta (expressão que se escreve por partes) e bloco_em (caixa em volta de um trecho)."""
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco
import motor as M
import skia

E.usar("Matemática", "Números e Contas")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-NUM-013_ordem_operacoes_parenteses.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("envelopes", "regra", "colchetes", "atalho", "questao", "fim"))
BR = "#FFFFFF"


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


def pal(s, estilo="i", size=84, cor=TINTA):
    """frase em palavras, para entrar uma a uma"""
    return [(p, estilo, size, cor) for p in s.split()]


def bola_txt(c, t, t0, s, cx, cy, r, size, cor=CERTO):
    """o resultado na esfera"""
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r, cor, a), E.centro(c, s, cx, cy + size * 0.35, size, "g", M.on(cor), a)))


def xpos(s, i, size):
    """x do caractere i dentro de s, escrito na grotesca pesada"""
    return E.larg(s[:i], "g", size) + (E.APERTO["g"] * size if i else 0)


def monta(c, t, s, mascara, tempos, cx, y, size, tinta=None):
    """expressão que se escreve por partes, cada uma na sua fala (peça local).
    mascara = uma letra por caractere; tempos = {letra: t0 ou (t0, cor)}"""
    assert len(s) == len(mascara), (s, mascara)
    x = cx - E.larg(s, "g", size) / 2
    i = 0
    while i < len(s):
        j = i
        while j < len(s) and mascara[j] == mascara[i]:
            j += 1
        v = tempos[mascara[i]]
        t0, cor = v if isinstance(v, tuple) else (v, tinta or TINTA)
        E.foco(c, t, t0, 0.45, lambda a, i=i, j=j, cor=cor: E.escreve(c, s[i:j], x + xpos(s, i, size), y, size, "g", cor, a))
        i = j


def bloco_em(c, t, t0, s, trecho, cx, y, size, cor=CLARO):
    """caixa pontilhada em volta de um trecho da expressão; devolve o centro do trecho (peça local)"""
    i = s.find(trecho)
    x = cx - E.larg(s, "g", size) / 2 + xpos(s, i, size)
    w = E.larg(trecho, "g", size)
    q = ep(t, t0, 0.4)
    E.caixa_pontilhada(c, x - 22, y - size * 0.92, w + 44, size * 1.2, q, cor, prog_=q)
    return x + w / 2


def envelope(c, cx, cy, w, h, s, a=1.0, cor=None):
    """envelope com o valor escrito (peça local)"""
    if a <= 0:
        return
    cor = cor or TINTA
    x, y = cx - w / 2, cy - h / 2
    M.rrect(c, x, y, w, h, 12, E.VAZIO, a)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 12, 12), M.paint(cor, a, stroke=5))
    aba = skia.Path()
    aba.moveTo(x + 6, y + 6); aba.lineTo(cx, y + h * 0.42); aba.lineTo(x + w - 6, y + 6)
    c.drawPath(aba, M.paint(cor, a, stroke=4))
    E.centro(c, s, cx, y + h * 0.86, h * 0.34, "g", cor, a)


def degrau(c, i, x, y, w, h, simb, nome, a):
    """um degrau da escada da ordem: número, símbolos e nome (peça local)"""
    if a <= 0:
        return
    M.rrect(c, x, y, w, h, 18, E.COR, a)
    E.escreve(c, str(i), x + 44, y + h * 0.71, 92, "g", E.SOBRE, a)
    E.escreve(c, simb, x + 150, y + h * 0.71, 88, "g", E.SOBRE, a)
    E.escreve(c, nome, x + 390, y + h * 0.7, 80, "i", E.SOBRE, a)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def conta():
        y, s = 410, 170
        E.foco(c, t, C["s01.a"], 0.5, lambda a: E.escreve(c, "2 + 3 × 4", XE, y, s, "g", TINTA, a))
        E.foco(c, t, C["s01.b"], 0.5, lambda a: E.escreve(c, "= 20", 1010, y, s, "g", ERRADO, a))
        E.risco(c, 1130, y + 20, 1420, y - 150, t, C["s01.c"], largura=16)
        E.foco(c, t, C["s01.c"], 0.5, lambda a: E.selo(c, 1580, y - 60, 90, False, a))
        E.frase(c, t, C["s01.d"] - 0.3, pal("a resposta é", size=110), XE, 760)
        bola_txt(c, t, C["s01.d"], "14", 960, 720, 150, 150)
    E.saida(c, t, C["s02"] - 0.1, conta)
    if t >= C["s02"]:
        ta, tb, tc = C["s02.a"], C["s02.b"], C["s02.c"]
        E.foco(c, t, tc - 0.2, 0.7, lambda a: E.bola(c, 1490, 520, 280 * ease_back(prog(t, tc - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, pal("até o fim desta aula", size=90), XE, 330)
        E.frase(c, t, lerp(ta, tb, 0.7), [("resolve", "g", 124), ("contas", "g", 124)], XE, 480)
        E.frase(c, t, tb, pal("com", size=110) + [("parênteses", "g", 120, COR)], XE, 640, passo=0.12)
        E.frase(c, t, lerp(tb, tc, 0.4), pal("e", size=110) + [("colchetes", "g", 120, COR)], XE, 790, passo=0.12)
        E.foco(c, t, tc + 0.2, 0.5, lambda a: (E.centro(c, "+ atalho", 1490, 505, 84, "g", E.SOBRE, a),
                                               E.centro(c, "de prova", 1490, 590, 84, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    ta, fim = C["s03.a"], C["s03.end"]
    E.frase(c, t, C["s03"] + 0.1, pal("você só precisa das"), XE, 410)
    E.foco(c, t, ta, 0.5, lambda a: E.escreve(c, "4", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, ta + 0.15, 0.5, lambda a: E.escreve(c, "operações", XE + 250, 700, 104, "i", TINTA, a))
    itens = (("+", "somar", 0.16), ("−", "subtrair", 0.23), ("×", "multiplicar", 0.30), ("÷", "dividir", 0.42))
    for i, (s, nome, f) in enumerate(itens):
        x, y = 980 + (i % 2) * 400, 230 + (i // 2) * 320
        ti = lerp(ta, fim, f)
        p = ep(t, ti, 0.5)
        E.caixa_pontilhada(c, x, y, 360, 280, p, prog_=p)
        E.foco(c, t, ti + 0.05, 0.45, lambda a, s=s, x=x, y=y, nome=nome: (E.centro(c, s, x + 180, y + 150, 150, "g", COR, a),
                                                                            E.centro(c, nome, x + 180, y + 240, 62, "i", TINTA, a)))


# ---------------- por que o vezes vem antes ----------------
XS = (380, 670, 960, 1250, 1540)  # lugar dos cinco envelopes
YE = 400


def b_envelopes(c, t, C, b):
    def carteira():
        E.frase(c, t, C["s04"] + 0.1, pal("por que", size=92) + [("14?", "g", 92, COR)], W / 2, 170, "center")
        ta, tb = C["s04.a"], C["s04.b"]
        for x, dt in ((380, 0.0), (670, 0.25)):
            a0 = 1 - ep(t, C["s05.c"], 0.4)
            E.foco(c, t, ta + dt, 0.5, lambda a, x=x: E.moeda(c, x, YE, 100, "R$ 1", a * a0))
        for x, dt in ((960, 0.0), (1250, 0.35), (1540, 0.7)):
            E.foco(c, t, tb + dt, 0.5, lambda a, x=x: envelope(c, x, YE, 260, 190, "R$ 4", a))

        def rotulos():
            E.foco(c, t, ta + 0.4, 0.5, lambda a: E.centro(c, "2 reais soltos", 525, 650, 66, "i", TINTA, a))
            E.foco(c, t, tb + 0.8, 0.5, lambda a: E.centro(c, "3 envelopes de 4 reais", 1250, 650, 66, "i", TINTA, a))
        E.saida(c, t, C["s05"] - 0.1, rotulos)
        E.saida(c, t, C["s05"] - 0.1, lambda: E.frase(c, t, C["s04.c"], pal("quanto dinheiro você", size=110) + [("tem?", "g", 110, COR)], W / 2, 860, "center"))
        # a conta dos envelopes
        ka, kb, kc, kd = C["s05.a"], C["s05.b"], C["s05.c"], C["s05.d"]
        E.chave(c, 840, 1660, 520, TINTA, ep(t, ka, 0.4), h=26)
        E.foco(c, t, ka, 0.5, lambda a: E.centro(c, "3 × 4 = 12", 1250, 660, 92, "g", TINTA, a))
        E.frase(c, t, kb, [("2 + 12 =", "g", 92), ("14", "g", 104, CERTO)], 525, 660, "center", passo=0.1)
        # quem soma primeiro: os reais soltos viram envelopes que nunca existiram
        for x, dt in ((380, 0.1), (670, 0.3)):
            E.foco(c, t, kc + dt, 0.5, lambda a, x=x: envelope(c, x, YE, 260, 190, "R$ 4", a, ERRADO))
        E.frase(c, t, kc, [("5 × 4 = 20", "g", 110, ERRADO)], W / 2, 840, "center")
        E.frase(c, t, kd, [("6", "g", 84, ERRADO)] + pal("reais que nunca existiram", size=84), W / 2, 980, "center", passo=0.12)
    E.saida(c, t, C["s06"] - 0.1, carteira)

    if t < C["s06"]:
        return
    ta, tb, fim = C["s06.a"], C["s06.b"], C["s06.end"]
    E.linha(c, t, [("o vezes é", "i", 92, TINTA, C["s06"] + 0.1), ("uma soma", "i", 92, TINTA, ta), ("empacotada", "g", 92, COR, ta + 0.3)], W / 2, 180, "center")
    y = 400
    for i, x in enumerate((560, 960, 1360)):
        E.foco(c, t, lerp(ta, tb, 0.2 + i * 0.09), 0.5, lambda a, x=x: envelope(c, x, y, 260, 190, "4", a))
    for x, f in ((760, 0.25), (1160, 0.34)):
        E.foco(c, t, lerp(ta, tb, f), 0.45, lambda a, x=x: E.centro(c, "+", x, y + 36, 110, "g", COR, a))
    E.frase(c, t, lerp(ta, tb, 0.5), [("÷", "g", 84, COR)] + pal("também: pacotes iguais", size=84), W / 2, 620, "center", passo=0.14)
    E.frase(c, t, tb, pal("primeiro os", size=96) + [("pacotes", "g", 100, COR)], W / 2, 790, "center", passo=0.14)
    E.frase(c, t, lerp(tb, fim, 0.5), pal("depois, o que está", size=96) + [("solto", "g", 100, COR)], W / 2, 930, "center", passo=0.14)


# ---------------- regra ----------------
def b_regra(c, t, C, b):
    def ordem():
        E.frase(c, t, C["s07"] + 0.1, pal("conta com mais de uma operação:", size=76), 750, 190, "center", passo=0.1)
        E.frase(c, t, C["s07.a"], [("expressão", "g", 100, COR)], 1490, 190, "center")
        E.frase(c, t, lerp(C["s07.a"], C["s07.b"], 0.45), pal("sempre a mesma ordem", size=76), W / 2, 310, "center", passo=0.1)
        for i, (k, simb, nome) in enumerate((("s07.b", "( )", "parênteses"), ("s07.c", "× ÷", "vezes e dividido"), ("s07.d", "+ −", "mais e menos"))):
            E.foco(c, t, C[k], 0.5, lambda a, i=i, simb=simb, nome=nome: degrau(c, i + 1, 240 + i * 130, 390 + i * 190, 1180, 160, simb, nome, a))
    E.saida(c, t, C["s08"] - 0.1, ordem)

    def parentese():
        ka, kb, kc = C["s08.a"], C["s08.b"], C["s08.c"]
        fim = C["s08.end"]
        E.frase(c, t, ka - 0.3, [("parêntese", "g", 88, COR)] + pal("manda fazer", size=92) + [("primeiro", "g", 88, COR)], W / 2, 190, "center", passo=0.14)
        E.expressao(c, t, [("(2 + 3) × 4", "(2 + 3)", kb + 0.8), ("20", "20", kc)], [kc], W / 2, 350, 124, t0=kb, empilha=150)
        E.frase(c, t, lerp(kc, fim, 0.22), pal("sem parêntese:", size=76) + [("2 + 3 × 4 = 14", "g", 80)], W / 2, 690, "center", passo=0.12)
        E.frase(c, t, lerp(kc, fim, 0.58), pal("com ele:", size=76) + pal("o de dentro", size=76) + pal("passa na", size=76) + [("frente", "g", 80, COR)], W / 2, 850, "center", passo=0.12)
    if C["s08"] - 0.1 <= t:
        E.saida(c, t, C["s09"] - 0.1, parentese)

    def dividido():
        ka, kb, kc = C["s09.a"], C["s09.b"], C["s09.c"]
        E.frase(c, t, C["s09"] + 0.1, pal("a ordem com o", size=84) + [("dividido", "g", 84, COR)], W / 2, 190, "center", passo=0.12)
        E.expressao(c, t, [("7 + 12 ÷ 3", "12 ÷ 3", kb), ("7 + 4", "7 + 4", kc), ("11", "11", lerp(kc, C["s09.end"], 0.72))],
                    [lerp(kb, kc, 0.72), lerp(kc, C["s09.end"], 0.72)], W / 2, 420, 130, empilha=175, t0=ka)
    if C["s09"] - 0.1 <= t:
        E.saida(c, t, C["s10"] - 0.1, dividido)

    if t >= C["s10"]:
        ka, kb, kc, kd = C["s10.a"], C["s10.b"], C["s10.c"], C["s10.d"]
        fim = C["s10.end"]
        E.frase(c, t, C["s10"] + 0.1, pal("agora, com", size=84) + [("tudo", "g", 84, COR), ("junto", "g", 84, COR)], W / 2, 170, "center", passo=0.12)
        tp = [lerp(kb, kc, 0.8), lerp(kc, kd, 0.8), lerp(kd, fim, 0.75)]
        E.expressao(c, t, [("30 − (2 + 4) × 3", "(2 + 4)", kb), ("30 − 6 × 3", "6 × 3", kc), ("30 − 18", "30 − 18", kd), ("12", "12", tp[2])],
                    tp, 700, 340, 116, empilha=170, t0=ka)
        x = 1290
        E.frase(c, t, kb, pal("primeiro", size=66) + [("o parêntese", "g", 62, COR)], x, 320, passo=0.1)
        E.frase(c, t, kc, pal("depois", size=66) + [("o vezes", "g", 62, COR)], x, 490, passo=0.1)
        E.frase(c, t, kd, pal("por último", size=66) + [("o menos", "g", 62, COR)], x, 660, passo=0.1)


# ---------------- colchetes ----------------
YC, SC = 400, 124


def b_colchetes(c, t, C, b):
    s = "20 − [3 × (4 + 1)]"
    if t < C["s12"]:
        ka, kb, kc, kd = C["s11.a"], C["s11.b"], C["s11.c"], C["s11.d"]
        E.frase(c, t, C["s11"] + 0.1, pal("e parêntese dentro de", size=88) + [("parêntese?", "g", 88, COR)], W / 2, 180, "center", passo=0.12)
        monta(c, t, s, "aaaaabccccdeeeeedb", dict(a=kb, b=(kb, COR), c=kc, d=kc, e=kd), W / 2, YC, SC)
        E.frase(c, t, ka - 0.2, pal("o de fora vira", size=84) + [("colchete", "g", 84, COR)], W / 2, 660, "center", passo=0.12)
        E.frase(c, t, lerp(ka, kb, 0.4), [("[ ]", "g", 90, COR)] + pal("um parêntese de cantos retos", size=78), W / 2, 820, "center", passo=0.12)
        return
    ka, kb, kc, kd, ke = C["s12.a"], C["s12.b"], C["s12.c"], C["s12.d"], C["s12.e"]
    E.frase(c, t, ka, pal("de", size=96) + [("dentro", "g", 96, COR)] + pal("para", size=96) + [("fora", "g", 96, COR)], W / 2, 190, "center", passo=0.12)
    E.expressao(c, t, [(s, "(4 + 1)", kb), ("20 − [3 × 5]", "[3 × 5]", kc), ("20 − 15", "20 − 15", kd), ("5", "5", ke)],
                [lerp(kb, kc, 0.6), lerp(kc, kd, 0.75), ke], W / 2, YC, SC, empilha=155, t0=C["s12"])


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    s = "12 ÷ 2 × 3"

    def engano():
        ka, kb, kc = C["s13.a"], C["s13.b"], C["s13.c"]
        E.frase(c, t, C["s13"] + 0.1, [("cuidado", "g", 100, ERRADO)] + pal("com este erro", size=96), W / 2, 200, "center", passo=0.13)
        E.frase(c, t, ka, pal("o vezes", size=88) + [("sempre", "g", 84, ERRADO)] + pal("vem antes do dividido?", size=88), W / 2, 350, "center", passo=0.12)
        cx, y, size = 760, 640, 170
        E.foco(c, t, kb, 0.5, lambda a: E.centro(c, s, cx, y, size, "g", TINTA, a))
        if t >= kc:
            bloco_em(c, t, kc, s, "2 × 3", cx, y, size, ERRADO)
        E.foco(c, t, kc + 0.4, 0.5, lambda a: E.escreve(c, "= 2", 1270, y, size, "g", ERRADO, a))
    E.saida(c, t, C["s14"] - 0.1, engano)
    if t < C["s14"]:
        return
    ka, kb, kc, kd, ke = C["s14.a"], C["s14.b"], C["s14.c"], C["s14.d"], C["s14.e"]
    fim = C["s14.end"]
    E.frase(c, t, ka, pal("no", size=92) + [("mesmo", "g", 92, COR), ("degrau", "g", 92, COR)], W / 2, 170, "center", passo=0.13)

    def pilar(y, s_, ti):
        def fn(a):
            M.rrect(c, 190, y, 620, 150, 18, E.COR, a)
            E.centro(c, s_, 500, y + 112, 100, "g", E.SOBRE, a)
        E.foco(c, t, ti, 0.5, fn)
    pilar(240, "× ÷", ka)
    if t >= kb:
        p = ep(t, kb, 0.7)
        M.arrow(c, 210, 450, 790, 450, COR, p, 7, 22, p)
    E.foco(c, t, kb + 0.1, 0.5, lambda a: E.centro(c, "da esquerda para a direita", 500, 530, 56, "i", TINTA, a))
    tp = [lerp(kc, kd, 0.72), lerp(kd, ke, 0.3)]
    E.expressao(c, t, [(s, "12 ÷ 2", kc), ("6 × 3", "6 × 3", kd), ("18", "18", tp[1])], tp, 1340, 340, 112, empilha=125, t0=C["s14"])
    pilar(690, "+ −", lerp(kd, ke, 0.5))
    if t >= lerp(kd, ke, 0.5):
        p = ep(t, lerp(kd, ke, 0.55), 0.7)
        M.arrow(c, 210, 880, 790, 880, COR, p, 7, 22, p)
    E.foco(c, t, ke, 0.5, lambda a: E.centro(c, "10 − 3 + 2", 1250, 810, 112, "g", TINTA, a))
    E.foco(c, t, lerp(ke, fim, 0.8), 0.5, lambda a: E.escreve(c, "= 9", 1540, 810, 112, "g", CERTO, a))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    s = "6 × 5 − 8 ÷ 2 + 1"

    def explica():
        ka, kb, kc = C["s15.a"], C["s15.b"], C["s15.c"]
        E.frase(c, t, C["s15"] + 0.1, pal("agora, o atalho:", size=84, cor=CLARO), W / 2, 200, "center", passo=0.1)
        E.frase(c, t, ka, pal("os", size=170, cor=BR) + [("blocos", "g", 170, BR)], W / 2, 390, "center", passo=0.14)
        E.frase(c, t, kb, pal("separe nos sinais de", size=84, cor=CLARO) + [("+", "g", 92, BR), ("e", "i", 84, CLARO), ("−", "g", 92, BR)], W / 2, 570, "center", passo=0.1)
        E.frase(c, t, lerp(kb, kc, 0.55), pal("cada pedaço é um bloco, resolvido sozinho", size=78, cor=CLARO), W / 2, 700, "center", passo=0.1)
        E.frase(c, t, kc, pal("só no fim,", size=90, cor=CLARO) + [("junte", "g", 92, BR), ("os", "g", 92, BR), ("blocos", "g", 92, BR)], W / 2, 860, "center", passo=0.1)
    E.saida(c, t, C["s16"] - 0.1, explica)

    def exemplo():
        ka, kb, kc, kd, ke = C["s16.a"], C["s16.b"], C["s16.c"], C["s16.d"], C["s16.e"]
        fim = C["s16.end"]
        cx, y, size = W / 2, 340, 140
        E.foco(c, t, ka, 0.5, lambda a: E.centro(c, s, cx, y, size, "g", BR, a))
        E.frase(c, t, lerp(ka, kb, 0.72), pal("três blocos", size=72, cor=CLARO), W / 2, 170, "center")
        y2 = 620
        xs = []
        for tr, k, res, f in (("6 × 5", kb, "30", 0.72), ("8 ÷ 2", kc, "4", 0.72), ("1", kd, "1", 0.2)):
            if t >= k:
                xs.append(bloco_em(c, t, k, s, tr, cx, y, size))
                seta_x = xs[-1]
                q = ep(t, k, 0.4)
                M.arrow(c, seta_x, y + 60, seta_x, y2 - 130, CLARO, q, 4, 14, q)
            prox = {kb: kc, kc: kd, kd: ke}[k]
            E.foco(c, t, lerp(k, prox, f), 0.45, lambda a, seta_x=seta_x if t >= k else 0, res=res: E.centro(c, res, seta_x, y2, 130, "g", CLARO, a))
        if len(xs) == 3:
            E.foco(c, t, ke, 0.45, lambda a: (E.centro(c, "−", (xs[0] + xs[1]) / 2, y2, 110, "g", BR, a),
                                              E.centro(c, "+", (xs[1] + xs[2]) / 2, y2, 110, "g", BR, a)))
        E.frase(c, t, lerp(ke, fim, 0.7), [("30 − 4 + 1 =", "g", 96, BR)], 900, 860, "center")
        bola_txt(c, t, lerp(ke, fim, 0.85), "27", 1320, 830, 110, 110)
    if C["s16"] - 0.1 <= t:
        E.saida(c, t, C["s17"] - 0.1, exemplo)

    if t >= C["s17"]:
        ka, kb, kc = C["s17.a"], C["s17.b"], C["s17.c"]
        fim = C["s17.end"]
        E.frase(c, t, C["s17"] + 0.1, pal("funciona porque", size=84, cor=CLARO), W / 2, 170, "center", passo=0.1)
        E.foco(c, t, ka, 0.5, lambda a: E.selo(c, 290, 320, 72, True, a))
        E.frase(c, t, C["s17"] + 0.4, [("×", "g", 76, BR), ("e", "i", 76, CLARO), ("÷", "g", 76, BR)] + pal("vêm antes,", size=76, cor=CLARO), 400, 300, passo=0.1)
        E.frase(c, t, ka, [("grudados", "g", 76, BR)] + pal("no mesmo bloco", size=76, cor=CLARO), 400, 390, passo=0.1)
        E.foco(c, t, kb, 0.5, lambda a: E.selo(c, 290, 560, 72, False, a))
        E.frase(c, t, kb, pal("não corte", size=76, cor=CLARO) + [("dentro", "g", 76, BR)] + pal("de parênteses", size=76, cor=CLARO), 400, 540, passo=0.1)
        E.frase(c, t, lerp(kb, kc, 0.3), pal("lá dentro é um bloco só, e vem primeiro", size=64, cor=CLARO), 400, 625, passo=0.08)
        E.foco(c, t, kc, 0.5, lambda a: E.selo(c, 290, 800, 72, False, a))
        E.frase(c, t, kc, pal("só", size=76, cor=CLARO) + [("×", "g", 76, BR), ("e", "i", 76, CLARO), ("÷?", "g", 76, BR)] + pal("não compensa", size=76, cor=CLARO), 400, 780, passo=0.1)
        E.frase(c, t, lerp(kc, fim, 0.5), pal("tudo um bloco, da esquerda para a direita", size=64, cor=CLARO), 400, 865, passo=0.08)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    ka, kb, kc = C["s18.a"], C["s18.b"], C["s18.c"]
    E.frase(c, t, C["s18"], pal("hora de testar", size=72, cor=COR), XE, 200)
    E.frase(c, t, ka - 0.3, pal("resolva", size=100), XE, 420)
    monta(c, t, "40 − [5 × (2 + 4)]", "aaaaabccccdeeeeedb", dict(a=ka, b=(ka, COR), c=kb, d=kb, e=kc), 640, 620, 106)
    E.relogio(c, t, C["s19.a"], 1490, 400, 200)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    ka, kb, kc, kd = C["s20.a"], C["s20.b"], C["s20.c"], C["s20.d"]
    fim = C["s20.end"]
    E.frase(c, t, C["s20"] + 0.1, pal("de dentro para", size=84) + [("fora", "g", 84, COR)], W / 2, 170, "center", passo=0.12)
    E.expressao(c, t, [("40 − [5 × (2 + 4)]", "(2 + 4)", ka), ("40 − [5 × 6]", "[5 × 6]", kb), ("40 − 30", "40 − 30", kc), ("10", "10", kd)],
                [lerp(ka, kb, 0.75), lerp(kb, kc, 0.75), kd], W / 2, 320, 116, empilha=145, t0=C["s20"])
    E.foco(c, t, kd + 0.2, 0.5, lambda a: E.selo(c, 1120, 725, 62, True, a))
    E.frase(c, t, lerp(kd, fim, 0.25), [("40 − 5", "g", 76, ERRADO)] + pal("primeiro saiu da ordem:", size=78) + pal("o colchete vem antes", size=78), W / 2, 930, "center", passo=0.1)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s21"], [("resumindo", "i", 92, COR)], W / 2, 190, "center")
        for i, (k, s) in enumerate((("s21.a", "parênteses"), ("s21.b", "vezes e dividido"), ("s21.c", "mais e menos"))):
            y = 350 + i * 170
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 300, y - 30, 56, a=a), E.centro(c, str(i + 1), 300, y - 7, 64, "g", E.SOBRE, a)))
            E.frase(c, t, C[k] + 0.1, [(s, "g", 92)], 400, y)
        E.frase(c, t, C["s21.d"] - 0.5, pal("no mesmo degrau,", size=84) + pal("da esquerda para a", size=84) + [("direita", "g", 84, COR)], W / 2, 900, "center", passo=0.12)
    E.saida(c, t, C["s22"] - 0.1, resumo)
    if t < C["s22"]:
        return
    E.frase(c, t, C["s22"] + 0.1, pal("próxima aula"), XE, 270)
    E.frase(c, t, C["s22.a"], pal("você lê um", size=96) + [("problema", "g", 110, COR)] + pal("de compra", size=96), XE, 420, passo=0.12)
    E.frase(c, t, C["s22.b"], pal("e monta a", size=96) + [("expressão", "g", 110, COR)] + pal("do troco", size=96), XE, 570, passo=0.12)
    E.foco(c, t, C["s22.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1440, 700, 76, estilo="g", a=a, cor=E.SOBRE))
    p = ease_io(prog(t, C["s22.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1770, 1570, p), lerp(960, 725, p), ep(t, C["s22.c"] + 0.2, 0.4))
    E.frase(c, t, C["s22.d"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 900, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, envelopes=b_envelopes, regra=b_regra, colchetes=b_colchetes, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
