"""Visual — Estudativo · MAT-CNT-004: fatorial.
Mesma linguagem da trilha Contagem e Probabilidade (MAT-CNT-001 a 003): casinhas() com o número de opções dentro, × entre elas,
igual_bola() com o resultado. Peças desta aula:
- livros(): a prateleira com cinco livros; cada livro que vai para a fila apaga na prateleira (sobram 4, 3, 2, 1).
- escada(): a escada dos fatoriais, um degrau por fatorial (0! a 6!), com "k!" em cima e o valor dentro; "× k" no espelho do degrau.
- fracao_corte(): fração de fatoriais em que o fator igual some de cima e de baixo, riscado na cor da matéria.
Sem voz ainda: todo instante vem de C[...] (cenas e marcadores), nunca de segundos fixos."""
import math
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Contagem e Probabilidade")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-CNT-004_fatorial.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("prateleira", "definicao", "cortar", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
F = math.factorial
assert [F(k) for k in range(7)] == [1, 1, 2, 6, 24, 120, 720] and F(7) == 5040 and 6 * 120 == 720
assert F(8) // F(6) == 56 == 8 * 7 and F(8) == 40320 and F(10) // F(7) == 720 == 10 * 9 * 8 and F(13) // F(11) == 156 == 13 * 12
assert F(4) + F(3) == 30 and F(12) // F(10) == 132 and F(12) == 479001600 and 5 * 4 == 20 and 20 * 3 == 60 and 60 * 2 == 120


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


# ---------------- peças desta aula ----------------
LIVROS = ("#C2463A", "#3E5F93", "#D8A53C", "#55895A", "#7B3FE4")


def livros(c, t, x0, base, tsai, a=1.0):
    """cinco livros em pé numa prateleira; o livro i apaga (vai para a fila) no instante tsai[i]"""
    if a <= 0:
        return
    alt = (190, 220, 175, 205, 185)
    larg = (70, 82, 64, 76, 70)
    x = x0
    for i in range(5):
        q = 1 - 0.75 * ep(t, tsai[i], 0.4) if tsai and tsai[i] is not None else 1
        r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, base - alt[i], larg[i], alt[i]), 8, 8)
        c.drawRRect(r, M.paint(LIVROS[i], a * q))
        c.drawRRect(r, M.paint(TINTA, a * q, stroke=3))
        for dy in (0.18, 0.82):
            M.line(c, x + 10, base - alt[i] * dy, x + larg[i] - 10, base - alt[i] * dy, BR, a * q * 0.8, 4)
        x += larg[i] + 16
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x0 - 40, base, x - x0 + 64, 18), 6, 6), M.paint("#8A6A48", a))


def degrau_xy(k, x0=150, base=1000, larg=230, alto=80):
    """canto de cima, à esquerda, do degrau do k!"""
    return x0 + k * larg, base - (110 + k * alto)


def escada(c, t, tdeg, tmul=None, x0=150, base=1000, larg=230, alto=80, destaque=()):
    """escada dos fatoriais: tdeg = {k: instante do degrau k!}; tmul = {k: instante do '× k' entre k−1 e k}"""
    for k, t0 in sorted(tdeg.items()):
        x, y = degrau_xy(k, x0, base, larg, alto)
        forte = k in destaque

        def f(a, x=x, y=y, k=k, forte=forte):
            r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x + 6, y, larg - 12, base - y), 14, 14)
            c.drawRRect(r, M.paint(E.COR if forte else BR, a))
            c.drawRRect(r, M.paint(TINTA, a, stroke=4))
            centro(c, f"{k}!", x + larg / 2, y - 22, 64, "g", TINTA, a)
            v = f"{F(k):,}".replace(",", ".")
            centro(c, v, x + larg / 2, y + 72, 60 if len(v) < 4 else 50, "g", BR if forte else COR, a)
        E.foco(c, t, t0, 0.45, f)
    for k, t0 in (tmul or {}).items():
        x, y = degrau_xy(k, x0, base, larg, alto)
        E.foco(c, t, t0, 0.4, lambda a, x=x, y=y, k=k: E.pilula(c, f"× {k}", x, y + 150, 34, estilo="b", fundo=E.COR, a=a))


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


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def conta():
        E.formula_em(c, t, C["s01.a"], "f{8!}{6!}", 700, 560, 220, "g", TINTA, "center")
        E.frase(c, t, C["s01.b"], [("de", "i", 84), ("cabeça,", "g", 84, COR)], 1300, 420)
        E.frase(c, t, C["s01.b"] + 0.8, ps("em uma linha", "i", 84), 1300, 530)
        igual_bola(c, t, C["s01.c"], 1000, 820, "56", r=120)
    E.saida(c, t, C["s02"] - 0.1, conta)
    if t >= C["s02"]:
        E.foco(c, t, C["s02.c"] - 0.2, 0.7, lambda a: E.bola(c, 1450, 520, 300 * ease_back(prog(t, C["s02.c"] - 0.2, 0.7))), blur=0)
        E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 96), XE, 330)
        E.frase(c, t, C["s02.a"] + 0.9, [("calcular", "g", 132)], XE, 480)
        E.frase(c, t, C["s02.a"] + 1.2, [("fatoriais", "g", 132, COR)], XE, 630)
        E.frase(c, t, C["s02.b"], [("e", "i", 96), ("cortar", "g", 96), ("contas", "i", 96)], XE, 790)
        E.foco(c, t, C["s02.c"] + 0.2, 0.5, lambda a: (E.escreve(c, "+ atalho", 1290, 505, 84, "g", BR, a),
                                                      E.escreve(c, "de prova", 1310, 590, 84, "i", BR, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], [("você", "i", 84), ("vai", "i", 84), ("usar", "i", 84)], W / 2, 210, "center")
    E.frase(c, t, C["s03.a"], [("duas", "g", 96, COR), ("coisas", "i", 96)], W / 2, 330, "center")
    for k, x, titulo in (("s03.b", 220, "casinhas"), ("s03.c", 1000, "simplificar fração")):
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, 420, 700, 480, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(titulo, "g", 72, COR)], x + 350, 530, "center")
    casinhas(c, t, 570, 700, [("", 3, C["s03.b"] + 0.3, C["s03.b"] + 0.5), ("", 4, C["s03.b"] + 0.5, C["s03.b"] + 0.7)], s=150)
    E.formula_em(c, t, C["s03.c"] + 0.4, "f{6}{9} = f{2}{3}", 1350, 740, 110, "g", TINTA, "center")
    E.foco(c, t, C["s03.c"] + 0.9, 0.5, lambda a: E.centro(c, "÷ 3 em cima e embaixo", 1350, 860, 46, "i", TINTA2, a))


# ---------------- prateleira ----------------
def b_prateleira(c, t, C, b):
    E.frase(c, t, C["s04.a"], [("5", "g", 84, COR), ("livros", "i", 84), ("diferentes", "i", 84)], W / 2, 170, "center")
    tsai = [C[k] + 0.7 for k in ("s05.a", "s05.b", "s05.c", "s05.d", "s05.e")]
    E.foco(c, t, C["s04.a"] + 0.3, 0.5, lambda a: livros(c, t, 760, 430, tsai, a))
    ks = ("s05.a", "s05.b", "s05.c", "s05.d", "s05.e")
    xs = casinhas(c, t, W / 2, 640, [(f"{i + 1}º lugar", 5 - i, C["s04.b"] + 0.15 * i, C[ks[i]]) for i in range(5)], s=150, gap=80,
                  tx=[C["s06.a"] - 0.2, C["s06.b"] - 0.2, C["s06.c"] - 0.2, C["s06.d"] - 0.2])
    E.foco(c, t, C["s05.b"] + 0.5, 0.5, lambda a: E.escreve(c, "o que foi não volta", 1330, 370, 52, "i", TINTA2, a) if t < C["s06"] else None)
    # a conta corrida, embaixo de cada casinha
    y = 900
    for k, (i, v) in zip(("s06.a", "s06.b", "s06.c", "s06.d"), ((1, 20), (2, 60), (3, 120), (4, 120))):
        E.foco(c, t, C[k], 0.45, lambda a, i=i, v=v: E.centro(c, str(v), xs[i], y, 72, "g", COR, a))
    E.foco(c, t, C["s06.a"], 0.45, lambda a: E.centro(c, "5 × 4 =", xs[0], y, 52, "b", TINTA2, a))
    E.foco(c, t, C["s06.d"] + 0.5, 0.5, lambda a: E.centro(c, "formas", xs[4], y + 80, 56, "i", COR, a))


# ---------------- definição e escada ----------------
def b_definicao(c, t, C, b):
    def nome():
        E.frase(c, t, C["s07.a"], [("isso", "i", 84), ("é", "i", 84), ("o", "i", 84)], W / 2, 220, "center")
        E.frase(c, t, C["s07.a"] + 0.4, [("fatorial", "g", 160, COR)], W / 2, 400, "center")
        E.foco(c, t, C["s07.b"], 0.5, lambda a: (E.escreve(c, "5", 760, 680, 240, "g", TINTA, a), E.escreve(c, "!", 905, 680, 240, "g", COR, a)))
        E.foco(c, t, C["s07.b"] + 0.8, 0.5, lambda a: E.pilula(c, "não é espanto: é conta", 1350, 600, 50, estilo="b", fundo=TINTA2, a=a)
               if t < C["s07.c"] else None)
        E.formula_em(c, t, C["s07.c"], "= 5 × 4 × 3 × 2 × 1", 1010, 680, 96, "g", TINTA)
        if t >= C["s07.d"]:
            x1 = 1010 + E.formula(None, "= 5 × 4 × 3 × 2 × ", 0, 0, 96, a=0)
            w1 = E.larg("1", "g", 96)
            E.foco(c, t, C["s07.d"], 0.4, lambda a: E.caixa_pontilhada(c, x1 - 18, 590, w1 + 36, 110, a, E.COR, a))
            E.foco(c, t, C["s07.d"] + 0.2, 0.5, lambda a: E.centro(c, "até o 1", x1 + w1 / 2, 780, 52, "i", COR, a))
        E.frase(c, t, C["s07.c"] + 0.4, ps("descendo de um em um", "i", 64, TINTA2), W / 2, 900, "center")
    E.saida(c, t, C["s08"] - 0.1, nome)
    if t < C["s08"]:
        return
    E.saida(c, t, C["s09.b"] - 0.1, lambda: E.frase(c, t, C["s08"] + 0.1, ps("os fatoriais crescem rápido", "i", 72), W / 2, 170, "center"))
    tdeg = {k: C[f"s08.{'abcdef'[k - 1]}"] for k in range(1, 7)}
    tdeg[0] = C["s09.d"]
    tmul = {k: C["s09.a"] + 0.3 * (k - 2) for k in range(2, 7)}
    tmul[1] = C["s09.d"] + 0.6
    destaque = (0,) if t >= C["s09.e"] else (6, 5) if C["s09.b"] <= t < C["s09.c"] else ()
    escada(c, t, tdeg, tmul, destaque=destaque)
    # 6! = 6 × 5!, depois 7! = 7 × 6!
    t7 = lerp(C["s09.b"], C["s09.c"], 0.55)
    E.saida(c, t, t7 - 0.1, lambda: E.formula_em(c, t, C["s09.b"], "6! = 6 × 5! = 6 × 120 = 720", XE, 200, 72, "g", TINTA))
    E.saida(c, t, C["s09.c"] - 0.1, lambda: E.formula_em(c, t, t7, "7! = 7 × 6! = 5.040", XE, 200, 72, "g", TINTA))
    E.saida(c, t, C["s09.d"] - 0.1, lambda: E.foco(c, t, C["s09.c"], 0.5, lambda a: E.pilula(c, "a chave para cortar contas", W / 2, 180, 52, estilo="g", a=a)))
    if t >= C["s09.d"]:
        E.formula_em(c, t, C["s09.d"], "1! = 1 × 0!", 900, 200, 80, "g", TINTA)
        E.foco(c, t, C["s09.e"], 0.5, lambda a: E.pilula(c, "0! = 1", 1500, 175, 64, estilo="g", a=a))


# ---------------- cortar ----------------
def b_cortar(c, t, C, b):
    E.frase(c, t, C["s10"] + 0.1, ps("voltando ao começo", "i", 72, TINTA2), W / 2, 170, "center")
    def antes():
        E.formula_em(c, t, C["s10.a"], "f{8!}{6!}", 400, 560, 200, "g", TINTA, "center")
        if t >= C["s10.b"]:
            p = ep(t, C["s10.b"], 0.5)
            M.arrow(c, 600, 500, 760, 500, TINTA2, p, 5, 16, p)
            E.foco(c, t, C["s10.b"], 0.5, lambda a: E.centro(c, "abra só até o 6!", 680, 430, 52, "i", TINTA2, a))
    E.saida(c, t, C["s11.a"] - 0.1, antes)
    cx = lerp(1260, 760, ease_io(prog(t, C["s11.a"] - 0.1, 0.6)))
    if t >= C["s10.c"]:
        fracao_corte(c, t, C["s10.c"], cx, 520, 140, ["8", "×", "7", "×", "6!"], "6!", [C["s10.c"], C["s10.c"] + 0.2, C["s10.c"] + 0.3, C["s10.c"] + 0.5,
                                                                                      C["s10.c"] + 0.7], C["s11.b"], (4,))
    if t >= C["s11.a"]:
        E.foco(c, t, C["s11.a"], 0.5, lambda a: E.pilula(c, "÷ 6! em cima e embaixo", 1420, 330, 50, estilo="b", fundo=TINTA2, a=a))
        E.foco(c, t, C["s11.b"] + 0.3, 0.5, lambda a: E.escreve(c, "some de cima e de baixo", 1180, 520, 52, "i", COR, a))
        E.formula_em(c, t, C["s11.c"], "8 × 7", 1180, 800, 110, "g", TINTA)
        igual_bola(c, t, C["s11.c"] + 0.4, 1500, 762, "56", r=110)
        E.foco(c, t, C["s11.c"] + 1.6, 0.5, lambda a: E.centro(c, "caminho longo: 40.320 ÷ 720", W / 2, 1010, 50, "i", TINTA2, a))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s12"] + 0.1, [("cuidado", "g", 96, ERRADO), ("com", "i", 90), ("isto", "i", 90)], W / 2, 180, "center")
    E.frase(c, t, C["s12.a"], ps("conta só com os números que aparecem", "i", 64, TINTA2), W / 2, 300, "center", passo=0.12)
    E.formula_em(c, t, C["s12"] + 0.4, "f{8!}{6!}", 400, 600, 170, "g", TINTA, "center")
    E.formula_em(c, t, C["s12.b"], "8 − 6 = 2", 640, 560, 96, "g", ERRADO)
    E.formula_em(c, t, C["s12.c"], "2! = 2", 640, 700, 96, "g", ERRADO)
    if t >= C["s12.c"] + 1.4:
        E.risco(c, 620, 520, 1110, 520, t, C["s12.c"] + 1.4, largura=12)
        E.risco(c, 620, 665, 960, 665, t, C["s12.c"] + 1.6, largura=12)
    E.foco(c, t, C["s12.c"] + 1.2, 0.5, lambda a: E.escreve(c, "longe de 56", 1200, 640, 64, "g", ERRADO, a))
    E.frase(c, t, C["s12.d"], [("abra", "i", 76), ("o", "i", 76), ("maior", "g", 76, COR), ("e", "i", 76), ("corte", "g", 76, COR), ("só", "i", 76),
                               ("o", "i", 76), ("igual", "i", 76)], W / 2, 920, "center")


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def tres():
        E.frase(c, t, C["s13.a"], [("a", "i", 80, CLARO), ("diferença", "g", 80, BR), ("diz", "i", 80, CLARO), ("quantos", "i", 80, CLARO),
                                   ("números", "i", 80, CLARO), ("sobram", "g", 80, BR)], W / 2, 180, "center", passo=0.15)
        linhas = (("s13.b", "f{8!}{6!}", "2", "8 × 7", "56", 380), ("s13.c", "f{10!}{7!}", "3", "10 × 9 × 8", "720", 640),
                  ("s13.e", "f{13!}{11!}", "2", "13 × 12", "156", 900))
        for k, fr_, dif, conta, res, y in linhas:
            E.formula_em(c, t, C[k], fr_, 330, y + 40, 100, "g", BR, "center")
            E.foco(c, t, C[k] + 0.4, 0.4, lambda a, dif=dif, y=y: E.pilula(c, f"diferença {dif}", 680, y, 44, estilo="b", fundo=E.COR, a=a))
            tc = {"s13.b": C["s13.b"] + 1.4, "s13.c": C["s13.d"], "s13.e": C["s13.f"]}[k]
            E.formula_em(c, t, tc, conta, 920, y + 30, 96, "g", BR)
            igual_bola(c, t, tc + 0.4, 1500, y, res, r=85, cor=E.COR, escuro=True)
    E.saida(c, t, C["s14"] - 0.1, tres)
    if t < C["s14"]:
        return
    E.frase(c, t, C["s14.a"], ps("tudo do menor fatorial para baixo se corta", "i", 70, CLARO), W / 2, 200, "center", passo=0.12)

    def longe():
        E.foco(c, t, C["s14.b"], 0.5, lambda a: E.pilula(c, "não compensa", 360, 420, 50, estilo="g", fundo=ERRADO, a=a))
        E.formula_em(c, t, C["s14.b"] + 0.3, "f{10!}{2!}", 720, 470, 100, "g", BR, "center")
        E.formula_em(c, t, C["s14.b"] + 0.8, "10 × 9 × 8 × 7 × 6 × 5 × 4 × 3", 900, 455, 64, "g", CLARO)
        E.foco(c, t, C["s14.b"] + 1.2, 0.5, lambda a: E.escreve(c, "sobram 8 números", 900, 540, 52, "i", CLARO, a))
    longe()
    E.foco(c, t, C["s14.c"], 0.5, lambda a: E.pilula(c, "na soma", 360, 760, 50, estilo="g", fundo=ERRADO, a=a))
    E.formula_em(c, t, C["s14.c"] + 0.3, "8! + 6!", 640, 790, 100, "g", BR)
    E.foco(c, t, C["s14.c"] + 0.8, 0.5, lambda a: E.escreve(c, "nada se corta: calcule cada um", 1040, 780, 56, "i", CLARO, a))


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s15"] + 0.1, [("hora", "i", 72, COR), ("de", "i", 72, COR), ("testar", "i", 72, COR)], XE, 190)
    E.foco(c, t, C["s15.a"] - 0.3, 0.5, lambda a: (E.bola(c, XE + 36, 400, 36, a=a), centro(c, "1", XE + 36, 416, 44, "g", BR, a)))
    E.formula_em(c, t, C["s15.a"], "4! + 3! = ?", XE + 110, 440, 120, "g", TINTA)
    E.foco(c, t, C["s15.b"] - 0.3, 0.5, lambda a: (E.bola(c, XE + 36, 720, 36, a=a), centro(c, "2", XE + 36, 736, 44, "g", BR, a)))
    E.formula_em(c, t, C["s15.b"], "f{12!}{10!} = ?", XE + 110, 760, 120, "g", TINTA)
    E.relogio(c, t, C["s16.a"], 1450, 460, 200)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    def soma():
        E.frase(c, t, C["s17"] + 0.3, [("na", "i", 72), ("soma,", "i", 72), ("nada", "g", 72, COR), ("se", "i", 72), ("corta", "g", 72, COR)], W / 2, 190, "center")
        E.formula_em(c, t, C["s17.a"], "4! = 24", 400, 420, 110, "g", TINTA)
        E.formula_em(c, t, C["s17.b"], "3! = 6", 400, 580, 110, "g", TINTA)
        E.formula_em(c, t, C["s17.c"], "24 + 6", 400, 790, 110, "g", TINTA)
        igual_bola(c, t, C["s17.c"] + 0.4, 820, 752, "30", r=110, cor=CERTO)
        E.formula_em(c, t, C["s17.c"] + 1.6, "7! = 5.040", 1300, 600, 96, "g", ERRADO)
        if t >= C["s17.c"] + 2.4:
            E.risco(c, 1280, 560, 1800, 560, t, C["s17.c"] + 2.4, largura=12)
        E.foco(c, t, C["s17.c"] + 2.0, 0.5, lambda a: E.escreve(c, "juntou tudo", 1300, 470, 56, "i", ERRADO, a))
    E.saida(c, t, C["s18"] - 0.1, soma)
    if t < C["s18"]:
        return
    E.frase(c, t, C["s18"] + 0.1, [("diferença", "i", 72), ("2:", "g", 72, COR), ("sobram", "i", 72), ("2", "g", 72, COR), ("números", "i", 72)],
            W / 2, 190, "center")
    fracao_corte(c, t, C["s18"] + 0.5, 520, 520, 120, ["12", "×", "11", "×", "10!"], "10!",
                 [C["s18.a"], C["s18.a"] + 0.2, C["s18.a"] + 0.4, C["s18.a"] + 0.6, C["s18.a"] + 0.8], C["s18.a"] + 1.2, (4,))
    E.formula_em(c, t, C["s18.b"], "12 × 11", 1000, 560, 110, "g", TINTA)
    igual_bola(c, t, C["s18.b"] + 0.4, 1440, 522, "132", r=115, cor=CERTO)
    E.foco(c, t, C["s18.c"], 0.5, lambda a: E.centro(c, "sem cortar: 12! = 479.001.600", W / 2, 900, 64, "b", TINTA2, a))
    E.foco(c, t, C["s18.c"] + 0.6, 0.5, lambda a: E.centro(c, "mais de 400 milhões", W / 2, 990, 56, "i", TINTA2, a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s19"], [("resumindo", "i", 92, COR)], W / 2, 210, "center")
        E.foco(c, t, C["s19.a"], 0.5, lambda a: (E.bola(c, 300, 430, 56, a=a), centro(c, "1", 300, 453, 64, "g", BR, a)))
        E.formula_em(c, t, C["s19.a"] + 0.2, "5! = 5 × 4 × 3 × 2 × 1", 400, 465, 96, "g", TINTA)
        E.frase(c, t, C["s19.a"] + 0.8, ps("todos os de baixo, até o 1", "i", 60, TINTA2), 400, 560)
        E.foco(c, t, C["s19.b"], 0.5, lambda a: (E.bola(c, 300, 760, 56, a=a), centro(c, "2", 300, 783, 64, "g", BR, a)))
        E.formula_em(c, t, C["s19.b"] + 0.2, "f{8!}{6!} = 8 × 7", 400, 800, 96, "g", TINTA)
        E.frase(c, t, C["s19.b"] + 0.8, [("abra", "i", 60, TINTA2), ("o", "i", 60, TINTA2), ("maior", "i", 60, TINTA2), ("e", "i", 60, TINTA2),
                                         ("corte", "g", 60, COR)], 880, 790)
    E.saida(c, t, C["s20"] - 0.1, resumo)
    if t < C["s20"]:
        return
    E.frase(c, t, C["s20"] + 0.1, ps("próxima aula", "i", 84), XE, 300)
    E.frase(c, t, C["s20.a"], [("filas", "g", 140, COR), ("e", "i", 130)], XE, 450)
    E.frase(c, t, C["s20.a"] + 0.3, [("anagramas", "g", 140, COR)], XE, 600)
    E.frase(c, t, C["s20.b"], ps("com gente sempre junta", "i", 72), XE, 730)
    E.foco(c, t, C["s20.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1430, 400, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s20.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1760, 1560, p), lerp(720, 425, p), ep(t, C["s20.c"] + 0.2, 0.4))
    E.frase(c, t, C["s20.d"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 920, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, prateleira=b_prateleira, definicao=b_definicao, cortar=b_cortar, erro=b_erro, atalho=b_atalho,
              questao=b_questao, resposta=b_resposta, fim=b_fim)
