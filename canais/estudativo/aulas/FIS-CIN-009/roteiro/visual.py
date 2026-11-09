"""Visual — Estudativo · FIS-CIN-009: Torricelli e distância de frenagem.

Segue a LINGUAGEM VISUAL DA FÍSICA do cabeçalho de FIS-CIN-001 (peças em _ferramentas/fisica.py, importado como F).
Nesta aula: a distância de parada é uma faixa sob o carro (faixa()), cinza-tinta na REAÇÃO (velocidade constante) e laranja
na FRENAGEM, na escala da cena; a velocidade em petróleo (F.VEL) e a aceleração em violeta (F.ACEL). A fórmula nova entra com
F.formula_legenda. O "×4" da frenagem é mostrado com o quadrado que dobra de lado (quadrados()), como em MAT-RAZ-010.
Todo instante vem de C[...] (marcadores do roteiro)."""
import math

import editorial as E
import fisica as F
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Física", "Cinemática")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_FIS-CIN-009_torricelli_e_distancia_de_frenagem.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("torricelli", "frenagem", "reacao", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"

fren = lambda v, a: v * v / (2 * a)
# todas as contas da aula
assert fren(10, 5) == 10 and fren(20, 5) == 40 and fren(30, 5) == 90
assert 10 ** 2 + 2 * 2 * 24 == 100 + 96 == 196 and math.isqrt(196) == 14
assert 20 ** 2 == 400 and 400 / 10 == 40 and 20 * 1 + 40 == 60
a_q = 15 ** 2 / (2 * 15)
assert a_q == 7.5 and fren(30, a_q) == 60 == 4 * 15 and 15 * 1 + 15 == 30 and 30 * 1 + 60 == 90 and 90 / 30 == 3


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças gerais (copiadas entre as aulas FIS-CIN) ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def bola_txt(c, t, t0, s, cx, cy, r, size, cor=None):
    """resposta na esfera: "20 m/s" com a unidade menor"""
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


def lembrete(c, t, C, cena, itens, desenhos=None):
    """'você precisa de N coisas': itens = [(cue, linha fina, linha forte)]; desenhos[i](a, x, y) à direita de cada caixa"""
    n = len(itens)
    E.frase(c, t, C[cena] + 0.2, ps("você precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C[cena + ".a"], 0.5, lambda a: E.escreve(c, str(n), XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C[cena + ".a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 820, 1000
    h, gap, s1 = (230, 290, 58) if n == 2 else (196, 236, 52)
    y0 = 520 - (h + gap * (n - 1)) / 2
    for i, (k, l1, l2) in enumerate(itens):
        y = y0 + i * gap
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, h, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", s1)], x + 44, y + h * 0.4)
        E.frase(c, t, C[k] + 0.3, [(l2, "g", s1, COR)], x + 44, y + h * 0.74)
        if desenhos:
            E.foco(c, t, C[k] + 0.6, 0.5, lambda a, i=i, y=y: desenhos[i](a, x + w - 150, y + h / 2))
    ult = itens[-1][0]
    E.frase(c, t, lerp(C[ult], C[cena + ".end"], 0.6), ps("faltou alguma?", "i", 56, COR) + ps("procure no canal", "i", 56), 820, 990, "left", 0.12)


def promessa(c, t, C, cena, itens, titulo="até o fim da aula"):
    """gancho: a órbita à direita e a lista numerada; itens = [(cue, texto, atraso)]"""
    tb = C[cena + ".a"] + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1480, 540, 330 * ease_back(prog(t, tb, 0.8)), giro=12 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, C[cena + ".a"], ps(titulo, "i", 88), XE, 280, passo=0.14)
    for i, (k, s, dt) in enumerate(itens):
        y = 450 + i * 160
        E.foco(c, t, C[k] + dt, 0.5, lambda a, i=i, y=y: (E.bola(c, XE + 40, y - 30, 38, a=a),
                                                        centro(c, str(i + 1), XE + 40, y - 8, 48, "g", BR, a)))
        E.frase(c, t, C[k] + dt + 0.1, [(s, "g", 80, COR if i == 0 else TINTA)], XE + 110, y)


def fim_inscreva(c, t, C, cena, k_insc, k_bons):
    E.foco(c, t, C[k_insc], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 420, 76, estilo="g", a=a))
    p = ease_io(prog(t, C[k_insc] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(720, 445, p), ep(t, C[k_insc] + 0.2, 0.4))
    E.frase(c, t, C[k_bons], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1570, 990, "center")


def resumo(c, t, C, cena, itens):
    """resumo numerado: itens = [(cue, partes de E.frase)]"""
    E.frase(c, t, C[cena], [("resumindo", "i", 92, COR)], W / 2, 180, "center")
    for i, (k, partes) in enumerate(itens):
        y = 360 + i * 190
        E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 300, y - 26, 52, a=a), centro(c, str(i + 1), 300, y - 4, 60, "g", BR, a)))
        E.frase(c, t, C[k] + 0.1, partes, 400, y, passo=0.12)


# ---------------- peças desta aula ----------------
def conta(c, t, linhas, x, y0, size=90, dy=None, cor=TINTA):
    """linhas de conta, uma por instante: linhas = [(instante, texto[, cor])]"""
    dy = dy or size * 1.35
    for i, l in enumerate(linhas):
        E.formula_em(c, t, l[0], l[1], x, y0 + i * dy, size, "g", l[2] if len(l) > 2 else cor)


def faixa(c, t, t0, x0, x1, y, cor, rot=None, d=0.7, h=34, size=46, cor_rot=None):
    """faixa de distância de x0 a x1 que cresce a partir de t0, com o rótulo embaixo"""
    q = ease_io(prog(t, t0, d))
    if q <= 0:
        return
    M.rrect(c, x0, y, (x1 - x0) * q, h, h / 2, cor, 0.9)
    if rot and q > 0.9:
        a = ep(t, t0 + d * 0.9, 0.3)
        v, _, u = rot.partition(" ")
        F.medida(c, v, u, (x0 + x1) / 2, y + h + size + 6, size, cor_rot or cor, a, "center")


def quadrados(c, t, t0, x, y, l, a_=1.0):
    """um quadrado de lado l e, ao lado, o de lado 2l dividido em 4"""
    E.foco(c, t, t0, 0.5, lambda a: M.rrect(c, x, y - l, l, l, 6, E.COR, 0.85 * a))
    def grande(a):
        x2 = x + l + 60
        M.rrect(c, x2, y - 2 * l, 2 * l, 2 * l, 6, E.COR, 0.85 * a)
        M.line(c, x2 + l, y - 2 * l, x2 + l, y, BR, a, 4)
        M.line(c, x2, y - l, x2 + 2 * l, y - l, BR, a, 4)
    E.foco(c, t, t0 + 0.6, 0.5, grande)


# ---------------- gancho ----------------
K = 30  # pixels por metro


def b_gancho(c, t, C, b):
    def um():
        x0 = 330
        y1, y2 = 400, 860
        for y in (y1, y2):
            if t >= C["s01.a"]:
                M.line(c, 120, y, 1840, y, TINTA, ep(t, C["s01.a"], 0.4), 5)
        q1 = ease_out(prog(t, C["s01.c"], 1.2))
        E.foco(c, t, C["s01.a"], 0.4, lambda a: F.carrinho(c, x0 + 10 * K * q1, y1, 180, a=a))
        E.foco(c, t, C["s01.b"], 0.4, lambda a: F.medida(c, 10, "m/s", 190, y1 - 150, 60, F.VEL, a))
        faixa(c, t, C["s01.c"], x0, x0 + 10 * K, y1 + 20, E.COR, "10 m", 1.2)
        E.foco(c, t, C["s01.d"], 0.4, lambda a: F.carrinho(c, x0, y2, 180, a=a) if t < C["s01.f"] else None)
        E.foco(c, t, C["s01.d"] + 0.3, 0.4, lambda a: F.medida(c, 20, "m/s", 190, y2 - 150, 60, F.VEL, a))
        if C["s01.e"] <= t < C["s01.f"]:
            faixa(c, t, C["s01.e"], x0, x0 + 20 * K, y2 + 20, ERRADO, "20 m?", 0.6)
        if t >= C["s01.f"]:
            q2 = ease_out(prog(t, C["s01.f"], 1.6))
            F.carrinho(c, x0 + 40 * K * q2, y2, 180)
            faixa(c, t, C["s01.f"], x0, x0 + 40 * K, y2 + 20, E.COR, "40 m", 1.6)
            pilula_em(c, t, C["s01.f"] + 1.6, "4 vezes", 1500, y2 - 230, 60, E.COR)
        E.frase(c, t, C["s01.d"] - 0.6, ps("o dobro da velocidade, a mesma freada:", "i", 58, TINTA2), XE, 620, passo=0.08)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t >= C["s02"]:
        promessa(c, t, C, "s02", (("s02.b", "sem saber o tempo", 0), ("s02.c", "a distância de parada", 0)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    lembrete(c, t, C, "s03", (("s03.b", "funções do MUV:", "a da velocidade e a da posição"), ("s03.c", "dobrou o lado:", "a área fica 4 vezes maior"),
                              ("s03.d", "raiz quadrada:", "√196 = 14")))


# ---------------- Torricelli ----------------
def b_torricelli(c, t, C, b):
    def s04_05():
        for i, f_ in enumerate(("v = v₀ + a · t", "s = s₀ + v₀ · t + f{a · t^2}{2}")):
            y = 260 + i * 150
            E.foco(c, t, C["s04"] + 0.3 + 0.4 * i, 0.5, lambda a, f_=f_, y=y: E.formula(c, f_, 1300, y, 72, "g", TINTA2, a, "center"))
        E.frase(c, t, C["s04.a"], ps("o", "i", 70) + [("t", "g", 70, ERRADO)] + ps("aparece em todas", "i", 70), XE, 280, passo=0.12)
        E.frase(c, t, C["s04.b"], ps("e quando não há tempo?", "i", 64, TINTA2), XE, 400, passo=0.1)
        E.frase(c, t, C["s04.c"], [("Torricelli", "g", 110, COR)], XE, 560)
        F.formula_legenda(c, t, C["s04.d"], "v^2 = v₀^2 + 2 · a · Δs",
                          [("v", "velocidade final", "m/s"), ("v₀", "velocidade inicial", "m/s"), ("a", "aceleração", "m/s^2"), ("Δs", "deslocamento", "m")],
                          XE, 690, 100, tl=[C["s05.a"], C["s05.b"], C["s05.c"], C["s05.d"]], size_l=44, dy=54)
        E.frase(c, t, C["s05.e"], ps("sai das duas, tirando o t", "i", 56, TINTA2), 1080, 870, "left", 0.1)
        pilula_em(c, t, C["s05.f"], "sem tempo? Torricelli", 1440, 990, 52, E.COR)
    E.saida(c, t, C["s06"] - 0.1, s04_05)
    if t < C["s06"]:
        return
    E.frase(c, t, C["s06.a"], [("v₀", "g", 66, F.VEL), ("=", "g", 66, TINTA2), ("10", "g", 66), ("m/s", "b", 50, F.UNID)], XE, 220, passo=0.1)
    E.frase(c, t, C["s06.b"], [("a", "g", 66, F.ACEL), ("=", "g", 66, TINTA2), ("2", "g", 66), ("m/s²", "b", 50, F.UNID)], XE + 450, 220, passo=0.1)
    E.frase(c, t, C["s06.c"], [("Δs", "g", 66, COR), ("=", "g", 66, TINTA2), ("24", "g", 66), ("m", "b", 50, F.UNID)], XE + 900, 220, passo=0.1)
    E.formula_em(c, t, C["s06.d"], "v^2 = 10^2 + 2 · 2 · 24", XE, 430, 90, "g", TINTA)
    E.formula_em(c, t, C["s06.e"], "= 100 + 96", XE + 120, 580, 90, "g", TINTA)
    E.formula_em(c, t, C["s06.f"], "= 196", XE + 120, 730, 90, "g", TINTA)
    E.formula_em(c, t, C["s06.g"], "v = r{196}", XE, 900, 90, "g", COR)
    bola_txt(c, t, C["s06.g"] + 1.0, "14 m/s", 1250, 760, 130, 66, F.VEL)


# ---------------- frenagem ----------------
def b_frenagem(c, t, C, b):
    def s07():
        x = 1450
        E.foco(c, t, C["s07"], 0.4, lambda a: F.carrinho(c, x, 900, 240, a=a))
        if t >= C["s07"]:
            F.chao(c, 1100, 1840, 900, ep(t, C["s07"], 0.4))
        F.vetor(c, t, C["s07.c"], (x, 720), (x + 300, 720), "v", "20 m/s", F.VEL, 10, size=48)
        F.vetor(c, t, C["s07.d"], (x, 590), (x - 230, 590), "a", "−5 m/s^2", F.ACEL, 10, lado=-1, size=48)
        E.frase(c, t, C["s07.a"], [("para:", "i", 70), ("v = 0", "g", 70, COR)], XE, 230, passo=0.12)
        E.frase(c, t, C["s07.b"], [("a", "g", 70, F.ACEL), ("negativa:", "i", 70)] + ps("contra a velocidade", "i", 64, TINTA2), XE, 340, passo=0.1)
        E.formula_em(c, t, C["s07.e"], "0 = 400 − 10 · Δs", XE, 540, 86, "g", TINTA)
        E.formula_em(c, t, C["s07.f"], "10 · Δs = 400", XE, 700, 86, "g", TINTA)
        bola_txt(c, t, C["s07.g"], "40 m", XE + 260, 890, 110, 70)
    E.saida(c, t, C["s08"] - 0.1, s07)
    if t < C["s08"]:
        return
    E.frase(c, t, C["s08.a"], ps("parar: isole o", "i", 64, TINTA2) + [("Δs", "g", 60, COR)] + ps("com v = 0", "i", 64, TINTA2), XE, 220, passo=0.1)
    E.formula_em(c, t, C["s08.b"], "Δs = f{v₀^2}{2 · |a|}", XE, 440, 130, "g", TINTA)
    if t >= C["s08.c"]:
        wq = E.formula(None, "Δs = ", 0, 0, 130, a=0)
        c.drawCircle(XE + wq + 90, 370, 80, M.paint(E.COR, ep(t, C["s08.c"], 0.4), stroke=7))
    E.frase(c, t, C["s08.d"], [("2×", "g", 76), ("velocidade", "i", 70), ("→", "g", 70, TINTA2), ("4×", "g", 76, COR), ("frenagem", "i", 70)], XE, 760, passo=0.12)
    E.frase(c, t, C["s08.e"], [("3×", "g", 76), ("velocidade", "i", 70), ("→", "g", 70, TINTA2), ("9×", "g", 76, COR), ("frenagem", "i", 70)], XE, 890, passo=0.12)
    quadrados(c, t, C["s08.d"] - 0.4, 1250, 560, 120)


# ---------------- reação ----------------
def b_reacao(c, t, C, b):
    y = 760
    x0 = 300
    E.frase(c, t, C["s09.a"], [("tempo", "g", 76), ("de", "i", 76), ("reação", "g", 76, COR)], XE, 230, passo=0.12)
    E.frase(c, t, C["s09.b"], [("≈", "g", 70, TINTA2), ("1", "g", 70), ("s", "b", 54, F.UNID)], XE + 700, 230, passo=0.1)
    E.frase(c, t, C["s09.c"], ps("o pé ainda vai para o freio:", "i", 60), XE, 350, passo=0.08)
    E.frase(c, t, C["s09.d"], ps("velocidade constante,", "i", 60) + [("MU", "g", 60, COR)], XE + 760, 350, passo=0.08)
    E.formula_em(c, t, C["s09.e"], "reação = v · t", XE, 500, 84, "g", TINTA)
    if t >= C["s09"]:
        M.line(c, 120, y, 1840, y, TINTA, ep(t, C["s09"], 0.4), 5)
    # a vinte metros por segundo: 20 m de reação + 40 m de frenagem
    k = 22
    if t < C["s10"]:
        E.foco(c, t, C["s09"], 0.4, lambda a: F.carrinho(c, x0, y, 180, a=a))
        return
    tr, tf = C["s10.b"], C["s10.c"]
    xr = x0 + 20 * k * ease_io(prog(t, tr, 1.0))
    xf = xr + 40 * k * ease_out(prog(t, tf, 1.4))
    F.carrinho(c, xf, y, 180)
    E.frase(c, t, C["s10.a"], [("parada", "g", 64, COR), ("=", "g", 64, TINTA2), ("reação", "i", 66), ("+", "g", 64, TINTA2), ("frenagem", "i", 66)], XE, 640, passo=0.12)
    faixa(c, t, tr, x0, x0 + 20 * k, y + 20, TINTA2, "20 m", 1.0, cor_rot=TINTA)
    faixa(c, t, tf, x0 + 20 * k, x0 + 60 * k, y + 20, E.COR, "40 m", 1.4)
    bola_txt(c, t, C["s10.d"], "60 m", 1650, 560, 110, 70)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s11"], [("cuidado", "g", 96, ERRADO)], XE, 200)
    E.frase(c, t, C["s11.a"], ps("esquecer a reação", "i", 72), XE + 480, 200, passo=0.12)
    y, x0, k = 760, 300, 22
    M.line(c, 120, y, 1840, y, TINTA, 1.0, 5)
    xo = x0 + 40 * k
    E.foco(c, t, C["s11.b"], 0.4, lambda a: (M.line(c, xo, y - 220, xo, y, ERRADO, a, 6), E.pilula(c, "a conta: 40 m", xo, y - 260, 46, "g", fundo=ERRADO, a=a)))
    q = ease_out(prog(t, C["s11.c"], 1.6))
    F.carrinho(c, x0 + 60 * k * q, y, 180)
    faixa(c, t, C["s11.c"], x0, x0 + 20 * k, y + 20, TINTA2, "reação", 0.8, cor_rot=TINTA)
    faixa(c, t, C["s11.c"] + 0.8, x0 + 20 * k, x0 + 60 * k, y + 20, E.COR, "frenagem", 1.0)
    E.foco(c, t, C["s11.c"] + 1.6, 0.4, lambda a: E.pilula(c, "+20 m", (xo + x0 + 60 * k) / 2, y - 140, 52, "g", fundo=E.COR, a=a))
    E.formula_em(c, t, C["s11.b"], "só Torricelli: 40 m ?", XE, 420, 84, "g", ERRADO)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def s12():
        E.frase(c, t, C["s12"], ps("agora, o atalho", "i", 76, CLARO), W / 2, 160, "center")
        E.frase(c, t, C["s12.a"], [("velocidade", "g", 66, BR), ("× n", "g", 66, CLARO), ("→", "g", 66, CLARO), ("frenagem", "g", 66, BR), ("× n²", "g", 66, CLARO)], W / 2, 300, "center", 0.12)
        E.foco(c, t, C["s12.b"] - 0.3, 0.4, lambda a: (centro(c, "v (m/s)", 700, 440, 50, "b", CLARO, a), centro(c, "frenagem (m)", 1220, 440, 50, "b", CLARO, a)))
        for i, (k, v, d_, m) in enumerate((("s12.b", "10", "10", ""), ("s12.c", "20", "40", "× 4"), ("s12.d", "30", "90", "× 9"))):
            yy = 560 + i * 130
            E.foco(c, t, C[k], 0.4, lambda a, yy=yy, v=v, d_=d_, m=m: (centro(c, v, 700, yy, 90, "g", BR, a), centro(c, d_, 1220, yy, 90, "g", BR, a),
                                                                       E.escreve(c, m, 1400, yy, 64, "g", CLARO, a)))
        E.frase(c, t, lerp(C["s12.d"], C["s12.end"], 0.4), ps("sem refazer a conta", "i", 62, CLARO), W / 2, 1000, "center", 0.1)
    E.saida(c, t, C["s13"] - 0.1, s12)
    if t < C["s13"]:
        return
    E.frase(c, t, C["s13.a"], ps("a velocidade entra", "i", 70, CLARO) + [("ao quadrado", "g", 66, BR)], W / 2, 260, "center", 0.12)
    E.frase(c, t, C["s13.b"], [("não", "g", 64, ERRADO)] + ps("vale para a parada inteira:", "i", 66, CLARO), W / 2, 480, "center", 0.1)
    E.frase(c, t, C["s13.c"], ps("a reação só dobra", "g", 66, BR), W / 2, 590, "center", 0.12)
    E.frase(c, t, C["s13.d"], ps("só com a mesma freada:", "i", 66, CLARO) + ps("pista molhada muda a conta", "g", 60, BR), W / 2, 820, "center", 0.1)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s14"], ps("hora de testar", "i", 72, COR), XE, 200)
    E.frase(c, t, C["s14.a"], [("15", "g", 76), ("m/s", "b", 58, F.UNID), ("→", "g", 70, TINTA2)], XE, 360, passo=0.12)
    E.frase(c, t, C["s14.b"], [("15", "g", 76, COR), ("m", "b", 58, F.UNID)] + ps("de frenagem", "i", 70), XE + 400, 360, passo=0.12)
    E.frase(c, t, C["s14.c"], [("reação:", "i", 70), ("1", "g", 70), ("s", "b", 54, F.UNID)], XE, 480, passo=0.12)
    E.frase(c, t, C["s14.d"], ps("distância de parada?", "g", 72), XE, 680, passo=0.12)
    E.frase(c, t, C["s14.e"], ps("e a", "i", 70) + [("30", "g", 70, COR), ("m/s?", "b", 56, F.UNID)], XE, 800, passo=0.12)
    if t >= C["s15"]:
        E.relogio(c, t, C["s15.a"], cx=1500, cy=520, r=190)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    x0, k = 380, 12
    y1, y2 = 420, 780
    for y in (y1, y2):
        M.line(c, 120, y, 1840, y, TINTA, ep(t, C["s16"], 0.4), 5)
    E.foco(c, t, C["s16"], 0.4, lambda a: (E.escreve(c, "15", 140, y1 - 90, 60, "g", F.VEL, a), E.escreve(c, "m/s", 140, y1 - 40, 40, "b", F.UNID, a)))
    faixa(c, t, C["s16.a"], x0, x0 + 15 * k, y1 + 20, TINTA2, "15 m", 0.6, cor_rot=TINTA)
    faixa(c, t, C["s16.b"], x0 + 15 * k, x0 + 30 * k, y1 + 20, E.COR, "15 m", 0.6)
    bola_txt(c, t, C["s16.c"], "30 m", 1300, y1 - 40, 95, 56)
    if t >= C["s17"]:
        E.foco(c, t, C["s17"], 0.4, lambda a: (E.escreve(c, "30", 140, y2 - 90, 60, "g", F.VEL, a), E.escreve(c, "m/s", 140, y2 - 40, 40, "b", F.UNID, a)))
        faixa(c, t, C["s17.a"], x0, x0 + 30 * k, y2 + 20, TINTA2, "30 m", 0.6, cor_rot=TINTA)
        faixa(c, t, C["s17.b"], x0 + 30 * k, x0 + 90 * k, y2 + 20, E.COR, "60 m", 0.8)
        E.foco(c, t, C["s17.b"] + 0.5, 0.4, lambda a: centro(c, "4 × 15", x0 + 60 * k, y2 - 30, 46, "b", COR, a))
        bola_txt(c, t, C["s17.c"], "90 m", 1650, y2 - 170, 95, 56)
        E.frase(c, t, C["s17.d"], [("v", "g", 60, F.VEL), ("× 2", "g", 60), ("→", "g", 60, TINTA2), ("parada", "i", 62), ("× 3", "g", 60, COR)], W / 2, 1010, "center", 0.12)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def s18():
        resumo(c, t, C, "s18", (("s18.a", [("sem", "i", 70), ("o", "i", 70), ("tempo:", "i", 70), ("Torricelli", "g", 70, COR)]),
                                ("s18.b", [("parada", "g", 70), ("=", "g", 70, TINTA2), ("reação", "i", 70), ("+", "g", 70, TINTA2), ("frenagem", "i", 70)]),
                                ("s18.c", [("2×", "g", 70), ("velocidade", "i", 70), ("→", "g", 70, TINTA2), ("4×", "g", 70, COR), ("frenagem", "i", 70)])))
    E.saida(c, t, C["s19"] - 0.1, s18)
    if t < C["s19"]:
        return
    E.frase(c, t, C["s19"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C["s19.a"], [("praticando:", "g", 100, COR)], XE, 410)
    E.frase(c, t, C["s19.a"] + 0.5, ps("vetores e movimentos", "i", 80), XE, 520, passo=0.12)
    E.frase(c, t, C["s19.b"], ps("a equação certa para cada questão", "i", 60, TINTA2), XE, 640, passo=0.08)
    for i in range(5):
        E.foco(c, t, C["s19.b"] + 0.3 + 0.15 * i, 0.4, lambda a, i=i: (M.rrect(c, XE + i * 170, 760, 140, 170, 18, E.COR if i % 2 == 0 else TINTA, a),
                                                                      centro(c, str(i + 1), XE + i * 170 + 70, 870, 80, "g", BR, a)))
    fim_inscreva(c, t, C, "s19", "s19.c", "s19.d")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, torricelli=b_torricelli, frenagem=b_frenagem, reacao=b_reacao, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
