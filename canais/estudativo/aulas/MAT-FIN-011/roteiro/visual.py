"""Visual — Estudativo · MAT-FIN-011: à vista ou a prazo.

Linguagem da trilha Matemática Financeira, herdada de Porcentagem:
- linha_tempo(): a seta das datas (hoje, 1 mês, 2 meses); pagamento(): a pílula do valor pago naquela data.
- cadeia(): o dinheiro aplicado mês a mês (R$ 1.000 → × 1,05 → R$ 1.050 → × 1,05 → R$ 1.102,50), embaixo da linha do tempo.
- fluxo(): o saldo que fica com a loja virando a parcela (R$ 100 → R$ 110).
Todo instante vem de C[...] (marcadores do roteiro) e dos tempos reais da voz."""
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Matemática Financeira")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-FIN-011_a_vista_ou_a_prazo.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("datas", "embutida", "atalho", "questao", "fim"))
BR = "#FFFFFF"
assert round(1000 * 1.05, 6) == 1050 and round(1050 * 0.05, 6) == 52.5 and round(1050 + 52.5, 6) == 1102.5 and round(1102.5 - 1100, 6) == 2.5
assert round(1000 * 1.01 ** 2) == 1020 and 200 - 100 == 100 and (110 - 100) / 100 == 0.10 and 100 + 110 == 210 and 10 / 200 == 0.05
assert 900 - 500 == 400 and (500 - 400) / 400 == 0.25 and round(100 / 900 * 100) == 11


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
LX0, LX1 = 440, 1780  # linhas do tempo com duas formas de pagar


def forma(c, t, t0, y, nome, rotulos, tm=None, cor=None):
    """uma forma de pagar: nome à esquerda e a linha do tempo; devolve os x dos tiques"""
    E.foco(c, t, t0, 0.45, lambda a: E.escreve(c, nome, XE, y + 22, 62, "i", cor or TINTA, a))
    return linha_tempo(c, t, t0, LX0, LX1, y, rotulos, tm, size=50)


def pag(c, t, x, y, itens, cor=None, alto=120, size=58):
    """pílula de pagamento que pode trocar de valor: itens = [(t0, texto)] ou [(t0, texto, t_sai)]"""
    for i, it in enumerate(itens):
        t0, s = it[0], it[1]
        fim = it[2] if len(it) > 2 else (itens[i + 1][0] if i + 1 < len(itens) else 1e9)
        E.saida(c, t, fim - 0.05, lambda t0=t0, s=s: pagamento(c, t, t0, x, y, s, cor, alto, size), d=0.3)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    ka, kb, kc = C["s01.a"], C["s01.b"], C["s01.c"]

    def um():
        xs = forma(c, t, ka, 380, "à vista", ["hoje", "1 mês"], [ka, kb])
        pag(c, t, xs[0], 380, [(w("s01", "duzentos"), "R$ 200")], TINTA)
        forma(c, t, kb - 0.3, 740, "a prazo", ["hoje", "1 mês"], [kb, w("s01", "daqui")])
        pag(c, t, xs[0], 740, [(kb, "R$ 100")])
        pag(c, t, xs[1], 740, [(w("s01", "cento"), "R$ 110")])
        E.saida(c, t, kc - 0.1, lambda: E.frase(c, t, w("s01", "Parece"), ps("parece só", "i", 76) + [("5%", "g", 84)] + ps("a mais", "i", 76),
                                                 W / 2, 960, "center", 0.14))
        E.frase(c, t, kc, ps("são", "i", 76) + [("10% de juros ao mês", "g", 84, COR)], W / 2, 960, "center", 0.14)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t >= C["s02"]:
        ta, tb = C["s02.a"], C["s02.b"]
        E.foco(c, t, tb - 0.2, 0.7, lambda a: E.bola(c, 1500, 540, 250 * ease_back(prog(t, tb - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, ps("até o fim desta aula", "i", 90), XE, 300, passo=0.14)
        E.frase(c, t, w("s02", "comparar"), ps("comparar", "i", 90) + [("datas diferentes", "g", 92, COR)], XE, 450, passo=0.14)
        E.frase(c, t, w("s02", "achar"), ps("achar os", "i", 90) + [("juros escondidos", "g", 92, COR)], XE, 590, passo=0.14)
        E.frase(c, t, w("s02", "compra"), ps("na compra a prazo", "i", 80), XE, 720, passo=0.12)
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
    E.caixa_pontilhada(c, x, 170, wc, 360, p, prog_=p)
    E.frase(c, t, ka + 0.1, [("juros compostos", "i", 62)], x + 44, 255)
    E.frase(c, t, w("s03", "levar"), ps("para a frente:", "i", 60, TINTA2) + [("× fator", "g", 66, COR)], x + 44, 360, "left", 0.15)
    E.frase(c, t, w("s03", "trazer"), ps("para hoje:", "i", 60, TINTA2) + [("÷ fator", "g", 66, COR)], x + 44, 460, "left", 0.15)
    p = ep(t, kb, 0.5)
    E.caixa_pontilhada(c, x, 580, wc, 270, p, prog_=p)
    E.frase(c, t, kb + 0.1, [("variação percentual", "i", 62)], x + 44, 665)
    E.frase(c, t, w("s03", "diferença"), [("diferença ÷ valor de antes", "g", 62, COR)], x + 44, 780)
    q = ease_io(prog(t, kb - 0.35, 0.5))
    E.cursor(c, x + wc - 30, lerp(500, 820, q), ep(t, ka, 0.4))
    E.frase(c, t, w("s03", "Se"), ps("faltou alguma?", "i", 58, COR) + ps("procure no canal", "i", 58), x, 1000, "left", 0.12)


# ---------------- comparar na mesma data ----------------
XS3 = [260, 617, 975, 1332, 1690]  # hoje, máquina, 1 mês, máquina, 2 meses


def b_datas(c, t, C, b):
    a4, b4 = C["s04.a"], C["s04.b"]
    a5, b5, c5 = C["s05.a"], C["s05.b"], C["s05.c"]
    a6, b6 = C["s06.a"], C["s06.b"]
    a7, b7, c7 = C["s07.a"], C["s07.b"], C["s07.c"]
    a8, b8, c8, d8 = C["s08.a"], C["s08.b"], C["s08.c"], C["s08.d"]
    y = 520

    def tela1():
        E.saida(c, t, C["s05"] - 0.1, lambda: E.frase(c, t, a4, ps("datas diferentes:", "i", 76) + [("não se compara direto", "g", 76, COR)],
                                                       W / 2, 180, "center", 0.12))
        xs = linha_tempo(c, t, w("s04", "Mil") - 0.4, 200, 1800, y, ["hoje", "1 mês", "2 meses"], size=50)
        pag(c, t, xs[0], y, [(w("s04", "Mil"), "R$ 1.000")], TINTA)
        pag(c, t, xs[2], y, [(b4, "R$ 1.100")])
        E.saida(c, t, C["s05"] - 0.1, lambda: E.frase(c, t, w("s04", "Depende"), ps("depende de quanto o seu dinheiro", "i", 70) + [("rende", "g", 76, COR)],
                                                       W / 2, 820, "center", 0.12))
        if t >= C["s05"]:
            E.saida(c, t, C["s07"] - 0.1, lambda: (
                E.frase(c, t, b5, ps("o seu dinheiro rende", "i", 72) + [("5% ao mês", "g", 80, COR)], W / 2, 170, "center", 0.12),
                E.frase(c, t, w("s05", "alta"), ps("(taxa alta, só para a conta sair redonda)", "i", 48, TINTA2), W / 2, 250, "center", 0.06)))
            q = ep(t, c5, 0.5)
            E.caixa_pontilhada(c, xs[2] - 190, y - 230, 380, 360, q, prog_=q)
            E.saida(c, t, C["s07"] - 0.1, lambda: E.foco(c, t, c5 + 0.2, 0.4, lambda q: E.pilula(c, "mesma data", xs[2], y + 175, 46, "g", fundo=TINTA, a=q)))
        cadeia(c, t, 800, ["R$ 1.000", "R$ 1.050", "R$ 1.102,50"], ["× 1,05", "× 1,05"], [w("s06", "Aplicados"), a6, b6],
               [w("s06", "viram"), w("s06", "segundo")], xs=XS3, size=62)
        E.saida(c, t, C["s07"] - 0.1, lambda: E.frase(c, t, w("s06", "cinco"), [("5% de R$ 1.050", "g", 56), ("=", "g", 56, TINTA2), ("R$ 52,50", "g", 56, COR)],
                                                       W / 2, 970, "center", 0.2))
        if t >= C["s07"]:
            q = ep(t, a7, 0.4)
            if q > 0:
                M.rrect(c, XS3[4] - 190, 720, 380, 160, 26, E.COR, 0.12 * q)
            E.frase(c, t, a7, ps("você tem", "i", 52, COR), XS3[4], 700, "center")
            E.linha(c, t, [("R$ 1.102,50 − R$ 1.100", "g", 66, TINTA, b7), ("=", "g", 66, TINTA2, w("s07", "sobram")),
                           ("sobram R$ 2,50", "g", 66, CERTO, w("s07", "sobram") + 0.2)], W / 2, 990, "center")
            E.foco(c, t, c7, 0.45, lambda q: E.pilula(c, "pagar a prazo é melhor", W / 2, 180, 66, "g", a=q))
    E.saida(c, t, C["s08"] - 0.1, tela1)
    if t < C["s08"]:
        return
    E.frase(c, t, C["s08"] + 0.3, [("a regra", "g", 80, COR)], W / 2, 170, "center")
    E.frase(c, t, a8, ps("leve todos os valores para", "i", 72) + [("a mesma data", "g", 76, COR)], W / 2, 320, "center", 0.12)
    E.frase(c, t, w("s08", "com"), ps("com a taxa que o seu dinheiro rende", "i", 60, TINTA2), W / 2, 410, "center", 0.1)
    E.frase(c, t, b8, ps("só então,", "i", 84) + [("compare", "g", 96, COR)], W / 2, 560, "center", 0.14)
    E.frase(c, t, c8, ps("se rendesse", "i", 64) + [("1% ao mês:", "g", 68)], 820, 760, "right", 0.12)
    E.frase(c, t, w("s08", "mil", 1), [("R$ 1.000", "g", 72), ("→", "g", 72, TINTA2), ("≈ R$ 1.020", "g", 72, COR)], 860, 760, "left", 0.25)
    E.foco(c, t, d8, 0.45, lambda q: E.pilula(c, "pagar à vista ganharia", W / 2, 910, 66, "g", fundo=TINTA, a=q))


# ---------------- juros embutidos ----------------
def b_embutida(c, t, C, b):
    a9, b9 = C["s09.a"], C["s09.b"]
    a10, b10, c10, d10 = C["s10.a"], C["s10.b"], C["s10.c"], C["s10.d"]
    y1, y2 = 340, 650
    E.frase(c, t, C["s09"] + 0.3, ps("os juros", "i", 72) + [("escondidos", "g", 76, COR)], W / 2, 120, "center", 0.12)
    xs = forma(c, t, a9, y1, "à vista", ["hoje", "1 mês"], [a9, a9 + 0.1])
    pag(c, t, xs[0], y1, [(a9, "R$ 200"), (a10, "R$ 100")], TINTA)
    forma(c, t, w("s09", "ou"), y2, "a prazo", ["hoje", "1 mês"], [w("s09", "ou"), w("s09", "ou") + 0.1])
    pag(c, t, xs[0], y2, [(w("s09", "cem"), "R$ 100", C["s10"] - 0.2)])
    pag(c, t, xs[1], y2, [(w("s09", "cento"), "R$ 110")])
    # a entrada é igual nas duas: sai das duas
    if b9 <= t < C["s10"]:
        def entrada():
            q = ep(t, b9, 0.5)
            E.caixa_pontilhada(c, xs[0] - 170, y1 - 185, 340, y2 - y1 + 225, q, prog_=q)
            E.foco(c, t, b9 + 0.2, 0.4, lambda a: E.pilula(c, "a entrada: R$ 100 nas duas", W / 2, y2 + 200, 60, "g", fundo=TINTA, a=a))
            E.frase(c, t, w("s09", "tire"), [("− R$ 100", "g", 60, ERRADO)], xs[0] + 140, y1 - 100, "left")
            E.frase(c, t, w("s09", "tire") + 0.3, [("− R$ 100", "g", 60, ERRADO)], xs[0] + 140, y2 - 100, "left")
        E.saida(c, t, C["s10"] - 0.2, entrada)
    if t < C["s10"]:
        return
    E.frase(c, t, a10, ps("faltariam hoje", "i", 50, TINTA2), xs[0], y1 + 160 - 40 + 40, "center")
    p = ease_io(prog(t, w("s10", "pegar"), 0.8))
    if p > 0:
        M.arrow(c, xs[0] + 120, y1 - 120, lerp(xs[0] + 120, xs[1] - 120, p), lerp(y1 - 120, y2 - 120, p), E.COR, 1.0, 6, 22, 1.0)
    E.foco(c, t, w("s10", "pegar"), 0.45, lambda q: E.pilula(c, "pegar R$ 100 e devolver R$ 110", W / 2 + 40, (y1 + y2) / 2 - 150, 46, "g", fundo=TINTA2, a=q))
    E.frase(c, t, w("s10", "Dez", 3), [("R$ 10 ÷ R$ 100", "g", 80), ("=", "g", 80, TINTA2)], 1060, 910, "right", 0.2)
    E.frase(c, t, c10, [("10% ao mês", "g", 90, COR)], 1100, 910, "left")
    E.foco(c, t, d10, 0.45, lambda q: E.pilula(c, "taxa de juros embutida", W / 2, 1015, 56, "g", a=q))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    a, b_, c_ = C["s11.a"], C["s11.b"], C["s11.c"]
    E.frase(c, t, C["s11"] + 0.3, [("o erro", "g", 100, ERRADO)] + ps("comum", "i", 96), W / 2, 170, "center", 0.14)
    E.frase(c, t, w("s11", "comparar"), ps("comparar com o", "i", 66) + [("preço inteiro", "g", 70, ERRADO)], W / 2, 290, "center", 0.12)
    E.frase(c, t, a, [("R$ 100 + R$ 110", "g", 90), ("=", "g", 90, TINTA2), ("R$ 210", "g", 90)], W / 2, 450, "center", 0.25)
    E.frase(c, t, b_, [("10 ÷ 200", "g", 90), ("=", "g", 90, TINTA2), ("5%", "g", 90, ERRADO)], W / 2, 600, "center", 0.25)
    if t >= c_:
        E.risco(c, 700, 620, 1220, 520, t, c_, largura=12)
    E.frase(c, t, c_, ps("a entrada", "i", 76) + [("não foi emprestada", "g", 80, COR)], W / 2, 780, "center", 0.12)
    E.frase(c, t, w("s11", "Os"), ps("juros só sobre o que", "i", 70) + [("ficou para depois", "g", 74, COR)], W / 2, 910, "center", 0.12)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    a12, b12, c12 = C["s12.a"], C["s12.b"], C["s12.c"]
    a13, b13 = C["s13.a"], C["s13.b"]

    def regra():
        E.frase(c, t, C["s12"] + 0.3, [("o atalho", "g", 64, BR)] + ps("entrada + 1 parcela", "i", 68, CLARO), W / 2, 140, "center", 0.2)
        E.frase(c, t, a12, [("saldo", "g", 90, BR), ("=", "g", 90, CLARO), ("à vista − entrada", "g", 84, CLARO)], W / 2, 320, "center", 0.2)
        E.frase(c, t, b12, [("parcela ÷ saldo", "g", 90, BR)], W / 2, 480, "center")
        E.frase(c, t, w("s12", "passar"), ps("o que passar de 1", "i", 66, CLARO) + [("é a taxa", "g", 70, BR)], W / 2, 600, "center", 0.12)
        E.frase(c, t, c12, [("110 ÷ 100", "g", 100, BR), ("=", "g", 100, CLARO), ("1,1", "g", 100, BR)], W / 2, 790, "center", 0.25)
        E.foco(c, t, w("s12", "dez", 2), 0.5, lambda q: E.pilula(c, "10%", W / 2, 930, 90, "g", fundo=CLARO, cor="#07070F", a=q))
    E.saida(c, t, C["s13"] - 0.1, regra)
    if t < C["s13"]:
        return
    E.frase(c, t, a13, ps("o saldo é o único dinheiro que", "i", 70, CLARO) + [("fica com a loja", "g", 74, BR)], W / 2, 300, "center", 0.12)
    E.frase(c, t, w("s13", "Não"), ps("várias parcelas, meses diferentes:", "i", 66, CLARO) + [("não compensa", "g", 70, BR)], W / 2, 520, "center", 0.12)
    E.foco(c, t, b13, 0.5, lambda q: E.pilula(c, "leve tudo para a mesma data", W / 2, 720, 80, "g", fundo=CLARO, cor="#07070F", a=q))


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    a, b_, c_, d = C["s14.a"], C["s14.b"], C["s14.c"], C["s14.d"]
    E.frase(c, t, C["s14"] + 0.3, ps("hora de", "i", 72, COR) + [("testar", "g", 72)], XE, 130)
    E.frase(c, t, w("s14", "geladeira"), ps("uma geladeira", "i", 64, TINTA2), XE + 490, 130)
    y1, y2 = 340, 620
    xs = forma(c, t, a, y1, "à vista", ["hoje", "30 dias"], [a, a + 0.1])
    pag(c, t, xs[0], y1, [(a, "R$ 900")], TINTA)
    forma(c, t, b_, y2, "a prazo", ["no ato", "30 dias"], [b_, w("s14", "outra")])
    pag(c, t, xs[0], y2, [(w("s14", "uma", 2), "R$ 500")])
    pag(c, t, xs[1], y2, [(w("s14", "outra"), "R$ 500")])
    E.saida(c, t, C["s15"] - 0.1, lambda: (
        E.frase(c, t, c_, [("1.", "g", 62, COR)] + ps("qual é a taxa embutida?", "i", 66), XE + 160, 840, "left", 0.1),
        E.frase(c, t, d, [("2.", "g", 62, COR)] + ps("rendendo", "i", 66) + [("1% ao mês,", "g", 66)] + ps("qual vale mais a pena?", "i", 66),
                XE + 160, 950, "left", 0.1)))
    E.relogio(c, t, C["s15.a"], 960, 820, 100)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    a, b_, c_ = C["s16.a"], C["s16.b"], C["s16.c"]
    a17, b17, c17 = C["s17.a"], C["s17.b"], C["s17.c"]

    def conta():
        E.frase(c, t, w("s16", "parcela"), ps("a parcela no ato", "i", 66) + [("é a entrada", "g", 70, COR)], W / 2, 170, "center", 0.12)
        E.frase(c, t, a, ps("saldo:", "i", 72) + [("900 − 500 = 400", "g", 84)], W / 2, 320, "center", 0.15)
        fluxo(c, t, 560, "R$ 400", [(b_, "?"), (c_, "+ 25%")], "R$ 500", w("s16", "quatrocentos"), b_, b_ + 0.3,
              rot=("fica com a loja", "daqui a 1 mês"), size=84)
        E.frase(c, t, w("s16", "Cem"), [("100 ÷ 400", "g", 90), ("=", "g", 90, TINTA2)], 1000, 840, "right", 0.2)
        E.frase(c, t, c_, [("25% ao mês", "g", 96, COR)], 1040, 840, "left")
    E.saida(c, t, C["s17"] - 0.1, conta)
    if t < C["s17"]:
        return
    E.frase(c, t, C["s17"] + 0.3, [("25%", "g", 130, COR)] + ps("ao mês", "i", 90) + [(">", "g", 110, TINTA2), ("1%", "g", 130)],
            W / 2, 330, "center", 0.2)
    E.foco(c, t, b17, 0.45, lambda q: E.pilula(c, "melhor pagar à vista", W / 2, 510, 80, "g", a=q))
    E.frase(c, t, w("s17", "Quem"), ps("quem dividiu", "i", 70) + [("100 ÷ 900", "g", 80)] + ps("achou", "i", 70) + [("≈ 11%", "g", 80, ERRADO)],
            W / 2, 770, "center", 0.12)
    if t >= w("s17", "errou"):
        E.risco(c, 1290, 800, 1580, 700, t, w("s17", "errou"), largura=12)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    a18, b18 = C["s18.a"], C["s18.b"]

    def resumo():
        E.frase(c, t, C["s18"] + 0.3, [("resumindo", "i", 92, COR)], W / 2, 210, "center")
        E.frase(c, t, a18, ps("compare sempre", "i", 84) + [("na mesma data", "g", 96, COR)], W / 2, 450, "center", 0.14)
        E.frase(c, t, b18, ps("juros só sobre o que", "i", 76) + [("fica para depois", "g", 84, COR)], W / 2, 680, "center", 0.14)
    E.saida(c, t, C["s19"] - 0.1, resumo)
    if t < C["s19"]:
        return
    a, b_, c_, d = C["s19.a"], C["s19.b"], C["s19.c"], C["s19.d"]
    E.frase(c, t, C["s19"] + 0.1, [("próxima", "i", 84), ("aula", "i", 84)], XE, 300)
    E.frase(c, t, a - 0.3, [("Tabelas SAC e Price", "g", 112, COR)], XE, 450)
    E.frase(c, t, a, ps("as parcelas de um financiamento", "i", 66), XE, 580, "left", 0.1)
    E.frase(c, t, b_, ps("na", "i", 72) + [("Price,", "g", 76)] + ps("mais juros que na", "i", 72) + [("SAC", "g", 76, COR)], XE, 720, "left", 0.15)
    E.foco(c, t, c_, 0.5, lambda q: E.pilula(c, "Inscreva-se", 1520, 300, 72, estilo="g", a=q))
    p = ease_io(prog(t, c_ + 0.3, 0.8))
    E.cursor(c, lerp(1800, 1640, p), lerp(620, 325, p), ep(t, c_ + 0.2, 0.4))
    E.frase(c, t, d, [("bons", "i", 120), ("estudos!", "i", 120, COR)], W / 2, 940, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, datas=b_datas, embutida=b_embutida, erro=b_erro, atalho=b_atalho,
              questao=b_questao, resposta=b_resposta, fim=b_fim)
