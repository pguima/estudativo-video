"""Visual — Estudativo · MAT-POR-014: erro relativo, qual erro pesa mais.
Linguagem da trilha Porcentagem (cartao, maquina, fluxo: as mesmas peças de MAT-POR-005): o valor de partida é o cartão
escuro, o resultado é o cartão na cor da matéria e a máquina guarda a conta ("÷ 200 cm", "− 20%"). A conversão de unidade
usa a ESCADA do metro de MAT-MED-001 (degraus m, dm, cm, mm; a bolinha pula e a vírgula anda uma casa por degrau).
Peças desta aula: parede() do pedreiro, engrenagem() do relojoeiro, a balança do gancho (E.balanca, que vira para o lado
do erro que pesa mais), anda_z() (a vírgula anda e os zeros da frente somem: 0,005 → 0,5) e a pizza em 10 e em 200 fatias.
A voz é real: os marcadores vêm de C[...] e, dentro da frase, PW(cena, palavra) lê o instante da palavra no tempos.json."""
import json
import math
import unicodedata
from pathlib import Path

import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Porcentagem")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-POR-014_erro_relativo.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("ideia", "pedreiro", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"

# as contas da aula, conferidas
assert 2 * 100 == 200 and 1 / 200 == 0.005 and 0.005 * 100 == 0.5 and 1 / 10 == 0.1 and 0.1 * 100 == 10
assert 10 / 0.5 == 20 and 1 / 2 == 0.5 and 10 * 10 == 100 and 2 / 100 == 0.02 and 5 * 100 == 500
assert 3 / 500 == 0.006 and abs(0.006 * 100 - 0.6) < 1e-12 and 2 > 0.6 and 120 * 0.8 == 96

_TEMPOS = json.loads((Path(__file__).resolve().parents[1] / "audio" / "tempos.json").read_text(encoding="utf-8"))


def _n(s):
    return "".join(ch for ch in unicodedata.normalize("NFD", s.lower()) if ch.isalnum())


def PW(sid, palavra, n=1):
    """instante em que a voz diz a n-ésima `palavra` da cena sid"""
    for s in _TEMPOS["scenes"]:
        if s["id"] == sid:
            k = 0
            for tk in s["tokens"]:
                if _n(tk["disp"]) == _n(palavra):
                    k += 1
                    if k == n:
                        return s["start"] + tk["t0"]
    raise KeyError((sid, palavra, n))


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças gerais ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    """uma frase, palavra a palavra, no mesmo estilo"""
    return [(w, est, size, cor) for w in txt.split()]


def cen(c, t, ti, s, x, y, size=64, cor=None, est="g"):
    E.foco(c, t, ti, 0.45, lambda a: centro(c, s, x, y, size, est, cor or TINTA, a))


def num_bola(c, s, cx, cy, r, size, a=1.0, cor=None):
    E.bola(c, cx, cy + 3, r, cor, a)
    centro(c, s, cx, cy + size * 0.36, size, "g", E.SOBRE if cor is None else M.on(cor), a)


def bolinha(c, t, t0, n, x, y, r=40):
    E.foco(c, t, t0, 0.45, lambda a: (E.bola(c, x, y, r, a=a), centro(c, str(n), x, y + r * 0.42, r * 1.15, "g", E.SOBRE, a)))


def grupo(c, cx, cy, k, fn):
    """desenha fn() escalado por k em torno de (cx, cy)"""
    c.save(); c.translate(cx, cy); c.scale(k, k); c.translate(-cx, -cy)
    fn()
    c.restore()


def fase(c, t, t0, t1, fn):
    """desenha fn de t0 até t1 e some desfocando"""
    if t0 - 0.01 <= t < t1 + 0.4:
        E.saida(c, t, t1, fn)


def vez(itens, t):
    """itens = texto fixo ou [(t0, texto), ...]; devolve [(t0, t_fim, texto)]"""
    if isinstance(itens, str):
        return [(None, 1e9, itens)]
    return [(t0, itens[i + 1][0] if i + 1 < len(itens) else 1e9, s) for i, (t0, s) in enumerate(itens)]


# ---------------- linguagem da trilha Porcentagem ----------------
def larg_cartao(valores, size):
    return max(max(E.larg(s, "g", size) for s in valores) + size * 1.0, size * 2.9)


def cartao(c, t, t0, cx, cy, valor, rotulo=None, depois=False, size=92, w=None, cor=None):
    """valor num cartão: entra em t0. valor = texto ou [(t0, texto), ...] ("?" sai cinza). depois=True: cor da matéria"""
    itens = vez(valor, t)
    w = w or larg_cartao([s for _, _, s in itens], size)
    h = size * 1.75
    tinta = cor or (COR if depois else TINTA)

    def caixa(a):
        r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2, cy - h / 2, w, h), 30, 30)
        s = skia.Paint(AntiAlias=True, Color=M.hexc("#000000", 0.10 * a))
        s.setMaskFilter(skia.MaskFilter.MakeBlur(skia.kNormal_BlurStyle, 14))
        c.save(); c.translate(6, 12); c.drawRRect(r, s); c.restore()
        c.drawRRect(r, M.paint(BR, a))
        c.drawRRect(r, M.paint(tinta, a, stroke=6))
        if rotulo:
            centro(c, rotulo, cx, cy - h / 2 - 28, 58, "i", (cor or COR) if depois else TINTA2, a)
    E.foco(c, t, t0, 0.5, caixa)
    for ti, tf, s in itens:
        ti = t0 if ti is None else ti
        cor_s = CINZA if s == "?" else tinta
        E.saida(c, t, tf - 0.05, lambda s=s, ti=ti, cor_s=cor_s: E.foco(c, t, ti, 0.45, lambda a: centro(c, s, cx, cy + size * 0.36, size, "g", cor_s, a)), d=0.25)
    return w


def maquina(c, t, t0, cx, cy, fator, size=84):
    """a máquina: a conta numa caixa cheia da cor da matéria. fator = texto ou [(t0, texto), ...]"""
    itens = vez(fator, t)
    w = max(max(E.larg(s, "g", size) for _, _, s in itens) + size * 1.2, size * 2.8)
    h = size * 1.9

    def caixa(a):
        r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2, cy - h / 2, w, h), 22, 22)
        s = skia.Paint(AntiAlias=True, Color=M.hexc("#000000", 0.22 * a))
        s.setMaskFilter(skia.MaskFilter.MakeBlur(skia.kNormal_BlurStyle, 16))
        c.save(); c.translate(8, 14); c.drawRRect(r, s); c.restore()
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeLinear([skia.Point(cx, cy - h / 2), skia.Point(cx, cy + h / 2)],
                                                   [M.hexc(E.mix(E.COR, BR, 0.18), a), M.hexc(E.mix(E.COR, "#000000", 0.25), a)]))
        c.drawRRect(r, p)
        for dx in (-1, 1):  # parafusos: é uma máquina
            c.drawCircle(cx + dx * (w / 2 - 22), cy - h / 2 + 22, 7, M.paint(E.mix(E.COR, BR, 0.45), a))
            c.drawCircle(cx + dx * (w / 2 - 22), cy + h / 2 - 22, 7, M.paint(E.mix(E.COR, BR, 0.45), a))
    E.foco(c, t, t0, 0.5, caixa)
    for ti, tf, s in itens:
        ti = t0 if ti is None else ti
        E.saida(c, t, tf - 0.05, lambda s=s, ti=ti: E.foco(c, t, ti, 0.45, lambda a: centro(c, s, cx, cy + size * 0.36, size, "g", E.SOBRE, a)), d=0.25)
    return w


XA, XM, XD = 400, 960, 1520  # antes, máquina, depois


def fluxo(c, t, y, antes, fator, depois, ta, tf, td, rot=("antes", "depois"), size=92, x=(XA, XM, XD), cor_d=None):
    """antes → [conta] → depois. ta, tf, td = instantes de cada parte (None = não desenha)"""
    xa, xm, xd = x
    wa = wd = 0
    if ta is not None:
        wa = cartao(c, t, ta, xa, y, antes, rot[0], False, size)
    if td is not None:
        wd = cartao(c, t, td, xd, y, depois, rot[1], True, size, cor=cor_d)
    if tf is not None:
        wm = maquina(c, t, tf, xm, y, fator, size * 0.9)
        p = ep(t, tf - 0.1, 0.5)
        if p > 0:
            M.arrow(c, xa + max(wa, size * 2.9) / 2 + 22, y, xm - wm / 2 - 22, y, TINTA2, p, 6, 20, p)
            M.arrow(c, xm + wm / 2 + 22, y, xd - max(wd, size * 2.9) / 2 - 22, y, TINTA2, p, 6, 20, p)


# ================= a ESCADA das unidades (a mesma peça da trilha Medidas e Unidades, MAT-MED-001) =================
UN = ("m", "dm", "cm", "mm")
NOMES = ("metro", "decímetro", "centímetro", "milímetro")


class Escada:
    """degraus descendo da esquerda para a direita. (x, y) = canto de cima do 1º degrau; sw, sh = largura e altura do degrau.
    base = onde todos os degraus apoiam. meio = índice da unidade principal (degrau cheio da cor da matéria)."""

    def __init__(s, x=110, y=300, sw=186, sh=78, base=950, un=UN, nomes=NOMES, meio=0, size=60):
        s.x, s.y, s.sw, s.sh, s.base, s.un, s.nomes, s.meio, s.size = x, y, sw, sh, base, un, nomes, meio, size
        s.n = len(un)

    def cx(s, i):
        return s.x + (i + 0.5) * s.sw

    def topo(s, i):
        return s.y + i * s.sh

    def ponto(s, i):
        k = min(max(i, 0), s.n - 1)
        return s.cx(k), s.y + k * s.sh - 34

    def degraus(s, c, t, td, tl=None, a=1.0, acesos=(), ta=None, escuro=False, nomes=True):
        if a <= 0:
            return
        for i in range(s.n):
            ti = td[i] if isinstance(td, (list, tuple)) else td + 0.09 * i
            q = ep(t, ti, 0.45)
            if q <= 0:
                continue
            top, x0 = s.topo(i), s.x + i * s.sw
            hh = (s.base - top) * ease_io(prog(t, ti, 0.45))
            meio = i == s.meio
            fundo, borda, tinta = (E.COR, E.COR, E.SOBRE) if meio else ("#FFFFFF", TINTA2, TINTA)
            acende = ep(t, ta, 0.4) if (i in acesos and ta is not None and not meio) else 0.0
            M.rrect(c, x0 + 4, s.base - hh, s.sw - 8, hh, 12, fundo, q * a)
            if acende > 0:
                M.rrect(c, x0 + 4, s.base - hh, s.sw - 8, hh, 12, E.COR, 0.16 * acende * q * a)
            c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x0 + 4, s.base - hh, s.sw - 8, hh), 12, 12), M.paint(borda, q * a, stroke=3))
            tli = tl[i] if tl else ti + 0.2
            E.foco(c, t, tli, 0.45, lambda b, i=i, top=top, tinta=tinta: centro(c, s.un[i], s.cx(i), top + s.size * 1.12, s.size, "g", tinta, b * a))
            if nomes:
                cor_n = E.SOBRE if meio else TINTA2
                E.foco(c, t, tli + 0.1, 0.45, lambda b, i=i, top=top, cor_n=cor_n: centro(c, s.nomes[i], s.cx(i), top + s.size * 1.12 + 50, 40, "i", cor_n, b * a))

    def pulos(s, c, t, i0, hops, t0, a=1.0, cor=None, dur=0.7, rastro=True):
        if a <= 0 or t < t0:
            return
        cor = cor or E.COR
        atual, pulo = float(i0), 0.0
        de = i0
        for k, (th, j) in enumerate(hops):
            q = prog(t, th, dur)
            if q <= 0:
                break
            if rastro:
                s._arco(c, de, j, min(1.0, q * 1.25), k + 1, cor, a)
            if q < 1:
                e = ease_io(q)
                atual, pulo = lerp(de, j, e), math.sin(math.pi * q) * 70
                break
            atual, de = float(j), j
        x0, y0 = s.ponto(math.floor(atual))
        x1, y1 = s.ponto(math.ceil(atual))
        f = atual - math.floor(atual)
        E.bola(c, lerp(x0, x1, f), lerp(y0, y1, f) - pulo, 30 * ease_back(prog(t, t0, 0.5)), cor, a)

    def _arco(s, c, i, j, p, k, cor, a):
        (xa, ya), (xb, yb) = s.ponto(i), s.ponto(j)
        ya, yb = ya - 36, yb - 36
        mx, my = (xa + xb) / 2, min(ya, yb) - 64
        pts = [(lerp(lerp(xa, mx, u), lerp(mx, xb, u), u), lerp(lerp(ya, my, u), lerp(my, yb, u), u)) for u in [p * n / 24 for n in range(25)]]
        path = skia.Path()
        path.moveTo(*pts[0])
        for x_, y_ in pts[1:]:
            path.lineTo(x_, y_)
        c.drawPath(path, M.paint(cor, 0.75 * a, stroke=5, cap_round=True))
        if p >= 1:
            (xp, yp), (xe, ye) = pts[-2], pts[-1]
            ang = math.atan2(ye - yp, xe - xp)
            h = skia.Path()
            h.moveTo(xe + math.cos(ang) * 3, ye + math.sin(ang) * 3)
            h.lineTo(xe - 18 * math.cos(ang - 0.5), ye - 18 * math.sin(ang - 0.5))
            h.lineTo(xe - 18 * math.cos(ang + 0.5), ye - 18 * math.sin(ang + 0.5))
            h.close()
            c.drawPath(h, M.paint(cor, 0.75 * a))
            xm, ym = pts[12]
            c.drawCircle(xm, ym - 4, 24, M.paint(cor, a))
            centro(c, str(k), xm, ym + 11, 32, "g", E.SOBRE, a)


def posicao(t, pos, saltos, dur=0.7):
    """posição da vírgula no instante t (a mesma conta de E.anda)"""
    atual, fim = float(pos), pos
    for t0, novo in saltos:
        q = ease_io(prog(t, t0, dur))
        if q <= 0:
            break
        if q >= 1:
            atual, fim = float(novo), novo
            continue
        return lerp(fim, novo, q)
    return atual


def num_un(c, t, dig, pos, saltos, x, y, size, unidades, cor=None, tv=None, some=False, t0=None, cor_un=None):
    """número com a vírgula que anda (E.anda) e a unidade logo depois dele, que troca a cada salto (MAT-MED-001)"""
    if t0 is not None and t < t0:
        return None
    a0 = ep(t, t0, 0.5) if t0 is not None else 1.0
    c.saveLayer(None, M.paint("#000000", a0)) if a0 < 1 else None
    px = E.anda(c, t, dig, pos, saltos, x, y, size, cor=cor, tv=tv, some=some)
    cl = E.casa(size)
    ncas = max(len(dig), math.ceil(posicao(t, pos, saltos) - 1e-6))
    xu = x + ncas * cl + size * 0.3
    for k, (tu, u) in enumerate(unidades):
        prox = unidades[k + 1][0] if k + 1 < len(unidades) else None
        if t < tu:
            break
        if prox is not None and t >= prox + 0.35:
            continue
        sai = 1 - ep(t, prox, 0.35) if prox is not None else 1.0
        E.foco(c, t, tu, 0.4, lambda b, u=u: E.escreve(c, u, xu, y, size * 0.72, "g", cor_un or COR, b * sai))
    if a0 < 1:
        c.restore()
    return px


# ---------------- peças desta aula ----------------
def anda_z(c, t, dig, pos, saltos, x, y, size, n0=None, a=1.0, cor=None, some=False):
    """a vírgula anda (como E.anda) e, no fim, os zeros da frente que sobraram somem e o número encosta: 0,005 → 0,5.
    dig = algarismos ("0005" é 0,005; "010" é 0,1 com o zero que vai entrar); n0 = quantos já estão na tela (o resto
    entra quando a vírgula passa). some = a vírgula some (resultado inteiro). Devolve o x da borda direita do número."""
    if a <= 0:
        return x
    cor = cor or TINTA
    cl = E.casa(size)
    n0 = n0 or len(dig)
    atual = posicao(t, pos, saltos)
    pulo = 0.0
    for t0, _ in saltos:
        q = prog(t, t0, 0.7)
        if 0 < q < 1:
            pulo = math.sin(q * math.pi) * size * 0.95
    fim, tf = saltos[-1][1], saltos[-1][0] + 0.7
    nz = 0
    for i in range(fim - 1):
        if dig[i] != "0":
            break
        nz += 1
    z = ep(t, tf - 0.15, 0.35)
    xx = x - ease_io(prog(t, tf + 0.05, 0.4)) * nz * cl
    for i, ch in enumerate(dig):
        al = a
        if i >= n0:
            k = next((t0 for t0, nv in saltos if nv >= i + 1), None)
            al *= ep(t, k + 0.55, 0.4) if k is not None else 0
        if i < nz:
            al *= 1 - z
        if al > 0:
            E._digito(c, ch, xx + (i + 0.5) * cl, y, size, "g", cor, al)
    vis = a * (1 - ep(t, tf + 0.2, 0.3)) if some else a
    E._virgula(c, xx + atual * cl, y - pulo, size, COR, vis)
    return xx + max(n0, math.ceil(atual - 1e-6)) * cl


def conta_pct(c, t, ti, ta, saltos, tp, txt, dig, pos, x, y, size, n0=None, some=False, cor=None):
    """"1 ÷ 200 =" (em ti) seguido do decimal (em ta) que anda a vírgula e ganha o "%" (em tp). x = início da linha"""
    E.foco(c, t, ti, 0.45, lambda a: E.escreve(c, txt, x, y, size, "g", TINTA, a))
    xn = x + E.larg(txt, "g", size) + size * 0.35
    q = ep(t, ta, 0.45)
    if q <= 0:
        return
    xe = anda_z(c, t, dig, pos, saltos, xn, y, size, n0=n0, a=q, some=some)
    E.foco(c, t, tp, 0.45, lambda a: E.escreve(c, "%", xe + 6, y, size, "g", cor or COR, a))


def frac_pal(c, t, tn, td, num, den, cx, cy, size, cor=None, a=1.0):
    """fração de palavras: o de cima entra em tn, o de baixo em td; a barra vem com o de cima"""
    cor = cor or TINTA
    w = max(E.larg(num, "g", size), E.larg(den, "g", size)) + size * 0.5
    E.foco(c, t, tn, 0.45, lambda b: (centro(c, num, cx, cy - size * 0.36, size, "g", cor, a * b),
                                      M.line(c, cx - w / 2, cy, cx + w / 2, cy, cor, a * b, size * 0.09)))
    E.foco(c, t, td, 0.45, lambda b: centro(c, den, cx, cy + size * 1.02, size, "g", cor, a * b))


def parede(c, x, y, w, h, a=1.0, fiadas=5):
    """parede de tijolos vista de frente"""
    if a <= 0:
        return
    M.rrect(c, x, y, w, h, 6, "#E7DDCC", a)
    bh = h / fiadas
    bw = bh * 2.3
    junta = "#B9AB93"
    for r in range(1, fiadas):
        M.line(c, x, y + r * bh, x + w, y + r * bh, junta, a, 3)
    for r in range(fiadas):
        xx = x + (bw if r % 2 == 0 else bw / 2)
        while xx < x + w - 8:
            M.line(c, xx, y + r * bh, xx, y + (r + 1) * bh, junta, a, 3)
            xx += bw
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 6, 6), M.paint(TINTA, a, stroke=4))


def engrenagem(c, cx, cy, r, a=1.0, dentes=12, cor=None):
    """peça de relógio: engrenagem com furo no meio"""
    if a <= 0:
        return
    p = skia.Path()
    n = dentes * 4
    ri = r * 0.8
    for k in range(n + 1):
        ang = 2 * math.pi * (k - 0.5) / n
        rr = r if (k % 4) in (1, 2) else ri
        px, py = cx + rr * math.cos(ang), cy + rr * math.sin(ang)
        p.moveTo(px, py) if k == 0 else p.lineTo(px, py)
    p.close()
    c.drawPath(p, M.paint(cor or E.mix(E.COR, "#FFFFFF", 0.72), a))
    pt = M.paint(TINTA, a, stroke=4)
    pt.setStrokeJoin(skia.Paint.kRound_Join)
    c.drawPath(p, pt)
    c.drawCircle(cx, cy, r * 0.5, M.paint(TINTA2, 0.5 * a, stroke=3))
    c.drawCircle(cx, cy, r * 0.17, M.paint(E.PAPEL, a))
    c.drawCircle(cx, cy, r * 0.17, M.paint(TINTA, a, stroke=4))


def cota(c, t, t0, x0, x1, y, rot, size=60, cor=None):
    """linha de cota com tracinhos nas pontas e a medida embaixo"""
    p = ease_io(prog(t, t0, 0.5))
    if p <= 0:
        return
    cor = cor or TINTA
    xm = (x0 + x1) / 2
    M.line(c, lerp(xm, x0, p), y, lerp(xm, x1, p), y, cor, 1.0, 4)
    for xx in (lerp(xm, x0, p), lerp(xm, x1, p)):
        M.line(c, xx, y - 16, xx, y + 16, cor, 1.0, 4)
    E.foco(c, t, t0 + 0.2, 0.4, lambda a: centro(c, rot, xm, y + size + 14, size, "g", cor, a))


def _fatia(cx, cy, r, a0, varre):
    p = skia.Path()
    p.moveTo(cx, cy)
    p.arcTo(skia.Rect.MakeXYWH(cx - r, cy - r, 2 * r, 2 * r), a0, varre, False)
    p.close()
    return p


def pizza(c, cx, cy, r, n, pint=0, a=1.0, sai=0.0, cor=None, lw=3):
    """pizza de n fatias iguais no palco escuro (a peça de MAT-POR-001); a primeira fatia fica na cor e sai `sai` px"""
    if a <= 0 or r <= 0:
        return
    cor = cor or CLARO
    c.drawCircle(cx, cy, r, M.paint("#FFFFFF", a * 0.08))
    passo_ = 360 / n
    for i in range(n):
        ang = math.radians(-90 + i * passo_)
        M.line(c, cx, cy, cx + r * math.cos(ang), cy + r * math.sin(ang), CLARO, a * 0.45, lw)
    c.drawCircle(cx, cy, r, M.paint(CLARO, a, stroke=4))
    for i in range(min(int(pint), n)):
        a0 = -90 + i * passo_
        meio = math.radians(a0 + passo_ / 2)
        p = _fatia(cx + sai * math.cos(meio), cy + sai * math.sin(meio), r, a0, passo_)
        c.drawPath(p, M.paint(cor, a))
        if n <= 50:
            c.drawPath(p, M.paint("#07070F", a, stroke=3))


ESC = Escada(x=110, y=330, sw=212, sh=120, base=930, size=64)
ESC2 = Escada(x=100, y=330, sw=165, sh=88, base=700, size=54)


# ---------------- gancho ----------------
XP, XR = 480, 1440  # coluna do pedreiro e do relojoeiro


def b_gancho(c, t, C, b):
    ka, kb, kc = C["s01.a"], C["s01.b"], C["s01.c"]

    def um():
        # pedreiro
        cen(c, t, PW("s01", "pedreiro"), "pedreiro", XP, 160, 64, TINTA2, "i")
        E.foco(c, t, PW("s01", "parede"), 0.5, lambda a: parede(c, XP - 230, 210, 460, 210, a))
        cota(c, t, PW("s01", "dois"), XP - 230, XP + 230, 460, "2 m")
        E.foco(c, t, ka, 0.45, lambda a: E.pilula(c, "erro: 1 cm", XP, 640, 58, "g", fundo=TINTA, a=a))
        # relojoeiro
        cen(c, t, PW("s01", "relojoeiro"), "relojoeiro", XR, 160, 64, TINTA2, "i")
        E.foco(c, t, PW("s01", "peça"), 0.5, lambda a: engrenagem(c, XR, 318, 110, a))
        cota(c, t, PW("s01", "centímetro", 2), XR - 110, XR + 110, 460, "1 cm")
        E.foco(c, t, kb, 0.45, lambda a: E.pilula(c, "erro: 1 mm", XR, 640, 58, "g", fundo=TINTA, a=a))
        # 1 cm é 10 vezes 1 mm: a balança pende para o centímetro... e vira
        td = PW("s01", "dez")
        E.frase(c, t, td - 0.4, [("1 cm", "g", 64), ("=", "g", 64, TINTA2), ("10 mm", "g", 64)], W / 2, 330, "center", 0.15)
        inc = lerp(-0.75, 1.0, ease_io(prog(t, kc, 0.9)))
        E.foco(c, t, td, 0.5, lambda a: grupo(c, W / 2, 860, 0.58, lambda: E.balanca(c, W / 2, 860, "1 cm", "1 mm", inc, a, 100)))
        q = ep(t, kc + 0.5, 0.5)
        if q > 0:
            E.caixa_pontilhada(c, XR - 225, 100, 450, 610, q, COR, prog_=q)
            E.pilula(c, "pesa mais", XR + 60, 880, 74, "g", a=q)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t >= C["s02"]:
        ta, tb = C["s02.a"], C["s02.b"]
        E.foco(c, t, tb - 0.2, 0.7, lambda a: E.bola(c, 1500, 540, 250 * ease_back(prog(t, tb - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, ps("até o fim desta aula", "i", 90), XE, 330, passo=0.14)
        E.frase(c, t, PW("s02", "medir"), ps("medir o", "i", 90) + [("peso de um erro", "g", 100, COR)], XE, 500, passo=0.12)
        E.frase(c, t, PW("s02", "em"), [("em %", "g", 100)], XE, 670)
        E.foco(c, t, tb + 0.1, 0.5, lambda a: (centro(c, "+ atalho", 1500, 525, 80, "g", E.SOBRE, a),
                                               centro(c, "de prova", 1500, 610, 80, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    a3, b3, c3 = C["s03.a"], C["s03.b"], C["s03.c"]
    E.frase(c, t, C["s03"] + 0.3, ps("você precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, a3, 0.5, lambda a: E.escreve(c, "2", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, a3 + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 210, 700, 120, "i", TINTA, a))
    x, w = 900, 880
    p = ep(t, b3, 0.5)
    E.caixa_pontilhada(c, x, 200, w, 300, p, prog_=p)
    bolinha(c, t, b3, 1, x + 60, 270, 34)
    E.frase(c, t, b3 + 0.1, [("converter", "i", 66), ("m, cm e mm", "g", 66, COR)], x + 120, 292)
    E.frase(c, t, PW("s03", "degrau"), ps("cada degrau da escada:", "i", 54, TINTA2) + [("× 10", "g", 58, COR)], x + 120, 390, "left", 0.1)
    E.frase(c, t, PW("s03", "degrau") + 0.6, [("m → dm → cm → mm", "g", 50, TINTA2)], x + 120, 460)
    E.cursor(c, x + w - 30, 470, ep(t, b3, 0.4))
    p2 = ep(t, c3, 0.5)
    E.caixa_pontilhada(c, x, 550, w, 200, p2, prog_=p2)
    bolinha(c, t, c3, 2, x + 60, 620, 34)
    E.frase(c, t, c3 + 0.1, [("calcular a", "i", 66), ("variação %", "g", 66, COR)], x + 120, 642)
    E.frase(c, t, PW("s03", "percentual"), [("diferença ÷ valor de antes", "g", 50, TINTA2)], x + 120, 715)
    E.frase(c, t, PW("s03", "Se"), ps("faltou?", "i", 58, COR) + ps("procure no canal", "i", 58), x, 850, "left", 0.12)


# ---------------- absoluto e relativo ----------------
def b_ideia(c, t, C, b):
    a4, b4, c4 = C["s04.a"], C["s04.b"], C["s04.c"]

    def quatro():
        E.linha(c, t, [("quanto um erro pesa", "i", 66, TINTA, C["s04"] + 0.3), ("depende do", "i", 66, TINTA, PW("s04", "depende")),
                       ("tamanho do que você mede", "g", 70, COR, a4)], W / 2, 170, "center")
        # a parede: 1 cm em 2 m mal aparece (2 m = 600 px, então 1 cm = 3 px)
        x0, y0, w, h = 190, 330, 600, 300
        t1 = PW("s04", "Um", 2)
        E.foco(c, t, t1 - 0.6, 0.5, lambda a: parede(c, x0, y0, w, h, a, 6))
        cota(c, t, t1 - 0.4, x0, x0 + w, y0 + h + 50, "2 m", 56)
        q = ep(t, t1, 0.4)
        if q > 0:
            M.rrect(c, x0 + w, y0, 3, h, 0, ERRADO, q)
            M.arrow(c, x0 + w + 120, y0 - 60, x0 + w + 12, y0 + 20, ERRADO, q, 5, 18)
            centro(c, "+1 cm", x0 + w + 130, y0 - 80, 56, "g", ERRADO, q)
        E.foco(c, t, b4, 0.45, lambda a: E.pilula(c, "quase não se nota", x0 + w / 2, 900, 58, "g", fundo=TINTA, a=a))
        # a peça: 1 mm em 1 cm (1 cm = 300 px, então 1 mm = 30 px)
        cx, cy, r = 1420, 480, 150
        t2 = PW("s04", "Um", 3)
        E.foco(c, t, t2 - 0.6, 0.5, lambda a: engrenagem(c, cx, cy, r, a))
        cota(c, t, t2 - 0.4, cx - r, cx + r, y0 + h + 50, "1 cm", 56)
        q2 = ep(t, t2, 0.4)
        if q2 > 0:
            pt = M.paint(ERRADO, q2, stroke=6)
            pt.setPathEffect(skia.DashPathEffect.Make([16, 12], 0))
            c.drawCircle(cx, cy, r + 30 * ease_io(q2), pt)
            centro(c, "+1 mm", cx + r + 110, cy - r - 10, 56, "g", ERRADO, q2)
        E.foco(c, t, c4, 0.45, lambda a: E.pilula(c, "estraga a peça", cx, 900, 58, "g", fundo=ERRADO, a=a))
    E.saida(c, t, C["s05"] - 0.1, quatro)

    a5, b5, c5, d5 = C["s05.a"], C["s05.b"], C["s05.c"], C["s05.d"]

    def cinco():
        E.frase(c, t, C["s05"] + 0.3, ps("dois jeitos de olhar um erro", "i", 70), W / 2, 160, "center", 0.1)
        xl, xr = 500, 1420
        cen(c, t, a5, "erro absoluto", xl, 320, 84, TINTA)
        cen(c, t, PW("s05", "tamanho"), "o tamanho do erro", xl, 400, 56, TINTA2, "i")
        tu = PW("s05", "unidade")
        cen(c, t, tu, "1 cm", xl - 190, 600, 104, TINTA)
        cen(c, t, tu + 0.25, "1 mm", xl + 190, 600, 104, TINTA)
        cen(c, t, b5, "erro relativo", xr, 320, 84, COR)
        cen(c, t, PW("s05", "compara"), "compara com a medida", xr, 400, 56, TINTA2, "i")
        frac_pal(c, t, c5, PW("s05", "medida", 3), "erro", "medida", xr, 560, 96, COR)
        tc = PW("s05", "Com", 2)
        E.linha(c, t, [("cm ÷ cm", "g", 76, TINTA, tc), ("→", "g", 76, TINTA2, d5), ("sem unidade", "g", 76, COR, d5 + 0.2)], W / 2, 860, "center")
        E.foco(c, t, PW("s05", "só"), 0.45, lambda a: E.pilula(c, "só um número", W / 2, 970, 54, "g", a=a))
    if C["s05"] - 0.1 <= t:
        E.saida(c, t, C["s06"] - 0.1, cinco)

    if t < C["s06"]:
        return
    a6, b6, c6 = C["s06.a"], C["s06.b"], C["s06.c"]
    E.frase(c, t, C["s06"] + 0.2, ps("a mesma conta da", "i", 76) + [("variação %", "g", 80, COR)], W / 2, 200, "center", 0.12)
    frac_pal(c, t, a6, PW("s06", "referência"), "diferença", "referência", 560, 520, 96, TINTA)
    q = ep(t, b6 - 0.2, 0.5)
    if q > 0:
        M.arrow(c, 860, 540, 1060, 540, TINTA2, q, 6, 20, q)
    frac_pal(c, t, b6, c6, "erro", "medida", 1360, 520, 120, COR)
    E.foco(c, t, c6 + 0.4, 0.45, lambda a: E.pilula(c, "erro relativo", 1360, 880, 64, "g", a=a))


# ---------------- pedreiro ----------------
def b_pedreiro(c, t, C, b):
    a7, b7, c7 = C["s07.a"], C["s07.b"], C["s07.c"]
    h1, h2 = PW("s07", "dois"), PW("s07", "dois") + 0.7

    def sete():
        E.frase(c, t, C["s07"] + 0.2, [("pedreiro:", "g", 70, COR), ("1 cm em 2 m", "g", 70)], XE, 170, "left", 0.12)
        ESC.degraus(c, t, PW("s07", "escada"), acesos=(1, 2), ta=h1)
        ESC.pulos(c, t, 0, [(h1, 1), (h2, 2)], PW("s07", "metro", 2))
        E.frase(c, t, a7, ps("antes de dividir:", "i", 54) + [("mesma unidade", "g", 58, COR)], 1030, 300, "left", 0.1)
        num_un(c, t, "2", 1, [(h1, 2), (h2, 3)], 1120, 540, 150, [(PW("s07", "metro", 2), "m"), (h1 + 0.7, "dm"), (h2 + 0.7, "cm")],
               tv=h1 - 0.3, some=True, t0=PW("s07", "metro", 2))
        E.foco(c, t, PW("s07", "degraus"), 0.45, lambda a: E.pilula(c, "2 degraus", 1250, 700, 56, "g", fundo=TINTA, a=a))
        E.foco(c, t, b7, 0.45, lambda a: E.pilula(c, "× 100", 1560, 700, 56, "g", a=a))
        E.foco(c, t, c7, 0.5, lambda a: num_bola(c, "200 cm", 1450, 870, 150, 66, a))
    E.saida(c, t, C["s08"] - 0.1, sete)
    if t < C["s08"]:
        return
    a8, b8, c8 = C["s08.a"], C["s08.b"], C["s08.c"]
    fluxo(c, t, 300, "1 cm", [(C["s08"], "?"), (a8, "÷ 200 cm")], [(C["s08"], "?"), (b8, "0,5%")], C["s08"], C["s08"], C["s08"],
          rot=("erro", "erro relativo"), size=84)
    hz = PW("s08", "duas")
    conta_pct(c, t, a8, PW("s08", "zero"), [(hz, 2), (hz + 0.7, 3)], b8, "1 ÷ 200 =", "0005", 1, 330, 640, 120)
    E.foco(c, t, PW("s08", "Ande"), 0.45, lambda a: E.pilula(c, "vírgula: 2 casas →", 600, 830, 56, "g", fundo=TINTA, a=a))
    E.foco(c, t, c8, 0.45, lambda a: E.pilula(c, "menos de 1% da parede", 1360, 830, 56, "g", a=a))


# ---------------- relojoeiro ----------------
def b_relojoeiro(c, t, C, b):
    a9, b9, c9 = C["s09.a"], C["s09.b"], C["s09.c"]
    hop = PW("s09", "tem")

    def nove():
        E.frase(c, t, C["s09"] + 0.2, [("relojoeiro:", "g", 70, COR), ("1 mm em 1 cm", "g", 70)], XE, 170, "left", 0.12)
        ESC2.degraus(c, t, PW("s09", "De"), acesos=(3,), ta=PW("s09", "degrau"), nomes=False)
        ESC2.pulos(c, t, 2, [(hop, 3)], PW("s09", "centímetro"))
        num_un(c, t, "1", 1, [(hop, 2)], 860, 470, 140, [(a9, "cm"), (hop + 0.7, "mm")], tv=hop - 0.3, some=True, t0=a9)
        E.foco(c, t, PW("s09", "degrau"), 0.45, lambda a: E.pilula(c, "1 degrau: × 10", 1120, 600, 56, "g", a=a))
        conta_pct(c, t, b9, PW("s09", "zero"), [(PW("s09", "Andando"), 2), (PW("s09", "Andando") + 0.7, 3)], c9, "1 ÷ 10 =", "010", 1,
                  520, 860, 120, n0=2, some=True)
    E.saida(c, t, C["s10"] - 0.1, nove)
    if t < C["s10"]:
        return
    a0, b0, c0, d0, e0 = (C[f"s10.{k}"] for k in "abcde")
    y = 330
    cartao(c, t, a0, 560, y, "10%", "relojoeiro", True, 110)
    cartao(c, t, b0, 1360, y, "0,5%", "pedreiro", False, 110)
    E.foco(c, t, c0, 0.5, lambda a: num_bola(c, "20 ×", W / 2, y, 90, 70, a))
    E.foco(c, t, c0 + 0.5, 0.45, lambda a: centro(c, "pesa 20 vezes mais", 560, y + 170, 50, "i", COR, a))
    tm = PW("s10", "menor")
    cen(c, t, tm, "erro de 1 mm", 560, y + 245, 54, TINTA2, "g")
    cen(c, t, tm + 0.2, "erro de 1 cm", 1360, y + 245, 54, TINTA2, "g")
    E.foco(c, t, tm + 0.4, 0.45, lambda a: centro(c, "(o menor)", 560, y + 305, 46, "i", TINTA2, a))
    E.frase(c, t, d0 - 0.3, ps("em prova:", "i", 76) + [("precisão", "g", 96, COR)], W / 2, 790, "center", 0.12)
    E.frase(c, t, e0 - 0.6, ps("menor erro relativo", "i", 64) + [("→", "g", 64, TINTA2), ("mais precisa", "g", 68, COR)], W / 2, 930, "center", 0.12)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    a, b_, c_, d, e = (C[f"s11.{k}"] for k in "abcde")
    E.frase(c, t, a - 0.6, [("o erro:", "g", 84, ERRADO)] + ps("dividir sem", "i", 84) + [("converter", "g", 84)], W / 2, 170, "center", 0.12)
    xl = 600
    xs = E.linha(c, t, [("1 cm", "g", 110, TINTA, b_), ("e", "i", 90, TINTA2, b_ + 0.4), ("2 m", "g", 110, TINTA, PW("s11", "dois"))], xl, 390, "center")
    E.linha(c, t, [("1 ÷ 2", "g", 110, ERRADO, PW("s11", "faz")), ("=", "g", 110, TINTA2, c_ - 0.3), ("50%", "g", 110, ERRADO, c_)], xl, 590, "center")
    if t >= d:
        E.risco(c, xl - 300, 610, xl + 300, 510, t, d, largura=12)
        q = ep(t, d, 0.4)
        for x_, s_, u_ in ((xs[0], "1 cm", "cm"), (xs[2], "2 m", "m")):
            xc, wu = x_ + E.larg(s_, "g", 110) - E.larg(u_, "g", 110) / 2, E.larg(u_, "g", 110)
            c.drawOval(skia.Rect.MakeXYWH(xc - wu / 2 - 22, 290, wu + 44, 130), M.paint(ERRADO, q, stroke=5))
        E.foco(c, t, d + 0.3, 0.45, lambda a: E.pilula(c, "unidades diferentes", xl, 730, 56, "g", fundo=ERRADO, a=a))
    # meia parede
    px, py, pw, ph = 1200, 300, 560, 300
    E.foco(c, t, PW("s11", "Seria") - 0.2, 0.5, lambda q: parede(c, px, py, pw, ph, q, 6))
    q = ep(t, PW("s11", "meia"), 0.5)
    if q > 0:
        M.rrect(c, px + pw / 2, py, pw / 2 * ease_io(q), ph, 4, ERRADO, 0.55 * q)
        centro(c, "meia parede?", px + pw / 2, py + ph + 80, 60, "g", ERRADO, q)
    E.frase(c, t, PW("s11", "razão") - 0.3, ps("como na razão:", "i", 60, TINTA2), XE, 900)
    bolinha(c, t, e, 1, 700, 880, 38)
    E.frase(c, t, e + 0.1, [("converta", "g", 70, COR)], 760, 904)
    bolinha(c, t, PW("s11", "Só"), 2, 1200, 880, 38)
    E.frase(c, t, PW("s11", "divida"), [("divida", "g", 70)], 1260, 904)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    a2, b2, c2, d2 = C["s12.a"], C["s12.b"], C["s12.c"], C["s12.d"]

    def doze():
        E.frase(c, t, PW("s12", "atalho") - 0.1, ps("o atalho:", "i", 80, CLARO) + [("mesmo número em cima", "g", 80, BR)], W / 2, 180, "center", 0.12)
        E.frase(c, t, PW("s12", "olhe"), ps("olhe só", "i", 70, CLARO) + [("embaixo", "g", 74, BR)], W / 2, 290, "center", 0.12)
        y, s = 520, 170
        E.foco(c, t, b2, 0.5, lambda a: E.fracao(c, 1, 200, 620, y, s, BR, a))
        E.foco(c, t, c2, 0.5, lambda a: E.fracao(c, 1, 10, 1300, y, s, BR, a))
        q = ep(t, d2, 0.45)
        if q > 0:
            E.caixa_pontilhada(c, 1300 - 150, y + 20, 300, 200, q, CLARO, prog_=q)
            centro(c, "menor embaixo", 1300, y + 290, 52, "g", CLARO, q)
        E.foco(c, t, PW("s12", "maior"), 0.45, lambda a: centro(c, "<", 960, y + 40, 150, "g", CLARO, a))
        E.foco(c, t, PW("s12", "pesa"), 0.45, lambda a: E.pilula(c, "1/10 pesa mais", 1300, 935, 60, "g", fundo=CLARO, cor="#07070F", a=a))
        E.foco(c, t, PW("s12", "sem"), 0.45, lambda a: centro(c, "sem fazer conta", 620, 955, 60, "i", CLARO, a))
    E.saida(c, t, C["s13"] - 0.1, doze)
    if t < C["s13"]:
        return
    a3, b3, c3 = C["s13.a"], C["s13.b"], C["s13.c"]

    def pizzas():
        E.frase(c, t, C["s13"] + 0.2, ps("como repartir uma", "i", 76, CLARO) + [("pizza", "g", 80, BR)], W / 2, 170, "center", 0.12)
        y, r = 560, 230
        E.foco(c, t, a3, 0.6, lambda q: pizza(c, 560, y, r, 10, 1, q, 26 * ease_back(prog(t, a3 + 0.5, 0.5))))
        cen(c, t, a3 + 0.3, "cortada em 10", 560, y + r + 90, 58, CLARO, "i")
        td = PW("s13", "duzentos")
        E.foco(c, t, td - 0.4, 0.6, lambda q: pizza(c, 1360, y, r, 200, 1, q, 26 * ease_back(prog(t, td + 0.2, 0.5)), lw=1.2))
        cen(c, t, td - 0.1, "cortada em 200", 1360, y + r + 90, 58, CLARO, "i")
        E.foco(c, t, PW("s13", "fatia"), 0.45, lambda a: E.pilula(c, "fatia bem maior", 560, y + r + 175, 54, "g", fundo=CLARO, cor="#07070F", a=a))
    E.saida(c, t, b3 - 0.1, pizzas)
    if t < b3 - 0.1:
        return
    E.frase(c, t, b3 - 0.1, ps("não compensa: números de", "i", 70, CLARO) + [("cima diferentes", "g", 74, BR)], W / 2, 200, "center", 0.12)
    y, s = 540, 160
    E.foco(c, t, PW("s13", "quatro"), 0.5, lambda a: E.fracao(c, 4, 200, 620, y, s, BR, a))
    E.foco(c, t, PW("s13", "contra"), 0.45, lambda a: centro(c, "contra", 960, y + 20, 64, "i", CLARO, a))
    E.foco(c, t, PW("s13", "três"), 0.5, lambda a: E.fracao(c, 3, 100, 1300, y, s, BR, a))
    E.foco(c, t, c3 - 0.2, 0.5, lambda a: E.pilula(c, "calcule cada %", W / 2, 920, 70, "g", fundo=CLARO, cor="#07070F", a=a))


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    a4, b4, c4 = C["s14.a"], C["s14.b"], C["s14.c"]
    E.frase(c, t, C["s14"] + 0.3, ps("hora de testar", "i", 72, COR), XE, 140)
    fluxo(c, t, 330, "2 mm", [(PW("s14", "dez"), "÷ 10 cm")], [(c4, "?%")], a4, PW("s14", "dez"), c4, rot=("erro do marceneiro", "em %"), size=80)
    fluxo(c, t, 610, "3 cm", [(PW("s14", "cinco"), "÷ 5 m")], [(c4, "?%")], b4, PW("s14", "cinco"), c4, rot=("erro do pedreiro", "em %"), size=80)
    E.saida(c, t, C["s15"] - 0.1, lambda: E.frase(c, t, c4, [("qual erro", "i", 84), ("pesa mais?", "g", 90, COR)], W / 2, 900, "center", 0.12))
    if t >= C["s15"]:
        E.relogio(c, t, C["s15.a"], W / 2, 830, 95)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    a6, b6, c6 = C["s16.a"], C["s16.b"], C["s16.c"]
    a7, b7, c7, d7, e7 = (C[f"s17.{k}"] for k in "abcde")
    t0 = C["s16"]
    xl, xr = 500, 1420
    # marceneiro
    cen(c, t, t0, "marceneiro", xl, 150, 66, COR, "i")
    cen(c, t, t0 + 0.2, "2 mm em 10 cm", xl, 260, 64, TINTA)
    E.linha(c, t, [("10 cm", "g", 76, TINTA, a6), ("=", "g", 76, TINTA2, PW("s16", "são")), ("100 mm", "g", 76, COR, PW("s16", "cem"))], xl, 410, "center")
    hz = PW("s16", "zero") + 0.6
    conta_pct(c, t, b6, PW("s16", "zero"), [(hz, 2), (hz + 0.7, 3)], c6, "2 ÷ 100 =", "002", 1, xl - 310, 570, 80, some=True)
    cartao(c, t, t0 + 0.3, xl, 780, [(t0 + 0.3, "?"), (c6, "2%")], "erro relativo", True, 80)
    # pedreiro
    cen(c, t, t0 + 0.4, "pedreiro", xr, 150, 66, COR, "i")
    cen(c, t, t0 + 0.6, "3 cm em 5 m", xr, 260, 64, TINTA)
    E.linha(c, t, [("5 m", "g", 76, TINTA, a7), ("=", "g", 76, TINTA2, PW("s17", "são")), ("500 cm", "g", 76, COR, PW("s17", "quinhentos"))], xr, 410, "center")
    hz2 = PW("s17", "que") - 0.8
    conta_pct(c, t, b7, PW("s17", "zero"), [(hz2, 2), (hz2 + 0.7, 3)], c7, "3 ÷ 500 =", "0006", 1, xr - 400, 570, 80)
    cartao(c, t, t0 + 0.7, xr, 780, [(t0 + 0.7, "?"), (c7, "0,6%")], "erro relativo", True, 80)
    # quem pesa mais
    q = ep(t, d7, 0.5)
    if q > 0:
        E.caixa_pontilhada(c, xl - 200, 610, 400, 255, q, CERTO, prog_=q)
        E.foco(c, t, d7, 0.45, lambda a: E.pilula(c, "pesa mais", xl, 930, 64, "g", fundo=CERTO, a=a))
        E.foco(c, t, d7 + 0.3, 0.45, lambda a: centro(c, ">", W / 2 - 20, 820, 110, "g", TINTA2, a))
    E.linha(c, t, [("só pelo tamanho", "i", 54, TINTA2, e7 - 0.4), ("(3 cm > 2 mm)", "g", 52, TINTA2, PW("s17", "três", 2))], xr, 905, "center")
    E.linha(c, t, [("escolheria o", "i", 58, TINTA, e7), ("pedreiro", "g", 62, ERRADO, PW("s17", "pedreiro", 2))], xr - 40, 990, "center")
    te = PW("s17", "erraria")
    E.foco(c, t, te, 0.45, lambda a: E.selo(c, xr + 290, 970, 40, False, a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s18"] + 0.2, [("resumindo", "i", 92, COR)], W / 2, 200, "center")
        itens = (("s18.a", [("erro", "g", 84), ("÷", "g", 84, TINTA2), ("medida", "g", 84)]),
                 ("s18.b", ps("sempre na", "i", 80) + [("mesma unidade", "g", 84)]),
                 ("s18.c", ps("em %:", "g", 84, COR) + ps("quanto o erro pesa", "i", 80)))
        for i, (k, partes) in enumerate(itens):
            y = 410 + i * 200
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 330, y - 30, 56, a=a),
                                                         E.escreve(c, str(i + 1), 330 - E.larg(str(i + 1), "g", 64) / 2, y - 7, 64, "g", "#FFFFFF", a)))
            E.frase(c, t, C[k] + 0.1, partes, 430, y, "left", 0.12)
    E.saida(c, t, C["s19"] - 0.1, resumo)
    if t < C["s19"]:
        return
    a9, b9, c9, d9 = C["s19.a"], C["s19.b"], C["s19.c"], C["s19.d"]
    E.frase(c, t, PW("s19", "próxima"), [("próxima aula:", "i", 76), ("a % volta para o preço", "g", 76, COR)], W / 2, 190, "center", 0.12)
    fluxo(c, t, 470, [(a9, "?"), (b9, "R$ 120")], "− 20%", "R$ 96", a9, PW("s19", "vinte"), PW("s19", "noventa"), rot=("antes", "com desconto"), size=86)
    E.foco(c, t, c9, 0.5, lambda a: E.pilula(c, "Inscreva-se", W / 2, 760, 72, estilo="g", a=a))
    p = ease_io(prog(t, c9 + 0.3, 0.8))
    E.cursor(c, lerp(1300, W / 2 + 120, p), lerp(960, 785, p), ep(t, c9 + 0.2, 0.4))
    E.frase(c, t, d9, [("bons", "i", 110), ("estudos!", "i", 110, COR)], W / 2, 970, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, ideia=b_ideia, pedreiro=b_pedreiro, relojoeiro=b_relojoeiro, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
