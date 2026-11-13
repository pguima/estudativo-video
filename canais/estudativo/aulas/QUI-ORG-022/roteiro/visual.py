"""Visual — Estudativo · QUI-ORG-022: esterificação e hidrólise de ésteres.

Segue a LINGUAGEM VISUAL DA QUÍMICA (cabeçalho de QUI-MIS-001), o complemento da Orgânica de QUI-ORG-015 (estr) e a
linguagem das reações de QUI-ORG-018. Pose da esterificação (ester): ácido à esquerda com o OH apontando para a direita,
álcool à direita com o H apontando para a esquerda; o OH do ácido e o H do álcool descem em TINTA2 e viram H–OH; o O do
álcool encosta no carbono do ácido e a ligação nova nasce em COR. volta=True roda a hidrólise. No nome, a parte do ácido
fica em COR e a do álcool em TINTA, sempre nessa ordem.
Todo instante vem de C[...] (marcadores do roteiro), para acompanhar a voz real quando ela chegar."""
import math

import editorial as E
import quimica as Q
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Química", "Química Orgânica")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_QUI-ORG-022_esterificacao_e_hidrolise.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("ester", "nome", "volta", "atalho", "questao", "fim"))

for eq in ("CH3COOH + CH3CH2OH -> CH3COOCH2CH3 + H2O", "CH3CH2CH2COOH + CH3CH2OH -> CH3CH2CH2COOCH2CH3 + H2O",
           "HCOOH + CH3CH2OH -> HCOOCH2CH3 + H2O", "CH3COOH + CH3CH2CH2CH2OH -> CH3COOCH2CH2CH2CH3 + H2O"):
    assert Q.lados(eq)[0] == Q.lados(eq)[1], eq
assert Q.contar("CH3CH2CH2COOCH2CH3") == Q.contar("CH3COOCH2CH2CH2CH3") == Q.contar("C6H12O2")
NOMES = dict(etanoico="etanoato", metanoico="metanoato", butanoico="butanoato")
assert all(v == k[:-3] + "ato" for k, v in NOMES.items()) and "etanol"[:-4] + "ila" == "etila" and "butanol"[:-4] + "ila" == "butila"


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
def ester(c, t, t0, tu, cx, cy, esc, size, R="H3C", R2="CH2–CH3", volta=False, d=1.6, escuro=False, a=1.0, x2=None):
    """ácido R–C(=O)–OH + H–O–R2 → R–C(=O)–O–R2 + H–OH. Devolve os pontos (R, C, O=, OH, H, O, R2)"""
    u = ease_io(prog(t, tu, d)) if tu is not None else 0.0
    if volta:
        u = 1 - u
    wR = _meia(R, size)[0] / esc
    w2 = (x2 if x2 is not None else _meia(R2, size)[0] / esc + 0.55)
    at = [(R, -0.75 - wR, 0), ("C", 0, 0), ("O", 0, -1.05), ("OH", lerp(1.1, 1.25, u), lerp(0, 1.45, u)),
          ("H", lerp(2.15, 0.5, u), lerp(0, 1.45, u)), ("O", lerp(2.85, 1.05, u), 0), (R2, lerp(2.85, 1.05, u) + w2, 0)]
    ligs = [(0, 1, 1), (1, 2, 2), (5, 6, 1)]
    if u < 0.3:
        ligs += [(1, 3, 1), (4, 5, 1)]
    if u > 0.7:
        ligs += [(1, 5, 1, E.COR), (4, 3, 1)]
    tl = [t0, t0 + 0.1, t0 + 0.2, t0 + 0.3, t0 + 0.5, t0 + 0.6, t0 + 0.7] if t0 is not None else None
    return estr(c, t, t0, at, ligs, cx, cy, esc, size, tl=tl, cores={3: TINTA2, 4: TINTA2}, escuro=escuro, a=a)


def nome_partes(c, t, t0, p1, p2, cx, y, size=90):
    """nome do éster: a parte do ácido (COR) + "de" + a do álcool"""
    E.frase(c, t, t0, [(p1, "g", size, COR), ("de", "i", size * 1.05), (p2, "g", size)], cx, y, "center", 0.3)


# ---------------- gancho ----------------
def abacaxi(c, cx, cy, s, a=1.0):
    if a <= 0:
        return
    for k, ang in enumerate((-30, -10, 10, 30)):
        c.save(); c.rotate(ang, cx, cy - s * 0.9)
        M.rrect(c, cx - s * 0.12, cy - s * 1.6, s * 0.24, s * 0.8, s * 0.12, "#3E8E41", a)
        c.restore()
    M.rrect(c, cx - s * 0.55, cy - s * 0.95, s * 1.1, s * 1.6, s * 0.5, "#E9A73B", a, shadow=True)
    for i in range(4):
        for j in range(3):
            E.escreve(c, "×", cx - s * 0.35 + j * s * 0.3, cy - s * 0.55 + i * s * 0.33, s * 0.28, "g", "#B97A22", a)


def b_gancho(c, t, C, b):
    a1, b1, c1, d1 = C["s01.a"], C["s01.b"], C["s01.c"], C["s01.d"]
    if t < C["s02"]:
        E.foco(c, t, a1, 0.5, lambda a: abacaxi(c, 1500, 560, 260, a))
        E.frase(c, t, a1, ps("cheiro de abacaxi, sem abacaxi", "i", 70), XE, 240, passo=0.1)
        E.frase(c, t, c1, [("ácido", "g", 90, COR), ("+", "g", 90, TINTA2), ("álcool", "g", 90, COR)], XE, 480, passo=0.2)
        E.frase(c, t, d1, [("butanoato", "g", 84, COR), ("de", "i", 88), ("etila", "g", 84)], XE, 720, passo=0.2)
        Q.formula_em(c, t, d1 + 1.0, "CH3–CH2–CH2–COO–CH2–CH3", XE, 860, 64)
        return
    tb = C["s02.a"] + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1600, 560, 260 * ease_back(prog(t, tb, 0.8)), giro=8 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 88), XE, 260, passo=0.14)
    lista(c, t, [(C["s02.b"], [("ácido", "g", 64, COR), ("+", "g", 64, TINTA2), ("álcool", "g", 64, COR), ("→", "g", 64, TINTA2), ("éster", "g", 64), ("+", "g", 64, TINTA2), ("água", "g", 64)]),
                 (C["s02.c"], [("o", "i", 70), ("caminho", "i", 70), ("de", "i", 70), ("volta", "g", 66)]),
                 (C["s02.d"], [("o", "i", 70), ("nome", "g", 66), ("do", "i", 70), ("éster", "i", 70)]),
                 (C["s02.e"], [("atalho", "g", 66, COR), ("de", "i", 70), ("prova", "i", 70)])], XE, 420, 150)


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], ps("lembre da aula de funções", "i", 70, TINTA2), XE, 190, passo=0.12)
    for k, (nome, f, tk) in enumerate((("ácido", "CH3–COOH", "s03.a"), ("álcool", "CH3–CH2–OH", "s03.b"), ("éster", "CH3–COO–CH2–CH3", "s03.c"))):
        y = 360 + k * 170
        E.foco(c, t, C[tk], 0.4, lambda a, nome=nome, y=y: E.escreve(c, nome, XE, y, 70, "g", COR, a))
        Q.formula_em(c, t, C[tk] + 0.2, f, XE + 380, y, 80)
    nome_partes(c, t, C["s03.d"], "etanoato", "etila", W / 2, 950, 76)


# ---------------- esterificação ----------------
EX, EY = 700, 640


def b_ester(c, t, C, b):
    if t < C["s06"]:
        E.frase(c, t, C["s04"], [("esterificação", "g", 90, COR)], XE, 200)
        Q.equacao(c, t, C["s04.a"], "ácido + álcool -> éster + H2O", W / 2, 330, 64, tl=[C["s04.a"], C["s04.a"] + 0.2, C["s04.a"] + 0.4, C["s04.c"] - 0.2, C["s04.c"], C["s04.d"], C["s04.d"] + 0.1])
        E.foco(c, t, C["s04.b"], 0.4, lambda a: E.pilula(c, "um pouco de ácido sulfúrico ajuda", W / 2, 420, 42, "g", fundo=TINTA, a=a))
        P = ester(c, t, C["s04.a"] + 0.4, C["s05.c"] - 0.2, EX, EY, 130, 74)
        if t < C["s05.c"]:
            circ(c, t, C["s05.a"], P[3][0], P[3][1], 62, E.COR)
            E.foco(c, t, C["s05.a"] + 0.2, 0.4, lambda a: E.pilula(c, "OH do ácido", P[3][0], P[3][1] + 120, 42, "g", fundo=TINTA2, a=a))
            circ(c, t, C["s05.b"], P[4][0], P[4][1], 46, E.COR)
            E.foco(c, t, C["s05.b"] + 0.2, 0.4, lambda a: E.pilula(c, "H do álcool", P[4][0] + 60, P[4][1] - 120, 42, "g", fundo=TINTA2, a=a))
        E.foco(c, t, C["s05.c"] + 1.2, 0.4, lambda a: E.pilula(c, "H₂O", P[3][0] + 190, P[3][1], 50, "g", fundo=TINTA2, a=a))
        if t >= C["s05.d"]:
            circ(c, t, C["s05.d"], P[5][0], P[5][1], 50, E.COR)
            E.foco(c, t, C["s05.e"], 0.4, lambda a: E.pilula(c, "a ligação do éster", P[5][0] + 200, P[5][1] - 110, 46, "g", fundo=E.COR, a=a))
        return
    tl = [C["s06.a"], C["s06.b"] - 0.2, C["s06.b"], C["s06.c"] - 0.2, C["s06.c"], C["s06.d"], C["s06.d"] + 0.2]
    Q.equacao(c, t, C["s06"], "CH3–COOH + HO–CH2–CH3 -> CH3–COO–CH2–CH3 + H2O", W / 2, 300, 64, tl=tl, cores={4: COR})
    for k, (s, x, tk) in enumerate((("ácido etanoico", 330, "s06.a"), ("etanol", 820, "s06.b"), ("etanoato de etila", 1360, "s06.c"))):
        E.foco(c, t, C[tk] + 0.3, 0.4, lambda a, s=s, x=x: centro(c, s, x, 400, 46, "i", TINTA2, a))
    ester(c, t, C["s06"] + 0.3, C["s06.c"], EX, 720, 120, 70)
    E.foco(c, t, C["s06.e"], 0.4, lambda a: E.pilula(c, "solvente de removedor de esmalte", W / 2, 1000, 48, "g", fundo=E.COR, a=a))


# ---------------- nome ----------------
def b_nome(c, t, C, b):
    E.frase(c, t, C["s07"], ps("o nome tem duas partes, nesta ordem", "i", 66, TINTA2), XE, 190, passo=0.1)
    E.frase(c, t, C["s07.a"], [("1", "g", 66, COR)] + ps("a do ácido:", "i", 70), XE, 340, passo=0.12)
    E.frase(c, t, C["s07.b"], [("ico", "g", 70, TINTA2), ("→", "g", 70, TINTA2), ("ato", "g", 70, COR)], XE + 560, 340, passo=0.15)
    E.frase(c, t, C["s07.c"], [("etanoico", "g", 76), ("→", "g", 76, TINTA2), ("etanoato", "g", 76, COR)], XE + 60, 460, passo=0.2)
    E.frase(c, t, C["s07.d"], [("2", "g", 66, COR)] + ps("a do álcool:", "i", 70), XE, 620, passo=0.12)
    E.frase(c, t, C["s07.e"], [("anol", "g", 70, TINTA2), ("→", "g", 70, TINTA2), ("ila", "g", 70)], XE + 560, 620, passo=0.15)
    E.frase(c, t, C["s07.f"], [("etanol", "g", 76), ("→", "g", 76, TINTA2), ("etila", "g", 76)], XE + 60, 740, passo=0.2)
    nome_partes(c, t, C["s07.g"], "etanoato", "etila", W / 2, 940, 96)


# ---------------- hidrólise ----------------
def b_volta(c, t, C, b):
    E.frase(c, t, C["s08"], ps("e o caminho de volta?", "i", 70, TINTA2), XE, 180, passo=0.12)
    Q.equacao(c, t, C["s08.a"], "éster + H2O <=> ácido + álcool", W / 2, 320, 70, tl=[C["s08.a"] + 0.3 * k for k in range(7)])
    E.frase(c, t, C["s08.b"], [("hidrólise", "g", 76, COR), ("=", "g", 76, TINTA2)] + ps("quebra pela água", "i", 76), W / 2, 450, "center", 0.12)
    P = ester(c, t, C["s08"], C["s08.c"], EX, 720, 120, 70, volta=True)
    if t >= C["s08.d"]:
        circ(c, t, C["s08.d"], P[3][0], P[3][1], 56, E.COR)
    if t >= C["s08.e"]:
        circ(c, t, C["s08.e"], P[4][0], P[4][1], 44, E.COR)
    E.foco(c, t, C["s08.f"], 0.4, lambda a: E.pilula(c, "vai e volta: seta de duas pontas", W / 2, 1010, 46, "g", fundo=TINTA, a=a))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s09"], [("cuidado", "g", 96, ERRADO)], XE, 190)
    E.frase(c, t, C["s09.a"], ps("trocar a ordem do nome", "i", 74), XE + 450, 190, passo=0.12)
    nome_partes(c, t, C["s09.b"], "butanoato", "etila", 520, 380, 66)
    E.foco(c, t, C["s09.b"] + 0.6, 0.4, lambda a: E.escreve(c, "ácido butanoico + etanol", 200, 470, 46, "i", TINTA2, a))
    Q.formula_em(c, t, C["s09.b"] + 1.0, "CH3–CH2–CH2–COO–CH2–CH3", 480, 600, 50, align="center", cores={k: COR for k in range(9)})
    E.foco(c, t, C["s09.b"] + 1.6, 0.4, lambda a: abacaxi(c, 520, 900, 110, a))
    nome_partes(c, t, C["s09.c"], "etanoato", "butila", 1400, 380, 66)
    E.foco(c, t, C["s09.c"] + 0.6, 0.4, lambda a: E.escreve(c, "ácido etanoico + butanol", 1100, 470, 46, "i", TINTA2, a))
    Q.formula_em(c, t, C["s09.c"] + 1.0, "CH3–COO–CH2–CH2–CH2–CH3", 1440, 600, 50, align="center", cores={k: COR for k in range(5)})
    E.foco(c, t, C["s09.d"], 0.4, lambda a: E.pilula(c, "outra substância", 1400, 760, 50, "g", fundo=TINTA, a=a))
    E.foco(c, t, C["s09.d"], 0.5, lambda a: centro(c, "≠", W / 2 - 10, 600, 120, "g", ERRADO, a))
    E.frase(c, t, C["s09.e"], ps("a primeira palavra é a do", "i", 62) + [("ácido", "g", 58, COR)], 1400, 960, "center", 0.1)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    if t < C["s11"]:
        E.frase(c, t, C["s10"], ps("o atalho para escrever o éster", "i", 70, CLARO), W / 2, 160, "center", 0.12)
        s, fx, fy, fs = "CH3–COOH", W / 2, 420, 150
        if t < C["s10.c"] + 1.0:
            Q.formula_em(c, t, C["s10.a"], s, fx, fy, fs, align="center", escuro=True)
            G = Q.grupos(s, fx, fy, fs, "center")
            gH = G[-1]
            circ(c, t, C["s10.b"], gH["cx"], fy - fs * 0.35, 80, E.CLARO)
        else:
            Q.formula_em(c, t, C["s10.c"] + 1.0, "CH3–COO–CH2–CH3", fx, fy, 130, align="center", escuro=True, cores={k: E.CLARO for k in (5, 6, 7, 8)})
        E.frase(c, t, C["s10.b"], ps("troque o", "i", 66, CLARO) + [("H do COOH", "g", 62, BR)] + ps("pela", "i", 66, CLARO) + [("cadeia do álcool", "g", 62, E.CLARO)], W / 2, 650, "center", 0.1)
        E.frase(c, t, C["s10.d"], ps("o éster é o ácido com o grupo do álcool no lugar do H", "i", 58, CLARO), W / 2, 900, "center", 0.08)
        return
    E.frase(c, t, C["s11.a"], ps("na volta, ao contrário", "i", 70, CLARO), W / 2, 200, "center", 0.12)
    s, fx, fy, fs = "CH3–CO|O–CH2–CH3", W / 2, 470, 120
    Q.formula_em(c, t, C["s11.a"] + 0.3, "CH3–CO–O–CH2–CH3", fx, fy, fs, align="center", escuro=True)
    G = [g for g in Q.grupos("CH3–CO–O–CH2–CH3", fx, fy, fs, "center")]
    gO = [g for g in G if g["s"] == "O"]
    if len(gO) >= 2 and t >= C["s11.b"]:
        xm = (gO[0]["x1"] + gO[1]["x0"]) / 2
        p = ep(t, C["s11.b"], 0.4)
        M.line(c, xm, fy - fs * 1.0, xm, fy - fs * 1.0 + fs * 1.3 * p, ERRADO, 1, 8, dash=[16, 10])
    E.frase(c, t, C["s11.c"], [("lado do C=O", "g", 58, BR)] + ps("ganha OH:", "i", 62, CLARO) + [("ácido", "g", 58, E.CLARO)], W / 2, 720, "center", 0.1)
    E.frase(c, t, C["s11.d"], [("o outro lado", "g", 58, BR)] + ps("ganha H:", "i", 62, CLARO) + [("álcool", "g", 58, E.CLARO)], W / 2, 840, "center", 0.1)


# ---------------- questão e resposta ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s12"], ps("hora de testar", "i", 72, COR), XE, 170)
    Q.formula_em(c, t, C["s12.a"], "H–COOH + HO–CH2–CH3", W / 2, 420, 96, align="center")
    E.foco(c, t, C["s12.a"] + 0.4, 0.4, lambda a: (centro(c, "ácido metanoico", 640, 520, 48, "i", TINTA2, a), centro(c, "etanol", 1310, 520, 48, "i", TINTA2, a)))
    E.frase(c, t, C["s12.b"], [("1", "g", 58, COR)] + ps("fórmula do éster?", "i", 64), XE, 720, passo=0.1)
    E.frase(c, t, C["s12.c"], [("2", "g", 58, COR)] + ps("nome do éster?", "i", 64), XE, 840, passo=0.1)
    if t >= C["s13"]:
        E.relogio(c, t, C["s13.a"], cx=1450, cy=780, r=140)


def b_resposta(c, t, C, b):
    E.frase(c, t, C["s14"], ps("resolvendo", "i", 72, COR), XE, 170)
    ester(c, t, C["s14"] + 0.2, C["s14.a"] + 0.3, 900, 520, 120, 70, R="H")
    E.foco(c, t, C["s14.b"], 0.4, lambda a: Q.formula(c, "H–COO–CH2–CH3", W / 2, 860, 90, TINTA, a, "center", cores={k: COR for k in (4, 5, 6, 7)}))
    E.foco(c, t, C["s14.c"], 0.4, lambda a: E.pilula(c, "+ H₂O", W / 2 + 500, 835, 50, "g", fundo=TINTA2, a=a))
    E.frase(c, t, C["s15.a"], [("metanoico", "g", 56), ("→", "g", 56, TINTA2), ("metanoato", "g", 56, COR)], 420, 1000, "center", 0.15)
    E.frase(c, t, C["s15.b"], [("etanol", "g", 56), ("→", "g", 56, TINTA2), ("etila", "g", 56)], 1000, 1000, "center", 0.15)
    E.foco(c, t, C["s15.c"], 0.4, lambda a: E.pilula(c, "metanoato de etila", 1560, 980, 50, "g", fundo=CERTO, a=a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s16"], [("resumindo", "i", 92, COR)], XE, 170)
        itens = (("s16.a", [("ácido", "g", 62), ("+", "g", 62, TINTA2), ("álcool", "g", 62), ("→", "g", 62, TINTA2), ("éster", "g", 62, COR), ("+", "g", 62, TINTA2), ("água", "g", 62)]),
                 ("s16.b", [("hidrólise:", "g", 62, COR)] + ps("o caminho de volta", "i", 66)),
                 ("s16.c", [("nome:", "g", 62, COR), ("…ato", "g", 62), ("de", "i", 66), ("…ila", "g", 62)]))
        for i, (k, partes) in enumerate(itens):
            y = 340 + i * 180
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, XE + 40, y - 26, 46, a=a), centro(c, str(i + 1), XE + 40, y - 4, 56, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, partes, XE + 120, y, passo=0.1)
    E.saida(c, t, C["s17"] - 0.1, resumo)
    if t < C["s17"]:
        return
    E.frase(c, t, C["s17"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 230)
    E.frase(c, t, C["s17"] + 0.6, ps("a gordura também é um", "i", 70) + [("éster", "g", 66, COR)], XE, 360, passo=0.1)
    E.foco(c, t, C["s17.a"], 0.4, lambda a: E.pilula(c, "+ base → sabão", XE + 230, 520, 52, "g", fundo=TINTA, a=a))
    E.foco(c, t, C["s17.b"], 0.4, lambda a: E.pilula(c, "+ álcool → biodiesel", XE + 290, 640, 52, "g", fundo=E.COR, a=a))
    E.foco(c, t, C["s17.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 470, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s17.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(770, 495, p), ep(t, C["s17.c"] + 0.2, 0.4))
    E.frase(c, t, C["s17.d"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1520, 990, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, ester=b_ester, nome=b_nome, volta=b_volta, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
