"""Visual — Estudativo · MAT-FIN-013: rendimento líquido.

Linguagem da trilha Matemática Financeira, herdada de Porcentagem:
- cartao() e maquina(): o valor num cartão e o fator (× 0,85, × 1,21) na máquina da cor da matéria.
- barra_montante(): o montante como barra, capital + rendimento; o rendimento abre em imposto e líquido.
Todo instante vem de C[...] (marcadores do roteiro) e dos tempos reais da voz."""
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Matemática Financeira")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-FIN-013_rendimento_liquido.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("regra", "compostos", "comparar", "atalho", "questao", "fim"))
BR = "#FFFFFF"
assert 11000 - 10000 == 1000 and 0.15 * 1000 == 150 and 1000 - 150 == 850 and 10000 + 850 == 10850 and round(11000 * 0.85) == 9350
assert round(10 * 0.85, 2) == 8.5 and round(10000 * 1.21) == 12100 and round(0.10 * 2100) == 210 and round(0.05 * 2100) == 105 and 2100 - 315 == 1785
assert round(0.15 * 11000) == 1650 and 11000 - 1650 == 9350 and round(12 * 0.85, 2) == 10.2 and round(12 - 1.2 - 0.6, 6) == 10.2
assert 0.12 * 20000 == 2400 and 0.15 * 2400 == 360 and 2400 - 360 == 2040 and 0.10 * 20000 == 2000 and 2040 - 2000 == 40


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
BX, BY, BH = 200, 300, 130  # barra do montante
WCAP, WREN = 1180, 330      # capital e rendimento (esquemático: o rendimento aparece maior que a proporção)


def barra_montante(c, t, tc, tr, cap="R$ 10.000", ren="R$ 1.000"):
    """o montante como barra: capital (escuro, entra em tc) + rendimento (cor da matéria, entra em tr)"""
    q = ep(t, tc, 0.5)
    if q > 0:
        M.rrect(c, BX, BY, WCAP - 6, BH, 22, TINTA, q)
        centro(c, "capital " + cap, BX + WCAP / 2, BY + BH / 2 + 24, 64, "g", BR, q)
    q = ep(t, tr, 0.5)
    if q > 0:
        M.rrect(c, BX + WCAP + 6, BY, WREN - 6, BH, 22, E.COR, q)
        centro(c, ren, BX + WCAP + WREN / 2, BY + BH / 2 + 24, 64, "g", E.SOBRE, q)


def zoom_rendimento(c, t, t0, tp, ti, tl, y=560, x0=440, x1=1720, h=140):
    """o rendimento aberto embaixo: imposto (15%) + líquido (85%), com as guias saindo do pedaço da barra"""
    q = ep(t, t0, 0.6)
    if q <= 0:
        return
    M.line(c, BX + WCAP + 6, BY + BH + 6, x0, y - 6, TINTA2, q, 3, dash=[10, 8])
    M.line(c, BX + WCAP + WREN, BY + BH + 6, x1, y - 6, TINTA2, q, 3, dash=[10, 8])
    wi = (x1 - x0) * 0.15
    qi = ep(t, ti, 0.5)
    ql = ep(t, tl, 0.5)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x0, y, x1 - x0, h), 22, 22), M.paint(TINTA2, q * (1 - ql) * 0.6, stroke=4))
    if qi > 0:
        M.rrect(c, x0, y, wi - 6, h, 22, ERRADO, qi)
        centro(c, "R$ 150", x0 + wi / 2, y + h / 2 + 18, 46, "g", BR, qi)
        centro(c, "imposto", x0 + wi / 2, y + h + 56, 46, "i", ERRADO, qi)
    if ql > 0:
        M.rrect(c, x0 + wi + 6, y, x1 - x0 - wi - 6, h, 22, E.COR, ql)
        centro(c, "R$ 850", x0 + wi + (x1 - x0 - wi) / 2, y + h / 2 + 24, 64, "g", E.SOBRE, ql)
        centro(c, "rendimento líquido", x0 + wi + (x1 - x0 - wi) / 2, y + h + 56, 46, "i", COR, ql)
    if tp is not None:
        E.foco(c, t, tp, 0.4, lambda a: centro(c, "rendimento bruto: R$ 1.000", (x0 + x1) / 2, y - 30, 44, "i", TINTA2, a))


def explica(c, t, itens, y=880, x=None):
    """uma linha de explicação por vez: itens = [(t0, partes)]"""
    for i, (t0, partes) in enumerate(itens):
        fim = itens[i + 1][0] if i + 1 < len(itens) else 1e9
        E.saida(c, t, fim - 0.1, lambda t0=t0, partes=partes: E.frase(c, t, t0, partes, x or W / 2, y, "center", 0.15))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    ka, kb, kc = C["s01.a"], C["s01.b"], C["s01.c"]

    def um():
        fluxo(c, t, 330, "R$ 10.000", "rendeu", "R$ 11.000", w("s01", "dez"), w("s01", "chegou"), w("s01", "onze"),
              rot=("você aplicou", "chegou a"), size=80)
        E.foco(c, t, kb, 0.45, lambda q: E.pilula(c, "imposto de 15%", W / 2, 540, 70, "g", fundo=TINTA, a=q))
        E.frase(c, t, w("s01", "Você", 2), ps("leva para casa", "i", 76) + [("R$ 9.350?", "g", 84)], W / 2, 720, "center", 0.14)
        if t >= w("s01", "Não"):
            E.saida(c, t, kc - 0.1, lambda: E.risco(c, 1060, 740, 1440, 650, t, w("s01", "Não"), largura=12))
        E.foco(c, t, kc, 0.5, lambda q: E.pilula(c, "R$ 10.850", W / 2, 900, 110, "g", a=q))
    E.saida(c, t, C["s02"] - 0.1, um)
    if t >= C["s02"]:
        ta, tb = C["s02.a"], C["s02.b"]
        E.foco(c, t, tb - 0.2, 0.7, lambda a: E.bola(c, 1500, 540, 250 * ease_back(prog(t, tb - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, ps("até o fim desta aula", "i", 90), XE, 330, passo=0.14)
        E.frase(c, t, w("s02", "descontar"), ps("descontar o", "i", 90) + [("imposto", "g", 96, COR)], XE, 490, passo=0.14)
        E.frase(c, t, w("s02", "comparar"), ps("e comparar", "i", 90) + [("aplicações", "g", 96, COR)], XE, 630, passo=0.12)
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
    E.frase(c, t, ka + 0.1, [("porcentagem de cabeça", "i", 62)], x + 44, 285)
    E.frase(c, t, w("s03", "quinze"), [("15%", "g", 72), ("=", "g", 72, TINTA2), ("10% + 5%", "g", 72, COR)], x + 44, 420, "left", 0.25)
    p = ep(t, kb, 0.5)
    E.caixa_pontilhada(c, x, 570, wc, 260, p, prog_=p)
    E.frase(c, t, kb + 0.1, [("montante nos juros compostos", "i", 62)], x + 44, 655)
    E.frase(c, t, w("s03", "capital"), [("capital × fator × fator…", "g", 64, COR)], x + 44, 770)
    q = ease_io(prog(t, kb - 0.35, 0.5))
    E.cursor(c, x + wc - 30, lerp(470, 800, q), ep(t, ka, 0.4))
    E.frase(c, t, w("s03", "Se"), ps("faltou alguma?", "i", 58, COR) + ps("procure no canal", "i", 58), x, 1000, "left", 0.12)


# ---------------- os nomes ----------------
def b_nomes(c, t, C, b):
    a4, b4 = C["s04.a"], C["s04.b"]
    a5, b5, c5, d5 = C["s05.a"], C["s05.b"], C["s05.c"], C["s05.d"]
    a6, b6 = C["s06.a"], C["s06.b"]
    E.chave(c, BX + 6, BX + WCAP + WREN - 6, BY - 24, TINTA2, ep(t, w("s04", "Montante"), 0.5), -26, 6)
    E.foco(c, t, w("s04", "Montante"), 0.45, lambda q: centro(c, "montante: R$ 11.000", BX + (WCAP + WREN) / 2, BY - 80, 56, "g", TINTA, q))
    barra_montante(c, t, w("s04", "capital"), a4)
    E.foco(c, t, a4, 0.45, lambda q: centro(c, "rendimento bruto", BX + WCAP + WREN / 2, BY + BH + 60, 46, "i", COR, q))
    zoom_rendimento(c, t, a5, None, b5 + 1.5, c5)
    explica(c, t, [(a4 + 0.6, [("rendimento bruto", "g", 64, COR), ("=", "g", 64, TINTA2)] + ps("montante − capital", "i", 64)),
                   (w("s04", "Onze"), [("R$ 11.000 − R$ 10.000", "g", 70), ("=", "g", 70, TINTA2), ("R$ 1.000", "g", 70, COR)]),
                   (a5, ps("imposto de 15%:", "i", 64) + [("só sobre o rendimento", "g", 66, ERRADO)]),
                   (w("s05", "Quinze", 2), [("15% de R$ 1.000", "g", 66), ("=", "g", 66, TINTA2), ("100 + 50", "g", 66), ("=", "g", 66, TINTA2),
                                         ("R$ 150", "g", 66, ERRADO)]),
                   (w("s05", "mil", 2), [("R$ 1.000 − R$ 150", "g", 70), ("=", "g", 70, TINTA2), ("R$ 850", "g", 70, COR)]),
                   (a6, ps("você leva:", "i", 66) + [("R$ 10.000 + R$ 850", "g", 70)]),
                   (b6, ps("você leva:", "i", 66) + [("R$ 10.000 + R$ 850", "g", 70), ("=", "g", 70, TINTA2), ("R$ 10.850", "g", 76, COR)])],
            y=900)


# ---------------- a regra ----------------
def b_regra(c, t, C, b):
    a, b_, c_ = C["s07.a"], C["s07.b"], C["s07.c"]
    E.frase(c, t, C["s07"] + 0.3, [("a regra", "g", 80, COR)], W / 2, 170, "center")
    fluxo(c, t, 380, "bruto", "× 0,85", "líquido", a, w("s07", "vezes"), w("s07", "bruto") - 0.3, rot=("rendimento", "rendimento"), size=84)
    E.frase(c, t, w("s07", "Tirar"), ps("tirar", "i", 72) + [("15%", "g", 80, ERRADO)] + ps("é ficar com", "i", 72) + [("85%", "g", 80, COR)],
            W / 2, 600, "center", 0.14)
    fluxo(c, t, 830, "10%", "× 0,85", "8,5%", c_, w("s07", "viram"), w("s07", "oito"), rot=("taxa bruta", "taxa líquida"), size=84)


# ---------------- juros compostos ----------------
def b_compostos(c, t, C, b):
    a8, b8, c8 = C["s08.a"], C["s08.b"], C["s08.c"]
    a9, b9, c9, d9, e9 = (C["s09." + k] for k in "abcde")
    E.frase(c, t, a8, [("10% ao ano", "g", 72, COR)] + ps("por 2 anos", "i", 72), W / 2, 170, "center", 0.14)
    fluxo(c, t, 380, "R$ 10.000", "× 1,21", "R$ 12.100", a8, b8, w("s08", "montante"), rot=("capital", "montante"), size=80)
    E.frase(c, t, w("s08", "Rendimento"), ps("rendimento bruto:", "i", 70) + [("R$ 2.100", "g", 84, COR)], W / 2, 600, "center", 0.14)
    E.frase(c, t, w("s09", "Imposto"), ps("imposto:", "i", 64), 400, 760, "right")
    E.frase(c, t, a9 - 1.2, [("10% =", "g", 64), ("R$ 210", "g", 64)], 440, 760, "left", 0.3)
    E.frase(c, t, b9 - 0.6, [("+", "g", 64, TINTA2), ("5% =", "g", 64), ("R$ 105", "g", 64)], 900, 760, "left", 0.3)
    E.frase(c, t, c9, [("=", "g", 64, TINTA2), ("R$ 315", "g", 68, ERRADO)], 1400, 760, "left", 0.2)
    E.frase(c, t, w("s09", "Líquido"), ps("líquido:", "i", 70) + [("R$ 2.100 − R$ 315", "g", 76)], 1080, 900, "right", 0.14)
    E.frase(c, t, d9, [("=", "g", 76, TINTA2), ("R$ 1.785", "g", 84, COR)], 1110, 900, "left", 0.2)
    E.foco(c, t, e9, 0.45, lambda q: E.pilula(c, "imposto sobre o rendimento do período todo, de uma vez", W / 2, 1015, 46, "g", fundo=TINTA, a=q))


# ---------------- comparar duas aplicações ----------------
def b_comparar(c, t, C, b):
    a, b_, c_, d, e = (C["s10." + k] for k in "abcde")
    for x, nome, ti in ((520, "aplicação A", w("s10", "aplicação")), (1400, "aplicação B", w("s10", "aplicação", 2))):
        E.foco(c, t, ti, 0.45, lambda q, x=x, nome=nome: E.pilula(c, nome, x, 170, 64, "g", fundo=TINTA, a=q))
    cartao(c, t, a, 520, 340, [(a, "10% ao ano"), (c_, "8,5% ao ano")], None, c_ <= t, 76)
    E.frase(c, t, w("s10", "quinze"), ps("15% de imposto", "i", 56, ERRADO), 520, 480, "center", 0.1)
    cartao(c, t, b_, 1400, 340, "9% ao ano", None, True, 76)
    E.frase(c, t, w("s10", "sem"), ps("sem imposto", "i", 56, CERTO), 1400, 480, "center", 0.1)
    E.frase(c, t, w("s10", "taxa"), ps("a taxa maior", "i", 72) + [("engana", "g", 76, ERRADO)], W / 2, 680, "center", 0.12)
    E.frase(c, t, c_, ps("líquido de A", "i", 52, COR), 520, 550, "center", 0.1)
    E.foco(c, t, w("s10", "B", 3) + 0.2, 0.45, lambda q: E.pilula(c, "B ganha", 1400, 560, 64, "g", a=q))
    E.frase(c, t, w("s10", "Em"), ps("com", "i", 66) + [("R$ 10.000:", "g", 70)], W / 2, 800, "center", 0.12)
    E.frase(c, t, e, [("A", "g", 76, TINTA2), ("→", "g", 76, TINTA2), ("R$ 850", "g", 84)], 520, 940, "center", 0.2)
    E.frase(c, t, w("s10", "novecentos") - 0.4, [("B", "g", 76, TINTA2), ("→", "g", 76, TINTA2), ("R$ 900", "g", 84, COR)], 1400, 940, "center", 0.2)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    a, b_, c_, d = C["s11.a"], C["s11.b"], C["s11.c"], C["s11.d"]
    E.frase(c, t, C["s11"] + 0.3, [("o erro", "g", 100, ERRADO)] + ps("comum", "i", 96), W / 2, 170, "center", 0.14)
    E.frase(c, t, a, ps("tirar o imposto", "i", 72) + [("de tudo, até do capital", "g", 76, ERRADO)], W / 2, 320, "center", 0.12)
    E.frase(c, t, w("s11", "Quinze"), [("15% de R$ 11.000", "g", 84), ("=", "g", 84, TINTA2), ("R$ 1.650", "g", 84, ERRADO)], W / 2, 490, "center", 0.2)
    E.frase(c, t, c_ - 0.4, ps("sobrariam", "i", 76) + [("R$ 9.350", "g", 90, ERRADO)], W / 2, 640, "center", 0.14)
    E.frase(c, t, w("s11", "menos"), ps("menos do que os", "i", 66) + [("R$ 10.000", "g", 70)] + ps("aplicados!", "i", 66), W / 2, 760, "center", 0.12)
    E.foco(c, t, d, 0.45, lambda q: E.pilula(c, "o imposto nunca come o capital", W / 2, 910, 80, "g", a=q))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    a12, b12, c12 = C["s12.a"], C["s12.b"], C["s12.c"]
    a13, b13 = C["s13.a"], C["s13.b"]

    def um():
        E.frase(c, t, C["s12"] + 0.3, [("o atalho", "g", 64, BR)] + ps("para comparar", "i", 68, CLARO), W / 2, 140, "center", 0.2)
        E.linha(c, t, [("taxa bruta", "g", 84, BR, a12), ("− 10% dela", "g", 84, CLARO, w("s12", "dez")), ("− 5% dela", "g", 84, CLARO, w("s12", "cinco"))],
                W / 2, 340, "center")
        E.frase(c, t, w("s12", "Doze"), [("12%", "g", 120, BR)], 560, 600, "center")
        E.frase(c, t, b12, [("− 1,2", "g", 110, CLARO)], 960, 600, "center")
        E.frase(c, t, w("s12", "zero"), [("− 0,6", "g", 110, CLARO)], 1360, 600, "center")
        E.foco(c, t, c12, 0.5, lambda q: E.pilula(c, "= 10,2% líquidos", W / 2, 820, 100, "g", fundo=CLARO, cor="#07070F", a=q))
    E.saida(c, t, C["s13"] - 0.1, um)
    if t < C["s13"]:
        return
    E.frase(c, t, a13, ps("o imposto é", "i", 72, CLARO) + [("uma fração fixa", "g", 76, BR)] + ps("do rendimento", "i", 72, CLARO), W / 2, 260, "center", 0.12)
    E.frase(c, t, w("s13", "então"), ps("tirar 15% do rendimento ou da taxa:", "i", 64, CLARO) + [("dá no mesmo", "g", 68, BR)], W / 2, 380, "center", 0.1)
    E.frase(c, t, w("s13", "Não"), ps("prazos diferentes ou vários períodos:", "i", 64, CLARO) + [("não compensa", "g", 68, BR)], W / 2, 560, "center", 0.1)
    E.foco(c, t, b13, 0.5, lambda q: E.pilula(c, "calcule o rendimento do período todo em reais", W / 2, 740, 64, "g", fundo=CLARO, cor="#07070F", a=q))


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    a, b_, c_, d = C["s14.a"], C["s14.b"], C["s14.c"], C["s14.d"]
    E.frase(c, t, C["s14"] + 0.3, ps("hora de", "i", 72, COR) + [("testar", "g", 72)], XE, 140)
    E.frase(c, t, a, [("R$ 20.000", "g", 76)] + ps("por 1 ano", "i", 70), XE + 500, 140, "left", 0.15)
    for x, nome, ti, taxa, imp, cor in ((520, "opção A", b_, "12% ao ano", "15% de imposto", ERRADO), (1400, "opção B", c_, "10% ao ano", "sem imposto", CERTO)):
        E.foco(c, t, ti - 0.6, 0.45, lambda q, x=x, nome=nome: E.pilula(c, nome, x, 300, 64, "g", fundo=TINTA, a=q))
        cartao(c, t, ti, x, 470, taxa, None, True, 80)
        E.frase(c, t, ti + 1.2, ps(imp, "i", 56, cor), x, 620, "center", 0.1)
    E.saida(c, t, C["s15"] - 0.1, lambda: E.frase(c, t, d, ps("qual rende mais,", "i", 80) + [("e quanto a mais?", "g", 84, COR)], W / 2, 830, "center", 0.12))
    E.relogio(c, t, C["s15.a"], 960, 820, 100)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    a, b_, c_ = C["s16.a"], C["s16.b"], C["s16.c"]
    a17, b17, c17, d17 = (C["s17." + k] for k in "abcd")
    E.foco(c, t, C["s16"] + 0.3, 0.45, lambda q: E.pilula(c, "opção A", 520, 160, 60, "g", fundo=TINTA, a=q))
    E.frase(c, t, w("s16", "bruto"), ps("bruto:", "i", 60, TINTA2) + [("12% de 20.000", "g", 62)], 520, 290, "center", 0.12)
    E.frase(c, t, a, [("= R$ 2.400", "g", 70)], 520, 380, "center")
    E.frase(c, t, w("s16", "Imposto"), ps("imposto:", "i", 60, TINTA2) + [("240 + 120", "g", 62)], 520, 500, "center", 0.12)
    E.frase(c, t, b_, [("= R$ 360", "g", 70, ERRADO)], 520, 590, "center")
    E.foco(c, t, c_, 0.5, lambda q: E.pilula(c, "líquido: R$ 2.040", 520, 730, 72, "g", a=q))
    E.foco(c, t, C["s17"] + 0.2, 0.45, lambda q: E.pilula(c, "opção B", 1400, 160, 60, "g", fundo=TINTA, a=q))
    E.frase(c, t, C["s17"] + 0.4, [("10% de 20.000", "g", 62)], 1400, 290, "center")
    E.frase(c, t, a17, [("= R$ 2.000", "g", 70)], 1400, 380, "center")
    E.frase(c, t, w("s17", "sem"), ps("sem desconto", "i", 60, CERTO), 1400, 500, "center", 0.1)
    E.foco(c, t, a17 + 0.4, 0.5, lambda q: E.pilula(c, "R$ 2.000", 1400, 730, 72, "g", fundo=TINTA2, a=q))
    E.frase(c, t, b17 - 0.8, ps("A rende mais, por", "i", 70) + [("R$ 40", "g", 84, COR)], W / 2, 870, "center", 0.12)
    E.frase(c, t, w("s17", "Pelo"), ps("atalho:", "i", 60, TINTA2) + [("12% → 10,2% > 10%", "g", 62)], W / 2, 970, "center", 0.12)
    if t >= d17:
        E.foco(c, t, d17, 0.45, lambda q: E.pilula(c, "nem sempre a sem imposto ganha: faça a conta", W / 2, 1040, 44, "g", fundo=TINTA, a=q))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    a18, b18 = C["s18.a"], C["s18.b"]

    def resumo():
        E.frase(c, t, C["s18"] + 0.3, [("resumindo", "i", 92, COR)], W / 2, 210, "center")
        E.frase(c, t, a18, ps("o imposto vale só sobre", "i", 80) + [("o rendimento", "g", 90, COR)], W / 2, 450, "center", 0.14)
        E.frase(c, t, b18, ps("compare sempre", "i", 80) + [("o líquido", "g", 90, COR)], W / 2, 680, "center", 0.14)
    E.saida(c, t, C["s19"] - 0.1, resumo)
    if t < C["s19"]:
        return
    a, b_, c_, d = C["s19.a"], C["s19.b"], C["s19.c"], C["s19.d"]
    E.frase(c, t, C["s19"] + 0.1, [("próxima", "i", 84), ("aula", "i", 84)], XE, 300)
    E.frase(c, t, w("s19", "praticar"), [("Praticando:", "g", 112, COR)], XE, 450)
    E.frase(c, t, a, ps("taxas, inflação, compras a prazo,", "i", 60) + ps("financiamentos e aplicações", "i", 60), XE, 580, "left", 0.08)
    E.frase(c, t, b_, ps("para escolher", "i", 70) + [("a melhor proposta", "g", 76, COR)], XE, 720, "left", 0.12)
    E.foco(c, t, c_, 0.5, lambda q: E.pilula(c, "Inscreva-se", 1520, 300, 72, estilo="g", a=q))
    p = ease_io(prog(t, c_ + 0.3, 0.8))
    E.cursor(c, lerp(1800, 1640, p), lerp(620, 325, p), ep(t, c_ + 0.2, 0.4))
    E.frase(c, t, d, [("bons", "i", 120), ("estudos!", "i", 120, COR)], W / 2, 940, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, nomes=b_nomes, regra=b_regra, compostos=b_compostos, comparar=b_comparar, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
