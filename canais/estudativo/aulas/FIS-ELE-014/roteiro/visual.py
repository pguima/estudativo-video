"""Visual — Estudativo · FIS-ELE-014: curto-circuito, fusível e choque.

Segue a linguagem visual da Física (cabeçalho do visual.py da FIS-CIN-001) e a da Eletricidade (cabeçalho do visual.py da
FIS-ELE-001: circuito com F.fio, F.pilha, F.resistor, F.lampada, F.chave; corrente = setinhas laranja; Ω e = só na
fonte pesada).
Nesta aula: o FIO DO CURTO é sempre vermelho (ERRADO), desenhado por fora do resistor (peça `curto`); o resistor em curto
fica apagado (cinza claro). O disjuntor é F.chave no fio de cima, antes dos aparelhos, e abre no instante da fala.
O choque usa a peça `pessoa` (corpo em tinta, caminho da corrente em laranja) e o `passaro` no fio.
Todo instante vem de C[...] (marcadores do roteiro)."""
import math

import editorial as E
import fisica as F
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Física", "Eletricidade")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_FIS-ELE-014_curto_circuito_fusivel_e_choque.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("curto", "casa", "choque", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
APAGADO = "#C9C6BF"

# todas as contas da aula
assert 4 + 2 == 6 and 12 / 6 == 2 and 12 / 2 == 6 == 3 * 2
assert 127 / 1000 == 0.127 and round(127 / 100000, 5) == 0.00127 and 0.127 * 1000 > 100 > 10 and 0.00127 * 1000 < 10
assert 3 * 4 == 12 and 12 / 12 == 1 and 2 * 4 == 8 and 12 / 8 == 1.5


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças da trilha ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def bola_txt(c, t, t0, s, cx, cy, r, size, cor=None):
    """resposta na esfera: "2 A" com a unidade menor"""
    v, _, u = s.partition(" ")
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r * ease_back(prog(t, t0, 0.5)), cor, a),
                                     F.medida(c, v, u, cx, cy + size * 0.36, size, E.SOBRE, a, "center", cor_u=E.SOBRE)))


def troca(c, t, itens, fn):
    """um de cada vez: itens = [(instante, arg)], cada um sai quando o próximo chega; fn(arg, a) desenha"""
    for i, (ti, s) in enumerate(itens):
        fim = itens[i + 1][0] - 0.1 if i + 1 < len(itens) else 1e9
        if t >= ti - 0.01:
            E.saida(c, t, fim, lambda s=s, ti=ti: E.foco(c, t, ti, 0.45, lambda a: fn(s, a)), d=0.25)


def pilula_em(c, t, t0, s, cx, cy, size, fundo=None, est="g"):
    E.foco(c, t, t0, 0.4, lambda a: E.pilula(c, s, cx, cy, size, est, fundo=fundo, a=a, cor=BR))


def lembrete(c, t, C, cena, itens, desenhos=()):
    """lembrete de 2 ou 3 coisas: itens = [(cue, linha fina, linha forte, linha de fórmula ou None)]"""
    n = len(itens)
    E.frase(c, t, C[cena] + 0.2, ps("você precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C[cena + ".a"], 0.5, lambda a: E.escreve(c, str(n), XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C[cena + ".a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 820, 1000
    hs = [200 + (80 if it[3] else 0) for it in itens]
    gap = 40 if n == 2 else 30
    y = 120 + (800 - sum(hs) - gap * (n - 1)) / 2
    for i, (k, l1, l2, l3) in enumerate(itens):
        h = hs[i]
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, h, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 56)], x + 44, y + 82)
        E.frase(c, t, C[k] + 0.3, [(l2, "g", 56, COR)], x + 44, y + 160)
        if l3:
            E.foco(c, t, C[k] + 0.9, 0.5, lambda a, l3=l3, y=y: fi(c, l3, x + 44, y + 245, 50, "b", TINTA2, a))
        if i < len(desenhos) and desenhos[i]:
            E.foco(c, t, C[k] + 0.6, 0.5, lambda a, i=i, y=y, h=h: desenhos[i](a, x + w - 160, y + 105))
        y += h + gap
    E.frase(c, t, lerp(C[itens[-1][0]], C[cena + ".end"], 0.7), ps("faltou alguma?", "i", 54, COR) + ps("procure no canal", "i", 54),
            820, 1000, "left", 0.12)


def tag(c, t, t0, s, cx, cy, size=40, fundo=None, est="b"):
    """pílula pequena (tensão de um resistor, corrente de um ramo, potencial de um ponto)"""
    E.foco(c, t, t0, 0.4, lambda a: E.pilula(c, s, cx, cy, size, est, fundo=fundo or TINTA2, a=a, cor=BR))


def numero(c, t, t0, i, cx, cy, r=30, cor=None):
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r, cor, a), centro(c, str(i), cx, cy + r * 0.55, r * 1.3, "g", BR, a)))


# ---------------- fórmula com índice: cópia local de E.formula que aceita "_" (R_{eq}, R_1) ----------------
def _ler_i(s, i=0, fim=None):
    nos, txt = [], ""

    def solta():
        nonlocal txt
        if txt:
            nos.append(("t", txt))
            txt = ""

    while i < len(s):
        ch = s[i]
        if ch == fim:
            solta()
            return nos, i + 1
        if ch in "^_":
            solta()
            if s[i + 1] == "{":
                dentro, i = _ler_i(s, i + 2, "}")
            else:
                dentro, i = [("t", s[i + 1])], i + 2
            nos.append(("e" if ch == "^" else "i", dentro))
        elif ch == "f" and i + 1 < len(s) and s[i + 1] == "{":
            solta()
            cima, i = _ler_i(s, i + 2, "}")
            baixo, i = _ler_i(s, i + 1, "}")
            nos.append(("f", cima, baixo))
        else:
            txt += ch
            i += 1
    solta()
    return nos, i


def _medir_i(nos, size, est):
    w = 0.0
    for n in nos:
        if n[0] == "t":
            w += E.larg(n[1], est, size) + E.APERTO[est] * size + size * 0.02
        elif n[0] == "e":
            w += _medir_i(n[1], size * 0.58, est) + size * 0.04
        elif n[0] == "i":
            w += _medir_i(n[1], size * 0.5, "b") + size * 0.04
        else:
            w += max(_medir_i(n[1], size * 0.78, est), _medir_i(n[2], size * 0.78, est)) + size * 0.22
    return w


def _desenhar_i(c, nos, x, y, size, est, cor, a):
    for n in nos:
        if n[0] == "t":
            E.escreve(c, n[1], x, y, size, est, cor, a)
            x += E.larg(n[1], est, size) + E.APERTO[est] * size + size * 0.02
        elif n[0] == "e":
            _desenhar_i(c, n[1], x + size * 0.02, y - size * 0.42, size * 0.58, est, cor, a)
            x += _medir_i(n[1], size * 0.58, est) + size * 0.04
        elif n[0] == "i":
            _desenhar_i(c, n[1], x + size * 0.01, y + size * 0.16, size * 0.5, "b", cor, a)
            x += _medir_i(n[1], size * 0.5, "b") + size * 0.04
        else:
            s_ = size * 0.78
            wc, wb = _medir_i(n[1], s_, est), _medir_i(n[2], s_, est)
            w = max(wc, wb) + size * 0.12
            _desenhar_i(c, n[1], x + (w - wc) / 2, y - size * 0.46, s_, est, cor, a)
            _desenhar_i(c, n[2], x + (w - wb) / 2, y + size * 0.46, s_, est, cor, a)
            b = max(4, size * 0.07)
            c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y - size * 0.3 - b / 2, w, b), b / 2, b / 2), M.paint(cor, a))
            x += w + size * 0.1
    return x


def fi(c, s, x, y, size, estilo="g", cor=None, a=1.0, align="left"):
    """como E.formula (expoente ^ e fração f{}{}), com índice: "R_{eq} = R_1 + R_2". Devolve a largura"""
    nos, _ = _ler_i(s)
    w = _medir_i(nos, size, estilo)
    if a > 0 and c is not None:
        xi = x - w / 2 if align == "center" else x - w if align == "right" else x
        _desenhar_i(c, nos, xi, y, size, estilo, cor or TINTA, a)
    return w


def fi_em(c, t, t0, s, x, y, size, estilo="g", cor=None, align="left"):
    E.foco(c, t, t0, 0.5, lambda a: fi(c, s, x, y, size, estilo, cor, a, align))


# ---------------- peças de circuito (as mesmas nas aulas FIS-ELE-011 a 016) ----------------
def malha(c, t, t0, x0, y0, x1, y1, pecas, pilha=None, tp=None, d=0.8, escuro=False):
    """circuito em série: pilha no lado esquerdo (+ em cima), peças no lado de cima, fios no resto.
    pecas = [(tipo, rótulo, instante[, acesa])], tipo "R" (resistor) ou "L" (lâmpada). Devolve os (A, B) de cada peça"""
    n = len(pecas)
    xs = [x0 + (x1 - x0) * k / n for k in range(n + 1)]
    F.fio(c, t, t0, [(x0, y1), (x1, y1), (x1, y0)], d, escuro=escuro)
    F.pilha(c, t, tp if tp is not None else t0, (x0, y1), (x0, y0), pilha, escuro=escuro)
    ab = []
    for k, p in enumerate(pecas):
        A, B = (xs[k], y0), (xs[k + 1], y0)
        ab.append((A, B))
        if p[0] == "R":
            F.resistor(c, t, p[2], A, B, p[1], escuro=escuro)
        else:
            F.lampada(c, t, p[2], A, B, acesa=p[3] if len(p) > 3 else None, rotulo=p[1], escuro=escuro)
    return ab


def volta(x0, y0, x1, y1):
    """o caminho da corrente na malha: sai do + (canto de cima à esquerda) e volta pelo −"""
    return [(x0, y0), (x1, y0), (x1, y1), (x0, y1)]


def escada(c, t, t0, x0, y0, y1, xs, ramos, pilha=None, tp=None, d=0.8, escuro=False, nos=True):
    """circuito em paralelo: pilha no lado esquerdo (+ em cima), trilho de cima em y0 e de baixo em y1; cada ramo é uma peça
    vertical em xs[k] ligando os dois trilhos. ramos = [(tipo, rótulo, instante)] (tipo "R" ou "L")"""
    F.fio(c, t, t0, [(x0, y0), (xs[-1], y0)], d, escuro=escuro)
    F.fio(c, t, t0, [(x0, y1), (xs[-1], y1)], d, escuro=escuro)
    F.pilha(c, t, tp if tp is not None else t0, (x0, y1), (x0, y0), pilha, escuro=escuro)
    for k, p in enumerate(ramos):
        A, B = (xs[k], y0), (xs[k], y1)
        if p[0] == "R":
            F.resistor(c, t, p[2], A, B, p[1], escuro=escuro)
        else:
            F.lampada(c, t, p[2], A, B, rotulo=p[1], escuro=escuro)
        if nos and k < len(xs) - 1:
            E.foco(c, t, p[2], 0.4, lambda a, A=A, B=B: (F.no(c, A, a, escuro), F.no(c, B, a, escuro)))


def corrente_escada(c, t, t0, x0, y0, y1, xs, ramos=None, cor=None):
    """setinhas da corrente no circuito em escada: tronco pela pilha, uma descida por ramo (ramos = índices)"""
    F.corrente(c, t, t0, [(x0, y1), (x0, y0), (xs[-1], y0)], cor, fecha=False)
    F.corrente(c, t, t0, [(xs[-1], y1), (x0, y1)], cor, fecha=False)
    for k in (ramos if ramos is not None else range(len(xs))):
        F.corrente(c, t, t0, [(xs[k], y0), (xs[k], y1)], cor, fecha=False)


def curto(c, t, t0, A, B, fundo=110, d=0.6, cor=ERRADO):
    """fio do curto: sai de A, desce `fundo` px, passa por baixo e volta em B (vermelho)"""
    if t >= t0:
        F.poli(c, [A, (A[0], A[1] + fundo), (B[0], B[1] + fundo), B], ease_io(prog(t, t0, d)), cor, 1.0, 8)


def apaga(c, t, t0, A, B, larg=150):
    """véu de papel sobre um resistor que saiu do circuito (fica cinza)"""
    q = ep(t, t0, 0.6)
    if q > 0:
        cx, cy = (A[0] + B[0]) / 2, (A[1] + B[1]) / 2
        M.rrect(c, cx - larg / 2, cy - 40, larg, 80, 10, E.PAPEL if hasattr(E, "PAPEL") else "#F4F3EF", 0.7 * q)


def raio_choque(c, x, y, s, a=1.0, cor=None):
    """raiozinho de choque em zigue-zague"""
    if a <= 0:
        return
    pts = [(x, y), (x + s * 0.5, y + s * 0.6), (x + s * 0.1, y + s * 0.7), (x + s * 0.6, y + s * 1.4)]
    F.poli(c, pts, 1.0, cor or E.COR, a, max(5, s * 0.12))


def pessoa(c, x, ychao, s, a=1.0, mao_alto=True):
    """boneco em pé com os pés em ychao; devolve (mão, pé) para o caminho da corrente"""
    if a <= 0:
        return None
    cab = (x, ychao - s * 1.75)
    c.drawCircle(*cab, s * 0.16, M.paint(TINTA, a))
    ombro, quadril = (x, ychao - s * 1.5), (x, ychao - s * 0.85)
    M.line(c, *ombro, *quadril, TINTA, a, s * 0.1)
    pe1, pe2 = (x - s * 0.22, ychao), (x + s * 0.22, ychao)
    M.line(c, *quadril, *pe1, TINTA, a, s * 0.09)
    M.line(c, *quadril, *pe2, TINTA, a, s * 0.09)
    mao = (x + s * 0.35, ychao - s * 2.25) if mao_alto else (x + s * 0.5, ychao - s * 1.2)
    M.line(c, *ombro, *mao, TINTA, a, s * 0.08)
    M.line(c, *ombro, x - s * 0.35, ychao - s * 1.05, TINTA, a, s * 0.08)
    return mao, pe2, ombro, quadril


def passaro(c, x, y, s, a=1.0, asa=0.0):
    """passarinho pousado com as patas em (x ± s·0.15, y); asa = 0..1 abre a asa para baixo"""
    if a <= 0:
        return
    for dx in (-0.15, 0.15):
        M.line(c, x + dx * s, y, x + dx * s, y - s * 0.3, TINTA, a, 4)
    corpo = skia.Rect.MakeXYWH(x - s * 0.5, y - s * 0.85, s * 1.0, s * 0.6)
    c.drawOval(corpo, M.paint(F.VEL, a))
    c.drawCircle(x + s * 0.42, y - s * 0.85, s * 0.22, M.paint(F.VEL, a))
    c.drawCircle(x + s * 0.48, y - s * 0.9, s * 0.05, M.paint(BR, a))
    bico = skia.Path(); bico.moveTo(x + s * 0.62, y - s * 0.9); bico.lineTo(x + s * 0.8, y - s * 0.84); bico.lineTo(x + s * 0.62, y - s * 0.78); bico.close()
    c.drawPath(bico, M.paint("#FFC400", a))
    M.line(c, x - s * 0.1, y - s * 0.7, x - s * 0.1 - s * 0.4 * asa, y - s * 0.7 + s * 1.1 * asa, E.mix(F.VEL, "#000000", 0.25), a, s * 0.14)


def poste_fio(c, t, t0, x0, x1, y, a=1.0):
    """dois postes e o fio da rua entre eles"""
    q = ep(t, t0, 0.5) * a
    if q <= 0:
        return
    for x in (x0, x1):
        M.rrect(c, x - 12, y - 40, 24, 640, 6, "#8A8F99", q)
        M.line(c, x - 60, y, x + 60, y, "#8A8F99", q, 10)
    M.line(c, x0, y, x1, y, TINTA, q, 6)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def um():
        y, ychao = 330, 930
        poste_fio(c, t, C["s01.a"], 860, 1800, y)
        E.foco(c, t, C["s01.a"] + 0.4, 0.5, lambda a: passaro(c, 1060, y, 100, a))
        E.foco(c, t, C["s01.b"], 0.4, lambda a: E.pilula(c, "nada", 1060, y - 170, 46, "g", fundo=CERTO, a=a))
        if t >= C["s01.c"]:
            M.line(c, 900, ychao, 1780, ychao, TINTA2, ep(t, C["s01.c"], 0.4), 5)
            E.foco(c, t, C["s01.c"], 0.5, lambda a: pessoa(c, 1450, ychao, 270, a))
        if t >= C["s01.d"]:
            q = ep(t, C["s01.d"], 0.3)
            raio_choque(c, 1570 + 6 * math.sin(t * 30), 360, 80, q, ERRADO)
            raio_choque(c, 1360 + 6 * math.sin(t * 27), 520, 70, q, ERRADO)
            E.foco(c, t, C["s01.d"], 0.4, lambda a: E.pilula(c, "choque!", 1700, 600, 50, "g", fundo=ERRADO, a=a))
        E.frase(c, t, C["s01.a"], [("passarinho", "g", 72), ("no", "i", 76), ("fio:", "i", 76)], XE, 300, passo=0.12)
        E.frase(c, t, C["s01.b"], [("nada", "g", 72, CERTO)], XE, 400)
        E.frase(c, t, C["s01.c"], [("pessoa", "g", 72), ("na", "i", 76), ("tomada:", "i", 76)], XE, 600, passo=0.12)
        E.frase(c, t, C["s01.d"], [("choque", "g", 72, ERRADO)], XE, 700)
        E.frase(c, t, lerp(C["s01.d"], C["s01.end"], 0.4), ps("qual é a diferença?", "i", 66, COR), XE, 880, passo=0.12)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t < C["s02"]:
        return
    tb = C["s02.a"] + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1520, 540, 300 * ease_back(prog(t, tb, 0.8)), giro=12 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 88), XE, 230, passo=0.14)
    itens = (("s02.a", "achar o curto", 1.2), ("s02.b", "o disjuntor", 0), ("s02.c", "a ligação da casa", 0), ("s02.d", "o perigo do choque", 0))
    for i, (k, s, dt) in enumerate(itens):
        y = 400 + i * 150
        numero(c, t, C[k] + dt, i + 1, XE + 40, y - 30, 38)
        E.frase(c, t, C[k] + dt + 0.1, [(s, "g", 72, COR if i == 0 else TINTA)], XE + 110, y)


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    lembrete(c, t, C, "s03", (("s03.b", "a lei de Ohm:", "U = R · i", None),
                              ("s03.c", "reduzir com série e paralelo,", "uma letra em cada nó", None)))


# ---------------- curto ----------------
def b_curto(c, t, C, b):
    E.frase(c, t, C["s04"], [("curto-circuito", "g", 90, ERRADO)], XE, 200)
    if t < C["s06"]:
        A, B = (900, 520), (1500, 520)
        F.fio(c, t, C["s04"], [(760, 520), A], 0.4)
        F.resistor(c, t, C["s04"] + 0.2, A, B, "R")
        F.fio(c, t, C["s04"] + 0.3, [B, (1640, 520)], 0.4)
        E.foco(c, t, C["s04"] + 0.4, 0.4, lambda a: (F.no(c, A, a), F.no(c, B, a)))
        curto(c, t, C["s04.a"], A, B, 180)
        E.frase(c, t, C["s04.a"], ps("um fio, sem resistor,", "i", 60) + [("ligando", "i", 60), ("2", "g", 58, COR), ("pontos", "i", 60)], XE, 340, passo=0.1)
        E.foco(c, t, C["s04.b"], 0.4, lambda a: E.formula(c, "R ≈ 0", 1200, 790, 64, "g", ERRADO, a, "center"))
        E.formula_em(c, t, C["s04.c"], "U = 0 · i = 0", XE, 900, 84, "g", TINTA)
        if t >= C["s05"]:
            apaga(c, t, C["s05.b"], A, B, 180)
            E.formula_em(c, t, C["s05.a"], "i no R = 0", XE + 700, 900, 84, "g", COR)
            E.foco(c, t, C["s05.b"] + 0.3, 0.4, lambda a: E.pilula(c, "sai do circuito", 1200, 330, 46, "b", fundo=TINTA, a=a))
            tag(c, t, C["s05.c"], "A", A[0], A[1] - 80, 46, E.COR, "g")
            tag(c, t, C["s05.c"] + 0.4, "A", B[0], B[1] - 80, 46, E.COR, "g")
            E.frase(c, t, C["s05.d"], ps("as duas pontas na mesma letra:", "i", 52, TINTA2) + [("some", "g", 50, COR)], XE, 1010, passo=0.08)
        return
    # s06: exemplo; s07: o pior caso
    x0, y0, x1, y1 = 760, 380, 1640, 820

    def s06():
        ab = malha(c, t, C["s06.a"], x0, y0, x1, y1, [("R", "4 Ω", C["s06.b"]), ("R", "2 Ω", C["s06.b"] + 0.3)], "12 V")
        F.corrente(c, t, C["s06.c"], volta(x0, y0, x1, y1), vel=80 if t < C["s06.e"] else 220)
        troca(c, t, [(C["s06.c"], "2 A"), (C["s06.f"], "6 A")], lambda s, a: E.pilula(c, s, (x0 + x1) / 2, y0 - 170, 50, "g", fundo=E.COR, a=a))
        A, B = ab[0]
        curto(c, t, C["s06.d"], A, B, 130)
        apaga(c, t, C["s06.e"], A, B, 180)
        E.formula_em(c, t, C["s06.c"], "6 Ω → 2 A", XE, 960, 64, "g", TINTA2)
        E.formula_em(c, t, C["s06.f"], "12 ÷ 2 = 6 A", XE + 520, 960, 64, "g", TINTA)
        E.foco(c, t, C["s06.g"], 0.5, lambda a: E.pilula(c, "× 3", 1780, y0 - 170, 56, "g", fundo=ERRADO, a=a))
    E.saida(c, t, C["s07"] - 0.1, s06)
    if t < C["s07"]:
        return
    F.pilha(c, t, C["s07"], (1000, 820), (1000, 420), "pilha")
    F.fio(c, t, C["s07"] + 0.2, [(1000, 420), (1400, 420), (1400, 820), (1000, 820)], 0.6)
    if t >= C["s07.b"]:
        q = 0.5 + 0.5 * math.sin(t * 6)
        F.poli(c, [(1000, 420), (1400, 420), (1400, 820), (1000, 820)], 1.0, ERRADO, ep(t, C["s07.b"], 0.5) * (0.5 + 0.5 * q), 14)
        F.corrente(c, t, C["s07.b"], [(1000, 420), (1400, 420), (1400, 820), (1000, 820)], fecha=False, vel=400, espaco=80)
    E.frase(c, t, C["s07.a"], ps("um fio direto nos polos", "i", 60), XE, 360, passo=0.1)
    E.frase(c, t, C["s07.b"], [("R", "g", 64), ("≈", "g", 64, TINTA2), ("0", "g", 64), ("→", "g", 64, TINTA2), ("i", "g", 64, ERRADO), ("enorme", "g", 64, ERRADO)],
            XE, 480, passo=0.12)
    E.frase(c, t, C["s07.c"], ps("esquenta os fios:", "i", 60) + [("incêndio", "g", 58, ERRADO)], XE, 620, passo=0.1)
    E.foco(c, t, C["s07.d"], 0.4, lambda a: E.pilula(c, "o calor da corrente: outra aula", XE + 400, 760, 42, "b", fundo=TINTA2, a=a))


# ---------------- proteção e casa ----------------
HX0, HY0, HY1, HXS = 330, 400, 820, [960, 1220, 1480, 1740]


def casa(c, t, t0, aberta, ramos, ligados, desliga=None, escuro=False, rot_disj="disjuntor"):
    """circuito da casa: a rede à esquerda, o disjuntor (chave) no fio de cima e os aparelhos em paralelo.
    aberta = 0..1 (1 = disjuntor aberto); ramos = quantos aparelhos; ligados = instante da corrente; desliga = (índice, instante)"""
    nomes = (("L", "lâmpada"), ("R", "TV"), ("R", "chuveiro"), ("R", "ferro"))
    xs = HXS[:ramos]
    F.fio(c, t, t0, [(HX0, HY0), (460, HY0)], 0.3)
    F.chave(c, t, t0, (460, HY0), (680, HY0), fechada=1 - aberta, rotulo=rot_disj)
    F.fio(c, t, t0, [(680, HY0), (xs[-1], HY0)], 0.6)
    F.fio(c, t, t0, [(HX0, HY1), (xs[-1], HY1)], 0.6)
    E.foco(c, t, t0, 0.4, lambda a: (E.pilula(c, "rede", HX0, (HY0 + HY1) / 2, 44, "g", fundo=TINTA, a=a),
                                     M.line(c, HX0, HY0, HX0, (HY0 + HY1) / 2 - 40, TINTA, a, 6),
                                     M.line(c, HX0, (HY0 + HY1) / 2 + 40, HX0, HY1, TINTA, a, 6)))
    for k, x in enumerate(xs):
        tipo, nome = nomes[k]
        if tipo == "L":
            F.lampada(c, t, t0 + 0.2 * k, (x, HY0), (x, HY1), acesa=(ligados if aberta < 0.5 and not (desliga and desliga[0] == k and t >= desliga[1]) else None),
                      rotulo=None)
        else:
            F.resistor(c, t, t0 + 0.2 * k, (x, HY0), (x, HY1), None)
        E.foco(c, t, t0 + 0.2 * k, 0.4, lambda a, x=x, nome=nome: E.pilula(c, nome, x, HY1 + 60, 38, "b", fundo=TINTA2, a=a))
        if k < len(xs) - 1:
            E.foco(c, t, t0 + 0.2 * k, 0.4, lambda a, x=x: (F.no(c, (x, HY0), a), F.no(c, (x, HY1), a)))
    if ligados is not None and aberta < 0.5:
        F.corrente(c, t, ligados, [(HX0, HY0), (xs[-1], HY0)], fecha=False)
        for k, x in enumerate(xs):
            if not (desliga and desliga[0] == k and t >= desliga[1]):
                F.corrente(c, t, ligados, [(x, HY0), (x, HY1)], fecha=False)


def b_casa(c, t, C, b):
    def s08():
        aberta = ease_io(prog(t, C["s08.e"], 0.4))
        casa(c, t, C["s08"], aberta, 3, C["s08.c"] if t < C["s08.e"] else None)
        E.frase(c, t, C["s08.a"], [("fusível", "g", 70, COR), ("e", "i", 74), ("disjuntor", "g", 70, COR)], XE, 220, passo=0.12)
        if t >= C["s08.b"]:
            p = ep(t, C["s08.b"], 0.5)
            E.caixa_pontilhada(c, 430, HY0 - 140, 280, 220, p, cor=E.COR, prog_=p)
            E.foco(c, t, C["s08.b"] + 0.4, 0.4, lambda a: E.escreve(c, "em série, no começo", 420, HY0 + 150, 46, "i", TINTA2, a))
        tag(c, t, C["s08.c"], "i > limite", 1100, 300, 46, ERRADO, "g")
        E.frase(c, t, C["s08.d"], ps("o fio do fusível", "i", 56, TINTA2) + [("derrete", "g", 54, ERRADO)], XE, 1020, passo=0.1)
        E.frase(c, t, C["s08.e"], ps("o disjuntor", "i", 56, TINTA2) + [("desarma", "g", 54, ERRADO)], XE + 820, 1020, passo=0.1)
        E.foco(c, t, C["s08.f"], 0.4, lambda a: E.pilula(c, "i = 0", 1500, 300, 50, "g", fundo=TINTA, a=a))
    E.saida(c, t, C["s09"] - 0.1, s08)
    if t < C["s09"]:
        return
    nr = 3 if t < C["s10.b"] else 4
    casa(c, t, C["s09"], ease_io(prog(t, C["s10.c"] + 0.8, 0.4)), nr, C["s09"] + 0.3, desliga=(1, C["s09.d"]), rot_disj="disjuntor" if t < C["s10.c"] else None)
    if nr == 4:
        E.foco(c, t, C["s10.b"], 0.4, lambda a: E.pilula(c, "+ 1 ramo", HXS[3], HY0 - 70, 42, "g", fundo=E.COR, a=a))
    E.frase(c, t, C["s09.a"], ps("a casa é ligada em", "i", 66) + [("paralelo", "g", 64, COR)], XE, 200, passo=0.12)
    for k in range(3):
        tag(c, t, C["s09.c"] + 0.2 * k, "127 V", HXS[k] + 100, (HY0 + HY1) / 2, 40)
    if t >= C["s09.d"] and t < C["s10"]:
        E.foco(c, t, C["s09.d"], 0.4, lambda a: E.pilula(c, "desligou: os outros seguem", 1260, HY1 + 190, 42, "b", fundo=TINTA, a=a))
    E.frase(c, t, C["s10.a"], ps("em série, a tensão se dividiria", "i", 54, TINTA2), XE, 1020, passo=0.1)
    E.frase(c, t, C["s10.b"], [("ramo", "i", 56), ("novo:", "i", 56), ("R eq", "g", 54), ("↓", "g", 54, CERTO), ("i", "g", 54), ("↑", "g", 54, ERRADO)],
            XE + 960, 1020, passo=0.1)
    E.foco(c, t, C["s10.c"], 0.4, lambda a: E.pilula(c, "o disjuntor desarma", 570, 300, 46, "g", fundo=ERRADO, a=a))


# ---------------- choque ----------------
def b_choque(c, t, C, b):
    def s11():
        y, ychao = 330, 930
        poste_fio(c, t, C["s11"], 1000, 1800, y)
        M.line(c, 1000, ychao, 1800, ychao, TINTA2, ep(t, C["s11"], 0.4), 5)
        r = pessoa(c, 1450, ychao, 270, ep(t, C["s11"], 0.5))
        if r and t >= C["s11.a"]:
            mao, pe, ombro, quadril = r
            F.corrente(c, t, C["s11.a"], [mao, ombro, quadril, pe], fecha=False, vel=150, espaco=70)
        E.frase(c, t, C["s11.a"], ps("o que machuca:", "i", 62) + [("a", "g", 60), ("corrente", "g", 60, COR)], XE, 330, passo=0.12)
        E.frase(c, t, C["s11.a"] + 1.2, ps("que atravessa o corpo", "i", 62), XE, 420, passo=0.12)
        E.frase(c, t, C["s11.b"], ps("só passa com", "i", 58, TINTA2) + [("tensão", "g", 56)] + ps("entre 2 pontos", "i", 58, TINTA2), XE, 560, passo=0.1)
        tag(c, t, C["s11.c"], "mão no fio", 1660, 260, 44, E.COR, "g")
        tag(c, t, C["s11.c"] + 0.5, "pé no chão", 1640, 990, 44, E.COR, "g")
    E.saida(c, t, C["s12"] - 0.1, s11)
    if C["s12"] <= t < C["s13"]:
        def s12():
            y = 470
            M.line(c, 760, y, 1840, y, TINTA, ep(t, C["s12"], 0.5), 6)
            asa = ease_io(prog(t, C["s12.c"], 0.6))
            E.foco(c, t, C["s12"], 0.5, lambda a: passaro(c, 1250, y, 170, a, asa))
            tag(c, t, C["s12.a"], "mesmo fio", 1250, y + 90, 44, TINTA)
            E.frase(c, t, C["s12.a"], ps("as duas patas no mesmo fio", "i", 58), XE, 330, passo=0.1)
            E.frase(c, t, C["s12.b"], [("U", "g", 70), ("=", "g", 70, TINTA2), ("0", "g", 70, CERTO), ("→", "g", 70, TINTA2), ("i", "g", 70), ("=", "g", 70, TINTA2),
                                       ("0", "g", 70, CERTO)], XE, 600, passo=0.12)
            if t >= C["s12.c"]:
                M.line(c, 760, 720, 1840, 720, TINTA, ep(t, C["s12.c"], 0.4), 6)
                q = ep(t, C["s12.c"] + 0.6, 0.3)
                raio_choque(c, 1140, 600, 70, q, ERRADO)
                E.frase(c, t, C["s12.c"], ps("a asa em outro fio:", "i", 56, TINTA2) + [("choque", "g", 54, ERRADO)], XE, 860, passo=0.1)
        E.saida(c, t, C["s13"] - 0.1, s12)
    if t < C["s13"]:
        return

    def s13():
        E.frase(c, t, C["s13.a"], ps("a resistência do corpo muda muito", "i", 62), XE, 230, passo=0.1)
        E.frase(c, t, C["s13.b"], ps("pele seca:", "i", 62) + [("100.000", "g", 62), ("Ω", "g", 50, F.UNID)], XE, 380, passo=0.12)
        E.frase(c, t, C["s13.c"], ps("molhada:", "i", 62) + [("1.000", "g", 62, ERRADO), ("Ω", "g", 50, F.UNID)], XE, 500, passo=0.12)
        E.formula_em(c, t, C["s13.d"], "i = 127 ÷ 1.000", XE, 700, 90, "g", TINTA)
        bola_txt(c, t, C["s13.e"], "0,127 A", 1250, 670, 150, 64, ERRADO)
    E.saida(c, t, C["s14"] - 0.1, s13)
    if t < C["s14"]:
        return
    # régua de perigo: 0 a 150 milésimos de ampère
    x0, x1, y = 260, 1660, 560
    vx = lambda v: lerp(x0, x1, v / 150)
    q = ep(t, C["s14"], 0.5)
    p = skia.Paint(AntiAlias=True)
    p.setShader(skia.GradientShader.MakeLinear([skia.Point(x0, 0), skia.Point(x1, 0)], [M.hexc(CERTO, q), M.hexc("#FFC400", q), M.hexc(ERRADO, q)], [0, 0.35, 0.75]))
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x0, y - 22, x1 - x0, 44), 22, 22), p)
    E.foco(c, t, C["s14"], 0.4, lambda a: E.escreve(c, "corrente pelo corpo (milésimos de ampère)", x0, y - 190, 48, "i", TINTA2, a))
    for v, s, k, dy in ((10, "10: os músculos travam", "s14.a", 110), (100, "100: o coração", "s14.b", 110)):
        E.foco(c, t, C[k], 0.5, lambda a, v=v, s=s, dy=dy: (M.line(c, vx(v), y - 30, vx(v), y + 50, TINTA, a, 5),
                                                            E.centro(c, s, vx(v) + (60 if v == 10 else 0), y + dy, 46, "b", TINTA, a)))
    E.foco(c, t, C["s14.c"], 0.5, lambda a: (E.bola(c, vx(127), y, 46, ERRADO, a), E.centro(c, "molhada: 127", vx(127), y - 80, 46, "g", ERRADO, a)))
    E.foco(c, t, C["s14.d"], 0.5, lambda a: (E.bola(c, vx(1.3), y, 34, CERTO, a), E.centro(c, "seca: ~1", vx(1.3) + 40, y - 80, 46, "g", CERTO, a)))
    E.frase(c, t, C["s14.e"], ps("nunca mexa em eletricidade com a", "i", 62) + [("mão", "g", 60, ERRADO), ("molhada", "g", 60, ERRADO)], W / 2, 900, "center", 0.1)


# ---------------- erro ----------------
def fusivel(c, cx, cy, w, rot, a=1.0, cor=TINTA, queimado=0.0):
    """fusível de cartucho: corpo de vidro, tampas e o fio fino dentro"""
    if a <= 0:
        return
    M.rrect(c, cx - w / 2, cy - w * 0.18, w, w * 0.36, w * 0.08, "#E9EEF2", a)
    for s in (-1, 1):
        M.rrect(c, cx + s * w / 2 - (w * 0.16 if s > 0 else 0), cy - w * 0.2, w * 0.16, w * 0.4, 6, "#8A8F99", a)
    if queimado < 1:
        M.line(c, cx - w * 0.34, cy, cx + w * 0.34, cy, cor, a * (1 - queimado), 4)
    E.centro(c, rot, cx, cy + w * 0.36, w * 0.2, "g", cor, a)


def b_erro(c, t, C, b):
    E.frase(c, t, C["s15"], [("cuidado", "g", 96, ERRADO)], XE, 200)
    E.frase(c, t, C["s15.a"], ps("o fusível vive queimando", "i", 64), XE, 350, passo=0.12)
    E.foco(c, t, C["s15.a"], 0.5, lambda a: fusivel(c, 440, 560, 300, "20 A", a, queimado=ep(t, C["s15.a"] + 0.8, 0.6)))
    E.foco(c, t, C["s15.b"], 0.5, lambda a: fusivel(c, 920, 560, 300, "40 A", a, ERRADO))
    E.foco(c, t, C["s15.b"], 0.4, lambda a: F.seta(c, 620, 560, 740, 560, TINTA2, a, 10))
    E.frase(c, t, C["s15.c"], ps("para de queimar...", "i", 58, TINTA2), 1200, 470, passo=0.1)
    E.frase(c, t, C["s15.d"], ps("mas o problema", "i", 58), 1200, 570, passo=0.1)
    E.frase(c, t, C["s15.d"] + 0.6, [("continua", "g", 58, ERRADO)], 1200, 650)
    if t >= C["s15.e"]:
        q = 0.5 + 0.5 * math.sin(t * 6)
        M.line(c, 260, 860, 1660, 860, ERRADO, ep(t, C["s15.e"], 0.5) * (0.55 + 0.45 * q), 16)
        E.foco(c, t, C["s15.e"], 0.4, lambda a: E.pilula(c, "fios sem proteção", 960, 960, 46, "g", fundo=ERRADO, a=a))
    E.frase(c, t, lerp(C["s15.e"], C["s15.end"], 0.7), [("certo:", "g", 52, CERTO)] + ps("descobrir a causa", "i", 56), 1200, 760, passo=0.1)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    E.frase(c, t, C["s16"], ps("o atalho para achar o", "i", 74, CLARO) + [("curto", "g", 72, BR)], W / 2, 170, "center", 0.12)
    x0, y0, x1, y1 = 560, 360, 1500, 780
    ab = malha(c, t, C["s16"], x0, y0, x1, y1, [("R", "R1", C["s16"]), ("R", "R2", C["s16"]), ("R", "R3", C["s16"])], None, escuro=True)
    A, B = ab[1]
    curto(c, t, C["s16.a"], A, B, 130, cor=CLARO)
    tag(c, t, C["s16.b"], "B", A[0], A[1] - 120, 46, E.COR, "g")
    tag(c, t, C["s16.b"] + 0.4, "B", B[0], B[1] - 120, 46, E.COR, "g")
    if t >= C["s16.c"]:
        M.line(c, A[0] + 30, A[1] + 40, B[0] - 30, B[1] - 40, ERRADO, 1.0, 10, progress=ep(t, C["s16.c"], 0.4))
    E.frase(c, t, C["s16.d"], ps("sobra um circuito mais simples", "g", 56, BR), W / 2, 920, "center", 0.1)
    E.frase(c, t, C["s16.e"], [("não", "g", 54, ERRADO)] + ps("é curto: fio com lâmpada ou resistor no meio", "i", 56, CLARO), W / 2, 1020, "center", 0.08)


# ---------------- questão ----------------
QX = (900, 420, 1760, 820)


def b_questao(c, t, C, b):
    E.frase(c, t, C["s17"], ps("hora de testar", "i", 72, COR), XE, 200)
    E.foco(c, t, C["s17.a"], 0.5, lambda a: F.medida(c, 12, "V", XE, 340, 100, COR, a))
    E.frase(c, t, C["s17.b"], ps("3 lâmpadas iguais de", "i", 60) + [("4", "g", 58), ("Ω", "g", 46, F.UNID)], XE, 470, passo=0.1)
    E.frase(c, t, C["s17.b"] + 1.2, ps("em série", "g", 58), XE, 550, passo=0.1)
    E.frase(c, t, C["s17.c"], ps("um fio nas pontas de uma", "i", 56, ERRADO), XE, 670, passo=0.1)
    E.frase(c, t, C["s17.d"], ps("essa lâmpada?", "g", 60), XE, 800, passo=0.1)
    E.frase(c, t, C["s17.e"], ps("corrente nas outras?", "g", 60, COR), XE, 900, passo=0.1)
    if t < C["s18"]:
        x0, y0, x1, y1 = QX
        ab = malha(c, t, C["s17.a"], x0, y0, x1, y1, [("L", None, C["s17.b"], C["s17.b"]), ("L", None, C["s17.b"] + 0.2, C["s17.b"]),
                                                      ("L", None, C["s17.b"] + 0.4, C["s17.b"])], "12 V")
        curto(c, t, C["s17.c"], *ab[1], 130)
    else:
        E.relogio(c, t, C["s18.a"], cx=1400, cy=500, r=200)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    x0, y0, x1, y1 = QX
    on = C["s19"]
    ab = malha(c, t, C["s19"], x0, y0, x1, y1, [("L", "4 Ω", on, on), ("L", "4 Ω", on, on if t < C["s19.c"] else None), ("L", "4 Ω", on, on)], "12 V")
    curto(c, t, C["s19.b"], *ab[1], 130)
    F.corrente(c, t, C["s19.a"], volta(x0, y0, x1, y1), vel=90 if t < C["s19.e"] else 160)
    troca(c, t, [(C["s19.a"], "1 A"), (C["s19.e"], "1,5 A")], lambda s, a: E.pilula(c, s, (x0 + x1) / 2, y0 - 180, 50, "g", fundo=E.COR, a=a))
    E.formula_em(c, t, C["s19.a"], "antes: 12 Ω → 1 A", XE, 330, 66, "g", TINTA2)
    E.frase(c, t, C["s19.b"], ps("a do meio fica sem tensão:", "i", 54), XE, 460, passo=0.1)
    E.frase(c, t, C["s19.c"], [("apaga", "g", 64, ERRADO)], XE, 550)
    E.formula_em(c, t, C["s19.d"], "4 + 4 = 8 Ω", XE, 690, 76, "g", TINTA)
    E.formula_em(c, t, C["s19.e"], "12 ÷ 8 = ", XE, 830, 76, "g", TINTA)
    bola_txt(c, t, C["s19.e"] + 0.5, "1,5 A", 640, 805, 90, 54, CERTO)
    E.frase(c, t, C["s19.f"], [("R", "g", 56), ("total", "i", 58), ("↓", "g", 56, CERTO), ("→", "g", 56, TINTA2), ("i", "g", 56), ("↑", "g", 56, ERRADO)],
            XE, 990, passo=0.1)


# ---------------- fechamento ----------------
def medidor(c, cx, cy, r, s, a=1.0, escuro=False):
    if a <= 0:
        return
    c.drawCircle(cx, cy, r, M.paint(BR if not escuro else "#14141C", a))
    c.drawCircle(cx, cy, r, M.paint(TINTA if not escuro else BR, a, stroke=6))
    E._meio(c, s, cx, cy, r * 1.0, "g", E.COR, a)


def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s20"], [("resumindo", "i", 92, COR)], W / 2, 170, "center")
        itens = (("s20.a", [("fio", "i", 60), ("sem", "i", 60), ("resistor", "i", 60), ("=", "g", 58, TINTA2), ("curto", "g", 58, ERRADO)]),
                 ("s20.b", [("fusível", "g", 58), ("e", "i", 60), ("disjuntor:", "g", 58), ("em", "i", 60), ("série", "g", 58, COR)]),
                 ("s20.c", [("casa", "g", 58), ("em", "i", 60), ("paralelo:", "g", 58, COR), ("mesma", "i", 60), ("tensão", "i", 60)]),
                 ("s20.d", [("choque", "g", 58), ("=", "g", 58, TINTA2), ("corrente", "g", 58, COR), ("pelo", "i", 60), ("corpo", "i", 60)]))
        for i, (k, partes) in enumerate(itens):
            y = 360 + i * 165
            numero(c, t, C[k], i + 1, 340, y - 24, 46)
            E.frase(c, t, C[k] + 0.1, partes, 430, y, passo=0.1)
    E.saida(c, t, C["s21"] - 0.1, resumo)
    if t < C["s21"]:
        return
    E.frase(c, t, C["s21"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C["s21.a"], [("amperímetro", "g", 96, COR)], XE, 400)
    E.frase(c, t, C["s21.a"] + 0.5, [("e", "i", 96), ("voltímetro", "g", 96, COR)], XE, 530)
    E.foco(c, t, C["s21.a"] + 0.8, 0.5, lambda a: (medidor(c, 330, 760, 80, "A", a), medidor(c, 560, 760, 80, "V", a)))
    E.foco(c, t, C["s21.b"], 0.5, lambda a: E.pilula(c, "a ponte de Wheatstone", 560, 940, 46, "g", fundo=TINTA, a=a))
    E.foco(c, t, C["s21.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 420, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s21.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(720, 445, p), ep(t, C["s21.c"] + 0.2, 0.4))
    E.frase(c, t, C["s21.d"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1570, 990, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, curto=b_curto, casa=b_casa, choque=b_choque, erro=b_erro, atalho=b_atalho,
              questao=b_questao, resposta=b_resposta, fim=b_fim)
