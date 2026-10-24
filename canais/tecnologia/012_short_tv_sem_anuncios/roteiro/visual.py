"""Visual do Short 012 (Tecnativo English) — a TV dos pais sem anúncios com o Claude Code (cleanyourtv). 1080x1920.
render.py <proj> --vertical --lang en. Tema 'tech' (cores, painéis, chips), mas fundo, legenda e moldura próprios
para o formato vertical: zona útil entre y=200 e y=1560 (a interface do Shorts cobre o rodapé e a lateral direita).

Imagens REAIS (original/imagens/, crédito na tela "Images: @gathint · cleanyour.tv"): o antes/depois que o autor
postou (card.jpg do repositório, MIT) e a tela do launcher. Terminal, radar e post são recriações (selo "illustration"
onde não é texto real); os nomes de pacote são reais (examples/xiaomi-mitv-afmu0/debloat.txt)."""
import math
from functools import lru_cache
from pathlib import Path
import numpy as np
import skia
import idioma
import motor
import tech
from motor import *  # noqa
from tech import *  # noqa

motor.PESOS["mono"] = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono"
motor.PESOS["monob"] = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold"

ARQUIVO_FINAL = "tecnologia_012_short_tv_sem_anuncios.mp4"
MARCA = ""
SOM = dict(intro=False, ganho_trilha=0.40, lufs=-14, bpm=124, sfx={
    "01.a": "alert", "01.b": ["glitch", "impact@+0.25"],
    "02.a": "notif", "02.b": "lock",
    "03.a": "data", "03.b": "typing", "03.c": ["data", "data@+0.6", "data@+1.2"], "03.d": ["deny", "deny@+0.35", "deny@+0.7"],
    "04.a": "typing", "04.b": "click", "04.c": "impact", "04.d": "shimmer",
    "05.a": "data", "05.b": "data", "05.c": "data",
    "06.a": "confirm", "06.b": "confirm", "06.c": "alert", "06.d": "deny",
    "07.a": "lock", "07.b": "glitch"})

IMG = Path(__file__).resolve().parent.parent / "original" / "imagens"
CLAUDE = "#E8825A"   # laranja "Claude" (só cor, sem logo)
AD = "#FF3B4E"
YEL = "#FFD84A"
CX = W / 2
PT = idioma.LANG == "pt"   # versão do Tecnativo (português): textos da tela em roteiro/textos.py, números no formato BR
TOP, BOT = 210, 1560          # zona útil


# ---------------------------------------------------------------- utilidades
def fade(t, t0, t1, d=0.35, d_out=0.3):
    return ep(t, t0, d) * (1 - prog(t, t1, d_out))


@lru_cache(None)
def img(nome):
    return skia.Image.open(str(IMG / nome))


# recortes do card.jpg (1600x1280): telas "antes" e "depois" fotografadas pelo autor
ANTES = ("card.jpg", (76, 830, 752, 1196))
DEPOIS = ("card.jpg", (849, 839, 1526, 1187))


def draw_img(c, ref, x, y, w, h, a=1.0, zoom=1.0, fx=0.5, fy=0.5):
    nome, (sx0, sy0, sx1, sy1) = ref if isinstance(ref, tuple) else (ref, (0, 0, img(ref).width(), img(ref).height()))
    sw, sh = (sx1 - sx0) / zoom, (sy1 - sy0) / zoom
    ox = sx0 + (sx1 - sx0 - sw) * fx
    oy = sy0 + (sy1 - sy0 - sh) * fy
    p = skia.Paint(AntiAlias=True); p.setAlphaf(clamp(a))
    c.drawImageRect(img(nome), skia.Rect.MakeXYWH(ox, oy, sw, sh), skia.Rect.MakeXYWH(x, y, w, h),
                    skia.SamplingOptions(skia.FilterMode.kLinear, skia.MipmapMode.kLinear), p)


def tv(c, x, y, w, ref, a=1.0, zoom=1.0, fx=0.5, fy=0.5, glow=CYAN, stand=True):
    """TV com moldura fina, pé e brilho; ref = imagem (ou None para tela apagada). Devolve a área da tela."""
    h = w * 9 / 16
    if a <= 0:
        return (x, y, w, h)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x - 14, y - 14, w + 28, h + 28), 16, 16), blur_paint(glow, 0.28 * a, 40))
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x - 12, y - 12, w + 24, h + 24), 14, 14), paint("#05070C", a))
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x - 12, y - 12, w + 24, h + 24), 14, 14), paint("#2A3552", a, stroke=2))
    c.save()
    c.clipRect(skia.Rect.MakeXYWH(x, y, w, h), doAntiAlias=True)
    if ref:
        draw_img(c, ref, x, y, w, h, a, zoom, fx, fy)
    else:
        c.drawRect(skia.Rect.MakeXYWH(x, y, w, h), paint("#0A0E18", a))
    c.restore()
    if stand:
        c.drawRect(skia.Rect.MakeXYWH(x + w / 2 - 70, y + h + 12, 140, 14), paint("#1A2236", a))
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x + w / 2 - 190, y + h + 24, 380, 12), 6, 6), paint("#1A2236", a))
    return (x, y, w, h)


def title(c, s, y, a, col=INK, size=74, hl=None, hl_col=YEL, maxw=980):
    """título grande centralizado; hl = palavra destacada (caixa amarela)"""
    if a <= 0:
        return
    f = ease_out(clamp(a))
    while text_w(s, "black", size) > maxw:
        size -= 2
    w = text_w(s, "black", size)
    x = CX - w / 2
    yy = y + (1 - f) * 26
    if hl and hl in s:
        pre = s[:s.index(hl)]
        gap = 16 if pre else 0
        x -= gap
        hx = x + text_w(pre, "black", size) + gap
        hw = text_w(hl, "black", size)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(hx - 12, yy - size * 0.86, (hw + 24) * ep(a, 0.3, 0.5), size * 1.12), 10, 10),
                    paint(hl_col, f))
        text(c, pre, x, yy, size, "black", col, f, align="left")
        text(c, hl, hx, yy, size, "black", "#0B0F1A", f, align="left")
        text(c, s[s.index(hl) + len(hl):], hx + hw + 16, yy, size, "black", col, f, align="left")
    else:
        glow_text(c, s, CX, yy, size, "black", col, f, glow=0.18)


def stamp(c, s, cx, cy, col, a, size=40, rot=-8, scale=1.0):
    """carimbo inclinado (AD, BRICKED...)"""
    if a <= 0:
        return
    k = 1 + 0.6 * (1 - ease_out(clamp(a * 2.2)))
    c.save(); c.translate(cx, cy); c.rotate(rot); c.scale(k * scale, k * scale)
    w = text_w(s, "black", size) + size * 0.9
    h = size * 1.45
    r = skia.Rect.MakeXYWH(-w / 2, -h / 2, w, h)
    c.drawRRect(skia.RRect.MakeRectXY(r, 10, 10), blur_paint(col, 0.5 * a, 16))
    c.drawRRect(skia.RRect.MakeRectXY(r, 10, 10), paint(col, a))
    text_mid(c, s, 0, 0, size, "black", "#FFFFFF", a)
    c.restore()


def credit(c, a, s="Images: @gathint · cleanyour.tv"):
    text(c, s, CX, 1238, 24, "medium", INK2, 0.85 * a)


def shake(t, t0, amp=14, d=0.35):
    u = prog(t, t0, d)
    if u <= 0 or u >= 1:
        return 0.0, 0.0
    k = (1 - u) * amp
    return k * math.sin(t * 90), k * math.cos(t * 77)


def wifi_icon(c, cx, cy, s, col, a):
    for i in range(3):
        r = s * (0.35 + 0.33 * i)
        c.drawArc(skia.Rect.MakeXYWH(cx - r, cy - r, 2 * r, 2 * r), 225, 90, False, paint(col, a, stroke=s * 0.12, cap_round=True))
    c.drawCircle(cx, cy, s * 0.1, paint(col, a))


def check_row(c, x, y, kind, s, a, col):
    """linha de checklist: kind = ok / warn / no"""
    if a <= 0:
        return
    dx = (1 - ease_out(a)) * -40
    rrect(c, x + dx, y - 62, 960, 112, 22, PANEL, 0.92 * a)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x + dx, y - 62, 960, 112), 22, 22), paint(col, 0.7 * a, stroke=2.5))
    cx, cy = x + dx + 64, y - 6
    c.drawCircle(cx, cy, 34, paint(col, a))
    if kind == "ok":
        pth = skia.Path(); pth.moveTo(cx - 15, cy + 1); pth.lineTo(cx - 4, cy + 13); pth.lineTo(cx + 17, cy - 12)
        c.drawPath(pth, paint("#04130A", a, stroke=7, cap_round=True))
    elif kind == "no":
        for sg in (1, -1):
            c.drawLine(cx - 13, cy - 13 * sg, cx + 13, cy + 13 * sg, paint("#2A0508", a, stroke=7, cap_round=True))
    else:
        text_mid(c, "!", cx, cy, 46, "black", "#2A1A00", a)
    text_mid(c, s, x + dx + 124, cy, 46, "extrabold", INK, a, align="left")


# ---------------------------------------------------------------- fundo, legenda, moldura
@lru_cache(None)
def _bg():
    s = skia.Surface(W, H); c = s.getCanvas()
    p = skia.Paint()
    p.setShader(skia.GradientShader.MakeRadial(center=(W * 0.5, H * 0.33), radius=H * 0.75,
                                               colors=[hexc("#13204A"), hexc("#070B1A"), hexc("#020308")], positions=[0, 0.55, 1]))
    c.drawRect(skia.Rect.MakeWH(W, H), p)
    g = paint("#22D3EE", 0.05, stroke=1.2)
    for x in range(0, W, 60):
        c.drawLine(x, 0, x, H, g)
    for y in range(0, H, 60):
        c.drawLine(0, y, W, y, g)
    return s.makeImageSnapshot()


def BACKGROUND(c, t):
    c.drawImage(_bg(), 0, 0)
    for i in range(40):
        x = hash01(i, 1) * W + math.sin(t * 0.4 + i) * 14
        y = H - ((hash01(i, 3) * H + t * (20 + 50 * hash01(i, 5))) % (H + 40))
        c.drawCircle(x, y, 1.5 + 2 * hash01(i, 7), paint(CYAN if i % 3 else VIOLET, 0.25 + 0.3 * hash01(i, 9)))
    # brilho que segue o tema da cena (vermelho do anúncio no começo e no fim)
    red = max(fade(t, 0, 4.6, 0.01, 0.5), ep(t, 39.0, 0.6))
    if red > 0:
        c.drawCircle(CX, 640, 620, blur_paint(AD, 0.13 * red, 160))


CAP_Y = 1395


NUMEROS = [("seven point four million", "7.4M"), ("twenty-seven thousand", "27,000"), ("two hundred fifty-two", "252"),
           ("twenty-five", "25"), ("six days", "6 days"),
           ("sete vírgula quatro milhões", "7,4 milhões"), ("vinte e sete mil", "27 mil"),
           ("duzentos e cinquenta e dois", "252"), ("vinte e cinco", "25"), ("seis dias", "6 dias")]


def _numeros(tokens):
    """junta os tokens de um número falado por extenso num token só, em algarismos (mantém pontuação final)"""
    out, i = [], 0
    while i < len(tokens):
        for frase, dig in NUMEROS:
            n = len(frase.split())
            grupo = tokens[i:i + n]
            txt = " ".join(tk["disp"] for tk in grupo).lower()
            if len(grupo) == n and txt.rstrip(".,:?!").replace("*", "") == frase:
                out.append(dict(disp=dig + txt[len(txt.rstrip(".,:?!")):], bold=any(tk["bold"] for tk in grupo),
                                t0=grupo[0]["t0"], t1=grupo[-1]["t1"]))
                i += n
                break
        else:
            out.append(tokens[i]); i += 1
    return out


def _chunks(tokens):
    tokens = _numeros(tokens)
    out, cur = [], []
    for tk in tokens:
        cur.append(tk)
        end = tk["disp"].rstrip()[-1:] in ".,:?!"
        if len(cur) >= 3 or end or sum(len(x["disp"]) + 1 for x in cur) > 16:
            out.append(cur); cur = []
    if cur:
        out.append(cur)
    return out


def CAPTION(c, scene, t):
    """legenda de Shorts: 1 a 3 palavras por vez, bem grandes, palavra falada em amarelo; destaque *x* em ciano"""
    lt = t - scene["start"]
    chunks = scene.setdefault("_ch", _chunks(scene["tokens"]))
    for i, ch in enumerate(chunks):
        s = ch[0]["t0"] - 0.06
        e = chunks[i + 1][0]["t0"] - 0.06 if i + 1 < len(chunks) else scene["dur"] - 0.05
        if s <= lt < e:
            break
    else:
        return
    words = [tk["disp"].upper() for tk in ch]
    size = 96
    sp = 26
    while sum(text_w(wd, "black", size) for wd in words) + sp * (len(words) - 1) > 960:
        size -= 3
    tot = sum(text_w(wd, "black", size) for wd in words) + sp * (len(words) - 1)
    pop = ease_back(clamp((lt - s) / 0.16))
    x = CX - tot / 2
    c.save(); c.translate(CX, CAP_Y); c.scale(0.85 + 0.15 * pop, 0.85 + 0.15 * pop); c.translate(-CX, -CAP_Y)
    for tk, wd in zip(ch, words):
        ww = text_w(wd, "black", size)
        falando = tk["t0"] - 0.05 <= lt
        col = YEL if (falando and lt < tk["t1"] + 0.25) else (CYAN if tk["bold"] else INK)
        f = motor.font("black", size)
        sh = skia.Paint(AntiAlias=True, Style=skia.Paint.kStroke_Style, StrokeWidth=size * 0.16, Color=skia.ColorBLACK)
        sh.setStrokeJoin(skia.Paint.kRound_Join)
        c.drawString(wd, x, CAP_Y + size * 0.36, f, sh)
        if col == YEL:
            c.drawString(wd, x, CAP_Y + size * 0.36, f, blur_paint(YEL, 0.35, 14))
        c.drawString(wd, x, CAP_Y + size * 0.36, f, paint(col, 1.0))
        x += ww + sp
    c.restore()


def OVERLAY(c, t):
    # marca do canal no topo
    a = 0.95
    chip(c, "TECNATIVO", CX, 150, CYAN, a, anchor="center", size=26, filled=True)
    # glitch nas viradas fortes (copia faixas do quadro deslocadas, com franja RGB)
    for t0 in GLITCH:
        u = (t - t0) / 0.32
        if 0 <= u < 1:
            surf = c.getSurface()
            if surf is None:
                break
            snap = surf.makeImageSnapshot()
            rnd = np.random.default_rng(int(t * 30))
            for _ in range(9):
                y = int(rnd.uniform(200, 1500)); h = int(rnd.uniform(10, 70)); dx = rnd.uniform(-60, 60) * (1 - u)
                c.drawImageRect(snap, skia.Rect.MakeXYWH(0, y, W, h), skia.Rect.MakeXYWH(dx, y, W, h))
                c.drawRect(skia.Rect.MakeXYWH(0, y, W, h), paint(rnd.choice([CYAN, MAGENTA, AD]), 0.12 * (1 - u)))


GLITCH = []


def _glitch(C):
    if not GLITCH:
        GLITCH[:] = [C["01.b"], C["04.c"] - 0.05, C["07.b"]]


# ---------------------------------------------------------------- blocos
def b_gancho(c, t, C, B):
    _glitch(C)
    t_a, t_b = C["01.a"], C["01.b"]
    # TV com a tela "antes" (foto real) e zoom no anúncio
    z = 1.0 + 0.55 * ease_io(prog(t, t_a + 0.35, 1.6))
    sx, sy = shake(t, t_b + 0.25, 18)
    c.save(); c.translate(sx, sy)
    x, y, w, h = tv(c, 60, 560, 960, ANTES, fade(t, t_a - 0.05, B["end"], 0.15), zoom=z, fx=0.05, fy=0.15, glow=AD)
    # caixa vermelha pulsando sobre o anúncio
    pulse = 0.6 + 0.4 * math.sin(t * 12)
    aa = ep(t, t_a + 0.5, 0.3) * (1 - prog(t, t_b, 0.3))
    if aa > 0:
        bx, by, bw, bh = x + 26, y + 26, w * 0.62 + (z - 1) * 260, h * 0.36 + (z - 1) * 150
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(bx, by, bw, bh), 12, 12), paint(AD, aa * pulse, stroke=7))
        stamp(c, "AD", bx + bw - 10, by + 8, AD, aa, 52)
    credit(c, ep(t, t_a, 0.3) * (1 - prog(t, B["end"] - 0.3, 0.3)))
    c.restore()
    title(c, "AN AD BEFORE NETFLIX?!", 400, ep(t, t_a, 0.3) * (1 - prog(t, t_b - 0.1, 0.25)), hl="NETFLIX", hl_col=AD, size=78)
    # virada: a IA assume
    ab = ep(t, t_b, 0.25)
    if ab > 0:
        c.drawRect(skia.Rect.MakeWH(W, H), paint("#000000", 0.35 * ab * (1 - prog(t, B["end"] - 0.3, 0.3))))
        title(c, "AI TAKEOVER", 420, ab * (1 - prog(t, B["end"] - 0.3, 0.3)), CLAUDE, 104)
        aout = ab * (1 - prog(t, B["end"] - 0.3, 0.3))
        terminal(c, 150, 640, 780, 330, aout, "claude code", CLAUDE)
        rows = ["> scanning network...", "> device found", "> access: granted"]
        for i, r in enumerate(rows):
            ai = ep(t, t_b + 0.3 + i * 0.35, 0.2) * (1 - prog(t, B["end"] - 0.3, 0.3))
            text(c, r, 200, 760 + i * 64, 40, "monob", LIME if i == 2 else CLAUDE, ai, align="left")


def b_post(c, t, C, B):
    _glitch(C)
    a = fade(t, B["start"], B["end"])
    t_b = C["02.b"]
    title(c, "ONE INPUT", 360, a, INK, 92, hl="ONE")
    # post recriado (texto real do post, sem logo/avatar)
    x, y, w, h = 70, 470, 940, 620
    k = ease_out(a)
    rrect(c, x, y + (1 - k) * 40, w, h, 34, "#0E1424", a)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y + (1 - k) * 40, w, h), 34, 34), paint("#2A3552", a, stroke=2))
    yy = y + (1 - k) * 40
    c.drawCircle(x + 80, yy + 84, 42, paint(CYAN, 0.25 * a))
    text_mid(c, "G", x + 80, yy + 84, 44, "black", CYAN, a)
    text(c, "Gathin", x + 146, yy + 76, 40, "extrabold", INK, a, align="left")
    text(c, "@gathint · Oct 17, 2026", x + 146, yy + 120, 30, "regular", INK2, a, align="left")
    linhas = ["Vibe coded my parents' TV this afternoon!", "It was showing a sponsored ad before you",
              "could even get to Netflix. Gave Claude Code", "the model number, it found the TV on wifi,",
              "removed 25 Xiaomi packages and wrote a", "new launcher. Looks like an Apple TV now lol"]
    for i, ln in enumerate(linhas):
        ly = yy + 210 + i * 58
        if "the model number" in ln:
            hx = x + 60
            hw = text_w("the model number", "medium", 36)
            u = ep(t, t_b, 0.35)
            c.drawRect(skia.Rect.MakeXYWH(hx - 6, ly - 36, (hw + 12) * u, 50), paint(YEL, 0.9 * a))
            text(c, "the model number", hx, ly, 36, "medium", mix(INK, "#0B0F1A", u), a, align="left")
            text(c, ln[len("the model number"):], hx + hw, ly, 36, "medium", INK, a, align="left")
        else:
            text(c, ln, x + 60, ly, 36, "medium", INK, a, align="left")
    text(c, "post on X · 7.4M views", x + 60, yy + h - 40, 28, "monob", DIM, a, align="left")
    chip(c, "CLAUDE CODE", CX, 1190, CLAUDE, ep(t, C["02.a"] + 0.6, 0.3) * a, anchor="center", size=34, filled=True)


PKGS = ["com.miui.tv.analytics", "com.xiaomi.statistic", "com.mitv.tvhome.atv", "com.mitv.tvhome.michannel",
        "com.mitv.tvhome.mitvplus", "com.mitv.tvhome.oemtab", "com.xm.webcontent", "com.xiaomi.tvqs.overseas.y24",
        "com.google.android.feedback", "com.xiaomi.mimusic2", "com.mitv.videoplayer", "com.mitv.gallery"]


def b_hack(c, t, C, B):
    _glitch(C)
    a = fade(t, B["start"], B["end"])
    ta, tb, tc, td = C["03.a"], C["03.b"], C["03.c"], C["03.d"]
    # (a) radar Wi-Fi achando a TV
    ar = a * (1 - prog(t, tb, 0.3))
    if ar > 0:
        title(c, "FOUND IT ON WI-FI", 380, ar, INK, 80, hl="WI-FI", hl_col=CYAN)
        cy = 820
        for i in range(4):
            r = ((t - ta) * 260 + i * 110) % 440
            c.drawCircle(CX, cy, r, paint(CYAN, ar * 0.5 * (1 - r / 440), stroke=3))
        wifi_icon(c, CX, cy + 30, 90, CYAN, ar)
        u = ep(t, ta + 0.6, 0.3)
        tv(c, 640, 640, 300, None, ar * u, glow=LIME, stand=False)
        text_mid(c, "Xiaomi TV", 790, 724, 34, "extrabold", LIME, ar * u)
        text(c, "illustration", CX, 1200, 24, "mono", DIM, ar)
    # (b)(c) terminal com ADB e os pacotes reais sendo desligados
    at = a * ep(t, tb, 0.3)
    if at > 0:
        title(c, "ANDROID DEBUG BRIDGE", 360, at * (1 - prog(t, tc, 0.25)), INK, 74, hl="DEBUG BRIDGE", hl_col=CYAN)
        n = int(clamp((t - tc) / max(0.1, td - tc - 0.2)) * 25)
        cnt = ep(t, tc + 0.25, 0.2)
        if cnt > 0:
            glow_text(c, f"{n}", CX - 40, 470, 150, "black", AD, at * cnt, align="right", glow=0.35)
            text(c, "APPS", CX - 10, 410, 54, "black", INK, at * cnt, align="left")
            text(c, "DISABLED", CX - 10, 470, 54, "black", AD, at * cnt, align="left")
        x, y, w, h = 60, 540, 960, 620
        terminal(c, x, y, w, h, at, "claude code · bash", CLAUDE)
        lines = [[("$ ", LIME), ("adb connect 192.168.1.42:5555", INK)], [("connected", LIME)]]
        k = int(clamp((t - tc) / max(0.1, td - tc - 0.2)) * len(PKGS))
        rows = [(f"pm disable-user {p}", True) for p in PKGS[:k]]
        yy = y + 110
        for i, ln in enumerate(lines):
            ai = ep(t, tb + 0.25 + i * 0.4, 0.2) * at
            xx = x + 40
            for s, col in ln:
                xx += text(c, s, xx, yy + i * 50, 30, "mono", col, ai, align="left")
        vis = rows[-8:]
        for i, (s, _) in enumerate(vis):
            ly = yy + 110 + i * 50
            text(c, "✕", x + 40, ly, 30, "monob", AD, at, align="left")
            text(c, s, x + 80, ly, 27, "mono", INK2, at, align="left")
    # (d) o que saiu
    tags = (("ADS", 0.0, 250, 1100), ("TRACKING", 0.35, 620, 1030), ("SPONSORED ROWS", 0.7, 540, 1200))
    for s, dt, cx, cy in tags:
        stamp(c, s, cx, cy, AD, a * ep(t, td + dt, 0.2), 44, rot=-6 if cx < 400 else 5)


def b_launcher(c, t, C, B):
    _glitch(C)
    a = fade(t, B["start"], B["end"])
    ta, tb, tc, td = C["04.a"], C["04.b"], C["04.c"], C["04.d"]
    # (a) "escrevendo" o launcher
    al = a * (1 - prog(t, tb, 0.2))
    if al > 0:
        title(c, "NEW HOME SCREEN", 380, al, INK, 82, hl="HOME", hl_col=CLAUDE)
        u = clamp((t - ta) / max(0.3, tb - ta - 0.1))
        terminal(c, 60, 520, 960, 560, al, "claude code", CLAUDE)
        code = ["class Launcher : Activity() {", "  val dock = listOf(Netflix,", "    PrimeVideo, YouTube, Hotstar)",
                "  // no ads. no sponsored rows.", "  fun onHome() = showDock()", "}"]
        for i, ln in enumerate(code[:int(u * len(code)) + 1]):
            text(c, ln, 100, 640 + i * 56, 32, "mono", LIME if "//" in ln else INK, al, align="left")
        bar_meter(c, 100, 1010, 880, 16, u, CLAUDE, al)
        text(c, f"building launcher · {int(474 * u)} KB", 100, 990, 26, "mono", INK2, al, align="left")
    # (b) antes -> (c) depois (fotos reais)
    ab = a * ep(t, tb, 0.15)
    if ab > 0:
        sx, sy = shake(t, tc, 16)
        c.save(); c.translate(sx, sy)
        depois = t >= tc
        w = 960
        x, y, _, h = tv(c, 60, 560, w, ANTES, ab, glow=AD if not depois else LIME)
        if depois:
            u = ep(t, tc, 0.28)
            c.save(); c.clipRect(skia.Rect.MakeXYWH(x, y, w * u, h))
            draw_img(c, DEPOIS, x, y, w, h, ab)
            c.restore()
            c.drawRect(skia.Rect.MakeXYWH(x + w * u - 4, y, 8, h), paint("#FFFFFF", ab * (1 - u)))
            c.drawRect(skia.Rect.MakeWH(W, H), paint("#FFFFFF", 0.45 * (1 - prog(t, tc, 0.18))))
        title(c, "AFTER" if depois else "BEFORE", 410, ab, LIME if depois else AD, 110)
        credit(c, ab)
        c.restore()
        stamp(c, "APPLE TV VIBES", CX, 1150, LIME, a * ep(t, td, 0.2), 50, rot=-4)


def counter(c, cy, val, label, sub, col, a, u, fmt):
    if a <= 0:
        return
    dx = (1 - ease_out(a)) * 60
    rrect(c, 70 + dx, cy - 120, 940, 230, 30, PANEL, 0.9 * a)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(70 + dx, cy - 120, 940, 230), 30, 30), paint(col, 0.75 * a, stroke=3))
    glow_text(c, fmt(val * ease_out(u)), 120 + dx, cy + 30, 120, "black", col, a, align="left", glow=0.3)
    text(c, label, 120 + dx, cy + 82, 36, "extrabold", INK, a, align="left")
    if sub:
        text(c, sub, 990 + dx, cy + 82, 30, "monob", INK2, a, align="right")


def b_viral(c, t, C, B):
    _glitch(C)
    a = fade(t, B["start"], B["end"])
    title(c, "IT WENT VIRAL", 360, a, INK, 92, hl="VIRAL", hl_col=AD)
    ta, tb, tc = C["05.a"], C["05.b"], C["05.c"]
    counter(c, 590, 7.4, "VIEWS ON X", "", CYAN, a * ep(t, ta, 0.3), prog(t, ta, 1.2), lambda v: f"{v:.1f}".replace(".", ",") + " mi" if PT else f"{v:.1f}M")
    counter(c, 870, 27790, "GITHUB STARS", "IN 6 DAYS", GOLD, a * ep(t, tb, 0.3), prog(t, tb, 1.6), lambda v: f"{int(v):,}".replace(",", "." if PT else ","))
    counter(c, 1150, 252, "TV MODELS", "74 BRANDS", LIME, a * ep(t, tc, 0.3), prog(t, tc, 1.0), lambda v: f"{int(v)}")


def b_cuidado(c, t, C, B):
    _glitch(C)
    a = fade(t, B["start"], B["end"])
    title(c, "BEFORE YOU TRY IT", 360, a, INK, 86, hl="TRY IT", hl_col=GOLD)
    ta, tb, tc, td = C["06.a"], C["06.b"], C["06.c"], C["06.d"]
    check_row(c, 60, 560, "ok", "Nothing deleted", a * ep(t, ta, 0.3), LIME)
    check_row(c, 60, 720, "ok", "One command undoes it", a * ep(t, tb + 0.5, 0.3), LIME)
    check_row(c, 60, 880, "warn", "Android & Google TV only", a * ep(t, tc, 0.3), GOLD)
    sx, sy = shake(t, td + 0.6, 12)
    c.save(); c.translate(sx, sy)
    check_row(c, 60, 1040, "no", "At least one TV bricked", a * ep(t, td + 0.5, 0.3), AD)
    c.restore()
    text(c, "source: TechCrunch, Oct 19, 2026", CX, 1200, 24, "mono", DIM, a * ep(t, td + 0.5, 0.3))


def b_final(c, t, C, B):
    _glitch(C)
    a = ep(t, B["start"], 0.3)
    ta, tb = C["07.a"], C["07.b"]
    title(c, "WOULD YOU LET AN AI", 330, a * (1 - prog(t, tb, 0.25)), INK, 78)
    title(c, "INTO YOUR TV?", 430, a * (1 - prog(t, tb, 0.25)), INK, 96, hl="YOUR TV?", hl_col=CLAUDE)
    ab = ep(t, tb, 0.2)
    title(c, "OR KEEP WATCHING THIS?", 400, ab, INK, 80, hl="THIS?", hl_col=AD)
    # a TV "antes" volta (fecha o loop com o começo)
    z = 1.0 + 0.55 * ease_io(prog(t, tb, 1.4))
    x, y, w, h = tv(c, 60, 560, 960, ANTES, a, zoom=z, fx=0.05, fy=0.15, glow=AD)
    if ab > 0:
        pulse = 0.6 + 0.4 * math.sin(t * 12)
        bx, by, bw, bh = x + 26, y + 26, w * 0.62 + (z - 1) * 260, h * 0.36 + (z - 1) * 150
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(bx, by, bw, bh), 12, 12), paint(AD, ab * pulse, stroke=7))
        stamp(c, "AD", bx + bw - 10, by + 8, AD, ab, 52)
    credit(c, a)


BLOCKS = dict(gancho=b_gancho, post=b_post, hack=b_hack, launcher=b_launcher, viral=b_viral, cuidado=b_cuidado,
              final=b_final)
