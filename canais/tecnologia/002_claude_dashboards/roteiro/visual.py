"""Visual do vídeo Tecnologia 002 — Claude Dashboards: painéis de dados ao vivo. Tema 'tech' (futurista)."""
import math
import skia
import tech
from motor import *  # noqa
from tech import *  # noqa

tech.SERIE = "TECH//002 · DASHBOARDS"
MARCA = ""
ARQUIVO_FINAL = "tecnologia_002_claude_dashboards.mp4"
BACKGROUND, CAPTION, OVERLAY = tech.background, tech.caption, tech.overlay


# ---------------- peças deste vídeo ----------------
def cylinder(c, cx, cy, w, h, col, a, label=None):
    """ícone de banco de dados (cilindro)"""
    if a <= 0:
        return
    ry = w * 0.18
    r = skia.Rect.MakeXYWH(cx - w / 2, cy - h / 2, w, h)
    c.drawRect(r, paint(PANEL, 0.95 * a))
    c.drawRect(skia.Rect.MakeXYWH(cx - w / 2 - 4, cy - h / 2, w + 8, h), blur_paint(col, 0.18 * a, 14))
    for k in range(3):
        y = cy - h / 2 + k * h / 2
        c.drawOval(skia.Rect.MakeXYWH(cx - w / 2, y - ry, w, 2 * ry), paint(PANEL, a) if k == 0 else paint(col, 0))
        c.drawOval(skia.Rect.MakeXYWH(cx - w / 2, y - ry, w, 2 * ry), paint(col, a * (1 if k == 0 else 0.5), stroke=3))
    c.drawLine(cx - w / 2, cy - h / 2, cx - w / 2, cy + h / 2, paint(col, a, stroke=3))
    c.drawLine(cx + w / 2, cy - h / 2, cx + w / 2, cy + h / 2, paint(col, a, stroke=3))
    if label:
        text(c, label, cx, cy + h / 2 + ry + 44, 26, "monob", col, a)


def bars(c, x, y, w, h, vals, col, a, grow=1.0, labels=None, hi=None, gap=0.32):
    """barras verticais (vals 0..1), base em y+h"""
    if a <= 0:
        return
    n = len(vals)
    bw = w / n
    for i, v in enumerate(vals):
        g = ease_out(clamp(grow * 1.6 - i * 0.6 / n))
        bh = h * v * g
        cc = (hi if hi is not None and i == n - 1 else col)
        rrect(c, x + i * bw + bw * gap / 2, y + h - bh, bw * (1 - gap), bh, 4, cc, a)
        if labels:
            text(c, labels[i], x + i * bw + bw / 2, y + h + 34, 20, "mono", DIM, a)
    c.drawLine(x, y + h, x + w, y + h, paint(DIM, 0.6 * a, stroke=1.5))


def linechart(c, x, y, w, h, pts, col, a, progress=1.0, fill=True):
    if a <= 0 or progress <= 0:
        return
    n = len(pts)
    m = max(2, int(1 + (n - 1) * clamp(progress)))
    p = skia.Path()
    for i in range(m):
        px, py = x + w * i / (n - 1), y + h - h * pts[i]
        (p.moveTo if i == 0 else p.lineTo)(px, py)
    if fill:
        f = skia.Path(p)
        f.lineTo(x + w * (m - 1) / (n - 1), y + h); f.lineTo(x, y + h); f.close()
        sh = skia.Paint(AntiAlias=True)
        sh.setShader(skia.GradientShader.MakeLinear(points=[(x, y), (x, y + h)], colors=[hexc(col, 0.35 * a), hexc(col, 0.0)]))
        c.drawPath(f, sh)
    c.drawPath(p, blur_paint(col, 0.5 * a, 6, stroke=8))
    c.drawPath(p, paint(col, a, stroke=3.5, cap_round=True))
    ex, ey = x + w * (m - 1) / (n - 1), y + h - h * pts[m - 1]
    c.drawCircle(ex, ey, 7, paint(INK, a))


def kpi(c, x, y, w, h, label, value, delta=None, col=CYAN, a=1.0, dcol=LIME):
    if a <= 0:
        return
    panel(c, x, y, w, h, a, col, k=14, glow=False)
    text(c, label, x + 28, y + 46, 20, "monob", DIM, a, align="left")
    glow_text(c, value, x + 28, y + h - 30, 52, "black", INK, a, align="left", glow=0.12)
    if delta:
        chip(c, delta, x + w - 24, y + h - 46, dcol, a, anchor="right", size=22, filled=True)


def live_dot(c, x, cy, t, a, s="AO VIVO", col=LIME):
    if a <= 0:
        return
    b = 0.5 + 0.5 * math.sin(t * 5)
    c.drawCircle(x, cy, 12, blur_paint(col, 0.6 * a * b, 8))
    c.drawCircle(x, cy, 7, paint(col, a))
    text(c, s, x + 22, cy + 8, 22, "monob", col, a, align="left")


def bubble(c, x, y, w, h, a, col=VIOLET, who="você"):
    """balão de mensagem do chat"""
    panel(c, x, y, w, h, a, col, k=16, label=who)


SQL_KW = ("SELECT", "FROM", "WHERE", "GROUP", "BY", "ORDER", "COUNT(*)", "AND", "AS", "DESC", "LIMIT")


def sql(c, lines, x, y, size, t, t0, a=1.0, step=0.22):
    """SQL com realce simples: palavras-chave violeta, resto branco, strings verdes"""
    segs = []
    for ln in lines:
        row = []
        for i, w in enumerate(ln.split(" ")):
            col = VIOLET if w in SQL_KW else LIME if w.startswith("'") else INK
            row.append((w + " ", col))
        segs.append(row)
    code_lines(c, segs, x, y, size, t, t0, step=step, a=a)


def mini_dash(c, x, y, w, h, t, a, col=CYAN, label="dashboard", grow=1.0, live=True):
    """painel de dashboard genérico (KPI + barras + linha)"""
    if a <= 0:
        return
    panel(c, x, y, w, h, a, col, label=label)
    if live:
        live_dot(c, x + w - 150, y + 40, t, a)
    pw = (w - 90) / 2
    bars(c, x + 40, y + 90, pw, h - 160, [0.35, 0.5, 0.42, 0.62, 0.55, 0.78, 0.9], col, a, grow, hi=LIME)
    wob = [0.3, 0.42, 0.38, 0.5, 0.47, 0.6, 0.58, 0.7, 0.66, 0.8]
    pts = [clamp(v + 0.03 * math.sin(t * 1.5 + i)) for i, v in enumerate(wob)]
    linechart(c, x + 60 + pw, y + 90, pw - 10, h - 160, pts, VIOLET, a, progress=grow)


# ======================================================================
def b_hook(c, t, C, B):
    a0 = ep(t, B["start"], 0.6)
    out = 1 - ep(t, C["01.c"], 0.5)
    bubble(c, 150, 230, 820, 190, a0 * out)
    if a0 * out > 0:
        typed(c, "Quantas pessoas se cadastraram esta", 190, 320, 34, t, B["start"] + 0.3, cps=30, col=INK, peso="semibold",
              cursor=False, a=out)
        typed(c, "semana, comparado com o mês passado?", 190, 375, 34, t, B["start"] + 1.5, cps=30, col=INK,
              peso="semibold", a=out)
    aa = ep(t, C["01.a"], 0.5) * out
    if aa > 0:
        link(c, 980, 325, 1250, 325, GOLD, aa, t, progress=ep(t, C["01.a"], 0.6), pulses=1, speed=0.2)
        node(c, 1420, 325, 95, "EQUIPE DE DADOS", None, GOLD, aa, t, glyph="SQL", gsize=44)
    ab = ep(t, C["01.b"], 0.5) * out
    if ab > 0:
        for k in range(5):
            ak = ep(t, C["01.b"] + 0.15 * k, 0.4) * out
            panel(c, 160 + k * 26, 520 + k * 26, 620, 90, ak * (0.4 + 0.15 * k), DIM, k=12, glow=False)
        text(c, "pedido #4127 · na fila", 300, 690, 30, "mono", INK2, ab, align="left")
        chip(c, "RESPOSTA EM DIAS", 1420, 640, ROSE, ep(t, C["01.b"] + 1.2, 0.5) * out, anchor="center", size=30, filled=True)
    ac = ep(t, C["01.c"], 0.6)
    if ac > 0:
        bubble(c, 150, 240, 560, 150, ac)
        text(c, "Só perguntar.", 200, 335, 44, "black", INK, ac, align="left")
        glow_line(c, 720, 315, 870, 315, CYAN, ac, 3, progress=ep(t, C["01.c"] + 0.3, 0.6))
        mini_dash(c, 900, 220, 870, 560, t, ep(t, C["01.c"] + 0.5, 0.5), grow=prog(t, C["01.c"] + 0.6, 1.4))
        chip(c, "ATUALIZA SOZINHO", 1335, 840, LIME, ep(t, C["01.c"] + 2.5, 0.5), anchor="center", size=28, filled=True)


def b_intro(c, t, C, B):
    a0 = ep(t, C["02.a"], 0.6)
    cx = W / 2
    chip(c, "ANTHROPIC", cx, 270, DIM, a0, anchor="center", size=26)
    glow_text(c, "Claude", cx, 430, 150, "black", INK, a0, glow=0.0)
    glow_text(c, "Dashboards", cx, 590, 150, "black", CYAN, a0 * (0.85 + 0.15 * math.sin(t * 2)), glow=0.6)
    ab = ep(t, C["02.b"], 0.5)
    chip(c, "08/10/2026", cx - 160, 700, INK2, ab, anchor="center", size=30)
    chip(c, "BETA", cx + 120, 700, GOLD, ep(t, C["02.b"] + 0.9, 0.5), anchor="center", size=30, filled=True)
    ac = ep(t, C["02.c"], 0.5)
    chip(c, "+ CLAUDE MOTION", cx - 150, 800, VIOLET, ac, anchor="center", size=26)
    text(c, "animações curtas", cx + 170, 810, 28, "mono", INK2, ac, align="left")


def b_mapa(c, t, C, B):
    head(c, t, B["start"], "ROTEIRO", "NESTE VÍDEO")
    items = [("03.a", "O QUE É", "pergunta → painel", CYAN), ("03.b", "POR BAIXO", "um SQL por gráfico", VIOLET),
             ("03.c", "DADOS", "warehouses e apps", CYAN), ("03.d", "CRIAR", "o seu primeiro painel", MAGENTA),
             ("03.e", "COMPARTILHAR", "equipe e permissões", LIME), ("03.f", "LIMITES", "o que saber antes", ROSE)]
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


def b_oque(c, t, C, B):
    head(c, t, B["start"], "O QUE É", "UM MODELO DE ARTIFACT")
    aa = ep(t, C["04.a"], 0.5)
    if aa > 0:
        text(c, "Artifacts", 150, 290, 30, "monob", INK2, aa, align="left")
        tabs = [("Docs", C["04.b"]), ("Slides", C["04.b"] + 0.5), ("Design", C["04.b"] + 1.0), ("Dashboards", C["04.a"])]
        x = 330
        for k, (s, t0) in enumerate(tabs):
            a = ep(t, t0, 0.4) * aa
            last = k == 3
            x0, x1 = chip(c, s, x, 280, CYAN if last else DIM, a, size=28, filled=last, peso="bold")
            x = x1 + 22 if a > 0 else x + text_w(s, "bold", 28) + 58
    ac = ep(t, C["04.c"], 0.5)
    if ac > 0:
        cylinder(c, 300, 560, 170, 190, VIOLET, ac, "seus dados")
        link(c, 400, 560, 560, 560, VIOLET, ac, t, progress=ep(t, C["04.c"] + 0.2, 0.5), pulses=2)
        bubble(c, 570, 470, 470, 180, ep(t, C["04.c"] + 0.8, 0.5))
        text(c, "pergunta em", 610, 560, 32, "semibold", INK, ep(t, C["04.c"] + 0.8, 0.5), align="left")
        text(c, "linguagem natural", 610, 605, 32, "semibold", INK, ep(t, C["04.c"] + 0.8, 0.5), align="left")
    ad = ep(t, C["04.d"], 0.5)
    if ad > 0:
        link(c, 1045, 560, 1130, 560, CYAN, ad, t, progress=ep(t, C["04.d"], 0.4), pulses=1)
        mini_dash(c, 1140, 380, 630, 420, t, ad, grow=prog(t, C["04.d"] + 0.2, 1.4))


def b_diferenca(c, t, C, B):
    head(c, t, B["start"], "A DIFERENÇA", "FOTO × JANELA", VIOLET)
    aa, dya = reveal(t, C["05.a"])
    if aa > 0:
        panel(c, 150, 250 + dya, 780, 520, aa, DIM, label="gráfico no chat")
        bars(c, 210, 340 + dya, 660, 300, [0.4, 0.55, 0.5, 0.7, 0.62], DIM, aa, 1.0)
        chip(c, "FOTO · 14:02 · CONGELADO", 540, 720 + dya, GOLD, aa, anchor="center", size=24)
    ab, dyb = reveal(t, C["05.b"])
    if ab > 0:
        tomorrow = ep(t, C["05.c"] + 1.0, 0.8)
        vals = [0.4, 0.55, 0.5, 0.7, 0.62]
        vals2 = [0.55, 0.5, 0.7, 0.62, 0.86]
        vv = [lerp(p, q, tomorrow) for p, q in zip(vals, vals2)]
        panel(c, 990, 250 + dyb, 780, 520, ab, CYAN, label="dashboard")
        live_dot(c, 1600, 290 + dyb, t, ab)
        bars(c, 1050, 340 + dyb, 660, 300, vv, CYAN, ab, 1.0, hi=LIME if tomorrow > 0.5 else None)
        chip(c, "AMANHÃ" if tomorrow > 0.5 else "HOJE", 1380, 720 + dyb, LIME, ab, anchor="center", size=26, filled=True)
        cylinder(c, 1380, 900, 90, 70, CYAN, ep(t, C["05.b"] + 0.6, 0.5))
        link(c, 1380, 860, 1380, 772 + dyb, CYAN, ep(t, C["05.b"] + 0.8, 0.5), t, pulses=2)


def b_fluxo(c, t, C, B):
    head(c, t, B["start"], "POR BAIXO", "TRÊS PASSOS")
    steps = [("06.s1", "CONECTAR", "banco ou app", VIOLET, "DB"), ("06.s2", "PERGUNTAR", "em português", CYAN, "?"),
             ("06.s3", "SQL", "um por gráfico", MAGENTA, "SQL")]
    xs = [330, 960, 1590]
    for k, (cue, lab, sub, col, g) in enumerate(steps):
        a = ep(t, C[cue], 0.55)
        if a <= 0:
            continue
        node(c, xs[k], 400, 105, lab, sub, col, a, t, glyph=g, gsize=70 if len(g) == 1 else 50)
        glow_text(c, f"0{k + 1}", xs[k], 245, 34, "monob", col, a, glow=0.4)
        if k > 0:
            link(c, xs[k - 1] + 110, 400, xs[k] - 110, 400, steps[k - 1][3], a, t, progress=ep(t, C[cue] - 0.2, 0.5))
    a3 = ep(t, C["06.s3"] + 1.0, 0.5)
    if a3 > 0:
        panel(c, 150, 660, 1060, 200, a3, MAGENTA, k=16, label="chart_1.sql")
        sql(c, ["SELECT date, COUNT(*) AS cadastros", "FROM signups GROUP BY date"], 190, 740, 30, t, C["06.s3"] + 1.2, a3)
    a4 = ep(t, C["06.s4"], 0.5)
    if a4 > 0:
        chip(c, "NÃO É CHUTE", 1490, 710, ROSE, a4, anchor="center", size=28)
        chip(c, "NÚMERO REAL, DO SEU BANCO", 1490, 800, LIME, ep(t, C["06.s4"] + 0.8, 0.5), anchor="center", size=28,
             filled=True)


def b_transparencia(c, t, C, B):
    head(c, t, B["start"], "O PONTO MAIS IMPORTANTE", "TRANSPARÊNCIA", LIME)
    a0 = ep(t, B["start"] + 0.3, 0.5)
    panel(c, 150, 240, 760, 560, a0, CYAN, label="cadastros por semana")
    hi_on = ep(t, C["07.c"], 0.3)
    bars(c, 210, 330, 640, 330, [0.42, 0.5, 0.46, 0.58, 0.85], CYAN, a0, 1.0, hi=mix(CYAN, LIME, hi_on),
         labels=["S1", "S2", "S3", "S4", "S5"])
    if hi_on > 0:
        bx = 210 + 4 * 128 + 64
        c.drawRect(skia.Rect.MakeXYWH(bx - 44, 365, 88, 290), blur_paint(LIME, 0.35 * hi_on, 14))
        p = skia.Path(); p.moveTo(bx + 10, 470); p.lineTo(bx + 10, 512); p.lineTo(bx + 21, 502); p.lineTo(bx + 32, 524)
        p.lineTo(bx + 40, 520); p.lineTo(bx + 29, 498); p.lineTo(bx + 44, 498); p.close()
        c.drawPath(p, paint(INK, hi_on)); c.drawPath(p, paint("#03050B", hi_on, stroke=2))
    ab = ep(t, C["07.b"], 0.5)
    if ab > 0:
        text(c, "última atualização: 14:02", 210, 760, 24, "mono", LIME, ab, align="left")
        c.drawCircle(196, 752, 6, paint(LIME, ab * (0.5 + 0.5 * math.sin(t * 5))))
    aa, dya = reveal(t, C["07.a"])
    if aa > 0:
        panel(c, 990, 240 + dya, 780, 290, aa, VIOLET, k=16, label="consulta")
        sql(c, ["SELECT week, COUNT(*)", "FROM signups", "WHERE created_at >= '2026-09-07'", "GROUP BY week"],
            1030, 320 + dya, 28, t, C["07.a"] + 0.3, aa, step=0.18)
    ad, dyd = reveal(t, C["07.d"])
    if ad > 0:
        bubble(c, 990, 580 + dyd, 780, 220, ad, CYAN, "Claude")
        for i, s in enumerate(("“Conta cada usuário novo uma vez,", "pela data de cadastro, agrupado", "por semana.”")):
            text(c, s, 1030, 650 + i * 46 + dyd, 30, "semibold", INK2, ep(t, C["07.d"] + 0.3 * i, 0.4), align="left")
    ae = ep(t, C["07.d"] + 2.4, 0.5)
    if ae > 0:
        glow_text(c, "SEM CONFIAR ÀS CEGAS", W / 2, 862, 44, "black", LIME, ae, glow=0.45)


def b_fontes(c, t, C, B):
    head(c, t, B["start"], "DE ONDE VÊM OS DADOS", "FONTES CONECTADAS")
    hub = (1060, 540)
    a0 = ep(t, C["08.a"], 0.5)
    chip(c, "DATA WAREHOUSES", 150, 250, CYAN, a0, size=24, filled=True)
    names = ["Amazon Redshift", "BigQuery", "ClickHouse", "Databricks", "Snowflake"]
    for k, s in enumerate(names):
        a, dy = reveal(t, C[f"08.a{k + 1}"], 0.45)
        if a <= 0:
            continue
        y = 300 + k * 108 + dy
        panel(c, 150, y, 470, 84, a, CYAN, k=14, glow=False)
        cylinder(c, 205, y + 42, 38, 34, CYAN, a)
        text(c, s, 260, y + 54, 32, "bold", INK, a, align="left")
        link(c, 625, y + 42, hub[0] - 110, hub[1], CYAN, a, t, progress=ep(t, C[f"08.a{k + 1}"] + 0.2, 0.5), pulses=1)
    if a0 > 0:
        node(c, hub[0], hub[1], 110, "CLAUDE", "dashboards", CYAN, a0, t, glyph="AI", gsize=58)
    ab, dyb = reveal(t, C["08.b"])
    if ab > 0:
        chip(c, "APPS CONECTADOS", 1770, 250, VIOLET, ab, anchor="right", size=24, filled=True)
        panel(c, 1370, 440 + dyb, 400, 200, ab, VIOLET, label="app")
        glow_text(c, "Salesforce", 1570, 560 + dyb, 48, "black", INK, ab, glow=0.15)
        link(c, 1365, 540, hub[0] + 115, hub[1], VIOLET, ab, t, progress=ep(t, C["08.b"] + 0.3, 0.5), pulses=2)


def b_levar(c, t, C, B):
    head(c, t, B["start"], "QUANDO PRECISA DE MAIS", "LEVE O PAINEL ADIANTE", MAGENTA)
    a0 = ep(t, B["start"] + 0.3, 0.5)
    mini_dash(c, 150, 260, 620, 440, t, a0, MAGENTA, "dashboard", grow=prog(t, B["start"] + 0.4, 1.2), live=False)
    aa = ep(t, C["09.a"], 0.5)
    tools = ["Grafana", "Mixpanel", "Amplitude", "PostHog"]
    for k, s in enumerate(tools):
        a = ep(t, C["09.a"] + 0.9 + 0.45 * k, 0.4)
        y = 290 + k * 100
        link(c, 780, 480, 1010, y, MAGENTA, a, t, progress=ep(t, C["09.a"] + 0.9 + 0.45 * k, 0.4), pulses=1)
        chip(c, s, 1020, y, MAGENTA, a, size=32, filled=True, peso="bold")
    more = ep(t, C["09.a"] + 3.0, 0.5)
    text(c, "+ Hex · Sigma · Omni · Perplexity", 1020, 720, 26, "mono", INK2, more * aa, align="left")
    ab = ep(t, C["09.b"], 0.5)
    if ab > 0:
        text(c, "EM BREVE", 150, 830, 26, "monob", GOLD, ab, align="left")
        for k, s in enumerate(("Looker", "Tableau", "monday.com")):
            chip(c, s, 330 + k * 260, 820, GOLD, ep(t, C["09.b"] + 0.4 * k, 0.4), size=28, peso="bold")


def b_ex1(c, t, C, B):
    head(c, t, B["start"], "EXEMPLO 01", "CADASTROS: SEMANA × MÊS", CYAN)
    aa = ep(t, C["10.a"] - 0.3, 0.5)
    bubble(c, 150, 230, 1620, 120, aa)
    if aa > 0:
        typed(c, "Compare os cadastros desta semana com os do mês anterior.", 190, 305, 36, t, C["10.a"], cps=34,
              col=INK, peso="semibold")
    ab, dyb = reveal(t, C["10.b"])
    if ab > 0:
        panel(c, 150, 410 + dyb, 640, 400, ab, VIOLET, k=16, label="consulta")
        sql(c, ["SELECT week, COUNT(*)", "FROM signups", "WHERE created_at >=", "  '2026-09-07'", "GROUP BY week"],
            190, 490 + dyb, 28, t, C["10.b"] + 0.2, ab, step=0.16)
    ac, dyc = reveal(t, C["10.c"])
    if ac > 0:
        panel(c, 850, 410 + dyc, 920, 400, ac, CYAN, label="cadastros por semana")
        bars(c, 900, 480 + dyc, 520, 240, [0.5, 0.56, 0.48, 0.6, 0.82], CYAN, ac, prog(t, C["10.c"], 1.2), hi=LIME,
             labels=["S1", "S2", "S3", "S4", "HOJE"])
        text(c, "dados ilustrativos", 1745, 790 + dyc, 18, "mono", DIM, ac, align="right")
    ad = ep(t, C["10.d"], 0.5)
    if ad > 0:
        text(c, "VARIAÇÃO", 1480, 520 + dyc, 22, "monob", DIM, ad, align="left")
        glow_text(c, "+38%", 1480, 610 + dyc, 84, "black", LIME, ad, align="left", glow=0.4)
        text(c, "vs. média do mês", 1480, 655 + dyc, 22, "mono", INK2, ad, align="left")
    ae = ep(t, C["10.d"] + 2.6, 0.5)
    chip(c, "DA FILA PARA A CONVERSA", W / 2, 856, LIME, ae, anchor="center", size=28, filled=True)


def b_ex2(c, t, C, B):
    head(c, t, B["start"], "EXEMPLO 02", "OPORTUNIDADES NO SALESFORCE", VIOLET)
    a0 = ep(t, B["start"] + 0.3, 0.5)
    panel(c, 150, 230, 1620, 600, a0, VIOLET, label="pipeline de vendas")
    text(c, "dados ilustrativos", 1745, 815, 18, "mono", DIM, a0, align="right")
    morph = ep(t, C["11.e"], 0.9)
    fa = ep(t, C["11.d"] + 0.6, 0.4)
    if fa > 0:
        chip(c, "REGIÃO: SUL", 1090, 280, CYAN, fa, size=22, filled=True)
        chip(c, "ÚLTIMO TRIMESTRE", 1330, 280, CYAN, ep(t, C["11.d"] + 1.8, 0.4), size=22, filled=True)
    aa = ep(t, C["11.a"], 0.5)
    if aa > 0:
        text(c, "FUNIL POR ETAPA", 200, 300, 22, "monob", DIM, aa, align="left")
        st = [("Prospecção", 1.0, 0.8), ("Qualificação", 0.74, 0.62), ("Proposta", 0.52, 0.47),
              ("Negociação", 0.34, 0.36), ("Fechado", 0.2, 0.25)]
        for k, (s, v1, v2) in enumerate(st):
            a = ep(t, C["11.a"] + 0.2 * k, 0.4)
            v = lerp(v1, v2, morph)
            y = 340 + k * 84
            text(c, s, 200, y + 40, 26, "mono", INK2, a, align="left")
            rrect(c, 420, y + 10, 420 * v * ep(t, C["11.a"] + 0.2 * k, 0.7), 46, 6, mix(VIOLET, CYAN, k / 4), a)
    ab = ep(t, C["11.b"], 0.5)
    v = "R$ 2,4 mi" if morph < 0.5 else "R$ 0,9 mi"
    kpi(c, 920, 340, 380, 180, "EM NEGOCIAÇÃO", v, None, CYAN, ab)
    ac = ep(t, C["11.c"], 0.5)
    if ac > 0:
        text(c, "MAIORES NEGÓCIOS ABERTOS", 920, 590, 22, "monob", DIM, ac, align="left")
        rows = [("Conta Alfa", "R$ 420 mil"), ("Conta Beta", "R$ 310 mil"), ("Conta Gama", "R$ 275 mil")]
        if morph > 0.5:
            rows = [("Conta Delta", "R$ 260 mil"), ("Conta Beta", "R$ 190 mil"), ("Conta Ômega", "R$ 120 mil")]
        for i, (n, val) in enumerate(rows):
            a = ep(t, C["11.c"] + 0.25 * i, 0.4)
            y = 640 + i * 54
            c.drawLine(920, y + 16, 1720, y + 16, paint(LINE if False else "#18233D", a, stroke=1.5))
            text(c, n, 920, y, 28, "semibold", INK, a, align="left")
            text(c, val, 1720, y, 28, "monob", LIME, a, align="right")
    kp = ep(t, C["11.b"] + 0.4, 0.5)
    kpi(c, 1340, 340, 380, 180, "NEGÓCIOS ABERTOS", "38" if morph < 0.5 else "14", None, VIOLET, kp)


def b_comecar(c, t, C, B):
    head(c, t, B["start"], "COMO CRIAR", "TRÊS CAMINHOS", LIME)
    cards = [("12.a", "PEDIR NO CHAT", "em qualquer conversa", CYAN), ("12.b", "OUTPUT → DASHBOARDS", "na caixa de mensagem", VIOLET),
             ("12.c", "ABA ARTIFACTS", "modelo de Dashboards", MAGENTA)]
    for k, (cue, t1, t2, col) in enumerate(cards):
        a, dy = reveal(t, C[cue])
        if a <= 0:
            continue
        x = 150 + k * 550
        y = 260 + dy
        panel(c, x, y, 500, 560, a, col, label=f"0{k + 1}")
        text(c, t1, x + 250, y + 90, 32 if k != 1 else 30, "black", INK, a)
        text(c, t2, x + 250, y + 135, 24, "mono", INK2, a)
        bx, by = x + 40, y + 190
        if k == 0:
            panel(c, bx, by, 420, 120, a, VIOLET, k=12, glow=False)
            text(c, "Monte um painel com...", bx + 30, by + 72, 28, "semibold", INK, a, align="left")
            mini = ep(t, C[cue] + 0.8, 0.5)
            bars(c, bx + 60, by + 170, 300, 150, [0.4, 0.6, 0.5, 0.85], CYAN, a * mini, prog(t, C[cue] + 0.8, 1))
        elif k == 1:
            rrect(c, bx, by, 420, 70, 10, "#0E1830", a, stroke=1.5, stroke_color=DIM)
            text(c, "Pergunte algo...", bx + 24, by + 46, 26, "mono", DIM, a, align="left")
            chip(c, "Output", bx + 400, by + 35, VIOLET, a, anchor="right", size=22, filled=True, peso="bold")
            menu = ep(t, C[cue] + 0.7, 0.4)
            for i, s in enumerate(("Docs", "Slides", "Design", "Dashboards")):
                on = i == 3 and t > C[cue] + 1.4
                yy = by + 110 + i * 62
                rrect(c, bx + 160, yy, 260, 54, 8, VIOLET if on else "#0E1830", a * menu)
                text(c, s, bx + 185, yy + 37, 26, "bold", "#03050B" if on else INK2, a * menu, align="left")
        else:
            for i, s in enumerate(("Dashboard de vendas", "Métricas de produto", "Funil de marketing")):
                aa = ep(t, C[cue] + 0.5 + 0.3 * i, 0.4) * a
                yy = by + i * 110
                panel(c, bx, yy, 420, 90, aa, MAGENTA if i == 0 else DIM, k=12, glow=False)
                text(c, s, bx + 30, yy + 56, 28, "semibold", INK, aa, align="left")


def b_dica(c, t, C, B):
    head(c, t, B["start"], "DICA DE OURO", "A PERGUNTA, NÃO O GRÁFICO", GOLD)
    aa = ep(t, C["13.a"], 0.5)
    if aa > 0:
        chip(c, "DIGA A PERGUNTA", 1100, 150, LIME, aa, size=24, filled=True)
        chip(c, "NÃO O TIPO DE GRÁFICO", 1400, 150, ROSE, ep(t, C["13.a"] + 0.8, 0.4), size=24)
    ab, dyb = reveal(t, C["13.b"])
    if ab > 0:
        panel(c, 150, 250 + dyb, 780, 240, ab, ROSE, label="EM VEZ DE")
        text(c, "“Gráfico de barras com", 200, 350 + dyb, 36, "semibold", INK2, ab, align="left")
        text(c, "a coluna X por Y...”", 200, 405 + dyb, 36, "semibold", INK2, ab, align="left")
        st = ep(t, C["13.c"], 0.5)
        if st > 0:
            c.drawLine(190, 370 + dyb, 190 + 600 * st, 370 + dyb, paint(ROSE, ab, stroke=4))
            c.drawLine(190, 425 + dyb, 190 + 500 * st, 425 + dyb, paint(ROSE, ab, stroke=4))
    ac, dyc = reveal(t, C["13.c"])
    if ac > 0:
        panel(c, 990, 250 + dyc, 780, 240, ac, LIME, label="PERGUNTE")
        text(c, "“Quais produtos mais", 1040, 350 + dyc, 40, "black", INK, ac, align="left")
        text(c, "cresceram este mês?”", 1040, 405 + dyc, 40, "black", LIME, ac, align="left")
    ad, dyd = reveal(t, C["13.d"])
    if ad > 0:
        panel(c, 560, 560 + dyd, 800, 300, ad, CYAN, k=16, label="o Claude escolhe a forma")
        prods = [("Produto A", 0.9), ("Produto B", 0.66), ("Produto C", 0.48), ("Produto D", 0.3)]
        for i, (s, v) in enumerate(prods):
            y = 620 + i * 54 + dyd
            text(c, s, 600, y + 28, 24, "mono", INK2, ad, align="left")
            rrect(c, 780, y, 520 * v * ep(t, C["13.d"] + 0.15 * i, 0.7), 34, 5, LIME if i == 0 else CYAN, ad)


def b_planos(c, t, C, B):
    head(c, t, B["start"], "QUEM PODE USAR", "PLANOS E ATIVAÇÃO", GOLD)
    aa = ep(t, C["14.a"], 0.5)
    if aa > 0:
        chip(c, "BETA · PLANOS PAGOS", 150, 280, GOLD, aa, size=28, filled=True)
        for k, s in enumerate(("Pro", "Max", "Team", "Enterprise")):
            a, dy = reveal(t, C["14.a"] + 0.4 + 0.3 * k)
            panel(c, 150 + k * 410, 360 + dy, 370, 150, a, CYAN if k < 3 else GOLD, k=16)
            glow_text(c, s, 335 + k * 410, 455 + dy, 48, "black", INK, a, glow=0.12)
    ab, dyb = reveal(t, C["14.b"])
    if ab > 0:
        on = ep(t, C["14.c"] + 2.2, 0.4)
        panel(c, 150, 590 + dyb, 1620, 230, ab, GOLD, label="Configurações da organização")
        crumbs = ep(t, C["14.c"], 0.5)
        text(c, "Organização  ›  Artifacts  ›  Dashboards", 200, 680 + dyb, 34, "monob", INK, crumbs * ab, align="left")
        text(c, "Enterprise: vem desligado por padrão", 200, 760 + dyb, 28, "mono", INK2, ab, align="left")
        tx, ty = 1560, 690 + dyb
        rrect(c, tx, ty - 32, 130, 64, 32, mix("#1A2440", LIME, on), ab)
        c.drawCircle(tx + 32 + 66 * on, ty, 24, paint(INK, ab))
        text(c, "ATIVO" if on > 0.5 else "DESLIGADO", tx + 65, ty + 76, 22, "monob", LIME if on > 0.5 else DIM, ab)


def b_compartilhar(c, t, C, B):
    head(c, t, B["start"], "COMPARTILHAR", "CADA UM COM SUA PERMISSÃO", LIME)
    a0 = ep(t, B["start"] + 0.3, 0.5)
    mini_dash(c, 150, 240, 640, 420, t, a0, CYAN, "dashboard", grow=1.0)
    aa = ep(t, C["15.a"], 0.5)
    if aa > 0:
        for k, (col, ox, oy) in enumerate(((MAGENTA, 330, 380), (GOLD, 560, 470), (LIME, 600, 330))):
            x = 150 + ox + 18 * math.sin(t * 1.3 + k)
            y = oy + 14 * math.cos(t * 1.1 + k * 2)
            c.drawCircle(x, y, 13, blur_paint(col, 0.6 * aa, 8))
            c.drawCircle(x, y, 9, paint(col, aa))
        chip(c, "EDIÇÃO EM EQUIPE + CLAUDE", 470, 720, CYAN, aa, anchor="center", size=24)
    ac = ep(t, C["15.c"], 0.5)
    if ac > 0:
        chip(c, "CADA PESSOA USA AS PRÓPRIAS CONEXÕES", 1290, 250, VIOLET, ac, anchor="center", size=24, filled=True)
        panel(c, 860, 320, 420, 380, ac, LIME, label="você")
        bars(c, 900, 400, 340, 200, [0.4, 0.6, 0.5, 0.85], CYAN, ac, 1.0)
        check_icon(c, 1070, 650, 18, ac, LIME)
    ad = ep(t, C["15.d"], 0.5)
    if ad > 0:
        panel(c, 1350, 320, 420, 380, ad, ROSE, label="colega")
        rrect(c, 1390, 400, 340, 200, 10, "#1A0E18", ad, stroke=2, stroke_color=ROSE)
        check_icon(c, 1560, 470, 26, ad, ROSE, "x")
        text(c, "sem acesso à fonte", 1560, 560, 26, "monob", ROSE, ad)
    ae = ep(t, C["15.e"], 0.5)
    if ae > 0:
        glow_text(c, "NADA VAZA PARA QUEM NÃO TEM PERMISSÃO", W / 2, 800, 46, "black", LIME, ae, glow=0.4)


def b_limites(c, t, C, B):
    head(c, t, B["start"], "LIMITES", "O QUE SABER ANTES", GOLD)
    aa = ep(t, C["16.a"], 0.5)
    if aa > 0:
        chip(c, "01 · BETA", 1060, 150, GOLD, aa, size=26, filled=True)
        text(c, "pode mudar", 1260, 160, 26, "mono", INK2, aa, align="left")
    ab = ep(t, C["16.b"], 0.5)
    if ab > 0:
        chip(c, "02 · SEM CAMADA SEMÂNTICA", 150, 260, ROSE, ab, size=26, filled=True)
    defs = [("painel_vendas.sql", "WHERE last_login >= now() - 30", "1.240", CYAN),
            ("painel_colega.sql", "WHERE last_order >= now() - 90", "870", VIOLET)]
    for k, (lab, cond, val, col) in enumerate(defs):
        a, dy = reveal(t, C["16.c"] + 0.6 * k)
        if a <= 0:
            continue
        x = 150 + k * 830
        panel(c, x, 330 + dy, 790, 420, a, col, label=lab)
        text(c, "“cliente ativo”", x + 40, 410 + dy, 34, "black", INK, a, align="left")
        sql(c, ["SELECT COUNT(*) FROM clientes", cond], x + 40, 480 + dy, 26, t, C["16.c"] + 0.6 * k + 0.2, a)
        glow_text(c, val, x + 40, 680 + dy, 90, "black", col, a, align="left", glow=0.35)
    ad = ep(t, C["16.d"], 0.5)
    chip(c, "CONFIRA A CONSULTA ANTES DA REUNIÃO", W / 2, 850, LIME, ad, anchor="center", size=30, filled=True)


def b_custos(c, t, C, B):
    head(c, t, B["start"], "LIMITES", "CUSTOS E DADOS SENSÍVEIS", GOLD)
    aa, dya = reveal(t, C["17.a"])
    if aa > 0:
        panel(c, 150, 260 + dya, 500, 460, aa, CYAN, label="03 · uso")
        text(c, "LIMITE DO PLANO", 400, 380 + dya, 34, "black", INK, aa)
        bar_meter(c, 200, 450 + dya, 400, 20, 0.2 + 0.45 * prog(t, C["17.a"], 2.5), CYAN, aa)
        text(c, "cada painel consome", 400, 540 + dya, 26, "mono", INK2, aa)
        text(c, "o uso normal", 400, 580 + dya, 26, "mono", INK2, aa)
    ab, dyb = reveal(t, C["17.b"])
    if ab > 0:
        panel(c, 710, 260 + dyb, 500, 460, ab, GOLD, label="warehouse")
        cylinder(c, 960, 430 + dyb, 130, 120, GOLD, ab)
        text(c, "processamento cobrado", 960, 590 + dyb, 26, "mono", INK2, ab)
        text(c, "PELO PROVEDOR", 960, 640 + dyb, 32, "black", GOLD, ab)
    ac, dyc = reveal(t, C["17.c"])
    if ac > 0:
        panel(c, 1270, 260 + dyc, 500, 460, ac, ROSE, label="saúde")
        glow_text(c, "+", 1520, 470 + dyc, 160, "black", ROSE, ac, glow=0.4)
        text(c, "fora da cobertura", 1520, 570 + dyc, 28, "mono", INK2, ac)
        text(c, "de conformidade", 1520, 610 + dyc, 28, "mono", INK2, ac)
        chip(c, "DEIXE DE FORA", 1520, 670 + dyc, ROSE, ep(t, C["17.c"] + 2.0, 0.4), anchor="center", size=26, filled=True)


def b_resumo(c, t, C, B):
    head(c, t, B["start"], "RESUMO", "O QUE LEVAR DESTE VÍDEO", CYAN)
    panel(c, 150, 220, 1620, 660, ep(t, B["start"] + 0.3, 0.5), CYAN, label="README.md")
    rows = [("18.a", "uma pergunta vira um painel ao vivo", CYAN),
            ("18.b", "cada gráfico = uma consulta SQL na sua fonte", VIOLET),
            ("18.c", "consulta à mostra + hora da última atualização", LIME),
            ("18.d", "Redshift · BigQuery · ClickHouse · Databricks · Snowflake · Salesforce", CYAN),
            ("18.e", "respeita a permissão de cada pessoa", LIME),
            ("18.f", "é beta: confira a consulta", GOLD)]
    for k, (cue, s, col) in enumerate(rows):
        a, dy = reveal(t, C[cue], 0.45)
        y = 320 + k * 92 + dy
        glow_text(c, f"0{k + 1}", 220, y, 40, "black", col, a, align="left", glow=0.4)
        text(c, s, 310, y, 36 if k != 3 else 32, "bold", INK, a, align="left")


def b_cta(c, t, C, B):
    tech.cta(c, t, C["19.like"], C["19.sub"], C["19.bell"], C["19.com"], C["19.bye"],
             "Qual pergunta você faria aos seus dados?")
    a = ep(t, B["start"], 0.5) * (1 - prog(t, C["19.like"] - 0.4, 0.4))
    if a > 0:
        glow_text(c, "Claude Dashboards", W / 2, 520, 120, "black", CYAN, a, glow=0.7)
        text(c, "beta · planos pagos · aba Artifacts", W / 2, 620, 34, "mono", INK2, a)


BLOCKS = dict(hook=b_hook, intro=b_intro, mapa=b_mapa, oque=b_oque, diferenca=b_diferenca, fluxo=b_fluxo,
              transparencia=b_transparencia, fontes=b_fontes, levar=b_levar, ex1=b_ex1, ex2=b_ex2, comecar=b_comecar,
              dica=b_dica, planos=b_planos, compartilhar=b_compartilhar, limites=b_limites, custos=b_custos,
              resumo=b_resumo, cta=b_cta)
