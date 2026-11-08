"""Visual — Estudativo · MAT-LEI-002: palavras que mudam a conta.

Linguagem da trilha Leitura de Problemas (as peças abaixo de "linguagem da trilha" servem a todas as aulas MAT-LEI):
- enunciado(): o problema num cartão branco com fio da cor da matéria. Os números são escritos em grotesca; a pergunta fica numa
  linha própria. marca = marca-texto da cor da matéria (dado útil), aponta = caixa pontilhada (dado em dúvida),
  risca = traço vermelho e número cinza (dado que não entra na conta).
- pessoa(): ícone simples para a quantidade que só existe inteira.
- tira(): a quantidade como tira (x, x + 3, x − 3, 3x); barra(): o total cortado em casas, para "fração de quê?".
Todo instante vem de C[...] (marcadores do roteiro) ou de pal() (a palavra na voz real)."""
import json
from pathlib import Path
import re
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Leitura de Problemas")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-LEI-002_palavras_que_mudam_a_conta.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("restante", "minimo", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
# as contas da aula, conferidas
assert 10 + 3 == 13 and 3 * 10 == 30 and 10 - 3 == 7
assert 60 // 3 == 20 and 60 - 20 == 40 and 40 // 4 == 10 and 40 - 10 == 30 and 60 // 4 == 15
assert 30 / 8 == 3.75 and 3 * 8 == 24 and 30 - 24 == 6 and 4 * 8 == 32 and 32 // 8 == 4
assert 8 * 12 == 96 <= 100 < 9 * 12 == 108
assert 90 // 3 == 30 and 90 - 30 == 60 and 60 // 4 == 15 and 60 - 15 == 45 and 2 * 20 == 40 <= 45 < 3 * 20 == 60
assert 90 / 4 == 22.5 and 60 - 22.5 == 37.5 and 20 <= 37.5 < 40


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- instante de uma palavra na voz ----------------
_T = json.loads((Path(__file__).resolve().parents[1] / "audio" / "tempos.json").read_text(encoding="utf-8"))
_TOK = {s["id"]: (s["start"], s["tokens"]) for s in _T["scenes"]}


def pal(sid, palavra, n=1):
    """instante em que a n-ésima ocorrência de `palavra` começa na cena sid"""
    st, toks = _TOK[sid]
    k = 0
    for tk in toks:
        if tk["disp"].lower().strip(".,:;!?") == palavra:
            k += 1
            if k == n:
                return st + tk["t0"]
    raise KeyError((sid, palavra, n))


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


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    a1, b1, c1 = C["s01.a"], C["s01.b"], C["s01.c"]

    def cena():
        E.linha(c, t, [("Maria tem", "i", 96, TINTA, C["s01"]), ("x", "g", 110, COR, a1), ("reais", "i", 96, TINTA, a1 + 0.3)], W / 2, 230, "center")
        E.linha(c, t, [("João tem", "i", 96, TINTA, pal("s01", "joão")), ("3 reais", "g", 104, TINTA, b1), ("a mais que", "g", 104, COR, pal("s01", "a")),
                       ("Maria", "i", 96, TINTA, pal("s01", "maria", 2))], W / 2, 400, "center")
        xs = E.linha(c, t, [("João =", "g", 150, TINTA, c1 - 0.3), ("3x", "g", 150, ERRADO, c1)], W / 2, 650, "center")
        tt = pal("s01", "trocou")
        if t >= tt:
            E.risco(c, xs[1] - 20, 650, xs[1] + E.larg("3x", "g", 150) + 20, 530, t, tt, ERRADO, 14)
        E.linha(c, t, [("trocou uma", "i", 80, TINTA, tt), ("soma", "g", 84, CERTO, pal("s01", "soma")),
                       ("por uma", "i", 80, TINTA, pal("s01", "por")), ("multiplicação", "g", 84, ERRADO, pal("s01", "multiplicação"))], W / 2, 880, "center")
    E.saida(c, t, C["s02"] - 0.1, cena)
    if t >= C["s02"]:
        ta, tb = C["s02.a"], C["s02.b"]
        E.foco(c, t, tb - 0.2, 0.7, lambda a: E.bola(c, 1500, 540, 250 * ease_back(prog(t, tb - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, ps("até o fim desta aula", "i", 86), XE, 330, passo=0.12)
        E.frase(c, t, pal("s02", "traduz"), [("3 expressões", "g", 100, COR)], XE, 490, passo=0.12)
        E.frase(c, t, pal("s02", "mudam"), ps("que mudam", "i", 92) + [("a conta", "g", 96, COR)], XE, 630, passo=0.12)
        E.foco(c, t, tb + 0.1, 0.5, lambda a: (centro(c, "+ atalho", 1500, 525, 80, "g", E.SOBRE, a),
                                               centro(c, "de prova", 1500, 610, 80, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    lista(c, t, C, "s03", (("s03.a", "a letra guarda", "o lugar de um número"), ("s03.b", "antes de cada fração,", "fração de quê?"),
                           ("s03.c", "leia", "a pergunta primeiro")), "3")
    E.frase(c, t, pal("s03", "se"), ps("faltou alguma?", "i", 58, COR) + ps("procure no canal", "i", 58), 960, 1010, "left", 0.12)


# ---------------- a mais que ----------------
UX, U3 = 460, 120  # largura de x e de 3 na tira
TX = 430


def b_amais(c, t, C, b):
    a4, b4, c4 = C["s04.a"], C["s04.b"], C["s04.c"]
    a5, b5, c5 = C["s05.a"], C["s05.b"], C["s05.c"]
    a6, b6, c6 = C["s06.a"], C["s06.b"], C["s06.c"]
    t_menos, t_vezes = pal("s05", "com"), C["s06"] + 0.3

    def topo():
        E.frase(c, t, a4, [("a mais que", "g", 110, COR)], XE, 190)
        E.frase(c, t, pal("s04", "compara"), ps("compara duas quantidades", "i", 62, TINTA2), XE + 640, 185, "left", 0.1)
    E.saida(c, t, t_menos - 0.2, topo)
    E.saida(c, t, t_vezes - 0.2, lambda: E.frase(c, t, t_menos, [("a menos que", "g", 110, COR)], XE, 190))
    E.frase(c, t, t_vezes, [("3 vezes", "g", 110, COR)] + ps("o que Maria tem", "i", 92), XE, 190, "left", 0.12)

    # a frase, com a base marcada
    def frase_base():
        xs = E.linha(c, t, [("João tem 3 reais a mais que", "i", 70, TINTA, pal("s04", "a", 2)), ("Maria", "g", 72, COR, pal("s04", "a", 2) + 0.3)], XE, 330)
        q = ep(t, b4, 0.4)
        E.caixa_pontilhada(c, xs[1] - 16, 268, E.larg("Maria", "g", 72) + 32, 86, q, prog_=q)
        E.foco(c, t, b4 + 0.2, 0.4, lambda a: E.pilula(c, "a base", xs[1] + E.larg("Maria", "g", 72) + 150, 305, 44, "g", a=a, cor=E.SOBRE))
    E.saida(c, t, t_menos - 0.2, frase_base)

    # as tiras: Maria e João
    E.foco(c, t, pal("s04", "maria") - 0.2, 0.5, lambda a: (E.escreve(c, "Maria", XE, 520, 64, "i", TINTA, a), tira(c, TX, 455, 100, [(UX, E.COR, "x")], a)))
    q_mais = ease_io(prog(t, c4, 0.6))
    q_menos = ease_io(prog(t, t_menos + 0.5, 0.9))
    q_vez = ease_io(prog(t, t_vezes + 0.4, 1.0))
    if t < t_vezes:
        extra = U3 * q_mais * (1 - q_menos)
        falta = U3 * q_menos
        pecas = [(UX - falta, TINTA, "x"), (extra, CERTO, "3")]
        if falta > 4:
            pecas.append((falta, ERRADO, "3" if q_menos > 0.6 else "", True))
    else:
        pecas = [(UX * M.clamp(1 + 2 * q_vez - j), TINTA, "x") for j in range(3)]
    E.foco(c, t, pal("s04", "joão"), 0.5, lambda a: (E.escreve(c, "João", XE, 670, 64, "i", TINTA, a), tira(c, TX, 605, 100, pecas, a)))

    # as fórmulas embaixo, uma de cada vez
    estados = [(a5, "João: x + 3"), (pal("s05", "dez"), "Maria: 10  →  João: 13"), (pal("s05", "três", 2), "3 a menos que Maria: x − 3"),
               (a6, "3 vezes o que Maria tem: 3x")]
    for i, (t0, s) in enumerate(estados):
        t1 = estados[i + 1][0] if i + 1 < len(estados) else b6 - 0.2
        E.saida(c, t, t1 - 0.15, lambda t0=t0, s=s: fcen(c, t, t0, s, W / 2, 880, 90), d=0.3)
    for x, t0, l1, l2 in ((620, b6, "a mais", "soma +"), (1300, c6, "vezes", "multiplica ×")):
        E.foco(c, t, t0, 0.5, lambda a, x=x, l1=l1, l2=l2: (E.pilula(c, l1, x, 860, 64, "g", a=a, cor=E.SOBRE),
                                                              centro(c, l2, x, 990, 76, "g", COR, a)))


# ---------------- do restante ----------------
BX, BW, BH = 420, 1300, 130


def b_restante(c, t, C, b):
    a7, b7, c7, d7, e7 = (C[f"s07.{k}"] for k in "abcde")
    a8, b8, c8, d8 = (C[f"s08.{k}"] for k in "abcd")
    a9, b9, c9 = C["s09.a"], C["s09.b"], C["s09.c"]
    cel = BW / 12
    xc = lambda i: BX + cel * i
    E.frase(c, t, a7, [("do restante", "g", 100, COR)] + ps("ou do que sobrou", "i", 84), W / 2, 160, "center", 0.12)
    E.frase(c, t, b7, ps("muda", "i", 60, TINTA2) + [("o total da fração", "g", 60, TINTA2)], W / 2, 250, "center", 0.1)
    y1 = 400
    E.foco(c, t, c7, 0.4, lambda a: E.escreve(c, "60 balas", BX, y1 - 30, 56, "g", TINTA, a))
    cortes = [(4, ep(t, d7, 0.5)), (8, ep(t, d7 + 0.1, 0.5)), (6, ep(t, c8, 0.5)), (10, ep(t, c8 + 0.1, 0.5))]
    pinta = [(0, 4, E.COR, ep(t, a8, 0.6)), (4, 6, TINTA, ep(t, c8 + 0.4, 0.6))]
    rot = [(0, 4, "20", ep(t, a8 + 0.4, 0.4)), (4, 6, "10", ep(t, pal("s08", "dez"), 0.4)), (6, 12, "30", ep(t, d8, 0.4))]
    E.foco(c, t, c7, 0.5, lambda a: barra(c, BX, y1, BW, BH, 12, cortes, pinta, a, rot))
    if t >= d8:
        q = ep(t, d8, 0.4)
        E.caixa_pontilhada(c, xc(6) + 4, y1 - 10, cel * 6 - 8, BH + 20, q, CERTO, prog_=q)

    def chaves():
        chave_rot(c, t, b8 - 0.4, xc(4), xc(12), y1 - 18, "restante: 40", COR, cima=True, size=52)
        chave_rot(c, t, a8, xc(0), xc(4), y1 + BH + 20, "Ana: f{1}{3} de 60", E.COR, size=52)
        chave_rot(c, t, pal("s08", "dez") - 0.6, xc(4), xc(6), y1 + BH + 20, "Bia: f{1}{4} de 40", TINTA, size=52, desce=95)
        E.foco(c, t, d8 + 0.2, 0.4, lambda a: centro(c, "sobram 30", xc(9) + 80, y1 + BH + 110, 54, "g", CERTO, a))
    E.saida(c, t, C["s09"] + 0.2, chaves)
    # "fração de quê?" na fala
    te = pal("s08", "e")
    E.saida(c, t, te - 0.2, lambda: E.frase(c, t, e7, ps("e um quarto", "i", 66) + [("do restante", "g", 66, COR)] + ps("para a Bia", "i", 66),
                                            W / 2, 960, "center", 0.1))
    E.saida(c, t, C["s09"] - 0.2, lambda: E.frase(c, t, te, ps("um quarto de quê?", "i", 72) + [("do restante", "g", 72, COR)], W / 2, 960, "center", 0.12))
    # sem a palavra restante
    if t >= C["s09"]:
        y2 = 680
        E.frase(c, t, a9, ps("sem a palavra:", "i", 56, TINTA2) + [("um quarto das balas", "g", 56)], BX, y2 - 30, "left", 0.1)
        cort2 = [(3, ep(t, a9 + 0.6, 0.5)), (6, ep(t, a9 + 0.7, 0.5)), (9, ep(t, a9 + 0.8, 0.5))]
        E.foco(c, t, a9, 0.5, lambda a: barra(c, BX, y2, BW, BH, 12, cort2, [(0, 3, ERRADO, ep(t, b9 - 0.3, 0.5))], a, [(0, 3, "15", ep(t, b9, 0.4))]))
        E.frase(c, t, c9, [("Bia:", "i", 72), ("15", "g", 80, ERRADO)] + ps("em vez de", "i", 72) + [("10", "g", 80, CERTO)], W / 2, 920, "center", 0.12)
        E.foco(c, t, pal("s09", "fração", 2) - 0.3, 0.5, lambda a: E.pilula(c, "fração de quê?", W / 2, 1010, 54, "g", a=a, cor=E.SOBRE))


# ---------------- no mínimo / no máximo ----------------
def cabine(c, x, y, w, h, a=1.0):
    if a <= 0:
        return
    M.rrect(c, x, y, w, h, 16, BR, a, shadow=True)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 16, 16), M.paint(TINTA, a, stroke=4))
    M.line(c, x + w / 2, y + 10, x + w / 2, y + h - 10, FIO, a, 3)


def b_minimo(c, t, C, b):
    a0, b0, c0, d0 = C["s10.a"], C["s10.b"], C["s10.c"], C["s10.d"]
    a1, b1, c1, d1, e1, f1 = (C[f"s11.{k}"] for k in "abcdef")
    a2, b2, c2, d2, e2 = (C[f"s12.{k}"] for k in "abcde")
    if t < C["s12"] - 0.1:
        def elevador():
            E.linha(c, t, [("no mínimo,", "g", 96, COR, a0), ("quantas viagens?", "i", 92, TINTA, d0 + 0.4)], XE, 170)
            E.linha(c, t, [("8", "g", 72, TINTA, b0 + 0.1), ("por viagem", "i", 66, TINTA, b0 + 0.4), ("·", "g", 66, CINZA, c0),
                           ("30", "g", 72, TINTA, c0), ("pessoas", "i", 66, TINTA, c0 + 0.3)], XE, 270)
            x0, y0, w, h, g = 170, 340, 230, 330, 262
            entra = ease_io(prog(t, c1, 0.7))
            for i in range(4):
                ti = (b0 if i == 0 else b1 - 0.3 + 0.15 * i) if i < 3 else c1 - 0.3
                E.foco(c, t, ti, 0.4, lambda a, i=i: cabine(c, x0 + i * g, y0, w, h, a))
                for k in range(8 if i < 3 else 0):
                    px, py = x0 + i * g + 65 + (k % 2) * 100, y0 + 96 + (k // 2) * 74
                    E.foco(c, t, ti + 0.2 + 0.03 * k, 0.3, lambda a, px=px, py=py: pessoa(c, px, py, 54, E.COR, a), blur=4)
            # as 30 pessoas na fila: 24 entram nas 3 viagens, 6 esperam e sobem na 4ª
            for k in range(30):
                fx0, fy0 = x0 + 20 + k * 34, y0 + h + 150
                if k < 24:
                    E.saida(c, t, b1 + 0.1 * (k // 8), lambda fx0=fx0, fy0=fy0: E.foco(c, t, c0 + 0.02 * k, 0.3, lambda a: pessoa(c, fx0, fy0, 54, CINZA, a), blur=4))
                else:
                    j = k - 24
                    px, py = x0 + 3 * g + 65 + (j % 2) * 100, y0 + 96 + (j // 2) * 74
                    fx, fy = lerp(fx0, px, entra), lerp(fy0, py, entra)
                    cor = CINZA if t < pal("s11", "seis") else ERRADO if entra < 0.5 else CERTO
                    E.foco(c, t, c0 + 0.02 * k, 0.3, lambda a, fx=fx, fy=fy, cor=cor: pessoa(c, fx, fy, 54, cor, a), blur=4)
            for k in (6, 7):
                px, py = x0 + 3 * g + 65 + (k % 2) * 100, y0 + 96 + (k // 2) * 74
                E.saida(c, t, f1 - 0.2, lambda px=px, py=py: E.foco(c, t, e1 + 0.3, 0.4, lambda a: pessoa(c, px, py, 54, CINZA, a), blur=4))
            xr = 1500

            def contas():
                fcen(c, t, a1, "30 ÷ 8 = 3,75", xr, 400, 84)
                fcen(c, t, b1, "3 × 8 = 24", xr, 520, 84)
                E.frase(c, t, pal("s11", "seis"), [("6", "g", 76, ERRADO)] + ps("esperando", "i", 70, ERRADO), xr, 630, "center", 0.1)
                bola_txt(c, t, c1, "4", xr - 110, 770, 80, 100, CERTO)
                E.frase(c, t, c1 + 0.2, [("viagens", "g", 70, CERTO)], xr - 10, 795)
            E.saida(c, t, e1 - 0.2, contas)
            E.frase(c, t, e1, [("32", "g", 84)] + ps("pessoas:", "i", 76), xr, 420, "center", 0.1)
            fcen(c, t, pal("s11", "quatro", 3), "32 ÷ 8 = 4", xr, 560, 84, CERTO)
            E.frase(c, t, pal("s11", "sem"), ps("sem arredondar nada", "i", 62, TINTA2), xr, 660, "center", 0.1)
            E.saida(c, t, f1 - 0.2, lambda: E.frase(c, t, d1, ps("pede", "i", 62) + [("o menor número", "g", 64, COR)] + ps("que ainda resolve tudo", "i", 62),
                                                    W / 2, 950, "center", 0.1))
            E.frase(c, t, f1, [("pelo menos", "g", 76, COR)] + ps("funciona igual a", "i", 72) + [("no mínimo", "g", 76, COR)], W / 2, 950, "center", 0.12)
        E.saida(c, t, C["s12"] - 0.2, elevador)
        return
    E.linha(c, t, [("o par:", "i", 84, TINTA, C["s12"] + 0.2), ("no máximo", "g", 100, COR, a2)], XE, 170)
    E.linha(c, t, [("R$ 100", "g", 72, TINTA, pal("s12", "cem")), ("·", "g", 66, CINZA, pal("s12", "quantos")), ("ingressos de", "i", 66, TINTA, pal("s12", "ingressos")),
                   ("R$ 12", "g", 72, TINTA, pal("s12", "doze"))], XE, 270)
    y = 560
    ti = pal("s12", "ingressos")
    vx = E.reta(c, t, ti + 0.4, 260, 1660, y, 72, 120, [72, 84, 96, 108, 120], size=50, tm=[ti + 0.6 + 0.1 * i for i in range(5)])
    x100 = vx(100)
    E.foco(c, t, ti + 1.0, 0.4, lambda a: (c.drawCircle(x100, y, 18, M.paint(E.COR, a)), centro(c, "R$ 100", x100, y - 50, 58, "g", COR, a)))
    E.foco(c, t, b2, 0.4, lambda a: centro(c, "8 × 12", vx(96), y + 170, 58, "g", CERTO, a))
    E.foco(c, t, c2, 0.4, lambda a: (centro(c, "9 × 12", vx(108), y + 170, 58, "g", ERRADO, a), centro(c, "não dá", vx(108), y + 250, 54, "i", ERRADO, a)))
    E.frase(c, t, d2, ps("pede", "i", 62) + [("o maior número", "g", 64, COR)] + ps("que ainda cabe", "i", 62), W / 2, 950, "center", 0.1)
    bola_txt(c, t, e2, "8", 1640, 820, 80, 100, CERTO)


# ---------------- erro comum ----------------
def b_erro(c, t, C, b):
    a3, b3, c3 = C["s13.a"], C["s13.b"], C["s13.c"]
    E.frase(c, t, C["s13"] + 0.3, ps("o erro do começo", "i", 70, TINTA2), W / 2, 170, "center", 0.1)
    E.frase(c, t, a3, ps("ler", "i", 92) + [("a mais que", "g", 96, ERRADO)] + ps("como", "i", 92) + [("vezes", "g", 96, ERRADO)], W / 2, 310, "center", 0.12)
    E.frase(c, t, pal("s13", "três"), ps("3 reais a mais", "i", 76) + [("não é o triplo", "g", 76, ERRADO)], W / 2, 450, "center", 0.12)
    E.frase(c, t, pal("s13", "se"), ps("se Maria tem", "i", 76) + [("10", "g", 84, COR)], W / 2, 600, "center", 0.12)
    xl, xr = 620, 1300
    fcen(c, t, pal("s13", "três", 2), "3x = 30", xl, 790, 110, ERRADO)
    E.foco(c, t, b3 + 0.4, 0.5, lambda a: E.selo(c, xl, 900, 50, False, a))
    fcen(c, t, c3 - 0.3, "x + 3 = 13", xr, 790, 110, CERTO)
    E.foco(c, t, c3 + 0.3, 0.5, lambda a: E.selo(c, xr, 900, 50, True, a))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    a4, b4, c4 = C["s14.a"], C["s14.b"], C["s14.c"]
    a5, b5 = C["s15.a"], C["s15.b"]

    def um():
        E.frase(c, t, C["s14"] + 0.3, ps("agora, o atalho", "i", 70, CLARO), W / 2, 150, "center", 0.1)
        E.frase(c, t, a4, ps("na dúvida, troque a letra por", "i", 84, CLARO) + [("10", "g", 100, BR)], W / 2, 290, "center", 0.12)
        E.linha(c, t, [("Maria:", "i", 80, CLARO, pal("s14", "se")), ("10", "g", 90, BR, pal("s14", "dez", 2)), ("→", "g", 80, CLARO, pal("s14", "três")),
                       ("João:", "i", 80, CLARO, pal("s14", "três")), ("13", "g", 90, BR, b4)], W / 2, 450, "center")
        xl, xr = 640, 1280
        fcen(c, t, c4, "x + 3 = 13", xl, 650, 100, BR)
        E.foco(c, t, c4 + 1.0, 0.5, lambda a: E.selo(c, xl, 760, 48, True, a))
        fcen(c, t, pal("s14", "três", 3), "3x = 30", xr, 650, 100, BR)
        E.foco(c, t, pal("s14", "trinta") + 0.3, 0.5, lambda a: E.selo(c, xr, 760, 48, False, a))
        E.frase(c, t, pal("s14", "só"), ps("só a primeira", "i", 80, CLARO) + [("serve", "g", 84, BR)], W / 2, 940, "center", 0.12)
    E.saida(c, t, C["s15"] - 0.1, um)
    if t < C["s15"]:
        return
    tn = pal("s15", "não", 3)

    def dois():
        E.frase(c, t, a5 - 0.4, ps("a conta errada dá um valor", "i", 80, CLARO) + [("que não bate", "g", 84, BR)], W / 2, 240, "center", 0.12)
        E.frase(c, t, pal("s15", "só"), ps("só não teste com", "i", 76, CLARO) + [("2", "g", 90, BR)], W / 2, 420, "center", 0.12)
        fcen(c, t, pal("s15", "dobro"), "2 × 2 = 4", 680, 580, 96, CLARO)
        fcen(c, t, pal("s15", "ele"), "2 + 2 = 4", 1240, 580, 96, CLARO)
    E.saida(c, t, tn - 0.2, dois)
    if t >= tn - 0.2:
        E.foco(c, t, tn, 0.5, lambda a: E.selo(c, 330, 380, 56, False, a))
        E.frase(c, t, tn, ps("não compensa: a frase já vem", "i", 76, CLARO), 430, 405, "left", 0.1)
        E.frase(c, t, tn + 1.0, ps("na ordem da conta", "g", 80, BR), 430, 510, "left", 0.1)
        E.frase(c, t, b5, ps("um número mais três", "i", 84, CLARO), 660, 740, "center", 0.12)
        E.ponte(c, t, pal("s15", "escreva"), 1100, 1330, 720, "direto", None, 44)
        fcen(c, t, pal("s15", "escreva") + 0.3, "x + 3", 1550, 750, 110, BR)


# ---------------- questão ----------------
def linhas_q(C):
    return [(C["s16.a"], "Uma pessoa tem [R$ 90|t]."), (C["s16.b"], "Gasta [um terço|a] no mercado"),
            (C["s16.c"], "e [um quarto do restante|b] na farmácia."), (pal("s16", "com"), "Com o que sobrou, quer comprar"),
            (C["s16.d"], "camisetas de [R$ 20|c]."), (C["s16.e"], "No máximo, quantas ela compra?", True)]


def b_questao(c, t, C, b):
    E.frase(c, t, C["s16"] + 0.2, ps("hora de testar", "i", 64, COR), XE, 110, passo=0.12)
    enunciado(c, t, XE, 160, 1180, linhas_q(C), size=60)
    E.relogio(c, t, C["s17.a"], 1580, 440, 170)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    a8, b8, c8, d8 = (C[f"s18.{k}"] for k in "abcd")
    a9, b9, c9, d9 = (C[f"s19.{k}"] for k in "abcd")
    cel = BW / 12
    xc = lambda i: BX + cel * i
    y1 = 300

    def barra_90():
        E.foco(c, t, C["s18"] + 0.2, 0.4, lambda a: E.escreve(c, "R$ 90", BX, y1 - 30, 56, "g", TINTA, a))
        cortes = [(4, ep(t, a8, 0.5)), (8, ep(t, a8 + 0.1, 0.5)), (6, ep(t, c8, 0.5)), (10, ep(t, c8 + 0.1, 0.5))]
        pinta = [(0, 4, E.COR, ep(t, a8 + 0.3, 0.6)), (4, 6, TINTA, ep(t, c8 + 0.4, 0.6))]
        rot = [(0, 4, "30", ep(t, pal("s18", "trinta"), 0.4)), (4, 6, "15", ep(t, pal("s18", "quinze"), 0.4)), (6, 12, "45", ep(t, d8, 0.4))]
        E.foco(c, t, C["s18"] + 0.2, 0.5, lambda a: barra(c, BX, y1, BW, BH, 12, cortes, pinta, a, rot))
        chave_rot(c, t, a8, xc(0), xc(4), y1 + BH + 20, "mercado: f{1}{3} de 90", E.COR, size=50)
        chave_rot(c, t, c8, xc(4), xc(6), y1 + BH + 20, "farmácia: f{1}{4} de 60", TINTA, size=50, desce=95)
        chave_rot(c, t, pal("s18", "restante") - 0.2, xc(4), xc(12), y1 - 18, "restante: 60", COR, cima=True, size=50)
        if t >= d8:
            q = ep(t, d8, 0.4)
            E.caixa_pontilhada(c, xc(6) + 4, y1 - 10, cel * 6 - 8, BH + 20, q, CERTO, prog_=q)
        E.foco(c, t, d8 + 0.2, 0.4, lambda a: centro(c, "sobram R$ 45", xc(9) + 80, y1 + BH + 110, 54, "g", CERTO, a))
    E.saida(c, t, d9 - 0.3, barra_90)
    y = 830

    def camisetas():
        fcen(c, t, a9, "2 × 20 = 40", 500, y, 84, CERTO)
        E.foco(c, t, a9 + 0.8, 0.5, lambda a: E.selo(c, 500, y + 100, 44, True, a))
        fcen(c, t, b9, "3 × 20 = 60", 1060, y, 84, ERRADO)
        E.foco(c, t, pal("s19", "não"), 0.5, lambda a: E.selo(c, 1060, y + 100, 44, False, a))
        bola_txt(c, t, c9, "2", 1560, y - 30, 80, 100, CERTO)
        E.frase(c, t, c9 + 0.2, [("camisetas", "g", 60, CERTO)], 1560, y + 120, "center")
    E.saida(c, t, d9 - 0.3, camisetas)
    if t < d9 - 0.3:
        return
    tq = pal("s19", "quem")
    E.frase(c, t, tq, ps("quem tirou", "i", 76) + [("um quarto dos 90", "g", 76, ERRADO)], W / 2, 260, "center", 0.12)
    fcen(c, t, tq + 1.2, "90 − 30 − 22,50 = 37,50", W / 2, 480, 100, ERRADO)
    E.frase(c, t, pal("s19", "respondeu"), ps("e respondeu", "i", 80) + [("1 camiseta só", "g", 84, ERRADO)], W / 2, 720, "center", 0.12)
    E.foco(c, t, pal("s19", "respondeu") + 0.8, 0.5, lambda a: E.selo(c, W / 2, 880, 56, False, a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s20"] + 0.1, [("resumindo", "i", 88, COR)], W / 2, 170, "center")
        itens = (("s20.a", "a mais que", "soma à base"), ("s20.b", "do restante", "muda o total"),
                 ("s20.c", "no mínimo", "o menor que resolve"), ("s20.d", "no máximo", "o maior que cabe"))
        for i, (k, l1, l2) in enumerate(itens):
            y = 320 + i * 160
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 230, y - 28, 52, a=a), centro(c, str(i + 1), 230, y - 6, 60, "g", E.SOBRE, a)))
            E.frase(c, t, C[k] + 0.1, [(l1, "g", 74, COR)] + ps(l2, "i", 72), 320, y, "left", 0.1)
        E.frase(c, t, pal("s20", "são"), ps("são pistas: a história", "i", 60, TINTA2) + [("sempre confere", "g", 60, TINTA2)], W / 2, 1000, "center", 0.1)
    E.saida(c, t, C["s21"] - 0.1, resumo)
    if t < C["s21"]:
        return
    a1, b1, c1, d1, e1 = (C[f"s21.{k}"] for k in "abcde")
    E.frase(c, t, C["s21"] + 0.2, ps("na próxima aula", "i", 84), XE, 240, passo=0.14)
    E.frase(c, t, a1, ps("resolver", "i", 92) + [("desenhando", "g", 100, COR)], XE, 390, passo=0.12)
    x = XE
    for s, k in (("barras para as frações", b1), ("tabelas para as opções", c1)):
        w = E.larg(s, "b", 56) + 56 * 1.1
        E.foco(c, t, k, 0.4, lambda a, s=s, x=x, w=w: E.pilula(c, s, x + w / 2, 540, 56, "b", a=a, cor=E.SOBRE))
        x += w + 30
    E.foco(c, t, d1, 0.5, lambda a: E.pilula(c, "Inscreva-se", 1440, 750, 76, estilo="g", a=a, cor=E.SOBRE))
    p = ease_io(prog(t, d1 + 0.3, 0.8))
    E.cursor(c, lerp(1770, 1570, p), lerp(990, 775, p), ep(t, d1 + 0.2, 0.4))
    E.frase(c, t, e1, [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 930, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, amais=b_amais, restante=b_restante, minimo=b_minimo, erro=b_erro, atalho=b_atalho,
              questao=b_questao, resposta=b_resposta, fim=b_fim)
