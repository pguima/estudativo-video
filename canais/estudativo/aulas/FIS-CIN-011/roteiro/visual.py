"""Visual — Estudativo · FIS-CIN-011: gráfico posição por tempo.

Segue a LINGUAGEM VISUAL DA FÍSICA do cabeçalho de FIS-CIN-001 (peças em _ferramentas/fisica.py, importado como F).
Nesta aula: o gráfico s × t é F.grafico (eixos com nome e unidade); a linha do corpo em laranja (E.curva); a inclinação
é o "degrau" Δt (deitado) e Δs (em pé) desenhado sobre a reta (degrau()), em petróleo, porque dá a velocidade; trechos
pintados por tipo: vai (laranja), repouso (cinza), volta (azul F.NEG). O carro na pista, embaixo, anda junto com o
gráfico quando ajuda a ler (s(t) → posição na pista). Encontro = esfera laranja no cruzamento, com guias até os eixos.
Todo instante vem de C[...] (marcadores do roteiro)."""
import math

import editorial as E
import fisica as F
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Física", "Cinemática")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_FIS-CIN-011_grafico_posicao_por_tempo.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("ler", "passeio", "encontro", "parabola", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"

mu = lambda t: 10 + 5 * t
passeio = lambda t: 5 * t if t <= 4 else (20 if t <= 6 else 20 - 5 * (t - 6))
par = lambda t: 8 * t - t * t
cA = lambda t: 10 * t
cB = lambda t: 60 - 5 * t
# todas as contas da aula
assert mu(0) == 10 and mu(2) == 20 and mu(4) == 30 and (mu(4) - mu(0)) / 4 == 5
assert passeio(4) == 20 and passeio(6) == 20 and passeio(10) == 0 and (0 - 20) / 4 == -5
assert par(4) == 16 and 8 - 2 * 4 == 0
assert cA(8) == 80 and cB(8) == 20 and (80 - 0) / 8 == 10 and (20 - 60) / 8 == -5 and cA(4) == cB(4) == 40


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
def degrau(c, t, t0, P, x0, x1, f, rot_t=None, rot_s=None, cor=None, size=44, dentro=False):
    """degrau da inclinação: Δt deitado de x0 a x1 e Δs em pé até a reta, com os rótulos"""
    cor = cor or F.VEL
    y0, y1 = f(x0), f(x1)
    q1 = ep(t, t0, 0.5)
    q2 = ep(t, t0 + 0.5, 0.5)
    if q1 > 0:
        M.line(c, P.x(x0), P.y(y0), lerp(P.x(x0), P.x(x1), q1), P.y(y0), cor, 1.0, 6, dash=E.TRACO)
        if rot_t:
            centro(c, rot_t, (P.x(x0) + P.x(x1)) / 2, P.y(y0) + (52 if y1 >= y0 else -22), size, "b", cor, q1)
    if q2 > 0:
        M.line(c, P.x(x1), P.y(y0), P.x(x1), lerp(P.y(y0), P.y(y1), q2), cor, 1.0, 6, dash=E.TRACO)
        if rot_s:
            xr = P.x(x1) - 20 - E.larg(rot_s, "b", size) if dentro else P.x(x1) + 20
            E.escreve(c, rot_s, xr, (P.y(y0) + P.y(y1)) / 2 + 16, size, "b", cor, q2)


def trecho(c, t, t0, P, f, a, b, cor, d=0.8):
    E.curva(c, t, t0, P, f, a, b, d=d, cor=cor, largura=9)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def um():
        P = F.grafico(c, t, C["s01.a"], 1000, 240, 760, 640, 0, 8, 0, 80, eixo_x="t (s)", eixo_y="s (m)", passo=1, passo_y=10, marcas_x=[2, 4, 6, 8], marcas_y=[20, 40, 60, 80])
        E.curva(c, t, C["s01.b"], P, lambda x: 3 * x, 0, 8, d=1.0, cor=TINTA2, largura=8)
        E.curva(c, t, C["s01.c"], P, lambda x: 10 * x, 0, 8, d=1.0, cor=E.COR, largura=9)
        E.foco(c, t, C["s01.b"] + 0.8, 0.4, lambda a: E.escreve(c, "devagar", P.x(8) - 30, P.y(24) + 60, 48, "i", TINTA2, a))
        E.foco(c, t, C["s01.c"] + 0.8, 0.4, lambda a: E.escreve(c, "quase em pé", P.x(2.6), P.y(52), 48, "i", COR, a))
        E.frase(c, t, C["s01.a"], ps("gráfico da", "i", 70) + [("posição", "g", 66)], XE, 300, passo=0.12)
        E.frase(c, t, C["s01.a"] + 0.8, ps("pelo", "i", 70) + [("tempo", "g", 66)], XE, 400, passo=0.12)
        E.frase(c, t, C["s01.c"] + 1.0, ps("mais rápido?", "i", 70), XE, 560, passo=0.12)
        E.frase(c, t, C["s01.d"], [("mais", "g", 70, COR), ("inclinada", "g", 70, COR)], XE, 680, passo=0.12)
        E.frase(c, t, C["s01.e"], [("inclinação", "g", 60), ("=", "g", 60, TINTA2)], XE, 840, passo=0.12)
        E.frase(c, t, C["s01.e"] + 0.4, [("velocidade", "g", 66, F.VEL)], XE, 930)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t >= C["s02"]:
        promessa(c, t, C, "s02", (("s02.a", "velocidade no gráfico", 1.4), ("s02.b", "repouso, ida, volta", 0), ("s02.e", "encontro", 0)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    lembrete(c, t, C, "s03", (("s03.b", "ler um gráfico:", "quando sobe, quando desce"), ("s03.c", "taxa de variação:", "Δy ÷ Δx"),
                              ("s03.d", "funções da posição:", "MU e MUV")))


# ---------------- ler o gráfico ----------------
def b_ler(c, t, C, b):
    P = F.grafico(c, t, C["s04"], 900, 220, 840, 640, 0, 6, 0, 40, eixo_x="t (s)", eixo_y="s (m)", passo=1, passo_y=10, marcas_x=[1, 2, 3, 4, 5, 6], marcas_y=[10, 20, 30, 40])
    if t < C["s05"]:
        q = ep(t, C["s04.a"], 0.4) * (1 - ep(t, C["s04.b"], 0.4))
        if q > 0:
            M.line(c, P.x(0), P.oy, P.x(6), P.oy, E.COR, q, 12)
        q = ep(t, C["s04.b"], 0.4) * (1 - ep(t, C["s04.c"], 0.4))
        if q > 0:
            M.line(c, P.ox, P.y(0), P.ox, P.y(40), E.COR, q, 12)
        E.frase(c, t, C["s04.a"], [("tempo:", "g", 64), ("eixo", "i", 66), ("deitado", "i", 66)], XE, 320, passo=0.12)
        E.frase(c, t, C["s04.b"], [("posição:", "g", 64), ("eixo", "i", 66), ("em", "i", 66), ("pé", "i", 66)], XE, 430, passo=0.12)
        E.frase(c, t, C["s04.c"], ps("cada ponto: onde estava", "i", 56, TINTA2), XE, 580, passo=0.08)
        E.frase(c, t, C["s04.c"] + 1.0, ps("e quando", "i", 56, TINTA2), XE, 660, passo=0.08)
        if t >= C["s04.d"]:
            E.ponto(c, t, C["s04.d"], P, 2, 20, "(2 s, 20 m)", guias=True)
        return
    E.curva(c, t, C["s05.b"], P, mu, 0, 6, d=1.0, largura=9)
    if t >= C["s05.c"]:
        E.ponto(c, t, C["s05.c"], P, 0, 10, None)
    E.formula_em(c, t, C["s05.a"], "s = 10 + 5t", XE, 300, 84, "g", TINTA)
    E.frase(c, t, C["s05.b"], [("função", "i", 64), ("afim:", "i", 64), ("reta", "g", 64, COR)], XE, 420, passo=0.12)
    E.frase(c, t, C["s05.c"], [("corta", "i", 60), ("em", "i", 60), ("s₀", "g", 60, COR), ("= 10 m", "g", 60)], XE, 520, passo=0.12)
    if t < C["s06"]:
        return
    degrau(c, t, C["s06.c"], P, 0, 4, mu, "Δt = 4 s", "Δs = 20 m")
    E.formula_em(c, t, C["s06.b"], "v = f{Δs}{Δt}", XE, 720, 90, "g", F.VEL)
    E.formula_em(c, t, C["s06.e"], "= f{20}{4} = 5 m/s", XE + 60, 880, 80, "g", F.VEL)
    E.frase(c, t, lerp(C["s06.e"], C["s06.end"], 0.6), ps("o mesmo número colado no t", "i", 54, TINTA2), XE, 1010, passo=0.08)


# ---------------- passeio: ida, repouso, volta ----------------
def b_passeio(c, t, C, b):
    P = F.grafico(c, t, C["s07"], 900, 230, 840, 540, 0, 10, 0, 25, eixo_x="t (s)", eixo_y="s (m)", passo=1, passo_y=5, marcas_x=[2, 4, 6, 8, 10], marcas_y=[5, 10, 15, 20])
    trecho(c, t, C["s07.a"], P, passeio, 0, 4, E.COR)
    trecho(c, t, C["s07.c"], P, passeio, 4, 6, TINTA2)
    trecho(c, t, C["s07.e"], P, passeio, 6, 10, F.NEG)
    # o carro na pista, embaixo, anda com o gráfico
    y = 1000
    vx = lambda v: 300 + v * 30
    if t >= C["s07"]:
        M.line(c, vx(0) - 30, y, vx(25) + 30, y, TINTA, ep(t, C["s07"], 0.4), 5)
    tt = 0.0
    for k, a_, b_ in (("s07.a", 0, 4), ("s07.c", 4, 6), ("s07.e", 6, 10)):
        if t >= C[k]:
            tt = lerp(a_, b_, ease_io(prog(t, C[k], 1.6)))
    E.foco(c, t, C["s07"] + 0.3, 0.4, lambda a: F.carrinho(c, vx(passeio(tt)), y, 130, a=a, sentido=-1 if tt > 6 else 1))
    E.foco(c, t, C["s07"] + 0.3, 0.4, lambda a: (E.escreve(c, "0", vx(0) - 10, y + 50, 36, "b", TINTA, a), E.escreve(c, "20 m", vx(20) - 30, y + 50, 36, "b", TINTA, a)))
    if t < C["s08"]:
        E.frase(c, t, C["s07.b"], [("sobe:", "g", 66, COR), ("vai", "i", 70)], XE, 340, passo=0.12)
        E.frase(c, t, C["s07.d"], [("deitada:", "g", 66, TINTA2), ("repouso", "i", 70)], XE, 470, passo=0.12)
        E.frase(c, t, C["s07.f"], [("desce:", "g", 66, F.NEG), ("volta", "i", 70)], XE, 600, passo=0.12)
        return
    E.frase(c, t, C["s08.a"], [("subindo:", "g", 60, COR), ("v", "g", 60), ("> 0", "g", 60)], XE, 330, passo=0.12)
    E.frase(c, t, C["s08.b"], [("deitada:", "g", 60, TINTA2), ("v", "g", 60), ("= 0", "g", 60)], XE, 450, passo=0.12)
    E.frase(c, t, C["s08.c"], [("descendo:", "g", 60, F.NEG), ("v", "g", 60), ("< 0", "g", 60)], XE, 570, passo=0.12)
    degrau(c, t, C["s08.d"], P, 6, 10, passeio, "Δt = 4 s", "−20 m", cor=F.NEG, size=40, dentro=True)
    E.formula_em(c, t, C["s08.d"] + 1.2, "v = f{−20}{4} = −5 m/s", XE, 760, 70, "g", F.NEG)


# ---------------- encontro ----------------
def b_encontro(c, t, C, b):
    P = F.grafico(c, t, C["s09"], 900, 230, 840, 640, 0, 8, 0, 80, eixo_x="t (s)", eixo_y="s (m)", passo=1, passo_y=10, marcas_x=[2, 4, 6, 8], marcas_y=[20, 40, 60, 80])
    E.curva(c, t, C["s09.a"], P, lambda x: 5 * x + 20, 0, 8, d=1.0, largura=9)
    E.curva(c, t, C["s09.a"] + 0.6, P, lambda x: 70 - 5 * x, 0, 8, d=1.0, cor=F.NEG, largura=9)
    if t >= C["s09.b"]:
        E.ponto(c, t, C["s09.b"], P, 5, 45, None, r=18)
    q = ep(t, C["s09.d"], 0.5)
    if q > 0:
        M.line(c, P.x(5), P.y(45), P.x(5), P.oy, TINTA, q, 4, dash=E.TRACO)
        E.pilula(c, "quando: 5 s", P.x(5), P.oy + 110, 40, "g", fundo=TINTA, a=q)
    q = ep(t, C["s09.e"], 0.5)
    if q > 0:
        M.line(c, P.x(5), P.y(45), P.ox, P.y(45), TINTA, q, 4, dash=E.TRACO)
        E.pilula(c, "onde: 45 m", P.ox + 150, P.y(45) - 50, 40, "g", fundo=TINTA, a=q)
    E.frase(c, t, C["s09.a"], ps("dois corpos, um gráfico", "i", 64), XE, 320, passo=0.1)
    E.frase(c, t, C["s09.b"], [("cruzou:", "g", 64)] + ps("mesma posição,", "i", 62), XE, 470, passo=0.1)
    E.frase(c, t, C["s09.b"] + 1.8, ps("mesmo instante", "i", 62), XE, 560, passo=0.1)
    E.frase(c, t, C["s09.c"], [("encontro", "g", 90, COR)], XE, 720)


# ---------------- parábola ----------------
def b_parabola(c, t, C, b):
    if t < C["s11"]:
        E.frase(c, t, C["s10.a"], [("MUV:", "g", 64), ("s", "g", 64, COR), ("tem", "i", 66), ("t²", "g", 64, COR)], XE, 260, passo=0.12)
        E.frase(c, t, C["s10.b"], [("parábola", "g", 84, COR)], XE, 380)
        for i, (k, sg, f) in enumerate((("s10.c", "a > 0", lambda x: (x - 2) ** 2 + 1), ("s10.d", "a < 0", lambda x: 5 - (x - 2) ** 2))):
            x0 = 220 + i * 470
            P = E.plano(c, t, C[k], x0, 520, 360, 300, 0, 4, 0, 6, 1, 1, grade=False, rotulos=False, nomes=("t", "s"))
            E.curva(c, t, C[k] + 0.3, P, f, 0, 4, d=0.8, largura=8)
            E.foco(c, t, C[k] + 0.3, 0.4, lambda a, x0=x0, sg=sg, i=i: E.escreve(c, sg + (": abre para cima" if i == 0 else ": abre para baixo"), x0, 930, 42, "b", TINTA, a))
        E.frase(c, t, C["s10.e"], ps("a inclinação muda", "i", 58, TINTA2), 1180, 480, "left", 0.08)
        E.frase(c, t, C["s10.e"] + 0.8, ps("a cada ponto", "i", 58, TINTA2), 1180, 560, "left", 0.08)
        E.frase(c, t, C["s10.e"] + 2.2, [("mais", "i", 58), ("em", "i", 58), ("pé:", "i", 58), ("|v|", "g", 56, F.VEL), ("aumenta", "i", 58)], 1180, 680, "left", 0.1)
        E.frase(c, t, C["s10.e"] + 4.4, [("mais", "i", 58), ("deitada:", "i", 58), ("|v|", "g", 56, F.VEL), ("diminui", "i", 58)], 1180, 790, "left", 0.1)
        return
    P = F.grafico(c, t, C["s11"], 900, 230, 840, 640, 0, 8, 0, 20, eixo_x="t (s)", eixo_y="s (m)", passo=1, passo_y=5, marcas_x=[2, 4, 6, 8], marcas_y=[4, 8, 12, 16])
    E.curva(c, t, C["s11"] + 0.3, P, par, 0, 8, d=1.4, largura=9)
    E.formula_em(c, t, C["s11"] + 0.3, "s = 8t − t^2", XE, 280, 76, "g", TINTA2)
    if t >= C["s11.a"]:
        E.ponto(c, t, C["s11.a"], P, 4, 16, "vértice", r=16, lado=(1, -1))
    q = ep(t, C["s11.b"], 0.5)
    if q > 0:
        M.line(c, P.x(2.6), P.y(16), P.x(5.4), P.y(16), F.VEL, q, 6, dash=E.TRACO)
    E.frase(c, t, C["s11.b"], [("deitada:", "i", 64), ("v = 0", "g", 64, F.VEL)], XE, 440, passo=0.12)
    E.frase(c, t, C["s11.c"], ps("para e vira", "g", 64, COR), XE, 560, passo=0.12)
    E.frase(c, t, C["s11.d"], [("antes", "i", 60), ("ia,", "g", 60), ("depois", "i", 60), ("volta", "g", 60)], XE, 680, passo=0.12)
    E.frase(c, t, lerp(C["s11.d"], C["s11.end"], 0.4), [("antes:", "i", 56), ("freia;", "g", 56)], XE, 820, passo=0.1)
    E.frase(c, t, lerp(C["s11.d"], C["s11.end"], 0.6), [("depois:", "i", 56), ("acelera", "g", 56)], XE, 910, passo=0.1)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s12"], [("cuidado", "g", 96, ERRADO)], XE, 200)
    E.frase(c, t, C["s12.a"], ps("gráfico não é o caminho", "i", 72), XE + 480, 200, passo=0.12)
    P = F.grafico(c, t, C["s12.a"] + 0.4, 280, 330, 600, 420, 0, 4, 0, 40, eixo_x="t (s)", eixo_y="s (m)", passo=1, passo_y=10, marcas_x=[2, 4], marcas_y=[20, 40], size=34)
    E.curva(c, t, C["s12.b"], P, lambda x: 10 * x, 0, 4, d=0.8, largura=9)
    # a leitura errada: o carro subindo uma ladeira
    def ladeira(a):
        M.line(c, 1120, 860, 1760, 420, TINTA2, a, 6)
        c.save(); c.translate(1440, 640); c.rotate(-34.5); F.carrinho(c, 0, 0, 170, a=a); c.restore()
    E.saida(c, t, C["s12.d"], lambda: E.foco(c, t, C["s12.c"], 0.5, ladeira))
    if C["s12.c"] + 0.6 <= t < C["s12.d"] + 0.4:
        E.risco(c, 1150, 880, 1750, 420, t, C["s12.d"] - 0.5, largura=12)
    if t >= C["s12.d"]:
        M.line(c, 1080, 760, 1800, 760, TINTA, ep(t, C["s12.d"], 0.4), 5)
        q = ease_io(prog(t, C["s12.d"] + 0.3, 2.5))
        F.carrinho(c, lerp(1160, 1700, q), 760, 170)
        E.foco(c, t, C["s12.d"] + 0.3, 0.4, lambda a: E.escreve(c, "rua plana", 1340, 840, 50, "i", TINTA2, a))
    E.frase(c, t, C["s12.e"], ps("sobe o", "i", 62) + [("número", "g", 60, COR)] + ps("da posição", "i", 62), W / 2, 1000, "center", 0.1)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def s13():
        E.frase(c, t, C["s13"], ps("agora, o atalho", "i", 76, CLARO), W / 2, 160, "center")
        E.frase(c, t, C["s13.a"], ps("compare as", "i", 68, CLARO) + [("inclinações", "g", 66, BR)], XE, 300, passo=0.12)
        P = E.plano(c, t, C["s13.a"] + 0.4, 1100, 260, 640, 520, 0, 8, 0, 80, 1, 10, grade=False, rotulos=False, nomes=("t", "s"), escuro=True)
        E.curva(c, t, C["s13.b"], P, lambda x: 9 * x, 0, 8, d=0.8, cor=BR, largura=8)
        E.curva(c, t, C["s13.b"] + 0.4, P, lambda x: 3 * x, 0, 8, d=0.8, cor=CLARO, largura=8)
        E.curva(c, t, C["s13.c"], P, lambda x: 3 * x + 30, 0, 8, d=0.8, cor=CLARO, largura=8, tracejada=True)
        E.frase(c, t, C["s13.b"], [("mais", "i", 64, CLARO), ("em", "i", 64, CLARO), ("pé:", "i", 64, CLARO), ("mais rápido", "g", 62, BR)], XE, 440, passo=0.12)
        E.frase(c, t, C["s13.c"], [("paralelas:", "i", 64, CLARO), ("mesma", "g", 62, BR), ("v", "g", 62, BR)], XE, 560, passo=0.12)
        E.frase(c, t, C["s13.d"], ps("valor: dois pontos", "i", 64, CLARO) + [("na grade", "g", 62, BR)], XE, 720, passo=0.12)
    E.saida(c, t, C["s14"] - 0.1, s13)
    if t < C["s14"]:
        return
    E.formula_em(c, t, C["s14.a"], "inclinação = f{Δs}{Δt} = v", W / 2, 320, 100, "g", BR, "center")
    E.frase(c, t, C["s14.b"], [("não", "g", 62, ERRADO), ("compensa", "i", 64, CLARO)] + ps("no olho com escalas diferentes", "i", 64, CLARO), W / 2, 600, "center", 0.1)
    E.frase(c, t, C["s14.c"], [("parábola:", "g", 62, BR)] + ps("dois pontos dão a", "i", 64, CLARO) + [("velocidade média", "g", 62, BR)], W / 2, 780, "center", 0.1)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s15"], ps("hora de testar", "i", 72, COR), XE, 200)
    P = F.grafico(c, t, C["s15"] + 0.3, 960, 230, 800, 640, 0, 8, 0, 80, eixo_x="t (s)", eixo_y="s (m)", passo=1, passo_y=10, marcas_x=[2, 4, 6, 8], marcas_y=[20, 40, 60, 80])
    E.curva(c, t, C["s15.a"], P, cA, 0, 8, d=1.0, largura=9, rotulo="A", em=(7.2, 76))
    E.curva(c, t, C["s15.b"], P, cB, 0, 8, d=1.0, cor=F.NEG, largura=9, rotulo="B", em=(7.4, 30))
    E.frase(c, t, C["s15.a"], [("A:", "g", 64, COR)] + ps("sai do zero", "i", 64), XE, 360, passo=0.12)
    E.frase(c, t, C["s15.b"], [("B:", "g", 64, F.NEG)] + ps("sai dos 60 m", "i", 64), XE, 460, passo=0.12)
    E.frase(c, t, C["s15.c"], ps("velocidade de cada um?", "g", 56), XE, 620, passo=0.1)
    E.frase(c, t, C["s15.d"], [("quando", "g", 56, COR), ("e", "i", 58), ("onde", "g", 56, COR)], XE, 720, passo=0.1)
    E.frase(c, t, C["s15.d"] + 0.6, ps("se encontram?", "g", 56), XE, 800, passo=0.1)
    if t >= C["s16"]:
        E.foco(c, t, C["s16.a"], 0.5, lambda a: (E.bola(c, XE + 70, 900, 70, a=a), M.rrect(c, XE + 46, 870, 16, 60, 6, BR, a), M.rrect(c, XE + 78, 870, 16, 60, 6, BR, a)))
        E.frase(c, t, C["s16.a"] + 0.2, ps("pause o vídeo", "i", 64), XE + 170, 920, passo=0.1)
        f_ = min(1.0, max(0.0, (t - C["s16.a"] - 0.8) / 3.0))
        if f_ > 0:
            E.arco(c, XE + 70, 900, 96, -90, 360 * f_, TINTA, 8)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    P = F.grafico(c, t, C["s17"], 960, 230, 800, 640, 0, 8, 0, 80, eixo_x="t (s)", eixo_y="s (m)", passo=1, passo_y=10, marcas_x=[2, 4, 6, 8], marcas_y=[20, 40, 60, 80])
    E.curva(c, t, C["s17"], P, cA, 0, 8, d=0.6, largura=9)
    E.curva(c, t, C["s17"], P, cB, 0, 8, d=0.6, cor=F.NEG, largura=9)
    if t < C["s18"]:
        E.saida(c, t, C["s17.b"] - 0.1, lambda: degrau(c, t, C["s17.a"], P, 0, 8, cA, None, "80 m", dentro=True))
        degrau(c, t, C["s17.b"], P, 0, 8, cB, None, "−40 m", cor=F.NEG, dentro=True)
        E.formula_em(c, t, C["s17.a"], "vA = f{80}{8} = 10 m/s", XE, 340, 74, "g", COR)
        E.formula_em(c, t, C["s17.c"], "vB = f{20 − 60}{8} = −5 m/s", XE, 560, 70, "g", F.NEG)
        pilula_em(c, t, C["s17.d"], "B volta", XE + 200, 760, 52, F.NEG)
        return
    E.ponto(c, t, C["s18.a"], P, 4, 40, None, r=18, guias=True)
    E.foco(c, t, C["s18.a"] + 0.2, 0.4, lambda a: E.pilula(c, "4 s", P.x(4), P.oy + 110, 44, "g", fundo=TINTA, a=a))
    E.foco(c, t, C["s18.b"], 0.4, lambda a: E.pilula(c, "40 m", P.ox - 110, P.y(40) - 70, 44, "g", fundo=TINTA, a=a))
    E.formula_em(c, t, C["s18.c"], "A: 10 · 4 = 40", XE, 400, 76, "g", COR)
    E.formula_em(c, t, C["s18.d"], "B: 60 − 5 · 4 = 40", XE, 560, 76, "g", F.NEG)
    E.foco(c, t, C["s18.d"] + 1.2, 0.4, lambda a: E.selo(c, XE + 120, 740, 56, True, a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def s19():
        resumo(c, t, C, "s19", (("s19.a", [("inclinação", "g", 70), ("=", "g", 70, TINTA2), ("velocidade", "g", 70, F.VEL)]),
                                ("s19.b", [("sobe,", "g", 70, COR), ("vai;", "i", 70), ("deitada,", "g", 70, TINTA2), ("repouso;", "i", 70), ("desce,", "g", 70, F.NEG), ("volta", "i", 70)]),
                                ("s19.c", [("cruzou,", "g", 70, COR), ("encontrou", "i", 70)])))
    E.saida(c, t, C["s20"] - 0.1, s19)
    if t < C["s20"]:
        return
    E.frase(c, t, C["s20"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C["s20"] + 1.0, [("gráfico", "g", 100, COR), ("v × t", "g", 100, COR)], XE, 400, passo=0.14)
    E.frase(c, t, C["s20.a"], [("inclinação:", "i", 64), ("aceleração", "g", 64, F.ACEL)], XE, 530, passo=0.12)
    E.frase(c, t, C["s20.b"], [("área:", "i", 64), ("deslocamento", "g", 64, COR)], XE, 630, passo=0.12)
    P = E.plano(c, t, C["s20"] + 1.2, 300, 700, 640, 290, 0, 6, 0, 30, 1, 10, grade=False, rotulos=False, nomes=("t", "v"))
    E.curva(c, t, C["s20"] + 1.6, P, lambda x: 4 * x + 4, 0, 6, d=0.8, cor=F.VEL, largura=8)
    if t >= C["s20.b"]:
        E.area(c, t, C["s20.b"], P, lambda x: 4 * x + 4, 0, 6, alfa=0.28)
    fim_inscreva(c, t, C, "s20", "s20.c", "s20.d")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, ler=b_ler, passeio=b_passeio, encontro=b_encontro, parabola=b_parabola, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
