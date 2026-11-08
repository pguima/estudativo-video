"""Visual — Estudativo · MAT-PRO-005: atalhos da PA, termo do meio e contar termos.

Linguagem visual da trilha Progressões (MAT-PRO-004): fila de caixas com o termo dentro (preto) e a posição embaixo (índigo);
a razão é o arco verde por cima das caixas; índice escrito como índice (a₁, aₙ) com fx(); palco escuro só no atalho.
Nesta aula: 2, x, 10 com os dois saltos iguais; as caixas x − r | x | x + r com o −r e o +r riscados na soma; a lista 105 … 994
de razão 7 e a frase "último menos primeiro, dividido pela razão, mais um" com a chave dos saltos.
Peças locais: fx(), fx_em(), caixa(), fila(), pula(), resultado(), caixa_em() (as da MAT-PRO-004)."""
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Matemática", "Progressões")
COR, CLARO = E.COR_TEXTO, E.CLARO
ENT, SAI, RAZ = COR, TINTA, CERTO  # posição n · termo aₙ · razão
ARQUIVO_FINAL = "estudativo_MAT-PRO-005_atalhos_da_pa_termo_do_meio_e_contar_termos.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("meio", "tres", "contar", "atalho", "questao", "fim"))
BR = "#FFFFFF"

assert (2 + 10) / 2 == 6 and 6 - 2 == 10 - 6 == 4
assert 18 / 3 == 6 and 6 + 2 == 2 * (6 - 2) and (4 + 6 + 8) == 18
assert divmod(100, 7) == (14, 2) and 7 * 14 == 98 and divmod(999, 7) == (142, 5) and 7 * 142 == 994
assert 994 - 105 == 889 and 889 / 7 == 127 and (21 - 7) / 7 == 2 and divmod(99, 7) == (14, 1) and 142 - 14 == 128
assert (8 + 20) / 2 == 14 and 45 / 3 == 15 and 15 + 5 == 2 * (15 - 5)
assert divmod(400, 6) == (66, 4) and divmod(99, 6) == (16, 3) and 66 - 16 == 50


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


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
    ws = [_w(s, size, est) for s, _ in partes]
    xx = x - sum(ws) / 2 if align == "center" else x - sum(ws) if align == "right" else x
    out = []
    for (s, cr), w in zip(partes, ws):
        out.append((xx, w))
        if a > 0:
            px = xx
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
        size = r * (0.62 if len(s) <= 3 else 0.5 if len(s) <= 5 else 0.4)
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


def eixos_pa(c, t, t0, P, nome_y="a_n"):
    """depois de E.plano: o eixo das posições em índigo e os nomes n (índigo) e aₙ (preto)"""
    x, y, w, h = P.caixa
    if t >= t0:
        M.arrow(c, x - 10, P.oy, x + w + 44, P.oy, ENT, 1.0, 6, 22, ep(t, t0, 0.6))
    E.foco(c, t, t0 + 0.5, 0.4, lambda a: (fx(c, [("n", ENT)], x + w + 30, P.oy + 70, 56, a),
                                          fx(c, [(nome_y, SAI)], P.ox + 24, y - 20, 56, a)))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def s01():
        E.frase(c, t, C["s01.a"], ps("quantos números de", "i", 84), XE, 260)
        E.frase(c, t, C["s01.a"] + 0.8, [("3", "g", 96, COR), ("algarismos", "i", 96), ("são", "i", 96)], XE, 390)
        E.frase(c, t, C["s01.a"] + 1.6, [("múltiplos", "g", 110), ("de", "i", 110), ("7?", "g", 120, COR)], XE, 540)
        lista = "105, 112, 119, 126, 133, 140, 147, …"
        p = ep(t, C["s01.a"] + 3.4, 1.2)
        if p > 0:
            c.save(); c.clipRect(skia.Rect.MakeXYWH(XE, 600, 1600 * p, 120))
            E.escreve(c, lista, XE, 680, 60, "b", CINZA, 1)
            c.restore()
        E.frase(c, t, C["s01.b"], [("uma", "i", 84), ("conta", "g", 80, COR), ("só", "i", 84)], XE, 860)
        resultado(c, t, C["s01.c"], "128", 1500, 470, 170)
        E.foco(c, t, C["s01.c"] + 1.4, 0.5, lambda a: E.pilula(c, "tem armadilha!", 1500, 760, 54, "g", fundo=ERRADO, a=a))
    E.saida(c, t, C["s02"] - 0.1, s01)
    if t < C["s02"]:
        return
    E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 80), XE, 220)
    itens = ((2.0, [("o ", TINTA), ("termo do meio", COR)]), (4.4, [("3 termos com ", TINTA), ("1 letra", COR)]), (7.0, [("contar os termos", COR)]))
    for i, (dt, partes) in enumerate(itens):
        y = 390 + i * 160
        E.foco(c, t, C["s02.a"] + dt, 0.5, lambda a, i=i, y=y: (E.bola(c, XE + 40, y - 30, 48, a=a), centro(c, str(i + 1), XE + 40, y - 6, 56, "g", BR, a)))
        fx_em(c, t, C["s02.a"] + dt + 0.1, partes, XE + 130, y, 90)
    E.foco(c, t, C["s02.a"] + 9.6, 0.5, lambda a: E.pilula(c, "+ atalho de prova", 1420, 880, 58, "g", a=a))


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], ps("você só precisa de", "i", 84), XE, 410)
    E.foco(c, t, C["s03"] + 0.6, 0.5, lambda a: E.escreve(c, "2", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03"] + 0.75, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 900, 880
    itens = (("s03.a", "termo geral da PA", [("a_n", SAI), (" = ", TINTA), ("a_1", SAI), (" + (", TINTA), ("n", ENT), (" − 1) · ", TINTA), ("r", RAZ)]),
             ("s03.b", "múltiplos de 7", [("7, 14, 21, 28, …", COR)]))
    for i, (k, l1, l2) in enumerate(itens):
        y = 280 + i * 280
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 220, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 62)], x + 44, y + 84)
        fx_em(c, t, C[k] + 0.3, l2, x + 44, y + 178, 76)
    q = ease_io(prog(t, C["s03.b"] - 0.35, 0.5))
    E.cursor(c, x + w - 30, lerp(280 + 190, 560 + 190, q), ep(t, C["s03.a"], 0.4))


# ---------------- termo do meio ----------------
MX = (560, 960, 1360)


def b_meio(c, t, C, b):
    cy = 330
    seis = t >= C["s05.d"]
    vals = (2, "6" if seis else "x", 10)
    for i, (x, v) in enumerate(zip(MX, vals)):
        cor = (COR if i == 1 else None)
        E.foco(c, t, C["s04.a"] + 0.48 * i, 0.5, lambda a, x=x, v=v, i=i, cor=cor: caixa(c, x, cy, 220, 160, v, a, f"{i + 1}º", 90, cor, COR if i == 1 else None))
    rot = ("+4", "+4") if seis else ("x − 2", "10 − x")
    for i in range(2):
        pula(c, t, C["s04.b"] + 0.9 * i, MX[i], MX[i + 1], cy - 80, rot[i], alto=90, size=56)
    E.foco(c, t, C["s04.b"] + 1.6, 0.4, lambda a: centro(c, "mesmo salto", W / 2, cy + 200, 48, "i", RAZ, a * (1 - ep(t, C["s05.d"], 0.3))))
    if C["s06.c"] <= t:
        p = prog(t, C["s06.c"], 1.0)
        for x in ((MX[0] + MX[1]) / 2, (MX[1] + MX[2]) / 2):
            if p < 1:
                c.drawCircle(x, cy - 190, 50 + 50 * ease_out(p), M.paint(RAZ, 1 - p, stroke=6))

    def s05():
        fx_em(c, t, C["s05.a"], [("x", COR), (" − 2 = 10 − ", TINTA), ("x", COR)], XE, 640, 96)
        fx_em(c, t, C["s05.b"], [("2", TINTA), ("x", COR), (" = 12", TINTA)], XE, 790, 96)
        E.foco(c, t, C["s05.b"] + 0.2, 0.4, lambda a: E.escreve(c, "x de um lado, números do outro", 560, 790, 46, "i", TINTA2, a))
        fx_em(c, t, C["s05.c"], [("x", COR), (" = 6", TINTA)], XE, 940, 96)
        resultado(c, t, C["s05.c"] + 0.3, "6", 1560, 790, 120)
    E.saida(c, t, C["s06"] - 0.1, s05)
    if t < C["s06"]:
        return
    fx_em(c, t, C["s06.a"], "f{2 + 10}{2} = f{12}{2} = 6", W / 2, 680, 100, "center")
    E.frase(c, t, C["s06.b"], [("meio", "g", 76, COR), ("=", "g", 76), ("média", "g", 76, COR), ("dos", "i", 80), ("vizinhos", "i", 80)], W / 2, 870, "center")
    E.frase(c, t, C["s06.c"], [("a", "i", 64), ("mesma", "g", 60, RAZ), ("distância", "i", 64), ("de", "i", 64), ("cada", "i", 64), ("lado", "i", 64)], W / 2, 985, "center")


# ---------------- três termos ----------------
TX = (520, 960, 1400)


def b_tres(c, t, C, b):
    cy = 280
    if t < C["s08.a"]:
        vals = ("?", "?", "?")
    elif t < C["s08.b"]:
        vals = ("?", "x", "?")
    elif t < C["s09.a"]:
        vals = ("x − r", "x", "x + r")
    elif t < C["s09.e"]:
        vals = ("6 − r", "6", "6 + r")
    else:
        vals = ("4", "6", "8")
    for i, (x, v) in enumerate(zip(TX, vals)):
        cor = CINZA if v == "?" else (COR if "x" in v or (i == 1 and v == "6") else None)
        E.foco(c, t, C["s07.a"] + 0.2 * i, 0.5, lambda a, x=x, v=v, i=i, cor=cor: caixa(c, x, cy, 340, 160, v, a, f"{i + 1}º", 84, cor))

    def s07():
        E.frase(c, t, C["s07.a"], [("3", "g", 84, COR), ("números", "i", 88), ("em", "i", 88), ("PA", "g", 84), ("·", "g", 84, TINTA2), ("soma", "i", 88), ("18", "g", 84, COR)], W / 2, 640, "center")
        E.frase(c, t, C["s07.b"], [("maior", "g", 84), ("=", "g", 84), ("2", "g", 84, COR), ("×", "g", 84), ("menor", "g", 84)], W / 2, 800, "center")
        E.frase(c, t, C["s07.b"] + 2.0, [("quais", "i", 80), ("são?", "g", 76, COR)], W / 2, 940, "center")
    E.saida(c, t, C["s08"] - 0.1, s07)

    def s08():
        E.frase(c, t, C["s08.a"], [("o", "i", 72), ("do", "i", 72), ("meio", "i", 72), ("é", "i", 72), ("x", "g", 76, COR)], W / 2, 120, "center")
        y = 620
        pos = fx_em(c, t, C["s08.c"], [("(x ", TINTA), ("− r", TINTA), (") + x + (x ", TINTA), ("+ r", TINTA), (") = 18", TINTA)], W / 2, y, 96, "center")
        for k, j in ((0, 1), (1, 3)):
            x0, w0 = pos[j]
            if t >= C["s08.c"] + 1.0 + 0.3 * k:
                E.risco(c, x0 - 6, y + 10, x0 + w0 + 6, y - 70, t, C["s08.c"] + 1.0 + 0.3 * k, cor=ERRADO, largura=10)
        E.foco(c, t, C["s08.c"] + 1.6, 0.4, lambda a: centro(c, "se cancelam", W / 2, y + 90, 50, "i", ERRADO, a))
        fx_em(c, t, C["s08.d"], [("3", TINTA), ("x", COR), (" = 18", TINTA)], 640, 860, 100, "center")
        fx_em(c, t, C["s08.e"], [("x", COR), (" = 6", TINTA)], 1200, 860, 100, "center")
        E.foco(c, t, C["s08.e"] + 0.4, 0.4, lambda a: E.escreve(c, "de cara!", 1400, 860, 60, "i", CERTO, a))
    if t >= C["s08"]:
        E.saida(c, t, C["s09"] - 0.1, s08)
    if t < C["s09"]:
        return
    E.frase(c, t, C["s09"] + 0.6, [("maior", "g", 62), ("=", "g", 62), ("2", "g", 62, COR), ("×", "g", 62), ("menor", "g", 62)], W / 2, 120, "center")
    xs, s = 620, 90
    fx_em(c, t, C["s09.a"], [("6 + ", TINTA), ("r", RAZ), (" = 2(6 − ", TINTA), ("r", RAZ), (")", TINTA)], xs, 550, s)
    fx_em(c, t, C["s09.b"], [("6 + ", TINTA), ("r", RAZ), (" = 12 − 2", TINTA), ("r", RAZ)], xs, 670, s)
    fx_em(c, t, C["s09.c"], [("3", TINTA), ("r", RAZ), (" = 6", TINTA)], xs, 790, s)
    fx_em(c, t, C["s09.d"], [("r", RAZ), (" = 2", TINTA)], xs, 910, s)
    E.foco(c, t, C["s09.e"] + 2.2, 0.5, lambda a: (fx(c, "8 = 2 · 4", 1450, 790, 90, a, "center"), E.selo(c, 1450, 900, 44, True, a)))


# ---------------- contar termos ----------------
def b_contar(c, t, C, b):
    def s10_11():
        E.frase(c, t, C["s10.a"], [("o", "i", 72), ("primeiro", "g", 72, COR)], XE, 200)
        fx_em(c, t, C["s10.b"], "100 ÷ 7 = 14, resto 2", XE, 340, 72)
        fx_em(c, t, C["s10.b"] + 3.2, "7 · 14 = 98", XE, 460, 72)
        E.foco(c, t, C["s10.b"] + 4.0, 0.4, lambda a: E.escreve(c, "só 2 algarismos", XE + 470, 460, 50, "i", ERRADO, a))
        E.foco(c, t, C["s10.c"], 0.5, lambda a: caixa(c, XE + 150, 600, 260, 140, "105", a, "1º", 84, COR, COR))
        x2 = 1010
        E.frase(c, t, C["s11.a"], [("o", "i", 72), ("último", "g", 72, COR)], x2, 200)
        fx_em(c, t, C["s11.b"], "999 ÷ 7 = 142, resto 5", x2, 340, 72)
        fx_em(c, t, C["s11.c"], "7 · 142 = 994", x2, 460, 72)
        E.foco(c, t, C["s11.c"] + 0.6, 0.5, lambda a: caixa(c, x2 + 150, 600, 260, 140, "994", a, "último", 84, COR, COR))
        cy = 880
        XS = (420, 700, 980)
        fila(c, t, [(x, v, None, C["s11.d"] + 0.2 * i) for i, (x, v) in enumerate(zip(XS, (105, 112, 119)))] + [(1230, "…", None, C["s11.d"] + 0.6),
                                                                                                                (1500, 994, None, C["s11.d"] + 0.8, COR)], cy, 220, 120, 70)
        for i in range(2):
            pula(c, t, C["s11.d"] + 0.4 + 0.3 * i, XS[i], XS[i + 1], cy - 60, "+7", alto=60, size=46)
    E.saida(c, t, C["s12"] - 0.1, s10_11)
    if t < C["s12"]:
        return
    E.frase(c, t, C["s12"], [("n", "g", 76, ENT), ("desconhecido", "i", 80)], W / 2, 170, "center")
    xs, s = 380, 96
    fx_em(c, t, C["s12.a"], [("994", COR), (" = 105 + (", TINTA), ("n", ENT), (" − 1) · ", TINTA), ("7", RAZ)], xs, 380, s)

    def s12():
        fx_em(c, t, C["s12.b"], [("889", TINTA), (" = (", TINTA), ("n", ENT), (" − 1) · ", TINTA), ("7", RAZ)], xs, 530, s)
        E.foco(c, t, C["s12.b"] + 0.3, 0.4, lambda a: E.escreve(c, "994 − 105", xs + 900, 530, 50, "i", TINTA2, a))
        fx_em(c, t, C["s12.c"], [("n", ENT), (" − 1 = 127", TINTA)], xs, 680, s)
        E.foco(c, t, C["s12.c"] + 0.3, 0.4, lambda a: E.escreve(c, "889 ÷ 7", xs + 900, 680, 50, "i", TINTA2, a))
        fx_em(c, t, C["s12.d"], [("n", ENT), (" = 128", TINTA)], xs, 830, s)
        resultado(c, t, C["s12.d"] + 0.3, "128", 1560, 720, 130)
    E.saida(c, t, C["s13"] - 0.1, s12)
    if t < C["s13"]:
        return
    y = 720
    pos = fx_em(c, t, C["s13.a"], [("f{último − primeiro}{razão}", TINTA), (" + 1", COR)], W / 2, y, 96, "center")
    (x0, w0), (x1, w1) = pos
    if t >= C["s13.b"]:
        E.chave(c, x0, x0 + w0, y + 110, TINTA, ep(t, C["s13.b"], 0.5), 24, 5)
    E.foco(c, t, C["s13.b"] + 0.2, 0.4, lambda a: centro(c, "saltos", x0 + w0 / 2, y + 200, 56, "i", TINTA, a))
    caixa_em(c, t, C["s13.c"], x1 + 24, w1 - 24, y, 96, COR)
    E.foco(c, t, C["s13.c"] + 0.2, 0.4, lambda a: centro(c, "o 1º termo", x1 + w1 / 2 + 12, y - 150, 56, "i", COR, a))


# ---------------- erro ----------------
EX = (560, 960, 1360)


def b_erro(c, t, C, b):
    E.frase(c, t, C["s14.a"], [("esquecer", "i", 80), ("o", "i", 80), ("+1", "g", 84, ERRADO)], XE, 180)
    E.foco(c, t, C["s14.b"], 0.5, lambda a: (fx(c, [("f{889}{7} = 127", ERRADO)], 1180, 200, 84, a), E.selo(c, 1720, 170, 40, False, a)))
    cy = 520
    fila(c, t, [(x, v, None, C["s14.c"] + 0.48 * i) for i, (x, v) in enumerate(zip(EX, (7, 14, 21)))], cy, 220, 150, 90)
    for i in range(2):
        pula(c, t, C["s14.d"] + 0.4 * i, EX[i], EX[i + 1], cy - 75, f"salto {i + 1}", alto=80, size=46)
    E.foco(c, t, C["s14.d"] - 0.6, 0.5, lambda a: fx(c, "f{21 − 7}{7} = 2", W / 2, 820, 84, a, "center"))
    for i, x in enumerate(EX):
        k = ease_back(prog(t, C["s14.e"] + 0.25 * i, 0.4))
        if k > 0:
            E.bola(c, x, cy + 130, 34 * k, CERTO)
            E.foco(c, t, C["s14.e"] + 0.25 * i, 0.3, lambda a, i=i, x=x: centro(c, str(i + 1), x, cy + 146, 44, "g", BR, a), sobe=0)
    E.frase(c, t, C["s14.e"] + 1.6, [("2", "g", 76, RAZ), ("saltos,", "i", 80), ("3", "g", 76, CERTO), ("termos", "i", 80)], W / 2, 980, "center")


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def s15():
        E.frase(c, t, C["s15.a"], [("conte", "g", 72, BR), ("até", "i", 76, CLARO), ("o", "i", 76, CLARO), ("fim", "g", 72, BR)], W / 2, 180, "center")
        E.frase(c, t, C["s15.a"] + 1.6, [("tire", "g", 72, BR), ("os", "i", 76, CLARO), ("de", "i", 76, CLARO), ("antes", "i", 76, CLARO), ("do", "i", 76, CLARO),
                                         ("começo", "g", 72, BR)], W / 2, 290, "center")
        fx_em(c, t, C["s15.b"], [("até 999:  ", CLARO), ("999 ÷ 7 → 142", BR)], 360, 480, 80)
        fx_em(c, t, C["s15.c"], [("até 99:  ", CLARO), ("99 ÷ 7 = 14, resto 1", BR)], 360, 620, 80)
        fx_em(c, t, C["s15.d"], [("142 − 14 = ", BR)], 360, 820, 100)
        resultado(c, t, C["s15.d"] + 0.4, "128", 1060, 785, 100)
    E.saida(c, t, C["s16"] - 0.1, s15)
    if t < C["s16"]:
        return
    E.frase(c, t, C["s16.a"], [("a", "i", 72, CLARO), ("divisão", "g", 70, BR), ("conta", "i", 72, CLARO), ("desde", "i", 72, CLARO), ("o", "i", 72, CLARO), ("primeiro", "g", 70, BR)], W / 2, 200, "center")
    fx_em(c, t, C["s16.a"] + 1.4, [("7 · 1,  7 · 2,  …,  7 · 142", CLARO)], W / 2, 330, 76, "center")
    E.foco(c, t, C["s16.b"], 0.5, lambda a: (E.pilula(c, "não compensa", 470, 560, 56, "g", fundo=ERRADO, a=a),
                                             fx(c, [("4, 9, 14", BR), (": não são múltiplos", CLARO)], 720, 580, 70, a, est="g")))
    fx_em(c, t, C["s16.c"], [("f{último − primeiro}{razão}", BR), (" + 1", CLARO)], W / 2, 840, 84, "center")


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s17"], ps("hora de testar", "i", 72, COR), XE, 150)
    perg = (("s17.a", [("8, ", TINTA), ("x", COR), (", 20 em PA:  ", TINTA), ("x", COR), (" = ?", TINTA)], None),
            ("s17.b", [("idades em PA, soma 45", TINTA)], [("mais velho = 2 × mais novo", TINTA2)]),
            ("s17.c", [("múltiplos de 6", TINTA)], [("entre 100 e 400?", TINTA2)]))
    for i, (k, l1, l2) in enumerate(perg):
        y = 330 + i * 230
        E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, XE + 40, y - 26, 44, a=a), centro(c, str(i + 1), XE + 40, y - 4, 52, "g", BR, a)))
        fx_em(c, t, C[k] + 0.1, l1, XE + 120, y, 72)
        if l2:
            fx_em(c, t, C[k] + 1.6, l2, XE + 120, y + 90, 60)
    if t >= C["s18"]:
        E.relogio(c, t, C["s18.a"], 1560, 520, 170)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    def s19():
        E.foco(c, t, C["s19.a"], 0.5, lambda a: (E.bola(c, XE + 40, 194, 40, a=a), centro(c, "1", XE + 40, 214, 48, "g", BR, a)))
        fx_em(c, t, C["s19.a"], "8 + 20 = 28", XE + 120, 220, 76)
        fx_em(c, t, C["s19.b"], [("28 ÷ 2 = ", TINTA), ("14", COR)], 760, 220, 76)
        E.foco(c, t, C["s19.c"] - 1.2, 0.5, lambda a: (E.bola(c, XE + 40, 394, 40, a=a), centro(c, "2", XE + 40, 414, 48, "g", BR, a)))
        fx_em(c, t, C["s19.c"], [("3", TINTA), ("x", COR), (" = 45  →  ", TINTA), ("x", COR), (" = 15", TINTA)], XE + 120, 420, 76)
        fx_em(c, t, C["s19.d"], [("15 + ", TINTA), ("r", RAZ), (" = 2(15 − ", TINTA), ("r", RAZ), (")", TINTA)], XE + 120, 560, 76)
        fx_em(c, t, C["s19.e"], [("3", TINTA), ("r", RAZ), (" = 15  →  ", TINTA), ("r", RAZ), (" = 5", TINTA)], XE + 120, 700, 76)
        XS = (1180, 1430, 1680)
        fila(c, t, [(x, v, None, C["s19.f"] + 0.48 * i, COR) for i, (x, v) in enumerate(zip(XS, (10, 15, 20)))], 600, 200, 140, 84)
        E.foco(c, t, C["s19.f"] + 1.4, 0.4, lambda a: centro(c, "anos", 1430, 760, 60, "i", TINTA, a))
    E.saida(c, t, C["s20"] - 0.1, s19)
    if t < C["s20"]:
        return
    E.foco(c, t, C["s20"], 0.5, lambda a: (E.bola(c, XE + 40, 194, 40, a=a), centro(c, "3", XE + 40, 214, 48, "g", BR, a)))
    E.frase(c, t, C["s20"], [("múltiplos", "i", 76), ("de", "i", 76), ("6", "g", 72, COR)], XE + 120, 220)
    fx_em(c, t, C["s20.a"], [("até 400:  ", TINTA2), ("400 ÷ 6 = 66, resto 4", TINTA)], XE, 420, 76)
    fx_em(c, t, C["s20.b"], [("até 99:  ", TINTA2), ("99 ÷ 6 = 16, resto 3", TINTA)], XE, 580, 76)
    fx_em(c, t, C["s20.c"], "66 − 16 = ", XE, 800, 96)
    resultado(c, t, C["s20.c"] + 0.4, "50", XE + 640, 765, 100)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s21"], [("resumindo", "i", 92, COR)], W / 2, 200, "center")
        itens = (("s21.a", [("meio = média dos vizinhos", TINTA)]),
                 ("s21.b", [("x − r,  x,  x + r", TINTA)]),
                 ("s21.c", [("termos = saltos + 1", TINTA)]))
        for i, (k, partes) in enumerate(itens):
            y = 390 + i * 190
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 330, y - 30, 56, a=a), centro(c, str(i + 1), 330, y - 7, 64, "g", BR, a)))
            fx_em(c, t, C[k] + 0.1, partes, 430, y, 84)
    E.saida(c, t, C["s22"] - 0.1, resumo)
    if t < C["s22"]:
        return
    E.frase(c, t, C["s22"], ps("próxima aula", "i", 80), XE, 260)
    E.frase(c, t, C["s22"] + 0.6, [("Soma", "g", 140, COR)], XE, 420)
    E.frase(c, t, C["s22"] + 0.9, [("da", "i", 130), ("PA", "g", 140, COR)], XE, 570)
    fx_em(c, t, C["s22.a"], [("1 + 2 + … + 100", TINTA)], 1100, 300, 84)
    E.frase(c, t, C["s22.a"] + 1.8, [("a", "i", 64), ("ideia", "i", 64), ("de", "i", 64), ("Gauss", "g", 62, COR)], 1100, 400)
    E.frase(c, t, C["s22.b"], [("o", "i", 64), ("total", "i", 64), ("de", "i", 64), ("30", "g", 62, COR), ("dias", "i", 64)], 1100, 540)
    E.foco(c, t, C["s22.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 560, 760, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s22.c"] + 0.3, 0.8))
    E.cursor(c, lerp(900, 700, p), lerp(1000, 785, p), ep(t, C["s22.c"] + 0.2, 0.4))
    E.frase(c, t, C["s22.d"], [("bons", "i", 120), ("estudos!", "i", 120, COR)], W / 2, 960, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, meio=b_meio, tres=b_tres, contar=b_contar, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
