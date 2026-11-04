"""Visual do Short 015 (Tecnativo) — o pedido de IPO da Anthropic na Nasdaq. 1080x1920.
render.py <proj> --vertical. Tema 'tech' (cores, painéis, chips) com fundo, legenda e moldura verticais do Short 012:
zona útil entre y=200 e y=1560 (a interface do Shorts cobre o rodapé e a lateral direita).

Sem logos nem fotos: só gráficos desenhados aqui. Números do S-1 (SEC, 26/10/2026); captação de US$ 100 bi e recorde da
SpaceX vêm da imprensa e aparecem marcados assim na tela (original/fonte_ipo_anthropic.md)."""
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

ARQUIVO_FINAL = "tecnologia_015_short_ipo_anthropic.mp4"
MARCA = ""
SOM = dict(intro=False, ganho_trilha=0.40, lufs=-14, bpm=124, sfx={
    "01.a": ["alert", "impact@+0.9"], "01.b": ["glitch", "shimmer@+0.4"],
    "02.a": ["typing", "lock@+1.0"], "02.b": "impact",
    "03.a": ["data", "data@+0.5"], "03.b": "data", "03.c": ["impact", "shimmer@+0.3"],
    "04.a": "alert", "04.b": "data", "04.c": "pop", "04.d": "confirm",
    "05.a": "data", "05.b": "data", "05.c": "glitch",
    "06.a": "lock", "06.b": "confirm",
    "07.a": "notif", "07.b": "glitch"})

CLAUDE = "#E8825A"   # laranja "Claude" (só cor, sem logo)
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
    # brilho vermelho no gancho (o prejuízo)
    red = fade(t, 0, 3.6, 0.01, 0.6)
    if red > 0:
        c.drawCircle(CX, 640, 620, blur_paint(RED, 0.13 * red, 160))


CAP_Y = 1395


NUMEROS = [("oitenta bilhões de dólares", "US$ 80 bilhões"), ("seis meses", "6 meses"),
           ("dois mil e vinte e três", "2023"), ("quarenta e um milhões", "41 milhões"),
           ("dois mil e vinte e cinco", "2025"), ("quatro vírgula seis bilhões", "4,6 bilhões"),
           ("dezesseis vírgula três bilhões", "16,3 bilhões"), ("setenta e dois bilhões", "72 bilhões"),
           ("seiscentos e noventa e três milhões", "693 milhões"), ("cem bilhões", "100 bilhões"),
           ("setenta e cinco bilhões", "75 bilhões"), ("sete fundadores", "7 fundadores"),
           ("cinquenta vírgula um por cento", "50,1%"),
           ("eighty billion dollars", "$80 billion"), ("six months", "6 months"), ("twenty twenty-three", "2023"),
           ("forty-one million", "41 million"), ("twenty twenty-five", "2025"), ("four point six billion", "4.6 billion"),
           ("sixteen point three billion", "16.3 billion"), ("seventy-two billion", "72 billion"),
           ("six hundred ninety-three million", "693 million"), ("a hundred billion", "100 billion"),
           ("seventy-five billion", "75 billion"), ("seven founders", "7 founders"),
           ("fifty point one percent", "50.1%")]


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
        GLITCH[:] = [C["01.b"], C["04.b"], C["07.b"]]


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


def chart_up(c, x, y, w, h, u, col, a):
    """linha de bolsa subindo (desenhada até a fração u)"""
    pts = [(0, 0.05), (0.12, 0.12), (0.22, 0.08), (0.35, 0.25), (0.45, 0.2), (0.58, 0.42), (0.68, 0.36), (0.8, 0.62),
           (0.88, 0.58), (1.0, 0.95)]
    pth = skia.Path()
    n = min(len(pts), max(2, int(len(pts) * clamp(u)) + 1))
    for i, (px, py) in enumerate(pts[:n]):
        X, Y = x + px * w, y + h - py * h
        pth.moveTo(X, Y) if i == 0 else pth.lineTo(X, Y)
    c.drawPath(pth, blur_paint(col, 0.5 * a, 14, stroke=10))
    c.drawPath(pth, paint(col, a, stroke=8, cap_round=True))
    px, py = pts[n - 1]
    c.drawCircle(x + px * w, y + h - py * h, 14, paint(col, a))


# ---------------------------------------------------------------- blocos
def b_gancho(c, t, C, B):
    _glitch(C)
    ta, tb = C["01.a"], C["01.b"]
    out = 1 - prog(t, B["end"] - 0.3, 0.3)
    aa = ep(t, ta + 0.1, 0.3) * (1 - prog(t, tb - 0.1, 0.25))
    if aa > 0:
        chip(c, "EMPRESA DO CLAUDE", CX, 420, CLAUDE, aa, anchor="center", size=34, filled=True)
        sx, sy = shake(t, ta + 1.55, 20)
        c.save(); c.translate(sx, sy)
        money(c, "-US$ 80 BI", 740, RED, ep(t, ta + 1.5, 0.3) * aa, 200)
        c.restore()
        title(c, "EM 6 MESES", 940, ep(t, ta + 3.3, 0.25) * aa, INK, 96, hl="6 MESES", hl_col=RED)
    ab = ep(t, tb, 0.25) * out
    if ab > 0:
        title(c, "E MESMO ASSIM...", 400, ab, INK, 80)
        chart_up(c, 120, 520, 840, 460, prog(t, tb + 0.3, 2.0), LIME, ab)
        stamp(c, "MAIOR IPO DA HISTÓRIA?", CX, 1130, GOLD, ab * ep(t, tb + 1.2, 0.2), 52, rot=-4)


def b_s1(c, t, C, B):
    _glitch(C)
    a = fade(t, B["start"], B["end"])
    ta, tb = C["02.a"], C["02.b"]
    title(c, "SEGUNDA, 26/10", 370, a, INK, 84, hl="26/10", hl_col=CLAUDE)
    # documento oficial (recriado; o S-1 é público na SEC); some quando entra o letreiro da bolsa
    a0 = a
    a = a * (1 - prog(t, tb, 0.3))
    k = ease_out(a)
    x, y, w, h = 150, 480 + (1 - k) * 40, 780, 640
    panel(c, x, y, w, h, a, CYAN, label="sec.gov")
    text(c, "FORM S-1", x + 60, y + 120, 64, "black", INK, a, align="left")
    text(c, "REGISTRATION STATEMENT", x + 60, y + 175, 30, "monob", INK2, a, align="left")
    text(c, "Anthropic, PBC", x + 60, y + 270, 52, "extrabold", CLAUDE, a, align="left")
    for i, ln in enumerate(["Class A common stock", "Nasdaq Global Select Market", "price per share: $ __ – $ __"]):
        text(c, ln, x + 60, y + 360 + i * 56, 32, "mono", INK2, a * ep(t, ta + 0.4 + i * 0.25, 0.2), align="left")
    stamp(c, "PROTOCOLADO", x + w - 190, y + h - 70, LIME, a * ep(t, ta + 1.0, 0.2), 40, rot=-8)
    # (b) letreiro da bolsa
    ab = a0 * ep(t, tb, 0.25)
    if ab > 0:
        bw, bh = 900, 300
        bx, by = CX - bw / 2, 720
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(bx, by, bw, bh), 26, 26), blur_paint(LIME, 0.35 * ab, 30))
        rrect(c, bx, by, bw, bh, 26, "#050A0C", ab)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(bx, by, bw, bh), 26, 26), paint(LIME, ab, stroke=4))
        text(c, "NASDAQ", CX, by + 90, 46, "monob", INK2, ab)
        glow_text(c, "ANT", CX, by + 230, 150, "black", LIME, ab, glow=0.4)
        note(c, "código pedido no S-1", by + bh + 50, ab)


BARRAS = [("2023", 0.041, "US$ 41 mi"), ("2024", 0.386, "US$ 386 mi"), ("2025", 4.6, "US$ 4,6 bi"),
          ("1º SEM.\n2026", 16.3, "US$ 16,3 bi")]


def b_receita(c, t, C, B):
    _glitch(C)
    a = fade(t, B["start"], B["end"])
    ta, tb, tc = C["03.a"], C["03.b"], C["03.c"]
    title(c, "RECEITA", 370, a, INK, 96, hl="RECEITA", hl_col=LIME)
    base, top = 1180, 560
    x0, bw, gap = 110, 190, 50
    c.drawLine(80, base, 1000, base, paint(INK2, 0.6 * a, stroke=3))
    quando = [ta + 0.9, ta + 2.6, tb + 0.6, tc + 1.2]
    for i, (rot, v, lab) in enumerate(BARRAS):
        u = ep(t, quando[i], 0.6) * a
        x = x0 + i * (bw + gap)
        hh = max(6, (base - top - 120) * v / 16.3) * u
        col = GOLD if i == 3 else LIME
        if u > 0:
            if i == 3:
                c.drawRect(skia.Rect.MakeXYWH(x - 8, base - hh - 8, bw + 16, hh + 8), blur_paint(GOLD, 0.45 * a, 26))
            rrect(c, x, base - hh, bw, hh, 10, col, 0.9 * u)
            text(c, lab, x + bw / 2, base - hh - 24, 34 if i < 3 else 40, "black", col, u)
        for j, ln in enumerate(rot.split("\n")):
            text(c, ln, x + bw / 2, base + 50 + j * 36, 32, "monob", INK if i == 3 else INK2, a)
    stamp(c, "+1.300% EM 1 ANO", CX, 520, GOLD, a * ep(t, tc + 2.2, 0.2), 46, rot=-4)
    note(c, "fonte: S-1 da Anthropic (SEC)", 1290, a)


def b_prejuizo(c, t, C, B):
    _glitch(C)
    a = fade(t, B["start"], B["end"])
    ta, tb, tc, td = C["04.a"], C["04.b"], C["04.c"], C["04.d"]
    title(c, "E O PREJUÍZO?", 370, a, INK, 92, hl="PREJUÍZO?", hl_col=RED)
    money(c, "-US$ 80,7 BI", 560, RED, a * ep(t, ta + 0.4, 0.3), 130, 0.3)
    note(c, "prejuízo líquido · 1º semestre 2026", 630, a * ep(t, ta + 0.4, 0.3), INK2, 28)
    # barra dividida: 72,4 de contabilidade + 8,3 do resto
    x, y, w, h = 90, 700, 900, 110
    ub = ep(t, tb, 0.5) * a
    if ub > 0:
        rrect(c, x, y, w, h, 16, RED, 0.25 * a)
        w1 = w * 72.4 / 80.7 * ub
        rrect(c, x, y, w1, h, 16, VIOLET, 0.95 * ub)
        text_mid(c, "72,4 bi: CONTABILIDADE", x + 30, y + h / 2, 40, "black", "#120A24", ub, align="left")
        text_mid(c, "8,3", x + w - 20, y + h / 2, 34, "black", INK, ub, align="right")
    # (c) explicação: valor da empresa sobe -> dívidas conversíveis "encarecem" no balanço
    uc = ep(t, tc, 0.3) * a * (1 - prog(t, td, 0.3))
    if uc > 0:
        panel(c, 90, 860, 900, 300, uc, VIOLET, label="valor justo")
        text(c, "valor da empresa", 140, 950, 40, "extrabold", INK, uc, align="left")
        arrow(c, 860, 960, 860, 900, LIME, uc, 8, 22)
        u2 = ep(t, tc + 2.0, 0.3) * uc
        text(c, "dívidas que viram ações", 140, 1050, 40, "extrabold", INK, u2, align="left")
        text(c, "pesam mais no balanço", 140, 1100, 34, "medium", INK2, u2, align="left")
        arrow(c, 860, 1080, 860, 1020, RED, u2, 8, 22)
        text(c, "não é dinheiro saindo do caixa", CX, 1130 + 70, 26, "mono", DIM, u2)
    ud = ep(t, td, 0.3) * a
    if ud > 0:
        panel(c, 90, 880, 900, 260, ud, GOLD, label="operação")
        text(c, "PREJUÍZO OPERACIONAL", CX, 960, 38, "monob", INK2, ud)
        money(c, "-US$ 693 MI", 1080, GOLD, ud, 110, 0.3)
        note(c, "era -US$ 2,1 bi no 1º semestre de 2025 · fonte: S-1", 1200, ud)


def b_recorde(c, t, C, B):
    _glitch(C)
    a = fade(t, B["start"], B["end"])
    ta, tb, tc = C["05.a"], C["05.b"], C["05.c"]
    title(c, "RECORDE?", 370, a, INK, 100, hl="RECORDE?", hl_col=GOLD)
    x, w = 90, 900
    rows = [("ANTHROPIC", "~US$ 100 bi", 100, CLAUDE, ta + 0.6, "projeção da imprensa", True),
            ("SPACEX · JUN/2026", "US$ 75 bi", 75, CYAN, tb + 0.6, "recorde atual", False)]
    for i, (nm, val, v, col, t0, sub, dash) in enumerate(rows):
        u = ep(t, t0, 0.6) * a
        y = 560 + i * 260
        text(c, nm, x, y, 40, "black", INK, a * ep(t, t0 - 0.4, 0.3), align="left")
        text(c, sub, x + w, y, 26, "mono", INK2, a * ep(t, t0 - 0.4, 0.3), align="right")
        bwid = w * v / 100 * u
        if dash:
            rrect(c, x, y + 30, bwid, 110, 14, col, 0.35 * u)
            c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y + 30, max(1, bwid), 110), 14, 14),
                        paint(col, u, stroke=4))
        else:
            rrect(c, x, y + 30, bwid, 110, 14, col, 0.9 * u)
        text_mid(c, val, x + 30, y + 85, 52, "black", INK if dash else "#04121A", u, align="left")
    note(c, "captação em uma estreia na bolsa (IPO)", 1080, a * ep(t, tb + 0.6, 0.3))
    sx, sy = shake(t, tc + 0.2, 12)
    c.save(); c.translate(sx, sy)
    stamp(c, "PREÇO DA AÇÃO: ???", CX, 1190, RED, a * ep(t, tc + 0.1, 0.2), 48, rot=-4)
    c.restore()


def b_controle(c, t, C, B):
    _glitch(C)
    a = fade(t, B["start"], B["end"])
    ta, tb = C["06.a"], C["06.b"]
    title(c, "QUEM MANDA?", 370, a, INK, 96, hl="MANDA?", hl_col=VIOLET)
    # rosca: 50,1% dos votos com os fundadores
    cx, cy, r = CX, 760, 230
    u = ep(t, ta + 1.2, 1.0) * a
    rect = skia.Rect.MakeXYWH(cx - r, cy - r, 2 * r, 2 * r)
    c.drawArc(rect, 0, 360, False, paint("#1A2236", a, stroke=70))
    if u > 0:
        c.drawArc(rect, -90, 360 * 0.501 * u, False, paint(CLAUDE, a, stroke=70))
    glow_text(c, f"{50.1 * u:.1f}%".replace(".", "," if PT else "."), cx, cy + 10, 100, "black", CLAUDE, a * ep(t, ta + 1.2, 0.3), glow=0.3)
    text(c, "DOS VOTOS", cx, cy + 70, 34, "monob", INK2, a * ep(t, ta + 1.2, 0.3))
    chip(c, "7 FUNDADORES", cx, 1060, CLAUDE, a * ep(t, ta + 1.0, 0.3), anchor="center", size=34, filled=True)
    ub = ep(t, tb, 0.3) * a
    if ub > 0:
        panel(c, 90, 1110, 900, 150, ub, VIOLET, label="Long-Term Benefit Trust")
        text_mid(c, "fundo independente elege", CX, 1165, 36, "extrabold", INK, ub)
        text_mid(c, "a maioria do conselho", CX, 1215, 36, "extrabold", VIOLET, ub)


def bolha(c, cx, cy, r, a, t):
    if a <= 0:
        return
    rr = r * (0.92 + 0.08 * math.sin(t * 3))
    p = skia.Paint(AntiAlias=True)
    p.setShader(skia.GradientShader.MakeRadial(center=(cx - rr * 0.3, cy - rr * 0.35), radius=rr * 1.3,
                                               colors=[hexc("#FFFFFF", 0.25 * a), hexc(CYAN, 0.08 * a), hexc(MAGENTA, 0.18 * a)],
                                               positions=[0, 0.6, 1]))
    c.drawCircle(cx, cy, rr, p)
    c.drawCircle(cx, cy, rr, paint(CYAN, 0.7 * a, stroke=4))
    c.drawArc(skia.Rect.MakeXYWH(cx - rr * 0.7, cy - rr * 0.7, rr * 1.4, rr * 1.4), 200, 50, False,
              paint("#FFFFFF", 0.7 * a, stroke=10, cap_round=True))


def b_final(c, t, C, B):
    _glitch(C)
    a = ep(t, B["start"], 0.3)
    ta, tb = C["07.a"], C["07.b"]
    aa = a * (1 - prog(t, tb, 0.25))
    title(c, "VOCÊ COMPRARIA", 380, aa, INK, 90)
    title(c, "UMA AÇÃO ANT?", 490, aa, INK, 96, hl="ANT?", hl_col=LIME)
    chart_up(c, 120, 600, 840, 440, prog(t, ta + 0.3, 1.8), LIME, aa)
    ab = ep(t, tb, 0.2)
    if ab > 0:
        title(c, "OU É BOLHA?", 420, ab, INK, 110, hl="BOLHA?", hl_col=MAGENTA)
        bolha(c, CX, 820, 300 * (0.7 + 0.3 * ease_back(ab)), ab, t)
        text_mid(c, "IA", CX, 820, 120, "black", INK, ab)
    note(c, "não é recomendação de investimento", 1240, a, INK2)


BLOCKS = dict(gancho=b_gancho, s1=b_s1, receita=b_receita, prejuizo=b_prejuizo, recorde=b_recorde, controle=b_controle,
              final=b_final)
