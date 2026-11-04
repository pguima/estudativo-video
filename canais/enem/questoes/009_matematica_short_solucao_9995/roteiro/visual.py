"""Visual — Estudativo · Short 009 (vertical 1080x1920): ENEM 2025, questão 137, a solução de 99,95% (aula completa: 008).
render.py <proj> --vertical. Paleta e notação do design system de matemática (_ferramentas/matematica.py), com layout de
Short: selo no alto, título grande, figura no meio, legenda de 1 a 3 palavras bem grandes, contagem para pausar.
Cores com função: âmbar = dado (10 L, %, S2), ciano = incógnita / S1 no desenho, menta = certo, coral = pegadinha."""
import idioma
import matematica
from matematica import *  # noqa
from matematica import _num

IDIOMAS_NO_CODIGO = True
EN = idioma.LANG == "en"
ARQUIVO_FINAL = "estudativo_short_009_solucao_9995.mp4"
MARCA = ""

SOM = dict(intro=False, ganho_trilha=0.32, lufs=-14, bpm=118, sfx={
    "01.a": ["pop", "pop@+2.6"], "01.b": "whoosh", "01.c": "impact",
    "02.a": ["pop", "pop@+0.15", "pop@+0.3", "pop@+0.45", "pop@+0.6"], "02.b": "notif",
    "02.c": ["alert", "tick@+1.55", "tick@+2.55", "tick2@+3.55"],   # tiques do cronômetro 3-2-1
    "03.a": "deny", "03.b": ["impact", "deny@+0.3"],
    "04.a": "shimmer", "04.b": ["data", "confirm@+3.0"],
    "05.a": "data", "05.b": ["whoosh", "impact@+1.6"],
    "06.a": ["impact", "shimmer@+0.3"], "06.b": "confirm",
    "07.a": "notif", "07.b": "lock"})

T = dict(   # (inglês, português)
    selo=("ENEM 2025 · MATH QUESTION", "ENEM 2025 · QUESTÃO DE MATEMÁTICA"),
    sai=("HOW MUCH COMES OUT?", "QUANTO SAI?"), so_s1=("only S1 comes out", "sai só S1"),
    comenta=("comment before you see it ↓", "comenta antes de ver ↓"), pausa=("PAUSE AND THINK", "PAUSE E PENSE"),
    peg=("TRAP!", "PEGADINHA!"), totais=("DIFFERENT TOTALS", "TOTAIS DIFERENTES"),
    de10=("of 10 L", "de 10 L"), deT=("of ? L", "de ? L"),
    segredo=("WHAT DOESN'T CHANGE", "O QUE NÃO MUDA"), nao_muda=("doesn't change", "não muda"),
    dobrou=("DOUBLED", "DOBROU"), metade=("HALF!", "METADE!"), total=("TOTAL ÷ 2", "TOTAL ÷ 2"),
    antes=("BEFORE · 10 L", "ANTES · 10 L"), depois=("AFTER", "DEPOIS"), lupa=("magnifier: S2 enlarged", "lupa: S2 ampliado"),
    saem=("COMES OUT", "SAEM"), letra=("ANSWER E", "LETRA E"),
    acertou=("DID YOU GET IT?", "VOCÊ ACERTOU?"), conta=("tell me in the comments ↓", "conta nos comentários ↓"),
    aula=("FULL LESSON", "AULA COMPLETA"), passo=("step by step on the channel", "passo a passo no canal"),
    canal=("ESTUDATIVO ENGLISH", "ESTUDATIVO"),
)
L = {k: (v[0] if EN else v[1]) for k, v in T.items()}
_EXTRA = [] if EN else [
    ("dois mil e vinte e cinco", "2025"), ("noventa e nove vírgula noventa e cinco por cento", "99,95%"),
    ("noventa e nove vírgula noventa por cento", "99,90%"), ("zero vírgula zero cinco por cento", "0,05%"),
    ("zero vírgula dez por cento", "0,10%"), ("zero vírgula zero zero cinco litro", "0,005 L"),
    ("cinco mililitros", "5 mL"), ("dez litros", "10 L"), ("cinco litros", "5 L"), ("s um", "S1"), ("s dois", "S2")]
matematica.NUMEROS_EXTRA[:] = sorted(_EXTRA, key=lambda p: -len(p[0].split()))
n_ = lambda s: s.replace(",", ".") if EN else s   # noqa: E731
CX = W / 2
CAP_Y = 1440


def OVERLAY(c, t):
    pill(c, L["selo"], CX, 150, 26, AMB, BG0, 0.95, "extrabold")


def big(c, s, y, a, col=WHITE, size=100, hl=None, hl_col=CYA, maxw=980):
    """título grande centralizado; hl = trecho em pílula colorida"""
    if a <= 0:
        return
    f = ease_out(clamp(a))
    while text_w(s, "black", size) > maxw:
        size -= 3
    w = text_w(s, "black", size)
    x = CX - w / 2
    yy = y + (1 - f) * 24
    if hl and hl in s:
        i_hl = s.rindex(hl)
        pre = s[:i_hl]
        hx = x + text_w(pre, "black", size)
        hw = text_w(hl, "black", size)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(hx - 14, yy - size * 0.84, hw + 28, size * 1.1), 14, 14), paint(hl_col, f))
        text(c, pre, x, yy, size, "black", col, f, align="left")
        text(c, hl, hx, yy, size, "black", BG0, f, align="left")
        text(c, s[i_hl + len(hl):], hx + hw, yy, size, "black", col, f, align="left")
    else:
        glow_text(c, s, CX, yy, size, "black", col, f, glow=0.14)


def stamp(c, s, cx, cy, col, a, size=56, rot=-7):
    if a <= 0:
        return
    k = 1 + 0.6 * (1 - ease_out(clamp(a * 2.2)))
    c.save(); c.translate(cx, cy); c.rotate(rot); c.scale(k, k)
    w = text_w(s, "black", size) + size * 0.9
    h = size * 1.45
    r = skia.Rect.MakeXYWH(-w / 2, -h / 2, w, h)
    c.drawRRect(skia.RRect.MakeRectXY(r, 12, 12), blur_paint(col, 0.5 * a, 16))
    c.drawRRect(skia.RRect.MakeRectXY(r, 12, 12), paint(col, a))
    text_mid(c, s, 0, 0, size, "black", BG0, a)
    c.restore()


def recipiente(c, cx, base, a, t, nivel=1.0, w=380, h=600, hl_s2=0.0, fantasma=0.0, rot="10 L", rot_col=AMB, marca5=0.0):
    """recipiente de vidro (S1 em ciano); nivel 1 = 10 L; S2 = gotinhas âmbar no fundo (mesmo desenho da aula 008)"""
    if a <= 0:
        return
    x0, x1, top = cx - w / 2, cx + w / 2, base - h
    cheio = h * 0.86
    lv = base - cheio * nivel
    p = skia.Paint(AntiAlias=True)
    p.setShader(skia.GradientShader.MakeLinear([(cx, lv), (cx, base)], [hexc(CYA), hexc("#1F6F99")]))
    p.setAlphaf(0.55 * a)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeLTRB(x0 + 8, lv, x1 - 8, base - 8), 18, 18), p)
    c.drawLine(x0 + 10, lv, x1 - 10, lv + 2 * math.sin(t * 3), paint(WHITE, 0.6 * a, stroke=3))
    if fantasma > 0:
        pf = paint(CYA, 0.7 * a * fantasma, stroke=4)
        pf.setPathEffect(skia.DashPathEffect.Make([16, 12], t * 30 % 28))
        c.drawRect(skia.Rect.MakeLTRB(x0 + 14, base - cheio, x1 - 14, lv), pf)
    pul = 0.5 + 0.5 * math.sin(t * 6)
    for i in range(5):
        gx, gy = cx - 70 + i * 35, base - 34 - 12 * (i % 2)
        if hl_s2 > 0:
            c.drawCircle(gx, gy, 20, blur_paint(AMB, (0.4 + 0.4 * pul) * a * hl_s2, 12))
        c.drawCircle(gx, gy, 8, paint(AMB, a))
    pth = skia.Path(); pth.moveTo(x0 - 18, top); pth.lineTo(x0, top + 16); pth.lineTo(x0, base - 26)
    pth.quadTo(x0, base, x0 + 26, base); pth.lineTo(x1 - 26, base); pth.quadTo(x1, base, x1, base - 26)
    pth.lineTo(x1, top + 16); pth.lineTo(x1 + 18, top)
    c.drawPath(pth, blur_paint(WHITE, 0.25 * a, 8, stroke=8))
    c.drawPath(pth, paint(WHITE, 0.85 * a, stroke=6))
    for k in range(1, 11):
        yk = base - cheio * k / 10
        c.drawLine(x1 - (46 if k % 5 == 0 else 26), yk, x1 - 4, yk, paint(WHITE, 0.45 * a, stroke=3))
    if marca5 > 0:
        y5 = base - cheio * 0.5
        c.drawLine(x0 - 34, y5, x1 + 34, y5, paint(AMB, a * marca5, stroke=4))
        label(c, "5 L", x1 + 50, y5, a * marca5, 40, AMB, "black", "left")
    if rot:
        label(c, rot, cx, base + 60, a, 56, rot_col, "black")


def lupa(c, cx, cy, r, a, frac, col=AMB, rotulo="S2"):
    if a <= 0:
        return
    c.save()
    pth = skia.Path(); pth.addCircle(cx, cy, r)
    c.clipPath(pth, doAntiAlias=True)
    c.drawRect(skia.Rect.MakeXYWH(cx - r, cy - r, 2 * r, 2 * r), paint(CYA, 0.45 * a))
    c.drawRect(skia.Rect.MakeXYWH(cx + r - 2 * r * frac, cy - r, 2 * r * frac, 2 * r), paint(col, a))
    c.restore()
    c.drawCircle(cx, cy, r, paint(WHITE, a, stroke=6))
    c.drawLine(cx + r * 0.72, cy + r * 0.72, cx + r * 1.15, cy + r * 1.15, paint(WHITE, a, stroke=14, cap_round=True))
    if rotulo and frac > 0.08:
        text_mid(c, rotulo, cx + r - r * frac, cy, 34, "black", BG0, a)


def barra(c, x, y, w, a, pct_s2, titulo, r=110, lx=None):
    """barra 100% (S1 ciano) + lupa no S2 (fino demais para ver)"""
    if a <= 0:
        return
    label(c, titulo, x, y - 56, a, 38, WHITE, "extrabold", "left")
    rrect(c, x, y - 30, w, 60, 14, CYA, 0.45 * a)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y - 30, w, 60), 14, 14), paint(CYA, a, stroke=3))
    lx = lx if lx is not None else x + w - 140
    c.drawCircle(x + w - 8, y, 26, paint(AMB, 0.9 * a, stroke=3))
    c.drawLine(x + w - 8, y + 26, lx, y + 70, paint(AMB, 0.7 * a, stroke=3))
    lupa(c, lx, y + 70 + r, r, a, min(1, pct_s2 * 3))


def opcoes(c, y0, a, t, t0, destaque=None, certo=None, errado=None, dim=0.0):
    ops = [("A", n_("0,0050")), ("B", n_("0,0100")), ("C", n_("0,5000")), ("D", n_("4,9775")), ("E", n_("5,0000"))]
    for i, (le, v) in enumerate(ops):
        y = y0 + i * 118
        k = a * pop(t, t0 + i * 0.15, 0.3)
        if k <= 0:
            continue
        col = MNT if le == certo else (RED if le == errado else CYA)
        fade_k = k * (1 - dim * 0.75 * (le not in (certo, errado)))
        rrect(c, 170, y - 48, 740, 96, 48, BG1, 0.92 * fade_k)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(170, y - 48, 740, 96), 48, 48),
                    paint(col, fade_k, stroke=4 if le in (certo, errado, destaque) else 2))
        c.drawCircle(230, y, 34, paint(col, fade_k))
        text_mid(c, le, 230, y, 40, "black", BG0, fade_k)
        text_mid(c, v + " L", 300, y, 54, "black", WHITE, fade_k, align="left")
        if le == certo:
            check(c, 850, y, 30, k)
        if le == errado:
            cross(c, 850, y, 30, k)


def contagem(c, cx, cy, a, t, t0, dur=3.0):
    """cronômetro 3 → 1 com anel que esvazia"""
    if a <= 0 or t < t0:
        return
    u = clamp((t - t0) / dur)
    n = max(1, 3 - int((t - t0) / (dur / 3)))
    r = 120
    c.drawCircle(cx, cy, r, paint(BG1, 0.9 * a))
    c.drawArc(skia.Rect.MakeXYWH(cx - r, cy - r, 2 * r, 2 * r), -90, 360 * (1 - u), False, paint(AMB, a, stroke=14, cap_round=True))
    k = 1 + 0.25 * (1 - ep(t, t0 + (3 - n) * dur / 3, 0.25))
    c.save(); c.translate(cx, cy); c.scale(k, k)
    text_mid(c, str(n), 0, 0, 130, "black", WHITE, a)
    c.restore()


# ---------------------------------------------------------------- legenda de Short (1 a 3 palavras, grandes)
def _chunks(tokens):
    out, cur = [], []
    for tk in _num(tokens):
        cur.append(tk)
        end = tk["disp"][-1:] in PUNCT
        if len(cur) >= 3 or end or sum(len(x["disp"]) + 1 for x in cur) > 15:
            out.append(cur); cur = []
    if cur:
        out.append(cur)
    return out


def CAPTION(c, scene, t):
    lt = t - scene["start"]
    chunks = scene.setdefault("_chs", _chunks(scene["tokens"]))
    for i, ch in enumerate(chunks):
        s = ch[0]["t0"] - 0.06
        e = chunks[i + 1][0]["t0"] - 0.06 if i + 1 < len(chunks) else min(scene["dur"] - 0.05, ch[-1]["t1"] + 0.6)
        if s <= lt < e:
            break
    else:
        return
    words = [tk["disp"].upper() if not any(ch_.isdigit() for ch_ in tk["disp"]) else tk["disp"] for tk in ch]
    size, sp = 92, 24
    while sum(text_w(wd, "black", size) for wd in words) + sp * (len(words) - 1) > 960:
        size -= 3
    tot = sum(text_w(wd, "black", size) for wd in words) + sp * (len(words) - 1)
    pp = ease_back(clamp((lt - s) / 0.16))
    x = CX - tot / 2
    c.save(); c.translate(CX, CAP_Y); c.scale(0.85 + 0.15 * pp, 0.85 + 0.15 * pp); c.translate(-CX, -CAP_Y)
    f = motor.font("black", size)
    for tk, wd in zip(ch, words):
        falando = tk["t0"] - 0.05 <= lt < tk["t1"] + 0.25
        col = AMB if falando else (CYA if tk["bold"] else WHITE)
        sh = skia.Paint(AntiAlias=True, Style=skia.Paint.kStroke_Style, StrokeWidth=size * 0.16, Color=hexc(BG0))
        sh.setStrokeJoin(skia.Paint.kRound_Join)
        c.drawString(wd, x, CAP_Y + size * 0.36, f, sh)
        c.drawString(wd, x, CAP_Y + size * 0.36, f, paint(col, 1.0))
        x += text_w(wd, "black", size) + sp
    c.restore()


# ---------------------------------------------------------------- cenas
def b_gancho(c, t, C, B):
    ta, tb, tc = (C[f"01.{k}"] for k in "abc")
    a = ep(t, ta, 0.2) * (1 - prog(t, B["end"] - 0.2, 0.2))
    recipiente(c, CX, 1180, a, t, 1.0)
    popill(c, "S1 = " + n_("99,95%"), CX, 320, 54, AMB, BG0, a * (1 - ep(t, tc, 0.15)), t, ta + 1.4)
    kb = a * ep(t, tb, 0.3)
    if kb > 0:
        for i in range(3):
            u = ((t - tb) * 0.8 + i / 3) % 1
            yy = 520 - 110 * u
            c.drawLine(CX - 110 + i * 110, yy + 50, CX - 110 + i * 110, yy, paint(CYA, kb * (1 - u), stroke=8, cap_round=True))
        label(c, L["so_s1"], CX, 420, kb * (1 - ep(t, tc, 0.2)), 44, CYA, "black")
        popill(c, "→ " + n_("99,90%"), CX, 420, 54, AMB, BG0, kb * ep(t, tb + 1.5, 0.2) * (1 - ep(t, tc, 0.2)), t, tb + 1.5)
    kc = a * ep(t, tc, 0.2)
    if kc > 0:
        k = 1 + 0.04 * math.sin(t * 8)
        c.save(); c.translate(CX, 440); c.scale(k, k); c.translate(-CX, -440)
        big(c, L["sai"], 470, kc, WHITE, 116, hl=L["sai"].split()[-1], hl_col=CYA)
        c.restore()


def b_opcoes(c, t, C, B):
    ta, tb, tc = (C[f"02.{k}"] for k in "abc")
    a = fade(t, B["start"], B["end"], 0.2, 0.15)
    t0 = B["end"] - 3.1
    ko = a * (1 - ep(t, t0, 0.2))
    big(c, L["sai"], 330, ko, WHITE, 100, hl=L["sai"].split()[-1], hl_col=CYA)
    opcoes(c, 520, ko, t, ta)
    label(c, L["comenta"], CX, 1150, ko * ep(t, tb, 0.3), 46, AMB, "extrabold")
    if t >= t0:
        kp = a * ep(t, t0, 0.2)
        label(c, L["pausa"], CX, 480, kp, 84, AMB, "black")
        c.save(); c.translate(CX, 820); c.scale(1.5, 1.5); c.translate(-CX, -820)
        contagem(c, CX, 820, kp, t, t0, 3.0)
        c.restore()
        label(c, L["comenta"], CX, 1150, kp, 46, AMB, "extrabold")


def b_pegadinha(c, t, C, B):
    ta, tb = C["03.a"], C["03.b"]
    a = fade(t, B["start"], B["end"], 0.2, 0.2)
    ka = a * (1 - ep(t, tb + 1.0, 0.25))
    eq(c, [(n_("99,95%") + " − " + n_("99,90%"), AMB), (" = ", WHITE), (n_("0,05%"), RED)], 340, ka * ep(t, ta, 0.3), 70, cx=CX, maxw=960)
    eq(c, [(n_("0,05%") + " × 10 L = ", WHITE), (n_("0,005") + " L", RED)], 470, ka * ep(t, ta + 1.2, 0.3), 70, cx=CX, maxw=960)
    opcoes(c, 650, ka, t, ta + 2.0, errado="A", dim=1.0)
    stamp(c, L["peg"], CX, 1190, RED, ka * ep(t, tb, 0.2), 76)
    kb = a * ep(t, tb + 1.0, 0.3)
    if kb > 0:
        big(c, L["totais"], 360, kb, WHITE, 84, hl=L["totais"].split()[-1] if not EN else "DIFFERENT", hl_col=RED)
        recipiente(c, 290, 1100, kb, t, 1.0, w=300, h=470, rot=n_("99,95%") + " " + L["de10"])
        recipiente(c, 790, 1100, kb, t, 0.5, w=300, h=470, rot=n_("99,90%") + " " + L["deT"], rot_col=CYA)
        label(c, "≠", CX, 860, kb, 120, RED, "black")


def b_segredo(c, t, C, B):
    ta, tb = C["04.a"], C["04.b"]
    a = fade(t, B["start"], B["end"], 0.2, 0.2)
    big(c, L["segredo"], 330, a, WHITE, 92, hl=L["segredo"].split()[-1] if not EN else "CHANGE", hl_col=AMB)
    kb = a * ep(t, tb, 0.3)
    yb = 1060 + 140 * ease_io(kb)
    recipiente(c, CX, yb, a, t, 1.0, w=340, h=520 - 80 * ease_io(kb), hl_s2=ep(t, ta + 1.4, 0.3), rot="")
    label(c, "S2: " + L["nao_muda"], CX, yb + 70, a * ep(t, ta + 1.6, 0.3), 50, AMB, "black")
    if kb > 0:
        eq(c, [("S2 = ", AMB), (n_("0,05%"), AMB), (" × 10 L", WHITE)], 490, kb, 76, cx=CX, maxw=960)
        eq(c, [("S2 = ", AMB), (n_("0,005") + " L", AMB)], 630, kb * ep(t, tb + 3.0, 0.3), 92, cx=CX, maxw=960, box=AMB)


def b_dobro(c, t, C, B):
    ta, tb = C["05.a"], C["05.b"]
    a = fade(t, B["start"], B["end"], 0.2, 0.2)
    ka = a * (1 - ep(t, tb, 0.25))
    if ka > 0:
        barra(c, 110, 330, 860, ka, 0.05, L["antes"] + "  ·  " + n_("0,05%"), r=100, lx=300)
        barra(c, 110, 760, 860, ka * ep(t, ta + 1.2, 0.3), 0.10, L["depois"] + "  ·  " + n_("0,10%"), r=100, lx=300)
        stamp(c, "×2  " + L["dobrou"], 760, 1010, AMB, ka * ep(t, ta + 2.6, 0.2), 60, rot=-5)
    kb = a * ep(t, tb, 0.3)
    if kb > 0:
        big(c, L["total"], 340, kb, WHITE, 100, hl="÷ 2", hl_col=AMB)
        nv = 1 - 0.5 * ease_io(prog(t, tb + 0.3, 1.2))
        recipiente(c, CX, 1120, kb, t, nv, w=380, h=600, marca5=ep(t, tb + 1.4, 0.3), rot="T = 5 L" if t > tb + 1.5 else "T = ?",
                   rot_col=CYA)


def b_resposta(c, t, C, B):
    ta, tb = C["06.a"], C["06.b"]
    a = fade(t, B["start"], B["end"], 0.2, 0.2)
    ka = a * (1 - ep(t, tb, 0.25))
    if ka > 0:
        big(c, L["saem"], 300, ka, WHITE, 90)
        k = pop(t, ta, 0.4)
        c.save(); c.translate(CX, 470); c.scale(k, k); c.translate(-CX, -470)
        glow_text(c, "5 L", CX, 520, 230, "black", MNT, ka, glow=0.3)
        c.restore()
        recipiente(c, CX, 1170, ka, t, 0.5, w=320, h=480, fantasma=1, marca5=1, rot="")
        stamp(c, L["metade"], CX, 1240, AMB, ka * ep(t, ta + 1.4, 0.2), 70, rot=-5)
    kb = a * ep(t, tb, 0.3)
    if kb > 0:
        big(c, L["letra"], 340, kb, WHITE, 110, hl="E", hl_col=MNT)
        opcoes(c, 560, kb, t, tb - 0.4, certo="E", errado="A", dim=1.0)


def b_final(c, t, C, B):
    ta, tb = C["07.a"], C["07.b"]
    a = ep(t, B["start"], 0.2)
    ka = a * (1 - ep(t, tb, 0.25))
    if ka > 0:
        big(c, L["acertou"], 380, ka, WHITE, 104, hl=L["acertou"].split()[-1], hl_col=AMB)
        opcoes(c, 560, ka, t, ta - 1.0, certo="E")
        label(c, L["conta"], CX, 1180, ka * ep(t, ta + 0.8, 0.3), 50, AMB, "extrabold")
    kb = a * ep(t, tb, 0.3)
    if kb > 0:
        cartao(c, 120, 330, 840, 760, kb, CYA, L["aula"])
        recipiente(c, CX, 820, kb, t, 0.5, w=260, h=380, fantasma=1, rot="")
        text_mid(c, L["passo"], CX, 930, 46, "extrabold", WHITE, kb)
        glow_text(c, L["canal"], CX, 1040, 96, "black", WHITE, kb * ep(t, tb + 1.0, 0.3), glow=0.14)
        w = text_w(L["canal"], "black", 96)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(CX - w / 2, 1066, w * ep(t, tb + 1.3, 0.6), 12), 6, 6), paint(AMB, kb))


BLOCKS = dict(gancho=b_gancho, opcoes=b_opcoes, pegadinha=b_pegadinha, segredo=b_segredo, dobro=b_dobro,
              resposta=b_resposta, final=b_final)
