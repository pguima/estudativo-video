"""Visual — Estudativo · MAT-CNT-010: praticando contagem (5 situações).
Mesma linguagem da trilha Contagem e Probabilidade (MAT-CNT-001 a 009): casinhas() com o número de opções dentro e a etapa embaixo,
"?" em cinza, × entre elas, igual_bola() com o resultado na esfera; regra() = pílula da restrição; ordem() = esfera com a ordem de
preenchimento; marca() = caixa pontilhada na casinha da vez.
Peças vindas da MAT-CNT-005: letra() (ficha de letra), bloco().
Peças desta aula:
- decisao(): as 4 escolhas (multiplico, permuto, arranjo, combino) no alto da tela; a da vez acende na cor da matéria.
- questao_n(): o quadradinho numerado de cada questão da prova (situação 5).
Sem voz ainda: todo instante vem de C[...] (cenas e marcadores), nunca de segundos fixos."""
import math
from itertools import combinations, permutations
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Contagem e Probabilidade")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-CNT-010_praticando_contagem.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("lembrete", "questao1", "questao2", "questao3", "questao4", "questao5", "fim"))
BR = "#FFFFFF"
F = math.factorial
C_ = lambda n, p: sum(1 for _ in combinations(range(n), p))
assert sum(1 for n in range(1000, 10000) if len(set(str(n))) == 4 and n % 2 == 1) == 2240 == 5 * 8 * 8 * 7
assert 5 * 8 == 40 and 40 * 8 == 320 and 320 * 7 == 2240
assert sum(1 for p in set(permutations("PRATO")) if p[0] in "AO") == 48 == 2 * F(4) and F(5) == 120
assert 12 * 11 == 132 and 132 // 2 == 66
assert C_(7, 4) == 35 == 7 * 6 * 5 // F(3) == 7 * 6 * 5 * 4 // F(4) and 7 * 6 * 5 == 210 and 7 * 6 * 5 * 4 == 840
assert sum(1 for g in combinations(range(1, 11), 7) if 1 in g and 2 in g) == 56 == C_(8, 5) == 8 * 7 * 6 // F(3) and C_(10, 7) == 120

OPCOES = ("multiplico", "permuto", "arranjo", "combino")


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


def ordem(c, t, t0, x, y, s, n, cor=None):
    """esfera pequena no canto de cima, à esquerda, com a ordem em que a casinha é preenchida"""
    cx, cy = x - s / 2, y - s / 2
    k = ease_back(prog(t, t0, 0.45))
    if k > 0:
        E.bola(c, cx, cy, 30 * k, cor)
        centro(c, str(n), cx, cy + 13, 36 * k, "g", BR)


def letra(c, cx, cy, s, ch, a=1.0, fundo=BR, tinta=TINTA, borda=TINTA):
    """ficha de letra, como as de jogo de palavras (MAT-CNT-005)"""
    if a <= 0:
        return
    r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - s / 2, cy - s / 2, s, s), s * 0.16, s * 0.16)
    sh = skia.Paint(AntiAlias=True, Color=M.hexc("#000000", 0.12 * a))
    sh.setMaskFilter(skia.MaskFilter.MakeBlur(skia.kNormal_BlurStyle, 8))
    c.save(); c.translate(0, 6); c.drawRRect(r, sh); c.restore()
    c.drawRRect(r, M.paint(fundo, a))
    c.drawRRect(r, M.paint(borda, a, stroke=4))
    centro(c, ch, cx, cy + s * 0.22, s * 0.6, "g", tinta, a)


# ---------------- peças desta aula ----------------
def decisao(c, t, t0, escolha=None, te=None, n=None):
    """faixa do alto: o número da situação à esquerda e as 4 escolhas à direita; em te a escolhida acende"""
    if n is not None:
        E.foco(c, t, t0, 0.4, lambda a: E.pilula(c, f"situação {n}", XE + 130, 105, 40, estilo="g", fundo=TINTA2, a=a))
    xs = (870, 1140, 1390, 1630)
    for i, (op, x) in enumerate(zip(OPCOES, xs)):
        q = ep(t, te, 0.4) if (te is not None and escolha is not None) else 0.0
        if op == escolha:
            fundo, alfa = M.mix(TINTA2, E.COR, q), 1.0
        else:
            fundo, alfa = TINTA2, 1 - 0.65 * q
        E.foco(c, t, t0 + 0.08 * i, 0.4, lambda a, op=op, x=x, fundo=fundo, alfa=alfa: E.pilula(c, op, x, 105, 38, estilo="b", fundo=fundo, a=a * alfa))


def enunciado(c, t, C, k, n, linhas, relogio):
    """tela de pergunta: 'situação n' grande e o texto em linhas [(t0, partes)], relógio de pausa à direita"""
    E.frase(c, t, C[k + ".a"], [("situação", "i", 80, COR)], XE, 250)
    E.foco(c, t, C[k + ".a"] + 0.3, 0.5, lambda a: (E.bola(c, XE + 370, 222, 60, a=a), centro(c, str(n), XE + 370, 247, 72, "g", BR, a)))
    for i, (t0, partes) in enumerate(linhas):
        E.frase(c, t, t0, partes, XE, 420 + i * 120, passo=0.12)
    E.relogio(c, t, relogio, 1500, 600, 190)


def questao_n(c, x, y, s, n, estado, a=1.0):
    """quadradinho numerado de uma questão da prova. estado: 'livre', 'dentro' (cheio), 'escolhe' (cor), 'fora' (vermelho)"""
    if a <= 0:
        return
    r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x - s / 2, y - s / 2, s, s), s * 0.18, s * 0.18)
    fundo = {"livre": BR, "dentro": TINTA, "escolhe": E.COR, "fora": ERRADO}[estado]
    c.drawRRect(r, M.paint(fundo, a))
    c.drawRRect(r, M.paint(TINTA if estado == "livre" else fundo, a, stroke=4))
    centro(c, str(n), x, y + s * 0.2, s * 0.52, "g", TINTA if estado == "livre" else BR, a)


FRUTAS = ("#E9C846", "#D94B3D", "#F08C2E", "#7CB342", "#8E5BD9", "#E86A92", "#4FA3C7")


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    E.frase(c, t, C["s01.a"], [("5", "g", 140, COR), ("situações", "g", 140)], W / 2, 270, "center")
    E.frase(c, t, C["s01.a"] + 1.0, ps("a decisão vem antes da conta", "i", 72, TINTA2), W / 2, 390, "center", passo=0.12)
    for i, op in enumerate(OPCOES):
        x = W / 2 + (i - 1.5) * 380
        E.foco(c, t, C["s01.b"] + 0.35 * i, 0.4, lambda a, op=op, x=x: E.pilula(c, op + ("?" if op == "combino" else ""), x, 540, 60, estilo="g", a=a))
    E.relogio(c, t, C["s01.c"], W / 2, 780, 90)


# ---------------- lembrete ----------------
LINHAS_T = (("s02.b", "etapas de coisas diferentes?", "multiplico", "casinhas"),
            ("s02.c", "todos entram em fila?", "permuto", "n!"),
            ("s02.d", "só alguns, e a ordem muda?", "arranjo", "desce do total"),
            ("s02.e", "só alguns, e a ordem não muda?", "combino", "arranjo ÷ p!"))


def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s02.a"], [("antes", "i", 80), ("da", "i", 80), ("conta,", "i", 80), ("o", "i", 80), ("teste", "g", 84, COR)], W / 2, 180, "center")
    for i, (k, perg, op, dica) in enumerate(LINHAS_T):
        y = 340 + i * 160
        E.frase(c, t, C[k] - 1.2, ps(perg, "i", 58), XE, y + 20, passo=0.08)
        E.foco(c, t, C[k], 0.45, lambda a, op=op, y=y: E.pilula(c, op, 1200, y, 50, estilo="g", a=a))
        E.foco(c, t, C[k] + 0.3, 0.45, lambda a, dica=dica, y=y: E.formula(c, dica, 1390, y + 18, 50, "b", TINTA2, a))
    E.frase(c, t, lerp(C["s02.e"], C["s02.end"], 0.5), ps("travou? procure a aula no canal", "i", 50, TINTA2), W / 2, 1010, "center", passo=0.1)


# ---------------- situação 1 ----------------
def b_questao1(c, t, C, b):
    enunciado(c, t, C, "s03", 1, [(C["s03.b"], [("quantos", "i", 76), ("números", "i", 76), ("de", "i", 76), ("4", "g", 84, COR), ("algarismos", "i", 76)]),
                                  (C["s03.b"] + 1.0, [("diferentes", "g", 84)]),
                                  (C["s03.b"] + 1.5, [("são", "i", 76), ("ímpares?", "g", 84, COR)])], C["s04.a"])


NOMES4 = ("milhar", "centena", "dezena", "unidade")


def b_resposta1(c, t, C, b):
    decisao(c, t, C["s05"], "multiplico", C["s05"] + 1.0, n=1)
    y, s = 440, 170
    tv = (C["s06.b"], C["s06.c"], C["s06.d"], C["s05.c"])
    xs = casinhas(c, t, 860, y, [(n_, v, C["s05"] + 0.8 + 0.1 * i, tv[i]) for i, (n_, v) in enumerate(zip(NOMES4, (8, 8, 7, 5)))], s=s, gap=90,
                  tx=[C["s06.e"] + 0.6, C["s06.f"], C["s06.g"]])
    for i in range(4):
        if t < tv[i]:
            E.foco(c, t, C["s05"] + 0.9 + 0.1 * i, 0.4, lambda a, x=xs[i]: E.formula(c, "?", x, y + 34, 96, "g", CINZA, a, "center"))
    marca(c, t, C["s05.a"], xs[3], y, s, C["s06.a"] - 0.2, COR)
    marca(c, t, C["s06.a"], xs[0], y, s, C["s06.c"] - 0.2, COR)
    ordem(c, t, C["s05.a"] + 0.2, xs[3], y, s, 1)
    ordem(c, t, C["s06.a"] + 0.2, xs[0], y, s, 2)
    ordem(c, t, C["s06.c"], xs[1], y, s, 3)
    ordem(c, t, C["s06.d"], xs[2], y, s, 4)
    yr = y - s / 2 - 62
    E.frase(c, t, C["s05.b"], [("1,", "g", 40, COR), ("3,", "g", 40, COR), ("5,", "g", 40, COR), ("7", "g", 40, COR), ("ou", "i", 38), ("9", "g", 40, COR)],
            xs[3], yr + 14, "center", passo=0.38)
    regra(c, t, C["s06.b"] - 0.6, xs[0], yr, "sem 0 e sem a unidade", fundo=ERRADO, size=32)
    regra(c, t, C["s06.c"] - 0.6, (xs[1] + xs[2]) / 2, yr, "sem os já usados", size=32)
    E.formula_em(c, t, C["s06.e"], "5 × 8 = 40", 240, 770, 84, "g", TINTA)
    E.formula_em(c, t, C["s06.f"], "40 × 8 = 320", 820, 770, 84, "g", TINTA)
    E.formula_em(c, t, C["s06.g"], "320 × 7", 240, 935, 96, "g", TINTA)
    igual_bola(c, t, C["s06.g"] + 0.4, 690, 900, "2.240", r=105, cor=CERTO)
    E.foco(c, t, C["s06.h"], 0.5, lambda a: E.pilula(c, "pela frente, a unidade trava", 1380, 910, 40, estilo="b", fundo=ERRADO, a=a))


# ---------------- situação 2 ----------------
def b_questao2(c, t, C, b):
    enunciado(c, t, C, "s07", 2, [(C["s07.b"], [("quantos", "i", 76), ("anagramas", "g", 84)]),
                                  (C["s07.b"] + 0.8, [("de", "i", 76), ("PRATO", "g", 84, COR)]),
                                  (C["s07.b"] + 1.4, [("começam", "i", 76), ("com", "i", 76), ("vogal?", "g", 84, COR)])], C["s08.a"])


def b_resposta2(c, t, C, b):
    decisao(c, t, C["s09"], "permuto", C["s09.a"], n=2)
    for i, ch in enumerate("PRATO"):
        voga = ch in "AO" and t >= C["s09.c"]
        E.foco(c, t, C["s09.b"] + 0.3 * i, 0.4, lambda a, i=i, ch=ch, voga=voga: letra(c, W / 2 + (i - 2) * 130, 270, 105, ch, a,
                                                                                    E.COR if voga else BR, BR if voga else TINTA))
    y, s = 560, 150
    tv = [C["s09.c"] + 0.4] + [C["s09.d"] - 0.6 + 0.15 * i for i in range(4)]
    xs = casinhas(c, t, 820, y, [("", v, C["s09.c"] - 0.4 + 0.08 * i, tv[i]) for i, v in enumerate((2, 4, 3, 2, 1))], s=s, gap=70,
                  tx=[C["s09.e"] - 0.2, C["s09.d"], C["s09.d"], C["s09.d"]])
    regra(c, t, C["s09.c"], xs[0], y - s / 2 - 48, "A ou O", fundo=E.COR, size=36)
    if t >= C["s09.d"]:
        E.chave(c, xs[1] - s / 2, xs[4] + s / 2, y + s / 2 + 30, COR, ep(t, C["s09.d"], 0.5))
        E.formula_em(c, t, C["s09.d"] + 0.3, "4! = 24", (xs[1] + xs[4]) / 2, y + s / 2 + 130, 72, "g", COR, "center")
    E.formula_em(c, t, C["s09.e"], "2 × 24", 240, 930, 96, "g", TINTA)
    igual_bola(c, t, C["s09.e"] + 0.4, 600, 895, "48", r=95, cor=CERTO)
    E.foco(c, t, C["s09.f"], 0.5, lambda a: E.escreve(c, "sem a regra: 5! = 120", 1080, 920, 56, "b", TINTA2, a))
    E.foco(c, t, C["s09.f"] + 1.6, 0.5, lambda a: E.escreve(c, "48 é menor: bateu", 1080, 1000, 50, "i", CERTO, a))


# ---------------- situação 3 ----------------
AZUL, VERDE = "#3D7DD8", "#2FA84F"


def b_questao3(c, t, C, b):
    enunciado(c, t, C, "s10", 3, [(C["s10.b"], [("campeonato", "i", 76), ("com", "i", 76), ("12", "g", 84, COR), ("times", "i", 76)]),
                                  (C["s10.c"], [("quantas", "i", 76), ("possibilidades", "i", 76)]),
                                  (C["s10.c"] + 0.8, [("para", "i", 76), ("campeão", "g", 84, COR), ("e", "i", 76), ("vice?", "g", 84, COR)])], C["s11.a"])


def time_linha(c, x, y, campeao, vice, a=1.0):
    for i, (cargo, (nome, cor)) in enumerate((("campeão", campeao), ("vice", vice))):
        yy = y + i * 90
        E.escreve(c, cargo, x, yy, 50, "i", TINTA2, a)
        E.escreve(c, nome, x + 230, yy, 58, "g", cor, a)


def b_resposta3(c, t, C, b):
    decisao(c, t, C["s12"], "arranjo", C["s12.b"], n=3)

    def troca():
        E.foco(c, t, C["s12.a"], 0.5, lambda a: time_linha(c, 300, 330, ("Azul", AZUL), ("Verde", VERDE), a))
        E.foco(c, t, C["s12.a"] + 1.2, 0.5, lambda a: time_linha(c, 1150, 330, ("Verde", VERDE), ("Azul", AZUL), a))
        E.sinal(c, t, C["s12.a"] + 1.6, "≠", 960, 350, 120, ERRADO)
        E.foco(c, t, C["s12.b"], 0.5, lambda a: E.pilula(c, "a ordem importa", W / 2, 560, 50, estilo="g", fundo=CERTO, a=a))
        xs = casinhas(c, t, 640, 790, [("campeão", 12, C["s12.c"], C["s12.c"] + 0.2), ("vice", 11, C["s12.c"] + 0.15, C["s12.c"] + 0.5)], s=160, gap=100)
        igual_bola(c, t, C["s12.c"] + 1.0, xs[1] + 140, 790, "132", r=100, cor=CERTO)
    E.saida(c, t, C["s13"] - 0.1, troca)
    if t < C["s13"]:
        return
    E.foco(c, t, C["s13"] + 0.1, 0.5, lambda a: E.escreve(c, "como combinação:", 240, 330, 60, "i", TINTA2, a))
    E.formula_em(c, t, C["s13.a"] - 0.8, "132 ÷ 2", 240, 480, 104, "g", ERRADO)
    igual_bola(c, t, C["s13.a"], 680, 445, "66", r=90, cor=ERRADO)
    E.frase(c, t, C["s13.b"], ps("só diz quais times chegam à final", "i", 60), 1000, 470, passo=0.1)
    E.foco(c, t, C["s13.b"] + 1.6, 0.5, lambda a: E.escreve(c, "sem dizer quem ganhou", 1000, 550, 52, "b", ERRADO, a))
    for i, (txt, cor) in enumerate((("campeão", "#E2B33C"), ("vice", "#A7ADB8"))):
        x = 620 + i * 680
        E.foco(c, t, C["s13.c"] + 0.3 * i, 0.5, lambda a, x=x, txt=txt, cor=cor: (c.drawCircle(x - 170, 800, 60, M.paint(cor, a)),
                                                                             centro(c, "1" if txt == "campeão" else "2", x - 170, 825, 70, "g", BR, a),
                                                                             E.escreve(c, txt, x - 80, 822, 72, "g", TINTA, a)))
    E.foco(c, t, C["s13.c"] + 0.8, 0.5, lambda a: E.centro(c, "lugares diferentes, como ouro e prata", W / 2, 980, 56, "i", TINTA2, a))


# ---------------- situação 4 ----------------
def b_questao4(c, t, C, b):
    enunciado(c, t, C, "s14", 4, [(C["s14.b"], [("salada", "i", 76), ("com", "i", 76), ("4", "g", 84, COR), ("frutas", "i", 76), ("diferentes", "i", 76)]),
                                  (C["s14.c"], [("entre", "i", 76), ("7", "g", 84, COR), ("frutas", "i", 76)]),
                                  (C["s14.d"], [("quantas", "i", 76), ("saladas?", "g", 84, COR)])], C["s15.a"])
    for i, cor in enumerate(FRUTAS):
        E.foco(c, t, C["s14.c"] + 0.08 * i, 0.4, lambda a, i=i, cor=cor: E.bola(c, XE + 40 + i * 95, 880, 36, cor, a))


def b_resposta4(c, t, C, b):
    decisao(c, t, C["s16"], "combino", C["s16.a"], n=4)
    E.foco(c, t, C["s16"] + 0.3, 0.5, lambda a: E.escreve(c, "banana + maçã = maçã + banana", 240, 270, 52, "i", TINTA2, a))
    y = 430
    for i, cor in enumerate(FRUTAS):
        x = 330 + i * 140
        fora = i >= 4 and t >= C["s16.b"]
        E.foco(c, t, C["s16"] + 0.5 + 0.06 * i, 0.4, lambda a, x=x, cor=cor, fora=fora: E.bola(c, x, y, 50, cor, a * (0.35 if fora else 1.0)))
    if t >= C["s16.b"]:
        E.foco(c, t, C["s16.b"], 0.5, lambda a: bloco(c, 330 - 50, 330 + 3 * 140 + 50, y, 100, a))
        E.foco(c, t, C["s16.b"] + 0.3, 0.5, lambda a: E.centro(c, "4 entram", 330 + 1.5 * 140, y + 130, 46, "b", COR, a))
        E.foco(c, t, C["s16.b"] + 0.6, 0.5, lambda a: E.centro(c, "3 de fora", 330 + 5 * 140, y + 130, 46, "b", ERRADO, a))
    E.foco(c, t, C["s16.c"] - 0.3, 0.4, lambda a: E.escreve(c, "atalho:", 240, 700, 52, "i", COR, a))
    E.formula_em(c, t, C["s16.c"], "f{7 × 6 × 5}{3!} = f{210}{6}", 480, 700, 72, "g", TINTA)
    igual_bola(c, t, C["s16.d"], 1100, 680, "35", r=85, cor=CERTO)
    E.foco(c, t, C["s16.e"], 0.4, lambda a: E.escreve(c, "direto:", 240, 920, 52, "i", TINTA2, a))
    E.formula_em(c, t, C["s16.e"] + 0.3, "f{7 × 6 × 5 × 4}{4!} = f{840}{24}", 480, 920, 72, "g", TINTA2)
    bx = igual_bola(c, t, C["s16.f"], 1100, 900, "35", r=75, cor=CERTO)
    E.foco(c, t, C["s16.f"] + 0.6, 0.5, lambda a: E.escreve(c, "mesma resposta, conta maior", bx + 100, 920, 50, "i", TINTA2, a))


# ---------------- situação 5 ----------------
def b_questao5(c, t, C, b):
    enunciado(c, t, C, "s17", 5, [(C["s17.b"], [("prova", "i", 72), ("com", "i", 72), ("10", "g", 80, COR), ("questões:", "i", 72),
                                                ("escolha", "i", 72), ("7", "g", 80, COR)]),
                                  (C["s17.d"], [("a", "i", 72), ("1ª", "g", 80, COR), ("e", "i", 72), ("a", "i", 72), ("2ª", "g", 80, COR),
                                                ("são", "i", 72), ("obrigatórias", "g", 76)]),
                                  (C["s17.e"], [("de", "i", 72), ("quantos", "i", 72), ("jeitos?", "g", 80, COR)])], C["s18.a"])
    for i in range(10):
        est = "dentro" if (i < 2 and t >= C["s17.d"]) else "livre"
        E.foco(c, t, C["s17.b"] + 0.06 * i, 0.4, lambda a, i=i, est=est: questao_n(c, XE + 45 + i * 105, 860, 85, i + 1, est, a))


def b_resposta5(c, t, C, b):
    decisao(c, t, C["s19"], "combino", C["s19.a"], n=5)

    def certo():
        y = 330
        for i in range(10):
            est = "dentro" if (i < 2 and t >= C["s19.b"]) else ("escolhe" if (i >= 2 and t >= C["s19.c"]) else "livre")
            E.foco(c, t, C["s19"] + 0.4 + 0.05 * i, 0.4, lambda a, i=i, est=est: questao_n(c, 400 + i * 125, y, 100, i + 1, est, a))
        E.foco(c, t, C["s19.b"] + 0.2, 0.5, lambda a: E.centro(c, "já dentro", 462, y + 110, 46, "b", TINTA, a))
        E.foco(c, t, C["s19.c"] + 0.2, 0.5, lambda a: E.centro(c, "5 entre as 8 restantes", 400 + 5.5 * 125, y + 110, 46, "b", COR, a))
        E.foco(c, t, C["s19.d"] - 1.4, 0.5, lambda a: E.escreve(c, "= deixar 3 de fora", 240, 580, 52, "i", TINTA2, a))
        E.formula_em(c, t, C["s19.d"], "8 × 7 × 6 = 336", 240, 720, 80, "g", TINTA)
        E.formula_em(c, t, C["s19.e"], "f{336}{3!}", 240, 900, 90, "g", TINTA)
        igual_bola(c, t, C["s19.e"] + 0.4, 420, 885, "56", r=90, cor=CERTO)
    E.saida(c, t, C["s20"] - 0.1, certo)
    if t < C["s20"]:
        return
    E.frase(c, t, C["s20"] + 0.1, [("quem", "i", 72), ("esquece", "i", 72), ("a", "i", 72), ("regra", "g", 76, ERRADO)], W / 2, 270, "center")
    E.formula_em(c, t, C["s20.a"], "7 entre 10", 260, 450, 84, "g", ERRADO)
    igual_bola(c, t, C["s20.b"], 760, 420, "120", r=85, cor=ERRADO)
    y = 640
    padrao = [False, True, True, True, True, True, True, True, False, False]  # deixa a 1ª de fora
    for i in range(10):
        est = ("escolhe" if padrao[i] else ("fora" if i == 0 else "livre"))
        E.foco(c, t, C["s20.c"] + 0.05 * i, 0.4, lambda a, i=i, est=est: questao_n(c, 400 + i * 125, y, 100, i + 1, est, a))
    E.foco(c, t, C["s20.c"] + 0.7, 0.5, lambda a: E.centro(c, "deixou a 1ª de fora: não vale", 600, y + 110, 46, "b", ERRADO, a))
    E.foco(c, t, C["s20.d"], 0.5, lambda a: E.pilula(c, "coloque dentro primeiro e escolha só o resto", W / 2, 920, 50, estilo="g", fundo=CERTO, a=a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s21"], [("resumindo", "i", 92, COR)], W / 2, 210, "center")
        for i, (k, l1, l2) in enumerate((("s21.a", "antes da conta, decida:", "etapas, fila, ordem importa ou não"),
                                         ("s21.b", "tem regra?", "comece por ela"))):
            y = 430 + i * 260
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 300, y + 10, 56, a=a), centro(c, str(i + 1), 300, y + 33, 64, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, ps(l1, "i", 68), 400, y - 10, passo=0.1)
            E.frase(c, t, C[k] + 0.6, [(l2, "g", 80, COR)], 400, y + 95)
    E.saida(c, t, C["s22"] - 0.1, resumo)
    if t < C["s22"]:
        return
    E.frase(c, t, C["s22"] + 0.1, ps("próxima aula: assunto novo", "i", 80), XE, 300)
    E.frase(c, t, C["s22.a"], [("probabilidade", "g", 120, COR)], XE, 450)
    E.frase(c, t, C["s22.b"], [("a", "i", 64), ("chance", "g", 68), ("de", "i", 64), ("sair", "i", 64), ("par", "g", 68, COR), ("num", "i", 64),
                               ("dado", "g", 68)], XE, 590, passo=0.12)
    E.frase(c, t, C["s22.b"] + 1.6, ps("em fração e em porcentagem", "i", 64, TINTA2), XE, 690, passo=0.12)
    E.foco(c, t, C["s22.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1480, 330, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s22.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1810, 1610, p), lerp(650, 355, p), ep(t, C["s22.c"] + 0.2, 0.4))
    E.frase(c, t, C["s22.d"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 960, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, questao1=b_questao1, resposta1=b_resposta1, questao2=b_questao2, resposta2=b_resposta2,
              questao3=b_questao3, resposta3=b_resposta3, questao4=b_questao4, resposta4=b_resposta4, questao5=b_questao5, resposta5=b_resposta5,
              fim=b_fim)
