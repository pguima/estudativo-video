"""Visual — Estudativo · MAT-NUM-011: qual conta o problema pede.
Identidade em _ferramentas/editorial.py. Aula de leitura: cada conta tem esfera, equação, tira que mostra a quantidade e palavras-pista
em pílulas. Peças locais: sim (conta na esfera), pilulas e tira (comprimento = quantidade, para comparar Ana e Bia, água e luz)."""
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco
import motor as M
import skia

E.usar("Matemática", "Números e Contas")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-NUM-011_qual_conta_o_problema_pede.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("pergunta", "pista", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


def bola_txt(c, t, t0, s, cx, cy, r, size, cor=CERTO):
    """o resultado na esfera"""
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r, cor, a), E.centro(c, s, cx, cy + size * 0.35, size, "g", M.on(cor), a)))


def lin(c, t, t0, s, x, y, size=64, estilo="b", cor=None):
    """uma linha do painel ao lado da conta"""
    E.foco(c, t, t0, 0.4, lambda a: E.escreve(c, s, x, y, size, estilo, cor or TINTA, a))


def igual(c, t, t0, t1, s1, s2, x, y, size=66, estilo="b", cor=None, cor2=None):
    """conta em duas partes: a pergunta em t0 e o resultado só em t1, quando a voz chega nele"""
    lin(c, t, t0, s1, x, y, size, estilo, cor)
    lin(c, t, t1, s2, x + E.larg(s1 + " ", estilo, size), y, size, estilo, cor2 or cor or COR)


def lista(c, t, C, ini, ta, n, itens):
    E.frase(c, t, C[ini] + 0.7, [("você", "i", 84), ("só", "i", 84), ("precisa", "i", 84), ("de", "i", 84)], XE, 410)
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


def sim(c, t, t0, s, cx, cy, r, size=None, cor=None):
    """a conta na esfera: + − × ÷"""
    size = size or r * 1.15
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r, cor, a), E.centro(c, s, cx, cy + size * 0.36, size, "g", M.on(cor or E.COR), a)))


def pilulas(c, t, t0, itens, x, y, size=60, passo_=0.45):
    """as palavras-pista, uma a uma, na fala"""
    for i, s in enumerate(itens):
        w = E.larg(s, "b", size) + size * 1.1
        E.foco(c, t, t0 + i * passo_, 0.4, lambda a, s=s, x=x, w=w: E.pilula(c, s, x + w / 2, y, size, estilo="b", cor=E.SOBRE, a=a))
        x += w + 34


def tira(c, x, y, w, h, cor, a, s=None, tom=None, size=56):
    """tira de quantidade: o comprimento mostra o tamanho"""
    if a <= 0 or w <= 0:
        return
    M.rrect(c, x, y, w, h, 10, cor, a)
    if s:
        E.centro(c, s, x + w / 2, y + h / 2 + size * 0.36, size, "g", tom or M.on(cor), a)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def tudo():
        ka, kb, kcc, kd, ke = C["s01.a"], C["s01.b"], C["s01.c"], C["s01.d"], C["s01.e"]
        E.linha(c, t, [("Ana", "g", 120, COR, ka), ("tem", "i", 110, TINTA, ka + 0.4), ("R$ 30", "g", 120, TINTA, ka + 0.7)], W / 2, 230, "center")
        vermelho = t >= kd
        xs = E.linha(c, t, [("isso é", "i", 92, TINTA, kb), ("R$ 5", "g", 92, TINTA, kb + 0.4), ("a", "i", 92, TINTA, kb + 0.8), ("mais", "g", 92, ERRADO if vermelho else TINTA, kb + 1.0), ("do que", "i", 92, TINTA, kb + 1.3), ("Bia tem", "g", 92, TINTA, kb + 1.6)], W / 2, 390, "center")
        if vermelho:
            q = ep(t, kd, 0.3)
            E.caixa_pontilhada(c, xs[3] - 18, 390 - 84, E.larg("mais", "g", 92) + 36, 110, q, ERRADO, prog_=q)
        E.frase(c, t, kcc, [("quanto", "i", 110), ("Bia", "g", 100, COR), ("tem?", "i", 110)], W / 2, 560, "center", passo=0.2)
        E.foco(c, t, lerp(kd, ke, 0.55), 0.5, lambda a: E.escreve(c, "somou?", 540, 780, 120, "i", TINTA, a))
        E.foco(c, t, ke, 0.5, lambda a: E.escreve(c, "R$ 35", 920, 790, 150, "g", ERRADO, a))
        E.foco(c, t, ke + 0.4, 0.5, lambda a: E.selo(c, 1470, 740, 84, False, a))
        E.frase(c, t, ke + 0.3, [("está", "i", 84), ("errado", "g", 76, ERRADO)], W / 2, 930, "center", passo=0.2)
    E.saida(c, t, C["s02"] - 0.1, tudo)
    if t >= C["s02"]:
        ta, tb = C["s02.a"], C["s02.b"]
        E.foco(c, t, tb - 0.2, 0.7, lambda a: E.bola(c, 1500, 520, 270 * ease_back(prog(t, tb - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, [("até", "i", 90), ("o", "i", 90), ("fim", "i", 90), ("desta", "i", 90), ("aula", "i", 90)], XE, 340)
        E.frase(c, t, lerp(ta, tb, 0.29), [("escolher", "g", 110), ("a", "i", 100)], XE, 490, passo=0.3)
        E.frase(c, t, lerp(ta, tb, 0.34), [("conta", "g", 110, COR)], XE, 620)
        E.frase(c, t, lerp(ta, tb, 0.41), [("pelo", "i", 84), ("sentido", "g", 76, COR), ("do", "i", 84), ("texto", "i", 84)], XE, 740, passo=0.2)
        E.frase(c, t, lerp(ta, tb, 0.6), [("não", "i", 76), ("por", "i", 76), ("uma", "i", 76), ("palavra", "i", 76), ("solta", "i", 76)], XE, 850, passo=0.2)
        E.foco(c, t, tb + 0.2, 0.5, lambda a: (E.centro(c, "+ atalho", 1500, 505, 84, "g", E.SOBRE, a),
                                               E.centro(c, "de prova", 1500, 590, 84, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"] + 0.7, [("você", "i", 96), ("só", "i", 96), ("precisa", "i", 96)], XE, 470, passo=0.2)
    E.frase(c, t, C["s03"] + 1.4, [("saber", "g", 96, COR)], XE, 590)
    x = 920
    for i, (k, s, sub, sg) in enumerate((("s03.a", "somar", "", "+"), ("s03.b", "subtrair", "", "−"), ("s03.c", "multiplicar", "", "×"), ("s03.d", "dividir", "por um algarismo", "÷"))):
        y = 200 + i * 212
        sim(c, t, C[k], sg, x + 70, y, 70)
        E.frase(c, t, C[k] + 0.1, [(s, "g", 92, COR)], x + 180, y + (34 if not sub else 8))
        if sub:
            E.frase(c, t, C[k] + 0.4, [(sub, "i", 66)], x + 180, y + 72)


# ---------------- a pergunta ----------------
def b_pergunta(c, t, C, b):
    ka, kb = C["s04.a"], C["s04.b"]
    E.frase(c, t, C["s04"] + 0.1, [("todo", "i", 92), ("problema:", "i", 92), ("uma", "i", 92), ("pergunta", "g", 84, COR)], W / 2, 180, "center", passo=0.25)
    E.frase(c, t, ka, [("saindo", "i", 88), ("do", "i", 88), ("que", "i", 88), ("eu", "i", 88), ("sei", "g", 80)], W / 2, 340, "center", passo=0.25)
    E.frase(c, t, lerp(ka, kb, 0.24), [("para", "i", 88), ("chegar", "i", 88), ("ao", "i", 88), ("que", "i", 88), ("o", "i", 88), ("problema", "i", 88), ("pede,", "g", 80)], W / 2, 460, "center", passo=0.25)
    E.frase(c, t, lerp(ka, kb, 0.63), [("o", "i", 96), ("que", "i", 96), ("acontece", "i", 96), ("com", "i", 96), ("a", "i", 96), ("quantidade?", "g", 92, COR)], W / 2, 610, "center", passo=0.25)
    E.foco(c, t, kb - 0.1, 0.4, lambda a: E.escreve(c, "4 respostas", XE, 860, 92, "g", TINTA, a))
    for i, s in enumerate("+−×÷"):
        sim(c, t, kb + 0.5 + i * 0.25, s, 870 + i * 240, 830, 90)


# ---------------- as quatro contas ----------------
BX, BW, BY, BH = 372, 1176, 560, 100


def barra_soma(c, t, C):
    b_, c_ = C["s05.b"], C["s05.c"]
    E.foco(c, t, b_, 0.45, lambda a: tira(c, BX, BY, 840, BH, E.COR, a, "R$ 300"))
    E.foco(c, t, c_, 0.45, lambda a: tira(c, BX + 846, BY, 330, BH, TINTA, a, "R$ 120"))


def barra_sub(c, t, C):
    b_, c_, d_ = C["s06.b"], C["s06.c"], C["s06.d"]
    E.foco(c, t, b_, 0.45, lambda a: tira(c, BX, BY, 840, BH, E.COR, a, None if t >= c_ else "R$ 300"))
    if t >= c_:
        q = ep(t, c_, 0.4)
        M.rrect(c, BX + 840 - 336, BY, 336, BH, 10, E.PAPEL, q)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(BX + 840 - 336, BY, 336, BH), 10, 10), M.paint(ERRADO, q, stroke=4))
        E.centro(c, "R$ 120", BX + 840 - 168, BY + BH / 2 + 20, 56, "g", ERRADO, q)
    E.foco(c, t, d_, 0.45, lambda a: E.centro(c, "R$ 180", BX + 252, BY + BH / 2 + 20, 56, "g", E.SOBRE, a))


def barra_mult(c, t, C):
    b_, c_ = C["s07.b"], C["s07.c"]
    E.foco(c, t, b_, 0.45, lambda a: E.barra_fatias(c, BX, BY, BW, BH, 6, 6, E.COR, a))
    for i in range(6):
        E.foco(c, t, c_ + i * 0.1, 0.35, lambda a, i=i: E.centro(c, "12", BX + (i + 0.5) * BW / 6, BY + BH / 2 + 22, 62, "g", E.SOBRE, a))


def barra_div(c, t, C):
    b_, c_, d_ = C["s08.b"], C["s08.c"], C["s08.d"]
    E.foco(c, t, b_, 0.45, lambda a: E.barra_fatias(c, BX, BY, BW, BH, 6, 6, E.COR, a, ep(t, c_, 0.6)))
    for i in range(6):
        E.foco(c, t, d_ + i * 0.1, 0.35, lambda a, i=i: E.centro(c, "R$ 14", BX + (i + 0.5) * BW / 6, BY + BH / 2 + 19, 52, "g", E.SOBRE, a))


def cena(c, t, C, sid, sg, perg, nome, partes, barra, pistas, t_pista, extra=None):
    ka, kb, kcc, kd, ke = (C[f"{sid}.{x}"] for x in "abcde")
    fim_p = lerp(ka, kb, 0.6)
    sim(c, t, fim_p, sg, 260, 245, 100)
    E.frase(c, t, ka, [(p, "i", 88) for p in perg], 410, 215, passo=0.22)
    E.frase(c, t, fim_p, [("é", "i", 96), (nome, "g", 104, COR)], 410, 335, passo=0.2)
    E.linha(c, t, [partes[0] + (kb,), partes[1] + (kcc - 0.1,), partes[2] + (kcc,), partes[3] + (kd - 0.2,), partes[4] + (kd,)], W / 2, 500, "center")
    barra(c, t, C)
    if extra:
        extra()
    E.foco(c, t, t_pista, 0.4, lambda a: E.escreve(c, "pistas:", XE, 880, 76, "i", TINTA, a))
    pilulas(c, t, ke, pistas, 400, 858)


def b_quatro(c, t, C, b):
    g = lambda s, cor=None: (s, "g", 92, cor or TINTA)

    def f5():
        cena(c, t, C, "s05", "+", ("está", "juntando", "ou", "aumentando?"), "soma",
             (g("R$ 300", COR), g("+"), g("R$ 120"), g("="), g("R$ 420", COR)), barra_soma, ("recebeu", "ganhou", "juntou"), lerp(C["s05.d"], C["s05.e"], 0.7))

    def f6():
        cena(c, t, C, "s06", "−", ("está", "tirando", "ou", "diminuindo?"), "subtração",
             (g("R$ 300", COR), g("−"), g("R$ 120", ERRADO), g("="), g("R$ 180", COR)), barra_sub, ("gastou", "perdeu", "sobrou", "falta"), C["s06.e"] - 0.5)

    def f7():
        fim = lerp(C["s07.d"], C["s07.e"], 0.22)
        fala = lambda: E.foco(c, t, fim, 0.5, lambda a: E.centro(c, "12 + 12 + 12 + 12 + 12 + 12", W / 2, 770, 60, "b", TINTA2, a))
        cena(c, t, C, "s07", "×", ("está", "repetindo", "grupos", "iguais?"), "multiplicação",
             (g("6 caixas", COR), g("×"), g("12 ovos"), g("="), g("72 ovos", COR)), barra_mult, ("cada", "por dia", "o dobro"), C["s07.e"] - 0.5, fala)

    def f8():
        cena(c, t, C, "s08", "÷", ("está", "repartindo", "em", "partes", "iguais?"), "divisão",
             (g("R$ 84", COR), g("÷"), g("6 pessoas"), g("="), g("R$ 14", COR)), barra_div, ("entre", "igualmente", "a metade"), C["s08.e"] - 0.5)
    ini = ("s05", "s06", "s07", "s08")
    for i, (sid, fn) in enumerate(zip(ini, (f5, f6, f7, f8))):
        fim = C[ini[i + 1]] - 0.1 if i < 3 else 1e9
        if t >= C[sid]:
            E.saida(c, t, fim, fn)


# ---------------- pista não é regra ----------------
def b_pista(c, t, C, b):
    def f9():
        k = {x: C["s09." + x] for x in "abcdef"}
        E.frase(c, t, k["a"], [("pistas,", "g", 110, COR), ("não", "i", 120), ("regras", "g", 110, ERRADO)], W / 2, 190, "center", passo=0.2)
        E.frase(c, t, lerp(k["a"], k["b"], 0.4), [("nenhuma", "i", 76), ("palavra", "i", 76), ("decide", "i", 76), ("sozinha", "i", 76)], W / 2, 300, "center", passo=0.22)
        E.foco(c, t, k["b"], 0.45, lambda a: E.pilula(c, "cada", 290, 470, 76, estilo="b", cor=E.SOBRE, a=a))
        lin(c, t, k["c"], "72 ovos,", 480, 495, 80, "g")
        E.linha(c, t, [("6", "g", 80, TINTA, k["d"]), ("em", "i", 84, TINTA, k["d"] + 0.2), ("cada", "g", 80, COR, k["d"] + 0.4), ("caixa", "i", 84, TINTA, k["d"] + 0.6)], 860, 495)
        E.frase(c, t, k["e"], [("quantas", "i", 96), ("caixas?", "g", 92, COR)], XE, 640, passo=0.2)
        tv = lerp(k["e"], k["f"], 0.2)
        E.frase(c, t, tv, [("os", "i", 72), ("ovos", "i", 72), ("já", "i", 72), ("estão", "i", 72), ("contados:", "i", 72)], XE, 760, passo=0.2)
        E.frase(c, t, tv + 1.5, [("separar", "g", 66, COR), ("em", "i", 72), ("grupos", "i", 72)], XE, 860, passo=0.2)
        sim(c, t, k["f"], "÷", 1270, 760, 92)
        E.frase(c, t, k["f"] + 0.2, [("divisão:", "g", 72, COR)], 1400, 730)
        E.foco(c, t, lerp(k["f"], C["s09.end"], 0.4), 0.45, lambda a: E.escreve(c, "12 caixas", 1400, 820, 72, "g", TINTA, a))
    E.saida(c, t, C["s10"] - 0.1, f9)
    if t >= C["s10"]:
        k = {x: C["s10." + x] for x in "abcde"}
        E.frase(c, t, C["s10"] + 0.1, [("o", "i", 92), ("mesmo", "i", 92), ("vale", "i", 92), ("para", "i", 92)], XE, 225, passo=0.14)
        E.foco(c, t, k["a"], 0.45, lambda a: E.pilula(c, "sobrou", 1010, 200, 76, estilo="b", cor=E.SOBRE, a=a))
        lin(c, t, k["b"], "gastou R$ 80", XE, 390, 84, "g")
        lin(c, t, k["c"], "sobraram R$ 120", 800, 390, 84, "g")
        E.frase(c, t, k["d"], [("quanto", "i", 100), ("tinha", "i", 100), ("antes?", "g", 92, COR)], XE, 540, passo=0.2)
        tv = lerp(k["d"], k["e"], 0.2)
        E.frase(c, t, tv, [("do", "i", 72), ("que", "i", 72), ("sobrou", "i", 72), ("até", "i", 72), ("o", "i", 72), ("que", "i", 72), ("tinha:", "i", 72)], XE, 670, passo=0.22)
        E.frase(c, t, lerp(k["d"], k["e"], 0.72), [("a", "i", 72), ("quantidade", "i", 72), ("aumenta", "g", 66, COR)], 1000, 670, passo=0.2)
        igual(c, t, k["e"], lerp(k["e"], C["s10.end"], 0.3), "80 + 120 =", "200", XE, 820, 110, "g")
        sim(c, t, lerp(k["e"], C["s10.end"], 0.55), "+", 1190, 790, 92)
        E.frase(c, t, lerp(k["e"], C["s10.end"], 0.58), [("a", "i", 84), ("conta", "i", 84), ("é", "i", 84), ("soma", "g", 76, COR)], 1310, 820, passo=0.2)


# ---------------- erro ----------------
BA, BU = 340, 20  # início das tiras e pixels por real


def b_erro(c, t, C, b):
    def f11():
        ka, kb, kcc = C["s11.a"], C["s11.b"], C["s11.c"]
        a2, b2, c2 = C["s12.a"], C["s12.b"], C["s12.c"]
        tv = lerp(ka, kb, 0.72)
        E.saida(c, t, C["s12"] - 0.1, lambda: E.frase(c, t, ka, [("obedecer", "g", 80, ERRADO), ("à", "i", 88), ("palavra", "i", 88), ("sem", "i", 88), ("ler", "i", 88), ("a", "i", 88), ("frase", "g", 80)], W / 2, 170, "center", passo=0.22))
        if t >= C["s12"]:
            E.frase(c, t, C["s12"] + 0.1, [("dos", "i", 88), ("R$ 30", "g", 80), ("dela", "i", 88), ("até", "i", 88), ("o", "i", 88), ("valor", "i", 88), ("de", "i", 88), ("Bia", "g", 80, COR)], W / 2, 170, "center", passo=0.2)
        y1, y2, h = 300, 440, 104
        E.foco(c, t, tv, 0.45, lambda a: (E.escreve(c, "Ana", XE, y1 + 76, 76, "g", COR, a), tira(c, BA, y1, 30 * BU, h, E.COR, a, "R$ 30", None, 64)))
        E.foco(c, t, tv + 0.3, 0.45, lambda a: (E.escreve(c, "Bia", XE, y2 + 76, 76, "g", TINTA, a), tira(c, BA, y2, 25 * BU, h, TINTA, a, None if t >= b2 else "?", None, 64)))
        E.foco(c, t, b2, 0.45, lambda a: E.centro(c, "R$ 25", BA + 25 * BU / 2, y2 + h / 2 + 23, 64, "g", BR, a))
        q = ep(t, kcc, 0.4)
        if q > 0:  # os R$ 5 de diferença
            E.chave(c, BA + 25 * BU + 6, BA + 30 * BU, y2 + 8, COR, q, 26, 5)
            E.foco(c, t, kcc, 0.4, lambda a: E.escreve(c, "R$ 5", BA + 30 * BU + 24, y2 + 44, 60, "g", COR, a))

        def fala():
            E.frase(c, t, kb, [("ninguém", "i", 84), ("ganhou", "g", 76), ("nada:", "i", 84)], XE, 690, passo=0.2)
            E.frase(c, t, lerp(kb, kcc, 0.5), [("a", "i", 84), ("frase", "i", 84), ("só", "i", 84), ("compara", "g", 76, COR)], 1010, 690, passo=0.2)
            E.frase(c, t, kcc, [("quem", "i", 100), ("tem", "i", 100), ("mais?", "g", 92, COR)], XE, 840, passo=0.2)
            E.frase(c, t, lerp(kcc, C["s11.end"], 0.6), [("é", "i", 100), ("a", "i", 100), ("Ana", "g", 92, COR)], 880, 840, passo=0.15)
        E.saida(c, t, C["s12"] - 0.1, fala)
        if t >= C["s12"]:
            E.frase(c, t, a2, [("a", "i", 92), ("quantidade", "i", 92), ("diminui", "g", 84, COR)], XE, 700, passo=0.2)
            igual(c, t, b2, lerp(b2, c2, 0.6), "30 − 5 =", "25", XE, 860, 110, "g")
            lin(c, t, c2, "confira na história:", 990, 700, 70, "i")
            igual(c, t, c2 + 0.9, lerp(c2, C["s12.end"], 0.7), "25 + 5 =", "30", 990, 860, 110, "g")
            E.foco(c, t, lerp(c2, C["s12.end"], 0.85), 0.5, lambda a: E.selo(c, 1690, 820, 70, True, a))
    E.saida(c, t, C["s13"] - 0.1, f11)
    if t >= C["s13"]:
        ka, kb, kcc, kd, ke = C["s13.a"], C["s13.b"], C["s13.c"], C["s13.d"], C["s13.e"]
        E.frase(c, t, C["s13"] + 0.1, [("o", "i", 84), ("contrário", "i", 84), ("também", "i", 84), ("engana", "g", 76, ERRADO)], W / 2, 150, "center", passo=0.2)
        y1, y2, h, u, BA2 = 230, 350, 96, 16, 390
        E.foco(c, t, ka, 0.45, lambda a: (E.escreve(c, "água", XE, y1 + 70, 70, "g", COR, a), tira(c, BA2, y1, 40 * u, h, E.COR, a, "R$ 40", None, 60)))
        E.foco(c, t, kb, 0.45, lambda a: (E.escreve(c, "luz", XE, y2 + 70, 70, "g", TINTA, a), tira(c, BA2, y2, 48 * u, h, TINTA, a, None if t >= ke + 0.8 else "?", None, 60)))
        E.foco(c, t, ke + 0.8, 0.45, lambda a: E.centro(c, "R$ 48", BA2 + 24 * u, y2 + h / 2 + 22, 60, "g", BR, a))
        q = ep(t, kb + 0.4, 0.4)
        if q > 0:
            E.chave(c, BA2 + 40 * u + 4, BA2 + 48 * u, y1 + h - 6, COR, q, -26, 5)
            E.foco(c, t, kb + 0.4, 0.4, lambda a: E.escreve(c, "R$ 8", BA2 + 48 * u + 30, y1 + h - 6, 60, "g", COR, a))
        E.frase(c, t, kb, [("R$ 8", "g", 76), ("a", "i", 84), ("menos", "g", 76, ERRADO), ("do", "i", 84), ("que", "i", 84), ("a", "i", 84), ("conta", "i", 84), ("de", "i", 84), ("luz", "g", 76)], XE, 560, passo=0.18)
        E.frase(c, t, kcc, [("quanto", "i", 84), ("deu", "i", 84), ("a", "i", 84), ("de", "i", 84), ("luz?", "g", 76, COR)], XE, 670, passo=0.2)
        E.frase(c, t, kd, [("quem", "i", 84), ("custou", "i", 84), ("mais", "g", 76, COR), ("foi", "i", 84), ("a", "i", 84), ("luz", "g", 76, COR)], XE, 780, passo=0.2)
        igual(c, t, ke, ke + 0.8, "40 + 8 =", "48", XE, 930, 110, "g")


# ---------------- mais de uma conta ----------------
def b_passos(c, t, C, b):
    k = {x: C["s14." + x] for x in "abcdef"}
    E.frase(c, t, k["a"], [("mais", "i", 100), ("de", "i", 100), ("uma", "i", 100), ("conta", "g", 92, COR)], W / 2, 170, "center", passo=0.16)
    E.linha(c, t, [("3 camisas", "g", 80, TINTA, k["b"]), ("de", "i", 84, TINTA, k["b"] + 0.5), ("R$ 40,", "g", 80, TINTA, k["b"] + 0.7), ("pagas com", "i", 84, TINTA, k["c"]), ("R$ 200", "g", 80, TINTA, k["c"] + 0.5)], XE, 320)
    E.frase(c, t, k["d"], [("qual", "i", 92), ("é", "i", 92), ("o", "i", 92), ("troco?", "g", 84, COR)], XE, 450, passo=0.2)
    y1, y2 = 620, 830
    tp = lerp(k["d"], k["e"], 0.55)
    sim(c, t, tp, "×", 240, y1 - 26, 70)
    lin(c, t, tp, "repete grupos iguais:", 340, y1 - 44, 60, "i")
    igual(c, t, k["e"], lerp(k["e"], k["f"], 0.55), "3 × 40 =", "120", 340, y1 + 44, 88, "g")
    sim(c, t, lerp(k["e"], k["f"], 0.72), "−", 240, y2 - 26, 70)
    lin(c, t, lerp(k["e"], k["f"], 0.72), "depois, tira:", 340, y2 - 44, 60, "i")
    igual(c, t, k["f"], lerp(k["f"], C["s14.end"], 0.65), "200 − 120 =", "80", 340, y2 + 44, 88, "g")
    bola_txt(c, t, lerp(k["f"], C["s14.end"], 0.75), "R$ 80", 1490, 720, 150, 88)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def f15():
        k = {x: C["s15." + x] for x in "abcdefgh"}
        E.frase(c, t, C["s15"] + 0.1, [("agora,", "i", 72, CLARO), ("o", "i", 72, CLARO), ("atalho:", "i", 72, CLARO)], W / 2, 130, "center", passo=0.1)
        E.frase(c, t, k["a"], [("troque", "i", 110, CLARO), ("por", "i", 110, CLARO), ("números", "i", 110, CLARO), ("pequenos", "g", 100, BR)], W / 2, 260, "center", passo=0.18)
        E.linha(c, t, [("912 folhetos", "g", 80, BR, k["b"]), ("em pacotes de", "i", 84, CLARO, k["c"]), ("6", "g", 80, BR, k["c"] + 0.6)], XE, 410)
        E.frase(c, t, k["d"], [("quantos", "i", 84, CLARO), ("pacotes?", "g", 76, BR)], 1200, 410, passo=0.2)
        E.linha(c, t, [("10 folhetos", "g", 80, CLARO, k["e"]), ("em pacotes de", "i", 84, CLARO, k["e"] + 0.8), ("2", "g", 80, CLARO, k["e"] + 1.4)], XE, 570)
        E.frase(c, t, k["f"], [("dá", "i", 84, CLARO), ("5,", "g", 80, BR), ("e", "i", 84, CLARO), ("você", "i", 84, CLARO), ("dividiu", "g", 80, BR)], XE, 690, passo=0.2)
        E.foco(c, t, k["g"], 0.5, lambda a: E.escreve(c, "912 ÷ 6 =", XE, 880, 120, "g", BR, a))
        E.foco(c, t, k["h"], 0.5, lambda a: E.escreve(c, "152", XE + E.larg("912 ÷ 6 = ", "g", 120), 880, 130, "g", CLARO, a))
        E.frase(c, t, k["h"] + 0.6, [("pacotes", "i", 96, CLARO)], XE + 790, 880)
    E.saida(c, t, C["s16"] - 0.1, f15)
    if t >= C["s16"]:
        ka, kb = C["s16.a"], C["s16.b"]
        E.frase(c, t, ka, [("a", "i", 110, CLARO), ("conta", "i", 110, CLARO), ("depende", "i", 110, CLARO), ("da", "i", 110, CLARO), ("história", "g", 100, BR)], W / 2, 330, "center", passo=0.2)
        E.frase(c, t, ka + 1.6, [("não", "i", 84, CLARO), ("do", "i", 84, CLARO), ("tamanho", "i", 84, CLARO), ("dos", "i", 84, CLARO), ("números", "i", 84, CLARO)], W / 2, 460, "center", passo=0.2)
        E.foco(c, t, kb, 0.5, lambda a: E.selo(c, 300, 690, 72, False, a))
        E.frase(c, t, kb + 0.1, [("não", "i", 80, CLARO), ("compensa", "i", 80, CLARO), ("se", "i", 80, CLARO), ("a", "i", 80, CLARO), ("história", "g", 72, BR), ("já", "i", 80, CLARO), ("está", "i", 80, CLARO), ("clara", "g", 72, BR)], 410, 715, passo=0.15)
        E.frase(c, t, kb + 2.4, [("aí,", "i", 84, CLARO), ("vá", "g", 76, BR), ("direto", "g", 76, BR), ("à", "g", 76, BR), ("conta", "g", 76, BR)], 410, 840, passo=0.12)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s17"] + 0.1, [("hora", "i", 72, COR), ("de", "i", 72, COR), ("testar", "i", 72, COR)], XE, 200)
    E.linha(c, t, [("Caio tem", "i", 92, TINTA, C["s17.a"] - 0.5), ("45 anos", "g", 96, COR, C["s17.a"])], XE, 380)
    E.linha(c, t, [("isso é", "i", 92, TINTA, C["s17.b"] - 0.4), ("3 vezes", "g", 96, COR, C["s17.b"])], XE, 510)
    E.frase(c, t, C["s17.b"] + 0.7, [("a", "i", 92), ("idade", "i", 92), ("da", "i", 92), ("filha", "g", 84)], XE, 630, passo=0.2)
    E.frase(c, t, C["s17.c"], [("que", "i", 92), ("conta", "g", 84, COR), ("resolve?", "g", 84, COR)], XE, 790, passo=0.2)
    E.frase(c, t, lerp(C["s17.c"], C["s17.end"], 0.42), [("quantos", "i", 92), ("anos", "i", 92), ("tem", "i", 92), ("a", "i", 92), ("filha?", "g", 84, COR)], XE, 900, passo=0.2)
    E.relogio(c, t, C["s18.a"], 1490, 400, 200)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    k = {x: C["s19." + x] for x in "abcd"}
    p = {x: C["s20." + x] for x in "abc"}
    E.frase(c, t, C["s19"] + 0.1, [("vamos", "i", 80), ("lá", "i", 80, COR)], W / 2, 150, "center")

    def f19():
        E.foco(c, t, k["a"], 0.45, lambda a: E.pilula(c, "vezes", 310, 300, 72, estilo="b", cor=E.SOBRE, a=a))
        E.frase(c, t, k["a"] + 0.8, [("mas", "i", 80), ("o", "i", 80), ("total", "g", 72, COR), ("já", "i", 80), ("está", "i", 80), ("dado:", "i", 80), ("os", "i", 80), ("anos", "i", 80), ("do", "i", 80), ("Caio", "g", 72)], 500, 322, passo=0.18)
        E.frase(c, t, k["b"], [("quem", "i", 84), ("tem", "i", 84), ("mais", "i", 84), ("anos", "i", 84), ("é", "i", 84), ("ele", "g", 76, COR)], XE, 470, passo=0.18)
    E.saida(c, t, C["s20"] - 0.1, f19)
    x, w, y, h = 300, 1320, 590, 130
    E.foco(c, t, k["c"], 0.5, lambda a: E.barra_fatias(c, x, y, w, h, 3, 3, E.COR, a, ep(t, k["c"] + 0.3, 0.6)))
    E.foco(c, t, k["c"] - 0.1, 0.4, lambda a: E.centro(c, "45 anos do Caio", W / 2, y - 26, 64, "b", TINTA, a))
    for i in range(3):
        cx = x + (i + 0.5) * w / 3
        E.foco(c, t, p["b"] + i * 0.15, 0.4, lambda a, cx=cx: E.centro(c, "15", cx, y + h / 2 + 30, 84, "g", E.SOBRE, a))
    E.foco(c, t, lerp(k["c"], k["d"], 0.5), 0.45, lambda a: E.escreve(c, "cada parte é a idade dela", x, y + h + 70, 62, "i", TINTA, a))
    if t < C["s20"]:
        sim(c, t, k["d"], "÷", 900, 870, 66)
        E.frase(c, t, k["d"] + 0.2, [("repartir", "i", 76), ("é", "i", 76), ("divisão", "g", 72, COR)], x, 900, passo=0.2)
    if t >= C["s20"]:
        igual(c, t, p["a"], lerp(p["a"], p["b"], 0.75), "45 ÷ 3 =", "15", XE + 130, 340, 120, "g")
        bola_txt(c, t, p["b"], "15 anos", 1490, 300, 140, 62)
        igual(c, t, p["c"], lerp(p["c"], C["s20.end"], 0.55), "3 × 15 =", "45", x, 890, 96, "g")
        E.foco(c, t, lerp(p["c"], C["s20.end"], 0.8), 0.5, lambda a: E.selo(c, 1040, 860, 66, True, a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s21"], [("resumindo", "i", 92, COR)], W / 2, 190, "center")
        E.frase(c, t, C["s21.a"], [("a", "i", 120), ("palavra", "i", 120), ("é", "i", 120), ("pista", "g", 112, COR)], W / 2, 370, "center", passo=0.16)
        E.frase(c, t, C["s21.b"], [("a", "i", 120), ("história", "g", 112, COR), ("decide", "i", 120)], W / 2, 510, "center", passo=0.16)
        ka = C["s21.c"]
        E.frase(c, t, ka, [("do", "i", 76), ("que", "i", 76), ("eu", "i", 76), ("sei", "g", 68), ("até", "i", 76), ("o", "i", 76), ("que", "i", 76), ("o", "i", 76), ("problema", "i", 76), ("pede,", "g", 68)], W / 2, 700, "center", passo=0.24)
        E.frase(c, t, lerp(ka, C["s21.end"], 0.55), [("o", "i", 84), ("que", "i", 84), ("acontece", "i", 84), ("com", "i", 84), ("a", "i", 84), ("quantidade?", "g", 80, COR)], W / 2, 820, "center", passo=0.24)
    E.saida(c, t, C["s22"] - 0.1, resumo)
    if t < C["s22"]:
        return
    E.frase(c, t, C["s22"] + 0.1, [("próxima", "i", 84), ("aula", "i", 84)], XE, 280)
    E.frase(c, t, C["s22.a"], [("só", "i", 150), ("prática", "g", 150, COR)], XE, 430, passo=0.2)
    E.frase(c, t, C["s22.b"], [("problemas", "g", 76), ("do", "i", 84), ("dia", "i", 84), ("a", "i", 84), ("dia", "i", 84)], XE, 560, passo=0.18)
    E.frase(c, t, C["s22.b"] + 1.3, [("com", "i", 84), ("as", "i", 84), ("quatro", "g", 76, COR), ("contas", "g", 76, COR)], XE, 660, passo=0.16)
    E.frase(c, t, C["s22.c"], [("números", "i", 76), ("grandes", "g", 68), ("e", "i", 76), ("atalhos", "g", 68)], XE, 760, passo=0.16)
    E.foco(c, t, C["s22.d"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1440, 790, 76, estilo="g", a=a, cor=E.SOBRE))
    p = ease_io(prog(t, C["s22.d"] + 0.3, 0.8))
    E.cursor(c, lerp(1770, 1570, p), lerp(1000, 815, p), ep(t, C["s22.d"] + 0.2, 0.4))
    E.frase(c, t, C["s22.e"], [("bons", "i", 120), ("estudos!", "i", 120, COR)], XE, 900)


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, pergunta=b_pergunta, quatro=b_quatro, pista=b_pista, erro=b_erro, passos=b_passos,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
