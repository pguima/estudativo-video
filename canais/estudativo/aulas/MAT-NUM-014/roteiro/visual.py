"""Visual — Estudativo · MAT-NUM-014: montar a expressão de um problema.
Identidade em _ferramentas/editorial.py. A conta que se resolve passa por E.expressao, que confere se as etapas valem o mesmo.
Peças locais: nota (cédula), pacote (etiqueta de item da compra) e monta (expressão que se escreve por partes)."""
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco
import motor as M
import skia

E.usar("Matemática", "Números e Contas")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-NUM-014_montar_expressao_problema.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("problema", "dividir", "atalho", "questao", "fim"))
BR = "#FFFFFF"
EXPR = "200 − (3 × 25 + 2 × 40)"


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


def nota(c, x, y, w, h, s, a=1.0):
    """cédula na cor da matéria (peça local, a mesma de MAT-FRA-015)"""
    if a <= 0:
        return
    M.rrect(c, x, y, w, h, 22, E.COR, a)
    r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x + 16, y + 16, w - 32, h - 32), 12, 12)
    c.drawRRect(r, M.paint(E.SOBRE, 0.55 * a, stroke=4))
    E.centro(c, s, x + w / 2, y + h / 2 + h * 0.13, h * 0.38, "g", E.SOBRE, a)


def pacote(c, x, y, w, h, n, nome, preco, a=1.0):
    """item da compra: quantidade, nome e preço de cada um (peça local)"""
    if a <= 0:
        return
    M.rrect(c, x, y, w, h, 18, E.VAZIO, a)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 18, 18), M.paint(TINTA, a, stroke=4))
    E.escreve(c, n, x + 36, y + h * 0.68, 120, "g", COR, a)
    E.escreve(c, nome, x + 130, y + h * 0.46, 66, "b", TINTA, a)
    E.escreve(c, preco, x + 130, y + h * 0.8, 58, "i", TINTA2, a)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def conta():
        ka, kb, kc, kd = C["s01.a"], C["s01.b"], C["s01.c"], C["s01.d"]
        E.frase(c, t, C["s01"] + 0.1, pal("você paga com", size=96), XE, 280, passo=0.12)
        E.foco(c, t, ka, 0.5, lambda a: nota(c, XE, 330, 460, 230, "R$ 200", a))
        E.frase(c, t, kb - 0.3, pal("e o troco dá", size=96), 900, 280, passo=0.12)
        E.foco(c, t, kb, 0.5, lambda a: E.escreve(c, "R$ 205", 900, 500, 190, "g", ERRADO, a))
        E.frase(c, t, kc, pal("troco maior que o dinheiro entregue!", size=84), W / 2, 700, "center", passo=0.1)
        E.frase(c, t, kd, pal("faltou um par de", size=100) + [("parênteses", "g", 100, COR)], W / 2, 870, "center", passo=0.12)
    E.saida(c, t, C["s02"] - 0.1, conta)
    if t >= C["s02"]:
        ta, tb = C["s02.a"], C["s02.b"]
        E.foco(c, t, tb - 0.2, 0.7, lambda a: E.bola(c, 1490, 520, 280 * ease_back(prog(t, tb - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, pal("até o fim desta aula", size=90), XE, 330)
        E.frase(c, t, lerp(ta, tb, 0.45), [("um", "g", 124), ("problema", "g", 124)], XE, 490)
        E.frase(c, t, lerp(ta, tb, 0.7), pal("vira uma", size=110), XE, 640)
        E.frase(c, t, lerp(ta, tb, 0.8), [("expressão", "g", 120, COR)] + pal("só", size=110), XE, 790)
        E.foco(c, t, tb + 0.2, 0.5, lambda a: (E.centro(c, "+ atalho", 1490, 505, 84, "g", E.SOBRE, a),
                                               E.centro(c, "de prova", 1490, 590, 84, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    ka, kb, kc = C["s03.a"], C["s03.b"], C["s03.c"]
    E.frase(c, t, C["s03"] + 0.1, pal("você só precisa de"), XE, 410)
    E.foco(c, t, ka, 0.5, lambda a: E.escreve(c, "2", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, ka + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 240, 700, 120, "i", TINTA, a))
    x, w = 960, 780
    for y, k, l1, l2 in ((250, kb, "saber qual conta", "o problema pede"), (530, kc, "a ordem", "das operações")):
        p = ep(t, k, 0.5)
        E.caixa_pontilhada(c, x, y, w, 196, p, prog_=p)
        E.frase(c, t, k + 0.1, [(l1, "i", 62)], x + 44, y + 84)
        E.frase(c, t, k + 0.3, [(l2, "g", 62, COR)], x + 44, y + 160)
    E.frase(c, t, lerp(kc, C["s03.end"], 0.3), pal("( ) depois × ÷ por último + −", "g", 52, TINTA2), x + 44, 810, passo=0.06)
    py = lerp(420, 700, ease_io(prog(t, kc - 0.35, 0.5)))
    E.cursor(c, x + w - 30, py, ep(t, kb, 0.4))


# ---------------- montar ----------------
def b_problema(c, t, C, b):
    def enunciado():
        ka, kb, kc, kd = C["s04.a"], C["s04.b"], C["s04.c"], C["s04.d"]
        E.frase(c, t, C["s04"] + 0.1, pal("expressão:", "g", 80, COR) + pal("conta com mais de uma operação", size=80), W / 2, 170, "center", passo=0.1)
        E.foco(c, t, ka, 0.5, lambda a: pacote(c, 190, 260, 720, 220, "3", "camisetas", "R$ 25 cada", a))
        E.foco(c, t, kb, 0.5, lambda a: pacote(c, 1010, 260, 720, 220, "2", "bermudas", "R$ 40 cada", a))
        E.frase(c, t, kc - 0.2, pal("paga com", size=96), 560, 660, passo=0.12)
        E.foco(c, t, kc, 0.5, lambda a: nota(c, 960, 550, 350, 170, "R$ 200", a))
        E.frase(c, t, kd, pal("como escrever o", size=100) + [("troco", "g", 100, COR)] + pal("em uma expressão só?", size=100), W / 2, 890, "center", passo=0.12)
    E.saida(c, t, C["s05"] - 0.1, enunciado)

    def frase_troco():
        ka, kb, kc = C["s05.a"], C["s05.b"], C["s05.c"]
        E.frase(c, t, C["s05"] + 0.1, pal("comece pela frase,", size=88) + pal("sem número nenhum", size=88), W / 2, 220, "center", passo=0.12)
        y = 500
        xs = E.linha(c, t, [("troco", "g", 120, COR, ka), ("=", "g", 110, TINTA, ka + 0.3), ("o que paguei", "i", 116, TINTA, ka + 0.5),
                            ("−", "g", 110, TINTA, ka + 0.9), ("o que gastei", "i", 116, TINTA, ka + 1.2)], W / 2, y, "center")
        E.foco(c, t, kb, 0.5, lambda a: (E.centro(c, "200", xs[2] + 230, y + 170, 130, "g", COR, a),))
        E.foco(c, t, kc, 0.5, lambda a: E.centro(c, "?", xs[4] + 230, y + 180, 150, "g", ERRADO, a))
    if C["s05"] - 0.1 <= t:
        E.saida(c, t, C["s06"] - 0.1, frase_troco)

    def pistas():
        ka, kb, kc, kd = C["s06.a"], C["s06.b"], C["s06.c"], C["s06.d"]
        E.frase(c, t, C["s06"] + 0.1, pal("as palavras dão", size=80) + [("pistas", "g", 80, COR)] + pal("e a história decide", size=80), W / 2, 170, "center", passo=0.1)
        rows = ((ka, "cada", "×", "preço repetido"), (lerp(ka, kb, 0.36), "total", "+", "junta os gastos"), (lerp(ka, kb, 0.62), "troco", "−", "tira o gasto do pago"))
        for i, (ti, p_, s, nota_) in enumerate(rows):
            y = 300 + i * 110
            E.frase(c, t, ti, [(p_, "i", 80)], 300, y)
            E.foco(c, t, ti + 0.2, 0.4, lambda a, y=y, s=s: E.centro(c, s, 590, y, 84, "g", COR, a))
            E.frase(c, t, ti + 0.3, pal(nota_, size=70), 680, y, passo=0.08)
        y = 700
        E.frase(c, t, kb, pal("camisetas:", size=76) + [("3 × 25", "g", 88)], 560, y, "center", passo=0.12)
        E.frase(c, t, kc, pal("bermudas:", size=76) + [("2 × 40", "g", 88)], 1330, y, "center", passo=0.12)
        E.frase(c, t, kd, pal("gasto:", size=84) + [("3 × 25 + 2 × 40", "g", 110, COR)], W / 2, 880, "center", passo=0.12)
    if C["s06"] - 0.1 <= t:
        E.saida(c, t, C["s07"] - 0.1, pistas)

    def parenteses():
        ka, kb, kc = C["s07.a"], C["s07.b"], C["s07.c"]
        fim = C["s07.end"]
        E.frase(c, t, ka, pal("o gasto é", size=88) + [("uma", "g", 88, COR), ("coisa", "g", 88, COR), ("só", "g", 88, COR)], W / 2, 200, "center", passo=0.12)
        E.frase(c, t, lerp(ka, kb, 0.45), pal("o menos tira ele", size=80) + [("inteiro", "g", 80, COR)], W / 2, 320, "center", passo=0.12)
        s = 120
        monta(c, t, EXPR, "aaaaaabcccccccccccccccb"[:len(EXPR)], dict(a=kc, b=(kb, COR), c=kb - 0.2), W / 2, 580, s)
        E.frase(c, t, lerp(kc, fim, 0.72), pal("nada foi", size=80) + [("calculado", "g", 80, COR)] + pal("ainda", size=80), W / 2, 780, "center", passo=0.12)
        E.frase(c, t, lerp(kc, fim, 0.84), pal("a expressão só conta a história da compra", size=76), W / 2, 900, "center", passo=0.08)
    if C["s07"] - 0.1 <= t:
        E.saida(c, t, C["s08"] - 0.1, parenteses)

    if t >= C["s08"]:
        ka, kb, kc, kd, ke, kf = C["s08.a"], C["s08.b"], C["s08.c"], C["s08.d"], C["s08.e"], C["s08.f"]
        tp = [lerp(ka, kb, 0.8), lerp(kb, kc, 0.8), lerp(kc, kd, 0.75), ke]
        E.expressao(c, t, [(EXPR, "3 × 25", ka), ("200 − (75 + 2 × 40)", "2 × 40", kb), ("200 − (75 + 80)", "(75 + 80)", kc),
                           ("200 − 155", "200 − 155", kd), ("45", "45", ke)], tp, 800, 220, 92, empilha=128, t0=C["s08"])
        E.frase(c, t, ke + 0.3, pal("reais de", size=72) + [("troco", "g", 72, COR)], 900, 725)
        E.frase(c, t, kf, pal("confira:", size=76) + [("45 + 155 = 200", "g", 88)], W / 2, 900, "center", passo=0.12)
        E.foco(c, t, lerp(kf, C["s08.end"], 0.82), 0.5, lambda a: E.selo(c, 1490, 870, 62, True, a))


# ---------------- juntar antes de dividir ----------------
def b_dividir(c, t, C, b):
    ka, kb, kc, kd, ke = C["s09.a"], C["s09.b"], C["s09.c"], C["s09.d"], C["s09.e"]
    E.frase(c, t, C["s09"] + 0.1, pal("juntar", "g", 84, COR) + pal("antes de dividir", size=88), W / 2, 170, "center", passo=0.12)
    E.frase(c, t, ka, pal("3 amigos dividem igualmente", size=76), 560, 330, "center", passo=0.09)
    E.foco(c, t, lerp(ka, kb, 0.7), 0.5, lambda a: nota(c, 1020, 240, 300, 150, "R$ 90", a))
    E.foco(c, t, kb, 0.5, lambda a: nota(c, 1400, 240, 300, 150, "R$ 30", a))
    E.foco(c, t, lerp(ka, kb, 0.7), 0.5, lambda a: E.centro(c, "presente", 1170, 450, 56, "i", TINTA, a))
    E.foco(c, t, kb, 0.5, lambda a: E.centro(c, "entrega", 1550, 450, 56, "i", TINTA, a))
    y = 640
    E.foco(c, t, kc, 0.5, lambda a: E.centro(c, "(90 + 30) ÷ 3", 660, y, 120, "g", TINTA, a))
    bola_txt(c, t, kd, "40", 1230, y - 40, 104, 110)
    E.frase(c, t, kd + 0.2, pal("para cada um", size=68), 1360, y)
    E.frase(c, t, lerp(kd, ke, 0.4), pal("sem parêntese:", size=72) + [("90 + 30 ÷ 3", "g", 84)], 780, 880, "center", passo=0.1)
    E.frase(c, t, ke, [("= 100", "g", 96, ERRADO)], 1370, 880, "center")


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    ka, kb, kc, kd, ke = C["s10.a"], C["s10.b"], C["s10.c"], C["s10.d"], C["s10.e"]
    fim = C["s10.end"]
    E.frase(c, t, C["s10"] + 0.1, pal("e aquele troco de", size=84) + [("R$ 205?", "g", 84, ERRADO)], W / 2, 170, "center", passo=0.12)
    E.frase(c, t, ka, pal("esqueceu os", size=84) + [("parênteses", "g", 84, ERRADO)], W / 2, 290, "center", passo=0.12)
    s, cx, y, size = "200 − 75 + 80", W / 2, 490, 130
    E.foco(c, t, kb, 0.5, lambda a: E.centro(c, s, cx - 150, y, size, "g", TINTA, a))
    x0 = cx - 150 - E.larg(s, "g", size) / 2

    def mini(i, f, txt, tt, cor):
        if t < tt:
            return
        q = ep(t, tt, 0.4)
        xa = x0 + xpos(s, i, size)
        xb = x0 + xpos(s, f, size)
        M.line(c, xa, y + 30, xb, y + 30, cor, q, 7, progress=q)
        E.foco(c, t, tt, 0.4, lambda a: E.centro(c, txt, (xa + xb) / 2, y + 100, 60, "i", cor, a))
    mini(4, 8, "só as camisetas", kb, TINTA)
    mini(9, 13, "somando", kc, ERRADO)
    E.foco(c, t, kd + 0.8, 0.5, lambda a: E.escreve(c, "= 205", 1275, y, size, "g", ERRADO, a))
    E.frase(c, t, ke, [("200 − 75 − 80 = 45", "g", 100, CERTO)], W / 2, 790, "center")
    E.foco(c, t, ke + 0.8, 0.5, lambda a: E.selo(c, 1480, 755, 56, True, a))
    E.frase(c, t, lerp(ke, fim, 0.66), pal("o que não pode:", size=76) + [("tirar", "g", 76, ERRADO), ("um", "g", 76, ERRADO), ("e", "i", 76, ERRADO), ("somar", "g", 76, ERRADO), ("o", "g", 76, ERRADO), ("outro", "g", 76, ERRADO)], W / 2, 940, "center", passo=0.08)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def explica():
        ka, kb, kc, kd = C["s11.a"], C["s11.b"], C["s11.c"], C["s11.d"]
        E.frase(c, t, C["s11"] + 0.1, pal("agora, o atalho:", size=84, cor=CLARO), W / 2, 200, "center", passo=0.1)
        E.frase(c, t, ka, pal("a", size=170, cor=BR) + [("frase", "g", 170, BR)] + pal("primeiro", size=170, cor=BR), W / 2, 390, "center", passo=0.14)
        E.frase(c, t, kb, pal("troque cada palavra por", size=88, cor=CLARO) + [("números", "g", 88, BR)], W / 2, 570, "center", passo=0.1)
        E.frase(c, t, kc, pal("a frase diz", size=88, cor=CLARO) + pal("menos", "g", 88, BR) + pal("o", size=88, cor=CLARO) + pal("total?", "g", 88, BR), W / 2, 740, "center", passo=0.1)
        E.frase(c, t, kd, pal("o total vai entre", size=88, cor=CLARO) + [("parênteses", "g", 88, BR)], W / 2, 880, "center", passo=0.1)
    E.saida(c, t, C["s12"] - 0.1, explica)

    if t >= C["s12"]:
        ka, kb, kc = C["s12.a"], C["s12.b"], C["s12.c"]
        E.foco(c, t, ka, 0.5, lambda a: E.selo(c, 290, 280, 72, True, a))
        E.frase(c, t, C["s12"] + 0.2, pal("a frase mostra", size=80, cor=CLARO), 400, 262, passo=0.1)
        E.frase(c, t, ka, pal("o que vem", size=80, cor=CLARO) + [("primeiro", "g", 80, BR)], 400, 352, passo=0.1)
        E.frase(c, t, lerp(ka, kb, 0.5), pal("só tira o total depois de somar", size=66, cor=CLARO), 400, 445, passo=0.08)
        E.foco(c, t, kb, 0.5, lambda a: E.selo(c, 290, 640, 72, False, a))
        E.frase(c, t, kb, pal("não compensa com", size=80, cor=CLARO) + [("um", "g", 80, BR), ("item", "g", 80, BR), ("só", "g", 80, BR)], 400, 660, passo=0.1)
        E.frase(c, t, kc, [("200 − 3 × 25", "g", 100, BR)], 400, 800)
        E.frase(c, t, lerp(kc, C["s12.end"], 0.5), pal("o vezes já vem antes", size=66, cor=CLARO), 400, 900, passo=0.08)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    ka, kb, kc, kd = C["s13.a"], C["s13.b"], C["s13.c"], C["s13.d"]
    E.frase(c, t, C["s13"], pal("hora de testar", size=72, cor=COR), XE, 180)
    E.foco(c, t, ka, 0.5, lambda a: pacote(c, XE, 240, 500, 190, "4", "cadernos", "R$ 8 cada", a))
    E.foco(c, t, kb, 0.5, lambda a: pacote(c, XE + 540, 240, 500, 190, "5", "canetas", "R$ 3 cada", a))
    E.frase(c, t, kc, pal("paga com", size=92), XE, 610, passo=0.1)
    E.foco(c, t, kc, 0.5, lambda a: nota(c, XE + 390, 505, 330, 160, "R$ 100", a))
    E.frase(c, t, kd, pal("escreva a", size=92) + [("expressão", "g", 92, COR)] + pal("e calcule o", size=92) + [("troco", "g", 92, COR)], XE, 900, passo=0.12)
    E.relogio(c, t, C["s14.a"], 1490, 400, 200)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    s = "100 − (4 × 8 + 5 × 3)"

    def monta_():
        ka, kb = C["s15.a"], C["s15.b"]
        E.frase(c, t, ka, pal("troco =", size=92) + pal("o que paguei − o total", size=92), W / 2, 330, "center", passo=0.12)
        E.foco(c, t, kb, 0.5, lambda a: E.centro(c, s, W / 2, 620, 130, "g", TINTA, a))
    E.saida(c, t, C["s16"] - 0.1, monta_)
    if t < C["s16"]:
        return
    ka, kb, kc, kd, ke, kf, kg = (C[f"s16.{k}"] for k in "abcdefg")
    tp = [lerp(ka, kb, 0.75), lerp(kb, kc, 0.75), lerp(kc, kd, 0.8), ke]
    E.expressao(c, t, [(s, "4 × 8", ka), ("100 − (32 + 5 × 3)", "5 × 3", kb), ("100 − (32 + 15)", "(32 + 15)", kc), ("100 − 47", "100 − 47", kd), ("53", "53", ke)],
                tp, 760, 200, 92, empilha=125, t0=C["s16"])
    E.frase(c, t, ke + 0.3, pal("reais de", size=72) + [("troco", "g", 72, COR)], 860, 700)
    E.frase(c, t, kf, pal("confira:", size=76) + [("53 + 47 = 100", "g", 84)], 620, 880, "center", passo=0.12)
    E.foco(c, t, lerp(kf, kg, 0.8), 0.5, lambda a: E.selo(c, 1090, 850, 54, True, a))
    E.frase(c, t, kg, pal("sem os parênteses:", size=70), 1430, 840, "center", passo=0.08)
    E.frase(c, t, kg + 0.4, [("R$ 83", "g", 92, ERRADO)] + pal("inflados", size=74), 1430, 950, "center", passo=0.1)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s17"], [("resumindo", "i", 92, COR)], W / 2, 210, "center")
        for i, (k, s) in enumerate((("s17.a", "primeiro a frase"), ("s17.b", "depois os números"), ("s17.c", "total que se tira: ( )"))):
            y = 390 + i * 190
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 300, y - 30, 56, a=a), E.centro(c, str(i + 1), 300, y - 7, 64, "g", E.SOBRE, a)))
            E.frase(c, t, C[k] + 0.1, [(s, "g", 92)], 400, y)
    E.saida(c, t, C["s18"] - 0.1, resumo)
    if t < C["s18"]:
        return
    E.frase(c, t, C["s18.a"], pal("e quando você", size=88) + [("gasta", "g", 88, COR), ("mais", "g", 88, COR)] + pal("do que tem?", size=88), XE, 240, passo=0.12)
    E.frase(c, t, C["s18.b"] - 0.5, pal("próxima aula"), XE, 370)
    E.frase(c, t, C["s18.b"], [("números", "g", 120, COR), ("negativos", "g", 120, COR)], XE, 510, passo=0.14)
    E.frase(c, t, C["s18.c"], pal("e a", size=100) + [("reta", "g", 110, COR), ("numérica", "g", 110, COR)], XE, 650, passo=0.14)
    E.foco(c, t, C["s18.d"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1500, 640, 76, estilo="g", a=a, cor=E.SOBRE))
    p = ease_io(prog(t, C["s18.d"] + 0.3, 0.8))
    E.cursor(c, lerp(1790, 1630, p), lerp(900, 665, p), ep(t, C["s18.d"] + 0.2, 0.4))
    E.frase(c, t, C["s18.e"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 930, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, problema=b_problema, dividir=b_dividir, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
