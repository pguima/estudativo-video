"""Visual — Estudativo · MAT-CON-008: união e interseção de intervalos.
[1, 5] ∩ ]3, 7[ = ]3, 5] e [1, 5] ∪ ]3, 7[ = [1, 7[, com as retas empilhadas e uma faixa vertical sobre a parte em comum; questão [−2, 4[ e [0, 6].
Bolinha e pintura na mesma linguagem da MAT-EQU-015 (bolinha(), pinta()). A fonte da casa não tem ∈, ⊂, ∪, ∩ nem ℕ ℤ ℚ ℝ: tx() desenha esses símbolos no peso do texto. Sem voz gravada ainda: todo instante
vem de um marcador C[...] ou de entre(), que divide o trecho entre dois marcadores e por isso acompanha a voz real."""
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_out, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Conjuntos")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-CON-008_uniao_intersecao_intervalos.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("pilha", "uniao", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
# as contas da aula
assert max(1, 3) == 3 and min(5, 7) == 5 and max(1, 4) > min(2, 6) and max(-2, 0) == 0 and min(4, 6) == 4


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- símbolos de conjunto (a fonte da casa não tem ∈ ⊂ ∪ ∩ ℕ ℤ ℚ ℝ: desenhados aqui) ----------------
_TRACO = dict(g=0.15, b=0.1, m=0.075, i=0.052, s=0.052)
_DESENHA = "∈∉⊂⊄⊃∪∩∅"
_DUPLA = "ℕℤℚℝ"
_FM = skia.FontMgr()
_CM = _FM.makeFromFile("C:/Windows/Fonts/cambria.ttc", 1)


def _f2(size, est):
    f = skia.Font(_CM, size * 1.08)
    f.setSubpixel(True)
    f.setEdging(skia.Font.Edging.kAntiAlias)
    f.setEmbolden(est in "gb")
    return f


def _wsimb(ch, size, est):
    if ch in _DESENHA:
        return size * 0.78
    f = _f2(size, est)
    return f.measureText(ch) + size * 0.04


def _simb(c, ch, x, y, size, est, cor, a):
    sw = size * _TRACO[est]
    if ch in _DUPLA:
        f = _f2(size, est)
        p = M.paint(cor, a)
        if est in "gb":
            p.setStyle(skia.Paint.kStrokeAndFill_Style); p.setStrokeWidth(size * (0.025 if est == "g" else 0.012))
        c.drawString(ch, x + size * 0.02, y, f, p)
        return
    x0, x1 = x + size * 0.1 + sw / 2, x + size * 0.68 - sw / 2
    top, bot = y - size * 0.68 + sw / 2, y - size * 0.02 - sw / 2
    r = (bot - top) / 2
    pa = skia.Path()
    if ch in "∈∉⊂⊄":
        pa.moveTo(x1, top); pa.lineTo(x0 + r, top)
        pa.arcTo(skia.Rect.MakeLTRB(x0, top, x0 + 2 * r, bot), -90, -180, False)
        pa.lineTo(x1, bot)
        if ch in "∈∉":
            pa.moveTo(x0, (top + bot) / 2); pa.lineTo(x1 - sw * 0.3, (top + bot) / 2)
    elif ch == "⊃":
        pa.moveTo(x0, top); pa.lineTo(x1 - r, top)
        pa.arcTo(skia.Rect.MakeLTRB(x1 - 2 * r, top, x1, bot), -90, 180, False)
        pa.lineTo(x0, bot)
    elif ch == "∪":
        rr = (x1 - x0) / 2
        pa.moveTo(x0, top); pa.lineTo(x0, bot - rr)
        pa.arcTo(skia.Rect.MakeLTRB(x0, bot - 2 * rr, x1, bot), 180, -180, False)
        pa.lineTo(x1, top)
    elif ch == "∩":
        rr = (x1 - x0) / 2
        pa.moveTo(x0, bot); pa.lineTo(x0, top + rr)
        pa.arcTo(skia.Rect.MakeLTRB(x0, top, x1, top + 2 * rr), 180, 180, False)
        pa.lineTo(x1, bot)
    elif ch == "∅":
        cx, cy, rr = (x0 + x1) / 2 + size * 0.02, (top + bot) / 2, (bot - top) / 2 + size * 0.02
        pa.addCircle(cx, cy, rr)
        pa.moveTo(cx + rr * 0.95, cy - rr * 1.25); pa.lineTo(cx - rr * 0.95, cy + rr * 1.25)
    if ch in "∉⊄":
        pa.moveTo(x0 + (x1 - x0) * 0.82, top - size * 0.1); pa.lineTo(x0 + (x1 - x0) * 0.18, bot + size * 0.1)
    p = M.paint(cor, a, stroke=sw)
    p.setStrokeCap(skia.Paint.kButt_Cap); p.setStrokeJoin(skia.Paint.kMiter_Join)
    c.drawPath(pa, p)


def _pedacos(s):
    out, cur = [], ""
    for ch in s:
        if ch in _DESENHA or ch in _DUPLA:
            if cur:
                out.append(cur); cur = ""
            out.append(ch)
        else:
            cur += ch
    if cur:
        out.append(cur)
    return out


def tw(s, est, size):
    """largura de um texto que pode ter símbolos de conjunto"""
    return sum(_wsimb(p, size, est) if len(p) == 1 and (p in _DESENHA or p in _DUPLA) else E.larg(p, est, size) for p in _pedacos(s))


def tx(c, s, x, y, size, est="g", cor=None, a=1.0, align="left"):
    """como E.escreve, com ∈ ∉ ⊂ ⊄ ∪ ∩ ℕ ℤ ℚ ℝ; align left/center/right"""
    if a <= 0:
        return
    cor = cor or TINTA
    w = tw(s, est, size)
    x = x - w / 2 if align == "center" else x - w if align == "right" else x
    for p in _pedacos(s):
        if len(p) == 1 and (p in _DESENHA or p in _DUPLA):
            _simb(c, p, x, y, size, est, cor, a)
            x += _wsimb(p, size, est)
        else:
            E.escreve(c, p, x, y, size, est, cor, a)
            x += E.larg(p, est, size)


def txe(c, t, t0, s, x, y, size, est="g", cor=None, align="left", d=0.5):
    E.foco(c, t, t0, d, lambda a: tx(c, s, x, y, size, est, cor, a, align))


def fz(c, t, t0, partes, x, y, align="left", passo=0.12):
    """como E.frase, aceitando os símbolos: partes = [(texto, estilo, tamanho[, cor])]"""
    esp = lambda p: p[2] * (0.24 if p[1] in "is" else 0.26)
    w = sum(tw(p[0], p[1], p[2]) for p in partes) + sum(esp(p) for p in partes[:-1])
    xx = x - w / 2 if align == "center" else x - w if align == "right" else x
    for i, p in enumerate(partes):
        cor = p[3] if len(p) > 3 else TINTA
        E.foco(c, t, t0 + i * passo, 0.5, lambda a, p=p, xx=xx, cor=cor: tx(c, p[0], xx, y, p[2], p[1], cor, a))
        xx += tw(p[0], p[1], p[2]) + esp(p)
    return w
# ---------------- peças desta trilha ----------------
def ps(txt, est="i", size=84, cor=None):
    """uma frase, palavra a palavra, no mesmo estilo"""
    return [(w, est, size, cor or TINTA) for w in txt.split()]


def entre(C, k1, k2, f):
    """instante entre dois marcadores (f = fração do trecho): acompanha a voz real sem segundos fixos"""
    return lerp(C[k1], C[k2], f)


def ln(c, t, partes, x, y, size, est="g", align="left"):
    """pedaços colados de um mesmo texto, cada um no seu instante: partes = [(texto, t0[, cor])]; devolve o x de cada pedaço"""
    ws = [tw(p[0], est, size) for p in partes]
    xx = x - sum(ws) / 2 if align == "center" else x - sum(ws) if align == "right" else x
    xs = []
    for p, w in zip(partes, ws):
        cor = p[2] if len(p) > 2 else TINTA
        E.foco(c, t, p[1], 0.45, lambda a, p=p, xx=xx, cor=cor: tx(c, p[0], xx, y, size, est, cor, a))
        xs.append(xx)
        xx += w
    return xs


def esfera(c, t, t0, cx, cy, r, s, size, cor=None, est="g"):
    """esfera da matéria que cresce com um texto (ou símbolo) dentro"""
    k = ease_back(prog(t, t0, 0.6))
    if k <= 0:
        return
    E.bola(c, cx, cy, r * k, cor)
    E.foco(c, t, t0 + 0.15, 0.4, lambda a: tx(c, s, cx, cy + size * 0.36, size, est, E.SOBRE, a, "center"))


MENOS = lambda v: (f"{v:g}" if isinstance(v, float) else str(v)).replace("-", "−").replace(".", ",")


def fm(c, t, t0, s, x, y, size, cor=None, align="left"):
    E.formula_em(c, t, t0, s, x, y, size, "g", cor or TINTA, align)


def bolinha(c, t, t0, x, y, fecha, cor=None, r=19, escuro=False):
    """bolinha da reta, como na MAT-EQU-015: cheia = o número entra; aberta = fica de fora"""
    cor = cor or COR
    k = ease_back(prog(t, t0, 0.5))
    if k <= 0:
        return
    rr = r * k
    c.drawCircle(x, y, rr, M.paint(cor if fecha else ("#07070F" if escuro else E.PAPEL)))
    c.drawCircle(x, y, rr, M.paint(cor, 1.0, stroke=7))


def pinta(c, t, t0, x_ini, x_fim, y, cor=None, d=0.9, seta=None):
    """trecho pintado da reta, crescendo de x_ini para x_fim; seta=True põe a ponta de seta no fim (pedaço sem fim)"""
    p = ease_out(prog(t, t0, d))
    if p <= 0:
        return
    cor = cor or COR
    xm = lerp(x_ini, x_fim, p)
    M.line(c, x_ini, y, xm, y, cor, 1.0, 12, cap_round=False)
    if seta and p >= 0.99:
        lado = 1 if x_fim > x_ini else -1
        M.line(c, x_fim, y, x_fim - lado * 26, y - 18, cor, 1.0, 8)
        M.line(c, x_fim, y, x_fim - lado * 26, y + 18, cor, 1.0, 8)


def ponto(c, t, t0, x, y, cor, r=15):
    E.foco(c, t, t0, 0.4, lambda a: c.drawCircle(x, y, r, M.paint(cor, a)), blur=4)


def relacao(c, a, esq, sig, dir_, y, size, cor=None, xm=W / 2, cor_sig=None):
    """inequação alinhada pelo sinal em xm (mesma montagem da MAT-EQU-015)"""
    g = size * 0.5
    E.formula(c, esq, xm - g, y, size, "g", cor, a, "right")
    centro(c, sig, xm, y, size, "g", cor_sig or cor, a)
    E.formula(c, dir_, xm + g, y, size, "g", cor, a)


def pilha(c, t, linhas, ops, xm, y0, dy, size):
    g = size * 0.5
    for k, (t0, esq, sig, dir_) in enumerate(linhas):
        y = y0 + k * dy
        ult = k == len(linhas) - 1
        velha = not ult and t >= linhas[k + 1][0]
        cor = COR if ult else (CINZA if velha else TINTA)
        E.foco(c, t, t0, 0.5, lambda a, esq=esq, sig=sig, dir_=dir_, y=y, cor=cor: relacao(c, a, esq, sig, dir_, y, size, cor, xm))
        if k < len(ops):
            to, op = ops[k]
            we = E.formula(c, esq, 0, 0, size, a=0)
            wd = E.formula(c, dir_, 0, 0, size, a=0)
            cop = CINZA if velha else COR
            yo = y + size * 0.72
            for cx in (xm - g - we / 2, xm + g + wd / 2):
                E.foco(c, t, to, 0.45, lambda a, cx=cx, cop=cop: E.formula(c, op, cx, yo, size * 0.52, "b", cop, a, "center"), sobe=8)


def colchetes(c, t, t0, s, cx, y, size, cores=None, align="center"):
    """intervalo escrito grande; cores = {índice do caractere: cor} para acender um colchete"""
    w = E.larg(s, "g", size)
    x = cx - w / 2 if align == "center" else cx

    def desenha(a):
        xx = x
        f = E.fonte("g", size)
        for i, ch in enumerate(s):
            E.escreve(c, ch, xx, y, size, "g", (cores or {}).get(i, TINTA), a)
            xx += f.measureText(ch) + E.APERTO["g"] * size
    E.foco(c, t, t0, 0.5, desenha)
    return x



# ---------------- a pilha de retas ----------------
X0, X1 = 520, 1720  # todas as retas da pilha com os mesmos números alinhados


def vx_de(vmin, vmax):
    return lambda v: X0 + (v - vmin) / (vmax - vmin) * (X1 - X0)


def trecho(c, t, t0, vx, y, a, b, fa, fb, cor=None, tb=None):
    """intervalo na reta: pinta de a a b e põe as bolinhas (tb = instante das bolinhas, se vierem antes ou depois)"""
    pinta(c, t, t0 + 0.2, vx(a), vx(b), y, cor)
    tb = t0 if tb is None else tb
    bolinha(c, t, tb, vx(a), y, fa, cor)
    bolinha(c, t, tb, vx(b), y, fb, cor)


def faixa(c, t, t0, x0, x1, y0, y1, cor=None, alfa=0.14, t1=None):
    """régua vertical sobre a parte que interessa"""
    p = ep(t, t0, 0.6)
    if p <= 0:
        return
    if t1 is not None:
        p *= 1 - ep(t, t1, 0.4)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeLTRB(x0, y0, x1, y1), 14, 14), M.paint(cor or COR, alfa * p))


def rotulo(c, t, t0, s, y, cor=None, cores=None):
    colchetes(c, t, t0, s, 280, y + 24, 76, cores)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    ka, kb, kc, kd = (C[f"s01.{k}"] for k in "abcd")

    def erro():
        xs = ln(c, t, [("[1, 5] ", ka), ("∩ ", kb - 0.3, COR), ("]3, 7[ ", kb), ("= [3, 5]", kc, ERRADO)], W / 2, 300, 120, "g", "center")
        x3 = xs[3] + tw("= ", "g", 120)
        if t >= kd:
            E.risco(c, x3 - 10, 330, x3 + tw("[3, 5]", "g", 120) + 10, 200, t, kd, ERRADO, 12)
        E.frase(c, t, entre(C, "s01.c", "s01.d", 0.3), ps("muita gente responde: fechado no 3", "i", 58, TINTA2), W / 2, 430, "center", 0.06)
        y = 760
        vx = E.reta(c, t, kd - 0.3, 260, 1660, y, 0, 8, range(0, 9), str, size=52)
        bolinha(c, t, kd + 0.2, vx(3), y, False, ERRADO, 26)
        E.frase(c, t, kd + 0.4, ps("o", "i", 76) + [("3", "g", 84, ERRADO)] + ps("não pode entrar", "i", 76), W / 2, 950, "center", 0.1)
    E.saida(c, t, C["s02"] - 0.1, erro)
    if t < C["s02"]:
        return
    ta, tb = C["s02.a"], C["s02.b"]
    E.foco(c, t, tb - 0.2, 0.7, lambda a: E.bola(c, 1560, 560, 240 * ease_back(prog(t, tb - 0.2, 0.7))), blur=0)
    E.frase(c, t, ta, ps("até o fim desta aula", "i", 90), XE, 300, passo=0.14)
    fz(c, t, entre(C, "s02.a", "s02.b", 0.2), [("cruzar", "g", 90, COR), ("∩", "g", 100, COR), ("e juntar", "g", 90, COR), ("∪", "g", 100, COR)], XE, 450)
    E.frase(c, t, entre(C, "s02.a", "s02.b", 0.4), ps("intervalos", "i", 90), XE, 580, passo=0.12)
    E.frase(c, t, entre(C, "s02.a", "s02.b", 0.6), ps("sem errar", "i", 84) + [("as pontas", "g", 90)], XE, 720, passo=0.12)
    E.foco(c, t, tb + 0.1, 0.5, lambda a: (centro(c, "+ atalho", 1560, 545, 84, "g", E.SOBRE, a),
                                           centro(c, "de prova", 1560, 640, 84, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"] + 0.3, ps("você precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "2", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 240, 700, 120, "i", TINTA, a))
    x, w = 880, 900
    E.caixa_pontilhada(c, x, 200, w, 300, ep(t, C["s03.b"], 0.5), prog_=ep(t, C["s03.b"], 0.5))
    fz(c, t, C["s03.b"] + 0.1, [("∩", "g", 76, COR), ("interseção:", "g", 60), ("um", "i", 58), ("e", "g", 62, COR), ("o outro", "i", 58)], x + 44, 290, "left", 0.1)
    fz(c, t, entre(C, "s03.b", "s03.c", 0.6), [("∪", "g", 76, COR), ("união:", "g", 60), ("pelo menos um,", "i", 58), ("ou", "g", 62, COR)], x + 44, 420, "left", 0.1)
    E.caixa_pontilhada(c, x, 550, w, 230, ep(t, C["s03.c"], 0.5), prog_=ep(t, C["s03.c"], 0.5))
    colchetes(c, t, C["s03.c"] + 0.1, "]2, 5]", x + 44, 650, 76, {0: ERRADO, 5: CERTO}, "left")
    vx = lambda v: x + 380 + (v - 1) * 90
    q = ep(t, C["s03.c"] + 0.3, 0.5)
    if q > 0:
        M.line(c, x + 360, 700, x + 860, 700, TINTA, q, 4)
    pinta(c, t, C["s03.c"] + 0.5, vx(2), vx(5), 700)
    bolinha(c, t, C["s03.c"] + 0.5, vx(2), 700, False, r=14)
    bolinha(c, t, C["s03.c"] + 0.5, vx(5), 700, True, r=14)
    py = lerp(480, 760, ease_io(prog(t, C["s03.c"] - 0.35, 0.5)))
    E.cursor(c, x + w - 30, py, ep(t, C["s03.b"], 0.4))
    E.frase(c, t, entre(C, "s03.c", "s03.end", 0.75), ps("faltou alguma?", "i", 62, COR) + ps("procure no canal", "i", 62), x, 880, "left", 0.12)


# ---------------- empilhar ----------------
YA, YB, YR = 330, 560, 860  # reta de cima, de baixo e da resposta
V = vx_de(0, 8)


def pilha_base(c, t, ta, tb, t_resp=None):
    """as duas retas da aula, alinhadas: [1, 5] em cima e ]3, 7[ embaixo"""
    for y, t0 in ((YA, ta), (YB, tb)):
        E.reta(c, t, t0 - 0.2, X0, X1, y, 0, 8, range(0, 9), str, size=46)
    rotulo(c, t, ta, "[1, 5]", YA)
    trecho(c, t, ta + 0.2, V, YA, 1, 5, True, True, TINTA)
    rotulo(c, t, tb, "]3, 7[", YB)
    trecho(c, t, tb + 0.2, V, YB, 3, 7, False, False, TINTA)


def b_pilha(c, t, C, b):
    ka, kb, kc = C["s04.a"], C["s04.b"], C["s04.c"]
    E.frase(c, t, ka, ps("empilhe as retas,", "i", 70) + [("números alinhados", "g", 74, COR)], W / 2, 150, "center", 0.1)
    pilha_base(c, t, kb, kc)
    for v in range(0, 9):
        E.foco(c, t, ka + 0.5 + 0.05 * v, 0.4, lambda a, v=v: M.line(c, V(v), YA + 40, V(v), YB - 40, FIO, a, 2))
    E.frase(c, t, kb + 0.4, ps("fechadas no 1 e no 5", "i", 52, TINTA2), V(3), YA + 130, "center", 0.06)
    E.frase(c, t, kc + 0.4, ps("abertas no 3 e no 7", "i", 52, TINTA2), V(5), YB + 130, "center", 0.06)


# ---------------- interseção ----------------
def b_intersecao(c, t, C, b):
    a5, b5, c5 = C["s05.a"], C["s05.b"], C["s05.c"]
    a6, b6, c6, d6 = (C[f"s06.{k}"] for k in "abcd")
    a7, b7, c7, d7 = (C[f"s07.{k}"] for k in "abcd")
    pilha_base(c, t, C["s05"] - 9, C["s05"] - 9)
    fz(c, t, a5, [("∩", "g", 90, COR), ("é a palavra", "i", 62), ("e:", "g", 72, COR), ("onde", "i", 62), ("ambas", "g", 66), ("estão pintadas", "i", 62)], W / 2, 150, "center", 0.08)
    faixa(c, t, c5, V(3), V(5), YA - 70, YB + 70)
    # a régua desce
    p = ease_io(prog(t, entre(C, "s05.b", "s05.c", 0.4), 1.2))
    if 0 < p < 1:
        xr = lerp(V(0.5), V(7.5), p)
        M.line(c, xr, YA - 60, xr, YB + 60, COR, 0.6, 5)
    # as pontas
    if t >= a6:
        q = ep(t, a6, 0.4)
        c.drawCircle(V(3), YB, 44, M.paint(ERRADO, q, stroke=6))
        c.drawCircle(V(3), YA, 44, M.paint(TINTA2, q * 0.6, stroke=4))
    if t >= c6:
        q = ep(t, c6, 0.4)
        c.drawCircle(V(5), YA, 44, M.paint(CERTO, q, stroke=6))
        c.drawCircle(V(5), YB, 44, M.paint(CERTO, q, stroke=6))
    E.frase(c, t, b6, [("3", "g", 60, ERRADO)] + ps("fica de fora", "i", 54, ERRADO), V(3), YB + 150, "center", 0.08)
    E.frase(c, t, d6, [("5", "g", 60, CERTO)] + ps("entra", "i", 54, CERTO), V(5), YB + 150, "center", 0.08)
    # resposta
    E.foco(c, t, a7 - 0.3, 0.4, lambda a: M.line(c, X0 - 40, YR, X1 + 60, YR, TINTA, a, 5))
    trecho(c, t, a7, V, YR, 3, 5, False, True)
    fz(c, t, a7 + 0.3, [("∩", "g", 76, COR), ("=", "g", 70)], 160, YR + 26)
    colchetes(c, t, a7 + 0.5, "]3, 5]", 300, YR + 26, 76, {0: ERRADO, 5: CERTO}, "left")
    if C["s07"] <= t:
        E.frase(c, t, b7, ps("maiores que 3 e até 5", "i", 52, TINTA2), V(4), YR + 80, "center", 0.06)
        E.foco(c, t, c7, 0.4, lambda a: E.pilula(c, "duas condições ao mesmo tempo = interseção", W / 2, 1010, 44, "b", fundo=TINTA, a=a))


# ---------------- união ----------------
def b_uniao(c, t, C, b):
    ka, kb, kc, kd, ke, kf = (C[f"s08.{k}"] for k in "abcdef")
    pilha_base(c, t, C["s08"] - 9, C["s08"] - 9)
    fz(c, t, ka, [("∪", "g", 90, COR), ("é a palavra", "i", 62), ("ou:", "g", 72, COR), ("onde", "i", 62), ("pelo menos uma", "g", 66), ("está pintada", "i", 62)], W / 2, 150, "center", 0.08)
    faixa(c, t, kc, V(1), V(7), YA - 70, YB + 70)
    if t >= kd:
        c.drawCircle(V(1), YA, 44, M.paint(CERTO, ep(t, kd, 0.4), stroke=6))
    if t >= ke:
        for y in (YA, YB):
            c.drawCircle(V(7), y, 44, M.paint(ERRADO, ep(t, ke, 0.4), stroke=6))
    E.frase(c, t, kd + 0.2, [("1", "g", 60, CERTO)] + ps("entra", "i", 54, CERTO), V(1), YB + 150, "center", 0.08)
    E.frase(c, t, ke + 0.2, [("7", "g", 60, ERRADO)] + ps("fica de fora", "i", 54, ERRADO), V(7), YB + 150, "center", 0.08)
    E.foco(c, t, kf - 0.3, 0.4, lambda a: M.line(c, X0 - 40, YR, X1 + 60, YR, TINTA, a, 5))
    trecho(c, t, kf, V, YR, 1, 7, True, False)
    fz(c, t, kf + 0.3, [("∪", "g", 76, COR), ("=", "g", 70)], 160, YR + 26)
    colchetes(c, t, kf + 0.5, "[1, 7[", 300, YR + 26, 76, {0: CERTO, 5: ERRADO}, "left")


# ---------------- o erro ----------------
def b_erro(c, t, C, b):
    ka, kb, kc, kd = (C[f"s09.{k}"] for k in "abcd")
    pilha_base(c, t, C["s09"] - 9, C["s09"] - 9)
    fz(c, t, ka, [("o erro:", "g", 70, ERRADO), ("fechar o 3", "i", 66), ("[3, 5]", "g", 70, ERRADO)], W / 2, 150, "center", 0.1)
    if t >= entre(C, "s09.a", "s09.b", 0.3):
        c.drawCircle(V(3), YA, 44, M.paint(TINTA2, ep(t, entre(C, "s09.a", "s09.b", 0.3), 0.4), stroke=5))
    if t >= kb:
        c.drawCircle(V(3), YB, 44, M.paint(ERRADO, ep(t, kb, 0.4), stroke=7))
    E.frase(c, t, kb + 0.3, ps("a de baixo deixa o 3 de fora", "i", 54, ERRADO), V(3), YB + 150, "center", 0.06)
    fz(c, t, kc, [("∩", "g", 80, COR), ("basta", "i", 60), ("uma", "g", 64), ("deixar a ponta de fora: ela", "i", 60), ("sai", "g", 66, ERRADO)], W / 2, 860, "center", 0.08)
    fz(c, t, kd, [("∪", "g", 80, COR), ("basta", "i", 60), ("uma", "g", 64), ("pegar a ponta: ela", "i", 60), ("entra", "g", 66, CERTO)], W / 2, 980, "center", 0.08)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def regra():
        ka, kb, kc, kd = (C[f"s10.{k}"] for k in "abcd")
        E.frase(c, t, C["s10"] + 0.2, ps("agora, o atalho da interseção", "i", 70, CLARO), W / 2, 150, "center", 0.1)
        E.frase(c, t, ka, [("o maior", "g", 90, BR)] + ps("dos começos,", "i", 84, CLARO), W / 2, 300, "center", 0.12)
        E.frase(c, t, ka + 0.8, [("o menor", "g", 90, BR)] + ps("dos fins", "i", 84, CLARO), W / 2, 420, "center", 0.12)
        E.frase(c, t, entre(C, "s10.a", "s10.b", 0.4), ps("começos: 1 e 3", "i", 62, CLARO), 560, 590, "center", 0.08)
        fm(c, t, kb, "maior: 3", 560, 710, 100, BR, "center")
        E.frase(c, t, entre(C, "s10.b", "s10.c", 0.4), ps("fins: 5 e 7", "i", 62, CLARO), 1360, 590, "center", 0.08)
        fm(c, t, kc, "menor: 5", 1360, 710, 100, BR, "center")
        E.frase(c, t, kd, ps("do", "i", 84, CLARO) + [("3 ao 5,", "g", 96, BR)] + ps("sem desenhar", "i", 84, CLARO), W / 2, 920, "center", 0.12)
    E.saida(c, t, C["s11"] - 0.1, regra)
    if C["s11"] - 0.1 <= t:
        def porque():
            ka, kb, kc = C["s11.a"], C["s11.b"], C["s11.c"]
            E.frase(c, t, C["s11"] + 0.2, ps("para estar em ambos, o número precisa", "i", 66, CLARO), W / 2, 200, "center", 0.07)
            E.frase(c, t, ka, ps("ter passado de", "i", 76, CLARO) + [("cada começo", "g", 82, BR)], W / 2, 380, "center", 0.1)
            E.frase(c, t, kb, ps("e não ter chegado em", "i", 76, CLARO) + [("nenhum fim", "g", 82, BR)], W / 2, 520, "center", 0.1)
            E.frase(c, t, kc, ps("o atalho acha o pedaço;", "i", 70, CLARO) + [("as pontas, confira na pilha", "g", 74, BR)], W / 2, 800, "center", 0.08)
        E.saida(c, t, C["s12"] - 0.1, porque)
    if t < C["s12"]:
        return
    ka, kb, kc = C["s12.a"], C["s12.b"], C["s12.c"]
    E.frase(c, t, ka, ps("e se o maior começo", "i", 72, CLARO) + [("passar do menor fim?", "g", 76, BR)], W / 2, 170, "center", 0.1)
    vb = lambda v: 520 + v / 7 * 1100
    for y, (a_, b_), s in ((330, (1, 2), "[1, 2]"), (470, (4, 6), "[4, 6]")):
        t0 = entre(C, "s12.a", "s12.b", 0.4) + (0.4 if y > 400 else 0)
        E.foco(c, t, t0, 0.4, lambda a, y=y, s=s: (M.line(c, 480, y, 1660, y, CLARO, a, 4), E.escreve(c, s, 200, y + 24, 70, "g", BR, a)))
        pinta(c, t, t0 + 0.2, vb(a_), vb(b_), y, CLARO)
        bolinha(c, t, t0 + 0.2, vb(a_), y, True, CLARO, escuro=True)
        bolinha(c, t, t0 + 0.2, vb(b_), y, True, CLARO, escuro=True)
    fz(c, t, kb, [("não sobra nada:", "i", 70, CLARO), ("[1, 2] ∩ [4, 6] = ∅", "g", 80, BR)], W / 2, 650, "center", 0.12)
    E.frase(c, t, entre(C, "s12.b", "s12.c", 0.6), [("não compensa", "g", 76, BR)] + ps("na união:", "i", 72, CLARO), W / 2, 820, "center", 0.1)
    E.frase(c, t, kc, [("empilhe sempre", "g", 84, BR)], W / 2, 950, "center")


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    ka, kb, kc, kd = (C[f"s13.{k}"] for k in "abcd")
    E.frase(c, t, C["s13"] + 0.2, ps("hora de testar", "i", 72, COR), XE, 170, passo=0.12)
    colchetes(c, t, ka, "A = [−2, 4[", XE, 380, 130, align="left")
    colchetes(c, t, kb, "B = [0, 6]", XE, 580, 130, align="left")
    fz(c, t, kc, [("A ∩ B", "g", 110, COR)], XE, 820)
    fz(c, t, kd, [("A ∪ B", "g", 110, COR)], XE + 460, 820)
    E.relogio(c, t, C["s14.a"], 1520, 480, 170)


# ---------------- resposta ----------------
VQ = vx_de(-3, 7)


def b_resposta(c, t, C, b):
    t0 = C["s15"] + 0.2
    ya, yb, yr = 230, 420, 690
    for y in (ya, yb):
        E.reta(c, t, t0 - 0.2, X0, X1, y, -3, 7, range(-3, 8), MENOS, size=42)
    colchetes(c, t, t0, "[−2, 4[", 250, ya + 24, 68)
    trecho(c, t, t0 + 0.2, VQ, ya, -2, 4, True, False, TINTA)
    colchetes(c, t, t0 + 0.3, "[0, 6]", 250, yb + 24, 68)
    trecho(c, t, t0 + 0.5, VQ, yb, 0, 6, True, True, TINTA)
    ka, kb, kc, kd, ke = (C[f"s15.{k}"] for k in "abcde")
    a6, b6, c6, d6 = (C[f"s16.{k}"] for k in "abcd")
    uni = t >= C["s16"]

    def inter():
        E.frase(c, t, ka, ps("maior começo:", "i", 50, TINTA2) + [("0", "g", 56)], 300, yr + 160, "center", 0.06)
        E.frase(c, t, kb, ps("menor fim:", "i", 50, TINTA2) + [("4", "g", 56)], 300, yr + 230, "center", 0.06)
        faixa(c, t, ka, VQ(0), VQ(4), ya - 60, yb + 60)
        if t >= kc:
            for y in (ya, yb):
                c.drawCircle(VQ(0), y, 38, M.paint(CERTO, ep(t, kc, 0.4), stroke=6))
        if t >= kd:
            c.drawCircle(VQ(4), ya, 38, M.paint(ERRADO, ep(t, kd, 0.4), stroke=6))
        E.foco(c, t, ke - 0.3, 0.4, lambda a: M.line(c, X0 - 40, yr, X1 + 60, yr, TINTA, a, 5))
        trecho(c, t, ke, VQ, yr, 0, 4, True, False)
        fz(c, t, ke + 0.3, [("A ∩ B = [0, 4[", "g", 80, COR)], W / 2 + 200, yr + 200, "center")
    E.saida(c, t, C["s16"] - 0.1, inter)
    if not uni:
        return
    faixa(c, t, a6, VQ(-2), VQ(6), ya - 60, yb + 60)
    if t >= b6:
        c.drawCircle(VQ(-2), ya, 38, M.paint(CERTO, ep(t, b6, 0.4), stroke=6))
    if t >= c6:
        c.drawCircle(VQ(6), yb, 38, M.paint(CERTO, ep(t, c6, 0.4), stroke=6))
    E.frase(c, t, a6 + 0.3, ps("sem buraco", "i", 54, TINTA2), VQ(2), yb + 140, "center", 0.06)
    E.foco(c, t, d6 - 0.3, 0.4, lambda a: M.line(c, X0 - 40, yr, X1 + 60, yr, TINTA, a, 5))
    trecho(c, t, d6, VQ, yr, -2, 6, True, True)
    fz(c, t, d6 + 0.3, [("A ∪ B = [−2, 6]", "g", 80, COR)], W / 2, yr + 200, "center")


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s17"] + 0.2, [("resumindo", "i", 92, COR)], W / 2, 190, "center")
        itens = (("s17.a", [("empilhe", "g", 80), ("as retas", "i", 76)]),
                 ("s17.b", [("∩", "g", 90, COR), ("onde", "i", 76), ("ambas", "g", 80), ("estão pintadas", "i", 76)]),
                 ("s17.c", [("∪", "g", 90, COR), ("onde", "i", 76), ("pelo menos uma", "g", 80), ("está", "i", 76)]),
                 ("s17.d", [("confira", "i", 76), ("cada ponta", "g", 80)]))
        for i, (k, partes) in enumerate(itens):
            y = 350 + i * 175
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 260, y - 28, 52, a=a), centro(c, str(i + 1), 260, y - 6, 60, "g", E.SOBRE, a)))
            fz(c, t, C[k] + 0.1, partes, 350, y)
    E.saida(c, t, C["s18"] - 0.1, resumo)
    if t < C["s18"]:
        return
    ka, kb, kc, kd = (C[f"s18.{k}"] for k in "abcd")
    E.frase(c, t, C["s18"] + 0.2, ps("na próxima aula,", "i", 76), XE, 230, passo=0.1)
    E.frase(c, t, ka, [("hora de praticar", "g", 100, COR)], XE, 370)
    E.frase(c, t, entre(C, "s18.a", "s18.b", 0.3), ps("Venn, conjuntos de números, geratriz e intervalos", "i", 58), XE, 480, "left", 0.06)
    E.frase(c, t, kb, ps("tudo em", "i", 76) + [("problemas", "g", 84, COR)], XE, 610, "left", 0.12)
    E.foco(c, t, kc, 0.5, lambda a: E.pilula(c, "Inscreva-se", 1500, 760, 76, estilo="g", a=a, cor=E.SOBRE))
    p = ease_io(prog(t, kc + 0.3, 0.8))
    E.cursor(c, lerp(1800, 1630, p), lerp(980, 785, p), ep(t, kc + 0.2, 0.4))
    E.frase(c, t, kd, [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 960, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, pilha=b_pilha, intersecao=b_intersecao, uniao=b_uniao, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
