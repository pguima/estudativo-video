"""Visual — Estudativo · MAT-FRA-017: dividir com resultado decimal.
Identidade em _ferramentas/editorial.py. A conta na chave é o centro da aula: E.dividir faz a divisão de verdade e a vírgula
entra no quociente no instante da fala (tv). O painel à direita repete, em palavras, o passo que a voz está dizendo."""
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco
import motor as M
import skia

E.usar("Matemática", "Frações e Decimais")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-FRA-017_dividir_resultado_decimal.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("virgula", "continuar", "zero", "atalho", "questao", "fim"))
BR = "#FFFFFF"


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


def num(c, t, t0, s, xv, y, size, cor=None, cores=None):
    """decimal alinhado pela vírgula, com entrada de foco"""
    E.foco(c, t, t0, 0.5, lambda a: E.numero(c, s, xv, y, size, "g", cor, a, cores))


def bola_txt(c, t, t0, s, cx, cy, r, size, cor=CERTO):
    """o resultado na esfera"""
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r, cor, a), E.centro(c, s, cx, cy + size * 0.35, size, "g", M.on(cor), a)))


def lin(c, t, t0, s, x, y, size=64, estilo="b", cor=None):
    """uma linha do painel ao lado da conta"""
    E.foco(c, t, t0, 0.4, lambda a: E.escreve(c, s, x, y, size, estilo, cor or TINTA, a))


def resto(c, t, t0, x, y, size, linha, col, s):
    """o resto sozinho, antes de receber o algarismo ou o zero: E.conta_div só escreve a linha inteira, de uma vez (peça local).
    linha = linha de baixo (0 = a primeira), col = coluna do último algarismo. Fica no mesmo lugar em que a peça escreve depois."""
    cl, dy = E.casa(size), size * 1.12
    for m, ch in enumerate(s):
        i = col - (len(s) - 1 - m)
        E.foco(c, t, t0, 0.4, lambda a, ch=ch, i=i: E.centro(c, ch, x + (i + 0.5) * cl, y + (linha + 1) * dy, size, "g", TINTA, a))


def quociente(Q, D, size):
    """centro de cada algarismo do quociente, a partir do que E.conta_div devolve"""
    q = D["quociente"]
    pos = q.find(",")
    xv = Q["xq"] + (pos if pos >= 0 else len(q)) * E.larg("0", "g", size) * 1.1 + size * 0.17
    return E._centros(q, xv, size)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def tudo():
        ka, kb, kc, kd = C["s01.a"], C["s01.b"], C["s01.c"], C["s01.d"]
        E.linha(c, t, [("7 reais", "g", 120, COR, ka), ("entre", "i", 110, TINTA, kb - 0.3), ("4 pessoas", "g", 120, TINTA, kb)], W / 2, 260, "center")
        E.frase(c, t, kc, [("dá", "i", 120), ("1,", "g", 130), ("e", "i", 120), ("sobram", "i", 120), ("3", "g", 130, COR)], W / 2, 480, "center", passo=0.14)
        num(c, t, kd, "1,3", 900, 750, 230, ERRADO)
        E.frase(c, t, lerp(kd, C["s01.end"], 0.6), [("esse", "i", 92), ("dinheiro", "i", 92), ("não", "g", 84, ERRADO), ("fecha", "g", 84, ERRADO)], W / 2, 930, "center", passo=0.12)
    E.saida(c, t, C["s02"] - 0.1, tudo)
    if t >= C["s02"]:
        ta, tb = C["s02.a"], C["s02.b"]
        E.foco(c, t, tb - 0.2, 0.7, lambda a: E.bola(c, 1500, 520, 270 * ease_back(prog(t, tb - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, [("até", "i", 90), ("o", "i", 90), ("fim", "i", 90), ("desta", "i", 90), ("aula", "i", 90)], XE, 340)
        E.frase(c, t, lerp(ta, tb, 0.33), [("continuar", "g", 124)], XE, 490)
        E.frase(c, t, lerp(ta, tb, 0.38), [("a", "i", 110), ("divisão", "g", 124)], XE, 620)
        E.frase(c, t, lerp(ta, tb, 0.48), [("depois", "i", 92), ("da", "i", 92), ("vírgula", "i", 92, COR)], XE, 740)
        E.frase(c, t, lerp(ta, tb, 0.62), [("até", "i", 84), ("o", "i", 84), ("resto", "g", 76), ("acabar", "i", 84)], XE, 860)
        E.foco(c, t, tb + 0.2, 0.5, lambda a: (E.centro(c, "+ atalho", 1500, 505, 84, "g", E.SOBRE, a),
                                               E.centro(c, "de prova", 1500, 590, 84, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def lista(c, t, C, ini, ta, n, itens):
    E.frase(c, t, C[ini], [("você", "i", 84), ("só", "i", 84), ("precisa", "i", 84), ("de", "i", 84)], XE, 410)
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


def b_lembrete(c, t, C, b):
    lista(c, t, C, "s03", "s03.a", 2, (("s03.b", "dividir por um", "algarismo, com resto"), ("s03.c", "saber o que são", "décimos e centésimos")))


# ---------------- vírgula no dividendo ----------------
D_75 = E.dividir("7,5", 3)


def b_virgula(c, t, C, b):
    x, y, size = 230, 400, 130
    E.linha(c, t, [("R$ 7,50", "g", 84, COR, C["s04.a"]), ("para", "i", 92, TINTA, C["s04.b"] - 0.3), ("3 pessoas", "g", 84, TINTA, C["s04.b"])], W / 2, 170, "center")
    E.conta_div(c, t, D_75, (lerp(C["s05.a"], C["s05.b"], 0.7), lerp(C["s06.d"], C["s06.e"], 0.6)), (C["s06.b"], lerp(C["s06.d"], C["s06.e"], 0.85)), C["s04.c"], x, y, size, tv=C["s05.c"])
    resto(c, t, C["s05.b"], x, y, size, 0, 0, "1")
    xp = 1060

    def fala5():
        lin(c, t, C["s05.a"], "7 ÷ 3 = 2", xp, 340, 80)
        lin(c, t, C["s05.b"], "sobra 1", xp, 460, 80)
        E.frase(c, t, C["s05.c"], [("vírgula", "g", 72, COR), ("no", "i", 80), ("resultado", "i", 80)], xp, 600, passo=0.1)
    E.saida(c, t, C["s06"] - 0.1, fala5)
    if t >= C["s06"]:
        lin(c, t, C["s06.a"], "1 real vira", xp, 320, 72, "i")
        lin(c, t, C["s06.a"] + 0.2, "10 moedas de 10¢", xp, 410, 72, "b", COR)
        lin(c, t, C["s06.b"], "mais 5 moedas", xp, 510, 72, "b")
        lin(c, t, C["s06.c"], "15 ao todo", xp, 610, 72, "g", COR)
        lin(c, t, C["s06.d"], "15 ÷ 3 = 5", xp, 710, 72)
        bola_txt(c, t, C["s06.e"], "R$ 2,50", 1270, 880, 134, 60)
        E.frase(c, t, C["s06.f"], [("para", "i", 70), ("cada", "i", 70), ("pessoa", "i", 70)], 1425, 905, passo=0.1)


# ---------------- continuar depois da vírgula ----------------
D_7 = E.dividir("7", 4)


def b_continuar(c, t, C, b):
    x, y, size = 200, 380, 120
    xp = 1170
    E.linha(c, t, [("7 reais", "g", 84, COR, C["s07.a"]), ("para", "i", 92, TINTA, C["s07.a"]), ("4 pessoas", "g", 84, TINTA, C["s07.a"])], W / 2, 170, "center")
    Q = E.conta_div(c, t, D_7, (lerp(C["s07.a"], C["s07.b"], 0.7), lerp(C["s09.a"], C["s09.b"], 0.7), lerp(C["s10.a"], C["s10.b"], 0.7)), (C["s08.c"], C["s09.d"], C["s10.b"]), C["s07.a"], x, y, size, tv=C["s08.b"])
    resto(c, t, C["s07.b"], x, y, size, 0, 0, "3")
    resto(c, t, C["s09.b"], x, y, size, 1, 1, "2")
    dy = size * 1.12
    cl = E.casa(size)
    cen = quociente(Q, D_7, size)
    # o 3 que vira 30: caixa em volta da linha na fala do "trinta"
    if C["s08.d"] <= t < C["s09"]:
        q = ep(t, C["s08.d"], 0.3)
        E.caixa_pontilhada(c, x - 6, y + dy - size * 0.86, 2 * cl + 12, size * 1.02, q, COR, prog_=q)

    def fala7():
        lin(c, t, C["s07.a"] + 0.2, "7 ÷ 4 = 1", xp, 340, 80)
        lin(c, t, C["s07.b"], "sobram 3", xp, 460, 80)
    E.saida(c, t, C["s08"] - 0.1, fala7)

    def fala8():
        E.frase(c, t, C["s08"] + 0.1, [("a", "i", 70), ("conta", "i", 70), ("não", "i", 70), ("precisa", "i", 70), ("parar", "g", 62, COR)], xp, 310, passo=0.1)
        lin(c, t, C["s08.a"] - 0.5, "3 reais viram", xp, 430, 62, "i")
        lin(c, t, C["s08.a"], "30 moedas de 10¢", xp, 510, 62, "b", COR)
        E.frase(c, t, C["s08.b"], [("vírgula", "g", 62, COR), ("no", "i", 70), ("resultado", "i", 70)], xp, 630, passo=0.1)
        lin(c, t, C["s08.c"], "um zero ao lado do resto", xp, 730, 56, "i")
        lin(c, t, C["s08.d"], "o 3 vira 30", xp, 830, 66, "g", COR)
    if t >= C["s08"]:
        E.saida(c, t, C["s09"] - 0.1, fala8)

    def fala9():
        lin(c, t, C["s09.a"], "30 ÷ 4 = 7", xp, 340, 80)
        lin(c, t, C["s09.b"], "sobram 2 moedas", xp, 460, 64)
        lin(c, t, C["s09.c"], "viram 20 moedas de 1¢", xp, 570, 58, "b", COR)
        lin(c, t, C["s09.d"], "mais um zero: 20", xp, 680, 64, "g", COR)
    if t >= C["s09"]:
        E.saida(c, t, C["s10"] - 0.1, fala9)

    def fala10():
        lin(c, t, C["s10.a"], "20 ÷ 4 = 5", xp, 340, 80)
        lin(c, t, C["s10.b"], "sobra 0", xp, 460, 80, "b", CERTO)
        E.frase(c, t, C["s10.c"], [("acabou:", "i", 80), ("1,75", "g", 90, COR)], xp, 590, passo=0.2)
        bola_txt(c, t, C["s10.d"], "R$ 1,75", 1320, 790, 140, 64)
        E.frase(c, t, C["s10.d"] + 0.3, [("cada", "i", 72)], 1490, 790)
        E.frase(c, t, C["s10.d"] + 0.4, [("pessoa", "i", 72)], 1490, 860)
    if t >= C["s10"]:
        E.saida(c, t, C["s11"] - 0.1, fala10)

    def fala11():
        E.frase(c, t, C["s11"] + 0.1, [("confira", "i", 84, COR)], xp, 300)
        lin(c, t, C["s11.a"], "4 × R$ 1 = R$ 4", xp, 430, 72)
        lin(c, t, C["s11.b"], "4 × 75¢ = R$ 3", xp, 560, 72)
        lin(c, t, C["s11.c"], "total: R$ 7", xp, 700, 72, "g", COR)
        E.foco(c, t, lerp(C["s11.c"], C["s11.end"], 0.5), 0.5, lambda a: E.selo(c, xp + 560, 680, 62, True, a))
    if t >= C["s11"]:
        E.saida(c, t, C["s12"] - 0.1, fala11)

    if t >= C["s12"]:
        E.frase(c, t, C["s12.a"], [("sobrou", "i", 76), ("resto?", "i", 76)], xp, 320, passo=0.1)
        lin(c, t, C["s12.a"] + 0.6, "acrescente", xp, 420, 70, "g", COR)
        lin(c, t, C["s12.a"] + 0.8, "um zero", xp, 500, 70, "g", COR)
        lin(c, t, C["s12.a"] + 1.2, "e continue", xp, 590, 70, "i")
        y_q = Q["y_q"]
        for i, k, nome, yn in ((2, "s12.b", "décimos", 730), (3, "s12.c", "centésimos", 830)):
            q = ep(t, C[k], 0.4)
            if q > 0:
                E.caixa_pontilhada(c, cen[i] - 62, y_q - 108, 124, 128, q, COR, prog_=q)
            lin(c, t, C[k], nome, xp, yn, 76, "g", COR)


# ---------------- menor que o divisor ----------------
D_1 = E.dividir("1", 4)


def b_menor(c, t, C, b):
    x, y, size = 200, 380, 120
    xp = 1170
    ka, kb, kc, kd, ke = C["s13.a"], C["s13.b"], C["s13.c"], C["s13.d"], C["s13.e"]
    E.frase(c, t, C["s13"] + 0.1, [("e", "i", 88), ("se", "i", 88), ("não", "i", 88), ("der", "i", 88), ("nem", "i", 88), ("um", "i", 88), ("inteiro?", "g", 80, COR)], W / 2, 170, "center", passo=0.1)
    E.conta_div(c, t, D_1, (kb, lerp(kc, kd, 0.2), lerp(kd, ke, 0.3)), (kc, kd, lerp(kd, ke, 0.55)), ka, x, y, size, tv=kb + 0.5)
    resto(c, t, lerp(kc, kd, 0.5), x, y, size, 1, 1, "2")
    lin(c, t, ka, "R$ 1 para 4 pessoas", xp, 330, 58)
    lin(c, t, kb, "1 ÷ 4 não dá", xp, 440, 66, "b", ERRADO)
    lin(c, t, kb + 0.5, "zero e vírgula", xp, 530, 66, "g", COR)
    lin(c, t, kc, "10 ÷ 4 = 2, sobram 2", xp, 640, 58)
    lin(c, t, kd, "20 ÷ 4 = 5, sobra 0", xp, 730, 58)
    bola_txt(c, t, ke, "0,25", 1300, 880, 110, 76)
    E.frase(c, t, ke + 0.6, [("25", "g", 70), ("centavos", "i", 76)], 1430, 905)


# ---------------- zero no resultado ----------------
D_42 = E.dividir("4,2", 4)


def b_zero(c, t, C, b):
    x, y, size = 200, 380, 120
    xp = 1170
    ka, kb, kc, kd = C["s14.a"], C["s14.b"], C["s14.c"], C["s14.d"]
    pa, pb, pc, pd = C["s15.a"], C["s15.b"], C["s15.c"], C["s15.d"]
    E.frase(c, t, ka - 0.5, [("outra", "i", 88), ("armadilha", "g", 80, ERRADO)], W / 2, 170, "center")
    Q = E.conta_div(c, t, D_42, (lerp(kb, kc, 0.5), pa, lerp(pc, pd, 0.65)), (kd, pb, lerp(pc, pd, 0.85)), ka, x, y, size, tv=kc)
    resto(c, t, lerp(kb, kc, 0.8), x, y, size, 0, 0, "0")
    cen = quociente(Q, D_42, size)
    if t >= pa:
        q = ep(t, pa, 0.3)
        E.caixa_pontilhada(c, cen[2] - 62, Q["y_q"] - 108, 124, 128, q, ERRADO, prog_=q)

    def fala14():
        lin(c, t, kb, "4 ÷ 4 = 1, sobra 0", xp, 340, 62)
        E.frase(c, t, kc, [("vírgula", "g", 62, COR), ("no", "i", 70), ("resultado", "i", 70)], xp, 470, passo=0.1)
        lin(c, t, kd, "desça o 2", xp, 590, 66)
        lin(c, t, kd + 0.8, "2 ÷ 4 não dá", xp, 690, 66, "b", ERRADO)
    E.saida(c, t, C["s15"] - 0.1, fala14)
    if t >= C["s15"]:
        E.frase(c, t, C["s15"] + 0.1, [("não", "g", 76, ERRADO), ("pule", "g", 76, ERRADO), ("essa", "i", 84), ("casa", "i", 84)], xp, 320, passo=0.1)
        lin(c, t, pa, "zero no resultado", xp, 440, 62, "g", COR)
        lin(c, t, pb, "zero ao lado do 2", xp, 550, 62, "g", COR)
        lin(c, t, pc, "20 ÷ 4 = 5", xp, 660, 72)
        bola_txt(c, t, pd, "1,05", 1450, 840, 120, 84)


# ---------------- não acaba ----------------
D_10 = E.dividir("10", 3, 3)


def b_semfim(c, t, C, b):
    x, y, size = 170, 330, 96
    xp = 1235
    ka, kb, kc, kd = C["s16.a"], C["s16.b"], C["s16.c"], C["s16.d"]
    f = lambda v: lerp(kb, kc, v)
    E.frase(c, t, ka - 0.3, [("às", "i", 84), ("vezes,", "i", 84), ("o", "i", 84), ("resto", "i", 84), ("nunca", "g", 76, ERRADO), ("zera", "g", 76, ERRADO)], W / 2, 150, "center", passo=0.08)
    Q = E.conta_div(c, t, D_10, (f(0.27), f(0.38), f(0.44), f(0.49)), (f(0.27), f(0.38), f(0.44), f(0.72)), kb, x, y, size, tv=f(0.33))
    cen = quociente(Q, D_10, size)
    E.foco(c, t, f(0.55), 0.4, lambda a: E.escreve(c, "...", cen[4] + 40, Q["y_q"], 90, "g", COR, a))
    E.frase(c, t, f(0.6), [("sem", "i", 76), ("fim", "g", 68, COR)], xp, 300, passo=0.1)
    lin(c, t, f(0.72), "sobra 1 toda vez", xp, 400, 60)
    lin(c, t, kc, "pare na casa pedida", xp, 520, 58, "g", COR)
    lin(c, t, kc + 1.0, "e arredonde", xp, 600, 62, "i")
    tc3 = lerp(kc, kd, 0.55)
    lin(c, t, tc3, "a terceira é um 3,", xp, 700, 58, "i")
    lin(c, t, tc3 + 0.5, "menos que 5", xp, 770, 58, "b")
    bola_txt(c, t, kd, "3,33", 1500, 895, 110, 78)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    ka, kb, kc, kd, ke = C["s17.a"], C["s17.b"], C["s17.c"], C["s17.d"], C["s17.e"]
    E.frase(c, t, ka, [("colar", "g", 84, ERRADO), ("o", "i", 92), ("resto", "g", 84, ERRADO), ("depois", "i", 92), ("da", "i", 92), ("vírgula", "i", 92)], W / 2, 170, "center", passo=0.12)
    E.frase(c, t, lerp(ka, kb, 0.75), [("1,", "g", 110), ("resto", "i", 100), ("3", "g", 110)], 620, 380, "center", passo=0.1)
    if t >= kb:
        p = ep(t, kb - 0.1, 0.4)
        M.arrow(c, 860, 345, 1000, 345, ERRADO, p, 6, 20, p)
    num(c, t, kb, "1,3", 1190, 400, 190, ERRADO)
    E.frase(c, t, kc, [("4", "g", 110), ("×", "g", 92), ("R$ 1,30", "g", 110)], 660, 640, "center", passo=0.15)
    E.frase(c, t, kd, [("=", "g", 92), ("R$ 5,20", "g", 110, ERRADO)], 1250, 640, "center", passo=0.1)
    E.frase(c, t, ke, [("o", "i", 92), ("resto", "g", 84, COR), ("ainda", "i", 92), ("precisa", "i", 92), ("ser", "i", 92), ("dividido", "g", 84, COR)], W / 2, 850, "center", passo=0.12)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def metade():
        ka, kb, kc = C["s18.a"], C["s18.b"], C["s18.c"]
        E.frase(c, t, C["s18"] + 0.1, [("agora,", "i", 76, CLARO), ("o", "i", 76, CLARO), ("atalho:", "i", 76, CLARO)], W / 2, 160, "center", passo=0.1)
        E.frase(c, t, ka, [("dividir", "g", 108, BR), ("por", "i", 116, CLARO), ("4", "g", 130, CLARO)], W / 2, 300, "center", passo=0.1)
        E.frase(c, t, ka + 0.9, [("é", "i", 76, CLARO), ("tirar", "i", 76, CLARO), ("a", "i", 76, CLARO), ("metade,", "g", 68, BR), ("e", "i", 76, CLARO), ("depois", "i", 76, CLARO), ("a", "i", 76, CLARO), ("metade", "g", 68, BR), ("de", "i", 76, CLARO), ("novo", "i", 76, CLARO)], W / 2, 420, "center", passo=0.1)
        y = 700
        E.foco(c, t, kb - 0.3, 0.5, lambda a: E.centro(c, "R$ 7", 300, y + 45, 120, "g", BR, a))
        E.ponte(c, t, kb, 480, 730, y, "÷ 2", CLARO, 56)
        E.foco(c, t, kb + 0.4, 0.5, lambda a: E.centro(c, "R$ 3,50", 960, y + 45, 110, "g", BR, a))
        E.ponte(c, t, kc, 1190, 1440, y, "÷ 2", CLARO, 56)
        E.foco(c, t, kc + 0.4, 0.5, lambda a: E.centro(c, "R$ 1,75", 1640, y + 45, 110, "g", CLARO, a))
    E.saida(c, t, C["s19"] - 0.1, metade)
    if t >= C["s19"]:
        ka, kb = C["s19.a"], C["s19.b"]
        E.frase(c, t, ka, [("4", "g", 170, CLARO), ("=", "g", 140, BR), ("2", "g", 170, BR), ("×", "g", 130, BR), ("2", "g", 170, BR)], W / 2, 340, "center", passo=0.14)
        E.frase(c, t, lerp(ka, kb, 0.4), [("para", "i", 84, CLARO), ("quando", "i", 84, CLARO), ("o", "i", 84, CLARO), ("divisor", "g", 76, BR), ("é", "i", 84, CLARO), ("4", "g", 84, BR)], W / 2, 510, "center", passo=0.1)
        E.foco(c, t, kb, 0.5, lambda a: E.selo(c, 300, 720, 72, False, a))
        E.frase(c, t, kb + 0.1, [("não", "i", 80, CLARO), ("compensa", "i", 80, CLARO), ("se", "i", 80, CLARO), ("a", "i", 80, CLARO), ("metade", "g", 72, BR), ("não", "i", 80, CLARO), ("sai", "i", 80, CLARO), ("de", "i", 80, CLARO), ("cabeça", "g", 72, BR)], 410, 745, passo=0.1)
        E.frase(c, t, kb + 2.2, [("aí,", "i", 84, CLARO), ("arme", "g", 76, BR), ("a", "g", 76, BR), ("conta", "g", 76, BR)], 410, 870, passo=0.12)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s20"], [("hora", "i", 72, COR), ("de", "i", 72, COR), ("testar", "i", 72, COR)], XE, 200)
    E.frase(c, t, C["s20.a"], [("uma", "i", 92), ("conta", "i", 92), ("de", "i", 92), ("R$ 9,30", "g", 104, COR)], XE, 400, passo=0.12)
    E.frase(c, t, C["s20.b"], [("entre", "i", 92), ("6", "g", 104), ("amigos", "g", 92)], XE, 590, passo=0.12)
    E.frase(c, t, C["s20.c"], [("quanto", "i", 110), ("cada", "i", 110), ("um", "i", 110), ("paga?", "g", 100, COR)], XE, 830)
    E.relogio(c, t, C["s21.a"], 1490, 400, 200)


# ---------------- resposta ----------------
D_93 = E.dividir("9,3", 6)


def b_resposta(c, t, C, b):
    x, y, size = 200, 380, 120
    xp = 1170
    ka, kb, kc, kd, ke = C["s22.a"], C["s22.b"], C["s22.c"], C["s22.d"], C["s22.e"]
    pa, pb, pc, pd = C["s23.a"], C["s23.b"], C["s23.c"], C["s23.d"]
    E.frase(c, t, C["s22"] + 0.1, [("R$ 9,30", "g", 84, COR), ("entre", "i", 92), ("6", "g", 84), ("amigos", "g", 84)], W / 2, 170, "center", passo=0.1)
    E.conta_div(c, t, D_93, (lerp(ka, kb, 0.7), ke + 0.3, lerp(pb, pc, 0.6)), (kd, pa, pc), C["s22"] + 0.3, x, y, size, tv=kc)
    resto(c, t, kb, x, y, size, 0, 0, "3")
    resto(c, t, ke + 0.9, x, y, size, 1, 1, "3")

    def fala22():
        lin(c, t, ka, "9 ÷ 6 = 1", xp, 330, 72)
        lin(c, t, kb, "sobram 3", xp, 430, 72)
        E.frase(c, t, kc, [("vírgula", "g", 62, COR), ("no", "i", 70), ("resultado", "i", 70)], xp, 540, passo=0.1)
        lin(c, t, kd, "desça o 3: 33", xp, 650, 66)
        lin(c, t, ke, "33 ÷ 6 = 5, sobram 3", xp, 750, 58)
    E.saida(c, t, C["s23"] - 0.1, fala22)
    if t >= C["s23"]:
        lin(c, t, C["s23"] + 0.2, "sobrou resto: continua", xp, 330, 56, "i")
        lin(c, t, pa, "mais um zero: 30", xp, 440, 66, "g", COR)
        lin(c, t, pb, "30 ÷ 6 = 5", xp, 550, 72)
        lin(c, t, pc, "sobra 0", xp, 660, 72, "b", CERTO)
        bola_txt(c, t, pd, "R$ 1,55", 1320, 840, 140, 64)
        E.frase(c, t, pd + 0.3, [("cada", "i", 72)], 1490, 830)
        E.frase(c, t, pd + 0.4, [("amigo", "i", 72)], 1490, 900)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s24"], [("resumindo", "i", 92, COR)], W / 2, 210, "center")
        for i, (k, s) in enumerate((("s24.a", "chegou na vírgula, coloque a vírgula"), ("s24.b", "sobrou resto, acrescente zero"), ("s24.c", "continue até zerar ou até a casa pedida"))):
            y = 390 + i * 190
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 260, y - 24, 56, a=a),
                                                         E.centro(c, str(i + 1), 260, y - 1, 64, "g", E.SOBRE, a)))
            E.frase(c, t, C[k] + 0.1, [(s, "g", 66)], 350, y)
    E.saida(c, t, C["s25"] - 0.1, resumo)
    if t < C["s25"]:
        return
    E.frase(c, t, lerp(C["s25"], C["s25.a"], 0.72), [("próxima", "i", 84), ("aula", "i", 84)], XE, 300)
    E.frase(c, t, C["s25.a"], [("o", "i", 130), ("divisor", "g", 140, COR), ("tem", "i", 130), ("vírgula", "g", 140, COR)], XE, 450, passo=0.12)
    E.frase(c, t, C["s25.b"], [("tirar", "g", 72), ("essa", "i", 80), ("vírgula", "i", 80), ("antes", "i", 80), ("de", "i", 80), ("dividir", "g", 72, COR)], XE, 590, passo=0.1)
    E.foco(c, t, C["s25.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1440, 710, 76, estilo="g", a=a, cor=E.SOBRE))
    p = ease_io(prog(t, C["s25.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1770, 1570, p), lerp(960, 735, p), ep(t, C["s25.c"] + 0.2, 0.4))
    E.frase(c, t, C["s25.d"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 900, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, virgula=b_virgula, continuar=b_continuar, menor=b_menor, zero=b_zero,
              semfim=b_semfim, erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
