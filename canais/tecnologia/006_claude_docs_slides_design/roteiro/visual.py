"""Visual do vídeo Tecnologia 006 — Claude Docs, Slides e Design. Tema 'tech' (futurista)."""
import math
import skia
import motor
import tech
from motor import *  # noqa
from tech import *  # noqa

tech.SERIE = "TECH//006 · DOCS · SLIDES · DESIGN"
MARCA = ""
ARQUIVO_FINAL = "tecnologia_006_claude_docs_slides_design.mp4"
BACKGROUND, CAPTION, OVERLAY = tech.background, tech.caption, tech.overlay

DOC, SLD, DSG = CYAN, GOLD, MAGENTA


# ---------------- maquetes ----------------
def doc_mock(c, x, y, w, h, a, col=DOC, lines=9, grow=1.0, hi=None, hi_col=GOLD, title="Relatório semanal"):
    """página de documento: título + linhas de texto"""
    if a <= 0:
        return
    rrect(c, x, y, w, h, 10, "#E8EEF8", a)
    text(c, title, x + 36, y + 62, 30, "black", "#0B1430", a, align="left")
    c.drawRect(skia.Rect.MakeXYWH(x + 36, y + 80, 80, 5), paint(col, a))
    n = int(lines * clamp(grow) + 0.999)
    for i in range(n):
        ww = (w - 72) * (0.95 - 0.25 * hash01(i, 7))
        yy = y + 120 + i * 34
        if yy > y + h - 30:
            break
        if hi is not None and i == hi:
            rrect(c, x + 30, yy - 8, ww + 12, 28, 4, hi_col, 0.45 * a)
        rrect(c, x + 36, yy, ww, 12, 6, "#9AA8C0", a)


def slide_mock(c, x, y, w, a, col=SLD, title="Resultados da semana", vals=(0.4, 0.62, 0.5, 0.85), kind=0):
    """slide 16:9 com título e um gráfico simples"""
    if a <= 0:
        return
    h = w * 9 / 16
    rrect(c, x, y, w, h, 8, "#0F1A33", a, stroke=2, stroke_color=col)
    s = w / 640
    text(c, title, x + 30 * s, y + 60 * s, 30 * s, "black", INK, a, align="left")
    c.drawRect(skia.Rect.MakeXYWH(x + 30 * s, y + 76 * s, 60 * s, 5 * s), paint(col, a))
    if kind == 0:
        bw = (w - 120 * s) / len(vals)
        for i, v in enumerate(vals):
            bh = (h - 150 * s) * v
            rrect(c, x + 60 * s + i * bw + bw * 0.15, y + h - 40 * s - bh, bw * 0.7, bh, 4, col if i == len(vals) - 1 else "#5B6B8C", a)
    else:
        for i in range(3):
            c.drawCircle(x + 50 * s, y + (130 + i * 60) * s, 7 * s, paint(col, a))
            rrect(c, x + 70 * s, y + (124 + i * 60) * s, (380 - 60 * i) * s, 12 * s, 6 * s, "#5B6B8C", a)
    return h


def design_mock(c, x, y, w, h, a, t=0.0, brand=(MAGENTA, VIOLET), move=0.0, title="LANÇAMENTO"):
    """canvas de design: um 'pôster' com formas e título"""
    if a <= 0:
        return
    rrect(c, x, y, w, h, 10, "#0C1326", a, stroke=2, stroke_color=brand[0])
    c.drawCircle(x + w * 0.72, y + h * 0.32, h * 0.2, paint(brand[1], 0.85 * a))
    rrect(c, x + w * 0.1 + move * 60, y + h * 0.55, w * 0.42, h * 0.12, 8, brand[0], a)
    text(c, title, x + w * 0.1, y + h * 0.36, h * 0.11, "black", INK, a, align="left")
    text(c, "dia 20 · 19h", x + w * 0.1, y + h * 0.84, h * 0.06, "monob", brand[0], a, align="left")


def card3(c, x, y, w, h, title, sub, col, a, label=None):
    panel(c, x, y, w, h, a, col, label=label)
    text(c, title, x + w / 2, y + 80, 34, "black", INK, a)
    if sub:
        text(c, sub, x + w / 2, y + 122, 24, "mono", INK2, a)


def phone(c, cx, cy, a, col=CYAN, content=None):
    if a <= 0:
        return
    w, h = 220, 420
    rrect(c, cx - w / 2, cy - h / 2, w, h, 30, "#060B16", a, stroke=3, stroke_color=col)
    rrect(c, cx - 40, cy - h / 2 + 14, 80, 10, 5, "#1A2440", a)
    if content == "doc":
        doc_mock(c, cx - w / 2 + 16, cy - h / 2 + 40, w - 32, h - 70, a, lines=8, title="Relatório")
    elif content == "slide":
        slide_mock(c, cx - w / 2 + 14, cy - 60, w - 28, a)


def bubble(c, x, y, w, h, a, col=VIOLET, who="você"):
    panel(c, x, y, w, h, a, col, k=16, label=who)


# ======================================================================
def b_hook(c, t, C, B):
    merge = ep(t, C["01.d"], 0.7)
    apps = [(B["start"] + 0.2, "Editor de texto", DOC, 0), (C["01.a"], "Apresentações", SLD, 1), (C["01.b"], "Design", DSG, 2)]
    for t0, name, col, k in apps:
        a = ep(t, t0, 0.5) * (1 - merge)
        if a <= 0:
            continue
        x = 150 + k * 560
        panel(c, x, 250, 500, 470, a, col, label=name.lower())
        if k == 0:
            doc_mock(c, x + 40, 300, 420, 380, a, lines=8)
        elif k == 1:
            slide_mock(c, x + 30, 340, 440, a)
        else:
            design_mock(c, x + 40, 300, 420, 380, a, t)
    ac = ep(t, C["01.c"], 0.5) * (1 - merge)
    if ac > 0:
        for k in range(2):
            x0 = 650 + k * 560
            arrow(c, x0 - 10, 480, x0 + 70, 480, ROSE, ac, 4, 14)
            text(c, "copiar · colar", x0 + 30, 450, 18, "mono", ROSE, ac)
        chip(c, "3 PROGRAMAS · 3 ARQUIVOS", W / 2, 800, ROSE, ac, anchor="center", size=30, filled=True)
    if merge > 0:
        bubble(c, 560, 220, 800, 140, merge)
        text(c, "Uma conversa só.", 610, 310, 48, "black", INK, merge, align="left")
        for k, (s, col) in enumerate((("Docs", DOC), ("Slides", SLD), ("Design", DSG))):
            ak = ep(t, C["01.d"] + 0.5 + 0.3 * k, 0.4)
            x = 380 + k * 420
            link(c, 960, 365, x + 180, 470, col, ak, t, pulses=1)
            card3(c, x, 480, 360, 300, s, None, col, ak)
            if k == 0:
                doc_mock(c, x + 60, 580, 240, 180, ak, lines=4, title="Doc")
            elif k == 1:
                slide_mock(c, x + 40, 590, 280, ak)
            else:
                design_mock(c, x + 60, 580, 240, 180, ak, t)


def b_intro(c, t, C, B):
    a0 = ep(t, C["02.a"], 0.6)
    names = [("Docs", DOC), ("Slides", SLD), ("Design", DSG)]
    for k, (s, col) in enumerate(names):
        a = ep(t, C["02.a"] + 0.4 * k, 0.5)
        x = 480 + k * 480
        text(c, "Claude", x, 330, 44, "black", INK2, a)
        glow_text(c, s, x, 440, 110, "black", col, a, glow=0.6)
    ab = ep(t, C["02.b"], 0.5)
    chip(c, "BETA · 16/09/2026", W / 2 - 230, 580, INK2, ab, anchor="center", size=28)
    ac = ep(t, C["02.c"], 0.5)
    chip(c, "SEM BETA · 08/10/2026", W / 2 + 230, 580, LIME, ac, anchor="center", size=28, filled=True)
    chip(c, "TODOS OS PLANOS, INCLUSIVE O GRATUITO", W / 2, 670, LIME, ep(t, C["02.c"] + 1.2, 0.5), anchor="center", size=26)
    ad = ep(t, C["02.d"], 0.5)
    if ad > 0:
        n = int(45_000_000 * ease_out(prog(t, C["02.d"], 2.2)))
        glow_text(c, f"{n:,}+".replace(",", "."), W / 2, 820, 80, "black", GOLD, ad, glow=0.4)
        text(c, "documentos, apresentações e designs", W / 2, 870, 26, "mono", INK2, ad)


def b_mapa(c, t, C, B):
    head(c, t, B["start"], "ROTEIRO", "NESTE VÍDEO", VIOLET)
    items = [("03.a", "ARTIFACTS", "o que são", VIOLET), ("03.b", "DOCS", "escrever junto", DOC),
             ("03.c", "SLIDES", "montar e apresentar", SLD), ("03.d", "DESIGN", "visuais e marca", DSG),
             ("03.e", "EXEMPLO", "os três juntos", LIME), ("03.f", "SITE ANTIGO", "o que muda", ROSE)]
    for k, (cue, t1, t2, col) in enumerate(items):
        a, dy = reveal(t, C[cue])
        if a <= 0:
            continue
        x = 150 + (k % 3) * 550
        y = 260 + (k // 3) * 290 + dy
        panel(c, x, y, 500, 230, a, col)
        glow_text(c, f"0{k + 1}", x + 40, y + 90, 60, "black", col, a, align="left", glow=0.4)
        text(c, t1, x + 40, y + 155, 38, "black", INK, a, align="left")
        text(c, t2, x + 40, y + 198, 26, "mono", INK2, a, align="left")


def b_artifact(c, t, C, B):
    head(c, t, B["start"], "O CONCEITO", "O QUE É UM ARTIFACT", VIOLET)
    aa = ep(t, C["04.a"], 0.5)
    if aa > 0:
        text(c, "“Tudo o que o Claude cria e que você", 150, 280, 34, "semibold", INK, aa, align="left")
        text(c, "colocaria na frente de alguém.”", 150, 330, 34, "semibold", INK, aa, align="left")
    tiles = [("04.b1", "documento", DOC), ("04.b2", "apresentação", SLD), ("04.b3", "design", DSG), ("04.b4", "painel", LIME)]
    for k, (cue, s, col) in enumerate(tiles):
        a, dy = reveal(t, C[cue], 0.4)
        if a <= 0:
            continue
        x = 150 + k * 290
        panel(c, x, 400 + dy, 260, 300, a, col, k=14)
        if k == 0:
            doc_mock(c, x + 30, 430 + dy, 200, 200, a, lines=5, title="Doc")
        elif k == 1:
            slide_mock(c, x + 20, 460 + dy, 220, a)
        elif k == 2:
            design_mock(c, x + 30, 430 + dy, 200, 200, a, t)
        else:
            for i, v in enumerate((0.4, 0.7, 0.55, 0.9)):
                rrect(c, x + 45 + i * 45, 620 + dy - 150 * v, 30, 150 * v, 4, col, a)
        text(c, s, x + 130, 680 + dy, 26, "monob", col, a)
    ac = ep(t, C["04.c"], 0.5)
    if ac > 0:
        panel(c, 1360, 250, 410, 450, ac, VIOLET, label="barra lateral")
        text(c, "Artifacts", 1400, 330, 32, "black", INK, ac, align="left")
        for i, (s, col) in enumerate((("Relatório semanal", DOC), ("Deck do trimestre", SLD), ("Post de lançamento", DSG),
                                      ("Painel de vendas", LIME))):
            rrect(c, 1400, 360 + i * 74, 330, 58, 8, "#0E1830", ac)
            c.drawCircle(1424, 389 + i * 74, 8, paint(col, ac))
            text(c, s, 1445, 398 + i * 74, 24, "semibold", INK, ac, align="left")
    ad = ep(t, C["04.d"], 0.5)
    chip(c, "COMEÇA PRIVADO", 1565, 770, GOLD, ad, anchor="center", size=28, filled=True)


def b_comecar(c, t, C, B):
    head(c, t, B["start"], "COMO COMEÇAR", "TRÊS CAMINHOS", LIME)
    cards = [("05.a", "PEDIR NO CHAT", "em qualquer conversa", VIOLET), ("05.b", "OUTPUT → MODELO", "na caixa de mensagem", CYAN),
             ("05.c", "ABA ARTIFACTS", "escolha o modelo", MAGENTA)]
    for k, (cue, t1, t2, col) in enumerate(cards):
        a, dy = reveal(t, C[cue])
        if a <= 0:
            continue
        x = 150 + k * 550
        y = 250 + dy
        panel(c, x, y, 500, 580, a, col, label=f"0{k + 1}")
        text(c, t1, x + 250, y + 90, 32, "black", INK, a)
        text(c, t2, x + 250, y + 135, 24, "mono", INK2, a)
        bx, by = x + 40, y + 190
        if k == 0:
            panel(c, bx, by, 420, 120, a, VIOLET, k=12, glow=False)
            text(c, "Monte uma apresentação", bx + 24, by + 52, 26, "semibold", INK, a, align="left")
            text(c, "com estes números...", bx + 24, by + 90, 26, "semibold", INK, a, align="left")
            slide_mock(c, bx + 60, by + 160, 300, a * ep(t, C[cue] + 0.8, 0.5))
        elif k == 1:
            rrect(c, bx, by, 420, 66, 10, "#0E1830", a, stroke=1.5, stroke_color=DIM)
            text(c, "Pergunte algo...", bx + 24, by + 44, 24, "mono", DIM, a, align="left")
            chip(c, "Output", bx + 400, by + 33, CYAN, a, anchor="right", size=22, filled=True, peso="bold")
            menu = ep(t, C[cue] + 0.6, 0.4)
            items = [("Docs", DOC), ("Slides", SLD), ("Design", DSG), ("Dashboards", LIME), ("Motion", VIOLET)]
            sel = int(max(0, t - C[cue] - 1.0) / 0.7) % 3
            for i, (s, col2) in enumerate(items):
                on = i == sel and t > C[cue] + 1.0
                yy = by + 90 + i * 56
                rrect(c, bx + 160, yy, 260, 48, 8, col2 if on else "#0E1830", a * menu)
                text(c, s, bx + 185, yy + 33, 24, "bold", "#03050B" if on else INK2, a * menu, align="left")
        else:
            for i, (s, col2) in enumerate((("Documento", DOC), ("Apresentação", SLD), ("Design", DSG))):
                aa = ep(t, C[cue] + 0.5 + 0.3 * i, 0.4) * a
                yy = by + i * 110
                panel(c, bx, yy, 420, 90, aa, col2, k=12, glow=False)
                text(c, s, bx + 30, yy + 56, 28, "semibold", INK, aa, align="left")


def b_docs(c, t, C, B):
    head(c, t, B["start"], "CLAUDE DOCS", "ESCREVER JUNTO", DOC)
    aa = ep(t, C["06.a"], 0.5)
    doc_mock(c, 150, 230, 900, 620, aa, lines=14, grow=prog(t, C["06.b"], 4.0) if t >= C["06.b"] else 0.3)
    ae = ep(t, C["06.e"], 0.5)
    if ae > 0:
        for k, (col, name) in enumerate(((GOLD, "Ana"), (LIME, "Bruno"))):
            px = 400 + 300 * k + 60 * math.sin(t * 0.9 + k * 2)
            py = 420 + 140 * k + 30 * math.cos(t * 0.7 + k)
            c.drawRect(skia.Rect.MakeXYWH(px, py - 26, 4, 34), paint(col, ae))
            chip(c, name, px + 2, py - 44, col, ae, size=16, filled=True, peso="bold")
    notes = [("06.b", "Escrevi a seção de resultados.", VIOLET), ("06.c", "Qual é a meta do trimestre?", CYAN),
             ("06.d", "Sugiro um gráfico aqui.", MAGENTA)]
    for k, (cue, s, col) in enumerate(notes):
        a, dy = reveal(t, C[cue], 0.45)
        if a <= 0:
            continue
        y = 260 + k * 180 + dy
        panel(c, 1110, y, 660, 140, a, col, k=14, label="Claude")
        text(c, s, 1150, y + 82, 30, "semibold", INK, a, align="left")


def b_editclaude(c, t, C, B):
    head(c, t, B["start"], "CLAUDE DOCS", "EDITAR COM O CLAUDE", DOC)
    aa = ep(t, B["start"] + 0.3, 0.5)
    done = ep(t, C["07.d"], 0.5)
    hi = ep(t, C["07.a"], 0.4)
    doc_mock(c, 150, 230, 900, 620, aa, lines=14, hi=4 if hi > 0.5 else None, hi_col=LIME if done > 0.5 else GOLD)
    ab = ep(t, C["07.b"], 0.4)
    if ab > 0:
        chip(c, "Editar com o Claude", 700, 340, VIOLET, ab, size=24, filled=True, peso="bold")
    ac = ep(t, C["07.c"], 0.4)
    if ac > 0:
        panel(c, 1110, 300, 660, 160, ac, VIOLET, k=14, label="você")
        typed(c, "Deixe este trecho mais curto.", 1150, 395, 30, t, C["07.c"], cps=26, col=INK, peso="semibold")
    if done > 0:
        panel(c, 1110, 520, 660, 220, done, LIME, k=14, label="resultado")
        text(c, "Mudou só o trecho marcado.", 1150, 610, 30, "bold", LIME, done, align="left")
        text(c, "O resto do texto ficou igual.", 1150, 660, 28, "mono", INK2, done, align="left")


def b_docsshare(c, t, C, B):
    head(c, t, B["start"], "CLAUDE DOCS", "COMPARTILHAR E EXPORTAR", DOC)
    aa, dya = reveal(t, C["08.a"])
    if aa > 0:
        panel(c, 150, 240 + dya, 760, 380, aa, DOC, label="compartilhar")
        for i, (s, col) in enumerate((("ana@empresa.com", GOLD), ("bruno@empresa.com", LIME))):
            c.drawCircle(210, 330 + i * 70 + dya, 20, paint(col, aa))
            text(c, s, 250, 340 + i * 70 + dya, 28, "mono", INK, aa, align="left")
        rrect(c, 190, 470 + dya, 680, 60, 10, "#0E1830", aa)
        text(c, "Toda a organização", 220, 510 + dya, 28, "bold", INK, aa, align="left")
        chip(c, "pode editar", 850, 500 + dya, CYAN, aa, anchor="right", size=20)
    ab = ep(t, C["08.b"], 0.5)
    phone(c, 1100, 450, ab, DOC, "doc")
    ac = ep(t, C["08.c"], 0.5)
    if ac > 0:
        text(c, "EXPORTAR", 150, 700, 24, "monob", DIM, ac, align="left")
        x = 150
        for cue, s in (("08.c1", "Word"), ("08.c2", "PDF"), ("08.c3", "Markdown"), ("08.c4", "Google Docs")):
            x = chip(c, s, x, 770, DOC, ep(t, C[cue], 0.4), size=30, filled=True, peso="bold")[1] + 24


def b_slides(c, t, C, B):
    head(c, t, B["start"], "CLAUDE SLIDES", "MONTAR E APRESENTAR", SLD)
    aa = ep(t, C["09.a"], 0.5)
    if aa > 0:
        for i in range(5):
            ai = ep(t, C["09.a"] + 0.2 * i, 0.4)
            slide_mock(c, 150, 240 + i * 120, 180, ai, kind=i % 2,
                       title=("Resultados", "Destaques", "Funil", "Riscos", "Próximos")[i])
    edit = ep(t, C["09.b"], 0.5)
    title = "Vendas subiram 18%" if edit > 0.5 else "Resultados da semana"
    present = ep(t, C["09.c"], 0.6)
    if aa > 0:
        x, y, w = lerp(400, 380, present), lerp(250, 210, present), lerp(1000, 1180, present)
        slide_mock(c, x, y, w, aa, title=title)
        if edit > 0 and present < 0.5:
            chip(c, "editando o título", x + w - 20, y - 20, SLD, edit * (1 - present), anchor="right", size=22, filled=True)
    if present > 0:
        chip(c, "APRESENTAR", 1770, 300, SLD, present, anchor="right", size=28, filled=True)
        play = present * (0.6 + 0.4 * math.sin(t * 3))
        c.drawCircle(1700, 400, 40, paint(SLD, play, stroke=3))
        p = skia.Path(); p.moveTo(1688, 380); p.lineTo(1718, 400); p.lineTo(1688, 420); p.close()
        c.drawPath(p, paint(SLD, present))


def b_slidesexp(c, t, C, B):
    head(c, t, B["start"], "CLAUDE SLIDES", "LEVAR PARA FORA", SLD)
    a0 = ep(t, B["start"] + 0.3, 0.5)
    slide_mock(c, 150, 260, 640, a0)
    fmts = [("10.a", "PowerPoint", ".pptx"), ("10.b", "PDF", ".pdf"), ("10.c", "Google Slides", "editável")]
    for k, (cue, s, sub) in enumerate(fmts):
        a, dy = reveal(t, C[cue])
        if a <= 0:
            continue
        y = 260 + k * 130 + dy
        link(c, 800, 440, 940, y + 50, SLD, a, t, pulses=1)
        panel(c, 950, y, 820, 100, a, SLD, k=12, glow=False)
        text(c, s, 990, y + 64, 38, "black", INK, a, align="left")
        text(c, sub, 1740, y + 62, 26, "mono", SLD, a, align="right")
    ad = ep(t, C["10.d"], 0.5)
    if ad > 0:
        panel(c, 150, 700, 1620, 150, ad, GOLD, k=14, label="atenção")
        text(c, "Claude Slides = nativo, dentro do Claude", 200, 770, 30, "bold", INK, ad, align="left")
        text(c, "Claude para PowerPoint = complemento instalado no PowerPoint", 200, 820, 28, "mono", INK2, ad, align="left")


def b_design(c, t, C, B):
    head(c, t, B["start"], "CLAUDE DESIGN", "VISUAIS NO CANVAS", DSG)
    aa = ep(t, C["11.a"], 0.5)
    mv = 0.0
    if t >= C["11.b"]:
        mv = math.sin(min(1.0, (t - C["11.b"]) / 1.4) * math.pi / 2)
    if aa > 0:
        panel(c, 150, 230, 1000, 620, aa, DSG, label="canvas")
        design_mock(c, 220, 290, 860, 500, aa, t, move=mv)
    ab = ep(t, C["11.b"], 0.4)
    if ab > 0:
        cx = 220 + 86 + mv * 60 + 180
        cy = 290 + 275 + 30
        p = skia.Path(); p.moveTo(cx, cy); p.lineTo(cx, cy + 42); p.lineTo(cx + 11, cy + 32); p.lineTo(cx + 22, cy + 54)
        p.lineTo(cx + 30, cy + 50); p.lineTo(cx + 19, cy + 28); p.lineTo(cx + 34, cy + 28); p.close()
        c.drawPath(p, paint(INK, ab)); c.drawPath(p, paint("#03050B", ab, stroke=2))
        chip(c, "arrastar", 1210, 300, DSG, ab, size=24)
    ac = ep(t, C["11.c"], 0.4)
    if ac > 0:
        for k, (px, py, s) in enumerate(((900, 340, "mais contraste?"), (420, 760, "data maior"))):
            ak = ep(t, C["11.c"] + 0.4 * k, 0.3)
            c.drawCircle(px, py, 18, paint(GOLD, ak))
            text(c, str(k + 1), px, py + 8, 20, "black", "#03050B", ak)
        chip(c, "comentários", 1210, 400, GOLD, ac, size=24)
    ad = ep(t, C["11.d"], 0.5)
    if ad > 0:
        bubble(c, 1210, 480, 560, 150, ad)
        text(c, "Troque o fundo por", 1250, 560, 30, "semibold", INK, ad, align="left")
        text(c, "um tom mais escuro.", 1250, 600, 30, "semibold", INK, ad, align="left")


def b_designsystem(c, t, C, B):
    head(c, t, B["start"], "CLAUDE DESIGN", "DESIGN SYSTEMS", DSG)
    panel(c, 150, 230, 760, 600, ep(t, C["12.a"], 0.5), DSG, label="sua marca")
    a1 = ep(t, C["12.a1"], 0.4)
    brand = ["#FF6B35", "#1B998B", "#F7F7F2", "#2E294E"]
    if a1 > 0:
        text(c, "CORES", 200, 310, 22, "monob", DIM, a1, align="left")
        for i, col in enumerate(brand):
            rrect(c, 200 + i * 110, 330, 90, 90, 12, col, a1)
    a2 = ep(t, C["12.a2"], 0.4)
    if a2 > 0:
        text(c, "FONTES", 200, 480, 22, "monob", DIM, a2, align="left")
        text(c, "Aa  Título forte", 200, 545, 48, "black", INK, a2, align="left")
        text(c, "Aa  texto corrido da marca", 200, 590, 28, "mono", INK2, a2, align="left")
    a3 = ep(t, C["12.a3"], 0.4)
    if a3 > 0:
        text(c, "COMPONENTES", 200, 660, 22, "monob", DIM, a3, align="left")
        rrect(c, 200, 690, 200, 64, 32, brand[0], a3)
        text_mid(c, "Comprar", 300, 722, 26, "bold", "#03050B", a3)
        rrect(c, 430, 690, 200, 64, 32, PANEL, a3, stroke=3, stroke_color=brand[1])
        text_mid(c, "Saiba mais", 530, 722, 26, "bold", brand[1], a3)
    ab = ep(t, C["12.b"], 0.5)
    if ab > 0:
        text(c, "IMPORTAR DE", 980, 290, 24, "monob", DIM, ab, align="left")
        for i, s in enumerate(("repositório GitHub", "arquivos de design", "seu código (/design-sync)")):
            chip(c, s, 980, 340 + i * 64, DSG, ep(t, C["12.b"] + 0.4 * i, 0.4), size=24)
    ac = ep(t, C["12.c"], 0.5)
    if ac > 0:
        text(c, "TODO TRABALHO NOVO", 980, 560, 24, "monob", LIME, ac, align="left")
        design_mock(c, 980, 590, 360, 240, ac, t, brand=(brand[0], brand[1]), title="PROMO")
        slide_mock(c, 1380, 610, 390, ac, col=brand[0], title="Plano 2027")


def b_designexp(c, t, C, B):
    head(c, t, B["start"], "CLAUDE DESIGN", "EXPORTAR", DSG)
    a0 = ep(t, B["start"] + 0.3, 0.5)
    design_mock(c, 150, 260, 640, 480, a0, t)
    aa = ep(t, C["13.a"], 0.5)
    fmts = [".zip", "PDF", "PowerPoint", "HTML"]
    for k, s in enumerate(fmts):
        a = ep(t, C["13.a"] + 0.35 * k, 0.4)
        y = 270 + k * 110
        link(c, 800, 500, 940, y, DSG, a, t, pulses=1)
        chip(c, s, 950, y, DSG, a, size=34, filled=True, peso="bold")
    ab = ep(t, C["13.b"], 0.5)
    if ab > 0:
        link(c, 800, 560, 1300, 760, LIME, ab, t, pulses=2)
        chip(c, "direto para outra ferramenta →", 1310, 760, LIME, ab, size=28)


def b_exemplo(c, t, C, B):
    head(c, t, B["start"], "OS TRÊS JUNTOS", "EXEMPLO DA ANTHROPIC", LIME)
    aa = ep(t, C["14.a"], 0.5)
    if aa > 0:
        bubble(c, 150, 230, 1620, 110, aa)
        typed(c, "Analise o funil de vendas da semana, escreva o relatório e faça 5 slides.", 190, 300, 32, t,
              C["14.a"], cps=36, col=INK, peso="semibold", cursor=t < C["14.b"])
    ab, dyb = reveal(t, C["14.b"])
    if ab > 0:
        panel(c, 150, 400 + dyb, 560, 440, ab, DOC, label="relatório")
        doc_mock(c, 180, 440 + dyb, 500, 370, ab, lines=9, hi=5 if t >= C["14.c"] else None, hi_col=ROSE)
    ac = ep(t, C["14.c"], 0.4)
    if ac > 0:
        chip(c, "ATRASOU: 3 negócios", 430, 860, ROSE, ac, anchor="center", size=22, filled=True)
    ad = ep(t, C["14.d"], 0.5)
    if ad > 0:
        panel(c, 760, 400, 560, 440, ad, SLD, label="5 slides")
        for i in range(5):
            ai = ep(t, C["14.d"] + 0.2 * i, 0.3)
            slide_mock(c, 790 + (i % 2) * 260, 440 + (i // 2) * 130, 240, ai, kind=i % 2,
                       title=("Resumo", "Funil", "Atrasos", "Metas", "Próximos")[i])
    ae = ep(t, C["14.e"], 0.5)
    if ae > 0:
        panel(c, 1370, 400, 400, 440, ae, LIME, label="agendado")
        text(c, "toda", 1570, 540, 36, "mono", INK2, ae)
        glow_text(c, "SEGUNDA", 1570, 620, 62, "black", LIME, ae, glow=0.4)
        text(c, "repete sozinho", 1570, 700, 28, "mono", INK2, ae)


def b_planos(c, t, C, B):
    head(c, t, B["start"], "QUEM PODE USAR", "TODOS OS PLANOS", LIME)
    plans = ["Free", "Pro", "Max", "Team", "Enterprise"]
    for k, s in enumerate(plans):
        a, dy = reveal(t, C["15.a"] + 0.25 * k)
        if a <= 0:
            continue
        x = 150 + k * 330
        panel(c, x, 260 + dy, 300, 150, a, LIME, k=14)
        glow_text(c, s, x + 150, 350 + dy, 44, "black", INK, a, glow=0.12)
        check_icon(c, x + 265, 290 + dy, 14, a, LIME)
    ab = ep(t, C["15.b"], 0.5)
    chip(c, "ENTERPRISE: LIGADO POR PADRÃO EM 15/10", 1770, 470, GOLD, ab, anchor="right", size=24, filled=True)
    ac = ep(t, C["15.c"], 0.5)
    phone(c, 400, 700, ac, LIME, "slide")
    if ac > 0:
        for i, s in enumerate(("criar", "ver", "editar")):
            check_icon(c, 600, 600 + i * 70, 16, ep(t, C["15.c"] + 0.3 * i, 0.3), LIME)
            text(c, s, 635, 612 + i * 70, 32, "bold", INK, ep(t, C["15.c"] + 0.3 * i, 0.3), align="left")
    ad = ep(t, C["15.d"], 0.5)
    if ad > 0:
        panel(c, 900, 580, 870, 220, ad, GOLD, k=14, label="compartilhamento")
        text(c, "Mudar quem pode ver:", 950, 660, 30, "bold", INK, ad, align="left")
        text(c, "só no navegador ou no app do computador", 950, 720, 28, "mono", INK2, ad, align="left")


def b_siteantigo(c, t, C, B):
    head(c, t, B["start"], "ATENÇÃO", "O SITE SEPARADO VAI FECHAR", ROSE)
    a0 = ep(t, B["start"] + 0.3, 0.5)
    rrect(c, 150, 240, 1620, 70, 35, "#0E1830", a0, stroke=2, stroke_color=DIM)
    text(c, "claude.ai/design", 200, 287, 32, "mono", INK, a0, align="left")
    aa = ep(t, C["16.a"], 0.5)
    if aa > 0:
        panel(c, 150, 360, 520, 440, aa, ROSE, label="fecha em")
        glow_text(c, "14", 410, 590, 180, "black", ROSE, aa, glow=0.4)
        text(c, "DEZEMBRO · 2026", 410, 660, 32, "monob", INK, aa)
    rows = [("16.b", "design systems", "dá para migrar", LIME), ("16.c", "conversas e comentários", "serão apagados", ROSE)]
    for k, (cue, s, st, col) in enumerate(rows):
        a, dy = reveal(t, C[cue])
        if a <= 0:
            continue
        y = 360 + k * 150 + dy
        panel(c, 730, y, 1040, 120, a, col, k=14, glow=False)
        text(c, s, 780, y + 75, 36, "black", INK, a, align="left")
        chip(c, st, 1740, y + 60, col, a, anchor="right", size=26, filled=True)
    ad = ep(t, C["16.d"], 0.5)
    if ad > 0:
        panel(c, 730, 680, 1040, 120, ad, GOLD, k=14)
        text(c, "Baixe os seus projetos em .zip antes da data", 780, 755, 34, "black", GOLD, ad, align="left")


def b_cuidados(c, t, C, B):
    head(c, t, B["start"], "CUIDADOS", "QUEM ASSINA É VOCÊ", GOLD)
    rows = [("17.a", "O Claude escreve rápido", "mas a responsabilidade é sua", CYAN),
            ("17.b", "Revise números e fatos", "antes de mandar para alguém", LIME),
            ("17.c", "Compartilhar fora da empresa?", "pense duas vezes", ROSE)]
    for k, (cue, t1, t2, col) in enumerate(rows):
        a, dy = reveal(t, C[cue])
        if a <= 0:
            continue
        y = 260 + k * 190 + dy
        panel(c, 150, y, 1620, 160, a, col, k=14, glow=False)
        glow_text(c, f"0{k + 1}", 210, y + 100, 56, "black", col, a, align="left", glow=0.4)
        text(c, t1, 340, y + 78, 42, "black", INK, a, align="left")
        text(c, t2, 340, y + 124, 28, "mono", INK2, a, align="left")


def b_resumo(c, t, C, B):
    head(c, t, B["start"], "RESUMO", "O QUE LEVAR DESTE VÍDEO", VIOLET)
    panel(c, 150, 220, 1620, 620, ep(t, B["start"] + 0.3, 0.5), VIOLET, label="README.md")
    rows = [("18.a", "Docs: escreve com você e com a equipe, ao mesmo tempo", DOC),
            ("18.b", "Slides: monta, edita e apresenta", SLD),
            ("18.c", "Design: visuais com a cara da sua marca", DSG),
            ("18.d", "tudo começa numa conversa e fica na aba Artifacts", VIOLET),
            ("18.e", "exporta para Word, PowerPoint, PDF, Google...", LIME)]
    for k, (cue, s, col) in enumerate(rows):
        a, dy = reveal(t, C[cue], 0.45)
        y = 330 + k * 105 + dy
        glow_text(c, f"0{k + 1}", 220, y, 40, "black", col, a, align="left", glow=0.4)
        text(c, s, 310, y, 36, "bold", INK, a, align="left")


def b_cta(c, t, C, B):
    tech.cta(c, t, C["19.like"], C["19.sub"], C["19.bell"], C["19.com"], C["19.bye"],
             "Qual dos três você vai testar primeiro?")
    a = ep(t, B["start"], 0.5) * (1 - prog(t, C["19.like"] - 0.4, 0.4))
    if a > 0:
        for k, (s, col) in enumerate((("Docs", DOC), ("Slides", SLD), ("Design", DSG))):
            glow_text(c, s, 560 + k * 400, 520, 100, "black", col, a, glow=0.6)
        text(c, "no Claude · aba Artifacts", W / 2, 620, 34, "mono", INK2, a)


BLOCKS = dict(hook=b_hook, intro=b_intro, mapa=b_mapa, artifact=b_artifact, comecar=b_comecar, docs=b_docs,
              editclaude=b_editclaude, docsshare=b_docsshare, slides=b_slides, slidesexp=b_slidesexp, design=b_design,
              designsystem=b_designsystem, designexp=b_designexp, exemplo=b_exemplo, planos=b_planos,
              siteantigo=b_siteantigo, cuidados=b_cuidados, resumo=b_resumo, cta=b_cta)
