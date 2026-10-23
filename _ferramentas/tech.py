"""Linguagem visual do canal TECNOLOGIA (futurista / HUD / neon). 1920x1080.

Uso no roteiro/visual.py:
    import tech                       # registra e ativa o tema "tech" no motor
    from motor import *
    from tech import *
    BACKGROUND, CAPTION, OVERLAY = tech.background, tech.caption, tech.overlay   # ganchos do render.py

Peças: fundo espacial com grade em perspectiva animada, órbitas de luz, partículas, scanlines e moldura HUD;
painéis de vidro com cantos chanfrados e borda neon; títulos HUD alinhados à esquerda; chips mono;
terminal com digitação; nós e conexões com pulsos de dados; legenda neon; tela de CTA própria.
"""
import math
from functools import lru_cache
import skia
import motor

# ---------------- tema ----------------
motor.TEMAS["tech"] = dict(
    BG="#04060D", CARD="#0A1222", INK="#EAF2FF", INK2="#A9B8D0", GRAY="#62708A", LIGHT="#2A3552",
    LINE="#18233D", GREEN="#4ADE80", RED="#FB7185", AMBER="#FBBF24", BLUE="#22D3EE", PURPLE="#A78BFA",
    BG_GRAD=("#0B1430", "#03050B"), ARC=("#FFFFFF", 0.0), SHADOW_K=3.0, CARD_STROKE="#1E2A4A")
motor.set_theme("tech")
# fonte mono (Consolas do Windows): o motor junta FONTES / nome -> caminho absoluto funciona
motor.PESOS["mono"] = "C:/Windows/Fonts/consola"
motor.PESOS["monob"] = "C:/Windows/Fonts/consolab"

from motor import W, H, ep, prog, clamp, lerp, mix, ease_out, ease_io, ease_back, text, text_mid, text_w, paint, hexc, \
    rrect, line, arrow, check_icon, chunk_tokens, _layout  # noqa: E402

CYAN = "#22D3EE"
VIOLET = "#A78BFA"
MAGENTA = "#F472B6"
LIME = "#4ADE80"
ROSE = "#FB7185"
GOLD = "#FBBF24"
INK = motor.INK
INK2 = motor.INK2
DIM = "#62708A"
PANEL = "#0A1222"
SERIE = "TECH//001"


# ---------------- utilidades ----------------
def blur_paint(color, a, sigma, stroke=None):
    p = paint(color, a, stroke=stroke, cap_round=True)
    p.setMaskFilter(skia.MaskFilter.MakeBlur(skia.kNormal_BlurStyle, sigma))
    return p


def glow_text(c, s, x, y, size, peso="black", color=CYAN, a=1.0, align="center", glow=0.55, sigma=None):
    """texto com halo neon (y = linha de base)"""
    if a <= 0:
        return 0
    f = motor.font(peso, size)
    w = f.measureText(s)
    xx = x - w / 2 if align == "center" else x - w if align == "right" else x
    if glow > 0:
        c.drawString(s, xx, y, f, blur_paint(color, a * glow, sigma or max(6, size * 0.16)))
    c.drawString(s, xx, y, f, paint(color, a))
    return w


def glow_line(c, x0, y0, x1, y1, color, a=1.0, width=3, progress=1.0, glow=0.6):
    if a <= 0 or progress <= 0:
        return
    xe, ye = lerp(x0, x1, progress), lerp(y0, y1, progress)
    c.drawLine(x0, y0, xe, ye, blur_paint(color, a * glow, 6, stroke=width * 3))
    c.drawLine(x0, y0, xe, ye, paint(color, a, stroke=width, cap_round=True))


def chamfer_path(x, y, w, h, k):
    """retângulo com cantos superior-esquerdo e inferior-direito cortados"""
    p = skia.Path()
    p.moveTo(x + k, y); p.lineTo(x + w, y); p.lineTo(x + w, y + h - k)
    p.lineTo(x + w - k, y + h); p.lineTo(x, y + h); p.lineTo(x, y + k); p.close()
    return p


def reveal(t, t0, d=0.55):
    """alpha + deslocamento para entrada"""
    a = ep(t, t0, d)
    return a, (1 - a) * 22


def hash01(i, k=0):
    v = math.sin(i * 12.9898 + k * 78.233) * 43758.5453
    return v - math.floor(v)


# ---------------- fundo ----------------
@lru_cache(None)
def _base():
    s = skia.Surface(W, H)
    c = s.getCanvas()
    c.clear(hexc(motor.BG))
    sh = skia.GradientShader.MakeRadial(center=(W * 0.5, H * 0.18), radius=W * 0.8,
                                        colors=[hexc("#0E1A3A"), hexc("#060A18"), hexc("#03050B")], positions=[0, 0.5, 1])
    p = skia.Paint(AntiAlias=True); p.setShader(sh)
    c.drawRect(skia.Rect.MakeWH(W, H), p)
    # matriz de pontos (metade de cima)
    for gy in range(40, 640, 36):
        for gx in range(20, W, 36):
            fade = 1 - gy / 640
            c.drawCircle(gx, gy, 1.3, paint("#7DD3FC", 0.10 * fade))
    return s.makeImageSnapshot()


@lru_cache(None)
def _orb(color, r):
    size = int(r * 3)
    s = skia.Surface(size, size)
    c = s.getCanvas()
    c.clear(skia.ColorTRANSPARENT)
    c.drawCircle(size / 2, size / 2, r, blur_paint(color, 0.28, r * 0.45))
    return s.makeImageSnapshot()


@lru_cache(None)
def _over():
    s = skia.Surface(W, H)
    c = s.getCanvas()
    c.clear(skia.ColorTRANSPARENT)
    for y in range(0, H, 4):
        c.drawRect(skia.Rect.MakeXYWH(0, y, W, 1), paint("#000000", 0.10))
    sh = skia.GradientShader.MakeRadial(center=(W / 2, H / 2), radius=W * 0.72,
                                        colors=[hexc("#000000", 0.0), hexc("#000000", 0.0), hexc("#000000", 0.55)],
                                        positions=[0, 0.62, 1])
    p = skia.Paint(AntiAlias=True); p.setShader(sh)
    c.drawRect(skia.Rect.MakeWH(W, H), p)
    return s.makeImageSnapshot()


def _grid(c, t):
    hz, vx = 690, W / 2              # horizonte e ponto de fuga
    bottom = H
    col = CYAN
    # linhas que convergem
    for k in range(-14, 15):
        xb = vx + k * 190
        a = 0.16 * (1 - abs(k) / 16)
        g = skia.Paint(AntiAlias=True, StrokeWidth=1.4, Style=skia.Paint.kStroke_Style)
        g.setShader(skia.GradientShader.MakeLinear(points=[(vx, hz), (xb, bottom)],
                                                   colors=[hexc(col, 0.0), hexc(col, a)]))
        c.drawLine(vx + k * 14, hz, xb, bottom, g)
    # linhas horizontais rolando em direção à câmera
    sp = (t * 0.35) % 1.0
    for i in range(14):
        u = (i + sp) / 14
        y = hz + (bottom - hz) * u ** 2.2
        c.drawLine(0, y, W, y, paint(col, 0.14 * u ** 1.2, stroke=1.2))
    # brilho no horizonte
    c.drawRect(skia.Rect.MakeXYWH(0, hz - 2, W, 4), blur_paint(VIOLET, 0.35, 10))


def _particles(c, t):
    for i in range(46):
        x = hash01(i, 1) * W + math.sin(t * 0.3 + i) * 12
        sp = 8 + 22 * hash01(i, 2)
        y = H - ((hash01(i, 3) * H + t * sp) % (H + 40))
        r = 0.8 + 1.8 * hash01(i, 4)
        col = CYAN if i % 3 else VIOLET
        tw = 0.35 + 0.65 * (0.5 + 0.5 * math.sin(t * (1 + hash01(i, 5) * 2) + i))
        c.drawCircle(x, y, r, paint(col, 0.55 * tw))


def background(c, t=0.0):
    c.drawImage(_base(), 0, 0)
    o1, o2 = _orb(CYAN, 380), _orb(VIOLET, 420)
    c.drawImage(o1, -300 + 60 * math.sin(t * 0.11), -420 + 40 * math.cos(t * 0.13))
    c.drawImage(o2, W - 900 + 70 * math.cos(t * 0.09), H - 1000 + 50 * math.sin(t * 0.12))
    _grid(c, t)
    _particles(c, t)
    c.drawImage(_over(), 0, 0)


def _bracket(c, x, y, dx, dy, col, a, n=34):
    c.drawLine(x, y, x + dx * n, y, paint(col, a, stroke=3))
    c.drawLine(x, y, x, y + dy * n, paint(col, a, stroke=3))


def overlay(c, t):
    """moldura HUD por cima de tudo"""
    a = 0.75
    m = 34
    for x, y, dx, dy in ((m, m, 1, 1), (W - m, m, -1, 1), (m, H - m, 1, -1), (W - m, H - m, -1, -1)):
        _bracket(c, x, y, dx, dy, CYAN, a * 0.8)
    blink = 0.4 + 0.6 * (0.5 + 0.5 * math.sin(t * 4))
    mm, ss = divmod(t, 60)
    tw = text(c, f"T+{int(mm):02d}:{ss:05.2f}", W - m - 20, m + 38, 22, "mono", CYAN, 0.8, align="right")
    sw = text(c, SERIE + "  ·", W - m - 34 - tw, m + 38, 22, "monob", INK2, 0.8, align="right")
    c.drawCircle(W - m - 52 - tw - sw, m + 30, 6, paint(ROSE, blink))
    # barra de progresso fina embaixo
    text(c, "SYS.ONLINE", m + 20, H - m - 14, 18, "mono", DIM, 0.8, align="left")


# ---------------- componentes ----------------
def panel(c, x, y, w, h, a=1.0, col=CYAN, k=24, fill=0.78, label=None, glow=True):
    """painel de vidro escuro com cantos chanfrados e borda neon"""
    if a <= 0:
        return
    p = chamfer_path(x, y, w, h, k)
    if glow:
        c.drawPath(p, blur_paint(col, 0.10 * a, 24, stroke=10))
    c.drawPath(p, paint(PANEL, fill * a))
    g = skia.Paint(AntiAlias=True, StrokeWidth=1.6, Style=skia.Paint.kStroke_Style)
    g.setShader(skia.GradientShader.MakeLinear(points=[(x, y), (x + w, y + h)],
                                               colors=[hexc(col, 0.85 * a), hexc(col, 0.18 * a), hexc(col, 0.6 * a)],
                                               positions=[0, 0.55, 1]))
    c.drawPath(p, g)
    # acentos nos cantos cortados
    c.drawLine(x, y + k, x + k, y, paint(col, a, stroke=4, cap_round=True))
    c.drawLine(x + w - k, y + h, x + w, y + h - k, paint(col, a, stroke=4, cap_round=True))
    if label:
        tw = text_w(label, "monob", 20) + 28
        c.drawPath(chamfer_path(x + k + 10, y - 15, tw, 30, 8), paint(col, a))
        text_mid(c, label, x + k + 10 + tw / 2, y, 20, "monob", "#03050B", a)


def chip(c, s, x, cy, col=CYAN, a=1.0, anchor="left", size=24, filled=False, peso="monob"):
    if a <= 0:
        return (x, x)
    tw = text_w(s, peso, size)
    w, h = tw + size * 1.3, size * 1.7
    x0 = x if anchor == "left" else x - w / 2 if anchor == "center" else x - w
    p = chamfer_path(x0, cy - h / 2, w, h, h * 0.32)
    if filled:
        c.drawPath(p, blur_paint(col, 0.35 * a, 10))
        c.drawPath(p, paint(col, a))
        text_mid(c, s, x0 + w / 2, cy, size, peso, "#03050B", a)
    else:
        c.drawPath(p, paint(col, 0.12 * a))
        c.drawPath(p, paint(col, 0.9 * a, stroke=1.6))
        text_mid(c, s, x0 + w / 2, cy, size, peso, col, a)
    return (x0, x0 + w)


def head(c, t, t0, kicker, title, col=CYAN, t_out=None, x=150, y=118):
    """título HUD à esquerda: '// KICKER' mono + título grande + traço neon"""
    a = ep(t, t0, 0.5)
    if t_out is not None:
        a *= 1 - prog(t, t_out, 0.35)
    if a <= 0:
        return
    dx = (1 - a) * -30
    text(c, "// " + kicker, x + dx, y - 34, 24, "monob", col, a, align="left", tracking=2)
    tw = glow_text(c, title, x + dx, y + 30, 52, "black", INK, a, align="left", glow=0.18)
    glow_line(c, x, y + 52, x + tw + 60, y + 52, col, a, 3, progress=ep(t, t0 + 0.2, 0.7))
    c.drawRect(skia.Rect.MakeXYWH(x + tw + 70, y + 49, 14, 6), paint(col, a * (0.5 + 0.5 * math.sin(t * 6))))


def terminal(c, x, y, w, h, a=1.0, title="bash", col=CYAN):
    if a <= 0:
        return
    panel(c, x, y, w, h, a, col, k=18, fill=0.9)
    c.drawLine(x + 18, y + 54, x + w, y + 54, paint(col, 0.25 * a, stroke=1.2))
    for i, cc in enumerate((ROSE, GOLD, LIME)):
        c.drawCircle(x + 44 + i * 30, y + 28, 8, paint(cc, a))
    text_mid(c, title, x + w / 2, y + 28, 22, "mono", DIM, a)


def typed(c, s, x, y, size, t, t0, cps=26, col=INK, a=1.0, peso="mono", cursor=True, prompt=None, prompt_col=LIME):
    """digitação mono; retorna fração digitada"""
    if a <= 0 or t < t0:
        return 0.0
    n = int(clamp((t - t0) * cps, 0, len(s)))
    xx = x
    if prompt:
        xx += text(c, prompt + " ", x, y, size, peso, prompt_col, a, align="left")
    w = text(c, s[:n], xx, y, size, peso, col, a, align="left")
    if cursor and (n < len(s) or math.sin(t * 7) > 0):
        c.drawRect(skia.Rect.MakeXYWH(xx + w + 4, y - size * 0.78, size * 0.55, size * 0.95), paint(CYAN, a * 0.9))
    return n / max(1, len(s))


def node(c, cx, cy, r, label, sub=None, col=CYAN, a=1.0, t=0.0, glyph=None, gsize=None):
    """nó hexagonal com halo pulsante"""
    if a <= 0:
        return
    s = 0.7 + 0.3 * ease_back(clamp(a))
    p = skia.Path()
    for i in range(6):
        ang = math.pi / 6 + i * math.pi / 3
        px, py = cx + r * s * math.cos(ang), cy + r * s * math.sin(ang)
        (p.moveTo if i == 0 else p.lineTo)(px, py)
    p.close()
    pulse = 0.5 + 0.5 * math.sin(t * 2.2 + cx * 0.01)
    c.drawPath(p, blur_paint(col, (0.25 + 0.2 * pulse) * a, 22))
    c.drawPath(p, paint(PANEL, 0.95 * a))
    c.drawPath(p, paint(col, a, stroke=3))
    if glyph:
        glow_text(c, glyph, cx, cy + (gsize or r * 0.5) * 0.36, gsize or r * 0.5, "black", col, a, glow=0.5)
    if label:
        text(c, label, cx, cy + r + 52, 34, "extrabold", INK, a)
    if sub:
        text(c, sub, cx, cy + r + 90, 24, "mono", DIM, a)


def link(c, x0, y0, x1, y1, col=CYAN, a=1.0, t=0.0, progress=1.0, pulses=3, speed=0.45, dash=False):
    """conexão com pulsos de dados viajando"""
    if a <= 0 or progress <= 0:
        return
    xe, ye = lerp(x0, x1, progress), lerp(y0, y1, progress)
    p = paint(col, 0.35 * a, stroke=2.2)
    if dash:
        p.setPathEffect(skia.DashPathEffect.Make([10, 8], -t * 40))
    c.drawLine(x0, y0, xe, ye, p)
    if progress >= 1:
        for k in range(pulses):
            u = (t * speed + k / pulses) % 1.0
            x, y = lerp(x0, x1, u), lerp(y0, y1, u)
            c.drawCircle(x, y, 9, blur_paint(col, 0.7 * a, 6))
            c.drawCircle(x, y, 4, paint("#FFFFFF", a))


def bar_meter(c, x, y, w, h, frac, col=CYAN, a=1.0):
    rrect(c, x, y, w, h, h / 2, "#111A30", a)
    if frac > 0:
        rrect(c, x, y, w * frac, h, h / 2, col, a)
        c.drawRect(skia.Rect.MakeXYWH(x, y, w * frac, h), blur_paint(col, 0.4 * a, 8))


def code_lines(c, lines, x, y, size, t, t0, step=0.18, lh=None, a=1.0):
    """linhas de código (lista de [(texto, cor), ...]) aparecendo uma a uma"""
    lh = lh or size * 1.45
    for i, segs in enumerate(lines):
        ai = ep(t, t0 + i * step, 0.3) * a
        if ai <= 0:
            continue
        xx = x
        for s, col in segs:
            xx += text(c, s, xx, y + i * lh, size, "mono", col, ai, align="left")


# ---------------- legenda ----------------
CAP_Y = 968


def caption(c, scene, t):
    lt = t - scene["start"]
    chunks = scene.setdefault("_chunks", chunk_tokens(scene["tokens"]))
    if not chunks:
        return
    for i, ch in enumerate(chunks):
        s = ch[0]["t0"] - 0.12
        e = chunks[i + 1][0]["t0"] - 0.12 if i + 1 < len(chunks) else scene["dur"] - 0.15
        if s <= lt < e:
            break
    else:
        return
    out = 1 - prog(lt, e - 0.22, 0.22)
    lines, sp = _layout(ch)
    lh = 62
    y0 = CAP_Y - (len(lines) - 1) * lh / 2
    for li, (ws, lw) in enumerate(lines):
        x = W / 2 - lw / 2
        y = y0 + li * lh
        for tk, peso, size, ww in ws:
            a = prog(lt, tk["t0"] - 0.06, 0.25)
            if a > 0:
                f = ease_out(a)
                if tk["bold"]:
                    glow_text(c, tk["disp"], x, y + (1 - f) * 10, size, peso, CYAN, f * out, align="left", glow=0.45)
                else:
                    text(c, tk["disp"], x, y + (1 - f) * 10, size, peso, mix("#3A4766", INK, f), f * out, align="left")
            x += ww + sp


# ---------------- CTA ----------------
LIKE, BELL, CHAT = "\ue8e1", "\uea8f", "\ue90a"


def cta(c, t, like, sub, bell, com, bye, pergunta, despedida="Até o próximo vídeo!"):
    y = 250
    items = [(like, 330, CYAN, LIKE, "CURTIR"), (sub, 790, ROSE, None, "INSCREVA-SE"), (bell, 1250, GOLD, BELL, "SININHO")]
    for k, (t0, x, col, gl, lab) in enumerate(items):
        a = ep(t, t0 - 0.2, 0.5)
        if a <= 0:
            continue
        on = ep(t, t0 + 0.4, 0.3)
        panel(c, x, y + (1 - a) * 20, 340, 330, a, col if on > 0.5 else DIM, label=f"0{k + 1}")
        cx, cy = x + 170, y + 140 + (1 - a) * 20
        if gl:
            c.save()
            if gl == BELL:
                ring = prog(t, t0 + 0.4, 1.4)
                c.translate(cx, cy - 50); c.rotate(18 * math.sin(ring * math.pi * 6) * (1 - ring)); c.translate(-cx, -(cy - 50))
            motor.icon(c, gl, cx, cy, 120, p=blur_paint(col, 0.6 * on * a, 14))
            motor.icon(c, gl, cx, cy, 120, p=paint(mix(INK2, col, on), a))
            c.restore()
        else:
            press = math.sin(math.pi * prog(t, t0 + 1.1, 0.35))
            done = ep(t, t0 + 1.3, 0.3)
            chip(c, "INSCRITO" if done > 0.5 else "INSCREVA-SE", cx, cy + 10, col, a, anchor="center",
                 size=34 * (1 - 0.05 * press), filled=done <= 0.5)
        glow_text(c, lab, cx, y + 290 + (1 - a) * 20, 30, "monob", mix(INK2, col, on), a, glow=0.3 * on)
    a = ep(t, com, 0.5) * (1 - prog(t, bye, 0.4))
    if a > 0:
        w = max(1100, text_w(pergunta, "bold", 38) + 240)
        yy = 650 + (1 - a) * 20
        panel(c, W / 2 - w / 2, yy, w, 130, a, VIOLET)
        motor.icon(c, CHAT, W / 2 - w / 2 + 90, yy + 65, 56, p=paint(VIOLET, a))
        text_mid(c, pergunta, W / 2 + 40, yy + 65, 38, "bold", INK, a)
    ab = ep(t, bye, 0.6)
    if ab > 0:
        glow_text(c, despedida, W / 2, 770 + (1 - ab) * 20, 76, "black", INK, ab, glow=0.25)
        glow_line(c, W / 2 - 300, 800, W / 2 + 300, 800, CYAN, ab, 3, progress=ep(t, bye + 0.3, 0.8))
