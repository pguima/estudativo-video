"""Visual — Operações e Conjuntos Numéricos, Episódio 1: Ordem das operações e regra de sinais (iniciantes, tema claro).
Cores com função: azul = definição · roxo = regra/fórmula · âmbar = armadilha · verde = atalho/dica/resultado · vermelho = erro.
Peças próprias deste episódio:
- expr(): a expressão fica inteira na tela; a parte que está sendo resolvida fica roxa e "encolhe" para o resultado (verde).
- fila(): a fila do pronto-socorro (parênteses → potências → vezes e dividir → mais e menos), com o andar ativo aceso.
- reta numérica com saltos e extrato bancário (positivo = dinheiro que entra, negativo = dívida).
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
ARQUIVO_FINAL = "enem_matematica_conjuntos_ep1_ordem_e_sinais.mp4"
CARD_R = (140, 150, 1640, 690)
SYM = "C:/Windows/Fonts/seguisym.ttf"
HL = "#7C5CFA"          # parte em resolução (roxo)
DEBT = "#E5484D"        # dívida
CASH = "#16A36A"        # dinheiro que entra


# ======================================================================
# tempos das palavras (para encolher a conta no instante em que o resultado é dito)
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
# texto matemático (sobrescrito ^x e fonte reserva para símbolos que a Inter não tem)
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


def tag(c, s, cx, cy, col, a, size=28):
    """etiqueta colorida com símbolos matemáticos"""
    if a <= 0:
        return
    w, h = ftext_w(s, "black", size) + size * 1.2, size * 1.75
    rrect(c, cx - w / 2, cy - h / 2, w, h, h / 2.6, col, a, shadow=True)
    fmid(c, s, cx, cy, size, "black", on(col), a)


# ======================================================================
# expressão que encolhe passo a passo
# ======================================================================

def _toks(spec):
    """'a:12 b:− c:4' -> [(id, texto, colado)] ; prefixo ~ = sem espaço antes (ex.: '~d:)')"""
    out = []
    for item in spec.split("  "):
        item = item.strip()
        if not item:
            continue
        tight = item.startswith("~")
        item = item.lstrip("~")
        i, s = item.split(":", 1)
        out.append((i, s, tight))
    return out


def _layout(toks, size, cx):
    gap = size * 0.3
    ws = [ftext_w(s, "black", size) for _, s, _ in toks]
    total = sum(ws) + sum(0 if tg else gap for (_, _, tg) in toks[1:])
    x = cx - total / 2
    pos = {}
    for k, ((i, s, tg), w) in enumerate(zip(toks, ws)):
        if k and not tg:
            x += gap
        pos[i] = (x + w / 2, w)
        x += w
    return pos


def expr(c, t, states, cx, cy, size, a=1.0, D=0.7):
    """states = [dict(t=, s='id:txt  id:txt', hl='ids separados por espaço', thl=instante do destaque)]
    Entre dois estados, os tokens comuns deslizam, os que somem encolhem (roxos) e os novos crescem (verdes)."""
    if a <= 0 or t < states[0]["t"]:
        return
    a *= ep(t, states[0]["t"], 0.5)
    k = max(i for i, st in enumerate(states) if st["t"] <= t)
    cur = states[k]
    toks = _toks(cur["s"])
    pos = _layout(toks, size, cx)
    f = ease_io(prog(t, cur["t"], D)) if k > 0 else 1.0
    prev_toks = _toks(states[k - 1]["s"]) if k > 0 else []
    prev_pos = _layout(prev_toks, size, cx) if k > 0 else {}
    prev_ids = {i for i, _, _ in prev_toks}
    new_ids = {i for i, _, _ in toks} - prev_ids
    hl = set(cur.get("hl", "").split())
    ahl = ep(t, cur["thl"], 0.35) if cur.get("thl") is not None else 0
    green = 1 - prog(t, cur["thl"], 0.35) if cur.get("thl") is not None else 1.0
    # caixa do destaque atrás da parte em resolução
    if ahl > 0 and hl:
        xs = [(pos[i][0] - pos[i][1] / 2, pos[i][0] + pos[i][1] / 2) for i in hl if i in pos]
        if xs:
            x0, x1 = min(x for x, _ in xs) - 14, max(x for _, x in xs) + 14
            rrect(c, x0, cy - size * 0.8, x1 - x0, size * 1.6, 16, HL, a * ahl * 0.13)
    # tokens que estão saindo (do estado anterior)
    if k > 0 and f < 1:
        prev_hl = set(states[k - 1].get("hl", "").split())
        nx = [pos[i][0] for i in new_ids] or [cx]
        tx = sum(nx) / len(nx)
        for i, s, _ in prev_toks:
            if i in pos:
                continue
            x = lerp(prev_pos[i][0], tx, f)
            sc = 1 - 0.75 * f
            c.save(); c.translate(x, cy); c.scale(sc, sc)
            fmid(c, s, 0, 0, size, "black", HL if i in prev_hl else INK, a * (1 - f))
            c.restore()
    for i, s, _ in toks:
        x = pos[i][0]
        if i in prev_pos and k > 0:
            x = lerp(prev_pos[i][0], pos[i][0], f)
        col = INK
        if i in new_ids and k > 0:
            col = mix(INK, GREEN, green)
        if i in hl:
            col = mix(col, HL, ahl)
        sc = 1.0
        aa = a
        if i in new_ids and k > 0:
            sc = 0.4 + 0.6 * ease_back(clamp(f))
            aa = a * f
        c.save(); c.translate(x, cy); c.scale(sc, sc)
        fmid(c, s, 0, 0, size, "black", col, aa)
        c.restore()


# ======================================================================
# fila do pronto-socorro
# ======================================================================

FILA = [("( )  [ ]  { }", "parênteses"), ("x^2", "potências"), ("×  ÷", "vezes e dividir"), ("+  −", "mais e menos")]
TRIAGEM = ["#E5484D", "#F97316", "#E8A317", "#16A36A"]


def fila(c, x, y, a, ativo=None, w=420, dy=74, cues=None, t=0.0, titulo=True):
    """cartão com os 4 andares da fila; ativo = índice 0..3 aceso em roxo"""
    if a <= 0:
        return
    h = dy * 4 + (86 if titulo else 30)
    card(c, x, y, w, h, a)
    y0 = y + 30
    if titulo:
        icon(c, "", x + 44, y + 42, 30, RED, a)
        text(c, "FILA DE PRIORIDADE", x + 72, y + 52, 24, "black", INK, a, align="left")
        y0 = y + 86
    for k, (sym, lab) in enumerate(FILA):
        ak = a * (ep(t, cues[k], 0.45) if cues else 1.0)
        if ak <= 0:
            continue
        yy = y0 + k * dy
        on_ = ativo == k
        if on_:
            rrect(c, x + 14, yy, w - 28, dy - 10, 14, HL, ak * 0.14)
        rrect(c, x + 26, yy + 12, 8, dy - 34, 4, TRIAGEM[k], ak)
        badge_num(c, k + 1, x + 66, yy + (dy - 10) / 2, ak, 20, bg=HL if on_ else INK)
        fmid(c, sym, x + 100, yy + (dy - 10) / 2, 28, "black", HL if on_ else INK, ak, align="left")
        text_mid(c, lab, x + w - 24, yy + (dy - 10) / 2, 22, "bold", HL if on_ else INK2, ak, align="right")


def ativo_em(t, marcas):
    """marcas = [(instante, índice)] -> índice ativo"""
    at = None
    for tm, i in marcas:
        if t >= tm:
            at = i
    return at


# ======================================================================
# reta numérica e extrato
# ======================================================================

class Reta:
    def __init__(self, x0, x1, y, lo, hi):
        self.x0, self.x1, self.y, self.lo, self.hi = x0, x1, y, lo, hi

    def X(self, v):
        return lerp(self.x0, self.x1, (v - self.lo) / (self.hi - self.lo))

    def draw(self, c, a, tint=False):
        if a <= 0:
            return
        y = self.y
        if tint:
            rrect(c, self.x0 - 10, y - 18, self.X(0) - self.x0 + 10, 36, 10, DEBT, a * 0.10)
            rrect(c, self.X(0), y - 18, self.x1 - self.X(0) + 10, 36, 10, CASH, a * 0.10)
        arrow(c, self.x0 - 20, y, self.x1 + 34, y, INK2, a, 4, 14)
        for v in range(self.lo, self.hi + 1):
            x = self.X(v)
            line(c, x, y - (14 if v == 0 else 9), x, y + (14 if v == 0 else 9), INK2, a, 3 if v == 0 else 2)
            s = str(v).replace("-", "−")
            col = DEBT if v < 0 else CASH if v > 0 else INK
            text(c, s, x, y + 48, 24 if v else 28, "black" if v == 0 else "bold", col, a)

    def jump(self, c, v0, v1, col, a, p, lab=None):
        if a <= 0 or p <= 0:
            return
        x0, x1 = self.X(v0), self.X(v1)
        hgt = 40 + 6 * abs(v1 - v0)
        path = skia.Path()
        n = 40
        pts = []
        for i in range(n + 1):
            u = i / n * p
            pts.append((lerp(x0, x1, u), self.y - 16 - hgt * 4 * u * (1 - u)))
        path.moveTo(*pts[0])
        for q in pts[1:]:
            path.lineTo(*q)
        c.drawPath(path, paint(col, a, stroke=5, cap_round=True))
        if p > 0.95:
            (xa, ya), (xb, yb) = pts[-2], pts[-1]
            arrow(c, xa, ya, xb, yb + 2, col, a, 5, 16)
            c.drawCircle(x1, self.y, 10, paint(col, a))
        if lab:
            text(c, lab, (x0 + x1) / 2, self.y - 30 - hgt, 26, "black", col, a * clamp(p * 2 - 0.4))

    def dot(self, c, v, col, a):
        if a > 0:
            c.drawCircle(self.X(v), self.y, 11, paint(col, a))


def extrato(c, t, x, y, w, rows, saldo_t, saldo, a=1.0):
    """rows = [(instante, descrição, valor)] ; saldo exibido a partir de saldo_t"""
    if a <= 0:
        return
    h = 130 + 76 * len(rows) + 110
    card(c, x, y, w, h, a)
    pill(c, "EXTRATO", x + 30, y + 44, BLUE, size=22, a=a, bounds=(0, 1920))
    for k, (tc, desc, v) in enumerate(rows):
        ak, dy = rise(t, tc)
        ak *= a
        yy = y + 130 + k * 76 + dy
        text(c, desc, x + 34, yy, 30, "bold", INK2, ak, align="left")
        col = DEBT if v < 0 else CASH
        ftext(c, ("+ " if v > 0 else "− ") + f"R$ {abs(v)}", x + w - 34, yy, 34, "black", col, ak, align="right")
    ys = y + 130 + 76 * len(rows) + 10
    as_ = ep(t, saldo_t, 0.5) * a
    if as_ > 0:
        line(c, x + 30, ys - 30, x + w - 30, ys - 30, LINE, as_, 3)
        text(c, "SALDO", x + 34, ys + 22, 32, "black", INK, as_, align="left")
        col = DEBT if saldo < 0 else CASH
        s = ("− " if saldo < 0 else "+ ") + f"R$ {abs(saldo)}"
        c.save(); sc = 0.8 + 0.2 * ease_back(clamp(as_)); c.translate(x + w - 34, ys + 10); c.scale(sc, sc)
        ftext(c, s, 0, 12, 42, "black", col, as_, align="right")
        c.restore()


def regra(c, s, cx, cy, a, size=34, col=None, w=None):
    """faixa de regra (roxo por padrão)"""
    col = PURPLE if col is None else col
    if a <= 0:
        return
    a2, dy = a, (1 - a) * 14
    ww = (w or ftext_w(s, "black", size) + 90)
    rrect(c, cx - ww / 2, cy - 44 + dy, ww, 88, 22, col, a2 * 0.12)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - ww / 2, cy - 44 + dy, ww, 88), 22, 22),
                paint(col, a2, stroke=3))
    fmid(c, s, cx, cy + dy, size, "black", col, a2)


def pause_badge(c, x, y, a):
    if a <= 0:
        return
    rrect(c, x, y, 340, 96, 24, AMBER, a, shadow=True)
    c.drawRect(skia.Rect.MakeXYWH(x + 28, y + 22, 14, 52), paint(INK, a))
    c.drawRect(skia.Rect.MakeXYWH(x + 54, y + 22, 14, 52), paint(INK, a))
    text_mid(c, "PAUSE E TENTE", x + 210, y + 48, 30, "black", INK, a)


def erro_tiles(c, t, items):
    """[(instante, título, [linhas], cor)] -> 3 cartões: o erro · por que parece certo · a correção"""
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
            ftext(c, ln.lstrip("!"), x + cw / 2, y + 250 + j * 60, 46 if big else 32, "black",
                  (RED if k == 0 else GREEN if k == 2 else INK) if big else INK, a)


# ======================================================================
# gancho, promessa, pré-requisitos
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "ORDEM E SINAIS · EPISÓDIO 1", BLUE)
    a, dy = rise(t, C["01.a"])
    ftext(c, "2 + 3 × 4 = ?", W / 2, 360 + dy, 130, "black", INK, a)
    for k, (cue, val) in enumerate((("01.b", "20"), ("01.c", "14"))):
        ak, d = rise(t, C[cue])
        x = W / 2 - 330 + k * 660
        card(c, x - 220, 450 + d, 440, 230, ak)
        text(c, "metade responde", x, 510 + d, 30, "bold", INK2, ak)
        text(c, val, x, 640 + d, 110, "black", BLUE, ak)
    ad = ep(t, C["01.d"], 0.5)
    text(c, "só uma está certa", W / 2, 750, 40, "black", AMBER, ad)
    ae = ep(t, C["01.e"], 0.5)
    for k, s in enumerate(("FÍSICA", "FUNÇÃO", "ESTATÍSTICA")):
        pill(c, s, W / 2 - 330 + k * 330, 840, AMBER, size=28, a=ae * ep(t, C["01.e"] + 0.5 * k, 0.4), anchor="center")


def b_promessa(c, t, C, B):
    head(c, t, B["start"], "AO FINAL DESTA AULA", "VOCÊ VAI CONSEGUIR", GREEN)
    cards_row(c, t, [("1", "Resolver\nqualquer\nexpressão", C["02.a"], BLUE),
                     ("2", "Sem errar\nsinal", C["02.a"] + 1.6, RED),
                     ("3", "Entendendo\no porquê", C["02.b"], GREEN)], cw=440, chh=420, title_size=40)
    pill(c, "expressão = conta com várias operações juntas", W / 2, 760, BLUE, size=28,
         a=ep(t, C["02.a"] + 0.8, 0.5), anchor="center")


def termometro(c, x, y, a, nivel):
    """termômetro simples de -10 a +30; nivel em °C"""
    if a <= 0:
        return
    h = 420
    rrect(c, x - 26, y, 52, h, 26, "#FFFFFF", a, shadow=True, stroke=3, stroke_color=LIGHT)
    c.drawCircle(x, y + h + 20, 46, paint("#FFFFFF", a))
    c.drawCircle(x, y + h + 20, 46, paint(LIGHT, a, stroke=3))
    c.drawCircle(x, y + h + 20, 34, paint(BLUE, a))
    yv = lambda v: y + h - 30 - (v + 10) / 40 * (h - 60)
    rrect(c, x - 12, yv(nivel), 24, y + h + 10 - yv(nivel), 12, BLUE, a)
    for v in (-10, -5, 0, 10, 20, 30):
        line(c, x + 30, yv(v), x + 48, yv(v), INK2, a, 3)
        col = DEBT if v < 0 else INK2
        text_mid(c, str(v).replace("-", "−"), x + 60, yv(v), 24, "bold", col, a, align="left")
    line(c, x - 60, yv(0), x + 50, yv(0), INK, a, 3, dash=[8, 6])


def b_prereq(c, t, C, B):
    p1 = t < C["04"] - 0.2
    if p1:
        head(c, t, B["start"], "LEMBRETE 1", "NÚMERO NEGATIVO", BLUE)
        aa = ep(t, C["03.a"], 0.5)
        card(c, 160, 170, 520, 640, aa)
        nivel = lerp(18, -5, ease_io(prog(t, C["03.a"] + 0.6, 1.6)))
        termometro(c, 330, 230, aa, nivel)
        ftext(c, "−5 °C", 560, 470, 56, "black", DEBT, ep(t, C["03.a"] + 2.0, 0.4))
        pill(c, "negativo = abaixo do zero", 1220, 260, BLUE, size=30, a=aa, anchor="center")
        ab = ep(t, C["03.b"], 0.5)
        card(c, 740, 360, 1020, 380, ab)
        text(c, "RETA NUMÉRICA", 1250, 420, 30, "black", BLUE, ab)
        r = Reta(800, 1700, 560, -5, 5)
        r.draw(c, ab, tint=True)
        text(c, "negativos", r.X(-3), 680, 30, "black", DEBT, ep(t, C["03.b"] + 1.0, 0.4))
        text(c, "positivos", r.X(3), 680, 30, "black", CASH, ep(t, C["03.b"] + 2.2, 0.4))
        r.dot(c, -5, DEBT, ep(t, C["03.b"] + 0.4, 0.4))
        return
    head(c, t, C["04"], "LEMBRETE 2", "POTÊNCIA", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["04.t"], 0.5)
    ftext(c, "2^3", 520, 400, 150, "black", INK, a0)
    ftext(c, "= 2 × 2 × 2", 660, 400, 80, "black", INK, ep(t, C["04.a"] + 0.8, 0.5), align="left")
    ftext(c, "= 8", 1160, 400, 80, "black", GREEN, ep(t, WT(C, "04", "oito"), 0.4), align="left")
    ab = ep(t, C["04.b"], 0.4)
    arrow(c, 470, 520, 490, 430, BLUE, ab, 4, 14)
    text(c, "BASE", 450, 560, 34, "black", BLUE, ab)
    ac = ep(t, C["04.c"], 0.4)
    arrow(c, 760, 245, 625, 285, BLUE, ac, 4, 14)
    text(c, "EXPOENTE", 780, 235, 34, "black", BLUE, ac, align="left")
    text(c, "quantas vezes a base aparece", 780, 275, 24, "bold", INK2, ac, align="left")
    ad = ep(t, C["04.d"], 0.5)
    tag(c, "x^2 = ao quadrado", 640, 660, BLUE, ad, 30)
    tag(c, "x^3 = ao cubo", 1110, 660, BLUE, ep(t, C["04.d"] + 1.3, 0.5), 30)
    ae = ep(t, C["04.e"], 0.5)
    regra(c, "2^3 ≠ 2 × 3", W / 2, 770, ae, 36, AMBER)


# ======================================================================
# bloco a: a ordem
# ======================================================================

def b_ordem_por_que(c, t, C, B):
    head(c, t, B["start"], "POR QUE NÃO SÓ DA", "ESQUERDA PARA A DIREITA?", BLUE)
    ftext(c, "2 + 3 × 4", W / 2, 260, 70, "black", INK2, ep(t, C["05.t"], 0.5))
    for k, (cue, seqs, ok) in enumerate((("05.a", ("MEIA", "SAPATO"), True), ("05.b", ("SAPATO", "MEIA"), False))):
        a, dy = rise(t, C[cue])
        if a <= 0:
            continue
        x = 260 + k * 720
        card(c, x, 320 + dy, 680, 300, a)
        for j, s in enumerate(seqs):
            badge_num(c, j + 1, x + 80 + j * 330, 420 + dy, a, 28, bg=GREEN if ok else RED)
            text_mid(c, s, x + 124 + j * 330, 420 + dy, 38, "black", INK, a, align="left")
        arrow(c, x + 270, 420 + dy, x + 360, 420 + dy, INK2, a, 4, 14)
        mark(c, ok, x + 340, 540 + dy, a, 32)
    regra(c, "a ORDEM muda o resultado", W / 2, 730, ep(t, C["05.c"], 0.5), 38)


def b_ordem_pronto_socorro(c, t, C, B):
    head(c, t, B["start"], "A FILA DE PRIORIDADE", "COMO NUM PRONTO-SOCORRO", PURPLE)
    a0 = ep(t, C["06.t"], 0.5)
    card(c, 200, 190, 480, 600, a0)
    if a0 > 0:   # cruz do pronto-socorro
        cx, cy = 440, 400
        rrect(c, cx - 40, cy - 120, 80, 240, 14, RED, a0)
        rrect(c, cx - 120, cy - 40, 240, 80, 14, RED, a0)
        text(c, "o mais GRAVE", 440, 620, 34, "black", INK, a0)
        text(c, "é atendido primeiro", 440, 670, 30, "bold", INK2, a0)
    cues = [C["06.a"], C["06.b"], C["06.c"], C["06.d"]]
    k = ativo_em(t, [(cu, i) for i, cu in enumerate(cues)])
    fila(c, 760, 190, a0, k, w=960, dy=120, cues=cues, t=t)


def _fila_lado(c, t, a, marcas):
    fila(c, 1310, 180, a, ativo_em(t, marcas), w=420, dy=72)


def b_ordem_gancho(c, t, C, B):
    head(c, t, B["start"], "VOLTANDO AO COMEÇO", "QUEM É ATENDIDO PRIMEIRO?", PURPLE)
    card(c, 160, 180, 1110, 600, ep(t, C["07.t"], 0.5))
    states = [dict(t=C["07.a"], s="a:2  b:+  c:3  d:×  e:4", hl="c d e", thl=C["07.b"]),
              dict(t=WT(C, "07", "doze"), s="a:2  b:+  f:12", hl="a b f", thl=C["07.d"]),
              dict(t=WT(C, "07", "catorze"), s="g:14")]
    expr(c, t, states, 715, 440, 110)
    fbox(c, "2 + 3 × 4 = 14", 715, 650, 48, ep(t, WT(C, "07", "catorze") + 0.6, 0.5))
    af = ep(t, C["07.f"], 0.5)
    if af > 0:
        ftext(c, "(2 + 3) × 4 = 20", 1500, 760, 34, "black", RED, af)
        text(c, "furou a fila", 1500, 806, 28, "black", RED, af)
    _fila_lado(c, t, ep(t, C["07.t"], 0.5), [(C["07.b"], 2), (C["07.d"], 3)])


def b_ordem_exemplo(c, t, C, B):
    head(c, t, B["start"], "EXEMPLO RESOLVIDO", "TODAS AS ETAPAS DA FILA", PURPLE)
    card(c, 160, 180, 1110, 600, ep(t, C["08.t"], 0.5))
    t3 = WT(C, "08", "tres", 1, C["08.b"])
    t9 = WT(C, "08", "nove", 1, C["08.c"])
    t18 = WT(C, "08", "dezoito", 1, C["08.d"])
    t32 = WT(C, "08", "trinta", 1, C["08.e"])
    states = [dict(t=C["08.a"], s="a:50  b:−  c:2  d:×  e:(  ~f:1  g:+  h:2  ~i:)  ~j:^2", hl="e f g h i", thl=C["08.b"]),
              dict(t=t3, s="a:50  b:−  c:2  d:×  k:3  ~j:^2", hl="k j", thl=C["08.c"]),
              dict(t=t9, s="a:50  b:−  c:2  d:×  l:9", hl="c d l", thl=C["08.d"]),
              dict(t=t18, s="a:50  b:−  m:18", hl="a b m", thl=C["08.e"]),
              dict(t=t32, s="n:32")]
    expr(c, t, states, 715, 470, 96)
    _fila_lado(c, t, ep(t, C["08.t"], 0.5), [(C["08.b"], 0), (C["08.c"], 1), (C["08.d"], 2), (C["08.e"], 3)])


def caixas(c, cx, cy, a, n, t0, t):
    """caixas encaixadas: ( ) dentro de [ ] dentro de { }"""
    labs = [("( )", 200, 120), ("[ ]", 330, 190), ("{ }", 460, 260)]
    for k in range(n):
        lab, w, h = labs[k]
        ak = a * ep(t, t0[k], 0.5)
        if ak <= 0:
            continue
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2, cy - h / 2, w, h), 18, 18),
                    paint([HL, BLUE, AMBER][k], ak, stroke=5))
        text(c, lab, cx - w / 2 + 34, cy - h / 2 + 34, 24, "black", [HL, BLUE, AMBER][k], ak)


def b_ordem_colchetes(c, t, C, B):
    head(c, t, B["start"], "PARÊNTESES, COLCHETES E CHAVES", "DE DENTRO PARA FORA", PURPLE)
    card(c, *CARD_R)
    caixas(c, 400, 400, 1.0, 3, [C["09.t"], C["09.a"], C["09.f"]], t)
    arrow(c, 400, 400, 640, 400, GREEN, ep(t, C["09.a"] + 0.8, 0.5), 5, 18)
    text(c, "abre de dentro para fora", 400, 600, 28, "black", GREEN, ep(t, C["09.a"] + 0.8, 0.5))
    t4 = WT(C, "09", "quatro", 1, C["09.c"])
    t6 = WT(C, "09", "seis", 1, C["09.d"])
    t12 = WT(C, "09", "doze", 1, C["09.e"])
    states = [dict(t=C["09.b"], s="a:2  b:×  c:[  ~d:10  e:−  f:(  ~g:3  h:+  i:1  ~j:)  ~k:]", hl="f g h i j", thl=C["09.c"]),
              dict(t=t4, s="a:2  b:×  c:[  ~d:10  e:−  l:4  ~k:]", hl="c d e l k", thl=C["09.d"]),
              dict(t=t6, s="a:2  b:×  m:6", hl="a b m", thl=C["09.e"]),
              dict(t=t12, s="n:12")]
    expr(c, t, states, 1200, 420, 76)
    text(c, "{ } = a caixa mais de fora", 1200, 700, 30, "black", AMBER, ep(t, C["09.f"], 0.5))


def b_ordem_empate(c, t, C, B):
    head(c, t, B["start"], "EMPATE NA FILA", "DA ESQUERDA PARA A DIREITA", PURPLE)
    card(c, *CARD_R)
    aa = ep(t, C["10.a"], 0.5)
    tag(c, "×  ÷   mesma prioridade", 560, 250, PURPLE, aa, 32)
    tag(c, "+  −   também", 1260, 250, PURPLE, ep(t, C["10.a"] + 1.4, 0.5), 32)
    ab = ep(t, C["10.b"], 0.5)
    arrow(c, 560, 350, 1360, 350, GREEN, ab, 6, 20, progress=ease_io(prog(t, C["10.b"], 1.0)))
    text(c, "ordem de chegada", 960, 330, 28, "black", GREEN, ab)
    t6 = WT(C, "10", "seis", 1, C["10.d"])
    t18 = WT(C, "10", "dezoito", 1, C["10.e"])
    states = [dict(t=C["10.c"], s="a:12  b:÷  c:2  d:×  e:3", hl="a b c", thl=C["10.d"]),
              dict(t=t6, s="f:6  d:×  e:3", hl="f d e", thl=C["10.e"]),
              dict(t=t18, s="g:18")]
    expr(c, t, states, W / 2, 560, 110)


# ======================================================================
# blocos b-c: sinais na soma (dinheiro que entra x dívida)
# ======================================================================

def b_sinal_def(c, t, C, B):
    head(c, t, B["start"], "OS SINAIS", "DINHEIRO QUE ENTRA × DÍVIDA", BLUE)
    aa = ep(t, C["11.a"], 0.5)
    ftext(c, "+5", 700, 360, 120, "black", INK, aa)
    ftext(c, "−5", 1220, 360, 120, "black", INK, aa)
    for cx, s_ in ((700, "+5"), (1220, "−5")):
        w, ws = ftext_w(s_, "black", 120), ftext_w(s_[0], "black", 120)
        c.drawCircle(cx - w / 2 + ws / 2, 360 - 120 * 0.36, 58, paint(BLUE, aa * 0.9, stroke=4))
    pill(c, "sinal = o + ou o − na frente do número", W / 2, 470, BLUE, size=28, a=aa, anchor="center")
    for k, (cue, s, sub, col, gl) in enumerate((("11.c", "POSITIVO", "dinheiro que entra", CASH, ""),
                                                 ("11.d", "NEGATIVO", "dívida", DEBT, ""))):
        a, dy = rise(t, C[cue])
        if a <= 0:
            continue
        x = 300 + k * 700
        card(c, x, 540 + dy, 620, 220, a)
        rrect(c, x, 540 + dy, 16, 220, 8, col, a)
        text(c, s, x + 60, 620 + dy, 42, "black", col, a, align="left")
        text(c, sub, x + 60, 690 + dy, 34, "bold", INK, a, align="left")
        ftext(c, "+" if k == 0 else "−", x + 540, 680 + dy, 110, "black", col, a)


def saldo_demo(c, t, C, rows, saldo_t, saldo, jumps, eq_t, eq, lo=-12, hi=2, a=1.0, eq_y=300, regra_t=None, regra_s=None):
    extrato(c, t, 170, 180, 560, rows, saldo_t, saldo, a)
    r = Reta(860, 1680, 560, lo, hi)
    ar = a * ep(t, rows[0][0], 0.5)
    card(c, 790, 400, 960, 260, ar)
    r.draw(c, ar)
    for tj, v0, v1, col, lab in jumps:
        r.jump(c, v0, v1, col, ar * ep(t, tj, 0.2), ease_io(prog(t, tj, 0.9)), lab)
    fbox(c, eq, 1270, eq_y, 56, a * ep(t, eq_t, 0.5), INK)
    if regra_t is not None:
        regra(c, regra_s, W / 2, 770, a * ep(t, regra_t, 0.5), 34, PURPLE, w=1500)


def b_sinais_iguais(c, t, C, B):
    head(c, t, B["start"], "SINAIS IGUAIS NA SOMA", "DÍVIDA COM DÍVIDA", BLUE)
    a1 = 1 - prog(t, C["13.a"] - 0.3, 0.4)
    saldo_demo(c, t, C, [(C["12.t"], "Dívida com o amigo", -7), (C["12.a"], "Mais uma dívida", -3)], C["12.b"], -10,
               [(C["12.d"], 0, -7, DEBT, "−7"), (C["12.d"] + 1.6, -7, -10, DEBT, "−3")],
               C["12.c"], "−7 − 3 = −10", a=a1, regra_t=C["13.b"], regra_s="SINAIS IGUAIS: soma e mantém o sinal")
    a2 = ep(t, C["13.a"], 0.5)
    if a2 > 0:
        extrato(c, t, 170, 180, 560, [(C["13.a"], "Salário", 5), (C["13.a"] + 0.6, "Pix recebido", 3)], C["13.a"] + 1.4, 8, a2)
        r = Reta(860, 1680, 560, -2, 10)
        card(c, 790, 400, 960, 260, a2)
        r.draw(c, a2)
        r.jump(c, 0, 5, CASH, a2, ease_io(prog(t, C["13.a"] + 0.4, 0.8)), "+5")
        r.jump(c, 5, 8, CASH, a2, ease_io(prog(t, C["13.a"] + 1.4, 0.8)), "+3")
        fbox(c, "+5 + 3 = +8", 1270, 300, 56, a2 * ep(t, C["13.a"] + 1.6, 0.5), INK)
        regra(c, "SINAIS IGUAIS: soma e mantém o sinal", W / 2, 770, ep(t, C["13.b"], 0.5), 34, PURPLE, w=1500)


def b_sinais_diferentes(c, t, C, B):
    head(c, t, B["start"], "SINAIS DIFERENTES NA SOMA", "DÍVIDA × DINHEIRO", BLUE)
    a1 = 1 - prog(t, C["15.t"] - 0.3, 0.4)
    if a1 > 0:
        saldo_demo(c, t, C, [(C["14.a"], "Dívida", -7), (C["14.b"], "Entrou na conta", 3)], C["14.d"], -4,
                   [(C["14.a"] + 0.5, 0, -7, DEBT, "−7"), (C["14.c"], -7, -4, CASH, "+3")],
                   C["14.e"], "−7 + 3 = −4", lo=-9, hi=5, a=a1)
    a2 = ep(t, C["15.t"], 0.5)
    if a2 > 0:
        saldo_demo(c, t, C, [(C["15.a"], "Dívida", -3), (C["15.a"] + 1.0, "Entrou na conta", 7)], C["15.b"], 4,
                   [(C["15.a"] + 0.4, 0, -3, DEBT, "−3"), (C["15.a"] + 1.4, -3, 4, CASH, "+7")],
                   WT(C, "15", "mais", 1, C["15.b"]), "−3 + 7 = +4", lo=-5, hi=7, a=a2,
                   regra_t=C["15.c"], regra_s="SINAIS DIFERENTES: subtrai e fica com o sinal do MAIOR")
        text(c, "maior = o que pesa mais, sem olhar o sinal", W / 2, 850, 26, "black", BLUE, ep(t, C["15.d"], 0.5))


# ======================================================================
# bloco d: multiplicar e dividir
# ======================================================================

def nota(c, x, y, v, a, risco=0.0):
    """cartão de dívida (nota vermelha) com valor"""
    if a <= 0:
        return
    rrect(c, x, y, 190, 110, 16, "#FFFFFF", a, shadow=True)
    rrect(c, x, y, 190, 26, 12, DEBT, a * 0.9)
    text(c, "DÍVIDA", x + 95, y + 20, 18, "black", "#FFFFFF", a)
    ftext(c, v, x + 95, y + 86, 44, "black", DEBT, a)
    if risco > 0:
        line(c, x - 6, y + 104, x + 196, y + 10, GREEN, a, 7, progress=risco)


def b_mult_sinais(c, t, C, B):
    head(c, t, B["start"], "E NA MULTIPLICAÇÃO?", "DÍVIDAS QUE SE SOMAM OU SE CANCELAM", BLUE)
    card(c, *CARD_R)
    for k in range(3):
        ak = ep(t, C["16.a"] + 0.4 * k, 0.4)
        risco = ease_io(prog(t, C["16.b"] + 0.9 + 0.4 * k, 0.5))
        nota(c, 260 + k * 230, 240, "−4", ak, risco)
    fbox(c, "3 × (−4) = −12", 520, 470, 50, ep(t, WT(C, "16", "doze", 1, C["16.a"]), 0.5), DEBT)
    ab = ep(t, C["16.b"], 0.5)
    text(c, "alguém CANCELA as 3 dívidas", 1320, 290, 34, "black", INK, ab)
    ac = ep(t, C["16.c"], 0.5)
    pill(c, "tirar dívida = ganhar", 1320, 370, GREEN, size=32, a=ac, anchor="center")
    fbox(c, "(−3) × (−4) = +12", 1320, 470, 50, ep(t, C["16.d"], 0.5), GREEN)
    a2 = ep(t, C["16.d"] + 1.0, 0.5)
    tag(c, "menos 3 vezes = TIRAR 3 vezes", 960, 680, BLUE, a2, 28)


def b_mult_regra(c, t, C, B):
    head(c, t, B["start"], "REGRA DE SINAIS", "MULTIPLICAR E DIVIDIR", PURPLE)
    card(c, *CARD_R)
    rows = [("17.a", "(+) × (+) = +", GREEN), ("17.a", "(−) × (−) = +", GREEN), ("17.b", "(+) × (−) = −", RED), ("17.b", "(−) × (+) = −", RED)]
    for k, (cue, s, col) in enumerate(rows):
        a, dy = rise(t, C[cue] + (k % 2) * 0.7)
        y = 270 + k * 100 + dy
        fmid(c, s, 260, y, 52, "black", INK, a, align="left")
    regra(c, "IGUAIS → +", 1010, 320, ep(t, C["17.a"], 0.5), 36, GREEN, w=340)
    regra(c, "DIFERENTES → −", 1010, 520, ep(t, C["17.b"], 0.5), 36, RED, w=340)
    ac = ep(t, C["17.c"], 0.5)
    pill(c, "÷ segue a MESMA regra", 1460, 260, PURPLE, size=28, a=ac, anchor="center")
    ftext(c, "(−12) ÷ 4 = −3", 1460, 440, 46, "black", INK, ep(t, C["17.d"], 0.5))
    ftext(c, "(−12) ÷ (−4) = +3", 1460, 560, 46, "black", INK, ep(t, C["17.e"], 0.5))


def b_mult_armadilha(c, t, C, B):
    head(c, t, B["start"], "ARMADILHA", "\"MENOS COM MENOS DÁ MAIS\"", AMBER)
    card(c, *CARD_R)
    aa = ep(t, C["18.a"], 0.5)
    regra(c, "− com − = +   só em  ×  e  ÷", W / 2, 300, aa, 44, AMBER, w=1100)
    ab = ep(t, C["18.b"], 0.5)
    ftext(c, "−7 − 3 = +10", 640, 520, 70, "black", RED, ab)
    strike(c, 400, 497, 880, 497, ab, RED, ease_io(prog(t, C["18.b"] + 0.8, 0.5)))
    fbox(c, "−7 − 3 = −10", 1290, 500, 64, ep(t, WT(C, "18", "dez", 1, C["18.b"]), 0.5), GREEN)
    text(c, "na SOMA: dívida com dívida", 1290, 650, 30, "black", INK2, ab)


# ======================================================================
# bloco e: menos antes de parênteses
# ======================================================================

def b_menos_parenteses(c, t, C, B):
    head(c, t, B["start"], "MENOS ANTES DE PARÊNTESES", "O CONTRÁRIO DE", BLUE)
    card(c, *CARD_R)
    a1 = 1 - prog(t, C["20.t"] - 0.3, 0.4)
    if a1 > 0:
        pill(c, "−( )  =  o contrário de", W / 2, 240, BLUE, size=32, a=a1 * ep(t, C["19.a"], 0.5), anchor="center")
        ab = a1 * ep(t, C["19.b"], 0.5)
        text(c, "dever R$ 12", 640, 380, 48, "black", DEBT, ab)
        arrow(c, 820, 365, 1060, 365, INK2, ab, 5, 18)
        text(c, "contrário", 940, 340, 24, "bold", INK2, ab)
        text(c, "ter R$ 12", 1260, 380, 48, "black", CASH, ab)
        states = [dict(t=C["19.c"], s="a:−  ~b:(  ~c:−12  ~d:)", hl="a b c d", thl=C["19.c"] + 0.8),
                  dict(t=WT(C, "19", "vira"), s="e:+12")]
        expr(c, t, states, W / 2, 600, 110, a1)
        return
    tf = WT(C, "20", "tres", 1, C["20.d"])
    states = [dict(t=C["20.a"], s="a:−  ~b:(  ~c:5  d:−  e:8  ~f:)", hl="a c d", thl=C["20.b"]),
              dict(t=C["20.c"], s="g:−5  h:+  e:8", hl="g h e", thl=C["20.d"]),
              dict(t=tf, s="i:3")]
    expr(c, t, states, W / 2, 350, 110)
    pill(c, "o − de fora INVERTE todos os sinais de dentro", W / 2, 230, PURPLE, size=28,
         a=ep(t, C["20.b"], 0.5), anchor="center")
    ae = ep(t, C["20.e"], 0.5)
    if ae > 0:
        rrect(c, 360, 520, 1200, 230, 22, GREEN, ae * 0.08)
        text(c, "CONFERINDO POR DENTRO", W / 2, 570, 26, "black", GREEN, ae)
        ftext(c, "5 − 8 = −3", 700, 680, 54, "black", INK, ae)
        ftext(c, "−(−3) = 3  ✓", 1220, 680, 54, "black", GREEN, ep(t, C["20.f"], 0.5))


# ======================================================================
# bloco f: base negativa
# ======================================================================

def b_base_negativa(c, t, C, B):
    head(c, t, B["start"], "BASE NEGATIVA", "EXPOENTE PAR OU ÍMPAR", PURPLE)
    card(c, *CARD_R)
    a1 = 1 - prog(t, C["22.t"] - 0.3, 0.4)
    if a1 > 0:
        ftext(c, "(−2)^4", W / 2, 280, 80, "black", INK, a1 * ep(t, C["21.a"], 0.5))
        t4 = WT(C, "21", "quatro", 1, C["21.b"])
        t8 = WT(C, "21", "oito", 1, C["21.c"])
        t16 = WT(C, "21", "dezesseis", 1, C["21.d"])
        states = [dict(t=C["21.a"] + 1.2, s="a:(−2)  b:×  c:(−2)  d:×  e:(−2)  f:×  g:(−2)", hl="a b c", thl=C["21.b"]),
                  dict(t=t4, s="h:4  d:×  e:(−2)  f:×  g:(−2)", hl="h d e", thl=C["21.c"]),
                  dict(t=t8, s="i:−8  f:×  g:(−2)", hl="i f g", thl=C["21.d"]),
                  dict(t=t16, s="j:16")]
        expr(c, t, states, W / 2, 520, 76, a1)
        fbox(c, "(−2)^4 = 16", W / 2, 720, 50, a1 * ep(t, t16 + 0.6, 0.5))
        return
    # 22: pares de sinais
    for row, (cue, n, res, col) in enumerate((("22.a", 4, "+", GREEN), ("22.b", 3, "−", RED))):
        a = ep(t, C[cue], 0.5)
        if a <= 0:
            continue
        y = 300 + row * 200
        ftext(c, "(−2)^4" if n == 4 else "(−2)^3", 330, y + 20, 64, "black", INK, a)
        for k in range(n):
            x = 620 + k * 130
            sozinho = n == 3 and k == 2
            cc = RED if sozinho else INK
            c.drawCircle(x, y, 42, paint(cc if sozinho else "#FFFFFF", a * (0.15 if sozinho else 1)))
            c.drawCircle(x, y, 42, paint(cc, a, stroke=3))
            fmid(c, "−", x, y, 54, "black", cc, a)
        ap = ep(t, C[cue] + 0.8, 0.5)
        for k in range(n // 2):
            x0, x1 = 620 + 2 * k * 130, 620 + (2 * k + 1) * 130
            p = skia.Path(); p.moveTo(x0, y + 50); p.quadTo((x0 + x1) / 2, y + 100, x1, y + 50)
            c.drawPath(p, paint(GREEN, ap, stroke=5, cap_round=True))
            text(c, "+", (x0 + x1) / 2, y + 112, 30, "black", GREEN, ap)
        if n == 3:
            text(c, "sozinho", 880, y + 100, 26, "black", RED, ap)
        ftext(c, "= " + ("16" if n == 4 else "−8"), 1320, y + 20, 64, "black", col, ep(t, C[cue] + 1.4, 0.5))
    regra(c, "expoente PAR → +", 640, 770, ep(t, C["22.c"], 0.5), 36, GREEN, w=560)
    regra(c, "expoente ÍMPAR → −", 1280, 770, ep(t, C["22.d"], 0.5), 36, RED, w=560)


# ======================================================================
# recapitulação
# ======================================================================

FRASES = ["Parênteses → potência → × ÷ → + −",
          "Multiplicação: iguais +, diferentes −",
          "Sem parênteses, o expoente não pega o −"]


def b_recap(c, t, C, B):
    sid = "23" if B["start"] < C["37"] - 1 else "37"
    head(c, t, B["start"], "AS 3 FRASES", "PARA GUARDAR", GREEN)
    card(c, *CARD_R)
    for k, (cue, col) in enumerate((("a", PURPLE), ("b", GREEN), ("c", AMBER))):
        a, d = rise(t, C[f"{sid}.{cue}"])
        y = 330 + k * 150 + d
        badge_num(c, k + 1, 250, y - 16, a, 32, bg=col)
        ftext(c, FRASES[k], 310, y, 50, "black", INK, a, align="left")
    pill(c, "a 3ª é o erro mais caro da prova", W / 2, 790, AMBER, size=28, a=ep(t, C["23.d"], 0.5) if sid == "23" else 0,
         anchor="center")


# ======================================================================
# bloco g: −3² x (−3)²
# ======================================================================

def b_menos_quadrado(c, t, C, B):
    head(c, t, B["start"], "O ERRO MAIS CARO DA PROVA", "−3²  ×  (−3)²", AMBER)
    for k in range(2):
        card(c, 180 + k * 800, 180, 760, 600, ep(t, C["24.t"], 0.5))
    a0 = ep(t, C["24.t"], 0.5)
    text(c, "SEM PARÊNTESES", 560, 250, 30, "black", INK2, a0)
    text(c, "COM PARÊNTESES", 1360, 250, 30, "black", INK2, a0)
    tn = WT(C, "24", "nove", 1, C["24.e"])
    sl = [dict(t=C["24.t"], s="a:−  ~b:3^2", hl="b", thl=C["24.d"]),
          dict(t=tn, s="a:−  ~c:9", hl="a c", thl=C["24.f"]),
          dict(t=C["24.f"] + 0.9, s="d:−9")]
    expr(c, t, sl, 560, 440, 110)
    sr = [dict(t=C["24.t"], s="a:(−3)^2", hl="a", thl=C["25.a"]),
          dict(t=C["25.b"], s="b:(−3)  c:×  d:(−3)", hl="b c d", thl=C["25.b"] + 1.4),
          dict(t=WT(C, "25", "nove", 1, C["25.b"]), s="e:+9")]
    expr(c, t, sr, 1360, 440, 110 if t < C["25.b"] else 80)
    ab = ep(t, C["24.b"], 0.4) * (1 - prog(t, C["24.d"], 0.4))
    fmid(c, "≠", W / 2 - 20, 440, 110, "black", RED, ab)
    ad = ep(t, C["24.d"], 0.5)
    text(c, "o expoente só pega o 3", 560, 600, 30, "black", HL, ad)
    text(c, "o − entra DEPOIS", 560, 650, 30, "black", HL, ep(t, C["24.f"], 0.5))
    ae = ep(t, C["25.a"], 0.5)
    if ae > 0:   # embrulho
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(1210, 360, 240, 150), 20, 20), paint(GREEN, ae, stroke=5, ))
        text(c, "EMBRULHO: vai tudo junto", 1360, 600, 30, "black", GREEN, ae * (1 - prog(t, C["25.b"], 0.4)))
    fbox(c, "−3² = −9", 560, 720, 46, ep(t, C["25.c"], 0.5), RED)
    fbox(c, "(−3)² = +9", 1360, 720, 46, ep(t, C["25.c"] + 1.0, 0.5), GREEN)
    _fila_mini(c, t, ep(t, C["24.c"], 0.4) * (1 - prog(t, C["24.e"], 0.4)))


def _fila_mini(c, t, a):
    if a > 0:
        fila(c, W / 2 - 210, 520, a, 1, w=420, dy=56, titulo=False)


# ======================================================================
# erros clássicos
# ======================================================================

def b_erro1(c, t, C, B):
    head(c, t, B["start"], "ERRO 1", "FURAR A FILA", RED)
    erro_tiles(c, t, [(C["26.a"], "O ERRO", ["!2 + 3 × 4 = 20"], RED),
                      (C["26.b"], "POR QUE PARECE CERTO", ["a gente lê da", "esquerda para a", "direita, como texto"], AMBER),
                      (C["26.c"], "A CORREÇÃO", ["o × vem antes", "!2 + 12 = 14"], GREEN)])


def b_erro2(c, t, C, B):
    head(c, t, B["start"], "ERRO 2", "O EXPOENTE PEGAR O MENOS", RED)
    erro_tiles(c, t, [(C["27.a"], "O ERRO", ["!−3² = 9"], RED),
                      (C["27.b"], "POR QUE PARECE CERTO", ["o − está colado", "no 3, e − com −", "dá +"], AMBER),
                      (C["27.c"], "A CORREÇÃO", ["sem parênteses,", "o expoente só", "pega o 3", "!−3² = −9"], GREEN)])


def b_erro3(c, t, C, B):
    head(c, t, B["start"], "ERRO 3", "ESQUECER O MENOS COM MENOS", RED)
    erro_tiles(c, t, [(C["28.a"], "O ERRO", ["!12 − (−12) = 0"], RED),
                      (C["28.b"], "POR QUE PARECE CERTO", ["você vê o 12 e", "o −, e pensa em", "12 − 12"], AMBER),
                      (C["28.c"], "A CORREÇÃO", ["são DOIS sinais:", "tirar dívida = ganhar", "!12 + 12 = 24"], GREEN)])


# ======================================================================
# exercício rápido
# ======================================================================

def b_exercicio(c, t, C, B):
    head(c, t, B["start"], "SUA VEZ", "PAUSE E CALCULE", GREEN)
    for k, (cue, s, rcue, res, why) in enumerate((("29.a", "(−2)^3", "30.a", "−8", "base negativa, expoente ímpar"),
                                                  ("29.b", "−2^2", "30.b", "−4", "o expoente só pega o 2"))):
        a, dy = rise(t, C[cue])
        if a <= 0:
            continue
        x = 220 + k * 780
        card(c, x, 200 + dy, 700, 520, a)
        ar = ep(t, C[rcue], 0.5)
        ftext(c, s + (" = ?" if ar < 0.5 else " ="), x + 350, 400 + dy, 96, "black", INK, a)
        ftext(c, res, x + 350, 560 + dy, 110, "black", GREEN, ar)
        text(c, why, x + 350, 660 + dy, 28, "black", INK2, ar)
    pause_badge(c, W / 2 - 170, 760, ep(t, C["29.p"], 0.5) * (1 - prog(t, C["30.t"] - 0.3, 0.4)))


# ======================================================================
# questão 3
# ======================================================================

ALTS = [("A", "R$ 2,00", "35.a", "(−2)³ = +8  e  −(−12) → −12"),
        ("B", "R$ 10,00", "36.b", "não vem de regra: chute"),
        ("C", "R$ 18,00", "36.c", "(−2)³ = −6  e  sem ÷ 4"),
        ("D", "R$ 22,00", None, ""),
        ("E", "R$ 26,00", "35.e", "(−2)³ = +8")]
ALT_CUE = ["32.a", "32.b", "32.c", "32.d", "32.e"]


def b_questao(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO ESTILO ENEM", "O SALDO DA CONTA", BLUE)
    card(c, 140, 180, 720, 640)
    pill(c, "QUESTÃO", 170, 224, BLUE, size=22, bounds=(0, 1920))
    text(c, "Saldo atualizado por (em reais):", 180, 310, 30, "black", INK2, ep(t, C["31.e1"], 0.5), align="left")
    ftext(c, "12 − 4 × (−3) + (−2)^3 ÷ 4", 500, 390, 46, "black", INK, ep(t, C["31.e2"], 0.5))
    text(c, "Qual é o saldo?", 180, 450, 30, "black", INK2, ep(t, C["31.e3"], 0.5), align="left")
    aok = ep(t, C["34.d"], 0.5)
    for k, (L, s, cue_x, why) in enumerate(ALTS):
        a, d = rise(t, C[ALT_CUE[k]])
        y = 520 + k * 62 + d
        ok = cue_x is None
        if ok and aok > 0:
            rrect(c, 170, y - 40, 660, 56, 12, GREEN, 0.15 * aok)
        badge_num(c, L, 205, y - 12, a, 21, bg=GREEN if ok and aok > 0.5 else INK)
        ax = ep(t, C[cue_x], 0.4) if cue_x else 0
        text(c, s, 240, y, 30, "black", INK, a * (1 - 0.55 * ax), align="left")
        if ax > 0:
            strike(c, 236, y - 10, 246 + text_w(s, "black", 30), y - 10, ax, RED, ax)
            ftext(c, why, 420, y - 2, 21, "black", RED, ax, align="left")
    pause_badge(c, 1180, 400, ep(t, C["32.p"], 0.5) * (1 - prog(t, C["33.t"] - 0.3, 0.4)))
    # resolução
    ar = ep(t, C["33.t"], 0.5)
    sol_card(c, 900, 180, 880, 640, ar)
    if ar <= 0:
        return
    t8 = WT(C, "33", "oito", 1, C["33.b"])
    t12 = WT(C, "33", "doze", 1, C["33.d"])
    t2 = WT(C, "33", "dois", -1)
    tA = C["34.a"] + 0.65 * (C["34.b"] - C["34.a"])
    tB = C["34.b"] + 0.65 * (C["34.c"] - C["34.b"])
    t22 = WT(C, "34", "vinte", 1, C["34.c"])
    states = [dict(t=C["33.t"], s="a:12  b:−  c:4  d:×  e:(−3)  f:+  g:(−2)^3  h:÷  i:4", hl="g", thl=C["33.a"]),
              dict(t=t8, s="a:12  b:−  c:4  d:×  e:(−3)  f:+  j:(−8)  h:÷  i:4", hl="c d e", thl=C["33.d"]),
              dict(t=t12, s="a:12  b:−  k:(−12)  f:+  j:(−8)  h:÷  i:4", hl="j h i", thl=C["33.e"]),
              dict(t=t2, s="a:12  b:−  k:(−12)  f:+  l:(−2)", hl="b k", thl=C["34.a"]),
              dict(t=tA, s="a:12  m:+  n:12  f:+  l:(−2)", hl="f l", thl=C["34.b"]),
              dict(t=tB, s="a:12  m:+  n:12  o:−  p:2", hl="a m n o p", thl=C["34.c"] - 0.2),
              dict(t=t22, s="q:22")]
    expr(c, t, states, 1340, 330, 50, ar)
    notas = [(C["33.a"], "1º potência: base negativa, expoente ímpar → −"),
             (C["33.d"], "2º vezes: sinais diferentes → −"),
             (C["33.e"], "2º dividir: sinais diferentes → −"),
             (C["34.a"], "3º −(−12): cancelar dívida = ganhar → +12"),
             (C["34.c"], "4º mais e menos")]
    for k, (tc, s) in enumerate(notas):
        a, dy = rise(t, tc)
        ftext(c, s, 940, 450 + k * 52 + dy, 24, "black", HL, a * ar, align="left")
    pill(c, "RESPOSTA: D · R$ 22,00", 1340, 740, GREEN, size=30, a=ep(t, C["34.d"], 0.5) * (1 - prog(t, C["36.x"] - 0.4, 0.4)), anchor="center", bounds=(0, 1920))
    pill(c, "refaça pela FILA", 1340, 740, GREEN, size=30, a=ep(t, C["36.x"], 0.5), anchor="center", bounds=(0, 1920))


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    head(c, t, B["start"], "PRÓXIMO EPISÓDIO", "OS CONJUNTOS NUMÉRICOS", PURPLE)
    card(c, *CARD_R)
    a0 = ep(t, C["38.t"], 0.5)
    r = Reta(300, 1620, 330, -5, 5)
    r.draw(c, a0, tint=True)
    aa = ep(t, C["38.a"], 0.5)
    text(c, "de onde vieram esses números?", W / 2, 490, 40, "black", INK, aa)
    ab = ep(t, C["38.b"], 0.5)
    for k, s in enumerate(("1/2", "0,75", "√2", "π")):
        tag(c, s, 600 + k * 240, 590, AMBER if k >= 2 else BLUE, ab * ep(t, C["38.b"] + 0.3 * k, 0.4), 34)
    text(c, "existe número que não é fração?", W / 2, 690, 32, "black", AMBER, ab)
    pill(c, "EPISÓDIO 2: CONJUNTOS NUMÉRICOS", W / 2, 790, PURPLE, size=32, a=ep(t, C["38.c"], 0.5), anchor="center")


def b_cta(c, t, C, B):
    cta(c, t, C["39.like"], C["39.sub"], C["39.bell"], C["39.com"], C["39.bye"], "Antes desta aula, você respondia 14 ou 20?")


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, ordem_por_que=b_ordem_por_que,
              ordem_pronto_socorro=b_ordem_pronto_socorro, ordem_gancho=b_ordem_gancho, ordem_exemplo=b_ordem_exemplo,
              ordem_colchetes=b_ordem_colchetes, ordem_empate=b_ordem_empate, sinal_def=b_sinal_def,
              sinais_iguais=b_sinais_iguais, sinais_diferentes=b_sinais_diferentes, mult_sinais=b_mult_sinais,
              mult_regra=b_mult_regra, mult_armadilha=b_mult_armadilha, menos_parenteses=b_menos_parenteses,
              base_negativa=b_base_negativa, recap=b_recap, menos_quadrado=b_menos_quadrado, erro1=b_erro1,
              erro2=b_erro2, erro3=b_erro3, exercicio=b_exercicio, questao=b_questao, ponte=b_ponte, cta=b_cta)
