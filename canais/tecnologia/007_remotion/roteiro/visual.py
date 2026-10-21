"""Visual do vídeo Tecnologia 007 — Remotion (vídeos com React). Tema 'tech' (futurista)."""
import math
import skia
import motor
import tech
from motor import *  # noqa
from tech import *  # noqa

tech.SERIE = "TECH//007 · REMOTION"
MARCA = ""
ARQUIVO_FINAL = "tecnologia_007_remotion.mp4"
BACKGROUND, CAPTION, OVERLAY = tech.background, tech.caption, tech.overlay

RB = "#3B9BFF"   # azul Remotion (só em detalhes)
KW, NM, TX, NUM, CM = VIOLET, CYAN, INK, GOLD, DIM   # realce de código
NOMES = ["Ana", "Bruno", "Carla", "Diego", "Elisa", "Fábio", "Gabi", "Hugo", "Íris", "João", "Kátia", "Leo"]


# ---------------- maquetes ----------------
def thumb(c, x, y, w, a, col=CYAN, name=None, val=None, k=0):
    """miniatura de vídeo 16:9 com nome e número do cliente"""
    if a <= 0:
        return
    h = w * 9 / 16
    rrect(c, x, y, w, h, max(3, w * 0.03), "#0F1A33", a, stroke=1.5, stroke_color=col)
    s = w / 300
    c.drawCircle(x + w * 0.78, y + h * 0.42, h * 0.22, paint(col, 0.35 * a))
    if name:
        text(c, name, x + 18 * s, y + 62 * s, 34 * s, "black", INK, a, align="left")
    if val:
        text(c, val, x + 18 * s, y + 108 * s, 30 * s, "monob", col, a, align="left")
    rrect(c, x + 18 * s, y + h - 26 * s, (w - 36 * s) * (0.3 + 0.6 * hash01(k, 3)), 6 * s, 3 * s, col, a)


def canvas_frame(c, x, y, w, frame, a, col=CYAN, label=True, total=150):
    """tela 16:9 desenhada a partir do número do quadro (bolinha que anda + título que surge)"""
    if a <= 0:
        return
    h = w * 9 / 16
    rrect(c, x, y, w, h, 8, "#060B16", a, stroke=2, stroke_color=col)
    s = w / 640
    u = clamp(frame / max(1, total - 1))
    op = clamp(frame / 30)
    text(c, "Olá, Remotion", x + w / 2, y + h * 0.42, 52 * s, "black", INK, a * op)
    bx = x + 60 * s + (w - 120 * s) * ease_io(u)
    c.drawCircle(bx, y + h * 0.7, 18 * s, blur_paint(MAGENTA, 0.6 * a, 8))
    c.drawCircle(bx, y + h * 0.7, 14 * s, paint(MAGENTA, a))
    if label:
        chip(c, f"frame {int(frame)}", x + w - 14 * s, y + 34 * s, col, a, anchor="right", size=max(14, 22 * s), filled=True)


def studio(c, x, y, w, h, a, t, col=CYAN, frame=None, render_btn=0.0):
    """maquete do Remotion Studio: prévia + linha do tempo com cursor"""
    if a <= 0:
        return
    panel(c, x, y, w, h, a, col, label="Remotion Studio")
    pw = w * 0.62
    fr = (t * 30) % 150 if frame is None else frame
    canvas_frame(c, x + (w - pw) / 2, y + 40, pw, fr, a, col)
    ty = y + 40 + pw * 9 / 16 + 30
    tracks = [(0.0, 0.45, CYAN, "Intro"), (0.35, 0.85, VIOLET, "Título"), (0.1, 1.0, MAGENTA, "Áudio")]
    for i, (s0, s1, cc, lab) in enumerate(tracks):
        yy = ty + i * 38
        if yy + 28 > y + h - 10:
            break
        rrect(c, x + 150 + (w - 190) * s0, yy, (w - 190) * (s1 - s0), 28, 5, cc, 0.55 * a)
        text(c, lab, x + 40, yy + 21, 18, "mono", INK2, a, align="left")
    px = x + 150 + (w - 190) * (fr / 149)
    c.drawLine(px, ty - 8, px, ty + 3 * 38, paint(ROSE, a, stroke=2.5))
    if render_btn > 0:
        chip(c, "Render", x + w - 30, y + 40, LIME, a * render_btn, anchor="right", size=24, filled=True, peso="bold")


def code_panel(c, x, y, w, h, a, lines, t, t0, label="MyComposition.tsx", size=28, col=CYAN, step=0.14):
    panel(c, x, y, w, h, a, col, label=label)
    code_lines(c, lines, x + 40, y + 70, size, t, t0, step=step, a=a)


# ======================================================================
def b_hook(c, t, C, B):
    a0 = ep(t, B["start"] + 0.2, 0.5)
    code = ep(t, C["01.c"], 0.6)
    grid = a0 * (1 - code) * (1 - 0.8 * ep(t, C["01.b"], 0.5))
    if grid > 0:
        n = int(clamp((t - B["start"]) / 2.2) * 48) + 1
        for i in range(min(n, 48)):
            col_i, row_i = i % 8, i // 8
            ai = ep(t, B["start"] + 0.2 + i * 0.045, 0.3) * grid
            thumb(c, 150 + col_i * 205, 230 + row_i * 112, 185, ai, (CYAN, VIOLET, MAGENTA)[i % 3],
                  NOMES[i % 12] if t >= C["01.a"] else None, f"R$ {1000 + 137 * i:,}".replace(",", ".") if t >= C["01.a"] else None, i)
        glow_text(c, "1.000 VÍDEOS", W / 2, 205, 40, "black", INK, grid, glow=0.2)
    ab = ep(t, C["01.b"], 0.5) * (1 - code)
    if ab > 0:
        panel(c, 460, 380, 1000, 280, ab, ROSE, label="editor de vídeo")
        for i in range(3):
            rrect(c, 520, 450 + i * 54, 880 * (0.5 + 0.4 * hash01(i, 9)), 36, 6, "#2A3555", ab)
        glow_text(c, "SEMANAS DE TRABALHO", W / 2, 630, 44, "black", ROSE, ab, glow=0.4)
    if code > 0:
        lines = [[("const ", KW), ("cliente", NM), (" = { nome: ", TX), ('"Ana"', LIME), (", total: ", TX), ("1.137", NUM), (" }", TX)],
                 [],
                 [("<", TX), ("Video", NM), (" cliente={", TX), ("cliente", NM), ("} />", TX)]]
        code_panel(c, 150, 250, 900, 330, code, lines, t, C["01.c"] + 0.2, label="video.tsx", size=30)
        ad = ep(t, C["01.d"], 0.5)
        k = int(max(0, t - C["01.d"]) / 0.9) % 12 if ad > 0 else 0
        thumb(c, 1120, 250, 650, code, CYAN, NOMES[k], f"R$ {1000 + 137 * k:,}".replace(",", "."), k)
        if ad > 0:
            link(c, 1050, 420, 1115, 420, CYAN, ad, t, pulses=2)
            chip(c, "troca o dado → vídeo novo", 1120, 680, LIME, ad, size=26, filled=True)


def b_intro(c, t, C, B):
    aa = ep(t, C["02.a"], 0.6)
    if aa > 0:
        # logo: triângulo de play em camadas
        cx, cy = 360, 420
        for i, cc in enumerate((VIOLET, RB, CYAN)):
            ai = ep(t, C["02.a"] + 0.15 * i, 0.4)
            p = skia.Path(); d = 26 * (2 - i)
            p.moveTo(cx - 70 + d, cy - 90 + d * 0.3); p.lineTo(cx + 90 + d, cy + d * 0.3); p.lineTo(cx - 70 + d, cy + 90 + d * 0.3); p.close()
            c.drawPath(p, blur_paint(cc, 0.4 * ai, 16)); c.drawPath(p, paint(cc, 0.9 * ai))
        glow_text(c, "Remotion", 560, 470, 150, "black", INK, aa, align="left", glow=0.25)
    ab = ep(t, C["02.b"], 0.5)
    if ab > 0:
        text(c, '"Make videos programmatically with React."', 560, 560, 34, "mono", CYAN, ab, align="left")
        text(c, "faça vídeos programando, com React", 560, 610, 28, "semibold", INK2, ab, align="left")
    stats = [("02.c", 64000, "{:,}+".format, "ESTRELAS NO GITHUB", GOLD),
             ("02.d", 300, "{}+".format, "CONTRIBUIDORES", VIOLET),
             ("02.e", 5, "{}M+".format, "INSTALAÇÕES / MÊS", LIME)]
    for k, (cue, v, fmt, lab, col) in enumerate(stats):
        a, dy = reveal(t, C[cue])
        if a <= 0:
            continue
        x = 150 + k * 550
        panel(c, x, 680 + dy, 500, 190, a, col, k=16)
        n = int(v * ease_out(prog(t, C[cue], 1.6)))
        glow_text(c, fmt(n).replace(",", "."), x + 250, 780 + dy, 70, "black", col, a, glow=0.4)
        text(c, lab, x + 250, 835 + dy, 22, "monob", INK2, a)


def b_mapa(c, t, C, B):
    head(c, t, B["start"], "ROTEIRO", "NESTE VÍDEO", VIOLET)
    items = [("03.a", "A IDEIA", "vídeo = quadros", CYAN), ("03.b", "ANIMAR", "com código React", VIOLET),
             ("03.c", "COMEÇAR", "e renderizar", LIME), ("03.d", "DADOS", "1 modelo, mil vídeos", MAGENTA),
             ("03.e", "AGENTES DE IA", "você descreve", CYAN), ("03.f", "LICENÇA", "o detalhe importante", GOLD)]
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


def b_ideia(c, t, C, B):
    head(c, t, B["start"], "A IDEIA", "UM VÍDEO É UMA SEQUÊNCIA DE QUADROS", CYAN)
    aa = ep(t, C["04.a"], 0.5)
    if aa > 0:
        # tira de filme com quadros numerados
        shift = (t - C["04.a"]) * 60
        base, off = int(shift // 230), shift % 230
        c.save(); c.clipRect(skia.Rect.MakeXYWH(150, 230, 1620, 200))
        rrect(c, 150, 240, 1620, 180, 6, "#060B16", aa)
        for i in range(0, 9):
            fx = 150 + i * 230 - off
            fr = (i + base) * 15
            for k in range(6):
                rrect(c, fx + 12 + k * 36, 248, 20, 12, 3, "#2A3555", aa)
                rrect(c, fx + 12 + k * 36, 400, 20, 12, 3, "#2A3555", aa)
            canvas_frame(c, fx + 10, 268, 200, fr % 150, aa, CYAN, label=False)
            text(c, f"{fr}", fx + 110, 392, 18, "monob", GOLD, aa)
        c.restore()
    ab = ep(t, C["04.b"], 0.5)
    fr = (t - C["04.d"]) * 30 % 150 if t >= C["04.d"] else 42
    if ab > 0:
        panel(c, 150, 480, 520, 360, ab, GOLD, label="o Remotion te dá")
        glow_text(c, f"frame = {int(fr)}", 410, 620, 58, "black", GOLD, ab, glow=0.4)
        text(c, "+ uma tela em branco", 410, 700, 30, "mono", INK2, ab)
    ac = ep(t, C["04.c"], 0.5)
    if ac > 0:
        lines = [[("export const ", KW), ("Cena", NM), (" = () => {", TX)],
                 [("  const ", KW), ("frame", NM), (" = ", TX), ("useCurrentFrame", CYAN), ("();", TX)],
                 [("  return ", KW), ("<h1>", TX), ("Frame {frame}", LIME), ("</h1>", TX), (";", TX)],
                 [("};", TX)]]
        code_panel(c, 720, 480, 600, 360, ac, lines, t, C["04.c"] + 0.2, label="Cena.tsx", size=24, col=VIOLET)
    ad = ep(t, C["04.d"], 0.5)
    if ad > 0:
        canvas_frame(c, 1360, 540, 410, fr, ad, CYAN)
        chip(c, "= ANIMAÇÃO", 1565, 820, LIME, ad, anchor="center", size=26, filled=True)


def b_composicao(c, t, C, B):
    head(c, t, B["start"], "COMPOSIÇÃO", "O FORMATO DO VÍDEO", CYAN)
    a0 = ep(t, B["start"] + 0.3, 0.5)
    cues = [("05.a", 1), ("05.a", 2), ("05.b", 3), ("05.c", 4)]
    hi = -1
    for i, (cue, ln) in enumerate(cues):
        if t >= C[cue]:
            hi = ln if cue != "05.a" else (1 if t < C[cue] + 0.9 else 2)
    panel(c, 150, 240, 900, 520, a0, CYAN, label="Root.tsx")
    rows = [[("<", TX), ("Composition", NM)],
            [("  width", VIOLET), ("={", TX), ("1920", NUM), ("}", TX)],
            [("  height", VIOLET), ("={", TX), ("1080", NUM), ("}", TX)],
            [("  fps", VIOLET), ("={", TX), ("30", NUM), ("}", TX)],
            [("  durationInFrames", VIOLET), ("={", TX), ("150", NUM), ("}", TX)],
            [("  component", VIOLET), ("={", TX), ("MyComposition", NM), ("}", TX)],
            [("/>", TX)]]
    for i, segs in enumerate(rows):
        y = 330 + i * 58
        if i == hi and i in (1, 2, 3, 4):
            rrect(c, 180, y - 40, 840, 54, 6, GOLD, 0.18 * a0)
            c.drawRect(skia.Rect.MakeXYWH(180, y - 40, 5, 54), paint(GOLD, a0))
        xx = 200
        for s, col in segs:
            xx += text(c, s, xx, y, 34, "mono", col, a0, align="left")
    aa = ep(t, C["05.a"], 0.5)
    if aa > 0:
        rrect(c, 1120, 260, 560, 315, 6, "#060B16", aa, stroke=2, stroke_color=CYAN)
        text(c, "1920", 1400, 250, 26, "monob", CYAN, aa)
        text(c, "1080", 1720, 425, 26, "monob", CYAN, aa)
        text(c, "16:9", 1400, 430, 50, "black", INK2, aa)
    ab = ep(t, C["05.b"], 0.5)
    chip(c, "30 quadros / segundo", 1120, 630, VIOLET, ab, size=28)
    ac = ep(t, C["05.c"], 0.5)
    chip(c, "150 quadros no total", 1120, 700, VIOLET, ac, size=28)
    ad = ep(t, C["05.d"], 0.5)
    if ad > 0:
        panel(c, 1120, 760, 650, 110, ad, LIME, k=14)
        glow_text(c, "150 ÷ 30 = 5 segundos", 1445, 832, 46, "black", LIME, ad, glow=0.35)


def b_animar(c, t, C, B):
    head(c, t, B["start"], "ANIMAR COM CÓDIGO", "INTERPOLATE", VIOLET)
    lines = [[("const ", KW), ("frame", NM), (" = ", TX), ("useCurrentFrame", CYAN), ("();", TX)],
             [],
             [("const ", KW), ("opacity", NM), (" = ", TX), ("interpolate", CYAN), ("(", TX)],
             [("  frame, ", NM), ("[", TX), ("0", NUM), (", ", TX), ("30", NUM), ("], [", TX), ("0", NUM), (", ", TX), ("1", NUM), ("]", TX)],
             [(");", TX)]]
    aa = ep(t, C["06.a"], 0.5)
    panel(c, 150, 240, 900, 380, aa, VIOLET, label="Titulo.tsx")
    if aa > 0:
        for i, segs in enumerate(lines):
            gate = C["06.a"] if i < 2 else C["06.b"]
            ai = ep(t, gate + 0.1 * i, 0.35) * aa
            xx = 190
            for s, col in segs:
                xx += text(c, s, xx, 320 + i * 58, 30, "mono", col, ai, align="left")
    # gráfico frame → opacidade
    ac = ep(t, C["06.c"], 0.5)
    if ac > 0:
        gx, gy, gw, gh = 210, 680, 780, 160
        panel(c, 150, 650, 900, 220, ac, CYAN, k=14, glow=False)
        c.drawLine(gx, gy + gh - 20, gx + gw, gy + gh - 20, paint(DIM, ac, stroke=1.5))
        x30 = gx + gw * 0.35
        p = skia.Path(); p.moveTo(gx, gy + gh - 20); p.lineTo(x30, gy + 20); p.lineTo(gx + gw, gy + 20)
        pp = paint(CYAN, ac, stroke=4); c.drawPath(p, pp)
        text(c, "0", gx, gy + gh + 8, 20, "monob", GOLD, ac)
        text(c, "30", x30, gy + gh + 8, 20, "monob", GOLD, ac)
        text(c, "frame", gx + gw - 40, gy + gh + 8, 20, "mono", DIM, ac)
        text(c, "opacidade 0 → 1", gx + gw - 10, gy + 10, 20, "mono", CYAN, ac, align="right")
        fr = ((t - C["06.c"]) * 30) % 75
        u = clamp(fr / 30)
        dx = gx + gw * 0.35 * u if fr <= 30 else x30 + (gx + gw - x30) * (fr - 30) / 45
        dy = gy + gh - 20 - (gh - 40) * u
        c.drawCircle(dx, dy, 10, blur_paint(GOLD, 0.7 * ac, 6)); c.drawCircle(dx, dy, 7, paint(GOLD, ac))
    else:
        fr = 0
    ad = ep(t, C["06.d"], 0.5)
    pa = max(ac, ad)
    if pa > 0:
        rrect(c, 1120, 300, 650, 366, 8, "#060B16", pa, stroke=2, stroke_color=CYAN)
        op = clamp(fr / 30)
        glow_text(c, "Olá, Remotion", 1445, 500, 64, "black", INK, pa * op, glow=0.2 * op)
        chip(c, f"frame {int(fr)} · opacity {op:.2f}", 1750, 330, CYAN, pa, anchor="right", size=20, filled=True)
    chip(c, "aparece suavemente no 1º segundo", 1120, 720, LIME, ad, size=26, filled=True)


def b_spring(c, t, C, B):
    head(c, t, B["start"], "ANIMAR COM CÓDIGO", "SPRING, SEQUENCE E COMPONENTES", VIOLET)
    aa, dya = reveal(t, C["07.a"])
    if aa > 0:
        panel(c, 150, 240 + dya, 760, 330, aa, MAGENTA, label="spring()")
        gx, gy, gw = 200, 300 + dya, 660
        p = skia.Path()
        for i in range(101):
            u = i / 100
            v = 1 - math.exp(-5 * u) * math.cos(14 * u)
            px, py = gx + gw * u, gy + 200 - 170 * v
            (p.moveTo if i == 0 else p.lineTo)(px, py)
        c.drawPath(p, paint(MAGENTA, aa, stroke=4))
        c.drawLine(gx, gy + 30, gx + gw, gy + 30, paint(DIM, aa * 0.6, stroke=1.2))
        u = ((t - C["07.a"]) % 2.4) / 1.6
        u = clamp(u)
        v = 1 - math.exp(-5 * u) * math.cos(14 * u)
        c.drawCircle(gx + gw * u, gy + 200 - 170 * v, 12, paint(INK, aa))
    ab, dyb = reveal(t, C["07.b"])
    if ab > 0:
        panel(c, 960, 240 + dyb, 810, 330, ab, CYAN, label="<Sequence>")
        tracks = [(0.0, 0.35, CYAN, "Cena 1"), (0.3, 0.7, VIOLET, "Cena 2"), (0.65, 1.0, MAGENTA, "Cena 3")]
        for i, (s0, s1, col, lab) in enumerate(tracks):
            ai = ep(t, C["07.b"] + 0.25 * i, 0.4) * ab
            x0 = 1000 + 730 * s0
            rrect(c, x0, 310 + i * 70 + dyb, 730 * (s1 - s0), 50, 6, col, 0.6 * ai)
            text(c, lab, x0 + 16, 344 + i * 70 + dyb, 22, "bold", INK, ai, align="left")
        px = 1000 + 730 * ((t * 0.25) % 1)
        c.drawLine(px, 295 + dyb, px, 530 + dyb, paint(ROSE, ab, stroke=2.5))
    ac = ep(t, C["07.c"], 0.5)
    if ac > 0:
        text(c, "COMPONENTES PRONTOS", 150, 660, 24, "monob", DIM, ac, align="left")
        x = 150
        for k, s in enumerate(("texto", "<Img>", "<Video>", "<Audio>")):
            x = chip(c, s, x, 730, CYAN, ep(t, C["07.c"] + 0.35 * k, 0.4), size=34, filled=k == 0, peso="bold")[1] + 30


def b_comecar(c, t, C, B):
    head(c, t, B["start"], "COMO COMEÇAR", "UM COMANDO SÓ", LIME)
    a0 = ep(t, B["start"] + 0.3, 0.5)
    chip(c, "requisito: Node.js", 150, 230, LIME, a0, size=24)
    aa = ep(t, C["08.a"], 0.5)
    if aa > 0:
        terminal(c, 150, 280, 820, 300, aa, "terminal")
        typed(c, "npx create-video@latest", 190, 390, 34, t, C["08.a"] + 0.3, cps=20, prompt="$")
    ab = ep(t, C["08.b"], 0.5)
    if ab > 0:
        text(c, "? Escolha um modelo", 190, 460, 26, "mono", CYAN, ab, align="left")
        for i, s in enumerate(("Hello World", "Blank", "Next.js")):
            ai = ep(t, C["08.b"] + 0.25 * i, 0.3)
            text(c, ("> " if i == 0 else "  ") + s, 190, 500 + i * 34, 24, "mono", LIME if i == 0 else INK2, ai, align="left")
    ac = ep(t, C["08.c"], 0.5)
    if ac > 0:
        studio(c, 1020, 260, 750, 600, ac, t, CYAN)
    ad = ep(t, C["08.d"], 0.5)
    if ad > 0:
        chip(c, "prévia", 1020, 890 - 20, CYAN, ad, size=22, filled=True)
        chip(c, "linha do tempo", 1180, 890 - 20, VIOLET, ad, size=22, filled=True)
    if ac > 0:
        rrect(c, 150, 640, 820, 70, 35, "#0E1830", ac, stroke=2, stroke_color=DIM)
        text(c, "localhost:3000", 200, 687, 30, "mono", INK, ac, align="left")
        chip(c, "no navegador", 940, 675, CYAN, ac, anchor="right", size=20)


def b_render(c, t, C, B):
    head(c, t, B["start"], "RENDERIZAR", "DO CÓDIGO AO MP4", LIME)
    aa, dya = reveal(t, C["09.a"])
    if aa > 0:
        panel(c, 150, 240 + dya, 520, 200, aa, LIME, label="no Studio")
        press = math.sin(math.pi * prog(t, C["09.a"] + 0.7, 0.35))
        chip(c, "Render video", 410, 350 + dya, LIME, aa, anchor="center", size=34 * (1 - 0.06 * press), filled=True, peso="bold")
    ab = ep(t, C["09.b"], 0.5)
    if ab > 0:
        terminal(c, 720, 240, 1050, 200, ab, "terminal")
        typed(c, "npx remotion render", 760, 360, 34, t, C["09.b"] + 0.2, cps=22, prompt="$")
    ac = ep(t, C["09.c"], 0.5)
    if ac > 0:
        text(c, "EM ESCALA", 150, 510, 24, "monob", DIM, ac, align="left")
    nodes = [("09.c", "Servidor", "Node.js (SSR)", CYAN), ("09.d", "AWS Lambda", "nuvem", GOLD), ("09.e", "GitHub Actions", "CI", VIOLET)]
    for k, (cue, s, sub, col) in enumerate(nodes):
        a = ep(t, C[cue], 0.5)
        cx = 300 + k * 330
        node(c, cx, 620, 66, None, None, col, a, t, glyph=("S", "λ", "CI")[k], gsize=50)
        text(c, s, cx, 735, 28, "extrabold", INK, a)
        text(c, sub, cx, 770, 20, "mono", DIM, a)
        if k:
            link(c, cx - 330 + 76, 620, cx - 76, 620, col, a, t, pulses=2)
    af = ep(t, C["09.f"], 0.5)
    if af > 0:
        panel(c, 1240, 500, 530, 330, af, MAGENTA, label="formatos")
        for i, s in enumerate(("MP4", "áudio", "imagem", "GIF")):
            ai = ep(t, C["09.f"] + 0.3 * i, 0.35)
            chip(c, s, 1290 + (i % 2) * 230, 600 + (i // 2) * 100, MAGENTA, ai, size=32, filled=i == 0, peso="bold")


def b_dados(c, t, C, B):
    head(c, t, B["start"], "O PODER DE VERDADE", "VÍDEOS A PARTIR DE DADOS", MAGENTA)
    aa = ep(t, C["10.a"], 0.5)
    if aa > 0:
        panel(c, 150, 240, 520, 600, aa, MAGENTA, label="clientes.csv")
        text(c, "nome", 190, 320, 24, "monob", DIM, aa, align="left")
        text(c, "total", 520, 320, 24, "monob", DIM, aa, align="left")
        for i in range(8):
            ai = ep(t, C["10.a"] + 0.1 * i, 0.3) * aa
            y = 375 + i * 56
            hl = t >= C["10.e"] and int((t - C["10.e"]) / 0.5) % 8 == i
            if hl:
                rrect(c, 175, y - 36, 470, 50, 6, MAGENTA, 0.25 * ai)
            text(c, NOMES[i], 190, y, 28, "semibold", INK, ai, align="left")
            text(c, f"{1000 + 137 * i:,}".replace(",", "."), 520, y, 28, "mono", GOLD, ai, align="left")
    ab = ep(t, C["10.b"], 0.5)
    if ab > 0:
        for i, s in enumerate(("planilha", "API", "banco de dados")):
            chip(c, s, 700, 270 + i * 58, MAGENTA, ep(t, C["10.b"] + 0.35 * i, 0.4), size=22)
    ad = ep(t, C["10.d"], 0.5)
    if ad > 0:
        link(c, 680, 585, 800, 585, MAGENTA, ad, t, pulses=2)
        panel(c, 810, 470, 330, 230, ad, CYAN, k=14, label="1 modelo")
        k = int(max(0, t - C["10.e"]) / 0.5) % 8 if t >= C["10.e"] else 0
        thumb(c, 840, 510, 270, ad, CYAN, NOMES[k], f"R$ {1000 + 137 * k:,}".replace(",", "."), k)
    ae = ep(t, C["10.e"], 0.5)
    if ae > 0:
        link(c, 1150, 585, 1200, 585, CYAN, ae, t, pulses=2)
        n = int(clamp((t - C["10.e"]) / 3.0) * 30) + 1
        for i in range(min(n, 30)):
            thumb(c, 1210 + (i % 5) * 114, 250 + (i // 5) * 72, 104, ep(t, C["10.e"] + i * 0.1, 0.25),
                  (CYAN, VIOLET, MAGENTA)[i % 3], NOMES[i % 12], None, i)
        cnt = int(1000 * ease_out(prog(t, C["10.e"], 3.0)))
        glow_text(c, f"{cnt:,} renders".replace(",", "."), 1490, 740, 48, "black", LIME, ae, glow=0.35)
    af = ep(t, C["10.f"], 0.5)
    if af > 0:
        x = 700
        for i, s in enumerate(("relatórios em vídeo", "retrospectiva do ano", "legendas automáticas")):
            x = chip(c, s, x, 830, GOLD, ep(t, C["10.f"] + 0.4 * i, 0.4), size=24, filled=True)[1] + 20


def b_ia(c, t, C, B):
    head(c, t, B["start"], "AGENTES DE IA", "AGENT SKILLS DO REMOTION", VIOLET)
    aa, dya = reveal(t, C["11.a"])
    if aa > 0:
        panel(c, 150, 240 + dya, 760, 330, aa, VIOLET, label="remotion-dev/skills")
        for i, s in enumerate(("boas práticas de animação", "composições e sequências", "legendas, áudio, render")):
            ai = ep(t, C["11.a"] + 0.4 + 0.3 * i, 0.35) * aa
            check_icon(c, 210, 330 + i * 70 + dya, 16, ai, LIME)
            text(c, s, 245, 342 + i * 70 + dya, 30, "semibold", INK, ai, align="left")
    ab = ep(t, C["11.b"], 0.5)
    if ab > 0:
        terminal(c, 960, 240, 810, 330, ab, "terminal")
        typed(c, "npx skills add", 1000, 360, 32, t, C["11.b"] + 0.2, cps=20, prompt="$", cursor=False)
        typed(c, "remotion-dev/skills", 1000, 420, 32, t, C["11.b"] + 1.0, cps=20, col=CYAN)
        if t > C["11.b"] + 2.6:
            text(c, "skills instaladas", 1000, 500, 26, "mono", LIME, ep(t, C["11.b"] + 2.6, 0.3), align="left")
    ac = ep(t, C["11.c"], 0.5)
    if ac > 0:
        text(c, "FUNCIONA COM", 150, 650, 24, "monob", DIM, ac, align="left")
        x = 150
        for i, s in enumerate(("Claude Code", "Codex", "Cursor", "+ outros")):
            x = chip(c, s, x, 730, VIOLET if i < 3 else DIM, ep(t, C["11.c"] + 0.35 * i, 0.4), size=36,
                     filled=i == 0, peso="bold")[1] + 30


def b_fluxoia(c, t, C, B):
    head(c, t, B["start"], "AGENTES DE IA", "O FLUXO COM UM AGENTE", VIOLET)
    steps = [("12.a", "DESCREVER", "em português", MAGENTA, "1"), ("12.b", "CÓDIGO", "o agente escreve", VIOLET, "2"),
             ("12.c", "STUDIO", "você confere", CYAN, "3"), ("12.d", "MP4", "renderiza", LIME, "4")]
    for k, (cue, s, sub, col, g) in enumerate(steps):
        a = ep(t, C[cue], 0.5)
        cx = 300 + k * 440
        node(c, cx, 420, 90, s, sub, col, a, t, glyph=g, gsize=70)
        if k:
            link(c, cx - 440 + 100, 420, cx - 100, 420, col, a, t, pulses=2)
    aa = ep(t, C["12.a"], 0.4)
    if aa > 0 and t < C["12.e"]:
        panel(c, 150, 640, 1620, 110, aa * (1 - prog(t, C["12.e"] - 0.3, 0.3)), MAGENTA, k=14, label="você")
        typed(c, "Crie uma intro de 5 segundos com o logo girando e o título surgindo.", 190, 710, 30, t,
              C["12.a"] + 0.3, cps=34, col=INK, peso="semibold", a=aa * (1 - prog(t, C["12.e"] - 0.3, 0.3)))
    ae = ep(t, C["12.e"], 0.5)
    if ae > 0:
        panel(c, 150, 640, 1620, 160, ae, GOLD, k=14, label="dica")
        text(c, "Uma cena por vez", 200, 715, 40, "black", GOLD, ae, align="left")
        text(c, "em vez de pedir o vídeo inteiro de uma vez", 200, 765, 28, "mono", INK2, ae, align="left")


def b_licenca(c, t, C, B):
    head(c, t, B["start"], "ATENÇÃO", "A LICENÇA", GOLD)
    aa = ep(t, C["13.a"], 0.5)
    if aa > 0:
        panel(c, 150, 240, 760, 150, aa, CYAN, k=14, glow=False)
        text(c, "código aberto no GitHub", 200, 330, 36, "black", INK, aa, align="left")
        ax = ep(t, C["13.a"] + 1.2, 0.5)
        panel(c, 1010, 240, 760, 150, ax, ROSE, k=14, glow=False)
        text(c, "não é open source tradicional", 1060, 330, 34, "black", ROSE, ax, align="left")
    ab = ep(t, C["13.b"], 0.5)
    if ab > 0:
        panel(c, 150, 450, 900, 400, ab, LIME, label="grátis")
        for i, s in enumerate(("pessoas", "sem fins lucrativos", "empresas de até 3 pessoas")):
            ai = ep(t, C["13.b"] + 0.4 * i, 0.35)
            check_icon(c, 215, 540 + i * 80, 18, ai, LIME)
            text(c, s, 255, 553 + i * 80, 34, "bold", INK, ai, align="left")
        chip(c, "INCLUSIVE USO COMERCIAL", 200, 800, LIME, ep(t, C["13.c"], 0.4), size=24, filled=True)
    ad = ep(t, C["13.d"], 0.5)
    if ad > 0:
        panel(c, 1110, 450, 660, 400, ad, GOLD, label="licença paga")
        glow_text(c, "4+", 1440, 640, 150, "black", GOLD, ad, glow=0.4)
        text(c, "pessoas na empresa", 1440, 710, 32, "mono", INK2, ad)
        text(c, "Company License", 1440, 780, 30, "bold", GOLD, ad)


def b_precos(c, t, C, B):
    head(c, t, B["start"], "LICENÇA", "QUANTO CUSTA", GOLD)
    cards = [("14.a", "CRIADORES", "US$ 25", "por mês, por pessoa", CYAN),
             ("14.b", "AUTOMAÇÃO", "US$ 0,01", "por render · mínimo US$ 100/mês", MAGENTA)]
    for k, (cue, t1, price, sub, col) in enumerate(cards):
        a, dy = reveal(t, C[cue])
        if a <= 0:
            continue
        x = 150 + k * 830
        panel(c, x, 250 + dy, 790, 330, a, col, label=t1.lower())
        glow_text(c, price, x + 395, 430 + dy, 110, "black", col, a, glow=0.4)
        text(c, sub, x + 395, 510 + dy, 28, "mono", INK2, a)
    ac = ep(t, C["14.c"], 0.5)
    if ac > 0:
        panel(c, 150, 650, 1620, 170, ac, ROSE, k=14, label="regra para todos")
        text(c, "Não pode revender o código do Remotion", 200, 730, 40, "black", INK, ac, align="left")
        text(c, "como se fosse um produto seu", 200, 785, 28, "mono", INK2, ac, align="left")
    text(c, "preços do site oficial em 17/10/2026", 1770, 880, 18, "mono", DIM, ep(t, C["14.a"], 0.5), align="right")


def b_cuidados(c, t, C, B):
    head(c, t, B["start"], "CUIDADOS", "ANTES DE COMEÇAR", GOLD)
    rows = [("15.a", "Noção de JavaScript e React", "ou um agente programando com você", CYAN),
            ("15.b", "Revise o código da IA", "antes de renderizar em lote", LIME),
            ("15.c", "Vai usar na empresa?", "confira a licença primeiro", ROSE)]
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
    rows = [("16.a", "No Remotion, o vídeo é um componente React", CYAN),
            ("16.b", "cada quadro é um número; a animação é código", VIOLET),
            ("16.c", "com dados, um modelo vira mil vídeos", MAGENTA),
            ("16.d", "com agentes de IA, você descreve e eles programam", LIME),
            ("16.e", "grátis para pessoas e equipes de até 3", GOLD)]
    for k, (cue, s, col) in enumerate(rows):
        a, dy = reveal(t, C[cue], 0.45)
        y = 330 + k * 105 + dy
        glow_text(c, f"0{k + 1}", 220, y, 40, "black", col, a, align="left", glow=0.4)
        text(c, s, 310, y, 36, "bold", INK, a, align="left")


def b_cta(c, t, C, B):
    tech.cta(c, t, C["17.like"], C["17.sub"], C["17.bell"], C["17.com"], C["17.bye"],
             "Que vídeo você criaria com código?")
    a = ep(t, B["start"], 0.5) * (1 - prog(t, C["17.like"] - 0.4, 0.4))
    if a > 0:
        glow_text(c, "Remotion", W / 2, 520, 120, "black", INK, a, glow=0.3)
        text(c, "npx create-video@latest", W / 2, 620, 36, "mono", CYAN, a)


BLOCKS = dict(hook=b_hook, intro=b_intro, mapa=b_mapa, ideia=b_ideia, composicao=b_composicao, animar=b_animar,
              spring=b_spring, comecar=b_comecar, render=b_render, dados=b_dados, ia=b_ia, fluxoia=b_fluxoia,
              licenca=b_licenca, precos=b_precos, cuidados=b_cuidados, resumo=b_resumo, cta=b_cta)
