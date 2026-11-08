"""Visual — Estudativo · MAT-PRO-012: praticando progressão geométrica (5 problemas).

Linguagem visual da trilha Progressões (MAT-PRO-004/005/010/011): fila de caixas com o termo dentro (preto) e a posição embaixo
(índigo); a razão é o arco verde por cima das caixas; índice escrito como índice (a₁, Sₙ) com fx(); relógio de pausa em cada problema.
Nesta aula: os juros 2.000 → 2.662 com "hoje" no 1º termo; as colunas do remédio caindo pela metade (800 … 50) com 800 ÷ 4 riscado;
9 mil, ?, 16 mil com √144 e a média 12,5 riscada; a soma da campanha (18.900) pela fórmula e pelo atalho; a bola de 5 m (20 m).
Peças locais: fx(), fx_em(), caixa(), fila(), pula(), resultado(), caixa_em() (as da trilha), fr_fx(), s_inf(), bola_quica()
(as da MAT-PRO-011), problema() e pausa()."""
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Matemática", "Progressões")
COR, CLARO = E.COR_TEXTO, E.CLARO
ENT, SAI, RAZ = COR, TINTA, CERTO  # posição n · termo aₙ · razão
ARQUIVO_FINAL = "estudativo_MAT-PRO-012_praticando_progressao_geometrica.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("questao1", "questao2", "questao3", "questao4", "questao5", "fim"))
BR = "#FFFFFF"

assert round(2000 * 1.1 ** 3, 6) == 2662 and round(1.1 ** 3, 6) == 1.331 and round(2000 * 1.1, 6) == 2200 and round(2000 * 1.21, 6) == 2420
assert 24 / 6 == 4 and 800 / 2 ** 4 == 50 and 800 / 4 == 200
assert 9 * 16 == 144 == 12 ** 2 and (9 + 16) / 2 == 12.5 and 12 / 9 == 16 / 12
assert 300 * (2 ** 6 - 1) == 18900 and 300 * 2 ** 5 == 9600 and 2 * 9600 - 300 == 18900
assert abs(5 * (8 / 5) / (2 / 5) - 20) < 1e-9 and abs(3 / (2 / 5) - 7.5) < 1e-9 and 5 + 7.5 + 7.5 == 20


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




def problema(c, t, t0, n, tema, ultimo=False):
    """cabeçalho do problema: "problema n" e o tema numa pílula"""
    E.frase(c, t, t0, [("último" if ultimo else "problema", "i", 72, COR), ("problema" if ultimo else str(n), "i" if ultimo else "g", 72, COR)], XE, 150)
    w = E.larg("último problema" if ultimo else f"problema {n}", "i", 72) + 60
    E.foco(c, t, t0 + 0.4, 0.4, lambda a: E.pilula(c, tema, XE + w + E.larg(tema, "g", 44) / 2 + 60, 128, 44, "g", fundo=TINTA, a=a))


def pausa(c, t, C, k, cx=1500, cy=520, r=150):
    if t >= C[k]:
        E.relogio(c, t, C[k + ".a"], cx, cy, r)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    E.frase(c, t, C["s01.a"], [("5", "g", 130, COR), ("problemas", "i", 120)], XE, 330)
    E.frase(c, t, C["s01.a"] + 0.8, ps("de PG", "i", 100), XE, 460)
    itens = ("juros", "remédio", "bactérias", "campanha", "bola")
    for i, s in enumerate(itens):
        E.foco(c, t, C["s01.a"] + 1.4 + 0.25 * i, 0.4, lambda a, i=i, s=s: E.pilula(c, s, XE + 150 + (i % 2) * 360, 610 + (i // 2) * 110, 46, "g",
                                                                                     fundo=COR if i % 2 == 0 else TINTA, a=a))
    E.relogio(c, t, C["s01.b"], 1460, 450, 170)
    E.frase(c, t, C["s01.b"] + 3.4, [("errar", "i", 70), ("aqui", "i", 70), ("ensina", "g", 66, COR)], 1460, 900, "center")


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s02"], [("4", "g", 90, COR), ("ferramentas", "i", 90)], XE, 180)
    itens = (("s02.a", "termo geral", [("a_n", SAI), (" = ", TINTA), ("a_1", SAI), (" · ", TINTA), ("q", RAZ), ("^{n − 1}", ENT)]),
             ("s02.b", "termo do meio", [("meio² = vizinho · vizinho", TINTA)]),
             ("s02.c", "soma de n termos", [("S_n", SAI), (" = ", TINTA), ("a_1", SAI), (" · ", TINTA), ("f{q^n − 1}{q − 1}", TINTA)]),
             ("s02.d", "soma infinita", None))
    for i, (k, l1, l2) in enumerate(itens):
        x, y = 170 + (i % 2) * 820, 260 + (i // 2) * 360
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, 760, 300, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 60)], x + 40, y + 80)
        if l2:
            fx_em(c, t, C[k] + 0.3, l2, x + 40, y + 220, 56 if k == "s02.b" else 64)
        else:
            E.foco(c, t, C[k] + 0.3, 0.5, lambda a, x=x, y=y: s_inf(c, x + 40, y + 210, 72, a))


# ---------------- 1: juros ----------------
JX = (440, 800, 1160, 1520)


def b_questao1(c, t, C, b):
    problema(c, t, C["s03.a"], 1, "juros compostos")
    E.frase(c, t, C["s03.b"], [("R$", "g", 84, COR), ("2.000", "g", 96)], XE, 380)
    E.frase(c, t, C["s03.b"] + 1.2, [("a", "i", 84), ("10%", "g", 84, COR), ("ao", "i", 84), ("mês", "i", 84)], XE, 510)
    E.frase(c, t, C["s03.c"], [("depois", "i", 84), ("de", "i", 84), ("3", "g", 84, COR), ("meses?", "g", 80)], XE, 720)
    pausa(c, t, C, "s04")


def b_resposta1(c, t, C, b):
    fx_em(c, t, C["s05.a"], [("+10%", TINTA), ("  =  ", TINTA2), ("× 1,1", RAZ)], XE, 190, 84)
    E.foco(c, t, C["s05.a"] + 0.8, 0.4, lambda a: fx(c, [("q", RAZ), (" = 1,1", TINTA)], 1500, 190, 76, a))
    cy = 470
    tb, tc = C["s05.b"], C["s05.c"]
    tt = (tb, lerp(tb, tc, 0.4), lerp(tb, tc, 0.75), tc)
    for i, (x, v) in enumerate(zip(JX, ("2.000", "2.200", "2.420", "2.662"))):
        borda = COR if (i == 3 and t >= C["s06.d"]) or (i == 0 and t >= C["s06.e"]) else None
        E.foco(c, t, tt[i], 0.5, lambda a, x=x, v=v, i=i, borda=borda: caixa(c, x, cy, 300, 140, v, a, f"{i + 1}º", 72, COR if i == 3 else None, borda))
        E.foco(c, t, tt[i] + 0.2, 0.4, lambda a, x=x, i=i: centro(c, "hoje" if i == 0 else f"mês {i}", x, cy + 175, 44, "i", TINTA2, a))
    for i in range(3):
        pula(c, t, tt[i + 1] - 0.3, JX[i], JX[i + 1], cy - 70, "× 1,1", alto=60, size=44)
    if t >= C["s06.d"]:
        E.caixa_pontilhada(c, JX[3] - 170, cy - 90, 340, 270, ep(t, C["s06.d"], 0.4), COR, ep(t, C["s06.d"], 0.4))
    E.foco(c, t, C["s06.d"] + 0.3, 0.4, lambda a: E.pilula(c, "4º termo", JX[3], cy - 170, 44, "g", a=a))
    E.foco(c, t, C["s06.e"], 0.4, lambda a: E.pilula(c, "o 1º", JX[0], cy - 170, 44, "g", a=a))

    x0, s = XE, 80
    fx_em(c, t, C["s06.a"], [("a_4", SAI), (" = 2.000 · 1,1", TINTA), ("^3", ENT)], x0, 780, s)
    fx_em(c, t, C["s06.b"], [("1,1", TINTA), ("^3", ENT), (" = 1,331", TINTA)], x0, 910, s)
    fx_em(c, t, C["s06.c"], [("1,331 × 2.000 = ", TINTA)], 900, 910, s)
    resultado(c, t, C["s06.c"] + 0.4, "2.662", 1650, 880, 105, CERTO)


# ---------------- 2: meia-vida ----------------
def b_questao2(c, t, C, b):
    problema(c, t, C["s07.a"], 2, "remédio")
    E.frase(c, t, C["s07.b"], [("meia-vida:", "g", 64, COR), ("o", "i", 66), ("tempo", "i", 66), ("para", "i", 66), ("cair", "i", 66), ("pela", "i", 66), ("metade", "g", 64)], XE, 330)
    E.frase(c, t, C["s07.c"], [("meia-vida", "i", 76), ("de", "i", 76), ("6", "g", 76, COR), ("horas", "i", 76)], XE, 500)
    E.frase(c, t, C["s07.d"], [("dose:", "i", 76), ("800", "g", 76, COR), ("mg", "i", 76)], XE, 630)
    E.frase(c, t, C["s07.e"], [("quanto", "i", 80), ("resta", "i", 80), ("em", "i", 80), ("24", "g", 80, COR), ("horas?", "g", 76)], XE, 820)
    pausa(c, t, C, "s08")


def b_resposta2(c, t, C, b):
    fx_em(c, t, C["s09.a"], [("24 ÷ 6 = ", TINTA), ("4", COR), (" meias-vidas", TINTA)], XE, 170, 72)
    E.foco(c, t, C["s09.b"], 0.4, lambda a: fx(c, [("q", RAZ), (" = f{1}{2}", TINTA)], 1500, 170, 76, a))
    dados = [("0 h", 800), ("6 h", 400), ("12 h", 200), ("18 h", 100), ("24 h", 50)]
    tc, td = C["s09.c"], C["s09.d"]
    tt = (tc, lerp(tc, td, 0.33), lerp(tc, td, 0.6), lerp(tc, td, 0.82), td)
    x, w, slot = 240, 1100, 1100 / 5
    for i, dd in enumerate(dados):
        E.colunas(c, t, tt[i] - 0.3, [dd + ((COR if i == 4 else E.mix(COR, "#FFFFFF", 0.35)),)], x + slot * i, 330, slot, 500, vmax=900, size=46)
    resultado(c, t, td + 0.6, "50 mg", 1600, 560, 120, CERTO)

    if t < C["s10"]:
        return
    E.foco(c, t, C["s10.a"], 0.5, lambda a: fx(c, [("800 ÷ 4 = ", TINTA), ("200", ERRADO)], XE, 990, 66, a))
    if t >= C["s10.a"] + 0.6:
        E.risco(c, XE - 10, 1000, XE + 400, 940, t, C["s10.a"] + 0.6, ERRADO, 9)
    fx_em(c, t, C["s10.b"], [("800 ÷ 16 = 50", CERTO)], 760, 990, 66)
    fx_em(c, t, C["s10.c"], [("2", TINTA), ("^4", ENT), (" = 16", TINTA)], 1340, 990, 66)


# ---------------- 3: termo do meio ----------------
BXS = (560, 960, 1360)


def b_questao3(c, t, C, b):
    problema(c, t, C["s11.a"], 3, "bactérias")
    E.frase(c, t, C["s11.a"] + 1.2, ps("cresce em PG, hora a hora", "i", 66), XE, 300)
    cy = 560
    vals = ((C["s11.b"], "9 mil", "8 h"), (C["s11.d"], "?", "9 h"), (C["s11.c"], "16 mil", "10 h"))
    for (t0, v, h), x in zip(vals, BXS):
        E.foco(c, t, t0, 0.5, lambda a, x=x, v=v, h=h: caixa(c, x, cy, 300, 150, v, a, h, 76, CINZA if v == "?" else None))
    E.frase(c, t, C["s11.d"] + 0.4, [("quantas", "i", 80), ("às", "i", 80), ("9", "g", 80, COR), ("horas?", "g", 76)], XE, 860)
    pausa(c, t, C, "s12", 1640, 860, 110)


def b_resposta3(c, t, C, b):
    cy = 300
    meio = "12 mil" if t >= C["s13.d"] else "?"
    for i, (x, v, h) in enumerate(zip(BXS, ("9 mil", meio, "16 mil"), ("8 h", "9 h", "10 h"))):
        cor = COR if i == 1 and v != "?" else (CINZA if v == "?" else None)
        E.foco(c, t, C["s13"], 0.5, lambda a, x=x, v=v, h=h, cor=cor, i=i: caixa(c, x, cy, 300, 150, v, a, h, 76, cor, COR if i == 1 and t >= C["s13.a"] else None))
    E.saida(c, t, C["s14"] - 0.1, lambda: E.foco(c, t, C["s13.a"], 0.4, lambda a: E.pilula(c, "termo do meio", BXS[1], cy - 130, 44, "g", a=a)))

    def s13():
        fx_em(c, t, C["s13.b"], [("meio² = vizinho · vizinho", TINTA)], XE, 590, 72)
        fx_em(c, t, C["s13.c"], [("9 · 16 = 144", TINTA)], XE, 720, 84)
        E.foco(c, t, C["s13.c"] + 0.3, 0.4, lambda a: E.escreve(c, "em milhares", XE + 560, 720, 48, "i", TINTA2, a))
        fx_em(c, t, C["s13.d"], [("r{144} = ", TINTA), ("12", COR)], XE, 880, 92)
        E.foco(c, t, C["s13.e"], 0.5, lambda a: (fx(c, [("−12", ERRADO)], 1100, 880, 92, a), E.selo(c, 1320, 850, 40, False, a),
                                                 E.escreve(c, "não existe quantidade negativa", 1000, 970, 46, "i", ERRADO, a)))
    E.saida(c, t, C["s14"] - 0.1, s13)
    if t < C["s14"]:
        return
    E.foco(c, t, C["s14.a"], 0.5, lambda a: fx(c, [("(9 + 16) ÷ 2 = ", TINTA), ("12,5", ERRADO)], XE, 620, 80, a))
    if t >= C["s14.a"] + 1.2:
        E.risco(c, XE - 10, 630, XE + 760, 560, t, C["s14.a"] + 1.2, ERRADO, 10)
    E.foco(c, t, C["s14.a"] + 1.6, 0.4, lambda a: E.pilula(c, "isso é PA", 1250, 595, 50, "g", fundo=ERRADO, a=a))
    for i in range(2):
        pula(c, t, C["s14.b"] + 0.5 * i, BXS[i], BXS[i + 1], cy - 75, "× 4/3", alto=60, size=46)
    fx_em(c, t, C["s14.b"] + 1.2, [("12 ÷ 9 = 16 ÷ 12 = ", TINTA), ("f{4}{3}", RAZ)], XE, 860, 80)


# ---------------- 4: soma ----------------
def b_questao4(c, t, C, b):
    problema(c, t, C["s15.a"], 4, "campanha")
    E.frase(c, t, C["s15.b"], [("1ª", "g", 76, COR), ("semana:", "i", 80), ("R$", "g", 76, COR), ("300", "g", 80)], XE, 360)
    E.frase(c, t, C["s15.c"], [("cada", "i", 80), ("semana:", "i", 80), ("o", "i", 80), ("dobro", "g", 76, RAZ)], XE, 500)
    E.frase(c, t, C["s15.d"], [("total", "i", 84), ("em", "i", 84), ("6", "g", 84, COR), ("semanas?", "g", 80)], XE, 700)
    pausa(c, t, C, "s16")


def b_resposta4(c, t, C, b):
    def s17():
        E.foco(c, t, C["s17.a"], 0.5, lambda a: fx(c, [("a_1", SAI), (" = 300     ", TINTA), ("q", RAZ), (" = 2     ", TINTA), ("n", ENT), (" = 6", TINTA)], XE, 190, 76, a))
        fx_em(c, t, C["s17.a"] + 1.4, [("S_6", SAI), (" = 300 · ", TINTA), ("f{2^6 − 1}{2 − 1}", TINTA)], XE, 400, 90)
        x0, s = XE, 76
        fx_em(c, t, C["s17.b"], [("2", TINTA), ("^6", ENT), (" = 64", TINTA)], x0, 620, s)
        fx_em(c, t, C["s17.c"], [("64 − 1 = 63", TINTA)], x0, 740, s)
        fx_em(c, t, C["s17.d"], [("63 × 300 = 18.900", TINTA)], x0, 860, s)
        fx_em(c, t, C["s17.e"] - 1.8, [("÷ (2 − 1) = ÷ 1", TINTA2)], x0, 980, s)
        resultado(c, t, C["s17.e"], "18.900", 1450, 700, 150, CERTO)
        E.foco(c, t, C["s17.e"] + 0.5, 0.4, lambda a: centro(c, "reais", 1450, 920, 60, "i", TINTA, a))
    E.saida(c, t, C["s18"] - 0.1, s17)
    if t < C["s18"]:
        return
    E.frase(c, t, C["s18"], [("pelo", "i", 72), ("atalho", "g", 70, COR)], XE, 200)
    x0, s = XE, 84
    fx_em(c, t, C["s18.a"], [("a_6", SAI), (" = 300 · 32 = 9.600", TINTA)], x0, 400, s)
    fx_em(c, t, C["s18.b"], [("próximo:  ", TINTA), ("19.200", COR)], x0, 560, s)
    fx_em(c, t, C["s18.c"], [("19.200 − 300 = ", TINTA)], x0, 760, s)
    resultado(c, t, C["s18.c"] + 0.3, "18.900", 1060, 725, 120, CERTO)
    E.foco(c, t, C["s18.c"] + 2.2, 0.5, lambda a: (centro(c, "bateu!", 1500, 760, 72, "g", CERTO, a), E.selo(c, 1500, 620, 50, True, a)))


# ---------------- 5: a bola ----------------
def b_questao5(c, t, C, b):
    problema(c, t, C["s19.a"], 5, "bola", ultimo=True)
    E.frase(c, t, C["s19.b"], [("cai", "i", 76), ("de", "i", 76), ("5", "g", 76, COR), ("metros", "i", 76)], XE, 360)
    E.frase(c, t, C["s19.c"], [("sobe", "i", 76)], XE, 520)
    E.foco(c, t, C["s19.c"] + 0.3, 0.4, lambda a: fx(c, [("f{3}{5}", COR)], XE + 210, 520, 90, a))
    E.frase(c, t, C["s19.c"] + 0.6, [("da", "i", 76), ("altura", "i", 76)], XE + 330, 520)
    E.frase(c, t, C["s19.d"], [("distância", "i", 80), ("até", "i", 80), ("parar?", "g", 76, COR)], XE, 720)

    def bq():
        if t >= C["s19.b"]:
            M.line(c, 1060, 900, 1820, 900, TINTA, 1.0, 5, progress=ep(t, C["s19.b"], 0.5))
        ts = [C["s19.b"] + 0.2, C["s19.c"], C["s19.c"] + 0.5] + [C["s19.d"] + 0.25 * i for i in range(14)]
        bola_quica(c, t, ts, 5, 3 / 5, 1150, 900, 110, 200, n=7)
        E.foco(c, t, C["s19.b"] + 0.5, 0.4, lambda a: E.escreve(c, "5 m", 1010, 660, 56, "g", TINTA, a))
    E.saida(c, t, C["s20.a"] - 0.3, bq)
    pausa(c, t, C, "s20", 1440, 470, 170)


def b_resposta5(c, t, C, b):
    def s21():
        E.frase(c, t, C["s21"], [("pelo", "i", 72), ("atalho", "g", 70, COR), ("da", "i", 72), ("bola", "i", 72)], XE, 170)
        fx_em(c, t, C["s21"] + 0.8, [("altura · f{1 + fração}{1 − fração}", TINTA2)], 1080, 180, 60)
        x0, s = XE, 84
        fx_em(c, t, C["s21.a"], [("1 + f{3}{5} = f{8}{5}", TINTA)], x0, 400, s)
        fx_em(c, t, C["s21.b"], [("1 − f{3}{5} = f{2}{5}", TINTA)], x0, 600, s)
        fx_em(c, t, C["s21.c"], [("f{8}{5} ÷ f{2}{5} = 4", TINTA)], x0, 800, s)
        fx_em(c, t, C["s21.d"], [("5 · 4 = ", TINTA)], 1000, 600, 96)
        resultado(c, t, C["s21.d"] + 0.3, "20 m", 1450, 570, 130, CERTO)
    E.saida(c, t, C["s22"] - 0.1, s21)
    if t < C["s22"]:
        return
    E.frase(c, t, C["s22"], [("conferindo", "i", 72), ("pelas", "i", 72), ("somas", "g", 70, COR)], XE, 200)
    x0, s = XE, 84
    fx_em(c, t, C["s22.a"], [("subidas: 3 + ", TINTA), ("f{9}{5}", TINTA), (" + …", TINTA)], x0, 400, s)
    E.foco(c, t, C["s22.a"] + 0.4, 0.4, lambda a: E.escreve(c, "3 = 5 · 3/5", x0 + 760, 400, 50, "i", TINTA2, a))
    fx_em(c, t, C["s22.b"], [("3 ÷ f{2}{5} = 7,5", TINTA)], x0, 600, s)
    fx_em(c, t, C["s22.c"], [("5", TINTA), (" + 7,5", COR), (" + 7,5", TINTA), (" = ", TINTA)], x0, 820, 96)
    resultado(c, t, C["s22.c"] + 0.8, "20 m", 960, 790, 110, CERTO)
    E.foco(c, t, C["s22.c"] + 2.4, 0.5, lambda a: (centro(c, "bateu!", 1450, 820, 72, "g", CERTO, a), E.selo(c, 1450, 680, 50, True, a)))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s23"], [("resumindo", "i", 92, COR)], W / 2, 170, "center")
        itens = (("s23.a", [("uma posição", TINTA), ("  →  termo geral", COR)]),
                 ("s23.b", [("dois vizinhos", TINTA), ("  →  termo do meio", COR)]),
                 ("s23.c", [("um total", TINTA), ("  →  soma", COR)]),
                 ("s23.d", [("a bola", TINTA), ("  →  soma infinita", COR)]))
        for i, (k, partes) in enumerate(itens):
            y = 340 + i * 170
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 330, y - 28, 52, a=a), centro(c, str(i + 1), 330, y - 6, 60, "g", BR, a)))
            fx_em(c, t, C[k] + 0.1, partes, 430, y, 76)
        E.foco(c, t, C["s23.d"] + 1.6, 0.4, lambda a: E.escreve(c, "com subida e descida", 430, 940, 48, "i", TINTA2, a))
    E.saida(c, t, C["s24"] - 0.1, resumo)
    if t < C["s24"]:
        return
    E.frase(c, t, C["s24.a"], [("trilha", "i", 80), ("Progressões", "g", 76), ("fechada", "i", 80, CERTO)], XE, 200)
    E.frase(c, t, C["s24.b"] - 0.6, ps("próxima aula", "i", 80), XE, 360)
    E.frase(c, t, C["s24.b"], [("Trigonometria", "g", 140, COR)], XE, 520)
    E.frase(c, t, C["s24.c"], [("sen,", "g", 72), ("cos", "g", 72), ("e", "i", 76), ("tg", "g", 72), ("no", "i", 76), ("triângulo", "i", 76), ("retângulo", "i", 76)], XE, 650)
    E.foco(c, t, C["s24.d"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 560, 800, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s24.d"] + 0.3, 0.8))
    E.cursor(c, lerp(900, 700, p), lerp(1000, 825, p), ep(t, C["s24.d"] + 0.2, 0.4))
    E.frase(c, t, C["s24.e"], [("bons", "i", 120), ("estudos!", "i", 120, COR)], 1300, 960, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, questao1=b_questao1, resposta1=b_resposta1, questao2=b_questao2, resposta2=b_resposta2,
              questao3=b_questao3, resposta3=b_resposta3, questao4=b_questao4, resposta4=b_resposta4, questao5=b_questao5,
              resposta5=b_resposta5, fim=b_fim)
