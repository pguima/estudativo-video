"""Peças COMUNS da série Potenciação e Radiciação (019). Cada epN/roteiro/visual.py faz:

    import importlib.util; from pathlib import Path
    _p = Path(__file__).resolve().parents[2] / "comum.py"
    _s = importlib.util.spec_from_file_location("comum019", _p); K = importlib.util.module_from_spec(_s); _s.loader.exec_module(K)
    K.usar_tempos(Path(__file__).resolve().parents[1] / "audio" / "tempos.json")

Reexporta TUDO do 018/comum.py (fr, pizza, barra, reta, WT, which, frame, head_seq, para, wrap, boxed, regra, selo,
pause_timer, chip, erro_cards, ftext/fmid/fbox...) e troca expr/expr_w/alternativas por versões com a tipografia nova.

TIPOGRAFIA (expr, math_w, mdraw) — tokens separados por ESPAÇO (cada token pode ter a sua cor em `cores`):
    2^5   2^{-3}   10^{-8}   a^{m+n}   (-3)^2   (2/3)^{-2}   (2·10^{-2})^3   2^{3^2} (torre)   2^{1/2}
    √{50}   √[3]{54}   5√{2}   √{a·b}   √{√[3]{64}}   6/√{5}-√{2}   a/b (fração empilhada)   2|3/4 (misto)
  - "^" eleva o átomo anterior: grupo {…} ou um caractere. O expoente sai menor (0,6) e pode ter fração ou outra potência.
  - "/" fora de () {} [] faz fração empilhada (num/den); dentro de ( ) também (o parêntese cresce em volta).
  - "√[n]{…}" raiz com índice n pequeno; "√{…}" quadrada; o sinal é vetorial e o traço cobre o radicando.
  - "-" vira o menos tipográfico "−"; operadores (− + · × ÷ = < > ≠ ≈ ⟺ →) ganham respiro dos dois lados.
  - "|x|" (módulo) funciona como texto. Use "{}" vazio para separar átomos quando precisar.
"""
import importlib.util
import math
from functools import lru_cache
from pathlib import Path
import skia
import motor
motor.set_theme("claro")
from motor import *  # noqa
from aula import *  # noqa

_p18 = Path(__file__).resolve().parents[1] / "018_enem_matematica_fracoes" / "comum.py"
_s18 = importlib.util.spec_from_file_location("comum018_base", _p18)
F = importlib.util.module_from_spec(_s18); _s18.loader.exec_module(F)
motor.set_theme("claro")
for _k in dir(F):
    if not _k.startswith("__"):
        globals()[_k] = getattr(F, _k)

# cores das peças da série
PAPEL = "#FFFDF6"
PAPEL_BORDA = "#D8D2C2"
DEGRAU = "#EDEBE4"

expr018 = F.expr
expr_w018 = F.expr_w


def usar_tempos(path):
    F.usar_tempos(path)


# ======================================================================
# motor de tipografia matemática (caixas: w, asc, desc, draw)
# ======================================================================

OPS = set("−+·×÷=<>≠≈⟺→")


@lru_cache(None)
def _font(peso, size):
    return font(peso, size)


def _txt_pieces(s, peso, size):
    out, cur, cur_sym = [], "", None
    for ch in s:
        sym = not F._has(ch, peso)
        if cur and sym != cur_sym:
            out.append((cur, F._symfont(size) if cur_sym else _font(peso, size)))
            cur = ""
        cur += ch; cur_sym = sym
    if cur:
        out.append((cur, F._symfont(size) if cur_sym else _font(peso, size)))
    return out


class Txt:
    def __init__(self, s, size, peso, op=False):
        self.s, self.size, self.peso = s, size, peso
        self.pieces = _txt_pieces(s, peso, size)
        self.pad = size * 0.16 if op else 0
        self.w = sum(f.measureText(p) for p, f in self.pieces) + 2 * self.pad
        self.asc = size * 0.74
        self.desc = size * (0.2 if any(ch in "gjpqy,;()|" for ch in s) else 0.03)

    def draw(self, c, x, base, col, a):
        xx = x + self.pad
        for p, f in self.pieces:
            c.drawString(p, xx, base, f, paint(col, a))
            xx += f.measureText(p)


class Row:
    def __init__(self, items, size):
        self.items, self.size = items, size
        self.w = sum(b.w for b in items)
        self.asc = max([b.asc for b in items] + [size * 0.74])
        self.desc = max([b.desc for b in items] + [size * 0.03])

    def draw(self, c, x, base, col, a):
        for b in self.items:
            b.draw(c, x, base, col, a)
            x += b.w


class Frac:
    def __init__(self, num, den, size):
        self.num, self.den, self.size = num, den, size
        self.th = max(3.0, size * 0.075)
        self.gap = size * 0.14
        self.ax = size * 0.30                  # altura do traço acima da linha de base
        self.side = size * 0.14
        self.w = max(num.w, den.w) + 2 * self.side
        self.asc = self.ax + self.th / 2 + self.gap + num.desc + num.asc
        self.desc = max(0.0, den.asc + self.gap + self.th / 2 - self.ax + den.desc)

    def draw(self, c, x, base, col, a):
        y = base - self.ax
        self.num.draw(c, x + (self.w - self.num.w) / 2, y - self.th / 2 - self.gap - self.num.desc, col, a)
        line(c, x + self.side * 0.4, y, x + self.w - self.side * 0.4, y, col, a, self.th, cap_round=True)
        self.den.draw(c, x + (self.w - self.den.w) / 2, y + self.th / 2 + self.gap + self.den.asc, col, a)


class Sup:
    def __init__(self, base, exp, size):
        self.b, self.e, self.size = base, exp, size
        self.shift = max(size * 0.40, base.asc - exp.asc * 0.62, exp.desc + size * 0.34)
        self.kern = size * 0.04
        self.w = base.w + self.kern + exp.w
        self.asc = max(base.asc, self.shift + exp.asc)
        self.desc = base.desc

    def draw(self, c, x, base, col, a):
        self.b.draw(c, x, base, col, a)
        self.e.draw(c, x + self.b.w + self.kern, base - self.shift, col, a)


class Paren:
    def __init__(self, inner, size, l="(", r=")"):
        self.inner, self.size = inner, size
        self.top = max(inner.asc + size * 0.10, size * 0.84)
        self.bot = max(inner.desc + size * 0.10, size * 0.18)
        h = self.top + self.bot
        self.pw = min(size * 0.42, max(size * 0.30, h * 0.20))
        self.w = inner.w + 2 * self.pw
        self.asc, self.desc = self.top, self.bot

    def _arc(self, c, x0, base, left, col, a):
        h = self.top + self.bot
        y0, y1 = base - self.top, base + self.bot
        sw = max(3.0, self.size * 0.085)
        p = skia.Path()
        xo = x0 + self.pw * (0.78 if left else 0.22)
        xi = x0 + self.pw * (0.12 if left else 0.88)
        p.moveTo(xo, y0)
        p.cubicTo(xi, y0 + h * 0.22, xi, y1 - h * 0.22, xo, y1)
        c.drawPath(p, paint(col, a, stroke=sw, cap_round=True))

    def draw(self, c, x, base, col, a):
        self._arc(c, x, base, True, col, a)
        self.inner.draw(c, x + self.pw, base, col, a)
        self._arc(c, x + self.pw + self.inner.w, base, False, col, a)


class Rad:
    def __init__(self, inner, idx, size):
        self.inner, self.idx, self.size = inner, idx, size
        self.sw = max(3.0, size * 0.075)
        self.pad = size * 0.14
        self.top = inner.asc + size * 0.16 + self.sw
        self.bot = max(inner.desc, size * 0.06) + size * 0.04
        self.signw = size * 0.52
        self.ix = max(0.0, (idx.w - self.signw * 0.42)) if idx else 0.0
        self.w = self.ix + self.signw + inner.w + self.pad * 1.0
        self.asc = self.top + (max(0.0, idx.asc + idx.desc - self.top * 0.45) if idx else 0)
        self.desc = self.bot

    def draw(self, c, x, base, col, a):
        x0 = x + self.ix
        yt, yb = base - self.top, base + self.bot
        p = skia.Path()
        p.moveTo(x0, base - self.size * 0.28)
        p.lineTo(x0 + self.signw * 0.22, base - self.size * 0.36)
        p.lineTo(x0 + self.signw * 0.50, yb)
        p.lineTo(x0 + self.signw * 0.92, yt)
        p.lineTo(x0 + self.signw + self.inner.w + self.pad * 0.6, yt)
        pa = paint(col, a, stroke=self.sw)
        pa.setStrokeJoin(skia.Paint.kRound_Join); pa.setStrokeCap(skia.Paint.kRound_Cap)
        c.drawPath(p, pa)
        if self.idx:
            self.idx.draw(c, x0 + self.signw * 0.34 - self.idx.w, base - self.size * 0.46 - self.idx.desc, col, a)
        self.inner.draw(c, x0 + self.signw + self.pad * 0.15, base, col, a)


class Gap:
    def __init__(self, w):
        self.w, self.asc, self.desc = w, 0, 0

    def draw(self, *a):
        pass


def _match(s, i, o, cl):
    d = 0
    for j in range(i, len(s)):
        if s[j] == o:
            d += 1
        elif s[j] == cl:
            d -= 1
            if d == 0:
                return j
    raise ValueError(f"sem fechamento em {s!r}")


def _top(s, ch):
    d = 0
    for i, x in enumerate(s):
        if x in "({[":
            d += 1
        elif x in ")}]":
            d -= 1
        elif x == ch and d == 0:
            return i
    return -1


def _parse(s, size, peso, disp=True):
    """expressão (sem espaços) → caixa. disp=True: frações em 0,82 do tamanho (como no 018)."""
    s = s.replace("-", "−")
    k = _top(s, "|")
    if k > 0 and _top(s, "/") > k and s[:k].lstrip("−").isdigit():   # misto 2|3/4
        ip = Txt(s[:k], size * 1.12, peso)
        return Row([ip, Gap(size * 0.06), _parse(s[k + 1:], size, peso, disp)], size)
    k = _top(s, "/")
    if k > 0:
        fs = size * (0.82 if disp else 1.0)
        return Frac(_seq(s[:k], fs, peso), _seq(s[k + 1:], fs, peso), fs)
    return _seq(s, size, peso)


def _seq(s, size, peso):
    items, buf, i = [], "", 0

    def flush():
        nonlocal buf
        if buf:
            items.append(Txt(buf, size, peso))
            buf = ""

    while i < len(s):
        ch = s[i]
        if ch == "{":
            flush(); j = _match(s, i, "{", "}")
            items.append(_parse(s[i + 1:j], size, peso, True) if j > i + 1 else Gap(0)); i = j + 1
        elif ch == "(":
            flush(); j = _match(s, i, "(", ")")
            items.append(Paren(_parse(s[i + 1:j], size, peso, True), size)); i = j + 1
        elif ch == "√":
            flush(); i += 1; idx = None
            if i < len(s) and s[i] == "[":
                j = _match(s, i, "[", "]"); idx = _parse(s[i + 1:j], size * 0.5, peso, False); i = j + 1
            if i < len(s) and s[i] == "{":
                j = _match(s, i, "{", "}"); inner = _parse(s[i + 1:j], size, peso, True); i = j + 1
            else:
                j = i
                while j < len(s) and (s[j].isalnum() or s[j] == ","):
                    j += 1
                inner = Txt(s[i:j], size, peso); i = j
            items.append(Rad(inner, idx, size))
        elif ch == "^":
            flush(); i += 1
            if i < len(s) and s[i] == "{":
                j = _match(s, i, "{", "}"); e = _parse(s[i + 1:j], size * 0.6, peso, False); i = j + 1
            else:
                e = Txt(s[i], size * 0.6, peso); i += 1
            base = items.pop() if items else Txt("", size, peso)
            if isinstance(base, Txt) and len(base.s) > 1 and not base.pad:   # "2·10^3": só o último número sobe
                cut = len(base.s)
                while cut > 0 and (base.s[cut - 1].isalnum() or base.s[cut - 1] == ","):
                    cut -= 1
                if 0 < cut < len(base.s):
                    items.append(Txt(base.s[:cut], size, peso)); base = Txt(base.s[cut:], size, peso)
            items.append(Sup(base, e, size))
        elif ch in OPS:
            flush()
            first = not items
            items.append(Txt(ch, size, peso, op=not first))
            i += 1
        else:
            buf += ch; i += 1
    flush()
    if len(items) == 1:
        return items[0]
    return Row(items, size)


@lru_cache(4096)
def _tok(tok, size, peso):
    return _parse(tok, size, peso, True)


def math_w(s, size, peso="black", gap=None):
    toks = s.split()
    gap = size * 0.32 if gap is None else gap
    return sum(_tok(t, size, peso).w for t in toks) + gap * max(0, len(toks) - 1)


expr_w = math_w


def math_box(s, size, peso="black"):
    """(largura, altura acima do centro, altura abaixo do centro) de uma linha de expr — para encaixar em cartões"""
    toks = [_tok(t, size, peso) for t in s.split()]
    base = size * 0.36
    return math_w(s, size, peso), max(b.asc for b in toks) - base, max(b.desc for b in toks) + base


def expr(c, s, cx, cy, size, a=1.0, cores=None, align="center", peso="black", gap=None, alfas=None):
    """linha matemática centrada verticalmente em cy (linha de base = cy + 0,36·size, igual ao texto do motor).
    cores/alfas: {índice do token: valor}. Devolve a largura."""
    toks = s.split()
    gap = size * 0.32 if gap is None else gap
    total = math_w(s, size, peso, gap)
    if a <= 0:
        return total
    x = cx - total / 2 if align == "center" else (cx - total if align == "right" else cx)
    base = cy + size * 0.36
    for i, t_ in enumerate(toks):
        b = _tok(t_, size, peso)
        ai = a * (alfas or {}).get(i, 1.0)
        if ai > 0:
            b.draw(c, x, base, (cores or {}).get(i, INK), ai)
        x += b.w + gap
    return total


def mdraw(c, s, x, cy, size, col=None, a=1.0, align="left", peso="black"):
    """atalho: expr de uma cor só, alinhada à esquerda por padrão"""
    toks = s.split()
    return expr(c, s, x, cy, size, a, cores={i: col or INK for i in range(len(toks))}, align=align, peso=peso)


# ======================================================================
# alternativas (mesma API do 018, com a tipografia nova)
# ======================================================================

def alternativas(c, t, C, alts, x, y0, w, size, ok_cue, okL, cues_in, cues_x=None, gap=18):
    """lista A–E. alts = [(letra, texto_ou_expr, motivo_do_erro, cor_do_motivo)]; texto que começa com '=' é desenhado com
    expr (potências, raízes, frações). cues_in = {letra: instante de entrada}; cues_x = {letra: instante do risco}."""
    aok = ep(t, ok_cue, 0.5)
    y = y0
    for L, s, why, col in alts:
        a, d = rise(t, cues_in.get(L, 1e9))
        ok = L == okL
        is_expr = s.startswith("=")
        if is_expr:
            ww, up, dn = math_box(s[1:].strip(), size * 1.15)
            hh = max(size * 1.6, up + dn + 16)
        else:
            lines = wrap(s, "bold", size, w - 70)
            hh = len(lines) * (size + 8) + 10
        ax = ep(t, (cues_x or {}).get(L, 1e9), 0.4) if not ok else 0
        if a > 0:
            if ok and aok > 0:
                rrect(c, x - 20, y - 10 + d, w + 30, hh + 20, 14, GREEN, 0.15 * aok)
            badge_num(c, L, x + 10, y + hh / 2 + d, a, 22, bg=GREEN if ok and aok > 0.5 else INK)
            if is_expr:
                cyy = y + d + 8 + up
                expr(c, s[1:].strip(), x + 50, cyy, size * 1.15, a * (1 - 0.5 * ax), align="left")
                if ax > 0:
                    strike(c, x + 46, cyy, x + 54 + ww, cyy, ax, RED, ax)
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


# ======================================================================
# peças da série
# ======================================================================

def atalho(c, x, y, w, h, titulo, linhas, a, size=34):
    """caixa verde de ATALHO: linhas = lista de strings (texto) ou ('m', expr) para matemática"""
    if a <= 0:
        return
    boxed(c, x, y, w, h, GREEN, a, 0.08)
    text(c, titulo, x + w / 2, y + 44, 22, "black", GREEN, a, tracking=2)
    n = len(linhas)
    for k, ln in enumerate(linhas):
        yy = y + 70 + (h - 90) * (k + 0.5) / n
        if isinstance(ln, tuple):
            expr(c, ln[1], x + w / 2, yy, size, a, cores={i: INK for i in range(20)})
        else:
            text_mid(c, ln, x + w / 2, yy, size, "black", INK, a)


def selo_teste(c, x, y, a, ok=False, s="TESTE COM 2 E 3"):
    """selo do teste com números pequenos (verde = confirmou, vermelho = desmentiu)"""
    selo(c, x, y, a, s, GREEN if ok else RED, -5, 28)


def folha(c, cx, cy, w, h, dobras, a=1.0, prog_=1.0, cor=None):
    """folha de papel vista de frente depois de `dobras` dobras ao meio (alternando vertical/horizontal);
    prog_ = 0..1 anima a dobra seguinte (a metade de cima/direita gira sobre a outra). Devolve (w, h) atuais."""
    if a <= 0:
        return w, h
    cor = cor or PAPEL
    ww, hh = w, h
    for k in range(dobras):
        if k % 2 == 0:
            ww /= 2
        else:
            hh /= 2
    camadas = 2 ** dobras
    # pilha: deslocamentos pequenos mostram as camadas
    vis = min(camadas, 6)
    for j in range(vis - 1, -1, -1):
        off = j * 5
        rrect(c, cx - ww / 2 + off, cy - hh / 2 + off, ww, hh, 6, mix(cor, PAPEL_BORDA, 0.25 + 0.1 * j), a, shadow=(j == vis - 1))
    rrect(c, cx - ww / 2, cy - hh / 2, ww, hh, 6, cor, a)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - ww / 2, cy - hh / 2, ww, hh), 6, 6), paint(PAPEL_BORDA, a, stroke=3))
    if 0 < prog_ < 1:   # a próxima dobra em andamento: metade levantando
        if dobras % 2 == 0:
            sx = math.cos(math.pi * prog_)
            x_mid = cx
            wid = ww / 2 * sx
            rrect(c, min(x_mid, x_mid + wid), cy - hh / 2, abs(wid), hh, 6, mix(cor, "#FFFFFF", 0.3) if sx > 0 else mix(cor, PAPEL_BORDA, 0.15), a,
                  shadow=True)
            line(c, x_mid, cy - hh / 2, x_mid, cy + hh / 2, PAPEL_BORDA, a, 3)
        else:
            sy = math.cos(math.pi * prog_)
            y_mid = cy
            hei = hh / 2 * sy
            rrect(c, cx - ww / 2, min(y_mid, y_mid - hei), ww, abs(hei), 6, mix(cor, "#FFFFFF", 0.3) if sy > 0 else mix(cor, PAPEL_BORDA, 0.15), a,
                  shadow=True)
            line(c, cx - ww / 2, y_mid, cx + ww / 2, y_mid, PAPEL_BORDA, a, 3)
    return ww, hh


def contador(c, cx, cy, valor, a=1.0, rotulo="camadas", col=None, size=110):
    """contador grande (número + rótulo embaixo)"""
    if a <= 0:
        return
    col = col or BLUE
    card(c, cx - 150, cy - 110, 300, 230, a)
    text_mid(c, str(valor), cx, cy - 15, size, "black", col, a)
    text(c, rotulo, cx, cy + 85, 30, "black", INK2, a)


def escada(c, x0, y0, degraus, passo_x, passo_y, a=1.0, ativos=None, cor_ativa=None, size=54, larg=None, alt=110,
           setas=None, rotulo_seta="÷ 2"):
    """escada que DESCE da esquerda para a direita. degraus = [(expr, valor_expr)], ativos = {índice: alfa};
    setas = {índice: alfa} desenha a seta 'rotulo_seta' do degrau i para o i+1."""
    if a <= 0:
        return
    cor_ativa = cor_ativa or PURPLE
    larg = larg or passo_x - 10
    ativos = ativos or {}
    setas = setas or {}
    for i, (s, v) in enumerate(degraus):
        ai = a * ativos.get(i, 0.0)
        x, y = x0 + i * passo_x, y0 + i * passo_y
        if ai <= 0:
            continue
        rrect(c, x, y, larg, alt, 14, DEGRAU, ai, shadow=True)
        rrect(c, x, y, larg, 10, 5, cor_ativa, ai * 0.8)
        expr(c, s, x + larg / 2, y + alt * 0.36, size * 0.72, ai, cores={0: INK})
        expr(c, v, x + larg / 2, y + alt * 0.78, size * 0.62, ai, cores={0: cor_ativa})
    for i, sa in setas.items():
        sa *= a
        if sa <= 0 or i + 1 >= len(degraus):
            continue
        x1, y1 = x0 + i * passo_x + larg * 0.62, y0 + i * passo_y - 18
        x2, y2 = x0 + (i + 1) * passo_x + larg * 0.38, y0 + (i + 1) * passo_y - 18
        p = skia.Path(); p.moveTo(x1, y1); p.quadTo((x1 + x2) / 2, min(y1, y2) - 70, x2, y2)
        c.drawPath(p, paint(AMBER, sa, stroke=5, cap_round=True))
        ang = math.atan2(y2 - (min(y1, y2) - 70), x2 - (x1 + x2) / 2)
        for s_ in (-1, 1):
            c.drawLine(x2, y2, x2 - 18 * math.cos(ang + s_ * 0.5), y2 - 18 * math.sin(ang + s_ * 0.5), paint(AMBER, sa, stroke=5, cap_round=True))
        fmid(c, rotulo_seta, (x1 + x2) / 2, min(y1, y2) - 70, 30, "black", AMBER, sa)


def fila(c, x, cy, fatores, a=1.0, cores=None, size=56, gap=12, alfas=None, rotulo=None):
    """fila de fatores iguais em fichas (ex.: ['2','2','2']); devolve a largura. cores/alfas por índice."""
    if a <= 0:
        return 0
    cores, alfas = cores or {}, alfas or {}
    wch = size * 1.25
    for i, f_ in enumerate(fatores):
        ai = a * alfas.get(i, 1.0)
        col = cores.get(i, BLUE)
        xx = x + i * (wch + gap)
        if ai <= 0:
            continue
        rrect(c, xx, cy - wch / 2, wch, wch, 14, mix("#FFFFFF", col, 0.16), ai)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(xx, cy - wch / 2, wch, wch), 14, 14), paint(col, ai, stroke=3))
        expr(c, f_, xx + wch / 2, cy, size * 0.7, ai, cores={0: col})
    w = len(fatores) * (wch + gap) - gap
    if rotulo:
        text(c, rotulo, x + w / 2, cy + wch / 2 + 44, 28, "black", INK2, a)
    return w
