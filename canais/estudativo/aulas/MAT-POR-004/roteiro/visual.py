"""Visual — Estudativo · MAT-POR-004: fatores de aumento e de desconto.
Linguagem da trilha Porcentagem (cartao, maquina, fluxo: as mesmas peças de MAT-POR-006): antes = cartão escuro, a máquina índigo
é o fator, depois = cartão na cor da matéria. Peça desta aula: cem() é o preço antigo como 100%, com a taxa crescendo à direita
(aumento) ou ficando cinza e riscada no fim (desconto).
A voz é real: os marcadores vêm de C[...] e, onde a tela precisa da palavra exata, fala(cena, palavra) lê o tempos.json."""
import json
import math
from pathlib import Path
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Porcentagem")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-POR-004_fatores_de_aumento_e_desconto.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("longo", "desconto", "atalho", "questao", "fim"))
BR = "#FFFFFF"
assert 200 * 0.15 == 30 and 200 + 30 == 230 and 200 * 115 == 23000 and round(200 * 1.15, 2) == 230
assert 250 * 0.8 == 200 and 100 - 20 == 80 and 100 + 8 == 108 and 100 - 35 == 65
assert 180 * 112 == 20160 and round(180 * 1.12, 2) == 201.6 and 600 * 85 == 51000 and round(600 * 0.85, 2) == 510
assert 50 - 5 == 45 and round(50 * 0.9, 2) == 45


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- tempo da palavra dita ----------------
_TEMPOS = json.loads((Path(__file__).resolve().parents[1] / "audio" / "tempos.json").read_text(encoding="utf-8"))
_CENAS = {s["id"]: s for s in _TEMPOS["scenes"]}


def fala(sid, palavra, k=1):
    """instante em que a k-ésima `palavra` da cena começa a ser dita"""
    s = _CENAS[sid]
    n = 0
    for tk in s["tokens"]:
        if tk["disp"].lower().strip(".,:;?!") == palavra:
            n += 1
            if n == k:
                return s["start"] + tk["t0"]
    raise KeyError((sid, palavra, k))


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


# ---------------- linguagem da trilha Porcentagem ----------------
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




# ---------------- peças desta aula ----------------
def cem(c, t, x, y, w, h, taxa, t0, tt, tb=None, rot_b=None, a=1.0):
    """o preço antigo como uma barra de 100% (entra em t0). taxa > 0: um pedaço de taxa% cresce à direita (em tt);
    taxa < 0: o fim da barra fica cinza e riscado (em tt). tb/rot_b: chave por baixo com o total que o cliente paga"""
    q = ep(t, t0, 0.5) * a
    if q <= 0:
        return
    k = w / 100
    rr = E._casco(c, x, y, w, h, 14, q)
    c.save(); c.clipRRect(rr, True)
    c.drawRect(skia.Rect.MakeXYWH(x, y, w, h), M.paint(E.CLARO, q * 0.55))
    p = ease_io(prog(t, tt, 0.7)) if tt is not None else 0
    if taxa < 0 and p > 0:
        c.drawRect(skia.Rect.MakeXYWH(x + w - (-taxa) * k * p, y, (-taxa) * k * p, h), M.paint(CINZA, q * 0.8))
    c.restore()
    c.drawRRect(rr, M.paint(TINTA, q, stroke=4))
    if taxa < 0:
        cx = x + w - (-taxa) * k / 2
        centro(c, "100%", x + (100 + taxa) * k / 2, y + h / 2 + 24, 66, "g", TINTA, q * (1 - p))
        E.foco(c, t, tt + 0.5, 0.4, lambda a_: centro(c, f"−{-taxa}%", cx, y - 30, 60, "g", ERRADO, a_ * q)) if tt is not None else None
        if tt is not None and t >= tt + 0.5:
            E.risco(c, x + w - (-taxa) * k + 14, y + h - 14, x + w - 14, y + 14, t, tt + 0.5, cor=ERRADO, largura=8)
    else:
        centro(c, "100%", x + w / 2, y + h / 2 + 24, 66, "g", TINTA, q)
        if p > 0:
            r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x + w + 10, y, taxa * k * p, h), 14, 14)
            c.drawRRect(r, M.paint(E.COR, q))
            E.foco(c, t, tt + 0.5, 0.4, lambda a_: centro(c, f"+{taxa}%", x + w + 10 + taxa * k / 2, y + h / 2 + 22, 54, "g", BR, a_ * q))
    if tb is not None:
        fim = x + w + 10 + taxa * k if taxa > 0 else x + (100 + taxa) * k
        E.chave(c, x + 4, fim - 4, y + h + 20, COR, ep(t, tb, 0.5), 26, 6)
        E.foco(c, t, tb + 0.2, 0.45, lambda a_: centro(c, rot_b, (x + fim) / 2, y + h + 120, 80, "g", COR, a_ * q))


def bolinha(c, t, t0, n, x, y, r=40):
    E.foco(c, t, t0, 0.45, lambda a: (E.bola(c, x, y, r, a=a), centro(c, str(n), x, y + r * 0.42, r * 1.15, "g", E.SOBRE, a)))


def rot_maq(c, t, t0, s, x, y, cor=None):
    """rótulo embaixo da máquina: 'fator de aumento'"""
    E.foco(c, t, t0, 0.45, lambda a: E.pilula(c, s, x, y, 48, "g", fundo=cor or TINTA, a=a))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    ka, kb, kc, kd = C["s01.a"], C["s01.b"], C["s01.c"], C["s01.d"]

    def um():
        fluxo(c, t, 380, "R$ 200", "+ 15%", "?", ka, kb, kb + 0.4, rot=("antes", "depois"))
        E.frase(c, t, fala("s01", "o"), ps("o normal:", "i", 66, TINTA2), XE, 640, "left", 0.1)
        bolinha(c, t, fala("s01", "calcular"), 1, XE + 30, 735)
        E.frase(c, t, fala("s01", "calcular"), [("o aumento", "g", 66)], XE + 100, 760)
        bolinha(c, t, fala("s01", "somar"), 2, XE + 30, 855)
        E.frase(c, t, fala("s01", "somar"), [("somar", "g", 66)], XE + 100, 880)
        E.foco(c, t, kc, 0.5, lambda a: E.escreve(c, "2 contas", 900, 830, 110, "g", ERRADO, a))
        if t >= kd - 0.3:
            E.risco(c, 880, 850, 1350, 740, t, kd - 0.3, largura=12)
        E.foco(c, t, kd, 0.5, lambda a: num_bola(c, "1 só", 1580, 790, 130, 84, a))
    E.saida(c, t, C["s02"] - 0.1, um)
    if t >= C["s02"]:
        ta, tb = C["s02.a"], C["s02.b"]
        E.foco(c, t, tb - 0.2, 0.7, lambda a: E.bola(c, 1500, 540, 250 * ease_back(prog(t, tb - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, ps("até o fim desta aula", "i", 90), XE, 330, passo=0.14)
        E.frase(c, t, fala("s02", "aumentar"), [("aumentar", "g", 100, COR)], XE, 490)
        E.frase(c, t, fala("s02", "descontar"), ps("e", "i", 90) + [("descontar", "g", 100, COR)], XE, 630, passo=0.12)
        E.frase(c, t, fala("s02", "multiplicação"), ps("com", "i", 80) + [("1 multiplicação", "g", 84)], XE, 780, passo=0.12)
        E.foco(c, t, tb + 0.1, 0.5, lambda a: (centro(c, "+ atalho", 1500, 525, 80, "g", E.SOBRE, a),
                                               centro(c, "de prova", 1500, 610, 80, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"] + 0.3, ps("você só precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "2", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 900, 880
    itens = (("s03.b", "Trocar porcentagem", "por decimal"), ("s03.c", "Porcentagem de", "um valor"))
    for i, (k, l1, l2) in enumerate(itens):
        y = 230 + i * 270
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 220, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 66)], x + 44, y + 92)
        E.frase(c, t, C[k] + 0.3, [(l2, "g", 66, COR)], x + 44, y + 178)
    q = ease_io(prog(t, C["s03.c"] - 0.35, 0.5))
    E.cursor(c, x + w - 30, lerp(420, 690, q), ep(t, C["s03.b"], 0.4))
    E.frase(c, t, fala("s03", "se"), ps("faltou alguma?", "i", 58, COR) + ps("procure no canal", "i", 58), x, 900, "left", 0.12)


# ---------------- jeito longo ----------------
def b_longo(c, t, C, b):
    a4, b4, c4 = C["s04.a"], C["s04.b"], C["s04.c"]
    E.frase(c, t, C["s04"] + 0.3, ps("primeiro, do", "i", 80) + [("jeito longo", "g", 80, COR)], XE, 180, "left", 0.12)
    bolinha(c, t, a4, 1, XE + 40, 330, 46)
    E.frase(c, t, a4, [("15% de 200", "g", 84)], XE + 120, 360)
    E.linha(c, t, [("10% = 20", "g", 64, TINTA2, fala("s04", "dez")), ("+", "g", 64, TINTA2, fala("s04", "cinco")),
                   ("5% = 10", "g", 64, TINTA2, fala("s04", "cinco") + 0.2)], XE + 120, 470)
    E.linha(c, t, [("aumento:", "i", 84, TINTA, b4 - 0.3), ("R$ 30", "g", 90, COR, b4)], XE + 120, 600)
    bolinha(c, t, c4, 2, XE + 40, 750, 46)
    E.linha(c, t, [("200 + 30", "g", 84, TINTA, c4), ("=", "g", 84, TINTA2, fala("s04", "dá", 3)), ("R$ 230", "g", 90, COR, fala("s04", "duzentos", 3))],
            XE + 120, 780)
    E.foco(c, t, c4 + 1.2, 0.5, lambda a: E.pilula(c, "2 contas", 1500, 560, 80, "g", fundo=TINTA, a=a))


# ---------------- fator de aumento ----------------
def b_aumento(c, t, C, b):
    a5, b5, c5 = C["s05.a"], C["s05.b"], C["s05.c"]
    a6, b6, c6 = C["s06.a"], C["s06.b"], C["s06.c"]
    a7, b7 = C["s07.a"], C["s07.b"]

    def cinco():
        E.frase(c, t, C["s05"] + 0.3, ps("agora pense", "i", 84) + [("assim", "g", 84, COR)], W / 2, 200, "center", 0.12)
        E.frase(c, t, fala("s05", "preço"), ps("o preço antigo é", "i", 66, TINTA2), 260, 380, "left", 0.1)
        cem(c, t, 260, 440, 1100, 170, 15, a5, fala("s05", "mais"), c5, "115%")
        E.frase(c, t, fala("s05", "cliente"), ps("o cliente paga", "i", 66, TINTA2), 1200, 380, "left", 0.1)
    E.saida(c, t, C["s06"] - 0.1, cinco)
    if t < C["s06"]:
        return
    E.linha(c, t, [("115%", "g", 96, TINTA, C["s06"] + 0.3), ("=", "g", 96, TINTA2, fala("s06", "são")), ("115/100", "g", 96, TINTA, fala("s06", "cento", 3)),
                   ("=", "g", 96, TINTA2, a6 - 0.2), ("1,15", "g", 96, COR, a6)], W / 2, 220, "center")
    y = 520
    fluxo(c, t, y, "R$ 200", "× 1,15", [(b6, "?"), (c6, "R$ 230")], b6, fala("s06", "vezes"), b6 + 0.3, rot=("antes", "depois"))

    def seis():
        E.linha(c, t, [("sem vírgula:", "i", 66, TINTA2, fala("s06", "sem")), ("200 × 115", "g", 76, TINTA, fala("s06", "duzentos", 2)),
                       ("=", "g", 76, TINTA2, fala("s06", "dá")), ("23000", "g", 76, TINTA, fala("s06", "vinte"))], W / 2, 830, "center")
        E.linha(c, t, [("2 casas:", "i", 66, TINTA2, fala("s06", "com")), ("230,00", "g", 76, COR, c6)], W / 2, 950, "center")
    E.saida(c, t, C["s07"] - 0.1, seis)
    if t < C["s07"]:
        return
    rot_maq(c, t, a7, "fator de aumento", XM, y + 160, E.COR)
    E.frase(c, t, fala("s07", "o", 2), ps("o número que você", "i", 66) + [("multiplica", "g", 66, COR)], W / 2, 830, "center", 0.12)
    E.frase(c, t, b7, ps("nem calcula o aumento", "i", 66) + [("separado", "g", 66, COR)], W / 2, 950, "center", 0.12)


# ---------------- fator de desconto ----------------
def b_desconto(c, t, C, b):
    a8, b8, c8, d8 = C["s08.a"], C["s08.b"], C["s08.c"], C["s08.d"]
    a9, b9, c9 = C["s09.a"], C["s09.b"], C["s09.c"]
    E.frase(c, t, C["s08"] + 0.3, ps("com desconto, a mesma ideia,", "i", 72) + [("tirando", "g", 72, COR)], W / 2, 160, "center", 0.12)
    y = 400
    fluxo(c, t, y, "R$ 250", [(c8, "− 20%"), (a9, "× 0,8")], [(b8, "?"), (fala("s09", "duzentos", 2), "R$ 200")], b8, c8, c8 + 0.3, rot=("antes", "depois"))
    E.saida(c, t, a9 - 0.1, lambda: cem(c, t, 410, 720, 1100, 150, -20, d8, fala("s08", "menos"), fala("s08", "oitenta"), "80%"))
    if t < a9 - 0.1:
        return
    E.linha(c, t, [("80%", "g", 100, TINTA, a9 - 0.1), ("=", "g", 100, TINTA2, a9), ("0,8", "g", 100, COR, a9 + 0.2)], 520, 800, "center")
    E.linha(c, t, [("250 × 0,8", "g", 84, TINTA, b9), ("=", "g", 84, TINTA2, fala("s09", "dá")), ("200", "g", 84, COR, fala("s09", "duzentos", 2))],
            1340, 800, "center")
    rot_maq(c, t, c9, "fator de desconto", XM, y + 160, TINTA)


# ---------------- regra ----------------
def b_regra(c, t, C, b):
    a10, b10, c10, d10, e10 = C["s10.a"], C["s10.b"], C["s10.c"], C["s10.d"], C["s10.e"]
    E.frase(c, t, C["s10"] + 0.3, ps("a", "i", 80) + [("regra", "g", 80, COR)], W / 2, 150, "center", 0.12)
    for x, ti, nome, conta, fundo in ((520, a10, "aumento", "100% + taxa", E.COR), (1400, b10, "desconto", "100% − taxa", TINTA)):
        E.foco(c, t, ti, 0.45, lambda a, x=x, nome=nome, fundo=fundo: E.pilula(c, nome, x, 290, 64, "g", fundo=fundo, a=a))
        cen(c, t, ti + 0.9, conta, x, 440, 92, COR)
    E.frase(c, t, c10, ps("passe para", "i", 66, TINTA2) + [("decimal", "g", 66)] + ps("e", "i", 66, TINTA2) + [("multiplique", "g", 66)], W / 2, 570, "center", 0.12)
    for x, ti, taxa, tot, tp, fat, tf in ((520, d10, "+ 8%", "108%", fala("s10", "cento", 2), "× 1,08", fala("s10", "fator")),
                                          (1400, e10, "− 35%", "65%", fala("s10", "sessenta"), "× 0,65", fala("s10", "fator", 2))):
        cen(c, t, ti, taxa, x, 730, 80, TINTA)
        cen(c, t, tp, "→  " + tot, x, 830, 76, TINTA2)
        maquina(c, t, tf, x, 940, fat, 64)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    a11, b11, c11 = C["s11.a"], C["s11.b"], C["s11.c"]
    a12, b12 = C["s12.a"], C["s12.b"]
    E.frase(c, t, C["s11"] + 0.3, [("cuidado", "g", 96, ERRADO)] + ps("com um erro comum", "i", 90), W / 2, 170, "center", 0.12)
    y = 400

    def onze():
        cen(c, t, a11, "aumento de 5%", 520, y + 30, 84, TINTA)
        p = ep(t, fala("s11", "vira"), 0.5)
        if p > 0:
            M.arrow(c, 860, y, 1080, y, TINTA2, p, 6, 20, p)
        maquina(c, t, fala("s11", "um", 2), 1300, y, "× 1,5", 80)
        if t >= c11 + 0.6:
            E.risco(c, 1150, y + 80, 1450, y - 80, t, c11 + 0.6, largura=14)
        E.linha(c, t, [("1,5", "g", 90, TINTA, fala("s11", "um", 3)), ("=", "g", 90, TINTA2, fala("s11", "são")), ("150%", "g", 90, ERRADO, b11)], W / 2, 650, "center")
        E.frase(c, t, c11, ps("isso é aumento de", "i", 76) + [("50%", "g", 84, ERRADO)], W / 2, 800, "center", 0.12)
    E.saida(c, t, C["s12"] - 0.1, onze)
    if t < C["s12"]:
        return
    E.linha(c, t, [("100 + 5", "g", 96, TINTA, C["s12"]), ("=", "g", 96, TINTA2, fala("s12", "dá")), ("105%", "g", 96, TINTA, a12)], W / 2, y + 30, "center")
    E.frase(c, t, fala("s12", "fator"), ps("o fator certo:", "i", 70, TINTA2), 600, 680, "right")
    s, xv, yv = 190, 870, 720
    xs = E._centros("1,05", xv, s)
    E.foco(c, t, b12, 0.5, lambda a: E.numero(c, "1,05", xv, yv, s, a=a, cor=CERTO))
    E.foco(c, t, b12 + 0.6, 0.45, lambda a: E.selo(c, xs[3] + 220, yv - 70, 55, True, a))
    q = ep(t, fala("s12", "zero", 2), 0.4)
    if q > 0:
        E.caixa_pontilhada(c, xs[2] - s * 0.38, yv - s * 0.8, s * 0.76, s * 0.95, q, COR, prog_=q)
        E.foco(c, t, fala("s12", "casa"), 0.45, lambda a: centro(c, "casa dos décimos", xs[2], yv + 110, 56, "i", COR, a))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    a13, b13, c13, d13, e13 = C["s13.a"], C["s13.b"], C["s13.c"], C["s13.d"], C["s13.e"]
    a14, b14, c14 = C["s14.a"], C["s14.b"], C["s14.c"]

    def treze():
        E.frase(c, t, C["s13"] + 0.3, ps("o atalho:", "i", 84, CLARO) + [("leia o fator ao contrário", "g", 80, BR)], W / 2, 190, "center", 0.12)
        for y, tm, fat, tp, paga, tr, res in ((430, b13, "× 0,7", fala("s13", "setenta"), "paga 70%", c13, "desconto de 30%"),
                                              (730, d13, "× 1,25", fala("s13", "foi", 2), "paga 125%", e13, "aumento de 25%")):
            maquina(c, t, tm, 400, y, fat, 76)
            p = ep(t, tp, 0.5)
            if p > 0:
                M.arrow(c, 620, y, 760, y, CLARO, p, 6, 20, p)
            cen(c, t, tp, paga, 960, y + 28, 70, CLARO, "i")
            E.foco(c, t, tr, 0.5, lambda a, y=y, res=res: E.pilula(c, res, 1490, y, 64, "g", fundo=CLARO, cor="#07070F", a=a))
    E.saida(c, t, C["s14"] - 0.1, treze)
    if t < C["s14"]:
        return
    E.frase(c, t, a14, ps("o fator é", "i", 76, CLARO) + [("o preço novo", "g", 76, BR)], W / 2, 220, "center", 0.12)
    E.frase(c, t, fala("s14", "em"), ps("em % do antigo", "i", 76, CLARO), W / 2, 330, "center", 0.12)
    E.frase(c, t, fala("s14", "já"), ps("nem sempre compensa:", "i", 66, CLARO), XE, 560, "left", 0.1)
    E.frase(c, t, b14, [("10% de desconto em R$ 50", "g", 80, BR)], XE, 700)
    E.linha(c, t, [("tire", "i", 76, CLARO, fala("s14", "tire")), ("5", "g", 84, BR, fala("s14", "cinco")), ("e pague", "i", 76, CLARO, fala("s14", "pague"))], XE, 840)
    E.foco(c, t, c14, 0.5, lambda a: (E.bola(c, 1500, 790, 130, a=a), centro(c, "R$ 45", 1500, 818, 76, "g", BR, a)))


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    a15, b15, c15, d15, e15 = C["s15.a"], C["s15.b"], C["s15.c"], C["s15.d"], C["s15.e"]
    E.frase(c, t, C["s15"] + 0.3, ps("hora de testar", "i", 72, COR), XE, 140)
    fluxo(c, t, 330, "R$ 180", "+ 12%", "?", a15, b15, b15 + 0.3, rot=("conta de luz", "depois"), size=80)
    fluxo(c, t, 610, "R$ 600", "− 15%", "?", c15, d15, d15 + 0.3, rot=("fogão", "depois"), size=80)
    E.saida(c, t, C["s16"] - 0.1, lambda: E.frase(c, t, e15, ps("qual é o", "i", 80) + [("fator", "g", 80, COR)] + ps("e o", "i", 80) +
                                                  [("valor novo?", "g", 80, COR)], W / 2, 900, "center", 0.12))
    if t >= C["s16"]:
        E.relogio(c, t, C["s16.a"], W / 2, 830, 95)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    a17, b17, c17 = C["s17.a"], C["s17.b"], C["s17.c"]
    a18, b18, c18 = C["s18.a"], C["s18.b"], C["s18.c"]
    y = 330

    def luz():
        fluxo(c, t, y, "R$ 180", [(C["s17"], "+ 12%"), (a17, "× 1,12")], [(C["s17"], "?"), (c17, "R$ 201,60")], C["s17"], C["s17"], C["s17"],
              rot=("conta de luz", "depois"), size=80)
        E.linha(c, t, [("100 + 12", "g", 76, TINTA, fala("s17", "cem")), ("=", "g", 76, TINTA2, fala("s17", "dá")), ("112%", "g", 76, TINTA, fala("s17", "cento"))],
                W / 2, 600, "center")
        E.linha(c, t, [("180 × 112", "g", 76, TINTA, b17), ("=", "g", 76, TINTA2, fala("s17", "dá", 2)), ("20160", "g", 76, TINTA, fala("s17", "vinte"))],
                W / 2, 730, "center")
        E.frase(c, t, fala("s17", "com"), ps("2 casas:", "i", 66, TINTA2), 760, 900, "right")
        E.foco(c, t, fala("s17", "com") + 0.1, 0.45, lambda q: E.anda(c, t, "20160", 5, [(fala("s17", "casas"), 3)], 820, 900, 110, tv=fala("s17", "duas")))
    E.saida(c, t, C["s18"] - 0.1, luz)
    if t < C["s18"]:
        return
    fluxo(c, t, y, "R$ 600", [(C["s18"], "− 15%"), (a18, "× 0,85")], [(C["s18"], "?"), (c18, "R$ 510")], C["s18"], C["s18"], C["s18"],
          rot=("fogão", "depois"), size=80)
    E.linha(c, t, [("100 − 15", "g", 76, TINTA, fala("s18", "cem")), ("=", "g", 76, TINTA2, fala("s18", "dá")), ("85%", "g", 76, TINTA, fala("s18", "oitenta"))],
            W / 2, 600, "center")
    E.linha(c, t, [("600 × 85", "g", 76, TINTA, b18), ("=", "g", 76, TINTA2, fala("s18", "dá", 2)), ("51000", "g", 76, TINTA, fala("s18", "cinquenta"))],
            W / 2, 730, "center")
    E.frase(c, t, fala("s18", "com"), ps("2 casas:", "i", 66, TINTA2), 760, 900, "right")
    E.foco(c, t, fala("s18", "com") + 0.1, 0.45, lambda q: E.anda(c, t, "51000", 5, [(fala("s18", "casas"), 3)], 820, 900, 110, tv=fala("s18", "duas")))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s19"] + 0.2, [("resumindo", "i", 92, COR)], W / 2, 210, "center")
        for i, (k, s) in enumerate((("s19.a", "aumento: 100% + taxa"), ("s19.b", "desconto: 100% − taxa"), ("s19.c", "decimal e × uma vez só"))):
            y = 390 + i * 190
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 330, y - 30, 56, a=a),
                                                         E.escreve(c, str(i + 1), 330 - E.larg(str(i + 1), "g", 64) / 2, y - 7, 64, "g", "#FFFFFF", a)))
            E.frase(c, t, C[k] + 0.1, [(s, "g", 90)], 430, y)
    E.saida(c, t, C["s20"] - 0.1, resumo)
    if t < C["s20"]:
        return
    a20, b20, c20, d20 = C["s20.a"], C["s20.b"], C["s20.c"], C["s20.d"]
    E.frase(c, t, fala("s20", "próxima"), [("próxima", "i", 84), ("aula:", "i", 84), ("é o contrário", "g", 84, COR)], XE, 200, "left", 0.14)
    fluxo(c, t, 520, "R$ 80", "?", "R$ 100", a20, b20, fala("s20", "cem"), rot=("antes", "depois"), size=84)
    E.frase(c, t, b20, ps("de", "i", 84) + [("quantos %", "g", 84, COR)] + ps("foi o aumento?", "i", 84), W / 2, 780, "center", 0.12)
    E.foco(c, t, c20, 0.5, lambda a: E.pilula(c, "Inscreva-se", 1600, 180, 64, estilo="g", a=a))
    p = ease_io(prog(t, c20 + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1700, p), lerp(420, 205, p), ep(t, c20 + 0.2, 0.4))
    E.frase(c, t, d20, [("bons", "i", 120), ("estudos!", "i", 120, COR)], W / 2, 980, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, longo=b_longo, aumento=b_aumento, desconto=b_desconto, regra=b_regra,
              erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
