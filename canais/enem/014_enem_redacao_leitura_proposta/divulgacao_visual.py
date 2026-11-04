"""Visual da divulgação da série Leitura da Proposta (Redação ENEM) — compartilhado pelo Short (1080x1920, render.py
--vertical) e pelo horizontal (1920x1080). Cada projeto tem um visual.py curto que chama setup(PROJ) e define SOM/ARQUIVO.
Mundo visual: a folha de redação do ENEM (linhas numeradas, margem vermelha) sobre azul-noite; carimbo vermelho de nota;
o "endereço" da frase temática em blocos (analogia da série); as capas reais dos 6 episódios.
Cores com função (as da série): azul = tema · verde = certo/método · amarelo = destaque · vermelho = erro/penalidade."""
import json
import math
from functools import lru_cache
from pathlib import Path
import skia
import motor
import tech
from motor import W, H, paint, text, text_mid, text_w, ep, prog, ease_out, ease_back, ease_io, clamp, lerp  # noqa
from tech import blur_paint, glow_text, hash01  # noqa

SERIE = Path(__file__).resolve().parent
VERT = H > W
CX = W / 2
NAVY, NAVY2 = "#0A1430", "#16285A"
PAPER, PAPER_LN = "#FBF8F1", "#CBD7EE"
WHITE, INK, INK2, MUT = "#FFFFFF", "#18213A", "#B9C6E4", "#6B7591"
YEL, RED, GREEN, SKY, BLUE = "#FFD23F", "#FF4D5A", "#2BD47D", "#7CC4FF", "#3B6CF6"
ENTRADA_SECA = True
MARCA = ""
SAMP = skia.SamplingOptions(skia.FilterMode.kLinear, skia.MipmapMode.kLinear)

# títulos curtos dos 6 episódios (núcleo do título do YouTube, sem o sufixo da série)
EPISODIOS = ["A redação começa antes da 1ª linha: o que a prova pede",
             "Como desmontar a frase temática da redação do ENEM",
             "Linha copiada vira linha fantasma: textos motivadores",
             "Tangenciar o tema custa até 480 pontos",
             "Sua tese esqueceu um bloco? Do tema à tese em 6 passos",
             "Você cai nessas 10 pegadinhas da redação do ENEM?"]
PALAVRAS = {}   # (cena, palavra normalizada) -> instante absoluto da 1ª ocorrência
FLASH = []


def setup(proj):
    t = json.loads((Path(proj) / "audio" / "tempos.json").read_text(encoding="utf-8"))
    for s in t["scenes"]:
        for tk in s["tokens"]:
            k = (s["id"], tk["disp"].lower().strip(".,:;!?*"))
            PALAVRAS.setdefault(k, s["start"] + tk["t0"])
    FLASH[:] = [s["start"] - 0.05 for s in t["scenes"][1:] if s["id"] in ("02", "04", "05", "12" if not VERT else "06")]


def w_at(cena, palavra, padrao):
    return PALAVRAS.get((cena, palavra), padrao)


@lru_cache(None)
def capa(i):
    return skia.Image.open(str(next((SERIE / sorted(p.name for p in SERIE.glob("ep*"))[i] / "youtube").glob("capa_A*.jpg"))))


def fade(t, t0, t1, d=0.3, d_out=0.25):
    return ep(t, t0, d) * (1 - prog(t, t1, d_out))


def shake(t, t0, amp=14, d=0.3):
    u = prog(t, t0, d)
    if u <= 0 or u >= 1:
        return 0.0, 0.0
    k = (1 - u) * amp
    return k * math.sin(t * 90), k * math.cos(t * 77)


def fit(s, peso, size, maxw):
    while text_w(s, peso, size) > maxw and size > 10:
        size -= 2
    return size


def big(c, s, cx, y, a, size, col=WHITE, maxw=None, peso="black", glow=0.10):
    if a <= 0:
        return
    size = fit(s, peso, size, maxw or W - 120)
    glow_text(c, s, cx, y + (1 - ease_out(clamp(a))) * 26, size, peso, col, clamp(a), glow=glow)


def pill(c, s, cx, cy, size, bg, fg, a, peso="black"):
    if a <= 0:
        return
    w = text_w(s, peso, size) + size * 1.2
    h = size * 1.8
    r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2, cy - h / 2, w, h), h / 2, h / 2)
    c.drawRRect(r, blur_paint(bg, 0.4 * a, 18))
    c.drawRRect(r, paint(bg, a))
    text_mid(c, s, cx, cy, size, peso, fg, a)


def marca_texto(c, s, cx, y, size, a, col=YEL, fg=NAVY, peso="black", k=1.0):
    """palavra com marca-texto passando (k = quanto do marca-texto já passou)"""
    if a <= 0:
        return
    size = fit(s, peso, size, W - 140)
    w = text_w(s, peso, size)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2 - 16, y - size * 0.86, (w + 32) * clamp(k), size * 1.16), 10, 10),
                paint(col, a))
    text(c, s, cx, y, size, peso, fg if k > 0.5 else WHITE, a)


def cover(c, i, x, y, w, h, a, r=18, borda=None):
    if a <= 0:
        return
    rr = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), r, r)
    c.drawRRect(rr, blur_paint("#000000", 0.45 * a, 24))
    c.save(); c.clipRRect(rr, True)
    p = skia.Paint(AntiAlias=True); p.setAlphaf(clamp(a))
    c.drawImageRect(capa(i), skia.Rect.MakeXYWH(x, y, w, h), SAMP, p)
    c.restore()
    if borda:
        c.drawRRect(rr, paint(borda, a, stroke=5))


# ---------------------------------------------------------------- a folha de redação
@lru_cache(None)
def _barras(n):
    return [0.55 + 0.4 * hash01(i, 3) for i in range(n)]


def folha(c, cx, cy, w, h, a, rot=0.0, escrito=0.0, n=14, titulo=True):
    """folha de redação: cabeçalho, margem vermelha, linhas numeradas; `escrito` (0–1) = linhas com texto"""
    if a <= 0:
        return None
    c.save(); c.translate(cx, cy); c.rotate(rot); c.translate(-w / 2, -h / 2)
    rr = skia.RRect.MakeRectXY(skia.Rect.MakeWH(w, h), 14, 14)
    c.drawRRect(rr.makeOffset(0, 18) if hasattr(rr, "makeOffset") else rr, blur_paint("#000000", 0.5 * a, 30))
    c.drawRRect(rr, paint(PAPER, a))
    top = 0.15 * h if titulo else 0.06 * h
    if titulo:
        text(c, "REDAÇÃO", 40, top * 0.62, h * 0.042, "black", INK, a, align="left")
        text(c, "ENEM", w - 40, top * 0.62, h * 0.03, "extrabold", BLUE, a, align="right")
    lh = (h - top - 0.05 * h) / n
    mx = 70
    c.drawLine(mx, top - 6, mx, h - 20, paint(RED, 0.55 * a, stroke=2.5))
    linhas = []
    for i in range(n):
        y = top + (i + 1) * lh
        c.drawLine(24, y, w - 24, y, paint(PAPER_LN, a, stroke=2))
        text(c, str(i + 1), mx - 14, y - lh * 0.22, lh * 0.36, "semibold", MUT, a * 0.8, align="right")
        k = clamp(escrito * n - i)
        if k > 0:
            bw = (w - mx - 60) * _barras(n)[i] * k
            c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(mx + 18, y - lh * 0.5, bw, lh * 0.26), 5, 5), paint("#3A4566", 0.55 * a))
        linhas.append(y)
    c.restore()
    return dict(top=top, lh=lh, linhas=linhas)


def carimbo(c, s, sub, cx, cy, size, col, a, t, t0, rot=-0.18):
    """carimbo que bate: escala 1.7 → 1 em 0.18 s, com aro e respingo"""
    if t < t0 or a <= 0:
        return
    u = clamp((t - t0) / 0.18)
    sc = lerp(1.7, 1.0, ease_out(u))
    aa = a * clamp(u * 2)
    c.save(); c.translate(cx, cy); c.rotate(math.degrees(rot)); c.scale(sc, sc)
    tw = max(text_w(s, "black", size), text_w(sub, "black", size * 0.3) if sub else 0)
    w, h = tw + size * 0.7, size * (1.25 if sub else 1.05)
    rr = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(-w / 2, -h / 2, w, h), size * 0.16, size * 0.16)
    c.drawRRect(rr, paint(col, aa * 0.12))
    c.drawRRect(rr, paint(col, aa, stroke=size * 0.07))
    text(c, s, 0, (size * 0.30 if not sub else size * 0.18), size, "black", col, aa)
    if sub:
        text(c, sub, 0, h / 2 - size * 0.12, size * 0.26, "black", col, aa)
    c.restore()


def check(c, cx, cy, r, a, ok=True):
    if a <= 0:
        return
    col = GREEN if ok else RED
    c.drawCircle(cx, cy, r, paint(col, a))
    p = paint(WHITE, a, stroke=r * 0.28, cap_round=True)
    k = ease_out(clamp(a))
    if ok:
        pth = skia.Path(); pth.moveTo(cx - r * 0.45, cy + r * 0.02); pth.lineTo(cx - r * 0.1, cy + r * 0.38); pth.lineTo(cx + r * 0.5, cy - r * 0.35)
        c.drawPath(pth, p)
    else:
        d = r * 0.38 * k
        c.drawLine(cx - d, cy - d, cx + d, cy + d, p); c.drawLine(cx + d, cy - d, cx - d, cy + d, p)


# ---------------------------------------------------------------- fundo, legenda e selo
@lru_cache(None)
def _bg():
    s = skia.Surface(W, H); c = s.getCanvas()
    p = skia.Paint(Shader=skia.GradientShader.MakeLinear([(0, 0), (W * 0.3, H)], [motor.hexc(NAVY), motor.hexc(NAVY2)]))
    c.drawRect(skia.Rect.MakeWH(W, H), p)
    for y in range(0, H, 64):   # pauta de caderno, bem apagada
        c.drawLine(0, y, W, y, paint("#FFFFFF", 0.035, stroke=2))
    c.drawCircle(W * 0.85, H * 0.15, max(W, H) * 0.35, blur_paint(BLUE, 0.16, 160))
    c.drawCircle(W * 0.1, H * 0.9, max(W, H) * 0.3, blur_paint("#7C5CFA", 0.10, 160))
    return s.makeImageSnapshot()


def BACKGROUND(c, t):
    c.drawImage(_bg(), 0, 0)
    for i in range(22):
        x = hash01(i, 1) * W + math.sin(t * 0.5 + i) * 10
        y = H - ((hash01(i, 3) * H + t * (12 + 26 * hash01(i, 5))) % (H + 40))
        c.drawCircle(x, y, 1.5 + 2.5 * hash01(i, 7), paint(YEL if i % 4 == 0 else WHITE, 0.08 + 0.16 * hash01(i, 9)))


CAP_Y = 1470 if VERT else 1000
CAP_SIZE = 84 if VERT else 58
CAP_MAXW = 960 if VERT else 1500


def _chunks(tokens):
    out, cur = [], []
    lim = 3 if VERT else 5
    for tk in tokens:
        cur.append(tk)
        end = tk["disp"].rstrip()[-1:] in ".,:?!;"
        if len(cur) >= lim or end or sum(len(x["disp"]) + 1 for x in cur) > (18 if VERT else 30):
            out.append(cur); cur = []
    if cur:
        out.append(cur)
    return out


def CAPTION(c, scene, t):
    """legenda de redes sociais: poucas palavras, grandes, com contorno; palavra falada em amarelo, destaque em azul"""
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
    size, sp = CAP_SIZE, CAP_SIZE * 0.27
    while sum(text_w(wd, "black", size) for wd in words) + sp * (len(words) - 1) > CAP_MAXW:
        size -= 3
    tot = sum(text_w(wd, "black", size) for wd in words) + sp * (len(words) - 1)
    pop = ease_back(clamp((lt - s) / 0.16))
    x = CX - tot / 2
    c.save(); c.translate(CX, CAP_Y); c.scale(0.86 + 0.14 * pop, 0.86 + 0.14 * pop); c.translate(-CX, -CAP_Y)
    f = motor.font("black", size)
    for tk, wd in zip(ch, words):
        falando = tk["t0"] - 0.05 <= lt < tk["t1"] + 0.25
        col = YEL if falando else (SKY if tk["bold"] else WHITE)
        st = skia.Paint(AntiAlias=True, Style=skia.Paint.kStroke_Style, StrokeWidth=size * 0.17, Color=skia.Color(4, 10, 28))
        st.setStrokeJoin(skia.Paint.kRound_Join)
        c.drawString(wd, x, CAP_Y + size * 0.36, f, st)
        c.drawString(wd, x, CAP_Y + size * 0.36, f, paint(col, 1.0))
        x += text_w(wd, "black", size) + sp
    c.restore()


def OVERLAY(c, t):
    if VERT:
        pill(c, "REDAÇÃO ENEM · LEITURA DA PROPOSTA", CX, 150, 26, YEL, NAVY, 0.95, "extrabold")
    else:
        pill(c, "REDAÇÃO ENEM · LEITURA DA PROPOSTA", 300, 62, 20, YEL, NAVY, 0.95, "extrabold")
    for t0 in FLASH:   # corte seco com clarão nas viradas
        u = (t - t0) / 0.16
        if 0 <= u < 1:
            c.drawRect(skia.Rect.MakeWH(W, H), paint(WHITE, 0.28 * (1 - u)))


# ---------------------------------------------------------------- blocos
def b_gancho(c, t, C, B):
    a = 1 - prog(t, B["end"] - 0.1, 0.2)
    t_zero = w_at("01", "zero", C["01.a"] + 0.6)
    t_perf = w_at("01", "perfeito", C["01.b"] + 0.6)
    fw, fh = (640, 860) if VERT else (520, 700)
    fx, fy = (CX - 40, 780) if VERT else (560, 520)
    folha(c, fx, fy, fw, fh, a, rot=-2.5, escrito=ep(t, 0, 1.6))
    dx, dy = shake(t, t_zero)
    # verificações verdes nas linhas: o texto está "perfeito"
    for i in range(5):
        k = ep(t, t_perf - 0.1 + i * 0.09, 0.22)
        check(c, fx + fw / 2 - 30, fy - fh / 2 + fh * 0.22 + i * fh * 0.13, 26 if VERT else 22, a * k)
    if VERT:
        carimbo(c, "0", "NOTA FINAL", CX + 120 + dx, 1080 + dy, 250, RED, a, t, t_zero)
        pill(c, "TEXTO PERFEITO", CX, 262, 40, GREEN, NAVY, a * ep(t, t_perf, 0.25))
    else:
        carimbo(c, "0", "NOTA FINAL", 1340 + dx, 480 + dy, 280, RED, a, t, t_zero, rot=-0.12)
        pill(c, "TEXTO PERFEITO", 1340, 800, 38, GREEN, NAVY, a * ep(t, t_perf, 0.25))


def b_placar(c, t, C, B):
    a = ep(t, B["start"], 0.2) * (1 - prog(t, B["end"] - 0.1, 0.2))
    ta, tb, tc = C["02.a"], C["02.b"], C["02.c"]
    t_480 = w_at("02", "quatrocentos", tc + 0.6)
    # 1) fuga = zero
    k1 = fade(t, ta, tb - 0.05)
    if k1 > 0:
        y0 = 620 if VERT else 420
        big(c, "FUGIU DO TEMA?", CX, y0, k1, 110 if VERT else 120, WHITE)
        dx, dy = shake(t, ta + 0.5)
        carimbo(c, "ZERO", "", CX + dx, y0 + (300 if VERT else 260) + dy, 200, RED, k1, t, ta + 0.5, rot=-0.08)
    # 2) tangenciar: o placar das cinco competências
    k2 = ep(t, tb, 0.3) * a
    if k2 <= 0:
        return
    queda = ease_io(clamp((t - t_480 + 0.3) / 0.9))
    if VERT:
        x0, y0, bw, bh, gap = 220, 360, 700, 92, 46
        big(c, "TANGENCIOU?", CX, 300, k2, 100, YEL)
    else:
        x0, y0, bw, bh, gap = 330, 200, 760, 74, 30
        big(c, "TANGENCIOU?", 710, 150, k2, 76, YEL)
    total = 0
    for i in range(5):
        y = y0 + i * (bh + gap)
        cai = i in (1, 2, 4)
        v = 200 - (160 * queda if cai else 0)
        total += v
        ki = ep(t, tb + 0.08 * i, 0.3) * a
        text_mid(c, f"C{i + 1}", x0 - 30, y + bh / 2, bh * 0.42, "black", WHITE, ki, align="right")
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x0, y, bw, bh), bh / 2, bh / 2), paint("#FFFFFF", 0.10 * ki))
        col = motor.mix(GREEN, RED, queda) if cai else GREEN
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x0, y, max(bh, bw * v / 200 * ep(t, tb + 0.08 * i, 0.5)), bh), bh / 2, bh / 2), paint(col, ki))
        text_mid(c, f"{int(round(v))}", x0 + bw + 24, y + bh / 2, bh * 0.42, "black", RED if cai and queda > 0.5 else WHITE, ki, align="left")
    tot = int(round(1000 - 480 * queda))
    if VERT:
        big(c, f"{tot}", CX, 1200, k2, 170, RED if queda > 0.5 else WHITE)
        big(c, "−480 PONTOS", CX, 1320, a * ep(t, t_480 + 0.4, 0.25), 80, RED)
    else:
        big(c, f"{tot}", 1560, 470, k2, 210, RED if queda > 0.5 else WHITE, maxw=560)
        big(c, "−480 PONTOS", 1560, 600, a * ep(t, t_480 + 0.4, 0.25), 64, RED, maxw=560)


def b_causa(c, t, C, B):
    a = ep(t, B["start"], 0.2) * (1 - prog(t, B["end"] - 0.1, 0.2))
    h = C["03.c"] < 1e8
    t_pior = C["03.a"] if h else None
    t_err, t_read = (C["03.b"], C["03.c"]) if h else (C["03.a"], C["03.b"])
    if h:
        k0 = fade(t, t_pior, t_err - 0.05)
        big(c, "QUASE NINGUÉM PERCEBE", CX, 520, k0, 110, WHITE)
    k = ep(t, t_err, 0.3) * a
    fw, fh = (680, 760) if VERT else (560, 640)
    fx, fy = (CX, 880) if VERT else (640, 540)
    g = folha(c, fx, fy, fw, fh, k, escrito=0.0, n=10)
    if g:
        # a seta aponta para o espaço ANTES da linha 1
        y1 = fy - fh / 2 + g["top"] + g["lh"] * 0.4
        ka = ep(t, t_err + 0.3, 0.3) * a
        if VERT:
            motor.arrow(c, CX + 330, y1 - 160, fx + fw / 2 - 60, y1 - 8, RED, ka, width=10, head=34, progress=ka)
            pill(c, "O ERRO ESTÁ AQUI", CX + 120, y1 - 205, 38, RED, WHITE, ka)
        else:
            motor.arrow(c, 1180, y1 - 40, fx + fw / 2 - 40, y1 - 4, RED, ka, width=9, head=30, progress=ka)
            pill(c, "O ERRO ESTÁ AQUI", 1400, y1 - 40, 34, RED, WHITE, ka)
            text(c, "antes da 1ª linha", 1400, y1 + 40, 40, "extrabold", WHITE, ka)
    kr = ep(t, t_read, 0.3) * a
    if VERT:
        marca_texto(c, "LEITURA DA PROPOSTA", CX, 1330, 80, kr, k=ep(t, t_read + 0.15, 0.5))
    else:
        marca_texto(c, "LEITURA DA PROPOSTA", 1360, 720, 64, kr, k=ep(t, t_read + 0.15, 0.5))


BLOCOS_TEMA = ["Caminhos para combater", "a intolerância religiosa", "no Brasil"]


def b_teste(c, t, C, B):
    a = ep(t, B["start"], 0.2) * (1 - prog(t, B["end"] - 0.1, 0.2))
    ta, tb, tc, td, te = C["04.a"], C["04.b"], C["04.c"], C["04.d"], C["04.e"]
    if VERT:
        pill(c, "TEMA · ENEM 2016", CX, 300, 40, BLUE, WHITE, a * ep(t, ta, 0.25))
        caixas = [(CX, 470 + i * 210, 880, 160) for i in range(3)]
        size = 60
    else:
        pill(c, "TEMA · ENEM 2016", CX, 180, 34, BLUE, WHITE, a * ep(t, ta, 0.25))
        size, gap = 52, 40
        while sum(text_w(s, "black", size) + 80 for s in BLOCOS_TEMA) + 2 * gap > W - 200:
            size -= 2
        ws = [text_w(s, "black", size) + 80 for s in BLOCOS_TEMA]
        caixas, x = [], CX - (sum(ws) + 2 * gap) / 2
        for w_ in ws:
            caixas.append((x + w_ / 2, 360, w_, 140)); x += w_ + gap
    falta = ep(t, td, 0.3)
    for i, (cx, cy, w, h) in enumerate(caixas):
        ki = ep(t, tb + 0.35 * i, 0.3) * a
        if ki <= 0:
            continue
        sx = shake(t, td, 10)[0] if i != 1 else 0
        ok = i == 1
        col = BLUE if t < tc else (GREEN if ok else motor.mix(BLUE, RED, falta))
        rr = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2 + sx, cy - h / 2 + (1 - ki) * 30, w, h), 24, 24)
        c.drawRRect(rr, paint("#FFFFFF", 0.95 * ki))
        dash = skia.Paint(AntiAlias=True, Style=skia.Paint.kStroke_Style, StrokeWidth=8, Color=motor.hexc(col, ki))
        if not ok and falta > 0:
            dash.setPathEffect(skia.DashPathEffect.Make([26, 16], 0))
        c.drawRRect(rr, dash)
        text_mid(c, BLOCOS_TEMA[i], cx + sx, cy + (1 - ki) * 30, fit(BLOCOS_TEMA[i], "black", size, w - 60), "black", INK, ki)
        if t >= tc and ok:
            check(c, cx + w / 2 - 10, cy - h / 2 + 10, 34, a * ep(t, tc + 0.3, 0.25))
        if not ok:
            check(c, cx + w / 2 - 10 + sx, cy - h / 2 + 10, 34, a * falta, ok=False)
            if te < 1e8:
                pill(c, "FALTOU!", cx + sx, cy + h / 2 + 40, 30, RED, WHITE, a * ep(t, te + (0.0 if i == 0 else 0.6), 0.25))
    # o texto do aluno: só o assunto amplo
    ks = ep(t, tc, 0.3) * a
    if VERT:
        pill(c, "SEU TEXTO: SÓ INTOLERÂNCIA RELIGIOSA", CX, 1160, 36, "#24376E", WHITE, ks, "extrabold")
        dx, dy = shake(t, td + 0.2)
        carimbo(c, "TANGENCIOU", "C2 · C3 · C5 NO MÁXIMO 40", CX + dx, 1300 + dy, 120, RED, a, t, td + 0.2, rot=-0.06)
    else:
        pill(c, "SEU TEXTO: SÓ INTOLERÂNCIA RELIGIOSA", CX, 580, 36, "#24376E", WHITE, ks, "extrabold")
        dx, dy = shake(t, td + 0.2)
        carimbo(c, "TANGENCIOU", "C2 · C3 · C5 NO MÁXIMO 40", CX + dx, 760 + dy, 120, RED, a, t, td + 0.2, rot=-0.05)


def b_serie(c, t, C, B):   # Short: as 6 capas de uma vez
    a = ep(t, B["start"], 0.2) * (1 - prog(t, B["end"] - 0.1, 0.2))
    ta = C["05.a"]
    big(c, "6 AULAS · DO ZERO", CX, 300, a, 96, YEL)
    cw, ch, gx, gy = 470, 264, 40, 70
    x0, y0 = CX - cw - gx / 2, 380
    for i in range(6):
        k = ep(t, ta + 0.15 + 0.17 * i, 0.3) * a
        x = x0 + (i % 2) * (cw + gx)
        y = y0 + (i // 2) * (ch + gy) + (1 - ease_back(clamp(k))) * 60
        cover(c, i, x, y, cw, ch, k)
        pill(c, f"EP {i + 1}", x + 60, y + ch + 2, 22, YEL, NAVY, k)


def b_intro(c, t, C, B):   # horizontal: nome da série + fileira de capas
    a = ep(t, B["start"], 0.2) * (1 - prog(t, B["end"] - 0.1, 0.2))
    big(c, "SÉRIE", CX, 250, a, 50, INK2)
    marca_texto(c, "LEITURA DA PROPOSTA", CX, 400, 120, a, k=ep(t, C["05.a"] + 0.3, 0.5))
    big(c, "6 aulas para quem está começando", CX, 510, a * ep(t, C["05.b"], 0.3), 54, WHITE)
    cw, ch, gx = 270, 152, 22
    x0 = CX - (6 * cw + 5 * gx) / 2
    for i in range(6):
        k = ep(t, C["05.b"] + 0.1 * i, 0.3) * a
        cover(c, i, x0 + i * (cw + gx), 620 + (1 - ease_back(clamp(k))) * 50, cw, ch, k, r=12)


def b_eps(c, t, C, B):   # horizontal: um episódio por cena (06–11), capa grande + título
    ids = ["06", "07", "08", "09", "10", "11"]
    k_atual = max((i for i, s in enumerate(ids) if C[s] - 0.15 <= t), default=0)
    a_bl = ep(t, B["start"], 0.2) * (1 - prog(t, B["end"] - 0.1, 0.2))
    t0 = C[ids[k_atual]] - 0.15
    u = ease_out(clamp((t - t0) / 0.35))
    x, y, w, h = 120, 190, 960, 540
    # capa anterior sai pela esquerda, a nova entra pela direita
    if k_atual > 0 and u < 1:
        cover(c, k_atual - 1, x - 400 * u, y, w, h, a_bl * (1 - u), r=22)
    cover(c, k_atual, x + 300 * (1 - u), y, w, h, a_bl * u, r=22, borda=YEL)
    tx = 1160
    pill(c, f"EPISÓDIO {k_atual + 1}", tx + 120, 260, 30, YEL, NAVY, a_bl * u)
    # título em até 3 linhas
    palavras, linhas, cur = EPISODIOS[k_atual].split(), [], ""
    for p in palavras:
        if text_w((cur + " " + p).strip(), "black", 52) > 660:
            linhas.append(cur); cur = p
        else:
            cur = (cur + " " + p).strip()
    linhas.append(cur)
    for j, ln in enumerate(linhas[:4]):
        text(c, ln, tx, 380 + j * 66, 52, "black", WHITE, a_bl * ep(t, t0 + 0.1 + 0.06 * j, 0.3), align="left")
    # progresso: 6 bolinhas
    for i in range(6):
        cx = tx + 30 + i * 70
        on = i <= k_atual
        c.drawCircle(cx, 700, 22 if i == k_atual else 16, paint(YEL if on else "#FFFFFF", a_bl * (1 if on else 0.25)))
        if on:
            text_mid(c, str(i + 1), cx, 700, 22 if i == k_atual else 16, "black", NAVY, a_bl)


def wordmark(c, cx, cy, size, a, col=WHITE):
    if a <= 0:
        return
    w = text_w("ESTUDATIVO", "black", size)
    text(c, "ESTUDATIVO", cx - w / 2, cy + size * 0.35, size, "black", col, a, align="left")
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2, cy + size * 0.55, w * ep(a, 0.2, 0.6), size * 0.12), 4, 4),
                paint(YEL, a))


def busca(c, cx, cy, w, h, a, t, t0, termo="Estudativo"):
    if a <= 0:
        return
    rr = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2, cy - h / 2, w, h), h / 2, h / 2)
    c.drawRRect(rr, blur_paint("#000000", 0.4 * a, 20))
    c.drawRRect(rr, paint(WHITE, a))
    # lupa
    lx, r = cx - w / 2 + h * 0.6, h * 0.2
    c.drawCircle(lx, cy - r * 0.2, r, paint(MUT, a, stroke=h * 0.07))
    c.drawLine(lx + r * 0.7, cy + r * 0.5, lx + r * 1.4, cy + r * 1.2, paint(MUT, a, stroke=h * 0.08, cap_round=True))
    n = int(clamp((t - t0) / 0.7) * len(termo))
    s = termo[:n]
    tw = text(c, s, lx + h * 0.55, cy + h * 0.15, h * 0.42, "bold", INK, a, align="left")
    if (t * 2) % 1 < 0.6:
        c.drawRect(skia.Rect.MakeXYWH(lx + h * 0.55 + tw + 6, cy - h * 0.24, 4, h * 0.48), paint(INK, a))


def card_playlist(c, x, y, w, a, capa_i, nome, sub, destaque=True):
    if a <= 0:
        return
    h = w * 0.36
    rr = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 28, 28)
    c.drawRRect(rr, paint("#0B1C44", a))
    c.drawRRect(rr, paint(YEL if destaque else "#FFFFFF", a * (0.9 if destaque else 0.35), stroke=4))
    tw, th = h * 0.86 * 16 / 9, h * 0.86
    tx, ty = x + h * 0.07, y + h * 0.07
    for k in (2, 1):   # pilha de capas (é uma playlist)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(tx + 10 * k, ty - 8 * k, tw, th), 12, 12), paint("#FFFFFF", a * 0.15 * (3 - k)))
    cover(c, capa_i, tx, ty, tw, th, a, r=12)
    tl = x + h * 0.07 + tw + 34
    maxw = x + w - tl - 30
    text(c, "PLAYLIST", tl, y + h * 0.33, h * 0.11, "black", YEL if destaque else INK2, a, align="left")
    text(c, nome, tl, y + h * 0.56, fit(nome, "black", h * 0.17, maxw), "black", WHITE, a, align="left")
    text(c, sub, tl, y + h * 0.77, fit(sub, "semibold", h * 0.11, maxw), "semibold", INK2, a, align="left")


def b_cta(c, t, C, B):
    a = ep(t, B["start"], 0.25)
    cid = B_CTA
    ta, tb, tc, td = C[cid + ".a"], C[cid + ".b"], C[cid + ".c"], C[cid + ".d"]
    fim = td if td < 1e8 else tc
    if VERT:
        wordmark(c, CX, 330, 120, a)
        busca(c, CX, 520, 860, 120, a * ep(t, ta, 0.3), t, ta + 0.2)
        card_playlist(c, 80, 660, 920, a * ep(t, tb, 0.35), 0, "Redação: Leitura da Proposta", "6 aulas · do zero")
        kf = ep(t, fim, 0.3)
        pulse = 1 + 0.04 * math.sin(t * 6) * kf
        c.save(); c.translate(CX, 1150); c.scale(pulse, pulse)
        pill(c, "BONS ESTUDOS!", 0, 0, 56, YEL, NAVY, a * kf)
        c.restore()
    else:
        wordmark(c, 540, 300, 120, a)
        busca(c, 540, 500, 780, 116, a * ep(t, ta, 0.3), t, ta + 0.2)
        card_playlist(c, 1040, 150, 780, a * ep(t, tb, 0.35), 0, "Redação: Leitura da Proposta", "A série · 6 aulas do zero")
        card_playlist(c, 1040, 470, 780, a * ep(t, tc, 0.35), 5, "Redação ENEM do Zero", "A trilha completa da redação", destaque=False)
        kf = ep(t, fim, 0.3)
        pulse = 1 + 0.04 * math.sin(t * 6) * kf
        c.save(); c.translate(540, 700); c.scale(pulse, pulse)
        pill(c, "TE VEJO NA 1ª AULA!", 0, 0, 52, YEL, NAVY, a * kf)
        c.restore()


B_CTA = "06" if VERT else "12"
BLOCKS = dict(gancho=b_gancho, placar=b_placar, causa=b_causa, teste=b_teste, serie=b_serie, intro=b_intro, eps=b_eps,
              cta=b_cta)

# efeitos sonoros (som_tech.py): carimbo = impact, viradas = whoosh, capas = pop
SFX_short = {"01.a": ["impact@+0.6"], "01.b": ["confirm", "pop@+0.1", "pop@+0.2"], "02.a": ["deny@+0.5"],
             "02.b": ["data"], "02.c": ["alert@+0.6"], "03.a": ["whoosh"], "03.b": ["shimmer"],
             "04.b": ["pop", "pop@+0.35", "pop@+0.7"], "04.c": ["confirm@+0.3"], "04.d": ["impact@+0.2"],
             "05.a": ["pop@+0.15", "pop@+0.32", "pop@+0.49", "pop@+0.66", "pop@+0.83", "pop@+1.0"],
             "06.a": ["typing@+0.2"], "06.b": ["lock"], "06.c": ["shimmer"]}
SFX_horizontal = {"01.a": ["impact@+0.6"], "01.b": ["confirm", "pop@+0.1", "pop@+0.2"], "02.a": ["deny@+0.5"],
                  "02.b": ["data"], "02.c": ["alert@+0.6"], "03.b": ["whoosh"], "03.c": ["shimmer"],
                  "04.b": ["pop", "pop@+0.35", "pop@+0.7"], "04.c": ["confirm@+0.3"], "04.d": ["impact@+0.2"],
                  "04.e": ["deny", "deny@+0.6"], "05.a": ["shimmer@+0.3"],
                  "05.b": ["pop", "pop@+0.1", "pop@+0.2", "pop@+0.3", "pop@+0.4", "pop@+0.5"],
                  "06.a": ["whoosh@-0.3"], "07.a": ["whoosh@-0.3"], "08.a": ["whoosh@-0.3"], "09.a": ["whoosh@-0.3"],
                  "10.a": ["whoosh@-0.3"], "11.a": ["whoosh@-0.3"],
                  "12.a": ["typing@+0.2"], "12.b": ["lock"], "12.c": ["lock"], "12.d": ["shimmer"]}
