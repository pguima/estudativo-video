"""Visual — Estudativo · MAT-NUM-001: algarismos e valor posicional. A primeira aula do curso.
Identidade em _ferramentas/editorial.py. Dinheiro de verdade dá o valor de cada casa: moeda = unidade, nota de 10 = dezena,
nota de 100 = centena. As notas são retângulos simples da aula, não cópia de cédula."""
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco
import motor as M
import skia

E.usar("Matemática", "Números e Contas")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-NUM-001_algarismos_valor_posicional.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("algarismos", "casas", "lugar", "atalho", "questao", "fim"))
BR = "#FFFFFF"
CASAS = ("centena", "dezena", "unidade")
XC = (480, 960, 1440)  # o centro de cada casa, na tela cheia


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


def entre(a, b, f):
    """instante proporcional entre dois cues: sobrevive à troca do tempo provisório pela voz real"""
    return a + (b - a) * f


# ---------------- peças locais ----------------
def nota(c, cx, cy, w, s, a=1.0, cor=None, giro=0.0, k=1.0):
    """nota de dinheiro didática: retângulo com o valor, sem imitar cédula real"""
    if a <= 0 or k <= 0:
        return
    cor = cor or E.COR
    h = w * 0.5
    c.save(); c.translate(cx, cy); c.rotate(giro); c.scale(k, k)
    sombra = skia.Paint(AntiAlias=True, Color=M.hexc("#000000", 0.22 * a))
    sombra.setMaskFilter(skia.MaskFilter.MakeBlur(skia.kNormal_BlurStyle, max(3, w * 0.03)))
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(-w / 2 + 3, -h / 2 + 7, w, h), w * 0.04, w * 0.04), sombra)
    M.rrect(c, -w / 2, -h / 2, w, h, w * 0.04, cor, a)
    m = w * 0.045
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(-w / 2 + m, -h / 2 + m, w - 2 * m, h - 2 * m), w * 0.025, w * 0.025), M.paint(E.SOBRE, 0.45 * a, stroke=max(2, w * 0.008)))
    size = h * 0.5
    E.centro(c, "R$ " + s, 0, size * 0.36, size, "g", E.SOBRE, a)
    c.restore()


def leque(c, cx, cy, n, w, s, q, a=1.0, cor=None):
    """n notas empilhadas que se abrem em leque: q = 0 parece uma só, q = 1 aberto"""
    for i in range(n):
        d = i - (n - 1) / 2
        nota(c, cx + d * w * 0.1 * q, cy + d * w * 0.14 * q, w, s, a, cor, d * 3.2 * q)


def caixa_boleto(c, x, y, w, h, numero, a=1.0, xu=None, size=130):
    """boleto: papel branco, código de barras e o valor. O 3 ou o 4 da vez vem colorido pelo chamador"""
    if a <= 0:
        return
    sombra = skia.Paint(AntiAlias=True, Color=M.hexc("#000000", 0.14 * a))
    sombra.setMaskFilter(skia.MaskFilter.MakeBlur(skia.kNormal_BlurStyle, 14))
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x + 4, y + 10, w, h), 16, 16), sombra)
    M.rrect(c, x, y, w, h, 16, E.VAZIO, a)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 16, 16), M.paint(TINTA, a, stroke=3))
    E.escreve(c, "boleto", x + 40, y + h * 0.42, 60, "i", TINTA2, a)
    bx = x + 40
    larguras = (6, 3, 3, 8, 3, 5, 3, 3, 7, 3, 5, 8, 3, 3, 6, 3, 8, 3, 5, 3)
    for i, lw in enumerate(larguras):
        c.drawRect(skia.Rect.MakeXYWH(bx, y + h * 0.56, lw, h * 0.28), M.paint(TINTA, a))
        bx += lw + 5


def valor_casas(c, s, xu, y, size, a=1.0, cor3=None, destaque="3", sifrao=True):
    """valor em reais com os algarismos em colunas fixas: o 3 muda de coluna, e dá para ver. Devolve o x de cada algarismo"""
    cl = E.larg("0", "g", size) * 1.14
    xs = [xu - (len(s) - 1 - i) * cl for i in range(len(s))]
    for ch, x in zip(s, xs):
        E.centro(c, ch, x, y, size, "g", (cor3 or COR) if ch == destaque else TINTA, a)
    if sifrao:
        E.escreve(c, "R$", xs[0] - cl * 0.5 - E.larg("R$", "g", size * 0.6) - 18, y, size * 0.6, "g", TINTA2, a)
    return xs


def faixa(c, x, y, w, h, a):
    M.rrect(c, x, y, w, h, 18, E.COR, 0.08 * a)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    linhas = (("3", 96, C["s01.b"]), ("30", 306, C["s01.c"]), ("300", 516, C["s01.d"]))
    xu, x_c, w_c, h_c = 1420, 370, 1180, 180

    def boletos():
        # o três enorme vai para o primeiro boleto
        voa = ease_io(prog(t, C["s01.b"] - 0.1, 0.65))
        for s, y, ti in linhas:
            E.foco(c, t, ti - 0.1, 0.45, lambda a, y=y: caixa_boleto(c, x_c, y, w_c, h_c, s, a))
        if voa < 1:
            k = lerp(1.0, 130 / 560, voa)
            E.foco(c, t, C["s01.a"], 0.5, lambda a: (c.save(), c.translate(lerp(W / 2, xu, voa), lerp(740, 96 + 136, voa)), c.scale(k, k),
                                                     E.centro(c, "3", 0, 0, 560, "g", COR, a), c.restore()))
        for s, y, ti in linhas:
            if s == "3" and voa < 1:
                continue
            E.foco(c, t, ti, 0.45, lambda a, s=s, y=y: valor_casas(c, s, xu, y + 136, 130, a))
        # as três caixas mostram o 3 andando para a esquerda
        if t >= C["s01.e"]:
            p = ep(t, C["s01.e"], 0.5)
            cl = E.larg("0", "g", 130) * 1.14
            for i, (s, y, ti) in enumerate(linhas):
                x = xu - i * cl
                E.caixa_pontilhada(c, x - cl * 0.56, y + 26, cl * 1.12, 130, p, E.COR, prog_=p)
        E.frase(c, t, entre(C["s01.d"], C["s01.e"], 0.5), [("o", "i", 76), ("desenho", "i", 76), ("é", "i", 76), ("o", "i", 76), ("mesmo", "i", 76)], W / 2, 820, "center", passo=0.1)
        E.frase(c, t, C["s01.e"], [("o", "i", 118), ("que", "i", 118), ("muda", "i", 118), ("é", "i", 118), ("o", "i", 118), ("lugar", "g", 118, COR)], W / 2, 960, "center", passo=0.12)
    E.saida(c, t, C["s02"] - 0.1, boletos)

    if t >= C["s02"]:
        a_, b_ = C["s02.a"], C["s02.b"]
        E.foco(c, t, b_ - 0.2, 0.7, lambda a: E.bola(c, 1450, 520, 300 * ease_back(prog(t, b_ - 0.2, 0.7))), blur=0)
        E.frase(c, t, a_, [("até", "i", 92), ("o", "i", 92), ("fim", "i", 92), ("desta", "i", 92), ("aula", "i", 92)], XE, 330)
        E.frase(c, t, entre(a_, b_, 0.35), [("qualquer", "i", 92), ("número", "i", 92)], XE, 470)
        E.frase(c, t, entre(a_, b_, 0.6), [("quanto", "g", 124), ("vale", "g", 124)], XE, 620)
        E.frase(c, t, entre(a_, b_, 0.76), [("cada", "g", 124, COR), ("pedaço", "g", 124, COR)], XE, 760)
        E.foco(c, t, b_ + 0.2, 0.5, lambda a: (E.escreve(c, "+ atalho", 1270, 505, 88, "g", E.SOBRE, a),
                                               E.escreve(c, "de prova", 1300, 595, 88, "i", E.SOBRE, a)))


# ---------------- acolhida ----------------
def b_acolhida(c, t, C, b):
    a_, fim = C["s03.a"], C["s03.end"]
    E.frase(c, t, C["s03"] + 0.1, [("faz", "i", 88), ("anos", "i", 88), ("que", "i", 88), ("você", "i", 88), ("não", "i", 88), ("estuda?", "i", 88)], XE, 270, passo=0.12)
    E.frase(c, t, entre(C["s03"], a_, 0.6), [("está", "i", 110), ("no", "i", 110), ("lugar", "g", 110, COR), ("certo", "g", 110, COR)], XE, 420, passo=0.14)
    E.frase(c, t, a_, [("você", "i", 80), ("já", "g", 76, COR), ("usa", "i", 80), ("isso", "i", 80)], XE, 610)
    E.frase(c, t, a_ + 0.5, [("ao", "i", 80), ("conferir", "i", 80), ("um", "i", 80), ("troco", "g", 76)], XE, 710)
    # o troco na mão: uma nota e duas moedas caem na mesa
    q = ease_back(prog(t, a_ + 0.1, 0.6))
    if q > 0:
        nota(c, 1450, lerp(250, 340, q), 420, "10", E.clamp(q * 2), giro=-4 * (1 - q) - 3)
    for x, ti in ((1330, a_ + 0.5), (1540, a_ + 0.8)):
        q = ease_back(prog(t, ti, 0.55))
        if q > 0:
            E.moeda(c, x, lerp(490, 590, q), 92, "R$1", E.clamp(q * 2))
    E.frase(c, t, entre(a_, fim, 0.62), [("a", "i", 84), ("gente", "i", 84), ("só", "i", 84), ("vai", "i", 84), ("dar", "g", 80, COR), ("nome", "g", 80, COR),
                                         ("ao", "i", 84), ("que", "i", 84), ("você", "i", 84), ("já", "i", 84), ("faz", "i", 84)], W / 2, 900, "center", passo=0.13)


# ---------------- algarismos ----------------
def b_algarismos(c, t, C, b):
    def simbolos():
        a_, b_, c_ = C["s04.a"], C["s04.b"], C["s04.c"]
        E.frase(c, t, a_, [("dez", "g", 96, COR), ("símbolos", "i", 104)], W / 2, 190, "center")
        for i in range(10):
            x = 240 + i * 160
            ti = entre(a_, b_, 0.12 + i * 0.07)
            q = ease_back(prog(t, ti, 0.45))
            if q > 0:
                c.save(); c.translate(x, 420); c.scale(q, q)
                E.centro(c, str(i), 0, 0, 210, "g", COR if t >= b_ else TINTA, E.clamp(q * 1.5))
                c.restore()
        E.frase(c, t, b_, [("cada", "i", 84), ("um", "i", 84), ("é", "i", 84), ("um", "i", 84), ("algarismo", "g", 118, COR)], W / 2, 630, "center", passo=0.1)
        E.frase(c, t, c_, [("com", "i", 72), ("poucas", "i", 72), ("letras,", "i", 72), ("qualquer", "g", 64), ("palavra", "g", 64)], W / 2, 810, "center", passo=0.1)
        E.frase(c, t, entre(c_, C["s04.end"], 0.55), [("com", "i", 72), ("dez", "i", 72), ("algarismos,", "i", 72), ("qualquer", "g", 64, COR), ("número", "g", 64, COR)], W / 2, 930, "center", passo=0.1)
    E.saida(c, t, C["s05"] - 0.1, simbolos)
    if t < C["s05"]:
        return

    size = 400
    cl = E.larg("0", "g", size) * 1.1
    xv, y = W / 2 + 1.5 * cl + size * 0.17, 640
    cen = E._centros("352", xv, size)
    E.frase(c, t, C["s05.a"], [("um", "i", 104), ("número", "i", 104), ("só", "g", 100, COR)], W / 2, 210, "center")
    E.foco(c, t, C["s05.a"] + 0.2, 0.5, lambda a: E.numero(c, "352", xv, y, size, "g", TINTA, a))
    p = ep(t, C["s05.b"], 0.6)
    if p > 0:
        for i in range(3):
            x = cen[i] - cl / 2
            E.caixa_pontilhada(c, x + 6, y - 310, cl - 12, 340, ep(t, C["s05.b"] + i * 0.15, 0.4), E.COR, prog_=ep(t, C["s05.b"] + i * 0.15, 0.4))
    E.frase(c, t, C["s05.b"] + 0.2, [("três", "g", 80, COR), ("algarismos", "i", 88)], W / 2, 800, "center")
    E.frase(c, t, C["s05.c"], [("quanto", "i", 104), ("vale", "i", 104), ("cada", "g", 100, COR), ("um", "g", 100, COR), ("deles?", "g", 100, COR)], W / 2, 950, "center", passo=0.12)


# ---------------- as três casas ----------------
def b_casas(c, t, C, b):
    E.saida(c, t, C["s07"] - 0.1, lambda: E.frase(c, t, C["s06"] + 0.1, [("pagar", "i", 104), ("R$ 352", "g", 112, COR), ("em", "i", 104), ("dinheiro", "i", 104)], W / 2, 280, "center", passo=0.14))

    # a coluna da vez ganha uma faixa, que anda da direita para a esquerda
    q1, q2 = ease_io(prog(t, C["s08"], 0.6)), ease_io(prog(t, C["s09"], 0.6))
    if t >= C["s07"]:
        fx = lerp(lerp(XC[2], XC[1], q1), XC[0], q2)
        faixa(c, fx - 232, 100, 464, 910, ep(t, C["s07"], 0.5))

    cor = lambda k: COR if t >= C[k] else TINTA
    E.quadro_casas(c, t, CASAS, (C["s09.b"], C["s08.b"], C["s07.b"]),
                   [[("3", C["s07"] + 0.1, cor("s09.a")), ("5", C["s07"] + 0.1, cor("s08.a")), ("2", C["s07"] + 0.1, cor("s07.a"))]],
                   240, 190, 480, 130, h_lin=650, grossa=None)
    # "casa": o nome do lugar, na hora em que ele é dito
    ti = entre(C["s07"], C["s07.a"], 0.5)
    E.saida(c, t, C["s07.b"] - 0.1, lambda: E.foco(c, t, ti, 0.4, lambda a: (E.caixa_pontilhada(c, XC[2] - 140, 195, 280, 150, a, E.COR, prog_=a),
                                                                             E.pilula(c, "casa", XC[2] + 195, 270, 46, estilo="g", cor=E.SOBRE, a=a))))

    # o dinheiro de cada casa
    cy = 560
    qm = ease_io(prog(t, C["s07.a"], 0.5))
    q = ease_back(prog(t, C["s06.a"], 0.5))
    if q > 0:
        E.moeda(c, lerp(XC[2], XC[2] - 92, qm), cy, 84 * q, "R$1", E.clamp(q * 2))
    if qm > 0:
        k = ease_back(prog(t, C["s07.a"] + 0.1, 0.5))
        E.moeda(c, XC[2] + 92, cy, 84 * k, "R$1", E.clamp(k * 2))
    E.foco(c, t, C["s06.b"], 0.5, lambda a: leque(c, XC[1], cy, 5, 300, "10", ease_io(prog(t, C["s08.a"], 0.7)), a))
    E.foco(c, t, C["s06.c"], 0.5, lambda a: leque(c, XC[0], cy, 3, 300, "100", ease_io(prog(t, C["s09.a"], 0.7)), a, TINTA))

    rot = (("moedas de R$ 1", "s06.a", 2), ("notas de R$ 10", "s06.b", 1), ("notas de R$ 100", "s06.c", 0))
    for s, k, i in rot:
        E.foco(c, t, C[k] + 0.15, 0.45, lambda a, s=s, i=i: E.centro(c, s, XC[i], 800, 56, "i", TINTA2, a))
    for s, k, i in (("R$ 2", "s07.c", 2), ("R$ 50", "s08.c", 1), ("R$ 300", "s09.c", 0)):
        E.foco(c, t, C[k], 0.45, lambda a, s=s, i=i: E.centro(c, s, XC[i], 905, 100, "g", COR, a))
    for s, t0, i in (("de um em um", entre(C["s07.b"], C["s07.c"], 0.35), 2), ("grupo de dez", entre(C["s08.b"], C["s08.c"], 0.15), 1),
                     ("grupo de cem", entre(C["s09.b"], C["s09.c"], 0.15), 0)):
        E.foco(c, t, t0, 0.45, lambda a, s=s, i=i: E.pilula(c, s, XC[i], 975, 44, a=a, cor=E.SOBRE))


# ---------------- por que as casas são assim ----------------
def b_troca(c, t, C, b):
    def trocas():
        b_, c_, fim = C["s10.b"], C["s10.c"], C["s10.end"]
        E.frase(c, t, C["s10.a"], [("uma", "i", 88), ("troca", "g", 84, COR), ("que", "i", 88), ("você", "i", 88), ("já", "i", 88), ("conhece", "i", 88)], W / 2, 170, "center", passo=0.12)
        for i in range(10):
            ti = entre(b_, c_, 0.04 + i * 0.05)
            q = ease_back(prog(t, ti, 0.4))
            if q > 0:
                E.moeda(c, 330 + (i % 5) * 136, 320 + (i // 5) * 136, 62 * q, "1", E.clamp(q * 2))
        E.sinal(c, t, entre(b_, c_, 0.62), "=", 1130, 380, 120)
        E.foco(c, t, entre(b_, c_, 0.68), 0.5, lambda a: nota(c, 1450, 385, 460, "10", a))
        for i in range(10):
            ti = entre(c_, fim, 0.02 + i * 0.05)
            E.foco(c, t, ti, 0.35, lambda a, i=i: nota(c, 370 + i * 54, 790 + (i % 2) * 12, 300, "10", a), sobe=-14)
        E.sinal(c, t, entre(c_, fim, 0.62), "=", 1130, 790, 120)
        E.foco(c, t, entre(c_, fim, 0.68), 0.5, lambda a: nota(c, 1450, 795, 460, "100", a, TINTA))
    E.saida(c, t, C["s11"] - 0.1, trocas)
    if t < C["s11"]:
        return

    a_, b_ = C["s11.a"], C["s11.b"]
    E.frase(c, t, a_, [("nenhuma", "i", 92), ("casa", "i", 92), ("guarda", "i", 92), ("mais", "i", 92), ("que", "i", 92), ("nove", "g", 92, COR)], W / 2, 170, "center", passo=0.12)
    x0, wc, y = 560, 400, 300
    xd, xu = x0 + wc / 2, x0 + wc * 1.5
    E.quadro_casas(c, t, ("dezena", "unidade"), (C["s11"] + 0.1, C["s11"] + 0.1), [[("", 0), ("", 0)]], x0, y, wc, 120, h_lin=590, grossa=None)
    # as moedas chegam uma a uma; a décima não cabe
    fim_conta = entre(a_, b_, 0.5)
    pos = [(xu - 106 + (i % 3) * 106, 530 + (i // 3) * 104) for i in range(9)] + [(xu, 842)]
    une = ease_io(prog(t, b_, 0.55))
    n = 0
    for i, (x, yy) in enumerate(pos):
        ti = entre(a_, fim_conta, i / 9) if i < 9 else entre(a_, b_, 0.72)
        q = ease_back(prog(t, ti, 0.35))
        if t >= ti:
            n = i + 1
            if une < 1:
                E.moeda(c, lerp(x, xu, une), lerp(yy, 634, une), 47 * q * (1 - une * 0.6), "1", E.clamp(q * 2) * (1 - une))
    if t >= a_ and t < b_:
        s = str(n) if n else "0"
        E.foco(c, t, a_, 0.3, lambda a: E.centro(c, s, xu, 430, 120, "g", ERRADO if n >= 10 else TINTA, a))
    if t < b_:
        E.foco(c, t, a_, 0.3, lambda a: E.centro(c, "0", xd, 430, 120, "g", TINTA, a))
    else:
        E.foco(c, t, b_ + 0.2, 0.4, lambda a: E.centro(c, "0", xu, 430, 120, "g", TINTA, a))
        E.foco(c, t, b_ + 0.45, 0.4, lambda a: E.centro(c, "1", xd, 430, 120, "g", COR, a))
        # as dez moedas viram uma nota, e ela sobe para a casa da esquerda
        s = ease_io(prog(t, b_ + 0.25, 0.7))
        k = ease_back(prog(t, b_ + 0.05, 0.4))
        if k > 0:
            nota(c, lerp(xu, xd, s), lerp(634, 660, s) - 60 * M.math.sin(s * 3.14159), 290, "10", E.clamp(k * 2))
    E.frase(c, t, b_ + 0.3, [("sobe", "g", 84, COR), ("para", "i", 88), ("a", "i", 88), ("casa", "i", 88), ("da", "i", 88), ("esquerda", "i", 88)], W / 2, 985, "center", passo=0.12)


# ---------------- mesmo algarismo, outro lugar ----------------
def b_lugar(c, t, C, b):
    x0, wc, y, size, hl = 230, 260, 240, 130, 200
    xs = [x0 + (i + 0.5) * wc for i in range(3)]
    t0 = C["s12"] + 0.1
    q = ep(t, C["s12.b"], 0.5)
    if q > 0:
        faixa(c, xs[1] - 120, 150, 240, 2 * hl + 110, q)
    E.quadro_casas(c, t, CASAS, (t0, t0, t0),
                   [[("3", t0, COR), ("5", t0), ("2", t0)], [("2", C["s12.a"]), ("3", C["s12.a"], COR), ("5", C["s12.a"])]],
                   x0, y, wc, size, h_lin=hl, grossa=None)
    # o três muda de casa
    if t >= C["s12.b"]:
        p = ep(t, C["s12.b"], 0.5)
        M.arrow(c, xs[0] + 24, 395, xs[1] - 34, 470, E.COR, p, 6, 20, p)
    tx = 1140
    E.linha(c, t, [("vale", "i", 88, TINTA, C["s13.a"]), ("R$ 300", "g", 96, COR, C["s13.a"] + 0.15)], tx, 375)
    E.linha(c, t, [("vale", "i", 88, TINTA, C["s12.c"]), ("R$ 30", "g", 96, COR, C["s12.c"] + 0.15)], tx, 575)
    E.foco(c, t, C["s13.b"] - 0.1, 0.3, lambda a: M.rrect(c, tx - 26, 495, 460, 110, 16, E.COR, 0.1 * a))
    E.frase(c, t, C["s13.c"], [("mesmo", "i", 74), ("algarismo,", "g", 64), ("lugar", "i", 74), ("diferente,", "g", 64), ("valor", "i", 74), ("diferente", "g", 64, COR)], W / 2, 770, "center", passo=0.22)
    E.frase(c, t, C["s13.d"], [("valor", "g", 150, COR), ("posicional", "g", 150, COR)], W / 2, 950, "center", passo=0.2)


# ---------------- abrir o número ----------------
def b_abrir(c, t, C, b):
    y, s = 400, 158
    azul = lambda: COR if t >= C["s14.d"] else TINTA
    partes = [("352", "g", s, TINTA, C["s14"] + 0.2), ("=", "g", s, TINTA, entre(C["s14"], C["s14.a"], 0.8)), ("300", "g", s, COR, C["s14.a"]),
              ("+", "g", s, azul(), C["s14.b"]), ("50", "g", s, COR, C["s14.b"] + 0.1), ("+", "g", s, azul(), C["s14.c"]), ("2", "g", s, COR, C["s14.c"] + 0.1)]
    xs = E.linha(c, t, partes, W / 2, y, "center")
    cen = [x + E.larg(p[0], "g", s) / 2 for x, p in zip(xs, partes)]
    E.frase(c, t, C["s14.d"], [("o", "i", 80), ("sinal", "i", 80), ("de", "i", 80), ("mais", "g", 76, COR), ("quer", "i", 80), ("dizer", "i", 80), ("juntar", "g", 76)], W / 2, 170, "center", passo=0.12)
    # o nome do número, palavra embaixo de cada pedaço
    y2 = 640
    for s_, i, ti, cor in (("trezentos", 2, C["s14.e"] - 0.5, TINTA), ("e", 3, C["s14.e"], COR), ("cinquenta", 4, C["s14.e"] + 0.2, TINTA), ("e", 5, C["s14.f"], COR), ("dois", 6, C["s14.f"] + 0.2, TINTA)):
        if s_ == "e":
            E.foco(c, t, ti, 0.45, lambda a, s_=s_, i=i, cor=cor: E.centro(c, s_, cen[i], y2, 96, "g", cor, a))
            q = ep(t, ti + 0.1, 0.5)
            if q > 0:
                M.arrow(c, cen[i], y2 - 96, cen[i], y + 58, E.COR, q, 6, 20, q)
        else:
            E.foco(c, t, ti, 0.45, lambda a, s_=s_, i=i, cor=cor: E.centro(c, s_, cen[i], y2, 74, "i", cor, a))
    E.frase(c, t, C["s14.g"], [("esse", "i", 104), ("e", "g", 104, COR), ("é", "i", 104), ("um", "i", 104), ("mais", "g", 104, COR), ("escondido", "g", 104, COR)], W / 2, 880, "center", passo=0.14)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    def escrito():
        a_, b_, c_, d_ = C["s15.a"], C["s15.b"], C["s15.c"], C["s15.d"]
        E.frase(c, t, a_, [("escrever", "i", 104), ("como", "g", 96, ERRADO), ("se", "g", 96, ERRADO), ("fala", "g", 96, ERRADO)], W / 2, 180, "center")
        E.frase(c, t, entre(a_, b_, 0.45), [("ouviu", "i", 84), ("trezentos", "g", 72), ("e", "g", 72), ("dois?", "g", 72)], W / 2, 310, "center", passo=0.12)
        size = 280
        cl = E.larg("0", "g", size) * 1.1
        xv, y = W / 2 + 2 * cl + size * 0.17, 620
        cen = E._centros("3002", xv, size)
        E.foco(c, t, b_, 0.45, lambda a: [E.centro(c, ch, cen[i], y, size, "g", TINTA, a) for i, ch in enumerate("300")])
        E.foco(c, t, entre(b_, c_, 0.6), 0.45, lambda a: E.centro(c, "2", cen[3], y, size, "g", ERRADO, a))
        for i in range(4):
            q = ep(t, c_ + i * 0.13, 0.4)
            E.caixa_pontilhada(c, cen[i] - cl / 2 + 6, y - 225, cl - 12, 250, q, ERRADO, prog_=q)
        E.frase(c, t, c_ + 0.1, [("quatro", "g", 76, ERRADO), ("algarismos", "i", 84)], W / 2, 770, "center")
        E.frase(c, t, d_, [("outro", "i", 96), ("número:", "i", 96), ("três", "g", 96, ERRADO), ("mil", "g", 96, ERRADO), ("e", "g", 96, ERRADO), ("dois", "g", 96, ERRADO)], W / 2, 930, "center", passo=0.12)
    E.saida(c, t, C["s16"] - 0.1, escrito)
    if t < C["s16"]:
        return

    t0 = C["s16"] + 0.1
    E.quadro_casas(c, t, CASAS, (t0, t0, t0), [[("3", C["s16.a"]), ("0", C["s16.d"], COR), ("2", C["s16.c"])]], 240, 180, 480, 130, h_lin=520, grossa=None)
    cy = 530
    E.foco(c, t, C["s16.a"], 0.5, lambda a: leque(c, XC[0], cy, 3, 280, "100", 1, a, TINTA))
    E.foco(c, t, C["s16.a"] + 0.1, 0.45, lambda a: E.centro(c, "três centenas", XC[0], 745, 52, "i", TINTA2, a))
    E.foco(c, t, C["s16.b"], 0.45, lambda a: E.centro(c, "nenhuma dezena", XC[1], 745, 52, "i", TINTA2, a))
    q = ep(t, C["s16.b"], 0.5)
    E.caixa_pontilhada(c, XC[1] - 130, cy - 90, 260, 180, q, TINTA2, prog_=q)
    E.foco(c, t, C["s16.c"], 0.45, lambda a: E.centro(c, "duas unidades", XC[2], 745, 52, "i", TINTA2, a))
    for x, ti in ((XC[2] - 92, C["s16.c"]), (XC[2] + 92, C["s16.c"] + 0.15)):
        k = ease_back(prog(t, ti, 0.5))
        if k > 0:
            E.moeda(c, x, cy, 84 * k, "R$1", E.clamp(k * 2))
    E.frase(c, t, entre(C["s16.d"], C["s16.e"], 0.5), [("o", "i", 84), ("zero", "g", 80, COR), ("segura", "i", 84), ("o", "i", 84), ("lugar", "g", 80, COR)], W / 2, 860, "center", passo=0.12)
    E.frase(c, t, C["s16.e"], [("sem", "i", 80), ("ele,", "i", 80), ("302", "g", 84), ("vira", "i", 80), ("32", "g", 92, ERRADO)], W / 2, 975, "center", passo=0.12)


# ---------------- atalho ----------------
def casas_a_direita(c, t, x, y, s, n, tp, rot):
    """a chave embaixo das casas depois do algarismo, com a contagem. x = (início, fim)"""
    q = ep(t, tp, 0.5)
    E.chave(c, x[0], x[1], y, CLARO, q, h=26, largura=7)
    E.foco(c, t, tp + 0.15, 0.4, lambda a: E.centro(c, rot, (x[0] + x[1]) / 2, y + 88, 54, "i", CLARO, a))


def b_atalho(c, t, C, b):
    palco(c, t)

    def regra():
        a_, b_, c_, d_, e_, f_ = C["s17.a"], C["s17.b"], C["s17.c"], C["s17.d"], C["s17.e"], C["s17.f"]
        E.frase(c, t, a_, [("conte", "g", 84, BR), ("as", "g", 84, BR), ("casas", "g", 84, BR), ("à", "i", 92, CLARO), ("direita", "i", 92, CLARO)], W / 2, 150, "center", passo=0.12)
        E.frase(c, t, b_, [("o", "i", 66, CLARO), ("número", "i", 66, CLARO), ("de", "i", 66, CLARO), ("casas", "i", 66, CLARO), ("é", "i", 66, CLARO), ("o", "i", 66, CLARO), ("de", "i", 66, CLARO), ("zeros", "g", 62, BR)], W / 2, 250, "center", passo=0.08)
        s = 190
        cl = E.larg("0", "g", s) * 1.1
        xv, xr = 760, 1560
        for y, num, tn, tc, tv, casas, rot, val, cor in ((520, "352", C["s17"] + 0.3, c_, d_, 2, "duas casas", "300", {0: CLARO}), (850, "235", entre(d_, e_, 0.5), e_, f_, 1, "uma casa", "30", {1: CLARO})):
            E.foco(c, t, tn, 0.45, lambda a, num=num, y=y, cor=cor: E.numero(c, num, xv, y, s, "g", BR, a, cor))
            casas_a_direita(c, t, (xv - casas * cl + 12, xv - 12), y + 30, s, casas, tc, rot)
            p = ep(t, tv - 0.3, 0.4)
            if p > 0:
                M.arrow(c, 830, y - 60, 1020, y - 60, CLARO, p, 6, 20, p)
            E.foco(c, t, tv, 0.45, lambda a, val=val, y=y: (E.centro(c, "3", xr - (len(val) - 0.5) * cl, y, s, "g", CLARO, a)))
            E.foco(c, t, tv + 0.2, 0.45, lambda a, val=val, y=y: [E.centro(c, "0", xr - (k + 0.5) * cl, y, s, "g", BR, a) for k in range(len(val) - 1)])
    E.saida(c, t, C["s18"] - 0.1, regra)
    if t < C["s18"]:
        return

    y = 390
    itens = ((1490, "1", "de um em um", C["s18.a"]), (960, "10", "de dez em dez", C["s18.b"]), (430, "100", "de cem em cem", C["s18.c"]))
    for x, n, s, ti in itens:
        k = ease_back(prog(t, ti, 0.55))
        if k > 0:
            E.bola(c, x, y, 150 * k, a=E.clamp(k * 2))
            E.foco(c, t, ti + 0.15, 0.4, lambda a, x=x, n=n: E.centro(c, n, x, y + 42, 120, "g", E.SOBRE, a))
        E.foco(c, t, ti + 0.1, 0.45, lambda a, x=x, s=s: E.centro(c, s, x, y + 240, 66, "i", BR, a))
    tz = entre(C["s18.c"], C["s18.d"], 0.45)
    for x0, x1 in ((1320, 1130), (790, 600)):
        p = ep(t, tz, 0.5)
        if p > 0:
            M.arrow(c, x0, y, x1, y, CLARO, p, 6, 22, p)
    E.frase(c, t, tz, [("cada", "i", 76, CLARO), ("passo", "i", 76, CLARO), ("para", "i", 76, CLARO), ("a", "i", 76, CLARO), ("esquerda", "i", 76, CLARO), ("ganha", "i", 76, CLARO), ("um", "i", 76, CLARO), ("zero", "g", 72, BR)], W / 2, 150, "center", passo=0.08)
    E.frase(c, t, C["s18.d"], [("não", "g", 76, ERRADO), ("compensa", "g", 76, ERRADO), ("para", "i", 84, BR), ("o", "i", 84, BR), ("número", "i", 84, BR), ("inteiro:", "i", 84, BR), ("é", "i", 84, CLARO), ("só", "i", 84, CLARO), ("ler", "g", 76, BR)], W / 2, 880, "center", passo=0.1)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s19"], [("hora", "i", 72, COR), ("de", "i", 72, COR), ("testar", "i", 72, COR)], XE, 170)
    x, y, w, h = XE, 230, 960, 190
    E.foco(c, t, C["s19.a"], 0.5, lambda a: (caixa_boleto(c, x, y, w, h, "647", a), valor_casas(c, "647", x + w - 80, y + 140, 130, a, destaque="")))
    E.frase(c, t, C["s19.b"], [("quanto", "i", 100), ("vale", "i", 100), ("o", "i", 100), ("4?", "g", 110, COR)], XE, 610)
    E.frase(c, t, C["s19.c"], [("e", "i", 100), ("o", "i", 100), ("número", "g", 92, COR), ("aberto", "g", 92, COR)], XE, 770)
    E.frase(c, t, C["s19.c"] + 0.5, [("em", "i", 100), ("partes,", "i", 100), ("com", "i", 100), ("o", "i", 100), ("+", "g", 110, COR)], XE, 900)
    E.relogio(c, t, C["s20.a"], 1490, 400)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    x0, wc, y, size = 300, 300, 190, 150
    xs = [x0 + (i + 0.5) * wc for i in range(3)]
    t0 = C["s21"] + 0.1
    q = ep(t, C["s21.a"], 0.5)
    if q > 0:
        faixa(c, xs[1] - 140, 100, 280, 320, q)
    E.quadro_casas(c, t, CASAS, (t0, t0, t0), [[("6", t0), ("4", t0, COR if t >= C["s21.a"] else TINTA), ("7", t0)]], x0, y, wc, size, grossa=None)
    p = ep(t, C["s21.b"], 0.5)
    E.chave(c, xs[2] - 100, xs[2] + 100, 435, E.COR, p, h=22, largura=6)
    E.foco(c, t, C["s21.b"] + 0.15, 0.4, lambda a: E.centro(c, "uma casa", xs[2], 515, 56, "i", COR, a))
    k = ease_back(prog(t, C["s21.c"], 0.55))
    if k > 0:
        E.bola(c, 1500, 310, 170 * k, a=E.clamp(k * 2))
        E.foco(c, t, C["s21.c"] + 0.15, 0.4, lambda a: E.centro(c, "40", 1500, 370, 170, "g", E.SOBRE, a))
    s = 150
    E.linha(c, t, [("647", "g", s, TINTA, entre(C["s21.c"], C["s21.d"], 0.5)), ("=", "g", s, TINTA, entre(C["s21.c"], C["s21.d"], 0.8)), ("600", "g", s, TINTA, C["s21.d"]), ("+", "g", s, TINTA, C["s21.e"]),
                ("40", "g", s, COR, C["s21.e"] + 0.1), ("+", "g", s, TINTA, C["s21.f"]), ("7", "g", s, TINTA, C["s21.f"] + 0.1)], W / 2, 790, "center")


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        a_, f = C["s22.a"], C["s22.end"]
        E.frase(c, t, a_, [("quem", "i", 116), ("dá", "i", 116), ("o", "i", 116), ("valor", "g", 104)], W / 2, 330, "center", passo=0.14)
        E.frase(c, t, entre(a_, f, 0.25), [("ao", "i", 116), ("algarismo", "i", 116)], W / 2, 470, "center")
        E.frase(c, t, entre(a_, f, 0.48), [("é", "i", 180), ("o", "i", 180), ("lugar", "g", 180, COR)], W / 2, 680, "center", passo=0.14)
        E.frase(c, t, entre(a_, f, 0.72), [("onde", "i", 116), ("ele", "i", 116), ("está", "i", 116)], W / 2, 820, "center", passo=0.14)
    E.saida(c, t, C["s23"] - 0.1, resumo)
    if t < C["s23"]:
        return
    E.frase(c, t, C["s23.a"] - 1.0, [("próxima", "i", 84), ("aula", "i", 84)], XE, 270)
    E.frase(c, t, C["s23.a"], [("ler", "g", 120, COR), ("números", "g", 120, COR)], XE, 410)
    E.frase(c, t, C["s23.a"] + 0.5, [("na", "i", 84), ("casa", "i", 84), ("dos", "i", 84), ("milhões", "i", 84)], XE, 510)
    E.frase(c, t, C["s23.b"], [("dizer", "i", 84), ("qual", "i", 84), ("é", "i", 84), ("maior", "g", 84, COR)], XE, 640)
    E.foco(c, t, C["s23.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1400, 400, 76, estilo="g", cor=E.SOBRE, a=a))
    p = ease_io(prog(t, C["s23.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1760, 1530, p), lerp(720, 425, p), ep(t, C["s23.c"] + 0.2, 0.4))
    E.frase(c, t, C["s23.d"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 880, "center")


BLOCKS = dict(gancho=b_gancho, acolhida=b_acolhida, algarismos=b_algarismos, casas=b_casas, troca=b_troca, lugar=b_lugar,
              abrir=b_abrir, erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
