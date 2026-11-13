"""Visual — Estudativo · QUI-MIS-007: decantar, filtrar e centrifugar.

Segue a LINGUAGEM VISUAL DA QUÍMICA (cabeçalho de QUI-MIS-001/roteiro/visual.py) e as convenções da separação de misturas
(QUI-MIS-006: o aparelho do dia a dia desenhado e animado; o que SAI se move, o que FICA para). Nesta aula:
- barro = grãos cor de terra (BARRO) que descem no tempo da fala; água limpa = Q.AGUA; óleo = âmbar (OLEO);
- o funil de decantação (funil_sep) escoa a camada de baixo para o béquer, com o filete visível; a divisa fica marcada;
- densidade escrita ao lado de cada líquido, em g/cm³, em tinta; o mais denso fica embaixo, sempre.
Peças candidatas ao kit: funil_sep (funil de decantação com escoamento), filtro (funil com papel), centrifuga, tubo_sangue,
copo_barro (decantação animada).
Todo instante vem de C[...] (marcadores do roteiro)."""
import math
import random

import editorial as E
import quimica as Q
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Química", "Matéria e Misturas")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_QUI-MIS-007_decantar_filtrar_centrifugar.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("decantar", "filtrar", "centrifugar", "funil", "atalho", "questao", "fim"))
BR = "#FFFFFF"
OLEO = "#E8B23A"
BARRO = "#8B5E34"
DENSO = "#C8D3F0"  # o líquido de densidade 1,5 da questão (incolor-azulado, diferente da água)
D_AGUA, D_OLEO, D_OUTRO = 1.0, 0.9, 1.5
assert D_AGUA > D_OLEO and D_OUTRO > D_AGUA  # sai primeiro a água; no 2º caso, sai o outro


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def pilula_em(c, t, t0, s, cx, cy, size, fundo=None, est="g", cor=BR):
    E.foco(c, t, t0, 0.4, lambda a: E.pilula(c, s, cx, cy, size, est, fundo=fundo, a=a, cor=cor))


def lista(c, t, itens, x, y0, dy, r=44):
    for i, (ti, partes) in enumerate(itens):
        y = y0 + i * dy
        E.foco(c, t, ti, 0.5, lambda a, i=i, y=y: (E.bola(c, x + 40, y - 26, r, a=a), centro(c, str(i + 1), x + 40, y - 4, 54, "g", E.SOBRE, a)))
        E.frase(c, t, ti + 0.1, partes, x + 110, y, passo=0.12)


def riscado(c, t, t0, s, x, y, size=56):
    E.foco(c, t, t0, 0.4, lambda a: E.escreve(c, s, x, y, size, "i", ERRADO, a))
    if t >= t0 + 0.8:
        E.risco(c, x - 10, y + 14, x + E.larg(s, "i", size) + 10, y - size * 0.6, t, t0 + 0.8, largura=8)


def copo(c, t, t0, cx, yb, w, h, nivel=0.7, cor=None, a=1.0):
    """béquer simples: devolve (dentro, topo do líquido, fundo)"""
    if t < t0 or a <= 0:
        return None
    q = ep(t, t0, 0.5) * a
    contorno, dentro, (yt, yb_) = Q._copo_path("bequer", cx, yb, w, h)
    c.drawPath(dentro, M.paint(BR, 0.45 * q))
    yl = yb_ - (yb_ - yt) * nivel
    if nivel > 0:
        c.save(); c.clipPath(dentro, skia.ClipOp.kIntersect, True)
        c.drawRect(skia.Rect.MakeLTRB(cx - w, yl, cx + w, yb_ + 2), M.paint(cor or Q.AGUA, 0.92 * q))
        M.line(c, cx - w, yl, cx + w, yl, BR, 0.6 * q, 4)
        c.restore()
    c.drawPath(contorno, M.paint(Q.VIDRO, q, stroke=5))
    M.line(c, cx - w * 0.36, yt + h * 0.18, cx - w * 0.36, yt + h * 0.55, BR, 0.7 * q, max(4, w * 0.03))
    return dentro, yl, yb_


def copo_barro(c, t, t0, cx, yb, w, h, td, d=4.0, a=1.0, nivel=0.7, semente=3, turvo=True):
    """água barrenta que decanta: os grãos descem de td a td + d e formam o lodo no fundo"""
    r = copo(c, t, t0, cx, yb, w, h, nivel, M.mix(Q.AGUA, BARRO, 0.35 * (1 - ep(t, td, d)) if turvo else 0), a)
    if not r:
        return
    dentro, yl, yb_ = r
    q = ep(t, t0, 0.5) * a
    rnd = random.Random(semente)
    c.save(); c.clipPath(dentro, skia.ClipOp.kIntersect, True)
    for k in range(70):
        x = cx + (rnd.random() - 0.5) * (w - 24)
        y0 = yl + 10 + rnd.random() * (yb_ - yl - 20)
        yf = yb_ - 6 - rnd.random() * 28
        u = ease_io(prog(t, td + rnd.random() * d * 0.5, d * 0.6))
        c.drawCircle(x, lerp(y0, yf, u), 4 + 3 * rnd.random(), M.paint(BARRO if rnd.random() < 0.7 else "#A97A4A", q))
    c.restore()


def filtro(c, t, t0, cx, ytop, a=1.0, tp=None, retido=0.0):
    """funil com papel de filtro sobre um béquer; tp = instante em que a mistura passa; retido = areia no papel (0..1)"""
    if t < t0 or a <= 0:
        return
    q = ep(t, t0, 0.5) * a
    w, h = 300, 220
    cone = skia.Path(); cone.moveTo(cx - w / 2, ytop); cone.lineTo(cx + w / 2, ytop); cone.lineTo(cx + 22, ytop + h); cone.lineTo(cx - 22, ytop + h); cone.close()
    c.drawPath(cone, M.paint(BR, 0.5 * q))
    papel = skia.Path(); papel.moveTo(cx - w / 2 + 18, ytop + 6); papel.lineTo(cx + w / 2 - 18, ytop + 6); papel.lineTo(cx, ytop + h - 10); papel.close()
    c.drawPath(papel, M.paint("#F7F3EA", q)); c.drawPath(papel, M.paint("#C9C2B0", q, stroke=3))
    if retido > 0:
        bolo = skia.Path(); hh = 90 * retido
        bolo.moveTo(cx - hh * 0.6, ytop + h - 10 - hh); bolo.lineTo(cx + hh * 0.6, ytop + h - 10 - hh); bolo.lineTo(cx, ytop + h - 14); bolo.close()
        c.drawPath(bolo, M.paint(BARRO, q))
    c.drawPath(cone, M.paint(Q.VIDRO, q, stroke=5))
    M.line(c, cx, ytop + h, cx, ytop + h + 110, Q.VIDRO, q, 20)
    if tp is not None and t >= tp:
        for k in range(4):
            u = (t * 1.2 + k / 4) % 1
            E.bola(c, cx, ytop + h + 120 + u * 160, 9, Q.AGUA, q)


def centrifuga(c, t, t0, cx, cy, r, a=1.0, gira=0.0):
    """rotor visto de cima com quatro tubos girando; gira = ângulo em graus"""
    if t < t0 or a <= 0:
        return
    q = ep(t, t0, 0.5) * a
    c.drawCircle(cx, cy, r + 30, M.paint("#DDE3EA", q)); c.drawCircle(cx, cy, r + 30, M.paint(Q.VIDRO, q, stroke=5))
    for k in range(4):
        ang = math.radians(gira + 90 * k)
        x, y = cx + r * 0.62 * math.cos(ang), cy + r * 0.62 * math.sin(ang)
        c.save(); c.translate(x, y); c.rotate(math.degrees(ang))
        M.rrect(c, -r * 0.32, -22, r * 0.64, 44, 22, BR, q, stroke=3, stroke_color=Q.VIDRO)
        M.rrect(c, 0, -18, r * 0.3, 36, 18, "#B3262B", q)
        M.rrect(c, -r * 0.3, -18, r * 0.3, 36, 18, "#F2D27A", q)
        c.restore()
    E.bola(c, cx, cy, 30, "#6E747C", q)
    if gira:
        for k in range(3):
            E.arco(c, cx, cy, r + 60, gira * 1.2 + 120 * k, 60, E.COR, 6, 0.7 * q)


def tubo_sangue(c, cx, yb, h, sep, a=1.0):
    """tubo de ensaio com sangue: sep 0..1 separa o plasma (em cima, amarelo) das células (embaixo, vermelho)"""
    w = 90
    contorno, dentro, (yt, yb_) = Q._copo_path("tubo", cx, yb, w, h)
    c.drawPath(dentro, M.paint(BR, 0.5 * a))
    c.save(); c.clipPath(dentro, skia.ClipOp.kIntersect, True)
    yl = yb_ - (yb_ - yt) * 0.8
    ym = lerp(yl, yb_ - (yb_ - yt) * 0.36, sep)
    c.drawRect(skia.Rect.MakeLTRB(cx - w, yl, cx + w, ym), M.paint(M.mix("#9E1B22", "#F2D27A", sep), a))
    c.drawRect(skia.Rect.MakeLTRB(cx - w, ym, cx + w, yb_ + 2), M.paint("#9E1B22", a))
    c.restore()
    c.drawPath(contorno, M.paint(Q.VIDRO, a, stroke=5))
    return yl, ym, yb_


def funil_sep(c, t, t0, cx, ytop, baixo, cima, u=0.0, a=1.0, divisa=False):
    """funil de decantação: líquido de baixo (cor) e de cima (cor); u 0..1 = quanto do de baixo já escoou para o béquer"""
    if t < t0 or a <= 0:
        return None
    q = ep(t, t0, 0.5) * a
    w, h = 340, 470
    corpo = skia.Path()
    corpo.moveTo(cx - 34, ytop); corpo.lineTo(cx - 34, ytop + 40)
    corpo.cubicTo(cx - w * 0.62, ytop + h * 0.22, cx - w * 0.5, ytop + h * 0.6, cx - 16, ytop + h)
    corpo.lineTo(cx + 16, ytop + h)
    corpo.cubicTo(cx + w * 0.5, ytop + h * 0.6, cx + w * 0.62, ytop + h * 0.22, cx + 34, ytop + 40)
    corpo.lineTo(cx + 34, ytop); corpo.close()
    c.drawPath(corpo, M.paint(BR, 0.5 * q))
    yfundo = ytop + h
    hb0, ht = h * 0.3, h * 0.26
    hb = hb0 * (1 - u)
    c.save(); c.clipPath(corpo, skia.ClipOp.kIntersect, True)
    yb_top = yfundo - hb
    c.drawRect(skia.Rect.MakeLTRB(cx - w, yb_top, cx + w, yfundo + 2), M.paint(baixo, 0.95 * q))
    c.drawRect(skia.Rect.MakeLTRB(cx - w, yb_top - ht, cx + w, yb_top), M.paint(cima, 0.95 * q))
    M.line(c, cx - w, yb_top - ht, cx + w, yb_top - ht, BR, 0.6 * q, 4)
    c.restore()
    c.drawPath(corpo, M.paint(Q.VIDRO, q, stroke=5))
    M.rrect(c, cx - 44, ytop - 40, 88, 44, 10, "#6E747C", q)
    M.line(c, cx, yfundo, cx, yfundo + 150, Q.VIDRO, q, 18)
    M.rrect(c, cx - 70, yfundo + 46, 140, 30, 10, "#2A2B31", q)
    if divisa:
        M.line(c, cx + 130, yb_top, cx + 230, yb_top, E.COR, q, 5, dash=[10, 8])
    if 0 < u < 1:
        for k in range(5):
            uu = (t * 1.5 + k / 5) % 1
            E.bola(c, cx, yfundo + 160 + uu * 120, 8, baixo, q)
    return yb_top, yb_top - ht, yfundo


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def um():
        copo_barro(c, t, C["s01.a"], 1400, 900, 420, 560, C["s01.b"] - 0.4, 3.0)
        E.frase(c, t, C["s01.a"], [("água", "g", 110), ("barrenta", "g", 110, BARRO)], XE, 330, passo=0.14)
        E.frase(c, t, C["s01.a"] + 1.0, ps("parada em cima da mesa", "i", 60, TINTA2), XE, 440, passo=0.1)
        E.frase(c, t, C["s01.b"], ps("em uma hora: barro no fundo", "i", 62), XE, 600, passo=0.1)
        E.frase(c, t, C["s01.c"], ps("ninguém mexeu", "i", 62), XE, 720, passo=0.1)
        E.frase(c, t, C["s01.d"], ps("quem separou?", "i", 84, COR), XE, 900, passo=0.12)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t < C["s02"]:
        return
    tb = C["s02.a"] + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1540, 560, 280 * ease_back(prog(t, tb, 0.8)), giro=8 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 88), XE, 280, passo=0.14)
    lista(c, t, [(C["s02.b"], [("decantar,", "g", 70), ("filtrar,", "g", 70), ("centrifugar", "g", 70, COR)]),
                 (C["s02.c"], [("água", "g", 70), ("e", "i", 74), ("óleo", "g", 70, COR), ("sem", "i", 74), ("perder", "i", 74)])], XE, 470, 180)


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], ps("dois lembretes", "i", 80, TINTA2), XE, 220, passo=0.12)
    E.frase(c, t, C["s03.a"], [("mais", "g", 76, COR), ("denso", "g", 76, COR)] + ps("afunda, o menos denso fica em cima", "i", 66), XE, 420, passo=0.1)
    E.frase(c, t, C["s03.b"], ps("na mistura", "i", 70), XE, 640, passo=0.1)
    E.frase(c, t, C["s03.b"] + 0.6, [("heterogênea,", "g", 70, COR)] + ps("dá para ver as fases", "i", 70), XE + 340, 640, passo=0.1)
    E.foco(c, t, C["s03.c"], 0.5, lambda a: copo(c, t, C["s03.c"], 1450, 1000, 300, 280, 0.0, a=a))
    if t >= C["s03.c"]:
        r = copo(c, t, C["s03.c"], 1450, 1000, 300, 280, 0.75, OLEO)
        copo(c, t, C["s03.c"], 1450, 1000, 300, 280, 0.45, Q.AGUA)


# ---------------- decantação ----------------
def b_decantar(c, t, C, b):
    E.frase(c, t, C["s04.a"], ps("quem separou?", "i", 64, TINTA2), XE, 200, passo=0.1)
    E.frase(c, t, C["s04.a"] + 0.8, [("a", "i", 100), ("gravidade", "g", 100, COR)], XE, 330, passo=0.14)
    if t < C["s05"]:
        copo_barro(c, t, C["s04"], 1400, 900, 420, 560, C["s04.b"], 3.5)
        E.foco(c, t, C["s04.b"] + 0.5, 0.4, lambda a: (M.arrow(c, 1680, 520, 1680, 780, BARRO, a, 6, 22), E.escreve(c, "desce", 1710, 660, 44, "b", BARRO, a)))
    E.frase(c, t, C["s04.b"], ps("o barro é mais denso que a água", "i", 58), XE, 480, passo=0.08)
    E.frase(c, t, C["s04.c"], ps("deixar em repouso:", "i", 62), XE, 640, passo=0.1)
    E.frase(c, t, C["s04.c"] + 1.0, [("decantação", "g", 110, COR)], XE, 780)
    if t >= C["s05"]:
        inc = 28 * ease_io(prog(t, C["s05.a"], 1.0)) * (1 - ease_io(prog(t, C["s05.c"] - 0.5, 0.8)))
        c.save(); c.translate(1250, 640); c.rotate(inc); c.translate(-1250, -640)
        copo_barro(c, t, C["s04"], 1250, 900, 360, 480, C["s04"], 0.1, turvo=False, nivel=0.62 - 0.4 * ep(t, C["s05.a"] + 0.8, 1.5))
        c.restore()
        r = copo(c, t, C["s05.a"], 1700, 960, 280, 300, 0.6 * ep(t, C["s05.a"] + 0.8, 1.5))
        if C["s05.a"] + 0.8 <= t < C["s05.a"] + 2.3:
            for k in range(5):
                uu = (t * 1.5 + k / 5) % 1
                E.bola(c, lerp(1440, 1660, uu), lerp(470, 800, uu * uu), 9, Q.AGUA)
        E.foco(c, t, C["s05.b"], 0.4, lambda a: E.escreve(c, "o barro fica", 1080, 1010, 46, "b", BARRO, a))
        pilula_em(c, t, C["s05.c"], "heterogênea, uma parte mais densa", W / 2, 1040, 40, TINTA, "b")


# ---------------- filtração ----------------
def b_filtrar(c, t, C, b):
    if t < C["s07"]:
        def s06():
            E.frase(c, t, C["s06.a"], ps("mais rápido:", "i", 64, TINTA2), XE, 220, passo=0.1)
            E.frase(c, t, C["s06.a"] + 0.6, [("passe", "i", 80), ("num", "i", 80), ("filtro", "g", 80, COR)], XE, 340, passo=0.12)
            E.frase(c, t, C["s06.b"], ps("cheio de furos minúsculos", "i", 58), XE, 470, passo=0.08)
            E.frase(c, t, C["s06.c"], [("a", "i", 60), ("água", "g", 60), ("passa", "i", 60)], XE, 590, passo=0.1)
            E.frase(c, t, C["s06.d"], [("a", "i", 60), ("areia", "g", 60, BARRO), ("fica", "i", 60)], XE, 690, passo=0.1)
            E.frase(c, t, C["s06.e"], [("filtração", "g", 110, COR)], XE, 880)
            filtro(c, t, C["s06.a"], 1350, 300, tp=C["s06.c"], retido=ep(t, C["s06.d"], 1.2))
            copo(c, t, C["s06.a"], 1350, 1000, 300, 300, 0.5 * ep(t, C["s06.c"], 3.0))
            # o furo × o grão, ampliado
            if t >= C["s06.b"]:
                E.foco(c, t, C["s06.b"], 0.4, lambda a: (c.drawCircle(1720, 360, 110, M.paint(BR, 0.9 * a)), c.drawCircle(1720, 360, 110, M.paint("#2A2B31", a, stroke=10)),
                                                        M.rrect(c, 1640, 350, 160, 20, 6, "#C9C2B0", a),
                                                        [E.bola(c, 1660 + 40 * k, 360, 5, Q.AGUA, a) for k in range(4)],
                                                        E.bola(c, 1720, 320, 26, BARRO, a)))
        E.saida(c, t, C["s07"] - 0.1, s06)
        return
    E.frase(c, t, C["s07.a"], ps("todo dia:", "i", 64, TINTA2), XE, 240, passo=0.1)
    E.frase(c, t, C["s07.a"] + 0.6, [("o", "i", 90), ("coador", "g", 90, COR), ("de", "i", 90), ("café", "g", 90)], XE, 380, passo=0.12)
    filtro(c, t, C["s07.a"], 1400, 300, tp=C["s07.c"], retido=ep(t, C["s07.b"], 0.8))
    copo(c, t, C["s07.a"], 1400, 1000, 300, 300, 0.5 * ep(t, C["s07.c"], 2.0), "#6B3E1E")
    E.frase(c, t, C["s07.b"], [("o", "i", 60), ("pó", "g", 60, BARRO), ("fica", "i", 60)], XE, 540, passo=0.1)
    E.frase(c, t, C["s07.c"], [("o", "i", 60), ("café", "g", 60), ("passa", "i", 60)], XE, 640, passo=0.1)
    pilula_em(c, t, C["s07.d"], "separa por tamanho, não por densidade", 620, 860, 46, E.COR)


# ---------------- centrífuga ----------------
def b_centrifugar(c, t, C, b):
    E.frase(c, t, C["s08"], ps("partículas finas demais?", "i", 64, TINTA2), XE, 220, passo=0.1)
    E.frase(c, t, C["s08.a"], [("gire", "g", 90, COR), ("bem", "i", 90), ("rápido", "i", 90)], XE, 350, passo=0.12)
    vel = ep(t, C["s08.a"], 1.5) * (1 - ep(t, C["s09.a"], 1.5))
    ang = 0
    if t >= C["s08.a"]:
        t1 = min(t, C["s09.a"] + 1.5)
        ang = 600 * (t1 - C["s08.a"]) * 0.8
    if t < C["s09"]:
        centrifuga(c, t, C["s08.a"] - 0.3, 1380, 560, 300, gira=ang if vel > 0.01 else 0)
    E.frase(c, t, C["s08.b"], ps("o mais denso vai para o fundo do tubo", "i", 54), XE, 480, passo=0.08)
    E.frase(c, t, C["s08.c"], [("centrifugação", "g", 96, COR)], XE, 640)
    E.foco(c, t, C["s08.c"] + 1.0, 0.4, lambda a: E.escreve(c, "uma decantação acelerada", XE, 730, 54, "i", TINTA2, a))
    if t >= C["s09"]:
        E.foco(c, t, C["s09"], 0.5, lambda a: centrifuga(c, t, C["s09"], 1170, 640, 160, a, gira=ang if vel > 0.01 else 0))
        sep = ease_io(prog(t, C["s09.a"] + 0.8, 1.5))
        E.foco(c, t, C["s09.a"], 0.5, lambda a: tubo_sangue(c, 1480, 940, 560, sep, a))
        E.foco(c, t, C["s09.b"], 0.4, lambda a: (M.line(c, 1540, 860, 1580, 860, TINTA2, a, 3), E.escreve(c, "células", 1590, 860, 44, "b", "#9E1B22", a),
                                                E.escreve(c, "(mais densas)", 1590, 910, 40, "i", "#9E1B22", a)))
        E.foco(c, t, C["s09.c"], 0.4, lambda a: (M.line(c, 1540, 620, 1580, 620, TINTA2, a, 3), E.escreve(c, "plasma", 1590, 635, 44, "b", "#B8860B", a)))
        E.frase(c, t, C["s09.a"], ps("no laboratório: o sangue", "i", 54, TINTA2), XE, 880, passo=0.08)


# ---------------- funil ----------------
FX, FY = 1300, 260


def b_funil(c, t, C, b):
    E.frase(c, t, C["s10"], ps("dois líquidos que não se misturam", "i", 56, TINTA2), XE, 200, passo=0.08)
    E.frase(c, t, C["s10.a"], [("água", "g", 90), ("e", "i", 90), ("óleo", "g", 90, "#B8860B")], XE, 330, passo=0.12)
    E.frase(c, t, C["s10.b"], ps("o óleo, menos denso, fica em cima", "i", 54), XE, 450, passo=0.08)
    E.frase(c, t, C["s10.c"], [("funil", "g", 80, COR), ("de", "i", 80), ("decantação", "g", 80, COR)], XE, 600, passo=0.12)
    E.foco(c, t, C["s10.c"] + 1.4, 0.4, lambda a: E.escreve(c, "ou funil de separação", XE, 690, 50, "i", TINTA2, a))
    u = ease_io(prog(t, C["s11.b"] + 0.4, 3.0))
    r = funil_sep(c, t, C["s10.d"] - 0.3, FX, FY, Q.AGUA, OLEO, u, divisa=t >= C["s11.c"])
    copo(c, t, C["s10.d"] - 0.3, FX, 1040, 260, 220, 0.55 * u)
    if r:
        yd, yo, yf = r
        E.foco(c, t, C["s11.a"], 0.4, lambda a: (E.escreve(c, "óleo", FX + 200, yd - 40, 46, "b", "#B8860B", a), E.escreve(c, "água", FX + 200, yd + 60, 46, "b", TINTA2, a)))
        E.foco(c, t, C["s10.d"], 0.4, lambda a: E.escreve(c, "torneira", FX - 90 - E.larg("torneira", "b", 40), yf + 75, 40, "b", TINTA2, a))
    E.frase(c, t, C["s11.a"], ps("espere as camadas", "i", 54), XE, 800, passo=0.08)
    E.frase(c, t, C["s11.b"], [("abra:", "i", 58), ("sai", "i", 58), ("a", "i", 58), ("de", "i", 58), ("baixo", "g", 58, COR)], XE, 890, passo=0.1)
    E.frase(c, t, C["s11.c"], [("na", "i", 58), ("divisa,", "g", 58), ("feche", "i", 58)], XE, 980, passo=0.1)
    pilula_em(c, t, C["s11.d"], "o óleo fica no funil", 1700, 300, 44, TINTA)


# ---------------- atalho (palco) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    if t < C["s13"]:
        def arv():
            E.frase(c, t, C["s12"], ps("o atalho", "i", 70, CLARO), XE, 150, passo=0.12)
            E.frase(c, t, C["s12.a"], [("sólido", "g", 66, BR), ("no", "i", 66, CLARO), ("líquido?", "g", 66, BR)], XE, 280, passo=0.12)
            for k, (key, cond, met) in enumerate((("s12.b", "tem tempo", "decante"), ("s12.c", "quer rápido", "filtre"), ("s12.d", "fino demais", "centrifugue"))):
                y = 400 + 110 * k
                E.frase(c, t, C[key], [(cond, "i", 58, CLARO), ("→", "g", 58, CLARO), (met, "g", 58, E.CLARO)], XE + 80, y, passo=0.12)
            E.frase(c, t, C["s12.e"], [("dois", "g", 66, BR), ("líquidos", "g", 66, BR), ("que", "i", 66, CLARO), ("não", "i", 66, CLARO), ("se", "i", 66, CLARO), ("misturam?", "i", 66, CLARO)], XE, 790, passo=0.1)
            E.frase(c, t, C["s12.f"], [("funil:", "g", 62, E.CLARO)] + ps("sai primeiro o mais denso, o de baixo", "i", 62, BR), XE + 80, 910, passo=0.1)
        E.saida(c, t, C["s13"] - 0.1, arv)
        return
    E.frase(c, t, C["s13.a"], ps("os quatro usam a mesma coisa:", "i", 62, CLARO), W / 2, 280, "center", 0.1)
    E.frase(c, t, C["s13.a"] + 1.4, [("mistura", "g", 80, BR), ("heterogênea", "g", 80, E.CLARO)], W / 2, 420, "center", 0.12)
    E.foco(c, t, C["s13.a"] + 2.4, 0.4, lambda a: centro(c, "às vezes só no microscópio, como no sangue", W / 2, 510, 46, "i", CLARO, a))
    E.frase(c, t, C["s13.b"], [("não", "g", 66, ERRADO), ("separam", "i", 70, CLARO), ("mistura", "g", 66, BR), ("homogênea", "g", 66, BR)], W / 2, 700, "center", 0.12)
    pilula_em(c, t, C["s13.c"], "para essas: destilação, próxima aula", W / 2, 860, 48, E.COR)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s14"], [("cuidado", "g", 96, ERRADO)], XE, 190)
    riscado(c, t, C["s14.a"], "filtrar a água do mar para tirar o sal", XE, 340, 56)
    filtro(c, t, C["s14.a"] + 0.4, 1400, 300, tp=C["s15.a"])
    copo(c, t, C["s14.a"] + 0.4, 1400, 1000, 300, 300, 0.5 * ep(t, C["s15.a"], 2.5), "#9FD3E6")
    E.frase(c, t, C["s14.b"], [("não", "g", 80, ERRADO), ("dá", "i", 80)], XE, 500, passo=0.12)
    E.frase(c, t, C["s14.c"], ps("o sal está dissolvido:", "i", 58), XE, 640, passo=0.08)
    E.frase(c, t, C["s14.c"] + 1.2, ps("partículas menores que qualquer furo", "i", 58), XE, 730, passo=0.08)
    E.foco(c, t, C["s15.b"], 0.4, lambda a: E.escreve(c, "sai tão salgada quanto entrou", 1140, 1060, 46, "b", TINTA2, a))
    pilula_em(c, t, C["s15.c"], "o filtro só segura o que não está dissolvido", 660, 900, 42, E.COR)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s16"], ps("hora de testar", "i", 72, COR), XE, 180)
    E.frase(c, t, C["s16.a"], [("água:", "g", 60), ("1", "g", 60, COR), ("g/cm³", "b", 52, TINTA2)], XE, 330, passo=0.1)
    E.frase(c, t, C["s16.b"], [("óleo:", "g", 60, "#B8860B"), ("0,9", "g", 60, COR), ("g/cm³", "b", 52, TINTA2)], XE, 430, passo=0.1)
    E.frase(c, t, C["s16.c"], [("1", "g", 60, COR)] + ps("qual sai primeiro?", "i", 64), XE, 580, passo=0.1)
    E.frase(c, t, C["s16.d"], [("2", "g", 60, COR)] + ps("e se o outro tiver densidade 1,5?", "i", 64), XE, 720, passo=0.1)
    if t < C["s17"]:
        funil_sep(c, t, C["s16.a"], 1450, 260, Q.AGUA, OLEO)
    else:
        E.relogio(c, t, C["s17.a"], cx=1470, cy=470, r=200)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    u1 = ease_io(prog(t, C["s18.b"], 2.0))
    r = funil_sep(c, t, C["s18"], 620, 240, Q.AGUA, OLEO, u1, divisa=True)
    copo(c, t, C["s18"], 620, 1020, 240, 200, 0.55 * u1)
    if r:
        E.foco(c, t, C["s18.a"], 0.4, lambda a: (E.escreve(c, "0,9", 800, r[0] - 40, 46, "b", "#B8860B", a), E.escreve(c, "1", 800, r[0] + 60, 46, "b", TINTA2, a)))
    E.foco(c, t, C["s18.b"], 0.4, lambda a: E.escreve(c, "sai a água", 380, 120, 56, "g", COR, a))
    if t >= C["s19"]:
        u2 = ease_io(prog(t, C["s19.c"], 2.0))
        r2 = funil_sep(c, t, C["s19"], 1350, 240, DENSO, Q.AGUA, u2, divisa=True)
        copo(c, t, C["s19"], 1350, 1020, 240, 200, 0.55 * u2, DENSO)
        if r2:
            E.foco(c, t, C["s19.a"], 0.4, lambda a: (E.escreve(c, "1", 1530, r2[0] - 40, 46, "b", TINTA2, a), E.escreve(c, "1,5", 1530, r2[0] + 60, 46, "b", "#4A5FA8", a)))
        E.foco(c, t, C["s19.c"], 0.4, lambda a: E.escreve(c, "sai o outro", 1110, 120, 56, "g", COR, a))
        riscado(c, t, C["s19.d"], "sempre sai a água", 820, 960, 48)
        pilula_em(c, t, C["s19.e"], "sai o mais denso", W / 2, 1050, 50, E.COR)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s20"], [("resumindo", "i", 92, COR)], W / 2, 180, "center")
        itens = (("s20.a", [("decantar:", "g", 64), ("esperar", "i", 68), ("o", "i", 68), ("denso", "g", 64, COR), ("descer", "i", 68)]),
                 ("s20.b", [("filtrar:", "g", 64), ("reter", "i", 68), ("o", "i", 68), ("grão", "g", 64, COR), ("maior", "i", 68)]),
                 ("s20.c", [("centrifugar:", "g", 64), ("decantar", "i", 68), ("com", "i", 68), ("pressa", "g", 64, COR)]),
                 ("s20.d", [("funil:", "g", 64), ("sai", "i", 68), ("o", "i", 68), ("mais", "g", 64, COR), ("denso", "g", 64, COR)]))
        for i, (k, partes) in enumerate(itens):
            y = 350 + i * 170
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 300, y - 26, 52, a=a), centro(c, str(i + 1), 300, y - 4, 60, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, partes, 400, y, passo=0.12)
    E.saida(c, t, C["s21"] - 0.1, resumo)
    if t < C["s21"]:
        return
    E.frase(c, t, C["s21"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C["s21.a"], [("Destilação", "g", 110, COR)], XE, 400)
    E.frase(c, t, C["s21.a"] + 0.6, ps("simples e fracionada", "i", 80), XE, 520, passo=0.12)
    E.foco(c, t, C["s21.b"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1560, 420, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s21.b"] + 0.3, 0.8))
    E.cursor(c, lerp(1860, 1690, p), lerp(720, 445, p), ep(t, C["s21.b"] + 0.2, 0.4))
    E.frase(c, t, C["s21.c"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1560, 990, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, decantar=b_decantar, filtrar=b_filtrar, centrifugar=b_centrifugar, funil=b_funil,
              atalho=b_atalho, erro=b_erro, questao=b_questao, resposta=b_resposta, fim=b_fim)
