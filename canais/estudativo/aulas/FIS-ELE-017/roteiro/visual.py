"""Visual — Estudativo · FIS-ELE-017: potência elétrica e efeito Joule.

Segue a linguagem visual da Física (cabeçalho do visual.py da FIS-CIN-001) e a da Eletricidade (cabeçalho do visual.py da
FIS-ELE-001: F.resistor, F.lampada; unidades em cinza-tinta; Ω e = só na fonte pesada).
Nesta aula: a ETIQUETA do aparelho é a peça `etiqueta` (cartão com tensão e potência, como a placa do chuveiro); o
EFEITO JOULE é a peça `quente` (resistor com brilho laranja e ondas de calor subindo). As três fórmulas da potência ficam
sempre na mesma ordem: P = U·i, P = R·i², P = U²/R; a escolhida pelo que não muda ganha a pílula laranja.
Todo instante vem de C[...] (marcadores do roteiro)."""
import math

import editorial as E
import fisica as F
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Física", "Eletricidade")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_FIS-ELE-017_potencia_eletrica_e_efeito_joule.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("pui", "joule", "escolher", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"

# todas as contas da aula
assert 4400 / 220 == 20 and 220 / 20 == 11 and 11 * 20 ** 2 == 11 * 400 == 4400 and 220 ** 2 == 48400 and 48400 / 11 == 4400
assert 20 ** 2 / 10 == 40 and 20 ** 2 / 20 == 20
assert 100 * (110 / 220) ** 2 == 25 and 100 / 4 == 25
assert 1100 / 220 == 5 and 220 / 5 == 44 and 1100 / 4 == 275 and 110 ** 2 == 12100 and 12100 / 44 == 275 and 1100 / 2 == 550


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


# ---------------- peças desta aula ----------------
def etiqueta(c, x, y, w, linhas, a=1.0, titulo=None):
    """cartão de etiqueta do aparelho: linhas = [(texto, instante_alpha)] já resolvidas em alfa"""
    if a <= 0:
        return
    h = 120 + 110 * len(linhas)
    sombra = skia.Paint(AntiAlias=True, Color=M.hexc("#000000", 0.16 * a))
    sombra.setMaskFilter(skia.MaskFilter.MakeBlur(skia.kNormal_BlurStyle, 16))
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x + 6, y + 14, w, h), 24, 24), sombra)
    M.rrect(c, x, y, w, h, 24, "#FFFFFF", a)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 24, 24), M.paint(TINTA, a, stroke=4))
    M.rrect(c, x, y, w, 80, 24, TINTA, a)
    M.rrect(c, x, y + 50, w, 30, 0, TINTA, a)
    E.escreve(c, titulo or "ETIQUETA", x + 30, y + 56, 40, "b", BR, a)
    for i, (txt, q) in enumerate(linhas):
        v, _, u = txt.partition(" ")
        F.medida(c, v, u, x + 40, y + 170 + 110 * i, 84, TINTA, a * q)


def chuveiro(c, x, y, s, a=1.0, t=0.0):
    """chuveiro de lado: cano, crivo e gotas caindo"""
    if a <= 0:
        return
    M.line(c, x - s, y - s * 0.9, x, y - s * 0.9, TINTA2, a, s * 0.12)
    M.line(c, x, y - s * 0.9, x, y - s * 0.4, TINTA2, a, s * 0.12)
    p = skia.Path(); p.moveTo(x - s * 0.5, y); p.lineTo(x + s * 0.5, y); p.lineTo(x + s * 0.2, y - s * 0.45); p.lineTo(x - s * 0.2, y - s * 0.45); p.close()
    c.drawPath(p, M.paint("#8A8F99", a))
    for k in range(9):
        dx = (k - 4) * s * 0.11
        yy = y + 20 + ((t * 260 + k * 47) % (s * 1.4))
        M.line(c, x + dx * (1 + (yy - y) / (s * 2.5)), yy, x + dx * (1 + (yy - y + 18) / (s * 2.5)), yy + 18, "#4DA3D9", a * 0.9, 5)


def quente(c, t, t0, A, B, rot=None, onda=True, q=1.0):
    """resistor aquecido: brilho laranja atrás, o resistor em laranja e ondas de calor subindo"""
    k = ep(t, t0, 0.6) * q
    if k > 0:
        cx, cy = (A[0] + B[0]) / 2, (A[1] + B[1]) / 2
        g = skia.Paint(AntiAlias=True)
        g.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), 170, [M.hexc(E.COR, 0.45 * k), M.hexc(E.COR, 0)], [0, 1]))
        c.drawCircle(cx, cy, 170, g)
    F.resistor(c, t, t0, A, B, rot, cor=E.mix(TINTA, E.COR, k) if k > 0 else None, lado=-1)
    if onda and k > 0:
        cx = (A[0] + B[0]) / 2
        for j in range(3):
            x = cx - 50 + 50 * j
            pts = [(x + 10 * math.sin(t * 3 + j + i * 0.9), A[1] - 60 - 22 * i) for i in range(6)]
            F.poli(c, pts, 1.0, E.COR, k * 0.8, 5)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def um():
        E.foco(c, t, C["s01.a"], 0.5, lambda a: etiqueta(c, XE, 280, 620, [("220 V", ep(t, C["s01.b"], 0.4)), ("4.400 W", ep(t, C["s01.c"], 0.4))], a, "CHUVEIRO"))
        E.foco(c, t, C["s01.a"], 0.6, lambda a: chuveiro(c, 1450, 420, 220, a, t))
        E.frase(c, t, C["s01.d"], [("corrente:", "i", 70), ("?", "g", 76, COR)], 1050, 800, passo=0.12)
        E.frase(c, t, C["s01.e"], [("resistência:", "i", 70), ("?", "g", 76, COR)], 1050, 920, passo=0.12)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t < C["s02"]:
        return
    tb = C["s02.a"] + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1520, 540, 300 * ease_back(prog(t, tb, 0.8)), giro=12 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 88), XE, 260, passo=0.14)
    for i, f_ in enumerate(("P = U · i", "P = R · i^2", "P = f{U^2}{R}")):
        E.formula_em(c, t, C["s02.a"] + 1.2 + 0.4 * i, f_, XE + 360 * i, 480, 84, "g", COR if i == 0 else TINTA)
    E.frase(c, t, C["s02.b"], ps("e escolher pelo que", "i", 70) + [("não", "g", 66, COR), ("muda", "g", 66, COR)], XE, 760, passo=0.12)


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    lembrete(c, t, C, "s03", (("s03.b", "potência, em watt:", "energia ÷ tempo", "P = f{τ}{Δt}"),
                              ("s03.c", "energia da carga na tensão:", "carga × tensão", "τ = q · U"),
                              ("s03.d", "a lei de Ohm:", "U = R · i", None)))


# ---------------- P = U·i ----------------
def b_pui(c, t, C, b):
    def s04():
        E.frase(c, t, C["s04"], ps("de onde vem a", "i", 76) + [("potência", "g", 72, COR), ("elétrica?", "g", 72, COR)], XE, 200, passo=0.12)
        E.formula_em(c, t, C["s04.a"], "τ = q · U", XE, 380, 96, "g", TINTA)
        E.foco(c, t, C["s04.a"] + 0.4, 0.4, lambda a: E.escreve(c, "energia das cargas", XE + 520, 370, 50, "i", TINTA2, a))
        E.formula_em(c, t, C["s04.b"], "P = f{q · U}{Δt}", XE, 580, 96, "g", TINTA)
        E.formula_em(c, t, C["s04.c"], "f{q}{Δt} = i", XE + 620, 580, 96, "g", F.VEL)
        E.foco(c, t, C["s04.c"] + 0.4, 0.4, lambda a: E.escreve(c, "a corrente", XE + 1000, 570, 50, "i", TINTA2, a))
        E.foco(c, t, C["s04.d"], 0.6, lambda a: (E.bola(c, XE + 320, 820, 140, a=a), E.formula(c, "P = U · i", XE + 320, 850, 84, "g", E.SOBRE, a, "center")))
        E.frase(c, t, C["s04.e"], [("potência", "g", 62), ("=", "g", 62, TINTA2), ("tensão", "i", 66), ("×", "g", 62, TINTA2), ("corrente", "i", 66)], XE + 560, 820, passo=0.12)
        E.formula_em(c, t, C["s04.f"], "V · A = W", XE + 560, 930, 70, "g", F.UNID)
    E.saida(c, t, C["s05"] - 0.1, s04)
    if t < C["s05"]:
        return
    etiqueta(c, 1180, 260, 560, [("220 V", 1), ("4.400 W", 1)], ep(t, C["s05"], 0.5), "CHUVEIRO")
    E.formula_em(c, t, C["s05.a"], "4.400 = 220 · i", XE, 340, 80, "g", TINTA)
    E.formula_em(c, t, C["s05.b"], "i = 4.400 ÷ 220", XE, 500, 80, "g", TINTA)
    bola_txt(c, t, C["s05.c"], "20 A", 990, 470, 95, 60)
    E.formula_em(c, t, C["s05.d"], "R = 220 ÷ 20", XE, 720, 80, "g", TINTA)
    E.foco(c, t, C["s05.d"] + 0.4, 0.4, lambda a: E.escreve(c, "lei de Ohm", XE, 790, 46, "i", TINTA2, a))
    bola_txt(c, t, C["s05.e"], "11 Ω", 990, 690, 95, 60)


# ---------------- efeito Joule ----------------
def b_joule(c, t, C, b):
    def s06():
        E.frase(c, t, C["s06.a"], ps("a energia vira", "i", 76) + [("calor", "g", 72, COR)], XE, 220, passo=0.12)
        E.frase(c, t, C["s06.b"], [("efeito", "i", 90), ("Joule", "g", 90, COR)], XE, 380, passo=0.14)
        quente(c, t, C["s06.c"], (1050, 560), (1600, 560))
        E.frase(c, t, C["s06.c"], ps("a corrente esquenta o que tem resistência", "i", 52, TINTA2), XE, 480, passo=0.08)
        for i, s in enumerate(("ferro de passar", "torradeira", "secador")):
            E.foco(c, t, C["s06.d"] + 0.5 * i, 0.4, lambda a, s=s, i=i: E.pilula(c, s, XE + 200 + 430 * i, 700, 46, "g", fundo=E.COR, a=a))
        E.foco(c, t, C["s06.e"], 0.5, lambda a: F.lampada(c, t, C["s06.e"] - 10, (1300, 900), (1600, 900), acesa=C["s06.e"], r=60))
        E.frase(c, t, C["s06.e"], ps("lâmpada de filamento: quente", "i", 54), XE, 900, passo=0.1)
    E.saida(c, t, C["s07"] - 0.1, s06)
    if t < C["s07"]:
        return
    E.frase(c, t, C["s07"], ps("num resistor,", "i", 70) + [("U", "g", 66), ("=", "g", 66, TINTA2), ("R", "g", 66), ("·", "g", 66, TINTA2), ("i", "g", 66)], XE, 200, passo=0.12)
    linhas = (("P = U · i", -9, None), ("P = R · i^2", C["s07.a"], "troque o U por R · i"), ("P = f{U^2}{R}", C["s07.b"], "troque o i por U ÷ R"))
    for i, (f_, ti, nota) in enumerate(linhas):
        y = 400 + i * 200
        E.formula_em(c, t, ti if ti > 0 else C["s07"] + 0.5, f_, XE + 60, y, 100, "g", COR if i else TINTA)
        if nota:
            E.saida(c, t, C["s08"] - 0.1, lambda nota=nota, y=y, ti=ti: E.foco(c, t, ti + 0.4, 0.4, lambda a: E.escreve(c, nota, XE + 700, y - 20, 50, "i", TINTA2, a)))
    if C["s07.c"] <= t < C["s08"]:
        E.foco(c, t, C["s07.c"], 0.5, lambda a: E.pilula(c, "a mesma potência, 3 jeitos", W / 2, 990, 50, "g", fundo=TINTA, a=a))
    if t >= C["s08"]:
        E.formula_em(c, t, C["s08.a"], "11 · 20^2 = 11 · 400", XE + 700, 610, 64, "g", TINTA2)
        tag(c, t, C["s08.b"], "4.400 W", XE + 1500, 590, 46, CERTO, "g")
        E.formula_em(c, t, C["s08.c"], "f{220^2}{11} = f{48.400}{11}", XE + 700, 820, 64, "g", TINTA2)
        tag(c, t, C["s08.d"], "4.400 W", XE + 1500, 800, 46, CERTO, "g")


# ---------------- escolher ----------------
def b_escolher(c, t, C, b):
    E.frase(c, t, C["s09"], ps("qual usar?", "i", 76), XE, 200, passo=0.12)
    E.frase(c, t, C["s09.a"], ps("escolha pelo que", "i", 76) + [("não", "g", 72, COR), ("muda", "g", 72, COR)], XE + 450, 200, passo=0.12)
    # mesma corrente: um atrás do outro
    x0 = 160
    E.frase(c, t, C["s09.b"], [("mesma", "i", 62), ("corrente", "g", 60, F.VEL)], x0, 360, passo=0.12)
    E.formula_em(c, t, C["s09.b"] + 0.8, "P = R · i^2", x0, 470, 84, "g", TINTA)
    F.fio(c, t, C["s09.b"], [(x0, 700), (x0 + 60, 700)], 0.3)
    F.resistor(c, t, C["s09.b"], (x0 + 60, 700), (x0 + 330, 700), "R", lado=-1)
    quente(c, t, C["s09.c"], (x0 + 330, 700), (x0 + 700, 700), "2R", onda=True)
    F.fio(c, t, C["s09.b"], [(x0 + 700, 700), (x0 + 760, 700)], 0.3)
    F.corrente(c, t, C["s09.b"] + 0.4, [(x0, 700), (x0 + 760, 700)], fecha=False)
    E.frase(c, t, C["s09.c"], [("maior", "i", 58), ("R", "g", 56, COR), ("esquenta", "i", 58), ("mais", "g", 56, COR)], x0, 860, passo=0.1)
    # mesma tensão: na tomada
    x1 = 1020
    M.line(c, 980, 300, 980, 960, FIO, ep(t, C["s09.d"], 0.4), 3) if t >= C["s09.d"] else None
    E.frase(c, t, C["s09.d"], [("mesma", "i", 62), ("tensão", "g", 60, COR)], x1, 360, passo=0.12)
    E.formula_em(c, t, C["s09.d"] + 0.8, "P = f{U^2}{R}", x1, 470, 84, "g", TINTA)
    E.foco(c, t, C["s09.d"] + 0.4, 0.4, lambda a: E.pilula(c, "tomada", x1 + 600, 455, 44, "g", fundo=TINTA, a=a))
    quente(c, t, C["s09.e"], (x1 + 40, 700), (x1 + 330, 700), "R", onda=True)
    F.resistor(c, t, C["s09.d"] + 0.6, (x1 + 440, 700), (x1 + 780, 700), "2R", lado=-1)
    E.frase(c, t, C["s09.e"], [("menor", "i", 58), ("R", "g", 56, COR), ("esquenta", "i", 58), ("mais", "g", 56, COR)], x1, 860, passo=0.1)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s10"], [("cuidado", "g", 96, ERRADO)], XE, 200)
    E.frase(c, t, C["s10.a"], ps("mais R", "i", 70) + [("sempre", "g", 66), ("esquenta", "i", 70), ("mais?", "g", 66, ERRADO)], XE, 340, passo=0.12)
    E.foco(c, t, C["s10.c"], 0.5, lambda a: F.medida(c, 20, "V", XE, 480, 90, COR, a))
    E.frase(c, t, C["s10.b"], [("10", "g", 60), ("Ω", "g", 48, F.UNID), ("e", "i", 62), ("20", "g", 60), ("Ω,", "g", 48, F.UNID)] + ps("um de cada vez", "i", 60, TINTA2),
            XE + 320, 480, passo=0.1)
    fi_em(c, t, C["s11.a"], "f{20^2}{10} = f{400}{10}", XE, 680, 84, "g", TINTA)
    bola_txt(c, t, C["s11.a"] + 1.2, "40 W", 900, 655, 90, 60, CERTO)
    fi_em(c, t, C["s11.b"], "f{400}{20}", XE + 1000, 680, 84, "g", TINTA)
    bola_txt(c, t, C["s11.b"] + 0.8, "20 W", 1560, 655, 90, 60, TINTA2)
    E.frase(c, t, C["s11.c"], ps("tensão fixa: menor", "i", 62) + [("R", "g", 60, COR), ("→", "g", 60, TINTA2), ("mais", "i", 62), ("corrente", "g", 60, COR)], XE, 900, passo=0.1)
    E.frase(c, t, C["s11.d"], [("esquenta", "g", 60, COR), ("mais", "g", 60, COR)], XE, 990, passo=0.12)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def s12():
        E.frase(c, t, C["s12"], ps("o atalho:", "i", 72, CLARO), XE, 200)
        E.frase(c, t, C["s12.a"], ps("o mesmo aparelho, outra tensão", "g", 60, BR), XE + 330, 200, passo=0.1)
        F.lampada(c, t, C["s12.b"], (1150, 520), (1650, 520), acesa=C["s12.b"], r=90, escuro=True)
        F.lampada(c, t, C["s12.c"], (1150, 800), (1650, 800), acesa=None, r=90, escuro=True)
        if t >= C["s12.c"]:
            g = skia.Paint(AntiAlias=True)
            q = ep(t, C["s12.c"] + 0.4, 0.6)
            g.setShader(skia.GradientShader.MakeRadial(skia.Point(1400, 800), 140, [M.hexc("#FFC400", 0.25 * q), M.hexc("#FFC400", 0)], [0, 1]))
            c.drawCircle(1400, 800, 140, g)
        E.formula_em(c, t, C["s12.b"], "100 W em 220 V", XE, 420, 72, "g", BR)
        E.formula_em(c, t, C["s12.c"], "ligada em 110 V", XE, 560, 72, "g", CLARO)
        E.frase(c, t, C["s12.d"], [("R", "g", 56, BR), ("fixa:", "i", 58, CLARO)], XE, 700, passo=0.12)
        fi_em(c, t, C["s12.d"] + 0.6, "P = f{U^2}{R}", XE + 280, 700, 66, "g", BR)
        E.formula_em(c, t, C["s12.e"], "U ÷ 2 → P ÷ 4", XE, 860, 76, "g", BR)
        bola_txt(c, t, C["s12.f"], "25 W", XE + 700, 840, 90, 60)
    E.saida(c, t, C["s13"] - 0.1, s12)
    if t < C["s13"]:
        return
    E.frase(c, t, C["s13.a"], [("U", "g", 70, BR)] + ps("em cima e ao quadrado,", "i", 72, CLARO) + [("R", "g", 70, BR), ("fixa", "i", 72, CLARO)], W / 2, 380, "center", 0.12)
    E.frase(c, t, C["s13.b"], ps("o fator da tensão vai ao quadrado", "g", 62, BR), W / 2, 540, "center", 0.1)
    E.frase(c, t, C["s13.c"], [("não", "g", 58, ERRADO), ("vale:", "i", 62, CLARO)] + ps("se a questão disser que R muda", "i", 62, CLARO), W / 2, 780, "center", 0.1)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s14"], ps("hora de testar", "i", 72, COR), XE, 200)
    E.foco(c, t, C["s14.a"], 0.5, lambda a: etiqueta(c, XE, 280, 560, [("1.100 W", 1), ("220 V", 1)], a, "FERRO DE PASSAR"))
    E.frase(c, t, C["s14.b"], [("corrente?", "g", 66)], XE + 700, 380)
    E.frase(c, t, C["s14.c"], [("resistência?", "g", 66)], XE + 700, 500)
    E.frase(c, t, C["s14.d"], [("potência", "g", 66, COR), ("em", "i", 70), ("110", "g", 66, COR), ("V?", "g", 66, COR)], XE + 700, 620, passo=0.12)
    if t >= C["s15"]:
        E.relogio(c, t, C["s15.a"], cx=1580, cy=780, r=140)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    def s16():
        E.formula_em(c, t, C["s16.a"], "i = 1.100 ÷ 220", XE, 340, 90, "g", TINTA)
        bola_txt(c, t, C["s16.b"], "5 A", 1050, 310, 100, 66, CERTO)
        E.formula_em(c, t, C["s16.c"], "R = 220 ÷ 5", XE, 640, 90, "g", TINTA)
        bola_txt(c, t, C["s16.d"], "44 Ω", 1050, 610, 100, 66, CERTO)
    E.saida(c, t, C["s17"] - 0.1, s16)
    if t < C["s17"]:
        return
    E.frase(c, t, C["s17.a"], [("U", "g", 66), ("÷", "g", 66, TINTA2), ("2", "g", 66, COR), ("→", "g", 66, TINTA2), ("P", "g", 66), ("÷", "g", 66, TINTA2),
                               ("4", "g", 66, COR)], XE, 260, passo=0.12)
    E.formula_em(c, t, C["s17.b"], "1.100 ÷ 4", XE, 440, 90, "g", TINTA)
    bola_txt(c, t, C["s17.c"], "275 W", 900, 410, 110, 60, CERTO)
    fi_em(c, t, C["s17.d"], "f{110^2}{44} = f{12.100}{44} = 275", XE, 700, 76, "g", TINTA2)
    E.foco(c, t, C["s17.e"], 0.5, lambda a: F.medida(c, 550, "W", XE, 930, 80, ERRADO, a))
    if t >= C["s17.e"] + 0.6:
        E.risco(c, XE - 10, 950, XE + 260, 870, t, C["s17.e"] + 0.6, largura=10)
    E.frase(c, t, C["s17.e"] + 0.9, ps("dividiu só por 2: esqueceu o quadrado", "i", 54, TINTA2), XE + 330, 925, passo=0.1)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s18"], [("resumindo", "i", 92, COR)], W / 2, 190, "center")
        E.formula_em(c, t, C["s18.a"], "P = U · i", 400, 420, 90, "g", COR)
        E.foco(c, t, C["s18.a"] + 0.5, 0.4, lambda a: E.escreve(c, "qualquer aparelho", 400, 500, 50, "i", TINTA2, a))
        E.formula_em(c, t, C["s18.b"], "P = R · i^2", 1000, 420, 90, "g", TINTA)
        E.formula_em(c, t, C["s18.b"] + 0.5, "P = f{U^2}{R}", 1450, 420, 90, "g", TINTA)
        E.foco(c, t, C["s18.b"] + 0.9, 0.4, lambda a: E.escreve(c, "num resistor", 1000, 530, 50, "i", TINTA2, a))
        E.frase(c, t, C["s18.c"], ps("escolha pelo que", "i", 76) + [("não", "g", 72, COR), ("muda", "g", 72, COR)], W / 2, 760, "center", 0.12)
    E.saida(c, t, C["s19"] - 0.1, resumo)
    if t < C["s19"]:
        return
    E.frase(c, t, C["s19"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C["s19.a"], [("quilowatt-hora", "g", 100, COR)], XE, 400)
    E.frase(c, t, C["s19.b"], ps("e a conta de luz", "i", 90), XE, 540, passo=0.12)
    # o mostrador do medidor de luz
    def medidor_luz(a):
        M.rrect(c, XE + 40, 660, 560, 230, 26, "#1B1B20", a)
        for i, d in enumerate("04620"):
            M.rrect(c, XE + 80 + 96 * i, 700, 80, 110, 10, "#FFFFFF", a)
            E.centro(c, d, XE + 120 + 96 * i, 785, 80, "g", TINTA, a)
        E.escreve(c, "kWh", XE + 80, 860, 40, "b", BR, a)
    E.foco(c, t, C["s19.b"] + 0.3, 0.5, medidor_luz)
    E.foco(c, t, C["s19.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 420, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s19.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(720, 445, p), ep(t, C["s19.c"] + 0.2, 0.4))
    E.frase(c, t, C["s19.d"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1570, 990, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, pui=b_pui, joule=b_joule, escolher=b_escolher, erro=b_erro, atalho=b_atalho,
              questao=b_questao, resposta=b_resposta, fim=b_fim)
