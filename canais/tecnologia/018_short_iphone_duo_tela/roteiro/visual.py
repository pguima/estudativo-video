"""Visual do Short 018 (Tecnativo) — a tela do iPhone dobrável (iPhone Duo) está rachando. 1080x1920.
render.py <proj> --vertical. Mesmo esqueleto vertical dos Shorts 015–017 (fundo, legenda, moldura, glitch).

Sem logos nem fotos: o celular, a dobradiça e as fotos são desenhos (selo "ilustração"). Fatos, preços e citações:
CNBC 26/10, iFixit 25/10 e Fortune 27/10/2026 (original/fonte_iphone_duo_tela.md)."""
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

ARQUIVO_FINAL = "tecnologia_018_short_iphone_duo_tela.mp4"
MARCA = ""
SOM = dict(intro=False, ganho_trilha=0.40, lufs=-14, bpm=124, sfx={
    "01.a": ["whoosh", "pop@+1.4"], "01.b": ["glitch", "impact@+0.2"],
    "02.a": "notif", "02.b": ["notif@+0.3", "notif@+0.8", "click@+2.6"], "02.c": ["impact@-0.7", "alert@+0.1"],
    "03.a": ["confirm", "data@+1.2"], "03.b": ["confirm", "confirm@+0.5", "alert@+1.0"],
    "04.a": ["glitch", "click@+1.2"], "04.b": "data", "04.c": ["alert", "deny@+2.2"],
    "05.a": ["data", "impact@+3.6"], "05.b": ["deny", "impact@+0.3"],
    "06.a": ["data", "deny@+3.2"], "06.b": ["shimmer", "impact@+2.0"],
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


NUMEROS = [("dois mil dólares", "US$ 2 mil"), ("novecentos e noventa e nove dólares", "US$ 999"),
           ("two thousand dollars", "$2,000"), ("nine hundred ninety-nine dollars", "$999")]


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


SAND = "#E8C27A"


def selo(c, a, y=1250, s="ilustração"):
    note(c, s, y, a)


def celular(c, cx, cy, h, ab, a, crack=0.0, linha=0.0, t=0.0):
    """iPhone dobrável visto de frente (desenho, sem logo). ab = abertura 0 (fechado) → 1 (aberto).
    crack/linha: trinca na dobra e linha branca de pixels saindo da dobradiça."""
    if a <= 0:
        return
    hw = h * 0.36                    # largura de cada metade
    wr = hw * ab                     # metade direita "abre" (escala horizontal)
    x0 = cx - (hw + wr) / 2
    hinge = x0 + hw
    r = h * 0.07
    rrect(c, x0 - 14, cy - h / 2 - 14, hw + wr + 28, h + 28, r + 10, "#1B2130", a, shadow=True)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x0 - 14, cy - h / 2 - 14, hw + wr + 28, h + 28), r + 10, r + 10),
                paint("#5A6478", a, stroke=3))
    # tela (gradiente azul/violeta, como papel de parede genérico)
    p = skia.Paint(AntiAlias=True)
    p.setShader(skia.GradientShader.MakeLinear([(x0, cy - h / 2), (x0 + hw + wr, cy + h / 2)],
                                               [hexc("#1E3A8A"), hexc("#6D28D9"), hexc("#0EA5E9")]))
    p.setAlphaf(a)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x0, cy - h / 2, hw + wr, h), r, r), p)
    for i in range(4):  # ícones genéricos
        for j in range(2 if ab < 0.5 else 4):
            ix = x0 + 40 + j * (hw + wr - 80) / max(1, (1 if ab < 0.5 else 3)) - 26
            iy = cy - h / 2 + 70 + i * 120
            if ix + 52 < x0 + hw + wr:
                rrect(c, ix, iy, 52, 52, 14, "#FFFFFF", 0.22 * a)
    if ab > 0.05:  # vinco
        c.drawLine(hinge, cy - h / 2, hinge, cy + h / 2, paint("#FFFFFF", 0.10 * a * ab, stroke=3))
    if crack > 0:
        yc = cy - h * 0.12
        rnd = np.random.default_rng(7)
        pth = skia.Path(); pth.moveTo(hinge, yc)
        yy = yc
        for k in range(7):
            yy += h * 0.035 * crack
            pth.lineTo(hinge + rnd.uniform(-9, 9), yy)
        c.drawPath(pth, paint("#FFFFFF", a * crack, stroke=3))
        c.drawCircle(hinge, yc, 26 * crack, blur_paint(RED, 0.6 * a * crack, 14))
    if linha > 0:
        yl = cy - h * 0.12
        L = (x0 + hw + wr - hinge) * linha
        c.drawRect(skia.Rect.MakeXYWH(hinge, yl - 3, L, 6), blur_paint("#FFFFFF", 0.8 * a, 10))
        c.drawRect(skia.Rect.MakeXYWH(hinge, yl - 2, L, 4), paint("#FFFFFF", a))
        c.drawRect(skia.Rect.MakeXYWH(hinge - 2, yl, 4, (cy + h / 2 - yl) * linha), paint("#FFFFFF", 0.85 * a))


def dobra(t, t0, per=2.4):
    """abre e fecha em loop a partir de t0 (1 = aberto)"""
    if t < t0:
        return 1.0
    u = ((t - t0) / per) % 1
    return 0.15 + 0.85 * (0.5 + 0.5 * math.cos(u * 2 * math.pi))


def b_gancho(c, t, C, B):
    _glitch(C)
    ta, tb = C["01.a"], C["01.b"]
    a = ep(t, ta, 0.25) * (1 - prog(t, B["end"] - 0.3, 0.3))
    title(c, "IPHONE DOBRÁVEL", 380, a * (1 - prog(t, tb, 0.2)), INK, 92, hl="DOBRÁVEL", hl_col=CYAN)
    title(c, "TELA RACHANDO", 380, a * ep(t, tb + 0.15, 0.2), INK, 96, hl="RACHANDO", hl_col=RED)
    sx, sy = shake(t, tb + 0.2, 18)
    c.save(); c.translate(sx, sy)
    ab = ease_out(prog(t, ta + 0.2, 1.0))
    celular(c, CX, 820, 640, 0.0 + ab, a, crack=ep(t, tb + 0.1, 0.3), linha=ep(t, tb + 0.3, 0.5))
    c.restore()
    chip(c, "US$ 1.999", CX, 1220, GOLD, a * ep(t, ta + 1.3, 0.3) * (1 - prog(t, tb, 0.2)), anchor="center", size=46, filled=True)
    stamp(c, "EM POUCAS HORAS", CX, 1225, RED, a * ep(t, tb + 0.9, 0.2), 48, rot=-5)
    selo(c, a, 1300)


def b_relatos(c, t, C, B):
    _glitch(C)
    a = fade(t, B["start"], B["end"])
    ta, tb, tc = C["02.a"], C["02.b"], C["02.c"]
    title(c, "IPHONE DUO", 370, a, INK, 96, hl="DUO", hl_col=CYAN)
    chip(c, "à venda desde 23/10/2026", CX, 470, GOLD, a * ep(t, ta + 0.3, 0.3), anchor="center", size=32, filled=True)
    estalo = tc - 0.75
    ab = dobra(t, tb + 0.6) if t < estalo else 1.0
    sx, sy = shake(t, estalo, 14)
    c.save(); c.translate(sx, sy)
    celular(c, CX, 880, 560, ab, a * ep(t, ta + 0.2, 0.3), crack=ep(t, estalo, 0.2), linha=ep(t, tc, 0.5))
    c.restore()
    stamp(c, "CREC!", 840, 640, RED, a * ep(t, estalo, 0.15) * (1 - prog(t, estalo + 1.2, 0.3)), 60, rot=8)
    chip(c, "relatos no Reddit e em fóruns", CX, 1235, INK2, a * ep(t, tb, 0.3), anchor="center", size=30)
    selo(c, a, 1300)


def b_apple(c, t, C, B):
    _glitch(C)
    a = fade(t, B["start"], B["end"])
    ta, tb = C["03.a"], C["03.b"]
    title(c, "A APPLE CONFIRMOU", 370, a, INK, 86, hl="CONFIRMOU", hl_col=CYAN)
    aa = a * ep(t, ta + 0.2, 0.3) * (1 - prog(t, tb, 0.25))
    if aa > 0:
        panel(c, 70, 480, 940, 420, aa, CYAN, label="declaração da Apple à CNBC · 26/10/2026")
        for i, s in enumerate(["\"We are aware of an issue", "impacting the inner display", "on a small number", "of iPhone Duo units.\""]):
            text(c, s, 120, 590 + i * 80, 50, "extrabold", CYAN if i == 2 else INK, aa * ep(t, ta + 0.3 + i * 0.15, 0.3), align="left")
        money(c, "\"POUCOS APARELHOS\"", 1050, CYAN, aa * ep(t, ta + 1.4, 0.3), 76, 0.3)
    ab = a * ep(t, tb, 0.3)
    if ab > 0:
        check_row(c, 60, 560, "ok", "troca pela garantia", ep(t, tb + 0.1, 0.3) * ab, GREEN)
        check_row(c, 60, 720, "ok", "não precisa de AppleCare+", ep(t, tb + 0.5, 0.3) * ab, GREEN)
        check_row(c, 60, 880, "warn", "nenhum recall anunciado", ep(t, tb + 1.0, 0.3) * ab, GOLD)
        note(c, "fonte: CNBC, 9to5Mac e Fortune", 1060, ab)


def b_causa(c, t, C, B):
    _glitch(C)
    a = fade(t, B["start"], B["end"])
    ta, tb, tc = C["04.a"], C["04.b"], C["04.c"]
    title(c, "A CAUSA?", 370, a, INK, 100, hl="CAUSA?", hl_col=GOLD)
    chip(c, "desmontagem do iFixit", CX, 470, GOLD, a * ep(t, ta + 1.0, 0.3), anchor="center", size=32, filled=True)
    # antes do corte: o aparelho aberto com a dobradiça marcada
    ua = a * ep(t, ta + 0.6, 0.3) * (1 - prog(t, tb - 0.1, 0.25))
    if ua > 0:
        celular(c, CX, 860, 560, 1.0, ua)
        c.drawLine(CX, 560, CX, 1160, blur_paint(GOLD, 0.8 * ua, 12, stroke=10))
        c.drawLine(CX, 560, CX, 1160, paint(GOLD, ua, stroke=4))
        chip(c, "dobradiça", CX + 30, 1200, GOLD, ua, anchor="left", size=30, filled=True)
    # corte lateral da dobradiça (ilustração): duas placas, tela fazendo a "gota" e a barra central
    u = a * ep(t, tb, 0.3)
    if u > 0:
        y0 = 820
        fe = ep(t, tb + 0.2, 0.8)          # fecha um pouco
        ang = 0.35 * fe
        L = 380
        for sg in (-1, 1):
            x1 = CX + sg * 60
            x2 = x1 + sg * L * math.cos(ang)
            y2 = y0 - L * math.sin(ang)
            c.drawLine(x1, y0 + 40, x2, y2 + 40, paint("#5A6478", u, stroke=26, cap_round=True))
            c.drawLine(x1, y0, x2, y2, paint(CYAN, u, stroke=8, cap_round=True))
        pth = skia.Path(); pth.moveTo(CX - 60, y0)
        pth.cubicTo(CX - 60, y0 + 90, CX + 60, y0 + 90, CX + 60, y0)
        c.drawPath(pth, paint(CYAN, u, stroke=8))
        text(c, "tela", CX - 300, y0 - 170 * fe - 40, 32, "mono", CYAN, u)
        # barra de apoio central: devia descer, mas fica alta
        bar_y = y0 + 120 - 50 * ep(t, tc, 0.4)
        uc = ep(t, tc, 0.3)
        rrect(c, CX - 45, bar_y, 90, 60, 10, RED if uc > 0.5 else INK2, u)
        text(c, "barra de apoio", CX, y0 + 240, 32, "mono", INK2, u)
        if uc > 0:
            pul = 0.6 + 0.4 * math.sin(t * 9)
            c.drawCircle(CX, y0 + 70, 70, blur_paint(RED, 0.7 * uc * pul * u, 26))
            stamp(c, "HIPÓTESE", 790, 1215, GOLD, u * ep(t, tc + 3.0, 0.2), 50, rot=-6)
        text(c, "dobradiça", CX, y0 + 300, 38, "black", INK, u * ep(t, tb + 0.4, 0.3))
    selo(c, a, 1300, "ilustração · hipótese do iFixit, não confirmada")


def b_conta(c, t, C, B):
    _glitch(C)
    a = fade(t, B["start"], B["end"])
    ta, tb = C["05.a"], C["05.b"]
    title(c, "A CONTA", 370, a, INK, 100, hl="CONTA", hl_col=RED)
    chip(c, "fora da garantia", CX, 470, INK2, a * ep(t, ta + 1.0, 0.3), anchor="center", size=32)
    u = a * ep(t, ta + 3.4, 0.3)
    money(c, "US$ 999", 650, RED, u, 190)
    text(c, "troca da tela interna (preço da Apple)", CX, 720, 30, "mono", INK2, u)
    ub = a * ep(t, tb - 0.4, 0.3)
    if ub > 0:
        x, w = 120, 840
        text(c, "iPhone Duo · US$ 1.999", x, 850, 36, "extrabold", INK, ub, align="left")
        rrect(c, x, 875, w * ep(t, tb - 0.3, 0.6), 60, 14, CYAN, ub)
        text(c, "tela interna · US$ 999", x, 1010, 36, "extrabold", INK, ub, align="left")
        rrect(c, x, 1035, w * 0.5 * ep(t, tb, 0.6), 60, 14, RED, ub)
        stamp(c, "METADE", 760, 1070, RED, ub * ep(t, tb + 0.5, 0.2), 54, rot=-6)
        note(c, "Galaxy Z Fold 8 e Pixel 11 Pro Fold: US$ 419 a 579 (comparação iFixit)", 1200, ub, size=22)


def b_areia(c, t, C, B):
    _glitch(C)
    a = fade(t, B["start"], B["end"])
    ta, tb = C["06.a"], C["06.b"]
    aa = a * (1 - prog(t, tb, 0.25))
    if aa > 0:
        title(c, "QUANTOS?", 370, aa, INK, 100, hl="QUANTOS?", hl_col=GOLD)
        money(c, "?", 640, GOLD, aa * ep(t, ta + 0.3, 0.3), 260)
        text(c, "a Apple não divulgou", CX, 760, 36, "mono", INK2, aa * ep(t, ta + 0.8, 0.3))
        stamp(c, "FOTO FALSA", CX, 960, RED, aa * ep(t, ta + 3.0, 0.2), 64, rot=-6)
        text(c, "algumas imagens parecem feitas por IA (MacRumors)", CX, 1110, 28, "mono", INK2, aa * ep(t, ta + 3.3, 0.3))
    ab = a * ep(t, tb, 0.3)
    if ab > 0:
        title(c, "UM GRÃO DE AREIA", 370, ab, INK, 86, hl="AREIA", hl_col=SAND)
        # grão caindo na dobradiça
        f = ep(t, tb + 0.2, 1.4)
        gx, gy = CX + 140 * (1 - f), 480 + 160 * f
        c.drawCircle(gx, gy, 16, blur_paint(SAND, 0.6 * ab, 10))
        c.drawCircle(gx, gy, 11, paint(SAND, ab))
        c.drawLine(CX - 260, 660, CX + 260, 660, paint("#5A6478", ab, stroke=20, cap_round=True))
        citacao(c, "...a grain of sand can kill", "the fragile display panel.", "Kyle Wiens, CEO do iFixit · CNBC, 26/10/2026",
                760, ab * ep(t, tb + 1.4, 0.3), col=SAND, size=44)
        text(c, "\"um grão de areia pode matar a tela\"", CX, 1180, 38, "extrabold", SAND, ab * ep(t, tb + 2.2, 0.3))


def b_final(c, t, C, B):
    _glitch(C)
    a = ep(t, B["start"], 0.3)
    ta, tb = C["07.a"], C["07.b"]
    celular(c, CX, 960, 600, dobra(t, B["start"] + 0.2, 2.0), a)
    aa = a * (1 - prog(t, tb, 0.25))
    title(c, "VOCÊ PAGARIA", 360, aa, INK, 86)
    title(c, "QUASE US$ 2 MIL?", 470, aa, INK, 90, hl="US$ 2 MIL?", hl_col=GOLD)
    ab = ep(t, tb, 0.2)
    title(c, "OU ESPERA A", 360, ab, INK, 86)
    title(c, "2ª GERAÇÃO?", 470, ab, INK, 110, hl="GERAÇÃO?", hl_col=CYAN)


BLOCKS = dict(gancho=b_gancho, relatos=b_relatos, apple=b_apple, causa=b_causa, conta=b_conta, areia=b_areia, final=b_final)
