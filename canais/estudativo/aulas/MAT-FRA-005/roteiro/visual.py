"""Visual — Estudativo · MAT-FRA-005: comparar frações e marcar na reta.
Identidade em _ferramentas/editorial.py. As barras de chocolate mostram por que o tamanho dos números engana; no fim, a reta
numérica recebe 3/4 e 5/2 com pulos à vista. Todos os instantes vêm dos cues da voz.
Peças só desta aula: P, fica, relogio, conta, misto, eixo, sublinhas, pulo, ponto, cruz, garrafa."""
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, fr, sinal, palco, chocolate, chave, centro, pontes, frac_q
import motor as M
import skia

E.usar("Matemática", "Frações e Decimais")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-FRA-005_comparar_fracoes_marcar_na_reta.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("pedacos", "mmc", "atalho", "reta", "questao"))
BR = E.SOBRE


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças desta aula ----------------
def P(s, est="i", size=84, cor=None):
    """palavras de uma frase, todas no mesmo estilo"""
    return [(w, est, size, cor or TINTA) for w in s.split()]


def fica(c, t, t0, t1, partes, x, y, align="left", passo=0.15):
    """frase que entra em t0 e sai em t1"""
    E.saida(c, t, t1, lambda: E.frase(c, t, t0, partes, x, y, align, passo))


def relogio(c, t, t0, cx, cy):
    """relógio de pausa: enche nos 3 segundos da pausa"""
    r = 190 * ease_back(prog(t, t0, 0.6))
    if r <= 0:
        return
    E.bola(c, cx, cy, r)
    f = M.clamp(prog(t, t0 + 0.8, 3.0))
    if f > 0:
        E.arco(c, cx, cy, r + 30, -90, 360 * f, TINTA, 10)
    for dx in (-40, 40):
        M.rrect(c, cx + dx - 20, cy - 72, 40, 144, 11, BR, ep(t, t0 + 0.2, 0.4))
    E.foco(c, t, t0 + 0.2, 0.5, lambda a: centro(c, "pause o vídeo", cx, cy + 300, 60, "i", TINTA, a))


def conta(c, t, esq, t0, dir_, t1, x, y, size, cor=None, cor2=None):
    """conta em que o resultado só aparece quando é falado"""
    E.foco(c, t, t0, 0.5, lambda a: E.escreve(c, esq, x, y, size, "g", cor or TINTA, a))
    E.foco(c, t, t1, 0.4, lambda a: E.escreve(c, dir_, x + E.larg(esq, "g", size) + size * 0.28, y, size, "g", cor2 or cor or TINTA, a))


def misto(c, i, n, d, cx, cy, s, cor=None, a=1.0):
    """número misto: o inteiro grande e a fração ao lado"""
    if a <= 0:
        return
    n, d = str(n), str(d)
    wi = E.larg(str(i), "g", s * 1.7)
    wf = max(E.larg(n, "g", s), E.larg(d, "g", s)) + s * 0.2
    x0 = cx - (wi + s * 0.16 + wf) / 2
    E.escreve(c, str(i), x0, cy + s * 0.6, s * 1.7, "g", cor or TINTA, a)
    E.fracao(c, n, d, x0 + wi + s * 0.16 + wf / 2, cy, s, cor or TINTA, a)


def eixo(c, x0, x1, y, hi, p=1.0, a=1.0):
    """reta numérica de 0 a hi: cresce da esquerda para a direita, com seta na ponta e os inteiros marcados; p = 0..1"""
    if p <= 0 or a <= 0:
        return
    M.arrow(c, x0 - 40, y, x1 + 90, y, TINTA, a, 6, 26, p)
    for i in range(hi + 1):
        q = M.clamp(p * (hi + 1.4) - i)
        if q > 0:
            px = lerp(x0, x1, i / hi)
            M.line(c, px, y - 26, px, y + 26, TINTA, a * q, 6)
            centro(c, str(i), px, y + 92, 76, "g", TINTA, a * q)


def sublinhas(c, xa, xb, y, n, p, cor=None):
    """corta o trecho xa..xb em n partes iguais: as marcas crescem uma a uma; p = 0..1"""
    for i in range(1, n):
        q = ease_io(M.clamp(p * (n - 1) - (i - 1)))
        if q > 0:
            px = lerp(xa, xb, i / n)
            M.line(c, px, y - 20 * q, px, y + 20 * q, cor or COR, 1.0, 5)


def pulo(c, xa, xb, y, h, p, cor=None, largura=6):
    """pulo em arco sobre a reta, de xa até xb, com a ponta em seta; p = 0..1"""
    if p <= 0:
        return
    cor = cor or COR
    pts = [(lerp(xa, xb, p * i / 28), y - 8 - 4 * h * (p * i / 28) * (1 - p * i / 28)) for i in range(29)]
    path = skia.Path(); path.moveTo(*pts[0])
    for q in pts[1:]:
        path.lineTo(*q)
    c.drawPath(path, M.paint(cor, 1.0, stroke=largura, cap_round=True))
    (x1, y1), (x2, y2) = pts[-3], pts[-1]
    ang = M.math.atan2(y2 - y1, x2 - x1)
    seta = skia.Path(); seta.moveTo(x2 + 5 * M.math.cos(ang), y2 + 5 * M.math.sin(ang))
    seta.lineTo(x2 - 20 * M.math.cos(ang - 0.5), y2 - 20 * M.math.sin(ang - 0.5))
    seta.lineTo(x2 - 20 * M.math.cos(ang + 0.5), y2 - 20 * M.math.sin(ang + 0.5)); seta.close()
    c.drawPath(seta, M.paint(cor))


def ponto(c, x, y, p, cor=None):
    """o ponto marcado na reta"""
    r = 26 * ease_back(p)
    if r > 0:
        E.bola(c, x, y, r, cor)


def cruz(c, t, t0, n1, d1, n2, d2, xa, xb, y, s, ta, tb, cn, cl):
    """duas frações com a cruz: ta traça n1 × d2 (fica do lado esquerdo), tb traça n2 × d1 (fica do lado direito)"""
    fr(c, t, t0, n1, d1, xa, y, s, cn)
    fr(c, t, t0 + 0.2, n2, d2, xb, y, s, cn)
    ny, dy, m = y - s * 0.5, y + s * 0.5, s * 0.5
    p = ep(t, ta, 0.6)
    if p > 0:
        M.line(c, xa + m, ny, xb - m, dy, cl, 1.0, 8, progress=p)
    p = ep(t, tb, 0.6)
    if p > 0:
        M.line(c, xb - m, ny, xa + m, dy, cl, 1.0, 8, progress=p)


def garrafa(c, cx, y, w, h, n, cheias, a=1.0):
    """garrafa com n partes iguais e `cheias` partes de suco; y = topo do corpo"""
    if a <= 0:
        return
    x = cx - w / 2
    M.rrect(c, cx - w * 0.2, y - 58, w * 0.4, 76, 10, E.VAZIO, a, stroke=4, stroke_color=TINTA)
    rr = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 26, 26)
    c.drawRRect(rr, M.paint(E.VAZIO, a))
    c.save(); c.clipRRect(rr, True)
    al = h * cheias / n
    c.drawRect(skia.Rect.MakeXYWH(x, y + h - al, w, al), M.paint(COR, a))
    for i in range(1, n):
        ly = y + h * i / n
        M.line(c, x, ly, x + w, ly, BR if ly > y + h - al + 1 else FIO, a, 3, cap_round=False)
    c.restore()
    c.drawRRect(rr, M.paint(TINTA, a, stroke=4))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    s2, ta, tb, tc = C["s02"], C["s01.a"], C["s01.b"], C["s01.c"]

    def duelo():
        y, s, xa, xb = 400, 260, 500, 1420
        nao = tc + 1.7
        fr(c, t, ta, 2, 3, xa, y, s, COR)
        E.foco(c, t, ta + 0.4, 0.4, lambda a: centro(c, "ou", W / 2, y + 30, 120, "i", TINTA, a))
        fr(c, t, tb, 3, 5, xb, y, s, ERRADO if t >= nao else None)
        E.saida(c, t, nao - 0.1, lambda: E.frase(c, t, tb + 0.9, P("qual é maior?", "g", 96, COR), W / 2, 830, "center", passo=0.17), d=0.25)
        E.frase(c, t, nao, P("não!", "g", 130, ERRADO), W / 2, 760, "center")
        if t >= nao:
            E.risco(c, xb - 170, y + 190, xb + 170, y - 190, t, nao, largura=20)
        E.frase(c, t, nao + 0.5, P("em fração, o") + P("tamanho dos números", "g", 76, COR) + P("engana"), W / 2, 930, "center", passo=0.15)
    E.saida(c, t, s2 - 0.1, duelo)
    if t < s2:
        return

    E.frase(c, t, s2 + 0.2, P("até o fim desta aula, você vai", size=80, cor=COR), XE, 200, passo=0.13)
    ta2, tb2, tc2 = C["s02.a"], C["s02.b"], C["s02.c"]
    y = 400
    E.foco(c, t, ta2, 0.5, lambda a: (E.fracao(c, 2, 3, 240, y - 28, 88, COR, a), E.escreve(c, "?", 315, y + 8, 100, "g", TINTA2, a), E.fracao(c, 3, 5, 430, y - 28, 88, TINTA, a)))
    E.frase(c, t, ta2 + 0.1, P("comparar", "g", 88) + P("por dois caminhos", "i", 96), 600, y, passo=0.15)
    y = 640
    E.foco(c, t, tb2, 0.5, lambda a: (eixo(c, 200, 450, y - 36, 1, 1.0, a), None))
    E.frase(c, t, tb2 + 0.1, P("marcar", "g", 88) + P("frações na reta", "i", 96), 600, y, passo=0.15)
    y = 860
    p = ease_back(prog(t, tc2 - 0.1, 0.5))
    if p > 0:
        E.mais(c, 335, y - 30, 62 * p, giro=(1 - p) * 90)
    E.frase(c, t, tc2, P("atalho", "g", 88) + P("de prova", "i", 96), 600, y, passo=0.15)


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    ta = C["s03.a"]
    E.frase(c, t, C["s03"] + 0.3, P("para acompanhar,", size=76), XE, 310)
    E.frase(c, t, ta - 0.8, P("você precisa de", size=76), XE, 400, passo=0.14)
    E.foco(c, t, ta, 0.5, lambda a: E.escreve(c, "4", XE - 8, 710, 320, "g", COR, a))
    E.foco(c, t, ta + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 225, 690, 110, "i", TINTA, a))
    itens = ((C["s03.b"], "Frações", "equivalentes"), (C["s03.c"], "O", "MMC"), (C["s03.d"], "Número", "misto"), (C["s03.e"], "A reta", "numérica"))
    for i, (t0, l1, l2) in enumerate(itens):
        x, y = 830 + (i % 2) * 470, 200 + (i // 2) * 310
        p = ep(t, t0, 0.5)
        E.caixa_pontilhada(c, x, y, 440, 270, p, prog_=p)
        E.frase(c, t, t0 + 0.1, [(l1, "i", 66)], x + 34, y + 110)
        E.frase(c, t, t0 + 0.2, [(l2, "g", 62, COR)], x + 34, y + 190)
    E.frase(c, t, C["s04"] - 1.6, P("procure a aula", size=60) + P("no canal", "g", 54, COR), XE, 850, passo=0.14)


# ---------------- pedaços ----------------
def b_pedacos(c, t, C, b):
    s5 = C["s05"]
    ta, tb, tc = C["s04.a"], C["s04.b"], C["s04.c"]
    xa, xb = C["s05.a"], C["s05.b"]
    x, w, h = 500, 1200, 150

    def iguais():
        E.frase(c, t, ta - 1.6, P("fácil em um caso:", size=88), XE, 180, passo=0.15)
        E.frase(c, t, ta, P("o de baixo", size=96) + P("é igual", "g", 88, COR), 900, 180, passo=0.16)
        for y, n, cor, t0 in ((280, 5, COR, tb), (520, 3, TINTA2, tb + 0.8)):
            E.foco(c, t, t0, 0.5, lambda a, y=y, n=n, cor=cor: (E.fracao(c, n, 7, 310, y + h / 2, 92, cor, a),
                                                                chocolate(c, x, y, w, h, 7, [(i, cor, 1) for i in range(n)], a)))
        E.frase(c, t, tb + 1.4, P("pedaços do", size=72) + P("mesmo tamanho", "g", 66, COR), W / 2, 790, "center", passo=0.14)
        y = 920
        E.frase(c, t, tc - 1.5, P("quem tem mais pedaços ganha:", size=72), XE, y, passo=0.13)
        E.foco(c, t, tc, 0.5, lambda a: (M.rrect(c, 1120, y - 76, 610, 110, 55, CERTO, a), centro(c, "5/7 é maior", 1425, y, 76, "g", BR, a)))
    E.saida(c, t, s5 - 0.1, iguais)
    if t < s5 - 0.1:
        return

    E.frase(c, t, s5 + 0.2, P("com dois terços e três quintos,", size=88), W / 2, 170, "center", passo=0.14)
    for y, d, n, t0 in ((280, 3, 2, s5 + 0.3), (500, 5, 3, s5 + 0.5)):
        E.foco(c, t, t0, 0.5, lambda a, y=y, d=d, n=n: (E.fracao(c, n, d, 310, y + h / 2, 92, COR, a),
                                                       chocolate(c, x, y, w, h, d, [(i, COR, 1) for i in range(n)], a)))
    E.frase(c, t, xa, P("pedaços de") + P("tamanhos diferentes", "g", 76, ERRADO), W / 2, 760, "center", passo=0.15)
    # 15 pedaços nas duas barras: o mesmo corte para as duas
    E.frase(c, t, xb - 1.5, P("a saída: cortar tudo no", size=76), 340, 900, passo=0.13)
    E.frase(c, t, xb, P("mesmo tamanho", "g", 84, COR), 1020, 900)
    for i in range(1, 15):
        q = ep(t, xb + i * 0.04, 0.4)
        if q > 0:
            px = x + w * i / 15
            for y in (280, 500):
                M.line(c, px, y + 3, px, y + 3 + (h - 6) * q, BR if px < x + w * (2 / 3 if y == 280 else 3 / 5) else FIO, 0.9, 3)


# ---------------- MMC ----------------
def b_mmc(c, t, C, b):
    s7, s9 = C["s07"], C["s09"]
    ta, tb = C["s06.a"], C["s06.b"]

    def multiplos():
        E.frase(c, t, ta, P("MMC:", "g", 100, COR) + P("o mínimo múltiplo comum", size=100), W / 2, 200, "center", passo=0.15)
        E.frase(c, t, ta + 1.4, P("o menor número nas duas tabuadas", size=72), W / 2, 310, "center", passo=0.13)
        for y, base, vals, t0 in ((500, 3, (3, 6, 9, 12, 15), ta + 2.0), (680, 5, (5, 10, 15), ta + 2.5)):
            E.foco(c, t, t0, 0.4, lambda a, base=base, y=y: E.escreve(c, f"tabuada do {base}", XE, y, 62, "i", TINTA, a))
            for v in vals:
                x = 620 + (v / 15) * 1000 - 100
                if v == 15:
                    E.foco(c, t, tb, 0.4, lambda a, x=x, y=y: E.bola(c, x, y - 33, 74, CERTO, a))
                E.foco(c, t, t0 + v * 0.03, 0.35, lambda a, v=v, x=x, y=y: centro(c, str(v), x, y, 92, "g", BR if v == 15 and t >= tb else TINTA, a))
        E.foco(c, t, tb, 0.5, lambda a: centro(c, "MMC(3, 5) = 15", W / 2, 890, 110, "g", COR, a))
    E.saida(c, t, s7 - 0.1, multiplos)
    if t < s7 - 0.1:
        return

    # as duas trocas
    a1, b1, c1 = C["s07.a"], C["s07.b"], C["s07.c"]
    a2, b2, c2 = C["s08.a"], C["s08.b"], C["s08.c"]
    xa, xb = C["s09.a"], C["s09.b"]
    fica(c, t, s7 + 0.2, s9 - 0.1, P("com") + P("15", "g", 76, COR) + P("embaixo"), W / 2, 110, "center")
    fica(c, t, s9 + 0.1, C["s10"] - 1.7, P("pedaços iguais,") + P("é só contar", "g", 76, COR), W / 2, 110, "center")
    E.frase(c, t, C["s10"] - 1.6, P("por pouco,", size=84) + P("mas é", "g", 76, CERTO), W / 2, 110, "center", passo=0.14)
    s, x0, x1 = 120, 280, 720
    bx, bw, bh = 880, 840, 120
    for y, n, d, m, nf, tt, tb_, tc_ in ((260, 2, 3, 5, 10, a1, b1, c1), (590, 3, 5, 3, 9, a2, b2, c2)):
        fr(c, t, tt, n, d, x0, y, s, COR)
        pontes(c, t, x0 + 90, x1 - 80, y, s, f"× {m}", tb_, tt + 0.9, size=50)
        frac_q(c, t, tt + 0.2, nf, 15, tb_ + 0.8, tt + 0.9, x1, y, s)
        cor = COR
        ped = [(i, cor, prog(t, tc_ + i * 0.08, 0.3)) for i in range(nf)]
        E.foco(c, t, tt + 0.3, 0.5, lambda a, y=y, ped=ped: chocolate(c, bx, y - bh / 2, bw, bh, 15, ped, a))
        chave(c, bx + 4, bx + bw * nf / 15 - 4, y + bh / 2 + 12, COR, ep(t, xa, 0.4))
        E.foco(c, t, xa + 0.1, 0.4, lambda a, y=y, nf=nf: centro(c, f"{nf} pedaços", bx + bw * nf / 30, y + bh / 2 + 92, 62, "b", COR, a))
    y = 930
    E.frase(c, t, xa, [("10 > 9", "g", 110, COR)], 700, y, "center")
    E.foco(c, t, xb, 0.5, lambda a: (E.fracao(c, 2, 3, 1110, y - 36, 88, CERTO, a), E.escreve(c, ">", 1210, y - 6, 100, "g", CERTO, a), E.fracao(c, 3, 5, 1360, y - 36, 88, CERTO, a)))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    s11, ta, tb, tc = C["s11"], C["s10.a"], C["s10.b"], C["s10.c"]
    xa, xb = C["s11.a"], C["s11.b"]
    x, w, h = 500, 1200, 160
    E.frase(c, t, ta, P("o erro:", "g", 88, ERRADO) + P("número maior é fração maior?", size=92), W / 2, 170, "center", passo=0.14)
    E.foco(c, t, tb, 0.5, lambda a: (E.fracao(c, 1, 2, 310, 345, 96, COR, a), chocolate(c, x, 265, w, h, 2, [(0, COR, 1)], a)))
    E.foco(c, t, tc, 0.5, lambda a: (E.fracao(c, 1, 8, 310, 585, 96, ERRADO, a), chocolate(c, x, 505, w, h, 8, [(0, ERRADO, 1)], a)))
    fica(c, t, s11 + 0.1, xa - 0.1, P("8 é maior que 2,", "g", 76) + P("mas", size=84), W / 2, 800, "center")
    E.frase(c, t, xa, P("cortar em oito dá", size=84) + P("pedaços menores", "g", 76, ERRADO), W / 2, 800, "center", passo=0.14)
    E.frase(c, t, xb - 1.0, P("quanto maior o de baixo,", size=84), 280, 920, passo=0.14)
    E.frase(c, t, xb, P("menor o pedaço", "g", 76, COR), 1120, 920)
    # a chave compara o pedaço de cada barra
    chave(c, x + 6, x + w / 2 - 6, 265 + h + 12, COR, ep(t, xa, 0.4))
    chave(c, x + 6, x + w / 8 - 6, 505 + h + 12, ERRADO, ep(t, xa + 0.2, 0.4))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    s13, s14 = C["s13"], C["s14"]
    ta, tb = C["s12.a"], C["s12.b"]

    def titulo():
        E.frase(c, t, C["s12"] + 0.3, P("e o atalho prometido", "i", 86, CLARO), W / 2, 200, "center")
        E.frase(c, t, ta, P("o teste da", "i", 170, BR) + P("cruz", "g", 160, BR), W / 2, 430, "center", passo=0.2)
        E.foco(c, t, ta + 0.8, 0.5, lambda a: E.pilula(c, "produto cruzado", W / 2, 580, 58, estilo="b", fundo=E.COR, cor=BR, a=a))
        E.frase(c, t, tb - 2.2, P("lá, dizia se duas frações eram", "i", 72, CLARO) + P("iguais", "g", 66, BR), W / 2, 760, "center", passo=0.13)
        E.frase(c, t, tb, P("também diz", "i", 96, CLARO) + P("qual é a maior", "g", 90, BR), W / 2, 900, "center", passo=0.15)
    E.saida(c, t, s13 - 0.1, titulo)
    if t < s13 - 0.1:
        return

    def teste():
        xa, xb, xc, xd = C["s13.a"], C["s13.b"], C["s13.c"], C["s13.d"]
        y, s, x1, x2 = 500, 180, 660, 1260
        E.frase(c, t, s13 + 0.2, P("multiplique em cruz", "g", 84, BR), W / 2, 170, "center")
        E.frase(c, t, xa, P("o resultado fica do lado da fração", "i", 70, CLARO), W / 2, 270, "center", passo=0.12)
        cruz(c, t, s13 + 0.2, 2, 3, 3, 5, x1, x2, y, s, xb, xc, BR, CLARO)
        E.foco(c, t, xb, 0.45, lambda a: centro(c, "2 × 5", 300, y - 110, 72, "b", CLARO, a))
        E.foco(c, t, xb + 0.8, 0.4, lambda a: (E.bola(c, 300, y + 40, 96, CERTO if t >= xd else E.COR, a), centro(c, "10", 300, y + 74, 104, "g", BR, a)))
        E.foco(c, t, xc, 0.45, lambda a: centro(c, "3 × 3", 1620, y - 110, 72, "b", CLARO, a))
        E.foco(c, t, xc + 0.8, 0.4, lambda a: (E.bola(c, 1620, y + 40, 96, E.COR, a), centro(c, "9", 1620, y + 74, 104, "g", BR, a)))
        r = 62
        cx = (x1 + x2) / 2
        if t >= xb:
            c.drawCircle(cx, y, r, M.paint("#0A0820"))
        sinal(c, t, xd, ">", cx, y - 3, 110, CERTO)
        E.frase(c, t, xd, P("10 > 9:", "g", 76, BR) + P("dois terços é maior", "i", 84, CLARO), W / 2, 870, "center", passo=0.14)
    E.saida(c, t, s14 - 0.1, teste)
    if t < s14 - 0.1:
        return

    xa, xb, xc, xd = C["s14.a"], C["s14.b"], C["s14.c"], C["s14.d"]
    E.frase(c, t, xa, P("a cruz deixa o", "i", 80, CLARO) + P("mesmo número embaixo", "g", 74, BR), W / 2, 170, "center", passo=0.14)
    y = 400
    fr(c, t, xa + 0.3, 10, 15, 400, y, 130, BR)
    fr(c, t, xa + 0.5, 9, 15, 720, y, 130, CLARO)
    E.foco(c, t, xb, 0.5, lambda a: E.escreve(c, "3 × 5 = 15", 950, y + 10, 92, "g", BR, a))
    E.foco(c, t, xb + 0.4, 0.4, lambda a: E.escreve(c, "sem escrever", 950, y + 100, 66, "i", CLARO, a))
    y = 740
    E.frase(c, t, xc, P("não compensa com", "i", 72, CLARO), XE, 620, passo=0.13)
    for i, (n, d) in enumerate(((1, 2), (2, 3), (3, 4))):
        fr(c, t, xc + i * 0.15, n, d, 260 + i * 200, y, 100, BR)
    E.frase(c, t, xc + 1.0, P("só compara de duas em duas", "i", 70, CLARO), 860, y + 10, passo=0.12)
    E.foco(c, t, xd, 0.5, lambda a: E.pilula(c, "use o MMC", W / 2, 930, 70, estilo="g", fundo=CERTO, cor=BR, a=a))


# ---------------- a reta ----------------
X0, X1, YR = 250, 1650, 660


def px(v):
    return lerp(X0, X1, v / 3)


def b_reta(c, t, C, b):
    ta, tb = C["s15.a"], C["s15.b"]
    a6, b6, c6, d6 = C["s16.a"], C["s16.b"], C["s16.c"], C["s16.d"]
    a7, b7, c7, d7, e7 = C["s17.a"], C["s17.b"], C["s17.c"], C["s17.d"], C["s17.e"]
    a8, b8, c8 = C["s18.a"], C["s18.b"], C["s18.c"]

    eixo(c, X0, X1, YR, 3, ease_io(prog(t, ta, 1.0)))

    # s15: o que é a reta
    def apresenta():
        E.frase(c, t, C["s15"] + 0.2, P("vamos para a") + P("reta", "g", 76, COR), W / 2, 190, "center")
        E.frase(c, t, ta, P("uma linha com os números em ordem", size=76), W / 2, 320, "center", passo=0.13)
        q = ep(t, tb, 0.7)
        if q > 0:
            M.arrow(c, X0, 500, X1, 500, COR, q, 7, 26, q)
        E.frase(c, t, tb + 0.2, P("mais à direita,") + P("maior", "g", 76, COR), W / 2, 460, "center", passo=0.15)
        E.frase(c, t, tb + 1.8, P("fração também tem lugar nela", size=76, cor=COR), W / 2, 880, "center", passo=0.13)
    E.saida(c, t, a6 - 0.15, apresenta)

    # s16: três quartos
    def marca34():
        E.foco(c, t, a6, 0.5, lambda a: E.fracao(c, 3, 4, XE + 70, 260, 120, COR, a))
        E.frase(c, t, a6 + 0.4, P("de cima menor:", size=76), 390, 285, passo=0.13)
        E.frase(c, t, b6, P("entre 0 e 1", "g", 76, COR), 930, 285)
    E.saida(c, t, a7 - 0.15, marca34)

    def fala34():
        fica(c, t, c6, d6 - 0.1, P("corte em") + P("4 partes iguais", "g", 76, COR), W / 2, 900, "center")
        E.frase(c, t, d6, P("ande") + P("3 partes", "g", 76, COR) + P("a partir do zero"), W / 2, 900, "center", passo=0.14)
    E.saida(c, t, a7 - 0.15, fala34)
    q = ep(t, b6, 0.6)   # o trecho de 0 a 1
    if q > 0:
        M.line(c, px(0), YR, lerp(px(0), px(1), q), YR, COR, 1.0, 12)
    sublinhas(c, px(0), px(1), YR, 4, prog(t, c6, 0.8))
    for i in range(3):
        E.saida(c, t, a8 - 0.1, lambda i=i: pulo(c, px(i / 4), px((i + 1) / 4), YR, 62, ease_io(prog(t, d6 + 0.2 + i * 0.5, 0.45))), d=0.3)
    ponto(c, px(0.75), YR, prog(t, d6 + 1.6, 0.4))
    E.foco(c, t, d6 + 1.6, 0.5, lambda a: E.fracao(c, 3, 4, px(0.75), 470, 92, COR, a))

    # s17: cinco meios
    def marca52():
        E.foco(c, t, a7, 0.5, lambda a: E.fracao(c, 5, 2, XE + 70, 260, 120, COR, a))
        E.saida(c, t, b7 - 0.1, lambda: E.frase(c, t, a7 + 0.4, P("de cima maior:", size=76) + P("vire número misto", "g", 70, COR), 390, 285, passo=0.13), d=0.25)
        conta(c, t, "5 ÷ 2 = 2,", b7, "sobra 1", b7 + 1.3, 390, 285, 80)
        E.foco(c, t, c7, 0.5, lambda a: (E.escreve(c, "=", 1160, 288, 110, "g", TINTA, a), misto(c, 2, 1, 2, 1400, 255, 110, COR, a)))
    E.saida(c, t, a8 - 0.15, marca52)

    def fala52():
        fica(c, t, d7, e7 - 0.1, P("vá até o") + P("2", "g", 76, COR), W / 2, 900, "center")
        E.frase(c, t, e7, P("ande") + P("metade do caminho", "g", 76, COR) + P("até o 3"), W / 2, 900, "center", passo=0.14)
    E.saida(c, t, a8 - 0.15, fala52)
    E.saida(c, t, a8 - 0.1, lambda: pulo(c, px(0), px(2), YR, 92, ease_io(prog(t, d7, 0.7)), TINTA2, 5), d=0.3)
    sublinhas(c, px(2), px(3), YR, 2, prog(t, e7, 0.3))
    E.saida(c, t, a8 - 0.1, lambda: pulo(c, px(2), px(2.5), YR, 46, ease_io(prog(t, e7 + 0.3, 0.5))), d=0.3)
    ponto(c, px(2.5), YR, prog(t, e7 + 0.8, 0.4))
    E.foco(c, t, e7 + 0.8, 0.5, lambda a: E.fracao(c, 5, 2, px(2.5), 470, 92, COR, a))

    # s18: a comparação, sem conta
    E.foco(c, t, a8, 0.5, lambda a: centro(c, "antes do 1", px(0.75), 310, 66, "b", COR, a))
    E.foco(c, t, b8, 0.5, lambda a: centro(c, "depois do 2", px(2.5), 310, 66, "b", COR, a))
    E.frase(c, t, b8 + 1.0, P("a comparação sem conta", size=76), W / 2, 200, "center", passo=0.13)
    E.frase(c, t, c8, P("mais à direita:") + P("5/2 é maior", "g", 80, CERTO), W / 2, 900, "center", passo=0.15)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    ta, tb, tc = C["s19.a"], C["s19.b"], C["s19.c"]
    E.frase(c, t, C["s19"] + 0.3, P("hora de testar", size=72, cor=COR), XE, 170)
    E.frase(c, t, ta - 1.2, P("duas garrafas iguais de suco", size=76), XE, 290, passo=0.13)
    y, h = 410, 340
    E.foco(c, t, ta, 0.5, lambda a: garrafa(c, 320, y, 200, h, 7, 4, a))
    E.foco(c, t, ta + 0.1, 0.5, lambda a: E.fracao(c, 4, 7, 540, y + h / 2, 120, COR, a))
    E.foco(c, t, tb, 0.5, lambda a: garrafa(c, 820, y, 200, h, 5, 3, a))
    E.foco(c, t, tb + 0.1, 0.5, lambda a: E.fracao(c, 3, 5, 1040, y + h / 2, 120, TINTA, a))
    E.frase(c, t, tc, P("qual tem", size=120) + P("mais suco?", "g", 110, COR), XE, 920, passo=0.15)
    relogio(c, t, C["s20.a"], 1530, 340)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    ta, tb, tc = C["s21.a"], C["s21.b"], C["s21.c"]
    xa, xb = C["s22.a"], C["s22.b"]
    E.frase(c, t, C["s21"] + 0.2, P("pela cruz", size=80, cor=COR), W / 2, 130, "center")
    y, s, x1, x2 = 330, 150, 680, 1240
    cruz(c, t, C["s21"] + 0.3, 4, 7, 3, 5, x1, x2, y, s, ta, tb, TINTA, CINZA)
    conta(c, t, "4 × 5 =", ta, "20", ta + 0.9, XE, y + 30, 72, TINTA, COR)
    conta(c, t, "7 × 3 =", tb, "21", tb + 0.9, 1400, y + 30, 72, TINTA, CERTO if t >= tc else COR)
    r = 54
    cx = (x1 + x2) / 2
    if t >= ta:
        c.drawCircle(cx, y, r, M.paint(E.PAPEL))
    sinal(c, t, tc, "<", cx, y - 3, 96, CERTO)
    E.foco(c, t, tc + 0.4, 0.5, lambda a: (M.rrect(c, 420, 545, 1080, 130, 65, CERTO, a), centro(c, "a garrafa com 3/5 tem mais suco", W / 2, 632, 62, "g", BR, a)))
    # pelo MMC
    E.frase(c, t, C["s22"] + 0.1, P("pelo") + P("MMC", "g", 76, COR) + P("dá o mesmo"), XE, 840, passo=0.14)
    fr(c, t, xa, 20, 35, 1080, 830, 120, TINTA)
    E.frase(c, t, xb - 0.5, P("contra", size=76), 1220, 855)
    fr(c, t, xb, 21, 35, 1530, 830, 120, CERTO)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    s24 = C["s24"]

    def resumo():
        E.frase(c, t, C["s23"] + 0.3, P("resumindo", size=92, cor=COR), W / 2, 170, "center")
        itens = ((C["s23.a"], "pedaços do mesmo tamanho"), (C["s23.b"], "ou a cruz"), (C["s23.c"], "na reta: mais à direita, maior"))
        for i, (t0, s) in enumerate(itens):
            y = 400 + i * 190
            E.foco(c, t, t0, 0.5, lambda a, i=i, y=y: (E.bola(c, 250, y - 30, 58, a=a), centro(c, str(i + 1), 250, y - 7, 64, "g", BR, a)))
            E.frase(c, t, t0 + 0.1, [(s, "g", 88)], 350, y)
    E.saida(c, t, s24 - 0.1, resumo)
    if t < s24 - 0.1:
        return

    ta, tb, tc = C["s24.a"], C["s24.b"], C["s24.c"]
    E.frase(c, t, s24 + 0.2, P("próxima aula"), XE, 190)
    E.frase(c, t, ta, P("Praticando", "g", 124, COR), XE, 340)
    E.frase(c, t, ta + 0.5, P("simplificar, comparar", size=88), XE, 480, passo=0.15)
    E.frase(c, t, ta + 1.0, P("e calcular a fração de uma quantidade", size=88), XE, 590, passo=0.15)
    E.foco(c, t, tb, 0.5, lambda a: E.pilula(c, "Inscreva-se", 1460, 300, 84, estilo="g", cor=BR, a=a))
    p = ease_io(prog(t, tb + 0.3, 0.8))
    E.cursor(c, lerp(1770, 1650, p), lerp(520, 340, p), ep(t, tb + 0.2, 0.4), cor=TINTA)
    E.frase(c, t, tc, [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 870, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, pedacos=b_pedacos, mmc=b_mmc, erro=b_erro, atalho=b_atalho, reta=b_reta,
              questao=b_questao, resposta=b_resposta, fim=b_fim)
