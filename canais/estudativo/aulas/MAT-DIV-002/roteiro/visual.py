"""Visual — Estudativo · MAT-DIV-002: regras de divisibilidade.
Peças da aula: número com algarismos destacáveis (o teste aponta a casa certa), selo de sim/não, notas de dinheiro para o "trocado" e o placar dos sete testes.
Todo instante vem de C[...]: fala sem cue usa um ponto entre dois cues (lerp), para continuar certo com a voz real."""
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro, linha
import motor as M
import skia

E.usar("Matemática", "Divisibilidade, MMC e MDC")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-DIV-002_regras_divisibilidade.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("final", "soma", "atalho", "questao", "fim"))
BR = "#FFFFFF"
N = "4.572"
DIVS = (2, 3, 4, 5, 6, 9, 10)


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças desta aula ----------------
def num_bola(c, s, cx, cy, r, size, a=1.0, cor=None, tinta=None):
    """número dentro da esfera"""
    E.bola(c, cx, cy + 3, r, cor, a)
    centro(c, s, cx, cy + size * 0.36, size, "g", tinta or E.SOBRE, a)


def bola_entra(c, t, t0, s, cx, cy, r, size, cor=None, tinta=None):
    """esfera com número que chega com salto em t0"""
    q = ease_back(prog(t, t0, 0.5))
    if q > 0.05:
        num_bola(c, s, cx, cy, r * q, max(2, round(size * q)), 1.0, cor, tinta)


def casas(s, cx, size):
    """x inicial de cada caractere de s, centrado em cx, e a largura total"""
    w = E.larg(s, "g", size)
    x0 = cx - w / 2
    ap = E.APERTO["g"] * size
    return [x0 + (E.larg(s[:i], "g", size) + ap if i else 0) for i in range(len(s))], w


def numero(c, s, cx, y, size, cores=None, a=1.0, cor=None):
    """número desenhado caractere a caractere; cores = {índice: cor}"""
    xs, _ = casas(s, cx, size)
    for i, ch in enumerate(s):
        E.escreve(c, ch, xs[i], y, size, "g", (cores or {}).get(i, cor or TINTA), a)


def trecho(c, s, cx, y, size, i0, i1, p, cor=None):
    """caixa pontilhada em volta dos caracteres i0..i1-1 do número"""
    xs, w = casas(s, cx, size)
    x0 = xs[i0]
    x1 = xs[i1] if i1 < len(s) else cx + w / 2
    E.caixa_pontilhada(c, x0 - 14, y - size * 0.86, x1 - x0 + 28, size * 1.02, p, cor or E.COR, prog_=p)


def selo(c, cx, cy, r, ok, a=1.0):
    """sim ou não numa esfera verde ou vermelha"""
    if a <= 0 or r <= 1:
        return
    E.bola(c, cx, cy, r, CERTO if ok else ERRADO, a)
    k, w = r * 0.42, max(5, r * 0.16)
    if ok:
        M.line(c, cx - k, cy + k * 0.05, cx - k * 0.2, cy + k * 0.8, BR, a, w)
        M.line(c, cx - k * 0.2, cy + k * 0.8, cx + k, cy - k * 0.7, BR, a, w)
    else:
        M.line(c, cx - k * 0.8, cy - k * 0.8, cx + k * 0.8, cy + k * 0.8, BR, a, w)
        M.line(c, cx + k * 0.8, cy - k * 0.8, cx - k * 0.8, cy + k * 0.8, BR, a, w)


def selo_entra(c, t, t0, cx, cy, r, ok):
    selo(c, cx, cy, r * ease_back(prog(t, t0, 0.5)), ok, ep(t, t0, 0.2))


def pil(c, t, t0, s, cx, cy, size=64, fundo=None, cor=None):
    """pílula que entra com foco"""
    E.foco(c, t, t0, 0.45, lambda a: E.pilula(c, s, cx, cy, size, estilo="g", fundo=fundo or E.COR, cor=cor or E.SOBRE, a=a))


def teste(c, t, tp, ts, d, ok, cx, cy, size=64):
    """pílula do divisor e, ao lado, o selo do resultado"""
    pil(c, t, tp, f"÷ {d}", cx - size * 0.9, cy, size)
    selo_entra(c, t, ts, cx + size * 1.7, cy, size * 0.9, ok)


def nota(c, x, y, w, h, s, a=1.0, size=None):
    """nota de dinheiro"""
    if a <= 0:
        return
    r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 14, 14)
    c.drawRRect(r, M.paint(E.COR, a))
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x + 10, y + 10, w - 20, h - 20), 8, 8), M.paint(BR, 0.35 * a, stroke=3))
    size = size or h * 0.5
    centro(c, s, x + w / 2, y + h / 2 + size * 0.36, size, "g", BR, a)


def relogio(c, t, t0):
    """relógio de pausa: enche em 3 segundos"""
    r = 210 * ease_back(prog(t, t0, 0.6))
    if r > 0:
        cx, cy = 1490, 440
        E.bola(c, cx, cy, r)
        f = M.clamp(prog(t, t0 + 0.8, 3.0))
        if f > 0:
            E.arco(c, cx, cy, r + 34, -90, 360 * f, TINTA, 10)
        for dx in (-44, 44):
            M.rrect(c, cx + dx - 22, cy - 80, 44, 160, 12, E.SOBRE, ep(t, t0 + 0.2, 0.4))
        E.foco(c, t, t0 + 0.2, 0.5, lambda a: centro(c, "pause o vídeo", cx, cy + r + 120, 64, "i", TINTA, a))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def pergunta():
        s0, a_, b_ = C["s01"], C["s01.a"], C["s01.b"]
        E.frase(c, t, s0 + 0.2, [("o", "i", 96), ("número", "i", 96)], W / 2, 180, "center", passo=0.14)
        E.foco(c, t, a_, 0.5, lambda a: numero(c, N, W / 2, 500, 300, a=a))
        q = lerp(a_, b_, 0.45)
        E.frase(c, t, q, [("se", "i", 96), ("divide", "i", 96), ("por", "i", 96)], 820, 690, "center", passo=0.13)
        pil(c, t, q + 0.45, "9?", 1250, 660, 96)
        E.frase(c, t, b_, [("em", "i", 80), ("poucos", "g", 76, COR), ("segundos,", "g", 76, COR)], W / 2, 860, "center", passo=0.14)
        E.frase(c, t, b_ + 0.5, [("sem", "i", 80), ("armar", "i", 80), ("a", "i", 80), ("conta", "i", 80)], W / 2, 970, "center", passo=0.14)
    E.saida(c, t, C["s02"] - 0.1, pergunta)

    if t >= C["s02"]:
        s0, a_ = C["s02"], C["s02.a"]
        q = ease_back(prog(t, C["s02.b"] - 0.2, 0.7))
        if q > 0:
            E.bola(c, 1480, 540, 290 * q)
        E.frase(c, t, s0 + 0.3, [("até", "i", 90), ("o", "i", 90), ("fim", "i", 90), ("da", "i", 90), ("aula", "i", 90)], XE, 280)
        E.frase(c, t, lerp(s0, a_, 0.45), [("você", "i", 110), ("testa", "g", 110), ("contra", "i", 110)], XE, 430, passo=0.16)
        E.frase(c, t, a_, [("7", "g", 150, COR), ("divisores", "g", 130, COR)], XE, 590)
        for i, d in enumerate(DIVS):
            bola_entra(c, t, a_ + 0.3 + i * 0.1, str(d), XE + 56 + i * 134, 720, 60, 58)
        E.frase(c, t, a_ + 0.8, [("sem", "i", 90), ("dividir", "i", 90), ("nada", "i", 90)], XE, 890, passo=0.14)
        E.foco(c, t, C["s02.b"] + 0.2, 0.5, lambda a: (centro(c, "+ atalho", 1480, 525, 84, "g", E.SOBRE, a),
                                                      centro(c, "de prova", 1480, 610, 84, "i", E.SOBRE, a)))


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"] + 0.35, [("para", "i", 84), ("acompanhar,", "i", 84)], XE, 310)
    E.frase(c, t, lerp(C["s03"], C["s03.a"], 0.65), [("lembre", "i", 84), ("de", "i", 84)], XE, 420)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "2", XE - 8, 730, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 710, 120, "i", TINTA, a))
    x, w = 960, 780
    for i, (k, l1, l2) in enumerate((("s03.b", "O que é", "um divisor"), ("s03.c", "Como somar", "de cabeça"))):
        y = 240 + i * 250
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 196, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 62)], x + 44, y + 84)
        E.frase(c, t, C[k] + 0.3, [(l2, "g", 62, COR)], x + 44, y + 160)
    q = ease_io(prog(t, C["s03.c"] - 0.35, 0.5))
    E.cursor(c, x + w - 30, lerp(410, 660, q), ep(t, C["s03.b"], 0.4))
    E.frase(c, t, lerp(C["s03.c"], C["s03.end"], 0.4), [("procure", "i", 62), ("a", "i", 62), ("aula", "i", 62), ("no", "i", 62), ("canal", "i", 62)], x, 860, passo=0.14)


# ---------------- o que é divisível ----------------
def b_nome(c, t, C, b):
    a_, b_ = C["s04.a"], C["s04.b"]
    E.frase(c, t, a_, [("divisível", "g", 220, COR)], W / 2, 330, "center")
    E.frase(c, t, a_ + 0.5, [("divisão", "i", 96), ("sem", "i", 96), ("resto", "g", 90, CERTO)], W / 2, 470, "center", passo=0.16)
    u, v = lerp(a_, b_, 0.38), lerp(a_, b_, 0.64)
    linha(c, t, [("12", "g", 84, TINTA, u), ("é", "i", 88, TINTA, u + 0.15), ("divisível", "g", 84, COR, u + 0.3), ("por", "i", 88, TINTA, u + 0.5), ("3", "g", 84, TINTA, u + 0.65)], W / 2, 620, "center")
    linha(c, t, [("3", "g", 84, TINTA, v), ("é", "i", 88, TINTA, v + 0.15), ("divisor", "g", 84, COR, v + 0.3), ("de", "i", 88, TINTA, v + 0.5), ("12", "g", 84, TINTA, v + 0.65)], W / 2, 730, "center")
    E.frase(c, t, lerp(a_, b_, 0.86), [("regra", "i", 84), ("de", "i", 84), ("divisibilidade:", "i", 84)], W / 2, 870, "center", passo=0.14)
    E.frase(c, t, b_, [("responde", "g", 84, COR), ("sem", "g", 84, COR), ("dividir", "g", 84, COR)], W / 2, 980, "center", passo=0.14)


# ---------------- último algarismo ----------------
def b_final(c, t, C, b):
    def regras():
        v = C["s05.a"]
        linha(c, t, [("regras", "i", 84, TINTA, v - 0.4), ("que", "i", 84, TINTA, v - 0.3), ("olham", "i", 84, TINTA, v), ("só", "i", 84, TINTA, v + 0.15), ("o", "i", 84, TINTA, v + 0.25),
                     ("último", "g", 80, COR, v + 0.35), ("algarismo", "g", 80, COR, v + 0.5)], W / 2, 180, "center")
        d_, fim = C["s05.d"], C["s05.end"]
        for k, d, nome, digs, y, tb in (("s05.b", 10, "termina em", (0,), 370, None), ("s05.c", 5, "termina em", (0, 5), 570, None), ("s05.d", 2, "termina em", (0, 2, 4, 6, 8), 770, lerp(d_, fim, 0.42))):
            ti = C[k]
            pil(c, t, ti, f"÷ {d}", 290, y - 28, 72)
            E.frase(c, t, ti + 0.1, [(nome, "i", 76)], 460, y)
            if d == 2:
                E.frase(c, t, ti + 0.6, [("par:", "g", 72, COR)], 800, y)
            base = tb if tb else ti + 0.2
            passo_ = 0.16 if tb else 0.5
            for i, n in enumerate(digs):
                bola_entra(c, t, base + i * passo_, str(n), 1040 + i * 160, y - 28, 70, 76)
    E.saida(c, t, C["s06"] - 0.1, regras)

    def trocado():
        s0, a_, b_ = C["s06"], C["s06.a"], C["s06.b"]
        E.frase(c, t, s0 + 0.25, [("por", "i", 92), ("que", "i", 92), ("basta", "i", 92), ("o", "i", 92), ("final?", "g", 86, COR)], W / 2, 180, "center", passo=0.14)
        for i in range(5):
            nota(c, 200 + i * 34, 420 - i * 34, 340, 170, "10", ep(t, a_ + i * 0.12, 0.35), 96)
        E.frase(c, t, a_ + 0.3, [("notas", "g", 72, COR), ("de", "i", 76), ("10", "g", 72, COR)], 200, 660, passo=0.14)
        u = lerp(a_, b_, 0.35)
        E.frase(c, t, u, [("qualquer", "i", 72), ("quantidade", "i", 72)], 830, 340, passo=0.14)
        E.frase(c, t, u + 0.5, [("se", "i", 72), ("divide", "i", 72), ("certinho", "g", 66, CERTO), ("por", "i", 72)], 830, 440, passo=0.14)
        for i, d in enumerate((2, 5, 10)):
            pil(c, t, lerp(u, b_, 0.5 + i * 0.13), f"÷ {d}", 960 + i * 270, 560, 70)
        p = ep(t, b_, 0.4)
        E.foco(c, t, b_ - 0.3, 0.4, lambda a: numero(c, N, W / 2 - 160, 880, 180, {4: COR}, a))
        xs, w = casas(N, W / 2 - 160, 180)
        trecho(c, N, W / 2 - 160, 880, 180, 4, 5, p)
        E.frase(c, t, b_ + 0.2, [("quem", "i", 76), ("decide:", "i", 76)], 1130, 800, passo=0.14)
        E.frase(c, t, b_ + 0.6, [("o", "i", 76), ("trocado", "g", 84, COR)], 1130, 890, passo=0.14)
    if t >= C["s06"]:
        E.saida(c, t, C["s07"] - 0.1, trocado)

    if t >= C["s07"]:
        a_, b_ = C["s07.a"], C["s07.b"]
        E.frase(c, t, C["s07"] + 0.2, [("teste", "i", 90), ("em", "i", 90)], W / 2, 170, "center")
        E.foco(c, t, a_, 0.5, lambda q: numero(c, N, W / 2, 480, 280, {4: COR} if t >= b_ else None, q))
        trecho(c, N, W / 2, 480, 280, 4, 5, ep(t, b_, 0.4))
        E.frase(c, t, b_ + 0.2, [("termina", "i", 84), ("em", "i", 84), ("2", "g", 80, COR)], W / 2, 620, "center", passo=0.14)
        teste(c, t, C["s07.c"], C["s07.c"] + 0.2, 2, True, 440, 780, 84)
        teste(c, t, C["s07.d"], C["s07.d"] + 0.2, 5, False, 960, 780, 84)
        teste(c, t, C["s07.e"], C["s07.e"] + 0.2, 10, False, 1480, 780, 84)


# ---------------- por quatro ----------------
def b_quatro(c, t, C, b):
    def regra():
        a_, fim = C["s08.a"], C["s08.end"]
        pil(c, t, a_, "÷ 4", 350, 220, 110)
        E.frase(c, t, a_ + 0.3, [("olhe", "i", 92), ("os", "i", 92), ("últimos", "g", 86, COR), ("2", "g", 86, COR), ("algarismos", "g", 86, COR)], 560, 250, passo=0.14)
        u = lerp(a_, fim, 0.28)
        E.foco(c, t, a_ + 0.5, 0.5, lambda q: numero(c, N, W / 2, 620, 280, {3: COR, 4: COR} if t >= u else None, q))
        trecho(c, N, W / 2, 620, 280, 3, 5, ep(t, u, 0.4))
        v = lerp(a_, fim, 0.55)
        E.frase(c, t, v, [("ele", "i", 80), ("é", "i", 80), ("divisível", "i", 80), ("por", "i", 80), ("4?", "g", 76, COR)], W / 2, 790, "center", passo=0.14)
        E.frase(c, t, v + 0.8, [("o", "g", 72), ("número", "g", 72), ("inteiro", "g", 72), ("também", "g", 72, CERTO)], W / 2, 900, "center", passo=0.14)
    E.saida(c, t, C["s09"] - 0.1, regra)

    if t >= C["s09"]:
        a_, b_, c_, d_, e_ = C["s09.a"], C["s09.b"], C["s09.c"], C["s09.d"], C["s09.e"]
        E.frase(c, t, C["s09"] + 0.25, [("o", "i", 84), ("motivo", "i", 84), ("é", "i", 84), ("parecido", "g", 78, COR)], XE, 170, passo=0.14)
        nota(c, XE, 250, 360, 180, "100", ep(t, a_, 0.4), 104)
        if t >= a_ + 0.3:
            p = ep(t, a_ + 0.3, 0.5)
            M.arrow(c, 560, 340, 700, 340, TINTA2, p, 6, 20, p)
        for i in range(4):
            nota(c, 730 + i * 240, 270, 216, 140, "25", ep(t, a_ + 0.5 + i * 0.12, 0.35), 80)
        E.frase(c, t, lerp(a_, b_, 0.6), [("25", "g", 72, COR), ("para", "i", 76), ("cada", "i", 76)], 730, 510, passo=0.14)
        E.frase(c, t, b_, [("só", "i", 84), ("falta", "i", 84), ("decidir", "i", 84), ("o", "i", 84), ("final", "g", 78, COR)], XE, 660, passo=0.14)
        y = 880
        E.foco(c, t, c_ - 0.2, 0.4, lambda q: numero(c, N, 420, y, 150, {3: COR, 4: COR}, q))
        trecho(c, N, 420, y, 150, 3, 5, ep(t, c_, 0.4))
        v = lerp(c_, d_, 0.45)
        linha(c, t, [("72", "g", 120, TINTA, v), ("÷", "g", 100, CINZA, v + 0.15), ("4", "g", 120, TINTA, v + 0.3), ("=", "g", 100, CINZA, d_ - 0.15), ("18", "g", 120, COR, d_)], 760, y)
        teste(c, t, e_, e_ + 0.2, 4, True, 1560, y - 40, 72)


# ---------------- por três e por nove ----------------
def b_soma(c, t, C, b):
    def regra():
        a_, b_, fim = C["s10.a"], C["s10.b"], C["s10.end"]
        pil(c, t, a_, "÷ 3", 760, 230, 100)
        pil(c, t, a_ + 0.2, "÷ 9", 1160, 230, 100)
        E.frase(c, t, a_ + 0.5, [("a", "i", 84), ("regra", "i", 84), ("é", "i", 84), ("outra", "i", 84)], W / 2, 400, "center", passo=0.14)
        E.frase(c, t, b_, [("some", "g", 120, COR), ("todos", "g", 120, COR), ("os", "i", 120), ("algarismos", "i", 120)], W / 2, 590, "center", passo=0.14)
        u = lerp(b_, fim, 0.32)
        E.frase(c, t, u, [("soma", "i", 80), ("divisível", "i", 80), ("por", "i", 80), ("3?", "g", 76, COR), ("o", "i", 80), ("número", "i", 80), ("também", "g", 76, CERTO)], W / 2, 770, "center", passo=0.14)
        E.frase(c, t, lerp(b_, fim, 0.78), [("o", "i", 80), ("mesmo", "i", 80), ("vale", "i", 80), ("para", "i", 80), ("o", "i", 80), ("9", "g", 76, COR)], W / 2, 890, "center", passo=0.14)
    E.saida(c, t, C["s11"] - 0.1, regra)

    def conta():
        s0, a_, b_, c_, d_ = C["s11"], C["s11.a"], C["s11.b"], C["s11.c"], C["s11.d"]
        E.foco(c, t, s0 + 0.15, 0.4, lambda q: numero(c, N, W / 2, 270, 170, cor=CINZA if t >= a_ else TINTA, a=q))
        xs, _ = casas(N, W / 2, 170)
        orig = (xs[0], xs[2], xs[3], xs[4])
        destinos = (330, 590, 850, 1110)
        for i, dg in enumerate("4572"):
            ti = a_ + i * 0.28
            if t >= ti:  # o algarismo desce do número até a soma
                q = ease_io(prog(t, ti, 0.45))
                E.escreve(c, dg, lerp(orig[i], destinos[i] - 45, q), lerp(270, 510, q), round(lerp(170, 130, q)), "g", COR)
            if i:
                E.foco(c, t, ti, 0.35, lambda q, i=i: centro(c, "+", destinos[i] - 130, 500, 110, "g", CINZA, q))
        E.foco(c, t, b_ - 0.15, 0.35, lambda q: centro(c, "=", 1250, 500, 110, "g", CINZA, q))
        bola_entra(c, t, b_, "18", 1450, 465, 112, 110)
        u = lerp(b_, c_, 0.55)
        linha(c, t, [("18", "g", 90, TINTA, u), ("÷", "g", 74, CINZA, u + 0.1), ("3", "g", 90, TINTA, u + 0.2), ("=", "g", 74, CINZA, u + 0.3), ("6", "g", 90, COR, u + 0.4)], 200, 720)
        selo_entra(c, t, u + 0.5, 730, 690, 56, True)
        linha(c, t, [("18", "g", 90, TINTA, c_), ("÷", "g", 74, CINZA, c_ + 0.1), ("9", "g", 90, TINTA, c_ + 0.2), ("=", "g", 74, CINZA, c_ + 0.3), ("2", "g", 90, COR, c_ + 0.4)], 960, 720)
        selo_entra(c, t, c_ + 0.5, 1490, 690, 56, True)
        E.frase(c, t, d_, [("o", "i", 90), ("número", "i", 90), ("inteiro", "g", 84, CERTO), ("também", "g", 84, CERTO)], W / 2, 900, "center", passo=0.14)
    if t >= C["s11"]:
        E.saida(c, t, C["s12"] - 0.1, conta)

    if t >= C["s12"]:
        s0, a_, b_, c_, d_ = C["s12"], C["s12.a"], C["s12.b"], C["s12.c"], C["s12.d"]
        E.frase(c, t, s0 + 0.25, [("por", "i", 88), ("que", "i", 88), ("a", "i", 88), ("soma", "g", 82, COR), ("funciona?", "i", 88)], W / 2, 170, "center", passo=0.14)
        u = lerp(c_, d_, 0.42)  # "se dividem certinho"
        v = lerp(c_, d_, 0.8)  # "deixe essa parte de lado"
        for i, (n, m, ti) in enumerate((("10", "9", a_), ("100", "99", b_), ("1.000", "999", c_))):
            y = 340 + i * 150
            E.foco(c, t, ti, 0.4, lambda q, n=n, y=y: centro(c, n, 380, y, 120, "g", TINTA, q))
            E.foco(c, t, ti + 0.15, 0.4, lambda q, y=y: centro(c, "=", 620, y, 100, "g", CINZA, q))
            E.foco(c, t, ti + 0.25, 0.4, lambda q, m=m, y=y: centro(c, m, 840, y, 120, "g", CERTO if t >= u else COR, q * (1 - 0.65 * ep(t, v, 0.4))))
            E.foco(c, t, ti + 0.4, 0.4, lambda q, y=y: centro(c, "+", 1050, y, 100, "g", CINZA, q))
            E.foco(c, t, ti + 0.5, 0.4, lambda q, y=y: centro(c, "1", 1190, y, 120, "g", TINTA, q))
            if t >= v:
                w = E.larg(m, "g", 120) / 2 + 16
                E.risco(c, 840 - w, y - 12, 840 + w, y - 62, t, v + i * 0.12, largura=9)
        pil(c, t, u, "÷ 9", 1490, 300, 72, CERTO, BR)
        pil(c, t, u + 0.2, "÷ 3", 1490, 440, 72, CERTO, BR)
        E.frase(c, t, u + 0.4, [("certinho", "g", 66, CERTO)], 1490, 590, "center")
        E.frase(c, t, d_, [("cada", "i", 88), ("casa", "i", 88), ("vale", "i", 88), ("só", "i", 88), ("o", "i", 88), ("seu", "i", 88), ("algarismo", "g", 82, COR)], W / 2, 810, "center", passo=0.13)
        E.frase(c, t, lerp(d_, C["s12.end"], 0.55), [("por", "i", 88), ("isso", "i", 88), ("a", "i", 88), ("soma", "g", 82, COR), ("decide", "g", 82, COR)], W / 2, 930, "center", passo=0.14)


# ---------------- por seis ----------------
def b_seis(c, t, C, b):
    a_, b_, c_, d_, e_ = C["s13.a"], C["s13.b"], C["s13.c"], C["s13.d"], C["s13.e"]
    pil(c, t, a_, "÷ 6", 400, 200, 100)
    E.frase(c, t, a_ + 0.3, [("não", "g", 84, COR), ("tem", "i", 92), ("regra", "i", 92), ("nova", "i", 92)], 640, 225, passo=0.14)
    u = lerp(a_, b_, 0.45)
    linha(c, t, [("6", "g", 170, TINTA, u), ("=", "g", 130, CINZA, u + 0.2), ("2", "g", 170, COR, u + 0.35), ("×", "g", 130, CINZA, u + 0.5), ("3", "g", 170, COR, u + 0.65)], W / 2, 450, "center")
    E.frase(c, t, b_, [("precisa", "i", 84), ("passar", "i", 84), ("nas", "i", 84), ("duas", "g", 78, COR), ("regras", "g", 78, COR)], W / 2, 590, "center", passo=0.14)
    x1, x2, y = 480, 1250, 750
    p = ep(t, c_ - 0.2, 0.4)
    E.caixa_pontilhada(c, 170, y - 100, 660, 190, p, prog_=p)
    E.frase(c, t, c_, [("regra", "i", 60), ("do", "i", 60), ("2:", "g", 58, COR)], 210, y - 30, passo=0.1)
    E.frase(c, t, c_ + 0.3, [("é", "g", 72), ("par", "g", 72)], 210, y + 56)
    selo_entra(c, t, c_ + 0.4, 720, y - 5, 66, True)
    p = ep(t, d_ - 0.3, 0.4)
    E.caixa_pontilhada(c, 880, y - 100, 860, 190, p, prog_=p)
    E.frase(c, t, d_ - 0.2, [("regra", "i", 60), ("do", "i", 60), ("3:", "g", 58, COR)], 920, y - 30, passo=0.1)
    E.frase(c, t, d_, [("soma", "i", 72), ("18", "g", 72), ("÷", "g", 72, CINZA), ("3", "g", 72), ("=", "g", 72, CINZA), ("6", "g", 72, COR)], 920, y + 56, passo=0.1)
    selo_entra(c, t, d_ + 0.5, 1630, y - 5, 66, True)
    E.foco(c, t, e_, 0.5, lambda a: E.pilula(c, "divisível por 6", W / 2, 950, 76, estilo="g", fundo=CERTO, cor=BR, a=a))


# ---------------- placar ----------------
PLACAR = ((2, True, "s14.a"), (3, True, "s14.b"), (4, True, "s14.c"), (5, False, "s14.d"), (6, True, "s14.e"), (9, True, "s14.f"), (10, False, "s14.g"))


def b_placar(c, t, C, b):
    s0 = C["s14"]
    E.frase(c, t, s0 + 0.2, [("placar", "i", 90), ("final", "g", 84, COR)], W / 2, 170, "center")
    E.foco(c, t, s0 + 0.3, 0.5, lambda a: numero(c, N, W / 2, 360, 170, a=a))
    for i, (d, ok, k) in enumerate(PLACAR):
        x = 215 + i * 248
        pil(c, t, C[k], f"÷ {d}", x, 510, 62)
        selo_entra(c, t, C[k] + 0.1, x, 660, 76, ok)
    u = lerp(C["s14.g"], C["s14.end"], 0.42)
    linha(c, t, [("só", "i", 92, TINTA, u), ("não", "g", 86, ERRADO, u + 0.15), ("é", "i", 92, TINTA, u + 0.3), ("divisível", "i", 92, TINTA, u + 0.4), ("por", "i", 92, TINTA, u + 0.55),
                 ("5", "g", 86, ERRADO, u + 0.7), ("e", "i", 92, TINTA, u + 0.85), ("por", "i", 92, TINTA, u + 0.95), ("10", "g", 86, ERRADO, u + 1.1)], W / 2, 890, "center")


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    s0, a_, b_, c_, d_, e_ = C["s15"], C["s15.a"], C["s15.b"], C["s15.c"], C["s15.d"], C["s15.e"]
    linha(c, t, [("o", "i", 76, TINTA, s0 + 0.25), ("erro", "g", 70, ERRADO, s0 + 0.35), ("mais", "i", 76, TINTA, s0 + 0.5), ("comum:", "i", 76, TINTA, s0 + 0.65),
                 ("olhar", "g", 70, ERRADO, a_), ("o", "g", 70, ERRADO, a_ + 0.1), ("final", "g", 70, ERRADO, a_ + 0.2), ("no", "i", 76, TINTA, a_ + 0.3), ("3", "g", 70, ERRADO, a_ + 0.4)], W / 2, 170, "center")
    E.frase(c, t, b_, [("termina", "i", 92), ("em", "i", 92), ("3,", "g", 86), ("divide", "i", 92), ("por", "i", 92), ("3?", "g", 86)], W / 2, 300, "center", passo=0.13)
    if t >= c_:
        E.risco(c, 480, 276, 1440, 276, t, c_, largura=9)
    # 23: termina em 3 e deixa resto
    cx = 500
    E.foco(c, t, c_, 0.4, lambda a: numero(c, "23", cx, 560, 190, {1: ERRADO}, a))
    trecho(c, "23", cx, 560, 190, 1, 2, ep(t, c_ + 0.2, 0.4), ERRADO)
    selo_entra(c, t, c_ + 0.4, cx + 260, 490, 66, False)
    E.foco(c, t, c_ + 0.5, 0.4, lambda a: centro(c, "23 ÷ 3 = 7", cx, 690, 76, "g", TINTA, a))
    E.foco(c, t, c_ + 0.7, 0.4, lambda a: centro(c, "sobram 2", cx, 780, 76, "g", ERRADO, a))
    # 12: termina em 2 e se divide
    cx = 1400
    E.foco(c, t, d_, 0.4, lambda a: numero(c, "12", cx, 560, 190, {1: CERTO}, a))
    trecho(c, "12", cx, 560, 190, 1, 2, ep(t, d_ + 0.2, 0.4), CERTO)
    selo_entra(c, t, d_ + 0.4, cx + 260, 490, 66, True)
    E.foco(c, t, d_ + 0.5, 0.4, lambda a: centro(c, "12 ÷ 3 = 4", cx, 690, 76, "g", TINTA, a))
    E.foco(c, t, d_ + 0.7, 0.4, lambda a: centro(c, "sem resto", cx, 780, 76, "g", CERTO, a))
    linha(c, t, [("no", "i", 84, TINTA, e_ - 0.4), ("3", "g", 80, TINTA, e_ - 0.3), ("e", "i", 84, TINTA, e_ - 0.2), ("no", "i", 84, TINTA, e_ - 0.15), ("9,", "g", 80, TINTA, e_ - 0.1),
                 ("quem", "i", 84, TINTA, e_), ("manda", "i", 84, TINTA, e_ + 0.1), ("é", "i", 84, TINTA, e_ + 0.2), ("a", "g", 80, COR, e_ + 0.3), ("soma", "g", 80, COR, e_ + 0.4)], W / 2, 945, "center")


# ---------------- atalho (palco escuro) ----------------
DX = (370, 650, 1110, 1390)  # os quatro algarismos, em dois pares


def b_atalho(c, t, C, b):
    palco(c, t)

    def nome():
        E.frase(c, t, C["s16"] + 0.25, [("aqui", "i", 90, CLARO), ("está", "i", 90, CLARO), ("o", "i", 90, CLARO), ("atalho", "i", 90, CLARO)], W / 2, 220, "center", passo=0.14)
        E.frase(c, t, C["s16.a"], [("os", "i", 180, CLARO), ("noves", "g", 190, BR), ("fora", "g", 190, BR)], W / 2, 510, "center")
        v = C["s16.b"]
        E.frase(c, t, v, [("risque", "g", 84, BR), ("os", "i", 90, CLARO), ("algarismos", "i", 90, CLARO)], W / 2, 720, "center", passo=0.14)
        E.frase(c, t, v + 0.6, [("que", "i", 90, CLARO), ("juntos", "i", 90, CLARO), ("dão", "i", 90, CLARO), ("9", "g", 96, BR)], W / 2, 840, "center", passo=0.14)
    E.saida(c, t, C["s17"] - 0.1, nome)

    def riscar():
        s0, a_, b_, c_, d_ = C["s17"], C["s17.a"], C["s17.b"], C["s17.c"], C["s17.d"]
        E.foco(c, t, s0 + 0.1, 0.4, lambda q: centro(c, N, W / 2, 190, 96, "g", CLARO, q))
        r1, r2 = lerp(a_, b_, 0.72), lerp(b_, c_, 0.72)
        for i, dg in enumerate("4572"):
            risc = t >= (r1 if i < 2 else r2)
            E.foco(c, t, s0 + 0.2 + i * 0.08, 0.4, lambda q, i=i, dg=dg, risc=risc: centro(c, dg, DX[i], 520, 280, "g", M.mix(BR, CINZA, 0.6) if risc else BR, q))
        for (x0, x1, ti, tr) in ((DX[0], DX[1], a_, r1), (DX[2], DX[3], b_, r2)):
            p = ep(t, ti, 0.4)
            E.chave(c, x0 - 40, x1 + 40, 570, CLARO, p, 34, 6)
            pil(c, t, lerp(ti, tr, 0.5), "9", (x0 + x1) / 2, 660, 64)
            if t >= tr:
                E.risco(c, x0 - 80, 545, x0 + 80, 330, t, tr, largura=14)
                E.risco(c, x1 - 80, 545, x1 + 80, 330, t, tr + 0.1, largura=14)
        E.frase(c, t, c_, [("não", "i", 96, CLARO), ("sobrou", "i", 96, CLARO), ("nada", "g", 90, BR)], W / 2, 830, "center", passo=0.14)
        E.frase(c, t, d_, [("divisível", "g", 90, BR), ("por", "i", 96, CLARO), ("9", "g", 90, BR)], W / 2, 950, "center", passo=0.14)
    if t >= C["s17"]:
        E.saida(c, t, C["s18"] - 0.1, riscar)

    def porque():
        a_, b_ = C["s18.a"], C["s18.b"]
        E.frase(c, t, C["s18"] + 0.3, [("por", "i", 90, CLARO), ("que", "i", 90, CLARO), ("funciona?", "i", 90, CLARO)], XE, 200, passo=0.14)
        E.frase(c, t, a_, [("tirar", "g", 96, BR), ("9", "g", 96, BR), ("da", "i", 100, CLARO), ("soma", "i", 100, CLARO)], XE, 360, passo=0.14)
        E.frase(c, t, a_ + 0.5, [("não", "g", 96, BR), ("muda", "g", 96, BR), ("a", "i", 100, CLARO), ("resposta", "i", 100, CLARO)], XE, 480, passo=0.14)
        E.frase(c, t, lerp(a_, b_, 0.45), [("sobrou", "i", 80, CLARO), ("algum?", "i", 80, CLARO), ("teste", "g", 76, BR), ("o", "g", 76, BR), ("que", "g", 76, BR), ("sobrou", "g", 76, BR)], XE, 610, passo=0.14)
        E.frase(c, t, lerp(a_, b_, 0.85), [("9", "g", 96, BR), ("é", "i", 100, CLARO), ("múltiplo", "i", 100, CLARO), ("de", "i", 100, CLARO), ("3", "g", 96, BR)], XE, 790, passo=0.14)
        E.frase(c, t, b_, [("riscar", "i", 100, CLARO), ("vale", "g", 96, BR), ("no", "i", 100, CLARO), ("teste", "i", 100, CLARO), ("do", "i", 100, CLARO), ("3", "g", 96, BR)], XE, 910, passo=0.14)
    if t >= C["s18"]:
        E.saida(c, t, C["s19"] - 0.1, porque)

    if t >= C["s19"]:
        s0, a_, b_, c_ = C["s19"], C["s19.a"], C["s19.b"], C["s19.c"]
        E.frase(c, t, s0 + 0.25, [("quando", "i", 96, CLARO), ("não", "g", 90, BR), ("compensa?", "g", 90, BR)], W / 2, 200, "center", passo=0.14)
        E.foco(c, t, a_, 0.5, lambda q: num_bola(c, "1", 220, 370, 56, 64, q, E.COR, BR))
        E.frase(c, t, a_ + 0.1, [("nenhum", "i", 76, CLARO), ("grupo", "i", 76, CLARO), ("dá", "i", 76, CLARO), ("9,", "i", 76, CLARO)], 310, 380, passo=0.12)
        E.frase(c, t, lerp(a_, b_, 0.55), [("ou", "i", 76, CLARO), ("o", "i", 76, CLARO), ("número", "i", 76, CLARO), ("é", "i", 76, CLARO), ("curto", "i", 76, CLARO)], 310, 480, passo=0.12)
        E.frase(c, t, b_, [("some", "g", 76, BR), ("e", "g", 76, BR), ("pronto", "g", 76, BR)], 310, 580, passo=0.14)
        E.foco(c, t, c_, 0.5, lambda q: num_bola(c, "2", 220, 750, 56, 64, q, E.COR, BR))
        E.frase(c, t, c_ - 0.2, [("não", "i", 76, CLARO), ("serve", "i", 76, CLARO), ("para", "i", 76, CLARO)], 310, 760, passo=0.1)
        linha(c, t, [("2,", "g", 76, BR, c_), ("4,", "g", 76, BR, c_ + 0.15), ("5", "g", 76, BR, c_ + 0.3), ("ou", "i", 76, CLARO, c_ + 0.45), ("10", "g", 76, BR, c_ + 0.55)], 730, 760)
        E.frase(c, t, c_ + 0.9, [("esses", "i", 76, CLARO), ("olham", "i", 76, CLARO), ("o", "i", 76, CLARO), ("final", "g", 72, BR)], 310, 860, passo=0.14)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    s0, a_, b_ = C["s20"], C["s20.a"], C["s20.b"]
    E.frase(c, t, s0 + 0.3, [("hora", "i", 72, COR), ("de", "i", 72, COR), ("testar", "i", 72, COR)], XE, 200)
    for i, d in enumerate(DIVS):
        bola_entra(c, t, lerp(a_, b_, i / 7.5), str(d), XE + 60 + i * 138, 350, 62, 60)
    E.frase(c, t, b_, [("quais", "g", 120, COR), ("dividem", "i", 120)], XE, 590, passo=0.15)
    E.foco(c, t, lerp(b_, C["s20.end"], 0.35), 0.5, lambda a: numero(c, "7.290", 560, 830, 240, a=a))
    relogio(c, t, C["s21.a"])


# ---------------- resposta ----------------
N2 = "7.290"
RES = ((2, True), (3, True), (4, False), (5, True), (6, True), (9, True), (10, True))


def b_resposta(c, t, C, b):
    a_, b_, c_, d_, e_ = C["s22.a"], C["s22.b"], C["s22.c"], C["s22.d"], C["s22.e"]
    a2, b2, c2 = C["s23.a"], C["s23.b"], C["s23.c"]
    cx, y = 470, 260
    E.foco(c, t, C["s22"] + 0.1, 0.4, lambda q: numero(c, N2, cx, y, 170, a=q))
    xs, w = casas(N2, cx, 170)
    trecho(c, N2, cx, y, 170, 4, 5, ep(t, a_ - 0.3, 0.4) * (1 - ep(t, lerp(a_, b_, 0.8), 0.3)))
    for i, ti in ((0, lerp(b_, c_, 0.5)), (2, lerp(b_, c_, 0.7)), (3, lerp(c_, d_, 0.45))):
        if t >= ti:
            E.risco(c, xs[i] + 4, y + 16, xs[i] + 100, y - 136, t, ti, largura=11)
    ls = ((a_ - 0.2, "termina em 0", "b"), (b_ - 0.3, "noves fora: 7 + 2", "b"), (c_, "e o 9 sozinho", "b"), (lerp(c_, d_, 0.45), "só sobrou o 0", "b"), (lerp(d_, e_, 0.5), "par e passou no 3", "b"))
    for i, (ti, s, est) in enumerate(ls):
        E.foco(c, t, ti, 0.4, lambda q, i=i, s=s, est=est: E.escreve(c, s, XE, 390 + i * 96, 66, est, TINTA, q))
    E.foco(c, t, a2, 0.4, lambda q: E.escreve(c, "final 90: 90 ÷ 4 = 22", XE, 870, 66, "b", TINTA, q))
    E.foco(c, t, b2, 0.4, lambda q: E.escreve(c, "sobram 2", XE, 960, 66, "b", ERRADO, q))
    # o placar enche na ordem da fala
    tempo = {2: a_ + 0.2, 5: a_ + 0.5, 10: a_ + 0.8, 3: d_, 9: d_ + 0.3, 6: e_, 4: b2 + 0.2}
    for i, (d, ok) in enumerate(RES):
        x, yy = 1020 + (i % 4) * 225, 230 + (i // 4) * 300
        pil(c, t, C["s22"] + 0.2 + i * 0.08, f"÷ {d}", x, yy, 62)
        selo_entra(c, t, tempo[d], x, yy + 130, 70, ok)
    E.foco(c, t, c2, 0.5, lambda a: E.pilula(c, "só o 4 não divide", 1360, 870, 72, estilo="g", fundo=E.COR, cor=BR, a=a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s24"] + 0.25, [("resumindo", "i", 96, COR)], W / 2, 180, "center")
        ls = (("s24.a", [("2,", "g", 80, COR), ("5", "g", 80, COR), ("e", "i", 84), ("10", "g", 80, COR), ("olham", "i", 84), ("o", "i", 84), ("último", "i", 84), ("algarismo", "i", 84)]),
              ("s24.b", [("4", "g", 80, COR), ("olha", "i", 84), ("os", "i", 84), ("últimos", "i", 84), ("dois", "i", 84), ("algarismos", "i", 84)]),
              ("s24.c", [("3", "g", 80, COR), ("e", "i", 84), ("9", "g", 80, COR), ("olham", "i", 84), ("a", "i", 84), ("soma", "g", 80)]),
              ("s24.d", [("6", "g", 80, COR), ("junta", "i", 84), ("a", "i", 84), ("regra", "i", 84), ("do", "i", 84), ("2", "g", 80), ("com", "i", 84), ("a", "i", 84), ("do", "i", 84), ("3", "g", 80)]))
        for i, (k, partes) in enumerate(ls):
            y = 350 + i * 170
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: num_bola(c, str(i + 1), 220, y - 28, 56, 64, a))
            E.frase(c, t, C[k] + 0.1, partes, 310, y, passo=0.12)
    E.saida(c, t, C["s25"] - 0.1, resumo)
    if t < C["s25"]:
        return
    s0 = C["s25"]
    E.frase(c, t, s0 + 0.5, [("próxima", "i", 84), ("aula", "i", 84)], XE, 280)
    E.frase(c, t, C["s25.a"], [("números", "g", 140, COR), ("primos", "g", 140, COR)], XE, 430, passo=0.3)
    E.frase(c, t, C["s25.a"] + 0.6, [("e", "i", 130), ("fatoração", "g", 124, COR)], XE, 570)
    E.frase(c, t, lerp(C["s25.a"], C["s25.b"], 0.45), [("essas", "i", 76), ("regras", "i", 76), ("vão", "i", 76), ("trabalhar", "g", 70), ("por", "i", 76), ("lá", "i", 76)], XE, 700, passo=0.16)
    E.foco(c, t, C["s25.b"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1560, 690, 72, estilo="g", fundo=E.COR, cor=E.SOBRE, a=a))
    p = ease_io(prog(t, C["s25.b"] + 0.3, 0.8))
    E.cursor(c, lerp(1780, 1660, p), lerp(900, 730, p), ep(t, C["s25.b"] + 0.2, 0.4), TINTA)
    E.frase(c, t, C["s25.c"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 900, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, nome=b_nome, final=b_final, quatro=b_quatro, soma=b_soma, seis=b_seis, placar=b_placar,
              erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
