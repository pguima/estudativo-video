"""Visual — Estudativo · MAT-EST-002: tabela de frequência e classes.
Mesma linguagem da Estatística definida em MAT-EST-001 (docstring de lá): cada categoria com a sua cor de E._paleta, na
bolinha da tabela, na ficha da lista e na fatia da barra de 100%; tabela (quadro()) que entra coluna a coluna, célula no
marcador em que a fala diz o número, a coluna da vez na cor da matéria; frequência relativa = barra de 100% (barra100());
lista de dados = fichas (fichas()) que acendem na cor da categoria quando são contadas.
Novo nesta aula (para copiar nas próximas): classe(20, 30) desenha o rótulo "20 ⊢ 30" (a fonte não tem o sinal ⊢) e serve de
célula do quadro(); nas classes, as cores vêm de E._paleta(5), na ordem das classes.
Sem voz ainda: todo instante vem de C[...] (marcadores do roteiro), para acompanhar a voz real quando ela chegar."""
import math
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Estatística")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-EST-002_tabela_de_frequencia_e_classes.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("absoluta", "classes", "acumulada", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
PAPEL = E.PAPEL
CATS = E._paleta(4)    # ônibus, carro, bicicleta, a pé
CLS = E._paleta(5)     # as classes 10 ⊢ 20 ... 50 ⊢ 60
TRANSP = ["ônibus", "carro", "ônibus", "a pé", "bicicleta", "ônibus", "carro", "ônibus", "bicicleta", "a pé",
          "ônibus", "carro", "ônibus", "bicicleta", "carro", "ônibus", "a pé", "bicicleta", "carro", "ônibus"]
NOMES = ["ônibus", "carro", "bicicleta", "a pé"]
IDADES = [18, 23, 25, 31, 34, 19, 42, 27, 36, 30, 22, 45, 29, 38, 51, 26, 33, 40, 24, 37]
QUEST = [17, 22, 35, 28, 40, 19, 31, 20, 26, 45]
assert [TRANSP.count(n) for n in NOMES] == [8, 5, 4, 3] and len(TRANSP) == 20
assert [sum(1 for v in IDADES if 10 * k <= v < 10 * k + 10) for k in range(1, 6)] == [2, 7, 7, 3, 1]
assert [sum(1 for v in QUEST if 10 * k <= v < 10 * k + 10) for k in range(1, 5)] == [2, 4, 2, 2]
assert 8 * 100 // 20 == 40 and 5 * 5 == 25 and 4 * 5 == 20 and 3 * 5 == 15 and 40 + 25 + 20 + 15 == 100 and 7 * 5 == 35 and 2 * 5 == 10


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças comuns ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    """uma frase, palavra a palavra (palavra com %, ², ³ ou → vai na grotesca)"""
    return [(w, "g" if any(ch in w for ch in "%²³→") else est, size * (0.92 if any(ch in w for ch in "%²³→") and est != "g" else 1), cor) for w in txt.split()]


def fcen(c, t, t0, s, cx, y, size, cor=None):
    E.formula_em(c, t, t0, s, cx, y, size, "g", cor, "center")


def bola_txt(c, t, t0, s, cx, cy, r, size, cor=None):
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r * ease_back(prog(t, t0, 0.5)), cor, a),
                                     E.formula(c, s, cx, cy + size * 0.36, size, "g", E.SOBRE, a, "center")))


def fase(c, t, t0, t1, fn):
    if t0 - 0.01 <= t < t1 + 0.4:
        E.saida(c, t, t1, fn)


# ================= peças da Estatística (as de MAT-EST-001, mais classe()) =================
# ================= peças da Estatística (copiar nas próximas aulas) =================
def pessoas(c, t, t0, x, y, cols, lins, passo, r, estado=None, d=0.9):
    """a população em bolinhas: grade cols x lins a partir de (x, y), em onda da esquerda para a direita.
    estado(i, j) -> (cor, anel) muda a bolinha (cor None = cor da matéria; anel True = da amostra). Devolve os centros"""
    pts = []
    for j in range(lins):
        for i in range(cols):
            cx, cy = x + i * passo, y + j * passo
            k = ease_back(prog(t, t0 + d * (i / max(1, cols - 1)) * 0.8 + 0.02 * j, 0.35))
            cor, anel = (estado(i, j) if estado else (None, False))
            if k > 0:
                c.drawCircle(cx, cy, r * k, M.paint(cor or E.COR))
                if anel:
                    c.drawCircle(cx, cy, (r + 7) * k, M.paint(TINTA, 1, stroke=4))
            pts.append((cx, cy))
    return pts


def _cel(c, s, cx, y, size, estilo, cor, a):
    """célula da tabela: texto centrado, ou uma função (c, cx, y, size, cor, a) que desenha, como classe()"""
    if callable(s):
        s(c, cx, y, size, cor, a)
    else:
        centro(c, s, cx, y, size, estilo, cor, a)


def classe(ini, fim):
    """rótulo de classe "20 ⊢ 30" (o primeiro entra, o último não), desenhado: a fonte não tem o sinal.
    Devolve uma função para usar como célula do quadro() ou chamar direto: classe(20, 30)(c, cx, y, size, cor, a)"""
    def fn(c, cx, y, size, cor, a):
        s1, s2 = str(ini), str(fim)
        w1, w2 = E.larg(s1, "g", size), E.larg(s2, "g", size)
        gap = size * 1.05
        x0 = cx - (w1 + gap + w2) / 2
        E.escreve(c, s1, x0, y, size, "g", cor, a)
        sx, sy = x0 + w1 + size * 0.28, y - size * 0.36
        M.line(c, sx, sy - size * 0.32, sx, sy + size * 0.32, cor, a, max(3, size * 0.09))
        M.line(c, sx, sy, sx + gap - size * 0.56, sy, cor, a, max(3, size * 0.09))
        E.escreve(c, s2, x0 + w1 + gap, y, size, "g", cor, a)
    return fn


def quadro(c, t, x, y, colunas, linhas, total=None, size=58, h_lin=None, cores=None, t_fio=None):
    """tabela de dados que entra coluna a coluna. colunas = [(título, largura, t0)]; linhas = [[(texto, t0[, cor]), ...], ...];
    total = [(texto, t0[, cor]), ...] depois de um fio grosso; o texto pode ser uma função que desenha (classe(20, 30)); cores = cor de cada linha (bolinha antes da 1ª coluna).
    (x, y) = canto de cima à esquerda; devolve o y da linha de base de cada linha"""
    h_lin = h_lin or size * 1.55
    xs = [x]
    for _, w, _ in colunas:
        xs.append(xs[-1] + w)
    larg = xs[-1] - x
    t_cab = min(ti for _, _, ti in colunas)
    p = ease_io(prog(t, t_fio if t_fio is not None else t_cab, 0.6))
    if p > 0:
        M.line(c, x, y + 20, x + larg * p, y + 20, TINTA, 1, 3)
    for k, (tit, w, ti) in enumerate(colunas):
        cx = xs[k] + w / 2
        E.foco(c, t, ti, 0.45, lambda a, tit=tit, cx=cx: centro(c, tit, cx, y - 6, size * 0.78, "i", TINTA2, a))
    bases = []
    for j, lin in enumerate(linhas):
        yy = y + 20 + h_lin * (j + 1) - h_lin * 0.3
        bases.append(yy)
        for k, cel in enumerate(lin):
            s, ti, *cc = cel
            if s == "":
                continue
            cx = xs[k] + colunas[k][1] / 2
            if k == 0 and cores:
                E.foco(c, t, ti, 0.4, lambda a, yy=yy, j=j: c.drawCircle(xs[0] + 22, yy - size * 0.34, size * 0.24, M.paint(cores[j], a)))
                cx += 22
            E.foco(c, t, ti, 0.4, lambda a, s=s, cx=cx, yy=yy, cc=cc, k=k: _cel(c, s, cx, yy, size, "b" if k == 0 else "g", cc[0] if cc else TINTA, a))
    if total:
        yf = y + 20 + h_lin * len(linhas) + 8
        tt = min(cel[1] for cel in total if cel[0] != "")
        q = ease_io(prog(t, tt, 0.5))
        if q > 0:
            M.line(c, x, yf, x + larg * q, yf, TINTA, 1, 6)
        yy = yf + h_lin * 0.72
        bases.append(yy)
        for k, cel in enumerate(total):
            s, ti, *cc = cel
            if s == "":
                continue
            cx = xs[k] + colunas[k][1] / 2 + (22 if k == 0 and cores else 0)
            E.foco(c, t, ti, 0.4, lambda a, s=s, cx=cx, cc=cc, k=k: centro(c, s, cx, yy, size, "i" if k == 0 else "g", cc[0] if cc else TINTA, a))
    return bases


def barra100(c, t, t0, x, y, w, h, partes, cores=None, rotulos=None, size=46, d=1.0, a=1.0):
    """frequência relativa: barra deitada de 100% dividida nas fatias das categorias (partes em %), cada fatia entra no seu
    tempo (t0 número = em fila; lista = um instante por fatia) e ganha a % (ou o rótulo) dentro"""
    cores = cores or E._paleta(len(partes))
    tot = float(sum(partes))
    ts = t0 if isinstance(t0, (list, tuple)) else [t0 + d * i / len(partes) for i in range(len(partes))]
    xa = x
    r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 14, 14)
    if t >= min(ts):
        c.save(); c.clipRRect(r, True)
        c.drawRect(skia.Rect.MakeXYWH(x, y, w, h), M.paint(E.mix(FIO, PAPEL, 0.5), a))
        for i, v in enumerate(partes):
            wi = w * v / tot
            q = ease_io(prog(t, ts[i], 0.5))
            if q > 0:
                c.drawRect(skia.Rect.MakeXYWH(xa, y, wi * q, h), M.paint(cores[i], a))
            xa += wi
        c.restore()
        xa = x
        for i, v in enumerate(partes):
            wi = w * v / tot
            if i:
                M.line(c, xa, y, xa, y + h, PAPEL, a * ep(t, ts[i], 0.4), 5)
            s = rotulos[i] if rotulos else E._num(v) + "%"
            cor_t = BR if M.lum(cores[i]) < 0.5 else TINTA
            E.foco(c, t, ts[i] + 0.3, 0.4, lambda q, s=s, xa=xa, wi=wi, cor_t=cor_t: centro(c, s, xa + wi / 2, y + h / 2 + size * 0.36, size, "g", cor_t, q * a))
            xa += wi
        c.drawRRect(r, M.paint(TINTA, a * ep(t, min(ts), 0.4), stroke=3))


def ficha(c, s, cx, cy, size, a=1.0, cor=None, borda=None):
    """um dado da lista: pílula branca com borda fina (cor = fundo aceso)"""
    if a <= 0:
        return
    w = E.larg(s, "b", size) + size * 1.1
    h = size * 1.55
    rr = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2, cy - h / 2, w, h), h / 2, h / 2)
    c.drawRRect(rr, M.paint(cor or BR, a))
    c.drawRRect(rr, M.paint(borda or (cor or FIO), a, stroke=3))
    centro(c, s, cx, cy + size * 0.36, size, "b", (BR if cor and M.lum(cor) < 0.5 else TINTA), a)


def fichas(c, t, t0, itens, x, y, w, size=44, gap=22, passo=0.06, voa=None, esconde=()):
    """lista de dados em grade de fichas, da esquerda para a direita. itens = [(texto[, cor acesa, t_acende])].
    voa = {índice: (x, y, t)} faz a ficha voar até (x, y) a partir de t; esconde = índices que não se desenham (a ficha
    saiu da lista e é desenhada à parte), mas guardam o lugar. Devolve os centros"""
    cx, cy, centros = x, y, []
    h = size * 1.55
    for i, it in enumerate(itens):
        s = it[0]
        wi = E.larg(s, "b", size) + size * 1.1
        if cx + wi > x + w:
            cx, cy = x, cy + h + gap
        px, py = cx + wi / 2, cy
        if voa and i in voa:
            vx, vy, tv = voa[i]
            q = ease_io(prog(t, tv, 0.7))
            px, py = lerp(px, vx, q), lerp(py, vy, q)
        cor = it[1] if len(it) > 1 and t >= it[2] else None
        if i not in esconde:
            E.foco(c, t, t0 + passo * i, 0.4, lambda a, s=s, px=px, py=py, cor=cor: ficha(c, s, px, py, size, a, cor), sobe=8)
        centros.append((px, py))
        cx += wi + gap
    return centros


def caixa_tipo(c, t, t0, x, y, w, h, titulo, sub, cor=None):
    """a caixa de um tipo de variável: pontilhada, com o nome em cima"""
    p = ep(t, t0, 0.5)
    E.caixa_pontilhada(c, x, y, w, h, p, cor, prog_=p)
    E.foco(c, t, t0 + 0.1, 0.4, lambda a: (centro(c, titulo, x + w / 2, y - 70, 70, "g", cor or COR, a),
                                          centro(c, sub, x + w / 2, y - 18, 44, "i", TINTA2, a)))


# ---------------- peças desta aula ----------------
# ---------------- peças desta aula ----------------
def classe_de(v):
    return v // 10 - 1    # 18 → 0 (10 ⊢ 20), 23 → 1 ...


def cont_t(ts, i):
    """instante em que a i-ésima ficha de transporte acende: na hora em que a fala diz o meio de transporte dela"""
    return ts[NOMES.index(TRANSP[i])]


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    a1, b1, c1 = C["s01.a"], C["s01.b"], C["s01.c"]

    def um():
        itens = [(s, CATS[NOMES.index(s)], c1 + 0.3) for s in TRANSP]
        fichas(c, t, a1, itens, 140, 330, 980, size=40, gap=18, passo=0.05)
        E.frase(c, t, a1 + 0.2, [("20 pessoas:", "g", 64, COR)] + ps("como vão ao trabalho?", "i", 60), 140, 220, "left", 0.1)
        E.frase(c, t, b1, ps("lista solta:", "i", 56) + [("ninguém entende", "g", 60, ERRADO)], 140, 900, "left", 0.1)
        cols = [("transporte", 300, c1), ("pessoas", 200, c1)]
        linhas = [[(n, c1 + 0.2 + 0.2 * k), (str(TRANSP.count(n)), c1 + 0.4 + 0.2 * k)] for k, n in enumerate(NOMES)]
        quadro(c, t, 1260, 360, cols, linhas, size=54, cores=CATS)
        E.frase(c, t, c1 + 1.2, ps("na tabela:", "i", 56) + [("de uma olhada", "g", 60, CERTO)], 1260, 900, "left", 0.1)
    E.saida(c, t, C["s02"] - 0.1, um)

    if t >= C["s02"]:
        ta, tb = C["s02.a"], C["s02.b"]
        E.foco(c, t, tb - 0.2, 0.7, lambda a: E.bola(c, 1560, 600, 240 * ease_back(prog(t, tb - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, ps("até o fim desta aula", "i", 88), XE, 280, passo=0.14)
        E.frase(c, t, ta + 1.4, [("tabela", "g", 100, COR)] + ps("de frequência", "i", 88), XE, 430, passo=0.14)
        E.frase(c, t, ta + 3.2, ps("idades de", "i", 88) + [("10 em 10", "g", 100, COR)], XE, 580, passo=0.14)
        E.foco(c, t, tb + 0.1, 0.5, lambda a: (centro(c, "+ atalho", 1560, 575, 80, "g", E.SOBRE, a),
                                               centro(c, "de prova", 1560, 660, 80, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"] + 0.3, ps("você só precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "2", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 980, 820
    itens = (("s03.b", "o que é variável:", "qualitativa ou quantitativa"), ("s03.c", "quantos % a parte é do total:", "parte ÷ total"))
    for i, (k, l1, l2) in enumerate(itens):
        y = 260 + i * 280
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 210, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, ps(l1, "i", 54), x + 44, y + 84, "left", 0.1)
        E.formula_em(c, t, C[k] + 0.6, l2, x + 44, y + 170, 60, "g", COR)
    alvo = [260 + i * 280 + 180 for i in range(2)]
    q1 = ease_io(prog(t, C["s03.c"] - 0.35, 0.5))
    E.cursor(c, x + w - 30, lerp(alvo[0], alvo[1], q1), ep(t, C["s03.b"], 0.4))
    E.frase(c, t, lerp(C["s03.c"], C["s03.end"], 0.72), ps("faltou?", "i", 54, COR) + ps("procure no canal", "i", 54), x, 900, "left", 0.1)


# ---------------- frequência absoluta e relativa ----------------
TX, TY = 1040, 300


def tabela_transp(c, t, C, rel=True):
    """a tabela do transporte: transporte, absoluta e (depois) relativa"""
    b4, c4, d4 = C["s04.b"], C["s04.c"], C["s04.d"]
    ts = [lerp(b4, c4, k / 4) for k in range(4)]
    vez = lambda ti, prox: COR if ti <= t < prox else TINTA
    tr = [C["s05.c"], C["s06.a"], C["s06.b"], C["s06.c"]]
    cols = [("transporte", 300, C["s04.a"]), ("absoluta", 220, b4 - 0.3)]
    if rel:
        cols.append(("relativa", 220, C["s05.a"]))
    linhas = []
    for k, n in enumerate(NOMES):
        lin = [(n, C["s04.a"] + 0.3 + 0.2 * k), (str(TRANSP.count(n)), ts[k] + 0.2, vez(ts[k], c4))]
        if rel:
            lin.append((f"{TRANSP.count(n) * 5}%", tr[k], vez(tr[k], C["s06.d"])))
        linhas.append(lin)
    total = [("total", d4), ("20", d4, COR if d4 <= t < C["s05"] else TINTA)]
    if rel:
        total.append(("100%", C["s06.d"], COR))
    quadro(c, t, TX, TY, cols, linhas, total, size=54, cores=CATS)
    if C["s04.c"] <= t < C["s05"]:
        p = ep(t, c4, 0.4)
        E.caixa_pontilhada(c, TX + 300 - 6, TY - 60, 232, 470, p, None, prog_=p)
    return ts


def b_absoluta(c, t, C, b):
    a4, b4, c4, d4 = (C[f"s04.{k}"] for k in "abcd")
    ts = [lerp(b4, c4, k / 4) for k in range(4)]
    itens = [(s, CATS[NOMES.index(s)], cont_t(ts, i)) for i, s in enumerate(TRANSP)]
    fichas(c, t, C["s04"], itens, 140, 330, 820, size=38, gap=16, passo=0.04)
    tabela_transp(c, t, C, rel=False)
    E.frase(c, t, a4, ps("misturados na lista", "i", 54, TINTA2), 140, 220, "left", 0.1)
    E.frase(c, t, c4, ps("a contagem:", "i", 58) + [("frequência absoluta", "g", 62, COR)], 140, 880, "left", 0.1)
    E.frase(c, t, d4, ps("a soma dá o", "i", 58) + [("total: 20", "g", 62, COR)], 140, 980, "left", 0.1)


def b_relativa(c, t, C, b):
    a5, b5, c5 = C["s05.a"], C["s05.b"], C["s05.c"]
    a6, b6, c6, d6 = (C[f"s06.{k}"] for k in "abcd")
    tabela_transp(c, t, C, rel=True)
    X = 520

    def um():
        E.frase(c, t, a5, [("frequência relativa", "g", 64, COR)], X, 300, "center", 0.1)
        E.frase(c, t, a5 + 1.2, ps("quanto é do total, em %", "i", 54), X, 380, "center", 0.1)
        fcen(c, t, b5, "f{absoluta}{total}", X, 560, 66)
        fcen(c, t, c5, "8 ÷ 20 = 0,4 = 40%", X, 760, 66, COR)
    fase(c, t, C["s05"], C["s06"] - 0.1, um)
    if t >= C["s06"] - 0.1:
        fcen(c, t, a6, "5 ÷ 20 = 25%", X, 330, 64)
        fcen(c, t, b6, "4 ÷ 20 = 20%", X, 460, 64)
        fcen(c, t, c6, "3 ÷ 20 = 15%", X, 590, 64)
        fcen(c, t, d6, "40 + 25 + 20 + 15 = 100%", X, 740, 58, COR)
    barra100(c, t, [c5, a6, b6, c6], 140, 880, 1640, 90, [40, 25, 20, 15], CATS,
             ["ônibus 40%", "carro 25%", "bicicleta 20%", "a pé 15%"], size=38)


# ---------------- classes ----------------
CX0, CY0 = 1060, 300


def idades_fichas(c, t, t0, acende, x=140, y=330, w=820, size=40, voa=None):
    itens = [(str(v), CLS[classe_de(v)], acende(i, v)) for i, v in enumerate(IDADES)]
    return fichas(c, t, t0, itens, x, y, w, size=size, gap=18, passo=0.04, voa=voa)


def tabela_classes(c, t, C, acum=False, abs_cor=None, erro=None):
    """as classes 10 ⊢ 20 ... 50 ⊢ 60 com a absoluta e (acum=True) a acumulada"""
    a8 = C["s08.a"]
    tabs = [C[f"s09.{k}"] for k in "abcde"]
    freqs = [2, 7, 7, 3, 1]
    vez = lambda ti, prox: COR if ti <= t < prox else TINTA
    cols = [("classe (anos)", 340, a8), ("absoluta", 220, tabs[0] - 0.3)]
    if acum:
        cols.append(("acumulada", 240, C["s10.a"]))
    ac = [C["s10.c"], C["s10.d"], C["s10.e"], lerp(C["s10.e"], C["s10.f"], 0.5), C["s10.f"]]
    linhas = []
    for k in range(5):
        f = freqs[k]
        cor_f = vez(tabs[k], C["s09.end"])
        if erro is not None and k in (1, 2):
            f, cor_f = erro[k], (ERRADO if erro[k] != freqs[k] else CERTO)
        lin = [(classe(10 * (k + 1), 10 * (k + 2)), a8 + 0.3 * k), (str(f), tabs[k], cor_f)]
        if acum:
            lin.append((str([2, 9, 16, 19, 20][k]), ac[k], vez(ac[k], C["s11"])))
        linhas.append(lin)
    total = [("total", tabs[4] + 1.0), ("20", tabs[4] + 1.0)] + ([("", 0)] if acum else [])
    return quadro(c, t, CX0, CY0, cols, linhas, total, size=50, cores=CLS)


def b_classes(c, t, C, b):
    a7, b7, c7 = C["s07.a"], C["s07.b"], C["s07.c"]
    a8, b8, c8 = C["s08.a"], C["s08.b"], C["s08.c"]
    tabs = [C[f"s09.{k}"] for k in "abcde"]
    idades_fichas(c, t, a7, lambda i, v: tabs[classe_de(v)])
    E.frase(c, t, a7, ps("e a", "i", 60) + [("idade?", "g", 64, COR)] + ps("20 pessoas:", "i", 60), 140, 220, "left", 0.1)

    def um():
        E.frase(c, t, b7, ps("quase", "i", 56) + [("20 idades diferentes", "g", 60, ERRADO)], 140, 880, "left", 0.1)
        E.frase(c, t, c7, ps("agrupe em", "i", 60) + [("classes", "g", 66, COR)] + ps("de 10 em 10 anos", "i", 60), 140, 990, "left", 0.1)
    fase(c, t, C["s07"], C["s08"] - 0.1, um)
    if t < C["s08"] - 0.1:
        return
    tabela_classes(c, t, C)

    def sinal():
        E.foco(c, t, b8, 0.5, lambda a: classe(20, 30)(c, 520, 880, 110, COR, a))
        E.foco(c, t, b8 + 0.8, 0.4, lambda a: (centro(c, "entra", 405, 970, 46, "g", CERTO, a)))
        E.foco(c, t, b8 + 1.6, 0.4, lambda a: (centro(c, "não entra", 650, 970, 46, "g", ERRADO, a)))
        E.frase(c, t, c8, ps("de", "i", 54) + [("20 até 29", "g", 58, COR)] + ps("anos", "i", 54), 520, 1040, "center", 0.1)
    fase(c, t, C["s08"], C["s09"] - 0.1, sinal)


# ---------------- acumulada ----------------
def b_acumulada(c, t, C, b):
    a0, b0, c0, d0, e0, f0 = (C[f"s10.{k}"] for k in "abcdef")
    a1, b1, c1, d1 = (C[f"s11.{k}"] for k in "abcd")
    bases = tabela_classes(c, t, C, acum=True)
    X = 520

    def um():
        E.frase(c, t, a0, [("frequência acumulada", "g", 60, COR)], X, 300, "center", 0.1)
        E.frase(c, t, b0, ps("quantos até aquela classe:", "i", 52), X, 400, "center", 0.1)
        E.frase(c, t, b0 + 1.4, ps("soma de cima para baixo", "i", 52), X, 470, "center", 0.1)
        fcen(c, t, d0, "2 + 7 = 9", X, 620, 64)
        fcen(c, t, e0, "9 + 7 = 16", X, 730, 64)
        fcen(c, t, lerp(e0, f0, 0.5), "16 + 3 = 19", X, 840, 64)
        fcen(c, t, f0, "19 + 1 = 20", X, 950, 64, COR)
    fase(c, t, C["s10"], C["s11"] - 0.1, um)
    if t < C["s11"] - 0.1:
        return
    # menos de 40 anos: as três primeiras classes
    p = ep(t, a1, 0.5)
    y0, y1 = bases[0] - 68, bases[2] + 22
    E.caixa_pontilhada(c, CX0 - 16, y0, 832, y1 - y0, p, None, prog_=p)
    E.frase(c, t, a1, ps("quantos têm", "i", 56) + [("menos de 40?", "g", 60, COR)], X, 320, "center", 0.1)
    bola_txt(c, t, b1, "16", X, 500, 110, 96)
    E.frase(c, t, b1 + 0.5, ps("direto da tabela", "i", 48, TINTA2), X, 680, "center", 0.1)
    E.frase(c, t, c1, ps("a última acumulada =", "i", 52) + [("o total", "g", 56, COR)], X, 830, "center", 0.1)
    E.frase(c, t, d1, ps("se não der:", "i", 52) + [("faltou alguém", "g", 56, ERRADO)], X, 930, "center", 0.1)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    a2, b2, c2, d2, e2 = (C[f"s12.{k}"] for k in "abcde")
    i30 = IDADES.index(30)
    if t < c2:
        err = None
    elif t < e2:
        err = {1: 8, 2: 6}
    else:
        err = {1: 7, 2: 7}
    # a ficha do 30 voa para a classe errada e depois para a certa
    bases = tabela_classes(c, t, C, erro=err)
    q1 = ease_io(prog(t, b2 + 1.0, 0.8))
    q2 = ease_io(prog(t, e2, 0.8))
    itens = [(str(v), CLS[classe_de(v)], -1) for v in IDADES]
    pts = fichas(c, t, -9, itens, 140, 330, 820, size=40, gap=18, passo=0, esconde=(i30,) if t >= b2 else ())
    ox, oy = pts[i30]
    if t >= b2:
        dx1, dy1 = CX0 + 340 + 220 + 120, bases[1] - 18
        dx2, dy2 = CX0 + 340 + 220 + 120, bases[2] - 18
        px, py = lerp(lerp(ox, dx1, q1), dx2, q2), lerp(lerp(oy, dy1, q1), dy2, q2)
        cor = ERRADO if t < e2 else CERTO
        ficha(c, "30", px, py, 44, 1.0, cor)
    E.frase(c, t, C["s12"] + 0.2, [("erro comum:", "g", 60, ERRADO)] + ps("a borda da classe", "i", 56), 140, 220, "left", 0.1)
    E.frase(c, t, c2, ps("sai", "i", 56) + [("8 e 6", "g", 60, ERRADO)] + ps("no lugar de", "i", 56) + [("7 e 7", "g", 60, CERTO)], 140, 880, "left", 0.1)
    E.frase(c, t, d2, ps("30 fica", "i", 56) + [("fora", "g", 60, ERRADO)] + ps("de", "i", 56), 140, 990, "left", 0.1)
    E.foco(c, t, d2 + 0.4, 0.4, lambda a: classe(20, 30)(c, 590, 990, 56, TINTA, a))
    E.foco(c, t, e2 + 0.6, 0.5, lambda a: E.pilula(c, "30 entra em 30 ⊢ 40".replace(" ⊢ ", " a "), 1460, 1000, 50, "g", fundo=CERTO, a=a))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    a3, b3, c3, d3 = (C[f"s13.{k}"] for k in "abcd")
    a4, b4, c4, d4 = (C[f"s14.{k}"] for k in "abcd")

    def um():
        E.frase(c, t, C["s13"] + 0.2, ps("o atalho da relativa:", "i", 64, CLARO), W / 2, 180, "center", 0.1)
        E.frase(c, t, a3, ps("faça o total virar", "i", 72, CLARO) + [("100", "g", 80, BR)], W / 2, 290, "center", 0.1)
        fcen(c, t, b3, "20 × 5 = 100", W / 2, 450, 90, BR)
        fcen(c, t, c3, "f{7}{20} = f{35}{100} = 35%", W / 2, 680, 92, BR)
        fcen(c, t, d3, "f{2}{20} = f{10}{100} = 10%", W / 2, 920, 92, CLARO)
    fase(c, t, C["s13"], C["s14"] - 0.1, um)
    if t < C["s14"] - 0.1:
        return
    E.frase(c, t, C["s14"] + 0.2, ps("funciona porque", "i", 62, CLARO), W / 2, 180, "center", 0.1)
    E.frase(c, t, a4, ps("a fração equivalente", "i", 66, CLARO) + [("não muda o valor", "g", 70, BR)], W / 2, 300, "center", 0.1)
    E.frase(c, t, b4, ps("com", "i", 62, CLARO) + [("100", "g", 66, BR)] + ps("embaixo, o de cima", "i", 62, CLARO) + [("já é a %", "g", 66, BR)], W / 2, 430, "center", 0.1)
    E.foco(c, t, c4, 0.5, lambda a: E.selo(c, 520, 620, 46, False, a))
    E.frase(c, t, c4 + 0.1, ps("não compensa: total", "i", 62, CLARO) + [("37", "g", 66, BR)], 600, 645, "left", 0.1)
    E.foco(c, t, d4, 0.5, lambda a: E.pilula(c, "absoluta ÷ total", W / 2, 820, 66, "g", a=a, cor=E.SOBRE))


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    a5, b5, c5 = C["s15.a"], C["s15.b"], C["s15.c"]
    E.frase(c, t, C["s15"] + 0.1, ps("hora de testar", "i", 72, COR), XE, 180, passo=0.12)
    E.frase(c, t, a5, ps("idades de", "i", 58) + [("10 alunos:", "g", 62, COR)], XE, 290, passo=0.1)
    fichas(c, t, a5 + 0.4, [(str(v),) for v in QUEST], XE, 380, 1000, size=46, gap=22, passo=0.06)
    E.frase(c, t, b5, [("1)", "g", 60, COR)] + ps("tabela em classes de", "i", 58) + [("10 em 10", "g", 62, COR)], XE, 620, passo=0.1)
    E.frase(c, t, b5 + 2.2, ps("com absoluta e acumulada", "i", 54, TINTA2), XE + 60, 700, passo=0.1)
    E.frase(c, t, c5, [("2)", "g", 60, COR)] + ps("quantos % têm", "i", 58) + [("menos de 30?", "g", 62, COR)], XE, 840, passo=0.1)
    E.relogio(c, t, C["s16.a"], 1560, 560, 190)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    a7, b7, c7, d7 = (C[f"s17.{k}"] for k in "abcd")
    a8, b8, c8, d8 = (C[f"s18.{k}"] for k in "abcd")
    tabs = [a7, b7, c7, d7]
    cl4 = E._paleta(4)
    fichas(c, t, -9, [(str(v), cl4[classe_de(v)], tabs[classe_de(v)]) for v in QUEST], 140, 220, 1700, size=44, gap=22, passo=0)
    vez = lambda ti, prox: COR if ti <= t < prox else TINTA
    ac = [a8, lerp(a8, b8, 0.33), lerp(a8, b8, 0.66), b8]
    cols = [("classe (anos)", 340, C["s17"]), ("absoluta", 220, C["s17"]), ("acumulada", 240, a8 - 0.3)]
    linhas = [[(classe(10 * (k + 1), 10 * (k + 2)), C["s17"] + 0.2 * k), (str([2, 4, 2, 2][k]), tabs[k], vez(tabs[k], C["s18"])),
               (str([2, 6, 8, 10][k]), ac[k], vez(ac[k], c8))] for k in range(4)]
    bases = quadro(c, t, 140, 400, cols, linhas, [("total", d7 + 1.0), ("10", d7 + 1.0), ("", 0)], size=50, cores=cl4)
    if t >= c8:
        p = ep(t, c8, 0.5)
        y0, y1 = bases[0] - 64, bases[1] + 22
        E.caixa_pontilhada(c, 124, y0, 832, y1 - y0, p, None, prog_=p)
    X = 1450
    if t < C["s18"]:
        for k, (v, ti) in enumerate(((20, b7), (40, d7))):
            E.frase(c, t, ti + 0.2, ps(f"o {v} entra em", "i", 50, TINTA2), X - 100, 400 + 110 * k, "center", 0.1)
            E.foco(c, t, ti + 0.6, 0.4, lambda a, v=v, k=k: classe(v, v + 10)(c, X + 170, 400 + 110 * k, 50, TINTA2, a))
    E.frase(c, t, c8, ps("menos de 30:", "i", 58) + [("6 de 10", "g", 62, COR)], X, 600, "center", 0.1)
    fcen(c, t, d8, "6 × 10 = 60", X - 140, 800, 72)
    bola_txt(c, t, d8 + 0.6, "60%", X + 230, 780, 110, 68)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s19"], [("resumindo", "i", 92, COR)], W / 2, 200, "center")
        itens = (("s19.a", ps("a", "i", 64) + [("absoluta", "g", 70, COR)] + ps("conta", "i", 64)),
                 ("s19.b", ps("a", "i", 64) + [("relativa", "g", 70, COR)] + ps("divide pelo total", "i", 64)),
                 ("s19.c", ps("a", "i", 64) + [("acumulada", "g", 70, COR)] + ps("vai somando", "i", 64)),
                 ("s19.d", ps("na classe, o 1º", "i", 64) + [("entra", "g", 70, CERTO)] + ps("e o último", "i", 64) + [("não", "g", 70, ERRADO)]))
        for i, (k, partes) in enumerate(itens):
            y = 380 + i * 165
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 240, y - 25, 50, a=a), centro(c, str(i + 1), 240, y - 4, 58, "g", E.SOBRE, a)))
            E.frase(c, t, C[k] + 0.1, partes, 330, y, "left", 0.1)
    E.saida(c, t, C["s20"] - 0.1, resumo)
    if t < C["s20"]:
        return
    a0, b0, c0, d0, e0 = (C[f"s20.{k}"] for k in "abcde")
    E.frase(c, t, C["s20"] + 0.2, ps("na próxima aula", "i", 80), XE, 250, passo=0.12)
    E.frase(c, t, a0, [("gráficos", "g", 120, COR)] + ps("de barras e de linhas", "i", 80), XE, 410)
    E.frase(c, t, b0, ps("o período de", "i", 56) + [("maior alta", "g", 60, COR)], XE, 540, passo=0.1)
    E.frase(c, t, c0, ps("e a", "i", 56) + [("variação em %", "g", 60, COR)], XE, 630, passo=0.1)
    E.foco(c, t, d0, 0.5, lambda a: E.pilula(c, "Inscreva-se", 1550, 380, 76, estilo="g", a=a, cor=E.SOBRE))
    p = ease_io(prog(t, d0 + 0.3, 0.8))
    E.cursor(c, lerp(1830, 1680, p), lerp(700, 405, p), ep(t, d0 + 0.2, 0.4))
    E.frase(c, t, e0, [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 980, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, absoluta=b_absoluta, relativa=b_relativa, classes=b_classes,
              acumulada=b_acumulada, erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
