"""Visual — Estudativo · MAT-LEI-005: conta por faixas.

Linguagem da trilha Leitura de Problemas (as peças abaixo de "linguagem da trilha" servem a todas as aulas MAT-LEI):
- enunciado(): o problema num cartão branco com fio da cor da matéria. Os números são escritos em grotesca; a pergunta fica numa
  linha própria. marca = marca-texto da cor da matéria (dado útil), aponta = caixa pontilhada (dado em dúvida),
  risca = traço vermelho e número cinza (dado que não entra na conta).
- regua() e enche(): o consumo numa régua de 0 a 30 m³, com as três faixas atrás; cada pedaço do consumo ganha o tom da sua faixa.
- tabela(): a tabela de preços (cabeçalho na cor da matéria), a mesma peça das tabelas de palpite da trilha.
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
ARQUIVO_FINAL = "estudativo_MAT-LEI-005_conta_por_faixas.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("faixas", "conta", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
# as contas da aula, conferidas (em centavos, para não errar com vírgula)
assert 10 * 350 == 3500 and 10 * 500 == 5000 and 4 * 820 == 3280 and 4 * 82 == 328 and 3500 + 5000 + 3280 == 11780
assert 24 * 820 == 19680 and 19680 - 11780 == 7900 and 7 * 350 == 2450
assert 31 - 20 == 11 and 11 * 82 == 902 and 11 * 820 == 9020 and 8500 + 9020 == 17520


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




# ---------------- a régua das faixas ----------------
FX0, FX1, FMAX = 220, 1700, 30
TONS = None


def tons():
    return (E.mix(E.COR, BR, 0.55), E.mix(E.COR, BR, 0.22), E.mix(E.COR, "#000000", 0.3))


def fx(v):
    return FX0 + (FX1 - FX0) * v / FMAX


def regua(c, t, t0, y, h=110, precos=None, tp=(), cinza=False):
    """régua do consumo de 0 a 30 m³: as três faixas atrás, os limites 10 e 20 tracejados. precos = textos em cima de cada faixa (tp = instantes)"""
    def caixa(a):
        r = skia.RRect.MakeRectXY(skia.Rect.MakeLTRB(fx(0), y, fx(FMAX), y + h), 16, 16)
        s = skia.Paint(AntiAlias=True, Color=M.hexc("#000000", 0.10 * a))
        s.setMaskFilter(skia.MaskFilter.MakeBlur(skia.kNormal_BlurStyle, 14))
        c.save(); c.translate(4, 10); c.drawRRect(r, s); c.restore()
        c.drawRRect(r, M.paint(BR, a))
        for v0, v1, k in ((0, 10, 0), (10, 20, 1), (20, FMAX, 2)):
            c.drawRect(skia.Rect.MakeLTRB(fx(v0) + 2, y + h - 12, fx(v1) - 2, y + h - 2), M.paint(tons()[k], a * 0.9))
        for v in (10, 20):
            M.line(c, fx(v), y - 14, fx(v), y + h + 14, TINTA2, a, 4, dash=[10, 8])
        c.drawRRect(r, M.paint(TINTA, a, stroke=3))
        for v in (0, 10, 20, 30):
            centro(c, str(v), fx(v), y + h + 62, 50, "b", TINTA2, a)
        centro(c, "m³", fx(FMAX) + 70, y + h + 62, 46, "b", TINTA2, a)
    E.foco(c, t, t0, 0.5, caixa)
    if precos:
        for (v0, v1), s, ti in zip(((0, 10), (10, 20), (20, FMAX)), precos, tp):
            E.foco(c, t, ti, 0.4, lambda a, v0=v0, v1=v1, s=s: centro(c, s, (fx(v0) + fx(v1)) / 2, y - 34, 52, "g", TINTA, a))


def enche(c, t, y, h, pedacos, size=64):
    """pedaços do consumo: [(de, até, faixa 0..2, t0, rótulo)]"""
    for v0, v1, k, t0, s in pedacos:
        p = ease_io(prog(t, t0, 0.6))
        if p <= 0:
            continue
        x0 = fx(v0)
        w = (fx(v1) - x0) * p
        M.rrect(c, x0 + 4, y + 6, w - 8, h - 24, 10, tons()[k], 1.0)
        if s and p > 0.8:
            centro(c, s, x0 + (fx(v1) - x0) / 2, y + (h - 18) / 2 + size * 0.36, size, "g", TINTA if k == 0 else BR, ep(t, t0 + 0.4, 0.3))


def chip(c, x, y, s, k, a=1.0, size=56):
    """o pedaço do consumo como etiqueta na cor da faixa; (x, y) = canto esquerdo, y = linha de base"""
    w = E.larg(s, "g", size) + size * 0.9
    M.rrect(c, x, y - size * 0.95, w, size * 1.35, 12, tons()[k], a)
    E.escreve(c, s, x + size * 0.45, y, size, "g", TINTA if k == 0 else BR, a)
    return w


def linha_faixa(c, t, t0, y, s, k, conta, tc, cor=None, x=XE):
    """[10 m³] × R$ 3,50 = R$ 35,00, com a conta entrando em tc"""
    E.foco(c, t, t0, 0.4, lambda a: chip(c, x, y, s, k, a))
    E.formula_em(c, t, tc, conta, x + 240, y, 66, "g", cor)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    a1, b1, c1 = C["s01.a"], C["s01.b"], C["s01.c"]

    def cena():
        E.frase(c, t, pal("s01", "uma"), ps("uma casa gastou", "i", 84), W / 2, 210, "center", 0.12)
        E.frase(c, t, a1, [("24 m³", "g", 120, COR)] + ps("de água no mês", "i", 84), W / 2, 380, "center", 0.12)
        E.frase(c, t, pal("s01", "se"), ps("se você calculou", "i", 76), W / 2, 560, "center", 0.12)
        E.foco(c, t, b1, 0.5, lambda a: centro(c, "R$ 196,80", W / 2, 740, 150, "g", ERRADO, a))
        E.foco(c, t, c1 - 0.2, 0.5, lambda a: E.selo(c, W / 2 + 470, 690, 56, False, a))
        E.frase(c, t, c1, ps("cobrou", "i", 80) + [("quase R$ 80 a mais", "g", 84, ERRADO)], W / 2, 920, "center", 0.12)
    E.saida(c, t, C["s02"] - 0.1, cena)
    if t >= C["s02"]:
        ta, tb = C["s02.a"], C["s02.b"]
        E.foco(c, t, tb - 0.2, 0.7, lambda a: E.bola(c, 1500, 540, 250 * ease_back(prog(t, tb - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, ps("até o fim desta aula", "i", 86), XE, 300, passo=0.12)
        E.frase(c, t, pal("s02", "calcula"), ps("qualquer conta", "i", 86), XE, 450, passo=0.12)
        E.frase(c, t, pal("s02", "cobrada"), ps("cobrada", "i", 86) + [("por faixas", "g", 100, COR)], XE, 590, passo=0.12)
        E.foco(c, t, tb + 0.1, 0.5, lambda a: (centro(c, "+ atalho", 1500, 525, 80, "g", E.SOBRE, a),
                                               centro(c, "de prova", 1500, 610, 80, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    lista(c, t, C, "s03", (("s03.a", "multiplicar", "números com vírgula"), ("s03.b", "ler a pergunta", "antes do texto")), "2")
    E.frase(c, t, pal("s03", "se"), ps("faltou alguma?", "i", 58, COR) + ps("procure no canal", "i", 58), 960, 1000, "left", 0.12)


# ---------------- metro cúbico e faixas ----------------
PRECOS = ("R$ 3,50", "R$ 5,00", "R$ 8,20")


def linhas_precos(C):
    return [(C["s06.a"], [("primeiros 10 m³", TINTA), ("R$ 3,50", TINTA)]), (C["s06.b"], [("10 seguintes", TINTA), ("R$ 5,00", TINTA)]),
            (C["s06.c"], [("acima de 20 m³", TINTA), ("R$ 8,20", TINTA)])]


def b_faixas(c, t, C, b):
    a4, b4, c4 = C["s04.a"], C["s04.b"], C["s04.c"]
    a5, b5 = C["s05.a"], C["s05.b"]

    def cubo():
        E.frase(c, t, C["s04"] + 0.3, ps("antes, a unidade:", "i", 76) + [("metro cúbico", "g", 80, COR)], W / 2, 180, "center", 0.12)
        E.cubo(c, t, b4 - 0.2, 380, 830, 400, "1 m", todas=True)
        E.foco(c, t, a4 + 0.2, 0.5, lambda a: centro(c, "1 m³", 1350, 520, 150, "g", COR, a))
        E.foco(c, t, c4, 0.5, lambda a: centro(c, "= 1.000 litros", 1350, 700, 110, "g", TINTA, a))
        E.frase(c, t, b4, ps("1 m de largura, comprimento e altura", "i", 50, TINTA2), 1350, 850, "center", 0.06)
    E.saida(c, t, C["s05"] - 0.1, cubo)
    if t < C["s05"] - 0.1:
        return

    def ideia():
        E.frase(c, t, a5 - 0.6, ps("conta cobrada", "i", 84) + [("por faixas", "g", 96, COR)], W / 2, 230, "center", 0.12)
        E.frase(c, t, pal("s05", "quanto"), ps("quanto mais você gasta, mais caro cada metro cúbico", "i", 62), W / 2, 400, "center", 0.08)
        E.frase(c, t, b5, ps("mas", "i", 76) + [("só a parte que passou", "g", 80, COR)] + ps("de cada limite", "i", 76), W / 2, 560, "center", 0.1)
        E.frase(c, t, pal("s05", "veja"), ps("tabela inventada para esta aula", "i", 56, TINTA2), W / 2, 760, "center", 0.08)
    E.saida(c, t, C["s06"] - 0.1, ideia)
    if t < C["s06"] - 0.1:
        return
    E.frase(c, t, C["s06"] + 0.1, ps("tabela inventada para esta aula", "i", 56, TINTA2), W / 2, 170, "center", 0.08)
    tabela(c, t, 420, 220, (620, 460), ("consumo", "preço do m³"), linhas_precos(C), C["s06"], h=104, size=70)
    regua(c, t, C["s06.a"] - 0.3, 830, 100, PRECOS, (pal("s06", "três"), pal("s06", "cinco"), pal("s06", "oito")))


# ---------------- a conta de 24 m³ ----------------
RY, RH = 250, 120


def b_conta(c, t, C, b):
    a7, b7, c7, d7, e7 = (C[f"s07.{k}"] for k in "abcde")
    a8, b8 = C["s08.a"], C["s08.b"]
    a9, b9, c9 = C["s09.a"], C["s09.b"], C["s09.c"]
    a0, b0 = C["s10.a"], C["s10.b"]
    a1, b1, c1 = C["s11.a"], C["s11.b"], C["s11.c"]

    def conta24():
        E.frase(c, t, C["s07"] + 0.3, [("24 m³", "g", 72, COR)], XE, 130)
        E.foco(c, t, a7, 0.4, lambda a: E.pilula(c, "a pergunta: o valor em reais", 900, 108, 46, "g", a=a, cor=E.SOBRE))
        regua(c, t, C["s07"] + 0.4, RY, RH, PRECOS, (C["s07"] + 0.6,) * 3)
        enche(c, t, RY, RH, [(0, 10, 0, c7, "10"), (10, 20, 1, d7, "10"), (20, 24, 2, e7, "4")])
        E.saida(c, t, a8 - 0.2, lambda: E.frase(c, t, b7, ps("o segredo:", "i", 70) + [("cortar o consumo nas faixas", "g", 72, COR)], W / 2, 620, "center", 0.1))
        E.saida(c, t, a8 - 0.2, lambda: E.frase(c, t, pal("s07", "dez", 3), [("10 + 10 + 4 = 24", "g", 80)] + ps("fecha", "i", 72, CERTO), W / 2, 760, "center", 0.12))
        linha_faixa(c, t, a8 - 0.3, 600, "10 m³", 0, "× 3,50 = 35,00", pal("s08", "trinta"))
        linha_faixa(c, t, b8 - 0.3, 720, "10 m³", 1, "× 5,00 = 50,00", pal("s08", "cinquenta"))
        linha_faixa(c, t, a9 - 0.3, 840, "4 m³", 2, "× 8,20 = 32,80", c9)
        xr = 1500
        E.saida(c, t, a0 - 0.2, lambda: (E.frase(c, t, pal("s09", "sem"), ps("sem a vírgula:", "i", 56, TINTA2), xr, 640, "center", 0.08),
                                         fcen(c, t, b9, "4 × 82 = 328", xr, 740, 70),
                                         E.frase(c, t, pal("s09", "com"), ps("1 casa:", "i", 56, TINTA2) + [("32,8", "g", 66, COR)], xr, 840, "center", 0.08)))
        E.foco(c, t, a0, 0.4, lambda a: E.escreve(c, "total:", XE, 980, 60, "i", TINTA, a))
        E.formula_em(c, t, a0 + 0.2, "35 + 50 + 32,80", XE + 200, 980, 70, "g", TINTA)
        E.foco(c, t, b0, 0.5, lambda a: E.pilula(c, "R$ 117,80", 1450, 960, 84, "g", fundo=CERTO, a=a))
    E.saida(c, t, C["s11"] - 0.1, conta24)
    if t < C["s11"] - 0.1:
        return
    E.frase(c, t, C["s11"] + 0.2, ps("e quem gastou só", "i", 72) + [("7 m³?", "g", 80, COR)], XE, 150, "left", 0.12)
    regua(c, t, C["s11"] + 0.4, RY + 30, RH, PRECOS, (C["s11"] + 0.6,) * 3)
    enche(c, t, RY + 30, RH, [(0, 7, 0, a1 + 0.3, "7")])
    E.frase(c, t, pal("s11", "fica"), ps("tudo na", "i", 70) + [("primeira faixa", "g", 72, COR)], W / 2, 640, "center", 0.12)
    fcen(c, t, b1, "7 × 3,50 = 24,50", W / 2, 780, 96)
    E.frase(c, t, pal("s11", "cobrar"), ps("quem gasta pouco paga menos por metro cúbico,", "i", 58), W / 2, 920, "center", 0.07)
    E.frase(c, t, c1, [("pesa no bolso", "g", 64, ERRADO)] + ps("de quem gasta muito", "i", 62), W / 2, 1010, "center", 0.1)


# ---------------- erro comum ----------------
def b_erro(c, t, C, b):
    a2, b2 = C["s12.a"], C["s12.b"]
    a3, b3, c3, d3, e3 = (C[f"s13.{k}"] for k in "abcde")

    def errado():
        E.frase(c, t, pal("s12", "cento"), ps("e os", "i", 80) + [("R$ 196,80", "g", 86, ERRADO)] + ps("do começo?", "i", 80), W / 2, 200, "center", 0.12)
        E.frase(c, t, pal("s12", "viu"), ps("passou de 20, e cobrou", "i", 72) + [("tudo pelo preço mais caro", "g", 74, ERRADO)], W / 2, 400, "center", 0.1)
        fcen(c, t, b2, "24 × 8,20 = 196,80", W / 2, 620, 120, ERRADO)
        E.foco(c, t, b2 + 1.2, 0.5, lambda a: E.selo(c, W / 2 + 640, 580, 56, False, a))
    E.saida(c, t, C["s13"] - 0.1, errado)
    if t < C["s13"] - 0.1:
        return

    def certo():
        regua(c, t, C["s13"], 330, RH, PRECOS, (C["s13"] + 0.2,) * 3)
        enche(c, t, 330, RH, [(0, 10, 0, b3, "10"), (10, 20, 1, b3 + 0.2, "10"), (20, 24, 2, a3, "4")])
        E.frase(c, t, a3, ps("R$ 8,20 vale", "i", 64) + [("só para os 4 depois do 20", "g", 66, COR)], W / 2, 180, "center", 0.1)
        E.frase(c, t, b3, ps("os primeiros 20:", "i", 64) + [("preço das faixas de baixo", "g", 66, COR)], W / 2, 640, "center", 0.1)
        E.frase(c, t, c3, ps("passar de faixa", "i", 72) + [("não muda o preço", "g", 76, ERRADO)] + ps("do que veio antes", "i", 72), W / 2, 830, "center", 0.1)
    tq = pal("s13", "quem")
    E.saida(c, t, tq - 0.2, certo)
    if t < tq - 0.2:
        return
    E.linha(c, t, [("de", "i", 90, TINTA, tq), ("20 m³", "g", 100, TINTA, tq + 0.4), ("para", "i", 90, TINTA, pal("s13", "para", 2)),
                   ("21 m³", "g", 100, COR, d3)], W / 2, 330, "center")
    E.frase(c, t, e3 - 0.5, ps("paga só", "i", 90) + [("+ R$ 8,20", "g", 110, CERTO)], W / 2, 560, "center", 0.12)
    E.frase(c, t, pal("s13", "não", 2), ps("e não a conta inteira", "i", 76) + [("pelo preço mais caro", "g", 78, ERRADO)], W / 2, 800, "center", 0.1)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    a4, b4, c4 = C["s14.a"], C["s14.b"], C["s14.c"]
    a5, b5 = C["s15.a"], C["s15.b"]

    def um():
        E.frase(c, t, C["s14"] + 0.3, ps("agora, o atalho", "i", 70, CLARO), W / 2, 150, "center", 0.1)
        E.frase(c, t, a4, ps("faixa cheia vira", "i", 96, CLARO) + [("valor fixo", "g", 104, BR)], W / 2, 300, "center", 0.12)
        E.frase(c, t, pal("s14", "quem"), ps("quem passa de 20 sempre paga", "i", 70, CLARO), W / 2, 450, "center", 0.1)
        fcen(c, t, b4, "35 + 50 = 85", W / 2, 610, 130, BR)
        E.frase(c, t, pal("s14", "pelos"), ps("pelos primeiros", "i", 66, CLARO) + [("20 m³", "g", 66, BR)], W / 2, 710, "center", 0.1)
        E.frase(c, t, pal("s14", "depois"), ps("depois, só calcula", "i", 84, CLARO) + [("o que passou", "g", 90, BR)], W / 2, 900, "center", 0.12)
    E.saida(c, t, C["s15"] - 0.1, um)
    if t < C["s15"]:
        return
    E.frase(c, t, a5 - 0.6, ps("as faixas de baixo são", "i", 76, CLARO) + [("iguais para todo mundo", "g", 80, BR)], W / 2, 240, "center", 0.12)
    E.frase(c, t, pal("s15", "você"), ps("faça a conta", "i", 76, CLARO) + [("uma vez", "g", 80, BR)] + ps("e reaproveite", "i", 76, CLARO), W / 2, 380, "center", 0.12)
    tn = pal("s15", "não")
    E.foco(c, t, tn, 0.5, lambda a: E.selo(c, 330, 590, 56, False, a))
    E.frase(c, t, tn, ps("não compensa: consumo", "i", 76, CLARO) + [("dentro da 1ª faixa", "g", 80, BR)], 430, 615, "left", 0.1)
    E.frase(c, t, pal("s15", "aí"), ps("aí, é", "i", 86, CLARO) + [("uma multiplicação só", "g", 92, BR)], W / 2, 860, "center", 0.12)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s16"] + 0.2, ps("hora de testar,", "i", 64, COR) + ps("com a mesma tabela", "i", 64), XE, 150, "left", 0.1)
    tabela(c, t, XE, 210, (520, 380), ("consumo", "preço do m³"), [(C["s16"] + 0.5 + 0.15 * i, cel) for i, (_, cel) in enumerate(linhas_precos(C))],
           C["s16"] + 0.4, h=100, size=62)
    enunciado(c, t, XE, 680, 1200, [(C["s16.a"] - 0.5, "Uma casa gastou [31 m³|m] no mês."), (C["s16.b"], "Quanto vai pagar?", True)], size=66)
    E.relogio(c, t, C["s17.a"], 1600, 440, 160)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    a8, b8 = C["s18.a"], C["s18.b"]
    a9, b9, c9, d9 = (C[f"s19.{k}"] for k in "abcd")
    E.frase(c, t, C["s18"] + 0.3, ps("pelo", "i", 66) + [("atalho", "g", 70, COR)], XE, 130, "left", 0.1)
    regua(c, t, C["s18"] + 0.4, RY, RH, PRECOS, (C["s18"] + 0.6,) * 3)
    q = ep(t, b8, 0.6)
    enche(c, t, RY, RH, [(0, 20, 1, a8 - 0.4, "R$ 85")])
    if t >= b8:
        # o que passou de 20 vai até 31: a régua só mostra até 30, então a ponta passa da borda com uma seta
        x0, x1 = fx(20), fx(30) + 70 * q
        M.rrect(c, x0 + 4, RY + 6, x1 - x0 - 8, RH - 24, 10, tons()[2], 1.0)
        E.foco(c, t, b8 + 0.5, 0.3, lambda a: centro(c, "11", (x0 + x1) / 2, RY + (RH - 18) / 2 + 23, 64, "g", BR, a))
    E.foco(c, t, pal("s18", "passou"), 0.4, lambda a: E.escreve(c, "passou de 20:", XE, 600, 60, "i", TINTA, a))
    E.formula_em(c, t, b8, "31 − 20 = 11 m³", XE + 420, 600, 72, "g", COR)
    fcen(c, t, a9, "11 × 8,2", 560, 760, 80)
    E.frase(c, t, pal("s19", "sem"), ps("sem a vírgula:", "i", 54, TINTA2), 1200, 730, "center", 0.08)
    fcen(c, t, b9, "11 × 82 = 902", 1200, 820, 72)
    E.frase(c, t, c9, ps("1 casa:", "i", 56, TINTA2) + [("R$ 90,20", "g", 68, COR)], 560, 860, "center", 0.1)
    E.foco(c, t, d9 - 0.3, 0.4, lambda a: E.escreve(c, "total:", XE, 1000, 60, "i", TINTA, a))
    E.formula_em(c, t, d9, "85 + 90,20", XE + 200, 1000, 70, "g", TINTA)
    E.foco(c, t, pal("s19", "cento"), 0.5, lambda a: E.pilula(c, "R$ 175,20", 1450, 980, 84, "g", fundo=CERTO, a=a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s20"] + 0.1, [("resumindo", "i", 92, COR)], W / 2, 200, "center")
        itens = (("s20.a", "corte", "o consumo nas faixas"), ("s20.b", "cada pedaço", "com o seu preço"), ("s20.c", "some", "os pedaços no fim"))
        for i, (k, l1, l2) in enumerate(itens):
            y = 380 + i * 200
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 230, y - 30, 56, a=a), centro(c, str(i + 1), 230, y - 7, 64, "g", E.SOBRE, a)))
            E.frase(c, t, C[k] + 0.1, [(l1, "g", 76, COR)] + ps(l2, "i", 74), 320, y, "left", 0.1)
    E.saida(c, t, C["s21"] - 0.1, resumo)
    if t < C["s21"]:
        return
    a1, b1, c1, d1, e1 = (C[f"s21.{k}"] for k in "abcde")
    E.frase(c, t, C["s21"] + 0.2, ps("na próxima aula", "i", 84), XE, 240, passo=0.14)
    E.frase(c, t, a1, ps("escolher a", "i", 92) + [("melhor opção", "g", 100, COR)], XE, 390, passo=0.12)
    x = XE
    for s, k in (("o preço por litro", b1), ("a compra mais barata", c1)):
        w = E.larg(s, "b", 56) + 56 * 1.1
        E.foco(c, t, k, 0.4, lambda a, s=s, x=x, w=w: E.pilula(c, s, x + w / 2, 540, 56, "b", a=a, cor=E.SOBRE))
        x += w + 30
    E.foco(c, t, d1, 0.5, lambda a: E.pilula(c, "Inscreva-se", 1440, 750, 76, estilo="g", a=a, cor=E.SOBRE))
    p = ease_io(prog(t, d1 + 0.3, 0.8))
    E.cursor(c, lerp(1770, 1570, p), lerp(990, 775, p), ep(t, d1 + 0.2, 0.4))
    E.frase(c, t, e1, [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 930, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, faixas=b_faixas, conta=b_conta, erro=b_erro, atalho=b_atalho,
              questao=b_questao, resposta=b_resposta, fim=b_fim)
