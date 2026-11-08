"""Visual — Estudativo · MAT-PRO-009: atalhos da PG, termo do meio e três termos.

Linguagem visual da trilha Progressões (MAT-PRO-001, 004 e 008): fila de caixas de borda índigo com o termo dentro (preto) e a posição
embaixo (índigo); a razão é o arco verde "×q" por cima das caixas; índice como índice com fx(); palco escuro só no atalho.
Nesta aula: 4, x, 9 com os dois arcos "×q" iguais; x/4 = 9/x virando x · x = 4 · 9 (fração e raiz pela escrita de E.formula);
as caixas x/q | x | x · q com o "/q" e o "· q" riscados no produto; a fatoração de 12 e 75 com as duplas de primos marcadas
(duplas()); a caixa 5 × 10 × 20 em perspectiva (E.paralelepipedo) na resposta.
Peças locais: fx(), fx_em(), caixa(), fila(), pula(), resultado(), caixa_em() (as da MAT-PRO-004), duplas()."""
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Matemática", "Progressões")
COR, CLARO = E.COR_TEXTO, E.CLARO
ENT, SAI, RAZ = COR, TINTA, CERTO  # posição n · termo aₙ · razão
ARQUIVO_FINAL = "estudativo_MAT-PRO-009_atalhos_da_pg_termo_do_meio_e_tres_termos.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("meio", "tres", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"

assert 4 * 9 == 36 == 6 * 6 and 6 / 4 == 9 / 6 == 1.5 and (-6) * (-6) == 36 and -6 / 4 == 9 / -6 == -1.5
assert 6 ** 3 == 216 and 18 / 6 == 3 and 2 * 6 * 18 == 216
assert (4 + 9) / 2 == 6.5 and 6.5 / 4 == 1.625 and round(9 / 6.5, 2) == 1.38
assert 12 * 75 == 900 == 30 ** 2 == (2 * 3 * 5) ** 2
assert 2 * 50 == 100 == 10 ** 2 and 10 * 5 == 50 and 10 ** 3 == 1000 and 5 * 10 * 20 == 1000


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
GX = (560, 960, 1360)


def b_gancho(c, t, C, b):
    def s01():
        cy = 380
        seis = t >= C["s01.c"]
        for i, (x, v) in enumerate(zip(GX, (4, "6" if seis else "x", 9))):
            E.foco(c, t, C["s01.a"] + 0.48 * i, 0.5, lambda a, x=x, v=v, i=i: caixa(c, x, cy, 220, 160, v, a, f"{i + 1}º", 90, COR if i == 1 else None))
        E.frase(c, t, C["s01.a"] + 2.0, [("termos", "i", 60, TINTA2), ("positivos", "i", 60, TINTA2)], W / 2, 170, "center")
        E.foco(c, t, C["s01.b"], 0.5, lambda a: (fx(c, [("média: ", ERRADO), ("f{4 + 9}{2} = 6,5", ERRADO)], 380, 720, 84, a),
                                                 E.selo(c, 1120, 690, 40, False, a)))
        E.foco(c, t, C["s01.d"], 0.5, lambda a: fx(c, [("r{4 · 9} = r{36} = ", TINTA), ("6", CERTO)], W / 2, 920, 96, a, "center"))
    E.saida(c, t, C["s02"] - 0.1, s01)
    if t < C["s02"]:
        return
    E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 80), XE, 260)
    itens = ((2.4, [("o ", TINTA), ("termo do meio", COR), (" da PG", TINTA)]), (5.0, [("3 termos com ", TINTA), ("1 letra", COR)]))
    for i, (dt, partes) in enumerate(itens):
        y = 430 + i * 170
        E.foco(c, t, C["s02.a"] + dt, 0.5, lambda a, i=i, y=y: (E.bola(c, XE + 40, y - 30, 48, a=a), centro(c, str(i + 1), XE + 40, y - 6, 56, "g", BR, a)))
        fx_em(c, t, C["s02.a"] + dt + 0.1, partes, XE + 130, y, 90)
    E.foco(c, t, C["s02.a"] + 7.6, 0.5, lambda a: E.pilula(c, "+ atalho de prova", XE + 300, 800, 58, "g", a=a))


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], ps("você só precisa de", "i", 84), XE, 410)
    E.foco(c, t, C["s03"] + 0.6, 0.5, lambda a: E.escreve(c, "2", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03"] + 0.75, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 900, 880
    itens = (("s03.a", "a razão da PG", [("q", RAZ), (" = termo ÷ anterior", TINTA)]),
             ("s03.b", "raiz quadrada", [("r{36} = 6", COR), ("   pois 6 · 6 = 36", TINTA2)]))
    for i, (k, l1, l2) in enumerate(itens):
        y = 280 + i * 280
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 220, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 62)], x + 44, y + 84)
        fx_em(c, t, C[k] + 0.3, l2, x + 44, y + 180, 72)
    q = ease_io(prog(t, C["s03.b"] - 0.35, 0.5))
    E.cursor(c, x + w - 30, lerp(280 + 190, 560 + 190, q), ep(t, C["s03.a"], 0.4))


# ---------------- termo do meio ----------------
def b_meio(c, t, C, b):
    def topo():
        cy = 300
        seis = t >= C["s05.b"]
        for i, (x, v) in enumerate(zip(GX, (4, "6" if seis else "x", 9))):
            E.foco(c, t, C["s04"] + 0.15 * i, 0.5, lambda a, x=x, v=v, i=i: caixa(c, x, cy, 220, 160, v, a, f"{i + 1}º", 90, COR if i == 1 else None))
        rot = "×1,5" if t >= C["s05.d"] else "×q"
        for i in range(2):
            pula(c, t, C["s04.a"] + 0.5 * i, GX[i], GX[i + 1], cy - 80, rot, alto=90, size=56)
        E.foco(c, t, C["s04.a"] + 1.0, 0.4, lambda a: centro(c, "a mesma razão", W / 2, cy + 200, 48, "i", RAZ, a * (1 - ep(t, C["s05"], 0.3))))

        def s04():
            fx_em(c, t, C["s04.b"], [("f{x}{4} = f{9}{x}", TINTA)], XE + 40, 680, 110)
            fx_em(c, t, C["s04.c"], [("x · x = 4 · 9", TINTA)], 760, 680, 96)
            E.foco(c, t, C["s04.c"], 0.4, lambda a: E.escreve(c, "em cruz", 760, 760, 48, "i", TINTA2, a))
            fx_em(c, t, C["s04.d"], [("x", COR), ("^2", COR), (" = 36", TINTA)], 1400, 680, 110)
        E.saida(c, t, C["s05"] - 0.1, s04)

        def s05():
            fx_em(c, t, C["s05"] + 0.4, [("x", COR), ("^2", COR), (" = 36", TINTA)], XE + 40, 640, 90)
            fx_em(c, t, C["s05.a"], [("x = r{36} = ", TINTA), ("6", COR)], XE + 40, 800, 90)
            fx_em(c, t, C["s05.c"], [("6 ÷ 4 = ", TINTA), ("1,5", RAZ)], 1000, 640, 90)
            fx_em(c, t, C["s05.d"], [("9 ÷ 6 = ", TINTA), ("1,5", RAZ)], 1000, 800, 90)
        if t >= C["s05"]:
            E.saida(c, t, C["s06"] - 0.1, s05)
    E.saida(c, t, C["s07"] - 0.1, topo)
    if C["s06"] <= t < C["s07"] + 0.5:
        def s06():
            fx_em(c, t, C["s06.a"], [("(−6) · (−6) = 36", TINTA)], XE + 40, 560, 80)
            cy2 = 830
            XS = (380, 640, 900)
            fila(c, t, [(x, v, None, C["s06.b"] + 0.4 * i, ERRADO if i == 1 else None) for i, (x, v) in enumerate(zip(XS, ("4", "−6", "9")))], cy2, 190, 130, 80)
            for i in range(2):
                pula(c, t, C["s06.b"] + 1.2 + 0.3 * i, XS[i], XS[i + 1], cy2 - 65, "×(−1,5)", alto=50, size=40)
            E.foco(c, t, C["s06.c"], 0.5, lambda a: (E.pilula(c, "termos positivos", 1360, 620, 50, "g", fundo=COR, a=a),
                                                     fx(c, [("fica o ", TINTA), ("6", COR)], 1220, 730, 80, a)))
            E.foco(c, t, C["s06.d"], 0.5, lambda a: fx(c, [("sem aviso: ", TINTA2), ("6", COR), (" ou ", TINTA2), ("−6", ERRADO)], 1160, 900, 76, a))
        E.saida(c, t, C["s07"] - 0.1, s06)
    if t < C["s07"]:
        return
    E.frase(c, t, C["s07.a"], [("(meio)²", "g", 80, COR), ("=", "g", 80), ("produto", "g", 80), ("dos", "i", 84), ("vizinhos", "i", 84)], W / 2, 220, "center")
    cy = 480
    XS = (500, 960, 1420)
    fila(c, t, [(x, v, f"{i + 1}º", C["s07.b"] + 0.4 * i) for i, (x, v) in enumerate(zip(XS, ("a", "a · q", "a · q · q")))], cy, 380, 150, 80)
    E.foco(c, t, C["s07.c"], 0.5, lambda a: fx(c, [("a", TINTA), (" · ", TINTA2), ("a · q · q", TINTA), ("  =  ", TINTA2), ("a · a · q · q", TINTA)], W / 2, 780, 80, a, "center"))
    E.foco(c, t, C["s07.d"], 0.5, lambda a: fx(c, [("= ", TINTA2), ("(a · q)", COR), (" · ", TINTA), ("(a · q)", COR)], W / 2, 930, 90, a, "center"))


# ---------------- três termos ----------------
TX = (520, 960, 1400)


def b_tres(c, t, C, b):
    cy = 280
    if t < C["s09.a"]:
        vals = ("?", "?", "?")
    elif t < C["s09.b"]:
        vals = ("?", "x", "?")
    elif t < C["s09.c"]:
        vals = ("f{x}{q}", "x", "?")
    elif t < C["s10.e"]:
        vals = ("f{x}{q}", "x", "x · q")
    else:
        vals = ("2", "6", "18")
    for i, (x, v) in enumerate(zip(TX, vals)):
        cor = CINZA if v == "?" else (COR if "x" in v else None)
        E.foco(c, t, C["s08.a"] + 0.2 * i, 0.5, lambda a, x=x, v=v, i=i, cor=cor: caixa(c, x, cy, 340, 180, v, a, f"{i + 1}º", 76, cor))

    def s08():
        E.frase(c, t, C["s08.a"], [("3", "g", 84, COR), ("números", "i", 88), ("em", "i", 88), ("PG", "g", 84), ("·", "g", 84, TINTA2), ("produto", "i", 88),
                                   ("216", "g", 84, COR)], W / 2, 640, "center")
        E.frase(c, t, C["s08.b"], [("o", "i", 88), ("maior", "g", 84), ("é", "i", 88), ("18", "g", 84, COR)], W / 2, 800, "center")
        E.frase(c, t, C["s08.b"] + 1.6, [("quais", "i", 80), ("são?", "g", 76, COR)], W / 2, 940, "center")
    E.saida(c, t, C["s09"] - 0.1, s08)

    def s09():
        y = 660
        pos = fx_em(c, t, C["s09.d"], [("f{x}{q}", TINTA), (" · x · x", TINTA), (" · q", TINTA), (" = 216", TINTA)], W / 2, y, 100, "center")
        (x0, w0), (x2, w2) = pos[0], pos[2]
        if t >= C["s09.d"] + 1.0:
            E.risco(c, x0 - 4, y + 90, x0 + w0 + 4, y + 20, t, C["s09.d"] + 1.0, cor=ERRADO, largura=10)
            E.risco(c, x2 + 10, y + 10, x2 + w2 + 6, y - 70, t, C["s09.d"] + 1.3, cor=ERRADO, largura=10)
        E.foco(c, t, C["s09.d"] + 1.6, 0.4, lambda a: centro(c, "se cancelam", W / 2, y + 150, 50, "i", ERRADO, a))
        fx_em(c, t, C["s09.e"], [("x", COR), ("^3", COR), (" = 216", TINTA)], W / 2, 960, 110, "center")
    if t >= C["s09"]:
        E.saida(c, t, C["s10"] - 0.1, s09)
    if t < C["s10"]:
        return

    def s10():
        fx_em(c, t, C["s10.a"], "6 · 6 · 6 = 216", XE + 40, 560, 84)
        fx_em(c, t, C["s10.b"], [("x", COR), (" = 6", TINTA)], XE + 40, 700, 96)
        fx_em(c, t, C["s10.c"], [("6 · ", TINTA), ("q", RAZ), (" = 18", TINTA)], 900, 560, 84)
        fx_em(c, t, C["s10.d"], [("q", RAZ), (" = 3", TINTA)], 900, 700, 96)
        E.foco(c, t, C["s10.e"] + 1.0, 0.5, lambda a: (fx(c, "2 · 6 · 18 = 216", W / 2, 900, 80, a, "center"), E.selo(c, 1440, 870, 40, True, a)))
    E.saida(c, t, C["s11"] - 0.1, s10)
    if t < C["s11"]:
        return
    E.frase(c, t, C["s11.a"], [("deu", "i", 76), ("o", "i", 76), ("produto", "g", 72, COR), ("dos", "i", 76), ("três?", "i", 76)], W / 2, 620, "center")
    fx_em(c, t, C["s11.a"] + 1.6, [("f{x}{q}", TINTA), (",  x,  x · ", TINTA), ("q", RAZ)], W / 2, 780, 90, "center")
    fx_em(c, t, C["s11.b"], [("x = r3{216} = 6", TINTA)], W / 2, 960, 90, "center")


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s12.a"], [("tirar", "i", 80), ("a", "i", 80), ("média", "g", 80, ERRADO)], W / 2, 180, "center")
    fx_em(c, t, C["s12.b"], [("f{4 + 9}{2} = f{13}{2} = 6,5", ERRADO)], W / 2, 400, 100, "center")
    if t < C["s13"]:
        return
    fx_em(c, t, C["s13.a"], [("6,5 ÷ 4 = 1,625", TINTA)], XE + 40, 620, 80)
    fx_em(c, t, C["s13.b"], [("9 ÷ 6,5 ≈ 1,38", TINTA)], XE + 40, 740, 80)
    E.foco(c, t, C["s13.c"], 0.5, lambda a: (E.escreve(c, "≠", 1000, 690, 140, "g", ERRADO, a),
                                             E.escreve(c, "não é PG", 1110, 690, 80, "g", ERRADO, a), E.selo(c, 1560, 660, 44, False, a)))
    E.foco(c, t, C["s13.d"], 0.5, lambda a: (fx(c, [("na PG: ", TINTA2), ("r{4 · 9} = 6", CERTO)], W / 2, 930, 90, a, "center")))


# ---------------- atalho (palco escuro) ----------------
FXS = (720, 880, 1040)


def b_atalho(c, t, C, b):
    palco(c, t)
    y1, y2 = 470, 640

    def s14():
        E.frase(c, t, C["s14.a"], [("fatore", "g", 76, BR), ("em", "i", 80, CLARO), ("vez", "i", 80, CLARO), ("de", "i", 80, CLARO), ("multiplicar", "i", 80, CLARO)],
                W / 2, 160, "center")
        fx_em(c, t, C["s14.b"], [("12, ", BR), ("x", CLARO), (", 75", BR)], W / 2, 310, 90, "center")
        E.foco(c, t, C["s14.c"], 0.4, lambda a: E.escreve(c, "12 =", 470, y1, 90, "g", BR, a))
        for i, (x, v) in enumerate(zip(FXS, (2, 2, 3))):
            E.foco(c, t, C["s14.c"] + 0.3 + 0.3 * i, 0.4, lambda a, x=x, v=v, i=i: (centro(c, str(v), x, y1, 90, "g", BR, a),
                                                                                   i < 2 and centro(c, "·", x + 80, y1 - 10, 70, "g", CLARO, a)))
        E.foco(c, t, C["s14.d"], 0.4, lambda a: E.escreve(c, "75 =", 470, y2, 90, "g", BR, a))
        for i, (x, v) in enumerate(zip(FXS, (3, 5, 5))):
            E.foco(c, t, C["s14.d"] + 0.3 + 0.3 * i, 0.4, lambda a, x=x, v=v, i=i: (centro(c, str(v), x, y2, 90, "g", BR, a),
                                                                                   i < 2 and centro(c, "·", x + 80, y2 - 10, 70, "g", CLARO, a)))
        # as duplas: 2 e 2 em cima, 3 em cima com 3 embaixo, 5 e 5 embaixo
        duplas = ((FXS[0], y1, FXS[1], y1), (FXS[2], y1, FXS[0], y2), (FXS[1], y2, FXS[2], y2))
        for k, (xa, ya, xb, yb) in enumerate(duplas):
            p = ep(t, C["s14.e"] + 0.5 * k, 0.4)
            if p > 0:
                for X, Y in ((xa, ya), (xb, yb)):
                    c.drawCircle(X, Y - 32, 62, M.paint(CERTO, p, stroke=6))
                M.line(c, xa, ya - 32, xb, yb - 32, CERTO, p * 0.8, 4, dash=[12, 10])
        fx_em(c, t, C["s14.f"], [("x = 2 · 3 · 5 = ", BR), ("30", CLARO)], W / 2, 860, 100, "center")
        E.foco(c, t, C["s14.f"] + 1.4, 0.4, lambda a: centro(c, "12 · 75 = 900 = 30 · 30", W / 2, 960, 52, "b", CLARO, a))
    E.saida(c, t, C["s15"] - 0.1, s14)
    if t < C["s15"]:
        return
    E.frase(c, t, C["s15.a"], [("dois", "i", 76, CLARO), ("grupos", "g", 72, BR), ("iguais", "g", 72, BR)], W / 2, 200, "center")
    E.foco(c, t, C["s15.a"] + 1.2, 0.5, lambda a: fx(c, [("2 · 3 · 5", BR), ("   |   ", CLARO), ("2 · 3 · 5", BR)], W / 2, 340, 90, a, "center"))
    E.foco(c, t, C["s15.b"], 0.5, lambda a: (E.pilula(c, "não compensa", 470, 580, 56, "g", fundo=ERRADO, a=a),
                                             fx(c, [("4 e 9: multiplique de cabeça", CLARO)], 720, 600, 66, a, est="i")))
    E.foco(c, t, C["s15.c"], 0.5, lambda a: (E.pilula(c, "primo sem dupla", 470, 780, 56, "g", fundo=TINTA2, a=a),
                                             fx(c, [("raiz não exata", CLARO)], 760, 800, 66, a, est="i")))
    E.foco(c, t, C["s15.d"], 0.5, lambda a: fx(c, [("cerque entre dois inteiros", BR)], 760, 900, 66, a, est="i"))


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s16"], ps("hora de testar", "i", 72, COR), XE, 150)
    E.foco(c, t, C["s16.a"], 0.5, lambda a: (E.bola(c, XE + 40, 304, 44, a=a), centro(c, "1", XE + 40, 326, 52, "g", BR, a)))
    fx_em(c, t, C["s16.a"] + 0.1, [("2, ", TINTA), ("x", COR), (", 50 em PG, positivos:  ", TINTA), ("x", COR), (" = ?", TINTA)], XE + 120, 330, 70)
    E.foco(c, t, C["s16.b"], 0.5, lambda a: (E.bola(c, XE + 40, 504, 44, a=a), centro(c, "2", XE + 40, 526, 52, "g", BR, a)))
    fx_em(c, t, C["s16.b"] + 0.1, [("caixa com medidas em PG", TINTA)], XE + 120, 530, 70)
    fx_em(c, t, C["s16.c"], [("volume = ", TINTA2), ("1.000 cm³", COR)], XE + 120, 650, 62)
    fx_em(c, t, C["s16.d"], [("maior medida = ", TINTA2), ("20 cm", COR)], XE + 120, 760, 62)
    fx_em(c, t, C["s16.e"], [("as três medidas?", TINTA)], XE + 120, 880, 70)
    E.saida(c, t, C["s17"] - 0.1, lambda: E.paralelepipedo(c, t, C["s16.b"] + 0.4, 1260, 760, 360, 160, 220, ("?", "?", "?"), size=50))
    if t >= C["s17"]:
        E.relogio(c, t, C["s17.a"], 1560, 560, 150)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    def s18():
        fx_em(c, t, C["s18.a"], "2 · 50 = 100", XE, 300, 84)
        fx_em(c, t, C["s18.b"], [("x", COR), ("^2", COR), (" = 100  →  ", TINTA), ("x", COR), (" = 10", TINTA)], XE, 450, 84)
        XS = (520, 960, 1400)
        fila(c, t, [(x, v, f"{i + 1}º", C["s18.c"] + 0.2 * i, COR if i == 1 else None) for i, (x, v) in enumerate(zip(XS, (2, 10, 50)))], 760, 220, 150, 90)
        for i in range(2):
            pula(c, t, C["s18.c"] + 0.6 + 0.4 * i, XS[i], XS[i + 1], 760 - 75, "×5", alto=80, size=54)
    E.saida(c, t, C["s19"] - 0.1, s18)
    if t < C["s19"]:
        return
    fx_em(c, t, C["s19.a"], [("x", COR), ("^3", COR), (" = 1.000", TINTA)], XE, 300, 84)
    fx_em(c, t, C["s19.b"], [("10 · 10 · 10 = 1.000  →  ", TINTA), ("x", COR), (" = 10", TINTA)], XE, 440, 76)
    fx_em(c, t, C["s19.c"], [("10 · ", TINTA), ("q", RAZ), (" = 20  →  ", TINTA), ("q", RAZ), (" = 2", TINTA)], XE, 580, 76)
    fx_em(c, t, C["s19.d"], [("5, 10 e 20 cm", COR)], XE, 760, 90)
    E.foco(c, t, C["s19.d"] + 1.6, 0.4, lambda a: fx(c, "5 · 10 · 20 = 1.000", XE, 880, 60, a, cor=TINTA2))
    E.paralelepipedo(c, t, C["s19.d"], 1180, 820, 440, 120, 220, ("20 cm", "5 cm", "10 cm"), size=50)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s20"], [("resumindo", "i", 92, COR)], W / 2, 200, "center")
        itens = (("s20.a", [("(meio)", COR), ("^2", COR), (" = vizinho · vizinho", TINTA)]),
                 ("s20.b", [("produto dos três: ", TINTA), ("f{x}{q}", TINTA), (",  x,  x · ", TINTA), ("q", RAZ)]))
        for i, (k, partes) in enumerate(itens):
            y = 420 + i * 230
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 330, y - 30, 56, a=a), centro(c, str(i + 1), 330, y - 7, 64, "g", BR, a)))
            fx_em(c, t, C[k] + 0.1, partes, 430, y, 84)
    E.saida(c, t, C["s21"] - 0.1, resumo)
    if t < C["s21"]:
        return
    E.frase(c, t, C["s21"], ps("próxima aula", "i", 80), XE, 260)
    E.frase(c, t, C["s21"] + 0.6, [("Soma", "g", 140, COR)], XE, 420)
    E.frase(c, t, C["s21"] + 0.9, [("da", "i", 130), ("PG", "g", 140, COR)], XE, 570)
    fx_em(c, t, C["s21.a"], [("1 + 2 + 4 + … + 512", TINTA)], 1050, 320, 80)
    E.frase(c, t, C["s21.b"], [("uma", "i", 66), ("corrente", "g", 62, COR), ("em", "i", 66), ("10", "g", 62, ENT), ("rodadas", "i", 66)], 1050, 460)
    E.foco(c, t, C["s21.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 560, 760, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s21.c"] + 0.3, 0.8))
    E.cursor(c, lerp(900, 700, p), lerp(1000, 785, p), ep(t, C["s21.c"] + 0.2, 0.4))
    E.frase(c, t, C["s21.d"], [("bons", "i", 120), ("estudos!", "i", 120, COR)], W / 2, 960, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, meio=b_meio, tres=b_tres, erro=b_erro, atalho=b_atalho, questao=b_questao,
              resposta=b_resposta, fim=b_fim)
