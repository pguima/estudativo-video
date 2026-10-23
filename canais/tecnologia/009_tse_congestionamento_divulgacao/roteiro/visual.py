"""Visual do vídeo Tecnologia 009 — O que aconteceu com o sistema do TSE durante a divulgação dos votos? Tema 'tech'.
Minidocumentário: só motion graphics próprios + cartões de citação com fonte e data.
Toda reconstrução leva o selo RECONSTRUÇÃO ILUSTRATIVA / ILUSTRATIVO. Nenhuma imagem real, manchete ou documento falso."""
import math
from contextlib import contextmanager
import skia
import motor
import tech
from motor import *  # noqa
from tech import *  # noqa

# neste Linux não há Consolas: a fonte mono do tech.py não carrega (sai a fonte padrão). Usa DejaVu Sans Mono.
motor.PESOS["mono"] = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono"
motor.PESOS["monob"] = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold"

tech.SERIE = "TECH//009 · TSE"
MARCA = ""
ARQUIVO_FINAL = "tecnologia_009_tse_congestionamento_divulgacao.mp4"
BACKGROUND, CAPTION, OVERLAY = tech.background, tech.caption, tech.overlay


# ---------------------------------------------------------------- utilidades
def rise(t, t0, d=0.5):
    a = ep(t, t0, d)
    return a, (1 - a) * 24


def fade(t, t0, t1, d=0.5, d_out=0.4):
    """entra em t0, sai em t1"""
    return ep(t, t0, d) * (1 - prog(t, t1, d_out))


@contextmanager
def cam(c, t, B, z0=1.0, z1=1.045, px=0.0, py=0.0, cx=W / 2, cy=H / 2):
    """câmera digital: zoom e pan lentos ao longo do bloco"""
    u = clamp((t - B["start"]) / max(1.0, B["end"] - B["start"]))
    u = u * u * (3 - 2 * u)
    z = lerp(z0, z1, u)
    c.save()
    c.translate(cx + px * u, cy + py * u)
    c.scale(z, z)
    c.translate(-cx, -cy)
    try:
        yield
    finally:
        c.restore()


def selo(c, x, y, a=1.0, s="RECONSTRUÇÃO ILUSTRATIVA", anchor="left", size=20):
    """selo âmbar obrigatório em qualquer reconstrução"""
    if a <= 0:
        return
    chip(c, s, x, y, GOLD, a, anchor=anchor, size=size, filled=True)


def wrap(s, peso, size, maxw):
    words, lines, cur = s.split(), [], ""
    for w in words:
        tst = (cur + " " + w).strip()
        if cur and text_w(tst, peso, size) > maxw:
            lines.append(cur); cur = w
        else:
            cur = tst
    if cur:
        lines.append(cur)
    return lines


def para(c, s, x, y, size, peso, col, a, maxw, lh=None, align="left"):
    lh = lh or size * 1.32
    ls = wrap(s, peso, size, maxw)
    for i, ln in enumerate(ls):
        text(c, ln, x, y + i * lh, size, peso, col, a, align=align)
    return len(ls) * lh


def quote_card(c, x, y, w, a, quote, who, src, col=CYAN, size=40, note=None, label="DECLARAÇÃO"):
    """cartão de citação real: texto literal + autor + fonte e data"""
    if a <= 0:
        return 0
    qs = wrap("“" + quote + "”", "bold", size, w - 120)
    h = 70 + size + len(qs) * size * 1.3 + 24 + (102 if note else 60) + 36
    panel(c, x, y, w, h, a, col, label=label)
    glow_text(c, "“", x + 40, y + 120, 130, "black", col, a * 0.5, align="left", glow=0.3)
    yy = y + 70 + size
    for ln in qs:
        text(c, ln, x + 80, yy, size, "bold", INK, a, align="left")
        yy += size * 1.3
    yy += 24
    c.drawRect(skia.Rect.MakeXYWH(x + 80, yy - 22, 60, 4), paint(col, a))
    text(c, who, x + 80, yy + 20, 28, "extrabold", col, a, align="left")
    text(c, src, x + 80, yy + 60, 22, "mono", INK2, a, align="left")
    if note:
        text(c, note, x + 80, yy + 102, 21, "mono", DIM, a, align="left")
    return h


def monitor(c, cx, cy, s, a, col, screen=None):
    if a <= 0:
        return
    w, h = 1.6 * s, s
    rrect(c, cx - w / 2, cy - h / 2, w, h, 10, "#0B1426", a)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2, cy - h / 2, w, h), 10, 10), paint(col, a, stroke=3))
    c.drawLine(cx, cy + h / 2, cx, cy + h / 2 + s * 0.18, paint(col, a, stroke=4))
    c.drawLine(cx - s * 0.3, cy + h / 2 + s * 0.2, cx + s * 0.3, cy + h / 2 + s * 0.2, paint(col, a, stroke=4, cap_round=True))
    if screen:
        screen(cx - w / 2 + 12, cy - h / 2 + 12, w - 24, h - 24)


def phone(c, cx, cy, s, a, col):
    if a <= 0:
        return
    w, h = s * 0.55, s
    rr = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2, cy - h / 2, w, h), 12, 12)
    c.drawRRect(rr, paint("#0B1426", a))
    c.drawRRect(rr, paint(col, a, stroke=3))
    for i in range(4):
        rrect(c, cx - w / 2 + 12, cy - h / 2 + 22 + i * 18, (w - 24) * (0.5 + 0.5 * hash01(i, 9)), 8, 4, col, a * 0.5)


def urna(c, cx, cy, s, a, col):
    """urna eletrônica estilizada (ícone)"""
    if a <= 0:
        return
    w, h = s * 1.4, s
    p = skia.Path()
    p.moveTo(cx - w / 2 + 18, cy - h / 2); p.lineTo(cx + w / 2 - 18, cy - h / 2); p.lineTo(cx + w / 2, cy + h / 2)
    p.lineTo(cx - w / 2, cy + h / 2); p.close()
    c.drawPath(p, paint("#0B1426", a)); c.drawPath(p, paint(col, a, stroke=3))
    rrect(c, cx - w * 0.36, cy - h * 0.32, w * 0.36, h * 0.42, 4, col, a * 0.35)
    for r in range(4):
        for k in range(3):
            c.drawCircle(cx + w * 0.12 + k * s * 0.13, cy - h * 0.25 + r * s * 0.15, s * 0.04, paint(col, a))


def sigma(c, cx, cy, s, a, col):
    """ícone de soma (Σ desenhado)"""
    if a <= 0:
        return
    p = skia.Path()
    p.moveTo(cx + s * 0.35, cy - s * 0.45); p.lineTo(cx - s * 0.35, cy - s * 0.45); p.lineTo(cx + s * 0.05, cy)
    p.lineTo(cx - s * 0.35, cy + s * 0.45); p.lineTo(cx + s * 0.35, cy + s * 0.45)
    pp = paint(col, a, stroke=s * 0.13, cap_round=True); pp.setStrokeJoin(skia.Paint.kRound_Join)
    c.drawPath(p, blur_paint(col, a * 0.5, 8, stroke=s * 0.13)); c.drawPath(p, pp)


def pause_icon(c, cx, cy, s, a, col):
    if a <= 0:
        return
    for dx in (-s * 0.22, s * 0.22):
        rrect(c, cx + dx - s * 0.1, cy - s * 0.35, s * 0.2, s * 0.7, 4, col, a)


def rack(c, x, y, w, h, a, t, col=CYAN, jam=0.0, label=None):
    """rack de servidores com LEDs (jam: 0 normal → 1 sobrecarga)"""
    if a <= 0:
        return
    panel(c, x, y, w, h, a, mix(col, ROSE, jam), k=16, label=label)
    n = 6
    sh = (h - 60) / n
    for i in range(n):
        yy = y + 30 + i * sh
        rrect(c, x + 22, yy, w - 44, sh - 12, 6, "#0E1930", a)
        for k in range(10):
            c.drawLine(x + 40 + k * 10, yy + 12, x + 40 + k * 10, yy + sh - 24, paint("#22304F", a, stroke=3))
        for k in range(3):
            on = math.sin(t * (6 + 9 * hash01(i, k)) + i * 3 + k) > (0.2 - jam * 0.9)
            led = mix(LIME, ROSE, jam) if k < 2 else mix(CYAN, GOLD, jam)
            c.drawCircle(x + w - 50 - k * 24, yy + (sh - 12) / 2, 6, paint(led, a * (1.0 if on else 0.25)))


def stream(c, x0, y0, x1, y1, t, a, col=CYAN, n=10, speed=0.35, jam=0.0, size=6):
    """fluxo de pacotes; com jam > 0 eles se acumulam perto do destino"""
    if a <= 0:
        return
    c.drawLine(x0, y0, x1, y1, paint(col, 0.22 * a, stroke=2))
    for k in range(n):
        u = (t * speed * (1 - 0.85 * jam) + k / n + hash01(k, 3) * 0.05) % 1.0
        if jam > 0:
            u = lerp(u, 0.78 + 0.2 * (k / n), jam * 0.85)
        x, y = lerp(x0, x1, u), lerp(y0, y1, u)
        cc = mix(col, ROSE, jam * u)
        c.drawRect(skia.Rect.MakeXYWH(x - size, y - size / 2 - 3 * jam * hash01(k, 4), size * 2, size), blur_paint(cc, 0.6 * a, 5))
        c.drawRect(skia.Rect.MakeXYWH(x - size, y - size / 2, size * 2, size), paint("#FFFFFF", a * 0.9))


def glitch(c, x, y, w, h, t, amt, a=1.0):
    """leve distorção digital (faixas e deslocamento) quando a atualização trava"""
    if amt <= 0 or a <= 0:
        return
    for k in range(7):
        seed = math.floor(t * 12) + k * 7
        if hash01(seed, 1) > 0.55:
            yy = y + hash01(seed, 2) * h
            hh = 3 + 18 * hash01(seed, 3)
            off = (hash01(seed, 4) - 0.5) * 40 * amt
            col = (ROSE, CYAN, VIOLET)[k % 3]
            c.drawRect(skia.Rect.MakeXYWH(x + off, yy, w * (0.3 + 0.7 * hash01(seed, 5)), hh), paint(col, 0.16 * amt * a))


def question_marks(c, t, a, n=14):
    if a <= 0:
        return
    for i in range(n):
        x = 180 + hash01(i, 1) * 1560
        y = 250 + hash01(i, 2) * 560 - ((t * 14 * (0.5 + hash01(i, 3))) % 60)
        s = 40 + 80 * hash01(i, 4)
        if 430 < y < 620 and 520 < x < 1400:
            continue
        glow_text(c, "?", x, y, s, "black", (CYAN, VIOLET, GOLD)[i % 3], a * (0.18 + 0.25 * hash01(i, 5)), glow=0.6)


# ======================================================================  CENA 01 — ABERTURA
def _mini_bars(c, x, y, w, h, a, t, freeze_t, t0):
    """barras subindo (painel de resultados genérico, sem candidatos)"""
    n = 7
    for k in range(n):
        tt = min(t, freeze_t)
        v = 0.25 + 0.6 * abs(math.sin(k * 1.3 + 0.5)) * clamp((tt - t0) / 6 + 0.25 * hash01(k, 7))
        bw = w / n * 0.62
        bx = x + k * w / n + (w / n - bw) / 2
        rrect(c, bx, y + h - h * v, bw, h * v, 4, (CYAN, VIOLET, LIME)[k % 3], a * 0.85)


def b_abertura(c, t, C, B):
    tq = C["01.q"]
    if t < tq:
        with cam(c, t, dict(start=B["start"], end=tq), 1.0, 1.06, 0, -10):
            head(c, t, B["start"], "04.10.2026 · ELEIÇÕES 2026", "A NOITE DA DIVULGAÇÃO")
            aa = ep(t, C["01.a"], 0.6)
            jam = ep(t, C["01.c"], 0.8)
            # parede de monitores (reconstrução genérica, sem dados reais de candidatos)
            if aa > 0:
                panel(c, 150, 250, 980, 560, aa, mix(CYAN, ROSE, jam), label="resultados · reconstrução")
                text(c, "TOTALIZAÇÃO · PRESIDENTE", 200, 330, 30, "monob", INK2, aa, align="left")
                pct = 64 * clamp((min(t, C["01.c"]) - C["01.a"] + 6) / 9)
                glow_text(c, f"{pct:.0f}%", 200, 500, 150, "black", mix(CYAN, GOLD, jam), aa, align="left", glow=0.35)
                bar_meter(c, 200, 560, 880, 22, pct / 100, mix(CYAN, GOLD, jam), aa)
                text(c, "seções totalizadas", 200, 620, 26, "mono", DIM, aa, align="left")
                _mini_bars(c, 640, 330, 440, 190, aa * 0.9, t, C["01.c"], C["01.a"])
                if jam > 0:
                    blink = 0.6 + 0.4 * math.sin(t * 5)
                    chip(c, "ATUALIZAÇÃO PAUSADA", 200, 700, ROSE, jam * blink, size=30, filled=True)
                    pause_icon(c, 760, 700, 50, jam, ROSE)
                    # ponteiro de carregamento girando sem sair do lugar
                    for k in range(8):
                        ang = t * 4 + k * math.pi / 4
                        c.drawCircle(1000 + 26 * math.cos(ang), 700 + 26 * math.sin(ang), 4 + k * 0.6,
                                     paint(INK2, jam * (0.15 + k * 0.1)))
                glitch(c, 150, 250, 980, 560, t, jam, aa)
                selo(c, 150, 852, aa)
            # monitores menores à direita
            ab = ep(t, C["01.b"], 0.6)
            for k in range(3):
                ak = ab * ep(t, C["01.b"] + 0.25 * k, 0.5)
                if ak <= 0:
                    continue
                cy = 320 + k * 190
                def scr(x, y, w, h, k=k):
                    for i in range(6):
                        v = 0.3 + 0.6 * hash01(i, k + 2)
                        rrect(c, x + 10 + i * (w - 20) / 6, y + h - h * v * 0.85, (w - 20) / 6 * 0.6, h * v * 0.85, 3,
                              (CYAN, VIOLET, LIME)[(i + k) % 3], ak * (1 - 0.6 * jam))
                monitor(c, 1500, cy, 140, ak, mix(CYAN, ROSE, jam * (k == 1)), scr)
                glitch(c, 1388, cy - 70, 224, 140, t + k, jam * (k == 1), ak)
            ac = ep(t, C["01.c"], 0.5)
            chip(c, "CONGESTIONAMENTO", 1500, 840, ROSE, ac, anchor="center", size=26, filled=True)
        return
    # corte seco: tela preta
    c.drawRect(skia.Rect.MakeWH(W, H), paint("#000000", 1.0))
    a = prog(t, tq, 0.08)
    s = 1.0 + 0.04 * ep(t, tq, 1.2)
    c.save(); c.translate(W / 2, 470); c.scale(s, s); c.translate(-W / 2, -470)
    glow_text(c, "O QUE ACONTECEU?", W / 2, 510, 150, "black", INK, a, glow=0.25)
    c.restore()
    ar = ep(t, C["01.r"], 0.6)
    text(c, "a contagem dos votos foi interrompida?", W / 2, 640, 40, "mono", CYAN, ar)


# ======================================================================  CENA 02 — O CONGESTIONAMENTO
def b_congest(c, t, C, B):
    with cam(c, t, B, 1.0, 1.05, -20, 0):
        head(c, t, B["start"], "DOMINGO · 04/10/2026 · 1º TURNO", "O CONGESTIONAMENTO", CYAN)
        ad = fade(t, C["02.d"], C["02.a"] - 0.3)
        if ad > 0:
            # data em destaque
            panel(c, 460, 330, 1000, 380, ad, CYAN, label="data")
            glow_text(c, "04.10.2026", W / 2, 520, 130, "black", INK, ad, glow=0.25)
            text(c, "1º turno · Eleições 2026 · votação encerrada às 17h", W / 2, 610, 26, "mono", INK2, ad)
        aa = ep(t, C["02.a"], 0.6)
        jam = ep(t, C["02.b"] + 0.5, 1.6)
        stop = ep(t, C["02.c"], 0.5)
        if aa > 0:
            # entrada: dados chegando
            text(c, "DADOS RECEBIDOS", 330, 420, 26, "monob", DIM, aa)
            for k in range(5):
                stream(c, 170, 470 + k * 70, 680, 610, t + k * 0.13, aa, CYAN, n=6, speed=0.3 + 0.08 * k, jam=jam)
            rack(c, 700, 400, 360, 420, aa, t, CYAN, jam, label="sistema de divulgação")
            # saída: público
            out = 1 - stop
            link(c, 1080, 610, 1440, 610, mix(CYAN, ROSE, stop), aa, t, progress=ep(t, C["02.a"] + 0.4, 0.6),
                 pulses=3 if out > 0.5 else 0, dash=stop > 0.5)
            monitor(c, 1580, 590, 120, aa, mix(CYAN, ROSE, stop))
            phone(c, 1730, 700, 110, aa, mix(CYAN, ROSE, stop))
            text(c, "PÚBLICO", 1640, 810, 26, "monob", DIM, aa)
            if stop > 0:
                pause_icon(c, 1260, 610, 70, stop, ROSE)
                chip(c, "ATUALIZAÇÃO INTERROMPIDA", 1260, 700, ROSE, stop, anchor="center", size=24, filled=True)
        # gráfico de fluxo (ilustrativo)
        ab = ep(t, C["02.b"], 0.6)
        if ab > 0:
            px, py, pw, ph = 1150, 175, 620, 240
            a2 = ab
            panel(c, px, py, pw, ph, a2, GOLD, k=14, label="fluxo de dados")
            base = py + ph - 40
            cap_y = py + 100
            line(c, px + 30, cap_y, px + pw - 30, cap_y, GOLD, a2 * 0.8, 2, dash=(10, 8))
            text(c, "capacidade", px + pw - 30, cap_y - 10, 18, "mono", GOLD, a2, align="right")
            pts = []
            prog_ = ep(t, C["02.b"], 3.0)
            N = 40
            for i in range(int(N * prog_) + 1):
                u = i / N
                v = 0.25 + 0.1 * math.sin(u * 14) * (1 - u) + 0.75 * max(0, u - 0.35) ** 1.4 * 2.2
                pts.append((px + 30 + u * (pw - 60), base - min(v, 1.05) * (base - py - 40)))
            for (x0, y0), (x1, y1) in zip(pts, pts[1:]):
                col = ROSE if y1 < cap_y else CYAN
                c.drawLine(x0, y0, x1, y1, blur_paint(col, a2 * 0.5, 5, stroke=6))
                c.drawLine(x0, y0, x1, y1, paint(col, a2, stroke=3, cap_round=True))
            text(c, "requisições", px + 30, py + ph - 12, 18, "mono", DIM, a2, align="left")
            selo(c, px + pw, py + ph + 32, a2, "GRÁFICO ILUSTRATIVO · SEM ESCALA REAL", anchor="right", size=17)


# ======================================================================  linha do tempo 19h → 20h
def b_linha(c, t, C, B):
    with cam(c, t, B, 1.02, 1.0, 0, 0):
        tq = C["03.d"]
        head(c, t, B["start"], "LINHA DO TEMPO · 04/10/2026", "64% → 84%", GOLD)
        al = 1 - prog(t, tq - 0.2, 0.5)
        aa = ep(t, C["03.a"], 0.6) * al
        if aa > 0:
            x0, x1, y = 220, 1700, 640
            # eixo de horário 18h45 → 20h15
            def X(h, m):
                return x0 + ((h * 60 + m) - (18 * 60 + 45)) / 90 * (x1 - x0)
            glow_line(c, x0, y, x1, y, CYAN, aa * 0.6, 2, progress=ep(t, C["03.a"], 1.0))
            for hh, mm in ((19, 0), (19, 15), (19, 30), (19, 45), (20, 0)):
                c.drawLine(X(hh, mm), y - 10, X(hh, mm), y + 10, paint(INK2, aa, stroke=2))
                text(c, f"{hh}h{mm:02d}" if mm else f"{hh}h", X(hh, mm), y + 48, 26, "mono", INK2, aa)
            # 19h: 64%
            xa = X(19, 6)
            c.drawCircle(xa, y, 12, paint(GOLD, aa))
            panel(c, xa - 170, 300, 340, 220, aa, GOLD, k=16, label="por volta das 19h")
            glow_text(c, "64%", xa, 440, 110, "black", INK, aa, glow=0.2)
            text(c, "totalização · presidente", xa, 490, 22, "mono", INK2, aa)
            line(c, xa, 520, xa, y - 14, GOLD, aa, 2, dash=(6, 6))
            # trecho parado
            ab = ep(t, C["03.b"], 0.6) * al
            xb = X(20, 8)
            fr = ep(t, C["03.a"] + 0.6, 2.0)
            if aa > 0:
                rrect(c, xa, y - 30, (xb - xa) * fr, 60, 8, ROSE, aa * 0.14)
                glow_line(c, xa, y, lerp(xa, xb, fr), y, ROSE, aa, 5)
                if fr > 0.3:
                    text(c, "sem atualização na tela", (xa + xb) / 2, y - 48, 26, "monob", ROSE, aa * ep(t, C["03.a"] + 1.2, 0.5))
            if ab > 0:
                c.drawCircle(xb, y, 12, paint(LIME, ab))
                panel(c, xb - 170, 300, 340, 220, ab, LIME, k=16, label="por volta das 20h")
                glow_text(c, "84%", xb, 440, 110, "black", INK, ab, glow=0.2)
                text(c, "atualização retomada", xb, 490, 22, "mono", INK2, ab)
                line(c, xb, 520, xb, y - 14, LIME, ab, 2, dash=(6, 6))
            acx = ep(t, C["03.c"], 0.6) * al
            if acx > 0:
                chip(c, "ATRASO DE CERCA DE 1 HORA", W / 2, 760, GOLD, acx, anchor="center", size=30, filled=True)
                text(c, "registros: 64,81% às 19h06 · 84,96% às 20h08  (Canaltech e SpaceMoney, 05/10/2026)",
                     W / 2, 830, 22, "mono", DIM, acx)
            text(c, "fonte: Agência Brasil (04/10/2026) · Jornal do Brasil (05/10/2026)", W / 2, 870, 22, "mono", DIM,
                 aa * ep(t, C["03.a"] + 1, 0.5) * (1 - ep(t, C["03.c"], 0.3)))
        aq = ep(t, tq, 0.7)
        if aq > 0:
            quote_card(c, 260, 330, 1400, aq, "Antes da eficiência ou da rapidez, prezamos pela segurança",
                       "Kassio Nunes Marques, presidente do TSE",
                       "coletiva de 04/10/2026 · via Brasil 61", GOLD, size=52,
                       note="no portal do TSE: “Antes da rapidez e da eficiência, prezamos pela segurança.”")


# ======================================================================  CENA 03 — três etapas
XS = (380, 960, 1540)
NY = 430
ST = [("APURAÇÃO", CYAN), ("TOTALIZAÇÃO", VIOLET), ("DIVULGAÇÃO", LIME)]
DEFS = ["cada urna conta os votos da sua seção e gera o Boletim de Urna (BU)",
        "os resultados de todas as urnas do país e do exterior são reunidos e somados",
        "os resultados chegam ao Portal Resultados e aos demais canais"]


def etapas(c, t, cues, a_all=1.0, warn=0.0, ghost=0.0):
    for k, (lab, col) in enumerate(ST):
        a = ep(t, cues[k], 0.6) * a_all
        if a < ghost:  # contorno apagado antes de a etapa ser nomeada
            node(c, XS[k], NY, 95, None, None, DIM, ghost - a, t)
            text(c, "?", XS[k], NY + 22, 64, "black", DIM, ghost - a)
        cc = mix(col, GOLD, warn) if k == 2 else col
        if k > 0:
            pa = min(a, ep(t, cues[k - 1], 0.5) * a_all)
            lc = ST[k - 1][1] if not (k == 2 and warn > 0.5) else GOLD
            link(c, XS[k - 1] + 110, NY, XS[k] - 110, NY, lc, pa, t, progress=ep(t, cues[k], 0.7),
                 pulses=(0 if (k == 2 and warn > 0.5) else 4), dash=(k == 2 and warn > 0.5))
        node(c, XS[k], NY, 95, None, None, cc, a, t)
        if a > 0:
            if k == 0:
                urna(c, XS[k], NY, 70, a, cc)
            elif k == 1:
                sigma(c, XS[k], NY, 80, a, cc)
            else:
                monitor(c, XS[k] - 14, NY - 10, 44, a, cc)
                phone(c, XS[k] + 40, NY + 12, 46, a, cc)
            glow_text(c, lab, XS[k], NY + 165, 42, "black", INK, a, glow=0.15)
            text(c, f"ETAPA {k + 1}", XS[k], NY - 130, 22, "monob", cc, a)


def b_etapas(c, t, C, B):
    with cam(c, t, B, 1.0, 1.04, 0, 10):
        head(c, t, B["start"], "A CONTAGEM DOS VOTOS PAROU?", "TRÊS ETAPAS DIFERENTES", VIOLET)
        etapas(c, t, [C["04.a"], C["04.b"], C["04.c"]], ghost=ep(t, C["04.t"] + 0.6, 0.8) * 0.5)
        at = fade(t, C["04.t"] + 1.5, C["04.a"] - 0.2)
        if at > 0:
            for k, s in enumerate(("da urna", "à soma", "à tela")):
                text(c, s, XS[k], NY + 175, 34, "monob", INK2, at * ep(t, C["04.t"] + 1.5 + 0.7 * k, 0.5))
        for k, cue in enumerate(("04.d", "04.e", "04.f")):
            a = ep(t, C[cue], 0.5)
            if a <= 0:
                continue
            col = ST[k][1]
            panel(c, XS[k] - 260, 650, 520, 170, a, col, k=14, fill=0.85, glow=False)
            para(c, DEFS[k], XS[k] - 230, 705, 27, "medium", INK, a, 460, lh=36)
        text(c, "definições: portal do TSE (outubro/2026)", W - 150, 880, 20, "mono", DIM,
             ep(t, C["04.d"], 0.5), align="right")


def b_visualiza(c, t, C, B):
    with cam(c, t, B, 1.04, 1.0, 0, 0):
        head(c, t, B["start"], "A CONTAGEM DOS VOTOS PAROU?", "FALHA NA TELA ≠ VOTO PERDIDO", VIOLET)
        warn = ep(t, B["start"] + 0.3, 0.8)
        etapas(c, t, [B["start"] - 5] * 3, warn=warn)
        if warn > 0:
            pause_icon(c, XS[2], NY - 200, 50, warn, GOLD)
        av = fade(t, C["05.a"] + 0.3, C["05.b"] - 0.2)
        if av > 0:
            chip(c, "TELA SEM ATUALIZAR", XS[2], 700, GOLD, av, anchor="center", size=28, filled=True)
            chip(c, "CONTAGEM DOS VOTOS", (XS[0] + XS[1]) / 2, 700, LIME, av * ep(t, C["05.a"] + 1.2, 0.5),
                 anchor="center", size=28)
            glow_text(c, "≠", (XS[1] + XS[2]) / 2 + 40, 735, 90, "black", INK2, av * ep(t, C["05.a"] + 2.0, 0.5), glow=0.3)
            text(c, "uma coisa não implica a outra", W / 2, 820, 26, "mono", DIM, av * ep(t, C["05.a"] + 2.5, 0.5))
        ab = ep(t, C["05.b"], 0.6)
        if ab > 0:
            panel(c, 260, 650, 1400, 190, ab, LIME, label="segundo o TSE")
            para(c, "“a dificuldade ficou restrita à conversão dos dados pelo programa de divulgação e não afetou "
                    "a totalização dos votos”", 310, 712, 32, "bold", INK, ab, 1300, lh=42)
            text(c, "portal do TSE · pronunciamento de 04/10/2026", 310, 815, 22, "mono", INK2, ab, align="left")
        acc = ep(t, C["05.c"], 0.5)
        if acc > 0:
            check_icon(c, XS[0] + 80, NY - 80, 22, acc, LIME)
            check_icon(c, XS[1] + 80, NY - 80, 22, acc, LIME)


# ======================================================================  CENA 04 — HOUVE FRAUDE?
def boletim(c, x, y, w, h, a, t):
    """boletim de urna ILUSTRATIVO (sem dados reais)"""
    if a <= 0:
        return
    rr = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 6, 6)
    c.drawRRect(rr, paint("#E9EEF6", a * 0.95))
    text(c, "BOLETIM DE URNA", x + w / 2, y + 50, 26, "monob", "#0B1426", a)
    text(c, "modelo ilustrativo", x + w / 2, y + 80, 18, "mono", "#55607A", a)
    for i in range(7):
        yy = y + 120 + i * 34
        rrect(c, x + 26, yy, (w - 52) * (0.35 + 0.3 * hash01(i, 11)), 12, 6, "#9AA6BD", a)
        rrect(c, x + w - 26 - 60, yy, 60, 12, 6, "#9AA6BD", a)
    # QR genérico
    q = 10
    qx, qy = x + w / 2 - q * 6.5, y + h - 160
    for i in range(13):
        for j in range(13):
            corner = (i < 3 and j < 3) or (i > 9 and j < 3) or (i < 3 and j > 9)
            if corner or hash01(i * 13 + j, 21) > 0.52:
                c.drawRect(skia.Rect.MakeXYWH(qx + i * q, qy + j * q, q, q), paint("#0B1426", a))
    selo(c, x + w / 2, y + h + 34, a, "ILUSTRATIVO", anchor="center", size=20)


def b_fraude(c, t, C, B):
    with cam(c, t, B, 1.0, 1.04, 0, -10):
        head(c, t, B["start"], "HOUVE FRAUDE?", "SEPARAR OS FATOS", ROSE)
        tq = C["06.e"]
        aq = ep(t, C["06.a"], 0.6) * (1 - prog(t, C["06.b"], 0.5))
        question_marks(c, t, aq)
        if aq > 0:
            glow_text(c, "QUESTIONAMENTOS", W / 2, 560, 96, "black", INK, aq, glow=0.2)
        ab = ep(t, C["06.b"], 0.6) * (1 - prog(t, tq - 0.2, 0.5))
        if ab > 0:
            ad = ep(t, C["06.d"], 0.5)
            # comparação
            lw = 640
            panel(c, 170, 280, lw, 470, ab, GOLD, label="o que o TSE relatou")
            glow_text(c, "FALHA DE", 170 + lw / 2, 380, 50, "black", INK, ab, glow=0.15)
            glow_text(c, "DIVULGAÇÃO", 170 + lw / 2, 440, 50, "black", GOLD, ab, glow=0.3)
            for i, s in enumerate(("a tela deixa de atualizar", "o público recebe os números com atraso",
                                   "não muda o que a urna registrou")):
                ai = ab * ep(t, C["06.b"] + 0.4 + 0.3 * i, 0.4)
                c.drawCircle(220, 515 + i * 70, 7, paint(GOLD, ai))
                text(c, s, 245, 525 + i * 70, 28, "medium", INK, ai, align="left")
            ac = ep(t, C["06.c"], 0.6) * ab
            glow_text(c, "≠", 875, 560, 120, "black", INK2, ac, glow=0.3)
            panel(c, 940, 280, lw, 470, ac, ROSE, label="outra coisa")
            glow_text(c, "ALTERAÇÃO", 940 + lw / 2, 380, 50, "black", INK, ac, glow=0.15)
            glow_text(c, "DE DADOS", 940 + lw / 2, 440, 50, "black", ROSE, ac, glow=0.3)
            for i, s in enumerate(("mudaria votos registrados", "exigiria prova técnica verificável",
                                   "as fontes consultadas não apontam isso")):
                ai = ac * ep(t, C["06.c"] + 0.4 + 0.3 * i, 0.4)
                c.drawCircle(990, 515 + i * 70, 7, paint(ROSE, ai))
                text(c, s, 1015, 525 + i * 70, 28, "medium", INK, ai, align="left")
            if ad > 0:
                chip(c, "CONGESTIONAMENTO ≠ PROVA DE ALTERAÇÃO", W / 2, 820, LIME, ad, anchor="center", size=28,
                     filled=True)
        ae = ep(t, tq, 0.6)
        if ae > 0:
            boletim(c, 190, 240 + (1 - ae) * 20, 380, 540, ae, t)
            h1 = quote_card(c, 640, 225, 1140, ae, "O que ocorreu foi um congestionamento de dados.",
                            "Kassio Nunes Marques, presidente do TSE", "coletiva de 04/10/2026 · via Agência Brasil",
                            CYAN, size=31)
            a2 = ep(t, tq + 1.6, 0.6)
            quote_card(c, 640, 225 + h1 + 36, 1140, a2, "A princípio, não se sabe se isso foi derivado de outro problema.",
                       "Kassio Nunes Marques, presidente do TSE", "coletiva de 04/10/2026 · via Agência Brasil",
                       GOLD, size=31)


# ======================================================================  CENA 05 — AS PERGUNTAS
PERG = [("07.a", "Qual componente do sistema enfrentou o congestionamento?"),
        ("07.b", "Por que a infraestrutura não conseguiu absorver o volume de dados?"),
        ("07.c", "Quais mecanismos de redundância foram acionados?"),
        ("07.d", "Quais medidas podem impedir que o problema volte a acontecer?")]


def _monitoring(c, t, a):
    """painéis de monitoramento ao fundo (genéricos, ilustrativos)"""
    if a <= 0:
        return
    for k in range(3):
        x = 1290
        y = 250 + k * 210
        panel(c, x, y, 470, 180, a * 0.8, (CYAN, VIOLET, GOLD)[k], k=12, glow=False, label=("cpu", "rede", "fila")[k])
        pts = []
        for i in range(60):
            u = i / 59
            v = 0.5 + 0.3 * math.sin(u * 9 + t * (1.2 + k * 0.4) + k) * math.sin(u * 3.3 + k)
            pts.append((x + 20 + u * 430, y + 150 - v * 110))
        for (x0, y0), (x1, y1) in zip(pts, pts[1:]):
            c.drawLine(x0, y0, x1, y1, paint((CYAN, VIOLET, GOLD)[k], a * 0.8, stroke=2.5))


def b_perguntas(c, t, C, B):
    with cam(c, t, B, 1.0, 1.035, 0, 0):
        az = fade(t, C["07.z"], C["07.t"] - 0.2)
        if az > 0:
            panel(c, 360, 330, 1200, 360, az, GOLD, label="consulta em 22/10/2026")
            text(c, "RELATÓRIO TÉCNICO PÚBLICO", W / 2, 450, 52, "black", INK, az)
            text(c, "detalhando o incidente", W / 2, 510, 34, "medium", INK2, az)
            chip(c, "NÃO ENCONTRADO", W / 2, 600, GOLD, az, anchor="center", size=34, filled=True)
        at = ep(t, C["07.t"], 0.5)
        if at > 0:
            head(c, t, C["07.t"], "DO PONTO DE VISTA TECNOLÓGICO", "PERGUNTAS EM ABERTO", GOLD)
            _monitoring(c, t, at)
            cur = max([i for i, (cue, _) in enumerate(PERG) if t >= C[cue]] or [-1])
            for i, (cue, s) in enumerate(PERG):
                a, d = rise(t, C[cue])
                if a <= 0:
                    continue
                y = 260 + i * 160 + d
                hi = 1.0 if i == cur else 0.45
                col = (CYAN, VIOLET, MAGENTA, LIME)[i]
                panel(c, 150, y, 1080, 130, a * (0.55 + 0.45 * hi), col if i == cur else DIM, k=14, glow=i == cur)
                glow_text(c, f"{i + 1:02d}", 215, y + 85, 44, "black", col, a * (0.5 + 0.5 * hi), glow=0.4 * hi)
                para(c, s, 290, y + 58, 32, "bold", mix(INK2, INK, hi), a, 900, lh=40)


# ======================================================================  CENA 06 — ENCERRAMENTO
def b_fim(c, t, C, B):
    tx = C["08.x"]
    zoom_end = dict(start=B["start"], end=B["end"])
    with cam(c, t, zoom_end, 1.0, 1.06, 0, 0):
        a1 = ep(t, C["08.a"], 0.6) * (1 - prog(t, tx - 0.3, 0.6))
        if a1 > 0:
            glow_text(c, "CONFIANÇA", W / 2, 360, 120, "black", INK, a1, glow=0.2)
            for k, (s, col) in enumerate((("SEGURANÇA DOS SISTEMAS", CYAN), ("TRANSPARÊNCIA", LIME))):
                ak = a1 * ep(t, C["08.a"] + 1.2 + 1.6 * k, 0.6)
                chip(c, s, W / 2 + (k * 2 - 1) * 380, 470, col, ak, anchor="center", size=32)
                link(c, W / 2 + (k * 2 - 1) * 380, 440, W / 2, 380, col, ak * 0.8, t, pulses=2)
        ab = ep(t, C["08.b"], 0.6) * (1 - prog(t, tx - 0.3, 0.6))
        for k, (s, col) in enumerate((("INVESTIGAR FALHAS", GOLD), ("DIVULGAR EXPLICAÇÕES TÉCNICAS", VIOLET),
                                      ("IMPLEMENTAR MELHORIAS", LIME))):
            ak = ab * ep(t, C["08.b"] + 0.9 * k, 0.5)
            if ak <= 0:
                continue
            x = 370 + k * 590
            panel(c, x - 270, 600, 540, 150, ak, col, k=14)
            text_mid(c, f"0{k + 1}", x - 220, 675, 40, "black", col, ak)
            for i, ln in enumerate(wrap(s, "extrabold", 30, 360)):
                text(c, ln, x - 160, 670 + i * 38 - (len(wrap(s, "extrabold", 30, 360)) - 1) * 19 + 10, 30, "extrabold",
                     INK, ak, align="left")
    ax = ep(t, tx, 0.8)
    if ax > 0:
        c.drawRect(skia.Rect.MakeWH(W, H), paint("#02030A", 0.55 * ax))
        for k, (s, col) in enumerate((("TRANSPARÊNCIA.", CYAN), ("SEGURANÇA.", LIME), ("INFORMAÇÃO.", GOLD))):
            ak = ep(t, tx + 0.6 * k, 0.8)
            glow_text(c, s, W / 2, 400 + k * 130 + (1 - ak) * 14, 104, "black", col if k else col, ak, glow=0.35)
        glow_line(c, W / 2 - 360, 690, W / 2 + 360, 690, CYAN, ax, 3, progress=ep(t, tx + 1.8, 1.0))


# ======================================================================  CTA + FONTES
def b_cta(c, t, C, B):
    head(c, t, B["start"], "TECH//009", "OBRIGADO POR ASSISTIR", CYAN)
    cta(c, t, C["09.like"], C["09.sub"], C["09.bell"], C["09.com"], C["09.bye"],
        "Qual dessas perguntas você quer ver respondida?")


FONTES = [
    ("TSE · portal", "Presidente do TSE conclui 1º turno das Eleições 2026", "04/10/2026"),
    ("TSE · portal", "Saiba como foi a totalização dos votos no 1º turno / Entenda a diferença entre apuração e totalização", "out/2026"),
    ("Agência Brasil", "Congestionamento no sistema de dados gerou atraso na apuração, diz TSE", "04/10/2026"),
    ("Brasil 61", "Congestionamento de dados atrasa divulgação dos resultados das eleições, diz TSE", "04/10/2026"),
    ("CNN Brasil", "TSE registrou congestionamento no sistema de divulgação, diz Nunes Marques", "04/10/2026"),
    ("Jornal do Brasil", "Apuração do primeiro turno sofre atraso após problema no sistema do TSE", "05/10/2026"),
    ("SBT News", "TSE atribui atraso na apuração a congestionamento de dados", "05/10/2026"),
    ("Canaltech", "Por que os resultados do 1º turno das eleições travaram por mais de 1 hora", "05/10/2026"),
    ("SpaceMoney", "Falha no sistema de divulgação atrasa apuração do 1º turno", "05/10/2026"),
]


def b_fontes(c, t, C, B):
    head(c, t, B["start"], "CRÉDITOS", "FONTES", CYAN)
    a0 = ep(t, B["start"] + 0.2, 0.6)
    panel(c, 150, 230, 1620, 640, a0, CYAN, label="consultadas em 22/10/2026")
    for i, (v, tit, d) in enumerate(FONTES):
        a = ep(t, B["start"] + 0.4 + 0.12 * i, 0.4)
        y = 300 + i * 56
        text(c, v, 200, y, 26, "extrabold", CYAN, a, align="left")
        tt = tit if text_w(tit, "medium", 24) < 1040 else wrap(tit, "medium", 24, 1000)[0] + "…"
        text(c, tt, 450, y, 24, "medium", INK, a, align="left")
        text(c, d, 1720, y, 24, "mono", INK2, a, align="right")
    ab = ep(t, B["start"] + 1.8, 0.6)
    text(c, "Imagens: motion graphics do canal · reconstruções e gráficos marcados como ilustrativos · "
            "narração com voz sintética (IA)", W / 2, 840, 22, "mono", DIM, ab)


BLOCKS = dict(abertura=b_abertura, congest=b_congest, linha=b_linha, etapas=b_etapas, visualiza=b_visualiza,
              fraude=b_fraude, perguntas=b_perguntas, fim=b_fim, cta=b_cta, fontes=b_fontes)
