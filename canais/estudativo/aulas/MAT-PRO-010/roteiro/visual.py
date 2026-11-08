"""Visual — Estudativo · MAT-PRO-010: soma dos termos de uma PG.

Linguagem visual da trilha Progressões (MAT-PRO-004/005): fila de caixas com o termo dentro (preto) e a posição embaixo (índigo);
a razão é o arco verde por cima das caixas (na PG, "×2"); índice escrito como índice (a₁, Sₙ, aₙ) com fx(); palco escuro só no atalho.
Nesta aula: as dez colunas que dobram (1 a 512, total 1.023); as linhas S e 2S empilhadas com os termos iguais alinhados e riscados
(sobram 1.024 e 1); a fórmula Sₙ = a₁ · (qⁿ − 1)/(q − 1) com legendas; a fila 2⁰ … 2⁹ com as posições 1º … 10º no erro;
a corrente 3 → 6 → 12 desenhada como árvore.
Peças locais: fx(), fx_em(), caixa(), fila(), pula(), resultado(), caixa_em() (as da MAT-PRO-004/005) e corrente()."""
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Matemática", "Progressões")
COR, CLARO = E.COR_TEXTO, E.CLARO
ENT, SAI, RAZ = COR, TINTA, CERTO  # posição n · termo aₙ · razão
ARQUIVO_FINAL = "estudativo_MAT-PRO-010_soma_dos_termos_de_uma_pg.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("truque", "formula", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"

assert sum(2 ** i for i in range(10)) == 1023 and 2 ** 9 == 512 and 2 ** 10 == 1024 and 1024 - 1 == 1023
assert 2 ** 9 - 1 == 511 < 512
assert sum(3 * 2 ** i for i in range(10)) == 3069 == 3 * (2 ** 10 - 1) // (2 - 1)
assert 3 * 2 ** 9 == 1536 and 2 * 1536 == 3072 and 3072 - 3 == 3069


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
    """fórmula com índice de verdade (a_n, a_1, S_{10}); partes = texto ou [(texto, cor)]. Devolve [(x0, largura)] de cada parte.
    Em pedaço preto (SAI), a letra fica preta e o índice (a posição) sai em índigo"""
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
    """um termo: caixa de borda índigo com o valor dentro (preto) e a posição embaixo (índigo)"""
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


def caixa_em(c, t, t0, x0, w, y, size, cor=None, d=0.5):
    """caixa pontilhada em volta de um trecho já escrito (x0 = início, y = linha de base)"""
    p = ep(t, t0, d)
    if p > 0:
        E.caixa_pontilhada(c, x0 - 16, y - size * 0.9, w + 32, size * 1.25, p, cor, p)


def num(c, t, t0, s, x, y, size=72, cor=None, nx=None):
    """termo solto de uma linha de soma, centrado em x"""
    E.foco(c, t, t0, 0.4, lambda a: fx(c, [(s, cor or SAI)], x, y, size, a, "center"))


# ---------------- gancho ----------------
GX, GY, GW, GH = 820, 250, 1000, 560


def b_gancho(c, t, C, b):
    def s01():
        vmax = 512 * 1.16
        slot = GW / 10
        dados = [(str(i + 1), 2 ** i) for i in range(10)]
        for i, k in enumerate(("s01.a", "s01.b", "s01.c")):
            E.colunas(c, t, C[k] - 0.3, [dados[i]], GX + slot * i, GY, slot, GH, vmax=vmax, size=46)
        E.colunas(c, t, C["s01.d"] - 0.3, dados[3:], GX + slot * 3, GY, slot * 7, GH, vmax=vmax, size=46, passo=0.15)
        E.foco(c, t, C["s01.a"], 0.4, lambda a: E.escreve(c, "dia", GX - 120, GY + GH + 60, 46, "i", TINTA2, a))
        E.frase(c, t, C["s01.a"], [("R$", "g", 72, COR), ("por", "i", 80), ("dia", "i", 80)], XE, 200)
        E.frase(c, t, C["s01.c"], [("sempre", "i", 80), ("× 2", "g", 80, RAZ)], XE, 320)
        E.frase(c, t, C["s01.d"], [("por", "i", 80), ("10", "g", 80, COR), ("dias", "i", 80)], XE, 440)
        E.foco(c, t, C["s01.e"], 0.5, lambda a: E.escreve(c, "total", XE, 600, 64, "i", TINTA, a))
        E.foco(c, t, C["s01.e"] + 0.3, 0.4, lambda a: E.escreve(c, "R$", XE + 165, 600, 60, "g", COR, a))
        resultado(c, t, C["s01.e"], "1.023", XE + 400, 580, 120)
        E.frase(c, t, C["s01.e"] + 2.6, [("sem", "i", 64), ("somar", "g", 60, COR), ("os", "i", 64), ("10", "i", 64)], XE, 790)
    E.saida(c, t, C["s02"] - 0.1, s01)
    if t < C["s02"]:
        return
    E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 84), XE, 300)
    E.frase(c, t, C["s02.a"] + 1.0, [("a", "i", 130), ("soma", "g", 140, COR), ("da", "i", 130), ("PG", "g", 140, COR)], XE, 480)
    E.frase(c, t, C["s02.a"] + 2.2, [("numa", "i", 110), ("conta", "g", 110), ("só", "i", 110)], XE, 640)
    E.foco(c, t, C["s02.b"], 0.5, lambda a: E.pilula(c, "+ atalho de prova", 1420, 860, 60, "g", a=a))


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], ps("você só precisa de", "i", 84), XE, 410)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "1", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisa", XE + 200, 700, 120, "i", TINTA, a))
    x, w = 880, 900
    p = ep(t, C["s03.b"], 0.5)
    E.caixa_pontilhada(c, x, 150, w, 800, p, prog_=p)
    E.frase(c, t, C["s03.b"] + 0.1, [("a", "i", 62), ("PG", "g", 62, COR), ("e", "i", 62), ("a", "i", 62), ("razão", "i", 62), ("q", "g", 62, RAZ)], x + 44, 235)
    XS = (x + 160, x + 450, x + 740)
    fila(c, t, [(xx, v, None, C["s03.b"] + 0.6 + 0.3 * i) for i, (xx, v) in enumerate(zip(XS, (3, 6, 12)))], 500, 190, 130, 76)
    for i in range(2):
        pula(c, t, C["s03.b"] + 1.4 + 0.4 * i, XS[i], XS[i + 1], 435, "× q", alto=60, size=48)
    E.frase(c, t, C["s03.c"], [("termo", "i", 62), ("geral", "i", 62)], x + 44, 700)
    fx_em(c, t, C["s03.c"] + 0.5, [("a_n", SAI), (" = ", TINTA), ("a_1", SAI), (" · ", TINTA), ("q", RAZ), ("^{n − 1}", ENT)], x + 44, 850, 96)
    E.foco(c, t, C["s03.c"] + 4.0, 0.4, lambda a: E.escreve(c, "n − 1 = saltos", x + 600, 850, 46, "i", ENT, a))
    q = ease_io(prog(t, C["s03.c"] - 0.35, 0.5))
    E.cursor(c, x + w - 30, lerp(500, 850, q), ep(t, C["s03.b"], 0.4))


# ---------------- o truque: S e 2S ----------------
CX = [400 + 195 * i for i in range(6)] + [400 + 195 * 5 + 270]
Y1, Y2, TS = 330, 540, 78
LS = {0: "1", 1: "2", 2: "4", 3: "8", 4: "…", 5: "512"}
L2 = {1: "2", 2: "4", 3: "8", 4: "…", 5: "512", 6: "1.024"}


def _linha(c, t, termos, y, tempos, cores):
    """termos de uma linha de soma, com o + entre eles"""
    ks = sorted(termos)
    for j, k in enumerate(ks):
        cor = cores.get(k, SAI)
        num(c, t, tempos[k], termos[k], CX[k], y, TS, cor)
        if j:
            E.foco(c, t, tempos[k], 0.4, lambda a, k=k: centro(c, "+", (CX[k - 1] + CX[k]) / 2, y - 4, 64, "g", TINTA2, a))


def b_truque(c, t, C, b):
    a0 = C["s04.a"]
    t1 = {0: a0, 1: a0 + 0.46, 2: a0 + 0.92, 3: a0 + 1.38, 4: a0 + 2.0, 5: a0 + 2.6}
    e = C["s05.c"]
    _linha(c, t, LS, Y1, t1, {})
    d0 = C["s04.d"]
    t2 = {k: d0 + 0.25 * (k - 1) for k in L2}
    _linha(c, t, L2, Y2, t2, {6: COR} if t >= e else {})
    # rótulos S e 2S
    E.foco(c, t, C["s04.b"], 0.5, lambda a: fx(c, [("S =", TINTA)], 300, Y1, TS, a, "right"))
    E.foco(c, t, C["s04.c"], 0.5, lambda a: fx(c, [("2S =", TINTA)], 300, Y2, TS, a, "right"))
    E.foco(c, t, C["s04.c"], 0.5, lambda a: E.pilula(c, "× 2", 210, (Y1 + Y2) / 2 - 20, 46, "g", fundo=RAZ, a=a))
    # cada termo dobra e vira o seguinte: setas na diagonal
    for k in (0, 1, 2, 3, 5):
        tk = d0 + 0.25 * k
        if t >= tk:
            p = ep(t, tk, 0.5)
            M.arrow(c, CX[k] + 30, Y1 + 30, CX[k + 1] - 30, Y2 - 80, RAZ, p, 5, 16, p)
    # 2S vai de 2 até 1.024
    if t >= C["s05.a"]:
        E.chave(c, CX[1] - 60, CX[6] + 90, Y2 + 40, TINTA2, ep(t, C["s05.a"], 0.5), 22, 5)
    # do 2 ao 512 tudo se repete: risca nas duas linhas
    for i, k in enumerate((1, 2, 3, 5)):
        tk = C["s05.b"] + 0.3 + 0.25 * i
        w = 60 if k < 5 else 90
        for y in (Y1, Y2):
            if t >= tk:
                E.risco(c, CX[k] - w, y + 12, CX[k] + w, y - 66, t, tk, ERRADO, 9)
    E.foco(c, t, C["s05.b"] + 1.4, 0.4, lambda a: centro(c, "se repetem", (CX[1] + CX[5]) / 2, Y2 + 130, 56, "i", ERRADO, a))
    # sobram: 1.024 entrou, 1 saiu
    caixa_em(c, t, e, CX[6] - 92, 184, Y2, TS, COR)
    E.foco(c, t, e + 0.3, 0.4, lambda a: centro(c, "entrou no fim", CX[6], Y2 + 130, 50, "i", COR, a))
    caixa_em(c, t, C["s05.d"], CX[0] - 30, 60, Y1, TS, COR)
    E.foco(c, t, C["s05.d"] + 0.3, 0.4, lambda a: centro(c, "saiu do começo", CX[0], Y1 - 120, 50, "i", COR, a))
    # 2S − S = 1.024 − 1
    y = 860
    pos = fx_em(c, t, C["s06.a"], [("2S − S", TINTA)], 300, y, 96)
    fx_em(c, t, C["s06.b"], [(" = ", TINTA), ("1.024", COR), (" − ", TINTA), ("1", COR)], pos[0][0] + pos[0][1], y, 96)
    fx_em(c, t, C["s06.c"], [("S =", TINTA)], 1240, y, 96)
    resultado(c, t, C["s06.c"] + 0.2, "1.023", 1540, y - 34, 115)
    E.frase(c, t, C["s06.d"], [("termo", "i", 64), ("seguinte", "i", 64), ("ao", "i", 64), ("último", "g", 60, COR), ("−", "g", 60),
                               ("o", "i", 64), ("primeiro", "g", 60, COR)], W / 2, 1000, "center", passo=0.16)


# ---------------- a fórmula ----------------
FY = 270


def formula_topo(c, t, C, size=110):
    """Sₙ = a₁ · (qⁿ − 1)/(q − 1), no alto; devolve as posições das partes"""
    partes = [("S_n", SAI), (" = ", TINTA), ("a_1", SAI), (" · ", TINTA), ("f{q^n − 1}{q − 1}", TINTA)]
    E.saida(c, t, C["s07.c"], lambda: fx_em(c, t, C["s07.b"], [("S_n", SAI), (" = ", TINTA), ("a_1", SAI), (" · (", TINTA), ("q", RAZ),
                                                              ("^n", ENT), (" − 1)", TINTA)], W / 2, FY, size, "center"))
    return fx_em(c, t, C["s07.c"], partes, W / 2, FY + 10, size, "center")


def b_formula(c, t, C, b):
    def s07():
        E.frase(c, t, C["s07"], [("qualquer", "i", 72), ("PG", "g", 72, COR)], XE, 150)
        fx_em(c, t, C["s07.a"], [("q", RAZ), (" · S − S", TINTA)], W / 2, 620, 110, "center")
        E.foco(c, t, C["s07.a"] + 0.6, 0.4, lambda a: centro(c, "multiplique pela razão e tire a soma", W / 2, 740, 54, "i", TINTA2, a))
    E.saida(c, t, C["s08"] - 0.1, s07)
    pos = formula_topo(c, t, C)
    (xs, ws), _, (xa, wa), _, (xf, wf) = pos
    # s08: legendas
    def s08():
        yl = 470
        for t0, xm, txt, cor in ((C["s08.a"], xs + ws / 2, "soma", TINTA), (C["s08.b"], xa + wa / 2, "1º termo", TINTA)):
            E.foco(c, t, t0, 0.4, lambda a, xm=xm, txt=txt, cor=cor: (M.line(c, xm, yl - 90, xm, yl - 50, TINTA2, a, 4),
                                                                      centro(c, txt, xm, yl, 50, "i", cor, a)))
        E.foco(c, t, C["s08.a"] + 1.6, 0.4, lambda a: fx(c, [("n", ENT), (" = quantos termos", TINTA2)], xs - 40, yl + 80, 50, a, est="i"))
        E.foco(c, t, C["s08.b"] + 0.3, 0.4, lambda a: (M.line(c, xf + wf / 2, yl - 20, xf + wf / 2, yl + 10, TINTA2, a, 4),
                                                       fx(c, [("q", RAZ), (" = razão", TINTA2)], xf + wf / 2, yl + 70, 50, a, "center", "i")))
        y3 = 680
        fx_em(c, t, C["s08.c"], [("a_1", SAI), (" · ", TINTA), ("q", RAZ), ("^n", ENT)], XE + 60, y3, 92)
        E.frase(c, t, C["s08.c"] + 0.4, [("=", "g", 70), ("termo", "i", 72), ("seguinte", "i", 72), ("ao", "i", 72), ("último", "g", 66, COR)], XE + 380, y3)
        E.foco(c, t, C["s08.c"] + 2.4, 0.4, lambda a: E.pilula(c, "no exemplo: 1.024", 1630, y3 - 26, 46, "b", a=a))
        y4 = 870
        fx_em(c, t, C["s08.d"], [("q = 2:  ", RAZ), ("2S − S = ", TINTA), ("1S", COR)], XE + 60, y4, 76)
        fx_em(c, t, C["s08.d"] + 3.8, [("q = 3:  ", RAZ), ("3S − S = ", TINTA), ("2S", COR), ("  →  ÷ 2", TINTA2)], XE + 60, y4 + 120, 76)
        E.foco(c, t, C["s08.d"] + 0.3, 0.4, lambda a: centro(c, "q − 1 = 1", 1500, y4 - 6, 64, "g", TINTA2, a))
        E.foco(c, t, C["s08.d"] + 4.1, 0.4, lambda a: centro(c, "q − 1 = 2", 1500, y4 + 114, 64, "g", TINTA2, a))
    E.saida(c, t, C["s09"] - 0.1, s08)
    if t < C["s09"]:
        return

    # s09: conferir com 1, 2, 4, …, 512
    yd = 480
    def dado(t0, partes, cx):
        E.foco(c, t, t0, 0.5, lambda a: fx(c, partes, cx, yd, 86, a, "center"))
    dado(C["s09.a"], [("a_1", SAI), (" = 1", TINTA)], 440)
    dado(C["s09.b"], [("q", RAZ), (" = 2", TINTA)], 900)
    dado(C["s09.d"], [("n", ENT), (" = 10", TINTA)], 1400)
    for k, cx in (("s09.a", 440), ("s09.b", 900), ("s09.d", 1400)):
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, cx - 190, yd - 100, 380, 140, p, prog_=p)

    def s09():
        fx_em(c, t, C["s09.c"], [("512 = 2", TINTA), ("^9", ENT)], 640, 700, 92, "center")
        fx_em(c, t, C["s09.d"] - 1.4, [("n", ENT), (" − 1 = 9", TINTA)], 1280, 700, 92, "center")
        E.foco(c, t, C["s09.d"] - 1.2, 0.4, lambda a: E.escreve(c, "pelo termo geral", 1110, 790, 46, "i", TINTA2, a))
    E.saida(c, t, C["s10"] - 0.1, s09)
    if t < C["s10"]:
        return

    # s10: a conta
    x0, s = 300, 76
    fx_em(c, t, C["s10.a"], [("2", TINTA), ("^{10}", ENT), (" = 1.024", TINTA)], x0, 640, s)
    fx_em(c, t, C["s10.b"], [("1.024 − 1 = 1.023", TINTA)], x0, 745, s)
    fx_em(c, t, C["s10.c"], [("× 1", TINTA2), ("  →  1.023", TINTA)], x0, 850, s)
    fx_em(c, t, C["s10.d"], [("÷ (2 − 1)", TINTA2), (" = ÷ 1", TINTA2), ("  →  1.023", TINTA)], x0, 955, s)
    resultado(c, t, C["s10.d"] + 1.2, "1.023", 1450, 760, 130, CERTO)
    E.foco(c, t, C["s10.d"] + 2.4, 0.4, lambda a: centro(c, "bateu!", 1450, 960, 64, "g", CERTO, a))


# ---------------- erro ----------------
EXS = [W / 2 + (i - 4.5) * 172 for i in range(10)]


def b_erro(c, t, C, b):
    E.frase(c, t, C["s11.a"], [("contar", "i", 80), ("errado", "g", 76, ERRADO), ("os", "i", 80), ("termos", "i", 80)], XE, 170)
    fx_em(c, t, C["s11.a"] + 1.8, [("512 = 2", TINTA), ("^9", ENT)], XE, 330, 84)
    E.foco(c, t, C["s11.b"], 0.5, lambda a: (fx(c, [("n = 9", ERRADO)], 760, 330, 84, a), E.selo(c, 1060, 300, 40, False, a)))
    fx_em(c, t, C["s11.c"], [("2", TINTA), ("^9", ENT), (" − 1 = ", TINTA), ("511", ERRADO)], XE, 480, 84)
    E.frase(c, t, C["s12.a"], [("511", "g", 76, ERRADO), ("<", "g", 76), ("512,", "g", 76), ("o", "i", 80), ("último", "i", 80), ("sozinho?", "i", 80)], 820, 480)
    E.foco(c, t, C["s12.a"] + 2.2, 0.4, lambda a: E.pilula(c, "impossível", 1500, 330, 56, "g", fundo=ERRADO, a=a))
    # a fila 2⁰ … 2⁹ com as posições 1º … 10º
    cy = 790
    tb = C["s12.b"]
    fila(c, t, [(x, 2 ** i, None, tb + 0.12 * i) for i, x in enumerate(EXS)], cy, 150, 110, 52)
    for i, x in enumerate(EXS):
        cor = ERRADO if i == 9 and t < C["s12.c"] else ENT
        E.foco(c, t, tb + 1.4 + 0.1 * i, 0.4, lambda a, i=i, x=x, cor=cor: fx(c, [("2", TINTA2), (f"^{i}", cor if i in (0, 9) else TINTA2)], x, cy - 90, 50, a, "center"))
    E.foco(c, t, tb + 1.4, 0.4, lambda a: E.pilula(c, "expoente 0", EXS[0] + 30, cy - 200, 40, "b", a=a))
    tc = C["s12.c"]
    for i, x in enumerate(EXS):
        k = ease_back(prog(t, tc + 0.18 * i, 0.4))
        if k > 0:
            E.bola(c, x, cy + 110, 34 * k, CERTO if i < 9 else COR)
            E.foco(c, t, tc + 0.18 * i, 0.3, lambda a, i=i, x=x: centro(c, str(i + 1), x, cy + 126, 40 if i < 9 else 34, "g", BR, a), sobe=0)
    E.foco(c, t, tc + 2.0, 0.4, lambda a: fx(c, [("posição 10:  ", TINTA), ("n = 10", CERTO)], W / 2, 1010, 64, a, "center"))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def s13():
        E.frase(c, t, C["s13"], [("o", "i", 72, CLARO), ("atalho", "g", 76, BR)], W / 2, 170, "center")
        fx_em(c, t, C["s13.a"], [("S = ", BR), ("f{próximo − primeiro}{q − 1}", BR)], W / 2, 400, 104, "center")
        E.foco(c, t, C["s13.a"] + 1.6, 0.4, lambda a: centro(c, "próximo = o termo seguinte ao último", W / 2, 620, 50, "i", CLARO, a))
        E.foco(c, t, C["s13.b"] - 2.4, 0.4, lambda a: fx(c, [("q = 2  →  q − 1 = 1", CLARO)], W / 2, 770, 64, a, "center"))
        fx_em(c, t, C["s13.b"], [("S = próximo − primeiro", BR)], W / 2, 900, 84, "center")
        E.foco(c, t, C["s13.b"] + 1.5, 0.4, lambda a: centro(c, "1.024 − 1 = 1.023", W / 2, 1000, 56, "b", CLARO, a))
    E.saida(c, t, C["s14"] - 0.1, s13)
    if t < C["s14"]:
        return
    E.frase(c, t, C["s14"], ps("por que funciona", "i", 72, CLARO), W / 2, 180, "center")
    fx_em(c, t, C["s14.a"], [("a_1", BR), (" · ", BR), ("q", BR), ("^n", BR), (" = próximo", CLARO)], W / 2, 360, 96, "center")
    E.foco(c, t, C["s14.a"] + 2.6, 0.4, lambda a: centro(c, "a mesma fórmula, sem a potência", W / 2, 470, 54, "i", CLARO, a))
    E.foco(c, t, C["s14.b"], 0.5, lambda a: (E.pilula(c, "não compensa", 520, 680, 56, "g", fundo=ERRADO, a=a),
                                             fx(c, [("só n, sem o último", BR)], 820, 700, 64, a, est="g")))
    E.foco(c, t, C["s14.c"], 0.5, lambda a: fx(c, [("→ a fórmula direto", CLARO)], W / 2, 900, 80, a, "center"))


# ---------------- questão ----------------
def corrente(c, t, tn, x0, cy, dx, alto):
    """você → 3 → 6 → 12: cada pessoa repassa para duas novas. tn = instante de cada rodada"""
    niveis = [[cy]]
    for r, n in enumerate((3, 6, 12)):
        ys = [cy - alto / 2 + alto * (j + 0.5) / n for j in range(n)]
        niveis.append(ys)
    for r in range(1, 4):
        xa, xb = x0 + dx * (r - 1), x0 + dx * r
        for j, y in enumerate(niveis[r]):
            pai = 0 if r == 1 else j // 2
            ya = niveis[r - 1][pai]
            if t >= tn[r - 1]:
                M.line(c, xa + 18, ya, xb - 18, y, TINTA2, 1.0, 4, progress=ease_io(prog(t, tn[r - 1], 0.5)))
            k = ease_back(prog(t, tn[r - 1] + 0.35, 0.35))
            if k > 0:
                c.drawCircle(xb, y, 15 * k, M.paint(COR))
        E.foco(c, t, tn[r - 1] + 0.5, 0.4, lambda a, r=r, xb=xb: (centro(c, str(3 * 2 ** (r - 1)), xb, cy + alto / 2 + 80, 64, "g", COR, a),
                                                                 centro(c, f"{r}ª", xb, cy - alto / 2 - 40, 44, "b", TINTA2, a)))
    k = ease_back(prog(t, tn[0] - 0.3, 0.35))
    if k > 0:
        E.bola(c, x0, cy, 34 * k, TINTA)
    E.foco(c, t, tn[0], 0.4, lambda a: centro(c, "você", x0, cy + 90, 44, "i", TINTA, a))


def b_questao(c, t, C, b):
    E.frase(c, t, C["s15"], ps("hora de testar", "i", 72, COR), XE, 170)
    E.frase(c, t, C["s15.a"], [("1ª", "g", 64, COR), ("rodada:", "i", 68), ("3", "g", 64, COR), ("amigos", "i", 68)], XE, 340)
    E.frase(c, t, C["s15.b"], [("cada", "i", 64), ("um", "i", 64), ("repassa", "i", 64)], XE, 480)
    E.frase(c, t, C["s15.b"] + 1.2, [("para", "i", 64), ("2", "g", 60, RAZ), ("pessoas", "i", 64), ("novas", "i", 64)], XE, 570)
    E.frase(c, t, C["s15.c"], [("ao", "i", 72), ("todo,", "i", 72), ("em", "i", 72), ("10", "g", 70, COR), ("rodadas?", "g", 70, COR)], XE, 760)

    def arv():
        corrente(c, t, (C["s15.a"] + 0.4, C["s15.b"] + 1.2, C["s15.b"] + 2.0), 1030, 520, 230, 620)
        E.foco(c, t, C["s15.b"] + 2.6, 0.4, lambda a: centro(c, "…", 1820, 540, 90, "g", TINTA2, a))
    E.saida(c, t, C["s16.a"] - 0.3, arv)
    if t >= C["s16"]:
        E.relogio(c, t, C["s16.a"], 1440, 470, 170)


# ---------------- resposta ----------------
RX = (520, 860, 1200)


def b_resposta(c, t, C, b):
    def s17():
        cy = 330
        fila(c, t, [(x, v, f"{i + 1}ª", C["s17.a"] + 0.45 * i) for i, (x, v) in enumerate(zip(RX, (3, 6, 12)))] + [(1460, "…", None, C["s17.a"] + 1.4)], cy, 200, 140, 84)
        for i in range(2):
            pula(c, t, C["s17.a"] + 0.6 + 0.45 * i, RX[i], RX[i + 1], cy - 70, "× 2", alto=70, size=50)
        y = 680
        E.foco(c, t, C["s17.b"], 0.5, lambda a: fx(c, [("a_1", SAI), (" = 3", TINTA)], 480, y, 92, a, "center"))
        E.foco(c, t, C["s17.b"] + 1.0, 0.5, lambda a: fx(c, [("q", RAZ), (" = 2", TINTA)], 960, y, 92, a, "center"))
        E.foco(c, t, C["s17.c"], 0.5, lambda a: fx(c, [("n", ENT), (" = 10", TINTA)], 1440, y, 92, a, "center"))
    E.saida(c, t, C["s18"] - 0.1, s17)
    if t < C["s18"]:
        return

    def s18():
        fx_em(c, t, C["s18"], [("S_{10}", SAI), (" = 3 · ", TINTA), ("f{2^{10} − 1}{2 − 1}", TINTA)], W / 2, 250, 96, "center")
        x0, s = 300, 80
        fx_em(c, t, C["s18.a"], [("2", TINTA), ("^{10}", ENT), (" = 1.024", TINTA)], x0, 500, s)
        fx_em(c, t, C["s18.b"], [("1.024 − 1 = 1.023", TINTA)], x0, 620, s)
        fx_em(c, t, C["s18.c"], [("1.023 × 3 = 3.069", TINTA)], x0, 740, s)
        fx_em(c, t, C["s18.d"] - 1.8, [("÷ (2 − 1) = ÷ 1", TINTA2)], x0, 860, s)
        resultado(c, t, C["s18.d"], "3.069", 1480, 640, 150, CERTO)
        E.foco(c, t, C["s18.d"] + 0.6, 0.4, lambda a: centro(c, "pessoas", 1480, 870, 64, "i", TINTA, a))
    E.saida(c, t, C["s19"] - 0.1, s18)
    if t < C["s19"]:
        return
    E.frase(c, t, C["s19"], [("pelo", "i", 72), ("atalho", "g", 70, COR)], XE, 200)
    x0, s = 300, 86
    fx_em(c, t, C["s19.a"], [("a_{10}", SAI), (" = 3 · 2", TINTA), ("^9", ENT), (" = 1.536", TINTA)], x0, 400, s)
    fx_em(c, t, C["s19.b"], [("próximo:  1.536 × 2 = ", TINTA), ("3.072", COR)], x0, 560, s)
    fx_em(c, t, C["s19.c"], [("3.072 − 3 = ", TINTA)], x0, 760, s)
    resultado(c, t, C["s19.c"] + 0.3, "3.069", 1000, 730, 120, CERTO)
    E.foco(c, t, C["s19.c"] + 2.2, 0.5, lambda a: (centro(c, "bateu!", 1450, 760, 72, "g", CERTO, a), E.selo(c, 1450, 620, 50, True, a)))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s20"], [("resumindo", "i", 92, COR)], W / 2, 200, "center")
        itens = (("s20.a", [("q", RAZ), (" · S − S", TINTA)]),
                 ("s20.b", [("próximo − primeiro", TINTA)]),
                 ("s20.c", [("÷ (q − 1)", TINTA)]))
        for i, (k, partes) in enumerate(itens):
            y = 390 + i * 190
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 430, y - 30, 56, a=a), centro(c, str(i + 1), 430, y - 7, 64, "g", BR, a)))
            fx_em(c, t, C[k] + 0.1, partes, 530, y, 92)
    E.saida(c, t, C["s21"] - 0.1, resumo)
    if t < C["s21"]:
        return
    E.frase(c, t, C["s21"], ps("próxima aula", "i", 80), XE, 260)
    E.frase(c, t, C["s21.a"], [("Soma", "g", 140, COR)], XE, 420)
    E.frase(c, t, C["s21.a"] + 0.3, [("infinita", "g", 140, COR)], XE, 570)
    fx_em(c, t, C["s21.b"], [("1 + f{1}{2} + f{1}{4} + …", TINTA)], 1080, 330, 84)
    E.foco(c, t, C["s21.c"], 0.5, lambda a: fx(c, [("= ", TINTA), ("2", COR)], 1080, 500, 110, a))
    E.foco(c, t, C["s21.d"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 560, 760, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s21.d"] + 0.3, 0.8))
    E.cursor(c, lerp(900, 700, p), lerp(1000, 785, p), ep(t, C["s21.d"] + 0.2, 0.4))
    E.frase(c, t, C["s21.e"], [("bons", "i", 120), ("estudos!", "i", 120, COR)], W / 2, 960, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, truque=b_truque, formula=b_formula, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
