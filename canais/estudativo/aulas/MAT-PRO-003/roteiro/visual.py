"""Visual — Estudativo · MAT-PRO-003: padrões que se repetem, o resto manda.

Linguagem visual da trilha Progressões (definida em MAT-PRO-001): posição em índigo (ENT), termo / valor em preto (SAI); casa() = caixa
com o valor dentro e a posição embaixo; an(k) escreve a₁, aₙ; setas curvas com a regra numa pílula; atalho no palco escuro.
Nesta aula: a fila A B C D em blocos de quatro, com uma chave "volta n" em cima de cada bloco; as 506 voltas viram uma faixa cinza só,
e o resto anda casa a casa com setas "+1", "+2"; a divisão com resto numa linha, com o resto aceso (conta()); a roda dos sete dias
(roda()) com o ponteiro que gira as voltas inteiras e depois anda o resto; dois trilhos de 12 e 18 dias que se encontram no 36."""
import math
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Matemática", "Progressões")
COR, CLARO = E.COR_TEXTO, E.CLARO
ENT, SAI = COR, TINTA  # posição / índice · termo / valor
ARQUIVO_FINAL = "estudativo_MAT-PRO-003_padroes_que_se_repetem.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("ciclo", "dias", "ciclos", "atalho", "questao", "fim"))
BR = "#FFFFFF"

assert divmod(2026, 4) == (506, 2) and 4 * 506 == 2024 and "ABCD"[(2026 - 1) % 4] == "B"
assert divmod(2028, 4) == (507, 0) and "ABCD"[(2028 - 1) % 4] == "D" and divmod(26, 4) == (6, 2)
assert divmod(100, 7) == (14, 2) and ["dom", "seg", "ter", "qua", "qui", "sex", "sáb"][(2 + 100) % 7] == "qui"
assert math.lcm(12, 18) == 36 and divmod(36, 7) == (5, 1) and (1 + 36) % 7 == 2  # segunda + 36 = terça
assert divmod(100, 3) == (33, 1) and divmod(45, 7) == (6, 3) and (6 + 45) % 7 == 2  # sábado + 45 = terça


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




# ---------------- peças desta aula ----------------
DIAS = ["dom", "seg", "ter", "qua", "qui", "sex", "sáb"]
DOM, SEG, TER, QUA, QUI, SEX, SAB = range(7)
LUZES = {"vermelho": "#E53935", "azul": "#1E6FE0", "verde": "#2E9E4A"}


def roda(c, cx, cy, r, pos, a=1.0, acesa=None, rd=58, escuro=False):
    """roda dos sete dias (domingo no alto, sentido horário) com ponteiro em `pos` (pode ser fracionário: o ponteiro anda).
    acesa = índice do dia em destaque (preenchido de índigo)"""
    if a <= 0:
        return
    tinta = BR if escuro else TINTA
    c.drawCircle(cx, cy, r, M.paint(CLARO if escuro else FIO, a, stroke=6))
    ang = lambda i: math.radians(-90 + i * 360 / 7)
    for i, d in enumerate(DIAS):
        x, y = cx + r * math.cos(ang(i)), cy + r * math.sin(ang(i))
        luz = acesa == i
        c.drawCircle(x, y, rd, M.paint(COR if luz else ("#14142A" if escuro else "#FFFFFF"), a))
        c.drawCircle(x, y, rd, M.paint(CLARO if escuro else COR, a, stroke=5))
        centro(c, d, x, y + 15, 42, "b", BR if luz else tinta, a)
    th = ang(pos)
    L = r - rd - 26
    M.arrow(c, cx, cy, cx + L * math.cos(th), cy + L * math.sin(th), COR if not escuro else CLARO, a, 10, 30)
    c.drawCircle(cx, cy, 16, M.paint(tinta, a))


def anda(t, t0, de, passos, d=None):
    """posição do ponteiro: sai de `de` e anda `passos` casas a partir de t0 (cada casa em 0,45 s, ou em d no total)"""
    d = d or 0.45 * max(1, passos)
    return de + passos * ease_io(prog(t, t0, d))


def letra_casa(c, cx, cy, v, pos, a=1.0, s=100, luz=0.0, borda=None, cor_val=None):
    casa(c, cx, cy, v, pos, a, s, borda=borda, cor_val=cor_val, luz=luz, size=s * 0.5, pos_size=34)


def luz_cor(c, cx, cy, r, nome, a=1.0):
    """luz da fila: esfera na cor dela"""
    if a > 0:
        E.bola(c, cx, cy, r, LUZES[nome], a)


def conta(c, t, t0, dividendo, divisor, q, resto, x, y, size=96, cor_r=None):
    """a divisão com resto numa linha: "2.026 ÷ 4 = 506, resto 2" (o resto aceso)"""
    fx_em(c, t, t0, [(f"{dividendo} ÷ {divisor} = {q}", SAI), (",  resto ", TINTA2), (str(resto), cor_r or COR)], x, y, size)


# ---------------- gancho ----------------
FILA = "ABCDABCDABCD"


def b_gancho(c, t, C, b):
    def cena1():
        xs = xs_fila(XE, 12, 100, 14)
        for i, v in enumerate(FILA[:8]):
            E.foco(c, t, C["s01.a"] + 0.3 * (i % 4) + (1.4 if i >= 4 else 0), 0.4,
                   lambda a, i=i, v=v: letra_casa(c, xs[i], 330, v, ordinal(i + 1), a), sobe=8)
        E.foco(c, t, C["s01.a"] + 3.0, 0.4, lambda a: reticencias(c, xs[8] + 20, 330, a))
        E.foco(c, t, C["s01.b"], 0.5, lambda a: letra_casa(c, 1400, 330, "?", "2.026º", a, 130, borda=TINTA))
        E.frase(c, t, C["s01.b"] + 2.4, ps("sem escrever duas mil letras", "i", 62, TINTA2), XE, 640, passo=0.08)
        E.frase(c, t, C["s01.c"], [("basta", "i", 90), ("uma", "i", 90), ("divisão", "g", 96, COR)], XE, 830)
    E.saida(c, t, C["s02"] - 0.1, cena1)
    if t < C["s02"]:
        return
    tb, te = C["s02.a"], C["s02.end"]
    E.foco(c, t, te - 1.8, 0.7, lambda a: E.bola(c, 1480, 540, 290 * ease_back(prog(t, te - 1.8, 0.7))), blur=0)
    E.frase(c, t, tb, ps("até o fim da aula", "i", 84), XE, 300)
    E.frase(c, t, tb + 1.2, [("qualquer", "i", 100), ("posição", "g", 110, COR)], XE, 470)
    E.frase(c, t, tb + 3.6, [("o", "i", 100), ("dia", "g", 110, COR), ("da", "i", 100), ("semana", "g", 110, COR)], XE, 640)
    E.foco(c, t, te - 1.4, 0.5, lambda a: (E.escreve(c, "+ atalho", 1320, 525, 84, "g", BR, a),
                                           E.escreve(c, "de prova", 1340, 610, 84, "i", BR, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.linha(c, t, [("você", "i", 84, TINTA, C["s03"]), ("precisa", "i", 84, TINTA, C["s03"] + 0.2), ("de", "i", 84, TINTA, C["s03"] + 0.4),
                   ("3", "g", 90, COR, C["s03"] + 0.6), ("coisas", "i", 84, TINTA, C["s03"] + 0.8)], W / 2, 220, "center")
    itens = (("s03.a", lambda a, y: (fx(c, [("17 ÷ 5 = 3", SAI), (",  resto ", TINTA2), ("2", COR)], 430, y, 96, a),)),
             ("s03.b", lambda a, y: (fx(c, [("MMC(12, 18) = 36", SAI)], 430, y, 96, a),
                                     E.escreve(c, "encontros que se repetem", 1250, y, 54, "i", TINTA2, a))),
             ("s03.c", lambda a, y: (letra_casa(c, 490, y - 30, "B", None, a, 110),
                                     E.escreve(c, "termo", 580, y - 10, 60, "g", TINTA, a),
                                     E.escreve(c, "e a posição", 800, y - 10, 60, "i", TINTA, a),
                                     E.escreve(c, "2º", 1140, y - 10, 70, "g", COR, a))))
    for i, (k, fn) in enumerate(itens):
        y = 450 + i * 210
        E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 300, y - 30, 56, a=a),
                                                     E.escreve(c, str(i + 1), 300 - E.larg(str(i + 1), "g", 64) / 2, y - 7, 64, "g", BR, a)))
        E.foco(c, t, C[k] + 0.2, 0.5, lambda a, fn=fn, y=y: fn(a, y))


# ---------------- o ciclo ----------------
def b_ciclo(c, t, C, b):
    if t < C["s05"]:
        xs = xs_fila(XE, 12, 100, 14)
        Y = 400
        for i, v in enumerate(FILA):
            blk = i // 4
            lz = ep(t, C["s04.c"] + 0.4 * blk, 0.3) if v == "D" else 0
            E.foco(c, t, C["s04"] - 1.0 + 0.05 * i, 0.3, lambda a, i=i, v=v, lz=lz: letra_casa(c, xs[i], Y, v, ordinal(i + 1), a, luz=lz), sobe=6)
        for blk in range(3):
            q = ep(t, C["s04.a"] + 0.4 * blk, 0.5)
            if q > 0:
                x0, x1 = xs[4 * blk] - 50, xs[4 * blk + 3] + 50
                E.chave(c, x0, x1, Y - 80, COR, q, -24)
                E.foco(c, t, C["s04.b"] + 0.3 * blk, 0.4, lambda a, x0=x0, x1=x1, blk=blk: E.pilula(c, f"volta {blk + 1}", (x0 + x1) / 2, Y - 150, 40, "g", a=a), sobe=6)
        E.frase(c, t, C["s04.a"], [("blocos", "g", 76, COR), ("de", "i", 76), ("4", "g", 80, COR)], XE, 190)
        E.foco(c, t, C["s04.c"] + 1.4, 0.4, lambda a: (E.escreve(c, "D nas posições 4, 8, 12:", XE, 700, 64, "i", TINTA, a),
                                                       E.escreve(c, "múltiplos de 4", XE + 640, 700, 70, "g", COR, a)))
        return
    if t < C["s07"]:
        conta(c, t, C["s05.a"], "2.026", 4, 506, 2, XE, 220, 96)
        Y, s = 560, 120
        q = ep(t, C["s05.b"], 0.6)
        if q > 0:  # as 506 voltas completas, num bloco só
            M.rrect(c, XE, Y - s / 2, 640 * q, s, 20, CINZA, 0.25)
            E.foco(c, t, C["s05.b"] + 0.3, 0.4, lambda a: E.escreve(c, "506 voltas completas", XE + 40, Y + 18, 54, "g", TINTA, a))
        x1, x2, x3 = 920, 1080, 1240
        casa_em(c, t, C["s05.c"], x1, Y, "D", "2.024º", s, size=s * 0.5, pos_size=36)
        E.foco(c, t, C["s05.c"] + 0.6, 0.4, lambda a: E.escreve(c, "4 × 506 = 2.024", XE, 820, 64, "b", TINTA2, a))
        lzA = ep(t, C["s06.b"], 0.3)
        lzB = ep(t, C["s06.b"] + 0.6, 0.3)
        casa_em(c, t, C["s05.c"] + 0.4, x2, Y, "A" if t >= C["s06.b"] else "?", "2.025º", s, size=s * 0.5, pos_size=36, luz=lzA)
        casa_em(c, t, C["s05.c"] + 0.6, x3, Y, "B" if t >= C["s06.b"] + 0.6 else "?", "2.026º", s, size=s * 0.5, pos_size=36, luz=lzB,
                borda=CERTO if t >= C["s06.c"] else None)
        for k, (xa, xb) in enumerate(((x1, x2), (x2, x3))):
            seta_curva(c, t, C["s06.a"] + 0.5 * k, (xa + 20, Y - s / 2 - 8), (xb - 20, Y - s / 2 - 8), 50, f"+{k + 1}", size=32)
        E.foco(c, t, C["s06.a"], 0.4, lambda a: E.pilula(c, "o resto: anda 2 casas", 1460, 300, 44, "g", a=a), sobe=6)
        bola_res(c, t, C["s06.c"], "B", 1600, 560, 100, 110)
        E.foco(c, t, C["s06.d"], 0.4, lambda a: E.pilula(c, "quem manda é o resto", 1340, 940, 60, "g", a=a), sobe=6)
        return
    # a tabela do resto
    E.frase(c, t, C["s07"], [("resto", "g", 90, COR), ("→", "g", 80, TINTA2), ("letra", "g", 90)], XE, 220)
    for i, (k, r_, v) in enumerate((("s07.a", "1", "A"), ("s07.b", "2", "B"), ("s07.c", "3", "C"), ("s07.d", "0", "D"))):
        x = 330 + i * 380
        E.foco(c, t, C[k], 0.4, lambda a, x=x, r_=r_: (E.escreve(c, "resto", x - 110, 420, 50, "i", TINTA2, a),
                                                      E.escreve(c, r_, x + 50, 430, 100, "g", COR, a)), sobe=6)
        casa_em(c, t, C[k] + 0.2, x, 620, v, None, 150, size=80)
    E.foco(c, t, C["s07.d"] + 0.6, 0.4, lambda a: E.pilula(c, "a última do bloco", 330 + 3 * 380, 790, 44, "g", fundo=TINTA, a=a), sobe=6)


# ---------------- dias da semana ----------------
RX, RY, RR = 1360, 560, 300


def b_dias(c, t, C, b):
    acesa = None
    pos = TER
    if t >= C["s09.b"]:
        pos = TER + 7 * 14 * ease_io(prog(t, C["s09.b"], 1.6))
    if t >= C["s09.c"]:
        pos = TER + 98 + 2 * ease_io(prog(t, C["s09.c"], 1.0))
    if t >= C["s10.b"]:
        pos = TER + 7 * ease_io(prog(t, C["s10.b"] + 0.4, 1.2))
    if t >= C["s08.b"] and t < C["s09.b"]:
        acesa = TER
    if t >= C["s09.d"] and t < C["s10.b"]:
        acesa = QUI
    if t >= C["s10.b"] + 1.6:
        acesa = TER
    E.foco(c, t, C["s08.a"], 0.5, lambda a: roda(c, RX, RY, RR, pos % 7, a, acesa))
    E.frase(c, t, C["s08.a"], [("bloco", "i", 76), ("de", "i", 76), ("7", "g", 84, COR), ("dias", "i", 76)], XE, 220)

    def s08_09():
        E.frase(c, t, C["s08.b"], [("hoje:", "i", 70), ("terça", "g", 76, COR)], XE, 340)
        E.frase(c, t, C["s08.c"], [("daqui", "i", 70), ("a", "i", 70), ("100", "g", 80, COR), ("dias?", "i", 70)], XE, 450)
        conta(c, t, C["s09.a"], "100", 7, 14, 2, XE, 620, 84)
        E.foco(c, t, C["s09.b"], 0.4, lambda a: E.escreve(c, "14 voltas: terça de novo", XE, 720, 52, "i", TINTA2, a))
        E.foco(c, t, C["s09.c"], 0.4, lambda a: E.escreve(c, "+2: quarta, quinta", XE, 810, 60, "g", COR, a))
        E.foco(c, t, C["s09.d"], 0.4, lambda a: E.pilula(c, "quinta-feira", XE + 260, 940, 64, "g", fundo=CERTO, a=a), sobe=6)
    E.saida(c, t, C["s10"] - 0.1, s08_09)
    if t < C["s10"]:
        return
    E.frase(c, t, C["s10.a"], [("cada", "i", 66), ("volta", "g", 70, COR), ("de", "i", 66), ("7", "g", 70)], XE, 380)
    E.frase(c, t, C["s10.a"] + 1.0, ps("fecha no dia de hoje", "i", 66), XE, 470)
    E.foco(c, t, C["s10.b"], 0.4, lambda a: fx(c, [("resto ", TINTA), ("0", COR), (" = hoje", TINTA)], XE, 650, 96, a))
    E.foco(c, t, C["s10.b"] + 1.0, 0.4, lambda a: E.escreve(c, "daqui a 7 dias: terça", XE, 750, 56, "i", TINTA2, a))
    E.frase(c, t, lerp(C["s10.b"], C["s10.end"], 0.55), [("igual", "i", 54), ("às", "i", 54), ("letras:", "i", 54), ("resto 0", "g", 58, COR),
                                                         ("=", "g", 56), ("fim", "g", 58), ("da", "i", 54), ("volta", "g", 58)], XE, 900, passo=0.1)


# ---------------- dois ciclos ----------------
def trilho(c, t, t0, y, passo, rot, cor, vx, fim=36, t_fim=None):
    a = ep(t, t0, 0.5)
    if a <= 0:
        return
    M.line(c, vx(0), y, vx(fim) + 30, y, cor, a, 5)
    E.escreve(c, rot, XE, y + 16, 48, "g", cor, a)
    for k, v in enumerate(range(0, fim + 1, passo)):
        q = ep(t, t_fim if (v == fim and t_fim is not None) else t0 + 0.2 + 0.2 * k, 0.3)
        c.drawCircle(vx(v), y, 18, M.paint(cor, q))
        centro(c, str(v), vx(v), y + 60, 38, "b", cor, q)


def b_ciclos(c, t, C, b):
    E.frase(c, t, C["s11.a"], [("dois", "g", 84, COR), ("ciclos", "i", 80)], XE, 190)
    vx = lambda v: 480 + v * 36
    trilho(c, t, C["s11.b"], 340, 12, "a cada 12", COR, vx, t_fim=C["s12.b"])
    trilho(c, t, C["s11.c"], 500, 18, "a cada 18", TINTA, vx, t_fim=C["s12.b"])
    E.foco(c, t, C["s11.d"], 0.4, lambda a: E.pilula(c, "hoje: segunda, juntas", vx(0) + 60, 640, 40, "g", fundo=TINTA2, a=a), sobe=6)
    q = ep(t, C["s12.b"], 0.5)
    if q > 0:
        M.line(c, vx(36), 300, vx(36), 560, CERTO, q, 6, dash=E.TRACO)
        anel(c, t, C["s12.b"], vx(36), 340, CERTO)
        anel(c, t, C["s12.b"] + 0.2, vx(36), 500, CERTO)
    E.foco(c, t, C["s12.a"], 0.4, lambda a: E.pilula(c, "voltam a coincidir: MMC", 1500, 190, 44, "g", a=a), sobe=6)
    fx_em(c, t, C["s12.b"], [("MMC(12, 18) = ", SAI), ("36", COR)], XE, 760, 80)
    conta(c, t, C["s12.c"], "36", 7, 5, 1, XE, 880, 80)
    E.foco(c, t, C["s12.c"] + 1.6, 0.4, lambda a: E.escreve(c, "segunda + 1 = terça", XE, 970, 54, "i", TINTA2, a))
    bola_res(c, t, C["s12.d"], "terça", 1560, 840, 130, 70, "daqui a 36 dias")


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s13.a"], [("cuidado:", "g", 84, ERRADO), ("o", "i", 84), ("resto", "g", 84), ("zero", "g", 84, COR)], W / 2, 180, "center")
    xs = xs_fila(XE, 8, 100, 14)
    Y = 360
    certo = C["s14.a"]
    for i, v in enumerate(FILA[:8]):
        lz = pulso(t, certo + 0.2, 4.0) if v == "D" else 0
        E.foco(c, t, C["s13.a"] + 0.05 * i, 0.3, lambda a, i=i, v=v, lz=lz: letra_casa(c, xs[i], Y, v, ordinal(i + 1), a, luz=lz), sobe=6)
    E.foco(c, t, C["s13.a"] + 0.6, 0.4, lambda a: reticencias(c, xs[7] + 110, Y, a))
    if t < C["s14.b"]:
        casa_em(c, t, C["s13.b"], 1560, Y, "?", "2.028º", 130, size=64, pos_size=36, borda=TINTA)
    else:
        casa_em(c, t, C["s14.b"], 1560, Y, "D", "2.028º", 130, size=64, pos_size=36, borda=CERTO, luz=1)
    conta(c, t, C["s13.b"], "2.028", 4, 507, 0, XE, 620, 90)
    E.saida(c, t, certo - 0.1, lambda: (E.frase(c, t, C["s13.b"] + 3.0, ps("não sobrou nada… volta ao começo?", "i", 56, TINTA2), XE, 730, passo=0.08),
                                        E.foco(c, t, C["s13.c"], 0.4, lambda a: E.escreve(c, "A?", XE, 900, 120, "g", ERRADO, a))))
    if C["s13.c"] + 0.8 <= t < certo:
        E.risco(c, XE - 10, 920, XE + 190, 810, t, C["s13.c"] + 0.8, largura=12)
    E.foco(c, t, certo, 0.4, lambda a: (E.escreve(c, "resto 0:", XE, 760, 64, "g", COR, a),
                                       E.escreve(c, "a última volta acabou de fechar", XE + 300, 760, 60, "i", TINTA, a)))
    E.foco(c, t, certo + 1.6, 0.4, lambda a: E.escreve(c, "as voltas fecham em D: posições 4 e 8", XE, 860, 54, "i", TINTA2, a))
    bola_res(c, t, C["s14.b"], "D", 1560, 760, 110, 120)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def s15():
        E.frase(c, t, C["s15.a"], [("bloco", "i", 76, CLARO), ("de", "i", 76, CLARO), ("4:", "g", 80, BR), ("só", "i", 76, CLARO), ("os", "i", 76, CLARO),
                                   ("dois", "g", 80, BR), ("últimos", "g", 80, BR), ("algarismos", "i", 76, CLARO)], W / 2, 200, "center", passo=0.12)
        S = 220
        w1 = E.larg("2.0", "g", S)
        w2 = E.larg("26", "g", S)
        x0 = W / 2 - (w1 + w2) / 2
        q = ep(t, C["s15.b"], 0.4)
        E.foco(c, t, C["s15.a"] + 1.4, 0.5, lambda a: (E.escreve(c, "2.0", x0, 520, S, "g", lerp_a(BR, 0.35, q), a),
                                                       E.escreve(c, "26", x0 + w1, 520, S, "g", BR, a)))
        if q > 0:
            c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x0 + w1 - 4, 520 - S * 0.82, w2 + 24, S * 0.98), 24, 24), M.paint(CLARO, q, stroke=7))
        fx_em(c, t, C["s15.c"], [("26 ÷ 4 = 6", BR), (",  resto ", CLARO), ("2", BR)], W / 2, 760, 100, "center")
        E.foco(c, t, C["s15.d"], 0.4, lambda a: E.pilula(c, "o mesmo resto, de cabeça", W / 2, 900, 54, "g", fundo=CLARO, cor="#07070F", a=a))
    E.saida(c, t, C["s16"] - 0.1, s15)
    if t < C["s16"]:
        return
    E.frase(c, t, C["s16.a"], [("100", "g", 96, BR), ("=", "g", 90, CLARO), ("4", "g", 96, CLARO), ("×", "g", 90, CLARO), ("25", "g", 96, BR)], W / 2, 300, "center")
    E.foco(c, t, C["s16.a"] + 1.6, 0.4, lambda a: centro(c, "centenas e milhares fecham voltas inteiras", W / 2, 400, 52, "i", CLARO, a))
    E.frase(c, t, C["s16.b"], [("semana:", "i", 76, CLARO), ("bloco", "i", 76, CLARO), ("de", "i", 76, CLARO), ("7", "g", 84, BR)], W / 2, 600, "center")
    fx_em(c, t, C["s16.c"], [("100 ÷ 7 = 14", BR), (",  resto ", CLARO), ("2", BR)], W / 2, 740, 84, "center")
    E.foco(c, t, C["s16.d"], 0.4, lambda a: E.pilula(c, "faça a divisão inteira", W / 2, 900, 54, "g", fundo=BR, cor="#07070F", a=a))


def lerp_a(cor, k, q):
    """cor que apaga até k de opacidade conforme q (0..1)"""
    return E.mix(cor, "#07070F", (1 - k) * q)


# ---------------- questão ----------------
FCOR = ["vermelho", "azul", "verde"] * 2


def b_questao(c, t, C, b):
    E.frase(c, t, C["s17"], ps("hora de testar", "i", 72, COR), XE, 170)
    xs = xs_fila(XE, 7, 96, 30)
    for i, nome in enumerate(FCOR):
        E.foco(c, t, C["s17.a"] + 0.25 * i, 0.4, lambda a, i=i, nome=nome: (luz_cor(c, xs[i], 330, 46, nome, a),
                                                                          centro(c, ordinal(i + 1), xs[i], 420, 36, "b", COR, a)), sobe=6)
    E.foco(c, t, C["s17.a"] + 1.8, 0.4, lambda a: reticencias(c, xs[6], 330, a))
    E.foco(c, t, C["s17.b"], 0.4, lambda a: (E.bola(c, 1400, 330, 60, CINZA, a), centro(c, "?", 1400, 352, 64, "g", BR, a),
                                             centro(c, "100º", 1400, 440, 44, "b", COR, a)), sobe=6)
    E.foco(c, t, C["s17.b"], 0.4, lambda a: (E.escreve(c, "1)", XE, 600, 64, "g", COR, a), E.escreve(c, "a cor da posição 100", XE + 90, 600, 64, "i", TINTA, a)))
    E.foco(c, t, C["s17.c"], 0.4, lambda a: (E.escreve(c, "2)", XE, 720, 64, "g", COR, a), E.escreve(c, "hoje é sábado:", XE + 90, 720, 64, "i", TINTA, a)))
    E.foco(c, t, C["s17.d"] + 0.4, 0.4, lambda a: E.escreve(c, "e daqui a 45 dias?", XE + 90, 810, 64, "g", COR, a))
    if t >= C["s18"]:
        E.relogio(c, t, C["s18.a"], 1500, 720, 120)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    def s19():
        xs = xs_fila(XE, 3, 96, 30)
        for i, nome in enumerate(FCOR[:3]):
            E.foco(c, t, C["s19.a"] + 0.2 * i, 0.4, lambda a, i=i, nome=nome: (luz_cor(c, xs[i], 260, 46, nome, a),
                                                                             centro(c, ["resto 1", "resto 2", "resto 0"][i], xs[i], 350, 30, "b", COR, a)), sobe=6)
        E.foco(c, t, C["s19.a"], 0.4, lambda a: E.escreve(c, "bloco de 3 cores", 640, 280, 60, "i", TINTA2, a))
        conta(c, t, C["s19.b"], "100", 3, 33, 1, XE, 560, 96)
        E.foco(c, t, C["s19.c"], 0.4, lambda a: E.escreve(c, "resto 1 = a primeira cor", XE, 700, 60, "i", TINTA, a))
        E.foco(c, t, C["s19.c"] + 0.6, 0.5, lambda a: (E.bola(c, 1500, 560, 140, LUZES["vermelho"], a), centro(c, "vermelho", 1500, 580, 56, "g", BR, a)))
    E.saida(c, t, C["s20"] - 0.1, s19)
    if t < C["s20"]:
        return
    pos = SAB + 3 * ease_io(prog(t, C["s20.b"], 1.5))
    acesa = SAB if t < C["s20.b"] else (TER if t >= C["s20.c"] else None)
    E.foco(c, t, C["s20"], 0.5, lambda a: roda(c, RX, RY, RR, pos % 7, a, acesa))
    E.frase(c, t, C["s20"], [("hoje:", "i", 70), ("sábado", "g", 76, COR)], XE, 260)
    conta(c, t, C["s20.a"], "45", 7, 6, 3, XE, 440, 84)
    E.foco(c, t, C["s20.a"] + 1.2, 0.4, lambda a: E.escreve(c, "6 semanas: sábado de novo", XE, 540, 52, "i", TINTA2, a))
    E.foco(c, t, C["s20.b"], 0.4, lambda a: E.escreve(c, "+3: domingo, segunda, terça", XE, 660, 56, "g", COR, a))
    E.foco(c, t, C["s20.c"], 0.4, lambda a: E.pilula(c, "terça-feira", XE + 240, 820, 64, "g", fundo=CERTO, a=a), sobe=6)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s21"], [("resumindo", "i", 92, COR)], W / 2, 220, "center")
        itens = (("s21.a", [("divida", "g", 84), ("pelo", "i", 80), ("tamanho", "i", 80), ("do", "i", 80), ("bloco", "g", 84, COR)]),
                 ("s21.b", [("o", "i", 80), ("resto", "g", 84, COR), ("diz", "i", 80), ("onde", "i", 80), ("você", "i", 80), ("para", "g", 84)]),
                 ("s21.c", [("resto 0", "g", 84, COR), ("=", "g", 80), ("fim", "g", 84), ("de", "i", 80), ("uma", "i", 80), ("volta", "g", 84)]))
        for i, (k, partes) in enumerate(itens):
            y = 430 + i * 190
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 260, y - 30, 56, a=a),
                                                         E.escreve(c, str(i + 1), 260 - E.larg(str(i + 1), "g", 64) / 2, y - 7, 64, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, partes, 360, y)
    E.saida(c, t, C["s22"] - 0.1, resumo)
    if t < C["s22"]:
        return
    E.frase(c, t, C["s22"], [("próxima", "i", 84), ("aula", "i", 84)], XE, 200)
    xs = xs_fila(XE, 3, 120, 90)
    for i, v in enumerate(("5", "9", "13")):
        casa_em(c, t, C["s22.a"] + 0.3 * i, xs[i], 445, v, ordinal(i + 1), 120, pos_size=36)
    passos(c, t, xs, 445, [C["s22.a"] + 1.0, C["s22.a"] + 1.4], "+4", 120, size=30)
    E.frase(c, t, C["s22.b"], [("progressão", "g", 100, COR)], XE, 660)
    E.frase(c, t, C["s22.b"] + 0.3, [("aritmética", "g", 100, COR)], XE, 770)
    E.foco(c, t, C["s22.c"], 0.4, lambda a: fx(c, an(20) + [(" com uma fórmula", TINTA)], XE, 890, 60, a))
    E.foco(c, t, C["s22.d"], 0.4, lambda a: E.escreve(c, "parente da função afim", XE, 980, 54, "i", TINTA2, a))
    E.foco(c, t, C["s22.e"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1450, 420, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s22.e"] + 0.3, 0.8))
    E.cursor(c, lerp(1780, 1580, p), lerp(720, 445, p), ep(t, C["s22.e"] + 0.2, 0.4))
    E.frase(c, t, C["s22.f"], [("bons", "i", 110), ("estudos!", "i", 110, COR)], 1450, 990, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, ciclo=b_ciclo, dias=b_dias, ciclos=b_ciclos, erro=b_erro, atalho=b_atalho,
              questao=b_questao, resposta=b_resposta, fim=b_fim)
