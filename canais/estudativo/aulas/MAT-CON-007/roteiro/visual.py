"""Visual — Estudativo · MAT-CON-007: intervalos, colchetes e reta.
]2, 5] na reta (aberta no 2, fechada no 5); [1, 3] e ]1, 3[; 2x − 1 ≤ 5 → x ≤ 3 → ]−∞, 3]; questão [−1, 4[ e 3x + 2 > 11 → ]3, +∞[.
Bolinha e pintura na mesma linguagem da MAT-EQU-015 (bolinha(), pinta()). A fonte da casa não tem ∈, ⊂, ∪, ∩ nem ℕ ℤ ℚ ℝ: tx() desenha esses símbolos no peso do texto. Sem voz gravada ainda: todo instante
vem de um marcador C[...] ou de entre(), que divide o trecho entre dois marcadores e por isso acompanha a voz real."""
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_out, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Conjuntos")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-CON-007_intervalos.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("intervalo", "infinito", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
# as contas da aula
import math
assert 2 < math.pi < 5 and 2 < math.sqrt(10) < 5 and 2 * 3 - 1 == 5 and (5 + 1) / 2 == 3 and 2 < 4.9 <= 5
assert (11 - 2) / 3 == 3 and 3 * 3 + 2 == 11 and -1 <= 3.99 < 4


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


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    ka, kb, kc, kd, ke = (C[f"s01.{k}"] for k in "abcde")

    def quantos():
        E.frase(c, t, ka, ps("quantos reais existem entre", "i", 76) + [("2 e 5?", "g", 84, COR)], W / 2, 190, "center", 0.1)
        y = 560
        vx = E.reta(c, t, ka + 0.4, 260, 1660, y, 1, 6, range(1, 7), str, size=56)
        for i, v in enumerate((3, 4)):
            ponto(c, t, kb + 0.3 * i, vx(v), y, TINTA2, 17)
        for i, (v, s, dy) in enumerate(((2.5, "2,5", 70), (math.sqrt(10), "r{10}", 190), (math.pi, "π", 70))):
            t0 = entre(C, "s01.c", "s01.d", 0.25 * i)
            ponto(c, t, t0, vx(v), y, COR, 15)
            if dy > 100:
                E.foco(c, t, t0, 0.4, lambda a, v=v: M.line(c, vx(v), y - 24, vx(v) + 50, y - 120, COR, a, 4))
            fm(c, t, t0, s, vx(v) + (80 if dy > 100 else (-30 if s == "π" else 0)), y - dy, 60, COR, "center")
        pinta(c, t, kd, vx(2), vx(5), y)
        E.frase(c, t, kd + 0.3, [("infinitos", "g", 90, COR)], W / 2, 800, "center")
        colchetes(c, t, ke, "]2, 5]", W / 2, 990, 130, {0: COR, 5: COR})
    E.saida(c, t, C["s02"] - 0.1, quantos)
    if t < C["s02"]:
        return
    ta, tb = C["s02.a"], C["s02.b"]
    E.foco(c, t, tb - 0.2, 0.7, lambda a: E.bola(c, 1560, 560, 240 * ease_back(prog(t, tb - 0.2, 0.7))), blur=0)
    E.frase(c, t, ta, ps("até o fim desta aula", "i", 90), XE, 300, passo=0.14)
    E.frase(c, t, entre(C, "s02.a", "s02.b", 0.25), ps("ler e escrever", "i", 84) + [("intervalos", "g", 90, COR)], XE, 450, passo=0.12)
    E.frase(c, t, entre(C, "s02.a", "s02.b", 0.6), ps("e desenhar", "i", 84) + [("na reta", "g", 90, COR)], XE, 600, passo=0.12)
    E.foco(c, t, tb + 0.1, 0.5, lambda a: (centro(c, "+ atalho", 1560, 545, 84, "g", E.SOBRE, a),
                                           centro(c, "de prova", 1560, 640, 84, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"] + 0.3, ps("você precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "2", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 240, 700, 120, "i", TINTA, a))
    x, w = 900, 860
    E.caixa_pontilhada(c, x, 220, w, 230, ep(t, C["s03.b"], 0.5), prog_=ep(t, C["s03.b"], 0.5))
    fz(c, t, C["s03.b"] + 0.1, [("ℝ", "g", 80, COR), ("os reais:", "g", 62), ("todos os pontos da reta", "i", 58)], x + 44, 320, "left", 0.1)
    q = ep(t, C["s03.b"] + 0.4, 0.6)
    if q > 0:
        M.line(c, x + 60, 400, x + 60 + 740 * q, 400, COR, 1.0, 10, cap_round=False)
    E.caixa_pontilhada(c, x, 500, w, 230, ep(t, C["s03.c"], 0.5), prog_=ep(t, C["s03.c"], 0.5))
    E.frase(c, t, C["s03.c"] + 0.1, [("inequação na reta", "g", 62, COR)], x + 44, 580)
    bolinha(c, t, entre(C, "s03.c", "s03.end", 0.25), x + 70, 660, True)
    E.frase(c, t, entre(C, "s03.c", "s03.end", 0.25) + 0.1, ps("entra", "i", 58), x + 110, 680)
    bolinha(c, t, entre(C, "s03.c", "s03.end", 0.45), x + 400, 660, False)
    E.frase(c, t, entre(C, "s03.c", "s03.end", 0.45) + 0.1, ps("fica de fora", "i", 58), x + 440, 680)
    py = lerp(430, 710, ease_io(prog(t, C["s03.c"] - 0.35, 0.5)))
    E.cursor(c, x + w - 30, py, ep(t, C["s03.b"], 0.4))
    E.frase(c, t, entre(C, "s03.c", "s03.end", 0.8), ps("faltou alguma?", "i", 62, COR) + ps("procure no canal", "i", 62), x, 840, "left", 0.12)


# ---------------- intervalo ----------------
def b_intervalo(c, t, C, b):
    def oque():
        ka, kb, kc = C["s04.a"], C["s04.b"], C["s04.c"]
        E.frase(c, t, ka, [("intervalo", "g", 150, COR)], W / 2, 280, "center")
        E.frase(c, t, ka + 0.5, ps("um pedaço da reta", "i", 70), W / 2, 380, "center", 0.08)
        E.foco(c, t, kb, 0.5, lambda a: (centro(c, "[", 560, 700, 240, "g", COR, a), centro(c, "]", 1360, 700, 240, "g", COR, a)))
        E.frase(c, t, kb + 0.4, ps("ponta,", "i", 80) + ps("ponta", "i", 80), W / 2, 680, "center", 0.12)
        E.frase(c, t, kc, ps("cada colchete diz", "i", 70) + [("se a ponta entra", "g", 74, COR)], W / 2, 900, "center", 0.1)
    E.saida(c, t, C["s05"] - 0.1, oque)
    if C["s05"] - 0.1 <= t:
        def lados():
            ka, kb, kc, kd = (C[f"s05.{k}"] for k in "abcd")
            for x, k, kk, s1, s2, nome, cor, fecha in ((520, ka, kb, "[3", "3]", "fechado", CERTO, True), (1400, kc, kd, "]3", "3[", "aberto", ERRADO, False)):
                E.foco(c, t, k, 0.5, lambda a, x=x, s1=s1, s2=s2: (centro(c, s1, x - 170, 460, 200, "g", TINTA, a), centro(c, s2, x + 170, 460, 200, "g", TINTA, a)))
                E.frase(c, t, k + 0.4, ps("abraça: a ponta entra" if fecha else "de costas: fica de fora", "i", 62), x, 600, "center", 0.08)
                E.frase(c, t, kk, [(nome, "g", 110, cor)], x, 800, "center")
                bolinha(c, t, kk + 0.3, x, 920, fecha, cor, 26)
        E.saida(c, t, C["s06"] - 0.1, lados)
    if C["s06"] - 0.1 <= t < C["s08"] - 0.1 + 0.5:
        def doisa5():
            ka, kb, kc, kd = (C[f"s06.{k}"] for k in "abcd")
            a7, b7, c7, d7 = (C[f"s07.{k}"] for k in "abcd")
            cores = {}
            if t >= kb:
                cores[0] = ERRADO
            if t >= kc:
                cores[5] = CERTO
            colchetes(c, t, ka, "]2, 5]", W / 2, 300, 170, cores)
            E.foco(c, t, kb + 0.2, 0.4, lambda a: centro(c, "aberto", 690, 400, 52, "g", ERRADO, a))
            E.foco(c, t, kc + 0.2, 0.4, lambda a: centro(c, "fechado", 1240, 400, 52, "g", CERTO, a))
            E.frase(c, t, kd, ps("os reais", "i", 62) + [("maiores que 2", "g", 66)] + ps("e", "i", 62) + [("até 5, com o 5", "g", 66)], W / 2, 510, "center", 0.08)
            y = 720
            vx = E.reta(c, t, C["s07"], 260, 1660, y, 0, 7, range(0, 8), str, size=52)
            pinta(c, t, c7, vx(2), vx(5), y)
            bolinha(c, t, a7, vx(2), y, False)
            bolinha(c, t, b7, vx(5), y, True)
            fm(c, t, d7, "2 < x ≤ 5", W / 2, 960, 110, COR, "center")
        E.saida(c, t, C["s08"] - 0.1, doisa5)
    if t < C["s08"]:
        return
    ka, kb, kc = C["s08.a"], C["s08.b"], C["s08.c"]
    E.frase(c, t, C["s08"] + 0.2, ps("os colchetes também podem ser", "i", 70) + [("iguais", "g", 74, COR)], W / 2, 170, "center", 0.08)
    for y, k, s, fecha, cor in ((460, ka, "[1, 3]", True, CERTO), (820, kb, "]1, 3[", False, ERRADO)):
        colchetes(c, t, k, s, 330, y + 20, 110, {0: cor, len(s) - 1: cor})
        vx = E.reta(c, t, k + 0.2, 720, 1680, y, 0, 4, range(0, 5), str, size=48)
        pinta(c, t, k + 0.6, vx(1), vx(3), y)
        bolinha(c, t, k + 0.4, vx(1), y, fecha)
        bolinha(c, t, k + 0.4, vx(3), y, fecha)
    E.frase(c, t, ka + 0.6, ps("o 1 e o 3 entram", "i", 54, CERTO), 330, 580, "center", 0.06)
    E.frase(c, t, kb + 0.6, ps("o 1 e o 3 ficam de fora", "i", 54, ERRADO), 330, 940, "center", 0.06)
    vx = lambda v: 720 + v / 4 * 960
    ponto(c, t, kc, vx(2.99), 820, CERTO, 13)
    E.foco(c, t, entre(C, "s08.c", "s08.end", 0.5), 0.4, lambda a: M.line(c, vx(2.99), 790, vx(2.99) - 60, 700, CERTO, a, 4))
    fm(c, t, entre(C, "s08.c", "s08.end", 0.5), "2,99 continua lá", vx(2.99) - 70, 680, 50, CERTO, "right")


# ---------------- infinito ----------------
def b_infinito(c, t, C, b):
    def simbolo():
        ka, kb, kc, kd = (C[f"s09.{k}"] for k in "abcd")
        E.frase(c, t, C["s09"] + 0.2, ps("e quando o pedaço", "i", 76) + [("não tem fim?", "g", 80, COR)], W / 2, 190, "center", 0.1)
        E.foco(c, t, ka, 0.5, lambda a: centro(c, "∞", W / 2, 470, 260, "g", COR, a))
        E.frase(c, t, ka + 0.4, ps("um oito deitado", "i", 56, TINTA2), W / 2, 560, "center", 0.06)
        y = 720
        E.foco(c, t, kb, 0.5, lambda a: M.arrow(c, 1000, y, 1700, y, COR, a, 8, 26, a))
        E.foco(c, t, kb + 0.2, 0.4, lambda a: centro(c, "+∞", 1600, y - 50, 90, "g", COR, a))
        E.foco(c, t, kc, 0.5, lambda a: M.arrow(c, 920, y, 220, y, COR, a, 8, 26, a))
        E.foco(c, t, kc + 0.2, 0.4, lambda a: centro(c, "−∞", 320, y - 50, 90, "g", COR, a))
        E.frase(c, t, entre(C, "s09.c", "s09.d", 0.4), ps("infinito não é um número que se alcança", "i", 58, TINTA2), W / 2, 850, "center", 0.05)
        E.frase(c, t, kd, ps("do lado do", "i", 70) + [("∞:", "g", 76)] + [("sempre aberto", "g", 76, ERRADO)], W / 2, 970, "center", 0.1)
    E.saida(c, t, C["s10"] - 0.1, simbolo)
    if t < C["s10"]:
        return
    a0, b0, c0, d0 = (C[f"s10.{k}"] for k in "abcd")
    a1, b1, c1 = C["s11.a"], C["s11.b"], C["s11.c"]
    E.frase(c, t, C["s10"] + 0.1, ps("resolva", "i", 70, COR), XE, 160)
    pilha(c, t, ((a0, "2x − 1", "≤", "5"), (b0, "2x", "≤", "6"), (d0, "x", "≤", "3")), ((b0, "+ 1"), (c0, "÷ 2")), 560, 290, 190, 104)
    E.saida(c, t, C["s11"], lambda: E.frase(c, t, c0 + 0.3, ps("2 é positivo:", "i", 52, TINTA2) + ps("o sinal fica", "i", 52, TINTA2), 1000, 520, "left", 0.06))
    y = 900
    vx = E.reta(c, t, C["s11"], 260, 1660, y, -1, 6, range(-1, 7), MENOS, size=52)
    pinta(c, t, b1, vx(3), 90, y, seta=True)
    bolinha(c, t, a1, vx(3), y, True)
    colchetes(c, t, c1, "]−∞, 3]", 1420, 380, 130, {0: ERRADO, 6: CERTO})
    E.frase(c, t, c1 + 0.6, ps("aberto no", "i", 52, TINTA2) + [("−∞,", "b", 50, TINTA2)] + ps("fechado no 3", "i", 52, TINTA2), 1420, 470, "center", 0.06)


# ---------------- o erro ----------------
def b_erro(c, t, C, b):
    ka, kb, kc, kd, ke = (C[f"s12.{k}"] for k in "abcde")
    colchetes(c, t, C["s12"] + 0.3, "]2, 5]", 420, 260, 130)
    txe(c, t, ka, "≠ {3, 4, 5}", 700, 260, 130, "g", ERRADO)
    E.frase(c, t, kb, ps("chaves listam", "i", 66) + [("elementos soltos", "g", 70, ERRADO)], W / 2, 410, "center", 0.1)
    y = 650
    vx = E.reta(c, t, kc - 0.2, 260, 1660, y, 1.5, 5.5, range(2, 6), str, size=52)
    pinta(c, t, kc, vx(2), vx(5), y)
    bolinha(c, t, kc + 0.2, vx(2), y, False)
    bolinha(c, t, kc + 0.2, vx(5), y, True)
    E.frase(c, t, kc + 0.3, ps("todos os reais do pedaço", "i", 58, COR), W / 2, 820, "center", 0.06)
    for k, v, s, dx in ((kd, 4.9, "4,9", 0), (entre(C, "s12.d", "s12.e", 0.5), math.sqrt(10), "r{10}", 0)):
        ponto(c, t, k, vx(v), y, CERTO, 14)
        fm(c, t, k + 0.1, s, vx(v) + dx, y - 50, 60, CERTO, "center")
    E.frase(c, t, ke, [("chaves", "g", 72)] + ps("para listar,", "i", 68) + [("colchetes", "g", 72, COR)] + ps("para um pedaço da reta", "i", 68), W / 2, 950, "center", 0.1)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def tracinho():
        ka, kb, kc = C["s13.a"], C["s13.b"], C["s13.c"]
        E.frase(c, t, C["s13"] + 0.2, ps("agora, o atalho: da inequação para o intervalo", "i", 64, CLARO), W / 2, 170, "center", 0.07)
        E.frase(c, t, ka, ps("olhe o", "i", 84, CLARO) + [("tracinho", "g", 90, BR)] + ps("embaixo do sinal", "i", 84, CLARO), W / 2, 330, "center", 0.12)
        for x, k, sig, txt, br, cor in ((560, kb, "≤", "fecha", "]", CERTO), (1360, kc, "<", "abre", "[", ERRADO)):
            E.foco(c, t, k, 0.5, lambda a, x=x, sig=sig: centro(c, sig, x - 120, 640, 220, "g", BR, a))
            E.foco(c, t, k + 0.3, 0.4, lambda a, x=x: centro(c, "→", x + 40, 620, 100, "g", CLARO, a))
            E.foco(c, t, k + 0.4, 0.4, lambda a, x=x, br=br, cor=cor: centro(c, br, x + 180, 640, 220, "g", cor, a))
            E.frase(c, t, k + 0.4, ps(("tem tracinho:" if sig == "≤" else "sem tracinho:"), "i", 56, CLARO) + [(txt, "g", 60, BR)], x, 820, "center", 0.08)
    E.saida(c, t, C["s14"] - 0.1, tracinho)
    if t < C["s14"]:
        return
    ka, kb, kc, kd = (C[f"s14.{k}"] for k in "abcd")
    E.frase(c, t, ka, ps("o tracinho é um pedaço do", "i", 70, CLARO) + [("=", "g", 84, BR)] + ps(": a ponta também serve", "i", 70, CLARO), W / 2, 220, "center", 0.08)
    E.frase(c, t, kb, [("não vale", "g", 80, BR)] + ps("do lado do", "i", 74, CLARO) + [("∞:", "g", 78, BR)] + ps("sempre aberto", "i", 74, CLARO), W / 2, 420, "center", 0.1)
    E.frase(c, t, kc, ps("alguns livros usam", "i", 70, CLARO) + [("parênteses", "g", 76, BR)], W / 2, 620, "center", 0.1)
    E.foco(c, t, kc + 0.6, 0.5, lambda a: (centro(c, "]2, 5]", 700, 810, 120, "g", CLARO, a), centro(c, "=", 960, 810, 120, "g", CLARO, a),
                                           centro(c, "(2, 5]", 1220, 810, 120, "g", BR, a)))
    E.frase(c, t, kd, ps("parêntese também quer dizer", "i", 64, CLARO) + [("ponta de fora", "g", 70, BR)], W / 2, 980, "center", 0.08)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    ka, kb, kc, kd, ke = (C[f"s15.{k}"] for k in "abcde")
    E.frase(c, t, C["s15"] + 0.2, ps("hora de testar", "i", 72, COR), XE, 170, passo=0.12)
    colchetes(c, t, ka, "[−1, 4[", XE, 380, 150, align="left")
    E.frase(c, t, kb, ps("o", "i", 70) + [("−1", "g", 76)] + ps("entra?", "i", 70), XE, 520, "left", 0.1)
    E.frase(c, t, kc, ps("e o", "i", 70) + [("4?", "g", 76)], XE + 480, 520, "left", 0.1)
    fm(c, t, kd, "3x + 2 > 11", XE, 750, 120, COR)
    E.frase(c, t, ke, ps("escreva como", "i", 70) + [("intervalo", "g", 76, COR)], XE, 900, "left", 0.1)
    E.relogio(c, t, C["s16.a"], 1520, 480, 170)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    def colchete():
        ka, kb, kc = C["s17.a"], C["s17.b"], C["s17.c"]
        cores = {}
        if t >= ka:
            cores[0] = CERTO
        if t >= kb:
            cores[6] = ERRADO
        colchetes(c, t, C["s17"] + 0.2, "[−1, 4[", W / 2, 300, 170, cores)
        E.frase(c, t, ka + 0.2, ps("abraça: o −1 entra", "i", 60, CERTO), 560, 440, "center", 0.06)
        E.frase(c, t, kb + 0.2, ps("de costas: o 4 fica de fora", "i", 60, ERRADO), 1360, 440, "center", 0.06)
        y = 720
        vx = E.reta(c, t, kc - 0.2, 260, 1660, y, -2, 5, range(-2, 6), MENOS, size=52)
        pinta(c, t, kc + 0.3, vx(-1), vx(4), y)
        bolinha(c, t, kc, vx(-1), y, True)
        bolinha(c, t, kc, vx(4), y, False)
        E.frase(c, t, entre(C, "s17.c", "s18", 0.6), ps("o 3,99 ainda está lá dentro", "i", 58, TINTA2), W / 2, 900, "center", 0.06)
    E.saida(c, t, C["s18"] - 0.1, colchete)
    if t < C["s18"]:
        return
    ka, kb, kc, kd = (C[f"s18.{k}"] for k in "abcd")
    pilha(c, t, ((C["s18"] + 0.2, "3x + 2", ">", "11"), (ka, "3x", ">", "9"), (kb, "x", ">", "3")), ((ka, "− 2"), (kb, "÷ 3")), 560, 230, 190, 100)
    y = 860
    vx = E.reta(c, t, kc - 0.2, 260, 1660, y, -1, 6, range(-1, 7), MENOS, size=52)
    bolinha(c, t, kc, vx(3), y, False)
    E.frase(c, t, kc + 0.1, ps("sem tracinho:", "i", 54, TINTA2) + [("aberto", "g", 58, ERRADO)], vx(3), y - 70, "center", 0.06)
    pinta(c, t, kd, vx(3) + 22, W - 90, y, seta=True)
    colchetes(c, t, kd + 0.3, "]3, +∞[", 1420, 420, 130, {0: ERRADO, 6: ERRADO})


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s19"] + 0.2, [("resumindo", "i", 92, COR)], W / 2, 210, "center")
        itens = (("s19.a", "[ 2", "abraçando: a ponta entra", True), ("s19.b", "] 2", "de costas: fica de fora", False), ("s19.c", "∞ [", "no infinito: sempre aberto", False))
        for i, (k, s, txt, fecha) in enumerate(itens):
            y = 400 + i * 190
            E.foco(c, t, C[k], 0.5, lambda a, s=s, y=y, fecha=fecha: E.escreve(c, s, 240, y, 100, "g", CERTO if fecha else ERRADO, a))
            E.frase(c, t, C[k] + 0.1, ps(txt, "i", 80), 500, y, "left", 0.08)
    E.saida(c, t, C["s20"] - 0.1, resumo)
    if t < C["s20"]:
        return
    ka, kb, kc, kd = (C[f"s20.{k}"] for k in "abcd")
    E.frase(c, t, C["s20"] + 0.2, ps("na próxima aula,", "i", 76), XE, 230, passo=0.1)
    E.frase(c, t, ka, ps("você", "i", 84) + [("cruza e junta intervalos", "g", 88, COR)], XE, 370, "left", 0.12)
    E.frase(c, t, kb, ps("empilhando uma reta sobre a outra", "i", 66), XE, 480, "left", 0.08)
    for i, (a_, b_) in enumerate(((1, 5), (3, 7))):
        y = 600 + i * 70
        q = ep(t, kb + 0.3 + 0.3 * i, 0.6)
        if q > 0:
            M.line(c, 260, y, 1000, y, FIO, q, 4)
            M.line(c, 260 + a_ * 90, y, 260 + (a_ + (b_ - a_) * q) * 90, y, COR, 1.0, 12, cap_round=False)
    E.foco(c, t, kc, 0.5, lambda a: E.pilula(c, "Inscreva-se", 1500, 740, 76, estilo="g", a=a, cor=E.SOBRE))
    p = ease_io(prog(t, kc + 0.3, 0.8))
    E.cursor(c, lerp(1800, 1630, p), lerp(960, 765, p), ep(t, kc + 0.2, 0.4))
    E.frase(c, t, kd, [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 950, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, intervalo=b_intervalo, infinito=b_infinito, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
