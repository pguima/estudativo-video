"""Visual — Estudativo · MAT-CNT-016: eventos independentes, multiplicar as chances.
Mesma linguagem da trilha Contagem e Probabilidade (MAT-CNT-001 a 015): igual_bola() com o resultado na esfera, dado() e saco()/bolas()
da MAT-CNT-011, moedas Ca/Co da MAT-CNT-013 (E.moeda), linha() com contas e frações numa linha (MAT-CNT-013).
Peças desta aula:
- grade26(): a grade moeda × dado (2 linhas, cara e coroa; 6 colunas, as faces), no molde da tabela 6 × 6 da MAT-CNT-012:
  cada casa acende numa cor no instante da fala, e o véu de papel cobre a linha que a pista tira da conta.
- semaforo(): semáforo com a luz verde acesa.
- metade(): o retângulo do inteiro, metade pintada e a metade cortada em sextos (um sexto de um meio).
Sem voz ainda: todo instante vem de C[...] (cenas e marcadores), nunca de segundos fixos."""
import math
from fractions import Fraction as Fr
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Contagem e Probabilidade")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-CNT-016_eventos_independentes.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("tabela", "regra", "dependentes", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
PAPEL = "#F3F3F0"
AZUL, VERM = "#3D7DD8", "#D94B3D"
assert 2 * 6 == 12 and Fr(1, 2) * Fr(1, 6) == Fr(1, 12) and 8 < 100 / 12 < 9
assert Fr(22, 40) * 100 == 55 and Fr(10, 16) * 100 == Fr(125, 2) and Fr(2, 3) * Fr(5, 7) == Fr(10, 21)
assert Fr(1, 2) ** 3 == Fr(1, 8) and Fr(1, 2) ** 6 == Fr(1, 64)
assert Fr(2, 5) * Fr(1, 3) == Fr(2, 15) and 2 * 1 == 2 and 5 * 3 == 15 and 13 < 200 / 15 < 14


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças da trilha (MAT-CNT-002 a 015) ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    """uma frase, palavra a palavra, no mesmo estilo"""
    return [(w, est, size, cor) for w in txt.split()]


def igual_bola(c, t, t0, x, y, txt, r=120, size=None, cor=None, escuro=False, t_igual=None):
    """'=' em x e o resultado numa esfera à direita; y = centro. Devolve o centro da esfera."""
    size = size or r * (0.72 if len(txt) <= 2 else 0.56 if len(txt) == 3 else 0.46 if len(txt) == 4 else 0.38)
    E.sinal(c, t, t0 - 0.2 if t_igual is None else t_igual, "=", x, y, r * 0.75, BR if escuro else TINTA)
    bx = x + r * 0.55 + r
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, bx, y, r, cor, a), centro(c, txt, bx, y + size * 0.36, size, "g", E.SOBRE, a)))
    return bx


def nota(c, t, t0, x, y, txt, size=46, cor=TINTA2, estilo="b"):
    E.foco(c, t, t0, 0.45, lambda a: centro(c, txt, x, y, size, estilo, cor, a))


def larg_parte(p, size):
    return E.larg(p, "g", size) if isinstance(p, str) else max(E.larg(str(p[0]), "g", size), E.larg(str(p[1]), "g", size)) + size * 0.2


def linha(c, t, x, y, size, partes, align="left", gap=None):
    """conta numa linha: partes = [(texto ou (n, d), instante[, cor])]; y = altura da barra das frações. Devolve o x de cada parte e o fim"""
    gap = size * 0.28 if gap is None else gap
    ws = [larg_parte(p[0], size) for p in partes]
    tot = sum(ws) + gap * (len(partes) - 1)
    xx = x - tot / 2 if align == "center" else x - tot if align == "right" else x
    xs = []
    for (p, t0, *cor), w in zip(partes, ws):
        cor = cor[0] if cor else TINTA
        xs.append(xx)
        if isinstance(p, str):
            E.foco(c, t, t0, 0.45, lambda a, p=p, xx=xx, cor=cor: E.escreve(c, p, xx, y + size * 0.34, size, "g", cor, a))
        else:
            E.fr(c, t, t0, p[0], p[1], xx + w / 2, y, size, cor)
        xx += w + gap
    return xs, xx - gap


def pil_esq(c, t, t0, x, y, txt, size=46, fundo=None, cor=BR):
    """pílula com a borda esquerda em x"""
    w = E.larg(txt, "g", size) + size * 1.1
    E.foco(c, t, t0, 0.45, lambda a: E.pilula(c, txt, x + w / 2, y, size, estilo="g", fundo=fundo or TINTA2, cor=cor, a=a))


PINTAS = {1: [(0, 0)], 2: [(-1, -1), (1, 1)], 3: [(-1, -1), (0, 0), (1, 1)], 4: [(-1, -1), (1, -1), (-1, 1), (1, 1)],
          5: [(-1, -1), (1, -1), (0, 0), (-1, 1), (1, 1)], 6: [(-1, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (1, 1)]}


def dado(c, cx, cy, s, n, a=1.0, cor=None, fundo=BR, borda=None, sombra=True):
    """face de dado com as pintas (MAT-CNT-011)"""
    if a <= 0:
        return
    r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - s / 2, cy - s / 2, s, s), s * 0.2, s * 0.2)
    if sombra:
        sh = skia.Paint(AntiAlias=True, Color=M.hexc("#000000", 0.12 * a))
        sh.setMaskFilter(skia.MaskFilter.MakeBlur(skia.kNormal_BlurStyle, 8))
        c.save(); c.translate(0, 6); c.drawRRect(r, sh); c.restore()
    c.drawRRect(r, M.paint(fundo, a))
    c.drawRRect(r, M.paint(borda or (TINTA if fundo == BR else M.mix(fundo, "#000000", 0.35)), a, stroke=max(3, s * 0.035)))
    k = s * 0.27
    for dx, dy in PINTAS[n]:
        c.drawCircle(cx + dx * k, cy + dy * k, s * 0.085, M.paint(cor or (TINTA if fundo == BR else BR), a))


def moeda(c, cx, cy, r, face, a=1.0, escuro=False):
    """moeda da MAT-CNT-013: Ca na cor da matéria, Co em cinza"""
    E.moeda(c, cx, cy, r, face, a, E.COR if face == "Ca" else (CINZA if escuro else TINTA2))


def saco(c, cx, cy, w, h, a=1.0):
    """saco de pano visto de frente (MAT-CNT-011)"""
    if a <= 0:
        return
    p = skia.Path()
    p.moveTo(cx - w * 0.22, cy - h * 0.5)
    p.cubicTo(cx - w * 0.62, cy - h * 0.3, cx - w * 0.58, cy + h * 0.5, cx, cy + h * 0.5)
    p.cubicTo(cx + w * 0.58, cy + h * 0.5, cx + w * 0.62, cy - h * 0.3, cx + w * 0.22, cy - h * 0.5)
    p.close()
    c.drawPath(p, M.paint("#E9DCC4", a))
    c.drawPath(p, M.paint("#8C7A5B", a, stroke=6))
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w * 0.26, cy - h * 0.56, w * 0.52, h * 0.08), 12, 12), M.paint("#8C7A5B", a))


# ---------------- peças desta aula ----------------
def grade26(c, t, t0, x, y, cel, tl=None, tc=None, pinta=None, veu=None):
    """grade moeda × dado: (x, y) = canto de cima à esquerda; linhas = cara e coroa, colunas = faces 1 a 6.
    pinta = {(linha, face): (t0, cor, texto)}; veu = (t0, linha que fica). Devolve (linha, face) → centro"""
    centro_ = lambda i, v: (x + (v - 0.5) * cel, y + (i + 0.5) * cel)

    def grade(a):
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, 6 * cel, 2 * cel), 16, 16), M.paint(BR, 0.85 * a))
        for i in range(7):
            M.line(c, x + i * cel, y, x + i * cel, y + 2 * cel, TINTA2, a * 0.5, 2.5)
        for i in range(3):
            M.line(c, x, y + i * cel, x + 6 * cel, y + i * cel, TINTA2, a * 0.5, 2.5)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, 6 * cel, 2 * cel), 16, 16), M.paint(TINTA, a, stroke=4))
    E.foco(c, t, t0, 0.5, grade)
    for i, f in enumerate(("Ca", "Co")):
        E.foco(c, t, (tl[i] if tl else t0) , 0.4, lambda a, i=i, f=f: moeda(c, x - cel * 0.62, y + (i + 0.5) * cel, cel * 0.36, f, a))
    for v in range(1, 7):
        E.foco(c, t, (tc if tc is not None else t0) + 0.08 * v, 0.4, lambda a, v=v: dado(c, x + (v - 0.5) * cel, y - cel * 0.62, cel * 0.66, v, a))
    for (i, v), (tp, cor, txt) in (pinta or {}).items():
        cx, cy = centro_(i, v)

        def cheia(a, cx=cx, cy=cy, cor=cor, txt=txt):
            m = cel * 0.08
            c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - cel / 2 + m, cy - cel / 2 + m, cel - 2 * m, cel - 2 * m), 10, 10), M.paint(cor, a))
            if txt:
                centro(c, txt, cx, cy + cel * 0.13, cel * 0.36, "g", BR, a)
        E.foco(c, t, tp, 0.35, cheia, sobe=4)
    if veu and t >= veu[0]:
        q = ep(t, veu[0], 0.5)
        for i in range(2):
            if i != veu[1]:
                c.drawRect(skia.Rect.MakeXYWH(x + 2, y + i * cel + 2, 6 * cel - 4, cel - 4), M.paint(PAPEL, 0.85 * q))
                M.line(c, x - cel * 0.62 - cel * 0.45, y + (i + 0.5) * cel, x - cel * 0.62 + cel * 0.45, y + (i + 0.5) * cel, ERRADO, q, 8)
    return centro_


def semaforo(c, cx, cy, h, a=1.0, verde=True):
    """semáforo de três luzes, com a verde acesa"""
    if a <= 0:
        return
    w = h * 0.38
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2, cy - h / 2, w, h), w * 0.3, w * 0.3), M.paint("#22232A", a))
    for k, cor in enumerate(("#E5484D", "#F2B01E", "#16A36A")):
        acesa = verde and k == 2
        c.drawCircle(cx, cy - h * 0.3 + k * h * 0.3, w * 0.32, M.paint(cor if acesa else M.mix(cor, "#22232A", 0.75), a))
    c.drawRect(skia.Rect.MakeXYWH(cx - w * 0.08, cy + h / 2, w * 0.16, h * 0.35), M.paint("#22232A", a))


def metade(c, t, x, y, w, h, ta, tb, tc_=None):
    """o inteiro: em ta a metade da esquerda (cara) se pinta; em tb ela se corta em sextos e um sexto acende"""
    def casco(a):
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 14, 14), M.paint(BR, a))
    E.foco(c, t, ta - 0.5, 0.45, casco)
    if t >= ta:
        q = ep(t, ta, 0.6)
        c.drawRect(skia.Rect.MakeXYWH(x, y, w / 2 * q, h), M.paint(E.COR, 0.22))
        if q > 0.99:
            M.line(c, x + w / 2, y, x + w / 2, y + h, TINTA, 1, 5)
    if t >= tb:
        lp = w / 12
        for k in range(1, 6):
            q = ep(t, tb + 0.08 * k, 0.4)
            M.line(c, x + k * lp, y, x + k * lp, y + h * q, TINTA2, 0.8, 3)
        q = ep(t, tb + 0.7, 0.4)
        c.drawRect(skia.Rect.MakeXYWH(x + 5 * lp, y, lp, h), M.paint(E.COR, q))
    if tc_ is not None and t >= tc_:
        lp = w / 12
        for k in range(7, 12):
            q = ep(t, tc_ + 0.05 * k, 0.4)
            M.line(c, x + k * lp, y, x + k * lp, y + h * q, FIO, 1, 3)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 14, 14), M.paint(TINTA, ep(t, ta - 0.5, 0.45), stroke=4))


def fracao_partes(c, t, cx, y, size, cima, baixo, tcima, tbaixo, cor=None):
    """fração cujo de cima e o de baixo entram em instantes diferentes; y = barra"""
    w = max(E.larg(cima, "g", size), E.larg(baixo, "g", size)) + size * 0.3
    E.foco(c, t, min(tcima, tbaixo), 0.45, lambda a: c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2, y - size * 0.045, w, size * 0.09), 4, 4),
                                                                 M.paint(TINTA, a)))
    E.foco(c, t, tcima, 0.45, lambda a: centro(c, cima, cx, y - size * 0.2, size, "g", cor or TINTA, a))
    E.foco(c, t, tbaixo, 0.45, lambda a: centro(c, baixo, cx, y + size * 0.9, size, "g", cor or TINTA, a))
    return w


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def pergunta():
        for i in range(5):
            E.foco(c, t, C["s01.a"] + 0.25 * i, 0.4, lambda a, i=i: moeda(c, 260 + i * 200, 360, 80, "Ca", a))
        E.foco(c, t, C["s01.a"] + 0.2, 0.45, lambda a: E.escreve(c, "5 caras seguidas", 180, 520, 60, "i", TINTA2, a))
        E.foco(c, t, C["s01.b"], 0.45, lambda a: (c.drawCircle(1340, 360, 80, M.paint(BR, a)), c.drawCircle(1340, 360, 80, M.paint(TINTA2, a, stroke=5)),
                                                  centro(c, "?", 1340, 395, 100, "g", TINTA2, a)))
        E.foco(c, t, C["s01.b"] + 0.3, 0.45, lambda a: E.centro(c, "6ª jogada", 1340, 520, 52, "b", TINTA2, a))
        E.frase(c, t, C["s01.b"] + 0.2, [("coroa", "g", 80, COR), ("ficou", "i", 76), ("mais", "i", 76), ("provável?", "i", 76)], W / 2, 690, "center", passo=0.12)
        xs, xf = linha(c, t, W / 2, 820, 100, [("P(coroa) =", C["s01.c"]), ((1, 2), C["s01.c"] + 0.2, CERTO)], "center")
        E.foco(c, t, C["s01.d"], 0.5, lambda a: E.pilula(c, "a moeda não tem memória", W / 2, 1010, 50, estilo="g", a=a))
    E.saida(c, t, C["s02"] - 0.1, pergunta)

    if t >= C["s02"]:
        E.foco(c, t, C["s02.c"] - 0.2, 0.7, lambda a: E.bola(c, 1480, 520, 300 * ease_back(prog(t, C["s02.c"] - 0.2, 0.7))), blur=0)
        E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 96), XE, 300)
        E.frase(c, t, C["s02.a"] + 0.9, [("eventos", "g", 116, COR)], XE, 450)
        E.frase(c, t, C["s02.a"] + 1.3, [("independentes", "g", 116, COR)], XE, 600)
        pil_esq(c, t, C["s02.b"], XE, 760, "a chance de ambos", 50)
        E.foco(c, t, C["s02.c"] + 0.2, 0.5, lambda a: (E.centro(c, "+ atalho", 1480, 490, 88, "g", BR, a),
                                                      E.centro(c, "de prova", 1480, 600, 88, "g", BR, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"] + 0.1, [("você", "i", 84), ("vai", "i", 84), ("usar", "i", 84), ("duas", "g", 88, COR), ("coisas", "i", 84)], W / 2, 190, "center")
    for k, x, titulo in (("s03.b", 200, "condicional"), ("s03.c", 1000, "multiplicar frações")):
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, 290, 720, 620, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(titulo, "g", 64, COR)], x + 360, 400, "center")
    E.foco(c, t, C["s03.b"] + 0.5, 0.45, lambda a: E.pilula(c, "a pista vira", 560, 590, 56, estilo="g", a=a))
    E.foco(c, t, C["s03.b"] + 0.8, 0.45, lambda a: E.pilula(c, "o novo total", 560, 700, 56, estilo="g", a=a))
    xs, xf = linha(c, t, 1360, 620, 84, [((2, 3), C["s03.c"] + 0.5), ("×", C["s03.c"] + 0.7), ((5, 7), C["s03.c"] + 0.9), ("=", C["s03.c"] + 1.3),
                                          ((10, 21), C["s03.c"] + 1.5, COR)], "center")
    nota(c, t, C["s03.c"] + 2.0, 1360, 820, "em cima × em cima", 44, TINTA2, "i")
    nota(c, t, C["s03.c"] + 2.4, 1360, 875, "embaixo × embaixo", 44, TINTA2, "i")
    E.frase(c, t, lerp(C["s03.c"], C["s03.end"], 0.8), ps("faltou alguma? procure no canal", "i", 52, TINTA2), W / 2, 1010, "center", passo=0.1)


# ---------------- moeda e dado ----------------
GX, GY, GC = 260, 420, 140


def b_tabela(c, t, C, b):
    E.frase(c, t, C["s04.a"], [("1", "g", 80, COR), ("moeda", "i", 76), ("e", "i", 76), ("1", "g", 80, COR), ("dado", "i", 76)], GX + 3 * GC, 170, "center")
    pinta = {(i, v): (C["s04.e"] + 0.04 * (i * 6 + v), "#E6E4F5", None) for i in range(2) for v in range(1, 7)}
    f = grade26(c, t, C["s04.c"], GX, GY, GC, tl=[C["s04.c"], C["s04.c"] + 0.5], tc=C["s04.d"], pinta=pinta)
    cx, cy = f(0, 6)
    m = GC * 0.08
    E.foco(c, t, C["s05.a"], 0.35, lambda a: c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - GC / 2 + m, cy - GC / 2 + m, GC - 2 * m, GC - 2 * m), 10, 10),
                                                         M.paint(E.COR, a)), sobe=4)
    grade26(c, t, 1e9, GX, GY, GC, veu=(C["s06.a"], 0)) if t >= C["s06.a"] else None
    XP = 1250

    def p4():
        E.frase(c, t, C["s04.b"], [("cara", "g", 76, COR), ("e", "i", 72), ("6?", "g", 76, COR)], XP, 330, passo=0.12)
        E.formula_em(c, t, C["s04.e"], "2 × 6 = 12", XP, 520, 84, "g", TINTA)
        nota(c, t, C["s04.e"] + 0.5, XP + 200, 600, "casas", 50, TINTA2, "i")
    E.saida(c, t, C["s05"] - 0.1, p4)
    if C["s05"] <= t < C["s06"]:
        def p5():
            E.foco(c, t, C["s05.a"], 0.45, lambda a: E.escreve(c, "1 casa: cara e 6", XP, 330, 60, "g", COR, a))
            xs, xf = linha(c, t, XP, 520, 96, [("P =", C["s05.b"]), ((1, 12), C["s05.b"] + 0.2, COR)])
            nota(c, t, C["s05.b"] + 0.8, XP + 260, 690, "pouco mais de 8%", 48, TINTA2, "i")
        E.saida(c, t, C["s06"] - 0.1, p5)
    if t < C["s06"]:
        return
    E.foco(c, t, C["s06"] + 0.3, 0.45, lambda a: E.pilula(c, "pista: deu cara", XP + 230, 300, 48, estilo="g", fundo=TINTA2, a=a))
    E.foco(c, t, C["s06.a"], 0.45, lambda a: (E.escreve(c, "novo total:", XP, 430, 56, "i", TINTA, a), E.escreve(c, "6", XP + 320, 432, 72, "g", COR, a)))
    linha(c, t, XP, 580, 72, [("com pista:", C["s06.b"] - 0.3), ((1, 6), C["s06.b"], COR)])
    linha(c, t, XP, 760, 72, [("sem pista:", C["s06.c"] - 0.3), ((1, 6), C["s06.c"], COR)])
    E.foco(c, t, C["s06.d"], 0.5, lambda a: E.pilula(c, "a pista não mudou nada", W / 2, 960, 56, estilo="g", fundo=CERTO, a=a))


# ---------------- regra ----------------
def b_regra(c, t, C, b):
    def regra():
        E.frase(c, t, C["s07.a"], ps("saber de um não muda a chance do outro", "i", 60, TINTA2), W / 2, 200, "center", passo=0.08)
        E.foco(c, t, C["s07.b"], 0.5, lambda a: E.pilula(c, "independentes", W / 2, 340, 72, estilo="g", a=a))
        E.foco(c, t, C["s07.c"], 0.5, lambda a: E.centro(c, "P(A e B) = P(A) × P(B)", W / 2, 580, 100, "g", TINTA, a))
        linha(c, t, W / 2, 790, 100, [((1, 2), C["s07.d"]), ("×", C["s07.d"] + 0.3), ((1, 6), C["s07.d"] + 0.5), ("=", C["s07.d"] + 0.9),
                                      ((1, 12), C["s07.d"] + 1.1, COR)], "center")
        nota(c, t, C["s07.d"] + 2.0, W / 2, 990, "o mesmo da tabela, sem desenhar nada", 48, TINTA2, "i")
    E.saida(c, t, C["s08"] - 0.1, regra)
    if t < C["s08"]:
        return
    E.frase(c, t, C["s08"] + 0.1, [("por", "i", 80), ("que", "i", 80), ("vezes?", "g", 88, COR)], W / 2, 190, "center")
    x, y, w, h = 360, 330, 1200, 180
    metade(c, t, x, y, w, h, C["s08.a"], C["s08.b"], C["s08.c"] + 2.4)
    nota(c, t, C["s08.a"] + 0.3, x + w / 4, y + h + 70, "metade tem cara", 50, COR)
    nota(c, t, C["s08.b"] + 0.9, x + w * 5.5 / 12, y - 30, "1/6 da metade", 46, COR)
    linha(c, t, W / 2, 800, 100, [((1, 6), C["s08.c"]), ("de", C["s08.c"] + 0.3), ((1, 2), C["s08.c"] + 0.5), ("=", C["s08.c"] + 1.2),
                                  ((1, 6), C["s08.c"] + 1.4), ("×", C["s08.c"] + 1.6), ((1, 2), C["s08.c"] + 1.8), ("=", C["s08.c"] + 2.2),
                                  ((1, 12), C["s08.c"] + 2.4, COR)], "center")
    nota(c, t, C["s08.c"] + 3.0, W / 2, 1000, "como nas frações: “de” vira vezes", 48, TINTA2, "i")


# ---------------- dependentes ----------------
def b_dependentes(c, t, C, b):
    def turma():
        E.frase(c, t, C["s09"] + 0.1, ps("a turma da aula anterior", "i", 64, TINTA2), XE, 200, passo=0.1)
        E.frase(c, t, C["s09.a"], [("22", "g", 84, COR), ("mulheres", "i", 76), ("em", "i", 76), ("40", "g", 84), ("alunos", "i", 76)], XE, 330, passo=0.12)
        E.foco(c, t, C["s09.b"] - 0.4, 0.45, lambda a: E.escreve(c, "sem pista", XE, 480, 50, "b", TINTA2, a))
        xs, xf = linha(c, t, XE, 590, 84, [("P(mulher) =", C["s09.b"]), ((22, 40), C["s09.b"] + 0.3), ("= 55%", C["s09.b"] + 0.8, COR)])
        E.foco(c, t, C["s09.c"] - 0.4, 0.45, lambda a: E.escreve(c, "sabendo que usa óculos", XE, 760, 50, "b", TINTA2, a))
        xs, xf = linha(c, t, XE, 870, 84, [("P(mulher | óculos) =", C["s09.c"]), ((10, 16), C["s09.c"] + 0.3), ("= 62,5%", C["s09.c"] + 0.8, COR)])
        E.foco(c, t, C["s09.c"] + 1.4, 0.45, lambda a: E.pilula(c, "subiu", xf + 120, 870, 50, estilo="g", fundo=TINTA2, a=a))
    E.saida(c, t, C["s10"] - 0.1, turma)
    if t < C["s10"]:
        return
    E.foco(c, t, C["s10.a"], 0.5, lambda a: E.pilula(c, "a pista mudou a chance: dependentes", W / 2, 180, 52, estilo="g", fundo=ERRADO, a=a))
    nota(c, t, C["s10.a"] + 1.5, W / 2, 280, "não basta multiplicar", 50, ERRADO, "i")
    E.frase(c, t, C["s10.b"], [("o", "i", 70), ("teste:", "g", 76, COR), ("chance", "i", 70), ("com", "g", 76), ("a", "i", 70), ("pista", "i", 70), ("=", "g", 76),
                               ("chance", "i", 70), ("sem", "g", 76), ("a", "i", 70), ("pista?", "i", 70)], W / 2, 450, "center", passo=0.08)
    E.foco(c, t, C["s10.c"], 0.5, lambda a: (E.selo(c, 420, 620, 50, True, a), E.escreve(c, "igual: independentes, multiplique", 500, 640, 60, "g", CERTO, a)))
    E.foco(c, t, C["s10.d"], 0.5, lambda a: (E.selo(c, 420, 760, 50, False, a), E.escreve(c, "diferente: dependentes", 500, 780, 60, "g", ERRADO, a)))
    nota(c, t, lerp(C["s10.d"], C["s10.end"], 0.15), W / 2, 920, "moedas, dados, coisas sem ligação: já são independentes", 46, TINTA2, "i")
    nota(c, t, lerp(C["s10.d"], C["s10.end"], 0.65), W / 2, 1000, "na dúvida, faça a conta antes de decidir", 46, COR)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s11"] + 0.1, [("cuidado", "g", 90, ERRADO), ("com", "i", 84), ("isto", "i", 84)], W / 2, 160, "center")
    for i in range(5):
        E.foco(c, t, C["s11"] + 0.4 + 0.1 * i, 0.4, lambda a, i=i: moeda(c, 260 + i * 190, 360, 75, "Ca", a))
    E.foco(c, t, C["s11"] + 0.9, 0.45, lambda a: (c.drawCircle(1290, 360, 75, M.paint(BR, a)), c.drawCircle(1290, 360, 75, M.paint(TINTA2, a, stroke=5)),
                                                  centro(c, "?", 1290, 393, 96, "g", TINTA2, a)))
    E.foco(c, t, C["s11.a"], 0.5, lambda a: E.pilula(c, "“a coroa está devendo”", W / 2, 560, 60, estilo="g", fundo=ERRADO, a=a))
    if t >= C["s11.b"]:
        w = E.larg("“a coroa está devendo”", "g", 60) + 66
        E.risco(c, W / 2 - w / 2, 560, W / 2 + w / 2, 560, t, C["s11.b"], TINTA, 10)
    E.frase(c, t, C["s11.b"] + 0.3, [("cada", "i", 64), ("jogada", "i", 64), ("é", "i", 64), ("independente", "g", 70, COR)], W / 2, 720, "center", passo=0.1)
    nota(c, t, lerp(C["s11.b"], C["s11.c"], 0.5), W / 2, 800, "a moeda não sabe o que saiu antes", 48, TINTA2, "i")
    linha(c, t, W / 2, 930, 84, [("6ª:  P(cara) =", C["s11.c"]), ((1, 2), C["s11.c"] + 0.2, CERTO), ("  P(coroa) =", C["s11.c"] + 0.6), ((1, 2), C["s11.c"] + 0.8, CERTO)],
          "center")


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def tres():
        E.frase(c, t, C["s12.a"], [("a", "i", 72, CLARO), ("mesma", "i", 72, CLARO), ("chance", "g", 78, BR), ("repetida", "i", 72, CLARO), ("vira", "i", 72, CLARO),
                                   ("potência", "g", 78, BR)], W / 2, 200, "center", passo=0.1)
        for i in range(3):
            E.foco(c, t, C["s12.b"] + 0.2 * i, 0.4, lambda a, i=i: moeda(c, 760 + i * 200, 400, 80, "Ca", a, True))
        linha(c, t, W / 2, 640, 100, [((1, 2), C["s12.c"], BR), ("×", C["s12.c"] + 0.3, CLARO), ((1, 2), C["s12.c"] + 0.5, BR), ("×", C["s12.c"] + 0.8, CLARO),
                                      ((1, 2), C["s12.c"] + 1.0, BR)], "center")
        wp = E.formula(None, "= (f{1}{2})^3", 0, 0, 100, "g", a=0)
        E.formula_em(c, t, C["s12.d"], "= (f{1}{2})^3", 700, 920, 100, "g", BR)
        E.foco(c, t, C["s12.d"] + 1.6, 0.5, lambda a: (E.escreve(c, "=", 700 + wp + 40, 905, 100, "g", BR, a), E.fracao(c, 1, 8, 700 + wp + 180, 870, 100, CLARO, a)))
    E.saida(c, t, C["s13"] - 0.1, tres)
    if C["s13"] <= t < C["s14"]:
        def seis():
            E.frase(c, t, C["s13.a"], ps("potência é multiplicação repetida", "i", 64, CLARO), W / 2, 200, "center", passo=0.1)
            for i in range(6):
                E.foco(c, t, C["s13.b"] + 0.12 * i, 0.4, lambda a, i=i: moeda(c, 460 + i * 200, 380, 70, "Ca", a, True))
            nota(c, t, C["s13.b"] + 0.8, W / 2, 510, "vistas antes de começar", 46, CLARO, "i")
            wp = E.formula(None, "(f{1}{2})^6 =", 0, 0, 96, "g", a=0)
            E.formula_em(c, t, C["s13.c"] - 0.6, "(f{1}{2})^6 =", 640, 720, 96, "g", BR)
            E.foco(c, t, C["s13.c"], 0.5, lambda a: E.fracao(c, 1, 64, 640 + wp + 110, 685, 96, CLARO, a))
            nota(c, t, C["s13.c"] + 1.0, 1400, 715, "é raro", 60, CLARO, "i")
            E.foco(c, t, C["s13.d"], 0.5, lambda a: E.pilula(c, "5 caras já na mesa? falta 1 jogada: 1/2", W / 2, 950, 50, estilo="g", fundo=E.COR, a=a))
        E.saida(c, t, C["s14"] - 0.1, seis)
    if t < C["s14"]:
        return
    E.foco(c, t, C["s14.a"], 0.5, lambda a: E.pilula(c, "não compensa: a chance muda de uma vez para outra", W / 2, 200, 50, estilo="g", fundo=ERRADO, a=a))
    E.foco(c, t, C["s14.b"], 0.5, lambda a: saco(c, 640, 600, 420, 380, a))
    for k, (cor, x) in enumerate(((AZUL, 560), (VERM, 660), (AZUL, 720), (VERM, 590))):
        E.foco(c, t, C["s14.b"] + 0.3 + 0.08 * k, 0.4, lambda a, cor=cor, x=x, k=k: E.bola(c, x, 600 + (k % 2) * 70, 36, cor, a))
    E.frase(c, t, C["s14.b"] + 0.5, [("sem", "g", 72, BR), ("devolver", "g", 72, BR)], 980, 560, passo=0.12)
    E.frase(c, t, lerp(C["s14.b"], C["s14.end"], 0.4), ps("cada fração calculada de novo", "i", 56, CLARO), 980, 680, passo=0.08)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s15"] + 0.1, [("hora", "i", 72, COR), ("de", "i", 72, COR), ("testar", "i", 72, COR)], XE, 170)
    E.foco(c, t, C["s15.a"], 0.45, lambda a: semaforo(c, XE + 80, 420, 250, a))
    E.foco(c, t, C["s15.a"] + 0.3, 0.45, lambda a: semaforo(c, XE + 600, 420, 250, a))
    E.frase(c, t, C["s15.a"] + 0.8, ps("2 semáforos, sem ligação entre si", "i", 56, TINTA2), XE, 700, passo=0.08)
    E.foco(c, t, C["s15.b"], 0.45, lambda a: E.escreve(c, "1º verde:", XE + 190, 350, 50, "b", TINTA, a))
    E.fr(c, t, C["s15.b"] + 0.2, 2, 5, XE + 290, 470, 100, CERTO)
    E.foco(c, t, C["s15.c"], 0.45, lambda a: E.escreve(c, "2º verde:", XE + 710, 350, 50, "b", TINTA, a))
    E.fr(c, t, C["s15.c"] + 0.2, 1, 3, XE + 810, 470, 100, CERTO)
    E.frase(c, t, C["s15.d"], [("chance", "i", 72), ("de", "i", 72), ("pegar", "i", 72), ("ambos", "g", 80, COR), ("verdes?", "g", 80, CERTO)], XE, 860, passo=0.12)
    E.relogio(c, t, C["s16.a"], 1500, 560, 190)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    E.foco(c, t, C["s17"] + 0.4, 0.45, lambda a: (semaforo(c, 250, 330, 200, a), semaforo(c, 400, 330, 200, a)))
    E.foco(c, t, C["s17.a"], 0.5, lambda a: E.pilula(c, "independentes: multiplique", 1000, 330, 58, estilo="g", a=a))
    y = 680
    xs, xf = linha(c, t, 220, y, 110, [((2, 5), C["s17.a"] + 0.4), ("×", C["s17.a"] + 0.6), ((1, 3), C["s17.a"] + 0.8), ("=", C["s17.b"] - 0.2)])
    w = fracao_partes(c, t, xf + 170, y, 110, "2 × 1", "5 × 3", C["s17.b"], C["s17.c"])
    E.sinal(c, t, C["s17.d"] - 0.2, "=", xf + 170 + w / 2 + 70, y, 100)
    E.resultado(c, t, C["s17.d"], 2, 15, xf + 170 + w / 2 + 250, y, 100, 125, CERTO)
    nota(c, t, C["s17.d"] + 1.0, xf + 170 + w / 2 + 250, y + 210, "pouco mais de 13%", 46, TINTA2, "i")


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s18"], [("resumindo", "i", 92, COR)], W / 2, 190, "center")
        E.frase(c, t, C["s18.a"], ps("a pista não muda a chance?", "i", 68), W / 2, 380, "center", passo=0.1)
        E.foco(c, t, C["s18.a"] + 1.4, 0.5, lambda a: E.pilula(c, "independentes", W / 2, 510, 66, estilo="g", a=a))
        E.foco(c, t, C["s18.b"], 0.5, lambda a: E.centro(c, "P(A e B) = P(A) × P(B)", W / 2, 780, 100, "g", TINTA, a))
    E.saida(c, t, C["s19"] - 0.1, resumo)
    if t < C["s19"]:
        return
    E.frase(c, t, C["s19"] + 0.1, ps("próxima aula", "i", 84), XE, 300)
    E.foco(c, t, C["s19.a"], 0.45, lambda a: saco(c, XE + 170, 590, 300, 260, a))
    for k, (cor, x) in enumerate(((AZUL, XE + 120), (VERM, XE + 220))):
        E.foco(c, t, C["s19.a"] + 0.3 + 0.1 * k, 0.4, lambda a, cor=cor, x=x: E.bola(c, x, 610, 36, cor, a))
    E.frase(c, t, C["s19.a"] + 0.2, [("2", "g", 76, COR), ("bolas", "i", 70), ("de", "i", 70), ("uma", "i", 70), ("urna", "g", 76)], XE + 380, 560, passo=0.1)
    E.frase(c, t, C["s19.b"], [("devolvendo", "g", 70, COR), ("ou", "i", 66), ("não?", "g", 70)], XE + 380, 670, passo=0.1)
    E.foco(c, t, C["s19.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1560, 820, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s19.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1850, 1690, p), lerp(1040, 845, p), ep(t, C["s19.c"] + 0.2, 0.4))
    E.frase(c, t, C["s19.d"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 980, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, tabela=b_tabela, regra=b_regra, dependentes=b_dependentes, erro=b_erro, atalho=b_atalho,
              questao=b_questao, resposta=b_resposta, fim=b_fim)
