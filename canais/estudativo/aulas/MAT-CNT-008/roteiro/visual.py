"""Visual — Estudativo · MAT-CNT-008: combinação, quando a ordem não importa.
Mesma linguagem da trilha Contagem e Probabilidade (MAT-CNT-001 a 007): casinhas() com o número de opções dentro e a etapa embaixo,
"?" em cinza, × entre elas, igual_bola() com o resultado na esfera; regra() = pílula da restrição.
Peças vindas da MAT-CNT-005: pessoa(), fila() (troca de lugar em arco) e bloco() (o grupo). Da MAT-CNT-004: fracao_corte().
Peças desta aula:
- ficha(): a inicial de cada pessoa numa ficha na cor dela; ordens(): as 6 ordens de Ana, Bia e Caio, que se juntam numa comissão só.
- pizza(): pizza meio a meio que gira (calabresa com queijo é queijo com calabresa).
- quadro_frac(): a fração montada aos poucos (em cima o arranjo, embaixo p!).
Sem voz ainda: todo instante vem de C[...] (cenas e marcadores), nunca de segundos fixos."""
import math
from itertools import combinations, permutations
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Contagem e Probabilidade")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-CNT-008_combinacao.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("troca", "repetidas", "regra", "pizza", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
F = math.factorial
C_ = lambda n, p: sum(1 for _ in combinations(range(n), p))
assert 8 * 7 * 6 == 336 and 336 // F(3) == 56 == C_(8, 3) and F(3) == 6 and 336 // 3 == 112
assert F(8) // (F(8) * F(0)) == 1 == C_(8, 8)
assert 5 * 4 == 20 and 20 // F(2) == 10 == C_(5, 2)
assert 10 * 9 == 90 and 90 // 2 == 45 == C_(10, 8) == C_(10, 2) and 9 * 8 // 2 == 36 == C_(9, 7)
assert 11 * 10 == 110 and 110 // 2 == 55 == C_(11, 2) and 6 * 5 * 4 == 120 and 120 // 6 == 20 == C_(6, 3)
assert len(list(permutations("ABC"))) == 6

GENTE = ["#E08A3C", "#8E5BD9", "#5B8DB8", "#55895A", "#C2463A", "#9C9CA3", "#3FA7A0", "#B58A2E", "#D06A9A", "#6B7F3A"]
PESSOAS = {"Ana": GENTE[0], "Bia": GENTE[1], "Caio": GENTE[2]}
ORDENS = [("Ana", "Bia", "Caio"), ("Ana", "Caio", "Bia"), ("Bia", "Ana", "Caio"), ("Bia", "Caio", "Ana"), ("Caio", "Ana", "Bia"), ("Caio", "Bia", "Ana")]


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças da trilha (iguais às da MAT-CNT-002) ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    """uma frase, palavra a palavra, no mesmo estilo"""
    return [(w, est, size, cor) for w in txt.split()]


def casinhas(c, t, cx, y, itens, s=180, gap=None, tx=None, escuro=False, size=None, tnomes=None):
    """as casinhas do princípio multiplicativo, centradas em cx; y = centro das caixas.
    itens = [(nome embaixo, valor, t_caixa, t_valor[, cor do valor])]; valor None = caixa vazia; "?" sai em cinza;
    cor "fixo" = algarismo já decidido: caixa cheia, valor em branco, sem × ao lado.
    tx = instante de cada × (None = sem ×; senão, junto com a caixa da direita); tnomes = instante de cada nome.
    Devolve o centro de cada caixa."""
    n = len(itens)
    gap = s * 0.62 if gap is None else gap
    if size is None:
        vals = [len(str(it[1])) for it in itens if it[1] is not None]
        maior = max(vals) if vals else 1
        size = s * (0.56 if maior <= 1 else 0.46 if maior == 2 else 0.36)
    x0 = cx - (n * s + (n - 1) * gap) / 2
    xs = [x0 + s / 2 + i * (s + gap) for i in range(n)]
    borda = BR if escuro else TINTA
    fixo = [len(it) > 4 and it[4] == "fixo" for it in itens]
    for i, it in enumerate(itens):
        nome, val, tb, tv = it[:4]
        cor_v = it[4] if len(it) > 4 else (BR if escuro else (CINZA if val == "?" else COR))
        x = xs[i]

        def caixa(a, x=x, cheia=fixo[i]):
            r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x - s / 2, y - s / 2, s, s), s * 0.12, s * 0.12)
            if escuro:
                c.drawRRect(r, M.paint(BR, (0.3 if cheia else 0.08) * a))
            else:
                sh = skia.Paint(AntiAlias=True, Color=M.hexc("#000000", 0.10 * a))
                sh.setMaskFilter(skia.MaskFilter.MakeBlur(skia.kNormal_BlurStyle, 10))
                c.save(); c.translate(0, 8); c.drawRRect(r, sh); c.restore()
                c.drawRRect(r, M.paint(TINTA if cheia else BR, a))
            c.drawRRect(r, M.paint(borda, a, stroke=5))
        E.foco(c, t, tb, 0.45, caixa)
        if nome:
            tn = tnomes[i] if tnomes else tb + 0.15
            E.foco(c, t, tn, 0.45, lambda a, x=x, nome=nome: centro(c, nome, x, y + s / 2 + max(52, s * 0.34), max(42, s * 0.27), "i",
                                                                  CLARO if escuro else TINTA2, a))
        if val is not None and tv is not None:
            cv = BR if cor_v == "fixo" else cor_v
            E.foco(c, t, tv, 0.45, lambda a, x=x, val=str(val), cv=cv: E.formula(c, val, x, y + size * 0.36, size, "g", cv, a, "center"))
        if i and not fixo[i] and not fixo[i - 1]:
            ti = tx[i - 1] if tx else tb
            if ti is not None:
                E.sinal(c, t, ti, "×", (xs[i - 1] + x) / 2, y, s * 0.42, BR if escuro else TINTA)
    return xs


def igual_bola(c, t, t0, x, y, txt, r=120, size=None, cor=None, escuro=False, t_igual=None):
    """'=' em x e o resultado numa esfera à direita; y = centro. Devolve o centro da esfera."""
    size = size or r * (0.72 if len(txt) <= 2 else 0.56 if len(txt) == 3 else 0.46)
    E.sinal(c, t, t0 - 0.2 if t_igual is None else t_igual, "=", x, y, r * 0.75, BR if escuro else TINTA)
    bx = x + r * 0.55 + r
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, bx, y, r, cor, a), centro(c, txt, bx, y + size * 0.36, size, "g", E.SOBRE, a)))
    return bx


def marca(c, t, t0, x, y, s, t1=None, cor=None):
    """caixa pontilhada em volta da casinha da vez (some em t1)"""
    def f():
        p = ep(t, t0, 0.4)
        m = s * 0.16
        E.caixa_pontilhada(c, x - s / 2 - m, y - s / 2 - m, s + 2 * m, s + 2 * m, p, cor, p)
    if t >= t0:
        E.saida(c, t, t1, f) if t1 is not None else f()


def regra(c, t, t0, x, y, txt, fundo=None, size=40, t1=None):
    """pílula com a restrição, centrada em (x, y)"""
    f = lambda: E.foco(c, t, t0, 0.45, lambda a: E.pilula(c, txt, x, y, size, estilo="b", fundo=fundo or TINTA2, a=a))
    E.saida(c, t, t1, f) if t1 is not None else f()


def nota(c, t, t0, x, y, txt, size=46, cor=TINTA2, estilo="b"):
    E.foco(c, t, t0, 0.45, lambda a: centro(c, txt, x, y, size, estilo, cor, a))


# ---------------- peças da MAT-CNT-005 e da MAT-CNT-004 ----------------
def pessoa(c, cx, cy, h, cor, nome=None, a=1.0, cor_nome=None, nome_y=None):
    """boneco simples: cabeça e tronco; (cx, cy) = centro do tronco. nome_y = linha de base do nome (senão, embaixo)"""
    if a <= 0:
        return
    c.drawCircle(cx, cy - h * 0.36, h * 0.17, M.paint(cor, a))
    r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - h * 0.25, cy - h * 0.14, h * 0.5, h * 0.52), h * 0.2, h * 0.2)
    c.drawRRect(r, M.paint(cor, a))
    if nome:
        centro(c, nome, cx, nome_y if nome_y is not None else cy + h * 0.38 + 56, max(40, h * 0.24), "b", cor_nome or TINTA, a)


def bloco(c, x0, x1, cy, h, a=1.0, cor=None, largura=7):
    """contorno do grupo: quem está dentro anda junto"""
    if a <= 0:
        return
    m = 26
    r = skia.RRect.MakeRectXY(skia.Rect.MakeLTRB(x0 - m, cy - h / 2 - m, x1 + m, cy + h / 2 + m), 34, 34)
    c.drawRRect(r, M.paint(cor or E.COR, 0.08 * a))
    c.drawRRect(r, M.paint(cor or E.COR, a, stroke=largura))


def fracao_corte(c, t, t0, cx, cy, size, cima, baixo, tcima=None, tc=None, cortar=(), cor=None, escuro=False):
    """fração de fatoriais: cima = lista de partes ("8", "×", "7", "×", "6!"), baixo = texto de baixo.
    tcima = instante de cada parte de cima (senão, junto); tc = instante do corte; cortar = índices de cima que somem com o de baixo."""
    tinta = cor or (BR if escuro else TINTA)
    esp = size * 0.22
    ws = [E.larg(p, "g", size) for p in cima]
    wc = sum(ws) + esp * (len(cima) - 1)
    wb = E.larg(baixo, "g", size)
    w = max(wc, wb) + size * 0.3
    y_cima, y_baixo = cy - size * 0.22, cy + size * 0.95
    E.foco(c, t, t0, 0.45, lambda a: c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2, cy - size * 0.05, w, size * 0.09), 4, 4),
                                                 M.paint(tinta, a)))
    x = cx - wc / 2
    pos = []
    for i, (p, wp) in enumerate(zip(cima, ws)):
        ti = tcima[i] if tcima else t0
        E.foco(c, t, ti, 0.45, lambda a, p=p, x=x: E.escreve(c, p, x, y_cima, size, "g", tinta, a))
        pos.append((x, wp))
        x += wp + esp
    E.foco(c, t, t0, 0.45, lambda a: E.escreve(c, baixo, cx - wb / 2, y_baixo, size, "g", tinta, a))
    if tc is not None and t >= tc:
        risca = E.COR if not escuro else CLARO
        for i in cortar:
            xx, wp = pos[i]
            E.risco(c, xx - 8, y_cima + 8, xx + wp + 8, y_cima - size * 0.78, t, tc, risca, size * 0.09)
        E.risco(c, cx - wb / 2 - 8, y_baixo + 8, cx + wb / 2 + 8, y_baixo - size * 0.78, t, tc + 0.2, risca, size * 0.09)
    return w



def fila(c, t, estados, cx, cy, passo, desenha, d=0.6, alto=None):
    """itens em fila que trocam de lugar. estados = [(instante, [ids na ordem])]; desenha(id, x, y).
    Quem muda de lugar desliza em arco (os que vão para a direita por cima, os outros por baixo). Devolve {id: x}"""
    cur, ant, q = estados[0][1], estados[0][1], 1.0
    for ti, ordem in estados:
        if t >= ti:
            ant, cur = cur, ordem
            q = ease_io(prog(t, ti, d))
    n = len(cur)
    alto = passo * 0.6 if alto is None else alto
    xs = {}
    for k in cur:
        i0, i1 = ant.index(k), cur.index(k)
        x = cx + (lerp(i0, i1, q) - (n - 1) / 2) * passo
        y = cy - math.sin(math.pi * q) * alto * (1 if i1 > i0 else -1 if i1 < i0 else 0)
        xs[k] = x
        desenha(k, x, y)
    return xs


# ---------------- peças desta aula ----------------
def ficha(c, cx, cy, s, nome, a=1.0):
    """a inicial da pessoa numa ficha na cor dela"""
    if a <= 0:
        return
    r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - s / 2, cy - s / 2, s, s), s * 0.2, s * 0.2)
    sh = skia.Paint(AntiAlias=True, Color=M.hexc("#000000", 0.12 * a))
    sh.setMaskFilter(skia.MaskFilter.MakeBlur(skia.kNormal_BlurStyle, 8))
    c.save(); c.translate(0, 6); c.drawRRect(r, sh); c.restore()
    c.drawRRect(r, M.paint(PESSOAS[nome], a))
    centro(c, nome[0], cx, cy + s * 0.22, s * 0.6, "g", BR, a)


def trio(c, cx, cy, s, ordem, a=1.0, passo_=None):
    passo_ = passo_ or s * 1.18
    for i, nome in enumerate(ordem):
        ficha(c, cx + (i - 1) * passo_, cy, s, nome, a)


LUG6 = [(560, 420), (560, 600), (560, 780), (1360, 420), (1360, 600), (1360, 780)]


def ordens(c, t, t0, tj=None, centro_=(W / 2, 600), s=110, mini=False, t1=None):
    """as 6 ordens de Ana, Bia e Caio, uma a uma a partir de t0; em tj todas deslizam para o centro e viram uma só"""
    q = ease_io(prog(t, tj, 1.0)) if tj is not None else 0.0
    for k, (ordem, (x, y)) in enumerate(zip(ORDENS, LUG6)):
        if mini:
            x, y = 1110 + (k % 3) * 290, 570 + (k // 3) * 140
        xx, yy = lerp(x, centro_[0], q), lerp(y, centro_[1], q)
        aa = 1.0 if k == 0 else 1 - ease_io(prog(t, tj + 0.7, 0.4)) if tj is not None else 1.0
        tk = t1 if (k == 0 and t1 is not None) else t0 + 0.25 * k
        E.foco(c, t, tk, 0.4, lambda a, ordem=ordem, xx=xx, yy=yy, aa=aa: trio(c, xx, yy, s, ordem, a * aa))
        if not mini and q == 0:
            E.foco(c, t, tk + 0.1, 0.4, lambda a, k=k, x=x, y=y: (E.bola(c, x - 260, y, 30, a=a), centro(c, str(k + 1), x - 260, y + 13, 36, "g", BR, a)))


def pizza(c, cx, cy, r, s1, s2, giro=0.0, a=1.0, nomes=True):
    """pizza meio a meio: s1 e s2 = (nome, cor). giro em graus"""
    if a <= 0:
        return
    sh = skia.Paint(AntiAlias=True, Color=M.hexc("#000000", 0.14 * a))
    sh.setMaskFilter(skia.MaskFilter.MakeBlur(skia.kNormal_BlurStyle, 14))
    c.drawCircle(cx, cy + 12, r, sh)
    c.drawCircle(cx, cy, r, M.paint("#E7B873", a))
    c.save(); c.translate(cx, cy); c.rotate(giro)
    ri = r * 0.86
    for k, (nome, cor) in enumerate((s1, s2)):
        p = skia.Path(); p.moveTo(0, 0); p.arcTo(skia.Rect.MakeXYWH(-ri, -ri, 2 * ri, 2 * ri), 90 + 180 * k, 180, False); p.close()
        c.drawPath(p, M.paint(cor, a))
    c.drawLine(0, -r, 0, r, M.paint(BR, a, stroke=6))
    if nomes:
        for k, (nome, cor) in enumerate((s1, s2)):
            x = -ri * 0.5 if k == 0 else ri * 0.5
            c.save(); c.translate(x, 0); c.rotate(-giro)
            centro(c, nome, 0, 14, r * 0.15, "g", BR, a)
            c.restore()
    c.restore()


def quadro_frac(c, t, t0, x, y, esq, cima, baixo, tc, tb, size=110, cor_c=None, cor_b=None):
    """'esq =' e, à direita, a fração: a barra e 'cima' entram em tc, 'baixo' em tb. y = linha da barra"""
    if esq:
        E.formula_em(c, t, t0, esq, x, y + size * 0.34, size, "g", TINTA)
    s_ = size * 0.78
    xf = x + (E.larg(esq, "g", size) + size * 0.35 if esq else 0)
    wc, wb = E.larg(cima, "g", s_), E.larg(baixo, "g", s_)
    w = max(wc, wb) + size * 0.3
    E.foco(c, t, tc, 0.45, lambda a: c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(xf, y - 4, w, 9), 4, 4), M.paint(TINTA, a)))
    E.foco(c, t, tc, 0.45, lambda a: E.escreve(c, cima, xf + (w - wc) / 2, y - size * 0.22, s_, "g", cor_c or TINTA, a))
    E.foco(c, t, tb, 0.45, lambda a: E.escreve(c, baixo, xf + (w - wb) / 2, y + size * 0.78, s_, "g", cor_b or TINTA, a))
    return xf, w


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def pergunta():
        E.frase(c, t, C["s01.a"], [("8", "g", 84, COR), ("pessoas", "i", 84)], W / 2, 180, "center")
        for i in range(8):
            x = W / 2 + (i - 3.5) * 170
            E.foco(c, t, C["s01.a"] + 0.3 + 0.07 * i, 0.4, lambda a, i=i, x=x: pessoa(c, x, 360, 130, GENTE[i], None, a))
        if t >= C["s01.b"]:
            x0, x1 = W / 2 - 3.5 * 170 - 60, W / 2 - 1.5 * 170 + 60
            E.foco(c, t, C["s01.b"], 0.5, lambda a: bloco(c, x0 + 10, x1 - 10, 380, 190, a))
            E.foco(c, t, C["s01.b"] + 0.3, 0.5, lambda a: E.centro(c, "comissão de 3", (x0 + x1) / 2, 560, 60, "g", COR, a))
        E.formula_em(c, t, C["s01.c"], "8 × 7 × 6 = 336", 260, 790, 110, "g", ERRADO)
        E.foco(c, t, C["s01.c"] + 0.5, 0.4, lambda a: E.escreve(c, "conta do pódio", 270, 880, 52, "i", TINTA2, a))
        if t >= C["s01.c"] + 2.4:
            E.risco(c, 240, 750, 1080, 750, t, C["s01.c"] + 2.4, largura=12)
        E.foco(c, t, C["s01.d"], 0.4, lambda a: E.escreve(c, "são só", 1200, 820, 80, "i", TINTA, a))
        E.foco(c, t, C["s01.d"] + 0.2, 0.5, lambda a: (E.bola(c, 1590, 790, 120, a=a), centro(c, "56", 1590, 790 + 40, 110, "g", BR, a)))
    E.saida(c, t, C["s02"] - 0.1, pergunta)

    if t >= C["s02"]:
        E.foco(c, t, C["s02.c"] - 0.2, 0.7, lambda a: E.bola(c, 1450, 520, 300 * ease_back(prog(t, C["s02.c"] - 0.2, 0.7))), blur=0)
        E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 96), XE, 330)
        E.frase(c, t, C["s02.a"] + 0.9, [("a", "i", 110), ("ordem", "g", 120, COR), ("não", "g", 120)], XE, 480)
        E.frase(c, t, C["s02.a"] + 1.3, [("importa", "g", 120)], XE, 620)
        E.frase(c, t, C["s02.b"], [("de", "i", 84), ("onde", "i", 84), ("vem", "i", 84), ("a", "i", 84), ("divisão", "g", 90, COR)], XE, 790)
        E.foco(c, t, C["s02.c"] + 0.2, 0.5, lambda a: (E.escreve(c, "+ atalho", 1290, 505, 84, "g", BR, a),
                                                      E.escreve(c, "de prova", 1310, 590, 84, "i", BR, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], [("você", "i", 84), ("vai", "i", 84), ("usar", "i", 84)], W / 2, 190, "center")
    for k, x, titulo in (("s03.a", 160, "arranjo"), ("s03.c", 1000, "teste da troca")):
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, 290, 760, 640, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(titulo, "g", 64, COR)], x + 380, 390, "center")
    E.foco(c, t, C["s03.a"] + 0.3, 0.4, lambda a: E.centro(c, "a ordem importa", 540, 470, 46, "i", TINTA2, a))
    xs = casinhas(c, t, 540, 640, [("", v, C["s03.b"] + 0.1 * i, C["s03.b"] + 0.3 + 0.15 * i) for i, v in enumerate((8, 7, 6))], s=120, gap=60)
    E.foco(c, t, C["s03.b"] + 0.9, 0.4, lambda a: E.centro(c, "um número por lugar", 540, 820, 46, "i", TINTA2, a))
    est = [(C["s03.c"] + 0.3, ["Ana", "Bia"]), (C["s03.c"] + 1.4, ["Bia", "Ana"])]
    E.foco(c, t, C["s03.c"] + 0.3, 0.4, lambda a: fila(c, t, est, 1380, 640, 170, lambda k, x, y: ficha(c, x, y, 130, k, a), alto=110))
    E.foco(c, t, C["s03.c"] + 2.1, 0.4, lambda a: E.centro(c, "muda o resultado?", 1380, 820, 50, "i", TINTA2, a))
    E.frase(c, t, lerp(C["s03.c"], C["s03.end"], 0.72), ps("faltou alguma? procure no canal", "i", 52, TINTA2), W / 2, 1010, "center", passo=0.1)


# ---------------- o teste da troca ----------------
def b_troca(c, t, C, b):
    E.frase(c, t, C["s04"] + 0.1, [("o", "i", 80), ("teste", "i", 80), ("da", "i", 80), ("troca", "g", 84, COR)], W / 2, 180, "center")
    y = 520
    est = [(C["s04.a"], ["Ana", "Bia", "Caio"]), (C["s04.b"], ["Bia", "Caio", "Ana"])]

    def desenha(k, x, yy, a=1.0):
        pessoa(c, x, yy, 200, PESSOAS[k], k, a, TINTA)
    xs = fila(c, t, est, W / 2, y, 280, lambda k, x, yy: E.foco(c, t, C["s04.a"] + 0.12 * ["Ana", "Bia", "Caio"].index(k), 0.4,
                                                            lambda a: desenha(k, x, yy, a)), alto=170)
    E.foco(c, t, C["s04.b"], 0.4, lambda a: E.centro(c, "troque a ordem", W / 2 + 620, y, 56, "i", TINTA2, a) if t < C["s04.c"] else None)
    E.foco(c, t, C["s04.c"], 0.5, lambda a: bloco(c, W / 2 - 280 - 120, W / 2 + 280 + 120, y + 40, 360, a))
    E.foco(c, t, C["s04.c"] + 0.3, 0.5, lambda a: E.centro(c, "a mesma comissão", W / 2, 860, 72, "g", CERTO, a))
    E.foco(c, t, C["s04.d"], 0.5, lambda a: E.pilula(c, "a ordem não importa", W / 2, 980, 60, estilo="g", a=a))


# ---------------- repetições ----------------
def b_repetidas(c, t, C, b):
    def lista():
        E.frase(c, t, C["s05.a"], [("arranjo:", "g", 72, COR), ("cada", "i", 72), ("ordem", "g", 72), ("conta", "i", 72), ("1", "g", 72, COR)],
                W / 2, 200, "center")
        ordens(c, t, C["s05.b"] - 0.6, tj=C["s05.d"], t1=C["s05.a"] + 0.8)
        E.foco(c, t, C["s05.c"], 0.5, lambda a: E.pilula(c, "no arranjo: 6 resultados", W / 2, 960, 56, estilo="g", fundo=TINTA2, a=a)
               if t < C["s05.d"] else None)
        if t >= C["s05.d"] + 0.9:
            E.foco(c, t, C["s05.d"] + 0.9, 0.5, lambda a: bloco(c, W / 2 - 130 - 55, W / 2 + 130 + 55, 600, 110, a))
            E.foco(c, t, C["s05.d"] + 1.1, 0.5, lambda a: E.pilula(c, "na comissão: 1 só", W / 2, 840, 60, estilo="g", a=a))
    E.saida(c, t, C["s06.a"] - 0.1, lista)
    if C["s06.a"] <= t < C["s07"] + 0.5:
        def fatorial():
            E.frase(c, t, C["s06.a"], ps("por que 6?", "i", 84), W / 2, 200, "center")
            xs = casinhas(c, t, 760, 480, [(f"{i + 1}º", v, C["s06.a"] + 0.15 * i, C["s06.a"] + 0.4 + 0.15 * i) for i, v in enumerate((3, 2, 1))],
                          s=170, gap=100, tx=[C["s06.b"], C["s06.b"] + 0.15])
            E.foco(c, t, C["s06.a"] + 0.2, 0.5, lambda a: E.formula(c, "3!", 210, 520, 110, "g", COR, a))
            igual_bola(c, t, C["s06.b"] + 0.4, xs[2] + 150, 480, "6", r=105)
            E.frase(c, t, C["s06.c"], [("toda", "g", 68, COR), ("comissão", "g", 68, COR), ("aparece", "i", 68), ("6", "g", 72, COR),
                                       ("vezes", "i", 68), ("no", "i", 68), ("arranjo", "i", 68)], W / 2, 860, "center", passo=0.12)
        E.saida(c, t, C["s07"] - 0.1, fatorial)
    if t < C["s07"]:
        return
    E.frase(c, t, C["s07.a"], [("divida", "i", 90), ("pelas", "i", 90), ("repetições", "g", 96, COR)], W / 2, 260, "center")
    quadro_frac(c, t, C["s07.b"], 300, 600, "comissões =", "336", "3! = 6", C["s07.b"] + 0.2, C["s07.b"] + 0.5, size=96)
    igual_bola(c, t, C["s07.b"] + 1.0, 1260, 600, "56", r=120)


# ---------------- regra ----------------
def b_regra(c, t, C, b):
    def nome():
        E.frase(c, t, C["s08.a"], ps("escolher alguns sem que a ordem importe", "i", 64, TINTA2), W / 2, 200, "center", passo=0.12)
        E.frase(c, t, C["s08.b"], [("combinação", "g", 160, COR)], W / 2, 420, "center")
        for i, (k, l1, l2) in enumerate((("s08.c", "faça o", "arranjo"), ("s08.d", "divida pelo", "fatorial de quantos escolheu"))):
            y = 620 + i * 190
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 330, y, 50, a=a), centro(c, str(i + 1), 330, y + 21, 56, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, [(l1, "i", 68), (l2, "g", 72, COR)], 420, y + 24)
    E.saida(c, t, C["s09"] - 0.1, nome)
    if C["s09"] <= t < C["s10"] + 0.5:
        def formula():
            E.foco(c, t, C["s09.a"], 0.5, lambda a: E.pilula(c, "n = total", 560, 220, 52, estilo="b", fundo=TINTA2, a=a))
            E.foco(c, t, C["s09.a"] + 0.6, 0.5, lambda a: E.pilula(c, "p = quantos escolhe", 1180, 220, 52, estilo="b", fundo=TINTA2, a=a))
            xf, w = quadro_frac(c, t, C["s09.b"], 260, 480, "C(n, p) =", "A(n, p)", "p!", C["s09.b"], C["s09.c"], size=110, cor_c=COR)
            E.foco(c, t, C["s09.b"] + 0.5, 0.5, lambda a: E.escreve(c, "p números descendo do n", xf + w + 50, 450, 52, "i", COR, a))
            E.foco(c, t, C["s09.c"] + 0.3, 0.5, lambda a: E.escreve(c, "p fatorial", xf + w + 50, 580, 52, "i", TINTA2, a))
            E.foco(c, t, C["s09.d"], 0.5, lambda a: E.escreve(c, "nos livros:", 260, 760, 56, "i", TINTA2, a))
            E.formula_em(c, t, C["s09.d"] + 0.3, "C(n, p) = f{n!}{p! · (n − p)!}", 260, 900, 100, "g", TINTA)
            E.foco(c, t, C["s09.d"] + 2.5, 0.5, lambda a: E.pilula(c, "a mesma conta, sem cortar", 1420, 880, 46, estilo="b", fundo=TINTA2, a=a))
        E.saida(c, t, C["s10"] - 0.1, formula)
    if t < C["s10"]:
        return
    E.frase(c, t, C["s10.a"], [("e", "i", 84), ("se", "i", 84), ("escolher", "i", 84), ("todos", "g", 90, COR), ("os", "i", 84), ("8?", "g", 90, COR)],
            W / 2, 220, "center")
    E.formula_em(c, t, C["s10.a"] + 0.8, "C(8, 8) = f{8!}{8! · 0!}", 260, 520, 120, "g", TINTA)
    E.foco(c, t, C["s10.b"], 0.5, lambda a: E.pilula(c, "0! = 1", 1300, 500, 64, estilo="g", a=a))
    E.formula_em(c, t, C["s10.c"] - 0.3, "f{8!}{8!}", 600, 830, 100, "g", TINTA)
    igual_bola(c, t, C["s10.c"], 860, 800, "1", r=100)
    E.foco(c, t, C["s10.c"] + 0.5, 0.5, lambda a: E.escreve(c, "comissão só, com todos", 1150, 820, 56, "i", COR, a))


# ---------------- pizza ----------------
CALAB, QUEIJO = ("calabresa", "#C2463A"), ("queijo", "#E9B949")
SABORES = [CALAB, QUEIJO, ("frango", "#D9894A"), ("atum", "#7A8FA6"), ("milho", "#E6CF3B")]


def b_pizza(c, t, C, b):
    E.frase(c, t, C["s11.a"], [("pizza", "g", 76, COR), ("meio", "i", 76), ("a", "i", 76), ("meio:", "i", 76), ("2", "g", 76, COR),
                               ("sabores", "i", 76), ("diferentes", "i", 76)], W / 2, 170, "center", passo=0.12)
    giro = 180 * ease_io(prog(t, C["s11.c"] - 1.6, 1.2))
    E.foco(c, t, C["s11.a"] + 0.6, 0.5, lambda a: pizza(c, 520, 520, 230, CALAB, QUEIJO, giro, a))
    for i, (nome, cor) in enumerate(SABORES):
        y = 330 + i * 92
        E.foco(c, t, C["s11.b"] + 0.15 * i, 0.4, lambda a, y=y, nome=nome, cor=cor: (c.drawCircle(1000, y - 16, 26, M.paint(cor, a)),
                                                                                E.escreve(c, nome, 1050, y, 52, "b", TINTA, a)))
    E.foco(c, t, C["s11.c"] - 1.6, 0.4, lambda a: E.centro(c, "girou: a mesma pizza", 520, 820, 52, "i", TINTA2, a))
    E.foco(c, t, C["s11.c"], 0.5, lambda a: E.pilula(c, "combinação", 1560, 420, 60, estilo="g", a=a))
    E.formula_em(c, t, C["s11.d"], "5 × 4 = 20", 260, 990, 96, "g", TINTA)
    quadro_frac(c, t, C["s11.e"], 900, 920, "", "20", "2!", C["s11.e"], C["s11.e"] + 0.3, size=96)
    bx = igual_bola(c, t, C["s11.e"] + 0.8, 1110, 950, "10", r=95)
    E.foco(c, t, C["s11.e"] + 1.1, 0.5, lambda a: E.escreve(c, "pizzas", bx + 115, 972, 60, "g", COR, a))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s12"] + 0.1, [("cuidado", "g", 96, ERRADO), ("com", "i", 90), ("isto", "i", 90)], W / 2, 170, "center")
    E.frase(c, t, C["s12.a"], ps("dividir só pelo número de escolhidos", "i", 60, TINTA2), W / 2, 270, "center", passo=0.1)
    E.formula_em(c, t, C["s12.b"], "336 ÷ 3", 220, 470, 110, "g", ERRADO)
    E.formula_em(c, t, C["s12.c"], "= 112", 650, 470, 110, "g", ERRADO)
    if t >= C["s12.d"]:
        E.risco(c, 200, 430, 1010, 430, t, C["s12.d"], largura=12)
    ordens(c, t, C["s12.d"], mini=True, s=70)
    E.foco(c, t, C["s12.d"] + 1.5, 0.5, lambda a: E.centro(c, "aparece 6 vezes: uma por ordem", 1400, 870, 50, "i", TINTA, a))
    E.formula_em(c, t, C["s12.e"], "336 ÷ 3! = 56", 220, 960, 110, "g", CERTO)
    E.foco(c, t, C["s12.e"] + 0.6, 0.5, lambda a: E.pilula(c, "3!, não 3", 1400, 975, 56, estilo="g", fundo=CERTO, a=a))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def fora():
        E.frase(c, t, C["s13.a"], ps("escolher quem entra = escolher quem fica de fora", "i", 64, BR), W / 2, 180, "center", passo=0.1)
        E.frase(c, t, C["s13.b"], [("comissão", "i", 72, CLARO), ("de", "i", 72, CLARO), ("8", "g", 76, BR), ("entre", "i", 72, CLARO), ("10", "g", 76, BR)],
                W / 2, 300, "center")
        y = 500
        for i in range(10):
            x = W / 2 + (i - 4.5) * 150
            k = 1.0 if i >= 8 or t < C["s13.c"] else 1 - 0.6 * ep(t, C["s13.c"], 0.5)
            E.foco(c, t, C["s13.b"] + 0.3 + 0.05 * i, 0.4, lambda a, i=i, x=x, k=k: pessoa(c, x, y, 120, GENTE[i], None, a * k))
        if t >= C["s13.b"] + 0.9:
            E.foco(c, t, C["s13.b"] + 0.9, 0.5, lambda a: bloco(c, W / 2 - 4.5 * 150 - 50, W / 2 + 2.5 * 150 + 50, y + 20, 180, a, CLARO, 5))
        if t >= C["s13.c"]:
            E.foco(c, t, C["s13.c"], 0.5, lambda a: bloco(c, W / 2 + 3.5 * 150 - 50, W / 2 + 4.5 * 150 + 50, y + 20, 180, a, E.COR, 8))
            E.foco(c, t, C["s13.c"] + 0.3, 0.5, lambda a: E.centro(c, "só 2 de fora", W / 2 + 4 * 150, y + 190, 52, "g", BR, a))
        E.formula_em(c, t, C["s13.d"], "10 × 9 = 90", 260, 900, 100, "g", BR)
        E.formula_em(c, t, C["s13.e"], "90 ÷ 2! = 45", 1000, 900, 100, "g", BR)
    E.saida(c, t, C["s14"] - 0.1, fora)
    if t < C["s14"]:
        return
    E.frase(c, t, C["s14.a"], ps("cada comissão de 8 deixa 2 de fora", "i", 64, BR), W / 2, 180, "center", passo=0.1)
    E.frase(c, t, C["s14.b"], ps("e cada dupla de fora forma 1 comissão", "i", 64, CLARO), W / 2, 280, "center", passo=0.1)
    E.foco(c, t, C["s14.c"], 0.5, lambda a: E.pilula(c, "compensa: escolhe mais da metade", W / 2, 450, 54, estilo="g", fundo=CERTO, a=a))
    E.foco(c, t, C["s14.d"], 0.5, lambda a: E.pilula(c, "menos da metade: conta direto", W / 2, 590, 54, estilo="g", fundo=TINTA2, a=a))
    E.frase(c, t, C["s14.d"] + 1.6, [("7", "g", 72, BR), ("entre", "i", 66, CLARO), ("9:", "g", 72, BR), ("2", "g", 72, BR), ("de", "i", 66, CLARO),
                                     ("fora", "i", 66, CLARO)], 260, 800, passo=0.12)
    E.formula_em(c, t, C["s14.e"] - 0.8, "f{9 × 8}{2}", 900, 800, 96, "g", BR)
    igual_bola(c, t, C["s14.e"], 1210, 790, "36", r=95, cor=E.COR, escuro=True)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s15"] + 0.1, [("hora", "i", 72, COR), ("de", "i", 72, COR), ("testar", "i", 72, COR)], XE, 190)
    E.frase(c, t, C["s15.a"], [("turma", "i", 76), ("de", "i", 76), ("11", "g", 84, COR), ("pessoas", "i", 76)], XE, 350)
    E.frase(c, t, C["s15.b"], [("uma", "i", 76), ("dupla", "g", 84), ("para", "i", 76), ("o", "i", 76), ("trabalho", "i", 76)], XE, 460)
    E.frase(c, t, C["s15.c"], [("quantas", "i", 76), ("duplas?", "g", 84, COR)], XE, 570)
    E.frase(c, t, C["s15.d"], [("3", "g", 84, COR), ("livros", "i", 76), ("entre", "i", 76), ("6:", "g", 84, COR)], XE, 760)
    E.frase(c, t, C["s15.d"] + 1.0, [("quantos", "i", 76), ("jeitos?", "g", 84, COR)], XE, 870)
    E.relogio(c, t, C["s16.a"], 1500, 560, 200)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    def duplas():
        E.frase(c, t, C["s17.a"], [("trocar", "i", 72), ("a", "i", 72), ("ordem", "i", 72), ("não", "g", 72), ("muda:", "i", 72), ("combinação", "g", 76, COR)],
                W / 2, 200, "center", passo=0.12)
        xs = casinhas(c, t, 560, 500, [("", 11, C["s17.b"], C["s17.b"] + 0.2), ("", 10, C["s17.b"] + 0.15, C["s17.b"] + 0.35)], s=170, gap=100)
        E.formula_em(c, t, C["s17.b"] + 0.6, "= 110", xs[1] + 130, 545, 110, "g", TINTA)
        quadro_frac(c, t, C["s17.c"], 300, 820, "", "110", "2!", C["s17.c"], C["s17.c"] + 0.3, size=110)
        bx = igual_bola(c, t, C["s17.c"] + 0.8, 640, 850, "55", r=105, cor=CERTO)
        E.foco(c, t, C["s17.c"] + 1.1, 0.5, lambda a: E.escreve(c, "duplas", bx + 130, 872, 64, "g", CERTO, a))
    E.saida(c, t, C["s18"] - 0.1, duplas)
    if t < C["s18"]:
        return
    E.frase(c, t, C["s18.a"], [("livros:", "g", 76, COR), ("também", "i", 72), ("sem", "i", 72), ("ordem", "g", 72)], W / 2, 200, "center")
    xs = casinhas(c, t, 600, 480, [("", v, C["s18.b"] + 0.15 * i, C["s18.b"] + 0.2 + 0.15 * i) for i, v in enumerate((6, 5, 4))], s=160, gap=90)
    E.formula_em(c, t, C["s18.b"] + 0.8, "= 120", xs[2] + 125, 522, 104, "g", TINTA)
    quadro_frac(c, t, C["s18.c"], 300, 820, "", "120", "3!", C["s18.c"], C["s18.c"] + 0.3, size=110)
    E.foco(c, t, C["s18.c"] + 1.0, 0.5, lambda a: E.escreve(c, "3! = 6", 300, 1010, 56, "b", TINTA2, a))
    bx = igual_bola(c, t, C["s18.d"], 640, 850, "20", r=105, cor=CERTO)
    E.foco(c, t, C["s18.d"] + 0.3, 0.5, lambda a: E.escreve(c, "jeitos", bx + 130, 872, 64, "g", CERTO, a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s19"], [("resumindo", "i", 92, COR)], W / 2, 210, "center")
        for i, (k, l1, l2) in enumerate((("s19.a", "a ordem não importa?", "é combinação"),
                                         ("s19.b", "faça o arranjo e divida", "pelo fatorial dos escolhidos"))):
            y = 430 + i * 260
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 300, y + 10, 56, a=a), centro(c, str(i + 1), 300, y + 33, 64, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, ps(l1, "i", 68), 400, y - 10, passo=0.1)
            E.frase(c, t, C[k] + 0.6, [(l2, "g", 88, COR)], 400, y + 95)
    E.saida(c, t, C["s20"] - 0.1, resumo)
    if t < C["s20"]:
        return
    E.frase(c, t, C["s20"] + 0.1, ps("próxima aula", "i", 84), XE, 300)
    E.frase(c, t, C["s20"] + 0.6, [("comissões", "g", 92, COR), ("com", "i", 84), ("regras", "g", 92, COR)], XE, 440)
    E.frase(c, t, C["s20.a"], [("2", "g", 64, COR), ("homens", "i", 60), ("entre", "i", 60), ("5", "g", 64, COR), ("e", "i", 60), ("2", "g", 64, COR),
                               ("mulheres", "i", 60), ("entre", "i", 60), ("4", "g", 64, COR)], XE, 580, passo=0.1)
    E.frase(c, t, C["s20.b"], [("e", "i", 80), ("o", "i", 80), ("“pelo", "g", 84), ("menos", "g", 84), ("um”", "g", 84)], XE, 720)
    E.foco(c, t, C["s20.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1480, 330, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s20.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1810, 1610, p), lerp(650, 355, p), ep(t, C["s20.c"] + 0.2, 0.4))
    E.frase(c, t, C["s20.d"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 960, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, troca=b_troca, repetidas=b_repetidas, regra=b_regra, pizza=b_pizza, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
