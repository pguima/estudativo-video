"""Visual — Estudativo · MAT-POT-009: simplificar e somar radicais.
Peças da aula: os primos dentro da raiz, com as duplas que voam para fora dela, e as caixas que se somam como radicais iguais.
Todo instante vem de C[...]: fala sem cue usa um ponto entre dois cues (lerp), para continuar certo com a voz real."""
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro, linha
import motor as M
import skia

E.usar("Matemática", "Potências e Raízes")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-POT-009_simplificar_somar_radicais.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("multiplicar", "simplificar", "somar", "atalho", "questao", "fim"))
BR = "#FFFFFF"
assert 2 * 2 * 2 * 3 * 3 == 72 and 36 * 2 == 72 and 6 ** 2 == 36 and 2 * 8 == 16 and 4 * 9 == 36
assert 4 * 3 == 12 and 25 * 3 == 75 and 36 + 64 == 100 and 6 + 8 == 14 and 8 + 18 == 26 and 12 + 75 == 87 and 72 // 36 == 2


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


def num_bola(c, s, cx, cy, r, size, a=1.0, cor=None, tinta=None):
    """número dentro da esfera"""
    E.bola(c, cx, cy + 3, r, cor, a)
    centro(c, s, cx, cy + size * 0.36, size, "g", tinta or E.SOBRE, a)


def form(c, t, t0, s, x, y, size, cor=None, align="left"):
    E.formula_em(c, t, t0, s, x, y, size, "g", cor, align)


def fase(c, t, t0, t1, fn):
    """uma tela do bloco: de t0 até sumir em t1"""
    if t0 - 0.01 <= t < t1 + 0.4:
        E.saida(c, t, t1, fn)


def par(c, t, ta, tb, esq, dir_, x, y, s, cor=None, cor_d=None):
    """fórmula em ta e a continuação em tb, logo depois dela"""
    w = E.formula(c, esq, 0, 0, s, a=0)
    form(c, t, ta, esq, x, y, s, cor)
    form(c, t, tb, dir_, x + w + s * 0.2, y, s, cor_d or cor)


FATORES = "2 × 2 × 2 × 3 × 3"


def digito_x(x, s, i, txt=FATORES):
    """centro do caractere i do texto que está dentro da raiz escrita em x"""
    ap = E.APERTO["g"] * s
    return x + s * 0.56 + (E.larg(txt[:i], "g", s) + ap if i else 0) + E.larg(txt[i], "g", s) / 2


def voa(c, t, t0, s, x0, y0, x1, y1, size, cor=None, d=0.8):
    """número que sai de (x0, y0) e pousa em (x1, y1)"""
    if t >= t0:
        q = ease_io(prog(t, t0, d))
        centro(c, s, lerp(x0, x1, q), lerp(y0, y1, q), size, "g", cor or COR)


def caixas(c, t, t0, n, x, y, l, cor=None):
    """n caixinhas lado a lado, cada uma com a fita no meio. Devolve onde a fila termina"""
    for i in range(n):
        q = ease_back(prog(t, t0 + i * 0.09, 0.4))
        if q <= 0:
            continue
        cx, r = x + i * (l + 20) + l / 2, l * min(q, 1.05)
        M.rrect(c, cx - r / 2, y + (l - r) / 2, r, r, 10, cor or E.COR)
        M.rrect(c, cx - r * 0.07, y + (l - r) / 2, r * 0.14, r * 0.42, 0, BR, 0.8)
    return x + n * (l + 20)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    a_, b_, c_ = C["s01.a"], C["s01.b"], C["s01.c"]
    fim = C["s01.end"]
    form(c, t, a_, "r{2}", 330, 340, 170)
    E.frase(c, t, a_ + 0.3, ps("não é exata", "i", 88), 280, 480, passo=0.14)
    form(c, t, b_, "r{8}", 1180, 340, 170)
    E.frase(c, t, b_ + 0.3, ps("também não", "i", 88), 1130, 480, passo=0.14)
    form(c, t, c_ - 0.1, "r{2} × r{8} =", 480, 760, 150)
    E.foco(c, t, c_, 0.5, lambda p: num_bola(c, "4", 1400, 705, 120, 150, p))
    E.frase(c, t, lerp(c_, fim, 0.55), ps("na soma,", "i", 96) + ps("a história muda", "g", 88, ERRADO), W / 2, 950, "center", 0.15)


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    a_, b_, c_, d_ = (C[f"s02.{k}"] for k in "abcd")
    E.frase(c, t, C["s02"] + 0.1, ps("você precisa de", "i", 88), XE, 210, passo=0.14)
    for x, k, l1, l2 in ((XE, a_, "raiz quadrada", "exata"), (980, b_, "fatoração", "em primos")):
        p = ep(t, k, 0.5)
        E.caixa_pontilhada(c, x, 260, 760, 200, p, prog_=p)
        E.frase(c, t, k + 0.1, [(l1, "i", 70)], x + 44, 345)
        E.frase(c, t, k + 0.3, [(l2, "g", 66, COR)], x + 44, 425)
    E.frase(c, t, lerp(b_, c_, 0.3), ps("faltou algo? procure no canal", "i", 62), XE, 560, passo=0.12)
    E.frase(c, t, c_, ps("radical:", "g", 104, COR) + ps("a raiz escrita com o símbolo", "i", 92), W / 2, 760, "center", 0.12)
    form(c, t, d_, "r{2}", W / 2, 950, 150, COR, "center")


# ---------------- multiplicar ----------------
def b_multiplicar(c, t, C, b):
    def s03():
        a, b_, c_, d = (C[f"s03.{k}"] for k in "abcd")
        E.frase(c, t, C["s03"] + 0.1, ps("comece com números fáceis", "i", 88, COR), XE, 200, passo=0.13)
        form(c, t, a, "r{4} × r{9}", XE + 30, 430, 130)
        w = E.formula(c, "r{4} × r{9}", 0, 0, 130, a=0)
        par(c, t, lerp(a, b_, 0.5), b_, "= 2 × 3", "= 6", XE + 30 + w + 26, 430, 130, None, CERTO)
        E.frase(c, t, lerp(b_, c_, 0.3), ps("em uma raiz só:", "i", 84), XE + 30, 640, passo=0.13)
        par(c, t, c_, d, "r{4 × 9} = r{36}", "= 6", XE + 30, 840, 130, COR, CERTO)

    def s04a():
        a, b_, c_, d = (C[f"s04.{k}"] for k in "abcd")
        E.frase(c, t, a, ps("raiz vezes raiz é", "i", 96) + ps("a raiz da multiplicação", "g", 84, COR), W / 2, 240, "center", 0.13)
        form(c, t, b_, "r{2} × r{8}", 250, 600, 140)
        w = E.formula(c, "r{2} × r{8}", 0, 0, 140, a=0)
        form(c, t, c_, "= r{2 × 8} = r{16}", 250 + w + 30, 600, 140, COR)
        E.foco(c, t, d, 0.5, lambda p: E.escreve(c, "=", 780, 880, 130, "g", TINTA, p))
        E.foco(c, t, d + 0.1, 0.5, lambda p: num_bola(c, "4", 1010, 835, 120, 140, p))

    def s04b():
        d, e = C["s04.d"], C["s04.e"]
        fim = C["s04.end"]
        E.frase(c, t, lerp(d, e, 0.08), ps("por quê?", "g", 96, COR), XE, 200)
        form(c, t, lerp(d, e, 0.2), "(r{2} × r{8})^2", XE + 20, 400, 110)
        form(c, t, lerp(d, e, 0.42), "= (r{2})^2 × (r{8})^2", 780, 400, 110)
        E.frase(c, t, lerp(d, e, 0.6), ps("cada raiz, ao quadrado,", "i", 78), XE + 20, 560, passo=0.11)
        E.frase(c, t, lerp(d, e, 0.78), ps("devolve o de dentro", "g", 72, COR), 960, 560, passo=0.11)
        form(c, t, e, "= 2 × 8 = 16", XE + 20, 740, 130, CERTO)
        E.frase(c, t, lerp(e, fim, 0.42), ps("o positivo que, ao quadrado, dá 16:", "i", 80), XE + 20, 930, passo=0.11)
        E.foco(c, t, lerp(e, fim, 0.85), 0.5, lambda p: num_bola(c, "4", 1560, 900, 96, 120, p))

    a4, d4, e4 = C["s04"], C["s04.d"], C["s04.e"]
    tb = lerp(d4, e4, 0.06)
    fase(c, t, C["s03"], a4 - 0.1, s03)
    fase(c, t, a4, tb - 0.1, s04a)
    fase(c, t, tb, 1e9, s04b)


# ---------------- simplificar ----------------
def b_simplificar(c, t, C, b):
    x, y, s = 560, 350, 120
    yb = 660  # segunda linha: a forma simplificada
    xa, xm, xb, xr = 610, 700, 800, 900

    def s05_6():
        a5, b5, c5 = C["s05.a"], C["s05.b"], C["s05.c"]
        a6, b6, c6, d6, e6, f6 = (C[f"s06.{k}"] for k in "abcdef")
        E.saida(c, t, a6 - 0.1, lambda: E.frase(c, t, a5, ps("a regra anda", "i", 96) + ps("ao contrário", "g", 88, COR), W / 2, 150, "center", 0.15))
        form(c, t, b5, "r{72}", XE + 20, y, 160, COR)
        E.foco(c, t, c5 - 0.1, 0.4, lambda p: E.escreve(c, "=", 480, y - 10, 110, "g", TINTA, p))
        form(c, t, c5, "r{" + FATORES + "}", x, y, s)
        E.frase(c, t, a6, ps("procure as", "i", 96) + ps("duplas", "g", 92, COR), W / 2, 150, "center", 0.15)
        cx = lambda i: digito_x(x, s, i)
        for ti, i, j in ((b6, 0, 4), (c6, 12, 16)):
            q = ep(t, ti, 0.45)
            E.caixa_pontilhada(c, cx(i) - 44, y - 106, cx(j) - cx(i) + 88, 128, q, CERTO, prog_=q)
        q = ep(t, e6, 0.45)
        E.caixa_pontilhada(c, cx(8) - 38, y - 106, 76, 128, q, ERRADO, prog_=q)
        # as duplas saem como um número só; o que sobrou fica dentro
        E.foco(c, t, d6, 0.4, lambda p: E.escreve(c, "=", 480, yb - 10, 110, "g", TINTA, p))
        voa(c, t, d6, "2", (cx(0) + cx(4)) / 2, y, xa, yb, s)
        voa(c, t, d6 + 0.35, "3", (cx(12) + cx(16)) / 2, y, xb, yb, s)
        E.foco(c, t, d6 + 0.9, 0.4, lambda p: centro(c, "×", xm, yb, 100, "g", TINTA2, p))
        E.frase(c, t, d6 + 0.2, ps("cada dupla sai da raiz", "i", 78), XE, 830, passo=0.1)
        E.frase(c, t, d6 + 1.0, ps("como um número só", "g", 72, CERTO), 910, 830, passo=0.1)
        form(c, t, f6, "r{ }", xr, yb, s, COR)
        voa(c, t, f6, "2", cx(8), y, xr + s * 0.56 + 38, yb, s, ERRADO)
        E.frase(c, t, e6, ps("sobrou um 2 sem dupla:", "i", 78), XE, 950, passo=0.1)
        E.frase(c, t, f6, ps("fica dentro", "g", 72, ERRADO), 1000, 950, passo=0.1)

    def s07():
        a, b_, c_, d = (C[f"s07.{k}"] for k in "abcd")
        fim = C["s07.end"]
        E.frase(c, t, a, ps("fora:", "i", 88), XE, 200)
        form(c, t, a + 0.1, "2 × 3 = 6", 400, 205, 100)
        E.frase(c, t, b_, ps("dentro:", "i", 88), 1000, 200)
        form(c, t, b_ + 0.1, "2", 1290, 205, 100)
        form(c, t, c_, "6r{2}", XE + 20, 490, 200, COR)
        form(c, t, d, "= 6 × r{2}", 750, 480, 130)
        E.frase(c, t, d + 0.5, ps("o vezes escondido", "i", 72), 750, 590, passo=0.12)
        E.frase(c, t, lerp(d, fim, 0.34), ps("mais de um sem dupla:", "i", 76) + ps("todos ficam dentro", "g", 70, COR), W / 2, 760, "center", 0.11)
        form(c, t, lerp(d, fim, 0.68), "r{15}", 340, 950, 110)
        E.frase(c, t, lerp(d, fim, 0.74), ps("sem dupla:", "i", 76) + ps("forma mais simples", "g", 70, COR), 640, 940, passo=0.11)

    def s08():
        a, b_, c_ = C["s08.a"], C["s08.b"], C["s08.c"]
        E.frase(c, t, C["s08"] + 0.1, ps("conferindo", "i", 100, COR), W / 2, 210, "center")
        form(c, t, a, "6^2 = 36", 310, 480, 130)
        form(c, t, b_, "(r{2})^2 = 2", 1010, 480, 130)
        form(c, t, c_, "36 × 2 = 72", W / 2, 760, 170, CERTO, "center")
        ti = lerp(c_, C["s08.end"], 0.7)
        E.foco(c, t, ti, 0.45, lambda p: E.selo(c, 860, 900, 56, True, p))
        E.frase(c, t, ti, ps("bateu", "g", 90, CERTO), 940, 930)

    fase(c, t, C["s05"], C["s07"] - 0.1, s05_6)
    fase(c, t, C["s07"], C["s08"] - 0.1, s07)
    fase(c, t, C["s08"], 1e9, s08)


# ---------------- somar ----------------
def b_somar(c, t, C, b):
    def s09():
        a, b_, c_, d, e = (C[f"s09.{k}"] for k in "abcde")
        s0 = C["s09"]
        E.frase(c, t, lerp(s0, a, 0.2), ps("raiz exata vira número comum", "i", 76), XE, 180, passo=0.1)
        E.frase(c, t, lerp(s0, a, 0.55), ps("a não exata só com", "i", 76), XE, 280, passo=0.1)
        E.frase(c, t, a, ps("mesmo número dentro", "g", 76, COR), 800, 280, passo=0.1)
        l, y = 96, 430
        xf = caixas(c, t, b_, 2, 250, y, l)
        E.sinal(c, t, b_ + 0.5, "+", xf + 50, y + 44, 90)
        xf = caixas(c, t, b_ + 0.6, 3, xf + 110, y, l)
        E.sinal(c, t, c_ - 0.1, "=", xf + 50, y + 44, 90)
        caixas(c, t, c_, 5, xf + 110, y, l)
        par(c, t, d, e, "2r{2} + 3r{2}", "= 5r{2}", 310, 790, 150, None, CERTO)

    def s10_11():
        a0, b0, c0 = C["s10.a"], C["s10.b"], C["s10.c"]
        a1, b1, c1 = C["s11.a"], C["s11.b"], C["s11.c"]
        s = 110
        form(c, t, a0, "r{8} + r{18}", XE + 20, 240, 140)
        E.frase(c, t, lerp(a0, b0, 0.35), ps("parece não ter nada igual", "i", 76), 830, 190, passo=0.11)
        E.frase(c, t, lerp(a0, b0, 0.7), ps("simplifique primeiro", "g", 72, COR), 830, 280, passo=0.13)
        form(c, t, b0, "8 = 2 × 2 × 2", XE + 20, 470, s)
        form(c, t, c0, "r{8} = 2r{2}", 1010, 470, s, COR)
        form(c, t, a1, "18 = 2 × 3 × 3", XE + 20, 650, s)
        form(c, t, b1, "r{18} = 3r{2}", 1010, 650, s, COR)
        form(c, t, c1, "2r{2} + 3r{2} = 5r{2}", W / 2, 910, 140, CERTO, "center")

    fase(c, t, C["s09"], C["s10"] - 0.1, s09)
    fase(c, t, C["s10"], 1e9, s10_11)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    def s12():
        a, b_, c_, d, e = (C[f"s12.{k}"] for k in "abcde")
        E.frase(c, t, C["s12"] + 0.1, ps("o erro mais comum:", "i", 92), 560, 190, "center", 0.13)
        E.frase(c, t, a, ps("somar o de dentro", "g", 84, ERRADO), 1310, 190, "center", 0.13)
        form(c, t, b_, "r{2} + r{3} = r{5}", W / 2, 400, 140, ERRADO, "center")
        E.frase(c, t, c_ - 0.3, ps("teste com raízes exatas:", "i", 76), XE + 20, 540, passo=0.1)
        form(c, t, c_, "r{36} + r{64} = 6 + 8", XE + 20, 690, 110)
        form(c, t, d, "= 14", 1230, 690, 110, CERTO)
        form(c, t, e, "r{100} = 10", XE + 20, 880, 110, ERRADO)
        E.foco(c, t, lerp(e, C["s12.end"], 0.72), 0.45, lambda p: E.selo(c, 900, 840, 58, False, p))
        E.frase(c, t, lerp(e, C["s12.end"], 0.72), ps("não bate", "g", 96, ERRADO), 990, 875)

    def s13():
        a, b_, c_, d, e, f = (C[f"s13.{k}"] for k in "abcdef")
        fim = C["s13.end"]
        form(c, t, a, "r{2} ≈ 1,4", XE + 20, 250, 110)
        form(c, t, b_, "r{3} ≈ 1,7", 900, 250, 110)
        form(c, t, c_, "r{2} + r{3} ≈ 3,1", XE + 20, 450, 110, CERTO)
        form(c, t, d, "r{5} ≈ 2,2", 1120, 450, 110, ERRADO)
        E.frase(c, t, e, ps("essa soma", "i", 92) + ps("fica como está", "g", 84, COR), W / 2, 620, "center", 0.14)
        form(c, t, f, "r{8} + r{18} ≠ r{26}", XE + 20, 830, 120, ERRADO)
        E.frase(c, t, lerp(f, fim, 0.55), ps("esta dá perto de 5,", "i", 66), 1090, 790, passo=0.1)
        E.frase(c, t, lerp(f, fim, 0.75), ps("a soma certa, perto de 7", "g", 54, CERTO), 1090, 880, passo=0.1)

    fase(c, t, C["s12"], C["s13"] - 0.1, s12)
    fase(c, t, C["s13"], 1e9, s13)


# ---------------- atalho ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def s14():
        a, b_, c_, d = (C[f"s14.{k}"] for k in "abcd")
        E.frase(c, t, C["s14"] + 0.1, ps("agora, o atalho", "i", 84, CLARO), W / 2, 170, "center")
        E.frase(c, t, a, ps("o maior", "i", 96, CLARO) + ps("quadrado", "g", 92, BR) + ps("que divide o número", "i", 96, CLARO), W / 2, 320, "center", 0.14)
        E.frase(c, t, lerp(a, b_, 0.45), ps("quadrado: o resultado de elevar ao quadrado, como", "i", 58, CLARO), XE + 80, 440, passo=0.07)
        form(c, t, lerp(a, b_, 0.85), "9 ou 36", 1430, 445, 72, BR)
        form(c, t, b_, "72 ÷ 36 = 2", W / 2, 640, 130, BR, "center")
        par(c, t, c_, d, "r{72} = r{36} × r{2}", "= 6r{2}", 300, 880, 130, BR, CLARO)

    def s15():
        a, b_, c_ = C["s15.a"], C["s15.b"], C["s15.c"]
        E.frase(c, t, C["s15"] + 0.1, ps("funciona porque é a", "i", 92, CLARO), W / 2, 240, "center", 0.13)
        E.frase(c, t, a, ps("regra do vezes,", "g", 100, BR) + ps("ao contrário", "i", 110, CLARO), W / 2, 370, "center", 0.15)
        E.frase(c, t, b_ - 0.4, ps("não compensa em número grande:", "i", 80, CLARO), W / 2, 570, "center", 0.11)
        form(c, t, b_, "r{1.008}", W / 2, 750, 130, BR, "center")
        E.frase(c, t, c_, ps("a", "i", 110, CLARO) + ps("fatoração", "g", 104, BR) + ps("é mais segura", "i", 110, CLARO), W / 2, 950, "center", 0.15)

    fase(c, t, C["s14"], C["s15"] - 0.1, s14)
    fase(c, t, C["s15"], 1e9, s15)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    a_ = C["s16.a"]
    E.frase(c, t, C["s16"] + 0.1, ps("hora de testar", "i", 84, COR), XE, 240)
    form(c, t, a_, "r{12} + r{75} = ?", XE, 560, 130)
    E.frase(c, t, lerp(a_, C["s16.end"], 0.7), ps("na forma mais simples", "i", 92), XE, 760, passo=0.13)
    E.relogio(c, t, C["s17.a"], 1530, 420, 180)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    a8, b8, c8, d8 = (C[f"s18.{k}"] for k in "abcd")
    a9, b9, c9, d9 = (C[f"s19.{k}"] for k in "abcd")
    s = 120
    form(c, t, a8, "12 = 4 × 3", XE + 20, 240, s)
    form(c, t, b8, "r{12} = 2r{3}", 980, 240, s, COR)
    form(c, t, c8, "75 = 25 × 3", XE + 20, 430, s)
    form(c, t, d8, "r{75} = 5r{3}", 980, 430, s, COR)
    form(c, t, a9, "2 + 5 = 7", XE + 20, 680, s)
    E.foco(c, t, b9, 0.5, lambda p: (E.bola(c, 1450, 640, 142, a=p), E.formula(c, "7r{3}", 1450, 680, 110, cor=E.SOBRE, a=p, align="center")))
    form(c, t, c9, "r{87} ≈ 9", XE + 20, 900, 110, ERRADO)
    E.foco(c, t, c9 + 0.1, 0.45, lambda p: E.selo(c, 750, 860, 50, False, p))
    form(c, t, d9, "7r{3} ≈ 12", 980, 900, 110, CERTO)
    E.foco(c, t, d9 + 0.1, 0.45, lambda p: E.selo(c, 1580, 860, 50, True, p))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s20"] + 0.1, ps("resumindo", "i", 96, COR), W / 2, 200, "center")
        itens = ((400, "s20.a", ps("no vezes,", "i", 88) + ps("tudo entra na mesma raiz", "g", 76, COR)),
                 (590, "s20.b", ps("simplificar é", "i", 88) + ps("tirar as duplas", "g", 76, COR)),
                 (780, "s20.c", ps("não exata só soma com", "i", 80) + ps("o mesmo número dentro", "g", 62, COR)))
        for i, (y, k, partes) in enumerate(itens):
            E.foco(c, t, C[k], 0.5, lambda p: num_bola(c, str(i + 1), 230, y - 30, 58, 66, p))
            E.frase(c, t, C[k] + 0.1, partes, 320, y, passo=0.12)
    E.saida(c, t, C["s21"] - 0.1, resumo)
    if t < C["s21"]:
        return
    a_, b_, c_, d_ = (C[f"s21.{k}"] for k in "abcd")
    E.frase(c, t, C["s21"] + 0.2, ps("próxima aula", "i", 84), XE, 240)
    E.frase(c, t, a_, ps("prática", "g", 130, COR), XE, 400)
    E.frase(c, t, lerp(a_, b_, 0.45), ps("calcular, estimar e simplificar", "i", 80), XE, 530, passo=0.12)
    E.frase(c, t, b_, ps("problemas de medida", "g", 96, COR), XE, 680, passo=0.15)
    E.foco(c, t, c_, 0.5, lambda p: E.pilula(c, "Inscreva-se", 1460, 360, 76, estilo="g", fundo=E.COR, cor=E.SOBRE, a=p))
    p = ease_io(prog(t, c_ + 0.3, 0.8))
    E.cursor(c, lerp(1760, 1610, p), lerp(650, 405, p), ep(t, c_ + 0.2, 0.4), TINTA)
    E.frase(c, t, d_, ps("bons", "i", 130) + ps("estudos!", "i", 130, COR), W / 2, 880, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, multiplicar=b_multiplicar, simplificar=b_simplificar, somar=b_somar, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
