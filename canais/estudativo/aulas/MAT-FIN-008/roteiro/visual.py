"""Visual — Estudativo · MAT-FIN-008: taxa equivalente e taxa efetiva.

Linguagem da trilha Matemática Financeira, herdada de Porcentagem:
- cartao(): o valor num cartão branco. ANTES = contorno escuro; DEPOIS = contorno e número na cor da matéria.
- maquina(): o fator (× 1,1) numa caixa cheia da cor da matéria: é a "máquina" que transforma o dinheiro a cada mês.
- cadeia(): R$ 100 → [× 1,1] → R$ 110 → [× 1,1] → R$ 121, mês a mês; funde(): as duas máquinas viram uma só (× 1,21).
- contrato(): a folha com a frase do banco (12% ao ano, capitalização mensal).
Todo instante vem de C[...] (marcadores do roteiro) e dos tempos reais da voz."""
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Matemática Financeira")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-FIN-008_taxa_equivalente_e_efetiva.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("equivalente", "nominal", "atalho", "questao", "fim"))
BR = "#FFFFFF"
assert round(100 * 1.1, 6) == 110 and round(110 * 1.1, 6) == 121 and round(1.1 ** 2, 6) == 1.21 and round(1.21 ** 0.5, 6) == 1.1
assert round(1.01 ** 12, 4) == 1.1268 and round(1.01 ** 6, 4) == 1.0615 and round(100 * 1.1268, 2) == 112.68
assert 24 / 12 == 2 and round(1.02 ** 12, 2) == 1.27 and 10 + 10 + 10 * 10 / 100 == 21


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
        E.frase(c, t, ka + 0.2, ps("um financiamento cobra", "i", 80) + [("juros ao mês", "g", 80, COR)], W / 2, 200, "center", 0.12)
        fluxo(c, t, 540, "1%", "12 meses", [(kb, "12%?"), (kc, "12,68%")], w("s01", "um"), w("s01", "Em"), kb,
              rot=("ao mês", "em 1 ano"), size=96)
        E.saida(c, t, kc - 0.1, lambda: (E.risco(c, XD - 170, 600, XD + 170, 470, t, w("s01", "Não"), largura=12),
                                         selo_em(c, t, w("s01", "Não"), XD + 200, 400, 48, False)))
        E.frase(c, t, kc + 0.3, [("não", "i", 80), ("12%", "g", 80, ERRADO), ("·", "g", 80, TINTA2),
                                 ("12,68%", "g", 80, COR), ("ao ano", "i", 80)], W / 2, 900, "center", 0.25)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t >= C["s02"]:
        ta, tb = C["s02.a"], C["s02.b"]
        E.foco(c, t, tb - 0.2, 0.7, lambda a: E.bola(c, 1500, 540, 250 * ease_back(prog(t, tb - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, ps("até o fim desta aula", "i", 90), XE, 330, passo=0.14)
        E.frase(c, t, w("s02", "trocar"), ps("trocar", "i", 96) + [("taxa ao mês", "g", 100, COR)], XE, 490, passo=0.14)
        E.frase(c, t, w("s02", "por"), ps("por", "i", 96) + [("taxa ao ano", "g", 100, COR)], XE, 620, passo=0.14)
        E.frase(c, t, w("s02", "sem"), ps("sem cair nessa", "i", 80), XE, 760, passo=0.12)
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
    E.frase(c, t, ka + 0.1, [("juros compostos", "i", 62)], x + 44, 285)
    E.frase(c, t, w("s03", "multiplicado"), [("todo mês:", "i", 64, TINTA2), ("× fator", "g", 64, COR)], x + 44, 375, "left", 0.25)
    E.frase(c, t, w("s03", "um"), [("fator", "g", 64), ("=", "g", 64, TINTA2), ("1 + taxa", "g", 64, COR)], x + 44, 465, "left", 0.25)
    p = ep(t, kb, 0.5)
    E.caixa_pontilhada(c, x, 570, wc, 260, p, prog_=p)
    E.frase(c, t, kb + 0.1, [("expoente fracionário", "i", 62)], x + 44, 655)
    E.foco(c, t, w("s03", "elevar"), 0.45, lambda a: E.formula(c, "9^{1/2} = r{9}", x + 44, 770, 72, "g", COR, a))
    q = ease_io(prog(t, kb - 0.35, 0.5))
    E.cursor(c, x + wc - 30, lerp(470, 800, q), ep(t, ka, 0.4))
    E.frase(c, t, w("s03", "Se"), ps("faltou alguma?", "i", 58, COR) + ps("procure no canal", "i", 58), x, 1000, "left", 0.12)


# ---------------- exemplo de cabeça: 10% em 2 meses ----------------
def b_dois_meses(c, t, C, b):
    a4, b4, c4 = C["s04.a"], C["s04.b"], C["s04.c"]
    a5, b5 = C["s05.a"], C["s05.b"]
    E.frase(c, t, a4, [("10% ao mês", "g", 84, COR)] + ps("durante 2 meses", "i", 84), W / 2, 200, "center", 0.14)
    cadeia(c, t, 520, ["R$ 100", "R$ 110", "R$ 121"], ["× 1,1", "× 1,1"],
           [w("s04", "Cem"), b4, c4], [w("s04", "viram"), w("s04", "segundo")], rot=["hoje", "1º mês", "2º mês"], size=76)
    E.saida(c, t, a5 - 0.2, lambda: E.frase(c, t, w("s04", "valem"), ps("10% sobre", "i", 60) + [("R$ 110", "g", 60, COR)],
                                             1310, 720, "center", 0.12))
    E.saida(c, t, (w("s05", "real") - 0.2) - 0.2, lambda: (
        E.frase(c, t, a5, ps("cresceu", "i", 84) + [("21%", "g", 96, COR)], W / 2, 850, "center", 0.2),
        E.frase(c, t, w("s05", "não"), ps("e não", "i", 84) + [("20%", "g", 96, ERRADO)], W / 2, 970, "center", 0.2)))
    if t >= (w("s05", "real") - 0.2) - 0.2:
        E.frase(c, t, w("s05", "real"), ps("o", "i", 76) + [("R$ 1", "g", 76, COR)] + ps("a mais:", "i", 76), W / 2, 820, "center", 0.12)
        E.frase(c, t, b5, [("juros sobre juros", "g", 84, COR)], W / 2, 930, "center", 0.12)
        E.frase(c, t, w("s05", "dez"), [("10% de R$ 10", "g", 64), ("=", "g", 64, TINTA2), ("R$ 1", "g", 64, COR)], W / 2, 1030, "center", 0.25)


# ---------------- taxa equivalente ----------------
def b_equivalente(c, t, C, b):
    a6, b6 = C["s06.a"], C["s06.b"]
    a7, b7 = C["s07.a"], C["s07.b"]
    y = 400

    def tela1():
        cartao(c, t, C["s06"] + 0.2, 300, y, "R$ 100", None, False, 76)
        cartao(c, t, C["s06"] + 0.4, 1620, y, "R$ 121", None, True, 76)
        funde(c, t, a6, w("s06", "vinte"), 760, 1160, y, "× 1,1", "× 1,1", "× 1,21", size=70)
        p = ep(t, C["s06"] + 0.5, 0.5)
        u = ease_io(prog(t, w("s06", "vinte"), 0.8))
        if p > 0:
            M.arrow(c, 450, y, lerp(600, 780, u), y, TINTA2, p, 5, 18, p)
            M.arrow(c, lerp(1320, 1140, u), y, 1460, y, TINTA2, p, 5, 18, p)
        E.saida(c, t, w("s06", "vinte") - 0.1, lambda: cen(c, t, a6, "10% ao mês, 2 vezes", W / 2, 590, 56, TINTA2, "i"))
        cen(c, t, w("s06", "vinte"), "21% a cada 2 meses", W / 2, 600, 60, COR, "g")
        cen(c, t, w("s06", "capital"), "capital", 300, y - 110, 54, TINTA2, "i")
        cen(c, t, w("s06", "montante"), "montante", 1620, y - 110, 54, COR, "i")
        E.frase(c, t, b6, [("taxas equivalentes:", "g", 76, COR)], W / 2, 780, "center")
        E.frase(c, t, w("s06", "levam"), ps("mesmo capital, mesmo montante, mesmo tempo", "i", 62), W / 2, 880, "center", 0.1)
        E.frase(c, t, w("s06", "Montante"), [("montante", "g", 52, TINTA2), ("=", "g", 52, TINTA2)] + ps("valor final, já com os juros", "i", 52, TINTA2),
                W / 2, 990, "center", 0.1)
    E.saida(c, t, C["s07"] - 0.1, tela1)
    if t < C["s07"]:
        return
    E.frase(c, t, C["s07"] + 0.3, ps("na conta, é só", "i", 84) + [("potência", "g", 90, COR)], W / 2, 200, "center", 0.14)
    E.frase(c, t, a7, [("fator longo", "g", 80, COR), ("=", "g", 80, TINTA2)], 880, 420, "right", 0.2)
    E.formula_em(c, t, w("s07", "fator", 2), "(fator curto)^{n}", 920, 420, 80, "g", TINTA)
    E.frase(c, t, w("s07", "elevado"), [("n", "g", 56, COR), ("=", "g", 56, TINTA2)] + ps("quantas vezes o curto cabe no longo", "i", 56, TINTA2),
            W / 2, 540, "center", 0.1)
    E.formula_em(c, t, b7, "1,1^{2}", 930, 800, 140, "g", TINTA, "right")
    E.formula_em(c, t, w("s07", "um", 3), "= 1,21", 980, 800, 140, "g", COR)


# ---------------- 1% ao mês, durante 1 ano ----------------
TX, TY, TW, TH = 1080, 560, 700, 380  # a tabela do enunciado


def tabela_enunciado(c, t, t0, linhas, destaque=None):
    """caixa pontilhada com as potências que a prova dá; linhas = [(fórmula, valor)]; destaque = (i, t)"""
    p = ep(t, t0, 0.5)
    if p <= 0:
        return
    E.caixa_pontilhada(c, TX, TY, TW, TH, p, prog_=p)
    E.frase(c, t, t0 + 0.1, [("a prova dá", "i", 56, TINTA2)], TX + 40, TY + 80)
    for i, (f, v) in enumerate(linhas):
        yy = TY + 190 + 120 * i
        if destaque and destaque[0] == i:
            q = ep(t, destaque[1], 0.4)
            if q > 0:
                M.rrect(c, TX + 20, yy - 80, TW - 40, 110, 18, E.COR, 0.14 * q)
        E.foco(c, t, t0 + 0.3 + 0.3 * i, 0.45, lambda a, f=f, v=v, yy=yy: (E.formula(c, f, TX + 50, yy, 72, "g", TINTA, a),
                                                                          E.escreve(c, "≈ " + v, TX + 360, yy, 72, "g", COR, a)))


def b_um_ano(c, t, C, b):
    a8, b8, c8 = C["s08.a"], C["s08.b"], C["s08.c"]
    a9, b9, c9 = C["s09.a"], C["s09.b"], C["s09.c"]
    linhas = [("1,01^{6}", "1,0615"), ("1,01^{12}", "1,1268")]

    def tela1():
        E.frase(c, t, w("s08", "um"), [("1% ao mês", "g", 84, COR)] + ps("durante 1 ano", "i", 84), W / 2, 200, "center", 0.14)
        E.frase(c, t, w("s08", "fator"), ps("fator mensal", "i", 70), XE, 420)
        E.formula_em(c, t, a8, "1,01", XE + 480, 420, 96, "g", COR)
        E.frase(c, t, w("s08", "tem"), ps("12 meses", "i", 70), XE, 640)
        E.formula_em(c, t, b8, "1,01^{12}", XE + 480, 650, 130, "g", TINTA)
        E.frase(c, t, w("s08", "Essa"), ps("de cabeça? ninguém faz", "i", 56, TINTA2), XE, 820, "left", 0.1)
        tabela_enunciado(c, t, c8, linhas)
    E.saida(c, t, a9 + 0.6, tela1)
    if t < a9 + 0.6:
        return
    E.formula_em(c, t, a9 + 0.6, "1,01^{12} ≈ 1,1268", W / 2, 230, 100, "g", TINTA, "center")
    fluxo(c, t, 500, "R$ 100", "× 1,1268", "R$ 112,68", w("s09", "Vezes"), w("s09", "Vezes") + 0.4, w("s09", "cento"),
          rot=("capital", "em 1 ano"), size=76)
    E.saida(c, t, w("s09", "O") - 0.2, lambda: E.frase(c, t, w("s09", "Doze", 2), [("R$ 12,68", "g", 80, COR)] + ps("em cada", "i", 80) + [("R$ 100", "g", 80)],
                                                        W / 2, 760, "center", 0.15))
    E.frase(c, t, b9, [("=", "g", 110, TINTA2), ("12,68%", "g", 120, COR), ("ao ano", "i", 100)], W / 2, 900 if t < w("s09", "O") - 0.2 else 760, "center", 0.2)
    E.frase(c, t, w("s09", "O"), ps("o que passou de 12:", "i", 70) + [("juros sobre juros", "g", 76, COR)], W / 2, 930, "center", 0.12)


# ---------------- caminho de volta ----------------
def b_volta(c, t, C, b):
    a, b_, c_, d = C["s10.a"], C["s10.b"], C["s10.c"], C["s10.d"]
    y = 440
    E.frase(c, t, C["s10"] + 0.3, ps("e o caminho", "i", 84) + [("de volta?", "g", 84, COR)], W / 2, 180, "center", 0.14)
    cartao(c, t, a, 420, y, "21%", "a cada 2 meses", False, 92)
    cartao(c, t, w("s10", "Quanto"), 1500, y, [(w("s10", "Quanto"), "?"), (w("s10", "dez"), "10%")], "ao mês", True, 92)
    maquina(c, t, w("s10", "fator"), 960, y, [(w("s10", "fator"), "?"), (c_, "√")], 84)
    p = ep(t, w("s10", "fator") - 0.1, 0.5)
    if p > 0:
        M.arrow(c, 590, y, 800, y, TINTA2, p, 6, 20, p)
        M.arrow(c, 1120, y, 1330, y, TINTA2, p, 6, 20, p)
    E.frase(c, t, w("s10", "fator"), ps("fator mensal", "i", 64, TINTA2), W / 2, 680, "center")
    eq_f(c, t, [("1,21^{1/2}", TINTA, b_), ("=", TINTA2, c_), ("r{1,21}", TINTA, c_ + 0.2), ("=", TINTA2, d), ("1,1", COR, d + 0.1)], W / 2, 850, 110)
    E.frase(c, t, w("s10", "dez") + 0.3, [("10% ao mês", "g", 70, COR)], W / 2, 1000, "center")


# ---------------- taxa nominal e efetiva ----------------
XS12 = [250, 580, 910, 1270, 1650]
def b_nominal(c, t, C, b):
    a11, b11 = C["s11.a"], C["s11.b"]
    a12, b12, c12, d12 = C["s12.a"], C["s12.b"], C["s12.c"], C["s12.d"]
    a13, b13 = C["s13.a"], C["s13.b"]

    def tela1():
        E.frase(c, t, C["s11"] + 0.3, ps("a frase do", "i", 72) + [("contrato", "g", 72, COR)], W / 2, 160, "center", 0.14)
        contrato(c, t, a11, W / 2, 440, 1100, 380, [("12% ao ano", "g", TINTA, 110), ("com capitalização mensal", "i", COR, 72)])
        E.frase(c, t, w("s11", "Capitalização", 2), ps("capitalização mensal =", "i", 60, TINTA2), W / 2, 740, "center", 0.1)
        E.frase(c, t, b11, ps("os juros entram na conta", "i", 64) + [("todo mês", "g", 64, COR)], W / 2, 830, "center", 0.12)
        for i in range(12):
            x = lerp(330, 1590, i / 11)
            E.foco(c, t, b11 + 0.6 + 0.12 * i, 0.4, lambda a, x=x, i=i: (E.bola(c, x, 960, 40, a=a),
                                                                          centro(c, str(i + 1), x, 960 + 16, 44, "g", E.SOBRE, a)))
    E.saida(c, t, C["s12"] - 0.1, tela1)
    if C["s12"] <= t < C["s13"]:
        def tela2():
            cadeia(c, t, 470, ["12%", "1%", "12,68%"], ["÷ 12", "1,01¹²"], [w("s12", "doze"), b12, c12],
                   [w("s12", "divide"), w("s12", "isso")], rot=["ao ano", "ao mês", "ao ano"], size=80, xs=XS12)
            xs = XS12
            E.foco(c, t, a12, 0.45, lambda a: E.pilula(c, "taxa nominal", xs[0] + 40, 700, 56, "g", fundo=TINTA, a=a))
            cen(c, t, w("s12", "só"), "só um rótulo", xs[0] + 40, 800, 52, TINTA2, "i")
            cen(c, t, w("s12", "compostos"), "juros compostos", xs[3], 640, 46, TINTA2, "i")
            E.foco(c, t, d12, 0.45, lambda a: E.pilula(c, "taxa efetiva", xs[4] - 40, 700, 56, "g", a=a))
            cen(c, t, w("s12", "paga"), "a que você paga", xs[4] - 40, 800, 52, COR, "i")
        E.saida(c, t, C["s13"] - 0.1, tela2)
    if t < C["s13"]:
        return
    E.frase(c, t, C["s13"] + 0.3, ps("a receita:", "i", 84) + [("2 passos", "g", 84, COR)], XE, 190, "left", 0.14)
    E.passo(c, t, a13, 1, "divida a taxa nominal", "pelo número de períodos", 380)
    E.passo(c, t, b13, 2, "eleve o fator", "a esse número de períodos", 560)
    E.frase(c, t, w("s13", "Tire"), ps("tire o 1 da frente:", "i", 70), XE, 780, "left", 0.12)
    E.frase(c, t, w("s13", "frente"), [("1,1268", "g", 96), ("→", "g", 96, TINTA2)], XE, 920, "left", 0.25)
    E.frase(c, t, w("s13", "sobra"), [("12,68%", "g", 110, COR)], XE + 480, 920, "left")
    E.foco(c, t, w("s13", "efetiva"), 0.45, lambda a: E.pilula(c, "taxa efetiva", 1300, 890, 60, "g", a=a))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    a, b_, c_ = C["s14.a"], C["s14.b"], C["s14.c"]
    E.frase(c, t, C["s14"] + 0.3, [("o erro", "g", 100, ERRADO)] + ps("comum", "i", 96), W / 2, 180, "center", 0.14)
    E.frase(c, t, a, ps("multiplicar a taxa", "i", 76) + [("pelo tempo", "g", 76, ERRADO)], W / 2, 340, "center", 0.12)
    E.frase(c, t, w("s14", "um"), [("1% × 12", "g", 120), ("=", "g", 120, TINTA2), ("12%", "g", 120, ERRADO)], W / 2, 530, "center", 0.3)
    E.foco(c, t, b_, 0.45, lambda q: E.pilula(c, "isso é juros simples", W / 2, 680, 66, "g", fundo=TINTA, a=q))
    E.frase(c, t, w("s14", "em"), ps("os juros não rendem juros", "i", 60, TINTA2), W / 2, 790, "center", 0.1)
    E.frase(c, t, c_ - 0.9, ps("nos compostos:", "i", 76), W / 2, 930, "center", 0.12)
    E.frase(c, t, c_, ps("a efetiva sai", "i", 76) + [("sempre maior", "g", 80, COR)], W / 2, 1030, "center", 0.12)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    a15, b15, c15 = C["s15.a"], C["s15.b"], C["s15.c"]
    a16, b16, c16 = C["s16.a"], C["s16.b"], C["s16.c"]

    def regra():
        E.frase(c, t, C["s15"] + 0.3, [("o atalho", "g", 64, BR), ("para 2 períodos", "i", 68, CLARO)], W / 2, 130, "center", 0.2)
        E.linha(c, t, [("taxa + taxa", "g", 84, BR, a15), ("+", "g", 84, CLARO, w("s15", "some", 2)),
                       ("taxa × taxa ÷ 100", "g", 84, CLARO, w("s15", "vezes"))], W / 2, 360, "center")
        E.frase(c, t, w("s15", "Dez"), [("10 + 10", "g", 96, BR), ("=", "g", 96, CLARO), ("20", "g", 96, BR)], W / 2, 560, "center", 0.25)
        E.frase(c, t, b15, [("10 × 10 ÷ 100", "g", 96, BR), ("=", "g", 96, CLARO), ("1", "g", 96, BR)], W / 2, 730, "center", 0.25)
        E.foco(c, t, c15, 0.5, lambda a: E.pilula(c, "20 + 1 = 21%", W / 2, 900, 100, "g", fundo=CLARO, cor="#07070F", a=a))
    E.saida(c, t, C["s16"] - 0.1, regra)
    if t < C["s16"]:
        return
    E.frase(c, t, a16, ps("são", "i", 76, CLARO) + [("2 aumentos seguidos", "g", 76, BR)], W / 2, 190, "center", 0.12)
    E.frase(c, t, w("s16", "segundo"), ps("o 2º vale também sobre o 1º", "i", 64, CLARO), W / 2, 300, "center", 0.1)
    E.frase(c, t, w("s16", "Não"), ps("12 meses?", "i", 70, CLARO), 700, 470, "right")
    E.foco(c, t, b16, 0.45, lambda a: E.pilula(c, "use a tabela", 1000, 445, 64, "g", fundo=CLARO, cor="#07070F", a=a))
    q = ep(t, w("s16", "Mas"), 0.5)
    E.caixa_pontilhada(c, 300, 600, 1320, 420, q, CLARO, prog_=q)
    E.frase(c, t, w("s16", "guarde"), [("a pista", "g", 60, BR)] + ps("indo para um período mais longo:", "i", 60, CLARO), W / 2, 690, "center", 0.1)
    E.frase(c, t, c16, ps("alternativa", "i", 76, CLARO) + [("≤ taxa × tempo", "g", 84, BR)], W / 2, 830, "center", 0.15)
    E.frase(c, t, w("s16", "está"), [("está errada", "g", 84, ERRADO)], W / 2, 960, "center")


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    a, b_, c_ = C["s17.a"], C["s17.b"], C["s17.c"]
    E.frase(c, t, C["s17"] + 0.3, ps("hora de", "i", 72, COR) + [("testar", "g", 72)], XE, 150)
    contrato(c, t, a, 820, 400, 1060, 340, [("24% ao ano", "g", TINTA, 110), ("com capitalização mensal", "i", COR, 66)], "anúncio do banco")
    E.frase(c, t, b_, ps("o enunciado dá:", "i", 64, TINTA2), XE, 700)
    E.formula_em(c, t, w("s17", "um", 2), "1,02^{12} ≈ 1,27", XE + 520, 710, 96, "g", TINTA)
    E.saida(c, t, C["s18"] - 0.1, lambda: E.frase(c, t, c_, ps("qual é a", "i", 80) + [("taxa efetiva ao ano?", "g", 80, COR)],
                                                   W / 2, 900, "center", 0.14))
    E.relogio(c, t, C["s18.a"], 1600, 820, 110)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    a, b_, c_, d = C["s19.a"], C["s19.b"], C["s19.c"], C["s19.d"]
    a20, b20 = C["s20.a"], C["s20.b"]

    def conta():
        E.passo(c, t, w("s19", "Passo"), 1, "divida", "pelo número de meses", 220)
        E.frase(c, t, a, [("24% ÷ 12", "g", 84), ("=", "g", 84, TINTA2), ("2% ao mês", "g", 84, COR)], XE + 108, 400, "left", 0.25)
        E.frase(c, t, b_, ps("fator mensal:", "i", 66, TINTA2), XE + 108, 500)
        E.formula_em(c, t, b_ + 0.3, "1,02", XE + 560, 500, 84, "g", COR)
        E.passo(c, t, w("s19", "Passo", 2), 2, "eleve o fator", "a 12 meses", 640)
        E.formula_em(c, t, c_, "1,02^{12}", XE + 108, 830, 110, "g", TINTA)
        E.formula_em(c, t, w("s19", "como"), "≈ 1,27", XE + 420, 830, 110, "g", COR)
        E.frase(c, t, w("s19", "tabela"), ps("(tabela)", "i", 52, TINTA2), XE + 108, 930)
        E.frase(c, t, d, ps("tire o inteiro:", "i", 64, TINTA2), 1520, 450, "center", 0.1)
        E.foco(c, t, w("s19", "vinte", 3), 0.5, lambda q: num_bola(c, "27%", 1520, 640, 170, 110, q))
        E.frase(c, t, w("s19", "ao", 2), ps("ao ano", "i", 70), 1520, 900, "center")
    E.saida(c, t, C["s20"] - 0.1, conta)
    if t < C["s20"]:
        return
    E.frase(c, t, C["s20"] + 0.2, ps("bate com", "i", 84) + [("a pista", "g", 84, COR)], W / 2, 230, "center", 0.14)
    E.frase(c, t, a20, [("27%", "g", 140, COR), (">", "g", 140, TINTA2), ("24%", "g", 140)], W / 2, 500, "center", 0.3)
    selo_em(c, t, w("s20", "maior") + 0.6, 1480, 450, 56, True)
    E.frase(c, t, w("s20", "Quem"), [("24%?", "g", 90, ERRADO)], W / 2, 760, "center")
    E.frase(c, t, b20, ps("leu só", "i", 84) + [("o rótulo", "g", 84, ERRADO)], W / 2, 900, "center", 0.14)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    a21, b21 = C["s21.a"], C["s21.b"]

    def resumo():
        E.frase(c, t, C["s21"] + 0.3, [("resumindo", "i", 92, COR)], W / 2, 210, "center")
        E.frase(c, t, a21, ps("nos juros compostos,", "i", 80), W / 2, 400, "center", 0.12)
        E.frase(c, t, w("s21", "taxa"), [("taxa × tempo", "g", 110, ERRADO)], W / 2, 560, "center")
        if t >= w("s21", "multiplica"):
            E.risco(c, 600, 590, 1320, 480, t, w("s21", "multiplica"), largura=14)
        E.frase(c, t, b21, ps("eleve", "i", 130) + [("o fator", "g", 130, COR)], W / 2, 820, "center", 0.2)
    E.saida(c, t, C["s22"] - 0.1, resumo)
    if t < C["s22"]:
        return
    a, b_, c_, d, e = C["s22.a"], C["s22.b"], C["s22.c"], C["s22.d"], C["s22.e"]
    E.frase(c, t, C["s22"] + 0.1, [("próxima", "i", 84), ("aula", "i", 84)], XE, 300)
    E.frase(c, t, a - 0.6, [("Inflação acumulada", "g", 112, COR)], XE, 450)
    E.frase(c, t, a - 0.3, [("e poder de compra", "g", 112, COR)], XE, 580)
    E.frase(c, t, w("s22", "cinco"), [("5% e 4%", "g", 76)] + ps("não dão", "i", 76) + [("9%", "g", 76, ERRADO)], XE, 740, "left", 0.2)
    E.foco(c, t, d, 0.5, lambda q: E.pilula(c, "Inscreva-se", 1520, 300, 72, estilo="g", a=q))
    p = ease_io(prog(t, d + 0.3, 0.8))
    E.cursor(c, lerp(1800, 1640, p), lerp(620, 325, p), ep(t, d + 0.2, 0.4))
    E.frase(c, t, e, [("bons", "i", 120), ("estudos!", "i", 120, COR)], W / 2, 940, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, dois_meses=b_dois_meses, equivalente=b_equivalente, um_ano=b_um_ano,
              volta=b_volta, nominal=b_nominal, erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
