"""Visual do vídeo Tecnologia 010 — Claude Duet, o agente proativo da Anthropic. Tema 'tech'.
Só motion graphics próprios. Nenhuma captura de tela nem logo de terceiros: interfaces do Duet aparecem apenas como
MOCKUP desenhado aqui, sempre com o selo ILUSTRATIVO. Nomes de apps aparecem só como texto."""
import math
from contextlib import contextmanager
import skia
import motor
import tech
from motor import *  # noqa
from tech import *  # noqa

# neste Linux não há Consolas: a fonte mono do tech.py não carrega. Usa DejaVu Sans Mono (como no 009).
motor.PESOS["mono"] = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono"
motor.PESOS["monob"] = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold"

tech.SERIE = "TECH//010 · CLAUDE DUET"
MARCA = ""
ARQUIVO_FINAL = "tecnologia_010_claude_duet.mp4"
# som padrão do canal (_ferramentas/som_tech.py); aqui só os efeitos que fogem do "pop" de cada cue
SOM = dict(sfx={
    "01.a": "glitch", "01.b": [f"pop@+{0.35 * k:.2f}" for k in range(5)], "01.c": ["data@+0.3", "notif@+2.2"],
    "01.d": "impact", "05.c": ["typing@+0.2", "pop@+1.4", "pop@+1.9", "pop@+2.4"], "05.d": "notif", "08.d": "notif@+1.0",
    "10.a": "lock", "10.b": "lock", "10.c": "lock", "10.d": "lock", "10.e": "alert", "10.f": "deny", "10.g": "deny",
    "11.a": "lock", "11.b": "deny", "11.c": "alert", "11.d": "click",
    "12.a": "alert", "12.b": "alert", "12.c": "alert", "12.d": "alert",
    "14.a": "confirm", "14.b": "confirm", "14.c": "confirm", "14.d": "confirm", "14.e": "confirm"})
BACKGROUND, CAPTION, OVERLAY = tech.background, tech.caption, tech.overlay


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
    """selo âmbar obrigatório em qualquer mockup"""
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


# ---------------------------------------------------------------- ícones vetoriais simples (desenhados aqui)
def ic_mail(c, cx, cy, s, col, a):
    w, h = s, s * 0.68
    c.drawRect(skia.Rect.MakeXYWH(cx - w / 2, cy - h / 2, w, h), paint(col, a, stroke=s * 0.07))
    p = skia.Path(); p.moveTo(cx - w / 2, cy - h / 2); p.lineTo(cx, cy + h * 0.08); p.lineTo(cx + w / 2, cy - h / 2)
    pp = paint(col, a, stroke=s * 0.07); pp.setStrokeJoin(skia.Paint.kRound_Join)
    c.drawPath(p, pp)


def ic_cal(c, cx, cy, s, col, a):
    w = s
    c.drawRect(skia.Rect.MakeXYWH(cx - w / 2, cy - w * 0.42, w, w * 0.84), paint(col, a, stroke=s * 0.07))
    c.drawRect(skia.Rect.MakeXYWH(cx - w / 2, cy - w * 0.42, w, w * 0.2), paint(col, a))
    for i in range(3):
        for j in range(2):
            c.drawRect(skia.Rect.MakeXYWH(cx - w * 0.33 + i * w * 0.25, cy - w * 0.05 + j * w * 0.2, w * 0.14, w * 0.12),
                       paint(col, a))
    for dx in (-0.25, 0.25):
        c.drawLine(cx + dx * w, cy - w * 0.52, cx + dx * w, cy - w * 0.36, paint(col, a, stroke=s * 0.08, cap_round=True))


def ic_chat(c, cx, cy, s, col, a):
    r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - s / 2, cy - s * 0.4, s, s * 0.62), s * 0.14, s * 0.14)
    c.drawRRect(r, paint(col, a, stroke=s * 0.07))
    p = skia.Path(); p.moveTo(cx - s * 0.22, cy + s * 0.22); p.lineTo(cx - s * 0.3, cy + s * 0.42); p.lineTo(cx, cy + s * 0.22)
    c.drawPath(p, paint(col, a))
    for k in range(3):
        c.drawCircle(cx - s * 0.2 + k * s * 0.2, cy - s * 0.09, s * 0.055, paint(col, a))


def ic_sheet(c, cx, cy, s, col, a):
    c.drawRect(skia.Rect.MakeXYWH(cx - s / 2, cy - s * 0.42, s, s * 0.84), paint(col, a, stroke=s * 0.07))
    for k in (1, 2, 3):
        y = cy - s * 0.42 + k * s * 0.21
        c.drawLine(cx - s / 2, y, cx + s / 2, y, paint(col, a, stroke=s * 0.04))
    c.drawLine(cx - s * 0.17, cy - s * 0.42, cx - s * 0.17, cy + s * 0.42, paint(col, a, stroke=s * 0.04))


def ic_receipt(c, cx, cy, s, col, a):
    w, h = s * 0.7, s * 0.9
    p = skia.Path(); p.moveTo(cx - w / 2, cy - h / 2); p.lineTo(cx + w / 2, cy - h / 2); p.lineTo(cx + w / 2, cy + h / 2)
    n = 5
    for k in range(n):
        x1 = cx + w / 2 - (k + 0.5) * w / n
        x2 = cx + w / 2 - (k + 1) * w / n
        p.lineTo(x1, cy + h / 2 - s * 0.08); p.lineTo(x2, cy + h / 2)
    p.close()
    pp = paint(col, a, stroke=s * 0.07); pp.setStrokeJoin(skia.Paint.kRound_Join)
    c.drawPath(p, pp)
    for k in range(3):
        c.drawLine(cx - w * 0.28, cy - h * 0.25 + k * h * 0.2, cx + w * 0.28, cy - h * 0.25 + k * h * 0.2,
                   paint(col, a, stroke=s * 0.05, cap_round=True))


def ic_laptop(c, cx, cy, s, col, a):
    w, h = s, s * 0.62
    rrect(c, cx - w / 2, cy - h / 2 - s * 0.1, w, h, 6, "#0B1426", a)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2, cy - h / 2 - s * 0.1, w, h), 6, 6),
                paint(col, a, stroke=s * 0.04))
    rrect(c, cx - w * 0.62, cy + h / 2 - s * 0.08, w * 1.24, s * 0.08, 4, col, a)


def ic_phone(c, cx, cy, s, col, a):
    w, h = s * 0.55, s
    rrect(c, cx - w / 2, cy - h / 2, w, h, s * 0.08, "#0B1426", a)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2, cy - h / 2, w, h), s * 0.08, s * 0.08),
                paint(col, a, stroke=s * 0.04))
    c.drawCircle(cx, cy + h / 2 - s * 0.08, s * 0.03, paint(col, a))


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


ICONS = dict(mail=ic_mail, cal=ic_cal, chat=ic_chat, sheet=ic_sheet, receipt=ic_receipt)


def notif(c, x, y, w, a, title, body, col=CYAN, size=26):
    """bolha de notificação (mockup)"""
    if a <= 0:
        return
    h = 112
    panel(c, x, y, w, h, a, col, k=14, fill=0.92)
    c.drawCircle(x + 46, y + h / 2, 20, paint(col, a))
    text(c, title, x + 84, y + 44, 20, "monob", col, a, align="left")
    text(c, body, x + 84, y + 82, size, "bold", INK, a, align="left")


# ======================================================================  01 — GANCHO
APPS = [("mail", "E-MAIL", CYAN, (330, 330)), ("cal", "AGENDA", VIOLET, (640, 250)),
        ("chat", "MENSAGENS", MAGENTA, (1280, 250)), ("sheet", "PLANILHA", LIME, (1590, 330)),
        ("receipt", "FATURAS", GOLD, (960, 220))]


def app_tile(c, kind, lab, col, x, y, a, t, badge=None, s=1.0):
    if a <= 0:
        return
    w = 190 * s
    panel(c, x - w / 2, y - w / 2, w, w, a, col, k=18 * s, fill=0.88)
    ICONS[kind](c, x, y - 18 * s, 70 * s, col, a)
    text(c, lab, x, y + 62 * s, 20 * s, "monob", INK2, a)
    if badge:
        bx, by = x + w / 2 - 6, y - w / 2 + 6
        c.drawCircle(bx, by, 22 * s, blur_paint(ROSE, 0.5 * a, 8))
        c.drawCircle(bx, by, 20 * s, paint(ROSE, a))
        text_mid(c, badge, bx, by, 22 * s, "black", "#FFFFFF", a)


def b_gancho(c, t, C, B):
    with cam(c, t, B, 1.0, 1.05):
        ta, tb, tc, td = C["01.a"], C["01.b"], C["01.c"], C["01.d"]
        aq = ep(t, ta, 0.6) * (1 - prog(t, tb + 0.2, 0.5))
        if aq > 0:
            glow_text(c, "QUANTOS APPS", W / 2, 470, 120, "black", INK, aq, glow=0.2)
            glow_text(c, "ANTES DE TRABALHAR?", W / 2, 600, 92, "black", CYAN, aq, glow=0.35)
        conv = ep(t, tc + 0.3, 1.4)
        out = 1 - prog(t, td - 0.1, 0.5)
        badges = ["12", "5", "27", "3", "2"]
        for k, (kind, lab, col, (x0, y0)) in enumerate(APPS):
            a = ep(t, tb + 0.35 * k, 0.5) * out
            if a <= 0:
                continue
            # posição espalhada (com tremor de "bagunça") → converge para o centro
            jx = 8 * math.sin(t * 3 + k) * (1 - conv)
            yy = y0 + 280 + 20 * math.sin(t * 1.4 + k * 1.7)
            x = lerp(x0, W / 2, conv * 0.55) + jx
            y = lerp(yy, 470, conv * 0.4)
            app_tile(c, kind, lab, col, x, y, a * (1 - 0.55 * conv), t, badge=badges[k] if conv < 0.5 else None,
                     s=1.0 - 0.25 * conv)
            if conv > 0:
                link(c, x, y, W / 2, 470, col, a * conv, t, pulses=2)
        if conv > 0:
            node(c, W / 2, 470, 120, None, None, CYAN, conv * out, t)
            glow_text(c, "IA", W / 2, 498, 80, "black", CYAN, conv * out, glow=0.5)
            notif(c, W / 2 - 330, 650, 660, ep(t, tc + 2.2, 0.5) * out, "AGORA",
                  "Só isto precisa de você hoje.", CYAN, 28)
            text(c, "mockup ilustrativo", W / 2, 800, 20, "mono", DIM, ep(t, tc + 2.2, 0.5) * out)
        ad = ep(t, td, 0.7)
        if ad > 0:
            chip(c, "ANTHROPIC · 21/10/2026", W / 2, 330, CYAN, ad, anchor="center", size=28)
            s = 1 + 0.03 * (1 - ad)
            glow_text(c, "CLAUDE DUET", W / 2, 520, 170 * s, "black", INK, ad, glow=0.3)
            glow_line(c, W / 2 - 520, 570, W / 2 + 520, 570, CYAN, ad, 4, progress=ep(t, td + 0.3, 0.9))
            text(c, "o agente proativo da Anthropic", W / 2, 650, 44, "mono", CYAN, ep(t, td + 0.6, 0.6))
            chip(c, "PRÉVIA DE PESQUISA", W / 2, 750, GOLD, ep(t, td + 1.0, 0.5), anchor="center", size=26, filled=True)


# ======================================================================  02 — O QUE É
VERBOS = [("02.a", "VEM ATÉ VOCÊ", "com o que precisa da sua atenção", CYAN),
          ("02.b", "COMPLETA TAREFAS", "as que você pede", VIOLET),
          ("02.c", "CONTINUA TRABALHANDO", "quando você se afasta", LIME),
          ("02.d", "PERGUNTA ANTES", "de agir em seu nome", GOLD)]


def b_oque(c, t, C, B):
    with cam(c, t, B, 1.0, 1.035, -10, 0):
        head(c, t, B["start"], "O QUE É", "UM AGENTE PROATIVO", CYAN)
        a0 = ep(t, C["02.t"] + 0.2, 0.6)
        # app separado: dois "apps" lado a lado
        if a0 > 0:
            panel(c, 150, 250, 560, 560, a0, CYAN, label="app próprio")
            node(c, 430, 470, 120, None, None, CYAN, a0, t)
            glow_text(c, "DUET", 430, 488, 56, "black", CYAN, a0, glow=0.5)
            text(c, "separado do app", 430, 650, 28, "medium", INK2, a0)
            text(c, "principal do Claude", 430, 690, 28, "medium", INK2, a0)
            af = ep(t, C["02.f"], 0.5)
            chip(c, "MODELO · CLAUDE OPUS 5.5", 430, 770, VIOLET, af, anchor="center", size=24, filled=True)
        for k, (cue, tit, sub, col) in enumerate(VERBOS):
            a, dy = rise(t, C[cue])
            if a <= 0:
                continue
            y = 250 + k * 118 + dy
            panel(c, 790, y, 980, 100, a, col, k=14, fill=0.85, glow=False)
            glow_text(c, f"0{k + 1}", 840, y + 66, 40, "black", col, a, glow=0.4)
            text(c, tit, 920, y + 48, 34, "black", INK, a, align="left")
            text(c, sub, 920, y + 82, 24, "mono", INK2, a, align="left")
        ae = ep(t, C["02.e"], 0.5)
        if ae > 0:
            text(c, "FOCO:", 790, 765, 26, "monob", DIM, ae, align="left")
            x0, x1 = chip(c, "PROFISSIONAIS", 890, 757, LIME, ae, size=26)
            chip(c, "PEQUENAS EMPRESAS", x1 + 20, 757, LIME, ep(t, C["02.e"] + 0.5, 0.5), size=26)
        fonte(c, "citação: anúncio oficial · claude.com · 21/10/2026", ep(t, C["02.a"], 0.5), 850)


# ======================================================================  03 — FLUXO
FX = [215, 600, 960, 1320, 1705]
FY = 470
FN = [("APPS", "conectados", CYAN), ("DUET", "lê e organiza", VIOLET), ("BRIEF", "ou alerta", MAGENTA),
      ("VOCÊ", "aprova", GOLD), ("AÇÃO", "executada", LIME)]


def fluxo(c, t, cues, a_all=1.0, hi=-1):
    for k, (lab, sub, col) in enumerate(FN):
        a = ep(t, cues[k], 0.6) * a_all
        if k > 0:
            pa = min(a, ep(t, cues[k - 1], 0.5) * a_all)
            link(c, FX[k - 1] + 100, FY, FX[k] - 100, FY, FN[k - 1][2], pa, t, progress=ep(t, cues[k], 0.6), pulses=3)
        if a <= 0:
            continue
        node(c, FX[k], FY, 92, None, None, col, a * (1.0 if hi in (-1, k) else 0.5), t)
        glow_text(c, lab, FX[k], FY + 14, 38 if len(lab) <= 4 else 32, "black", col, a, glow=0.4)
        text(c, sub, FX[k], FY + 140, 28, "mono", INK2, a)
        if k == 3:  # pessoa
            c.drawCircle(FX[k], FY - 150, 22, paint(col, a))
            c.drawPath(_ombro(FX[k], FY - 112), paint(col, a))


def _ombro(cx, y):
    p = skia.Path()
    p.addArc(skia.Rect.MakeXYWH(cx - 38, y, 76, 60), 180, 180)
    p.close()
    return p


def b_fluxo(c, t, C, B):
    with cam(c, t, B, 1.0, 1.03):
        head(c, t, B["start"], "COMO FUNCIONA", "DOS SEUS APPS À AÇÃO", VIOLET)
        cues = [C["03.a"], C["03.b"], C["03.c"], C["03.d"], C["03.e"]]
        fluxo(c, t, cues)
        # herança da conta Claude
        ah = fade(t, C["03.a"] + 1.2, C["03.d"] - 0.3)
        if ah > 0:
            panel(c, 150, 690, 1000, 130, ah, VIOLET, k=14, label="herda da sua conta Claude", glow=False)
            for k, s in enumerate(("MEMÓRIA", "SKILLS", "APPS CONECTADOS")):
                chip(c, s, 200 + k * 260, 765, VIOLET, ah * ep(t, C["03.a"] + 1.6 + 0.4 * k, 0.4), size=24)
        ad = ep(t, C["03.d"], 0.5)
        if ad > 0:
            # cartão de aprovação (mockup)
            x, y = 1080, 640
            panel(c, x, y, 690, 190, ad, GOLD, k=14, fill=0.92, label="aprovação · mockup")
            text(c, "Enviar o lembrete de fatura?", x + 40, y + 70, 30, "bold", INK, ad, align="left")
            chip(c, "APROVAR", x + 40, y + 132, LIME, ad, size=24, filled=ep(t, C["03.e"], 0.3) > 0.5)
            chip(c, "EDITAR", x + 230, y + 132, INK2, ad, size=24)
            chip(c, "RECUSAR", x + 400, y + 132, ROSE, ad, size=24)
            selo(c, x + 690, y + 222, ad, anchor="right", size=17)
        af = ep(t, C["03.f"], 0.5)
        if af > 0:
            chip(c, "1 CONVERSA CONTÍNUA · TEXTO OU VOZ", 150, 260, CYAN, af, size=26, filled=True)


# ======================================================================  04 — BRIEF + CICLO
BRIEF = [("3 e-mails pedem resposta", CYAN), ("Reunião às 10h ainda sem pauta", VIOLET),
         ("2 faturas vencem esta semana", GOLD), ("1 mensagem marcada como urgente", ROSE)]


def brief_card(c, x, y, a, t, t0):
    """MOCKUP genérico de 'brief da manhã' (itens inventados como exemplo)"""
    if a <= 0:
        return
    w, h = 720, 560
    panel(c, x, y, w, h, a, CYAN, label="duet · mockup")
    text(c, "BRIEF DA MANHÃ", x + 50, y + 80, 38, "black", INK, a, align="left")
    text(c, "08:00 · o que importa hoje", x + 50, y + 120, 22, "mono", INK2, a, align="left")
    c.drawLine(x + 50, y + 150, x + w - 50, y + 150, paint(CYAN, 0.3 * a, stroke=1.5))
    for i, (s, col) in enumerate(BRIEF):
        ai = a * ep(t, t0 + 0.5 + 0.35 * i, 0.4)
        yy = y + 210 + i * 80
        rrect(c, x + 50, yy - 34, w - 100, 62, 8, "#0E1930", ai)
        c.drawRect(skia.Rect.MakeXYWH(x + 50, yy - 34, 6, 62), paint(col, ai))
        text(c, s, x + 80, yy + 8, 28, "bold", INK, ai, align="left")
    selo(c, x + w, y + h + 34, a, "ILUSTRATIVO · ITENS DE EXEMPLO", anchor="right", size=18)


def b_ciclo(c, t, C, B):
    with cam(c, t, B, 1.0, 1.03):
        head(c, t, B["start"], "BRIEF E ALERTAS", "DE MANHÃ E A CADA POUCAS HORAS", CYAN)
        aa = ep(t, C["04.a"], 0.6)
        brief_card(c, 150, 260, aa, t, C["04.a"])
        ab = ep(t, C["04.b"], 0.6)
        if ab > 0:
            cx, cy, R = 1420, 520, 220
            c.drawCircle(cx, cy, R, paint(CYAN, 0.25 * ab, stroke=3))
            sweep = (t - C["04.b"]) * 40
            p = skia.Path(); p.addArc(skia.Rect.MakeXYWH(cx - R, cy - R, 2 * R, 2 * R), -90, min(360, sweep) if sweep < 360 else 360)
            c.drawPath(p, blur_paint(CYAN, 0.5 * ab, 8, stroke=8))
            c.drawPath(p, paint(CYAN, ab, stroke=4))
            # pontos de checagem espaçados (sem escala exata: "a cada poucas horas")
            for k in range(6):
                ang = -math.pi / 2 + k * math.pi / 3
                px, py = cx + R * math.cos(ang), cy + R * math.sin(ang)
                hit = ((sweep % 360) / 60) >= k or sweep >= 360
                c.drawCircle(px, py, 16, paint(PANEL, ab))
                c.drawCircle(px, py, 16, paint(LIME if hit else DIM, ab, stroke=3))
                if hit:
                    c.drawCircle(px, py, 7, paint(LIME, ab))
            ang = -math.pi / 2 + math.radians(sweep)
            c.drawLine(cx, cy, cx + (R - 40) * math.cos(ang), cy + (R - 40) * math.sin(ang), paint(INK, ab, stroke=4, cap_round=True))
            c.drawCircle(cx, cy, 10, paint(INK, ab))
            text(c, "CHECAGEM", cx, cy - R - 40, 22, "monob", LIME, ab)
            glow_text(c, "a cada poucas horas", cx, cy + R + 70, 34, "bold", INK, ab, glow=0.15)
            text(c, "intervalo exato não divulgado", cx, cy + R + 108, 20, "mono", DIM, ab)
        acx = fade(t, C["04.c"], C["04.d"] - 0.2)
        if acx > 0:
            chip(c, "SEM PARAR = GASTA O LIMITE DO PLANO", 1420, 215, GOLD, acx, anchor="center", size=22, filled=True)
        ad = ep(t, C["04.d"], 0.5)
        if ad > 0:
            chip(c, "VOCÊ ESCOLHE: ASSUNTO + FREQUÊNCIA", 1420, 215, LIME, ad, anchor="center", size=22, filled=True)


# ======================================================================  05 — NUVEM
def browser_win(c, x, y, w, h, a, t, t0):
    rrect(c, x, y, w, h, 10, "#0B1426", a)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 10, 10), paint(VIOLET, 0.8 * a, stroke=2))
    for i, cc in enumerate((ROSE, GOLD, LIME)):
        c.drawCircle(x + 24 + i * 22, y + 22, 6, paint(cc, a))
    rrect(c, x + 100, y + 12, w - 130, 22, 11, "#16223D", a)
    # "dashboard" sendo montado
    u = clamp((t - t0) / 6)
    for k in range(6):
        v = (0.3 + 0.6 * abs(math.sin(k * 1.7 + 0.4))) * clamp(u * 6 - k)
        bw = (w - 80) / 6 * 0.6
        bx = x + 40 + k * (w - 80) / 6
        rrect(c, bx, y + h - 30 - (h - 90) * v, bw, (h - 90) * v, 4, (CYAN, VIOLET, LIME)[k % 3], a)


def b_nuvem(c, t, C, B):
    with cam(c, t, B, 1.0, 1.04):
        head(c, t, B["start"], "TRABALHA NA NUVEM", "UMA MÁQUINA SÓ DELE", LIME)
        aa = ep(t, C["05.a"], 0.7)
        if aa > 0:
            ic_cloud(c, 1110, 470, 760, VIOLET, aa, fill=0.85)
            text(c, "MÁQUINA VIRTUAL", 1110, 390, 28, "monob", VIOLET, aa)
            browser_win(c, 900, 420, 420, 230, aa, t, C["05.a"] + 0.5)
            text(c, "navegador próprio", 1110, 690, 24, "mono", INK2, aa)
        ab = ep(t, C["05.b"], 0.6)
        if ab > 0:
            for k, (fn, lab) in enumerate(((ic_laptop, "notebook"), (ic_phone, "celular"))):
                x = 260 + k * 230
                fn(c, x, 470, 150 if k == 0 else 130, DIM, ab)
                chip(c, "OFF", x, 590, DIM, ab, anchor="center", size=22)
                text(c, lab, x, 650, 24, "mono", DIM, ab)
            text(c, "podem ficar desligados", 375, 700, 28, "bold", INK, ab)
        acx = ep(t, C["05.c"], 0.5)
        if acx > 0:
            panel(c, 150, 260, 600, 90, acx, CYAN, k=12, fill=0.92, glow=False)
            typed(c, "Monte um dashboard de vendas", 180, 318, 28, t, C["05.c"] + 0.2, cps=22, col=INK, a=acx, peso="medium")
            text(c, "exemplo de pedido", 750, 380, 18, "mono", DIM, acx, align="right")
            for k, s in enumerate(("escolhe os apps", "define os passos", "executa em segundo plano")):
                ak = acx * ep(t, C["05.c"] + 1.4 + 0.5 * k, 0.4)
                x = 900 + k * 290
                chip(c, s.upper(), x, 790, VIOLET, ak, anchor="center", size=19)
        ad = ep(t, C["05.d"], 0.5)
        if ad > 0:
            notif(c, 150, 750, 560, ad, "DUET · MOCKUP", "Tarefa pronta para revisão", LIME, 26)


# ======================================================================  06 — TAREFAS
TAREFAS = [("06.a", "MARCAR REUNIÕES", CYAN), ("06.b", "DASHBOARDS", VIOLET), ("06.c", "PREVISÕES FINANCEIRAS E DE VENDAS", MAGENTA),
           ("06.d", "PROTÓTIPOS", GOLD), ("06.e", "APLICAÇÕES WEB", LIME)]


def b_tarefas(c, t, C, B):
    with cam(c, t, B, 1.0, 1.035):
        head(c, t, B["start"], "O QUE ELE FAZ", "DO SIMPLES AO COMPLEXO", MAGENTA)
        tf = C["06.f"]
        out = 1 - prog(t, tf - 0.2, 0.5)
        for k, (cue, lab, col) in enumerate(TAREFAS):
            a, dy = rise(t, C[cue])
            a *= out
            if a <= 0:
                continue
            x = 150 + k * 330
            h = 150 + k * 95
            y = 840 - h + dy
            panel(c, x, y, 300, h, a, col, k=14, fill=0.85)
            glow_text(c, f"0{k + 1}", x + 30, y + 60, 40, "black", col, a, align="left", glow=0.4)
            for i, ln in enumerate(wrap(lab, "black", 28, 250)):
                text(c, ln, x + 30, y + 110 + i * 34, 28, "black", INK, a, align="left")
        ar = ep(t, C["06.a"] + 0.5, 0.6) * out
        if ar > 0:
            arrow(c, 200, 300, 1600, 300, DIM, ar * 0.6, 3, 14, progress=ep(t, C["06.a"] + 0.5, 6.0))
            text(c, "simples", 200, 280, 22, "mono", DIM, ar, align="left")
            text(c, "complexo", 1600, 280, 22, "mono", DIM, ep(t, C["06.e"], 0.5) * out, align="right")
        af = ep(t, tf, 0.7)
        if af > 0:
            n = int(6000 * ep(t, tf, 1.6))
            glow_text(c, f"{n:,}".replace(",", ".") + "+", W / 2, 560, 220, "black", CYAN, af, glow=0.35)
            text(c, "CONECTORES E PLUGINS", W / 2, 650, 44, "black", INK, af)
            text(c, "no Claude Marketplace · número da Anthropic", W / 2, 710, 26, "mono", INK2, af)


# ======================================================================  07 — CONECTORES (exemplos oficiais)
EXS = [("07.a", "GMAIL + SLACK", "mensagens que você deixou passar", "rascunho de resposta", CYAN),
       ("07.b", "QUICKBOOKS / STRIPE", "faturas em aberto", "lembretes redigidos", GOLD),
       ("07.c", "GUSTO", "folha de pagamento", "preparada para você", VIOLET),
       ("07.d", "LINKEDIN", "vaga escrita pelo Duet", "publica após você editar e aprovar", MAGENTA),
       ("07.e", "LINK (STRIPE) · SHOP PAY", "compras para o negócio", "paga com cartão virtual", LIME)]


def b_conectores(c, t, C, B):
    with cam(c, t, B, 1.0, 1.03):
        head(c, t, B["start"], "EXEMPLOS DA ANTHROPIC", "CONECTADO AO QUE VOCÊ USA", GOLD)
        cur = max([i for i, e in enumerate(EXS) if t >= C[e[0]]] or [-1])
        for i, (cue, app, de, para_, col) in enumerate(EXS):
            a, dy = rise(t, C[cue])
            if a <= 0:
                continue
            y = 250 + i * 122 + dy
            on = 1.0 if i == cur else 0.55
            panel(c, 150, y, 1620, 104, a * (0.6 + 0.4 * on), col if i == cur else DIM, k=14, glow=i == cur)
            text(c, app, 190, y + 64, 30, "black", col, a * (0.5 + 0.5 * on), align="left")
            text(c, de, 640, y + 64, 28, "medium", mix(INK2, INK, on), a, align="left")
            arrow(c, 1150, y + 54, 1210, y + 54, col, a * on, 3, 12)
            text(c, para_, 1230, y + 64, 26 if text_w(para_, "bold", 26) < 500 else 22, "bold", mix(INK2, INK, on), a, align="left")
        fonte(c, "nomes citados no anúncio oficial · sem logos · 21/10/2026", ep(t, C["07.a"], 0.5), 885)


# ======================================================================  08 — CASOS
def b_casos(c, t, C, B):
    with cam(c, t, B, 1.0, 1.03):
        head(c, t, B["start"], "RELATOS PUBLICADOS PELA ANTHROPIC", "NA PRÁTICA", MAGENTA)
        cards = [("08.a", "CORRETORA DE IMÓVEIS", CYAN), ("08.b", "REDE DE RESTAURANTES", GOLD),
                 ("08.c", "ESTRATEGISTA DE MARCA", MAGENTA)]
        for k, (cue, lab, col) in enumerate(cards):
            a, dy = rise(t, C[cue])
            if a <= 0:
                continue
            x, y, w, h = 150 + k * 550, 250 + dy, 520, 560
            on = 1.0 if (k == 2 or t < C[cards[k + 1][0]]) else 0.6
            panel(c, x, y, w, h, a * (0.6 + 0.4 * on), col, k=18, label=lab, glow=on > 0.9)
            aa = a * on
            if k == 0:
                # mini calendário: visita no dia errado
                ic_cal(c, x + w / 2, y + 170, 150, col, aa)
                ak = a * ep(t, C[cue] + 1.6, 0.5)
                chip(c, "VISITA NO DIA ERRADO", x + w / 2, y + 330, ROSE, ak, anchor="center", size=24, filled=True)
                para(c, "alerta enviado sem ela pedir", x + 40, y + 420, 28, "bold", INK, aa, w - 80)
            elif k == 1:
                glow_text(c, "~110", x + w / 2, y + 180, 110, "black", col, aa, glow=0.3)
                text(c, "funcionários", x + w / 2, y + 225, 26, "mono", INK2, aa)
                text(c, "faturas revisadas loja por loja", x + w / 2, y + 300, 26, "bold", INK, aa)
                para(c, "“Não preciso abrir cem abas.”", x + 40, y + 400, 34, "black", INK,
                     a * ep(t, C[cue] + 3.0, 0.5), w - 80)
                text(c, "Amin Ebrahimi, dono · tradução livre", x + 40, y + 510, 20, "mono", INK2, a * ep(t, C[cue] + 3.0, 0.5),
                     align="left")
            else:
                # linha do tempo: call → voo
                y0 = y + 190
                line(c, x + 50, y0, x + w - 50, y0, INK2, aa * 0.6, 2)
                for xx, s, cc in ((x + 140, "CALL", col), (x + w - 140, "VOO", GOLD)):
                    c.drawCircle(xx, y0, 14, paint(cc, aa))
                    text(c, s, xx, y0 - 34, 26, "monob", cc, aa)
                text(c, "resumo da reunião preparado", x + w / 2, y + 290, 26, "bold", INK, aa)
                ad = a * ep(t, C["08.d"], 0.5)
                if ad > 0:
                    chip(c, "LOGO ANTES DO VOO", x + w / 2, y0 + 50, ROSE, ad, anchor="center", size=20, filled=True)
                    notif(c, x + 30, y + 360, w - 60, a * ep(t, C["08.d"] + 1.0, 0.5), "DUET · MOCKUP", "Quer remarcar a call?",
                          MAGENTA, 26)
        fonte(c, "fonte: anúncio oficial · claude.com · 21/10/2026", ep(t, C["08.a"], 0.5), 885)


# ======================================================================  09 — ACESSO
ACESSO = [("09.a", "STATUS", "prévia de pesquisa · lista de espera", CYAN),
          ("09.b", "PLANOS", "Pro e Max", VIOLET),
          ("09.c", "PAÍS", "só Estados Unidos (por enquanto)", GOLD),
          ("09.d", "ONDE", "iOS · Android · claude.ai", LIME),
          ("09.e", "CUSTO", "incluído no plano · mesmos limites do Claude", MAGENTA)]


def b_acesso(c, t, C, B):
    with cam(c, t, B, 1.0, 1.03):
        head(c, t, B["start"], "COMO USAR", "QUEM PODE, ONDE E QUANTO", LIME)
        for i, (cue, k, v, col) in enumerate(ACESSO):
            a, dy = rise(t, C[cue])
            if a <= 0:
                continue
            y = 250 + i * 106 + dy
            panel(c, 150, y, 1060, 90, a, col, k=12, fill=0.85, glow=False)
            text(c, k, 190, y + 57, 26, "monob", col, a, align="left")
            text(c, v, 390, y + 58, 30, "bold", INK, a, align="left")
        af = ep(t, C["09.e"] + 1.0, 0.6)
        if af > 0:
            px, py = 1280, 250
            panel(c, px, py, 490, 510, af, MAGENTA, label="limite do plano · ilustrativo")
            parts = [("conversas", 0.30, CYAN, C["09.e"] + 1.2), ("checagens em 2º plano", 0.18, GOLD, C["09.f"]),
                     ("tarefas grandes", 0.27, VIOLET, C["09.f"] + 1.0)]
            acc = 0
            bx, by, bw, bh = px + 60, py + 90, 110, 360
            rrect(c, bx, by, bw, bh, 10, "#111A30", af)
            for s, f, col, t0 in parts:
                ff = f * ep(t, t0, 0.8)
                rrect(c, bx, by + bh - (acc + ff) * bh, bw, ff * bh, 6, col, af)
                ly = by + bh - (acc + f / 2) * bh
                text(c, s, bx + bw + 30, ly + 8, 22, "bold", INK, af * ep(t, t0, 0.5), align="left")
                acc += ff
            text(c, "sem escala real", px + 245, py + 490, 18, "mono", DIM, af)
        text(c, "Team e Enterprise: ainda não (segundo o 9to5Mac)", 150, 830, 22, "mono", DIM, ep(t, C["09.b"] + 1.0, 0.5),
             align="left")
        fonte(c, "fonte: anúncio oficial · claude.com · 21/10/2026", ep(t, C["09.a"], 0.5), 870)


# ======================================================================  10 — APROVAÇÃO × PROIBIDO
APROV = [("10.a", "enviar uma mensagem"), ("10.b", "fazer um pagamento"), ("10.c", "assinar um documento"),
         ("10.d", "apagar qualquer coisa")]
PROIB = [("10.f", "negociar valores mobiliários"), ("10.g", "transferir dinheiro entre contas")]


def b_aprovacao(c, t, C, B):
    with cam(c, t, B, 1.0, 1.03):
        head(c, t, B["start"], "CUIDADOS", "QUEM DECIDE É VOCÊ", GOLD)
        a0 = ep(t, C["10.a"] - 0.3, 0.5)
        if a0 > 0:
            panel(c, 150, 250, 790, 580, a0, GOLD, label="exige a sua aprovação")
            for i, (cue, s) in enumerate(APROV):
                a, dy = rise(t, C[cue])
                if a <= 0:
                    continue
                y = 360 + i * 105 + dy
                ic_lock(c, 215, y - 10, 44, GOLD, a)
                text(c, s, 270, y + 4, 36, "bold", INK, a, align="left")
            ap = ep(t, C["10.d"] + 1.0, 0.5)
            text(c, "mostra o plano → espera o seu OK", 545, 790, 26, "mono", GOLD, ap)
        ae = ep(t, C["10.e"], 0.5)
        if ae > 0:
            panel(c, 980, 250, 790, 580, ae, ROSE, label="proibido mesmo com aprovação")
            for i, (cue, s) in enumerate(PROIB):
                a, dy = rise(t, C[cue])
                if a <= 0:
                    continue
                y = 400 + i * 150 + dy
                check_icon(c, 1050, y - 12, 26, a, ROSE, kind="x")
                for j, ln in enumerate(wrap(s, "bold", 36, 620)):
                    text(c, ln, 1100, y + j * 44, 36, "bold", INK, a, align="left")
            text(c, "bloqueado pelo próprio Duet", 1375, 790, 26, "mono", ROSE, ep(t, C["10.g"] + 0.8, 0.5))
        fonte(c, "fonte: anúncio oficial · claude.com · 21/10/2026", ep(t, C["10.a"], 0.5), 875)


# ======================================================================  11 — DADOS SENSÍVEIS
def b_sensivel(c, t, C, B):
    with cam(c, t, B, 1.0, 1.03):
        head(c, t, B["start"], "SEGURANÇA", "DADOS SENSÍVEIS", CYAN)
        rows = [("11.a", "SENHAS E TOKENS", "o Duet não vê diretamente", CYAN, "lock"),
                ("11.b", "CLASSIFICADOR NOVO", "bloqueia nº de cartão e documento de identidade", ROSE, "card"),
                ("11.c", "SAÚDE E FINANÇAS", "só com instrução explícita sua", GOLD, "warn"),
                ("11.d", "DESCONECTAR", "qualquer app, quando quiser", LIME, "plug")]
        for i, (cue, k, v, col, ic) in enumerate(rows):
            a, dy = rise(t, C[cue])
            if a <= 0:
                continue
            y = 250 + i * 145 + dy
            panel(c, 150, y, 1620, 120, a, col, k=14, fill=0.85, glow=False)
            cx, cy = 230, y + 60
            if ic == "lock":
                ic_lock(c, cx, cy, 64, col, a)
            elif ic == "card":
                c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - 40, cy - 26, 80, 52), 6, 6), paint(col, a, stroke=4))
                c.drawRect(skia.Rect.MakeXYWH(cx - 40, cy - 14, 80, 10), paint(col, a))
                c.drawLine(cx - 48, cy + 34, cx + 48, cy - 34, paint(col, a, stroke=5, cap_round=True))
            elif ic == "warn":
                ic_warn(c, cx, cy, 64, col, a)
            else:
                c.drawLine(cx - 40, cy, cx - 10, cy, paint(col, a, stroke=6, cap_round=True))
                c.drawLine(cx + 10, cy, cx + 40, cy, paint(col, a, stroke=6, cap_round=True))
                rrect(c, cx - 22, cy - 18, 14, 36, 3, col, a)
                rrect(c, cx + 8, cy - 18, 14, 36, 3, col, a)
            text(c, k, 310, y + 52, 30, "black", col, a, align="left")
            text(c, v, 310, y + 94, 30, "bold", INK, a, align="left")
        fonte(c, "segundo a Anthropic · claude.com · 21/10/2026 · mais detalhes prometidos “nos próximos dias”",
              ep(t, C["11.a"], 0.5), 850)


# ======================================================================  12 — LIMITES
def b_limites(c, t, C, B):
    with cam(c, t, B, 1.0, 1.03):
        head(c, t, B["start"], "LIMITES", "AINDA É UMA PRÉVIA", GOLD)
        rows = [("12.a", "pode entender mal uma conversa ou errar o que é urgente", "Anthropic"),
                ("12.b", "tarefas pessoais (ex.: comprar ingressos) ainda são mais fracas", "Anthropic"),
                ("12.c", "ainda não mostra o navegador trabalhando", "Anthropic"),
                ("12.d", "Microsoft 365 ainda não funciona no Duet", "segundo Flavio Copes, citando a central de ajuda")]
        for i, (cue, s, src) in enumerate(rows):
            a, dy = rise(t, C[cue])
            if a <= 0:
                continue
            y = 250 + i * 145 + dy
            col = GOLD if i < 3 else VIOLET
            panel(c, 150, y, 1620, 120, a, col, k=14, fill=0.85, glow=False)
            ic_warn(c, 230, y + 60, 64, col, a)
            text(c, s, 310, y + 58, 32, "bold", INK, a, align="left")
            text(c, src, 310, y + 96, 22, "mono", INK2, a, align="left")


# ======================================================================  13 — RIVAIS
def b_rivais(c, t, C, B):
    with cam(c, t, B, 1.0, 1.03):
        head(c, t, B["start"], "CONCORRÊNCIA · SEGUNDO A CNBC", "NÃO CHEGA SOZINHO", VIOLET)
        x0, x1, y = 260, 1660, 640
        aa = ep(t, C["13.a"], 0.6)
        if aa > 0:
            glow_line(c, x0, y, x1, y, INK2, aa * 0.6, 3, progress=ep(t, C["13.a"], 1.0))
            text(c, "CONSUMIDOR", x0, y + 60, 26, "monob", INK2, aa, align="left")
            text(c, "TRABALHO", x1, y + 60, 26, "monob", INK2, aa, align="right")
            text(c, "posição aproximada · descrição da CNBC", W / 2, y + 110, 20, "mono", DIM, aa)
        items = [("13.a", "MUSE", "Meta", "mira mais o consumidor", x0 + 160, MAGENTA),
                 ("13.b", "DOTS", "OpenAI", "entre empresas e consumidores", W / 2, LIME),
                 ("13.d", "DUET", "Anthropic", "foco em trabalho", x1 - 160, CYAN)]
        for cue, nm, who, desc, x, col in items:
            a = ep(t, C[cue] + (0.6 if cue == "13.a" else 0), 0.6)
            if a <= 0:
                continue
            node(c, x, 420, 100, None, None, col, a, t)
            glow_text(c, nm, x, 436, 44, "black", col, a, glow=0.4)
            text(c, who, x, 300, 28, "monob", INK2, a)
            c.drawLine(x, 520, x, y - 14, paint(col, 0.6 * a, stroke=2))
            c.drawCircle(x, y, 12, paint(col, a))
            text(c, desc, x, y + 160, 24, "bold", INK, a * ep(t, C["13.c"] if cue != "13.d" else C["13.d"], 0.5))
        fonte(c, "CNBC · 21/10/2026 · nomes citados sem logos", ep(t, C["13.a"], 0.5), 880)


# ======================================================================  14 — RESUMO
RES = [("14.a", "agente proativo, num app próprio", CYAN), ("14.b", "brief de manhã + checagens a cada poucas horas", VIOLET),
       ("14.c", "trabalha na nuvem, com tudo desligado", LIME), ("14.d", "pede aprovação: enviar, pagar, assinar, apagar", GOLD),
       ("14.e", "prévia com lista de espera · Pro e Max · EUA", MAGENTA)]


def b_resumo(c, t, C, B):
    with cam(c, t, B, 1.0, 1.03):
        head(c, t, B["start"], "RESUMO", "CLAUDE DUET EM 5 PONTOS", CYAN)
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
    head(c, t, B["start"], "TECH//010", "OBRIGADO POR ASSISTIR", CYAN)
    cta(c, t, C["15.like"], C["15.sub"], C["15.bell"], C["15.com"], C["15.bye"],
        "Você deixaria uma IA cuidar da sua caixa de entrada?")


FONTES = [
    ("Anthropic (oficial)", "Introducing Claude Duet · claude.com/resources/articles/claude-duet", "21/10/2026"),
    ("Claude no X (oficial)", "posts de anúncio da conta @claudeai (x.com/claudeai)", "21/10/2026"),
    ("CNBC", "Anthropic announces preview of Claude Duet... to take on Muse, Dots", "21/10/2026"),
    ("TechCrunch", "Claude Duet app is Anthropic's bet on agents", "22/10/2026"),
    ("9to5Mac", "9to5mac.com/2026/10/21 · anthropic-takes-on-chatgpt-dots-and-meta-muse…", "21/10/2026"),
    ("MacRumors", "macrumors.com/2026/10/21/anthropic-claude-duet", "21/10/2026"),
    ("9to5Google", "9to5google.com/2026/10/21/claude-duet-anthropic-ai-agent-waitlist", "21/10/2026"),
    ("Flavio Copes", "flaviocopes.com/claude-duet (blog; não testou o app)", "22/10/2026"),
    ("AIN.ua", "en.ain.ua · Anthropic introduced Claude Duet, an agent that autonomously tracks work tasks", "22/10/2026"),
]


def b_fontes(c, t, C, B):
    head(c, t, B["start"], "CRÉDITOS", "FONTES", CYAN)
    a0 = ep(t, B["start"] + 0.2, 0.6)
    panel(c, 150, 230, 1620, 640, a0, CYAN, label="consultadas em 22/10/2026")
    for i, (v, tit, d) in enumerate(FONTES):
        a = ep(t, B["start"] + 0.4 + 0.12 * i, 0.4)
        y = 300 + i * 56
        text(c, v, 200, y, 26, "extrabold", CYAN, a, align="left")
        tt = tit if text_w(tit, "medium", 24) < 1000 else wrap(tit, "medium", 24, 960)[0] + "…"
        text(c, tt, 520, y, 24, "medium", INK, a, align="left")
        text(c, d, 1720, y, 24, "mono", INK2, a, align="right")
    ab = ep(t, B["start"] + 1.8, 0.6)
    text(c, "telas do Duet: mockups ilustrativos · sem logos de terceiros · narração com voz sintética (IA)", W / 2, 840, 20, "mono", DIM, ab)


BLOCKS = dict(gancho=b_gancho, oque=b_oque, fluxo=b_fluxo, ciclo=b_ciclo, nuvem=b_nuvem, tarefas=b_tarefas,
              conectores=b_conectores, casos=b_casos, acesso=b_acesso, aprovacao=b_aprovacao, sensivel=b_sensivel,
              limites=b_limites, rivais=b_rivais, resumo=b_resumo, cta=b_cta, fontes=b_fontes)
