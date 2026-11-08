"""Visual — Estudativo · MAT-TOP-008: alinhamento de três pontos pelo determinante.
Mesma linguagem da MAT-TOP-007 (geometria analítica: plano à direita, eixo x em índigo, pontos em tinta, escala igual).
Peças desta aula: matriz() com as barras do determinante; coluna dos x em índigo, dos y em tinta e a dos 1 em cinza;
as duas colunas repetidas de Sarrus entram mais claras. diagonais(): "descendo para a direita" em índigo (soma que fica),
"no outro sentido" em âmbar (soma que sai). Resultado zero = verde (alinhados); diferente de zero = vermelho.
Sem voz ainda: todo instante vem de C[...] (cenas e marcadores), nunca de segundos fixos."""
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Tópicos Avançados")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-TOP-008_alinhamento_pelo_determinante.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("montar", "porque", "falta", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
AMB = "#D98A00"


def det3(m):
    (a, b, c), (d, e, f), (g, h, i) = m
    return (a * e * i + b * f * g + c * d * h), (c * e * g + a * f * h + b * d * i)


assert det3([(1, 1, 1), (2, 3, 1), (3, 5, 1)]) == (16, 16)
assert det3([(1, 1, 1), (2, 3, 1), (4, 6, 1)]) == (19, 20)
assert all(det3([(1, 1, 1), (2, 3, 1), (k, 7, 1)]) == (17 + k, 3 * k + 9) for k in range(-5, 6)) and 8 - 2 * 4 == 0
assert 1 * 4 - 2 * 2 == 0 and (2 - 1, 3 - 1) == (1, 2) and (3 - 1, 5 - 1) == (2, 4)
assert (7 - 1) / (4 - 1) == 2 and 2 * 8 - 4 * 4 == 0 and (5 - 1) / 2 == (9 - 1) / 4 == 2

PG = E.Plano(1250, 150, 540, 720, -1, 5, -1, 7)   # (1, 1), (2, 3), (3, 5) e (4, 6)


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def bola_txt(c, t, t0, s, cx, cy, r, size, cor=None):
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r * ease_back(prog(t, t0, 0.5)), cor, a),
                                     E.formula(c, str(s), cx, cy + size * 0.36, size, "g", BR, a, "center")))


def txt_em(c, t, t0, s, x, y, size, cor=TINTA, est="g", align="left"):
    E.foco(c, t, t0, 0.5, lambda a: E.formula(c, s, x, y, size, est, cor, a, align))


def plano(c, t, t0, P, size=38):
    E.plano(c, t, t0, *P.caixa, P.xmin, P.xmax, P.ymin, P.ymax, size=size, nomes=("", "y"))
    if t >= t0:
        x, y, w, h = P.caixa
        M.arrow(c, x - 10, P.oy, x + w + 44, P.oy, COR, 1.0, 6, 24, ep(t, t0, 0.6))
        E.foco(c, t, t0 + 0.5, 0.4, lambda a: E.escreve(c, "x", x + w + 26, P.oy + 62, 58, "i", COR, a))


# ---------------- matriz e Sarrus ----------------
CORES_COL = (COR, TINTA, TINTA2)


def matriz(c, t, linhas, x0, y0, cw, ch, size, tl, tc=None, trep=None, cores=None, escuro=False):
    """linhas = [(x, y, 1), ...]; tl = instante de cada linha; tc = instante de cada coluna (sobrepõe tl);
    trep = instante das duas colunas repetidas (Sarrus). cores = cor de cada célula (dict (i, j) → cor)"""
    tinta = BR if escuro else TINTA
    n = len(linhas)
    q = ep(t, min(tl), 0.4)
    if q > 0:
        for xb in (x0 - 18, x0 + 3 * cw + 18):
            M.line(c, xb, y0 - ch * 0.15, xb, y0 + n * ch - ch * 0.15, tinta, q, 6)
    for i, lin in enumerate(linhas):
        for j, v in enumerate(lin):
            t0 = tc[j] if tc else tl[i]
            t0 = max(t0, tl[i]) if tc else t0
            cor = (cores or {}).get((i, j), (CLARO, BR, "#9A9AB0")[j] if escuro else CORES_COL[j])
            E.foco(c, t, t0, 0.4, lambda a, i=i, j=j, v=v, cor=cor: centro(c, str(v), x0 + j * cw + cw / 2, y0 + i * ch + ch * 0.5, size, "g", cor, a))
        if trep is not None:
            for j in range(2):
                cor = (cores or {}).get((i, j), CORES_COL[j])
                E.foco(c, t, trep + 0.1 * i, 0.4, lambda a, i=i, j=j, cor=cor: centro(c, str(linhas[i][j]), x0 + (3 + j) * cw + cw / 2 + 30,
                                                                                    y0 + i * ch + ch * 0.5, size, "g", cor, a * 0.5))


def cel(x0, y0, cw, ch, i, j, size):
    """centro de uma célula (j = 3 e 4 são as repetidas)"""
    return x0 + j * cw + cw / 2 + (30 if j >= 3 else 0), y0 + i * ch + ch * 0.5 - size * 0.32


def diagonal(c, t, t0, x0, y0, cw, ch, size, j0, desce=True, cor=COR, d=0.6):
    p = ease_io(prog(t, t0, d))
    if p <= 0:
        return
    if desce:
        A, B = cel(x0, y0, cw, ch, 0, j0, size), cel(x0, y0, cw, ch, 2, j0 + 2, size)
    else:
        A, B = cel(x0, y0, cw, ch, 0, j0 + 2, size), cel(x0, y0, cw, ch, 2, j0, size)
    dx, dy = (B[0] - A[0]) * 0.12, (B[1] - A[1]) * 0.12
    A, B = (A[0] - dx, A[1] - dy), (B[0] + dx, B[1] + dy)
    M.line(c, A[0], A[1], lerp(A[0], B[0], p), lerp(A[1], B[1], p), cor, 0.4, 7)


# posição da matriz grande
MX, MY, MW, MH, MS = 180, 330, 150, 130, 84


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def cena1():
        plano(c, t, C["s01.a"], PG)
        for k, (x, y) in (("s01.a", (1, 1)), ("s01.b", (2, 3)), ("s01.c", (3, 5))):
            E.ponto(c, t, C[k] + 0.2, PG, x, y, f"({x}, {y})", cor=TINTA, lado=(1, 1))
        matriz(c, t, [(1, 1, 1), (2, 3, 1), (3, 5, 1)], MX, MY, MW, MH, MS, [C["s01.a"], C["s01.b"], C["s01.c"]],
               tc=None)
        E.foco(c, t, C["s01.d"], 0.4, lambda a: E.escreve(c, "determinante", MX, 800, 60, "i", TINTA, a))
        E.foco(c, t, C["s01.e"], 0.4, lambda a: E.escreve(c, "= 0", MX + 3 * MW + 60, MY + MH * 1.8, 110, "g", CERTO, a))
        E.foco(c, t, C["s01.e"] + 0.3, 0.4, lambda a: E.pilula(c, "alinhados", 500, 920, 64, "g", fundo=CERTO, a=a))
        if t >= C["s01.e"]:
            E.reta_pontos(c, t, C["s01.e"] + 0.2, PG, (1, 1), (3, 5), cor=CERTO, largura=6, pontos=False)
    E.saida(c, t, C["s02"] - 0.1, cena1)
    if t >= C["s02"]:
        E.foco(c, t, C["s02.b"] - 0.2, 0.7, lambda a: E.bola(c, 1450, 560, 270 * ease_back(prog(t, C["s02.b"] - 0.2, 0.7))), blur=0)
        E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 90), XE, 330)
        E.frase(c, t, C["s02.a"] + 0.9, [("3", "g", 120, COR), ("pontos", "g", 120)], XE, 480)
        E.frase(c, t, C["s02.a"] + 1.4, [("alinhados", "g", 120, COR)], XE, 630)
        E.frase(c, t, C["s02.a"] + 2.0, [("pelo", "i", 110), ("determinante", "g", 110)], XE, 780)
        E.foco(c, t, C["s02.b"] + 0.2, 0.5, lambda a: (E.escreve(c, "+ atalho", 1300, 545, 80, "g", BR, a),
                                                      E.escreve(c, "de prova", 1320, 630, 80, "i", BR, a)))


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], ps("você vai usar", "i", 84), XE, 200)
    E.frase(c, t, C["s03.a"], [("2", "g", 110, COR), ("coisas", "i", 100)], XE + 640, 200)
    for i, k in enumerate(("s03.b", "s03.c")):
        y = 290 + i * 340
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, XE, y, 1580, 290, p, prog_=p)
    E.frase(c, t, C["s03.b"] + 0.1, [("alinhados:", "i", 66), ("o", "i", 66), ("m", "g", 66, COR), ("não", "g", 64), ("muda", "g", 64)], XE + 50, 400)
    txt_em(c, t, C["s03.b"] + 0.8, "m = f{Δy}{Δx}", XE + 50, 530, 84)
    E.frase(c, t, C["s03.c"] + 0.1, [("determinante", "g", 64, COR), ("3", "g", 64), ("×", "g", 64), ("3:", "g", 64), ("Sarrus", "i", 66)], XE + 50, 740)
    E.foco(c, t, C["s03.c"] + 0.8, 0.4, lambda a: E.escreve(c, "descendo − no outro sentido", XE + 50, 860, 64, "g", TINTA, a))


# ---------------- montar e Sarrus ----------------
def b_montar(c, t, C, b):
    M1 = [(1, 1, 1), (2, 3, 1), (3, 5, 1)]
    tl = [C["s04.a"] + 0.2 * i for i in range(3)]
    tc = [C["s04.b"], C["s04.c"], C["s04.d"]]
    for i, (x, y) in enumerate(((1, 1), (2, 3), (3, 5))):
        E.foco(c, t, C["s04.a"] + 0.2 * i, 0.4, lambda a, i=i, x=x, y=y: E.escreve(c, f"({x}, {y})", 40, MY + i * MH + MH * 0.5 + 15, 40, "b", TINTA2, a))
    for j, (k, s, cor) in enumerate((("s04.b", "x", COR), ("s04.c", "y", TINTA), ("s04.d", "1", TINTA2))):
        E.foco(c, t, C[k], 0.4, lambda a, j=j, s=s, cor=cor: centro(c, s, MX + j * MW + MW / 2, MY - 60, 56, "i" if s != "1" else "g", cor, a))
    # descendo
    xs = 1150
    for n, k in enumerate(("s05.b", "s05.c", "s05.d")):
        diagonal(c, t, C[k], MX, MY, MW, MH, MS, n, True, COR)
    for n, (k, s) in enumerate((("s05.b", "1·3·1 = 3"), ("s05.c", "1·1·3 = 3"), ("s05.d", "1·2·5 = 10"))):
        E.foco(c, t, C[k] + 0.3, 0.4, lambda a, n=n, s=s: E.escreve(c, s, xs, 300 + n * 80, 56, "g", COR, a))
    E.foco(c, t, C["s05.e"], 0.4, lambda a: E.escreve(c, "soma = 16", xs, 560, 64, "g", COR, a))
    for n, k in enumerate(("s06.a", "s06.b", "s06.c")):
        diagonal(c, t, C[k], MX, MY, MW, MH, MS, n, False, AMB)
    xs2 = 1530
    for n, (k, s) in enumerate((("s06.a", "1·3·3 = 9"), ("s06.b", "1·1·5 = 5"), ("s06.c", "1·2·1 = 2"))):
        E.foco(c, t, C[k] + 0.3, 0.4, lambda a, n=n, s=s: E.escreve(c, s, xs2, 300 + n * 80, 56, "g", AMB, a))
    E.foco(c, t, C["s06.d"], 0.4, lambda a: E.escreve(c, "soma = 16", xs2, 560, 64, "g", AMB, a))
    matriz(c, t, M1, MX, MY, MW, MH, MS, tl, tc=tc, trep=C["s05.a"])
    E.foco(c, t, C["s06.e"], 0.5, lambda a: E.escreve(c, "16 − 16 = 0", 1150, 780, 110, "g", CERTO, a))
    E.foco(c, t, C["s06.f"], 0.5, lambda a: E.pilula(c, "alinhados", 1420, 920, 70, "g", fundo=CERTO, a=a))


# ---------------- por que funciona ----------------
def b_porque(c, t, C, b):
    def parte1():
        plano(c, t, C["s07"], PG)
        for x, y in ((1, 1), (2, 3), (3, 5)):
            E.ponto(c, t, C["s07"] + 0.2, PG, x, y, None, cor=TINTA)
        for k, A, B in (("s07.a", (1, 1), (2, 3)), ("s07.b", (2, 3), (3, 5))):
            if t >= C[k]:
                p = ease_io(prog(t, C[k], 0.6))
                (x0, y0), (x1, y1) = PG(*A), PG(*B)
                M.line(c, x0, y0, lerp(x0, x1, p), y0, "#0E9AA7", 1, 7)
                if p >= 1:
                    M.line(c, x1, y0, x1, lerp(y0, y1, ease_io(prog(t, C[k] + 0.6, 0.5))), AMB, 1, 7)
        E.foco(c, t, C["s07.a"], 0.4, lambda a: E.formula(c, "m = f{2}{1} = 2", XE, 360, 84, "g", TINTA, a))
        E.foco(c, t, C["s07.b"], 0.4, lambda a: E.formula(c, "m = f{2}{1} = 2", XE, 560, 84, "g", TINTA, a))
        E.foco(c, t, C["s07.c"], 0.4, lambda a: E.pilula(c, "mesmo m: alinhados", 460, 740, 60, "g", fundo=CERTO, a=a))
        E.frase(c, t, C["s07.d"], ps("o determinante faz o mesmo teste", "i", 56), XE, 900)
    E.saida(c, t, C["s08"] - 0.1, parte1)
    if t < C["s08"]:
        return
    M2 = [(1, 1, 1), (2, 3, 1), (4, 6, 1)]
    for n in range(3):
        diagonal(c, t, C["s08.b"] + n * 0.3, MX, MY, MW, MH, MS, n, True, COR)
        diagonal(c, t, C["s08.c"] + n * 0.3, MX, MY, MW, MH, MS, n, False, AMB)
    matriz(c, t, M2, MX, MY, MW, MH, MS, [C["s08"]] * 2 + [C["s08.a"]], trep=C["s08.a"] + 0.4, cores={(2, 0): ERRADO, (2, 1): ERRADO})
    E.foco(c, t, C["s08.f"], 0.5, lambda a: E.escreve(c, "trocar a ordem das linhas: zero continua zero", XE, 960, 54, "i", TINTA, a))
    E.foco(c, t, C["s08.b"] + 0.6, 0.4, lambda a: E.escreve(c, "3 + 4 + 12 = 19", 1150, 380, 68, "g", COR, a))
    E.foco(c, t, C["s08.c"] + 0.6, 0.4, lambda a: E.escreve(c, "12 + 6 + 2 = 20", 1150, 500, 68, "g", AMB, a))
    E.foco(c, t, C["s08.d"], 0.5, lambda a: E.escreve(c, "19 − 20 = −1", 1150, 700, 100, "g", ERRADO, a))
    E.foco(c, t, C["s08.e"], 0.5, lambda a: E.pilula(c, "≠ 0: formam um triângulo", 1440, 860, 60, "g", fundo=ERRADO, a=a))


# ---------------- o número que falta ----------------
def b_falta(c, t, C, b):
    E.frase(c, t, C["s09.a"], [("falta", "i", 76), ("um", "i", 76), ("número", "g", 70, COR)], XE, 190)
    M3 = [(1, 1, 1), (2, 3, 1), ("k", 7, 1)]
    for n in range(3):
        diagonal(c, t, C["s09.d"] + n * 0.3, MX, MY, MW, MH, MS, n, True, COR)
        diagonal(c, t, C["s09.e"] + n * 0.3, MX, MY, MW, MH, MS, n, False, AMB)
    matriz(c, t, M3, MX, MY, MW, MH, MS, [C["s09.b"]] * 3, trep=C["s09.c"], cores={(2, 0): ERRADO})
    E.foco(c, t, C["s10.d"], 0.5, lambda a: E.formula(c, "(1, 1) → (4, 7):  m = f{6}{3} = 2", XE, 900, 64, "g", CERTO, a))
    E.foco(c, t, C["s09.d"] + 0.6, 0.4, lambda a: E.escreve(c, "3 + k + 14", 1150, 360, 72, "g", COR, a))
    E.foco(c, t, C["s09.e"] + 0.6, 0.4, lambda a: E.escreve(c, "3k + 7 + 2", 1150, 480, 72, "g", AMB, a))
    E.foco(c, t, C["s10.a"], 0.5, lambda a: E.escreve(c, "(17 + k) − (3k + 9) = 0", 1000, 680, 72, "g", TINTA, a))
    E.foco(c, t, C["s10.b"], 0.5, lambda a: E.escreve(c, "8 − 2k = 0", 1000, 820, 84, "g", TINTA, a))
    bola_txt(c, t, C["s10.c"], "k = 4", 1600, 830, 120, 72, CERTO)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s11"], [("cuidado", "g", 90, ERRADO), ("com", "i", 84), ("isto", "i", 84)], XE, 200)
    E.frase(c, t, C["s11.a"], ps("somar as duas partes", "i", 70, ERRADO), 1000, 200)
    E.foco(c, t, C["s11.b"], 0.5, lambda a: E.escreve(c, "16 + 16 = 32", XE, 440, 130, "g", ERRADO, a))
    E.foco(c, t, C["s11.c"], 0.5, lambda a: E.escreve(c, "→ não alinhados?", XE + 900, 440, 70, "g", ERRADO, a))
    if t >= C["s11.d"]:
        E.risco(c, XE - 10, 470, XE + 1500, 360, t, C["s11.d"], largura=12)
    E.foco(c, t, C["s11.d"], 0.5, lambda a: E.escreve(c, "16 − 16 = 0", XE, 720, 130, "g", CERTO, a))
    E.foco(c, t, C["s11.d"] + 0.6, 0.5, lambda a: E.escreve(c, "primeira soma menos a segunda", XE, 860, 64, "i", TINTA, a))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def parte1():
        E.frase(c, t, C["s12"], [("atalho:", "i", 76, CLARO), ("leve", "i", 76, CLARO), ("o", "i", 76, CLARO), ("1º", "g", 72, BR),
                                 ("ponto", "g", 72, BR), ("à", "i", 76, CLARO), ("origem", "g", 72, BR)], W / 2, 180, "center")
        E.foco(c, t, C["s12.b"], 0.4, lambda a: E.escreve(c, "− (1, 1)", 260, 330, 70, "g", CLARO, a))
        E.foco(c, t, C["s12.c"], 0.4, lambda a: E.escreve(c, "(2, 3) → (1, 2)", 260, 450, 76, "g", BR, a))
        E.foco(c, t, C["s12.d"], 0.4, lambda a: E.escreve(c, "(3, 5) → (2, 4)", 260, 570, 76, "g", BR, a))
        if t >= C["s12.e"]:
            q = ep(t, C["s12.e"], 0.4)
            x0, y0 = 1150, 380
            for xb in (x0 - 20, x0 + 280):
                M.line(c, xb, y0 - 20, xb, y0 + 240, BR, q, 6)
            for i, (u, v) in enumerate(((1, 2), (2, 4))):
                centro(c, str(u), x0 + 60, y0 + 70 + i * 120, 90, "g", BR, q)
                centro(c, str(v), x0 + 200, y0 + 70 + i * 120, 90, "g", BR, q)
        E.foco(c, t, C["s12.e"] + 0.8, 0.5, lambda a: E.pilula(c, "1·4 − 2·2 = 0", W / 2, 820, 80, "g", fundo=CERTO, a=a))
    E.saida(c, t, C["s13"] - 0.1, parte1)
    if t < C["s13"]:
        return
    E.frase(c, t, C["s13.a"], ps("deslizar os 3 pontos juntos não muda o alinhamento", "i", 60, CLARO), W / 2, 300, "center")
    E.frase(c, t, C["s13.b"], [("2", "g", 64, BR), ("×", "g", 64, BR), ("2", "g", 64, BR), ("=", "g", 64, BR), ("multiplicar", "i", 66, CLARO),
                               ("em", "i", 66, CLARO), ("cruz", "g", 64, BR)], W / 2, 500, "center")
    E.foco(c, t, C["s13.c"], 0.5, lambda a: E.pilula(c, "dá o mesmo valor do 3 × 3", W / 2, 720, 64, "g", fundo=COR, a=a))


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s14"], ps("hora de testar", "i", 72, COR), XE, 200)
    for k, s, y in (("s14.a", "(0, 1)", 380), ("s14.b", "(2, 5)", 520), ("s14.c", "(k, 9)", 660)):
        txt_em(c, t, C[k], s, XE, y, 110, COR if "k" in s else TINTA)
    E.frase(c, t, C["s14.c"] + 0.8, [("alinhados:", "i", 84), ("k", "g", 84, COR), ("=", "g", 84), ("?", "g", 84, COR)], XE, 860)
    E.relogio(c, t, C["s15.a"], 1500, 450, 190)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    E.foco(c, t, C["s16.a"], 0.4, lambda a: E.escreve(c, "− (0, 1)", XE, 230, 70, "g", TINTA2, a))
    txt_em(c, t, C["s16.b"], "(2, 5) → (2, 4)", XE, 370, 84)
    txt_em(c, t, C["s16.c"], "(k, 9) → (k, 8)", XE, 500, 84, COR)
    E.foco(c, t, C["s16.d"], 0.5, lambda a: E.escreve(c, "2·8 − 4·k = 16 − 4k", XE, 700, 96, "g", TINTA, a))
    E.foco(c, t, C["s16.e"], 0.5, lambda a: E.escreve(c, "16 − 4k = 0", XE, 860, 96, "g", TINTA, a))
    bola_txt(c, t, C["s16.e"] + 0.6, "k = 4", 1450, 780, 140, 84, CERTO)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s17"], [("resumindo", "i", 92, COR)], W / 2, 220, "center")
        for i, (k, s) in enumerate((("s17.a", "uma linha por ponto, 1 no fim"), ("s17.b", "determinante 0: alinhados"))):
            y = 450 + i * 220
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 300, y - 30, 56, a=a), centro(c, str(i + 1), 300, y - 7, 64, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, [(s, "g", 90)], 400, y)
    E.saida(c, t, C["s18"] - 0.1, resumo)
    if t < C["s18"]:
        return
    E.frase(c, t, C["s18"], ps("próxima aula", "i", 84), XE, 300)
    E.frase(c, t, C["s18.a"], [("Duas", "g", 130), ("circunferências", "g", 130, COR)], XE, 470)
    E.frase(c, t, C["s18.b"], ps("se cortam, se encostam ou se separam", "i", 66), XE, 640)
    E.foco(c, t, C["s18.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1430, 800, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s18.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1760, 1560, p), lerp(1000, 825, p), ep(t, C["s18.c"] + 0.2, 0.4))
    E.frase(c, t, C["s18.d"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], XE, 960)


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, montar=b_montar, porque=b_porque, falta=b_falta, erro=b_erro, atalho=b_atalho,
              questao=b_questao, resposta=b_resposta, fim=b_fim)
