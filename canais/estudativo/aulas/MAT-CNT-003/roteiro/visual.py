"""Visual — Estudativo · MAT-CNT-003: contar os divisores de um número.
Mesma linguagem da trilha Contagem e Probabilidade (MAT-CNT-001 e 002): casinhas() com o número de opções dentro, × entre elas,
igual_bola() com o resultado. Peças desta aula:
- cadeiras(): as 72 cadeiras que se rearrumam em fileiras iguais (1 × 72, 2 × 36, 3 × 24, 4 × 18).
- fatores(): os pedaços da fatoração (2 2 2 3 3) em fichas, que o divisor pode pegar.
- grade_div(): a tabela de divisores, linha × coluna, com cabeçalhos na cor da matéria e destaque por célula.
A fatoração usa E.montar e E.tabela (divisões sucessivas, como em MAT-DIV-003).
Sem voz ainda: todo instante vem de C[...] (cenas e marcadores), nunca de segundos fixos."""
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro, montar, tabela, seta_primo
import motor as M
import skia

E.usar("Matemática", "Contagem e Probabilidade")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-CNT-003_contar_divisores.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("fatorar", "ideia", "tabela", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
DIV72 = [d for d in range(1, 73) if 72 % d == 0]
assert len(DIV72) == 12 and 2 ** 3 * 3 ** 2 == 72 and 8 * 9 == 72 and 4 * 3 == 12 and 12 - 3 == 9
assert 2 ** 3 * 3 ** 2 * 5 == 360 and len([d for d in range(1, 361) if 360 % d == 0]) == 24 == 4 * 3 * 2
assert [d for d in range(1, 361, 2) if 360 % d == 0] == [1, 3, 5, 9, 15, 45]
T72 = montar([72], [2, 2, 2, 3, 3])
G72 = dict(xs=(380,), xb=540, xp=640, y0=210, dy=128, s=96)  # tabela de uma coluna, 6 linhas
LIN, COL = (1, 2, 4, 8), (1, 3, 9)
assert sorted(a * b for a in LIN for b in COL) == DIV72


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


def regra(c, t, t0, x, y, txt, fundo=None, size=40, t1=None):
    """pílula com a restrição, centrada em (x, y)"""
    f = lambda: E.foco(c, t, t0, 0.45, lambda a: E.pilula(c, txt, x, y, size, estilo="b", fundo=fundo or TINTA2, a=a))
    E.saida(c, t, t1, f) if t1 is not None else f()


# ---------------- peças desta aula ----------------
def cadeiras(c, t, fases, cx, cy, wmax=1560, hmax=420, a=1.0):
    """72 cadeiras em fileiras iguais. fases = [(instante, fileiras)]: em cada instante, rearrumam em 'fileiras' linhas"""
    if a <= 0:
        return
    atual, ant, q = fases[0][1], fases[0][1], 1.0
    for ti, f in fases:
        if t >= ti:
            ant, atual = atual, f
            q = ease_io(prog(t, ti, 0.7))

    def lugar(f, i):
        cols = 72 // f
        cel = min(wmax / cols, hmax / f, 64)
        r, k = divmod(i, cols)
        return cx + (k - (cols - 1) / 2) * cel, cy + (r - (f - 1) / 2) * cel, cel
    for i in range(72):
        x0, y0, c0 = lugar(ant, i)
        x1, y1, c1 = lugar(atual, i)
        x, y, cel = lerp(x0, x1, q), lerp(y0, y1, q), lerp(c0, c1, q)
        lado = cel * 0.72
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x - lado / 2, y - lado / 2, lado, lado), lado * 0.22, lado * 0.22), M.paint(COR, a))


def ficha(c, cx, cy, n, a=1.0, cor=None, k=1.0, risco=False):
    """um fator primo numa ficha redonda"""
    if a <= 0 or k <= 0:
        return
    cor = cor or (E.COR if n == 2 else TINTA)
    r = 62 * k
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - r, cy - r, 2 * r, 2 * r), 26 * k, 26 * k), M.paint(cor, a))
    centro(c, str(n), cx, cy + 30 * k, 84 * k, "g", BR, a)
    if risco:
        M.line(c, cx - r - 10, cy + r + 10, cx + r + 10, cy - r - 10, ERRADO, a, 12)


def grade_div(c, t, x, y, cel, tl, tc, tcel, cores=None, apaga=None, size=None, cab=True):
    """tabela de divisores: linhas 1, 2, 4, 8 (fator 2) e colunas 1, 3, 9 (fator 3). (x, y) = canto da primeira célula.
    tl / tc = instante dos cabeçalhos de linha / coluna; tcel(i, j) = instante de cada célula.
    cores = {(i, j): cor de fundo}; apaga = {(i, j): opacidade}. Devolve o centro de cada célula."""
    size = size or cel * 0.42
    cores, apaga = cores or {}, apaga or {}
    centros = {}
    if cab:
        for i, v in enumerate(LIN):
            E.foco(c, t, tl + 0.25 * i, 0.4, lambda a, i=i, v=v: centro(c, str(v), x - cel * 0.55, y + cel * (i + 0.5) + size * 0.36, size, "g", COR, a))
        for j, v in enumerate(COL):
            E.foco(c, t, tc + 0.25 * j, 0.4, lambda a, j=j, v=v: centro(c, str(v), x + cel * (j + 0.5), y - cel * 0.3, size, "g", COR, a))
        E.foco(c, t, tc, 0.4, lambda a: centro(c, "×", x - cel * 0.55, y - cel * 0.3, size * 0.8, "b", CINZA, a))
    for i, a_ in enumerate(LIN):
        for j, b_ in enumerate(COL):
            cx, cy = x + cel * (j + 0.5), y + cel * (i + 0.5)
            centros[(i, j)] = (cx, cy)
            fundo = cores.get((i, j))
            op = apaga.get((i, j), 1.0)

            def f(a, cx=cx, cy=cy, v=a_ * b_, fundo=fundo, op=op):
                m = cel * 0.06
                r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - cel / 2 + m, cy - cel / 2 + m, cel - 2 * m, cel - 2 * m), cel * 0.12, cel * 0.12)
                c.drawRRect(r, M.paint(fundo or BR, a * op))
                c.drawRRect(r, M.paint(TINTA if not fundo else fundo, a * op, stroke=3))
                centro(c, str(v), cx, cy + size * 0.36, size, "g", BR if fundo else TINTA, a * op)
            E.foco(c, t, tcel(i, j), 0.4, f)
    return centros


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def cena():
        E.frase(c, t, C["s01.a"], [("72", "g", 96, COR), ("cadeiras", "i", 96)], W / 2, 200, "center")
        E.frase(c, t, C["s01.b"], ps("em fileiras iguais", "i", 72, TINTA2), W / 2, 300, "center")
        b_, c_ = C["s01.b"], C["s01.c"]
        fases = [(b_ + (c_ - b_) * k / 4, f) for k, f in enumerate((1, 2, 3, 4))]
        E.foco(c, t, C["s01.a"] + 0.3, 0.6, lambda a: cadeiras(c, t, fases, W / 2, 580, a=a))
        # o rótulo da arrumação da vez
        for k, (ti, f) in enumerate(fases):
            t1 = fases[k + 1][0] if k + 1 < len(fases) else C["s01.c"] + 0.2
            if ti <= t < t1 + 0.4:
                E.saida(c, t, t1, lambda f=f, ti=ti: E.foco(c, t, ti + 0.3, 0.4, lambda a: E.centro(
                    c, f"{f} fileira{'s' if f > 1 else ''} de {72 // f}", W / 2, 900, 64, "b", TINTA, a)), d=0.3)
        E.frase(c, t, C["s01.c"], [("cada", "i", 72), ("jeito", "i", 72), ("=", "g", 64), ("um", "i", 72), ("divisor", "g", 72, COR), ("de", "i", 72),
                                   ("72", "g", 72, COR)], W / 2, 900, "center")
        E.frase(c, t, C["s01.d"], [("sem", "i", 72), ("listar", "g", 72, COR)], W / 2, 1010, "center")
    E.saida(c, t, C["s02"] - 0.1, cena)

    if t >= C["s02"]:
        E.foco(c, t, C["s02.b"] - 0.2, 0.7, lambda a: E.bola(c, 1450, 520, 300 * ease_back(prog(t, C["s02.b"] - 0.2, 0.7))), blur=0)
        E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 96), XE, 330)
        E.frase(c, t, C["s02.a"] + 0.9, [("contar", "g", 132)], XE, 480)
        E.frase(c, t, C["s02.a"] + 1.2, [("divisores", "g", 132, COR)], XE, 630)
        E.frase(c, t, C["s02.a"] + 1.8, ps("de qualquer número", "i", 96), XE, 780)
        E.foco(c, t, C["s02.b"] + 0.2, 0.5, lambda a: (E.escreve(c, "+ atalho", 1290, 505, 84, "g", BR, a),
                                                      E.escreve(c, "de prova", 1310, 590, 84, "i", BR, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], ps("você vai precisar de", "i", 84), XE, 410)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "3", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 900, 860
    itens = (("s03.b", "fatorar com potências", "72 = 2^3 · 3^2"), ("s03.c", "princípio multiplicativo", "4 × 3 = 12"), ("s03.d", "expoente zero", "2^0 = 1"))
    for i, (k, l1, f) in enumerate(itens):
        y = 190 + i * 240
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 196, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 60)], x + 44, y + 80)
        E.formula_em(c, t, C[k] + 0.3, f, x + 44, y + 165, 64, "g", COR)


# ---------------- fatorar ----------------
def b_fatorar(c, t, C, b):
    a_ = C["s04.a"]
    marcos = [C["s04.a"], C["s04.b"], C["s04.c"], C["s04.d"], C["s04.e"]]
    tn = [[C["s04"] + 0.1]] + [[m + 0.3] for m in marcos]
    tn[1] = [lerp(C["s04.a"], C["s04.b"], 0.75)]
    tp = [a_] + [m - 0.4 for m in marcos[1:]]
    tb = [a_] + marcos[1:]
    tabela(c, t, T72, tn, tp, tb, G72, cor_fim=CERTO if t >= C["s04.e"] + 0.4 else None)
    ti = tp + [C["s04.e"] + 0.8]
    for i in range(5):
        seta_primo(c, t, ti[i], ti[i + 1], i, G72)
    E.frase(c, t, C["s04"], [("primeiro,", "i", 84), ("fatore", "g", 84, COR)], 1000, 230)
    # a conta de cada passo, ao lado
    contas = ("72 ÷ 2 = 36", "36 ÷ 2 = 18", "18 ÷ 2 = 9", "9 ÷ 3 = 3", "3 ÷ 3 = 1")
    for i, s in enumerate(contas):
        t0 = tn[i + 1][0] - 0.2
        t1 = tn[i + 2][0] - 0.3 if i < 4 else C["s05"] - 0.1
        if t0 <= t < t1 + 0.4:
            E.saida(c, t, t1, lambda s=s, t0=t0: E.formula_em(c, t, t0, s, 1000, 450, 96, "g", TINTA), d=0.3)
    E.saida(c, t, C["s05.a"] - 0.1, lambda: (E.formula_em(c, t, C["s04.e"] + 1.0, "8 × 9 = 72", 1000, 680, 80, "b", TINTA2),
                                             E.foco(c, t, C["s04.e"] + 1.0, 0.4, lambda a: E.escreve(c, "conferindo:", 1000, 590, 56, "i", TINTA2, a))))
    if t < C["s05"]:
        return
    # três divisões por 2, duas por 3
    p = ep(t, C["s05.a"], 0.5)
    s = G72["s"]
    E.caixa_pontilhada(c, G72["xp"] - s * 0.6, G72["y0"] - s * 0.9, s * 1.2, G72["dy"] * 2 + s * 1.15, p, E.COR, p)
    E.caixa_pontilhada(c, G72["xp"] - s * 0.6, G72["y0"] + 3 * G72["dy"] - s * 0.9, s * 1.2, G72["dy"] + s * 1.15, ep(t, C["s05.a"] + 0.6, 0.5), TINTA,
                       ep(t, C["s05.a"] + 0.6, 0.5))
    E.foco(c, t, C["s05.a"], 0.5, lambda a: E.escreve(c, "3 vezes o 2", 760, G72["y0"] + G72["dy"] + 30, 52, "b", COR, a))
    E.foco(c, t, C["s05.a"] + 0.6, 0.5, lambda a: E.escreve(c, "2 vezes o 3", 760, G72["y0"] + 3.5 * G72["dy"] + 30, 52, "b", TINTA, a))
    E.formula_em(c, t, C["s05.b"], "72 = 2^3 · 3^2", 1430, 920, 120, "g", COR, "center")


# ---------------- a ideia ----------------
def b_ideia(c, t, C, b):
    def pedacos():
        E.frase(c, t, C["s06.a"], [("o", "i", 84), ("que", "i", 84), ("é", "i", 84), ("um", "i", 84), ("divisor", "g", 84, COR), ("de", "i", 84),
                                   ("72?", "g", 84, COR)], W / 2, 190, "center")
        E.frase(c, t, C["s06.b"], ps("montado só com pedaços de", "i", 64, TINTA2), W / 2, 310, "center")
        xs = [520, 700, 880, 1100, 1280]
        for i, (x, n) in enumerate(zip(xs, (2, 2, 2, 3, 3))):
            E.foco(c, t, C["s06.b"] + 0.5 + 0.15 * i, 0.45, lambda a, x=x, n=n, i=i: ficha(c, x, 470, n, a * (0.35 if t >= C["s06.d"] + 2.2 and i not in (0, 3) else 1)))
        E.foco(c, t, C["s06.b"] + 0.5, 0.45, lambda a: E.escreve(c, "72 =", 190, 500, 96, "g", TINTA, a))
        for k, x in enumerate((610, 790, 990, 1190)):
            E.sinal(c, t, C["s06.b"] + 0.6 + 0.15 * k, "·", x, 470, 90)
        # nunca mais do que tem; nenhum outro primo
        E.foco(c, t, C["s06.c"], 0.5, lambda a: E.pilula(c, "no máximo três 2 e dois 3", 760, 640, 50, estilo="b", fundo=TINTA2, a=a))
        E.foco(c, t, C["s06.d"], 0.5, lambda a: ficha(c, 1580, 470, 5, a, CINZA, risco=True))
        E.foco(c, t, C["s06.d"] + 0.3, 0.5, lambda a: E.centro(c, "outro primo", 1580, 600, 48, "i", ERRADO, a))
        # o 6 usa um 2 e um 3
        E.formula_em(c, t, C["s06.d"] + 2.2, "6 = 2 · 3", W / 2, 860, 120, "g", COR, "center")
    E.saida(c, t, C["s07"] - 0.1, pedacos)
    if t < C["s07"]:
        return

    def opcoes():
        E.frase(c, t, C["s07"], [("quantas", "i", 72), ("vezes", "i", 72), ("entra", "i", 72), ("cada", "i", 72), ("fator?", "g", 72, COR)],
                W / 2, 170, "center")
        # fator 2: 2^0 ... 2^3
        x2, x3, y0, dy = 300, 940, 330, 120
        E.foco(c, t, C["s07"] + 0.4, 0.5, lambda a: E.pilula(c, "fator 2", x2 + 120, 260, 44, estilo="b", a=a))
        for k in range(4):
            tk = C["s07.a"] + 0.45 * k
            E.formula_em(c, t, tk, f"2^{k}", x2, y0 + 100 + k * dy, 84, "g", TINTA)
            E.formula_em(c, t, C["s07.c"] + 0.4 * k, f"= {2 ** k}", x2 + 120, y0 + 100 + k * dy, 84, "g", COR)
        E.foco(c, t, C["s07.b"], 0.5, lambda a: E.escreve(c, "4 opções", x2 + 330, y0 + 100 + 1.5 * dy + 25, 60, "i", COR, a))
        if t >= C["s08"]:
            E.foco(c, t, C["s08"] + 0.2, 0.5, lambda a: E.pilula(c, "fator 3", x3 + 120, 260, 44, estilo="b", fundo=TINTA, a=a))
            for k in range(3):
                tk = C["s08.a"] + 0.45 * k
                E.formula_em(c, t, tk, f"3^{k}", x3, y0 + 100 + k * dy, 84, "g", TINTA)
                E.formula_em(c, t, C["s08.c"] + 0.4 * k, f"= {3 ** k}", x3 + 120, y0 + 100 + k * dy, 84, "g", TINTA)
            E.foco(c, t, C["s08.b"], 0.5, lambda a: E.escreve(c, "3 opções", x3 + 330, y0 + 100 + dy + 25, 60, "i", TINTA, a))
    E.saida(c, t, C["s09"] - 0.1, opcoes)
    if t < C["s09"]:
        return
    E.frase(c, t, C["s09"], ps("montar um divisor é escolher", "i", 72), W / 2, 220, "center")
    xs = casinhas(c, t, 760, 560, [("fator 2", 4, C["s09.a"], C["s09.a"] + 0.4), ("fator 3", 3, C["s09.a"] + 0.6, C["s09.a"] + 1.0)], s=210,
                  tx=[C["s09.b"] - 0.3])
    E.foco(c, t, C["s09.a"] + 0.4, 0.5, lambda a: E.centro(c, "1, 2, 4 ou 8", xs[0], 790, 44, "b", TINTA2, a))
    E.foco(c, t, C["s09.a"] + 1.0, 0.5, lambda a: E.centro(c, "1, 3 ou 9", xs[1], 790, 44, "b", TINTA2, a))
    bx = igual_bola(c, t, C["s09.b"], xs[1] + 200, 560, "12", r=130)
    E.frase(c, t, C["s09.b"] + 0.4, [("divisores", "g", 64, COR)], bx, 790, "center")


# ---------------- a tabela ----------------
def b_tabela(c, t, C, b):
    E.frase(c, t, C["s10"] + 0.1, [("veja", "i", 80), ("na", "i", 80), ("tabela", "g", 80, COR)], W / 2, 150, "center")
    x, y, cel = 640, 300, 175
    tc = C["s10.c"]
    tcel = lambda i, j: tc if (i, j) == (2, 1) else tc + 0.7 + 0.12 * (i * 3 + j)
    cores = {}
    if t >= C["s10.e"]:
        cores = {(0, 0): CERTO, (3, 2): CERTO}
    elif t >= C["s10.c"] and t < tc + 0.7:
        cores = {(2, 1): E.COR}
    centros = grade_div(c, t, x, y, cel, C["s10.a"], C["s10.b"], tcel, cores)
    # linha vezes coluna, no exemplo 4 × 3
    E.foco(c, t, tc, 0.5, lambda a: E.formula(c, "4 × 3 = 12", 1300, 560, 84, "g", COR, a))
    E.foco(c, t, tc, 0.5, lambda a: E.escreve(c, "linha × coluna", 1300, 450, 60, "i", TINTA2, a))
    E.foco(c, t, C["s10.d"], 0.5, lambda a: (E.bola(c, 1480, 820, 120, a=a), centro(c, "12", 1480, 820 + 32, 90, "g", BR, a)))
    E.foco(c, t, C["s10.d"] + 0.3, 0.5, lambda a: E.centro(c, "divisores", 1480, 1010, 60, "g", COR, a))
    E.foco(c, t, C["s10.e"], 0.5, lambda a: E.escreve(c, "do 1 ao 72", 1300, 680, 60, "i", CERTO, a))


# ---------------- a regra ----------------
def b_regra(c, t, C, b):
    def regra3():
        E.frase(c, t, C["s11"], [("a", "i", 96), ("regra", "g", 96, COR)], W / 2, 200, "center")
        E.passo(c, t, C["s11.a"], 1, "fatore usando", "potências", 380)
        E.passo(c, t, C["s11.b"], 2, "some 1 em", "cada expoente", 580)
        E.passo(c, t, C["s11.c"], 3, "multiplique", "os resultados", 780)
        E.foco(c, t, C["s11.d"], 0.5, lambda a: E.pilula(c, "+1 = a opção nenhuma vez", 1300, 580, 52, estilo="b", a=a))
        E.formula_em(c, t, C["s11.d"] + 0.4, "2^0 = 1", 1300, 760, 96, "g", TINTA, "center")
    E.saida(c, t, C["s12"] - 0.1, regra3)
    if t < C["s12"]:
        return
    E.formula_em(c, t, C["s12"] + 0.1, "72 = 2^3 · 3^2", W / 2, 300, 140, "g", TINTA, "center")
    # os expoentes acesos
    w72 = E.formula(None, "72 = 2", 0, 0, 140, a=0)
    wtot = E.formula(None, "72 = 2^3 · 3^2", 0, 0, 140, a=0)
    x0 = W / 2 - wtot / 2
    w3 = E.formula(None, "72 = 2^3 · 3", 0, 0, 140, a=0)
    for xx, k in ((x0 + w72, "s12.a"), (x0 + w3, "s12.a")):
        p = ep(t, C[k], 0.4)
        if p > 0:
            c.drawCircle(xx + 26, 300 - 75, 50 * p, M.paint(E.COR, 0.18))
    xs = casinhas(c, t, 760, 640, [("fator 2", 4, C["s12.b"] - 0.2, C["s12.b"] + 0.5), ("fator 3", 3, C["s12.c"] - 0.2, C["s12.c"] + 0.5)], s=200,
                  tx=[C["s12.d"] - 0.2])
    E.formula_em(c, t, C["s12.b"], "3 + 1", xs[0], 480, 60, "b", COR, "center")
    E.formula_em(c, t, C["s12.c"], "2 + 1", xs[1], 480, 60, "b", COR, "center")
    igual_bola(c, t, C["s12.d"], xs[1] + 190, 640, "12", r=125)
    E.frase(c, t, C["s12.d"] + 1.0, ps("sem tabela e sem lista", "i", 60, TINTA2), W / 2, 960, "center")


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s13"] + 0.1, [("cuidado", "g", 96, ERRADO), ("com", "i", 90), ("isto", "i", 90)], W / 2, 170, "center")
    E.frase(c, t, C["s13.a"], [("esqueceu", "i", 72), ("o", "i", 72), ("+1", "g", 72, ERRADO)], 330, 330)
    E.formula_em(c, t, C["s13.b"], "3 × 2 = 6", 330, 470, 110, "g", ERRADO)
    if t >= C["s13.b"] + 1.4:
        E.risco(c, 310, 430, 820, 430, t, C["s13.b"] + 1.4, largura=12)
    x, y, cel = 1060, 300, 150
    contados = {(i, j) for i in range(1, 4) for j in range(1, 3)}
    fora = [(i, j) for i in range(4) for j in range(3) if (i, j) not in contados]
    cores = {k: ERRADO for k in contados} if t < C["s13.c"] else {}
    for k in fora:
        i, j = k
        on = (i == 0 and j > 0 and t >= C["s13.c"]) or (j == 0 and i > 0 and t >= C["s13.d"]) or (k == (0, 0) and t >= C["s13.e"])
        if on:
            cores[k] = CERTO
    apaga = {k: 0.28 for k in fora if k not in cores} if t >= C["s13.b"] + 0.6 else {}
    tcel = lambda i, j: C["s13.b"] + 0.4 + 0.05 * (i * 3 + j)
    grade_div(c, t, x, y, cel, C["s13.b"] + 0.3, C["s13.b"] + 0.3, tcel, cores, apaga)
    E.foco(c, t, C["s13.b"] + 0.9, 0.5, lambda a: E.escreve(c, "só 6 contados", 330, 620, 56, "i", ERRADO, a))
    E.foco(c, t, C["s13.c"], 0.5, lambda a: E.escreve(c, "sem o fator 2: o 9", 330, 760, 56, "b", CERTO, a))
    E.foco(c, t, C["s13.d"], 0.5, lambda a: E.escreve(c, "sem o fator 3: o 8", 330, 850, 56, "b", CERTO, a))
    E.foco(c, t, C["s13.e"], 0.5, lambda a: E.escreve(c, "e até o 1", 330, 940, 56, "b", CERTO, a))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def impares():
        E.frase(c, t, C["s14.a"], [("só", "i", 84, CLARO), ("os", "i", 84, CLARO), ("ímpares", "g", 84, BR), ("ou", "i", 84, CLARO), ("só", "i", 84, CLARO),
                                   ("os", "i", 84, CLARO), ("pares", "g", 84, BR)], W / 2, 190, "center")
        E.formula_em(c, t, C["s14.a"] + 1.0, "72 = 2^3 · 3^2", W / 2, 400, 130, "g", BR, "center")
        if t >= C["s14.b"]:
            wtot = E.formula(None, "72 = 2^3 · 3^2", 0, 0, 130, a=0)
            x0 = W / 2 - wtot / 2 + E.formula(None, "72 = ", 0, 0, 130, a=0)
            x1 = W / 2 - wtot / 2 + E.formula(None, "72 = 2^3 ·", 0, 0, 130, a=0)
            E.risco(c, x0 - 10, 420, x1 - 20, 300, t, C["s14.b"], cor=ERRADO, largura=12)
            E.foco(c, t, C["s14.b"] + 0.2, 0.4, lambda a: E.centro(c, "ignore o 2", x0 + 70, 520, 52, "i", CLARO, a))
        xs = casinhas(c, t, 760, 730, [("fator 3", 3, C["s14.c"], C["s14.c"] + 0.3)], s=180, escuro=True)
        E.foco(c, t, C["s14.d"], 0.5, lambda a: E.escreve(c, "3 ímpares:", 980, 720, 72, "g", BR, a))
        E.foco(c, t, C["s14.d"] + 0.6, 0.5, lambda a: E.escreve(c, "1, 3 e 9", 980, 810, 72, "i", CLARO, a))
    E.saida(c, t, C["s15"] - 0.1, impares)
    if t < C["s15"]:
        return

    def pares():
        E.frase(c, t, C["s15"] + 0.1, [("e", "i", 84, CLARO), ("os", "i", 84, CLARO), ("pares?", "g", 84, BR)], W / 2, 210, "center")
        E.formula_em(c, t, C["s15.a"], "12 − 3", 760, 420, 130, "g", BR, "center")
        igual_bola(c, t, C["s15.a"] + 0.5, 1000, 375, "9", r=100, cor=E.COR, escuro=True)
        E.frase(c, t, C["s15.b"], [("todo", "i", 64, CLARO), ("divisor", "i", 64, CLARO), ("é", "i", 64, CLARO), ("par", "g", 64, BR), ("ou", "i", 64, CLARO),
                                   ("ímpar", "g", 64, BR)], W / 2, 620, "center")
    E.saida(c, t, C["s15.c"] - 0.1, pares)
    if t < C["s15.c"]:
        return
    E.foco(c, t, C["s15.c"], 0.5, lambda a: E.pilula(c, "quer os divisores escritos?", W / 2, 420, 56, estilo="b", fundo=ERRADO, a=a))
    E.frase(c, t, C["s15.d"], [("monte", "i", 96, CLARO), ("a", "i", 96, CLARO), ("tabela", "g", 96, BR)], W / 2, 640, "center")


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s16"] + 0.1, [("hora", "i", 72, COR), ("de", "i", 72, COR), ("testar", "i", 72, COR)], XE, 190)
    E.formula_em(c, t, C["s16.a"], "360", XE, 420, 150, "g", TINTA)
    E.formula_em(c, t, C["s16.b"], "= 2^3 · 3^2 · 5", XE + 345, 420, 120, "g", TINTA)
    E.frase(c, t, C["s16.c"], [("quantos", "i", 80), ("divisores?", "g", 80, COR)], XE, 640)
    E.frase(c, t, C["s16.d"], [("quantos", "i", 80), ("são", "i", 80), ("ímpares?", "g", 80, COR)], XE, 790)
    E.relogio(c, t, C["s17.a"], 1500, 620, 190)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    E.formula_em(c, t, C["s18"] + 0.1, "360 = 2^3 · 3^2 · 5", W / 2, 230, 110, "g", TINTA, "center")
    if t >= C["s18.c"]:
        wtot = E.formula(None, "360 = 2^3 · 3^2 · 5", 0, 0, 110, a=0)
        E.formula_em(c, t, C["s18.c"], "1", W / 2 + wtot / 2 + 4, 230 - 46, 64, "g", ERRADO)
    ta, tb_, tcc = C["s18.a"], C["s18.b"], C["s18.d"]
    xs = casinhas(c, t, 720, 520, [("fator 2", 4, ta - 0.2, ta + 0.4), ("fator 3", 3, tb_ - 0.2, tb_ + 0.4), ("fator 5", 2, tcc - 0.2, tcc + 0.4)], s=170,
                  tx=[C["s19.a"], C["s19.b"]])
    E.formula_em(c, t, ta, "3 + 1", xs[0], 395, 52, "b", COR, "center")
    E.formula_em(c, t, tb_, "2 + 1", xs[1], 395, 52, "b", COR, "center")
    E.formula_em(c, t, tcc, "1 + 1", xs[2], 395, 52, "b", COR, "center")
    E.formula_em(c, t, C["s19.a"], "4 × 3 = 12", XE, 860, 84, "g", TINTA)
    E.formula_em(c, t, C["s19.b"], "12 × 2", 700, 860, 84, "g", TINTA)
    bx = igual_bola(c, t, C["s19.b"] + 0.4, 990, 830, "24", r=95)
    E.foco(c, t, C["s19.b"] + 0.7, 0.5, lambda a: E.escreve(c, "divisores", bx + 120, 850, 56, "g", COR, a))
    E.foco(c, t, C["s19.c"], 0.5, lambda a: E.escreve(c, "ímpares:", 1350, 470, 60, "i", TINTA, a))
    E.formula_em(c, t, C["s19.c"] + 0.3, "3 × 2", 1350, 570, 84, "g", TINTA)
    igual_bola(c, t, C["s19.c"] + 0.7, 1600, 540, "6", r=80, cor=CERTO)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s20"], [("resumindo", "i", 92, COR)], W / 2, 210, "center")
        for i, (k, s) in enumerate((("s20.a", "fatore"), ("s20.b", "some 1 em cada expoente"), ("s20.c", "multiplique"))):
            y = 390 + i * 190
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 470, y - 30, 56, a=a), centro(c, str(i + 1), 470, y - 7, 64, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, [(s, "g", 88)], 570, y)
    E.saida(c, t, C["s21"] - 0.1, resumo)
    if t < C["s21"]:
        return
    E.frase(c, t, C["s21"] + 0.1, ps("próxima aula", "i", 84), XE, 330)
    E.frase(c, t, C["s21.a"], [("o", "i", 140), ("fatorial", "g", 150, COR)], XE, 500)
    E.frase(c, t, C["s21.b"], ps("cortar contas enormes", "i", 76), XE, 750)
    E.foco(c, t, C["s21.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1430, 400, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s21.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1760, 1560, p), lerp(720, 425, p), ep(t, C["s21.c"] + 0.2, 0.4))
    E.frase(c, t, C["s21.d"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 920, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, fatorar=b_fatorar, ideia=b_ideia, tabela=b_tabela, regra=b_regra, erro=b_erro, atalho=b_atalho,
              questao=b_questao, resposta=b_resposta, fim=b_fim)
