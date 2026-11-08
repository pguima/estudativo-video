"""Visual — Estudativo · MAT-FIN-004: juros compostos, mês a mês e a fórmula.

Linguagem da trilha Matemática Financeira, herdada de Porcentagem:
- cartao(): o valor num cartão branco. ANTES = contorno escuro; DEPOIS = contorno e número na cor da matéria.
- maquina(): o fator (× 1,1) numa caixa cheia da cor da matéria: a "máquina" que transforma o dinheiro a cada mês.
- mes a mês: R$ 1.000 → R$ 1.100 → R$ 1.210 → R$ 1.331, primeiro somando os juros, depois com as máquinas × 1,1,
  que se fundem numa só (× 1,1³).
- tabela_enunciado(): a caixa pontilhada com a potência que a prova dá.
Todo instante vem de C[...] (marcadores do roteiro) e dos tempos reais da voz."""
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Matemática Financeira")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-FIN-004_juros_compostos_formula.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("mes", "fator", "formula", "atalho", "questao", "fim"))
BR = "#FFFFFF"
assert round(1000 * 1.1, 6) == 1100 and round(1100 * 1.1, 6) == 1210 and round(1210 * 1.1, 6) == 1331 and round(1.1 ** 3, 6) == 1.331
assert round(1.02 ** 6, 4) == 1.1262 and round(1000 * 1.1262, 2) == 1126.2 and round(1.02 * 6, 6) == 6.12
assert round(1.03 ** 4, 4) == 1.1255 and round(4000 * 1.1255, 6) == 4502 and 4502 - 4000 == 502 and round(4000 * 0.03 * 4, 6) == 480 and 502 - 480 == 22


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



# ---------------- peças desta aula ----------------
def pil(c, t, t0, s, cx, cy, size=60, fundo=None, cor=BR, est="g"):
    E.foco(c, t, t0, 0.45, lambda a: E.pilula(c, s, cx, cy, size, est, fundo=fundo, cor=cor, a=a))


def tabela_enunciado(c, t, t0, x, y, w, h, f, v, size=72):
    """caixa pontilhada com a potência que a prova dá: f ≈ v"""
    p = ep(t, t0, 0.5)
    if p <= 0:
        return
    E.caixa_pontilhada(c, x, y, w, h, p, prog_=p)
    E.frase(c, t, t0 + 0.1, [("a prova dá", "i", 50, TINTA2)], x + 36, y + 70)
    E.foco(c, t, t0 + 0.3, 0.45, lambda a: (E.formula(c, f, x + 40, y + h - 60, size, "g", TINTA, a),
                                            E.escreve(c, "≈ " + v, x + 40 + E.formula(c, f, 0, 0, size, a=0) + 24, y + h - 60, size, "g", COR, a)))


def barras_juros(c, t, x0, ybase, alto, vals, tv, cor, dx, rot=None, ta=None):
    """colunas dos juros de cada mês: vals = valores, tv = instantes; dx = deslocamento da coluna no grupo"""
    for i, (v, ti) in enumerate(zip(vals, tv)):
        p = ease_back(prog(t, ti, 0.45))
        if p <= 0:
            continue
        h = alto * v / 121 * min(p, 1.05)
        x = x0 + 300 * i + dx
        M.rrect(c, x, ybase - h, 110, h, 10, cor, min(1, p))
        centro(c, f"R$ {v}", x + 55, ybase - h - 14, 34, "g", cor if cor != E.COR else COR, min(1, p))


def tres_maquinas(c, t, ts, tf, xs, y, fator, junto, size=72):
    """três máquinas iguais (entram em ts[i]) que deslizam e viram uma só em tf"""
    xm = xs[1]
    p = ease_io(prog(t, tf, 0.8))
    if p < 1:
        lay = skia.Paint(); lay.setAlphaf(1 - p)
        c.saveLayer(None, lay)
        for x, ti in zip(xs, ts):
            maquina(c, t, ti, lerp(x, xm, p), y, fator, size)
        c.restore()
    if p > 0.5:
        maquina(c, t, tf + 0.5, xm, y, junto, size * 1.1)
    return p


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    ka, kb, kc, kd = (C[f"s01.{k}"] for k in "abcd")

    def um():
        cartao(c, t, ka + 0.1, 330, 540, "R$ 1.000", "hoje", False, 92)
        pil(c, t, kb + 0.3, "10% ao mês", 330, 760, 56, fundo=TINTA)
        pil(c, t, w("s01", "três"), "3 meses", 330, 870, 56, fundo=TINTA)
        for (y, tt, rot, val, cor) in ((340, kc, "juros simples", "R$ 1.300", TINTA), (740, kd, "juros compostos", "R$ 1.331", None)):
            p = ep(t, tt - 0.4, 0.5)
            if p > 0:
                M.arrow(c, 570, 540 + (y - 540) * 0.25, lerp(570, 1180, p), lerp(540 + (y - 540) * 0.25, y, p), TINTA2, p, 6, 22, p)
            cartao(c, t, tt, 1480, y, val, rot, cor is None, 92)
        E.foco(c, t, w("s01", "trinta", 2), 0.5, lambda q: E.pilula(c, "+ R$ 31?", 1480, 930, 64, "g", fundo=ERRADO, a=q))
    E.saida(c, t, C["s02"] - 0.1, um)
    if t >= C["s02"]:
        ta, tb = C["s02.a"], C["s02.b"]
        E.foco(c, t, tb - 0.2, 0.7, lambda a: E.bola(c, 1500, 540, 250 * ease_back(prog(t, tb - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, ps("até o fim desta aula", "i", 90), XE, 330, passo=0.14)
        E.frase(c, t, w("s02", "calcular"), ps("calcular", "i", 92) + [("juros compostos", "g", 96, COR)], XE, 480, passo=0.14)
        E.frase(c, t, w("s02", "mês"), ps("mês a mês e", "i", 84) + [("pela fórmula", "g", 88)], XE, 620, passo=0.14)
        E.foco(c, t, tb + 0.1, 0.5, lambda a: (centro(c, "+ atalho", 1500, 525, 80, "g", E.SOBRE, a),
                                               centro(c, "de prova", 1500, 610, 80, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    ka, kb, kc, kd = (C[f"s03.{k}"] for k in "abcd")
    E.frase(c, t, C["s03"] + 0.3, ps("você só precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, ka, 0.5, lambda a: E.escreve(c, "3", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, ka + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, wc = 880, 900
    p = ep(t, kb, 0.5)
    E.caixa_pontilhada(c, x, 200, wc, 640, p, prog_=p)
    E.frase(c, t, kb + 0.1, [("juros simples", "g", 64, COR)], x + 44, 300)
    E.frase(c, t, kc, ps("aumentos seguidos:", "i", 58), x + 44, 460)
    E.foco(c, t, kc + 0.5, 0.45, lambda a: E.escreve(c, "multiplique os fatores", x + 44, 545, 60, "g", COR, a))
    E.frase(c, t, kd, ps("potência de decimal:", "i", 58), x + 44, 690)
    E.foco(c, t, w("s03", "zero"), 0.45, lambda a: E.formula(c, "0,3^{2} = 0,09", x + 44, 790, 72, "g", COR, a))
    q = ease_io(prog(t, kd - 0.35, 0.5))
    E.cursor(c, x + wc - 30, lerp(330, 800, q), ep(t, kb, 0.4))
    E.frase(c, t, w("s03", "Se"), ps("faltou alguma?", "i", 58, COR) + ps("procure no canal", "i", 58), x, 960, "left", 0.12)


# ---------------- mês a mês ----------------
XC = [250, 730, 1200, 1660]  # os quatro cartões do mês a mês


def b_mes(c, t, C, b):
    a4, b4 = C["s04.a"], C["s04.b"]
    a5, b5, c5, d5 = (C[f"s05.{k}"] for k in "abcd")
    a6, b6, c6 = (C[f"s06.{k}"] for k in "abc")

    def tela1():
        E.frase(c, t, C["s04"] + 0.3, ps("nos", "i", 84) + [("juros compostos", "g", 90, COR)], W / 2, 220, "center", 0.14)
        E.frase(c, t, a4, ps("os juros de cada mês", "i", 72) + [("entram na conta", "g", 76)], W / 2, 380, "center", 0.1)
        E.frase(c, t, w("s04", "do", 1), ps("do mês seguinte", "i", 72), W / 2, 480, "center", 0.1)
        E.foco(c, t, b4, 0.5, lambda q: E.pilula(c, "juro sobre juro", W / 2, 660, 110, "g", a=q))
        E.frase(c, t, w("s04", "São"), ps("bancos, aplicações e dívidas", "i", 60, TINTA2), W / 2, 860, "center", 0.1)
    E.saida(c, t, C["s05"] - 0.1, tela1)
    if t < C["s05"]:
        return
    y = 300
    vals = [("R$ 1.000", "hoje", C["s05"] + 0.1), ("R$ 1.100", "1º mês", b5), ("R$ 1.210", "2º mês", d5), ("R$ 1.331", "3º mês", b6)]
    ws = []
    for i, (v, r, tv) in enumerate(vals):
        ws.append(cartao(c, t, tv, XC[i], y, v, r, i > 0, 68, w=300))
    juros = [("+ R$ 100", w("s05", "cem"), "10% de R$ 1.000"), ("+ R$ 110", w("s05", "São"), "10% de R$ 1.100"),
             ("+ R$ 121", w("s06", "cento"), "10% de R$ 1.210")]
    for j, (s_, tj, sub) in enumerate(juros):
        xm = (XC[j] + XC[j + 1]) / 2
        p = ep(t, tj - 0.3, 0.5)
        if p > 0:
            M.arrow(c, XC[j] + 155, y, XC[j + 1] - 160, y, TINTA2, p, 5, 18, p)
        pil(c, t, tj, s_, xm, y - 140, 46, fundo=E.COR)
        cen(c, t, [a5, c5, a6][j], sub, xm, y + 140, 38, TINTA2, "i")
    # os juros de cada mês: simples (cinza) × compostos (cor)
    if t >= w("s06", "Nos") - 0.2:
        x0, yb = 760, 900
        q = ep(t, w("s06", "Nos") - 0.2, 0.4)
        M.line(c, x0 - 40, yb, x0 + 900, yb, TINTA, q, 5)
        for i in range(3):
            cen(c, t, w("s06", "Nos"), f"{i + 1}º mês", x0 + 300 * i + 120, yb + 55, 42, TINTA2, "i")
        barras_juros(c, t, x0, yb, 260, [100, 100, 100], [w("s06", "simples") + 0.15 * i for i in range(3)], CINZA, 0)
        barras_juros(c, t, x0, yb, 260, [100, 110, 121], [w("s06", "cem", 2), w("s06", "dez", 3), w("s06", "um", 3)], E.COR, 130)
        E.frase(c, t, w("s06", "Nos"), [("simples:", "g", 48, CINZA)] + ps("R$ 100 todo mês", "i", 46, TINTA2), 360, 610, "center", 0.1)
        E.frase(c, t, c6, [("compostos:", "g", 48, COR)] + ps("os juros crescem", "i", 46), 360, 690, "center", 0.1)


# ---------------- fatores ----------------
def b_fator(c, t, C, b):
    a7, b7, c7 = (C[f"s07.{k}"] for k in "abc")
    a8, b8, c8, d8 = (C[f"s08.{k}"] for k in "abcd")

    def tela1():
        E.frase(c, t, C["s07"] + 0.3, ps("com fatores,", "i", 84) + [("mais rápido", "g", 88, COR)], W / 2, 170, "center", 0.14)
        E.frase(c, t, a7 - 1.0, ps("somar 10% é", "i", 72), 640, 440, "right", 0.1)
        maquina(c, t, a7, 960, 420, "× 1,1", 80)
        p = ep(t, a7, 0.5)
        if p > 0:
            M.arrow(c, 670, 420, 820, 420, TINTA2, p, 6, 20, p)
        cartao(c, t, a7 + 0.6, 1450, 420, "110%", "100% + 10%", True, 88)
        p = ep(t, a7 + 0.4, 0.5)
        if p > 0:
            M.arrow(c, 1120, 420, 1290, 420, TINTA2, p, 6, 20, p)
        E.frase(c, t, b7, [("3 meses", "g", 80)] + ps("=", "g", 80, TINTA2) + ps("3 aumentos seguidos de 10%", "i", 72), W / 2, 700, "center", 0.12)
        E.frase(c, t, c7, ps("aumentos seguidos:", "i", 70) + [("multiplique os fatores", "g", 74, COR)], W / 2, 850, "center", 0.12)
    E.saida(c, t, C["s08"] - 0.1, tela1)
    if t < C["s08"]:
        return
    y = 330
    xs = [640, 960, 1280]
    cartao(c, t, a8, 260, y, "R$ 1.000", "capital", False, 80)
    ts = [w("s08", "vezes", k) for k in (1, 2, 3)]
    p = tres_maquinas(c, t, ts, b8, xs, y, "× 1,1", "× 1,1³", 64)
    for i, ti in enumerate(ts):
        q = ep(t, ti - 0.1, 0.4) * (1 - p)
        if q > 0:
            xa = 490 if i == 0 else xs[i - 1] + 100
            M.arrow(c, xa, y, xs[i] - 105, y, TINTA2, q, 5, 16, q)
    if p > 0:
        M.arrow(c, 490, y, 960 - 135, y, TINTA2, p, 6, 20, p)
    cartao(c, t, d8, 1640, y, "R$ 1.331", "3 meses depois", True, 80)
    q = ep(t, d8 - 0.2, 0.4)
    if q > 0:
        M.arrow(c, 960 + 135, y, 1460, y, TINTA2, q, 6, 20, q)
    E.frase(c, t, w("s08", "mesmo"), ps("o mesmo número várias vezes =", "i", 66) + [("potência", "g", 70, COR)], W / 2, 590, "center", 0.1)
    E.linha(c, t, [("1,1 × 1,1 × 1,1", "g", 72, TINTA2, b8), ("=", "g", 72, TINTA2, b8 + 0.3)], 820, 730, "right")
    E.formula_em(c, t, b8 + 0.5, "1,1^{3}", 860, 730, 88, "g", TINTA)
    E.linha(c, t, [("1,1³", "g", 96, TINTA, c8), ("=", "g", 96, TINTA2, w("s08", "dá")), ("1,331", "g", 104, COR, w("s08", "um", 8))], W / 2, 900, "center")
    E.frase(c, t, d8, [("× R$ 1.000", "g", 72), ("=", "g", 72, TINTA2), ("R$ 1.331", "g", 76, COR)], W / 2, 1020, "center", 0.15)


# ---------------- a fórmula ----------------
def b_formula(c, t, C, b):
    a9, b9, c9, d9, e9 = (C[f"s09.{k}"] for k in "abcde")
    a10, b10, c10, d10, e10 = (C[f"s10.{k}"] for k in "abcde")
    a11, b11, c11 = C["s11.a"], C["s11.b"], C["s11.c"]
    if t < C["s10"]:
        def tela1():
            partes = [("M", b9, "montante"), ("=", None, None), ("C", c9, "capital"), ("·", None, None), ("(1 + i)^{t}", e9, None)]
            xs, ws = eq_f(c, t, [(s, TINTA, a9 + 0.12 * i) for i, (s, _, _) in enumerate(partes)], W / 2, 360, 150)
            for (s, tl, nome), x, w_ in zip(partes, xs, ws):
                if tl is None:
                    continue
                q = ep(t, tl, 0.4)
                if q > 0:
                    E.formula(c, s, x, 360, 150, "g", COR, q)
                if nome:
                    cen(c, t, tl, nome, x + w_ / 2, 480, 54, COR, "i")
            xf, wf = xs[4], ws[4]
            cen(c, t, d9, "t = nº de períodos", xf + wf / 2, 170, 50, COR, "i")
            cen(c, t, e9 + 0.2, "o fator", xf + wf / 2 - 30, 480, 54, COR, "i")
            E.frase(c, t, w("s09", "mesmo"), [("1 + i", "g", 64), ("=", "g", 64, TINTA2)] + ps("100% + a taxa, em decimal", "i", 60), W / 2, 640, "center", 0.1)
            E.frase(c, t, w("s09", "Atenção"), ps("atenção à ordem:", "i", 60, ERRADO), W / 2, 760, "center", 0.1)
            E.passo(c, t, w("s09", "só"), 1, "primeiro", "eleve o fator a t", 860)
            E.passo(c, t, w("s09", "Depois"), 2, "depois", "multiplique pelo capital", 1000)
        E.saida(c, t, C["s10"] - 0.1, tela1)
        return
    E.frase(c, t, C["s10"] + 0.2, ps("na prova, o enunciado", "i", 72) + [("dá uma tabela", "g", 76, COR)], W / 2, 150, "center", 0.12)
    if t < C["s11"]:
        def tela2():
            pil(c, t, b10 - 0.7, "C = R$ 1.000", 480, 330, 60, fundo=TINTA)
            pil(c, t, b10, "2% ao mês", 960, 330, 60, fundo=E.COR)
            pil(c, t, c10, "t = 6 meses", 1440, 330, 60, fundo=TINTA)
            E.linha(c, t, [("fator:", "i", 64, TINTA2, w("s10", "Fator")), ("100% + 2% = 102%", "g", 72, TINTA, w("s10", "cem")),
                           ("=", "g", 72, TINTA2, d10)], W / 2 - 100, 540, "center")
            E.foco(c, t, d10, 0.45, lambda q: E.pilula(c, "1,02", 1470, 515, 72, "g", a=q))
            E.formula_em(c, t, e10, "M = 1.000 · 1,02^{6}", W / 2, 800, 130, "g", TINTA, "center")
        E.saida(c, t, C["s11"] - 0.1, tela2)
        return
    E.formula_em(c, t, C["s11"], "M = 1.000 · 1,02^{6}", W / 2, 320, 90, "g", TINTA2, "center")
    tabela_enunciado(c, t, a11, 560, 400, 800, 230, "1,02^{6}", "1,1262", 80)
    E.linha(c, t, [("1,1262 × 1.000", "g", 80, TINTA, b11), ("→", "g", 80, TINTA2, b11 + 0.3)], 1000, 790, "right")
    E.frase(c, t, w("s11", "vírgula", 3), ps("a vírgula anda 3 casas", "i", 60, COR), 1040, 785)
    E.frase(c, t, c11, [("M ≈", "g", 96, TINTA2)], 790, 970, "right")
    E.foco(c, t, w("s11", "mil", 2), 0.5, lambda q: E.pilula(c, "R$ 1.126,20", 1150, 935, 96, "g", a=q))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    a, b_, c_, d = (C[f"s12.{k}"] for k in "abcd")
    E.frase(c, t, C["s12"] + 0.3, [("o erro comum", "g", 96, ERRADO)], W / 2, 170, "center")
    E.frase(c, t, a, ps("multiplicar o fator", "i", 72) + [("pelo tempo", "g", 76, ERRADO)], W / 2, 300, "center", 0.12)
    E.linha(c, t, [("1,02 × 6", "g", 100, TINTA, b_), ("=", "g", 100, TINTA2, w("s12", "dá")), ("6,12", "g", 100, ERRADO, w("s12", "seis", 2))], W / 2, 470, "center")
    E.frase(c, t, c_, ps("montante de", "i", 72) + [("R$ 6.120", "g", 80, ERRADO)] + ps("em 6 meses, a 2%?", "i", 72), W / 2, 620, "center", 0.12)
    E.foco(c, t, w("s12", "Absurdo"), 0.4, lambda q: E.pilula(c, "absurdo!", 1640, 520, 60, "g", fundo=ERRADO, a=q))
    if t >= w("s12", "Absurdo"):
        E.risco(c, 640, 500, 1290, 410, t, w("s12", "Absurdo"), largura=12)
    E.frase(c, t, d, ps("o tempo é", "i", 76) + [("o expoente:", "g", 80, COR)], 740, 830, "center", 0.12)
    E.formula_em(c, t, d + 0.4, "1,02^{6}", 1380, 840, 130, "g", COR)
    E.frase(c, t, w("s12", "quantas"), ps("quantas vezes o fator se repete", "i", 58, TINTA2), W / 2, 980, "center", 0.08)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    a13, b13, c13 = (C[f"s13.{k}"] for k in "abc")
    a14, b14, c14 = (C[f"s14.{k}"] for k in "abc")

    def regra():
        E.frase(c, t, C["s13"] + 0.3, [("o atalho", "g", 72, BR)] + ps("para 10%", "i", 72, CLARO), W / 2, 150, "center", 0.15)
        E.linha(c, t, [("× 1,1", "g", 100, BR, a13), ("=", "g", 100, CLARO, w("s13", "somar")), ("somar a décima parte", "g", 80, CLARO, w("s13", "décima"))],
                W / 2, 340, "center")
        E.linha(c, t, [("R$ 1.100", "g", 88, BR, b13), ("+ R$ 110", "g", 88, CLARO, w("s13", "cento")), ("=", "g", 88, CLARO, w("s13", "dá")),
                       ("R$ 1.210", "g", 88, BR, w("s13", "mil", 2))], W / 2, 560, "center")
        E.linha(c, t, [("R$ 1.210", "g", 88, BR, c13), ("+ R$ 121", "g", 88, CLARO, w("s13", "cento", 2)), ("=", "g", 88, CLARO, w("s13", "mil", 3)),
                       ("R$ 1.331", "g", 88, BR, w("s13", "trezentos"))], W / 2, 760, "center")
        cen(c, t, w("s13", "cento") + 0.3, "a décima parte de R$ 1.100", W / 2, 640, 44, CLARO, "i")
        cen(c, t, w("s13", "cento", 2) + 0.3, "a décima parte de R$ 1.210", W / 2, 840, 44, CLARO, "i")
    E.saida(c, t, C["s14"] - 0.1, regra)
    if t < C["s14"]:
        return
    E.frase(c, t, C["s14"] + 0.2, ps("funciona porque", "i", 76, CLARO), W / 2, 180, "center", 0.12)
    E.linha(c, t, [("1,1", "g", 110, BR, a14), ("=", "g", 110, CLARO, a14 + 0.4), ("1 inteiro", "g", 90, BR, w("s14", "inteiro")),
                   ("+", "g", 90, CLARO, w("s14", "mais")), ("1 décimo", "g", 90, CLARO, w("s14", "décimo"))], W / 2, 400, "center")
    E.frase(c, t, w("s14", "Não"), ps("taxa quebrada ou muitos meses?", "i", 64, CLARO), W / 2, 620, "center", 0.1)
    E.frase(c, t, b14, [("2% por 6 meses", "g", 84, BR)], 700, 800, "center")
    E.foco(c, t, c14, 0.5, lambda a: E.pilula(c, "use a tabela", 1330, 775, 76, "g", fundo=CLARO, cor="#07070F", a=a))


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    a, b_, c_, d, e = (C[f"s15.{k}"] for k in "abcde")
    E.frase(c, t, C["s15"] + 0.3, ps("hora de", "i", 72, COR) + [("testar", "g", 72)], XE, 150)
    cartao(c, t, a, 400, 380, "R$ 4.000", "aplicados", False, 84)
    pil(c, t, b_, "3% ao mês", 930, 330, 64, fundo=E.COR)
    pil(c, t, w("s15", "juros"), "juros compostos", 930, 450, 52, fundo=TINTA)
    cen(c, t, w("s15", "taxa"), "(taxa alta, só de exemplo)", 930, 540, 42, TINTA2, "i")
    pil(c, t, c_, "4 meses", 1400, 330, 64, fundo=TINTA)
    tabela_enunciado(c, t, d, 170, 640, 820, 230, "1,03^{4}", "1,1255", 80)
    E.frase(c, t, e, [("montante?", "g", 84, COR)], 1450, 820, "center")
    E.frase(c, t, w("s15", "juros", 2), [("juros?", "g", 84, COR)], 1450, 940, "center")
    E.relogio(c, t, C["s16.a"], 1700, 520, 90)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    a, b_, c_, d = (C[f"s17.{k}"] for k in "abcd")
    a18, b18, c18, d18 = (C[f"s18.{k}"] for k in "abcd")

    def conta():
        E.linha(c, t, [("fator:", "i", 64, TINTA2, w("s17", "Fator")), ("100% + 3% = 103%", "g", 72, TINTA, w("s17", "cem")),
                       ("=", "g", 72, TINTA2, a)], W / 2 - 100, 180, "center")
        E.foco(c, t, a, 0.45, lambda q: E.pilula(c, "1,03", 1470, 155, 72, "g", a=q))
        E.formula_em(c, t, b_, "M = 4.000 · 1,03^{4}", W / 2, 380, 110, "g", TINTA, "center")
        E.linha(c, t, [("M ≈", "g", 84, TINTA2, c_), ("4.000 × 1,1255", "g", 84, TINTA, c_ + 0.2)], W / 2, 560, "center")
        E.linha(c, t, [("1.000 × 1,1255", "g", 72, TINTA2, w("s17", "Vezes", 3)), ("=", "g", 72, TINTA2, w("s17", "dá", 2)),
                       ("1.125,5", "g", 72, TINTA, w("s17", "mil", 4))], W / 2, 720, "center")
        E.linha(c, t, [("× 4", "g", 84, TINTA, d), ("=", "g", 84, TINTA2, w("s17", "dá", 3))], 820, 900, "right")
        E.foco(c, t, w("s17", "quatro", 5), 0.5, lambda q: E.pilula(c, "R$ 4.502", 1080, 872, 90, "g", a=q))
        cen(c, t, w("s17", "reais"), "montante", 1430, 900, 60, COR, "i")
    E.saida(c, t, C["s18"] - 0.1, conta)
    if t < C["s18"]:
        return
    E.frase(c, t, C["s18"] + 0.2, [("juros", "g", 84, COR), ("=", "g", 84, TINTA2)] + ps("montante − capital", "i", 80), W / 2, 200, "center", 0.12)
    E.linha(c, t, [("R$ 4.502 − R$ 4.000", "g", 88, TINTA, a18), ("=", "g", 88, TINTA2, w("s18", "dá"))], 1060, 420, "right")
    E.foco(c, t, b18, 0.5, lambda q: num_bola(c, "R$ 502", 1320, 390, 140, 70, q))
    E.frase(c, t, c18, [("nos simples:", "i", 66, TINTA2), ("R$ 480", "g", 76, TINTA2)], W / 2, 680, "center", 0.15)
    E.frase(c, t, d18 - 1.5, ps("juro sobre juro rendeu", "i", 72) + [("R$ 22 a mais", "g", 80, COR)], W / 2, 860, "center", 0.12)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    a19, b19, c19 = (C[f"s19.{k}"] for k in "abc")

    def resumo():
        E.frase(c, t, C["s19"] + 0.3, [("resumindo", "i", 92, COR)], XE, 200)
        E.passo(c, t, a19, 1, "nos compostos, os juros", "rendem sobre o montante", 400)
        E.passo(c, t, b19, 2, "eleve o fator", "ao número de períodos", 600)
        E.passo(c, t, c19, 3, "multiplique", "pelo capital", 800)
        E.formula_em(c, t, b19, "M = C · (1 + i)^{t}", 1500, 640, 90, "g", COR, "center")
    E.saida(c, t, C["s20"] - 0.1, resumo)
    if t < C["s20"]:
        return
    a, b_, c_ = (C[f"s20.{k}"] for k in "abc")
    E.frase(c, t, C["s20"] + 0.2, ps("os compostos", "i", 76) + [("sempre rendem mais?", "g", 80, COR)], XE, 200, "left", 0.12)
    E.frase(c, t, w("s20", "Na"), [("próxima", "i", 84), ("aula", "i", 84)], XE, 360)
    E.frase(c, t, w("s20", "Na") + 0.4, [("Juros simples", "g", 104, COR)], XE, 500)
    E.frase(c, t, w("s20", "Na") + 0.7, [("contra compostos", "g", 104, COR)], XE, 630)
    E.frase(c, t, a, ps("quem ganha em", "i", 68) + [("1 mês,", "g", 70)] + [("menos de 1 mês", "g", 70)] + ps("e em", "i", 68) + [("2 anos?", "g", 70)],
            XE, 780, "left", 0.15)
    E.foco(c, t, b_, 0.5, lambda q: E.pilula(c, "Inscreva-se", 1520, 300, 72, estilo="g", a=q))
    p = ease_io(prog(t, b_ + 0.3, 0.8))
    E.cursor(c, lerp(1800, 1640, p), lerp(620, 325, p), ep(t, b_ + 0.2, 0.4))
    E.frase(c, t, c_, [("bons", "i", 120), ("estudos!", "i", 120, COR)], W / 2, 980, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, mes=b_mes, fator=b_fator, formula=b_formula, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
