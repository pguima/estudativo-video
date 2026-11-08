"""Visual — Estudativo · MAT-LEI-007: praticando, da leitura à decisão (5 situações).

Linguagem da trilha Leitura de Problemas (as peças abaixo de "linguagem da trilha" servem a todas as aulas MAT-LEI):
- enunciado(): o problema num cartão branco com fio da cor da matéria. Os números são escritos em grotesca; a pergunta fica numa
  linha própria. marca = marca-texto da cor da matéria (dado útil), aponta = caixa pontilhada (dado em dúvida),
  risca = traço vermelho e número cinza (dado que não entra na conta).
- pessoa(): ícone simples para a quantidade que só existe inteira.
- barra(): o livro em 12 quadradinhos; tabela(): os palpites (corridas de táxi e aplicativo); horas(): o tempo cortado nas faixas.
Cada situação: o enunciado no cartão com o relógio de pausa; na resposta, o mesmo cartão marcado e a conta da trilha que resolve.
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
ARQUIVO_FINAL = "estudativo_MAT-LEI-007_praticando_da_leitura_a_decisao.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("questao1", "questao2", "questao3", "questao4", "questao5", "fim"))
BR = "#FFFFFF"
# as contas da aula, conferidas
assert 130 / 8 == 16.25 and 16 * 8 == 128 and 130 - 128 == 2 and 17 * 8 == 136
assert 12 // 3 == 4 and 12 - 4 == 8 and 8 // 4 == 2 and 8 - 2 == 6 and 180 // 6 == 30 and 12 * 30 == 360 and 360 // 2 == 180
assert 52 * 19 * 30 == 29640 and 50 * 20 == 1000 and 1000 * 30 == 30000
assert 2 * 6 == 12 and 3 * 4 == 12 and 12 + 12 == 24 and 5 * 6 == 30
assert 5 + 3 * 8 == 29 and 4 * 8 == 32 and 32 - 29 == 3 and 5 + 3 * 5 == 4 * 5 == 20
assert 5 + 3 * 4 == 17 > 4 * 4 == 16 and 5 + 3 * 6 == 23 < 4 * 6 == 24


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
            onde["q%d" % i] = (pos[0][4], pos[-1][5], base)
        for s, k, est, sz, x0, x1 in pos:
            if k:
                onde[k] = (x0, x1, base)
        if t < t0:
            continue
        # marca-texto atrás dos pedaços úteis
        for k, (x0, x1, b_) in list(onde.items()):
            kk = "q" if re.fullmatch(r"q\d+", k) else k
            if b_ != base or kk not in marca or t < marca[kk]:
                continue
            p = ease_io(prog(t, marca[kk], 0.45))
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




def situacao(c, t, t0, n, cor=None):
    E.foco(c, t, t0, 0.4, lambda a: E.pilula(c, f"situação {n}" if n < 5 else "última situação", XE + 150, 130, 50, "g", a=a, cor=E.SOBRE))


def questao(c, t, C, n, linhas, relogio):
    situacao(c, t, linhas[0][0] - 0.6, n)
    enunciado(c, t, XE, 210, 1260, linhas, size=60)
    E.relogio(c, t, relogio, 1660, 470, 150)


def horas(c, x, y, w, h, n, pinta, a=1.0, rot=(), size=60):
    """o tempo em n horas: pinta = [(i0, i1, cor, p)], rot = [(i0, i1, texto, alfa)]"""
    barra(c, x, y, w, h, n, [(k, 1) for k in range(1, n)], pinta, a, rot, size)


def caixa_opcao(c, cx, y, s, cor, a, w=380):
    M.rrect(c, cx - w / 2, y - 80, w, 120, 24, BR, a, shadow=True)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2, y - 80, w, 120), 24, 24), M.paint(cor, a, stroke=4 if cor != TINTA else 2))
    centro(c, s, cx, y + 4, 64, "g", cor, a)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    a1, b1 = C["s01.a"], C["s01.b"]
    E.foco(c, t, a1, 0.7, lambda a: E.bola(c, 1460, 470, 270 * ease_back(prog(t, a1, 0.7))), blur=0)
    E.foco(c, t, a1 + 0.3, 0.5, lambda a: centro(c, "5", 1460, 580, 300, "g", E.SOBRE, a))
    E.frase(c, t, a1 + 0.2, [("5 problemas", "g", 100, COR)], XE, 300, "left")
    E.frase(c, t, pal("s01", "enunciado"), ps("de enunciado comprido", "i", 80), XE, 420, "left", 0.1)
    E.frase(c, t, pal("s01", "criados"), ps("criados para esta aula", "i", 60, TINTA2), XE, 510, "left", 0.08)
    E.frase(c, t, b1, ps("em cada um:", "i", 72) + [("pause e resolva", "g", 76, COR)], XE, 680, "left", 0.1)
    E.frase(c, t, pal("s01", "antes"), ps("antes de ver a resposta", "i", 72), XE, 790, "left", 0.1)
    E.frase(c, t, pal("s01", "é"), ps("é assim que a leitura", "i", 66, TINTA2) + [("vira hábito", "g", 68, COR)], XE, 960, "left", 0.1)


# ---------------- ferramentas ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s02"] + 0.3, ps("as ferramentas", "i", 84) + [("da trilha", "g", 88, COR)], W / 2, 200, "center", 0.12)
    itens = (("s02.a", "pergunta primeiro"), ("s02.b", "palavras que mudam a conta"), ("s02.c", "barras e tabelas"),
             ("s02.d", "estimativa"), ("s02.e", "faixas"), ("s02.f", "comparar opções"))
    for i, (k, s) in enumerate(itens):
        col, lin = i % 2, i // 2
        x, y = 200 + col * 720, 380 + lin * 200
        E.foco(c, t, C[k], 0.5, lambda a, i=i, x=x, y=y, s=s: (E.bola(c, x, y - 22, 50, a=a), centro(c, str(i + 1), x, y, 58, "g", E.SOBRE, a),
                                                                E.escreve(c, s, x + 80, y, 58, "g", TINTA, a)))
    E.frase(c, t, pal("s02", "se"), ps("se alguma travar,", "i", 58, COR) + ps("procure a aula no canal", "i", 58), W / 2, 1000, "center", 0.1)


# ---------------- situação 1: dados úteis e no mínimo ----------------
def linhas1(C):
    a, b_, c_, d_, e_, f_ = (C[f"s03.{k}"] for k in "abcdef")
    return [(b_ - 0.5, "Uma festa terá [130 convidados|c]."), (c_ - 0.6, "O salão abre às [7 da noite|h]."), (d_ - 0.6, "Cada mesa tem [8 lugares|l],"),
            (pal("s03", "e", 2), "e o aluguel de uma mesa custa [R$ 25|r]."), (f_, "No mínimo, quantas mesas", True), (f_ + 0.8, "precisam ser alugadas?", True)]


def b_questao1(c, t, C, b):
    questao(c, t, C, 1, linhas1(C), C["s04.a"])


def b_resposta1(c, t, C, b):
    a5, b5, c5, d5, e5, f5, g5, h5 = (C[f"s05.{k}"] for k in "abcdefgh")
    tr = pal("s05", "risque")

    def cartao():
        situacao(c, t, C["s05"] - 9, 1)
        enunciado(c, t, XE, 210, 1260, linhas1(C), size=60, t_card=C["s05"] - 9, marca={"q": a5, "c": b5, "l": pal("s05", "oito")},
                  aponta={"h": c5, "r": pal("s05", "aluguel")}, risca={"h": tr, "r": tr + 0.15})
        E.foco(c, t, a5 + 0.2, 0.5, lambda a: E.pilula(c, "procuro: mesas", 1660, 330, 54, "g", a=a, cor=E.SOBRE))
    E.saida(c, t, d5 - 1.2, cartao)
    if t < d5 - 1.2:
        return
    E.frase(c, t, d5 - 1.0, ps("pela", "i", 76) + [("tabuada do 8", "g", 80, COR)], W / 2, 180, "center", 0.12)
    y = 440
    vx = E.reta(c, t, d5 - 0.8, 300, 1620, y, 120, 144, [120, 128, 136, 144], size=54, tm=[d5 - 0.6, d5, e5, d5 - 0.5])
    x130 = vx(130)
    E.foco(c, t, d5 - 0.4, 0.4, lambda a: (c.drawCircle(x130, y, 18, M.paint(E.COR, a)), centro(c, "130", x130, y - 50, 62, "g", COR, a)))
    E.foco(c, t, d5 + 0.3, 0.4, lambda a: centro(c, "16 mesas", vx(128), y + 170, 58, "g", TINTA, a))
    E.foco(c, t, pal("s05", "dois"), 0.4, lambda a: centro(c, "2 em pé", vx(128), y + 250, 54, "i", ERRADO, a))
    E.foco(c, t, e5 + 0.2, 0.4, lambda a: centro(c, "17 mesas", vx(136), y + 170, 58, "g", CERTO, a))
    bola_txt(c, t, f5, "17", 1640, 760, 80, 96, CERTO)
    E.frase(c, t, f5 + 0.2, [("mesas", "g", 56, CERTO)], 1640, 900, "center")
    E.frase(c, t, g5, [("130 ÷ 8 = 16,25:", "g", 60)] + ps("a regra do 5 desceria", "i", 58, TINTA2), XE, 870, "left", 0.1)
    E.linha(c, t, [("mas a pergunta diz", "i", 58, TINTA, h5 - 0.6), ("no mínimo:", "g", 60, COR, h5), ("ninguém sem lugar,", "i", 58, TINTA, pal("s05", "ninguém")),
                   ("sobe", "g", 64, CERTO, pal("s05", "sobe"))], XE, 990)


# ---------------- situação 2: do restante, com barra ----------------
def linhas2(C):
    a, b_, c_, d_, e_ = (C[f"s06.{k}"] for k in "abcde")
    return [(b_ - 0.7, "Uma pessoa leu [um terço|a] de um livro"), (b_ + 1.0, "no primeiro dia e [um quarto do restante|b]"),
            (c_ + 0.6, "no segundo. Ainda faltam [180 páginas|f]."), (e_, "Quantas páginas tem o livro?", True)]


def b_questao2(c, t, C, b):
    questao(c, t, C, 2, linhas2(C), C["s07.a"])


LX, LW, LH, LY = 260, 1400, 150, 360


def b_resposta2(c, t, C, b):
    a8, b8, c8 = C["s08.a"], C["s08.b"], C["s08.c"]
    a9, b9, c9, d9 = (C[f"s09.{k}"] for k in "abcd")
    cel = LW / 12
    xc = lambda i: LX + cel * i
    E.frase(c, t, C["s08"] + 0.3, ps("o livro numa barra de", "i", 70) + [("12 quadradinhos", "g", 74, COR)], W / 2, 140, "center", 0.1)
    E.frase(c, t, pal("s08", "porque"), ps("12 divide por 3 e depois por 4", "i", 54, TINTA2), W / 2, 220, "center", 0.08)
    cortes = [(k, ep(t, a8 + 0.04 * k, 0.4)) for k in range(1, 12)]
    pinta = [(0, 4, E.COR, ep(t, b8, 0.6)), (4, 6, TINTA, ep(t, c8, 0.6)), (6, 12, CERTO, ep(t, a9, 0.6))]
    rot = [(i, i + 1, "30", ep(t, b9 + 1.2 + 0.05 * i, 0.3)) for i in range(12)]
    E.foco(c, t, a8, 0.5, lambda a: barra(c, LX, LY, LW, LH, 12, cortes, pinta, a, rot, 54))
    chave_rot(c, t, b8 + 0.2, xc(0), xc(4), LY + LH + 20, "1º dia: f{1}{3}", E.COR, size=50)
    chave_rot(c, t, pal("s08", "restam") - 0.2, xc(4), xc(12), LY - 18, "restam 8", COR, cima=True, size=50)
    chave_rot(c, t, c8 + 0.2, xc(4), xc(6), LY + LH + 20, "2º dia: f{1}{4} de 8", TINTA, size=50, desce=95)
    chave_rot(c, t, a9, xc(6), xc(12), LY + LH + 20, "faltam 6 = 180 páginas", CERTO, size=50)
    fcen(c, t, b9, "180 ÷ 6 = 30", 620, 820, 90)
    fcen(c, t, c9, "12 × 30 = 360", 1300, 820, 90, CERTO)
    E.frase(c, t, c9 + 0.8, [("360 páginas", "g", 64, CERTO)], 1300, 920, "center")
    E.frase(c, t, d9, ps("faltam 6 de 12:", "i", 58) + [("metade", "g", 60, COR)] + ps("· 180 é metade de 360", "i", 58), W / 2, 1020, "center", 0.08)
    E.foco(c, t, pal("s09", "bateu"), 0.5, lambda a: E.selo(c, 1700, 990, 40, True, a))


# ---------------- situação 3: estimativa ----------------
def linhas3(C):
    a, b_, c_, d_, e_, f_, g_ = (C[f"s10.{k}"] for k in "abcdefg")
    return [(b_ - 0.7, "Uma loja vendeu [52 kits por dia|k],"), (c_ - 0.2, "a [R$ 19|p] cada, durante [30 dias|d]."),
            (pal("s10", "o"), "O valor recebido foi de aproximadamente:", True), (e_, "R$ 3.000, R$ 30.000 ou R$ 300.000?", True)]


def b_questao3(c, t, C, b):
    questao(c, t, C, 3, linhas3(C), C["s11.a"])


def b_resposta3(c, t, C, b):
    a2, b2, c2, d2, e2, f2, g2 = (C[f"s12.{k}"] for k in "abcdefg")
    E.foco(c, t, a2, 0.4, lambda a: E.pilula(c, "aproximadamente", W / 2, 140, 60, "g", a=a, cor=E.SOBRE))
    E.frase(c, t, pal("s12", "e"), ps("opções longe uma da outra:", "i", 58) + [("estimativa basta", "g", 60, COR)], W / 2, 255, "center", 0.08)
    for x, de, para, k, sobe in ((560, "52", "50", b2, False), (1300, "19", "20", c2, True)):
        E.foco(c, t, k, 0.45, lambda a, x=x, de=de, para=para, sobe=sobe: (E.escreve(c, de, x - 70 - E.larg(de, "g", 100), 390, 100, "g", TINTA2, a),
                                                                            centro(c, "→", x, 384, 80, "g", TINTA2, a), E.escreve(c, para, x + 70, 390, 100, "g", COR, a),
                                                                            E.pilula(c, "sobe" if sobe else "desce", x + 70 + E.larg(para, "g", 100) + 100, 357, 40, "g", a=a, cor=E.SOBRE)))
    fcen(c, t, d2, "50 × 20 = 1.000 por dia", W / 2, 560, 84)
    fcen(c, t, e2, "1.000 × 30 = 30.000", W / 2, 690, 96, COR)
    y = 900
    for i, s in enumerate(("R$ 3.000", "R$ 30.000", "R$ 300.000")):
        x = 460 + i * 500
        cor = TINTA
        if s == "R$ 30.000" and t >= e2 + 0.6:
            cor = CERTO
        if s == "R$ 3.000" and t >= g2 - 0.2:
            cor = ERRADO
        E.foco(c, t, a2 + 0.3 + 0.12 * i, 0.4, lambda a, x=x, s=s, cor=cor: caixa_opcao(c, x, y, s, cor, a, 420))
    E.frase(c, t, f2, ps("exata:", "i", 54, TINTA2) + [("29.640", "g", 58, TINTA2)] + ps("· perto", "i", 54, TINTA2), 960, 790, "center", 0.08)
    E.frase(c, t, pal("s12", "quem"), ps("perdeu um zero?", "i", 50, ERRADO) + [("10 vezes menos", "g", 52, ERRADO)], 460, 1030, "center", 0.08)


# ---------------- situação 4: faixas ----------------
def linhas4(C):
    a, b_, c_, d_ = (C[f"s13.{k}"] for k in "abcd")
    return [(b_ - 1.4, "Um estacionamento cobra [R$ 6 por hora|p]"), (b_ + 0.6, "nas duas primeiras horas"),
            (c_, "e [R$ 4 por hora|q] depois disso."), (d_, "Quanto paga quem fica 5 horas?", True)]


def b_questao4(c, t, C, b):
    questao(c, t, C, 4, linhas4(C), C["s14.a"])


def b_resposta4(c, t, C, b):
    a5, b5, c5, d5, e5, f5 = (C[f"s15.{k}"] for k in "abcdef")
    E.frase(c, t, pal("s15", "corte"), ps("corte o tempo", "i", 76) + [("nas faixas", "g", 80, COR)], W / 2, 180, "center", 0.12)
    x, w, y, h = 360, 1200, 300, 150
    cel = w / 5
    pinta = [(0, 2, E.mix(E.COR, BR, 0.3), ep(t, a5, 0.6)), (2, 5, E.mix(E.COR, "#000000", 0.3), ep(t, b5, 0.6))]
    rot = [(i, i + 1, f"{i + 1}h", 1.0) for i in range(5)]
    E.foco(c, t, pal("s15", "corte"), 0.5, lambda a: horas(c, x, y, w, h, 5, pinta, a, rot, 54))
    chave_rot(c, t, a5 + 0.2, x, x + cel * 2, y + h + 20, "R$ 6 por hora", E.COR, size=52)
    chave_rot(c, t, b5 + 0.2, x + cel * 2, x + w, y + h + 20, "R$ 4 por hora", TINTA, size=52)
    fcen(c, t, c5, "2 × 6 = 12", 560, 720, 90)
    fcen(c, t, d5, "3 × 4 = 12", 1300, 720, 90)
    E.foco(c, t, e5 - 0.6, 0.4, lambda a: E.escreve(c, "total:", 640, 870, 70, "i", TINTA, a))
    E.foco(c, t, e5, 0.5, lambda a: E.pilula(c, "R$ 24", 980, 845, 84, "g", fundo=CERTO, a=a))
    E.frase(c, t, pal("s15", "quem"), ps("tudo a R$ 6:", "i", 56, ERRADO) + [("5 × 6 = 30", "g", 58, ERRADO)], 1480, 870, "center", 0.08)
    E.frase(c, t, pal("s15", "preço"), ps("o preço da 1ª faixa só vale para as 2 primeiras horas", "i", 52, TINTA2), W / 2, 1000, "center", 0.05)


# ---------------- situação 5: táxi ou aplicativo ----------------
def linhas5(C):
    a, b_, c_, d_, e_ = (C[f"s16.{k}"] for k in "abcde")
    return [(b_ - 1.0, "Um táxi cobra [R$ 5 fixos|f] para começar,"), (c_ - 0.6, "mais [R$ 3 por quilômetro|t]."),
            (d_ - 1.6, "Um aplicativo cobra [R$ 4 por quilômetro|a],"), (pal("s16", "sem"), "sem valor fixo."),
            (e_, "Para 8 km, qual sai mais barato?", True)]


def b_questao5(c, t, C, b):
    questao(c, t, C, 5, linhas5(C), C["s17.a"])


def b_resposta5(c, t, C, b):
    a8, b8, c8 = C["s18.a"], C["s18.b"], C["s18.c"]
    a9, b9, c9, d9, e9 = (C[f"s19.{k}"] for k in "abcde")

    def oito():
        E.frase(c, t, C["s18"] + 0.3, ps("para", "i", 76) + [("8 km", "g", 80, COR)], W / 2, 190, "center", 0.12)
        E.foco(c, t, pal("s18", "táxi") - 0.2, 0.4, lambda a: E.escreve(c, "táxi:", 360, 400, 76, "i", TINTA, a))
        E.formula_em(c, t, a8, "5 + 3 × 8 = 29", 620, 400, 96, "g", CERTO if t >= c8 else TINTA)
        E.foco(c, t, pal("s18", "aplicativo") - 0.2, 0.4, lambda a: E.escreve(c, "aplicativo:", 360, 560, 76, "i", TINTA, a))
        E.formula_em(c, t, b8, "4 × 8 = 32", 760, 560, 96, "g", TINTA)
        E.frase(c, t, c8, [("o táxi ganha", "g", 80, CERTO)] + ps("por R$ 3", "i", 76), W / 2, 780, "center", 0.12)
    E.saida(c, t, C["s19"] - 0.1, oito)
    if t < C["s19"] - 0.1:
        return
    E.frase(c, t, C["s19"] + 0.3, ps("qualquer corrida, com", "i", 70) + [("uma tabela", "g", 74, COR)], XE, 160, "left", 0.1)
    linhas = [(a9 - 0.3, ["4 km", "R$ 17", ("R$ 16", CERTO)]), (b9, ["5 km", "R$ 20", "R$ 20"]), (b9 + 1.2, ["6 km", ("R$ 23", CERTO), "R$ 24"]),
              (b9 + 1.6, ["8 km", ("R$ 29", CERTO), "R$ 32"])]
    xs, ys = tabela(c, t, XE, 240, (240, 300, 340), ("corrida", "táxi", "aplicativo"), linhas, C["s19"] + 0.4, h=110, size=68, verde=(1, c9), cor_cab=None)
    xr = 1450
    E.frase(c, t, a9, ps("a cada km, o aplicativo fica", "i", 54) + [("R$ 1", "g", 58, COR)], xr, 330, "center", 0.07)
    E.frase(c, t, a9 + 0.6, ps("mais caro que o táxi", "i", 54), xr, 400, "center", 0.07)
    E.frase(c, t, b9, ps("os R$ 5 fixos se pagam em", "i", 54) + [("5 km", "g", 58, COR)], xr, 520, "center", 0.07)
    E.frase(c, t, c9, [("empate:", "g", 60, CERTO)] + ps("R$ 20 cada", "i", 58), xr, 600, "center", 0.08)
    E.frase(c, t, d9, ps("abaixo de 5 km:", "i", 64) + [("aplicativo", "g", 68, COR)], xr, 780, "center", 0.1)
    E.frase(c, t, e9, ps("acima de 5 km:", "i", 64) + [("táxi", "g", 68, COR)], xr, 880, "center", 0.1)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s20"] + 0.1, [("resumindo", "i", 88, COR)], W / 2, 170, "center")
        itens = (("s20.a", "pergunta", "primeiro"), ("s20.b", "desenhe", "ou monte a tabela"), ("s20.c", "estime", "antes de calcular"),
                 ("s20.d", "confira", "se a resposta faz sentido"))
        for i, (k, l1, l2) in enumerate(itens):
            y = 330 + i * 165
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 230, y - 28, 52, a=a), centro(c, str(i + 1), 230, y - 6, 60, "g", E.SOBRE, a)))
            E.frase(c, t, C[k] + 0.1, [(l1, "g", 74, COR)] + ps(l2, "i", 72), 320, y, "left", 0.1)
    E.saida(c, t, C["s21"] - 0.1, resumo)
    if t < C["s21"]:
        return
    a1, b1, c1, d1 = (C[f"s21.{k}"] for k in "abcd")
    E.frase(c, t, C["s21"] + 0.3, ps("trilha de leitura de problemas:", "i", 70) + [("completa", "g", 74, CERTO)], XE, 200, "left", 0.1)
    E.frase(c, t, pal("s21", "a", 2) - 0.2, ps("na próxima aula", "i", 84), XE, 340, passo=0.14)
    E.frase(c, t, a1, [("conjuntos", "g", 110, COR)], XE, 490)
    E.foco(c, t, pal("s21", "entre"), 0.5, lambda a: centro(c, "{ 1, 2, 3 }", 1040, 480, 96, "g", TINTA, a))
    E.frase(c, t, b1, ps("o que", "i", 70) + [("pertence", "g", 74, COR)] + ps("a ele", "i", 70), XE, 620, passo=0.1)
    E.foco(c, t, c1, 0.5, lambda a: E.pilula(c, "Inscreva-se", 1440, 750, 76, estilo="g", a=a, cor=E.SOBRE))
    p = ease_io(prog(t, c1 + 0.3, 0.8))
    E.cursor(c, lerp(1770, 1570, p), lerp(990, 775, p), ep(t, c1 + 0.2, 0.4))
    E.frase(c, t, d1, [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 930, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, questao1=b_questao1, resposta1=b_resposta1, questao2=b_questao2, resposta2=b_resposta2,
              questao3=b_questao3, resposta3=b_resposta3, questao4=b_questao4, resposta4=b_resposta4, questao5=b_questao5, resposta5=b_resposta5,
              fim=b_fim)
