"""Visual — Estudativo · MAT-FIN-005: juros simples contra compostos.

Linguagem da trilha Matemática Financeira, herdada de Porcentagem:
- cartao(): o valor num cartão branco (montante); maquina(): o fator (× 1,1) na caixa da cor da matéria.
- coluna(): o duelo lado a lado, simples (preto) × compostos (índigo), com a conta e o montante de cada um; quem ganha leva o selo.
- grafico(): na linguagem de Funções: plano com o eixo x (tempo) em índigo e o eixo y (montante) em preto;
  a reta dos simples (E.reta_pontos, preta) e a curva dos compostos (E.curva, índigo) se cruzam em 1 período.
Todo instante vem de C[...] (marcadores do roteiro) e dos tempos reais da voz."""
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Matemática Financeira")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-FIN-005_juros_simples_contra_compostos.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("um", "meio", "grafico", "atalho", "questao", "fim"))
BR = "#FFFFFF"
assert round(1000 * 1.21, 6) == 1210 and round(1000 * 1.42, 6) == 1420 and round(1.21 ** 2, 4) == 1.4641 and round(1000 * 1.4641, 2) == 1464.1
assert round(1000 * 1.48, 6) == 1480 and round(1000 * 1.02 ** 24) == 1608 and round(1000 * 1.105, 6) == 1105 and round(1.21 ** 0.5, 6) == 1.1
assert round(1000 * 1.1, 6) == 1100 and 1105 - 1100 == 5 and round(1.1 * 1.1, 6) == 1.21
assert round(1000 * 1.24, 6) == 1240 and round(1.12 ** 2, 4) == 1.2544 and round(1000 * 1.2544, 2) == 1254.4


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


XS, XC = 520, 1400  # coluna dos simples e dos compostos


def coluna(c, t, x, th, nome, linhas, valor, tv, ganha=None, y0=300, ycard=420, rot="montante", dg=190):
    """uma coluna do duelo: pílula com o nome, linhas [(fórmula, t0[, cor])] e o montante num cartão.
    ganha = instante do selo de quem ganha"""
    comp = nome == "compostos"
    pil(c, t, th, nome, x, y0, 60, fundo=E.COR if comp else TINTA)
    for i, lin in enumerate(linhas):
        s_, ti = lin[:2]
        cor = lin[2] if len(lin) > 2 else TINTA
        E.formula_em(c, t, ti, s_, x, y0 + 170 + 110 * i, 64, "g", cor, "center")
    if tv is not None:
        cartao(c, t, tv, x, y0 + ycard, valor, rot, comp, 84, w=520)
    if ganha is not None:
        E.foco(c, t, ganha, 0.45, lambda a: E.pilula(c, "ganham!", x, y0 + ycard + dg, 60, "g", fundo=CERTO, a=a))


def divisoria(c, t, t0, y0=240, y1=800):
    p = ep(t, t0, 0.6)
    if p > 0:
        M.line(c, W / 2, y0, W / 2, lerp(y0, y1, p), FIO, 1, 4)


def empate(c, t, t0, y=880):
    E.foco(c, t, t0, 0.5, lambda a: (E.pilula(c, "empate", W / 2, y, 72, "g", fundo=TINTA2, a=a)))


def eixos(c, t, P, t0, mx, my, nome_x="tempo (meses)", nome_y="montante (R$)", size=36):
    """plano da trilha Funções: eixo x (tempo) em índigo, eixo y (montante) em preto, grade fina"""
    x, y, w, h = P.caixa
    if t < t0:
        return
    q = ep(t, t0, 0.8)
    for v in mx:
        M.line(c, P.x(v), y, P.x(v), y + h, FIO, q, 2)
    for v in my:
        M.line(c, x, P.y(v), x + w, P.y(v), FIO, q, 2)
    M.arrow(c, x - 10, P.oy, x + w + 40, P.oy, E.COR, 1.0, 6, 24, ep(t, t0, 0.7))
    M.arrow(c, P.ox, y + h + 10, P.ox, y - 40, TINTA, 1.0, 6, 24, ep(t, t0 + 0.2, 0.7))
    E.foco(c, t, t0 + 0.5, 0.4, lambda a: E.escreve(c, nome_x, x + w - E.larg(nome_x, "i", 48) + 40, P.oy + 100, 48, "i", COR, a))
    E.foco(c, t, t0 + 0.6, 0.4, lambda a: E.escreve(c, nome_y, P.ox + 22, y - 30, 48, "i", TINTA, a))
    for i, v in enumerate(mx):
        X = P.x(v)
        s_ = E._num(v)
        E.foco(c, t, t0 + 0.2 + i * 0.05, 0.4, lambda a, X=X, s_=s_: (M.line(c, X, P.oy - 10, X, P.oy + 10, E.COR, a, 4),
                                                                     centro(c, s_, X, P.oy + 14 + size, size, "b", TINTA2, a)), sobe=6)
    for i, v in enumerate(my):
        Y = P.y(v)
        s_ = E._num(v)
        E.foco(c, t, t0 + 0.3 + i * 0.05, 0.4, lambda a, Y=Y, s_=s_: (M.line(c, P.ox - 10, Y, P.ox + 10, Y, TINTA, a, 4),
                                                                     E.escreve(c, s_, P.ox - 22 - E.larg(s_, "b", size), Y + size * 0.36, size, "b", TINTA2, a)), sobe=6)


def simples(x):
    return 1000 * (1 + 0.21 * x)


def compostos(x):
    return 1000 * 1.21 ** x


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    ka, kb, kc = C["s01.a"], C["s01.b"], C["s01.c"]

    def um():
        E.frase(c, t, ka + 0.1, [("juros compostos", "g", 92, COR)] + ps("rendem", "i", 88), W / 2, 330, "center", 0.14)
        E.frase(c, t, w("s01", "sempre"), [("sempre mais", "g", 92)] + ps("que", "i", 88) + [("juros simples", "g", 92)], W / 2, 470, "center", 0.14)
        E.frase(c, t, w("s01", "Parece"), ps("parece verdade...", "i", 64, TINTA2), W / 2, 620, "center", 0.1)
        if t >= kb:
            E.risco(c, 300, 500, 1620, 360, t, kb, largura=14)
        E.foco(c, t, kb + 0.2, 0.45, lambda a: E.pilula(c, "falso!", 1600, 620, 72, "g", fundo=ERRADO, a=a))
        E.frase(c, t, kc, ps("em um caso,", "i", 80) + [("os simples ganham", "g", 84, COR)], W / 2, 850, "center", 0.14)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t >= C["s02"]:
        ta, tb = C["s02.a"], C["s02.b"]
        E.foco(c, t, tb - 0.2, 0.7, lambda a: E.bola(c, 1500, 540, 250 * ease_back(prog(t, tb - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, ps("até o fim desta aula", "i", 90), XE, 330, passo=0.14)
        E.frase(c, t, w("s02", "dizer"), ps("dizer", "i", 92) + [("quem rende mais", "g", 96, COR)], XE, 480, passo=0.14)
        E.frase(c, t, w("s02", "em"), ps("em qualquer prazo", "i", 84), XE, 620, passo=0.12)
        E.foco(c, t, tb + 0.1, 0.5, lambda a: (centro(c, "+ atalho", 1500, 525, 80, "g", E.SOBRE, a),
                                               centro(c, "de prova", 1500, 610, 80, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    ka, kb, kc = C["s03.a"], C["s03.b"], C["s03.c"]
    E.frase(c, t, C["s03"] + 0.3, ps("você só precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, ka, 0.5, lambda a: E.escreve(c, "2", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, ka + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, wc = 880, 900
    p = ep(t, kb, 0.5)
    E.caixa_pontilhada(c, x, 200, wc, 300, p, prog_=p)
    E.frase(c, t, kb + 0.1, [("a fórmula dos compostos", "i", 62)], x + 44, 285)
    E.foco(c, t, w("s03", "capital"), 0.45, lambda a: E.formula(c, "M = C · (1 + i)^{t}", x + 44, 420, 84, "g", COR, a))
    p = ep(t, kc, 0.5)
    E.caixa_pontilhada(c, x, 570, wc, 260, p, prog_=p)
    E.frase(c, t, kc + 0.1, [("expoente em fração", "i", 62)], x + 44, 655)
    E.foco(c, t, w("s03", "nove"), 0.45, lambda a: E.formula(c, "9^{1/2} = r{9}", x + 44, 775, 76, "g", COR, a))
    q = ease_io(prog(t, kc - 0.35, 0.5))
    E.cursor(c, x + wc - 30, lerp(470, 800, q), ep(t, kb, 0.4))
    E.frase(c, t, w("s03", "Se"), ps("faltou alguma?", "i", 58, COR) + ps("procure no canal", "i", 58), x, 1000, "left", 0.12)


# ---------------- em 1 período ----------------
def b_um(c, t, C, b):
    a4, b4, c4 = C["s04.a"], C["s04.b"], C["s04.c"]
    a5, b5, c5, d5 = (C[f"s05.{k}"] for k in "abcd")

    def tela1():
        E.frase(c, t, C["s04"] + 0.3, ps("compare com", "i", 80), W / 2, 200, "center", 0.12)
        cartao(c, t, a4, 520, 440, "R$ 1.000", "capital", False, 92)
        pil(c, t, b4, "21% ao mês", 1300, 440, 76, fundo=E.COR)
        E.frase(c, t, w("s04", "É"), ps("taxa absurda: só para as contas saírem redondas", "i", 56, TINTA2), W / 2, 640, "center", 0.07)
        E.frase(c, t, w("s04", "Fator"), ps("fator", "i", 72), 840, 860, "right")
        maquina(c, t, c4, 1080, 840, "× 1,21", 80)
    E.saida(c, t, C["s05"] - 0.1, tela1)
    if t < C["s05"]:
        return
    E.frase(c, t, a5, ps("em", "i", 84) + [("1 mês", "g", 90, COR)], W / 2, 170, "center", 0.14)
    divisoria(c, t, a5)
    coluna(c, t, XS, a5 + 0.3, "simples", [("21% de R$ 1.000", w("s05", "vinte"))], "R$ 1.210", b5)
    coluna(c, t, XC, w("s05", "compostos"), "compostos", [("R$ 1.000 · 1,21", c5 - 0.4)], "R$ 1.210", w("s05", "mil", 4))
    empate(c, t, d5)
    E.frase(c, t, w("s05", "Ainda"), ps("ainda não houve juro sobre juro", "i", 56, TINTA2), W / 2, 1010, "center", 0.08)


# ---------------- mais de 1 período ----------------
def b_mais(c, t, C, b):
    a6, b6, c6, d6, e6 = (C[f"s06.{k}"] for k in "abcde")
    a7, b7, c7 = C["s07.a"], C["s07.b"], C["s07.c"]

    def tela1():
        E.frase(c, t, a6, ps("em", "i", 84) + [("2 meses", "g", 90, COR)], W / 2, 170, "center", 0.14)
        divisoria(c, t, a6)
        coluna(c, t, XS, a6 + 0.3, "simples", [("42% de R$ 1.000", w("s06", "quarenta"))], "R$ 1.420", b6)
        coluna(c, t, XC, w("s06", "compostos"), "compostos", [("1,21^{2} = 1,4641", c6)], "R$ 1.464,10", d6, ganha=e6)
        E.frase(c, t, w("s06", "No"), ps("no 2º mês, os juros do 1º também renderam", "i", 56, TINTA2), W / 2, 1010, "center", 0.07)
    E.saida(c, t, C["s07"] - 0.1, tela1)
    if t < C["s07"]:
        return
    E.frase(c, t, C["s07"] + 0.3, ps("quanto mais tempo,", "i", 76) + [("maior a vantagem", "g", 80, COR)], W / 2, 170, "center", 0.12)
    pil(c, t, a7, "2% ao mês, por 2 anos (24 meses)", W / 2, 290, 56, fundo=TINTA)
    divisoria(c, t, a7 + 0.3, 360)
    coluna(c, t, XS, b7 - 1.0, "simples", [("48% de R$ 1.000", b7 - 0.6)], "R$ 1.480", w("s07", "mil", 2), y0=440)
    coluna(c, t, XC, w("s07", "compostos"), "compostos", [("R$ 1.000 · 1,02^{24}", w("s07", "potência"))], "≈ R$ 1.608", c7 + 0.6, y0=440)
    E.formula_em(c, t, w("s07", "tabela"), "1,02^{24} ≈ 1,6084  (tabela)", XC, 1030, 42, "g", TINTA2, "center")


# ---------------- menos de 1 período ----------------
def b_meio(c, t, C, b):
    a8, b8, c8, d8 = (C[f"s08.{k}"] for k in "abcd")
    a9, b9, c9, d9, e9, f9 = (C[f"s09.{k}"] for k in "abcdef")
    a10, b10, c10 = (C[f"s10.{k}"] for k in "abc")
    if t < C["s10"]:
        def tela1():
            E.frase(c, t, a8, ps("em", "i", 84) + [("menos de 1 mês?", "g", 90, COR)], W / 2, 150, "center", 0.14)
            pil(c, t, b8, "21% ao mês, por meio mês", W / 2, 260, 56, fundo=TINTA)
            divisoria(c, t, b8 + 0.3, 330, 940)
            coluna(c, t, XS, w("s08", "Nos"), "simples", [("metade da taxa: 10,5%", c8)], "R$ 1.105", d8, ganha=f9, y0=380, ycard=440, rot=None, dg=165)
            coluna(c, t, XC, C["s09"] + 0.3, "compostos", [("t = f{1}{2}", a9, COR)], "R$ 1.100", e9, y0=380, ycard=440, rot=None)
            eq_f(c, t, [("1,21^{1/2}", TINTA, b9), ("=", TINTA2, c9), ("r{1,21}", TINTA, c9 + 0.2), ("=", TINTA2, d9), ("1,1", COR, w("s09", "um", 5))],
                 XC, 640, 64)
            E.formula_em(c, t, w("s09", "porque"), "porque 1,1^{2} = 1,21", XC, 705, 40, "g", TINTA2, "center")
            E.frase(c, t, f9 + 0.4, ps("por", "i", 52) + [("R$ 5", "g", 56)], XS + 190, 1010, "left", 0.1)
        E.saida(c, t, C["s10"] - 0.1, tela1)
        return
    E.frase(c, t, C["s10"] + 0.2, [("por quê?", "g", 88, COR)], W / 2, 160, "center")
    cen(c, t, w("s10", "compostos"), "compostos", 300, 290, 56, COR, "g")
    cadeia(c, t, 450, ["R$ 1.000", "R$ 1.100", "R$ 1.210"], ["× 1,1", "× 1,1"], [a10 - 0.3, a10 + 0.4, b10 + 0.6], [a10, b10],
           rot=["início", "meio mês", "1 mês"], size=72)
    E.frase(c, t, w("s10", "fecham"), [("10%", "g", 64), ("+", "g", 64, TINTA2), ("10% sobre o que rendeu", "g", 64), ("=", "g", 64, TINTA2), ("21%", "g", 68, COR)],
            W / 2, 680, "center", 0.15)
    E.frase(c, t, w("s10", "Então"), ps("cada metade rende só", "i", 60) + [("10%", "g", 64, COR)], W / 2, 790, "center", 0.1)
    E.frase(c, t, c10, [("simples:", "g", 64)] + ps("cada metade rende", "i", 60) + [("10,5%", "g", 66)] + ps("e ganham", "i", 60),
            W / 2, 930, "center", 0.12)


# ---------------- o gráfico ----------------
def b_grafico(c, t, C, b):
    a, b_, c_, d, e = (C[f"s11.{k}"] for k in "abcde")
    P = E.Plano(300, 200, 1100, 720, 0, 2.2, 1000, 1500)
    eixos(c, t, P, C["s11"] - 0.3, [0.5, 1, 1.5, 2], [1100, 1200, 1300, 1400, 1500])
    E.foco(c, t, C["s11"] + 0.1, 0.4, lambda q: E.escreve(c, "1.000", P.ox - 22 - E.larg("1.000", "b", 36), P.oy + 13, 36, "b", TINTA2, q))
    E.reta_pontos(c, t, a, P, (0, 1000), (2, 1420), cor=TINTA, pontos=False, d=1.0)
    E.curva(c, t, b_, P, compostos, 0, 2.2, d=1.2, cor=E.COR)
    E.foco(c, t, a + 0.6, 0.4, lambda q: E.pilula(c, "simples: reta", 1640, 620, 46, "g", fundo=TINTA, a=q))
    E.foco(c, t, b_ + 0.6, 0.4, lambda q: E.pilula(c, "compostos: curva", 1640, 720, 46, "g", fundo=E.COR, a=q))
    E.ponto(c, t, c_, P, 1, 1210, "1 período", guias=True, cor=TINTA, r=16, lado=(-1, -1))
    # antes de 1: a reta por cima (½ mês: R$ 1.105 × R$ 1.100); depois: a curva na frente (2 meses: R$ 1.420 × R$ 1.464,10)
    p = ep(t, d, 0.5)
    if p > 0:
        M.rrect(c, P.x(0) + 4, P.caixa[1], P.x(1) - P.x(0) - 4, P.caixa[3], 0, TINTA, 0.06 * p)
    E.foco(c, t, d, 0.45, lambda q: E.pilula(c, "antes: ganham os simples", P.x(0.5) + 20, P.y(1430), 38, "g", fundo=TINTA, a=q))
    E.ponto(c, t, d + 0.3, P, 0.5, 1105, None, cor=TINTA, r=11)
    E.ponto(c, t, d + 0.5, P, 0.5, 1100, None, cor=E.COR, r=11)
    E.foco(c, t, d + 0.5, 0.4, lambda q: E.escreve(c, "R$ 1.105 > R$ 1.100", P.x(0.5) - 110, P.y(1040), 34, "g", TINTA, q))
    q = ep(t, e, 0.5)
    if q > 0:
        M.rrect(c, P.x(1), P.caixa[1], P.x(2.2) - P.x(1), P.caixa[3], 0, E.COR, 0.06 * q)
    E.foco(c, t, e, 0.45, lambda q: E.pilula(c, "depois: ganham os compostos", P.x(1.62), P.y(1090), 38, "g", fundo=E.COR, a=q))
    E.ponto(c, t, e + 0.3, P, 2, 1420, "R$ 1.420", cor=TINTA, r=13, lado=(1, 1), size=38)
    E.ponto(c, t, e + 0.5, P, 2, 1464.1, "R$ 1.464,10", cor=E.COR, r=13, lado=(-1, -1), size=38)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    a, b_, c_, d, e = (C[f"s12.{k}"] for k in "abcde")
    E.frase(c, t, C["s12"] + 0.3, [("o erro comum", "g", 96, ERRADO)], W / 2, 170, "center")
    E.frase(c, t, a, ps("achar que compostos", "i", 72) + [("sempre rendem mais", "g", 76, ERRADO)], W / 2, 300, "center", 0.12)
    E.frase(c, t, b_ - 1.4, ps("prazo menor que 1 período?", "i", 68), 900, 440, "right", 0.1)
    E.foco(c, t, b_, 0.45, lambda q: E.pilula(c, "é o contrário", 1220, 415, 60, "g", fundo=TINTA, a=q))
    E.frase(c, t, w("s12", "cuidado"), ps("cuidado:", "i", 70, ERRADO) + ps("o período é", "i", 70), 900, 610, "right", 0.1)
    E.foco(c, t, c_, 0.45, lambda q: E.pilula(c, "o da taxa", 1130, 585, 64, "g", a=q))
    E.frase(c, t, d, [("taxa ao ano:", "g", 64)] + ps("6 meses", "i", 64) + [("< 1 período", "g", 64, COR)], W / 2, 790, "center", 0.12)
    E.frase(c, t, e, [("taxa ao mês:", "g", 64)] + ps("15 dias", "i", 64) + [("< 1 período", "g", 64, COR)], W / 2, 920, "center", 0.12)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    a13, b13, c13, d13 = (C[f"s13.{k}"] for k in "abcd")
    a14, b14, c14 = C["s14.a"], C["s14.b"], C["s14.c"]

    def regra():
        E.frase(c, t, C["s13"] + 0.3, [("o atalho", "g", 72, BR)], W / 2, 150, "center")
        E.frase(c, t, a13, ps("compare o prazo com", "i", 72, CLARO) + [("1 período da taxa", "g", 76, BR)], W / 2, 290, "center", 0.12)
        for y, tl, rel, res, cor in ((480, b13, "prazo = 1", "empate", CLARO), (650, c13, "prazo < 1", "ganham os simples", BR),
                                     (820, d13, "prazo > 1", "ganham os compostos", E.mix(E.COR, BR, 0.55))):
            E.foco(c, t, tl, 0.45, lambda a, y=y, rel=rel: E.escreve(c, rel, 420, y, 84, "g", BR, a))
            p = ep(t, tl + 0.3, 0.4)
            if p > 0:
                M.arrow(c, 840, y - 28, 960, y - 28, CLARO, p, 5, 18, p)
            E.foco(c, t, tl + 0.4, 0.45, lambda a, y=y, res=res, cor=cor: E.pilula(c, res, 990 + E.larg(res, "g", 60) / 2 + 33, y - 28, 60, "g",
                                                                                    fundo=cor, cor="#07070F", a=a))
    E.saida(c, t, C["s14"] - 0.1, regra)
    if t < C["s14"]:
        return
    E.frase(c, t, C["s14"] + 0.2, ps("funciona porque", "i", 76, CLARO), W / 2, 180, "center", 0.12)
    E.frase(c, t, a14, ps("o", "i", 72, CLARO) + [("juro sobre juro", "g", 76, BR)] + ps("só aparece", "i", 72, CLARO), W / 2, 330, "center", 0.12)
    E.frase(c, t, w("s14", "depois"), ps("depois do 1º período", "i", 72, CLARO), W / 2, 440, "center", 0.1)
    E.frase(c, t, w("s14", "Não"), ps("a pergunta é", "i", 64, CLARO) + [("quanto a mais?", "g", 72, BR)], W / 2, 640, "center", 0.12)
    E.frase(c, t, w("s14", "e", 1), ps("e não quem ganha", "i", 56, CLARO), W / 2, 740, "center", 0.1)
    E.foco(c, t, c14, 0.5, lambda a: E.pilula(c, "faça as contas", W / 2, 890, 80, "g", fundo=CLARO, cor="#07070F", a=a))


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    a, b_, c_, d = (C[f"s15.{k}"] for k in "abcd")
    E.frase(c, t, C["s15"] + 0.3, ps("hora de", "i", 72, COR) + [("testar", "g", 72)], XE, 150)
    E.frase(c, t, w("s15", "Uma"), ps("uma aplicação paga", "i", 72), XE, 320, "left", 0.12)
    pil(c, t, a + 0.3, "12% ao ano", 1060, 296, 72, fundo=E.COR)
    E.frase(c, t, w("s15", "Quem"), ps("quem rende mais:", "i", 64) + [("simples", "g", 68)] + ps("ou", "i", 64) + [("compostos?", "g", 68, COR)],
            XE, 480, "left", 0.1)
    for i, (tl, s_) in enumerate(((b_, "em 6 meses?"), (c_, "em 1 ano?"), (d, "em 2 anos?"))):
        E.foco(c, t, tl, 0.45, lambda a, i=i, s_=s_: (E.bola(c, XE + 42, 640 + 130 * i, 42, a=a),
                                                       centro(c, "abc"[i], XE + 42, 640 + 130 * i + 18, 50, "g", E.SOBRE, a),
                                                       E.escreve(c, s_, XE + 110, 640 + 130 * i + 24, 72, "g", TINTA, a)))
    E.relogio(c, t, C["s16.a"], 1500, 780, 110)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    a, b_, c_, d = (C[f"s17.{k}"] for k in "abcd")
    a18, b18, c18 = C["s18.a"], C["s18.b"], C["s18.c"]

    def conta():
        E.frase(c, t, C["s17"] + 0.3, [("taxa ao ano", "g", 72)] + ps("→", "g", 72, TINTA2) + ps("o período é", "i", 70), 1020, 190, "right", 0.12)
        E.foco(c, t, a, 0.45, lambda q: E.pilula(c, "1 ano", 1200, 165, 72, "g", a=q))
        for i, (tl, prazo, rel, res, cor) in enumerate(((b_, "6 meses", "= meio período", "ganham os simples", TINTA),
                                                        (c_, "1 ano", "= 1 período", "empate", TINTA2),
                                                        (d, "2 anos", "mais de 1 período", "ganham os compostos", E.COR))):
            y = 400 + 200 * i
            E.foco(c, t, tl, 0.45, lambda q, y=y, i=i, prazo=prazo: (E.bola(c, XE + 42, y - 22, 42, a=q),
                                                                    centro(c, "abc"[i], XE + 42, y - 4, 50, "g", E.SOBRE, q),
                                                                    E.escreve(c, prazo, XE + 110, y, 72, "g", TINTA, q)))
            E.foco(c, t, tl + 0.4, 0.45, lambda q, y=y, rel=rel: E.escreve(c, rel, 620, y, 64, "i", TINTA2, q))
            E.foco(c, t, w("s17", ["ganham", "empate", "ganham"][i], [1, 1, 2][i]), 0.45,
                   lambda q, y=y, res=res, cor=cor: E.pilula(c, res, 1440, y - 22, 60, "g", fundo=cor, a=q))
    E.saida(c, t, C["s18"] - 0.1, conta)
    if t < C["s18"]:
        return
    E.frase(c, t, C["s18"] + 0.2, [("R$ 1.000", "g", 80)] + ps("em", "i", 76) + [("2 anos", "g", 80, COR)], W / 2, 170, "center", 0.12)
    divisoria(c, t, C["s18"] + 0.4)
    coluna(c, t, XS, w("s18", "nos"), "simples", [("24% de R$ 1.000", w("s18", "vinte"))], "R$ 1.240", a18)
    coluna(c, t, XC, w("s18", "nos", 2), "compostos", [("1,12^{2} = 1,2544", b18)], "R$ 1.254,40", c18, ganha=c18 + 1.2)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    a19, b19, c19 = (C[f"s19.{k}"] for k in "abc")

    def resumo():
        E.frase(c, t, C["s19"] + 0.3, [("resumindo", "i", 92, COR)], XE, 200)
        E.passo(c, t, a19, 1, "em 1 período", "empate", 400)
        E.passo(c, t, b19, 2, "antes", "ganham os simples", 600)
        E.passo(c, t, c19, 3, "depois", "ganham os compostos", 800)
    E.saida(c, t, C["s20"] - 0.1, resumo)
    if t < C["s20"]:
        return
    a, b_, c_, d = (C[f"s20.{k}"] for k in "abcd")
    E.frase(c, t, C["s20"] + 0.1, [("próxima", "i", 84), ("aula", "i", 84)], XE, 260)
    E.frase(c, t, w("s20", "conta"), [("Juros compostos:", "g", 96, COR)], XE, 390)
    E.frase(c, t, w("s20", "contrário"), [("achar o capital ou o tempo", "g", 84, COR)], XE, 510)
    E.frase(c, t, a, ps("quanto aplicar hoje para ter", "i", 64) + [("R$ 1.210", "g", 68)] + ps("em", "i", 64) + [("2 anos?", "g", 68)],
            XE, 670, "left", 0.12)
    E.frase(c, t, b_, ps("em quanto tempo o dinheiro", "i", 64) + [("dobra?", "g", 68, COR)], XE, 780, "left", 0.12)
    E.foco(c, t, c_, 0.5, lambda q: E.pilula(c, "Inscreva-se", 1520, 240, 72, estilo="g", a=q))
    p = ease_io(prog(t, c_ + 0.3, 0.8))
    E.cursor(c, lerp(1800, 1640, p), lerp(560, 265, p), ep(t, c_ + 0.2, 0.4))
    E.frase(c, t, d, [("bons", "i", 120), ("estudos!", "i", 120, COR)], W / 2, 980, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, um=b_um, mais=b_mais, meio=b_meio, grafico=b_grafico, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
