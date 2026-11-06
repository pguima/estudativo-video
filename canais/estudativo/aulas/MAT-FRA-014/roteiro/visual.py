"""Visual — Estudativo · MAT-FRA-014: ler, comparar e arredondar decimais.
Identidade em _ferramentas/editorial.py. Decimais sempre alinhados pela vírgula; a casa em jogo acende na fala dela."""
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco
import motor as M
import skia

E.usar("Matemática", "Frações e Decimais")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-FRA-014_ler_comparar_arredondar_decimais.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("virgula", "comparar", "atalho", "arredondar", "questao", "fim"))
BR = "#FFFFFF"


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


def num(c, t, t0, s, xv, y, size, cor=None, cores=None):
    """decimal alinhado pela vírgula, com entrada de foco"""
    E.foco(c, t, t0, 0.5, lambda a: E.numero(c, s, xv, y, size, "g", cor, a, cores))


def caixa_dig(c, cx, y, size, a=1.0, cor=None):
    """caixa pontilhada em volta de um algarismo de linha de base y"""
    E.caixa_pontilhada(c, cx - size * 0.46, y - size * 0.86, size * 0.92, size * 1.04, a, cor)


def seta(c, t, t0, x0, x1, y, cor=None):
    if t >= t0:
        p = ep(t, t0, 0.5)
        M.arrow(c, x0, y, x1, y, cor or COR, p, 6, 20, p)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def duelo():
        y, s = 590, 230
        num(c, t, C["s01.a"], "0,8", 492, y, s)
        E.foco(c, t, C["s01.b"] - 0.3, 0.4, lambda a: E.centro(c, "ou", 877, y - 20, 130, "i", TINTA2, a))
        erro = t >= C["s01.c"]
        num(c, t, C["s01.b"], "0,75", 1262, y, s, ERRADO if erro else None)
        E.frase(c, t, lerp(C["s01.b"], C["s01.c"], 0.32), [("qual", "i", 110), ("é", "i", 110), ("maior?", "g", 100, COR)], W / 2, 270, "center")
        E.frase(c, t, C["s01.c"], [("o", "i", 78), ("erro", "g", 70, ERRADO), ("mais", "i", 78), ("comum", "i", 78), ("dos", "i", 78), ("decimais", "i", 78)],
                W / 2, 830, "center", passo=0.16)
    E.saida(c, t, C["s02"] - 0.1, duelo)
    if t >= C["s02"]:
        ta, tb = C["s02.a"], C["s02.b"]
        E.foco(c, t, tb - 0.2, 0.7, lambda a: E.bola(c, 1470, 520, 290 * ease_back(prog(t, tb - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, [("até", "i", 90), ("o", "i", 90), ("fim", "i", 90), ("desta", "i", 90), ("aula", "i", 90)], XE, 360)
        E.frase(c, t, lerp(ta, tb, 0.38), [("ler,", "g", 132), ("comparar", "g", 132)], XE, 520)
        E.frase(c, t, lerp(ta, tb, 0.5), [("e", "i", 120), ("arredondar", "g", 132)], XE, 670)
        E.frase(c, t, lerp(ta, tb, 0.6), [("números", "i", 92), ("com", "i", 92), ("vírgula", "i", 92, COR)], XE, 800)
        E.foco(c, t, tb + 0.2, 0.5, lambda a: (E.escreve(c, "+ atalho", 1305, 505, 84, "g", E.SOBRE, a),
                                               E.escreve(c, "de prova", 1325, 590, 84, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def lista(c, t, C, ini, ta, n, itens):
    E.frase(c, t, C[ini], [("você", "i", 84), ("só", "i", 84), ("precisa", "i", 84), ("de", "i", 84)], XE, 410)
    E.foco(c, t, C[ta], 0.5, lambda a: E.escreve(c, str(n), XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C[ta] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 960, 780
    y0, dy = (280, 260) if len(itens) == 2 else (190, 240)
    for i, (k, l1, l2) in enumerate(itens):
        y = y0 + i * dy
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 196, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 62)], x + 44, y + 84)
        E.frase(c, t, C[k] + 0.3, [(l2, "g", 62, COR)], x + 44, y + 160)
    px = x + w - 30
    py = y0 + 170
    for i, (k, _, _) in enumerate(itens[1:], 1):
        py = lerp(py, y0 + i * dy + 170, ease_io(prog(t, C[k] - 0.35, 0.5)))
    E.cursor(c, px, py, ep(t, C[itens[0][0]], 0.4))


def b_lembrete(c, t, C, b):
    lista(c, t, C, "s03", "s03.a", 2, (("s03.b", "comparar", "números grandes"), ("s03.c", "fração é dividir", "em partes iguais")))


# ---------------- a vírgula ----------------
def b_virgula(c, t, C, b):
    E.frase(c, t, C["s04.a"], [("3 reais", "g", 84, COR), ("e", "i", 92), ("25 centavos", "g", 84, COR)], W / 2, 230, "center")
    s, y, xv = "3,25", 610, 800
    size = 320
    xs = E._centros(s, xv, size)
    qi = ep(t, C["s04.c"], 0.4)
    cores = {0: E.mix(TINTA, COR, qi), 1: COR}
    num(c, t, C["s04.b"], s, xv, y, size, None, cores)
    y_c = y + 40
    pi, pd = ep(t, C["s04.c"], 0.45), ep(t, C["s04.d"], 0.45)
    E.chave(c, xs[0] - 90, xs[0] + 90, y_c, COR, pi, 26)
    E.chave(c, xs[2] - 90, xs[3] + 90, y_c, TINTA, pd, 26)
    E.foco(c, t, C["s04.c"], 0.5, lambda a: (E.centro(c, "à esquerda,", xs[0], y_c + 100, 62, "i", TINTA, a),
                                             E.centro(c, "o inteiro", xs[0], y_c + 180, 66, "g", COR, a)))
    mid = (xs[2] + xs[3]) / 2 + 150
    E.foco(c, t, C["s04.d"], 0.5, lambda a: (E.centro(c, "à direita, o pedaço", mid, y_c + 100, 62, "i", TINTA, a),
                                             E.centro(c, "que não chega a um inteiro", mid, y_c + 180, 62, "g", TINTA, a)))


# ---------------- casas decimais ----------------
BX, BY, BW, BH = 170, 190, 1200, 140
MX, MY = 1580, 260


def _barra(c, t, ta, tb, n, partes, moeda, r):
    E.frase(c, t, ta, partes, BX, 135)
    a = ep(t, ta, 0.4)
    E.barra_fatias(c, BX, BY, BW, BH, n, 1 if t >= tb else 0, COR, a, ep(t, ta + 0.2, 0.7))
    if t >= tb:
        E.moeda(c, MX, MY, r * ease_back(prog(t, tb, 0.6)), moeda)


def b_casas(c, t, C, b):
    E.saida(c, t, C["s06"] - 0.1, lambda: _barra(c, t, C["s05.a"], C["s05.b"], 10,
                                                 [("1 real", "g", 62), ("em", "i", 68), ("10 partes iguais", "g", 62, COR)], "10¢", 105))
    if C["s06"] - 0.1 <= t:
        E.saida(c, t, C["s07"] - 0.1, lambda: _barra(c, t, C["s06.a"], C["s06.b"], 100,
                                                     [("o real", "g", 62), ("em", "i", 68), ("100 partes", "g", 62, COR)], "1¢", 85))
    if C["s07"] - 0.1 <= t:
        tn = lerp(C["s07.c"], C["s07.d"], 0.15)

        def mil():
            _barra(c, t, C["s07.a"], 1e9, 1000, [("em", "i", 68), ("1.000 partes", "g", 62, COR)], "", 0)
            k = ease_back(prog(t, tn, 0.5))
            if k > 0:
                E.moeda(c, MX, MY, 70 * k, "?", cor=CINZA)
                E.risco(c, MX - 90, MY + 90, MX + 90, MY - 90, t, tn + 0.4, largura=12)
        E.saida(c, t, C["s07.d"] - 0.1, mil)

        def tarja(a):  # a tarja do telejornal
            M.rrect(c, BX, BY, 1010, BH, 18, TINTA, a)
            E.pilula(c, "DÓLAR", BX + 180, BY + BH / 2, 56, "g", fundo=E.COR, cor=E.SOBRE, a=a)
            E.escreve(c, "R$", BX + 400, BY + 108, 96, "b", BR, a)
            E.numero(c, "5,428", BX + 640, BY + 108, 104, "g", BR, a, {4: CLARO})
        E.foco(c, t, C["s07.d"], 0.5, tarja)
    # o quadro fica: o mesmo para as três divisões
    x, y, wc, size, hl = 330, 575, 300, 74, 100
    d5, d6, c7 = C["s05.d"], C["s06.d"], C["s07.c"]
    E.quadro_casas(c, t, ("inteiro", "décimo", "centésimo", "milésimo"), (C["s05.c"], C["s05.c"], C["s06.c"], C["s07.b"]),
                   [[("0", d5), ("1", d5), ("", 0), ("", 0)], [("0", d6), ("0", d6), ("1", d6), ("", 0)], [("0", c7), ("0", c7), ("0", c7), ("1", c7)]],
                   x, y, wc, size, hl)
    for j, (ti, nome) in enumerate(((d5, "primeira casa"), (d6, "segunda casa"), (c7, "terceira casa"))):
        yy = y + hl * j + size * 1.02
        E.foco(c, t, ti, 0.4, lambda a, j=j, yy=yy: E.centro(c, "1", x + (j + 1.5) * wc, yy, size, "g", COR, a))
        E.foco(c, t, ti + 0.1, 0.45, lambda a, nome=nome, yy=yy: E.escreve(c, nome, x + 4 * wc + 26, yy - 6, 50, "i", COR, a))
    E.saida(c, t, C["s06"] - 0.1, lambda: E.frase(c, t, C["s05.e"], [("casa", "g", 60, COR), ("decimal:", "g", 60, COR), ("cada", "i", 66), ("lugar", "i", 66), ("depois", "i", 66),
                                                                      ("da", "i", 66), ("vírgula", "i", 66)], W / 2, 985, "center", passo=0.13))


# ---------------- leitura ----------------
def b_leitura(c, t, C, b):
    def tres():
        E.frase(c, t, C["s08.a"], [("duas", "g", 76, COR), ("formas", "i", 84), ("de", "i", 84), ("ler", "i", 84)], W / 2, 170, "center")
        s, xv, y, size = "3,25", 880, 440, 230
        xs = E._centros(s, xv, size)
        ultima = ep(t, C["s08.d"], 0.4)
        num(c, t, C["s08.a"] + 0.2, s, xv, y, size, None, {3: E.mix(TINTA, COR, ultima)})
        if ultima > 0:
            caixa_dig(c, xs[3], y, size, ultima)
        E.foco(c, t, C["s08.d"], 0.5, lambda a: E.pilula(c, "última casa", 1480, y - 90, 58, a=a, cor=E.SOBRE))
        E.frase(c, t, C["s08.b"], [("a", "i", 66, COR), ("rápida:", "i", 66, COR), ("três", "g", 58), ("vírgula", "g", 58), ("vinte", "g", 58), ("e", "g", 58),
                                   ("cinco", "g", 58)], W / 2, 650, "center", passo=0.12)
        E.frase(c, t, C["s08.c"], [("a", "i", 66, COR), ("completa:", "i", 66, COR), ("três", "g", 58), ("inteiros", "g", 58), ("e", "g", 58), ("vinte", "g", 58),
                                   ("e", "g", 58), ("cinco", "g", 58), ("centésimos", "g", 58, COR)], W / 2, 800, "center", passo=0.12)
    E.saida(c, t, C["s09"] - 0.1, tres)
    if t >= C["s09"]:
        num(c, t, C["s09.a"], "0,8", 900, 480, 290, None, {2: COR})
        E.frase(c, t, C["s09.a"] + 0.6, [("termina", "i", 84), ("nos", "i", 84), ("décimos", "g", 76, COR)], W / 2, 640, "center")
        E.frase(c, t, C["s09.b"], [("oito", "g", 140), ("décimos", "g", 140, COR)], W / 2, 860, "center")


# ---------------- comparar ----------------
def b_comparar(c, t, C, b):
    y1, y2 = 310, 560

    def moedas():
        num(c, t, C["s10.a"], "0,8", 290, y1, 140, E.COR)
        for i in range(8):
            E.foco(c, t, C["s10.a"] + 0.5 + i * 0.13, 0.35, lambda a, i=i: E.moeda(c, 604 + i * 88, y1 - 48, 44, "10¢", a))
        E.foco(c, t, C["s10.b"], 0.5, lambda a: E.escreve(c, "80 centavos", 1340, y1 - 22, 68, "g", COR, a))
        num(c, t, C["s10.c"], "0,75", 290, y2, 140)
        for i in range(7):
            E.foco(c, t, C["s10.d"] + i * 0.08, 0.35, lambda a, i=i: E.moeda(c, 604 + i * 88, y2 - 48, 44, "10¢", a))
        E.foco(c, t, C["s10.d"] + 0.56, 0.35, lambda a: E.moeda(c, 604 + 7 * 88 - 6, y2 - 48, 32, "5¢", a))
        E.foco(c, t, C["s10.d"] + 0.3, 0.5, lambda a: E.escreve(c, "75 centavos", 1340, y2 - 22, 68, "g", TINTA, a))
        E.frase(c, t, C["s11.a"], [("0,8", "g", 130, COR), ("é", "i", 120), ("maior", "i", 120), ("que", "i", 120), ("0,75", "g", 130)], W / 2, 850, "center", passo=0.2)
    E.saida(c, t, C["s12"] - 0.1, moedas)
    if t < C["s12"]:
        return
    E.frase(c, t, C["s12.a"], [("compare", "i", 84), ("casa", "g", 76, COR), ("por", "g", 76, COR), ("casa", "g", 76, COR)], W / 2, 170, "center")
    x0 = 640
    p = ep(t, C["s12.a"] + 0.5, 0.8)
    M.arrow(c, x0, 235, x0 + 640, 235, TINTA2, p, 5, 18, p)
    E.foco(c, t, C["s12.a"] + 0.5, 0.5, lambda a: E.centro(c, "da esquerda para a direita", W / 2, 305, 52, "i", TINTA2, a))
    xv, ya, yb, size = 960, 540, 730, 180
    xs = E._centros("0,75", xv, size)
    tb, tc, td = C["s12.b"], C["s12.c"], C["s12.d"]
    tn = lerp(td, C["s12.end"], 0.55)
    apaga = ep(t, tn, 0.4)
    num(c, t, C["s12.a"] + 0.3, "0,8", xv, ya, size, None, {2: E.mix(TINTA, COR, ep(t, tc, 0.4))})
    num(c, t, C["s12.a"] + 0.5, "0,75", xv, yb, size, None, {3: E.mix(TINTA, CINZA, apaga)})
    if t >= tb:
        cx = lerp(xs[0], xs[2], ease_io(prog(t, tc - 0.2, 0.5)))
        q = ep(t, tb, 0.4)
        E.caixa_pontilhada(c, cx - 88, ya - 170, 176, 380, q, prog_=q)
    if t >= tn:
        E.risco(c, xs[3] - 62, yb + 18, xs[3] + 62, yb - 138, t, tn, largura=10)
    fala = ((tb, tc, [("inteiros:", "i", 72), ("zero", "g", 64), ("e", "i", 72), ("zero,", "g", 64), ("empate", "g", 64, COR)]),
            (tc, td, [("décimos:", "i", 72), ("8", "g", 64, COR), ("contra", "i", 72), ("7", "g", 64)]),
            (td, 1e9, [("a", "i", 72), ("comparação", "i", 72), ("termina", "i", 72), ("aqui", "g", 64, COR)]))
    for t0, t1, partes in fala:
        if t0 <= t:
            E.saida(c, t, t1 - 0.1, lambda partes=partes, t0=t0: E.frase(c, t, t0, partes, W / 2, 925, "center", passo=0.12))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s13.a"] - 0.8, [("ler", "i", 74), ("depois", "i", 74), ("da", "i", 74), ("vírgula", "i", 74)], W / 2, 170, "center", passo=0.13)
    E.frase(c, t, C["s13.a"], [("como", "i", 74), ("número", "g", 66, ERRADO), ("inteiro", "g", 66, ERRADO)], W / 2, 265, "center", passo=0.13)
    y = 520
    E.frase(c, t, C["s13.b"], [("75", "g", 210, ERRADO), ("é", "i", 130), ("maior", "i", 130), ("que", "i", 130), ("8", "g", 210, ERRADO)], W / 2, y, "center", passo=0.16)
    if t >= C["s13.c"]:
        E.risco(c, 480, y - 165, 1440, y + 30, t, C["s13.c"], largura=16)
    E.frase(c, t, C["s13.c"], [("esse", "i", 84), ("8", "g", 76, COR), ("vale", "i", 84), ("80", "g", 76, COR), ("centavos", "g", 76, COR)], W / 2, 720, "center")
    E.frase(c, t, C["s13.d"], [("mais", "i", 76), ("algarismos", "g", 68), ("não", "i", 76), ("significa", "i", 76), ("número", "i", 76), ("maior", "g", 68, ERRADO)],
            W / 2, 900, "center", passo=0.15)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def um():
        E.frase(c, t, C["s14"] + 0.1, [("agora,", "i", 76, CLARO), ("o", "i", 76, CLARO), ("atalho:", "i", 76, CLARO)], W / 2, 170, "center")
        E.frase(c, t, C["s14.a"], [("iguale", "g", 92, BR), ("as", "g", 92, BR), ("casas", "g", 92, BR), ("com", "i", 100, CLARO), ("zeros", "g", 92, BR)], W / 2, 300, "center", passo=0.13)
        xv, ya, yb, size = 500, 560, 770, 190
        E.foco(c, t, C["s14.a"] + 0.3, 0.5, lambda a: E.numero(c, "0,8", xv, ya, size, "g", BR, a))
        E.foco(c, t, C["s14.a"] + 0.5, 0.5, lambda a: E.numero(c, "0,75", xv, yb, size, "g", BR, a))
        q = ep(t, C["s14.b"], 0.4) * (1 - ep(t, C["s14.d"], 0.3))
        xs = E._centros("0,80", xv, size)
        if q > 0:
            E.caixa_pontilhada(c, xs[3] - 88, ya - 165, 176, 200, q, CLARO, prog_=q)
        E.foco(c, t, C["s14.c"], 0.5, lambda a: E._so(c, "0,80", xv, ya, size, [3], CLARO, a))
        E.frase(c, t, C["s14.d"], [("80", "g", 170, CLARO), ("com", "i", 110, BR), ("75", "g", 170, BR)], 1340, 680, "center")

    E.saida(c, t, C["s15"] - 0.1, um)
    if t < C["s15"]:
        return
    E.frase(c, t, C["s15.a"], [("zero", "g", 76, BR), ("no", "i", 84, CLARO), ("fim,", "i", 84, CLARO), ("depois", "i", 84, CLARO), ("da", "i", 84, CLARO), ("vírgula,", "i", 84, CLARO)],
            W / 2, 210, "center", passo=0.12)
    E.frase(c, t, C["s15.a"] + 0.8, [("não", "g", 76, BR), ("muda", "g", 76, BR), ("o", "g", 76, BR), ("valor", "g", 76, BR)], W / 2, 320, "center", passo=0.12)
    E.frase(c, t, C["s15.a"] + 1.4, [("0,8", "g", 150, BR), ("=", "g", 130, CLARO), ("0,80", "g", 150, CLARO)], W / 2, 540, "center")
    E.frase(c, t, lerp(C["s15.a"], C["s15.b"], 0.5), [("8", "g", 64, BR), ("moedas", "i", 70, CLARO), ("de", "i", 70, CLARO), ("10", "g", 64, BR), ("centavos:", "i", 70, CLARO),
                                                       ("80", "g", 64, BR), ("centavos", "i", 70, CLARO)], W / 2, 680, "center", passo=0.1)
    E.foco(c, t, C["s15.b"], 0.5, lambda a: E.selo(c, 360, 860, 72, False, a))
    E.frase(c, t, C["s15.b"] + 0.1, [("não", "i", 84, CLARO), ("compensa", "i", 84, CLARO), ("com", "i", 84, CLARO), ("muitas", "g", 76, BR), ("casas", "g", 76, BR)], 470, 885, passo=0.12)


# ---------------- arredondar ----------------
def b_arredondar(c, t, C, b):
    def caixa_():
        size, xv, y = 230, 960, 430
        E.foco(c, t, C["s16.a"], 0.5, lambda a: E.escreve(c, "R$", 350, y, 130, "b", TINTA2, a))
        num(c, t, C["s16.a"], "3,146", xv - 120, y, size, None, {4: E.mix(TINTA, ERRADO, ep(t, C["s16.b"], 0.4))})
        E.frase(c, t, C["s16.b"], [("não", "i", 76), ("existe", "i", 76), ("moeda", "i", 76), ("menor", "i", 76), ("que", "i", 76), ("um", "i", 76), ("centavo", "g", 68, ERRADO)],
                W / 2, 640, "center", passo=0.13)
        E.frase(c, t, C["s16.c"], [("trocar", "i", 80), ("pelo", "i", 80), ("vizinho", "g", 72, COR), ("mais", "g", 72, COR), ("próximo", "g", 72, COR)], W / 2, 800, "center", passo=0.13)
        E.frase(c, t, C["s16.c"] + 0.9, [("com", "i", 80), ("menos", "i", 80), ("casas", "i", 80)], W / 2, 900, "center", passo=0.13)
    E.saida(c, t, C["s17"] - 0.1, caixa_)

    def vizinhos():
        x0, x1, y = 380, 1540, 520
        vx = E.reta(c, t, C["s17.a"], x0, x1, y, 3.14, 3.15, ())
        ti = lerp(C["s17.b"], C["s17.c"], 0.2)
        for k, v, s in (("s17.a", 3.14, "3,14"), ("s17.b", 3.15, "3,15")):
            xc = vx(v)
            xt = xc - E.larg(s + "0", "g", 76) / 2
            E.foco(c, t, C[k], 0.45, lambda a, xc=xc, s=s, xt=xt: (M.line(c, xc, y - 24, xc, y + 24, TINTA, a, 6), E.escreve(c, s, xt, y + 112, 76, "g", TINTA, a)))
            E.foco(c, t, ti, 0.45, lambda a, s=s, xt=xt: E.escreve(c, "0", xt + E.larg(s, "g", 76) + 4, y + 112, 76, "g", COR, a))
        xp = vx(3.146)
        k = ease_back(prog(t, C["s17.c"], 0.5))
        if k > 0:
            E.bola(c, xp, y, 26 * k)
            E.centro(c, "3,146", xp, y - 62, 76, "g", COR, ep(t, C["s17.c"], 0.4))
            p = ep(t, C["s17.c"] + 0.4, 0.6)
            M.arrow(c, xp + 36, y, vx(3.15) - 12, y, E.COR, p, 8, 22, p)
        E.frase(c, t, C["s17.c"], [("146", "g", 90, COR), ("está", "i", 96), ("mais", "g", 90), ("perto", "g", 90), ("de", "i", 96), ("150", "g", 90, COR)], W / 2, 860, "center", passo=0.13)
    if C["s17"] - 0.1 <= t:
        E.saida(c, t, C["s18"] - 0.1, vizinhos)

    def regra():
        E.frase(c, t, C["s18.a"], [("olhe", "i", 86), ("o", "i", 86), ("algarismo", "g", 76), ("logo", "g", 76), ("depois", "g", 76)], W / 2, 240, "center", passo=0.1)
        E.frase(c, t, C["s18.a"] + 1.0, [("da", "i", 86), ("última", "i", 86), ("casa", "i", 86), ("que", "i", 86), ("vai", "i", 86), ("ficar", "i", 86)], W / 2, 350, "center", passo=0.1)
        E.frase(c, t, C["s18.b"], [("5", "g", 110, COR), ("ou", "i", 110), ("mais:", "g", 92), ("essa", "i", 104), ("casa", "i", 104), ("sobe", "g", 92, COR), ("um", "g", 92, COR)], W / 2, 590, "center", passo=0.12)
        E.frase(c, t, C["s18.c"], [("menos", "i", 104), ("que", "i", 104), ("5:", "g", 110, COR), ("fica", "g", 92), ("como", "g", 92), ("está", "g", 92)], W / 2, 800, "center", passo=0.12)
    if C["s18"] - 0.1 <= t:
        E.saida(c, t, C["s19"] - 0.1, regra)

    def aqui():
        s, xv, y, size = "3,146", 860, 460, 260
        xs = E._centros(s, xv, size)
        ka, kb, kc = C["s19.a"], C["s19.b"], C["s19.c"]
        num(c, t, C["s19"], s, xv, y, size, None, {3: E.mix(TINTA, COR, ep(t, ka, 0.4)), 4: E.mix(TINTA, CERTO, ep(t, kb, 0.4))})
        if t >= ka:
            cx = lerp(xs[3], xs[4], ease_io(prog(t, kb - 0.2, 0.5)))
            caixa_dig(c, cx, y, size, ep(t, ka, 0.4))
        E.foco(c, t, ka, 0.5, lambda a: E.centro(c, "a última casa que fica", xs[3] - 40, 610, 58, "i", COR, a))
        E.foco(c, t, kb, 0.5, lambda a: E.pilula(c, "logo depois", xs[4] + 240, y - 100, 54, fundo=CERTO, a=a))
        E.corta(c, t, lerp(kb, kc, 0.55), xs[3], y - size * 0.36, size, 5, cor_novo=CERTO)
        E.foco(c, t, kc, 0.5, lambda a: (E.bola(c, 960, 810, 150, CERTO, a), E.centro(c, "3,15", 960, 845, 104, "g", BR, a)))
    if C["s19"] - 0.1 <= t:
        E.saida(c, t, C["s20"] - 0.1, aqui)

    if t >= C["s20"]:
        for y, s, ta, tb, r in ((270, "3,142", "s20.a", "s20.b", "3,14"), (740, "3,145", "s20.e", "s20.e", "3,15")):
            igual = ta == tb
            num(c, t, C[ta], s, 540, y, 170, None, {4: COR})
            seta(c, t, C[tb] + (0.4 if igual else 0), 975, 1075, y - 58, TINTA2)
            num(c, t, C[tb] + (0.6 if igual else 0.1), r, 1270, y, 170, CERTO)
        E.frase(c, t, C["s20.a"] + 0.6, [("2", "g", 64, COR), ("é", "i", 66), ("menos", "i", 66), ("que", "i", 66), ("5", "g", 64)], W / 2, 375, "center", passo=0.1)
        E.frase(c, t, C["s20.c"], [("e", "i", 92), ("se", "i", 92), ("for", "i", 92), ("exatamente", "i", 92), ("5?", "g", 84, COR)], W / 2, 530, "center", passo=0.12)
        E.foco(c, t, C["s20.d"], 0.5, lambda a: E.pilula(c, "por combinação, 5 manda subir", W / 2, 920, 62, "b", a=a, cor=E.SOBRE))


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s21"], [("hora", "i", 72, COR), ("de", "i", 72, COR), ("testar", "i", 72, COR)], XE, 190)
    xv = 780
    for y, nome, s, k in ((380, "banco A", "5,7", "s21.a"), (540, "banco B", "5,685", "s21.b")):
        E.foco(c, t, C[k] - 0.5, 0.5, lambda a, nome=nome, y=y: E.escreve(c, nome, XE, y, 80, "g", COR, a))
        E.foco(c, t, C[k], 0.5, lambda a, y=y: E.escreve(c, "R$", 530, y, 76, "b", TINTA2, a))
        num(c, t, C[k], s, xv, y, 130)
    E.frase(c, t, C["s21.c"], [("qual", "i", 104), ("é", "i", 104), ("o", "i", 104), ("mais", "g", 92, COR), ("barato?", "g", 92, COR)], XE, 720)
    E.frase(c, t, C["s21.d"], [("e", "i", 78), ("o", "i", 78), ("preço", "i", 78), ("do", "i", 78), ("banco", "i", 78), ("B,", "g", 70), ("arredondado", "g", 70, COR)], XE, 860, passo=0.13)
    E.frase(c, t, C["s21.d"] + 1.2, [("para", "i", 78), ("centavos?", "g", 70, COR)], XE, 955, passo=0.13)
    E.relogio(c, t, C["s22.a"], 1520, 390, 200)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    def compara():
        E.frase(c, t, C["s23"] + 0.3, [("iguale", "i", 76), ("as", "i", 76), ("casas", "i", 76)], W / 2, 170, "center")
        xv, y1, y2, size = 640, 400, 590, 170
        xs = E._centros("5,700", xv, size)
        E.foco(c, t, C["s23.a"], 0.5, lambda a: (E.numero(c, "5,7", xv, y1, size, "g", TINTA, a), E._so(c, "5,700", xv, y1, size, [3, 4], COR, a)))
        num(c, t, C["s23.b"], "5,685", xv, y2, size, None, {2: E.mix(TINTA, COR, ep(t, C["s23.c"], 0.4))})
        if t >= C["s23.c"]:
            q = ep(t, C["s23.c"], 0.4)
            E.caixa_pontilhada(c, xs[2] - 84, y1 - 165, 168, 380, q, prog_=q)
        E.frase(c, t, C["s23.c"] + 0.2, [("nos", "i", 76), ("décimos:", "i", 76)], 1120, 430)
        E.frase(c, t, C["s23.c"] + 0.5, [("6", "g", 92, COR), ("é", "i", 92), ("menor", "i", 92), ("que", "i", 92), ("7", "g", 92)], 1120, 540, passo=0.1)
        E.foco(c, t, C["s23.d"], 0.5, lambda a: (E.bola(c, 980, 840, 120, CERTO, a), E.centro(c, "B", 980, 880, 120, "g", BR, a)))
        E.frase(c, t, C["s23.d"] + 0.3, [("o", "i", 84), ("mais", "g", 76, CERTO), ("barato", "g", 76, CERTO)], 1130, 870)
    E.saida(c, t, C["s24"] - 0.1, compara)
    if t < C["s24"]:
        return
    s, xv, y, size = "5,685", 860, 450, 240
    xs = E._centros(s, xv, size)
    ka, kb, kc = C["s24.a"], C["s24.b"], C["s24.c"]
    num(c, t, C["s24"], s, xv, y, size, None, {3: E.mix(TINTA, COR, ep(t, ka, 0.4)), 4: E.mix(TINTA, CERTO, ep(t, kb, 0.4))})
    if t >= ka:
        caixa_dig(c, lerp(xs[3], xs[4], ease_io(prog(t, kb - 0.2, 0.5))), y, size, ep(t, ka, 0.4))
    E.foco(c, t, kb, 0.5, lambda a: E.pilula(c, "manda subir", xs[4] + 250, y - 100, 54, fundo=CERTO, a=a))
    E.corta(c, t, lerp(kb, kc, 0.6), xs[3], y - size * 0.36, size, 9, cor_novo=CERTO)
    E.foco(c, t, kc, 0.5, lambda a: (E.bola(c, 520, 810, 150, CERTO, a), E.centro(c, "5,69", 520, 845, 104, "g", BR, a)))
    E.frase(c, t, kc + 0.3, [("5", "g", 86), ("reais", "i", 92), ("e", "i", 92), ("69", "g", 86), ("centavos", "i", 92)], 730, 840, passo=0.13)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s25"], [("resumindo", "i", 92, COR)], W / 2, 210, "center")
        for i, (k, s) in enumerate((("s25.a", "a última casa dá o nome"), ("s25.b", "compare casa por casa"), ("s25.c", "de 5 para cima, sobe"))):
            y = 390 + i * 190
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 300, y - 30, 56, a=a),
                                                         E.centro(c, str(i + 1), 300, y - 7, 64, "g", E.SOBRE, a)))
            E.frase(c, t, C[k] + 0.1, [(s, "g", 92)], 400, y)
    E.saida(c, t, C["s26"] - 0.1, resumo)
    if t < C["s26"]:
        return
    E.frase(c, t, C["s26"] + 0.1, [("próxima", "i", 84), ("aula", "i", 84)], XE, 300)
    E.frase(c, t, C["s26.a"], [("Somar", "g", 140, COR), ("e", "i", 130), ("subtrair", "g", 140, COR)], XE, 450)
    E.frase(c, t, C["s26.a"] + 0.3, [("decimais", "g", 140, COR)], XE, 595)
    E.foco(c, t, C["s26.b"], 0.5, lambda a: E.pilula(c, "troco e dívida", 1010, 545, 62, a=a, cor=E.SOBRE))
    E.foco(c, t, C["s26.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1440, 690, 76, estilo="g", a=a, cor=E.SOBRE))
    p = ease_io(prog(t, C["s26.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1770, 1570, p), lerp(960, 715, p), ep(t, C["s26.c"] + 0.2, 0.4))
    E.frase(c, t, C["s26.d"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 900, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, virgula=b_virgula, casas=b_casas, leitura=b_leitura, comparar=b_comparar,
              erro=b_erro, atalho=b_atalho, arredondar=b_arredondar, questao=b_questao, resposta=b_resposta, fim=b_fim)
