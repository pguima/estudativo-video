"""Visual — Estudativo · MAT-POT-012: escrever em notação científica.
A vírgula salta com E.anda; andando com ela, os zeros somem. Peças locais: parafuso, balança da compensação,
casas contadas. Todo instante vem de C[...]: entre dois cues, lerp(C[a], C[b], f), que acompanha qualquer voz."""
import math

import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, passo, palco, centro
import motor as M
import skia

E.usar("Matemática", "Potências e Raízes")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-POT-012_escrever_em_notacao_cientifica.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("porque", "grande", "corrigir", "atalho", "questao", "fim"))
BR = "#FFFFFF"
assert 45 * 10 ** 3 == 45000 and 45 * 10 ** 3 == 45 * 10 ** 2 * 10 and 45 * 10 ** 6 == 45000000
assert len("45000000") == 8 and len("214000000") == 9 and 214 * 10 ** 6 == 214000000


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças desta aula ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    """uma frase, palavra a palavra, no mesmo estilo"""
    return [(w, est, size, cor) for w in txt.split()]


def cen(c, t, t0, s, cx, y, size, cor=None, est="g"):
    E.foco(c, t, t0, 0.5, lambda a: centro(c, s, cx, y, size, est, cor or TINTA, a))


def fcen(c, t, t0, s, cx, y, size, cor=None):
    E.formula_em(c, t, t0, s, cx, y, size, "g", cor, "center")


def pil_f(c, s, cx, cy, size, fundo=None, tinta=None, a=1.0):
    """pílula com fórmula dentro (E.pilula não entende expoente)"""
    w = E.formula(c, s, 0, 0, size, a=0)
    pw, ph = w + size * 1.1, size * 1.7
    M.rrect(c, cx - pw / 2, cy - ph / 2, pw, ph, ph / 2, fundo or E.COR, a)
    E.formula(c, s, cx, cy + size * 0.36, size, "g", tinta or E.SOBRE, a, "center")


def num_m(c, s, cx, y, size, cor=None, a=1.0, cores=None):
    """número com pontos de milhar, centrado; cores = {índice: cor}. Devolve x(i), a borda esquerda do caractere i"""
    ap = E.APERTO["g"] * size
    x0 = cx - E.larg(s, "g", size) / 2
    xs = lambda i: x0 + (E.larg(s[:i], "g", size) + ap if i else 0)
    if a > 0:
        for i, ch in enumerate(s):
            E.escreve(c, ch, xs(i), y, size, "g", (cores or {}).get(i, cor or TINTA), a)
    return xs


def anda_passos(c, t, dig, pos, novo, t0, t1, x, y, size, tv=None, cor=None, cor_v=None):
    """E.anda casa por casa, com o tempo esticado para caber em t0..t1 (o salto da peça dura 0,7 s fixos)"""
    n = abs(pos - novo)
    k = 0.7 * n / (t1 - t0)
    tt = t0 + (t - t0) * k
    lado = 1 if novo > pos else -1
    saltos = [(t0 + i * 0.7, pos + (i + 1) * lado) for i in range(n)]
    return E.anda(c, tt, dig, pos, saltos, x, y, size, cor=cor, cor_v=cor_v, tv=None if tv is None else t0 + (tv - t0) * k)


def casas_contadas(c, t, t0, t1, indices, x, y, size, cor=None):
    """o número de cada casa, embaixo do algarismo, no instante em que a vírgula passa por ele"""
    cl = E.casa(size)
    n = len(indices)
    for k, i in enumerate(indices):
        cen(c, t, lerp(t0, t1, k / n) + 0.2, str(k + 1), x + (i + 0.5) * cl, y + 74, 50, cor or COR, "b")


def some_digitos(c, t, t1, dig, indices, x, y, size, cor=None):
    """algarismos que somem em t1: é o lugar dos zeros que a potência de dez substituiu"""
    cl = E.casa(size)
    for i in indices:
        E.saida(c, t, t1, lambda i=i: E._digito(c, dig[i], x + (i + 0.5) * cl, y, size, "g", cor or TINTA, 1.0))


def parafuso(c, x, y, k, cor, a=1.0):
    """parafuso visto de lado: cabeça, corpo e rosca"""
    if a <= 0:
        return
    M.rrect(c, x - 19 * k, y, 38 * k, 15 * k, 4 * k, cor, a)
    M.rrect(c, x - 8 * k, y + 13 * k, 16 * k, 50 * k, 2 * k, cor, a)
    for j in range(4):
        yy = y + (22 + j * 10) * k
        M.line(c, x - 8 * k, yy + 3 * k, x + 8 * k, yy - 3 * k, E.PAPEL, a, 2.2 * k)


def balanca(c, cx, cy, w, giro, rot_e, rot_d, a=1.0):
    """balança da compensação: giro em graus (> 0 sobe o lado esquerdo); no nível, o valor é o mesmo"""
    if a <= 0:
        return
    ang = math.radians(giro)
    dx, dy = w / 2 * math.cos(ang), w / 2 * math.sin(ang)
    M.line(c, cx, cy, cx, cy + 250, TINTA, a, 10)
    M.line(c, cx - 110, cy + 250, cx + 110, cy + 250, TINTA, a, 12)
    M.line(c, cx - dx, cy - dy, cx + dx, cy + dy, TINTA, a, 12)
    E.bola(c, cx, cy, 24, a=a)
    for lado, rot in ((-1, rot_e), (1, rot_d)):
        px, py = cx + lado * dx, cy + lado * dy
        M.line(c, px, py, px, py + 92, TINTA2, a, 5)
        rot(px, py + 150)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    ka, kb, kc = C["s01.a"], C["s01.b"], C["s01.c"]

    def um():
        fcen(c, t, ka, "45 × 10^3", W / 2, 370, 190)
        E.foco(c, t, kb, 0.5, lambda a: (centro(c, "= 45.000", W / 2 - 40, 560, 120, "g", CERTO, a), E.selo(c, 1300, 520, 58, True, a)))
        E.foco(c, t, kc, 0.5, lambda a: E.selo(c, 1520, 310, 70, False, a))
        E.frase(c, t, kc, ps("não está na", "i", 92) + ps("forma correta", "g", 92, ERRADO), W / 2, 760, "center", 0.14)
        E.frase(c, t, lerp(kc, C["s01.end"], 0.42), ps("e uma prova pode cobrar exatamente isso", "i", 76), W / 2, 890, "center", 0.11)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t >= C["s02"]:
        ta, tb = C["s02.a"], C["s02.b"]
        E.foco(c, t, tb - 0.2, 0.7, lambda a: E.bola(c, 1490, 540, 250 * ease_back(prog(t, tb - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, ps("até o fim desta aula", "i", 90), XE, 300, passo=0.14)
        E.frase(c, t, lerp(ta, tb, 0.28), ps("números", "i", 90) + [("enormes", "g", 150, COR)], XE, 470)
        E.frase(c, t, lerp(ta, tb, 0.42), ps("e números", "i", 90) + [("minúsculos", "g", 64, COR)], XE, 610, passo=0.12)
        E.frase(c, t, lerp(ta, tb, 0.6), ps("em uma", "i", 90) + [("linha curta", "g", 100)], XE, 770, passo=0.14)
        E.foco(c, t, tb + 0.2, 0.5, lambda a: (centro(c, "+ atalho", 1490, 525, 80, "g", E.SOBRE, a),
                                               centro(c, "de prova", 1490, 610, 80, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"] + 0.3, ps("você só precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "2", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 240, 700, 120, "i", TINTA, a))
    x, w = 960, 780
    itens = (("s03.b", "ler números", "grandes"), ("s03.c", "conhecer as", "potências de 10"))
    for i, (k, l1, l2) in enumerate(itens):
        y = 200 + i * 260
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 196, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 62)], x + 44, y + 84)
        E.frase(c, t, C[k] + 0.3, [(l2, "g", 62, COR)], x + 44, y + 160)
    E.frase(c, t, lerp(C["s03.c"], C["s03.end"], 0.42), ps("inclusive com expoente negativo", "i", 56), x + 44, 720, passo=0.1)
    py = lerp(370, 630, ease_io(prog(t, C["s03.c"] - 0.35, 0.5)))
    E.cursor(c, x + w - 30, py, ep(t, C["s03.b"], 0.4))
    E.frase(c, t, lerp(C["s03.c"], C["s03.end"], 0.78), ps("faltou alguma?", "i", 62, COR) + ps("procure no canal", "i", 62), 960, 880, "left", 0.12)


# ---------------- por que existe ----------------
def b_porque(c, t, C, b):
    ka, kb, kc = C["s04.a"], C["s04.b"], C["s04.c"]
    s, y, cx = 190, 560, W / 2
    n = "45.000.000"
    zeros = {i: COR for i, ch in enumerate(n) if ch == "0"}
    tperde = lerp(kb, kc, 0.2)
    ttroca = lerp(kb, kc, 0.5)

    def topo():
        E.frase(c, t, ka - 0.1, ps("uma fábrica produziu", "i", 84), W / 2, 130, "center", 0.12)
        E.frase(c, t, ka + 0.2, [("45 milhões", "g", 120, COR)] + ps("de parafusos", "i", 110), W / 2, 270, "center", 0.2)
    E.saida(c, t, ttroca - 0.1, topo)
    for i in range(78):
        px, py = 150 + (i % 26) * 66, 440 + (i // 26) * 130
        if t < kb + 0.4:
            E.saida(c, t, kb, lambda i=i, px=px, py=py: E.foco(c, t, ka + 0.2 + i * 0.03, 0.3, lambda a: parafuso(c, px, py, 1.0, E.COR, a), sobe=-30))

    def numero():
        if t < tperde:
            E.foco(c, t, kb - 0.05, 0.5, lambda a: num_m(c, n, cx, y, s, TINTA, a, zeros))
        else:
            q = ep(t, tperde, 0.6)
            xs = num_m(c, n, cx, y, s, a=0)
            num_m(c, "45.000.00", cx, y, s, ERRADO)
            if q < 1:
                E.escreve(c, "0", xs(9), y + 260 * q * q, s, "g", ERRADO, 1 - q)
            E.frase(c, t, tperde + 0.25, ps("basta perder um para", "i", 76) + [("errar feio", "g", 76, ERRADO)], W / 2, y + 170, "center", 0.11)
        if kb <= t < tperde + 0.4:
            xs = num_m(c, n, cx, y, s, a=0)
            E.saida(c, t, tperde, lambda: (E.chave(c, xs(3), xs(10) - 8, y + 34, COR, ep(t, kb, 0.4), 24, 6),
                                           cen(c, t, kb + 0.1, "seis zeros", (xs(3) + xs(10)) / 2, y + 150, 80, COR)))
    E.saida(c, t, ttroca - 0.1, numero)
    E.frase(c, t, ttroca, ps("trocar os zeros por uma", "i", 90) + [("potência de 10", "g", 90, COR)], W / 2, 420, "center", 0.12)
    E.foco(c, t, kc, 0.5, lambda a: E.pilula(c, "notação científica", W / 2, 640, 120, "g", a=a, cor=E.SOBRE))


# ---------------- a forma ----------------
def b_forma(c, t, C, b):
    ka, kb, kc, kd = C["s05.a"], C["s05.b"], C["s05.c"], C["s05.d"]
    tf = lerp(kc, kd, 0.42)

    def forma():
        E.frase(c, t, ka, ps("a forma tem", "i", 84) + [("duas partes", "g", 84, COR)], W / 2, 170, "center", 0.14)
        y = 500
        p = ep(t, kb, 0.5)
        E.caixa_pontilhada(c, 340, y - 170, 500, 220, p, COR, prog_=p)
        cen(c, t, kb + 0.1, "número", 590, y - 30, 96, COR)
        E.foco(c, t, tf, 0.5, lambda a: E.pilula(c, "frente", 590, y - 230, 60, "i", a=a, cor=E.SOBRE))
        fcen(c, t, kc, "× 10^{?}", 1250, y, 170)
        cen(c, t, kc + 0.2, "potência de dez", 1250, y + 110, 70, TINTA, "i")
        E.frase(c, t, kd, ps("de", "i", 96) + [("1", "g", 120, COR)] + ps("até menos de", "i", 96) + [("10", "g", 120, COR)], W / 2, 870, "center", 0.16)
    E.saida(c, t, C["s06"] - 0.1, forma)
    if t < C["s06"]:
        return
    a6, b6, c6, d6, e6 = C["s06.a"], C["s06.b"], C["s06.c"], C["s06.d"], C["s06.e"]
    E.frase(c, t, C["s06"] + 0.1, ps("a frente vale?", "i", 84), W / 2, 180, "center", 0.14)
    for (s, ok, cx, k) in (("1", True, 340, a6), ("9,9", True, 760, b6), ("10", False, 1180, c6), ("0,5", False, 1600, d6)):
        cor = CERTO if ok else ERRADO
        E.foco(c, t, k, 0.5, lambda a, s=s, cx=cx, cor=cor, ok=ok: (centro(c, s, cx, 450, 170, "g", cor, a), E.selo(c, cx, 570, 56, ok, a)))
    E.frase(c, t, e6, ps("um único", "i", 84) + [("algarismo", "g", 84, COR)] + ps("antes da vírgula", "i", 84), W / 2, 790, "center", 0.14)
    E.frase(c, t, lerp(e6, C["s06.end"], 0.62), ps("e ele", "i", 84) + [("não pode ser zero", "g", 84, ERRADO)], W / 2, 920, "center", 0.14)


# ---------------- número grande ----------------
def b_grande(c, t, C, b):
    ka, kb, kc, kd = C["s07.a"], C["s07.b"], C["s07.c"], C["s07.d"]
    s, y = 170, 520
    cl = E.casa(s)
    x = W / 2 - 4 * cl
    w0, w1 = lerp(kb, kc, 0.3), lerp(kb, kc, 0.98)

    def legenda(t0, t1, partes):
        if t0 <= t:
            E.saida(c, t, t1 - 0.1, lambda: E.frase(c, t, t0, partes, W / 2, 270, "center", 0.11))

    def tela():
        E.frase(c, t, C["s07"] + 0.1, ps("quarenta e cinco milhões", "i", 80), W / 2, 150, "center", 0.11)
        legenda(kb, w0, ps("uma", "i", 80) + [("vírgula escondida", "g", 76, COR)] + ps("no fim", "i", 80))
        legenda(w0, kc, ps("ande para a", "i", 80) + [("esquerda", "g", 76, COR)] + ps("até sobrar um algarismo", "i", 80))
        marca = lambda a=1.0: (E.chave(c, x + cl + 8, x + 8 * cl - 8, y + 96, COR, a, 22, 6),
                               centro(c, "7 casas", x + 4.5 * cl, y + 210, 90, "g", COR, a))
        if t < kd:
            E.foco(c, t, ka, 0.5, lambda a: anda_passos(c, t, "45000000", 8, 1, w0, w1, x, y, s, tv=kb))
            casas_contadas(c, t, w0, w1, [7, 6, 5, 4, 3, 2, 1], x, y, s)
            E.foco(c, t, kc, 0.4, marca)
        else:
            xq = lerp(x, W / 2 - cl, ease_io(prog(t, kd + 0.2, 0.6)))
            E.anda(c, t, "45", 1, [], xq, y, s, cor=COR)
            some_digitos(c, t, kd, "45000000", range(2, 8), x, y, s)
            E.saida(c, t, kd, marca)
            cen(c, t, kd + 0.3, "fica", W / 2, y + 170, 100, TINTA, "i")
    E.saida(c, t, C["s08"] - 0.1, tela)
    if t < C["s08"]:
        return
    a8, b8, c8 = C["s08.a"], C["s08.b"], C["s08.c"]
    fcen(c, t, C["s08"] + 0.2, "4,5 ≠ 45.000.000", W / 2, 240, 120)
    for cx, k, rot, s_, fundo in ((540, a8, "andar 7 casas dividiu por", "÷ 10^7", TINTA), (1380, b8, "para o valor não mudar", "× 10^7", None)):
        cen(c, t, k, rot, cx, 410, 66, TINTA, "i")
        E.foco(c, t, k + 0.1, 0.5, lambda a, cx=cx, s_=s_, fundo=fundo: pil_f(c, s_, cx, 540, 110, fundo, a=a))
    E.cientifica(c, t, c8, "4,5", 7, W / 2, 860, 190, cor=COR, align="center")


# ---------------- número pequeno ----------------
def b_pequeno(c, t, C, b):
    ka, kb, kc = C["s09.a"], C["s09.b"], C["s09.c"]
    s, y = 170, 540
    cl = E.casa(s)
    x = W / 2 - 3 * cl
    w0, w1 = lerp(ka, kb, 0.45), lerp(ka, kb, 0.98)
    dig = "000032"

    def tela():
        E.frase(c, t, C["s09"] + 0.1, ps("número pequeno:", "i", 84) + [("o caminho de volta", "g", 76, COR)], W / 2, 150, "center", 0.12)
        E.saida(c, t, kc - 0.2, lambda: (E.frase(c, t, lerp(ka, kb, 0.33), ps("a vírgula anda para a", "i", 76) + [("direita", "g", 72, COR)], W / 2, 270, "center", 0.11),
                                         E.frase(c, t, lerp(ka, kb, 0.6), ps("até passar do primeiro algarismo que não é zero", "i", 68), W / 2, 370, "center", 0.08)))
        marca = lambda a=1.0: (E.chave(c, x + cl + 8, x + 5 * cl - 8, y + 96, COR, a, 22, 6),
                               centro(c, "4 casas", x + 3 * cl, y + 210, 90, "g", COR, a))
        if t < kc:
            E.foco(c, t, ka, 0.5, lambda a: anda_passos(c, t, dig, 1, 5, w0, w1, x, y, s))
            casas_contadas(c, t, w0, w1, [1, 2, 3, 4], x, y, s)
            E.foco(c, t, kb, 0.4, marca)
        else:
            xq = lerp(x + 4 * cl, W / 2 - cl, ease_io(prog(t, kc + 0.2, 0.6)))
            E.anda(c, t, "32", 1, [], xq, y, s, cor=COR)
            some_digitos(c, t, kc, dig, range(0, 4), x, y, s)
            E.saida(c, t, kc, marca)
            cen(c, t, kc + 0.3, "fica", W / 2, y + 170, 100, TINTA, "i")
    E.saida(c, t, C["s10"] - 0.1, tela)
    if t < C["s10"]:
        return
    a0, b0, c0, d0 = C["s10.a"], C["s10.b"], C["s10.c"], C["s10.d"]
    for cx, k, rot, s_, fundo in ((400, a0, "andar multiplicou por", "× 10.000", TINTA), (960, b0, "para desfazer", "÷ 10.000", None), (1500, c0, "é o mesmo que", "× 10^{−4}", None)):
        cen(c, t, k, rot, cx, 310, 62, TINTA, "i")
        E.foco(c, t, k + 0.1, 0.5, lambda a, cx=cx, s_=s_, fundo=fundo: pil_f(c, s_, cx, 450, 84, fundo, a=a))
    E.sinal(c, t, c0, "=", 1235, 450, 90)
    E.cientifica(c, t, d0, "3,2", -4, W / 2, 810, 190, cor=COR, align="center")


# ---------------- regra ----------------
def b_regra(c, t, C, b):
    E.frase(c, t, C["s11"] + 0.1, ps("a regra cabe em", "i", 80) + [("três linhas", "g", 76, COR)], XE, 150, "left", 0.14)
    passo(c, t, C["s11.a"], 1, "a vírgula andou para a esquerda", "expoente positivo", 320)
    passo(c, t, C["s11.b"], 2, "andou para a direita", "expoente negativo", 570)
    passo(c, t, C["s11.c"], 3, "quantas casas andou", "esse é o tamanho do expoente", 820)
    for k, y, x0, x1 in (("s11.a", 320, 1690, 1450), ("s11.b", 570, 1450, 1690)):
        if t >= C[k]:
            q = ep(t, C[k], 0.6)
            M.arrow(c, x0, y, x1, y, COR, q, 12, 34, q)


# ---------------- corrigir a forma ----------------
def b_corrigir(c, t, C, b):
    ka, kb, kc = C["s12.a"], C["s12.b"], C["s12.c"]
    a3, b3, c3, d3, e3 = C["s13.a"], C["s13.b"], C["s13.c"], C["s13.d"], C["s13.e"]
    s, y = 170, 320
    cl = E.casa(s)
    x = 500
    xf = x + 2 * cl + 44
    wf = E.formula(c, "× 10", 0, 0, s, a=0)

    def conta():
        cor = ERRADO if kb <= t < kc + 0.7 else TINTA
        E.foco(c, t, ka, 0.5, lambda a: E.anda(c, t, "45", 2, [(kc, 1)], x, y, s, cor=cor, tv=kc - 0.3))
        E.foco(c, t, ka, 0.5, lambda a: E.formula(c, "× 10", xf, y, s, a=a))
        xe = xf + wf
        E.foco(c, t, ka, 0.5, lambda a: E.formula(c, "^3", xe, y, s, a=a))
        E.corta(c, t, c3, xe + 30, y - 106, 76)
        E.foco(c, t, c3 + 0.3, 0.4, lambda a: E.formula(c, "^4", xe + 66, y, s, cor=COR, a=a))
    E.saida(c, t, d3 - 0.1, conta)
    E.saida(c, t, kc - 0.1, lambda: E.frase(c, t, C["s12"] + 0.1, ps("voltemos ao começo", "i", 72), W / 2, 130, "center", 0.12))
    E.saida(c, t, a3 - 0.1, lambda: (E.frase(c, t, kb, [("45", "g", 96, ERRADO)] + ps("passa de", "i", 96) + [("10", "g", 96, ERRADO)], W / 2, 520, "center", 0.15),
                                     E.frase(c, t, kc, ps("uma casa para a", "i", 80) + [("esquerda:", "g", 76, COR), ("4,5", "g", 90, COR)], W / 2, 680, "center", 0.12)))
    if a3 - 0.1 <= t:
        ang = 9 * ep(t, a3, 0.5) * (1 - ease_io(prog(t, b3, 0.8)))

        def rot(s_, k):
            def fn(px, py):
                E.foco(c, t, k, 0.4, lambda a: pil_f(c, s_, px, py, 76, a=a))
            return fn

        def bal():
            E.foco(c, t, a3, 0.5, lambda a: balanca(c, W / 2, 520, 860, ang, rot("÷ 10", a3), rot("× 10", b3), a))
            E.frase(c, t, a3, ps("frente", "i", 70) + [("10 vezes menor", "g", 64, COR)], 500, 900, "center", 0.12)
            E.frase(c, t, b3, ps("potência", "i", 70) + [("10 vezes maior", "g", 64, COR)], 1420, 900, "center", 0.12)
        E.saida(c, t, d3 - 0.1, bal)
    E.cientifica(c, t, d3, "4,5", 4, W / 2, 470, 190, cor=COR, align="center")
    E.foco(c, t, e3, 0.5, lambda a: (centro(c, "mesmo valor", W / 2, 690, 84, "i", TINTA, a),
                                     centro(c, "45.000", W / 2 - 60, 860, 140, "g", TINTA, a), E.selo(c, W / 2 + 310, 815, 66, True, a)))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    ka, kb, kc = C["s14.a"], C["s14.b"], C["s14.c"]
    a5, b5 = C["s15.a"], C["s15.b"]
    s, y = 160, 430
    n = "45.000.000"

    def um():
        E.frase(c, t, C["s14"] + 0.1, ps("o erro mais comum:", "i", 80), W / 2, 150, "center", 0.12)
        E.frase(c, t, ka, [("contar os zeros", "g", 110, ERRADO)], W / 2, 280, "center")
        zeros = {i: ERRADO for i, ch in enumerate(n) if ch == "0"}
        E.foco(c, t, kb, 0.5, lambda a: num_m(c, n, W / 2, y + 60, s, TINTA, a, zeros))
        xs = num_m(c, n, W / 2, y + 60, s, a=0)
        if t >= kb:
            E.chave(c, xs(3), xs(10) - 8, y + 90, ERRADO, ep(t, kb, 0.4), 22, 6)
        cen(c, t, kb + 0.2, "6 zeros", (xs(3) + xs(10)) / 2, y + 190, 66, ERRADO)
        E.cientifica(c, t, kc, "4,5", 6, W / 2 - 60, 900, 150, cor=ERRADO, align="center")
        E.foco(c, t, kc + 0.3, 0.5, lambda a: E.selo(c, 1520, 845, 64, False, a))
    E.saida(c, t, C["s15"] - 0.1, um)
    if t < C["s15"]:
        return

    def dois():
        E.cientifica(c, t, C["s15"] + 0.1, "4,5", 6, W / 2, 300, 150, cor=ERRADO, align="center")
        fcen(c, t, a5, "= 4.500.000", W / 2, 500, 130, ERRADO)
        E.frase(c, t, lerp(a5, b5, 0.6), [("dez vezes menos!", "g", 110, ERRADO)], W / 2, 700, "center")
    E.saida(c, t, b5 - 0.1, dois)
    if t >= b5:
        s2, yn = 150, 620
        cl = E.casa(s2)
        x = W / 2 - 4 * cl
        E.frase(c, t, b5, ps("quem manda é a", "i", 100) + [("vírgula", "g", 100, COR)], W / 2, 210, "center", 0.14)
        E.frase(c, t, b5 + 0.6, ps("não o zero", "i", 100), W / 2, 340, "center", 0.14)
        tp = lerp(b5, C["s15.end"], 0.42)
        E.foco(c, t, tp, 0.5, lambda a: E.anda(c, t, "45000000", 1, [], x, yn, s2))
        tf = lerp(b5, C["s15.end"], 0.72)
        q = ep(t, tp + 0.2, 0.4)
        E.caixa_pontilhada(c, x + cl + 2, yn - s2 * 0.92, cl - 4, s2 * 1.08, q, COR, prog_=q)
        for k in range(1, 8):
            cen(c, t, lerp(tp, tf, (k - 1) / 7), str(8 - k), x + (k + 0.5) * cl, yn + 84, 56, COR if k == 1 else TINTA2, "b")
        E.frase(c, t, tf, ps("essa casa", "i", 80) + [("entra na conta", "g", 76, COR)], W / 2, 880, "center", 0.12)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    ka, kb, kc = C["s16.a"], C["s16.b"], C["s16.c"]
    s, y = 170, 560
    cl = E.casa(s)
    x = W / 2 - 4 * cl
    px = lambda i: x + (i + 0.5) * cl

    def um():
        E.frase(c, t, C["s16"] + 0.1, ps("agora, o atalho", "i", 80, CLARO) + [("para número grande", "b", 62, BR)], W / 2, 170, "center", 0.11)
        E.frase(c, t, ka, ps("conte quantos algarismos vêm", "i", 76, CLARO) + [("depois do primeiro", "g", 72, BR)], W / 2, 290, "center", 0.1)
        for i, ch in enumerate("45000000"):
            cor = CLARO if t >= kc and i == 0 else BR
            E.foco(c, t, kb + i * 0.08, 0.35, lambda a, i=i, ch=ch, cor=cor: E._digito(c, ch, px(i), y, s, "g", cor, a))
        E.saida(c, t, kc, lambda: cen(c, t, kb + 0.6, "8 algarismos", W / 2, y + 170, 80, CLARO))
        E.foco(c, t, kc, 0.4, lambda a: (E.chave(c, px(1) - cl * 0.4, px(7) + cl * 0.4, y + 40, CLARO, a, 24, 6),
                                         centro(c, "sobram 7", W / 2 - 170, y + 180, 96, "g", BR, a)))
        fcen(c, t, lerp(kc, C["s16.end"], 0.5), "10^7", W / 2 + 220, y + 200, 140, CLARO)
        E.frase(c, t, lerp(kc, C["s16.end"], 0.72), ps("sem andar casa por casa", "i", 72, CLARO), W / 2, y + 340, "center", 0.11)
    E.saida(c, t, C["s17"] - 0.1, um)
    if t < C["s17"]:
        return
    a7, b7 = C["s17.a"], C["s17.b"]
    t0, t1 = a7 + 0.2, lerp(a7, b7, 0.92)
    E.frase(c, t, a7, ps("a vírgula", "i", 76, CLARO) + [("passa", "g", 72, BR)] + ps("por cada algarismo depois do primeiro", "i", 76, CLARO), W / 2, 200, "center", 0.09)
    E.foco(c, t, C["s17"] + 0.1, 0.5, lambda a: anda_passos(c, t, "45000000", 8, 1, t0, t1, x, 430, s, cor=BR, cor_v=CLARO))
    E.foco(c, t, b7, 0.5, lambda a: E.selo(c, 280, 690, 66, False, a))
    E.frase(c, t, b7 + 0.1, ps("não compensa se o número já vem", "i", 72, CLARO), 380, 670, "left", 0.1)
    E.frase(c, t, lerp(b7, C["s17.end"], 0.3), [("com vírgula ou com potência", "g", 68, BR)], 380, 760)
    E.frase(c, t, lerp(b7, C["s17.end"], 0.7), ps("aí,", "i", 80, CLARO) + [("ande a vírgula e compense", "g", 72, BR)], W / 2, 910, "center", 0.11)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s18"] + 0.1, ps("hora de testar", "i", 72, COR), XE, 160, passo=0.12)
    ka, kb, kc = C["s18.a"], C["s18.b"], C["s18.c"]
    E.frase(c, t, ka - 0.5, ps("o Brasil tem cerca de", "i", 76), XE, 300, passo=0.1)
    E.frase(c, t, ka + 0.2, [("214 milhões", "g", 96, COR)] + ps("de habitantes", "i", 76), XE, 410, passo=0.12)
    E.frase(c, t, kb - 0.9, ps("um glóbulo vermelho mede cerca de", "i", 76), XE, 560, passo=0.09)
    E.frase(c, t, kb + 0.2, [("0,000008", "g", 96, COR)] + ps("metro", "i", 76), XE, 670, passo=0.12)
    E.frase(c, t, kc, ps("escreva cada valor em", "i", 92) + [("notação científica", "g", 92, COR)], W / 2 + 40, 880, "center", 0.11)
    E.relogio(c, t, C["s19.a"], 1520, 330, 170)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    ka, kb, kc = C["s20.a"], C["s20.b"], C["s20.c"]
    a1, b1 = C["s21.a"], C["s21.b"]
    E.foco(c, t, ka, 0.5, lambda a: num_m(c, "214.000.000", 620, 190, 110, TINTA, a))
    cen(c, t, ka + 0.3, "9 algarismos", 1340, 180, 72, TINTA, "i")
    cen(c, t, kb, "sobram 8", 1340, 268, 76, COR)
    E.cientifica(c, t, kc, "2,14", 8, W / 2, 450, 150, cor=COR, align="center")
    s, y = 120, 690
    cl = E.casa(s)
    x = W / 2 - 3.5 * cl - 130
    w0, w1 = C["s21"] + 0.4, a1 - 0.05
    if C["s21"] - 0.1 <= t:
        if t < b1:
            E.foco(c, t, C["s21"], 0.5, lambda a: anda_passos(c, t, "0000008", 1, 7, w0, w1, x, y, s))
            casas_contadas(c, t, w0, w1, [1, 2, 3, 4, 5, 6], x, y - 8, s)
        else:
            some_digitos(c, t, b1, "0000008", range(0, 6), x, y, s)
            E._digito(c, "8", x + 6.5 * cl, y, s, "g", COR, 1.0)
    cen(c, t, a1, "6 casas", 1540, y - 50, 84, COR)
    E.frase(c, t, a1 + 0.5, ps("direita:", "i", 60) + [("negativo", "g", 60, COR)], 1540, y + 40, "center", 0.1)
    E.cientifica(c, t, b1, "8", -6, W / 2 - 80, 930, 150, cor=COR, align="center")
    E.frase(c, t, b1 + 0.9, ps("metro", "i", 90), W / 2 + 270, 930, "left")


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s22"], [("resumindo", "i", 92, COR)], W / 2, 210, "center")
        for i, (k, s) in enumerate((("s22.a", "um número de 1 até menos de 10"), ("s22.b", "vezes uma potência de 10"), ("s22.c", "o expoente conta as casas da vírgula"))):
            y = 390 + i * 190
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 260, y - 30, 56, a=a),
                                                         E.centro(c, str(i + 1), 260, y - 7, 64, "g", E.SOBRE, a)))
            E.frase(c, t, C[k] + 0.1, [(s, "g", 76)], 350, y)
    E.saida(c, t, C["s23"] - 0.1, resumo)
    if t < C["s23"]:
        return
    E.frase(c, t, C["s23"] + 0.1, ps("na próxima aula", "i", 84), XE, 250, passo=0.14)
    E.frase(c, t, C["s23.a"], [("contas", "g", 130, COR)] + ps("em notação científica", "i", 110), XE, 400, passo=0.14)
    E.frase(c, t, C["s23.b"], ps("quantas vezes a massa da", "i", 76) + [("Terra", "g", 76, COR)] + ps("é maior que a da", "i", 76) + [("Lua", "g", 76, COR)], XE, 540, passo=0.08)
    E.foco(c, t, C["s23.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1440, 700, 76, estilo="g", a=a, cor=E.SOBRE))
    p = ease_io(prog(t, C["s23.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1770, 1570, p), lerp(960, 725, p), ep(t, C["s23.c"] + 0.2, 0.4))
    E.frase(c, t, C["s23.d"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 900, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, porque=b_porque, forma=b_forma, grande=b_grande, pequeno=b_pequeno, regra=b_regra,
              corrigir=b_corrigir, erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
