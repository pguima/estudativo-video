"""Visual — Estudativo · MAT-DIV-004: calcular o MDC.
Peças da aula: as listas alinhadas por valor (os comuns ficam na mesma coluna), sacolas de frutas, fileiras de primos com par e a tabela do kit sobre uma folha clara no palco escuro.
Todo instante vem de C[...]: fala sem cue usa um ponto entre dois cues (lerp), para continuar certo com a voz real."""
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro, linha, montar, tabela, seta_primo
import motor as M
import skia

E.usar("Matemática", "Divisibilidade, MMC e MDC")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-DIV-004_calcular_mdc.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("listar", "fatorar", "atalho", "questao", "fim"))
BR = "#FFFFFF"

T72 = montar((72,), (2, 2, 2, 3, 3))
T120 = montar((120,), (2, 2, 2, 3, 5))
G72 = dict(xs=(300,), xb=450, xp=550, y0=225, dy=112, s=88)
G120 = dict(xs=(1120,), xb=1270, xp=1370, y0=225, dy=112, s=88)
_J = montar((72, 120), (2, 2, 2, 3, 3, 5))  # a divisão simultânea de verdade; o atalho para no 3 e 5, antes de chegar em 1
TJ = dict(primos=_J["primos"][:4], linhas=_J["linhas"][:5], desceu=_J["desceu"][:5])
GJ = dict(xs=(310, 530), xb=670, xp=775, y0=255, dy=132, s=100)
assert TJ["linhas"][-1] == (3, 5) and all(not any(d) for d in TJ["desceu"])  # só primos que dividem os dois


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


def bloco(c, x, y, w, h, r, cor, a=1.0, stroke=None):
    if a > 0:
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), r, r), M.paint(cor, a, stroke=stroke))


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


def fruta(c, x, y, r, cor, a=1.0):
    """fruta com um cabinho; laranja = cor da matéria, maçã = o tom claro"""
    if a > 0:
        E.bola(c, x, y, r, cor, a)
        M.line(c, x, y - r * 0.9, x + r * 0.28, y - r * 1.3, TINTA2, a, max(3, r * 0.14))


def conta_mult(ns, sep=" × "):
    return sep.join(str(n) for n in ns)


def primos_fila(c, t, ns, xs, y, ts, cores, r=66, size=76):
    """fileira de primos: um por coluna (None deixa a coluna vazia)"""
    for n, x, ti, cor in zip(ns, xs, ts, cores):
        if n is not None:
            bola_entra(c, t, ti, str(n), x, y, r, size, cor, BR)


def elo(c, t, t0, x, y0, y1, cor=CERTO):
    """liga os dois primos de um par"""
    if t >= t0:
        M.line(c, x, y0, x, y1, cor, 1.0, 12, progress=ep(t, t0, 0.3))


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
D120 = (1, 2, 3, 4, 5, 6, 8, 10, 12, 15, 20, 24, 30, 40, 60, 120)


def b_gancho(c, t, C, b):
    def pergunta():
        s0, a_, b_, c_ = C["s01"], C["s01.a"], C["s01.b"], C["s01.c"]
        E.frase(c, t, s0 + 0.25, [("qual", "i", 90), ("é", "i", 90), ("o", "i", 90), ("maior", "g", 84, COR), ("número", "i", 90), ("que", "i", 90), ("divide", "i", 90)], W / 2, 170, "center", passo=0.13)
        bola_entra(c, t, a_, "72", 640, 370, 130, 130)
        E.foco(c, t, b_ - 0.1, 0.4, lambda q: centro(c, "e", W / 2, 400, 110, "i", TINTA, q))
        bola_entra(c, t, b_, "120", 1280, 370, 130, 110)
        E.frase(c, t, lerp(b_, c_, 0.45), [("sem", "g", 72), ("deixar", "g", 72), ("resto", "g", 72, CERTO)], W / 2, 575, "center", passo=0.13)

        def lista():
            for i, n in enumerate(D120):
                E.foco(c, t, c_ + i * 0.05, 0.3, lambda a, i=i, n=n: centro(c, str(n), 330 + (i % 8) * 180, 790 + (i // 8) * 100, 80, "b", TINTA2, a), sobe=8)
        lista()
        E.frase(c, t, lerp(c_, C["s01.end"], 0.55), [("listar", "g", 72, ERRADO), ("tudo", "g", 72, ERRADO), ("cansa", "g", 72, ERRADO)], W / 2, 985, "center", passo=0.14)
        E.foco(c, t, c_ + 0.2, 0.4, lambda a: E.pilula(c, "só o 120: 16 divisores", W / 2, 670, 50, estilo="b", fundo=TINTA, cor=BR, a=a * ep(t, c_ + 0.2, 0.3)))
    E.saida(c, t, C["s02"] - 0.1, pergunta)

    if t >= C["s02"]:
        s0, a_ = C["s02"], C["s02.a"]
        q = ease_back(prog(t, C["s02.b"] - 0.2, 0.7))
        if q > 0:
            E.bola(c, 1480, 540, 290 * q)
        E.frase(c, t, s0 + 0.3, [("até", "i", 90), ("o", "i", 90), ("fim", "i", 90), ("da", "i", 90), ("aula", "i", 90)], XE, 350)
        E.frase(c, t, lerp(s0, a_, 0.5), [("você", "i", 124), ("acha", "g", 124)], XE, 510)
        E.frase(c, t, lerp(s0, a_, 0.8), [("esse", "i", 90), ("número", "i", 90)], XE, 640, passo=0.15)
        E.frase(c, t, a_, [("com", "i", 110), ("poucas", "g", 124, COR)], XE, 790, passo=0.15)
        E.frase(c, t, a_ + 0.4, [("contas", "g", 124, COR)], XE, 920)
        E.foco(c, t, C["s02.b"] + 0.2, 0.5, lambda a: (centro(c, "+ atalho", 1480, 525, 84, "g", E.SOBRE, a),
                                                      centro(c, "de prova", 1480, 610, 84, "i", E.SOBRE, a)))


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    s0, a_, b_ = C["s03"], C["s03.a"], C["s03.b"]
    E.frase(c, t, s0 + 0.35, [("para", "i", 84), ("acompanhar,", "i", 84)], XE, 290)
    E.frase(c, t, lerp(s0, a_, 0.5), [("você", "i", 84), ("só", "i", 84), ("precisa", "i", 84), ("de", "i", 84)], XE, 400, passo=0.13)
    E.foco(c, t, a_, 0.5, lambda q: E.escreve(c, "1", XE, 720, 340, "g", COR, q))
    E.foco(c, t, a_ + 0.15, 0.5, lambda q: E.escreve(c, "coisa", XE + 180, 705, 120, "i", TINTA, q))
    x, w = 900, 880
    p = ep(t, b_, 0.5)
    E.caixa_pontilhada(c, x, 230, w, 460, p, prog_=p)
    E.frase(c, t, b_ + 0.1, [("fatorar:", "g", 110, COR)], x + 50, 360)
    E.frase(c, t, b_ + 0.5, [("escrever", "i", 76), ("um", "i", 76), ("número", "i", 76), ("como", "i", 76)], x + 50, 470, passo=0.13)
    E.frase(c, t, b_ + 1.0, [("multiplicação", "g", 66), ("de", "i", 72), ("primos", "g", 66, COR)], x + 50, 560, passo=0.13)
    E.frase(c, t, b_ + 1.4, [("12", "g", 60), ("=", "g", 60, CINZA), ("2", "g", 60, COR), ("×", "g", 60, CINZA), ("2", "g", 60, COR), ("×", "g", 60, CINZA), ("3", "g", 60, COR)], x + 50, 650, passo=0.1)
    E.cursor(c, x + w - 30, 640, ep(t, b_, 0.4))
    E.frase(c, t, lerp(b_, C["s03.end"], 0.72), [("faltou?", "i", 62), ("procure", "i", 62), ("a", "i", 62), ("aula", "i", 62), ("no", "i", 62), ("canal", "i", 62)], x, 830, passo=0.13)


# ---------------- o que quer dizer ----------------
def b_nome(c, t, C, b):
    ys = (340, 600, 860)
    tam = 150
    letras = (("M", "áximo", 0.0), ("D", "ivisor", 0.5), ("C", "omum", 1.0))
    p = ease_io(prog(t, C["s04.a"] + 0.1, 0.6))  # o MDC gigante se desmonta nas três iniciais
    size0 = 440
    w0 = sum(E.larg(l, "g", size0) for l, _, _ in letras) + 2 * size0 * 0.02
    xi = W / 2 - w0 / 2
    for i, (l, resto, dt) in enumerate(letras):
        x, y, s = lerp(xi, XE, p), lerp(690, ys[i], p), round(lerp(size0, tam, p))
        E.foco(c, t, C["s04"] + 0.2 + i * 0.12, 0.5, lambda a, l=l, x=x, y=y, s=s: E.escreve(c, l, x, y, s, "g", COR, a))
        xi += E.larg(l, "g", size0) + size0 * 0.02
        E.foco(c, t, C["s04.a"] + 0.3 + dt, 0.5, lambda a, l=l, resto=resto, i=i: E.escreve(c, resto, XE + E.larg(l, "g", tam) + 2, ys[i], tam, "g", TINTA, a))

    E.saida(c, t, C["s05"] - 0.05, lambda: (E.frase(c, t, lerp(C["s04.a"], C["s04.end"], 0.6), [("o", "i", 84), ("nome", "i", 84), ("já", "i", 84), ("explica", "i", 84), ("tudo", "g", 76, COR)], 1000, 470, passo=0.15),
                                            E.frase(c, t, lerp(C["s04.a"], C["s04.end"], 0.82), [("parte", "i", 84), ("por", "i", 84), ("parte", "i", 84)], 1000, 590, passo=0.16)))
    X = 930
    a_, b_, c_ = C["s05.a"], C["s05.b"], C["s05.c"]
    E.frase(c, t, a_ + 0.3, [("divide", "i", 66), ("outro", "i", 66), ("número", "i", 66)], X, ys[1] - 62, passo=0.14)
    E.frase(c, t, lerp(a_, b_, 0.5), [("sem", "g", 60), ("deixar", "g", 60), ("resto", "g", 60, COR)], X, ys[1] + 18, passo=0.14)
    E.frase(c, t, b_ + 0.3, [("aparece", "i", 66), ("na", "i", 66), ("lista", "i", 66)], X, ys[2] - 62, passo=0.14)
    E.frase(c, t, lerp(b_, c_, 0.6), [("de", "g", 60), ("todos", "g", 60, COR)], X, ys[2] + 18, passo=0.14)
    E.frase(c, t, c_ + 0.2, [("o", "i", 66), ("maior", "g", 62, COR), ("deles", "i", 66)], X, ys[0] - 30, passo=0.14)
    q1, q2 = ease_io(prog(t, b_ - 0.3, 0.5)), ease_io(prog(t, c_ - 0.3, 0.5))
    E.cursor(c, 830, lerp(lerp(ys[1], ys[2], q1) - 60, ys[0] - 60, q2), ep(t, a_, 0.4))


# ---------------- listar ----------------
SLOT = (1, 2, 3, 4, 6, 9, 12, 18)  # um lugar por valor: o que é comum cai na mesma coluna
D12 = (1, 2, 3, 4, 6, 12)
D18 = (1, 2, 3, 6, 9, 18)


def b_listar(c, t, C, b):
    def frutas():
        s0, a_, b_, c_ = C["s06"], C["s06.a"], C["s06.b"], C["s06.c"]
        E.frase(c, t, s0 + 0.2, [("para", "i", 84), ("que", "i", 84), ("serve?", "g", 80, COR)], W / 2, 170, "center", passo=0.14)
        for i in range(12):
            fruta(c, 210 + (i % 6) * 92, 300 + (i // 6) * 100, 40, E.COR, ep(t, a_ + i * 0.03, 0.3))
        linha(c, t, [("12", "g", 96, COR, a_), ("laranjas", "i", 92, TINTA, a_ + 0.2)], 170, 560)
        for i in range(18):
            fruta(c, 1000 + (i % 6) * 92, 260 + (i // 6) * 92, 40, E.CLARO, ep(t, b_ + i * 0.03, 0.3))
        linha(c, t, [("18", "g", 96, TINTA2, b_), ("maçãs", "i", 92, TINTA, b_ + 0.2)], 960, 560)
        E.frase(c, t, lerp(b_, c_, 0.45), [("o", "i", 80), ("maior", "g", 74, COR), ("número", "i", 80), ("de", "i", 80), ("sacolas", "i", 80), ("iguais,", "i", 80)], W / 2, 710, "center", passo=0.13)
        E.frase(c, t, lerp(b_, c_, 0.75), [("sem", "g", 74), ("sobrar", "g", 74), ("fruta", "g", 74)], W / 2, 810, "center", passo=0.14)
        linha(c, t, [("divide", "i", 80, TINTA, c_ - 0.4), ("12", "g", 80, COR, c_ - 0.15), ("e", "i", 80, TINTA, c_), ("também", "i", 80, TINTA, c_ + 0.1), ("18", "g", 80, COR, c_ + 0.35)], W / 2, 930, "center")
    E.saida(c, t, C["s07"] - 0.1, frutas)

    X = lambda v: 340 + SLOT.index(v) * 192
    y1, y2 = 350, 620
    fim_lista = C["s08.d"] - 0.1

    def listas():
        a_, b_, a2, b2, c2 = C["s07.a"], C["s07.b"], C["s08.a"], C["s08.b"], C["s08.c"]
        E.frase(c, t, C["s07"] + 0.15, [("liste", "i", 84), ("os", "i", 84), ("divisores", "g", 80, COR)], W / 2, 130, "center", passo=0.13)
        E.frase(c, t, a_, [("de", "i", 70), ("12", "g", 70, COR)], XE, 230, passo=0.12)
        E.frase(c, t, b_, [("de", "i", 70), ("18", "g", 70, COR)], XE, 500, passo=0.12)
        for y, ds, t0, t1 in ((y1, D12, a_, b_), (y2, D18, b_, C["s07.end"])):
            for i, v in enumerate(ds):
                comum = v in (1, 2, 3, 6)
                ativo = comum and t >= a2 + (1, 2, 3, 6).index(v) * 0.25 if comum else False
                if ativo:
                    E.bola(c, X(v), y - 40, 84 * ease_back(prog(t, a2 + (1, 2, 3, 6).index(v) * 0.25, 0.5)), E.COR)
                ti = lerp(t0, t1, 0.12 + 0.72 * i / 6)
                E.foco(c, t, ti, 0.4, lambda a, v=v, y=y, ativo=ativo: centro(c, str(v), X(v), y, 110, "g", E.SOBRE if ativo else TINTA, a))
        p = ep(t, b2, 0.5)  # a coluna do 6: o maior comum
        E.caixa_pontilhada(c, X(6) - 110, y1 - 150, 220, y2 - y1 + 215, p, prog_=p)
        E.cursor(c, X(6) + 95, y2 + 45, ep(t, b2 + 0.2, 0.4))
        E.foco(c, t, c2, 0.5, lambda a: centro(c, "MDC de 12 e 18 = 6", W / 2, 860, 100, "g", COR, a))
    if t >= C["s07"]:
        E.saida(c, t, fim_lista, listas)

    def sacolas():
        d_ = C["s08.d"]
        E.frase(c, t, d_, [("6", "g", 170, COR), ("sacolas", "i", 150)], W / 2, 270, "center")
        for i in range(6):
            x, ti = 165 + i * 270, d_ + 0.3 + i * 0.1
            p = ep(t, ti, 0.35)
            bloco(c, x, 400, 240, 280, 26, BR, p * 0.9)
            bloco(c, x, 400, 240, 280, 26, TINTA, p, 4)
            for j in range(2):
                fruta(c, x + 72 + j * 96, 480, 40, E.COR, p)
            for j in range(3):
                fruta(c, x + 44 + j * 76, 595, 34, E.CLARO, p)
        linha(c, t, [("cada", "i", 84, TINTA, d_ + 0.5), ("uma:", "i", 84, TINTA, d_ + 0.6), ("2", "g", 84, COR, d_ + 0.75), ("laranjas", "i", 84, TINTA, d_ + 0.85), ("e", "i", 84, TINTA, d_ + 1.0), ("3", "g", 84, TINTA2, d_ + 1.15), ("maçãs", "i", 84, TINTA, d_ + 1.25)], W / 2, 830, "center")
        E.foco(c, t, d_ + 1.2, 0.4, lambda a: centro(c, "6 × 2 = 12    ·    6 × 3 = 18", W / 2, 950, 66, "b", TINTA2, a))
    if t >= C["s08.d"]:
        E.saida(c, t, C["s09"] - 0.1, sacolas)

    if t >= C["s09"]:
        s0, a_ = C["s09"], C["s09.a"]
        E.frase(c, t, s0 + 0.2, [("números", "i", 88), ("pequenos:", "i", 88), ("resolve", "g", 84, CERTO)], XE, 270, passo=0.15)
        E.frase(c, t, lerp(s0, a_, 0.6), [("números", "i", 88), ("maiores:", "i", 88)], XE, 470, passo=0.15)
        E.frase(c, t, a_, [("a", "g", 84, ERRADO), ("lista", "g", 84, ERRADO), ("cansa", "g", 84, ERRADO)], 760, 470, passo=0.15)
        for i, n in enumerate(D120[:10]):
            E.foco(c, t, a_ + i * 0.1, 0.3, lambda a, i=i, n=n: centro(c, str(n), 240 + i * 160, 620, 72, "b", CINZA, a), sobe=8)
        E.frase(c, t, lerp(a_, C["s09.end"], 0.5), [("e", "i", 96), ("aí", "i", 96), ("a", "i", 96), ("fatoração", "g", 110, COR), ("entra", "i", 96)], W / 2, 860, "center", passo=0.16)


# ---------------- fatorar ----------------
PX = tuple(420 + i * 190 for i in range(6))  # colunas das fileiras de primos


def tempos_fat(t0, t1):
    """cada "por dois, trinta e seis" entre o início da conta e o resultado"""
    ti = [lerp(t0, t1, 0.14 + i * 0.165) for i in range(5)]
    tp = [x + 0.05 for x in ti]
    tn = [[t0]] + [[x + 0.3] for x in ti]
    return ti, tp, tn, [t0] + ti


def b_fatorar(c, t, C, b):
    def fatorar():
        a1, b1, c1 = C["s10.a"], C["s10.b"], C["s10.c"]
        a2, b2 = C["s11.a"], C["s11.b"]
        E.saida(c, t, b1 - 0.1, lambda: E.frase(c, t, a1, [("primeiro,", "i", 110), ("fatore", "g", 120, COR), ("cada", "i", 110), ("número", "i", 110)], W / 2, 540, "center", passo=0.15), d=0.25)
        if t < b1:
            return
        for T, g, u, v, fim in ((T72, G72, b1, c1, C["s11"]), (T120, G120, a2, b2, C["s12"])):
            if t < u:
                continue
            ti, tp, tn, tb = tempos_fat(u, v)
            tabela(c, t, T, tn, tp, tb, g, cor_fim=CERTO if t >= tn[-1][0] else None)
            for i in range(5):
                seta_primo(c, t, ti[i], ti[i + 1] if i < 4 else fim - 0.3, i, g)
        E.foco(c, t, c1, 0.4, lambda q: centro(c, conta_mult(T72["primos"]), 425, 930, 66, "g", COR, q))
        E.foco(c, t, b2, 0.4, lambda q: centro(c, conta_mult(T120["primos"]), 1245, 930, 66, "g", COR, q))
    if t < C["s12"]:
        E.saida(c, t, C["s12"] - 0.1, fatorar)

    if C["s12"] <= t < C["s13"]:
        s0, a_, b_ = C["s12"], C["s12.a"], C["s12.b"]
        E.frase(c, t, s0 + 0.2, [("a", "i", 96), ("regra", "i", 96), ("do", "i", 96), ("MDC", "g", 96, COR)], W / 2, 220, "center", passo=0.15)
        E.frase(c, t, a_, [("só", "i", 120), ("entra", "i", 120), ("o", "i", 120), ("primo", "g", 120, COR)], W / 2, 450, "center", passo=0.15)
        E.frase(c, t, a_ + 0.6, [("que", "i", 120), ("divide", "i", 120), ("todos", "g", 120, COR)], W / 2, 600, "center", passo=0.15)
        E.frase(c, t, b_, [("aparece", "i", 96), ("nas", "i", 96), ("duas", "g", 90, COR), ("fatorações", "g", 90, COR)], W / 2, 830, "center", passo=0.15)

    # as duas fileiras: um primo por coluna, para os pares ficarem um sobre o outro
    n72 = (2, 2, 2, 3, 3, None)
    n120 = (2, 2, 2, 3, None, 5)
    if C["s13"] <= t < C["s15"] + 0.4:
        def filas():
            s0, a_, b_, c_, d_, e_, f_, g_ = (C["s13"], C["s13.a"], C["s13.b"], C["s13.c"], C["s13.d"], C["s13.e"], C["s13.f"], C["s13.g"])
            y1, y2 = 300, 540
            E.saida(c, t, C["s14"] - 0.1, lambda: E.frase(c, t, s0 + 0.2, [("forme", "i", 76), ("pares,", "g", 70, COR), ("um", "i", 76), ("primo", "i", 76), ("de", "i", 76), ("cada", "i", 76), ("número", "i", 76)], W / 2, 150, "center", passo=0.12), d=0.25)
            E.foco(c, t, s0 + 0.3, 0.4, lambda q: (E.escreve(c, "72", XE - 30, y1 + 30, 92, "g", TINTA, q), E.escreve(c, "120", XE - 30 - 28, y2 + 30, 92, "g", TINTA, q)))
            cinza = ep(t, g_, 0.4)
            c72 = [E.COR] * 4 + [M.mix(ERRADO, CINZA, cinza), None]
            c120 = [E.COR] * 4 + [None, M.mix(ERRADO, CINZA, cinza)]
            ts = [s0 + 0.35 + i * 0.08 for i in range(6)]
            pares = (a_, b_, c_, d_)
            for i, ti in enumerate(pares):
                elo(c, t, ti, PX[i], y1 + 66, y2 - 66)
                c72[i] = c120[i] = E.COR if t < ti else CERTO
            for i, (ns, y, cs) in enumerate(((n72, y1, c72), (n120, y2, c120))):
                for j, (n, cor) in enumerate(zip(ns, cs)):
                    if n is None:
                        continue
                    if j >= 4 and t < (e_ if j == 4 else f_):
                        cor = E.COR
                    bola_entra(c, t, ts[j] + i * 0.2, str(n), PX[j], y, 72, 84, cor, BR)
            E.frase(c, t, g_, [("sem", "g", 84, ERRADO), ("par,", "g", 84, ERRADO), ("ficam", "i", 90), ("de", "i", 90), ("fora", "i", 90)], 1170, 720, "center", passo=0.14) if t < C["s14"] else None
        E.saida(c, t, C["s15"] - 0.1, filas)

    if C["s14"] <= t < C["s15"]:
        a_, b_, c_ = C["s14.a"], C["s14.b"], C["s14.c"]
        E.frase(c, t, a_, [("o", "i", 80), ("MDC:", "g", 76, COR), ("os", "i", 80), ("primos", "i", 80), ("que", "i", 80), ("formaram", "i", 80), ("par", "g", 76, CERTO)], W / 2, 150, "center", passo=0.13)
        linha(c, t, [("2", "g", 150, CERTO, b_), ("×", "g", 120, CINZA, b_ + 0.15), ("2", "g", 150, CERTO, b_ + 0.3), ("×", "g", 120, CINZA, b_ + 0.45), ("2", "g", 150, CERTO, b_ + 0.6), ("×", "g", 120, CINZA, b_ + 0.75), ("3", "g", 150, CERTO, b_ + 0.9)], 690, 860, "center")
        E.foco(c, t, c_ - 0.15, 0.3, lambda q: centro(c, "=", 1250, 850, 130, "g", CINZA, q))
        bola_entra(c, t, c_, "24", 1460, 810, 140, 130)

    if t >= C["s15"]:
        a_, b_, fim = C["s15.a"], C["s15.b"], C["s15.end"]
        E.frase(c, t, C["s15"] + 0.2, [("para", "i", 100), ("conferir", "g", 96, COR)], W / 2, 220, "center", passo=0.15)
        linha(c, t, [("72", "g", 150, TINTA, a_), ("÷", "g", 120, CINZA, a_ + 0.2), ("24", "g", 150, COR, a_ + 0.35), ("=", "g", 120, CINZA, a_ + 0.6), ("3", "g", 150, TINTA, a_ + 0.8)], 860, 470, "center")
        selo_entra(c, t, a_ + 1.0, 1420, 420, 76, True)
        linha(c, t, [("120", "g", 150, TINTA, b_), ("÷", "g", 120, CINZA, b_ + 0.2), ("24", "g", 150, COR, b_ + 0.35), ("=", "g", 120, CINZA, b_ + 0.6), ("5", "g", 150, TINTA, b_ + 0.8)], 860, 690, "center")
        selo_entra(c, t, b_ + 1.0, 1420, 640, 76, True)
        E.frase(c, t, lerp(b_, fim, 0.72), [("nenhum", "g", 110, CERTO), ("resto", "g", 110, CERTO)], W / 2, 900, "center", passo=0.16)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    s0, a_, b_, c_, d_, e_ = C["s16"], C["s16.a"], C["s16.b"], C["s16.c"], C["s16.d"], C["s16.e"]
    linha(c, t, [("o", "i", 76, TINTA, s0 + 0.2), ("erro", "g", 70, ERRADO, s0 + 0.3), ("mais", "i", 76, TINTA, s0 + 0.45), ("comum:", "i", 76, TINTA, s0 + 0.55),
                 ("levar", "g", 70, ERRADO, a_), ("um", "g", 70, ERRADO, a_ + 0.1), ("primo", "g", 70, ERRADO, a_ + 0.2), ("sem", "g", 70, ERRADO, a_ + 0.35), ("par", "g", 70, ERRADO, a_ + 0.45)], W / 2, 170, "center")
    v = lerp(a_, b_, 0.6)
    y = 410
    for i, (n, x) in enumerate(zip((2, 2, 2, 3, 3), (260, 470, 680, 890, 1100))):
        ruim = i == 4
        bola_entra(c, t, b_ if ruim else v + i * 0.1, str(n), x, y - 40, 72, 84, ERRADO if ruim else E.COR, BR)
        if i:
            E.foco(c, t, v + i * 0.1, 0.3, lambda q, x=x: centro(c, "×", x - 105, y - 12, 64, "g", CINZA, q))
    E.foco(c, t, c_ - 0.15, 0.3, lambda q: centro(c, "=", 1290, y - 8, 110, "g", CINZA, q))
    bola_entra(c, t, c_, "72", 1500, y - 40, 110, 110, ERRADO, BR)
    linha(c, t, [("120", "g", 110, TINTA, d_), ("÷", "g", 90, CINZA, d_ + 0.15), ("72", "g", 110, TINTA, d_ + 0.3), ("=", "g", 90, CINZA, d_ + 0.45), ("1", "g", 110, TINTA, d_ + 0.6)], 720, 640, "center")
    E.foco(c, t, d_ + 0.8, 0.5, lambda a: E.pilula(c, "sobram 48", 1320, 605, 72, estilo="g", fundo=ERRADO, cor=BR, a=a))
    E.frase(c, t, e_ - 0.4, [("cada", "i", 88), ("primo", "i", 88), ("entra", "i", 88), ("só", "g", 84, COR), ("as", "g", 84, COR), ("vezes", "g", 84, COR)], W / 2, 820, "center", passo=0.13)
    E.frase(c, t, e_ + 0.3, [("que", "i", 88), ("aparece", "i", 88), ("nas", "i", 88), ("duas", "g", 84, COR), ("fatorações", "g", 84, COR)], W / 2, 930, "center", passo=0.13)


# ---------------- atalho (palco escuro) ----------------
def contas_escuro(c, t, ti, fim):
    """as contas de cada passo, à direita, em branco: passos() do kit é para o papel claro"""
    for i, p in enumerate(TJ["primos"]):
        t1 = ti[i + 1] - 0.1 if i + 1 < len(ti) else fim
        if not ti[i] <= t < t1 + 0.4:
            continue

        def painel(i=i, p=p):
            E.foco(c, t, ti[i], 0.4, lambda a: E.pilula(c, f"÷ {p}", 1350, 300, 84, estilo="g", fundo=E.COR, cor=BR, a=a))
            for j, n in enumerate(TJ["linhas"][i]):
                E.foco(c, t, ti[i] + 0.3 + j * 0.2, 0.4, lambda a, j=j, n=n: centro(c, f"{n} ÷ {p} = {n // p}", 1350, 500 + j * 120, 84, "b", BR, a))
        E.saida(c, t, t1, painel)


def b_atalho(c, t, C, b):
    palco(c, t)

    def nome():
        s0, a_, b_ = C["s17"], C["s17.a"], C["s17.b"]
        E.frase(c, t, s0 + 0.2, [("agora,", "i", 90, CLARO), ("o", "i", 90, CLARO), ("atalho", "i", 90, CLARO)], W / 2, 230, "center", passo=0.13)
        E.frase(c, t, a_, [("divida", "g", 130, BR), ("ao", "i", 130, CLARO), ("mesmo", "i", 130, CLARO), ("tempo", "g", 130, BR)], W / 2, 470, "center", passo=0.16)
        E.frase(c, t, b_, [("lado", "i", 90, CLARO), ("a", "i", 90, CLARO), ("lado,", "i", 90, CLARO)], W / 2, 680, "center", passo=0.13)
        E.frase(c, t, b_ + 0.5, [("só", "i", 90, CLARO), ("primos", "g", 84, BR), ("que", "i", 90, CLARO), ("dividam", "i", 90, CLARO), ("todos", "g", 84, BR)], W / 2, 800, "center", passo=0.13)
    E.saida(c, t, C["s18"] - 0.1, nome)

    def conta():
        s0 = C["s18"]
        a_, b_, c_, d_, e_, f_, g_ = (C["s18.a"], C["s18.b"], C["s18.c"], C["s18.d"], C["s18.e"], C["s18.f"], C["s18.g"])
        p = ep(t, s0, 0.35)
        bloco(c, 130, 110, 790, 800, 24, E.PAPEL, p)  # uma folha clara: a tabela do kit é desenhada para o papel
        ini = s0 + 0.1
        ti = [a_, b_, c_, d_]
        tp = [x + 0.05 for x in ti]
        tn = [[ini, ini + 0.1]] + [[x + 0.45, x + 0.7] for x in ti]
        tb = [ini] + ti
        tabela(c, t, TJ, tn, tp, tb, GJ)
        for i in range(4):
            seta_primo(c, t, ti[i], ti[i + 1] if i < 3 else e_, i, GJ)
        contas_escuro(c, t, ti, e_ - 0.1)
        q = ep(t, e_, 0.4)  # 3 e 5: pare
        s_, y_ = GJ["s"], GJ["y0"] + 4 * GJ["dy"]
        E.caixa_pontilhada(c, GJ["xs"][0] - 90, y_ - s_ * 0.92, 400, s_ * 1.18, q, ERRADO, prog_=q)
        X = 1030
        E.frase(c, t, e_, [("3", "g", 100, BR), ("e", "i", 100, CLARO), ("5:", "g", 100, BR)], X, 300, passo=0.12)
        E.frase(c, t, e_ + 0.4, [("só", "i", 84, CLARO), ("o", "i", 84, CLARO), ("1", "g", 80, BR), ("em", "i", 84, CLARO), ("comum", "i", 84, CLARO)], X, 410, passo=0.13)
        E.frase(c, t, e_ + 0.9, [("pare", "g", 110, BR)], X, 540)
        linha(c, t, [("2", "g", 100, CLARO, f_), ("×", "g", 80, BR, f_ + 0.15), ("2", "g", 100, CLARO, f_ + 0.3), ("×", "g", 80, BR, f_ + 0.45), ("2", "g", 100, CLARO, f_ + 0.6), ("×", "g", 80, BR, f_ + 0.75), ("3", "g", 100, CLARO, f_ + 0.9)], X, 730)
        p2 = ep(t, f_ - 0.2, 0.4)
        E.caixa_pontilhada(c, GJ["xp"] - 66, GJ["y0"] - s_ * 0.95, 132, GJ["dy"] * 3 + s_ * 1.2, p2, E.COR, prog_=p2)
        bola_entra(c, t, g_, "24", 1480, 885, 110, 110, E.COR, BR)
        E.foco(c, t, g_ - 0.15, 0.3, lambda q: E.escreve(c, "MDC =", X, 920, 80, "g", BR, q))
    if t >= C["s18"]:
        E.saida(c, t, C["s19"] - 0.1, conta)

    def porque():
        a_, b_ = C["s19.a"], C["s19.b"]
        E.frase(c, t, C["s19"] + 0.2, [("por", "i", 90, CLARO), ("que", "i", 90, CLARO), ("funciona?", "i", 90, CLARO)], W / 2, 220, "center", passo=0.13)
        E.frase(c, t, a_, [("cada", "i", 96, BR), ("primo", "i", 96, BR), ("usado", "i", 96, BR), ("divide", "g", 90, CLARO), ("todos", "g", 90, CLARO)], W / 2, 420, "center", passo=0.14)
        E.frase(c, t, lerp(a_, b_, 0.6), [("essa", "i", 84, CLARO), ("é", "i", 84, CLARO), ("a", "i", 84, CLARO), ("regra", "g", 80, BR), ("do", "g", 80, BR), ("MDC", "g", 80, BR)], W / 2, 540, "center", passo=0.14)
        E.frase(c, t, b_, [("uma", "g", 130, BR), ("conta", "g", 130, BR), ("só", "g", 130, BR)], W / 2, 760, "center", passo=0.16)
        E.frase(c, t, b_ + 0.7, [("em", "i", 84, CLARO), ("vez", "i", 84, CLARO), ("de", "i", 84, CLARO), ("duas", "i", 84, CLARO), ("fatorações", "i", 84, CLARO)], W / 2, 880, "center", passo=0.14)
    if t >= C["s19"]:
        E.saida(c, t, C["s20"] - 0.1, porque)

    if t >= C["s20"]:
        s0, a_, b_, c_, d_, e_ = C["s20"], C["s20.a"], C["s20.b"], C["s20.c"], C["s20.d"], C["s20.e"]
        E.frase(c, t, s0 + 0.2, [("quando", "i", 96, CLARO), ("não", "g", 90, BR), ("compensa?", "g", 90, BR)], W / 2, 190, "center", passo=0.13)
        E.frase(c, t, a_, [("nenhuma", "i", 76, CLARO), ("regra", "i", 76, CLARO), ("mostra", "i", 76, CLARO), ("um", "i", 76, CLARO), ("primo", "g", 72, BR), ("comum", "g", 72, BR)], W / 2, 310, "center", passo=0.13)
        for n, x, y, ti in (("91", 780, 480, b_), ("65", 780, 720, b_ + 0.3)):
            bola_entra(c, t, ti, n, x, y, 100, 96, E.COR, BR)
        linha(c, t, [("=", "g", 96, CLARO, c_ - 0.1), ("7", "g", 110, BR, c_), ("×", "g", 90, CLARO, c_ + 0.15), ("13", "g", 110, CLARO, c_ + 0.3)], 930, 515)
        linha(c, t, [("=", "g", 96, CLARO, d_ - 0.1), ("5", "g", 110, BR, d_), ("×", "g", 90, CLARO, d_ + 0.15), ("13", "g", 110, CLARO, d_ + 0.3)], 930, 755)
        E.frase(c, t, lerp(b_, c_, 0.6), [("fatore", "g", 76, BR), ("cada", "i", 76, CLARO), ("um", "i", 76, CLARO)], XE, 610, passo=0.13)
        p = ep(t, e_ - 0.2, 0.4)
        E.caixa_pontilhada(c, 1200, 400, 200, 400, p, CLARO, prog_=p)
        E.frase(c, t, e_, [("MDC", "g", 130, BR), ("13", "g", 130, CLARO)], W / 2, 950, "center", passo=0.2)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    s0, a_ = C["s21"], C["s21.a"]
    E.frase(c, t, s0 + 0.3, [("hora", "i", 72, COR), ("de", "i", 72, COR), ("testar", "i", 72, COR)], XE, 200)
    E.frase(c, t, a_, [("qual", "i", 110), ("é", "i", 110), ("o", "i", 110)], XE, 400, passo=0.15)
    v = a_ + 0.5
    linha(c, t, [("MDC", "g", 170, COR, v), ("de", "i", 130, TINTA, v + 0.4)], XE, 590)
    u = lerp(a_, C["s21.end"], 0.6)
    linha(c, t, [("48", "g", 170, TINTA, u), ("e", "i", 140, TINTA, u + 0.2), ("60?", "g", 170, TINTA, u + 0.4)], XE, 810)
    relogio(c, t, C["s22.a"])


# ---------------- resposta ----------------
RX = tuple(390 + i * 195 for i in range(6))  # uma coluna para cada primo


def b_resposta(c, t, C, b):
    n48 = (2, 2, 2, 2, 3, None)
    n60 = (2, 2, None, None, 3, 5)
    y1, y2 = 300, 560
    a_, b_ = C["s23.a"], C["s23.b"]
    a2, b2, c2, d2, e2 = C["s24.a"], C["s24.b"], C["s24.c"], C["s24.d"], C["s24.e"]

    E.foco(c, t, a_, 0.4, lambda q: E.escreve(c, "48", 120, y1 + 34, 100, "g", TINTA, q))
    E.foco(c, t, b_, 0.4, lambda q: E.escreve(c, "60", 120, y2 + 34, 100, "g", TINTA, q))
    # colunas: 0 e 1 são os pares de 2, a 4 é o par de 3
    pares = {0: a2, 1: b2, 4: c2}
    ordem48 = lerp(a_, b_, 0.72)
    ordem60 = lerp(b_, C["s23.end"], 0.72)
    i48 = i60 = 0
    for j in range(6):
        ok = j in pares and t >= pares[j]
        fora = t >= d2 and j not in pares
        cor = CERTO if ok else CINZA if fora else E.COR
        if n48[j] is not None:
            bola_entra(c, t, lerp(a_, ordem48, i48 / 4), str(n48[j]), RX[j], y1, 74, 86, cor, BR)
            i48 += 1
        if n60[j] is not None:
            bola_entra(c, t, lerp(b_, ordem60, i60 / 3), str(n60[j]), RX[j], y2, 74, 86, cor, BR)
            i60 += 1
    for j, ti in pares.items():
        elo(c, t, ti, RX[j], y1 + 72, y2 - 72)
    v = C["s23"] + 0.1
    E.saida(c, t, a2 - 0.2, lambda: E.frase(c, t, v, [("fatore", "i", 84), ("cada", "i", 84), ("um", "i", 84)], W / 2, 150, "center", passo=0.13), d=0.3)
    E.frase(c, t, a2, [("formam", "i", 84), ("par:", "g", 80, CERTO)], W / 2, 150, "center", passo=0.13)
    linha(c, t, [("2", "g", 150, CERTO, d2), ("×", "g", 120, CINZA, d2 + 0.15), ("2", "g", 150, CERTO, d2 + 0.3), ("×", "g", 120, CINZA, d2 + 0.45), ("3", "g", 150, CERTO, d2 + 0.6)], 720, 860, "center")
    E.foco(c, t, e2 - 0.15, 0.3, lambda q: centro(c, "=", 1110, 850, 130, "g", CINZA, q))
    bola_entra(c, t, e2, "12", 1330, 810, 140, 130, CERTO, BR)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s25"] + 0.25, [("resumindo", "i", 96, COR)], W / 2, 210, "center")
        linhas = (("s25.a", [("fatore", "g", 80, COR), ("cada", "i", 84), ("número", "i", 84)]),
                  ("s25.b", [("junte", "g", 80, COR), ("os", "i", 84), ("primos", "i", 84), ("que", "i", 84), ("aparecem", "i", 84), ("em", "i", 84), ("todos", "g", 80, COR)]),
                  ("s25.c", [("e", "i", 84), ("multiplique", "g", 80, COR)]))
        for i, (k, partes) in enumerate(linhas):
            y = 400 + i * 200
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: num_bola(c, str(i + 1), 220, y - 28, 56, 64, a))
            E.frase(c, t, C[k] + 0.1, partes, 310, y, passo=0.14)
    E.saida(c, t, C["s26"] - 0.1, resumo)
    if t < C["s26"]:
        return
    s0 = C["s26"]
    E.frase(c, t, s0 + 0.3, [("próxima", "i", 84), ("aula", "i", 84)], XE, 260)
    E.frase(c, t, lerp(s0, C["s26.a"], 0.5), [("o", "i", 76), ("outro", "i", 76), ("lado", "i", 76), ("da", "i", 76), ("moeda", "g", 70, COR)], XE, 370, passo=0.14)
    E.frase(c, t, C["s26.a"], [("MMC", "g", 200, COR)], XE, 570)
    E.frase(c, t, C["s26.a"] + 0.5, [("o", "i", 84), ("menor", "g", 80), ("múltiplo", "i", 84), ("em", "i", 84), ("comum", "i", 84)], XE, 700, passo=0.16)
    E.foco(c, t, C["s26.b"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1400, 400, 76, estilo="g", fundo=E.COR, cor=E.SOBRE, a=a))
    p = ease_io(prog(t, C["s26.b"] + 0.3, 0.8))
    E.cursor(c, lerp(1700, 1560, p), lerp(720, 445, p), ep(t, C["s26.b"] + 0.2, 0.4), TINTA)
    E.frase(c, t, C["s26.c"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 900, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, nome=b_nome, listar=b_listar, fatorar=b_fatorar, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
