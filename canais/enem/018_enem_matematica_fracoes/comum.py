"""Peças COMUNS da série Frações, Decimais e Dízimas (018). Cada epN/roteiro/visual.py faz:

    import importlib.util; from pathlib import Path
    _p = Path(__file__).resolve().parents[2] / "comum.py"
    _s = importlib.util.spec_from_file_location("comum018", _p); K = importlib.util.module_from_spec(_s); _s.loader.exec_module(K)
    K.usar_tempos(Path(__file__).resolve().parents[1] / "audio" / "tempos.json")
    from comum018-names...  (ou use K.pizza, K.expr etc.)

Peças (todas com alfa `a`):
- WT(C, sid, palavra, k=1, depois=None)  instante em que a palavra é dita (tempos do episódio, ver usar_tempos)
- ftext/fmid/fbox          texto com expoente (^2, ^{-2}) e fonte reserva para símbolos (≈ ≠ ÷ ≤ …)
- fr(c, num, den, cx, cy, size, ...)     fração empilhada (num em cima, traço, den embaixo); devolve a largura
- expr(c, "1/2 + 1/3 = 5/6", cx, cy, size, a, cores={i: cor}, align)  linha matemática: tokens separados por espaço;
      "a/b" vira fração empilhada; "2|3/4" vira número misto; "·", "÷", "=", "+", "−", "→", ">", "<" ficam como texto.
      cores: índice do token → cor (os demais em INK). Devolve a largura total. expr_w() só mede.
- pizza(c, cx, cy, r, n, sel, a, ...)    pizza cortada em n fatias; sel = quantas (int) ou quais (set) ficam coloridas;
      pull = afasta as fatias escolhidas; cut = 0..1 desenha os cortes aos poucos; rot = giro inicial (graus).
- barra(c, x, y, w, h, cols, rows, sel, a, ...)  barra de chocolate em quadradinhos (sel = índices ou nº de colunas).
- reta(c, x0, x1, y, a, marcas=[(valor 0..1, rótulo, cor)])  reta de 0 a 1 com a metade marcada.
- frame/head_seq/which/para/wrap/boxed/regra/selo/pause_timer/chip/erro_cards/alternativas · utilidades de cena.
Cores com função: azul = definição · roxo = regra/fórmula · âmbar = armadilha · verde = atalho/dica · vermelho = erro.
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

CARD_R = (140, 150, 1640, 690)
SYM = "C:/Windows/Fonts/seguisym.ttf"
MASSA = "#F3D9A4"      # massa da pizza
BORDA = "#D9A55B"      # borda assada
QUEIJO = "#FFE9A8"
MOLHO = "#E8743B"      # fatia escolhida (padrão)
CHOCO = "#7B4A2A"
CHOCO_ESC = "#5A341C"
CHOCO_SEL = "#E8A317"

# ======================================================================
# tempos das palavras
# ======================================================================

_TEMPOS = {"p": None}


def usar_tempos(path):
    _TEMPOS["p"] = str(path)
    _words.cache_clear()


def _n(s):
    s = unicodedata.normalize("NFD", s.lower())
    return re.sub(r"[^a-z0-9]", "", "".join(ch for ch in s if unicodedata.category(ch) != "Mn"))


@lru_cache(None)
def _words():
    p = Path(_TEMPOS["p"] or "")
    if not _TEMPOS["p"] or not p.exists():
        return {}
    d = json.loads(p.read_text(encoding="utf-8"))
    return {s["id"]: [(_n(w["disp"]), w["t0"]) for w in s.get("tokens", [])] for s in d["scenes"]}


def WT(C, sid, palavra, k=1, depois=None):
    """instante absoluto da k-ésima ocorrência da palavra na cena (depois = só a partir desse instante)"""
    ws = [(w, C[sid] + t0) for w, t0 in _words().get(sid, []) if w == _n(palavra)]
    if depois is not None:
        ws = [x for x in ws if x[1] >= depois - 0.05]
    if not ws:
        return (depois if depois is not None else C[sid]) + 1.0
    return ws[min(k - 1, len(ws) - 1) if k > 0 else k][1]


# ======================================================================
# texto matemático
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
        if s[i] == "^" and i + 1 < len(s):
            if buf:
                out.append((buf, None)); buf = ""
            if s[i + 1] == "{":
                j = s.index("}", i)
                out.append((s[i + 2:j], "^")); i = j + 1
            else:
                out.append((s[i + 1], "^")); i += 2
        else:
            buf += s[i]; i += 1
    if buf:
        out.append((buf, None))
    return out


def _pieces(s, peso, size):
    for txt, mode in _runs(s):
        sz = size * 0.6 if mode else size
        dy = -size * 0.42 if mode else 0
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


# ---------------- frações empilhadas ----------------

def fr_w(num, den, size, peso="black"):
    return max(ftext_w(str(num), peso, size), ftext_w(str(den), peso, size)) + size * 0.35


def fr(c, num, den, cx, cy, size, color=None, a=1.0, peso="black", num_col=None, den_col=None, bar_col=None):
    """fração empilhada centrada em (cx, cy = altura do traço); size = tamanho dos algarismos. Devolve a largura."""
    if a <= 0:
        return fr_w(num, den, size, peso)
    color = INK if color is None else color
    w = fr_w(num, den, size, peso)
    ftext(c, str(num), cx, cy - size * 0.16, size, peso, num_col or color, a)
    line(c, cx - w / 2, cy + size * 0.06, cx + w / 2, cy + size * 0.06, bar_col or color, a, max(3, size * 0.075), cap_round=True)
    ftext(c, str(den), cx, cy + size * 0.98, size, peso, den_col or color, a)
    return w


_FR = re.compile(r"^(-?\d+)\|(\d+)/(\d+)$|^([^/\s()]+)/([^/\s()]+)$")
_POT = re.compile(r"^\(([^/\s]+)/([^/\s]+)\)\^(\{[^}]+\}|\S+)$")


def _pot_parts(tok):
    m = _POT.match(tok)
    if not m:
        return None
    e = m.group(3)
    return m.group(1), m.group(2), e[1:-1] if e.startswith("{") else e


def _tok_w(tok, size, peso):
    p = _pot_parts(tok)
    if p:
        par = ftext_w("(", peso, size * 1.5)
        return 2 * par + fr_w(p[0], p[1], size * 0.8, peso) + ftext_w(p[2], peso, size * 0.6) + 8
    m = _FR.match(tok)
    if m and m.group(1):
        return ftext_w(m.group(1), peso, size * 1.15) + 6 + fr_w(m.group(2), m.group(3), size * 0.8, peso)
    if m:
        return fr_w(m.group(4), m.group(5), size * 0.8, peso)
    return ftext_w(tok, peso, size)


def expr_w(s, size, peso="black", gap=None):
    toks = s.split()
    gap = size * 0.32 if gap is None else gap
    return sum(_tok_w(t, size, peso) for t in toks) + gap * max(0, len(toks) - 1)


def expr(c, s, cx, cy, size, a=1.0, cores=None, align="center", peso="black", gap=None, alfas=None):
    """linha matemática centrada verticalmente em cy. Tokens separados por espaço:
    "3/4" → fração empilhada · "2|3/4" → misto · resto → texto. cores/alfas: {índice do token: valor}."""
    if a <= 0:
        return expr_w(s, size, peso, gap)
    toks = s.split()
    gap = size * 0.32 if gap is None else gap
    total = expr_w(s, size, peso, gap)
    x = cx - total / 2 if align == "center" else (cx - total if align == "right" else cx)
    for i, tok in enumerate(toks):
        col = (cores or {}).get(i, INK)
        ai = a * (alfas or {}).get(i, 1.0)
        w = _tok_w(tok, size, peso)
        m = _FR.match(tok)
        p = _pot_parts(tok)
        if p:
            par = ftext_w("(", peso, size * 1.5)
            fw_ = fr_w(p[0], p[1], size * 0.8, peso)
            fmid(c, "(", x + par / 2, cy - size * 0.05, size * 1.5, "bold", col, ai)
            fr(c, p[0], p[1], x + par + fw_ / 2, cy - size * 0.38, size * 0.8, col, ai, peso)
            fmid(c, ")", x + par * 1.5 + fw_, cy - size * 0.05, size * 1.5, "bold", col, ai)
            ftext(c, p[2], x + 2 * par + fw_ + 4, cy - size * 0.62, size * 0.6, peso, col, ai, align="left")
        elif m and m.group(1):
            wi = ftext_w(m.group(1), peso, size * 1.15)
            fmid(c, m.group(1), x + wi / 2, cy, size * 1.15, peso, col, ai)
            fr(c, m.group(2), m.group(3), x + wi + 6 + fr_w(m.group(2), m.group(3), size * 0.8, peso) / 2, cy - size * 0.38,
               size * 0.8, col, ai, peso)
        elif m:
            fr(c, m.group(4), m.group(5), x + w / 2, cy - size * 0.38, size * 0.8, col, ai, peso)
        else:
            fmid(c, tok, x + w / 2, cy, size, peso, col, ai)
        x += w + gap
    return total


# ======================================================================
# pizza, barra de chocolate, reta
# ======================================================================

def _wedge(cx, cy, r, a0, a1):
    p = skia.Path()
    p.moveTo(cx, cy)
    p.arcTo(skia.Rect.MakeLTRB(cx - r, cy - r, cx + r, cy + r), a0, a1 - a0, False)
    p.close()
    return p


def pizza(c, cx, cy, r, n, sel=0, a=1.0, sel_col=None, pull=0.0, cut=1.0, rot=-90.0, gone=None, label=None,
          contorno=None, sombra=True):
    """pizza em n fatias (todas do mesmo tamanho). sel = nº de fatias escolhidas (a partir do topo, no sentido horário)
    ou um set de índices; pull = quanto as escolhidas saem para fora (0..1); cut = progresso dos cortes;
    gone = set de fatias que sumiram (comidas: ficam só o contorno tracejado)."""
    if a <= 0:
        return
    sel_col = MOLHO if sel_col is None else sel_col
    escolhidas = set(range(sel)) if isinstance(sel, int) else set(sel)
    gone = gone or set()
    if sombra:
        c.drawCircle(cx, cy + r * 0.06, r * 1.02, blur_paint_(INK, 0.12 * a, r * 0.08))
    step = 360.0 / max(1, n)
    for i in range(n):
        a0 = rot + i * step
        mid = math.radians(a0 + step / 2)
        k = (pull * r * 0.10) if i in escolhidas else 0
        ox, oy = math.cos(mid) * k, math.sin(mid) * k
        if i in gone:
            p = _wedge(cx + ox, cy + oy, r, a0, a0 + step)
            pe = paint(LIGHT, a, stroke=3)
            pe.setPathEffect(skia.DashPathEffect.Make([12, 9], 0))
            c.drawPath(p, pe)
            continue
        c.drawPath(_wedge(cx + ox, cy + oy, r, a0, a0 + step), paint(BORDA, a))
        c.drawPath(_wedge(cx + ox, cy + oy, r * 0.88, a0, a0 + step), paint(sel_col if i in escolhidas else QUEIJO, a))
        if i in escolhidas and sel_col == MOLHO:   # "pepperoni" para dar textura
            for j in range(2):
                ang = math.radians(a0 + step * (0.35 + 0.3 * j))
                rr = r * (0.42 + 0.22 * j)
                c.drawCircle(cx + ox + math.cos(ang) * rr, cy + oy + math.sin(ang) * rr, r * 0.06, paint("#B23A2A", a * 0.9))
    # cortes
    if n > 1 and cut > 0:
        for i in range(n):
            ang = math.radians(rot + i * step)
            u = clamp(cut * n - i * 0.6) if cut < 1 else 1
            if u <= 0:
                continue
            c.drawLine(cx, cy, cx + math.cos(ang) * r * u, cy + math.sin(ang) * r * u, paint("#8A5A2B", a * (1 - 0.85 * clamp(pull)), stroke=max(3, r * 0.025)))
    if contorno:
        c.drawCircle(cx, cy, r + 8, paint(contorno, a, stroke=5))
    if label:
        text(c, label, cx, cy + r + 56, 34, "black", INK2, a)


def blur_paint_(col, a, sigma):
    p = paint(col, a)
    p.setMaskFilter(skia.MaskFilter.MakeBlur(skia.kNormal_BlurStyle, max(0.5, sigma)))
    return p


def barra(c, x, y, w, h, cols, rows, sel=None, a=1.0, sel_col=None, sel2=None, sel2_col=None, gap=6, label=None):
    """barra de chocolate cols × rows. sel/sel2 = conjunto de índices (linha*cols + coluna) destacados."""
    if a <= 0:
        return
    sel = set(sel or ()); sel2 = set(sel2 or ())
    sel_col = CHOCO_SEL if sel_col is None else sel_col
    sel2_col = RED if sel2_col is None else sel2_col
    rrect(c, x - 10, y - 10, w + 20, h + 20, 16, CHOCO_ESC, a, shadow=True)
    cw, ch = (w - gap * (cols - 1)) / cols, (h - gap * (rows - 1)) / rows
    for r_ in range(rows):
        for k in range(cols):
            i = r_ * cols + k
            col = sel2_col if i in sel2 else sel_col if i in sel else CHOCO
            xx, yy = x + k * (cw + gap), y + r_ * (ch + gap)
            rrect(c, xx, yy, cw, ch, 8, col, a)
            rrect(c, xx + 6, yy + 6, cw - 12, ch * 0.28, 6, "#FFFFFF", a * 0.10)
    if label:
        text(c, label, x + w / 2, y + h + 60, 32, "black", INK2, a)


def reta(c, x0, x1, y, a=1.0, marcas=(), meio=True, rotulos=True):
    """reta de 0 a 1; marcas = [(valor, rótulo, cor, alfa)] (rótulo 'a/b' vira fração empilhada)"""
    if a <= 0:
        return
    line(c, x0, y, x1, y, INK2, a, 5)
    for v, lab in ((0, "0"), (1, "1")):
        x = lerp(x0, x1, v)
        line(c, x, y - 20, x, y + 20, INK2, a, 5)
        if rotulos:
            text(c, lab, x, y + 66, 38, "black", INK2, a)
    if meio:
        xm = lerp(x0, x1, 0.5)
        line(c, xm, y - 26, xm, y + 26, PURPLE, a, 5)
        if rotulos:
            fr(c, 1, 2, xm, y + 74, 28, PURPLE, a)
    for m in marcas:
        v, lab, col = m[0], m[1], m[2]
        am = a * (m[3] if len(m) > 3 else 1)
        if am <= 0:
            continue
        x = lerp(x0, x1, v)
        c.drawCircle(x, y, 14, paint(col, am))
        if lab:
            if "/" in lab:
                n_, d_ = lab.split("/")
                fr(c, n_, d_, x, y - 92, 34, col, am)
            else:
                text(c, lab, x, y - 40, 34, "black", col, am)


# ======================================================================
# utilidades de cena
# ======================================================================

def wrap(s, peso, size, maxw):
    out, cur = [], ""
    for w in s.split():
        tst = (cur + " " + w).strip()
        if cur and text_w(tst, peso, size) > maxw:
            out.append(cur); cur = w
        else:
            cur = tst
    if cur:
        out.append(cur)
    return out


def para(c, s, x, y, size, peso, color, a, maxw, lh=None, align="left"):
    lh = lh or size * 1.32
    lines = wrap(s, peso, size, maxw)
    if a > 0:
        for k, ln in enumerate(lines):
            text(c, ln, x, y + k * lh, size, peso, color, a, align=align)
    return len(lines) * lh


def which(t, C, ids):
    cur = ids[0]
    for i in ids:
        if t >= C[i] - 0.05:
            cur = i
    return cur


def frame(c, t, t0, l1, l2, col):
    head(c, t, t0, l1, l2, col)
    card(c, *CARD_R)


def head_seq(c, t, C, heads):
    sid = which(t, C, [h[0] for h in heads])
    for h in heads:
        if h[0] == sid:
            head(c, t, C[sid], h[1], h[2], h[3])


def boxed(c, x, y, w, h, col, a, fill=0.10, r=22, sw=4):
    if a <= 0:
        return
    rrect(c, x, y, w, h, r, col, fill * a)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), r, r), paint(col, a, stroke=sw))


def regra(c, s, cx, cy, a, size=36, col=None):
    """faixa de regra (roxo por padrão); aceita texto com frações via expr se tiver '/' isolado"""
    col = PURPLE if col is None else col
    if a <= 0:
        return
    w = ftext_w(s, "black", size) + 90
    boxed(c, cx - w / 2, cy - 46, w, 92, col, a, 0.10)
    fmid(c, s, cx, cy, size, "black", col, a)


def selo(c, x, y, a, s, col=None, rot=-6, size=32):
    if a <= 0:
        return
    col = col or AMBER
    c.save(); c.translate(x, y); c.rotate(rot)
    w = text_w(s, "black", size) + 50
    sc = 0.8 + 0.2 * ease_back(clamp(a))
    c.scale(sc, sc)
    boxed(c, -w / 2, -32, w, 64, col, a, 0.15, 12, 5)
    text_mid(c, s, 0, 0, size, "black", col, a)
    c.restore()


def pause_timer(c, t, t0, x, y, a=1.0, dur=1.6, r=44):
    u = clamp((t - t0) / dur)
    ap = a * ep(t, t0, 0.3) * (1 - prog(t, t0 + dur + 0.4, 0.4))
    if ap <= 0:
        return
    c.drawCircle(x, y, r + 14, paint(AMBER, ap * 0.18))
    c.drawCircle(x, y, r, paint("#FFFFFF", ap))
    c.drawArc(skia.Rect.MakeLTRB(x - r, y - r, x + r, y + r), -90, 360 * (1 - u), False, paint(AMBER, ap, stroke=10, cap_round=True))
    c.drawRect(skia.Rect.MakeXYWH(x - 15, y - 20, 10, 40), paint(INK, ap)); c.drawRect(skia.Rect.MakeXYWH(x + 5, y - 20, 10, 40), paint(INK, ap))
    text(c, "PAUSE", x, y + r + 40, 26, "black", AMBER, ap)


def chip(c, s, cx, cy, col, a, size=40, fill=True, w=None):
    if a <= 0:
        return
    w = w or max(size * 1.5, text_w(s, "black", size) + size * 0.7)
    h = size * 1.5
    rrect(c, cx - w / 2, cy - h / 2, w, h, size * 0.3, mix("#FFFFFF", col, 0.16) if fill else "#FFFFFF", a)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2, cy - h / 2, w, h), size * 0.3, size * 0.3), paint(col, a, stroke=3))
    text_mid(c, s, cx, cy, size, "black", col, a)


def erro_cards(c, t, C, ids, items, total=None):
    """os erros clássicos: items = [(errado, parece_certo_porque, correção)], um por cena (ids). Cues a, b, c em cada cena.
    Textos podem trazer frações como 'a/b' isoladas (vão como texto); para frações empilhadas use cenas próprias."""
    total = total or len(items)
    sid = which(t, C, ids)
    n = ids.index(sid)
    err, parece, fix = items[n]
    head(c, t, C[sid], f"ERRO {n + 1} DE {total}", "OS ERROS CLÁSSICOS", RED)
    card(c, *CARD_R)
    for k in range(total):
        badge_num(c, k + 1, W / 2 - (total - 1) * 40 + k * 80, 210, 1, 22, bg=RED if k == n else LIGHT)
    q = lambda x: C[f"{sid}.{x}"]
    aa = ep(t, q("a"), 0.5)
    check_icon(c, 300, 330, 34, aa, RED, "x")
    para(c, err, 360, 345, 44, "black", RED, aa, 1300)
    ab = ep(t, q("b"), 0.5)
    pill(c, "PARECE CERTO PORQUE...", 300, 490, AMBER, size=26, a=ab, bounds=(0, 1920))
    para(c, parece, 300, 570, 36, "bold", INK2, ab, 1340)
    ac = ep(t, q("c"), 0.5)
    check_icon(c, 300, 700, 34, ac, GREEN)
    para(c, fix, 360, 714, 38, "black", GREEN, ac, 1300)


def alternativas(c, t, C, alts, x, y0, w, size, ok_cue, okL, cues_in, cues_x=None, gap=18):
    """lista A–E. alts = [(letra, texto_ou_expr, motivo_do_erro, cor_do_motivo)]; texto que começa com '=' é desenhado com
    expr (frações empilhadas). cues_in = {letra: instante de entrada}; cues_x = {letra: instante do risco}."""
    aok = ep(t, ok_cue, 0.5)
    y = y0
    for L, s, why, col in alts:
        a, d = rise(t, cues_in.get(L, 1e9))
        ok = L == okL
        is_expr = s.startswith("=")
        if is_expr:
            hh = size * 2.4
        else:
            lines = wrap(s, "bold", size, w - 70)
            hh = len(lines) * (size + 8) + 10
        ax = ep(t, (cues_x or {}).get(L, 1e9), 0.4) if not ok else 0
        if a > 0:
            if ok and aok > 0:
                rrect(c, x - 20, y - 10 + d, w + 30, hh + (30 if ax else 6), 14, GREEN, 0.15 * aok)
            badge_num(c, L, x + 10, y + hh / 2 - 6 + d, a, 22, bg=GREEN if ok and aok > 0.5 else INK)
            if is_expr:
                expr(c, s[1:].strip(), x + 50, y + hh / 2 + d, size * 1.15, a * (1 - 0.5 * ax), align="left")
                if ax > 0:
                    ww = expr_w(s[1:].strip(), size * 1.15)
                    strike(c, x + 46, y + hh / 2 + d, x + 54 + ww, y + hh / 2 + d, ax, RED, ax)
            else:
                for j, ln in enumerate(lines):
                    yy = y + d + size + j * (size + 8)
                    text(c, ln, x + 50, yy, size, "bold", INK, a * (1 - 0.5 * ax), align="left")
                    if ax > 0:
                        strike(c, x + 46, yy - size * 0.35, x + 54 + text_w(ln, "bold", size), yy - size * 0.35, ax, RED, ax)
            if ax > 0 and why:
                pill(c, why, x + w, y + hh / 2 + d, col or RED, size=20, a=ax, anchor="right", bounds=(0, 1920))
        y += hh + gap
    return y
