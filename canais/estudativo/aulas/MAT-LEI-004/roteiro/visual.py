"""Visual — Estudativo · MAT-LEI-004: estimar contas e quantidades.

Linguagem da trilha Leitura de Problemas (as peças abaixo de "linguagem da trilha" servem a todas as aulas MAT-LEI):
- enunciado(): o problema num cartão branco com fio da cor da matéria. Os números são escritos em grotesca; a pergunta fica numa
  linha própria. marca = marca-texto da cor da matéria (dado útil), aponta = caixa pontilhada (dado em dúvida),
  risca = traço vermelho e número cinza (dado que não entra na conta).
- coracao(): o coração que bate na tela; escada(): a mesma conta de degrau em degrau (minuto, hora, dia, 70 anos).
- vizinho(): o número que desce para o vizinho redondo, com seta para cima ou para baixo.
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
ARQUIVO_FINAL = "estudativo_MAT-LEI-004_estimar_contas_e_quantidades.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("estimar", "coracao", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
# as contas da aula, conferidas
assert 48 * 21 == 1008 and 50 * 20 == 1000 and 5 * 2 == 10
assert 70 * 60 == 4200 and 4000 * 25 == 100000 == 10 ** 5 and 70 * 360 == 25200 and 7 * 36 == 252
assert 70 * 60 * 24 * 365 * 70 == 2575440000 and 2.5 < 3.16 and 5 + 4 == 9
assert 48 * 29 == 1392 and 1392 - 1000 == 392 and 50 * 30 == 1500
assert 15 * 60 == 900 and 1000 * 24 == 24000 and 900 * 24 == 21600 and 2.4 < 3.16


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




def coracao(c, cx, cy, s, cor=None, a=1.0, t=None):
    """coração; com t, bate (uns 70 por minuto)"""
    if a <= 0:
        return
    if t is not None:
        import math
        s *= 1 + 0.07 * max(0.0, math.sin(t * 2 * math.pi * 1.17)) ** 6
    p = skia.Path()
    p.moveTo(cx, cy + 0.62 * s)
    p.cubicTo(cx - 1.25 * s, cy - 0.15 * s, cx - 0.62 * s, cy - 1.05 * s, cx, cy - 0.45 * s)
    p.cubicTo(cx + 0.62 * s, cy - 1.05 * s, cx + 1.25 * s, cy - 0.15 * s, cx, cy + 0.62 * s)
    p.close()
    sh = skia.Paint(AntiAlias=True, Color=M.hexc("#000000", 0.22 * a))
    sh.setMaskFilter(skia.MaskFilter.MakeBlur(skia.kNormal_BlurStyle, s * 0.12))
    c.save(); c.translate(s * 0.06, s * 0.12); c.drawPath(p, sh); c.restore()
    c.drawPath(p, M.paint(cor or ERRADO, a))


def vizinho(c, t, t0, cx, y0, y1, novo, sobe, size=110, cor=None):
    """seta do número de cima até o vizinho redondo embaixo, com ↑ ou ↓ ao lado"""
    q = ep(t, t0, 0.5)
    if q <= 0:
        return
    cor = cor or COR
    M.arrow(c, cx, y0, cx, lerp(y0, y1, q), CINZA, q, 5, 18, 1.0)
    E.foco(c, t, t0 + 0.2, 0.4, lambda a: (centro(c, novo, cx, y1 + size * 0.95, size, "g", cor, a),
                                           E.pilula(c, "sobe" if sobe else "desce", cx + 150, (y0 + y1) / 2, 38, "g", a=a, cor=E.SOBRE)))


def degrau(c, t, y, rot, t_rot, estados, x=640, size=76, w_rot=None):
    """um degrau da escada: rótulo à esquerda e a conta que cresce em partes [(t0, texto, cor)], lado a lado"""
    E.foco(c, t, t_rot, 0.45, lambda a: E.escreve(c, rot, XE, y, 58, "i", TINTA2, a))
    xx = x
    for t0, s, cor in estados:
        w = E.formula(c, s, 0, 0, size, a=0)
        E.formula_em(c, t, t0, s, xx, y, size, "g", cor)
        xx += w + size * 0.3


def bola_f(c, t, t0, s, cx, cy, r, size, cor=None):
    """fórmula (potência) na esfera"""
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r, cor, a), E.formula(c, s, cx, cy + size * 0.36, size, "g", M.on(cor or E.COR), a, "center")))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    a1, b1 = C["s01.a"], C["s01.b"]

    def cena():
        E.foco(c, t, C["s01"], 0.6, lambda a: coracao(c, 1520, 470, 230, a=a, t=t))
        E.frase(c, t, C["s01"] + 0.1, ps("quantas vezes o", "i", 84) + [("coração", "g", 88, ERRADO)], XE, 250, "left", 0.12)
        E.frase(c, t, pal("s01", "bate"), ps("bate em", "i", 84) + [("70 anos?", "g", 96, COR)], XE, 380, "left", 0.12)
        E.foco(c, t, pal("s01", "milhões"), 0.4, lambda a: E.pilula(c, "milhões?", XE + 170, 540, 60, "g", fundo=CINZA, a=a))
        E.foco(c, t, pal("s01", "bilhões"), 0.4, lambda a: E.pilula(c, "bilhões?", XE + 530, 540, 60, "g", fundo=CINZA, a=a))
        E.frase(c, t, pal("s01", "dá"), ps("dá para responder", "i", 80), XE, 760, "left", 0.1)
        E.frase(c, t, b1, [("sem calculadora", "g", 80, COR)], XE, 880, "left")
        E.frase(c, t, pal("s01", "sem", 2), [("sem conta comprida", "g", 80, COR)], XE, 990, "left")
    E.saida(c, t, C["s02"] - 0.1, cena)
    if t >= C["s02"]:
        ta, tb = C["s02.a"], C["s02.b"]
        E.foco(c, t, tb - 0.2, 0.7, lambda a: E.bola(c, 1500, 540, 250 * ease_back(prog(t, tb - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, ps("até o fim desta aula", "i", 86), XE, 300, passo=0.12)
        E.frase(c, t, pal("s02", "estimar"), [("estimar", "g", 110, COR)], XE, 460, passo=0.12)
        E.frase(c, t, pal("s02", "contas"), ps("contas e quantidades", "i", 86), XE, 590, passo=0.1)
        E.frase(c, t, pal("s02", "enormes"), [("enormes", "g", 96, COR)], XE, 720, passo=0.1)
        E.foco(c, t, tb + 0.1, 0.5, lambda a: (centro(c, "+ atalho", 1500, 525, 80, "g", E.SOBRE, a),
                                               centro(c, "de prova", 1500, 610, 80, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    lista(c, t, C, "s03", (("s03.a", "arredondar", "um número"), ("s03.b", "× 10 e × 100", "acrescentando zeros"),
                           ("s03.c", "ordem de grandeza:", "a potência de 10")), "3")
    E.frase(c, t, pal("s03", "se"), ps("faltou alguma?", "i", 58, COR) + ps("procure no canal", "i", 58), 960, 1010, "left", 0.12)


# ---------------- o que é estimar ----------------
def b_estimar(c, t, C, b):
    a4, b4, c4 = C["s04.a"], C["s04.b"], C["s04.c"]
    a5, b5, c5, d5, e5 = (C[f"s05.{k}"] for k in "abcde")
    a6 = C["s06.a"]
    a7, b7, c7 = C["s07.a"], C["s07.b"], C["s07.c"]

    def ideia():
        E.frase(c, t, C["s04"] + 0.3, [("estimar", "g", 110, COR)], W / 2, 220, "center")
        E.frase(c, t, a4, ps("é fazer uma conta parecida,", "i", 76) + [("só que fácil", "g", 76, COR)], W / 2, 380, "center", 0.1)
        E.frase(c, t, b4 - 0.4, ps("troque cada número por um", "i", 70) + [("vizinho redondo", "g", 72, COR)], W / 2, 520, "center", 0.1)
        E.foco(c, t, c4, 0.5, lambda a: centro(c, "≈", 760, 860, 260, "g", COR, a))
        E.frase(c, t, c4 + 0.2, ps("aproximadamente", "i", 80), 900, 820, "left")
        E.frase(c, t, c4 + 0.6, ps("um igual ondulado", "i", 60, TINTA2), 900, 900, "left")
    E.saida(c, t, C["s05"] - 0.1, ideia)

    def conta():
        xs = E.linha(c, t, [("48", "g", 130, TINTA, a5), ("×", "g", 110, TINTA, a5 + 0.3), ("21", "g", 130, TINTA, pal("s05", "vinte"))], W / 2, 300, "center")
        c48 = xs[0] + E.larg("48", "g", 130) / 2
        c21 = xs[2] + E.larg("21", "g", 130) / 2
        vizinho(c, t, pal("s05", "quarenta", 2), c48, 340, 440, "50", True)
        vizinho(c, t, pal("s05", "vinte", 2), c21, 340, 440, "20", False)
        E.foco(c, t, c5 + 0.2, 0.4, lambda a: centro(c, "×", (c48 + c21) / 2, 545, 100, "g", COR, a))
        E.linha(c, t, [("5 × 2 = 10", "g", 96, TINTA, d5), ("+ 2 zeros", "i", 80, TINTA2, pal("s05", "zeros") - 0.3)], W / 2, 740, "center")
        E.linha(c, t, [("48 × 21", "g", 96, TINTA, e5), ("≈", "g", 96, COR, e5), ("1.000", "g", 110, COR, e5 + 0.2)], W / 2, 900, "center")
        if t >= C["s06"]:
            E.frase(c, t, a6 - 0.6, ps("conta exata:", "i", 56, TINTA2) + [("1.008", "g", 60, TINTA2)], 1590, 560, "center", 0.1)
            E.frase(c, t, pal("s06", "errou"), ps("errou por 8,", "i", 56, TINTA2), 1590, 650, "center", 0.1)
            E.frase(c, t, pal("s06", "custou"), [("em 2 segundos", "g", 58, CERTO)], 1590, 740, "center", 0.1)
    if C["s05"] - 0.1 <= t:
        E.saida(c, t, C["s07"] - 0.1, conta)
    if t < C["s07"] - 0.1:
        return
    E.frase(c, t, C["s07"] + 0.3, ps("quando isso basta?", "i", 84) + [("leia a pergunta", "g", 84, COR)], W / 2, 190, "center", 0.12)
    E.foco(c, t, a7, 0.4, lambda a: E.pilula(c, "aproximadamente", W / 2, 330, 64, "g", a=a, cor=E.SOBRE))
    y1, y2 = 560, 840
    E.frase(c, t, b7 - 0.6, ps("alternativas longe:", "i", 60, TINTA2), XE, y1 - 90, "left", 0.1)
    for i, (s, k) in enumerate((("100", b7), ("1.000", pal("s07", "mil")), ("10.000", pal("s07", "dez")))):
        x = 560 + i * 420
        cor = CERTO if (s == "1.000" and t >= pal("s07", "estimativa")) else TINTA
        E.foco(c, t, k, 0.4, lambda a, x=x, s=s, cor=cor: (M.rrect(c, x - 170, y1 - 40, 340, 120, 24, BR, a, shadow=True),
                                                           centro(c, s, x, y1 + 50, 76, "g", cor, a)))
    E.frase(c, t, pal("s07", "estimativa"), ps("a estimativa", "i", 64) + [("já escolhe", "g", 64, CERTO)], 1500, y1 + 175, "center", 0.1)
    E.frase(c, t, c7 - 0.8, ps("alternativas perto:", "i", 60, TINTA2), XE, y2 - 50, "left", 0.1)
    for i, (s, k) in enumerate((("1.008", c7), ("1.010", pal("s07", "mil", 3)))):
        x = 560 + i * 420
        E.foco(c, t, k, 0.4, lambda a, x=x, s=s: (M.rrect(c, x - 170, y2, 340, 120, 24, BR, a, shadow=True), centro(c, s, x, y2 + 90, 76, "g", TINTA, a)))
    E.frase(c, t, pal("s07", "aí"), ps("aí, só a", "i", 64) + [("conta exata", "g", 64, ERRADO)], 1500, y2 + 85, "center", 0.1)


# ---------------- o coração ----------------
def b_coracao(c, t, C, b):
    a8, b8, c8, d8 = (C[f"s08.{k}"] for k in "abcd")
    a9, b9, c9, d9 = (C[f"s09.{k}"] for k in "abcd")
    a0, b0, c0, d0, e0 = (C[f"s10.{k}"] for k in "abcde")
    a1, b1, c1, d1 = (C[f"s11.{k}"] for k in "abcd")
    a2, b2, c2 = C["s12.a"], C["s12.b"], C["s12.c"]

    def escada():
        E.foco(c, t, C["s08"] + 0.2, 0.5, lambda a: coracao(c, 1720, 170, 80, a=a, t=t))
        E.frase(c, t, C["s08"] + 0.3, ps("em repouso,", "i", 64, TINTA2) + [("70 batidas por minuto", "g", 66, ERRADO)], XE, 170, "left", 0.1)
        degrau(c, t, 340, "por hora", b8, [(c8, "70 × 60 = 4.200", TINTA), (d8, "≈ 4.000", COR)])
        degrau(c, t, 540, "por dia", a9, [(a9, "24 h ≈ 25 h", TINTA2)], size=60)
        degrau(c, t, 640, "", c9, [(c9, "4.000 × 25 = 100.000", TINTA), (d9, "= 10^{5}", COR)])
        rot4 = "dias em 70 anos"
        E.foco(c, t, C["s10"] + 0.3, 0.45, lambda a: E.escreve(c, rot4, XE, 840, 58, "i", TINTA2, a))
        E.saida(c, t, b0 - 0.15, lambda: E.formula_em(c, t, a0, "70 × 365", 640, 840, 76, "g", TINTA), d=0.3)
        E.formula_em(c, t, b0, "70 × 360", 640, 840, 76, "g", TINTA)
        E.formula_em(c, t, d0, "= 25.200", 1010, 840, 76, "g", TINTA)
        E.formula_em(c, t, e0, "≈ 2,5 × 10^{4}", 1400, 840, 76, "g", COR)
        E.foco(c, t, c0, 0.4, lambda a: E.formula(c, "7 × 36 = 252, e dois zeros", 640, 940, 54, "b", TINTA2, a))
    E.saida(c, t, C["s11"] - 0.1, escada)
    if t < C["s11"] - 0.1:
        return
    E.foco(c, t, C["s11"], 0.5, lambda a: coracao(c, 1720, 170, 80, a=a, t=t))
    E.frase(c, t, C["s11"] + 0.3, ps("batidas em 70 anos:", "i", 64, TINTA2), XE, 170, "left", 0.1)
    fcen(c, t, a1, "10^{5} × 2,5 × 10^{4}", W / 2, 360, 110)
    E.frase(c, t, pal("s11", "frente"), ps("na frente:", "i", 64) + [("2,5", "g", 70, COR)], 620, 500, "center", 0.1)
    E.frase(c, t, pal("s11", "nas"), ps("nas potências:", "i", 64) + [("5 + 4 = 9", "g", 70, COR)], 1300, 500, "center", 0.1)
    fcen(c, t, c1, "= 2,5 × 10^{9}", W / 2, 680, 120, COR)
    E.saida(c, t, a2 - 0.2, lambda: E.frase(c, t, d1, ps("uns", "i", 76) + [("2 bilhões e meio", "g", 80, ERRADO)] + ps("de batidas", "i", 76),
                                            W / 2, 860, "center", 0.12))
    if t >= a2 - 0.2:
        E.frase(c, t, a2, [("2,5", "g", 70)] + ps("não passa de", "i", 64) + [("3,16", "g", 70)], 560, 860, "center", 0.1)
        bola_f(c, t, b2, "10^{9}", 1060, 840, 90, 76)
        E.frase(c, t, b2 + 0.2, ps("ordem de grandeza", "i", 54, TINTA2), 1060, 980, "center", 0.08)
        E.frase(c, t, pal("s12", "conta"), ps("conta exata:", "i", 56, TINTA2), 1570, 790, "center", 0.1)
        E.frase(c, t, pal("s12", "cerca"), [("≈ 2.575.000.000", "g", 60, TINTA2)], 1570, 870, "center", 0.1)
        E.frase(c, t, pal("s12", "mesma"), [("mesma ordem", "g", 62, CERTO)], 1570, 970, "center")


# ---------------- erro comum ----------------
def b_erro(c, t, C, b):
    a3, b3, c3, d3, e3 = (C[f"s13.{k}"] for k in "abcde")
    E.frase(c, t, C["s13"] + 0.3, ps("o erro:", "i", 84) + [("perder um zero", "g", 88, ERRADO)], W / 2, 200, "center", 0.12)
    xs = E.linha(c, t, [("50 × 20", "g", 130, TINTA, pal("s13", "cinquenta"))], W / 2, 400, "center")
    w0 = E.larg("0", "g", 130)
    if t >= pal("s13", "mas"):
        for cx0, k in ((xs[0] + E.larg("50", "g", 130) - w0 / 2, pal("s13", "cinquenta", 2)), (xs[0] + E.larg("50 × 20", "g", 130) - w0 / 2, pal("s13", "vinte", 2))):
            q = ep(t, k, 0.35)
            c.drawCircle(cx0, 353, 62 * q, M.paint(E.COR, 0.14 * q))
            c.drawCircle(cx0, 353, 62 * q, M.paint(E.COR, q, stroke=5))
    fcen(c, t, b3, "5 × 2 = 10", W / 2, 560, 96)
    xl, xr = 620, 1300
    E.foco(c, t, pal("s13", "pessoa"), 0.4, lambda a: centro(c, "só 1 zero", xl, 720, 60, "i", ERRADO, a))
    E.foco(c, t, c3, 0.5, lambda a: centro(c, "100", xl, 860, 130, "g", ERRADO, a))
    E.foco(c, t, c3 + 0.4, 0.5, lambda a: E.selo(c, xl + 200, 815, 46, False, a))
    E.foco(c, t, d3, 0.4, lambda a: centro(c, "2 zeros", xr, 720, 60, "i", CERTO, a))
    E.foco(c, t, d3 + 0.4, 0.5, lambda a: centro(c, "1.000", xr, 860, 130, "g", CERTO, a))
    E.foco(c, t, d3 + 0.8, 0.5, lambda a: E.selo(c, xr + 260, 815, 46, True, a))
    E.frase(c, t, e3 - 1.0, ps("errar um zero é errar", "i", 70) + [("10 vezes", "g", 76, ERRADO)], W / 2, 1010, "center", 0.1)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    a4, b4 = C["s14.a"], C["s14.b"]
    a5, b5, c5, d5 = (C[f"s15.{k}"] for k in "abcd")

    def par(x, y, de, para, sobe, t0, size=96):
        """48 → 50 com a seta ↑ (ou ↓)"""
        wd, wp = E.larg(de, "g", size), E.larg(para, "g", size)
        E.foco(c, t, t0, 0.45, lambda a: (E.escreve(c, de, x - 70 - wd, y, size, "g", CLARO, a), centro(c, "→", x, y - 6, size * 0.8, "g", CLARO, a),
                                          E.escreve(c, para, x + 70, y, size, "g", BR, a),
                                          E.pilula(c, "sobe" if sobe else "desce", x + 70 + wp + 110, y - size * 0.33, 44, "g", fundo=BR, cor=TINTA, a=a)))

    def um():
        E.frase(c, t, C["s14"] + 0.3, ps("agora, o atalho", "i", 70, CLARO), W / 2, 150, "center", 0.1)
        E.frase(c, t, a4, ps("na multiplicação, um", "i", 80, CLARO) + [("para cima,", "g", 84, BR)], W / 2, 290, "center", 0.12)
        E.frase(c, t, pal("s14", "o", 2), ps("o outro", "i", 80, CLARO) + [("para baixo", "g", 84, BR)], W / 2, 400, "center", 0.12)
        par(760, 600, "48", "50", True, pal("s14", "quarenta"))
        par(760, 760, "21", "20", False, pal("s14", "vinte"))
        E.frase(c, t, b4, ps("os erros", "i", 84, CLARO) + [("se compensam", "g", 90, BR)], W / 2, 960, "center", 0.12)
    E.saida(c, t, C["s15"] - 0.1, um)
    if t < C["s15"]:
        return
    tn = pal("s15", "não")

    def dois():
        E.frase(c, t, C["s15"] + 0.3, ps("no coração, igual", "i", 76, CLARO), W / 2, 180, "center", 0.1)
        par(760, 380, "4.200", "4.000", False, a5, 90)
        par(760, 530, "24", "25", True, b5, 90)
        E.frase(c, t, c5 - 0.6, ps("um que cresce", "i", 80, CLARO) + [("equilibra", "g", 84, BR)] + ps("o que diminui", "i", 80, CLARO), W / 2, 760, "center", 0.12)
    E.saida(c, t, tn - 0.2, dois)
    if t < tn - 0.2:
        return
    E.foco(c, t, tn, 0.5, lambda a: E.selo(c, 330, 240, 56, False, a))
    E.frase(c, t, tn, ps("não compensa:", "i", 76, CLARO) + [("descer longe demais", "g", 80, BR)], 430, 265, "left", 0.1)
    fcen(c, t, d5, "48 × 29", W / 2, 460, 110, BR)
    E.frase(c, t, pal("s15", "vai"), ps("29 vai para", "i", 72, CLARO) + [("30", "g", 84, BR)], W / 2, 600, "center", 0.12)
    E.frase(c, t, pal("s15", "forçar"), ps("forçar para 20:", "i", 66, CLARO) + [("50 × 20 = 1.000", "g", 70, BR)], W / 2, 780, "center", 0.1)
    E.frase(c, t, pal("s15", "quase"), ps("contra 1.392:", "i", 66, CLARO) + [("erro de quase 400", "g", 70, ERRADO)], W / 2, 900, "center", 0.1)


# ---------------- questão ----------------
def linhas_q(C):
    return [(C["s16.a"] - 2.0, "Em repouso, uma pessoa respira"), (C["s16.a"], "cerca de [15 vezes por minuto|r]."),
            (C["s16.b"], "Estime quantas vezes ela respira em um dia", True), (C["s16.c"], "e dê a ordem de grandeza.", True)]


def b_questao(c, t, C, b):
    E.frase(c, t, C["s16"] + 0.2, ps("hora de testar", "i", 64, COR), XE, 150, passo=0.12)
    enunciado(c, t, XE, 210, 1240, linhas_q(C), size=62)
    E.relogio(c, t, C["s17.a"], 1600, 760, 150)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    a8, b8, c8 = C["s18.a"], C["s18.b"], C["s18.c"]
    a9, b9, c9 = C["s19.a"], C["s19.b"], C["s19.c"]

    def escada():
        E.frase(c, t, C["s18"] + 0.3, ps("respirando", "i", 64, TINTA2) + [("15 vezes por minuto", "g", 66, COR)], XE, 170, "left", 0.1)
        degrau(c, t, 360, "por hora", pal("s18", "por"), [(a8, "15 × 60 = 900", TINTA), (b8, "≈ 1.000", COR)])
        degrau(c, t, 560, "por dia", pal("s18", "por", 2), [(c8, "1.000 × 24 = 24.000", TINTA)])
        E.frase(c, t, pal("s18", "aqui"), ps("o 24 fica:", "i", 60, TINTA2) + [("o 900 já subiu", "g", 62, COR)], 640, 690, "left", 0.1)
    E.saida(c, t, C["s19"] - 0.1, escada)
    if t < C["s19"] - 0.1:
        return
    fcen(c, t, a9, "24.000 = 2,4 × 10^{4}", W / 2, 300, 110)
    E.frase(c, t, pal("s19", "dois", 2), [("2,4", "g", 76)] + ps("não passa de", "i", 70) + [("3,16", "g", 76)], W / 2, 470, "center", 0.12)
    bola_f(c, t, b9, "10^{4}", 640, 720, 100, 84)
    E.frase(c, t, b9 + 0.3, ps("ordem de grandeza", "i", 60), 640, 880, "center", 0.1)
    E.frase(c, t, c9, ps("exata:", "i", 64, TINTA2) + [("21.600", "g", 76, TINTA2)], 1300, 700, "center", 0.1)
    E.frase(c, t, pal("s19", "mesma"), [("a mesma ordem", "g", 72, CERTO)], 1300, 820, "center")
    E.foco(c, t, pal("s19", "mesma") + 0.5, 0.5, lambda a: E.selo(c, 1300, 920, 44, True, a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s20"] + 0.1, [("resumindo", "i", 92, COR)], W / 2, 200, "center")
        itens = (("s20.a", "troque", "por vizinhos redondos"), ("s20.b", "conte os zeros", "com cuidado"), ("s20.c", "a pergunta", "diz se a estimativa basta"))
        for i, (k, l1, l2) in enumerate(itens):
            y = 380 + i * 200
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 230, y - 30, 56, a=a), centro(c, str(i + 1), 230, y - 7, 64, "g", E.SOBRE, a)))
            E.frase(c, t, C[k] + 0.1, [(l1, "g", 76, COR)] + ps(l2, "i", 74), 320, y, "left", 0.1)
    E.saida(c, t, C["s21"] - 0.1, resumo)
    if t < C["s21"]:
        return
    a1, b1, c1 = (C[f"s21.{k}"] for k in "abc")
    E.frase(c, t, C["s21"] + 0.2, ps("na próxima aula", "i", 84), XE, 240, passo=0.14)
    E.frase(c, t, pal("s21", "conta"), ps("a conta de água", "i", 90) + [("por faixas", "g", 100, COR)], XE, 390, passo=0.12)
    E.frase(c, t, pal("s21", "cada"), ps("cada faixa de consumo,", "i", 66) + [("um preço", "g", 68, COR)], XE, 520, passo=0.1)
    E.foco(c, t, b1, 0.5, lambda a: E.pilula(c, "Inscreva-se", 1440, 750, 76, estilo="g", a=a, cor=E.SOBRE))
    p = ease_io(prog(t, b1 + 0.3, 0.8))
    E.cursor(c, lerp(1770, 1570, p), lerp(990, 775, p), ep(t, b1 + 0.2, 0.4))
    E.frase(c, t, c1, [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 930, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, estimar=b_estimar, coracao=b_coracao, erro=b_erro, atalho=b_atalho,
              questao=b_questao, resposta=b_resposta, fim=b_fim)
