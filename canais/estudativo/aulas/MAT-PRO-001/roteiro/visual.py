"""Visual — Estudativo · MAT-PRO-001: sequências e lei de formação. Primeira aula da trilha Progressões.

Linguagem visual da trilha Progressões (as próximas aulas copiam daqui; herda a trilha Funções, MAT-FUN-003):
- posição (n, o índice, "1º", "2º"…) = índigo da matéria (ENT); termo / valor (aₙ, o número da lista) = tinta preta (SAI).
- cada termo é uma caixa branca com borda índigo: o VALOR dentro (preto) e a POSIÇÃO embaixo (índigo, "1º", "2º"…): casa().
  A fila de caixas (xs_fila()) é a sequência; "?" em cinza é termo ainda não descoberto; luz= acende a caixa da vez.
- "á índice um" na tela é a₁: a letra preta com o índice pequeno, rebaixado e índigo. Use an(k) dentro de fx():
  fx(c, an(1) + [(" = 4", SAI)], …) escreve a₁ = 4; an("n+1") escreve aₙ₊₁. O índice nunca vira número grande ao lado da letra.
- lei de formação = máquina escura de MAT-FUN-003 (maquina(), passa()): a posição entra em esfera índigo, o termo sai em esfera preta.
- recorrência = setas curvas por cima da fila, de uma caixa para a seguinte, com a regra numa pílula ("×2 −1"): passos().
- erro em vermelho, conferência em verde, atalho no palco escuro; fórmulas com fx() (índices) e E.formula.
Peças locais: casa(), casa_em(), an(), xs_fila(), reticencias(), esfera(), maquina(), passa(), passos(), seta_curva(), bola_res(),
palitos() (prévia da MAT-PRO-002); fl()/fx() escrevem índices com "_" ("a_n", "a_{n+1}")."""
import math
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Matemática", "Progressões")
COR, CLARO = E.COR_TEXTO, E.CLARO
ENT, SAI = COR, TINTA  # posição / índice · termo / valor
ARQUIVO_FINAL = "estudativo_MAT-PRO-001_sequencias_e_lei_de_formacao.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("sequencia", "lei", "recorrencia", "atalho", "questao", "fim"))
BR = "#FFFFFF"

a = lambda n: 3 * n + 1
assert [a(n) for n in (1, 2, 3, 4, 5)] == [4, 7, 10, 13, 16] and a(10) == 31 and a(100) == 301
assert (100 - 1) / 3 == 33 and (50 - 1) % 3 != 0 and (10 - 1) / 3 == 3
r = [3]
for _ in range(4):
    r.append(2 * r[-1] - 1)
assert r == [3, 5, 9, 17, 33]
assert 5 * 20 - 2 == 98 and (73 + 2) / 5 == 15
q = [1]
for _ in range(3):
    q.append(2 * q[-1] + 3)
assert q == [1, 5, 13, 29]


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças da trilha ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def pulso(t, t0, d=1.6):
    return ep(t, t0, 0.3) * (1 - ep(t, t0 + d, 0.5))


def _pedacos(s):
    """separa a escrita em trechos normais e índices: "log_2 x" → [("log", 0), ("2", 1), (" x", 0)]; "_{f{1}{2}}" vale inteiro"""
    out, i, txt = [], 0, ""
    while i < len(s):
        if s[i] == "_" and i + 1 < len(s):
            if txt:
                out.append((txt, 0))
                txt = ""
            if s[i + 1] == "{":
                k, j = 1, i + 2
                while k:
                    k += {"{": 1, "}": -1}.get(s[j], 0)
                    j += 1
                out.append((s[i + 2:j - 1], 1))
                i = j
            else:
                out.append((s[i + 1], 1))
                i += 2
        else:
            txt += s[i]
            i += 1
    if txt:
        out.append((txt, 0))
    return out


def fl(c, s, x, y, size, est="g", cor=TINTA, a=1.0):
    """E.formula com índice: o trecho depois de "_" sai pequeno e rebaixado (a₁, aₙ₊₁). Devolve a largura"""
    w = 0.0
    for txt, sub in _pedacos(s):
        if sub:
            w += E.formula(c if a > 0 else None, txt, x + w + size * 0.02, y + size * (0.34 if "f{" in txt else 0.2), size * 0.56, est, cor,
                           a) + size * 0.04
        else:
            w += E.formula(c if a > 0 else None, txt, x + w, y, size, est, cor, a)
    return w


def fx(c, partes, x, y, size, a=1.0, align="left", est="g"):
    """fórmula em pedaços de cor: partes = [(escrita, cor[, opacidade])]; "^x" sozinho é o expoente do pedaço anterior.
    Devolve (largura, [x de cada pedaço], [largura de cada pedaço])."""
    ws = [fl(None, p[0], 0, 0, size, est, a=0) for p in partes]
    w = sum(ws)
    xx = x - w / 2 if align == "center" else x - w if align == "right" else x
    xs = []
    for p, wi in zip(partes, ws):
        xs.append(xx)
        k = p[2] if len(p) > 2 else 1.0
        if a * k > 0:
            fl(c, p[0], xx, y, size, est, p[1], a * k)
        xx += wi
    return w, xs, ws


def fx_em(c, t, t0, partes, x, y, size, align="left", d=0.5):
    E.foco(c, t, t0, d, lambda a: fx(c, partes, x, y, size, a, align))


def par(c, xv, yv, x, y, size, a=1.0, align="left"):
    """par ordenado (x, y): x em índigo, y em preto"""
    return fx(c, [("(", TINTA), (xv, ENT), (", ", TINTA), (yv, SAI), (")", TINTA)], x, y, size, a, align)


def anel(c, t, t0, X, Y, cor=None):
    p = prog(t, t0, 0.9)
    if 0 < p < 1:
        c.drawCircle(X, Y, 14 + 60 * ease_out(p), M.paint(cor or COR, 1 - p, stroke=6))


def celula(c, s, cx, cy, size, cor, a):
    if "f{" in s:
        E.formula(c, s, cx, cy + size * 0.25, size * 0.92, "g", cor, a, "center")
    else:
        E.formula(c, s, cx, cy + size * 0.36, size, "g", cor, a, "center")


def tabela(c, t, x0, y0, cols, tc, wc=200, hl=100, size=62, luz=None):
    """tabela em pé: cols = [(cabeçalho em partes de fx, cor dos valores, valores, instante de cada valor)]; luz(i) = destaque da linha"""
    n, nl = len(cols), len(cols[0][2])
    a = ep(t, tc, 0.5)
    if a > 0:
        for j, (cab, _, _, _) in enumerate(cols):
            fx(c, cab, x0 + wc * (j + 0.5), y0 - 34, 56, a, "center")
        M.line(c, x0, y0, x0 + n * wc, y0, TINTA, a, 4)
        for j in range(1, n):
            M.line(c, x0 + wc * j, y0, x0 + wc * j, y0 + hl * nl + 10, TINTA, a, 4)
    for i in range(nl):
        cy = y0 + 10 + hl * i + hl / 2
        if luz is not None:
            q = luz(i)
            if q > 0:
                M.rrect(c, x0 - 8, cy - hl / 2 + 4, n * wc + 16, hl - 8, 14, COR, 0.14 * q)
        for j, (_, cor, vals, tv) in enumerate(cols):
            if tv[i] is not None:
                E.foco(c, t, tv[i], 0.4, lambda q, s=vals[i], j=j, cy=cy, cor=cor: celula(c, s, x0 + wc * (j + 0.5), cy, size, cor, q), sobe=6)


def luz_de(t, ks, fim):
    """destaque da linha i entre o instante dela (ks[i]) e o próximo"""
    def luz(i):
        k = ks[i]
        if k is None:
            return 0.0
        nxt = [v for v in ks if v is not None and v > k]
        t1 = min(nxt) if nxt else fim
        return ep(t, k, 0.3) * (1 - ep(t, t1 - 0.2, 0.3))
    return luz


def eqn(c, esq, dir_, y, size, a=1.0, xi=W / 2, op="=", cor_op=SAI):
    """equação ou inequação com o sinal (op) centrado em xi: esq e dir_ em partes de fx. Devolve (xs, ws) de cada lado"""
    gap = size * 0.28
    wi = E.larg(op, "g", size)
    _, xe, we = fx(c, esq, xi - wi / 2 - gap, y, size, a, "right")
    if a > 0:
        E.escreve(c, op, xi - wi / 2, y, size, "g", cor_op, a)
    _, xd, wd = fx(c, dir_, xi + wi / 2 + gap, y, size, a)
    return (xe, we), (xd, wd)


def eqn_em(c, t, t0, esq, dir_, y, size, xi=W / 2, op="=", cor_op=SAI, d=0.5):
    E.foco(c, t, t0, d, lambda a: eqn(c, esq, dir_, y, size, a, xi, op, cor_op))


def caixa(c, x, y, w, size, a, cor=None, dois=False):
    """contorno num pedaço de fórmula (x = borda, y = linha de base, w = largura)"""
    if a <= 0:
        return
    alto = size * (1.62 if dois else 1.0)
    topo = y - size * (1.12 if dois else 0.82)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x - size * 0.08, topo, w + size * 0.12, alto + size * 0.1), 16, 16),
                M.paint(cor or COR, a, stroke=5))


def nota(c, t, t0, txt, x, y, size=46, fundo=None, cor="#FFFFFF"):
    E.foco(c, t, t0, 0.4, lambda a: E.pilula(c, txt, x, y, size, "g", fundo=fundo or COR, cor=cor, a=a), sobe=6)


def nota_fx(c, t, t0, partes, cx, cy, size=48, fundo=None):
    """pílula com fórmula dentro (para log₂ e potências)"""
    def d(a):
        w = fx(c, partes, 0, 0, size, 0)[0]
        h = size * 1.7
        M.rrect(c, cx - w / 2 - size * 0.55, cy - h / 2, w + size * 1.1, h, h / 2, fundo or COR, a)
        fx(c, partes, cx, cy + size * 0.36, size, a, "center")
    E.foco(c, t, t0, 0.4, d, sobe=6)




def seta_curva(c, t, t0, A, B, bojo, rot=None, cor=None, size=36, d=0.5, escuro=False, largura=5):
    """seta curva de A até B (pixels), barriga de `bojo` px para a esquerda de quem anda de A para B; rot numa pílula no meio"""
    p = ease_io(prog(t, t0, d))
    if p <= 0:
        return
    cor = cor or (CLARO if escuro else COR)
    (x0, y0), (x1, y1) = A, B
    dx, dy = x1 - x0, y1 - y0
    n = math.hypot(dx, dy) or 1.0
    nx, ny = dy / n, -dx / n
    qx, qy = (x0 + x1) / 2 + nx * bojo, (y0 + y1) / 2 + ny * bojo
    pt = lambda s: ((1 - s) ** 2 * x0 + 2 * (1 - s) * s * qx + s * s * x1, (1 - s) ** 2 * y0 + 2 * (1 - s) * s * qy + s * s * y1)
    path = skia.Path()
    path.moveTo(x0, y0)
    for i in range(1, 31):
        path.lineTo(*pt(p * i / 30))
    c.drawPath(path, M.paint(cor, 1.0, stroke=largura, cap_round=True))
    if p > 0.9:
        ex, ey = pt(1.0)
        ux, uy = ex - qx, ey - qy
        k = math.hypot(ux, uy) or 1.0
        ux, uy = ux / k, uy / k
        tri = skia.Path()
        tri.moveTo(ex + ux * 6, ey + uy * 6)
        tri.lineTo(ex - ux * 20 - uy * 12, ey - uy * 20 + ux * 12)
        tri.lineTo(ex - ux * 20 + uy * 12, ey - uy * 20 - ux * 12)
        tri.close()
        c.drawPath(tri, M.paint(cor, ep(t, t0 + d * 0.9, 0.15)))
    if rot:
        mx, my = pt(0.5)
        w = E.larg(rot, "g", size) + size * 1.1
        s = 1 if bojo >= 0 else -1
        off = abs(nx) * (w / 2 + 6) + abs(ny) * (size * 0.8 + 6)
        E.foco(c, t, t0 + d * 0.5, 0.4, lambda a: E.pilula(c, rot, mx + s * nx * off, my + s * ny * off, size, "g",
                                                          fundo=cor, cor="#07070F" if escuro else E.SOBRE, a=a), sobe=6)




# ---------------- peças de Progressões (as próximas aulas copiam daqui) ----------------
def casa(c, cx, cy, val, pos=None, a=1.0, s=150, borda=None, cor_val=None, luz=0.0, size=None, pos_size=44):
    """o termo numa caixa: valor dentro (preto), posição embaixo (índigo). luz (0..1) pinta o fundo de índigo claro.
    val = "?" sai em cinza; val = "" deixa a caixa vazia."""
    if a <= 0:
        return
    x, y = cx - s / 2, cy - s / 2
    M.rrect(c, x, y, s, s, 22, "#FFFFFF", a)
    if luz > 0:
        M.rrect(c, x, y, s, s, 22, COR, 0.16 * luz * a)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, s, s), 22, 22), M.paint(borda or COR, a, stroke=5))
    if val != "":
        k = size or (s * 0.46 if len(val) <= 2 else s * 0.36 if len(val) <= 3 else s * 0.28)
        centro(c, val, cx, cy + k * 0.36, k, "g", cor_val or (CINZA if val == "?" else TINTA), a)
    if pos:
        centro(c, pos, cx, cy + s / 2 + pos_size + 14, pos_size, "b", COR, a)


def casa_em(c, t, t0, cx, cy, val, pos=None, s=150, **kw):
    E.foco(c, t, t0, 0.45, lambda a: casa(c, cx, cy, val, pos, a, s, **kw), sobe=10)


def ordinal(n):
    return f"{n}º"


def an(k, cor_a=None, cor_i=None):
    """partes de fx para "a" com índice k (a₁, aₙ, aₙ₊₁): letra em preto, índice (a posição) em índigo"""
    return [("a", cor_a or SAI), ("_{" + str(k) + "}", cor_i or ENT)]


def xs_fila(x0, n, s=150, gap=30):
    return [x0 + s / 2 + i * (s + gap) for i in range(n)]


def reticencias(c, cx, cy, a=1.0, cor=None):
    if a > 0:
        for dx in (-26, 0, 26):
            c.drawCircle(cx + dx, cy, 8, M.paint(cor or TINTA2, a))


# ---------------- a máquina (a mesma de MAT-FUN-003): a posição entra, o termo sai ----------------
def esfera(c, X, Y, s, cor, a=1.0, r=62, size=None):
    if a <= 0:
        return
    size = size or (r * 0.95 if len(s) < 3 else r * 0.62 if len(s) < 5 else r * 0.5)
    E.bola(c, X, Y, r, cor, a)
    centro(c, s, X, Y + size * 0.36, size, "g", BR, a)


def maquina(c, cx, cy, regra, a=1.0, w=520, h=280, size=72, rotulos=("posição", "termo"), nome="a"):
    """caixa escura com a regra; boca de entrada (índigo, a posição) à esquerda e de saída (o termo) à direita"""
    if a <= 0:
        return
    sh = skia.Paint(AntiAlias=True, Color=M.hexc("#000000", 0.25 * a))
    sh.setMaskFilter(skia.MaskFilter.MakeBlur(skia.kNormal_BlurStyle, 14))
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2 + 10, cy - h / 2 + 18, w, h), 40, 40), sh)
    M.rrect(c, cx - w / 2, cy - h / 2, w, h, 40, TINTA, a)
    M.rrect(c, cx - w / 2 - 22, cy - 66, 44, 132, 14, ENT, a)
    M.rrect(c, cx + w / 2 - 22, cy - 66, 44, 132, 14, TINTA2, a)
    if nome:
        E.escreve(c, nome, cx - w / 2 + 36, cy - h / 2 + 74, 64, "i", CLARO, a)
    if regra:
        E.formula(c, regra, cx, cy + size * 0.36 + 14, size, "g", BR, a, "center")
    if rotulos:
        centro(c, rotulos[0], cx - w / 2 - 150, cy + 120, 44, "i", ENT, a)
        centro(c, rotulos[1], cx + w / 2 + 150, cy + 120, 44, "i", SAI, a)


def passa(c, t, cx, cy, ent, sai, t_in, t_out, w=520, some=None, r=58, dist=260):
    """a posição rola até a boca e some; o termo nasce na outra boca e anda para fora. some = instante em que tudo vai embora"""
    fim = 1.0 if some is None else 1 - ep(t, some, 0.4)
    if fim <= 0:
        return
    p = ease_io(prog(t, t_in, 0.8))
    if ent is not None:
        if 0 < p < 1:
            esfera(c, lerp(cx - w / 2 - dist, cx - w / 2 - 10, p), cy, ent, ENT, (1 - ep(t, t_in + 0.55, 0.25)) * fim, r)
        elif p <= 0 and t >= t_in - 0.6:
            esfera(c, cx - w / 2 - dist, cy, ent, ENT, ep(t, t_in - 0.6, 0.4) * fim, r)
    if sai is not None:
        q = ease_out(prog(t, t_out, 0.8))
        if q > 0:
            esfera(c, lerp(cx + w / 2, cx + w / 2 + dist, q), cy, sai, SAI, min(1, q * 3) * fim, r)


def passos(c, t, xs, cy, ts, rot, s=150, cor=None, escuro=False, size=34):
    """setas curvas por cima da fila, de uma caixa para a seguinte, com a regra numa pílula: a recorrência"""
    for i, t0 in enumerate(ts):
        if t0 is None:
            continue
        A = (xs[i] + s * 0.18, cy - s / 2 - 8)
        B = (xs[i + 1] - s * 0.18, cy - s / 2 - 8)
        seta_curva(c, t, t0, A, B, 70, rot, cor=cor, escuro=escuro, size=size)


def bola_res(c, t, t0, txt, cx, cy, r, size, sub=None, cor=None):
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r, cor or CERTO, a), fx(c, txt if isinstance(txt, list) else [(txt, BR)], cx,
                                                                                 cy + size * 0.36 - (24 if sub else 0), size, a, "center"),
                                     sub and centro(c, sub, cx, cy + size * 0.36 + 50, 46, "i", BR, a)))


# ---------------- gancho ----------------
LISTA = ["4", "7", "10", "13"]


def b_gancho(c, t, C, b):
    def cena1():
        xs = xs_fila(170, 5, 150, 30)
        cy = 430
        for i, v in enumerate(LISTA):
            casa_em(c, t, C["s01.a"] + 0.6 * i, xs[i], cy, v, ordinal(i + 1))
        E.frase(c, t, C["s01.a"] + 2.6, [("qual", "i", 70), ("é", "i", 70), ("o", "i", 70), ("próximo?", "g", 72, COR)], XE, 220)
        q = ep(t, C["s01.b"], 0.4)
        casa_em(c, t, C["s01.a"] + 2.8, xs[4], cy, "16" if t >= C["s01.b"] else "?", "5º", luz=q)
        E.foco(c, t, C["s01.c"], 0.4, lambda a: reticencias(c, 1180, cy, a))
        casa_em(c, t, C["s01.c"] + 0.2, 1390, cy, "?", "100º", borda=TINTA)
        E.frase(c, t, C["s01.c"] + 1.4, ps("ninguém quer escrever cem números", "i", 64, TINTA2), XE, 800, passo=0.08)
    E.saida(c, t, C["s02"] - 0.1, cena1)
    if t < C["s02"]:
        return
    tb, te = C["s02.a"], C["s02.end"]
    E.foco(c, t, te - 1.8, 0.7, lambda a: E.bola(c, 1480, 540, 290 * ease_back(prog(t, te - 1.8, 0.7))), blur=0)
    E.frase(c, t, tb, ps("até o fim da aula", "i", 84), XE, 300)
    E.frase(c, t, tb + 1.2, [("qualquer", "i", 110), ("termo", "g", 120, COR)], XE, 470)
    E.frase(c, t, tb + 2.6, ps("sem escrever todos", "i", 70, TINTA2), XE, 570)
    E.frase(c, t, C["s02.b"], [("posição", "g", 110, COR), ("≠", "g", 100), ("valor", "g", 110)], XE, 760)
    E.foco(c, t, te - 1.4, 0.5, lambda a: (E.escreve(c, "+ atalho", 1320, 525, 84, "g", BR, a),
                                           E.escreve(c, "de prova", 1340, 610, 84, "i", BR, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.linha(c, t, [("você", "i", 84, TINTA, C["s03"]), ("precisa", "i", 84, TINTA, C["s03"] + 0.2), ("de", "i", 84, TINTA, C["s03"] + 0.4),
                   ("1", "g", 90, COR, C["s03"] + 0.6), ("coisa:", "i", 84, TINTA, C["s03"] + 0.8)], W / 2, 220, "center")
    fx_em(c, t, C["s03.a"], [("f(", SAI), ("x", ENT), (")", SAI)], W / 2, 400, 130, "center")
    for k, y, partes, rot, fundo in ((C["s03.a"] + 1.0, 620, [("f(", SAI), ("5", ENT), (") = ?", SAI)], "número nos parênteses: calcule", ENT),
                                     (C["s03.a"] + 2.6, 820, [("f(", SAI), ("x", ENT), (") = 30", SAI)], "número depois do igual: resolva", TINTA)):
        fx_em(c, t, k, partes, 380, y, 100)
        E.foco(c, t, k + 0.3, 0.4, lambda a, y=y, rot=rot, fundo=fundo: E.pilula(c, rot, 1230, y - 34, 46, "g", fundo=fundo, a=a), sobe=6)


# ---------------- o que é sequência ----------------
def b_sequencia(c, t, C, b):
    s = 150
    xs = xs_fila(XE + 260, 4, s, 60)
    cy = lerp(430, 330, ease_io(prog(t, C["s05"], 0.6)))
    E.saida(c, t, C["s05"] - 0.1, lambda: (
        E.frase(c, t, C["s04.a"], [("uma", "i", 70), ("lista", "i", 70), ("em", "i", 70), ("ordem", "g", 76, COR)], XE, 170),
        E.frase(c, t, C["s04.a"] + 1.0, [("=", "g", 70), ("sequência", "g", 76)], XE + 640, 170)))
    for i, v in enumerate(LISTA):
        casa_em(c, t, C["s04.a"] + 0.25 * i, xs[i], cy, v, ordinal(i + 1) if t >= C["s04.c"] + 0.2 * i else None, s,
                luz=pulso(t, C["s04.b"], 2.2) if i == 1 else 0)
    if t < C["s05"]:
        E.foco(c, t, C["s04.b"], 0.4, lambda a: (E.pilula(c, "termo", xs[1], cy - s / 2 - 70, 46, "g", fundo=TINTA, a=a),
                                                 M.arrow(c, xs[1], cy - s / 2 - 40, xs[1], cy - s / 2 - 8, TINTA, a, 4, 14)), sobe=6)
        E.foco(c, t, C["s04.c"] + 0.8, 0.4, lambda a: (E.pilula(c, "lugar na fila", xs[3] + 300, cy + s / 2 + 58, 44, "g", a=a)), sobe=6)
        return
    # o índice: a₁, a₂ em cima das caixas
    for i, k in ((0, "s05.b"), (1, "s05.c")):
        E.foco(c, t, C[k], 0.4, lambda a, i=i: fx(c, an(i + 1), xs[i], cy - s / 2 - 30, 64, a, "center"), sobe=6)
        fx_em(c, t, C[k] + 0.3, an(i + 1) + [(" = " + LISTA[i], SAI)], XE, 690 + 170 * i, 120)
    # o "a" grande com o índice
    X, Y = 1000, 800
    w, xs2, ws = fx(c, an(1), X, Y, 280, 0)
    E.foco(c, t, C["s05.a"], 0.5, lambda a: fx(c, an(1), X, Y, 280, a))
    xi = xs2[1] + ws[1] / 2
    E.foco(c, t, C["s05.a"] + 0.8, 0.4, lambda a: (M.arrow(c, xi + 150, Y + 60, xi + 40, Y + 40, ENT, a, 4, 14),
                                                   E.pilula(c, "índice", xi + 260, Y + 70, 44, "g", a=a)), sobe=6)
    E.foco(c, t, C["s05.d"], 0.4, lambda a: E.pilula(c, "= a posição", xi + 290, Y + 170, 44, "g", fundo=ENT, a=a), sobe=6)
    E.foco(c, t, C["s05.e"], 0.4, lambda a: (M.arrow(c, X - 40, Y - 200, X + 40, Y - 150, TINTA, a, 4, 14),
                                             E.pilula(c, "o que vale: o termo", X - 170, Y - 240, 44, "g", fundo=TINTA, a=a)), sobe=6)


# ---------------- lei de formação ----------------
LEI = an("n") + [(" = 3", SAI), ("n", ENT), (" + 1", SAI)]


def b_lei(c, t, C, b):
    def s06():
        S = 150
        w, xs, ws = fx(c, LEI, W / 2, 0, S, 0, "center")
        fx_em(c, t, C["s06.a"], LEI, W / 2, 360, S, "center")
        xn, xa = xs[3] + ws[3] / 2, xs[0] + (ws[0] + ws[1]) / 2
        E.foco(c, t, C["s06.b"], 0.4, lambda a: (E.pilula(c, "n = posição", xn, 520, 50, "g", a=a),
                                                 M.arrow(c, xn, 485, xn, 400, ENT, a, 4, 14)), sobe=6)
        E.foco(c, t, C["s06.c"], 0.4, lambda a: (E.pilula(c, "o termo", xa, 520, 50, "g", fundo=TINTA, a=a),
                                                 M.arrow(c, xa, 485, xa, 410, TINTA, a, 4, 14)), sobe=6)
        E.frase(c, t, C["s06.d"], [("lei", "g", 120, COR), ("de", "i", 110), ("formação", "g", 120, COR)], W / 2, 800, "center")
    E.saida(c, t, C["s07"] - 0.1, s06)
    if C["s07"] <= t < C["s08"]:
        fx_em(c, t, C["s07"], LEI, W / 2, 180, 80, "center")
        E.frase(c, t, C["s07.a"], [("a", "i", 66), ("posição", "g", 70, ENT), ("entra,", "i", 66), ("o", "i", 66), ("termo", "g", 70),
                                   ("sai", "i", 66)], W / 2, 320, "center")
        cx, cy = W / 2, 580
        E.foco(c, t, C["s07"] + 0.3, 0.5, lambda a: maquina(c, cx, cy, "3n + 1", a))
        passa(c, t, cx, cy, "1", "4", C["s07.b"], C["s07.b"] + 1.6, some=C["s07.c"] - 0.2)
        passa(c, t, cx, cy, "2", "7", C["s07.c"], C["s07.c"] + 1.6)
        E.saida(c, t, C["s07.c"] - 0.2, lambda: fx_em(c, t, C["s07.b"] + 0.8, [("3 · ", SAI), ("1", ENT), (" + 1 = ", SAI), ("4", SAI)], W / 2, 900, 90, "center"))
        fx_em(c, t, C["s07.c"] + 0.8, [("3 · ", SAI), ("2", ENT), (" + 1 = ", SAI), ("7", SAI)], W / 2, 900, 90, "center")
    if t < C["s08"]:
        return
    # o décimo e o centésimo, sem escrever os do meio
    xs = xs_fila(XE, 4, 120, 26)
    for i, v in enumerate(LISTA[:3]):
        casa(c, xs[i], 230, v, ordinal(i + 1), ep(t, C["s08"], 0.4), 120)
    E.foco(c, t, C["s08"] + 0.2, 0.4, lambda a: reticencias(c, xs[3], 230, a))
    casa_em(c, t, C["s08.c"], xs[3] + 180, 230, "31", "10º", 120, luz=1)
    fx_em(c, t, C["s08"] + 0.4, an(10) + [(" = 3 · ", SAI), ("10", ENT), (" + 1", SAI)], XE, 520, 110)
    fx_em(c, t, C["s08.a"], [("= 30 + 1", SAI)], XE + 230, 680, 110)
    fx_em(c, t, C["s08.b"], [("= 31", COR)], XE + 790, 680, 110)
    E.foco(c, t, C["s08.c"] + 0.6, 0.4, lambda a: E.escreve(c, "sem escrever os 9 de antes", 1080, 520, 50, "i", TINTA2, a))
    fx_em(c, t, C["s08.d"], an(100) + [(" = 3 · ", SAI), ("100", ENT), (" + 1 = ", SAI), ("301", COR)], XE, 900, 100)


# ---------------- recorrência ----------------
REC = an("n+1") + [(" = 2 · ", SAI)] + an("n") + [(" − 1", SAI)]
VREC = ["3", "5", "9", "17", "33"]


def b_recorrencia(c, t, C, b):
    def s09():
        E.frase(c, t, C["s09.a"], [("como", "i", 76), ("passar", "i", 76), ("de", "i", 76), ("um", "i", 76), ("termo", "g", 80),
                                   ("para", "i", 76), ("o", "i", 76), ("seguinte", "g", 80, COR)], W / 2, 220, "center", passo=0.12)
        S = 130
        w, xs, ws = fx(c, REC, W / 2, 0, S, 0, "center")
        fx_em(c, t, C["s09.b"], REC, W / 2, 480, S, "center")
        caixa(c, xs[1], 480 + S * 0.2, ws[1] - S * 0.1, S * 0.56, ep(t, C["s09.b"] + 1.2, 0.4))
        E.foco(c, t, C["s09.b"] + 1.4, 0.4, lambda a: E.escreve(c, "n + 1 todo no índice", xs[1] - 40, 640, 46, "i", ENT, a))
        E.foco(c, t, C["s09.c"], 0.4, lambda a: E.pilula(c, "o próximo", xs[0] + (ws[0] + ws[1]) / 2, 790, 50, "g", fundo=TINTA, a=a), sobe=6)
        E.foco(c, t, C["s09.c"] + 0.6, 0.4, lambda a: E.pilula(c, "o dobro do anterior, menos 1", xs[3] + 200, 790, 50, "g", a=a), sobe=6)
    E.saida(c, t, C["s10"] - 0.1, s09)
    if t < C["s10"]:
        return
    fx_em(c, t, C["s10"], REC, W / 2, 190, 84, "center")
    s, cy = 150, 600
    xs = xs_fila(200, 5, s, 110)
    ks = [C["s10.b"], C["s10.c"], C["s10.d"], C["s10.e"], C["s10.f"]]
    for i in range(5):
        tem = t >= ks[i]
        casa_em(c, t, C["s10"] + 0.3 + 0.1 * i, xs[i], cy, VREC[i] if tem else "?", ordinal(i + 1), s, luz=pulso(t, ks[i], 1.6))
    E.foco(c, t, C["s10.a"], 0.4, lambda a: E.pilula(c, "sem o 1º, não começa", xs[0] + 60, cy + s / 2 + 130, 44, "g", fundo=ERRADO, a=a * (1 - ep(t, C["s10.b"], 0.3))), sobe=6)
    E.foco(c, t, C["s10.b"] - 0.2, 0.4, lambda a: fx(c, an(1) + [(" = 3", SAI)], xs[0] - 60, cy + s / 2 + 150, 64, a), sobe=6)
    passos(c, t, xs, cy, [k - 0.5 for k in ks[1:]], "×2 −1", s)
    if t >= C["s11"]:
        q = pulso(t, C["s11.a"], 3.0)
        if q > 0:
            for i in range(4):
                M.line(c, xs[i] + s / 2, cy, xs[i + 1] - s / 2, cy, COR, q, 6)
        E.frase(c, t, C["s11.a"], [("cada", "i", 64), ("um", "i", 64), ("depende", "g", 66, COR), ("do", "i", 64), ("anterior", "i", 64)],
                W / 2, 920, "center")
        E.foco(c, t, C["s11.b"], 0.4, lambda a: (reticencias(c, 1700, cy, a), centro(c, "até o 10º", 1700, cy + 110, 44, "b", COR, a)))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s12.a"], [("cuidado:", "g", 84, ERRADO), ("trocar", "i", 84), ("posição", "g", 84, COR), ("por", "i", 84),
                               ("valor", "g", 84)], W / 2, 180, "center")

    def s12():
        fx_em(c, t, C["s12.b"], [("pede ", SAI)] + an(10) + [(" em  ", SAI)] + LEI, XE, 360, 90)
        fx_em(c, t, C["s12.c"], [("3", SAI), ("n", ENT), (" + 1 = 10", ERRADO)], XE, 560, 100)
        fx_em(c, t, C["s12.d"], [("n", ENT), (" = 3", ERRADO)], XE, 730, 100)
        E.foco(c, t, C["s12.d"] + 1.0, 0.4, lambda a: E.pilula(c, "resposta: 3?", XE + 620, 700, 54, "g", fundo=ERRADO, a=a), sobe=6)
    E.saida(c, t, C["s13"] - 0.1, s12)
    if t < C["s13"]:
        return
    xs = xs_fila(XE + 200, 4, 140, 40)
    for i, v in enumerate(LISTA):
        casa(c, xs[i], 360, v, ordinal(i + 1), ep(t, C["s13"], 0.4), 140, luz=ep(t, C["s13.a"], 0.4) if i == 2 else 0)
    E.foco(c, t, C["s13.b"], 0.4, lambda a: fx(c, an(3) + [(" = 10", SAI), ("  não  ", ERRADO)] + an(10), xs[3] + 140, 380, 80, a))
    for k, x, l1, l2, ex, fundo in ((C["s13.c"], XE, "número embaixo da letra", "troque o n e calcule", an(10) + [(" → n = 10", ENT)], ENT),
                                    (C["s13.d"], 1000, "valor depois do igual", "resolva a equação", an("n") + [(" = 10 → 3n + 1 = 10", SAI)], TINTA)):
        p = ep(t, k, 0.5)
        if p > 0:
            E.caixa_pontilhada(c, x, 560, 760, 380, p, fundo, p)
        E.foco(c, t, k, 0.4, lambda a, x=x, l1=l1, fundo=fundo: E.escreve(c, l1, x + 40, 660, 54, "g", fundo, a))
        E.foco(c, t, k + 0.3, 0.4, lambda a, x=x, l2=l2: E.escreve(c, l2, x + 40, 750, 54, "i", TINTA, a))
        E.foco(c, t, k + 0.8, 0.4, lambda a, x=x, ex=ex: fx(c, ex, x + 40, 880, 64, a))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def s14_15():
        E.frase(c, t, C["s14.a"], [("o", "i", 84, CLARO), ("caminho", "g", 90, BR), ("de", "i", 84, CLARO), ("volta", "g", 90, BR)], W / 2, 190, "center")
        E.foco(c, t, C["s14.a"] + 1.6, 0.4, lambda a: E.escreve(c, "o 100 está?", XE, 340, 66, "i", CLARO, a))
        fx_em(c, t, C["s14.b"], [("3", BR), ("n", CLARO), (" + 1 = 100", BR)], XE, 480, 90)
        fx_em(c, t, C["s14.c"], [("3", BR), ("n", CLARO), (" = 99", BR)], XE + 60, 620, 90)
        fx_em(c, t, C["s14.d"], [("n", CLARO), (" = 33", BR)], XE + 140, 760, 90)
        E.foco(c, t, C["s14.d"] + 0.8, 0.4, lambda a: E.pilula(c, "está: 33º lugar", XE + 300, 880, 50, "g", fundo=CERTO, a=a), sobe=6)
        X = 1040
        E.foco(c, t, C["s15"], 0.4, lambda a: E.escreve(c, "e o 50?", X, 340, 66, "i", CLARO, a))
        fx_em(c, t, C["s15"] + 0.6, [("3", BR), ("n", CLARO), (" + 1 = 50", BR)], X, 480, 90)
        fx_em(c, t, C["s15.a"], [("3", BR), ("n", CLARO), (" = 49", BR)], X + 60, 620, 90)
        fx_em(c, t, C["s15.b"], [("n = 49 ÷ 3 = 16,33…", BR)], X, 760, 80)
        if t >= C["s15.b"] + 0.8:
            E.risco(c, X - 10, 790, X + 760, 720, t, C["s15.b"] + 0.8, largura=10)
        E.foco(c, t, C["s15.c"], 0.4, lambda a: E.pilula(c, "o 50 não está", X + 300, 880, 50, "g", fundo=ERRADO, a=a), sobe=6)
    E.saida(c, t, C["s16"] - 0.1, s14_15)
    if t < C["s16"]:
        return
    E.frase(c, t, C["s16.a"], [("posição", "g", 90, BR), ("é", "i", 84, CLARO), ("inteira:", "g", 90, BR)], W / 2, 260, "center")
    E.foco(c, t, C["s16.a"] + 0.8, 0.4, lambda a: centro(c, "1, 2, 3, 4, …", W / 2, 400, 90, "g", CLARO, a))
    E.foco(c, t, C["s16.b"], 0.4, lambda a: E.pilula(c, "regra do anterior: não volta direto", W / 2, 620, 54, "g", fundo=CLARO, cor="#07070F", a=a))
    E.foco(c, t, C["s16.c"], 0.4, lambda a: E.pilula(c, "escreva os termos até passar do número", W / 2, 790, 54, "g", fundo=BR, cor="#07070F", a=a))


# ---------------- questão ----------------
LEI2 = an("n") + [(" = 5", SAI), ("n", ENT), (" − 2", SAI)]


def b_questao(c, t, C, b):
    E.frase(c, t, C["s17"], ps("hora de testar", "i", 72, COR), XE, 170)
    fx_em(c, t, C["s17.a"], LEI2, XE, 320, 96)
    E.foco(c, t, C["s17.b"], 0.4, lambda a: (E.escreve(c, "1)", XE, 450, 64, "g", COR, a), fx(c, an(20) + [(" = ?", SAI)], XE + 90, 450, 76, a)))
    E.foco(c, t, C["s17.c"], 0.4, lambda a: (E.escreve(c, "2)", XE, 560, 64, "g", COR, a), E.escreve(c, "em que posição está o 73?", XE + 90, 560, 64, "i", TINTA, a)))
    fx_em(c, t, C["s17.d"], an(1) + [(" = 1   e   ", SAI)] + an("n+1") + [(" = 2 · ", SAI)] + an("n") + [(" + 3", SAI)], XE, 740, 80)
    E.foco(c, t, C["s17.e"], 0.4, lambda a: (E.escreve(c, "3)", XE, 880, 64, "g", COR, a), fx(c, an(4) + [(" = ?", SAI)], XE + 90, 880, 76, a)))
    if t >= C["s18"]:
        E.relogio(c, t, C["s18.a"], 1580, 520, 150)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    def s19():
        fx_em(c, t, C["s19"] + 0.8, an(20) + [(" = 5 · ", SAI), ("20", ENT), (" − 2", SAI)], XE, 230, 90)
        fx_em(c, t, C["s19.a"], [("= 100 − 2", SAI)], XE + 200, 360, 90)
        fx_em(c, t, C["s19.b"], [("= 98", COR)], XE + 700, 360, 90)
        E.foco(c, t, C["s19.b"] + 0.6, 0.4, lambda a: E.pilula(c, "posição → calcule", 1500, 230, 44, "g", fundo=ENT, a=a), sobe=6)
        E.foco(c, t, C["s19.c"] - 1.2, 0.4, lambda a: E.pilula(c, "valor → equação", 1500, 560, 44, "g", fundo=TINTA, a=a), sobe=6)
        fx_em(c, t, C["s19.c"], [("5", SAI), ("n", ENT), (" − 2 = 73", SAI)], XE, 580, 90)
        fx_em(c, t, C["s19.d"], [("5", SAI), ("n", ENT), (" = 75", SAI)], XE + 60, 720, 90)
        fx_em(c, t, C["s19.e"], [("n", ENT), (" = 15", COR)], XE + 120, 860, 90)
        bola_res(c, t, C["s19.e"] + 0.5, "15º lugar", 1500, 820, 140, 56)
    E.saida(c, t, C["s20"] - 0.1, s19)
    if t < C["s20"]:
        return
    fx_em(c, t, C["s20"], an(1) + [(" = 1   e   ", SAI)] + an("n+1") + [(" = 2 · ", SAI)] + an("n") + [(" + 3", SAI)], W / 2, 190, 80, "center")
    s, cy = 160, 560
    xs = xs_fila(260, 4, s, 140)
    vals = ["1", "5", "13", "29"]
    ks = [C["s20"] + 0.8, C["s20.a"], C["s20.b"], C["s20.c"]]
    for i in range(4):
        casa_em(c, t, C["s20"] + 0.6 + 0.1 * i, xs[i], cy, vals[i] if t >= ks[i] else "?", ordinal(i + 1), s, luz=pulso(t, ks[i], 1.4))
    passos(c, t, xs, cy, [k - 0.5 for k in ks[1:]], "×2 +3", s)
    for k, txt, i in ((C["s20.a"], "2 · 1 + 3 = 5", 1), (C["s20.b"], "2 · 5 + 3 = 13", 2), (C["s20.c"], "2 · 13 + 3 = 29", 3)):
        E.saida(c, t, (ks[i + 1] - 0.2) if i < 3 else C["s20.d"] - 0.1,
                lambda k=k, txt=txt: fx_em(c, t, k + 0.2, [(txt, TINTA2)], W / 2, 860, 70, "center"))
    bola_res(c, t, C["s20.d"], an(4, BR, BR) + [(" = 29", BR)], W / 2, 870, 150, 66)


# ---------------- fechamento ----------------
def palitos(c, x, y, n, l=90, a=1.0, cor=None):
    """fileira de n quadradinhos de palitos, lado l; (x, y) = canto de cima à esquerda"""
    if a <= 0:
        return
    cor = cor or TINTA
    g = 8
    for i in range(n):
        x0 = x + i * l
        M.line(c, x0 + g, y, x0 + l - g, y, cor, a, 9)
        M.line(c, x0 + g, y + l, x0 + l - g, y + l, cor, a, 9)
    for i in range(n + 1):
        M.line(c, x + i * l, y + g, x + i * l, y + l - g, cor, a, 9)


def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s21"], [("resumindo", "i", 92, COR)], W / 2, 220, "center")
        itens = (("s21.a", [("embaixo:", "i", 80), ("posição;", "g", 84, COR), ("termo:", "i", 80), ("valor", "g", 84)]),
                 ("s21.b", [("lei", "i", 80), ("em", "i", 80), ("n:", "g", 84, COR), ("troque", "i", 80), ("e", "i", 80), ("calcule", "g", 84)]),
                 ("s21.c", [("regra", "i", 80), ("do", "i", 80), ("anterior:", "g", 84), ("passo", "i", 80), ("a", "i", 80), ("passo", "g", 84, COR)]))
        for i, (k, partes) in enumerate(itens):
            y = 430 + i * 190
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 260, y - 30, 56, a=a),
                                                         E.escreve(c, str(i + 1), 260 - E.larg(str(i + 1), "g", 64) / 2, y - 7, 64, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, partes, 360, y)
    E.saida(c, t, C["s22"] - 0.1, resumo)
    if t < C["s22"]:
        return
    E.frase(c, t, C["s22"], [("próxima", "i", 84), ("aula", "i", 84)], XE, 260)
    E.frase(c, t, C["s22"] + 0.8, [("padrões", "g", 120, COR)], XE, 400)
    E.frase(c, t, C["s22"] + 1.1, [("em", "i", 110), ("figuras", "g", 120, COR)], XE, 530)
    for i, n in enumerate((1, 2, 3)):
        E.foco(c, t, C["s22.a"] + 0.4 * i, 0.4, lambda a, i=i, n=n: palitos(c, XE + [0, 160, 410][i], 600, n, 70, a))
    E.foco(c, t, C["s22.b"], 0.4, lambda a: (E.escreve(c, "figura 50:", XE, 820, 66, "i", TINTA, a),
                                             E.escreve(c, "quantos palitos?", XE + 310, 820, 66, "g", COR, a)))
    E.foco(c, t, C["s22.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1450, 420, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s22.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1780, 1580, p), lerp(720, 445, p), ep(t, C["s22.c"] + 0.2, 0.4))
    E.frase(c, t, C["s22.d"], [("bons", "i", 110), ("estudos!", "i", 110, COR)], 1450, 990, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, sequencia=b_sequencia, lei=b_lei, recorrencia=b_recorrencia, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
