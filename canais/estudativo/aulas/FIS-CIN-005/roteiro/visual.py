"""Visual — Estudativo · FIS-CIN-005: movimento uniforme, a função horária.

Segue a LINGUAGEM VISUAL DA FÍSICA do cabeçalho de FIS-CIN-001 (peças em _ferramentas/fisica.py, importado como F).
Nesta aula: a estrada é a pista numerada (F.pista) e o carro anda com F.movel, deixando marcas fantasma de hora em hora
(rastro); cada hora vira um salto petróleo (E.salto, F.VEL) com "+80". A fórmula nova entra com F.formula_legenda.
Contas de achar o tempo em linhas (conta()), uma por fala, com o resultado na esfera.
Todo instante vem de C[...] (marcadores do roteiro)."""
import math

import editorial as E
import fisica as F
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Física", "Cinemática")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_FIS-CIN-005_movimento_uniforme_funcao_horaria.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("mu", "formula", "tempo", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"

# todas as contas da aula
assert 20 + 80 * 3 == 260 and 80 * 3 == 240 and [20 + 80 * h for h in range(4)] == [20, 100, 180, 260]
assert 340 - 20 == 320 and 320 / 80 == 4 and 20 + 80 * 4 == 340
assert 100 / 5 == 20 and 100 - 5 * 20 == 0
assert 50 + 54 * 10 == 590 and 54 / 3.6 == 15 and 50 + 15 * 10 == 200
assert 40 + 5 * 20 == 140 and 140 - 40 == 100 and 100 / 5 == 20 and 5 * 3.6 == 18


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


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def um():
        y = 640
        vx = F.pista(c, t, C["s01.a"], 260, 1660, y, 0, 300, list(range(0, 301, 40)), "km", size=34)
        ta = C["s01.c"] + 0.4
        pos = lambda s: 20 + 240 * ease_io(min(1.0, s / 2.5))
        F.movel(c, t, ta, vx, y, pos, w=180) if t >= C["s01.a"] else None
        E.foco(c, t, C["s01.a"] + 0.2, 0.4, lambda a: E.pilula(c, "km 20", vx(20), y + 150, 42, "g", fundo=TINTA, a=a))
        E.frase(c, t, C["s01.b"], [("sempre", "i", 72)], XE, 260)
        E.foco(c, t, C["s01.b"] + 0.3, 0.5, lambda a: F.medida(c, 80, "km/h", XE + 250, 260, 96, COR, a))
        E.foco(c, t, C["s01.c"], 0.5, lambda a: F.cronometro(c, 1560, 260, 80, 3 * 15 * ease_io(prog(t, C["s01.c"], 2.5)) / 15 * 20, a, "3 h"))
        E.foco(c, t, C["s01.d"], 0.4, lambda a: E.pilula(c, "km 240?", vx(240), y - 230, 52, "g", fundo=ERRADO, a=a))
        if t >= C["s01.e"]:
            E.risco(c, vx(240) - 120, y - 200, vx(240) + 120, y - 260, t, C["s01.e"], largura=9)
        E.foco(c, t, C["s01.e"] + 0.5, 0.5, lambda a: E.pilula(c, "km 260", vx(260), y + 150, 56, "g", fundo=CERTO, a=a))
    E.saida(c, t, C["s02"] - 0.1, um)
    if t >= C["s02"]:
        promessa(c, t, C, "s02", (("s02.a", "a fórmula da posição", 1.4), ("s02.b", "achar a posição", 0), ("s02.c", "achar o tempo", 0)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    lembrete(c, t, C, "s03", (("s03.b", "deslocamento:", "final − inicial"), ("s03.c", "função afim:", "f(x) = b + a·x"),
                              ("s03.d", "de km/h para m/s:", "divida por 3,6")))


# ---------------- movimento uniforme ----------------
def b_mu(c, t, C, b):
    y = 800
    vx = F.pista(c, t, C["s04"], 220, 1700, y, 0, 280, list(range(0, 281, 40)), "km", size=34)
    t0 = C["s04.c"]
    horas = [(t0 + 0.9 * h, 20 + 80 * h, f"{h} h") for h in range(4)]
    pos = lambda s: 20 + 80 * min(3.0, s / 0.9)
    F.movel(c, t, t0, vx, y, pos, w=170, rastro=horas[:-1]) if t >= C["s04"] + 0.4 else None
    if t < C["s05"]:
        for h in range(3):
            E.salto(c, t, C["s04.d"] + 0.5 * h, vx(20 + 80 * h), vx(100 + 80 * h), y - 200, 70, F.VEL, "+80", size=48)
        E.frase(c, t, C["s04"], [("movimento", "g", 84, COR), ("uniforme", "g", 84, COR)], XE, 220, passo=0.14)
        E.frase(c, t, C["s04.a"], [("velocidade", "i", 70), ("constante", "g", 66)], XE, 330, passo=0.12)
        E.frase(c, t, C["s04.b"], ps("distâncias iguais em tempos iguais", "i", 60, TINTA2), XE, 410, passo=0.1)
        return
    E.foco(c, t, C["s05"], 0.3, lambda a: centro(c, "3 h", vx(260), y - 160, 40, "b", TINTA, a))
    q = ep(t, C["s05.a"], 0.5)
    if q > 0:
        M.line(c, vx(20), y - 260, vx(260), y - 260, F.VEL, q, 5)
        for xx in (vx(20), vx(260)):
            M.line(c, xx, y - 280, xx, y - 240, F.VEL, q, 5)
        F.medida(c, 240, "km", (vx(20) + vx(260)) / 2, y - 285, 56, F.VEL, q, "center")
    E.foco(c, t, C["s05.b"], 0.4, lambda a: E.pilula(c, "saiu do km 20", vx(20) + 60, y + 120, 42, "g", fundo=TINTA, a=a))
    E.formula_em(c, t, C["s05.c"], "20 + 240 = 260", W / 2, 260, 100, "g", TINTA, "center")
    E.frase(c, t, C["s05.d"], [("240:", "g", 60, F.VEL)] + ps("o quanto andou", "i", 62), 300, 1010, "left", 0.1)
    E.frase(c, t, C["s05.e"], [("260:", "g", 60, COR)] + ps("onde ele está", "i", 62), 1060, 1010, "left", 0.1)


# ---------------- a fórmula ----------------
def b_formula(c, t, C, b):
    def s06():
        F.formula_legenda(c, t, C["s06.a"], "s = s₀ + v · t",
                          [("s", "posição no instante t", "m"), ("s₀", "posição inicial, cronômetro em 0", "m"), ("v", "velocidade", "m/s"), ("t", "tempo", "s")],
                          XE, 330, 150, tl=[C["s06.b"], C["s06.c"], C["s06.d"], C["s06.e"]], size_l=56)
        E.foco(c, t, C["s06.f"], 0.5, lambda a: E.pilula(c, "Sistema Internacional", 1500, 300, 48, "g", fundo=E.COR, a=a))
    E.saida(c, t, C["s07"] - 0.1, s06)
    if C["s07"] <= t < C["s08"]:
        def s07():
            E.formula_em(c, t, C["s07"], "s = s₀ + v · t", W / 2, 360, 150, "g", TINTA, "center")
            w = E.formula(None, "s = s₀ + v · t", 0, 0, 150, a=0)
            x0 = W / 2 - w / 2
            wv = E.formula(None, "v · t", 0, 0, 150, a=0)
            ws = E.formula(None, "s₀", 0, 0, 150, a=0)
            xs = x0 + E.formula(None, "s = ", 0, 0, 150, a=0)
            q = ep(t, C["s07.a"], 0.5)
            if q > 0:
                E.chave(c, x0 + w - wv, x0 + w, 420, F.VEL, q, 40)
                centro(c, "o que andou", x0 + w - wv / 2, 540, 56, "i", F.VEL, q)
            q2 = ep(t, C["s07.b"], 0.5)
            if q2 > 0:
                E.chave(c, xs, xs + ws, 420, COR, q2, 40)
                centro(c, "onde começou", xs + ws / 2, 540, 56, "i", COR, q2)
            for i, s in enumerate(("s", "s₀", "v", "t")):
                E.foco(c, t, C["s07.c"] + 0.3 * i, 0.4, lambda a, i=i, s=s: (E.bola(c, 560 + i * 260, 800, 80, a=a), E.formula(c, s, 560 + i * 260, 828, 72, "g", BR, a, "center")))
            E.frase(c, t, C["s07.c"] + 1.4, [("sorvete", "g", 90, COR)], W / 2, 1000, "center")
        E.saida(c, t, C["s08"] - 0.1, s07)
    if t < C["s08"]:
        return
    E.formula_em(c, t, C["s08.a"], "f(x) = b + a · x", W / 2, 260, 100, "g", TINTA2, "center")
    E.formula_em(c, t, C["s08.a"] + 0.6, "s = s₀ + v · t", W / 2, 420, 100, "g", TINTA, "center")
    E.frase(c, t, C["s08.b"], [("s₀", "g", 66, COR), ("=", "g", 66, TINTA2)] + ps("valor inicial, o número sozinho", "i", 60), XE, 580, passo=0.1)
    E.frase(c, t, C["s08.c"], [("v", "g", 66, COR), ("=", "g", 66, TINTA2)] + ps("taxa, o número colado no t", "i", 60), XE, 680, passo=0.1)
    E.formula_em(c, t, C["s08.d"], "s = 10 + 5t", XE, 860, 96, "g", TINTA)
    E.foco(c, t, C["s08.d"] + 1.6, 0.5, lambda a: (F.medida(c, "s₀ = 10", "m", 960, 860, 72, COR, a), F.medida(c, "v = 5", "m/s", 1420, 860, 72, COR, a)))


# ---------------- achar o tempo ----------------
def b_tempo(c, t, C, b):
    def s09():
        E.formula_em(c, t, C["s09.a"], "s = 20 + 80t", XE, 260, 90, "g", TINTA2)
        E.frase(c, t, C["s09.a"] + 0.8, ps("km e h", "i", 56, TINTA2), XE + 640, 260)
        E.frase(c, t, C["s09.b"], [("quando", "i", 70), ("chega", "i", 70), ("ao", "i", 70), ("km 340?", "g", 70, COR)], XE, 400, passo=0.12)
        conta(c, t, [(C["s09.c"], "340 = 20 + 80t"), (C["s09.d"], "320 = 80t")], XE, 580, 96)
        E.foco(c, t, C["s09.d"] + 0.4, 0.4, lambda a: E.escreve(c, "− 20 dos dois lados", 860, 710, 50, "i", TINTA2, a))
        E.formula_em(c, t, C["s09.e"], "t = 320 ÷ 80", XE, 840, 96, "g", TINTA)
        bola_txt(c, t, C["s09.e"] + 1.0, "4 h", 1500, 800, 110, 72)
    E.saida(c, t, C["s10"] - 0.1, s09)
    if t < C["s10"]:
        return
    y = 520
    vx = F.pista(c, t, C["s10"], 300, 1620, y, 0, 100, list(range(0, 101, 20)), "m", size=40)
    if t < C["s11"]:
        F.movel(c, t, C["s10.e"] + 0.6, vx, y, lambda s: 100 - 5 * min(s, 6), w=170) if t >= C["s10.a"] else None
        F.vetor(c, t, C["s10.a"] + 0.3, (vx(90), y - 200), (vx(50), y - 200), None, None, F.VEL, 11)
        E.foco(c, t, C["s10.a"] + 0.6, 0.4, lambda a: centro(c, "posições diminuem", vx(70), y - 240, 48, "i", TINTA2, a))
        E.frase(c, t, C["s10.b"], [("v", "g", 76, COR), ("negativa:", "i", 76), ("retrógrado", "g", 76, COR)], XE, 780, passo=0.12)
        E.frase(c, t, C["s10.d"], [("v", "g", 66), ("positiva:", "i", 66), ("progressivo", "g", 66)], XE, 890, passo=0.12)
        E.formula_em(c, t, C["s10.e"], "s = 100 − 5t", XE, 250, 90, "g", TINTA)
        return
    E.formula_em(c, t, C["s10"], "s = 100 − 5t", XE, 250, 90, "g", TINTA)
    F.carrinho(c, vx(0), y, 170) if t >= C["s11.d"] else F.movel(c, t, C["s11"], vx, y, lambda s: 100 - 100 * ease_io(min(1.0, s / 4)), w=170)
    E.foco(c, t, C["s11.a"], 0.4, lambda a: E.pilula(c, "origem: s = 0", vx(0) + 40, y - 170, 44, "g", fundo=E.COR, a=a))
    conta(c, t, [(C["s11.b"], "0 = 100 − 5t"), (C["s11.c"], "5t = 100")], XE, 760, 84, 120)
    bola_txt(c, t, C["s11.d"], "20 s", 1300, 800, 110, 72)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s12"], [("cuidado", "g", 96, ERRADO)], XE, 200)
    E.frase(c, t, C["s12.a"], ps("misturar unidades", "i", 72), XE + 480, 200, passo=0.12)

    def s12():
        E.frase(c, t, C["s12.b"], [("s₀", "g", 70, COR), ("=", "g", 70, TINTA2), ("50", "g", 70), ("m", "b", 56, F.UNID)], XE, 360, passo=0.12)
        E.frase(c, t, C["s12.c"], [("v", "g", 70, COR), ("=", "g", 70, TINTA2), ("54", "g", 70), ("km/h", "b", 56, ERRADO)], XE + 560, 360, passo=0.12)
        E.frase(c, t, C["s12.d"], [("t", "g", 70, COR), ("=", "g", 70, TINTA2), ("10", "g", 70), ("s", "b", 56, ERRADO)], XE + 1130, 360, passo=0.12)
        E.foco(c, t, C["s12.e"], 0.5, lambda a: E.formula(c, "50 + 54 · 10 = 590 ?", W / 2, 640, 110, "g", ERRADO, a, "center"))
        if t >= C["s12.e"] + 2.0:
            E.risco(c, W / 2 - 560, 660, W / 2 + 560, 560, t, C["s12.e"] + 2.0, largura=12)
        E.foco(c, t, C["s12.e"] + 1.2, 0.4, lambda a: E.pilula(c, "km/h com segundo", W / 2, 820, 52, "g", fundo=ERRADO, a=a))
    E.saida(c, t, C["s13"] - 0.1, s12)
    if t < C["s13"]:
        return
    E.formula_em(c, t, C["s13.a"], "54 ÷ 3,6 = 15 m/s", XE, 380, 96, "g", TINTA)
    E.formula_em(c, t, C["s13.b"], "s = 50 + 15 · 10", XE, 560, 96, "g", TINTA)
    bola_txt(c, t, C["s13.c"], "200 m", 1400, 520, 120, 66, CERTO)
    E.frase(c, t, C["s13.d"], ps("antes da fórmula:", "i", 66) + [("mesmas unidades", "g", 66, COR)], W / 2, 860, "center", 0.12)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def s14():
        E.frase(c, t, C["s14"], ps("agora, o atalho", "i", 76, CLARO), W / 2, 160, "center")
        E.frase(c, t, C["s14.a"], ps("a função já entrega as respostas", "i", 66, CLARO), W / 2, 280, "center", 0.1)
        E.frase(c, t, C["s14.b"], [("número", "g", 64, BR), ("sozinho:", "g", 64, BR)] + ps("posição inicial", "i", 64, CLARO), XE, 420, passo=0.1)
        E.frase(c, t, C["s14.c"], [("colado", "g", 64, BR), ("no", "g", 64, BR), ("t:", "g", 64, BR)] + ps("velocidade", "i", 64, CLARO), XE, 520, passo=0.1)
        E.frase(c, t, C["s14.d"], [("sinal:", "g", 64, BR)] + ps("progressivo ou retrógrado", "i", 64, CLARO), XE, 620, passo=0.1)
        E.formula_em(c, t, C["s14.e"], "s = 8 − 3t", W / 2, 820, 120, "g", BR, "center")
        for i, (s, x, k) in enumerate((("8 m", 760, 0.6), ("−3 m/s", 1160, 1.4), ("retrógrado", 1500, 2.2))):
            pilula_em(c, t, C["s14.e"] + k, s, x, 950, 48, E.COR)
    E.saida(c, t, C["s15"] - 0.1, s14)
    if t < C["s15"]:
        return
    E.formula_em(c, t, C["s15.a"], "s = s₀ + v · t", W / 2, 280, 110, "g", BR, "center")
    E.formula_em(c, t, C["s15.b"], "s = −3t + 8", W / 2, 520, 110, "g", CLARO, "center")
    E.frase(c, t, C["s15.b"] + 1.4, ps("o colado no t continua sendo a velocidade", "i", 58, CLARO), W / 2, 640, "center", 0.08)
    E.frase(c, t, C["s15.c"], [("não", "g", 64, ERRADO), ("serve:", "i", 66, CLARO)] + ps("velocidade que muda", "i", 66, CLARO), W / 2, 860, "center", 0.12)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s16"], ps("hora de testar", "i", 72, COR), XE, 200)
    E.frase(c, t, C["s16.a"], [("ciclista:", "i", 72)], XE, 360)
    E.formula_em(c, t, C["s16.a"] + 0.3, "s = 40 + 5t", XE + 330, 360, 100, "g", COR)
    E.frase(c, t, C["s16.a"] + 1.4, ps("metros e segundos", "i", 54, TINTA2), XE + 330, 440, passo=0.1)
    E.frase(c, t, C["s16.b"], [("posição", "g", 64), ("inicial?", "g", 64)], XE, 600, passo=0.12)
    E.frase(c, t, C["s16.b"] + 1.0, [("velocidade", "g", 64)] + ps("em m/s e km/h?", "i", 64), XE, 700, passo=0.12)
    E.frase(c, t, C["s16.c"], ps("quando passa por", "i", 64) + [("140 m?", "g", 64, COR)], XE, 860, passo=0.12)
    if t >= C["s17"]:
        E.relogio(c, t, C["s17.a"], cx=1500, cy=600, r=190)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    def s18():
        E.formula_em(c, t, C["s18"], "s = 40 + 5t", W / 2, 230, 100, "g", TINTA2, "center")
        E.frase(c, t, C["s18.a"], [("sozinho:", "i", 66)], XE, 420)
        E.foco(c, t, C["s18.a"] + 0.3, 0.5, lambda a: F.medida(c, "s₀ = 40", "m", XE + 300, 420, 84, COR, a))
        E.frase(c, t, C["s18.b"], [("colado", "i", 66), ("no", "i", 66), ("t:", "i", 66)], XE, 570, passo=0.1)
        E.foco(c, t, C["s18.b"] + 0.3, 0.5, lambda a: F.medida(c, "v = 5", "m/s", XE + 300, 570, 84, COR, a))
        pilula_em(c, t, C["s18.b"] + 1.4, "progressivo", 1300, 545, 50, TINTA)
        E.formula_em(c, t, C["s18.c"], "5 × 3,6 = 18 km/h", XE, 760, 90, "g", TINTA)
    E.saida(c, t, C["s19"] - 0.1, s18)
    if t < C["s19"]:
        return
    conta(c, t, [(C["s19.a"], "140 = 40 + 5t"), (C["s19.b"], "100 = 5t")], XE, 380, 100)
    E.formula_em(c, t, C["s19.c"], "t = 100 ÷ 5", XE, 700, 100, "g", TINTA)
    bola_txt(c, t, C["s19.c"] + 1.0, "20 s", 1350, 560, 130, 80)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def s20():
        resumo(c, t, C, "s20", (("s20.a", [("posição", "g", 70), ("=", "g", 70, TINTA2), ("começo", "i", 70), ("+", "g", 70, TINTA2), ("o", "i", 70), ("que", "i", 70), ("andou", "i", 70)]),
                                ("s20.b", [("s = s₀ + v · t", "g", 70, COR)]),
                                ("s20.c", [("tudo", "i", 70), ("nas", "i", 70), ("mesmas", "g", 70), ("unidades", "g", 70)])))
    E.saida(c, t, C["s21"] - 0.1, s20)
    if t < C["s21"]:
        return
    E.frase(c, t, C["s21"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C["s21.a"], [("onde", "g", 100, COR), ("e", "i", 100), ("quando", "g", 100, COR)], XE, 410, passo=0.14)
    E.frase(c, t, C["s21.a"] + 0.6, ps("dois carros se encontram", "i", 76), XE, 530, passo=0.12)
    y = 900
    if t >= C["s21.b"]:
        F.chao(c, 160, 1100, y, ep(t, C["s21.b"], 0.4))
    q = ease_io(prog(t, C["s21.b"], 2.0))
    E.foco(c, t, C["s21.b"], 0.4, lambda a: (F.carrinho(c, lerp(300, 520, q), y, 200, a=a), F.carrinho(c, lerp(960, 810, q), y, 200, a=a, sentido=-1)))
    fim_inscreva(c, t, C, "s21", "s21.c", "s21.d")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, mu=b_mu, formula=b_formula, tempo=b_tempo, erro=b_erro, atalho=b_atalho,
              questao=b_questao, resposta=b_resposta, fim=b_fim)
