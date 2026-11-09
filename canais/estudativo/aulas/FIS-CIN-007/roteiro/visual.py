"""Visual — Estudativo · FIS-CIN-007: aceleração e velocidade no MUV.

Segue a LINGUAGEM VISUAL DA FÍSICA do cabeçalho de FIS-CIN-001 (peças em _ferramentas/fisica.py, importado como F).
Nesta aula: velocidade em petróleo (F.VEL) e ACELERAÇÃO em violeta (F.ACEL), as duas como setas sobre o carro; a tabela
tempo × velocidade cresce linha a linha com "+4" de um degrau a outro (tabela_v()). Fórmulas novas com F.formula_legenda.
Atalho dos sinais no palco escuro, em quadro de quatro linhas.
Todo instante vem de C[...] (marcadores do roteiro)."""
import math

import editorial as E
import fisica as F
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Física", "Cinemática")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_FIS-CIN-007_aceleracao_e_velocidade_no_muv.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("aceleracao", "funcao", "freada", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"

# todas as contas da aula
assert [4 * s for s in range(4)] == [0, 4, 8, 12] and (20 - 0) / 5 == 4
assert 10 + 2 * 6 == 22 and 20 - 4 * 5 == 0 and 20 / 4 == 5
assert -3 + (-2) * 1 == -5 and abs(-5) > abs(-3)
assert (30 - 0) / 6 == 5 and 0 + 5 * 4 == 20


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


def setas_carro(c, t, t0, x, y, v, a, kv=60, ka=60, tv=None, ta=None, rv=None, ra=None, escuro=False, sentido=None):
    """carro em (x, y) com a seta da velocidade (petróleo) em cima e a da aceleração (violeta) mais acima; v, a com sinal"""
    E.foco(c, t, t0, 0.4, lambda q: F.carrinho(c, x, y, 220, a=q, sentido=sentido or (1 if v >= 0 else -1)))
    tv = t0 + 0.3 if tv is None else tv
    ta = t0 + 0.6 if ta is None else ta
    if v:
        F.vetor(c, t, tv, (x, y - 170), (x + kv * v, y - 170), "v", rv, F.VEL, 10, lado=1 if v > 0 else -1, size=50, escuro=escuro)
    if a:
        F.vetor(c, t, ta, (x, y - 290), (x + ka * a, y - 290), "a", ra, F.ACEL, 10, lado=1 if a > 0 else -1, size=50, escuro=escuro)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def um():
        E.foco(c, t, C["s01.a"], 0.6, lambda a: E.formula(c, "m/s^2", 700, 560, 300, "g", COR, a, "center"))
        E.frase(c, t, C["s01.a"] + 1.4, ps("a unidade da aceleração", "i", 64, TINTA2), 700, 720, "center", 0.1)
        E.foco(c, t, C["s01.b"], 0.5, lambda a: E.formula(c, "s^2 ?", 1470, 520, 220, "g", TINTA, a, "center"))
        E.foco(c, t, C["s01.c"], 0.5, lambda a: F.cronometro(c, 1470, 760, 110, 15, a, ""))
        if t >= C["s01.c"] + 0.6:
            E.risco(c, 1330, 900, 1610, 620, t, C["s01.c"] + 0.6, largura=12)
        E.frase(c, t, C["s01.d"], ps("até o fim da aula:", "i", 60), XE, 940, passo=0.1)
        E.frase(c, t, C["s01.d"] + 1.2, [("vai", "g", 60, COR), ("fazer", "g", 60, COR), ("sentido", "g", 60, COR)], XE + 520, 940, passo=0.12)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t >= C["s02"]:
        E.foco(c, t, C["s02"] + 0.3, 0.8, lambda a: E.simbolo(c, 1480, 540, 330 * ease_back(prog(t, C["s02"] + 0.3, 0.8)), giro=12 * math.sin(t * 0.4)), blur=0)
        E.frase(c, t, C["s02"], ps("e você vai", "i", 88), XE, 280, passo=0.14)
        for i, (k, s) in enumerate((("s02.a", "calcular a aceleração"), ("s02.b", "achar a velocidade"), ("s02.c", "acelerado ou retardado"))):
            y = 450 + i * 160
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, XE + 40, y - 30, 38, a=a), centro(c, str(i + 1), XE + 40, y - 8, 48, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, [(s, "g", 76, COR if i == 0 else TINTA)], XE + 110, y)


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    lembrete(c, t, C, "s03", (("s03.b", "movimento uniforme:", "velocidade constante"), ("s03.c", "o delta:", "final − inicial")))


# ---------------- aceleração ----------------
def tabela_v(c, t, linhas, x, y0, dy=96, size=70):
    """tabela t × v que cresce linha a linha; linhas = [(instante, t, v)]; o "+4" aparece entre as linhas"""
    E.foco(c, t, linhas[0][0] - 0.3, 0.4, lambda a: (E.formula(c, "t (s)", x, y0, 54, "b", TINTA2, a, "center"),
                                                    E.formula(c, "v (m/s)", x + 300, y0, 54, "b", TINTA2, a, "center"),
                                                    M.line(c, x - 120, y0 + 26, x + 440, y0 + 26, TINTA2, a, 3)))
    for i, (ti, ts, vs) in enumerate(linhas):
        yy = y0 + (i + 1) * dy
        E.foco(c, t, ti, 0.4, lambda a, yy=yy, ts=ts, vs=vs: (centro(c, ts, x, yy, size, "g", TINTA, a), centro(c, vs, x + 300, yy, size, "g", F.VEL, a)))
        if i:
            E.foco(c, t, ti + 0.2, 0.4, lambda a, yy=yy: centro(c, "+4", x + 470, yy - dy / 2 + 14, 46, "b", COR, a))


def b_aceleracao(c, t, C, b):
    def s04():
        y = 900
        vx = F.pista(c, t, C["s04.a"], 760, 1760, y, 0, 20, [0, 5, 10, 15, 20], "m", size=34)
        pos = lambda s: min(20.0, 2 * s * s / 4)
        F.movel(c, t, C["s04.b"], vx, y, pos, w=170) if t >= C["s04.a"] else None
        tabela_v(c, t, [(C["s04.a"], "0", "0"), (C["s04.b"], "1", "4"), (C["s04.c"], "2", "8"), (C["s04.d"], "3", "12")], 1120, 230, 96, 66)
        E.frase(c, t, C["s04.a"], ps("sai parado", "i", 70), XE, 260, passo=0.12)
        E.frase(c, t, C["s04.e"], [("+4", "g", 80, COR), ("m/s", "b", 60, F.UNID)], XE, 520, passo=0.12)
        E.frase(c, t, C["s04.e"] + 0.6, ps("a cada segundo", "i", 70), XE, 620, passo=0.12)
    E.saida(c, t, C["s05"] - 0.1, s04)
    if C["s05"] <= t < C["s06"]:
        def s05():
            E.frase(c, t, C["s05.a"], [("aceleração", "g", 96, F.ACEL)], XE, 230)
            E.frase(c, t, C["s05.a"] + 0.6, ps("quanto a velocidade muda a cada segundo", "i", 58, TINTA2), XE, 320, passo=0.08)
            F.formula_legenda(c, t, C["s05.b"], "a = f{Δv}{Δt}", [("Δv", "variação da velocidade", "m/s"), ("Δt", "tempo", "s")], XE, 540, 110,
                              tl=[C["s05.b"] + 1.2, C["s05.b"] + 1.8], size_l=52)
            E.frase(c, t, C["s05.c"], [("0", "g", 66), ("→", "g", 66, TINTA2), ("20", "g", 66), ("m/s", "b", 50, F.UNID)] + ps("em", "i", 66) + [("5", "g", 66), ("s", "b", 50, F.UNID)],
                    1080, 470, "left", 0.12)
            E.formula_em(c, t, C["s05.d"], "a = 20 ÷ 5 = 4", 1080, 640, 90, "g", TINTA)
        E.saida(c, t, C["s06"] - 0.1, s05)
    if t < C["s06"]:
        return
    E.frase(c, t, C["s06"], ps("e a unidade?", "i", 76), XE, 230)
    E.formula_em(c, t, C["s06.a"], "f{m/s}{s}", 560, 470, 120, "g", TINTA, "center")
    E.frase(c, t, C["s06.b"], [("4", "g", 70, F.ACEL), ("m/s", "b", 54, F.UNID)] + ps("a cada segundo", "i", 66), XE, 700, passo=0.12)
    E.formula_em(c, t, C["s06.c"], "= m/s^2", 760, 470, 120, "g", F.ACEL)
    E.frase(c, t, C["s06.d"], [("s²", "g", 70, COR), ("=", "g", 70, TINTA2)] + ps("por segundo, a cada segundo", "i", 66), XE, 880, passo=0.1)


# ---------------- MUV e função ----------------
def b_funcao(c, t, C, b):
    def s07():
        E.frase(c, t, C["s07.a"], ps("aceleração", "i", 80) + [("constante", "g", 80, F.ACEL)], XE, 300, passo=0.12)
        E.frase(c, t, C["s07.b"], [("movimento", "g", 76), ("uniformemente", "g", 76), ("variado", "g", 76)], XE, 470, passo=0.14)
        E.foco(c, t, C["s07.c"], 0.5, lambda a: E.pilula(c, "MUV", XE + 180, 650, 110, "g", fundo=E.COR, a=a))
        E.frase(c, t, C["s07.c"] + 0.6, ps("muda sempre o mesmo tanto por segundo", "i", 58, TINTA2), XE, 880, passo=0.1)
    E.saida(c, t, C["s08"] - 0.1, s07)
    if C["s08"] <= t < C["s09"]:
        def s08():
            F.formula_legenda(c, t, C["s08.a"], "v = v₀ + a · t",
                              [("v", "velocidade no instante t", "m/s"), ("v₀", "velocidade inicial", "m/s"), ("a", "aceleração", "m/s^2"), ("t", "tempo", "s")],
                              XE, 300, 140, tl=[C["s08.b"], C["s08.c"], C["s08.d"], C["s08.d"] + 1.0], size_l=56)
            w = E.formula(None, "v = v₀ + a · t", 0, 0, 140, a=0)
            wa = E.formula(None, "a · t", 0, 0, 140, a=0)
            q = ep(t, C["s08.e"], 0.5)
            if q > 0:
                E.chave(c, XE + w - wa, XE + w, 350, F.ACEL, q, 34)
                E.escreve(c, "o que a velocidade ganhou", XE + w + 30, 400, 52, "i", F.ACEL, q)
            E.frase(c, t, lerp(C["s08.e"], C["s08.end"], 0.55), ps("a mesma ideia do", "i", 60, TINTA2) + [("sorvete", "g", 60, COR)], XE, 960, passo=0.1)
        E.saida(c, t, C["s09"] - 0.1, s08)
    if t < C["s09"]:
        return
    setas_carro(c, t, C["s09.a"], 1400, 860, 1, 1, kv=260, ka=170, tv=C["s09.a"] + 0.3, ta=C["s09.b"], rv=None, ra=None)
    E.frase(c, t, C["s09.a"], [("ônibus:", "i", 70)], XE, 260)
    E.frase(c, t, C["s09.a"] + 0.4, [("v₀", "g", 70, F.VEL), ("=", "g", 70, TINTA2), ("10", "g", 70), ("m/s", "b", 52, F.UNID)], XE + 280, 260, passo=0.1)
    E.frase(c, t, C["s09.b"], [("a", "g", 70, F.ACEL), ("=", "g", 70, TINTA2), ("2", "g", 70), ("m/s²", "b", 52, F.UNID)], XE + 280, 370, passo=0.1)
    E.frase(c, t, C["s09.c"], [("t", "g", 70, COR), ("=", "g", 70, TINTA2), ("6", "g", 70), ("s", "b", 52, F.UNID)], XE + 280, 480, passo=0.1)
    E.formula_em(c, t, C["s09.d"], "v = 10 + 2 · 6", XE, 680, 96, "g", TINTA)
    bola_txt(c, t, C["s09.e"], "22 m/s", XE + 300, 880, 120, 60, F.VEL)


# ---------------- freada ----------------
def b_freada(c, t, C, b):
    def s10():
        setas_carro(c, t, C["s10.a"], 1350, 880, 1, -1, kv=300, ka=200, tv=C["s10.c"], ta=C["s10.d"], rv="20 m/s", ra="−4 m/s^2")
        E.frase(c, t, C["s10.a"], [("freada:", "g", 76, COR)], XE, 230)
        E.frase(c, t, C["s10.b"], ps("a com sinal contrário ao de v", "i", 64), XE, 340, passo=0.1)
        E.formula_em(c, t, C["s10.e"], "parar: v = 0", XE, 520, 80, "g", TINTA2)
        E.formula_em(c, t, C["s10.f"], "0 = 20 − 4t", XE, 660, 96, "g", TINTA)
        bola_txt(c, t, C["s10.g"], "5 s", XE + 230, 880, 110, 76)
    E.saida(c, t, C["s11"] - 0.1, s10)
    if t < C["s11"]:
        return
    x1, x2, w, y, h = 170, 1000, 750, 260, 620
    for x, k in ((x1, "s11.a"), (x2, "s11.c")):
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, h, p, prog_=p)
    E.frase(c, t, C["s11.a"], ps("|v| aumenta", "g", 64), x1 + 50, y + 100, passo=0.1)
    E.foco(c, t, C["s11.b"], 0.5, lambda a: E.pilula(c, "acelerado", x1 + w / 2, y + 200, 64, "g", fundo=E.COR, a=a))
    E.frase(c, t, C["s11.c"], ps("|v| diminui", "g", 64), x2 + 50, y + 100, passo=0.1)
    E.foco(c, t, C["s11.d"], 0.5, lambda a: E.pilula(c, "retardado", x2 + w / 2, y + 200, 64, "g", fundo=TINTA, a=a))
    for i, (x, k, v, a_) in enumerate(((x1, "s11.e", 1, 1), (x2, "s11.f", 1, -1))):
        E.foco(c, t, C[k], 0.4, lambda q, x=x: F.carrinho(c, x + w / 2 - 60, y + 590, 200, a=q))
        F.vetor(c, t, C[k] + 0.3, (x + w / 2 - 60, y + 450), (x + w / 2 - 60 + 200 * v, y + 450), "v", None, F.VEL, 9, size=44)
        F.vetor(c, t, C[k] + 0.5, (x + w / 2 - 60, y + 340), (x + w / 2 - 60 + 140 * a_, y + 340), "a", None, F.ACEL, 9, size=44, lado=1 if a_ > 0 else -1)
        E.foco(c, t, C[k] + 0.2, 0.4, lambda q, x=x, i=i: E.escreve(c, ("ônibus", "freando")[i], x + 50, y + 590, 44, "i", TINTA2, q))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s12"], [("cuidado", "g", 96, ERRADO)], XE, 200)
    E.frase(c, t, C["s12.a"], ps("a negativa = freada?", "i", 72), XE + 480, 200, passo=0.12)
    setas_carro(c, t, C["s12.b"], 1450, 900, -1, -1, kv=230, ka=160, tv=C["s12.b"] + 0.3, ta=C["s12.c"], rv="−3", ra="−2", sentido=1)
    E.foco(c, t, C["s12.b"], 0.4, lambda a: E.escreve(c, "de ré", 1400, 990, 50, "i", TINTA2, a))
    F.vetor(c, t, C["s12"] + 2.0, (1150, 400), (1350, 400), None, None, TINTA2, 6)
    E.foco(c, t, C["s12"] + 2.3, 0.4, lambda a: E.escreve(c, "frente = +", 1370, 414, 44, "i", TINTA2, a))
    E.formula_em(c, t, C["s12.d"], "−3 + (−2) · 1 = −5", XE, 520, 84, "g", TINTA)
    E.formula_em(c, t, C["s12.e"], "5 m/s > 3 m/s", XE, 690, 84, "g", COR)
    E.frase(c, t, C["s12.f"], ps("acelerando,", "g", 70, CERTO) + ps("para trás", "i", 72), XE, 860, passo=0.12)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def s13():
        E.frase(c, t, C["s13"], ps("agora, o atalho", "i", 76, CLARO), W / 2, 160, "center")
        E.frase(c, t, C["s13.a"], ps("olhe só os", "i", 76, CLARO) + [("sinais", "g", 76, BR)] + ps("de v e de a", "i", 76, CLARO), W / 2, 290, "center", 0.12)
        linhas = ((C["s13.b"], "+", "+", "acelerado", BR), (C["s13.b"] + 0.4, "−", "−", "acelerado", BR),
                  (C["s13.c"], "+", "−", "retardado", CLARO), (C["s13.c"] + 0.4, "−", "+", "retardado", CLARO))
        E.foco(c, t, C["s13.b"] - 0.4, 0.4, lambda a: (centro(c, "v", 640, 420, 60, "g", F.VEL, a), centro(c, "a", 820, 420, 60, "g", E.mix(F.ACEL, BR, 0.3), a)))
        for i, (ti, sv, sa, r, cr) in enumerate(linhas):
            yy = 520 + i * 100
            E.foco(c, t, ti, 0.4, lambda a, yy=yy, sv=sv, sa=sa, r=r, cr=cr: (centro(c, sv, 640, yy, 80, "g", BR, a), centro(c, sa, 820, yy, 80, "g", BR, a),
                                                                              E.escreve(c, r, 980, yy, 70, "g", cr, a)))
        E.frase(c, t, C["s13.d"], ps("como na multiplicação:", "i", 62, CLARO) + ps("sinais iguais dão +", "g", 60, BR), W / 2, 980, "center", 0.1)
    E.saida(c, t, C["s14"] - 0.1, s13)
    if t < C["s14"]:
        return
    y = 520
    E.frase(c, t, C["s14.a"], ps("mesmo sentido: empurra", "i", 66, CLARO) + [("a favor", "g", 66, BR)], W / 2, 240, "center", 0.1)
    E.frase(c, t, C["s14.b"], ps("sentido contrário: empurra", "i", 66, CLARO) + [("contra", "g", 66, BR)], W / 2, 360, "center", 0.1)
    F.vetor(c, t, C["s14.a"] + 0.4, (700, y), (1000, y), "v", None, F.VEL, 10, size=50, escuro=True)
    F.vetor(c, t, C["s14.a"] + 0.8, (1000, y), (1200, y), "a", None, E.mix(F.ACEL, BR, 0.3), 10, size=50, escuro=True)
    E.frase(c, t, C["s14.c"], [("não", "g", 64, ERRADO), ("serve", "i", 66, CLARO), ("com", "i", 66, CLARO), ("v = 0:", "g", 64, BR)] + ps("partindo ou virando", "i", 66, CLARO),
            W / 2, 800, "center", 0.1)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s15"], ps("hora de testar", "i", 72, COR), XE, 200)
    E.frase(c, t, C["s15.a"], [("moto:", "i", 70), ("parte", "i", 70), ("do", "i", 70), ("repouso", "g", 66)], XE, 330, passo=0.12)
    E.frase(c, t, C["s15.a"] + 1.2, [("v₀", "g", 60, F.VEL), ("=", "g", 60, TINTA2), ("0", "g", 60)], XE + 840, 330, passo=0.1)
    E.frase(c, t, C["s15.b"], [("30", "g", 70), ("m/s", "b", 52, F.UNID), ("em", "i", 70), ("6", "g", 70), ("s", "b", 52, F.UNID)], XE, 450, passo=0.12)
    for i, (k, s) in enumerate((("s15.d", "a aceleração?"), ("s15.e", "v depois de 4 s?"), ("s15.f", "acelerado ou retardado?"))):
        y = 620 + i * 110
        E.foco(c, t, C[k], 0.4, lambda a, y=y, i=i: (E.bola(c, XE + 30, y - 22, 30, a=a), centro(c, "abc"[i], XE + 30, y - 6, 40, "g", BR, a)))
        E.frase(c, t, C[k] + 0.1, ps(s, "g", 62), XE + 90, y, passo=0.1)
    if t >= C["s16"]:
        E.relogio(c, t, C["s16.a"], cx=1500, cy=520, r=190)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    E.formula_em(c, t, C["s17.a"], "Δv = 30 − 0 = 30", XE, 260, 84, "g", TINTA2)
    E.formula_em(c, t, C["s17.b"], "a = 30 ÷ 6", XE, 400, 90, "g", TINTA)
    bola_txt(c, t, C["s17.b"] + 1.0, "5 m/s²", 1250, 360, 120, 52, F.ACEL)
    E.formula_em(c, t, C["s17.c"], "v = 0 + 5 · 4", XE, 610, 90, "g", TINTA)
    bola_txt(c, t, C["s17.d"], "20 m/s", 1250, 660, 120, 56, F.VEL)
    E.frase(c, t, C["s17.e"], [("v", "g", 66, F.VEL), ("e", "i", 66), ("a", "g", 66, F.ACEL), ("positivos:", "i", 66), ("acelerado", "g", 66, COR)], XE, 850, passo=0.12)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def s18():
        resumo(c, t, C, "s18", (("s18.a", [("aceleração", "g", 66, F.ACEL), ("=", "g", 66, TINTA2), ("quanto", "i", 66), ("v", "i", 66), ("muda", "i", 66), ("por", "i", 66), ("segundo", "i", 66)]),
                                ("s18.b", [("v = v₀ + a · t", "g", 70, COR)]),
                                ("s18.c", [("sinais", "i", 66), ("iguais:", "i", 66), ("acelerado;", "g", 66), ("diferentes:", "i", 66), ("retardado", "g", 66)])))
    E.saida(c, t, C["s19"] - 0.1, s18)
    if t < C["s19"]:
        return
    E.frase(c, t, C["s19"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C["s19.a"], ps("onde o corpo está?", "i", 76), XE, 400, passo=0.12)
    E.frase(c, t, C["s19.b"], [("função", "g", 100, COR), ("do", "i", 100), ("2º", "g", 100, COR), ("grau", "g", 100, COR)], XE, 560, passo=0.14)
    P = E.plano(c, t, C["s19.b"] + 0.3, 300, 640, 700, 330, 0, 5, 0, 25, 1, 5, grade=False, rotulos=False, nomes=("t", "s"))
    E.curva(c, t, C["s19.b"] + 0.8, P, lambda x: x * x, 0, 5, d=1.0)
    fim_inscreva(c, t, C, "s19", "s19.c", "s19.d")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, aceleracao=b_aceleracao, funcao=b_funcao, freada=b_freada, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
