"""Visual — Estudativo · MAT-FRA-015: somar e subtrair decimais.
Identidade em _ferramentas/editorial.py. Toda conta armada passa por E.armada, que refaz a conta e para se o número estiver errado."""
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco
import motor as M
import skia

E.usar("Matemática", "Frações e Decimais")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-FRA-015_somar_subtrair_decimais.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("alinhar", "subtrair", "negativo", "atalho", "questao", "fim"))
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


def bola_txt(c, t, t0, s, cx, cy, r, size, cor=CERTO):
    """o resultado na esfera"""
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r, cor, a), E.centro(c, s, cx, cy + size * 0.35, size, "g", M.on(cor), a)))


def nota(c, x, y, w, h, s, a):
    """cédula na cor da matéria (peça local)"""
    if a <= 0:
        return
    M.rrect(c, x, y, w, h, 22, E.COR, a)
    r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x + 18, y + 18, w - 36, h - 36), 12, 12)
    c.drawRRect(r, M.paint(E.SOBRE, 0.55 * a, stroke=4))
    for px, py in ((x + 70, y + 70), (x + w - 70, y + h - 70)):
        c.drawCircle(px, py, 26, M.paint(E.SOBRE, 0.25 * a))
    E.centro(c, s, x + w / 2, y + h / 2 + 46, 130, "g", E.SOBRE, a)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def conta():
        y, s = 430, 150
        num(c, t, C["s01.a"], "2,35", 430, y, s)
        E.sinal(c, t, C["s01.b"] - 0.1, "+", 750, y - 55, 120)
        num(c, t, C["s01.b"], "1,4", 960, y, s)
        E.sinal(c, t, C["s01.c"] - 0.1, "=", 1170, y - 55, 120)
        num(c, t, C["s01.c"], "2,49", 1400, y, s, ERRADO)
        if t >= C["s02.b"]:
            E.risco(c, 1250, y + 20, 1640, y - 130, t, C["s02.b"], largura=16)
        E.saida(c, t, C["s02"] - 0.1, lambda: E.frase(c, t, lerp(C["s01.c"], C["s01.end"], 0.45), [("a", "i", 96), ("vírgula", "g", 86, ERRADO), ("te", "i", 96), ("enganou", "i", 96)], W / 2, 720, "center"))
        E.frase(c, t, C["s02.a"], [("2", "g", 110, COR), ("+", "g", 96), ("1", "g", 110, COR), ("=", "g", 96), ("3", "g", 110, COR)], W / 2, 690, "center", passo=0.12)
        E.frase(c, t, C["s02.b"], [("o", "i", 86), ("resultado", "i", 86), ("não", "g", 76, ERRADO), ("pode", "g", 76, ERRADO), ("ser", "i", 86), ("menor", "i", 86)], W / 2, 870, "center", passo=0.12)
    E.saida(c, t, C["s03"] - 0.1, conta)
    if t >= C["s03"]:
        ta, tb = C["s03.a"], C["s03.b"]
        E.foco(c, t, tb - 0.2, 0.7, lambda a: E.bola(c, 1490, 520, 280 * ease_back(prog(t, tb - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, [("até", "i", 90), ("o", "i", 90), ("fim", "i", 90), ("desta", "i", 90), ("aula", "i", 90)], XE, 340)
        E.frase(c, t, lerp(ta, tb, 0.33), [("somar", "g", 128), ("e", "i", 116), ("subtrair", "g", 128)], XE, 490)
        E.frase(c, t, lerp(ta, tb, 0.48), [("decimais", "g", 128)], XE, 630)
        E.frase(c, t, lerp(ta, tb, 0.52), [("sem", "i", 100), ("tropeçar", "i", 100)], XE, 740)
        E.frase(c, t, lerp(ta, tb, 0.62), [("até", "i", 84), ("com", "i", 84), ("número", "i", 84), ("negativo", "i", 84, COR)], XE, 850)
        E.foco(c, t, tb + 0.2, 0.5, lambda a: (E.centro(c, "+ atalho", 1490, 505, 84, "g", E.SOBRE, a),
                                               E.centro(c, "do troco", 1490, 590, 84, "i", E.SOBRE, a)))


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
    lista(c, t, C, "s04", "s04.a", 3, (("s04.b", "ler décimos", "e centésimos"), ("s04.c", "subtrair", "pedindo emprestado"), ("s04.d", "somar inteiros:", "dívida e pagamento")))


# ---------------- alinhar ----------------
def b_alinhar(c, t, C, b):
    xv, y0, size = 500, 380, 150
    tb_, tc_, td_ = C["s05.b"], C["s05.c"], C["s05.d"]
    A = E.armada(c, t, ["2,35", "1,4"], "+", "3,75", (C["s05.a"], C["s05.a"] + 0.4), (C["s07.a"], C["s07.b"], C["s07.d"]), xv, y0, size, tz=C["s06.a"])
    dy = size * 1.22
    E.frase(c, t, C["s05.a"], [("vírgula", "g", 88, COR), ("embaixo", "i", 96), ("de", "i", 96), ("vírgula", "g", 88, COR)], W / 2, 170, "center")
    cen = A["centros"][0]

    def coluna():
        q = ep(t, C["s05.a"] + 0.5, 0.4)
        cx = xv
        for ti, alvo in ((tb_, cen[0]), (tc_, cen[2]), (td_, cen[3])):
            cx = lerp(cx, alvo, ease_io(prog(t, ti - 0.15, 0.4)))
        E.caixa_pontilhada(c, cx - 70, y0 - 135, 140, dy + 190, q, prog_=q)
        for y, ti, partes in ((340, tb_, [("inteiro", "g", 66, COR), ("com", "i", 74), ("inteiro", "g", 66, COR)]),
                              (460, tc_, [("décimo", "g", 66, COR), ("com", "i", 74), ("décimo", "g", 66, COR)]),
                              (580, td_, [("centésimo", "g", 66, COR), ("com", "i", 74), ("centésimo", "g", 66, COR)])):
            E.frase(c, t, ti, partes, 960, y, passo=0.13)
    E.saida(c, t, C["s06"] - 0.1, coluna)

    def completa():
        E.frase(c, t, C["s06.a"], [("complete", "i", 80), ("com", "i", 80), ("zero", "g", 72, COR)], 960, 340)
        E.frase(c, t, C["s06.a"] + 0.6, [("1,4", "g", 96), ("=", "g", 84), ("1,40", "g", 96, COR)], 960, 480)
        E.frase(c, t, lerp(C["s06.a"], C["s06.end"], 0.4), [("o", "i", 76), ("valor", "i", 76), ("não", "g", 68, COR), ("muda", "g", 68, COR)], 960, 610)
    if C["s06"] - 0.1 <= t:
        E.saida(c, t, C["s07"] - 0.1, completa)
    if t >= C["s07"]:
        E.foco(c, t, C["s07.a"], 0.4, lambda a: E.escreve(c, "5 + 0 = 5", 960, 330, 76, "b", TINTA, a))
        E.foco(c, t, C["s07.b"], 0.4, lambda a: E.escreve(c, "3 + 4 = 7", 960, 450, 76, "b", TINTA, a))
        E.frase(c, t, C["s07.c"], [("a", "i", 76), ("vírgula", "g", 68, COR), ("desce", "i", 76), ("reta", "i", 76)], 960, 570, passo=0.1)
        E.foco(c, t, C["s07.d"], 0.4, lambda a: E.escreve(c, "2 + 1 = 3", 960, 690, 76, "b", TINTA, a))
        bola_txt(c, t, C["s07.e"], "3,75", 1560, 800, 140, 96)
        if t >= C["s07.c"]:  # a vírgula desce da linha de cima, reta, até o resultado
            E._virgula(c, xv, lerp(y0 + dy, A["y_res"], ease_io(prog(t, C["s07.c"], 0.6))), size, COR, 1.0)


# ---------------- subtrair ----------------
def b_subtrair(c, t, C, b):
    def compra():
        E.frase(c, t, C["s08.a"] - 0.5, [("você", "i", 84), ("paga", "i", 84)], 230, 330)
        E.foco(c, t, C["s08.a"], 0.5, lambda a: E.escreve(c, "R$", 230, 530, 100, "b", TINTA2, a))
        num(c, t, C["s08.a"], "3,25", 590, 530, 180, COR)
        E.foco(c, t, C["s08.b"], 0.5, lambda a: nota(c, 1080, 240, 620, 320, "R$ 10", a))
        E.frase(c, t, C["s08.c"], [("qual", "i", 130), ("é", "i", 130), ("o", "i", 130), ("troco?", "g", 120, COR)], W / 2, 830, "center")
    E.saida(c, t, C["s09"] - 0.1, compra)

    if C["s09"] - 0.1 <= t < C["s12"] + 0.4:
        def conta():
            xv, y0, size = 620, 450, 150
            ti, tv = C["s10.b"], C["s10.c"]
            A = E.armada(c, t, ["10", "3,25"], "−", "6,75", (C["s09.a"], C["s09.c"]), (C["s11.a"], C["s11.b"], C["s11.c"]), xv, y0, size,
                         tz=C["s09.b"], tl=C["s09.c"] + 0.2, marcas=[(0, 0, None, ti), (0, 1, 9, ti), (0, 3, 9, tv), (0, 4, 10, C["s10.d"])])
            xp = 1040

            def fala9():
                E.frase(c, t, C["s09.a"], [("uma", "i", 82), ("vírgula", "g", 74, COR), ("escondida", "i", 82), ("no", "i", 82), ("fim", "i", 82)], W / 2, 170, "center", passo=0.12)
                E.frase(c, t, C["s09.b"], [("10", "g", 104), ("=", "g", 92), ("10,00", "g", 104, COR)], xp, 460)
                E.frase(c, t, C["s09.c"], [("vírgula", "g", 62, COR), ("embaixo", "i", 70), ("de", "i", 70), ("vírgula", "g", 62, COR)], xp, 620, passo=0.1)
            E.saida(c, t, C["s10"] - 0.1, fala9)

            def fala10():
                E.frase(c, t, C["s10"] + 0.1, [("zero", "i", 72), ("menos", "i", 72), ("cinco", "i", 72), ("não", "g", 64, ERRADO), ("dá", "g", 64, ERRADO)], xp, 300, passo=0.1)
                E.frase(c, t, C["s10.a"], [("o", "i", 72), ("empréstimo", "i", 72), ("vem", "i", 72), ("lá", "i", 72), ("do", "i", 72), ("10", "g", 64, COR)], xp, 400, passo=0.1)
                E.foco(c, t, ti, 0.4, lambda a: E.escreve(c, "9 reais", xp, 560, 72, "g", CERTO, a))
                E.foco(c, t, tv, 0.4, lambda a: E.escreve(c, "9 moedas de 10 centavos", xp, 680, 66, "b", CERTO, a))
                E.foco(c, t, C["s10.d"], 0.4, lambda a: E.escreve(c, "10 moedas de 1 centavo", xp, 800, 66, "b", CERTO, a))
            if C["s10"] - 0.1 <= t:
                E.saida(c, t, C["s11"] - 0.1, fala10)
            if t >= C["s11"]:
                for y, k, s in ((340, "s11.a", "10 − 5 = 5"), (460, "s11.b", "9 − 2 = 7"), (580, "s11.c", "9 − 3 = 6")):
                    E.foco(c, t, C[k], 0.4, lambda a, s=s, y=y: E.escreve(c, s, xp + 40, y, 76, "b", TINTA, a))
                bola_txt(c, t, C["s11.d"], "R$ 6,75", 1540, 800, 170, 76)
                E.foco(c, t, C["s11.d"] + 0.2, 0.4, lambda a: E.escreve(c, "o troco", 1080, 825, 80, "i", TINTA, a))
        E.saida(c, t, C["s12"] - 0.1, conta)

    if t >= C["s12"]:
        ta, tb = C["s12.a"], C["s12.b"]
        E.frase(c, t, C["s12"] + 0.1, [("confira", "i", 92), ("com", "i", 92), ("uma", "i", 92), ("soma", "g", 84, COR)], W / 2, 170, "center")
        E.armada(c, t, ["6,75", "3,25"], "+", "10,00", (ta, lerp(ta, tb, 0.5)), (tb, tb + 0.1, tb + 0.2, tb + 0.3), 820, 390, 150)
        E.foco(c, t, lerp(tb, C["s12.end"], 0.45), 0.5, lambda a: E.selo(c, 1480, 590, 110, True, a))


# ---------------- negativo ----------------
def b_negativo(c, t, C, b):
    def ideia():
        E.frase(c, t, C["s13.a"], [("−2,5", "g", 150, COR), ("+", "g", 120), ("1,2", "g", 150)], W / 2, 330, "center", passo=0.3)
        E.frase(c, t, C["s13.b"], [("−2,5:", "g", 80, COR), ("uma", "i", 88), ("dívida", "g", 80, COR), ("de", "i", 88), ("R$ 2,50", "g", 80)], W / 2, 580, "center", passo=0.13)
        E.frase(c, t, C["s13.c"], [("+1,2:", "g", 80), ("um", "i", 88), ("pagamento", "g", 80), ("de", "i", 88), ("R$ 1,20", "g", 80)], W / 2, 740, "center", passo=0.13)
    E.saida(c, t, C["s14"] - 0.1, ideia)
    if t < C["s14"]:
        return
    y = 400
    vx = E.reta(c, t, C["s14"] + 0.1, 280, 1600, y, -3, 0, (-3, -2, -1, 0), fmt=lambda v: str(v).replace("-", "−"), size=54)
    x0, x1 = vx(-2.5), vx(-1.3)
    ka, kb = C["s14.a"], C["s14.b"]
    k = ease_back(prog(t, ka, 0.5))
    if k > 0:
        E.bola(c, x0, y, 24 * k)
    E.foco(c, t, ka, 0.4, lambda a: E.centro(c, "−2,5", x0, y + 92, 64, "g", COR, a), sobe=6)
    E.salto(c, t, kb, x0, x1, y, 150, rotulo="+1,2", size=64)
    k2 = ease_back(prog(t, kb + 0.7, 0.5))
    if k2 > 0:
        E.bola(c, x1, y, 24 * k2, TINTA)
    E.foco(c, t, C["s15.c"], 0.4, lambda a: E.centro(c, "−1,3", x1 + 110, y - 40, 64, "g", CERTO, a), sobe=6)
    E.frase(c, t, C["s14.c"], [("a", "i", 84), ("dívida", "g", 76, COR), ("é", "i", 84), ("maior:", "i", 84), ("você", "i", 84), ("ainda", "i", 84), ("deve", "g", 76, COR)], W / 2, 660, "center", passo=0.12)
    E.frase(c, t, C["s15.a"], [("2,5", "g", 110), ("−", "g", 96), ("1,2", "g", 110)], 640, 880, "center", passo=0.2)
    E.frase(c, t, C["s15.b"], [("=", "g", 96), ("1,3", "g", 110, COR)], 1000, 880, "center")
    bola_txt(c, t, C["s15.c"], "−1,3", 1420, 845, 130, 90)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s16"] + 0.1, [("de", "i", 86), ("onde", "i", 86), ("veio", "i", 86), ("2,49?", "g", 78, ERRADO)], W / 2, 170, "center")
    size, xv, y1, y2 = 170, 460, 400, 590
    cl = E.larg("0", "g", size) * 1.1
    ka, kb, kc, kd = C["s16.a"], C["s16.b"], C["s16.c"], C["s16.d"]
    xs1 = E._centros("2,35", xv, size)
    num(c, t, ka, "2,35", xv, y1, size, None, {3: E.mix(TINTA, ERRADO, ep(t, kb, 0.4))})
    num(c, t, ka + 0.3, "1,4", xv + cl, y2, size, None, {2: E.mix(TINTA, ERRADO, ep(t, kb, 0.4))})
    if t >= kb:
        q = ep(t, kb, 0.4)
        E.caixa_pontilhada(c, xs1[3] - 80, y1 - 150, 160, 380, q, ERRADO, prog_=q)
    E.frase(c, t, ka, [("alinhou", "i", 80), ("pela", "i", 80), ("direita", "g", 72, ERRADO)], 960, 340)
    E.frase(c, t, kc, [("décimo", "g", 72, ERRADO), ("somado", "i", 80)], 960, 490)
    E.frase(c, t, kc + 0.4, [("com", "i", 80), ("centésimo", "g", 72, ERRADO)], 960, 590)
    y = 840
    E.foco(c, t, kd, 0.5, lambda a: (E.moeda(c, 310, y, 92, "10¢", a=a), E.centro(c, "=", 500, y + 40, 110, "g", TINTA, a), E.moeda(c, 690, y, 92, "1¢", a=a)))
    if t >= kd + 0.8:
        E.risco(c, 445, y + 60, 555, y - 60, t, kd + 0.8, largura=12)
    E.frase(c, t, kd + 0.5, [("como", "i", 80), ("se", "i", 80), ("valessem", "i", 80), ("o", "i", 80), ("mesmo", "g", 72, ERRADO)], 850, y + 28, passo=0.13)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def troco():
        E.frase(c, t, C["s17"] + 0.1, [("agora,", "i", 72, CLARO), ("o", "i", 72, CLARO), ("atalho:", "i", 72, CLARO)], W / 2, 150, "center", passo=0.1)
        E.frase(c, t, C["s17.a"], [("o", "i", 96, BR), ("troco", "g", 88, BR), ("do", "i", 96, BR), ("caixa", "g", 88, BR)], W / 2, 260, "center", passo=0.1)
        E.frase(c, t, C["s17.b"], [("suba", "g", 66, CLARO), ("do", "i", 72, CLARO), ("preço", "i", 72, CLARO), ("até", "i", 72, CLARO), ("a", "i", 72, CLARO), ("nota", "i", 72, CLARO)], W / 2, 365, "center", passo=0.1)
        y = 660
        xs = (260, 680, 1040, 1660)
        p = ep(t, C["s17.b"], 1.2)
        if t >= C["s17.b"]:
            M.line(c, xs[0], y, xs[3], y, CLARO, 0.6, 4, progress=p)
        for x, s, k in zip(xs, ("3,25", "3,50", "4", "10"), ("s17.b", "s17.c", "s17.d", "s17.e")):
            E.foco(c, t, C[k], 0.4, lambda a, x=x, s=s: (M.line(c, x, y - 22, x, y + 22, BR, a, 6), E.centro(c, s, x, y + 96, 76, "g", BR, a)), sobe=6)
        for i, (r, k) in enumerate((("25¢", "s17.c"), ("50¢", "s17.d"), ("R$ 6", "s17.e"))):
            E.salto(c, t, C[k] - 0.1, xs[i], xs[i + 1], y, 130, CLARO, r, size=70)
        E.frase(c, t, C["s17.f"], [("25¢", "b", 76, BR), ("+", "b", 76, BR), ("50¢", "b", 76, BR), ("+", "b", 76, BR), ("R$ 6", "b", 76, BR), ("=", "b", 76, BR), ("R$ 6,75", "g", 100, CLARO)], W / 2, 930, "center", passo=0.08)
    E.saida(c, t, C["s18"] - 0.1, troco)
    if t < C["s18"]:
        return
    E.frase(c, t, C["s18.a"], [("subtrair", "i", 100, CLARO), ("é", "i", 100, CLARO), ("medir", "g", 92, BR), ("a", "g", 92, BR), ("distância", "g", 92, BR)], W / 2, 250, "center", passo=0.12)
    y, x0, x1 = 520, 420, 1500
    p = ep(t, C["s18.a"] + 0.6, 0.7)
    M.arrow(c, (x0 + x1) / 2, y, lerp((x0 + x1) / 2, x0, p), y, CLARO, p, 6, 20, p)
    M.arrow(c, (x0 + x1) / 2, y, lerp((x0 + x1) / 2, x1, p), y, CLARO, p, 6, 20, p)
    E.foco(c, t, C["s18.a"] + 0.6, 0.5, lambda a: (E.centro(c, "3,25", x0 - 130, y + 30, 84, "g", BR, a), E.centro(c, "10", x1 + 100, y + 30, 84, "g", BR, a)))
    E.foco(c, t, C["s18.b"], 0.5, lambda a: E.selo(c, 300, 790, 72, False, a))
    E.frase(c, t, C["s18.b"] + 0.1, [("não", "i", 84, CLARO), ("compensa", "i", 84, CLARO), ("com", "i", 84, CLARO), ("muitas", "g", 76, BR), ("casas", "g", 76, BR)], 410, 815, passo=0.12)
    E.frase(c, t, C["s18.b"] + 1.6, [("aí,", "i", 84, CLARO), ("arme", "g", 76, BR), ("a", "g", 76, BR), ("conta", "g", 76, BR)], 410, 925, passo=0.12)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s19"], [("hora", "i", 72, COR), ("de", "i", 72, COR), ("testar", "i", 72, COR)], XE, 200)
    E.frase(c, t, C["s19.a"], [("seu", "i", 92), ("saldo:", "i", 92), ("−7,4", "g", 104, COR), ("reais", "i", 92)], XE, 400, passo=0.12)
    E.frase(c, t, C["s19.b"], [("deposita", "i", 92), ("5", "g", 104), ("reais", "i", 92)], XE, 590, passo=0.12)
    E.frase(c, t, C["s19.c"], [("qual", "i", 110), ("é", "i", 110), ("o", "i", 110), ("novo", "g", 100, COR), ("saldo?", "g", 100, COR)], XE, 830)
    E.relogio(c, t, C["s20.a"], 1490, 400, 200)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    E.frase(c, t, C["s21.a"], [("−7,4", "g", 110, COR), ("+", "g", 96), ("5", "g", 110)], 520, 200, "center", passo=0.25)
    E.foco(c, t, C["s21.b"], 0.5, lambda a: E.pilula(c, "você ainda deve", 1250, 170, 70, a=a, cor=E.SOBRE))
    tc, fim = C["s21.c"], C["s21.end"]
    xv, y0, size = 520, 430, 150
    E.armada(c, t, ["7,4", "5"], "−", "2,4", (tc, lerp(tc, fim, 0.42)), (C["s22.a"], C["s22.b"]), xv, y0, size, tz=lerp(tc, fim, 0.62), tl=lerp(tc, fim, 0.42) + 0.2)
    xp = 980
    E.foco(c, t, C["s22.a"], 0.4, lambda a: E.escreve(c, "4 − 0 = 4", xp, 400, 76, "b", TINTA, a))
    E.foco(c, t, C["s22.b"], 0.4, lambda a: E.escreve(c, "7 − 5 = 2", xp, 520, 76, "b", TINTA, a))
    E.frase(c, t, C["s22.c"], [("2,4", "g", 76, COR), ("e", "i", 84), ("ainda", "i", 84), ("é", "i", 84), ("dívida", "g", 76, COR)], xp, 660, passo=0.1)
    bola_txt(c, t, C["s22.d"], "−2,4", 1170, 860, 140, 96)
    E.frase(c, t, C["s22.d"] + 0.3, [("reais", "i", 100)], 1340, 890)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s23"], [("resumindo", "i", 92, COR)], W / 2, 210, "center")
        for i, (k, s) in enumerate((("s23.a", "vírgula embaixo de vírgula"), ("s23.b", "zero para completar as casas"), ("s23.c", "o sinal de quem for maior"))):
            y = 390 + i * 190
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 300, y - 30, 56, a=a),
                                                         E.centro(c, str(i + 1), 300, y - 7, 64, "g", E.SOBRE, a)))
            E.frase(c, t, C[k] + 0.1, [(s, "g", 84)], 400, y)
    E.saida(c, t, C["s24"] - 0.1, resumo)
    if t < C["s24"]:
        return
    E.frase(c, t, C["s24"] + 0.1, [("próxima", "i", 84), ("aula", "i", 84)], XE, 270)
    E.frase(c, t, C["s24.a"], [("a", "i", 130), ("vírgula", "g", 130, COR), ("sai", "i", 130), ("andando", "g", 130, COR)], XE, 420, passo=0.12)
    E.frase(c, t, C["s24.b"], [("multiplica", "i", 80), ("por", "i", 80), ("100", "g", 76), ("e", "i", 80), ("divide", "i", 80), ("por", "i", 80), ("1.000", "g", 76)], XE, 560, passo=0.1)
    E.frase(c, t, C["s24.c"], [("decimal", "g", 84, COR), ("×", "g", 84), ("decimal", "g", 84, COR)], XE, 690, passo=0.15)
    E.foco(c, t, C["s24.d"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1440, 700, 76, estilo="g", a=a, cor=E.SOBRE))
    p = ease_io(prog(t, C["s24.d"] + 0.3, 0.8))
    E.cursor(c, lerp(1770, 1570, p), lerp(960, 725, p), ep(t, C["s24.d"] + 0.2, 0.4))
    E.frase(c, t, C["s24.e"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 900, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, alinhar=b_alinhar, subtrair=b_subtrair, negativo=b_negativo, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
