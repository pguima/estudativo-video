"""Visual — Operações e Conjuntos Numéricos, Episódio 2: Os conjuntos numéricos — racional ou irracional? (iniciantes, tema claro)
Cores com função: azul = definição · roxo = regra · âmbar = armadilha · verde = atalho/dica/acerto · vermelho = erro.
Peças próprias deste episódio:
- bonecas(): os conjuntos como bonecas russas / círculos encaixados (ℕ ⊂ ℤ ⊂ ℚ), 𝕀 ao lado de ℚ e a caixa ℝ em volta.
- decimal_rola(): o decimal escrito dígito a dígito — 0,75 PARA; 0,333… REPETE (o 3 pisca); 1,4142135… segue sem padrão.
- ritual(): o teste sempre igual — acaba? · repete? · nem acaba nem repete?
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
ARQUIVO_FINAL = "enem_matematica_conjuntos_ep2_conjuntos_numericos.mp4"
CARD_R = (140, 150, 1640, 690)
SYM = "C:/Windows/Fonts/seguisym.ttf"   # ℕ ℤ ℚ ℝ 𝕀 ⊂ ∪ (a Inter não tem)
HL = "#7C5CFA"
# cor de cada conjunto (iguais no vídeo inteiro e na capa)
CN, CZ, CQ, CI, CR = "#0D9488", "#3B6CF6", "#6366F1", "#EA580C", "#1C1C1E"


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
    ws = [(w, C[sid] + t0) for w, t0 in _words().get(sid, []) if w == _n(palavra)]
    if depois is not None:
        ws = [x for x in ws if x[1] >= depois - 0.05]
    if not ws:
        return (depois if depois is not None else C[sid]) + 1.2
    return ws[k - 1 if k > 0 else k][1]


# ======================================================================
# texto matemático: ^sobrescrito, _subscrito e fonte reserva
# ======================================================================

@lru_cache(None)
def _symfont(size):
    f = skia.Font(skia.Typeface.MakeFromFile(SYM), size)
    f.setEmbolden(True); f.setSubpixel(True); f.setEdging(skia.Font.Edging.kAntiAlias)
    return f


@lru_cache(None)
def _has(ch, peso):
    return font(peso, 40).textToGlyphs(ch)[0] != 0


def _runs(s):
    out, buf, i = [], "", 0
    while i < len(s):
        if s[i] in "_^" and i + 1 < len(s):
            if buf:
                out.append((buf, None)); buf = ""
            mode = s[i]
            if s[i + 1] == "{":
                j = s.index("}", i)
                out.append((s[i + 2:j], mode)); i = j + 1
            else:
                out.append((s[i + 1], mode)); i += 2
        else:
            buf += s[i]; i += 1
    if buf:
        out.append((buf, None))
    return out


def _pieces(s, peso, size):
    for txt, mode in _runs(s):
        sz = size * 0.6 if mode else size
        dy = size * 0.2 if mode == "_" else -size * 0.42 if mode == "^" else 0
        cur, cur_sym = "", None
        for ch in txt:
            sym = not _has(ch, peso)
            if cur and sym != cur_sym:
                yield cur, (_symfont(sz) if cur_sym else font(peso, sz)), dy
                cur = ""
            cur += ch; cur_sym = sym
        if cur:
            yield cur, (_symfont(sz) if cur_sym else font(peso, sz)), dy


def ftext_w(s, peso, size):
    return sum(f.measureText(p) for p, f, _ in _pieces(s, peso, size))


def ftext(c, s, x, y, size, peso="black", color=None, a=1.0, align="center"):
    if a <= 0:
        return 0
    color = INK if color is None else color
    w = ftext_w(s, peso, size)
    xx = x - w / 2 if align == "center" else x - w if align == "right" else x
    for p, f, dy in _pieces(s, peso, size):
        c.drawString(p, xx, y + dy, f, paint(color, a))
        xx += f.measureText(p)
    return w


def fmid(c, s, x, cy, size, peso="black", color=None, a=1.0, align="center"):
    return ftext(c, s, x, cy + size * 0.36, size, peso, color, a, align)


def fbox(c, s, cx, cy, size, a, color=None):
    color = GREEN if color is None else color
    if a <= 0:
        return
    w = ftext_w(s, "black", size) + 60
    h = size * 1.6
    s_ = 0.85 + 0.15 * ease_back(clamp(a))
    c.save(); c.translate(cx, cy); c.scale(s_, s_)
    rrect(c, -w / 2, -h / 2, w, h, 18, color, a * 0.12)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(-w / 2, -h / 2, w, h), 18, 18), paint(color, a, stroke=3))
    fmid(c, s, 0, 0, size, "black", color, a)
    c.restore()


def tag(c, s, cx, cy, col, a, size=28):
    if a <= 0:
        return
    w, h = ftext_w(s, "black", size) + size * 1.2, size * 1.75
    rrect(c, cx - w / 2, cy - h / 2, w, h, h / 2.6, col, a, shadow=True)
    fmid(c, s, cx, cy, size, "black", on(col), a)


def regra(c, s, cx, cy, a, size=34, col=None, w=None):
    col = PURPLE if col is None else col
    if a <= 0:
        return
    dy = (1 - a) * 14
    ww = (w or ftext_w(s, "black", size) + 90)
    rrect(c, cx - ww / 2, cy - 44 + dy, ww, 88, 22, col, a * 0.12)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - ww / 2, cy - 44 + dy, ww, 88), 22, 22), paint(col, a, stroke=3))
    fmid(c, s, cx, cy + dy, size, "black", col, a)


def pause_badge(c, x, y, a, s="PAUSE E TENTE"):
    if a <= 0:
        return
    w = text_w(s, "black", 28) + 150
    rrect(c, x, y, w, 96, 24, AMBER, a, shadow=True)
    c.drawRect(skia.Rect.MakeXYWH(x + 28, y + 22, 14, 52), paint(INK, a))
    c.drawRect(skia.Rect.MakeXYWH(x + 54, y + 22, 14, 52), paint(INK, a))
    text_mid(c, s, x + 86, y + 48, 28, "black", INK, a, align="left")


def erro_tiles(c, t, items):
    cw, gap = 500, 40
    x0 = W / 2 - (3 * cw + 2 * gap) / 2
    for k, (tc, tt, lines, col) in enumerate(items):
        a, dy = rise(t, tc)
        if a <= 0:
            continue
        x, y = x0 + k * (cw + gap), 200 + dy
        card(c, x, y, cw, 500, a)
        rrect(c, x, y, cw, 70, 28, col, a * 0.15)
        text_mid(c, tt, x + cw / 2, y + 38, 30, "black", col, a)
        if k == 0:
            check_icon(c, x + cw / 2, y + 140, 30, a, RED, "x")
        elif k == 2:
            check_icon(c, x + cw / 2, y + 140, 30, a, GREEN)
        else:
            text_mid(c, "?", x + cw / 2, y + 140, 70, "black", AMBER, a)
        for j, ln in enumerate(lines):
            big = ln.startswith("!")
            ftext(c, ln.lstrip("!"), x + cw / 2, y + 250 + j * 60, 44 if big else 32, "black",
                  (RED if k == 0 else GREEN if k == 2 else INK) if big else INK, a)


# ======================================================================
# bonecas russas / conjuntos encaixados
# ======================================================================

def _ell(c, cx, cy, w, h, col, a, fill=0.10, stroke=5):
    r = skia.Rect.MakeXYWH(cx - w / 2, cy - h / 2, w, h)
    c.drawOval(r, paint(col, a * fill))
    c.drawOval(r, paint(col, a, stroke=stroke))


def bonecas(c, t, cx, cy, s, ap, ex=None, hl=None, metade=0.0):
    """ap = dict(N=,Z=,Q=,I=,R=) com o instante de entrada de cada conjunto (None = não aparece).
    ex = dict(N=[...], ...) exemplos dentro de cada região; hl = conjunto destacado; metade = 0..1 divide ℝ em duas metades."""
    ex = ex or {}
    qx = cx - 150 * s

    def A(k):
        return ep(t, ap[k], 0.6) if ap.get(k) is not None else 0

    def grow(a):
        return 0.86 + 0.14 * ease_back(clamp(a))

    aR = A("R")
    if aR > 0:
        w, h = 1180 * s, 540 * s
        x0, y0 = cx - 590 * s + 40 * s, cy - 270 * s
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x0, y0, w, h), 34, 34), paint(CR, aR * 0.04))
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x0, y0, w, h), 34, 34), paint(CR, aR, stroke=5))
        fmid(c, "ℝ  reais", x0 + 30 * s, y0 + 42 * s, 38 * s, "black", CR, aR, align="left")
        if metade > 0:
            xm = cx + 210 * s
            line(c, xm, y0 + 12, xm, y0 + h - 12, CR, aR * metade, 4, dash=[14, 10])
    layers = [("Q", qx, cy + 20 * s, 640 * s, 450 * s, CQ, "ℚ  racionais"),
              ("Z", qx, cy + 75 * s, 440 * s, 310 * s, CZ, "ℤ  inteiros"),
              ("N", qx, cy + 125 * s, 240 * s, 170 * s, CN, "ℕ  naturais")]
    for k, x, y, w, h, col, lab in layers:
        a = A(k)
        if a <= 0:
            continue
        g = grow(a)
        c.save(); c.translate(x, y); c.scale(g, g); c.translate(-x, -y)
        on_ = hl == k
        _ell(c, x, y, w, h, col, a, 0.16 if on_ else 0.08, 7 if on_ else 5)
        fmid(c, lab, x, y - h / 2 + 40 * s, 36 * s, "black", col, a)
        c.restore()
    aI = A("I")
    if aI > 0:
        x, y, w, h = cx + 400 * s, cy + 20 * s, 300 * s, 450 * s
        g = grow(aI)
        c.save(); c.translate(x, y); c.scale(g, g); c.translate(-x, -y)
        _ell(c, x, y, w, h, CI, aI, 0.16 if hl == "I" else 0.08, 7 if hl == "I" else 5)
        fmid(c, "𝕀", x, y - h / 2 + 44 * s, 44 * s, "black", CI, aI)
        fmid(c, "irracionais", x, y - h / 2 + 92 * s, 28 * s, "black", CI, aI)
        c.restore()
    # exemplos
    pos = dict(N=(qx, cy + 150 * s), Z=(qx, cy + 3 * s), Q=(qx, cy - 110 * s), I=(cx + 400 * s, cy + 40 * s))
    cols = dict(N=CN, Z=CZ, Q=CQ, I=CI)
    for k, itens in ex.items():
        x, y = pos[k]
        for j, (tc, sx) in enumerate(itens):
            a = ep(t, tc, 0.4) * A(k)
            if k == "I":
                fmid(c, sx, x, y + 30 * s + (j - (len(itens) - 1) / 2) * 70 * s, 44 * s, "black", cols[k], a)
            elif k == "Z":
                xx = x + (-1 if j % 2 == 0 else 1) * 160 * s
                fmid(c, sx, xx, y + (j // 2) * 50 * s, 38 * s, "black", cols[k], a)
            else:
                xx = x + (j - (len(itens) - 1) / 2) * 120 * s
                fmid(c, sx, xx, y, 38 * s, "black", cols[k], a)


def boneca(c, cx, base_y, h, col, a, rotulo=""):
    """silhueta simples de boneca russa (matriosca)"""
    if a <= 0:
        return
    w = h * 0.62
    body = skia.Rect.MakeXYWH(cx - w / 2, base_y - h * 0.68, w, h * 0.68)
    head = skia.Rect.MakeXYWH(cx - w * 0.36, base_y - h, w * 0.72, h * 0.42)
    c.drawOval(body, paint(col, a))
    c.drawOval(head, paint(col, a))
    c.drawOval(skia.Rect.MakeXYWH(cx - w * 0.24, base_y - h * 0.93, w * 0.48, h * 0.3), paint("#FDEBD3", a))
    c.drawCircle(cx, base_y - h * 0.38, w * 0.2, paint("#FFFFFF", a * 0.85))
    if rotulo:
        fmid(c, rotulo, cx, base_y - h * 0.38, h * 0.17, "black", col, a)


# ======================================================================
# decimal rolando e ritual
# ======================================================================

def decimal_rola(c, t, t0, x, y, size, inteiro, digs, tipo, a=1.0, vel=4.5, align="left"):
    """tipo: 'acaba' (para no fim), 'repete' (os dígitos repetidos piscam), 'nao' (segue sem padrão)"""
    if a <= 0 or t < t0:
        return 0
    n = int((t - t0) * vel)
    shown = digs[:min(n, len(digs))]
    s0 = inteiro + ","
    w0 = ftext_w(s0, "black", size)
    xx = x if align == "left" else x - (w0 + ftext_w(digs, "black", size)) / 2
    ftext(c, s0, xx, y, size, "black", INK, a, align="left")
    xx += w0
    for i, ch in enumerate(shown):
        ai = a * ep(t, t0 + (i + 1) / vel, 0.15)
        col = INK
        if tipo == "repete":
            col = mix(INK, AMBER, 0.5 + 0.5 * math.sin((t - t0) * 6 - i * 0.6))
        ftext(c, ch, xx, y, size, "black", col, ai, align="left")
        xx += ftext_w(ch, "black", size)
    acabou = n >= len(digs)
    if acabou and tipo != "acaba":
        dots = "…"
        ftext(c, dots, xx, y, size, "black", INK2, a * (0.55 + 0.45 * math.sin(t * 5)), align="left")
        xx += ftext_w(dots, "black", size)
    if acabou and tipo == "acaba":
        af = ep(t, t0 + len(digs) / vel + 0.2, 0.4)
        c.drawRect(skia.Rect.MakeXYWH(xx + 14, y - size * 0.8, 8, size * 0.9), paint(GREEN, a * af))
        text(c, "PAROU", xx + 34, y - size * 0.2, size * 0.3, "black", GREEN, a * af, align="left")
    return xx


RIT = ["ACABA?", "REPETE?", "NEM ACABA NEM REPETE?"]


def ritual(c, t, x, y, a, sel=None, t_sel=0.0, w=1520, cues=None):
    """faixa do teste: escreva em decimal → olhe depois da vírgula → acaba? repete? nem/nem?"""
    if a <= 0:
        return
    cw = [300, 300, 520]
    gap = (w - sum(cw)) / 2
    xx = x
    for k, s in enumerate(RIT):
        ak = a * (ep(t, cues[k], 0.4) if cues else 1.0)
        on_ = sel == k and t >= t_sel
        col = (RED if k == 2 else GREEN) if on_ else INK2
        aon = ep(t, t_sel, 0.35) if on_ else 0
        rrect(c, xx, y, cw[k], 74, 20, col, ak * (0.10 + 0.08 * aon), shadow=False)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(xx, y, cw[k], 74), 20, 20),
                    paint(col, ak * (0.35 + 0.65 * aon), stroke=3 if on_ else 2))
        text_mid(c, s, xx + cw[k] / 2, y + 37, 28, "black", col if on_ else INK, ak)
        if on_:
            res = "IRRACIONAL" if k == 2 else "RACIONAL"
            pill(c, res, xx + cw[k] / 2, y + 120, RED if k == 2 else GREEN, size=26, a=ak * aon, anchor="center",
                 bounds=(0, 1920))
        xx += cw[k] + gap


# ======================================================================
# gancho, promessa, pré-requisitos, conjunto
# ======================================================================

def quadrado_diag(c, x, y, L, a, diag=1.0, sobre=0.0, metades=0.0):
    """quadrado de lado L com a diagonal; sobre = quadrado desenhado em cima da diagonal"""
    if a <= 0:
        return
    if sobre > 0:   # quadrado sobre a diagonal (de (x, y+L) a (x+L, y)), para fora (para cima/direita)
        p = skia.Path()
        p.moveTo(x, y + L); p.lineTo(x + L, y); p.lineTo(x + L * 2, y + L); p.lineTo(x + L, y + 2 * L); p.close()
        # desenhado do outro lado: espelha para cima
        c.save(); c.translate(0, 0)
        p2 = skia.Path()
        p2.moveTo(x, y + L); p2.lineTo(x + L, y); p2.lineTo(x, y - L); p2.lineTo(x - L, y); p2.close()
        c.drawPath(p2, paint(AMBER, a * sobre * 0.18))
        c.drawPath(p2, paint(AMBER, a * sobre, stroke=5))
        if metades > 0:
            line(c, x - L, y, x + L, y, AMBER, a * metades, 3, dash=[10, 8])
            line(c, x, y - L, x, y + L, AMBER, a * metades, 3, dash=[10, 8])
        c.restore()
    rrect(c, x, y, L, L, 6, BLUE, a * 0.10)
    c.drawRect(skia.Rect.MakeXYWH(x, y, L, L), paint(BLUE, a, stroke=5))
    line(c, x, y + L, x + L, y, RED, a, 7, progress=diag)
    text(c, "1", x + L / 2, y + L + 44, 32, "black", BLUE, a)
    text(c, "1", x + L + 30, y + L / 2 + 12, 32, "black", BLUE, a)


def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "CONJUNTOS NUMÉRICOS · EPISÓDIO 2", BLUE)
    a0 = ep(t, C["01.a"], 0.5)
    card(c, 160, 190, 980, 300, a0)
    decimal_rola(c, t, C["01.a"] + 0.3, 210, 380, 84, "1", "41421356237", "nao", a0, vel=3.2)
    pill(c, "nunca termina", 330, 440, RED, size=26, a=ep(t, C["01.a"] + 0.8, 0.4), anchor="center")
    pill(c, "nunca se repete", 620, 440, RED, size=26, a=ep(t, C["01.b"], 0.4), anchor="center")
    ac = ep(t, C["01.c"], 0.5)
    card(c, 1220, 190, 540, 560, ac)
    quadrado_diag(c, 1380, 300, 230, ac, diag=ease_io(prog(t, C["01.c"] + 0.4, 1.0)))
    text(c, "a diagonal", 1495, 680, 32, "black", RED, ac)
    ad = ep(t, C["01.d"], 0.5)
    text(c, "ESCÂNDALO", 650, 640, 92, "black", AMBER, ad)
    text(c, "segundo a lenda", 650, 700, 30, "bold", INK2, ad)
    pill(c, "cai no ENEM", 650, 800, GREEN, size=32, a=ep(t, C["01.e"], 0.5), anchor="center")


def b_promessa(c, t, C, B):
    head(c, t, B["start"], "AO FINAL DESTA AULA", "VOCÊ VAI CONSEGUIR", GREEN)
    a, dy = rise(t, C["02.a"])
    card(c, 260, 220 + dy, 1400, 480, a)
    for k, (s, col, cue) in enumerate((("√9", GREEN, "02.b"), ("0,333…", GREEN, "02.b"), ("π", RED, "02.b"), ("1/2", GREEN, "02.b"))):
        x = 470 + k * 330
        ak = a * ep(t, C["02.a"] + 0.5 * k, 0.4)
        fmid(c, s, x, 380 + dy, 80, "black", INK, ak)
        ab = ep(t, C[cue] + 0.5 * k, 0.4)
        pill(c, "IRRACIONAL" if col == RED else "RACIONAL", x, 520 + dy, col, size=24, a=ab * a, anchor="center")
    text(c, "em segundos", W / 2, 640 + dy, 40, "black", BLUE, ep(t, C["02.b"] + 1.5, 0.5))


def b_prereq(c, t, C, B):
    if t < C["04"] - 0.2:
        head(c, t, B["start"], "LEMBRETE 1", "FRAÇÃO É DIVISÃO", BLUE)
        card(c, *CARD_R)
        aa = ep(t, C["03.a"], 0.5)
        frac(c, "3", "4", 420, 400, 120, INK, aa)
        ftext(c, "= 3 ÷ 4", 560, 440, 90, "black", INK, ep(t, C["03.b"], 0.5), align="left")
        ftext(c, "= 0,75", 1000, 440, 90, "black", GREEN, ep(t, WT(C, "03", "setenta", 1, C["03.b"]), 0.4), align="left")
        text(c, "decimal: escrito com vírgula", 1150, 520, 28, "black", BLUE, ep(t, WT(C, "03", "decimal"), 0.4))
        ac = ep(t, C["03.c"], 0.4)
        arrow(c, 300, 320, 380, 345, BLUE, ac, 4, 14)
        text(c, "NUMERADOR", 300, 300, 30, "black", BLUE, ac, align="right")
        ad = ep(t, C["03.d"], 0.4)
        arrow(c, 300, 560, 380, 520, BLUE, ad, 4, 14)
        text(c, "DENOMINADOR", 300, 590, 30, "black", BLUE, ad, align="right")
        text(c, "em quantas partes", 300, 630, 24, "bold", INK2, ad, align="right")
        return
    head(c, t, C["04"], "LEMBRETE 2", "RAIZ QUADRADA", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["04.a"], 0.5)
    ftext(c, "3^2 = 3 × 3 = 9", W / 2 - 300, 360, 90, "black", INK, aa)
    ab = ep(t, C["04.b"], 0.5)
    ftext(c, "√9 = 3", W / 2 + 420, 360, 90, "black", GREEN, ab)
    arrow(c, 960, 460, 1240, 460, BLUE, ab, 5, 18)
    arrow(c, 1240, 520, 960, 520, BLUE, ab, 5, 18)
    text(c, "quadrado", 1100, 445, 28, "black", INK2, aa)
    text(c, "raiz: o caminho de volta", 1100, 575, 28, "black", BLUE, ab)
    text(c, "o número que, vezes ele mesmo, dá 9", W / 2, 720, 34, "black", INK, ep(t, WT(C, "04", "mesmo"), 0.5))


def b_conjunto(c, t, C, B):
    head(c, t, B["start"], "PALAVRA-CHAVE", "CONJUNTO", BLUE)
    card(c, *CARD_R)
    pill(c, "conjunto = grupo de coisas com algo em comum", W / 2, 250, BLUE, size=30, a=ep(t, C["05.a"], 0.5), anchor="center")
    dias = ["seg", "ter", "qua", "qui", "sex", "sáb", "dom"]
    ab = ep(t, C["05.a"] + 1.5, 0.5)
    _ell(c, W / 2, 470, 1100, 260, BLUE, ab)
    for k, d in enumerate(dias):
        text_mid(c, d, W / 2 - 390 + k * 130, 470, 40, "black", INK, ab * ep(t, C["05.a"] + 1.7 + 0.15 * k, 0.3))
    ac = ep(t, C["05.b"], 0.5)
    fmid(c, "{ seg, ter, qua, qui, sex, sáb, dom }", W / 2, 720, 48, "black", INK, ac)
    for x in (W / 2 - ftext_w("{ seg, ter, qua, qui, sex, sáb, dom }", "black", 48) / 2 + 14,
              W / 2 + ftext_w("{ seg, ter, qua, qui, sex, sáb, dom }", "black", 48) / 2 - 14):
        c.drawCircle(x, 718, 34, paint(BLUE, ac * ep(t, C["05.b"] + 0.8, 0.4), stroke=4))
    text(c, "chaves", W / 2, 800, 28, "black", BLUE, ep(t, C["05.b"] + 0.8, 0.4))


def b_historia(c, t, C, B):
    head(c, t, B["start"], "A HISTÓRIA DOS NÚMEROS", "CADA PROBLEMA, UM NÚMERO NOVO", BLUE)
    passos = [("contar ovelhas", "ℕ", CN), ("dívida, frio", "ℤ", CZ), ("dividir a pizza", "ℚ", CQ), ("a diagonal", "𝕀", CI)]
    for k, (s, sym, col) in enumerate(passos):
        a, dy = rise(t, C["06.a"] + 0.6 * k)
        x = 230 + k * 400
        card(c, x, 280 + dy, 340, 380, a)
        text(c, "problema", x + 170, 350 + dy, 24, "bold", INK2, a)
        text(c, s, x + 170, 410 + dy, 32, "black", INK, a)
        arrow(c, x + 170, 450 + dy, x + 170, 510 + dy, INK2, a, 4, 14)
        fmid(c, sym, x + 170, 580 + dy, 90, "black", col, a)
        if k < 3:
            arrow(c, x + 350, 470 + dy, x + 390, 470 + dy, LIGHT, a, 4, 12)


# ======================================================================
# blocos a-e: os conjuntos, um a um (as bonecas vão se formando)
# ======================================================================

BX, BY, BS = 960, 520, 1.0   # posição padrão do diagrama


def ovelha(c, x, y, a, r=34):
    if a <= 0:
        return
    for dx, dy in ((-0.5, 0), (0.5, 0), (0, -0.45), (-0.25, 0.3), (0.25, 0.3)):
        c.drawCircle(x + dx * r, y + dy * r, r * 0.62, paint("#FFFFFF", a))
        c.drawCircle(x + dx * r, y + dy * r, r * 0.62, paint(LIGHT, a, stroke=2))
    c.drawOval(skia.Rect.MakeXYWH(x + r * 0.7, y - r * 0.55, r * 0.7, r * 0.55), paint(INK2, a))


def b_naturais(c, t, C, B):
    head(c, t, B["start"], "1º PROBLEMA: CONTAR", "OS NATURAIS", CN)
    card(c, *CARD_R)
    if t < C["08"] - 0.2:
        for k in range(3):
            ak = ep(t, C["07.b"] + 0.5 * k, 0.4)
            ovelha(c, 380 + k * 170, 420, ep(t, C["07.a"], 0.5), 62)
            fmid(c, str(k + 1), 380 + k * 170, 290, 64, "black", CN, ak)
        ac = ep(t, C["07.c"], 0.5)
        tag(c, "naturais = números de contar", 1250, 330, BLUE, ac, 30)
        ad = ep(t, C["07.d"], 0.5)
        fmid(c, "ℕ", 1250, 540, 220, "black", CN, ad)
        text(c, "N com traço duplo", 1250, 720, 30, "black", INK2, ad)
        return
    aa = ep(t, C["08.a"], 0.5)
    ovelha(c, 360, 380, 0.25 * aa, 40)
    fmid(c, "0", 360, 380, 90, "black", CN, aa)
    text(c, "no Brasil, o ZERO é natural", 360, 520, 30, "black", AMBER, aa)
    ab = ep(t, C["08.b"], 0.5)
    fmid(c, "ℕ = {0, 1, 2, 3, …}", 1150, 400, 84, "black", CN, ab)
    text(c, "…  = continua para sempre", 1150, 520, 30, "black", BLUE, ep(t, WT(C, "08", "continua"), 0.4))


def termometro(c, x, y, a, nivel):
    if a <= 0:
        return
    h = 340
    rrect(c, x - 22, y, 44, h, 22, "#FFFFFF", a, shadow=True, stroke=3, stroke_color=LIGHT)
    c.drawCircle(x, y + h + 16, 38, paint("#FFFFFF", a)); c.drawCircle(x, y + h + 16, 38, paint(LIGHT, a, stroke=3))
    c.drawCircle(x, y + h + 16, 28, paint(BLUE, a))
    yv = lambda v: y + h - 30 - (v + 10) / 40 * (h - 60)
    rrect(c, x - 10, yv(nivel), 20, y + h + 10 - yv(nivel), 10, BLUE, a)
    line(c, x - 50, yv(0), x + 50, yv(0), INK, a, 3, dash=[8, 6])
    text_mid(c, "0", x + 62, yv(0), 24, "bold", INK2, a, align="left")
    text_mid(c, "−2 °C", x + 62, yv(-2) + 22, 28, "black", RED, a, align="left")


def b_inteiros(c, t, C, B):
    head(c, t, B["start"], "2º PROBLEMA: ABAIXO DO ZERO", "OS INTEIROS", CZ)
    if t < C["11"] - 0.2:
        card(c, *CARD_R)
        if t < C["10"] - 0.2:
            aa = ep(t, C["09.t"], 0.5)
            ftext(c, "3 − 5 = ?", 460, 380, 100, "black", INK, aa)
            text(c, "tem R$ 3, gasta R$ 5", 460, 470, 32, "bold", INK2, aa)
            termometro(c, 1200, 230, ep(t, C["09.a"], 0.5), lerp(10, -2, ease_io(prog(t, C["09.a"] + 0.3, 1.2))))
            regra(c, "ℕ não tem nada abaixo do zero", W / 2, 760, ep(t, C["09.b"], 0.5), 34, AMBER)
            return
        aa = ep(t, C["10.a"], 0.5)
        tag(c, "inteiros = negativos + naturais", W / 2, 260, BLUE, aa, 30)
        ab = ep(t, C["10.b"], 0.5)
        fmid(c, "ℤ", 420, 470, 200, "black", CZ, ab)
        text(c, "de Zahlen: \"números\" em alemão", 420, 640, 28, "black", INK2, ab)
        ac = ep(t, C["10.c"], 0.5)
        fmid(c, "ℤ = {…, −2, −1, 0, 1, 2, …}", 1150, 480, 66, "black", CZ, ac)
        arrow(c, 860, 580, 760, 580, RED, ac, 5, 16)
        arrow(c, 1440, 580, 1540, 580, GREEN, ac, 5, 16)
        text(c, "para os dois lados", 1150, 595, 28, "black", INK2, ac)
        return
    # 11: bonecas
    aa = ep(t, C["11.a"], 0.5)
    card(c, 160, 180, 560, 600, aa)
    for k, (h, col, lab) in enumerate(((330, CZ, "ℤ"), (230, CN, "ℕ"))):
        boneca(c, 330 + k * 210, 700, h, col, aa * ep(t, C["11.a"] + 0.4 * k, 0.4), lab)
    text(c, "bonecas russas", 440, 250, 32, "black", INK, aa)
    bonecas(c, t, 1250, 480, 1.0, dict(N=C["11.t"], Z=C["11.b"]), hl="Z" if t > C["11.b"] else None,
            ex=dict(N=[(C["11.t"], "0"), (C["11.t"], "1"), (C["11.t"], "2")], Z=[(C["11.b"] + 0.5, "−1"), (C["11.b"] + 0.7, "−2")]))


def pizza(c, cx, cy, r, comidas, a):
    if a <= 0:
        return
    for k in range(4):
        p = skia.Path()
        p.moveTo(cx, cy)
        p.arcTo(skia.Rect.MakeXYWH(cx - r, cy - r, 2 * r, 2 * r), -90 + k * 90, 90, False)
        p.close()
        on_ = k < comidas
        c.drawPath(p, paint("#F59E0B" if on_ else "#FDE7B0", a))
        c.drawPath(p, paint("#FFFFFF", a, stroke=6))
    c.drawCircle(cx, cy, r, paint("#B45309", a, stroke=5))


def b_racionais(c, t, C, B):
    head(c, t, B["start"], "3º PROBLEMA: DIVIDIR", "OS RACIONAIS", CQ)
    if t < C["14"] - 0.2:
        card(c, *CARD_R)
        if t < C["13"] - 0.2:
            aa = ep(t, C["12.t"], 0.5)
            pizza(c, 520, 470, 200, int(clamp((t - C["12.a"]) * 2, 0, 3)), aa)
            ab = ep(t, C["12.b"], 0.5)
            frac(c, "3", "4", 1150, 430, 140, CQ, ab)
            text(c, "entre 0 e 1: não é inteiro", 1150, 690, 32, "black", AMBER, ep(t, C["12.c"], 0.5))
            return
        aa = ep(t, C["13.t"], 0.5)
        tag(c, "racional = fração de inteiros", W / 2, 260, BLUE, aa, 30)
        fmid(c, "ℚ", 430, 480, 200, "black", CQ, ep(t, C["13.a"], 0.5))
        text(c, "de quociente: resultado da divisão", 430, 650, 26, "black", INK2, ep(t, C["13.a"], 0.5))
        ab = ep(t, C["13.b"], 0.5)
        frac(c, "a", "b", 1150, 430, 120, CQ, ab)
        regra(c, "b ≠ 0", 1150, 640, ab, 40, PURPLE, w=300)
        text(c, "ninguém corta pizza em 0 pedaços", 1150, 740, 28, "black", INK2, ep(t, C["13.c"], 0.5))
        return
    card(c, 160, 180, 560, 600)
    for k, (cue, s) in enumerate((("14.a", "1/2"), ("14.b", "0,75 = 3/4"), ("14.c", "−5 = −5/1"))):
        a, dy = rise(t, C[cue])
        fmid(c, s, 440, 300 + k * 130 + dy, 52, "black", CQ, a)
    regra(c, "todo inteiro vira fração", 440, 700, ep(t, C["14.d"], 0.5), 28, PURPLE, w=480)
    bonecas(c, t, 1250, 470, 1.0, dict(N=C["14"] - 5, Z=C["14"] - 5, Q=C["14.e"]), hl="Q" if t > C["14.e"] else None,
            ex=dict(N=[(0, "1"), (0, "2")], Z=[(0, "−1"), (0, "−5")], Q=[(C["14.e"] + 0.5, "1/2"), (C["14.e"] + 0.7, "0,75")]))


def b_irracionais(c, t, C, B):
    head(c, t, B["start"], "4º PROBLEMA: A DIAGONAL", "OS IRRACIONAIS", CI)
    card(c, *CARD_R)
    if t < C["17"] - 0.2:
        a0 = ep(t, C["15.a"], 0.5)
        sobre = ep(t, C["16.a"], 0.8)
        L = 200
        quadrado_diag(c, 560, 400, L, a0, diag=ease_io(prog(t, C["15.b"], 0.9)), sobre=sobre, metades=ep(t, C["16.a"] + 1.4, 0.5))
        if t < C["16"]:
            text(c, "diagonal: de um canto ao outro", 1200, 460, 32, "black", RED, ep(t, C["15.b"], 0.5))
            text(c, "lado 1", 660, 680, 28, "black", BLUE, a0)
            return
        text(c, "área 1", 660, 520, 30, "black", BLUE, sobre)
        text(c, "área 2", 560, 330, 34, "black", AMBER, sobre)
        text(c, "o quadrado grande = 4 metades = 2 quadrados de área 1", 1260, 460, 26, "black", AMBER, ep(t, C["16.a"] + 1.4, 0.5))
        ab = ep(t, C["16.b"], 0.5)
        fmid(c, "diagonal × diagonal = 2", 1260, 380, 46, "black", INK, ab)
        fbox(c, "diagonal = √2", 1260, 540, 64, ep(t, C["16.c"], 0.5), CI)
        return
    if t < C["18"] - 0.2:
        a0 = ep(t, C["17.t"], 0.5)
        fmid(c, "√2 =", 300, 380, 80, "black", CI, a0, align="left")
        decimal_rola(c, t, C["17.a"], 520, 410, 80, "1", "4142135623730950", "nao", a0, vel=3.2)
        pill(c, "nunca termina", 640, 560, RED, size=28, a=ep(t, C["17.b"], 0.4), anchor="center")
        pill(c, "nunca se repete", 1000, 560, RED, size=28, a=ep(t, C["17.c"], 0.4), anchor="center")
        regra(c, "nenhuma fração de inteiros chega nela", W / 2, 720, ep(t, C["17.d"], 0.5), 32, AMBER)
        return
    aa = ep(t, C["18.t"], 0.5)
    tag(c, "irracional = decimal infinito que não se repete", W / 2, 230, BLUE, aa, 28)
    fmid(c, "𝕀", 360, 520, 180, "black", CI, ep(t, C["18.b"], 0.5))
    bonecas(c, t, 1100, 530, 0.85, dict(N=C["18"] - 5, Z=C["18"] - 5, Q=C["18"] - 5, I=C["18.c"]), hl="I" if t > C["18.d"] else None,
            ex=dict(Q=[(0, "1/2"), (0, "0,75")], I=[(C["18.c"] + 0.5, "√2")]))
    ftext(c, "outra boneca, do lado de FORA de ℚ", 1100, 840, 30, "black", CI, ep(t, C["18.d"], 0.5))


class Reta:
    def __init__(self, x0, x1, y, lo, hi):
        self.x0, self.x1, self.y, self.lo, self.hi = x0, x1, y, lo, hi

    def X(self, v):
        return lerp(self.x0, self.x1, (v - self.lo) / (self.hi - self.lo))

    def draw(self, c, a, buraco=None, tampa=0.0):
        if a <= 0:
            return
        y = self.y
        arrow(c, self.x0 - 20, y, self.x1 + 34, y, INK2, a, 5, 14)
        for v in range(int(self.lo), int(self.hi) + 1):
            x = self.X(v)
            line(c, x, y - 12, x, y + 12, INK2, a, 3)
            text(c, str(v), x, y + 50, 28, "black", INK, a)
        if buraco is not None:
            x = self.X(buraco)
            c.drawCircle(x, y, 13, paint("#FFFFFF" if tampa < 1 else CI, a))
            c.drawCircle(x, y, 13, paint(CI, a, stroke=3))
            if tampa > 0:
                c.drawCircle(x, y, 13 * tampa, paint(CI, a))


def b_reais(c, t, C, B):
    head(c, t, B["start"], "JUNTANDO TUDO", "OS REAIS", CR)
    if t < C["20"] - 0.2:
        card(c, *CARD_R)
        a0 = ep(t, C["19.a"], 0.5)
        r = Reta(300, 1620, 450, 0, 3)
        tampa = ep(t, C["19.c"], 0.6)
        r.draw(c, a0, buraco=math.sqrt(2) if t > C["19.b"] else None, tampa=tampa)
        for v, s in ((0.5, "1/2"), (0.75, "3/4"), (1.5, "3/2"), (2.25, "9/4")):
            x = r.X(v)
            c.drawCircle(x, 450, 9, paint(CQ, a0))
            fmid(c, s, x, 380, 28, "black", CQ, a0 * ep(t, C["19.b"], 0.4))
        fmid(c, "√2 ≈ 1,41", r.X(math.sqrt(2)), 330, 40, "black", CI, ep(t, C["19.a"] + 0.6, 0.4))
        text(c, "só com racionais: BURACOS", W / 2, 640, 36, "black", AMBER, ep(t, C["19.b"], 0.5) * (1 - tampa))
        text(c, "os irracionais tapam os buracos", W / 2, 640, 36, "black", GREEN, tampa)
        return
    bonecas(c, t, 800, 500, 0.8, dict(N=0, Z=0, Q=0, I=0, R=C["20.a"]), hl="R",
            ex=dict(Q=[(0, "1/2"), (0, "0,75")], I=[(0, "√2"), (0, "π")]))
    ab = ep(t, C["20.b"], 0.5)
    r = Reta(1380, 1760, 260, 0, 2)
    tag(c, "a reta SEM buracos", 1570, 330, BLUE, ab, 26)
    ac = ep(t, C["20.c"], 0.5)
    card(c, 1360, 420, 420, 300, ac)
    fmid(c, "∪", 1570, 520, 110, "black", BLUE, ac)
    text(c, "união = juntar", 1570, 650, 30, "black", BLUE, ac)
    fbox(c, "ℝ = ℚ ∪ 𝕀", 1570, 800, 50, ep(t, C["20.d"], 0.5), PURPLE)


def b_cadeia(c, t, C, B):
    head(c, t, B["start"], "AS BONECAS INTEIRAS", "QUEM CABE DENTRO DE QUEM", PURPLE)
    if t < C["22"] - 0.2:
        card(c, *CARD_R)
        aa = ep(t, C["21.a"], 0.5)
        fmid(c, "⊂", 420, 420, 200, "black", BLUE, aa)
        text(c, "\"está contido em\" = cabe dentro de", 420, 620, 30, "black", BLUE, aa)
        parts = [("ℕ", CN, "21.b"), ("⊂", INK, "21.b"), ("ℤ", CZ, "21.b"), ("⊂", INK, "21.c"), ("ℚ", CQ, "21.c"),
                 ("⊂", INK, "21.d"), ("ℝ", CR, "21.d")]
        x = 860
        for s, col, cue in parts:
            a = ep(t, C[cue], 0.4)
            ftext(c, s, x, 450, 96, "black", col, a, align="left")
            x += ftext_w(s, "black", 96) + 30
        for k, (h, col, lab) in enumerate(((230, CR, "ℝ"), (190, CQ, "ℚ"), (150, CZ, "ℤ"), (110, CN, "ℕ"))):
            boneca(c, 960 + k * 170, 760, h, col, ep(t, C["21.b"] + 0.3 * k, 0.4), lab)
        return
    if t < C["23"] - 0.2:
        card(c, *CARD_R)
        fmid(c, "ℕ ⊂ ℤ ⊂ ℚ ⊂ ℝ", W / 2, 260, 80, "black", INK, 1)
        regra(c, "o caminho de VOLTA não vale", W / 2, 390, ep(t, C["22.t"], 0.5), 34, AMBER)
        for k, (cue, num, sim, nao) in enumerate((("22.a", "−5", ("ℤ", CZ), ("ℕ", CN)), ("22.b", "1/2", ("ℚ", CQ), ("ℤ", CZ)))):
            a, dy = rise(t, C[cue])
            x = 560 + k * 800
            fmid(c, num, x, 530 + dy, 90, "black", INK, a)
            for j, ((sym, col), ok) in enumerate(((sim, True), (nao, False))):
                xx = x - 110 + j * 220
                fmid(c, sym, xx - 22, 680 + dy, 60, "black", col, a)
                check_icon(c, xx + 36, 680 + dy, 24, a, GREEN if ok else RED, "check" if ok else "x")
        return
    bonecas(c, t, 900, 520, 0.92, dict(N=0, Z=0, Q=0, I=C["23.a"] - 0.3, R=0), hl="I" if t < C["23.b"] else None,
            metade=ep(t, C["23.b"], 0.6),
            ex=dict(Q=[(0, "1/2"), (0, "0,75")], I=[(0, "√2"), (0, "π")]))
    text(c, "FORA da fila: reais, mas não racionais", 900, 860, 30, "black", CI, ep(t, C["23.a"], 0.5))
    tag(c, "racionais", 900 - 150 * 0.92, 205, CQ, ep(t, C["23.c"], 0.4), 26)
    tag(c, "irracionais", 900 + 400 * 0.92, 205, CI, ep(t, C["23.d"], 0.4), 26)


def b_notacoes(c, t, C, B):
    head(c, t, B["start"], "ENFEITES DO ENUNCIADO", "SÓ PARA NÃO TRAVAR", BLUE)
    card(c, *CARD_R)
    rows = [("24.a", "*", "asterisco = TIRA O ZERO", None),
            ("24.b", "ℕ*", "{1, 2, 3, …}", CN),
            ("24.c", "ℝ*", "todos os reais, menos o 0", CR),
            ("25.a", "ℤ_+", "{0, 1, 2, …}  zero e positivos", CZ),
            ("25.b", "ℤ_−", "{…, −2, −1, 0}  zero e negativos", CZ),
            ("25.c", "ℤ*_+", "{1, 2, 3, …}  só positivos", CZ)]
    for k, (cue, sym, s, col) in enumerate(rows):
        a, dy = rise(t, C[cue])
        y = 250 + k * 100 + dy
        if col is None:
            tag(c, s, W / 2, y - 10, BLUE, a, 30)
            continue
        fmid(c, sym, 460, y - 12, 66, "black", col, a)
        fmid(c, s, 620, y - 12, 40, "black", INK, a, align="left")


# ======================================================================
# blocos h-j: o critério, os famosos, a pegadinha da raiz
# ======================================================================

def b_criterio(c, t, C, B):
    head(c, t, B["start"], "RACIONAL OU IRRACIONAL?", "O TESTE DA FORMA DECIMAL", PURPLE)
    card(c, *CARD_R)
    a0 = ep(t, C["26.b"], 0.5)
    passos = [("26.c", "1. escreva em decimal"), ("26.d", "2. olhe depois da vírgula")]
    for k, (cue, s) in enumerate(passos):
        tag(c, s, 560 + k * 760, 230, BLUE, ep(t, C[cue], 0.4), 26)
    sel, tsel = None, 0
    if t >= C["27"]:
        sel, tsel = 0, C["27.a"]
    if t >= C["28"]:
        sel, tsel = 1, C["28.a"]
    if t >= C["29"]:
        sel, tsel = 2, C["29.a"]
    ritual(c, t, 200, 310, a0, sel, tsel, cues=[C["26.e"] + 0.3, C["26.e"] + 0.9, C["26.e"] + 1.5])
    x0 = 330
    if C["27"] - 0.2 <= t < C["28"] - 0.2:
        ftext(c, "3/4 =", 330, 600, 80, "black", INK, 1)
        decimal_rola(c, t, C["27.t"] + 0.6, 580, 600, 80, "0", "75", "acaba", 1, vel=3)
        tag(c, "decimal exato: acaba", 1300, 570, BLUE, ep(t, C["27.b"], 0.4), 30)
    elif C["28"] - 0.2 <= t < C["29"] - 0.2:
        ftext(c, "1/3 =", 330, 600, 80, "black", INK, 1)
        xe = decimal_rola(c, t, C["28.t"] + 0.6, 580, 600, 80, "0", "33333333", "repete", 1, vel=3)
        tag(c, "dízima periódica: repete", 1380, 540, BLUE, ep(t, C["28.b"], 0.4), 28)
        tag(c, "período = o 3, que repete", 1380, 620, BLUE, ep(t, C["28.c"], 0.4), 28)
        ad = ep(t, C["28.d"], 0.5)
        fmid(c, "0,333… = 1/3", 600, 740, 48, "black", GREEN, ad)
        text(c, "tem fração que a gera · cálculo: vídeo próprio", 1180, 752, 26, "black", INK2, ep(t, C["28.e"], 0.4))
    elif t >= C["29"] - 0.2:
        ftext(c, "√2 =", 330, 600, 80, "black", INK, 1)
        decimal_rola(c, t, C["29.t"] + 0.6, 560, 600, 80, "1", "414213562", "nao", 1, vel=3)
        regra(c, "acaba ou repete → RACIONAL  ·  nem acaba nem repete → IRRACIONAL", W / 2, 770,
              ep(t, C["29.c"], 0.5), 30, PURPLE, w=1480)


def b_famosos(c, t, C, B):
    head(c, t, B["start"], "OS IRRACIONAIS DA PROVA", "OS QUE MAIS APARECEM", CI)
    card(c, *CARD_R)
    a0 = ep(t, C["30.a"], 0.5)
    text(c, "raízes NÃO exatas", 520, 250, 32, "black", CI, a0)
    for k, s in enumerate(("√2", "√3", "√5", "√10")):
        fmid(c, s, 260 + k * 175, 360, 72, "black", INK, ep(t, C["30.a"] + 0.6 + 0.5 * k, 0.4))
    fam = [("31.a", "π ≈ 3,14159…", "contorno do círculo ÷ largura"),
           ("31.b", "e ≈ 2,718…", "contas de crescimento"),
           ("31.c", "φ ≈ 1,618…", "número de ouro: arte e natureza")]
    for k, (cue, s, sub) in enumerate(fam):
        a, dy = rise(t, C[cue])
        y = 520 + k * 100 + dy
        fmid(c, s, 220, y, 54, "black", CI, a, align="left")
        text_mid(c, sub, 820, y, 30, "bold", INK2, a, align="left")
    if C["31.a"] < t:
        # círculo com contorno e largura
        a = ep(t, C["31.a"], 0.5) * (1 - prog(t, C["31.b"], 0.4))
        if a > 0:
            c.drawCircle(1500, 330, 110, paint(CI, a, stroke=6))
            line(c, 1390, 330, 1610, 330, BLUE, a, 5)


def b_raiz_exata(c, t, C, B):
    head(c, t, B["start"], "PEGADINHA", "TER RAIZ NÃO É SER IRRACIONAL", AMBER)
    card(c, *CARD_R)
    if t < C["33"] - 0.2:
        regra(c, "todo número com raiz é irracional?  NÃO", W / 2, 240, ep(t, C["32.a"], 0.5), 34, AMBER)
        ex = [("32.b", "√9 = 3", "3 × 3 = 9"), ("32.c", "√0,25 = 0,5", "0,5 × 0,5 = 0,25"), ("32.d", "√(16/25) = 4/5", "4/5 × 4/5 = 16/25")]
        for k, (cue, s, why) in enumerate(ex):
            a, dy = rise(t, C[cue])
            x = 380 + k * 580
            fmid(c, s, x, 470 + dy, 58, "black", GREEN, a)
            text(c, why, x, 560 + dy, 28, "black", INK2, a)
            pill(c, "RACIONAL", x, 650 + dy, GREEN, size=24, a=a, anchor="center")
        return
    tag(c, "quadrado perfeito = inteiro × ele mesmo", W / 2, 230, BLUE, ep(t, C["33.t"], 0.5), 28)
    for k in range(20):
        n = k + 1
        x = 260 + (k % 10) * 155
        y = 360 + (k // 10) * 170
        a = ep(t, C["33.a"] + 0.12 * k, 0.3)
        fmid(c, str(n * n), x, y, 50, "black", INK, a)
        text(c, f"{n}×{n}", x, y + 56, 22, "bold", INK2, a)
    text(c, "sua lista de RAÍZES EXATAS", W / 2, 690, 34, "black", GREEN, ep(t, C["33.b"], 0.5))
    regra(c, "raiz de quadrado perfeito → RACIONAL", W / 2, 790, ep(t, C["33.c"], 0.5), 32, PURPLE)


# ======================================================================
# recapitulação
# ======================================================================

FRASES = ["ℕ ⊂ ℤ ⊂ ℚ ⊂ ℝ;  𝕀 fica ao lado de ℚ",
          "Acaba ou repete: racional. Nem/nem: irracional",
          "Raiz de quadrado perfeito é racional"]


def b_recap(c, t, C, B):
    sid = "34" if B["start"] < C["48"] - 1 else "48"
    head(c, t, B["start"], "AS 3 FRASES", "PARA GUARDAR", GREEN)
    card(c, *CARD_R)
    for k, (cue, col) in enumerate((("a", CQ), ("b", PURPLE), ("c", GREEN))):
        a, d = rise(t, C[f"{sid}.{cue}"])
        y = 330 + k * 160 + d
        badge_num(c, k + 1, 250, y - 16, a, 32, bg=col)
        ftext(c, FRASES[k], 310, y, 50, "black", INK, a, align="left")


# ======================================================================
# truque de ordenar
# ======================================================================

def b_ordenar(c, t, C, B):
    head(c, t, B["start"], "TRUQUE DE PROVA", "PASSE TUDO PARA DECIMAL", GREEN)
    card(c, *CARD_R)
    if t < C["36"] - 0.2:
        tag(c, "raiz, fração e decimal misturados? → DECIMAL", W / 2, 240, GREEN, ep(t, C["35.a"], 0.5), 30)
        vals = [("√2", "1,41"), ("√3", "1,73"), ("√5", "2,24"), ("π", "3,14")]
        for k, (s, v) in enumerate(vals):
            a, dy = rise(t, WT(C, "35", ["dois", "tres", "cinco", "pi"][k], 1, C["35.b"]) - 0.2)
            x = 330 + k * 420
            card(c, x - 160, 360 + dy, 320, 280, a)
            fmid(c, s, x, 450 + dy, 70, "black", CI, a)
            fmid(c, "≈ " + v, x, 570 + dy, 56, "black", INK, a)
        text(c, "guarde estes quatro", W / 2, 760, 32, "black", GREEN, ep(t, C["35.b"], 0.5))
        return
    a0 = ep(t, C["36.t"], 0.5)
    fmid(c, "√3     1,7     7/4", W / 2, 280, 66, "black", INK, a0)
    ra = ep(t, C["36.a"], 0.4)
    rb = ep(t, C["36.b"], 0.4)
    # reta com os três valores
    r = Reta(360, 1560, 560, 1.6, 1.8)
    x0, x1 = 360, 1560
    arrow(c, x0 - 20, 560, x1 + 30, 560, INK2, a0, 5, 14)
    for v in (1.6, 1.65, 1.7, 1.75, 1.8):
        x = r.X(v)
        line(c, x, 548, x, 572, INK2, a0, 3)
        text(c, f"{v:.2f}".replace(".", ","), x, 610, 24, "bold", INK2, a0)
    for v, s, a, col in ((1.7, "1,7", ep(t, C["36.t"] + 1.0, 0.4), INK), (math.sqrt(3), "√3 ≈ 1,73", ra, CI), (1.75, "7/4 = 1,75", rb, CQ)):
        x = r.X(v)
        c.drawCircle(x, 560, 12, paint(col, a))
        fmid(c, s, x, 470 - (40 if s.startswith("7") else 0), 34, "black", col, a)
    fbox(c, "1,7  <  √3  <  7/4", W / 2, 740, 56, ep(t, C["36.c"], 0.5), GREEN)


# ======================================================================
# erros e exercício
# ======================================================================

def b_erro1(c, t, C, B):
    head(c, t, B["start"], "ERRO 1", "DÍZIMA PERIÓDICA = IRRACIONAL?", RED)
    erro_tiles(c, t, [(C["37.a"], "O ERRO", ["!0,333… é irracional"], RED),
                      (C["37.b"], "POR QUE PARECE CERTO", ["ela também", "nunca termina"], AMBER),
                      (C["37.c"], "A CORREÇÃO", ["ela REPETE:", "repetiu, tem fração", "!RACIONAL"], GREEN)])


def b_erro2(c, t, C, B):
    head(c, t, B["start"], "ERRO 2", "TODA RAIZ É IRRACIONAL?", RED)
    erro_tiles(c, t, [(C["38.a"], "O ERRO", ["!√9 é irracional"], RED),
                      (C["38.b"], "POR QUE PARECE CERTO", ["os irracionais", "famosos são raízes"], AMBER),
                      (C["38.c"], "A CORREÇÃO", ["quadrado perfeito", "dá raiz exata", "!√9 = 3"], GREEN)])


def b_erro3(c, t, C, B):
    head(c, t, B["start"], "ERRO 3", "22/7 É O π?", RED)
    erro_tiles(c, t, [(C["39.a"], "O ERRO", ["!22/7 é irracional"], RED),
                      (C["39.b"], "POR QUE PARECE CERTO", ["muita gente usa", "22/7 no lugar do π"], AMBER),
                      (C["39.c"], "A CORREÇÃO", ["é só aproximação", "e é FRAÇÃO", "!RACIONAL"], GREEN)])


def b_exercicio(c, t, C, B):
    head(c, t, B["start"], "SUA VEZ", "PAUSE E CLASSIFIQUE", GREEN)
    itens = [("40.a", "0,75", "41.a", "acaba", True), ("40.b", "√16", "41.b", "= 4", True),
             ("40.c", "√7", "41.c", "nem acaba nem repete", False), ("40.d", "0,444…", "41.d", "repete", True)]
    for k, (cue, s, rc, why, rac) in enumerate(itens):
        a, dy = rise(t, C[cue])
        if a <= 0:
            continue
        x = 180 + k * 400
        card(c, x, 220 + dy, 360, 460, a)
        fmid(c, s, x + 180, 360 + dy, 64, "black", INK, a)
        ar = ep(t, C[rc], 0.4)
        text(c, why, x + 180, 490 + dy, 26, "black", INK2, ar)
        pill(c, "RACIONAL" if rac else "IRRACIONAL", x + 180, 590 + dy, GREEN if rac else RED, size=26, a=ar, anchor="center")
    pause_badge(c, W / 2 - 230, 740, ep(t, C["40.p"], 0.5) * (1 - prog(t, C["41.t"] - 0.3, 0.4)), "PAUSE E CLASSIFIQUE")


# ======================================================================
# questão 6
# ======================================================================

NUMS = [("√9", "= 3", True, "n1"), ("√10", "≈ 3,162…", False, "n2"), ("1,2323…", "repete", True, "n3"),
        ("π", "3,14159…", False, "n4"), ("22/7", "fração", True, "n5"), ("√(16/25)", "= 4/5", True, "n6")]
ALTS = [("A", "1", "46.a", "só o π"), ("B", "2", None, ""), ("C", "3", "46.c", "+ 22/7 (pegadinha)"),
        ("D", "4", "47.d", "+ a dízima"), ("E", "5", "47.e", "toda raiz + dízima")]


def b_questao(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO ESTILO ENEM", "QUANTOS SÃO IRRACIONAIS?", BLUE)
    card(c, 140, 180, 1000, 640)
    pill(c, "QUESTÃO", 170, 224, BLUE, size=22, bounds=(0, 1920))
    a1 = ep(t, C["42.e1"], 0.5)
    text(c, "Considere os números:", 180, 300, 30, "black", INK2, a1, align="left")
    sid_of = {"n1": "44", "n2": "44", "n3": "45", "n4": "45", "n5": "45", "n6": "45"}
    for k, (s, why, rac, cue) in enumerate(NUMS):
        x = 300 + (k % 3) * 300
        y = 400 + (k // 3) * 190
        ak = a1 * ep(t, WT(C, "42", ["nove", "dez", "dois", "pi", "vinte", "dezesseis"][k], 1, C["42.e1"]) - 0.1, 0.4)
        ar = ep(t, C[f"{sid_of[cue]}.{cue}"] + 0.6, 0.4)
        col = mix(INK, GREEN if rac else RED, ar)
        fmid(c, s, x, y, 52, "black", col, ak)
        if ar > 0:
            text(c, why, x, y + 60, 24, "black", INK2, ar)
            pill(c, "RACIONAL" if rac else "IRRACIONAL", x, y + 100, GREEN if rac else RED, size=20, a=ar, anchor="center")
    text(c, "Quantos deles são irracionais?", 180, 790, 30, "black", INK, ep(t, C["42.e2"], 0.5), align="left")
    # alternativas
    card(c, 1180, 180, 600, 640, ep(t, C["43.t"], 0.5))
    aok = ep(t, C["46.r"], 0.5)
    for k, (L, s, cue_x, why) in enumerate(ALTS):
        a, d = rise(t, C[f"43.{L.lower()}"])
        y = 300 + k * 100 + d
        ok = cue_x is None
        if ok and aok > 0:
            rrect(c, 1205, y - 44, 550, 70, 14, GREEN, 0.15 * aok)
        badge_num(c, L, 1245, y - 12, a, 24, bg=GREEN if ok and aok > 0.5 else INK)
        ax = ep(t, C[cue_x], 0.4) if cue_x else 0
        text(c, s, 1290, y, 40, "black", INK, a * (1 - 0.55 * ax), align="left")
        if ax > 0:
            strike(c, 1286, y - 14, 1290 + text_w(s, "black", 40) + 6, y - 14, ax, RED, ax)
            ftext(c, why, 1350, y - 4, 26, "black", RED, ax, align="left")
    pause_badge(c, 1290, 740, ep(t, C["43.p"], 0.5) * (1 - prog(t, C["44.t"] - 0.3, 0.4)))
    pill(c, "RESPOSTA: B · √10 e π", 1480, 770, GREEN, size=28, a=ep(t, C["46.r"], 0.5), anchor="center", bounds=(0, 1920))


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    head(c, t, B["start"], "PRÓXIMO EPISÓDIO", "INTERVALOS REAIS", PURPLE)
    card(c, *CARD_R)
    a0 = ep(t, C["49.t"], 0.5)
    r = Reta(300, 1620, 420, 0, 7)
    r.draw(c, a0)
    text(c, "a reta real: sem buracos", W / 2, 300, 36, "black", INK, a0)
    aa = ep(t, C["49.a"], 0.5)
    if aa > 0:
        x2, x5 = r.X(2), r.X(5)
        rrect(c, x2, 405, (x5 - x2) * ease_io(prog(t, C["49.a"], 0.9)), 30, 15, PURPLE, aa * 0.8)
        c.drawCircle(x2, 420, 16, paint(PURPLE, aa)); c.drawCircle(x5, 420, 16, paint(PURPLE, aa))
        text(c, "só um pedaço: de 2 até 5", W / 2, 580, 36, "black", PURPLE, aa)
    pill(c, "EPISÓDIO 3: INTERVALOS REAIS", W / 2, 720, PURPLE, size=32, a=ep(t, C["49.b"], 0.5), anchor="center")


def b_cta(c, t, C, B):
    cta(c, t, C["50.like"], C["50.sub"], C["50.bell"], C["50.com"], C["50.bye"], "Você já tinha caído na pegadinha do 22/7?")


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, conjunto=b_conjunto, historia=b_historia,
              naturais=b_naturais, inteiros=b_inteiros, racionais=b_racionais, irracionais=b_irracionais, reais=b_reais,
              cadeia=b_cadeia, notacoes=b_notacoes, criterio=b_criterio, famosos=b_famosos, raiz_exata=b_raiz_exata,
              recap=b_recap, ordenar=b_ordenar, erro1=b_erro1, erro2=b_erro2, erro3=b_erro3, exercicio=b_exercicio,
              questao=b_questao, ponte=b_ponte, cta=b_cta)
