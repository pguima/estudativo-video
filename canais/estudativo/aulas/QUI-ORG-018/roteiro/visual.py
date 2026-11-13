"""Visual — Estudativo · QUI-ORG-018: reações de adição. Primeira aula do módulo Reações orgânicas.

Segue a LINGUAGEM VISUAL DA QUÍMICA (cabeçalho de QUI-MIS-001) e o complemento da Orgânica de QUI-ORG-015 (estr, alceno).
LINGUAGEM DAS REAÇÕES ORGÂNICAS (QUI-ORG-018 a 024 copiam daqui):
- A equação vem em cima, em fórmula condensada (Q.equacao, cada termo no seu instante, seta na cor da matéria); embaixo, o
  "zoom" da reação em estrutura plana, onde se vê o que quebra e o que entra.
- O átomo ou grupo que ENTRA fica na cor da matéria (COR) do começo ao fim; o que SAI fica em cinza (TINTA2) e desliza para
  fora da molécula. A ligação que se desfaz some com desfoque; a nova cresce.
- Pose fixa da adição (adicao): os carbonos da dupla na horizontal; os átomos novos chegam de cima, do reagente desenhado
  sobre a molécula, e os ligantes antigos se abrem para os lados, até o carbono ficar com quatro ligações em cruz.
- Contagem de hidrogênios de um carbono (Markovnikov e afins): caixa pontilhada nos H e a pílula "2 H" / "1 H" ao lado.
Todo instante vem de C[...] (marcadores do roteiro), para acompanhar a voz real quando ela chegar."""
import math

import editorial as E
import quimica as Q
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Química", "Química Orgânica")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_QUI-ORG-018_reacoes_de_adicao.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("adicao", "h2", "margarina", "markov", "atalho", "questao", "fim"))

# toda equação da aula fecha a conta de átomos
for eq in ("C2H4 + H2 -> C2H6", "C2H4 + HBr -> C2H5Br", "C3H6 + HBr -> C3H7Br", "C4H8 + HBr -> C4H9Br", "C4H8 + H2 -> C4H10",
           "CH4 + Cl2 -> CH3Cl + HCl"):
    assert Q.lados(eq)[0] == Q.lados(eq)[1], eq
assert Q.contar("CH2CH2") == Q.contar("C2H4") and Q.contar("CH3CH3") == Q.contar("C2H6") == {"C": 2, "H": 6}
assert Q.contar("CH2CHCH3") == Q.contar("C3H6") and Q.contar("CH3CHBrCH3") == Q.contar("C3H7Br")
assert Q.contar("CH2CHCH2CH3") == Q.contar("C4H8") and Q.contar("CH3CHBrCH2CH3") == Q.contar("C4H9Br")
assert Q.contar("CH3CH2CH2CH3") == Q.contar("C4H10")


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças da Orgânica (candidatas ao kit quimica.py; iguais em todas as aulas QUI-ORG-015 a 028) ----------------
BR = "#FFFFFF"


def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def bola_txt(c, t, t0, s, cx, cy, r, size, cor=None):
    """resposta na esfera"""
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r * ease_back(prog(t, t0, 0.5)), cor, a),
                                     E.formula(c, s, cx, cy + size * 0.36, size, "g", E.SOBRE, a, "center")))


def pilula_em(c, t, t0, s, cx, cy, size, fundo=None, est="g", cor=BR):
    E.foco(c, t, t0, 0.4, lambda a: E.pilula(c, s, cx, cy, size, est, fundo=fundo, a=a, cor=cor))


def lista(c, t, itens, x, y0, dy, escuro=False):
    """lista numerada: itens = [(instante, partes da frase)]"""
    for i, (ti, partes) in enumerate(itens):
        y = y0 + i * dy
        E.foco(c, t, ti, 0.5, lambda a, i=i, y=y: (E.bola(c, x + 40, y - 26, 44, a=a), centro(c, str(i + 1), x + 40, y - 4, 54, "g", E.SOBRE, a)))
        E.frase(c, t, ti + 0.1, partes, x + 110, y, passo=0.12)


def rot(c, s, cx, cy, size, cor=None, a=1.0, escuro=False):
    """rótulo químico (CH3, OH, COOH) centrado em (cx, cy) nas duas direções"""
    if a > 0 and s:
        Q.formula(c, s, cx, cy + size * 0.36, size, cor, a, "center", escuro=escuro)


def _meia(s, size):
    """meia largura e meia altura da caixa de um rótulo"""
    if not s:
        return size * 0.05, size * 0.05
    return Q.formula(None, s, 0, 0, size) / 2, size * 0.42


def _corta(P, s, size, ux, uy, folga):
    """distância do centro do rótulo até a borda dele na direção (ux, uy)"""
    w, h = _meia(s, size)
    if not s:
        return 0
    k = min(w / abs(ux) if abs(ux) > 1e-6 else 1e9, h / abs(uy) if abs(uy) > 1e-6 else 1e9)
    return k + folga


def estr(c, t, t0, atomos, ligs, cx, cy, esc=150, size=80, tl=None, passo=0.12, cores=None, escuro=False, a=1.0, cor_lig=None, d=0.4):
    """fórmula estrutural plana com rótulos químicos: atomos = [(rótulo, x, y)] em unidades de ligação (rótulo "" = vértice
    sem letra); ligs = [(i, j, ordem[, cor])]. Cada átomo entra no seu instante (tl ou t0 + i·passo); a ligação cresce quando as
    duas pontas existem. cores = {i: cor} pinta o rótulo i. t0 = None desenha parado. Devolve os pontos na tela"""
    tinta = Q._tinta(escuro)
    pts = [(cx + x * esc, cy + y * esc) for _, x, y in atomos]
    ts = [(tl[i] if tl else (t0 if t0 is not None else -99) + i * passo) for i in range(len(atomos))]
    lw = max(5, size * 0.075)
    for lg in ligs:
        i, j, o = lg[0], lg[1], lg[2]
        cr = lg[3] if len(lg) > 3 and lg[3] else (cor_lig or tinta)
        p = 1.0 if t0 is None else ease_out(prog(t, max(ts[i], ts[j]) + 0.2, 0.4))
        if p <= 0 or o <= 0:
            continue
        A, B = pts[i], pts[j]
        ux, uy = E._uni(*A, *B)
        nx, ny = -uy, ux
        ra = _corta(A, atomos[i][0], size, ux, uy, size * 0.14)
        rb = _corta(B, atomos[j][0], size, ux, uy, size * 0.14)
        A2, B2 = (A[0] + ux * ra, A[1] + uy * ra), (B[0] - ux * rb, B[1] - uy * rb)
        g = size * 0.17
        for k in {1: (0,), 2: (-0.5, 0.5), 3: (-1, 0, 1)}[o]:
            M.line(c, A2[0] + nx * k * g, A2[1] + ny * k * g, B2[0] + nx * k * g, B2[1] + ny * k * g, cr, a, lw, progress=p)
    for i, (s, _, _) in enumerate(atomos):
        cr = (cores or {}).get(i, None)
        if t0 is None:
            rot(c, s, *pts[i], size, cr, a, escuro)
        else:
            E.foco(c, t, ts[i], d, lambda q, s=s, i=i, cr=cr: rot(c, s, *pts[i], size, cr, q * a, escuro))
    return pts


# alceno plano: os dois carbonos da dupla na horizontal e os quatro ligantes a 120°
ALC = [("C", -0.62, 0), ("C", 0.62, 0), (None, -1.25, -0.95), (None, -1.25, 0.95), (None, 1.25, -0.95), (None, 1.25, 0.95)]


def alceno(c, t, t0, cx, cy, subs, esc=150, size=80, tl=None, cores=None, escuro=False, a=1.0, ordem=2, carbonos=("C", "C"), cor_dupla=None):
    """subs = (em cima à esquerda, embaixo à esquerda, em cima à direita, embaixo à direita). Devolve os 6 pontos"""
    at = [(carbonos[0], -0.62, 0), (carbonos[1], 0.62, 0)] + [(s, x, y) for s, (_, x, y) in zip(subs, ALC[2:])]
    ligs = [(0, 1, ordem, cor_dupla), (0, 2, 1), (0, 3, 1), (1, 4, 1), (1, 5, 1)]
    return estr(c, t, t0, at, ligs, cx, cy, esc, size, tl, 0.1, cores, escuro, a)


def colchetes(c, x0, x1, cy, h, a=1.0, cor=None, n="n", size=64, escuro=False):
    """[ ... ]n em volta da unidade que se repete"""
    if a <= 0:
        return
    cr = cor or Q._tinta(escuro)
    lw, k = 6, h * 0.12
    for x, s in ((x0, 1), (x1, -1)):
        pth = skia.Path(); pth.moveTo(x + s * k, cy - h / 2); pth.lineTo(x, cy - h / 2); pth.lineTo(x, cy + h / 2); pth.lineTo(x + s * k, cy + h / 2)
        c.drawPath(pth, M.paint(cr, a, stroke=lw))
    if n:
        E.escreve(c, n, x1 + 12, cy + h / 2 + size * 0.2, size, "g", cr, a)


def espelho(c, x, y0, y1, a=1.0, escuro=False):
    """espelho visto de lado: faixa azulada com fio tracejado"""
    if a <= 0:
        return
    p = skia.Paint(AntiAlias=True)
    p.setShader(skia.GradientShader.MakeLinear([skia.Point(x - 22, 0), skia.Point(x + 22, 0)],
                                               [M.hexc("#9CC9E8", 0.0), M.hexc("#9CC9E8", 0.55 * a), M.hexc("#9CC9E8", 0.0)], [0, 0.5, 1]))
    c.drawRect(skia.Rect.MakeLTRB(x - 22, y0, x + 22, y1), p)
    M.line(c, x, y0, x, y1, "#5B8DB8", a, 4, dash=[18, 12])


def seta_em(c, t, t0, x0, x1, y, size=80, rotulo=None, escuro=False, eq=False, cor=None, d=0.6):
    """seta da reação que cresce a partir de t0; y = linha de base do texto ao lado"""
    p = ease_out(prog(t, t0, d))
    if p > 0:
        Q.seta_reacao(c, x0, x1, y, size, cor or (E.CLARO if escuro else E.COR), 1.0, p, eq, rotulo, escuro)


def x_em(c, t, t0, cx, cy, r=34, ok=False):
    """selo de certo ou errado que entra com salto"""
    q = ease_back(prog(t, t0, 0.45))
    if q > 0:
        E.selo(c, cx, cy, r * q, ok, min(1, q))


def anel(c, cx, cy, r, a=1.0, cor=None, lw=7, giro=90):
    """benzeno em bastão: hexágono com três duplas por dentro"""
    if a <= 0:
        return []
    cr = cor or TINTA
    v = [(cx + r * math.cos(math.radians(giro + 60 * k)), cy - r * math.sin(math.radians(giro + 60 * k))) for k in range(6)]
    for k in range(6):
        M.line(c, *v[k], *v[(k + 1) % 6], cr, a, lw)
        if k % 2 == 0:
            A, B = v[k], v[(k + 1) % 6]
            mx, my = (A[0] + B[0]) / 2, (A[1] + B[1]) / 2
            ux, uy = cx - mx, cy - my
            n = math.hypot(ux, uy)
            ux, uy = ux / n * r * 0.17, uy / n * r * 0.17
            M.line(c, lerp(A[0], B[0], 0.18) + ux, lerp(A[1], B[1], 0.18) + uy, lerp(A[0], B[0], 0.82) + ux, lerp(A[1], B[1], 0.82) + uy, cr, a, lw)
    return v


def circ(c, t, t0, cx, cy, r, cor=None, lw=7, t1=None):
    """círculo de destaque que se fecha em volta de algo"""
    if t < t0 or (t1 is not None and t >= t1 + 0.4):
        return
    p = ease_out(prog(t, t0, 0.45))
    a = 1 - ep(t, t1, 0.4) if t1 is not None else 1
    pth = skia.Path(); pth.addArc(skia.Rect.MakeLTRB(cx - r, cy - r, cx + r, cy + r), -90, 360 * p)
    c.drawPath(pth, M.paint(cor or E.COR, a, stroke=lw))


def caixa(c, t, t0, x, y, w, h, cor=None, t1=None):
    """caixa pontilhada que se desenha (x, y = canto de cima à esquerda)"""
    if t < t0 or (t1 is not None and t >= t1 + 0.4):
        return
    p = ep(t, t0, 0.4)
    a = 1 - ep(t, t1, 0.4) if t1 is not None else 1
    E.caixa_pontilhada(c, x, y, w, h, p * a, cor, prog_=p)


def caixa_rot(c, t, t0, P, s, size, cor=None, pad=14, t1=None):
    """caixa pontilhada em volta de um rótulo da estrutura (P = centro dele)"""
    w, h = _meia(s, size)
    caixa(c, t, t0, P[0] - w - pad, P[1] - h - pad, 2 * (w + pad), 2 * (h + pad), cor, t1)


# ---------------- peças desta aula ----------------
OLEO = "#F2C94C"
# pose da adição: ligantes antigos (alceno) → posição final em cruz; átomos novos chegam de cima
ANTES = [(-1.25, -0.95), (-1.25, 0.95), (1.25, -0.95), (1.25, 0.95)]
DEPOIS = [(-1.8, 0.0), (-0.62, 1.15), (1.8, 0.0), (0.62, 1.15)]
REAG = [(-0.45, -2.0), (0.45, -2.0)]
NOVO = [(-0.62, -1.15), (0.62, -1.15)]


def adicao(c, t, t0, tr, tu, cx, cy, esc, size, subs, novos=("H", "H"), escuro=False, cores=None, d=1.4, a=1.0, dx=None):
    """alceno (entra em t0) + reagente em cima (entra em tr) → em tu a dupla abre e cada carbono recebe um átomo novo.
    subs = ligantes do alceno (em cima à esq., embaixo à esq., em cima à dir., embaixo à dir.); dx = afasta rótulos longos.
    Devolve os pontos: C1, C2, os 4 ligantes, os 2 novos"""
    u = ease_io(prog(t, tu, d)) if tu is not None else 0.0
    dx = dx or {}
    lig = [(lerp(x0, x1, u) + (dx.get(k, 0) * (1 if x1 > 0 else -1) * u), lerp(y0, y1, u)) for k, ((x0, y0), (x1, y1)) in enumerate(zip(ANTES, DEPOIS))]
    nov = [(lerp(x0, x1, u), lerp(y0, y1, u)) for (x0, y0), (x1, y1) in zip(REAG, NOVO)]
    at = [("C", -0.62, 0), ("C", 0.62, 0)] + [(s, x, y) for s, (x, y) in zip(subs, lig)] + [(s, x, y) for s, (x, y) in zip(novos, nov)]
    ordem = 2 if u < 0.45 else 1
    ligs = [(0, 1, ordem, E.COR if ordem == 2 else None), (0, 2, 1), (0, 3, 1), (1, 4, 1), (1, 5, 1)]
    if u < 0.25:
        ligs.append((6, 7, 1))           # a ligação do reagente, que se desfaz
    if u > 0.75:
        ligs += [(0, 6, 1, E.COR), (1, 7, 1, E.COR)]  # as ligações novas
    tl = [t0, t0 + 0.1, t0 + 0.2, t0 + 0.3, t0 + 0.4, t0 + 0.5, tr, tr + 0.15]
    cr = dict(cores or {})
    cr.setdefault(6, CLARO if escuro else COR); cr.setdefault(7, CLARO if escuro else COR)
    return estr(c, t, t0, at, ligs, cx, cy, esc, size, tl=tl, cores=cr, escuro=escuro, a=a)


def conta_h(c, t, t0, P, n, lado, size=44, cor=None):
    """pílula com o número de hidrogênios de um carbono, ao lado dele"""
    E.foco(c, t, t0, 0.4, lambda a: E.pilula(c, f"{n} H", P[0] + lado * 0, P[1] + 120, size, "g", fundo=cor or E.COR, a=a))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    a1, b1, c1, d1 = C["s01.a"], C["s01.b"], C["s01.c"], C["s01.d"]
    if t < C["s02"]:
        Q.bequer(c, t, a1, 560, 860, 360, 420, 0.72, OLEO, graduacao=False)
        E.foco(c, t, a1 + 0.3, 0.4, lambda a: centro(c, "óleo: líquido", 560, 960, 56, "g", TINTA, a))
        E.foco(c, t, b1, 0.5, lambda a: (M.rrect(c, 1180, 600, 420, 260, 40, "#FFF4C2", a, shadow=True),
                                         M.rrect(c, 1160, 560, 460, 70, 30, E.COR, a),
                                         centro(c, "margarina", 1390, 610, 46, "g", BR, a)))
        E.foco(c, t, b1 + 0.3, 0.4, lambda a: centro(c, "margarina: pastosa", 1390, 960, 56, "g", TINTA, a))
        E.frase(c, t, c1, [("hidrogênio", "g", 70, COR)] + ps("entrando nas duplas", "i", 70), W / 2, 200, "center", 0.12)
        E.frase(c, t, d1, [("reação", "g", 80), ("de", "i", 84), ("adição", "g", 80, COR)], W / 2, 330, "center", 0.15)
        seta_em(c, t, b1, 820, 1100, 720, 100, cor=TINTA2)
        return
    tb = C["s02.a"] + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1600, 560, 260 * ease_back(prog(t, tb, 0.8)), giro=8 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 88), XE, 260, passo=0.14)
    lista(c, t, [(C["s02.b"], [("adição", "g", 66, COR), ("de", "i", 70)]),
                 (C["s02.c"], [("regra", "i", 70), ("de", "i", 70), ("Markovnikov", "g", 66, COR)]),
                 (C["s02.d"], [("a", "i", 70), ("margarina", "g", 66)]),
                 (C["s02.e"], [("atalho", "g", 66, COR), ("de", "i", 70), ("prova", "i", 70)])], XE, 420, 150)
    w = E._arranjo([("adição", "g", 66), ("de", "i", 70)], 0, "left")[0]
    Q.formula_em(c, t, C["s02.b"] + 0.5, "H2", XE + 110 + w + 24, 420, 66)
    Q.formula_em(c, t, C["s02.b"] + 0.8, "e HBr", XE + 110 + w + 120, 420, 66)


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], ps("lembre dos hidrocarbonetos", "i", 70, TINTA2), XE, 190, passo=0.12)
    E.frase(c, t, C["s03.a"], [("alceno", "g", 120, COR)], XE, 360)
    E.frase(c, t, C["s03.a"] + 0.6, ps("tem dupla entre carbonos", "i", 66), XE + 500, 345, passo=0.12)
    E.frase(c, t, C["s03.b"], [("carbono", "g", 70), ("=", "g", 70, TINTA2), ("4", "g", 70, COR), ("ligações", "i", 76)], XE, 560, passo=0.12)
    P = alceno(c, t, C["s03.a"] + 1.0, 1300, 780, ("H", "H", "H", "H"), 150, 80, cor_dupla=E.COR)
    E.frase(c, t, C["s03.c"], ps("a dupla conta", "i", 64) + [("2", "g", 60, COR)], XE, 760, passo=0.12)
    if t >= C["s03.c"]:
        circ(c, t, C["s03.c"] + 0.3, P[0][0], P[0][1], 140, E.COR)
        E.foco(c, t, C["s03.c"] + 0.6, 0.4, lambda a: E.escreve(c, "1 + 1 + 2 = 4", XE, 900, 60, "g", TINTA2, a))


# ---------------- o que é adição ----------------
def porta(c, cx, cy, h, abre, a=1.0):
    """porta de duas folhas vista de cima: abre = 0 fechada, 1 aberta"""
    if a <= 0:
        return
    L = h * 0.5
    for s in (-1, 1):  # a parede dos dois lados do vão
        M.line(c, cx + s * L, cy, cx + s * (L + 160), cy, TINTA2, a, 16)
    for s in (-1, 1):
        pth = skia.Path(); r_ = L
        pth.addArc(skia.Rect.MakeLTRB(cx + s * L - r_, cy - r_, cx + s * L + r_, cy + r_), 180 if s > 0 else 0, -90 * s)
        c.drawPath(pth, M.paint(TINTA2, 0.35 * a, stroke=3))
    for s in (-1, 1):
        ang = math.radians(90 * abre) * s
        x0 = cx + s * L
        x1, y1 = x0 - s * L * math.cos(ang), cy + L * math.sin(abs(ang))
        M.line(c, x0, cy, x1, y1, "#A97F48", a, 22)
        E.bola(c, x0, cy, 14, "#5A5F68", a)


def b_adicao(c, t, C, b):
    if t < C["s05"]:
        E.frase(c, t, C["s04"], ps("pense numa porta de", "i", 72) + [("duas folhas", "g", 68)], XE, 220, passo=0.12)
        ab = ease_io(prog(t, C["s04.b"], 1.0))
        E.foco(c, t, C["s04.a"], 0.5, lambda a: porta(c, 620, 520, 560, ab, a))
        E.foco(c, t, C["s04.a"] + 0.4, 0.4, lambda a: centro(c, "fechada" if ab < 0.5 else "aberta: cada folha com um lado livre", 620, 880, 50, "i", TINTA2, a))
        P = alceno(c, t, C["s04.c"], 1420, 560, ("H", "H", "H", "H"), 140, 76, cor_dupla=E.COR)
        if t >= C["s04.d"]:
            for k in range(2):
                circ(c, t, C["s04.d"] + 0.2 * k, P[k][0], P[k][1] - 120, 40, E.COR)
                E.foco(c, t, C["s04.d"] + 0.3 + 0.2 * k, 0.3, lambda a, k=k: centro(c, "?", P[k][0], P[k][1] - 101, 52, "g", COR, a))
            E.foco(c, t, C["s04.d"] + 0.4, 0.4, lambda a: E.pilula(c, "uma vaga em cada carbono", 1420, 900, 48, "g", fundo=E.COR, a=a))
        return
    E.frase(c, t, C["s05"], [("adição:", "g", 90, COR)], XE, 200)
    E.frase(c, t, C["s05.a"], [("2", "g", 70, COR)] + ps("moléculas viram", "i", 74) + [("1", "g", 70, COR)], XE + 420, 200, passo=0.12)
    adicao(c, t, C["s05"] + 0.4, C["s05"] + 0.8, C["s05.c"] - 0.2, W / 2, 680, 150, 80, ("H", "H", "H", "H"), ("H", "H"))
    E.foco(c, t, C["s05.b"], 0.4, lambda a: E.pilula(c, "dupla → simples", 360, 560, 48, "g", fundo=TINTA, a=a))
    E.foco(c, t, C["s05.c"] + 0.6, 0.4, lambda a: E.pilula(c, "cada carbono ganha um", 1560, 480, 48, "g", fundo=E.COR, a=a))
    E.foco(c, t, C["s05.d"], 0.4, lambda a: E.pilula(c, "nada sai", 1560, 900, 56, "g", fundo=TINTA, a=a))


# ---------------- hidrogenação ----------------
EQ_H2 = "CH2=CH2 + H2 ->{Ni} CH3–CH3"


def b_h2(c, t, C, b):
    tl = [C["s06.a"], C["s06.b"], C["s06.b"] + 0.2, C["s06.c"], C["s06.e"]]
    Q.equacao(c, t, C["s06.a"], EQ_H2, W / 2, 220, 84, tl=tl, cores={2: COR})
    if t < C["s07"]:
        adicao(c, t, C["s06.a"] + 0.4, C["s06.b"] + 0.3, C["s06.c"], W / 2, 690, 150, 80, ("H", "H", "H", "H"), ("H", "H"))
        E.foco(c, t, C["s06.b"] + 0.8, 0.4, lambda a: E.pilula(c, "níquel ajuda", 1500, 380, 46, "g", fundo=TINTA2, a=a))
        E.foco(c, t, C["s06.e"] + 0.3, 0.4, lambda a: centro(c, "etano", W / 2, 1010, 64, "g", COR, a))
        return
    E.frase(c, t, C["s07.a"], [("hidrogenação", "g", 110, COR)], W / 2, 440, "center")
    E.frase(c, t, C["s07.a"] + 0.8, ps("adição de hidrogênio", "i", 60, TINTA2), W / 2, 530, "center", 0.1)
    E.foco(c, t, C["s07.b"], 0.4, lambda a: E.escreve(c, "antes", 380, 700, 56, "i", TINTA2, a))
    E.foco(c, t, C["s07.b"] + 0.3, 0.4, lambda a: Q.formula(c, "2 C · 4 + 2 H", 380, 800, 70, TINTA, a))
    E.foco(c, t, C["s07.c"], 0.4, lambda a: E.pilula(c, "os 2 do H₂", 600, 880, 44, "g", fundo=E.COR, a=a))
    E.foco(c, t, C["s07.d"], 0.4, lambda a: E.escreve(c, "depois", 1180, 700, 56, "i", TINTA2, a))
    E.foco(c, t, C["s07.d"] + 0.3, 0.4, lambda a: Q.formula(c, "2 C · 6 H", 1180, 800, 70, TINTA, a))
    x_em(c, t, C["s07.d"] + 0.8, 1640, 780, 50, True)


# ---------------- margarina ----------------
def b_margarina(c, t, C, b):
    pts = Q.zigzag(14)
    E.frase(c, t, C["s08.a"], ps("óleo vegetal: moléculas compridas com", "i", 62) + [("várias duplas", "g", 58, COR)], XE, 200, passo=0.1)
    tc = C["s08.c"]
    if t < tc + 0.6:
        E.saida(c, t, tc + 0.5, lambda: Q.bastao(c, t, C["s08.a"] + 0.5, pts, W / 2, 470, 110, duplas=[(2, 3), (5, 6), (8, 9)], d=1.2))
    if t >= tc:
        E.foco(c, t, tc + 0.2, 0.5, lambda a: Q.bastao(c, t, -99, pts, W / 2, 470, 110, duplas=[(8, 9)]), blur=0)
        for k, (i, j) in enumerate(((2, 3), (5, 6))):
            mx, my = (pts[i][0] + pts[j][0]) / 2, (pts[i][1] + pts[j][1]) / 2
            E.foco(c, t, tc + 0.4 + 0.2 * k, 0.4, lambda a, mx=mx, my=my: Q.formula(c, "+ H2", W / 2 + mx * 110, 470 + my * 110 - 70, 48, COR, a, "center"))
    E.foco(c, t, C["s08.b"], 0.4, lambda a: E.pilula(c, "+ hidrogênio, quente, com níquel", W / 2, 680, 50, "g", fundo=TINTA, a=a))
    Q.bequer(c, t, C["s08.d"] - 0.4, 560, 1000, 260, 240, 0.72, OLEO, graduacao=False)
    seta_em(c, t, C["s08.d"], 800, 1080, 900, 90, cor=TINTA2)
    E.foco(c, t, C["s08.d"] + 0.4, 0.5, lambda a: (M.rrect(c, 1180, 820, 360, 180, 36, "#FFF4C2", a, shadow=True),
                                                   M.rrect(c, 1160, 790, 400, 60, 26, E.COR, a)))
    E.foco(c, t, C["s08.e"], 0.4, lambda a: centro(c, "margarina", 1360, 935, 56, "g", TINTA, a))


# ---------------- HBr e Markovnikov ----------------
PROP = ("H", "H", "H", "CH3")


def b_markov(c, t, C, b):
    if t < C["s10"]:
        def s09():
            Q.equacao(c, t, C["s09.a"], "CH2=CH2 + HBr -> CH3–CH2Br", W / 2, 220, 84, tl=[C["s09"], C["s09.a"], C["s09.a"] + 0.2, C["s09.c"], C["s09.c"] + 0.6], cores={2: COR})
            adicao(c, t, C["s09"] + 0.3, C["s09.a"] + 0.3, C["s09.c"], W / 2, 690, 150, 80, ("H", "H", "H", "H"), ("H", "Br"))
            E.foco(c, t, C["s09.b"], 0.4, lambda a: E.pilula(c, "no eteno, tanto faz", 1560, 420, 48, "g", fundo=TINTA, a=a))
        E.saida(c, t, C["s10"] - 0.1, s09)
        return
    Q.formula_em(c, t, C["s10.a"], "CH2=CH–CH3", W / 2, 210, 90, align="center")
    E.foco(c, t, C["s10.a"], 0.4, lambda a: E.escreve(c, "propeno", XE, 210, 56, "i", TINTA2, a))
    tu = C["s11.d"]
    P = adicao(c, t, C["s10.a"] + 0.4, C["s10.c"], tu, W / 2, 690, 150, 80, PROP, ("H", "Br"), dx={3: 0.25})
    if t < C["s11"]:
        E.foco(c, t, C["s10.b"], 0.4, lambda a: E.pilula(c, "carbonos diferentes", 1560, 420, 48, "g", fundo=TINTA, a=a))
        E.frase(c, t, C["s10.c"], ps("o bromo vai para a", "i", 64) + [("ponta", "g", 60, COR)] + ps("ou para o", "i", 64) + [("meio?", "g", 60, COR)], W / 2, 1010, "center", 0.1)
        return
    if t < tu:
        E.frase(c, t, C["s11.a"], [("Markovnikov:", "g", 60, COR)] + ps("o H vai para o carbono da dupla", "i", 60), W / 2, 1000, "center", 0.1)
        E.frase(c, t, C["s11.b"], ps("que já tem", "i", 60) + [("mais hidrogênios", "g", 56, COR)], W / 2, 1065, "center", 0.1)
    caixa(c, t, C["s11.c"], P[2][0] - 60, P[2][1] - 60, 120, P[3][1] - P[2][1] + 120, E.COR, t1=tu)
    caixa(c, t, C["s11.c"] + 0.5, P[4][0] - 60, P[4][1] - 60, 120, 120, TINTA2, t1=tu)
    E.saida(c, t, tu, lambda: (E.foco(c, t, C["s11.c"] + 0.2, 0.4, lambda a: E.pilula(c, "2 H", P[2][0] - 160, P[0][1], 50, "g", fundo=E.COR, a=a)),
                               E.foco(c, t, C["s11.c"] + 0.7, 0.4, lambda a: E.pilula(c, "1 H", P[4][0] + 160, P[4][1], 50, "g", fundo=TINTA2, a=a))))
    if t >= C["s11.e"]:
        circ(c, t, C["s11.e"], P[7][0], P[7][1], 66, E.COR)
        E.foco(c, t, C["s11.e"] + 0.3, 0.4, lambda a: E.pilula(c, "bromo no carbono do meio", 1500, 420, 48, "g", fundo=E.COR, a=a))
        Q.formula_em(c, t, C["s11.e"] + 0.6, "CH3–CHBr–CH3", W / 2, 1030, 80, align="center", cores={"Br": COR})


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s12"], [("cuidado", "g", 96, ERRADO)], XE, 190)
    E.frase(c, t, C["s12.a"], ps("inverter a regra", "i", 74), XE + 450, 190, passo=0.12)
    P = adicao(c, t, C["s12"] + 0.3, C["s12"] + 0.5, C["s12.b"] + 0.2, 820, 640, 140, 76, PROP, ("Br", "H"), dx={3: 0.25},
               cores={6: ERRADO, 7: ERRADO})
    xr = 1180
    E.frase(c, t, C["s12.b"], ps("H no carbono com", "i", 58) + [("menos H", "g", 54, ERRADO)], xr, 420, passo=0.1)
    wr = Q.formula(None, "CH2Br–CH2–CH3", 0, 0, 68)
    E.foco(c, t, C["s12.c"], 0.4, lambda a: Q.formula(c, "CH2Br–CH2–CH3", xr, 560, 68, ERRADO, a))
    if t >= C["s12.c"] + 0.8:
        E.risco(c, xr - 10, 575, xr + wr + 10, 500, t, C["s12.c"] + 0.8, largura=10)
    E.foco(c, t, C["s12.d"], 0.4, lambda a: E.pilula(c, "sai pouco", xr + 140, 660, 48, "g", fundo=ERRADO, a=a))
    wc = Q.formula(None, "CH3–CHBr–CH3", 0, 0, 68)
    E.foco(c, t, C["s12.d"] + 1.2, 0.4, lambda a: Q.formula(c, "CH3–CHBr–CH3", xr, 850, 68, TINTA, a, cores={"Br": COR}))
    x_em(c, t, C["s12.d"] + 1.6, xr + wc + 60, 828, 38, True)
    E.foco(c, t, C["s12.d"] + 1.6, 0.4, lambda a: E.escreve(c, "o principal, que a prova cobra", xr, 940, 50, "i", TINTA2, a))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    if t < C["s14"]:
        E.frase(c, t, C["s13"], ps("o atalho para não inverter", "i", 70, CLARO), W / 2, 160, "center", 0.12)
        E.frase(c, t, C["s13.a"], ps("quem tem", "i", 80, CLARO) + [("mais H", "g", 76, BR)] + ps("ganha", "i", 80, CLARO) + [("mais H", "g", 76, E.CLARO)], W / 2, 330, "center", 0.12)
        E.frase(c, t, C["s13.b"], ps("o rico fica mais rico", "i", 70, CLARO), W / 2, 450, "center", 0.12)
        adicao(c, t, C["s13.a"] + 0.6, C["s13.a"] + 1.0, C["s13.b"] + 0.4, W / 2, 780, 120, 64, PROP, ("H", "Br"), escuro=True, dx={3: 0.25})
        E.foco(c, t, C["s13.b"] + 2.4, 0.4, lambda a: E.pilula(c, "o porquê: outra aula", W / 2, 1020, 44, "g", fundo=E.COR, a=a))
        return
    E.frase(c, t, C["s14.a"], [("não", "g", 66, ERRADO)] + ps("precisa da regra quando", "i", 70, CLARO), W / 2, 200, "center", 0.12)
    E.frase(c, t, C["s14.a"] + 0.6, [("1", "g", 60, CLARO)] + ps("os dois átomos que entram são iguais", "i", 62, CLARO), XE, 370, passo=0.1)
    Q.formula_em(c, t, C["s14.a"] + 1.4, "H2", 1500, 370, 76, escuro=True)
    E.frase(c, t, C["s14.b"], [("2", "g", 60, CLARO)] + ps("a molécula é igual dos dois lados da dupla", "i", 62, CLARO), XE, 520, passo=0.1)
    Q.formula_em(c, t, C["s14.b"] + 1.2, "CH2=CH2", 560, 700, 80, align="center", escuro=True)
    Q.formula_em(c, t, C["s14.b"] + 1.6, "CH3–CH=CH–CH3", 1300, 700, 80, align="center", escuro=True)
    E.frase(c, t, C["s14.c"], ps("qualquer lado dá o", "i", 66, CLARO) + [("mesmo produto", "g", 62, BR)], W / 2, 920, "center", 0.12)


# ---------------- questão ----------------
QF = "CH2=CH–CH2–CH3"


def b_questao(c, t, C, b):
    E.frase(c, t, C["s15"], ps("hora de testar", "i", 72, COR), XE, 170)
    E.foco(c, t, C["s15"] + 0.6, 0.4, lambda a: E.escreve(c, "but-1-eno", XE + 520, 170, 62, "g", TINTA, a))
    Q.formula_em(c, t, C["s15.a"], QF, XE, 400, 110)
    G = [g for g in Q.grupos(QF, XE, 400, 110) if g["s"] == "C"]
    for k, g in enumerate(G):
        x = g["x0"] + 110 * 0.36
        E.foco(c, t, C["s15.a"] + 0.6 + 0.15 * k, 0.4, lambda a, x=x, k=k: (E.bola(c, x, 400 - 110 - 36, 30, a=a), centro(c, str(k + 1), x, 400 - 110 - 22, 38, "g", E.SOBRE, a)))
    E.frase(c, t, C["s15.b"], [("1", "g", 58, COR)] + ps("com HBr: em que carbono fica o bromo?", "i", 62), XE, 650, passo=0.1)
    w2 = E.frase(c, t, C["s15.c"], [("2", "g", 58, COR), ("com", "i", 62)], XE, 760, passo=0.1)
    Q.formula_em(c, t, C["s15.c"] + 0.2, "H2", XE + w2 + 16, 760, 62)
    E.frase(c, t, C["s15.c"] + 0.3, ps(": o que sai?", "i", 62), XE + w2 + 100, 760, passo=0.1)
    if t >= C["s16"]:
        E.relogio(c, t, C["s16.a"], cx=1520, cy=560, r=180)


# ---------------- resposta ----------------
BUT = ("H", "H", "H", "CH2–CH3")


def b_resposta(c, t, C, b):
    E.frase(c, t, C["s17"], ps("resolvendo", "i", 72, COR), XE, 170)
    if t < C["s18"]:
        tu = C["s17.c"]
        P = adicao(c, t, C["s17"] + 0.2, C["s17"] + 0.4, tu, W / 2 - 60, 640, 145, 78, BUT, ("H", "Br"), dx={3: 0.45})
        caixa(c, t, C["s17.a"], P[2][0] - 60, P[2][1] - 60, 120, P[3][1] - P[2][1] + 120, E.COR, t1=tu)
        caixa(c, t, C["s17.b"], P[4][0] - 60, P[4][1] - 60, 120, 120, TINTA2, t1=tu)
        E.saida(c, t, tu, lambda: (E.foco(c, t, C["s17.a"] + 0.2, 0.4, lambda a: E.pilula(c, "C1: 2 H", P[2][0] - 200, P[0][1], 48, "g", fundo=E.COR, a=a)),
                                   E.foco(c, t, C["s17.b"] + 0.2, 0.4, lambda a: E.pilula(c, "C2: 1 H", P[4][0] + 210, P[4][1], 48, "g", fundo=TINTA2, a=a))))
        if t >= C["s17.d"]:
            circ(c, t, C["s17.d"], P[7][0], P[7][1], 66, E.COR)
            Q.formula_em(c, t, C["s17.d"] + 0.4, "CH3–CHBr–CH2–CH3", W / 2, 1020, 76, align="center", cores={"Br": COR})
            x_em(c, t, C["s17.d"] + 0.8, 1660, 1000, 36, True)
        return
    Q.equacao(c, t, C["s18.a"], "CH2=CH–CH2–CH3 + H2 -> CH3–CH2–CH2–CH3", W / 2, 420, 76, tl=[C["s18.a"], C["s18.a"] + 0.3, C["s18.a"] + 0.5, C["s18.a"] + 0.9, C["s18.b"]], cores={2: COR})
    E.frase(c, t, C["s18.a"], ps("a regra nem entra:", "i", 64, TINTA2) + ps("um H em cada carbono", "i", 64), W / 2, 260, "center", 0.1)
    E.foco(c, t, C["s18.b"] + 0.3, 0.4, lambda a: centro(c, "butano", W / 2 + 420, 560, 64, "g", COR, a))
    Q.formula_em(c, t, C["s18.b"] + 0.6, "C4H10", W / 2 + 420, 700, 90, align="center")
    x_em(c, t, C["s18.b"] + 1.0, W / 2 + 640, 670, 44, True)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s19"], [("resumindo", "i", 92, COR)], XE, 170)
        itens = (("s19.a", [("adição:", "g", 64, COR)] + ps("a dupla abre, 2 moléculas viram 1", "i", 66)),
                 ("s19.b", [("com", "i", 66), ("H₂:", "g", 64), ("hidrogenação,", "i", 66), ("margarina", "g", 64)]),
                 ("s19.c", [("com", "i", 66), ("HBr:", "g", 64), ("o H vai para quem tem", "i", 66), ("mais H", "g", 64, COR)]))
        for i, (k, partes) in enumerate(itens):
            y = 340 + i * 180
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, XE + 40, y - 26, 46, a=a), centro(c, str(i + 1), XE + 40, y - 4, 56, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, partes, XE + 120, y, passo=0.1)
        adicao(c, t, C["s19.a"] + 0.4, C["s19.a"] + 0.6, C["s19.a"] + 1.0, 1560, 860, 95, 52, ("H", "H", "H", "H"), ("H", "H"))
    E.saida(c, t, C["s20"] - 0.1, resumo)
    if t < C["s20"]:
        return
    E.frase(c, t, C["s20"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 230)
    E.frase(c, t, C["s20"] + 0.6, [("substituição", "g", 110, COR)], XE, 370)
    E.frase(c, t, C["s20.a"], ps("um H sai, outro átomo entra", "i", 62, TINTA2), XE, 480, passo=0.1)
    Q.equacao(c, t, C["s20.b"], "CH4 + Cl2 -> CH3Cl + HCl", 640, 720, 76, cores={"Cl": COR})
    E.foco(c, t, C["s20.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 470, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s20.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(770, 495, p), ep(t, C["s20.c"] + 0.2, 0.4))
    E.frase(c, t, C["s20.d"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1520, 990, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, adicao=b_adicao, h2=b_h2, margarina=b_margarina, markov=b_markov,
              erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
