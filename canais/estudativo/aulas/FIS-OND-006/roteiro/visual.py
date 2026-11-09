"""Visual — Estudativo · FIS-OND-006: som — altura, intensidade e timbre.
Linguagem visual da trilha Ondas e Som: docstring do visual.py da FIS-OND-001. Nesta aula: grave/agudo = onda mais
espaçada/apertada (mesma altura no desenho); forte/fraco = onda mais alta/baixa (mesmo λ), sempre lado a lado;
longitudinal = faixas verticais que se apertam; timbre = soma de senoides (onda() com harmônicos), mesma frequência.
Todo instante vem de C[...] (marcadores do roteiro)."""
import math

import editorial as E
import fisica as F
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Física", "Ondas e Som")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_FIS-OND-006_som_altura_intensidade_timbre.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("som", "altura", "intensidade", "timbre", "atalho", "questao", "fim"))
BR = "#FFFFFF"

# todas as contas da aula
assert 10 ** ((80 - 60) / 10) == 100 and 10 * 10 == 100                     # conversa 60 → trânsito 80
assert abs(10 * math.log10(2) - 3) < 0.02 and abs(80 + 10 * math.log10(2) - 83) < 0.02   # duas máquinas ≈ 83 dB
assert 10 ** ((160 - 80) / 10) == 1e8                                       # 160 dB seria 10⁸ vezes uma máquina
assert 10 ** ((90 - 60) / 10) == 1000                                       # atalho: 3 dezenas = mil
assert 110 - 60 == 50 and 10 ** (50 / 10) == 100000                         # questão
assert 440 * 2 == 880 and 220 * 2 == 440


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças (da FIS-OND-001) ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def bola_txt(c, t, t0, s, cx, cy, r, size, cor=None):
    v, _, u = s.partition(" ")
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r * ease_back(prog(t, t0, 0.5)), cor, a),
                                     F.medida(c, v, u, cx, cy + size * 0.36, size, E.SOBRE, a, "center", cor_u=E.SOBRE)))


def conta(c, t, linhas, x, y0, dy, size, align="left", escuro=False):
    tinta = BR if escuro else TINTA
    for i, ln in enumerate(linhas):
        ti, s = ln[0], ln[1]
        prox = linhas[i + 1][0] if i + 1 < len(linhas) else 1e9
        cor = ln[2] if len(ln) > 2 else ((CLARO if escuro else COR) if t < prox else tinta)
        E.formula_em(c, t, ti, s, x, y0 + i * dy, size, "g", cor, align)


def pilula(c, t, t0, s, cx, cy, size, fundo=None, est="g"):
    E.foco(c, t, t0, 0.4, lambda a: E.pilula(c, s, cx, cy, size, est, fundo=fundo, a=a, cor=BR))


def lembrete2(c, t, C, cena, itens, desenhos):
    E.frase(c, t, C[cena] + 0.2, ps("você precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C[cena + ".a"], 0.5, lambda a: E.escreve(c, "2", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C[cena + ".a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 820, 1000
    for i, (k, l1, l2) in enumerate(itens):
        y = 230 + i * 290
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 230, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 58)], x + 44, y + 90)
        E.frase(c, t, C[k] + 0.3, [(l2, "g", 58, COR)], x + 44, y + 170)
        E.foco(c, t, C[k] + 0.6, 0.5, lambda a, i=i, y=y: desenhos[i](a, x + w - 170, y + 115))
    q1 = ease_io(prog(t, C[itens[1][0]] - 0.35, 0.5))
    E.cursor(c, x + w - 30, lerp(430, 720, q1), ep(t, C[itens[0][0]], 0.4))
    E.frase(c, t, lerp(C[itens[1][0]], C[cena + ".end"], 0.6), ps("faltou alguma?", "i", 56, COR) + ps("procure no canal", "i", 56), 820, 920, "left", 0.12)


def onda(c, t, t0, x0, x1, y, A, lam, cor=None, harm=((1, 1.0),), d=0.8, vel=0.0, largura=7, eixo=True, a=1.0):
    """onda (soma de harmônicos [(n, peso)]) de x0 a x1; A = maior afastamento do desenho; vel em px/s faz correr"""
    if t < t0 or a <= 0:
        return
    cor = cor or E.COR
    n = max(60, int((x1 - x0) / 3))
    desl = vel * (t - t0)
    f = lambda x: sum(w * math.sin(k * 2 * math.pi * (x - desl) / lam) for k, w in harm)
    pico = max(abs(f(x0 + lam * i / 200)) for i in range(200)) or 1
    p = ease_io(prog(t, t0, d))
    if eixo:
        M.line(c, x0 - 20, y, x1 + 20, y, TINTA, 0.3 * a, 3, dash=E.TRACO, progress=p)
    pts = [(x0 + (x1 - x0) * i / n, y - A * f(x0 + (x1 - x0) * i / n) / pico) for i in range(n + 1)]
    F.poli(c, pts, p, cor, a, largura)


def faixas(c, t, t0, x0, x1, y, h, lam, vel=120, cor=None, a=1.0):
    """onda longitudinal: faixas verticais que se apertam (compressão) e se afastam (rarefação)"""
    if t < t0:
        return
    q = ep(t, t0, 0.5) * a
    cor = cor or E.COR
    desl = vel * (t - t0)
    n = 34
    for i in range(n):
        x = x0 + (x1 - x0) * i / (n - 1)
        x += 0.12 * lam * math.sin(2 * math.pi * (x - desl) / lam)
        M.line(c, x, y - h / 2, x, y + h / 2, cor, q, 6)


# ---------------- gancho ----------------
def celular(c, x, y, nivel, a=1.0):
    """celular com a barra de volume (nivel de 0 a 1)"""
    if a <= 0:
        return
    M.rrect(c, x - 140, y - 260, 280, 520, 40, "#1B1B20", a)
    M.rrect(c, x - 120, y - 230, 240, 440, 18, "#2A2A33", a)
    M.rrect(c, x - 22, y - 180, 44, 340, 22, "#55555F", a)
    hh = 340 * nivel
    M.rrect(c, x - 22, y + 160 - hh, 44, hh, 22, E.COR, a)
    E._meio(c, "volume", x, y + 240, 30, "b", BR, a)


def b_gancho(c, t, C, b):
    if t < C["s02"]:
        def um():
            nivel = 1 - 0.7 * ease_io(prog(t, C["s01.a"] + 0.4, 1.2))
            E.foco(c, t, C["s01.a"], 0.5, lambda a: celular(c, 1500, 520, nivel, a))
            E.frase(c, t, C["s01.a"], ps("abaixou o volume:", "i", 76), XE, 280, passo=0.12)
            E.frase(c, t, C["s01.b"], [("mais", "g", 96), ("baixo?", "g", 96, TINTA)], XE, 420, passo=0.15)
            if t >= C["s01.c"]:
                E.risco(c, XE - 10, 430, XE + 560, 340, t, C["s01.c"], largura=12)
            E.frase(c, t, C["s01.d"], [("mais", "g", 96), ("fraco", "g", 96, CERTO)], XE, 590, passo=0.15)
        E.saida(c, t, C["s01.e"] - 0.1, um)
        if t >= C["s01.e"]:
            E.frase(c, t, C["s01.e"], ps("na Física,", "i", 80) + [("som", "g", 80), ("alto", "g", 80, COR)], XE, 330, passo=0.12)
            E.frase(c, t, C["s01.e"] + 0.9, [("=", "g", 110, TINTA2), ("agudo", "g", 120, COR)], XE, 500, passo=0.15)
            onda(c, t, C["s01.e"] + 1.2, XE, 1700, 760, 80, 70, vel=60)
            E.foco(c, t, C["s01.e"] + 1.6, 0.4, lambda a: E.escreve(c, "como um apito", XE, 950, 60, "i", TINTA2, a))
        return
    tb = C["s02.a"] + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1480, 540, 330 * ease_back(prog(t, tb, 0.8)), giro=12 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 88), XE, 280, passo=0.14)
    for i, (k, s) in enumerate((("s02.b", "grave × fraco"), ("s02.c", "decibéis"), ("s02.d", "timbre"))):
        y = 470 + i * 170
        E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, XE + 40, y - 30, 38, a=a), centro(c, str(i + 1), XE + 40, y - 8, 48, "g", BR, a)))
        E.frase(c, t, C[k] + 0.1, [(s, "g", 84, COR if i == 0 else TINTA)], XE + 110, y)


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    def desenho_onda(a, x, y):
        onda(c, 99, 0, x - 200, x + 80, y - 10, 40, 140, d=0.01, largura=5, a=a, eixo=False)

    def db(a, x, y):
        for i, h in enumerate((50, 120)):
            M.rrect(c, x - 40 + i * 90, y + 60 - h, 70, h, 8, E.COR if i else TINTA2, a)
    lembrete2(c, t, C, "s03", (("s03.b", "da onda:", "A, λ e f"), ("s03.c", "decibéis:", "+10 dB = ×10")), (desenho_onda, db))


# ---------------- o som ----------------
def b_som(c, t, C, b):
    E.frase(c, t, C["s04"], [("som", "g", 110, COR)], XE, 240)
    E.frase(c, t, C["s04.a"], ps("onda", "i", 70) + [("mecânica", "g", 70), ("e", "i", 70), ("longitudinal", "g", 70)], XE, 360, passo=0.12)
    if t < C["s04.c"]:
        faixas(c, t, C["s04.a"] + 0.6, 900, 1760, 600, 200, 220)
        E.foco(c, t, C["s04.a"] + 1.0, 0.4, lambda a: (centro(c, "o ar vai e vem", 1330, 780, 52, "i", TINTA2, a)))
        F.seta(c, 1100, 860, 1560, 860, TINTA2, ep(t, C["s04.a"] + 1.0, 0.4), 6)
        E.frase(c, t, C["s04.b"], ps("no ar:", "i", 70) + [("340", "g", 76, COR), ("m/s", "b", 56, F.UNID)], XE, 520, passo=0.12)
        return
    # faixa do audível
    x0, x1, y = 560, 1340, 650
    E.frase(c, t, C["s04.c"] - 0.4, ps("o ouvido escuta", "i", 70), XE, 500, passo=0.12)
    q = ep(t, C["s04.c"], 0.6)
    M.rrect(c, x0, y - 40, (x1 - x0) * q, 80, 40, E.COR, q)
    E.foco(c, t, C["s04.c"], 0.4, lambda a: (M.line(c, x0, y - 70, x0, y + 70, TINTA, a, 5), F.medida(c, 20, "Hz", x0, y + 150, 70, TINTA, a, "center")))
    E.foco(c, t, C["s04.d"], 0.4, lambda a: (M.line(c, x1, y - 70, x1, y + 70, TINTA, a, 5), F.medida(c, "20.000", "Hz", x1, y + 150, 70, TINTA, a, "center")))
    E.foco(c, t, C["s04.d"] + 0.3, 0.4, lambda a: E._meio(c, "audível", (x0 + x1) / 2, y, 56, "g", BR, a))
    E.foco(c, t, C["s04.e"], 0.5, lambda a: (M.rrect(c, 170, y - 40, 330, 80, 40, TINTA2, a), E._meio(c, "infrassom", 335, y, 48, "g", BR, a)))
    E.foco(c, t, C["s04.f"], 0.5, lambda a: (M.rrect(c, 1400, y - 40, 330, 80, 40, TINTA2, a), E._meio(c, "ultrassom", 1565, y, 48, "g", BR, a)))
    E.foco(c, t, C["s04.f"] + 0.8, 0.4, lambda a: centro(c, "ultrassonografia", 1565, y + 250, 50, "i", TINTA2, a))


# ---------------- altura ----------------
def b_altura(c, t, C, b):
    if t < C["s06"]:
        def s05():
            E.frase(c, t, C["s05.a"], [("altura", "g", 100, COR)], XE, 230)
            E.frase(c, t, C["s05.b"], [("=", "g", 80, TINTA2), ("só", "i", 84), ("a", "i", 84), ("frequência", "g", 80)], XE + 420, 230, passo=0.12)
            for i, (k, s1, s2, lam, s3) in enumerate((("s05.c", "f alta:", "agudo (alto)", 80, "apito"), ("s05.d", "f baixa:", "grave (baixo)", 300, "bumbo"))):
                y = 470 + i * 300
                E.frase(c, t, C[k], [(s1, "g", 60), (s2, "g", 60, COR)], XE, y - 90, passo=0.12)
                onda(c, t, C[k] + 0.3, XE, 1250, y + 40, 60, lam, vel=50)
                kk = "s05.e" if i == 0 else "s05.f"
                pilula(c, t, C[kk], s3, 1520, y + 40, 60, E.COR if i == 0 else TINTA)
        E.saida(c, t, C["s06"] - 0.1, s05)
        return
    E.frase(c, t, C["s06"], ps("cada nota é uma frequência", "i", 76), XE, 230, passo=0.12)
    for i, (k, v, s, lam) in enumerate((("s06.a", "440", "lá", 240), ("s06.b", "880", "o mesmo lá, mais agudo", 120))):
        y = 470 + i * 300
        E.foco(c, t, C[k], 0.5, lambda a, v=v, y=y: F.medida(c, v, "Hz", XE, y - 70, 90, COR, a))
        E.frase(c, t, C[k] + 0.4, ps(s, "i", 60, TINTA2), XE + 360, y - 70, passo=0.1)
        onda(c, t, C[k] + 0.3, XE, 1700, y + 60, 55, lam, vel=40)
    pilula(c, t, C["s06.b"] + 0.8, "f ×2", 1700, 700, 56, E.COR)


# ---------------- intensidade ----------------
def b_intensidade(c, t, C, b):
    if t < C["s08"]:
        E.frase(c, t, C["s07.a"], [("intensidade", "g", 100, COR)], XE, 230)
        E.frase(c, t, C["s07.a"] + 0.8, ps("forte ou fraco: o volume", "i", 64, TINTA2), XE, 330, passo=0.1)
        E.frase(c, t, C["s07.b"], [("=", "g", 80, TINTA2), ("amplitude", "g", 80)], XE + 780, 230, passo=0.12)
        for i, (s, A) in enumerate((("forte", 130), ("fraco", 40))):
            y = 560 + i * 300
            ti = C["s07.c"] + 0.6 * i
            E.foco(c, t, ti, 0.4, lambda a, s=s, y=y, i=i: E.escreve(c, s, XE, y + 25, 70, "g", COR if i == 0 else TINTA2, a))
            onda(c, t, ti, XE + 300, 1700, y, A, 230, vel=40, cor=E.COR if i == 0 else TINTA2)
        return
    if t < C["s09"]:
        def s08():
            E.frase(c, t, C["s08.a"], [("decibéis", "g", 96, COR), ("(dB)", "b", 70, TINTA2)], XE, 230, passo=0.12)
            E.frase(c, t, C["s08.b"], [("+10", "g", 76), ("dB", "b", 56, F.UNID), ("→", "g", 76, TINTA2), ("×10", "g", 76, COR)], XE, 380, passo=0.12)
            # escada: conversa 60, trânsito 80
            base, x = 900, 1100
            for i, (k, v, s) in enumerate((("s08.c", 60, "conversa"), ("s08.d", 80, "trânsito pesado"))):
                h = (v - 40) * 11
                q = ep(t, C[k], 0.5)
                xx = x + i * 330
                if q > 0:
                    M.rrect(c, xx, base - h * q, 250, h * q, 14, E.COR if i else TINTA2, q)
                E.foco(c, t, C[k] + 0.3, 0.4, lambda a, xx=xx, v=v, s=s, h=h: (F.medida(c, v, "dB", xx + 125, base - h - 30, 72, TINTA, a, "center"),
                                                                             centro(c, s, xx + 125, base + 70, 46, "i", TINTA2, a)))
            E.frase(c, t, C["s08.e"] - 1.2, [("+20", "g", 76), ("dB", "b", 56, F.UNID)], XE, 600, passo=0.12)
            E.foco(c, t, C["s08.e"], 0.5, lambda a: E.formula(c, "×10 · ×10 = ×100", XE, 760, 90, "g", COR, a))
        E.saida(c, t, C["s09"] - 0.1, s08)
        return
    E.frase(c, t, C["s09.a"], ps("quando a prova dá a fórmula:", "i", 70), XE, 230, passo=0.12)
    E.formula_em(c, t, C["s09.b"], "β = 10 · log f{I}{I₀}", W / 2, 470, 130, "g", TINTA, "center")
    E.foco(c, t, C["s09.b"] + 0.8, 0.4, lambda a: centro(c, "nível, em dB", W / 2 - 430, 600, 46, "i", COR, a))
    E.frase(c, t, C["s09.c"], [("I", "g", 64, COR)] + ps("o som que chega;", "i", 64) + [("I₀", "g", 64, COR)] + ps("o mais fraco que se ouve (0 dB)", "i", 64),
            W / 2, 740, "center", 0.08)
    E.frase(c, t, C["s09.d"], ps("mas a", "i", 80) + [("regra do 10", "g", 80, COR)] + ps("resolve quase tudo", "i", 80), W / 2, 920, "center", 0.12)


# ---------------- timbre ----------------
VIOLAO = ((1, 1.0), (2, 0.55), (3, 0.35), (4, 0.2))
PIANO = ((1, 1.0), (2, 0.15), (3, 0.5), (5, 0.25))


def b_timbre(c, t, C, b):
    if t < C["s11"]:
        E.frase(c, t, C["s10.a"], [("timbre", "g", 100, COR)], XE, 230)
        E.frase(c, t, C["s10.b"], ps("mesma nota, mesma força", "i", 66, TINTA2), XE + 420, 230, passo=0.1)
        for i, (s, h) in enumerate((("violão", VIOLAO), ("piano", PIANO))):
            y = 520 + i * 300
            ti = C["s10.b"] + 0.6 + 0.6 * i
            E.foco(c, t, ti, 0.4, lambda a, s=s, y=y: E.escreve(c, s, XE, y + 25, 70, "g", TINTA, a))
            onda(c, t, ti, XE + 330, 1700, y, 100, 340, harm=h, vel=40, cor=E.COR if i == 0 else F.NEG)
        pilula(c, t, C["s10.c"], "muda o formato", 1520, 980, 56, E.COR)
        return
    E.frase(c, t, C["s11"], ps("a corda não vibra numa onda só", "i", 70), XE, 200, passo=0.1)
    xs, xe = XE + 300, 1000
    for i, (n, w) in enumerate(VIOLAO):
        y = 330 + i * 150
        ti = C["s11.a"] + 0.5 * i
        E.foco(c, t, ti, 0.4, lambda a, n=n, y=y: E.escreve(c, "principal" if n == 1 else f"×{n}", XE, y + 18, 50, "g", COR if n == 1 else TINTA2, a))
        onda(c, t, ti, xs, xe, y, 55 * w, 340 / n, cor=E.COR if n == 1 else TINTA2, largura=5)
    E.foco(c, t, C["s11.a"] + 1.2, 0.4, lambda a: centro(c, "harmônicos", XE + 100, 900, 50, "i", TINTA2, a))
    E.foco(c, t, C["s11.b"], 0.5, lambda a: (centro(c, "+", 1110, 580, 120, "g", TINTA2, a)))
    onda(c, t, C["s11.b"] + 0.4, 1220, 1800, 560, 120, 290, harm=VIOLAO, largura=8)
    pilula(c, t, C["s11.c"], "esse desenho = timbre", 1510, 800, 56, E.COR)
    E.foco(c, t, C["s11.c"] + 1.0, 0.4, lambda a: centro(c, "(harmônicos: próxima aula)", 1510, 900, 46, "i", TINTA2, a))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s12"], [("cuidado", "g", 96, ERRADO)], XE, 190)
    E.frase(c, t, C["s12.a"], ps("somar decibéis", "i", 76), XE + 480, 190, passo=0.12)
    E.foco(c, t, C["s12.a"] + 1.2, 0.5, lambda a: E.formula(c, "80 dB + 80 dB = 160 dB?", XE, 400, 100, "g", TINTA, a))
    if t >= C["s12.b"] + 0.6:
        E.risco(c, XE - 10, 410, XE + 1270, 310, t, C["s12.b"] + 0.6, largura=12)
    E.frase(c, t, C["s12.c"], [("intensidade", "i", 70), ("×2", "g", 70, COR), ("→", "g", 70, TINTA2), ("só", "i", 70), ("+3", "g", 70, COR), ("dB", "b", 52, F.UNID)],
            XE, 600, passo=0.12)
    E.foco(c, t, C["s12.d"], 0.5, lambda a: F.medida(c, "≈ 83", "dB", XE, 790, 130, CERTO, a))
    E.foco(c, t, C["s12.d"] + 1.2, 0.5, lambda a: E.formula(c, "160 dB = 10^8 vezes uma máquina", XE, 960, 66, "b", TINTA2, a))


# ---------------- atalho (palco) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    E.frase(c, t, C["s13"], ps("agora, o atalho", "i", 76, CLARO), W / 2, 170, "center")
    E.frase(c, t, C["s13.a"], ps("conte as", "i", 80, CLARO) + [("dezenas", "g", 80, BR)], W / 2, 310, "center", 0.12)
    E.frase(c, t, C["s13.b"], [("cada", "i", 64, CLARO), ("+10", "g", 64, BR), ("=", "g", 64, CLARO), ("um", "i", 64, CLARO), ("zero", "g", 64, BR), ("a", "i", 64, CLARO),
                               ("mais", "i", 64, CLARO)], W / 2, 430, "center", 0.1)
    # 60 → 70 → 80 → 90
    for i, v in enumerate((60, 70, 80, 90)):
        x = 420 + i * 360
        ti = C["s13.c"] + 0.5 * i
        E.foco(c, t, ti, 0.4, lambda a, x=x, v=v: E.pilula(c, f"{v} dB", x, 620, 56, "g", fundo=E.COR, a=a, cor=BR))
        if i:
            E.foco(c, t, ti, 0.4, lambda a, x=x: (F.seta(c, x - 260, 620, x - 120, 620, CLARO, a, 6), centro(c, "×10", x - 190, 580, 44, "g", CLARO, a)))
    E.foco(c, t, C["s13.d"], 0.5, lambda a: E.formula(c, "×1.000", W / 2, 810, 120, "g", BR, a, "center"))
    E.frase(c, t, C["s13.e"], [("+7", "g", 60, ERRADO), ("dB?", "g", 60, ERRADO)] + ps("não é dezena:", "i", 60, CLARO) + [("use a fórmula", "g", 58, BR)],
            W / 2, 970, "center", 0.1)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s14"], ps("hora de testar", "i", 72, COR), XE, 200)
    E.frase(c, t, C["s14.a"], [("show", "i", 70)], XE, 340)
    E.foco(c, t, C["s14.a"] + 0.3, 0.5, lambda a: F.medida(c, 110, "dB", XE + 250, 340, 84, COR, a))
    E.frase(c, t, C["s14.a"] + 1.4, [("conversa", "i", 70)], XE, 450)
    E.foco(c, t, C["s14.a"] + 1.7, 0.5, lambda a: F.medida(c, 60, "dB", XE + 330, 450, 84, TINTA, a))
    E.frase(c, t, C["s14.b"], [("quantas", "i", 70), ("vezes?", "g", 70, COR)], XE, 580, passo=0.12)
    E.foco(c, t, C["s14.c"], 0.5, lambda a: (F.medida(c, 220, "Hz", XE, 740, 76, TINTA, a), E.escreve(c, "→", XE + 300, 740, 76, "g", TINTA2, a),
                                             F.medida(c, 440, "Hz", XE + 400, 740, 76, COR, a)))
    E.frase(c, t, C["s14.c"] + 1.6, [("mais", "i", 66), ("forte", "g", 66), ("ou", "i", 66), ("mais", "i", 66), ("agudo?", "g", 66, COR)], XE, 870, passo=0.12)
    if t < C["s15"]:
        E.foco(c, t, C["s14.a"], 0.5, lambda a: celular(c, 1500, 520, 0.9, a))
    else:
        E.relogio(c, t, C["s15.a"], cx=1460, cy=440, r=200)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    E.frase(c, t, C["s16"], [("vamos", "i", 70, COR), ("lá", "i", 70, COR)], XE, 190)
    conta(c, t, [(C["s16.a"], "110 − 60 = 50 dB"), (C["s16.b"], "5 dezenas → 10^5")], XE, 360, 160, 90)
    bola_txt(c, t, C["s16.c"], "×100.000", 1500, 400, 190, 56)
    E.frase(c, t, C["s16.d"], [("f", "g", 80, COR), ("×2", "g", 80)], XE, 720, passo=0.12)
    onda(c, t, C["s16.d"] + 0.2, 600, 1150, 700, 50, 220, cor=TINTA2, largura=5)
    onda(c, t, C["s16.d"] + 0.6, 1250, 1800, 700, 50, 110, largura=5)
    E.frase(c, t, C["s16.e"], [("mais", "i", 76), ("agudo", "g", 76, CERTO), ("não", "i", 76), ("mais", "i", 76), ("forte", "g", 76, ERRADO)], XE, 900, passo=0.12)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s17"], [("resumindo", "i", 92, COR)], W / 2, 180, "center")
        itens = (("s17.a", "altura", "= frequência", "agudo ou grave"), ("s17.b", "intensidade", "= amplitude", "forte ou fraco, dB"),
                 ("s17.c", "timbre", "= formato", "da onda"))
        for i, (k, s1, s2, s3) in enumerate(itens):
            y = 380 + i * 200
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 260, y - 26, 52, a=a), centro(c, str(i + 1), 260, y - 4, 60, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, [(s1, "g", 70, COR), (s2, "g", 70)], 360, y, passo=0.15)
            E.frase(c, t, C[k] + 0.6, ps(s3, "i", 56, TINTA2), 1260, y, passo=0.1)
    E.saida(c, t, C["s18"] - 0.1, resumo)
    if t < C["s18"]:
        return
    E.frase(c, t, C["s18"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C["s18.a"], [("os", "i", 100), ("harmônicos", "g", 110, COR)], XE, 400, passo=0.15)
    for i, (k, s) in enumerate((("s18.b", "cordas"), ("s18.c", "tubos"), ("s18.d", "ressonância"))):
        E.foco(c, t, C[k], 0.4, lambda a, i=i, s=s: E.pilula(c, s, XE + (130, 440, 820)[i], 560, 54, "g", fundo=TINTA, a=a, cor=BR))
    # corda vibrando em 2 fusos
    if t >= C["s18.b"]:
        q = ep(t, C["s18.b"], 0.5)
        x0, x1, y = XE + 20, 1200, 780
        k = math.cos(2 * math.pi * (t - C["s18.b"]) / 0.8)
        pts = [(x0 + (x1 - x0) * i / 100, y - 90 * k * math.sin(2 * math.pi * i / 100)) for i in range(101)]
        F.poli(c, pts, 1.0, E.COR, q, 7)
        for xx in (x0, (x0 + x1) / 2, x1):
            c.drawCircle(xx, y, 12, M.paint(TINTA, q))
    E.foco(c, t, C["s18.e"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 420, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s18.e"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(720, 445, p), ep(t, C["s18.e"] + 0.2, 0.4))
    E.frase(c, t, C["s18.f"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1570, 990, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, som=b_som, altura=b_altura, intensidade=b_intensidade, timbre=b_timbre,
              erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
