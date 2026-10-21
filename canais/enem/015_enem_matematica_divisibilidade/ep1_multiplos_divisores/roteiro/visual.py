"""Visual — Divisibilidade, Primos, MMC e MDC, Episódio 1: Múltiplos, divisores e critérios (iniciantes, tema claro).
Cores com função: azul = definição · roxo = regra/fórmula · âmbar = armadilha · verde = atalho/dica · vermelho = erro.

Peças REAPROVEITÁVEIS pelos próximos episódios da série (importe este arquivo como V1):
- grade(c, cx, cy, n, cols, cell, a, ...)  · n quadradinhos em fileiras de `cols` (sobra em vermelho), com os lados nas bordas.
- grade_morph(c, t, keys, cx, cy, n, cell)   · os mesmos n quadradinhos deslizando entre retângulos [(instante, colunas)].
- balas(c, ...) / criancas(...)              · balas repartidas entre crianças, com o resto em vermelho.
- escada(c, ...)                            · escada de degraus com os pisados de k em k acesos (múltiplos).
- soma_algarismos(c, t, t0, numero, ...)     · os algarismos "pulam" do número para uma soma ao lado.
- ftext/fmid/fbox                           · texto com expoente (^) e fonte reserva para símbolos.
- frame/head_seq/which/para/boxed/selo/pause_timer/regra/erro_cards · utilidades de cena.
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
ARQUIVO_FINAL = "enem_matematica_divisibilidade_ep1_multiplos_divisores.mp4"
CARD_R = (140, 150, 1640, 690)
SYM = "C:/Windows/Fonts/seguisym.ttf"
CANDY = ["#E5484D", "#3B6CF6", "#16A36A", "#E8A317", "#7C5CFA", "#F97316"]
SQ = "#5B8DEF"          # quadradinho padrão
SQ_EDGE = "#2F5FD0"


# ======================================================================
# tempos das palavras
# ======================================================================

def _n(s):
    s = unicodedata.normalize("NFD", s.lower())
    return re.sub(r"[^a-z0-9]", "", "".join(ch for ch in s if unicodedata.category(ch) != "Mn"))


TEMPOS = Path(__file__).resolve().parents[1] / "audio" / "tempos.json"


@lru_cache(None)
def _words(path=str(TEMPOS)):
    p = Path(path)
    if not p.exists():
        return {}
    d = json.loads(p.read_text(encoding="utf-8"))
    return {s["id"]: [(_n(w["disp"]), w["t0"]) for w in s.get("tokens", [])] for s in d["scenes"]}


def WT(C, sid, palavra, k=1, depois=None, path=str(TEMPOS)):
    """instante (absoluto) da k-ésima ocorrência da palavra na cena; depois = só a partir desse instante"""
    ws = [(w, C[sid] + t0) for w, t0 in _words(path).get(sid, []) if w == _n(palavra)]
    if depois is not None:
        ws = [x for x in ws if x[1] >= depois - 0.05]
    if not ws:
        return (depois if depois is not None else C[sid]) + 1.0
    return ws[k - 1 if k > 0 else k][1]


# ======================================================================
# texto matemático (expoente ^x e fonte reserva)
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
    """faixa de regra (roxo por padrão)"""
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
    """quadradinho com um algarismo/símbolo (para dígitos e listas)"""
    if a <= 0:
        return
    w = w or max(size * 1.5, text_w(s, "black", size) + size * 0.7)
    h = size * 1.5
    rrect(c, cx - w / 2, cy - h / 2, w, h, size * 0.3, mix("#FFFFFF", col, 0.16) if fill else "#FFFFFF", a)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2, cy - h / 2, w, h), size * 0.3, size * 0.3), paint(col, a, stroke=3))
    text_mid(c, s, cx, cy, size, "black", col, a)


def erro_cards(c, t, C, ids, items, total=3):
    """os erros clássicos: [(errado, parece_certo_porque, correção)] um por cena (ids = cenas)"""
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


# ======================================================================
# peças da série: balas, crianças, escada, grade de quadradinhos, soma de algarismos
# ======================================================================

def crianca(c, cx, by, a, col=BLUE, s=1.0):
    """bonequinho simples; by = base (pés)"""
    if a <= 0:
        return
    c.drawCircle(cx, by - 92 * s, 22 * s, paint(col, a))
    rrect(c, cx - 30 * s, by - 64 * s, 60 * s, 64 * s, 22 * s, col, a)


def bala(c, x, y, col, a, r=14):
    if a <= 0:
        return
    for sx in (-1, 1):
        p = skia.Path()
        p.moveTo(x + sx * r * 0.8, y); p.lineTo(x + sx * r * 1.7, y - r * 0.6); p.lineTo(x + sx * r * 1.7, y + r * 0.6); p.close()
        c.drawPath(p, paint(mix(col, "#FFFFFF", 0.25), a))
    c.drawCircle(x, y, r, paint(col, a))
    c.drawCircle(x - r * 0.35, y - r * 0.35, r * 0.25, paint("#FFFFFF", a * 0.6))


def balas(c, t, n, kids, cx, top_y, kid_y, t_div, t_resto, a=1.0, spread=300, show_kids=True):
    """n balas: começam num monte (topo) e, a partir de t_div, vão para as crianças (kids por linha);
    as que sobram ficam no monte e ficam vermelhas em t_resto. Retorna (por_crianca, resto)."""
    if a <= 0:
        return n // kids, n % kids
    q, r = n // kids, n % kids
    xs = [cx + (k - (kids - 1) / 2) * spread for k in range(kids)]
    if show_kids:
        for k, x in enumerate(xs):
            crianca(c, x, kid_y, a, [BLUE, PURPLE, GREEN, AMBER, RED, INK2, BLUE][k % 7], 0.9)
    u_all = clamp((t - t_div) / 2.0)
    for i in range(n):
        col = CANDY[i % len(CANDY)]
        px = cx + ((i % 7) - 3) * 40
        py = top_y + (i // 7) * 40
        if i < q * kids:
            k, j = i % kids, i // kids
            tx = xs[k] + ((j % 2) - 0.5) * 40
            ty = kid_y - 150 - (j // 2) * 38
            u = ease_out(clamp(u_all * 1.4 - i / max(1, n) * 0.4))
            bala(c, lerp(px, tx, u), lerp(py, ty, u), col, a)
        else:
            ra = ep(t, t_resto, 0.4)
            bala(c, px, py, mix(col, RED, ra), a, 14 + 4 * ra)
    return q, r


def escada(c, t, x0, y0, n, passo, t0, a=1.0, dx=95, dy=36, label=True, dur=0.55):
    """n degraus subindo para a direita; a partir de t0 um pino pula de passo em passo; degraus pisados acendem"""
    if a <= 0:
        return
    for k in range(1, n + 1):
        x = x0 + (k - 1) * dx
        y = y0 - k * dy
        pis = k % passo == 0
        hops = int(max(0.0, (t - t0) / dur))
        lit = pis and k <= hops * passo
        rrect(c, x, y, dx, k * dy, 0, mix("#FFFFFF", GREEN, 0.35) if lit else "#ECEBE6", a)
        line(c, x, y, x + dx, y, GREEN if lit else LIGHT, a, 4)
        if label:
            text(c, str(k), x + dx / 2, y + 30, 22, "black", GREEN if lit else GRAY, a)
    hops_f = max(0.0, (t - t0) / dur)
    k_now = min(int(hops_f), n // passo)
    frac = hops_f - int(hops_f) if k_now < n // passo else 0
    k1 = k_now * passo
    k2 = min(n, k1 + passo)
    def pos(k):
        return (x0 + (k - 0.5) * dx if k > 0 else x0 - dx * 0.5, y0 - k * dy)
    p1, p2 = pos(k1), pos(k2)
    u = ease_out(frac)
    px, py = lerp(p1[0], p2[0], u), lerp(p1[1], p2[1], u) - math.sin(math.pi * frac) * 70
    if t >= t0 - 0.3:
        c.drawCircle(px, py - 26, 20, paint(BLUE, a))


def _cells(n, cols):
    return [(i % cols, i // cols) for i in range(n)]


def grade(c, cx, cy, n, cols, cell, a, col=SQ, gap=None, sobra_col=RED, lados=True, lado_col=PURPLE, lado_a=None):
    """n quadradinhos em fileiras de `cols`, centrados em (cx, cy). Fileira incompleta (sobra) em vermelho.
    Lados (colunas em cima, fileiras à esquerda) só quando o retângulo fecha."""
    if a <= 0:
        return
    gap = cell * 0.12 if gap is None else gap
    rows = math.ceil(n / cols)
    W_ = cols * cell + (cols - 1) * gap
    H_ = rows * cell + (rows - 1) * gap
    x0, y0 = cx - W_ / 2, cy - H_ / 2
    full = n % cols == 0
    for i, (ix, iy) in enumerate(_cells(n, cols)):
        sob = (not full) and iy == rows - 1
        cc = sobra_col if sob else col
        rrect(c, x0 + ix * (cell + gap), y0 + iy * (cell + gap), cell, cell, cell * 0.18, cc, a)
    if lados and full:
        la = a if lado_a is None else lado_a
        text(c, str(cols), cx, y0 - 22, 40, "black", lado_col, la)
        text(c, str(rows), x0 - 30, cy + 14, 40, "black", lado_col, la, align="right")


def grade_morph(c, t, keys, cx, cy, n, cell, a=1.0, dur=0.9, col=SQ, lados=True):
    """keys = [(instante, colunas), ...]: os n quadradinhos deslizam de um retângulo para o próximo"""
    if a <= 0:
        return
    k = 0
    for i, (tk, _) in enumerate(keys):
        if t >= tk:
            k = i
    cols_b = keys[k][1]
    cols_a = keys[k - 1][1] if k > 0 else cols_b
    u = ease_io(clamp((t - keys[k][0]) / dur)) if k > 0 else 1.0
    gap = cell * 0.12

    def layout(cols):
        rows = math.ceil(n / cols)
        W_ = cols * cell + (cols - 1) * gap
        H_ = rows * cell + (rows - 1) * gap
        x0, y0 = cx - W_ / 2, cy - H_ / 2
        return [(x0 + ix * (cell + gap), y0 + iy * (cell + gap)) for ix, iy in _cells(n, cols)], (W_, H_, rows)

    pa, _ = layout(cols_a)
    pb, (Wb, Hb, rows_b) = layout(cols_b)
    full = n % cols_b == 0
    for i in range(n):
        x = lerp(pa[i][0], pb[i][0], u)
        y = lerp(pa[i][1], pb[i][1], u)
        sob = (not full) and (i // cols_b) == rows_b - 1 and u > 0.9
        rrect(c, x, y, cell, cell, cell * 0.18, RED if sob else col, a)
    if lados and full and u > 0.85:
        la = a * clamp((u - 0.85) / 0.15)
        text(c, str(cols_b), cx, cy - Hb / 2 - 22, 40, "black", PURPLE, la)
        text(c, str(rows_b), cx - Wb / 2 - 30, cy + 14, 40, "black", PURPLE, la, align="right")


def numero(c, s, cx, cy, size, a, col=INK, hl=None, hl_col=GREEN, hl_a=1.0):
    """número grande com algarismos em caixas invisíveis; hl = índices destacados (retorna centros x)"""
    gapw = size * 0.08
    ws = [text_w(ch, "black", size) for ch in s]
    tot = sum(ws) + gapw * (len(s) - 1)
    x = cx - tot / 2
    xs = []
    for k, (ch, w) in enumerate(zip(s, ws)):
        on = hl is not None and k in hl
        if on and hl_a > 0 and ch != " ":
            rrect(c, x - 8, cy - size * 0.62, w + 16, size * 1.24, 14, hl_col, a * hl_a * 0.16)
        text_mid(c, ch, x + w / 2, cy, size, "black", mix(col, hl_col, hl_a) if on else col, a)
        xs.append(x + w / 2)
        x += w + gapw
    return xs


def soma_algarismos(c, t, t0, s, cx, cy, size, sx, sy, ssize, total, a=1.0, step=0.45, col=PURPLE, res_t=None, res_col=GREEN):
    """o número s em (cx, cy); a partir de t0 cada algarismo 'pula' para a soma 'd + d + d = total' que começa em (sx, sy)"""
    xs = numero(c, s, cx, cy, size, a)
    digs = [(k, ch) for k, ch in enumerate(s) if ch != " "]
    x = sx
    plus_w = text_w(" + ", "black", ssize)
    for j, (k, ch) in enumerate(digs):
        u = ease_out(clamp((t - (t0 + j * step)) / 0.5))
        w = text_w(ch, "black", ssize)
        if u > 0:
            hop = math.sin(math.pi * u) * 70
            px, py = lerp(xs[k], x + w / 2, u), lerp(cy, sy, u) - hop
            text_mid(c, ch, px, py, lerp(size, ssize, u), "black", col, a)
        x += w
        if j < len(digs) - 1:
            text_mid(c, "+", x + plus_w / 2, sy, ssize, "black", col, a * ep(t, t0 + (j + 1) * step, 0.3))
            x += plus_w
    rt = res_t if res_t is not None else t0 + len(digs) * step + 0.3
    ar = ep(t, rt, 0.4)
    text_mid(c, " = " + str(total), x, sy, ssize, "black", res_col, ar, align="left")
    return x + text_w(" = " + str(total), "black", ssize)


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "MÚLTIPLOS, DIVISORES E CRITÉRIOS · EP. 1", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["01.a"], 0.5)
    numero(c, "6 813", 640, 430, 170, aa)
    fmid(c, "÷ 9 ?", 640, 600, 80, "black", BLUE, aa)
    # cronômetro de 2 segundos
    ab = ep(t, C["01.a"] + 1.0, 0.4)
    if ab > 0:
        cx_, cy_, r = 1290, 360, 110
        c.drawCircle(cx_, cy_, r + 12, paint(GREEN, ab * 0.15))
        c.drawCircle(cx_, cy_, r, paint("#FFFFFF", ab))
        c.drawArc(skia.Rect.MakeLTRB(cx_ - r, cy_ - r, cx_ + r, cy_ + r), -90, 360 * clamp((t - C["01.a"] - 1.0) / 2.0), False,
                  paint(GREEN, ab, stroke=18, cap_round=True))
        text_mid(c, "2 s", cx_, cy_, 64, "black", INK, ab)
    pill(c, "sem fazer a divisão", 1290, 560, GREEN, size=32, a=ep(t, C["01.b"], 0.4), anchor="center", bounds=(0, 1920))
    ac = ep(t, C["01.c"], 0.4)
    for k, s in enumerate(("CÓDIGO", "SENHA")):
        x = 1160 + k * 260
        rrect(c, x - 110, 660, 220, 90, 18, "#FFFFFF", ac, shadow=True)
        text_mid(c, s, x, 705, 32, "black", AMBER, ac)


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "AO FINAL DESTA AULA", "VOCÊ VAI SABER", GREEN)
    rows = [("02.a", "o que é MÚLTIPLO e DIVISOR"), ("02.b", "listar TODOS os divisores, sem esquecer"),
            ("02.c", "usar os ATALHOS da divisibilidade")]
    for j, (cue, s) in enumerate(rows):
        a, d = rise(t, C[cue])
        y = 320 + j * 150 + d
        check_icon(c, 330, y - 14, 36, a, GREEN)
        text(c, s, 400, y, 54, "black", INK, a, align="left")


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "LEMBRANDO EM 30 SEGUNDOS", "DIVISÃO E RESTO", BLUE)
    a0 = ep(t, C["03.a"], 0.5)
    balas(c, t, 14, 3, 640, 250, 760, C["03.b"], C["03.c"], a0, spread=270)
    fmid(c, "14 balas · 3 crianças", 1400, 260, 34, "black", INK2, a0)
    fmid(c, "cada uma: 4", 1400, 360, 40, "black", BLUE, ep(t, C["03.b"], 0.4))
    fmid(c, "4 × 3 = 12", 1400, 420, 34, "black", INK2, ep(t, C["03.b"] + 0.8, 0.4))
    fmid(c, "sobram 2", 1400, 500, 40, "black", RED, ep(t, C["03.c"], 0.4))
    pill(c, "RESTO = o que sobra", 1400, 590, BLUE, size=30, a=ep(t, C["03.d"], 0.4), anchor="center", bounds=(0, 1920))
    fbox(c, "14 ÷ 3 = 4, resto 2", 1400, 720, 40, ep(t, C["03.e"], 0.4), PURPLE)


# ======================================================================
# bloco A — divisão exata, divisor e múltiplo
# ======================================================================

def b_exata(c, t, C, B):
    frame(c, t, B["start"], "E SE FOSSEM 12 BALAS?", "DIVISÃO EXATA", BLUE)
    a0 = ep(t, C["04.t"], 0.5)
    balas(c, t, 12, 3, 640, 250, 760, C["04.a"], C["04.b"], a0, spread=270)
    fmid(c, "12 ÷ 3 = 4, resto 0", 1400, 300, 44, "black", INK, ep(t, C["04.a"], 0.4))
    fmid(c, "não sobra nenhuma", 1400, 380, 34, "black", GREEN, ep(t, C["04.b"], 0.4))
    ac = ep(t, C["04.c"], 0.4)
    boxed(c, 1130, 450, 540, 130, BLUE, ac, 0.07)
    text_mid(c, "DIVISÃO EXATA", 1400, 492, 34, "black", BLUE, ac)
    text_mid(c, "resto zero", 1400, 545, 28, "bold", INK2, ac)
    ad = ep(t, C["04.d"], 0.4)
    text_mid(c, "12 é DIVISÍVEL por 3", 1400, 660, 40, "black", BLUE, ad)
    text_mid(c, "a divisão por 3 é exata", 1400, 715, 26, "bold", INK2, ad)


def b_divisor(c, t, C, B):
    frame(c, t, B["start"], "QUEM DIVIDIU CERTINHO?", "DIVISOR", BLUE)
    a0 = ep(t, C["05.t"], 0.5)
    balas(c, t, 12, 3, 620, 250, 760, C["05.t"] - 10, 1e9, a0, spread=260)
    ab = ep(t, C["05.b"], 0.5)
    numero(c, "3", 1300, 330, 140, ab, BLUE)
    text_mid(c, "é DIVISOR de", 1300, 450, 40, "black", INK, ab)
    numero(c, "12", 1300, 560, 120, ab)
    ac = ep(t, C["05.c"], 0.4)
    boxed(c, 1060, 660, 480, 110, BLUE, ac, 0.07)
    text_mid(c, "divide certinho,", 1300, 696, 30, "black", BLUE, ac)
    text_mid(c, "sem sobrar bala", 1300, 738, 30, "black", BLUE, ac)


def b_multiplo(c, t, C, B):
    frame(c, t, B["start"], "SUBINDO DE 3 EM 3", "MÚLTIPLO", BLUE)
    a0 = ep(t, C["06.a"], 0.5)
    escada(c, t, 220, 790, 12, 3, C["06.b"], a0, dx=72, dy=40, dur=0.55)
    for k, w in enumerate(("três", "seis", "nove", "doze")):
        tk = WT(C, "06", w, depois=C["06.b"])
        fmid(c, str(3 * (k + 1)), 1180 + k * 120, 260, 54, "black", GREEN, ep(t, tk, 0.3))
    ac = ep(t, C["06.c"], 0.4)
    text_mid(c, "12 é MÚLTIPLO de 3", 1360, 420, 46, "black", BLUE, ac)
    ad = ep(t, C["06.d"], 0.4)
    boxed(c, 1110, 520, 500, 120, BLUE, ad, 0.07)
    text_mid(c, "múltiplo = a TABUADA", 1360, 560, 32, "black", BLUE, ad)
    text_mid(c, "3 · 6 · 9 · 12 · 15 · …", 1360, 605, 28, "bold", INK2, ad)


def b_mesma(c, t, C, B):
    frame(c, t, B["start"], "REPARE", "A MESMA FRASE, DOIS JEITOS", PURPLE)
    aa = ep(t, C["07.a"], 0.5)
    fbox(c, "12 ÷ 3 = 4  (resto 0)", W / 2, 300, 60, aa, PURPLE)
    ab = ep(t, C["07.b"], 0.5)
    arrow(c, W / 2 - 80, 370, 560, 500, BLUE, ab, 5, 18, progress=ab)
    rrect(c, 260, 510, 600, 150, 22, mix("#FFFFFF", BLUE, 0.08), ab, shadow=True)
    text_mid(c, "3 é DIVISOR de 12", 560, 585, 44, "black", BLUE, ab)
    ac = ep(t, C["07.c"], 0.5)
    arrow(c, W / 2 + 80, 370, 1360, 500, GREEN, ac, 5, 18, progress=ac)
    rrect(c, 1060, 510, 600, 150, 22, mix("#FFFFFF", GREEN, 0.08), ac, shadow=True)
    text_mid(c, "12 é MÚLTIPLO de 3", 1360, 585, 44, "black", GREEN, ac)
    pill(c, "a mesma frase, dita de dois jeitos", W / 2, 750, PURPLE, size=32, a=ep(t, C["07.d"], 0.4), anchor="center")


# ======================================================================
# bloco B — divisores acabam, múltiplos não
# ======================================================================

def b_finito(c, t, C, B):
    frame(c, t, B["start"], "QUANTOS DIVISORES O 12 TEM?", "LISTA QUE ACABA", BLUE)
    divs = [("um", 1), ("dois", 2), ("três", 3), ("quatro", 4), ("seis", 6), ("doze", 12)]
    a0 = ep(t, C["08.a"], 0.4)
    ftext(c, "D(12) =", 300, 340, 56, "black", INK, a0, align="left")
    fmid(c, "{", 545, 320, 80, "black", INK2, a0)
    for k, (w, d) in enumerate(divs):
        tk = WT(C, "08", w, depois=C["08.a"])
        chip(c, str(d), 640 + k * 160, 320, BLUE, ep(t, tk, 0.3), 48)
    fmid(c, "}", 1580, 320, 80, "black", INK2, ep(t, C["08.b"], 0.3))
    ab = ep(t, C["08.b"], 0.4)
    text_mid(c, "6 divisores · e ACABOU", W / 2, 470, 46, "black", INK, ab)
    text_mid(c, "nenhum passa do próprio 12", W / 2, 550, 34, "bold", INK2, ep(t, C["08.c"], 0.4))
    pill(c, "FINITA = lista que acaba", W / 2, 690, BLUE, size=34, a=ep(t, C["08.d"], 0.4), anchor="center")


def b_infinito(c, t, C, B):
    frame(c, t, B["start"], "E OS MÚLTIPLOS DE 3?", "LISTA QUE NÃO ACABA", BLUE)
    a0 = ep(t, C["09.a"], 0.4)
    ftext(c, "M(3) =", 260, 320, 56, "black", INK, a0, align="left")
    fmid(c, "{", 470, 300, 80, "black", INK2, a0)
    mults = [("zero", 0), ("três", 3), ("seis", 6), ("nove", 9), ("doze", 12), ("quinze", 15)]
    for k, (w, d) in enumerate(mults):
        tk = WT(C, "09", w, depois=C["09.a"])
        chip(c, str(d), 560 + k * 150, 300, GREEN, ep(t, tk, 0.3), 46)
    ab = ep(t, C["09.b"], 0.4)
    for j in range(3):
        c.drawCircle(1470 + j * 30, 300, 8, paint(GREEN, ab * ep(t, C["09.b"] + 0.25 * j, 0.3)))
    arrow(c, 1380, 380, 1660, 380, GREEN, ab, 5, 18, progress=ep(t, C["09.b"], 1.2))
    text(c, "nunca termina", 1520, 430, 26, "black", GREEN, ab)
    pill(c, "INFINITA = lista que não acaba", W / 2, 540, BLUE, size=34, a=ep(t, C["09.c"], 0.4), anchor="center")
    regra(c, "Divisores acabam; múltiplos não.", W / 2, 700, ep(t, C["09.d"], 0.4), 40)


# ======================================================================
# bloco C — regras que sempre valem
# ======================================================================

def b_regras(c, t, C, B):
    frame(c, t, B["start"], "REGRAS QUE SEMPRE VALEM", "O 1 E O PRÓPRIO NÚMERO", PURPLE)
    for k, (cue, titulo, kids) in enumerate((("10.a", "1 divide TODO número", 1), ("10.b", "todo número divide A SI MESMO", 7))):
        a = ep(t, C[cue], 0.5)
        x0 = 220 + k * 760
        rrect(c, x0, 210, 720, 580, 22, "#FFFFFF", a, shadow=True)
        text_mid(c, titulo, x0 + 360, 260, 34, "black", PURPLE, a)
        cx = x0 + 360
        if kids == 1:
            crianca(c, cx, 690, a, BLUE, 1.0)
            for i in range(7):
                bala(c, cx - 90 + (i % 4) * 60, 470 + (i // 4) * 50, CANDY[i % 6], a * ep(t, C[cue] + 0.6, 0.4))
            fmid(c, "7 ÷ 1 = 7", cx, 740, 40, "black", INK, ep(t, C[cue] + 1.0, 0.4))
        else:
            for i in range(7):
                x = x0 + 75 + i * 95
                crianca(c, x, 690, a, [BLUE, PURPLE, GREEN, AMBER, RED, INK2, BLUE][i], 0.75)
                bala(c, x, 540, CANDY[i % 6], a * ep(t, C[cue] + 0.6 + 0.08 * i, 0.3), 16)
            fmid(c, "7 ÷ 7 = 1", cx, 740, 40, "black", INK, ep(t, C[cue] + 1.2, 0.4))


def b_zero(c, t, C, B):
    frame(c, t, B["start"], "E O ZERO?", "MÚLTIPLO SIM · DIVISOR NUNCA", PURPLE)
    aa = ep(t, C["11.a"], 0.5)
    rrect(c, 220, 220, 720, 360, 22, mix("#FFFFFF", GREEN, 0.07), aa, shadow=True)
    check_icon(c, 300, 290, 30, aa, GREEN)
    text(c, "0 é MÚLTIPLO de todos", 350, 302, 38, "black", GREEN, aa, align="left")
    fmid(c, "3 × 0 = 0", 580, 420, 64, "black", INK, aa)
    text_mid(c, "o degrau onde a escada começa", 580, 520, 28, "bold", INK2, aa)
    ab = ep(t, C["11.b"], 0.5)
    rrect(c, 980, 220, 720, 360, 22, mix("#FFFFFF", RED, 0.06), ab, shadow=True)
    check_icon(c, 1060, 290, 30, ab, RED, "x")
    text(c, "0 NÃO é divisor", 1110, 302, 38, "black", RED, ab, align="left")
    ac = ep(t, C["11.c"], 0.5)
    fmid(c, "12 ÷ 0 = ?", 1340, 420, 64, "black", INK, ac)
    text_mid(c, "12 balas para ZERO crianças?", 1340, 520, 28, "bold", INK2, ac)
    regra(c, "divisão por zero NÃO EXISTE", W / 2, 700, ep(t, C["11.d"], 0.4), 40, RED)


def trio(c, x, y, a, col, s=34):
    """um grupinho de 3 quadradinhos"""
    for j in range(3):
        rrect(c, x + j * (s + 4), y, s, s, 6, col, a)
    return 3 * (s + 4)


def b_soma(c, t, C, B):
    frame(c, t, B["start"], "UMA ÚLTIMA REGRA", "SOMA E DIFERENÇA", PURPLE)
    aa = ep(t, C["12.a"], 0.5)
    for k in range(4):
        trio(c, 300 + k * 140, 280, aa, BLUE)
    fmid(c, "12", 230, 297, 40, "black", BLUE, aa)
    for k in range(3):
        trio(c, 300 + k * 140, 370, aa, GREEN)
    fmid(c, "9", 230, 387, 40, "black", GREEN, aa)
    ab = ep(t, C["12.b"], 0.5)
    for k in range(7):
        trio(c, 300 + k * 140, 500, ab, BLUE if k < 4 else GREEN)
    fmid(c, "21", 230, 517, 40, "black", INK, ab)
    text(c, "12 + 9 = 21 = 3 × 7", 1340, 530, 34, "black", INK, ab, align="left")
    ac = ep(t, C["12.c"], 0.5)
    trio(c, 300, 600, ac, BLUE)
    fmid(c, "3", 230, 617, 40, "black", INK, ac)
    text(c, "12 − 9 = 3", 1340, 630, 34, "black", INK, ac, align="left")
    text(c, "3 divide 12 e divide 9", 1340, 310, 32, "black", PURPLE, aa, align="left")
    regra(c, "quem divide os dois divide a soma e a diferença", W / 2, 760, ep(t, C["12.d"], 0.4), 30)


# ======================================================================
# bloco D — os retângulos de quadradinhos
# ======================================================================

RET = [("13.a", 36), ("13.b", 36), ("13.c", 18), ("13.d", 12), ("13.e", 9), ("13.f", 6)]


def b_retangulos(c, t, C, B):
    sid = which(t, C, ["13", "14"])
    head_seq(c, t, C, [("13", "OS DIVISORES DE 36", "QUAIS RETÂNGULOS DÁ PARA MONTAR?", BLUE),
                       ("14", "E COM 5 FILEIRAS?", "OS LADOS SÃO OS DIVISORES", BLUE)])
    card(c, *CARD_R)
    a0 = ep(t, C["13.a"], 0.5)
    keys = [(C[cue], cols) for cue, cols in RET]
    if sid == "14":
        keys += [(C["14.t"], 7), (C["14.b"], 6)]
    cell = 34
    grade_morph(c, t, keys, W / 2 - 60, 470, 36, cell, a0)
    if sid == "13":
        fmid(c, "36 quadradinhos", W / 2, 230, 34, "black", INK2, a0 * (1 - ep(t, C["13.b"], 0.3)))
        prs = [("13.b", "1 × 36"), ("13.c", "2 × 18"), ("13.d", "3 × 12"), ("13.e", "4 × 9"), ("13.f", "6 × 6")]
        for k, (cue, s) in enumerate(prs):
            fmid(c, s, 1580, 300 + k * 90, 38, "black", PURPLE, ep(t, C[cue] + 0.8, 0.4), align="center")
        return
    # 14: tentativa com 5 fileiras (7 colunas → sobra 1), depois volta ao 6×6
    tt = C["14.t"]
    if t < C["14.b"] - 0.05:
        # 36 em fileiras de 7: 5 fileiras cheias + 1 sobrando
        pass
    a_fail = ep(t, C["14.a"], 0.4) * (1 - ep(t, C["14.b"], 0.3))
    selo(c, 1520, 330, a_fail, "SOBRA 1", RED, -6, 34)
    text_mid(c, "5 não é divisor de 36", 1520, 430, 28, "black", RED, a_fail)
    ab = ep(t, C["14.b"], 0.4)
    for k, d in enumerate((1, 2, 3, 4, 6, 9, 12, 18, 36)):
        chip(c, str(d), 260 + k * 80 if k < 5 else 260 + k * 80, 790, PURPLE, ab * ep(t, C["14.b"] + 0.1 * k, 0.3), 30)
    ac = ep(t, C["14.c"], 0.4)
    pill(c, "6 × 6: os lados SE ENCONTRARAM", 1500, 400, GREEN, size=26, a=ac, anchor="center", bounds=(0, 1920))
    text_mid(c, "depois disso, só se repetem", 1500, 470, 26, "bold", INK2, ac)


def b_pares(c, t, C, B):
    frame(c, t, B["start"], "O MÉTODO DOS PARES", "SEM ESQUECER NENHUM", GREEN)
    a0 = ep(t, C["15.a"], 0.4)
    text(c, "de 1 para cima, procure PARES que multiplicados dão 36", 260, 230, 30, "black", GREEN, a0, align="left")
    prs = [("um", 1, 36), ("dois", 2, 18), ("três", 3, 12), ("quatro", 4, 9), ("seis", 6, 6)]
    for k, (w, p, q) in enumerate(prs):
        tk = WT(C, "15", w, depois=C["15.b"])
        a = ep(t, tk, 0.3)
        y = 320 + k * 82
        chip(c, str(p), 360, y, BLUE, a, 36)
        fmid(c, "×", 450, y, 36, "black", INK2, a)
        chip(c, str(q), 540, y, PURPLE, a, 36)
        if p == q:
            arrow(c, 620, y, 720, y, GREEN, ep(t, C["15.c"], 0.3), 4, 14, progress=1.0)
            text(c, "se encontraram: PARE", 740, y + 10, 30, "black", GREEN, ep(t, C["15.c"], 0.3), align="left")
    ad = ep(t, C["15.d"], 0.4)
    ftext(c, "D(36) = {1, 2, 3, 4, 6, 9, 12, 18, 36}", 1300, 470, 40, "black", INK, ad)
    fbox(c, "9 divisores", 1300, 600, 50, ep(t, C["15.e"], 0.4), GREEN)


# ======================================================================
# bloco E — critérios que se usam de verdade
# ======================================================================

def b_criterio(c, t, C, B):
    frame(c, t, B["start"], "E SE O NÚMERO FOR GRANDE?", "CRITÉRIO DE DIVISIBILIDADE", BLUE)
    a0 = ep(t, C["16.t"], 0.4)
    ab = ep(t, C["16.b"], 0.4)
    xs = numero(c, "6 813", 640, 400, 160, a0, INK, hl=(0, 2, 3, 4), hl_col=PURPLE, hl_a=ab)
    aa = ep(t, C["16.a"], 0.4)
    boxed(c, 1080, 280, 560, 230, BLUE, aa, 0.07)
    text_mid(c, "CRITÉRIO DE DIVISIBILIDADE", 1360, 330, 30, "black", BLUE, aa)
    text_mid(c, "um TESTE RÁPIDO:", 1360, 395, 32, "black", INK, aa)
    text_mid(c, "a divisão é exata? sem fazer a conta", 1360, 450, 26, "bold", INK2, aa)
    text_mid(c, "ALGARISMOS = os símbolos de 0 a 9 que formam o número", W / 2, 600, 30, "black", PURPLE, ab)
    for k in range(10):
        chip(c, str(k), 520 + k * 98, 700, PURPLE, ab * ep(t, C["16.b"] + 0.08 * k, 0.3), 34)


def teste_fim(c, t, num, cx, cy, size, hl, a, a_hl, ok_t, col=GREEN):
    xs = numero(c, num, cx, cy, size, a, INK, hl=hl, hl_col=col, hl_a=a_hl)
    return xs


def b_c2(c, t, C, B):
    frame(c, t, B["start"], "O MAIS FÁCIL", "DIVISÍVEL POR 2", GREEN)
    aa = ep(t, C["17.a"], 0.4)
    text_mid(c, "termina em algarismo PAR", W / 2, 240, 40, "black", GREEN, aa)
    for k, d in enumerate("02468"):
        chip(c, d, 760 + k * 100, 330, GREEN, aa * ep(t, C["17.a"] + 0.6 + 0.1 * k, 0.3), 40)
    ab = ep(t, C["17.b"], 0.4)
    numero(c, "374", W / 2, 540, 150, ab, INK, hl=(2,), hl_col=GREEN, hl_a=ep(t, C["17.b"] + 1.0, 0.4))
    check_icon(c, W / 2 + 230, 540, 36, ep(t, C["17.b"] + 1.6, 0.3), GREEN)
    fmid(c, "÷ 2 ✓", W / 2, 700, 44, "black", GREEN, ep(t, C["17.b"] + 1.6, 0.3))


def b_c5(c, t, C, B):
    frame(c, t, B["start"], "OS DO FINAL DO NÚMERO", "DIVISÍVEL POR 5 E POR 10", GREEN)
    aa = ep(t, C["18.a"], 0.4)
    text_mid(c, "por 5: termina em 0 ou 5", 560, 250, 36, "black", GREEN, aa)
    ab = ep(t, C["18.b"], 0.4)
    numero(c, "895", 560, 450, 130, ab, INK, hl=(2,), hl_col=GREEN, hl_a=ep(t, C["18.b"] + 1.0, 0.4))
    fmid(c, "÷ 5 ✓", 560, 600, 44, "black", GREEN, ep(t, C["18.b"] + 1.5, 0.3))
    ac = ep(t, C["18.c"], 0.4)
    line(c, W / 2, 230, W / 2, 760, LINE, ac, 3)
    text_mid(c, "por 10: termina em 0", 1360, 250, 36, "black", GREEN, ac)
    ad = ep(t, C["18.d"], 0.4)
    numero(c, "2 470", 1360, 450, 130, ad, INK, hl=(4,), hl_col=GREEN, hl_a=ep(t, C["18.d"] + 0.8, 0.4))
    fmid(c, "÷ 10 ✓", 1360, 600, 44, "black", GREEN, ep(t, C["18.d"] + 1.3, 0.3))


def b_c3(c, t, C, B):
    frame(c, t, B["start"], "O MAIS ÚTIL DE TODOS", "DIVISÍVEL POR 3", GREEN)
    aa = ep(t, C["19.a"], 0.4)
    regra(c, "some os algarismos: a soma é divisível por 3?", W / 2, 250, aa, 34, GREEN)
    ab = ep(t, C["19.b"], 0.4)
    soma_algarismos(c, t, C["19.b"] + 0.6, "471", 470, 470, 150, 820, 470, 80, 12, ab,
                    res_t=WT(C, "19", "doze", depois=C["19.b"]))
    ac = ep(t, C["19.c"], 0.4)
    fmid(c, "12 ÷ 3 = 4  ✓", 1300, 620, 44, "black", GREEN, ac)
    fbox(c, "471 é divisível por 3", W / 2, 740, 40, ep(t, C["19.d"], 0.4), GREEN)


def b_c9(c, t, C, B):
    frame(c, t, B["start"], "IGUALZINHO AO DO 3", "DIVISÍVEL POR 9", GREEN)
    a0 = ep(t, C["20.t"], 0.4)
    regra(c, "soma dos algarismos divisível por 9", W / 2, 250, a0, 34, GREEN)
    aa = ep(t, C["20.a"], 0.4)
    soma_algarismos(c, t, C["20.b"], "6 813", 460, 470, 140, 820, 470, 70, 18, aa, step=0.85,
                    res_t=WT(C, "20", "dezoito", depois=C["20.b"]))
    ac = ep(t, C["20.c"], 0.4)
    fmid(c, "18 ÷ 9 = 2  ✓", 1300, 620, 44, "black", GREEN, ac)
    fbox(c, "6 813 é divisível por 9", W / 2, 740, 40, ep(t, C["20.d"], 0.4), GREEN)


# ======================================================================
# recap
# ======================================================================

FRASES = ["Divisor divide sem sobrar; múltiplo é a tabuada.", "Divisores acabam; múltiplos não.",
          "3 e 9: some os algarismos."]


def b_recap(c, t, C, B):
    sid = which(t, C, ["21", "36"])
    frame(c, t, B["start"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "21" else "PARA FECHAR", PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 320 + k * 170 + d
        badge_num(c, k + 1, 280, y - 16, a, 36, bg=PURPLE)
        text(c, s, 350, y, 52, "black", INK, a, align="left")


# ======================================================================
# bloco F — 4, 6, 8 (e o 7 e o 11 só citados)
# ======================================================================

def b_c4(c, t, C, B):
    frame(c, t, B["start"], "OS DOIS ÚLTIMOS ALGARISMOS", "DIVISÍVEL POR 4", GREEN)
    aa = ep(t, C["22.a"], 0.4)
    regra(c, "os 2 últimos algarismos formam um número divisível por 4?", W / 2, 250, aa, 30, GREEN)
    ab = ep(t, C["22.b"], 0.4)
    numero(c, "2 524", 620, 480, 150, ab, INK, hl=(3, 4), hl_col=GREEN, hl_a=ep(t, C["22.b"] + 1.2, 0.4))
    a2 = ep(t, C["22.b"] + 1.6, 0.4)
    arrow(c, 900, 480, 1080, 480, GREEN, a2, 5, 18, progress=a2)
    fmid(c, "24", 1200, 480, 110, "black", GREEN, a2)
    ac = ep(t, C["22.c"], 0.4)
    fmid(c, "24 ÷ 4 = 6  ✓", 1200, 640, 44, "black", GREEN, ac)
    fbox(c, "2 524 é divisível por 4", W / 2, 760, 36, ep(t, C["22.c"] + 1.2, 0.4), GREEN)


def b_c6(c, t, C, B):
    frame(c, t, B["start"], "DOIS TESTES DE UMA VEZ", "DIVISÍVEL POR 6", GREEN)
    aa = ep(t, C["23.a"], 0.4)
    regra(c, "por 6 = passa no do 2 E no do 3", W / 2, 250, aa, 34, PURPLE)
    ab = ep(t, C["23.b"], 0.4)
    numero(c, "726", 430, 480, 150, ab, INK, hl=(2,), hl_col=GREEN, hl_a=ab)
    rrect(c, 760, 360, 420, 250, 20, mix("#FFFFFF", GREEN, 0.07), ab)
    text_mid(c, "TESTE DO 2", 970, 400, 24, "black", GREEN, ab)
    text_mid(c, "termina em 6: par", 970, 470, 30, "black", INK, ab)
    check_icon(c, 970, 550, 26, ep(t, C["23.b"] + 1.2, 0.3), GREEN)
    ac = ep(t, C["23.c"], 0.4)
    rrect(c, 1220, 360, 420, 250, 20, mix("#FFFFFF", GREEN, 0.07), ac)
    text_mid(c, "TESTE DO 3", 1430, 400, 24, "black", GREEN, ac)
    fmid(c, "7 + 2 + 6 = 15", 1430, 470, 34, "black", INK, ac)
    check_icon(c, 1430, 550, 26, ep(t, C["23.c"] + 1.4, 0.3), GREEN)
    fbox(c, "726 é divisível por 6", W / 2, 730, 40, ep(t, C["23.d"], 0.4), GREEN)


def b_c8(c, t, C, B):
    frame(c, t, B["start"], "OS TRÊS ÚLTIMOS ALGARISMOS", "DIVISÍVEL POR 8", GREEN)
    a0 = ep(t, C["24.t"], 0.4)
    ab_ = ep(t, C["24.b"], 0.4)
    k = 1 - ab_
    numero(c, "5 120", 560, 380, 140, a0, INK, hl=(2, 3, 4), hl_col=GREEN, hl_a=ep(t, C["24.a"] + 0.8, 0.4))
    aa = ep(t, C["24.a"] + 1.4, 0.4)
    fmid(c, "120 = 8 × 15  ✓", 1220, 380, 48, "black", GREEN, aa)
    line(c, 220, 520, 1700, 520, LINE, ab_, 3)
    for j, (n_, s_) in enumerate((("7", "dobre o último, subtraia... trabalhoso"), ("11", "soma alternada dos algarismos"))):
        x = 520 + j * 760
        chip(c, n_, x - 200, 620, GRAY, ab_, 44)
        text(c, s_, x - 130, 632, 28, "bold", INK2, ab_, align="left")
    pill(c, "o do 7: muitas vezes é mais rápido DIVIDIR", W / 2, 760, AMBER, size=30, a=ep(t, C["24.c"], 0.4), anchor="center")


# ======================================================================
# bloco G — combinar critérios
# ======================================================================

def b_combinar(c, t, C, B):
    sid = which(t, C, ["25", "26"])
    head_seq(c, t, C, [("25", "E DIVISÍVEL POR 12?", "JUNTE DOIS TESTES", GREEN), ("26", "POR QUE NÃO 2 E 6?", "A ARMADILHA", AMBER)])
    card(c, *CARD_R)
    if sid == "25":
        rows = [("25.b", "12", "3", "4"), ("25.c", "15", "3", "5"), ("25.d", "45", "5", "9")]
        for k, (cue, n_, p, q) in enumerate(rows):
            a, d = rise(t, C[cue])
            y = 270 + k * 120 + d
            chip(c, n_, 500, y, INK2, a, 46)
            arrow(c, 570, y, 700, y, GREEN, a, 4, 14)
            text_mid(c, "teste o", 790, y, 30, "bold", INK2, a)
            chip(c, p, 900, y, GREEN, a, 46)
            text_mid(c, "e o", 990, y, 30, "bold", INK2, a)
            chip(c, q, 1080, y, GREEN, a, 46)
        ae = ep(t, C["25.e"], 0.4)
        boxed(c, 360, 640, 1200, 130, BLUE, ae, 0.07)
        text_mid(c, "PRIMOS ENTRE SI", W / 2, 680, 32, "black", BLUE, ae)
        text_mid(c, "o único divisor em comum é o 1", W / 2, 730, 30, "bold", INK2, ae)
        return
    aa = ep(t, C["26.a"], 0.4)
    text_mid(c, "2 e 6 têm o 2 em comum: NÃO são primos entre si", W / 2, 240, 32, "black", AMBER, aa)
    ab = ep(t, C["26.b"], 0.4)
    numero(c, "30", 420, 420, 150, ab)
    for k, (s, tk) in enumerate((("par  ✓", C["26.b"] + 0.6), ("÷ 6  ✓", C["26.b"] + 1.4))):
        fmid(c, s, 760, 360 + k * 90, 40, "black", GREEN, ep(t, tk, 0.3), align="left")
    ac = ep(t, C["26.c"], 0.4)
    fmid(c, "30 ÷ 12 = 2, resto 6", 1340, 400, 44, "black", RED, ac)
    check_icon(c, 1340, 480, 30, ac, RED, "x")
    ad = ep(t, C["26.d"], 0.4)
    rrect(c, 360, 600, 1200, 150, 20, mix("#FFFFFF", GREEN, 0.07), ad)
    fmid(c, "com 3 e 4:  30 ÷ 4 = 7, resto 2  →  reprova, como deve ser", W / 2, 675, 32, "black", GREEN, ad)


def b_erros(c, t, C, B):
    erro_cards(c, t, C, ["27", "28", "29"],
               [("Achar que o ZERO é divisor de todo número", "o zero aparece em toda tabuada",
                 "isso faz dele MÚLTIPLO de todos; divisão por zero não existe"),
                ("Listar divisores no chute e esquecer algum", "os pequenos vêm fácil: 1, 2, 3, 4, 6...",
                 "use os PARES: cada pequeno traz o seu par grande (o 18, o 36)"),
                ("Testar divisível por 12 com o 2 e o 6", "2 × 6 = 12",
                 "2 e 6 têm divisor em comum: o 30 passa nos dois. Use 3 e 4")])


# ======================================================================
# exercício e questão
# ======================================================================

def b_exercicio(c, t, C, B):
    head_seq(c, t, C, [("30", "SUA VEZ", "PAUSE E RESPONDA", GREEN), ("31", "CONFERINDO", "OS TRÊS TESTES", GREEN)])
    card(c, *CARD_R)
    rows = [("30.a", "522", "÷ 3 ?", "31.a", "5 + 2 + 2 = 9  ✓"), ("30.b", "1 316", "÷ 4 ?", "31.b", "16 = 4 × 4  ✓"),
            ("30.c", "534", "÷ 6 ?", "31.c", "par ✓  e  5 + 3 + 4 = 12 ✓")]
    for k, (cq, n_, q, cr, r) in enumerate(rows):
        a, d = rise(t, C[cq])
        y = 300 + k * 160 + d
        fmid(c, n_, 420, y, 80, "black", INK, a)
        fmid(c, q, 700, y, 60, "black", BLUE, a)
        ar = ep(t, C[cr], 0.4)
        fmid(c, r, 1000, y, 40, "black", GREEN, ar, align="left")
        if ar > 0:
            selo(c, 1600, y, ar, "SIM", GREEN, -6, 34)
    pause_timer(c, t, C["30.end"] - 1.9, 1500, 460)


def codigo(c, cx, cy, a, xval=None, x_col=AMBER, size=60):
    digs = ["4", "3", "7", "x" if xval is None else str(xval), "0"]
    for k, d in enumerate(digs):
        x = cx + (k - 2) * (size * 1.5)
        rrect(c, x - size * 0.6, cy - size * 0.7, size * 1.2, size * 1.4, 14, "#FFFFFF", a, shadow=True)
        text_mid(c, d, x, cy, size, "black", x_col if k == 3 else INK, a)


def b_questao(c, t, C, B):
    sid = which(t, C, ["32", "33", "34", "35"])
    head_seq(c, t, C, [("32", "QUESTÃO 3", "CÓDIGO COM ALGARISMO DESCONHECIDO", BLUE), ("33", "RESOLVENDO", "TESTE DO 2 E DO 3", GREEN),
                       ("34", "TESTANDO O X", "DE 0 A 9", GREEN), ("35", "REPARE", "O PADRÃO DE 3 EM 3", GREEN)])
    card(c, *CARD_R)
    if sid == "32":
        a = ep(t, C["32.a"], 0.4)
        codigo(c, 520, 300, a)
        para(c, "Um código de validação tem cinco algarismos na forma 4 3 7 x 0, em que x é um algarismo desconhecido. "
             "O código só é válido se o número for divisível por 6. Quantos valores de x tornam o código válido?",
             200, 440, 28, "bold", INK, ep(t, C["32.a"], 0.4), 660, 36)
        ad = ep(t, C["32.d"], 0.4)
        for k, s in enumerate(("1", "2", "3", "4", "5")):
            y = 260 + k * 92
            badge_num(c, "ABCDE"[k], 1050, y, ad, 26, bg=INK)
            text(c, s, 1100, y + 14, 40, "black", INK, ad, align="left")
        pause_timer(c, t, C["32.end"] - 1.9, 1520, 470)
        text(c, "Questão do material de estudo (seção 12)", 180, 860, 16, "medium", GRAY, a, align="left")
        return
    if sid == "33":
        codigo(c, W / 2, 270, 1.0)
        regra(c, "por 6 = por 2 E por 3", W / 2, 400, ep(t, C["33.a"], 0.4), 34)
        ab = ep(t, C["33.b"], 0.4)
        text(c, "por 2: termina em 0 (par)  ✓  qualquer x", 320, 530, 34, "black", GREEN, ab, align="left")
        ac = ep(t, C["33.c"], 0.4)
        text(c, "por 3: soma dos algarismos divisível por 3", 320, 610, 34, "black", INK, ac, align="left")
        fbox(c, "4 + 3 + 7 + x + 0 = 14 + x", W / 2, 730, 44, ep(t, C["33.d"], 0.4), PURPLE)
        return
    # 34 / 35: tabela x × (14 + x)
    cues = ["34.a", "34.b", "34.c", "34.c", "34.d", "34.e", "34.e", "34.f", "34.g", "34.g"]
    x0, y0, cw = 300, 330, 132
    text(c, "x", x0 - 70, y0 + 12, 34, "black", AMBER, 1.0, align="center")
    text(c, "14 + x", x0 - 70, y0 + 112, 26, "black", PURPLE, 1.0, align="center")
    for k in range(10):
        a = ep(t, C[cues[k]], 0.3) if sid == "34" else 1.0
        ok = (14 + k) % 3 == 0
        x = x0 + k * cw
        rrect(c, x, y0 - 30, cw - 10, 80, 12, "#F4F5F7", a)
        text_mid(c, str(k), x + (cw - 10) / 2, y0 + 10, 36, "black", INK, a)
        rrect(c, x, y0 + 70, cw - 10, 80, 12, mix("#FFFFFF", GREEN if ok else RED, 0.12), a)
        text_mid(c, str(14 + k), x + (cw - 10) / 2, y0 + 110, 36, "black", GREEN if ok else INK2, a)
        check_icon(c, x + (cw - 10) / 2, y0 + 200, 22, a, GREEN if ok else RED, "check" if ok else "x")
    if sid == "34":
        ah = ep(t, C["34.h"], 0.4)
        text_mid(c, "x = 1, 4 ou 7  →  3 valores", W / 2, 650, 46, "black", GREEN, ah)
        selo(c, W / 2, 760, ep(t, C["34.i"], 0.4), "LETRA C", GREEN, -4, 40)
        return
    aa = ep(t, C["35.a"], 0.4)
    for j, (k1, k2) in enumerate(((1, 4), (4, 7))):
        xa, xb = x0 + k1 * cw + (cw - 10) / 2, x0 + k2 * cw + (cw - 10) / 2
        pth = skia.Path(); pth.moveTo(xa, y0 - 40); pth.quadTo((xa + xb) / 2, y0 - 120, xb, y0 - 40)
        pm = skia.PathMeasure(pth, False); seg = skia.Path()
        pm.getSegment(0, pm.getLength() * ep(t, C["35.a"] + 0.5 * j, 0.6), seg, True)
        c.drawPath(seg, paint(GREEN, aa, stroke=5, cap_round=True))
        text_mid(c, "+3", (xa + xb) / 2, y0 - 110, 30, "black", GREEN, aa)
    ab = ep(t, C["35.b"], 0.4)
    text_mid(c, "a soma sobe de 3 em 3: 15 → 18 → 21", W / 2, 650, 40, "black", PURPLE, ab)
    pill(c, "quem marca 2 parou de testar antes do 7", W / 2, 760, AMBER, size=30, a=ep(t, C["35.c"], 0.4), anchor="center")


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "OS NÚMEROS PRIMOS", PURPLE)
    a0 = ep(t, C["37.a"], 0.4)
    keys = [(C["37.a"], 4), (C["37.a"] + 1.4, 3), (C["37.a"] + 2.8, 7)]
    grade_morph(c, t, keys, 760, 360, 7, 70, a0, lados=False)
    fail = ep(t, C["37.a"] + 0.6, 0.3) * (1 - ep(t, C["37.a"] + 2.8, 0.3))
    text_mid(c, "não fecha...", 760, 520, 30, "black", RED, fail)
    text_mid(c, "só uma FILA: 1 × 7", 760, 520, 32, "black", PURPLE, ep(t, C["37.a"] + 3.4, 0.4))
    ab = ep(t, C["37.b"], 0.4)
    for k, n_ in enumerate(("7", "13", "29")):
        chip(c, n_, 1260 + k * 130, 330, PURPLE, ab * ep(t, C["37.b"] + 0.5 * k, 0.3), 46)
    text_mid(c, "NÚMEROS PRIMOS", 1390, 470, 46, "black", PURPLE, ep(t, C["37.c"], 0.4))
    ad = ep(t, C["37.d"], 0.4)
    for r_ in range(3):
        for k in range(4 - (r_ % 2)):
            rrect(c, 1180 + k * 110 + (r_ % 2) * 55, 560 + r_ * 50, 100, 42, 6, "#C2603B", ad)
    text_mid(c, "os TIJOLOS de todos os números", 1390, 760, 32, "black", "#C2603B", ad)


def b_cta(c, t, C, B):
    cta(c, t, C["38.like"], C["38.sub"], C["38.bell"], C["38.com"], C["38.bye"], "Você já conhecia o truque de somar os algarismos?",
        canal="no Estudativo")


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, exata=b_exata, divisor=b_divisor, multiplo=b_multiplo,
              mesma=b_mesma, finito=b_finito, infinito=b_infinito, regras=b_regras, zero=b_zero, soma=b_soma,
              retangulos=b_retangulos, pares=b_pares, criterio=b_criterio, c2=b_c2, c5=b_c5, c3=b_c3, c9=b_c9, recap=b_recap,
              c4=b_c4, c6=b_c6, c8=b_c8, combinar=b_combinar, erros=b_erros, exercicio=b_exercicio, questao=b_questao,
              ponte=b_ponte, cta=b_cta)
