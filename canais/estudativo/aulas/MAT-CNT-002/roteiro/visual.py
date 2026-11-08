"""Visual — Estudativo · MAT-CNT-002: contar com restrições, comece pelo mais difícil.
Mesma linguagem da MAT-CNT-001 (as casinhas da trilha Contagem e Probabilidade), com as peças de restrição:
- casinhas(): caixa branca por etapa, número de opções dentro (cor da matéria), nome embaixo, × entre elas. "?" em cinza.
  Cor "fixo" = caixa preenchida com o algarismo que já está decidido (uma opção só); não leva × ao lado.
- marca(): caixa pontilhada em volta da casinha da vez; regra(): pílula da restrição em cima da casinha;
  ordem(): esfera pequena no canto com a ordem de preenchimento; nota(): a conta da casinha embaixo do nome.
- igual_bola(): "=" e o resultado na esfera.
Sem voz ainda: todo instante vem de C[...] (cenas e marcadores), nunca de segundos fixos."""
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Contagem e Probabilidade")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-CNT-002_contar_com_restricoes.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("regras", "casos", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
assert 9 * 9 == 81 and 81 * 8 == 648 and 10 * 9 * 8 == 720 and 720 - 72 == 648 and 1 * 9 * 8 == 72
assert 9 * 8 == 72 and 8 * 8 == 64 and 72 + 64 == 136 and 4 * 8 == 32 and 9 + 32 == 41
# conferência por força bruta
assert sum(1 for n in range(100, 1000) if len(set(str(n))) == 3) == 648
assert sum(1 for n in range(100, 1000) if len(set(str(n))) == 3 and n % 5 == 0) == 136
assert sum(1 for n in range(10, 100) if len(set(str(n))) == 2 and n % 2 == 0) == 41


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças da trilha ----------------
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


def ordem(c, t, t0, x, y, s, n, cor=None):
    """esfera pequena no canto de cima, à esquerda, com a ordem em que a casinha é preenchida"""
    cx, cy = x - s / 2, y - s / 2
    k = ease_back(prog(t, t0, 0.45))
    if k > 0:
        E.bola(c, cx, cy, 30 * k, cor)
        centro(c, str(n), cx, cy + 13, 36 * k, "g", BR)


def nota(c, t, t0, x, y, txt, size=46, cor=TINTA2, estilo="b"):
    E.foco(c, t, t0, 0.45, lambda a: centro(c, txt, x, y, size, estilo, cor, a))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def pergunta():
        E.frase(c, t, C["s01.a"], ps("quantos números de 3 algarismos", "i", 80), W / 2, 230, "center", passo=0.15)
        E.frase(c, t, C["s01.b"], [("todos", "g", 84, COR), ("diferentes?", "g", 84, COR)], W / 2, 350, "center")
        E.foco(c, t, C["s01.b"] + 0.8, 0.5, lambda a: (E.centro(c, "472", W / 2 - 150, 470, 64, "b", CERTO, a), E.centro(c, "477", W / 2 + 150, 470, 64, "b", ERRADO, a)))
        x = W / 2
        E.formula_em(c, t, C["s01.c"], "10 × 9 × 8 = 720", x, 680, 120, "g", ERRADO if t >= C["s01.d"] else TINTA, "center")
        if t >= C["s01.d"]:
            E.risco(c, x - 470, 640, x + 470, 640, t, C["s01.d"], largura=14)
            E.foco(c, t, C["s01.d"] + 0.2, 0.4, lambda a: E.centro(c, "errou", x + 600, 690, 72, "g", ERRADO, a))
        E.foco(c, t, C["s01.e"], 0.4, lambda a: E.escreve(c, "são", 700, 900, 90, "i", TINTA, a))
        E.foco(c, t, C["s01.e"] + 0.2, 0.5, lambda a: (E.bola(c, 1010, 870, 115, a=a), centro(c, "648", 1010, 870 + 32, 88, "g", BR, a)))
    E.saida(c, t, C["s02"] - 0.1, pergunta)

    if t >= C["s02"]:
        E.foco(c, t, C["s02.c"] - 0.2, 0.7, lambda a: E.bola(c, 1450, 520, 300 * ease_back(prog(t, C["s02.c"] - 0.2, 0.7))), blur=0)
        E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 96), XE, 330)
        E.frase(c, t, C["s02.a"] + 0.9, [("contar", "g", 132)], XE, 480)
        E.frase(c, t, C["s02.a"] + 1.2, [("com", "i", 120), ("regras", "g", 132)], XE, 630)
        E.frase(c, t, C["s02.b"], [("qual", "i", 96), ("casinha", "i", 96), ("primeiro", "g", 96, COR)], XE, 790)
        E.foco(c, t, C["s02.c"] + 0.2, 0.5, lambda a: (E.centro(c, "somar", 1450, 470, 84, "g", BR, a),
                                                      E.centro(c, "ou", 1450, 560, 76, "i", BR, a),
                                                      E.centro(c, "multiplicar?", 1450, 650, 72, "g", BR, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], [("lembre", "i", 84), ("do", "i", 84)], W / 2, 200, "center")
    E.frase(c, t, C["s03.a"], [("princípio", "g", 96, COR), ("multiplicativo", "g", 96, COR)], W / 2, 320, "center")
    tb = C["s03.b"]
    xs = casinhas(c, t, 820, 600, [("camisa", 3, tb, C["s03.c"]), ("calça", 4, tb + 0.2, C["s03.c"] + 0.3), ("tênis", 2, tb + 0.4, C["s03.c"] + 0.6)],
                  s=180, tx=[C["s03.d"], C["s03.d"] + 0.2])
    E.foco(c, t, C["s03.b"] + 0.3, 0.5, lambda a: E.centro(c, "uma casinha por etapa", 820, 900, 52, "i", TINTA2, a))
    E.foco(c, t, C["s03.c"] + 0.2, 0.5, lambda a: E.centro(c, "opções dentro", 820, 980, 52, "i", TINTA2, a))
    igual_bola(c, t, C["s03.d"] + 0.5, xs[2] + 170, 600, "24", r=110)


# ---------------- as regras ----------------
CX3, Y3, S3, G3 = 700, 540, 190, 190
NOMES3 = ("centena", "dezena", "unidade")


def b_regras(c, t, C, b):
    E.frase(c, t, C["s04"] + 0.1, [("3", "g", 84, COR), ("algarismos,", "i", 84), ("3", "g", 84, COR), ("casinhas", "i", 84)], W / 2, 190, "center")
    ta = C["s04.a"]
    casinhas(c, t, CX3, Y3, [(n_, None, ta + 0.2 * i, None) for i, n_ in enumerate(NOMES3)], s=S3, gap=G3, tx=[None, None],
             tnomes=[C["s04.b"] + 0.3 * i for i in range(3)])
    regra(c, t, C["s04.c"], 1500, 400, "não pode repetir", size=46)
    regra(c, t, C["s04.d"], 1500, 560, "zero não vai na frente", size=46, fundo=ERRADO)
    # 047 é só 47
    if t >= C["s04.e"]:
        y = 900
        E.foco(c, t, C["s04.e"], 0.5, lambda a: (E.escreve(c, "0", 520, y, 120, "g", ERRADO, a), E.escreve(c, "47", 600, y, 120, "g", TINTA, a)))
        E.sinal(c, t, C["s04.e"] + 0.6, "=", 850, y - 44, 100)
        E.foco(c, t, C["s04.e"] + 0.9, 0.5, lambda a: E.escreve(c, "47", 940, y, 120, "g", TINTA, a))
        E.foco(c, t, C["s04.e"] + 1.4, 0.5, lambda a: E.escreve(c, "só 2 algarismos", 1150, y - 10, 64, "i", ERRADO, a))


# ---------------- comece pelo mais difícil ----------------
def b_casinhas(c, t, C, b):
    def primeira():
        E.frase(c, t, C["s05"] + 0.1, [("qual", "i", 84), ("casinha", "i", 84), ("tem", "i", 84), ("mais", "i", 84), ("regra?", "g", 84, COR)],
                W / 2, 190, "center")
        tv = (C["s05.c"], C["s06.c"], C["s07.c"])
        xs = casinhas(c, t, CX3, Y3, [(n_, v, C["s05"], tv[i]) for i, (n_, v) in enumerate(zip(NOMES3, (9, 9, 8)))], s=S3, gap=G3,
                      tx=[C["s08.a"], C["s08.a"] + 0.2])
        for i, (k0, k1) in enumerate((("s05.a", "s06.a"), ("s06.a", "s07.a"), ("s07.a", "s08.a"))):
            marca(c, t, C[k0], xs[i], Y3, S3, C[k1] - 0.2, COR)
        ordem(c, t, C["s05.b"], xs[0], Y3, S3, 1)
        ordem(c, t, C["s06.a"], xs[1], Y3, S3, 2)
        ordem(c, t, C["s07.a"], xs[2], Y3, S3, 3)
        yr = Y3 - S3 / 2 - 70
        regra(c, t, C["s05.a"] + 0.3, xs[0], yr, "sem o 0", fundo=ERRADO, size=36)
        regra(c, t, C["s06.b"], xs[1], yr, "sem o da centena", size=36)
        regra(c, t, C["s07.b"], xs[2], yr, "sem os 2 usados", size=36)
        yn = Y3 + S3 / 2 + 120
        nota(c, t, C["s05.c"] + 0.3, xs[0], yn, "1 a 9")
        nota(c, t, C["s06.c"] + 0.3, xs[1], yn, "10 − 1")
        nota(c, t, C["s07.c"] + 0.3, xs[2], yn, "10 − 2")
        E.foco(c, t, C["s05.b"], 0.5, lambda a: E.escreve(c, "comece por ela", 1300, Y3 + 20, 64, "i", COR, a) if t < C["s06.a"] else None)
        # a conta
        y = 920
        E.formula_em(c, t, C["s08.a"], "9 × 9 = 81", 330, y, 96, "g", TINTA)
        E.formula_em(c, t, C["s08.b"], "81 × 8", 900, y, 96, "g", TINTA)
        igual_bola(c, t, C["s08.b"] + 0.4, 1250, y - 34, "648", r=110)
    E.saida(c, t, C["s09"] - 0.1, primeira)
    if t < C["s09"]:
        return
    E.frase(c, t, C["s09"] + 0.1, [("e", "i", 84), ("se", "i", 84), ("começar", "i", 84), ("pela", "i", 84), ("unidade?", "g", 84, COR)],
            W / 2, 190, "center")
    vals = ("?", 9, 10)
    tv = (C["s09.c"], C["s09.b"], C["s09.a"])
    xs = casinhas(c, t, CX3, Y3, [(n_, vals[i], C["s09"] + 0.3, tv[i], ERRADO if i == 0 else COR) for i, n_ in enumerate(NOMES3)], s=S3, gap=G3,
                  tx=[None, None])
    ordem(c, t, C["s09.a"], xs[2], Y3, S3, 1)
    ordem(c, t, C["s09.b"], xs[1], Y3, S3, 2)
    ordem(c, t, C["s09.c"], xs[0], Y3, S3, 3, ERRADO)
    regra(c, t, C["s09.c"] + 0.4, xs[0], Y3 - S3 / 2 - 70, "8 ou 7?", fundo=ERRADO, size=46)
    E.foco(c, t, C["s09.c"] + 0.6, 0.5, lambda a: E.escreve(c, "a conta trava", 1300, Y3 + 20, 72, "g", ERRADO, a))
    E.frase(c, t, C["s09.d"], [("comece", "i", 76), ("pela", "i", 76), ("casinha", "i", 76), ("mais", "i", 76), ("difícil", "g", 76, COR)],
            W / 2, 940, "center")


# ---------------- casos ----------------
R1, R2, CXC, SC = 330, 640, 1050, 150


def linha_caso(c, t, y, t0, rot, vals, tvs, fixo, tfim, res, tr):
    """um caso numa linha: rótulo à esquerda, centena e dezena com a conta, unidade fixa, '= resultado'"""
    E.frase(c, t, t0, rot, XE, y + 20)
    itens = [("centena", vals[0], t0 + 0.3, tvs[0]), ("dezena", vals[1], t0 + 0.4, tvs[1]), ("unidade", fixo, t0 + 0.5, t0 + 0.6, "fixo")]
    xs = casinhas(c, t, CXC, y, itens, s=SC, gap=80, tx=[tfim, None])
    igual_bola(c, t, tr, xs[2] + 150, y, res, r=95)
    return xs


def b_casos(c, t, C, b):
    def apresenta():
        E.frase(c, t, C["s10.a"], ps("3 algarismos diferentes", "i", 84), W / 2, 260, "center")
        E.frase(c, t, C["s10.b"], [("terminados", "i", 84), ("em", "i", 84), ("0", "g", 96, COR), ("ou", "i", 84), ("5", "g", 96, COR)],
                W / 2, 380, "center")
        if t >= C["s11"]:
            xs = casinhas(c, t, CX3, 650, [(n_, "?" if i < 2 else None, C["s11"] + 0.1 * i, C["s11"] + 0.3) for i, n_ in enumerate(NOMES3)],
                          s=170, gap=G3, tx=[None, None])
            marca(c, t, C["s11.a"], xs[2], 650, 170, None, COR)
            regra(c, t, C["s11.a"] + 0.3, xs[2], 650 - 85 - 60, "0 ou 5", fundo=E.COR, size=46)
            if t >= C["s11.b"]:
                p = ease_io(prog(t, C["s11.b"], 0.8))
                path = skia.Path(); path.moveTo(xs[2], 650 + 160); path.quadTo((xs[0] + xs[2]) / 2, 1000, xs[0], 650 + 160)
                pt = M.paint(COR, 1, stroke=6); pt.setPathEffect(skia.DashPathEffect.Make([18, 12], 0))
                seg = skia.Path(); skia.PathMeasure(path, False).getSegment(0, skia.PathMeasure(path, False).getLength() * p, seg, True)
                c.drawPath(seg, pt)
                E.foco(c, t, C["s11.b"] + 0.6, 0.5, lambda a: E.centro(c, "muda a centena", (xs[0] + xs[2]) / 2, 1050, 56, "i", COR, a))
            E.foco(c, t, C["s11.c"], 0.5, lambda a: E.pilula(c, "separe em casos", 1550, 650, 52, estilo="g", a=a))
    E.saida(c, t, C["s12"] - 0.1, apresenta)
    if t < C["s12"]:
        return

    def casos():
        linha_caso(c, t, R1, C["s12.a"], [("caso", "i", 56), ("1:", "i", 56), ("termina", "i", 56), ("em", "i", 56), ("0", "g", 64, COR)],
                   (9, 8), (C["s12.b"], C["s12.c"]), "0", C["s12.d"] - 0.3, "72", C["s12.d"])
        if t >= C["s13"]:
            xs = linha_caso(c, t, R2, C["s13.a"], [("caso", "i", 56), ("2:", "i", 56), ("termina", "i", 56), ("em", "i", 56), ("5", "g", 64, COR)],
                            (8, 8), (C["s13.c"], C["s13.d"]), "5", C["s13.e"] - 0.3, "64", C["s13.e"])
            regra(c, t, C["s13.b"], xs[0], R2 - SC / 2 - 50, "nem 0 nem 5", fundo=ERRADO, size=36)
    E.saida(c, t, C["s15"] - 0.1, casos)
    if C["s14"] <= t < C["s15"] + 0.4:
        def soma():
            E.frase(c, t, C["s14.a"], [("cada", "i", 64), ("número", "i", 64), ("cai", "i", 64), ("em", "i", 64), ("um", "g", 64, COR),
                                       ("caso", "g", 64, COR), ("só", "g", 64, COR)], XE, 920)
            E.formula_em(c, t, C["s14.c"], "72 + 64", 1080, 940, 96, "g", TINTA)
            igual_bola(c, t, C["s14.c"] + 0.5, 1500, 905, "136", r=105)
            E.foco(c, t, C["s14.b"], 0.5, lambda a: E.pilula(c, "+ se somam", 1500, 780, 48, estilo="g", fundo=CERTO, a=a) if t < C["s14.c"] + 0.4 else None)
        E.saida(c, t, C["s15"] - 0.1, soma)
    if t < C["s15"]:
        return
    E.frase(c, t, C["s15.a"], [("a", "i", 84), ("palavra", "i", 84), ("ou", "g", 96, COR), ("ajuda,", "i", 84), ("mas", "i", 84),
                               ("não", "i", 84), ("decide", "i", 84)], W / 2, 220, "center", passo=0.15)
    for k, y, l1, l2, sg, cor in (("s15.b", 470, "eu faço todas as etapas?", "multiplique", "×", COR),
                                  ("s15.c", 760, "cada resultado cai em um caso só?", "some os casos", "+", CERTO)):
        E.foco(c, t, C[k], 0.5, lambda a, y=y, sg=sg, cor=cor: (E.bola(c, XE + 70, y + 10, 70, cor, a), centro(c, sg, XE + 70, y + 42, 90, "g", BR, a)))
        E.frase(c, t, C[k] + 0.1, ps(l1, "i", 72), XE + 180, y - 10)
        E.frase(c, t, C[k] + 0.9, [(l2, "g", 84, cor)], XE + 180, y + 90)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s16"] + 0.1, [("cuidado", "g", 96, ERRADO), ("com", "i", 90), ("isto", "i", 90)], W / 2, 180, "center")
    xs = casinhas(c, t, 760, 470, [(n_, v, C["s16.a"] + 0.15 * i, C["s16.a"] + 0.3 + 0.15 * i) for i, (n_, v) in enumerate(zip(NOMES3, (10, 9, 8)))],
                  s=180)
    igual_bola(c, t, C["s16.a"] + 1.0, xs[2] + 170, 470, "720", r=110, cor=ERRADO)
    regra(c, t, C["s16.a"] + 0.6, xs[0], 470 - 90 - 60, "aceitou o 0", fundo=ERRADO)
    y = 860
    E.foco(c, t, C["s16.b"], 0.5, lambda a: (E.escreve(c, "0", 560, y, 130, "g", ERRADO, a), E.escreve(c, "47", 645, y, 130, "g", TINTA, a)))
    E.foco(c, t, C["s16.b"] + 0.4, 0.5, lambda a: E.escreve(c, "entrou na conta", 920, y - 20, 64, "i", TINTA2, a) if t < C["s16.c"] else None)
    E.foco(c, t, C["s16.c"], 0.5, lambda a: E.escreve(c, "não tem 3 algarismos", 920, y - 20, 64, "g", ERRADO, a))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def conta():
        E.frase(c, t, C["s17.a"], [("conte", "i", 84, CLARO), ("tudo", "g", 84, BR), ("e", "i", 84, CLARO), ("tire", "i", 84, CLARO),
                                   ("o", "i", 84, CLARO), ("que", "i", 84, CLARO), ("não", "g", 84, BR), ("pode", "g", 84, BR)], W / 2, 190, "center", passo=0.15)
        y1, y2 = 400, 700
        E.frase(c, t, C["s17.b"], [("tudo", "g", 60, BR)], XE, y1 + 20)
        xs = casinhas(c, t, 800, y1, [("", v, C["s17.b"] + 0.15 * i, C["s17.b"] + 0.3 + 0.15 * i) for i, v in enumerate((10, 9, 8))], s=150, escuro=True)
        igual_bola(c, t, C["s17.b"] + 0.9, xs[2] + 140, y1, "720", r=95, cor=E.COR, escuro=True)
        E.frase(c, t, C["s17.c"], [("com", "i", 56, CLARO), ("0", "g", 60, BR)], XE, y2 - 10)
        E.frase(c, t, C["s17.c"] + 0.2, [("na", "i", 56, CLARO), ("frente", "i", 56, CLARO)], XE, y2 + 50)
        xs = casinhas(c, t, 800, y2, [("", 1, C["s17.c"], C["s17.c"] + 0.2), ("", 9, C["s17.c"] + 0.4, C["s17.c"] + 0.6),
                                      ("", 8, C["s17.c"] + 0.8, C["s17.c"] + 1.0)], s=150, escuro=True)
        E.foco(c, t, C["s17.c"] + 0.2, 0.4, lambda a: E.centro(c, "só o 0", xs[0], y2 + 130, 44, "i", CLARO, a))
        igual_bola(c, t, C["s17.d"], xs[2] + 140, y2, "72", r=95, cor=ERRADO, escuro=True)
        E.formula_em(c, t, C["s17.e"], "720 − 72", 700, 960, 110, "g", BR, "center")
        igual_bola(c, t, C["s17.e"] + 0.5, 1020, 920, "648", r=100, cor=E.COR, escuro=True)
    E.saida(c, t, C["s18"] - 0.1, conta)
    if t < C["s18"]:
        return
    E.frase(c, t, C["s18.a"], ps("cada número da conta grande", "i", 76, CLARO), W / 2, 220, "center", passo=0.15)
    E.frase(c, t, C["s18.a"] + 1.2, [("ou", "i", 84, CLARO), ("é", "i", 84, CLARO), ("proibido,", "g", 84, BR), ("ou", "i", 84, CLARO), ("não", "g", 84, BR)],
            W / 2, 330, "center")
    E.foco(c, t, C["s18.b"], 0.5, lambda a: E.pilula(c, "compensa", 520, 560, 56, estilo="g", fundo=CERTO, a=a))
    E.frase(c, t, C["s18.b"] + 0.3, ps("proibido fácil de contar", "i", 66, BR), 800, 580)
    E.foco(c, t, C["s18.c"], 0.5, lambda a: E.pilula(c, "não compensa", 520, 780, 56, estilo="g", fundo=ERRADO, a=a))
    E.frase(c, t, C["s18.c"] + 0.3, ps("proibido em muitos casos:", "i", 66, BR), 800, 770)
    E.frase(c, t, C["s18.c"] + 1.2, [("conte", "g", 66, BR), ("direto", "g", 66, BR)], 800, 850)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s19"] + 0.1, [("hora", "i", 72, COR), ("de", "i", 72, COR), ("testar", "i", 72, COR)], XE, 190)
    E.frase(c, t, C["s19.a"], ps("quantos números de", "i", 88), XE, 380)
    E.frase(c, t, C["s19.a"] + 0.8, [("2", "g", 96, COR), ("algarismos", "i", 88)], XE, 500)
    E.frase(c, t, C["s19.a"] + 1.4, [("diferentes", "g", 88)], XE, 620)
    E.frase(c, t, C["s19.a"] + 2.0, [("são", "i", 88), ("pares?", "g", 96, COR)], XE, 740)
    E.frase(c, t, C["s19.b"], ps("par termina em", "i", 60, TINTA2), XE, 900)
    E.frase(c, t, C["s19.b"] + 0.4, [("0,", "g", 64, COR), ("2,", "g", 64, COR), ("4,", "g", 64, COR), ("6", "g", 64, COR), ("ou", "i", 60, TINTA2),
                                     ("8", "g", 64, COR)], XE + 440, 900, passo=0.35)
    E.relogio(c, t, C["s20.a"], 1450, 440, 200)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    E.foco(c, t, C["s21.a"], 0.5, lambda a: E.pilula(c, "separe em casos", W / 2, 150, 50, estilo="g", a=a))
    ya, yb, cxr = 370, 760, 820
    E.frase(c, t, C["s21.b"], [("termina", "i", 60), ("em", "i", 60), ("0", "g", 68, COR)], XE, ya + 20)
    xs = casinhas(c, t, cxr, ya, [("dezena", 9, C["s21.b"] + 0.3, C["s21.b"] + 1.4), ("unidade", "0", C["s21.b"] + 0.4, C["s21.b"] + 0.5, "fixo")],
                  s=160, gap=70)
    nota(c, t, C["s21.b"] + 1.6, xs[0], ya + 80 + 120, "1 a 9")
    igual_bola(c, t, C["s21.c"], xs[1] + 150, ya, "9", r=90)
    if t >= C["s22"]:
        E.frase(c, t, C["s22.a"], [("termina", "i", 60), ("em", "i", 60), ("2,", "g", 68, COR), ("4,", "g", 68, COR), ("6,", "g", 68, COR),
                                   ("8", "g", 68, COR)], XE, yb + 20, passo=0.3)
        xs = casinhas(c, t, cxr + 260, yb, [("dezena", 8, C["s22.a"] + 0.3, C["s22.c"]), ("unidade", 4, C["s22.a"] + 0.4, C["s22.a"] + 1.4)],
                      s=160, gap=70, tx=[C["s22.d"] - 0.3])
        regra(c, t, C["s22.b"], xs[0], yb - 80 - 50, "sem 0 e sem o da unidade", fundo=ERRADO, size=34)
        igual_bola(c, t, C["s22.d"], xs[1] + 150, yb, "32", r=90)
        E.formula_em(c, t, C["s22.e"], "9 + 32", XE, 1010, 96, "g", TINTA)
        igual_bola(c, t, C["s22.e"] + 0.5, 520, 976, "41", r=90, cor=CERTO)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s23"], [("resumindo", "i", 92, COR)], W / 2, 210, "center")
        for i, (k, l1, l2) in enumerate((("s23.a", "comece pela casinha", "mais difícil"), ("s23.b", "ela muda as outras?", "separe em casos e some"))):
            y = 430 + i * 260
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 300, y + 10, 56, a=a), centro(c, str(i + 1), 300, y + 33, 64, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, ps(l1, "i", 72), 400, y - 10)
            E.frase(c, t, C[k] + 0.6, [(l2, "g", 100, COR)], 400, y + 95)
    E.saida(c, t, C["s24"] - 0.1, resumo)
    if t < C["s24"]:
        return
    E.frase(c, t, C["s24"] + 0.1, ps("próxima aula", "i", 84), XE, 300)
    E.frase(c, t, C["s24.a"], [("contar", "g", 140, COR)], XE, 450)
    E.frase(c, t, C["s24.a"] + 0.3, [("divisores", "g", 140, COR)], XE, 600)
    E.frase(c, t, C["s24.b"], [("do", "i", 80), ("72,", "g", 76), ("sem", "i", 80), ("listar", "i", 80)], XE, 730)
    E.foco(c, t, C["s24.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1430, 400, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s24.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1760, 1560, p), lerp(720, 425, p), ep(t, C["s24.c"] + 0.2, 0.4))
    E.frase(c, t, C["s24.d"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 920, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, regras=b_regras, casinhas=b_casinhas, casos=b_casos, erro=b_erro, atalho=b_atalho,
              questao=b_questao, resposta=b_resposta, fim=b_fim)
