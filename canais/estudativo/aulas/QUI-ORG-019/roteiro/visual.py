"""Visual — Estudativo · QUI-ORG-019: reações de substituição.

Segue a LINGUAGEM VISUAL DA QUÍMICA (cabeçalho de QUI-MIS-001), o complemento da Orgânica de QUI-ORG-015 (estr, alceno) e a
linguagem das reações de QUI-ORG-018: equação condensada em cima, "zoom" plano embaixo; o que ENTRA em COR, o que SAI em
TINTA2, deslizando para fora. Pose da substituição (troca): carbono em cruz, o reagente chega pela direita, o átomo que sai
desce para a direita e encontra o par dele (H + Cl), enquanto o novo ocupa o lugar vago.
Todo instante vem de C[...] (marcadores do roteiro), para acompanhar a voz real quando ela chegar."""
import math

import editorial as E
import quimica as Q
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Química", "Química Orgânica")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_QUI-ORG-019_reacoes_de_substituicao.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("troca", "metano", "qual", "benzeno", "atalho", "questao", "fim"))

for eq in ("CH4 + Cl2 -> CH3Cl + HCl", "C3H8 + Cl2 -> C3H7Cl + HCl", "C6H6 + HNO3 -> C6H5NO2 + H2O", "C4H10 + Br2 -> C4H9Br + HBr",
           "C2H5OH -> C2H4 + H2O"):
    assert Q.lados(eq)[0] == Q.lados(eq)[1], eq
assert Q.contar("CH3CH2CH3") == Q.contar("C3H8") and 3 + 3 == 6 and Q.contar("CH3CH2CH3")["H"] - 6 == 2  # 6 H nas pontas, 2 no meio
assert Q.contar("CH(CH3)3") == Q.contar("C4H10") and 3 * 3 == 9 and 9 + 1 == 10                     # metilpropano: 9 + 1


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
CRUZ = [(0, -1.05), (-1.15, 0), (0, 1.05), (1.15, 0)]  # em cima, à esquerda, embaixo, à direita (a que sai)


def troca(c, t, t0, tr, tu, cx, cy, esc, size, centro_="C", ligantes=("H", "H", "H", "H"), entra=("Cl", "Cl"), escuro=False, d=1.4, a=1.0):
    """substituição no carbono em cruz: o ligante da direita sai e encontra entra[1]; entra[0] ocupa o lugar dele.
    t0 = molécula, tr = reagente (à direita, em cima), tu = troca. Devolve os pontos"""
    u = ease_io(prog(t, tu, d)) if tu is not None else 0.0
    sai = (lerp(1.15, 2.55, u), lerp(0, 1.15, u))
    e0 = (lerp(2.4, 1.25, u), lerp(-1.25, 0, u))
    e1 = (lerp(3.35, 3.45, u), lerp(-1.25, 1.15, u))
    at = [(centro_, 0, 0)] + [(s, x, y) for s, (x, y) in zip(ligantes[:3], CRUZ[:3])] + [(ligantes[3], *sai), (entra[0], *e0), (entra[1], *e1)]
    ligs = [(0, 1, 1), (0, 2, 1), (0, 3, 1)]
    if u < 0.3:
        ligs += [(0, 4, 1), (5, 6, 1)]
    if u > 0.7:
        ligs += [(0, 5, 1, E.COR), (4, 6, 1)]
    tl = [t0, t0 + 0.1, t0 + 0.2, t0 + 0.3, t0 + 0.4, tr, tr + 0.15]
    cl = CLARO if escuro else COR
    return estr(c, t, t0, at, ligs, cx, cy, esc, size, tl=tl, cores={4: TINTA2 if not escuro else "#9AA0A8", 5: cl, 6: cl}, escuro=escuro, a=a)


def propano(c, t, t0, cx, cy, esc, size, cores=None, cl=None, a=1.0):
    """propano com todos os H à vista; cl = rótulo que troca um H do meio (cima). Devolve os pontos"""
    at = [("C", -1, 0), ("C", 0, 0), ("C", 1, 0),
          ("H", -2.05, 0), ("H", -1, -1), ("H", -1, 1), (cl or "H", 0, -1), ("H", 0, 1), ("H", 1, -1), ("H", 1, 1), ("H", 2.05, 0)]
    ligs = [(0, 1, 1), (1, 2, 1), (0, 3, 1), (0, 4, 1), (0, 5, 1), (1, 6, 1), (1, 7, 1), (2, 8, 1), (2, 9, 1), (2, 10, 1)]
    return estr(c, t, t0, at, ligs, cx, cy, esc, size, passo=0.06, cores=cores, a=a)


PONTA = (3, 4, 5, 8, 9, 10)
MEIO = (6, 7)


def benzeno_sub(c, t, t0, cx, cy, R, u, sai="H", entra="NO2", escuro=False):
    """anel do benzeno com um ligante na direita: sai o H (desliza para baixo) e entra o grupo novo"""
    q = 1.0 if t0 is None else ep(t, t0, 0.5)
    anel(c, cx, cy, R, q, Q._tinta(escuro), giro=0)
    x0 = cx + R
    M.line(c, x0, cy, x0 + 70, cy, Q._tinta(escuro), q, 7)
    if u < 1:
        rot(c, sai, lerp(x0 + 110, x0 + 220, u), lerp(cy, cy + 200, u), 80, TINTA2 if u > 0 else Q._tinta(escuro), q * (1 - 0.5 * u))
    if u > 0:
        w = _meia(entra, 80)[0]
        rot(c, entra, lerp(x0 + 380, x0 + 80 + w, u), lerp(cy - 200, cy, u), 80, CLARO if escuro else COR, q * min(1, u * 2))


# ---------------- gancho ----------------
def jogador(c, x, y, cor, n, a=1.0):
    E.bola(c, x, y - 70, 44, cor, a)
    M.rrect(c, x - 52, y - 20, 104, 120, 36, cor, a)
    centro(c, str(n), x, y + 66, 56, "g", BR, a)


def b_gancho(c, t, C, b):
    a1, b1, c1 = C["s01.a"], C["s01.b"], C["s01.c"]
    if t < C["s02"]:
        u = ease_io(prog(t, a1 + 1.5, 1.4))
        E.foco(c, t, a1, 0.5, lambda a: (jogador(c, 560, 520, TINTA, 7, a), jogador(c, 760, 520, TINTA, 9, a)))
        E.foco(c, t, a1 + 0.3, 0.5, lambda a: jogador(c, lerp(960, 1180, u), lerp(520, 700, u), TINTA2, 10, a * (1 - 0.5 * u)))
        E.foco(c, t, a1 + 0.6, 0.5, lambda a: jogador(c, lerp(1380, 960, u), 520, E.COR, 11, a))
        E.frase(c, t, a1, ps("sai um, entra outro", "i", 76), XE, 220, passo=0.12)
        E.frase(c, t, b1, ps("na molécula, a mesma troca:", "i", 66, TINTA2), XE, 880, passo=0.1)
        E.frase(c, t, c1, [("sai", "i", 70), ("H,", "g", 66, TINTA2), ("entra", "i", 70), ("Cl", "g", 66, COR)], XE + 840, 880, passo=0.15)
        return
    tb = C["s02.a"] + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1600, 560, 260 * ease_back(prog(t, tb, 0.8)), giro=8 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 88), XE, 260, passo=0.14)
    lista(c, t, [(C["s02.b"], [("cloração", "g", 66, COR), ("de", "i", 70), ("um", "i", 70), ("alcano", "i", 70)]),
                 (C["s02.c"], [("nitração", "g", 66, COR), ("do", "i", 70), ("benzeno", "i", 70)]),
                 (C["s02.d"], [("qual", "i", 70), ("H", "g", 66), ("sai", "i", 70), ("primeiro", "i", 70)]),
                 (C["s02.e"], [("atalho", "g", 66, COR), ("de", "i", 70), ("prova", "i", 70)])], XE, 420, 150)


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], ps("lembre de duas coisas", "i", 70, TINTA2), XE, 190, passo=0.12)
    E.frase(c, t, C["s03.a"], [("alcano", "g", 100, COR)] + ps("só ligações simples", "i", 70), XE, 340, passo=0.15)
    Q.formula_em(c, t, C["s03.a"] + 1.2, "CH3–CH2–CH3", 1450, 340, 76, align="center")
    E.frase(c, t, C["s03.b"], ps("carbono", "i", 70) + [("primário,", "g", 62), ("secundário", "g", 62), ("ou", "i", 70), ("terciário", "g", 62)], XE, 540, passo=0.12)
    for i, (n, nome) in enumerate(((1, "primário"), (2, "secundário"), (3, "terciário"))):
        x = 420 + i * 560
        E.foco(c, t, C["s03.c"] + 0.4 * i, 0.4, lambda a, x=x, n=n, nome=nome: (
            E.bola(c, x, 760, 70, a=a), centro(c, str(n), x, 790, 86, "g", E.SOBRE, a),
            centro(c, "carbono vizinho" if n == 1 else "carbonos vizinhos", x, 890, 48, "i", TINTA2, a),
            centro(c, nome, x, 960, 56, "g", COR, a)))


# ---------------- o que é substituição ----------------
def b_troca(c, t, C, b):
    E.frase(c, t, C["s04"], ps("adição precisa de dupla; sem ela:", "i", 64, TINTA2), XE, 200, passo=0.1)
    E.frase(c, t, C["s04.a"], [("substituição", "g", 120, COR)], XE, 360)
    troca(c, t, C["s04"] + 0.4, C["s04.a"] + 0.6, C["s04.c"], 760, 700, 150, 84)
    E.foco(c, t, C["s04.b"], 0.4, lambda a: E.pilula(c, "um sai", 1420, 940, 50, "g", fundo=TINTA2, a=a))
    E.foco(c, t, C["s04.c"] + 0.5, 0.4, lambda a: E.pilula(c, "outro entra no lugar", 1080, 500, 50, "g", fundo=E.COR, a=a))
    E.foco(c, t, C["s04.d"], 0.4, lambda a: E.pilula(c, "entram 2, saem 2", 1560, 360, 56, "g", fundo=TINTA, a=a))


# ---------------- cloração do metano ----------------
def b_metano(c, t, C, b):
    tl = [C["s05.a"], C["s05.b"], C["s05.b"] + 0.2, C["s05.d"], C["s06.a"], C["s06.b"] - 0.3, C["s06.b"]]
    Q.equacao(c, t, C["s05.a"], "CH4 + Cl2 ->{luz} CH3Cl + HCl", W / 2, 200, 84, tl=tl, cores={2: COR})
    u0 = C["s05.c"] + 0.2
    troca(c, t, C["s05.a"] + 0.4, C["s05.b"] + 0.3, u0, 700, 640, 150, 84)
    E.foco(c, t, C["s05.c"], 0.4, lambda a: E.pilula(c, "o Cl₂ se divide", 1500, 380, 48, "g", fundo=TINTA, a=a))
    E.foco(c, t, C["s05.d"] + 0.4, 0.4, lambda a: E.pilula(c, "um Cl no lugar do H", 1100, 470, 46, "g", fundo=E.COR, a=a))
    E.foco(c, t, C["s05.e"], 0.4, lambda a: E.pilula(c, "o outro sai com o H", 1500, 900, 46, "g", fundo=TINTA2, a=a))
    if t >= C["s06.c"]:
        E.foco(c, t, C["s06.c"], 0.5, lambda a: Q.formula(c, "CH3Cl → CH2Cl2 → CHCl3 → CCl4", W / 2, 1060, 54, TINTA2, a, "center"))


# ---------------- qual H sai primeiro ----------------
def b_qual(c, t, C, b):
    Q.formula_em(c, t, C["s07.a"], "CH3–CH2–CH3", W / 2, 200, 90, align="center")
    E.foco(c, t, C["s07.a"], 0.4, lambda a: E.escreve(c, "propano", XE, 200, 56, "i", TINTA2, a))
    cl = t >= C["s08.c"]
    cores = {}
    if t >= C["s07.b"]:
        cores.update({i: TINTA2 for i in PONTA})
    if t >= C["s07.c"]:
        cores.update({i: COR for i in MEIO})
    P = propano(c, t, C["s07.a"] + 0.4, W / 2, 560, 140, 76, cores=cores, cl="Cl" if cl else None)
    E.foco(c, t, C["s07.b"] + 0.3, 0.4, lambda a: E.pilula(c, "pontas: C primário", 420, 820, 46, "g", fundo=TINTA2, a=a))
    E.foco(c, t, C["s07.c"] + 0.3, 0.4, lambda a: E.pilula(c, "meio: C secundário", W / 2, 820, 46, "g", fundo=E.COR, a=a))
    E.frase(c, t, C["s08.a"], [("sai mais fácil:", "i", 60), ("terciário", "g", 56, COR), (">", "g", 56, TINTA2), ("secundário", "g", 56, COR),
                               (">", "g", 56, TINTA2), ("primário", "g", 56)], W / 2, 960, "center", 0.12) if t >= C["s08.b"] else \
        E.frase(c, t, C["s08.a"], [("sai mais fácil:", "i", 60), ("secundário", "g", 56, COR), (">", "g", 56, TINTA2), ("primário", "g", 56)], W / 2, 960, "center", 0.12)
    if cl:
        circ(c, t, C["s08.c"], P[6][0], P[6][1], 62, E.COR)
        E.foco(c, t, C["s08.c"] + 0.3, 0.4, lambda a: E.pilula(c, "produto principal", 1500, 420, 46, "g", fundo=E.COR, a=a))
    E.foco(c, t, C["s08.d"], 0.4, lambda a: centro(c, "6 H nas pontas, 2 no meio", W / 2, 330, 52, "g", TINTA, a))


# ---------------- benzeno ----------------
def b_benzeno(c, t, C, b):
    E.frase(c, t, C["s09"], [("benzeno", "g", 90, COR)] + ps("também troca", "i", 76), XE, 200, passo=0.12)
    tl = [C["s09.c"] - 0.4, C["s09.c"] - 0.2, C["s09.c"], C["s10.b"], C["s10.e"], C["s10.d"] - 0.2, C["s10.d"]]
    Q.equacao(c, t, C["s09.c"] - 0.4, "C6H6 + HNO3 -> C6H5NO2 + H2O", W / 2, 1010, 76, tl=tl, cores={2: COR})
    u = ease_io(prog(t, C["s10.a"], 1.6))
    benzeno_sub(c, t, C["s09"] + 0.4, 760, 560, 150, u)
    E.foco(c, t, C["s09.a"], 0.4, lambda a: E.pilula(c, "tem duplas", 760, 340, 46, "g", fundo=TINTA, a=a))
    E.foco(c, t, C["s09.b"], 0.4, lambda a: E.pilula(c, "estável: troca em vez de abrir", 1380, 340, 46, "g", fundo=E.COR, a=a))
    E.foco(c, t, C["s10.b"] + 0.4, 0.4, lambda a: E.escreve(c, "nitro", 1300, 520, 56, "i", COR, a))
    if t >= C["s10.c"]:
        E.foco(c, t, C["s10.c"], 0.4, lambda a: Q.formula(c, "H + OH", 1240, 800, 70, TINTA2, a))
        E.foco(c, t, C["s10.d"], 0.4, lambda a: Q.formula(c, "→ H2O", 1540, 800, 70, TINTA, a))
    E.foco(c, t, C["s10.e"], 0.4, lambda a: E.pilula(c, "nitrobenzeno", 760, 820, 50, "g", fundo=E.COR, a=a))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s11"], [("cuidado", "g", 96, ERRADO)], XE, 190)
    E.frase(c, t, C["s11.a"], ps("benzeno faz adição?", "i", 74), XE + 450, 190, passo=0.12)

    def aberto():
        q = ep(t, C["s11.b"], 0.5)
        if q > 0:
            v = anel(c, 600, 600, 170, 1 - 0.6 * q, TINTA, giro=0)
            E.foco(c, t, C["s11.b"] + 0.3, 0.4, lambda a: E.pilula(c, "o anel perderia a estabilidade", 600, 870, 46, "g", fundo=ERRADO, a=a))
            if t >= C["s11.b"] + 0.6:
                E.risco(c, 430, 780, 770, 420, t, C["s11.b"] + 0.6, largura=12)
    E.saida(c, t, C["s11.c"] - 0.1, aberto)
    if t >= C["s11.c"]:
        E.frase(c, t, C["s11.c"], ps("com", "i", 60, TINTA2), XE, 360)
        for k, s in enumerate(("HNO3", "Cl2", "Br2")):
            Q.formula_em(c, t, C["s11.c"] + 0.3 + 0.2 * k, s, XE + 120 + k * 230, 360, 64)
        E.frase(c, t, C["s11.c"] + 1.2, [("substituição", "g", 64, COR)], XE + 860, 360)
        benzeno_sub(c, t, C["s11.c"] + 0.4, 760, 650, 150, ease_io(prog(t, C["s11.c"] + 1.0, 1.2)), entra="Br")
        E.foco(c, t, C["s11.d"], 0.4, lambda a: E.pilula(c, "o anel continua inteiro", 760, 900, 50, "g", fundo=E.COR, a=a))
        x_em(c, t, C["s11.d"] + 0.3, 1100, 900, 34, True)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    if t < C["s13"]:
        E.frase(c, t, C["s12"], ps("de onde sai o H?", "i", 72, CLARO), W / 2, 160, "center", 0.12)
        for i, (nome, n) in enumerate((("terciário", 3), ("secundário", 2), ("primário", 1))):
            x = 420 + i * 540
            E.foco(c, t, C["s12.a"] + 0.4 * i, 0.4, lambda a, x=x, n=n, nome=nome, i=i: (
                E.bola(c, x, 420, 90 - 14 * i, a=a), centro(c, str(i + 1) + "º", x, 452 - 4 * i, 90 - 14 * i, "g", E.SOBRE, a),
                centro(c, nome, x, 600, 64, "g", BR, a), centro(c, f"{n} C vizinho" + ("s" if n > 1 else ""), x, 680, 46, "i", CLARO, a)))
        E.frase(c, t, C["s12.b"], ps("mais carbonos vizinhos,", "i", 64, CLARO) + [("sai mais fácil", "g", 60, BR)], W / 2, 860, "center", 0.12)
        E.foco(c, t, C["s12.c"], 0.4, lambda a: E.pilula(c, "o porquê: outra aula", W / 2, 980, 44, "g", fundo=E.COR, a=a))
        return
    E.frase(c, t, C["s13.a"], [("todos", "g", 66, BR)] + ps("os H iguais? a ordem não importa", "i", 66, CLARO), W / 2, 300, "center", 0.12)
    for k, (s, x) in enumerate((("CH4", 640), ("CH3–CH3", 1260))):
        Q.formula_em(c, t, C["s13.a"] + 1.0 + 0.3 * k, s, x, 580, 120, align="center", escuro=True)
    E.frase(c, t, C["s13.b"], ps("qualquer troca dá o", "i", 66, CLARO) + [("mesmo produto", "g", 62, BR)], W / 2, 840, "center", 0.12)


# ---------------- questão ----------------
MP = [("C", 0, 0), ("H", 0, -1.05), ("H3C", -1.25, 0), ("CH3", 1.25, 0), ("CH3", 0, 1.1)]
MPL = [(0, 1, 1), (0, 2, 1), (0, 3, 1), (0, 4, 1)]


def b_questao(c, t, C, b):
    E.frase(c, t, C["s14"], ps("hora de testar", "i", 72, COR), XE, 170)
    E.foco(c, t, C["s14"] + 0.6, 0.4, lambda a: E.escreve(c, "metilpropano + bromo, com luz", XE + 520, 170, 54, "g", TINTA, a))
    estr(c, t, C["s14.a"], MP, MPL, 640, 600, 170, 84, passo=0.15)
    E.frase(c, t, C["s14.b"], [("1", "g", 58, COR)] + ps("de que carbono sai o H?", "i", 62), 1100, 520, passo=0.1)
    E.frase(c, t, C["s14.c"], [("2", "g", 58, COR)] + ps("onde fica o bromo?", "i", 62), 1100, 640, passo=0.1)
    if t >= C["s15"]:
        E.relogio(c, t, C["s15.a"], cx=1450, cy=800, r=110)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    E.frase(c, t, C["s16"], ps("resolvendo", "i", 72, COR), XE, 170)
    br = t >= C["s16.d"]
    at = list(MP)
    if br:
        at[1] = ("Br", 0, -1.05)
    cores = {}
    if t >= C["s16.a"]:
        cores.update({2: TINTA2, 3: TINTA2, 4: TINTA2})
    if t >= C["s16.b"]:
        cores[0] = COR
    if br:
        cores[1] = COR
    P = estr(c, t, None, at, MPL, 640, 600, 170, 84, cores=cores)
    for k, i in enumerate((2, 3, 4)):
        dy = 110 if i != 4 else 120
        E.foco(c, t, C["s16.a"] + 0.2 * k, 0.4, lambda a, i=i, dy=dy: E.pilula(c, "primário", P[i][0], P[i][1] + dy, 38, "g", fundo=TINTA2, a=a))
    E.foco(c, t, C["s16.b"], 0.4, lambda a: E.pilula(c, "terciário", P[0][0] + 150, P[0][1] - 90, 40, "g", fundo=E.COR, a=a))
    E.frase(c, t, C["s16.c"], [("terciário", "g", 58, COR)] + ps("solta o H mais fácil", "i", 60), 1060, 420, passo=0.1)
    if br:
        circ(c, t, C["s16.d"], P[1][0], P[1][1], 60, E.COR)
        E.frase(c, t, C["s16.d"] + 0.3, [("bromo", "g", 58), ("no", "i", 60), ("carbono central", "g", 58, COR)], 1060, 540, passo=0.1)
    E.foco(c, t, C["s17.a"], 0.4, lambda a: E.escreve(c, "9 H nas pontas, 1 no centro", 1060, 720, 54, "g", TINTA, a))
    E.frase(c, t, C["s17.b"], ps("com bromo: quase tudo no centro", "i", 58), 1060, 830, passo=0.1)
    E.foco(c, t, C["s17.c"], 0.4, lambda a: E.pilula(c, "o bromo escolhe mais que o cloro", 1440, 960, 46, "g", fundo=E.COR, a=a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s18"], [("resumindo", "i", 92, COR)], XE, 170)
        itens = (("s18.a", [("substituição:", "g", 62, COR)] + ps("um sai, outro entra", "i", 66)),
                 ("s18.b", [("alcano:", "g", 62)] + ps("H por cloro", "i", 66)),
                 ("s18.c", [("benzeno:", "g", 62)] + ps("H por nitro", "i", 66)),
                 ("s18.d", [("o", "i", 66), ("H", "g", 62), ("sai", "i", 66), ("primeiro", "i", 66), ("do", "i", 66), ("terciário", "g", 62, COR)]))
        for i, (k, partes) in enumerate(itens):
            y = 320 + i * 150
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, XE + 40, y - 26, 46, a=a), centro(c, str(i + 1), XE + 40, y - 4, 56, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, partes, XE + 120, y, passo=0.1)
        benzeno_sub(c, t, C["s18.c"] + 0.4, 1420, 700, 110, 1.0)
    E.saida(c, t, C["s19"] - 0.1, resumo)
    if t < C["s19"]:
        return
    E.frase(c, t, C["s19"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 230)
    E.frase(c, t, C["s19"] + 0.6, [("eliminação", "g", 110, COR)], XE, 370)
    Q.equacao(c, t, C["s19.a"], "CH3–CH2–OH -> CH2=CH2 + H2O", 640, 640, 70, cores={2: COR})
    E.foco(c, t, C["s19.b"], 0.4, lambda a: E.pilula(c, "a adição de trás para a frente", 640, 780, 48, "g", fundo=TINTA, a=a))
    E.foco(c, t, C["s19.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 470, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s19.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(770, 495, p), ep(t, C["s19.c"] + 0.2, 0.4))
    E.frase(c, t, C["s19.d"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1520, 990, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, troca=b_troca, metano=b_metano, qual=b_qual, benzeno=b_benzeno,
              erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
