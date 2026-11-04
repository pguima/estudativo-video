"""Visual — Estudativo · Short 019 (vertical 1080x1920): ENEM 2025, questão 141, as cores do poliedro (aula: 018).
render.py <proj> --vertical. Paleta e notação do design system de matemática (_ferramentas/matematica.py), com o layout de
Short do 011/013/015 (selo no alto, título grande, figura no meio, legenda de 1 a 3 palavras, contagem para pausar) e os
o protótipo em 3D da aula 018 (solido()). Cores das quatro classes de faces: âmbar (hexágono de baixo), ciano (retângulos),
menta (trapézios), rosa (hexágono de cima); coral = a pegadinha (os dois hexágonos da mesma cor)."""
import idioma
import matematica
from matematica import *  # noqa
from matematica import _num

IDIOMAS_NO_CODIGO = True
EN = idioma.LANG == "en"
ARQUIVO_FINAL = "estudativo_short_019_poliedro_cores.mp4"
MARCA = ""

SOM = dict(intro=False, ganho_trilha=0.32, lufs=-14, bpm=118, sfx={
    "01.a": ["pop", "whoosh@+1.6"], "01.b": "data", "01.c": "alert",
    "02.a": ["pop", "pop@+0.6", "pop@+1.2", "pop@+1.8", "pop@+2.4"], "02.b": "notif",
    "02.c": ["alert", "tick@+1.87", "tick@+2.67", "tick2@+3.47"],   # tiques do cronômetro 3-2-1 (ajustados ao áudio)
    "03.a": "deny", "03.b": ["impact", "deny@+0.3"],
    "04.a": "whoosh", "04.b": "confirm", "04.c": "confirm", "04.d": "confirm", "04.e": "confirm",
    "05.a": ["impact", "shimmer@+0.3"], "05.b": "confirm", "05.c": "data", "05.d": "whoosh",
    "06.a": "notif", "06.b": "lock"})

ROSA = "#FF8FB1"
COR = dict(base=AMB, ret=CYA, trap=MNT, topo=ROSA)

T = dict(   # (inglês, português)
    selo=("ENEM 2025 · MATH QUESTION", "ENEM 2025 · QUESTÃO DE MATEMÁTICA"),
    quantas=("HOW MANY", "QUANTAS"), cores=("COLORS?", "CORES?"), regra=("congruent faces → same color", "faces congruentes → mesma cor"),
    comenta=("comment before you see it ↓", "comenta antes de ver ↓"), pausa=("PAUSE AND THINK", "PAUSE E PENSE"),
    mesma=("SAME COLOR?", "MESMA COR?"), peg=("TRAP!", "PEGADINHA!"), tres=("3 colors → E", "3 cores → E"),
    menor=("smaller: NOT congruent", "menor: NÃO é congruente"),
    dentro=("glued bases → inside", "bases coladas → dentro"), letra=("ANSWER D", "LETRA D"),
    tipos=("14 faces · 4 kinds", "14 faces · 4 tipos"), piramide=("A FULL PYRAMID?", "PIRÂMIDE INTEIRA?"),
    tres_c=("3 COLORS", "3 CORES"), cong=("same shape AND same size", "mesma forma E mesmo tamanho"),
    acertou=("DID YOU GET IT?", "VOCÊ ACERTOU?"), conta=("tell me in the comments ↓", "conta nos comentários ↓"),
    aula=("FULL LESSON", "AULA COMPLETA"), passo=("step by step on the channel", "passo a passo no canal"),
    canal=("ESTUDATIVO ENGLISH", "ESTUDATIVO"),
)
L = {k: (v[0] if EN else v[1]) for k, v in T.items()}
_EXTRA = [] if EN else [("dois mil e vinte e cinco", "2025")]
matematica.NUMEROS_EXTRA[:] = sorted(_EXTRA, key=lambda p: -len(p[0].split()))
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





# ---------------------------------------------------------------- o sólido em 3D
def _faces(n=6, R=1.0, H=1.1, r=0.55, F=0.75, explode=0.0, ponta=False):
    """faces do protótipo (coordenadas do mundo, y para cima): lista de (tipo, sólido, [vértices]).
    sólido 0 = prisma (y de 0 a H), 1 = tronco (y de H a H + F, deslocado para cima por explode)"""
    ang = [2 * math.pi * k / n + math.pi / n for k in range(n)]
    P = lambda rr, y: [(rr * math.cos(a), y, rr * math.sin(a)) for a in ang]   # noqa: E731
    b0, b1 = P(R, 0), P(R, H)
    y2 = H + explode
    g0, g1 = P(R, y2), ([(0, y2 + F, 0)] * n if ponta else P(r, y2 + F))
    out = [("base", 0, b0[::-1]), ("cola", 0, b1)]
    for k in range(n):
        j = (k + 1) % n
        out.append(("ret", 0, [b0[k], b0[j], b1[j], b1[k]]))
    out.append(("cola", 1, g0[::-1]))
    if not ponta:
        out.append(("topo", 1, g1))
    for k in range(n):
        j = (k + 1) % n
        out.append(("trap", 1, [g0[k], g0[j], g1[j], g1[k]] if not ponta else [g0[k], g0[j], g1[0]]))
    return out


def solido(c, cx, cy, s, t, a=1.0, yaw=None, pitch=0.42, explode=0.0, pintura=None, so=None, hl=None, n=6, R=1.0, H=1.1,
           r=0.55, F=0.75, ponta=False, fundo=None):
    """desenha o protótipo. pintura = {tipo: alfa da cor} (0 = cinza-azulado); so = {sólidos visíveis};
    hl = {tipo: alfa de um contorno âmbar}; cy = altura do centro do prisma; fundo = alfa das faces de trás (tracejado)"""
    if a <= 0:
        return
    yaw = (0.35 + 0.18 * t) if yaw is None else yaw
    cyw, syw, cp, sp = math.cos(yaw), math.sin(yaw), math.cos(pitch), math.sin(pitch)
    ymid = (H + F + explode) / 2

    def rot(p):
        x, y, z = p
        return (x * cyw + z * syw, y - ymid, -x * syw + z * cyw)

    def proj(q):
        return (cx + s * q[0], cy - s * (q[1] * cp) + s * q[2] * sp)
    v = (0.0, sp, cp)                                         # direção de quem olha (de cima e da frente)
    luz = (-0.35, 0.8, 0.5)
    faces = _faces(n, R, H, r, F, explode, ponta)
    centros = {}
    for so_ in (0, 1):
        pts = [p for _, k, vs in faces if k == so_ for p in vs]
        centros[so_] = [sum(q[i] for q in pts) / len(pts) for i in range(3)]
    pintura = pintura or {}
    hl = hl or {}
    for so_ in ((0, 1) if sp >= 0 else (1, 0)):   # de cima, o tronco por último; de baixo, o prisma por último
        if so is not None and so_ not in so:
            continue
        cen = rot(centros[so_])
        desenhar = []
        for tipo, k, vs in faces:
            if k != so_ or (tipo == "cola" and explode < 0.02 and so is None):   # juntas, as bases coladas somem
                continue
            q = [rot(p) for p in vs]
            u = [q[1][i] - q[0][i] for i in range(3)]
            w = [q[-1][i] - q[0][i] for i in range(3)]
            nn = [u[1] * w[2] - u[2] * w[1], u[2] * w[0] - u[0] * w[2], u[0] * w[1] - u[1] * w[0]]
            fc = [sum(p[i] for p in q) / len(q) for i in range(3)]
            if sum(nn[i] * (fc[i] - cen[i]) for i in range(3)) < 0:
                nn = [-x for x in nn]
            ln = math.sqrt(sum(x * x for x in nn)) or 1
            nn = [x / ln for x in nn]
            vis = sum(nn[i] * v[i] for i in range(3)) > 1e-6
            desenhar.append((vis, tipo, q, nn))
        if fundo:
            for vis, tipo, q, nn in desenhar:
                if not vis:
                    pth = skia.Path(); pth.addPoly([skia.Point(*proj(p)) for p in q], True)
                    pd = paint(INK2, a * fundo * 0.6, stroke=2); pd.setPathEffect(skia.DashPathEffect.Make([8, 8], 0))
                    c.drawPath(pth, pd)
        for vis, tipo, q, nn in desenhar:
            if not vis:
                continue
            br = 0.55 + 0.45 * max(0.0, sum(nn[i] * luz[i] for i in range(3)) / 1.03)
            pth = skia.Path(); pth.addPoly([skia.Point(*proj(p)) for p in q], True)
            base = mix_hex(BG2, "#3A4F7A", br)
            kp = pintura.get(tipo, 0.0)
            cor = mix_hex(base, mix_hex("#000000", COR.get(tipo, RED if tipo == "cola" else AMB), 0.45 + 0.55 * br), kp)
            c.drawPath(pth, paint(cor, a))
            c.drawPath(pth, paint(WHITE if kp < 0.5 else BG0, a * 0.75, stroke=2.5))
            if hl.get(tipo, 0) > 0:
                c.drawPath(pth, paint(AMB, a * hl[tipo], stroke=6))


def mix_hex(c1, c2, u):
    """mistura de duas cores '#RRGGBB' (u = 0 → c1, 1 → c2)"""
    u = clamp(u)
    a_ = [int(c1[i:i + 2], 16) for i in (1, 3, 5)]
    b_ = [int(c2[i:i + 2], 16) for i in (1, 3, 5)]
    return "#" + "".join(f"{int(round(x + (y - x) * u)):02X}" for x, y in zip(a_, b_))


def hexagono(c, cx, cy, R, cor, a, stroke=False):
    pth = skia.Path()
    pth.addPoly([skia.Point(cx + R * math.cos(math.pi / 3 * k), cy + R * math.sin(math.pi / 3 * k)) for k in range(6)], True)
    c.drawPath(pth, paint(cor, a, stroke=4) if stroke else paint(cor, a))




OPS = [("A", "9"), ("B", "8"), ("C", "6"), ("D", "4"), ("E", "3")]


def opcoes(c, y0, a, t, t0, certo=None, errado=None, dim=0.0):
    """as cinco alternativas (número de cores)"""
    for i, (le, v) in enumerate(OPS):
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
        text_mid(c, v + (" colors" if EN else " cores"), 300, y, 54, "black", WHITE, fade_k, align="left")
        if le == certo:
            check(c, 850, y, 30, k)
        if le == errado:
            cross(c, 850, y, 30, k)


FY = 900   # centro do sólido na tela do Short


# ---------------------------------------------------------------- cenas
def b_gancho(c, t, C, B):
    ta, tb, tc = (C[f"01.{k}"] for k in "abc")
    a = ep(t, ta, 0.2) * (1 - prog(t, B["end"] - 0.2, 0.2))
    ex = 0.8 * (1 - ease_io(prog(t, ta + 1.4, 1.0)))
    solido(c, CX, FY + 40, 290, t, a, explode=ex)
    kb = a * ep(t, tb, 0.2)
    label(c, L["regra"], CX, 500, kb, 46, AMB, "black")
    kc = a * ep(t, ta + 0.3, 0.2)   # a pergunta já no começo (Short: pergunta nos 3 primeiros segundos)
    if kc > 0:
        k = 1 + 0.04 * math.sin(t * 8) * ep(t, tc, 0.2)
        c.save(); c.translate(CX, 330); c.scale(k, k); c.translate(-CX, -330)
        big(c, L["quantas"], 280, kc, WHITE, 120)
        big(c, L["cores"], 400, kc, WHITE, 120, hl=L["cores"], hl_col=CYA)
        c.restore()


def b_opcoes(c, t, C, B):
    ta, tb, tc = (C[f"02.{k}"] for k in "abc")
    a = fade(t, B["start"], B["end"], 0.2, 0.15)
    t0 = B["end"] - 2.5   # depois do "Valendo!"
    ko = a * (1 - ep(t, t0, 0.2))
    big(c, L["quantas"], 300, ko, WHITE, 100)
    big(c, L["cores"], 420, ko, WHITE, 100, hl=L["cores"], hl_col=CYA)
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
    kh = a * ep(t, ta + 0.3, 0.3)
    u = ease_io(prog(t, tb + 3.4, 1.2))   # o menor vai para cima do maior: não cobre
    hexagono(c, CX - 170 + 170 * u, 900, 230, AMB, kh * 0.3)
    hexagono(c, CX - 170 + 170 * u, 900, 230, AMB, kh, stroke=True)
    x2 = CX + 270 - 270 * u
    hexagono(c, x2, 900, 130, RED if t >= tb else ROSA, kh * 0.4)
    hexagono(c, x2, 900, 130, RED if t >= tb else ROSA, kh, stroke=True)
    big(c, L["mesma"], 300, a * ep(t, ta + 0.4, 0.3) * (1 - ep(t, tb, 0.2)), AMB, 100)
    stamp(c, L["peg"], CX, 280, RED, a * ep(t, tb, 0.2), 76)
    pos = eq(c, [(L["tres"], WHITE)], 450, a * ep(t, ta + 2.6, 0.3), 70, cx=CX, maxw=980)
    if pos:
        strike(c, pos[0][0], pos[-1][1], 450, a, ep(t, tb, 0.3))
    label(c, L["cong"], CX, 580, a * ep(t, tb + 1.0, 0.3), 50, CYA, "black")
    label(c, L["menor"], CX, 1240, a * ep(t, tb + 4.2, 0.3), 54, RED, "black")


def b_faces(c, t, C, B):
    ta, tb, tc, td, te = (C[f"04.{k}"] for k in "abcde")
    a = fade(t, B["start"], B["end"], 0.2, 0.2)
    ex = 0.7 * (1 - ease_io(prog(t, ta + 1.2, 1.2)))
    kc = ep(t, ta + 0.3, 0.3) * (1 - ep(t, ta + 2.2, 0.4))
    pint = dict(cola=kc, ret=ep(t, tb + 0.6, 0.4), trap=ep(t, tc + 0.6, 0.4), base=ep(t, td + 0.6, 0.4), topo=ep(t, te + 0.8, 0.4))
    pv = 0.42 + (-0.35 - 0.42) * ep(t, td - 0.3, 0.5) * (1 - ep(t, te - 0.3, 0.5))   # vira por baixo no hexágono de baixo
    solido(c, CX, FY, 300, t, a, explode=ex, pitch=pv, pintura=pint, fundo=0.6 * (1 - ep(t, ta + 2.2, 0.4)))
    label(c, L["dentro"], CX, 330, a * ep(t, ta + 0.4, 0.3) * (1 - ep(t, tb, 0.2)), 56, RED, "black")
    linhas = [(tb, "ret"), (tc, "trap"), (td, "base"), (te, "topo")]
    for j, (t0, k) in enumerate(linhas):   # os quatro quadradinhos de cor, um por tipo
        kk = a * pop(t, t0 + 0.6, 0.3)
        if kk > 0:
            x = CX - 255 + j * 170
            rrect(c, x - 55, 330 - 55, 110, 110, 22, COR[k], kk)
            text_mid(c, str(j + 1), x, 330, 64, "black", BG0, kk)


def b_resposta(c, t, C, B):
    ta, tb, tc, td = (C[f"05.{k}"] for k in "abcd")
    a = fade(t, B["start"], B["end"], 0.2, 0.2)
    kd = ep(t, td, 0.4)
    solido(c, CX, FY + 80, 260, t, a * (1 - kd), pintura=dict(ret=1, trap=1, base=1, topo=1))
    solido(c, CX, FY + 80, 260, t, a * kd, ponta=True, F=1.0, pintura=dict(ret=1, trap=1, base=1))   # a pirâmide inteira
    k = pop(t, ta, 0.4)
    c.save(); c.translate(CX, 360); c.scale(k, k); c.translate(-CX, -360)
    glow_text(c, "4" + (" COLORS" if EN else " CORES"), CX, 400, 170, "black", MNT, a * (1 - ep(t, tb, 0.25)), glow=0.3)
    c.restore()
    big(c, L["letra"], 340, a * ep(t, tb, 0.3) * (1 - ep(t, tc, 0.25)), WHITE, 120, hl="D", hl_col=MNT)
    big(c, L["tipos"], 360, a * ep(t, tc, 0.3) * (1 - kd), CYA, 96)
    big(c, L["piramide"], 300, a * kd, AMB, 96)
    big(c, L["tres_c"], 430, a * ep(t, td + 2.6, 0.3), WHITE, 110, hl=L["tres_c"], hl_col=MNT)


def b_final(c, t, C, B):
    ta, tb = C["06.a"], C["06.b"]
    a = ep(t, B["start"], 0.2)
    ka = a * (1 - ep(t, tb, 0.25))
    if ka > 0:
        big(c, L["acertou"], 380, ka, WHITE, 104, hl=L["acertou"].split()[-1], hl_col=AMB)
        opcoes(c, 560, ka, t, ta - 1.0, certo="D")
        label(c, L["conta"], CX, 1200, ka * ep(t, ta + 0.8, 0.3), 50, AMB, "extrabold")
    kb = a * ep(t, tb, 0.3)
    if kb > 0:
        cartao(c, 120, 330, 840, 760, kb, CYA, L["aula"])
        solido(c, CX, 650, 120, t, kb, pintura=dict(ret=1, trap=1, base=1, topo=1))
        text_mid(c, L["passo"], CX, 860, 46, "extrabold", WHITE, kb)
        glow_text(c, L["canal"], CX, 1000, 96, "black", WHITE, kb * ep(t, tb + 1.0, 0.3), glow=0.14)
        w = text_w(L["canal"], "black", 96)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(CX - w / 2, 1026, w * ep(t, tb + 1.3, 0.6), 12), 6, 6), paint(AMB, kb))


BLOCKS = dict(gancho=b_gancho, opcoes=b_opcoes, pegadinha=b_pegadinha, faces=b_faces, resposta=b_resposta, final=b_final)
