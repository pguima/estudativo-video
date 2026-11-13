"""Visual — Estudativo · QUI-ELE-012: meia-vida e datação por carbono-14.
Linguagem visual: a da Química (QUI-MIS-001), a da trilha (QUI-ELE-001) e a da Radioatividade (cabeçalho da QUI-ELE-011).
AMOSTRA = grade de núcleos: os que ainda não decaíram em laranja (PROTON), os que já decaíram em cinza claro (peça local
amostra(), candidata ao kit); a cada meia-vida, metade dos laranjas que sobraram apaga. METADES = cadeia "80 → 40 → 20 → 10"
com a meia-vida em cada seta (peça local metades()). Gráfico da massa pelo tempo com E.plano + E.curva. Carbono-14 em
CPK do carbono (cinza-escuro) com o "14" turquesa. Todo instante vem de C[...]."""
import math
import random

import editorial as E
import quimica as Q
from editorial import W, H, TINTA, TINTA2, CINZA, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Química", "Eletroquímica e Radioatividade")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_QUI-ELE-012_meia_vida_e_carbono_14.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("ideia", "conta", "c14", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
PROTON, APAGADO, BETA = "#E07B39", "#DCDDE0", Q.ELETRON

assert 80 / 2 ** 3 == 10 and 3 * 8 == 24 and 2 * 5730 == 11460 and 3 * 5730 == 17190
assert 100 / 2 ** 3 == 12.5 and 1 / 2 ** 2 == 0.25


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    """palavras de uma frase; sinais (=, −, +, ×, →) vão na grotesca, porque a serifada itálica não tem esses glifos"""
    return [((w, "g", size * 0.9, cor) if w in ("=", "−", "+", "×", "→", "≠") else (w, "b", size * 0.9, cor) if ("-" in w and est == "i") else (w, est, size, cor)) for w in txt.split()]


def pilula_em(c, t, t0, s, cx, cy, size, fundo=None, est="g", cor=BR):
    E.foco(c, t, t0, 0.4, lambda a: E.pilula(c, s, cx, cy, size, est, fundo=fundo, a=a, cor=cor))


def lista(c, t, itens, x, y0, dy, size=66, r=40):
    for i, (ti, partes) in enumerate(itens):
        y = y0 + i * dy
        E.foco(c, t, ti, 0.5, lambda a, i=i, y=y: (E.bola(c, x + r, y - size * 0.38, r, a=a), centro(c, str(i + 1), x + r, y - size * 0.38 + r * 0.42, r * 1.2, "g", E.SOBRE, a)))
        E.frase(c, t, ti + 0.1, partes, x + r * 2 + 40, y, passo=0.1)


_ORDEM = list(range(64))
random.Random(7).shuffle(_ORDEM)


def amostra(c, t, x, y, cols, lins, passo, tl, r=14, a=1.0, tremula=True):
    """grade de núcleos; tl = instante de cada meia-vida: em cada uma, metade dos que restam apaga"""
    n = cols * lins
    ordem = [k for k in _ORDEM if k < n]
    vivos = n
    apaga = {}
    for k, tk in enumerate(tl):
        novos = vivos // 2
        for idx in ordem[n - vivos:n - vivos + novos]:
            apaga[idx] = tk
        vivos -= novos
    for k in range(n):
        cx, cy = x + (k % cols) * passo, y + (k // cols) * passo
        tk = apaga.get(k)
        f = ep(t, tk, 0.5) if tk is not None else 0
        cor = M.mix(PROTON, APAGADO, f)
        dx = 1.5 * math.sin(t * 30 + k) if tremula and f < 1 else 0
        E.bola(c, cx + dx, cy, r, cor, a)


def metades(c, t, tl, vals, x, y, size=90, rot="8 dias", dx=330, cor=None):
    for k, v in enumerate(vals):
        q = ep(t, tl[k], 0.4)
        if q <= 0:
            continue
        xx = x + k * dx
        E.foco(c, t, tl[k], 0.4, lambda a, v=v, xx=xx: E.escreve(c, v, xx, y, size, "g", cor or TINTA, a))
        if k > 0:
            p = ease_io(prog(t, tl[k] - 0.3, 0.4))
            x0 = x + (k - 1) * dx + E.larg(vals[k - 1], "g", size) + 20
            M.arrow(c, x0, y - size * 0.3, lerp(x0, xx - 20, p), y - size * 0.3, E.COR, 1, 5, 18, p)
            if rot:
                E.foco(c, t, tl[k] - 0.2, 0.3, lambda a, x0=x0, xx=xx: centro(c, rot, (x0 + xx) / 2, y - size * 0.75, 36, "b", TINTA2, a))


def carbono14(c, x, y, r, a=1.0):
    Q.atomo(c, x, y, r, "C", a)
    E.escreve(c, "14", x + r * 0.7, y - r * 0.7, r * 0.7, "g", COR, a)


def osso(c, cx, cy, w, a=1.0):
    if a <= 0:
        return
    h = w * 0.22
    M.rrect(c, cx - w / 2, cy - h / 2, w, h, h / 2, "#EDE3C8", a)
    for sx in (-1, 1):
        for sy in (-1, 1):
            c.drawCircle(cx + sx * w / 2, cy + sy * h * 0.55, h * 0.62, M.paint("#EDE3C8", a))
    p = skia.Path(); p.addRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2, cy - h / 2, w, h), h / 2, h / 2))
    c.drawPath(p, M.paint("#BFAF85", 0.6 * a, stroke=3))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    if t < C["s02"]:
        def s01():
            E.foco(c, t, C["s01.a"], 0.5, lambda a: osso(c, 560, 520, 520, a))
            E.frase(c, t, C["s01.a"] + 0.4, ps("um osso numa caverna:", "i", 62), XE, 260, passo=0.1)
            E.foco(c, t, C["s01.a"] + 1.4, 0.4, lambda a: (carbono14(c, 1250, 500, 70, a), E.escreve(c, "1/4", 1380, 530, 150, "g", COR, a)))
            E.foco(c, t, C["s01.a"] + 2.0, 0.4, lambda a: E.escreve(c, "do carbono 14 de quando era vivo", 1080, 640, 46, "b", TINTA2, a))
            bolha = lambda a: (E.bola(c, 1350, 850, 120, E.COR, a), centro(c, "11.500", 1350, 860, 64, "g", BR, a), centro(c, "anos", 1350, 910, 40, "b", BR, a))
            E.foco(c, t, C["s01.c"], 0.5, bolha)
            E.frase(c, t, C["s01.b"], ps("só com isso, a idade", "i", 64), XE, 860, passo=0.1)
            E.frase(c, t, C["s01.d"], [("como?", "g", 70, COR)], XE, 980)
        E.saida(c, t, C["s02"] - 0.1, s01)
        return
    tb = C["s02.a"] + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1580, 560, 230 * ease_back(prog(t, tb, 0.8)), giro=8 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 88), XE, 230, passo=0.14)
    lista(c, t, [(C["s02.b"], [("quanto resta", "g", 62, COR)] + ps("de um material radioativo", "i", 62)),
                 (C["s02.c"], [("quanto tempo", "g", 62)] + ps("passou", "i", 66)),
                 (C["s02.d"], ps("a", "i", 66) + [("idade de um fóssil", "g", 62)]),
                 (C["s02.e"], [("atalho", "g", 62, COR), ("de", "i", 66), ("prova", "i", 66)])], XE, 390, 150, 62)


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], ps("você precisa de", "i", 76, TINTA2) + [("duas", "g", 70, COR), ("coisas", "i", 76, TINTA2)], XE, 200, passo=0.12)
    E.frase(c, t, C["s03.a"], ps("o núcleo radioativo", "i", 64) + [("decai", "g", 60, COR)] + ps("e vira outro", "i", 64), XE, 380, passo=0.1)
    E.frase(c, t, C["s03.b"], [("meia-vida", "g", 64, COR)] + ps("= tempo para cair pela metade", "i", 64), XE, 540, passo=0.1)
    metades(c, t, [C["s03.c"] + 0.3 * k for k in range(4)], ("80", "40", "20", "10"), 300, 780, 100, None)
    E.foco(c, t, C["s03.c"] + 1.4, 0.4, lambda a: E.escreve(c, "miligramas de remédio", 300, 870, 48, "i", TINTA2, a))


# ---------------- a meia-vida radioativa ----------------
def b_ideia(c, t, C, b):
    if t < C["s05"]:
        amostra(c, t, 1150, 300, 8, 8, 70, [C["s04.d"] + 0.4], 22)
        E.frase(c, t, C["s04.a"], ps("os núcleos", "i", 64) + [("não decaem juntos", "g", 60)], XE, 260, passo=0.1)
        E.frase(c, t, C["s04.b"], ps("cada um, numa hora que", "i", 60) + [("ninguém prevê", "g", 56)], XE, 380, passo=0.1)
        E.frase(c, t, C["s04.c"], ps("mas o grupo tem um", "i", 60) + [("ritmo fixo", "g", 56, COR)], XE, 520, passo=0.1)
        E.foco(c, t, C["s04.d"] + 0.6, 0.4, lambda a: E.pilula(c, "metade já decaiu", 1395, 880, 50, "g", fundo=PROTON, a=a))
        E.frase(c, t, C["s04.e"], ps("esse tempo é a", "i", 64) + [("meia-vida", "g", 64, COR)], XE, 700, passo=0.1)
        return
    E.frase(c, t, C["s05.a"], ps("não muda com", "i", 64) + [("calor, pressão", "g", 60)] + ps("nem tamanho da amostra", "i", 64), XE, 300, passo=0.1)
    E.frase(c, t, C["s05.b"], ps("é uma marca de", "i", 64) + [("cada isótopo", "g", 60, COR)], XE, 430, passo=0.1)
    E.foco(c, t, C["s05.c"], 0.4, lambda a: (E.bola(c, 420, 700, 110, "#6B2FA0", a), centro(c, "I-131", 420, 720, 60, "g", BR, a)))
    E.foco(c, t, C["s05.c"] + 0.4, 0.4, lambda a: E.escreve(c, "iodo 131, exames da tireoide", 600, 690, 56, "i", TINTA, a))
    E.foco(c, t, C["s05.c"] + 1.2, 0.4, lambda a: E.pilula(c, "meia-vida: cerca de 8 dias", 880, 800, 54, "g", fundo=E.COR, a=a))


# ---------------- a conta ----------------
def b_conta(c, t, C, b):
    tl = [C["s06.a"], C["s06.b"], C["s06.c"], C["s06.d"]]
    metades(c, t, tl, ("80 mg", "40", "20", "10 mg"), 200, 460, 110, "8 dias", 420)
    amostra(c, t, 1320, 640, 8, 4, 60, [C["s06.b"], C["s06.c"], C["s06.d"]], 20)
    if t < C["s07"]:
        E.frase(c, t, C["s06"], ps("iodo 131, meia-vida de", "i", 60, TINTA2) + [("8 dias", "g", 56)], XE, 220, passo=0.1)
        E.frase(c, t, C["s06.e"], ps("metade do que", "i", 60) + [("sobrou", "g", 56, COR)] + ps("não da inicial", "i", 60), XE, 720, passo=0.1)
        return
    E.foco(c, t, C["s07.a"], 0.4, lambda a: E.pilula(c, "3 metades", 700, 640, 56, "g", fundo=E.COR, a=a))
    E.foco(c, t, C["s07.b"], 0.4, lambda a: E.escreve(c, "3 meias-vidas", 300, 800, 64, "g", TINTA, a))
    E.foco(c, t, C["s07.c"], 0.4, lambda a: E.formula(c, "3 × 8 = 24 dias", 300, 920, 84, "g", COR, a))
    E.frase(c, t, C["s07.e"], ps("tempo =", "i", 54) + [("metades × meia-vida", "g", 50)], 1100, 960, passo=0.1)


# ---------------- gráfico ----------------
def b_grafico(c, t, C, b):
    P = E.plano(c, t, C["s08"], 300, 230, 1200, 680, 0, 40, 0, 80, passo=8, passo_y=20, nomes=("t (dias)", "massa (mg)"), size=36)
    E.curva(c, t, C["s08.a"], P, lambda x: 80 * 0.5 ** (x / 8), 0, 40, d=2.5)
    for k, (x, y) in enumerate(((8, 40), (16, 20), (24, 10))):
        E.ponto(c, t, C["s08.c"] + 0.4 * k, P, x, y, None, guias=True)
    E.foco(c, t, C["s08.b"], 0.4, lambda a: E.pilula(c, "cai rápido, depois devagar", 1250, 300, 46, "g", fundo=TINTA, a=a))
    E.foco(c, t, C["s08.c"], 0.4, lambda a: E.pilula(c, "a cada 8 dias, a metade", 1250, 400, 46, "g", fundo=E.COR, a=a))
    E.foco(c, t, C["s08.d"], 0.4, lambda a: E.pilula(c, "na conta, nunca chega a zero", 1250, 500, 46, "g", fundo=TINTA2, a=a))


# ---------------- carbono-14 ----------------
def b_c14(c, t, C, b):
    if t < C["s10"]:
        E.frase(c, t, C["s09.a"], ps("no ar, um pouco do carbono é", "i", 60) + [("carbono-14", "g", 56, COR)], XE, 230, passo=0.1)
        E.foco(c, t, C["s09.a"] + 1.4, 0.4, lambda a: carbono14(c, 1600, 210, 50, a))
        for k, (s, x) in enumerate((("planta absorve", 480), ("animal come", 1000))):
            E.foco(c, t, C["s09.b"] + 0.6 * k, 0.4, lambda a, s=s, x=x: (E.bola(c, x, 560, 120, ("#2FA84F", "#B5742A")[k], a), centro(c, s, x, 740, 48, "g", TINTA, a)))
        if t >= C["s09.b"] + 0.4:
            M.arrow(c, 620, 560, lerp(620, 860, ep(t, C["s09.b"] + 0.4, 0.5)), 560, TINTA2, 1, 6, 22, ep(t, C["s09.b"] + 0.4, 0.5))
        E.foco(c, t, C["s09.c"], 0.4, lambda a: E.pilula(c, "a proporção dentro = a do ar", 760, 880, 50, "g", fundo=E.COR, a=a))
        return
    if t < C["s11"]:
        E.frase(c, t, C["s10.a"], ps("morreu:", "i", 64) + [("para de repor", "g", 60, ERRADO)], XE, 230, passo=0.1)
        E.foco(c, t, C["s10.b"], 0.4, lambda a: (carbono14(c, 380, 450, 60, a), E.escreve(c, "→", 500, 470, 80, "g", TINTA2, a), Q.atomo(c, 680, 450, 60, "N", a), E.escreve(c, "+ β", 780, 470, 70, "g", BETA, a)))
        E.foco(c, t, C["s10.c"], 0.4, lambda a: E.pilula(c, "meia-vida: 5.730 anos", 560, 640, 60, "g", fundo=E.COR, a=a))
        E.frase(c, t, C["s10.d"], ps("menos carbono-14,", "i", 60) + [("mais tempo desde a morte", "g", 56)], XE, 820, passo=0.1)
        amostra(c, t, 1260, 300, 8, 8, 64, [C["s10.b"] + 1.0, C["s10.c"] + 0.6, C["s10.d"]], 20)
        return
    if t < C["s12"]:
        E.foco(c, t, C["s11"], 0.4, lambda a: osso(c, 420, 280, 360, a))
        E.foco(c, t, C["s11.a"], 0.4, lambda a: E.escreve(c, "um quarto do original", 700, 300, 60, "g", TINTA, a))
        metades(c, t, [C["s11.b"], C["s11.b"] + 0.6, C["s11.b"] + 1.2], ("1", "1/2", "1/4"), 300, 560, 110, "5.730 anos", 420)
        E.foco(c, t, C["s11.c"], 0.4, lambda a: E.pilula(c, "2 meias-vidas", 1620, 420, 56, "g", fundo=E.COR, a=a))
        E.foco(c, t, C["s11.d"], 0.4, lambda a: E.formula(c, "2 × 5.730", 300, 800, 90, "g", TINTA2, a))
        E.foco(c, t, C["s11.e"], 0.4, lambda a: E.formula(c, "= 11.460 anos", 820, 800, 90, "g", COR, a))
        return
    E.frase(c, t, C["s12.a"], ps("funciona até cerca de", "i", 64) + [("50 mil anos", "g", 60, COR)], XE, 260, passo=0.1)
    E.frase(c, t, C["s12.b"], ps("depois, sobra carbono-14", "i", 60) + [("de menos", "g", 56)], XE, 380, passo=0.1)
    E.foco(c, t, C["s12.c"], 0.4, lambda a: E.pilula(c, "dinossauro: mais de 66 milhões de anos", 760, 600, 50, "g", fundo=ERRADO, a=a))
    E.foco(c, t, C["s12.d"], 0.4, lambda a: E.escreve(c, "datado por outros isótopos, nas rochas", XE, 760, 56, "i", TINTA, a))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s13"], [("cuidado", "g", 96, ERRADO)], XE, 190)
    E.frase(c, t, C["s13.a"], ps("em duas meias-vidas, acaba tudo?", "i", 62), XE + 450, 190, passo=0.1)

    def errado():
        E.foco(c, t, C["s13.b"], 0.4, lambda a: E.formula(c, "1 − 1/2 − 1/2 = 0", W / 2, 440, 110, "g", ERRADO, a, "center"))
        if t >= C["s13.b"] + 1.2:
            E.risco(c, W / 2 - 480, 460, W / 2 + 480, 360, t, C["s13.b"] + 1.2, largura=12)
    E.saida(c, t, C["s13.c"] - 0.1, errado)
    if t >= C["s13.c"]:
        metades(c, t, [C["s13.c"], C["s13.c"] + 0.6, C["s13.c"] + 1.2], ("1", "1/2", "1/4"), 560, 460, 120, None, 420)
        E.frase(c, t, C["s13.c"] + 0.3, ps("a segunda corta a metade do que", "i", 58) + [("sobrou", "g", 54, COR)], W / 2, 640, "center", 0.1)
    E.foco(c, t, C["s13.d"], 0.4, lambda a: E.pilula(c, "sobra um quarto, não nada", W / 2, 820, 60, "g", fundo=CERTO, a=a))


# ---------------- atalho (palco) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    if t < C["s15"]:
        E.frase(c, t, C["s14"], ps("o atalho de prova", "i", 72, CLARO), W / 2, 170, "center", 0.12)
        E.frase(c, t, C["s14.a"], ps("o que sobrou vira", "i", 62, CLARO) + [("fração", "g", 58, BR)], W / 2, 290, "center", 0.1)
        linhas = ((C["s14.b"], "1/2", "1"), (C["s14.c"], "1/4", "2"), (C["s14.d"], "1/8", "3"), (C["s14.e"], "1/16", "4"))
        for k, (tk, fr_, n) in enumerate(linhas):
            y = 430 + 120 * k
            E.foco(c, t, tk, 0.4, lambda a, fr_=fr_, n=n, y=y: (E.formula(c, fr_, 760, y, 90, "g", BR, a, "right"), E.formula(c, "→", 860, y, 80, "g", CLARO, a), E.escreve(c, n, 980, y, 90, "g", E.CLARO, a), E.escreve(c, "meia-vida" if n == "1" else "meias-vidas", 1060, y, 56, "b", CLARO, a)))
        E.frase(c, t, C["s14.f"], ps("cada meia-vida", "i", 58, CLARO) + [("dobra o número de baixo", "g", 54, BR)], W / 2, 960, "center", 0.1)
        return
    E.frase(c, t, C["s15.a"], ps("e em porcentagem?", "i", 62, CLARO), W / 2, 200, "center", 0.1)
    for k, (tk, pct, fr_) in enumerate(((C["s15.b"], "50%", "1/2"), (C["s15.c"], "25%", "1/4"), (C["s15.d"], "12,5%", "1/8"))):
        x = 500 + 460 * k
        E.foco(c, t, tk, 0.4, lambda a, pct=pct, fr_=fr_, x=x: (E.formula(c, pct, x, 380, 90, "g", BR, a, "center"), E.formula(c, "= " + fr_, x, 490, 80, "g", E.CLARO, a, "center")))
    E.frase(c, t, C["s15.e"], ps("cada meia-vida multiplica por", "i", 58, CLARO) + [("um meio", "g", 54, BR)], W / 2, 650, "center", 0.1)
    E.frase(c, t, C["s15.f"], [("não", "g", 56, ERRADO), ("compensa", "i", 58, CLARO)] + ps("com um terço:", "i", 58, CLARO), W / 2, 790, "center", 0.1)
    pilula_em(c, t, C["s15.g"], "aí, logaritmo, outra aula; na prova, quase sempre 1/2, 1/4, 1/8", W / 2, 910, 42, E.COR)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s16"], ps("hora de testar", "i", 72, COR), XE, 180)
    E.frase(c, t, C["s16.a"], ps("madeira de uma canoa antiga:", "i", 62), XE, 320, passo=0.1)
    E.foco(c, t, C["s16.a"] + 1.2, 0.4, lambda a: (E.formula(c, "12,5%", XE, 500, 150, "g", COR, a), E.escreve(c, "do carbono 14 de uma árvore viva", XE + 520, 480, 50, "b", TINTA2, a)))
    E.foco(c, t, C["s16.b"], 0.4, lambda a: E.pilula(c, "meia-vida: 5.730 anos", 470, 650, 54, "g", fundo=TINTA, a=a))
    E.frase(c, t, C["s16.c"], ps("qual é a idade da canoa?", "i", 64), XE, 820, passo=0.1)
    if t >= C["s17"]:
        E.relogio(c, t, C["s17.a"], cx=1560, cy=600, r=170)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    E.foco(c, t, C["s18.a"], 0.4, lambda a: E.formula(c, "12,5% = 1/8", W / 2, 260, 100, "g", TINTA, a, "center"))
    metades(c, t, [C["s18.b"] + 0.4 * k for k in range(4)], ("100", "50", "25", "12,5"), 330, 480, 110, None, 360)
    E.foco(c, t, C["s18.c"], 0.4, lambda a: E.pilula(c, "3 meias-vidas", W / 2, 620, 60, "g", fundo=E.COR, a=a))
    E.foco(c, t, C["s18.d"], 0.4, lambda a: E.formula(c, "3 × 5.730", W / 2 - 40, 820, 100, "g", TINTA2, a, "right"))
    E.foco(c, t, C["s18.e"], 0.4, lambda a: E.formula(c, "= 17.190 anos", W / 2, 820, 100, "g", COR, a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s19"], [("resumindo", "i", 92, COR)], W / 2, 190, "center")
        lista(c, t, [(C["s19.a"], ps("cada meia-vida corta", "i", 64) + [("metade do que sobrou", "g", 60)]),
                     (C["s19.b"], [("tempo", "g", 60, COR)] + ps("= metades × meia-vida", "i", 64)),
                     (C["s19.c"], ps("o", "i", 64) + [("carbono-14", "g", 60, COR)] + ps("data o que já foi vivo", "i", 64))], 220, 390, 190, 64, 46)
    E.saida(c, t, C["s20"] - 0.1, resumo)
    if t < C["s20"]:
        return
    E.frase(c, t, C["s20"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C["s20.a"], [("fissão", "g", 100, COR), ("e", "i", 100), ("fusão", "g", 100, COR)], XE, 420, passo=0.15)
    E.frase(c, t, C["s20.b"], ps("a usina nuclear e as", "i", 70) + [("estrelas", "g", 66)], XE, 570, passo=0.1)
    E.foco(c, t, C["s20.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 420, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s20.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(720, 445, p), ep(t, C["s20.c"] + 0.2, 0.4))
    E.frase(c, t, C["s20.d"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1520, 990, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, ideia=b_ideia, conta=b_conta, grafico=b_grafico, c14=b_c14, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
