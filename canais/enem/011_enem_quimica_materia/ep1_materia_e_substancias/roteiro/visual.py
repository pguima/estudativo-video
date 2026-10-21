"""Visual — Matéria, Substâncias e Misturas, Episódio 1: matéria e substância simples × composta (iniciantes, tema claro).
Cores com função: azul = definição · roxo = regra · âmbar = armadilha · verde = atalho/dica · vermelho = erro.
Peças próprias deste episódio:
- peca()/mol(): átomos como bolinhas coloridas (cada elemento uma cor fixa); as montagens se encaixam peça por peça.
- formula(): a fórmula com índices; os símbolos "acendem" um a um (fundo na cor do elemento) na hora de contar.
- ritual(): o cartão de 3 passos (olhe a fórmula → conte as letras → 1 simples / 2+ composta), sempre igual.
"""
import json
import math
import re
import unicodedata
from functools import lru_cache
from pathlib import Path
import skia
import motor
motor.set_theme("claro")
from motor import *  # noqa
from aula import *  # noqa

MARCA = ""
ARQUIVO_FINAL = "enem_quimica_materia_ep1_materia_e_substancias.mp4"
CARD_R = (140, 150, 1640, 690)
SYM = "C:/Windows/Fonts/seguisym.ttf"

# cor de cada elemento (fixa na série) e cor do texto quando o símbolo acende
EL = {"O": "#E5484D", "H": "#F4F4F2", "N": "#3B6CF6", "C": "#3A3A3C", "S": "#F2C230", "Fe": "#C2662D",
      "Na": "#8E5CF0", "Cl": "#2FB36B", "P": "#F28C28", "He": "#EC6FB0"}
ELTXT = {"H": "#8E8E93", "S": "#B88A00"}
NOME = {"O": "oxigênio", "H": "hidrogênio", "N": "nitrogênio", "C": "carbono", "S": "enxofre", "Fe": "ferro",
        "Na": "sódio", "Cl": "cloro", "P": "fósforo", "He": "hélio"}
WATER = "#7FB2F0"


def eltxt(e):
    return ELTXT.get(e, EL[e])


# ======================================================================
# tempos das palavras
# ======================================================================

def _n(s):
    s = unicodedata.normalize("NFD", s.lower())
    return re.sub(r"[^a-z0-9]", "", "".join(ch for ch in s if unicodedata.category(ch) != "Mn"))


@lru_cache(None)
def _words():
    p = Path(__file__).resolve().parents[1] / "audio" / "tempos.json"
    if not p.exists():
        return {}
    d = json.loads(p.read_text(encoding="utf-8"))
    return {s["id"]: [(_n(w["disp"]), w["t0"]) for w in s.get("tokens", [])] for s in d["scenes"]}


def WT(C, sid, palavra, k=1, depois=None):
    """instante (absoluto) da k-ésima ocorrência da palavra na cena (k=-1: última); depois = só após esse instante"""
    ws = [(w, C[sid] + t0) for w, t0 in _words().get(sid, []) if w == _n(palavra)]
    if depois is not None:
        ws = [x for x in ws if x[1] >= depois - 0.05]
    if not ws:
        return (depois if depois is not None else C[sid]) + 1.2
    return ws[k - 1 if k > 0 else k][1]


# ======================================================================
# átomos e montagens
# ======================================================================

def peca(c, x, y, r, e, a=1.0, label=True, glow=0.0):
    """um átomo: bolinha na cor do elemento, com brilho e o símbolo dentro"""
    if a <= 0:
        return
    col = EL[e]
    if glow > 0:
        c.drawCircle(x, y, r * 1.35, paint(AMBER, a * glow * 0.35))
    sh = skia.Paint(AntiAlias=True, Color=skia.Color4f(0, 0, 0, 0.16 * a))
    sh.setMaskFilter(skia.MaskFilter.MakeBlur(skia.kNormal_BlurStyle, r * 0.18))
    c.drawCircle(x + r * 0.06, y + r * 0.14, r, sh)
    c.drawCircle(x, y, r, paint(col, a))
    g = skia.GradientShader.MakeRadial(skia.Point(x - r * 0.35, y - r * 0.4), r * 1.1,
                                       [skia.Color4f(1, 1, 1, 0.55 * a), skia.Color4f(1, 1, 1, 0)])
    p = skia.Paint(AntiAlias=True); p.setShader(g)
    c.drawCircle(x, y, r, p)
    c.drawCircle(x, y, r, paint(mix(col, "#000000", 0.25) if e != "H" else "#B8B8BC", a, stroke=max(1.5, r * 0.06)))
    if label and r >= 16:
        text_mid(c, e, x, y, r * (0.78 if len(e) == 1 else 0.62), "black", on(col) if e != "H" else "#6E6E73", a)


def _ring(n, R, start=-90):
    return [(R * math.cos(math.radians(start + 360 * k / n)), R * math.sin(math.radians(start + 360 * k / n))) for k in range(n)]


def _glicose():
    out = []
    ring = _ring(6, 2.3, -90)
    for k, (x, y) in enumerate(ring):
        out.append(("O" if k == 0 else "C", x, y, 1.0))
    # carbono extra preso ao anel
    ex, ey = ring[1][0] * 1.9, ring[1][1] * 1.9
    out.append(("C", ex, ey, 1.0))
    out.append(("O", ex + 1.7, ey - 0.9, 1.0))
    out.append(("H", ex + 2.9, ey - 1.6, 0.62))
    out.append(("H", ex - 0.2, ey - 1.65, 0.62))
    out.append(("H", ex + 0.9, ey + 1.3, 0.62))
    for k in (2, 3, 4, 5):
        x, y = ring[k]
        L = math.hypot(x, y)
        ux, uy = x / L, y / L
        ox, oy = x + ux * 1.75, y + uy * 1.75
        out.append(("O", ox, oy, 1.0))
        out.append(("H", ox + ux * 1.25 - uy * 0.5, oy + uy * 1.25 + ux * 0.5, 0.62))
        out.append(("H", x - uy * 1.35 + ux * 0.2, y + ux * 1.35 + uy * 0.2, 0.62))
    out.append(("H", ring[1][0] - 0.2, ring[1][1] + 1.45, 0.62))
    return out


def _grade(cols, rows, a_el, b_el=None, rb=0.72):
    out = []
    for j in range(rows):
        for i in range(cols):
            x, y = (i - (cols - 1) / 2) * 2.0, (j - (rows - 1) / 2) * 2.0
            if b_el and (i + j) % 2:
                out.append((b_el, x, y, rb))
            else:
                out.append((a_el, x, y, 1.0))
    return out


MOLS = {
    "O2": [("O", -0.92, 0, 1), ("O", 0.92, 0, 1)],
    "N2": [("N", -0.92, 0, 1), ("N", 0.92, 0, 1)],
    "H2": [("H", -0.62, 0, 0.7), ("H", 0.62, 0, 0.7)],
    "O3": [("O", -1.55, 0.7, 1), ("O", 0, -0.35, 1), ("O", 1.55, 0.7, 1)],
    "H2O": [("O", 0, -0.25, 1), ("H", -1.25, 0.75, 0.66), ("H", 1.25, 0.75, 0.66)],
    "CO2": [("O", -1.85, 0, 1), ("C", 0, 0, 1), ("O", 1.85, 0, 1)],
    "CH4": [("C", 0, 0, 1), ("H", 0, -1.5, 0.64), ("H", 1.5, 0, 0.64), ("H", 0, 1.5, 0.64), ("H", -1.5, 0, 0.64)],
    "S8": [("S", x, y, 0.78) for x, y in _ring(8, 2.15, -90)],
    "He": [("He", 0, 0, 1)],
    "Fe": _grade(4, 3, "Fe"),
    "NaCl": _grade(4, 3, "Cl", "Na", 0.72),
    "C6H12O6": _glicose(),
    "O": [("O", 0, 0, 1)],
    "H": [("H", 0, 0, 0.8)],
}
BONDS = {"O2", "N2", "H2", "O3", "H2O", "CO2", "CH4", "S8", "C6H12O6"}


def mol(c, nome, cx, cy, r, a=1.0, build=1.0, label=True, glow=None, drop=70):
    """desenha a montagem; build 0..1 encaixa as peças uma a uma (caem de cima e assentam)"""
    if a <= 0:
        return
    pcs = MOLS[nome]
    n = len(pcs)
    pos = [(cx + x * r, cy + y * r, s * r, e) for e, x, y, s in pcs]
    if nome in BONDS and build > 0:
        ab = a * clamp(build * 1.2 - 0.2)
        for i in range(n):
            for j in range(i + 1, n):
                (x0, y0, r0, _), (x1, y1, r1, _) = pos[i], pos[j]
                if math.hypot(x1 - x0, y1 - y0) < (r0 + r1) * 1.05 + r * 0.55:
                    line(c, x0, y0, x1, y1, "#B8B8BC", ab, r * 0.28)
    for i, (x, y, rr, e) in enumerate(pos):
        f = clamp(build * n - i) if build < 1 else 1.0
        if f <= 0:
            continue
        k = ease_back(f)
        g = glow(e) if glow else 0.0
        peca(c, x, y - (1 - k) * drop, rr, e, a * clamp(f * 2), label, g)


def brick(c, x, y, w, h, col, a=1.0):
    """peça de LEGO vista de lado"""
    if a <= 0:
        return
    stud_w, stud_h = w * 0.24, h * 0.22
    for k in (0.27, 0.73):
        rrect(c, x + w * k - stud_w / 2, y - stud_h, stud_w, stud_h + 6, 5, mix(col, "#000000", 0.08), a)
    rrect(c, x, y, w, h, 10, col, a, shadow=True)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 10, 10),
                paint(mix(col, "#000000", 0.22) if col != EL["H"] else "#B8B8BC", a, stroke=3))


# ======================================================================
# fórmula com símbolos que acendem
# ======================================================================

def parse(f):
    return [(m.group(1), int(m.group(2)) if m.group(2) else 1) for m in re.finditer(r"([A-Z][a-z]?)(\d*)", f)]


def _flayout(f, size, g=0.04):
    items, x = [], 0.0
    for e, n in parse(f):
        w = text_w(e, "black", size)
        sub = str(n) if n > 1 else ""
        ws = text_w(sub, "black", size * 0.56) if sub else 0
        items.append((e, sub, x, w, ws))
        x += w + ws + (size * g)
    return items, x


def formula_w(f, size):
    return _flayout(f, size)[1]


def formula(c, f, cx, cy, size, a=1.0, lit=0.0, nums=1.0, upper=False):
    """lit: quantos símbolos já acenderam (fração = acendendo) · nums < 1 apaga os índices · upper: destaca só a maiúscula"""
    if a <= 0:
        return
    items, tw = _flayout(f, size, 0.04 + 0.13 * ease_io(clamp(lit)))
    x0 = cx - tw / 2
    base = cy + size * 0.36
    for k, (e, sub, x, w, ws) in enumerate(items):
        l = clamp(lit - k)
        if l > 0:
            ww = text_w(e[0], "black", size) if upper else w
            s_ = 1 + 0.12 * math.sin(math.pi * l)
            pad = size * 0.05
            c.save(); c.translate(x0 + x + ww / 2, cy); c.scale(s_, s_)
            rrect(c, -ww / 2 - pad, -size * 0.62, ww + pad * 2, size * 1.24, size * 0.18, EL[e], a * l * 0.28)
            c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(-ww / 2 - pad, -size * 0.62, ww + pad * 2, size * 1.24),
                                              size * 0.18, size * 0.18), paint(eltxt(e), a * l, stroke=max(2, size * 0.04)))
            c.restore()
        col = mix(INK, eltxt(e), l)
        text(c, e, x0 + x, base, size, "black", col, a, align="left")
        if sub:
            text(c, sub, x0 + x + w, base + size * 0.2, size * 0.56, "black", mix(LIGHT, INK2, nums), a, align="left")
            if nums < 1:
                strike(c, x0 + x + w - 4, base + size * 0.02, x0 + x + w + ws + 4, base - size * 0.3, a * (1 - nums) * 0.9, RED)
    return tw


def n_el(f):
    return len({e for e, _ in parse(f)})


def veredito(c, f, cx, cy, a, size=30):
    k = n_el(f)
    s = "SIMPLES" if k == 1 else "COMPOSTA"
    pill(c, f"{k} {'letra' if k == 1 else 'letras'} → {s}", cx, cy, PURPLE, size=size, a=a, anchor="center", bounds=(0, 1920))


def fchip(c, f, cx, cy, size, a, lit=0.0, verdict=0.0, w=None, h=None, upper=True):
    """cartão pequeno com fórmula; verdict acende a classificação"""
    if a <= 0:
        return
    w = w or max(formula_w(f, size) + 80, 200)
    h = h or size * 2.2
    card(c, cx - w / 2, cy - h / 2, w, h, a, r=20)
    formula(c, f, cx, cy - (size * 0.25 if verdict > 0 else 0), size, a, lit, upper=upper)
    if verdict > 0:
        k = n_el(f)
        text(c, "SIMPLES" if k == 1 else "COMPOSTA", cx, cy + h / 2 - 18, size * 0.42, "black", PURPLE, a * verdict)


# ======================================================================
# ritual de classificação
# ======================================================================

RITUAL = [("olhe a fórmula", ""), ("conte as LETRAS", "maiúsculas · não os números"), ("1 letra: SIMPLES", "2 ou mais: COMPOSTA")]


def ritual(c, x, y, w, a, cues=None, t=0.0, ativo=None, dy=110, titulo=True):
    if a <= 0:
        return
    h = dy * 3 + (90 if titulo else 30)
    card(c, x, y, w, h, a)
    y0 = y + 30
    if titulo:
        text(c, "RITUAL", x + 36, y + 58, 26, "black", PURPLE, a, align="left")
        y0 = y + 86
    for k, (s1, s2) in enumerate(RITUAL):
        ak = a * (ep(t, cues[k], 0.45) if cues else 1.0)
        if ak <= 0:
            continue
        yy = y0 + k * dy
        on_ = ativo == k
        if on_:
            rrect(c, x + 14, yy, w - 28, dy - 12, 16, PURPLE, ak * 0.13)
        badge_num(c, k + 1, x + 58, yy + (dy - 12) / 2, ak, 24, bg=PURPLE)
        sz = 34 if w > 600 else 28
        text(c, s1, x + 100, yy + (dy - 12) / 2 + (2 if s2 else 12) - (sz * 0.1 if s2 else 0), sz, "black", INK, ak, align="left")
        if s2:
            text(c, s2, x + 100, yy + (dy - 12) / 2 + sz * 0.95, sz * 0.66, "bold", INK2, ak, align="left")


def ativo_em(t, marcas):
    at = None
    for tm, i in marcas:
        if t >= tm:
            at = i
    return at


def regra(c, s, cx, cy, a, size=34, col=None, w=None):
    col = PURPLE if col is None else col
    if a <= 0:
        return
    dy = (1 - a) * 14
    ww = (w or text_w(s, "black", size) + 90)
    rrect(c, cx - ww / 2, cy - 44 + dy, ww, 88, 22, col, a * 0.12)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - ww / 2, cy - 44 + dy, ww, 88), 22, 22), paint(col, a, stroke=3))
    text_mid(c, s, cx, cy + dy, size, "black", col, a)


def defbox(c, titulo, corpo, cx, cy, a, w=900, col=None):
    """cartão de definição (azul): título forte + explicação curta"""
    col = BLUE if col is None else col
    if a <= 0:
        return
    w = max(w, text_w(titulo, "black", 40) + 70, text_w(corpo, "bold", 30) + 70 if corpo else 0)
    dy = (1 - a) * 16
    h = 150 if corpo else 96
    rrect(c, cx - w / 2, cy - h / 2 + dy, w, h, 24, col, a * 0.10)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2, cy - h / 2 + dy, w, h), 24, 24), paint(col, a, stroke=3))
    if corpo:
        text(c, titulo, cx, cy - 12 + dy, 40, "black", col, a)
        text(c, corpo, cx, cy + 44 + dy, 30, "bold", INK, a)
    else:
        text_mid(c, titulo, cx, cy + dy, 40, "black", col, a)


def pause_badge(c, x, y, a):
    if a <= 0:
        return
    rrect(c, x, y, 340, 96, 24, AMBER, a, shadow=True)
    c.drawRect(skia.Rect.MakeXYWH(x + 28, y + 22, 14, 52), paint(INK, a))
    c.drawRect(skia.Rect.MakeXYWH(x + 54, y + 22, 14, 52), paint(INK, a))
    text_mid(c, "PAUSE E TENTE", x + 210, y + 48, 30, "black", INK, a)


def erro_tiles(c, t, items, draw_extra=None):
    """[(instante, título, [linhas], cor)] -> 3 cartões: o erro · por que parece certo · a correção"""
    cw, gap = 500, 40
    x0 = W / 2 - (3 * cw + 2 * gap) / 2
    for k, (tc, tt, lines, col) in enumerate(items):
        a, dy = rise(t, tc)
        if a <= 0:
            continue
        x, y = x0 + k * (cw + gap), 190 + dy
        card(c, x, y, cw, 560, a)
        rrect(c, x, y, cw, 70, 28, col, a * 0.15)
        text_mid(c, tt, x + cw / 2, y + 38, 30, "black", col, a)
        if k == 0:
            check_icon(c, x + cw / 2, y + 130, 30, a, RED, "x")
        elif k == 2:
            check_icon(c, x + cw / 2, y + 130, 30, a, GREEN)
        else:
            text_mid(c, "?", x + cw / 2, y + 130, 70, "black", AMBER, a)
        for j, ln in enumerate(lines):
            big = ln.startswith("!")
            text(c, ln.lstrip("!"), x + cw / 2, y + 240 + j * 56, 44 if big else 31, "black",
                 (RED if k == 0 else GREEN if k == 2 else INK) if big else INK, a)
        if draw_extra:
            draw_extra(c, k, x, y, cw, a)


# ======================================================================
# objetos do cotidiano
# ======================================================================

def copo(c, cx, by, w, h, a, nivel=0.7, cheio=True):
    """copo de vidro (trapézio) com água; by = base"""
    if a <= 0:
        return
    tw, bw = w, w * 0.78
    p = skia.Path()
    p.moveTo(cx - tw / 2, by - h); p.lineTo(cx - bw / 2, by); p.lineTo(cx + bw / 2, by); p.lineTo(cx + tw / 2, by - h)
    if cheio:
        hw = h * nivel
        wl = bw + (tw - bw) * nivel
        q = skia.Path()
        q.moveTo(cx - wl / 2, by - hw); q.lineTo(cx - bw / 2, by); q.lineTo(cx + bw / 2, by); q.lineTo(cx + wl / 2, by - hw); q.close()
        c.drawPath(q, paint(WATER, a * 0.75))
        line(c, cx - wl / 2, by - hw, cx + wl / 2, by - hw, "#5B95DE", a, 3)
    c.drawPath(p, paint("#9AA3AD", a, stroke=5, cap_round=True))
    line(c, cx - tw / 2 + 14, by - h + 20, cx - bw / 2 + 12, by - 20, "#FFFFFF", a * 0.8, 5)


def balanca(c, cx, by, a, ang=0.0):
    """balança de cozinha com mostrador; ang em graus (0 = vazio)"""
    if a <= 0:
        return
    rrect(c, cx - 170, by - 150, 340, 150, 26, "#FFFFFF", a, shadow=True, stroke=3, stroke_color=LIGHT)
    rrect(c, cx - 200, by - 172, 400, 24, 12, "#D7DADF", a)
    dx, dy = cx, by - 72
    c.drawCircle(dx, dy, 52, paint("#F4F5F7", a))
    c.drawCircle(dx, dy, 52, paint(INK2, a, stroke=3))
    for k in range(9):
        th = math.radians(-210 + k * 30)
        line(c, dx + 40 * math.cos(th), dy + 40 * math.sin(th), dx + 48 * math.cos(th), dy + 48 * math.sin(th), INK2, a, 2.5)
    th = math.radians(-210 + ang)
    line(c, dx, dy, dx + 38 * math.cos(th), dy + 38 * math.sin(th), RED, a, 5)
    c.drawCircle(dx, dy, 7, paint(INK, a))


def lanterna(c, cx, cy, a, s=1.0):
    if a <= 0:
        return
    beam = skia.Path()
    beam.moveTo(cx + 40 * s, cy - 22 * s); beam.lineTo(cx + 170 * s, cy - 80 * s)
    beam.lineTo(cx + 170 * s, cy + 80 * s); beam.lineTo(cx + 40 * s, cy + 22 * s); beam.close()
    c.drawPath(beam, paint("#FFE066", a * 0.6))
    rrect(c, cx - 110 * s, cy - 20 * s, 120 * s, 40 * s, 10 * s, "#4A4A4E", a)
    rrect(c, cx + 4 * s, cy - 30 * s, 40 * s, 60 * s, 8 * s, "#2C2C2E", a)


def som(c, cx, cy, a, s=1.0):
    if a <= 0:
        return
    p = skia.Path()
    p.moveTo(cx - 70 * s, cy - 24 * s); p.lineTo(cx - 40 * s, cy - 24 * s); p.lineTo(cx, cy - 60 * s)
    p.lineTo(cx, cy + 60 * s); p.lineTo(cx - 40 * s, cy + 24 * s); p.lineTo(cx - 70 * s, cy + 24 * s); p.close()
    c.drawPath(p, paint("#4A4A4E", a))
    for k, R in enumerate((40, 75, 110)):
        r = skia.Rect.MakeXYWH(cx + 10 * s - R * s, cy - R * s, 2 * R * s, 2 * R * s)
        pa = paint(BLUE, a * (1 - k * 0.25), stroke=7 * s, cap_round=True)
        c.drawArc(r, -45, 90, False, pa)


def chama(c, cx, by, a, s=1.0):
    if a <= 0:
        return
    for col, k in (("#F97316", 1.0), ("#FBBF24", 0.62)):
        p = skia.Path()
        h, w = 200 * s * k, 70 * s * k
        p.moveTo(cx, by - h)
        p.cubicTo(cx + w * 0.4, by - h * 0.6, cx + w * 1.3, by - h * 0.45, cx + w, by - h * 0.15)
        p.cubicTo(cx + w * 0.8, by, cx - w * 0.8, by, cx - w, by - h * 0.15)
        p.cubicTo(cx - w * 1.2, by - h * 0.45, cx - w * 0.2, by - h * 0.55, cx, by - h)
        c.drawPath(p, paint(col, a))
    rrect(c, cx - 110 * s, by + 4, 220 * s, 18 * s, 9, "#4A4A4E", a)


def bexiga(c, cx, cy, a, s=1.0, col="#E5484D"):
    if a <= 0:
        return
    c.drawOval(skia.Rect.MakeXYWH(cx - 70 * s, cy - 90 * s, 140 * s, 175 * s), paint(col, a))
    c.drawOval(skia.Rect.MakeXYWH(cx - 42 * s, cy - 66 * s, 34 * s, 50 * s), paint("#FFFFFF", a * 0.4))
    p = skia.Path(); p.moveTo(cx - 10 * s, cy + 94 * s); p.lineTo(cx, cy + 82 * s); p.lineTo(cx + 10 * s, cy + 94 * s); p.close()
    c.drawPath(p, paint(col, a))
    q = skia.Path(); q.moveTo(cx, cy + 94 * s); q.cubicTo(cx + 20 * s, cy + 130 * s, cx - 20 * s, cy + 160 * s, cx + 4 * s, cy + 200 * s)
    c.drawPath(q, paint(INK2, a, stroke=3))


def prego(c, cx, cy, a, s=1.0):
    if a <= 0:
        return
    rrect(c, cx - 50 * s, cy - 110 * s, 100 * s, 18 * s, 6, "#8C8F94", a)
    p = skia.Path()
    p.moveTo(cx - 10 * s, cy - 92 * s); p.lineTo(cx + 10 * s, cy - 92 * s); p.lineTo(cx + 10 * s, cy + 80 * s)
    p.lineTo(cx, cy + 112 * s); p.lineTo(cx - 10 * s, cy + 80 * s); p.close()
    c.drawPath(p, paint("#A4A8AE", a))
    line(c, cx - 4 * s, cy - 88 * s, cx - 4 * s, cy + 74 * s, "#FFFFFF", a * 0.6, 3)


def cilindro(c, cx, by, a, s=1.0):
    """cilindro de oxigênio hospitalar (verde, no Brasil)"""
    if a <= 0:
        return
    w, h = 130 * s, 360 * s
    rrect(c, cx - w / 2, by - h, w, h, w / 2, "#2E9E5B", a, shadow=True)
    rrect(c, cx - w / 2 + 14 * s, by - h + 30 * s, 16 * s, h - 80 * s, 8, "#FFFFFF", a * 0.25)
    rrect(c, cx - 20 * s, by - h - 46 * s, 40 * s, 50 * s, 8, "#8C8F94", a)
    c.drawCircle(cx, by - h - 60 * s, 22 * s, paint("#5A5D62", a))
    rrect(c, cx - w / 2 + 10 * s, by - h * 0.55, w - 20 * s, 70 * s, 10, "#FFFFFF", a)
    text_mid(c, "O₂", cx, by - h * 0.55 + 35 * s, 40 * s, "black", "#2E9E5B", a)


def digital(c, cx, cy, a, s=1.0, col=None):
    col = PURPLE if col is None else col
    if a <= 0:
        return
    for k in range(7):
        rx, ry = (18 + k * 14) * s, (26 + k * 17) * s
        r = skia.Rect.MakeXYWH(cx - rx, cy - ry + k * 3 * s, 2 * rx, 2 * ry)
        c.drawArc(r, 200 - k * 4, 300 - k * 10, False, paint(col, a, stroke=5 * s, cap_round=True))


def rosto(c, cx, cy, a, s=1.0, col="#F2C9A0"):
    if a <= 0:
        return
    c.drawCircle(cx, cy, 70 * s, paint(col, a))
    c.drawCircle(cx, cy, 70 * s, paint(mix(col, "#000000", 0.25), a, stroke=3))
    c.drawCircle(cx - 24 * s, cy - 14 * s, 7 * s, paint(INK, a))
    c.drawCircle(cx + 24 * s, cy - 14 * s, 7 * s, paint(INK, a))
    p = skia.Path(); p.moveTo(cx, cy - 6 * s); p.lineTo(cx - 14 * s, cy + 24 * s); p.lineTo(cx + 4 * s, cy + 24 * s)
    c.drawPath(p, paint(mix(col, "#000000", 0.4), a, stroke=4, cap_round=True))
    c.drawArc(skia.Rect.MakeXYWH(cx - 26 * s, cy + 10 * s, 52 * s, 40 * s), 20, 140, False, paint(INK, a, stroke=4, cap_round=True))


def termometro(c, x, y, a, h=300, nivel=0.7, col=RED):
    if a <= 0:
        return
    rrect(c, x - 18, y, 36, h, 18, "#FFFFFF", a, shadow=True, stroke=3, stroke_color=LIGHT)
    c.drawCircle(x, y + h + 14, 32, paint("#FFFFFF", a))
    c.drawCircle(x, y + h + 14, 32, paint(LIGHT, a, stroke=3))
    c.drawCircle(x, y + h + 14, 23, paint(col, a))
    top = y + h - (h - 20) * nivel
    rrect(c, x - 8, top, 16, y + h + 6 - top, 8, col, a)


def bequer(c, x, y, w, h, a, liquido=WATER, nivel=0.78):
    if a <= 0:
        return
    hl = h * nivel
    rrect(c, x + 6, y + h - hl, w - 12, hl - 6, 14, liquido, a * 0.35)
    p = skia.Path()
    p.moveTo(x - 10, y); p.lineTo(x, y + 10); p.lineTo(x, y + h - 16); p.quadTo(x, y + h, x + 16, y + h)
    p.lineTo(x + w - 16, y + h); p.quadTo(x + w, y + h, x + w, y + h - 16); p.lineTo(x + w, y + 10); p.lineTo(x + w + 10, y)
    c.drawPath(p, paint("#9AA3AD", a, stroke=5, cap_round=True))


def lapis(c, cx, cy, a, s=1.0):
    if a <= 0:
        return
    c.save(); c.translate(cx, cy); c.rotate(-30); c.scale(s, s)
    rrect(c, -150, -24, 240, 48, 6, "#F2C230", a)
    rrect(c, -190, -24, 44, 48, 6, "#F49AB0", a)
    rrect(c, -152, -24, 14, 48, 2, "#B8B8BC", a)
    p = skia.Path(); p.moveTo(90, -24); p.lineTo(160, 0); p.lineTo(90, 24); p.close()
    c.drawPath(p, paint("#E9C9A0", a))
    p = skia.Path(); p.moveTo(136, -8); p.lineTo(160, 0); p.lineTo(136, 8); p.close()
    c.drawPath(p, paint("#3A3A3C", a))
    c.restore()


def diamante(c, cx, cy, a, s=1.0):
    if a <= 0:
        return
    pts_top = [(-110, -30), (-60, -80), (60, -80), (110, -30)]
    p = skia.Path(); p.moveTo(cx - 110 * s, cy - 30 * s)
    for x, y in pts_top[1:]:
        p.lineTo(cx + x * s, cy + y * s)
    p.lineTo(cx, cy + 110 * s); p.close()
    c.drawPath(p, paint("#BFE3F7", a))
    for (x0, y0), (x1, y1) in [((-110, -30), (110, -30)), ((-60, -80), (-30, -30)), ((60, -80), (30, -30)),
                               ((-30, -30), (0, 110)), ((30, -30), (0, 110)), ((-110, -30), (0, 110)), ((110, -30), (0, 110))]:
        line(c, cx + x0 * s, cy + y0 * s, cx + x1 * s, cy + y1 * s, "#5BA6D6", a, 3)
    c.drawPath(p, paint("#5BA6D6", a, stroke=4))


# ======================================================================
# gancho, promessa, pré-requisitos
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "QUÍMICA ENEM", "MATÉRIA E SUBSTÂNCIAS · EPISÓDIO 1", BLUE)
    items = [("01.a", "O2", "O₂", "gás oxigênio", "2 átomos", 46), ("01.b", "S8", "S₈", "enxofre", "8 átomos", 36),
             ("01.c", "H2O", "H₂O", "água", "3 átomos", 50)]
    for k, (cue, m, f, nome, n, r) in enumerate(items):
        a, dy = rise(t, C[cue])
        if a <= 0:
            continue
        x = 250 + k * 500
        card(c, x, 190 + dy, 440, 520, a)
        text(c, nome.upper(), x + 220, 250 + dy, 30, "black", INK2, a)
        mol(c, m, x + 220, 420 + dy, r, a, ease_io(prog(t, C[cue], 1.2)))
        text(c, f, x + 220, 600 + dy, 64, "black", INK, a)
        text(c, n, x + 220, 668 + dy, 32, "black", BLUE, ep(t, C[cue] + 0.8, 0.4) * a)
    ad = ep(t, C["01.d"], 0.5)
    pill(c, "COMPOSTA", 1470, 754, PURPLE, size=30, a=ad, anchor="center", bounds=(0, 1920))
    for x in (470, 970):
        text_mid(c, "?", x, 754, 50, "black", AMBER, ad)
    ae = ep(t, C["01.e"], 0.5)
    if ae > 0:
        s_ = 0.8 + 0.2 * ease_back(ae)
        c.save(); c.translate(W / 2, 830); c.scale(s_, s_)
        rrect(c, -190, -46, 380, 92, 24, AMBER, ae, shadow=True)
        text_mid(c, "POR QUÊ?", 0, 0, 50, "black", INK, ae)
        c.restore()
    pill(c, "átomo? já explico", 1530, 836, BLUE, size=26, a=ep(t, C["01.f"], 0.5), anchor="center", bounds=(0, 1920))


def b_promessa(c, t, C, B):
    head(c, t, B["start"], "AO FINAL DESTA AULA", "VOCÊ VAI CONSEGUIR", GREEN)
    xs = [430, 960, 1490]
    for k, (cue, titulo) in enumerate((("02.a", "QUALQUER\nFÓRMULA"), ("02.b", "EM 2\nSEGUNDOS"), ("02.c", "SEM\nDECORAR"))):
        a, dy = rise(t, C[cue])
        if a <= 0:
            continue
        x = xs[k]
        card(c, x - 230, 200 + dy, 460, 520, a)
        for j, ln in enumerate(titulo.split("\n")):
            text(c, ln, x, 600 + dy + j * 54, 46, "black", INK, a)
        if k == 0:
            for j, f in enumerate(("CO₂", "Fe", "C₆H₁₂O₆")):
                text_mid(c, f, x, 300 + j * 80 + dy, 50, "black", INK2, a * ep(t, C[cue] + 0.3 * j, 0.4))
        elif k == 1:   # cronômetro
            cy = 400 + dy
            c.drawCircle(x, cy, 110, paint("#FFFFFF", a))
            c.drawCircle(x, cy, 110, paint(GREEN, a, stroke=10))
            rrect(c, x - 20, cy - 150, 40, 30, 8, GREEN, a)
            p = prog(t, C[cue] + 0.3, 2.0)
            c.drawArc(skia.Rect.MakeXYWH(x - 90, cy - 90, 180, 180), -90, 360 * p, True, paint(GREEN, a * 0.25))
            th = math.radians(-90 + 360 * p)
            line(c, x, cy, x + 80 * math.cos(th), cy + 80 * math.sin(th), INK, a, 6)
            text_mid(c, "2 s", x, cy + 50, 34, "black", INK, a)
        else:
            for j, s in enumerate(("lista", "tabela", "decoreba")):
                yy = 300 + j * 80 + dy
                text_mid(c, s, x, yy, 40, "bold", INK2, a)
                strike(c, x - 100, yy, x + 100, yy, a, RED, ease_io(prog(t, C[cue] + 0.4 + 0.25 * j, 0.4)))


def b_prereq(c, t, C, B):
    if t < C["04"] - 0.2:
        head(c, t, B["start"], "LEMBRETE 1", "ÁTOMO", BLUE)
        card(c, *CARD_R)
        aa = ep(t, C["03.a"], 0.5)
        for k in range(18):   # um monte de pecinhas
            x, y = 330 + (k % 6) * 70 + (35 if (k // 6) % 2 else 0), 330 + (k // 6) * 64
            peca(c, x, y, 28, ["O", "H", "C", "N", "Fe", "S"][k % 6], aa * ep(t, C["03.a"] + 0.05 * k, 0.3), label=False)
        defbox(c, "ÁTOMO", "pecinha pequena demais para ver", 560, 650, ep(t, C["03.a"] + 1.4, 0.5), w=680)
        ab = ep(t, C["03.b"], 0.5)
        text_mid(c, "=", 1050, 420, 90, "black", INK2, ab)
        for k, col in enumerate((EL["O"], EL["N"], EL["S"])):
            brick(c, 1170 + k * 140, 400 - k * 0 + (1 - ab) * 30, 120, 80, col, ab * ep(t, C["03.b"] + 0.2 * k, 0.4))
        text(c, "peças de LEGO", 1380, 600, 40, "black", INK, ab)
        return
    if t < C["05"] - 0.2:
        head(c, t, C["04"], "LEMBRETE 2", "ELEMENTO QUÍMICO", BLUE)
        card(c, *CARD_R)
        for k, e in enumerate(("O", "H", "Fe")):
            a = ep(t, C["04.a"] + 0.6 * k, 0.4)
            x = 420 + k * 280
            peca(c, x, 330, 70, e, a, label=ep(t, C["04.c"], 0.3) > 0.5)
            text(c, NOME[e], x, 450, 34, "black", eltxt(e), a)
            brick(c, x - 70, 540 + (1 - ep(t, C["04.b"] + 0.2 * k, 0.4)) * 20, 140, 90, EL[e], ep(t, C["04.b"] + 0.2 * k, 0.4))
        defbox(c, "ELEMENTO = TIPO de átomo", "", 1400, 300, ep(t, C["04.a"], 0.5), w=560)
        regra(c, "elemento = COR da peça", 1400, 460, ep(t, C["04.b"], 0.5), 34, BLUE, w=560)
        ac = ep(t, C["04.c"], 0.5)
        if ac > 0:
            card(c, 1150, 560, 500, 170, ac)
            text(c, "SÍMBOLO", 1400, 610, 26, "black", BLUE, ac)
            text_mid(c, "O  →  oxigênio", 1400, 660, 32, "black", INK, ac)
            text_mid(c, "H  →  hidrogênio", 1400, 706, 32, "black", INK, ep(t, C["04.c"] + 1.0, 0.4))
        return
    head(c, t, C["05"], "LEMBRETE 3", "FÓRMULA QUÍMICA", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["05.t"], 0.5)
    defbox(c, "FÓRMULA = etiqueta das peças", "", 960, 220, a0, w=760)
    aa = ep(t, C["05.a"], 0.5)
    formula(c, "H2O", 560, 440, 170, aa)
    mol(c, "H2O", 1300, 420, 70, aa, ease_io(prog(t, C["05.a"] + 0.4, 1.0)))
    text(c, "água", 1300, 560, 34, "black", INK2, aa)
    ab = ep(t, C["05.b"], 0.5)
    if ab > 0:
        arrow(c, 560, 620, 560, 520, BLUE, ab, 4, 16)
        text(c, "ÍNDICE: conta as peças", 560, 660, 32, "black", BLUE, ab)
        text(c, "2 hidrogênios", 560, 704, 28, "bold", INK2, ep(t, C["05.b"] + 1.4, 0.4))
    ac = ep(t, C["05.c"], 0.5)
    if ac > 0:
        arrow(c, 760, 610, 700, 525, BLUE, ac, 4, 16)
        text(c, "sem número = 1", 770, 650, 30, "black", BLUE, ac, align="left")
    ad = ep(t, C["05.d"], 0.5)
    pill(c, "LETRAS → cores (elementos)", 1080, 650, BLUE, size=28, a=ad, bounds=(0, 1920))
    pill(c, "NÚMEROS → quantas peças", 1080, 730, INK2, size=28, a=ep(t, C["05.d"] + 1.2, 0.5), bounds=(0, 1920))


# ======================================================================
# bloco a: matéria
# ======================================================================

def b_materia(c, t, C, B):
    head(c, t, B["start"], "O QUE É", "MATÉRIA?", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["06.a"], 0.5)
    ab = ep(t, C["06.b"], 0.5)
    down = ease_io(prog(t, C["06.b"], 0.8))
    balanca(c, 560, 760, ab, ang=60 * ease_out(prog(t, C["06.b"] + 0.7, 0.8)) if ab > 0 else 0)
    cy_copo = lerp(520, 592, down) if ab > 0 else 520
    copo(c, 560, cy_copo, 200, 240, aa)
    if ab > 0:
        defbox(c, "MASSA", "o que a balança mede", 1300, 280, ep(t, C["06.b"] + 1.2, 0.5), w=620)
    ac = ep(t, C["06.c"], 0.5)
    if ac > 0:
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(440, cy_copo - 260, 240, 270), 18, 18),
                    paint(BLUE, ac, stroke=4))
        line(c, 440, cy_copo - 260, 680, cy_copo + 10, BLUE, ac * 0, 1)
        text(c, "ocupa espaço", 560, cy_copo - 280, 30, "black", BLUE, ac)
        text(c, "onde a água está, não cabe outra coisa", 1300, 460, 28, "bold", INK2, ac)
    defbox(c, "MATÉRIA", "tem MASSA e ocupa ESPAÇO", 1300, 640, ep(t, C["06.d"], 0.5), w=620)


def b_materia_nao(c, t, C, B):
    head(c, t, B["start"], "E O QUE", "NÃO É MATÉRIA?", BLUE)
    items = [("07.a", "LUZ", lanterna), ("07.b", "SOM", som), ("07.c", "CALOR", chama)]
    ad = ep(t, C["07.d"], 0.5)
    for k, (cue, s, fn) in enumerate(items):
        a, dy = rise(t, C[cue])
        if a <= 0:
            continue
        x = 180 + k * 400
        card(c, x, 190 + dy, 360, 460, a)
        if fn is chama:
            fn(c, x + 180, 450 + dy, a, 0.9)
        else:
            fn(c, x + 170, 380 + dy, a, 0.95)
        text(c, s, x + 180, 560 + dy, 44, "black", INK, a)
        text(c, "sem massa", x + 180, 615 + dy, 28, "black", INK2, ad * a)
        if ad > 0:
            check_icon(c, x + 310, 240 + dy, 26, ad * a, GRAY, "x")
    pill(c, "NÃO são matéria", 680, 720, INK2, size=32, a=ad, anchor="center", bounds=(0, 1920))
    ae, dy = rise(t, C["07.e"])
    if ae > 0:
        card(c, 1400, 190 + dy, 360, 460, ae)
        bexiga(c, 1580, 350 + dy, ae, 1.0, BLUE)
        for k in range(10):
            th = k * 2.4
            c.drawCircle(1580 + 40 * math.cos(th) * (k % 3) / 2, 340 + dy + 50 * math.sin(th) * (k % 4) / 3, 7,
                         paint("#FFFFFF", ae * 0.8))
        text(c, "AR", 1580, 600 + dy, 44, "black", INK, ae)
        check_icon(c, 1710, 240 + dy, 26, ae, BLUE)
        pill(c, "invisível, mas É matéria", 1580, 720, BLUE, size=28, a=ae, anchor="center", bounds=(0, 1920))


# ======================================================================
# bloco b: propriedades
# ======================================================================

def b_prop_gerais(c, t, C, B):
    head(c, t, B["start"], "PROPRIEDADES", "GERAIS", BLUE)
    card(c, *CARD_R)
    defbox(c, "PROPRIEDADE = característica da matéria", "", W / 2, 230, ep(t, C["08.a"], 0.5), w=980)
    ab = ep(t, C["08.b"], 0.5)
    pill(c, "massa", 620, 330, BLUE, size=30, a=ab, anchor="center", bounds=(0, 1920))
    pill(c, "volume = espaço ocupado", 1150, 330, BLUE, size=30, a=ep(t, C["08.b"] + 1.0, 0.5), anchor="center", bounds=(0, 1920))
    objs = [(prego, "prego"), (copo, "água"), (bexiga, "ar")]
    for k, (fn, s) in enumerate(objs):
        a = ep(t, C["08.c"] + 0.8 * k, 0.4)
        x = 520 + k * 440
        if fn is copo:
            fn(c, x, 620, 140, 170, a)
        elif fn is bexiga:
            fn(c, x, 500, a, 0.7, BLUE)
        else:
            fn(c, x, 520, a, 0.9)
        pill(c, "tem massa ✓", x, 680, INK2, size=24, a=a, anchor="center", bounds=(0, 1920))
    ad = ep(t, C["08.d"], 0.5)
    text(c, "…mas isso não diz O QUE é", W / 2, 760, 34, "black", AMBER, ad * (1 - ep(t, C["08.e"], 0.4)))
    pill(c, "PROPRIEDADES GERAIS: valem para tudo", W / 2, 760, BLUE, size=32, a=ep(t, C["08.e"], 0.5), anchor="center", bounds=(0, 1920))


def b_prop_especificas(c, t, C, B):
    head(c, t, B["start"], "PROPRIEDADES", "ESPECÍFICAS", BLUE)
    card(c, *CARD_R)
    rows = [("09.a", "PONTO DE FUSÃO", "temperatura em que derrete"), ("09.b", "PONTO DE EBULIÇÃO", "temperatura em que ferve"),
            ("09.c", "DENSIDADE", "quanto pesa um mesmo volume")]
    for k, (cue, s1, s2) in enumerate(rows):
        a, dy = rise(t, C[cue])
        y = 250 + k * 150 + dy
        if a <= 0:
            continue
        rrect(c, 200, y - 40, 760, 120, 20, BLUE, a * 0.08)
        text(c, s1, 230, y + 6, 36, "black", BLUE, a, align="left")
        text(c, s2, 230, y + 54, 28, "bold", INK2, a, align="left")
    ad = ep(t, C["09.d"], 0.5)
    for k, (nome, temp, niv, col) in enumerate((("água", "100 °C", 0.85, WATER), ("álcool", "78 °C", 0.62, "#F2C230"))):
        a = ad * ep(t, C["09.d"] + 1.6 * k, 0.5)
        if a <= 0:
            continue
        x = 1110 + k * 290
        bequer(c, x, 380, 180, 220, a, col, 0.6)
        for j in range(5):   # bolhas subindo
            ph = (t * 0.8 + j * 0.21) % 1.0
            c.drawCircle(x + 30 + j * 30, 580 - ph * 120, 8, paint("#FFFFFF", a * (1 - ph)))
        termometro(c, x + 230, 300, a, 260, niv, RED)
        text(c, nome, x + 90, 660, 34, "black", INK, a)
        text(c, temp, x + 90, 712, 40, "black", RED, a)
    pill(c, "ESPECÍFICAS: mudam de material para material", W / 2, 790, BLUE, size=30, a=ep(t, C["09.e"], 0.5), anchor="center", bounds=(0, 1920))


def b_prop_digital(c, t, C, B):
    head(c, t, B["start"], "GERAL × ESPECÍFICA", "NARIZ × IMPRESSÃO DIGITAL", BLUE)
    a0 = ep(t, C["10.t"], 0.5)
    card(c, 160, 180, 760, 560, a0)
    for k, col in enumerate(("#F2C9A0", "#C98E62", "#8D5A3B")):
        rosto(c, 330 + k * 210, 340, a0 * ep(t, C["10.t"] + 0.3 * k, 0.4), 0.9, col)
    text(c, "todo mundo tem nariz", 540, 500, 36, "black", INK, a0)
    aa = ep(t, C["10.a"], 0.5)
    pill(c, "GERAL: não identifica ninguém", 540, 580, INK2, size=28, a=aa, anchor="center", bounds=(0, 1920))
    ab, dy = rise(t, C["10.b"])
    card(c, 1000, 180 + dy, 760, 560, ab)
    digital(c, 1380, 340 + dy, ab, 1.1)
    text(c, "só você tem", 1380, 500 + dy, 36, "black", INK, ab)
    pill(c, "ESPECÍFICA: identifica", 1380, 580 + dy, PURPLE, size=28, a=ab, anchor="center", bounds=(0, 1920))
    ac = ep(t, C["10.c"], 0.5)
    if ac > 0:
        text(c, "massa, volume", 540, 680, 30, "bold", INK2, ac)
        text(c, "fusão, ebulição, densidade", 1380, 680, 30, "bold", PURPLE, ac)
    regra(c, "as específicas IDENTIFICAM o material", W / 2, 810, ep(t, C["10.d"], 0.5), 34, PURPLE, w=1000)


# ======================================================================
# bloco c: molécula e substância pura
# ======================================================================

def b_molecula(c, t, C, B):
    head(c, t, B["start"], "O QUE É UMA", "SUBSTÂNCIA?", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["11.a"], 0.5)
    snap = ease_io(prog(t, C["11.a"] + 0.6, 1.2))
    brick(c, lerp(260, 330, snap), lerp(300, 380, snap), 150, 80, EL["H"], aa)
    brick(c, lerp(560, 480, snap), lerp(300, 380, snap), 150, 80, EL["H"], aa)
    brick(c, 380, lerp(470, 300, snap), 160, 80, EL["O"], aa)
    text(c, "peças encaixadas = montagem", 460, 560, 32, "black", INK, aa)
    defbox(c, "MOLÉCULA = montagem de átomos", "", 460, 680, ep(t, C["11.b"], 0.5), w=700)
    ac = ep(t, C["11.c"], 0.5)
    if ac > 0:
        bequer(c, 1000, 220, 600, 500, ac, WATER, 0.9)
        k = 0
        for j in range(4):
            for i in range(5):
                x = 1080 + i * 110 + (55 if j % 2 else 0) - (20 if j % 2 else 0)
                y = 330 + j * 100
                if x > 1560:
                    continue
                mol(c, "H2O", x, y, 22, ac * ep(t, C["11.c"] + 0.06 * k, 0.3), label=False)
                k += 1
    ad = ep(t, C["11.d"], 0.5)
    pill(c, "todas IGUAIS", 1300, 780, BLUE, size=32, a=ad, anchor="center", bounds=(0, 1920))


def b_pura(c, t, C, B):
    head(c, t, B["start"], "SUBSTÂNCIA PURA", "× MISTURA", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["12.t"], 0.5)
    dimL = 1.0
    dimR = 1 - 0.6 * ep(t, C["12.d"], 0.5)
    for side in (0, 1):
        x = 240 + side * 760
        aa = a0 * (dimL if side == 0 else dimR)
        if side == 1:
            aa *= ep(t, C["12.a"] - 0.5, 0.5)
        if aa <= 0:
            continue
        bequer(c, x, 230, 520, 380, aa, WATER, 0.88)
        for j in range(3):
            for i in range(4):
                xx, yy = x + 80 + i * 120 + (40 if j % 2 else 0), 320 + j * 100
                if side == 1 and (i + j) % 3 == 1:
                    peca(c, xx - 16, yy, 18, "Na", aa, label=False)
                    peca(c, xx + 18, yy, 22, "Cl", aa, label=False)
                else:
                    mol(c, "H2O", xx, yy, 20, aa, label=False)
        text(c, "água pura" if side == 0 else "água com sal", x + 260, 670, 34, "black", INK, aa)
    defbox(c, "SUBSTÂNCIA PURA", "1 único tipo de montagem", 500, 770, ep(t, C["12.b"], 0.5), w=640)
    defbox(c, "MISTURA", "2 ou mais tipos", 1260, 770, ep(t, C["12.c"], 0.5) * dimR, w=560)
    pill(c, "hoje: só as puras", 500, 180, GREEN, size=26, a=ep(t, C["12.d"], 0.5), anchor="center", bounds=(0, 1920))


# ======================================================================
# blocos d-e: simples e composta
# ======================================================================

def b_simples(c, t, C, B):
    head(c, t, B["start"], "SUBSTÂNCIA", "SIMPLES", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["13.a"], 0.5)
    cilindro(c, 360, 720, aa, 1.2)
    ab = ep(t, C["13.b"], 0.5)
    formula(c, "O2", 900, 330, 150, ab, lit=ep(t, C["13.c"], 0.5))
    mol(c, "O2", 1380, 330, 90, ab, ease_io(prog(t, C["13.b"] + 0.3, 1.0)))
    ac = ep(t, C["13.c"], 0.5)
    text(c, "2 peças · 1 cor", 1380, 480, 38, "black", eltxt("O"), ac)
    defbox(c, "SUBSTÂNCIA SIMPLES", "1 elemento só (1 cor), não importa quantas peças", 1140, 660, ep(t, C["13.d"], 0.5), w=980)


SIMP_EX = [("14.a", "O3", "O₃", "ozônio", 34), ("14.b", "N2", "N₂", "nitrogênio", 38), ("14.c", "S8", "S₈", "enxofre", 26),
           ("14.d", "He", "He", "hélio", 44), ("14.e", "Fe", "Fe", "ferro", 22)]


def b_simples_ex(c, t, C, B):
    head(c, t, B["start"], "SUBSTÂNCIAS SIMPLES", "1 ELEMENTO SÓ", BLUE)
    af = ep(t, C["14.f"], 0.5)
    for k, (cue, m, f, nome, r) in enumerate(SIMP_EX):
        a, dy = rise(t, C[cue])
        if a <= 0:
            continue
        x = 160 + k * 324
        card(c, x, 190 + dy, 300, 560, a)
        text(c, nome.upper(), x + 150, 245 + dy, 26, "black", INK2, a)
        mol(c, m, x + 150, 400 + dy, r, a, ease_io(prog(t, C[cue], 1.0)))
        formula(c, m, x + 150, 590 + dy, 64, a, lit=af)
        pill(c, "SIMPLES", x + 150, 690 + dy, PURPLE, size=24, a=af * a, anchor="center", bounds=(0, 1920))
    pill(c, "Fe: as peças formam um BLOCO", 1590, 820, INK2, size=22, a=ep(t, C["14.e"] + 0.8, 0.4) * (1 - af), anchor="center", bounds=(0, 1920))
    regra(c, "1 elemento = simples", W / 2, 830, af, 34, PURPLE, w=700)


def b_maiuscula(c, t, C, B):
    head(c, t, B["start"], "ATENÇÃO AO SÍMBOLO", "Fe = 2 LETRAS, 1 ELEMENTO", AMBER)
    card(c, *CARD_R)
    a0 = ep(t, C["15.t"], 0.5)
    formula(c, "Fe", 520, 400, 260, a0)
    if a0 > 0:
        fw_ = text_w("F", "black", 260)
        tw_ = formula_w("Fe", 260)
        x0 = 520 - tw_ / 2
        text(c, "maiúscula", x0 + fw_ / 2, 590, 30, "black", INK, ep(t, C["15.t"] + 1.0, 0.4))
        text(c, "minúscula", x0 + fw_ + (tw_ - fw_) / 2 + 20, 590, 30, "black", INK2, ep(t, C["15.t"] + 1.8, 0.4))
    aa = ep(t, C["15.a"], 0.5)
    pill(c, "2 letras, mas 1 elemento só", 520, 680, AMBER, size=30, a=aa, anchor="center", bounds=(0, 1920))
    ab = ep(t, C["15.b"], 0.5)
    for k, s in enumerate(("Na", "Cl", "He")):
        ak = ab * ep(t, C["15.b"] + 0.4 * k, 0.4)
        x = 1050 + k * 200
        formula(c, s, x, 300, 90, ak, lit=ep(t, C["15.c"] + 0.3 * k, 0.4), upper=True)
        text(c, NOME[s], x, 380, 26, "bold", INK2, ak)
    ac = ep(t, C["15.c"], 0.5)
    regra(c, "cada MAIÚSCULA = um elemento novo", 1250, 520, ac, 32, GREEN, w=760)
    ad = ep(t, C["15.d"], 0.5)
    if ad > 0:
        text(c, "\"conte as letras\" = conte as MAIÚSCULAS", 1250, 660, 32, "black", GREEN, ad)


def b_composta(c, t, C, B):
    head(c, t, B["start"], "SUBSTÂNCIA", "COMPOSTA", BLUE)
    card(c, *CARD_R)
    for k, (cue, m, nome) in enumerate((("16.a", "H2O", "água"), ("16.b", "CO2", "gás carbônico"))):
        a, dy = rise(t, C[cue])
        if a <= 0:
            continue
        x = 520 + k * 880
        text(c, nome.upper(), x, 240 + dy, 30, "black", INK2, a)
        mol(c, m, x - (0 if k else 0), 380 + dy, 62 if k == 0 else 54, a, ease_io(prog(t, C[cue], 1.0)))
        formula(c, m, x, 540 + dy, 110, a, lit=1.5 * prog(t, C[cue] + 1.2, 1.2) + (0.5 if prog(t, C[cue] + 1.2, 1.2) >= 1 else 0))
        text(c, "2 cores", x, 670 + dy, 36, "black", PURPLE, ep(t, C[cue] + 2.5, 0.4) * a)
    defbox(c, "SUBSTÂNCIA COMPOSTA", "2 ou mais elementos (cores diferentes)", W / 2, 760, ep(t, C["16.c"], 0.5), w=900)


def b_composta_ex(c, t, C, B):
    head(c, t, B["start"], "SUBSTÂNCIAS COMPOSTAS", "2 OU MAIS ELEMENTOS", BLUE)
    a0 = ep(t, C["17.a"], 0.5)
    card(c, 160, 180, 760, 600, a0)
    text(c, "SAL DE COZINHA", 540, 240, 30, "black", INK2, a0)
    grow = ease_io(prog(t, C["17.b"], 1.2))
    if a0 > 0:
        c.save()
        c.clipRect(skia.Rect.MakeXYWH(170, 260, 740, 300))
        mol(c, "NaCl", 540, 410, lerp(34, 24, grow), a0, ease_io(prog(t, C["17.a"], 1.2)))
        if grow > 0:
            for dx in (-1, 1):
                c.save(); c.translate(dx * 8 * 24 * grow, 0)
                mol(c, "NaCl", 540, 410, 24, a0 * grow * 0.9, label=False)
                c.restore()
        c.restore()
    formula(c, "NaCl", 540, 620, 100, a0, lit=2.2 * prog(t, C["17.a"] + 1.0, 1.0), upper=True)
    pill(c, "um bloco enorme, todo encaixado", 540, 730, INK2, size=26, a=ep(t, C["17.b"], 0.5), anchor="center", bounds=(0, 1920))
    ac, dy = rise(t, C["17.c"])
    card(c, 1000, 180 + dy, 760, 600, ac)
    text(c, "GLICOSE (açúcar da uva)", 1380, 240 + dy, 30, "black", INK2, ac)
    mol(c, "C6H12O6", 1370, 420 + dy, 22, ac, ease_io(prog(t, C["17.c"], 1.6)), drop=40)
    formula(c, "C6H12O6", 1380, 620 + dy, 90, ac, lit=3.2 * prog(t, C["17.c"] + 1.6, 1.4))
    text(c, "24 peças · 3 cores", 1380, 730 + dy, 34, "black", PURPLE, ep(t, C["17.c"] + 3.0, 0.4) * ac)
    regra(c, "todas COMPOSTAS", W / 2, 840, ep(t, C["17.d"], 0.5), 32, PURPLE, w=520)


# ======================================================================
# bloco f: o ritual
# ======================================================================

def b_ritual(c, t, C, B):
    head(c, t, B["start"], "O RITUAL", "PARA CLASSIFICAR", PURPLE)
    cues = [C["18.a"], C["18.b"], C["18.c"]]
    k = ativo_em(t, [(cu, i) for i, cu in enumerate(cues)])
    ritual(c, 160, 180, 900, ep(t, C["18.t"], 0.5), cues, t, k, dy=150)
    a0 = ep(t, C["18.a"], 0.5)
    card(c, 1120, 180, 640, 600, a0)
    f = "CO2"
    formula(c, f, 1440, 340, 130, a0, lit=2.2 * prog(t, C["18.b"] + 0.4, 1.2), nums=1 - ep(t, WT(C, "18", "numeros"), 0.4))
    ab = ep(t, C["18.b"] + 1.6, 0.4)
    text(c, "C, O → 2 letras", 1440, 500, 40, "black", INK, ab)
    text(c, "o 2 pequeno não entra", 1440, 556, 28, "bold", RED, ep(t, WT(C, "18", "numeros"), 0.4))
    veredito(c, f, 1440, 680, ep(t, C["18.c"] + 1.2, 0.5))


def b_ritual_gancho(c, t, C, B):
    head(c, t, B["start"], "DE VOLTA AO GANCHO", "ELEMENTOS, NÃO ÁTOMOS", PURPLE)
    for k, (cue, m, n) in enumerate((("19.a", "O2", "2 átomos"), ("19.b", "S8", "8 átomos"), ("19.c", "H2O", "3 átomos"))):
        a0 = ep(t, C["19.t"], 0.5)
        x = 250 + k * 500
        card(c, x, 190, 440, 540, a0)
        mol(c, m, x + 220, 330, 30 if m == "S8" else 40, a0, label=False)
        text(c, n, x + 220, 440, 28, "bold", INK2, a0 * (1 - 0.5 * ep(t, C[cue], 0.4)))
        if t > C[cue] - 0.1:
            strike(c, x + 150, 430, x + 290, 430, a0, RED, ease_io(prog(t, C[cue], 0.4)))
        formula(c, m, x + 220, 540, 90, a0, lit=n_el(m) * prog(t, C[cue] + 0.2, 0.8), nums=1 - 0.6 * ep(t, C[cue], 0.4))
        veredito(c, m, x + 220, 660, ep(t, C[cue] + 1.0, 0.5), 26)
    regra(c, "critério: nº de ELEMENTOS, nunca de átomos", W / 2, 810, ep(t, C["19.d"], 0.5), 34, PURPLE, w=1100)


# ======================================================================
# bloco g: como se separa
# ======================================================================

def funil(c, cx, cy, a):
    if a <= 0:
        return
    p = skia.Path(); p.moveTo(cx - 60, cy - 50); p.lineTo(cx + 60, cy - 50); p.lineTo(cx + 12, cy + 10)
    p.lineTo(cx + 12, cy + 60); p.lineTo(cx - 12, cy + 60); p.lineTo(cx - 12, cy + 10); p.close()
    c.drawPath(p, paint("#D7DADF", a))
    c.drawPath(p, paint(INK2, a, stroke=4))


def eletrolise(c, cx, cy, a, t, t0):
    if a <= 0:
        return
    bequer(c, cx - 120, cy - 70, 240, 150, a, WATER, 0.8)
    for dx, col in ((-55, "#3A3A3C"), (55, "#3A3A3C")):
        rrect(c, cx + dx - 8, cy - 110, 16, 150, 4, col, a)
    line(c, cx - 55, cy - 110, cx - 55, cy - 140, RED, a, 4)
    line(c, cx + 55, cy - 110, cx + 55, cy - 140, BLUE, a, 4)
    line(c, cx - 55, cy - 140, cx + 55, cy - 140, INK2, a, 4)
    rrect(c, cx - 30, cy - 158, 60, 36, 6, AMBER, a)
    text_mid(c, "⚡", cx, cy - 140, 24, "black", INK, a)
    for j in range(4):
        ph = ((t - t0) * 0.7 + j * 0.25) % 1.0
        c.drawCircle(cx - 55 + (j % 2) * 8, cy + 50 - ph * 100, 6, paint("#FFFFFF", a * (1 - ph)))
        c.drawCircle(cx + 55 - (j % 2) * 8, cy + 50 - ph * 100, 5, paint("#FFFFFF", a * (1 - ph)))


def b_separar(c, t, C, B):
    head(c, t, B["start"], "DÁ PARA SEPARAR", "EM PARTES MAIS SIMPLES?", BLUE)
    rows = [("20.a", "MISTURA", "processo FÍSICO", "filtrar, destilar · as montagens ficam inteiras", BLUE),
            ("20.b", "COMPOSTA", "processo QUÍMICO", "desmonta as peças", PURPLE),
            ("20.d", "SIMPLES", "não se separa", "já tem uma cor só", GREEN)]
    for k, (cue, s1, s2, s3, col) in enumerate(rows):
        a, dy = rise(t, C[cue])
        if a <= 0:
            continue
        y = 180 + k * 210 + dy
        card(c, 160, y, 1600, 190, a)
        rrect(c, 160, y, 16, 190, 8, col, a)
        text(c, s1, 220, y + 80, 40, "black", INK, a, align="left")
        text(c, s2, 220, y + 136, 30, "black", col, a, align="left")
        text(c, s3, 640, y + 110, 28, "bold", INK2, a, align="left")
        if k == 0:
            funil(c, 1500, y + 95, a)
            for j in range(3):
                mol(c, "H2O", 1620 + (j % 2) * 40, y + 60 + j * 40, 12, a, label=False)
        elif k == 1:
            ac = ep(t, C["20.c"], 0.5)
            c.save(); c.translate(1340, y + 108); c.scale(0.62, 0.62)
            eletrolise(c, 0, 40, ac, t, C["20.c"])
            c.restore()
            if ac > 0:
                sp = ease_io(prog(t, C["20.c"] + 1.4, 1.2))
                mol(c, "H2O", 1560, y + 95, 26, ac * (1 - sp))
                mol(c, "H2", lerp(1560, 1520, sp), y + 70, 26, ac * sp)
                mol(c, "O2", lerp(1560, 1660, sp), y + 125, 22, ac * sp)
                text(c, "ex.: ELETRÓLISE da água", 640, y + 156, 24, "bold", PURPLE, ac, align="left")
        else:
            mol(c, "O2", 1500, y + 95, 34, a)
            check_icon(c, 1640, y + 95, 26, a, GRAY, "x")


# ======================================================================
# recapitulação
# ======================================================================

FRASES = ["Matéria é tudo que tem massa e ocupa espaço.",
          "Conte as letras, não os números.",
          "Uma letra: simples. Duas ou mais: composta."]


def b_recap(c, t, C, B):
    sid = "21" if B["start"] < C["32"] - 1 else "32"
    head(c, t, B["start"], "AS 3 FRASES", "PARA GUARDAR", GREEN)
    card(c, *CARD_R)
    for k, (cue, col) in enumerate((("a", BLUE), ("b", GREEN), ("c", PURPLE))):
        a, d = rise(t, C[f"{sid}.{cue}"])
        y = 330 + k * 150 + d
        badge_num(c, k + 1, 250, y - 16, a, 32, bg=col)
        text(c, FRASES[k], 310, y, 52, "black", INK, a, align="left")


# ======================================================================
# erros clássicos
# ======================================================================

def b_erro1(c, t, C, B):
    head(c, t, B["start"], "ERRO 1", "\"O₂ É COMPOSTA\"", RED)

    def extra(c, k, x, y, cw, a):
        if k == 2:
            mol(c, "O2", x + cw / 2, y + 470, 34, a)
    erro_tiles(c, t, [(C["22.a"], "O ERRO", ["!O₂ é composta"], RED),
                      (C["22.b"], "POR QUE PARECE CERTO", ["tem 2 átomos, e", "\"composto\" lembra", "mais de uma parte"], AMBER),
                      (C["22.c"], "A CORREÇÃO", ["mesma cor, 1 letra", "!SIMPLES"], GREEN)], extra)


def b_erro2(c, t, C, B):
    head(c, t, B["start"], "ERRO 2", "\"SIMPLES = 1 ÁTOMO\"", RED)

    def extra(c, k, x, y, cw, a):
        if k == 2:
            mol(c, "S8", x + cw / 2, y + 470, 24, a)
    erro_tiles(c, t, [(C["23.a"], "O ERRO", ["!simples =", "!átomo sozinho"], RED),
                      (C["23.b"], "POR QUE PARECE CERTO", ["\"simples\" lembra", "pequeno, uma", "coisa só"], AMBER),
                      (C["23.c"], "A CORREÇÃO", ["S₈: 8 átomos", "!1 ELEMENTO"], GREEN)], extra)


def b_erro3(c, t, C, B):
    head(c, t, B["start"], "ERRO 3", "IDENTIFICAR PELA MASSA", RED)

    def extra(c, k, x, y, cw, a):
        if k == 2:
            digital(c, x + cw / 2, y + 470, a, 0.55)
    erro_tiles(c, t, [(C["24.a"], "O ERRO", ["!massa ou volume", "!identificam"], RED),
                      (C["24.b"], "POR QUE PARECE CERTO", ["são as medidas", "que a gente", "mais conhece"], AMBER),
                      (C["24.c"], "A CORREÇÃO", ["1 kg de ferro =", "1 kg de algodão", "!use as ESPECÍFICAS"], GREEN)], extra)


# ======================================================================
# exercício rápido
# ======================================================================

EXER = [("25.a", "26.a", "H2"), ("25.b", "26.b", "CH4"), ("25.c", "26.c", "O3"), ("25.d", "26.d", "NaCl")]


def b_exercicio(c, t, C, B):
    head(c, t, B["start"], "SUA VEZ", "PAUSE E CLASSIFIQUE", GREEN)
    for k, (cue, rcue, f) in enumerate(EXER):
        a, dy = rise(t, C[cue])
        if a <= 0:
            continue
        x = 180 + k * 400
        card(c, x, 200 + dy, 360, 480, a)
        ar = ep(t, C[rcue], 0.5) if rcue in C else 0
        formula(c, f, x + 180, 340 + dy, 96, a, lit=n_el(f) * prog(t, C[rcue] + 0.2, 0.8) if ar > 0 else 0, upper=True)
        text(c, "?", x + 180, 520 + dy, 80, "black", LIGHT, a * (1 - ar))
        if ar > 0:
            mol(c, f, x + 180, 490 + dy, 30 if f != "NaCl" else 18, ar, label=False)
            k_ = n_el(f)
            text(c, f"{k_} {'letra' if k_ == 1 else 'letras'}", x + 180, 600 + dy, 28, "bold", INK2, ar)
            text(c, "SIMPLES" if k_ == 1 else "COMPOSTA", x + 180, 648 + dy, 32, "black", PURPLE, ar)
    pause_badge(c, W / 2 - 170, 730, ep(t, C["25.p"], 0.5) * (1 - prog(t, C["26.t"] - 0.3, 0.4)))


# ======================================================================
# questão 3
# ======================================================================

Q_F = ["O2", "O3", "H2O", "NaCl", "N2", "CO2", "Fe"]
ALTS = [("A", "2", "31.a", "contou átomos, não elementos"),
        ("B", "3", "31.b", "contou Fe como 2 elementos"),
        ("C", "4", None, ""),
        ("D", "5", "31.d", "não sai de nenhuma regra"),
        ("E", "7", "31.e", "confundiu pura com simples")]
ALT_CUE = ["28.a", "28.b", "28.c", "28.d", "28.e"]


def b_questao(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO ESTILO ENEM", "QUANTAS SÃO SIMPLES?", BLUE)
    card(c, 140, 170, 760, 660)
    pill(c, "QUESTÃO", 170, 214, BLUE, size=22, bounds=(0, 1920))
    text(c, "Considere as espécies químicas:", 180, 290, 30, "black", INK2, ep(t, C["27.e1"], 0.5), align="left")
    ae2 = ep(t, C["27.e2"], 0.5)
    for k, f in enumerate(Q_F):
        ak = ae2 * ep(t, C["27.e2"] + 0.55 * k, 0.35)
        formula(c, f, 230 + (k % 4) * 175, 345 + (k // 4) * 72, 46, ak, upper=True)
    text(c, "O número de substâncias simples é:", 180, 500, 30, "black", INK2, ep(t, C["27.e3"], 0.5), align="left")
    aok = ep(t, C["30.ok"], 0.5)
    for k, (L, s, cue_x, why) in enumerate(ALTS):
        a, d = rise(t, C[ALT_CUE[k]])
        y = 570 + k * 54 + d
        ok = cue_x is None
        if ok and aok > 0:
            rrect(c, 170, y - 38, 700, 52, 12, GREEN, 0.15 * aok)
        badge_num(c, L, 205, y - 12, a, 20, bg=GREEN if ok and aok > 0.5 else INK)
        ax = ep(t, C[cue_x], 0.4) if cue_x else 0
        text(c, s, 245, y, 32, "black", INK, a * (1 - 0.55 * ax), align="left")
        if ax > 0:
            strike(c, 240, y - 11, 268 + text_w(s, "black", 32), y - 11, ax, RED, ax)
            text(c, why, 300, y - 2, 24, "black", RED, ax, align="left")
    pause_badge(c, 1180, 400, ep(t, C["28.p"], 0.5) * (1 - prog(t, C["29.t"] - 0.3, 0.4)))
    ar = ep(t, C["29.t"], 0.5)
    sol_card(c, 940, 170, 840, 660, ar)
    if ar <= 0:
        return
    for k, s in enumerate(("1 olhe a fórmula", "2 conte as letras", "3 uma: simples")):
        pill(c, s, 1090 + k * 270, 262, PURPLE, size=22, a=ar, anchor="center", bounds=(0, 1920))
    cues = ["29.s1", "29.s2", "29.s3", "29.s4", "30.s5", "30.s6", "30.s7"]
    n_s = 0
    for k, (f, cu) in enumerate(zip(Q_F, cues)):
        a = ep(t, C[cu], 0.4)
        if a <= 0:
            continue
        col, row = k % 4, k // 4
        x, y = 1060 + col * 200, 400 + row * 175
        simp = n_el(f) == 1
        n_s += simp and a > 0.5
        rrect(c, x - 92, y - 70, 184, 150, 18, PURPLE if simp else "#FFFFFF", a * (0.12 if simp else 1), shadow=not simp)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x - 92, y - 70, 184, 150), 18, 18),
                    paint(PURPLE if simp else LINE, a, stroke=3))
        formula(c, f, x, y - 14, 52, a, lit=n_el(f) * prog(t, C[cu] + 0.1, 0.6), upper=True)
        text(c, "SIMPLES" if simp else "composta", x, y + 58, 24, "black", PURPLE if simp else INK2, a)
    ar2 = ep(t, C["30.r"], 0.5)
    if ar2 > 0:
        pill(c, "4 simples → RESPOSTA C", 1360, 790, GREEN, size=30, a=ar2, anchor="center", bounds=(0, 1920))


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    head(c, t, B["start"], "PRÓXIMO EPISÓDIO", "ALOTROPIA", PURPLE)
    card(c, *CARD_R)
    a0 = ep(t, C["33.t"], 0.5)
    for k in range(5):
        peca(c, 760 + k * 100, 260, 36, "C", a0 * ep(t, C["33.t"] + 0.2 * k, 0.4))
    text(c, "o MESMO elemento → substâncias diferentes?", W / 2, 360, 36, "black", INK, a0)
    aa = ep(t, C["33.a"], 0.5)
    lapis(c, 580, 560, aa, 1.0)
    text(c, "grafite", 580, 720, 34, "black", INK, aa)
    text_mid(c, "=", W / 2, 560, 90, "black", AMBER, ep(t, C["33.a"] + 1.4, 0.4))
    text(c, "C", W / 2, 650, 40, "black", INK2, ep(t, C["33.a"] + 1.4, 0.4))
    diamante(c, 1340, 560, ep(t, C["33.a"] + 0.8, 0.5), 1.0)
    text(c, "diamante", 1340, 720, 34, "black", INK, ep(t, C["33.a"] + 0.8, 0.5))
    pill(c, "EPISÓDIO 2: ALOTROPIA", W / 2, 800, PURPLE, size=32, a=ep(t, C["33.b"], 0.5), anchor="center", bounds=(0, 1920))


def b_cta(c, t, C, B):
    cta(c, t, C["34.like"], C["34.sub"], C["34.bell"], C["34.com"], C["34.bye"], "Você achava que O₂ era composta?")


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, materia=b_materia, materia_nao=b_materia_nao,
              prop_gerais=b_prop_gerais, prop_especificas=b_prop_especificas, prop_digital=b_prop_digital,
              molecula=b_molecula, pura=b_pura, simples=b_simples, simples_ex=b_simples_ex, maiuscula=b_maiuscula,
              composta=b_composta, composta_ex=b_composta_ex, ritual=b_ritual, ritual_gancho=b_ritual_gancho,
              separar=b_separar, recap=b_recap, erro1=b_erro1, erro2=b_erro2, erro3=b_erro3, exercicio=b_exercicio,
              questao=b_questao, ponte=b_ponte, cta=b_cta)
