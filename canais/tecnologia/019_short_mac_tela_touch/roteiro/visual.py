"""Visual do Short 019 (Tecnativo) — o primeiro Mac com tela touch (e o Steve Jobs dizia que não funcionava). 1080x1920.
render.py <proj> --vertical. Mesmo esqueleto vertical dos Shorts 015–018 (fundo, legenda, moldura, glitch).

Sem logos nem fotos: o notebook, o dedo e o braço são desenhos (selo "ilustração"). Fatos, preços e a frase do Jobs:
Apple Newsroom 28/10, MacRumors 28/10, Tecnoblog/TechTudo 28–29/10/2026, evento "Back to the Mac" de 20/10/2010
(original/fonte_mac_tela_touch.md). Cenas 05 e 06 mudam por idioma: preço/data do Brasil (pt) × diferença de preço e
"dá para desligar o toque" (en)."""
import math
import numpy as np
import skia
import idioma
import motor
import tech
from motor import *  # noqa
from tech import *  # noqa

motor.PESOS["mono"] = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono"
motor.PESOS["monob"] = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold"

ARQUIVO_FINAL = "tecnologia_019_short_mac_tela_touch.mp4"
MARCA = ""
SOM = dict(intro=False, ganho_trilha=0.40, lufs=-14, bpm=124, sfx={
    "01.a": ["whoosh", "deny@+2.4"], "01.b": ["glitch", "impact@+0.2", "confirm@+1.4"],
    "02.a": ["data", "pop@+1.0"], "02.b": "whoosh", "02.c": ["deny", "impact@+0.6"],
    "03.a": ["shimmer", "pop@+1.6"], "03.b": ["click", "click@+1.2", "pop@+2.2"], "03.c": "typing",
    "04.a": ["notif", "pop@+0.4"], "04.b": ["confirm", "confirm@+0.5"],
    "05.a": ["glitch", "data@+1.0", "impact@+2.4"], "05.b": ["impact", "alert@+0.3"],
    "06.a": ["notif", "confirm@+1.6"], "06.b": ["click", "deny@+0.4"],
    "07.a": "whoosh", "07.b": "glitch"})

RED = "#FF3B4E"
YEL = "#FFD84A"
CX = W / 2
PT = idioma.LANG == "pt"   # Tecnativo English (--lang en): textos da tela em roteiro/textos_en.py, números no formato EUA
TOP, BOT = 210, 1560          # zona útil

# ---------------------------------------------------------------- utilidades
def fade(t, t0, t1, d=0.35, d_out=0.3):
    return ep(t, t0, d) * (1 - prog(t, t1, d_out))



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
    """carimbo inclinado (PROTOCOLADO, BOLHA?...)"""
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



def shake(t, t0, amp=14, d=0.35):
    u = prog(t, t0, d)
    if u <= 0 or u >= 1:
        return 0.0, 0.0
    k = (1 - u) * amp
    return k * math.sin(t * 90), k * math.cos(t * 77)



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


CAP_Y = 1395


NUMEROS = [("dois mil e dez", "2010"), ("dezesseis anos", "16 anos"),
           ("dois mil oitocentos e noventa e nove dólares", "US$ 2.899"),
           ("trinta e quatro mil novecentos e noventa e nove reais", "R$ 34.999"), ("seis de novembro", "6 de novembro"),
           ("twenty ten", "2010"), ("sixteen years", "16 years"), ("two thousand eight hundred ninety-nine dollars", "$2,899"),
           ("four hundred dollars", "$400"), ("november sixth", "November 6")]


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
                c.drawRect(skia.Rect.MakeXYWH(0, y, W, h), paint(rnd.choice([CYAN, MAGENTA, RED]), 0.12 * (1 - u)))


GLITCH = []


def _glitch(C):
    if not GLITCH:
        GLITCH[:] = [C["01.b"], C["05.a"], C["07.b"]]


def money(c, s, y, col, a, size=170, glow=0.35):
    """valor enorme centralizado (entra crescendo)"""
    if a <= 0:
        return
    k = 0.8 + 0.2 * ease_back(clamp(a))
    c.save(); c.translate(CX, y); c.scale(k, k)
    while text_w(s, "black", size) > 980:
        size -= 4
    glow_text(c, s, 0, 0, size, "black", col, clamp(a), glow=glow)
    c.restore()


def note(c, s, y, a, col=DIM, size=26):
    text(c, s, CX, y, size, "mono", col, a)



def citacao(c, s1, s2, quem, y, a, col=CYAN, size=46):
    if a <= 0:
        return
    panel(c, 70, y, 940, 330, a, col, label="citação")
    text(c, "“", 120, y + 130, 140, "black", col, a, align="left")
    text(c, s1, 200, y + 130, size, "extrabold", INK, a, align="left")
    text(c, s2, 200, y + 195, size, "extrabold", INK, a, align="left")
    text(c, quem, 200, y + 275, 28, "mono", INK2, a, align="left")



def selo(c, a, y=1300, s="ilustração"):
    note(c, s, y, a)


OLED = ("#05060A", "#7C3AED", "#EC4899", "#F59E0B")


def notebook(c, cx, cy, w, a, t, liga=1.0, ilha=0.0, toque=None, desenho=0.0, rolar=0.0, pinca=0.0, x_red=0.0):
    """notebook de frente (desenho, sem logo). liga: tela acesa (OLED, preto profundo + cores); ilha: Dynamic Island
    (0 → 1 expande); toque = (u, v, k) ponto tocado em coordenadas da tela (0–1) com ondinha; desenho/rolar/pinca: gestos;
    x_red: X vermelho sobre a tela (a frase do Jobs)"""
    if a <= 0:
        return
    h = w * 0.64
    x0, y0 = cx - w / 2, cy - h / 2
    rrect(c, x0 - 18, y0 - 18, w + 36, h + 36, 26, "#11151F", a, shadow=True)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x0 - 18, y0 - 18, w + 36, h + 36), 26, 26), paint("#5A6478", a, stroke=3))
    c.save(); c.clipRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x0, y0, w, h), 12, 12), True)
    c.drawRect(skia.Rect.MakeXYWH(x0, y0, w, h), paint("#05060A", a))
    if liga > 0:   # papel de parede OLED: preto puro com faixas de cor brilhantes
        for i, col in enumerate(OLED[1:]):
            p = skia.Paint(AntiAlias=True)
            fx = x0 + w * (0.25 + 0.3 * i) + 40 * math.sin(t * 0.7 + i)
            p.setShader(skia.GradientShader.MakeRadial((fx, y0 + h * (0.7 - 0.15 * i)), w * 0.42,
                                                       [hexc(col), hexc("#05060A")]))
            p.setAlphaf(0.75 * a * liga)
            c.drawRect(skia.Rect.MakeXYWH(x0, y0, w, h), p)
        # janelas genéricas (rolam com o gesto)
        for i in range(3):
            yy = y0 + h * 0.22 + i * h * 0.24 - (rolar * h * 0.3) % (h * 0.24)
            rrect(c, x0 + w * 0.12, yy, w * 0.5, h * 0.17, 10, "#FFFFFF", 0.13 * a * liga)
        if pinca > 0:   # foto que cresce com a pinça
            k = 1 + 0.6 * pinca
            pw, ph = w * 0.26 * k, h * 0.3 * k
            rrect(c, x0 + w * 0.7 - pw / 2, y0 + h * 0.5 - ph / 2, pw, ph, 10, CYAN, 0.55 * a * liga)
        if desenho > 0:   # traço desenhado com o dedo
            pth = skia.Path(); n = 60; m = int(n * clamp(desenho))
            for j in range(m + 1):
                u = j / n
                px = x0 + w * (0.15 + 0.7 * u)
                py = y0 + h * (0.55 + 0.22 * math.sin(u * 2 * math.pi * 1.5))
                (pth.moveTo if j == 0 else pth.lineTo)(px, py)
            c.drawPath(pth, blur_paint(YEL, 0.6 * a, 10, stroke=14))
            c.drawPath(pth, paint(YEL, a, stroke=7, cap_round=True))
    c.restore()
    if ilha > 0:   # Dynamic Island no topo
        iw = w * (0.11 + 0.17 * ease_out(clamp(ilha)))
        ih = h * (0.055 + 0.03 * ease_out(clamp(ilha)))
        rrect(c, cx - iw / 2, y0 + 10, iw, ih, ih / 2, "#000000", a)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - iw / 2, y0 + 10, iw, ih), ih / 2, ih / 2),
                    paint(CYAN, 0.6 * a * ilha, stroke=2))
        if ilha > 0.6:
            c.drawCircle(cx + iw / 2 - ih / 2, y0 + 10 + ih / 2, ih * 0.28, paint(GREEN, a * ilha))
    # base (teclado em perspectiva)
    pth = skia.Path(); pth.moveTo(x0 - 18, y0 + h + 18); pth.lineTo(x0 + w + 18, y0 + h + 18)
    pth.lineTo(x0 + w + 90, y0 + h + 70); pth.lineTo(x0 - 90, y0 + h + 70); pth.close()
    c.drawPath(pth, paint("#2A3142", a)); c.drawPath(pth, paint("#5A6478", a, stroke=3))
    rrect(c, cx - w * 0.12, y0 + h + 40, w * 0.24, 18, 6, "#11151F", a)
    if toque:
        u, v, k = toque
        if k > 0:
            px, py = x0 + w * u, y0 + h * v
            for r_ in range(3):
                rr = (((t * 1.4) + r_ / 3) % 1)
                c.drawCircle(px, py, 18 + 70 * rr, paint(CYAN, a * k * (1 - rr), stroke=4))
            c.drawCircle(px, py, 16, blur_paint(CYAN, 0.8 * a * k, 10))
            c.drawCircle(px, py, 10, paint("#FFFFFF", a * k))
    if x_red > 0:
        L = h * 0.32 * ease_out(clamp(x_red))
        for sg in (1, -1):
            c.drawLine(cx - L, cy - L * sg, cx + L, cy + L * sg, blur_paint(RED, 0.7 * a, 14, stroke=34))
            c.drawLine(cx - L, cy - L * sg, cx + L, cy + L * sg, paint(RED, a, stroke=22, cap_round=True))


def braco(c, x0, y0, x1, y1, a, cansa=0.0):
    """braço (cápsula) do canto de baixo até a tela; cansa 0 → 1: o braço cai"""
    if a <= 0:
        return
    xe = x1 + (x0 - x1) * 0.15 * cansa
    ye = y1 + 260 * cansa ** 1.5
    c.drawLine(x0, y0, xe, ye, paint("#C98B5E", a, stroke=78, cap_round=True))
    c.drawLine(x0, y0, xe, ye, paint("#000000", 0.25 * a, stroke=2))
    c.drawCircle(xe, ye, 26, paint("#E0A576", a))
    if cansa > 0.3:   # gotas de suor
        for i in range(3):
            u = ((cansa * 3 + i * 0.33) % 1)
            c.drawCircle(xe + 60 + i * 26, ye - 70 + 90 * u, 9, paint(CYAN, a * (1 - u)))


def b_gancho(c, t, C, B):
    _glitch(C)
    ta, tb = C["01.a"], C["01.b"]
    a = ep(t, ta, 0.25) * (1 - prog(t, B["end"] - 0.3, 0.3))
    k1 = a * (1 - prog(t, tb, 0.2))
    chip(c, "STEVE JOBS · 2010", CX, 260, GOLD, k1, anchor="center", size=40, filled=True)
    title(c, "\"NÃO FUNCIONA\"", 420, k1 * ep(t, ta + 2.0, 0.2), INK, 92, hl="NÃO FUNCIONA", hl_col=RED)
    k2 = a * ep(t, tb + 0.15, 0.2)
    chip(c, "16 ANOS DEPOIS", CX, 260, CYAN, k2, anchor="center", size=40, filled=True)
    title(c, "1º MAC TOUCH", 420, k2, INK, 104, hl="TOUCH", hl_col=CYAN)
    sx, sy = shake(t, tb + 0.2, 18)
    c.save(); c.translate(sx, sy)
    liga = ep(t, tb + 0.3, 0.5)
    notebook(c, CX, 860, 820, a, t, liga=liga, toque=(0.55, 0.45, ep(t, tb + 1.0, 0.3)),
             x_red=ep(t, ta + 2.2, 0.25) * (1 - prog(t, tb, 0.2)))
    c.restore()
    selo(c, a, 1260)


def b_jobs(c, t, C, B):
    _glitch(C)
    a = fade(t, B["start"], B["end"])
    ta, tb, tc = C["02.a"], C["02.b"], C["02.c"]
    title(c, "O ARGUMENTO", 360, a, INK, 96, hl="ARGUMENTO", hl_col=GOLD)
    citacao(c, "Touch surfaces don't want", "to be vertical.", "Steve Jobs · evento da Apple, 20/10/2010", 450,
            a * ep(t, ta + 0.4, 0.3) * (1 - prog(t, tb, 0.25)), col=GOLD, size=48)
    ub = a * ep(t, tb, 0.3)
    if ub > 0:
        notebook(c, 520, 700, 560, ub, t, liga=0.6)
        cansa = ep(t, tb + 0.4, (tc - tb) + 1.6)
        braco(c, 1060, 1250, 640, 700, ub, cansa)
        citacao(c, "...your arm wants", "to fall off.", "Steve Jobs, 2010", 930, ub * ep(t, tc + 0.6, 0.3), col=RED, size=50)


def b_toque(c, t, C, B):
    _glitch(C)
    a = fade(t, B["start"], B["end"])
    ta, tb, tc = C["03.a"], C["03.b"], C["03.c"]
    title(c, "TELA OLED", 360, a * (1 - prog(t, tb, 0.2)), INK, 104, hl="OLED", hl_col=VIOLET)
    title(c, "+ TOQUE", 360, a * ep(t, tb, 0.2), INK, 110, hl="TOQUE", hl_col=CYAN)
    chip(c, "MacBook Pro · 14\" e 16\"", CX, 470, INK2, a * ep(t, ta + 0.6, 0.3), anchor="center", size=32)
    g1, g2 = tb + 0.9, tb + 2.1     # rolar → pinça → desenhar
    rol = prog(t, g1, 1.0) * 2
    pin = ep(t, g2, 0.8) * (1 - prog(t, tc, 0.3))
    des = prog(t, tc + 0.4, 1.6)
    tq = None
    if t >= tc + 0.4:
        u = clamp((t - tc - 0.4) / 1.6)
        tq = (0.15 + 0.7 * u, 0.55 + 0.22 * math.sin(u * 2 * math.pi * 1.5), a)
    elif t >= g2:
        tq = (0.7, 0.5, a * pin)
    elif t >= g1:
        tq = (0.4, 0.6 - 0.3 * clamp(t - g1), a)
    notebook(c, CX, 860, 860, a, t, liga=1.0, toque=tq, rolar=rol, pinca=pin, desenho=des)
    for i, (s, t0) in enumerate((("rolar", g1), ("zoom", g2), ("desenhar", tc + 0.3))):
        chip(c, s, 250 + i * 290, 1290, CYAN, a * ep(t, t0, 0.3), anchor="center", size=38, filled=t >= t0)
    selo(c, a, 1300)


def b_ilha(c, t, C, B):
    _glitch(C)
    a = fade(t, B["start"], B["end"])
    ta, tb = C["04.a"], C["04.b"]
    title(c, "DYNAMIC ISLAND", 360, a, INK, 92, hl="ISLAND", hl_col=CYAN)
    chip(c, "a ilha do iPhone, agora no Mac", CX, 470, INK2, a * ep(t, ta + 1.0, 0.3), anchor="center", size=32)
    ilha = ep(t, ta + 0.5, 0.8)
    aa = a
    c.save(); k = 1 + 0.25 * ep(t, ta + 0.5, 1.0) * (1 - prog(t, tb, 0.4)) - 0.25 * ep(t, tb, 0.4)   # depois encolhe p/ caber a lista
    c.translate(CX, 560); c.scale(k, k); c.translate(-CX, -560)
    notebook(c, CX, 860, 820, aa, t, liga=1.0, ilha=ilha)
    c.restore()
    ub = a * ep(t, tb, 0.3)
    if ub > 0:
        check_row(c, 60, 1120, "ok", "teclado continua", ep(t, tb + 0.1, 0.3) * ub, GREEN)
        check_row(c, 60, 1260, "ok", "trackpad continua", ep(t, tb + 0.5, 0.3) * ub, GREEN)


def b_preco(c, t, C, B):
    _glitch(C)
    a = fade(t, B["start"], B["end"])
    ta, tb = C["05.a"], C["05.b"]
    title(c, "A CONTA", 360, a, INK, 104, hl="CONTA", hl_col=RED)
    chip(c, "EUA · MacBook Pro 14\" com toque", CX, 470, INK2, a * ep(t, ta + 0.8, 0.3), anchor="center", size=32)
    money(c, "US$ 2.899", 660, GOLD, a * ep(t, ta + 2.2, 0.3), 190)
    text(c, "preço inicial · site da Apple", CX, 750, 30, "mono", INK2, a * ep(t, ta + 2.6, 0.3))
    ub = a * ep(t, tb, 0.3)
    if ub > 0:
        if PT:
            chip(c, "BRASIL", CX, 900, GREEN, ub, anchor="center", size=40, filled=True)
            money(c, "R$ 34.999", 1080, GREEN, ub * ep(t, tb + 1.2, 0.3), 180)
            text(c, "14 polegadas · site da Apple Brasil", CX, 1170, 30, "mono", INK2, ub * ep(t, tb + 1.6, 0.3))
        else:
            x, w = 120, 840
            text(c, "sem toque (mini-LED)", x, 880, 36, "extrabold", INK, ub, align="left")
            rrect(c, x, 905, w * 0.86 * ep(t, tb, 0.6), 60, 14, INK2, ub)
            text(c, "com toque (OLED)", x, 1040, 36, "extrabold", INK, ub, align="left")
            rrect(c, x, 1065, w * ep(t, tb + 0.3, 0.6), 60, 14, GOLD, ub)
            stamp(c, "+US$ 400", 780, 1100, RED, ub * ep(t, tb + 0.9, 0.2), 54, rot=-6)
            note(c, "fonte: MacRumors · os modelos sem toque continuam à venda", 1210, ub, size=22)


def calendario(c, cx, cy, dia, mes, a, col=CYAN):
    if a <= 0:
        return
    rrect(c, cx - 170, cy - 170, 340, 340, 34, PANEL, 0.95 * a, shadow=True)
    rrect(c, cx - 170, cy - 170, 340, 90, 34, col, a)
    c.drawRect(skia.Rect.MakeXYWH(cx - 170, cy - 110, 340, 30), paint(col, a))
    text_mid(c, mes, cx, cy - 125, 44, "black", "#0B0F1A", a)
    text_mid(c, dia, cx, cy + 50, 170, "black", INK, a)


def interruptor(c, cx, cy, on, a):
    """chave liga/desliga (on 1 → 0 desliga)"""
    if a <= 0:
        return
    w, h = 220, 110
    col = GREEN if on > 0.5 else "#5A6478"
    rrect(c, cx - w / 2, cy - h / 2, w, h, h / 2, col, a)
    x = cx - w / 2 + h / 2 + (w - h) * on
    c.drawCircle(x, cy, h / 2 - 10, paint("#FFFFFF", a))


def b_data(c, t, C, B):
    _glitch(C)
    a = fade(t, B["start"], B["end"])
    ta, tb = C["06.a"], C["06.b"]
    title(c, "PRÉ-VENDA ABERTA", 360, a, INK, 88, hl="ABERTA", hl_col=GREEN)
    ua = a * (1 - prog(t, tb, 0.25) * (0 if PT else 1))
    calendario(c, CX, 720, "6", "NOV" if PT else "NOV", ua * ep(t, ta + 1.2, 0.3))
    text(c, "entregas nos EUA · sexta, 6/11/2026", CX, 950, 32, "mono", INK2, ua * ep(t, ta + 1.6, 0.3))
    ub = a * ep(t, tb, 0.3)
    if ub > 0:
        if PT:
            stamp(c, "BRASIL: SEM DATA", CX, 1120, GOLD, ub, 58, rot=-5)
            note(c, "a Apple ainda não informou a previsão (Tecnoblog)", 1225, ub, size=24)
        else:
            text(c, "TOUCH", CX, 640, 70, "black", INK, ub)
            interruptor(c, CX, 790, 1 - ep(t, tb + 1.2, 0.4), ub)
            text(c, "you can turn it off (MacRumors)", CX, 920, 30, "mono", INK2, ub)


def b_final(c, t, C, B):
    _glitch(C)
    a = ep(t, B["start"], 0.3)
    ta, tb = C["07.a"], C["07.b"]
    notebook(c, CX, 900, 820, a, t, liga=1.0, toque=(0.5, 0.5, 0.6 + 0.4 * math.sin(t * 3)))
    aa = a * (1 - prog(t, tb, 0.25))
    title(c, "O STEVE JOBS", 340, aa, INK, 86)
    title(c, "ESTAVA ERRADO?", 450, aa, INK, 92, hl="ERRADO?", hl_col=RED)
    ab = ep(t, tb, 0.2)
    title(c, "VOCÊ TOCARIA", 340, ab, INK, 86)
    title(c, "NA TELA?", 450, ab, INK, 110, hl="TELA?", hl_col=CYAN)


BLOCKS = dict(gancho=b_gancho, jobs=b_jobs, toque=b_toque, ilha=b_ilha, preco=b_preco, data=b_data, final=b_final)
