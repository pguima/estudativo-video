"""Visual — Estudativo · QUI-ORG-016: isomeria óptica, carbono quiral.

Segue a LINGUAGEM VISUAL DA QUÍMICA (cabeçalho de QUI-MIS-001) e o complemento da Orgânica de QUI-ORG-015 (estr, alceno).
Nesta aula: o carbono quiral leva um asterisco na cor da matéria; os quatro ligantes diferentes ganham, cada um, uma caixa
no instante da fala; as duas formas de espelho ficam sempre dos dois lados de espelho() (faixa azulada tracejada), com a
da direita desenhada pelo espelhamento da da esquerda, para que a imagem seja de fato a do espelho.
Todo instante vem de C[...] (marcadores do roteiro), para acompanhar a voz real quando ela chegar."""
import math

import editorial as E
import quimica as Q
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Química", "Química Orgânica")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_QUI-ORG-016_isomeria_optica_carbono_quiral.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("maos", "quiral", "contar", "erro", "atalho", "questao", "fim"))

# as contas e fórmulas da aula
assert 2 ** 3 == 2 * 2 * 2 == 8 and [2 ** n for n in (1, 2, 3)] == [2, 4, 8] and 2 ** 4 == 16 and 2 ** 2 == 4
assert Q.contar("CH3CH(OH)COOH") == Q.contar("C3H6O3")                      # ácido lático
assert Q.contar("CH3CH(OH)CH3") == Q.contar("C3H8O")                        # propan-2-ol
assert Q.contar("CH3CH(OH)CH2CH3") == Q.contar("C4H10O")                    # butan-2-ol
assert Q.contar("CH3CH(OH)CH(OH)CH2CH3") == Q.contar("C5H12O2")             # pentano-2,3-diol, a questão


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
PELE, PELE2 = "#E9B892", "#B9825C"


def mao(c, cx, cy, s, espelha=False, a=1.0):
    """mão aberta vista pela palma; espelha = a outra mão"""
    if a <= 0:
        return
    c.save(); c.translate(cx, cy)
    if espelha:
        c.scale(-1, 1)

    def peca(x, y, w, h, r, ang=0):
        c.save(); c.rotate(ang, x * s, y * s)
        rr = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH((x - w / 2) * s, (y - h) * s, w * s, h * s), r * s, r * s)
        c.drawRRect(rr, M.paint(PELE, a)); c.drawRRect(rr, M.paint(PELE2, a, stroke=4))
        c.restore()
    for x, h in ((-0.68, 1.15), (-0.23, 1.4), (0.23, 1.5), (0.68, 1.3)):
        peca(x, 0.1, 0.4, h, 0.2)
    peca(1.0, 1.05, 0.46, 1.05, 0.22, 48)  # polegar
    rr = skia.RRect.MakeRectXY(skia.Rect.MakeLTRB(-0.92 * s, -0.25 * s, 0.92 * s, 1.35 * s), 0.38 * s, 0.38 * s)
    c.drawRRect(rr, M.paint(PELE, a)); c.drawRRect(rr, M.paint(PELE2, a, stroke=4))
    c.restore()


def polegar(cx, cy, s, espelha=False):
    """centro aproximado do polegar desenhado por mao()"""
    return cx + (-1 if espelha else 1) * 1.35 * s, cy + 0.6 * s


# carbono com quatro ligantes em perspectiva: em cima, à esquerda, à direita e na frente (embaixo)
TETRA = [(0, -1.05), (-1.0, 0.35), (1.0, 0.35), (0.3, 0.95)]


def tetra(c, t, t0, cx, cy, esc, grupos, espelha=False, escuro=False, a=1.0, tl=None, rotulos=True, r=None):
    """grupos = [(rótulo, elemento da cor), ...] nas posições de TETRA; o centro é o carbono (escuro). Devolve os pontos"""
    s = -1 if espelha else 1
    pts = [(cx + s * x * esc, cy + y * esc) for x, y in TETRA]
    r = r or esc * 0.3
    ts = tl or [t0 + 0.15 * (k + 1) for k in range(4)] if t0 is not None else [-99] * 4
    for k, (P, (rt, el)) in enumerate(zip(pts, grupos)):
        p = 1.0 if t0 is None else ease_out(prog(t, ts[k], 0.4))
        if p > 0:
            M.line(c, cx, cy, lerp(cx, P[0], p), lerp(cy, P[1], p), "#9AA0A8", a, esc * 0.09)
    for k, (P, (rt, el)) in enumerate(sorted(zip(pts, grupos), key=lambda z: z[0][1])):
        kk = pts.index(P)
        q = 1.0 if t0 is None else ease_back(prog(t, ts[kk], 0.45))
        if q > 0:
            cr = el if el.startswith("#") else None
            Q.atomo(c, P[0], P[1], r * (1.12 if kk == 3 else 1) * q, "C" if cr else el, a * min(1, q), rotulo=False, escuro=escuro, cor=cr)
            if rotulos and len(rt) <= 2 and rt != "OH":
                rot(c, rt, P[0], P[1], r * 0.62, BR if el != "H" else TINTA, a * min(1, q))
            elif rotulos:  # grupo de várias letras: o nome fica do lado de fora da bolinha
                ux, uy = E._uni(cx, cy, P[0], P[1])
                sz = max(40, esc * 0.3)
                w_, h_ = _meia(rt, sz)
                rot(c, rt, P[0] + ux * (r + w_ * abs(ux) + h_ * abs(uy) + 10), P[1] + uy * (r + h_ + 6), sz, Q._tinta(escuro), a * min(1, q))
    q = 1.0 if t0 is None else ease_back(prog(t, t0, 0.45))
    if q > 0:
        Q.atomo(c, cx, cy, r * 0.95 * q, "C", a * min(1, q), escuro=escuro)
    return pts


LATICO = [("H", "H"), ("OH", "O"), ("CH3", "C"), ("COOH", "#7A5BB0")]
GENERICO = [("H", "H"), ("F", "F"), ("Cl", "Cl"), ("Br", "Br")]


def asterisco(c, t, t0, x, y, size=70, cor=None):
    E.foco(c, t, t0, 0.4, lambda a: E.escreve(c, "*", x, y, size, "g", cor or COR, a))


def capsula(c, cx, cy, w, a=1.0):
    """cápsula de remédio deitada, metade branca e metade turquesa"""
    if a <= 0:
        return
    h = w * 0.38
    c.save(); c.rotate(-18, cx, cy)
    M.rrect(c, cx - w / 2, cy - h / 2, w, h, h / 2, "#FFFFFF", a, shadow=True)
    c.save(); c.clipRect(skia.Rect.MakeLTRB(cx, cy - h, cx + w, cy + h))
    M.rrect(c, cx - w / 2, cy - h / 2, w, h, h / 2, E.COR, a)
    c.restore()
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2, cy - h / 2, w, h), h / 2, h / 2), M.paint(TINTA2, 0.5 * a, stroke=3))
    c.restore()


def giro_luz(c, t, t0, cx, cy, r, horario=True, cor=None, a_=1.0):
    """seta curva: a luz desviada para a direita (horário) ou para a esquerda"""
    p = ease_out(prog(t, t0, 0.6))
    if p <= 0:
        return
    cr = cor or E.COR
    ini, var = (200, 140) if horario else (-20, -140)
    pth = skia.Path(); pth.addArc(skia.Rect.MakeLTRB(cx - r, cy - r, cx + r, cy + r), ini, var * p)
    c.drawPath(pth, M.paint(cr, a_, stroke=8))
    if p > 0.95:
        ang = math.radians(ini + var)
        x, y = cx + r * math.cos(ang), cy + r * math.sin(ang)
        tx, ty = -math.sin(ang) * (1 if horario else -1), math.cos(ang) * (1 if horario else -1)
        F = [(x + tx * 26, y + ty * 26), (x - ty * 16, y + tx * 16), (x + ty * 16, y - tx * 16)]
        pth = skia.Path(); pth.moveTo(*F[0]); pth.lineTo(*F[1]); pth.lineTo(*F[2]); pth.close()
        c.drawPath(pth, M.paint(cr, a_))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    a1, b1, c1, d1 = C["s01.a"], C["s01.b"], C["s01.c"], C["s01.d"]
    if t < C["s02"]:
        E.frase(c, t, a1, [("1957", "g", 200, COR)], XE, 330)
        E.frase(c, t, a1 + 0.8, ps("um calmante usado contra o enjoo na gravidez", "i", 54, TINTA2), XE, 430, passo=0.08)
        E.frase(c, t, b1, [("talidomida", "g", 110)], XE, 600)

        def remedio():
            E.foco(c, t, b1, 0.6, lambda a: capsula(c, 1450, 480, 420, a))
        E.saida(c, t, d1 - 0.1, remedio)
        E.frase(c, t, c1, ps("cerca de", "i", 66) + [("10 mil", "g", 66, ERRADO)] + ps("bebês com malformações", "i", 66), XE, 790, passo=0.1)
        if t >= d1:
            tetra(c, t, d1, 1240, 520, 130, GENERICO)
            E.foco(c, t, d1 + 0.3, 0.5, lambda a: espelho(c, 1500, 300, 760, a))
            tetra(c, t, d1 + 0.6, 1760, 520, 130, GENERICO, espelha=True)
            E.frase(c, t, d1 + 0.6, ps("uma gêmea no espelho", "i", 66, COR), XE, 950, passo=0.12)
        return
    tb = C["s02.a"] + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1550, 560, 280 * ease_back(prog(t, tb, 0.8)), giro=8 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 88), XE, 280, passo=0.14)
    lista(c, t, [(C["s02.b"], [("achar", "i", 74), ("o", "i", 74), ("carbono quiral", "g", 70, COR)]),
                 (C["s02.c"], [("contar", "i", 74), ("os", "i", 74), ("isômeros", "g", 70), ("com", "i", 74), ("2ⁿ", "g", 70, COR)]),
                 (C["s02.d"], [("o", "i", 74), ("caso", "i", 74), ("da", "i", 74), ("talidomida", "g", 70)])], XE, 460, 170)


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], ps("você vai precisar de", "i", 70, TINTA2), XE, 200, passo=0.12)
    E.frase(c, t, C["s03.a"], [("isômeros", "g", 110, COR)], XE, 360)
    E.frase(c, t, C["s03.a"] + 0.8, [("mesma", "i", 66), ("fórmula molecular,", "g", 60)], XE + 660, 320, passo=0.12)
    E.frase(c, t, C["s03.a"] + 1.8, [("estruturas", "g", 60), ("diferentes", "i", 66)], XE + 660, 400, passo=0.12)
    E.frase(c, t, C["s03.b"], [("potência", "g", 110, COR)], XE, 640)
    E.formula_em(c, t, C["s03.b"] + 1.0, "2^3 = 2 · 2 · 2 =", XE, 850, 120, "g", TINTA)
    w = E.formula(None, "2^3 = 2 · 2 · 2 =", 0, 0, 120, a=0)
    bola_txt(c, t, C["s03.c"], "8", XE + w + 100, 810, 76, 100)


# ---------------- mãos ----------------
MX1, MX2, MY, MS = 620, 1300, 560, 120


def b_maos(c, t, C, b):
    if t < C["s05"]:
        E.frase(c, t, C["s04"] + 0.2, ps("olhe para as suas mãos", "i", 76), W / 2, 170, "center", 0.12)
        E.foco(c, t, C["s04.a"], 0.5, lambda a: mao(c, MX1, MY, MS, True, a))
        E.foco(c, t, C["s04.a"] + 0.3, 0.5, lambda a: mao(c, MX2, MY, MS, False, a))
        E.saida(c, t, C["s04.d"], lambda: E.frase(c, t, C["s04.a"] + 0.6, ps("mesmas partes, mesma ordem", "i", 60, TINTA2), W / 2, 960, "center", 0.1))
        E.foco(c, t, C["s04.b"], 0.5, lambda a: espelho(c, (MX1 + MX2) / 2, 330, 800, a))
        # encaixar uma sobre a outra: a esquerda desliza até a direita
        u = ease_io(prog(t, C["s04.c"], 1.2))
        if u > 0:
            c.saveLayerAlpha(None, int(150))
            mao(c, lerp(MX1, MX2, u), MY, MS, True, 1)
            c.restore()
        if t >= C["s04.d"]:
            for esp in (True, False):
                circ(c, t, C["s04.d"] + (0 if esp else 0.25), *polegar(MX2, MY, MS, esp), 90, ERRADO)
            E.foco(c, t, C["s04.d"] + 0.5, 0.4, lambda a: E.pilula(c, "polegar do lado errado", MX2, 1040 - 80, 46, "g", fundo=ERRADO, a=a))
        return
    mao(c, 420, 600, 95, True, 1 - ep(t, C["s05"] + 2.5, 0.5) * 0)
    mao(c, 840, 600, 95, False)
    E.frase(c, t, C["s05"], ps("a luva da direita não serve na esquerda", "i", 60, TINTA2), XE, 200, passo=0.1)
    E.frase(c, t, C["s05.a"], [("quiral", "g", 170, COR)], 1180, 560)
    E.frase(c, t, C["s05.a"] + 0.6, ps("não se encaixa na", "i", 56, TINTA2), 1180, 660, passo=0.1)
    E.frase(c, t, C["s05.a"] + 1.2, ps("própria imagem do espelho", "i", 56, TINTA2), 1180, 730, passo=0.1)
    E.foco(c, t, C["s05.b"], 0.5, lambda a: E.pilula(c, "do grego: mão", 1440, 880, 56, "g", fundo=E.COR, a=a))


# ---------------- carbono quiral ----------------
def b_quiral(c, t, C, b):
    if t < C["s07"]:
        def s06():
            E.frase(c, t, C["s06.a"], [("carbono", "g", 130, COR)], XE, 330)
            E.frase(c, t, C["s06.a"] + 0.5, [("quiral", "g", 130, COR)], XE, 470)
            E.frase(c, t, C["s06.b"], [("4", "g", 70, COR)] + ps("ligantes diferentes", "i", 74), XE, 640, passo=0.12)
            E.frase(c, t, C["s06.c"], ps("todos por", "i", 66, TINTA2) + [("ligação simples", "g", 62)], XE, 750, passo=0.12)
            P = tetra(c, t, C["s06.b"], 1450, 560, 170, GENERICO, rotulos=True)
            asterisco(c, t, C["s06.d"], 1490, 560, 110)
            E.foco(c, t, C["s06.d"], 0.5, lambda a: (Q.formula(c, "C", XE, 960, 120, TINTA, a), E.escreve(c, "*", XE + 92, 920, 110, "g", COR, a)))
            E.frase(c, t, C["s06.d"] + 0.4, ps("na fórmula", "i", 60, TINTA2), XE + 220, 950)
        E.saida(c, t, C["s07"] - 0.1, s06)
        return
    if t < C["s08"]:
        def s07():
            E.frase(c, t, C["s07"], ps("o ácido lático, do iogurte", "i", 66, TINTA2), XE, 160, passo=0.12)
            Q.formula_em(c, t, C["s07.a"], "CH3–CH(OH)–COOH", W / 2, 320, 110, align="center")
            cx, cy, es = W / 2, 690, 175
            at = [("C", 0, 0), ("H", 0, -1), ("H3C", -1.15, 0), ("COOH", 1.3, 0), ("OH", 0, 1)]
            ks = {1: "s07.b", 4: "s07.c", 2: "s07.d", 3: "s07.e"}
            cores = {i: COR for i, k in ks.items() if t >= C[k]}
            P = estr(c, t, C["s07.a"] + 0.6, at, [(0, 1, 1), (0, 2, 1), (0, 3, 1), (0, 4, 1)], cx, cy, es, 90, cores=cores)
            for i, k in ks.items():
                caixa_rot(c, t, C[k], P[i], at[i][0], 90, E.COR)
            asterisco(c, t, C["s07.f"], cx + 38, cy - 42, 90)
            E.foco(c, t, C["s07.f"] + 0.3, 0.4, lambda a: E.pilula(c, "4 diferentes: quiral", 1560, 1010, 50, "g", fundo=E.COR, a=a))
        E.saida(c, t, C["s08"] - 0.1, s07)
        return
    # s08: as duas formas de espelho; iguais em quase tudo, diferentes na luz polarizada
    tetra(c, t, C["s08.a"], 620, 470, 140, LATICO)
    E.foco(c, t, C["s08.b"], 0.5, lambda a: espelho(c, W / 2, 250, 700, a))
    tetra(c, t, C["s08.b"] + 0.3, 1300, 470, 140, LATICO, espelha=True)
    E.frase(c, t, C["s08.a"], [("2", "g", 70, COR)] + ps("formas", "i", 74), XE, 190, passo=0.12)

    def iguais():
        E.frase(c, t, C["s08.c"], ps("ferver, derreter, dissolver:", "i", 62, TINTA2) + [("iguais", "g", 60, COR)], W / 2, 860, "center", 0.1)
    E.saida(c, t, C["s08.d"] - 0.1, iguais)
    E.frase(c, t, C["s08.d"], [("luz polarizada", "g", 64, COR)], W / 2, 860, "center")
    giro_luz(c, t, C["s08.e"], 620, 470, 250, True)
    E.foco(c, t, C["s08.e"] + 0.3, 0.4, lambda a: centro(c, "para a direita", 620, 980, 52, "g", TINTA, a))
    giro_luz(c, t, C["s08.f"], 1300, 470, 250, False)
    E.foco(c, t, C["s08.f"] + 0.3, 0.4, lambda a: centro(c, "para a esquerda", 1300, 980, 52, "g", TINTA, a))


# ---------------- talidomida ----------------
def b_talidomida(c, t, C, b):
    E.frase(c, t, C["s09"], ps("no corpo, as moléculas também são", "i", 64, TINTA2) + [("quirais", "g", 60, COR)], W / 2, 180, "center", 0.1)
    E.frase(c, t, C["s09.a"] + 0.6, [("talidomida", "g", 90)], W / 2, 300, "center")
    tetra(c, t, C["s09.b"] - 0.4, 560, 560, 130, GENERICO)
    E.foco(c, t, C["s09.b"], 0.5, lambda a: espelho(c, W / 2, 380, 760, a))
    tetra(c, t, C["s09.c"] - 0.4, 1360, 560, 130, GENERICO, espelha=True)
    E.foco(c, t, C["s09.b"] + 0.3, 0.4, lambda a: E.pilula(c, "acalmava", 560, 860, 56, "g", fundo=E.COR, a=a))
    E.foco(c, t, C["s09.c"] + 0.3, 0.4, lambda a: E.pilula(c, "malformações", 1360, 860, 56, "g", fundo=ERRADO, a=a))
    if t >= C["s09.d"]:
        seta_em(c, t, C["s09.d"], 800, 1120, 600, 110, eq=True, cor=TINTA)
        E.frase(c, t, C["s09.d"] + 0.4, ps("o corpo transforma uma na outra", "i", 62) , W / 2, 990, "center", 0.1)


# ---------------- contar: 2 elevado a n ----------------
def b_contar(c, t, C, b):
    if t < C["s11"]:
        def s10():
            E.frase(c, t, C["s10"], ps("a conta", "i", 80, COR), XE, 190)
            E.frase(c, t, C["s10.a"], ps("cada carbono quiral:", "i", 66) + [("2 jeitos", "g", 62, COR)], XE, 320, passo=0.12)
            linhas = (("s10.b", "1", "2", "2"), ("s10.c", "2", "2 · 2", "4"), ("s10.d", "3", "2 · 2 · 2", "8"))
            for i, (k, n, conta, r) in enumerate(linhas):
                y = 520 + i * 160
                E.foco(c, t, C[k], 0.4, lambda a, n=n, y=y: (E.escreve(c, n, XE + 40, y, 90, "g", COR, a), E.escreve(c, "C*", XE + 120, y, 70, "g", TINTA, a)))
                E.formula_em(c, t, C[k] + 0.3, conta + " =", 900, y, 84, "g", TINTA2, "right")
                bola_txt(c, t, C[k] + 0.6, r, 990, y - 30, 56, 70)
                E.foco(c, t, C[k] + 0.7, 0.4, lambda a, y=y: E.escreve(c, "isômeros", 1070, y, 64, "i", TINTA, a))
        E.saida(c, t, C["s11"] - 0.1, s10)
        return
    E.frase(c, t, C["s11"], [("n", "g", 70, COR)] + ps("carbonos quirais diferentes", "i", 66), XE, 200, passo=0.12)
    E.formula_em(c, t, C["s11.a"], "2^n", W / 2 - 200, 540, 260, "g", COR, "center")
    E.frase(c, t, C["s11.a"] + 0.6, ps("isômeros ópticos", "i", 76), W / 2 + 20, 500, passo=0.12)
    E.frase(c, t, C["s11.b"], ps("glicose, em cadeia aberta:", "i", 62, TINTA2) + [("4", "g", 60, COR), ("C*", "g", 60)], XE, 820, passo=0.1)
    E.formula_em(c, t, C["s11.c"], "2^4 =", 1380, 830, 100, "g", TINTA, "right")
    bola_txt(c, t, C["s11.c"] + 0.4, "16", 1490, 800, 72, 84)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s12"], [("cuidado", "g", 96, ERRADO)], XE, 190)
    E.frase(c, t, C["s12.a"], ps("todo C com OH no meio é quiral?", "i", 66), XE + 450, 190, passo=0.1)
    cx, cy, es = 700, 620, 165
    butan = t >= C["s13.d"]
    direita = "CH2–CH3" if butan else "CH3"
    at = [("C", 0, 0), ("H", 0, -1), ("H3C", -1.15, 0), (direita, 1.8 if butan else 1.15, 0), ("OH", 0, 1)]
    cores = {2: COR, 3: COR} if C["s13.b"] <= t < C["s13.d"] else ({3: COR} if butan else None)
    P = estr(c, t, C["s12.b"] + 0.4, at, [(0, 1, 1), (0, 2, 1), (0, 3, 1), (0, 4, 1)], cx, cy, es, 86, cores=cores)
    nome = "butan-2-ol" if butan else "propan-2-ol"
    E.foco(c, t, C["s12.b"], 0.4, lambda a: centro(c, nome, cx, 940, 64, "g", COR if butan else TINTA, a))
    caixa_rot(c, t, C["s13.a"], P[1], "H", 86, TINTA2, t1=C["s13.b"])
    caixa_rot(c, t, C["s13.a"] + 0.2, P[4], "OH", 86, TINTA2, t1=C["s13.b"])
    caixa_rot(c, t, C["s13.b"], P[2], "H3C", 86, E.COR, t1=C["s13.d"])
    caixa_rot(c, t, C["s13.b"] + 0.2, P[3], "CH3", 86, E.COR, t1=C["s13.d"])
    if t < C["s13.d"]:
        def nao():
            x_em(c, t, C["s13.c"], 1300, 560, 52, False)
            E.frase(c, t, C["s13.c"] + 0.2, ps("2 ligantes iguais:", "i", 62), 1380, 540, passo=0.1)
            E.frase(c, t, C["s13.c"] + 0.8, [("não", "g", 62, ERRADO), ("é", "i", 66), ("quiral", "g", 62)], 1380, 640, passo=0.1)
        nao()
        return
    asterisco(c, t, C["s13.e"], cx + 36, cy - 40, 84)
    x_em(c, t, C["s13.e"], 1360, 560, 52, True)
    E.frase(c, t, C["s13.e"] + 0.2, ps("4 diferentes:", "i", 62), 1440, 540, passo=0.1)
    E.frase(c, t, C["s13.e"] + 0.6, [("quiral", "g", 66, COR)], 1440, 640)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    if t < C["s15"]:
        def s14():
            E.frase(c, t, C["s14"], ps("o atalho de prova", "i", 72, CLARO), W / 2, 150, "center", 0.12)
            E.frase(c, t, C["s14.a"], [("risque", "g", 66, BR)] + ps("os que nunca são quirais", "i", 70, CLARO), W / 2, 270, "center", 0.1)
            E.frase(c, t, C["s14.b"], [("1", "g", 60, CLARO)] + ps("carbono de", "i", 64, CLARO) + [("dupla ou tripla", "g", 60, BR)], XE, 420, passo=0.1)
            E.frase(c, t, C["s14.c"], [("2", "g", 60, CLARO)] + ps("carbono com", "i", 64, CLARO) + [("2 ou 3 H", "g", 60, BR)], XE, 530, passo=0.1)
            Q.formula_em(c, t, C["s14.c"] + 0.4, "CH2", 1250, 530, 70, escuro=True)
            Q.formula_em(c, t, C["s14.c"] + 0.6, "CH3", 1450, 530, 70, escuro=True)
            s, fx, fy, fs = "CH3–CH(OH)–CH2–CH3", W / 2, 800, 110
            Q.formula_em(c, t, C["s14.d"] - 0.6, s, fx, fy, fs, align="center", escuro=True)
            G = [g for g in Q.grupos(s, fx, fy, fs, "center") if g["s"] == "C"]
            for k, i in enumerate((0, 2, 3)):
                g = G[i]
                if t >= C["s14.d"] + 0.2 * k:
                    E.risco(c, g["x0"] - 10, g["base"] + 10, g["x0"] + fs * 1.3, g["topo"] - 10, t, C["s14.d"] + 0.2 * k, largura=8)
            circ(c, t, C["s14.d"] + 0.8, G[1]["x0"] + fs * 0.35, fy - fs * 0.35, 80, E.CLARO)
            E.foco(c, t, C["s14.d"] + 1.0, 0.4, lambda a: centro(c, "sobra 1 para testar", W / 2, 990, 50, "g", BR, a))
        E.saida(c, t, C["s15"] - 0.1, s14)
        return
    E.frase(c, t, C["s15.a"], ps("molécula", "i", 76, CLARO) + [("simétrica?", "g", 70, BR)], W / 2, 380, "center", 0.12)
    E.formula_em(c, t, C["s15.a"] + 1.0, "2^n", W / 2, 640, 200, "g", BR, "center")
    if t >= C["s15.a"] + 1.8:
        E.risco(c, W / 2 - 160, 660, W / 2 + 160, 460, t, C["s15.a"] + 1.8, largura=12)
    pilula_em(c, t, C["s15.b"], "o número real é menor: outra aula", W / 2, 850, 50, E.COR)


# ---------------- questão ----------------
QS, QX, QYF, QFS = "CH3–CH(OH)–CH(OH)–CH2–CH3", W / 2, 470, 104


def numeros_c(c, t, t0, s, fx, fy, fs, escuro=False):
    G = [g for g in Q.grupos(s, fx, fy, fs, "center") if g["s"] == "C"]
    for k, g in enumerate(G):
        x = g["x0"] + fs * 0.36
        E.foco(c, t, t0 + 0.15 * k, 0.4, lambda a, x=x, k=k: (E.bola(c, x, fy - fs - 36, 30, a=a), centro(c, str(k + 1), x, fy - fs - 22, 38, "g", E.SOBRE, a)))
    return G


def b_questao(c, t, C, b):
    E.frase(c, t, C["s16"], ps("hora de testar", "i", 72, COR), XE, 170)
    Q.formula_em(c, t, C["s16.a"], QS, QX, QYF, QFS, align="center", cores={"O": COR})
    numeros_c(c, t, C["s16.a"] + 0.6, QS, QX, QYF, QFS)
    E.frase(c, t, C["s16.b"], [("1", "g", 58, COR)] + ps("quantos carbonos quirais?", "i", 64), XE, 720, passo=0.1)
    E.frase(c, t, C["s16.c"], [("2", "g", 58, COR)] + ps("quantos isômeros ópticos?", "i", 64), XE, 830, passo=0.1)
    if t >= C["s17"]:
        E.relogio(c, t, C["s17.a"], cx=1520, cy=780, r=170)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    Q.formula(c, QS, QX, QYF, QFS, TINTA, 1, "center", cores={"O": COR})
    G = numeros_c(c, t, -9, QS, QX, QYF, QFS)
    for k, i in enumerate((0, 3, 4)):
        g = G[i]
        if t >= C["s18.a"] + 0.25 * k:
            E.risco(c, g["x0"] - 10, g["base"] + 10, g["x0"] + QFS * 1.3, g["topo"] - 10, t, C["s18.a"] + 0.25 * k, largura=8)
    for k, (i, tk, lig) in enumerate(((1, "s18.b", "H, OH, CH3, resto da cadeia"), (2, "s18.c", "H, OH, CH2–CH3, outro lado"))):
        x = G[i]["x0"] + QFS * 0.36
        circ(c, t, C[tk], x, QYF - QFS * 0.35, 76, E.COR)
        asterisco(c, t, C[tk] + 0.4, x + 30, QYF - QFS * 0.75, 70)
        y = 690 + k * 110
        E.foco(c, t, C[tk] + 0.3, 0.4, lambda a, k=k, y=y: centro(c, f"C{k + 2}", XE + 50, y, 60, "g", COR, a))
        E.foco(c, t, C[tk] + 0.5, 0.4, lambda a, lig=lig, y=y: Q.formula(c, lig, XE + 130, y, 52, TINTA, a))
        x_em(c, t, C[tk] + 1.2, 1120, y - 18, 30, True)
    E.frase(c, t, C["s19.a"], [("2", "g", 66, COR), ("C*", "g", 66)] + ps("e metades diferentes", "i", 66), XE, 960, passo=0.12)
    E.formula_em(c, t, C["s19.b"], "2^2 =", 1460, 960, 100, "g", TINTA, "right")
    bola_txt(c, t, C["s19.c"], "4", 1570, 930, 70, 90, CERTO)
    E.foco(c, t, C["s19.c"] + 0.3, 0.4, lambda a: E.escreve(c, "isômeros", 1660, 960, 56, "i", TINTA, a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s20"], [("resumindo", "i", 92, COR)], XE, 170)
        itens = (("s20.a", [("carbono quiral", "g", 64), ("=", "g", 64, TINTA2), ("4", "g", 64, COR), ("ligantes diferentes", "i", 68)]),
                 ("s20.b", [("cada", "i", 68), ("um:", "i", 68), ("2 formas", "g", 64, COR), ("de", "i", 68), ("espelho", "i", 68)]),
                 ("s20.c", [("n", "g", 64, COR), ("quirais", "i", 68), ("→", "g", 64, TINTA2), ("2ⁿ", "g", 64, COR), ("isômeros", "i", 68)]))
        for i, (k, partes) in enumerate(itens):
            y = 340 + i * 170
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, XE + 40, y - 26, 46, a=a), centro(c, str(i + 1), XE + 40, y - 4, 56, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, partes, XE + 120, y, passo=0.12)
        tetra(c, t, C["s20.b"] + 0.4, 1320, 860, 110, GENERICO)
        E.foco(c, t, C["s20.b"] + 0.6, 0.4, lambda a: espelho(c, 1510, 720, 1000, a))
        tetra(c, t, C["s20.b"] + 0.8, 1700, 860, 110, GENERICO, espelha=True)
    E.saida(c, t, C["s21"] - 0.1, resumo)
    if t < C["s21"]:
        return
    E.frase(c, t, C["s21"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C["s21"] + 0.6, [("praticando", "g", 110, COR)], XE, 390)
    E.frase(c, t, C["s21.a"], ps("ebulição, solubilidade, isomerias", "i", 62, TINTA2), XE, 500, passo=0.1)
    E.foco(c, t, C["s21.b"], 0.5, lambda a: capsula(c, 520, 760, 300, a))
    E.foco(c, t, C["s21.b"] + 0.4, 0.4, lambda a: E.pilula(c, "remédios e alimentos", 560, 960, 50, "g", fundo=TINTA, a=a))
    E.foco(c, t, C["s21.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 470, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s21.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(770, 495, p), ep(t, C["s21.c"] + 0.2, 0.4))
    E.frase(c, t, C["s21.d"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1520, 990, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, maos=b_maos, quiral=b_quiral, talidomida=b_talidomida, contar=b_contar,
              erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
