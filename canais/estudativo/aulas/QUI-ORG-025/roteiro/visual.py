"""Visual — Estudativo · QUI-ORG-025: polímeros de adição. Primeira aula do módulo Polímeros.

Segue a LINGUAGEM VISUAL DA QUÍMICA (cabeçalho de QUI-MIS-001), o complemento da Orgânica de QUI-ORG-015 (estr, colchetes) e a
linguagem das reações de QUI-ORG-018.
LINGUAGEM DOS POLÍMEROS (QUI-ORG-025 a 028 copiam daqui):
- MONÔMEROS em fila, cada um em pose de cruz (carbonos na horizontal, ligantes em cima e embaixo); na polimerização (polimeriza)
  a dupla de cada um perde a segunda linha, eles se aproximam e as ligações entre vizinhos nascem na cor da matéria; nas pontas
  da cadeia ficam traços abertos (a cadeia continua).
- UNIDADE QUE SE REPETE entre colchetes (colchetes), com o n pequeno à direita, embaixo; o grupo que diferencia o polímero
  (Cl, F, anel) vai em COR. Fórmula condensada com n: formula_n.
- Monômero ↔ polímero sempre lado a lado, com seta de duas vias quando se ensina o caminho de volta.
Todo instante vem de C[...] (marcadores do roteiro), para acompanhar a voz real quando ela chegar."""
import math

import editorial as E
import quimica as Q
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Química", "Química Orgânica")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_QUI-ORG-025_polimeros_de_adicao.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("poli", "pe", "outros", "atalho", "questao", "fim"))

# monômero e unidade têm os mesmos átomos (na adição, nada sai)
for mono, unid in (("CH2CH2", "C2H4"), ("CH2CHCl", "C2H3Cl"), ("CF2CF2", "C2F4"), ("CH2CHC6H5", "C8H8"), ("CH2CHCH3", "C3H6")):
    assert Q.contar(mono) == Q.contar(unid), mono


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
def polimeriza(c, t, t0, tu, x0, y, k, subs, esc=95, size=56, d=1.6, cores=None, escuro=False, a=1.0, n_ini=3.3, n_fim=2.0):
    """k monômeros em fila; subs = (em cima à esq., embaixo à esq., em cima à dir., embaixo à dir.). Em tu, as duplas abrem e
    eles se ligam. Devolve as posições dos carbonos (lista de pares)"""
    u = ease_io(prog(t, tu, d)) if tu is not None else 0.0
    gap = lerp(n_ini, n_fim, u)
    tinta = Q._tinta(escuro)
    cr = cores or {}
    at, ligs, cs = [], [], []
    for i in range(k):
        cx = (i - (k - 1) / 2) * gap
        b = len(at)
        at += [("C", cx - 0.5, 0), ("C", cx + 0.5, 0), (subs[0], cx - 0.5, -1.05), (subs[1], cx - 0.5, 1.05), (subs[2], cx + 0.5, -1.05), (subs[3], cx + 0.5, 1.05)]
        ordem = 2 if u < 0.45 else 1
        ligs += [(b, b + 1, ordem, E.COR if ordem == 2 else None), (b, b + 2, 1), (b, b + 3, 1), (b + 1, b + 4, 1), (b + 1, b + 5, 1)]
        if u > 0.6 and i < k - 1:
            ligs.append((b + 1, b + 7, 1, E.COR))
        cs.append(b)
    tl = None if t0 is None else [t0 + 0.25 * (j // 6) + 0.05 * (j % 6) for j in range(len(at))]
    cores_ = {j: cr.get(j % 6) for j in range(len(at)) if cr.get(j % 6)}
    P = estr(c, t, t0, at, ligs, x0, y, esc, size, tl=tl, cores=cores_, escuro=escuro, a=a)
    if u > 0.8:
        q = ep(t, tu + d * 0.8, 0.3) if tu is not None else 1
        for j, s in ((cs[0], -1), (cs[-1] + 1, 1)):
            M.line(c, P[j][0] + s * size * 0.45, y, P[j][0] + s * size * 1.3, y, E.COR, q * a, max(5, size * 0.075))
    return [(P[j], P[j + 1]) for j in cs]


def formula_n(c, t, t0, s, x, y, size, align="left", cores=None, escuro=False, cor=None):
    """fórmula da unidade com colchetes e o n pequeno embaixo, à direita"""
    w = Q.formula(None, s, 0, 0, size)
    x0 = x - w / 2 if align == "center" else x
    E.foco(c, t, t0, 0.5, lambda a: (Q.formula(c, s, x0, y, size, cor, a, cores=cores, escuro=escuro),
                                     E.escreve(c, "n", x0 + w + 6, y + size * 0.3, size * 0.6, "g", cor or Q._tinta(escuro), a)))
    return w


def unidade(c, t, t0, cx, cy, subs, esc=110, size=64, cores=None, escuro=False, a=1.0, simples=True):
    """a unidade que se repete, em estrutura plana, com traços abertos e colchetes"""
    at = [("C", -0.5, 0), ("C", 0.5, 0), (subs[0], -0.5, -1.05), (subs[1], -0.5, 1.05), (subs[2], 0.5, -1.05), (subs[3], 0.5, 1.05), ("", -1.35, 0), ("", 1.35, 0)]
    ligs = [(0, 1, 1 if simples else 2, None if simples else ERRADO), (0, 2, 1), (0, 3, 1), (1, 4, 1), (1, 5, 1), (0, 6, 1), (1, 7, 1)]
    P = estr(c, t, t0, at, ligs, cx, cy, esc, size, cores=cores, escuro=escuro, a=a)
    q = 1.0 if t0 is None else ep(t, t0 + 0.5, 0.4)
    colchetes(c, cx - 1.25 * esc, cx + 1.25 * esc, cy, 2.6 * esc, q * a, n="n", size=size * 0.8, escuro=escuro)
    return P


def sacola(c, cx, cy, s, a=1.0):
    if a <= 0:
        return
    M.rrect(c, cx - s * 0.6, cy - s * 0.5, s * 1.2, s * 1.3, s * 0.12, "#F4F6F7", a, shadow=True)
    for dx in (-0.28, 0.28):
        pth = skia.Path(); pth.addArc(skia.Rect.MakeLTRB(cx + (dx - 0.18) * s, cy - s * 0.85, cx + (dx + 0.18) * s, cy - s * 0.2), 180, 180)
        c.drawPath(pth, M.paint("#C9CED3", a, stroke=s * 0.07))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    a1, b1, c1, d1 = C["s01.a"], C["s01.b"], C["s01.c"], C["s01.d"]
    if t < C["s02"]:
        E.foco(c, t, a1, 0.5, lambda a: sacola(c, 360, 560, 300, a))
        E.frase(c, t, a1 + 0.3, ps("fios invisíveis:", "i", 66, TINTA2), 760, 260, passo=0.1)
        E.frase(c, t, b1, [("1", "g", 80, COR), ("fio", "i", 84), ("=", "g", 80, TINTA2), ("1", "g", 80, COR), ("molécula", "i", 84)], 760, 380, passo=0.15)
        polimeriza(c, t, c1, c1 + 0.6, 1300, 700, 4, ("H", "H", "H", "H"), 80, 48)
        E.foco(c, t, c1 + 1.6, 0.4, lambda a: E.pilula(c, "milhares de pedaços iguais", 1300, 900, 46, "g", fundo=TINTA, a=a))
        E.foco(c, t, d1, 0.4, lambda a: E.pilula(c, "o pedaço vem do eteno", 1300, 1000, 50, "g", fundo=E.COR, a=a))
        return
    tb = C["s02.a"] + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1600, 560, 260 * ease_back(prog(t, tb, 0.8)), giro=8 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 88), XE, 260, passo=0.14)
    lista(c, t, [(C["s02.b"], [("monômero", "g", 64, COR), ("de", "i", 68), ("PE,", "g", 64), ("PVC,", "g", 64), ("teflon,", "g", 64), ("isopor", "g", 64)]),
                 (C["s02.c"], [("a", "i", 70), ("cadeia", "g", 66), ("que", "i", 70), ("se", "i", 70), ("repete", "i", 70)]),
                 (C["s02.d"], [("atalho", "g", 66, COR), ("de", "i", 70), ("prova", "i", 70)])], XE, 440, 170)


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], ps("lembre da adição", "i", 72, TINTA2), XE, 200, passo=0.12)
    E.frase(c, t, C["s03.a"], ps("uma ligação da", "i", 70) + [("dupla", "g", 66, COR)] + ps("se abre", "i", 70), XE, 360, passo=0.12)
    E.frase(c, t, C["s03.b"], ps("cada carbono:", "i", 70) + [("uma vaga", "g", 66, COR)], XE, 470, passo=0.12)
    P = alceno(c, t, C["s03.a"] + 0.3, 1400, 760, ("H", "H", "H", "H"), 140, 76, cor_dupla=E.COR)
    if t >= C["s03.b"]:
        for k in range(2):
            circ(c, t, C["s03.b"] + 0.2 * k, P[k][0], P[k][1] - 115, 38, E.COR)


# ---------------- o que é polímero ----------------
def b_poli(c, t, C, b):
    E.frase(c, t, C["s04.a"], [("poli", "g", 150, COR)], XE, 330)
    E.frase(c, t, C["s04.a"] + 0.6, ps("= muitos", "i", 80), XE + 330, 330)
    E.frase(c, t, C["s04.b"], [("mero", "g", 150)], XE, 520)
    E.frase(c, t, C["s04.b"] + 0.5, ps("= parte", "i", 80), XE + 420, 520)
    E.frase(c, t, C["s04.c"], ps("molécula enorme, uma", "i", 62, TINTA2) + [("unidade que se repete", "g", 58)], XE, 680, passo=0.1)
    E.frase(c, t, C["s04.d"], [("monômero", "g", 90, COR)] + ps("= a molécula pequena de partida", "i", 62), XE, 860, passo=0.12)
    E.foco(c, t, C["s04.e"], 0.4, lambda a: E.pilula(c, "mono = uma", 1500, 990, 50, "g", fundo=TINTA, a=a))
    E.foco(c, t, C["s04.a"] + 0.4, 0.6, lambda a: (alceno(c, 0, None, 1500, 400, ("H", "H", "H", "H"), 100, 54, a=a)), blur=10)


# ---------------- polietileno ----------------
def b_pe(c, t, C, b):
    if t < C["s06"]:
        Q.formula_em(c, t, C["s05.a"], "CH2=CH2", W / 2, 220, 90, align="center")
        E.foco(c, t, C["s05.a"], 0.4, lambda a: E.escreve(c, "eteno", XE, 220, 56, "i", TINTA2, a))
        polimeriza(c, t, C["s05.a"] + 0.4, C["s05.b"], W / 2, 620, 4, ("H", "H", "H", "H"), 110, 62, d=2.4)
        E.foco(c, t, C["s05.c"], 0.4, lambda a: E.pilula(c, "as vagas se ligam aos vizinhos", W / 2, 880, 48, "g", fundo=E.COR, a=a))
        E.foco(c, t, C["s05.e"], 0.4, lambda a: E.pilula(c, "a cadeia cresce", W / 2, 990, 52, "g", fundo=TINTA, a=a))
        return
    Pc = polimeriza(c, t, None, -99, W / 2, 400, 3, ("H", "H", "H", "H"), 115, 58)
    if t >= C["s06.a"]:
        q = ep(t, C["s06.a"], 0.4)
        colchetes(c, Pc[1][0][0] - 57, Pc[1][1][0] + 57, 400, 300, q, n="n", size=54)
    formula_n(c, t, C["s06.b"], "[–CH2–CH2–]", W / 2, 720, 110, "center")
    E.foco(c, t, C["s06.c"], 0.4, lambda a: E.pilula(c, "n = quantas vezes se repete", 1560, 600, 44, "g", fundo=TINTA, a=a))
    E.foco(c, t, C["s06.d"], 0.4, lambda a: centro(c, "polietileno: sacolas e frascos", W / 2, 860, 60, "g", COR, a))
    E.foco(c, t, C["s06.e"], 0.4, lambda a: E.pilula(c, "nada sai: polímero de adição", W / 2, 980, 52, "g", fundo=E.COR, a=a))


# ---------------- outros ----------------
def linha_poli(c, t, t0, y, mono, unid, nome, uso, cores):
    Q.formula_em(c, t, t0, mono, 260, y, 60, cores=cores)
    seta_em(c, t, t0 + 0.4, 740, 880, y, 60)
    formula_n(c, t, t0 + 0.7, unid, 930, y, 60, cores=cores)
    E.foco(c, t, t0 + 1.0, 0.4, lambda a: (E.escreve(c, nome, 1540, y - 6, 56, "g", COR, a), E.escreve(c, uso, 1540, y + 50, 40, "i", TINTA2, a)))


def b_outros(c, t, C, b):
    E.frase(c, t, C["s07"], ps("troque um H do eteno, e muda o plástico", "i", 64, TINTA2), XE, 180, passo=0.1)
    linha_poli(c, t, C["s07.a"], 360, "CH2=CHCl", "[–CH2–CHCl–]", "PVC", "canos", {"Cl": COR})
    E.foco(c, t, C["s07.a"] + 0.2, 0.4, lambda a: E.escreve(c, "cloreto de vinila", 260, 420, 40, "i", TINTA2, a))
    linha_poli(c, t, C["s07.d"], 590, "CF2=CF2", "[–CF2–CF2–]", "teflon", "antiaderente", {"F": COR})
    linha_poli(c, t, C["s08.a"], 820, "CH2=CH–C6H5", "[–CH2–CH(C6H5)–]", "poliestireno", "isopor", {"C6H5": COR, 4: COR, 5: COR, 6: COR, 7: COR})
    E.foco(c, t, C["s08.a"] + 0.2, 0.4, lambda a: E.escreve(c, "estireno", 260, 880, 40, "i", TINTA2, a))
    E.foco(c, t, C["s08.c"], 0.4, lambda a: E.pilula(c, "com bolhas de gás: isopor", W / 2, 1000, 48, "g", fundo=E.COR, a=a))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s09"], [("cuidado", "g", 96, ERRADO)], XE, 190)
    E.frase(c, t, C["s09.a"], ps("a dupla fica no colchete?", "i", 74), XE + 450, 190, passo=0.12)
    P = unidade(c, t, C["s09.a"] + 0.3, 620, 600, ("H", "H", "H", "H"), 130, 70, simples=False)
    if t >= C["s09.b"]:
        circ(c, t, C["s09.b"], P[0][0], P[0][1], 70, ERRADO)
        E.foco(c, t, C["s09.b"] + 0.3, 0.4, lambda a: E.pilula(c, "5 ligações!", 620, 920, 50, "g", fundo=ERRADO, a=a))
    E.frase(c, t, C["s09.c"], ps("o carbono só faz", "i", 64) + [("4", "g", 62, COR)], 1150, 460, passo=0.12)
    unidade(c, t, C["s09.d"], 1440, 680, ("H", "H", "H", "H"), 110, 60)
    x_em(c, t, C["s09.d"] + 0.6, 1700, 560, 38, True)
    E.foco(c, t, C["s09.d"] + 0.5, 0.4, lambda a: E.pilula(c, "só ligações simples", 1440, 960, 46, "g", fundo=E.COR, a=a))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    if t < C["s11"]:
        E.frase(c, t, C["s10.a"], [("monômero", "g", 62, BR), ("→", "g", 62, CLARO), ("polímero", "g", 62, BR)], XE, 160, passo=0.12)
        for i, (k, s) in enumerate((("s10.b", "1 apague uma ligação da dupla"), ("s10.c", "2 um traço em cada ponta"), ("s10.d", "3 colchetes e o n"))):
            E.foco(c, t, C[k], 0.4, lambda a, s=s, i=i: E.escreve(c, s, XE, 260 + i * 70, 48, "g", CLARO, a))
        Q.formula_em(c, t, C["s10.b"], "CH2=CHCl", 1300, 330, 76, escuro=True)
        formula_n(c, t, C["s10.d"], "[–CH2–CHCl–]", 1300, 430, 76, escuro=True)
        E.frase(c, t, C["s10.e"], [("polímero", "g", 62, BR), ("→", "g", 62, CLARO), ("monômero", "g", 62, BR)], XE, 640, passo=0.12)
        E.foco(c, t, C["s10.f"], 0.4, lambda a: E.escreve(c, "pegue a unidade de 2 C e devolva a dupla", XE, 740, 48, "g", CLARO, a))
        formula_n(c, t, C["s10.f"] + 0.4, "[–CF2–CF2–]", 560, 900, 76, escuro=True)
        seta_em(c, t, C["s10.f"] + 0.8, 1000, 1160, 900, 76, escuro=True)
        Q.formula_em(c, t, C["s10.f"] + 1.1, "CF2=CF2", 1220, 900, 76, escuro=True, cores={0: E.CLARO, 1: E.CLARO})
        return
    E.frase(c, t, C["s11.a"], ps("O ou N", "g", 66, BR) + ps("ligando as partes da cadeia?", "i", 66, CLARO), W / 2, 400, "center", 0.12)
    pilula_em(c, t, C["s11.b"], "outro tipo: próxima aula", W / 2, 560, 56, E.COR)


# ---------------- questão e resposta ----------------
PP = ("H", "H", "H", "CH3")


def b_questao(c, t, C, b):
    E.frase(c, t, C["s12"], ps("hora de testar", "i", 72, COR), XE, 170)
    E.frase(c, t, C["s12.a"], [("polipropileno", "g", 64)] + ps("dos potes de margarina", "i", 60, TINTA2), XE, 300, passo=0.1)
    formula_n(c, t, C["s12.b"], "[–CH2–CH(CH3)–]", XE, 500, 96, cores={"CH3": COR, 5: COR, 6: COR})
    unidade(c, t, C["s12.b"] + 0.4, 600, 800, PP, 100, 56, cores={5: COR})
    E.frase(c, t, C["s12.c"], ps("qual é o monômero?", "i", 70, COR), 1000, 1000, passo=0.12)
    if t >= C["s13"]:
        E.relogio(c, t, C["s13.a"], cx=1500, cy=520, r=150)


def b_resposta(c, t, C, b):
    E.frase(c, t, C["s14"], ps("resolvendo", "i", 72, COR), XE, 170)
    if t < C["s14.b"]:
        unidade(c, t, None, 560, 560, PP, 120, 64, cores={5: COR}, a=1 - ep(t, C["s14.a"] + 0.8, 0.4) * 0)
        if t >= C["s14.a"]:
            E.risco(c, 380, 620, 450, 500, t, C["s14.a"], largura=8)
            E.risco(c, 670, 620, 740, 500, t, C["s14.a"] + 0.2, largura=8)
    else:
        alceno(c, t, C["s14.b"], 560, 560, PP, 120, 64, cores={5: COR}, cor_dupla=E.COR)
    E.foco(c, t, C["s14.b"], 0.4, lambda a: E.pilula(c, "devolva a dupla", 560, 880, 50, "g", fundo=E.COR, a=a))
    Q.formula_em(c, t, C["s14.c"], "CH2=CH–CH3", 1080, 560, 96, cores={"CH3": COR})
    E.foco(c, t, C["s14.d"], 0.4, lambda a: E.pilula(c, "propeno", 1330, 700, 60, "g", fundo=CERTO, a=a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s15"], [("resumindo", "i", 92, COR)], XE, 170)
        itens = (("s15.a", [("polímero:", "g", 62, COR)] + ps("monômero que se repete", "i", 66)),
                 ("s15.b", [("adição:", "g", 62, COR)] + ps("a dupla abre e nada sai", "i", 66)),
                 ("s15.c", [("eteno", "g", 62), ("→", "g", 62, TINTA2), ("PE;", "g", 62), ("cloreto de vinila", "g", 62), ("→", "g", 62, TINTA2), ("PVC", "g", 62)]),
                 ("s15.d", [("estireno", "g", 62), ("→", "g", 62, TINTA2), ("isopor", "g", 62)]))
        for i, (k, partes) in enumerate(itens):
            y = 320 + i * 150
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, XE + 40, y - 26, 46, a=a), centro(c, str(i + 1), XE + 40, y - 4, 56, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, partes, XE + 120, y, passo=0.1)
    E.saida(c, t, C["s16"] - 0.1, resumo)
    if t < C["s16"]:
        return
    E.frase(c, t, C["s16"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 230)
    E.frase(c, t, C["s16"] + 0.6, [("condensação", "g", 110, COR)], XE, 370)
    E.frase(c, t, C["s16.a"], ps("sai água a cada ligação", "i", 62, TINTA2), XE, 480, passo=0.1)
    E.foco(c, t, C["s16.b"], 0.4, lambda a: E.pilula(c, "PET e náilon", XE + 180, 600, 56, "g", fundo=TINTA, a=a))
    E.foco(c, t, C["s16.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 470, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s16.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(770, 495, p), ep(t, C["s16.c"] + 0.2, 0.4))
    E.frase(c, t, C["s16.d"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1520, 990, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, poli=b_poli, pe=b_pe, outros=b_outros, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
