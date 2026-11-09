"""Visual — Estudativo · FIS-CIN-008: posição no MUV, a função do 2º grau.

Segue a LINGUAGEM VISUAL DA FÍSICA do cabeçalho de FIS-CIN-001 (peças em _ferramentas/fisica.py, importado como F).
Nesta aula: a foto estroboscópica do carro na pista (F.movel com rastro de segundo em segundo) mostra 1, 4, 9, 16 m;
a velocidade média aparece como colunas de velocidade que crescem por igual (colunas_v()) com a linha tracejada da média;
a função nova fica grande no alto e cada parte ganha uma linha de legenda (partes()). Bhaskara em linhas de conta.
Todo instante vem de C[...] (marcadores do roteiro)."""
import math

import editorial as E
import fisica as F
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Física", "Cinemática")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_FIS-CIN-008_posicao_no_muv_funcao_do_2_grau.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("media", "funcao", "tempo", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"

s_ = lambda s0, v0, a, t: s0 + v0 * t + a * t * t / 2
# todas as contas da aula
assert [s_(0, 0, 2, t) for t in (1, 2, 3, 4)] == [1, 4, 9, 16]
assert (10 + 30) / 2 == 20 and 20 * 4 == 80 and s_(0, 10, 5, 4) == 80
assert 10 * 4 == 40 and 2 * 16 / 2 == 16 and s_(0, 10, 2, 4) == 56
assert 5 ** 2 - 4 * 1 * (-50) == 225 and math.isqrt(225) == 15 and (-5 + 15) / 2 == 5 and (-5 - 15) / 2 == -10 and s_(0, 5, 2, 5) == 50
assert 40 + 2 * 16 == 72 and 10 + 2 * 4 == 18 and (10 + 18) / 2 == 14 and 14 * 4 == 56
assert 12 * 5 == 60 and 2 * 25 / 2 == 25 and s_(0, 12, 2, 5) == 85 and 12 + 2 * 5 == 22 and (12 + 22) / 2 == 17 and 17 * 5 == 85


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


def colunas_v(c, t, t0, x, yb, v0, v1, n, k, w=70, gap=26, media=None, escuro=False):
    """n colunas de velocidade crescendo por igual de v0 a v1 (k = pixels por m/s); media = instante da linha da média"""
    for i in range(n):
        v = v0 + (v1 - v0) * i / (n - 1)
        q = ease_out(prog(t, t0 + 0.12 * i, 0.4))
        if q > 0:
            M.rrect(c, x + i * (w + gap), yb - v * k * q, w, v * k * q, 8, F.VEL, 0.85)
    if media is not None and t >= media:
        vm = (v0 + v1) / 2
        M.line(c, x - 30, yb - vm * k, x + n * (w + gap) + 10, yb - vm * k, E.COR, 1.0, 6, dash=E.TRACO, progress=ease_io(prog(t, media, 0.6)))
    M.line(c, x - 30, yb, x + n * (w + gap) + 10, yb, BR if escuro else TINTA, ep(t, t0, 0.4), 4)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def um():
        y = 700
        vx = F.pista(c, t, C["s01.a"], 300, 1700, y, 0, 16, [0, 1, 4, 9, 16], "m", size=40)
        ks = ("s01.c", "s01.d", "s01.e", "s01.f")
        marcas = [(C["s01.a"] + 0.2, 0, "")] + [(C[k], (i + 1) ** 2, f"{i + 1} s") for i, k in enumerate(ks)]
        def pos(s):
            # o carro chega a cada marca no instante da fala
            tt = C["s01.a"] + 0.2 + s
            for i in range(4, 0, -1):
                if tt >= C[ks[i - 1]]:
                    if i == 4:
                        return 16
                    return lerp(i * i, (i + 1) ** 2, ease_io(prog(tt, C[ks[i - 1]], max(0.3, C[ks[i]] - C[ks[i - 1]]))))
            return lerp(0, 1, ease_io(prog(tt, C["s01.b"], max(0.3, C["s01.c"] - C["s01.b"]))))
        F.movel(c, t, C["s01.a"] + 0.2, vx, y, pos, w=150, rastro=marcas[:-1])
        E.frase(c, t, C["s01.a"], ps("parte do repouso", "i", 70), XE, 230, passo=0.12)
        E.frase(c, t, C["s01.b"], [("a", "g", 70, F.ACEL), ("=", "g", 70, TINTA2), ("2", "g", 70), ("m/s²", "b", 54, F.UNID)], XE, 340, passo=0.12)
        for i, k in enumerate(ks):
            E.foco(c, t, C[k], 0.4, lambda a, i=i: centro(c, str((i + 1) ** 2), 900 + i * 180, 930, 96, "g", COR, a))
        E.foco(c, t, C["s01.g"], 0.5, lambda a: E.pilula(c, "quadrados perfeitos", 1450, 300, 56, "g", fundo=E.COR, a=a))
    E.saida(c, t, C["s02"] - 0.1, um)
    if t >= C["s02"]:
        promessa(c, t, C, "s02", (("s02.a", "a posição", 1.4), ("s02.a", "o tempo", 2.6), ("s02.b", "atalho sem t²", 0)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    lembrete(c, t, C, "s03", (("s03.b", "função da velocidade:", "v = v₀ + a · t"), ("s03.c", "potência:", "4² = 16"),
                              ("s03.d", "fórmula de Bhaskara:", "equação do 2º grau")))


# ---------------- velocidade média ----------------
def b_media(c, t, C, b):
    def s04():
        E.foco(c, t, C["s04.a"], 0.5, lambda a: E.formula(c, "s = s₀ + v · t ?", XE, 300, 110, "g", TINTA, a))
        E.frase(c, t, C["s04.b"], ps("aqui o v muda o tempo todo", "i", 66), XE, 440, passo=0.1)
        colunas_v(c, t, C["s04.b"] + 0.4, 900, 940, 10, 30, 5, 12, w=90, gap=40)
        E.foco(c, t, C["s04.c"], 0.4, lambda a: E.pilula(c, "pouca", 945, 990, 40, "g", fundo=TINTA, a=a))
        E.foco(c, t, C["s04.d"], 0.4, lambda a: E.pilula(c, "demais", 945 + 4 * 130, 990, 40, "g", fundo=TINTA, a=a))
    E.saida(c, t, C["s05"] - 0.1, s04)
    if C["s05"] <= t < C["s06"]:
        def s05():
            E.frase(c, t, C["s05.a"], [("velocidade", "g", 84, COR), ("média", "g", 84, COR)], XE, 230, passo=0.14)
            E.frase(c, t, C["s05.b"], ps("o valor do meio", "i", 70), XE, 340, passo=0.12)
            colunas_v(c, t, C["s05"] + 0.3, 1100, 900, 10, 30, 5, 14, w=90, gap=40, media=C["s05.b"])
            E.formula_em(c, t, C["s05.c"], "média = f{v₀ + v}{2}", XE, 560, 110, "g", TINTA)
            E.formula_em(c, t, C["s05.d"], "Δs = média · t", XE, 820, 110, "g", COR)
        E.saida(c, t, C["s06"] - 0.1, s05)
    if t < C["s06"]:
        return
    E.frase(c, t, C["s06.a"], [("10", "g", 70), ("→", "g", 70, TINTA2), ("30", "g", 70), ("m/s", "b", 54, F.UNID)], XE, 260, passo=0.12)
    E.frase(c, t, C["s06.b"], [("em", "i", 70), ("4", "g", 70), ("s", "b", 54, F.UNID)], XE + 520, 260, passo=0.12)
    E.formula_em(c, t, C["s06.c"], "f{10 + 30}{2} = 20", XE, 480, 100, "g", TINTA)
    E.formula_em(c, t, C["s06.d"], "20 · 4", XE, 760, 100, "g", TINTA)
    bola_txt(c, t, C["s06.d"] + 1.0, "80 m", 800, 720, 120, 70)
    colunas_v(c, t, C["s06.a"], 1150, 900, 10, 30, 5, 14, w=90, gap=40, media=C["s06.c"])


# ---------------- a função da posição ----------------
FORM = "s = s₀ + v₀ · t + f{a · t^2}{2}"


def b_funcao(c, t, C, b):
    if t < C["s09"]:
        E.formula_em(c, t, C["s07.a"], "v = v₀ + a · t", XE, 230, 70, "g", TINTA2)
        E.formula_em(c, t, C["s07.b"], FORM, W / 2, 470, 130, "g", TINTA, "center")
        w = E.formula(None, FORM, 0, 0, 130, a=0)
        x0 = W / 2 - w / 2
        partes = (("s08.a", "s₀", "posição inicial"), ("s08.b", "v₀ · t", "o que andaria sem acelerar"), ("s08.c", "f{a · t^2}{2}", "o que a aceleração acrescenta"))
        for i, (k, f_, s) in enumerate(partes):
            y = 700 + i * 110
            E.foco(c, t, C[k], 0.5, lambda a, f_=f_, y=y: E.formula(c, f_, 560, y, 64, "g", COR, a, "right"))
            E.frase(c, t, C[k] + 0.2, ps(s, "i", 60), 600, y, passo=0.08)
        E.foco(c, t, C["s08.d"], 0.5, lambda a: E.pilula(c, "t² : o tempo pesa duas vezes", W / 2, 1010, 44, "b", fundo=TINTA, a=a) if t < C["s08.e"] else None)
        pilula_em(c, t, C["s08.e"], "sorvetão", W / 2 + 560, 300, 64, E.COR)
        return
    if t < C["s10"]:
        E.formula_em(c, t, C["s09"], FORM, W / 2, 260, 96, "g", TINTA2, "center")
        E.frase(c, t, C["s09.a"], [("s₀ = 0,", "g", 70), ("v₀ = 0,", "g", 70), ("a = 2", "g", 70, F.ACEL)], W / 2, 430, "center", 0.2)
        E.formula_em(c, t, C["s09.b"], "s = f{2 · t^2}{2}", W / 2 - 160, 650, 120, "g", TINTA, "right")
        E.formula_em(c, t, C["s09.c"], "= t^2", W / 2 - 120, 650, 140, "g", COR)
        E.frase(c, t, C["s09.d"], [("1,", "g", 80, COR), ("4,", "g", 80, COR), ("9,", "g", 80, COR), ("16", "g", 80, COR)], W / 2, 900, "center", 0.2)
        return
    E.frase(c, t, C["s10.a"], [("v₀", "g", 66, F.VEL), ("=", "g", 66, TINTA2), ("10", "g", 66), ("m/s", "b", 50, F.UNID)], XE, 220, passo=0.1)
    E.frase(c, t, C["s10.b"], [("a", "g", 66, F.ACEL), ("=", "g", 66, TINTA2), ("2", "g", 66), ("m/s²", "b", 50, F.UNID)], XE + 450, 220, passo=0.1)
    E.frase(c, t, C["s10.c"], [("t", "g", 66, COR), ("=", "g", 66, TINTA2), ("4", "g", 66), ("s", "b", 50, F.UNID)], XE + 900, 220, passo=0.1)
    E.formula_em(c, t, C["s10.d"], "10 · 4 = 40", XE, 440, 96, "g", TINTA)
    E.formula_em(c, t, C["s10.e"], "f{2 · 16}{2} = 16", XE, 640, 96, "g", TINTA)
    E.formula_em(c, t, C["s10.f"], "40 + 16", XE, 880, 96, "g", TINTA)
    bola_txt(c, t, C["s10.f"] + 1.0, "56 m", 1100, 840, 120, 70)


# ---------------- achar o tempo ----------------
def b_tempo(c, t, C, b):
    def s11():
        E.frase(c, t, C["s11.a"], ps("achar o tempo:", "i", 70) + [("equação", "g", 66, COR), ("do", "i", 70), ("2º", "g", 66, COR), ("grau", "g", 66, COR)], XE, 230, passo=0.1)
        E.frase(c, t, C["s11.b"], [("v₀", "g", 66, F.VEL), ("=", "g", 66, TINTA2), ("5", "g", 66), ("m/s", "b", 50, F.UNID)], XE, 380, passo=0.1)
        E.frase(c, t, C["s11.c"], [("a", "g", 66, F.ACEL), ("=", "g", 66, TINTA2), ("2", "g", 66), ("m/s²", "b", 50, F.UNID)], XE + 450, 380, passo=0.1)
        E.frase(c, t, C["s11.d"], [("s", "g", 66, COR), ("=", "g", 66, TINTA2), ("50", "g", 66), ("m?", "b", 50, F.UNID)], XE + 900, 380, passo=0.1)
        E.formula_em(c, t, C["s11.e"], "50 = 5t + t^2", W / 2, 680, 130, "g", TINTA, "center")
        E.frase(c, t, C["s11.e"] + 1.2, ps("o 2 do á cortou com o ÷2", "i", 54, TINTA2), W / 2, 820, "center", 0.08)
    E.saida(c, t, C["s12"] - 0.1, s11)
    if t < C["s12"]:
        return
    E.formula_em(c, t, C["s12.a"], "t^2 + 5t − 50 = 0", XE, 240, 90, "g", TINTA)
    pilula_em(c, t, C["s12.b"] + 0.4, "Δ da Bhaskara ≠ variação", 1440, 210, 46, ERRADO)
    E.formula_em(c, t, C["s12.c"], "Δ = 25 + 200 = 225", XE, 420, 84, "g", TINTA2)
    E.formula_em(c, t, C["s12.c"] + 1.8, "r{225} = 15", XE + 960, 420, 84, "g", TINTA2)
    E.formula_em(c, t, C["s12.d"], "t = f{−5 + 15}{2} = 5 s", XE, 650, 100, "g", CERTO)
    E.formula_em(c, t, C["s12.e"], "t = f{−5 − 15}{2} = −10", XE, 900, 90, "g", ERRADO)
    if t >= C["s12.f"]:
        E.risco(c, XE - 10, 920, XE + 860, 800, t, C["s12.f"], largura=11)
    E.frase(c, t, C["s12.f"] + 0.3, ps("tempo negativo não serve", "i", 58, ERRADO), 1150, 870, "left", 0.08)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s13"], [("cuidado", "g", 96, ERRADO)], XE, 200)
    E.frase(c, t, C["s13.a"], ps("esquecer o ÷ 2", "i", 72), XE + 480, 200, passo=0.12)
    E.formula_em(c, t, C["s13.b"], "a · t^2 = 2 · 16 = 32", XE, 420, 90, "g", ERRADO)
    E.formula_em(c, t, C["s13.c"], "40 + 32 = 72 m ?", XE, 580, 100, "g", ERRADO)
    if t >= C["s13.d"] - 0.4:
        E.risco(c, XE - 10, 600, XE + 760, 500, t, C["s13.d"] - 0.4, largura=12)
    E.formula_em(c, t, C["s13.d"], "40 + f{32}{2} = 56 m", XE, 800, 100, "g", CERTO)
    E.foco(c, t, C["s13.d"] + 0.8, 0.4, lambda a: E.selo(c, 1200, 770, 60, True, a))
    E.frase(c, t, lerp(C["s13.d"], C["s13.end"], 0.5), ps("sem o ÷2, a aceleração conta em dobro", "i", 58, TINTA2), W / 2, 1000, "center", 0.08)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def s14():
        E.frase(c, t, C["s14"], ps("agora, o atalho", "i", 76, CLARO), W / 2, 160, "center")
        E.frase(c, t, C["s14.a"], ps("tem", "i", 72, CLARO) + [("v₀", "g", 70, BR), ("e", "i", 72, CLARO), ("v?", "g", 70, BR)], W / 2, 290, "center", 0.12)
        E.formula_em(c, t, C["s14.b"], "Δs = f{v₀ + v}{2} · t", W / 2, 470, 110, "g", BR, "center")
        E.frase(c, t, C["s14.c"], [("10", "g", 66, BR), ("→", "g", 66, CLARO), ("18", "g", 66, BR), ("m/s", "b", 50, CLARO)] + ps("em", "i", 66, CLARO) + [("4", "g", 66, BR), ("s", "b", 50, CLARO)],
                W / 2, 680, "center", 0.12)
        E.formula_em(c, t, C["s14.d"], "média 14", W / 2 - 300, 840, 84, "g", CLARO, "center")
        E.formula_em(c, t, C["s14.e"], "14 · 4 = 56", W / 2 + 250, 840, 84, "g", BR, "center")
        E.frase(c, t, C["s14.e"] + 1.2, [("sem", "i", 60, CLARO), ("t²", "g", 56, BR)], W / 2 + 250, 940, "center")
    E.saida(c, t, C["s15"] - 0.1, s14)
    if t < C["s15"]:
        return
    E.frase(c, t, C["s15.a"], ps("o que falta no começo", "i", 66, CLARO) + [("sobra", "g", 66, BR)] + ps("no fim", "i", 66, CLARO), W / 2, 220, "center", 0.1)
    x0, x1, yb, ya, yc = 560, 1360, 700, 440, 570
    q = ease_io(prog(t, C["s15.a"] + 0.5, 0.8))
    if q > 0:
        M.line(c, x0, yb, x1, yb, BR, q, 4)
        M.line(c, x0, 700, lerp(x0, x1, q), lerp(700, ya, q), F.VEL, 1.0, 8)
    if t >= C["s15.a"] + 1.4:
        a = ep(t, C["s15.a"] + 1.4, 0.5)
        M.line(c, x0, yc, x1, yc, E.COR, a, 6, dash=E.TRACO)
        xm = (x0 + x1) / 2
        p1 = skia.Path(); p1.moveTo(x0, 700); p1.lineTo(x0, yc); p1.lineTo(xm, yc); p1.close()
        p2 = skia.Path(); p2.moveTo(xm, yc); p2.lineTo(x1, yc); p2.lineTo(x1, ya); p2.close()
        c.drawPath(p1, M.paint(ERRADO, 0.35 * a)); c.drawPath(p2, M.paint(CERTO, 0.35 * a))
        centro(c, "média", x1 + 110, yc + 16, 46, "i", CLARO, a)
    E.frase(c, t, C["s15.b"], [("só", "i", 64, CLARO), ("no", "i", 64, CLARO), ("MUV", "g", 64, BR)] + ps("(aceleração constante)", "i", 64, CLARO), W / 2, 850, "center", 0.1)
    E.frase(c, t, C["s15.c"], [("sem", "i", 64, CLARO), ("o", "i", 64, CLARO), ("v", "g", 64, BR), ("final:", "i", 64, CLARO), ("sorvetão", "g", 64, BR)], W / 2, 960, "center", 0.1)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s16"], ps("hora de testar", "i", 72, COR), XE, 200)
    E.frase(c, t, C["s16.a"], [("v₀", "g", 76, F.VEL), ("=", "g", 76, TINTA2), ("12", "g", 76), ("m/s", "b", 58, F.UNID)], XE, 380, passo=0.12)
    E.frase(c, t, C["s16.b"], [("a", "g", 76, F.ACEL), ("=", "g", 76, TINTA2), ("2", "g", 76), ("m/s²", "b", 58, F.UNID)], XE, 500, passo=0.12)
    E.frase(c, t, C["s16.c"], [("t", "g", 76, COR), ("=", "g", 76, TINTA2), ("5", "g", 76), ("s", "b", 58, F.UNID)], XE, 620, passo=0.12)
    E.frase(c, t, C["s16.d"], ps("quanto ele anda?", "g", 76), XE, 820, passo=0.12)
    if t < C["s17"]:
        E.foco(c, t, C["s16.a"], 0.5, lambda a: F.carrinho(c, 1450, 640, 320, a=a))
        if t >= C["s16.a"]:
            F.chao(c, 1150, 1800, 640, ep(t, C["s16.a"], 0.4))
    else:
        E.relogio(c, t, C["s17.a"], cx=1460, cy=480, r=200)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    E.frase(c, t, C["s18"], [("sorvetão:", "g", 64, COR)], XE, 220)
    E.formula_em(c, t, C["s18.a"], "12 · 5 = 60", XE, 360, 84, "g", TINTA)
    E.formula_em(c, t, C["s18.b"], "f{2 · 25}{2} = 25", XE, 540, 84, "g", TINTA)
    E.formula_em(c, t, C["s18.c"], "60 + 25", XE, 740, 84, "g", TINTA)
    bola_txt(c, t, C["s18.c"] + 1.0, "85 m", 760, 710, 110, 66)
    q = ep(t, C["s19"], 0.5)
    if q > 0:
        M.rrect(c, 1000, 160, 800, 720, 30, E.COR, 0.1 * q)
        centro(c, "confira pelo atalho", 1400, 240, 52, "i", COR, q)
    E.formula_em(c, t, C["s19.a"], "v = 12 + 2 · 5 = 22", 1400, 400, 70, "g", TINTA, "center")
    E.formula_em(c, t, C["s19.b"], "f{12 + 22}{2} = 17", 1400, 580, 80, "g", TINTA, "center")
    E.formula_em(c, t, C["s19.c"], "17 · 5 = 85", 1400, 790, 84, "g", CERTO, "center")
    E.foco(c, t, C["s19.c"] + 1.0, 0.4, lambda a: E.selo(c, 1700, 760, 50, True, a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def s20():
        E.frase(c, t, C["s20"], [("resumindo", "i", 92, COR)], W / 2, 180, "center")
        E.formula_em(c, t, C["s20.a"], FORM, W / 2, 470, 120, "g", TINTA, "center")
        E.formula_em(c, t, C["s20.b"], "Δs = f{v₀ + v}{2} · t", W / 2, 800, 110, "g", COR, "center")
    E.saida(c, t, C["s21"] - 0.1, s20)
    if t < C["s21"]:
        return
    E.frase(c, t, C["s21"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C["s21.a"], [("distância", "g", 96, COR), ("de", "i", 96), ("frenagem", "g", 96, COR)], XE, 420, passo=0.14)
    E.frase(c, t, C["s21.b"], [("2×", "g", 90), ("velocidade", "i", 84), ("→", "g", 84, TINTA2), ("4×", "g", 90, COR), ("distância", "i", 84)], XE, 600, passo=0.14)
    E.foco(c, t, C["s21.a"] + 0.4, 0.5, lambda a: F.carrinho(c, 620, 900, 280, a=a))
    if t >= C["s21.a"] + 0.4:
        F.chao(c, 160, 1100, 900, ep(t, C["s21.a"] + 0.4, 0.4))
        for k in range(3):
            M.line(c, 200 + k * 60, 880 - k * 3, 440, 880 - k * 3, TINTA2, 0.4 * ep(t, C["s21.a"] + 0.8, 0.4), 5)
    fim_inscreva(c, t, C, "s21", "s21.c", "s21.d")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, media=b_media, funcao=b_funcao, tempo=b_tempo, erro=b_erro, atalho=b_atalho,
              questao=b_questao, resposta=b_resposta, fim=b_fim)
