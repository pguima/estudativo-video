"""Visual — Estudativo · QUI-ORG-026: polímeros de condensação (PET e náilon).

Segue a LINGUAGEM VISUAL DA QUÍMICA (cabeçalho de QUI-MIS-001) e a LINGUAGEM DOS POLÍMEROS de QUI-ORG-025 (colchetes, n,
formula_n). Condensação em PEÇAS (fila_cond): cada monômero é uma peça com um grupo reativo em cada ponta (COOH em COR, OH ou
NH2 em tinta); quando duas pontas se encaixam, sobe uma bolha H₂O em TINTA2 e a junta vira o grupo novo (éster ou amida) numa
caixa pontilhada. Na fórmula da cadeia, o grupo que se repete fica em COR.
Todo instante vem de C[...] (marcadores do roteiro), para acompanhar a voz real quando ela chegar."""
import math

import editorial as E
import quimica as Q
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Química", "Química Orgânica")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_QUI-ORG-026_polimeros_de_condensacao.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("cond", "pet", "nailon", "erro", "atalho", "questao", "fim"))

# cada ligação nova solta uma água: monômero A + monômero B → unidade + 2 H2O (duas ligações por unidade)
for eq in ("C8H6O4 + C2H6O2 -> C10H8O4 + 2 H2O",              # PET: ácido tereftálico + etilenoglicol
           "C6H10O4 + C6H16N2 -> C12H22N2O2 + 2 H2O",          # náilon 6,6: ácido adípico + hexanodiamina
           "C6H10O4 + C2H6O2 -> C8H12O4 + 2 H2O",              # a questão: ácido adípico + etilenoglicol
           "C2H4O2 + C2H6O -> C4H8O2 + H2O"):                  # o erro: ácido etanoico + etanol, um éster só
    assert Q.lados(eq)[0] == Q.lados(eq)[1], eq


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


# (peças copiadas de QUI-ORG-025)
def formula_n(c, t, t0, s, x, y, size, align="left", cores=None, escuro=False, cor=None):
    """fórmula da unidade com colchetes e o n pequeno embaixo, à direita"""
    w = Q.formula(None, s, 0, 0, size)
    x0 = x - w / 2 if align == "center" else x
    E.foco(c, t, t0, 0.5, lambda a: (Q.formula(c, s, x0, y, size, cor, a, cores=cores, escuro=escuro),
                                     E.escreve(c, "n", x0 + w + 6, y + size * 0.3, size * 0.6, "g", cor or Q._tinta(escuro), a)))
    return w


# ---------------- peças desta aula ----------------
def peca(c, cx, cy, w, meio, esq, dir_, cor_e=None, cor_d=None, a=1.0, h=110, size=46):
    """um monômero como peça de montar: o miolo e um grupo reativo em cada ponta (None = ponta sem grupo)"""
    if a <= 0:
        return
    M.rrect(c, cx - w / 2, cy - h / 2, w, h, 22, "#FFFFFF", a, shadow=True)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2, cy - h / 2, w, h), 22, 22), M.paint(FIO, a, stroke=3))
    Q.formula(c, meio, cx, cy + size * 0.36, size, TINTA, a, "center")
    for s, g, cr in ((-1, esq, cor_e), (1, dir_, cor_d)):
        if g:
            gw = Q.formula(None, g, 0, 0, size) + 30
            x = cx + s * (w / 2 + gw / 2 - 4)
            M.rrect(c, x - gw / 2, cy - h * 0.32, gw, h * 0.64, 14, cr or E.COR, a)
            Q.formula(c, g, x, cy + size * 0.36, size, BR, a, "center")


def fila_cond(c, t, t0, tu, pecas, cx, cy, gap0=420, gap1=330, w=220, d=1.6, rotulo="éster"):
    """fila de peças que se encaixam a partir de tu; cada encaixe solta uma bolha H₂O e ganha a caixa do grupo novo"""
    u = ease_io(prog(t, tu, d)) if tu is not None else 0.0
    gap1 = w + 190  # as pontas se encostam
    gap0 = gap1 + 110
    gap = lerp(gap0, gap1, u)
    k = len(pecas)
    xs = [cx + (i - (k - 1) / 2) * gap for i in range(k)]
    for i, (x, p) in enumerate(zip(xs, pecas)):
        q = 1.0 if t0 is None else ep(t, t0 + 0.25 * i, 0.4)
        peca(c, x, cy, w, *p, a=q)
    if u > 0.6:
        for i in range(k - 1):
            xm = (xs[i] + xs[i + 1]) / 2
            b = ep(t, tu + d * 0.6 + 0.1 * i, 0.9) if tu is not None else 1
            if b < 1:
                E.pilula(c, "H₂O", xm, cy - 90 - 120 * b, 40, "g", fundo=TINTA2, a=1 - b)
            qq = ep(t, tu + d * 0.8, 0.4) if tu is not None else 1
            jun = "CO–O" if rotulo == "éster" else "CO–NH"
            jw = Q.formula(None, jun, 0, 0, 46) + 40
            M.rrect(c, xm - jw / 2, cy - 40, jw, 80, 16, "#FFFFFF", qq)
            Q.formula(c, jun, xm, cy + 16, 46, COR, qq, "center")
            E.caixa_pontilhada(c, xm - jw / 2 - 14, cy - 60, jw + 28, 120, qq, E.COR, prog_=qq)
            E.foco(c, t, (tu or -9) + d * 0.9, 0.3, lambda a, xm=xm: centro(c, rotulo, xm, cy + 120, 40, "g", COR, a))
    return xs


ACIDO_T = ("C6H4", "HOOC", "COOH")
GLICOL = ("CH2–CH2", "HO", "OH")
ADIPICO = ("(CH2)4", "HOOC", "COOH")
DIAMINA = ("(CH2)6", "H2N", "NH2")
PET = "[–CO–C6H4–CO–O–CH2–CH2–O–]"
NAILON = "[–CO–(CH2)4–CO–NH–(CH2)6–NH–]"
QPOLI = "[–CO–(CH2)4–CO–O–CH2–CH2–O–]"


def ac(p):
    return (p[0], p[1], p[2], E.COR, E.COR)


def al(p):
    return (p[0], p[1], p[2], TINTA, TINTA)


# ---------------- gancho ----------------
def garrafa_pet(c, cx, yb, h, a=1.0):
    if a <= 0:
        return
    w = h * 0.36
    M.rrect(c, cx - w / 2, yb - h * 0.8, w, h * 0.8, w * 0.3, "#CFEDEA", a * 0.9, shadow=True)
    M.rrect(c, cx - w * 0.2, yb - h, w * 0.4, h * 0.25, 10, "#CFEDEA", a * 0.9)
    M.rrect(c, cx - w * 0.24, yb - h * 1.04, w * 0.48, h * 0.08, 8, E.COR, a)


def b_gancho(c, t, C, b):
    a1, b1, c1 = C["s01.a"], C["s01.b"], C["s01.c"]
    if t < C["s02"]:
        E.foco(c, t, a1, 0.5, lambda a: garrafa_pet(c, 520, 900, 520, a))
        E.foco(c, t, a1 + 0.5, 0.4, lambda a: centro(c, "PET", 520, 980, 56, "g", TINTA, a))
        E.foco(c, t, a1 + 0.8, 0.5, lambda a: (M.rrect(c, 1250, 420, 260, 460, 80, "#E9DCC8", a, shadow=True), centro(c, "náilon", 1380, 980, 56, "g", TINTA, a)))
        E.frase(c, t, b1, ps("a cada ligação nova da cadeia", "i", 64, TINTA2), W / 2, 200, "center", 0.1)
        E.foco(c, t, c1, 0.5, lambda a: E.pilula(c, "sai uma água", W / 2, 320, 70, "g", fundo=E.COR, a=a))
        return
    tb = C["s02.a"] + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1600, 560, 260 * ease_back(prog(t, tb, 0.8)), giro=8 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 88), XE, 260, passo=0.14)
    lista(c, t, [(C["s02.b"], [("PET", "g", 66, COR), ("e", "i", 70), ("náilon", "g", 66, COR)]),
                 (C["s02.c"], [("o", "i", 70), ("éster", "g", 66), ("e", "i", 70), ("a", "i", 70), ("amida", "g", 66)]),
                 (C["s02.d"], [("a", "i", 70), ("molécula", "i", 70), ("que", "i", 70), ("sai", "g", 66)]),
                 (C["s02.e"], [("atalho", "g", 66, COR), ("de", "i", 70), ("prova", "i", 70)])], XE, 420, 150)


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], ps("lembre de duas aulas", "i", 70, TINTA2), XE, 190, passo=0.12)
    Q.formula_em(c, t, C["s03.a"], "ácido + álcool -> éster + H2O", XE, 340, 72)
    E.foco(c, t, C["s03.b"], 0.4, lambda a: (E.escreve(c, "éster:", XE, 480, 64, "g", COR, a), Q.formula(c, "–COO–", XE + 240, 480, 80, TINTA, a, cores={0: COR, 1: COR, 2: COR})))
    E.foco(c, t, C["s03.c"], 0.4, lambda a: E.escreve(c, "amida:", XE, 660, 64, "g", COR, a))
    Q.formula_em(c, t, C["s03.d"], "–CO–NH–", XE + 260, 660, 80, cores={0: COR, 1: COR, 2: COR, 3: COR})


# ---------------- condensação ----------------
def b_cond(c, t, C, b):
    if t < C["s05"]:
        E.frase(c, t, C["s04"], [("condensação", "g", 100, COR)], XE, 220)
        E.frase(c, t, C["s04.a"], ps("cada ligação nova solta uma", "i", 64) + [("molécula pequena", "g", 60, COR)], XE, 340, passo=0.1)
        fila_cond(c, t, C["s04.a"] + 0.3, C["s04.a"] + 1.4, [ac(ACIDO_T), al(GLICOL)], W / 2, 620)
        E.frase(c, t, C["s04.b"], ps("uma ligação só não faz cadeia", "i", 60, TINTA2), XE, 880, passo=0.1)
        E.frase(c, t, C["s04.c"], ps("cada monômero:", "i", 62) + [("um grupo em cada ponta", "g", 58, COR)], XE, 990, passo=0.1)
        return
    E.frase(c, t, C["s05.a"], ps("peças com encaixe nas duas pontas", "i", 66), XE, 220, passo=0.1)
    fila_cond(c, t, C["s05.a"] + 0.3, C["s05.b"], [ac(ACIDO_T), al(GLICOL), ac(ACIDO_T), al(GLICOL)], W / 2, 520, 470, 360, 170)
    E.foco(c, t, C["s05.b"] + 1.6, 0.4, lambda a: E.pilula(c, "a fila cresce", W / 2, 720, 50, "g", fundo=E.COR, a=a))
    E.foco(c, t, C["s05.c"], 0.4, lambda a: peca(c, W / 2 - 150, 900, 200, "CH2–CH3", "HO", None, TINTA, a=a))
    E.foco(c, t, C["s05.c"] + 0.4, 0.4, lambda a: E.pilula(c, "encaixe numa ponta só: fecha a fila", W / 2 + 400, 900, 44, "g", fundo=ERRADO, a=a))


# ---------------- PET ----------------
def b_pet(c, t, C, b):
    if t < C["s07"]:
        E.frase(c, t, C["s06"], ps("o PET junta duas peças", "i", 70, TINTA2), XE, 200, passo=0.12)
        E.foco(c, t, C["s06.a"], 0.4, lambda a: peca(c, 660, 460, 240, *ac(ACIDO_T), a=a))
        E.foco(c, t, C["s06.a"] + 0.5, 0.4, lambda a: centro(c, "ácido tereftálico", 660, 600, 50, "g", COR, a))
        E.foco(c, t, C["s06.b"], 0.4, lambda a: peca(c, 660, 780, 240, *al(GLICOL), a=a))
        E.foco(c, t, C["s06.b"] + 0.5, 0.4, lambda a: centro(c, "etilenoglicol", 660, 920, 50, "g", TINTA, a))
        E.foco(c, t, C["s06.a"] + 0.6, 0.5, lambda a: (anel(c, 1460, 520, 120, a, giro=0), centro(c, "C6H4: um anel de benzeno", 1460, 720, 44, "i", TINTA2, a)))
        return
    fila_cond(c, t, C["s07"], C["s07.a"], [ac(ACIDO_T), al(GLICOL), ac(ACIDO_T)], W / 2, 420, 470, 400, 230)
    formula_n(c, t, C["s07.d"], PET, W / 2, 760, 70, "center", cores={k: COR for k in (0, 1, 4, 5, 6)})
    E.foco(c, t, C["s07.d"] + 0.5, 0.4, lambda a: E.pilula(c, "poliéster", W / 2, 860, 56, "g", fundo=E.COR, a=a))
    E.foco(c, t, C["s07.e"], 0.4, lambda a: centro(c, "PET = poli(tereftalato de etileno)", W / 2, 990, 50, "i", TINTA2, a))


# ---------------- náilon ----------------
def b_nailon(c, t, C, b):
    E.frase(c, t, C["s08"], [("náilon", "g", 90, COR)], XE, 200)
    E.foco(c, t, C["s08.a"], 0.4, lambda a: E.escreve(c, "hexanodiamina", 1300, 200, 50, "g", TINTA, a))
    E.foco(c, t, C["s08.b"], 0.4, lambda a: E.escreve(c, "+ ácido adípico", 820, 200, 50, "g", COR, a))
    fila_cond(c, t, C["s08.a"], C["s08.c"], [ac(ADIPICO), al(DIAMINA), ac(ADIPICO)], W / 2, 440, 470, 410, 230, rotulo="amida")
    formula_n(c, t, C["s09.a"], NAILON, W / 2, 760, 66, "center")
    E.foco(c, t, C["s09.a"] + 0.5, 0.4, lambda a: E.pilula(c, "poliamida", W / 2, 860, 56, "g", fundo=E.COR, a=a))
    E.foco(c, t, C["s09.b"], 0.4, lambda a: E.pilula(c, "náilon 6,6: seis carbonos em cada monômero", W / 2, 980, 46, "g", fundo=TINTA, a=a))


# ---------------- comparar ----------------
def b_compara(c, t, C, b):
    E.frase(c, t, C["s10.a"], ps("compare com a aula anterior", "i", 70, TINTA2), XE, 200, passo=0.12)
    for k, (tk, nome, s1, s2) in enumerate((("s10.b", "adição", "a dupla abre", "nada sai"), ("s10.c", "condensação", "dois grupos reagem", "sai água"))):
        x = 520 + k * 880
        E.foco(c, t, C[tk], 0.4, lambda a, x=x, nome=nome: centro(c, nome, x, 460, 90, "g", COR, a))
        E.foco(c, t, C[tk] + 0.4, 0.4, lambda a, x=x, s1=s1: centro(c, s1, x, 600, 60, "i", TINTA, a))
        E.foco(c, t, C[tk] + 0.8, 0.4, lambda a, x=x, s2=s2, k=k: E.pilula(c, s2, x, 740, 60, "g", fundo=TINTA if k == 0 else E.COR, a=a))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s11"], [("cuidado", "g", 96, ERRADO)], XE, 190)
    E.frase(c, t, C["s11.a"], ps("qualquer ácido + álcool faz polímero?", "i", 64), XE + 450, 190, passo=0.1)
    fila_cond(c, t, C["s11.b"], C["s11.b"] + 0.8, [("CH3", None, "COOH", E.COR, E.COR), ("CH2–CH3", "HO", None, TINTA, TINTA)], W / 2, 520, 420, 330, 200)
    E.foco(c, t, C["s11.b"] + 0.4, 0.4, lambda a: centro(c, "ácido etanoico + etanol", W / 2, 360, 50, "i", TINTA2, a))
    E.foco(c, t, C["s11.c"], 0.4, lambda a: E.pilula(c, "1 grupo cada", W / 2, 760, 50, "g", fundo=TINTA, a=a))
    E.foco(c, t, C["s11.d"], 0.4, lambda a: E.pilula(c, "não sobra ponta: um éster só", W / 2, 880, 52, "g", fundo=ERRADO, a=a))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    E.frase(c, t, C["s12.a"], ps("procure", "i", 70, CLARO) + [("COO", "g", 66, BR)] + ps("ou", "i", 70, CLARO) + [("CO–NH", "g", 66, BR)] + ps("que se repete", "i", 70, CLARO), W / 2, 170, "center", 0.12)
    formula_n(c, t, C["s12.a"] + 0.6, PET, W / 2, 360, 70, "center", escuro=True, cores={k: E.CLARO for k in (0, 1, 4, 5, 6)})
    E.foco(c, t, C["s12.b"], 0.4, lambda a: E.pilula(c, "condensação: saiu água", W / 2, 470, 52, "g", fundo=E.COR, a=a))
    E.frase(c, t, C["s12.c"], ps("monômeros: corte ali e", "i", 64, CLARO) + [("devolva a água", "g", 60, BR)], W / 2, 640, "center", 0.12)
    E.frase(c, t, C["s12.d"], [("C=O", "g", 58, E.CLARO)] + ps("ganha OH:", "i", 62, CLARO) + [("ácido", "g", 58, BR)], W / 2, 770, "center", 0.12)
    E.frase(c, t, C["s12.e"], [("o outro lado", "g", 58, E.CLARO)] + ps("ganha H:", "i", 62, CLARO) + [("álcool ou amina", "g", 58, BR)], W / 2, 880, "center", 0.12)


# ---------------- questão e resposta ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s13"], ps("hora de testar", "i", 72, COR), XE, 170)
    formula_n(c, t, C["s13.a"], QPOLI, W / 2, 400, 80, "center")
    E.frase(c, t, C["s13.c"], [("1", "g", 58, COR)] + ps("que grupo se repete?", "i", 62), XE, 620, passo=0.1)
    E.frase(c, t, C["s13.d"], [("2", "g", 58, COR)] + ps("que molécula saiu?", "i", 62), XE, 730, passo=0.1)
    E.frase(c, t, C["s13.e"], [("3", "g", 58, COR)] + ps("quais são os monômeros?", "i", 62), XE, 840, passo=0.1)
    if t >= C["s14"]:
        E.relogio(c, t, C["s14.a"], cx=1480, cy=730, r=150)


def b_resposta(c, t, C, b):
    E.frase(c, t, C["s15"], ps("resolvendo", "i", 72, COR), XE, 170)
    formula_n(c, t, -9, QPOLI, W / 2, 330, 76, "center", cores={k: COR for k in (0, 1, 4, 5, 6)} if t >= C["s15.a"] else None)
    E.foco(c, t, C["s15.a"], 0.4, lambda a: E.pilula(c, "CO–O: éster", W / 2 - 300, 440, 48, "g", fundo=E.COR, a=a))
    E.foco(c, t, C["s15.b"], 0.4, lambda a: E.pilula(c, "poliéster: saiu água", W / 2 + 300, 440, 48, "g", fundo=TINTA, a=a))
    E.foco(c, t, C["s15.c"], 0.4, lambda a: peca(c, 640, 680, 230, *ac(ADIPICO), a=a))
    E.foco(c, t, C["s15.c"] + 0.4, 0.4, lambda a: centro(c, "ácido adípico", 640, 810, 50, "g", COR, a))
    E.foco(c, t, C["s15.d"], 0.4, lambda a: peca(c, 1380, 680, 230, *al(GLICOL), a=a))
    E.foco(c, t, C["s15.d"] + 0.4, 0.4, lambda a: centro(c, "etilenoglicol", 1380, 810, 50, "g", TINTA, a))
    x_em(c, t, C["s15.d"] + 1.0, W / 2, 940, 40, True)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s16"], [("resumindo", "i", 92, COR)], XE, 170)
        itens = (("s16.a", [("condensação:", "g", 62, COR)] + ps("cada ligação solta água", "i", 66)),
                 ("s16.b", [("PET", "g", 62), ("=", "g", 62, TINTA2), ("poliéster", "g", 62, COR)]),
                 ("s16.c", [("náilon", "g", 62), ("=", "g", 62, TINTA2), ("poliamida", "g", 62, COR)]),
                 ("s16.d", ps("monômero com grupos nas duas pontas", "i", 66)))
        for i, (k, partes) in enumerate(itens):
            y = 320 + i * 150
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, XE + 40, y - 26, 46, a=a), centro(c, str(i + 1), XE + 40, y - 4, 56, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, partes, XE + 120, y, passo=0.1)
    E.saida(c, t, C["s17"] - 0.1, resumo)
    if t < C["s17"]:
        return
    E.frase(c, t, C["s17"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 230)
    E.frase(c, t, C["s17.a"], ps("polímeros da natureza:", "i", 70) + [("amido, borracha", "g", 64, COR)], XE, 370, passo=0.1)
    E.foco(c, t, C["s17.b"], 0.4, lambda a: E.pilula(c, "qual plástico se recicla derretendo?", XE + 400, 520, 46, "g", fundo=TINTA, a=a))
    E.foco(c, t, C["s17.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 470 + 200, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s17.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(970, 695, p), ep(t, C["s17.c"] + 0.2, 0.4))
    E.frase(c, t, C["s17.d"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1520, 990, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, cond=b_cond, pet=b_pet, nailon=b_nailon, compara=b_compara,
              erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
