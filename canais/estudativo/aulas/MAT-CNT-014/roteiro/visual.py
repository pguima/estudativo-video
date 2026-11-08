"""Visual — Estudativo · MAT-CNT-014: probabilidade da união.
Mesma linguagem da trilha Contagem e Probabilidade (MAT-CNT-001 a 013): igual_bola() com o resultado na esfera, bloco() em volta de um grupo,
linha() com contas e frações numa linha (MAT-CNT-013), E.venn como na MAT-CON-003 (A = reis, B = copas, AB = rei de copas).
Símbolos ∪ ∩ desenhados por tx() (a fonte da casa não tem), como na MAT-CON-002.
Peças desta aula:
- carta(): carta de baralho com valor e naipe (♥ ♦ ♠ ♣ desenhados em naipe()); verso() o verso na cor da matéria.
- bolinha(): bolinha numerada da urna, que pinta por múltiplo.
Sem voz ainda: todo instante vem de C[...] (cenas e marcadores), nunca de segundos fixos."""
import math
from fractions import Fraction as Fr
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Contagem e Probabilidade")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-CNT-014_probabilidade_uniao.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("baralho", "venn", "formula", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
VERM = "#D94B3D"
AMBAR = "#E8920C"
VALORES = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
NAIPES = ["copas", "espadas", "ouros", "paus"]
BARALHO = [(v, n) for n in NAIPES for v in VALORES]
REIS = [x for x in BARALHO if x[0] == "K"]
COPAS = [x for x in BARALHO if x[1] == "copas"]
assert len(BARALHO) == 52 == 4 * 13 and len(REIS) == 4 and len(COPAS) == 13 and [x for x in REIS if x in COPAS] == [("K", "copas")]
assert len(set(REIS) | set(COPAS)) == 16 == 3 + 1 + 12 == 4 + 13 - 1 and Fr(16, 52) == Fr(4, 13) and round(16 / 52 * 100) == 31 and Fr(4, 13) < Fr(1, 3)
assert 4 + 4 == 8 and Fr(8, 52) == Fr(2, 13) and 4 + 13 == 17 and 60 + 50 - 30 == 80
M3 = [n for n in range(1, 31) if n % 3 == 0]
M5 = [n for n in range(1, 31) if n % 5 == 0]
assert len(M3) == 10 and len(M5) == 6 and [n for n in M3 if n in M5] == [15, 30] and 10 + 6 - 2 == 14 and Fr(14, 30) == Fr(7, 15) < Fr(1, 2)


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- símbolos ∪ ∩ (a fonte da casa não tem: desenhados, como na MAT-CON-002) ----------------
_TRACO = dict(g=0.15, b=0.1, m=0.075, i=0.052, s=0.052)
_DESENHA = "∪∩"


def _simb(c, ch, x, y, size, est, cor, a):
    sw = size * _TRACO[est]
    x0, x1 = x + size * 0.1 + sw / 2, x + size * 0.68 - sw / 2
    top, bot = y - size * 0.68 + sw / 2, y - size * 0.02 - sw / 2
    rr = (x1 - x0) / 2
    pa = skia.Path()
    if ch == "∪":
        pa.moveTo(x0, top); pa.lineTo(x0, bot - rr)
        pa.arcTo(skia.Rect.MakeLTRB(x0, bot - 2 * rr, x1, bot), 180, -180, False)
        pa.lineTo(x1, top)
    else:
        pa.moveTo(x0, bot); pa.lineTo(x0, top + rr)
        pa.arcTo(skia.Rect.MakeLTRB(x0, top, x1, top + 2 * rr), 180, 180, False)
        pa.lineTo(x1, bot)
    p = M.paint(cor, a, stroke=sw)
    p.setStrokeCap(skia.Paint.kButt_Cap); p.setStrokeJoin(skia.Paint.kMiter_Join)
    c.drawPath(pa, p)


def _pedacos(s):
    out, cur = [], ""
    for ch in s:
        if ch in _DESENHA:
            if cur:
                out.append(cur); cur = ""
            out.append(ch)
        else:
            cur += ch
    if cur:
        out.append(cur)
    return out


def tw(s, est, size):
    return sum(size * 0.78 if p in _DESENHA else E.larg(p, est, size) for p in _pedacos(s))


def tx(c, s, x, y, size, est="g", cor=None, a=1.0, align="left"):
    """como E.escreve, com ∪ e ∩; align left/center/right"""
    if a <= 0:
        return
    cor = cor or TINTA
    w = tw(s, est, size)
    x = x - w / 2 if align == "center" else x - w if align == "right" else x
    for p in _pedacos(s):
        if p in _DESENHA:
            _simb(c, p, x, y, size, est, cor, a)
            x += size * 0.78
        else:
            E.escreve(c, p, x, y, size, est, cor, a)
            x += E.larg(p, est, size)


def txe(c, t, t0, s, x, y, size, est="g", cor=None, align="left"):
    E.foco(c, t, t0, 0.45, lambda a: tx(c, s, x, y, size, est, cor, a, align))


# ---------------- peças da trilha (MAT-CNT-002 a 013) ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    """uma frase, palavra a palavra, no mesmo estilo"""
    return [(w, est, size, cor) for w in txt.split()]


def igual_bola(c, t, t0, x, y, txt, r=120, size=None, cor=None, escuro=False, t_igual=None):
    """'=' em x e o resultado numa esfera à direita; y = centro. Devolve o centro da esfera."""
    size = size or r * (0.72 if len(txt) <= 2 else 0.56 if len(txt) == 3 else 0.46 if len(txt) == 4 else 0.38)
    E.sinal(c, t, t0 - 0.2 if t_igual is None else t_igual, "=", x, y, r * 0.75, BR if escuro else TINTA)
    bx = x + r * 0.55 + r
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, bx, y, r, cor, a), centro(c, txt, bx, y + size * 0.36, size, "g", E.SOBRE, a)))
    return bx


def nota(c, t, t0, x, y, txt, size=46, cor=TINTA2, estilo="b"):
    E.foco(c, t, t0, 0.45, lambda a: centro(c, txt, x, y, size, estilo, cor, a))


def bloco(c, x0, x1, cy, h, a=1.0, cor=None, largura=7):
    """contorno do grupo: quem está dentro anda junto"""
    if a <= 0:
        return
    m = 26
    r = skia.RRect.MakeRectXY(skia.Rect.MakeLTRB(x0 - m, cy - h / 2 - m, x1 + m, cy + h / 2 + m), 34, 34)
    c.drawRRect(r, M.paint(cor or E.COR, 0.08 * a))
    c.drawRRect(r, M.paint(cor or E.COR, a, stroke=largura))


def larg_parte(p, size):
    return tw(p, "g", size) if isinstance(p, str) else max(E.larg(str(p[0]), "g", size), E.larg(str(p[1]), "g", size)) + size * 0.2


def linha(c, t, x, y, size, partes, align="left", gap=None):
    """conta numa linha: partes = [(texto ou (n, d), instante[, cor])]; y = altura da barra das frações. Devolve o x de cada parte e o fim"""
    gap = size * 0.28 if gap is None else gap
    ws = [larg_parte(p[0], size) for p in partes]
    tot = sum(ws) + gap * (len(partes) - 1)
    xx = x - tot / 2 if align == "center" else x - tot if align == "right" else x
    xs = []
    for (p, t0, *cor), w in zip(partes, ws):
        cor = cor[0] if cor else TINTA
        xs.append(xx)
        if isinstance(p, str):
            E.foco(c, t, t0, 0.45, lambda a, p=p, xx=xx, cor=cor: tx(c, p, xx, y + size * 0.34, size, "g", cor, a))
        else:
            E.fr(c, t, t0, p[0], p[1], xx + w / 2, y, size, cor)
        xx += w + gap
    return xs, xx - gap


def pil_esq(c, t, t0, x, y, txt, size=46, fundo=None, cor=BR):
    """pílula com a borda esquerda em x"""
    w = E.larg(txt, "g", size) + size * 1.1
    E.foco(c, t, t0, 0.45, lambda a: E.pilula(c, txt, x + w / 2, y, size, estilo="g", fundo=fundo or TINTA2, cor=cor, a=a))


# ---------------- peças desta aula: cartas ----------------
def naipe(c, cx, cy, s, tipo, a=1.0, cor=None):
    """naipe desenhado, de altura ~s, centrado em (cx, cy)"""
    if a <= 0:
        return
    cor = cor or (VERM if tipo in ("copas", "ouros") else TINTA)
    p = M.paint(cor, a)
    h = s / 2
    pa = skia.Path()
    if tipo == "copas":
        pa.moveTo(cx, cy + h)
        pa.cubicTo(cx - h * 1.9, cy - h * 0.1, cx - h * 0.9, cy - h * 1.5, cx, cy - h * 0.45)
        pa.cubicTo(cx + h * 0.9, cy - h * 1.5, cx + h * 1.9, cy - h * 0.1, cx, cy + h)
        c.drawPath(pa, p)
    elif tipo == "ouros":
        pa.moveTo(cx, cy - h); pa.lineTo(cx + h * 0.75, cy); pa.lineTo(cx, cy + h); pa.lineTo(cx - h * 0.75, cy); pa.close()
        c.drawPath(pa, p)
    elif tipo == "espadas":
        pa.moveTo(cx, cy - h)
        pa.cubicTo(cx + h * 1.8, cy + h * 0.15, cx + h * 0.8, cy + h * 1.2, cx, cy + h * 0.35)
        pa.cubicTo(cx - h * 0.8, cy + h * 1.2, cx - h * 1.8, cy + h * 0.15, cx, cy - h)
        c.drawPath(pa, p)
        c.drawPath(_pe(cx, cy, h), p)
    else:  # paus
        rr = h * 0.42
        for dx, dy in ((0, -h * 0.5), (-h * 0.5, h * 0.05), (h * 0.5, h * 0.05)):
            c.drawCircle(cx + dx, cy + dy, rr, p)
        c.drawPath(_pe(cx, cy, h), p)


def _pe(cx, cy, h):
    pa = skia.Path()
    pa.moveTo(cx - h * 0.12, cy + h * 0.2); pa.lineTo(cx + h * 0.12, cy + h * 0.2)
    pa.lineTo(cx + h * 0.4, cy + h); pa.lineTo(cx - h * 0.4, cy + h); pa.close()
    return pa


def carta(c, cx, cy, w, valor, tipo, a=1.0, borda=None, apaga=1.0):
    """carta de baralho de largura w (altura 1,4 w) com o valor no canto e o naipe grande no meio"""
    if a <= 0:
        return
    a = a * apaga
    h = w * 1.4
    r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2, cy - h / 2, w, h), w * 0.12, w * 0.12)
    sh = skia.Paint(AntiAlias=True, Color=M.hexc("#000000", 0.12 * a))
    sh.setMaskFilter(skia.MaskFilter.MakeBlur(skia.kNormal_BlurStyle, 6))
    c.save(); c.translate(0, 5); c.drawRRect(r, sh); c.restore()
    c.drawRRect(r, M.paint(BR, a))
    c.drawRRect(r, M.paint(borda or TINTA2, a, stroke=7 if borda else max(2, w * 0.025)))
    cor = VERM if tipo in ("copas", "ouros") else TINTA
    sz = w * 0.34
    E.escreve(c, valor, cx - w / 2 + w * 0.1, cy - h / 2 + sz * 1.05, sz, "g", cor, a)
    naipe(c, cx + w * 0.06, cy + h * 0.12, w * 0.46, tipo, a)


def verso(c, cx, cy, w, a=1.0, k=1.0):
    """verso da carta na cor da matéria; k = escala horizontal (virar)"""
    if a <= 0:
        return
    h = w * 1.4
    c.save(); c.translate(cx, cy); c.scale(max(0.04, k), 1)
    r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(-w / 2, -h / 2, w, h), w * 0.12, w * 0.12)
    c.drawRRect(r, M.paint(E.COR, a))
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(-w / 2 + 14, -h / 2 + 14, w - 28, h - 28), w * 0.08, w * 0.08), M.paint(BR, 0.6 * a, stroke=4))
    c.drawCircle(0, 0, w * 0.18, M.paint(BR, 0.6 * a, stroke=4))
    c.restore()


def bolinha(c, cx, cy, r, n, a=1.0, cor=None, anel=None):
    """bolinha numerada da urna; cor = cor do miolo (branca se None); anel = cor do contorno grosso"""
    if a <= 0:
        return
    c.drawCircle(cx, cy, r, M.paint(cor or BR, a))
    c.drawCircle(cx, cy, r, M.paint(anel or TINTA2, a, stroke=9 if anel else 3))
    centro(c, str(n), cx, cy + r * 0.3, r * 0.8, "g", BR if cor else TINTA, a)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def pergunta():
        E.foco(c, t, C["s01.a"], 0.5, lambda a: verso(c, 380, 430, 230, a))
        E.frase(c, t, C["s01.a"] + 0.2, [("tire", "i", 80), ("1", "g", 88, COR), ("carta", "g", 84)], 640, 330)
        E.frase(c, t, C["s01.b"], [("rei", "g", 92, COR), ("ou", "i", 84), ("copas?", "g", 92, COR)], 640, 470)
        E.foco(c, t, C["s01.b"] + 0.5, 0.45, lambda a: carta(c, 1400, 440, 130, "K", "espadas", a))
        E.foco(c, t, C["s01.b"] + 0.7, 0.45, lambda a: carta(c, 1570, 440, 130, "7", "copas", a))
        y = 790
        xs, xf = linha(c, t, 380, y, 110, [("4 + 13 =", C["s01.c"] - 0.4), ((17, 52), C["s01.c"], ERRADO)])
        if t >= C["s01.d"]:
            E.risco(c, xs[1] - 10, y + 120, xf + 10, y - 120, t, C["s01.d"], largura=12)
        E.foco(c, t, C["s01.d"] + 0.3, 0.5, lambda a: E.pilula(c, "errou por 1 carta só", xf + 330, y, 54, estilo="g", fundo=ERRADO, a=a))
    E.saida(c, t, C["s02"] - 0.1, pergunta)

    if t >= C["s02"]:
        E.foco(c, t, C["s02.c"] - 0.2, 0.7, lambda a: E.bola(c, 1480, 520, 300 * ease_back(prog(t, C["s02.c"] - 0.2, 0.7))), blur=0)
        E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 96), XE, 300)
        E.frase(c, t, C["s02.a"] + 0.9, [("a", "i", 100), ("chance", "g", 120, COR), ("de", "i", 100)], XE, 450)
        E.frase(c, t, C["s02.b"] - 0.3, [("um", "i", 100), ("evento", "i", 100), ("ou", "g", 120, COR), ("outro", "i", 100)], XE, 600)
        pil_esq(c, t, C["s02.b"] + 0.6, XE, 760, "sem contar nada 2 vezes", 50)
        E.foco(c, t, C["s02.c"] + 0.2, 0.5, lambda a: (E.centro(c, "+ atalho", 1480, 490, 88, "g", BR, a),
                                                      E.centro(c, "de prova", 1480, 600, 88, "g", BR, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"] + 0.1, [("você", "i", 84), ("vai", "i", 84), ("usar", "i", 84), ("duas", "g", 88, COR), ("coisas", "i", 84)], W / 2, 190, "center")
    for k, x, titulo in (("s03.b", 200, "probabilidade"), ("s03.c", 1000, "união no Venn")):
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, 290, 720, 620, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(titulo, "g", 64, COR)], x + 360, 400, "center")
    E.foco(c, t, C["s03.b"] + 0.4, 0.45, lambda a: E.escreve(c, "P =", 250, 640, 96, "g", TINTA, a))
    E.fr(c, t, C["s03.b"] + 0.7, "favoráveis", "possíveis", 640, 610, 66, COR)
    E.venn(c, t, C["s03.c"] + 0.3, 1360, 600, 95, ("A", "B"), pinta=[("A", C["s03.c"] + 1.0), ("B", C["s03.c"] + 1.0), ("AB", C["s03.c"] + 1.0)],
           universo=None, size=40)
    txe(c, t, C["s03.c"] + 1.4, "n(A ∪ B) =", 1360, 790, 54, "g", TINTA, "center")
    txe(c, t, C["s03.c"] + 2.0, "n(A) + n(B) − n(A ∩ B)", 1360, 870, 54, "g", COR, "center")
    E.frase(c, t, lerp(C["s03.c"], C["s03.end"], 0.8), ps("faltou alguma? procure no canal", "i", 52, TINTA2), W / 2, 1010, "center", passo=0.1)


# ---------------- baralho ----------------
CW, CX0, CY0, CDX, CDY = 96, 280, 380, 112, 152


def pos_carta(i, j):
    return CX0 + j * CDX, CY0 + i * CDY


def b_baralho(c, t, C, b):
    E.frase(c, t, C["s04.a"], [("52", "g", 96, COR), ("cartas", "i", 84)], W / 2, 150, "center")
    for i, nn in enumerate(NAIPES):
        for j, v in enumerate(VALORES):
            x, y = pos_carta(i, j)
            E.foco(c, t, C["s04.a"] + 0.25 * i + 0.03 * j, 0.35, lambda a, x=x, y=y, v=v, nn=nn: carta(c, x, y, CW, v, nn, a), sobe=8)
        x, y = pos_carta(i, 0)
        E.foco(c, t, C["s04.b"] + 0.5 * i, 0.4, lambda a, y=y, nn=nn: (naipe(c, 160, y - 22, 60, nn, a), centro(c, nn, 160, y + 48, 32, "b", TINTA2, a)))
    # 13 cartas por naipe
    if t >= C["s04.c"]:
        x0, _ = pos_carta(0, 0)
        x1, _ = pos_carta(0, 12)
        E.chave(c, x0 - CW / 2, x1 + CW / 2, CY0 - CDY / 2 - 14, E.COR, ep(t, C["s04.c"], 0.6), -24)
        nota(c, t, C["s04.c"] + 0.3, (x0 + x1) / 2, 245, "13 por naipe: do ás ao rei", 46, COR)
    # os 4 reis
    xk, _ = pos_carta(0, 12)
    if t >= C["s04.d"]:
        E.foco(c, t, C["s04.d"], 0.5, lambda a: bloco(c, xk - CW / 2, xk + CW / 2, CY0 + 1.5 * CDY, 3 * CDY + CW * 1.4, a, largura=6))
    E.foco(c, t, C["s04.d"] + 0.3, 0.45, lambda a: E.pilula(c, "4 reis", xk, CY0 + 3 * CDY + 150, 46, estilo="g", a=a))


# ---------------- Venn ----------------
VX, VY, VR = 600, 600, 230
XP = 1110  # coluna do texto


def b_venn(c, t, C, b):
    ts = {"A": C["s06.a"] + 0.3, "B": C["s06.b"] + 0.3, "AB": C["s05.d"] + 0.3}
    pinta = [("A", C["s05.a"]), ("B", C["s05.b"]), ("AB", C["s05.c"])] if t < C["s06.c"] else [("A", C["s06.c"]), ("B", C["s06.c"]), ("AB", C["s06.c"])]
    E.venn(c, t, C["s05"] + 0.3, VX, VY, VR, ("A", "B"), numeros={"A": 3, "AB": 1, "B": 12}, tn=ts, pinta=pinta, size=72,
           alfa=0.22 if t < C["s06.c"] else 0.32)
    E.foco(c, t, C["s05.d"] + 0.1, 0.45, lambda a: carta(c, VX, VY + VR * 0.36, 70, "K", "copas", a, E.COR))

    def contar():
        E.foco(c, t, C["s05.a"], 0.45, lambda a: (E.escreve(c, "A = reis:", XP, 300, 64, "i", TINTA, a), E.escreve(c, "4", XP + 300, 300, 72, "g", COR, a)))
        E.foco(c, t, C["s05.b"], 0.45, lambda a: (E.escreve(c, "B = copas:", XP, 420, 64, "i", TINTA, a), E.escreve(c, "13", XP + 320, 420, 72, "g", COR, a)))
        E.foco(c, t, C["s05.c"], 0.45, lambda a: E.escreve(c, "em ambos:", XP, 580, 64, "i", TINTA, a))
        E.foco(c, t, C["s05.d"], 0.45, lambda a: E.escreve(c, "rei de copas", XP, 680, 72, "g", COR, a))
        E.foco(c, t, C["s05.d"] + 0.8, 0.45, lambda a: E.escreve(c, "vai no meio", XP, 770, 54, "i", TINTA2, a))
    E.saida(c, t, C["s06"] - 0.1, contar)
    if C["s06"] <= t < C["s07"]:
        def pedacos():
            E.frase(c, t, C["s06"] + 0.1, ps("de dentro para fora", "i", 64, TINTA2), XP, 260, passo=0.1)
            E.foco(c, t, C["s06.a"], 0.45, lambda a: E.escreve(c, "só rei:", XP, 400, 60, "i", TINTA, a))
            E.formula_em(c, t, C["s06.a"] + 0.3, "4 − 1 = 3", XP + 230, 400, 72, "g", COR)
            E.foco(c, t, C["s06.b"], 0.45, lambda a: E.escreve(c, "só copas:", XP, 520, 60, "i", TINTA, a))
            E.formula_em(c, t, C["s06.b"] + 0.3, "13 − 1 = 12", XP + 280, 520, 72, "g", COR)
            E.formula_em(c, t, C["s06.c"], "3 + 1 + 12 = 16", XP, 700, 84, "g", TINTA)
            nota(c, t, C["s06.c"] + 0.8, XP + 300, 790, "cartas que servem", 50, TINTA2, "i")
        E.saida(c, t, C["s07"] - 0.1, pedacos)
    if t < C["s07"]:
        return
    nota(c, t, C["s07"] + 0.1, XP + 330, 260, "rei ou copas", 56, COR, "g")
    y = 480
    xs, xf = linha(c, t, XP - 20, y, 96, [("P =", C["s07.a"]), ((16, 52), C["s07.a"] + 0.2, COR)])
    E.pontes(c, t, xf + 15, xf + 185, y, 96, "÷ 4", C["s07.b"] - 0.6, C["s07.b"] - 0.3, size=38)
    E.fr(c, t, C["s07.b"], 4, 13, xf + 270, y, 96, COR)
    E.foco(c, t, C["s07.c"], 0.5, lambda a: E.escreve(c, "≈ 31%", XP, 790, 110, "g", CERTO, a))
    nota(c, t, C["s07.c"] + 1.0, XP + 330, 900, "pouco menos de 1/3", 50, TINTA2, "i")


# ---------------- fórmula ----------------
def b_formula(c, t, C, b):
    def formula():
        txe(c, t, C["s08.a"], "P(A): a chance do evento A", W / 2, 220, 60, "b", TINTA2, "center")
        y = 420
        partes = [("P(A ∪ B)", C["s08.b"], COR), ("=", C["s08.c"] - 0.2), ("P(A) + P(B)", C["s08.c"]), ("− P(A ∩ B)", C["s08.d"], ERRADO)]
        xs, xf = linha(c, t, W / 2, y, 100, partes, "center")
        nota(c, t, C["s08.b"] + 0.4, xs[0] + tw("P(A ∪ B)", "g", 100) / 2, y + 130, "A ou B", 48, COR)
        nota(c, t, C["s08.d"] + 0.4, xs[3] + tw("− P(A ∩ B)", "g", 100) / 2, y + 130, "ambos juntos", 48, ERRADO)
        if t >= C["s09"]:
            y2 = 740
            ys, yf = linha(c, t, W / 2, y2, 96, [((4, 52), C["s09.a"]), ("+", C["s09.b"] - 0.2), ((13, 52), C["s09.b"]), ("−", C["s09.c"] - 0.2),
                                                 ((1, 52), C["s09.c"], ERRADO), ("=", C["s09.d"] - 0.2), (("4 + 13 − 1", 52), C["s09.d"]),
                                                 ("=", C["s09.e"] - 0.2), ((16, 52), C["s09.e"], COR)], "center")
            nota(c, t, lerp(C["s09.c"], C["s09.d"], 0.35), W / 2, 960, "embaixo, sempre o total: 52", 48, TINTA2, "i")
    E.saida(c, t, C["s10"] - 0.1, formula)
    if t < C["s10"]:
        return
    E.frase(c, t, C["s10.a"], [("sem", "i", 76), ("parte", "i", 76), ("em", "i", 76), ("comum?", "g", 84, COR)], W / 2, 180, "center")

    def separados(a):
        c.drawRect(skia.Rect.MakeLTRB(160, 280, 1160, 840), M.paint(TINTA, a, stroke=4))
        for cx, nome in ((420, "reis"), (900, "damas")):
            c.drawCircle(cx, 600, 200, M.paint(E.COR, 0.18 * a))
            c.drawCircle(cx, 600, 200, M.paint(TINTA, a, stroke=6))
            centro(c, nome, cx, 370, 48, "g", COR, a)
    E.foco(c, t, C["s10.b"], 0.5, separados)
    E.foco(c, t, C["s10.b"] + 0.4, 0.45, lambda a: (carta(c, 420, 620, 110, "K", "ouros", a), carta(c, 900, 620, 110, "Q", "paus", a)))
    E.foco(c, t, C["s10.c"], 0.5, lambda a: E.pilula(c, "interseção vazia: nada para tirar", 660, 920, 46, estilo="g", fundo=TINTA2, a=a))
    E.formula_em(c, t, C["s10.d"], "4 + 4 = 8", 1250, 460, 96, "g", TINTA)
    xs, xf = linha(c, t, 1250, 700, 100, [("P =", C["s10.e"]), ((8, 52), C["s10.e"] + 0.2), ("=", C["s10.e"] + 1.0), ((2, 13), C["s10.e"] + 1.2, COR)])


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s11"] + 0.1, [("cuidado", "g", 90, ERRADO), ("com", "i", 84), ("isto", "i", 84)], W / 2, 160, "center")
    w, dx = 96, 112
    x0 = 300
    E.foco(c, t, C["s11.a"] - 0.4, 0.45, lambda a: E.escreve(c, "4 reis", 160, 330, 44, "b", TINTA2, a))
    for j, nn in enumerate(("paus", "ouros", "espadas", "copas")):
        E.foco(c, t, C["s11.a"] - 0.4 + 0.08 * j, 0.4, lambda a, j=j, nn=nn: carta(c, x0 + j * dx, 420, w, "K", nn, a))
    E.foco(c, t, C["s11.a"] - 0.2, 0.45, lambda a: E.escreve(c, "13 de copas", 160, 560, 44, "b", TINTA2, a))
    some = ep(t, C["s11.c"], 0.6)
    for j, v in enumerate(VALORES):
        ap = 1 - 0.75 * some if v == "K" else 1.0
        E.foco(c, t, C["s11.a"] - 0.2 + 0.04 * j, 0.4, lambda a, j=j, v=v, ap=ap: carta(c, x0 + j * dx, 650, w, v, "copas", a, apaga=ap))
    xk1, xk2 = x0 + 3 * dx, x0 + 12 * dx
    if t >= C["s11.b"]:
        p = ep(t, C["s11.b"], 0.4)
        for xx, yy in ((xk1, 420), (xk2, 650)):
            E.caixa_pontilhada(c, xx - 66, yy - 84, 132, 168, p, ERRADO, p)
        nota(c, t, C["s11.b"] + 0.3, xk2 - 250, 470, "contado 2 vezes", 50, ERRADO)
    if t >= C["s11.c"]:
        E.risco(c, xk2 - 50, 720, xk2 + 50, 580, t, C["s11.c"], largura=10)
    E.formula_em(c, t, C["s11.a"], "4 + 13 = 17", 300, 880, 90, "g", ERRADO)
    E.formula_em(c, t, C["s11.c"] + 0.3, "17 − 1 = 16", 900, 880, 90, "g", CERTO)
    E.foco(c, t, C["s11.d"], 0.5, lambda a: E.pilula(c, "“ou”: dá para acontecer junto?", W / 2, 1000, 48, estilo="g", a=a))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def quantidades():
        E.frase(c, t, C["s12.a"], [("conte", "i", 80, CLARO), ("cartas,", "g", 84, BR), ("divida", "i", 80, CLARO), ("no", "i", 80, CLARO), ("fim", "g", 84, BR)],
                W / 2, 210, "center", passo=0.12)
        E.formula_em(c, t, C["s12.a"] + 1.4, "4 + 13 − 1 = 16", 300, 500, 104, "g", BR)
        if t >= C["s12.a"] + 2.2:
            p = ep(t, C["s12.a"] + 2.2, 0.5)
            M.arrow(c, 1150, 465, 1330, 465, BR, p, 6, 22, p)
            E.foco(c, t, C["s12.a"] + 2.2, 0.45, lambda a: E.centro(c, "÷ 52", 1240, 420, 48, "b", CLARO, a))
        E.fr(c, t, C["s12.a"] + 2.6, 16, 52, 1460, 465, 110, BR)
        E.foco(c, t, C["s12.b"], 0.5, lambda a: E.pilula(c, "o resultado é o mesmo", W / 2, 720, 56, estilo="g", fundo=E.COR, a=a))
        E.frase(c, t, C["s12.c"], [("o", "i", 64, CLARO), ("mesmo", "i", 64, CLARO), ("total", "g", 70, BR), ("embaixo:", "i", 64, CLARO), ("52", "g", 70, BR)],
                W / 2, 880, "center", passo=0.1)
    E.saida(c, t, C["s13"] - 0.1, quantidades)
    if t < C["s13"]:
        return
    E.foco(c, t, C["s13.a"], 0.5, lambda a: E.pilula(c, "não compensa: a questão já dá em %", W / 2, 180, 50, estilo="g", fundo=ERRADO, a=a))
    for k, y, nome, v in (("s13.b", 360, "cartão", "60%"), ("s13.c", 480, "pix", "50%"), ("s13.d", 600, "ambos", "30%")):
        E.foco(c, t, C[k], 0.45, lambda a, y=y, nome=nome, v=v: (E.escreve(c, nome, 300, y, 70, "i", CLARO, a), E.escreve(c, v, 620, y, 80, "g", BR, a)))
    nota(c, t, lerp(C["s13.d"], C["s13.e"], 0.5), 1350, 480, "cartão ou pix?", 64, CLARO, "i")
    xs, xf = linha(c, t, 300, 830, 100, [("60% + 50% − 30%", C["s13.e"], BR)])
    igual_bola(c, t, C["s13.e"] + 0.8, xf + 60, 830, "80%", r=110, cor=E.COR, escuro=True)


# ---------------- questão ----------------
def urna(c, t, t0, x, y, passo=84, r=34, cor_de=None, anel_de=None):
    """as 30 bolinhas em 3 linhas de 10, a partir do centro da primeira (x, y)"""
    for n in range(1, 31):
        i, j = (n - 1) // 10, (n - 1) % 10
        cx, cy = x + j * passo, y + i * passo
        cor = cor_de(n) if cor_de else None
        anel = anel_de(n) if anel_de else None
        E.foco(c, t, t0 + 0.02 * n, 0.35, lambda a, cx=cx, cy=cy, n=n, cor=cor, anel=anel: bolinha(c, cx, cy, r, n, a, cor, anel), sobe=6)


def b_questao(c, t, C, b):
    E.frase(c, t, C["s14"] + 0.1, [("hora", "i", 72, COR), ("de", "i", 72, COR), ("testar", "i", 72, COR)], XE, 190)
    urna(c, t, C["s14.a"], XE + 40, 320, passo=84, r=36)
    E.frase(c, t, C["s14.a"] + 0.6, [("30", "g", 66, COR), ("bolinhas,", "i", 62), ("de", "i", 62), ("1", "g", 66), ("a", "i", 62), ("30", "g", 66)], XE, 650, passo=0.1)
    E.frase(c, t, C["s14.b"], [("chance", "i", 70), ("de", "i", 70), ("sair", "i", 70), ("um", "i", 70), ("múltiplo", "g", 76)], XE, 800, passo=0.12)
    E.frase(c, t, C["s14.b"] + 0.6, [("de", "i", 70), ("3", "g", 80, COR), ("ou", "i", 70), ("de", "i", 70), ("5?", "g", 80, COR)], XE, 900, passo=0.12)
    E.relogio(c, t, C["s15.a"], 1500, 560, 190)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    t3, t5, tab = C["s16.a"], C["s16.b"], C["s16.c"]
    cor_de = lambda n: (E.COR if (n % 3 == 0 and t >= t3 + 0.3) else None)
    anel_de = lambda n: (AMBAR if (n % 5 == 0 and t >= t5 + 0.3) else None)
    urna(c, t, C["s16"], 420, 200, passo=100, r=40, cor_de=cor_de, anel_de=anel_de)
    if t >= tab:
        for n in (15, 30):
            i, j = (n - 1) // 10, (n - 1) % 10
            E.caixa_pontilhada(c, 420 + j * 100 - 52, 200 + i * 100 - 52, 104, 104, ep(t, tab, 0.4), ERRADO, ep(t, tab, 0.4))

    def listas():
        E.foco(c, t, t3, 0.45, lambda a: (E.bola(c, 460, 560, 26, E.COR, a), E.escreve(c, "múltiplos de 3:", 510, 580, 60, "i", TINTA, a),
                                          E.escreve(c, "10", 940, 582, 72, "g", COR, a)))
        E.foco(c, t, t5, 0.45, lambda a: (c.drawCircle(460, 670, 26, M.paint(AMBAR, a, stroke=9)), E.escreve(c, "múltiplos de 5:", 510, 690, 60, "i", TINTA, a),
                                          E.escreve(c, "6", 940, 692, 72, "g", AMBAR, a)))
        E.foco(c, t, tab, 0.45, lambda a: (E.escreve(c, "nos dois:", 510, 800, 60, "i", TINTA, a), E.escreve(c, "15 e 30", 780, 802, 72, "g", ERRADO, a)))
        E.foco(c, t, C["s16.d"], 0.5, lambda a: E.pilula(c, "em ambas as listas", 1450, 780, 48, estilo="g", fundo=ERRADO, a=a))
    E.saida(c, t, C["s17"] - 0.1, listas)
    if t < C["s17"]:
        return
    E.formula_em(c, t, C["s17.a"], "10 + 6 = 16", 300, 600, 90, "g", TINTA)
    E.formula_em(c, t, C["s17.b"], "16 − 2 = 14", 300, 760, 90, "g", TINTA)
    nota(c, t, C["s17.b"] + 0.5, 520, 850, "tira o 15 e o 30", 46, ERRADO, "i")
    y = 680
    xs, xf = linha(c, t, 860, y, 110, [("P =", C["s17.c"]), ((14, 30), C["s17.c"] + 0.2, COR)])
    E.pontes(c, t, xf + 15, xf + 175, y, 110, "÷ 2", C["s17.d"] - 0.6, C["s17.d"] - 0.3, size=40)
    E.resultado(c, t, C["s17.d"], 7, 15, xf + 310, y, 90, 115, CERTO)
    nota(c, t, C["s17.d"] + 1.0, xf + 310, 880, "pouco menos da metade", 46, TINTA2, "i")


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s18"], [("resumindo", "i", 92, COR)], W / 2, 190, "center")
        E.venn(c, t, C["s18.a"] - 0.2, 520, 580, 170, ("A", "B"), pinta=[("A", C["s18.a"] + 0.4), ("B", C["s18.a"] + 0.4),
                                                                      ("AB", C["s18.b"])], size=56, alfa=0.3)
        E.frase(c, t, C["s18.a"], [("na", "i", 72), ("palavra", "i", 72), ("“ou”,", "g", 80, COR), ("some", "g", 80)], 1000, 470, passo=0.12)
        E.frase(c, t, C["s18.b"], [("e", "i", 72), ("tire", "g", 80, ERRADO), ("uma", "i", 72), ("vez", "i", 72)], 1000, 590, passo=0.12)
        E.frase(c, t, C["s18.b"] + 0.6, ps("a parte em comum", "i", 72), 1000, 700, passo=0.12)
        linha(c, t, W / 2, 940, 76, [("P(A ∪ B) = P(A) + P(B) − P(A ∩ B)", C["s18.b"] + 1.4, TINTA)], "center")
    E.saida(c, t, C["s19"] - 0.1, resumo)
    if t < C["s19"]:
        return
    E.frase(c, t, C["s19"] + 0.1, ps("próxima aula", "i", 84), XE, 300)
    E.frase(c, t, C["s19.a"], [("a", "i", 72), ("questão", "i", 72), ("dá", "i", 72), ("uma", "i", 72), ("pista", "g", 84, COR)], XE, 440, passo=0.12)

    def oculos(a):
        for cx in (XE + 90, XE + 250):
            c.drawCircle(cx, 640, 62, M.paint(E.COR, a, stroke=12))
        M.line(c, XE + 152, 630, XE + 188, 630, E.COR, a, 10)
    E.foco(c, t, C["s19.b"], 0.5, oculos)
    E.frase(c, t, C["s19.b"] + 0.3, [("sabendo", "i", 64), ("que", "i", 64), ("usa", "i", 64), ("óculos", "g", 70, COR)], XE + 380, 660, passo=0.1)
    E.foco(c, t, C["s19.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1560, 820, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s19.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1850, 1690, p), lerp(1040, 845, p), ep(t, C["s19.c"] + 0.2, 0.4))
    E.frase(c, t, C["s19.d"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 980, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, baralho=b_baralho, venn=b_venn, formula=b_formula, erro=b_erro, atalho=b_atalho,
              questao=b_questao, resposta=b_resposta, fim=b_fim)
