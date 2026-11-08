"""Visual — Estudativo · MAT-PRO-011: soma infinita de uma PG.

Linguagem visual da trilha Progressões (MAT-PRO-004/005/010): termo em preto, posição/índice em índigo (a₁, Sₙ com fx()),
razão q em verde; palco escuro só no atalho.
Nesta aula: o chão até a parede de 2 m com os passos 1, 1/2, 1/4… pintados embaixo e a chave vermelha do que falta; colunas que
encolhem (q = 1/2) ao lado das que crescem (q = 2, riscadas); a fórmula com qⁿ riscado até sobrar S = a₁/(1 − q); a bola que quica
(subidas em índigo, descidas tracejadas em preto); 0,444… = 4/10 + 4/100 + …
Peças locais: fx(), fx_em(), caixa(), fila(), pula(), resultado(), caixa_em() (as da MAT-PRO-004/005/010), fr_fx(), s_inf(),
trilho() e bola_quica()."""
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Matemática", "Progressões")
COR, CLARO = E.COR_TEXTO, E.CLARO
ENT, SAI, RAZ = COR, TINTA, CERTO  # posição n · termo aₙ · razão
ARQUIVO_FINAL = "estudativo_MAT-PRO-011_soma_infinita_de_uma_pg.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("parede", "formula", "bola", "erro", "dizima", "atalho", "questao", "fim"))
BR = "#FFFFFF"

assert 1 / (1 - 1 / 2) == 2 and (1 / 2) ** 10 == 1 / 1024
assert abs(5 / (1 - 1 / 2) - 10) < 1e-9 and 10 + 10 + 10 == 30 and 10 / (1 - 1 / 2) == 20
assert abs(10 * 1.5 / 0.5 - 30) < 1e-9
assert abs((4 / 10) / (1 - 1 / 10) - 4 / 9) < 1e-12
assert abs(4 / (1 - 1 / 3) - 6) < 1e-9 and 12 + 6 + 6 == 24 and abs(12 * 4 / 3 - 16) < 1e-9 and abs(16 / (2 / 3) - 24) < 1e-9


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


def fr_fx(c, cima, baixo, x, y, size, a=1.0, align="left", est="g"):
    """fração com índice dentro (a₁ em cima, 1 − q embaixo): cima e baixo = partes de fx(). y = linha de base da conta. Devolve a largura"""
    s_ = size * 0.78
    wc = sum(w for _, w in fx(None, cima, 0, 0, s_, 0, est=est))
    wb = sum(w for _, w in fx(None, baixo, 0, 0, s_, 0, est=est))
    w = max(wc, wb) + size * 0.16
    xi = x - w / 2 if align == "center" else x - w if align == "right" else x
    if a > 0:
        fx(c, cima, xi + w / 2, y - size * 0.46, s_, a, "center", est)
        fx(c, baixo, xi + w / 2, y + size * 0.46, s_, a, "center", est)
        b = max(4, size * 0.07)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(xi, y - size * 0.3 - b / 2, w, b), b / 2, b / 2), M.paint(TINTA if est else TINTA, a))
    return w


def s_inf(c, x, y, size, a=1.0, align="left", cor=TINTA):
    """S = a₁ / (1 − q)"""
    w1 = sum(w for _, w in fx(None, [("S = ", cor)], 0, 0, size, 0))
    wf = fr_fx(None, [("a_1", SAI)], [("1 − ", TINTA), ("q", RAZ)], 0, 0, size, 0)
    xi = x - (w1 + wf) / 2 if align == "center" else x
    if a > 0:
        fx(c, [("S = ", cor)], xi, y, size, a)
        fr_fx(c, [("a_1", SAI)], [("1 − ", TINTA), ("q", RAZ)], xi + w1, y, size, a)
    return xi, w1 + wf


# ---------------- a parede: passos 1, 1/2, 1/4, … ----------------
PX0, PX1 = 260, 1660
PM = (PX1 - PX0) / 2  # px por metro
ROT = ("1", "f{1}{2}", "f{1}{4}", "f{1}{8}")


def _pos(k):
    return 2 * (1 - 2 ** -k)


def trilho(c, t, t0, ts, y, falta=None, rotulos=3):
    """chão, parede a 2 m e os passos; ts = instante de cada passo. falta = instante em que a chave do que falta aparece"""
    a = ep(t, t0, 0.6)
    if a <= 0:
        return
    M.line(c, PX0 - 40, y, PX1, y, TINTA, a, 5, progress=a)
    # parede
    q = ep(t, t0 + 0.2, 0.5)
    if q > 0:
        M.rrect(c, PX1, y - 300 * q, 46, 300 * q, 6, TINTA2, a)
        for k in range(6):
            yy = y - 40 - k * 46
            if yy > y - 300 * q:
                M.line(c, PX1 + 6, yy, PX1 + 40, yy - 26, "#FFFFFF", 0.5 * a, 3)
    E.foco(c, t, t0 + 0.4, 0.4, lambda a: centro(c, "parede", PX1 + 23, y - 330, 44, "i", TINTA2, a))
    # cota de 2 m
    if t >= t0 + 0.5:
        p = ep(t, t0 + 0.5, 0.6)
        yc = y - 200
        M.line(c, PX0, yc, lerp(PX0, PX1, p), yc, TINTA2, 1.0, 3)
        for xx in (PX0, PX1):
            M.line(c, xx, yc - 14, xx, yc + 14, TINTA2, p, 3)
        E.foco(c, t, t0 + 0.8, 0.4, lambda a: centro(c, "2 m", (PX0 + PX1) / 2, yc - 26, 56, "g", TINTA, a))
    # passos: barra embaixo do chão
    pos = 0.0
    for k, tk in enumerate(ts):
        p = ease_io(prog(t, tk, 0.5))
        if p <= 0:
            break
        xa, xb = PX0 + PM * _pos(k), PX0 + PM * _pos(k + 1)
        cor = COR if k % 2 == 0 else E.mix(COR, "#FFFFFF", 0.45)
        M.rrect(c, xa, y + 14, max(2, (xb - xa) * p - 3), 44, 6, cor, 1.0)
        if k < rotulos:
            E.foco(c, t, tk + 0.2, 0.4, lambda a, xa=xa, xb=xb, k=k: E.formula(c, ROT[k], (xa + xb) / 2, y + 150, 76, "g", COR, a, "center"))
        pos = lerp(_pos(k), _pos(k + 1), p)
    # quem anda
    xw = PX0 + PM * pos
    k = ease_back(prog(t, t0 + 0.3, 0.4))
    if k > 0:
        E.bola(c, xw, y - 34, 30 * k, TINTA)
    if falta is not None and t >= falta and pos < 1.999:
        E.chave(c, xw + 36, PX1 - 6, y - 80, ERRADO, ep(t, falta, 0.4), -22, 5)
    return pos


def b_gancho(c, t, C, b):
    def s01():
        E.frase(c, t, C["s01.a"], [("a", "i", 80), ("2", "g", 80, COR), ("metros", "i", 80), ("da", "i", 80), ("parede", "i", 80)], XE, 170)
        ts = [C["s01.b"], C["s01.c"], C["s01.d"]] + [C["s01.d"] + 2.0 + 0.32 * i for i in range(7)]
        trilho(c, t, C["s01.a"], ts, 620)
        E.foco(c, t, C["s01.d"] + 1.2, 0.4, lambda a: E.pilula(c, "sempre a metade", 1300, 170 - 22, 50, "g", fundo=RAZ, a=a))
        E.frase(c, t, C["s01.e"], [("infinitos", "g", 72, COR), ("passos", "i", 76)], XE, 900)
        E.foco(c, t, C["s01.f"], 0.5, lambda a: fx(c, [("1 + f{1}{2} + f{1}{4} + … = ", TINTA), ("2", COR)], 1000, 900, 84, a))
    E.saida(c, t, C["s02"] - 0.1, s01)
    if t < C["s02"]:
        return
    E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 80), XE, 220)
    itens = ((C["s02.a"] + 1.4, [("soma ", TINTA), ("infinita", COR), (" numa conta", TINTA)]),
             (C["s02.b"], [("a bola que ", TINTA), ("quica", COR)]))
    for i, (t0, partes) in enumerate(itens):
        y = 420 + i * 180
        E.foco(c, t, t0, 0.5, lambda a, i=i, y=y: (E.bola(c, XE + 40, y - 30, 48, a=a), centro(c, str(i + 1), XE + 40, y - 6, 56, "g", BR, a)))
        fx_em(c, t, t0 + 0.1, partes, XE + 130, y, 90)
    E.foco(c, t, C["s02.b"] + 2.4, 0.5, lambda a: E.pilula(c, "+ atalho de prova", 1420, 860, 60, "g", a=a))


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], ps("você só precisa de", "i", 84), XE, 410)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "2", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 900, 880
    itens = (("s03.b", "soma da PG", [("S_n", SAI), (" = ", TINTA), ("a_1", SAI), (" · ", TINTA), ("f{q^n − 1}{q − 1}", TINTA)]),
             ("s03.c", "fração de uma dízima", [("0,444… = f{4}{9}", COR)]))
    for i, (k, l1, l2) in enumerate(itens):
        y = 200 + i * 360
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 300, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 62)], x + 44, y + 84)
        fx_em(c, t, C[k] + 0.3, l2, x + 44, y + 210, 84)
    q = ease_io(prog(t, C["s03.c"] - 0.35, 0.5))
    E.cursor(c, x + w - 30, lerp(200 + 270, 560 + 270, q), ep(t, C["s03.b"], 0.4))


# ---------------- por que não estoura ----------------
def b_parede(c, t, C, b):
    def s04():
        E.frase(c, t, C["s04"], [("por", "i", 76), ("que", "i", 76), ("não", "i", 76), ("estoura?", "g", 72, COR)], XE, 170)
        ts = [C["s04.b"] - 0.6, C["s04.c"] - 0.6, C["s04.d"]] + [C["s04.e"] + 0.3 * i for i in range(7)]
        pos = trilho(c, t, C["s04"], ts, 600, falta=C["s04.a"], rotulos=3)
        xw = PX0 + PM * (pos or 0)
        if t >= C["s04.a"] and (pos or 0) < 1.999:
            f = 2 - (pos or 0)
            txt = "2" if f > 1.99 else "1" if abs(f - 1) < 0.01 else "f{1}{2}" if abs(f - 0.5) < 0.01 else "f{1}{4}" if abs(f - 0.25) < 0.01 else None
            if txt and xw + 36 < PX1 - 60:
                cx = min((xw + PX1) / 2, PX1 - 170)
                E.foco(c, t, C["s04.a"] + 0.2, 0.3, lambda a: (centro(c, "falta", cx - 70, 460, 60, "i", ERRADO, a),
                                                              E.formula(c, txt, cx + 40, 460, 70, "g", ERRADO, a)))
        E.foco(c, t, C["s04.d"], 0.5, lambda a: fx(c, [("cada passo = ", TINTA), ("metade", COR), (" do que falta", TINTA)], XE, 870, 64, a))
        E.foco(c, t, C["s04.e"], 0.5, lambda a: fx(c, [("falta: 1 → f{1}{2} → f{1}{4} → … → ", TINTA2), ("0", ERRADO)], XE, 1000, 60, a))
    E.saida(c, t, C["s05"] - 0.1, s04)
    if t < C["s05"]:
        return
    fx_em(c, t, C["s05.a"], [("−1 < ", TINTA), ("q", RAZ), (" < 1", TINTA)], W / 2, 210, 100, "center")
    meio = lambda v: {1: "1", 0.5: "f{1}{2}", 0.25: "f{1}{4}", 0.125: "f{1}{8}", 0.0625: "f{1}{16}"}.get(v, str(int(v)))
    E.colunas(c, t, C["s05.b"], [("", 1 / 2 ** i) for i in range(5)], 180, 380, 680, 480, vmax=1.35, fmt=meio, size=46)
    E.foco(c, t, C["s05.b"], 0.4, lambda a: fx(c, [("q", RAZ), (" = f{1}{2}", TINTA)], 520, 990, 72, a, "center"))
    E.foco(c, t, C["s05.b"] + 1.4, 0.4, lambda a: centro(c, "encolhem", 520, 340, 56, "i", CERTO, a))
    E.colunas(c, t, C["s05.c"], [("", 2 ** i, CINZA) for i in range(5)], 1060, 380, 680, 480, vmax=20, size=46)
    E.foco(c, t, C["s05.c"], 0.4, lambda a: fx(c, [("q", RAZ), (" = 2", TINTA)], 1400, 990, 72, a, "center"))
    if t >= C["s05.c"] + 1.4:
        E.risco(c, 1080, 860, 1720, 400, t, C["s05.c"] + 1.4, ERRADO, 14)
    E.foco(c, t, C["s05.c"] + 1.8, 0.4, lambda a: E.pilula(c, "sem fim", 1400, 330, 50, "g", fundo=ERRADO, a=a))


# ---------------- a fórmula ----------------
FY = 260
FS = 110


def b_formula(c, t, C, b):
    partes = [("S_n", SAI), (" = ", TINTA), ("a_1", SAI), (" · ", TINTA), ("f{q^n − 1}{q − 1}", TINTA)]

    def s06():
        pos = fx_em(c, t, C["s06"], partes, W / 2, FY, FS, "center")
        xf, wf = pos[4]
        s_ = FS * 0.78
        wn = E.formula(None, "q^n − 1", 0, 0, s_, a=0)
        wq = E.formula(None, "q^n", 0, 0, s_, a=0)
        xn = xf + (wf - FS * 0.1 - wn) / 2
        caixa_em(c, t, C["s06.a"], xn - 4, wq + 10, FY - FS * 0.46, s_, COR)
        if t >= C["s06.d"]:
            E.risco(c, xn - 10, FY - FS * 0.4, xn + wq + 10, FY - FS * 1.1, t, C["s06.d"], ERRADO, 10)
        fx_em(c, t, C["s06.b"], [("(f{1}{2})^{10} = f{1}{1.024}", TINTA)], W / 2, 600, 96, "center")
        E.foco(c, t, C["s06.c"], 0.5, lambda a: fx(c, [("≈ 0,001  →  quase ", TINTA2), ("0", COR)], W / 2, 780, 80, a, "center"))
        E.foco(c, t, C["s06.d"], 0.5, lambda a: fx(c, [("infinitos termos:  ", TINTA2), ("q", RAZ), ("^n", ENT), (" some", ERRADO)], W / 2, 940, 76, a, "center"))
    E.saida(c, t, C["s07"] - 0.1, s06)
    if t < C["s07"]:
        return

    def s07a():
        w1 = sum(w for _, w in fx(None, [("S = ", TINTA)], 0, 0, FS, 0))
        wf = fr_fx(None, [("−a_1", SAI)], [("q − 1", TINTA)], 0, 0, FS, 0)
        x = W / 2 - (w1 + wf) / 2
        E.foco(c, t, C["s07.a"], 0.5, lambda a: (fx(c, [("S = ", TINTA)], x, FY, FS, a), fr_fx(c, [("−a_1", SAI)], [("q − 1", TINTA)], x + w1, FY, FS, a)))
        tt = lerp(C["s07.a"], C["s07.b"], 0.33)
        E.frase(c, t, tt, [("troque", "i", 64), ("o", "i", 64), ("sinal", "g", 60, COR), ("em", "i", 64), ("cima", "i", 64), ("e", "i", 64), ("embaixo", "i", 64)], W / 2, 520, "center")
        E.foco(c, t, lerp(C["s07.a"], C["s07.b"], 0.62), 0.5, lambda a: fx(c, [("f{−6}{−2} = f{6}{2} = 3", TINTA2)], W / 2, 720, 80, a, "center"))
    E.saida(c, t, C["s07.b"] - 0.1, s07a)
    if t < C["s07.b"]:
        return

    def s07b():
        yf, sf = 420, 160
        E.foco(c, t, C["s07.b"], 0.5, lambda a: s_inf(c, W / 2, yf, sf, a, "center"))
        xi, w = s_inf(None, W / 2, yf, sf, 0, "center")
        p = ep(t, C["s07.b"] + 0.6, 0.5)
        E.caixa_pontilhada(c, xi - 50, yf - 230, w + 100, 420, p, COR, p)
        E.foco(c, t, C["s07.b"] + 0.6, 0.4, lambda a: centro(c, "soma infinita", W / 2, yf - 260, 60, "i", COR, a))
        E.foco(c, t, C["s07.c"], 0.4, lambda a: fx(c, [("q", RAZ), (" = razão", TINTA2)], xi + w + 280, yf + 130, 64, a, "center", "i"))
        fx_em(c, t, C["s07.d"], [("−1 < ", TINTA), ("q", RAZ), (" < 1", TINTA)], W / 2, 860, 110, "center")
    E.saida(c, t, C["s08"] - 0.1, s07b)
    if t < C["s08"]:
        return
    E.frase(c, t, C["s08"], [("na", "i", 72), ("parede", "g", 70, COR)], XE, 170)
    E.foco(c, t, C["s08.a"], 0.5, lambda a: fx(c, [("a_1", SAI), (" = 1", TINTA), ("      q", RAZ), (" = f{1}{2}", TINTA)], XE, 350, 84, a))
    fx_em(c, t, C["s08.b"], [("1 − f{1}{2} = f{1}{2}", TINTA)], XE, 540, 90)
    fx_em(c, t, C["s08.c"], [("S = 1 ÷ f{1}{2} = 1 · 2 = 2", TINTA)], XE, 760, 96)
    resultado(c, t, C["s08.d"], "2 m", 1450, 600, 150, CERTO)
    E.foco(c, t, C["s08.d"] + 0.4, 0.4, lambda a: centro(c, "os 2 metros da parede", 1450, 830, 52, "i", TINTA, a))


# ---------------- a bola ----------------
def quiques(H, r, x0, yb, esc, larg0, n=9):
    """trechos da bola: (tipo, xa, xb, h). tipo 'q' = queda inicial, 's' = subida, 'd' = descida"""
    out = [("q", x0, x0, H)]
    x = x0
    for k in range(1, n + 1):
        h = H * r ** k
        w = larg0 * (h / (H * r)) ** 0.5
        out.append(("s", x, x + w / 2, h))
        out.append(("d", x + w / 2, x + w, h))
        x += w
    return out


def bola_quica(c, t, ts, H, r, x0, yb, esc, larg0, n=9, cores=None, mostra=True):
    """desenha a trajetória até onde ts (instante de cada trecho) deixa; a bola fica na ponta"""
    cores = cores or {"q": TINTA, "s": COR, "d": TINTA}
    tr = quiques(H, r, x0, yb, esc, larg0, n)
    ponta = None
    for i, (tipo, xa, xb, h) in enumerate(tr):
        if i >= len(ts):
            break
        d = 0.5 if i < 3 else 0.25
        p = ease_io(prog(t, ts[i], d)) if tipo != "q" else ease_in2(prog(t, ts[i], d))
        if p <= 0:
            break
        cor = cores[tipo]
        if tipo == "q":
            ya = yb - h * esc
            M.line(c, xa, ya, xa, lerp(ya, yb, p), cor, 1.0, 6)
            ponta = (xa, lerp(ya, yb, p))
        else:
            path = skia.Path()
            N = 30
            xm = xb if tipo == "s" else xa  # topo
            for j in range(N + 1):
                u = j / N * p
                x = lerp(xa, xb, u)
                y = yb - h * esc * (1 - ((x - xm) / (xb - xa)) ** 2)
                path.moveTo(x, y) if j == 0 else path.lineTo(x, y)
                ponta = (x, y)
            pt = M.paint(cor, 1.0, stroke=6, cap_round=True)
            if tipo == "d":
                pt.setPathEffect(skia.DashPathEffect.Make([18, 12], 0))
            c.drawPath(path, pt)
    if ponta and mostra:
        E.bola(c, ponta[0], ponta[1] - 22, 22, ERRADO)
    return tr


def ease_in2(p):
    return p * p


BX0, BYB, BESC, BL0 = 330, 900, 56, 260


def chao(c, t, t0, x0=200, x1=1150, y=BYB):
    if t >= t0:
        M.line(c, x0, y, x1, y, TINTA, 1.0, 5, progress=ep(t, t0, 0.5))


def b_bola(c, t, C, b):
    chao(c, t, C["s09"])
    ts = [C["s09.a"], C["s09.b"], C["s09.b"] + 0.5] + [C["s09.c"] + 0.25 * i for i in range(16)]
    tr = bola_quica(c, t, ts, 10, 0.5, BX0, BYB, BESC, BL0, n=7)
    # alturas
    E.foco(c, t, C["s09.a"] + 0.4, 0.4, lambda a: (M.line(c, BX0 - 40, BYB - 560, BX0 - 40, BYB, TINTA2, a, 3),
                                                   E.escreve(c, "10 m", BX0 - 190, BYB - 260, 60, "g", TINTA, a)))
    for k, (t0, txt) in enumerate(((C["s10.b"], "5"), (C["s10.c"], "2,5"), (C["s11.a"] + 1.0, "1,25"))):
        _, xa, xb, h = tr[1 + 2 * k]
        E.foco(c, t, t0, 0.4, lambda a, xb=xb, h=h, txt=txt, k=k: centro(c, txt, xb, BYB - h * BESC - 30, 56 - 6 * k, "g", COR, a))
    E.foco(c, t, C["s09.b"] + 0.3, 0.4, lambda a: E.pilula(c, "sobe a metade", 760, 300, 46, "g", fundo=COR, a=a))
    E.foco(c, t, C["s10.a"], 0.4, lambda a: E.pilula(c, "queda", BX0 + 40, BYB - 620, 40, "b", fundo=TINTA, a=a))

    def s09():
        E.frase(c, t, C["s09.c"], [("distância", "i", 72), ("até", "i", 72), ("parar?", "g", 70, COR)], 1180, 300)
    E.saida(c, t, C["s10"] - 0.1, s09)
    xr = 1220

    def s10():
        E.foco(c, t, C["s10.b"], 0.4, lambda a: (M.line(c, xr, 390, xr + 70, 390, COR, a, 7),
                                                 E.escreve(c, "sobe", xr + 90, 405, 56, "i", COR, a)))
        E.foco(c, t, C["s10.b"] + 0.6, 0.4, lambda a: (M.line(c, xr + 280, 390, xr + 350, 390, TINTA, a, 6, dash=[18, 12]),
                                                       E.escreve(c, "desce", xr + 370, 405, 56, "i", TINTA, a)))
        E.foco(c, t, C["s10.d"], 0.5, lambda a: E.pilula(c, "conta 2 vezes", xr + 280, 540, 56, "g", fundo=COR, a=a))
    E.saida(c, t, C["s11"] - 0.1, s10)
    if t < C["s11"]:
        return
    x0 = xr - 40
    E.foco(c, t, C["s11.a"], 0.5, lambda a: E.escreve(c, "subidas", x0, 330, 64, "g", COR, a))
    fx_em(c, t, C["s11.a"] + 0.4, [("5 + 2,5 + 1,25 + …", TINTA)], x0, 430, 64)
    fx_em(c, t, C["s11.b"], [("5 ÷ f{1}{2} = ", TINTA), ("10", COR)], x0, 570, 72)
    fx_em(c, t, C["s11.c"], [("descidas", TINTA), (" = 10", TINTA)], x0, 710, 64)
    fx_em(c, t, C["s11.d"], [("10 + 10 + 10 = ", TINTA)], x0, 880, 72)
    resultado(c, t, C["s11.d"] + 0.5, "30 m", 1730, 850, 100, CERTO)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s12.a"], [("tudo", "i", 76), ("na", "i", 76), ("fórmula", "i", 76), ("de", "i", 76), ("uma", "i", 76), ("vez", "g", 72, ERRADO)], XE, 180)
    E.foco(c, t, C["s12.b"], 0.5, lambda a: (fx(c, [("10 ÷ f{1}{2} = ", TINTA), ("20", ERRADO)], XE, 360, 90, a), E.selo(c, 900, 330, 44, False, a)))
    fx_em(c, t, C["s12.c"], [("10 + 5 + 2,5 + …", TINTA), ("  = 20", ERRADO)], XE, 560, 80)
    E.foco(c, t, C["s12.c"] + 0.5, 0.4, lambda a: E.escreve(c, "cada altura uma vez só", XE + 1000, 560, 50, "i", ERRADO, a))
    fx_em(c, t, C["s12.d"], [("10", TINTA), (" + 5 + 5", COR), (" + 2,5 + 2,5", COR), (" + …", TINTA), ("  = 30", CERTO)], XE, 760, 80)
    E.foco(c, t, C["s12.d"] + 0.5, 0.4, lambda a: E.escreve(c, "sobe e desce", XE + 1150, 760, 56, "i", COR, a))
    E.foco(c, t, C["s12.e"], 0.5, lambda a: (caixa_em(c, t, C["s12.e"], XE, E.formula(None, "10", 0, 0, 80, a=0), 760, 80, TINTA),
                                             E.escreve(c, "a 1ª queda: só uma vez", XE - 10, 900, 52, "i", TINTA, a)))


# ---------------- dízima ----------------
def b_dizima(c, t, C, b):
    def s13():
        E.foco(c, t, C["s13.a"], 0.5, lambda a: fx(c, [("0,444…", COR)], W / 2, 280, 150, a, "center"))
        fx_em(c, t, C["s13.b"], [("f{4}{10} + f{4}{100} + f{4}{1.000} + …", TINTA)], W / 2, 560, 100, "center")
        E.foco(c, t, C["s13.c"], 0.5, lambda a: fx(c, [("a_1", SAI), (" = f{4}{10}", TINTA), ("        q", RAZ), (" = f{1}{10}", TINTA)], W / 2, 830, 90, a, "center"))
    E.saida(c, t, C["s14"] - 0.1, s13)
    if t < C["s14"]:
        return
    E.foco(c, t, C["s14"], 0.5, lambda a: fx(c, [("0,444…", COR)], XE, 200, 90, a))
    fx_em(c, t, C["s14.a"], [("1 − f{1}{10} = f{9}{10}", TINTA)], XE, 420, 96)
    fx_em(c, t, C["s14.b"], [("f{4}{10} ÷ f{9}{10} = ", TINTA)], XE, 680, 96)
    xr = XE + E.formula(None, "f{4}{10} ÷ f{9}{10} = ", 0, 0, 96, a=0) + 20
    E.foco(c, t, C["s14.b"] + 0.6, 0.5, lambda a: fx(c, [("f{4}{9}", CERTO)], xr, 680, 120, a))
    E.foco(c, t, C["s14.c"], 0.5, lambda a: fx(c, [("= a fração da dízima", CERTO)], xr + 160, 690, 56, a, est="i"))
    if t >= C["s14.d"]:
        p = ep(t, C["s14.d"], 0.5)
        E.caixa_pontilhada(c, xr - 10, 650, 100, 105, p, COR, p)
        w1 = E.formula(None, "1 − f{1}{10} = ", 0, 0, 96, a=0)
        E.caixa_pontilhada(c, XE + w1 - 16, 290, 110, 100, p, COR, p)
    E.foco(c, t, C["s14.d"] + 0.4, 0.4, lambda a: E.escreve(c, "o 9 de baixo", xr + 120, 800, 52, "i", COR, a))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def s15():
        E.frase(c, t, C["s15"], [("o", "i", 72, CLARO), ("atalho", "g", 76, BR), ("da", "i", 72, CLARO), ("bola", "g", 76, BR)], W / 2, 170, "center")
        fx_em(c, t, C["s15.a"], [("altura · f{1 + fração}{1 − fração}", BR)], W / 2, 400, 104, "center")
        E.foco(c, t, C["s15.a"] + 2.0, 0.4, lambda a: centro(c, "fração = quanto ela sobe", W / 2, 590, 50, "i", CLARO, a))
        fx_em(c, t, C["s15.b"], [("10 · 1,5 = 15", BR)], W / 2, 760, 84, "center")
        fx_em(c, t, C["s15.c"], [("15 ÷ f{1}{2} = ", BR), ("30", CLARO)], W / 2, 920, 90, "center")
    E.saida(c, t, C["s16"] - 0.1, s15)
    if t < C["s16"]:
        return
    E.frase(c, t, C["s16"], ps("por que funciona", "i", 72, CLARO), W / 2, 170, "center")
    fx_em(c, t, C["s16.a"], [("descidas = ", CLARO), ("f{altura}{1 − fração}", BR)], W / 2, 360, 84, "center")
    fx_em(c, t, C["s16.b"], [("subidas = descidas · fração", BR)], W / 2, 540, 72, "center")
    E.foco(c, t, C["s16.c"], 0.5, lambda a: (E.pilula(c, "não compensa", 470, 720, 52, "g", fundo=ERRADO, a=a),
                                             fx(c, [("lançada para cima", BR)], 740, 740, 64, a, est="g")))
    E.foco(c, t, C["s16.d"], 0.5, lambda a: fx(c, [("só as subidas  →  ", BR), ("somas uma a uma", CLARO)], 740, 880, 64, a, est="g"))


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s17"], ps("hora de testar", "i", 72, COR), XE, 170)
    E.frase(c, t, C["s17.a"], [("cai", "i", 76), ("de", "i", 76), ("12", "g", 76, COR), ("metros", "i", 76)], XE, 360)
    E.frase(c, t, C["s17.b"], [("sobe", "i", 76)], XE, 520)
    E.foco(c, t, C["s17.b"] + 0.3, 0.4, lambda a: fx(c, [("f{1}{3}", COR)], XE + 210, 520, 90, a))
    E.frase(c, t, C["s17.b"] + 0.6, [("da", "i", 76), ("altura", "i", 76)], XE + 330, 520)
    E.frase(c, t, C["s17.c"], [("distância", "i", 80), ("até", "i", 80), ("parar?", "g", 76, COR)], XE, 720)

    def bq():
        if t >= C["s17.a"]:
            M.line(c, 1060, 900, 1820, 900, TINTA, 1.0, 5, progress=ep(t, C["s17.a"], 0.5))
        ts = [C["s17.a"] + 0.2, C["s17.b"], C["s17.b"] + 0.5] + [C["s17.c"] + 0.25 * i for i in range(10)]
        bola_quica(c, t, ts, 12, 1 / 3, 1150, 900, 50, 300, n=6)
        E.foco(c, t, C["s17.a"] + 0.5, 0.4, lambda a: E.escreve(c, "12 m", 1000, 620, 56, "g", TINTA, a))
    E.saida(c, t, C["s18.a"] - 0.3, bq)
    if t >= C["s18"]:
        E.relogio(c, t, C["s18.a"], 1440, 470, 170)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    def s19():
        x0, s = XE, 80
        fx_em(c, t, C["s19.a"], [("subidas: 4 + f{4}{3} + …   ", TINTA), ("q", RAZ), (" = f{1}{3}", TINTA)], x0, 230, s)
        fx_em(c, t, C["s19.b"], [("1 − f{1}{3} = f{2}{3}", TINTA)], x0, 430, s)
        fx_em(c, t, C["s19.c"], [("4 ÷ f{2}{3} = 4 · f{3}{2} = ", TINTA), ("6", COR)], x0, 630, s)
        fx_em(c, t, C["s19.d"], [("12", TINTA), (" + 6", COR), (" + 6", TINTA), (" = ", TINTA)], x0, 870, 96)
        resultado(c, t, C["s19.d"] + 0.6, "24 m", 900, 840, 120, CERTO)
        E.foco(c, t, C["s19.d"] + 0.3, 0.4, lambda a: E.escreve(c, "queda + subidas + descidas", 1100, 870, 46, "i", TINTA2, a))
    E.saida(c, t, C["s20"] - 0.1, s19)
    if t < C["s20"]:
        return
    E.frase(c, t, C["s20"], [("pelo", "i", 72), ("atalho", "g", 70, COR)], XE, 200)
    fx_em(c, t, C["s20.a"], [("12 · f{4}{3} = 16", TINTA)], XE, 450, 96)
    fx_em(c, t, C["s20.b"], [("16 ÷ f{2}{3} = 16 · f{3}{2} = ", TINTA)], XE, 700, 96)
    resultado(c, t, C["s20.b"] + 0.5, "24", 1350, 670, 110, CERTO)
    E.foco(c, t, C["s20.b"] + 1.6, 0.5, lambda a: (centro(c, "bateu!", 1650, 700, 72, "g", CERTO, a), E.selo(c, 1650, 560, 50, True, a)))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s21"], [("resumindo", "i", 92, COR)], W / 2, 200, "center")
        E.foco(c, t, C["s21.a"], 0.5, lambda a: (E.bola(c, 430, 410, 56, a=a), centro(c, "1", 430, 433, 64, "g", BR, a)))
        fx_em(c, t, C["s21.a"] + 0.1, [("−1 < ", TINTA), ("q", RAZ), (" < 1", TINTA)], 530, 440, 92)
        E.foco(c, t, C["s21.b"], 0.5, lambda a: (E.bola(c, 430, 680, 56, a=a), centro(c, "2", 430, 703, 64, "g", BR, a)))
        E.foco(c, t, C["s21.b"] + 0.1, 0.5, lambda a: s_inf(c, 530, 710, 110, a))
    E.saida(c, t, C["s22"] - 0.1, resumo)
    if t < C["s22"]:
        return
    E.frase(c, t, C["s22"], ps("próxima aula", "i", 80), XE, 260)
    E.frase(c, t, C["s22.a"], [("Praticando", "g", 140, COR)], XE, 420)
    E.frase(c, t, C["s22.a"] + 0.3, [("PG", "g", 140, COR)], XE, 570)
    E.frase(c, t, C["s22.b"], [("juros", "g", 64)], 1180, 330)
    E.frase(c, t, C["s22.b"] + 0.8, [("remédio", "g", 64), ("no", "i", 66), ("sangue", "i", 66)], 1180, 440)
    E.frase(c, t, C["s22.b"] + 1.8, [("bola", "g", 64), ("quicando", "i", 66)], 1180, 550)
    E.foco(c, t, C["s22.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 560, 760, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s22.c"] + 0.3, 0.8))
    E.cursor(c, lerp(900, 700, p), lerp(1000, 785, p), ep(t, C["s22.c"] + 0.2, 0.4))
    E.frase(c, t, C["s22.d"], [("bons", "i", 120), ("estudos!", "i", 120, COR)], W / 2, 960, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, parede=b_parede, formula=b_formula, bola=b_bola, erro=b_erro,
              dizima=b_dizima, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
