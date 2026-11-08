"""Visual — Estudativo · MAT-FIN-012: tabelas SAC e Price.

Linguagem da trilha Matemática Financeira, herdada de Porcentagem:
- tabela_fin(): a tabela do financiamento (mês, saldo devedor, juros, amortização, prestação), que se preenche
  célula a célula no tempo da fala; o saldo que fica desce para a linha seguinte.
- prestacao_barra(): a prestação como uma barra com duas partes, juros e amortização.
- cartao() e maquina(): o valor num cartão, como em toda a trilha.
Todo instante vem de C[...] (marcadores do roteiro) e dos tempos reais da voz."""
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Matemática Financeira")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-FIN-012_tabelas_sac_e_price.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("sac", "price", "porque", "atalho", "questao", "fim"))
BR = "#FFFFFF"
PMT = 10000 * 0.02 / (1 - 1.02 ** -10)
assert round(PMT, 2) == 1113.27 and round(PMT - 200) == 913 and round(10000 - (PMT - 200)) == 9087
assert 10000 / 10 == 1000 and 0.02 * 10000 == 200 and 0.02 * 9000 == 180 and 1000 + 200 == 1200 and 1000 + 180 == 1180
assert sum(0.02 * (10000 - 1000 * k) for k in range(10)) == 1100 and round(10 * PMT - 10000) == 1133 and round(10 * PMT, -1) == 11130
assert 1200 - 9 * 20 == 1020 and 0.02 * 1000 == 20
assert 60000 / 60 == 1000 and 0.01 * 60000 == 600 and 1000 + 600 == 1600 and 60000 - 1000 == 59000 and 0.01 * 59000 + 1000 == 1590


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
TX, TY = 130, 250
LARG = [150, 420, 320, 420, 360]
CAB = ["mês", "saldo devedor", "juros", "amortização", "prestação"]
HL = 100


def tabela(c, t, linhas, tl, tc=None, destaque=None):
    tabela_fin(c, t, TX, TY, LARG, CAB, linhas, tl, tc, size=54, h_lin=HL, destaque=destaque)


def desce(c, t, t0, i=0):
    """seta curva do 'saldo que fica' (fim da linha i), por baixo da tabela, até o saldo da linha i + 1; some depois"""
    def seta():
        p = ease_io(prog(t, t0 - 0.5, 0.6))
        if p <= 0:
            return
        x0 = TX + sum(LARG) + 20
        y0 = TY + HL * (i + 1.5)
        x1 = TX + LARG[0] + LARG[1] / 2 + 60
        y1 = TY + HL * (i + 3) - 18
        mx, my = (x0 + x1) / 2 + 200, y1 + 190
        pts = []
        n = 40
        for k in range(int(n * p) + 1):
            u = k / n
            pts.append(((1 - u) ** 2 * x0 + 2 * u * (1 - u) * mx + u * u * x1, (1 - u) ** 2 * y0 + 2 * u * (1 - u) * my + u * u * y1))
        for (ax, ay), (bx, by) in zip(pts, pts[1:]):
            M.line(c, ax, ay, bx, by, E.COR, 1.0, 5)
        if len(pts) > 2 and p > 0.3:
            M.arrow(c, pts[-2][0], pts[-2][1], pts[-1][0], pts[-1][1], E.COR, 1.0, 5, 20)
    E.saida(c, t, t0 + 2.5, seta)


def explica(c, t, itens, y=760, size=64):
    """uma linha de explicação por vez embaixo da tabela: itens = [(t0, [(texto, estilo, tamanho, cor)...])]"""
    for i, (t0, partes) in enumerate(itens):
        fim = itens[i + 1][0] if i + 1 < len(itens) else 1e9
        E.saida(c, t, fim - 0.1, lambda t0=t0, partes=partes: E.frase(c, t, t0, partes, W / 2, y, "center", 0.15))


def prestacao_barra(c, t, x, y, wb, h, fj, tj, ta, a0):
    """a prestação como barra: juros (fração fj, escuro) + amortização (cor da matéria)"""
    q = ep(t, a0, 0.5)
    if q <= 0:
        return
    E.caixa_pontilhada(c, x - 14, y - 14, wb + 28, h + 28, q, prog_=q)
    centro(c, "prestação", x + wb / 2, y - 40, 56, "i", TINTA2, q)
    qj = ep(t, tj, 0.5)
    if qj > 0:
        M.rrect(c, x, y, wb * fj - 6, h, 20, TINTA, qj)
        centro(c, "juros", x + wb * fj / 2, y + h / 2 + 22, 60, "g", BR, qj)
    qa = ep(t, ta, 0.5)
    if qa > 0:
        M.rrect(c, x + wb * fj + 6, y, wb * (1 - fj) - 6, h, 20, E.COR, qa)
        centro(c, "amortização", x + wb * fj + wb * (1 - fj) / 2, y + h / 2 + 22, 60, "g", E.SOBRE, qa)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    ka, kb, kc = C["s01.a"], C["s01.b"], C["s01.c"]

    def um():
        cartao(c, t, ka, 560, 400, "R$ 10.000", "financiamento A", False, 96)
        cartao(c, t, ka + 0.3, 1360, 400, "R$ 10.000", "financiamento B", False, 96)
        E.frase(c, t, kb, ps("mesma taxa,", "i", 76) + ps("mesmo prazo", "i", 76), W / 2, 620, "center", 0.14)
        E.frase(c, t, kc - 0.4, ps("um cobrou", "i", 80) + [("mais juros", "g", 90, COR)], W / 2, 790, "center", 0.14)
        E.frase(c, t, w("s01", "Qual"), [("qual?", "g", 90, COR)] + ps("e por quê?", "i", 84), W / 2, 940, "center", 0.2)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t >= C["s02"]:
        ta, tb = C["s02.a"], C["s02.b"]
        E.foco(c, t, tb - 0.2, 0.7, lambda a: E.bola(c, 1500, 540, 250 * ease_back(prog(t, tb - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, ps("até o fim desta aula", "i", 90), XE, 300, passo=0.14)
        E.frase(c, t, w("s02", "montar"), ps("montar a", "i", 90) + [("1ª linha", "g", 92, COR)], XE, 450, passo=0.14)
        E.frase(c, t, w("s02", "financiamento"), ps("de um financiamento", "i", 80), XE, 570, passo=0.12)
        E.frase(c, t, w("s02", "saber"), ps("e qual", "i", 80) + [("cobra mais juros", "g", 84, COR)], XE, 710, passo=0.12)
        E.foco(c, t, tb + 0.1, 0.5, lambda a: (centro(c, "+ atalho", 1500, 525, 80, "g", E.SOBRE, a),
                                               centro(c, "de prova", 1500, 610, 80, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"] + 0.3, ps("você só precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, w("s03", "uma"), 0.5, lambda a: E.escreve(c, "1", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, w("s03", "coisa"), 0.5, lambda a: E.escreve(c, "coisa", XE + 200, 700, 120, "i", TINTA, a))
    x, wc = 880, 900
    ka, kb = C["s03.a"], C["s03.b"]
    p = ep(t, ka, 0.5)
    E.caixa_pontilhada(c, x, 260, wc, 520, p, prog_=p)
    E.frase(c, t, ka + 0.1, [("juros de um mês", "i", 66)], x + 44, 350)
    E.frase(c, t, w("s03", "taxa"), [("taxa × valor devido", "g", 72, COR)], x + 44, 470)
    E.frase(c, t, w("s03", "Dois"), [("2% de R$ 10.000", "g", 64)], x + 44, 600, "left")
    E.frase(c, t, kb, [("=", "g", 64, TINTA2), ("R$ 200", "g", 72, COR)], x + 44, 700, "left", 0.2)
    q = ease_io(prog(t, kb - 0.35, 0.5))
    E.cursor(c, x + wc - 30, lerp(500, 760, q), ep(t, ka, 0.4))
    E.frase(c, t, w("s03", "Se"), ps("faltou?", "i", 58, COR) + ps("procure no canal", "i", 58), x, 1000, "left", 0.12)


# ---------------- os nomes ----------------
def b_nomes(c, t, C, b):
    a4, b4, c4 = C["s04.a"], C["s04.b"], C["s04.c"]
    a5, b5 = C["s05.a"], C["s05.b"]

    def tela1():
        E.frase(c, t, C["s04"] + 0.3, ps("cada parcela, a", "i", 76) + [("prestação,", "g", 80, COR)] + ps("tem 2 partes", "i", 76),
                W / 2, 190, "center", 0.12)
        prestacao_barra(c, t, 360, 380, 1200, 170, 0.32, b4, c4, a4)
        E.frase(c, t, w("s04", "aluguel"), ps("o aluguel", "i", 58), 360 + 1200 * 0.16, 660, "center", 0.08)
        E.frase(c, t, w("s04", "aluguel") + 0.3, ps("do dinheiro no mês", "i", 58), 360 + 1200 * 0.16, 740, "center", 0.08)
        E.frase(c, t, w("s04", "pedaço"), ps("o pedaço que", "i", 58), 360 + 1200 * 0.66, 660, "center", 0.08)
        E.frase(c, t, w("s04", "abate"), [("abate a dívida", "g", 62, COR)], 360 + 1200 * 0.66, 740, "center", 0.08)
    E.saida(c, t, C["s05"] - 0.1, tela1)
    if t < C["s05"]:
        return
    E.foco(c, t, a5, 0.45, lambda q: E.pilula(c, "saldo devedor", W / 2, 230, 84, "g", a=q))
    E.frase(c, t, a5 + 0.3, ps("o que você ainda deve", "i", 64, TINTA2), W / 2, 360, "center", 0.1)
    q = ep(t, w("s05", "regra"), 0.5)
    E.caixa_pontilhada(c, 240, 470, 1440, 470, q, prog_=q)
    E.frase(c, t, w("s05", "regra"), [("regra de ouro", "g", 60, COR)], W / 2, 560, "center")
    E.frase(c, t, b5, [("juros do mês", "g", 80), ("=", "g", 80, TINTA2), ("taxa × saldo devedor", "g", 80, COR)], W / 2, 710, "center", 0.2)
    E.frase(c, t, w("s05", "não"), ps("e não sobre", "i", 64) + [("o valor que você pegou", "g", 64, ERRADO)], W / 2, 850, "center", 0.12)


# ---------------- SAC ----------------
def b_sac(c, t, C, b):
    a6, b6, c6 = C["s06.a"], C["s06.b"], C["s06.c"]
    a7, b7, c7, d7, e7, f7 = (C["s07." + k] for k in "abcdef")
    a8, b8, c8 = C["s08.a"], C["s08.b"], C["s08.c"]

    def tela1():
        E.foco(c, t, a6, 0.45, lambda q: E.pilula(c, "SAC", W / 2, 250, 130, "g", a=q))
        E.frase(c, t, w("s06", "sistema", 2), ps("sistema de", "i", 72) + [("amortização constante", "g", 76, COR)], W / 2, 440, "center", 0.12)
        E.frase(c, t, b6, ps("constante =", "i", 70) + [("igual todo mês", "g", 74)], W / 2, 560, "center", 0.12)
        E.frase(c, t, w("s06", "Dez"), [("R$ 10.000", "g", 80)] + ps("em", "i", 72) + [("10 meses", "g", 80)], W / 2, 740, "center", 0.15)
        E.frase(c, t, c6, [("R$ 10.000 ÷ 10", "g", 84), ("=", "g", 84, TINTA2), ("R$ 1.000", "g", 90, COR)] + ps("por mês", "i", 72),
                W / 2, 890, "center", 0.2)
    E.saida(c, t, C["s07"] - 0.1, tela1)
    if t < C["s07"]:
        return
    E.frase(c, t, C["s07"] + 0.2, [("SAC", "g", 72, COR)] + ps("·", "i", 72) + [("2% ao mês", "g", 72)], W / 2, 170, "center", 0.2)
    r2 = w("s07", "nove")
    tabela(c, t, [[("1", b7 - 0.3), ("R$ 10.000", b7), ("R$ 200", c7, COR), ("R$ 1.000", d7), ("R$ 1.200", e7, COR)],
                  [("2", r2), ("R$ 9.000", f7), ("R$ 180", a8, COR), ("R$ 1.000", w("s08", "Prestação")), ("R$ 1.180", b8, COR)]],
          [b7 - 0.3, r2], tc=a7)
    desce(c, t, f7)
    explica(c, t, [(w("s07", "Juros"), [("juros:", "i", 62), ("2% de R$ 10.000", "g", 64), ("=", "g", 64, TINTA2), ("R$ 200", "g", 64, COR)]),
                   (w("s07", "Prestação"), [("prestação:", "i", 62), ("R$ 1.000 + R$ 200", "g", 64), ("=", "g", 64, TINTA2), ("R$ 1.200", "g", 64, COR)]),
                   (w("s07", "Saldo", 2), [("saldo que fica:", "i", 62), ("R$ 9.000", "g", 64, COR)]),
                   (w("s08", "juros"), [("juros:", "i", 62), ("2% de R$ 9.000", "g", 64), ("=", "g", 64, TINTA2), ("R$ 180", "g", 64, COR)])])
    E.foco(c, t, c8, 0.45, lambda q: E.pilula(c, "na SAC, a prestação começa alta e vai caindo", W / 2, 920, 56, "g", fundo=TINTA, a=q))


# ---------------- Price ----------------
def b_price(c, t, C, b):
    a9, b9, c9 = C["s09.a"], C["s09.b"], C["s09.c"]
    a10, b10, c10 = C["s10.a"], C["s10.b"], C["s10.c"]

    def tela1():
        E.foco(c, t, a9, 0.45, lambda q: E.pilula(c, "tabela Price", W / 2, 220, 110, "g", a=q))
        E.frase(c, t, b9, ps("todas as prestações", "i", 72) + [("iguais", "g", 80, COR)], W / 2, 400, "center", 0.12)
        for i in range(10):
            x = 380 + i * 120
            E.foco(c, t, b9 + 0.3 + 0.08 * i, 0.4, lambda q, x=x, i=i: (M.rrect(c, x, 470, 84, 220, 14, E.COR, q),
                                                                        centro(c, str(i + 1), x + 42, 740, 40, "b", TINTA2, q)))
        E.frase(c, t, w("s09", "A", 2), ps("a conta da prestação fica para outra aula:", "i", 52, TINTA2), W / 2, 830, "center", 0.06)
        E.frase(c, t, w("s09", "prova"), ps("a prova costuma dar pronta", "i", 52, TINTA2), W / 2, 900, "center", 0.06)
        E.foco(c, t, c9, 0.45, lambda q: E.pilula(c, "≈ R$ 1.113 por mês", W / 2, 1000, 64, "g", a=q))
    E.saida(c, t, C["s10"] - 0.1, tela1)
    if t < C["s10"]:
        return
    E.frase(c, t, C["s10"] + 0.2, [("Price", "g", 72, COR)] + ps("·", "i", 72) + [("2% ao mês", "g", 72)], W / 2, 170, "center", 0.2)
    p0 = w("s10", "Primeira")
    tabela(c, t, [[("1", p0 + 0.3), ("R$ 10.000", w("s10", "saldo")), ("R$ 200", a10, COR), ("≈ R$ 913", w("s10", "dá")), ("≈ R$ 1.113", p0 + 0.6, COR)],
                  [("2", c10 - 0.2), ("≈ R$ 9.087", c10), ("", c10), ("", c10), ("≈ R$ 1.113", c10 + 0.3, COR)]],
          [p0 + 0.3, c10 - 0.2], tc=p0)
    desce(c, t, c10)
    explica(c, t, [(a10, [("juros:", "i", 62), ("2% de R$ 10.000", "g", 64), ("=", "g", 64, TINTA2), ("R$ 200", "g", 64, COR)]),
                   (b10, [("amortização:", "i", 62), ("R$ 1.113 − R$ 200", "g", 64), ("≈", "g", 64, TINTA2), ("R$ 913", "g", 64, COR)]),
                   (w("s10", "Saldo", 2), [("saldo que fica:", "i", 62), ("≈ R$ 9.087", "g", 64, COR)])])


# ---------------- por que a Price cobra mais ----------------
def b_porque(c, t, C, b):
    a11, b11, c11, d11 = C["s11.a"], C["s11.b"], C["s11.c"], C["s11.d"]
    a12, b12 = C["s12.a"], C["s12.b"]

    def tela1():
        E.frase(c, t, C["s11"] + 0.3, ps("saldo depois do", "i", 76) + [("1º mês", "g", 80, COR)], W / 2, 180, "center", 0.12)
        cartao(c, t, a11, 560, 400, "R$ 9.000", "SAC", False, 96)
        cartao(c, t, b11, 1360, 400, "≈ R$ 9.087", "Price", True, 96)
        E.frase(c, t, c11, ps("na Price, a dívida", "i", 70) + [("cai mais devagar", "g", 76, COR)] + ps("no começo", "i", 70), W / 2, 680, "center", 0.12)
        E.frase(c, t, d11, ps("juros sobre uma", "i", 70) + [("dívida maior,", "g", 76)] + ps("por mais tempo", "i", 70), W / 2, 830, "center", 0.12)
    E.saida(c, t, C["s12"] - 0.1, tela1)
    if t < C["s12"]:
        return
    E.frase(c, t, C["s12"] + 0.2, ps("juros no", "i", 76) + [("total", "g", 80, COR)], W / 2, 160, "center", 0.12)
    for x, nome, ti in ((520, "SAC", C["s12"] + 0.5), (1400, "Price", w("s12", "Price"))):
        E.foco(c, t, ti, 0.45, lambda q, x=x, nome=nome: E.pilula(c, nome, x, 290, 72, "g", fundo=TINTA if nome == "SAC" else E.COR, a=q))
    E.frase(c, t, w("s12", "duzentos"), [("200 + 180 + … + 20", "g", 60)], 520, 440, "center")
    E.foco(c, t, a12, 0.5, lambda q: centro(c, "R$ 1.100", 520, 760, 130, "g", TINTA, q))
    E.frase(c, t, w("s12", "dez"), [("10 × R$ 1.113", "g", 60)], 1400, 440, "center")
    E.frase(c, t, w("s12", "somam"), [("≈ R$ 11.130", "g", 60)], 1400, 520, "center")
    E.frase(c, t, w("s12", "Tirando"), [("− R$ 10.000", "g", 60, TINTA2)], 1400, 600, "center")
    E.foco(c, t, b12, 0.5, lambda q: centro(c, "≈ R$ 1.130", 1400, 760, 130, "g", COR, q))
    E.frase(c, t, b12 + 1.0, ps("de juros", "i", 64), 520, 880, "center")
    E.frase(c, t, b12 + 1.0, ps("de juros", "i", 64), 1400, 880, "center")


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    a, b_, c_ = C["s13.a"], C["s13.b"], C["s13.c"]
    E.frase(c, t, C["s13"] + 0.3, [("o erro", "g", 100, ERRADO)] + ps("comum", "i", 96), W / 2, 170, "center", 0.14)
    E.frase(c, t, a, ps("juros sempre sobre", "i", 72) + [("o valor que você pegou", "g", 74, ERRADO)], W / 2, 320, "center", 0.12)
    E.frase(c, t, w("s13", "segundo"), ps("2º mês da SAC:", "i", 66, TINTA2), W / 2, 450, "center")
    E.frase(c, t, w("s13", "faz"), [("2% de R$ 10.000", "g", 84), ("=", "g", 84, TINTA2), ("R$ 200", "g", 84, ERRADO)], W / 2, 580, "center", 0.2)
    if t >= w("s13", "Mas"):
        E.risco(c, 560, 600, 1360, 500, t, w("s13", "Mas"), largura=12)
    E.frase(c, t, w("s13", "Mas"), ps("você já devolveu", "i", 66) + [("R$ 1.000", "g", 70)], W / 2, 720, "center", 0.12)
    E.frase(c, t, c_, [("2% de R$ 9.000", "g", 90), ("=", "g", 90, TINTA2), ("R$ 180", "g", 90, CERTO)], W / 2, 880, "center", 0.2)
    selo_em(c, t, c_ + 1.2, 1600, 845, 52, True)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    a14, b14, c14 = C["s14.a"], C["s14.b"], C["s14.c"]
    a15, b15 = C["s15.a"], C["s15.b"]

    def um():
        E.frase(c, t, C["s14"] + 0.3, [("o atalho", "g", 64, BR)] + ps("da SAC", "i", 68, CLARO), W / 2, 130, "center", 0.2)
        E.frase(c, t, w("s14", "saldo"), ps("o saldo cai", "i", 68, CLARO) + [("R$ 1.000", "g", 72, BR)] + ps("por mês", "i", 68, CLARO), W / 2, 280, "center", 0.12)
        E.frase(c, t, a14, ps("os juros caem", "i", 68, CLARO) + [("2% de R$ 1.000 = R$ 20", "g", 72, BR)], W / 2, 400, "center", 0.12)
        E.frase(c, t, b14, ps("cada prestação:", "i", 68, CLARO) + [("R$ 20 a menos", "g", 72, BR)], W / 2, 540, "center", 0.12)
        vals = ["1.200", "1.180", "1.160", "1.140", "…", "1.020"]
        for i, v in enumerate(vals):
            x = 330 + i * 252
            fundo = CLARO if i == 5 and t >= c14 else "#2A2A3A"
            cor = "#07070F" if fundo == CLARO else BR
            E.foco(c, t, b14 + 0.6 + 0.2 * i, 0.4, lambda q, x=x, v=v, fundo=fundo, cor=cor: E.pilula(c, v, x, 690, 56, "g", fundo=fundo, cor=cor, a=q))
            if i < 4:
                E.foco(c, t, b14 + 0.6 + 0.2 * i, 0.4, lambda q, x=x, i=i: centro(c, f"{i + 1}ª", x, 790, 40, "i", CLARO, q))
        E.foco(c, t, b14 + 1.6, 0.4, lambda q: centro(c, "10ª", 330 + 5 * 252, 790, 40, "i", CLARO, q))
        E.frase(c, t, c14, ps("a 10ª:", "i", 68, CLARO) + [("1.200 − 9 × 20 = 1.020", "g", 76, BR)], W / 2, 940, "center", 0.12)
    E.saida(c, t, C["s15"] - 0.1, um)
    if t < C["s15"]:
        return
    E.frase(c, t, a15, ps("funciona porque a", "i", 72, CLARO) + [("amortização é sempre a mesma", "g", 76, BR)], W / 2, 400, "center", 0.12)
    E.frase(c, t, w("s15", "Não"), ps("na Price, a amortização", "i", 72, CLARO) + [("muda todo mês", "g", 76, BR)], W / 2, 580, "center", 0.12)
    E.foco(c, t, b15 + 0.3, 0.45, lambda q: E.pilula(c, "na Price, não serve", W / 2, 760, 72, "g", fundo=CLARO, cor="#07070F", a=q))


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    a, b_, c_, d = C["s16.a"], C["s16.b"], C["s16.c"], C["s16.d"]
    E.frase(c, t, C["s16"] + 0.3, ps("hora de", "i", 72, COR) + [("testar", "g", 72)], XE, 140)
    cartao(c, t, a, 420, 370, "R$ 60.000", "pela SAC", False, 84)
    cartao(c, t, b_, 960, 370, "60 meses", "prazo", False, 84)
    cartao(c, t, c_, 1500, 370, "1% ao mês", "taxa", True, 84)
    E.saida(c, t, C["s17"] - 0.1, lambda: (
        E.frase(c, t, d, [("1.", "g", 64, COR)] + ps("monte a primeira linha", "i", 68), XE + 160, 640, "left", 0.1),
        E.frase(c, t, w("s16", "diga"), [("2.", "g", 64, COR)] + ps("qual é a", "i", 68) + [("2ª prestação?", "g", 70)], XE + 160, 760, "left", 0.1)))
    E.relogio(c, t, C["s17.a"], 960, 740, 110)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    a, b_, c_, d = C["s18.a"], C["s18.b"], C["s18.c"], C["s18.d"]
    a19, b19, c19 = C["s19.a"], C["s19.b"], C["s19.c"]
    E.frase(c, t, C["s18"] + 0.2, [("SAC", "g", 72, COR)] + ps("·", "i", 72) + [("R$ 60.000 · 60 meses · 1% ao mês", "g", 60)], W / 2, 170, "center", 0.2)
    r2 = w("s18", "Saldo")
    tabela(c, t, [[("1", w("s18", "Amortização")), ("R$ 60.000", w("s18", "Amortização") + 0.2), ("R$ 600", b_, COR), ("R$ 1.000", a + 1.8),
                   ("R$ 1.600", c_, COR)],
                  [("2", r2), ("R$ 59.000", d), ("R$ 590", w("s19", "quinhentos", 2), COR), ("R$ 1.000", c19), ("R$ 1.590", b19, COR)]],
          [w("s18", "Amortização"), r2], tc=C["s18"] + 0.4, destaque={(1, 4): (E.COR, b19)})
    desce(c, t, d)
    explica(c, t, [(a, [("amortização:", "i", 62), ("60.000 ÷ 60", "g", 64), ("=", "g", 64, TINTA2), ("R$ 1.000", "g", 64, COR)]),
                   (w("s18", "Juros"), [("juros:", "i", 62), ("1% de 60.000", "g", 64), ("=", "g", 64, TINTA2), ("R$ 600", "g", 64, COR)]),
                   (w("s18", "Prestação"), [("prestação:", "i", 62), ("R$ 1.000 + R$ 600", "g", 64), ("=", "g", 64, TINTA2), ("R$ 1.600", "g", 64, COR)]),
                   (C["s19"] + 0.3, [("atalho:", "i", 62), ("os juros caem 1% de R$ 1.000", "g", 64), ("=", "g", 64, TINTA2), ("R$ 10", "g", 64, COR)]),
                   (b19, [("2ª prestação:", "i", 62), ("R$ 1.600 − R$ 10", "g", 64), ("=", "g", 64, TINTA2), ("R$ 1.590", "g", 64, COR)]),
                   (w("s19", "Confira"), [("confira:", "i", 62), ("1% de R$ 59.000 = R$ 590", "g", 64), ("+ R$ 1.000", "g", 64, COR)])])
    selo_em(c, t, c19 + 0.8, 1700, 910, 48, True)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    a20, b20 = C["s20.a"], C["s20.b"]

    def resumo():
        E.frase(c, t, C["s20"] + 0.3, [("resumindo", "i", 92, COR)], W / 2, 210, "center")
        E.frase(c, t, a20, ps("juros: sempre sobre o", "i", 80) + [("saldo devedor", "g", 90, COR)], W / 2, 450, "center", 0.14)
        E.frase(c, t, b20, ps("a Price cobra mais:", "i", 76) + [("amortiza menos no começo", "g", 80, COR)], W / 2, 680, "center", 0.14)
    E.saida(c, t, C["s21"] - 0.1, resumo)
    if t < C["s21"]:
        return
    a, b_, c_ = C["s21.a"], C["s21.b"], C["s21.c"]
    E.frase(c, t, C["s21"] + 0.1, [("próxima", "i", 84), ("aula", "i", 84)], XE, 300)
    E.frase(c, t, w("s21", "outro"), [("Rendimento líquido", "g", 112, COR)], XE, 450)
    E.frase(c, t, w("s21", "dinheiro"), ps("o dinheiro que rende", "i", 66), XE, 580, "left", 0.1)
    E.frase(c, t, a, ps("o imposto vale só sobre", "i", 70) + [("o rendimento", "g", 76, COR)], XE, 720, "left", 0.12)
    E.foco(c, t, b_, 0.5, lambda q: E.pilula(c, "Inscreva-se", 1520, 300, 72, estilo="g", a=q))
    p = ease_io(prog(t, b_ + 0.3, 0.8))
    E.cursor(c, lerp(1800, 1640, p), lerp(620, 325, p), ep(t, b_ + 0.2, 0.4))
    E.frase(c, t, c_, [("bons", "i", 120), ("estudos!", "i", 120, COR)], W / 2, 940, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, nomes=b_nomes, sac=b_sac, price=b_price, porque=b_porque, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
