"""Visual — Estudativo · MAT-FIN-009: inflação acumulada e poder de compra.

Linguagem da trilha Matemática Financeira, herdada de Porcentagem:
- cartao() e maquina(): o valor num cartão e o fator (× 1,05) na máquina da cor da matéria; cadeia() junta os anos.
- pacote(): o pacote de café de R$ 20 que mede o poder de compra (5 pacotes viram 4).
- barra_partes(): os preços em partes iguais (4 partes + 1 = 5), no atalho das frações.
Todo instante vem de C[...] (marcadores do roteiro) e dos tempos reais da voz."""
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Matemática Financeira")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-FIN-009_inflacao_e_poder_de_compra.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("acumulada", "poder", "atalho", "questao", "fim"))
BR = "#FFFFFF"
assert round(1.05 * 1.04, 6) == 1.092 and 105 * 104 == 10920 and 5 + 4 + 5 * 4 / 100 == 9.2
assert 100 / 20 == 5 and 100 / 25 == 4 and round(20 * 1.25, 6) == 25 and 1 / 1.25 == 0.8 and round(0.8 * 1.25, 6) == 1
assert 0.75 * 100 / 20 == 3.75  # o erro: perder 25% deixaria 3 pacotes e 3/4
assert round(1.25 * 1.2, 6) == 1.5 and 125 * 12 == 1500 and abs(1 / 1.5 - 2 / 3) < 1e-9 and 25 + 20 == 45


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


def txt(c, t, ti, s, x, y, size=64, cor=None, est="g"):
    E.foco(c, t, ti, 0.45, lambda a: E.escreve(c, s, x, y, size, est, cor or TINTA, a))


def num_bola(c, s, cx, cy, r, size, a=1.0, cor=None):
    E.bola(c, cx, cy + 3, r, cor, a)
    centro(c, s, cx, cy + size * 0.36, size, "g", E.SOBRE if cor is None else M.on(cor), a)


def zero_some(c, t, x, y, size, t1, cor=None):
    """o 0 à esquerda de 0,8: some quando a vírgula sai dele. x = borda esquerda do primeiro algarismo depois da vírgula"""
    E.saida(c, t, t1, lambda: centro(c, "0", x - E.casa(size) * 0.5, y, size, "g", cor or TINTA))


def grupo(c, cx, cy, k, fn):
    """desenha fn() escalado por k em torno de (cx, cy)"""
    c.save(); c.translate(cx, cy); c.scale(k, k); c.translate(-cx, -cy)
    fn()
    c.restore()


def vez(itens, t):
    """itens = texto fixo ou [(t0, texto), ...]; devolve [(t0, t_fim, texto)]"""
    if isinstance(itens, str):
        return [(None, 1e9, itens)]
    return [(t0, itens[i + 1][0] if i + 1 < len(itens) else 1e9, s) for i, (t0, s) in enumerate(itens)]


# ---------------- linguagem herdada de Porcentagem: cartão do valor e máquina do fator ----------------
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
    """a máquina: o fator numa caixa cheia da cor da matéria. fator = texto ou [(t0, texto), ...]"""
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
    """antes → [fator] → depois. ta, tf, td = instantes de cada parte (None = não desenha)"""
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


def volta(c, t, t0, x0, x1, y, rotulo, alto=170, size=62, escuro=False):
    """seta curva por baixo, de x1 (depois) a x0 (antes), com a conta inversa numa pílula. rotulo = texto ou [(t0, texto)]"""
    p = ease_io(prog(t, t0, 0.8))
    if p <= 0:
        return
    cor = "#FFFFFF" if escuro else TINTA
    mx, my = (x0 + x1) / 2, y + 2 * alto
    pts = []
    n = 60
    for i in range(int(n * p) + 1):
        u = i / n
        pts.append(((1 - u) ** 2 * x1 + 2 * u * (1 - u) * mx + u * u * x0, (1 - u) ** 2 * y + 2 * u * (1 - u) * my + u * u * y))
    for (ax, ay), (bx, by) in zip(pts, pts[1:]):
        M.line(c, ax, ay, bx, by, cor, 1.0, 6)
    if len(pts) >= 2 and p > 0.15:
        (ax, ay), (bx, by) = pts[-2], pts[-1]
        M.arrow(c, ax, ay, bx, by, cor, 1.0, 6, 22)
    for ti, tf, s in vez(rotulo, t):
        ti = t0 + 0.4 if ti is None else ti
        E.saida(c, t, tf - 0.05, lambda s=s, ti=ti: E.foco(c, t, ti, 0.45, lambda a: E.pilula(c, s, mx, y + alto, size, "g", fundo=cor,
                                                                                                  cor=TINTA if escuro else BR, a=a)), d=0.25)



def cadeia(c, t, y, valores, fatores, tv, tf, xs=None, rot=None, size=76, cores=None):
    """valor → [fator] → valor → [fator] → valor... na mesma linguagem do fluxo.
    valores/fatores = texto ou [(t0, texto)]; tv/tf = instantes (None = não desenha); rot = rótulo de cada valor.
    O primeiro valor é o de antes (contorno escuro); os outros são depois (cor da matéria)."""
    n = len(valores)
    xs = xs or [lerp(260, W - 260, i / (2 * n - 2)) for i in range(2 * n - 1)]
    ws = []
    for i, v in enumerate(valores):
        if tv[i] is None:
            ws.append(size * 2.9)
            continue
        cor = cores[i] if cores else None
        ws.append(cartao(c, t, tv[i], xs[2 * i], y, v, rot[i] if rot else None, i > 0, size, cor=cor))
    for j, f in enumerate(fatores):
        if tf[j] is None:
            continue
        xm = xs[2 * j + 1]
        wm = maquina(c, t, tf[j], xm, y, f, size * 0.9)
        p = ep(t, tf[j] - 0.1, 0.5)
        if p > 0:
            M.arrow(c, xs[2 * j] + ws[j] / 2 + 14, y, xm - wm / 2 - 14, y, TINTA2, p, 5, 18, p)
            M.arrow(c, xm + wm / 2 + 14, y, xs[2 * j + 2] - ws[j + 1] / 2 - 14, y, TINTA2, p, 5, 18, p)
    return xs


def funde(c, t, t0, t1, x1, x2, y, f1, f2, junto, size=80, sinal_x=True):
    """duas máquinas lado a lado (entram em t0) que deslizam e viram uma só em t1, com o fator multiplicado"""
    xm = (x1 + x2) / 2
    p = ease_io(prog(t, t1, 0.8))
    if p < 1:
        def duas():
            a = 1 - p
            for x, f, d in ((x1, f1, 0), (x2, f2, 0.4)):
                xx = lerp(x, xm, p)
                c.save(); c.translate(0, 0)
                if a < 1:
                    lay = skia.Paint(); lay.setAlphaf(a)
                    c.saveLayer(None, lay)
                maquina(c, t, t0 + d, xx, y, f, size)
                if a < 1:
                    c.restore()
                c.restore()
            if sinal_x and p < 0.3:
                E.foco(c, t, t0 + 0.6, 0.4, lambda q: centro(c, "×", xm, y + size * 0.35, size, "g", TINTA2, q * (1 - p / 0.3)))
        duas()
    if p > 0.5:
        maquina(c, t, t1 + 0.5, xm, y, junto, size * 1.1)


def selo_em(c, t, t0, cx, cy, r=50, ok=True):
    E.foco(c, t, t0, 0.45, lambda p: E.selo(c, cx, cy, r, ok, p))


def topo(c, t, fn, y=470, yf=270, k=0.62):
    """o fluxo da questão, pequeno no alto durante a resposta"""
    grupo(c, W / 2, y, k, lambda: (c.translate(0, (yf - y) / k), fn()))




# ---------------- peças da Matemática Financeira ----------------
def fcen(c, t, t0, s, cx, y, size=84, cor=None, est="g"):
    """fórmula centrada (1,01^{12}, r{1,21}) que entra com foco"""
    E.formula_em(c, t, t0, s, cx, y, size, est, cor, "center")


def contrato(c, t, t0, cx, cy, w, h, linhas, titulo="contrato", size=60):
    """folha de contrato com o canto dobrado; linhas = [(texto, estilo, cor[, tamanho])], centradas"""
    def folha(a):
        x, y = cx - w / 2, cy - h / 2
        s = skia.Paint(AntiAlias=True, Color=M.hexc("#000000", 0.10 * a))
        s.setMaskFilter(skia.MaskFilter.MakeBlur(skia.kNormal_BlurStyle, 14))
        r = skia.Rect.MakeXYWH(x, y, w, h)
        c.save(); c.translate(6, 12); c.drawRect(r, s); c.restore()
        d = 56
        p = skia.Path()
        p.moveTo(x, y); p.lineTo(x + w - d, y); p.lineTo(x + w, y + d); p.lineTo(x + w, y + h); p.lineTo(x, y + h); p.close()
        c.drawPath(p, M.paint(BR, a))
        c.drawPath(p, M.paint(TINTA2, a, stroke=4))
        q = skia.Path()
        q.moveTo(x + w - d, y); q.lineTo(x + w - d, y + d); q.lineTo(x + w, y + d)
        c.drawPath(q, M.paint(TINTA2, a, stroke=4))
        E.escreve(c, titulo.upper(), x + 40, y + 58, 34, "b", TINTA2, a)
        M.line(c, x + 40, y + 78, x + w - 90, y + 78, FIO, a, 3)
        n = len(linhas)
        for i, lin in enumerate(linhas):
            s_, est, cor = lin[:3]
            sz = lin[3] if len(lin) > 3 else size
            yy = y + 78 + (h - 78) * (i + 0.5) / n + sz * 0.36
            centro(c, s_, cx, yy, sz, est, cor, a)
    E.foco(c, t, t0, 0.5, folha)


def linha_tempo(c, t, t0, x0, x1, y, rotulos, tm=None, size=48, cor=None, escuro=False):
    """linha do tempo dos pagamentos: seta de x0 a x1 com um tique por rótulo (hoje, 1 mês, 2 meses...).
    tm = instante de cada rótulo. Devolve a lista de x dos tiques."""
    tinta = cor or ("#FFFFFF" if escuro else TINTA)
    n = len(rotulos)
    xs = [lerp(x0 + 60, x1 - 110, i / max(n - 1, 1)) for i in range(n)]
    p = ease_io(prog(t, t0, 0.8))
    if p > 0:
        M.arrow(c, x0, y, lerp(x0, x1, p), y, tinta, 1.0, 6, 22)
    for i, (x, r) in enumerate(zip(xs, rotulos)):
        ti = tm[i] if tm else t0 + 0.15 * i
        E.foco(c, t, ti, 0.45, lambda a, x=x, r=r: (M.line(c, x, y - 18, x, y + 18, tinta, a, 6),
                                                    centro(c, r, x, y + 30 + size, size, "i", tinta, a)))
    return xs


def pagamento(c, t, t0, x, y, valor, cor=None, alto=150, size=60, cima=True):
    """seta do tique da linha do tempo até a pílula com o valor pago naquele dia"""
    cor = cor or E.COR
    def fn(a):
        y1 = y - alto if cima else y + alto
        M.line(c, x, y + (-14 if cima else 14), x, y1 + (34 if cima else -34), cor, a, 6)
        E.pilula(c, valor, x, y1, size, "g", fundo=cor, cor=M.on(cor), a=a)
    E.foco(c, t, t0, 0.45, fn)


def tabela_fin(c, t, x, y, larg, cab, linhas, tl, tc=None, size=52, h_lin=88, cor_cab=None, destaque=None):
    """tabela do financiamento: cab = títulos das colunas (entram em tc); linhas[i][j] = texto ou (texto, t0[, cor]);
    tl[i] = instante da linha i (as células sem instante próprio entram nele, uma depois da outra).
    destaque = {(i, j): cor} pinta o fundo da célula. (x, y) = canto de cima à esquerda."""
    wt = sum(larg)
    tc = tl[0] - 0.4 if tc is None else tc
    q = ep(t, tc, 0.5)
    if q > 0:
        M.rrect(c, x, y, wt, h_lin, 16, cor_cab or E.COR, q)
        xx = x
        for w, s in zip(larg, cab):
            centro(c, s, xx + w / 2, y + h_lin / 2 + size * 0.3, size * 0.82, "b", E.SOBRE, q)
            xx += w
    for i, lin in enumerate(linhas):
        yy = y + h_lin * (i + 1)
        qi = ep(t, tl[i], 0.4)
        if qi > 0:
            M.line(c, x, yy + h_lin, x + wt, yy + h_lin, FIO, qi, 3)
        xx = x
        for j, (w, cel) in enumerate(zip(larg, lin)):
            if isinstance(cel, tuple):
                s, ti = cel[0], cel[1]
                cor = cel[2] if len(cel) > 2 else TINTA
            else:
                s, ti, cor = cel, tl[i] + 0.12 * j, TINTA
            if destaque and (i, j) in destaque:
                qd = ep(t, destaque[(i, j)][1], 0.4)
                if qd > 0:
                    M.rrect(c, xx + 8, yy + 8, w - 16, h_lin - 16, 12, destaque[(i, j)][0], 0.16 * qd)
            if s:
                E.foco(c, t, ti, 0.4, lambda a, s=s, xx=xx, w=w, cor=cor: centro(c, s, xx + w / 2, yy + h_lin / 2 + size * 0.36, size, "g", cor, a))
            xx += w


def eq_f(c, t, partes, cx, y, size):
    """conta em partes [(fórmula, cor, t0)], centrada em cx; devolve os x e as larguras"""
    ws = [E.formula(c, s, 0, 0, size, a=0) for s, _, _ in partes]
    gap = size * 0.26
    x = cx - (sum(ws) + gap * (len(ws) - 1)) / 2
    xs = []
    for (s, cor, t0), w_ in zip(partes, ws):
        xs.append(x)
        E.formula_em(c, t, t0, s, x, y, size, "g", cor)
        x += w_ + gap
    return xs, ws


# ---------------- tempos reais das palavras ----------------
import json
from pathlib import Path
_TEMPOS = json.loads((Path(__file__).resolve().parents[1] / "audio" / "tempos.json").read_text(encoding="utf-8"))
_CENAS = {s["id"]: s for s in _TEMPOS["scenes"]}


def _limpa(s):
    return s.strip(".,:;?!\"'()").lower()


def w(sid, palavra, n=1):
    """instante em que a voz diz a n-ésima vez `palavra` na cena sid (tempos reais da narração)"""
    s = _CENAS[sid]
    k = 0
    for tk in s["tokens"]:
        if _limpa(tk["disp"]) == _limpa(palavra):
            k += 1
            if k == n:
                return s["start"] + tk["t0"]
    raise KeyError(f"{sid}: '{palavra}' ({n}ª vez) não está na fala")


# ---------------- peças desta aula ----------------
def pacote(c, cx, cy, a=1.0, cor=None, enche=1.0, k=1.0):
    """pacote de café: (cx, cy) = centro. enche < 1 pinta só a parte de baixo (3/4 de pacote) e deixa o contorno tracejado"""
    if a <= 0:
        return
    cor = cor or E.COR
    w, h = 104 * k, 150 * k
    x, y = cx - w / 2, cy - h / 2

    def corpo():
        p = skia.Path()
        p.moveTo(x + 8 * k, y + 22 * k)
        for i in range(7):  # dobra serrilhada no alto
            p.lineTo(x + 8 * k + (w - 16 * k) * (i + 0.5) / 7, y + (12 if i % 2 else 0) * k)
        p.lineTo(x + w - 8 * k, y + 22 * k)
        p.lineTo(x + w, y + h - 14 * k)
        p.quadTo(x + w, y + h, x + w - 14 * k, y + h)
        p.lineTo(x + 14 * k, y + h)
        p.quadTo(x, y + h, x, y + h - 14 * k)
        p.close()
        return p
    p = corpo()
    if enche >= 1:
        s = skia.Paint(AntiAlias=True, Color=M.hexc("#000000", 0.14 * a))
        s.setMaskFilter(skia.MaskFilter.MakeBlur(skia.kNormal_BlurStyle, 8))
        c.save(); c.translate(4, 8); c.drawPath(p, s); c.restore()
        c.drawPath(p, M.paint(cor, a))
    else:
        c.save()
        c.clipRect(skia.Rect.MakeXYWH(x - 4, y + h * (1 - enche), w + 8, h * enche + 4))
        c.drawPath(p, M.paint(cor, a))
        c.restore()
        q = skia.Paint(AntiAlias=True, Color=M.hexc(cor, a), Style=skia.Paint.kStroke_Style, StrokeWidth=4)
        q.setPathEffect(skia.DashPathEffect.Make([12, 9], 0))
        c.drawPath(p, q)
    if enche >= 1:
        M.rrect(c, x + 16 * k, y + 58 * k, w - 32 * k, 46 * k, 10 * k, BR, 0.92 * a)
        centro(c, "café", cx, y + 92 * k, 30 * k, "b", cor, a)


def pacotes(c, t, x0, y, n, t0, passo_x=170, d=0.12, cor=None, enche_ultimo=1.0, k=1.0):
    """n pacotes lado a lado, entrando um a um a partir de t0; o último pode ser parcial"""
    for i in range(n):
        en = enche_ultimo if i == n - 1 else 1.0
        E.foco(c, t, t0 + d * i, 0.4, lambda a, i=i, en=en: pacote(c, x0 + passo_x * i, y, a, cor, en, k))


def barra_partes(c, t, t0, x, y, n, wp, cores, rotulo=None, h=120, escuro=False, d=0.12):
    """barra de n partes de largura wp, entrando uma a uma; cores[i] = cor cheia ou None (só o contorno)"""
    tinta = CLARO if escuro else TINTA
    for i in range(n):
        def fn(a, i=i):
            r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x + i * wp + 6, y, wp - 12, h), 18, 18)
            if cores[i]:
                c.drawRRect(r, M.paint(cores[i], a))
            c.drawRRect(r, M.paint(tinta, a, stroke=4))
        E.foco(c, t, t0 + d * i, 0.4, fn)
    if rotulo:
        E.foco(c, t, t0, 0.45, lambda a: centro(c, rotulo, x - 170, y + h / 2 + 18, 52, "i", tinta, a))


def frac_em(c, t, t0, n, d, cx, cy, size, cor=None):
    E.foco(c, t, t0, 0.45, lambda a: E.fracao(c, n, d, cx, cy, size, cor, a))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    ka, kb, kc = C["s01.a"], C["s01.b"], C["s01.c"]

    def um():
        E.frase(c, t, ka, [("inflação", "g", 76, COR)], W / 2, 170, "center")
        maquina(c, t, w("s01", "cinco"), 620, 380, [(w("s01", "cinco"), "+ 5%")], 90)
        cen(c, t, w("s01", "ano"), "1º ano", 620, 260, 54, TINTA2, "i")
        maquina(c, t, w("s01", "quatro"), 1300, 380, [(w("s01", "quatro"), "+ 4%")], 90)
        cen(c, t, w("s01", "seguinte"), "2º ano", 1300, 260, 54, TINTA2, "i")
        cen(c, t, w("s01", "quatro") + 0.2, "→", 960, 410, 90, TINTA2)
        E.frase(c, t, w("s01", "subiram"), ps("os preços subiram", "i", 80) + [("9%?", "g", 96)], W / 2, 640, "center", 0.14)
        if t >= w("s01", "Quase"):
            E.saida(c, t, kc - 0.1, lambda: E.risco(c, 1130, 660, 1370, 570, t, w("s01", "Quase"), largura=12))
        E.frase(c, t, w("s01", "Quase"), [("quase", "i", 70, ERRADO)], 1480, 640)
        E.foco(c, t, kc, 0.5, lambda a: num_bola(c, "9,2%", W / 2, 850, 140, 100, a))
    E.saida(c, t, C["s02"] - 0.1, um)
    if t >= C["s02"]:
        ta, tb = C["s02.a"], C["s02.b"]
        E.foco(c, t, tb - 0.2, 0.7, lambda a: E.bola(c, 1500, 540, 250 * ease_back(prog(t, tb - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, ps("até o fim desta aula", "i", 90), XE, 330, passo=0.14)
        E.frase(c, t, w("s02", "acumular"), ps("acumular", "i", 96) + [("inflação", "g", 100, COR)], XE, 490, passo=0.14)
        E.frase(c, t, w("s02", "medir"), ps("medir quanto o", "i", 80) + [("dinheiro perde", "g", 84, COR)], XE, 630, passo=0.12)
        E.foco(c, t, tb + 0.1, 0.5, lambda a: (centro(c, "+ atalho", 1500, 525, 80, "g", E.SOBRE, a),
                                               centro(c, "de prova", 1500, 610, 80, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"] + 0.3, ps("você só precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, w("s03", "duas"), 0.5, lambda a: E.escreve(c, "2", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, w("s03", "duas") + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, wc = 880, 900
    ka, kb = C["s03.a"], C["s03.b"]
    p = ep(t, ka, 0.5)
    E.caixa_pontilhada(c, x, 200, wc, 300, p, prog_=p)
    E.frase(c, t, ka + 0.1, [("aumentos seguidos", "i", 62)], x + 44, 285)
    E.frase(c, t, w("s03", "multiplicando"), [("× fator", "g", 72, COR), ("× fator", "g", 72, COR)], x + 44, 420, "left", 0.3)
    p = ep(t, kb, 0.5)
    E.caixa_pontilhada(c, x, 570, wc, 260, p, prog_=p)
    E.frase(c, t, kb + 0.1, [("desfazer uma variação", "i", 62)], x + 44, 655)
    E.frase(c, t, w("s03", "divida"), [("1 ÷ fator", "g", 72, COR)], x + 44, 770)
    q = ease_io(prog(t, kb - 0.35, 0.5))
    E.cursor(c, x + wc - 30, lerp(470, 800, q), ep(t, ka, 0.4))
    E.frase(c, t, w("s03", "Se"), ps("faltou alguma?", "i", 58, COR) + ps("procure no canal", "i", 58), x, 1000, "left", 0.12)


# ---------------- inflação acumulada ----------------
def b_acumulada(c, t, C, b):
    a4, b4 = C["s04.a"], C["s04.b"]
    a5, b5, c5 = C["s05.a"], C["s05.b"], C["s05.c"]
    a6, b6, c6, d6 = C["s06.a"], C["s06.b"], C["s06.c"], C["s06.d"]
    a7, b7, c7 = C["s07.a"], C["s07.b"], C["s07.c"]

    def tela1():
        E.frase(c, t, a4, [("inflação", "g", 96, COR), ("=", "g", 90, TINTA2)] + ps("subida geral dos preços", "i", 84), W / 2, 220, "center", 0.14)
        E.frase(c, t, w("s04", "medida"), ps("medida em %", "i", 60, TINTA2), W / 2, 320, "center")
        fluxo(c, t, 620, "R$ 100", [(w("s04", "cinco"), "+ 5%"), (w("s04", "custava"), "× 1,05")], "R$ 105",
              w("s04", "custava"), w("s04", "cinco"), w("s04", "cento", 3), rot=("custava", "passou a custar"), size=84)
        E.frase(c, t, w("s04", "média"), ps("em média", "i", 56, TINTA2), XM, 820, "center")
    E.saida(c, t, C["s05"] - 0.1, tela1)
    if C["s05"] <= t < C["s07"]:
        def tela2():
            cadeia(c, t, 300, ["R$ 100", "R$ 105", [(a5, "?"), (c6, "+ 9,2%")]], ["× 1,05", "× 1,04"],
                   [C["s05"], C["s05"] + 0.2, a5], [C["s05"] + 0.1, w("s05", "quatro")], rot=["hoje", "1 ano", "2 anos"], size=76)
            E.frase(c, t, w("s05", "preços"), ps("os 4% valem sobre", "i", 56, TINTA2) + [("R$ 105", "g", 56, COR)], 1310, 470, "center", 0.1)
            E.frase(c, t, b5, ps("aumentos seguidos:", "i", 70) + [("multiplique os fatores", "g", 70, COR)], W / 2, 600, "center", 0.12)
            eq_f(c, t, [("1,05 × 1,04", TINTA, c5), ("= 1,092", COR, b6)], W / 2, 750, 110)
            E.saida(c, t, w("s06", "Tire") - 0.1, lambda: E.frase(c, t, a6, ps("sem vírgulas:", "i", 60, TINTA2) +
                                                                   [("105 × 104 = 10920", "g", 64), ("com 4 casas", "i", 60, TINTA2)],
                                                                   W / 2, 900, "center", 0.15))
            E.frase(c, t, w("s06", "Tire"), ps("tire o inteiro:", "i", 70) + [("9,2%", "g", 90, COR)], 760, 910, "center", 0.15)
            E.foco(c, t, d6, 0.45, lambda a: E.pilula(c, "inflação acumulada", 1420, 885, 60, "g", a=a))
            cen(c, t, w("s06", "subida"), "a subida total do período", 1420, 1000, 46, TINTA2, "i")
        E.saida(c, t, C["s07"] - 0.1, tela2)
    if t < C["s07"]:
        return
    E.frase(c, t, C["s07"] + 0.3, ps("o atalho de", "i", 80) + [("aumentos seguidos", "g", 80, COR)] + ps("confirma", "i", 80), W / 2, 210, "center", 0.12)
    E.frase(c, t, a7, [("5 + 4", "g", 110), ("=", "g", 110, TINTA2), ("9", "g", 110)], W / 2, 430, "center", 0.25)
    E.frase(c, t, b7, [("5 × 4 ÷ 100", "g", 110), ("=", "g", 110, TINTA2), ("0,2", "g", 110)], W / 2, 620, "center", 0.25)
    E.foco(c, t, c7, 0.5, lambda a: E.pilula(c, "9 + 0,2 = 9,2%", W / 2, 830, 100, "g", a=a))


# ---------------- poder de compra ----------------
PX0 = 1080  # x do primeiro pacote


def b_poder(c, t, C, b):
    a8, b8, c8 = C["s08.a"], C["s08.b"], C["s08.c"]
    a9, b9, c9 = C["s09.a"], C["s09.b"], C["s09.c"]
    a10, b10, c10 = C["s10.a"], C["s10.b"], C["s10.c"]
    a11, b11, c11 = C["s11.a"], C["s11.b"], C["s11.c"]
    a12, b12 = C["s12.a"], C["s12.b"]

    def tela1():
        E.frase(c, t, C["s08"] + 0.3, ps("o outro lado:", "i", 76) + [("poder de compra", "g", 80, COR)], W / 2, 150, "center", 0.12)
        E.frase(c, t, w("s08", "quanto"), ps("quanto o seu dinheiro consegue comprar", "i", 56, TINTA2), W / 2, 240, "center", 0.08)
        # antes
        cartao(c, t, w("s08", "cem"), 300, 460, "R$ 100", "você tem", False, 70)
        cartao(c, t, b8, 700, 460, "R$ 20", "o café", False, 70)
        pacotes(c, t, PX0, 470, 5, c8, passo_x=135, k=0.85)
        cen(c, t, c8 + 0.6, "= 5", 1760, 500, 90, COR, "g")
        # depois
        E.foco(c, t, a9, 0.45, lambda q: E.pilula(c, "preços + 25%", W / 2, 690, 58, "g", fundo=TINTA, a=q))
        cartao(c, t, w("s09", "dinheiro"), 300, 900, "R$ 100", "o mesmo", False, 70)
        cartao(c, t, b9, 700, 900, "R$ 25", "o café", True, 70)
        pacotes(c, t, PX0, 910, 4, c9, passo_x=135, k=0.85)
        cen(c, t, c9 + 0.5, "= 4", 1760, 940, 90, COR, "g")
    E.saida(c, t, C["s10"] - 0.1, tela1)
    if C["s10"] <= t < C["s11"]:
        def tela2():
            E.frase(c, t, C["s10"] + 0.3, ps("eram", "i", 80) + [("5", "g", 90)] + ps("e ficaram", "i", 80) + [("4", "g", 90, COR)], W / 2, 190, "center", 0.12)
            for i in range(5):
                perde = i == 4
                cor = None
                if perde and t >= a10:
                    cor = E.mix(E.COR, BR, 0.75)
                E.foco(c, t, C["s10"] + 0.3 + 0.1 * i, 0.4, lambda q, i=i, cor=cor: pacote(c, 620 + 170 * i, 420, q, cor))
            if t >= a10:
                E.risco(c, 1260, 500, 1400, 340, t, a10, largura=10)
            E.frase(c, t, w("s10", "um", 2), ps("perdeu 1 em 5 =", "i", 76), 880, 680, "right", 0.12)
            frac_em(c, t, w("s10", "quinto"), 1, 5, 990, 640, 84, COR)
            E.frase(c, t, b10, [("=", "g", 90, TINTA2), ("20%", "g", 100, COR)], 1080, 680, "left", 0.2)
            E.frase(c, t, w("s10", "Os"), ps("preços:", "i", 70) + [("+ 25%", "g", 80)], 620, 880, "center", 0.15)
            E.frase(c, t, c10 - 0.6, ps("perda:", "i", 70) + [("20%", "g", 90, COR)], 1320, 880, "center", 0.15)
        E.saida(c, t, C["s11"] - 0.1, tela2)
    if C["s11"] <= t < C["s12"]:
        def tela3():
            E.frase(c, t, C["s11"] + 0.3, [("a regra", "g", 80, COR)], W / 2, 180, "center")
            E.frase(c, t, w("s11", "poder"), ps("poder de compra novo =", "i", 76) + [("1 ÷ fator", "g", 84, COR)], W / 2, 330, "center", 0.12)
            E.frase(c, t, b11, [("1 ÷ 1,25", "g", 130), ("=", "g", 130, TINTA2)], 1080, 560, "right", 0.3)
            E.frase(c, t, w("s11", "zero"), [("0,8", "g", 130, COR)], 1130, 560, "left")
            E.frase(c, t, w("s11", "oitenta"), ps("compra", "i", 76) + [("80%", "g", 84)] + ps("do que comprava", "i", 76), W / 2, 760, "center", 0.12)
            E.foco(c, t, c11, 0.45, lambda q: E.pilula(c, "perda de 20%", W / 2, 900, 80, "g", a=q))
        E.saida(c, t, C["s12"] - 0.1, tela3)
    if t < C["s12"]:
        return
    E.frase(c, t, C["s12"] + 0.3, ps("a conta de", "i", 76) + [("voltar ao valor original", "g", 76, COR)], W / 2, 180, "center", 0.12)
    fluxo(c, t, 520, "80%", "+ 25%", "100%", w("s12", "comprava"), a12, b12 - 0.6, rot=("compra hoje", "recupera"), size=90)
    E.frase(c, t, a12, ps("o salário precisa subir", "i", 72) + [("25%", "g", 80, COR)], W / 2, 800, "center", 0.12)
    E.frase(c, t, b12, ps("o mesmo que", "i", 72) + [("os preços", "g", 76)], W / 2, 920, "center", 0.12)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    a, b_, c_ = C["s13.a"], C["s13.b"], C["s13.c"]
    E.frase(c, t, C["s13"] + 0.3, [("o erro", "g", 100, ERRADO)] + ps("comum", "i", 96), W / 2, 170, "center", 0.14)
    E.frase(c, t, a, ps("preço", "i", 76) + [("+ 25%", "g", 84)] + ps("tira", "i", 76) + [("25%", "g", 84, ERRADO)] + ps("do poder?", "i", 76),
            W / 2, 330, "center", 0.12)
    E.frase(c, t, w("s13", "Se"), ps("se fosse assim:", "i", 60, TINTA2), 360, 560, "center")
    pacotes(c, t, 660, 560, 4, b_, cor=ERRADO, enche_ultimo=0.75)
    E.frase(c, t, w("s13", "três", 2), [("3 e ¾", "g", 80, ERRADO)], 1400, 590)
    E.frase(c, t, w("s13", "Mas"), ps("mas você leva:", "i", 60, TINTA2), 360, 830, "center")
    pacotes(c, t, 660, 830, 4, c_)
    E.frase(c, t, c_ + 0.3, [("4", "g", 100, COR)], 1400, 865)
    selo_em(c, t, c_ + 0.5, 1540, 830, 50, True)


# ---------------- atalho (palco escuro) ----------------
WP = 230


def b_atalho(c, t, C, b):
    palco(c, t)
    a14, b14, c14 = C["s14.a"], C["s14.b"], C["s14.c"]
    a15, b15, c15, d15 = C["s15.a"], C["s15.b"], C["s15.c"], C["s15.d"]

    def barras():
        E.frase(c, t, C["s14"] + 0.3, [("o atalho", "g", 64, BR), ("com frações", "i", 68, CLARO)], W / 2, 130, "center", 0.2)
        E.frase(c, t, a14, [("25% =", "g", 100, BR)], 920, 310, "right")
        frac_em(c, t, a14 + 0.6, 1, 4, 1030, 270, 90, CLARO)
        x0 = 520
        barra_partes(c, t, w("s14", "tinham"), x0, 420, 4, WP, [None] * 4, "preço antigo", escuro=True)
        novo = [CLARO if t >= c14 else None] * 4 + ["#3A3A4A" if t >= c14 else None]
        barra_partes(c, t, w("s14", "ganharam"), x0, 620, 5, WP, novo, "preço novo", escuro=True)
        if t >= w("s14", "ganharam"):
            E.foco(c, t, w("s14", "ganharam"), 0.4, lambda q: E.pilula(c, "+1", x0 + 4.5 * WP, 470, 56, "g", fundo=CLARO, cor="#07070F", a=q))
        E.chave(c, x0 + 6, x0 + 5 * WP - 6, 770, CLARO, ep(t, b14, 0.4), 24, 6)
        E.foco(c, t, b14 + 0.1, 0.4, lambda q: centro(c, "5 partes", x0 + 2.5 * WP, 850, 54, "i", CLARO, q))
        E.frase(c, t, c14, ps("seu dinheiro paga", "i", 70, CLARO) + [("4 de 5", "g", 76, BR)], W / 2, 960, "center", 0.12)
        E.foco(c, t, w("s14", "perdeu"), 0.45, lambda q: E.pilula(c, "perdeu 1/5", 1600, 930, 60, "g", fundo=CLARO, cor="#07070F", a=q))
    E.saida(c, t, C["s15"] - 0.1, barras)
    if t < C["s15"]:
        return
    for y, ti, n1, d1, n2, d2 in ((280, a15, 1, 4, 1, 5), (470, b15, 1, 3, 1, 4)):
        E.frase(c, t, ti, ps("subiu", "i", 80, CLARO), 700, y + 30, "right")
        frac_em(c, t, ti + 0.2, n1, d1, 790, y, 84, BR)
        E.frase(c, t, ti + 0.6, [("→", "g", 80, CLARO)] + ps("perde", "i", 80, CLARO), 900, y + 30, "left", 0.15)
        frac_em(c, t, ti + 1.0, n2, d2, 1210, y, 84, CLARO)
    E.frase(c, t, w("s15", "perda"), ps("a perda é sobre", "i", 66, CLARO) + [("o preço novo", "g", 70, BR)] + ps("(maior)", "i", 66, CLARO),
            W / 2, 680, "center", 0.12)
    E.frase(c, t, w("s15", "sete"), [("7%?", "g", 96, BR)], 700, 900, "center")
    if t >= w("s15", "sete") + 0.5:
        E.risco(c, 590, 920, 820, 820, t, w("s15", "sete") + 0.5, largura=12)
    E.foco(c, t, d15, 0.5, lambda q: E.pilula(c, "1 ÷ fator", 1180, 870, 84, "g", fundo=CLARO, cor="#07070F", a=q))


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    a, b_, c_, d = C["s16.a"], C["s16.b"], C["s16.c"], C["s16.d"]
    E.frase(c, t, C["s16"] + 0.3, ps("hora de", "i", 72, COR) + [("testar", "g", 72)], XE, 150)
    E.frase(c, t, w("s16", "inflação"), ps("inflação alta", "i", 60, TINTA2), XE + 520, 150)
    cen(c, t, a, "1º ano", 640, 260, 54, TINTA2, "i")
    maquina(c, t, a, 640, 370, "+ 25%", 90)
    cen(c, t, b_ + 0.1, "→", 960, 400, 90, TINTA2)
    cen(c, t, b_, "2º ano", 1280, 260, 54, TINTA2, "i")
    maquina(c, t, b_, 1280, 370, "+ 20%", 90)
    E.frase(c, t, w("s16", "salário"), ps("salário de Ana:", "i", 66) + [("não mudou", "g", 70, COR)], W / 2, 590, "center", 0.12)
    E.saida(c, t, C["s17"] - 0.1, lambda: (E.frase(c, t, c_, [("1.", "g", 66, COR)] + ps("inflação acumulada?", "i", 70), XE + 200, 780, "left", 0.12),
                                           E.frase(c, t, d, [("2.", "g", 66, COR)] + ps("quanto Ana perdeu de poder de compra?", "i", 70), XE + 200, 900, "left", 0.1)))
    E.relogio(c, t, C["s17.a"], 960, 780, 110)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    a, b_, c_, d = C["s18.a"], C["s18.b"], C["s18.c"], C["s18.d"]
    a19, b19, c19, d19 = C["s19.a"], C["s19.b"], C["s19.c"], C["s19.d"]

    def inflacao():
        E.frase(c, t, w("s18", "Fatores"), ps("fatores:", "i", 76), XE, 230)
        E.frase(c, t, a, [("1,25", "g", 90, COR), ("e", "i", 80), ("1,2", "g", 90, COR)], XE + 300, 230, "left", 0.4)
        E.frase(c, t, w("s18", "Sem"), ps("sem vírgulas:", "i", 64, TINTA2), XE, 400)
        E.frase(c, t, b_, [("125 × 12", "g", 84), ("=", "g", 84, TINTA2), ("1500", "g", 84)], XE + 420, 400, "left", 0.25)
        E.frase(c, t, w("s18", "Com"), ps("3 casas:", "i", 64, TINTA2), XE, 570)
        E.frase(c, t, c_, [("1,25 × 1,2", "g", 84), ("=", "g", 84, TINTA2), ("1,5", "g", 84, COR)], XE + 420, 570, "left", 0.25)
        E.foco(c, t, w("s18", "cinquenta"), 0.5, lambda q: num_bola(c, "50%", 1560, 420, 160, 110, q))
        cen(c, t, w("s18", "inflação"), "acumulada", 1560, 660, 56, COR, "i")
        E.frase(c, t, w("s18", "Quem"), ps("quem somou:", "i", 70, TINTA2) + [("25 + 20 = 45%", "g", 80, ERRADO)], W / 2, 860, "center", 0.12)
        if t >= d + 0.6:
            E.risco(c, 940, 880, 1460, 800, t, d + 0.6, largura=12)
    E.saida(c, t, C["s19"] - 0.1, inflacao)
    if t < C["s19"]:
        return
    E.frase(c, t, C["s19"] + 0.3, ps("poder de compra:", "i", 76) + [("50% = metade", "g", 76, COR)], W / 2, 150, "center", 0.12)
    x0 = 600
    barra_partes(c, t, a19, x0, 260, 2, WP, [None] * 2, "preço antigo")
    pago = [E.COR if t >= b19 else None] * 2 + [E.mix(E.COR, BR, 0.75) if t >= b19 else None]
    barra_partes(c, t, w("s19", "ganharam"), x0, 430, 3, WP, pago, "preço novo")
    E.frase(c, t, b19, ps("o dinheiro de Ana paga", "i", 64) + [("2 de 3", "g", 70, COR)], W / 2, 660, "center", 0.12)
    E.frase(c, t, c19 - 0.4, ps("perdeu", "i", 80), 760, 830, "right")
    frac_em(c, t, c19, 1, 3, 860, 790, 80, COR)
    E.frase(c, t, w("s19", "cerca"), [("≈ 33%", "g", 90, COR)], 940, 830, "left")
    E.frase(c, t, d19, ps("pelo fator:", "i", 64, TINTA2) + [("1 ÷ 1,5 =", "g", 76)], 1060, 980, "right", 0.12)
    frac_em(c, t, w("s19", "dois"), 2, 3, 1150, 945, 70, COR)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    a20, b20 = C["s20.a"], C["s20.b"]

    def resumo():
        E.frase(c, t, C["s20"] + 0.3, [("resumindo", "i", 92, COR)], W / 2, 210, "center")
        E.frase(c, t, a20, ps("inflação acumula:", "i", 84) + [("× fatores", "g", 96, COR)], W / 2, 450, "center", 0.14)
        E.frase(c, t, b20, ps("poder de compra:", "i", 84) + [("1 ÷ fator", "g", 96, COR)], W / 2, 680, "center", 0.14)
    E.saida(c, t, C["s21"] - 0.1, resumo)
    if t < C["s21"]:
        return
    a, b_, c_, d = C["s21.a"], C["s21.b"], C["s21.c"], C["s21.d"]
    E.frase(c, t, C["s21"] + 0.1, [("próxima", "i", 84), ("aula", "i", 84)], XE, 300)
    E.frase(c, t, w("s21", "rendimento") - 0.3, [("Taxa real de juros", "g", 112, COR)], XE, 450)
    E.frase(c, t, a, ps("rendeu", "i", 76) + [("10%", "g", 76)] + ps("· inflação", "i", 76) + [("5%", "g", 76)], XE, 610, "left", 0.15)
    E.frase(c, t, b_, ps("ganho de verdade:", "i", 76) + [("não é 5%", "g", 76, ERRADO)], XE, 740, "left", 0.15)
    E.foco(c, t, c_, 0.5, lambda q: E.pilula(c, "Inscreva-se", 1520, 300, 72, estilo="g", a=q))
    p = ease_io(prog(t, c_ + 0.3, 0.8))
    E.cursor(c, lerp(1800, 1640, p), lerp(620, 325, p), ep(t, c_ + 0.2, 0.4))
    E.frase(c, t, d, [("bons", "i", 120), ("estudos!", "i", 120, COR)], W / 2, 940, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, acumulada=b_acumulada, poder=b_poder, erro=b_erro, atalho=b_atalho,
              questao=b_questao, resposta=b_resposta, fim=b_fim)
