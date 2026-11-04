"""Visual do Short 017 (Tecnativo) — o Reddit vai virar um site só para quem tem login. 1080x1920.
render.py <proj> --vertical. Mesmo esqueleto vertical dos Shorts 015/016 (fundo, legenda, moldura, glitch).

Sem logos nem prints: busca, página de login e gráficos são recriações (selo "ilustração"); o nome "reddit" aparece só
como texto. Números e citações: CNBC e 9to5Google, 29/10/2026 (original/fonte_reddit_login.md)."""
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

ARQUIVO_FINAL = "tecnologia_017_short_reddit_login.mp4"
MARCA = ""
SOM = dict(intro=False, ganho_trilha=0.40, lufs=-14, bpm=124, sfx={
    "01.a": ["typing", "pop@+1.6"], "01.b": ["lock", "impact@+0.3"],
    "02.a": "notif", "02.b": ["lock", "alert@+0.4"],
    "03.a": "glitch", "03.b": ["typing", "shimmer@+0.6"], "03.c": "deny",
    "04.a": ["data", "deny@+1.0"], "04.b": ["alert", "impact@+0.4"],
    "05.a": ["data", "data@+0.4", "data@+0.8"], "05.b": "lock",
    "06.a": "notif", "06.b": "pop",
    "07.a": "lock", "07.b": "glitch"})

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
    # brilho laranja no gancho (o muro de login)
    red = 0.0
    if red > 0:
        c.drawCircle(CX, 640, 620, blur_paint(RED, 0.13 * red, 160))


CAP_Y = 1395


NUMEROS = [("um milhão", "1 milhão"), ("quinze por cento", "15%"),
           ("one million", "1 million"), ("fifteen percent", "15%")]


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
        GLITCH[:] = [C["01.b"], C["03.a"], C["07.b"]]


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


ORANGE = "#FF4500"   # laranja do Reddit (só cor, sem logo)


def selo(c, a, y=1250, s="ilustração"):
    note(c, s, y, a)


def busca(c, x, y, w, a, t, t0, query="melhor fone bom e barato", hl=1.0):
    """página de busca genérica: barra digitando + resultados (o 1º é do reddit)"""
    if a <= 0:
        return
    rrect(c, x, y, w, 110, 55, "#F1F3F7", a)
    n = int(clamp((t - t0) / 1.2) * len(query))
    text_mid(c, query[:n] + ("|" if int(t * 3) % 2 else ""), x + 50, y + 55, 40, "medium", "#1A1F2B", a, align="left")
    res = [("reddit.com › r/fones", "Qual o melhor fone bom e barato? : r/fones", ORANGE),
           ("loja-exemplo.com", "Fones em oferta | Compre já", INK2), ("blog-exemplo.com", "10 fones para comprar em 2026", INK2)]
    for i, (url, tit, col) in enumerate(res):
        u = ep(t, t0 + 1.0 + i * 0.2, 0.3) * a
        yy = y + 180 + i * 170
        if i == 0:
            rrect(c, x - 10, yy - 20, w + 20, 150, 18, ORANGE, 0.14 * u * hl)
            c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x - 10, yy - 20, w + 20, 150), 18, 18), paint(ORANGE, u * hl, stroke=3))
        text(c, url, x + 10, yy + 30, 28, "mono", col, u, align="left")
        text(c, tit, x + 10, yy + 90, 38, "bold", INK if i == 0 else INK2, u, align="left")


def cadeado(c, cx, cy, s, col, a):
    if a <= 0:
        return
    c.drawArc(skia.Rect.MakeXYWH(cx - s * 0.32, cy - s * 0.75, s * 0.64, s * 0.7), 180, 180, False, paint(col, a, stroke=s * 0.11))
    c.drawLine(cx - s * 0.32, cy - s * 0.4, cx - s * 0.32, cy - s * 0.15, paint(col, a, stroke=s * 0.11))
    c.drawLine(cx + s * 0.32, cy - s * 0.4, cx + s * 0.32, cy - s * 0.15, paint(col, a, stroke=s * 0.11))
    rrect(c, cx - s * 0.48, cy - s * 0.18, s * 0.96, s * 0.7, s * 0.1, col, a)
    c.drawCircle(cx, cy + s * 0.14, s * 0.08, paint("#0B0F1A", a))


def muro(c, a, t, y=560):
    """janela de login por cima de tudo"""
    if a <= 0:
        return
    c.drawRect(skia.Rect.MakeWH(W, H), paint("#000000", 0.6 * a))
    k = 0.85 + 0.15 * ease_back(clamp(a))
    c.save(); c.translate(CX, y + 300); c.scale(k, k); c.translate(-CX, -(y + 300))
    rrect(c, 110, y, 860, 600, 30, "#10151F", a)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(110, y, 860, 600), 30, 30), paint(ORANGE, a, stroke=4))
    cadeado(c, CX, y + 170, 130, ORANGE, a)
    text(c, "Entre para continuar", CX, y + 300, 52, "black", INK, a)
    text(c, "reddit", CX, y + 360, 34, "monob", ORANGE, a)
    rrect(c, 180, y + 420, 340, 100, 50, ORANGE, a)
    text_mid(c, "Entrar", 350, y + 470, 40, "black", "#FFFFFF", a)
    rrect(c, 560, y + 420, 340, 100, 50, "#232B3A", a)
    text_mid(c, "Criar conta", 730, y + 470, 40, "black", INK, a)
    c.restore()


def citacao(c, s1, s2, quem, y, a, col=ORANGE, size=46):
    if a <= 0:
        return
    panel(c, 70, y, 940, 330, a, col, label="citação")
    text(c, "“", 120, y + 130, 140, "black", col, a, align="left")
    text(c, s1, 200, y + 130, size, "extrabold", INK, a, align="left")
    text(c, s2, 200, y + 195, size, "extrabold", INK, a, align="left")
    text(c, quem, 200, y + 275, 28, "mono", INK2, a, align="left")


def robo(c, cx, cy, s, col, a):
    if a <= 0:
        return
    rrect(c, cx - s * 0.5, cy - s * 0.4, s, s * 0.8, s * 0.18, col, a)
    c.drawCircle(cx - s * 0.2, cy - s * 0.05, s * 0.1, paint("#0B0F1A", a))
    c.drawCircle(cx + s * 0.2, cy - s * 0.05, s * 0.1, paint("#0B0F1A", a))
    c.drawLine(cx, cy - s * 0.4, cx, cy - s * 0.62, paint(col, a, stroke=s * 0.06))
    c.drawCircle(cx, cy - s * 0.66, s * 0.07, paint(col, a))
    c.drawRect(skia.Rect.MakeXYWH(cx - s * 0.22, cy + s * 0.18, s * 0.44, s * 0.06), paint("#0B0F1A", a))


def b_gancho(c, t, C, B):
    _glitch(C)
    ta, tb = C["01.a"], C["01.b"]
    a = ep(t, ta, 0.25) * (1 - prog(t, B["end"] - 0.3, 0.3))
    title(c, "ACHOU NO REDDIT?", 380, a * (1 - prog(t, tb, 0.2)), INK, 92, hl="REDDIT?", hl_col=ORANGE)
    busca(c, 80, 500, 920, a, t, ta + 0.1)
    selo(c, a)
    sx, sy = shake(t, tb + 0.3, 16)
    c.save(); c.translate(sx, sy)
    muro(c, a * ep(t, tb, 0.25), t)
    c.restore()
    title(c, "LOGIN OBRIGATÓRIO", 390, a * ep(t, tb + 0.2, 0.2), INK, 90, hl="OBRIGATÓRIO", hl_col=ORANGE)


def b_anuncio(c, t, C, B):
    _glitch(C)
    a = fade(t, B["start"], B["end"])
    ta, tb = C["02.a"], C["02.b"]
    title(c, "ANÚNCIO OFICIAL", 370, a, INK, 90, hl="OFICIAL", hl_col=ORANGE)
    u = a * ep(t, ta + 0.2, 0.3)
    panel(c, 70, 480, 940, 300, u, ORANGE, label="29/10/2026 · resultado do 3º trimestre")
    text(c, "STEVE HUFFMAN", 120, 600, 64, "black", INK, u, align="left")
    text(c, "cofundador e CEO do Reddit", 120, 670, 38, "medium", INK2, u, align="left")
    ub = a * ep(t, tb, 0.3)
    if ub > 0:
        money(c, "SÓ COM CONTA", 960, ORANGE, ub, 130, 0.35)
        chip(c, "\"logged-in-only experience\"", CX, 1080, INK2, ub * ep(t, tb + 0.5, 0.3), anchor="center", size=30)
        cadeado(c, CX, 1220, 90, ORANGE, ub)


def b_culpado(c, t, C, B):
    _glitch(C)
    a = fade(t, B["start"], B["end"])
    ta, tb, tc = C["03.a"], C["03.b"], C["03.c"]
    title(c, "O CULPADO: GOOGLE", 370, a, INK, 88, hl="GOOGLE", hl_col=CYAN)
    ub = a * ep(t, tb, 0.3)
    if ub > 0:
        panel(c, 70, 480, 940, 420, ub, VIOLET, label="resumo de IA na busca")
        for i in range(5):
            w = 840 - (i % 3) * 140
            u = ep(t, tb + 0.2 + i * 0.12, 0.3)
            shim = 0.55 + 0.45 * math.sin(t * 4 + i)
            c.drawRect(skia.Rect.MakeXYWH(120, 560 + i * 62, w * u, 26), paint(VIOLET, (0.6 + 0.3 * shim) * ub))
        text(c, "a resposta já aparece aqui", 120, 880, 30, "mono", INK2, ub, align="left")
    uc = a * ep(t, tc, 0.3)
    rrect(c, 120, 990, 840, 130, 18, PANEL, uc)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(120, 990, 840, 130), 18, 18), paint(ORANGE, uc, stroke=3))
    text_mid(c, "reddit.com › r/fones", 160, 1055, 38, "monob", ORANGE, uc, align="left")
    if uc > 0:
        u = ep(t, tc + 0.4, 0.25)
        c.drawLine(140, 1010, 140 + 800 * u, 1100, paint(RED, uc, stroke=10, cap_round=True))
        stamp(c, "NINGUÉM CLICA", 760, 1170, RED, uc * u, 44, rot=-5)
    selo(c, a)


def b_numeros(c, t, C, B):
    _glitch(C)
    a = fade(t, B["start"], B["end"])
    ta, tb = C["04.a"], C["04.b"]
    title(c, "O ESTRAGO", 370, a, INK, 100, hl="ESTRAGO", hl_col=RED)
    u = a * ep(t, ta + 0.3, 0.3)
    money(c, "-1 MILHÃO", 580, RED, u, 150)
    text(c, "de visitas por semana vindas da busca (média)", CX, 650, 30, "mono", INK2, u)
    ub = a * ep(t, tb, 0.3)
    if ub > 0:
        # gráfico caindo
        pts = [(0, 0.85), (0.15, 0.9), (0.3, 0.8), (0.45, 0.86), (0.6, 0.78), (0.7, 0.8), (0.78, 0.3), (1.0, 0.22)]
        x, y, w, h = 120, 760, 840, 360
        pth = skia.Path()
        n = max(2, min(len(pts), int(len(pts) * prog(t, tb + 0.1, 1.0)) + 1))
        for i, (px, py) in enumerate(pts[:n]):
            X, Y = x + px * w, y + h - py * h
            pth.moveTo(X, Y) if i == 0 else pth.lineTo(X, Y)
        c.drawPath(pth, blur_paint(RED, 0.5 * ub, 14, stroke=10))
        c.drawPath(pth, paint(RED, ub, stroke=8, cap_round=True))
        stamp(c, "AÇÕES: -15%", 720, 1180, RED, ub * ep(t, tb + 0.9, 0.2), 54, rot=-5)
    note(c, "fonte: CNBC e 9to5Google, 29/10/2026", 1290, a)


def b_robos(c, t, C, B):
    _glitch(C)
    a = fade(t, B["start"], B["end"])
    ta, tb = C["05.a"], C["05.b"]
    title(c, "O OUTRO ALVO", 370, a, INK, 96, hl="ALVO", hl_col=VIOLET)
    aa = a * (1 - prog(t, tb, 0.25))
    if aa > 0:
        rrect(c, 90, 520, 360, 460, 24, PANEL, aa)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(90, 520, 360, 460), 24, 24), paint(ORANGE, aa, stroke=3))
        text(c, "reddit", 270, 590, 44, "monob", ORANGE, aa)
        for i in range(5):
            c.drawRect(skia.Rect.MakeXYWH(130, 640 + i * 62, 280 - (i % 2) * 80, 22), paint(INK2, 0.5 * aa))
        for i in range(3):
            u = ep(t, ta + 0.3 + i * 0.35, 0.3) * aa
            ry = 600 + i * 170
            robo(c, 860, ry + 40, 120, VIOLET, u)
            # páginas voando para o robô
            f = ((t - ta) * 0.8 + i * 0.33) % 1
            px = 460 + (740 - 460) * f
            rrect(c, px, ry + 10 - 30 * math.sin(f * math.pi), 60, 76, 6, INK, u * (1 - f) * 0.9)
        text(c, "robôs copiando conteúdo para treinar IA", CX, 1090, 30, "mono", INK2, aa)
        selo(c, aa, 1150)
    ab = a * ep(t, tb, 0.3)
    if ab > 0:
        text(c, "ACESSO NÃO AUTORIZADO", CX, 560, 46, "black", INK2, ab)
        money(c, "QUASE TODO", 720, VIOLET, ab, 130, 0.35)
        text(c, "vem de quem não está logado", CX, 820, 50, "extrabold", INK, ab)
        cadeado(c, CX, 1030, 150, ORANGE, ab * ep(t, tb + 0.8, 0.3))
        note(c, "segundo Steve Huffman, CEO do Reddit", 1230, ab)


def b_quando(c, t, C, B):
    _glitch(C)
    a = fade(t, B["start"], B["end"])
    ta, tb = C["06.a"], C["06.b"]
    title(c, "QUANDO?", 370, a, INK, 100, hl="QUANDO?", hl_col=GOLD)
    u = a * ep(t, ta + 0.2, 0.3)
    chip(c, "TESTES: 4º TRIMESTRE 2026", CX, 520, GOLD, u, anchor="center", size=40, filled=True)
    chip(c, "PAÍSES FORA DOS EUA", CX, 610, CYAN, a * ep(t, ta + 1.4, 0.3), anchor="center", size=40, filled=True)
    text(c, "data final ainda não divulgada", CX, 700, 30, "mono", INK2, u)
    citacao(c, "It's a sign of", "the times.", "Steve Huffman · CNBC, 29/10/2026", 820, a * ep(t, tb + 0.6, 0.3))
    text(c, "\"é um sinal dos tempos\"", CX, 1240, 40, "extrabold", ORANGE, a * ep(t, tb + 1.4, 0.3))


def b_final(c, t, C, B):
    _glitch(C)
    a = ep(t, B["start"], 0.3)
    ta, tb = C["07.a"], C["07.b"]
    muro(c, a, t, 600)
    aa = a * (1 - prog(t, tb, 0.25))
    title(c, "VOCÊ CRIARIA UMA CONTA", 360, aa, INK, 80)
    title(c, "SÓ PARA LER?", 460, aa, INK, 90, hl="LER?", hl_col=ORANGE)
    ab = ep(t, tb, 0.2)
    title(c, "A INTERNET ABERTA", 360, ab, INK, 86)
    title(c, "ACABOU?", 470, ab, INK, 110, hl="ACABOU?", hl_col=RED)


BLOCKS = dict(gancho=b_gancho, anuncio=b_anuncio, culpado=b_culpado, numeros=b_numeros, robos=b_robos, quando=b_quando,
              final=b_final)
