"""Visual — Estudativo · QUI-ORG-020: reações de eliminação (desidratação do etanol).

Segue a LINGUAGEM VISUAL DA QUÍMICA (cabeçalho de QUI-MIS-001), o complemento da Orgânica de QUI-ORG-015 (estr, alceno) e a
linguagem das reações de QUI-ORG-018. A eliminação é desenhada como a adição de QUI-ORG-018 rodando ao contrário (reacao com
volta=True): o OH e o H vizinho sobem em TINTA2, se juntam em H–OH (a água) e a dupla fecha na cor da matéria.
Todo instante vem de C[...] (marcadores do roteiro), para acompanhar a voz real quando ela chegar."""
import math

import editorial as E
import quimica as Q
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Química", "Química Orgânica")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_QUI-ORG-020_reacoes_de_eliminacao.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("elimina", "etanol", "volta", "atalho", "questao", "fim"))

for eq in ("C2H6O -> C2H4 + H2O", "C2H4 + H2O -> C2H6O", "2 C2H6O -> C4H10O + H2O", "C3H8O -> C3H6 + H2O"):
    assert Q.lados(eq)[0] == Q.lados(eq)[1], eq
assert Q.contar("CH3CH2OH") == Q.contar("C2H6O") and Q.contar("CH3CH(OH)CH3") == Q.contar("C3H8O")
assert Q.contar("CH2CHCH3") == Q.contar("C3H6") and Q.contar("CH3CH2OCH2CH3") == Q.contar("C4H10O")


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
ANTES = [(-1.25, -0.95), (-1.25, 0.95), (1.25, -0.95), (1.25, 0.95)]
DEPOIS = [(-1.8, 0.0), (-0.62, 1.15), (1.8, 0.0), (0.62, 1.15)]
REAG = [(-0.45, -2.0), (0.45, -2.0)]
NOVO = [(-0.62, -1.15), (0.62, -1.15)]


def reacao(c, t, t0, tu, cx, cy, esc, size, subs, pecas=("H", "OH"), volta=False, escuro=False, cores=None, d=1.4, a=1.0, dx=None, cor_p=None):
    """a adição de QUI-ORG-018 nos dois sentidos. volta=True = eliminação: começa no composto em cruz e, a partir de tu,
    as pecas sobem e saem juntas (H–OH) enquanto a dupla fecha. Devolve os pontos: C1, C2, 4 ligantes, 2 peças"""
    u = ease_io(prog(t, tu, d)) if tu is not None else 0.0
    if volta:
        u = 1 - u
    dx = dx or {}
    lig = [(lerp(x0, x1, u) + dx.get(k, 0) * (1 if x1 > 0 else -1) * u, lerp(y0, y1, u)) for k, ((x0, y0), (x1, y1)) in enumerate(zip(ANTES, DEPOIS))]
    nov = [(lerp(x0, x1, u), lerp(y0, y1, u)) for (x0, y0), (x1, y1) in zip(REAG, NOVO)]
    at = [("C", -0.62, 0), ("C", 0.62, 0)] + [(s, x, y) for s, (x, y) in zip(subs, lig)] + [(s, x, y) for s, (x, y) in zip(pecas, nov)]
    ordem = 2 if u < 0.45 else 1
    ligs = [(0, 1, ordem, E.COR if ordem == 2 else None), (0, 2, 1), (0, 3, 1), (1, 4, 1), (1, 5, 1)]
    if u < 0.25:
        ligs.append((6, 7, 1))
    if u > 0.75:
        ligs += [(0, 6, 1), (1, 7, 1)]
    cr = dict(cores or {})
    cp = cor_p or (TINTA2 if volta else (CLARO if escuro else COR))
    cr.setdefault(6, cp); cr.setdefault(7, cp)
    return estr(c, t, t0, at, ligs, cx, cy, esc, size, passo=0.08, cores=cr, escuro=escuro, a=a)


ETANOL_SUBS = ("H", "H", "H", "H")


# ---------------- gancho ----------------
def cana(c, x, y, h, a=1.0):
    """um colmo de cana com nós e duas folhas"""
    if a <= 0:
        return
    for k in range(5):
        M.rrect(c, x - 18, y - h + k * h / 5, 36, h / 5 - 6, 10, "#7FB24A", a)
    for s in (-1, 1):
        pth = skia.Path(); pth.moveTo(x, y - h * 0.9); pth.quadTo(x + s * 120, y - h * 1.1, x + s * 170, y - h * 0.7)
        c.drawPath(pth, M.paint("#5E9A35", a, stroke=10))


def b_gancho(c, t, C, b):
    a1, b1, c1, d1 = C["s01.a"], C["s01.b"], C["s01.c"], C["s01.d"]
    if t < C["s02"]:
        E.frase(c, t, a1, [("2010:", "g", 80, COR)] + ps("plástico feito de cana", "i", 76), XE, 220, passo=0.12)
        E.foco(c, t, a1 + 0.5, 0.5, lambda a: (cana(c, 260, 960, 380, a), cana(c, 350, 980, 340, a)))
        Q.equacao(c, t, b1, "CH3–CH2–OH -> CH2=CH2 + H2O", 1200, 600, 72, tl=[b1, c1, c1 + 0.2, b1 + 0.8, b1 + 1.0], cores={})
        E.foco(c, t, b1 + 0.2, 0.4, lambda a: centro(c, "etanol", 910, 700, 52, "i", TINTA2, a))
        E.foco(c, t, c1 + 0.2, 0.4, lambda a: centro(c, "eteno: vira plástico", 1400, 700, 52, "g", COR, a))
        E.frase(c, t, d1, [("reação", "g", 80), ("de", "i", 84), ("eliminação", "g", 80, COR)], 1230, 900, "center", 0.15)
        return
    tb = C["s02.a"] + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1600, 560, 260 * ease_back(prog(t, tb, 0.8)), giro=8 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 88), XE, 260, passo=0.14)
    lista(c, t, [(C["s02.b"], [("etanol", "g", 66, COR), ("→", "g", 66, TINTA2), ("eteno", "g", 66, COR)]),
                 (C["s02.c"], [("a", "i", 70), ("adição", "g", 66), ("de", "i", 70), ("trás", "i", 70), ("para", "i", 70), ("a", "i", 70), ("frente", "i", 70)]),
                 (C["s02.d"], [("atalho", "g", 66, COR), ("de", "i", 70), ("prova", "i", 70)])], XE, 440, 170)


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], ps("lembre de duas aulas", "i", 70, TINTA2), XE, 190, passo=0.12)
    E.frase(c, t, C["s03.a"], [("álcool:", "g", 90, COR)] + ps("OH num carbono de ligações simples", "i", 62), XE, 340, passo=0.12)
    Q.formula_em(c, t, C["s03.b"], "CH3–CH2–OH", XE, 500, 90, cores={"O": COR})
    E.frase(c, t, C["s03.c"], [("adição:", "g", 80, COR)] + ps("a dupla abre, 2 viram 1", "i", 66), XE, 720, passo=0.12)
    Q.formula_em(c, t, C["s03.c"] + 1.0, "CH2=CH2 + H2 -> CH3–CH3", XE, 880, 76)


# ---------------- o que é eliminação ----------------
def b_elimina(c, t, C, b):
    E.frase(c, t, C["s04"], [("eliminação:", "g", 90, COR)] + ps("o contrário", "i", 76), XE, 200, passo=0.12)
    reacao(c, t, C["s04"] + 0.3, C["s04.a"] + 0.4, W / 2, 700, 150, 80, ETANOL_SUBS, ("H", "OH"), volta=True)
    E.foco(c, t, C["s04.a"] + 0.6, 0.4, lambda a: E.pilula(c, "sai um pedaço pequeno", 1500, 380, 48, "g", fundo=TINTA2, a=a))
    E.foco(c, t, C["s04.b"], 0.4, lambda a: E.pilula(c, "uma vaga em cada carbono", 330, 560, 46, "g", fundo=TINTA, a=a))
    E.foco(c, t, C["s04.c"] + 0.4, 0.4, lambda a: E.pilula(c, "a dupla fecha", 330, 840, 50, "g", fundo=E.COR, a=a))
    E.foco(c, t, C["s04.d"], 0.4, lambda a: E.pilula(c, "entra 1, saem 2", 1560, 900, 56, "g", fundo=TINTA, a=a))


# ---------------- desidratação do etanol ----------------
def b_etanol(c, t, C, b):
    tl = [C["s05"], C["s06.c"] + 0.4, C["s06.e"], C["s06.e"] + 0.3, C["s06.e"] + 0.5]
    Q.equacao(c, t, C["s05"], "CH3–CH2–OH ->{170 °C} CH2=CH2 + H2O", W / 2, 200, 80, tl=tl)
    E.foco(c, t, C["s05.a"], 0.4, lambda a: E.pilula(c, "sai água", 1560, 340, 50, "g", fundo=TINTA2, a=a))
    E.frase(c, t, C["s05.b"], [("desidratação", "g", 72, COR)], XE, 340)
    E.foco(c, t, C["s05.c"], 0.4, lambda a: E.pilula(c, "ácido sulfúrico puxa a água", 560, 1000, 44, "g", fundo=TINTA, a=a))
    tu = C["s06.c"] - 0.3
    P = reacao(c, t, C["s05"] + 0.3, tu, W / 2, 720, 150, 80, ETANOL_SUBS, ("H", "OH"), volta=True,
               cores={7: COR, 6: COR} if t < tu else None)
    if t < tu:
        circ(c, t, C["s06.a"], P[7][0], P[7][1], 70, E.COR)
        circ(c, t, C["s06.b"], P[6][0], P[6][1], 54, E.COR)
        E.foco(c, t, C["s06.b"] + 0.3, 0.4, lambda a: E.pilula(c, "do carbono vizinho", P[6][0] - 300, P[6][1], 42, "g", fundo=E.COR, a=a))
    E.foco(c, t, C["s06.c"] + 0.6, 0.4, lambda a: E.pilula(c, "H + OH = H₂O", W / 2, 360 + 70, 46, "g", fundo=TINTA2, a=a))
    E.foco(c, t, C["s06.e"], 0.4, lambda a: centro(c, "eteno", W / 2 + 420, 760, 64, "g", COR, a))


# ---------------- caminho oposto ----------------
def b_volta(c, t, C, b):
    E.frase(c, t, C["s07"], ps("volte à adição", "i", 72, TINTA2), XE, 180, passo=0.12)
    Q.equacao(c, t, C["s07.a"], "CH2=CH2 + H2O <=> CH3–CH2–OH", W / 2, 360, 84, tl=[C["s07.a"], C["s07.a"] + 0.2, C["s07.a"] + 0.4, C["s07.b"], C["s07.b"] + 0.3])
    E.foco(c, t, C["s07.b"] + 0.4, 0.4, lambda a: E.pilula(c, "adição de água", W / 2, 470, 48, "g", fundo=TINTA, a=a))
    # a mesma molécula, indo e voltando
    ida = t >= C["s07.c"]
    if ida:
        per = 3.2
        k = (t - C["s07.c"]) % (2 * per)
        tu = t - k if k < per else t - (k - per)
        volta = k >= per
        reacao(c, t, None, tu, W / 2, 790, 120, 66, ETANOL_SUBS, ("H", "OH"), volta=volta, d=1.2)
    E.foco(c, t, C["s07.d"], 0.4, lambda a: E.pilula(c, "adição: a dupla abre", 420, 760, 48, "g", fundo=E.COR, a=a))
    E.foco(c, t, C["s07.e"], 0.4, lambda a: E.pilula(c, "eliminação: a dupla fecha", 1500, 760, 48, "g", fundo=TINTA, a=a))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s08"], [("cuidado", "g", 96, ERRADO)], XE, 190)
    E.frase(c, t, C["s08.a"], ps("H do mesmo carbono do OH?", "i", 70), XE + 450, 190, passo=0.12)
    cx, cy, es = 760, 640, 150
    at = [("C", -0.62, 0), ("C", 0.62, 0), ("H", -1.8, 0), ("H", -0.62, -1.15), ("H", -0.62, 1.15), ("H", 1.8, 0), ("OH", 0.62, -1.15), ("H", 0.62, 1.15)]
    ligs = [(0, 1, 1), (0, 2, 1), (0, 3, 1), (0, 4, 1), (1, 5, 1), (1, 6, 1), (1, 7, 1)]
    P = estr(c, t, C["s08"] + 0.3, at, ligs, cx, cy, es, 80, passo=0.06, cores={6: ERRADO, 7: ERRADO} if t >= C["s08.a"] else None)
    if t >= C["s08.b"]:
        circ(c, t, C["s08.b"], P[1][0], P[1][1], 150, ERRADO)
        E.foco(c, t, C["s08.b"] + 0.3, 0.4, lambda a: E.pilula(c, "os dois do mesmo carbono", 1400, 500, 46, "g", fundo=ERRADO, a=a))
        E.foco(c, t, C["s08.c"], 0.4, lambda a: E.pilula(c, "o vizinho fica sem vaga", 1400, 620, 46, "g", fundo=ERRADO, a=a))
        x_em(c, t, C["s08.c"] + 0.4, 1720, 620, 34, False)
    if t >= C["s08.d"]:
        circ(c, t, C["s08.d"], P[3][0], P[3][1], 54, E.COR)
        E.foco(c, t, C["s08.d"] + 0.3, 0.4, lambda a: E.pilula(c, "o H sai do carbono ao lado", 1400, 820, 50, "g", fundo=E.COR, a=a))
        x_em(c, t, C["s08.d"] + 0.6, 1760, 820, 34, True)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    if t < C["s10"]:
        E.frase(c, t, C["s09"], ps("o atalho de prova", "i", 72, CLARO), W / 2, 150, "center", 0.12)
        s, fx, fy, fs = "CH3–CH2–OH", 640, 520, 110
        if t < C["s09.c"]:
            Q.formula_em(c, t, C["s09"] + 0.3, s, fx, fy, fs, align="center", escuro=True)
            G = Q.grupos(s, fx, fy, fs, "center")
            gO = [g for g in G if g["s"] == "O"][0]
            if t >= C["s09.a"]:
                E.risco(c, gO["x0"] - 10, gO["base"] + 10, gO["x0"] + fs * 1.45, gO["topo"] - 10, t, C["s09.a"], largura=9)
            gH = [g for g in G if g["s"] == "H"][0]
            if t >= C["s09.b"]:
                E.risco(c, gH["x0"] - 6, gH["base"] + 10, gH["x1"] + 6, gH["topo"] - 10, t, C["s09.b"], largura=9)
        else:
            Q.formula_em(c, t, C["s09.c"], "CH2=CH2", fx, fy, fs, align="center", escuro=True, cores={0: E.CLARO, 1: E.CLARO})
        E.frase(c, t, C["s09.a"], [("1", "g", 60, CLARO)] + ps("risque o", "i", 66, CLARO) + [("OH", "g", 62, BR)], 1150, 420, passo=0.1)
        E.frase(c, t, C["s09.b"], [("2", "g", 60, CLARO)] + ps("risque um", "i", 66, CLARO) + [("H vizinho", "g", 62, BR)], 1150, 540, passo=0.1)
        E.frase(c, t, C["s09.c"], [("3", "g", 60, CLARO)] + ps("desenhe a", "i", 66, CLARO) + [("dupla", "g", 62, E.CLARO)], 1150, 660, passo=0.1)
        E.foco(c, t, C["s09.d"], 0.4, lambda a: E.pilula(c, "o que você riscou = água", W / 2, 900, 52, "g", fundo=E.COR, a=a))
        return
    E.frase(c, t, C["s10.a"], [("170 °C:", "g", 66, BR)] + ps("eteno", "i", 70, CLARO), XE, 300, passo=0.12)
    E.frase(c, t, C["s10.a"] + 1.2, [("140 °C:", "g", 66, BR)] + ps("éter", "i", 70, CLARO), XE, 420, passo=0.12)
    Q.formula_em(c, t, C["s10.b"], "2 CH3–CH2–OH -> CH3–CH2–O–CH2–CH3 + H2O", W / 2, 600, 66, align="center", escuro=True)
    E.frase(c, t, C["s10.b"] + 0.6, ps("2 moléculas, 1 água só", "i", 60, CLARO), W / 2, 700, "center", 0.1)
    E.frase(c, t, C["s10.c"], ps("dois vizinhos diferentes? podem sair", "i", 60, CLARO) + [("2 alcenos", "g", 58, BR)], W / 2, 880, "center", 0.1)
    E.foco(c, t, C["s10.c"] + 2.0, 0.4, lambda a: E.pilula(c, "em geral, mais o de dupla no meio: outra aula", W / 2, 990, 42, "g", fundo=E.COR, a=a))


# ---------------- questão e resposta ----------------
QS, QX, QY, QF = "CH3–CH(OH)–CH3", W / 2, 420, 110


def b_questao(c, t, C, b):
    E.frase(c, t, C["s11"], ps("hora de testar", "i", 72, COR), XE, 170)
    E.foco(c, t, C["s11"] + 0.6, 0.4, lambda a: E.escreve(c, "propan-2-ol", XE + 520, 170, 62, "g", TINTA, a))
    Q.formula_em(c, t, C["s11.a"], QS, QX, QY, QF, align="center", cores={"O": COR})
    E.frase(c, t, C["s11.b"], [("1", "g", 58, COR)] + ps("que alceno se forma?", "i", 64), XE, 680, passo=0.1)
    E.frase(c, t, C["s11.c"], [("2", "g", 58, COR)] + ps("que molécula pequena sai?", "i", 64), XE, 800, passo=0.1)
    if t >= C["s12"]:
        E.relogio(c, t, C["s12.a"], cx=1480, cy=760, r=150)


PROP = ("H", "H", "H", "CH3")


def b_resposta(c, t, C, b):
    E.frase(c, t, C["s13"], ps("resolvendo", "i", 72, COR), XE, 170)
    tu = C["s13.d"]
    P = reacao(c, t, C["s13"] + 0.2, tu, W / 2, 680, 150, 80, PROP, ("H", "OH"), volta=True, dx={3: 0.25},
               cores={6: COR, 7: COR} if t < tu else None)
    if t < tu:
        circ(c, t, C["s13.a"], P[7][0], P[7][1], 70, E.COR)
        circ(c, t, C["s13.b"], P[6][0], P[6][1], 54, E.COR)
        E.foco(c, t, C["s13.c"], 0.4, lambda a: E.pilula(c, "vizinhos iguais: tanto faz", 420, 860, 44, "g", fundo=TINTA, a=a))
    E.foco(c, t, C["s13.e"], 0.4, lambda a: Q.formula(c, "CH2=CH–CH3", W / 2, 1010, 80, TINTA, a, "center"))
    E.foco(c, t, C["s13.e"] + 0.4, 0.4, lambda a: E.pilula(c, "propeno", W / 2 + 420, 985, 50, "g", fundo=E.COR, a=a))
    E.foco(c, t, C["s14.b"], 0.4, lambda a: E.pilula(c, "água", W / 2 + 280, 380, 56, "g", fundo=CERTO, a=a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s15"], [("resumindo", "i", 92, COR)], XE, 170)
        itens = (("s15.a", [("eliminação:", "g", 62, COR)] + ps("sai um pedaço, a dupla fecha", "i", 66)),
                 ("s15.b", [("etanol", "g", 62), ("→", "g", 62, TINTA2), ("eteno", "g", 62), ("+", "g", 62, TINTA2), ("água", "g", 62)]),
                 ("s15.c", ps("a adição de trás para a frente", "i", 66)))
        for i, (k, partes) in enumerate(itens):
            y = 340 + i * 180
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, XE + 40, y - 26, 46, a=a), centro(c, str(i + 1), XE + 40, y - 4, 56, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, partes, XE + 120, y, passo=0.1)
        reacao(c, t, C["s15.a"] + 0.4, C["s15.a"] + 0.8, 1560, 880, 90, 50, ETANOL_SUBS, ("H", "OH"), volta=True)
    E.saida(c, t, C["s16"] - 0.1, resumo)
    if t < C["s16"]:
        return
    E.frase(c, t, C["s16"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 230)
    E.frase(c, t, C["s16.a"], [("oxidação", "g", 110, COR)], XE, 370)
    E.foco(c, t, C["s16.b"], 0.4, lambda a: E.pilula(c, "vinho → vinagre", XE + 230, 520, 52, "g", fundo=TINTA, a=a))
    E.foco(c, t, C["s16.c"], 0.4, lambda a: E.pilula(c, "bafômetro", XE + 200, 640, 52, "g", fundo=E.COR, a=a))
    E.foco(c, t, C["s16.d"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 470, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s16.d"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(770, 495, p), ep(t, C["s16.d"] + 0.2, 0.4))
    E.frase(c, t, C["s16.e"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1520, 990, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, elimina=b_elimina, etanol=b_etanol, volta=b_volta, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
