"""Componentes reutilizáveis para vídeos de aula (canal de estudos ENEM).

Uso no roteiro/visual.py:
    import motor; motor.set_theme("claro")
    from motor import *
    from aula import *
"""
import math
import skia
import motor
from motor import W, H, ep, prog, ease_back, ease_io, clamp, lerp, mix, text, text_mid, text_w, line, card, pill, \
    rrect, badge_num, check_icon, title_chip, icon, paint, hexc


def C_(nome):
    """cor atual do tema (resolvida em tempo de execução)"""
    return getattr(motor, nome)


def fw(t, t_in, t_out=1e9, d_in=0.45, d_out=0.4):
    return ep(t, t_in, d_in) * (1 - prog(t, t_out, d_out))


def rise(t, t0, d=0.5):
    a = ep(t, t0, d)
    return a, (1 - a) * 18


def frac(c, num, den, cx, cy, size, color=None, a=1.0, peso="bold"):
    color = C_("INK") if color is None else color
    if a <= 0:
        return 0
    w = max(text_w(num, peso, size), text_w(den, peso, size)) + 16
    text(c, num, cx, cy - size * 0.28, size, peso, color, a)
    line(c, cx - w / 2, cy, cx + w / 2, cy, color, a, max(2.5, size * 0.06), cap_round=False)
    text(c, den, cx, cy + size * 0.98, size, peso, color, a)
    return w


def seq(c, parts, x, y, size, a=1.0, align="center", gap=14):
    """linha matemática: partes (texto, cor[, peso]) ou ('FRAC', num, den[, cor])"""
    if a <= 0:
        return 0
    widths = []
    for p in parts:
        if p[0] == "FRAC":
            widths.append(max(text_w(p[1], "bold", size * 0.8), text_w(p[2], "bold", size * 0.8)) + 16)
        else:
            widths.append(text_w(p[0], p[2] if len(p) > 2 else "bold", size))
    total = sum(widths) + gap * (len(parts) - 1)
    xx = x - total / 2 if align == "center" else x
    for p, w in zip(parts, widths):
        if p[0] == "FRAC":
            frac(c, p[1], p[2], xx + w / 2, y - size * 0.32, size * 0.8, p[3] if len(p) > 3 else C_("INK"), a)
        else:
            text(c, p[0], xx, y, size, p[2] if len(p) > 2 else "bold", p[1] if len(p) > 1 and p[1] else C_("INK"), a,
                 align="left")
        xx += w + gap
    return total


def strike(c, x0, y0, x1, y1, a, color=None, progress=1.0):
    line(c, x0, y0, x1, y1, C_("RED") if color is None else color, a, 5, progress=progress)


def mark(c, ok, x, y, a, r=24):
    check_icon(c, x, y, r, a, C_("GREEN") if ok else C_("RED"), "check" if ok else "x")


def head(c, t, t0, l1, l2, col=None, t_out=None):
    title_chip(c, l1, l2, t, t0, C_("BLUE") if col is None else col, t_out=t_out)


def stmt_card(c, t, items, x=140, y=150, w=700, h=690, title="QUESTÃO", size=36):
    card(c, x, y, w, h)
    pill(c, title, x + 30, y + 44, C_("BLUE"), size=22, bounds=(0, 1920))
    yy = y + 120
    for tc, s in items:
        a, dy = rise(t, tc)
        lines = s.split("\n")
        if a > 0:
            for k, ln in enumerate(lines):
                text(c, ln, x + 40, yy + dy + k * (size + 12), size, "semibold", C_("INK"), a, align="left")
        yy += (size + 12) * len(lines) + 26


def sol_card(c, x=880, y=150, w=900, h=690, a=1.0, title="RESOLUÇÃO"):
    card(c, x, y, w, h, a)
    pill(c, title, x + 30, y + 44, C_("GREEN"), size=22, a=a, bounds=(0, 1920))


def result_box(c, s, cx, cy, size, a, color=None):
    color = C_("GREEN") if color is None else color
    if a <= 0:
        return
    w = text_w(s, "black", size) + 60
    h = size * 1.6
    s_ = 0.85 + 0.15 * ease_back(clamp(a))
    c.save(); c.translate(cx, cy); c.scale(s_, s_)
    rrect(c, -w / 2, -h / 2, w, h, 18, color, a * 0.12)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(-w / 2, -h / 2, w, h), 18, 18), paint(color, a, stroke=3))
    text_mid(c, s, 0, 0, size, "black", color, a)
    c.restore()


def cards_row(c, t, items, y=240, cw=440, chh=380, gap=40, title_size=42):
    """cartões numerados lado a lado: items = [(n, texto com \\n, cue_time, cor)]"""
    x0 = W / 2 - (len(items) * cw + (len(items) - 1) * gap) / 2
    for k, (n, s, tc, col) in enumerate(items):
        a, dy = rise(t, tc)
        if a <= 0:
            continue
        x = x0 + k * (cw + gap)
        card(c, x, y + dy, cw, chh, a)
        badge_num(c, n, x + cw / 2, y + 110 + dy, a, 46, bg=col)
        lines = s.split("\n")
        for j, ln in enumerate(lines):
            text(c, ln, x + cw / 2, y + 250 + dy + j * (title_size + 12), title_size, "extrabold", C_("INK"), a)


def errors_list(c, t, rows, x=260, y=170, w=1400, h=680):
    """rows = [(cue_time, errado, certo)]"""
    card(c, x, y, w, h)
    step = (h - 80) / max(1, len(rows))
    for k, (tc, err, ok) in enumerate(rows):
        a, dy = rise(t, tc)
        yy = y + 90 + k * step + dy
        mark(c, False, x + 80, yy - 12, a, 24)
        text(c, err, x + 130, yy, 36, "bold", C_("INK"), a, align="left")
        b = ep(t, tc + 0.6, 0.4)
        mark(c, True, x + 760, yy - 12, b, 24)
        text(c, ok, x + 810, yy, 36, "bold", C_("GREEN"), b, align="left")


def cursor(c, x, y, a, press=0.0):
    if a <= 0:
        return
    s = 1 - 0.15 * press
    c.save(); c.translate(x, y); c.scale(1.6 * s, 1.6 * s)
    p = skia.Path()
    pts = [(0, 0), (0, 22), (6, 17), (10, 26), (14, 24), (10, 15.5), (17, 15.5)]
    p.moveTo(*pts[0])
    for q in pts[1:]:
        p.lineTo(*q)
    p.close()
    c.drawPath(p, paint(C_("INK"), a))
    c.drawPath(p, paint("#FFFFFF", a, stroke=1.6))
    c.restore()


def cta(c, t, like, sub, bell, com, bye, pergunta, despedida="Bons estudos!", canal="no canal", anki=None):
    """anki = tempo do cue {anki}: troca a pergunta pelo aviso dos flashcards (Anki) com link na descrição"""
    INK, BLUE, RED, AMBER, INK2 = C_("INK"), C_("BLUE"), C_("RED"), C_("AMBER"), C_("INK2")
    y = 240
    a = ep(t, like - 0.2, 0.5)
    lx = 300
    card(c, lx, y, 340, 340, a, scale=1 + 0.06 * math.sin(math.pi * prog(t, like + 0.4, 0.5)))
    onl = ep(t, like + 0.5, 0.3)
    icon(c, "", lx + 170, y + 150, 120, mix(INK, BLUE, onl), a)
    text(c, "Curtir", lx + 170, y + 290, 36, "bold", mix(INK, BLUE, onl), a)
    a = ep(t, sub - 0.2, 0.5)
    sx, sw_ = 720, 480
    card(c, sx, y, sw_, 340, a)
    if a > 0:
        done = ep(t, sub + 1.3, 0.3)
        press = math.sin(math.pi * prog(t, sub + 1.1, 0.35))
        bw, bh = 340 * (1 - 0.04 * press), 96 * (1 - 0.04 * press)
        bx, by = sx + sw_ / 2 - bw / 2, y + 130 - bh / 2
        rrect(c, bx, by, bw, bh, 48, mix(RED, "#E5E5EA", done), a, shadow=True)
        text_mid(c, "INSCREVA-SE", bx + bw / 2, by + bh / 2, 34, "extrabold", "#FFFFFF", a * (1 - done))
        text_mid(c, "INSCRITO  ✓", bx + bw / 2, by + bh / 2, 34, "extrabold", INK2, a * done)
        text(c, canal, sx + sw_ / 2, y + 290, 36, "bold", INK, a)
        ca = fw(t, sub + 0.2, bell + 0.4)
        mv = ep(t, sub + 0.2, 0.9)
        cursor(c, lerp(sx + sw_ + 140, bx + bw * 0.62, mv), lerp(y + 420, by + bh * 0.55, mv), ca, press)
    a = ep(t, bell - 0.2, 0.5)
    bxx = 1280
    card(c, bxx, y, 340, 340, a)
    if a > 0:
        ring = prog(t, bell + 0.4, 1.4)
        ang = 18 * math.sin(ring * math.pi * 6) * (1 - ring)
        c.save(); c.translate(bxx + 170, y + 90); c.rotate(ang); c.translate(-(bxx + 170), -(y + 90))
        icon(c, "", bxx + 170, y + 150, 120, mix(INK, AMBER, ep(t, bell + 0.4, 0.3)), a)
        c.restore()
        text(c, "Ativar o sininho", bxx + 170, y + 290, 34, "bold", INK, a)
    a = fw(t, com, anki if anki is not None else bye)
    if a > 0:
        yy = 640 + (1 - a) * 20
        w = max(1000, text_w(pergunta, "bold", 38) + 220)
        card(c, W / 2 - w / 2, yy, w, 130, a, r=36)
        icon(c, "", W / 2 - w / 2 + 90, yy + 65, 56, BLUE, a)
        text_mid(c, pergunta, W / 2 + 40, yy + 65, 38, "bold", INK, a)
    if anki is not None:
        GREEN = C_("GREEN")
        a = fw(t, anki, bye)
        if a > 0:
            yy = 640 + (1 - a) * 20
            s1, s2 = "Flashcards do ENEM (Anki)", "link na descrição do vídeo"
            w = max(text_w(s1, "extrabold", 40), text_w(s2, "bold", 32)) + 260
            card(c, W / 2 - w / 2, yy, w, 150, a, r=36)
            rrect(c, W / 2 - w / 2 + 40, yy + 35, 80, 80, 20, GREEN, a)
            ax, ay = W / 2 - w / 2 + 80, yy + 75
            pa = skia.Paint(AntiAlias=True, Color=hexc("#FFFFFF", a), Style=skia.Paint.kStroke_Style,
                            StrokeWidth=8, StrokeCap=skia.Paint.kRound_Cap, StrokeJoin=skia.Paint.kRound_Join)
            pth = skia.Path(); pth.moveTo(ax, ay - 22); pth.lineTo(ax, ay + 18)
            pth.moveTo(ax - 16, ay + 2); pth.lineTo(ax, ay + 18); pth.lineTo(ax + 16, ay + 2)
            c.drawPath(pth, pa); c.drawLine(ax - 20, ay + 28, ax + 20, ay + 28, pa)
            text(c, s1, W / 2 - w / 2 + 150, yy + 68, 40, "extrabold", INK, a, align="left")
            text(c, s2, W / 2 - w / 2 + 150, yy + 115, 32, "bold", GREEN, a, align="left")
    ab = ep(t, bye, 0.6)
    if ab > 0:
        text(c, despedida, W / 2, 760 + (1 - ab) * 20, 72, "black", INK, ab)


# ---------------- ondas ----------------

def wave_path(x0, x1, y, A, lam, phase=0.0, n=None, env=None):
    """caminho senoidal y = y - A·sin(2π(x-x0)/λ - fase). env(x) -> fator de amplitude (opcional)"""
    p = skia.Path()
    n = n or max(40, int((x1 - x0) / 4))
    for i in range(n + 1):
        x = x0 + (x1 - x0) * i / n
        k = env(x) if env else 1.0
        yy = y - A * k * math.sin(2 * math.pi * (x - x0) / lam - phase)
        p.moveTo(x, yy) if i == 0 else p.lineTo(x, yy)
    return p


def wave(c, x0, x1, y, A, lam, phase=0.0, color=None, a=1.0, width=5, progress=1.0, env=None):
    if a <= 0 or progress <= 0:
        return
    color = C_("BLUE") if color is None else color
    p = wave_path(x0, lerp(x0, x1, progress), y, A, lam, phase, env=env)
    c.drawPath(p, paint(color, a, stroke=width, cap_round=True))


def wave_y(x, x0, y, A, lam, phase=0.0):
    return y - A * math.sin(2 * math.pi * (x - x0) / lam - phase)
