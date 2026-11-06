"""Visual editorial do Estudativo (curso novo): tipografia em movimento sobre papel claro, com UMA cor forte por matéria.

Conceito (referências em videos-referencias): muito espaço vazio, grotesca pesada misturada com serifada itálica, palavras
que entram desfocadas e ganham foco, formas geométricas enormes, caixa pontilhada com cursor. A identidade de cada matéria
vem de MATERIAS: a cor e a forma-símbolo. Trocar uma matéria é trocar uma linha aqui.

Uso em roteiro/visual.py:  import editorial as E;  E.usar("Matemática");  BACKGROUND = E.fundo;  OVERLAY = E.acabamento
"""
import json
import math
import re
from decimal import Decimal
from fractions import Fraction
from functools import lru_cache
from pathlib import Path

import skia

import motor as M
from motor import W, H, clamp, ep, prog, lerp, mix, ease_out, ease_io, ease_back, hexc

SERIFA = Path(__file__).parent / "fontes" / "instrument_serif"

PAPEL, PAPEL2, TINTA, TINTA2, CINZA, FIO = "#F3F3F0", "#DCDCD8", "#121214", "#3B3B40", "#8A8A90", "#D5D5D0"
CERTO, ERRADO = "#16A36A", "#E5484D"
VAZIO = "#FFFFFF"  # a parte vazia das barras: é superfície, não depende da matéria

# cor forte + forma-símbolo de cada matéria (a capa usa a cor em tela cheia, então cada uma é reconhecível de longe)
MATERIAS = {
    "Matemática": dict(cor="#2B14D9", forma="mais"),
    "Português": dict(cor="#E3212F", forma="aspas"),
    "Redação": dict(cor="#FFC400", forma="traco"),
    "Literatura": dict(cor="#8A1C4A", forma="livro"),
    "Inglês": dict(cor="#C6E800", forma="balao"),
    "Espanhol": dict(cor="#FFA8BC", forma="balao"),
    "Artes": dict(cor="#E0009C", forma="estrela"),
    "Física": dict(cor="#FF5A1F", forma="orbita"),
    "Química": dict(cor="#00B8A0", forma="hexagono"),
    "Biologia": dict(cor="#2FA84F", forma="folha"),
    "História": dict(cor="#B5742A", forma="arco"),
    "Geografia": dict(cor="#0A93E0", forma="relevo"),
    "Filosofia": dict(cor="#7B3FE4", forma="olho"),
    "Sociologia": dict(cor="#0B5D6B", forma="pessoas"),
}
COR = MATERIAS["Matemática"]["cor"]  # a cor da matéria: formas, faixas, capa
COR_TEXTO = COR  # a mesma cor, escurecida se preciso, para texto sobre o papel
SOBRE = "#FFFFFF"  # texto sobre a cor da matéria
CLARO = mix(COR, "#FFFFFF", 0.5)  # a cor legível sobre o palco escuro
FORMA = "mais"
ROTULO = ("Matemática", "")


def usar(materia, rotulo=""):
    """escolhe a matéria da aula (antes de desenhar). No visual.py, depois disto: COR = E.COR_TEXTO"""
    global COR, COR_TEXTO, SOBRE, CLARO, FORMA, ROTULO
    COR, FORMA, ROTULO = MATERIAS[materia]["cor"], MATERIAS[materia]["forma"], (materia, rotulo)
    COR_TEXTO = mix(COR, "#000000", 0.5) if M.lum(COR) > 0.55 else COR  # amarelo, lima e rosa somem sobre o papel
    SOBRE = M.on(COR)
    CLARO = mix(COR, "#FFFFFF", 0.5)


@lru_cache(None)
def _serifa(nome):
    return skia.Typeface.MakeFromFile(str(SERIFA / f"InstrumentSerif-{nome}.ttf"))


@lru_cache(None)
def fonte(estilo, size):
    """g = grotesca pesada · m = grotesca média · i = serifada itálica · s = serifada romana"""
    tf = {"g": lambda: M.typeface("black"), "b": lambda: M.typeface("bold"), "m": lambda: M.typeface("medium"),
          "i": lambda: _serifa("Italic"), "s": lambda: _serifa("Regular")}[estilo]()
    f = skia.Font(tf, size)
    f.setSubpixel(True)
    f.setEdging(skia.Font.Edging.kAntiAlias)
    return f


APERTO = dict(g=-0.035, b=-0.03, m=-0.015, i=-0.012, s=-0.012)  # letras justas, como nas referências


def larg(s, estilo, size):
    f = fonte(estilo, size)
    return f.measureText(s) + APERTO[estilo] * size * max(0, len(s) - 1)


def escreve(c, s, x, y, size, estilo="g", cor=None, a=1.0):
    """escreve com o aperto de letras do estilo; x = início, y = linha de base"""
    if a <= 0:
        return
    f, p, ap = fonte(estilo, size), M.paint(cor or TINTA, a), APERTO[estilo] * size
    for ch, adv in zip(s, f.getWidths(f.textToGlyphs(s))):
        c.drawString(ch, x, y, f, p)
        x += adv + ap


def foco(c, t, t0, d, fn, sobe=18, blur=16):
    """entrada da referência: desfocado e transparente até ficar nítido. fn(a) desenha."""
    p = prog(t, t0, d)
    if p <= 0:
        return
    e = ease_out(p)
    if e >= 0.995:
        fn(1.0)
        return
    tinta = skia.Paint()
    b = blur * (1 - e)
    if b > 0.25:
        tinta.setImageFilter(skia.ImageFilters.Blur(b, b))
    tinta.setAlphaf(clamp(e * 1.4))
    c.saveLayer(None, tinta)
    c.translate(0, sobe * (1 - e))
    fn(1.0)
    c.restore()


def _arranjo(partes, x, align):
    """largura de uma linha de tipografia mista e o x de cada parte"""
    esp = lambda p: p[2] * (0.24 if p[1] in "is" else 0.26)
    w = sum(larg(p[0], p[1], p[2]) for p in partes) + sum(esp(p) for p in partes[:-1])
    xx = x - w / 2 if align == "center" else x - w if align == "right" else x
    xs = []
    for p in partes:
        xs.append(xx)
        xx += larg(p[0], p[1], p[2]) + esp(p)
    return w, xs


def frase(c, t, t0, partes, x, y, align="left", passo=0.2, dur=0.5):
    """linha de tipografia mista, palavra a palavra. partes = [(texto, estilo, tamanho[, cor]), ...]"""
    w, xs = _arranjo(partes, x, align)
    for i, (p, xx) in enumerate(zip(partes, xs)):
        ti, s, est, size = t0 + i * passo, p[0], p[1], p[2]
        cor = p[3] if len(p) > 3 else TINTA
        foco(c, t, ti, dur, lambda a, s=s, est=est, size=size, cor=cor, xx=xx: escreve(c, s, xx, y, size, est, cor, a))
    return w


def saida(c, t, t1, fn, d=0.4):
    """desenha fn e some com desfoque a partir de t1"""
    if t < t1:
        fn()
        return
    p = prog(t, t1, d)
    if p >= 1:
        return
    pt = skia.Paint()
    pt.setImageFilter(skia.ImageFilters.Blur(14 * p, 14 * p))
    pt.setAlphaf(1 - ease_io(p))
    c.saveLayer(None, pt)
    fn()
    c.restore()


# ---------------- formas ----------------
def bola(c, cx, cy, r, cor=None, a=1.0):
    """esfera com volume e sombra longa (referência 5)"""
    cor = cor or COR
    if a <= 0 or r <= 0:
        return
    s = skia.Paint(AntiAlias=True, Color=hexc("#000000", 0.28 * a))
    s.setMaskFilter(skia.MaskFilter.MakeBlur(skia.kNormal_BlurStyle, max(2, r * 0.13)))
    c.drawCircle(cx + r * 0.1, cy + r * 0.16, r * 0.98, s)
    p = skia.Paint(AntiAlias=True)
    p.setShader(skia.GradientShader.MakeRadial(
        skia.Point(cx - r * 0.3, cy - r * 0.36), r * 1.5,
        [hexc(mix(cor, "#FFFFFF", 0.3), a), hexc(cor, a), hexc(mix(cor, "#000000", 0.32), a)], [0.0, 0.55, 1.0]))
    c.drawCircle(cx, cy, r, p)


def mais(c, cx, cy, r, cor=None, a=1.0, giro=0.0, sombra=True):
    """o símbolo da Matemática: um + largo, com volume"""
    cor = cor or COR
    if a <= 0:
        return
    b = r * 0.36
    path = skia.Path()
    path.addRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(-r, -b, 2 * r, 2 * b), b * 0.3, b * 0.3))
    path.addRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(-b, -r, 2 * b, 2 * r), b * 0.3, b * 0.3))
    path.setFillType(skia.PathFillType.kWinding)
    c.save(); c.translate(cx, cy); c.rotate(giro)
    if sombra:
        s = skia.Paint(AntiAlias=True, Color=hexc("#000000", 0.22 * a))
        s.setMaskFilter(skia.MaskFilter.MakeBlur(skia.kNormal_BlurStyle, r * 0.1))
        c.save(); c.translate(r * 0.08, r * 0.13); c.drawPath(path, s); c.restore()
    p = skia.Paint(AntiAlias=True)
    p.setShader(skia.GradientShader.MakeLinear(
        [skia.Point(-r, -r), skia.Point(r, r)], [hexc(mix(cor, "#FFFFFF", 0.22), a), hexc(mix(cor, "#000000", 0.25), a)]))
    c.drawPath(path, p)
    c.restore()


def simbolo(c, cx, cy, r, a=1.0, giro=0.0):
    """forma-símbolo da matéria atual (por enquanto desenhada só a da Matemática; as outras saem como esfera)"""
    mais(c, cx, cy, r, a=a, giro=giro) if FORMA == "mais" else bola(c, cx, cy, r, a=a)


def arco(c, cx, cy, r, ini, varre, cor, largura, a=1.0):
    p = M.paint(cor, a, stroke=largura)
    c.drawArc(skia.Rect.MakeXYWH(cx - r, cy - r, 2 * r, 2 * r), ini, varre, False, p)


def caixa_pontilhada(c, x, y, w, h, a=1.0, cor=None, prog_=1.0):
    """caixa de seleção com pontos nos cantos (referências 1 e 2)"""
    if a <= 0:
        return
    cor = cor or TINTA
    p = M.paint(cor, a, stroke=2)
    p.setPathEffect(skia.DashPathEffect.Make([7, 6], 0))
    path = skia.Path(); path.addRect(skia.Rect.MakeXYWH(x, y, w * prog_, h))
    c.drawPath(path, p)
    if prog_ >= 0.98:
        for px, py in ((x, y), (x + w, y), (x, y + h), (x + w, y + h)):
            c.drawCircle(px, py, 5.5, M.paint(cor, a))


def cursor(c, x, y, a=1.0, cor=None, escala=1.0):
    """seta de mouse grande (referência 1)"""
    if a <= 0:
        return
    p = skia.Path()
    p.moveTo(0, 0); p.lineTo(13, 46); p.lineTo(22, 27); p.lineTo(46, 19); p.close()
    c.save(); c.translate(x, y); c.scale(escala * 1.3, escala * 1.3)
    s = skia.Paint(AntiAlias=True, Color=hexc("#000000", 0.28 * a))
    s.setMaskFilter(skia.MaskFilter.MakeBlur(skia.kNormal_BlurStyle, 4))
    c.save(); c.translate(3, 5); c.drawPath(p, s); c.restore()
    c.drawPath(p, M.paint(cor or COR, a))
    c.restore()


def pilula(c, s, cx, cy, size, estilo="i", fundo=None, cor="#FFFFFF", a=1.0, contorno=False):
    """rótulo arredondado (referência 1: GAANE WALA)"""
    if a <= 0:
        return
    w, h = larg(s, estilo, size) + size * 1.1, size * 1.6
    r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2, cy - h / 2, w, h), h / 2, h / 2)
    if contorno:
        c.drawRRect(r, M.paint(cor, a, stroke=3))
    else:
        c.drawRRect(r, M.paint(fundo or COR, a))
    escreve(c, s, cx - larg(s, estilo, size) / 2, cy + size * 0.33, size, estilo, cor, a)


def fracao(c, n, d, cx, cy, size, cor=None, a=1.0, estilo="g", barra=None):
    """fração empilhada, centrada em (cx, cy)"""
    if a <= 0:
        return
    cor = cor or TINTA
    n, d = str(n), str(d)
    lw = max(larg(n, estilo, size), larg(d, estilo, size)) + size * 0.2
    escreve(c, n, cx - larg(n, estilo, size) / 2, cy - size * 0.2, size, estilo, cor, a)
    escreve(c, d, cx - larg(d, estilo, size) / 2, cy + size * 0.9, size, estilo, cor, a)
    b = size * 0.085
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - lw / 2, cy - b / 2 + size * 0.03, lw, b), b / 2, b / 2),
                M.paint(barra or cor, a))
    return lw


def _casco(c, x, y, w, h, canto, a, escuro=False):
    """sombra e fundo de uma barra (no palco, só um véu claro); devolve o contorno"""
    rr = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), canto, canto)
    if not escuro:
        sombra = skia.Paint(AntiAlias=True, Color=hexc("#000000", 0.14 * a))
        sombra.setMaskFilter(skia.MaskFilter.MakeBlur(skia.kNormal_BlurStyle, 16))
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x + 4, y + 12, w, h), canto, canto), sombra)
    c.drawRRect(rr, M.paint(VAZIO, a * (0.07 if escuro else 1)))
    return rr


def barra_fatias(c, x, y, w, h, partes, pintadas, cor, a=1.0, cortes=1.0, enche=1.0, canto=14):
    """barra dividida em `partes` iguais com `pintadas` preenchidas (a escala é a mesma para qualquer divisão)"""
    if a <= 0:
        return
    rr = _casco(c, x, y, w, h, canto, a)
    c.save(); c.clipRRect(rr, True)
    c.drawRect(skia.Rect.MakeXYWH(x, y, w * pintadas / partes * enche, h), M.paint(cor, a))
    for i in range(1, partes):
        lx = x + w * i / partes
        M.line(c, lx, y, lx, y + h * clamp(cortes), "#FFFFFF" if i <= pintadas else FIO, a, 4)
    c.restore()
    c.drawRRect(rr, M.paint(TINTA, a, stroke=3))


def risco(c, x0, y0, x1, y1, t, t0, cor=ERRADO, largura=12, d=0.35):
    M.line(c, x0, y0, x1, y1, cor, 1.0, largura, progress=ease_out(prog(t, t0, d)))


# ---------------- fundo e acabamento ----------------
@lru_cache(None)
def _papel():
    """papel com quadriculado fino e vinheta (sempre igual: pintar uma vez só deixa o render bem mais rápido)"""
    s = skia.Surface(W, H); c = s.getCanvas()
    c.clear(hexc(PAPEL))
    p = skia.Paint(AntiAlias=True)
    p.setShader(skia.GradientShader.MakeRadial(
        skia.Point(W / 2, H / 2), W * 0.72, [hexc("#FBFBF9"), hexc(PAPEL), hexc(PAPEL2)], [0.0, 0.5, 1.0]))
    c.drawRect(skia.Rect.MakeWH(W, H), p)
    g = M.paint("#000000", 0.035, stroke=1)
    for x in range(0, W + 1, 64):
        c.drawLine(x, 0, x, H, g)
    for y in range(0, H + 1, 64):
        c.drawLine(0, y, W, y, g)
    return s.makeImageSnapshot()


def fundo(c, t):
    c.drawImage(_papel(), 0, 0)
    gira = t * 2.2  # o arco grosso cinza das referências 2 e 3, à deriva
    arco(c, W * 0.86, H * 1.02, 760, 186 + gira, 120, "#000000", 92, 0.04)
    arco(c, W * 0.1, -80, 620, 8 - gira * 0.7, 110, "#000000", 72, 0.03)


def acabamento(c, t):
    """textinhos verticais nas margens (referência 1)"""
    mat, rot = ROTULO
    for i, (s, x) in enumerate((("ESTUDATIVO", 48), (f"{mat.upper()}  ·  {rot.upper()}" if rot else mat.upper(), W - 48))):
        c.save(); c.translate(x, H / 2); c.rotate(-90)
        f = fonte("m", 15)
        c.drawString(s, -f.measureText(s) / 2, 5, f, M.paint(TINTA, 0.5))
        c.restore()


def cortina(c, t, t0, cor=None, d=0.7):
    """transição: painel da cor da matéria varre a tela (referência 5). Cobre tudo no meio do tempo d."""
    p = prog(t, t0 - d / 2, d)
    if p <= 0 or p >= 1:
        return
    e = ease_io(p)
    x0 = W * clamp((e - 0.5) * 2)
    x1 = W * clamp(e * 2)
    c.drawRect(skia.Rect.MakeLTRB(x0, 0, x1, H), M.paint(cor or COR))


# ---------------- kit de aula: peças prontas para o visual.py ----------------
XE = 170  # margem esquerda


def carregar_cortinas(visual_py, blocos):
    """instantes de início dos blocos que abrem com cortina. visual_py = __file__ do visual.py"""
    tempos = json.loads((Path(visual_py).resolve().parents[1] / "audio" / "tempos.json").read_text(encoding="utf-8"))
    inicio = {}
    for s in tempos["scenes"]:
        inicio.setdefault(s["block"], s["start"])
    return [inicio[b] for b in blocos]


def fr(c, t, t0, n, d, cx, cy, size, cor=None, estilo="g"):
    """fração que entra com foco no instante t0"""
    foco(c, t, t0, 0.5, lambda a: fracao(c, n, d, cx, cy, size, cor, a, estilo))


def sinal(c, t, t0, s, cx, cy, size, cor=None, estilo="g"):
    """sinal (+, −, =) ou palavra curta centrada, com entrada de foco"""
    w = larg(s, estilo, size)
    foco(c, t, t0, 0.45, lambda a: escreve(c, s, cx - w / 2, cy + size * 0.36, size, estilo, cor or TINTA, a))


def resultado(c, t, t0, n, d, cx, cy, size, r, cor=None):
    """fração dentro da esfera: a resposta"""
    tinta = SOBRE if cor is None else M.on(cor)
    foco(c, t, t0, 0.5, lambda a: (bola(c, cx, cy + 3, r, cor, a), fracao(c, n, d, cx, cy, size, tinta, a)))


def passo(c, t, t0, n, l1, l2, y):
    """linha de um método: número na esfera, itálico curto e texto pesado"""
    foco(c, t, t0, 0.5, lambda a: (bola(c, XE + 42, y, 42, a=a),
                                   escreve(c, str(n), XE + 42 - larg(str(n), "g", 50) / 2, y + 18, 50, "g", SOBRE, a)))
    frase(c, t, t0 + 0.1, [(l1, "i", 64)], XE + 108, y - 8)
    frase(c, t, t0 + 0.3, [(l2, "g", 48)], XE + 108, y + 46)


def corrida(c, t, y, n1, d1, sg, n2, d2, t0, tm, mmc, a1, a2, b1, b2, n3, n4, d3, r, dr, tp, tr, s=116):
    """conta corrida numa linha: a/b ∓ c/d → (MMC) → e/m ∓ f/m = r/m.
    a1/b1 = (conta, instante, conta 2) sob cada fração nova; a2/b2 não usados (None); tp = instantes dos numeradores"""
    ct = COR_TEXTO
    fr(c, t, t0, n1, d1, 270, y, s, ct)
    sinal(c, t, t0 + 0.25, sg, 395, y - 15, 80)
    fr(c, t, t0 + 0.4, n2, d2, 520, y, s)
    if t >= tm:
        p = ep(t, tm, 0.5)
        M.arrow(c, 640, y, 740, y, TINTA, p, 4, 14, p)
        foco(c, t, tm, 0.5, lambda a: pilula(c, f"MMC = {mmc}", 690, y - 110, 40, estilo="b", cor=SOBRE, a=a))
    for x, n, cor, tq, ct_ in ((880, n3, ct, tp[0], a1), (1195, n4, TINTA, tp[1], b1)):
        if t >= tm:
            foco(c, t, tm + 0.1, 0.5, lambda q: fracao(c, n if t >= tq else "?", d3, x, y, s, cor if t >= tq else CINZA, q))
        foco(c, t, ct_[1], 0.4, lambda q: (escreve(c, ct_[0], x - larg(ct_[0], "m", 40) / 2, y + 190, 40, "m", TINTA2, q),
                                           escreve(c, ct_[2], x - larg(ct_[2], "b", 42) / 2, y + 244, 42, "b", COR_TEXTO, q)))
    if t >= tm:
        sinal(c, t, tm + 0.1, sg, 1038, y - 15, 80)
    sinal(c, t, tr - 0.2, "=", 1345, y - 15, 80)
    resultado(c, t, tr, r, dr, 1540, y, s * 0.92, 136)


def centro(c, s, cx, y, size, estilo="g", cor=None, a=1.0):
    """texto centrado em cx; y = linha de base"""
    escreve(c, s, cx - larg(s, estilo, size) / 2, y, size, estilo, cor, a)


def linha(c, t, partes, x, y, align="left"):
    """como frase, mas cada parte entra no seu instante: partes = [(texto, estilo, tamanho, cor, t0), ...]; devolve o x de cada uma"""
    _, xs = _arranjo(partes, x, align)
    for (s, est, size, cor, ti), xx in zip(partes, xs):
        foco(c, t, ti, 0.5, lambda a, s=s, est=est, size=size, cor=cor, xx=xx: escreve(c, s, xx, y, size, est, cor, a))
    return xs


def tablete(c, x, y, w, h, cor, a=1.0, k=1.0):
    """um pedaço de chocolate pintado, com o relevo da barra; k = escala"""
    if a <= 0 or k <= 0:
        return
    m, i = max(3, w * 0.03), min(w, h) * 0.14
    cx, cy = x + w / 2, y + h / 2
    c.save(); c.translate(cx, cy); c.scale(k, k); c.translate(-cx, -cy)
    p = skia.Paint(AntiAlias=True)
    p.setShader(skia.GradientShader.MakeLinear(
        [skia.Point(x, y), skia.Point(x + w, y + h)], [hexc(mix(cor, "#FFFFFF", 0.16), a), hexc(mix(cor, "#000000", 0.14), a)]))
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x + m, y + m, w - 2 * m, h - 2 * m), 10, 10), p)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x + i, y + i, w - 2 * i, h - 2 * i), 7, 7), M.paint(SOBRE, 0.2 * a, stroke=3))
    c.restore()


def chocolate(c, x, y, w, h, n, pedacos=(), a=1.0, cortes=1.0, escuro=False):
    """barra de pedaços que se contam: n iguais, cortes = 0..1 desce um a um, pedacos = [(i, cor, p 0..1[, dy])], escuro = sobre o palco"""
    if a <= 0:
        return
    rr = _casco(c, x, y, w, h, 16, a, escuro)
    lp = w / n
    for i in range(1, n):
        q = clamp(cortes * (n - 1) - (i - 1))
        if q > 0:
            M.line(c, x + lp * i, y + 2, x + lp * i, y + 2 + (h - 4) * ease_io(q), CLARO if escuro else FIO, a * (0.6 if escuro else 1), 4)
    c.drawRRect(rr, M.paint(CLARO if escuro else TINTA, a, stroke=3))
    for ped in pedacos:
        i, cor, p = ped[:3]
        dy = ped[3] if len(ped) > 3 else 0
        if p > 0:
            tablete(c, x + lp * i, y + dy, lp, h, cor, a * clamp(p * 1.6), lerp(0.55, 1.0, ease_back(p)))


def barra(c, x, y, w, h, pintado, cortes, a=1.0, cor=None, enche=1.0, largura=5):
    """barra de área contínua: a fração `pintado` fica fixa e os cortes = [(posição 0..1, p 0..1)] descem como lâmina e podem voltar"""
    if a <= 0:
        return
    cor = cor or COR
    rr = _casco(c, x, y, w, h, 14, a)
    c.save(); c.clipRRect(rr, True)
    c.drawRect(skia.Rect.MakeXYWH(x, y, w * pintado * enche, h), M.paint(cor, a))
    for pos, p in cortes:
        if p > 0:
            lx = x + w * pos
            M.line(c, lx, y, lx, y + h * p, M.on(cor) if pos <= pintado * enche + 1e-6 else TINTA2, a, largura, cap_round=False)
    c.restore()
    c.drawRRect(rr, M.paint(TINTA, a, stroke=3))
    for pos, p in cortes:
        if 0 < p < 1:
            c.drawCircle(x + w * pos, y + h * p, 11, M.paint(TINTA, a))


def chave(c, x0, x1, y, cor=TINTA2, p=1.0, h=22, largura=5, abre=True):
    """colchete que marca um trecho de barra: nasce em y e fecha em y + h (h < 0 = acima); p = 0..1 abre do meio, ou só surge se abre=False"""
    if p <= 0:
        return
    if not abre:  # três traços de ponta redonda, não o path de quina viva
        for x0_, y0_, x1_, y1_ in ((x0, y + h, x1, y + h), (x0, y + h, x0, y), (x1, y + h, x1, y)):
            M.line(c, x0_, y0_, x1_, y1_, cor, p, largura)
        return
    m = (x0 + x1) / 2
    a, b = lerp(m, x0, p), lerp(m, x1, p)
    path = skia.Path()
    path.moveTo(a, y); path.lineTo(a, y + h); path.lineTo(b, y + h); path.lineTo(b, y)
    c.drawPath(path, M.paint(cor, min(1.0, p * 2), stroke=largura, cap_round=True))


def ponte(c, t, t0, x0, x1, y, rotulo, cor=None, size=54):
    """seta de uma fração para a outra, com a operação numa pílula em cima da seta"""
    if t < t0:
        return
    p = ep(t, t0, 0.5)
    M.arrow(c, x0, y, x1, y, cor or COR_TEXTO, p, 5, 18, p)
    tinta = SOBRE if cor is None else M.on(cor)
    foco(c, t, t0, 0.4, lambda a: pilula(c, rotulo, (x0 + x1) / 2, y, size, estilo="g", fundo=cor or COR, cor=tinta, a=a), sobe=6)


def pontes(c, t, x0, x1, cy, s, rot, tc, tb, cor=None, size=54):
    """a mesma operação no de cima (em tc) e no de baixo (em tb) de uma fração de tamanho s"""
    ponte(c, t, tc, x0, x1, cy - s * 0.565, rot, cor, size)
    ponte(c, t, tb, x0, x1, cy + s * 0.535, rot, cor, size)


def frac_q(c, t, t0, n, d, tn, td, cx, cy, s, cor=None):
    """fração que chega com ? e ganha os números na fala (tn = de cima, td = de baixo)"""
    pronto = t >= tn and t >= td
    foco(c, t, t0, 0.5, lambda a: fracao(c, n if t >= tn else "?", d if t >= td else "?", cx, cy, s,
                                         (cor or COR_TEXTO) if pronto else CINZA, a))


# tabela de fatoração simultânea: montar faz as divisões de verdade, então tabela, contas ao lado e fala não têm como divergir
TAB_GRANDE = dict(xs=(300, 500, 700), xb=825, xp=925, y0=225, dy=125, s=96)
TAB_PEQUENA = dict(xs=(250, 395, 540), xb=640, xp=715, y0=325, dy=104, s=78)


def montar(nums, primos):
    """faz a fatoração de verdade: devolve as linhas da tabela e, para cada célula, se o número só desceu repetido"""
    linhas, desceu = [tuple(nums)], [(False,) * len(nums)]
    for p in primos:
        ant = linhas[-1]
        assert any(n % p == 0 for n in ant), (ant, p)
        linhas.append(tuple(n // p if n % p == 0 else n for n in ant))
        desceu.append(tuple(n % p != 0 for n in ant))
    assert all(n == 1 for n in linhas[-1])
    return dict(primos=tuple(primos), linhas=linhas, desceu=desceu)


def tabela(c, t, T, tn, tp, tb, g=TAB_GRANDE, cor_fim=None, cor_primo=None):
    """a fatoração à vista; tn = instante de cada número por linha, tp = de cada primo, tb = do traço em cada linha"""
    xs, xb, xp, y0, dy, s = g["xs"], g["xb"], g["xp"], g["y0"], g["dy"], g["s"]
    # o traço cresce linha a linha
    alto = y0 - s * 0.8
    baixo = y0 + s * 0.2
    for i, ti in enumerate(tb):
        baixo = max(baixo, lerp(y0 + (i - 1) * dy + s * 0.2, y0 + i * dy + s * 0.2, ease_io(prog(t, ti, 0.4)))) if t >= ti else baixo
    if t >= tb[0]:
        c.drawRect(skia.Rect.MakeXYWH(xb - 3, alto, 6, (baixo - alto) * ep(t, tb[0], 0.4)), M.paint(TINTA))
    for i, lin in enumerate(T["linhas"]):
        y = y0 + i * dy
        for j, v in enumerate(lin):
            desce, ti = T["desceu"][i][j], tn[i][j]
            cor = CINZA if desce else TINTA
            if cor_fim and i == len(T["linhas"]) - 1:
                cor = cor_fim
            if desce:  # o número escorrega da linha de cima, repetido
                if t >= ti:
                    q = ease_io(prog(t, ti, 0.45))
                    centro(c, str(v), xs[j], lerp(y - dy, y, q), s, "g", cor, min(1.0, q * 2.5))
            else:
                foco(c, t, ti, 0.45, lambda a, v=v, j=j, y=y, cor=cor: centro(c, str(v), xs[j], y, s, "g", cor, a))
    for i, p in enumerate(T["primos"]):
        cor = (cor_primo or {}).get(i, COR_TEXTO)
        foco(c, t, tp[i], 0.45, lambda a, i=i, p=p, cor=cor: centro(c, str(p), xp, y0 + i * dy, s, "g", cor, a))


def seta_primo(c, t, ini, fim, i, g=TAB_GRANDE):
    """caixa pontilhada na casa do primo da vez"""
    if ini <= t < fim:
        q = ep(t, ini, 0.3) * (1 - ep(t, fim - 0.25, 0.25))
        s, y = g["s"], g["y0"] + i * g["dy"]
        caixa_pontilhada(c, g["xp"] - s * 0.62, y - s * 0.92, s * 1.24, s * 1.18, q, prog_=q)


def passos(c, t, T, ti, tp, tn, tf):
    """painel à direita com a conta de cada número; ti = início de cada passo, tp e tn como em tabela, tf = fim do último"""
    for i, p in enumerate(T["primos"]):
        t1 = ti[i + 1] - 0.1 if i + 1 < len(ti) else tf
        if not ti[i] <= t < t1 + 0.4:
            continue

        def painel(i=i, p=p):
            foco(c, t, tp[i], 0.45, lambda a: pilula(c, f"÷ {p}", 1250, 245, 72, estilo="g", fundo=COR, cor=SOBRE, a=a))
            for j, n in enumerate(T["linhas"][i]):
                cai = n % p != 0
                s = f"{n} desce" if cai else f"{n} ÷ {p} = {n // p}"
                foco(c, t, tn[i + 1][j], 0.4, lambda a, s=s, j=j, cai=cai: escreve(c, s, 1150, 420 + j * 90, 64, "m" if cai else "b", CINZA if cai else TINTA, a))
        saida(c, t, t1, painel)


def produto(c, t, T, ts, x0, y, g=TAB_GRANDE, s=84, passo_x=125):
    """os primos saem da coluna e voam até formar a multiplicação"""
    for i, p in enumerate(T["primos"]):
        xf = x0 + i * passo_x
        if i and t >= ts[i] - 0.1:
            centro(c, "×", xf - passo_x / 2, y, 58, "b", TINTA2, ep(t, ts[i] - 0.1, 0.3))
        if t >= ts[i] - 0.25:
            q = ease_io(prog(t, ts[i] - 0.25, 0.55))
            centro(c, str(p), lerp(g["xp"], xf, q), lerp(g["y0"] + i * g["dy"], y, q), round(lerp(g["s"], s, q)), "g", COR_TEXTO)


def palco(c, t):
    """palco escuro com brilho da cor da matéria (referência 1): atalhos, macetes e momentos especiais"""
    c.drawRect(skia.Rect.MakeWH(W, H), M.paint("#07070F"))
    for cx, cy, r, f in ((280 + 40 * math.sin(t * 0.5), 180, 720, 0.75), (1650, 960 + 30 * math.cos(t * 0.4), 820, 0.6)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [hexc(COR, f), hexc(COR, 0.0)], [0.0, 1.0]))
        c.drawCircle(cx, cy, r, p)
    arco(c, 1500, -200, 520, 30, 130, CLARO, 3, 0.25)


# ---------------- questão e conferência ----------------
def relogio(c, t, t0, cx=1490, cy=440, r=210, escuro=False):
    """relógio de pausa: enche em 3 segundos, com "pause o vídeo" embaixo"""
    k = r * ease_back(prog(t, t0, 0.6))
    if k <= 0:
        return
    bola(c, cx, cy, k)
    tinta = "#FFFFFF" if escuro else TINTA
    f = clamp(prog(t, t0 + 0.8, 3.0))
    if f > 0:
        arco(c, cx, cy, k + 34, -90, 360 * f, tinta, 10)
    for dx in (-44, 44):
        M.rrect(c, cx + dx * r / 210 - 22 * r / 210, cy - 80 * r / 210, 44 * r / 210, 160 * r / 210, 12, SOBRE, ep(t, t0 + 0.2, 0.4))
    foco(c, t, t0 + 0.2, 0.5, lambda a: centro(c, "pause o vídeo", cx, cy + k + 120, 64, "i", tinta, a))


def selo(c, cx, cy, r, ok, a=1.0):
    """sim ou não numa esfera verde ou vermelha"""
    if a <= 0 or r <= 1:
        return
    bola(c, cx, cy, r, CERTO if ok else ERRADO, a)
    k, w = r * 0.42, max(5, r * 0.16)
    if ok:
        M.line(c, cx - k, cy + k * 0.05, cx - k * 0.2, cy + k * 0.8, "#FFFFFF", a, w)
        M.line(c, cx - k * 0.2, cy + k * 0.8, cx + k, cy - k * 0.7, "#FFFFFF", a, w)
    else:
        M.line(c, cx - k * 0.8, cy - k * 0.8, cx + k * 0.8, cy + k * 0.8, "#FFFFFF", a, w)
        M.line(c, cx + k * 0.8, cy - k * 0.8, cx - k * 0.8, cy + k * 0.8, "#FFFFFF", a, w)


def corta(c, t, t0, cx, cy, size, novo=None, cor=None, cor_novo=None, tn=None, tf=None):
    """risca um número centrado em (cx, cy) e escreve o valor novo em cima, à direita: é o corte em cruz e o empréstimo.
    tf = instante em que esse valor novo some, porque a casa vai mudar de novo (0 → 10 → 9)"""
    k = size * 0.48
    risco(c, cx - k, cy + k, cx + k, cy - k, t, t0, cor or ERRADO, max(6, size * 0.08))
    if novo is not None:
        s = size * 0.56
        if tf is not None and t >= tf:
            return
        foco(c, t, tn if tn is not None else t0 + 0.3, 0.4,
             lambda a: escreve(c, str(novo), cx + size * 0.3, cy - size * 0.5, s, "g", cor_novo or COR_TEXTO, a), sobe=8)


def grade(c, x, y, w, h, cols, lins, pc=0, pl=0, a=1.0, ec=1.0, el=1.0):
    """multiplicar frações por área: pinta pc colunas (ec = 0..1) e marca pl linhas por cima (el = 0..1); o cruzamento fica forte"""
    if a <= 0:
        return
    rr = _casco(c, x, y, w, h, 14, a)
    c.save(); c.clipRRect(rr, True)
    lc, ll = w / cols, h / lins
    if pc and ec > 0:
        c.drawRect(skia.Rect.MakeXYWH(x, y, lc * pc, h * ec), M.paint(CLARO, a))
    if pl and el > 0:
        c.drawRect(skia.Rect.MakeXYWH(x, y, w * el, ll * pl), M.paint(TINTA, 0.14 * a))
        c.drawRect(skia.Rect.MakeXYWH(x, y, min(w * el, lc * pc), min(h * ec, ll * pl)), M.paint(COR, a))
    for i in range(1, cols):
        M.line(c, x + lc * i, y, x + lc * i, y + h, FIO, a, 3)
    for j in range(1, lins):
        M.line(c, x, y + ll * j, x + w, y + ll * j, FIO, a, 3)
    c.restore()
    c.drawRRect(rr, M.paint(TINTA, a, stroke=3))


# ---------------- decimais: cada algarismo na sua casa, com a vírgula sempre no mesmo lugar ----------------
def casa(size):
    """largura de uma casa de algarismo: sobra espaço para a vírgula entre duas casas"""
    return larg("0", "g", size) * 1.36


def _digito(c, s, cx, y, size, estilo, cor, a):
    escreve(c, s, cx - larg(s, estilo, size) / 2, y, size, estilo, cor, a)


def _virgula(c, x, y, size, cor, a, estilo="g"):
    escreve(c, ",", x - larg(",", estilo, size) / 2, y, size, estilo, cor, a)


def numero(c, s, xv, y, size, estilo="g", cor=None, a=1.0, cores=None):
    """número alinhado pela vírgula: xv = onde fica a vírgula (sem vírgula, a borda direita das unidades).
    cores = {índice do caractere: cor}. Devolve {índice: x do centro}"""
    if a <= 0:
        return {}
    xs = _centros(s, xv, size)
    for i, ch in enumerate(s):
        if ch == ",":
            _virgula(c, xv, y, size, (cores or {}).get(i, cor or TINTA), a, estilo)
        else:
            _digito(c, ch, xs[i], y, size, estilo, (cores or {}).get(i, cor or TINTA), a)
    return xs


def anda(c, t, dig, pos, saltos, x, y, size, cor=None, cor_v=None, cor_novo=None, tv=None, some=False):
    """a vírgula anda e os algarismos ficam parados. dig = algarismos sem vírgula ("37"); pos = quantos antes da vírgula (1 = 3,7).
    saltos = [(t0, pos nova), ...]; o zero que faltar entra ao fim do salto. x = borda esquerda do primeiro algarismo.
    tv = instante em que a vírgula aparece (a "vírgula escondida" de 45); some = a vírgula some no fim (370)."""
    cor, cor_v, cor_novo = cor or TINTA, cor_v or COR_TEXTO, cor_novo or COR_TEXTO
    cl = casa(size)
    px = lambda i: x + (i + 0.5) * cl  # centro da casa i
    atual, fim = float(pos), pos
    for t0, novo in saltos:
        q = ease_io(prog(t, t0, 0.7))
        if q <= 0:
            break
        if q >= 1:
            atual, fim = float(novo), novo
            continue
        atual = lerp(fim, novo, q)
        break
    pulo = 0.0
    for t0, novo in saltos:
        q = prog(t, t0, 0.7)
        if 0 < q < 1:
            pulo = math.sin(q * math.pi) * size * 0.95  # por cima do algarismo, não através dele
    for i, ch in enumerate(dig):
        _digito(c, ch, px(i), y, size, "g", cor, 1.0)
    vistos = set()
    for t0, novo in saltos:  # o zero que a vírgula pediu: à direita até ela, ou à esquerda dela com o 0 antes da vírgula
        casas_ = range(len(dig), novo) if novo > 0 else range(novo - 1, 0)
        for i in casas_:
            if i not in vistos:
                vistos.add(i)
                foco(c, t, t0 + 0.55, 0.4, lambda a, i=i: _digito(c, "0", px(i), y, size, "g", cor_novo, a))
    vis = 1.0 if tv is None else ep(t, tv, 0.4)
    if some and saltos:
        vis *= 1 - ep(t, saltos[-1][0] + 0.9, 0.4)
    _virgula(c, x + atual * cl, y - pulo, size, cor_v, vis)
    return px


def armada(c, t, nums, op, res, tn, tr, xv, y0, size=110, dy=None, cor_res=None, cz=None, tz=None, marcas=(), tl=None, escuro=False, tv=None, vai=()):
    """conta armada de somar ou subtrair, com vírgula sobre vírgula. A conta é refeita aqui: número errado não passa.
    nums = ["2,35", "1,4"]; tn = instante de cada número; res = "3,75"; tr = instantes dos algarismos do resultado, da direita para a esquerda.
    tz = instante dos zeros que completam as casas (cor cz). marcas = [(linha, índice do caractere, novo, t0)]: empréstimo.
    tv = instante da vírgula do resultado. vai = [(coluna contada da direita, texto, t0[, t_some])]: vai-um, em cima da conta."""
    op = "−" if op == "-" else op
    dec = lambda s: Decimal(s.replace(",", "."))
    a_, b_ = dec(nums[0]), dec(nums[1])
    assert (a_ + b_ if op == "+" else a_ - b_) == dec(res), (nums, op, res)
    tinta = "#FFFFFF" if escuro else TINTA
    forte = cor_res or (CLARO if escuro else COR_TEXTO)
    dy = dy or size * 1.22
    cd = max(len((n.split(",") + [""])[1]) for n in nums + [res])
    cheio = []
    for n in nums:
        i, d = (n.split(",") + [""])[:2]
        cheio.append((i + "," + d.ljust(cd, "0")) if cd else i)
    res_ = res if not cd else (res.split(",")[0] + "," + (res.split(",") + [""])[1].ljust(cd, "0"))
    posic = {}
    for l, (n, cheia) in enumerate(zip(nums, cheio)):
        y = y0 + l * dy
        foco(c, t, tn[l], 0.45, lambda a, n=n, y=y: numero(c, n, xv, y, size, "g", tinta, a))
        if len(cheia) > len(n):  # os zeros que completam as casas, e a vírgula se ela estava escondida
            ti = tz if tz is not None else tn[l]
            foco(c, t, ti, 0.45, lambda a, n=n, cheia=cheia, y=y: _so(c, cheia, xv, y, size, range(len(n), len(cheia)), cz or forte, a))
        posic[l] = _centros(cheia, xv, size)
    larg_i = max(len(s.split(",")[0]) for s in cheio + [res_])
    x_op = xv - (larg_i + 1.0) * casa(size)
    ti_l = tl if tl is not None else tn[-1] + 0.2
    foco(c, t, ti_l, 0.4, lambda a: _digito(c, op, x_op, y0 + dy, size, "g", tinta, a))
    y_l = y0 + (len(nums) - 1) * dy + size * 0.32
    if t >= ti_l:
        M.line(c, x_op - size * 0.42, y_l, xv + (cd + 0.4) * casa(size), y_l, tinta, 1.0, 6, progress=ep(t, ti_l, 0.5))
    y_r = y0 + len(nums) * dy + size * 0.12
    idx = [i for i, ch in enumerate(res_) if ch != ","][::-1]
    cres = _centros(res_, xv, size)
    assert len(tr) == len(idx), (len(tr), len(idx))
    for i, ti in zip(idx, tr):
        foco(c, t, ti, 0.4, lambda a, i=i: _digito(c, res_[i], cres[i], y_r, size, "g", forte, a))
    if cd:
        ti_v = tv if tv is not None else tr[min(cd, len(tr) - 1)] - 0.15 if len(tr) > cd else tr[-1]
        foco(c, t, ti_v, 0.4, lambda a: _virgula(c, xv, y_r, size, forte, a))
    for v in vai:
        _vai(c, t, v, cres[idx[v[0]]], y0 - size * 0.86, size, CERTO)
    for n_, (l, i, novo, t0) in enumerate(marcas):
        depois = [m[3] for m in marcas[n_ + 1:] if m[:2] == (l, i)]  # a mesma casa muda de novo: 0 → 10 → 9
        corta(c, t, t0, posic[l][i], y0 + l * dy - size * 0.36, size, novo, cor_novo=CERTO, tf=depois[0] if depois else None)
    return dict(y_res=y_r, x_op=x_op, centros=posic, cres=cres)


def _vai(c, t, v, x, y, size, cor):
    """o algarismo pequeno que sobe para a próxima coluna: (coluna, texto, t0[, t_some])"""
    t_some = v[3] if len(v) > 3 else 1e9
    s = size * 0.5
    saida(c, t, t_some, lambda: foco(c, t, v[2], 0.4, lambda a: centro(c, str(v[1]), x, y, s, "g", cor, a), sobe=-14))


def conta_mult(c, t, a, b, tn, tl, xv, y0, size=100, tz=(), tr=(), tsoma=None, vai=(), escuro=False, cor=None):
    """conta armada de multiplicar, refeita aqui: a de cima, b de baixo, inteiros.
    tn = (instante de a, de b); tl = uma lista por linha, com os instantes dos algarismos da direita para a esquerda (sem o zero de deslocamento).
    tz = instante do zero de cada linha depois da primeira; tsoma = traço da soma; tr = algarismos da soma, da direita para a esquerda.
    vai = [(coluna contada da direita, texto, t0[, t_some])]. Devolve as posições, para desenhar por cima."""
    tinta = "#FFFFFF" if escuro else TINTA
    forte = cor or (CLARO if escuro else COR_TEXTO)
    cl, dy = larg("0", "g", size) * 1.14, size * 1.16
    px = lambda k: xv - (k + 0.5) * cl
    sa, sb = str(a), str(b)
    parciais = [a * int(ch) for ch in reversed(sb)]
    assert len(tl) == len(parciais), (len(tl), len(parciais))
    assert sum(p * 10 ** i for i, p in enumerate(parciais)) == a * b

    def num(s, y, cor_, q):
        for k, ch in enumerate(reversed(s)):
            _digito(c, ch, px(k), y, size, "g", cor_, q)

    foco(c, t, tn[0], 0.45, lambda q: num(sa, y0, tinta, q))
    foco(c, t, tn[1], 0.45, lambda q: num(sb, y0 + dy, tinta, q))
    w = max(len(str(a * b)), len(sa), len(sb) + 1)
    x_op = px(len(sb)) - cl * 0.15
    foco(c, t, tn[1], 0.45, lambda q: _digito(c, "×", x_op, y0 + dy, size, "g", tinta, q))
    y_l = y0 + dy + size * 0.3
    if t >= tn[1]:
        M.line(c, xv - (w + 1.2) * cl, y_l, xv + cl * 0.2, y_l, tinta, 1.0, 6, progress=ep(t, tn[1] + 0.2, 0.5))
    ys = []
    so_uma = len(parciais) == 1
    for i, (p_, tis) in enumerate(zip(parciais, tl)):
        y = y0 + (2 + i) * dy + size * 0.12
        ys.append(y)
        dig = str(p_)[::-1]
        assert len(tis) == len(dig), (p_, len(tis), len(dig))
        if i:
            foco(c, t, tz[i - 1], 0.4, lambda q, i=i, y=y: [_digito(c, "0", px(k), y, size, "g", forte, q) for k in range(i)])
        for k, (ch, ti) in enumerate(zip(dig, tis)):
            foco(c, t, ti, 0.4, lambda q, k=k, ch=ch, y=y, i=i: _digito(c, ch, px(k + i), y, size, "g", forte if so_uma else tinta, q))
    if tsoma is not None:
        y_s = ys[-1] + size * 0.3
        M.line(c, xv - (w + 1.2) * cl, y_s, xv + cl * 0.2, y_s, tinta, 1.0, 6, progress=ep(t, tsoma, 0.5))
        _digito(c, "+", xv - (w + 0.65) * cl, ys[-1], size, "g", tinta, ep(t, tsoma, 0.4))
        dig = str(a * b)[::-1]
        assert len(tr) == len(dig), (len(tr), len(dig))
        for k, (ch, ti) in enumerate(zip(dig, tr)):
            foco(c, t, ti, 0.4, lambda q, k=k, ch=ch: _digito(c, ch, px(k), ys[-1] + dy + size * 0.12, size, "g", forte, q))
    for v in vai:
        _vai(c, t, v, px(v[0]), y0 - size * 0.92, size, CERTO)
    return dict(px=px, ys=ys, dy=dy, cl=cl)


def _centros(s, xv, size):
    """centro de cada algarismo: casas justas, com um respiro só em volta da vírgula"""
    cl, folga = larg("0", "g", size) * 1.1, size * 0.17
    v = s.find(",")
    ate = len(s) if v < 0 else v
    return {i: (xv - folga - (ate - i - 0.5) * cl if i < ate else xv + folga + (i - v - 0.5) * cl) for i, ch in enumerate(s) if ch != ","}


def _so(c, s, xv, y, size, indices, cor, a):
    """só os caracteres de `indices`, cada um na sua casa"""
    cen = _centros(s, xv, size)
    for i in indices:
        if i in cen:
            _digito(c, s[i], cen[i], y, size, "g", cor, a)
        else:
            _virgula(c, xv, y, size, cor, a)


def dividir(dividendo, divisor, casas_max=6):
    """faz a divisão de verdade, como no papel, e devolve os passos: a tela e a conta não têm como divergir.
    dividendo = "7,5" ou "7"; divisor inteiro. Cada passo: parte, q, resto, coluna, desceu, depois_da_virgula, zero (zero acrescentado)."""
    i_, d_ = (dividendo.split(",") + [""])[:2]
    digs = [(int(ch), False, False) for ch in i_] + [(int(ch), True, False) for ch in d_]
    passos_, r, q_txt, tem_v = [], 0, "", False
    n, extras = 0, 0
    while True:
        if n < len(digs):
            d, depois, zero = digs[n]
        elif r == 0 or extras >= casas_max:
            break
        else:
            d, depois, zero = 0, True, True
            extras += 1
        parte = r * 10 + d
        q, r = parte // divisor, parte % divisor
        if depois and not tem_v:
            q_txt = (q_txt or "0") + ","
            tem_v = True
        if not (not q_txt and q == 0 and n < len(i_) - 1):
            q_txt += str(q)
            passos_.append(dict(parte=parte, q=q, resto=r, coluna=n, desceu=d, depois=depois, zero=zero))
        n += 1
    exato = Fraction(dividendo.replace(",", ".")) / divisor
    if r == 0:
        assert Fraction(q_txt.replace(",", ".")) == exato, (dividendo, divisor, q_txt)
    elif "," not in q_txt and "," not in dividendo:
        assert int(q_txt) * divisor + r == int(dividendo), (dividendo, divisor, q_txt, r)
    return dict(dividendo=dividendo, divisor=divisor, quociente=q_txt, passos=passos_, resto=r)


def conta_div(c, t, D, tq, tr, t0, x, y, size=104, tv=None, escuro=False, cor=None, ts=None):
    """conta de dividir na chave, em que cada resto recebe o algarismo que desce. D = dividir(...).
    t0 = instante da conta; tq = instante de cada algarismo do quociente; tr = instante de cada linha (uma por passo depois do primeiro, e o resto final).
    tv = instante da vírgula no quociente (sem isso, entra com o primeiro algarismo depois dela). x = borda esquerda do dividendo.
    ts = instante em que o resto aparece sozinho, uma por linha menos a última; em tr o algarismo desce e completa a linha."""
    tinta = "#FFFFFF" if escuro else TINTA
    forte = cor or (CLARO if escuro else COR_TEXTO)
    cl, dy = casa(size), size * 1.12
    txt = D["dividendo"].replace(",", "")
    v = D["dividendo"].find(",")
    px = lambda i: x + (i + 0.5) * cl
    cols = max(len(txt), D["passos"][-1]["coluna"] + 1)
    xb = x + cols * cl + size * 0.5  # a chave fica depois da última coluna usada
    def cabeca(a):
        for i, ch in enumerate(txt):
            _digito(c, ch, px(i), y, size, "g", tinta, a)
        if v >= 0:
            _virgula(c, x + v * cl, y, size, tinta, a)
    foco(c, t, t0, 0.45, cabeca)
    s_div = str(D["divisor"])
    lw = max(larg(s_div, "g", size) + size * 0.9, (len(D["quociente"]) + 0.6) * cl)
    y_top, y_meio = y - size * 0.92, y + size * 0.22
    if t >= t0 + 0.2:
        p = ep(t, t0 + 0.2, 0.5)
        M.line(c, xb, y_top, xb, y_meio, tinta, 1.0, 7, progress=p)
        M.line(c, xb, y_meio, xb + lw, y_meio, tinta, 1.0, 7, progress=p)
    foco(c, t, t0 + 0.2, 0.45, lambda a: escreve(c, s_div, xb + size * 0.38, y, size, "g", tinta, a))
    # quociente: cada algarismo na sua casa, a vírgula entre as casas
    q, y_q, xq = D["quociente"], y + size * 1.22, xb + size * 0.42
    ind = [i for i, ch in enumerate(q) if ch != ","]
    assert len(tq) == len(ind), (len(tq), len(ind), q)
    pos_v = q.find(",")
    xv_q = xq + (pos_v if pos_v >= 0 else len(q)) * larg("0", "g", size) * 1.1 + size * 0.17
    cen = _centros(q, xv_q, size)
    for i, ti in zip(ind, tq):
        foco(c, t, ti, 0.4, lambda a, i=i: _digito(c, q[i], cen[i], y_q, size, "g", forte, a))
    if pos_v >= 0:
        ti = tv if tv is not None else tq[pos_v]
        foco(c, t, ti, 0.4, lambda a: _virgula(c, xv_q, y_q, size, forte, a))
    # linhas de baixo: o resto de cada passo com o algarismo que desceu
    linhas = [(p["parte"], p["coluna"], p["zero"]) for p in D["passos"][1:]] + [(D["resto"], D["passos"][-1]["coluna"], None)]
    assert len(tr) == len(linhas), (len(tr), len(linhas))
    for j, ((v_, col, zero), ti) in enumerate(zip(linhas, tr)):
        s, yy = str(v_), y + (j + 1) * dy
        fim = zero is None and v_ == 0
        def linha_(a, s=s, yy=yy, col=col, zero=zero, fim=fim, so=None):
            for m, ch in enumerate(s):
                if so is not None and (m == len(s) - 1) != so:
                    continue
                i = col - (len(s) - 1 - m)
                cor_ = CERTO if fim else forte if (zero and m == len(s) - 1) else tinta
                _digito(c, ch, px(i), yy, size, "g", cor_, a)
        if ts is not None and j < len(ts):
            foco(c, t, ts[j], 0.4, lambda a, f=linha_: f(a, so=False))  # o resto, antes de o algarismo descer
            foco(c, t, ti, 0.4, lambda a, f=linha_: f(a, so=True))
        else:
            foco(c, t, ti, 0.4, linha_)
    return dict(xb=xb, lw=lw, y_q=y_q, xq=xq, cl=cl, dy=dy)


def quadro_casas(c, t, nomes, tc, linhas, x, y, w_col, size=96, h_lin=None, cor_cab=None, a=1.0, grossa=1):
    """quadro de casas. nomes = cabeçalhos; tc = instante de cada um; linhas = [[(algarismo ou "", t0[, cor]), ...], ...].
    Uma linha grossa antes da coluna `grossa` separa o inteiro das casas decimais; grossa=None para centena, dezena, unidade."""
    h_lin = h_lin or size * 1.45
    alto = y + h_lin * len(linhas) + 10
    for i, (nome, ti) in enumerate(zip(nomes, tc)):
        cx = x + (i + 0.5) * w_col
        foco(c, t, ti, 0.45, lambda q, nome=nome, cx=cx: centro(c, nome, cx, y - 26, 46, "i", cor_cab or COR_TEXTO, q * a))
        if i:
            xl = x + i * w_col
            if t >= ti:
                M.line(c, xl, y - 76, xl, alto, TINTA if i == grossa else FIO, a, 6 if i == grossa else 3, progress=ep(t, ti, 0.4))
    for j, lin in enumerate(linhas):
        yy = y + h_lin * j + size * 1.02
        for i, (s, ti, *cor) in enumerate(lin):
            if s != "":
                foco(c, t, ti, 0.4, lambda q, s=s, i=i, yy=yy, cor=cor: centro(c, s, x + (i + 0.5) * w_col, yy, size, "g", cor[0] if cor else TINTA, q * a))


def reta(c, t, t0, x0, x1, y, vmin, vmax, marcas, fmt=str, cor=None, escuro=False, size=46, tm=None):
    """reta numérica; marcas = valores com traço e rótulo; tm = instante de cada marca (senão, entram em fila). Devolve a função valor → x"""
    tinta = "#FFFFFF" if escuro else TINTA
    vx = lambda v: x0 + (float(v) - float(vmin)) / (float(vmax) - float(vmin)) * (x1 - x0)
    if t >= t0:
        M.arrow(c, x0 - 40, y, x1 + 60, y, cor or tinta, ep(t, t0, 0.6), 5, 18, ep(t, t0, 0.6))
    for i, v in enumerate(marcas):
        ti = tm[i] if tm else t0 + 0.2 + i * 0.08
        foco(c, t, ti, 0.4, lambda a, v=v: (M.line(c, vx(v), y - 20, vx(v), y + 20, tinta, a, 5),
                                            centro(c, fmt(v), vx(v), y + 80, size, "b", tinta, a)), sobe=6)
    return vx


def salto(c, t, t0, x0, x1, y, alto=120, cor=None, rotulo=None, d=0.7, largura=7, size=52):
    """arco de x0 a x1 sobre a reta, com ponta de seta e rótulo em cima"""
    p = ease_out(prog(t, t0, d))
    if p <= 0:
        return
    cor = cor or COR_TEXTO
    ant = (x0, y)
    n = max(2, int(36 * p))
    for i in range(1, n + 1):
        u = p * i / n
        pt = (lerp(x0, x1, u), y - alto * math.sin(u * math.pi))
        M.line(c, ant[0], ant[1], pt[0], pt[1], cor, 1.0, largura)
        ant = pt
    if p >= 0.99:
        lado = 1 if x1 > x0 else -1
        M.line(c, x1, y, x1 - lado * 22, y - 24, cor, 1.0, largura)
        M.line(c, x1, y, x1 + lado * 6, y - 32, cor, 1.0, largura)
    if rotulo:
        foco(c, t, t0 + 0.2, 0.4, lambda a: centro(c, rotulo, (x0 + x1) / 2, y - alto - 28, size, "b", cor, a), sobe=6)


def valor_expr(s):
    """calcula a expressão como escrita na tela, com frações exatas"""
    x = s.replace("×", "*").replace("÷", "/").replace("−", "-").replace("[", "(").replace("]", ")").replace(".", "")
    return eval(re.sub(r"\d+", lambda m: f"Fraction({m.group()})", x), {"Fraction": Fraction})


def expressao(c, t, estados, tp, cx, y, size=96, empilha=0, cor=None, escuro=False, t0=None):
    """expressão que se resolve no lugar. estados = [(texto, trecho da vez ou None[, instante do destaque]), ...]; todos precisam valer o mesmo (assert).
    tp = instante em que cada estado passa ao seguinte (um a menos que os estados); sem instante próprio, o trecho acende em tp[k] - 0.9.
    t0 = entrada do primeiro estado. empilha = dy: em vez de trocar no lugar, cada etapa desce uma linha e a anterior fica cinza."""
    assert all(valor_expr(e[0]) == valor_expr(estados[0][0]) for e in estados), [e[0] for e in estados]
    assert len(tp) == len(estados) - 1
    tinta = "#FFFFFF" if escuro else TINTA
    forte = cor or (CLARO if escuro else COR_TEXTO)
    ini = [t0 if t0 is not None else -1.0] + list(tp)
    for k, e in enumerate(estados):
        s, trecho = e[0], e[1]
        fim = tp[k] if k < len(tp) else 1e9
        if not empilha and t >= fim + 0.45:
            continue
        ty = e[2] if len(e) > 2 else (tp[k] - 0.9 if k < len(tp) else 1e9)
        yy = y + k * empilha

        def desenha(a, s=s, trecho=trecho, ty=ty, yy=yy, fim=fim):
            x = cx - larg(s, "g", size) / 2
            ate = lambda u: larg(u, "g", size) + (APERTO["g"] * size if u else 0)  # onde escreve termina: conta o aperto depois da última letra
            i0 = s.find(trecho) if trecho else -1
            ativo = trecho and t >= ty and (not empilha or t < fim)
            if ativo:
                w, x0 = larg(trecho, "g", size), x + ate(s[:i0])
                M.rrect(c, x0 - size * 0.14, yy - size * 0.92, w + size * 0.28, size * 1.2, size * 0.2, forte, 0.16 * a * ep(t, ty, 0.3))
            if empilha and t >= fim:
                escreve(c, s, x, yy, size, "g", CINZA, a)
            elif ativo:
                escreve(c, s[:i0], x, yy, size, "g", tinta, a)
                escreve(c, trecho, x + ate(s[:i0]), yy, size, "g", forte, a)
                escreve(c, s[i0 + len(trecho):], x + ate(s[:i0 + len(trecho)]), yy, size, "g", tinta, a)
            else:
                escreve(c, s, x, yy, size, "g", tinta, a)

        if not empilha and fim <= t < fim + 0.45:
            saida(c, t, fim, lambda: desenha(1.0), d=0.4)
        else:
            foco(c, t, ini[k], 0.45, desenha)


def divida(c, cx, cy, w, h, valor, a=1.0, cancela=0.0, topo="dívida", cor=None):
    """cartão de dívida; cancela = 0..1 risca o cartão e ele apaga. É a imagem de MAT-FRA-016: tirar uma dívida é como ganhar"""
    if a <= 0:
        return
    cor = cor or ERRADO
    q = a * (1 - 0.65 * clamp(cancela))
    c.save(); c.translate(cx, cy); c.rotate(-3)
    M.rrect(c, -w / 2, -h / 2, w, h, 14, VAZIO, q)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(-w / 2, -h / 2, w, h), 14, 14), M.paint(cor, q, stroke=5))
    centro(c, topo, 0, -h * 0.12, h * 0.26, "i", TINTA2, q)
    centro(c, str(valor), 0, h * 0.34, h * 0.4, "g", cor, q)
    c.restore()
    if cancela > 0:
        k = min(w, h) * 0.5
        M.line(c, cx - k, cy - k, cx + k, cy + k, TINTA, a, 8, progress=ease_out(clamp(cancela)))


def moeda(c, cx, cy, r, s, a=1.0, cor=None):
    """moeda na cor da matéria, com aro e o valor no meio"""
    if a <= 0 or r <= 1:
        return
    cor = cor or COR
    bola(c, cx, cy, r, cor, a)
    tom = M.on(cor)
    c.drawCircle(cx, cy, r * 0.82, M.paint(tom, 0.55 * a, stroke=max(2, r * 0.05)))
    size = r * (0.8 if len(s) <= 2 else 0.58 if len(s) <= 3 else 0.46)
    centro(c, s, cx, cy + size * 0.35, size, "g", tom, a)


# ---------------- capa ----------------
def capa_base(c, cor, grande=1.0):
    """fundo da capa: a cor da matéria em tela cheia, que é o que identifica a matéria na lista de vídeos"""
    p = skia.Paint(AntiAlias=True)
    p.setShader(skia.GradientShader.MakeRadial(
        skia.Point(W * 0.34, H * 0.4), W * 0.85, [hexc(mix(cor, "#FFFFFF", 0.1)), hexc(cor), hexc(mix(cor, "#000000", 0.42))], [0.0, 0.5, 1.0]))
    c.drawRect(skia.Rect.MakeWH(W, H), p)
    tom = M.on(cor)
    g = M.paint(tom, 0.05, stroke=1.5)
    for x in range(0, W + 1, 96):
        c.drawLine(x, 0, x, H, g)
    for y in range(0, H + 1, 96):
        c.drawLine(0, y, W, y, g)
    arco(c, W * 0.98, H * 1.1, 760, 180, 110, tom, 100, 0.08)


def capa_rotulo(c, materia, cor):
    tom = M.on(cor)
    s = materia.upper()
    w = larg(s, "b", 46) + 76
    r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(80, 72, w, 88), 44, 44)
    c.drawRRect(r, M.paint(tom))
    escreve(c, s, 118, 132, 46, "b", cor)


def capa_modelo(c, materia, l1, l2, it):
    """o modelo de capa: tira da matéria, duas linhas pesadas, uma itálica e a forma-símbolo"""
    cor = MATERIAS[materia]["cor"]
    capa_base(c, cor)
    capa_rotulo(c, materia, cor)
    tom = M.on(cor)
    escreve(c, l1, 76, 450, 210, "g", tom)
    escreve(c, l2, 76, 660, 210, "g", tom)
    escreve(c, it, 84, 860, 170, "i", tom)
    (mais if MATERIAS[materia]["forma"] == "mais" else bola)(c, 1640, 760, 210, mix(cor, "#FFFFFF", 0.82), 1.0)
