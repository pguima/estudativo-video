"""Visual — Redação ENEM, Leitura da Proposta, Episódio 1: O que a prova pede (tema claro).
Analogia âncora da série: ETIQUETA DE ENCOMENDA (cidade = assunto · endereço completo = tema · dentro da caixa = tese).
Apoio: encomenda de BOLO (regras da casa · fotos de referência · pedido exato) e a FOLHA DE RASCUNHO (letra manuscrita).
Cores: azul = definição/tema · verde = dica/método · âmbar = armadilha · vermelho = erro/penalidade · roxo = regra oficial.
"""
import json
import math
import re
from pathlib import Path
import skia
import motor
motor.set_theme("claro")
from motor import *  # noqa
from aula import *  # noqa

MARCA = ""
ARQUIVO_FINAL = "enem_redacao_leitura_proposta_ep1_o_que_a_prova_pede.mp4"
CARD_R = (140, 150, 1640, 690)

TEMA25 = "Perspectivas acerca do envelhecimento na sociedade brasileira"
TEMA20 = "O estigma associado às doenças mentais na sociedade brasileira"
TEMA22 = "Desafios para a valorização de comunidades e povos tradicionais no Brasil"
TEMA17 = "Desafios para a formação educacional de surdos no Brasil"
TESE20 = "O estigma afasta as pessoas do tratamento e precisa ser combatido na escola e na mídia."

PAPER = "#FFFDF4"
PAPER_LINE = "#CFE0F5"
PEN = "#1F3A93"
KRAFT = "#C8955C"

# ======================================================================
# utilidades
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


def regra(c, s, cy, a, size=40, col=None):
    if a <= 0:
        return
    col = col or PURPLE
    w = text_w(s, "black", size) + 90
    boxed(c, W / 2 - w / 2, cy - 50, w, 100, col, a, 0.10)
    text_mid(c, s, W / 2, cy, size, "black", col, a)


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


def bubble(c, s, x, y, w, col, a, left=True, size=32, fg=None):
    if a <= 0:
        return 0
    lines = wrap(s, "bold", size, w - 60)
    h = len(lines) * size * 1.3 + 44
    rrect(c, x, y, w, h, 26, col, a, shadow=True)
    p = skia.Path()
    if left:
        p.moveTo(x + 30, y + h - 2); p.lineTo(x + 6, y + h + 22); p.lineTo(x + 64, y + h - 2)
    else:
        p.moveTo(x + w - 30, y + h - 2); p.lineTo(x + w - 6, y + h + 22); p.lineTo(x + w - 64, y + h - 2)
    c.drawPath(p, paint(col, a))
    for k, ln in enumerate(lines):
        text(c, ln, x + 30, y + 22 + size * 0.95 + k * size * 1.3, size, "bold", fg or on(col), a, align="left")
    return h


def person(c, x, y, col, a, s=1.0):
    if a <= 0:
        return
    c.drawCircle(x, y, 34 * s, paint(col, a))
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x - 50 * s, y + 44 * s, 100 * s, 90 * s), 40 * s, 40 * s), paint(col, a))


def xmark(c, cx, cy, r, a, col=None, w=10):
    if a <= 0:
        return
    col = col or RED
    line(c, cx - r, cy - r, cx + r, cy + r, col, a, w, progress=clamp(a * 2))
    line(c, cx + r, cy - r, cx - r, cy + r, col, a, w, progress=clamp(a * 2 - 1))


# ======================================================================
# letra manuscrita (folha de rascunho)
# ======================================================================

HAND_TF = skia.Typeface.MakeFromFile("C:/Windows/Fonts/segoesc.ttf")
HAND_TFB = skia.Typeface.MakeFromFile("C:/Windows/Fonts/segoescb.ttf")
_HF = {}


def hfont(size, bold=False):
    k = (size, bold)
    if k not in _HF:
        _HF[k] = skia.Font(HAND_TFB if bold else HAND_TF, size)
    return _HF[k]


def hand_w(s, size, bold=False):
    return hfont(size, bold).measureText(s)


def hand(c, s, x, y, size, color, a=1.0, reveal=1.0, align="left", bold=False, pen=True):
    """texto manuscrito; reveal < 1 escreve aos poucos, com a ponta da caneta"""
    if a <= 0 or reveal <= 0:
        return 0
    f = hfont(size, bold)
    full = f.measureText(s)
    n = len(s) if reveal >= 1 else int(len(s) * reveal)
    sub = s[:n]
    xx = x - full / 2 if align == "center" else x - full if align == "right" else x
    c.drawString(sub, xx, y, f, paint(color, a))
    if pen and 0 < reveal < 1:
        px = xx + f.measureText(sub)
        c.drawCircle(px + 4, y - size * 0.25, 6, paint(color, a))
    return full


def hwrap(s, size, maxw, bold=False):
    out, cur = [], ""
    for w in s.split():
        tst = (cur + " " + w).strip()
        if cur and hand_w(tst, size, bold) > maxw:
            out.append(cur); cur = w
        else:
            cur = tst
    if cur:
        out.append(cur)
    return out


def hand_para(c, s, x, y, size, color, a, maxw, lh, reveal=1.0, bold=False):
    """parágrafo manuscrito revelado em ordem; retorna nº de linhas"""
    lines = hwrap(s, size, maxw, bold)
    tot = sum(len(l) for l in lines)
    done = reveal * tot
    for k, ln in enumerate(lines):
        r = clamp(done / max(1, len(ln)))
        hand(c, ln, x, y + k * lh, size, color, a, r, bold=bold)
        done -= len(ln)
    return len(lines)


def paper(c, x, y, w, h, a, lh=56, top=None, margin=True, rot=0.0):
    """folha de rascunho pautada"""
    if a <= 0:
        return
    if rot:
        c.save(); c.translate(x + w / 2, y + h / 2); c.rotate(rot); c.translate(-(x + w / 2), -(y + h / 2))
    rrect(c, x, y, w, h, 10, PAPER, a, shadow=True)
    yy = (top or y + 70)
    while yy < y + h - 20:
        line(c, x + 14, yy + 12, x + w - 14, yy + 12, PAPER_LINE, a, 2)
        yy += lh
    if margin:
        line(c, x + 80, y + 10, x + 80, y + h - 10, "#F3A6A6", a, 2.5)
    text(c, "RASCUNHO", x + w - 24, y + 40, 18, "black", LIGHT, a, align="right", tracking=2)
    if rot:
        c.restore()


def underline(c, x0, x1, y, col, a, prog_=1.0, w=6):
    if a <= 0:
        return
    line(c, x0, y, x0 + (x1 - x0) * clamp(prog_), y + 2, col, a, w)


# ======================================================================
# tempos das palavras (para escrever junto com a voz)
# ======================================================================

TEMPOS = Path(__file__).resolve().parent.parent / "audio" / "tempos.json"
try:
    _SC = {s["id"]: s for s in json.load(open(TEMPOS, encoding="utf-8"))["scenes"]}
except Exception:
    _SC = {}


def _norm(w):
    return re.sub(r"[^\wà-ú]", "", w.lower())


def phrase_span(sid, phrase, t_a, t_b):
    """(início, fim) absolutos da frase dita na cena; fallback = intervalo (t_a, t_b)"""
    ws = [_norm(w) for w in phrase.split()]
    sc = _SC.get(sid)
    if sc and len(ws) >= 2:
        toks = sc["tokens"]
        n = len(ws)
        for i in range(len(toks) - 1):
            if [_norm(toks[i + j]["disp"]) for j in range(min(2, len(toks) - i))] == ws[:2]:
                j = min(i + n - 1, len(toks) - 1)
                return sc["start"] + toks[i]["t0"], sc["start"] + toks[j].get("t1", toks[j]["t0"] + 0.3)
    return t_a, t_b


def wreveal(t, span):
    return clamp((t - span[0]) / max(0.3, span[1] - span[0]))


# ======================================================================
# encomenda: caixa + etiqueta
# ======================================================================

def caixa(c, x, y, w, h, a, open_=0.0, inner=None, inner_a=0.0, label=None, label_a=1.0, shake=0.0):
    """caixa de papelão vista de frente; open_ abre as abas; inner = texto que sai de dentro"""
    if a <= 0:
        return
    c.save()
    if shake:
        c.translate(shake, 0)
    if open_ > 0:   # interior
        rrect(c, x + 8, y - 6, w - 16, 40, 6, mix(KRAFT, "#000000", 0.35), a)
    if inner and inner_a > 0:
        lift = 150 * ease_out(inner_a)
        lines = wrap(inner, "black", 26, w + 40)
        hh = len(lines) * 34 + 40
        rrect(c, x - 20, y - lift - hh + 60, w + 40, hh, 14, mix("#FFFFFF", BLUE, 0.10), a * inner_a, shadow=True)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x - 20, y - lift - hh + 60, w + 40, hh), 14, 14), paint(BLUE, a * inner_a, stroke=4))
        for j, ln in enumerate(lines):
            text(c, ln, x + w / 2, y - lift - hh + 60 + 44 + j * 34, 26, "black", BLUE, a * inner_a)
    rrect(c, x, y, w, h, 8, KRAFT, a, shadow=True)
    rrect(c, x + w / 2 - 40, y, 80, h, 0, mix(KRAFT, "#FFFFFF", 0.35), a * 0.7)
    # abas
    ang = 110 * ease_out(open_)
    if open_ <= 0:
        rrect(c, x - 6, y - 26, w + 12, 32, 6, mix(KRAFT, "#000000", 0.12), a)
    else:
        lw = w / 2
        for side in (-1, 1):
            c.save()
            px = x if side < 0 else x + w
            c.translate(px, y)
            c.rotate(-ang if side < 0 else ang)
            rrect(c, 0 if side < 0 else -lw, -26, lw, 30, 6, mix(KRAFT, "#000000", 0.12), a)
            c.restore()
    if label and label_a > 0:
        lw, lh_ = w * 0.7, h * 0.42
        rrect(c, x + w / 2 - lw / 2, y + h * 0.36, lw, lh_, 6, "#FFFFFF", a * label_a)
        for j in range(3):
            line(c, x + w / 2 - lw / 2 + 14, y + h * 0.36 + 26 + j * 22, x + w / 2 + lw / 2 - 14 - j * 30, y + h * 0.36 + 26 + j * 22, LIGHT, a * label_a, 5)
    c.restore()


def etiqueta(c, x, y, w, a, rows, title="DESTINATÁRIO"):
    """etiqueta de encomenda; rows = [(rótulo_campo, valor, alpha, cor_valor, pílula|None, alpha_pílula)]"""
    if a <= 0:
        return 0
    hrow = []
    for lab, val, ra, col, pl, pa in rows:
        lines = wrap(val, "black", 34, w - 80) if val else [""]
        hrow.append(52 + len(lines) * 44 + 18)
    h = 96 + sum(hrow) + 20
    rrect(c, x, y, w, h, 18, "#FFFFFF", a, shadow=True)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x + 10, y + 10, w - 20, h - 20), 12, 12), paint(LIGHT, a, stroke=2))
    # código de barras
    bx = x + w - 260
    for k in range(34):
        ww = 3 if k % 3 else 6
        c.drawRect(skia.Rect.MakeXYWH(bx + k * 6.5, y + 30, ww, 44), paint(INK, a * 0.85))
    text(c, title, x + 40, y + 66, 22, "black", GRAY, a, align="left", tracking=2)
    yy = y + 96
    for (lab, val, ra, col, pl, pa), hh in zip(rows, hrow):
        line(c, x + 30, yy, x + w - 30, yy, LINE, a, 2)
        if ra > 0:
            text(c, lab, x + 40, yy + 38, 20, "black", GRAY, a * ra, align="left", tracking=1.5)
            if pl and pa > 0:
                pill(c, pl, x + w - 40, yy + 30, BLUE, size=22, a=a * ra * pa, anchor="right", bounds=(0, 1920))
            if val:
                para(c, val, x + 40, yy + 86, 34, "black", col, a * ra, w - 80, 44)
        yy += hh
    return h


def truck(c, x, y, a, col=None, s=1.0):
    if a <= 0:
        return
    col = col or BLUE
    rrect(c, x, y, 150 * s, 80 * s, 10 * s, col, a, shadow=True)
    rrect(c, x + 150 * s, y + 24 * s, 62 * s, 56 * s, 10 * s, mix(col, "#000000", 0.2), a)
    rrect(c, x + 166 * s, y + 32 * s, 30 * s, 20 * s, 4 * s, "#DCEBFF", a)
    for wx in (x + 34 * s, x + 170 * s):
        c.drawCircle(wx, y + 84 * s, 17 * s, paint(INK, a))
        c.drawCircle(wx, y + 84 * s, 7 * s, paint(LIGHT, a))


# ======================================================================
# proposta de redação estilizada
# ======================================================================

def proposta_page(c, x, y, w, h, a, hl=(0, 0, 0), dim=0.0, frase=True):
    """página com 3 zonas: 1 instruções · 2 textos motivadores · 3 comando + frase temática.
    hl = destaque (0–1) de cada zona; dim apaga as zonas não destacadas."""
    if a <= 0:
        return
    rrect(c, x, y, w, h, 14, "#FFFFFF", a, shadow=True)
    text(c, "PROPOSTA DE REDAÇÃO", x + w / 2, y + 48, 24, "black", INK, a, tracking=2)
    pad = 28
    zx, zw = x + pad, w - 2 * pad
    z1 = (y + 72, 92)
    z2 = (y + 72 + 92 + 16, h * 0.40)
    z3 = (z2[0] + z2[1] + 16, h - (z2[0] + z2[1] + 16 - y) - pad)
    zones = [z1, z2, z3]
    cols = [INK2, BLUE, PURPLE]
    m = max(hl) if hl else 0
    for k, ((zy, zh), col) in enumerate(zip(zones, cols)):
        za = a * (1 - dim * m * (1 - hl[k]))
        if hl[k] > 0:
            rrect(c, zx - 10, zy - 8, zw + 20, zh + 16, 12, mix("#FFFFFF", col, 0.10), a * hl[k])
            c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(zx - 10, zy - 8, zw + 20, zh + 16), 12, 12), paint(col, a * hl[k], stroke=4))
        if k == 0:
            text(c, "INSTRUÇÕES", zx, zy + 22, 16, "black", GRAY, za, align="left", tracking=1.5)
            for j in range(3):
                c.drawCircle(zx + 8, zy + 44 + j * 18, 4, paint(GRAY, za))
                line(c, zx + 22, zy + 44 + j * 18, zx + zw * (0.85 - 0.15 * j), zy + 44 + j * 18, LIGHT, za, 6)
        elif k == 1:
            text(c, "TEXTOS MOTIVADORES", zx, zy + 22, 16, "black", GRAY, za, align="left", tracking=1.5)
            bw = (zw - 2 * 14) / 3
            for j in range(3):
                bx = zx + j * (bw + 14)
                by, bh = zy + 38, zh - 46
                rrect(c, bx, by, bw, bh, 8, "#F4F5F7", za)
                text(c, "TEXTO " + "I" * (j + 1), bx + bw / 2, by + 24, 14, "black", GRAY, za, tracking=1)
                if j == 0:
                    for q in range(5):
                        line(c, bx + 12, by + 46 + q * 16, bx + bw - 12 - (q % 2) * 20, by + 46 + q * 16, LIGHT, za, 5)
                elif j == 1:
                    for q, hh in enumerate((0.35, 0.6, 0.45, 0.8)):
                        bhh = (bh - 60) * hh
                        rrect(c, bx + 16 + q * (bw - 32) / 4, by + bh - 12 - bhh, (bw - 32) / 4 - 8, bhh, 3, BLUE, za * 0.8)
                else:
                    c.drawCircle(bx + bw * 0.32, by + bh * 0.42, 12, paint(AMBER, za))
                    p = skia.Path()
                    p.moveTo(bx + 10, by + bh - 10); p.lineTo(bx + bw * 0.45, by + bh * 0.45); p.lineTo(bx + bw * 0.65, by + bh * 0.7)
                    p.lineTo(bx + bw * 0.8, by + bh * 0.55); p.lineTo(bx + bw - 10, by + bh - 10); p.close()
                    c.drawPath(p, paint(GREEN, za * 0.8))
        else:
            text(c, "COMANDO", zx, zy + 22, 16, "black", GRAY, za, align="left", tracking=1.5)
            for j in range(2):
                line(c, zx, zy + 46 + j * 18, zx + zw * (0.95 - 0.1 * j), zy + 46 + j * 18, LIGHT, za, 6)
            if frase:
                fy = zy + 82
                rrect(c, zx, fy, zw, min(zh - 92, 58), 10, mix("#FFFFFF", BLUE, 0.16), za)
                text_mid(c, "frase temática", zx + zw / 2, fy + min(zh - 92, 58) / 2, 20, "black", BLUE, za)
    return zones


# ======================================================================
# abertura
# ======================================================================

def comp_bars(c, x, y, a, cap=0.0, w=620):
    """5 competências (0–200); cap > 0 prende C2, C3 e C5 em 40"""
    if a <= 0:
        return
    for k in range(5):
        yy = y + k * 74
        text(c, f"C{k + 1}", x, yy + 14, 30, "black", INK2, a, align="left")
        rrect(c, x + 70, yy - 14, w, 34, 10, "#EDEDEA", a)
        capped = k in (1, 2, 4)
        full = w * (1 - (0.8 * cap if capped else 0))
        rrect(c, x + 70, yy - 14, full, 34, 10, RED if (capped and cap > 0.5) else GREEN, a * 0.85)
        if capped and cap > 0:
            text(c, "40", x + 70 + full + 16, yy + 14, 30, "black", RED, a * cap, align="left")
    text(c, "cada uma até 200", x + 70 + w, y - 40, 20, "bold", GRAY, a, align="right")


def b_hook(c, t, C, B):
    head(c, t, B["start"], "REDAÇÃO ENEM", "LEITURA DA PROPOSTA", BLUE)
    aa = ep(t, C["01.a"], 0.6)
    ab = ep(t, C["01.b"], 0.5)
    # proposta (à esquerda) e folha em branco
    proposta_page(c, 200, 190, 520, 620, aa, hl=(0, 0, 0))
    if aa > 0:
        rrect(c, 760, 230, 260, 560, 10, PAPER, aa * (1 - ab), shadow=True)
        for j in range(12):
            line(c, 780, 290 + j * 42, 1000, 290 + j * 42, PAPER_LINE, aa * (1 - ab), 2)
        text(c, "linha 1", 890, 276, 18, "bold", GRAY, aa * (1 - ab))
        pill(c, "começa AQUI", 460, 160, GREEN, size=26, a=aa * (1 - ab), anchor="center", bounds=(0, 1920))
    # leitura errada → competências presas
    lupa = ab * (1 - ep(t, C["01.c"], 0.4))
    if lupa > 0:
        cx, cy = 460 + 40 * math.sin(t * 1.6), 560
        c.drawCircle(cx, cy, 70, paint(RED, lupa * 0.12))
        c.drawCircle(cx, cy, 70, paint(RED, lupa, stroke=8))
        line(c, cx + 50, cy + 50, cx + 110, cy + 110, RED, lupa, 14)
        pill(c, "erro na leitura", 460, 700, RED, size=26, a=lupa, anchor="center", bounds=(0, 1920))
    cap = ep(t, C["01.b"] + 1.6, 0.8)
    comp_bars(c, 900, 330, ab, cap, 600)
    ac = ep(t, C["01.c"], 0.4)
    selo(c, 1240, 520, ac, "NOTA ZERO", RED, -8, 60)
    ad = ep(t, C["01.d"], 0.5)
    pill(c, "mesmo escrevendo muito bem", 1240, 770, AMBER, size=30, a=ad, anchor="center", bounds=(0, 1920))


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "AO FINAL DESTA AULA", "VOCÊ VAI CONSEGUIR", GREEN)
    rows = [("02.a", "saber o que a prova PEDE", "exatamente"), ("02.b", "separar ASSUNTO, TEMA e TESE", "de qualquer proposta")]
    for j, (cue, s, sub) in enumerate(rows):
        a, d = rise(t, C[cue])
        y = 330 + j * 190 + d
        check_icon(c, 330, y - 14, 36, a, GREEN)
        text(c, s, 400, y, 54, "black", INK, a, align="left")
        text(c, sub, 400, y + 56, 32, "bold", GRAY, a, align="left")
    pill(c, "cada palavra nova vai ser explicada", W / 2, 760, BLUE, size=30, a=ep(t, C["02.c"], 0.5), anchor="center")


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "PRÉ-REQUISITOS", "NENHUM", GREEN)
    a0 = ep(t, C["03.t"], 0.5)
    text(c, "0", 470, 560, 300, "black", GREEN, a0)
    aa, dy = rise(t, C["03.a"])
    text(c, "nunca escreveu uma redação?", 760, 360 + dy, 40, "black", INK2, aa, align="left")
    text(c, "começamos do zero", 760, 412 + dy, 34, "bold", GREEN, aa, align="left")
    ab = ep(t, C["03.b"], 0.5)
    if ab > 0:
        rrect(c, 760, 480, 820, 110, 20, "#F7F7F5", ab)
        text(c, "VIU A SÉRIE DE LINGUAGENS?", 790, 522, 20, "black", GRAY, ab, align="left", tracking=1.5)
        text(c, "Compreensão global e tese", 790, 568, 34, "black", BLUE, ab, align="left")
    ac = ep(t, C["03.c"], 0.6)
    if ac > 0:
        rrect(c, 760, 640, 820, 40, 20, "#EDEDEA", ac)
        rrect(c, 760, 640, 410 * ep(t, C["03.c"] + 0.2, 0.8), 40, 20, GREEN, ac)
        text(c, "meio caminho andado", 1170, 730, 34, "black", GREEN, ac)


# ======================================================================
# bloco A — o que o ENEM pede
# ======================================================================

def b_pede(c, t, C, B):
    head_seq(c, t, C, [("04", "O QUE A PROVA", "DE REDAÇÃO PEDE?", BLUE), ("05", "1 · O TIPO DE TEXTO", "DISSERTATIVO-ARGUMENTATIVO", BLUE),
                       ("06", "2 · O RECORTE", "A FRASE TEMÁTICA", BLUE)])
    card(c, *CARD_R)
    sid = which(t, C, ["04", "05", "06"])
    if sid == "04":
        a4 = fw(t, C["04.a"], C["05"])
        person(c, 380, 330, LIGHT, a4)
        bubble(c, "um texto sobre um assunto", 470, 250, 640, "#F2F2EF", a4, True, 38, INK)
        ab = ep(t, C["04.b"], 0.5)
        if ab > 0:
            paper(c, 560, 440, 760, 300, ab, lh=50, top=520)
            hand(c, "Escreva sobre a velhice.", 680, 530, 44, PEN, ab, wreveal(t, phrase_span("04", "escreva sobre a velhice.", C["04.b"], C["04.c"])))
        pill(c, "parece certo...", 1500, 470, AMBER, size=30, a=ep(t, C["04.c"], 0.4), anchor="center", bounds=(0, 1920))
        ad = ep(t, C["04.d"], 0.4)
        xmark(c, 940, 600, 120, ad, RED, 16)
        selo(c, 1500, 640, ad, "NÃO É ISSO", RED, -6, 40)
    elif sid == "05":
        a0 = ep(t, C["05.a"], 0.5)
        boxed(c, 300, 200, 1320, 120, BLUE, a0, 0.08)
        text_mid(c, "texto dissertativo-argumentativo", W / 2, 260, 58, "black", BLUE, a0)
        ab = ep(t, C["05.b"], 0.5)
        if ab > 0:
            pill(c, "PONTO DE VISTA", W / 2, 420, BLUE, size=34, a=ab, anchor="center")
            for k, xx in enumerate((520, 960, 1400)):
                aa = ab * ep(t, C["05.b"] + 0.3 + 0.25 * k, 0.4)
                rrect(c, xx - 150, 530, 300, 70, 16, "#F7F7F5", aa)
                text_mid(c, f"argumento {k + 1}", xx, 565, 28, "black", INK2, aa)
                arrow(c, xx, 525, lerp(xx, W / 2, 0.6), 450, GREEN, aa, 4, 14, progress=aa)
        ac = ep(t, C["05.c"], 0.5)
        if ac > 0:
            # prosa × versos
            rrect(c, 420, 650, 380, 160, 12, "#FFFFFF", ac, shadow=True)
            for j in range(4):
                line(c, 450 + (30 if j in (0, 2) else 0), 685 + j * 30, 770, 685 + j * 30, LIGHT, ac, 7)
            check_icon(c, 830, 730, 24, ac, GREEN)
            text(c, "parágrafos", 870, 742, 30, "black", GREEN, ac, align="left")
            rrect(c, 1120, 650, 380, 160, 12, "#FFFFFF", ac * 0.6, shadow=True)
            for j in range(4):
                line(c, 1240, 685 + j * 30, 1240 + (120 if j % 2 else 160), 685 + j * 30, LIGHT, ac * 0.6, 7)
            xmark(c, 1310, 730, 50, ep(t, C["05.c"] + 0.8, 0.4), RED, 8)
            text(c, "versos", 1310, 840, 26, "black", RED, ac * 0.8)
    else:
        aa = ep(t, C["06.a"], 0.5)
        pill(c, "FRASE TEMÁTICA", W / 2, 230, BLUE, size=36, a=aa, anchor="center")
        text(c, "diz exatamente sobre o que escrever", W / 2, 310, 34, "bold", INK2, aa)
        ab = ep(t, C["06.b"], 0.4)
        pill(c, "ENEM 2025", 330, 410, INK2, size=26, a=ab, bounds=(0, 1920))
        ac = ep(t, C["06.c"], 0.6)
        boxed(c, 300, 450, 1320, 150, BLUE, ac, 0.10)
        para(c, "“" + TEMA25 + "”", W / 2, 512, 46, "black", BLUE, ac, 1240, 58, align="center")
        ad = ep(t, C["06.d"], 0.5)
        text(c, "velhice", 620, 730, 46, "black", INK2, ad)
        if ad > 0:
            strike(c, 530, 714, 710, 714, ad, RED, ep(t, C["06.d"] + 0.3, 0.4))
        check_icon(c, 1060, 714, 30, ep(t, C["06.d"] + 1.0, 0.4), GREEN)
        text(c, "esse recorte", 1110, 730, 46, "black", GREEN, ep(t, C["06.d"] + 1.0, 0.4), align="left")


# ======================================================================
# bloco B — as três partes da proposta
# ======================================================================

def cartilha(c, x, y, a, inep=0.0, s=1.0):
    if a <= 0:
        return
    w, h = 300 * s, 400 * s
    rrect(c, x + 12 * s, y + 12 * s, w, h, 14, mix(PURPLE, "#000000", 0.25), a)
    rrect(c, x, y, w, h, 14, PURPLE, a, shadow=True)
    rrect(c, x, y, 28 * s, h, 10, mix(PURPLE, "#000000", 0.18), a)
    text(c, "CARTILHA", x + w / 2 + 12, y + 120 * s, 34 * s, "black", "#FFFFFF", a)
    text(c, "DO", x + w / 2 + 12, y + 162 * s, 26 * s, "black", "#FFFFFF", a)
    text(c, "PARTICIPANTE", x + w / 2 + 12, y + 202 * s, 30 * s, "black", "#FFFFFF", a)
    text(c, "REDAÇÃO ENEM", x + w / 2 + 12, y + 260 * s, 20 * s, "bold", "#E6DEFF", a, tracking=1)
    if inep > 0:
        pill(c, "Inep", x + w / 2 + 12, y + h - 60 * s, "#FFFFFF", PURPLE, size=28 * s, a=a * inep, anchor="center", bounds=(0, 1920))


CALLOUT = {
    "11": (0, "1 · INSTRUÇÕES", "= regras da casa", ["limite de linhas", "uso do rascunho", "o que pode ANULAR"], INK2),
    "12": (1, "2 · TEXTOS MOTIVADORES", "= fotos de referência", ["notícias · dados · gráficos · imagens", "mostram a SITUAÇÃO-PROBLEMA", "entender ✓   copiar ✗"], BLUE),
    "13": (2, "3 · COMANDO", "= pedido exato", ["o que você tem que fazer"], PURPLE),
}


def b_proposta(c, t, C, B):
    ids = [i for i in ("07", "08", "09", "11", "12", "13", "14") if B["start"] - 0.05 <= C[i] < B["end"]]
    heads = {"07": ("ONDE FICA A FRASE?", "A PROPOSTA DE REDAÇÃO", BLUE), "08": ("QUEM EXPLICA", "A CARTILHA DO PARTICIPANTE", PURPLE),
             "09": ("SEGUNDO A CARTILHA", "TRÊS PARTES", PURPLE), "11": ("NA PROPOSTA É IGUAL", "AS INSTRUÇÕES", INK2),
             "12": ("NA PROPOSTA É IGUAL", "OS TEXTOS MOTIVADORES", BLUE), "13": ("NA PROPOSTA É IGUAL", "O COMANDO", PURPLE),
             "14": ("REPARE NO PERIGO", "LEIA AS TRÊS PARTES", RED)}
    head_seq(c, t, C, [(i, *heads[i]) for i in ids])
    card(c, *CARD_R)
    sid = which(t, C, ids)
    if "07" in ids:
        # 1ª parte do bloco: página → cartilha → três partes
        a0 = ep(t, C["07.a"], 0.6)
        a8 = ep(t, C["08"], 0.6)
        px = lerp(700, 980, a8)
        proposta_page(c, px, 180, 560, 640, a0, hl=tuple(ep(t, C["09.b"] + 0.5 * k, 0.4) for k in range(3)) if t > C["09.b"] else (0, 0, 0))
        text(c, "tudo o que você", 420, 480, 34, "black", BLUE, a0 * (1 - a8))
        text(c, "precisa para escrever", 420, 524, 34, "black", BLUE, a0 * (1 - a8))
        ac = ep(t, C["08.t"] + 0.6, 0.6)
        cartilha(c, 330, 230, ac, ep(t, C["09.a"], 0.5))
        text(c, "o guia oficial", 480, 690, 30, "black", PURPLE, ep(t, C["08.a"], 0.5))
        text(c, "da redação", 480, 730, 30, "black", PURPLE, ep(t, C["08.a"], 0.5))
        ai = ep(t, C["09.a"], 0.5) * (1 - ep(t, C["09.b"], 0.4))
        text(c, "Inep = órgão do governo", 480, 790, 24, "bold", INK2, ai)
        text(c, "que organiza o ENEM", 480, 822, 24, "bold", INK2, ai)
        if t > C["09.b"]:
            for k, (zy, lab) in enumerate(((180 + 72 + 46, "1"), (180 + 72 + 92 + 16 + 128, "2"), (180 + 72 + 92 + 16 + 256 + 16 + 90, "3"))):
                badge_num(c, lab, px + 600, zy, ep(t, C["09.b"] + 0.5 * k, 0.4), 30, bg=(INK2, BLUE, PURPLE)[k])
        return
    # 2ª parte do bloco (depois do bolo): página à esquerda + cartão explicativo à direita
    hl = [0, 0, 0]
    if sid in CALLOUT:
        hl[CALLOUT[sid][0]] = ep(t, C[sid], 0.5)
    proposta_page(c, 220, 180, 560, 640, 1.0, hl=tuple(hl), dim=0.6)
    if sid in CALLOUT:
        k, tt, sub, items, col = CALLOUT[sid]
        a, d = rise(t, C[sid])
        x0 = 860
        rrect(c, x0, 210 + d, 820, 560, 24, mix("#FFFFFF", col, 0.06), a, shadow=True)
        c.drawRect(skia.Rect.MakeXYWH(x0, 210 + d, 12, 560), paint(col, a))
        text(c, tt, x0 + 50, 290 + d, 44, "black", col, a, align="left")
        text(c, sub, x0 + 50, 345 + d, 32, "bold", GRAY, a, align="left")
        cues = {"11": ["11.b", "11.b", "11.c"], "12": ["12.b", "12.c", "12.d"], "13": ["13.a"]}[sid]
        for j, (s, cu) in enumerate(zip(items, cues)):
            aj = ep(t, C[cu] + (0.6 * j if sid == "11" and j < 2 else 0), 0.4) * a
            yy = 450 + j * 95 + d
            if "✓" in s:
                check_icon(c, x0 + 70, yy - 12, 20, aj, GREEN)
                text(c, "entender", x0 + 104, yy, 36, "black", GREEN, aj, align="left")
                check_icon(c, x0 + 330, yy - 12, 20, aj, RED, "x")
                text(c, "copiar", x0 + 364, yy, 36, "black", RED, aj, align="left")
                continue
            c.drawCircle(x0 + 70, yy - 12, 9, paint(col, aj))
            tc = RED if "ANULAR" in s else (BLUE if "SITUAÇÃO" in s else INK)
            text(c, s, x0 + 100, yy, 36 if len(s) < 30 else 32, "black", tc, aj, align="left")
        # ícone do bolo correspondente
        if sid == "13":
            ticket(c, x0 + 410, 560 + d, a * ep(t, C["13.a"] + 0.6, 0.5), s=0.9)
    if sid == "14":
        rows = [("14.a", "só a frase temática", "perde as REGRAS"), ("14.b", "só os textos motivadores", "risco de COPIAR")]
        for j, (cu, s1, s2) in enumerate(rows):
            a, d = rise(t, C[cu])
            yy = 300 + j * 230 + d
            if a <= 0:
                continue
            rrect(c, 860, yy - 60, 820, 180, 22, mix("#FFFFFF", RED, 0.07), a, shadow=True)
            text(c, "quem lê", 900, yy - 10, 26, "bold", GRAY, a, align="left")
            text(c, s1, 900, yy + 34, 38, "black", INK, a, align="left")
            check_icon(c, 920, yy + 82, 18, a, RED, "x")
            text(c, s2, 952, yy + 94, 34, "black", RED, a, align="left")


# ======================================================================
# encomenda de bolo
# ======================================================================

def bolo(c, cx, by, a, s=1.0, col="#6B3E26", top="#F6D7B0", andares=2):
    if a <= 0:
        return
    w = 200 * s
    rrect(c, cx - w * 0.75, by - 10 * s, w * 1.5, 16 * s, 8 * s, LIGHT, a)
    y = by - 10 * s
    for k in range(andares):
        ww = w * (1 - 0.3 * k)
        hh = 70 * s
        rrect(c, cx - ww / 2, y - hh, ww, hh, 10 * s, col, a)
        rrect(c, cx - ww / 2, y - hh, ww, 16 * s, 8 * s, top, a)
        y -= hh
    c.drawCircle(cx, y - 10 * s, 12 * s, paint(RED, a))


def ticket(c, x, y, a, s=1.0):
    if a <= 0:
        return
    w, h = 300 * s, 230 * s
    rrect(c, x, y, w, h, 10, "#FFF8E1", a, shadow=True)
    text(c, "PEDIDO", x + w / 2, y + 40 * s, 22 * s, "black", AMBER, a, tracking=2)
    for j, s_ in enumerate(("chocolate", "2 andares", "para sábado")):
        check_icon(c, x + 36 * s, y + (86 + j * 46) * s, 12 * s, a, GREEN)
        text(c, s_, x + 60 * s, y + (96 + j * 46) * s, 28 * s, "black", INK, a, align="left")


def b_bolo(c, t, C, B):
    frame(c, t, B["start"], "PENSE NUMA ENCOMENDA", "DE BOLO", GREEN)
    xs = (420, 960, 1500)
    labs = (("10.a", "REGRAS DA CASA"), ("10.b", "FOTOS DE REFERÊNCIA"), ("10.c", "PEDIDO EXATO"))
    ad = ep(t, C["10.d"], 0.5)
    for k, ((cu, lab), x) in enumerate(zip(labs, xs)):
        a, d = rise(t, C[cu])
        if a <= 0:
            continue
        al = a * (1 - 0.6 * ad if k != 1 else 1)
        rrect(c, x - 230, 220 + d, 460, 480, 24, "#FFFFFF", al, shadow=True)
        text(c, lab, x, 280 + d, 28, "black", INK2, al, tracking=1)
        if k == 0:
            rrect(c, x - 120, 330 + d, 240, 300, 12, "#F4F1EA", al)
            rrect(c, x - 50, 316 + d, 100, 30, 8, GRAY, al)
            for j, s_ in enumerate(("prazo", "tamanho máx.")):
                c.drawCircle(x - 80, 412 + j * 70 + d, 8, paint(INK2, al))
                text(c, s_, x - 60, 422 + j * 70 + d, 30, "bold", INK, al, align="left")
        elif k == 1:
            for j in range(2):
                c.save(); c.translate(x - 70 + j * 140, 470 + d); c.rotate(-8 + 16 * j)
                rrect(c, -100, -130, 200, 240, 8, "#FFFFFF", al, shadow=True)
                rrect(c, -86, -116, 172, 170, 4, "#E8EEF9", al)
                bolo(c, 0, 40, al, 0.55)
                c.restore()
        else:
            ticket(c, x - 150, 330 + d, al)
            bolo(c, x, 680 + d, al * ep(t, C["10.c"] + 1.2, 0.5), 0.55)
    selo(c, 960, 640, ad, "ERRA O BOLO", RED, -6, 44)


# ======================================================================
# bloco C — o comando, trecho por trecho (rascunho + competências)
# ======================================================================

TRECHOS = [("A partir da leitura dos textos motivadores", "17", "C2", BLUE),
           ("e com base nos conhecimentos construídos ao longo de sua formação,", "18", "C2 · C3", BLUE),
           ("redija texto dissertativo-argumentativo", "19", "C2", BLUE),
           ("em modalidade escrita formal da língua portuguesa", "20", "C1", BLUE),
           ("sobre o tema…", "21", "C2 · C3 · C5", BLUE),
           ("+ proposta de intervenção", "22", "C5", BLUE)]
COMP = [("C1", "escrita formal", "20.d"), ("C2", "compreender a proposta", "17.c"), ("C3", "organizar argumentos", "18.d"),
        ("C4", "coesão", "23.b"), ("C5", "proposta de intervenção", "22.c")]
NOTA = {"17": ("entender a situação-problema", None),
        "18": ("repertório sociocultural", "o que você sabe e leva para o texto"),
        "19": ("defender um ponto de vista", None),
        "20": ("norma-padrão", "português das regras da gramática · sem “tipo”, “né”"),
        "21": ("discutir o recorte POR INTEIRO", None),
        "22": ("proposta de intervenção", "ação concreta para o problema · respeitando os direitos humanos"),
        "23": ("coesão", "as palavras que costuram uma ideia na outra")}
RX, RY, RW, RH = 160, 170, 1010, 670
HS, HLH = 33, 54
_TL = {}


def trecho_layout():
    if "l" in _TL:
        return _TL["l"]
    out, yy = [], RY + 104
    for s, sid, comp, col in TRECHOS:
        lines = hwrap(s, HS, RW - 250)
        out.append((lines, yy))
        yy += len(lines) * HLH
    _TL["l"] = out
    return out


def b_comando(c, t, C, B):
    sid = which(t, C, [f"{k}" for k in range(15, 24)])
    heads = {"15": ("O COMANDO", "CADA PEDAÇO É UMA EXIGÊNCIA", PURPLE), "16": ("CADA EXIGÊNCIA →", "UMA COMPETÊNCIA", PURPLE)}
    l1, l2, col = heads.get(sid, ("O COMANDO", "TRECHO POR TRECHO", PURPLE))
    head(c, t, C["15"] if sid in ("15",) else C["16"] if sid == "16" else C["17"], l1, l2, col)
    paper(c, RX, RY, RW, RH, 1.0, lh=HLH, top=RY + 104 - 40)
    pill(c, "Cartilha do Participante", RX + 110, RY + 44, PURPLE, size=20, a=ep(t, C["15.b"], 0.4), bounds=(0, 1920))
    lay = trecho_layout()
    qa, qb = C["15.q"], C["15.end"] - 0.4
    total = sum(len(s) for s, *_ in TRECHOS[:5])
    acc = 0
    for k, ((s, ts, comp, tc), (lines, yy)) in enumerate(zip(TRECHOS, lay)):
        if k < 5:
            sp = (lerp(qa, qb, acc / total), lerp(qa, qb, (acc + len(s)) / total))
            acc += len(s)
            rv = wreveal(t, sp)
            ink = PEN
        else:
            rv = ep(t, C["22.a"], 1.6)
            ink = GREEN
        cur = sid == ts
        done = t >= C[ts + ".a"] - 0.05 if ts + ".a" in C else False
        ua = ep(t, C[ts + ".a"], 0.3) if (ts + ".a") in C else 0
        for j, ln in enumerate(lines):
            lw = hand_w(ln, HS)
            if ua > 0:
                hlc = AMBER if cur else mix(AMBER, "#FFFFFF", 0.5)
                rrect(c, RX + 96, yy + j * HLH - HS * 0.95, lw + 16, HS * 1.25, 6, hlc, ua * (0.30 if cur else 0.16))
                underline(c, RX + 98, RX + 98 + lw + 10, yy + j * HLH + 10, PURPLE if cur else LIGHT, ua, prog(t, C[ts + ".a"], 0.6), 4)
        nr = sum(len(l) for l in lines)
        done_ch = rv * nr
        for j, ln in enumerate(lines):
            r = clamp(done_ch / max(1, len(ln)))
            hand(c, ln, RX + 104, yy + j * HLH, HS, ink, 1.0, r)
            done_ch -= len(ln)
        # nota de margem (→ C2)
        ma = ep(t, C[ts + ".c"] if ts + ".c" in C else C[ts + ".b"], 0.4) if ts in ("17", "18", "19", "20", "21", "22") else 0
        if ts == "18":
            ma = ep(t, C["18.d"], 0.4)
        elif ts == "20":
            ma = ep(t, C["20.d"], 0.4)
        elif ts == "21":
            ma = ep(t, C["21.c"], 0.4)
        elif ts == "22":
            ma = ep(t, C["22.c"], 0.4)
        elif ts == "19":
            ma = ep(t, C["19.c"], 0.4)
        if ma > 0:
            ly = yy + (len(lines) - 1) * HLH
            hand(c, "→ " + comp, RX + RW - 30, ly, 30, PURPLE, ma, 1.0, align="right", bold=True)
    # nota (definição do trecho atual) — post-it
    if sid in NOTA:
        tt, sub = NOTA[sid]
        cue0 = {"17": "17.b", "18": "18.b", "19": "19.b", "20": "20.b", "21": "21.b", "22": "22.a", "23": "23.b"}[sid]
        a, d = rise(t, C[cue0])
        if a > 0:
            ny = RY + RH - 150
            rrect(c, RX + 40, ny + d, RW - 80, 124, 10, "#EAF1FF", a, shadow=True)
            c.drawRect(skia.Rect.MakeXYWH(RX + 40, ny + d, 10, 124), paint(BLUE, a))
            text(c, tt, RX + 80, ny + 52 + d, 36, "black", BLUE, a, align="left")
            if sub:
                sa = ep(t, C[{"18": "18.c", "20": "20.c", "22": "22.b", "23": "23.b"}.get(sid, cue0)] + 0.3, 0.4) * a
                text(c, sub, RX + 80, ny + 98 + d, 26, "bold", INK2, sa, align="left")
    # competências à direita
    a16 = ep(t, C["16.a"], 0.5)
    x0, w0 = 1210, 560
    for k, (cn, lab, cue) in enumerate(COMP):
        y = 178 + k * 132
        ak = a16 * ep(t, C["16.a"] + 0.15 * k, 0.4)
        if ak <= 0:
            continue
        lit = ep(t, C[cue], 0.4)
        flash = 0.0
        if sid == "21" and cn in ("C2", "C3", "C5"):
            flash = ep(t, C["21.c"], 0.3) * (0.5 + 0.5 * math.sin((t - C["21.c"]) * 8)) * (1 - prog(t, C["21.c"] + 2.2, 0.4))
        if sid == "16" and t > C["16.c"]:
            flash = 0.35
        on_ = max(lit, flash)
        rrect(c, x0, y, w0, 112, 18, mix("#FFFFFF", PURPLE, 0.10 * on_), ak, shadow=True)
        if on_ > 0:
            c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x0, y, w0, 112), 18, 18), paint(PURPLE, ak * on_, stroke=4))
        c.drawCircle(x0 + 62, y + 56, 38, paint(PURPLE if on_ > 0.3 else LIGHT, ak))
        text_mid(c, cn, x0 + 62, y + 56, 30, "black", "#FFFFFF", ak)
        text(c, lab, x0 + 118, y + 52, 28, "black", INK, ak * lit, align="left")
        text(c, "até 200 pontos", x0 + 118, y + 88, 20, "bold", GRAY, ak * ep(t, C["16.b"], 0.4), align="left")
    text(c, "hoje: só uma frase de cada", x0 + w0 / 2, 860, 24, "black", GREEN, fw(t, C["16.d"], C["17"]))
    if sid == "23":
        ac = ep(t, C["23.a"], 0.4)
        text(c, "não aparece no comando", x0 + w0 / 2, 860, 24, "black", GRAY, ac)


# ======================================================================
# bloco D — assunto × tema: a etiqueta de encomenda
# ======================================================================

def b_endereco(c, t, C, B):
    head_seq(c, t, C, [("24", "ASSUNTO E TEMA", "NÃO SÃO A MESMA COISA?", BLUE), ("25", "A FRASE TEMÁTICA =", "ENDEREÇO DE ENTREGA COMPLETO", BLUE),
                       ("26", "O TEMA =", "O ENDEREÇO EXATO", BLUE), ("27", "A CARTILHA CONFIRMA", "TEMA = RECORTE DO ASSUNTO", PURPLE)])
    card(c, *CARD_R)
    sid = which(t, C, ["24", "25", "26", "27"])
    a27 = ep(t, C["27"], 0.6)
    aa = ep(t, C["24.a"], 0.5)
    # caixa à esquerda
    sh = 0.0
    if C["24.c"] < t < C["24.d"] + 1.0:
        u = t - C["24.c"]
        sh = 6 * math.sin(u * 22) * math.exp(-u * 1.5)
    caixa(c, 230, 400, 360, 300, aa * (1 - a27), label="x", label_a=1.0, shake=sh)
    # etiqueta
    if sid == "24":
        rows = [("CIDADE", "São Paulo", ep(t, C["24.b"], 0.5), INK, None, 0),
                ("RUA · NÚMERO · BAIRRO", "", ep(t, C["24.d"], 0.4), INK, None, 0)]
        h = etiqueta(c, 720, 220, 900, aa, rows)
        ad = ep(t, C["24.d"], 0.4)
        if ad > 0:
            for k, s in enumerate(("rua?", "número?", "bairro?")):
                pill(c, s, 800 + k * 240, 220 + h - 70, AMBER, size=28, a=ad * ep(t, C["24.d"] + 0.4 * k + 0.6, 0.3), bounds=(0, 1920))
        text_mid(c, "?", 410, 300, 110, "black", AMBER, ep(t, C["24.c"], 0.3) * (1 - ad))
        selo(c, 410, 770, ad, "NÃO CHEGA", RED, -6, 36)
    elif sid in ("25", "26"):
        ab = ep(t, C["25.b"], 0.5)
        r2 = ep(t, C["26.a"], 0.5)
        rows = [("CIDADE", "envelhecimento" if t > C["25.c"] - 0.1 else "", ab, BLUE, "ASSUNTO", ep(t, C["25.b"] + 0.4, 0.4)),
                ("ENDEREÇO COMPLETO", TEMA25 if t > C["26.b"] - 0.1 else "", r2, BLUE, "TEMA", ep(t, C["26.a"] + 0.4, 0.4))]
        etiqueta(c, 720, 200, 900, ep(t, C["25.a"], 0.5), rows)
        sub = ep(t, C["25.b"], 0.4) * (1 - r2)
        text(c, "a área ampla", 1170, 800, 32, "bold", INK2, sub)
        ac = ep(t, C["26.c"], 0.5)
        if ac > 0:
            truck(c, 1000, 690, ac, AMBER, 0.8)
            pill(c, "parada na cidade", 1260, 730, AMBER, size=28, a=ac, bounds=(0, 1920))
    if a27 > 0:
        aq = ep(t, C["27.a"], 0.5)
        boxed(c, 260, 220, 1400, 200, PURPLE, aq, 0.08)
        text(c, "CARTILHA DO PARTICIPANTE", 300, 266, 20, "black", PURPLE, aq, align="left", tracking=2)
        para(c, "o tema “se caracteriza por ser uma delimitação de um assunto mais abrangente”", 300, 324, 40, "black", INK, aq, 1320, 52)
        ab = ep(t, C["27.b"], 0.5)
        if ab > 0:
            # círculo grande (assunto) e o pedaço recortado (tema)
            c.drawCircle(700, 640, 150, paint(mix("#FFFFFF", INK2, 0.12), ab))
            text_mid(c, "ASSUNTO", 660, 640, 30, "black", INK2, ab)
            cut = ep(t, C["27.b"] + 0.5, 0.7)
            pth = skia.Path()
            pth.moveTo(700, 640); pth.arcTo(skia.Rect.MakeLTRB(550, 490, 850, 790), -30, 60, False); pth.close()
            c.drawPath(pth, paint("#FFFFFF", ab * cut))
            c.save(); c.translate(cut * 140, 0)
            c.drawPath(pth, paint(BLUE, ab))
            c.restore()
            text(c, "TEMA", 800 + cut * 140, 760, 30, "black", BLUE, ab * cut, align="center")
            text(c, "delimitação", 1300, 620, 40, "black", INK2, ab)
            text(c, "= RECORTE", 1300, 680, 52, "black", BLUE, ab)


# ======================================================================
# tabela de temas (seção 03)
# ======================================================================

TAB = [("2016", "intolerância religiosa", "Caminhos para combater a intolerância religiosa no Brasil", "28.a"),
       ("2017", "educação de pessoas surdas", TEMA17, None),
       ("2020", "saúde mental", TEMA20, "28.b"),
       ("2022", "povos e comunidades tradicionais", TEMA22, None),
       ("2025", "envelhecimento", TEMA25, "28.c")]


def tabela(c, t, C, a, fill17=0.0, fill22=0.0, d_hl=0.0, q_pulse=0.0):
    if a <= 0:
        return
    xs = (200, 360, 800)
    text(c, "ANO", xs[0] + 10, 225, 22, "black", GRAY, a, align="left", tracking=1.5)
    text(c, "ASSUNTO · a cidade", xs[1] + 10, 225, 22, "black", GRAY, a, align="left", tracking=1.5)
    text(c, "TEMA · o endereço completo", xs[2] + 10, 225, 22, "black", BLUE, a, align="left", tracking=1.5)
    line(c, 190, 248, 1730, 248, LINE, a, 3)
    for k, (ano, ass, tema, cue) in enumerate(TAB):
        y = 300 + k * 108
        if cue:
            ra, d = rise(t, C[cue])
        else:
            ra, d = ep(t, C["28.t"] + 0.4, 0.5), 0
            if fill17 > 0 and ano == "2017":
                ra = 1
            if fill22 > 0 and ano == "2022":
                ra = 1
        ra *= a
        if ra <= 0:
            continue
        filled = (cue is not None) or (ano == "2017" and fill17 > 0) or (ano == "2022" and fill22 > 0)
        fa = 1 if cue else (fill17 if ano == "2017" else fill22)
        text(c, ano, xs[0] + 10, y + d, 34, "black", INK, ra, align="left")
        if filled:
            para(c, ass, xs[1] + 10, y + d, 28, "bold", INK2, ra * fa, 400, 34)
            para(c, tema, xs[2] + 10, y + d, 28, "black", BLUE, ra * fa, 920, 34)
        if not cue:
            qa = ra * (1 - fa)
            pul = 1 + 0.06 * math.sin(t * 5) * q_pulse
            for xx in (xs[1] + 60, xs[2] + 60):
                c.save(); c.translate(xx, y - 10 + d); c.scale(pul, pul)
                pill(c, "?", 0, 0, AMBER, size=30, a=qa, anchor="center", bounds=(0, 1920))
                c.restore()
        line(c, 190, y + 50 + d, 1730, y + 50 + d, LINE, ra, 2)
    if d_hl > 0:
        boxed(c, xs[1] - 4, 260, 430, 540, INK2, d_hl, 0.0, 16, 4)
        boxed(c, xs[2] - 4, 260, 940, 540, BLUE, d_hl, 0.0, 16, 4)
        pill(c, "2 ou 3 palavras", xs[1] + 210, 830, INK2, size=24, a=d_hl, anchor="center", bounds=(0, 1920))
        pill(c, "a frase inteira", xs[2] + 470, 830, BLUE, size=24, a=d_hl, anchor="center", bounds=(0, 1920))


def b_tabela(c, t, C, B):
    frame(c, t, B["start"], "EM PROVAS DE VERDADE", "ASSUNTO × TEMA", BLUE)
    tabela(c, t, C, ep(t, C["28.t"], 0.4), d_hl=ep(t, C["28.d"], 0.5) * (1 - ep(t, C["28.e"], 0.4)), q_pulse=ep(t, C["28.e"], 0.4))
    ab = ep(t, C["28.b2"], 0.4) * (1 - ep(t, C["28.c"], 0.4))
    pill(c, "estigma = rótulo de preconceito", 1300, 860, AMBER, size=24, a=ab, anchor="center", bounds=(0, 1920))
    pill(c, "quem preenche é VOCÊ", 1300, 860, GREEN, size=26, a=ep(t, C["28.e"] + 0.6, 0.4), anchor="center", bounds=(0, 1920))


# ======================================================================
# bloco E — aviso de nomenclatura
# ======================================================================

def b_nomes(c, t, C, B):
    frame(c, t, B["start"], "AVISO RÁPIDO", "SOBRE OS NOMES", AMBER)
    aa, ab = ep(t, C["29.a"], 0.5), ep(t, C["29.b"], 0.5)
    if aa > 0:
        rrect(c, 230, 220, 680, 420, 24, "#F7F7F5", aa)
        text(c, "SÉRIE DE LINGUAGENS", 570, 280, 24, "black", GRAY, aa, tracking=1.5)
        text(c, "campo amplo =", 570, 400, 36, "bold", INK2, aa)
        pill(c, "TEMA", 570, 480, INK2, size=40, a=aa, anchor="center", bounds=(0, 1920))
    if ab > 0:
        rrect(c, 1010, 220, 680, 420, 24, mix("#FFFFFF", PURPLE, 0.06), ab, shadow=True)
        text(c, "REDAÇÃO · CARTILHA DO INEP", 1350, 280, 24, "black", PURPLE, ab, tracking=1.5)
        text(c, "o amplo =", 1200, 400, 34, "bold", INK2, ab)
        pill(c, "ASSUNTO", 1200, 470, INK2, size=34, a=ab, anchor="center", bounds=(0, 1920))
        text(c, "o recorte =", 1500, 400, 34, "bold", INK2, ab * ep(t, C["29.b"] + 1.0, 0.4))
        pill(c, "TEMA", 1500, 470, BLUE, size=34, a=ab * ep(t, C["29.b"] + 1.0, 0.4), anchor="center", bounds=(0, 1920))
    ac = ep(t, C["29.c"], 0.5)
    if ac > 0:
        boxed(c, 330, 690, 560, 110, INK2, ac, 0.05)
        text_mid(c, "sobre o que se fala", 610, 745, 36, "black", INK2, ac)
        text_mid(c, "≠", 960, 745, 70, "black", RED, ac)
        boxed(c, 1030, 690, 560, 110, BLUE, ac, 0.08)
        text_mid(c, "o recorte exato", 1310, 745, 36, "black", BLUE, ac)


# ======================================================================
# bloco F — tema × tese (a caixa)
# ======================================================================

def b_tese(c, t, C, B):
    head_seq(c, t, C, [("30", "O QUE É SEU", "NA REDAÇÃO?", BLUE), ("31", "TEMA × TESE", "O TESTE DA CONTESTAÇÃO", BLUE)])
    card(c, *CARD_R)
    sid = which(t, C, ["30", "31"])
    if sid == "30":
        a0 = ep(t, C["30.t"], 0.5)
        ab = ep(t, C["30.b"], 0.5)
        if ab <= 0:
            op = ep(t, C["30.a"], 0.7)
            caixa(c, 760, 470, 400, 320, a0, open_=op, inner="?", inner_a=0)
            if op > 0:
                for k in range(3):
                    r = 30 + 40 * ((t * 0.8 + k / 3) % 1)
                    c.drawCircle(960, 450, r * 2.2, paint(AMBER, op * 0.25 * (1 - ((t * 0.8 + k / 3) % 1)), stroke=4))
                text(c, "dentro da caixa", 960, 350, 40, "black", AMBER, op)
        else:
            # todos recebem o mesmo endereço; cada um entrega uma coisa
            shapes = [BLUE, GREEN, PURPLE, AMBER]
            ac = ep(t, C["30.c"], 0.5)
            for k in range(4):
                x = 290 + k * 360
                a = ab * ep(t, C["30.b"] + 0.2 * k, 0.4)
                rrect(c, x, 210, 260, 64, 10, "#FFFFFF", a, shadow=True)
                text(c, "MESMO ENDEREÇO", x + 130, 250, 18, "black", BLUE, a, tracking=1)
                caixa(c, x + 30, 520, 200, 200, a, open_=ac, inner=None)
                if ac > 0:
                    yy = 470 - 50 * ease_out(ac)
                    if k == 0:
                        c.drawCircle(x + 130, yy, 40, paint(shapes[k], a * ac))
                    elif k == 1:
                        rrect(c, x + 90, yy - 40, 80, 80, 10, shapes[k], a * ac)
                    elif k == 2:
                        p = skia.Path(); p.moveTo(x + 130, yy - 46); p.lineTo(x + 176, yy + 36); p.lineTo(x + 84, yy + 36); p.close()
                        c.drawPath(p, paint(shapes[k], a * ac))
                    else:
                        rrect(c, x + 80, yy - 26, 100, 52, 26, shapes[k], a * ac)
            ad = ep(t, C["30.d"], 0.5)
            pill(c, "TESE = a SUA posição sobre o tema", W / 2, 810, BLUE, size=36, a=ad, anchor="center")
    else:
        a0, d0 = rise(t, C["31.t"])
        rrect(c, 230, 220 + d0, 680, 330, 24, "#F7F7F5", a0)
        text(c, "TEMA", 570, 300 + d0, 48, "black", BLUE, a0)
        text(c, "dado pela prova", 570, 380 + d0, 34, "bold", INK2, a0)
        text(c, "igual para TODOS", 570, 440 + d0, 34, "black", INK, a0)
        aa, d1 = rise(t, C["31.a"])
        rrect(c, 1010, 220 + d1, 680, 330, 24, mix("#FFFFFF", BLUE, 0.08), aa, shadow=True)
        text(c, "TESE", 1350, 300 + d1, 48, "black", BLUE, aa)
        text(c, "é SUA", 1350, 380 + d1, 34, "black", INK, aa)
        text(c, "uma frase completa", 1350, 440 + d1, 30, "bold", INK2, aa)
        ab = ep(t, C["31.b"], 0.5)
        if ab > 0:
            person(c, 1240, 590, "#F97316", ab, 0.6)
            bubble(c, "Eu discordo!", 1300, 560, 300, "#F97316", ab, True, 30)
            regra(c, "Alguém poderia contestar? Então é tese.", 770, ab, 32, GREEN)
            text(c, "ninguém contesta um tema", 570, 640, 30, "black", GRAY, ab)


def b_eufaco(c, t, C, B):
    head(c, t, B["start"], "EU FAÇO · ENEM 2020", "3 PERGUNTAS NO RASCUNHO", GREEN)
    paper(c, 160, 160, 1600, 690, 1.0, lh=58, top=200)
    rows = [("32.a", "32.a2", "1. De que área a prova fala?", "saúde mental", "ASSUNTO = cidade"),
            ("32.b", "32.b2", "2. Que recorte dessa área ela pede?", "o estigma associado às doenças mentais na sociedade brasileira", "TEMA = endereço"),
            ("33.c", "33.c2", "3. O que eu defendo sobre esse recorte?", "que o estigma afasta as pessoas do tratamento e precisa ser combatido na escola e na mídia", "TESE = caixa")]
    y = 252
    for k, (cq, ca, q, ans, lab) in enumerate(rows):
        qa = ep(t, C[cq], 0.3)
        span_q = (C[cq], C[cq] + 1.6)
        hand(c, q, 260, y, 34, PEN, qa, wreveal(t, span_q), bold=True)
        if ca == "33.c2":
            sp = (C["33.c2"], C["33.d"] - 0.3)
        elif ca == "32.b2":
            sp = (C["32.b2"], C["32.b2"] + 3.2)
        else:
            sp = (C[ca], C[ca] + 0.9)
        n = hand_para(c, ans, 300, y + 58, 32, mix(PEN, "#000000", 0.2) if k < 2 else BLUE, ep(t, C[ca], 0.2), 1140, 58, wreveal(t, sp))
        # rótulo à direita
        la = ep(t, sp[1] - 0.2, 0.4)
        pill(c, lab, 1720, y - 12, BLUE, size=24, a=la, anchor="right", bounds=(0, 1920))
        if k == 2:
            # pensando...
            th = fw(t, C["33.c1"], C["33.c2"])
            if th > 0:
                for j in range(3):
                    c.drawCircle(320 + j * 34, y + 50, 9, paint(GRAY, th * (0.4 + 0.6 * (0.5 + 0.5 * math.sin(t * 6 - j)))))
        y += 58 + max(1, n) * 58 + 30
    ad = ep(t, C["33.d"], 0.4)
    if ad > 0:
        check_icon(c, 300, 800, 22, ad, GREEN)
        text(c, "alguém poderia discordar? poderia → é tese", 336, 810, 30, "black", GREEN, ad, align="left")
    ae = ep(t, C["33.e"], 0.5)
    if ae > 0:
        caixa(c, 1480, 690, 170, 130, ae, open_=1.0)
        text(c, "dentro da caixa", 1565, 670 - 10 * ae, 22, "black", BLUE, ae)


# ======================================================================
# bloco G — repetir o tema não é tese
# ======================================================================

FALSA = "O estigma associado às doenças mentais é um tema muito importante."


def b_repetir(c, t, C, B):
    head_seq(c, t, C, [("34", "ARMADILHA", "PARECE TESE?", AMBER), ("35", "FAÇA O TESTE", "REPETIR O TEMA NÃO É TESE", RED)])
    card(c, *CARD_R)
    a35 = ep(t, C["35"], 0.6)
    ab = ep(t, C["34.b"], 0.5)
    # cartão da frase falsa: centralizado em 34, vai para a esquerda em 35
    x = lerp(360, 200, a35)
    w = lerp(1200, 720, a35)
    if ab > 0:
        rrect(c, x, 200, w, lerp(200, 260, a35), 22, mix("#FFFFFF", AMBER, 0.10), ab, shadow=True)
        sz = lerp(44, 32, a35)
        lines = wrap(FALSA, "black", sz, w - 80)
        for j, ln in enumerate(lines):
            text(c, ln, x + 40, 270 + j * sz * 1.3, sz, "black", INK, ab, align="left")
        # palavras do tema sublinhadas
        ub = ep(t, C["35.b"], 0.5)
        if ub > 0:
            for j, ln in enumerate(lines):
                tw = text_w(ln.replace("é um tema muito importante.", "").rstrip(), "black", sz) if j == len(lines) - 1 or "é um" in ln else text_w(ln, "black", sz)
                underline(c, x + 40, x + 40 + tw, 270 + j * sz * 1.3 + 10, RED, ub, prog(t, C["35.b"], 0.8), 5)
    ac = ep(t, C["34.c"], 0.4) * (1 - a35)
    pill(c, "tem as palavras do tema · soa séria", W / 2, 520, AMBER, size=30, a=ac, anchor="center")
    pill(c, "parece tese...", W / 2, 610, AMBER, size=34, a=ac, anchor="center")
    if a35 > 0:
        aa = ep(t, C["35.a"], 0.4)
        text(c, "alguém discorda?", 560, 520, 34, "black", INK2, aa)
        text(c, "NINGUÉM", 560, 570, 40, "black", RED, ep(t, C["35.a"] + 0.8, 0.4))
        acc = ep(t, C["35.c"], 0.5)
        caixa(c, 300, 670, 260, 160, acc, open_=acc, label="x")
        text(c, "caixa", 640, 730, 36, "black", RED, acc, align="left")
        text(c, "VAZIA", 640, 776, 36, "black", RED, acc, align="left")
        ad, dd = rise(t, C["35.d"])
        if ad > 0:
            rrect(c, 1000, 200 + dd, 700, 260, 22, mix("#FFFFFF", BLUE, 0.10), ad, shadow=True)
            text(c, "TESE", 1040, 250 + dd, 22, "black", BLUE, ad, align="left", tracking=2)
            para(c, "O estigma afasta as pessoas do tratamento.", 1040, 320 + dd, 38, "black", BLUE, ad, 620, 48)
            check_icon(c, 1060, 560, 26, ep(t, C["35.d"] + 1.6, 0.4), GREEN)
            text(c, "toma partido", 1100, 572, 38, "black", GREEN, ep(t, C["35.d"] + 1.6, 0.4), align="left")
            caixa(c, 1210, 690, 220, 140, ad, open_=1.0, inner=None)
            rrect(c, 1270, 640, 100, 60, 10, BLUE, ad)


# ======================================================================
# nós fazemos — 2022
# ======================================================================

def b_exercicio(c, t, C, B):
    head_seq(c, t, C, [("36", "SUA VEZ · ENEM 2022", "ASSUNTO E TEMA", GREEN), ("37", "VAMOS CONFERIR", "ASSUNTO E TEMA", GREEN)])
    card(c, *CARD_R)
    ab = ep(t, C["36.b"], 0.5)
    boxed(c, 220, 190, 1480, 140, BLUE, ab, 0.08)
    sz = 40
    s = "“" + TEMA22 + "”"
    lines = wrap(s, "black", sz, 1400)
    for j, ln in enumerate(lines):
        text(c, ln, W / 2, 250 + j * 50, sz, "black", BLUE, ab)
    # sublinhar desafios / valorização / no Brasil (37.c)
    uc = ep(t, C["37.c"], 0.4)
    if uc > 0 and len(lines) >= 1:
        x0 = W / 2 - text_w(lines[0], "black", sz) / 2
        for k, wd in enumerate(("Desafios", "valorização")):
            i = lines[0].find(wd)
            if i >= 0:
                xa = x0 + text_w(lines[0][:i], "black", sz)
                underline(c, xa, xa + text_w(wd, "black", sz), 262, GREEN, uc, ep(t, C["37.c"] + 0.4 * k, 0.4), 6)
        ln = lines[-1]
        i = ln.find("no Brasil")
        if i >= 0:
            x1 = W / 2 - text_w(ln, "black", sz) / 2
            xa = x1 + text_w(ln[:i], "black", sz)
            underline(c, xa, xa + text_w("no Brasil", "black", sz), 262 + (len(lines) - 1) * 50, GREEN, uc, ep(t, C["37.c"] + 0.8, 0.4), 6)
    pa = ep(t, C["36.c"], 0.4)
    if pa > 0:
        paper(c, 260, 380, 1400, 420, pa, lh=70, top=420)
        hand(c, "Assunto (a cidade):", 380, 480, 34, PEN, pa, bold=True)
        hand(c, "Tema (o endereço completo):", 380, 620, 34, PEN, ep(t, C["36.d"], 0.4), bold=True)
        r1 = wreveal(t, (C["37.a"] + 0.3, C["37.a"] + 2.0))
        hand(c, "povos e comunidades tradicionais", 820, 480, 34, BLUE, pa, r1)
        sp = (C["37.b"] + 0.3, C["37.b"] + 2.6)
        hand_para(c, "Desafios para a valorização de comunidades e povos tradicionais no Brasil", 380, 690, 32, BLUE, pa, 1200, 60, wreveal(t, sp))
    pause_timer(c, t, C["36.end"] - 1.8, 1580, 520)


# ======================================================================
# recapitulação e erros
# ======================================================================

FRASES = ["Assunto é a cidade; tema é o endereço completo.",
          "O tema a prova dá; a tese é sua.",
          "“É um tema importante” não é tese."]


def b_recap(c, t, C, B):
    sid = which(t, C, ["38", "46"])
    frame(c, t, B["start"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "38" else "PARA FECHAR", PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 320 + k * 170 + d
        badge_num(c, k + 1, 280, y - 16, a, 36, bg=PURPLE)
        text(c, s, 350, y, 50, "black", INK, a, align="left")


ERROS = [("39", "Achar que a redação é “sobre um assunto” qualquer", "na escola era assim: “escreva sobre as férias”", "o ENEM pede um RECORTE EXATO: o endereço completo"),
         ("40", "Inverter ASSUNTO e TEMA", "no dia a dia as duas palavras viram sinônimos", "assunto = cidade (curtinho) · tema = a frase inteira"),
         ("41", "Repetir a frase temática achando que é tese", "tem todas as palavras da prova", "alguém poderia discordar? se não, a caixa está vazia")]


def b_erros(c, t, C, B):
    sid = which(t, C, [e[0] for e in ERROS])
    n = [e[0] for e in ERROS].index(sid)
    _, err, parece, fix = ERROS[n]
    head(c, t, C[sid], f"ERRO {n + 1} DE 3", "OS ERROS CLÁSSICOS", RED)
    card(c, *CARD_R)
    for k in range(3):
        badge_num(c, k + 1, 880 + k * 80, 210, 1, 22, bg=RED if k == n else LIGHT)
    cue = lambda x: C[f"{sid}.{x}"]
    aa = ep(t, cue("a"), 0.5)
    check_icon(c, 300, 330, 34, aa, RED, "x")
    para(c, err, 360, 345, 44, "black", RED, aa, 1300)
    ab = ep(t, cue("b"), 0.5)
    pill(c, "PARECE CERTO PORQUE...", 300, 480, AMBER, size=26, a=ab, bounds=(0, 1920))
    text(c, parece, 300, 560, 38, "bold", INK2, ab, align="left")
    ac = ep(t, cue("c"), 0.5)
    check_icon(c, 300, 678, 34, ac, GREEN)
    para(c, fix, 360, 694, 40, "black", GREEN, ac, 1300)


# ======================================================================
# questão 1 (seção 12)
# ======================================================================

ALTS = [("A", "assunto: desafios para a formação educacional de surdos no Brasil; tema: educação.", "45.ea", "INVERTE cidade e endereço", RED),
        ("B", "assunto: educação de pessoas surdas; tema: os desafios para a formação educacional de surdos no Brasil.", None, "", GREEN),
        ("C", "assunto e tema coincidem: ambos correspondem à palavra “surdos”.", "45.ec", "APAGA a diferença", RED),
        ("D", "assunto: a Língua Brasileira de Sinais; tema: a surdez como condição biológica.", "45.ed", "TROCA o endereço", RED),
        ("E", "assunto: educação de pessoas surdas; tema: a educação de surdos nos diferentes países do mundo.", "45.ee", "TIRA o bairro: e o “no Brasil”?", AMBER)]


def b_questao(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO · ESTILO ENEM", "ASSUNTO E TEMA", BLUE)
    card(c, *CARD_R)
    alt_on = ep(t, C["43"], 0.7)
    # enunciado (grande na cena 42, compacto à esquerda depois)
    x = lerp(260, 180, alt_on)
    w = lerp(1400, 600, alt_on)
    sz = lerp(40, 26, alt_on)
    a0 = ep(t, C["42.a"], 0.5)
    y = lerp(260, 220, alt_on)
    h1 = para(c, "O tema da redação do Enem 2017 foi", x, y, sz, "bold", INK2, a0, w, sz * 1.3)
    ab = ep(t, C["42.b"], 0.5)
    hb = len(wrap("“" + TEMA17 + "”", "black", sz * 1.1, w - 40)) * sz * 1.45 + 30
    boxed(c, x - 10, y + h1 - sz * 0.6, w + 20, hb, BLUE, ab, 0.08, 16)
    para(c, "“" + TEMA17 + "”", x + 10, y + h1 + sz * 0.9, sz * 1.1, "black", BLUE, ab, w - 40, sz * 1.45)
    acq = ep(t, C["42.c"], 0.5)
    para(c, "A alternativa que identifica corretamente o assunto amplo e o tema dessa proposta, nessa ordem, é:", x, y + h1 + hb + sz * 0.9,
         sz, "bold", INK, acq, w, sz * 1.3)
    text(c, "Questão do material de estudo (seção 12)", x, 820, 18, "medium", GRAY, a0 * alt_on, align="left")
    if alt_on <= 0:
        return
    aok = ep(t, C["45.ok"], 0.5)
    yy = 225
    for L, s, cx, why, col in ALTS:
        a, d = rise(t, C[f"43.{L.lower()}"])
        a *= alt_on
        lines = wrap(s, "bold", 24, 820)
        hh = len(lines) * 31 + 16 + (30 if cx else 0)
        ok = cx is None
        if ok and aok > 0:
            rrect(c, 830, yy - 32 + d, 900, hh + 12, 12, GREEN, 0.15 * aok)
        badge_num(c, L, 862, yy - 8 + d, a, 20, bg=GREEN if ok and aok > 0.5 else INK)
        ax = ep(t, C[cx], 0.4) if cx else 0
        for j, ln in enumerate(lines):
            text(c, ln, 900, yy + d + j * 31, 24, "bold", INK, a * (1 - 0.5 * ax), align="left")
            if ax > 0:
                strike(c, 896, yy + d + j * 31 - 8, 904 + text_w(ln, "bold", 24), yy + d + j * 31 - 8, ax, RED, ax)
        if ax > 0:
            pill(c, why, 900, yy + d + len(lines) * 31 + 2, col, size=18, a=ax, bounds=(0, 1920))
        yy += hh + 16
    pause_timer(c, t, C["43.end"] - 1.8, 480, 700)
    # resolução com a etiqueta (cena 44)
    ae = fw(t, C["44.a"], C["45"])
    if ae > 0:
        rows = [("CIDADE · ASSUNTO", "educação de pessoas surdas", ep(t, C["44.a"], 0.4), BLUE, None, 0),
                ("ENDEREÇO · TEMA", "a frase inteira", ep(t, C["44.b"], 0.4), BLUE, None, 0)]
        rrect(c, 160, 560, 640, 270, 18, "#FFFFFF", ae)
        etiqueta(c, 160, 560, 640, ae, rows)
    result_box(c, "Letra B", 480, 740, 56, aok, GREEN)


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "A FRASE TEMÁTICA, BLOCO A BLOCO", PURPLE)
    aa = ep(t, C["47.a"], 0.5)
    pieces = ["Perspectivas acerca", "do envelhecimento", "na sociedade brasileira"]
    ab = ep(t, C["47.b"], 0.5)
    ac = ep(t, C["47.c"], 0.6)
    x = 260
    for k, s in enumerate(pieces):
        w = text_w(s, "black", 40) + 60
        gap = 30 * ac
        missing = (k == 2) and ab > 0 and ac < 0.5
        al = aa * (1 - 0.85 * ab * (1 - ac) if k == 2 else 1)
        rrect(c, x + k * gap, 300, w, 100, 14, mix("#FFFFFF", BLUE, 0.12), al, shadow=True)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x + k * gap, 300, w, 100), 14, 14), paint(BLUE, al, stroke=4))
        text_mid(c, s, x + k * gap + w / 2, 350, 40, "black", BLUE, al)
        if missing:
            c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x + k * gap, 300, w, 100), 14, 14), paint(RED, ab, stroke=4))
            text_mid(c, "?", x + k * gap + w / 2, 350, 60, "black", RED, ab)
        x += w
    if ab > 0:
        truck(c, 560, 520, ab * (1 - ac), RED, 0.9)
        selo(c, 1200, 560, ab * (1 - ac), "ENTREGA DEU ERRADO", RED, -5, 36)
    pill(c, "ep. 2 · como desmontar a frase temática bloco a bloco", W / 2, 720, PURPLE, size=32, a=ac, anchor="center")


def b_cta(c, t, C, B):
    cta(c, t, C["48.like"], C["48.sub"], C["48.bell"], C["48.com"], C["48.bye"], "No tema de 2022, você acertou o assunto e o tema?")


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, pede=b_pede, proposta=b_proposta, bolo=b_bolo,
              comando=b_comando, endereco=b_endereco, tabela=b_tabela, nomes=b_nomes, tese=b_tese, eufaco=b_eufaco,
              repetir=b_repetir, exercicio=b_exercicio, recap=b_recap, erros=b_erros, questao=b_questao, ponte=b_ponte, cta=b_cta)
