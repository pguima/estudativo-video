"""Visual do vídeo Tecnologia 014 — API oficial do WhatsApp (Meta): custo, configuração e multiatendimento. Tema 'tech'.
Só motion graphics próprios. Sem logos nem capturas de tela de terceiros: telas da Meta e do Chatwoot aparecem apenas como
MOCKUP desenhado aqui, com o selo ILUSTRATIVO. Preços = tabela oficial da Meta em BRL (01/10/2026), ver original/."""
import math
from contextlib import contextmanager
import skia
import motor
import tech
from motor import *  # noqa
from tech import *  # noqa

# neste Linux não há Consolas: a fonte mono do tech.py não carrega. Usa DejaVu Sans Mono (como no 009/010).
motor.PESOS["mono"] = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono"
motor.PESOS["monob"] = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold"

tech.SERIE = "TECH//014 · API OFICIAL DO WHATSAPP"
MARCA = ""
ARQUIVO_FINAL = "tecnologia_014_api_oficial_whatsapp.mp4"
# som padrão do canal (_ferramentas/som_tech.py); aqui só os efeitos que fogem do "pop" de cada cue
SOM = dict(sfx={
    "01.a": ["notif@+0.3", "notif@+0.9", "notif@+1.5"], "01.b": "glitch", "01.c": "impact",
    "02.b": "data", "02.c": "notif",
    "04.d": "confirm", "05.a": "alert", "05.d": "alert",
    "06.a": "data", "06.b": "data", "06.c": "data", "06.d": "impact",
    "08.c": "typing@+0.3", "09.a": "lock", "09.b": "typing@+0.3", "09.d": "confirm",
    "10.a": "typing@+0.2", "10.c": "confirm", "10.d": "notif",
    "11.a": "notif", "12.c": ["confirm@+0.4", "confirm@+0.9", "confirm@+1.4", "confirm@+1.9"],
    "14.a": "lock", "14.b": "alert", "14.c": "lock", "14.d": "lock",
    "15.a": "confirm", "15.b": "confirm", "15.c": "confirm", "15.d": "confirm", "15.e": "confirm"})
BACKGROUND, CAPTION, OVERLAY = tech.background, tech.caption, tech.overlay

WA = "#25D366"   # verde de "mensagem" (sem logo)


# ---------------------------------------------------------------- utilidades
def fade(t, t0, t1, d=0.5, d_out=0.4):
    return ep(t, t0, d) * (1 - prog(t, t1, d_out))


def rise(t, t0, d=0.5, dy=24):
    a = ep(t, t0, d)
    return a, (1 - a) * dy


@contextmanager
def cam(c, t, B, z0=1.0, z1=1.04, px=0.0, py=0.0, cx=W / 2, cy=H / 2):
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


def selo(c, x, y, a=1.0, s="ILUSTRATIVO", anchor="left", size=20):
    if a > 0:
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
    lh = lh or size * 1.3
    ls = wrap(s, peso, size, maxw)
    for i, ln in enumerate(ls):
        text(c, ln, x, y + i * lh, size, peso, col, a, align=align)
    return len(ls) * lh


def fonte(c, s, a, y=860):
    text(c, s, W - 150, y, 20, "mono", DIM, a, align="right")


def brl(v, casas=2):
    s = f"{v:,.{casas}f}"
    if casas > 2:
        s = s.rstrip("0")
    s = s.replace(",", "X").replace(".", ",").replace("X", ".")
    return "R$ " + s


# ---------------------------------------------------------------- ícones vetoriais (desenhados aqui)
def ic_phone(c, cx, cy, s, col, a, fill="#0B1426"):
    w, h = s * 0.55, s
    rrect(c, cx - w / 2, cy - h / 2, w, h, s * 0.08, fill, a)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2, cy - h / 2, w, h), s * 0.08, s * 0.08),
                paint(col, a, stroke=max(2, s * 0.03)))
    c.drawCircle(cx, cy + h / 2 - s * 0.07, s * 0.025, paint(col, a))


def ic_person(c, cx, cy, s, col, a):
    c.drawCircle(cx, cy - s * 0.22, s * 0.2, paint(col, a))
    p = skia.Path()
    p.addArc(skia.Rect.MakeXYWH(cx - s * 0.36, cy + s * 0.04, s * 0.72, s * 0.62), 180, 180)
    p.close()
    c.drawPath(p, paint(col, a))


def ic_lock(c, cx, cy, s, col, a):
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - s * 0.4, cy - s * 0.05, s * 0.8, s * 0.55), 8, 8),
                paint(col, a))
    p = skia.Path()
    p.addArc(skia.Rect.MakeXYWH(cx - s * 0.26, cy - s * 0.5, s * 0.52, s * 0.6), 180, 180)
    c.drawPath(p, paint(col, a, stroke=s * 0.09))
    c.drawLine(cx - s * 0.26, cy - s * 0.2, cx - s * 0.26, cy - s * 0.05, paint(col, a, stroke=s * 0.09))
    c.drawLine(cx + s * 0.26, cy - s * 0.2, cx + s * 0.26, cy - s * 0.05, paint(col, a, stroke=s * 0.09))
    c.drawCircle(cx, cy + s * 0.2, s * 0.07, paint("#03050B", a))


def ic_warn(c, cx, cy, s, col, a):
    p = skia.Path(); p.moveTo(cx, cy - s * 0.48); p.lineTo(cx + s * 0.52, cy + s * 0.42); p.lineTo(cx - s * 0.52, cy + s * 0.42)
    p.close()
    pp = paint(col, a, stroke=s * 0.08); pp.setStrokeJoin(skia.Paint.kRound_Join)
    c.drawPath(p, pp)
    c.drawLine(cx, cy - s * 0.15, cx, cy + s * 0.12, paint(col, a, stroke=s * 0.09, cap_round=True))
    c.drawCircle(cx, cy + s * 0.27, s * 0.055, paint(col, a))


def ic_card(c, cx, cy, s, col, a):
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - s / 2, cy - s * 0.32, s, s * 0.64), 6, 6),
                paint(col, a, stroke=s * 0.05))
    c.drawRect(skia.Rect.MakeXYWH(cx - s / 2, cy - s * 0.17, s, s * 0.12), paint(col, a))
    c.drawRect(skia.Rect.MakeXYWH(cx - s * 0.36, cy + s * 0.1, s * 0.3, s * 0.07), paint(col, a))


def ic_cloud(c, cx, cy, s, col, a, fill=0.0):
    pth = skia.Path()
    pth.addRect(skia.Rect.MakeXYWH(cx - 0.28 * s, cy + 0.0 * s, 0.58 * s, 0.27 * s))
    for dx, dy, r in ((-0.28, 0.05, 0.22), (0.0, -0.1, 0.3), (0.3, 0.06, 0.2)):
        q = skia.Path(); q.addCircle(cx + dx * s, cy + dy * s, r * s)
        pth = skia.Op(pth, q, skia.PathOp.kUnion_PathOp)
    if fill > 0:
        c.drawPath(pth, paint(PANEL, fill * a))
    c.drawPath(pth, blur_paint(col, 0.3 * a, 16, stroke=8))
    c.drawPath(pth, paint(col, a, stroke=3))


def bubble(c, x, y, w, s, a, col=WA, mine=False, size=26):
    """balão de mensagem (desenho próprio, sem logo)"""
    if a <= 0:
        return
    h = 64
    rrect(c, x, y, w, h, 18, "#0E2A1E" if not mine else "#13213B", a)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 18, 18), paint(col, a, stroke=2))
    text(c, s, x + 24, y + 42, size, "bold", INK, a, align="left")


# ======================================================================  01 — GANCHO
def b_gancho(c, t, C, B):
    with cam(c, t, B, 1.0, 1.05):
        ta, tb, tc, td = C["01.a"], C["01.b"], C["01.c"], C["01.d"]
        out_a = 1 - prog(t, tb - 0.1, 0.5)
        aa = ep(t, ta, 0.6) * out_a
        if aa > 0:
            cx, cy = W / 2, 520
            ic_phone(c, cx, cy, 300, WA, aa)
            for k, (px, py) in enumerate(((cx - 520, cy + 120), (cx - 440, cy - 110), (cx, cy + 250),
                                          (cx + 440, cy - 110), (cx + 520, cy + 120))):
                ak = aa * ep(t, ta + 0.3 + 0.25 * k, 0.4)
                tug = 10 * math.sin(t * 7 + k * 1.3)
                c.drawLine(px, py, cx + tug, cy, paint(ROSE, 0.45 * ak, stroke=3))
                ic_person(c, px, py, 90, INK2, ak)
            glow_text(c, "1 CELULAR", cx, 300, 64, "black", INK, aa, glow=0.2)
            chip(c, "5 PESSOAS ATENDENDO", cx, 850, ROSE, aa * ep(t, ta + 1.2, 0.5), anchor="center", size=30, filled=True)
        ab = fade(t, tb, tc - 0.1)
        if ab > 0:
            gl = 6 * math.sin(t * 40) * (1 - ep(t, tb, 0.4))
            panel(c, 460 + gl, 300, 1000, 420, ab, ROSE, label="não oficial")
            ic_warn(c, 620 + gl, 470, 120, ROSE, ab)
            text(c, "imita o", 730, 440, 36, "medium", INK2, ab, align="left")
            text(c, "WhatsApp Web", 730, 500, 60, "black", INK, ab, align="left")
            chip(c, "PODE PARAR A QUALQUER MOMENTO", 960, 640, ROSE, ab * ep(t, tb + 1.2, 0.4), anchor="center", size=28)
        ac = ep(t, tc, 0.7)
        if ac > 0:
            chip(c, "META · OFICIAL", W / 2, 300, LIME, ac, anchor="center", size=28)
            s = 1 + 0.03 * (1 - ac)
            glow_text(c, "API OFICIAL", W / 2, 470, 150 * s, "black", INK, ac, glow=0.3)
            glow_text(c, "DO WHATSAPP", W / 2, 600, 110 * s, "black", WA, ac, glow=0.4)
            glow_line(c, W / 2 - 480, 640, W / 2 + 480, 640, WA, ac, 4, progress=ep(t, tc + 0.3, 0.9))
        ad = ep(t, td, 0.5)
        if ad > 0:
            for k, (s, col) in enumerate((("CUSTO", GOLD), ("CONFIGURAÇÃO", CYAN), ("MULTIATENDIMENTO", MAGENTA))):
                ak = ep(t, C["01.d"] + 0.6 + 0.9 * k, 0.4)
                chip(c, f"0{k + 1} · {s}", W / 2 - 560 + k * 560, 740, col, ak, anchor="center", size=30, filled=True)


# ======================================================================  02 — O QUE É
def b_oque(c, t, C, B):
    with cam(c, t, B, 1.0, 1.03):
        head(c, t, B["start"], "O QUE É", "CLOUD API: A META HOSPEDA", CYAN)
        X1, X2, X3, Y = 330, 960, 1590, 520
        aa = ep(t, C["02.a"], 0.6)
        if aa > 0:
            ic_cloud(c, X2, Y, 420, CYAN, aa, fill=0.85)
            glow_text(c, "CLOUD API", X2, Y + 30, 46, "black", CYAN, aa, glow=0.4)
            text(c, "servidores da Meta", X2, Y + 80, 24, "mono", INK2, aa)
            chip(c, "NADA PARA INSTALAR", X2, 300, CYAN, aa * ep(t, C["02.a"] + 1.5, 0.5), anchor="center", size=24)
            node(c, X1, Y, 100, "SEU SISTEMA", None, VIOLET, aa, t, glyph="</>", gsize=44)
            ic_phone(c, X3, Y, 190, WA, aa)
            text(c, "CLIENTE", X3, Y + 150, 34, "extrabold", INK, aa)
            link(c, X2 + 220, Y, X3 - 80, Y, WA, aa, t, pulses=2)
        ab = ep(t, C["02.b"], 0.5)
        if ab > 0:
            arrow(c, X1 + 110, Y - 70, X2 - 200, Y - 70, VIOLET, ab, 4, 16, progress=ep(t, C["02.b"], 0.8))
            chip(c, "ENVIAR · HTTP POST", (X1 + X2) / 2 - 40, Y - 120, VIOLET, ab, anchor="center", size=22, filled=True)
        ac = ep(t, C["02.c"], 0.5)
        if ac > 0:
            arrow(c, X2 - 200, Y + 70, X1 + 110, Y + 70, CYAN, ac, 4, 16, progress=ep(t, C["02.c"], 0.8))
            chip(c, "RECEBER · WEBHOOK", (X1 + X2) / 2 - 40, Y + 120, CYAN, ac, anchor="center", size=22, filled=True)
            for k, s in enumerate(("mensagem nova", "entregue", "lida")):
                ak = ep(t, C["02.c"] + 1.4 + 0.5 * k, 0.4)
                chip(c, s.upper(), 220 + k * 230, Y + 230, INK2, ak, anchor="left", size=20)
        ad = ep(t, C["02.d"], 0.5)
        if ad > 0:
            panel(c, 1180, 720, 590, 120, ad, GOLD, k=14, fill=0.92, label="preço")
            text(c, "sem mensalidade da Meta", 1220, 775, 30, "bold", INK, ad, align="left")
            text(c, "paga por mensagem", 1220, 815, 28, "monob", GOLD, ep(t, C["02.d"] + 1.0, 0.5), align="left")
        fonte(c, "fonte: developers.facebook.com/docs/whatsapp", ep(t, C["02.a"], 0.5), 885)


# ======================================================================  03 — JANELA + MODELOS
CATS = [("03.d", "MARKETING", "promoções, ofertas", MAGENTA),
        ("03.e", "UTILIDADE", "confirmação de pedido", CYAN),
        ("03.f", "AUTENTICAÇÃO", "código de login", VIOLET)]


def b_janela(c, t, C, B):
    with cam(c, t, B, 1.0, 1.03):
        head(c, t, B["start"], "DUAS REGRAS", "JANELA DE 24H E MODELOS", LIME)
        tc = C["03.c"]
        out = 1 - prog(t, tc - 0.1, 0.5)
        x0, x1, x2, y = 200, 1180, 1720, 560
        aa = ep(t, C["03.a"], 0.5) * out
        if aa > 0:
            bubble(c, x0, 330, 420, "Oi, meu pedido chegou?", aa, WA, size=26)
            text(c, "cliente manda", x0, 425, 22, "mono", INK2, aa, align="left")
            u = ep(t, C["03.a"] + 0.6, 2.0)
            rrect(c, x0, y - 30, x1 - x0, 60, 10, "#0E1930", aa)
            rrect(c, x0, y - 30, (x1 - x0) * u, 60, 10, LIME, aa * 0.85)
            text_mid(c, "JANELA DE 24 HORAS", x0 + (x1 - x0) / 2, y, 28, "black", "#03050B", aa * u)
            text(c, "0h", x0, y + 70, 22, "mono", INK2, aa, align="left")
            text(c, "24h", x1, y + 70, 22, "mono", INK2, aa, align="center")
            chip(c, "TEXTO LIVRE", x0 + (x1 - x0) / 2, y + 120, LIME, aa * ep(t, C["03.a"] + 2.4, 0.4), anchor="center", size=26,
                 filled=True)
        ab = ep(t, C["03.b"], 0.5) * out
        if ab > 0:
            p = paint(GOLD, ab * 0.8, stroke=3); p.setPathEffect(skia.DashPathEffect.Make([14, 10], -t * 30))
            c.drawRect(skia.Rect.MakeXYWH(x1 + 20, y - 30, x2 - x1 - 20, 60), p)
            text_mid(c, "FORA DA JANELA", x1 + 20 + (x2 - x1 - 20) / 2, y, 24, "monob", GOLD, ab)
            chip(c, "SÓ MODELO APROVADO", x1 + 20 + (x2 - x1 - 20) / 2, y + 120, GOLD, ab, anchor="center", size=24,
                 filled=True)
            text(c, "(template)", x1 + 20 + (x2 - x1 - 20) / 2, y + 180, 24, "mono", INK2, ab)
        ac = ep(t, tc, 0.5)
        if ac > 0:
            text(c, "TODO MODELO TEM UMA CATEGORIA", W / 2, 300, 34, "black", INK, ac)
        for k, (cue, nm, ex, col) in enumerate(CATS):
            a, dy = rise(t, C[cue])
            if a <= 0:
                continue
            x = 150 + k * 550
            panel(c, x, 380 + dy, 520, 380, a, col, k=18)
            glow_text(c, nm, x + 260, 520 + dy, 50 if len(nm) < 11 else 42, "black", col, a, glow=0.4)
            text(c, ex, x + 260, 600 + dy, 30, "medium", INK, a)
            text(c, "modelo", x + 260, 700 + dy, 22, "mono", DIM, a)


# ======================================================================  04 — PREÇOS
PRECOS = [("04.a", "MARKETING", 0.3217, "≈ 32 centavos", MAGENTA),
          ("04.b", "UTILIDADE", 0.035, "3,5 centavos", CYAN),
          ("04.c", "AUTENTICAÇÃO", 0.035, "3,5 centavos", VIOLET)]


def b_precos(c, t, C, B):
    with cam(c, t, B, 1.0, 1.03):
        head(c, t, B["start"], "QUANTO CUSTA", "PREÇO POR MENSAGEM", GOLD)
        a0 = ep(t, C["04.t"] + 1.0, 0.5)
        chip(c, "TABELA OFICIAL DA META · BRL · NÚMEROS DO BRASIL · DESDE 01/10/2026", 150, 255, GOLD, a0, size=22)
        for k, (cue, nm, v, sub, col) in enumerate(PRECOS):
            a, dy = rise(t, C[cue])
            if a <= 0:
                continue
            x, y = 150 + k * 550, 320 + dy
            panel(c, x, y, 520, 330, a, col, k=18, label="por mensagem entregue")
            text(c, nm, x + 260, y + 80, 34, "black", col, a)
            glow_text(c, brl(v, 4 if v < 0.1 or len(str(v)) > 5 else 2), x + 260, y + 200, 76, "black", INK, a, glow=0.25)
            text(c, sub, x + 260, y + 270, 26, "mono", INK2, a)
        ad = ep(t, C["04.d"], 0.5)
        if ad > 0:
            panel(c, 150, 700, 1620, 120, ad, LIME, k=14, fill=0.92, glow=True)
            bubble(c, 190, 728, 300, "cliente → você", ad, WA, size=24)
            glow_text(c, "GRÁTIS", 560, 784, 56, "black", LIME, ad, align="left", glow=0.4)
            text(c, "a Meta não cobra mensagens do usuário para a empresa", 820, 778, 26, "medium", INK2, ad, align="left")
        fonte(c, "fonte: Meta · rate card BRL · effective October 1, 2026 · coluna Brazil", ep(t, C["04.a"], 0.5), 870)


# ======================================================================  05 — SERVIÇO (mudança de 01/10/2026)
def b_servico(c, t, C, B):
    with cam(c, t, B, 1.0, 1.03):
        head(c, t, B["start"], "MUDOU EM 01/10/2026", "RESPOSTAS DE ATENDIMENTO", ROSE)
        aa = ep(t, C["05.a"], 0.5)
        if aa > 0:
            bubble(c, 150, 270, 470, "Seu pedido sai hoje!", aa, CYAN, mine=True, size=26)
            text(c, "resposta dentro da janela", 150, 370, 22, "mono", INK2, aa, align="left")
            chip(c, "ANTES: GRÁTIS", 700, 302, DIM, aa, size=24)
            chip(c, "AGORA: COBRADA", 950, 302, ROSE, aa * ep(t, C["05.a"] + 1.4, 0.4), size=24, filled=True)
        ab = ep(t, C["05.b"], 0.5)
        if ab > 0:
            x, y, w = 150, 470, 1620
            fr_free = 0.4
            u = ep(t, C["05.b"] + 0.2, 1.6)
            rrect(c, x, y, w, 70, 12, "#0E1930", ab)
            rrect(c, x, y, w * fr_free * u, 70, 12, LIME, ab * 0.9)
            text_mid(c, "1.000 GRÁTIS / MÊS / NÚMERO", x + w * fr_free / 2, y + 35, 28, "black", "#03050B", ab * u)
            text(c, "0", x, y + 110, 22, "mono", INK2, ab, align="left")
            text(c, "1.000", x + w * fr_free, y + 110, 22, "mono", INK2, ab)
            text(c, "mensagens de serviço no mês →", x + w, y + 110, 22, "mono", INK2, ab, align="right")
            ac = ep(t, C["05.c"], 0.5)
            if ac > 0:
                u2 = ep(t, C["05.c"] + 0.2, 1.2)
                rrect(c, x + w * fr_free + 6, y, (w * (1 - fr_free) - 6) * u2, 70, 12, GOLD, ac * 0.9)
                text_mid(c, "DA 1.001ª EM DIANTE: R$ 0,035 CADA", x + w * fr_free + (w * (1 - fr_free)) / 2, y + 35, 28, "black",
                         "#03050B", ac * u2)
        ad = ep(t, C["05.d"], 0.5)
        if ad > 0:
            panel(c, 150, 680, 1620, 130, ad, ROSE, k=14, fill=0.92, label="aviso da Meta")
            ic_card(c, 240, 745, 80, ROSE, ad)
            text(c, "sem forma de pagamento cadastrada", 320, 735, 32, "bold", INK, ad, align="left")
            text(c, "a entrega das mensagens de serviço pode ser interrompida", 320, 785, 26, "mono", ROSE, ad, align="left")
        fonte(c, "fonte: developers.facebook.com/docs/whatsapp/pricing · 29/10/2026", ep(t, C["05.a"], 0.5), 870)


# ======================================================================  06 — SIMULAÇÃO
SIM = [("06.a", "Marketing", 2000, 0.3217, 0, MAGENTA),
       ("06.b", "Utilidade (confirmações)", 5000, 0.035, 0, CYAN),
       ("06.c", "Serviço (respostas)", 3000, 0.035, 1000, LIME)]


def b_simulacao(c, t, C, B):
    with cam(c, t, B, 1.0, 1.03):
        head(c, t, B["start"], "SIMULAÇÃO", "UMA LOJA, UM MÊS", MAGENTA)
        a0 = ep(t, C["06.t"] + 0.6, 0.5)
        panel(c, 150, 260, 1060, 560, a0, MAGENTA, label="exemplo · contas com a tabela oficial")
        text(c, "CATEGORIA", 200, 335, 22, "monob", DIM, a0, align="left")
        text(c, "QTD", 690, 335, 22, "monob", DIM, a0, align="right")
        text(c, "× PREÇO", 880, 335, 22, "monob", DIM, a0, align="right")
        text(c, "TOTAL", 1160, 335, 22, "monob", DIM, a0, align="right")
        total = 0.0
        vals = []
        for i, (cue, nm, q, p, free, col) in enumerate(SIM):
            a, dy = rise(t, C[cue])
            v = (q - free) * p
            vals.append((v, col, a))
            if a <= 0:
                continue
            total += v * ep(t, C[cue] + 0.6, 1.0)
            y = 410 + i * 110 + dy
            c.drawRect(skia.Rect.MakeXYWH(200, y - 34, 6, 50), paint(col, a))
            text(c, nm, 225, y, 30, "bold", INK, a, align="left")
            text(c, f"{q:,}".replace(",", "."), 690, y, 30, "mono", INK, a, align="right")
            text(c, brl(p, 4), 880, y, 26, "mono", INK2, a, align="right")
            text(c, brl(v * ep(t, C[cue] + 0.6, 1.0)), 1160, y, 30, "monob", col, a, align="right")
            if free:
                text(c, "1.000 grátis → cobra 2.000", 225, y + 36, 20, "mono", LIME, a, align="left")
        ad = ep(t, C["06.d"], 0.5)
        if ad > 0:
            c.drawLine(200, 735, 1160, 735, paint(INK2, 0.5 * ad, stroke=1.5))
            text(c, "TOTAL DO MÊS", 200, 790, 30, "black", INK, ad, align="left")
            glow_text(c, brl(888.40), 1160, 795, 54, "black", GOLD, ad, align="right", glow=0.35)
        # barra de proporção
        ae = ep(t, C["06.e"], 0.6)
        x, y, h = 1300, 260, 560
        if a0 > 0:
            panel(c, x, y, 470, h, a0, INK2, label="de onde vem o custo", glow=False)
            bx, by, bw, bh = x + 70, y + 60, 120, h - 110
            rrect(c, bx, by, bw, bh, 10, "#111A30", a0)
            tot = sum(v for v, _, _ in vals)
            acc = 0.0
            for (v, col, a), (_, nm, *_r) in zip(vals, SIM):
                f = v / tot
                ff = f * a
                rrect(c, bx, by + bh - (acc + ff) * bh, bw, ff * bh, 6, col, a0)
                ly = by + bh - (acc + f / 2) * bh
                if a > 0:
                    text(c, f"{round(100 * f)}%", bx + bw + 30, ly + 12, 34 if col == MAGENTA else 26, "black", col, a,
                         align="left")
                acc += ff
            if ae > 0:
                chip(c, "MARKETING = 72%", x + 235, y + h + 40, MAGENTA, ae, anchor="center", size=24, filled=True)


# ======================================================================  07 — DETALHES DE CUSTO
DET = [("07.a", "VOLUME", "utilidade e autenticação: −5% a −25% · marketing: sem desconto", CYAN),
       ("07.b", "ANÚNCIO", "conversa vinda de “clique para o WhatsApp”: respostas grátis por até 7 dias", MAGENTA),
       ("07.c", "MOEDA", "cobrança em reais (BRL) disponível desde 01/07/2026", LIME),
       ("07.d", "PARCEIROS", "plataforma ou parceiro da Meta (BSP): mensalidade à parte", GOLD)]


def b_detalhes(c, t, C, B):
    with cam(c, t, B, 1.0, 1.03):
        head(c, t, B["start"], "CUSTO", "MAIS 4 DETALHES", CYAN)
        for i, (cue, k, v, col) in enumerate(DET):
            a, dy = rise(t, C[cue])
            if a <= 0:
                continue
            y = 260 + i * 140 + dy
            panel(c, 150, y, 1620, 115, a, col, k=14, fill=0.85, glow=False)
            glow_text(c, f"0{i + 1}", 200, y + 72, 44, "black", col, a, align="left", glow=0.4)
            text(c, k, 290, y + 50, 26, "monob", col, a, align="left")
            text(c, v, 290, y + 92, 31, "bold", INK, a, align="left")
        fonte(c, "fonte: Meta · volume tiers BRL e docs de pricing · 29/10/2026", ep(t, C["07.a"], 0.5), 870)


# ======================================================================  08/09 — CONFIGURAÇÃO (8 passos)
PASSOS = [("08.a", "Portfólio empresarial"), ("08.b", "App no Meta for Developers"), ("08.c", "Número de teste"),
          ("08.d", "Número de verdade"), ("09.a", "Token permanente"), ("09.b", "Webhook"),
          ("09.c", "Forma de pagamento"), ("09.d", "Verificar a empresa")]


def lista_passos(c, t, C, cur, a0):
    panel(c, 150, 250, 560, 600, a0, CYAN, label="passo a passo", glow=False)
    for i, (cue, s) in enumerate(PASSOS):
        a = ep(t, C[cue] - 0.3, 0.4) * a0 if cue in C else 0
        if cue in C and t < C[cue] - 0.3 and i >= 4 and cur < 4:
            a = 0.35 * a0     # passos futuros aparecem apagados
        if i < 4 and cur >= 4:
            a = a0
        if a <= 0:
            a = 0.3 * a0
        y = 315 + i * 68
        on = i == cur
        done = i < cur
        col = CYAN if on else (LIME if done else DIM)
        if on:
            rrect(c, 175, y - 30, 510, 58, 8, "#11223F", a)
            c.drawRect(skia.Rect.MakeXYWH(175, y - 30, 5, 58), paint(CYAN, a))
        c.drawCircle(220, y, 20, paint(PANEL, a))
        c.drawCircle(220, y, 20, paint(col, a, stroke=2.5))
        if done:
            check_icon(c, 220, y, 13, a, LIME)
        else:
            text_mid(c, str(i + 1), 220, y, 22, "black", col, a)
        text(c, s, 260, y + 10, 27, "bold" if on else "medium", INK if (on or done) else INK2, a, align="left")


def campo(c, x, y, w, rot, val, a, col=CYAN, t=None, t0=None, ok=False):
    text(c, rot, x, y, 20, "mono", INK2, a, align="left")
    rrect(c, x, y + 14, w, 54, 8, "#0E1930", a)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y + 14, w, 54), 8, 8), paint(col, 0.6 * a, stroke=1.5))
    if t is not None:
        typed(c, val, x + 18, y + 52, 24, t, t0, cps=30, col=INK, a=a)
    else:
        text(c, val, x + 18, y + 52, 24, "mono", INK, a, align="left")
    if ok:
        check_icon(c, x + w - 30, y + 41, 14, a, LIME)


def detalhe(c, t, C, i, a):
    """painel da direita com o detalhe do passo i (mockups ilustrativos)"""
    x, y, w, h = 760, 250, 1010, 600
    if a <= 0:
        return
    cue = PASSOS[i][0]
    t0 = C[cue]
    panel(c, x, y, w, h, a, CYAN, label=f"passo {i + 1}")
    X = x + 60
    if i == 0:
        text(c, "PORTFÓLIO EMPRESARIAL", X, y + 110, 44, "black", INK, a, align="left")
        text(c, "o antigo Business Manager · business.facebook.com", X, y + 160, 24, "mono", INK2, a, align="left")
        for k, s in enumerate(("dono da conta do WhatsApp", "dos números", "do pagamento")):
            ak = a * ep(t, t0 + 1.0 + 0.4 * k, 0.4)
            chip(c, s.upper(), X, y + 260 + k * 80, VIOLET, ak, size=24)
    elif i == 1:
        text(c, "developers.facebook.com", X, y + 100, 26, "mono", CYAN, a, align="left")
        campo(c, X, y + 150, 880, "App Dashboard → Create App · caso de uso", "Connect with customers through WhatsApp", a,
              CYAN, t, t0 + 0.8)
        campo(c, X, y + 290, 880, "Business portfolio", "Minha Empresa", a * ep(t, t0 + 3.0, 0.4))
        selo(c, x + w - 40, y + h - 40, a, anchor="right", size=18)
    elif i == 2:
        terminal(c, X, y + 70, 880, 300, a, "API Setup · mockup", CYAN)
        code_lines(c, [[("From  ", DIM), ("número de teste da Meta", INK)],
                       [("Token ", DIM), ("temporário · ", INK), ("expira", GOLD)],
                       [("To    ", DIM), ("+55 11 9xxxx-xxxx", INK)],
                       [("▶ Send message", LIME)]], X + 40, y + 180, 28, t, t0 + 0.4, step=0.5, a=a)
        if t > t0 + 2.6:
            bubble(c, X + 300, y + 420, 560, "Hello World", a * ep(t, t0 + 2.6, 0.4), WA, size=28)
        selo(c, x + w - 40, y + h - 40, a, anchor="right", size=18)
    elif i == 3:
        ic_phone(c, X + 120, y + 300, 300, WA, a)
        text(c, "SEU NÚMERO", X + 120, y + 500, 26, "monob", WA, a)
        ab = a * ep(t, t0 + 1.4, 0.5)
        panel(c, X + 300, y + 90, 590, 150, ab, ROSE, k=12, fill=0.92, glow=False)
        text(c, "não pode estar ativo no app", X + 340, y + 155, 30, "bold", INK, ab, align="left")
        text(c, "apague a conta do app antes", X + 340, y + 200, 24, "mono", ROSE, ab, align="left")
        for k, s in enumerate(("NOME DE EXIBIÇÃO", "PIN DE DUAS ETAPAS")):
            ak = a * ep(t, t0 + 3.8 + 0.6 * k, 0.4)
            chip(c, s, X + 300, y + 320 + k * 90, LIME, ak, size=28, filled=True)
        text(c, "ou a coexistência (mais adiante)", X + 300, y + 520, 22, "mono", DIM, a * ep(t, t0 + 3.8, 0.4), align="left")
    elif i == 4:
        text(c, "Configurações do negócio → Usuários do sistema", X, y + 100, 26, "mono", CYAN, a, align="left")
        node(c, X + 90, y + 250, 70, None, None, VIOLET, a, t)
        ic_person(c, X + 90, y + 255, 70, VIOLET, a)
        text(c, "usuário do sistema", X + 90, y + 370, 22, "mono", INK2, a)
        arrow(c, X + 190, y + 250, X + 300, y + 250, INK2, a, 3, 12)
        terminal(c, X + 320, y + 160, 560, 260, a, "permissões do token", GOLD)
        code_lines(c, [[("✓ ", LIME), ("whatsapp_business_messaging", INK)],
                       [("✓ ", LIME), ("whatsapp_business_management", INK)],
                       [("✓ ", LIME), ("business_management", INK)]], X + 350, y + 270, 22, t, t0 + 2.2, step=0.6, a=a)
        chip(c, "EXPIRA: NUNCA · GUARDE NO SERVIDOR", X, y + 500, GOLD, a * ep(t, t0 + 4.0, 0.4), size=24, filled=True)
    elif i == 5:
        text(c, "WhatsApp → Configuration · webhook", X, y + 100, 26, "mono", CYAN, a, align="left")
        campo(c, X, y + 150, 880, "Callback URL", "https://seu-sistema.com/webhook", a, CYAN, t, t0 + 0.5)
        campo(c, X, y + 270, 880, "Verify token (você inventa)", "meu-token-secreto", a * ep(t, t0 + 2.4, 0.4), VIOLET,
              t, t0 + 2.6)
        ak = a * ep(t, C["09.b"] + 4.5, 0.4) if "09.b" in C else a
        campo(c, X, y + 390, 420, "Webhook field", "messages", ak, LIME, ok=True)
        selo(c, x + w - 40, y + h - 40, a, anchor="right", size=18)
    elif i == 6:
        ic_card(c, X + 160, y + 280, 220, GOLD, a)
        text(c, "FORMA DE PAGAMENTO", X + 360, y + 260, 40, "black", INK, a, align="left")
        text(c, "obrigatória para as mensagens cobradas", X + 360, y + 310, 24, "mono", INK2, a, align="left")
    else:
        text(c, "LIMITE DE CONTATOS EM 24H (FORA DA JANELA)", X, y + 100, 26, "monob", CYAN, a, align="left")
        steps = [("250", "início"), ("2.000", "após verificar"), ("10.000", "automático"), ("100.000", "automático"),
                 ("ILIMITADO", "automático")]
        for k, (v, s) in enumerate(steps):
            ak = a * ep(t, t0 + 0.6 + 0.35 * k, 0.4)
            bx = X + k * 180
            bh = 70 + k * 60
            col = LIME if k == 1 else (CYAN if k == 0 else VIOLET)
            rrect(c, bx, y + 520 - bh, 150, bh, 8, col, ak * (0.95 if k < 2 else 0.5))
            text(c, v, bx + 75, y + 500 - bh, 28 if k < 4 else 22, "black", col, ak)
            text(c, s, bx + 75, y + 560, 18, "mono", INK2, ak)
        chip(c, "POR PORTFÓLIO EMPRESARIAL", X, y + 150, INK2, a, size=20)


def _cur(t, C):
    cur = 0
    for i, (cue, _) in enumerate(PASSOS):
        if cue in C and t >= C[cue] - 0.3:
            cur = i
    return cur


def b_config1(c, t, C, B):
    with cam(c, t, B, 1.0, 1.02):
        head(c, t, B["start"], "CONFIGURAÇÃO", "DO ZERO AO PRIMEIRO ENVIO", CYAN)
        a0 = ep(t, C["08.t"] + 0.5, 0.5)
        cur = _cur(t, C)
        lista_passos(c, t, C, cur, a0)
        for i in range(4):
            a = ep(t, C[PASSOS[i][0]] - 0.3, 0.4) * (1 - prog(t, C[PASSOS[i + 1][0]] - 0.45, 0.25) if i < 3 else 1)
            detalhe(c, t, C, i, a)


def b_config2(c, t, C, B):
    with cam(c, t, B, 1.0, 1.02):
        head(c, t, B["start"], "CONFIGURAÇÃO", "TOKEN, WEBHOOK E LIMITES", CYAN)
        cur = _cur(t, C)
        lista_passos(c, t, C, cur, 1.0)
        for i in range(4, 8):
            t_in = C[PASSOS[i][0]] - 0.3
            t_out = C[PASSOS[i + 1][0]] - 0.45 if i < 7 else 1e9
            if i == 7:
                t_in = C["09.d"] - 0.3
            a = (ep(t, t_in, 0.4) if i > 4 else 1.0) * (1 - prog(t, t_out, 0.25))
            detalhe(c, t, C, i, a)


# ======================================================================  10 — CÓDIGO
REQ = [[("POST ", MAGENTA), ("https://graph.facebook.com/v26.0/", INK2)],
       [("     ", INK), ("{PHONE_NUMBER_ID}", CYAN), ("/messages", INK2)],
       [("Authorization: ", VIOLET), ("Bearer {TOKEN}", GOLD)],
       [("", INK)],
       [("{", INK)],
       [('  "messaging_product"', CYAN), (': "whatsapp",', INK)],
       [('  "to"', CYAN), (': "5511999999999",', INK)],
       [('  "type"', CYAN), (': "text",', INK)],
       [('  "text"', CYAN), (': { "body": "Seu pedido saiu!" }', INK)],
       [("}", INK)]]
RESP = [[('"messages"', CYAN), (': [{ "id": "wamid.HBgM..." }]', INK)]]
HOOK = [[('"from"', CYAN), (': "5511999999999",', INK)],
        [('"profile"', CYAN), (': { "name": "Ana" },', INK)],
        [('"type"', CYAN), (': "text",', INK)],
        [('"text"', CYAN), (': { "body": "Obrigada!" }', INK)]]


def b_codigo(c, t, C, B):
    with cam(c, t, B, 1.0, 1.02):
        head(c, t, B["start"], "NO CÓDIGO", "ENVIAR E RECEBER", VIOLET)
        aa = ep(t, C["10.a"], 0.5)
        if aa > 0:
            terminal(c, 150, 240, 1000, 620, aa, "enviar · HTTP", VIOLET)
            code_lines(c, REQ[:3], 190, 345, 25, t, C["10.a"] + 0.2, step=0.6, a=aa)
            code_lines(c, REQ[3:], 190, 345 + 3 * 36, 25, t, C["10.b"], step=0.35, a=aa)
        ac = ep(t, C["10.c"], 0.5)
        if ac > 0:
            terminal(c, 1190, 240, 580, 210, ac, "resposta", LIME)
            code_lines(c, RESP, 1215, 345, 19, t, C["10.c"] + 0.2, a=ac)
            chip(c, "ID DA MENSAGEM", 1215, 410, LIME, ac, size=20)
        ad = ep(t, C["10.d"], 0.5)
        if ad > 0:
            terminal(c, 1190, 480, 580, 380, ad, "webhook · recebido", CYAN)
            code_lines(c, HOOK, 1215, 585, 19, t, C["10.d"] + 0.8, step=0.6, a=ad)
            arrow(c, 1480, 820, 1480, 820, CYAN, 0)
            text(c, "Meta → seu servidor", 1480, 835, 20, "mono", DIM, ad)
        fonte(c, "trechos simplificados · Graph API v26.0 (29/07/2026) · números fictícios", ep(t, C["10.a"], 0.5), 895)


# ======================================================================  11 — ARQUITETURA DO MULTIATENDIMENTO
def b_arquitetura(c, t, C, B):
    with cam(c, t, B, 1.0, 1.03):
        head(c, t, B["start"], "MULTIATENDIMENTO", "UM SISTEMA NO MEIO", MAGENTA)
        Y = 470
        XC, XM, XS, XA = 230, 680, 1150, 1640
        aa = ep(t, C["11.a"], 0.5)
        if aa > 0:
            ic_phone(c, XC, Y, 200, WA, aa)
            text(c, "CLIENTE", XC, Y + 150, 30, "extrabold", INK, aa)
        ab = ep(t, C["11.b"], 0.5)
        if ab > 0:
            link(c, XC + 70, Y, XM - 100, Y, WA, ab, t, progress=ep(t, C["11.b"], 0.6), pulses=2)
            node(c, XM, Y, 95, "META", "Cloud API", CYAN, ab, t, glyph="API", gsize=40)
            link(c, XM + 100, Y, XS - 160, Y, CYAN, ab, t, progress=ep(t, C["11.b"] + 0.6, 0.6), pulses=2)
            chip(c, "WEBHOOK", (XM + XS) / 2 - 30, Y - 50, CYAN, ab, anchor="center", size=20)
        acx = ep(t, C["11.c"], 0.5)
        if acx > 0:
            panel(c, XS - 160, Y - 190, 320, 380, acx, MAGENTA, label="seu sistema")
            text(c, "FILA", XS, Y - 110, 26, "monob", MAGENTA, acx)
            for k in range(4):
                ak = acx * ep(t, C["11.c"] + 0.3 + 0.2 * k, 0.3)
                rrect(c, XS - 110, Y - 80 + k * 52, 220, 40, 8, "#1A1530", ak)
                c.drawCircle(XS - 85, Y - 60 + k * 52, 9, paint((WA, CYAN, GOLD, VIOLET)[k], ak))
                rrect(c, XS - 65, Y - 66 + k * 52, 140 - 20 * (k % 2), 12, 6, INK2, ak * 0.6)
            ak = acx * ep(t, C["11.c"] + 2.0, 0.4)
            x0 = XS - 250
            for k, s in enumerate(("POR EQUIPE", "ETIQUETA", "RODÍZIO")):
                _, x0 = chip(c, s, x0, Y + 240, MAGENTA, ak * ep(t, C["11.c"] + 2.0 + 0.5 * k, 0.3), size=20)
                x0 += 14
        for k in range(3):
            ak = ep(t, C["11.c"] + 1.0 + 0.3 * k, 0.4)
            if ak <= 0:
                continue
            yy = Y - 170 + k * 170
            link(c, XS + 160, Y, XA - 70, yy, MAGENTA, ak, t, pulses=1)
            panel(c, XA - 60, yy - 60, 220, 120, ak, (CYAN, LIME, GOLD)[k], k=12, fill=0.9, glow=False)
            ic_person(c, XA - 10, yy - 4, 56, (CYAN, LIME, GOLD)[k], ak)
            text(c, f"atend. {k + 1}", XA + 30, yy + 8, 20, "mono", INK2, ak, align="left")
        ad = ep(t, C["11.d"], 0.5)
        if ad > 0:
            chip(c, "RESPONDE NO PAINEL", XA + 50, Y + 260, LIME, ad, anchor="center", size=20, filled=True)
        ae = ep(t, C["11.e"], 0.5)
        if ae > 0:
            arrow(c, XS - 10, Y + 330, XM + 130, Y + 330, LIME, ae, 4, 16, progress=ep(t, C["11.e"], 0.8))
            c.drawLine(XM + 120, Y + 330, XM + 120, Y + 40, paint(LIME, ae * 0.7, stroke=3))
            text(c, "POST /messages", (XM + XS) / 2, Y + 310, 22, "monob", LIME, ae)
        af = ep(t, C["11.f"], 0.5)
        if af > 0:
            chip(c, "1 NÚMERO · VÁRIOS ATENDENTES", 760, 150, LIME, af, size=26, filled=True)


# ======================================================================  12 — CHATWOOT
CHECKS = ["Number access", "Template access", "Webhook callback", "Webhook subscription"]


def b_chatwoot(c, t, C, B):
    with cam(c, t, B, 1.0, 1.02):
        head(c, t, B["start"], "EXEMPLO · CÓDIGO ABERTO", "CHATWOOT + WHATSAPP CLOUD", LIME)
        a0 = ep(t, C["12.t"] + 0.6, 0.5)
        if a0 > 0:
            chip(c, "LICENÇA MIT (EXCETO A PASTA enterprise/)", 150, 255, LIME, a0, size=20)
            chip(c, "SELF-HOSTED OU NUVEM", 760, 255, INK2, a0, size=20)
        aa = ep(t, C["12.a"], 0.5)
        x, y, w, h = 150, 310, 1000, 540
        if aa > 0:
            panel(c, x, y, w, h, aa, LIME, label="nova caixa de entrada · mockup")
            text(c, "Configurações › Caixas de entrada › Adicionar", x + 50, y + 80, 24, "mono", INK2, aa, align="left")
            chip(c, "WHATSAPP CLOUD", x + 50, y + 135, WA, aa, size=24, filled=True)
            text(c, "configuração manual", x + 330, y + 145, 22, "mono", DIM, aa, align="left")
            selo(c, x + w - 30, y + 40, aa, anchor="right", size=18)
        tb = C["12.b"]
        for k, (rot, val, dt) in enumerate((("Phone Number ID", "1234567890", 0.9), ("WhatsApp Business Account ID",
                                                                                     "9876543210", 2.2),
                                            ("Permanent access token", "EAAG••••••••••••••••", 3.7))):
            ak = aa * ep(t, tb + dt - 0.3, 0.4)
            if ak > 0:
                campo(c, x + 50, y + 200 + k * 108, 900, rot, val, ak, LIME, t, tb + dt, ok=t > C["12.c"] + 0.4 + 0.5 * k)
        acx = ep(t, C["12.c"], 0.5)
        if acx > 0:
            panel(c, 1200, 310, 570, 360, acx, CYAN, label="o Chatwoot confere", glow=False)
            for k, s in enumerate(CHECKS):
                ak = acx * ep(t, C["12.c"] + 0.4 + 0.5 * k, 0.3)
                yy = 400 + k * 66
                check_icon(c, 1250, yy - 8, 16, ak, LIME)
                text(c, s, 1285, yy, 26, "medium", INK, ak, align="left")
                chip(c, "VERIFIED", 1740, yy - 8, LIME, ak, anchor="right", size=16)
            text(c, "e configura o webhook na Meta", 1485, 650, 22, "mono", CYAN, acx * ep(t, C["12.c"] + 2.4, 0.4))
        ad = ep(t, C["12.d"], 0.5)
        if ad > 0:
            panel(c, 1200, 700, 570, 150, ad, MAGENTA, label="atendentes", glow=False)
            for k in range(5):
                ak = ad * ep(t, C["12.d"] + 0.3 + 0.2 * k, 0.3)
                ic_person(c, 1270 + k * 105, 785, 64, (CYAN, LIME, GOLD, MAGENTA, VIOLET)[k], ak)
        fonte(c, "fonte: Chatwoot User Guide · “How to setup a WhatsApp channel (Manual flow)” · 29/10/2026",
              ep(t, C["12.a"], 0.5), 905)


# ======================================================================  13 — OPERAÇÃO
def b_operacao(c, t, C, B):
    with cam(c, t, B, 1.0, 1.03):
        head(c, t, B["start"], "NO DIA A DIA", "3 DICAS", GOLD)
        tips = [("13.a", "JANELA DE 24H", "passou do prazo → o atendente envia um modelo", LIME),
                ("13.b", "PERMISSÃO", "sem whatsapp_business_management, os modelos não aparecem", GOLD)]
        for i, (cue, k, v, col) in enumerate(tips):
            a, dy = rise(t, C[cue])
            a *= 1 - prog(t, C["13.c"] - 0.2, 0.4)
            if a <= 0:
                continue
            y = 280 + i * 230 + dy
            panel(c, 150, y, 1620, 190, a, col, k=16, fill=0.88)
            glow_text(c, f"0{i + 1}", 210, y + 115, 64, "black", col, a, align="left", glow=0.4)
            text(c, k, 340, y + 80, 30, "monob", col, a, align="left")
            text(c, v, 340, y + 135, 34, "bold", INK, a, align="left")
        ac = ep(t, C["13.c"], 0.5)
        if ac > 0:
            glow_text(c, "03", 210, 330, 64, "black", VIOLET, ac, align="left", glow=0.4)
            text(c, "COEXISTÊNCIA", 340, 310, 30, "monob", VIOLET, ac, align="left")
            text(c, "o mesmo número no app e na API", 340, 355, 34, "bold", INK, ac, align="left")
            Y = 600
            ic_phone(c, 420, Y, 230, WA, ac)
            text(c, "app WhatsApp Business", 420, Y + 160, 22, "mono", INK2, ac)
            node(c, 960, Y, 90, None, None, LIME, ac, t, glyph="+55", gsize=36)
            text(c, "1 número", 960, Y + 140, 24, "monob", LIME, ac)
            node(c, 1500, Y, 90, None, None, CYAN, ac, t, glyph="API", gsize=40)
            text(c, "Cloud API + multiatendimento", 1500, Y + 140, 22, "mono", INK2, ac)
            link(c, 520, Y, 860, Y, LIME, ac, t, pulses=2)
            link(c, 1060, Y, 1400, Y, LIME, ac, t, pulses=2)
            chip(c, "ATÉ 6 MESES DE HISTÓRICO", 960, 470, VIOLET, ac * ep(t, C["13.c"] + 3.0, 0.4), anchor="center", size=22,
                 filled=True)
        ad = ep(t, C["13.d"], 0.5)
        if ad > 0:
            chip(c, "VIA CADASTRO DE UM PARCEIRO (EMBEDDED SIGNUP) · NÃO NO FLUXO MANUAL", W / 2, 840, GOLD, ad,
                 anchor="center", size=20)
        fonte(c, "fontes: docs da Meta (coexistence) e do Chatwoot · 29/10/2026", ep(t, C["13.a"], 0.5), 895)


# ======================================================================  14 — CUIDADOS
def b_cuidados(c, t, C, B):
    with cam(c, t, B, 1.0, 1.03):
        head(c, t, B["start"], "CUIDADOS", "PARA NÃO PERDER O NÚMERO", ROSE)
        rows = [("14.a", "CONSENTIMENTO", "a pessoa precisa aceitar antes de você mandar primeiro", CYAN, "lock"),
                ("14.b", "QUALIDADE", "modelo mal avaliado derruba a qualidade e trava o limite", GOLD, "warn"),
                ("14.c", "TOKEN", "fica no servidor · nunca no front-end", ROSE, "lock"),
                ("14.d", "ASSINATURA", "valide o cabeçalho X-Hub-Signature-256 de cada webhook", LIME, "lock")]
        for i, (cue, k, v, col, ic) in enumerate(rows):
            a, dy = rise(t, C[cue])
            if a <= 0:
                continue
            y = 260 + i * 145 + dy
            panel(c, 150, y, 1620, 120, a, col, k=14, fill=0.85, glow=False)
            (ic_lock if ic == "lock" else ic_warn)(c, 230, y + 60, 60, col, a)
            text(c, k, 310, y + 52, 28, "black", col, a, align="left")
            text(c, v, 310, y + 94, 30, "bold", INK, a, align="left")
        fonte(c, "WhatsApp Business Messaging Policy · docs de webhooks da Meta", ep(t, C["14.a"], 0.5), 870)


# ======================================================================  15 — RESUMO
RES = [("15.a", "oficial, hospedada pela Meta, sem mensalidade", CYAN),
       ("15.b", "paga por mensagem: marketing R$ 0,3217 · demais R$ 0,035", GOLD),
       ("15.c", "1.000 respostas de atendimento grátis/mês por número", LIME),
       ("15.d", "app → número → token permanente → webhook", VIOLET),
       ("15.e", "multiatendimento: 1 número, vários atendentes", MAGENTA)]


def b_resumo(c, t, C, B):
    with cam(c, t, B, 1.0, 1.03):
        head(c, t, B["start"], "RESUMO", "API OFICIAL EM 5 PONTOS", CYAN)
        for i, (cue, s, col) in enumerate(RES):
            a, dy = rise(t, C[cue])
            if a <= 0:
                continue
            y = 250 + i * 118 + dy
            panel(c, 150, y, 1620, 100, a, col, k=14, fill=0.85, glow=False)
            check_icon(c, 220, y + 50, 26, a, col)
            text(c, s, 280, y + 62, 36, "bold", INK, a, align="left")


# ======================================================================  CTA + FONTES
def b_cta(c, t, C, B):
    head(c, t, B["start"], "TECH//014", "OBRIGADO POR ASSISTIR", CYAN)
    cta(c, t, C["16.like"], C["16.sub"], C["16.bell"], C["16.com"], C["16.bye"],
        "Qual sistema de atendimento você usa com o WhatsApp?")


FONTES = [
    ("Meta (oficial)", "WhatsApp Business Platform · Pricing · developers.facebook.com/docs/whatsapp/pricing", "29/10/2026"),
    ("Meta (oficial)", "Rate card BRL e volume tiers BRL · effective October 1, 2026", "01/10/2026"),
    ("Meta (oficial)", "Cloud API · Get started · developers.facebook.com/docs/whatsapp/cloud-api/get-started", "29/10/2026"),
    ("Meta (oficial)", "Business phone numbers · Messaging limits", "29/10/2026"),
    ("Meta (oficial)", "Embedded Signup · Onboarding WhatsApp Business app users (coexistence)", "29/10/2026"),
    ("Meta (oficial)", "Graph API changelog · v26.0", "29/07/2026"),
    ("Chatwoot", "User Guide · How to setup a WhatsApp channel (Manual flow)", "29/10/2026"),
    ("Chatwoot", "github.com/chatwoot/chatwoot · LICENSE (MIT, exceto enterprise/)", "29/10/2026"),
]


def b_fontes(c, t, C, B):
    head(c, t, B["start"], "CRÉDITOS", "FONTES", CYAN)
    a0 = ep(t, B["start"] + 0.2, 0.6)
    panel(c, 150, 230, 1620, 640, a0, CYAN, label="consultadas em 29/10/2026")
    for i, (v, tit, d) in enumerate(FONTES):
        a = ep(t, B["start"] + 0.4 + 0.12 * i, 0.4)
        y = 310 + i * 62
        text(c, v, 200, y, 26, "extrabold", CYAN, a, align="left")
        tt = tit if text_w(tit, "medium", 24) < 1080 else wrap(tit, "medium", 24, 1040)[0] + "…"
        text(c, tt, 440, y, 24, "medium", INK, a, align="left")
        text(c, d, 1720, y, 24, "mono", INK2, a, align="right")
    ab = ep(t, B["start"] + 1.8, 0.6)
    text(c, "telas da Meta e do Chatwoot: mockups ilustrativos · sem logos de terceiros · narração com voz sintética (IA)",
         W / 2, 840, 20, "mono", DIM, ab)


BLOCKS = dict(gancho=b_gancho, oque=b_oque, janela=b_janela, precos=b_precos, servico=b_servico, simulacao=b_simulacao,
              detalhes=b_detalhes, config1=b_config1, config2=b_config2, codigo=b_codigo, arquitetura=b_arquitetura,
              chatwoot=b_chatwoot, operacao=b_operacao, cuidados=b_cuidados, resumo=b_resumo, cta=b_cta, fontes=b_fontes)
