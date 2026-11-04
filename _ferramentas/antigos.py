"""Visual do canal Nós, os Antigos: o museu de 2526, vetorial plano com luz de museu (1920x1080).

Dois mundos: o museu (frio, escuro, verde-água, holofotes âmbar) e as reconstituições do século 21
(quentes e saturadas, ver RECON). Nada de roxo neon nem pássaros (para não parecer cópia do Kurzgesagt).
Peças: paleta, fontes, a Lume (curadora), o salão, a vitrine com pedestal e etiqueta, holofote, poeira,
a peça 001 (rocha com celular), o logo e a câmera (zoom em um ponto do mundo).
"""
import math
import random
from functools import lru_cache
from pathlib import Path
import skia

W, H, FPS = 1920, 1080, 30
FONTES = Path(__file__).parent / "fontes" / "antigos"

# ---------------- paleta ----------------
# paleta alegre (v2, 01/11/2026): azul-noturno vivo + cores de festa; referências: Kurzgesagt e Infographics Show,
# mas sem roxo neon. A Lume não muda.
INK, VAULT, LINE = "#14206b", "#1f3196", "#3a52c4"
BONE, DUST = "#fff6e8", "#b8c4ff"
AMBER, CORAL, CYAN = "#ffc94a", "#ff5d73", "#3ee6c8"
PINK, SKY = "#ff7eb6", "#4cc9ff"
FESTA = [PINK, SKY, AMBER, CYAN, CORAL]
LUME = dict(corpo="#45e0cf", sombra="#2fb5a6", sombra2="#1b7a70", brilho="#a6f7ec", olho="#f7f2e8",
            iris="#1a5a6e", pupila="#0b1622", lanterna="#ffd27a", pe="#24968a", cracha="#ffb547", boca="#0f3b3a")
# reconstituições do século 21: quentes, saturadas, caóticas
RECON = dict(ceu1="#ff5d8f", ceu2="#ff9f43", ceu3="#ffe08a", predios=["#2e47c9", "#e8487a", "#17a99a", "#f08a2e", "#3a63e0"],
             fundo="#c4507a", janela="#fff1a8", estrada="#26307e", farol="#fff6d0", verde="#3fd17a")


def hexc(h, a=1.0):
    h = h.lstrip("#")
    return skia.ColorSetARGB(int(max(0, min(1, a)) * 255), int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16))


def mix(c1, c2, f):
    a = [int(c1.lstrip("#")[i:i + 2], 16) for i in (0, 2, 4)]
    b = [int(c2.lstrip("#")[i:i + 2], 16) for i in (0, 2, 4)]
    return "#" + "".join(f"{int(x + (y - x) * f):02x}" for x, y in zip(a, b))


# ---------------- tempo ----------------
def clamp(x, a=0.0, b=1.0):
    return max(a, min(b, x))


def lerp(a, b, f):
    return a + (b - a) * f


def prog(t, t0, d=0.5):
    return clamp((t - t0) / d) if d > 0 else float(t >= t0)


def ease_out(x):
    return 1 - (1 - x) ** 3


def ease_io(x):
    return 4 * x ** 3 if x < 0.5 else 1 - (-2 * x + 2) ** 3 / 2


def ease_back(x):
    c1, c3 = 1.70158, 2.70158
    return 1 + c3 * (x - 1) ** 3 + c1 * (x - 1) ** 2


def ep(t, t0, d=0.5):
    return ease_out(prog(t, t0, d))


def mola(t, t0, freq=3.0, amort=4.0):
    """oscilação amortecida que começa em t0 (para antena, balanço, aterrissagem)"""
    u = t - t0
    return 0.0 if u < 0 else math.exp(-amort * u) * math.sin(2 * math.pi * freq * u)


# ---------------- fontes e texto ----------------
def _tag(s):
    return (ord(s[0]) << 24) | (ord(s[1]) << 16) | (ord(s[2]) << 8) | ord(s[3])


@lru_cache(None)
def typeface(fam, wght=400):
    """fam: display (Bricolage Grotesque) · sans (IBM Plex Sans) · mono (IBM Plex Mono) · thumb (Rubik)"""
    # o skia-python 144 ignora o eixo de peso das fontes variáveis (fica no peso padrão: Bricolage 800,
    # Plex Sans 400, Rubik 300); por isso o Rubik das miniaturas vem de um arquivo estático Black
    if fam == "thumb" and wght >= 800:
        return skia.Typeface.MakeFromFile(str(FONTES / "Rubik-Black.ttf"))
    if fam == "mono":
        return skia.Typeface.MakeFromFile(str(FONTES / ("IBMPlexMono-Medium.ttf" if wght >= 500 else "IBMPlexMono-Regular.ttf")))
    tf = skia.Typeface.MakeFromFile(str(FONTES / {"display": "BricolageGrotesque.ttf", "sans": "IBMPlexSans.ttf",
                                                   "thumb": "Rubik.ttf"}[fam]))
    C = skia.FontArguments.VariationPosition.Coordinate
    coords = [C(_tag("wght"), wght)] + ([C(_tag("opsz"), 96)] if fam == "display" else [])
    fa = skia.FontArguments()
    fa.setVariationDesignPosition(skia.FontArguments.VariationPosition(skia.FontArguments.VariationPosition.Coordinates(coords)))
    return tf.makeClone(fa)


@lru_cache(512)
def font(fam, size, wght=400):
    f = skia.Font(typeface(fam, wght), size)
    f.setSubpixel(True)
    f.setEdging(skia.Font.Edging.kSubpixelAntiAlias)
    f.setHinting(skia.FontHinting.kNone)
    f.setLinearMetrics(True)
    return f


def text_w(s, size, fam="sans", wght=400, tracking=0.0):
    return font(fam, size, wght).measureText(s) + tracking * size * max(0, len(s) - 1)


def text(c, s, x, y, size, fam="sans", wght=400, color=BONE, a=1.0, align="left", tracking=0.0):
    """tracking em fração do tamanho da letra (0.12 = espaçado, como nas etiquetas)"""
    f, p = font(fam, size, wght), paint(color, a)
    w = text_w(s, size, fam, wght, tracking)
    x0 = x - w / 2 if align == "center" else x - w if align == "right" else x
    if not tracking:
        c.drawString(s, x0, y, f, p)
        return w
    for ch in s:
        c.drawString(ch, x0, y, f, p)
        x0 += f.measureText(ch) + tracking * size
    return w


# ---------------- pintura ----------------
def paint(color, a=1.0, stroke=None, blur=0.0, blend=None, cap_round=True):
    p = skia.Paint(AntiAlias=True, Color=hexc(color, a))
    if stroke:
        p.setStyle(skia.Paint.kStroke_Style)
        p.setStrokeWidth(stroke)
        if cap_round:
            p.setStrokeCap(skia.Paint.kRound_Cap)
            p.setStrokeJoin(skia.Paint.kRound_Join)
    if blur:
        p.setMaskFilter(skia.MaskFilter.MakeBlur(skia.kNormal_BlurStyle, blur))
    if blend:
        p.setBlendMode(blend)
    return p


def linear(x0, y0, x1, y1, cores, pos=None, a=1.0):
    p = skia.Paint(AntiAlias=True)
    p.setShader(skia.GradientShader.MakeLinear([skia.Point(x0, y0), skia.Point(x1, y1)],
                                               [hexc(*cc) if isinstance(cc, tuple) else hexc(cc, a) for cc in cores], pos))
    return p


def radial(cx, cy, r, cores, pos=None, blend=None):
    p = skia.Paint(AntiAlias=True)
    p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), max(r, 0.1),
                                               [hexc(*cc) if isinstance(cc, tuple) else hexc(cc) for cc in cores], pos))
    if blend:
        p.setBlendMode(blend)
    return p


def poly(pts, close=True):
    p = skia.Path()
    p.moveTo(*pts[0])
    for q in pts[1:]:
        p.lineTo(*q)
    if close:
        p.close()
    return p


def oval(cx, cy, rx, ry):
    return skia.Rect.MakeLTRB(cx - rx, cy - ry, cx + rx, cy + ry)


def rr(x, y, w, h, r):
    return skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), r, r)


def glow(c, cx, cy, r, color, a=1.0):
    """brilho aditivo (lanternas, holofotes, telas)"""
    c.drawCircle(cx, cy, r, radial(cx, cy, r, [(color, a), (color, a * 0.35), (color, 0)], [0, 0.35, 1],
                                   blend=skia.BlendMode.kScreen))


# =====================================================================
# A LUME
# =====================================================================
POSE = dict(look=(0.0, 0.0), blink=0.0, lid=0.0, brow=0.0, brow_y=0.0, mouth=0.0, smile=0.6, squash=0.0, tilt=0.0,
            arm_l=0.15, arm_r=0.15, lantern=1.0, sway=0.0, face=1, cheek=0.5, o_mouth=False)


def pose(**kw):
    d = dict(POSE)
    d.update(kw)
    return d


def lume(c, x, y, s=1.0, p=None):
    """A Lume com os pés em (x, y). s=1 → ~210 px de altura (com a antena). p = pose(...)
    look: para onde a pupila olha (-1..1) · blink/lid: pálpebra (1 = fechado) · brow: sobrancelha
    (+ curiosa, - preocupada) · mouth: boca aberta (0..1, para a fala) · smile: curva do sorriso
    squash: + achata / - estica · tilt: inclinação em radianos · arm_l/arm_r: ângulo dos braços
    (0 = pendurado, 2.6 = para cima) · sway: balanço da antena · face: 1 olha p/ direita, -1 p/ esquerda"""
    p = p or POSE
    L = LUME
    # sombra no chão (fica fora da escala vertical)
    c.drawOval(oval(x, y + 2, 58 * s * (1 + 0.15 * p["squash"]), 9 * s), paint(INK, 0.55, blur=6 * s))
    c.save()
    c.translate(x, y)
    c.rotate(math.degrees(p["tilt"]))
    sq = p["squash"]
    c.scale(s * p["face"] * (1 + 0.5 * sq), s * (1 - sq))
    bx, by, rx, ry = 0.0, -70.0, 60.0, 64.0

    # pés
    for fx in (-24, 24):
        c.drawOval(oval(fx, -6, 17, 9), paint(L["pe"]))

    # braços (atrás do corpo): cápsulas presas nas laterais
    for side, ang in ((-1, p["arm_l"]), (1, p["arm_r"])):
        c.save()
        c.translate(side * 50, -64)
        c.rotate(-side * math.degrees(ang))
        c.drawRRect(rr(-7, -4, 14, 40, 7), paint(L["sombra"]))
        c.drawCircle(0, 34, 8.5, paint(L["corpo"]))
        c.restore()

    # antena com lanterna
    sw = p["sway"]
    tipx, tipy = 16 + 26 * math.sin(sw), -184 + 6 * (1 - math.cos(sw))
    ant = skia.Path()
    ant.moveTo(6, -130)
    ant.cubicTo(8, -150, tipx - 10 * math.sin(sw) - 4, -160, tipx, tipy + 12)
    c.drawPath(ant, paint(L["sombra2"], stroke=5))
    lt = p["lantern"]
    if lt > 0:
        glow(c, tipx, tipy, 70, L["lanterna"], 0.55 * lt)
    c.drawRRect(rr(tipx - 7, tipy + 7, 14, 7, 3), paint(L["sombra2"]))
    c.drawCircle(tipx, tipy, 11.5, paint(mix(L["sombra2"], L["lanterna"], 0.25 + 0.75 * lt)))
    c.drawCircle(tipx - 3.5, tipy - 3.5, 3.6, paint("#ffffff", 0.75 * lt))

    # corpo com sombreamento plano (uma forma de sombra + um brilho)
    corpo = skia.Path()
    corpo.addOval(oval(bx, by, rx, ry))
    c.drawPath(corpo, paint(L["corpo"]))
    c.save()
    c.clipPath(corpo, doAntiAlias=True)
    c.drawOval(oval(bx + 26, by + 30, rx * 1.05, ry * 0.95), paint(L["sombra"]))
    c.drawOval(oval(bx - 24, by - 30, 30, 20), paint(L["brilho"], 0.55))
    # luz âmbar da lanterna no topo
    c.drawOval(oval(bx + 4, by - ry - 6, rx * 0.9, 22), paint(L["lanterna"], 0.22 * lt, blur=6))
    c.restore()

    # crachá de curadora
    c.save()
    c.translate(-30, -44)
    c.rotate(-12)
    c.drawRRect(rr(-11, -8, 22, 16, 3), paint(L["cracha"]))
    c.drawRect(skia.Rect.MakeXYWH(-6, -2, 12, 2.4), paint(INK, 0.6))
    c.drawRect(skia.Rect.MakeXYWH(-6, 2.5, 8, 2.4), paint(INK, 0.4))
    c.restore()

    # bochecha
    if p["cheek"]:
        c.drawOval(oval(40, -54, 9, 5.5), paint("#ff8a7a", p["cheek"]))

    # o olho grande
    ex, ey, er = 10.0, -84.0, 27.0
    olho = skia.Path()
    olho.addCircle(ex, ey, er)
    c.drawCircle(ex, ey + 2, er + 3.5, paint(L["sombra2"], 0.35))
    c.drawPath(olho, paint(L["olho"]))
    c.save()
    c.clipPath(olho, doAntiAlias=True)
    lx, ly = p["look"]
    ix, iy = ex + 9 * lx, ey + 7 * ly
    c.drawCircle(ix, iy, 16, paint(L["iris"]))
    c.drawCircle(ix, iy, 16, paint(CYAN, 0.55, stroke=2.2))
    c.drawCircle(ix, iy, 8.5, paint(L["pupila"]))
    c.drawCircle(ix - 6, iy - 6, 4.6, paint("#ffffff", 0.95))
    c.drawCircle(ix + 5, iy + 5, 2.0, paint("#ffffff", 0.6))
    # pálpebra de cima
    fech = max(p["blink"], p["lid"])
    if fech > 0.01:
        yb = ey - er + 2 * er * fech
        c.drawRect(skia.Rect.MakeLTRB(ex - er - 2, ey - er - 2, ex + er + 2, yb), paint(L["corpo"]))
        c.drawLine(ex - er, yb, ex + er, yb, paint(L["sombra2"], stroke=3))
    c.restore()

    # sobrancelha
    c.save()
    c.translate(ex + 2, ey - er - 11 - 6 * p["brow_y"])
    c.rotate(-14 * p["brow"])
    br = skia.Path()
    br.moveTo(-15, 2)
    br.quadTo(0, -4 - 2 * abs(p["brow"]), 15, 2)
    c.drawPath(br, paint(L["sombra2"], stroke=5))
    c.restore()

    # boca: sorriso fechado ou aberta (fala)
    mx, my, mo = 10.0, -42.0, p["mouth"]
    if p["o_mouth"]:
        c.drawOval(oval(mx, my, 6 + 3 * mo, 7 + 4 * mo), paint(L["boca"]))
    elif mo < 0.06:
        sm = skia.Path()
        sm.moveTo(mx - 10, my - 2 * p["smile"])
        sm.quadTo(mx, my + 9 * p["smile"], mx + 10, my - 2 * p["smile"])
        c.drawPath(sm, paint(L["sombra2"], stroke=4))
    else:
        h = 4 + 13 * mo
        bo = skia.Path()
        bo.moveTo(mx - 11, my - 2)
        bo.quadTo(mx, my - 2 + 2 * p["smile"], mx + 11, my - 2)
        bo.quadTo(mx + 9, my + h, mx, my + h)
        bo.quadTo(mx - 9, my + h, mx - 11, my - 2)
        c.drawPath(bo, paint(L["boca"]))
        c.save()
        c.clipPath(bo, doAntiAlias=True)
        c.drawOval(oval(mx + 1, my + h + 1, 7, 4 + 3 * mo), paint(CORAL, 0.9))
        c.restore()
    c.restore()


def lume_viva(t, base=None, fala=0.0, olhar=None):
    """pose com vida: respiração, piscadas e antena balançando; fala = abertura da boca (0..1)"""
    p = pose(**(base or {}))
    p["squash"] += 0.025 * math.sin(t * 2.1)
    # piscadas em tempos pseudo-aleatórios (determinísticas)
    for tb in (1.3, 4.9, 7.2, 11.8, 15.1, 19.6, 22.4, 26.3, 30.5, 33.9, 38.2):
        u = (t - tb) / 0.16
        if 0 <= u <= 1:
            p["blink"] = max(p["blink"], math.sin(math.pi * u))
    p["sway"] += 0.08 * math.sin(t * 1.6) + 0.04 * math.sin(t * 3.7)
    p["mouth"] = max(p["mouth"], fala)
    if olhar is not None:
        p["look"] = olhar
    return p


# =====================================================================
# O SALÃO DO MUSEU (coordenadas do mundo: plano geral em 1920x1080)
# =====================================================================
CHAO = 770  # linha onde a parede encontra o chão


def _silhueta(c, tipo, cx, by, s, cor):
    """objetos do século 21 nos nichos do fundo, só em silhueta"""
    pp = paint(cor)
    if tipo == "cone":
        c.drawPath(poly([(cx - 26 * s, by), (cx - 9 * s, by - 80 * s), (cx + 9 * s, by - 80 * s), (cx + 26 * s, by)]), pp)
        c.drawRect(skia.Rect.MakeLTRB(cx - 34 * s, by - 6 * s, cx + 34 * s, by), pp)
    elif tipo == "garrafa":
        c.drawRRect(rr(cx - 18 * s, by - 76 * s, 36 * s, 76 * s, 10 * s), pp)
        c.drawRRect(rr(cx - 7 * s, by - 100 * s, 14 * s, 30 * s, 4 * s), pp)
    elif tipo == "cadeira":
        c.drawRect(skia.Rect.MakeLTRB(cx - 26 * s, by - 50 * s, cx + 26 * s, by - 42 * s), pp)
        c.drawRect(skia.Rect.MakeLTRB(cx + 18 * s, by - 110 * s, cx + 26 * s, by - 42 * s), pp)
        for lx in (-24, 18):
            c.drawRect(skia.Rect.MakeLTRB(cx + lx * s, by - 44 * s, cx + (lx + 6) * s, by), pp)
    elif tipo == "violao":
        c.drawOval(oval(cx, by - 30 * s, 28 * s, 30 * s), pp)
        c.drawOval(oval(cx, by - 74 * s, 21 * s, 22 * s), pp)
        c.drawRect(skia.Rect.MakeLTRB(cx - 4 * s, by - 150 * s, cx + 4 * s, by - 80 * s), pp)
    elif tipo == "tv":
        c.drawRRect(rr(cx - 50 * s, by - 86 * s, 100 * s, 70 * s, 6 * s), pp)
        c.drawRect(skia.Rect.MakeLTRB(cx - 20 * s, by - 16 * s, cx + 20 * s, by), pp)
    elif tipo == "carrinho":
        c.drawRRect(rr(cx - 46 * s, by - 70 * s, 92 * s, 46 * s, 6 * s), pp)
        for wx in (-30, 30):
            c.drawCircle(cx + wx * s, by - 10 * s, 10 * s, pp)


def nichos(c, t, px=0.0):
    """parede do fundo: nichos em arco com objetos em silhueta (parallax px)"""
    tipos = ["violao", "cone", "tv", "cadeira", "garrafa", "carrinho", "cone", "tv"]
    for i in range(-1, 8):
        cx = 120 + i * 270 + px * 0.35
        top, bot, w = 250, CHAO - 40, 170
        arco = skia.Path()
        arco.moveTo(cx - w / 2, bot)
        arco.lineTo(cx - w / 2, top + w / 2)
        arco.arcTo(skia.Rect.MakeLTRB(cx - w / 2, top, cx + w / 2, top + w), 180, 180, False)
        arco.lineTo(cx + w / 2, bot)
        arco.close()
        cor = FESTA[(i + 1) % len(FESTA)]
        c.drawPath(arco, linear(0, top, 0, bot, [mix(cor, "#1d2f8f", 0.55), mix(cor, "#1d2f8f", 0.15)]))
        c.save()
        c.clipPath(arco, doAntiAlias=True)
        c.drawOval(oval(cx, bot, w * 0.7, 60), paint("#ffffff", 0.18, blur=20))
        c.drawPath(poly([(cx - 14, top), (cx + 14, top), (cx + 60, bot), (cx - 60, bot)]),
                   linear(0, top, 0, bot, [(AMBER, 0.10), (AMBER, 0.0)]))
        _silhueta(c, tipos[i % len(tipos)], cx, bot - 4, 0.85, mix(cor, INK, 0.55))
        c.restore()
        c.drawPath(arco, paint("#ffffff", 0.25, stroke=3))


def salao(c, t, px=0.0, titulo="ALA 01 · O QUE SOBROU", titulo_a=1.0):
    """parede, nichos, faixa de luz verde-água, chão polido com reflexos"""
    c.drawRect(skia.Rect.MakeWH(W, CHAO), linear(0, 0, 0, CHAO, ["#111b5c", "#1d2f8f", "#2540a8"], [0, 0.55, 1]))
    # trilhos de luz do teto
    c.drawRect(skia.Rect.MakeLTRB(0, 0, W, 70), paint("#0c1550"))
    for i in range(-1, 12):
        xx = 40 + i * 180 + px * 0.5
        c.drawRect(skia.Rect.MakeLTRB(xx - 30, 64, xx + 30, 70), paint(LINE))
    nichos(c, t, px)
    if titulo:
        text(c, titulo, W / 2 + px * 0.35, 196, 30, "mono", 500, DUST, 0.55 * titulo_a, "center", tracking=0.32)
    # rodapé de luz verde-água (o "futuro" do museu)
    c.drawRect(skia.Rect.MakeLTRB(0, CHAO - 8, W, CHAO), paint(VAULT))
    c.drawRect(skia.Rect.MakeLTRB(0, CHAO - 3, W, CHAO - 1), paint(CYAN, 0.75))
    c.drawRect(skia.Rect.MakeLTRB(0, CHAO - 14, W, CHAO + 8), paint(CYAN, 0.18, blur=8))
    # chão
    c.drawRect(skia.Rect.MakeLTRB(0, CHAO, W, H + 400), linear(0, CHAO, 0, H, ["#2238a0", "#131f66"]))
    c.drawRect(skia.Rect.MakeLTRB(0, CHAO, W, CHAO + 60), paint(CYAN, 0.12, blur=18))
    vx, vy = W / 2 + px * 0.2, 430
    pl = paint(LINE, 0.45, stroke=1.5)
    for i in range(-14, 15):
        xb = W / 2 + i * 260 + px
        x0 = vx + (xb - vx) * 0.0
        u = (CHAO - vy) / (H + 400 - vy)
        c.drawLine(lerp(vx, xb, u), CHAO, xb, H + 400, pl)
    for k in range(1, 9):
        yy = CHAO + (H + 400 - CHAO) * (k / 9) ** 1.8
        c.drawLine(0, yy, W, yy, paint(LINE, 0.25, stroke=1))


def poeira(c, t, rect, n=40, seed=1, a=0.5, cor=BONE, zoom=1.0):
    """partículas flutuando na luz (dentro de rect = (x0, y0, x1, y1))"""
    x0, y0, x1, y1 = rect
    rnd = random.Random(seed)
    for _ in range(n):
        bx, by = rnd.uniform(x0, x1), rnd.uniform(y0, y1)
        sp, ph, r = rnd.uniform(4, 14), rnd.uniform(0, 6.28), rnd.uniform(0.8, 2.6)
        xx = x0 + ((bx - x0 + 9 * math.sin(t * 0.4 + ph)) % (x1 - x0))
        yy = y0 + ((by - y0 - sp * t) % (y1 - y0))
        tw = 0.5 + 0.5 * math.sin(t * 1.3 + ph * 3)
        c.drawCircle(xx, yy, r / zoom ** 0.4, paint(cor, a * (0.35 + 0.65 * tw)))


def holofote(c, cx, top, bot, w_top, w_bot, a=1.0):
    """cone de luz âmbar de cima para baixo + luminária no teto"""
    if a <= 0:
        return
    c.drawPath(poly([(cx - w_top / 2, top), (cx + w_top / 2, top), (cx + w_bot / 2, bot), (cx - w_bot / 2, bot)]),
               linear(0, top, 0, bot, [(AMBER, 0.30 * a), (AMBER, 0.10 * a), (AMBER, 0.0)], [0, 0.6, 1]))
    c.drawRRect(rr(cx - 26, top - 30, 52, 30, 6), paint("#0c1550"))
    c.drawOval(oval(cx, top, 22, 6), paint("#fff1d0", a))
    glow(c, cx, top + 4, 60, AMBER, 0.6 * a)


def pedestal(c, cx, top, w, h, etiqueta=None, luz=1.0):
    """bloco do pedestal com a etiqueta de museu na frente"""
    d = 16  # profundidade do tampo visto de cima
    c.drawPath(poly([(cx - w / 2, top), (cx + w / 2, top), (cx + w / 2 - d, top - d), (cx - w / 2 + d, top - d)]),
               paint(mix("#4a66e0", AMBER, 0.3 * luz)))
    c.drawRect(skia.Rect.MakeLTRB(cx - w / 2, top, cx + w / 2, top + h),
               linear(0, top, 0, top + h, [mix("#3350cc", AMBER, 0.14 * luz), "#1c2c8c"]))
    c.drawRect(skia.Rect.MakeLTRB(cx - w / 2, top, cx + w / 2, top + 4), paint(mix(LINE, AMBER, 0.5 * luz)))
    c.drawRect(skia.Rect.MakeLTRB(cx + w / 2 - 22, top, cx + w / 2, top + h), paint(INK, 0.35))
    c.drawOval(oval(cx, top + h, w * 0.62, 14), paint(INK, 0.6, blur=8))
    if etiqueta:
        ew, eh = min(w - 60, text_w(etiqueta, 15, "mono", 500, 0.08) + 34), 40
        ey = top + 40
        c.drawRRect(rr(cx - ew / 2, ey, ew, eh, 3), paint(mix("#ffe9c2", AMBER, 0.15 * luz)))
        c.drawRect(skia.Rect.MakeLTRB(cx - ew / 2, ey + eh - 5, cx + ew / 2, ey + eh), paint("#e2b97a"))
        text(c, etiqueta, cx, ey + 25, 15, "mono", 500, "#3a2c18", 1, "center", tracking=0.08)


def vitrine_vidro(c, cx, base, w, h, t=0.0, a=1.0, cam_x=0.0):
    """caixa de vidro sobre o pedestal (desenhar DEPOIS da peça)"""
    x0, y0 = cx - w / 2, base - h
    c.drawRect(skia.Rect.MakeLTRB(x0, y0, x0 + w, base), paint("#cfe6ff", 0.06 * a))
    # reflexos diagonais que deslizam um pouco com a câmera
    off = 30 * math.sin(t * 0.25) + cam_x * 0.15
    c.save()
    c.clipRect(skia.Rect.MakeLTRB(x0, y0, x0 + w, base))
    for k, (dx, ww, aa) in enumerate(((0.12, 0.16, 0.09), (0.36, 0.05, 0.07), (0.78, 0.10, 0.05))):
        xx = x0 + w * dx + off
        c.drawPath(poly([(xx, y0), (xx + w * ww, y0), (xx + w * ww - h * 0.55, base), (xx - h * 0.55, base)]),
                   paint("#ffffff", aa * a))
    c.restore()
    c.drawRect(skia.Rect.MakeLTRB(x0, y0, x0 + w, base), paint("#d6f1fa", 0.5 * a, stroke=3, cap_round=False))
    c.drawRect(skia.Rect.MakeLTRB(x0 - 4, y0 - 10, x0 + w + 4, y0), paint("#2c45b8", a))
    c.drawRect(skia.Rect.MakeLTRB(x0 - 4, y0 - 10, x0 + w + 4, y0 - 8), paint("#9fb4ff", 0.9 * a))
    c.drawLine(x0 + 3, y0 + 4, x0 + 3, base - 4, paint("#ffffff", 0.25 * a, stroke=2))


def vinheta(c, a=0.75):
    c.drawRect(skia.Rect.MakeWH(W, H), radial(W / 2, H / 2, W * 0.72, [("#070c38", 0), ("#070c38", 0), ("#070c38", a)],
                                              [0, 0.55, 1]))


# =====================================================================
# PEÇA 001: o celular preso na rocha
# =====================================================================
ESTRATOS = ["#c8673a", "#e88d4c", "#a94f2e", "#f2ab62", "#8f3f28", "#dc7a4a", "#b85a35"]


def rocha(c, cx, cy, w, h, luz=1.0, seed=3):
    """bloco de rocha sedimentar em camadas (cx, cy = centro)"""
    rnd = random.Random(seed)
    pts = []
    for k in range(14):
        ang = 2 * math.pi * k / 14
        rx, ry = w / 2 * rnd.uniform(0.9, 1.0), h / 2 * rnd.uniform(0.86, 1.0)
        # caixa arredondada: mais quadrada que um círculo
        ca, sa = math.cos(ang), math.sin(ang)
        sx = math.copysign(abs(ca) ** 0.55, ca)
        sy = math.copysign(abs(sa) ** 0.55, sa)
        pts.append((cx + rx * sx, cy + ry * sy))
    pedra = poly(pts)
    c.drawOval(oval(cx, cy + h / 2 + 4, w * 0.5, 12), paint(INK, 0.6, blur=8))
    c.drawPath(pedra, paint(ESTRATOS[0]))
    c.save()
    c.clipPath(pedra, doAntiAlias=True)
    y = cy - h / 2 - 10
    i = 0
    while y < cy + h / 2 + 10:
        hh = rnd.uniform(18, 40) * h / 220
        faixa = skia.Path()
        faixa.moveTo(cx - w, y)
        for k in range(9):
            faixa.lineTo(cx - w + k * w / 4, y + rnd.uniform(-5, 5))
        faixa.lineTo(cx + w, y + hh)
        faixa.lineTo(cx - w, y + hh)
        faixa.close()
        c.drawPath(faixa, paint(ESTRATOS[i % len(ESTRATOS)]))
        i += 1
        y += hh
    # pedrinhas e conchinhas nas camadas
    for _ in range(18):
        c.drawOval(oval(cx + rnd.uniform(-w / 2, w / 2), cy + rnd.uniform(-h / 2, h / 2), rnd.uniform(1.5, 3.2) * w / 280,
                        rnd.uniform(1, 2) * w / 280), paint("#fff1d6", rnd.uniform(0.25, 0.5)))
    # luz de cima e sombra embaixo/direita
    c.drawRect(skia.Rect.MakeLTRB(cx - w, cy - h / 2 - 20, cx + w, cy - h / 2 + 26), paint(AMBER, 0.22 * luz, blur=10))
    c.drawPath(poly([(cx + w * 0.18, cy + h), (cx + w, cy - h * 0.2), (cx + w, cy + h)]), paint(INK, 0.28))
    c.restore()
    c.drawPath(pedra, paint("#5a2416", 0.7, stroke=3))
    return pedra


def celular(c, cx, cy, s=1.0, ang=-14, tela=0.0, raiox=0.0, bateria=0.0, t=0.0):
    """celular rachado; tela = fantasma holográfico da tela acesa (0..1); raiox = contorno por dentro"""
    c.save()
    c.translate(cx, cy)
    c.rotate(ang)
    c.scale(s, s)
    w, h = 96, 176
    c.drawRRect(rr(-w / 2 + 6, -h / 2 + 8, w, h, 16), paint(INK, 0.5, blur=6))
    c.drawRRect(rr(-w / 2, -h / 2, w, h, 16), paint("#1c232c"))
    c.drawRRect(rr(-w / 2, -h / 2, w, h, 16), paint("#c9d3d6", 0.9, stroke=3.5))
    sc = rr(-w / 2 + 7, -h / 2 + 9, w - 14, h - 18, 9)
    c.drawRRect(sc, paint("#25323c"))
    c.save()
    c.clipRRect(sc, doAntiAlias=True)
    # rachaduras
    rach = paint("#8fb3bd", 0.75, stroke=1.8)
    for seg in [[(-12, -50), (6, -18), (-4, 4), (18, 40), (10, 70)], [(6, -18), (34, -30)], [(-4, 4), (-36, 18)],
                [(18, 40), (40, 52)], [(-12, -50), (-30, -80)]]:
        c.drawPath(poly(seg, close=False), rach)
    c.drawPath(poly([(-30, -82), (10, -82), (-30, -30)]), paint("#ffffff", 0.08))
    # fantasma da tela acesa (o passado do objeto)
    if tela > 0:
        c.drawRRect(sc, paint("#3fd0ff", 0.55 * tela))
        cores = [CORAL, AMBER, BONE, CYAN, "#7be36b"]
        for r_ in range(4):
            for k in range(3):
                c.drawRRect(rr(-30 + k * 22, -62 + r_ * 26, 16, 16, 5), paint(cores[(r_ * 3 + k) % 5], 0.9 * tela))
    c.restore()
    # contorno de raio-x: bateria por dentro
    if raiox > 0:
        c.drawRRect(rr(-30, -40, 60, 96, 6), paint(CYAN, raiox, stroke=2.5))
        c.drawRRect(rr(-30, -40, 60, 96, 6), paint(CYAN, 0.35 * raiox, stroke=10, blur=6))
        c.drawRect(skia.Rect.MakeXYWH(-10, -47, 20, 7), paint(CYAN, raiox))
        if bateria > 0:
            pisca = 0.55 + 0.45 * math.sin(t * 9)
            c.drawRect(skia.Rect.MakeXYWH(-24, 42, 48 * 0.06, 8), paint(CORAL, bateria * pisca))
            c.drawRRect(rr(-24, 42, 48, 8, 2), paint(CORAL, bateria * 0.8, stroke=1.5))
    c.restore()


def peca_001(c, cx, cy, s=1.0, t=0.0, tela=0.0, raiox=0.0, bateria=0.0, luz=1.0):
    """bloco de rocha com o celular preso no meio (cx, cy = centro do bloco)"""
    rocha(c, cx, cy, 280 * s, 190 * s, luz)
    celular(c, cx + 6 * s, cy - 20 * s, 0.82 * s, -14, tela, raiox, bateria, t)
    # um pedaço da rocha cobrindo o canto de baixo do celular (está "preso")
    lasca = poly([(cx - 64 * s, cy + 40 * s), (cx + 10 * s, cy + 28 * s), (cx + 70 * s, cy + 46 * s),
                  (cx + 40 * s, cy + 92 * s), (cx - 70 * s, cy + 92 * s)])
    c.save()
    c.clipPath(lasca, doAntiAlias=True)
    rocha(c, cx, cy, 280 * s, 190 * s, luz)
    c.restore()
    c.drawPath(poly([(cx - 64 * s, cy + 40 * s), (cx + 10 * s, cy + 28 * s), (cx + 70 * s, cy + 46 * s)], close=False),
               paint("#5a2416", 0.8, stroke=2.5))


# =====================================================================
# LOGO E CÂMERA
# =====================================================================
def logo(c, cx, cy, s=1.0, a=1.0, sub="MUSEU DA ERA DOS ANTIGOS · ANO 2526"):
    if a <= 0:
        return
    c.saveLayerAlpha(None, int(255 * clamp(a)))
    l1, l2 = "NÓS, OS ", "ANTIGOS"
    f = 96 * s
    w1, w2 = text_w(l1, f, "display", 800), text_w(l2, f, "display", 800)
    x0 = cx - (w1 + w2) / 2
    text(c, l1, x0, cy, f, "display", 800, BONE)
    text(c, l2, x0 + w1, cy, f, "display", 800, AMBER)
    c.drawRect(skia.Rect.MakeLTRB(x0, cy + 26 * s, x0 + w1 + w2, cy + 28.5 * s), paint(CYAN, 0.8))
    text(c, sub, cx, cy + 66 * s, 22 * s, "mono", 500, DUST, 1, "center", tracking=0.28)
    c.restore()


def camera(c, cx, cy, zoom):
    """mostra o ponto (cx, cy) do mundo no centro da tela com esse zoom"""
    c.translate(W / 2, H / 2)
    c.scale(zoom, zoom)
    c.translate(-cx, -cy)


# =====================================================================
# MUNDO QUENTE: reconstituição do século 21 (amostra)
# =====================================================================
def _guindaste(c, x, base, h, cor, t):
    c.drawRect(skia.Rect.MakeLTRB(x - 6, base - h, x + 6, base), paint(cor))
    lança = 220 + 0 * t
    c.drawRect(skia.Rect.MakeLTRB(x - 70, base - h - 8, x + lança, base - h + 4), paint(cor))
    c.drawPath(poly([(x - 6, base - h - 8), (x, base - h - 46), (x + 6, base - h - 8)]), paint(cor))
    gx = x + 60 + 120 * (0.5 + 0.5 * math.sin(t * 0.5))
    c.drawLine(gx, base - h + 4, gx, base - h + 120, paint(cor, stroke=2))
    c.drawRect(skia.Rect.MakeXYWH(gx - 14, base - h + 120, 28, 18), paint(cor))


def cidade_quente(c, t, seed=7, luzes=1.0, transito=1.0, cinza=0.0):
    """cidade do século 21 ao entardecer: quente, colorida, cheia de luz e movimento"""
    R = RECON
    c.drawRect(skia.Rect.MakeWH(W, H), linear(0, 0, 0, 760, [R["ceu1"], R["ceu2"], R["ceu3"]], [0, 0.6, 1]))
    sx, sy = 1300, 470
    glow(c, sx, sy, 520, "#fff3c4", 0.55)
    c.drawCircle(sx, sy, 130, paint("#fff6d6"))
    rnd = random.Random(seed)
    for camada in range(3):
        base, hmin, hmax = ((700, 120, 330), (730, 160, 420), (770, 200, 540))[camada]
        x = -40 - rnd.uniform(0, 80)
        while x < W + 40:
            bw = rnd.uniform(60, 150) * (0.8 + 0.2 * camada)
            bh = rnd.uniform(hmin, hmax)
            if rnd.random() < 0.12 * camada:
                bh *= 0.45  # terreno em obra
            cor = rnd.choice(R["predios"] if camada == 2 else ["#e8487a", "#f08a2e", "#ff7eb6", "#d8584f", "#7a63e0"])
            cor = mix(cor, (R["ceu3"], R["ceu1"], cor)[camada], (0.6, 0.35, 0.0)[camada])
            c.drawRect(skia.Rect.MakeLTRB(x, base - bh, x + bw - 6, base + 400), paint(cor))
            if camada == 2:
                c.drawRect(skia.Rect.MakeLTRB(x + bw - 26, base - bh, x + bw - 6, base + 400), paint(INK, 0.22))
                c.drawRect(skia.Rect.MakeLTRB(x, base - bh, x + bw - 6, base - bh + 8), paint("#ffffff", 0.25))
                if rnd.random() < 0.25:  # antena no topo
                    c.drawRect(skia.Rect.MakeLTRB(x + bw / 2 - 2, base - bh - 40, x + bw / 2 + 2, base - bh), paint(cor))
                    c.drawCircle(x + bw / 2, base - bh - 42, 4, paint(CORAL, 0.6 + 0.4 * math.sin(t * 4 + x)))
            if camada > 0:
                jan = 0.95 if camada == 2 else 0.4
                for yy in range(int(base - bh + 18), base - 8, 24 if camada == 2 else 18):
                    for xx in range(int(x + 10), int(x + bw - 30), 20 if camada == 2 else 15):
                        if rnd.random() < 0.5:
                            c.drawRRect(rr(xx, yy, 9 if camada == 2 else 6, 12 if camada == 2 else 8, 2),
                                        paint(R["janela"], jan * rnd.uniform(0.55, 1) * luzes))
            x += bw
        if camada == 1:
            c.drawRect(skia.Rect.MakeWH(W, H), paint(R["ceu2"], 0.10))
            for gx, gh in ((420, 430), (1560, 380)):
                _guindaste(c, gx, 740, gh, mix(R["fundo"], INK, 0.3), t)
    # avenida com faróis andando
    c.drawRect(skia.Rect.MakeLTRB(0, 770, W, H), linear(0, 770, 0, H, ["#3a3f9a", R["estrada"]]))
    c.drawRect(skia.Rect.MakeLTRB(0, 770, W, 776), paint(R["ceu2"], 0.7))
    if cinza:
        c.drawRect(skia.Rect.MakeLTRB(0, 0, W, 770), paint("#5a6aa8", 0.45 * cinza))
    for faixa, (y, v, cor) in enumerate(((830, 260, R["farol"]), (890, -320, CORAL), (960, 380, R["farol"]), (1030, -280, CORAL))):
        if transito <= 0:
            break
        rnd2 = random.Random(faixa)
        for k in range(12):
            xx = (k * 190 + rnd2.uniform(0, 120) + v * t) % (W + 200) - 100
            c.drawRRect(rr(xx, y, 46, 7, 3), paint(cor, 0.95 * transito))
            glow(c, xx + 23, y + 3, 30, cor, 0.4 * transito)
    for k in range(12):
        c.drawRect(skia.Rect.MakeXYWH(k * 200 + (t * 120) % 200 - 200, 925, 90, 4), paint(BONE, 0.45))


def rotulo(c, s, x, y, cor=CYAN, a=1.0, size=30, fg=None, align="center"):
    """etiqueta em pílula colorida (texto curto: nome de uma parte, número). y = centro"""
    if a <= 0:
        return
    fg = fg or (INK if cor in (CYAN, AMBER, SKY, BONE) else "#ffffff")
    w = text_w(s, size, "display", 700) + size * 1.1
    h = size * 1.55
    x0 = x - w / 2 if align == "center" else x
    sc = 0.85 + 0.15 * ease_back(clamp(a))
    c.save()
    c.translate(x0 + w / 2, y)
    c.scale(sc, sc)
    c.drawRRect(rr(-w / 2 + 3, -h / 2 + 5, w, h, h / 2), paint(INK, 0.35 * a))
    c.drawRRect(rr(-w / 2, -h / 2, w, h, h / 2), paint(cor, a))
    text(c, s, 0, size * 0.36, size, "display", 700, fg, a, "center")
    c.restore()


# =====================================================================
# PEÇAS GERAIS PARA AS CENAS
# =====================================================================
def fundo(c, cima, baixo):
    c.drawRect(skia.Rect.MakeWH(W, H), linear(0, 0, 0, H, [cima, baixo]))


def titulo(c, s, x, y, size, cor=BONE, a=1.0, fam="display", wght=800, sombra=True, align="center"):
    """texto grande que entra com um pulinho (a = progresso 0..1 da entrada)"""
    if a <= 0:
        return
    sc = 0.6 + 0.4 * ease_back(clamp(a))
    c.save()
    c.translate(x, y)
    c.scale(sc, sc)
    if sombra:
        text(c, s, 4, 6, size, fam, wght, "#070c38", 0.35 * clamp(a * 2), align)
    text(c, s, 0, 0, size, fam, wght, cor, clamp(a * 2), align)
    c.restore()


def pop(a):
    """escala de entrada com pulinho (0..1 → ~0..1 passando de 1)"""
    return ease_back(clamp(a)) if a > 0 else 0.0


def estrelas(c, t, seed=4, n=160, a=1.0, rect=(0, 0, W, H)):
    rnd = random.Random(seed)
    x0, y0, x1, y1 = rect
    for _ in range(n):
        x, y, r, ph = rnd.uniform(x0, x1), rnd.uniform(y0, y1), rnd.uniform(0.8, 2.4), rnd.uniform(0, 6.3)
        c.drawCircle(x, y, r, paint(BONE, a * (0.45 + 0.55 * (0.5 + 0.5 * math.sin(t * 1.7 + ph)))))


def relogio(c, cx, cy, r, ang, a=1.0, velocidade=0.0, t=0.0):
    """relógio de museu: ang = ângulo do ponteiro grande (rad); o pequeno anda 1/12"""
    if a <= 0:
        return
    c.save()
    c.translate(cx, cy)
    sc = pop(a)
    c.scale(sc, sc)
    glow(c, 0, 0, r * 1.6, AMBER, 0.35)
    c.drawCircle(0, 0, r + 14, paint(VAULT))
    c.drawCircle(0, 0, r + 14, paint(AMBER, stroke=6))
    c.drawCircle(0, 0, r, paint(BONE))
    for k in range(60):
        an = 2 * math.pi * k / 60
        l = 18 if k % 5 == 0 else 8
        c.drawLine(math.sin(an) * (r - 10), -math.cos(an) * (r - 10), math.sin(an) * (r - 10 - l), -math.cos(an) * (r - 10 - l),
                   paint(INK, stroke=5 if k % 5 == 0 else 2))
    if velocidade > 0:  # rastro de movimento do ponteiro
        for k in range(1, 7):
            an = ang - k * 0.07 * min(1, velocidade)
            c.drawLine(0, 0, math.sin(an) * r * 0.78, -math.cos(an) * r * 0.78, paint(CORAL, 0.12 * (7 - k) / 7, stroke=9))
    ah = ang / 12
    c.drawLine(0, 0, math.sin(ah) * r * 0.5, -math.cos(ah) * r * 0.5, paint(INK, stroke=12))
    c.drawLine(0, 0, math.sin(ang) * r * 0.8, -math.cos(ang) * r * 0.8, paint(CORAL, stroke=7))
    c.drawCircle(0, 0, 12, paint(INK))
    c.drawCircle(0, 0, 5, paint(AMBER))
    c.restore()


CONTINENTES = [  # formas simples em coordenadas de esfera (lon, lat) em graus
    [(-160, 60), (-130, 70), (-90, 72), (-60, 55), (-75, 40), (-95, 28), (-110, 25), (-125, 40), (-150, 58)],
    [(-80, 10), (-60, 8), (-35, -8), (-40, -22), (-58, -38), (-70, -52), (-75, -20), (-80, -2)],
    [(-15, 35), (10, 37), (35, 30), (50, 12), (40, -15), (30, -34), (18, -34), (8, -5), (-15, 12)],
    [(-10, 43), (5, 50), (30, 70), (90, 75), (140, 70), (160, 60), (130, 40), (120, 22), (100, 10), (80, 22), (60, 25), (40, 40), (20, 40)],
    [(115, -20), (135, -12), (150, -22), (150, -38), (130, -32), (115, -33)],
    [(-50, 62), (-30, 70), (-22, 78), (-45, 82), (-60, 76)],
]


def globo(c, cx, cy, r, rot=0.0, a=1.0, oceano=SKY, terra="#3fd17a", noite=0.0):
    """Terra simples: oceano, continentes girando (rot em graus), brilho da atmosfera"""
    if a <= 0:
        return
    c.saveLayerAlpha(None, int(255 * clamp(a)))
    glow(c, cx, cy, r * 1.35, SKY, 0.5)
    esf = skia.Path()
    esf.addCircle(cx, cy, r)
    c.drawPath(esf, paint(oceano))
    c.save()
    c.clipPath(esf, doAntiAlias=True)
    for cont in CONTINENTES:
        pts, vis = [], 0
        for lon, lat in cont:
            lo = math.radians(lon + rot)
            la = math.radians(lat)
            z = math.cos(la) * math.cos(lo)
            vis += z > 0
            pts.append((cx + r * math.cos(la) * math.sin(lo), cy - r * math.sin(la)))
        if vis >= len(cont) // 2:
            path = skia.Path()
            path.moveTo(*pts[0])
            for k in range(1, len(pts)):
                mx, my = (pts[k - 1][0] + pts[k][0]) / 2, (pts[k - 1][1] + pts[k][1]) / 2
                path.quadTo(pts[k - 1][0], pts[k - 1][1], mx, my)
            path.close()
            c.drawPath(path, paint(terra))
    c.drawCircle(cx + r * 0.35, cy + r * 0.3, r * 1.05, paint(INK, 0.28 + 0.5 * noite))
    c.drawCircle(cx - r * 0.35, cy - r * 0.4, r * 0.35, paint("#ffffff", 0.12))
    c.restore()
    c.drawCircle(cx, cy, r, paint("#ffffff", 0.5, stroke=3))
    c.restore()


def camadas(c, x0, y0, x1, y1, cores, seed=1, onda=6.0, alturas=None):
    """faixas de rocha/sedimento horizontais com borda ondulada; devolve as linhas (y) de cada faixa"""
    rnd = random.Random(seed)
    n = len(cores)
    alt = alturas or [1.0] * n
    tot = sum(alt)
    y = y0
    limites = []
    for k, cor in enumerate(cores):
        h = (y1 - y0) * alt[k] / tot
        p = skia.Path()
        p.moveTo(x0, y)
        xs = 12
        for i in range(xs + 1):
            p.lineTo(x0 + (x1 - x0) * i / xs, y + (rnd.uniform(-onda, onda) if 0 < k else 0))
        p.lineTo(x1, y1)
        p.lineTo(x0, y1)
        p.close()
        c.drawPath(p, paint(cor))
        limites.append((y, y + h))
        y += h
    return limites


def arvore(c, x, y, s=1.0, cor="#3fd17a", a=1.0):
    if a <= 0:
        return
    k = pop(a)
    c.drawRect(skia.Rect.MakeLTRB(x - 5 * s, y - 40 * s * k, x + 5 * s, y), paint("#8a4b2f"))
    c.drawCircle(x, y - 52 * s * k, 30 * s * k, paint(cor))
    c.drawCircle(x - 14 * s * k, y - 44 * s * k, 20 * s * k, paint(mix(cor, "#ffffff", 0.15)))
    c.drawCircle(x + 10 * s * k, y - 62 * s * k, 14 * s * k, paint(mix(cor, INK, 0.2)))


PELE = ["#f6c49a", "#d99a6c", "#a8673f", "#7a4a2c", "#f1b38a"]


def pessoa(c, x, y, s=1.0, roupa=CORAL, pele=PELE[0], capacete=None, braco=0.0, a=1.0, cabelo="#3a2416", olhar=1):
    """pessoa simples, chapada (pés em x, y); braco = ângulo do braço direito (0 = abaixado)"""
    if a <= 0:
        return
    c.saveLayerAlpha(None, int(255 * clamp(a)))
    c.save()
    c.translate(x, y)
    c.scale(s * olhar, s)
    c.drawOval(oval(0, 0, 34, 6), paint(INK, 0.3))
    for lx in (-11, 11):
        c.drawRRect(rr(lx - 6, -58, 12, 58, 6), paint(mix(roupa, INK, 0.45)))
    c.save()
    c.translate(16, -112)
    c.rotate(-math.degrees(braco))
    c.drawRRect(rr(-6, 0, 12, 48, 6), paint(mix(roupa, INK, 0.15)))
    c.drawCircle(0, 50, 7, paint(pele))
    c.restore()
    c.drawRRect(rr(-22, -122, 44, 70, 18), paint(roupa))
    c.drawRRect(rr(-26, -110, 10, 46, 5), paint(mix(roupa, INK, 0.15)))
    c.drawCircle(0, -146, 22, paint(pele))
    c.drawCircle(8, -148, 3, paint(INK))
    if capacete:
        c.drawPath(_meia_lua(0, -150, 25), paint(capacete))
        c.drawRect(skia.Rect.MakeLTRB(-28, -152, 30, -147), paint(capacete))
    else:
        c.drawPath(_meia_lua(0, -150, 23), paint(cabelo))
    c.restore()
    c.restore()


def _meia_lua(cx, cy, r):
    p = skia.Path()
    p.addArc(skia.Rect.MakeLTRB(cx - r, cy - r, cx + r, cy + r), 180, 180)
    p.close()
    return p


def icone(c, nome, cx, cy, s=1.0, cor=None, a=1.0):
    """ícones chapados (tamanho base ~80 px): carro celular garrafa predio arvore pessoa foto carta livro musica
    arquivo duvida privada xicara azulejo osso frango filme capsula check xis"""
    if a <= 0:
        return
    k = pop(a)
    c.save()
    c.translate(cx, cy)
    c.scale(s * k, s * k)
    P = lambda col, al=1.0: paint(col, al * clamp(a * 2))
    cor = cor or SKY
    if nome == "carro":
        c.drawRRect(rr(-40, -10, 80, 26, 8), P(cor))
        c.drawRRect(rr(-24, -28, 46, 22, 8), P(mix(cor, "#ffffff", 0.2)))
        c.drawRRect(rr(-18, -24, 34, 14, 4), P("#bfe6ff"))
        for wx in (-24, 24):
            c.drawCircle(wx, 18, 10, P(INK))
            c.drawCircle(wx, 18, 4, P("#cfd6ff"))
    elif nome == "celular":
        c.drawRRect(rr(-22, -40, 44, 80, 9), P("#1c232c"))
        c.drawRRect(rr(-17, -32, 34, 62, 5), P(cor))
    elif nome == "garrafa":
        c.drawRRect(rr(-16, -26, 32, 62, 10), P(cor, 0.85))
        c.drawRRect(rr(-7, -42, 14, 20, 4), P(cor, 0.85))
        c.drawRRect(rr(-9, -48, 18, 8, 3), P("#3a7bd5"))
        c.drawRect(skia.Rect.MakeLTRB(-16, -4, 16, 10), P(CORAL))
    elif nome == "predio":
        c.drawRect(skia.Rect.MakeLTRB(-26, -44, 26, 40), P(cor))
        for yy in range(-36, 32, 14):
            for xx in (-16, 4):
                c.drawRect(skia.Rect.MakeXYWH(xx, yy, 10, 8), P("#fff1a8"))
    elif nome == "arvore":
        c.drawRect(skia.Rect.MakeLTRB(-5, 0, 5, 40), P("#8a4b2f"))
        c.drawCircle(0, -12, 30, P("#3fd17a"))
    elif nome == "pessoa":
        c.drawCircle(0, -26, 14, P(PELE[1]))
        c.drawRRect(rr(-20, -8, 40, 48, 16), P(cor))
    elif nome == "foto":
        c.rotate(-6)
        c.drawRect(skia.Rect.MakeLTRB(-32, -36, 32, 36), P("#ffffff"))
        c.drawRect(skia.Rect.MakeLTRB(-26, -30, 26, 18), P(SKY))
        c.drawPath(poly([(-26, 18), (-6, -8), (8, 6), (16, -2), (26, 18)]), P("#3fd17a"))
        c.drawCircle(14, -18, 6, P(AMBER))
    elif nome == "carta":
        c.drawRect(skia.Rect.MakeLTRB(-38, -24, 38, 26), P("#fff6e8"))
        c.drawPath(poly([(-38, -24), (0, 6), (38, -24)], close=False), paint("#d8b98a", stroke=3))
        c.drawCircle(24, 12, 7, P(CORAL))
    elif nome == "livro":
        c.drawRRect(rr(-28, -36, 56, 72, 4), P(cor))
        c.drawRect(skia.Rect.MakeLTRB(-28, -36, -20, 36), P(mix(cor, INK, 0.3)))
        c.drawRect(skia.Rect.MakeLTRB(-12, -18, 20, -12), P("#ffffff", 0.7))
    elif nome == "musica":
        c.drawCircle(-14, 22, 12, P(cor))
        c.drawCircle(20, 14, 12, P(cor))
        c.drawRect(skia.Rect.MakeLTRB(-6, -30, -2, 22), P(cor))
        c.drawRect(skia.Rect.MakeLTRB(28, -38, 32, 14), P(cor))
        c.drawPath(poly([(-6, -30), (32, -38), (32, -26), (-6, -18)]), P(cor))
    elif nome == "arquivo":
        c.drawPath(poly([(-26, -36), (12, -36), (26, -22), (26, 36), (-26, 36)]), P("#ffffff"))
        c.drawPath(poly([(12, -36), (12, -22), (26, -22)]), P("#cfd6ff"))
        for yy in (-10, 2, 14):
            c.drawRect(skia.Rect.MakeLTRB(-16, yy, 16, yy + 5), P(cor))
    elif nome == "duvida":
        c.drawCircle(0, 0, 36, P(cor))
        text(c, "?", 0, 18, 52, "display", 800, "#ffffff", clamp(a * 2), "center")
    elif nome == "privada":
        c.drawRRect(rr(-30, -46, 26, 40, 6), P("#ffffff"))
        c.drawPath(poly([(-34, -6), (34, -6), (28, 12), (12, 20), (16, 40), (-16, 40), (-12, 20), (-28, 12)]), P("#ffffff"))
        c.drawOval(oval(0, -6, 34, 7), P("#dfe6ff"))
    elif nome == "xicara":
        c.drawPath(poly([(-28, -20), (24, -20), (18, 26), (-22, 26)]), P("#ffffff"))
        c.drawCircle(30, 0, 12, paint("#ffffff", clamp(a * 2), stroke=6))
        c.drawRect(skia.Rect.MakeLTRB(-26, -8, 22, 2), P(cor))
    elif nome == "azulejo":
        c.drawRect(skia.Rect.MakeLTRB(-32, -32, 32, 32), P("#ffffff"))
        c.drawCircle(0, 0, 18, P(SKY))
        c.drawCircle(0, 0, 8, P(AMBER))
    elif nome == "osso":
        c.rotate(-24)
        c.drawRRect(rr(-34, -6, 68, 12, 6), P(BONE))
        for ex in (-34, 34):
            c.drawCircle(ex, -6, 9, P(BONE))
            c.drawCircle(ex, 6, 9, P(BONE))
    elif nome == "frango":
        c.drawOval(oval(0, 6, 34, 26), P("#ffffff"))
        c.drawCircle(26, -18, 15, P("#ffffff"))
        c.drawPath(poly([(38, -20), (50, -16), (38, -12)]), P(AMBER))
        c.drawPath(poly([(22, -32), (26, -42), (30, -32)]), P(CORAL))
        c.drawCircle(30, -20, 3, P(INK))
        for lx in (-8, 8):
            c.drawRect(skia.Rect.MakeLTRB(lx - 2, 28, lx + 2, 42), P(AMBER))
    elif nome == "filme":
        c.drawCircle(0, 0, 36, P("#2a2f3a"))
        for k2 in range(6):
            an = k2 * math.pi / 3
            c.drawCircle(math.cos(an) * 20, math.sin(an) * 20, 7, P("#9fb4ff"))
        c.drawCircle(0, 0, 6, P(AMBER))
    elif nome == "capsula":
        c.drawRRect(rr(-16, -44, 32, 88, 14), P("#d9844a"))
        c.drawRect(skia.Rect.MakeLTRB(-16, -30, 16, -24), P("#a85a2c"))
        c.drawRRect(rr(-10, -40, 6, 70, 3), P("#ffffff", 0.3))
    elif nome == "check":
        c.drawCircle(0, 0, 32, P(CYAN))
        c.drawPath(poly([(-14, 0), (-4, 12), (16, -12)], close=False), paint("#ffffff", clamp(a * 2), stroke=8))
    elif nome == "xis":
        c.drawCircle(0, 0, 32, P(CORAL))
        c.drawLine(-12, -12, 12, 12, paint("#ffffff", clamp(a * 2), stroke=8))
        c.drawLine(12, -12, -12, 12, paint("#ffffff", clamp(a * 2), stroke=8))
    c.restore()


def carimbo(c, s, x, y, cor=CORAL, a=1.0, ang=-8, size=64):
    """carimbo que bate na tela (a = progresso)"""
    if a <= 0:
        return
    k = 1.8 - 0.8 * ease_out(clamp(a / 0.5)) if a < 0.5 else 1.0
    w = text_w(s, size, "display", 800) + size
    h = size * 1.5
    c.save()
    c.translate(x, y)
    c.rotate(ang)
    c.scale(k, k)
    al = clamp(a * 3)
    c.drawRRect(rr(-w / 2, -h / 2, w, h, 12), paint(cor, al, stroke=8))
    c.drawRRect(rr(-w / 2 + 12, -h / 2 + 12, w - 24, h - 24, 6), paint(cor, al * 0.5, stroke=3))
    text(c, s, 0, size * 0.36, size, "display", 800, cor, al, "center")
    c.restore()


def fonte(c, s, a=1.0):
    """crédito da fonte no canto inferior direito"""
    if a <= 0:
        return
    w = text_w(s, 18, "mono", 500) + 28
    c.drawRRect(rr(W - w - 40, H - 72, w, 34, 17), paint("#070c38", 0.55 * a))
    text(c, s, W - 40 - w / 2, H - 49, 18, "mono", 500, BONE, 0.9 * a, "center")
