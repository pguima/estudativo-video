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


def orbita(c, cx, cy, r, cor=None, a=1.0, giro=0.0, sombra=True):
    """o símbolo da Física: um núcleo com volume e duas órbitas cruzadas, cada uma com um elétron. r = meia largura da órbita"""
    cor = cor or COR
    if a <= 0 or r <= 0:
        return
    ry, lw, rn = r * 0.36, max(3, r * 0.085), r * 0.3
    claro, escuro = hexc(mix(cor, "#FFFFFF", 0.22), a), hexc(mix(cor, "#000000", 0.25), a)

    def aneis(frente):
        for k, ang in enumerate((28, -28)):
            c.save(); c.translate(cx, cy); c.rotate(ang + giro)
            p = skia.Paint(AntiAlias=True, Style=skia.Paint.kStroke_Style, StrokeWidth=lw)
            p.setShader(skia.GradientShader.MakeLinear([skia.Point(-r, -ry), skia.Point(r, ry)], [claro, escuro]))
            ret = skia.Rect.MakeXYWH(-r, -ry, 2 * r, 2 * ry)
            c.drawArc(ret, 0 if frente else 180, 180, False, p)  # metade de baixo passa na frente do núcleo
            if frente:  # elétron na frente, em lados opostos nas duas órbitas
                e = math.radians(18 if k == 0 else 162)
                c.drawCircle(r * math.cos(e), ry * math.sin(e), lw * 1.35, M.paint(mix(cor, "#000000", 0.18), a))
            c.restore()
    if sombra:
        s = skia.Paint(AntiAlias=True, Color=hexc("#000000", 0.2 * a))
        s.setMaskFilter(skia.MaskFilter.MakeBlur(skia.kNormal_BlurStyle, r * 0.08))
        c.drawCircle(cx + r * 0.05, cy + r * 0.1, rn, s)
    aneis(False)
    bola(c, cx, cy, rn, cor, a)
    aneis(True)


def hexagono(c, cx, cy, r, cor=None, a=1.0, giro=0.0, sombra=True):
    """o símbolo da Química: anel hexagonal com volume, como o benzeno, com o círculo das ligações no meio. r = raio do anel"""
    cor = cor or COR
    if a <= 0 or r <= 0:
        return
    lw = r * 0.26

    def hexa(R):
        p = skia.Path()
        for k in range(6):
            g = math.radians(90 + 60 * k)
            (p.moveTo if k == 0 else p.lineTo)(R * math.cos(g), -R * math.sin(g))
        p.close()
        return p
    anel = hexa(r)
    c.save(); c.translate(cx, cy); c.rotate(giro)
    if sombra:
        s = skia.Paint(AntiAlias=True, Color=hexc("#000000", 0.22 * a), Style=skia.Paint.kStroke_Style, StrokeWidth=lw)
        s.setStrokeJoin(skia.Paint.kRound_Join)
        s.setMaskFilter(skia.MaskFilter.MakeBlur(skia.kNormal_BlurStyle, r * 0.07))
        c.save(); c.translate(r * 0.07, r * 0.11); c.drawPath(anel, s); c.restore()
    p = skia.Paint(AntiAlias=True, Style=skia.Paint.kStroke_Style, StrokeWidth=lw)
    p.setStrokeJoin(skia.Paint.kRound_Join)
    p.setShader(skia.GradientShader.MakeLinear(
        [skia.Point(-r, -r), skia.Point(r, r)], [hexc(mix(cor, "#FFFFFF", 0.25), a), hexc(cor, a), hexc(mix(cor, "#000000", 0.3), a)], [0.0, 0.5, 1.0]))
    c.drawPath(anel, p)
    brilho = skia.Paint(AntiAlias=True, Style=skia.Paint.kStroke_Style, StrokeWidth=lw * 0.16, Color=hexc("#FFFFFF", 0.35 * a))
    brilho.setStrokeJoin(skia.Paint.kRound_Join)
    c.drawPath(hexa(r + lw * 0.22), brilho)
    q = skia.Paint(AntiAlias=True, Style=skia.Paint.kStroke_Style, StrokeWidth=lw * 0.42)
    q.setShader(skia.GradientShader.MakeLinear(
        [skia.Point(-r * 0.5, -r * 0.5), skia.Point(r * 0.5, r * 0.5)], [hexc(mix(cor, "#FFFFFF", 0.15), a), hexc(mix(cor, "#000000", 0.3), a)]))
    c.drawCircle(0, 0, r * 0.47, q)
    c.restore()


def simbolo(c, cx, cy, r, a=1.0, giro=0.0, cor=None, forma=None):
    """forma-símbolo da matéria atual (desenhadas: o + da Matemática, a órbita da Física e o hexágono da Química; as outras saem como esfera)"""
    forma = forma or FORMA
    if forma == "mais":
        mais(c, cx, cy, r, cor, a=a, giro=giro)
    elif forma == "orbita":
        orbita(c, cx, cy, r, cor, a=a, giro=giro)
    elif forma == "hexagono":
        hexagono(c, cx, cy, r * 0.92, cor, a=a, giro=giro)
    else:
        bola(c, cx, cy, r, cor, a=a)


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


# ---------------- fórmulas: expoente, raiz e fração em linha ----------------
def _ler(s, i=0, fim=None):
    """lê a escrita de fórmula até `fim`: 2^5, 10^{-3}, r{72}, r3{27} (índice antes da chave), f{2}{3}. Devolve (nós, posição)"""
    nos, txt = [], ""

    def solta():
        nonlocal txt
        if txt:
            nos.append(("t", txt))
            txt = ""

    while i < len(s):
        ch = s[i]
        if ch == fim:
            solta()
            return nos, i + 1
        if ch == "^":
            solta()
            if s[i + 1] == "{":
                dentro, i = _ler(s, i + 2, "}")
            else:
                dentro, i = [("t", s[i + 1])], i + 2
            nos.append(("e", dentro))
        elif ch == "r" and i + 1 < len(s) and (s[i + 1] == "{" or (s[i + 1] in "0123456789" and i + 2 < len(s) and s[i + 2] == "{")):
            solta()
            ind = None
            i += 1
            if s[i] != "{":
                ind, i = s[i], i + 1
            dentro, i = _ler(s, i + 1, "}")
            nos.append(("r", dentro, ind))
        elif ch == "f" and i + 1 < len(s) and s[i + 1] == "{":
            solta()
            cima, i = _ler(s, i + 2, "}")
            baixo, i = _ler(s, i + 1, "}")
            nos.append(("f", cima, baixo))
        else:
            txt += ch
            i += 1
    solta()
    return nos, i


def _medir(nos, size, est):
    w = 0.0
    for n in nos:
        if n[0] == "t":
            w += larg(n[1], est, size) + APERTO[est] * size + size * 0.02
        elif n[0] == "e":
            w += _medir(n[1], size * 0.58, est) + size * 0.04
        elif n[0] == "r":
            w += _medir(n[1], size, est) + size * 0.62 + (size * 0.14 if n[2] else 0)
        else:
            w += max(_medir(n[1], size * 0.78, est), _medir(n[2], size * 0.78, est)) + size * 0.22
    return w


def _desenhar(c, nos, x, y, size, est, cor, a):
    for n in nos:
        if n[0] == "t":
            escreve(c, n[1], x, y, size, est, cor, a)
            x += larg(n[1], est, size) + APERTO[est] * size + size * 0.02
        elif n[0] == "e":
            _desenhar(c, n[1], x + size * 0.02, y - size * 0.42, size * 0.58, est, cor, a)
            x += _medir(n[1], size * 0.58, est) + size * 0.04
        elif n[0] == "r":
            dentro = _medir(n[1], size, est)
            if n[2]:
                escreve(c, n[2], x, y - size * 0.5, size * 0.42, est, cor, a)
                x += size * 0.14
            tem_f = any(m[0] == "f" for m in n[1])  # com fração dentro, a raiz cresce para abraçar os dois andares
            alto, baixo, l = y - size * (1.2 if tem_f else 0.92), y + size * (0.56 if tem_f else 0.06), max(4, size * 0.075)
            x0, x1, x2, x3 = x + size * 0.04, x + size * 0.15, x + size * 0.3, x + size * 0.5
            p = skia.Path()
            p.moveTo(x0, y - size * 0.3); p.lineTo(x1, y - size * 0.38); p.lineTo(x2, baixo); p.lineTo(x3, alto); p.lineTo(x3 + dentro + size * 0.1, alto)
            pt = M.paint(cor, a, stroke=l, cap_round=True)
            pt.setStrokeJoin(skia.Paint.kRound_Join)
            c.drawPath(p, pt)
            _desenhar(c, n[1], x3 + size * 0.06, y, size, est, cor, a)
            x += dentro + size * 0.62
        else:
            s_ = size * 0.78
            wc, wb = _medir(n[1], s_, est), _medir(n[2], s_, est)
            w = max(wc, wb) + size * 0.12
            _desenhar(c, n[1], x + (w - wc) / 2, y - size * 0.46, s_, est, cor, a)
            _desenhar(c, n[2], x + (w - wb) / 2, y + size * 0.46, s_, est, cor, a)
            b = max(4, size * 0.07)
            c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y - size * 0.3 - b / 2, w, b), b / 2, b / 2), M.paint(cor, a))
            x += w + size * 0.1
    return x


def formula(c, s, x, y, size, estilo="g", cor=None, a=1.0, align="left"):
    """fórmula numa linha, com expoente, raiz e fração de verdade. x é a borda (ou o centro, com align="center"), y a linha de base. Devolve a largura.
    Escrita: 2^5 · 2^4 | 10^{−3} | r{72} (raiz) | 6r{2} | r3{27} (cúbica) | r4{16} | f{2}{3} (fração) | (f{2}{3})^3 | 9^{1/2} | r{f{9}{16}}"""
    nos, _ = _ler(s)
    w = _medir(nos, size, estilo)
    if a > 0:
        xi = x - w / 2 if align == "center" else x - w if align == "right" else x
        _desenhar(c, nos, xi, y, size, estilo, cor or TINTA, a)
    return w


def formula_em(c, t, t0, s, x, y, size, estilo="g", cor=None, align="left"):
    """fórmula que entra com foco no instante t0"""
    foco(c, t, t0, 0.5, lambda a: formula(c, s, x, y, size, estilo, cor, a, align))


def cientifica(c, t, t0, n, e, x, y, size=110, cor=None, cor_e=None, te=None, align="left"):
    """número em notação científica: n = "4,5", e = expoente. te = instante do expoente (senão, junto); cor_e destaca o expoente.
    Confere a forma: 1 ≤ n < 10, senão para (assert); para mostrar a forma errada, use E.formula."""
    assert 1 <= float(n.replace(",", ".")) < 10, n
    e_ = str(e).replace("-", "−")
    corpo = f"{n} × 10"
    w_c = formula(c, corpo, 0, 0, size, a=0)
    w_e = formula(c, f"^{{{e_}}}", 0, 0, size, a=0)
    xi = x - (w_c + w_e) / 2 if align == "center" else x
    foco(c, t, t0, 0.5, lambda a: formula(c, corpo, xi, y, size, cor=cor, a=a))
    foco(c, t, te if te is not None else t0, 0.5, lambda a: formula(c, f"^{{{e_}}}", xi + w_c, y, size, cor=cor_e or cor, a=a))
    return w_c + w_e


# ---------------- equações ----------------
def balanca(c, cx, cy, esq, dir_, inclina=0.0, a=1.0, size=96, larg_braco=620, cor=None, escuro=False):
    """balança de dois pratos: esq e dir_ são fórmulas (escrita de E.formula) ou funções fn(c, x, y) que desenham sobre o prato.
    inclina: −1..1, positivo baixa o prato da direita (lado mais pesado). Fica equilibrada com 0: é a equação."""
    if a <= 0:
        return
    tinta = "#FFFFFF" if escuro else TINTA
    cor = cor or COR
    ang = math.radians(9 * clamp(inclina, -1, 1))
    topo = cy - 250
    # base e coluna
    M.rrect(c, cx - 150, cy + 220, 300, 26, 13, tinta, a)
    M.line(c, cx, cy + 220, cx, topo, tinta, a, 12)
    c.drawCircle(cx, topo, 20, M.paint(cor, a))
    pontas = []
    for lado in (-1, 1):
        px = cx + lado * larg_braco / 2 * math.cos(ang)
        py = topo + lado * larg_braco / 2 * math.sin(ang)
        pontas.append((px, py))
    M.line(c, pontas[0][0], pontas[0][1], pontas[1][0], pontas[1][1], tinta, a, 12)
    for (px, py), conteudo in zip(pontas, (esq, dir_)):
        yp = py + 300  # prato pendurado sempre na vertical, com fio longo para passar por fora da fórmula
        wt = formula(c, conteudo, 0, 0, size, a=0) if isinstance(conteudo, str) and conteudo else 200
        hw = max(170, wt / 2 + 80)
        for dx in (-hw, hw):
            M.line(c, px, py, px + dx, yp, CINZA, a, 3)
        p = skia.Path()
        p.moveTo(px - hw, yp); p.lineTo(px + hw, yp); p.lineTo(px + hw - 50, yp + 34); p.lineTo(px - hw + 50, yp + 34); p.close()
        c.drawPath(p, M.paint(cor, a))
        if callable(conteudo):
            conteudo(c, px, yp - 20)
        elif conteudo:
            formula(c, conteudo, px, yp - 24, size, cor=tinta, a=a, align="center")
    return pontas


def intervalo(c, t, t0, vx, y, ini, fim, fecha_ini=False, fecha_fim=False, cor=None, d=0.7, r=17):
    """trecho de solução sobre a reta: vx = função valor → x de E.reta; ini/fim = None para seguir até a ponta (com seta).
    fecha_* = bolinha cheia (o número entra); aberta = o número não entra."""
    p = ease_out(prog(t, t0, d))
    if p <= 0:
        return
    cor = cor or COR
    x0 = vx(ini) if ini is not None else 60
    x1 = vx(fim) if fim is not None else W - 60
    xm = lerp(x0, x1, p) if ini is not None else lerp(x1, x0, p)
    a_, b_ = (x0, xm) if ini is not None else (xm, x1)
    M.line(c, a_, y, b_, y, cor, 1.0, 12, cap_round=False)
    if p >= 0.99:
        if ini is None:
            M.line(c, x0, y, x0 + 26, y - 18, cor, 1.0, 8)
            M.line(c, x0, y, x0 + 26, y + 18, cor, 1.0, 8)
        if fim is None:
            M.line(c, x1, y, x1 - 26, y - 18, cor, 1.0, 8)
            M.line(c, x1, y, x1 - 26, y + 18, cor, 1.0, 8)
    for v, fecha in ((ini, fecha_ini), (fim, fecha_fim)):
        if v is None:
            continue
        x = vx(v)
        c.drawCircle(x, y, r, M.paint(cor if fecha else PAPEL, ep(t, t0, 0.3)))
        c.drawCircle(x, y, r, M.paint(cor, ep(t, t0, 0.3), stroke=6))


def sistema(c, t, t0, linhas, x, y, size=96, dy=None, cor=None, tl=None):
    """sistema de equações: chave à esquerda e uma fórmula por linha. tl = instante de cada linha (senão, entram juntas)."""
    dy = dy or size * 1.45
    cor = cor or TINTA
    alto, baixo = y - size * 0.95, y + (len(linhas) - 1) * dy + size * 0.35
    meio = (alto + baixo) / 2
    q = ep(t, t0, 0.5)
    if q > 0:
        p = skia.Path()
        k = size * 0.32
        p.moveTo(x, alto); p.cubicTo(x - k, alto, x - k * 0.2, meio - k, x - k, meio)
        p.cubicTo(x - k * 0.2, meio + k, x - k, baixo, x, baixo)
        c.drawPath(p, M.paint(cor, q, stroke=max(5, size * 0.07), cap_round=True))
    for i, l in enumerate(linhas):
        ti = tl[i] if tl else t0
        foco(c, t, ti, 0.5, lambda a, l=l, i=i: formula(c, l, x + size * 0.3, y + i * dy, size, cor=cor, a=a))


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
    forma = MATERIAS[materia]["forma"]
    r = 260 if forma == "orbita" else 250 if forma == "hexagono" else 210  # órbita e hexágono são vazados: precisam de mais largura
    simbolo(c, 1640 if forma not in ("orbita", "hexagono") else 1590, 760, r, cor=mix(cor, "#FFFFFF", 0.82), forma=forma)


# =====================================================================================================================
# geometria, gráficos e diagramas: todas recebem (c, t, t0, ...), entram com animação e usam a cor da matéria.
# Rótulos aceitam a escrita de E.formula ("f{1}{2}", "r{3}", "x^2"); letra grega sai na grotesca, porque a serifada não tem.
# =====================================================================================================================
def _num(v):
    """número para a tela: 3 → "3", -2 → "−2", 2.5 → "2,5\""""
    if isinstance(v, str):
        return v
    v = float(v)
    s = str(int(round(v))) if abs(v - round(v)) < 1e-9 else f"{v:.2f}".rstrip("0").rstrip(".").replace(".", ",")
    return s.replace("-", "−")


def _est(s, estilo):
    """a serifada não tem letra grega nem raiz: nesses casos o rótulo sai na grotesca bold"""
    if estilo in "is":
        f = fonte(estilo, 40)
        if any(g == 0 for g in f.textToGlyphs(re.sub(r"[{}^]", "", s))):
            return "b"
    return estilo


def _mede(s, size, estilo):
    """largura e meia altura do rótulo (fração ocupa dois andares)"""
    estilo = _est(s, estilo)
    return formula(None, s, 0, 0, size, estilo, a=0), size * (0.75 if "f{" in s else 0.37)


def _meio(c, s, cx, cy, size, estilo="b", cor=None, a=1.0):
    """rótulo centrado em (cx, cy), nas duas direções"""
    if a <= 0 or s is None or s == "":
        return
    s = _num(s)
    estilo = _est(s, estilo)
    formula(c, s, cx, cy + size * 0.36, size, estilo, cor or TINTA, a, "center")


def _cola(c, s, x, y, nx, ny, gap, size, estilo="b", cor=None, a=1.0):
    """rótulo encostado no ponto (x, y) pelo lado da direção (nx, ny): a borda mais próxima fica a `gap` px do ponto"""
    if s is None or s == "":
        return
    s = _num(s)
    n = math.hypot(nx, ny) or 1.0
    nx, ny = nx / n, ny / n
    w, hh = _mede(s, size, estilo)
    k = gap + min(abs(nx) * w / 2 + abs(ny) * hh, math.hypot(w / 2, hh))
    _meio(c, s, x + nx * k, y + ny * k, size, estilo, cor, a)


def _uni(ax, ay, bx, by):
    dx, dy = bx - ax, by - ay
    n = math.hypot(dx, dy) or 1.0
    return dx / n, dy / n


def _ponto_px(c, x, y, r, cor, a):
    if a > 0:
        c.drawCircle(x, y, r, M.paint(cor, a))


TRACO = [16, 12]  # tracejado das linhas auxiliares e das arestas ocultas


# ---------------- plano cartesiano ----------------
class Plano:
    """o que E.plano devolve: x(v) e y(v) levam valor a pixel, p(x, y) faz os dois; caixa = (x, y, w, h) do gráfico"""

    def __init__(s, x, y, w, h, xmin, xmax, ymin, ymax, escuro=False):
        s.caixa, s.xmin, s.xmax, s.ymin, s.ymax, s.escuro = (x, y, w, h), xmin, xmax, ymin, ymax, escuro
        s.ox = s.x(0) if xmin <= 0 <= xmax else x  # onde passa cada eixo
        s.oy = s.y(0) if ymin <= 0 <= ymax else y + h

    def x(s, v):
        return s.caixa[0] + (float(v) - s.xmin) / (s.xmax - s.xmin) * s.caixa[2]

    def y(s, v):
        return s.caixa[1] + s.caixa[3] - (float(v) - s.ymin) / (s.ymax - s.ymin) * s.caixa[3]

    def p(s, x, y):
        return s.x(x), s.y(y)

    __call__ = p


def _marcas(vmin, vmax, passo):
    k0 = math.ceil(vmin / passo - 1e-9)
    out, k = [], k0
    while k * passo <= vmax + 1e-9:
        out.append(round(k * passo, 10))
        k += 1
    return out


def plano(c, t, t0, x, y, w, h, xmin, xmax, ymin, ymax, passo=1, passo_y=None, marcas_x=None, marcas_y=None, grade=True,
          nomes=("x", "y"), fmt=None, size=40, escuro=False, d=0.6, rotulos=True):
    """plano cartesiano na caixa (x, y, w, h), com eixos em seta, marcas, rótulos e grade. Devolve um Plano: P.x(v), P.y(v), P(x, y).
    marcas_x/marcas_y = valores rotulados (senão, de `passo` em `passo`); fmt = valor → texto; rotulos=False só põe os traços."""
    P = Plano(x, y, w, h, xmin, xmax, ymin, ymax, escuro)
    tinta = "#FFFFFF" if escuro else TINTA
    fmt = fmt or _num
    mx = marcas_x if marcas_x is not None else _marcas(xmin, xmax, passo)
    my = marcas_y if marcas_y is not None else _marcas(ymin, ymax, passo_y or passo)
    if grade and t >= t0:
        q = ep(t, t0, 0.8) * (0.14 if escuro else 1)
        for v in _marcas(xmin, xmax, passo):
            M.line(c, P.x(v), y, P.x(v), y + h, CLARO if escuro else FIO, q, 2)
        for v in _marcas(ymin, ymax, passo_y or passo):
            M.line(c, x, P.y(v), x + w, P.y(v), CLARO if escuro else FIO, q, 2)
    if t >= t0:
        p = ep(t, t0, d)
        M.arrow(c, x - 10, P.oy, x + w + 44, P.oy, tinta, 1.0, 5, 22, p)
        M.arrow(c, P.ox, y + h + 10, P.ox, y - 44, tinta, 1.0, 5, 22, p)
    nx_, ny_ = nomes
    foco(c, t, t0 + d * 0.8, 0.4, lambda a: _meio(c, nx_, x + w + 44, P.oy + 42, 56, "i", tinta, a))
    foco(c, t, t0 + d * 0.8, 0.4, lambda a: _cola(c, ny_, P.ox + 16, y - 30, 1, 0, 0, 56, "i", tinta, a))
    zero = False
    for i, v in enumerate(mx):
        if abs(v) < 1e-12 and P.ox == P.x(0):
            zero = True
            continue
        X = P.x(v)
        foco(c, t, t0 + 0.2 + i * 0.03, 0.4, lambda a, X=X, v=v: (
            M.line(c, X, P.oy - 10, X, P.oy + 10, tinta, a, 4),
            rotulos and centro(c, fmt(v), X, P.oy + 14 + size, size, "b", tinta, a)), sobe=6)
    for i, v in enumerate(my):
        if abs(v) < 1e-12 and P.oy == P.y(0):
            continue
        Y = P.y(v)
        foco(c, t, t0 + 0.2 + i * 0.03, 0.4, lambda a, Y=Y, v=v: (
            M.line(c, P.ox - 10, Y, P.ox + 10, Y, tinta, a, 4),
            rotulos and escreve(c, fmt(v), P.ox - 22 - larg(fmt(v), "b", size), Y + size * 0.36, size, "b", tinta, a)), sobe=6)
    if zero and rotulos:
        foco(c, t, t0 + 0.2, 0.4, lambda a: escreve(c, "0", P.ox - 16 - larg("0", "b", size), P.oy + 14 + size, size, "b", tinta, a))
    return P


def ponto(c, t, t0, P, x, y, rotulo=None, guias=False, valores=False, cor=None, r=13, lado=(1, -1), size=48, d=0.5):
    """ponto (x, y) no plano P, com rótulo do lado (dx, dy) (1, −1 = acima à direita). guias = tracejado até os eixos;
    valores = escreve x e y na ponta das guias (para valor fora das marcas)"""
    cor = cor or COR
    tinta = "#FFFFFF" if P.escuro else TINTA
    X, Y = P(x, y)
    if guias and t >= t0:
        q = ep(t, t0 + 0.1, d)
        M.line(c, X, Y, X, P.oy, tinta, 0.75, 4, dash=TRACO, progress=q)
        M.line(c, X, Y, P.ox, Y, tinta, 0.75, 4, dash=TRACO, progress=q)
    if valores:
        foco(c, t, t0 + 0.3, 0.4, lambda a: (
            centro(c, _num(x), X, P.oy + (14 + size if y >= 0 else -24), size * 0.9, "g", COR_TEXTO, a),
            escreve(c, _num(y), P.ox - 22 - larg(_num(y), "g", size * 0.9), Y + size * 0.32, size * 0.9, "g", COR_TEXTO, a)))
    k = ease_back(prog(t, t0, 0.45))
    if k > 0:
        _ponto_px(c, X, Y, r * k, cor, 1.0)
    if rotulo:
        foco(c, t, t0 + 0.2, 0.4, lambda a: _cola(c, rotulo, X, Y, lado[0], lado[1], r + 8, size, "b", COR_TEXTO if not P.escuro else CLARO, a))
    return X, Y


def _avalia(f, x):
    try:
        v = f(x)
        if isinstance(v, complex) or v is None:
            return None
        v = float(v)
        return v if math.isfinite(v) else None
    except (ZeroDivisionError, ValueError, OverflowError, TypeError):
        return None


def _trechos(P, f, a, b, n):
    """amostra f em [a, b] e corta nos furos e assíntotas: sem valor, ou um salto de mais de uma tela entre duas amostras"""
    x, y, w, h = P.caixa
    trechos, atual, ant = [], [], None
    for i in range(n + 1):
        xv = a + (b - a) * i / n
        v = _avalia(f, xv)
        if v is None:
            if len(atual) > 1:
                trechos.append(atual)
            atual, ant = [], None
            continue
        py = P.y(v)
        if ant is not None:
            fora = (ant < y and py > y + h) or (ant > y + h and py < y)
            if fora or abs(py - ant) > h * 1.2:
                if len(atual) > 1:
                    trechos.append(atual)
                atual = []
        atual.append((P.x(xv), clamp(py, y - 2 * h, y + 3 * h), xv))
        ant = py
    if len(atual) > 1:
        trechos.append(atual)
    return trechos


def curva(c, t, t0, P, f, a=None, b=None, d=1.2, cor=None, largura=7, n=700, rotulo=None, em=None, size=52, tracejada=False):
    """gráfico de f no plano P, desenhado da esquerda para a direita em d segundos. Corta sozinho em assíntota e furo (1/x, tg x, log x).
    rotulo = nome da curva ("f(x) = x^2"), posto em `em` = (x, y) em valores (senão, perto do fim do traço)"""
    if t < t0:
        return
    cor = cor or COR
    a = P.xmin if a is None else a
    b = P.xmax if b is None else b
    p = ease_io(prog(t, t0, d))
    lim = a + (b - a) * p
    x, y, w, h = P.caixa
    c.save()
    c.clipRect(skia.Rect.MakeXYWH(x - 6, y - 6, w + 12, h + 12), True)
    pt = M.paint(cor, 1.0, stroke=largura, cap_round=True)
    pt.setStrokeJoin(skia.Paint.kRound_Join)
    if tracejada:
        pt.setPathEffect(skia.DashPathEffect.Make(TRACO, 0))
    ult = None
    for tr in _trechos(P, f, a, b, n):
        path, ok = skia.Path(), False
        for i, (px, py, xv) in enumerate(tr):
            if xv > lim + 1e-12:
                break
            path.lineTo(px, py) if ok else path.moveTo(px, py)
            ok = True
            if y - 2 <= py <= y + h + 2:
                ult = (px, py)
        if ok:
            c.drawPath(path, pt)
    c.restore()
    if rotulo:
        if em is not None:
            lx, ly = P(*em)
            foco(c, t, t0 + d * 0.8, 0.5, lambda q: _meio(c, rotulo, lx, ly, size, "b", COR_TEXTO if not P.escuro else CLARO, q))
        elif ult:
            lx, ly = ult
            foco(c, t, t0 + d * 0.8, 0.5, lambda q: _cola(c, rotulo, lx, ly, -1, 1 if ly < y + 80 else -1, 18, size, "b", COR_TEXTO if not P.escuro else CLARO, q))


def _corta_caixa(x0, y0, x1, y1, cx, cy, cw, ch):
    """recorte de um segmento numa caixa (Liang-Barsky); devolve None se ficar todo fora"""
    dx, dy = x1 - x0, y1 - y0
    u0, u1 = 0.0, 1.0
    for p_, q_ in ((-dx, x0 - cx), (dx, cx + cw - x0), (-dy, y0 - cy), (dy, cy + ch - y0)):
        if abs(p_) < 1e-12:
            if q_ < 0:
                return None
            continue
        r = q_ / p_
        if p_ < 0:
            u0 = max(u0, r)
        else:
            u1 = min(u1, r)
    if u0 > u1:
        return None
    return x0 + dx * u0, y0 + dy * u0, x0 + dx * u1, y0 + dy * u1


def reta_pontos(c, t, t0, P, A, B, cor=None, largura=7, pontos=True, rotulos=(None, None), rotulo=None, d=0.8, size=48):
    """reta que passa por A = (x1, y1) e B = (x2, y2), de borda a borda do plano; pontos = marca A e B (com rotulos).
    rotulo = nome da reta, perto da borda direita"""
    cor = cor or COR
    (ax, ay), (bx, by) = P(*A), P(*B)
    dx, dy = bx - ax, by - ay
    k = 1e4 / (math.hypot(dx, dy) or 1)
    x, y, w, h = P.caixa
    seg = _corta_caixa(ax - dx * k, ay - dy * k, ax + dx * k, ay + dy * k, x, y, w, h)
    if seg and t >= t0:
        x0, y0, x1, y1 = seg
        M.line(c, x0, y0, x1, y1, cor, 1.0, largura, progress=ease_io(prog(t, t0, d)))
        if rotulo:
            foco(c, t, t0 + d * 0.8, 0.4, lambda q: _cola(c, rotulo, x1, y1, -1, 1 if y1 < y + h / 2 else -1, 20, size, "b", COR_TEXTO if not P.escuro else CLARO, q))
    if pontos:
        for i, (pv, rot) in enumerate(zip((A, B), rotulos)):
            ponto(c, t, t0 + d * 0.5 + 0.15 * i, P, pv[0], pv[1], rot, cor=TINTA if not P.escuro else "#FFFFFF", r=12, lado=(1, 1) if dy < 0 and dx > 0 else (1, -1), size=size)


def area(c, t, t0, P, f, a, b, g=None, cor=None, alfa=0.24, d=0.8, n=300):
    """região entre f e g (ou o eixo x) de a até b, pintada da esquerda para a direita"""
    if t < t0:
        return
    cor = cor or COR
    g = g or (lambda x: 0.0)
    xs = [a + (b - a) * i / n for i in range(n + 1)]
    cima = [(P.x(v), P.y(_avalia(f, v) or 0.0)) for v in xs]
    baixo = [(P.x(v), P.y(_avalia(g, v) or 0.0)) for v in reversed(xs)]
    path = skia.Path()
    path.moveTo(*cima[0])
    for q in cima[1:] + baixo:
        path.lineTo(*q)
    path.close()
    x, y, w, h = P.caixa
    p = ease_io(prog(t, t0, d))
    c.save()
    c.clipRect(skia.Rect.MakeXYWH(x, y, w, h), True)
    c.clipRect(skia.Rect.MakeLTRB(P.x(a) - 1, y - 10, lerp(P.x(a), P.x(b), p) + 1, y + h + 10), True)
    c.drawPath(path, M.paint(cor, alfa))
    c.restore()


# ---------------- gráficos de dados ----------------
def _passo_bom(span, n=4):
    """passo redondo para ~n divisões"""
    bruto = span / n
    e = 10 ** math.floor(math.log10(bruto))
    for m in (1, 2, 2.5, 5, 10):
        if m * e >= bruto - 1e-12:
            return m * e
    return 10 * e


def _eixo_dados(c, t, t0, x, y, w, h, vmin, vmax, marcas, fmt, size, tinta, grade=True, eixo_y=True):
    """linha de base e, se pedido, eixo vertical com marcas e grade horizontal fina"""
    vy = lambda v: y + h - (v - vmin) / (vmax - vmin) * h
    if grade and t >= t0:
        for v in marcas:
            if v != vmin:
                M.line(c, x, vy(v), x + w, vy(v), FIO, ep(t, t0, 0.6), 2)
    if eixo_y:
        if t >= t0:
            M.line(c, x, y + h, x, y - 20, tinta, 1.0, 4, progress=ep(t, t0, 0.5))
        for i, v in enumerate(marcas):
            foco(c, t, t0 + 0.15 + i * 0.04, 0.4, lambda a, v=v: escreve(c, fmt(v), x - 20 - larg(fmt(v), "b", size), vy(v) + size * 0.36, size, "b", TINTA2, a), sobe=6)
    if t >= t0:
        M.line(c, x - (10 if eixo_y else 0), y + h, x + w, y + h, tinta, 1.0, 5, progress=ep(t, t0, 0.5))
    return vy


def colunas(c, t, t0, dados, x, y, w, h, vmax=None, cor=None, destaque=(), fmt=None, size=44, deitado=False, passo=0.12,
            valores=True, eixo_y=False, marcas=None, escuro=False, d=0.6):
    """gráfico de colunas (deitado=True: barras). dados = [(rótulo, valor[, cor])]; destaque = índices na cor da matéria, os outros em cinza
    (sem destaque, todas na cor da matéria). Cada coluna cresce no seu tempo e ganha o valor na ponta. Devolve o centro de cada coluna"""
    tinta = "#FFFFFF" if escuro else TINTA
    fmt = fmt or _num
    vmax = vmax or max(v for _, v, *_ in dados) * 1.12
    n = len(dados)
    cores = []
    for i, (_, _, *cc) in enumerate(dados):
        cores.append(cc[0] if cc else (cor or COR) if not destaque or i in destaque else mix(CINZA, PAPEL, 0.25))
    centros = []
    if not deitado:
        if marcas is None and eixo_y:
            marcas = _marcas(0, vmax, _passo_bom(vmax))
        vy = _eixo_dados(c, t, t0, x, y, w, h, 0, vmax, marcas or [], fmt, size, tinta, grade=eixo_y, eixo_y=eixo_y)
        slot = w / n
        bw = slot * 0.62
        for i, (rot, v, *_) in enumerate(dados):
            cx = x + slot * (i + 0.5)
            ti = t0 + 0.3 + i * passo
            q = ease_out(prog(t, ti, d))
            topo = lerp(y + h, vy(v), q)
            if q > 0:
                M.rrect(c, cx - bw / 2, topo, bw, y + h - topo, min(10, bw * 0.12), cores[i], 1.0)
                c.drawRect(skia.Rect.MakeXYWH(cx - bw / 2, y + h - 12, bw, 12), M.paint(cores[i]))
            foco(c, t, ti, 0.4, lambda a, rot=rot, cx=cx: _meio(c, rot, cx, y + h + 18 + size * 0.55, size, "b", tinta, a), sobe=6)
            if valores:
                foco(c, t, ti + d * 0.8, 0.4, lambda a, v=v, cx=cx, i=i: _meio(c, fmt(v), cx, vy(v) - 20 - size * 0.5, size * 1.1, "g", (COR_TEXTO if cores[i] == (cor or COR) else tinta) if not escuro else "#FFFFFF", a))
            centros.append((cx, vy(v)))
        return centros
    # barras deitadas: rótulo à esquerda de x, barras crescem para a direita até x + w
    if t >= t0:
        M.line(c, x, y - 10, x, y + h + 10, tinta, 1.0, 5, progress=ep(t, t0, 0.5))
    slot = h / n
    bh = slot * 0.62
    vx = lambda v: x + v / vmax * w
    for i, (rot, v, *_) in enumerate(dados):
        cy = y + slot * (i + 0.5)
        ti = t0 + 0.3 + i * passo
        q = ease_out(prog(t, ti, d))
        if q > 0:
            fim = lerp(x, vx(v), q)
            M.rrect(c, x, cy - bh / 2, fim - x, bh, min(10, bh * 0.12), cores[i], 1.0)
            c.drawRect(skia.Rect.MakeXYWH(x, cy - bh / 2, min(12, fim - x), bh), M.paint(cores[i]))
        foco(c, t, ti, 0.4, lambda a, rot=rot, cy=cy: formula(c, _num(rot), x - 24, cy + size * 0.36, size, _est(_num(rot), "b"), tinta, a, "right"), sobe=6)
        if valores:
            foco(c, t, ti + d * 0.8, 0.4, lambda a, v=v, cy=cy, i=i: escreve(c, fmt(v), vx(v) + 20, cy + size * 0.4, size * 1.1, "g", (COR_TEXTO if cores[i] == (cor or COR) else tinta) if not escuro else "#FFFFFF", a))
        centros.append((vx(v), cy))
    return centros


def serie(c, t, t0, dados, x, y, w, h, vmin=0, vmax=None, marcas=None, cor=None, fmt=None, size=40, pontos=True, valores=True,
          d=1.4, eixos=True, destaque=(), largura=7):
    """gráfico de linha (série no tempo). dados = [(rótulo do eixo x, valor)]; a linha cresce em d segundos e cada ponto acende quando
    ela chega. marcas = valores do eixo vertical (senão, redondos). Chame de novo com eixos=False para uma segunda série. Devolve os pontos"""
    cor = cor or COR
    fmt = fmt or _num
    vals = [v for _, v in dados]
    vmax = vmax if vmax is not None else max(vals) * 1.1
    if marcas is None:
        marcas = _marcas(vmin, vmax, _passo_bom(vmax - vmin))
    if eixos:
        vy = _eixo_dados(c, t, t0, x, y, w, h, vmin, vmax, marcas, fmt, size, TINTA)
    else:
        vy = lambda v: y + h - (v - vmin) / (vmax - vmin) * h
    n = len(dados)
    xs = [x + w * (i + 0.5) / n for i in range(n)]
    pts = [(xs[i], vy(v)) for i, v in enumerate(vals)]
    if eixos:
        for i, (rot, _) in enumerate(dados):
            foco(c, t, t0 + 0.2 + i * 0.04, 0.4, lambda a, rot=rot, i=i: _meio(c, rot, xs[i], y + h + 18 + size * 0.55, size, "b", TINTA, a), sobe=6)
    t1 = t0 + 0.5
    p = ease_io(prog(t, t1, d)) * (n - 1)
    if p > 0:
        path = skia.Path()
        path.moveTo(*pts[0])
        k = int(p)
        for i in range(1, min(k, n - 1) + 1):
            path.lineTo(*pts[i])
        if k < n - 1:
            f_ = p - k
            path.lineTo(lerp(pts[k][0], pts[k + 1][0], f_), lerp(pts[k][1], pts[k + 1][1], f_))
        pt = M.paint(cor, 1.0, stroke=largura, cap_round=True)
        pt.setStrokeJoin(skia.Paint.kRound_Join)
        c.drawPath(path, pt)
    for i, (px, py) in enumerate(pts):
        ti = t1 + d * (i / max(1, n - 1)) - 0.05
        if pontos:
            k_ = ease_back(prog(t, ti, 0.4))
            if k_ > 0:
                c.drawCircle(px, py, 13 * k_, M.paint(cor))
                c.drawCircle(px, py, 6 * k_, M.paint(PAPEL))
        if valores and (not destaque or i in destaque):
            acima = i == 0 or i == n - 1 or vals[i] >= (vals[i - 1] + vals[i + 1]) / 2
            foco(c, t, ti + 0.1, 0.4, lambda a, i=i, px=px, py=py, acima=acima: _meio(c, fmt(vals[i]), px, py + (-1 if acima else 1) * (26 + size * 0.5), size * 1.05, "g", COR_TEXTO if i in destaque or not destaque else TINTA, a), sobe=6)
    return pts


def _paleta(n, cor=None):
    """tons da cor da matéria, do forte ao claro, com o cinza para completar"""
    cor = cor or COR
    base = [cor, mix(cor, "#FFFFFF", 0.45), mix(cor, "#000000", 0.38), mix(cor, "#FFFFFF", 0.72), TINTA2, CINZA, mix(cor, "#FFFFFF", 0.25), "#B8B8BE"]
    return [base[i % len(base)] for i in range(n)]


def pizza(c, t, t0, dados, cx, cy, r, cores=None, pct=True, rosca=0.0, size=44, d=1.2, destaque=(), rotulos=True, casas=0):
    """gráfico de setores. dados = [(rótulo, valor)]; os setores giram a partir do alto, no sentido do relógio, e cada um ganha
    rótulo e porcentagem por fora. rosca = 0..0.8 abre o miolo; destaque = índices que saem um pouco do centro"""
    total = float(sum(v for _, v in dados))
    cores = cores or _paleta(len(dados))
    p = ease_io(prog(t, t0, d))
    ang = -90.0
    for i, (rot, v) in enumerate(dados):
        varre = 360.0 * v / total
        fim = min(ang + varre, -90 + 360 * p)
        meio = math.radians(ang + varre / 2)
        sai = 22 if i in destaque else 0
        ox, oy = math.cos(meio) * sai, math.sin(meio) * sai
        if fim > ang:
            path = skia.Path()
            ro = skia.Rect.MakeXYWH(cx + ox - r, cy + oy - r, 2 * r, 2 * r)
            if rosca > 0:
                ri = r * rosca
                path.arcTo(ro, ang, fim - ang, True)
                path.arcTo(skia.Rect.MakeXYWH(cx + ox - ri, cy + oy - ri, 2 * ri, 2 * ri), fim, ang - fim, False)
                path.close()
            else:
                path.moveTo(cx + ox, cy + oy)
                path.arcTo(ro, ang, fim - ang, False)
                path.close()
            c.drawPath(path, M.paint(cores[i]))
            sep = M.paint(PAPEL, 1.0, stroke=5)
            sep.setStrokeJoin(skia.Paint.kRound_Join)
            c.drawPath(path, sep)
        ti = t0 + d * ((ang + varre / 2 + 90) / 360) + 0.1
        if rotulos:
            ux, uy = math.cos(meio), math.sin(meio)
            px, py = cx + ox + ux * (r + 28), cy + oy + uy * (r + 28)
            porc = 100 * v / total
            ps = (f"{porc:.{casas}f}".replace(".", ",") if casas else str(round(porc))) + "%"
            w1 = max(_mede(rot, size, "b")[0], larg(ps, "g", size * 1.2))
            k = min(abs(ux) * w1 / 2, w1 / 2) + abs(uy) * size * 0.95
            lx, ly = px + ux * k, py + uy * k
            foco(c, t, ti, 0.45, lambda a, lx=lx, ly=ly, rot=rot, ps=ps, i=i: (
                _meio(c, rot, lx, ly - size * 0.62, size, "b", TINTA, a),
                pct and _meio(c, ps, lx, ly + size * 0.62, size * 1.2, "g", cores[i] if M.lum(cores[i]) < 0.4 else mix(cores[i], "#000000", 0.4), a)), sobe=6)
        ang += varre


def histograma(c, t, t0, limites, freqs, x, y, w, h, vmax=None, marcas=None, cor=None, fmt=None, size=40, valores=True,
               passo=0.1, poligono=False, d=0.5, destaque=()):
    """histograma: classes coladas, limites = [0, 10, 20, 30] (um a mais que freqs). Rótulos nos limites.
    poligono = polígono de frequências: abre meia classe de cada lado e põe as frequências dentro das colunas"""
    assert len(limites) == len(freqs) + 1, (limites, freqs)
    cor = cor or COR
    fmt = fmt or _num
    vmax = vmax or max(freqs) * 1.15
    if marcas is None:
        marcas = _marcas(0, vmax, _passo_bom(vmax))
    vy = _eixo_dados(c, t, t0, x, y, w, h, 0, vmax, marcas, fmt, size, TINTA)
    lo, hi = limites[0], limites[-1]
    folga = w / (len(freqs) + 1) / 2 if poligono else 0.0
    vx = lambda v: x + folga + (v - lo) / (hi - lo) * (w - 2 * folga)
    for i, v in enumerate(limites):
        foco(c, t, t0 + 0.2 + i * 0.04, 0.4, lambda a, v=v: (M.line(c, vx(v), y + h, vx(v), y + h + 14, TINTA, a, 4),
                                                         centro(c, fmt(v), vx(v), y + h + 24 + size, size, "b", TINTA, a)), sobe=6)
    meios = []
    for i, f_ in enumerate(freqs):
        x0, x1 = vx(limites[i]), vx(limites[i + 1])
        ti = t0 + 0.3 + i * passo
        q = ease_out(prog(t, ti, d))
        cr = cor if not destaque or i in destaque else mix(CINZA, PAPEL, 0.25)
        if q > 0:
            topo = lerp(y + h, vy(f_), q)
            c.drawRect(skia.Rect.MakeLTRB(x0, topo, x1, y + h), M.paint(cr))
            c.drawRect(skia.Rect.MakeLTRB(x0, topo, x1, y + h), M.paint(PAPEL, 1.0, stroke=4))
        if valores:
            dentro = poligono and (y + h - vy(f_)) > size * 2.4
            yv = vy(f_) + 30 + size * 0.55 if dentro else vy(f_) - 18 - size * 0.5
            cv = M.on(cr) if dentro else COR_TEXTO if cr == cor else TINTA2
            foco(c, t, ti + d * 0.8, 0.4, lambda a, f_=f_, x0=x0, x1=x1, yv=yv, cv=cv: _meio(c, fmt(f_), (x0 + x1) / 2, yv, size * 1.05, "g", cv, a), sobe=6)
        meios.append(((x0 + x1) / 2, vy(f_)))
    if poligono:
        tp = t0 + 0.3 + len(freqs) * passo + d
        pts = [(vx(lo) - (meios[0][0] - vx(lo)), y + h)] + meios + [(vx(hi) + (vx(hi) - meios[-1][0]), y + h)]
        q = ease_io(prog(t, tp, 1.0)) * (len(pts) - 1)
        for i in range(len(pts) - 1):
            f_ = clamp(q - i)
            if f_ > 0:
                M.line(c, *pts[i], *pts[i + 1], TINTA, 1.0, 6, progress=f_)
        for i, (px, py) in enumerate(pts):
            if t >= tp and q >= i:
                c.drawCircle(px, py, 10, M.paint(TINTA))
    return meios


# ---------------- geometria plana ----------------
def marcas_iguais(c, A, B, n=1, cor=None, a=1.0, tam=18, largura=5):
    """n tracinhos no meio do lado AB: lados com o mesmo número de tracinhos são iguais"""
    if a <= 0 or n <= 0:
        return
    ux, uy = _uni(*A, *B)
    mx, my = (A[0] + B[0]) / 2, (A[1] + B[1]) / 2
    for k in range(n):
        off = (k - (n - 1) / 2) * 12
        px, py = mx + ux * off, my + uy * off
        M.line(c, px - uy * tam, py + ux * tam, px + uy * tam, py - ux * tam, cor or TINTA, a, largura)


def segmento(c, t, t0, A, B, medida=None, rotulos=None, cor=None, lado=1, afasta=26, largura=6, pontas=True, tracejado=False,
             size=48, d=0.6, cota=False):
    """segmento de A até B que cresce em d segundos, com a medida ao lado (lado = 1 ou −1 escolhe o lado) e os nomes nas pontas.
    cota = linha de cota com tracinhos, afastada do segmento, como em desenho técnico"""
    cor = cor or TINTA
    ux, uy = _uni(*A, *B)
    nx, ny = uy * lado, -ux * lado
    if t >= t0:
        M.line(c, *A, *B, cor, 1.0, largura, dash=TRACO if tracejado else None, progress=ease_io(prog(t, t0, d)))
    if pontas:
        for i, P_ in enumerate((A, B)):
            k = ease_back(prog(t, t0 + (0 if i == 0 else d * 0.9), 0.35))
            if k > 0:
                c.drawCircle(P_[0], P_[1], 10 * k, M.paint(cor))
    if rotulos:
        for i, (P_, s) in enumerate(zip((A, B), rotulos)):
            sx, sy = (-ux, -uy) if i == 0 else (ux, uy)
            foco(c, t, t0 + d * 0.6, 0.4, lambda a, P_=P_, s=s, sx=sx, sy=sy: _cola(c, s, P_[0], P_[1], sx, sy, 18, size, "b", TINTA, a))
    if medida is not None:
        mx, my = (A[0] + B[0]) / 2, (A[1] + B[1]) / 2
        if cota:
            off = afasta + 20
            a0 = (A[0] + nx * off, A[1] + ny * off)
            b0 = (B[0] + nx * off, B[1] + ny * off)
            q = ep(t, t0 + d * 0.7, 0.5)
            if q > 0:
                M.line(c, *a0, *b0, TINTA2, q, 3)
                for P_ in (a0, b0):
                    M.line(c, P_[0] - nx * 14, P_[1] - ny * 14, P_[0] + nx * 14, P_[1] + ny * 14, TINTA2, q, 3)
            mx, my = mx + nx * off, my + ny * off
            foco(c, t, t0 + d * 0.7, 0.4, lambda a: _cola(c, medida, mx, my, nx, ny, 12, size, "b", COR_TEXTO, a))
        else:
            foco(c, t, t0 + d * 0.7, 0.4, lambda a: _cola(c, medida, mx, my, nx, ny, afasta, size, "b", COR_TEXTO, a))


def angulo(c, t, t0, V, A, B, rotulo=None, r=64, cor=None, reto=None, preenche=0.2, largura=5, size=46, d=0.5, afasta=14, dentro=False):
    """ângulo AVB: arco do lado de VA até o lado de VB (o menor dos dois) com rótulo na bissetriz. reto=None reconhece 90° e
    desenha o quadradinho; dentro=True põe o rótulo dentro do arco (ângulo grande)"""
    if t < t0:
        return
    cor = cor or COR
    a1 = math.degrees(math.atan2(A[1] - V[1], A[0] - V[0]))
    a2 = math.degrees(math.atan2(B[1] - V[1], B[0] - V[0]))
    varre = (a2 - a1 + 180) % 360 - 180
    if reto is None:
        reto = abs(abs(varre) - 90) < 0.6
    p = ease_out(prog(t, t0, d))
    bis = math.radians(a1 + varre / 2)
    bx, by = math.cos(bis), math.sin(bis)
    if reto:
        s = r * 0.62
        u1 = (math.cos(math.radians(a1)), math.sin(math.radians(a1)))
        u2 = (math.cos(math.radians(a2)), math.sin(math.radians(a2)))
        q1 = (V[0] + u1[0] * s, V[1] + u1[1] * s)
        q2 = (V[0] + u2[0] * s, V[1] + u2[1] * s)
        qm = (q1[0] + u2[0] * s, q1[1] + u2[1] * s)
        path = skia.Path()
        path.moveTo(*V); path.lineTo(*q1); path.lineTo(*qm); path.lineTo(*q2); path.close()
        c.drawPath(path, M.paint(cor, preenche * p))
        pt = M.paint(cor, p, stroke=largura)
        pt.setStrokeJoin(skia.Paint.kRound_Join)
        borda = skia.Path()
        borda.moveTo(*q1); borda.lineTo(*qm); borda.lineTo(*q2)
        c.drawPath(borda, pt)
        c.drawCircle(V[0] + bx * s * 0.62, V[1] + by * s * 0.62, max(3.5, largura * 0.8), M.paint(cor, p))
        ralo = s * 1.41
    else:
        ret = skia.Rect.MakeXYWH(V[0] - r, V[1] - r, 2 * r, 2 * r)
        if preenche > 0:
            path = skia.Path()
            path.moveTo(*V); path.arcTo(ret, a1, varre * p, False); path.close()
            c.drawPath(path, M.paint(cor, preenche))
        c.drawArc(ret, a1, varre * p, False, M.paint(cor, 1.0, stroke=largura, cap_round=True))
        ralo = r
    if rotulo:
        cr = COR_TEXTO if cor == COR else cor
        if dentro:
            foco(c, t, t0 + d * 0.7, 0.4, lambda a: _meio(c, rotulo, V[0] + bx * ralo * 0.58, V[1] + by * ralo * 0.58, size, "b", cr, a))
        else:
            w_, hh = _mede(_num(rotulo), size, "b")
            dist = ralo + afasta + min(abs(bx) * w_ / 2 + abs(by) * hh, math.hypot(w_ / 2, hh))
            meia = math.radians(abs(varre) / 2)
            if meia < math.radians(80):  # ângulo estreito: o rótulo se afasta até não tocar nenhum dos dois lados
                for a_ in (a1, a2):
                    nx_, ny_ = -math.sin(math.radians(a_)), math.cos(math.radians(a_))
                    dist = max(dist, (abs(nx_) * w_ / 2 + abs(ny_) * hh + 10) / max(0.15, math.sin(meia)))
            foco(c, t, t0 + d * 0.7, 0.4, lambda a: _meio(c, rotulo, V[0] + bx * dist, V[1] + by * dist, size, "b", cr, a))


def _contorno(c, pts, p, cor, largura, fecha=True, dash=None):
    """contorno que se desenha em volta, p = 0..1 do perímetro"""
    if p <= 0:
        return
    lados = list(zip(pts, pts[1:] + (pts[:1] if fecha else [])))
    comp = [math.dist(a, b) for a, b in lados]
    alvo = sum(comp) * p
    path = skia.Path()
    path.moveTo(*pts[0])
    for (a, b), L in zip(lados, comp):
        if alvo >= L:
            path.lineTo(*b)
            alvo -= L
        else:
            f_ = alvo / L if L else 0
            path.lineTo(lerp(a[0], b[0], f_), lerp(a[1], b[1], f_))
            break
    else:
        if fecha:
            path.close()
    pt = M.paint(cor, 1.0, stroke=largura, cap_round=True)
    pt.setStrokeJoin(skia.Paint.kRound_Join)
    if dash:
        pt.setPathEffect(skia.DashPathEffect.Make(dash, 0))
    c.drawPath(path, pt)


def poligono(c, t, t0, pts, vertices=None, lados=None, angulos=None, iguais=None, retos=(), cor=None, preenche=0.1, largura=6,
             size=50, d=0.9, tl=None, ta=None, tv=None, r_ang=None, escuro=False):
    """polígono pelos pontos, desenhado em volta em d segundos. vertices = nomes; lados = medida de cada lado (lado i vai de pts[i] a pts[i+1]);
    angulos = rótulo de cada vértice (None = sem arco); iguais = tracinhos de cada lado; retos = vértices com quadradinho.
    tv, tl, ta = instantes dos nomes, das medidas e dos ângulos (senão, em fila depois do contorno). Devolve os pontos"""
    pts = [tuple(p_) for p_ in pts]
    n = len(pts)
    tinta = "#FFFFFF" if escuro else TINTA
    cor_f = cor or COR
    gx, gy = sum(p_[0] for p_ in pts) / n, sum(p_[1] for p_ in pts) / n
    if preenche > 0 and t >= t0:
        path = skia.Path()
        path.addPoly(pts, True)
        c.drawPath(path, M.paint(cor_f, preenche * ep(t, t0 + d * 0.6, 0.5)))
    if t >= t0:
        _contorno(c, pts, ease_io(prog(t, t0, d)), tinta, largura)
    lado_min = min(math.dist(pts[i], pts[(i + 1) % n]) for i in range(n))
    for i in range(n):
        V, ant, prox = pts[i], pts[i - 1], pts[(i + 1) % n]
        ang_ = (angulos[i] if angulos and i < len(angulos) else None)
        if ang_ is not None or i in retos:
            ti = ta[i] if ta else t0 + d + 0.3 + 0.12 * i
            angulo(c, t, ti, V, ant, prox, ang_ if ang_ != "" else None, r=r_ang or min(70, lado_min * 0.3), cor=cor, reto=True if i in retos else None)
    for i in range(n):
        A, B = pts[i], pts[(i + 1) % n]
        if iguais and i < len(iguais) and iguais[i]:
            q = ep(t, (tl[i] if tl else t0 + d + 0.1 * i), 0.4)
            marcas_iguais(c, A, B, iguais[i], tinta, q)
        if lados and i < len(lados) and lados[i] is not None:
            ux, uy = _uni(*A, *B)
            nx, ny = uy, -ux
            mx, my = (A[0] + B[0]) / 2, (A[1] + B[1]) / 2
            if (mx + nx - gx) ** 2 + (my + ny - gy) ** 2 < (mx - gx) ** 2 + (my - gy) ** 2:
                nx, ny = -nx, -ny
            ti = tl[i] if tl else t0 + d + 0.1 * i
            foco(c, t, ti, 0.4, lambda a, s=lados[i], mx=mx, my=my, nx=nx, ny=ny: _cola(c, s, mx, my, nx, ny, 20, size * 0.94, "b", COR_TEXTO if not escuro else CLARO, a))
    if vertices:
        for i, s in enumerate(vertices):
            if not s:
                continue
            V, ant, prox = pts[i], pts[i - 1], pts[(i + 1) % n]
            u1, u2 = _uni(*V, *ant), _uni(*V, *prox)
            ox, oy = -(u1[0] + u2[0]), -(u1[1] + u2[1])
            if math.hypot(ox, oy) < 1e-6:
                ox, oy = V[0] - gx, V[1] - gy
            if (ox * (V[0] - gx) + oy * (V[1] - gy)) < 0:  # vértice côncavo: o rótulo vai para fora mesmo assim
                ox, oy = -ox, -oy
            ti = tv[i] if tv else t0 + d * 0.4 + 0.1 * i
            foco(c, t, ti, 0.4, lambda a, s=s, V=V, ox=ox, oy=oy: _cola(c, s, V[0], V[1], ox, oy, 14, size, "g", tinta, a))
    return pts


def triangulo(c, t, t0, A, B, C, vertices=("A", "B", "C"), **kw):
    """triângulo ABC: lados[0] = AB, lados[1] = BC, lados[2] = CA; angulos na ordem dos vértices. Os outros parâmetros são os de E.poligono"""
    return poligono(c, t, t0, [A, B, C], vertices, **kw)


def regular(c, t, t0, n, cx, cy, r, vertices=None, lado=None, raio=None, apotema=None, giro=0.0, mostra_centro=None, **kw):
    """polígono regular de n lados com um lado deitado embaixo; lado = medida escrita no lado de baixo;
    raio e apotema = rótulos (desenham o segmento do centro). giro em graus. Os outros parâmetros são os de E.poligono"""
    ini = 90 - 180 / n + giro
    pts = [(cx + r * math.cos(math.radians(ini + k * 360 / n)), cy + r * math.sin(math.radians(ini + k * 360 / n))) for k in range(n)]
    d = kw.get("d", 0.9)
    lados = [lado] + [None] * (n - 1) if lado is not None else kw.pop("lados", None)
    poligono(c, t, t0, pts, vertices, lados=lados, **kw)
    t1 = t0 + d + 0.4
    if mostra_centro or raio or apotema:
        k = ease_back(prog(t, t1, 0.35))
        if k > 0:
            c.drawCircle(cx, cy, 9 * k, M.paint(TINTA))
    if raio:
        V = pts[n // 2]
        segmento(c, t, t1 + 0.2, (cx, cy), V, raio, cor=TINTA2, pontas=False, tracejado=True, largura=5, lado=1, size=kw.get("size", 50) * 0.94)
    if apotema:
        mx, my = (pts[0][0] + pts[1][0]) / 2, (pts[0][1] + pts[1][1]) / 2
        segmento(c, t, t1 + 0.5, (cx, cy), (mx, my), None, cor=COR_TEXTO, pontas=False, tracejado=True, largura=5)
        angulo(c, t, t1 + 0.8, (mx, my), (cx, cy), pts[1], r=34, reto=True, preenche=0.0)
        foco(c, t, t1 + 0.8, 0.4, lambda a: _cola(c, apotema, (cx + mx) / 2, (cy + my) / 2, -1, 0, 16, kw.get("size", 50) * 0.94, "b", COR_TEXTO, a))
    return pts


def retangulo(c, t, t0, x, y, w, h, base=None, altura=None, vertices=None, **kw):
    """retângulo (x, y = canto de cima à esquerda) com a base escrita embaixo e a altura à esquerda. Vértices na ordem:
    embaixo à esquerda, embaixo à direita, em cima à direita, em cima à esquerda. Os outros parâmetros são os de E.poligono"""
    pts = [(x, y + h), (x + w, y + h), (x + w, y), (x, y)]
    return poligono(c, t, t0, pts, vertices, lados=kw.pop("lados", [base, None, None, altura]), **kw)


def quadrado(c, t, t0, x, y, l, lado=None, vertices=None, **kw):
    """quadrado de lado l (px) com a medida embaixo e os tracinhos de lados iguais"""
    kw.setdefault("iguais", [1, 1, 1, 1])
    kw.setdefault("retos", (0,))
    return retangulo(c, t, t0, x, y, l, l, lado, None, vertices, **kw)


def _altura(c, t, t0, topo, pe, rotulo, lado=1, size=48, cor=None):
    """altura tracejada de topo até pe, com o quadradinho e o rótulo do lado (1 = direita)"""
    segmento(c, t, t0, topo, pe, None, cor=cor or TINTA2, pontas=False, tracejado=True, largura=5)
    angulo(c, t, t0 + 0.3, pe, topo, (pe[0] + lado * 50, pe[1]), r=40, reto=True, preenche=0.0)
    foco(c, t, t0 + 0.4, 0.4, lambda a: _cola(c, rotulo, pe[0], (topo[1] + pe[1]) / 2, lado, 0, 16, size, "b", COR_TEXTO, a))


def paralelogramo(c, t, t0, x, y, w, h, desloca, base=None, altura=None, lado=None, vertices=None, **kw):
    """paralelogramo: base w embaixo, de (x, y + h); o lado de cima começa desloca px à direita. altura = rótulo da altura
    tracejada (do vértice de cima à esquerda); lado = medida do lado inclinado da direita"""
    pts = [(x, y + h), (x + w, y + h), (x + w + desloca, y), (x + desloca, y)]
    d = kw.get("d", 0.9)
    poligono(c, t, t0, pts, vertices, lados=kw.pop("lados", [base, lado, None, None]), **kw)
    if altura:
        _altura(c, t, t0 + d + 0.4, pts[3], (x + desloca, y + h), altura, 1, kw.get("size", 50) * 0.94)
    return pts


def trapezio(c, t, t0, x, y, B, b, h, desloca=None, base_maior=None, base_menor=None, altura=None, vertices=None, **kw):
    """trapézio: base maior B embaixo, de (x, y + h); base menor b em cima, desloca px à direita (sem desloca: isósceles)"""
    desloca = (B - b) / 2 if desloca is None else desloca
    pts = [(x, y + h), (x + B, y + h), (x + desloca + b, y), (x + desloca, y)]
    d = kw.get("d", 0.9)
    poligono(c, t, t0, pts, vertices, lados=kw.pop("lados", [base_maior, None, base_menor, None]), **kw)
    if altura:
        _altura(c, t, t0 + d + 0.4, pts[3], (x + desloca, y + h), altura, 1, kw.get("size", 50) * 0.94)
    return pts


def _no_circ(cx, cy, r, ang):
    """ponto do círculo no ângulo ang (graus, anti-horário a partir da direita, como na matemática)"""
    return cx + r * math.cos(math.radians(ang)), cy - r * math.sin(math.radians(ang))


def circulo(c, t, t0, cx, cy, r, o="O", raio=None, diametro=None, corda=None, setor=None, arco=None, cor=None, preenche=0.0,
            size=50, d=0.8, te=None, largura=6):
    """circunferência que se fecha em d segundos, com centro o. Ângulos em graus, anti-horário a partir da direita:
    raio = (ângulo, rótulo); diametro = (ângulo, rótulo); corda = (a1, a2, rótulo); setor = (a1, a2, rótulo do ângulo) pintado;
    arco = (a1, a2, rótulo) em destaque, de a1 até a2 no sentido anti-horário.
    te = {"raio": t, "diametro": t, ...} instantes de cada peça (senão, em fila)"""
    cor = cor or COR
    te = te or {}
    fila = [k for k, v in (("setor", setor), ("raio", raio), ("diametro", diametro), ("corda", corda), ("arco", arco)) if v]
    quando = {k: te.get(k, t0 + d + 0.2 + 0.5 * i) for i, k in enumerate(fila)}
    ret = skia.Rect.MakeXYWH(cx - r, cy - r, 2 * r, 2 * r)
    if setor:
        a1, a2, rot = setor
        q = ease_io(prog(t, quando["setor"], 0.7))
        if q > 0:
            varre = ((a2 - a1) % 360) * q
            path = skia.Path()
            path.moveTo(cx, cy); path.arcTo(ret, -a1, -varre, False); path.close()
            c.drawPath(path, M.paint(cor, 0.22))
            pt = M.paint(cor, 1.0, stroke=largura - 1)
            pt.setStrokeJoin(skia.Paint.kRound_Join)
            c.drawPath(path, pt)
            if rot:
                bis = a1 + (a2 - a1) % 360 / 2
                ra = min(90, r * 0.32)
                c.drawArc(skia.Rect.MakeXYWH(cx - ra, cy - ra, 2 * ra, 2 * ra), -a1, -varre, False, M.paint(cor, 1.0, stroke=5))
                foco(c, t, quando["setor"] + 0.5, 0.4, lambda a: _cola(c, rot, *_no_circ(cx, cy, ra, bis), math.cos(math.radians(bis)), -math.sin(math.radians(bis)), 14, size, "b", COR_TEXTO, a))
    if preenche > 0 and t >= t0:
        c.drawCircle(cx, cy, r, M.paint(cor, preenche * ep(t, t0 + d * 0.6, 0.5)))
    if t >= t0:
        c.drawArc(ret, 0, -360 * ease_io(prog(t, t0, d)), False, M.paint(TINTA, 1.0, stroke=largura, cap_round=True))
    if arco:
        a1, a2, rot = arco
        q = ease_io(prog(t, quando["arco"], 0.6))
        if q > 0:
            varre = (a2 - a1) % 360
            c.drawArc(ret, -a1, -varre * q, False, M.paint(cor, 1.0, stroke=largura + 8, cap_round=True))
            meio = a1 + varre / 2
            foco(c, t, quando["arco"] + 0.4, 0.4, lambda a: _cola(c, rot, *_no_circ(cx, cy, r + largura, meio), math.cos(math.radians(meio)), -math.sin(math.radians(meio)), 16, size, "b", COR_TEXTO, a))
    if diametro:
        ang, rot = diametro
        P1, P2 = _no_circ(cx, cy, r, ang + 180), _no_circ(cx, cy, r, ang)
        segmento(c, t, quando["diametro"], P1, P2, None, cor=COR_TEXTO, pontas=True, largura=6)
        nx, ny = -math.sin(math.radians(ang)), -math.cos(math.radians(ang))  # normal "para cima" na tela
        mx, my = (P1[0] * 0.25 + P2[0] * 0.75), (P1[1] * 0.25 + P2[1] * 0.75)
        foco(c, t, quando["diametro"] + 0.4, 0.4, lambda a: _cola(c, rot, mx, my, nx, ny, 16, size, "b", COR_TEXTO, a))
    if raio:
        ang, rot = raio
        P1 = _no_circ(cx, cy, r, ang)
        segmento(c, t, quando["raio"], (cx, cy), P1, None, cor=COR_TEXTO, pontas=False, largura=6)
        k = ease_back(prog(t, quando["raio"] + 0.5, 0.35))
        if k > 0:
            c.drawCircle(*P1, 10 * k, M.paint(COR_TEXTO))
        nx, ny = -math.sin(math.radians(ang)), -math.cos(math.radians(ang))
        if ny > 0.2:
            nx, ny = -nx, -ny
        mx, my = (cx + P1[0]) / 2, (cy + P1[1]) / 2
        foco(c, t, quando["raio"] + 0.4, 0.4, lambda a: _cola(c, rot, mx, my, nx, ny, 16, size, "b", COR_TEXTO, a))
    if corda:
        a1, a2, rot = corda
        P1, P2 = _no_circ(cx, cy, r, a1), _no_circ(cx, cy, r, a2)
        segmento(c, t, quando["corda"], P1, P2, None, cor=TINTA2, pontas=True, largura=6)
        mx, my = (P1[0] + P2[0]) / 2, (P1[1] + P2[1]) / 2
        foco(c, t, quando["corda"] + 0.4, 0.4, lambda a: _cola(c, rot, mx, my, cx - mx, cy - my, 14, size, "b", TINTA2, a))
    k = ease_back(prog(t, t0 + d * 0.5, 0.35))
    if k > 0:
        c.drawCircle(cx, cy, 10 * k, M.paint(TINTA))
    if o:
        foco(c, t, t0 + d * 0.5, 0.4, lambda a: _cola(c, o, cx, cy, -0.7, 1, 20, size, "g", TINTA, a))


def paralelas(c, t, t0, cx, cy, w=1100, gap=300, inclina=60, angulos=None, nomes=("r", "s", "t"), cores=None, size=50, d=0.7, ta=None, r_ang=62):
    """duas paralelas (r em cima, s embaixo) cortadas pela transversal t, que passa por (cx, cy) com inclinação `inclina` (graus).
    angulos = {k: rótulo}, k de 1 a 8: 1 a 4 no cruzamento de cima, 5 a 8 no de baixo, na ordem acima à direita, acima à esquerda,
    abaixo à esquerda, abaixo à direita. cores = {k: cor}; ta = {k: instante}"""
    angulos, cores, ta = angulos or {}, cores or {}, ta or {}
    y1, y2 = cy - gap / 2, cy + gap / 2
    k_ = 1 / math.tan(math.radians(inclina))
    P1 = (cx + gap / 2 * k_, y1)
    P2 = (cx - gap / 2 * k_, y2)
    if t >= t0:
        for i, yy in enumerate((y1, y2)):
            M.line(c, cx - w / 2, yy, cx + w / 2, yy, TINTA, 1.0, 6, progress=ease_io(prog(t, t0 + 0.15 * i, d)))
        ux, uy = math.cos(math.radians(inclina)), -math.sin(math.radians(inclina))
        M.line(c, P2[0] - ux * 130, P2[1] - uy * 130, P1[0] + ux * 130, P1[1] + uy * 130, TINTA2, 1.0, 6,
               progress=ease_io(prog(t, t0 + 0.4, d)))
        # setinhas de paralela
        q = ep(t, t0 + d, 0.4)
        for yy in (y1, y2):
            xm = cx + w * 0.36
            M.line(c, xm - 14, yy - 16, xm + 6, yy, TINTA, q, 5)
            M.line(c, xm - 14, yy + 16, xm + 6, yy, TINTA, q, 5)
    ux, uy = math.cos(math.radians(inclina)), -math.sin(math.radians(inclina))
    for i, (s, x_, y_) in enumerate(((nomes[0], cx + w / 2 + 20, y1), (nomes[1], cx + w / 2 + 20, y2))):
        foco(c, t, t0 + d * 0.8, 0.4, lambda a, s=s, x_=x_, y_=y_: escreve(c, s, x_, y_ + 20, 64, "i", TINTA, a))
    foco(c, t, t0 + d + 0.3, 0.4, lambda a: _cola(c, nomes[2], P1[0] + ux * 130, P1[1] + uy * 130, 1, 0, 14, 64, "i", TINTA2, a))
    raios = (0, inclina, 180, 180 + inclina)
    for k, rot in sorted(angulos.items()):
        V = P1 if k <= 4 else P2
        j = (k - 1) % 4
        a1, a2 = raios[j], raios[(j + 1) % 4] if j < 3 else 360
        A = _no_circ(V[0], V[1], 10, a1)
        B = _no_circ(V[0], V[1], 10, a2)
        angulo(c, t, ta.get(k, t0 + d + 0.5 + 0.15 * k), V, A, B, rot, r=r_ang, cor=cores.get(k), size=size)
    return P1, P2


# ---------------- geometria espacial: perspectiva simples, arestas ocultas tracejadas ----------------
def _vista_obliqua(k=0.5, ang=38):
    """perspectiva cavaleira: a frente fica em verdadeira grandeza, a profundidade sobe para a direita"""
    kc, ks = k * math.cos(math.radians(ang)), k * math.sin(math.radians(ang))
    return (1, 0, kc), (0, 1, ks), (kc, ks, -1)  # direita, cima, de onde se olha (z = profundidade)


def _vista_alta(giro=-24, inclina=22):
    """vista de cima e de lado (ortogonal): bases viram elipses deitadas"""
    g, p = math.radians(giro), math.radians(inclina)
    v = (math.sin(g) * math.cos(p), math.sin(p), math.cos(g) * math.cos(p))
    R = (math.cos(g), 0, -math.sin(g))
    U = (v[1] * R[2] - v[2] * R[1], v[2] * R[0] - v[0] * R[2], v[0] * R[1] - v[1] * R[0])
    return R, U, v


def _proj(P, R, U, ox, oy):
    return ox + sum(a * b for a, b in zip(P, R)), oy - sum(a * b for a, b in zip(P, U))


def _solido(c, t, t0, verts, faces, vista, ox, oy, cor=None, preenche=0.14, largura=6, d=1.0, escuro=False):
    """sólido convexo: verts 3D, faces = listas de índices. Arestas que só tocam faces de costas saem tracejadas. Devolve os pontos na tela"""
    R, U, v = vista
    tinta = "#FFFFFF" if escuro else TINTA
    cor = cor or COR
    pts = [_proj(P, R, U, ox, oy) for P in verts]
    g = [sum(P[i] for P in verts) / len(verts) for i in range(3)]
    vis = []
    for f in faces:
        a, b, c_ = (verts[f[0]], verts[f[1]], verts[f[2]])
        u1 = [b[i] - a[i] for i in range(3)]
        u2 = [c_[i] - a[i] for i in range(3)]
        n = (u1[1] * u2[2] - u1[2] * u2[1], u1[2] * u2[0] - u1[0] * u2[2], u1[0] * u2[1] - u1[1] * u2[0])
        fc = [sum(verts[i][k] for i in f) / len(f) for k in range(3)]
        if sum(n[k] * (fc[k] - g[k]) for k in range(3)) < 0:
            n = tuple(-x for x in n)
        nn = math.sqrt(sum(x * x for x in n)) or 1
        vis.append((sum(n[k] * v[k] for k in range(3)) / nn, n))
    q = ep(t, t0 + d * 0.5, 0.6)
    if preenche > 0 and q > 0:
        for f, (dv, n) in zip(faces, vis):
            if dv > 1e-6:
                nn = math.sqrt(sum(x * x for x in n)) or 1
                luz = 0.55 + 0.45 * max(0.0, (n[1] * 0.8 + n[0] * -0.3) / nn)  # o topo mais claro, a frente mais escura
                path = skia.Path()
                path.addPoly([pts[i] for i in f], True)
                c.drawPath(path, M.paint(mix(cor, "#FFFFFF", 1 - luz * 0.5), preenche * q * 2.2))
    arestas, sentido = {}, {}
    for fi, f in enumerate(faces):
        for i in range(len(f)):
            e = tuple(sorted((f[i], f[(i + 1) % len(f)])))
            arestas.setdefault(e, []).append(fi)
            sentido.setdefault(e, (f[i], f[(i + 1) % len(f)]))
    p = prog(t, t0, d)
    N = len(arestas)
    ocultas, visiveis = [], []
    for k, (e, fs) in enumerate(arestas.items()):
        q_ = ease_io(clamp((p - 0.6 * k / N) / 0.4))  # uma aresta puxa a outra, como quem desenha
        (ocultas if all(vis[fi][0] <= 1e-6 for fi in fs) else visiveis).append((sentido[e], q_))
    for (i, j), q_ in ocultas:
        M.line(c, *pts[i], *pts[j], tinta, 0.55, largura - 2, dash=TRACO, progress=q_)
    for (i, j), q_ in visiveis:
        M.line(c, *pts[i], *pts[j], tinta, 1.0, largura, progress=q_)
    return pts


def _medida_aresta(c, t, t0, A, B, s, lado, size, cor=None, gap=18, longe=None):
    """rótulo de aresta: do lado (nx, ny) indicado; longe = ponto do qual o rótulo foge"""
    if not s:
        return
    mx, my = (A[0] + B[0]) / 2, (A[1] + B[1]) / 2
    nx, ny = lado
    foco(c, t, t0, 0.4, lambda a: _cola(c, s, mx, my, nx, ny, gap, size, "b", cor or COR_TEXTO, a))


def paralelepipedo(c, t, t0, x, y, a, b, h, medidas=(None, None, None), cor=None, preenche=0.14, size=48, d=1.0, vertices=None, tm=None, **kw):
    """paralelepípedo em perspectiva cavaleira: (x, y) = canto de baixo à esquerda da frente; a = largura, b = profundidade, h = altura (px).
    medidas = (largura, profundidade, altura): embaixo, na aresta que sobe para trás à direita, e à esquerda. vertices = 8 nomes
    (frente: embaixo esq, embaixo dir, cima dir, cima esq; depois os de trás na mesma ordem). tm = instante das medidas"""
    V = [(0, 0, 0), (a, 0, 0), (a, h, 0), (0, h, 0), (0, 0, b), (a, 0, b), (a, h, b), (0, h, b)]
    F = [(0, 1, 2, 3), (4, 5, 6, 7), (0, 1, 5, 4), (3, 2, 6, 7), (0, 3, 7, 4), (1, 2, 6, 5)]
    pts = _solido(c, t, t0, V, F, _vista_obliqua(), x, y, cor, preenche, d=d, **kw)
    tm = tm if tm is not None else t0 + d + 0.2
    ma, mb, mh = medidas
    _medida_aresta(c, t, tm, pts[0], pts[1], ma, (0, 1), size)
    _medida_aresta(c, t, tm + 0.15, pts[1], pts[5], mb, (1, 0.35), size)
    _medida_aresta(c, t, tm + 0.3, pts[0], pts[3], mh, (-1, 0), size)
    if vertices:
        G = (sum(p_[0] for p_ in pts) / 8, sum(p_[1] for p_ in pts) / 8)
        for i, s in enumerate(vertices):
            if s:
                foco(c, t, t0 + d * 0.6 + 0.05 * i, 0.4, lambda q, i=i, s=s: _cola(c, s, *pts[i], pts[i][0] - G[0], pts[i][1] - G[1], 12, size, "g", TINTA, q))
    return pts


def cubo(c, t, t0, x, y, a, medida=None, todas=False, **kw):
    """cubo de aresta a (px), em perspectiva cavaleira; medida escrita embaixo (todas=True: nas três direções)"""
    return paralelepipedo(c, t, t0, x, y, a, a, a, (medida, medida, medida) if todas else (medida, None, None), **kw)


def _base_regular(n, r, giro=0.0):
    ini = math.radians(90 + 180 / n + giro)  # um lado de frente para quem olha
    return [(r * math.cos(ini + k * 2 * math.pi / n), r * math.sin(ini + k * 2 * math.pi / n)) for k in range(n)]


def prisma(c, t, t0, cx, cy, n, r, h, altura=None, aresta=None, cor=None, preenche=0.14, size=48, d=1.0, giro=0.0, vista=(-24, 22), tm=None, **kw):
    """prisma reto de base regular com n lados (raio r px) e altura h px; (cx, cy) = centro da base de baixo na tela.
    altura = rótulo na aresta lateral mais à direita; aresta = rótulo de uma aresta da base, na frente"""
    base = _base_regular(n, r, giro)
    V = [(px, 0, pz) for px, pz in base] + [(px, h, pz) for px, pz in base]
    F = [tuple(range(n)), tuple(range(n, 2 * n))] + [(i, (i + 1) % n, n + (i + 1) % n, n + i) for i in range(n)]
    vs = _vista_alta(*vista)
    pts = _solido(c, t, t0, V, F, vs, cx, cy, cor, preenche, d=d, **kw)
    tm = tm if tm is not None else t0 + d + 0.2
    i_dir = max(range(n), key=lambda i: pts[i][0])
    _medida_aresta(c, t, tm + 0.15, pts[i_dir], pts[n + i_dir], altura, (1, 0), size)
    if aresta:
        i_fr = max(range(n), key=lambda i: pts[i][1] + pts[(i + 1) % n][1])
        _medida_aresta(c, t, tm, pts[i_fr], pts[(i_fr + 1) % n], aresta, (0, 1), size)
    return pts


def piramide(c, t, t0, cx, cy, n, r, h, altura=None, aresta=None, cor=None, preenche=0.14, size=48, d=1.0, giro=0.0, vista=(-24, 18), tm=None, **kw):
    """pirâmide reta de base regular com n lados (raio r px) e altura h px; (cx, cy) = centro da base na tela.
    altura = rótulo da altura tracejada (do vértice ao centro da base); aresta = rótulo de uma aresta da base, na frente"""
    base = _base_regular(n, r, giro)
    V = [(px, 0, pz) for px, pz in base] + [(0, h, 0)]
    F = [tuple(range(n))] + [(i, (i + 1) % n, n) for i in range(n)]
    vs = _vista_alta(*vista)
    pts = _solido(c, t, t0, V, F, vs, cx, cy, cor, preenche, d=d, **kw)
    tm = tm if tm is not None else t0 + d + 0.2
    if altura:
        topo, pe = pts[n], _proj((0, 0, 0), vs[0], vs[1], cx, cy)
        segmento(c, t, tm, topo, pe, None, cor=TINTA2, pontas=False, tracejado=True, largura=5)
        k = ease_back(prog(t, tm + 0.4, 0.3))
        if k > 0:
            c.drawCircle(*pe, 8 * k, M.paint(TINTA))
        foco(c, t, tm + 0.4, 0.4, lambda a: _cola(c, altura, pe[0], lerp(pe[1], topo[1], 0.3), 1, 0, 14, size, "b", COR_TEXTO, a))
    if aresta:
        i_fr = max(range(n), key=lambda i: pts[i][1] + pts[(i + 1) % n][1])
        _medida_aresta(c, t, tm, pts[i_fr], pts[(i_fr + 1) % n], aresta, (0, 1), size)
    return pts


def _elipse(c, cx, cy, rx, ry, a1, varre, cor, a, largura, dash=None):
    """arco de elipse; ângulos da tela (graus, horário a partir da direita)"""
    if a <= 0 or abs(varre) < 0.01:
        return
    pt = M.paint(cor, a, stroke=largura, cap_round=True)
    if dash:
        pt.setPathEffect(skia.DashPathEffect.Make(dash, 0))
    c.drawArc(skia.Rect.MakeXYWH(cx - rx, cy - ry, 2 * rx, 2 * ry), a1, varre, False, pt)


def _volume(c, path, x0, x1, cor, a):
    """preenchimento claro com sombra suave da esquerda para a direita (superfície curva)"""
    p = skia.Paint(AntiAlias=True)
    p.setShader(skia.GradientShader.MakeLinear(
        [skia.Point(x0, 0), skia.Point(x1, 0)],
        [hexc(mix(cor, "#FFFFFF", 0.62), a), hexc(mix(cor, "#FFFFFF", 0.82), a), hexc(mix(cor, "#FFFFFF", 0.5), a)], [0.0, 0.38, 1.0]))
    c.drawPath(path, p)


def cilindro(c, t, t0, cx, cy, r, h, raio=None, altura=None, cor=None, preenche=0.5, size=48, d=1.0, inclina=22, largura=6, tm=None):
    """cilindro reto: (cx, cy) = centro da base de baixo na tela; r e h em px. A metade de trás da base sai tracejada.
    raio = rótulo do raio desenhado na tampa; altura = rótulo à direita"""
    cor = cor or COR
    ry = r * math.sin(math.radians(inclina))
    hy = h * math.cos(math.radians(inclina))
    ct = cy - hy
    p = ease_io(prog(t, t0, d))
    q = ep(t, t0 + d * 0.5, 0.6)
    if q > 0 and preenche > 0:
        corpo = skia.Path()
        corpo.moveTo(cx - r, ct); corpo.lineTo(cx - r, cy)
        corpo.arcTo(skia.Rect.MakeXYWH(cx - r, cy - ry, 2 * r, 2 * ry), 180, -180, False)
        corpo.lineTo(cx + r, ct)
        corpo.arcTo(skia.Rect.MakeXYWH(cx - r, ct - ry, 2 * r, 2 * ry), 0, -180, False)
        corpo.close()
        _volume(c, corpo, cx - r, cx + r, cor, q * preenche * 1.6)
        c.drawOval(skia.Rect.MakeXYWH(cx - r, ct - ry, 2 * r, 2 * ry), M.paint(mix(cor, "#FFFFFF", 0.7), q * preenche * 1.6))
    if p > 0:
        _elipse(c, cx, cy, r, ry, 180, 180 * p, TINTA, 0.55, largura - 2, TRACO)  # metade de trás (em cima, na tela)
        _elipse(c, cx, cy, r, ry, 180, -180 * p, TINTA, 1.0, largura)
        _elipse(c, cx, ct, r, ry, 180, 360 * p, TINTA, 1.0, largura)
        for x_ in (cx - r, cx + r):
            M.line(c, x_, cy, x_, ct, TINTA, 1.0, largura, progress=p)
    tm = tm if tm is not None else t0 + d + 0.2
    if raio:
        segmento(c, t, tm, (cx, ct), (cx + r, ct), None, cor=COR_TEXTO, pontas=False, largura=5)
        k = ease_back(prog(t, tm, 0.3))
        if k > 0:
            c.drawCircle(cx, ct, 8 * k, M.paint(TINTA))
        foco(c, t, tm + 0.3, 0.4, lambda a: _cola(c, raio, cx + r / 2, ct, 0, -1, 10, size, "b", COR_TEXTO, a))
    if altura:
        foco(c, t, tm + 0.2, 0.4, lambda a: _cola(c, altura, cx + r, (cy + ct) / 2, 1, 0, 18, size, "b", COR_TEXTO, a))


def cone(c, t, t0, cx, cy, r, h, raio=None, altura=None, geratriz=None, cor=None, preenche=0.5, size=48, d=1.0, inclina=22, largura=6, tm=None):
    """cone reto: (cx, cy) = centro da base na tela; r e h em px. A parte de trás da base sai tracejada; altura e raio por dentro, tracejados.
    geratriz = rótulo na lateral direita"""
    cor = cor or COR
    ry = r * math.sin(math.radians(inclina))
    hy = h * math.cos(math.radians(inclina))
    vx, vy = cx, cy - hy
    # pontos de tangência das laterais com a elipse da base
    yt = -ry * ry / hy
    xt = r * math.sqrt(max(0.0, 1 - (yt / ry) ** 2))
    at = math.degrees(math.atan2(yt / ry, xt / r))  # ângulo (tela) do ponto à direita, um pouco para trás
    p = ease_io(prog(t, t0, d))
    q = ep(t, t0 + d * 0.5, 0.6)
    if q > 0 and preenche > 0:
        corpo = skia.Path()
        corpo.moveTo(vx, vy); corpo.lineTo(cx - xt, cy + yt)
        corpo.arcTo(skia.Rect.MakeXYWH(cx - r, cy - ry, 2 * r, 2 * ry), 180 - at, -(180 - 2 * at), False)
        corpo.close()
        _volume(c, corpo, cx - r, cx + r, cor, q * preenche * 1.6)
    if p > 0:
        _elipse(c, cx, cy, r, ry, at, (180 - 2 * at) * p, TINTA, 1.0, largura)  # frente (para baixo na tela)
        _elipse(c, cx, cy, r, ry, at, -(180 + 2 * at) * p, TINTA, 0.55, largura - 2, TRACO)  # trás
        M.line(c, vx, vy, cx - xt, cy + yt, TINTA, 1.0, largura, progress=p)
        M.line(c, vx, vy, cx + xt, cy + yt, TINTA, 1.0, largura, progress=p)
    tm = tm if tm is not None else t0 + d + 0.2
    if altura:
        segmento(c, t, tm, (vx, vy), (cx, cy), None, cor=TINTA2, pontas=False, tracejado=True, largura=5)
        foco(c, t, tm + 0.3, 0.4, lambda a: _cola(c, altura, cx, (vy + cy) / 2 + 30, -1, 0, 12, size, "b", COR_TEXTO, a))
    if raio:
        segmento(c, t, tm + 0.3, (cx, cy), (cx + r, cy), None, cor=COR_TEXTO, pontas=False, tracejado=True, largura=5)
        foco(c, t, tm + 0.6, 0.4, lambda a: _cola(c, raio, cx + r / 2, cy, 0, -1, 10, size, "b", COR_TEXTO, a))
    k = ease_back(prog(t, tm if (altura or raio) else 1e9, 0.3))
    if k > 0:
        c.drawCircle(cx, cy, 8 * k, M.paint(TINTA))
    if geratriz:
        foco(c, t, tm + 0.5, 0.4, lambda a: _cola(c, geratriz, (vx + cx + xt) / 2, (vy + cy + yt) / 2, 1, -0.25, 18, size, "b", COR_TEXTO, a))


def esfera(c, t, t0, cx, cy, r, raio=None, cor=None, preenche=0.5, size=48, d=1.0, inclina=18, largura=6, tm=None):
    """esfera: contorno, equador com a metade de trás tracejada e, se pedido, o raio do centro até a borda"""
    cor = cor or COR
    p = ease_io(prog(t, t0, d))
    q = ep(t, t0 + d * 0.5, 0.6)
    if q > 0 and preenche > 0:
        g = skia.Paint(AntiAlias=True)
        g.setShader(skia.GradientShader.MakeRadial(
            skia.Point(cx - r * 0.35, cy - r * 0.4), r * 1.45,
            [hexc(mix(cor, "#FFFFFF", 0.88), q * preenche * 1.6), hexc(mix(cor, "#FFFFFF", 0.62), q * preenche * 1.6), hexc(mix(cor, "#FFFFFF", 0.35), q * preenche * 1.6)], [0.0, 0.6, 1.0]))
        c.drawCircle(cx, cy, r, g)
    ry = r * math.sin(math.radians(inclina))
    if p > 0:
        c.drawArc(skia.Rect.MakeXYWH(cx - r, cy - r, 2 * r, 2 * r), 180, 360 * p, False, M.paint(TINTA, 1.0, stroke=largura, cap_round=True))
        _elipse(c, cx, cy, r, ry, 180, 180 * p, TINTA, 0.55, largura - 2, TRACO)
        _elipse(c, cx, cy, r, ry, 180, -180 * p, TINTA, 1.0, largura - 1)
    tm = tm if tm is not None else t0 + d + 0.2
    if raio:
        k = ease_back(prog(t, tm, 0.3))
        if k > 0:
            c.drawCircle(cx, cy, 9 * k, M.paint(TINTA))
        ang = -32
        P1 = (cx + r * math.cos(math.radians(ang)), cy + r * math.sin(math.radians(ang)))
        segmento(c, t, tm + 0.1, (cx, cy), P1, None, cor=COR_TEXTO, pontas=False, largura=6)
        foco(c, t, tm + 0.4, 0.4, lambda a: _cola(c, raio, (cx + P1[0]) / 2, (cy + P1[1]) / 2, -0.55, -1, 18, size, "b", COR_TEXTO, a))


# ---------------- diagramas ----------------
def _venn_centros(n, cx, cy, r):
    if n == 2:
        return [(cx - r * 0.62, cy), (cx + r * 0.62, cy)]
    return [(cx - r * 0.56, cy - r * 0.34), (cx + r * 0.56, cy - r * 0.34), (cx, cy + r * 0.6)]


def _venn_caixa(n, cx, cy, r, size=60):
    """o retângulo do universo, com lugar para os nomes dos conjuntos em cima"""
    cs = _venn_centros(n, cx, cy, r)
    x0 = min(x for x, _ in cs) - r - r * 0.32
    x1 = max(x for x, _ in cs) + r + r * 0.32
    y0 = min(y for _, y in cs) - r - size - 46
    y1 = max(y for _, y in cs) + r + r * 0.22
    return x0, y0, x1, y1


def _regiao_path(n, cx, cy, r, reg, size=60):
    """caminho da região: dentro dos conjuntos de reg ('A', 'AB', ...), fora dos outros; '' = só no universo"""
    cs = _venn_centros(n, cx, cy, r)
    letras = "ABC"[:n]
    x0, y0, x1, y1 = _venn_caixa(n, cx, cy, r, size)
    res = skia.Path()
    res.addRect(skia.Rect.MakeLTRB(x0, y0, x1, y1))
    for L, (x, y) in zip(letras, cs):
        circ = skia.Path()
        circ.addCircle(x, y, r)
        res = skia.Op(res, circ, skia.PathOp.kIntersect_PathOp if L in reg else skia.PathOp.kDifference_PathOp)
    return res


@lru_cache(None)
def _venn_lugar(n, cx, cy, r, reg):
    """o ponto mais folgado da região (longe de todas as bordas): é onde o número fica"""
    cs = _venn_centros(n, cx, cy, r)
    letras = "ABC"[:n]
    x0, y0, x1, y1 = min(x for x, _ in cs) - r, min(y for _, y in cs) - r, max(x for x, _ in cs) + r, max(y for _, y in cs) + r
    melhor, best = None, -1
    passo_ = max(4, r / 40)
    yy = y0
    while yy <= y1:
        xx = x0
        while xx <= x1:
            ok, folga = True, 1e9
            for L, (x, y) in zip(letras, cs):
                dd = math.hypot(xx - x, yy - y)
                if (dd < r) != (L in reg):
                    ok = False
                    break
                folga = min(folga, abs(dd - r))
            if ok and folga > best:
                melhor, best = (xx, yy), folga
            xx += passo_
        yy += passo_
    return melhor


def venn(c, t, t0, cx, cy, r, nomes=("A", "B"), numeros=None, pinta=(), universo="U", cor=None, size=60, d=0.8, tn=None, alfa=0.32, tp=None):
    """diagrama de Venn com 2 ou 3 conjuntos (raio r px), centrado em (cx, cy), dentro do retângulo do universo.
    Regiões pelo lugar do conjunto, não pelo nome: 'A', 'B', 'AB', 'C', 'AC', 'BC', 'ABC'; '' = fora de todos.
    numeros = {região: valor}; pinta = [região ou (região, instante)]; tn = {região: instante} dos números; tp = instante da pintura"""
    n = len(nomes)
    cor = cor or COR
    cs = _venn_centros(n, cx, cy, r)
    x0, y0, x1, y1 = _venn_caixa(n, cx, cy, r, size)
    if universo is not None and t >= t0:
        q = ep(t, t0, 0.5)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeLTRB(x0, y0, x1, y1), 18, 18), M.paint(TINTA, q, stroke=4))
        if universo:
            foco(c, t, t0 + 0.2, 0.4, lambda a: escreve(c, universo, x0 + 8, y0 - 16, 60, "i", TINTA2, a))  # o U fica por fora, no canto
    for i, item in enumerate(pinta):
        reg, ti = (item, tp if tp is not None else t0 + d + 0.3) if isinstance(item, str) else item
        q = ep(t, ti, 0.5)
        if q > 0:
            c.drawPath(_regiao_path(n, cx, cy, r, "".join(sorted(reg)), size), M.paint(cor, alfa * q))
    for i, (x, y) in enumerate(cs):
        q = ease_io(prog(t, t0 + 0.15 * i, d))
        if q > 0:
            c.drawArc(skia.Rect.MakeXYWH(x - r, y - r, 2 * r, 2 * r), -90, 360 * q, False, M.paint(TINTA, 1.0, stroke=6, cap_round=True))
    # nomes dos conjuntos: os de cima acima do círculo, puxados para fora; o de baixo, embaixo à direita
    for i, (s, (x, y)) in enumerate(zip(nomes, cs)):
        if i < 2:
            lx, ly = x + (-1 if i == 0 else 1) * r * 0.3, y - r - 14 - size * 0.37
            foco(c, t, t0 + d * 0.6 + 0.12 * i, 0.4, lambda a, s=s, lx=lx, ly=ly: _meio(c, s, lx, ly, size, "g", COR_TEXTO, a))
        else:
            foco(c, t, t0 + d * 0.6 + 0.12 * i, 0.4, lambda a, s=s, x=x, y=y: _cola(c, s, x + r * 0.72, y + r * 0.7, 1, 0.6, 22, size, "g", COR_TEXTO, a))
    for i, (reg, v) in enumerate((numeros or {}).items()):
        reg_ = "".join(sorted(reg))
        lugar = (x1 - size, y1 - size * 0.8) if reg_ == "" else _venn_lugar(n, float(cx), float(cy), float(r), reg_)
        if lugar is None:
            continue
        ti = (tn or {}).get(reg, t0 + d + 0.4 + 0.15 * i)
        foco(c, t, ti, 0.4, lambda a, v=v, lugar=lugar: _meio(c, v, lugar[0], lugar[1], size, "g", TINTA, a))
    return dict(centros=cs, caixa=(x0, y0, x1, y1))


def arvore(c, t, t0, niveis, x, y, w, h, ramos=None, folha=None, raiz="", tn=None, tf=None, destaque=(), size=48, size_ramo=40):
    """árvore de possibilidades, da esquerda para a direita, na caixa (x, y, w, h). niveis = uma lista de rótulos por nível, igual para
    todos os nós (["C", "K"]), ou uma função caminho → rótulos (sorteio sem reposição). ramos = rótulo de cada ramo, do mesmo jeito
    (lista paralela a niveis[i], ou função (caminho, rótulo) → texto, como "f{1}{2}"). folha = função caminho → texto no fim do ramo.
    tn = instante de cada nível; tf = das folhas; destaque = caminhos (tuplas) pintados na cor da matéria. Devolve {caminho: (x, y)}"""
    L = len(niveis)
    filhos = lambda cam: list(niveis[len(cam)](cam) if callable(niveis[len(cam)]) else niveis[len(cam)])

    def ramo_txt(cam, rot):
        if not ramos or ramos[len(cam)] is None:
            return None
        r_ = ramos[len(cam)]
        return r_(cam, rot) if callable(r_) else r_[filhos(cam).index(rot)]

    folhas = []

    def junta(cam):
        if len(cam) == L:
            folhas.append(cam)
            return
        for f_ in filhos(cam):
            junta(cam + (f_,))

    junta(())
    nf = len(folhas)
    larg_folha = 0
    if folha:
        larg_folha = max(larg(_num(folha(f_)), "b", size) for f_ in folhas) + 40
    col = (w - larg_folha - 40) / L
    pos = {}
    for j, f_ in enumerate(folhas):
        pos[f_] = (x + 40 + col * L, y + h * (j + 0.5) / nf)
    for nivel in range(L - 1, -1, -1):
        for f_ in folhas:
            cam = f_[:nivel]
            if cam not in pos:
                ys = [pos[g][1] for g in pos if len(g) == nivel + 1 and g[:nivel] == cam]
                pos[cam] = (x + 40 + col * nivel if nivel else x + 20, sum(ys) / len(ys))
    tn = tn or [t0 + 0.7 * i for i in range(L)]
    rotw = lambda s: (formula(None, _num(s), 0, 0, size, _est(_num(s), "g"), a=0) if s else 0)
    if raiz:
        foco(c, t, t0, 0.4, lambda a: _meio(c, raiz, pos[()][0], pos[()][1], size, "g", TINTA, a))
    else:
        k = ease_back(prog(t, t0, 0.35))
        if k > 0:
            c.drawCircle(*pos[()], 11 * k, M.paint(TINTA))
    for cam, (px, py) in pos.items():
        if not cam:
            continue
        pai = cam[:-1]
        ax, ay = pos[pai]
        ax += (rotw(pai[-1]) / 2 + 14) if pai else (rotw(raiz) / 2 + 14 if raiz else 14)
        bx = px - rotw(cam[-1]) / 2 - 14
        ti = tn[len(cam) - 1]
        forte = any(cam == dd[:len(cam)] for dd in destaque)
        cr = COR if forte else TINTA2
        if t >= ti:
            M.line(c, ax, ay, bx, py, cr, 1.0, 7 if forte else 5, progress=ease_io(prog(t, ti, 0.5)))
        foco(c, t, ti + 0.35, 0.4, lambda a, cam=cam, px=px, py=py, forte=forte: _meio(c, cam[-1], px, py, size, "g", COR_TEXTO if forte else TINTA, a))
        rt = ramo_txt(pai, cam[-1])
        if rt:
            mx, my = (ax + bx) / 2, (ay + py) / 2
            ux, uy = _uni(ax, ay, bx, py)
            nx, ny = (uy, -ux) if py <= ay else (-uy, ux)
            if abs(py - ay) < 1:
                nx, ny = 0, -1
            foco(c, t, ti + 0.4, 0.4, lambda a, rt=rt, mx=mx, my=my, nx=nx, ny=ny, forte=forte: _cola(c, rt, mx, my, nx, ny, 8, size_ramo, "b", COR_TEXTO if forte else TINTA2, a))
    if folha:
        tf = tf if tf is not None else tn[-1] + 0.7
        for j, f_ in enumerate(folhas):
            px, py = pos[f_]
            forte = f_ in destaque
            s = _num(folha(f_))
            foco(c, t, tf + 0.06 * j, 0.4, lambda a, s=s, px=px, py=py, f_=f_, forte=forte: escreve(c, s, px + rotw(f_[-1]) / 2 + 40, py + size * 0.36, size, "b", COR_TEXTO if forte else CINZA, a))
    return pos


def trigono(c, t, t0, cx, cy, r, ang, rotulo="θ", seno=True, cosseno=True, tangente=False, notaveis=(), ponto_="P", cor=None,
            size=46, ts=None, escuro=False):
    """círculo trigonométrico de raio r px em (cx, cy). ang em graus (pode variar com t, para girar). Mostra o ângulo, o ponto,
    o cosseno projetado no eixo x e o seno no eixo y; tangente=True traça a tangente em x = 1. notaveis = ângulos marcados com rótulo.
    ts = {"circulo", "raio", "cos", "sen", "tg"}: instantes (senão, em fila)"""
    cor = cor or COR
    tinta = "#FFFFFF" if escuro else TINTA
    ts = ts or {}
    tc = ts.get("circulo", t0)
    tr = ts.get("raio", t0 + 1.0)
    tcos = ts.get("cos", tr + 0.8)
    tsen = ts.get("sen", tcos + 0.8)
    ttg = ts.get("tg", tsen + 0.8)
    if t >= tc:
        q = ep(t, tc, 0.6)
        M.arrow(c, cx - r - 70, cy, cx + r + 90, cy, tinta, 1.0, 4, 20, q)
        M.arrow(c, cx, cy + r + 70, cx, cy - r - 90, tinta, 1.0, 4, 20, q)
        c.drawArc(skia.Rect.MakeXYWH(cx - r, cy - r, 2 * r, 2 * r), 0, -360 * ease_io(prog(t, tc + 0.2, 0.9)), False, M.paint(tinta, 1.0, stroke=5))
    foco(c, t, tc + 0.6, 0.4, lambda a: (escreve(c, "cos", cx + r + 60, cy + 58, size, "i", TINTA2 if not escuro else CLARO, a),
                                         escreve(c, "sen", cx + 22, cy - r - 62, size, "i", TINTA2 if not escuro else CLARO, a)))
    for s, X, Y, horiz, nx, ny in (("1", cx + r, cy, True, -1, 1), ("−1", cx - r, cy, True, 1, 1), ("1", cx, cy - r, False, -1, 1), ("−1", cx, cy + r, False, -1, -1)):
        foco(c, t, tc + 0.7, 0.4, lambda a, s=s, X=X, Y=Y, horiz=horiz, nx=nx, ny=ny: (
            M.line(c, X - (0 if horiz else 10), Y - (10 if horiz else 0), X + (0 if horiz else 10), Y + (10 if horiz else 0), tinta, a, 4),
            _cola(c, s, X, Y, nx, ny, 16, size * 0.9, "b", tinta, a)))  # por dentro: por fora ficam os ângulos notáveis
    for i, g in enumerate(notaveis):
        X, Y = _no_circ(cx, cy, r, g)
        gd = math.radians(g + (22 if g % 90 == 0 else 0))  # sobre o eixo, o rótulo sai de lado para não cair na seta
        foco(c, t, tc + 0.9 + 0.05 * i, 0.4, lambda a, g=g, X=X, Y=Y, gd=gd: (
            c.drawCircle(X, Y, 7, M.paint(CINZA, a)),
            _cola(c, f"{_num(g)}°", X, Y, math.cos(gd), -math.sin(gd), 14, 40, "b", CINZA, a)))
    a_r = math.radians(ang)
    co, se = math.cos(a_r), math.sin(a_r)
    Px, Py = cx + r * co, cy - r * se
    if cosseno and t >= tcos:
        q = ep(t, tcos, 0.5)
        M.line(c, Px, Py, Px, cy, tinta, 0.7, 4, dash=TRACO, progress=q)
        M.line(c, cx, cy, cx + r * co, cy, cor, 1.0, 12, progress=ep(t, tcos + 0.3, 0.5), cap_round=False)
        foco(c, t, tcos + 0.5, 0.4, lambda a: _meio(c, f"cos {rotulo}", cx + r * co / 2, cy + (1 if se >= 0 else -1) * (size * 0.95), size, "b", COR_TEXTO if not escuro else CLARO, a))
    if seno and t >= tsen:
        q = ep(t, tsen, 0.5)
        M.line(c, Px, Py, cx, Py, tinta, 0.7, 4, dash=TRACO, progress=q)
        M.line(c, cx, cy, cx, Py, cor, 1.0, 12, progress=ep(t, tsen + 0.3, 0.5), cap_round=False)
        foco(c, t, tsen + 0.5, 0.4, lambda a: _cola(c, f"sen {rotulo}", cx, cy - r * se / 2, -1 if co >= 0 else 1, 0, 18, size, "b", COR_TEXTO if not escuro else CLARO, a))
    if tangente and abs(co) > 0.05 and t >= ttg:
        tg = se / co
        q = ep(t, ttg, 0.5)
        Ty = cy - r * tg
        M.line(c, cx + r, cy - r * 1.6, cx + r, cy + r * 1.6, tinta, q * 0.5, 3)
        M.line(c, cx, cy, cx + r, Ty, tinta, 0.7, 4, dash=TRACO, progress=q)
        M.line(c, cx + r, cy, cx + r, Ty, cor, 1.0, 12, progress=ep(t, ttg + 0.3, 0.5), cap_round=False)
        foco(c, t, ttg + 0.5, 0.4, lambda a: _cola(c, f"tg {rotulo}", cx + r, Ty, 1, 0, 18, size, "b", COR_TEXTO if not escuro else CLARO, a))
    if t >= tr:
        q = ep(t, tr, 0.5)
        ra = r * 0.24
        path = skia.Path()
        path.moveTo(cx, cy); path.arcTo(skia.Rect.MakeXYWH(cx - ra, cy - ra, 2 * ra, 2 * ra), 0, -ang * q, False); path.close()
        c.drawPath(path, M.paint(cor, 0.2))
        c.drawArc(skia.Rect.MakeXYWH(cx - ra, cy - ra, 2 * ra, 2 * ra), 0, -ang * q, False, M.paint(cor, 1.0, stroke=5))
        M.line(c, cx, cy, Px, Py, tinta, 1.0, 6, progress=q)
        k = ease_back(prog(t, tr + 0.3, 0.35))
        if k > 0:
            c.drawCircle(Px, Py, 13 * k, M.paint(cor))
        bis = math.radians(ang / 2)
        foco(c, t, tr + 0.3, 0.4, lambda a: _cola(c, rotulo, cx + ra * math.cos(bis), cy - ra * math.sin(bis), math.cos(bis), -math.sin(bis), 12, size, "b", COR_TEXTO if not escuro else CLARO, a))
        if ponto_:
            dp = math.radians(ang + 35)
            foco(c, t, tr + 0.4, 0.4, lambda a: _cola(c, ponto_, Px, Py, math.cos(dp), -math.sin(dp), 18, size * 1.1, "g", tinta, a))
    return Px, Py


# ---------------- matrizes e determinantes ----------------
class _GM:
    """geometria de uma matriz desenhada: x[j] = centro da coluna j, y[i] = centro da linha i; x0, x1, y0, y1 = moldura"""


def _cel_txt(v):
    return "" if v is None else _num(v) if not isinstance(v, str) else v.replace("-", "−")


def matriz_geo(m, cx, cy, size=88, gap=None, dy=None, wmin=None):
    """só a geometria (sem desenhar): útil para posicionar setas e marcas antes da matriz entrar"""
    lin, col = len(m), len(m[0])
    gap = size * 0.7 if gap is None else gap
    dy = size * 1.32 if dy is None else dy
    wmin = size * 0.62 if wmin is None else wmin
    ws = [max(wmin, max(formula(None, _cel_txt(m[i][j]), 0, 0, size, "g", a=0) for i in range(lin))) for j in range(col)]
    w = sum(ws) + gap * (col - 1)
    h = dy * (lin - 1) + size * 1.15
    G = _GM()
    x = cx - w / 2
    G.x = []
    for wj in ws:
        G.x.append(x + wj / 2)
        x += wj + gap
    G.y = [cy - dy * (lin - 1) / 2 + i * dy for i in range(lin)]
    pad = size * 0.46
    G.x0, G.x1, G.y0, G.y1 = cx - w / 2 - pad, cx + w / 2 + pad, cy - h / 2, cy + h / 2
    G.ws, G.dy, G.size, G.cx, G.cy = ws, dy, size, cx, cy
    return G


def matriz(c, t, t0, m, cx, cy, size=88, cor=None, cores=None, tc=None, tl=None, barras=False, nome=None, gap=None, dy=None,
           escuro=False, d=0.5, wmin=None, tm=None):
    """matriz com colchetes (barras=True: as barras do determinante), centrada em (cx, cy). Devolve a geometria G (G.x, G.y).
    m = lista de linhas; elemento = número, texto na escrita de E.formula ("a₁₂", "2x") ou None (casa vazia).
    cores = {(i, j): cor, ("l", i): cor, ("c", j): cor}; tc = {(i, j): instante} de cada elemento; tl = instante de cada linha;
    tm = instante da moldura (senão t0). nome = "A" escreve "A =" à esquerda."""
    G = matriz_geo(m, cx, cy, size, gap, dy, wmin)
    tinta = "#FFFFFF" if escuro else TINTA
    cores, tc = cores or {}, tc or {}
    tmold = t0 if tm is None else tm
    q = ep(t, tmold, 0.5)
    if q > 0:
        lw = max(5, size * 0.075)
        pt = M.paint(cor or tinta, q, stroke=lw, cap_round=True)
        pt.setStrokeJoin(skia.Paint.kRound_Join)
        k = size * 0.22
        meio, meia = (G.y0 + G.y1) / 2, (G.y1 - G.y0) / 2 * ease_out(q)
        for x, s in ((G.x0, 1), (G.x1, -1)):
            p = skia.Path()
            if barras:
                p.moveTo(x + s * k * 0.5, meio - meia); p.lineTo(x + s * k * 0.5, meio + meia)
            else:
                p.moveTo(x + s * k, meio - meia); p.lineTo(x, meio - meia); p.lineTo(x, meio + meia); p.lineTo(x + s * k, meio + meia)
            c.drawPath(p, pt)
    if nome:
        foco(c, t, tmold, d, lambda a: formula(c, f"{nome} =", G.x0 - size * 0.3, cy + size * 0.36, size, "g", cor or tinta, a, "right"))
    for i, linha_ in enumerate(m):
        for j, v in enumerate(linha_):
            s = _cel_txt(v)
            if not s:
                continue
            ti = tc.get((i, j), tl[i] if tl else t0)
            cc = cores.get((i, j), cores.get(("l", i), cores.get(("c", j), tinta)))
            foco(c, t, ti, d, lambda a, s=s, i=i, j=j, cc=cc: formula(c, s, G.x[j], G.y[i] + size * 0.36, size, "g", cc, a, "center"))
    return G


def matriz_marca(c, G, linha=None, coluna=None, cor=None, a=1.0, p=1.0, folga=None, cheia=0.12):
    """faixa arredondada sobre uma linha, uma coluna ou um elemento (linha e coluna) de uma matriz já desenhada.
    p = 0..1 faz a faixa crescer; cheia = opacidade do fundo (0 = só contorno)"""
    if a <= 0 or p <= 0:
        return
    cor = cor or COR
    f = G.size * 0.22 if folga is None else folga
    if linha is not None:
        y0, y1 = G.y[linha] - G.size * 0.58, G.y[linha] + G.size * 0.58
    else:
        y0, y1 = G.y0 + G.size * 0.0, G.y1
    if coluna is not None:
        x0, x1 = G.x[coluna] - G.ws[coluna] / 2 - f, G.x[coluna] + G.ws[coluna] / 2 + f
    else:
        x0, x1 = G.x0 + G.size * 0.12, G.x1 - G.size * 0.12
    if linha is None:
        y0, y1 = y0 - f * 0.2, y1 + f * 0.2
    e = ease_out(clamp(p))
    if coluna is None or linha is not None and coluna is None:
        x1 = x0 + (x1 - x0) * e
    else:
        y1 = y0 + (y1 - y0) * e
    r = skia.RRect.MakeRectXY(skia.Rect.MakeLTRB(x0, y0, x1, y1), G.size * 0.3, G.size * 0.3)
    if cheia > 0:
        c.drawRRect(r, M.paint(cor, a * cheia))
    c.drawRRect(r, M.paint(cor, a, stroke=max(4, G.size * 0.05)))
