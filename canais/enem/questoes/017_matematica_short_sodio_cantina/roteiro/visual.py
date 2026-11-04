"""Visual — Estudativo · Short 017 (vertical 1080x1920): ENEM 2025, questão 140, o sódio por pacote (aula: 016).
render.py <proj> --vertical. Paleta e notação do design system de matemática (_ferramentas/matematica.py), com o layout de
Short do 011/013/015 (selo no alto, título grande, figura no meio, legenda de 1 a 3 palavras, contagem para pausar) e os
cartões dos rótulos da aula 016. Cores com função: âmbar = dado do rótulo, ciano = a pergunta (por pacote), menta = certo,
coral = a pegadinha (o menor POR PORÇÃO)."""
import idioma
import matematica
from matematica import *  # noqa
from matematica import _num

IDIOMAS_NO_CODIGO = True
EN = idioma.LANG == "en"
ARQUIVO_FINAL = "estudativo_short_017_sodio_cantina.mp4"
MARCA = ""

SOM = dict(intro=False, ganho_trilha=0.32, lufs=-14, bpm=118, sfx={
    "01.a": ["pop", "data@+1.6"], "01.b": "whoosh", "01.c": "alert",
    "02.a": ["pop", "pop@+0.9", "pop@+1.8", "pop@+2.7", "pop@+3.6"], "02.b": "notif",
    "02.c": ["alert", "tick@+2.65", "tick@+3.45", "tick2@+4.25"],   # tiques do cronômetro 3-2-1 (ajustados ao áudio)
    "03.a": "deny", "03.b": ["impact", "deny@+0.3"],
    "04.a": "whoosh", "04.b": "data", "04.c": "data", "04.d": "data", "04.e": "data", "04.f": "data",
    "05.a": ["impact", "shimmer@+0.3"], "05.b": "confirm", "05.c": "deny",
    "06.a": "notif", "06.b": "lock"})

T = dict(   # (inglês, português)
    selo=("ENEM 2025 · MATH QUESTION", "ENEM 2025 · QUESTÃO DE MATEMÁTICA"),
    qual=("WHICH HAS", "QUAL TEM"), menos=("LESS SODIUM?", "MENOS SÓDIO?"), uma=("label = 1 serving", "rótulo = 1 porção"),
    comenta=("comment before you see it ↓", "comenta antes de ver ↓"), pausa=("PAUSE AND THINK", "PAUSE E PENSE"),
    menor_rot=("SMALLEST ON THE LABEL?", "O MENOR DO RÓTULO?"), peg=("TRAP!", "PEGADINHA!"),
    formula=("servings × sodium", "porções × sódio"), letra=("ANSWER A", "LETRA A"), chips=("potato chips", "batata chips"),
    gramas=("AND THE GRAMS?", "E AS GRAMAS?"), fora=("not in the math", "fora da conta"),
    acertou=("DID YOU GET IT?", "VOCÊ ACERTOU?"), conta=("tell me in the comments ↓", "conta nos comentários ↓"),
    aula=("FULL LESSON", "AULA COMPLETA"), passo=("step by step on the channel", "passo a passo no canal"),
    canal=("ESTUDATIVO ENGLISH", "ESTUDATIVO"),
)
L = {k: (v[0] if EN else v[1]) for k, v in T.items()}
_EXTRA = [] if EN else [("dois mil e vinte e cinco", "2025"), ("dois mil cento e doze", "2.112"), ("dois mil e quatro", "2.004"),
                        ("mil e cinquenta", "1.050")]
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



# ---------------------------------------------------------------- figuras
# (nome, porções, gramas por porção, mg de sódio por porção, alternativa, cor do rótulo na prova) — igual à aula 016
PROD = [("Batata chips", 3, 50, 170, "A", "#8FD3F4"), ("Palitos salgados", 4, 20, 501, "B", "#9BD3AE"),
        ("Biscoito multigrãos", 8, 25, 264, "C", "#B8B3D8"), ("Biscoito de polvilho", 6, 15, 175, "D", "#F7BBA6"),
        ("Biscoito de água e sal", 5, 40, 166, "E", "#FFF59D")]
NOMES_EN = ["Potato chips", "Salted sticks", "Multigrain crackers", "Tapioca biscuits", "Water crackers"]
TOT = [p * s for _, p, _, s, _, _ in PROD]                       # 510, 2004, 2112, 1050, 830
ORDEM = sorted(range(5), key=lambda i: TOT[i])
POS = {i: k for k, i in enumerate(ORDEM)}
CW, CH, PASSO_Y, Y0 = 860, 124, 146, 660                           # cartão maior que na aula (tela de celular)
mg = lambda v: n_(f"{v:,}".replace(",", ".")) + " mg"              # noqa: E731


def nome(i):
    return NOMES_EN[i] if EN else PROD[i][0]


def rotulo(c, i, x, y, a, borda=INK2, glow=0.0, total=0.0, cor_t=MNT, riscar=0.0, cor_s=AMB):
    """cartão do rótulo i (mesmo da aula 016): faixa colorida + letra, nome, '3 porções de 50 g · 170 mg'; à direita,
    o total do pacote (total = alfa). riscar = 0..1 risca as gramas. (x, y) = centro"""
    if a <= 0:
        return
    nm, p, g, sd, le, cor = PROD[i]
    x0, y0 = x - CW / 2, y - CH / 2
    r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x0, y0, CW, CH), 20, 20)
    if glow > 0:
        c.drawRRect(r, blur_paint(borda, 0.5 * a * glow, 16))
    c.drawRRect(r, paint(BG1, 0.95 * a))
    c.save(); c.clipRRect(r, doAntiAlias=True)
    c.drawRect(skia.Rect.MakeXYWH(x0, y0, 16, CH), paint(cor, a))
    c.restore()
    c.drawRRect(r, paint(borda, a, stroke=3.5))
    c.drawCircle(x0 + 60, y, 28, paint(cor, a))
    text_mid(c, le, x0 + 60, y, 32, "black", BG0, a)
    text_mid(c, nome(i), x0 + 108, y - 26, 38, "black", WHITE, a, align="left")
    por = "servings of" if EN else "porções de"
    s1, s2, s3 = f"{p} ", f"{por} ", f"{g} g"
    xx = x0 + 108
    text_mid(c, s1, xx, y + 26, 31, "black", AMB, a, align="left"); xx += text_w(s1, "black", 31)
    text_mid(c, s2, xx, y + 26, 31, "semibold", INK2, a, align="left"); xx += text_w(s2, "semibold", 31)
    xg = xx
    text_mid(c, s3, xx, y + 26, 31, "semibold", INK2, a * (1 - 0.6 * riscar), align="left"); xx += text_w(s3, "semibold", 31)
    if riscar > 0:
        c.drawLine(xg - 4, y + 26, xg - 4 + (xx - xg + 8) * ease_io(riscar), y + 26, paint(RED, a, stroke=5, cap_round=True))
    text_mid(c, f"  ·  {sd} mg", xx, y + 26, 31, "black", cor_s, a, align="left")
    if total > 0:
        text_mid(c, mg(p * sd), x0 + CW - 26, y, 44, "black", cor_t, a * total, align="right")


def coluna(c, a, u=0.0, estilo=None, x=CX, y0=Y0, passo=PASSO_Y):
    """os cinco cartões; u = 0: ordem das alternativas (A..E), u = 1: ordem crescente do total"""
    for i in range(5):
        uu = ease_io(clamp(u * 1.3 - 0.3 * (i / 4)))
        y = y0 + passo * (i + (POS[i] - i) * uu)
        dx = 50 * math.sin(math.pi * uu) * (1 if POS[i] > i else -1) if POS[i] != i else 0
        rotulo(c, i, x + dx, y, a, **((estilo(i) if estilo else None) or {}))


def bolinha(c, x, y, v, a, col=INK2, fundo=BG1, glow=0.0, k=1.0):
    if a <= 0 or k <= 0:
        return
    c.save(); c.translate(x, y); c.scale(k, k)
    if glow:
        c.drawCircle(0, 0, 46, blur_paint(col, 0.5 * a * glow, 14))
    c.drawCircle(0, 0, 42, paint(fundo, 0.95 * a))
    c.drawCircle(0, 0, 42, paint(col, a, stroke=4))
    text_mid(c, str(v), 0, 0, 40, "black", WHITE, a)
    c.restore()


def opcoes(c, y0, a, t, t0, certo=None, errado=None, dim=0.0):
    """as cinco alternativas (nomes dos lanches)"""
    for i in range(5):
        le = PROD[i][4]
        y = y0 + i * 118
        k = a * pop(t, t0 + i * 0.15, 0.3)
        if k <= 0:
            continue
        col = MNT if le == certo else (RED if le == errado else CYA)
        fade_k = k * (1 - dim * 0.75 * (le not in (certo, errado)))
        rrect(c, 120, y - 48, 840, 96, 48, BG1, 0.92 * fade_k)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(120, y - 48, 840, 96), 48, 48),
                    paint(col, fade_k, stroke=4 if le in (certo, errado) else 2))
        c.drawCircle(180, y, 34, paint(col, fade_k))
        text_mid(c, le, 180, y, 40, "black", BG0, fade_k)
        text_mid(c, nome(i), 240, y, 48, "black", WHITE, fade_k, align="left")
        if le == certo:
            check(c, 900, y, 30, k)
        if le == errado:
            cross(c, 900, y, 30, k)


# ---------------------------------------------------------------- cenas
def b_gancho(c, t, C, B):
    ta, tb, tc = (C[f"01.{k}"] for k in "abc")
    a = ep(t, ta, 0.2) * (1 - prog(t, B["end"] - 0.2, 0.2))
    coluna(c, a, 0, lambda i: dict(borda=AMB) if t >= ta + 1.6 + i * 0.12 else None)
    kb = a * ep(t, tb, 0.2)
    if kb > 0:
        k = 1 + 0.04 * math.sin(t * 8)
        c.save(); c.translate(CX, 330); c.scale(k, k); c.translate(-CX, -330)
        big(c, L["qual"], 280, kb, WHITE, 110)
        big(c, L["menos"], 400, kb, WHITE, 110, hl=L["menos"], hl_col=CYA)
        c.restore()
    label(c, L["uma"], CX, 520, a * ep(t, tc + 0.6, 0.3), 48, AMB, "black")


def b_opcoes(c, t, C, B):
    ta, tb, tc = (C[f"02.{k}"] for k in "abc")
    a = fade(t, B["start"], B["end"], 0.2, 0.15)
    t0 = B["end"] - 2.5   # depois do "Valendo!"
    ko = a * (1 - ep(t, t0, 0.2))
    big(c, L["qual"], 300, ko, WHITE, 96)
    big(c, L["menos"], 420, ko, WHITE, 96, hl=L["menos"], hl_col=CYA)
    opcoes(c, 600, ko, t, ta + 0.6)
    label(c, L["comenta"], CX, 1230, ko * ep(t, tb, 0.3), 46, AMB, "extrabold")
    if t >= t0:
        kp = a * ep(t, t0, 0.2)
        label(c, L["pausa"], CX, 480, kp, 84, AMB, "black")
        c.save(); c.translate(CX, 820); c.scale(1.5, 1.5); c.translate(-CX, -820)
        contagem(c, CX, 820, kp, t, t0, 2.4)
        c.restore()
        label(c, L["comenta"], CX, 1150, kp, 46, AMB, "extrabold")


def b_pegadinha(c, t, C, B):
    ta, tb = C["03.a"], C["03.b"]
    a = fade(t, B["start"], B["end"], 0.2, 0.2)
    kr = ep(t, ta + 1.4, 0.3)
    kb = ep(t, tb + 1.0, 0.3)
    coluna(c, a, 0, lambda i: dict(borda=RED, glow=kr, cor_s=RED, total=kb, cor_t=RED) if i == 4 and kr > 0 else None)
    big(c, L["menor_rot"], 300, a * ep(t, ta + 0.4, 0.3) * (1 - ep(t, tb, 0.2)), AMB, 92)
    stamp(c, L["peg"], CX, 270, RED, a * ep(t, tb, 0.2), 76)
    pos = eq(c, [("166 mg → ", WHITE), ("E", RED)], 432, a * kr, 68, cx=CX, maxw=980)
    if pos:
        strike(c, pos[0][0], pos[-1][1], 432, a, ep(t, tb, 0.3))
    eq(c, [("5 × 166 = ", WHITE), ("830 mg", RED)], 535, a * kb, 68, cx=CX, maxw=980)


def b_contas(c, t, C, B):
    ta = C["04.a"]
    ts = [C[f"04.{k}"] for k in "bcdef"]
    a = fade(t, B["start"], B["end"], 0.2, 0.2)
    fins = ts[1:] + [B["end"]]
    atual = max([j for j, t0 in enumerate(ts) if t >= t0], default=-1)

    def est(i):
        if i == atual:
            return dict(borda=AMB, glow=1.0, total=ep(t, ts[i] + 0.55 * (fins[i] - ts[i]), 0.3))
        if i < atual:
            return dict(borda=MNT, total=1.0, cor_t=WHITE)
        return None
    coluna(c, a, 0, est)
    big(c, L["formula"], 300, a * ep(t, ta, 0.3), WHITE, 76, hl=L["formula"].split(" × ")[0], hl_col=AMB)
    if atual >= 0:
        _, p, _, s, _, _ = PROD[atual]
        t0, t1 = ts[atual], fins[atual]
        kj = a * ep(t, t0, 0.2) * (1 - ep(t, t1 - 0.15, 0.15) if atual < 4 else 1)
        eq(c, [(f"{p} × {s} = ", WHITE), (mg(p * s), MNT)], 450, kj, 84, cx=CX, maxw=980)


def b_resposta(c, t, C, B):
    ta, tb, tc = (C[f"05.{k}"] for k in "abc")
    a = fade(t, B["start"], B["end"], 0.2, 0.2)
    u = prog(t, ta + 0.2, 1.2)
    kr = ep(t, tc + 1.4, 0.6)
    coluna(c, a, u, lambda i: dict(borda=MNT if i == 0 else INK2, glow=1.0 if i == 0 else 0, total=1.0,
                                    cor_t=MNT if i == 0 else WHITE, riscar=kr))
    ka = a * (1 - ep(t, tb, 0.25))
    if ka > 0:
        k = pop(t, ta, 0.4)
        c.save(); c.translate(CX, 380); c.scale(k, k); c.translate(-CX, -380)
        glow_text(c, "510 mg", CX, 440, 190, "black", MNT, ka, glow=0.3)
        c.restore()
    kb = a * ep(t, tb, 0.3)
    big(c, L["letra"], 340, kb * (1 - ep(t, tc, 0.25)), WHITE, 110, hl="A", hl_col=MNT)
    label(c, L["chips"], CX, 470, kb * (1 - ep(t, tc, 0.25)), 60, MNT, "black")
    kc = a * ep(t, tc, 0.3)
    big(c, L["gramas"], 330, kc, RED, 88)
    label(c, L["fora"], CX, 470, kc * ep(t, tc + 1.2, 0.3), 60, WHITE, "black")


def b_final(c, t, C, B):
    ta, tb = C["06.a"], C["06.b"]
    a = ep(t, B["start"], 0.2)
    ka = a * (1 - ep(t, tb, 0.25))
    if ka > 0:
        big(c, L["acertou"], 380, ka, WHITE, 104, hl=L["acertou"].split()[-1], hl_col=AMB)
        opcoes(c, 560, ka, t, ta - 1.0, certo="A")
        label(c, L["conta"], CX, 1200, ka * ep(t, ta + 0.8, 0.3), 50, AMB, "extrabold")
    kb = a * ep(t, tb, 0.3)
    if kb > 0:
        cartao(c, 120, 330, 840, 760, kb, CYA, L["aula"])
        for j, v in enumerate("ABCDE"):
            bolinha(c, CX - 280 + j * 140, 680, v, kb, MNT if j == 0 else INK2, glow=1.0 if j == 0 else 0, k=1.0)
        text_mid(c, L["passo"], CX, 860, 46, "extrabold", WHITE, kb)
        glow_text(c, L["canal"], CX, 1000, 96, "black", WHITE, kb * ep(t, tb + 1.0, 0.3), glow=0.14)
        w = text_w(L["canal"], "black", 96)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(CX - w / 2, 1026, w * ep(t, tb + 1.3, 0.6), 12), 6, 6), paint(AMB, kb))


BLOCKS = dict(gancho=b_gancho, opcoes=b_opcoes, pegadinha=b_pegadinha, contas=b_contas, resposta=b_resposta,
              final=b_final)
