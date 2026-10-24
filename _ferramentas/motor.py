"""Motor de renderização dos vídeos do canal (estilo claro/minimalista, 1920x1080).

Fornece: paleta, fontes, easing, primitivas (cartões, pílulas, ícones), legenda cinética
sincronizada com a narração e um desenhador de gráficos de candles.
"""
import math
from functools import lru_cache
from pathlib import Path
import os
import skia

# VIDEO_FORMATO=vertical (render.py --vertical): Shorts 1080x1920
W, H = (1080, 1920) if os.environ.get("VIDEO_FORMATO") == "vertical" else (1920, 1080)
FPS = 30
FONTES = Path(__file__).parent / "fontes" / "inter" / "extras" / "ttf"
# Segoe Icons só existe no Windows; fora dele os ícones do CTA saem como vetor (ver ICONES_VETOR)
ICONES = next((p for p in ("C:/Windows/Fonts/SegoeIcons.ttf", str(Path(__file__).parent / "fontes" / "SegoeIcons.ttf"))
               if Path(p).exists()), None)


def hexc(h, a=1.0):
    h = h.lstrip("#")
    r, g, b = int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)
    return skia.ColorSetARGB(int(max(0, min(1, a)) * 255), r, g, b)


# ---------------- paleta ----------------
BG = "#EFEFEC"
CARD = "#FFFFFF"
INK = "#1C1C1E"
INK2 = "#3A3A3C"
GRAY = "#8E8E93"
LIGHT = "#C7C7CC"
LINE = "#E3E3E0"
GREEN = "#16A36A"
RED = "#E5484D"
AMBER = "#E8A317"
BLUE = "#3B6CF6"
PURPLE = "#7C5CFA"
BG_GRAD = ("#F6F6F4", "#E8E8E5")
ARC = ("#FFFFFF", 0.35)
SHADOW_K = 1.0
CARD_STROKE = None

TEMAS = {
    "claro": dict(BG="#EFEFEC", CARD="#FFFFFF", INK="#1C1C1E", INK2="#3A3A3C", GRAY="#8E8E93", LIGHT="#C7C7CC",
                  LINE="#E3E3E0", GREEN="#16A36A", RED="#E5484D", AMBER="#E8A317", BLUE="#3B6CF6", PURPLE="#7C5CFA",
                  BG_GRAD=("#F6F6F4", "#E8E8E5"), ARC=("#FFFFFF", 0.35), SHADOW_K=1.0, CARD_STROKE=None),
    "seguridade": dict(BG="#EFEFEC", CARD="#FFFFFF", INK="#1C1C1E", INK2="#3A3A3C", GRAY="#8E8E93", LIGHT="#C7C7CC",
                       LINE="#E3E3E0", GREEN="#16A36A", RED="#E5484D", AMBER="#E8A317", BLUE="#0F766E", PURPLE="#4F46E5",
                       BG_GRAD=("#F6F6F4", "#E8E8E5"), ARC=("#FFFFFF", 0.35), SHADOW_K=1.0, CARD_STROKE=None),
    "escuro": dict(BG="#0D1117", CARD="#161B22", INK="#F2F4F7", INK2="#C9D1D9", GRAY="#8B949E", LIGHT="#3D4450",
                   LINE="#262D36", GREEN="#22C27A", RED="#F25C62", AMBER="#F5B83D", BLUE="#5B8CFF", PURPLE="#9B7BFF",
                   BG_GRAD=("#161C25", "#0A0D12"), ARC=("#FFFFFF", 0.025), SHADOW_K=3.2, CARD_STROKE="#252C36"),
}


def set_theme(nome):
    """troca a paleta inteira (chamar antes de 'from motor import *')"""
    globals().update(TEMAS[nome])


def lum(h):
    h = h.lstrip("#")
    r, g, b = (int(h[i:i + 2], 16) / 255 for i in (0, 2, 4))
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def on(bg):
    """cor de texto legível sobre bg"""
    return "#11151B" if lum(bg) > 0.72 else "#FFFFFF"


# ---------------- tempo / easing ----------------
def clamp(x, a=0.0, b=1.0):
    return a if x < a else b if x > b else x


def prog(t, t0, d=0.5):
    if d <= 0:
        return 1.0 if t >= t0 else 0.0
    return clamp((t - t0) / d)


def ease_out(x):
    return 1 - (1 - x) ** 3


def ease_io(x):
    return 4 * x ** 3 if x < 0.5 else 1 - (-2 * x + 2) ** 3 / 2


def ease_back(x):
    c1, c3 = 1.70158, 2.70158
    return 1 + c3 * (x - 1) ** 3 + c1 * (x - 1) ** 2


def ep(t, t0, d=0.5):
    return ease_out(prog(t, t0, d))


def lerp(a, b, f):
    return a + (b - a) * f


def mix(c1, c2, f):
    """mistura duas cores hex -> hex"""
    a = [int(c1.lstrip("#")[i:i + 2], 16) for i in (0, 2, 4)]
    b = [int(c2.lstrip("#")[i:i + 2], 16) for i in (0, 2, 4)]
    return "#" + "".join(f"{int(lerp(x, y, f)):02X}" for x, y in zip(a, b))


class Cues(dict):
    """Dicionário de cues; cue inexistente = 'nunca' (1e9)."""
    def __missing__(self, k):
        return 1e9


# ---------------- fontes ----------------
PESOS = {"light": "Inter-Light", "regular": "Inter-Regular", "medium": "Inter-Medium",
         "semibold": "Inter-SemiBold", "bold": "Inter-Bold", "extrabold": "Inter-ExtraBold", "black": "Inter-Black"}


@lru_cache(None)
def typeface(peso):
    if peso == "icons":
        return skia.Typeface.MakeFromFile(ICONES)
    return skia.Typeface.MakeFromFile(str(FONTES / f"{PESOS[peso]}.ttf"))


@lru_cache(None)
def font(peso, size):
    f = skia.Font(typeface(peso), size)
    f.setSubpixel(True)
    f.setEdging(skia.Font.Edging.kAntiAlias)
    return f


def paint(color, a=1.0, stroke=None, cap_round=False):
    p = skia.Paint(AntiAlias=True, Color=hexc(color, a))
    if stroke:
        p.setStyle(skia.Paint.kStroke_Style)
        p.setStrokeWidth(stroke)
        if cap_round:
            p.setStrokeCap(skia.Paint.kRound_Cap)
    return p


def text_w(s, peso, size):
    return font(peso, size).measureText(s)


def text(c, s, x, y, size=40, peso="regular", color=None, a=1.0, align="center", tracking=0.0):
    """y = linha de base"""
    color = INK if color is None else color
    f = font(peso, size)
    if tracking:
        w = sum(f.measureText(ch) for ch in s) + tracking * (len(s) - 1)
        xx = x - w / 2 if align == "center" else x - w if align == "right" else x
        for ch in s:
            c.drawString(ch, xx, y, f, paint(color, a))
            xx += f.measureText(ch) + tracking
        return w
    w = f.measureText(s)
    xx = x - w / 2 if align == "center" else x - w if align == "right" else x
    c.drawString(s, xx, y, f, paint(color, a))
    return w


def text_mid(c, s, x, cy, size, peso="regular", color=None, a=1.0, align="center", tracking=0.0):
    """centraliza verticalmente pelo cap-height"""
    color = INK if color is None else color
    return text(c, s, x, cy + size * 0.36, size, peso, color, a, align, tracking)


# Contornos (grade 24x24) que imitam os glifos da Segoe Fluent Icons usados no CTA
ICONES_VETOR = {
    "\ue8e1": ["M9 20.5C7.2 20.5 5.9 19.4 5.6 17.6L5.2 15C5 13.6 5.6 12.5 6.7 11.7L10.6 7.6L11.6 4.3"
               "C11.9 3.3 12.9 2.8 13.8 3.3C14.6 3.8 14.9 4.8 14.7 5.8L13.9 10H16.9C18.3 10 19.2 11.3 18.9 12.7"
               "L17.8 18.4C17.5 19.7 16.5 20.5 15.3 20.5Z"],                                         # curtir
    "\uea8f": ["M12 3.2A5.8 5.8 0 0 0 6.2 9V13.4L4.6 15.7A0.9 0.9 0 0 0 5.4 17.1H18.6A0.9 0.9 0 0 0 19.4 15.7"
               "L17.8 13.4V9A5.8 5.8 0 0 0 12 3.2Z", "M9.6 17.1a2.4 2.4 0 0 0 4.8 0"],            # sininho
    "\ue90a": ["M5.2 4.5H18.8A1.7 1.7 0 0 1 20.5 6.2V15.3A1.7 1.7 0 0 1 18.8 17H11L7.3 20.4V17H5.2"
               "A1.7 1.7 0 0 1 3.5 15.3V6.2A1.7 1.7 0 0 1 5.2 4.5Z"],                               # comentário
}


def _svg_path(d):
    """caminho SVG (M L H V C A Z, absolutos e relativos) -> skia.Path"""
    import re
    tk = re.findall(r"[MLHVCAZmlhvcaz]|-?(?:\d+\.?\d*|\.\d+)", d)
    p, i, cmd, x, y, sx, sy = skia.Path(), 0, None, 0.0, 0.0, 0.0, 0.0
    while i < len(tk):
        if tk[i].isalpha():
            cmd = tk[i]; i += 1
            if cmd in "Zz":
                p.close(); x, y = sx, sy
                continue
        rel, up = cmd.islower(), cmd.upper()
        n = {"M": 2, "L": 2, "H": 1, "V": 1, "C": 6, "A": 7}[up]
        v = [float(s) for s in tk[i:i + n]]; i += n
        ox, oy = (x, y) if rel else (0.0, 0.0)
        if up == "M":
            x, y = ox + v[0], oy + v[1]; p.moveTo(x, y); sx, sy = x, y
            cmd = "l" if rel else "L"
        elif up == "L":
            x, y = ox + v[0], oy + v[1]; p.lineTo(x, y)
        elif up == "H":
            x = ox + v[0]; p.lineTo(x, y)
        elif up == "V":
            y = oy + v[0]; p.lineTo(x, y)
        elif up == "C":
            p.cubicTo(ox + v[0], oy + v[1], ox + v[2], oy + v[3], ox + v[4], oy + v[5]); x, y = ox + v[4], oy + v[5]
        else:
            x, y = ox + v[5], oy + v[6]
            p.arcTo(v[0], v[1], v[2], skia.Path.ArcSize.kLarge_ArcSize if v[3] else skia.Path.ArcSize.kSmall_ArcSize,
                    skia.PathDirection.kCW if v[4] else skia.PathDirection.kCCW, x, y)
    return p


@lru_cache(None)
def icon_path(glyph):
    if glyph not in ICONES_VETOR:
        return None
    p = skia.Path()
    for d in ICONES_VETOR[glyph]:
        p.addPath(_svg_path(d))
    return p


def icon(c, glyph, cx, cy, size, color=None, a=1.0, p=None):
    """desenha um glifo da Segoe Icons centrado em (cx, cy); sem a fonte, usa o contorno vetorial. p = Paint opcional"""
    color = INK if color is None else color
    p = paint(color, a) if p is None else p
    if ICONES:
        f = font("icons", size)
        w = f.measureText(glyph)
        c.drawString(glyph, cx - w / 2, cy + size / 2, f, p)
        return
    path = icon_path(glyph)
    if path is None:
        raise ValueError(f"ícone U+{ord(glyph[0]):04X} sem a fonte Segoe Icons e sem contorno em ICONES_VETOR")
    # mesma área e centro que o glifo da fonte ocuparia: lado maior = 95% do tamanho, traço fino como o da Segoe
    bb = path.computeTightBounds()
    k = size * 0.95 / max(bb.width(), bb.height())
    c.save(); c.translate(cx - bb.centerX() * k, cy - bb.centerY() * k); c.scale(k, k)
    q = skia.Paint(p)
    q.setStyle(skia.Paint.kStroke_Style); q.setStrokeWidth(size * 0.048 / k)
    q.setStrokeCap(skia.Paint.kRound_Cap); q.setStrokeJoin(skia.Paint.kRound_Join)
    c.drawPath(path, q)
    c.restore()


# ---------------- primitivas ----------------
def shadow_rrect(c, x, y, w, h, r, a=1.0, strength=1.0):
    p = skia.Paint(AntiAlias=True, Color=hexc("#000000", min(1, 0.10 * a * strength * SHADOW_K)))
    p.setMaskFilter(skia.MaskFilter.MakeBlur(skia.kNormal_BlurStyle, 22))
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y + 14, w, h), r, r), p)
    p2 = skia.Paint(AntiAlias=True, Color=hexc("#000000", min(1, 0.06 * a * strength * SHADOW_K)))
    p2.setMaskFilter(skia.MaskFilter.MakeBlur(skia.kNormal_BlurStyle, 4))
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y + 2, w, h), r, r), p2)


def rrect(c, x, y, w, h, r, color=None, a=1.0, shadow=False, stroke=None, stroke_color=None):
    color = CARD if color is None else color
    stroke_color = LINE if stroke_color is None else stroke_color
    if shadow:
        shadow_rrect(c, x, y, w, h, r, a)
    rr = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), r, r)
    c.drawRRect(rr, paint(color, a))
    if stroke:
        c.drawRRect(rr, paint(stroke_color, a, stroke=stroke))


def card(c, x, y, w, h, a=1.0, r=28, scale=1.0):
    if a <= 0:
        return
    if scale != 1.0:
        c.save(); cx, cy = x + w / 2, y + h / 2
        c.translate(cx, cy); c.scale(scale, scale); c.translate(-cx, -cy)
    rrect(c, x, y, w, h, r, CARD, a, shadow=True, stroke=1.5 if CARD_STROKE else None, stroke_color=CARD_STROKE)
    if scale != 1.0:
        c.restore()


PILL_BOUNDS = (158, 1762)


def pill(c, s, x, cy, bg, fg=None, size=22, a=1.0, anchor="left", peso="bold", pad=None, shadow=True, r=None,
         bounds=None):
    """Etiqueta arredondada. anchor: left/center/right em relação a x. Retorna (x0, x1)."""
    if a <= 0:
        return (x, x)
    pad = size * 0.62 if pad is None else pad
    fg = on(bg) if fg is None else fg
    tw = text_w(s, peso, size)
    w, h = tw + pad * 2, size * 1.75
    x0 = x if anchor == "left" else x - w / 2 if anchor == "center" else x - w
    b = bounds or PILL_BOUNDS
    x0 = max(b[0], min(x0, b[1] - w))
    rr = r if r is not None else h / 2.6
    if shadow:
        shadow_rrect(c, x0, cy - h / 2, w, h, rr, a, 0.6)
    rrect(c, x0, cy - h / 2, w, h, rr, bg, a)
    text_mid(c, s, x0 + w / 2, cy, size, peso, fg, a)
    return (x0, x0 + w)


def badge_num(c, n, cx, cy, a=1.0, r=22, bg=None, fg=None):
    if a <= 0:
        return
    bg = INK if bg is None else bg
    fg = on(bg) if fg is None else fg
    s = 0.6 + 0.4 * ease_back(clamp(a))
    c.save(); c.translate(cx, cy); c.scale(s, s)
    shadow_rrect(c, -r, -r, 2 * r, 2 * r, r, a, 0.7)
    c.drawCircle(0, 0, r, paint(bg, a))
    text_mid(c, str(n), 0, 0, r * 1.05, "bold", fg, a)
    c.restore()


def check_icon(c, cx, cy, r=20, a=1.0, color=None, kind="check"):
    if a <= 0:
        return
    color = GREEN if color is None else color
    s = 0.5 + 0.5 * ease_back(clamp(a))
    c.save(); c.translate(cx, cy); c.scale(s, s)
    c.drawCircle(0, 0, r, paint(color, a))
    p = skia.Path()
    if kind == "check":
        p.moveTo(-r * 0.42, 0.02 * r); p.lineTo(-r * 0.1, r * 0.33); p.lineTo(r * 0.45, -r * 0.3)
    else:
        k = r * 0.36
        p.moveTo(-k, -k); p.lineTo(k, k); p.moveTo(k, -k); p.lineTo(-k, k)
    pp = paint("#FFFFFF", a, stroke=r * 0.2, cap_round=True)
    pp.setStrokeJoin(skia.Paint.kRound_Join)
    c.drawPath(p, pp)
    c.restore()


def hline(c, x0, x1, y, color, a=1.0, width=2.5, dash=None, progress=1.0):
    if a <= 0 or progress <= 0:
        return
    p = paint(color, a, stroke=width)
    if dash:
        p.setPathEffect(skia.DashPathEffect.Make(dash, 0))
    c.drawLine(x0, y, lerp(x0, x1, progress), y, p)


def line(c, x0, y0, x1, y1, color, a=1.0, width=2.5, dash=None, progress=1.0, cap_round=True):
    if a <= 0 or progress <= 0:
        return
    p = paint(color, a, stroke=width, cap_round=cap_round)
    if dash:
        p.setPathEffect(skia.DashPathEffect.Make(dash, 0))
    c.drawLine(x0, y0, lerp(x0, x1, progress), lerp(y0, y1, progress), p)


def arrow(c, x0, y0, x1, y1, color, a=1.0, width=4, head=16, progress=1.0):
    if a <= 0 or progress <= 0:
        return
    xe, ye = lerp(x0, x1, progress), lerp(y0, y1, progress)
    line(c, x0, y0, xe, ye, color, a, width)
    ang = math.atan2(ye - y0, xe - x0)
    p = skia.Path()
    p.moveTo(xe + math.cos(ang) * 4, ye + math.sin(ang) * 4)
    p.lineTo(xe - head * math.cos(ang - 0.45), ye - head * math.sin(ang - 0.45))
    p.lineTo(xe - head * math.cos(ang + 0.45), ye - head * math.sin(ang + 0.45))
    p.close()
    c.drawPath(p, paint(color, a))


def title_chip(c, l1, l2, t, t0, color2=None, cy=82, t_out=None):
    """Título de duas linhas no topo (linha 1 escura, linha 2 colorida)."""
    color2 = GREEN if color2 is None else color2
    a = ep(t, t0, 0.5)
    if t_out is not None:
        a *= 1 - prog(t, t_out, 0.35)
    if a <= 0:
        return
    s1, s2 = 30, 30
    w = max(text_w(l1, "extrabold", s1), text_w(l2, "extrabold", s2) if l2 else 0) + 56
    h = 96 if l2 else 62
    y = cy - h / 2 + (1 - a) * -14
    rrect(c, W / 2 - w / 2, y, w, h, 18, CARD, a, shadow=True)
    if l2:
        text_mid(c, l1, W / 2, y + 30, s1, "extrabold", INK, a, tracking=0.5)
        text_mid(c, l2, W / 2, y + 66, s2, "extrabold", color2, a, tracking=0.5)
    else:
        text_mid(c, l1, W / 2, y + h / 2, s1, "extrabold", INK, a, tracking=0.5)


def background(c):
    c.clear(hexc(BG))
    sh = skia.GradientShader.MakeRadial(center=(W / 2, H * 0.42), radius=W * 0.75,
                                        colors=[hexc(BG_GRAD[0]), hexc(BG_GRAD[1])])
    p = skia.Paint(AntiAlias=True); p.setShader(sh)
    c.drawRect(skia.Rect.MakeWH(W, H), p)
    # arcos decorativos suaves (como na referência)
    p2 = paint(ARC[0], ARC[1], stroke=46)
    c.drawArc(skia.Rect.MakeXYWH(-260, 640, 620, 620), 270, 90, False, p2)
    c.drawArc(skia.Rect.MakeXYWH(W - 360, -260, 620, 620), 90, 90, False, p2)


# ---------------- legenda cinética ----------------
CAP_Y = 948          # linha de base (1 linha)
CAP_MAXW = 1450
CAP_SIZE = 44
CAP_BOLD = 50
ENDS = (".", "!", "?", ":", "…", "...")


def chunk_tokens(tokens):
    chunks, cur = [], []
    for i, tk in enumerate(tokens):
        cur.append(tk)
        d = tk["disp"]
        # quantas palavras faltam até o fim da frase
        rest = 0
        for nx in tokens[i + 1:]:
            rest += 1
            if nx["disp"].endswith(ENDS):
                break
        if d.endswith(ENDS) or ((len(cur) >= 7 and d.endswith(",") or len(cur) >= 10) and rest > 3) or len(cur) >= 14:
            chunks.append(cur); cur = []
    if cur:
        chunks.append(cur)
    return chunks


def _layout(chunk):
    words = []
    for tk in chunk:
        peso, size = ("extrabold", CAP_BOLD) if tk["bold"] else ("medium", CAP_SIZE)
        words.append((tk, peso, size, text_w(tk["disp"], peso, size)))
    sp = 13
    lines, cur, cw = [], [], 0
    for w in words:
        add = w[3] + (sp if cur else 0)
        if cur and cw + add > CAP_MAXW:
            lines.append((cur, cw)); cur, cw = [w], w[3]
        else:
            cur.append(w); cw += add
    if cur:
        lines.append((cur, cw))
    return lines, sp


def draw_caption(c, scene, t):
    """scene: dict com start, dur, tokens (t0/t1 relativos à cena)."""
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
    lh = 64
    y0 = CAP_Y - (len(lines) - 1) * lh / 2
    for li, (ws, lw) in enumerate(lines):
        x = W / 2 - lw / 2
        y = y0 + li * lh
        for tk, peso, size, ww in ws:
            a = prog(lt, tk["t0"] - 0.06, 0.28)
            if a > 0:
                f = ease_out(a)
                col = mix(LIGHT, INK if tk["bold"] else INK2, f)
                text(c, tk["disp"], x, y + (1 - f) * 12, size, peso, col, f * out, align="left")
            x += ww + sp


# ---------------- gráfico de candles ----------------
class Chart:
    def __init__(self, candles, rect, pmin=None, pmax=None, body=0.62, max_body=64, pad_lo=0.06, pad_hi=0.06):
        self.k = candles
        self.x0, self.y0, self.w, self.h = rect
        lo = min(k[2] for k in candles); hi = max(k[1] for k in candles)
        self.pmin = pmin if pmin is not None else lo - (hi - lo) * pad_lo
        self.pmax = pmax if pmax is not None else hi + (hi - lo) * pad_hi
        self.n = len(candles)
        self.rx = self.x0
        self.body, self.max_body = body, max_body
        self.step = self.w / self.n
        self.bw = min(self.step * body, max_body)

    def view(self, v0, v1, pmin=None, pmax=None):
        """câmera: mostra os índices v0..v1 (float) e a faixa de preço pmin..pmax"""
        self.step = self.w / (v1 - v0)
        self.bw = min(self.step * self.body, self.max_body)
        self.x0 = self.rx - v0 * self.step
        if pmin is not None:
            self.pmin, self.pmax = pmin, pmax
        return self

    def full_view(self):
        return (0.0, float(self.n), self.pmin, self.pmax)

    def x(self, i):
        return self.x0 + (i + 0.5) * self.step

    def y(self, p):
        return self.y0 + (self.pmax - p) / (self.pmax - self.pmin) * self.h

    def xl(self, i):
        return self.x(i) - self.bw / 2

    def xr(self, i):
        return self.x(i) + self.bw / 2

    def draw(self, c, nvis, a=1.0, color_fn=None, alpha_fn=None, start=0):
        full = int(math.floor(nvis))
        frac = nvis - full
        wick_w = max(2.0, min(3.2, self.bw * 0.16))
        for i in range(start, min(self.n, full + (1 if frac > 0 else 0))):
            o, h, l, cl = self.k[i]
            if i == full:  # candle em formação
                f = ease_out(frac)
                cl = o + (cl - o) * f
                h = max(o, cl) + (h - max(o, self.k[i][3])) * f
                l = min(o, cl) - (min(o, self.k[i][3]) - l) * f
            up = self.k[i][3] >= self.k[i][0]
            col = color_fn(i) if color_fn else (GREEN if up else RED)
            aa = a * (alpha_fn(i) if alpha_fn else 1.0)
            if aa <= 0:
                continue
            x = self.x(i)
            c.drawLine(x, self.y(h), x, self.y(l), paint(col, aa, stroke=wick_w))
            top, bot = self.y(max(o, cl)), self.y(min(o, cl))
            if bot - top < 2.5:
                top, bot = (top + bot) / 2 - 1.25, (top + bot) / 2 + 1.25
            r = min(3.0, self.bw * 0.12)
            c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeLTRB(x - self.bw / 2, top, x + self.bw / 2, bot), r, r),
                        paint(col, aa))

    def zone(self, c, i0, i1, p0, p1, color=None, a=1.0, progress=1.0, fill=0.22, border=True, ext=0.0):
        """retângulo de preço entre p0..p1, de i0 até i1 (índices) — ext estende à direita em px."""
        color = AMBER if color is None else color
        if a <= 0 or progress <= 0:
            return
        xa = self.xl(i0) - 4
        xb = self.xr(i1) + ext
        xb = lerp(xa, xb, progress)
        ya, yb = self.y(max(p0, p1)), self.y(min(p0, p1))
        rr = skia.RRect.MakeRectXY(skia.Rect.MakeLTRB(xa, ya, xb, yb), 4, 4)
        c.drawRRect(rr, paint(color, a * fill))
        if border:
            c.drawRRect(rr, paint(color, a * 0.9, stroke=2))

    def level(self, c, i0, i1, p, color=None, a=1.0, dash=(10, 8), width=2.5, progress=1.0, ext=0.0):
        color = INK if color is None else color
        hline(c, self.x(i0), self.x(i1) + ext, self.y(p), color, a, width, dash, progress)

    def ring(self, c, i, p, color=None, a=1.0, r=16):
        color = INK if color is None else color
        if a <= 0:
            return
        s = 0.6 + 0.4 * ease_back(clamp(a))
        c.drawCircle(self.x(i), self.y(p), r * s, paint(color, a, stroke=3))

    def wick_glow(self, c, i, which, color=None, a=1.0):
        """destaca o pavio superior ('h') ou inferior ('l') de um candle."""
        color = BLUE if color is None else color
        if a <= 0:
            return
        o, h, l, cl = self.k[i]
        x = self.x(i)
        if which == "h":
            y0, y1 = self.y(h), self.y(max(o, cl))
        else:
            y0, y1 = self.y(min(o, cl)), self.y(l)
        p = paint(color, a * 0.35, stroke=16, cap_round=True)
        c.drawLine(x, y0, x, y1, p)
        c.drawLine(x, y0, x, y1, paint(color, a, stroke=5, cap_round=True))
