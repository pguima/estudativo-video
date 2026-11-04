"""Visual — Estudativo · Short 013 (vertical 1080x1920): ENEM 2025, questão 138, o caminhão-tanque (aula completa: 012).
render.py <proj> --vertical. Paleta e notação do design system de matemática (_ferramentas/matematica.py), com o layout de
Short do 011 (selo no alto, título grande, figura no meio, legenda de 1 a 3 palavras, contagem para pausar) e o caminhão
da aula 012. Cores com função: âmbar = dado (10.200, 9.900, o combustível), ciano = incógnita (quanto enviar),
menta = certo / o que chega, coral = o descarte e a pegadinha."""
import idioma
import matematica
from matematica import *  # noqa
from matematica import _num

IDIOMAS_NO_CODIGO = True
EN = idioma.LANG == "en"
ARQUIVO_FINAL = "estudativo_short_013_combustivel_descarte.mp4"
MARCA = ""

SOM = dict(intro=False, ganho_trilha=0.32, lufs=-14, bpm=118, sfx={
    "01.a": ["pop", "whoosh@+2.4"], "01.b": "data", "01.c": "impact",
    "02.a": ["pop", "pop@+0.9", "pop@+1.8", "pop@+2.7", "pop@+3.6"], "02.b": "notif",
    "02.c": ["alert", "tick@+1.87", "tick@+2.67", "tick2@+3.47"],   # tiques do cronômetro 3-2-1
    "03.a": "shimmer", "03.b": "impact",
    "04.a": "deny", "04.b": ["impact", "deny@+0.3"],
    "05.a": "whoosh", "05.b": ["data", "impact@+1.6"],
    "06.a": ["impact", "shimmer@+0.3"], "06.b": "confirm",
    "07.a": "notif", "07.b": "lock"})

T = dict(   # (inglês, português)
    selo=("ENEM 2025 · MATH QUESTION", "ENEM 2025 · QUESTÃO DE MATEMÁTICA"),
    quanto=("HOW MUCH", "QUANTO"), enviar=("TO SEND?", "ENVIAR?"),
    enviou=("sent", "enviou"), chegou=("arrived", "chegou"), dobro=("new order: 2 × 10,000", "novo pedido: 2 × 10.000"),
    comenta=("comment before you see it ↓", "comenta antes de ver ↓"), pausa=("PAUSE AND THINK", "PAUSE E PENSE"),
    descarte=("DISCARD", "DESCARTE"), peg=("TRAP!", "PEGADINHA!"), fixo=("IT DOESN'T DOUBLE", "NÃO DOBRA"),
    sempre=("every trip: −300 L", "toda viagem: −300 L"),
    chegam=("20,000 L arrive", "chegam 20.000 L"), letra=("ANSWER C", "LETRA C"),
    acertou=("DID YOU GET IT?", "VOCÊ ACERTOU?"), conta=("tell me in the comments ↓", "conta nos comentários ↓"),
    aula=("FULL LESSON", "AULA COMPLETA"), passo=("step by step on the channel", "passo a passo no canal"),
    canal=("ESTUDATIVO ENGLISH", "ESTUDATIVO"),
)
L = {k: (v[0] if EN else v[1]) for k, v in T.items()}


def _mil(n):
    """'vinte mil e trezentos' → '20.300'"""
    k, r = divmod(n, 1000)
    s = ("" if k == 1 else matematica._extenso_pt(k) + " ") + "mil"
    return s + (" e " + matematica._extenso_pt(r) if r else ""), f"{n:,}".replace(",", ".")


_VALORES = (10000, 10200, 9900, 20000, 20100, 20200, 20300, 20400, 20600)
_EXTRA = [] if EN else (
    [("dois mil e vinte e cinco", "2025")]
    + [(f + " litros", d + " L") for f, d in map(_mil, _VALORES)] + [_mil(v) for v in _VALORES]
    + [("trezentos litros", "300 L"), ("duas vezes", "2 ×")])
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
METAL = "#D7E0EE"


def caminhao(c, cx, gy, s, a, nivel, t, cor=AMB, txt=None, txt_col=None):
    """caminhão-tanque de lado: tanque (cápsula) centrado em cx, rodas no chão gy, escala s (s = 1 → ~500 px).
    nivel ∈ [0, 1] = fração do tanque cheia (com ondinha na superfície); txt = número escrito no tanque"""
    if a <= 0:
        return
    c.save(); c.translate(cx, gy); c.scale(s, s)
    tx0, tx1, ty0, ty1 = -260, 90, -230, -70
    tank = skia.RRect.MakeRectXY(skia.Rect.MakeLTRB(tx0, ty0, tx1, ty1), 80, 80)
    rrect(c, -270, -64, 510, 18, 6, "#5B6B88", a)                                     # chassi
    cab = skia.Path(); cab.moveTo(108, -60); cab.lineTo(108, -170); cab.lineTo(185, -170); cab.lineTo(235, -112)
    cab.lineTo(240, -60); cab.close()
    c.drawPath(cab, paint(BG2, a)); c.drawPath(cab, paint(METAL, a, stroke=5))
    win = skia.Path(); win.moveTo(126, -150); win.lineTo(180, -150); win.lineTo(214, -112); win.lineTo(126, -112); win.close()
    c.drawPath(win, paint(CYA, 0.45 * a))
    c.drawRRect(tank, paint(BG2, 0.9 * a))
    if nivel > 0:   # combustível
        c.save(); c.clipRRect(tank, True)
        y = ty1 - (ty1 - ty0) * clamp(nivel)
        pth = skia.Path(); pth.moveTo(tx0, ty1)
        for i in range(0, 41):
            x = tx0 + (tx1 - tx0) * i / 40
            pth.lineTo(x, y + 4 * math.sin(x / 26 + t * 3))
        pth.lineTo(tx1, ty1); pth.close()
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeLinear([(0, ty0), (0, ty1)], [hexc("#FFD36A"), hexc(cor)]))
        p.setAlphaf(0.9 * a)
        c.drawPath(pth, p)
        c.restore()
    c.drawRRect(tank, paint(METAL, a, stroke=6))
    for x in (-200, -110, 170):   # rodas
        c.drawCircle(x, -30, 32, paint("#1B2236", a)); c.drawCircle(x, -30, 32, paint(METAL, a, stroke=5))
        c.drawCircle(x, -30, 10, paint(METAL, a))
    if txt:
        txt_col = txt_col or (BG0 if nivel > 0.55 else WHITE)   # escuro sobre o combustível, claro sobre o tanque vazio
        glow_text(c, txt, (tx0 + tx1) / 2, (ty0 + ty1) / 2, 50, "black", txt_col, a, glow=0.1)
    c.restore()


def gota(c, x, y, r, a, cor=RED):
    """gota (o combustível descartado): ponta para cima, centro da parte redonda em (x, y)"""
    if a <= 0:
        return
    pth = skia.Path(); pth.addCircle(x, y, r)
    tri_ = skia.Path(); tri_.moveTo(x - r * 0.86, y - r * 0.5); tri_.lineTo(x, y - r * 2.1); tri_.lineTo(x + r * 0.86, y - r * 0.5)
    tri_.close()
    pth = skia.Op(pth, tri_, skia.kUnion_PathOp)
    c.drawPath(pth, blur_paint(cor, 0.45 * a, 8))
    c.drawPath(pth, paint(cor, a))
    c.drawCircle(x - r * 0.35, y - r * 0.2, r * 0.22, paint(WHITE, 0.6 * a))


def descarte(c, cx, gy, s, a, t, t0, txt="−300 L"):
    """gota caindo da válvula do tanque (atrás do caminhão) com o rótulo do descarte; repete a cada 1,6 s a partir de t0"""
    if a <= 0 or t < t0:
        return
    vx, vy = cx - 285 * s, gy - 58 * s   # cano na traseira do chassi
    c.drawLine(vx + 15 * s, vy, vx, vy, paint(METAL, a, stroke=7 * s, cap_round=True))
    c.drawLine(vx, vy, vx, vy + 22 * s, paint(METAL, a, stroke=7 * s, cap_round=True))
    u = ((t - t0) % 1.6) / 1.6
    gota(c, vx, vy + 50 * s + 70 * s * ease_io(u), 18 * s, a * (1 - u * 0.6))
    label(c, txt, vx + 26 * s, vy + 110 * s, a * ep(t, t0, 0.3), 46, RED, "black", "left")   # no Short: embaixo, à direita da gota (a borda corta à esquerda)


def seta(c, x0, y0, x1, y1, a, col=INK2, w=6):
    if a <= 0:
        return
    c.drawLine(x0, y0, x1, y1, paint(col, a, stroke=w, cap_round=True))
    ang = math.atan2(y1 - y0, x1 - x0)
    pth = skia.Path(); pth.moveTo(x1 + 4 * math.cos(ang), y1 + 4 * math.sin(ang))
    for d in (2.5, -2.5):
        pth.lineTo(x1 - 22 * math.cos(ang + d * 0.2), y1 - 22 * math.sin(ang + d * 0.2))
    pth.close()
    c.drawPath(pth, paint(col, a))



def opcoes(c, y0, a, t, t0, certo=None, errado=None, dim=0.0):
    ops = [("A", "20.100"), ("B", "20.200"), ("C", "20.300"), ("D", "20.400"), ("E", "20.600")]
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
        text_mid(c, n_(v) + " L", 300, y, 54, "black", WHITE, fade_k, align="left")
        if le == certo:
            check(c, 850, y, 30, k)
        if le == errado:
            cross(c, 850, y, 30, k)


# ---------------------------------------------------------------- cenas
S = 1.45                 # escala do caminhão
TX = CX + 15 * S         # centro do tanque (o caminhão inteiro fica centralizado)
GY = 1180                # chão do caminhão


def b_gancho(c, t, C, B):
    ta, tb, tc = (C[f"01.{k}"] for k in "abc")
    a = ep(t, ta, 0.2) * (1 - prog(t, B["end"] - 0.2, 0.2))
    caminhao(c, TX, GY, S, a, 0.34, t, txt=n_("10.200") if t >= tb else None)
    descarte(c, TX, GY, S, a * ep(t, ta + 2.4, 0.3), t, ta + 2.4, "?" if t < tb else "−300 L")
    kb = a * ep(t, tb, 0.3)
    if kb > 0:
        eq(c, [(L["enviou"] + " ", INK2), (n_("10.200"), AMB), ("  →  " + L["chegou"] + " ", INK2), (n_("9.900"), MNT)],
           640, kb, 56, cx=CX, maxw=980)
    kc = a * ep(t, tc, 0.2)
    if kc > 0:
        label(c, L["dobro"], CX, 740, kc, 52, CYA, "black")
        k = 1 + 0.04 * math.sin(t * 8)
        c.save(); c.translate(CX, 380); c.scale(k, k); c.translate(-CX, -380)
        big(c, L["quanto"], 330, kc, WHITE, 120)
        big(c, L["enviar"], 470, kc, WHITE, 120, hl=L["enviar"], hl_col=CYA)
        c.restore()


def b_opcoes(c, t, C, B):
    ta, tb, tc = (C[f"02.{k}"] for k in "abc")
    a = fade(t, B["start"], B["end"], 0.2, 0.15)
    t0 = B["end"] - 2.5   # depois do "Valendo!"
    ko = a * (1 - ep(t, t0, 0.2))
    big(c, L["quanto"], 300, ko, WHITE, 96)
    big(c, L["enviar"], 420, ko, WHITE, 96, hl=L["enviar"], hl_col=CYA)
    opcoes(c, 580, ko, t, ta + 0.6, dim=0.0)
    label(c, L["comenta"], CX, 1200, ko * ep(t, tb, 0.3), 46, AMB, "extrabold")
    if t >= t0:
        kp = a * ep(t, t0, 0.2)
        label(c, L["pausa"], CX, 480, kp, 84, AMB, "black")
        c.save(); c.translate(CX, 820); c.scale(1.5, 1.5); c.translate(-CX, -820)
        contagem(c, CX, 820, kp, t, t0, 2.4)
        c.restore()
        label(c, L["comenta"], CX, 1150, kp, 46, AMB, "extrabold")


def b_descarte(c, t, C, B):
    ta, tb = C["03.a"], C["03.b"]
    a = fade(t, B["start"], B["end"], 0.2, 0.2)
    big(c, L["descarte"], 320, a * ep(t, ta, 0.3), WHITE, 110, hl=L["descarte"], hl_col=RED)
    eq(c, [(n_("10.200"), AMB), (" − ", WHITE), (n_("9.900"), MNT)], 500, a * ep(t, ta + 1.0, 0.3), 96, cx=CX, maxw=960)
    eq(c, [("= ", WHITE), ("300 L", RED)], 650, a * ep(t, tb, 0.3), 120, cx=CX, maxw=960, box=RED)
    caminhao(c, TX, GY, S, a, 0.34, t, txt=n_("10.200"))
    descarte(c, TX, GY, S, a * ep(t, tb, 0.3), t, tb)


def b_pegadinha(c, t, C, B):
    ta, tb = C["04.a"], C["04.b"]
    a = fade(t, B["start"], B["end"], 0.2, 0.2)
    ka = a * (1 - ep(t, tb + 1.0, 0.25))
    pos = eq(c, [("2 × " + n_("10.200") + " = ", WHITE), (n_("20.400"), RED)], 360, ka * ep(t, ta + 0.6, 0.3), 88, cx=CX, maxw=960)
    opcoes(c, 560, ka, t, ta + 2.6, errado="D", dim=1.0)
    stamp(c, L["peg"], CX, 1190, RED, ka * ep(t, tb, 0.2), 76)
    if pos:
        strike(c, pos[0][0], pos[-1][1], 360, ka, ep(t, tb, 0.3))
    kb = a * ep(t, tb + 1.0, 0.3)
    if kb > 0:   # o descarte é fixo: com 10.000 ou 20.000 L, os mesmos 300
        big(c, L["descarte"], 300, kb, WHITE, 100, hl=L["descarte"], hl_col=RED)
        big(c, L["fixo"], 420, kb * ep(t, tb + 2.6, 0.3), AMB, 100)
        caminhao(c, TX, 790, 1.15, kb, 0.33, t, txt=n_("10.000"))
        descarte(c, TX, 790, 1.15, kb, t, tb + 1.4)
        caminhao(c, TX, 1200, 1.15, kb * ep(t, tb + 1.6, 0.3), 0.67, t, txt=n_("20.000"))
        descarte(c, TX, 1200, 1.15, kb * ep(t, tb + 1.6, 0.3), t, tb + 2.0)


def b_conta(c, t, C, B):
    ta, tb = C["05.a"], C["05.b"]
    a = fade(t, B["start"], B["end"], 0.2, 0.2)
    eq(c, [("2 × " + n_("10.000") + " = ", WHITE), (n_("20.000") + " L", MNT)], 330, a * ep(t, ta, 0.3), 84, cx=CX, maxw=960)
    eq(c, [(n_("20.000"), MNT), (" + ", WHITE), ("300", RED)], 480, a * ep(t, tb, 0.3), 96, cx=CX, maxw=960)
    eq(c, [("= ", WHITE), (n_("20.300") + " L", CYA)], 640, a * ep(t, tb + 1.6, 0.3), 120, cx=CX, maxw=960, box=CYA)
    n = ep(t, ta + 0.3, 1.0) * (20000 / 30000) + ep(t, tb + 0.2, 0.6) * (300 / 30000)
    caminhao(c, TX, GY, S, a, n, t, txt=(n_("20.300") if t >= tb + 1.6 else n_("20.000")) if n > 0.1 else None)
    descarte(c, TX, GY, S, a * ep(t, tb, 0.3), t, tb)


def b_resposta(c, t, C, B):
    ta, tb = C["06.a"], C["06.b"]
    a = fade(t, B["start"], B["end"], 0.2, 0.2)
    ka = a * (1 - ep(t, tb, 0.25))
    if ka > 0:
        k = pop(t, ta, 0.4)
        c.save(); c.translate(CX, 420); c.scale(k, k); c.translate(-CX, -420)
        glow_text(c, n_("20.300"), CX, 440, 190, "black", MNT, ka, glow=0.3)
        c.restore()
        label(c, "LITROS", CX, 560, ka, 64, WHITE, "black")
        caminhao(c, TX, GY - 60, S, ka, 0.68, t, txt=n_("20.300"))
        descarte(c, TX, GY - 60, S, ka, t, ta + 1.2)
        label(c, L["chegam"], CX, GY + 80, ka * ep(t, ta + 2.4, 0.3), 60, MNT, "black")
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
        caminhao(c, CX + 12, 800, 0.95, kb, 0.68, t)
        text_mid(c, L["passo"], CX, 930, 46, "extrabold", WHITE, kb)
        glow_text(c, L["canal"], CX, 1040, 96, "black", WHITE, kb * ep(t, tb + 1.0, 0.3), glow=0.14)
        w = text_w(L["canal"], "black", 96)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(CX - w / 2, 1066, w * ep(t, tb + 1.3, 0.6), 12), 6, 6), paint(AMB, kb))


BLOCKS = dict(gancho=b_gancho, opcoes=b_opcoes, descarte=b_descarte, pegadinha=b_pegadinha, conta=b_conta,
              resposta=b_resposta, final=b_final)
