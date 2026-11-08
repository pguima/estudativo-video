"""Visual — Estudativo · MAT-LEI-003: desenhar o problema, barras e tabelas.

Linguagem da trilha Leitura de Problemas (as peças abaixo de "linguagem da trilha" servem a todas as aulas MAT-LEI):
- enunciado(): o problema num cartão branco com fio da cor da matéria. Os números são escritos em grotesca; a pergunta fica numa
  linha própria. marca = marca-texto da cor da matéria (dado útil), aponta = caixa pontilhada (dado em dúvida),
  risca = traço vermelho e número cinza (dado que não entra na conta).
- pessoa(): ícone simples para a quantidade que só existe inteira.
- tira(): blocos iguais lado a lado (o filho é 1 bloco, o Pedro são 3); barra(): o total cortado em partes iguais.
- tabela(): cabeçalho na cor da matéria e uma linha por palpite; a linha da resposta acende em verde.
Aula ainda sem voz: todo instante vem só de C[...] (marcadores do roteiro), para acompanhar a voz real quando ela chegar."""
import re
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Leitura de Problemas")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-LEI-003_desenhar_o_problema_barras_e_tabelas.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("barra2", "tabela", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
# as contas da aula, conferidas
assert 600 // 3 == 200 and 5 * 200 == 1000 and 1000 * 2 // 5 == 400 and 1000 - 400 == 600 and 400 // 2 == 200
assert 48 // 4 == 12 and 3 * 12 == 36 and 12 + 36 == 48
assert 4 * 0 + 2 * 10 == 20 and 4 * 1 + 2 * 9 == 22 and 32 - 20 == 12 and 12 // 2 == 6 and 6 * 4 == 24 and 4 * 2 == 8 and 24 + 8 == 32
assert 600 * 2 // 5 == 240 and 600 + 240 == 840
assert 12 * 5 == 60 and 85 - 60 == 25 and 25 // 5 == 5 and 5 * 10 + 7 * 5 == 50 + 35 == 85 and 5 + 7 == 12


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças gerais ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    """uma frase, palavra a palavra, no mesmo estilo"""
    return [(w, est, size, cor) for w in txt.split()]


def fcen(c, t, t0, s, cx, y, size, cor=None):
    E.formula_em(c, t, t0, s, cx, y, size, "g", cor, "center")


def bola_txt(c, t, t0, s, cx, cy, r, size, cor=None):
    """o resultado na esfera"""
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r, cor, a), centro(c, s, cx, cy + size * 0.36, size, "g", M.on(cor or E.COR), a)))


# ---------------- linguagem da trilha Leitura de Problemas ----------------
_PEDACO = re.compile(r"\[([^|\]]+)\|(\w+)\]")


def _tokens(txt):
    """'Uma escola tem [8 turmas|tur].' -> [('Uma', None), ('escola', None), ('tem', None), ('8 turmas', 'tur'), ('.', None)]"""
    out, i = [], 0
    for m in _PEDACO.finditer(txt):
        out += [(w, None) for w in txt[i:m.start()].split()]
        out.append((m.group(1), m.group(2)))
        i = m.end()
    out += [(w, None) for w in txt[i:].split()]
    return out


def _layout(linha, x, size, pergunta):
    """x de cada pedaço da linha; pontuação cola no pedaço anterior"""
    pos, xx = [], x
    for j, (s, k) in enumerate(linha):
        est = "b" if (k or pergunta) else "i"
        sz = size * 0.9 if est == "b" else size
        if j and not s[0] in ".,:;?!":
            xx += size * 0.25
        w = E.larg(s, est, sz)
        pos.append((s, k, est, sz, xx, xx + w))
        xx += w
    return pos


def enunciado(c, t, x, y, w, linhas, size=60, dy=None, t_card=None, marca=None, risca=None, aponta=None):
    """o problema num cartão. linhas = [(t0, "texto com [número|chave]"[, True se for a pergunta])].
    marca / risca / aponta = {chave: instante}; a chave "q" marca a pergunta inteira. Devolve {chave: (x0, x1, base)}"""
    marca, risca, aponta = marca or {}, risca or {}, aponta or {}
    dy = dy or size * 1.62
    pad = size * 0.85
    h = pad * 2 + size * 1.05 + dy * (len(linhas) - 1)
    t_card = linhas[0][0] - 0.3 if t_card is None else t_card

    def cartao(a):
        r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 26, 26)
        s = skia.Paint(AntiAlias=True, Color=M.hexc("#000000", 0.10 * a))
        s.setMaskFilter(skia.MaskFilter.MakeBlur(skia.kNormal_BlurStyle, 18))
        c.save(); c.translate(6, 14); c.drawRRect(r, s); c.restore()
        c.drawRRect(r, M.paint(BR, a))
        c.save(); c.clipRRect(r, True)
        c.drawRect(skia.Rect.MakeXYWH(x, y, 14, h), M.paint(E.COR, a))
        c.restore()
    E.foco(c, t, t_card, 0.5, cartao, blur=8)
    onde = {}
    for i, ln in enumerate(linhas):
        t0, txt = ln[0], ln[1]
        pergunta = len(ln) > 2 and ln[2]
        base = y + pad + size * 0.78 + i * dy
        pos = _layout(_tokens(txt), x + pad + 14, size, pergunta)
        if pergunta:
            onde["q"] = (pos[0][4], pos[-1][5], base)
        for s, k, est, sz, x0, x1 in pos:
            if k:
                onde[k] = (x0, x1, base)
        if t < t0:
            continue
        # marca-texto atrás dos pedaços úteis
        for k, (x0, x1, b_) in list(onde.items()):
            if b_ != base or k not in marca or t < marca[k]:
                continue
            p = ease_io(prog(t, marca[k], 0.45))
            M.rrect(c, x0 - 12, base - size * 0.8, (x1 - x0 + 24) * p, size * 1.08, 12, E.COR, 0.16)

        def texto(a, pos=pos, pergunta=pergunta):
            for s, k, est, sz, x0, x1 in pos:
                kk = "q" if pergunta else k
                cor = TINTA
                if kk and kk in marca and t >= marca[kk]:
                    cor = COR
                if kk and kk in risca and t >= risca[kk] + 0.2:
                    cor = CINZA
                E.escreve(c, s, x0, base, sz, est, cor, a)
        E.foco(c, t, t0, 0.5, texto, sobe=10)
    for k, ta in aponta.items():
        if k in onde and t >= ta and (k not in risca or t < risca[k] + 0.4):
            x0, x1, b_ = onde[k]
            q = ep(t, ta, 0.35) * (1 - ep(t, risca.get(k, 1e9), 0.4))
            E.caixa_pontilhada(c, x0 - 14, b_ - size * 0.86, x1 - x0 + 28, size * 1.16, q, ERRADO, prog_=ep(t, ta, 0.35))
    for k, tr in risca.items():
        if k in onde and t >= tr:
            x0, x1, b_ = onde[k]
            E.risco(c, x0 - 10, b_ - size * 0.3, x1 + 10, b_ - size * 0.3, t, tr, ERRADO, 8)
    return onde


def pessoa(c, cx, base, h, cor=TINTA, a=1.0):
    """bonequinho de pé, com os pés em base"""
    if a <= 0:
        return
    c.drawCircle(cx, base - h * 0.84, h * 0.15, M.paint(cor, a))
    M.rrect(c, cx - h * 0.17, base - h * 0.64, h * 0.34, h * 0.64, h * 0.12, cor, a)


def lista(c, t, C, ini, itens, n_txt):
    """'você só precisa de N coisas' com as caixas pontilhadas"""
    E.frase(c, t, C[ini] + 0.5, ps("você só precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C[itens[0][0]] - 0.4, 0.5, lambda a: E.escreve(c, n_txt, XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C[itens[0][0]] - 0.25, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 960, 800
    y0, dy = (250, 280) if len(itens) == 2 else (170, 240)
    for i, (k, l1, l2) in enumerate(itens):
        y = y0 + i * dy
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 196, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 60)], x + 44, y + 84)
        E.frase(c, t, C[k] + 0.3, [(l2, "g", 60, COR)], x + 44, y + 160)
    py = y0 + 170
    for i, (k, _, _) in enumerate(itens[1:], 1):
        py = lerp(py, y0 + i * dy + 170, ease_io(prog(t, C[k] - 0.35, 0.5)))
    E.cursor(c, x + w - 30, py, ep(t, C[itens[0][0]], 0.4))




def tira(c, x, y, h, pecas, a=1.0, size=60):
    """tira de quantidade feita de peças [(largura, cor, rótulo[, tracejada])], encostadas da esquerda para a direita"""
    if a <= 0:
        return x
    for p in pecas:
        w, cor, s = p[0], p[1], p[2]
        tracejada = len(p) > 3 and p[3]
        if w <= 2:
            continue
        if tracejada:
            pt = M.paint(cor, a, stroke=4)
            pt.setPathEffect(skia.DashPathEffect.Make([12, 9], 0))
            c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x + 3, y + 3, w - 6, h - 6), 10, 10), pt)
            if s:
                centro(c, s, x + w / 2, y + h / 2 + size * 0.36, size, "g", cor, a)
        else:
            M.rrect(c, x + 2, y, w - 4, h, 10, cor, a)
            if s and w > size * 0.8:
                centro(c, s, x + w / 2, y + h / 2 + size * 0.36, size, "g", BR, a)
        x += w
    return x


def barra(c, x, y, w, h, n, cortes=(), pinta=(), a=1.0, rot=(), size=60):
    """total cortado em n casas iguais. cortes = [(posição em casas, p)], pinta = [(i0, i1, cor, p)],
    rot = [(i0, i1, texto, alfa)] escreve no meio do trecho (branco sobre a parte pintada)"""
    if a <= 0:
        return
    rr = E._casco(c, x, y, w, h, 14, a)
    cel = w / n
    c.save(); c.clipRRect(rr, True)
    pint = []
    for i0, i1, cor, p in pinta:
        if p > 0:
            c.drawRect(skia.Rect.MakeXYWH(x + cel * i0, y, cel * (i1 - i0) * M.clamp(p), h), M.paint(cor, a))
            if p > 0.95:
                pint.append((i0, i1))
    for pos, p in cortes:
        if p > 0:
            dentro = any(i0 < pos < i1 or pos in (i0, i1) for i0, i1 in pint)
            M.line(c, x + cel * pos, y, x + cel * pos, y + h * M.clamp(p), BR if dentro else TINTA2, a, 5)
    c.restore()
    c.drawRRect(rr, M.paint(TINTA, a, stroke=3))
    for i0, i1, s, q in rot:
        if q > 0:
            cheio = any(j0 <= i0 and i1 <= j1 for j0, j1 in pint)
            centro(c, s, x + cel * (i0 + i1) / 2, y + h / 2 + size * 0.36, size, "g", BR if cheio else TINTA, a * q)


def chave_rot(c, t, t0, x0, x1, y, rot, cor=TINTA2, cima=False, size=54, desce=0):
    """chave sob (ou sobre) um trecho, com o rótulo (aceita a escrita de E.formula)"""
    E.chave(c, x0 + 6, x1 - 6, y, cor, ep(t, t0, 0.5), -22 if cima else 22)
    E.foco(c, t, t0 + 0.2, 0.4, lambda a: E.formula(c, rot, (x0 + x1) / 2, y + (-40 if cima else 90 + desce), size, "g", cor, a, "center"))



def tabela(c, t, x, y, larg, cab, linhas, t_cab, h=96, size=60, escuro=False, verde=None, cor_cab=None):
    """tabela de palpites. cab = títulos; linhas = [(t0, [células])], célula = texto ou (texto, cor);
    verde = (índice da linha, instante): a linha da resposta acende. Devolve (x de cada coluna, y de cada linha)"""
    tinta = BR if escuro else TINTA
    total = sum(larg)
    xs, xx = [], x
    for w in larg:
        xs.append(xx + w / 2)
        xx += w

    def topo(a):
        M.rrect(c, x, y, total, h, 18, cor_cab or E.COR, a)
        for s, cx in zip(cab, xs):
            centro(c, s, cx, y + h / 2 + size * 0.3, size * 0.8, "b", BR, a)
    E.foco(c, t, t_cab, 0.5, topo)
    ys = []
    if verde is not None and t >= verde[1]:
        q = ep(t, verde[1], 0.4)
        yy = y + h * (verde[0] + 1)
        M.rrect(c, x - 6, yy + 4, total + 12, h - 8, 16, CERTO, 0.16 * q)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x - 6, yy + 4, total + 12, h - 8), 16, 16), M.paint(CERTO, q, stroke=4))
    for i, (t0, cel) in enumerate(linhas):
        yy = y + h * (i + 1)
        ys.append(yy + h / 2)

        def linha_(a, yy=yy, cel=cel):
            M.line(c, x, yy + h, x + total, yy + h, CINZA if escuro else FIO, a, 2)
            for s, cx in zip(cel, xs):
                cor = tinta
                if isinstance(s, tuple):
                    s, cor = s
                centro(c, s, cx, yy + h / 2 + size * 0.36, size, "g", cor, a)
        E.foco(c, t, t0, 0.45, linha_, sobe=8)
    return xs, ys


def blocos(c, x, y, n, w, h, cor, rot, a=1.0, size=64):
    """n blocos iguais lado a lado; rot = texto dentro de cada um"""
    tira(c, x, y, h, [(w, cor, rot)] * n, a, size)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    a1, b1, c1 = C["s01.a"], C["s01.b"], C["s01.c"]

    def cena():
        E.frase(c, t, a1 - 0.3, ps("gastou", "i", 92), 520, 230)
        E.foco(c, t, a1, 0.5, lambda a: E.fracao(c, 2, 5, 860, 190, 100, COR, a))
        E.frase(c, t, a1 + 0.4, ps("do salário", "i", 92), 960, 230, "left", 0.12)
        E.frase(c, t, b1 - 0.4, ps("e ficou com", "i", 92) + [("R$ 600", "g", 100, COR)], W / 2, 420, "center", 0.12)
        E.frase(c, t, lerp(b1, c1, 0.3), ps("qual é o", "i", 92) + [("salário?", "g", 100)], W / 2, 580, "center", 0.12)
        E.frase(c, t, lerp(b1, c1, 0.6), ps("precisa de", "i", 76, TINTA2) + [("equação?", "g", 80, ERRADO)], W / 2, 740, "center", 0.12)
        E.frase(c, t, c1 - 0.3, ps("basta", "i", 96) + [("um desenho", "g", 100, COR)], W / 2, 920, "center", 0.12)
        E.foco(c, t, c1 + 0.2, 0.5, lambda a: barra(c, 1400, 860, 360, 80, 5, [(k, 1) for k in range(1, 5)], [(0, 2, E.COR, 1)], a))
    E.saida(c, t, C["s02"] - 0.1, cena)
    if t >= C["s02"]:
        ta, tb = C["s02.a"], C["s02.b"]
        E.foco(c, t, tb - 0.2, 0.7, lambda a: E.bola(c, 1500, 540, 250 * ease_back(prog(t, tb - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, ps("até o fim desta aula", "i", 86), XE, 300, passo=0.12)
        E.frase(c, t, lerp(ta, tb, 0.25), ps("resolver", "i", 92) + [("desenhando", "g", 100, COR)], XE, 450, passo=0.12)
        E.frase(c, t, lerp(ta, tb, 0.5), [("barras", "g", 100, COR)] + ps("e", "i", 92) + [("tabelas", "g", 100, COR)], XE, 600, passo=0.12)
        E.foco(c, t, tb + 0.1, 0.5, lambda a: (centro(c, "+ atalho", 1500, 525, 80, "g", E.SOBRE, a),
                                               centro(c, "de prova", 1500, 610, 80, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    lista(c, t, C, "s03", (("s03.a", "leia", "a pergunta primeiro"), ("s03.b", "antes de cada fração,", "fração de quê?"),
                           ("s03.c", "troque a letra", "pelo número")), "3")
    E.frase(c, t, lerp(C["s03.c"], C["s03.end"], 0.55), ps("faltou alguma?", "i", 58, COR) + ps("procure no canal", "i", 58), 960, 1010, "left", 0.12)


# ---------------- barra: da parte para o total ----------------
SX, SW, SH, SY = 360, 1200, 150, 380


def barra_salario(c, t, ta, tc, tp, rot, a=1.0):
    """o salário em 5 partes: ta = barra, tc = cortes, tp = pintar 2 partes; rot = [(i0, i1, texto, alfa)]"""
    cortes = [(k, ep(t, tc + 0.08 * k, 0.4)) for k in range(1, 5)]
    E.foco(c, t, ta, 0.5, lambda q: barra(c, SX, SY, SW, SH, 5, cortes, [(0, 2, E.COR, ep(t, tp, 0.6))], a * q, rot, 64))


def b_barra1(c, t, C, b):
    a4, b4, c4, d4 = C["s04.a"], C["s04.b"], C["s04.c"], C["s04.d"]
    a5, b5 = C["s05.a"], C["s05.b"]
    a6, b6, c6 = C["s06.a"], C["s06.b"], C["s06.c"]
    cel = SW / 5
    xc = lambda i: SX + cel * i
    E.frase(c, t, C["s04"] + 0.2, ps("desenhe", "i", 80) + [("o salário", "g", 84, COR)] + ps("como uma barra", "i", 80), W / 2, 180, "center", 0.12)
    tv = lerp(b5, C["s05.end"], 0.55)  # "cada parte vale duzentos reais"
    rot = [(i, i + 1, "200", ep(t, tv + 0.12 * (i - 2), 0.4) if i >= 2 else ep(t, a6 + 0.12 * i, 0.4)) for i in range(5)]
    barra_salario(c, t, a4, b4, c4, rot)
    E.foco(c, t, b4 + 0.3, 0.4, lambda a: centro(c, "5 partes iguais", W / 2, SY - 40, 54, "i", TINTA2, a * (1 - ep(t, c4, 0.4))))
    chave_rot(c, t, c4 + 0.2, xc(0), xc(2), SY + SH + 20, "gastou", E.COR, size=56)

    def sobra():
        chave_rot(c, t, d4, xc(2), xc(5), SY + SH + 20, "sobram 3 partes", TINTA, size=56)
    E.saida(c, t, a5 - 0.2, sobra)
    chave_rot(c, t, a5, xc(2), xc(5), SY + SH + 20, "sobrou R$ 600", CERTO, size=56)
    E.saida(c, t, b6 - 0.2, lambda: fcen(c, t, b5, "600 ÷ 3 = 200", W / 2, 820, 100))
    E.saida(c, t, a6 - 0.2, lambda: E.frase(c, t, tv, ps("cada parte vale", "i", 70) + [("R$ 200", "g", 76, COR)], W / 2, 950, "center", 0.1))
    # o salário inteiro e a conferência
    if t >= a6 - 0.2:
        chave_rot(c, t, a6, xc(0), xc(5), SY - 20, "salário: 5 × 200 = R$ 1.000", COR, cima=True, size=58)
        E.foco(c, t, b6, 0.5, lambda a: E.formula(c, "f{2}{5} de 1.000 = 400", W / 2, 830, 90, "g", TINTA, a, "center"))
        E.foco(c, t, c6, 0.5, lambda a: E.formula(c, "1.000 − 400 = 600", W / 2, 960, 90, "g", CERTO, a, "center"))
        E.foco(c, t, lerp(c6, C["s06.end"], 0.6), 0.5, lambda a: E.selo(c, W / 2 + 470, 930, 46, True, a))


# ---------------- barra: comparar ----------------
BLX, BLW, BLH = 520, 250, 120


def b_barra2(c, t, C, b):
    a7, b7 = C["s07.a"], C["s07.b"]
    a8, b8, c8, d8, e8, f8 = (C[f"s08.{k}"] for k in "abcdef")
    a9, b9, c9 = C["s09.a"], C["s09.b"], C["s09.c"]
    tb = lerp(a9, b9, 0.7)  # "No salário, se o texto desse a parte gasta"

    def pedro():
        E.frase(c, t, C["s07"] + 0.2, ps("a barra também", "i", 70, TINTA2) + [("compara", "g", 72, TINTA2)], XE, 140, "left", 0.1)
        E.linha(c, t, [("Pedro:", "i", 76, TINTA, a7), ("o triplo", "g", 80, COR, a7 + 0.4), ("da idade do filho", "i", 76, TINTA, a7 + 0.8)], XE, 250)
        E.linha(c, t, [("somadas:", "i", 76, TINTA, b7), ("48 anos", "g", 80, COR, b7 + 0.3)], XE + 1150, 250)
        y1, y2 = 400, 580
        E.foco(c, t, a8, 0.4, lambda a: E.escreve(c, "filho", XE, y1 + 82, 64, "i", TINTA, a))
        E.foco(c, t, a8, 0.5, lambda a: blocos(c, BLX, y1, 1, BLW, BLH, E.COR, "12" if t >= e8 else "?", a, 70))
        E.foco(c, t, b8 - 0.2, 0.4, lambda a: E.escreve(c, "Pedro", XE, y2 + 82, 64, "i", TINTA, a))
        for k in range(3):
            E.foco(c, t, b8 + 0.15 * k, 0.5, lambda a, k=k: blocos(c, BLX + k * BLW, y2, 1, BLW, BLH, TINTA, "12" if t >= f8 else "?", a, 70))
        if t >= c8:
            q = ep(t, c8, 0.4)
            E.caixa_pontilhada(c, BLX - 20, y1 - 20, 3 * BLW + 40, y2 + BLH - y1 + 40, q, prog_=q)
            E.foco(c, t, c8 + 0.3, 0.4, lambda a: (centro(c, "4 blocos", 1520, 520, 72, "i", TINTA, a), centro(c, "= 48", 1520, 620, 96, "g", COR, a)))
        fcen(c, t, d8, "48 ÷ 4 = 12", W / 2, 860, 100)
        E.linha(c, t, [("filho:", "i", 72, TINTA, e8), ("12 anos", "g", 76, COR, e8 + 0.3), ("·", "g", 72, CINZA, f8), ("Pedro:", "i", 72, TINTA, f8),
                       ("3 × 12 = 36 anos", "g", 76, COR, f8 + 0.3)], W / 2, 990, "center")
    E.saida(c, t, C["s09"] - 0.1, pedro)
    if t < C["s09"] - 0.1:
        return

    def ideia():
        E.frase(c, t, C["s09"] + 0.2, ps("ninguém montou", "i", 90) + [("equação", "g", 96, COR)], W / 2, 260, "center", 0.12)
        E.frase(c, t, a9, ps("o desenho mostra", "i", 80) + [("quantas partes iguais", "g", 84, COR)], W / 2, 480, "center", 0.12)
        E.frase(c, t, lerp(a9, b9, 0.35), ps("e a conta vira uma", "i", 80) + [("divisão", "g", 84, COR)], W / 2, 640, "center", 0.12)
    E.saida(c, t, tb - 0.2, ideia)
    if t < tb - 0.2:
        return
    cel = SW / 5
    xc = lambda i: SX + cel * i
    E.frase(c, t, tb, ps("e se o texto desse", "i", 76) + [("a parte gasta?", "g", 80, COR)], W / 2, 200, "center", 0.12)
    barra_salario(c, t, tb, tb + 0.2, tb + 0.4, [(i, i + 1, "200", ep(t, lerp(b9, c9, 0.5) + 0.1 * i, 0.4)) for i in range(5)])
    chave_rot(c, t, b9, xc(0), xc(2), SY + SH + 20, "2 partes = R$ 400", E.COR, size=56)
    fcen(c, t, lerp(b9, c9, 0.5), "400 ÷ 2 = 200", W / 2, 820, 96)
    E.foco(c, t, c9, 0.5, lambda a: E.formula(c, "salário: 5 × 200 = R$ 1.000", W / 2, 960, 84, "g", CERTO, a, "center"))


# ---------------- tabela de casos ----------------
TBX, TBY = 170, 320
TBL = (270, 270, 270)


def b_tabela(c, t, C, b):
    a0, b0, c0 = C["s10.a"], C["s10.b"], C["s10.c"]
    a1, b1, c1, d1 = C["s11.a"], C["s11.b"], C["s11.c"], C["s11.d"]
    a2, b2, c2 = C["s12.a"], C["s12.b"], C["s12.c"]
    a3, b3, c3, d3 = C["s13.a"], C["s13.b"], C["s13.c"], C["s13.d"]
    E.linha(c, t, [("poucas opções?", "i", 80, TINTA, C["s10"] + 0.2), ("a tabela", "g", 90, COR, a0)], XE, 170)
    E.linha(c, t, [("10 veículos", "g", 64, TINTA, b0), ("·", "g", 64, CINZA, c0), ("32 rodas", "g", 64, TINTA, c0),
                   ("·", "g", 64, CINZA, lerp(c0, C["s10.end"], 0.5)), ("quantos carros?", "i", 68, COR, lerp(c0, C["s10.end"], 0.5))], XE, 260)
    linhas = [(c1, ["0", "10", "20"]), (d1, ["1", "9", "22"]), (lerp(c2, C["s12.end"], 0.35), [("...", CINZA), ("...", CINZA), ("...", CINZA)]),
              (c2 + 0.4, [("6", CERTO), ("4", CERTO), ("32", CERTO)])]
    xs, ys = tabela(c, t, TBX, TBY + 40, TBL, ("carros", "motos", "rodas"), linhas, a1, h=104, size=66, verde=(3, a3))
    E.frase(c, t, lerp(a1, b1, 0.5), ps("cada linha é um", "i", 58, TINTA2) + [("palpite", "g", 60, TINTA2)], TBX, TBY + 40 + 104 * 5 + 80, "left", 0.1)
    xr = 1500

    def regra():
        fcen(c, t, b1, "rodas = 4 × carros", xr, 380, 66)
        fcen(c, t, b1 + 0.5, "+ 2 × motos", xr, 470, 66)
    E.saida(c, t, a2 - 0.2, regra)
    # o padrão: +2 a cada troca
    if t >= a2:
        x3 = TBX + sum(TBL) + 30
        p = ep(t, a2, 0.6)
        M.arrow(c, x3, ys[0], x3, ys[1], COR, p, 6, 20, p)
        E.foco(c, t, a2 + 0.3, 0.4, lambda a: E.pilula(c, "+2", x3 + 58, (ys[0] + ys[1]) / 2, 50, "g", a=a, cor=E.SOBRE))

    def conta():
        E.frase(c, t, a2, ps("cada carro no lugar de uma moto:", "i", 54), xr, 380, "center", 0.08)
        E.frase(c, t, a2 + 0.5, [("+ 2 rodas", "g", 70, COR)], xr, 470, "center")
        fcen(c, t, b2, "32 − 20 = 12", xr, 610, 80)
        fcen(c, t, c2, "12 ÷ 2 = 6", xr, 730, 80, CERTO)
        E.frase(c, t, c2 + 0.4, [("6 carros", "g", 66, CERTO)], xr, 820, "center")
        E.frase(c, t, lerp(c2, C["s12.end"], 0.35), ps("pulou 4 linhas, sem equação", "i", 54, TINTA2), xr, 920, "center", 0.08)
    E.saida(c, t, a3 - 0.2, conta)
    if t >= a3 - 0.2:
        E.frase(c, t, a3, ps("confira na linha", "i", 66), xr, 380, "center", 0.1)
        fcen(c, t, b3, "6 × 4 = 24", xr, 520, 80)
        fcen(c, t, c3, "4 × 2 = 8", xr, 640, 80)
        fcen(c, t, d3, "24 + 8 = 32", xr, 780, 90, CERTO)
        E.foco(c, t, d3 + 0.8, 0.5, lambda a: E.selo(c, xr, 890, 46, True, a))


# ---------------- erro comum ----------------
def b_erro(c, t, C, b):
    a4, b4 = C["s14.a"], C["s14.b"]
    a5, b5 = C["s15.a"], C["s15.b"]

    def errado():
        E.frase(c, t, C["s14"] + 0.2, ps("o erro comum", "i", 80, ERRADO), W / 2, 200, "center", 0.12)
        fcen(c, t, a4, "f{2}{5} de 600 = 240", W / 2, 420, 110)
        fcen(c, t, b4, "600 + 240 = 840", W / 2, 640, 120, ERRADO)
        E.foco(c, t, b4 + 0.8, 0.5, lambda a: E.selo(c, W / 2 + 580, 600, 56, False, a))
    E.saida(c, t, C["s15"] - 0.1, errado)
    if t < C["s15"] - 0.1:
        return
    cel = SW / 5
    xc = lambda i: SX + cel * i
    E.frase(c, t, C["s15"] + 0.2, [("600", "g", 84, ERRADO)] + ps("não é o salário", "i", 80), W / 2, 170, "center", 0.12)
    E.frase(c, t, a5, ps("é", "i", 80) + [("a parte que sobrou", "g", 84, COR)], W / 2, 290, "center", 0.12)
    barra_salario(c, t, a5 + 0.3, a5 + 0.4, a5 + 0.5, [])
    chave_rot(c, t, lerp(a5, b5, 0.4), xc(0), xc(5), SY + SH + 140, "f{2}{5} são do salário inteiro", TINTA2, size=54)
    if t >= b5:
        q = ep(t, b5, 0.4)
        E.caixa_pontilhada(c, xc(2) - 8, SY - 14, cel * 3 + 16, SH + 28, q, CERTO, prog_=q)
        chave_rot(c, t, b5, xc(2), xc(5), SY + SH + 20, "R$ 600", CERTO, size=60)
    E.frase(c, t, b5 + 0.4, [("600", "g", 80, CERTO)] + ps("ocupa", "i", 76) + [("3 partes,", "g", 80, CERTO)] + ps("não 5", "i", 76), W / 2, 960, "center", 0.12)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    a6, b6, c6, d6 = C["s16.a"], C["s16.b"], C["s16.c"], C["s16.d"]
    a7, b7 = C["s17.a"], C["s17.b"]

    def um():
        E.frase(c, t, C["s16"] + 0.2, ps("agora, o atalho da tabela", "i", 70, CLARO), W / 2, 140, "center", 0.1)
        E.frase(c, t, a6, ps("não preencha", "i", 84, CLARO) + [("linha por linha", "g", 88, BR)], W / 2, 260, "center", 0.12)
        linhas = [(b6, ["0", "10", "20"]), (c6 + 0.2, ["1", "9", "22"]), (d6 - 0.1, [("...", CINZA), ("...", CINZA), ("...", CINZA)]),
                  (d6 + 0.3, [("6", BR), ("4", BR), ("32", BR)])]
        xs, ys = tabela(c, t, 360, 340, (250, 250, 250), ("carros", "motos", "rodas"), linhas, b6 - 0.3, escuro=True, verde=(3, d6 + 0.5))
        x3 = xs[2] + 150
        E.foco(c, t, b6, 0.4, lambda a: E.pilula(c, "1ª linha", 230, ys[0], 40, "g", fundo=BR, cor=TINTA, a=a))
        if t >= c6:
            p = ep(t, c6, 0.5)
            M.arrow(c, x3, ys[0], x3, ys[1], CLARO, p, 6, 20, p)
            E.foco(c, t, c6 + 0.3, 0.4, lambda a: E.pilula(c, "+2 por troca", x3 + 160, (ys[0] + ys[1]) / 2, 46, "g", fundo=BR, cor=TINTA, a=a))
        if t >= d6:
            p = ep(t, d6, 0.6)
            M.arrow(c, xs[0] - 200, ys[0], xs[0] - 200, ys[3], CLARO, p, 6, 20, p)
            E.foco(c, t, d6 + 0.4, 0.4, lambda a: E.pilula(c, "pule!", 230, ys[3], 40, "g", fundo=BR, cor=TINTA, a=a))
    E.saida(c, t, C["s17"] - 0.1, um)
    if t < C["s17"]:
        return
    E.frase(c, t, a7 - 0.4, ps("cada troca muda", "i", 84, CLARO) + [("sempre o mesmo tanto", "g", 88, BR)], W / 2, 260, "center", 0.12)
    tn = lerp(a7, b7, 0.3)
    E.foco(c, t, tn, 0.5, lambda a: E.selo(c, 330, 470, 56, False, a))
    E.frase(c, t, tn, ps("não compensa: a mudança", "i", 76, CLARO) + [("não é igual", "g", 80, BR)], 430, 495, "left", 0.1)
    E.frase(c, t, lerp(a7, b7, 0.55), ps("preço que fica mais barato a partir de certa quantidade", "i", 56, CLARO), 430, 600, "left", 0.06)
    E.frase(c, t, b7, ps("aí,", "i", 90, CLARO) + [("preencha com calma", "g", 96, BR)], W / 2, 850, "center", 0.12)


# ---------------- questão ----------------
def linhas_q(C):
    a, b_, c_ = C["s18.a"], C["s18.b"], C["s18.c"]
    return [(a - 0.4, "Um caixa tem [12 notas|n],"), (lerp(a, b_, 0.45), "umas de [R$ 5|c] e outras de [R$ 10|d]."),
            (b_, "O total é [R$ 85|t]."), (c_, "Quantas notas de R$ 10 há no caixa?", True)]


def b_questao(c, t, C, b):
    E.frase(c, t, C["s18"] + 0.2, ps("hora de testar", "i", 64, COR), XE, 150, passo=0.12)
    enunciado(c, t, XE, 210, 1180, linhas_q(C), size=64)
    E.relogio(c, t, C["s19.a"], 1580, 440, 170)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    a0, b0, c0 = C["s20.a"], C["s20.b"], C["s20.c"]
    a1, b1, c1, d1 = C["s21.a"], C["s21.b"], C["s21.c"], C["s21.d"]
    E.frase(c, t, C["s20"] + 0.2, ps("pela", "i", 76) + [("tabela", "g", 80, COR)], XE, 190, "left", 0.12)
    linhas = [(a0, ["0", "12", "R$ 60"]), (lerp(b1 - 0.3, b1, 0.3), [("...", CINZA), ("...", CINZA), ("...", CINZA)]),
              (b1, [("5", CERTO), ("7", CERTO), ("R$ 85", CERTO)])]
    xs, ys = tabela(c, t, TBX, TBY, (270, 270, 290), ("de R$ 10", "de R$ 5", "total"), linhas, C["s20"] + 0.4, h=104, size=66, verde=(2, c1))
    xr = 1450

    def conta():
        E.frase(c, t, b0, ps("cada nota de 5 trocada por uma de 10:", "i", 54), xr, 380, "center", 0.07)
        E.frase(c, t, b0 + 0.6, [("+ R$ 5", "g", 72, COR)], xr, 470, "center")
        fcen(c, t, c0, "85 − 60 = 25", xr, 620, 84)
        fcen(c, t, a1, "25 ÷ 5 = 5", xr, 750, 84, CERTO)
        E.frase(c, t, a1 + 0.5, [("5 trocas", "g", 66, CERTO)], xr, 840, "center")
    E.saida(c, t, d1 - 0.3, conta)
    if t >= d1 - 0.3:
        E.frase(c, t, d1 - 0.2, ps("confira", "i", 70), xr, 420, "center")
        fcen(c, t, d1, "5 × 10 = 50", xr, 540, 80)
        fcen(c, t, d1 + 0.5, "7 × 5 = 35", xr, 650, 80)
        fcen(c, t, lerp(d1, C["s21.end"], 0.4), "50 + 35 = 85", xr, 790, 90, CERTO)
        E.foco(c, t, lerp(d1, C["s21.end"], 0.75), 0.5, lambda a: E.selo(c, xr, 900, 46, True, a))
    bola_txt(c, t, b1 + 0.4, "5", 360, 900, 80, 100, CERTO)
    E.frase(c, t, b1 + 0.6, [("notas de R$ 10", "g", 64, CERTO)], 470, 925)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s22"] + 0.1, [("resumindo", "i", 92, COR)], W / 2, 200, "center")
        itens = (("s22.a", "fração", "vira barra de partes iguais"), ("s22.b", "opções", "viram tabela"), ("s22.c", "a última linha", "sempre é conferida"))
        for i, (k, l1, l2) in enumerate(itens):
            y = 380 + i * 200
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 230, y - 30, 56, a=a), centro(c, str(i + 1), 230, y - 7, 64, "g", E.SOBRE, a)))
            E.frase(c, t, C[k] + 0.1, [(l1, "g", 76, COR)] + ps(l2, "i", 74), 320, y, "left", 0.1)
    E.saida(c, t, C["s23"] - 0.1, resumo)
    if t < C["s23"]:
        return
    a3, b3, c3, d3 = (C[f"s23.{k}"] for k in "abcd")
    E.frase(c, t, C["s23"] + 0.2, ps("na próxima aula", "i", 84), XE, 240, passo=0.14)
    E.frase(c, t, a3, [("estimar", "g", 100, COR)] + ps("contas e quantidades", "i", 90), XE, 390, passo=0.12)
    E.frase(c, t, b3, ps("quantas vezes seu", "i", 70) + [("coração", "g", 72, COR)] + ps("já bateu?", "i", 70), XE, 520, passo=0.1)
    E.foco(c, t, c3, 0.5, lambda a: E.pilula(c, "Inscreva-se", 1440, 750, 76, estilo="g", a=a, cor=E.SOBRE))
    p = ease_io(prog(t, c3 + 0.3, 0.8))
    E.cursor(c, lerp(1770, 1570, p), lerp(990, 775, p), ep(t, c3 + 0.2, 0.4))
    E.frase(c, t, d3, [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 930, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, barra1=b_barra1, barra2=b_barra2, tabela=b_tabela, erro=b_erro, atalho=b_atalho,
              questao=b_questao, resposta=b_resposta, fim=b_fim)
