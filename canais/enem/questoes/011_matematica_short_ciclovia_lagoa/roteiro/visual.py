"""Visual — Estudativo · Short 011 (vertical 1080x1920): ENEM 2025, questão 136, a ciclovia da lagoa (aula completa: 010).
render.py <proj> --vertical. Paleta e notação do design system de matemática (_ferramentas/matematica.py), com layout de
Short do 009: selo no alto, título grande, figura no meio, legenda de 1 a 3 palavras bem grandes, contagem para pausar.
Figuras da aula 010 (lagoa, trechos da ciclovia, policiais, desenrolar). Cores com função: âmbar = dado (1 km, 200 m, π ≈ 3),
ciano = incógnita / trecho protegido, menta = certo, coral = pegadinha e trecho sem proteção."""
import idioma
import matematica
from matematica import *  # noqa
from matematica import _num

IDIOMAS_NO_CODIGO = True
EN = idioma.LANG == "en"
ARQUIVO_FINAL = "estudativo_short_011_ciclovia_lagoa.mp4"
MARCA = ""

SOM = dict(intro=False, ganho_trilha=0.32, lufs=-14, bpm=118, sfx={
    "01.a": ["pop", "pop@+2.6"], "01.b": "whoosh", "01.c": "impact",
    "02.a": ["pop", "pop@+0.15", "pop@+0.3", "pop@+0.45", "pop@+0.6"], "02.b": "notif",
    "02.c": ["alert", "tick@+2.07", "tick@+2.87", "tick2@+3.67"],   # tiques do cronômetro 3-2-1
    "03.a": "shimmer", "03.b": ["data", "confirm@+3.0"],
    "04.a": "deny", "04.b": ["impact", "deny@+0.3"],
    "05.a": "whoosh", "05.b": ["data", "impact@+2.0"],
    "06.a": ["impact", "shimmer@+0.3"], "06.b": "confirm",
    "07.a": "notif", "07.b": "lock"})

T = dict(   # (inglês, português)
    selo=("ENEM 2025 · MATH QUESTION", "ENEM 2025 · QUESTÃO DE MATEMÁTICA"),
    quantos=("HOW MANY", "QUANTOS"), policiais_q=("OFFICERS?", "POLICIAIS?"), policiais=("officers", "policiais"),
    comenta=("comment before you see it ↓", "comenta antes de ver ↓"), pausa=("PAUSE AND THINK", "PAUSE E PENSE"),
    peg=("TRAP!", "PEGADINHA!"), cada_lado=("EACH SIDE", "PARA CADA LADO"),
    frente=("ahead", "à frente"), atras=("behind", "atrás"), sem=("UNPROTECTED", "SEM PROTEÇÃO"),
    letra=("ANSWER C", "LETRA C"),
    acertou=("DID YOU GET IT?", "VOCÊ ACERTOU?"), conta=("tell me in the comments ↓", "conta nos comentários ↓"),
    aula=("FULL LESSON", "AULA COMPLETA"), passo=("step by step on the channel", "passo a passo no canal"),
    canal=("ESTUDATIVO ENGLISH", "ESTUDATIVO"),
)
L = {k: (v[0] if EN else v[1]) for k, v in T.items()}
_EXTRA = [] if EN else [
    ("dois mil e vinte e cinco", "2025"), ("um quilômetro", "1 km"), ("seis mil metros", "6.000 m"),
    ("mil metros", "1.000 m"), ("seis mil", "6.000"), ("quatrocentos metros", "400 m"), ("duzentos metros", "200 m"),
    ("dividido por", "÷"), ("dois vezes", "2 ×"), ("pi", "π")]
matematica.NUMEROS_EXTRA[:] = sorted(_EXTRA, key=lambda p: -len(p[0].split()))
n_ = lambda s: s.replace(".", "#").replace(",", ".").replace("#", ",") if EN else s   # noqa: E731  troca , e . no inglês
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


# ---------------------------------------------------------------- figuras (da aula 010)
AGUA = ("#4CC9F0", "#1F6F99")
PISTA = "#D7E0EE"
GRAU = math.pi / 180


def pt(cx, cy, R, ang):
    """ponto na circunferência; ang em radianos, 0 = topo, sentido horário"""
    return cx + R * math.sin(ang), cy - R * math.cos(ang)


def lagoa(c, cx, cy, R, a, t, agua=1.0, pista=1.0):
    """lagoa (água em ciano) com a ciclovia (anel claro com faixa tracejada)"""
    if a <= 0:
        return
    if agua > 0:
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial((cx - R * 0.3, cy - R * 0.35), R * 1.4, [hexc(AGUA[0]), hexc(AGUA[1])]))
        p.setAlphaf(0.55 * a * agua)
        c.drawCircle(cx, cy, R * 0.955, p)
        for i in range(3):   # marolas
            yy = cy - R * 0.3 + i * R * 0.3
            w = R * (0.5 - 0.1 * abs(i - 1))
            ph = math.sin(t * 1.2 + i * 2)
            pth = skia.Path(); pth.moveTo(cx - w + ph * 10, yy)
            pth.quadTo(cx - w / 2 + ph * 10, yy - 10, cx + ph * 10, yy); pth.quadTo(cx + w / 2 + ph * 10, yy + 10, cx + w + ph * 10, yy)
            c.drawPath(pth, paint(WHITE, 0.16 * a * agua, stroke=3, cap_round=True))
    if pista > 0:
        sw = max(14, R * 0.075)
        c.drawCircle(cx, cy, R, blur_paint(PISTA, 0.18 * a * pista, 10, stroke=sw + 8))
        c.drawCircle(cx, cy, R, paint(PISTA, 0.9 * a * pista, stroke=sw))
        pd = paint(BG1, 0.55 * a * pista, stroke=2.5)
        pd.setPathEffect(skia.DashPathEffect.Make([14, 12], 0))
        c.drawCircle(cx, cy, R, pd)


def arco(c, cx, cy, R, a0, a1, col, a, w=22, glow=True):
    """trecho da ciclovia de a0 a a1 (rad, 0 = topo, horário)"""
    if a <= 0 or a1 <= a0:
        return
    rect = skia.Rect.MakeLTRB(cx - R, cy - R, cx + R, cy + R)
    pth = skia.Path(); pth.addArc(rect, a0 / GRAU - 90, (a1 - a0) / GRAU)
    if glow:
        c.drawPath(pth, blur_paint(col, 0.45 * a, 12, stroke=w + 10))
    p = paint(col, a, stroke=w)
    c.drawPath(pth, p)


def policial(c, x, y, s, a, col=CYA, k=1.0):
    """marcador do policial: alfinete com bonequinho"""
    if a <= 0 or k <= 0:
        return
    c.save(); c.translate(x, y); c.scale(k, k)
    pth = skia.Path()   # alfinete: círculo com ponta para baixo
    pth.addCircle(0, -s * 1.25, s)
    tri_ = skia.Path(); tri_.moveTo(-s * 0.62, -s * 0.5); tri_.lineTo(0, 0); tri_.lineTo(s * 0.62, -s * 0.5); tri_.close()
    pth = skia.Op(pth, tri_, skia.kUnion_PathOp)
    c.drawPath(pth, blur_paint(col, 0.4 * a, 8))
    c.drawPath(pth, paint(col, a))
    c.drawPath(pth, paint(WHITE, a, stroke=max(2, s * 0.12)))
    c.drawCircle(0, -s * 1.5, s * 0.24, paint(BG0, a))                      # cabeça
    body = skia.Path(); body.addArc(skia.Rect.MakeXYWH(-s * 0.45, -s * 1.22, s * 0.9, s * 0.8), 180, 180)
    c.drawPath(body, paint(BG0, a))                                          # ombros
    c.restore()


def policial_na_pista(c, cx, cy, R, ang, s, a, col=CYA, k=1.0):
    x, y = pt(cx, cy, R, ang)
    policial(c, x, y, s, a, col, k)


def ponto_p(c, cx, cy, R, ang, a, t):
    x, y = pt(cx, cy, R, ang)
    pul = 0.5 + 0.5 * math.sin(t * 5)
    c.drawCircle(x, y, 22, blur_paint(AMB, (0.35 + 0.3 * pul) * a, 10))
    c.drawCircle(x, y, 11, paint(AMB, a))
    c.drawCircle(x, y, 11, paint(BG0, a, stroke=3))
    lx, ly = pt(cx, cy, R - 60, ang)
    label(c, "P", lx, ly, a, 44, AMB, "black")


def cota_arco(c, cx, cy, R, a0, a1, s, a, col=AMB, off=58, size=32):
    """rótulo de um trecho, por fora do anel, no meio do arco"""
    if a <= 0:
        return
    m = (a0 + a1) / 2
    x, y = pt(cx, cy, R + off, m)
    label(c, s, x, y, a, size, col, "black")


def curva(cx, base, R, u):
    """'desenrola' a circunferência de raio R: devolve f(s) → (x, y), s ∈ [−L/2, L/2] medido a partir do ponto de baixo.
    u = 0: círculo com o ponto de baixo em (cx, base); u = 1: segmento horizontal de comprimento L = 2πR."""
    u = clamp(u)
    if u > 0.999:
        return lambda s: (cx + s, base)
    rho = R / (1 - u)

    def f(s):
        ph = s / rho
        return cx + rho * math.sin(ph), base - rho * (1 - math.cos(ph))
    return f


def tracar(c, f, s0, s1, col, a, w, n=None, glow=False):
    if a <= 0 or s1 <= s0:
        return
    n = n or max(8, int((s1 - s0) / 6))
    pth = skia.Path()
    pth.moveTo(*f(s0))
    for i in range(1, n + 1):
        pth.lineTo(*f(s0 + (s1 - s0) * i / n))
    if glow:
        c.drawPath(pth, blur_paint(col, 0.4 * a, 10, stroke=w + 10))
    p = paint(col, a, stroke=w)
    p.setStrokeCap(skia.Paint.kRound_Cap)
    p.setStrokeJoin(skia.Paint.kRound_Join)
    c.drawPath(pth, p)


D12 = 12 * GRAU    # 200 m de 6.000 m


def opcoes(c, y0, a, t, t0, certo=None, errado=None, dim=0.0):
    ops = [("A", "4"), ("B", "8"), ("C", "15"), ("D", "30"), ("E", "60")]
    for i, (le, v) in enumerate(ops):
        y = y0 + i * 118
        k = a * pop(t, t0 + i * 0.15, 0.3)
        if k <= 0:
            continue
        col = MNT if le == certo else (RED if le == errado else CYA)
        fade_k = k * (1 - dim * 0.75 * (le not in (certo, errado)))
        rrect(c, 170, y - 48, 740, 96, 48, BG1, 0.92 * fade_k)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(170, y - 48, 740, 96), 48, 48),
                    paint(col, fade_k, stroke=4 if le in (certo, errado) else 2))
        c.drawCircle(230, y, 34, paint(col, fade_k))
        text_mid(c, le, 230, y, 40, "black", BG0, fade_k)
        text_mid(c, v + " " + L["policiais"], 300, y, 54, "black", WHITE, fade_k, align="left")
        if le == certo:
            check(c, 850, y, 30, k)
        if le == errado:
            cross(c, 850, y, 30, k)


def anel(c, cx, cy, R, a, t, t0, n, passo=0.12, s=24, ang0=0.0, tam=None):
    """n policiais com trechos de tam rad (padrão 24° = 400 m) aparecendo um a um a partir de t0; devolve quantos já apareceram"""
    tam = tam or 2 * D12
    vis = 0
    for i in range(n):
        k = ep(t, t0 + i * passo, 0.3)
        if k <= 0:
            continue
        vis += 1
        a0 = ang0 + i * tam
        arco(c, cx, cy, R, a0, a0 + tam * k, CYA if i % 2 == 0 else MNT, a * 0.9, 26, glow=False)
    for i in range(n):
        if t >= t0 + i * passo:
            policial_na_pista(c, cx, cy, R, ang0 + i * tam + tam / 2, s, a, CYA if i % 2 == 0 else MNT, pop(t, t0 + i * passo, 0.35))
    return vis


def um_policial(c, cx, cy, R, ang, a, t, t0, meia=24 * GRAU, rot=True):
    """um policial com o trecho que ele protege (fora de escala, como na figura do enunciado)"""
    k = ep(t, t0 + 0.2, 0.6)
    arco(c, cx, cy, R, ang - meia * k, ang + meia * k, CYA, a, 30)
    policial_na_pista(c, cx, cy, R, ang, 34, a, CYA, pop(t, t0, 0.4))
    if rot:
        cota_arco(c, cx, cy, R, ang - meia, ang, "200 m", a * ep(t, t0 + 0.8, 0.3), AMB, 112, 40)
        cota_arco(c, cx, cy, R, ang, ang + meia, "200 m", a * ep(t, t0 + 0.8, 0.3), AMB, 112, 40)


# ---------------------------------------------------------------- cenas
LY = 930     # centro da lagoa
LR = 300     # raio da lagoa
P90 = 90 * GRAU   # o policial de exemplo fica à direita (os rótulos cabem dos dois lados)


def b_gancho(c, t, C, B):
    ta, tb, tc = (C[f"01.{k}"] for k in "abc")
    a = ep(t, ta, 0.2) * (1 - prog(t, B["end"] - 0.2, 0.2))
    lagoa(c, CX, LY, LR, a, t)
    kr = a * ep(t, ta + 1.4, 0.3) * (1 - ep(t, tb, 0.2))
    if kr > 0:
        c.drawCircle(CX, LY, 9, paint(WHITE, kr))
        c.drawLine(CX, LY, CX + LR - 14, LY, paint(AMB, kr, stroke=7, cap_round=True))
        label(c, "1 km", CX + LR / 2, LY - 46, kr, 56, AMB, "black")
    if t >= tb:
        um_policial(c, CX, LY, LR, P90, a, t, tb)
    kc = a * ep(t, tc, 0.2)
    if kc > 0:
        k = 1 + 0.04 * math.sin(t * 8)
        c.save(); c.translate(CX, 380); c.scale(k, k); c.translate(-CX, -380)
        big(c, L["quantos"], 330, kc, WHITE, 112)
        big(c, L["policiais_q"], 460, kc, WHITE, 112, hl=L["policiais_q"], hl_col=CYA)
        c.restore()


def b_opcoes(c, t, C, B):
    ta, tb, tc = (C[f"02.{k}"] for k in "abc")
    a = fade(t, B["start"], B["end"], 0.2, 0.15)
    t0 = B["end"] - 2.5   # depois do "Valendo!"
    ko = a * (1 - ep(t, t0, 0.2))
    big(c, L["quantos"], 300, ko, WHITE, 96)
    big(c, L["policiais_q"], 410, ko, WHITE, 96, hl=L["policiais_q"], hl_col=CYA)
    opcoes(c, 580, ko, t, ta + 0.6)
    label(c, L["comenta"], CX, 1200, ko * ep(t, tb, 0.3), 46, AMB, "extrabold")
    if t >= t0:
        kp = a * ep(t, t0, 0.2)
        label(c, L["pausa"], CX, 480, kp, 84, AMB, "black")
        c.save(); c.translate(CX, 820); c.scale(1.5, 1.5); c.translate(-CX, -820)
        contagem(c, CX, 820, kp, t, t0, 2.4)
        c.restore()
        label(c, L["comenta"], CX, 1150, kp, 46, AMB, "extrabold")


def b_volta(c, t, C, B):
    ta, tb = C["03.a"], C["03.b"]
    a = fade(t, B["start"], B["end"], 0.2, 0.2)
    eq(c, [("C = 2 · π · ", WHITE), ("r", AMB)], 330, a * ep(t, ta + 1.2, 0.3), 96, cx=CX, maxw=960)
    R = 150
    u = ease_io(prog(t, tb + 0.6, 1.2))
    base = 1000
    lagoa(c, CX, base - R, R, a * (1 - u), t, pista=0)
    Lc = 2 * math.pi * R
    f = curva(CX, base, R, u)
    tracar(c, f, -Lc / 2, Lc / 2, PISTA, a, 16, n=160)
    kr = a * (1 - u) * ep(t, ta + 1.6, 0.3)
    if kr > 0:
        c.drawCircle(CX, base - R, 7, paint(WHITE, kr))
        c.drawLine(CX, base - R, CX + R - 10, base - R, paint(AMB, kr, stroke=6, cap_round=True))
        label(c, "r", CX + R / 2, base - R - 34, kr, 46, AMB, "black")
    eq(c, [("C = 2 · ", WHITE), ("3", AMB), (" · ", WHITE), (n_("1.000"), AMB)], 480, a * ep(t, tb, 0.3), 84, cx=CX, maxw=960)
    kk = a * ep(t, tb + 1.7, 0.3)
    if kk > 0:
        x0 = CX - Lc / 2
        for i in range(7):
            x = x0 + Lc * i / 6
            c.drawLine(x, base + 22, x, base + 48, paint(WHITE, kk, stroke=3))
            label(c, str(i), x, base + 80, kk, 34, INK2, "bold")
        label(c, "km", x0 + Lc + 46, base + 80, kk, 34, INK2, "bold")
        eq(c, [("C = ", WHITE), (n_("6.000") + " m", CYA)], 660, kk, 104, cx=CX, maxw=960, box=CYA)


def b_pegadinha(c, t, C, B):
    ta, tb = C["04.a"], C["04.b"]
    a = fade(t, B["start"], B["end"], 0.2, 0.2)
    ka = a * (1 - ep(t, tb + 1.0, 0.25))
    pos = eq(c, [(n_("6.000") + " ÷ 200 = ", WHITE), ("30", RED)], 360, ka * ep(t, ta, 0.3), 88, cx=CX, maxw=960)
    opcoes(c, 560, ka, t, ta + 1.4, errado="D", dim=1.0)
    stamp(c, L["peg"], CX, 1190, RED, ka * ep(t, tb, 0.2), 76)
    kb = a * ep(t, tb + 1.0, 0.3)
    if kb > 0:
        big(c, L["cada_lado"], 330, kb, WHITE, 96, hl=L["cada_lado"].split()[-1], hl_col=AMB)
        lagoa(c, CX, LY, LR, kb, t)
        um_policial(c, CX, LY, LR, P90, kb, t, tb + 1.2)


def b_cobertura(c, t, C, B):
    ta, tb = C["05.a"], C["05.b"]
    a = fade(t, B["start"], B["end"], 0.2, 0.2)
    ka = a * (1 - ep(t, tb, 0.25))
    if ka > 0:
        lagoa(c, CX, LY, LR, ka, t)
        um_policial(c, CX, LY, LR, P90, ka, t, B["start"] - 10, rot=False)
        cota_arco(c, CX, LY, LR, P90, P90 + 24 * GRAU, L["frente"], ka * ep(t, ta, 0.3), CYA, 125, 40)
        cota_arco(c, CX, LY, LR, P90 - 24 * GRAU, P90, L["atras"], ka * ep(t, ta + 1.2, 0.3), CYA, 110, 40)
        eq(c, [("200 + 200 = ", WHITE), ("400 m", CYA)], 360, ka * ep(t, ta + 2.0, 0.3), 100, cx=CX, maxw=960, box=CYA)
    kb = a * ep(t, tb, 0.3)
    if kb > 0:
        eq(c, [(n_("6.000") + " ÷ 400 = ", WHITE), ("15", MNT)], 360, kb, 100, cx=CX, maxw=960, box=MNT)
        lagoa(c, CX, LY, LR, kb, t)
        vis = anel(c, CX, LY, LR, kb, t, tb + 0.3, 15, 0.12)
        if vis:
            label(c, str(vis), CX, LY - 10, kb, 150, WHITE, "black")


def b_resposta(c, t, C, B):
    ta, tb = C["06.a"], C["06.b"]
    a = fade(t, B["start"], B["end"], 0.2, 0.2)
    ka = a * (1 - ep(t, tb, 0.25))
    if ka > 0:
        k = pop(t, ta, 0.4)
        c.save(); c.translate(CX, 380); c.scale(k, k); c.translate(-CX, -380)
        glow_text(c, "15", CX, 430, 230, "black", MNT, ka, glow=0.3)
        c.restore()
        label(c, L["policiais"].upper(), CX, 520, ka, 64, WHITE, "black")
        # com 14: o buraco de 400 m pisca embaixo
        g0 = 168 * GRAU   # o buraco de 400 m: 168°–192° (embaixo); os 14 policiais começam em 192°
        lagoa(c, CX, LY + 40, LR - 20, ka, t)
        anel(c, CX, LY + 40, LR - 20, ka, t, B["start"] - 10, 14, 0.0, s=22, ang0=g0 + 2 * D12)
        kg = ka * ep(t, ta + 1.0, 0.3)
        if kg > 0:
            pul = 0.55 + 0.45 * math.sin(t * 7)
            arco(c, CX, LY + 40, LR - 20, g0, g0 + 2 * D12, RED, kg * pul, 30)
            label(c, "14", CX, LY + 30, kg, 130, WHITE, "black")
            label(c, "400 m " + L["sem"], CX, LY + 40 + LR + 50, kg, 44, RED, "black")
    kb = a * ep(t, tb, 0.3)
    if kb > 0:
        big(c, L["letra"], 340, kb, WHITE, 110, hl="C", hl_col=MNT)
        opcoes(c, 560, kb, t, tb - 0.4, certo="C", errado="D", dim=1.0)


def b_final(c, t, C, B):
    ta, tb = C["07.a"], C["07.b"]
    a = ep(t, B["start"], 0.2)
    ka = a * (1 - ep(t, tb, 0.25))
    if ka > 0:
        big(c, L["acertou"], 380, ka, WHITE, 104, hl=L["acertou"].split()[-1], hl_col=AMB)
        opcoes(c, 560, ka, t, ta - 1.0, certo="C")
        label(c, L["conta"], CX, 1180, ka * ep(t, ta + 0.8, 0.3), 50, AMB, "extrabold")
    kb = a * ep(t, tb, 0.3)
    if kb > 0:
        cartao(c, 120, 330, 840, 760, kb, CYA, L["aula"])
        lagoa(c, CX, 680, 150, kb, t)
        anel(c, CX, 680, 150, kb, t, tb + 0.2, 15, 0.05, s=14)
        text_mid(c, L["passo"], CX, 930, 46, "extrabold", WHITE, kb)
        glow_text(c, L["canal"], CX, 1040, 96, "black", WHITE, kb * ep(t, tb + 1.0, 0.3), glow=0.14)
        w = text_w(L["canal"], "black", 96)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(CX - w / 2, 1066, w * ep(t, tb + 1.3, 0.6), 12), 6, 6), paint(AMB, kb))


BLOCKS = dict(gancho=b_gancho, opcoes=b_opcoes, volta=b_volta, pegadinha=b_pegadinha, cobertura=b_cobertura,
              resposta=b_resposta, final=b_final)
