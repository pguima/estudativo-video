"""Visual — Estudativo · MAT-EQU-001: a letra no lugar de um número.
O estacionamento mostra a conta que se repete e a letra que guarda o lugar das horas; depois, ler 2x + 3 pedaço por pedaço,
escrever frases em linguagem matemática, o parêntese da soma, o erro do x + 2 e o teste do dez no palco escuro.
Todo instante vem de C[...]; o que cai entre dois cues usa lerp(C[a], C[b], f), que acompanha a voz gravada."""
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Equações do 1º Grau")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-EQU-001_a_letra_no_lugar_de_um_numero.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("estacionamento", "escrever", "atalho", "questao", "fim"))
BR = "#FFFFFF"

assert 2 * 5 + 3 == 13 and 2 * 8 + 3 == 19
assert 2 * 10 + 3 == 23 and 2 * (10 + 3) == 26 and 10 + 2 == 12 and 2 * 10 == 20
assert 2 * 2 == 2 + 2 == 4
assert 3 * 10 == 30 and 30 - 4 == 26 and 3 * 10 - 4 == 26


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


def form(c, t, t0, s, x, y, size, cor=None, align="left"):
    E.formula_em(c, t, t0, s, x, y, size, "g", cor, align)


def fase(c, t, t0, t1, fn):
    """uma tela do bloco: de t0 até sumir em t1"""
    if t0 - 0.01 <= t < t1 + 0.4:
        E.saida(c, t, t1, fn)


def ate(s, size):
    """onde termina o trecho s escrito em estilo g (com o aperto depois da última letra)"""
    return E.larg(s, "g", size) + (E.APERTO["g"] * size if s else 0)


def realce(c, t, t0, s, trecho, x, y, size, cor=None, align="left", n=0):
    """fundo claro atrás de um trecho de uma fórmula escrita em estilo g; n = qual ocorrência"""
    a = ep(t, t0, 0.35)
    if a <= 0:
        return
    xi = x - ate(s, size) / 2 if align == "center" else x
    i0 = -1
    for _ in range(n + 1):
        i0 = s.find(trecho, i0 + 1)
    x0, w = xi + ate(s[:i0], size), E.larg(trecho, "g", size)
    pad = min(size * 0.14, 16)
    M.rrect(c, x0 - pad, y - size * 0.92, w + pad * 2, size * 1.2, size * 0.2, cor or COR, 0.16 * a)


def meio(s, trecho, x, size, align="left", n=0):
    """centro de um trecho dentro da fórmula"""
    xi = x - ate(s, size) / 2 if align == "center" else x
    i0 = -1
    for _ in range(n + 1):
        i0 = s.find(trecho, i0 + 1)
    return xi + ate(s[:i0], size) + E.larg(trecho, "g", size) / 2


def num_bola(c, s, cx, cy, r, size, a=1.0, cor=None, tinta=None):
    """número dentro da esfera"""
    E.bola(c, cx, cy + 3, r, cor, a)
    centro(c, s, cx, cy + size * 0.36, size, "g", tinta or E.SOBRE, a)


def seta(c, t, t0, x0, x1, y, cor=None):
    p = ep(t, t0, 0.45)
    if p > 0:
        M.arrow(c, x0, y, x1, y, cor or COR, p, 5, 16, p)


def traducao(c, t, linhas, xl, xs, xf, size_l=78, size_f=110):
    """tabela frase → fórmula: linhas = [(y, frase, t_frase, fórmula, t_fórmula, cor)]"""
    for y, fr_, tf, fo, tfo, cor in linhas:
        E.frase(c, t, tf, ps(fr_, "i", size_l), xl, y, passo=0.1)
        seta(c, t, tfo - 0.3, xs, xs + 120, y - size_l * 0.3)
        form(c, t, tfo, fo, xf, y + 8, size_f, cor)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    a_, b_, c_, d_ = (C[f"s01.{k}"] for k in "abcd")

    def conta():
        form(c, t, a_, "x = 5", XE, 300, 130, COR)
        form(c, t, b_, "2x =", 520, 640, 210)
        if t < c_ + 0.2:
            E.foco(c, t, b_ + 0.3, 0.4, lambda p: E.escreve(c, "?", 1060, 640, 210, "g", CINZA, p))
        E.foco(c, t, c_, 0.4, lambda p: E.escreve(c, "25", 1010, 640, 210, "g", ERRADO, p))
        if t >= lerp(c_, d_, 0.45):
            E.risco(c, 990, 690, 1300, 470, t, lerp(c_, d_, 0.45), largura=16)
        E.frase(c, t, lerp(c_, d_, 0.3), ps("juntou os algarismos", "i", 78, ERRADO), 1010, 820, passo=0.12)
        E.foco(c, t, d_, 0.5, lambda p: num_bola(c, "10", 1560, 570, 170 * ease_back(prog(t, d_, 0.6)), 150, p, CERTO, BR))
    E.saida(c, t, C["s02"] - 0.1, conta)
    if t < C["s02"]:
        return
    a2, b2 = C["s02.a"], C["s02.b"]
    E.frase(c, t, a2, ps("até o fim desta aula, você", "i", 84), XE, 260, passo=0.12)
    E.frase(c, t, lerp(a2, b2, 0.3), ps("lê", "g", 100), XE, 450)
    form(c, t, lerp(a2, b2, 0.35), "2x + 3", XE + 150, 455, 130, COR)
    E.frase(c, t, lerp(a2, b2, 0.55), ps("e escreve", "g", 100) + ps("frases", "i", 104), XE, 640, passo=0.15)
    E.frase(c, t, lerp(a2, b2, 0.8), ps("em linguagem", "i", 104) + ps("matemática", "g", 100, COR), XE, 790, passo=0.15)
    E.foco(c, t, b2 - 0.2, 0.7, lambda p: E.bola(c, 1600, 840, 190 * ease_back(prog(t, b2 - 0.2, 0.7))), blur=0)
    E.foco(c, t, b2 + 0.2, 0.5, lambda p: (centro(c, "+ atalho", 1600, 830, 64, "g", BR, p), centro(c, "de prova", 1600, 900, 64, "i", BR, p)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    a_, b_, c_ = C["s03.a"], C["s03.b"], C["s03.c"]
    fim = C["s03.end"]
    E.frase(c, t, C["s03"] + 0.4, ps("lembre de", "i", 92), XE, 400)
    E.foco(c, t, a_, 0.5, lambda p: E.escreve(c, "2", XE - 8, 720, 340, "g", COR, p))
    E.foco(c, t, a_ + 0.15, 0.5, lambda p: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, p))
    x, w = 880, 900
    p1 = ep(t, b_, 0.5)
    E.caixa_pontilhada(c, x, 200, w, 230, p1, prog_=p1)
    E.frase(c, t, b_ + 0.1, ps("expressão", "g", 70, COR), x + 44, 290)
    E.frase(c, t, b_ + 0.6, ps("conta com mais de uma operação", "i", 64), x + 44, 380, passo=0.1)
    p2 = ep(t, c_, 0.5)
    E.caixa_pontilhada(c, x, 480, w, 300, p2, prog_=p2)
    E.frase(c, t, c_ + 0.1, ps("a ordem", "g", 70, COR), x + 44, 570)
    # parênteses → vezes e dividido → mais e menos, na hora em que a voz fala cada um
    t1, t2, t3 = lerp(c_, fim, 0.12), lerp(c_, fim, 0.27), lerp(c_, fim, 0.48)
    y = 700
    form(c, t, t1, "( )", x + 44, y, 80)
    seta(c, t, t2 - 0.2, x + 190, x + 280, y - 25)
    form(c, t, t2, "× ÷", x + 310, y, 80)
    seta(c, t, t3 - 0.2, x + 510, x + 600, y - 25)
    form(c, t, t3, "+ −", x + 630, y, 80)
    E.frase(c, t, lerp(c_, fim, 0.78), ps("faltou alguma? procure no canal", "i", 60, TINTA2), x + 44, 900, passo=0.1)


# ---------------- por que uma letra: o estacionamento ----------------
L1 = "2 × 5 + 3"
L2 = "2 × 8 + 3"
XC, Y1, Y2, SC = 700, 600, 790, 110


def placa(c, t, a_, b_):
    E.foco(c, t, a_, 0.5, lambda p: num_bola(c, "P", XE + 90, 250, 92, 110, p))
    E.frase(c, t, a_ + 0.4, ps("entrada", "i", 72), XE + 220, 230)
    form(c, t, a_ + 0.8, "R$ 3", XE + 480, 235, 76, COR)
    E.frase(c, t, b_, ps("mais", "i", 72), XE + 220, 330)
    form(c, t, b_ + 0.2, "R$ 2", XE + 400, 335, 76, COR)
    E.frase(c, t, b_ + 0.5, ps("por hora", "i", 72), XE + 600, 330)


def b_estacionamento(c, t, C, b):
    a4, b4, c4, d4, e4, f4 = (C[f"s04.{k}"] for k in "abcdef")
    a5, b5, c5, d5 = (C[f"s05.{k}"] for k in "abcd")
    fim4 = C["s04.end"]

    def contas():
        placa(c, t, a4, b4)
        realce(c, t, a5, L1, "2 ×", XC, Y1, SC)
        realce(c, t, a5, L1, "+ 3", XC, Y1, SC)
        realce(c, t, a5 + 0.2, L2, "2 ×", XC, Y2, SC)
        realce(c, t, a5 + 0.2, L2, "+ 3", XC, Y2, SC)
        E.frase(c, t, c4, ps("5 horas", "i", 84), XE, Y1)
        form(c, t, d4, L1, XC, Y1, SC)
        form(c, t, lerp(d4, e4, 0.55), "= R$ 13", XC + ate(L1, SC) + 40, Y1, SC, COR)
        E.frase(c, t, e4, ps("8 horas", "i", 84), XE, Y2)
        form(c, t, f4, L2, XC, Y2, SC)
        form(c, t, lerp(f4, fim4, 0.6), "= R$ 19", XC + ate(L2, SC) + 40, Y2, SC, COR)
        for y, s in ((Y1, L1), (Y2, L2)):  # o número de horas acende na cor da matéria
            E.foco(c, t, b5, 0.4, lambda p, y=y, s=s: centro(c, s[4], meio(s, s[4], XC, SC), y, SC, "g", COR, p))
        E.frase(c, t, a5, ps("a conta é", "i", 60) + ps("sempre a mesma", "g", 56, COR), 1080, 250, passo=0.12)
        E.frase(c, t, b5, ps("só muda o número de horas", "i", 60), 1080, 340, passo=0.1)
        # a letra no lugar das horas
        y3 = 970
        E.frase(c, t, c5, ps("? horas", "i", 84, CINZA), XE, y3)
        form(c, t, c5 + 0.3, "2 ×", XC, y3, SC)
        form(c, t, c5 + 0.3, "+ 3", XC + ate("2 × 5 ", SC), y3, SC)
        q = ep(t, c5 + 0.3, 0.45)
        cx = meio(L1, "5", XC, SC)
        E.caixa_pontilhada(c, cx - 46, y3 - 104, 92, 128, q, COR, prog_=q)
        E.foco(c, t, d5, 0.45, lambda p: centro(c, "x", cx, y3, SC, "g", COR, p))
    E.saida(c, t, C["s06"] - 0.1, contas)
    if t < C["s06"]:
        return
    a6, b6 = C["s06.a"], C["s06.b"]
    fim6 = C["s06.end"]
    E.frase(c, t, C["s06"] + 0.3, ps("preço =", "i", 120), 440, 400)
    form(c, t, a6, "2 × x + 3", 800, 405, 150, COR)
    E.frase(c, t, b6, ps("a letra", "i", 96) + ps("guarda o lugar", "g", 88, COR) + ps("de um número", "i", 96), W / 2, 620, "center", 0.13)
    E.foco(c, t, lerp(b6, fim6, 0.35), 0.5, lambda p: E.pilula(c, "um número que muda: as horas", W / 2, 780, 58, a=p))
    E.foco(c, t, lerp(b6, fim6, 0.62), 0.5, lambda p: E.pilula(c, "ou um número que você ainda não sabe", W / 2, 920, 58, fundo=TINTA, a=p))


# ---------------- ler ----------------
def b_ler(c, t, C, b):
    a7, b7, c7 = C["s07.a"], C["s07.b"], C["s07.c"]
    fim7 = C["s07.end"]

    def s07():
        E.frase(c, t, lerp(C["s07"], a7, 0.5), ps("entre um número e uma letra,", "i", 84), W / 2, 220, "center", 0.12)
        E.frase(c, t, a7, ps("o vezes fica", "i", 92) + ps("escondido", "g", 86, COR), W / 2, 340, "center", 0.15)
        # 2 × x: o vezes some e o x encosta no 2
        size, y = 230, 650
        q = ease_io(prog(t, b7, 0.8))
        w0, w1 = ate("2 × x", size), ate("2x", size)
        x0 = lerp(W / 2 - w0 / 2, W / 2 - w1 / 2, q)
        xx = lerp(W / 2 - w0 / 2 + ate("2 × ", size), W / 2 - w1 / 2 + ate("2", size), q)
        t0 = lerp(a7, b7, 0.5)
        E.foco(c, t, t0, 0.5, lambda p: (E.escreve(c, "2", x0, y, size, "g", TINTA, p), E.escreve(c, "x", xx, y, size, "g", COR, p)))
        if t < b7 + 0.8:
            E.foco(c, t, t0, 0.5, lambda p: E.escreve(c, "×", W / 2 - w0 / 2 + ate("2 ", size), y, size, "g", TINTA, p * (1 - q)))
        E.saida(c, t, c7 - 0.1, lambda: E.frase(c, t, b7 + 0.8, ps("número colado na frente da letra", "i", 70, TINTA2), W / 2, 820, "center", 0.1))
        if t >= c7:
            E.frase(c, t, c7, [("×", "g", 140, ERRADO)] + ps("parece um", "i", 90) + [("x", "g", 140, ERRADO)], W / 2, 900, "center", 0.2)
    fase(c, t, C["s07"], C["s08"] - 0.1, s07)

    a8, b8, c8, d8 = (C[f"s08.{k}"] for k in "abcd")
    fim8 = C["s08.end"]

    def s08():
        form(c, t, a8, "2x = 2 × x", W / 2, 260, 140, COR, "center")
        form(c, t, b8, "x = 5", XE, 490, 110, COR)
        form(c, t, lerp(b8, c8, 0.4), "2 × 5 =", 620, 490, 110)
        E.foco(c, t, lerp(b8, c8, 0.6), 0.5, lambda p: num_bola(c, "10", 1180, 455, 100, 100, p, CERTO, BR))
        tv = lerp(b8, c8, 0.78)
        E.foco(c, t, tv, 0.4, lambda p: E.escreve(c, "25", 1420, 490, 110, "g", ERRADO, p))
        if t >= tv + 0.3:
            E.risco(c, 1400, 520, 1600, 400, t, tv + 0.3, largura=14)
        E.frase(c, t, c8, ps("a letra", "i", 74) + ps("não é um algarismo", "g", 66, ERRADO) + ps("para colar no 2", "i", 74), W / 2, 660, "center", 0.12)
        form(c, t, d8, "x =", 760, 890, 140)
        E.foco(c, t, lerp(d8, fim8, 0.18), 0.5, lambda p: E.escreve(c, "1", 760 + ate("x = ", 140), 890, 140, "g", CINZA, p))
        form(c, t, lerp(d8, fim8, 0.25), "x", 760 + ate("x = 1", 140), 890, 140, COR)
        E.frase(c, t, lerp(d8, fim8, 0.5), ps("o 1 está ali,", "i", 64, TINTA2), 1180, 830, passo=0.1)
        E.frase(c, t, lerp(d8, fim8, 0.7), ps("só não se escreve", "i", 64, TINTA2), 1180, 905, passo=0.1)
    fase(c, t, C["s08"], C["s09"] - 0.1, s08)

    a9, b9, c9, d9, e9 = (C[f"s09.{k}"] for k in "abcde")
    S, Y, SZ = "2x + 3", 400, 210

    def s09():
        realce(c, t, b9, S, "2x", W / 2, Y, SZ, align="center")
        realce(c, t, c9, S, "+ 3", W / 2, Y, SZ, align="center")
        form(c, t, a9, S, W / 2, Y, SZ, None, "center")
        x1, x2 = meio(S, "2x", W / 2, SZ, "center"), meio(S, "+ 3", W / 2, SZ, "center")
        E.foco(c, t, b9, 0.45, lambda p: num_bola(c, "1", 470, 530, 44, 52, p))
        E.frase(c, t, b9, ps("primeiro o vezes:", "g", 64, COR), 540, 555, passo=0.1)
        E.frase(c, t, lerp(b9, c9, 0.45), ps("duas vezes o número", "i", 72), 1110, 555, passo=0.1)
        E.foco(c, t, c9, 0.45, lambda p: num_bola(c, "2", 470, 640, 44, 52, p))
        E.frase(c, t, c9, ps("depois o mais:", "g", 64, COR), 540, 665, passo=0.1)
        E.frase(c, t, lerp(c9, d9, 0.4), ps("mais três", "i", 72), 1110, 665, passo=0.1)
        E.frase(c, t, d9, ps("o", "i", 96) + ps("dobro", "g", 90, COR) + ps("de um número mais três", "i", 96), W / 2, 820, "center", 0.12)
        E.foco(c, t, e9, 0.5, lambda p: E.pilula(c, "dobro = 2 vezes", W / 2, 950, 60, estilo="b", a=p))
    fase(c, t, C["s09"], 1e9, s09)


# ---------------- escrever ----------------
XL, XS, XF = XE + 40, 900, 1070


def b_escrever(c, t, C, b):
    a0, b0, c0, d0, e0, f0 = (C[f"s10.{k}"] for k in "abcdef")
    fim0 = C["s10.end"]

    def s10():
        E.frase(c, t, a0, ps("frase", "i", 90) + [("→", "g", 80, COR)] + ps("linguagem", "i", 90) + ps("matemática", "g", 84, COR), W / 2, 190, "center", 0.12)
        E.frase(c, t, b0, ps("pedaço por pedaço", "i", 68, TINTA2), W / 2, 290, "center", 0.12)
        traducao(c, t, [(450, "um número", c0, "x", lerp(c0, d0, 0.42), None),
                        (610, "o dobro de um número", d0, "2x", lerp(d0, e0, 0.55), None),
                        (770, "mais três", e0, "+ 3", lerp(e0, f0, 0.35), None)], XL, XS, XF)
        realce(c, t, f0, "2x + 3", "2x + 3", W / 2, 960, 140, align="center")
        form(c, t, f0, "2x + 3", W / 2, 960, 140, COR, "center")
    fase(c, t, C["s10"], C["s11"] - 0.1, s10)

    a1, b1, c1, d1 = (C[f"s11.{k}"] for k in "abcd")

    def s11():
        E.frase(c, t, a1, ps("triplo", "g", 120, COR) + ps("é três vezes", "i", 120), W / 2, 330, "center", 0.15)
        traducao(c, t, [(600, "o triplo de um número", lerp(C["s11"], b1, 0.85), "3x", b1, COR),
                        (800, "um número mais quatro", c1, "x + 4", d1, COR)], XL, XS, XF)
    fase(c, t, C["s11"], C["s12"] - 0.1, s11)

    a2, b2, c2, d2, e2, f2 = (C[f"s12.{k}"] for k in "abcdef")
    fim2 = C["s12.end"]
    t_vez, t_pista, t_sem, t_dez = lerp(d2, e2, 0.26), lerp(d2, e2, 0.51), lerp(d2, e2, 0.66), lerp(d2, e2, 0.83)
    partes = ps("o dobro da", "i", 80) + ps("soma de um número com três", "g", 72, COR)

    def p1():
        _, xs = E._arranjo(partes, W / 2, "center")
        E.frase(c, t, a2, partes, W / 2, 230, "center", 0.12)
        x0, x1 = xs[3] - 10, xs[-1] + E.larg(partes[-1][0], "g", 72) + 10
        E.chave(c, x0, x1, 262, COR, ep(t, b2, 0.6), 26, 6)
        E.foco(c, t, b2 + 0.3, 0.4, lambda p: centro(c, "a soma inteira", (x0 + x1) / 2, 360, 58, "i", COR, p))
        E.frase(c, t, c2, ps("vai entre", "i", 80) + ps("parênteses", "g", 74, COR), W / 2, 500, "center", 0.12)
        S, y, sz = "2(x + 3)", 760, 200
        xi = W / 2 - ate(S, sz) / 2
        ts = (d2, lerp(d2, e2, 0.05), lerp(d2, e2, 0.1), lerp(d2, e2, 0.16))
        for s0, s1, ti in (("", "2", ts[0]), ("2", "(", ts[1]), ("2(", "x + 3", ts[2]), ("2(x + 3", ")", ts[3])):
            cor = COR if s1 in "()" else TINTA
            E.foco(c, t, ti, 0.4, lambda p, s0=s0, s1=s1, cor=cor: E.escreve(c, s1, xi + ate(s0, sz), y, sz, "g", cor, p))
        E.foco(c, t, t_vez, 0.5, lambda p: E.pilula(c, "2 × (x + 3): o vezes escondido de novo", W / 2, 930, 54, estilo="b", fundo=TINTA, a=p))
    fase(c, t, C["s12"], t_pista - 0.15, p1)

    def p2():
        E.frase(c, t, t_pista, ps("a pista é a palavra", "i", 84) + ps("soma", "g", 80, COR), W / 2, 200, "center", 0.12)
        for i, (titulo, frase_, f, tv, v) in enumerate(((ps("sem soma", "g", 64, TINTA2), "o dobro de um número mais três", "2x + 3", e2, "23"),
                                                         (ps("com soma", "g", 64, COR), "o dobro da soma de um número com três", "2(x + 3)", f2, "26"))):
            cx = 520 + i * 880
            ti = t_pista + 0.6 if i else t_sem
            q = ep(t, ti, 0.5)
            E.caixa_pontilhada(c, cx - 400, 290, 800, 600, q, COR if i else TINTA2, prog_=q)
            E.frase(c, t, ti, titulo, cx, 380, "center")
            for k, linha_ in enumerate((frase_[:frase_.find(" de um")], frase_[frase_.find("de um"):])):
                E.foco(c, t, ti + 0.2, 0.5, lambda p, k=k, linha_=linha_: centro(c, linha_, cx, 470 + k * 66, 54, "i", TINTA, p))
            form(c, t, ti + 0.4, f, cx, 680, 120, COR if i else TINTA, "center")
            E.foco(c, t, tv, 0.5, lambda p, v=v, cx=cx: (E.escreve(c, "com x = 10:", cx - 300, 820, 56, "i", TINTA2, p),
                                                          E.escreve(c, v, cx + 40, 830, 100, "g", COR if i else TINTA, p)))
        E.foco(c, t, t_dez, 0.5, lambda p: centro(c, "testando com o número dez", W / 2, 990, 60, "i", TINTA2, p))
    fase(c, t, t_pista, 1e9, p2)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    a_, b_, c_, d_ = (C[f"s13.{k}"] for k in "abcd")
    E.frase(c, t, C["s13"] + 0.3, ps("cuidado", "g", 110, ERRADO) + ps("com este erro", "i", 100), W / 2, 200, "center")
    E.frase(c, t, lerp(C["s13"], a_, 0.6), ps("o dobro de um número", "i", 92), W / 2, 360, "center", 0.12)
    xa, xb, y = 560, 1360, 600
    form(c, t, a_, "x + 2", xa, y, 170, ERRADO, "center")
    tr = lerp(a_, b_, 0.45)
    if t >= tr:
        E.risco(c, xa - 220, y + 50, xa + 220, y - 150, t, tr, largura=16)
    E.foco(c, t, tr + 0.3, 0.4, lambda p: centro(c, "não é somar 2", xa, y + 120, 60, "i", ERRADO, p))
    form(c, t, b_, "2x", xb, y, 170, CERTO, "center")
    E.foco(c, t, b_ + 0.3, 0.4, lambda p: centro(c, "é multiplicar por 2", xb, y + 120, 60, "i", CERTO, p))
    E.foco(c, t, lerp(b_, c_, 0.5), 0.5, lambda p: centro(c, "teste com o número 10", W / 2, 840, 60, "i", TINTA2, p))
    form(c, t, c_ - 0.6, "2 × 10 = 20", xb, 960, 100, CERTO, "center")
    form(c, t, d_ - 0.5, "10 + 2 = 12", xa, 960, 100, ERRADO, "center")


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    a4, b4, c4 = C["s14.a"], C["s14.b"], C["s14.c"]

    def s14():
        E.frase(c, t, C["s14"] + 0.3, ps("agora, o atalho", "i", 90, CLARO), W / 2, 330, "center")
        E.frase(c, t, a4, ps("o teste do", "i", 170, BR) + ps("10", "g", 190, CLARO), W / 2, 580, "center", 0.2)
        E.foco(c, t, b4, 0.5, lambda p: (num_bola(c, "1", 470, 790, 46, 56, p), E.formula(c, "troque o x por 10", 550, 815, 70, "b", BR, p)))
        E.foco(c, t, c4, 0.5, lambda p: (num_bola(c, "2", 470, 920, 46, 56, p), E.escreve(c, "confira com a frase", 550, 945, 70, "b", BR, p)))
    fase(c, t, C["s14"], C["s15"] - 0.1, s14)

    a5, b5, c5 = C["s15.a"], C["s15.b"], C["s15.c"]
    fim5 = C["s15.end"]

    def s15():
        form(c, t, C["s15"] + 0.3, "2x + 3", W / 2, 260, 150, CLARO, "center")
        E.frase(c, t, a5, ps("frase:", "g", 70, CLARO) + ps("o dobro de 10 mais 3", "i", 80, BR), XE, 470, passo=0.12)
        form(c, t, lerp(a5, b5, 0.55), "20 + 3 = 23", 1180, 475, 100, BR)
        E.frase(c, t, b5 + 0.3, ps("expressão:", "g", 70, CLARO), XE, 680)
        form(c, t, lerp(b5, c5, 0.3), "2 × 10 + 3", 560, 685, 100, BR)
        form(c, t, lerp(b5, c5, 0.75), "= 23", 560 + ate("2 × 10 + 3 ", 100), 685, 100, BR)
        E.foco(c, t, c5, 0.45, lambda p: E.selo(c, 820, 880, 64, True, p))
        E.frase(c, t, c5, ps("bateu", "g", 120, BR), 920, 920)
    fase(c, t, C["s15"], C["s16"] - 0.1, s15)

    a6, b6, c6, d6 = (C[f"s16.{k}"] for k in "abcd")
    fim6 = C["s16.end"]

    def s16a():
        E.frase(c, t, a6, ps("o", "i", 110, CLARO) + ps("x", "g", 120, BR) + ps("é um número", "i", 110, CLARO), W / 2, 420, "center", 0.15)
        E.frase(c, t, b6, ps("expressão certa acerta", "i", 90, CLARO) + ps("qualquer número", "g", 84, BR), W / 2, 620, "center", 0.12)
    fase(c, t, C["s16"], c6 - 0.1, s16a)

    def s16b():
        E.frase(c, t, c6, ps("não teste com o", "i", 100, CLARO) + ps("2", "g", 120, BR), W / 2, 260, "center", 0.13)
        form(c, t, lerp(c6, d6, 0.25), "2 × 2 = 4", 330, 500, 110, BR)
        form(c, t, lerp(c6, d6, 0.4), "2 + 2 = 4", 1060, 500, 110, BR)
        E.foco(c, t, lerp(c6, d6, 0.4), 0.4, lambda p: (E.escreve(c, "dobro", 330, 590, 56, "i", CLARO, p), E.escreve(c, "mais dois", 1060, 590, 56, "i", CLARO, p)))
        E.frase(c, t, lerp(c6, d6, 0.68), ps("o erro passa", "i", 96, CLARO) + ps("escondido", "g", 90, BR), W / 2, 800, "center", 0.13)
    fase(c, t, c6, d6 - 0.1, s16b)

    def s16c():
        E.frase(c, t, d6, ps("frase de", "i", 96, CLARO) + ps("uma conta só?", "g", 90, BR), W / 2, 330, "center", 0.13)
        E.frase(c, t, lerp(d6, fim6, 0.35), ps("um número mais quatro", "i", 84, CLARO), W / 2, 530, "center", 0.12)
        form(c, t, lerp(d6, fim6, 0.55), "x + 4", W / 2, 720, 140, BR, "center")
        E.frase(c, t, lerp(d6, fim6, 0.75), ps("escreva", "i", 96, CLARO) + ps("direto", "g", 90, BR), W / 2, 920, "center", 0.13)
    fase(c, t, d6, 1e9, s16c)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    a_, b_ = C["s17.a"], C["s17.b"]
    fim = C["s17.end"]
    E.frase(c, t, C["s17"] + 0.3, ps("hora de testar", "i", 72, COR), XE, 180)
    E.frase(c, t, lerp(C["s17"], a_, 0.5), ps("escreva em", "i", 76) + ps("linguagem matemática", "g", 70, COR), XE, 290, passo=0.12)
    E.frase(c, t, a_, ps("pense em", "i", 96) + ps("um número,", "g", 90), XE, 460, passo=0.13)
    E.frase(c, t, lerp(a_, b_, 0.32), ps("calcule", "i", 96) + ps("o triplo", "g", 90, COR) + ps("dele", "i", 96), XE, 600, passo=0.13)
    E.frase(c, t, lerp(a_, b_, 0.6), ps("e", "i", 96) + ps("tire quatro", "g", 90, COR), XE, 740, passo=0.13)
    E.foco(c, t, b_, 0.5, lambda p: E.pilula(c, "confira com o teste do 10", XE + 430, 900, 60, estilo="b", a=p))
    E.relogio(c, t, C["s18.a"], 1490, 440, 200)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    a9, b9, c9, d9 = (C[f"s19.{k}"] for k in "abcd")

    def s19():
        E.frase(c, t, C["s19"] + 0.3, ps("pedaço por pedaço", "i", 72, TINTA2), W / 2, 200, "center", 0.12)
        traducao(c, t, [(380, "um número", a9, "x", lerp(a9, b9, 0.4), None),
                        (550, "o triplo dele", b9, "3x", lerp(b9, c9, 0.48), None),
                        (720, "tire quatro", c9, "− 4", lerp(c9, d9, 0.33), None)], XL, XS, XF)
        realce(c, t, d9, "3x − 4", "3x − 4", W / 2, 940, 150, CERTO, "center")
        form(c, t, d9, "3x − 4", W / 2, 940, 150, CERTO, "center")
    fase(c, t, C["s19"], C["s20"] - 0.1, s19)

    a0, b0, c0 = C["s20.a"], C["s20.b"], C["s20.c"]

    def s20():
        form(c, t, C["s20"] + 0.2, "3x − 4", W / 2, 230, 130, CERTO, "center")
        E.frase(c, t, C["s20"] + 0.5, ps("teste do 10", "i", 70, TINTA2), W / 2, 330, "center")
        E.frase(c, t, lerp(C["s20"], a0, 0.5), ps("frase:", "g", 66, COR) + ps("o triplo de 10 dá 30", "i", 76), XE, 500, passo=0.12)
        form(c, t, a0, "30 − 4 = 26", 1180, 505, 100)
        E.frase(c, t, lerp(a0, b0, 0.8), ps("expressão:", "g", 66, COR), XE, 700)
        form(c, t, b0, "3 × 10 − 4 = 26", 560, 705, 100)
        E.foco(c, t, c0, 0.45, lambda p: E.selo(c, 820, 880, 64, True, p))
        E.frase(c, t, c0, ps("bateu", "g", 120, CERTO), 920, 920)
    fase(c, t, C["s20"], 1e9, s20)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    a1, b1 = C["s21.a"], C["s21.b"]

    def resumo():
        E.frase(c, t, C["s21"] + 0.3, ps("resumindo", "i", 96, COR), W / 2, 220, "center")
        E.foco(c, t, a1, 0.5, lambda p: num_bola(c, "1", 230, 430, 58, 66, p))
        E.frase(c, t, a1 + 0.1, ps("a letra", "i", 84) + ps("guarda o lugar", "g", 76, COR) + ps("de um número", "i", 84), 320, 460, passo=0.12)
        E.foco(c, t, b1, 0.5, lambda p: num_bola(c, "2", 230, 650, 58, 66, p))
        E.frase(c, t, b1 + 0.1, ps("número colado na letra é", "i", 84) + ps("vezes", "g", 76, COR), 320, 680, passo=0.12)
        form(c, t, b1 + 1.0, "2x = 2 × x", 320, 860, 110, COR)
    E.saida(c, t, C["s22"] - 0.1, resumo)
    if t < C["s22"]:
        return
    a_, b_, c_, d_, e_ = (C[f"s22.{k}"] for k in "abcde")
    E.frase(c, t, C["s22"] + 0.2, ps("próxima aula", "i", 84), XE, 230)
    E.frase(c, t, a_, ps("trocar a letra", "g", 110, COR), XE, 380)
    E.frase(c, t, a_ + 0.4, ps("por números", "g", 110, COR), XE, 510)
    E.frase(c, t, b_, ps("até negativos", "i", 84), XE, 630, passo=0.13)
    E.frase(c, t, c_, ps("e por que o", "i", 84) + ps("parêntese", "g", 76, COR) + ps("é obrigatório", "i", 84), XE, 740, passo=0.12)
    E.foco(c, t, d_, 0.5, lambda p: E.pilula(c, "Inscreva-se", 1500, 330, 76, estilo="g", fundo=E.COR, cor=E.SOBRE, a=p))
    p = ease_io(prog(t, d_ + 0.3, 0.8))
    E.cursor(c, lerp(1780, 1640, p), lerp(620, 375, p), ep(t, d_ + 0.2, 0.4), TINTA)
    E.frase(c, t, e_, ps("bons", "i", 130) + ps("estudos!", "i", 130, COR), W / 2, 940, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, estacionamento=b_estacionamento, ler=b_ler, escrever=b_escrever,
              erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
