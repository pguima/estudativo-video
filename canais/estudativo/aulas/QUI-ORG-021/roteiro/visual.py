"""Visual — Estudativo · QUI-ORG-021: oxidação de álcoois (vinagre e bafômetro).

Segue a LINGUAGEM VISUAL DA QUÍMICA (cabeçalho de QUI-MIS-001), o complemento da Orgânica de QUI-ORG-015 (estr) e a
linguagem das reações de QUI-ORG-018. Oxidação em fila: álcool → aldeído → ácido, cada estrutura plana ligada pela seta [O]
na cor da matéria; os H que saem ganham círculo e somem; a ligação C=O nova nasce em COR; o nox do carbono do OH fica numa
pílula embaixo de cada etapa. O H do carbono do OH, que decide tudo, fica em COR quando se conta.
Todo instante vem de C[...] (marcadores do roteiro), para acompanhar a voz real quando ela chegar."""
import math

import editorial as E
import quimica as Q
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Química", "Química Orgânica")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_QUI-ORG-021_oxidacao_de_alcoois.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("primario", "secterc", "bafometro", "atalho", "questao", "fim"))

# nox do carbono do OH: H vale +1, O vale −2, C–C não conta; soma das ligações do carbono
nox = lambda h, o_simples, o_dupla: -h + o_simples + 2 * o_dupla
assert nox(2, 1, 0) == -1 and nox(1, 0, 1) == 1 and nox(0, 1, 1) == 3       # etanol, etanal, ácido etanoico
assert Q.contar("CH3CH2OH") == Q.contar("C2H6O") and Q.contar("CH3CHO") == Q.contar("C2H4O") and Q.contar("CH3COOH") == Q.contar("C2H4O2")
assert Q.contar("CH3COCH3") == Q.contar("C3H6O") and Q.contar("CH3COCH2CH3") == Q.contar("C4H8O")
# dicromato: 2 Cr + 7 O(−2) = −2 → Cr = +6
assert (-2 - 7 * (-2)) / 2 == 6


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
LARANJA, VERDE = "#F08A24", "#3FA34D"
# estruturas planas (rótulo, x, y) e ligações; o índice 1 é sempre o carbono do OH
ETANOL = ([("H3C", -1.2, 0), ("C", 0, 0), ("H", 0, -1), ("H", 0, 1), ("O", 1.05, 0), ("H", 1.85, 0)],
          [(0, 1, 1), (1, 2, 1), (1, 3, 1), (1, 4, 1), (4, 5, 1)])
ETANAL = ([("H3C", -1.2, 0), ("C", 0, 0), ("O", 0, -1.05), ("H", 0, 1)], [(0, 1, 1), (1, 2, 2, E.COR), (1, 3, 1)])
ACIDO = ([("H3C", -1.2, 0), ("C", 0, 0), ("O", 0, -1.05), ("OH", 0, 1.05)], [(0, 1, 1), (1, 2, 2), (1, 3, 1)])
PROPANOL = ([("H3C", -1.2, 0), ("C", 0, 0), ("H", 0, -1), ("OH", 0, 1.05), ("CH3", 1.2, 0)], [(0, 1, 1), (1, 2, 1), (1, 3, 1), (1, 4, 1)])
PROPANONA = ([("H3C", -1.2, 0), ("C", 0, 0), ("O", 0, -1.05), ("CH3", 1.2, 0)], [(0, 1, 1), (1, 2, 2, E.COR), (1, 3, 1)])
TERC = ([("H3C", -1.2, 0), ("C", 0, 0), ("CH3", 0, -1.05), ("OH", 0, 1.05), ("CH3", 1.2, 0)], [(0, 1, 1), (1, 2, 1), (1, 3, 1), (1, 4, 1)])
BUTANOL = ([("H3C", -1.2, 0), ("C", 0, 0), ("H", 0, -1), ("OH", 0, 1.05), ("CH2–CH3", 1.75, 0)], [(0, 1, 1), (1, 2, 1), (1, 3, 1), (1, 4, 1)])
BUTANONA = ([("H3C", -1.2, 0), ("C", 0, 0), ("O", 0, -1.05), ("CH2–CH3", 1.75, 0)], [(0, 1, 1), (1, 2, 2, E.COR), (1, 3, 1)])


def mol(c, t, t0, M_, cx, cy, esc=110, size=64, cores=None, a=1.0, escuro=False):
    return estr(c, t, t0, M_[0], M_[1], cx, cy, esc, size, passo=0.06, cores=cores, a=a, escuro=escuro)


def seta_o(c, t, t0, x0, x1, y, escuro=False):
    seta_em(c, t, t0, x0, x1, y + 24, 100, rotulo="[O]", escuro=escuro)


def nox_p(c, t, t0, s, cx, y):
    E.foco(c, t, t0, 0.4, lambda a: E.pilula(c, "nox " + s, cx, y, 46, "g", fundo=E.COR, a=a))


# ---------------- gancho ----------------
def garrafa(c, cx, yb, a=1.0, cor="#7A1F3D"):
    if a <= 0:
        return
    M.rrect(c, cx - 60, yb - 300, 120, 300, 30, cor, a, shadow=True)
    M.rrect(c, cx - 22, yb - 420, 44, 140, 12, cor, a)
    M.rrect(c, cx - 50, yb - 220, 100, 90, 10, "#F3E6C8", a)


def b_gancho(c, t, C, b):
    a1, b1, c1, d1 = C["s01.a"], C["s01.b"], C["s01.c"], C["s01.d"]
    if t < C["s02"]:
        E.foco(c, t, a1, 0.5, lambda a: garrafa(c, 420, 820, a))
        E.foco(c, t, a1 + 0.4, 0.4, lambda a: centro(c, "vinho → vinagre", 420, 900, 56, "g", TINTA, a))
        cor = lambda tt: Q.muda_cor(tt, b1 + 0.8, LARANJA, VERDE, 1.5)
        Q.tubo(c, t, b1, 1450, 820, 110, 380, 0.6, cor, graduacao=False)
        E.foco(c, t, b1 + 0.3, 0.4, lambda a: centro(c, "bafômetro químico", 1450, 900, 56, "g", TINTA, a))
        E.frase(c, t, c1, ps("o mesmo tipo de reação:", "i", 70), W / 2, 200, "center", 0.12)
        E.frase(c, t, d1, [("oxidação", "g", 90, COR), ("do", "i", 90), ("álcool", "g", 90)], W / 2, 340, "center", 0.15)
        return
    tb = C["s02.a"] + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1600, 560, 240 * ease_back(prog(t, tb, 0.8)), giro=8 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 88), XE, 240, passo=0.14)
    lista(c, t, [(C["s02.b"], [("primário", "g", 66, COR)]), (C["s02.c"], [("secundário", "g", 66, COR)]), (C["s02.d"], [("terciário", "g", 66, COR)]),
                 (C["s02.e"], [("vinagre", "g", 66), ("e", "i", 70), ("bafômetro", "g", 66)]),
                 (C["s02.f"], [("atalho", "g", 66, COR), ("de", "i", 70), ("prova", "i", 70)])], XE, 380, 135)


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    if t < C["s04"]:
        E.frase(c, t, C["s03.a"], [("oxidar", "g", 80, COR), ("=", "g", 80, TINTA2)] + ps("perder elétrons, nox sobe", "i", 70), XE, 220, passo=0.12)
        for k, (nome, s, tk) in enumerate((("aldeído", "CH3–CHO", "s03.b"), ("cetona", "CH3–CO–CH3", "s03.c"), ("ácido", "CH3–COOH", "s03.d"))):
            x = 380 + k * 580
            E.foco(c, t, C[tk], 0.4, lambda a, x=x, nome=nome: centro(c, nome, x, 460, 64, "g", COR, a))
            Q.formula_em(c, t, C[tk] + 0.2, s, x, 600, 72, align="center")
        E.foco(c, t, C["s03.b"] + 0.5, 0.4, lambda a: centro(c, "C=O na ponta", 380, 700, 46, "g", TINTA2, a))
        E.foco(c, t, C["s03.c"] + 0.3, 0.4, lambda a: centro(c, "C=O no meio", 960, 700, 46, "g", TINTA2, a))
        return
    E.frase(c, t, C["s04.a"], ps("olhe o", "i", 76) + [("carbono do OH", "g", 72, COR)], XE, 220, passo=0.12)
    for k, (M_, nome, tk) in enumerate(((ETANOL, "primário", "s04.b"), (PROPANOL, "secundário", "s04.c"), (TERC, "terciário", "s04.d"))):
        x = 380 + k * 580
        mol(c, t, C[tk], M_, x, 600, 110, 62, cores={1: COR})
        E.foco(c, t, C[tk] + 0.4, 0.4, lambda a, x=x, nome=nome, k=k: (centro(c, nome, x, 900, 60, "g", COR, a),
                                                                      centro(c, f"{k + 1} carbono" + ("s" if k else "") + " ligado" + ("s" if k else ""), x, 970, 46, "i", TINTA2, a)))


# ---------------- primário: etanol → etanal → ácido ----------------
def b_primario(c, t, C, b):
    E.frase(c, t, C["s05"], ps("etanol, um álcool", "i", 70, TINTA2) + [("primário", "g", 64, COR)], XE, 180, passo=0.12)
    y = 560
    P = mol(c, t, C["s05"] + 0.2, ETANOL, 330, y, 110, 64, cores={2: COR, 5: COR} if t >= C["s05.c"] else None,
            a=1 - 0.5 * ep(t, C["s05.e"], 0.5))
    if t >= C["s05.c"]:
        circ(c, t, C["s05.c"], P[2][0], P[2][1], 44, E.COR)
        circ(c, t, C["s05.c"] + 0.2, P[5][0], P[5][1], 44, E.COR)
    E.foco(c, t, C["s05.a"], 0.4, lambda a: E.pilula(c, "oxidante: o O₂ do ar, com bactérias", W / 2, 300, 44, "g", fundo=TINTA, a=a))
    E.foco(c, t, C["s05.b"], 0.4, lambda a: E.pilula(c, "saem 2 H", 330, 780, 46, "g", fundo=TINTA2, a=a))
    seta_o(c, t, C["s05.d"], 590, 760, y)
    mol(c, t, C["s05.d"] + 0.3, ETANAL, 1000, y, 110, 64)
    E.foco(c, t, C["s05.e"], 0.4, lambda a: centro(c, "etanal (aldeído)", 1000, 780, 50, "g", COR, a))
    seta_o(c, t, C["s06.a"], 1200, 1370, y)
    mol(c, t, C["s06.a"] + 0.3, ACIDO, 1600, y, 110, 64, cores={3: COR})
    E.foco(c, t, C["s06.b"], 0.4, lambda a: centro(c, "ácido etanoico", 1600, 780, 50, "g", COR, a))
    E.foco(c, t, C["s06.c"], 0.4, lambda a: E.pilula(c, "vinagre", 1600, 300, 56, "g", fundo=E.COR, a=a))
    for s, x, tk in (("−1", 330, "s07.a"), ("+1", 1000, "s07.b"), ("+3", 1600, "s07.c")):
        nox_p(c, t, C[tk], s, x, 880)
    E.frase(c, t, C["s07.d"], ps("o nox sobe a cada passo:", "i", 62) + [("oxidação", "g", 58, COR)], W / 2, 1010, "center", 0.1)


# ---------------- secundário e terciário ----------------
def b_secterc(c, t, C, b):
    if t < C["s09"]:
        E.frase(c, t, C["s08.a"], ps("álcool", "i", 70) + [("secundário", "g", 64, COR)], XE, 200, passo=0.12)
        P = mol(c, t, C["s08.a"] + 0.3, PROPANOL, 520, 600, 130, 72, cores={2: COR} if t >= C["s08.b"] else None)
        E.foco(c, t, C["s08.a"] + 0.6, 0.4, lambda a: centro(c, "propan-2-ol", 520, 880, 56, "g", TINTA, a))
        if t >= C["s08.b"]:
            circ(c, t, C["s08.b"], P[2][0], P[2][1], 50, E.COR)
            E.foco(c, t, C["s08.b"] + 0.2, 0.4, lambda a: E.pilula(c, "1 H só", P[2][0] + 160, P[2][1], 44, "g", fundo=E.COR, a=a))
        seta_o(c, t, C["s08.c"], 850, 1050, 600)
        mol(c, t, C["s08.c"] + 0.4, PROPANONA, 1420, 600, 130, 72)
        E.foco(c, t, C["s08.d"], 0.4, lambda a: centro(c, "propanona, a acetona", 1420, 880, 56, "g", COR, a))
        E.foco(c, t, C["s08.e"], 0.4, lambda a: E.pilula(c, "sem H ali: para", 1420, 990, 48, "g", fundo=TINTA, a=a))
        return
    E.frase(c, t, C["s09.a"], ps("álcool", "i", 70) + [("terciário", "g", 64, COR)], XE, 200, passo=0.12)
    P = mol(c, t, C["s09.a"] + 0.3, TERC, 700, 600, 140, 76, cores={1: COR})
    E.foco(c, t, C["s09.a"] + 0.6, 0.4, lambda a: E.pilula(c, "nenhum H no carbono do OH", 700, 900, 48, "g", fundo=E.COR, a=a))
    seta_o(c, t, C["s09.b"], 1050, 1250, 600)
    E.foco(c, t, C["s09.b"] + 0.3, 0.4, lambda a: centro(c, "?", 1450, 640, 140, "g", CINZA, a))
    x_em(c, t, C["s09.c"], 1450, 600, 80, False)
    E.foco(c, t, C["s09.c"] + 0.3, 0.4, lambda a: centro(c, "não oxida", 1450, 760, 64, "g", ERRADO, a))


# ---------------- bafômetro ----------------
def b_bafometro(c, t, C, b):
    E.frase(c, t, C["s10"], [("bafômetro", "g", 90, COR)] + ps("químico", "i", 80), XE, 200, passo=0.12)
    t1 = C["s10.e"]
    cor = lambda tt: Q.muda_cor(tt, t1, LARANJA, VERDE, 1.4)
    Q.tubo(c, t, C["s10.a"], 1500, 900, 140, 520, 0.55, cor, graduacao=False)
    E.foco(c, t, C["s10.a"] + 0.3, 0.4, lambda a: Q.formula(c, "K2Cr2O7", XE, 380, 80, TINTA, a))
    E.foco(c, t, C["s10.a"] + 0.5, 0.4, lambda a: E.pilula(c, "laranja", XE + 520, 355, 48, "g", fundo=LARANJA, a=a))
    E.foco(c, t, C["s10.b"], 0.4, lambda a: E.escreve(c, "etanol do hálito: se oxida", XE, 520, 56, "g", TINTA, a))
    E.foco(c, t, C["s10.c"], 0.4, lambda a: E.escreve(c, "crômio: ganha elétrons, se reduz", XE, 630, 56, "g", TINTA, a))
    E.foco(c, t, C["s10.d"], 0.4, lambda a: Q.formula(c, "Cr: +6 → +3", XE, 780, 80, COR, a))
    E.foco(c, t, C["s10.e"], 0.4, lambda a: (Q.formula(c, "Cr^3+", XE, 920, 80, TINTA, a), E.pilula(c, "verde", XE + 360, 895, 48, "g", fundo=VERDE, a=a)))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s11"], [("cuidado", "g", 96, ERRADO)], XE, 190)
    E.frase(c, t, C["s11.a"], ps("todo álcool oxida?", "i", 74), XE + 450, 190, passo=0.12)
    mol(c, t, C["s11"] + 0.4, TERC, 600, 620, 140, 76, cores={1: COR})
    E.frase(c, t, C["s11.b"], [("terciário", "g", 60), ("→", "g", 60, TINTA2), ("cetona?", "g", 60, ERRADO)], 1150, 480, passo=0.12)
    if t >= C["s11.b"] + 1.0:
        E.risco(c, 1140, 500, 1820, 430, t, C["s11.b"] + 1.0, largura=10)
    E.frase(c, t, C["s11.c"], ps("cetona exige perder", "i", 60) + [("1 H", "g", 56, COR)], 1150, 640, passo=0.1)
    E.frase(c, t, C["s11.d"], ps("o terciário tem", "i", 60) + [("nenhum H", "g", 56, ERRADO)], 1150, 760, passo=0.1)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    E.frase(c, t, C["s12.a"], ps("conte os H do", "i", 72, CLARO) + [("carbono do OH", "g", 68, BR)], W / 2, 170, "center", 0.12)
    linhas = (("s12.b", "2", "aldeído → ácido"), ("s12.c", "1", "cetona"), ("s12.d", "0", "não oxida"))
    for i, (k, n, r) in enumerate(linhas):
        y = 360 + i * 160
        E.foco(c, t, C[k], 0.4, lambda a, n=n, y=y: (E.bola(c, 520, y - 30, 70, a=a), centro(c, n, 520, y - 4, 64, "g", E.SOBRE, a)))
        seta_em(c, t, C[k] + 0.2, 640, 820, y, 80, escuro=True)
        E.foco(c, t, C[k] + 0.4, 0.4, lambda a, r=r, y=y, i=i: E.escreve(c, r, 880, y, 70, "g", ERRADO if i == 2 else BR, a))
    E.frase(c, t, C["s12.e"], ps("cada passo gasta", "i", 64, CLARO) + [("1 H", "g", 60, E.CLARO)] + ps("daquele carbono", "i", 64, CLARO), W / 2, 870, "center", 0.12)
    E.foco(c, t, C["s13.a"], 0.4, lambda a: E.pilula(c, "metanol, com 3 H, vai mais longe: outra aula", W / 2, 990, 44, "g", fundo=E.COR, a=a))


# ---------------- questão e resposta ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s14"], ps("hora de testar", "i", 72, COR), XE, 170)
    mol(c, t, C["s14.a"], BUTANOL, 500, 560, 130, 70)
    E.foco(c, t, C["s14.a"] + 0.5, 0.4, lambda a: centro(c, "butan-2-ol", 540, 840, 56, "g", TINTA, a))
    mol(c, t, C["s14.b"], TERC, 1460, 560, 130, 70)
    E.foco(c, t, C["s14.b"] + 0.5, 0.4, lambda a: centro(c, "2-metilpropan-2-ol", 1460, 840, 56, "g", TINTA, a))
    E.frase(c, t, C["s14.b"] + 1.2, ps("o que se forma ao oxidar cada um?", "i", 64), W / 2, 990, "center", 0.1)
    if t >= C["s15"]:
        E.relogio(c, t, C["s15.a"], cx=1050, cy=500, r=95)


def b_resposta(c, t, C, b):
    E.frase(c, t, C["s16"], ps("resolvendo", "i", 72, COR), XE, 170)
    if t < C["s16.c"] + 0.4:
        P = mol(c, t, None, BUTANOL, 560, 560, 130, 70, cores={2: COR} if t >= C["s16.b"] else {1: COR})
        if t >= C["s16.b"]:
            circ(c, t, C["s16.b"], P[2][0], P[2][1], 50, E.COR)
    else:
        mol(c, t, C["s16.c"] + 0.4, BUTANONA, 560, 560, 130, 70)
    E.foco(c, t, C["s16.a"], 0.4, lambda a: E.pilula(c, "secundário", 560, 330, 46, "g", fundo=TINTA, a=a))
    E.foco(c, t, C["s16.d"], 0.4, lambda a: (centro(c, "butanona", 600, 860, 64, "g", COR, a)))
    x_em(c, t, C["s16.d"] + 0.3, 840, 840, 34, True)
    mol(c, t, None if t >= C["s17"] else -9, TERC, 1420, 560, 130, 70, cores={1: COR} if t >= C["s17.a"] else None, a=ep(t, C["s16"], 0.4))
    E.foco(c, t, C["s17.a"], 0.4, lambda a: E.pilula(c, "terciário", 1420, 330, 46, "g", fundo=TINTA, a=a))
    E.foco(c, t, C["s17.b"], 0.4, lambda a: E.pilula(c, "nenhum H", 1680, 650, 46, "g", fundo=E.COR, a=a))
    x_em(c, t, C["s17.c"], 1420, 870, 44, False)
    E.foco(c, t, C["s17.c"] + 0.2, 0.4, lambda a: E.escreve(c, "não oxida", 1490, 890, 56, "g", ERRADO, a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s18"], [("resumindo", "i", 92, COR)], XE, 170)
        itens = (("s18.a", [("primário", "g", 62, COR), ("→", "g", 62, TINTA2), ("aldeído", "g", 62), ("→", "g", 62, TINTA2), ("ácido", "g", 62)]),
                 ("s18.b", [("secundário", "g", 62, COR), ("→", "g", 62, TINTA2), ("cetona", "g", 62)]),
                 ("s18.c", [("terciário", "g", 62, COR), ("→", "g", 62, TINTA2), ("não", "g", 62, ERRADO), ("oxida", "g", 62)]),
                 ("s18.d", [("vinagre:", "g", 62)] + ps("etanol oxidado até ácido", "i", 66)),
                 ("s18.e", [("bafômetro:", "g", 62)] + ps("o crômio se reduz", "i", 66)))
        for i, (k, partes) in enumerate(itens):
            y = 320 + i * 140
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, XE + 40, y - 26, 44, a=a), centro(c, str(i + 1), XE + 40, y - 4, 54, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, partes, XE + 120, y, passo=0.1)
    E.saida(c, t, C["s19"] - 0.1, resumo)
    if t < C["s19"]:
        return
    E.frase(c, t, C["s19"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 230)
    E.frase(c, t, C["s19.a"], [("ácido", "g", 90, COR), ("+", "g", 90, TINTA2), ("álcool", "g", 90, COR)], XE, 380, passo=0.15)
    E.foco(c, t, C["s19.b"], 0.4, lambda a: E.pilula(c, "→ éster, o cheiro das frutas", XE + 360, 520, 50, "g", fundo=TINTA, a=a))
    E.foco(c, t, C["s19.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 470, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s19.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(770, 495, p), ep(t, C["s19.c"] + 0.2, 0.4))
    E.frase(c, t, C["s19.d"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1520, 990, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, primario=b_primario, secterc=b_secterc, bafometro=b_bafometro, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
