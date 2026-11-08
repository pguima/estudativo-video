"""Visual — Estudativo · MAT-FIN-003: conta atrasada, multa com juros.

Linguagem da trilha Matemática Financeira, herdada de Porcentagem:
- cartao(): o valor num cartão branco. ANTES = contorno escuro; DEPOIS = contorno e número na cor da matéria.
- maquina(): a operação numa caixa cheia da cor da matéria (2% de, ÷ 30).
- boleto(): a conta com valor, multa e mora, e o carimbo de atraso.
- recibo(): a soma da conta, linha a linha (conta + multa + mora = total).
Todo instante vem de C[...] (marcadores do roteiro) e dos tempos reais da voz."""
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Matemática Financeira")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-FIN-003_conta_atrasada_multa_juros.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("duas", "mora", "total", "atalho", "questao", "fim"))
BR = "#FFFFFF"
assert round(200 * 0.02, 6) == 4 and round(3 / 30, 6) == 0.1 and round(200 * 0.001, 6) == 0.2 and round(0.2 * 10, 6) == 2
assert 200 + 4 + 2 == 206 and 200 + 4 + 6 == 210 and 4 * 10 == 40 and 200 + 40 + 2 == 242 and 242 - 206 == 36
assert round(200 * 0.03, 6) == 6 and round(150 * 0.02, 6) == 3 and round(1.5 / 30, 6) == 0.05 and round(0.05 * 20, 6) == 1
assert round(150 * 0.01, 6) == 1.5 and 150 + 3 + 1.5 == 154.5 and round(150 * 0.03, 6) == 4.5


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


def boleto(c, t, t0, cx, cy, w, h, linhas, titulo="BOLETO", atraso=None):
    """a conta: folha branca com título, linhas [(rótulo, valor, t0[, cor])] e código de barras.
    atraso = (texto, t0): carimbo vermelho inclinado"""
    x, y = cx - w / 2, cy - h / 2

    def folha(a):
        s = skia.Paint(AntiAlias=True, Color=M.hexc("#000000", 0.10 * a))
        s.setMaskFilter(skia.MaskFilter.MakeBlur(skia.kNormal_BlurStyle, 14))
        r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 18, 18)
        c.save(); c.translate(6, 12); c.drawRRect(r, s); c.restore()
        c.drawRRect(r, M.paint(BR, a))
        c.drawRRect(r, M.paint(TINTA2, a, stroke=4))
        E.escreve(c, titulo, x + 40, y + 62, 36, "b", TINTA2, a)
        M.line(c, x + 40, y + 84, x + w - 40, y + 84, FIO, a, 3)
        bx = x + 40
        k = 0
        while bx < x + w - 40:  # código de barras
            lw = (3, 7, 4, 10, 3, 5)[k % 6]
            c.drawRect(skia.Rect.MakeXYWH(bx, y + h - 86, lw, 50), M.paint(TINTA, 0.85 * a))
            bx += lw + (6, 4, 8, 5)[k % 4]
            k += 1
    E.foco(c, t, t0, 0.5, folha)
    n = len(linhas)
    zona = h - 84 - 110
    for i, lin in enumerate(linhas):
        rot, val, ti = lin[:3]
        cor = lin[3] if len(lin) > 3 else TINTA
        yy = y + 84 + zona * (i + 0.5) / n + 20
        E.foco(c, t, ti, 0.45, lambda a, rot=rot, val=val, yy=yy, cor=cor: (
            E.escreve(c, rot, x + 44, yy, 50, "i", TINTA2, a),
            E.escreve(c, val, x + w - 44 - E.larg(val, "g", 58), yy, 58, "g", cor, a)))
    if atraso:
        s_, ta = atraso
        p = ease_back(prog(t, ta, 0.45))
        if p > 0:
            c.save(); c.translate(x + w - 30, y + 20); c.rotate(-12); c.scale(lerp(1.6, 1, min(p, 1)), lerp(1.6, 1, min(p, 1)))
            E.pilula(c, s_, 0, 0, 46, "g", fundo=None, cor=ERRADO, a=min(1, p), contorno=True)
            c.restore()


def recibo(c, t, cx, ytop, w, linhas, total, titulo=None, cor_total=None, size=64):
    """soma linha a linha: linhas = [(rótulo, valor, t0, cor)]; total = (valor, t0). Devolve o y do total"""
    x0, x1 = cx - w / 2, cx + w / 2
    if titulo:
        s_, tt = titulo
        cen(c, t, tt, s_, cx, ytop, 56, TINTA2, "i")
    y = ytop + 110
    for rot, val, ti, cor in linhas:
        E.foco(c, t, ti, 0.45, lambda a, rot=rot, val=val, y=y, cor=cor: (
            E.escreve(c, rot, x0, y, size * 0.8, "i", TINTA2, a),
            E.escreve(c, val, x1 - E.larg(val, "g", size), y, size, "g", cor, a)))
        y += size * 1.45
    v, tv = total
    q = ep(t, tv - 0.2, 0.4)
    if q > 0:
        M.line(c, x0, y - size * 0.75, lerp(x0, x1, q), y - size * 0.75, TINTA, 1, 5)
    E.foco(c, t, tv, 0.5, lambda a: (E.escreve(c, "total", x0, y + 30, size * 0.8, "i", TINTA2, a),
                                     E.pilula(c, v, x1 - E.larg(v, "g", size * 1.1) / 2 - size * 0.4, y + 8, size * 1.1, "g",
                                              fundo=cor_total, a=a)))
    return y


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    ka, kb, kc, kd, ke = (C[f"s01.{k}"] for k in "abcde")

    def um():
        boleto(c, t, C["s01"] + 0.2, 580, 540, 780, 640, [("valor", "R$ 200", ka), ("multa", "2%", kc), ("juros de mora", "3% ao mês", kd)],
               atraso=("10 dias de atraso", kb + 0.4))
        E.frase(c, t, w("s01", "Quanto"), ps("quanto você", "i", 80) + [("paga?", "g", 88, COR)], 1440, 330, "center", 0.12)
        cartao(c, t, ke, 1440, 560, "R$ 242", "se deu", False, 96, cor=ERRADO)
        E.frase(c, t, w("s01", "trinta") - 0.3, [("R$ 36", "g", 76, ERRADO)] + ps("a mais", "i", 72), 1440, 790, "center", 0.12)
        E.frase(c, t, w("s01", "devia"), ps("do que devia", "i", 64, TINTA2), 1440, 880, "center", 0.1)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t >= C["s02"]:
        ta, tb = C["s02.a"], C["s02.b"]
        E.foco(c, t, tb - 0.2, 0.7, lambda a: E.bola(c, 1500, 540, 250 * ease_back(prog(t, tb - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, ps("até o fim desta aula", "i", 90), XE, 360, passo=0.14)
        E.frase(c, t, w("s02", "conferir"), ps("conferir qualquer", "i", 90), XE, 500, passo=0.14)
        E.frase(c, t, w("s02", "conta"), [("conta atrasada", "g", 100, COR)], XE, 640)
        E.foco(c, t, tb + 0.1, 0.5, lambda a: (centro(c, "+ atalho", 1500, 525, 80, "g", E.SOBRE, a),
                                               centro(c, "de prova", 1500, 610, 80, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"] + 0.3, ps("você só precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "1", XE + 10, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisa", XE + 200, 700, 120, "i", TINTA, a))
    x, wc = 880, 900
    kb = C["s03.b"]
    p = ep(t, kb, 0.5)
    E.caixa_pontilhada(c, x, 300, wc, 420, p, prog_=p)
    E.frase(c, t, kb + 0.1, [("juros simples", "g", 72, COR)], x + 44, 410)
    E.foco(c, t, w("s03", "simples") + 0.2, 0.45, lambda a: E.formula(c, "J = C · i · t", x + 44, 530, 72, "g", TINTA, a))
    E.frase(c, t, w("s03", "taxa"), ps("taxa e tempo", "i", 60) + [("na mesma unidade", "g", 60, COR)], x + 44, 650, "left", 0.1)
    q = ease_io(prog(t, w("s03", "taxa") - 0.35, 0.5))
    E.cursor(c, x + wc - 30, lerp(450, 690, q), ep(t, kb, 0.4))
    E.frase(c, t, w("s03", "Se"), ps("faltou?", "i", 58, COR) + ps("procure no canal", "i", 58), x, 860, "left", 0.12)


# ---------------- duas cobranças ----------------
XL, XR = 520, 1400


def b_duas(c, t, C, b):
    a4, b4, c4 = C["s04.a"], C["s04.b"], C["s04.c"]
    a5, b5, c5 = C["s05.a"], C["s05.b"], C["s05.c"]
    E.frase(c, t, C["s04"] + 0.3, ps("conta atrasada tem", "i", 76) + [("2 cobranças diferentes", "g", 80, COR)], W / 2, 160, "center", 0.12)
    p = ep(t, a5, 0.5)
    if p > 0:
        M.line(c, W / 2 - 40, 280, W / 2 - 40, lerp(280, 1000, p), FIO, 1, 4)
    pil(c, t, b4, "multa", XL, 320, 80, fundo=TINTA)
    E.frase(c, t, w("s04", "punição"), ps("punição pelo atraso", "i", 56), XL, 450, "center", 0.1)
    E.foco(c, t, c4, 0.5, lambda a: E.pilula(c, "1 vez só", XL, 570, 64, "g", fundo=E.COR, a=a))
    E.frase(c, t, w("s04", "não"), ps("1 dia ou 1 mês: a mesma", "i", 50, TINTA2), XL, 690, "center", 0.08)
    E.frase(c, t, w("s04", "Em"), ps("em muitas contas:", "i", 54, TINTA2) + [("2%", "g", 64, COR)], XL, 820, "center", 0.1)
    pil(c, t, a5, "juros de mora", XR, 320, 80, fundo=E.COR)
    E.frase(c, t, w("s05", "aluguel"), ps("aluguel do dinheiro", "i", 54) + ps("pelos dias de atraso", "i", 54), XR, 450, "center", 0.08)
    E.frase(c, t, b5, [("mora", "g", 60, COR), ("=", "g", 60, TINTA2)] + ps("demora", "i", 60), XR, 560, "center", 0.12)
    E.frase(c, t, c5, ps("cresce", "i", 56) + [("a cada dia", "g", 60, COR)], XR, 670, "center", 0.1)
    for i in range(8):
        hh = 18 + 12 * i
        E.foco(c, t, c5 + 0.3 + 0.08 * i, 0.3, lambda a, i=i, hh=hh: M.rrect(c, XR - 200 + 52 * i, 790 - hh, 36, hh, 6, E.COR, a))
    E.frase(c, t, w("s05", "simples"), ps("juros simples,", "i", 50, TINTA2) + ps("sobre o valor da conta", "i", 50, TINTA2), XR, 870, "center", 0.08)
    E.frase(c, t, w("s05", "Por"), ps("pagou antes,", "i", 60) + [("menos mora", "g", 64, COR)], XR, 980, "center", 0.12)


# ---------------- multa ----------------
def b_multa(c, t, C, b):
    a, b_ = C["s06.a"], C["s06.b"]
    E.frase(c, t, a, [("multa:", "g", 84, COR)] + ps("2% de R$ 200", "i", 84), W / 2, 220, "center", 0.14)
    fluxo(c, t, 520, "R$ 200", "2% de", [(a + 0.6, "?"), (b_, "R$ 4")], a + 0.4, a + 0.6, a + 0.6, rot=("conta", "multa"), size=96)
    E.frase(c, t, w("s06", "Um"), [("1%", "g", 76, TINTA2), ("=", "g", 76, TINTA2), ("R$ 2", "g", 76)], W / 2, 820, "center", 0.2)
    E.frase(c, t, w("s06", "dois", 3), [("2%", "g", 76), ("=", "g", 76, TINTA2), ("R$ 4", "g", 76, COR)], W / 2, 940, "center", 0.2)


# ---------------- mora ----------------
def b_mora(c, t, C, b):
    a7, b7, c7, d7 = (C[f"s07.{k}"] for k in "abcd")
    a8, b8, c8 = C["s08.a"], C["s08.b"], C["s08.c"]
    a9, b9, c9 = C["s09.a"], C["s09.b"], C["s09.c"]
    if t < C["s08"]:
        def tela1():
            E.frase(c, t, C["s07"] + 0.3, ps("agora,", "i", 84) + [("a mora", "g", 90, COR)], W / 2, 170, "center", 0.14)
            E.frase(c, t, w("s07", "Na"), ps("luz e condomínio: costuma ser", "i", 56, TINTA2) + [("1% ao mês", "g", 60)], W / 2, 290, "center", 0.08)
            E.frase(c, t, w("s07", "As"), ps("nesta aula, taxas maiores: a conta sai redonda", "i", 52, TINTA2), W / 2, 380, "center", 0.07)
            pil(c, t, a7, "taxa: ao mês", 620, 540, 66, fundo=E.COR)
            E.foco(c, t, w("s07", "mas"), 0.4, lambda q: centro(c, "≠", W / 2, 565, 100, "g", ERRADO, q))
            pil(c, t, w("s07", "mas"), "atraso: em dias", 1300, 540, 66, fundo=TINTA)
            E.frase(c, t, w("s07", "taxa", 2), ps("precisam da", "i", 60) + [("mesma unidade", "g", 64, COR)], W / 2, 690, "center", 0.1)
            E.foco(c, t, b7, 0.5, lambda q: E.pilula(c, "mês comercial = 30 dias", W / 2, 840, 72, "g", fundo=TINTA, a=q))
        E.saida(c, t, c7 - 0.1, tela1)
        if t >= c7:
            E.frase(c, t, c7, ps("a mora", "i", 84) + [("ao dia", "g", 90, COR)], W / 2, 190, "center", 0.14)
            fluxo(c, t, 500, "3%", "÷ 30", [(c7 + 0.6, "?"), (d7, "0,1%")], c7 + 0.2, w("s07", "dividido"), c7 + 0.6, rot=("ao mês", "ao dia"), size=96)
            E.frase(c, t, c7 + 0.4, ps("mês comercial: 30 dias", "i", 56, TINTA2), W / 2, 800, "center", 0.08)
        return
    if t < C["s09"]:
        def tela2():
            E.frase(c, t, a8, [("0,1% de R$ 200", "g", 92)], W / 2, 210, "center")
            E.frase(c, t, w("s08", "Um"), [("1%", "g", 76, TINTA2), ("=", "g", 76, TINTA2), ("R$ 2", "g", 76, TINTA2)], W / 2, 360, "center", 0.2)
            E.frase(c, t, w("s08", "zero", 2), [("0,1%", "g", 84), ("=", "g", 84, TINTA2)] + ps("a décima parte", "i", 76), 1150, 510, "right", 0.15)
            E.foco(c, t, w("s08", "vinte"), 0.5, lambda q: E.pilula(c, "R$ 0,20 por dia", 1480, 485, 64, "g", a=q))
            for i in range(10):
                x = lerp(520, 1400, i / 9)
                E.foco(c, t, c8 + 0.1 * i, 0.35, lambda q, x=x, i=i: (E.bola(c, x, 700, 40, a=q),
                                                                      centro(c, str(i + 1), x, 716, 42, "g", E.SOBRE, q)))
            cen(c, t, c8, "dias de atraso", W / 2, 800, 48, TINTA2, "i")
            E.linha(c, t, [("10 × R$ 0,20", "g", 84, TINTA, c8 + 0.4), ("=", "g", 84, TINTA2, w("s08", "dois", 2)),
                           ("R$ 2", "g", 92, COR, w("s08", "dois", 2) + 0.2)], W / 2 - 120, 960, "center")
            cen(c, t, w("s08", "mora"), "de mora", 1380, 960, 64, COR, "i")
        E.saida(c, t, C["s09"] - 0.1, tela2)
        return
    E.frase(c, t, C["s09"] + 0.3, ps("conferindo", "i", 84) + [("pelo mês", "g", 88, COR)], W / 2, 200, "center", 0.14)
    E.frase(c, t, a9, [("10 dias", "g", 84), ("=", "g", 84, TINTA2)], 900, 420, "right", 0.2)
    E.foco(c, t, a9 + 0.4, 0.45, lambda q: E.formula(c, "f{1}{3}", 960, 440, 96, "g", COR, q))
    E.frase(c, t, a9 + 0.6, ps("do mês", "i", 76), 1070, 420)
    E.linha(c, t, [("1/3 de 3%", "g", 84, TINTA, w("s09", "um", 2)), ("=", "g", 84, TINTA2, b9), ("1%", "g", 92, COR, b9 + 0.2)], W / 2, 640, "center")
    E.linha(c, t, [("1% de R$ 200", "g", 84, TINTA, w("s09", "um", 4)), ("=", "g", 84, TINTA2, c9 - 0.4), ("R$ 2", "g", 92, COR, c9)], W / 2, 840, "center")
    selo_em(c, t, c9 + 0.5, 1480, 790, 46, True)


# ---------------- total ----------------
def b_total(c, t, C, b):
    a, b_, c_, d = (C[f"s10.{k}"] for k in "abcd")
    a11, b11, c11 = C["s11.a"], C["s11.b"], C["s11.c"]
    E.frase(c, t, C["s10"] + 0.3, [("total", "g", 88, COR)], W / 2, 150, "center")
    xa = lerp(W / 2, 540, ease_io(prog(t, C["s11"], 0.8)))
    recibo(c, t, xa, 230, 640, [("conta", "R$ 200", a, TINTA), ("+ multa", "R$ 4", b_, TINTA), ("+ mora", "R$ 2", c_, COR)], ("R$ 206", d),
           titulo=("10 dias de atraso", C["s10"] + 0.5))
    if t < C["s11"]:
        return
    recibo(c, t, 1380, 230, 640, [("conta", "R$ 200", a11 - 0.3, TINTA), ("+ multa", "R$ 4", b11, TINTA), ("+ mora", "R$ 6", w("s11", "seis"), COR)],
           ("R$ 210", c11), titulo=("30 dias de atraso", a11), cor_total=TINTA)
    cen(c, t, w("s11", "seis") + 0.3, "1 mês inteiro: 3%", 1380, 900, 46, COR, "i")
    cen(c, t, b11 + 0.3, "a multa não cresce", 540, 900, 46, TINTA2, "i")


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    a, b_, c_, d, e = (C[f"s12.{k}"] for k in "abcde")
    E.frase(c, t, C["s12"] + 0.3, ps("o erro do gancho:", "i", 80) + [("multa todo dia", "g", 84, ERRADO)], W / 2, 180, "center", 0.12)
    E.linha(c, t, [("R$ 4 × 10 dias", "g", 92, TINTA, w("s12", "Quatro")), ("=", "g", 92, TINTA2, b_ - 0.3), ("R$ 40", "g", 92, ERRADO, b_)], W / 2, 380, "center")
    E.linha(c, t, [("R$ 200 + R$ 40 + R$ 2", "g", 80, TINTA, w("s12", "Com")), ("=", "g", 80, TINTA2, c_), ("R$ 242", "g", 88, ERRADO, w("s12", "quarenta", 2))],
            W / 2, 560, "center")
    if t >= d:
        E.risco(c, 380, 590, 1540, 490, t, d, largura=12)
    E.foco(c, t, d, 0.5, lambda q: E.pilula(c, "multa: 1 vez só", W / 2, 730, 66, "g", a=q))
    E.foco(c, t, e, 0.5, lambda q: E.pilula(c, "cresce com o tempo: só a mora", W / 2, 850, 60, "g", fundo=TINTA, a=q))
    E.frase(c, t, e + 0.6, [("R$ 4", "g", 72)] + ps("+", "g", 72, TINTA2) + [("R$ 2", "g", 72, COR)] + ps("→", "g", 72, TINTA2) + [("R$ 206", "g", 80, COR)],
            W / 2, 1000, "center", 0.15)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    a13, b13, c13, d13 = (C[f"s13.{k}"] for k in "abcd")
    a14, b14, c14, d14 = (C[f"s14.{k}"] for k in "abcd")

    def regra():
        E.frase(c, t, C["s13"] + 0.3, [("o atalho", "g", 72, BR)], W / 2, 150, "center")
        E.frase(c, t, a13, ps("some", "i", 76, CLARO) + [("as porcentagens", "g", 80, BR)] + ps("antes", "i", 76, CLARO), W / 2, 290, "center", 0.12)
        E.linha(c, t, [("2%", "g", 110, BR, b13), ("+", "g", 110, CLARO, w("s13", "mais")), ("1%", "g", 110, BR, w("s13", "um")),
                       ("=", "g", 110, CLARO, w("s13", "três")), ("3%", "g", 120, CLARO, w("s13", "três") + 0.2)], W / 2, 500, "center")
        cen(c, t, b13 + 0.4, "multa", 650, 590, 48, CLARO, "i")
        cen(c, t, w("s13", "mora"), "mora em 10 dias", 1000, 590, 48, CLARO, "i")
        E.linha(c, t, [("3% de R$ 200", "g", 84, BR, c13), ("=", "g", 84, CLARO, w("s13", "dá")), ("R$ 6", "g", 92, CLARO, w("s13", "seis"))], W / 2, 760, "center")
        E.foco(c, t, d13, 0.5, lambda a: E.pilula(c, "R$ 206", W / 2 - 130, 920, 100, "g", fundo=CLARO, cor="#07070F", a=a))
        cen(c, t, w("s13", "numa"), "numa conta só", W / 2 + 270, 945, 64, CLARO, "i")
    E.saida(c, t, C["s14"] - 0.1, regra)
    if t < C["s14"]:
        return
    E.frase(c, t, C["s14"] + 0.2, ps("funciona porque", "i", 76, CLARO), W / 2, 170, "center", 0.12)
    E.frase(c, t, a14, ps("multa e mora são calculadas", "i", 64, CLARO) + [("sobre o mesmo valor", "g", 68, BR)], W / 2, 300, "center", 0.1)
    E.frase(c, t, w("s14", "conta"), ps("a conta original:", "i", 64, CLARO) + [("R$ 200", "g", 72, BR)], W / 2, 400, "center", 0.1)
    E.frase(c, t, b14 - 2.4, ps("não compensa quando o boleto traz", "i", 60, CLARO), W / 2, 590, "center", 0.08)
    E.frase(c, t, b14, [("a mora em reais por dia", "g", 72, BR)], W / 2, 690, "center")
    E.foco(c, t, c14, 0.45, lambda a: E.pilula(c, "R$ 0,07 por dia", 560, 860, 64, "g", fundo=E.COR, a=a))
    E.foco(c, t, d14, 0.5, lambda a: E.pilula(c, "× dias, e some", 1300, 860, 64, "g", fundo=CLARO, cor="#07070F", a=a))


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    a, b_, c_, d, e = (C[f"s15.{k}"] for k in "abcde")
    E.frase(c, t, C["s15"] + 0.3, ps("hora de", "i", 72, COR) + [("testar", "g", 72)], XE, 150)
    boleto(c, t, C["s15"] + 0.6, 640, 590, 820, 640, [("internet", "R$ 150", a), ("multa", "2%", c_), ("juros de mora", "1,5% ao mês", d)],
           titulo="CONTA DE INTERNET", atraso=("20 dias de atraso", b_ + 0.3))
    E.frase(c, t, e, ps("quanto", "i", 84) + [("foi pago?", "g", 88, COR)], 1500, 380, "center", 0.12)
    E.relogio(c, t, C["s16.a"], 1500, 700, 110)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    a, b_, c_, d = (C[f"s17.{k}"] for k in "abcd")
    a18, b18, c18 = C["s18.a"], C["s18.b"], C["s18.c"]

    def conta():
        E.linha(c, t, [("multa:", "i", 64, TINTA2, a), ("2% de R$ 150", "g", 76, TINTA, w("s17", "dois")), ("=", "g", 76, TINTA2, w("s17", "dá")),
                       ("R$ 3", "g", 80, COR, w("s17", "três"))], W / 2, 210, "center")
        E.linha(c, t, [("mora ao dia:", "i", 64, TINTA2, w("s17", "Mora")), ("1,5% ÷ 30", "g", 76, TINTA, b_), ("=", "g", 76, TINTA2, w("s17", "dá", 2)),
                       ("0,05%", "g", 80, COR, w("s17", "zero"))], W / 2, 420, "center")
        E.linha(c, t, [("em 20 dias:", "i", 64, TINTA2, c_), ("0,05% × 20", "g", 76, TINTA, c_ + 0.3), ("=", "g", 76, TINTA2, w("s17", "um", 2)),
                       ("1%", "g", 80, COR, w("s17", "um", 2) + 0.2)], W / 2, 630, "center")
        E.linha(c, t, [("mora:", "i", 64, TINTA2, d), ("1% de R$ 150", "g", 76, TINTA, d + 0.2), ("=", "g", 76, TINTA2, w("s17", "dá", 3)),
                       ("R$ 1,50", "g", 80, COR, w("s17", "um", 4))], W / 2, 840, "center")
    E.saida(c, t, C["s18"] - 0.1, conta)
    if t < C["s18"]:
        return
    E.linha(c, t, [("total:", "i", 64, TINTA2, C["s18"] + 0.1), ("R$ 150 + R$ 3 + R$ 1,50", "g", 76, TINTA, C["s18"] + 0.2),
                   ("=", "g", 76, TINTA2, a18 - 0.2)], W / 2 - 300, 250, "center")
    E.foco(c, t, a18, 0.5, lambda q: E.pilula(c, "R$ 154,50", 1460, 222, 80, "g", a=q))
    E.frase(c, t, w("s18", "Pelo"), ps("pelo", "i", 76) + [("atalho:", "g", 80, COR)], W / 2, 470, "center", 0.12)
    E.linha(c, t, [("2% + 1%", "g", 84, TINTA, b18), ("=", "g", 84, TINTA2, w("s18", "dá")), ("3%", "g", 92, COR, w("s18", "três"))], W / 2, 640, "center")
    E.linha(c, t, [("3% de R$ 150", "g", 84, TINTA, c18), ("=", "g", 84, TINTA2, w("s18", "dá", 2)), ("R$ 4,50", "g", 92, COR, w("s18", "quatro", 2))],
            W / 2, 820, "center")
    E.foco(c, t, w("s18", "Bateu"), 0.45, lambda q: E.pilula(c, "bateu!", W / 2, 970, 70, "g", fundo=CERTO, a=q))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    a19, b19, c19 = C["s19.a"], C["s19.b"], C["s19.c"]

    def resumo():
        E.frase(c, t, C["s19"] + 0.3, [("resumindo", "i", 92, COR)], XE, 200)
        E.passo(c, t, a19, 1, "multa", "uma vez só", 400)
        E.passo(c, t, b19, 2, "mora", "por dia, em juros simples", 600)
        E.passo(c, t, c19, 3, "tudo", "sobre o valor da conta", 800)
    E.saida(c, t, C["s20"] - 0.1, resumo)
    if t < C["s20"]:
        return
    a, b_, c_, d = (C[f"s20.{k}"] for k in "abcd")
    E.frase(c, t, C["s20"] + 0.1, [("próxima", "i", 84), ("aula", "i", 84)], XE, 300)
    E.frase(c, t, a, [("Juros compostos:", "g", 104, COR)], XE, 440)
    E.frase(c, t, a + 0.3, [("mês a mês", "g", 104, COR)], XE, 570)
    E.frase(c, t, w("s20", "mil"), [("R$ 1.000", "g", 72)] + ps("a", "i", 70) + [("10% ao mês", "g", 72)], XE, 720, "left", 0.15)
    E.frase(c, t, b_, [("→", "g", 72, TINTA2), ("R$ 1.331", "g", 76, COR)] + ps("em 3 meses", "i", 70), XE, 820, "left", 0.15)
    E.frase(c, t, w("s20", "não"), ps("e não", "i", 64) + [("R$ 1.300", "g", 68, ERRADO)], XE + 740, 820, "left", 0.12)
    E.foco(c, t, c_, 0.5, lambda q: E.pilula(c, "Inscreva-se", 1520, 300, 72, estilo="g", a=q))
    p = ease_io(prog(t, c_ + 0.3, 0.8))
    E.cursor(c, lerp(1800, 1640, p), lerp(620, 325, p), ep(t, c_ + 0.2, 0.4))
    E.frase(c, t, d, [("bons", "i", 120), ("estudos!", "i", 120, COR)], W / 2, 980, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, duas=b_duas, multa=b_multa, mora=b_mora, total=b_total, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
