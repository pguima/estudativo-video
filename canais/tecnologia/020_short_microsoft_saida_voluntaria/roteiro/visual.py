"""Visual do Short 020 (Tecnativo) — a Microsoft oferece saída voluntária a 60 mil funcionários (por causa da IA). 1080x1920.
render.py <proj> --vertical. Mesmo esqueleto vertical dos Shorts 015–019 (fundo, legenda, moldura, glitch).

Sem logos nem fotos: pessoas, prédio, servidores e memorando são desenhos (selo "ilustração"). Fatos, números e a frase da
chefe de pessoas: SiliconANGLE, Yahoo Finance, Tom's Hardware e CNBC, 26–27/10/2026 (original/fonte_microsoft_saida_voluntaria.md)."""
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

ARQUIVO_FINAL = "tecnologia_020_short_microsoft_saida_voluntaria.mp4"
MARCA = ""
SOM = dict(intro=False, ganho_trilha=0.40, lufs=-14, bpm=124, sfx={
    "01.a": ["whoosh", "data@+1.2", "impact@+2.2"], "01.b": ["glitch", "alert@+0.2"],
    "02.a": ["pop", "pop@+0.6", "pop@+1.1", "pop@+1.6"], "02.b": ["impact", "alert@+0.3"],
    "03.a": ["data", "click@+2.0"], "03.b": ["confirm", "confirm@+0.6"],
    "04.a": ["glitch", "impact@+0.9"], "04.b": ["data", "impact@+2.6"], "04.c": "data",
    "05.a": "click", "05.b": ["impact", "alert@+0.4"],
    "06.a": ["notif", "click@+1.2"], "06.b": "typing", "06.c": ["typing", "confirm@+2.0"],
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


NUMEROS = [("sessenta mil", "60 mil"),
           ("cento e setenta bilhões de dólares", "US$ 170 bilhões"), ("nove mil", "9 mil"), ("sete vezes", "7 vezes"),
           ("uma ou duas", "1 ou 2"), ("seis meses", "6 meses"),
           ("sixty thousand", "60,000"),
           ("one hundred seventy billion dollars", "$170 billion"), ("nine thousand", "9,000"), ("seven times", "7 times"),
           ("one or two", "1 or 2"), ("six months", "6 months")]


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
        GLITCH[:] = [C["01.b"], C["04.a"], C["07.b"]]


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


SAI = sorted(range(240), key=lambda i: hash01(i, 11))[:60]   # 60 de 240 (1/4) saem
SAI_SET = set(SAI)


def pessoa(c, x, y, s, a, col):
    """bonequinho: cabeça + ombros"""
    if a <= 0:
        return
    c.drawCircle(x, y - s * 0.55, s * 0.42, paint(col, a))
    pth = skia.Path(); pth.addArc(skia.Rect.MakeXYWH(x - s * 0.75, y - s * 0.05, s * 1.5, s * 1.3), 180, 180)
    c.drawPath(pth, paint(col, a))


def multidao(c, a, t, t0=None, sai=0.0, y0=560, cols=16, rows=15, dx=58, dy=46, s=17, pisca=None):
    """240 funcionários; os 60 de SAI ficam vermelhos (a partir de t0) e saem pela direita conforme sai (0 → 1)"""
    x0 = CX - (cols - 1) * dx / 2
    for i in range(cols * rows):
        r, q = divmod(i, cols)
        x, y = x0 + q * dx, y0 + r * dy
        col, aa = INK2, a * 0.85
        if i in SAI_SET and t0 is not None and t >= t0 + 0.02 * SAI.index(i):
            col = RED
            u = clamp(sai * 1.6 - 0.6 * hash01(i, 5))
            x += u * 700
            aa = a * (1 - u)
        pessoa(c, x, y, s, aa, col)


def predio(c, cx, cy, a, t):
    """prédio de escritórios (desenho genérico)"""
    if a <= 0:
        return
    rrect(c, cx - 200, cy - 300, 400, 600, 14, "#1B2130", a, shadow=True)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - 200, cy - 300, 400, 600), 14, 14), paint("#5A6478", a, stroke=3))
    for r in range(8):
        for q in range(5):
            on = hash01(r * 5 + q, int(t * 2)) > 0.35
            rrect(c, cx - 170 + q * 70, cy - 270 + r * 70, 46, 44, 6, GOLD if on else "#2A3142", a * (0.9 if on else 0.6))


def rack(c, x, y, w, h, a, t, k=0):
    """servidor de data center com LEDs piscando"""
    if a <= 0:
        return
    rrect(c, x, y, w, h, 12, "#141A28", a)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 12, 12), paint("#5A6478", a, stroke=2.5))
    n = int(h // 44)
    for i in range(n):
        yy = y + 14 + i * 44
        rrect(c, x + 12, yy, w - 24, 32, 6, "#1F2738", a)
        for j in range(4):
            on = hash01(i * 7 + j + k * 31, int(t * 6)) > 0.45
            c.drawCircle(x + w - 30 - j * 18, yy + 16, 5, paint(CYAN if j % 2 else GREEN, a * (1 if on else 0.2)))


def b_gancho(c, t, C, B):
    _glitch(C)
    ta, tb = C["01.a"], C["01.b"]
    a = ep(t, ta, 0.25) * (1 - prog(t, B["end"] - 0.3, 0.3))
    title(c, "MICROSOFT", 330, a, INK, 110, hl="MICROSOFT", hl_col=CYAN)
    t0 = ta + 1.2
    multidao(c, a, t, t0, ep(t, tb + 0.6, 2.2), y0=560)
    money(c, "60 MIL" if PT else "60,000", 470, RED, a * ep(t, ta + 2.0, 0.3), 120)
    stamp(c, "≈ 1/4 DA EMPRESA", CX, 1300, RED, a * ep(t, tb + 0.3, 0.2), 58, rot=-5)
    selo(c, a, 1250)


def b_quem(c, t, C, B):
    _glitch(C)
    a = fade(t, B["start"], B["end"])
    ta, tb = C["02.a"], C["02.b"]
    title(c, "ONDE VALE", 340, a, INK, 104, hl="VALE", hl_col=GOLD)
    for i, s in enumerate(["EUA", "CANADÁ", "ÍNDIA", "REINO UNIDO"]):
        k = a * ep(t, ta + 0.1 + i * 0.5, 0.25)
        chip(c, s, CX, 520 + i * 130, CYAN, k, anchor="center", size=58, filled=True)
    ub = a * ep(t, tb, 0.3)
    if ub > 0:
        stamp(c, "ATÉ VICE-PRESIDENTE", CX, 1120, GOLD, ub, 64, rot=-5)
        note(c, "nível interno 70 ou abaixo · algumas equipes ficaram de fora", 1240, ub, size=24)


def b_pacote(c, t, C, B):
    _glitch(C)
    a = fade(t, B["start"], B["end"])
    ta, tb = C["03.a"], C["03.b"]
    title(c, "O PACOTE", 340, a, INK, 110, hl="PACOTE", hl_col=GREEN)
    chip(c, "segundo o Business Insider", CX, 450, INK2, a * ep(t, ta + 0.4, 0.3), anchor="center", size=30)
    ua = a * ep(t, ta + 1.4, 0.3)
    if ua > 0:   # linha do tempo: a cada 6 meses de casa, 1 ou 2 semanas de salário
        x0, w = 120, 840
        c.drawLine(x0, 640, x0 + w, 640, paint(INK2, ua, stroke=4))
        for i in range(5):
            x = x0 + i * w / 4
            k = ua * ep(t, ta + 1.6 + i * 0.25, 0.25)
            c.drawCircle(x, 640, 12, paint(INK, k))
            text(c, f"{6 * i}m" if PT else f"{6 * i}mo", x, 600, 28, "mono", INK2, k)
            if i:
                rrect(c, x - 60, 670, 120, 70, 14, GREEN, k)
                text_mid(c, "+1–2 sem." if PT else "+1–2 wks", x, 705, 30, "black", "#04130A", k)
        text(c, "semanas de salário a cada 6 meses de casa", CX, 800, 30, "mono", INK2, ua)
    ub = a * ep(t, tb, 0.3)
    if ub > 0:
        check_row(c, 60, 950, "ok", "ações por 6 a 12 meses", ep(t, tb + 0.1, 0.3) * ub, GREEN)
        check_row(c, 60, 1090, "warn", "plano de saúde por um tempo", ep(t, tb + 0.6, 0.3) * ub, GOLD)


def b_motivo(c, t, C, B):
    _glitch(C)
    a = fade(t, B["start"], B["end"])
    ta, tb, tc = C["04.a"], C["04.b"], C["04.c"]
    title(c, "O MOTIVO?", 340, a * (1 - prog(t, ta + 0.9, 0.2)), INK, 110, hl="MOTIVO?", hl_col=GOLD)
    title(c, "IA", 340, a * ep(t, ta + 0.9, 0.2), INK, 150, hl="IA" if PT else "AI", hl_col=VIOLET)
    money(c, "US$ 170 BI+", 560, GOLD, a * ep(t, tb + 2.4, 0.3), 160)
    text(c, "investimento planejado em 2026", CX, 640, 30, "mono", INK2, a * ep(t, tb + 2.8, 0.3))
    uc = a * ep(t, tc - 0.3, 0.3)
    for i in range(4):
        rack(c, 110 + i * 220, 760, 190, 400, uc * ep(t, tc - 0.3 + i * 0.15, 0.3), t, i)
    text(c, "data centers de IA", CX, 1210, 36, "black", CYAN, uc)
    selo(c, a, 1270)


def b_maio(c, t, C, B):
    _glitch(C)
    a = fade(t, B["start"], B["end"])
    ta, tb = C["05.a"], C["05.b"]
    title(c, "EM MAIO", 340, a * (1 - prog(t, tb, 0.2)), INK, 110, hl="MAIO", hl_col=GOLD)
    title(c, "AGORA", 340, a * ep(t, tb, 0.2), INK, 120, hl="AGORA", hl_col=RED)
    x, w = 120, 840
    ua = a * ep(t, ta + 0.4, 0.3)
    text(c, "maio de 2026", x, 560, 38, "extrabold", INK, ua, align="left")
    rrect(c, x, 585, w * (9 / 60) * ep(t, ta + 0.5, 0.5), 80, 14, GOLD, ua)
    text(c, "9 MIL" if PT else "9,000", x + w * 9 / 60 + 24, 640, 48, "black", GOLD, ua * ep(t, ta + 1.4, 0.3), align="left")
    ub = a * ep(t, tb - 0.3, 0.3)
    text(c, "outubro de 2026", x, 800, 38, "extrabold", INK, ub, align="left")
    rrect(c, x, 825, w * ep(t, tb - 0.2, 0.8), 80, 14, RED, ub)
    text(c, "60 MIL" if PT else "60,000", x + w - 24, 880, 48, "black", "#2A0508", ub * ep(t, tb + 0.6, 0.3), align="right")
    stamp(c, "QUASE 7×", CX, 1080, RED, ub * ep(t, tb + 0.9, 0.2), 80, rot=-6)


def memo(c, y, a, t, t0):
    """memorando com a frase (digitada)"""
    if a <= 0:
        return
    panel(c, 70, y, 940, 420, a, CYAN, label="memorando aos funcionários")
    linhas = ["\"The Voluntary Exit Offer", "is new for us.", "We'll learn from it.\""]
    tot = sum(len(s) for s in linhas)
    n = int(tot * clamp((t - t0) / 1.6))
    for i, s in enumerate(linhas):
        k = max(0, min(len(s), n)); n -= len(s)
        text(c, s[:k], 120, y + 120 + i * 80, 52, "extrabold", CYAN if i else INK, a, align="left")
    text(c, "Amy Coleman, chefe de pessoas da Microsoft", 120, y + 370, 28, "mono", INK2, a, align="left")


def b_memo(c, t, C, B):
    _glitch(C)
    a = fade(t, B["start"], B["end"])
    ta, tb, tc = C["06.a"], C["06.b"], C["06.c"]
    title(c, "PRAZO", 340, a * (1 - prog(t, tb, 0.2)), INK, 120, hl="PRAZO", hl_col=GOLD)
    ua = a * ep(t, ta + 0.3, 0.3) * (1 - prog(t, tb, 0.25))
    if ua > 0:
        rrect(c, CX - 190, 520, 380, 380, 36, PANEL, 0.95 * ua, shadow=True)
        rrect(c, CX - 190, 520, 380, 100, 36, GOLD, ua)
        c.drawRect(skia.Rect.MakeXYWH(CX - 190, 590, 380, 30), paint(GOLD, ua))
        text_mid(c, "DEZ" if PT else "DEC", CX, 570, 52, "black", "#0B0F1A", ua)
        text_mid(c, "início" if PT else "early", CX, 760, 90, "black", INK, ua)
        text(c, "quem aceitar sai em dezembro", CX, 980, 32, "mono", INK2, ua)
    ub = a * ep(t, tb, 0.3)
    if ub > 0:
        title(c, "O MEMORANDO", 340, ub, INK, 100, hl="MEMORANDO", hl_col=CYAN)
        memo(c, 520, ub, t, tc - 0.6)
        text(c, "\"isso é novo para nós. vamos aprender.\"", CX, 1060, 36, "extrabold", CYAN, ub * ep(t, tc + 1.2, 0.3))


def b_final(c, t, C, B):
    _glitch(C)
    a = ep(t, B["start"], 0.3)
    ta, tb = C["07.a"], C["07.b"]
    multidao(c, a, t, B["start"], 0.0, y0=620)
    aa = a * (1 - prog(t, tb, 0.25))
    title(c, "SE TE PAGASSEM", 340, aa, INK, 86)
    title(c, "PARA SAIR?", 450, aa, INK, 100, hl="SAIR?", hl_col=RED)
    ab = ep(t, tb, 0.2)
    title(c, "OU A IA CHEGA", 340, ab, INK, 86, hl="IA", hl_col=VIOLET)
    title(c, "DE QUALQUER JEITO?", 450, ab, INK, 90, hl="JEITO?", hl_col=RED)


BLOCKS = dict(gancho=b_gancho, quem=b_quem, pacote=b_pacote, motivo=b_motivo, maio=b_maio, memo=b_memo, final=b_final)
