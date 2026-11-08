"""Visual — Estudativo · MAT-CNT-015: probabilidade condicional.
Mesma linguagem da trilha Contagem e Probabilidade (MAT-CNT-001 a 014): igual_bola() com o resultado na esfera, bloco() em volta de um
grupo, dado() da MAT-CNT-011, pessoa() da MAT-CNT-005, linha() com contas e frações numa linha (MAT-CNT-013), ∩ desenhado por tx() (MAT-CON-002).
Peças desta aula:
- tabela2(): tabela de dupla entrada com totais (linhas × colunas), números que entram na fala, coluna ou linha marcada com bloco
  e véu de papel sobre o que sai da conta (a pista vira o novo total).
- pessoa() com saia para as mulheres e oculos() na cor da matéria.
Sem voz ainda: todo instante vem de C[...] (cenas e marcadores), nunca de segundos fixos."""
import math
from fractions import Fraction as Fr
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Contagem e Probabilidade")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-CNT-015_probabilidade_condicional.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("dado", "regra", "tabela", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
PAPEL = "#F3F3F0"
TURMA = [[6, 12], [10, 12]]  # homens / mulheres × óculos / sem óculos
assert [sum(l) for l in TURMA] == [18, 22] and sum(map(sum, TURMA)) == 40 and TURMA[0][0] + TURMA[1][0] == 16 and TURMA[0][1] + TURMA[1][1] == 24
assert Fr(10, 16) == Fr(5, 8) and Fr(5, 8) * 100 == Fr(125, 2) and Fr(10, 40) == Fr(1, 4) and Fr(10, 22) == Fr(5, 11) and Fr(1, 6) < Fr(1, 3)
EMP = [[18, 12], [8, 12]]  # manhã / tarde × ônibus / carro
assert sum(map(sum, EMP)) == 50 and 18 + 8 == 26 and Fr(18, 26) == Fr(9, 13) and round(9 / 13 * 100) == 69


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- ∩ desenhado (a fonte da casa não tem; como na MAT-CON-002) ----------------
def _cap(c, x, y, size, cor, a):
    sw = size * 0.15
    x0, x1 = x + size * 0.1 + sw / 2, x + size * 0.68 - sw / 2
    top, bot = y - size * 0.68 + sw / 2, y - size * 0.02 - sw / 2
    rr = (x1 - x0) / 2
    pa = skia.Path()
    pa.moveTo(x0, bot); pa.lineTo(x0, top + rr)
    pa.arcTo(skia.Rect.MakeLTRB(x0, top, x1, top + 2 * rr), 180, 180, False)
    pa.lineTo(x1, bot)
    p = M.paint(cor, a, stroke=sw)
    p.setStrokeCap(skia.Paint.kButt_Cap)
    c.drawPath(pa, p)


def tw(s, est, size):
    return sum(size * 0.78 if p == "∩" else E.larg(p, est, size) for p in _ped(s))


def _ped(s):
    out, cur = [], ""
    for ch in s:
        if ch == "∩":
            if cur:
                out.append(cur); cur = ""
            out.append(ch)
        else:
            cur += ch
    return out + ([cur] if cur else [])


def tx(c, s, x, y, size, est="g", cor=None, a=1.0, align="left"):
    if a <= 0:
        return
    cor = cor or TINTA
    w = tw(s, est, size)
    x = x - w / 2 if align == "center" else x - w if align == "right" else x
    for p in _ped(s):
        if p == "∩":
            _cap(c, x, y, size, cor, a)
            x += size * 0.78
        else:
            E.escreve(c, p, x, y, size, est, cor, a)
            x += E.larg(p, est, size)


# ---------------- peças da trilha (MAT-CNT-002 a 014) ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    """uma frase, palavra a palavra, no mesmo estilo"""
    return [(w, est, size, cor) for w in txt.split()]


def igual_bola(c, t, t0, x, y, txt, r=120, size=None, cor=None, escuro=False, t_igual=None):
    """'=' em x e o resultado numa esfera à direita; y = centro. Devolve o centro da esfera."""
    size = size or r * (0.72 if len(txt) <= 2 else 0.56 if len(txt) == 3 else 0.46 if len(txt) == 4 else 0.38)
    E.sinal(c, t, t0 - 0.2 if t_igual is None else t_igual, "=", x, y, r * 0.75, BR if escuro else TINTA)
    bx = x + r * 0.55 + r
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, bx, y, r, cor, a), centro(c, txt, bx, y + size * 0.36, size, "g", E.SOBRE, a)))
    return bx


def nota(c, t, t0, x, y, txt, size=46, cor=TINTA2, estilo="b"):
    E.foco(c, t, t0, 0.45, lambda a: centro(c, txt, x, y, size, estilo, cor, a))


def bloco(c, x0, x1, cy, h, a=1.0, cor=None, largura=7):
    """contorno do grupo: quem está dentro anda junto"""
    if a <= 0:
        return
    m = 26
    r = skia.RRect.MakeRectXY(skia.Rect.MakeLTRB(x0 - m, cy - h / 2 - m, x1 + m, cy + h / 2 + m), 34, 34)
    c.drawRRect(r, M.paint(cor or E.COR, 0.08 * a))
    c.drawRRect(r, M.paint(cor or E.COR, a, stroke=largura))


def larg_parte(p, size):
    return tw(p, "g", size) if isinstance(p, str) else max(tw(str(p[0]), "g", size), tw(str(p[1]), "g", size)) + size * 0.2


def linha(c, t, x, y, size, partes, align="left", gap=None):
    """conta numa linha: partes = [(texto ou (n, d), instante[, cor])]; y = altura da barra das frações. Devolve o x de cada parte e o fim"""
    gap = size * 0.28 if gap is None else gap
    ws = [larg_parte(p[0], size) for p in partes]
    tot = sum(ws) + gap * (len(partes) - 1)
    xx = x - tot / 2 if align == "center" else x - tot if align == "right" else x
    xs = []
    for (p, t0, *cor), w in zip(partes, ws):
        cor = cor[0] if cor else TINTA
        xs.append(xx)
        if isinstance(p, str):
            E.foco(c, t, t0, 0.45, lambda a, p=p, xx=xx, cor=cor: tx(c, p, xx, y + size * 0.34, size, "g", cor, a))
        else:
            E.fr(c, t, t0, p[0], p[1], xx + w / 2, y, size, cor)
        xx += w + gap
    return xs, xx - gap


def pil_esq(c, t, t0, x, y, txt, size=46, fundo=None, cor=BR):
    """pílula com a borda esquerda em x"""
    w = E.larg(txt, "g", size) + size * 1.1
    E.foco(c, t, t0, 0.45, lambda a: E.pilula(c, txt, x + w / 2, y, size, estilo="g", fundo=fundo or TINTA2, cor=cor, a=a))


PINTAS = {1: [(0, 0)], 2: [(-1, -1), (1, 1)], 3: [(-1, -1), (0, 0), (1, 1)], 4: [(-1, -1), (1, -1), (-1, 1), (1, 1)],
          5: [(-1, -1), (1, -1), (0, 0), (-1, 1), (1, 1)], 6: [(-1, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (1, 1)]}


def dado(c, cx, cy, s, n, a=1.0, cor=None, fundo=BR, borda=None, sombra=True):
    """face de dado com as pintas (MAT-CNT-011)"""
    if a <= 0:
        return
    r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - s / 2, cy - s / 2, s, s), s * 0.2, s * 0.2)
    if sombra:
        sh = skia.Paint(AntiAlias=True, Color=M.hexc("#000000", 0.12 * a))
        sh.setMaskFilter(skia.MaskFilter.MakeBlur(skia.kNormal_BlurStyle, 8))
        c.save(); c.translate(0, 6); c.drawRRect(r, sh); c.restore()
    c.drawRRect(r, M.paint(fundo, a))
    c.drawRRect(r, M.paint(borda or (TINTA if fundo == BR else M.mix(fundo, "#000000", 0.35)), a, stroke=max(3, s * 0.035)))
    k = s * 0.27
    for dx, dy in PINTAS[n]:
        c.drawCircle(cx + dx * k, cy + dy * k, s * 0.085, M.paint(cor or (TINTA if fundo == BR else BR), a))


def pessoa(c, cx, cy, h, cor, a=1.0, mulher=False):
    """boneco simples (MAT-CNT-005): cabeça e tronco; a mulher tem o tronco em saia. (cx, cy) = centro do tronco"""
    if a <= 0:
        return
    c.drawCircle(cx, cy - h * 0.36, h * 0.17, M.paint(cor, a))
    if mulher:
        pa = skia.Path()
        pa.moveTo(cx - h * 0.16, cy - h * 0.14); pa.lineTo(cx + h * 0.16, cy - h * 0.14)
        pa.lineTo(cx + h * 0.3, cy + h * 0.38); pa.lineTo(cx - h * 0.3, cy + h * 0.38); pa.close()
        c.drawPath(pa, M.paint(cor, a))
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - h * 0.17, cy - h * 0.15, h * 0.34, h * 0.2), h * 0.08, h * 0.08), M.paint(cor, a))
    else:
        r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - h * 0.25, cy - h * 0.14, h * 0.5, h * 0.52), h * 0.2, h * 0.2)
        c.drawRRect(r, M.paint(cor, a))


def oculos(c, cx, cy, s, cor=None, a=1.0):
    """óculos de largura ~2s centrados em (cx, cy)"""
    if a <= 0:
        return
    cor = cor or E.COR
    for dx in (-s * 0.5, s * 0.5):
        c.drawCircle(cx + dx, cy, s * 0.4, M.paint(BR, a))
        c.drawCircle(cx + dx, cy, s * 0.4, M.paint(cor, a, stroke=max(3, s * 0.16)))
    M.line(c, cx - s * 0.12, cy - s * 0.05, cx + s * 0.12, cy - s * 0.05, cor, a, max(3, s * 0.12))


# ---------------- peça desta aula: a tabela de dupla entrada ----------------
def _janelas(t, itens):
    """[(..., t0, t1)] → os que valem agora, com a opacidade de entrada e de saída"""
    out = []
    for it in itens or ():
        t0, t1 = it[-2], it[-1]
        q = ep(t, t0, 0.45) * (1 - (ep(t, t1, 0.4) if t1 is not None else 0))
        if q > 0:
            out.append((it[:-2], q))
    return out


def tabela2(c, t, x, y, w0, cw, ch, cabc, cabl, vals, tcab, tlin, tv, size=60, veu=None, col=None, lin=None, cel=None, totais=True):
    """tabela de dupla entrada. (x, y) = canto de cima à esquerda; w0 = largura da coluna dos nomes; cw/ch = célula.
    cabc/cabl = nomes das colunas e das linhas; vals[i][j] = texto (None = vazio); tcab[j], tlin[i] e tv[(i, j)] = instantes.
    totais = a última linha e a última coluna são de total (fundo cinza).
    veu = [(guarda(i, j), t0, t1)]: papel sobre as células fora da pista; col/lin = [(índice, t0, t1)]: bloco em volta;
    cel = [(i, j, cor, t0, t1)]: caixa em volta da célula. Devolve (i, j) → centro"""
    nl, nc = len(cabl), len(cabc)
    cx_ = lambda j: x + w0 + (j + 0.5) * cw
    cy_ = lambda i: y + ch + (i + 0.5) * ch
    tg = min(tcab + tlin)
    X1, Y1 = x + w0 + nc * cw, y + ch + nl * ch

    def grade(a):
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeLTRB(x + w0, y + ch, X1, Y1), 14, 14), M.paint(BR, 0.9 * a))
        if totais:
            c.drawRect(skia.Rect.MakeLTRB(x + w0 + (nc - 1) * cw, y + ch, X1, Y1), M.paint("#E4E4EC", a))
            c.drawRect(skia.Rect.MakeLTRB(x + w0, y + ch + (nl - 1) * ch, X1, Y1), M.paint("#E4E4EC", a))
        for j in range(nc + 1):
            M.line(c, x + w0 + j * cw, y + ch, x + w0 + j * cw, Y1, TINTA2, a * 0.5, 2.5)
        for i in range(nl + 1):
            M.line(c, x + w0, y + ch + i * ch, X1, y + ch + i * ch, TINTA2, a * 0.5, 2.5)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeLTRB(x + w0, y + ch, X1, Y1), 14, 14), M.paint(TINTA, a, stroke=4))
    E.foco(c, t, tg, 0.5, grade)
    for j, nome in enumerate(cabc):
        E.foco(c, t, tcab[j], 0.4, lambda a, j=j, nome=nome: centro(c, nome, cx_(j), y + ch * 0.68, size * 0.66, "b", TINTA2, a))
    for i, nome in enumerate(cabl):
        E.foco(c, t, tlin[i], 0.4, lambda a, i=i, nome=nome: E.escreve(c, nome, x, cy_(i) + size * 0.25, size * 0.72, "b", TINTA2, a))
    for (i, j), t0 in tv.items():
        v = vals[i][j]
        if v is not None:
            tot = totais and (i == nl - 1 or j == nc - 1)
            E.foco(c, t, t0, 0.4, lambda a, i=i, j=j, v=str(v), tot=tot: centro(c, v, cx_(j), cy_(i) + size * 0.36, size, "g", TINTA2 if tot else TINTA, a))
    for (guarda,), q in _janelas(t, veu):
        for i in range(nl):
            for j in range(nc):
                if not guarda(i, j):
                    c.drawRect(skia.Rect.MakeXYWH(cx_(j) - cw / 2 + 2, cy_(i) - ch / 2 + 2, cw - 4, ch - 4), M.paint(PAPEL, 0.85 * q))
    for (j,), q in _janelas(t, col):
        bloco(c, cx_(j) - cw / 2 + 14, cx_(j) + cw / 2 - 14, (y + Y1) / 2, Y1 - y - 28, q, largura=6)
    for (i,), q in _janelas(t, lin):
        bloco(c, x + 14, X1 - 14, cy_(i), ch - 28, q, largura=6)
    for (i, j, cor), q in _janelas(t, cel):
        E.caixa_pontilhada(c, cx_(j) - cw / 2 + 8, cy_(i) - ch / 2 + 8, cw - 16, ch - 16, q, cor, 1.0)
    return lambda i, j: (cx_(j), cy_(i))


# a turma: sempre no mesmo lugar, à esquerda
TX, TY, TW0, TCW, TCH = 120, 240, 260, 230, 112
CABC = ["óculos", "sem óculos", "total"]
CABL = ["homens", "mulheres", "total"]
VALS = [[6, 12, 18], [10, 12, 22], [16, None, 40]]


def turma(c, t, t0, **kw):
    """a tabela da turma inteira já montada (para os blocos depois de 'tabela')"""
    tv = {(i, j): t0 + 0.02 * (i + j) for i in range(3) for j in range(3)}
    return tabela2(c, t, TX, TY, TW0, TCW, TCH, CABC, CABL, VALS, [t0] * 3, [t0] * 3, tv, **kw)


# ---------------- gancho ----------------
GENTE = [(False, False), (True, True), (False, False), (True, False), (False, True), (True, True), (False, False), (True, False), (True, True), (False, False)]


def b_gancho(c, t, C, b):
    def pergunta():
        E.frase(c, t, C["s01.a"], [("1", "g", 84, COR), ("pessoa", "i", 80), ("é", "i", 80), ("sorteada", "g", 84)], W / 2, 180, "center")
        fora = ep(t, C["s01.b"] + 0.8, 0.6)
        for k, (mulher, ocl) in enumerate(GENTE):
            x = 290 + k * 150
            al = 1 - 0.75 * fora if not ocl else 1.0
            E.foco(c, t, C["s01.a"] + 0.4 + 0.06 * k, 0.4, lambda a, x=x, mulher=mulher, al=al: pessoa(c, x, 400, 170, TINTA, a * al, mulher))
            if ocl:
                E.foco(c, t, C["s01.b"] + 0.3 + 0.1 * k, 0.4, lambda a, x=x: oculos(c, x, 339, 34, a=a), sobe=-12)
        E.foco(c, t, C["s01.b"], 0.45, lambda a: E.pilula(c, "pista: usa óculos", W / 2, 620, 54, estilo="g", a=a))
        E.frase(c, t, C["s01.c"], [("muda", "i", 72), ("a", "i", 72), ("chance", "i", 72), ("de", "i", 72), ("ser", "i", 72), ("mulher?", "g", 80, COR)],
                W / 2, 800, "center", passo=0.12)
        E.foco(c, t, lerp(C["s01.c"], C["s01.d"], 0.7), 0.45, lambda a: E.escreve(c, "muda!", 1500, 805, 80, "g", CERTO, a))
        E.foco(c, t, C["s01.d"], 0.45, lambda a: E.pilula(c, "ignorar a pista: erro na conta", W / 2, 950, 48, estilo="g", fundo=ERRADO, a=a))
    E.saida(c, t, C["s02"] - 0.1, pergunta)

    if t >= C["s02"]:
        E.foco(c, t, C["s02.c"] - 0.2, 0.7, lambda a: E.bola(c, 1480, 520, 300 * ease_back(prog(t, C["s02.c"] - 0.2, 0.7))), blur=0)
        E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 96), XE, 300)
        E.frase(c, t, C["s02.a"] + 0.9, [("a", "i", 100), ("pista", "g", 120, COR), ("encolhe", "i", 100)], XE, 450)
        E.frase(c, t, C["s02.a"] + 1.4, [("o", "i", 100), ("espaço", "i", 100), ("amostral", "g", 110)], XE, 600)
        pil_esq(c, t, C["s02.b"], XE, 760, "numa tabela", 50)
        E.foco(c, t, C["s02.c"] + 0.2, 0.5, lambda a: (E.centro(c, "+ atalho", 1480, 490, 88, "g", BR, a),
                                                      E.centro(c, "de prova", 1480, 600, 88, "g", BR, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"] + 0.1, [("você", "i", 84), ("vai", "i", 84), ("usar", "i", 84), ("duas", "g", 88, COR), ("coisas", "i", 84)], W / 2, 190, "center")
    for k, x, titulo in (("s03.b", 200, "probabilidade"), ("s03.c", 1000, "espaço amostral")):
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, 290, 720, 620, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(titulo, "g", 64, COR)], x + 360, 400, "center")
    E.foco(c, t, C["s03.b"] + 0.4, 0.45, lambda a: E.escreve(c, "P =", 250, 640, 96, "g", TINTA, a))
    E.fr(c, t, C["s03.b"] + 0.7, "favoráveis", "possíveis", 640, 610, 66, COR)
    for i in range(6):
        E.foco(c, t, C["s03.c"] + 0.5 + 0.08 * i, 0.4, lambda a, i=i: dado(c, 1135 + i * 90, 580, 72, i + 1, a))
    E.foco(c, t, C["s03.c"] + 1.2, 0.45, lambda a: E.centro(c, "Ω = {1, 2, 3, 4, 5, 6}", 1360, 730, 60, "g", TINTA, a))
    nota(c, t, C["s03.c"] + 1.6, 1360, 830, "todos os resultados possíveis", 46, TINTA2, "i")
    E.frase(c, t, lerp(C["s03.c"], C["s03.end"], 0.8), ps("faltou alguma? procure no canal", "i", 52, TINTA2), W / 2, 1010, "center", passo=0.1)


# ---------------- dado ----------------
def b_dado(c, t, C, b):
    E.frase(c, t, C["s04"] + 0.1, [("um", "i", 76), ("dado", "g", 80)], W / 2, 150, "center")
    sai = ep(t, C["s05.a"], 0.5)
    for i in range(6):
        n = i + 1
        x = 460 + i * 200
        par = n % 2 == 0
        al = 1.0 if par else 1 - 0.75 * sai
        cor = COR if n == 6 and t >= C["s04.a"] else TINTA
        E.foco(c, t, C["s04"] + 0.3 + 0.06 * i, 0.4, lambda a, x=x, n=n, al=al, cor=cor: dado(c, x, 400, 150, n, a * al, cor))
        if not par and t >= C["s05.a"]:
            E.risco(c, x - 70, 470, x + 70, 330, t, C["s05.a"] + 0.1 * i, largura=9)
    xs, xf = linha(c, t, 220, 720, 110, [("P(6) =", C["s04.b"]), ((1, 6), C["s04.b"] + 0.2)])
    E.foco(c, t, C["s04.c"], 0.45, lambda a: E.pilula(c, "pista: saiu par", W / 2, 250, 50, estilo="g", fundo=TINTA2, a=a))
    tb = [C["s05.b"], lerp(C["s05.b"], C["s05.c"], 0.15), lerp(C["s05.b"], C["s05.c"], 0.3)]
    for k, n in enumerate((2, 4, 6)):
        x = 460 + (n - 1) * 200
        E.foco(c, t, tb[k], 0.4, lambda a, x=x: E.caixa_pontilhada(c, x - 92, 308, 184, 184, a, E.COR, 1.0))
    E.foco(c, t, C["s05.c"], 0.45, lambda a: E.escreve(c, "Ω encolheu: {2, 4, 6}", 220, 900, 64, "g", COR, a))
    E.saida(c, t, C["s05.d"] - 0.1, lambda: E.foco(c, t, lerp(C["s04.c"], C["s04.end"], 0.55), 0.45,
            lambda a: E.escreve(c, "e agora, chance de 6?", 1060, 745, 64, "i", COR, a)))
    xs2, xf2 = linha(c, t, 1060, 720, 110, [("P(6 | par) =", C["s05.d"]), ((1, 3), C["s05.d"] + 0.2, CERTO)])
    E.foco(c, t, C["s05.d"] + 0.6, 0.4, lambda a: E.selo(c, xf2 + 70, 720, 44, True, a))


# ---------------- regra ----------------
def b_regra(c, t, C, b):
    def ideia():
        E.frase(c, t, C["s06.a"], [("probabilidade", "g", 84, COR), ("condicional", "g", 84, COR)], W / 2, 220, "center", passo=0.15)
        E.frase(c, t, C["s06.b"], ps("a chance de um evento, sabendo que outro já aconteceu", "i", 56, TINTA2), W / 2, 340, "center", passo=0.08)
        E.foco(c, t, C["s06.c"], 0.5, lambda a: E.pilula(c, "a pista vira o novo total", W / 2, 560, 72, estilo="g", a=a))
        E.frase(c, t, C["s06.d"], [("o", "i", 60), ("que", "i", 60), ("está", "i", 60), ("fora", "g", 64, ERRADO), ("da", "i", 60), ("pista", "i", 60),
                                   ("sai", "g", 64, ERRADO), ("da", "i", 60), ("conta", "i", 60)], W / 2, 780, "center", passo=0.1)
    E.saida(c, t, C["s07"] - 0.1, ideia)
    if t < C["s07"]:
        return
    E.foco(c, t, C["s07.a"], 0.5, lambda a: E.centro(c, "P(A | B)", W / 2, 300, 150, "g", TINTA, a))
    wb = E.larg("P(A | B)", "g", 150)
    xbar = W / 2 - wb / 2 + E.larg("P(A ", "g", 150) + E.larg("|", "g", 150) / 2
    if t >= C["s07.b"]:
        p = ep(t, C["s07.b"], 0.4)
        M.arrow(c, xbar, 420, xbar, 330, E.COR, p, 5, 18, p)
    E.foco(c, t, C["s07.b"] + 0.2, 0.45, lambda a: E.pilula(c, "| = dado que, sabendo que", xbar, 470, 44, estilo="g", a=a))
    y = 760
    E.foco(c, t, C["s07.c"], 0.45, lambda a: E.escreve(c, "P(A | B) =", 220, y + 34, 100, "g", TINTA, a))
    fx = 220 + E.larg("P(A | B) =", "g", 100) + 40
    wf = tw("n(A ∩ B)", "g", 96) + 30
    E.foco(c, t, C["s07.c"], 0.45, lambda a: c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(fx, y - 5, wf, 10), 5, 5), M.paint(TINTA, a)))
    E.foco(c, t, C["s07.c"] + 0.2, 0.45, lambda a: tx(c, "n(B)", fx + wf / 2, y + 100, 96, "g", COR, a, "center"))
    E.foco(c, t, C["s07.d"], 0.45, lambda a: tx(c, "n(A ∩ B)", fx + wf / 2, y - 30, 96, "g", TINTA, a, "center"))
    E.foco(c, t, C["s07.c"] + 0.5, 0.45, lambda a: E.escreve(c, "casos de B: a pista", fx + wf + 60, y + 80, 50, "b", COR, a))
    E.foco(c, t, C["s07.d"] + 0.5, 0.45, lambda a: E.escreve(c, "de A que estão em B", fx + wf + 60, y - 50, 50, "b", TINTA2, a))


# ---------------- tabela ----------------
def b_tabela(c, t, C, b):
    E.frase(c, t, C["s08.a"], [("turma", "i", 76), ("de", "i", 76), ("40", "g", 84, COR), ("alunos", "i", 76)], TX + 470, 160, "center")
    tb, tc_ = C["s08.b"], C["s08.c"]
    tv = {(2, 2): C["s08.a"] + 0.4,
          (0, 0): tb + 1.0, (0, 1): tb + 1.8, (0, 2): tb + 0.3,
          (1, 0): tc_ + 1.0, (1, 1): tc_ + 1.8, (1, 2): tc_ + 0.3,
          (2, 0): C["s09.c"] + 1.2}
    veu, col, lin, cel = [], [], [], []
    lin += [(0, C["s09.a"], C["s09.a"] + 1.2), (1, C["s09.a"] + 1.2, C["s09.b"])]
    col += [(0, C["s09.c"], C["s10"]), (0, C["s10.c"], None)]
    veu += [(lambda i, j: j == 0, C["s10.c"], None)]
    cel += [(1, 0, CERTO, C["s10.d"], None)]
    if C["s09.b"] <= t < C["s09.c"]:
        col += [(0, C["s09.b"], C["s09.b"] + 1.0), (1, C["s09.b"] + 1.0, C["s09.c"])]
    tabela2(c, t, TX, TY, TW0, TCW, TCH, CABC, CABL, VALS, [tb - 0.3, tb - 0.1, tb + 0.1], [tb, tc_, C["s08.a"] + 0.2], tv,
            veu=veu, col=col, lin=lin, cel=cel)
    XP = 1170

    def montar():
        E.formula_em(c, t, tb + 2.2, "homens: 6 + 12 = 18", XP, 380, 60, "g", TINTA)
        E.formula_em(c, t, tc_ + 2.2, "mulheres: 10 + 12 = 22", XP, 500, 60, "g", TINTA)
        E.foco(c, t, C["s09.a"], 0.45, lambda a: E.escreve(c, "linha: homens ou mulheres", XP, 640, 48, "i", TINTA2, a))
        E.foco(c, t, C["s09.b"], 0.45, lambda a: E.escreve(c, "coluna: com ou sem óculos", XP, 720, 48, "i", TINTA2, a))
        E.formula_em(c, t, C["s09.c"] + 0.4, "de óculos: 6 + 10 = 16", XP, 860, 60, "g", COR)
    E.saida(c, t, C["s10"] - 0.1, montar)
    if C["s10"] <= t:
        def pista():
            E.foco(c, t, C["s10.a"], 0.45, lambda a: E.escreve(c, "P(mulher | óculos)?", XP, 360, 64, "g", TINTA, a))
            E.foco(c, t, C["s10.b"], 0.45, lambda a: E.pilula(c, "pista: usa óculos", XP + 240, 470, 46, estilo="g", fundo=TINTA2, a=a))
            E.foco(c, t, C["s10.c"], 0.45, lambda a: (E.escreve(c, "novo total:", XP, 620, 56, "i", TINTA, a), E.escreve(c, "16", XP + 330, 622, 72, "g", COR, a)))
            E.foco(c, t, C["s10.d"], 0.45, lambda a: (E.escreve(c, "mulheres:", XP, 740, 56, "i", TINTA, a), E.escreve(c, "10", XP + 300, 742, 72, "g", CERTO, a)))
        E.saida(c, t, C["s11"] - 0.1, pista)
    if t < C["s11"]:
        return
    E.foco(c, t, C["s11"] + 0.1, 0.45, lambda a: E.escreve(c, "P(mulher | óculos)", XP, 360, 60, "g", TINTA, a))
    xs, xf = linha(c, t, XP, 560, 100, [("=", C["s11.a"] - 0.2), ((10, 16), C["s11.a"], CERTO), ("=", C["s11.b"] - 0.2), ((5, 8), C["s11.b"], CERTO)])
    nota(c, t, C["s11.b"] + 0.2, (xs[1] + xs[3]) / 2 + 60, 700, "÷ 2", 44, TINTA2)
    igual_bola(c, t, C["s11.c"], XP + 20, 860, "62,5%", r=110, cor=CERTO)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    XP = 1170
    t0 = C["s12"]
    veu = [(lambda i, j: (i, j) in ((1, 0), (2, 2)), C["s12.b"], C["s12.d"]), (lambda i, j: j == 0, C["s12.d"], C["s13"]),
           (lambda i, j: i == 1, C["s13.b"], None)]
    col = [(0, C["s12.d"], C["s13"])]
    lin = [(1, C["s13.b"], None)]
    cel = [(1, 0, ERRADO, C["s12.b"], C["s12.d"]), (2, 2, ERRADO, C["s12.b"], C["s12.d"]), (1, 0, CERTO, C["s12.d"], C["s13"]),
           (1, 0, CERTO, C["s13.c"], None), (1, 2, COR, C["s13.b"], None)]
    turma(c, t, t0, veu=veu, col=col, lin=lin, cel=cel)

    def turma_toda():
        E.foco(c, t, C["s12.a"], 0.45, lambda a: E.pilula(c, "dividir pela turma inteira", XP + 300, 300, 46, estilo="g", fundo=ERRADO, a=a))
        xs, xf = linha(c, t, XP, 480, 96, [((10, 40), C["s12.b"], ERRADO), ("=", C["s12.b"] + 0.5), ((1, 4), C["s12.b"] + 0.7, ERRADO)])
        if t >= C["s12.d"]:
            E.risco(c, XP - 10, 580, xf + 10, 380, t, C["s12.d"], largura=11)
        nota(c, t, C["s12.c"], XP + 300, 660, "é mulher e usa óculos,", 46, TINTA2)
        nota(c, t, C["s12.c"] + 0.8, XP + 300, 720, "sem pista nenhuma", 46, TINTA2)
        xs2, xf2 = linha(c, t, XP, 880, 70, [("com a pista:", C["s12.d"] + 0.2), ((10, 16), C["s12.d"] + 0.6, CERTO)])
    E.saida(c, t, C["s13"] - 0.1, turma_toda)
    if t < C["s13"]:
        return
    E.frase(c, t, C["s13"] + 0.1, [("a", "i", 64), ("ordem", "g", 70, COR), ("importa", "i", 64)], XP, 280, passo=0.12)
    E.foco(c, t, C["s13.a"], 0.45, lambda a: E.escreve(c, "P(óculos | mulher)?", XP, 400, 64, "g", TINTA, a))
    E.foco(c, t, C["s13.b"], 0.45, lambda a: (E.escreve(c, "novo total:", XP, 520, 56, "i", TINTA, a), E.escreve(c, "22", XP + 330, 522, 72, "g", COR, a)))
    xs, xf = linha(c, t, XP, 680, 96, [((10, 22), C["s13.c"], CERTO), ("=", C["s13.c"] + 0.5), ((5, 11), C["s13.c"] + 0.7, CERTO)])
    E.foco(c, t, C["s13.d"], 0.5, lambda a: E.pilula(c, "outra pista, outra resposta", XP + 300, 900, 48, estilo="g", a=a))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def palavras():
        E.frase(c, t, C["s14.a"], [("ache", "i", 76, CLARO), ("a", "i", 76, CLARO), ("pista", "g", 84, BR), ("e", "i", 76, CLARO), ("cubra", "g", 84, BR),
                                   ("o", "i", 76, CLARO), ("resto", "i", 76, CLARO)], W / 2, 210, "center", passo=0.12)
        for k, y, txt in (("s14.b", 400, "sabendo que"), ("s14.c", 540, "dado que"), ("s14.d", 680, "entre os que")):
            E.foco(c, t, C[k], 0.45, lambda a, y=y, txt=txt: E.pilula(c, txt, 560, y, 58, estilo="g", fundo=E.COR, a=a))
        if t >= C["s14.d"] + 0.5:
            p = ep(t, C["s14.d"] + 0.5, 0.5)
            M.arrow(c, 900, 540, 1060, 540, BR, p, 6, 22, p)
        E.frase(c, t, C["s14.d"] + 0.7, [("o", "i", 70, CLARO), ("que", "i", 70, CLARO), ("vem", "i", 70, CLARO), ("depois", "i", 70, CLARO)], 1110, 480, passo=0.1)
        E.frase(c, t, C["s14.d"] + 1.2, [("é", "i", 70, CLARO), ("o", "i", 70, CLARO), ("novo", "g", 78, BR), ("total", "g", 78, BR)], 1110, 590, passo=0.1)
        nota(c, t, lerp(C["s14.d"], C["s14.end"], 0.75), W / 2, 900, "use só aquela linha ou coluna", 56, CLARO, "i")
    E.saida(c, t, C["s15"] - 0.1, palavras)
    if t < C["s15"]:
        return
    E.frase(c, t, C["s15.a"], [("a", "i", 72, CLARO), ("pista", "g", 80, BR), ("elimina", "i", 72, CLARO), ("todo", "i", 72, CLARO), ("o", "i", 72, CLARO),
                               ("resto", "g", 80, BR)], W / 2, 220, "center", passo=0.12)
    E.foco(c, t, C["s15.b"], 0.5, lambda a: E.pilula(c, "às vezes a pista vem escondida", W / 2, 400, 52, estilo="g", fundo=ERRADO, a=a))
    E.frase(c, t, C["s15.c"], [("“um", "i", 76, CLARO), ("aluno", "i", 76, CLARO), ("de", "g", 82, BR), ("óculos", "g", 82, BR), ("foi", "i", 76, CLARO),
                               ("sorteado”", "i", 76, CLARO)], W / 2, 600, "center", passo=0.12)
    if t >= C["s15.c"] + 1.0:
        x0 = W / 2 - E.larg("“um aluno de óculos foi sorteado”", "i", 76) / 2 + E.larg("“um aluno ", "i", 76)
        E.risco(c, x0 - 10, 625, x0 + E.larg("de óculos", "g", 82) + 30, 625, t, C["s15.c"] + 1.0, E.COR, 8)
    E.frase(c, t, C["s15.d"], [("quem", "i", 70, CLARO), ("ainda", "i", 70, CLARO), ("pode", "i", 70, CLARO), ("ter", "i", 70, CLARO), ("sido", "i", 70, CLARO),
                               ("sorteado?", "g", 78, BR)], W / 2, 820, "center", passo=0.12)


# ---------------- questão ----------------
QX, QY, QW0, QCW, QCH = 150, 330, 230, 200, 112


def b_questao(c, t, C, b):
    E.frase(c, t, C["s16"] + 0.1, [("hora", "i", 72, COR), ("de", "i", 72, COR), ("testar", "i", 72, COR)], XE, 160)
    E.frase(c, t, C["s16.a"], [("empresa:", "i", 60), ("50", "g", 66, COR), ("funcionários", "i", 60)], XE, 260, passo=0.1)
    tb, tc_ = C["s16.b"], C["s16.c"]
    tv = {(0, 0): tb + 1.4, (0, 1): tb + 2.6, (1, 0): tc_ + 1.4, (1, 1): tc_ + 2.6}
    tabela2(c, t, QX, QY, QW0, QCW, QCH, ["ônibus", "carro"], ["manhã", "tarde"], EMP, [tb + 1.2, tb + 2.4], [tb, tc_], tv, totais=False)
    E.frase(c, t, C["s16.d"] - 2.2, ps("sorteado alguém que vai de ônibus:", "i", 54), XE, 780, passo=0.08)
    E.frase(c, t, C["s16.d"], [("chance", "i", 64), ("de", "i", 64), ("ser", "i", 64), ("da", "i", 64), ("manhã?", "g", 72, COR)], XE, 880, passo=0.12)
    E.relogio(c, t, C["s17.a"], 1500, 560, 190)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    t0 = C["s18"]
    vals = [[18, 12, None], [8, 12, None], [26, None, 50]]
    tv = {(0, 0): t0, (0, 1): t0, (1, 0): t0, (1, 1): t0, (2, 2): t0, (2, 0): C["s18.b"] + 1.2}
    tabela2(c, t, TX, TY, TW0, TCW, TCH, ["ônibus", "carro", "total"], ["manhã", "tarde", "total"], vals, [t0] * 3, [t0] * 3, tv,
            veu=[(lambda i, j: j == 0, C["s18.b"], None)], col=[(0, C["s18.a"], None)], cel=[(0, 0, CERTO, C["s18.c"], None)])
    XP = 1170
    E.foco(c, t, C["s18.a"], 0.45, lambda a: E.pilula(c, "pista escondida: vai de ônibus", XP + 300, 300, 44, estilo="g", fundo=TINTA2, a=a))
    E.formula_em(c, t, C["s18.b"], "novo total: 18 + 8 = 26", XP, 440, 56, "g", COR)
    E.formula_em(c, t, C["s18.c"], "da manhã: 18", XP, 540, 56, "g", CERTO)
    xs, xf = linha(c, t, XP, 720, 90, [("P =", C["s18.d"]), ((18, 26), C["s18.d"] + 0.2), ("=", C["s18.e"] - 0.2)])
    E.resultado(c, t, C["s18.e"], 9, 13, xf + 120, 720, 84, 105, CERTO)
    nota(c, t, C["s18.e"] + 1.0, XP + 300, 920, "quase 70%", 50, TINTA2, "i")


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s19"], [("resumindo", "i", 92, COR)], W / 2, 190, "center")
        E.foco(c, t, C["s19.a"], 0.5, lambda a: E.pilula(c, "a pista vira o novo total", W / 2, 380, 66, estilo="g", a=a))
        E.frase(c, t, C["s19.b"], ps("em cima: só quem cumpre as duas condições", "i", 60, TINTA2), W / 2, 560, "center", passo=0.08)
        y = 780
        E.foco(c, t, C["s19.b"] + 1.0, 0.45, lambda a: E.escreve(c, "P(A | B) =", 520, y + 30, 90, "g", TINTA, a))
        fx = 520 + E.larg("P(A | B) =", "g", 90) + 36
        wf = tw("n(A ∩ B)", "g", 84) + 30
        E.foco(c, t, C["s19.b"] + 1.0, 0.45, lambda a: (c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(fx, y - 5, wf, 10), 5, 5), M.paint(TINTA, a)),
                                                       tx(c, "n(A ∩ B)", fx + wf / 2, y - 26, 84, "g", TINTA, a, "center"),
                                                       tx(c, "n(B)", fx + wf / 2, y + 90, 84, "g", COR, a, "center")))
    E.saida(c, t, C["s20"] - 0.1, resumo)
    if t < C["s20"]:
        return
    E.frase(c, t, C["s20"] + 0.1, [("e", "i", 76), ("se", "i", 76), ("a", "i", 76), ("pista", "g", 84, COR), ("não", "i", 76), ("muda", "i", 76), ("nada?", "g", 84)],
            XE, 300, passo=0.12)
    E.foco(c, t, C["s20.a"] + 0.6, 0.45, lambda a: E.moeda(c, XE + 90, 500, 80, "Ca", a))
    E.foco(c, t, C["s20.a"] + 1.4, 0.45, lambda a: dado(c, XE + 300, 500, 150, 6, a, COR))
    E.frase(c, t, C["s20.b"], [("próxima", "i", 64), ("aula:", "i", 64), ("eventos", "g", 70, COR), ("independentes", "g", 70, COR)], XE, 700, passo=0.1)
    E.foco(c, t, C["s20.b"] + 1.4, 0.45, lambda a: E.escreve(c, "multiplique as chances", XE, 800, 60, "i", TINTA2, a))
    E.foco(c, t, C["s20.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 470, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s20.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1830, 1650, p), lerp(760, 495, p), ep(t, C["s20.c"] + 0.2, 0.4))
    E.frase(c, t, C["s20.d"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 980, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, dado=b_dado, regra=b_regra, tabela=b_tabela, erro=b_erro, atalho=b_atalho,
              questao=b_questao, resposta=b_resposta, fim=b_fim)
