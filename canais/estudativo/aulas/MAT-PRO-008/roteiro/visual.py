"""Visual — Estudativo · MAT-PRO-008: progressão geométrica, razão e termo geral.

Linguagem visual da trilha Progressões (MAT-PRO-001 e MAT-PRO-004): fila de caixas de borda índigo com o termo dentro (preto) e a
posição embaixo (índigo); a razão é o arco verde por cima das caixas, agora com "×2" no lugar do "+4" da PA; índice como índice
(aₙ: letra preta, índice índigo) com fx(); os saltos (n − 1) sobem para o expoente da razão q.
Gráfico na linguagem de Funções: E.plano com o eixo do tempo t em índigo e o do montante M em preto (eixos_pa()); montantes mês a mês
com E.ponto sobre a curva 1.000 · 1,1ᵗ (E.curva) e, para comparar, a reta tracejada de uma PA. Palco escuro só no atalho.
Peças locais: fx(), fx_em(), caixa(), fila(), pula(), resultado(), caixa_em(), eixos_pa() (as da MAT-PRO-004), mil()."""
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Matemática", "Progressões")
COR, CLARO = E.COR_TEXTO, E.CLARO
ENT, SAI, RAZ = COR, TINTA, CERTO  # posição n · termo aₙ · razão
ARQUIVO_FINAL = "estudativo_MAT-PRO-008_progressao_geometrica_razao_e_termo_geral.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("pg", "formula", "juros", "atalho", "questao", "fim"))
BR = "#FFFFFF"

a_ = lambda n: 3 * 2 ** (n - 1)
assert [a_(n) for n in (1, 2, 3, 4, 5, 8)] == [3, 6, 12, 24, 48, 384] and 2 ** 7 == 128 and 3 * 128 == 384
assert 3 + 7 * 2 == 17 and 2 ** 4 == 16 and 24 * 16 == 384 and 2 ** 10 == 1024
assert [round(1000 * 1.1 ** t) for t in range(4)] == [1000, 1100, 1210, 1331] and round(1000 * 1.1 ** 10) == 2594
assert 2 * 3 ** 5 == 486 and 3 ** 5 == 243 and round(40000 * 0.9) == 36000 and round(36000 * 0.9) == 32400


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


def mil(v):
    return f"{int(round(v)):,}".replace(",", ".")


# ---------------- peças da trilha ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def _pedacos(s):
    """separa "a_{20} = 5" em [(0, "a"), (1, "20"), (0, " = 5")]: 1 = índice"""
    out, buf, i = [], "", 0
    while i < len(s):
        if s[i] == "_":
            if buf:
                out.append((0, buf))
                buf = ""
            if s[i + 1] == "{":
                j = s.index("}", i)
                out.append((1, s[i + 2:j]))
                i = j + 1
            else:
                out.append((1, s[i + 1]))
                i += 2
        else:
            buf += s[i]
            i += 1
    if buf:
        out.append((0, buf))
    return out


def _w(s, size, est):
    return sum(E.formula(None, p, 0, 0, size * (0.6 if k else 1), est, a=0) + (size * 0.03 if k else 0) for k, p in _pedacos(s))


def fx(c, partes, x, y, size, a=1.0, align="left", est="g", cor=None):
    """fórmula com índice de verdade (a_n, a_1, a_{20}); partes = texto ou [(texto, cor)]. Devolve [(x0, largura)] de cada parte.
    Como na MAT-PRO-001: em pedaço preto (SAI), a letra fica preta e o índice (a posição) sai em índigo"""
    if isinstance(partes, str):
        partes = [(partes, cor or TINTA)]
    ws = [_w(s, size, est) + (size * 0.06 if s.startswith("^") else 0) for s, _ in partes]  # expoente solto: um respiro depois da base
    xx = x - sum(ws) / 2 if align == "center" else x - sum(ws) if align == "right" else x
    out = []
    for (s, cr), w in zip(partes, ws):
        out.append((xx, w))
        if a > 0:
            px = xx + (size * 0.06 if s.startswith("^") else 0)
            for k, p in _pedacos(s):
                sz = size * (0.6 if k else 1)
                E.formula(c, p, px + (size * 0.01 if k else 0), y + (size * 0.2 if k else 0), sz, est, ENT if (k and cr == SAI) else cr, a)
                px += E.formula(None, p, 0, 0, sz, est, a=0) + (size * 0.03 if k else 0)
        xx += w
    return out


def fx_em(c, t, t0, partes, x, y, size, align="left", est="g", cor=None):
    E.foco(c, t, t0, 0.5, lambda a: fx(c, partes, x, y, size, a, align, est, cor))
    return fx(c, partes, x, y, size, 0, align, est, cor)


def caixa(c, cx, cy, w, h, val, a=1.0, pos=None, size=80, cor=None, borda=None, escuro=False, pos_size=44):
    """um termo: caixa de borda índigo com o valor dentro (preto) e a posição embaixo (índigo), como casa() da MAT-PRO-001"""
    if a <= 0:
        return
    rr = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2, cy - h / 2, w, h), 20, 20)
    c.drawRRect(rr, M.paint("#1A1830" if escuro else "#FFFFFF", a))
    c.drawRRect(rr, M.paint(borda or (CLARO if escuro else COR), a, stroke=5))
    if val is not None and val != "":
        fx(c, [(str(val), cor or (BR if escuro else SAI))], cx, cy + size * 0.36, size, a, "center")
    if pos:
        centro(c, pos, cx, cy + h / 2 + pos_size + 14, pos_size, "b", CLARO if escuro else ENT, a)


def fila(c, t, itens, cy, w=190, h=150, size=80, escuro=False, pos_size=44):
    """itens = [(cx, valor, posição, t0[, cor[, borda]])]; valor "…" = reticências sem caixa"""
    for it in itens:
        cx, val, pos, t0 = it[:4]
        cor = it[4] if len(it) > 4 else None
        borda = it[5] if len(it) > 5 else None
        if val == "…":
            E.foco(c, t, t0, 0.5, lambda a, cx=cx: centro(c, "…", cx, cy + 20, 90, "g", BR if escuro else TINTA2, a))
        else:
            E.foco(c, t, t0, 0.5, lambda a, cx=cx, val=val, pos=pos, cor=cor, borda=borda: caixa(
                c, cx, cy, w, h, val, a, pos, size, cor, borda, escuro, pos_size))


def pula(c, t, t0, x0, x1, ytopo, rot, cor=RAZ, alto=80, size=52):
    """a razão: arco por cima das caixas, de um termo para o seguinte"""
    E.salto(c, t, t0, x0, x1, ytopo - 8, alto, cor, rot, size=size)


def resultado(c, t, t0, s, cx, cy, r=110, cor=None):
    k = ease_back(prog(t, t0, 0.6))
    if k > 0:
        E.bola(c, cx, cy, r * k, cor)
        size = r * (0.62 if len(s) <= 3 else 0.5 if len(s) <= 5 else 0.4 if len(s) <= 8 else 0.33)
        E.foco(c, t, t0 + 0.2, 0.4, lambda a: centro(c, s, cx, cy + size * 0.36, size, "g", BR, a), sobe=0)


def par(c, xv, yv, x, y, size, a=1.0, align="left", est="g"):
    """par (posição, termo): posição em índigo, termo em preto"""
    partes = (("(", TINTA), (xv, ENT), (", ", TINTA), (yv, SAI), (")", TINTA))
    w = sum(E.larg(s, est, size) for s, _ in partes) + size * 0.04 * 4
    xx = x - w / 2 if align == "center" else x
    for s, cor in partes:
        E.escreve(c, s, xx, y, size, est, cor, a)
        xx += E.larg(s, est, size) + size * 0.04
    return w


def caixa_em(c, t, t0, x0, w, y, size, cor=None, d=0.5):
    """caixa pontilhada em volta de um trecho já escrito (x0 = início, y = linha de base)"""
    p = ep(t, t0, d)
    if p > 0:
        E.caixa_pontilhada(c, x0 - 16, y - size * 0.9, w + 32, size * 1.25, p, cor, p)


def eixos_pa(c, t, t0, P, nome_y="a_n", nome_x="n"):
    """depois de E.plano: o eixo das posições em índigo e os nomes n (índigo) e aₙ (preto)"""
    x, y, w, h = P.caixa
    if t >= t0:
        M.arrow(c, x - 10, P.oy, x + w + 44, P.oy, ENT, 1.0, 6, 22, ep(t, t0, 0.6))
    E.foco(c, t, t0 + 0.5, 0.4, lambda a: (fx(c, [(nome_x, ENT)], x + w + 30, P.oy + 70, 56, a),
                                          fx(c, [(nome_y, SAI)], P.ox + 24, y - 20, 56, a)))


# ---------------- gancho ----------------
GX = (300, 540, 780, 1020)


def b_gancho(c, t, C, b):
    def s01():
        cy = 420
        fila(c, t, [(x, v, f"{i + 1}º", C["s01.a"] + 0.48 * i) for i, (x, v) in enumerate(zip(GX, (3, 6, 12, 24)))], cy)
        for i in range(3):
            pula(c, t, C["s01.b"] + 0.3 * i, GX[i], GX[i + 1], cy - 75, "×2")
        fila(c, t, [(1260, "…", None, C["s01.c"] - 0.3)], cy)
        fim = t >= C["s01.d"]
        E.foco(c, t, C["s01.c"], 0.5, lambda a: caixa(c, 1520, cy, 210, 150, "384" if fim else "?", a, "8º", 80, COR if fim else CINZA))
        E.frase(c, t, C["s01.b"], [("cada", "i", 76), ("termo", "i", 76), ("é", "i", 76), ("o", "i", 76), ("dobro", "g", 72, RAZ), ("do", "i", 76), ("anterior", "i", 76)],
                W / 2, 720, "center")
        E.frase(c, t, C["s01.d"], [("uma", "i", 84), ("conta", "g", 80, COR), ("só", "i", 84)], W / 2, 880, "center")
    E.saida(c, t, C["s02"] - 0.1, s01)
    if t < C["s02"]:
        return
    E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 80), XE, 300)
    E.frase(c, t, C["s02.a"] + 1.4, [("a", "i", 110), ("razão", "g", 110, RAZ)], XE, 450)
    E.frase(c, t, C["s02.a"] + 2.4, [("e", "i", 110), ("qualquer", "i", 110), ("termo", "g", 110, COR)], XE, 600)
    PG = E.Plano(1200, 250, 520, 480, 0, 6, 0, 2000)
    if t >= C["s02.b"] - 0.2:
        E.plano(c, t, C["s02.b"] - 0.2, *PG.caixa, 0, 6, 0, 2000, passo=1, passo_y=500, rotulos=False, nomes=("", ""), size=30)
        eixos_pa(c, t, C["s02.b"] - 0.2, PG, "M", "t")
        E.curva(c, t, C["s02.b"] + 0.2, PG, lambda x: 1000 * 1.1 ** x, 0, 6, d=0.9, cor=COR, largura=6)
        for i in range(0, 7):
            E.ponto(c, t, C["s02.b"] + 0.2 + 0.12 * i, PG, i, 1000 * 1.1 ** i, cor=COR, r=11)
        E.frase(c, t, C["s02.b"], [("juros", "g", 66, COR), ("compostos", "g", 66, COR)], 1460, 880, "center")
    E.foco(c, t, C["s02.b"] + 1.4, 0.5, lambda a: E.pilula(c, "+ atalho de prova", XE + 300, 780, 56, "g", a=a))


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], ps("você só precisa de", "i", 84), XE, 410)
    E.foco(c, t, C["s03"] + 0.6, 0.5, lambda a: E.escreve(c, "3", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03"] + 0.75, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 900, 880
    itens = (("s03.a", "termo geral da PA", [("a_n", SAI), (" = ", TINTA), ("a_1", SAI), (" + (", TINTA), ("n", ENT), (" − 1) · ", TINTA), ("r", RAZ)]),
             ("s03.b", "juros compostos", [("1.000 → 1.100 → 1.210", COR)]),
             ("s03.c", "exponencial", [("fator", COR), ("^{tempo}", ENT)]))
    for i, (k, l1, l2) in enumerate(itens):
        y = 190 + i * 240
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 196, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 62)], x + 44, y + 84)
        fx_em(c, t, C[k] + 0.3, l2, x + 44, y + 166, 68)
    alvo = [(x + w - 30, 190 + i * 240 + 170) for i in range(3)]
    q1, q2 = ease_io(prog(t, C["s03.b"] - 0.35, 0.5)), ease_io(prog(t, C["s03.c"] - 0.35, 0.5))
    E.cursor(c, alvo[0][0], lerp(lerp(alvo[0][1], alvo[1][1], q1), alvo[2][1], q2), ep(t, C["s03.a"], 0.4))


# ---------------- o que é PG ----------------
PX = (480, 760, 1040, 1320)


def b_pg(c, t, C, b):
    def lista():
        cy = 330
        dest = {}
        if C["s05.b"] <= t < C["s05.c"]:
            dest = {0: RAZ, 1: RAZ}
        elif C["s05.c"] <= t < C["s05.d"]:
            dest = {1: RAZ, 2: RAZ}
        fila(c, t, [(x, v, f"{i + 1}º", C["s04"] + 0.15 * i, None, dest.get(i)) for i, (x, v) in enumerate(zip(PX, (3, 6, 12, 24)))], cy)
        fila(c, t, [(1540, "…", None, C["s04"] + 0.6)], cy)
        for i in range(3):
            pula(c, t, C["s04.a"] + 0.45 * i, PX[i], PX[i + 1], cy - 75, "×2")

        def s04():
            E.frase(c, t, C["s04.a"], ps("multiplica sempre pelo mesmo número", "i", 70), W / 2, 620, "center", passo=0.15)
            E.frase(c, t, C["s04.b"], [("progressão", "g", 100, COR), ("geométrica", "g", 100, COR)], W / 2, 770, "center")
            E.foco(c, t, C["s04.b"] + 0.8, 0.5, lambda a: E.pilula(c, "PG", W / 2, 870, 56, "g", a=a))
            E.frase(c, t, C["s04.c"], [("a", "i", 80), ("razão", "g", 80, RAZ)], 640, 1000, "center")
            E.frase(c, t, C["s04.d"], [("letra", "i", 80), ("q", "g", 96, RAZ)], 1280, 1000, "center")
        E.saida(c, t, C["s05"] - 0.1, s04)
        if t < C["s05"]:
            return
        E.frase(c, t, C["s05.a"], [("divida", "g", 76, RAZ), ("um", "i", 80), ("termo", "i", 80), ("pelo", "i", 80), ("anterior", "i", 80)], W / 2, 620, "center")
        fx_em(c, t, C["s05.b"], [("6 ÷ 3 = ", TINTA), ("2", RAZ)], XE + 60, 780, 96)
        fx_em(c, t, C["s05.c"], [("12 ÷ 6 = ", TINTA), ("2", RAZ)], XE + 60, 920, 96)
        resultado(c, t, C["s05.d"], "q = 2", 1560, 830, 130, RAZ)
        E.frase(c, t, C["s05.e"] - 1.6, [("na", "i", 64, TINTA2), ("PA,", "g", 60, TINTA2), ("subtraía", "i", 64, TINTA2)], 760, 780)
        E.frase(c, t, C["s05.e"], [("na", "i", 70), ("PG,", "g", 66, COR), ("divide", "g", 66, RAZ)], 760, 920)
    E.saida(c, t, C["s06"] - 0.1, lista)
    if t < C["s06"]:
        return
    E.frase(c, t, C["s06"], ps("a razão pode ser fração ou negativa", "i", 70), W / 2, 130, "center")
    y1, y2 = 420, 800
    XS = (420, 700, 980)
    fila(c, t, [(x, v, f"{i + 1}º", C["s06.a"] + 0.48 * i) for i, (x, v) in enumerate(zip(XS, (80, 40, 20)))], y1)
    for i in range(2):
        pula(c, t, C["s06.b"] + 0.3 * i, XS[i], XS[i + 1], y1 - 75, "×½")
    fx_em(c, t, C["s06.b"] + 0.4, [("q = ", TINTA), ("f{1}{2}", RAZ)], 1220, y1 + 30, 100)
    E.foco(c, t, C["s06.b"] + 0.6, 0.5, lambda a: E.escreve(c, "cai pela metade", 1230, y1 + 140, 52, "i", TINTA2, a))
    XS2 = (420, 640, 860, 1080)
    fila(c, t, [(x, v, f"{i + 1}º", C["s06.c"] + 0.4 * i) for i, (x, v) in enumerate(zip(XS2, ("1", "−2", "4", "−8")))], y2, 180, 150)
    for i in range(3):
        pula(c, t, C["s06.d"] + 0.3 * i, XS2[i], XS2[i + 1], y2 - 75, "×(−2)", size=42)
    fx_em(c, t, C["s06.d"] + 0.4, [("q = ", TINTA), ("−2", RAZ)], 1260, y2 + 36, 100)
    E.foco(c, t, C["s06.d"] + 0.8, 0.5, lambda a: E.escreve(c, "o sinal troca", 1270, y2 + 120, 52, "i", TINTA2, a))


# ---------------- saltos ----------------
SX = (300, 540, 780, 1020)


def b_saltos(c, t, C, b):
    cy = 380
    fila(c, t, [(x, v, f"{i + 1}º", C["s07"] + 0.15 * i) for i, (x, v) in enumerate(zip(SX, (3, 6, 12, 24)))], cy, 180, 140, 76)
    fila(c, t, [(1270, "…", None, C["s07"] + 0.6), (1540, "?", "8º", C["s07"] + 0.7, CINZA)], cy, 180, 140, 76)
    if t >= C["s07.a"]:
        E.chave(c, SX[0] - 90, 1540 + 90, cy + 140, COR, ep(t, C["s07.a"], 0.6), 26, 6)
        E.foco(c, t, C["s07.a"] + 0.3, 0.5, lambda a: fx(c, [("7", COR), (" saltos, como na PA", TINTA)], W / 2 + 60, cy + 250, 64, a, "center"))
    for i in range(3):
        pula(c, t, C["s07.b"] + 0.3 * i, SX[i], SX[i + 1], cy - 70, "×2")
    fx_em(c, t, C["s07.c"], [("×2 sete vezes  =  × ", TINTA), ("2", RAZ), ("^7", COR)], W / 2, 860, 100, "center")


# ---------------- fórmula ----------------
FORM = [("a_n", SAI), (" = ", TINTA), ("a_1", SAI), (" · ", TINTA), ("q", RAZ), ("^{n − 1}", ENT)]


def b_formula(c, t, C, b):
    def s08():
        E.frase(c, t, C["s08.a"], ps("o termo geral da PG", "i", 80), W / 2, 190, "center")
        y, s = 540, 160
        pos = fx_em(c, t, C["s08.b"], FORM, W / 2, y, s, "center")
        x1, w1 = pos[2]
        caixa_em(c, t, C["s08.c"], x1, w1, y, s, SAI)
        E.foco(c, t, C["s08.c"] + 0.2, 0.4, lambda a: centro(c, "1º termo", x1 + w1 / 2, y + 140, 56, "i", TINTA, a))
        xq, wq = pos[4]
        caixa_em(c, t, C["s08.d"], xq, wq, y, s, RAZ)
        E.foco(c, t, C["s08.d"] + 0.2, 0.4, lambda a: centro(c, "razão", xq + wq / 2, y + 140, 56, "i", RAZ, a))
        xe, we = pos[5]
        p = ep(t, C["s08.e"], 0.5)
        if p > 0:
            E.caixa_pontilhada(c, xe - 10, y - s * 1.05, we + 20, s * 0.62, p, ENT, p)
        E.foco(c, t, C["s08.e"] + 0.2, 0.4, lambda a: centro(c, "saltos, no expoente", xe + we / 2, y - s * 1.2, 52, "i", ENT, a))
    E.saida(c, t, C["s09"] - 0.1, s08)
    if t < C["s09"]:
        return
    fx_em(c, t, C["s09"], FORM, W / 2, 210, 100, "center")
    s = 100
    pos = fx_em(c, t, C["s09.a"], [("a_8", SAI), (" = 3 · ", TINTA), ("2", RAZ), ("^7", ENT)], 460, 440, s)
    xe = pos[1][0]
    fx_em(c, t, C["s09.b"], [("2", RAZ), ("^7", ENT), (" = 128", TINTA)], 1150, 440, 80)
    fx_em(c, t, C["s09.c"], [(" = 3 · 128 = ", TINTA)], xe, 600, s)
    resultado(c, t, C["s09.c"] + 0.6, "384", xe + E.formula(None, " = 3 · 128 = ", 0, 0, s, "g", a=0) + 100, 565, 95)
    E.foco(c, t, C["s09.d"], 0.5, lambda a: (E.bola(c, 470, 820, 40, a=a), centro(c, "1", 470, 840, 48, "g", BR, a),
                                             E.escreve(c, "a potência", 540, 840, 64, "g", TINTA, a)))
    E.foco(c, t, C["s09.d"] + 0.8, 0.5, lambda a: (E.bola(c, 470, 940, 40, a=a), centro(c, "2", 470, 960, 48, "g", BR, a),
                                                   E.escreve(c, "vezes o 1º termo", 540, 960, 64, "g", TINTA, a)))


# ---------------- juros: a PG é exponencial ----------------
JX = (330, 640, 950, 1260)
PL = E.Plano(1000, 200, 760, 680, 0, 10, 0, 3000)


def b_juros(c, t, C, b):
    def s10_11():
        cy = 380
        E.frase(c, t, C["s10.a"], [("R$", "g", 66), ("1.000", "g", 66), ("a", "i", 70), ("10%", "g", 66, COR), ("ao", "i", 70), ("mês", "i", 70)], XE, 140)
        vals = ("1.000", "1.100", "1.210", "1.331")
        fila(c, t, [(x, v, f"{i + 1}º", C["s10.b"] + 0.5 * i) for i, (x, v) in enumerate(zip(JX, vals))], cy, 260, 140, 70)
        fila(c, t, [(1480, "…", None, C["s10.b"] + 2.0)], cy)
        for i in range(3):
            pula(c, t, C["s10.d"] + 0.3 * i, JX[i], JX[i + 1], cy - 70, "×1,1", alto=70, size=48)
        for i, x in enumerate(JX):
            E.foco(c, t, C["s11.a"] + 0.2 * i, 0.4, lambda a, x=x, i=i: E.pilula(c, f"mês {i}", x, cy + 175, 40, "g", fundo=COR, a=a))

        def s10():
            fx_em(c, t, C["s10.c"], [("1.100 ÷ 1.000 = ", TINTA), ("1,1", RAZ)], XE, 650, 90)
            E.frase(c, t, C["s10.d"], [("é", "i", 76), ("uma", "i", 76), ("PG:", "g", 72, COR), ("a", "i", 76), ("razão", "g", 72, RAZ), ("é", "i", 76), ("o", "i", 76),
                                       ("fator", "g", 72, RAZ)], XE, 820)
        E.saida(c, t, C["s11"] - 0.1, s10)
        if t < C["s11"]:
            return
        E.frase(c, t, C["s11.a"], [("1º", "g", 66, ENT), ("termo", "i", 70), ("=", "g", 66), ("mês", "i", 70), ("0", "g", 66, COR)], XE, 650)
        fx_em(c, t, C["s11.b"], [("n − 1", ENT), (" = meses que passaram", TINTA)], 900, 650, 66)
        fx_em(c, t, C["s11.c"], [("M = 1.000 · ", TINTA), ("1,1", RAZ), ("^t", ENT)], XE, 840, 110)
        E.frase(c, t, C["s11.d"], [("função", "g", 70, COR), ("exponencial", "g", 70, COR)], 1060, 830)
    E.saida(c, t, C["s12"] - 0.1, s10_11)
    if t < C["s12"]:
        return
    E.plano(c, t, C["s12"], *PL.caixa, 0, 10, 0, 3000, passo=1, passo_y=500, marcas_x=[2, 4, 6, 8, 10], marcas_y=[1000, 2000, 3000],
            nomes=("", ""), size=36, fmt=mil)
    eixos_pa(c, t, C["s12"], PL, "M", "t")
    for i in range(11):
        E.ponto(c, t, C["s12.a"] + 0.2 * i, PL, i, 1000 * 1.1 ** i, cor=COR, r=13)
    E.curva(c, t, C["s12.b"], PL, lambda x: 1000 * 1.1 ** x, 0, 10, d=1.2, cor=COR, largura=5)
    E.curva(c, t, C["s12.c"], PL, lambda x: 1000 + 100 * x, 0, 10, d=1.0, cor=TINTA2, largura=5, tracejada=True)
    E.foco(c, t, C["s12.c"] + 0.8, 0.4, lambda a: E.escreve(c, "PA", PL.x(10) + 20, PL.y(2000) + 20, 52, "g", TINTA2, a))
    E.foco(c, t, C["s12.d"], 0.4, lambda a: E.escreve(c, "PG", PL.x(10) + 20, PL.y(2594) + 20, 52, "g", COR, a))
    fx_em(c, t, C["s12"] + 0.4, [("M = 1.000 · ", TINTA), ("1,1", RAZ), ("^t", ENT)], XE, 230, 72)
    E.frase(c, t, C["s12.a"], [("o", "i", 66), ("montante", "g", 62, COR), ("mês", "i", 66), ("a", "i", 66), ("mês", "i", 66)], XE, 400)
    E.frase(c, t, C["s12.b"], [("sobe", "i", 66), ("cada", "i", 66), ("vez", "i", 66), ("mais", "g", 62, COR)], XE, 520)
    E.frase(c, t, C["s12.c"], [("PA", "g", 70, TINTA2), ("→", "g", 66, TINTA2), ("reta", "i", 74, TINTA2)], XE, 720)
    E.frase(c, t, C["s12.d"], [("PG", "g", 70, COR), ("→", "g", 66, COR), ("curva", "i", 74, COR)], XE, 840)
    E.frase(c, t, C["s12.d"] + 0.6, [("exponencial", "g", 62, COR)], XE, 940)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s13.a"], [("usar", "i", 80), ("a", "i", 80), ("fórmula", "i", 80), ("da", "i", 80), ("PA", "g", 80, ERRADO)], W / 2, 190, "center")
    pos = fx_em(c, t, C["s13.b"], [("a_8 = 3 + 7 · 2", ERRADO)], 460, 400, 110)
    xe = pos[0][0] + pos[0][1]
    fx_em(c, t, C["s13.c"], [(" = 17", ERRADO)], xe, 400, 110)
    E.foco(c, t, C["s13.c"] + 0.5, 0.4, lambda a: E.selo(c, xe + 400, 363, 46, False, a))
    if t < C["s14"]:
        return
    XS = (300, 500, 700, 900, 1100)
    fila(c, t, [(x, v, f"{i + 1}º", C["s14"] + 0.12 * i, COR if i == 4 else None) for i, (x, v) in enumerate(zip(XS, (3, 6, 12, 24, 48)))], 610, 170, 120, 68, pos_size=40)
    E.foco(c, t, C["s14.a"], 0.5, lambda a: fx(c, [("a_5", SAI), (" = 48 > 17", TINTA)], 1260, 630, 76, a))
    E.frase(c, t, C["s14.b"], [("PA:", "g", 66, TINTA2), ("+", "g", 66, TINTA2), ("r", "g", 66, TINTA2), ("uma", "i", 70, TINTA2), ("vez", "i", 70, TINTA2),
                               ("por", "i", 70, TINTA2), ("salto", "i", 70, TINTA2)], XE + 60, 840)
    pos2 = E.frase(c, t, C["s14.c"], [("PG:", "g", 66, COR), ("×", "g", 66, RAZ), ("q,", "g", 66, RAZ), ("saltos", "i", 70), ("no", "i", 70), ("expoente", "g", 66, ENT)],
                   XE + 60, 960)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def s15():
        E.frase(c, t, C["s15.a"], [("pule", "g", 80, BR), ("do", "i", 80, CLARO), ("termo", "i", 80, CLARO), ("mais", "i", 80, CLARO), ("perto", "i", 80, CLARO)],
                W / 2, 140, "center")
        cy = 480
        E.foco(c, t, C["s15.b"], 0.5, lambda a: caixa(c, 520, cy, 200, 150, "24", a, "4º", 84, escuro=True))
        E.foco(c, t, C["s15.b"], 0.5, lambda a: fx(c, [("a_4", CLARO)], 300, cy + 30, 76, a, "right"))
        fila(c, t, [(960, "…", None, C["s15.c"] - 0.2)], cy, escuro=True)
        fim = t >= C["s15.d"] + 0.6
        E.foco(c, t, C["s15.c"] - 0.2, 0.5, lambda a: caixa(c, 1400, cy, 200, 150, "384" if fim else "?", a, "8º", 84,
                                                           BR if fim else CINZA, BR if fim else None, True))
        E.salto(c, t, C["s15.c"], 520, 1400, cy - 75 - 8, 150, CLARO, "4 saltos", d=0.9, size=56)
        E.foco(c, t, C["s15.c"] + 0.6, 0.4, lambda a: fx(c, [("2", BR), ("^4", CLARO), (" = 16", BR)], W / 2, 720, 76, a, "center"))
        fx_em(c, t, C["s15.d"], [("24 · 16 = ", BR), ("384", CLARO)], W / 2, 880, 100, "center")
    E.saida(c, t, C["s16"] - 0.1, s15)
    if t < C["s16"]:
        return
    E.frase(c, t, C["s16.a"], [("cada", "i", 76, CLARO), ("salto", "g", 72, BR), ("multiplica", "i", 76, CLARO), ("pela", "i", 76, CLARO), ("razão", "g", 72, BR)],
            W / 2, 170, "center")
    for i in range(10):
        x, y = 260 + (i % 5) * 340, 380 + (i // 5) * 190
        E.foco(c, t, C["s16.b"] + 0.15 * i, 0.4, lambda a, x=x, y=y, i=i: (fx(c, [("2", CLARO), (f"^{{{i + 1}}}", CLARO), (" = ", CLARO)], x - 70, y, 56, a, "right"),
                                                                             E.escreve(c, mil(2 ** (i + 1)), x - 50, y, 64, "g", BR, a)))
    E.foco(c, t, C["s16.c"], 0.5, lambda a: (E.pilula(c, "não compensa", 470, 820, 56, "g", fundo=ERRADO, a=a),
                                             fx(c, [("deu o ", CLARO), ("a_1", BR), (": o pulo é a própria fórmula", CLARO)], 720, 840, 64, a, est="i")))


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s17"], ps("hora de testar", "i", 72, COR), XE, 150)
    perg = (("s17.a", [("PG 2, 6, 18: a ", TINTA), ("razão", RAZ), (" e o ", TINTA), ("a_6", SAI), ("?", TINTA)]),
            ("s17.b", [("carro de R$ 40.000 perde ", TINTA), ("10%", COR), (" ao ano", TINTA)]),
            ("s17.c", [("os valores: PG de ", TINTA), ("razão", RAZ), ("?", TINTA)]),
            ("s17.d", [("valor depois de ", TINTA), ("2 anos", ENT), ("?", TINTA)]))
    for i, (k, partes) in enumerate(perg):
        y = 330 + i * 170
        if i != 1:
            n = i + 1 if i == 0 else i
            E.foco(c, t, C[k], 0.5, lambda a, n=n, y=y: (E.bola(c, XE + 40, y - 26, 44, a=a), centro(c, str(n), XE + 40, y - 4, 52, "g", BR, a)))
        fx_em(c, t, C[k] + 0.1, partes, XE + 120, y, 66)
    if t >= C["s18"]:
        E.relogio(c, t, C["s18.a"], 1600, 760, 120)


# ---------------- resposta ----------------
CX3 = (420, 860, 1300)


def b_resposta(c, t, C, b):
    def s19():
        fx_em(c, t, C["s19.a"], [("6 ÷ 2 = 3  →  ", TINTA), ("q = 3", RAZ)], XE, 260, 84)
        E.frase(c, t, C["s19.b"], [("6º", "g", 72, ENT), ("termo:", "i", 76), ("5", "g", 72, COR), ("saltos", "i", 76)], XE, 420)
        fx_em(c, t, C["s19.c"], [("3", RAZ), ("^5", ENT), (" = 243", TINTA)], XE, 580, 84)
        pos = fx_em(c, t, C["s19.d"], [("a_6", SAI), (" = 2 · 243 = ", TINTA)], XE, 760, 96)
        resultado(c, t, C["s19.d"] + 0.6, "486", pos[-1][0] + pos[-1][1] + 90, 725, 95)
    E.saida(c, t, C["s20"] - 0.1, s19)
    if t < C["s20"]:
        return
    cy = 330
    vals = ("R$ 40.000", "R$ 36.000", "R$ 32.400")
    rot = ("hoje", "1 ano", "2 anos")
    fila(c, t, [(CX3[0], vals[0], rot[0], C["s20"] + 0.2)], cy, 370, 140, 58)
    fila(c, t, [(CX3[1], vals[1], rot[1], C["s20.b"] + 0.4)], cy, 370, 140, 58)
    fila(c, t, [(CX3[2], vals[2], rot[2], C["s20.c"] + 0.4, COR)], cy, 370, 140, 58)
    pula(c, t, C["s20.b"], CX3[0], CX3[1], cy - 70, "×0,9", alto=70, size=50)
    pula(c, t, C["s20.c"], CX3[1], CX3[2], cy - 70, "×0,9", alto=70, size=50)
    fx_em(c, t, C["s20.a"], [("perder 10% = × ", TINTA), ("0,9", RAZ), ("  →  ", TINTA2), ("q = 0,9", RAZ)], XE, 620, 80)
    fx_em(c, t, C["s20.b"], "40.000 · 0,9 = 36.000", XE, 760, 80)
    fx_em(c, t, C["s20.c"], "36.000 · 0,9 = 32.400", XE, 900, 80)
    resultado(c, t, C["s20.c"] + 1.0, "R$ 32.400", 1560, 800, 160)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s21"], [("resumindo", "i", 92, COR)], W / 2, 200, "center")
        itens = (("s21.a", [("q", RAZ), (" = termo ÷ anterior", TINTA)]),
                 ("s21.b", [("saltos no expoente: ", TINTA), ("q", RAZ), ("^{n − 1}", ENT)]),
                 ("s21.c", [("PG = exponencial", TINTA)]))
        for i, (k, partes) in enumerate(itens):
            y = 390 + i * 190
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 330, y - 30, 56, a=a), centro(c, str(i + 1), 330, y - 7, 64, "g", BR, a)))
            fx_em(c, t, C[k] + 0.1, partes, 430, y, 80)
    E.saida(c, t, C["s22"] - 0.1, resumo)
    if t < C["s22"]:
        return
    E.frase(c, t, C["s22"], ps("próxima aula", "i", 80), XE, 260)
    E.frase(c, t, C["s22"] + 0.6, [("Atalhos", "g", 140, COR)], XE, 420)
    E.frase(c, t, C["s22"] + 0.9, [("da", "i", 130), ("PG", "g", 140, COR)], XE, 570)
    fx_em(c, t, C["s22.a"], [("4, ", TINTA), ("x", COR), (", 9", TINTA)], 1150, 300, 90)
    fx_em(c, t, C["s22.b"], [("f{x}{q}", TINTA), (",  x,  x · ", TINTA), ("q", RAZ)], 1150, 480, 84)
    E.foco(c, t, C["s22.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 560, 760, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s22.c"] + 0.3, 0.8))
    E.cursor(c, lerp(900, 700, p), lerp(1000, 785, p), ep(t, C["s22.c"] + 0.2, 0.4))
    E.frase(c, t, C["s22.d"], [("bons", "i", 120), ("estudos!", "i", 120, COR)], W / 2, 960, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, pg=b_pg, saltos=b_saltos, formula=b_formula, juros=b_juros, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
