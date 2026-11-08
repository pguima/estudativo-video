"""Visual — Estudativo · MAT-FIN-007: praticando juros simples e compostos.

Linguagem da trilha Matemática Financeira, herdada de Porcentagem (e a mesma da prática MAT-FIN-014):
- situacao(): a pílula "situação n" no alto, com o assunto da aula que ela treina.
- cartao(): o valor num cartão branco. ANTES = contorno escuro; DEPOIS = contorno e número na cor da matéria.
- maquina(): a operação ou o fator (÷ 12, × 1,3) na caixa da cor da matéria; cadeia(): a ida mês a mês ou ano a ano.
- coluna(): simples (preto) × compostos (índigo) lado a lado, como em MAT-FIN-005.
Todo instante vem de C[...] (marcadores do roteiro) e dos tempos reais da voz."""
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Matemática Financeira")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-FIN-007_praticando_juros.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("questao1", "questao2", "questao3", "questao4", "questao5", "atalho", "fim"))
BR = "#FFFFFF"
assert 18 / 12 == 1.5 and 1.5 * 8 == 12 and round(2500 * 0.12, 6) == 300 and 250 + 50 == 300 and 2500 + 300 == 2800
assert 1040 - 800 == 240 and 240 / 6 == 40 and 40 / 800 == 0.05
assert round(1200 * 0.02, 6) == 24 and round(1200 * 0.005, 6) == 6 and round(1200 * 0.025, 6) == 30 and 1200 + 24 + 6 == 1230
assert round(5000 * 0.12, 6) == 600 and round(5000 * 1.1268, 6) == 5634 and 634 - 600 == 34 and round(1.01 ** 12, 4) == 1.1268
assert round(1.3 ** 2, 6) == 1.69 and round(8450 / 1.69, 6) == 5000 and 845000 / 169 == 5000 and round(5000 * 1.3, 6) == 6500 and round(6500 * 1.3, 6) == 8450
assert 100 / 8 == 12.5 and 72 / 8 == 9


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



# ---------------- peças da prática ----------------
def pil(c, t, t0, s, cx, cy, size=60, fundo=None, cor=BR, est="g"):
    E.foco(c, t, t0, 0.45, lambda a: E.pilula(c, s, cx, cy, size, est, fundo=fundo, cor=cor, a=a))


def situacao(c, t, t0, n, assunto):
    """a pílula da situação no alto, com o assunto da aula que ela treina"""
    E.foco(c, t, t0, 0.45, lambda q: E.pilula(c, f"situação {n}", XE + 170, 130, 58, "g", a=q))
    E.foco(c, t, t0 + 0.3, 0.45, lambda q: E.escreve(c, assunto, XE + 380, 150, 52, "i", TINTA2, q))


def pausa(c, t, t0, cx=1600, cy=760, r=100):
    E.relogio(c, t, t0, cx, cy, r)


def seta(c, t, t0, x0, x1, y):
    p = ep(t, t0, 0.5)
    if p > 0:
        M.arrow(c, x0, y, lerp(x0, x1, p), y, TINTA2, p, 6, 22, p)


def coluna(c, t, x, th, nome, linhas, y0=300):
    """uma coluna do duelo: pílula com o nome e as linhas [(texto, t0[, cor, tamanho])] da conta"""
    comp = nome == "compostos"
    pil(c, t, th, nome, x, y0, 58, fundo=E.COR if comp else TINTA)
    for i, lin in enumerate(linhas):
        s_, ti = lin[:2]
        cor = lin[2] if len(lin) > 2 else TINTA
        sz = lin[3] if len(lin) > 3 else 62
        E.formula_em(c, t, ti, s_, x, y0 + 150 + 115 * i, sz, "g", cor, "center")


# ---------------- abertura ----------------
def b_gancho(c, t, C, b):
    ka, kb = C["s01.a"], C["s01.b"]
    E.foco(c, t, ka, 0.5, lambda a: E.escreve(c, "5", XE - 8, 560, 340, "g", COR, a))
    E.frase(c, t, ka + 0.3, ps("situações", "i", 100), XE + 220, 420)
    E.frase(c, t, w("s01", "criadas"), ps("criadas para esta aula", "i", 56, TINTA2), XE + 220, 520, "left", 0.08)
    E.frase(c, t, w("s01", "Empréstimo"), [("empréstimo,", "g", 50), ("aplicação,", "g", 50), ("conta atrasada", "g", 50, COR)], XE + 220, 620, "left", 0.5)
    E.frase(c, t, kb, ps("pause e", "i", 76) + [("resolva antes", "g", 80, COR)], XE, 820, "left", 0.12)
    E.frase(c, t, w("s01", "Errar"), ps("errar aqui não custa nada", "i", 60, TINTA2), XE, 940, "left", 0.1)
    E.foco(c, t, kb, 0.5, lambda a: (E.bola(c, 1600, 480, 160 * a),
                                     M.rrect(c, 1600 - 52, 480 - 60, 34, 120, 10, E.SOBRE, a),
                                     M.rrect(c, 1600 + 18, 480 - 60, 34, 120, 10, E.SOBRE, a)))


def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s02"] + 0.3, ps("você vai usar", "i", 84), XE, 190)
    E.foco(c, t, C["s02.a"], 0.5, lambda a: E.escreve(c, "3", XE - 8, 560, 300, "g", COR, a))
    E.frase(c, t, C["s02.a"] + 0.2, ps("ferramentas", "i", 80), XE + 200, 530)
    x = 930
    itens = [("b", "juros simples", "J = C · i · t"), ("c", "juros compostos", "M = C · (1 + i)^{t}"), ("d", "taxa e tempo", "na mesma unidade")]
    for i, (k, nome, f) in enumerate(itens):
        y = 330 + i * 220
        ti = C["s02." + k]
        E.foco(c, t, ti, 0.45, lambda a, i=i, y=y: num_bola(c, str(i + 1), x, y - 20, 42, 48, a))
        E.frase(c, t, ti + 0.1, [(nome, "i", 58, TINTA2)], x + 80, y - 30)
        E.foco(c, t, ti + 0.4, 0.45, lambda a, f=f, y=y, i=i: E.formula(c, f, x + 80, y + 60, 70, "g", COR if i < 2 else TINTA, a))
    E.frase(c, t, w("s02", "Se"), ps("travou? procure a aula no canal", "i", 58, TINTA2), 1250, 1000, "center", 0.1)


# ---------------- situação 1: juros simples, total pago ----------------
def b_questao1(c, t, C, b):
    a, b_, c_, d, e = (C[f"s03.{k}"] for k in "abcde")
    situacao(c, t, a, 1, "juros simples")
    cartao(c, t, b_, 420, 440, "R$ 2.500", "empréstimo", False, 84)
    pil(c, t, c_, "18% ao ano", 960, 380, 60, fundo=E.COR)
    pil(c, t, w("s03", "juros"), "juros simples", 960, 500, 48, fundo=TINTA)
    seta(c, t, c_, 650, 1260, 440)
    cartao(c, t, d, 1480, 440, "?", "8 meses depois", True, 84, w=300)
    E.saida(c, t, C["s04"] + 0.2, lambda: E.frase(c, t, e, ps("quanto foi pago", "i", 80) + [("no total?", "g", 84, COR)], W / 2, 760, "center", 0.12))
    pausa(c, t, C["s04.a"], 960, 780, 100)


def b_resposta1(c, t, C, b):
    a, b_, c_ = C["s05.a"], C["s05.b"], C["s05.c"]
    a6, b6, c6 = C["s06.a"], C["s06.b"], C["s06.c"]
    situacao(c, t, C["s05"], 1, "juros simples")
    E.frase(c, t, w("s05", "Taxa"), ps("taxa ao ano, tempo em meses:", "i", 62, TINTA2), XE, 290)
    pil(c, t, a, "converta", XE + 960, 270, 56)
    fluxo(c, t, 450, "18%", "÷ 12", [(b_ + 0.3, "?"), (w("s05", "um"), "1,5%")], b_, w("s05", "dividido"), b_ + 0.3, rot=("ao ano", "ao mês"), size=76)
    E.linha(c, t, [("1,5% × 8 meses", "g", 76, TINTA, c_), ("=", "g", 76, TINTA2, w("s05", "doze", 2)), ("12%", "g", 80, COR, w("s05", "doze", 2) + 0.2)],
            W / 2, 680, "center")
    E.linha(c, t, [("12% de R$ 2.500:", "g", 64, TINTA, a6), ("R$ 250", "g", 64, TINTA2, w("s06", "duzentos")),
                   ("+ R$ 50", "g", 64, TINTA2, w("s06", "cinquenta", 2)), ("=", "g", 64, TINTA2, b6 - 0.3), ("R$ 300", "g", 68, COR, b6)], W / 2, 820, "center")
    cen(c, t, w("s06", "Dez"), "10%           +   2%", W / 2 + 140, 880, 40, TINTA2, "i")
    E.frase(c, t, w("s06", "total"), ps("total:", "i", 64) + [("R$ 2.500 + R$ 300 =", "g", 68)], 1020, 990, "right", 0.12)
    E.foco(c, t, c6, 0.5, lambda q: E.pilula(c, "R$ 2.800", 1230, 965, 72, "g", a=q))


# ---------------- situação 2: achar a taxa ----------------
def b_questao2(c, t, C, b):
    a, b_, c_, d, e = (C[f"s07.{k}"] for k in "abcde")
    situacao(c, t, a, 2, "achar a taxa")
    cartao(c, t, b_, 420, 440, "R$ 800", "empréstimo", False, 84)
    pil(c, t, w("s07", "juros"), "juros simples", 960, 380, 48, fundo=TINTA)
    pil(c, t, d, "6 meses", 960, 500, 56, fundo=TINTA)
    seta(c, t, c_, 650, 1260, 440)
    cartao(c, t, c_, 1480, 440, "R$ 1.040", "quitado com", True, 84)
    E.saida(c, t, C["s08"] + 0.2, lambda: E.frase(c, t, e, ps("qual foi a", "i", 80) + [("taxa ao mês?", "g", 84, COR)], W / 2, 760, "center", 0.12))
    pausa(c, t, C["s08.a"], 960, 780, 100)


def b_resposta2(c, t, C, b):
    a, b_, c_, d, e = (C[f"s09.{k}"] for k in "abcde")
    situacao(c, t, C["s09"], 2, "achar a taxa")
    E.frase(c, t, w("s09", "Cuidado"), ps("cuidado:", "i", 64, ERRADO) + [("R$ 1.040", "g", 68)] + ps("é o", "i", 64) + [("montante", "g", 68, COR)],
            XE, 290, "left", 0.12)
    E.linha(c, t, [("juros:", "i", 62, TINTA2, b_), ("R$ 1.040 − R$ 800", "g", 72, TINTA, w("s09", "mil", 2)), ("=", "g", 72, TINTA2, w("s09", "dá")),
                   ("R$ 240", "g", 76, COR, w("s09", "duzentos"))], XE, 450)
    E.linha(c, t, [("juro de 1 mês:", "i", 62, TINTA2, c_ - 0.8), ("R$ 240 ÷ 6", "g", 72, TINTA, c_), ("=", "g", 72, TINTA2, w("s09", "dá", 2)),
                   ("R$ 40", "g", 76, COR, w("s09", "quarenta", 5))], XE, 600)
    E.linha(c, t, [("taxa:", "i", 62, TINTA2, d), ("R$ 40 ÷ R$ 800", "g", 72, TINTA, d + 0.2), ("=", "g", 72, TINTA2, w("s09", "dá", 3)),
                   ("0,05", "g", 76, COR, w("s09", "zero"))], XE, 750)
    E.foco(c, t, e, 0.5, lambda q: num_bola(c, "5%", 1580, 640, 150, 96, q))
    E.frase(c, t, e + 0.4, ps("ao mês", "i", 64), 1580, 870, "center")


# ---------------- situação 3: conta atrasada ----------------
def b_questao3(c, t, C, b):
    a, b_, c_, d, e, f = (C[f"s10.{k}"] for k in "abcdef")
    situacao(c, t, a, 3, "conta atrasada")
    cartao(c, t, b_, 420, 440, "R$ 1.200", "condomínio", False, 84)
    pil(c, t, c_, "15 dias de atraso", 420, 620, 52, fundo=ERRADO)
    pil(c, t, d, "multa de 2%", 1200, 360, 60, fundo=TINTA)
    pil(c, t, e, "mora de 1% ao mês", 1200, 480, 60, fundo=E.COR)
    cen(c, t, w("s10", "cobrados"), "cobrada por dia", 1200, 580, 50, TINTA2, "i")
    E.saida(c, t, C["s11"] + 0.2, lambda: E.frase(c, t, f, ps("quanto foi", "i", 80) + [("pago?", "g", 84, COR)], W / 2, 800, "center", 0.12))
    pausa(c, t, C["s11.a"], 960, 800, 100)


def b_resposta3(c, t, C, b):
    a, b_, c_, d = (C[f"s12.{k}"] for k in "abcd")
    a13, b13 = C["s13.a"], C["s13.b"]
    situacao(c, t, C["s12"], 3, "conta atrasada")
    E.linha(c, t, [("multa (1 vez só):", "i", 60, TINTA2, a), ("2% de R$ 1.200", "g", 68, TINTA, w("s12", "dois")), ("=", "g", 68, TINTA2, w("s12", "dá")),
                   ("R$ 24", "g", 72, COR, w("s12", "vinte"))], XE, 290)
    E.linha(c, t, [("mora:", "i", 60, TINTA2, w("s12", "Mora")), ("15 dias = meio mês", "g", 68, TINTA, b_)], XE, 420)
    E.linha(c, t, [("metade de 1%", "g", 68, TINTA, w("s12", "Metade")), ("=", "g", 68, TINTA2, c_ - 0.2), ("0,5%", "g", 72, COR, c_)], XE, 540)
    E.linha(c, t, [("0,5% de R$ 1.200", "g", 68, TINTA, d), ("=", "g", 68, TINTA2, w("s12", "dá", 3)), ("R$ 6", "g", 72, COR, w("s12", "seis"))], XE, 660)
    E.linha(c, t, [("atalho:", "i", 60, COR, w("s13", "Pelo")), ("2% + 0,5% = 2,5%", "g", 68, TINTA, a13), ("→", "g", 68, TINTA2, w("s13", "trinta") - 0.3),
                   ("R$ 30", "g", 72, COR, w("s13", "trinta"))], XE, 800)
    E.frase(c, t, b13 - 1.0, ps("total:", "i", 64) + [("R$ 1.200 + R$ 30 =", "g", 68)], 1100, 950, "right", 0.12)
    E.foco(c, t, b13, 0.5, lambda q: E.pilula(c, "R$ 1.230", 1320, 925, 76, "g", a=q))


# ---------------- situação 4: simples × compostos ----------------
def b_questao4(c, t, C, b):
    a, b_, c_, d, e, f = (C[f"s14.{k}"] for k in "abcdef")
    situacao(c, t, a, 4, "simples × compostos")
    cartao(c, t, b_, 420, 420, "R$ 5.000", "aplicados", False, 84)
    pil(c, t, c_, "12 meses", 960, 360, 60, fundo=TINTA)
    pil(c, t, d, "1% ao mês", 960, 480, 60, fundo=E.COR)
    E.frase(c, t, e, ps("quanto rende", "i", 66) + [("a mais", "g", 70, COR)], 1500, 380, "center", 0.12)
    E.frase(c, t, w("s14", "compostos"), ps("nos compostos do que nos simples?", "i", 50), 1500, 470, "center", 0.08)
    p = ep(t, f, 0.5)
    if p > 0:
        E.caixa_pontilhada(c, 270, 640, 820, 230, p, prog_=p)
        E.frase(c, t, f + 0.1, [("a prova dá", "i", 50, TINTA2)], 306, 710)
        E.formula_em(c, t, w("s14", "um", 2), "1,01^{12} ≈ 1,1268", 310, 820, 76, "g", TINTA)
    pausa(c, t, C["s15.a"], 1500, 760, 100)


def b_resposta4(c, t, C, b):
    a, b_, c_ = C["s16.a"], C["s16.b"], C["s16.c"]
    a17, b17, c17 = C["s17.a"], C["s17.b"], C["s17.c"]
    situacao(c, t, C["s16"], 4, "simples × compostos")
    E.frase(c, t, w("s16", "Doze"), [("12 meses", "g", 60)] + ps("passam de 1 período:", "i", 58, TINTA2) + [("ganham os compostos", "g", 60, COR)],
            W / 2, 270, "center", 0.1)
    p = ep(t, b_ - 0.5, 0.6)
    if p > 0:
        M.line(c, W / 2, 350, W / 2, lerp(350, 860, p), FIO, 1, 4)
    coluna(c, t, 520, w("s16", "Simples"), "simples", [("1% × 12 = 12%", b_), ("12% de R$ 5.000", c_ - 1.6), ("juros: R$ 600", c_, TINTA, 70)], y0=410)
    coluna(c, t, 1400, C["s17"] + 0.1, "compostos", [("R$ 5.000 · 1,1268", a17), ("≈ R$ 5.634", b17, COR), ("juros: R$ 634", w("s17", "Juros"), COR, 70)], y0=410)
    E.frase(c, t, c17 - 1.4, ps("diferença:", "i", 66), 800, 990, "right", 0.1)
    E.foco(c, t, c17, 0.5, lambda q: E.pilula(c, "R$ 34 a mais nos compostos", 1260, 965, 60, "g", a=q))


# ---------------- situação 5: achar o capital ----------------
def b_questao5(c, t, C, b):
    a, b_, c_, d, e = (C[f"s18.{k}"] for k in "abcde")
    situacao(c, t, a, 5, "valor presente")
    cartao(c, t, w("s18", "Uma"), 420, 440, "?", "hoje", False, 84, w=300)
    cartao(c, t, b_, 1480, 440, "R$ 8.450", "daqui a 2 anos", True, 84)
    seta(c, t, d, 600, 1250, 440)
    pil(c, t, d, "30% ao ano", 930, 380, 60, fundo=E.COR)
    pil(c, t, w("s18", "juros"), "juros compostos", 930, 500, 48, fundo=TINTA)
    cen(c, t, w("s18", "taxa"), "(taxa alta, só de exemplo)", 930, 590, 40, TINTA2, "i")
    E.saida(c, t, C["s19"] + 0.2, lambda: E.frase(c, t, e, ps("quanto ela precisa", "i", 76) + [("aplicar hoje?", "g", 80, COR)], W / 2, 790, "center", 0.12))
    pausa(c, t, C["s19.a"], 960, 800, 100)


def b_resposta5(c, t, C, b):
    a, b_, c_, d, e = (C[f"s20.{k}"] for k in "abcde")
    a21, b21 = C["s21.a"], C["s21.b"]
    situacao(c, t, C["s20"], 5, "valor presente")

    def conta():
        E.linha(c, t, [("fator:", "i", 64, TINTA2, w("s20", "Fator")), ("1,3", "g", 80, COR, a)], XE, 290)
        cen(c, t, b_ - 0.6, "2 anos:", 760, 290, 52, TINTA2, "i")
        E.formula_em(c, t, b_, "1,3^{2} = 1,69", 900, 290, 80, "g", TINTA)
        E.formula_em(c, t, c_, "R$ 8.450 ÷ 1,69", W / 2, 480, 96, "g", TINTA, "center")
        cen(c, t, w("s20", "Ande"), "ande 2 casas nos dois", W / 2, 580, 50, TINTA2, "i")
        E.linha(c, t, [("845.000 ÷ 169", "g", 96, TINTA, d), ("=", "g", 96, TINTA2, e - 0.3)], W / 2 - 200, 760, "center")
        E.foco(c, t, e, 0.5, lambda q: num_bola(c, "R$ 5.000", 1430, 730, 160, 66, q))
    E.saida(c, t, C["s21"] - 0.1, conta)
    if t < C["s21"]:
        return
    E.frase(c, t, C["s21"] + 0.2, ps("conferindo pela", "i", 72) + [("ida", "g", 76, COR)], W / 2, 270, "center", 0.12)
    cadeia(c, t, 470, ["R$ 5.000", "R$ 6.500", "R$ 8.450"], ["× 1,3", "× 1,3"], [a21 - 0.3, w("s21", "seis"), w("s21", "oito")],
           [a21, w("s21", "que")], rot=["hoje", "1 ano", "2 anos"], size=74)
    selo_em(c, t, w("s21", "Bateu"), 1800, 340, 46, True)
    E.frase(c, t, w("s21", "Quem"), ps("tirar 30% duas vezes do total?", "i", 64) + [("errado", "g", 68, ERRADO)], W / 2, 760, "center", 0.1)
    E.frase(c, t, w("s21", "os", 1), ps("os juros nasceram", "i", 64) + [("do capital", "g", 68, COR)] + ps("e não do montante", "i", 64), W / 2, 880, "center", 0.1)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    a, b_, c_, d, e = (C[f"s22.{k}"] for k in "abcde")
    a23, b23 = C["s23.a"], C["s23.b"]
    E.frase(c, t, C["s22"] + 0.3, [("o atalho", "g", 72, BR)] + ps("para", "i", 72, CLARO) + [("dobrar", "g", 76, BR)], W / 2, 150, "center", 0.15)
    p = ep(t, b_, 0.6)
    if p > 0:
        M.line(c, W / 2, 230, W / 2, lerp(230, 720, p), "#3A3A4A", 1, 4)
    for x, tn, nome, regra, tc, conta, res in ((520, b_, "nos simples", "100 ÷ taxa", d, "100 ÷ 8", "12,5 meses"),
                                               (1400, c_, "nos compostos", "72 ÷ taxa", e, "72 ÷ 8", "≈ 9 meses")):
        E.frase(c, t, tn, ps(nome, "i", 64, CLARO), x, 300, "center", 0.1)
        E.foco(c, t, tn + 0.5, 0.45, lambda q, x=x, regra=regra: E.pilula(c, regra, x, 420, 76, "g", fundo=CLARO, cor="#07070F", a=q))
        E.linha(c, t, [(conta, "g", 80, BR, tc), ("=", "g", 80, CLARO, tc + 0.4), (res, "g", 80, CLARO, tc + 0.6)], x, 640, "center")
    cen(c, t, d - 1.0, "a 8% ao mês:", W / 2, 560, 50, CLARO, "i")
    E.frase(c, t, a23, ps("os compostos dobram antes:", "i", 62, CLARO) + [("juro sobre juro", "g", 66, BR)], W / 2, 850, "center", 0.1)
    E.frase(c, t, b23, ps("o 72 é", "i", 58, CLARO) + [("uma estimativa:", "g", 62, BR)] + ps("erra mais com taxas muito altas", "i", 58, CLARO),
            W / 2, 970, "center", 0.08)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    a24, b24, c24 = (C[f"s24.{k}"] for k in "abc")

    def resumo():
        E.frase(c, t, C["s24"] + 0.3, [("resumindo", "i", 92, COR)], XE, 200)
        E.passo(c, t, a24, 1, "taxa e tempo", "na mesma unidade", 400)
        E.passo(c, t, b24, 2, "separe", "juros de montante", 600)
        E.passo(c, t, c24, 3, "confira se a resposta", "faz sentido", 800)
    E.saida(c, t, C["s25"] - 0.1, resumo)
    if t < C["s25"]:
        return
    a, b_, c_, d = (C[f"s25.{k}"] for k in "abcd")

    def ponte():
        E.frase(c, t, C["s25"] + 0.2, ps("repare na", "i", 72) + [("situação 4", "g", 76, COR)], W / 2, 220, "center", 0.12)
        E.frase(c, t, a - 1.6, [("1% ao mês", "g", 84)] + ps("rendeu em 1 ano", "i", 76), W / 2, 400, "center", 0.12)
        E.foco(c, t, a, 0.5, lambda q: E.pilula(c, "12,68%", W / 2, 560, 110, "g", a=q))
        E.frase(c, t, w("s25", "não"), ps("e não", "i", 76) + [("12%", "g", 84, ERRADO)], W / 2, 740, "center", 0.12)
    E.saida(c, t, b_ - 0.4, ponte)
    if t < b_ - 0.4:
        return
    E.frase(c, t, b_ - 0.3, [("próxima", "i", 84), ("aula", "i", 84)], XE, 300)
    E.frase(c, t, b_, [("Taxa equivalente", "g", 104, COR)], XE, 440)
    E.frase(c, t, b_ + 0.4, [("e taxa efetiva", "g", 104, COR)], XE, 570)
    E.frase(c, t, b_ + 0.8, ps("por que 1% ao mês dá", "i", 66) + [("12,68% ao ano", "g", 70, COR)], XE, 720, "left", 0.1)
    E.foco(c, t, c_, 0.5, lambda q: E.pilula(c, "Inscreva-se", 1520, 300, 72, estilo="g", a=q))
    p = ease_io(prog(t, c_ + 0.3, 0.8))
    E.cursor(c, lerp(1800, 1640, p), lerp(620, 325, p), ep(t, c_ + 0.2, 0.4))
    E.frase(c, t, d, [("bons", "i", 120), ("estudos!", "i", 120, COR)], W / 2, 980, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, questao1=b_questao1, resposta1=b_resposta1, questao2=b_questao2, resposta2=b_resposta2,
              questao3=b_questao3, resposta3=b_resposta3, questao4=b_questao4, resposta4=b_resposta4, questao5=b_questao5, resposta5=b_resposta5,
              atalho=b_atalho, fim=b_fim)
