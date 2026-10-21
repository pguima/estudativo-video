"""Visual do vídeo Tecnologia 003 — Claude Motion: animações feitas com código. Tema 'tech' (futurista)."""
import math
import re
import skia
import tech
from motor import *  # noqa
from tech import *  # noqa

tech.SERIE = "TECH//003 · MOTION"
MARCA = ""
ARQUIVO_FINAL = "tecnologia_003_claude_motion.mp4"
BACKGROUND, CAPTION, OVERLAY = tech.background, tech.caption, tech.overlay


# ---------------- peças deste vídeo ----------------
def bars(c, x, y, w, h, vals, col, a, grow=1.0, labels=None, hi=None, gap=0.32):
    """barras verticais (vals 0..1), base em y+h"""
    if a <= 0:
        return
    n = len(vals)
    bw = w / n
    for i, v in enumerate(vals):
        g = ease_out(clamp(grow * 1.6 - i * 0.6 / n))
        bh = h * v * g
        cc = hi if hi is not None and i == n - 1 else col
        rrect(c, x + i * bw + bw * gap / 2, y + h - bh, bw * (1 - gap), bh, 4, cc, a)
        if labels:
            text(c, labels[i], x + i * bw + bw / 2, y + h + 34, 20, "mono", DIM, a)
    c.drawLine(x, y + h, x + w, y + h, paint(DIM, 0.6 * a, stroke=1.5))


def linechart(c, x, y, w, h, pts, col, a, progress=1.0):
    if a <= 0 or progress <= 0:
        return
    n = len(pts)
    m = max(2, int(1 + (n - 1) * clamp(progress)))
    p = skia.Path()
    for i in range(m):
        (p.moveTo if i == 0 else p.lineTo)(x + w * i / (n - 1), y + h - h * pts[i])
    c.drawPath(p, blur_paint(col, 0.5 * a, 6, stroke=8))
    c.drawPath(p, paint(col, a, stroke=4, cap_round=True))
    c.drawCircle(x + w * (m - 1) / (n - 1), y + h - h * pts[m - 1], 8, paint(INK, a))


def bubble(c, x, y, w, h, a, col=VIOLET, who="você"):
    panel(c, x, y, w, h, a, col, k=16, label=who)


def loop(t, period=4.0):
    """fase 0..1 de uma animação em loop (para as prévias que 'rodam')"""
    return (t % period) / period


def play_icon(c, cx, cy, r, col, a):
    if a <= 0:
        return
    c.drawCircle(cx, cy, r, blur_paint(col, 0.35 * a, 14))
    c.drawCircle(cx, cy, r, paint(PANEL, 0.9 * a))
    c.drawCircle(cx, cy, r, paint(col, a, stroke=3))
    p = skia.Path(); p.moveTo(cx - r * 0.3, cy - r * 0.42); p.lineTo(cx + r * 0.48, cy); p.lineTo(cx - r * 0.3, cy + r * 0.42); p.close()
    c.drawPath(p, paint(col, a))


def scrub(c, x, y, w, frac, col, a):
    """barra de reprodução com cabeça"""
    if a <= 0:
        return
    rrect(c, x, y, w, 8, 4, "#1A2440", a)
    rrect(c, x, y, w * frac, 8, 4, col, a)
    c.drawCircle(x + w * frac, y + 4, 11, paint(INK, a))


def preview(c, x, y, w, h, t, a, col=MAGENTA, label="preview", num="R$ 4,2 mi", period=4.0):
    """'player' com uma animação de exemplo rodando em loop: título, número e barras crescendo"""
    if a <= 0:
        return
    panel(c, x, y, w, h, a, col, label=label)
    u = loop(t, period)
    at = ep(u * period, 0.1, 0.5)
    text(c, "RESULTADO DO TRIMESTRE", x + 40, y + 80, 24, "monob", DIM, a * at, align="left")
    an = ep(u * period, 0.5, 0.6)
    glow_text(c, num, x + 40, y + 80 + 70 + (1 - an) * 16, 60, "black", INK, a * an, align="left", glow=0.12)
    bh = h - 270
    if bh > 60:
        bars(c, x + 40, y + 190, w - 80, bh, [0.45, 0.6, 0.52, 0.9], col, a, prog(u * period, 1.0, 1.6), hi=LIME)
    scrub(c, x + 40, y + h - 46, w - 80, u, col, a)


CODE_KW = {"scene", "text", "bar_chart", "fade_in", "grow", "duration", "at", "image", "shape", "move", "def", "for",
           "panel", "bars", "caption", "return"}


def code(c, lines, x, y, size, t, t0, a=1.0, step=0.2, hi_line=None, hi_col=GOLD, hi_w=820):
    """código com realce: chamadas violeta, números âmbar, strings verdes"""
    lh = size * 1.5
    for i, ln in enumerate(lines):
        ai = ep(t, t0 + i * step, 0.3) * a
        if ai <= 0:
            continue
        if hi_line == i:
            c.drawRect(skia.Rect.MakeXYWH(x - 14, y + i * lh - size * 0.95, hi_w, lh), paint(hi_col, 0.14 * ai))
        xx = x
        for tok in re.findall(r"'[^']*'|\"[^\"]*\"|[A-Za-z_]+|\d[\d.,]*|\s+|.", ln):
            if tok.startswith(("'", '"')):
                col = LIME
            elif tok in CODE_KW:
                col = VIOLET
            elif tok[0].isdigit():
                col = GOLD
            elif tok.strip() and tok[0].isalpha():
                col = CYAN
            else:
                col = INK2
            xx += text(c, tok, xx, y + i * lh, size, "mono", col, ai, align="left") if tok.strip() else text_w(tok, "mono", size)


def crossed(c, x, y, w, h, a, title, sub, col=ROSE):
    """painel 'não é isso': conteúdo apagado com X"""
    if a <= 0:
        return
    panel(c, x, y, w, h, a, col, glow=False)
    text(c, title, x + w / 2, y + h / 2 - 6, 36, "black", INK2, a)
    text(c, sub, x + w / 2, y + h / 2 + 40, 24, "mono", DIM, a)
    k = ep(1, 0, 1)
    c.drawLine(x + 30, y + 30, x + w - 30, y + h - 30, paint(col, 0.8 * a * k, stroke=5, cap_round=True))
    c.drawLine(x + w - 30, y + 30, x + 30, y + h - 30, paint(col, 0.8 * a * k, stroke=5, cap_round=True))


def toggle(c, x, cy, on, a):
    rrect(c, x, cy - 30, 120, 60, 30, mix("#1A2440", LIME, on), a)
    c.drawCircle(x + 30 + 60 * on, cy, 22, paint(INK, a))


# ======================================================================
def b_hook(c, t, C, B):
    a0 = ep(t, B["start"], 0.6)
    out = 1 - ep(t, C["01.c"], 0.5)
    panel(c, 150, 230, 760, 470, a0 * out, DIM, label="slide 7 de 32")
    if a0 * out > 0:
        text(c, "Resultados do 3º trimestre", 200, 320, 36, "black", INK2, a0 * out, align="left")
        for i, s in enumerate(("Receita: R$ 4,2 mi", "Clientes novos: 312", "Retenção: 94%")):
            text(c, "•  " + s, 200, 400 + i * 60, 30, "mono", DIM, a0 * out, align="left")
        glow_text(c, "0:30", 860, 650, 40, "black", GOLD, a0 * out, align="right", glow=0.3)
    aa = ep(t, C["01.a"], 0.5) * out
    chip(c, "SLIDE PARADO", 530, 770, ROSE, aa, anchor="center", size=28, filled=True)
    ab = ep(t, C["01.b"], 0.5) * out
    if ab > 0:
        panel(c, 990, 230, 780, 470, ab, GOLD, label="editor de vídeo")
        for r in range(5):
            text(c, f"V{r + 1}", 1020, 320 + r * 64, 20, "monob", DIM, ab, align="left")
            for k in range(6):
                w = 40 + 70 * hash01(r * 7 + k, 3)
                xx = 1070 + k * 110 + 20 * hash01(r, k)
                rrect(c, xx, 296 + r * 64, w, 34, 5, (CYAN, VIOLET, MAGENTA, GOLD, LIME)[r], ab * 0.6)
        ph = 1070 + (t * 90) % 660
        c.drawLine(ph, 280, ph, 620, paint(ROSE, ab, stroke=2))
        chip(c, "HORAS DE TRABALHO", 1380, 770, GOLD, ep(t, C["01.b"] + 1.2, 0.5) * out, anchor="center", size=28,
             filled=True)
    ac = ep(t, C["01.c"], 0.6)
    if ac > 0:
        bubble(c, 150, 260, 640, 160, ac)
        text(c, "Anime o meu relatório.", 200, 360, 44, "black", INK, ac, align="left")
        glow_line(c, 800, 340, 930, 340, MAGENTA, ac, 3, progress=ep(t, C["01.c"] + 0.3, 0.6))
        preview(c, 950, 230, 820, 560, t, ep(t, C["01.c"] + 0.5, 0.5))


def b_intro(c, t, C, B):
    a0 = ep(t, C["02.a"], 0.6)
    cx = W / 2
    chip(c, "ANTHROPIC", cx, 250, DIM, a0, anchor="center", size=26)
    glow_text(c, "Claude", cx, 420, 160, "black", INK, a0, glow=0.0)
    # 'Motion' com rastro de movimento
    for k in range(4, 0, -1):
        glow_text(c, "Motion", cx - k * 26 * (0.6 + 0.4 * math.sin(t * 2)), 590, 160, "black", MAGENTA, a0 * 0.10 * (5 - k),
                  glow=0.0)
    glow_text(c, "Motion", cx, 590, 160, "black", MAGENTA, a0, glow=0.6)
    ab = ep(t, C["02.b"], 0.5)
    chip(c, "08/10/2026", cx - 330, 700, INK2, ab, anchor="center", size=28)
    chip(c, "BETA", cx - 90, 700, GOLD, ep(t, C["02.b"] + 0.8, 0.5), anchor="center", size=28, filled=True)
    chip(c, "+ CLAUDE DASHBOARDS", cx + 230, 700, CYAN, ep(t, C["02.b"] + 1.8, 0.5), anchor="center", size=26)
    ac = ep(t, C["02.c"], 0.5)
    chip(c, "ANIMAÇÕES CURTAS", cx - 180, 800, MAGENTA, ac, anchor="center", size=28)
    chip(c, "animacao.mp4", cx + 180, 800, LIME, ep(t, C["02.d"], 0.5), anchor="center", size=28, filled=True)


def b_mapa(c, t, C, B):
    head(c, t, B["start"], "ROTEIRO", "NESTE VÍDEO", MAGENTA)
    items = [("03.a", "O SEGREDO", "código, não vídeo", MAGENTA), ("03.b", "O QUE FAZ", "3 exemplos oficiais", CYAN),
             ("03.c", "CRIAR", "/motion e prompt", VIOLET), ("03.d", "EDITAR E EXPORTAR", "chat · editor · MP4", CYAN),
             ("03.e", "QUEM PODE USAR", "Team · Enterprise", LIME), ("03.f", "LIMITES", "o que saber antes", ROSE)]
    for k, (cue, t1, t2, col) in enumerate(items):
        a, dy = reveal(t, C[cue])
        if a <= 0:
            continue
        x = 150 + (k % 3) * 550
        y = 260 + (k // 3) * 290 + dy
        panel(c, x, y, 500, 230, a, col)
        glow_text(c, f"0{k + 1}", x + 40, y + 90, 60, "black", col, a, align="left", glow=0.4)
        text(c, t1, x + 40, y + 155, 38 if len(t1) < 14 else 34, "black", INK, a, align="left")
        text(c, t2, x + 40, y + 198, 26, "mono", INK2, a, align="left")


def b_segredo(c, t, C, B):
    head(c, t, B["start"], "O SEGREDO", "NÃO É UM MODELO DE VÍDEO", MAGENTA)
    aa = ep(t, C["04.a"], 0.5) * (1 - ep(t, C["04.b"], 0.5))
    crossed(c, 560, 300, 800, 380, aa, "MODELO DE VÍDEO", "gera pixels do zero")
    ab, dyb = reveal(t, C["04.b"])
    if ab > 0:
        panel(c, 150, 240 + dyb, 860, 460, ab, VIOLET, label="animacao.js")
        code(c, ["scene(1, duration=3)",
                 "  text('Receita: R$ 4,2 mi').fade_in()",
                 "  bar_chart(dados_q3).grow()",
                 "scene(2, duration=4)",
                 "  image('logo.png').move(at=0.5)"], 190, 330 + dyb, 28, t, C["04.b"] + 0.3, ab, step=0.3)
    acs = ep(t, C["04.c"], 0.5)
    if acs > 0:
        x = 150
        for k, s in enumerate(("seu texto", "seus gráficos", "formas", "imagens")):
            x = chip(c, s, x, 760, CYAN, ep(t, C["04.c"] + 0.45 * k, 0.4), size=26)[1] + 24
    ad = ep(t, C["04.d"], 0.5)
    if ad > 0:
        link(c, 1015, 470, 1080, 470, MAGENTA, ad, t, pulses=1)
        preview(c, 1090, 240, 680, 460, t, ad, label="roda como vídeo")


def b_semfake(c, t, C, B):
    head(c, t, B["start"], "CONSEQUÊNCIA", "SÓ O SEU CONTEÚDO", LIME)
    crossed(c, 150, 260, 520, 230, ep(t, C["05.a"], 0.5), "FILMAGEM GERADA", "cenas inventadas")
    ab = ep(t, C["05.b"], 0.5)
    if ab > 0:
        crossed(c, 150, 540, 520, 230, ab, "", "")
        c.drawCircle(410, 610, 34, paint(INK2, 0.5 * ab, stroke=3))
        p = skia.Path(); p.addArc(skia.Rect.MakeXYWH(350, 650, 120, 90), 180, 180)
        c.drawPath(p, paint(INK2, 0.5 * ab, stroke=3))
        text(c, "PESSOAS CRIADAS POR IA", 410, 745, 26, "black", INK2, ab)
    ac, dyc = reveal(t, C["05.c"])
    if ac > 0:
        preview(c, 740, 260 + dyc, 1030, 510, t, ac, LIME, "seu conteúdo, em movimento")
    ad = ep(t, C["05.d"], 0.5)
    chip(c, "NADA DE CENA INVENTADA", 1255, 830, LIME, ad, anchor="center", size=28, filled=True)


def b_codigo(c, t, C, B):
    head(c, t, B["start"], "A VANTAGEM", "EDITAR SEM REFAZER", CYAN)
    aa, dya = reveal(t, C["06.a"])
    sw = ep(t, C["06.b"] + 0.8, 0.4)
    if aa > 0:
        panel(c, 150, 240 + dya, 900, 400, aa, CYAN, label="cena_1")
        num = "4,8" if sw > 0.5 else "4,2"
        code(c, [f"text = 'Receita: R$ {num} mi'", "duration = 3.0", "x = 120   y = 300", "color = '#22D3EE'"],
             190, 330 + dya, 32, t, C["06.a"] + 0.3, aa, step=0.3, hi_line=0 if t >= C["06.b"] else None)
    ab = ep(t, C["06.b"], 0.5)
    if ab > 0:
        chip(c, "TROCA SÓ O NÚMERO", 600, 700, GOLD, ab, anchor="center", size=26, filled=True)
    ac = ep(t, C["06.c"], 0.5)
    if ac > 0:
        for i in range(1, 4):
            ai = ep(t, C["06.c"] + 0.3 * i, 0.4)
            check_icon(c, 1000, 330 + i * 48 + dya - 12, 14, ai, LIME)
        chip(c, "O RESTO FICA IGUAL", 600, 790, LIME, ac, anchor="center", size=26)
    ad, dyd = reveal(t, C["06.d"])
    if ad > 0:
        panel(c, 1110, 240 + dyd, 660, 400, ad, ROSE, label="vídeo gerado por IA")
        for k in range(9):
            jx = 6 * math.sin(t * 7 + k * 2) * ad
            col = (ROSE, GOLD, VIOLET)[(k + int(t * 3)) % 3]
            rrect(c, 1150 + (k % 3) * 200 + jx, 300 + (k // 3) * 105 + dyd, 180, 90, 8, col, ad * 0.35)
        text(c, "uma mudança → cena inteira muda", 1440, 700, 26, "mono", ROSE, ad)


def b_meta(c, t, C, B):
    head(c, t, B["start"], "CURIOSIDADE", "ESTE VÍDEO É CÓDIGO", VIOLET)
    aa, dya = reveal(t, C["07.a"])
    if aa > 0:
        panel(c, 150, 240 + dya, 900, 480, aa, VIOLET, label="visual.py")
        code(c, ["def b_meta(c, t):",
                 "  panel(c, 150, 240, 900, 480)",
                 "  bars(c, 1180, 400, dados)",
                 "  caption(c, cena, t)",
                 "for quadro in range(9000):",
                 "  desenha(quadro / 30)"], 190, 330 + dya, 28, t, C["07.a"] + 0.2, aa, step=0.25)
    ab = ep(t, C["07.b"], 0.5)
    if ab > 0:
        # moldura de 'wireframe' sobre os elementos da tela
        for (x, y, w, h, lab) in ((1120, 250, 650, 300, "panel()"), (1160, 330, 570, 180, "bars()"), (300, 920, 1320, 80, "caption()")):
            p = paint(GOLD, 0.8 * ab, stroke=2)
            p.setPathEffect(skia.DashPathEffect.Make([10, 8], -t * 40))
            c.drawRect(skia.Rect.MakeXYWH(x, y, w, h), p)
            text(c, lab, x + 8, y - 10, 20, "monob", GOLD, ab, align="left")
        panel(c, 1120, 250, 650, 300, ab, CYAN, glow=False)
        bars(c, 1160, 330, 570, 180, [0.4, 0.62, 0.5, 0.85], CYAN, ab, prog(t, C["07.b"], 1.2), hi=LIME)
        text(c, "QUADRO", 1120, 640, 24, "monob", DIM, ab, align="left")
        glow_text(c, f"{int(t * 30):,}".replace(",", "."), 1120, 720, 70, "black", GOLD, ab, align="left", glow=0.3)
        text(c, "30 por segundo", 1460, 710, 26, "mono", INK2, ab, align="left")
    ac = ep(t, C["07.c"], 0.5)
    chip(c, "MOTION = ISSO, SEM PROGRAMAR", 600, 790, MAGENTA, ac, anchor="center", size=28, filled=True)


def b_exemplos(c, t, C, B):
    head(c, t, B["start"], "O QUE DÁ PARA FAZER", "3 EXEMPLOS OFICIAIS", CYAN)
    cards = [("08.a", "RELATÓRIO → 30 s", "explicador do trimestre", CYAN), ("08.b", "GRÁFICO DO DECK", "reunião do conselho", VIOLET),
             ("08.c", "BOAS-VINDAS", "passo a passo p/ clientes", LIME)]
    for k, (cue, t1, t2, col) in enumerate(cards):
        a, dy = reveal(t, C[cue])
        if a <= 0:
            continue
        x = 150 + k * 550
        y = 250 + dy
        panel(c, x, y, 500, 580, a, col, label=f"0{k + 1}")
        text(c, t1, x + 250, y + 90, 34, "black", INK, a)
        text(c, t2, x + 250, y + 135, 24, "mono", INK2, a)
        u = loop(t - C[cue], 4.0)
        if k == 0:
            n = 4.2 * ease_out(clamp(u * 2.5))
            glow_text(c, f"R$ {n:.1f} mi".replace(".", ","), x + 250, y + 300, 62, "black", CYAN, a, glow=0.3)
            bar_meter(c, x + 60, y + 360, 380, 14, clamp(u * 2.5), CYAN, a)
            glow_text(c, "0:30", x + 250, y + 490, 44, "black", GOLD, a, glow=0.2)
        elif k == 1:
            linechart(c, x + 50, y + 200, 400, 260, [0.2, 0.35, 0.3, 0.5, 0.48, 0.7, 0.9], VIOLET, a, progress=clamp(u * 1.6))
            line(c, x + 50, y + 460, x + 450, y + 460, DIM, a, 1.5)
        else:
            for i, s in enumerate(("crie a conta", "conecte os dados", "convide a equipe")):
                ai = ep(u * 4, 0.3 + i * 0.8, 0.4) * a
                rrect(c, x + 50, y + 210 + i * 110, 400, 84, 10, "#0E1830", a)
                glow_text(c, str(i + 1), x + 95, y + 268 + i * 110, 40, "black", LIME, a, glow=0.3)
                text(c, s, x + 140, y + 264 + i * 110, 28, "semibold", INK, a, align="left")
                check_icon(c, x + 410, y + 252 + i * 110, 16, ai, LIME)


def b_comecar(c, t, C, B):
    head(c, t, B["start"], "COMO CRIAR", "TRÊS CAMINHOS", VIOLET)
    cards = [("09.a", "PEDIR NO CHAT", "ou digitar /motion", MAGENTA), ("09.b", "OUTPUT → MOTION", "na caixa de mensagem", VIOLET),
             ("09.c", "ABA ARTIFACTS", "modelo de Motion", CYAN)]
    for k, (cue, t1, t2, col) in enumerate(cards):
        a, dy = reveal(t, C[cue])
        if a <= 0:
            continue
        x = 150 + k * 550
        y = 260 + dy
        panel(c, x, y, 500, 560, a, col, label=f"0{k + 1}")
        text(c, t1, x + 250, y + 90, 32, "black", INK, a)
        text(c, t2, x + 250, y + 135, 24, "mono", INK2, a)
        bx, by = x + 40, y + 190
        if k == 0:
            rrect(c, bx, by, 420, 74, 10, "#0E1830", a, stroke=1.5, stroke_color=MAGENTA)
            typed(c, "/motion", bx + 24, by + 48, 32, t, C[cue] + 0.6, cps=8, col=MAGENTA, peso="monob", a=a)
            for i, s in enumerate(("/motion", "/dashboards")):
                ai = ep(t, C[cue] + 1.4, 0.3) * a
                rrect(c, bx, by + 100 + i * 64, 420, 56, 8, MAGENTA if i == 0 else "#0E1830", ai)
                text(c, s, bx + 24, by + 138 + i * 64, 26, "monob", "#03050B" if i == 0 else INK2, ai, align="left")
        elif k == 1:
            rrect(c, bx, by, 420, 70, 10, "#0E1830", a, stroke=1.5, stroke_color=DIM)
            text(c, "Pergunte algo...", bx + 24, by + 46, 26, "mono", DIM, a, align="left")
            chip(c, "Output", bx + 400, by + 35, VIOLET, a, anchor="right", size=22, filled=True, peso="bold")
            menu = ep(t, C[cue] + 0.6, 0.4)
            for i, s in enumerate(("Docs", "Slides", "Dashboards", "Motion")):
                on = i == 3 and t > C[cue] + 1.3
                yy = by + 110 + i * 62
                rrect(c, bx + 160, yy, 260, 54, 8, VIOLET if on else "#0E1830", a * menu)
                text(c, s, bx + 185, yy + 37, 26, "bold", "#03050B" if on else INK2, a * menu, align="left")
        else:
            for i, s in enumerate(("Explicador animado", "Gráfico em movimento", "Passo a passo")):
                aa = ep(t, C[cue] + 0.5 + 0.3 * i, 0.4) * a
                yy = by + i * 110
                panel(c, bx, yy, 420, 90, aa, CYAN if i == 0 else DIM, k=12, glow=False)
                text(c, s, bx + 30, yy + 56, 28, "semibold", INK, aa, align="left")


def b_prompt(c, t, C, B):
    head(c, t, B["start"], "DICA OFICIAL", "COMO PEDIR BEM", GOLD)
    items = [("10.a", "QUEM", "vai assistir?", CYAN, "?"), ("10.b", "ONDE", "vai passar?", VIOLET, "@"),
             ("10.c", "QUANTO", "tempo dura?", MAGENTA, "30s")]
    xs = [330, 960, 1590]
    for k, (cue, lab, sub, col, g) in enumerate(items):
        a = ep(t, C[cue], 0.5)
        if a <= 0:
            continue
        node(c, xs[k], 400, 105, lab, sub, col, a, t, glyph=g, gsize=70 if len(g) == 1 else 50)
    ad = ep(t, C["10.d"], 0.5)
    if ad > 0:
        panel(c, 150, 660, 1620, 170, ad, LIME, label="anexos")
        for k, s in enumerate(("relatorio_q3.pdf", "dados_vendas.xlsx", "logo.png")):
            chip(c, "+ " + s, 210 + k * 520, 745, LIME, ep(t, C["10.d"] + 0.6 + 0.4 * k, 0.4), size=28, filled=k == 0)


def b_pedido(c, t, C, B):
    head(c, t, B["start"], "NA PRÁTICA", "UM PEDIDO DE VERDADE", MAGENTA)
    aa = ep(t, C["11.a"] - 0.3, 0.5)
    bubble(c, 150, 230, 1620, 170, aa)
    if aa > 0:
        typed(c, "Crie uma animação de 30 segundos para a reunião geral da empresa,", 190, 305, 32, t, C["11.a"],
              cps=30, col=INK, peso="semibold", cursor=False)
        typed(c, "mostrando os 3 principais números do relatório em anexo.", 190, 355, 32, t, C["11.b"], cps=30,
              col=INK, peso="semibold")
        chip(c, "+ relatorio_q3.pdf", 1740, 230, LIME, ep(t, C["11.b"] + 1.0, 0.4), anchor="right", size=20, filled=True)
    acs = ep(t, C["11.c"], 0.5)
    if acs > 0:
        text(c, "CENAS", 150, 470, 24, "monob", DIM, acs, align="left")
        for k, (s, col) in enumerate((("Receita", CYAN), ("Clientes", VIOLET), ("Retenção", LIME))):
            a = ep(t, C["11.c"] + 0.35 * k, 0.4)
            panel(c, 150 + k * 190, 500, 170, 110, a, col, k=10, glow=False)
            text(c, f"0{k + 1}", 170 + k * 190, 540, 20, "monob", col, a, align="left")
            text(c, s, 170 + k * 190, 590, 26, "bold", INK, a, align="left")
    ad, dyd = reveal(t, C["11.d"])
    if ad > 0:
        panel(c, 150, 650 + dyd, 550, 190, ad, VIOLET, k=14, label="código")
        code(c, ["scene(1, duration=10)", "  text('Receita').fade_in()"], 180, 730 + dyd, 26, t, C["11.d"] + 0.2, ad)
    ae = ep(t, C["11.e"], 0.5)
    if ae > 0:
        preview(c, 760, 460, 1010, 380, t, ae, MAGENTA, "rodando")
        play_icon(c, 1660, 560, 40, MAGENTA, ae * (0.6 + 0.4 * math.sin(t * 3)))


def b_editar(c, t, C, B):
    head(c, t, B["start"], "EDITAR", "PEÇA A MUDANÇA", CYAN)
    sw = ep(t, C["12.c"] + 0.6, 0.4)
    num = "R$ 4,8 mi" if sw > 0.5 else "R$ 4,2 mi"
    preview(c, 150, 230, 760, 420, t, ep(t, B["start"] + 0.3, 0.5), CYAN, "preview", num=num, period=7.0)
    # linha do tempo com 3 cenas; a 2ª estica
    a0 = ep(t, B["start"] + 0.5, 0.5)
    st = ep(t, C["12.b"] + 0.6, 0.8)
    ws = [200, 200 + 140 * st, 200]
    x = 150
    text(c, "LINHA DO TEMPO", 150, 710, 22, "monob", DIM, a0, align="left")
    for k, w in enumerate(ws):
        col = (CYAN, GOLD if st > 0 else VIOLET, LIME)[k]
        rrect(c, x, 740, w - 10, 70, 8, col, a0 * 0.75)
        text(c, f"cena {k + 1}", x + 20, 785, 24, "monob", "#03050B", a0, align="left")
        x += w
    ab = ep(t, C["12.b"], 0.5)
    if ab > 0:
        bubble(c, 980, 230, 790, 120, ab)
        text(c, "Deixe a segunda cena mais lenta.", 1020, 305, 34, "semibold", INK, ab, align="left")
    ac = ep(t, C["12.c"], 0.5)
    if ac > 0:
        bubble(c, 980, 390, 790, 120, ac)
        text(c, "Troque esse número.", 1020, 465, 34, "semibold", INK, ac, align="left")
    ad = ep(t, C["12.d"], 0.5)
    if ad > 0:
        panel(c, 980, 560, 790, 250, ad, VIOLET, label="editor")
        for i, (k, v) in enumerate((("texto", "Receita do trimestre"), ("duração", "3,0 s"), ("cor", "#22D3EE"))):
            text(c, k.upper(), 1020, 640 + i * 52, 22, "monob", DIM, ad, align="left")
            rrect(c, 1200, 612 + i * 52, 520, 40, 6, "#0E1830", ad)
            text(c, v, 1215, 640 + i * 52, 24, "mono", INK, ad, align="left")


def b_exportar(c, t, C, B):
    head(c, t, B["start"], "EXPORTAR", "MP4 E COMPARTILHAR", LIME)
    aa = ep(t, C["13.a"], 0.5)
    if aa > 0:
        chip(c, "Export", 150, 300, LIME, aa, size=32, filled=True, peso="bold")
        m = ep(t, C["13.a"] + 0.6, 0.4)
        rrect(c, 150, 350, 300, 70, 8, LIME, aa * m)
        text(c, "MP4", 180, 397, 30, "black", "#03050B", aa * m, align="left")
        fa = ep(t, C["13.a"] + 1.3, 0.5)
        panel(c, 560, 250, 620, 230, fa, LIME, label="arquivo")
        text(c, "animacao.mp4", 610, 350, 44, "black", INK, fa, align="left")
        bar_meter(c, 610, 400, 520, 14, prog(t, C["13.a"] + 1.5, 1.5), LIME, fa)
        text(c, "pronto para enviar", 610, 455, 24, "mono", INK2, fa, align="left")
    ab = ep(t, C["13.b"], 0.5)
    if ab > 0:
        panel(c, 150, 560, 760, 240, ab, GOLD, label="visibilidade")
        rrect(c, 210, 650, 60, 50, 8, GOLD, ab)
        p = skia.Path(); p.addArc(skia.Rect.MakeXYWH(220, 615, 40, 60), 180, 180)
        c.drawPath(p, paint(GOLD, ab, stroke=6))
        text(c, "PRIVADA", 300, 690, 44, "black", INK, ab, align="left")
        text(c, "só você vê, até compartilhar", 300, 740, 26, "mono", INK2, ab, align="left")
    ac = ep(t, C["13.c"], 0.5)
    if ac > 0:
        panel(c, 990, 560, 780, 240, ac, CYAN, label="Share")
        chip(c, "Share", 1050, 650, CYAN, ac, size=32, filled=True, peso="bold")
        for k in range(3):
            ak = ep(t, C["13.c"] + 0.5 + 0.3 * k, 0.4)
            c.drawCircle(1450 + k * 90, 650, 30, paint((MAGENTA, GOLD, LIME)[k], ak))
            link(c, 1200, 650, 1415 + k * 90, 650, CYAN, ak, t, pulses=1) if k == 0 else None
        text(c, "com quem você escolher", 1050, 740, 26, "mono", INK2, ac, align="left")


def b_levar(c, t, C, B):
    head(c, t, B["start"], "ACABAMENTO", "CONTINUE EM OUTRAS FERRAMENTAS", MAGENTA)
    a0 = ep(t, B["start"] + 0.3, 0.5)
    preview(c, 150, 260, 620, 440, t, a0, MAGENTA, "animacao.mp4")
    tools = ["Adobe", "Descript", "HeyGen", "Higgsfield", "invideo", "Luma AI", "Runway"]
    for k, s in enumerate(tools):
        cue = f"14.a{k + 1}"
        a = ep(t, C[cue], 0.4)
        col_x = 1000 + (k % 2) * 400
        y = 290 + (k // 2) * 105
        if k % 2 == 0:
            link(c, 780, 480, col_x - 10, y, MAGENTA, a, t, progress=ep(t, C[cue], 0.4), pulses=1)
        chip(c, s, col_x, y, MAGENTA, a, size=32, filled=True, peso="bold")
    ab = ep(t, C["14.b"], 0.5)
    if ab > 0:
        text(c, "EM BREVE", 150, 830, 26, "monob", GOLD, ab, align="left")
        chip(c, "Canva", 330, 820, GOLD, ep(t, C["14.b"], 0.4), size=28, peso="bold")
        chip(c, "Captions", 500, 820, GOLD, ep(t, C["14.b"] + 0.4, 0.4), size=28, peso="bold")


def b_planos(c, t, C, B):
    head(c, t, B["start"], "QUEM PODE USAR", "SÓ TEAM E ENTERPRISE", GOLD)
    aa = ep(t, C["15.a"], 0.5)
    chip(c, "BETA", 150, 270, GOLD, aa, size=28, filled=True)
    plans = [("Free", False), ("Pro", False), ("Max", False), ("Team", True), ("Enterprise", True)]
    for k, (s, ok) in enumerate(plans):
        cue = C["15.a"] + 0.3 * (k - 3) if ok else C["15.b"] + 0.4 * k
        a, dy = reveal(t, cue)
        if a <= 0:
            continue
        x = 150 + k * 330
        panel(c, x, 330 + dy, 300, 150, a, LIME if ok else DIM, k=14, glow=ok)
        glow_text(c, s, x + 150, 420 + dy, 44, "black", INK if ok else DIM, a, glow=0.12 if ok else 0)
        if not ok:
            check_icon(c, x + 265, 360 + dy, 14, a, ROSE, "x")
    ac, dyc = reveal(t, C["15.c"])
    if ac > 0:
        panel(c, 150, 560 + dyc, 760, 250, ac, LIME, label="Team")
        text(c, "já vem ligado", 200, 680 + dyc, 40, "black", INK, ac, align="left")
        toggle(c, 740, 670 + dyc, 1.0, ac)
    ad, dyd = reveal(t, C["15.d"])
    if ad > 0:
        on = ep(t, C["15.d"] + 3.5, 0.4)
        panel(c, 990, 560 + dyd, 780, 250, ad, GOLD, label="Enterprise")
        text(c, "Organização › Artifacts › Motion", 1040, 650 + dyd, 30, "monob", INK, ad, align="left")
        text(c, "o administrador ativa", 1040, 730 + dyd, 28, "mono", INK2, ad, align="left")
        toggle(c, 1600, 720 + dyd, on, ad)


def b_uso(c, t, C, B):
    head(c, t, B["start"], "CUSTO", "CONTA NO LIMITE DE USO", GOLD)
    aa = ep(t, C["16.a"], 0.5)
    if aa > 0:
        chip(c, "SEM COBRANÇA SEPARADA", 150, 280, LIME, ep(t, B["start"] + 0.5, 0.5), size=26)
        panel(c, 150, 350, 1620, 160, aa, GOLD, label="limite do plano")
        bar_meter(c, 200, 440, 1520, 22, 0.15 + 0.5 * ep(t, C["16.b"] + 1.0, 1.5), GOLD, aa)
    ab = ep(t, C["16.b"], 0.5)
    if ab > 0:
        for k, (lab, w, cost, col) in enumerate((("curta · simples", 260, "consome menos", LIME),
                                                 ("longa · complexa", 900, "consome mais", ROSE))):
            a = ep(t, C["16.b"] + 0.8 * k, 0.5)
            y = 600 + k * 120
            text(c, lab.upper(), 150, y + 48, 24, "monob", DIM, a, align="left")
            rrect(c, 520, y, w * ep(t, C["16.b"] + 0.8 * k, 0.8), 70, 8, col, a * 0.8)
            text(c, cost, 540 + w, y + 46, 28, "mono", col, a, align="left")


def b_limites(c, t, C, B):
    head(c, t, B["start"], "LIMITES", "O QUE SABER ANTES", ROSE)
    aa = ep(t, C["17.a"], 0.5)
    if aa > 0:
        chip(c, "01 · BETA", 1060, 150, GOLD, aa, size=26, filled=True)
        text(c, "desempenho pode variar", 1260, 160, 26, "mono", INK2, aa, align="left")
    ab, dyb = reveal(t, C["17.b"])
    if ab > 0:
        panel(c, 150, 250 + dyb, 640, 470, ab, CYAN, label="02 · duração")
        check_icon(c, 220, 380 + dyb, 20, ab, LIME)
        text(c, "clipes curtos", 260, 392 + dyb, 38, "black", INK, ab, align="left")
        text(c, "explicadores rápidos", 260, 440 + dyb, 28, "mono", INK2, ab, align="left")
        check_icon(c, 220, 560 + dyb, 20, ep(t, C["17.b"] + 1.2, 0.4), ROSE, "x")
        text(c, "treinamento de 1 hora", 260, 572 + dyb, 34, "bold", INK2, ep(t, C["17.b"] + 1.2, 0.4), align="left")
    ac, dyc = reveal(t, C["17.c"])
    if ac > 0:
        panel(c, 850, 250 + dyc, 920, 470, ac, ROSE, label="03 · explica, mas não confere")
        text(c, "FONTE", 900, 340 + dyc, 22, "monob", DIM, ac, align="left")
        text(c, "relatório: R$ 2,4 mi", 900, 385 + dyc, 32, "mono", INK, ac, align="left")
    ad = ep(t, C["17.d"], 0.5)
    if ad > 0:
        text(c, "ANIMAÇÃO", 900, 470 + dyc, 22, "monob", DIM, ad, align="left")
        u = loop(t, 2.5)
        glow_text(c, "R$ 4,2 mi", 900 + (1 - ep(u * 2.5, 0, 0.5)) * 30, 580 + dyc, 84, "black", ROSE, ad, align="left", glow=0.4)
        chip(c, "NÚMERO ERRADO, BEM ANIMADO", 900, 660 + dyc, ROSE, ad, size=24, filled=True)
    ae = ep(t, C["17.e"], 0.5)
    chip(c, "REVISE TUDO CONTRA A FONTE", W / 2, 800, LIME, ae, anchor="center", size=30, filled=True)


def b_resumo(c, t, C, B):
    head(c, t, B["start"], "RESUMO", "O QUE LEVAR DESTE VÍDEO", MAGENTA)
    panel(c, 150, 220, 1620, 660, ep(t, B["start"] + 0.3, 0.5), MAGENTA, label="README.md")
    rows = [("18.a", "o seu material vira uma animação curta", MAGENTA),
            ("18.b", "não é vídeo gerado por IA: é código animando o seu conteúdo", VIOLET),
            ("18.c", "cada detalhe se edita sem refazer o resto", CYAN),
            ("18.d", "Export → MP4 (começa privado)", LIME),
            ("18.e", "beta nos planos Team e Enterprise", GOLD),
            ("18.f", "regra de ouro: confira os números", ROSE)]
    for k, (cue, s, col) in enumerate(rows):
        a, dy = reveal(t, C[cue], 0.45)
        y = 320 + k * 92 + dy
        glow_text(c, f"0{k + 1}", 220, y, 40, "black", col, a, align="left", glow=0.4)
        text(c, s, 310, y, 36, "bold", INK, a, align="left")


def b_cta(c, t, C, B):
    tech.cta(c, t, C["19.like"], C["19.sub"], C["19.bell"], C["19.com"], C["19.bye"],
             "O que você transformaria em animação?")
    a = ep(t, B["start"], 0.5) * (1 - prog(t, C["19.like"] - 0.4, 0.4))
    if a > 0:
        glow_text(c, "Claude Motion", W / 2, 520, 130, "black", MAGENTA, a, glow=0.7)
        text(c, "beta · Team e Enterprise · /motion", W / 2, 620, 34, "mono", INK2, a)


BLOCKS = dict(hook=b_hook, intro=b_intro, mapa=b_mapa, segredo=b_segredo, semfake=b_semfake, codigo=b_codigo,
              meta=b_meta, exemplos=b_exemplos, comecar=b_comecar, prompt=b_prompt, pedido=b_pedido, editar=b_editar,
              exportar=b_exportar, levar=b_levar, planos=b_planos, uso=b_uso, limites=b_limites, resumo=b_resumo,
              cta=b_cta)
