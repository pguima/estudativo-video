"""Visual — Estudativo · MAT-FIN-010: taxa real de juros.

Linguagem da trilha Matemática Financeira, herdada de Porcentagem:
- cartao() e maquina(): o valor num cartão e a variação (+ 10%, × 1,05) na máquina da cor da matéria.
- fluxo() e cadeia(): o dinheiro passando pelas máquinas, como aumentos seguidos.
- a barra dos R$ 100 ganhos: metade cobre a inflação, metade é o ganho de verdade.
Todo instante vem de C[...] (marcadores do roteiro) e dos tempos reais da voz."""
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia
from fractions import Fraction as Fr

E.usar("Matemática", "Matemática Financeira")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-FIN-010_taxa_real_de_juros.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("exemplo", "regra", "atalho", "questao", "fim"))
BR = "#FFFFFF"
assert round(1000 * 1.1, 6) == 1100 and round(1000 * 1.05, 6) == 1050 and Fr(50, 1050) == Fr(1, 21) and 100 // 21 == 4 and 100 % 21 == 16
assert round(100 / 21, 1) == 4.8 and Fr(110, 105) == Fr(22, 21) == 1 + Fr(1, 21) and 1.04 / 1.05 < 1
assert round(100 * 1.05 * 1.05, 2) == 110.25 and round(130 / 120, 3) == 1.083 and Fr(126, 120) == Fr(105, 100) and 126 - 120 == 6 and 6 / 120 == 0.05
assert round(1.05 * 1.2, 6) == 1.26


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


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    ka, kb, kc = C["s01.a"], C["s01.b"], C["s01.c"]

    def um():
        cartao(c, t, w("s01", "dez"), 560, 330, "+ 10%", "a aplicação rendeu", True, 100)
        cartao(c, t, w("s01", "cinco"), 1360, 330, "5%", "a inflação foi", False, 100)
        E.frase(c, t, w("s01", "Você"), ps("ficou", "i", 84) + [("5%", "g", 96)] + ps("mais rico?", "i", 84), W / 2, 640, "center", 0.14)
        if t >= w("s01", "Não"):
            E.saida(c, t, kc - 0.1, lambda: E.risco(c, 640, 670, 1280, 570, t, w("s01", "Não"), largura=12))
        E.foco(c, t, kc, 0.5, lambda a: num_bola(c, "≈ 4,8%", W / 2, 860, 175, 78, a))
    E.saida(c, t, C["s02"] - 0.1, um)
    if t >= C["s02"]:
        ta, tb = C["s02.a"], C["s02.b"]
        E.foco(c, t, tb - 0.2, 0.7, lambda a: E.bola(c, 1500, 540, 250 * ease_back(prog(t, tb - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, ps("até o fim desta aula", "i", 90), XE, 330, passo=0.14)
        E.frase(c, t, w("s02", "descontar"), ps("descontar", "i", 96) + [("a inflação", "g", 100, COR)], XE, 490, passo=0.14)
        E.frase(c, t, w("s02", "qualquer"), ps("de qualquer rendimento", "i", 80), XE, 630, passo=0.12)
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
    E.frase(c, t, ka + 0.1, [("juntar variações seguidas", "i", 62)], x + 44, 285)
    E.frase(c, t, w("s03", "multiplicando"), [("× fator", "g", 72, COR), ("× fator", "g", 72, COR)], x + 44, 420, "left", 0.3)
    p = ep(t, kb, 0.5)
    E.caixa_pontilhada(c, x, 570, wc, 260, p, prog_=p)
    E.frase(c, t, kb + 0.1, [("achar o valor de antes", "i", 62)], x + 44, 655)
    E.frase(c, t, w("s03", "dividindo"), [("÷ fator", "g", 72, COR)], x + 44, 770)
    q = ease_io(prog(t, kb - 0.35, 0.5))
    E.cursor(c, x + wc - 30, lerp(470, 800, q), ep(t, ka, 0.4))
    E.frase(c, t, w("s03", "Se"), ps("faltou alguma?", "i", 58, COR) + ps("procure no canal", "i", 58), x, 1000, "left", 0.12)


# ---------------- aparente e real ----------------
def b_nomes(c, t, C, b):
    a, b_ = C["s04.a"], C["s04.b"]
    cen(c, t, w("s04", "dez"), "10%", 560, 380, 170, TINTA)
    E.foco(c, t, a, 0.45, lambda q: E.pilula(c, "taxa aparente", 560, 540, 70, "g", fundo=TINTA, a=q))
    E.frase(c, t, w("s04", "quanto"), ps("quanto o número", "i", 60), 560, 690, "center", 0.1)
    E.frase(c, t, w("s04", "número") + 0.3, ps("na conta cresceu", "i", 60), 560, 780, "center", 0.1)
    cen(c, t, b_, "?", 1360, 380, 170, COR)
    E.foco(c, t, b_, 0.45, lambda q: E.pilula(c, "taxa real", 1360, 540, 70, "g", a=q))
    E.frase(c, t, w("s04", "quanto", 2), ps("quanto cresceu", "i", 60), 1360, 690, "center", 0.1)
    E.frase(c, t, w("s04", "dinheiro"), ps("o que o dinheiro", "i", 60) + [("compra", "g", 62, COR)], 1360, 780, "center", 0.1)


# ---------------- exemplo com R$ 1.000 ----------------
def b_exemplo(c, t, C, b):
    a5, b5, c5 = C["s05.a"], C["s05.b"], C["s05.c"]
    a6, b6, c6 = C["s06.a"], C["s06.b"], C["s06.c"]
    a7, b7, c7 = C["s07.a"], C["s07.b"], C["s07.c"]

    def tela1():
        fluxo(c, t, 330, "R$ 1.000", "+ 10%", "R$ 1.100", a5, w("s05", "dez"), b5, rot=("você tinha", "na conta"), size=80)
        fluxo(c, t, 760, "R$ 1.000", "+ 5%", "R$ 1.050", w("s05", "custava"), w("s05", "cinco"), c5, rot=("custava", "agora custa"), size=80)
        cen(c, t, w("s05", "inflação"), "inflação", XM, 620, 52, TINTA2, "i")
    E.saida(c, t, C["s06"] - 0.1, tela1)
    if C["s06"] <= t < C["s07"]:
        def tela2():
            E.frase(c, t, C["s06"] + 0.3, ps("você ganhou", "i", 80) + [("R$ 100", "g", 90, COR)], W / 2, 200, "center", 0.14)
            x0, wb, y, h = 360, 1200, 330, 150
            q = ep(t, a6, 0.5)
            if q > 0:
                M.rrect(c, x0, y, wb / 2 - 8, h, 22, CINZA, q)
                centro(c, "R$ 50", x0 + wb / 4, y + h / 2 + 30, 84, "g", BR, q)
            E.frase(c, t, a6 + 0.3, ps("só cobriram a inflação", "i", 54, TINTA2), x0 + wb / 4, y + h + 80, "center", 0.08)
            q = ep(t, b6, 0.5)
            if q > 0:
                M.rrect(c, x0 + wb / 2 + 8, y, wb / 2 - 8, h, 22, E.COR, q)
                centro(c, "R$ 50", x0 + wb * 3 / 4, y + h / 2 + 30, 84, "g", E.SOBRE, q)
            E.frase(c, t, b6 + 0.2, [("ganho de verdade", "g", 56, COR)], x0 + wb * 3 / 4, y + h + 80, "center")
            E.frase(c, t, c6, [("R$ 50", "g", 90, COR)] + ps("sobre", "i", 84) + [("R$ 1.050", "g", 90)], W / 2, 790, "center", 0.2)
            E.frase(c, t, w("s06", "que", 2), ps("o que você precisava ter", "i", 58, TINTA2) + [("só para empatar", "g", 58, TINTA2)],
                    W / 2, 900, "center", 0.1)
        E.saida(c, t, C["s07"] - 0.1, tela2)
    if t < C["s07"]:
        return
    eq_f(c, t, [("f{50}{1050}", TINTA, a7), ("=", TINTA2, b7), ("f{1}{21}", COR, b7 + 0.2)], W / 2, 290, 110)
    E.frase(c, t, w("s07", "Simplificando"), ps("÷ 50 em cima e embaixo", "i", 52, TINTA2), W / 2, 460, "center", 0.08)
    E.frase(c, t, w("s07", "cem"), ps("em %:", "i", 70) + [("100 ÷ 21", "g", 84)], 760, 620, "right", 0.15)
    E.frase(c, t, w("s07", "cabe"), [("= 4", "g", 84), ("e sobram", "i", 70), ("16", "g", 84)], 800, 620, "left", 0.2)
    E.frase(c, t, w("s07", "segue"), ps("depois da vírgula:", "i", 66, TINTA2) + [("4,76...", "g", 84)], 760, 760, "center", 0.15)
    E.foco(c, t, c7, 0.5, lambda q: num_bola(c, "≈ 4,8%", 1530, 690, 175, 78, q))
    E.frase(c, t, w("s07", "pouco"), ps("um pouco menos que", "i", 64), 900, 940, "right", 0.1)
    E.formula_em(c, t, w("s07", "vigésimo") - 0.2, "f{1}{20} = 5%", 940, 960, 80, "g", TINTA)


# ---------------- a regra com fatores ----------------
def b_regra(c, t, C, b):
    a8, b8, c8 = C["s08.a"], C["s08.b"], C["s08.c"]
    a9, b9, c9 = C["s09.a"], C["s09.b"], C["s09.c"]
    a10, b10, c10 = C["s10.a"], C["s10.b"], C["s10.c"]

    def tela1():
        E.frase(c, t, C["s08"] + 0.3, ps("a regra,", "i", 72) + [("com fatores", "g", 72, COR)], W / 2, 140, "center", 0.12)
        E.linha(c, t, [("aparente", "g", 84, TINTA, w("s08", "fator")), ("=", "g", 84, TINTA2, a8), ("real", "g", 84, COR, w("s08", "real")),
                       ("×", "g", 84, TINTA2, w("s08", "vezes")), ("inflação", "g", 84, TINTA, w("s08", "inflação"))], W / 2, 290, "center")
        E.linha(c, t, [("real", "g", 96, COR, w("s08", "real", 2)), ("=", "g", 96, TINTA2, b8), ("aparente", "g", 96, TINTA, b8 + 0.3),
                       ("÷", "g", 96, TINTA2, w("s08", "pelo")), ("inflação", "g", 96, TINTA, w("s08", "pelo") + 0.3)], W / 2, 450, "center")
        if t >= b8 + 0.2:
            q = ep(t, b8, 0.5)
            E.caixa_pontilhada(c, 300, 350, 1320, 140, q, prog_=q)
        E.frase(c, t, c8, [("1,1 ÷ 1,05", "g", 96)], 900, 650, "right")
        E.frase(c, t, a9, [("=", "g", 96, TINTA2), ("110 ÷ 105", "g", 96)], 940, 650, "left", 0.2)
        E.frase(c, t, w("s09", "Ande"), ps("ande 2 casas", "i", 52, TINTA2), 700, 750, "center")
        E.frase(c, t, b9, [("=", "g", 96, TINTA2), ("22 ÷ 21", "g", 96)], 900, 870, "right", 0.2)
        E.foco(c, t, w("s09", "Simplificando"), 0.4, lambda q: centro(c, "÷ 5", 1410, 750, 52, "i", TINTA2, q))
        E.formula_em(c, t, c9, "= 1 f{1}{21}", 940, 885, 96, "g", COR)
        E.foco(c, t, w("s09", "ganho"), 0.45, lambda q: E.pilula(c, "real ≈ 4,8%", 1530, 860, 64, "g", a=q))
    E.saida(c, t, C["s10"] - 0.1, tela1)
    if t < C["s10"]:
        return
    E.frase(c, t, C["s10"] + 0.3, ps("e se a inflação", "i", 80) + [("passar do rendimento?", "g", 80, COR)], W / 2, 180, "center", 0.12)
    cartao(c, t, a10, 560, 400, "+ 4%", "rendeu", True, 90)
    cartao(c, t, w("s10", "inflação", 2), 1360, 400, "5%", "inflação", False, 90)
    E.frase(c, t, w("s10", "fator"), ps("fator real:", "i", 70), 640, 650, "right")
    E.frase(c, t, w("s10", "fator") + 0.2, [("1,04 ÷ 1,05", "g", 90)], 680, 650, "left")
    E.frase(c, t, b10, [("< 1", "g", 100, ERRADO)], 1300, 650)
    E.frase(c, t, w("s10", "número"), ps("a conta subiu, mas", "i", 70) + [("você compra menos", "g", 76, COR)], W / 2, 810, "center", 0.12)
    E.foco(c, t, w("s10", "taxa"), 0.45, lambda q: E.pilula(c, "taxa real negativa", W / 2, 940, 70, "g", fundo=ERRADO, a=q))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    a, b_, c_ = C["s11.a"], C["s11.b"], C["s11.c"]
    E.frase(c, t, C["s11"] + 0.3, [("o erro", "g", 100, ERRADO)] + ps("comum", "i", 96), W / 2, 160, "center", 0.14)
    E.frase(c, t, a, ps("subtrair:", "i", 80) + [("10% − 5% = 5%", "g", 96, ERRADO)], W / 2, 330, "center", 0.15)
    E.frase(c, t, w("s11", "Teste"), [("teste:", "g", 60, COR)] + ps("5% real e depois 5% de inflação", "i", 58), W / 2, 450, "center", 0.1)
    xs = [230, 560, 890, 1220, 1600]
    cadeia(c, t, 640, ["R$ 100", "R$ 105", "R$ 110,25"], ["× 1,05", "× 1,05"], [w("s11", "Cem"), w("s11", "cento"), b_],
           [w("s11", "cinco", 3), w("s11", "cinco", 4)], xs=xs, size=70)
    cen(c, t, w("s11", "real"), "real", xs[1], 760, 48, TINTA2, "i")
    cen(c, t, w("s11", "inflação"), "inflação", xs[3], 760, 48, TINTA2, "i")
    E.frase(c, t, c_ - 1.3, ps("o rendimento teria de ser", "i", 70) + [("10,25%", "g", 84, COR)], W / 2, 900, "center", 0.12)
    E.frase(c, t, w("s11", "não"), ps("e não", "i", 70) + [("10%", "g", 84, ERRADO)], W / 2, 1010, "center", 0.12)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    a12, b12, c12 = C["s12.a"], C["s12.b"], C["s12.c"]
    a13, b13, c13, d13 = C["s13.a"], C["s13.b"], C["s13.c"], C["s13.d"]

    def um():
        E.frase(c, t, C["s12"] + 0.3, [("o atalho", "g", 64, BR)] + ps("para conferir", "i", 68, CLARO), W / 2, 150, "center", 0.2)
        E.frase(c, t, a12, ps("a subtração", "i", 80, CLARO) + [("confere", "g", 84, BR)], W / 2, 330, "center", 0.14)
        E.frase(c, t, w("s12", "taxas"), ps("taxas pequenas:", "i", 66, CLARO), W / 2, 480, "center")
        E.frase(c, t, b12, ps("a real fica", "i", 66, CLARO) + [("um pouco abaixo", "g", 70, BR)] + ps("da diferença", "i", 66, CLARO), W / 2, 580, "center", 0.12)
        E.frase(c, t, w("s12", "Dez"), [("10 − 5 = 5", "g", 110, BR)], W / 2, 780, "center")
        E.foco(c, t, c12, 0.5, lambda q: E.pilula(c, "real: um pouco abaixo de 5%", W / 2, 920, 70, "g", fundo=CLARO, cor="#07070F", a=q))
    E.saida(c, t, C["s13"] - 0.1, um)
    if t < C["s13"]:
        return
    E.frase(c, t, C["s13"] + 0.3, ps("dividir pela inflação", "i", 70, CLARO) + [("encolhe um pouco", "g", 74, BR)] + ps("o ganho", "i", 70, CLARO),
            W / 2, 160, "center", 0.12)
    E.frase(c, t, w("s13", "Não"), ps("taxas altas:", "i", 70, CLARO) + [("não compensa", "g", 74, BR)], W / 2, 300, "center", 0.12)
    cartao(c, t, b13, 560, 530, "+ 30%", None, False, 80)
    cen(c, t, b13, "rendeu", 560, 430, 56, CLARO, "i")
    cartao(c, t, w("s13", "inflação", 2), 1360, 530, "20%", None, False, 80)
    cen(c, t, w("s13", "inflação", 2), "inflação", 1360, 430, 56, CLARO, "i")
    E.frase(c, t, w("s13", "diferença"), ps("diferença:", "i", 66, CLARO) + [("10", "g", 84, BR)], 560, 760, "center", 0.12)
    if t >= w("s13", "mas") + 0.3:
        E.risco(c, 620, 780, 740, 700, t, w("s13", "mas") + 0.3, largura=10)
    E.frase(c, t, c13, ps("real:", "i", 66, CLARO) + [("130 ÷ 120", "g", 84, BR)], 1300, 760, "center", 0.12)
    E.frase(c, t, w("s13", "cerca"), [("≈ 8,3%", "g", 90, CLARO)], 1300, 870, "center")
    E.foco(c, t, d13, 0.5, lambda q: E.pilula(c, "faça a divisão", W / 2, 985, 72, "g", fundo=CLARO, cor="#07070F", a=q))


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    a, b_, c_ = C["s14.a"], C["s14.b"], C["s14.c"]
    E.frase(c, t, C["s14"] + 0.3, ps("hora de", "i", 72, COR) + [("testar", "g", 72)], XE, 150)
    cartao(c, t, a, 560, 400, "+ 26%", "o investimento rendeu", True, 100)
    cartao(c, t, b_, 1360, 400, "20%", "inflação acumulada", False, 100)
    cen(c, t, w("s14", "dois"), "em 2 anos", W / 2, 580, 60, TINTA2, "i")
    E.saida(c, t, C["s15"] - 0.1, lambda: E.frase(c, t, c_, ps("qual foi a", "i", 84) + [("taxa real?", "g", 90, COR)], W / 2, 820, "center", 0.14))
    E.relogio(c, t, C["s15.a"], 960, 780, 110)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    a, b_, c_, d = C["s16.a"], C["s16.b"], C["s16.c"], C["s16.d"]
    a17, b17 = C["s17.a"], C["s17.b"]

    def conta():
        E.frase(c, t, w("s16", "Divida"), ps("divida os fatores:", "i", 66, TINTA2), XE, 230)
        E.frase(c, t, a, [("1,26 ÷ 1,2", "g", 96)], XE + 560, 235)
        E.frase(c, t, w("s16", "Ande"), ps("ande 2 casas:", "i", 66, TINTA2), XE, 390)
        E.frase(c, t, b_, [("126 ÷ 120", "g", 96)], XE + 560, 395)
        E.frase(c, t, w("s16", "Cento", 3), [("120", "g", 76)] + ps("cabe 1 vez, sobram", "i", 70) + [("6", "g", 76, COR)], XE, 560, "left", 0.15)
        E.frase(c, t, w("s16", "Seis", 4), [("6", "g", 84, COR), ("=", "g", 84, TINTA2), ("5% de 120", "g", 84)], XE, 710, "left", 0.2)
        E.frase(c, t, d, ps("fator", "i", 70) + [("1,05", "g", 90, COR)], XE, 870, "left", 0.15)
        E.foco(c, t, w("s16", "taxa"), 0.5, lambda q: num_bola(c, "5%", 1520, 520, 170, 120, q))
        E.frase(c, t, w("s16", "real"), ps("real nos 2 anos", "i", 64), 1520, 790, "center", 0.1)
    E.saida(c, t, C["s17"] - 0.1, conta)
    if t < C["s17"]:
        return
    E.frase(c, t, C["s17"] + 0.3, ps("confira", "i", 84, COR), W / 2, 230, "center")
    E.frase(c, t, a17, [("1,05 × 1,2", "g", 110), ("=", "g", 110, TINTA2), ("1,26", "g", 110, CERTO)], W / 2, 470, "center", 0.3)
    selo_em(c, t, w("s17", "Bateu"), 1640, 430, 56, True)
    E.frase(c, t, w("s17", "Quem"), ps("quem subtraiu:", "i", 76) + [("26 − 20 = 6%", "g", 90, ERRADO)], W / 2, 760, "center", 0.12)
    if t >= w("s17", "errou"):
        E.risco(c, 900, 790, 1520, 690, t, w("s17", "errou"), largura=12)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    a18, b18 = C["s18.a"], C["s18.b"]

    def resumo():
        E.frase(c, t, C["s18"] + 0.3, [("resumindo", "i", 92, COR)], W / 2, 210, "center")
        E.frase(c, t, a18, [("real", "g", 110, COR), ("=", "g", 110, TINTA2), ("aparente", "g", 110), ("÷", "g", 110, TINTA2), ("inflação", "g", 110)],
                W / 2, 470, "center", 0.25)
        E.frase(c, t, b18, ps("subtrair: só para", "i", 84) + [("conferir", "g", 90, COR)], W / 2, 720, "center", 0.14)
    E.saida(c, t, C["s19"] - 0.1, resumo)
    if t < C["s19"]:
        return
    a, b_, c_, d = C["s19.a"], C["s19.b"], C["s19.c"], C["s19.d"]
    E.frase(c, t, C["s19"] + 0.1, [("próxima", "i", 84), ("aula", "i", 84)], XE, 300)
    E.frase(c, t, a - 0.3, [("À vista ou a prazo", "g", 112, COR)], XE, 450)
    E.frase(c, t, a, ps("os juros escondidos na compra a prazo", "i", 64), XE, 580, "left", 0.1)
    E.frase(c, t, w("s19", "duzentos"), [("R$ 200", "g", 76)] + ps("à vista ou", "i", 70) + [("R$ 100 + R$ 110", "g", 76, COR)], XE, 720, "left", 0.2)
    E.foco(c, t, c_, 0.5, lambda q: E.pilula(c, "Inscreva-se", 1520, 300, 72, estilo="g", a=q))
    p = ease_io(prog(t, c_ + 0.3, 0.8))
    E.cursor(c, lerp(1800, 1640, p), lerp(620, 325, p), ep(t, c_ + 0.2, 0.4))
    E.frase(c, t, d, [("bons", "i", 120), ("estudos!", "i", 120, COR)], W / 2, 940, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, nomes=b_nomes, exemplo=b_exemplo, regra=b_regra, erro=b_erro, atalho=b_atalho,
              questao=b_questao, resposta=b_resposta, fim=b_fim)
