"""Visual — Operações e Conjuntos Numéricos, Episódio 4: Diagrama de Venn — a questão "ponto garantido" (iniciantes, tema claro)
Cores com função: azul = definição · roxo = fórmula · âmbar = armadilha ("apenas" sempre sublinhado em âmbar) ·
verde = atalho/dica/acerto · vermelho = erro.
Peças próprias deste episódio:
- Venn2 / Venn3: cada REGIÃO é um caminho (operações booleanas do skia) que se pinta e recebe o número quando é calculada.
- pessoa(): bonequinhos dentro dos círculos; os do meio piscam em dobro ("contado 2×") e o fantasma some ao descontar.
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
ARQUIVO_FINAL = "enem_matematica_conjuntos_ep4_venn.mp4"
CARD_R = (140, 150, 1640, 690)
SYM = "C:/Windows/Fonts/seguisym.ttf"
CA, CB, CC = "#3B6CF6", "#E8A317", "#16A36A"     # cores dos círculos (A / B / C)
MEIO = "#7C5CFA"
FORA = "#8E8E93"


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
# texto matemático (^sobrescrito) com fonte reserva
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


def apenas_txt(c, s, x, y, size, color, a, align="left", peso="black", sub=1.0):
    """escreve s; a palavra 'apenas' sai em âmbar e sublinhada (sub = progresso do sublinhado)"""
    if a <= 0:
        return
    w = ftext_w(s, peso, size)
    xx = x - w / 2 if align == "center" else x
    partes = re.split(r"(apenas|APENAS)", s)
    for p in partes:
        if not p:
            continue
        is_ap = p.lower() == "apenas"
        ftext(c, p, xx, y, size, peso, AMBER if is_ap else color, a, align="left")
        pw = ftext_w(p, peso, size)
        if is_ap:
            line(c, xx, y + size * 0.18, xx + pw, y + size * 0.18, AMBER, a, max(3, size * 0.09), progress=sub)
        xx += pw


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
            apenas_txt(c, ln.lstrip("!"), x + cw / 2, y + 250 + j * 60, 44 if big else 32,
                       (RED if k == 0 else GREEN if k == 2 else INK) if big else INK, a, align="center")


# ======================================================================
# Venn
# ======================================================================

def _circ(x, y, r):
    p = skia.Path(); p.addCircle(x, y, r); return p


def _op(a, b, kind):
    return skia.Op(a, b, {"-": skia.PathOp.kDifference_PathOp, "&": skia.PathOp.kIntersect_PathOp,
                          "|": skia.PathOp.kUnion_PathOp}[kind])


class Venn2:
    def __init__(self, cx, cy, r, d, rect_pad=70):
        self.cx, self.cy, self.r, self.d = cx, cy, r, d
        self.xa, self.xb = cx - d / 2, cx + d / 2
        self.A, self.B = _circ(self.xa, cy, r), _circ(self.xb, cy, r)
        self.rect = skia.Rect.MakeLTRB(self.xa - r - rect_pad, cy - r - rect_pad, self.xb + r + rect_pad, cy + r + rect_pad)
        U = skia.Path(); U.addRect(self.rect)
        AB = _op(self.A, self.B, "|")
        self.reg = dict(a=_op(self.A, self.B, "-"), m=_op(self.A, self.B, "&"), b=_op(self.B, self.A, "-"),
                        f=_op(U, AB, "-"), A=self.A, B=self.B, U=AB, nA=_op(U, self.A, "-"))
        self.pos = dict(a=(self.xa - r * 0.42, cy), m=(cx, cy), b=(self.xb + r * 0.42, cy),
                        f=(self.rect.right() - 70, self.rect.bottom() - 40))

    def pinta(self, c, k, col, a, alpha=0.30):
        if a > 0:
            c.drawPath(self.reg[k], paint(col, a * alpha))

    def base(self, c, a, la="A", lb="B", universo=False, ua=1.0):
        if a <= 0:
            return
        if universo:
            c.drawRoundRect(self.rect, 24, 24, paint(INK2, a * ua, stroke=3))
        c.drawPath(self.A, paint(CA, a, stroke=6))
        c.drawPath(self.B, paint(CB, a, stroke=6))
        fmid(c, la, self.xa - self.r * 0.55, self.cy - self.r - 32, 34, "black", CA, a)
        fmid(c, lb, self.xb + self.r * 0.55, self.cy - self.r - 32, 34, "black", CB, a)

    def num(self, c, k, s, a, col=INK, size=56):
        if a <= 0:
            return
        x, y = self.pos[k]
        sc = 0.7 + 0.3 * ease_back(clamp(a))
        c.save(); c.translate(x, y); c.scale(sc, sc)
        fmid(c, s, 0, 0, size, "black", col, a)
        c.restore()


class Venn3:
    def __init__(self, cx, cy, r):
        self.cx, self.cy, self.r = cx, cy, r
        cf = (cx - 0.58 * r, cy - 0.34 * r); cv = (cx + 0.58 * r, cy - 0.34 * r); cn = (cx, cy + 0.66 * r)
        self.cs = (cf, cv, cn)
        F, V, N = (_circ(*p, r) for p in self.cs)
        self.F, self.V, self.N = F, V, N
        FV, FN, VN = _op(F, V, "&"), _op(F, N, "&"), _op(V, N, "&")
        m = _op(FV, N, "&")
        self.rect = skia.Rect.MakeLTRB(cf[0] - r - 50, cf[1] - r - 50, cv[0] + r + 50, cn[1] + r + 40)
        U = skia.Path(); U.addRect(self.rect)
        self.reg = dict(m=m, fv=_op(FV, N, "-"), fn=_op(FN, V, "-"), vn=_op(VN, F, "-"),
                        f=_op(_op(F, V, "-"), N, "-"), v=_op(_op(V, F, "-"), N, "-"), n=_op(_op(N, F, "-"), V, "-"),
                        fora=_op(U, _op(_op(F, V, "|"), N, "|"), "-"))
        self.pos = dict(m=(cx, cy + 0.04 * r), fv=(cx, cy - 0.62 * r), fn=(cx - 0.5 * r, cy + 0.36 * r),
                        vn=(cx + 0.5 * r, cy + 0.36 * r), f=(cx - 1.0 * r, cy - 0.5 * r), v=(cx + 1.0 * r, cy - 0.5 * r),
                        n=(cx, cy + 1.2 * r), fora=(self.rect.right() - 60, self.rect.bottom() - 34))

    def pinta(self, c, k, col, a, alpha=0.30):
        if a > 0:
            c.drawPath(self.reg[k], paint(col, a * alpha))

    def base(self, c, a, labs=("F", "V", "N"), universo=False):
        if a <= 0:
            return
        if universo:
            c.drawRoundRect(self.rect, 24, 24, paint(INK2, a, stroke=3))
        for p, col in zip((self.F, self.V, self.N), (CA, CB, CC)):
            c.drawPath(p, paint(col, a, stroke=6))
        (fx, fy), (vx, vy), (nx, ny) = self.cs
        fmid(c, labs[0], fx - self.r * 0.75, fy - self.r * 0.8, 30, "black", CA, a)
        fmid(c, labs[1], vx + self.r * 0.75, vy - self.r * 0.8, 30, "black", CB, a)
        fmid(c, labs[2], nx + self.r * 0.95, ny + self.r * 0.7, 30, "black", CC, a)

    def num(self, c, k, s, a, col=INK, size=44):
        if a <= 0:
            return
        x, y = self.pos[k]
        sc = 0.7 + 0.3 * ease_back(clamp(a))
        c.save(); c.translate(x, y); c.scale(sc, sc)
        fmid(c, s, 0, 0, size, "black", col, a)
        c.restore()


def pessoa(c, x, y, col, a, s=1.0):
    if a <= 0:
        return
    c.drawCircle(x, y - 22 * s, 10 * s, paint(col, a))
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x - 14 * s, y - 9 * s, 28 * s, 32 * s), 12 * s, 12 * s), paint(col, a))


def multidao(c, cx, cy, n, col, a, t0, t, s=0.9, cols=3, dx=40, dy=52):
    for k in range(n):
        i, j = k % cols, k // cols
        x = cx + (i - (cols - 1) / 2) * dx
        y = cy + (j - 0.5) * dy
        pessoa(c, x, y, col, a * ep(t, t0 + 0.08 * k, 0.3), s)


# ======================================================================
# gancho, promessa, pré-requisitos
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "DIAGRAMA DE VENN · EPISÓDIO 4", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["01.a"], 0.5)
    v = Venn2(560, 470, 170, 200)
    v.pinta(c, "m", MEIO, a0 * (0.5 + 0.5 * math.sin(t * 3)))
    v.base(c, a0)
    text(c, "a questão mais PREVISÍVEL", 1250, 300, 40, "black", INK, a0)
    pill(c, "cai quase todo ano", 1250, 380, BLUE, size=30, a=ep(t, C["01.b"], 0.4), anchor="center")
    pill(c, "só  +  e  −", 1250, 460, GREEN, size=30, a=ep(t, C["01.c"], 0.4), anchor="center")
    text(c, "o erro mora em uma palavra:", 1250, 570, 30, "black", INK2, ep(t, C["01.d"], 0.4))
    ae = ep(t, C["01.e"], 0.5)
    apenas_txt(c, "APENAS", 1250, 680, 96, AMBER, ae, align="center", sub=ease_io(prog(t, C["01.e"] + 0.3, 0.6)))


def b_promessa(c, t, C, B):
    head(c, t, B["start"], "AO FINAL DESTA AULA", "VOCÊ VAI CONSEGUIR", GREEN)
    cards_row(c, t, [("2", "Venn com\ndois grupos", C["02.a"], CA),
                     ("3", "Venn com\ntrês grupos", C["02.b"], CB),
                     ("✓", "sem decorar\nfórmula", C["02.c"], GREEN)], cw=440, chh=420, title_size=40)


def b_prereq(c, t, C, B):
    head(c, t, B["start"], "PRÉ-REQUISITO", "SÓ SOMA E SUBTRAÇÃO", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["03.a"], 0.5)
    fmid(c, "+", 700, 400, 200, "black", GREEN, a0)
    fmid(c, "−", 1220, 400, 200, "black", RED, a0)
    regra(c, "nenhuma conta difícil", W / 2, 620, ep(t, C["03.b"], 0.5), 40, GREEN)
    tag(c, "o que você precisa: um DESENHO", W / 2, 760, BLUE, ep(t, C["03.c"], 0.5), 30)


# ======================================================================
# a) o diagrama (festa)
# ======================================================================

V_FESTA = lambda: Venn2(1150, 500, 220, 260)


def festa_venn(c, t, v, a, t_pessoas, meio_col=MEIO, blink=0.0, fantasma=0.0):
    v.base(c, a, "noiva", "noivo")
    multidao(c, v.pos["a"][0] - 20, v.cy, 9, CA, a, t_pessoas, t)
    multidao(c, v.pos["b"][0] + 20, v.cy, 6, CB, a, t_pessoas + 0.4, t, cols=2)
    for k in range(5):
        x, y = v.cx + (k - 2) * 0 + (0 if k == 2 else (-28 if k % 2 else 28)), v.cy - 70 + k * 36
        ak = a * ep(t, t_pessoas + 0.8 + 0.1 * k, 0.3)
        pessoa(c, x, y, meio_col, ak * (1 - 0.5 * blink * (0.5 + 0.5 * math.sin(t * 10))), 0.85)
        if fantasma > 0:   # a cópia que foi contada duas vezes
            pessoa(c, x + 18, y - 10, meio_col, ak * fantasma * 0.45, 0.85)


def b_festa(c, t, C, B):
    head(c, t, B["start"], "UM CASAMENTO", "QUANTOS CONVITES?", BLUE)
    card(c, *CARD_R)
    if t < C["05"] - 0.2:
        for k, (cue, s, n, col) in enumerate((("04.a", "lista da NOIVA", "30", CA), ("04.b", "lista do NOIVO", "25", CB))):
            a, dy = rise(t, C[cue])
            x = 300 + k * 560
            card(c, x, 220 + dy, 480, 340, a)
            text(c, s, x + 240, 290 + dy, 34, "black", col, a)
            multidao(c, x + 240, 400 + dy, 6, col, a, C[cue], t, cols=6)
            text(c, n + " amigos", x + 240, 520 + dy, 44, "black", INK, a)
        ac = ep(t, C["04.c"], 0.5)
        multidao(c, 1500, 360, 5, MEIO, ac, C["04.c"], t, cols=5)
        text(c, "5 amigos dos DOIS", 1500, 450, 34, "black", MEIO, ac)
        regra(c, "quantos convites imprimir?", W / 2, 720, ep(t, C["04.d"], 0.5), 40, AMBER)
        return
    v = V_FESTA()
    if t < C["06"] - 0.2:
        tag(c, "conjunto = grupo com algo em comum", 520, 280, BLUE, ep(t, C["05.t"], 0.4), 26)
        ae = ep(t, C["05.a"], 0.4)
        tag(c, "elemento = cada pessoa da lista", 520, 380, BLUE, ae, 26)
        tag(c, "DIAGRAMA DE VENN", 520, 520, PURPLE, ep(t, C["05.b"], 0.4), 30)
        festa_venn(c, t, v, ep(t, C["05.b"], 0.5), C["05.b"])
        if ae > 0:
            c.drawCircle(v.pos["a"][0] - 60, v.cy - 30, 30, paint(BLUE, ae * (0.5 + 0.5 * math.sin(t * 5)), stroke=4))
        return
    festa_venn(c, t, v, 1, C["06"] - 5)
    am = ep(t, C["06.b"], 0.5)
    v.pinta(c, "m", MEIO, am * (0.6 + 0.4 * math.sin(t * 4)))
    tag(c, "a sobreposição = quem está nos DOIS", 520, 400, MEIO, ep(t, C["06.c"], 0.4), 26)
    text(c, "os 5 amigos do casal", 520, 480, 30, "black", INK2, ep(t, C["06.c"] + 0.6, 0.4))


# ======================================================================
# b) as operações
# ======================================================================

OPS = [("07", "m|a|b", "UNIÃO", "A ∪ B", "noiva OU noivo OU os dois", ("a", "m", "b")),
       ("08", "m", "INTERSEÇÃO", "A ∩ B", "nos dois AO MESMO TEMPO", ("m",)),
       ("09", "a", "DIFERENÇA", "A − B", "SÓ da noiva", ("a",)),
       ("10", "nA", "COMPLEMENTAR", "A^c", "tudo FORA da noiva", ("b", "f"))]


def b_operacoes(c, t, C, B):
    head(c, t, B["start"], "AS 4 OPERAÇÕES", "EM LINGUAGEM DE FESTA", BLUE)
    card(c, *CARD_R)
    k = 0
    for i, op in enumerate(OPS):
        if t >= C[op[0]] - 0.2:
            k = i
    sid, _, nome, sym, desc, regs = OPS[k]
    v = Venn2(1150, 500, 200, 240, rect_pad=60)
    a_reg = ep(t, C[f"{sid}.a"] if sid != "10" else C["10.b"], 0.5)
    for r_ in regs:
        v.pinta(c, r_, MEIO if r_ == "m" else CA if r_ == "a" else CB if r_ == "b" else FORA, a_reg, 0.35)
    v.base(c, 1, "noiva", "noivo", universo=(sid == "10"), ua=ep(t, C["10.a"], 0.5) if sid == "10" else 1)
    a1, dy = rise(t, C[sid + ".t"])
    text(c, nome, 480, 320 + dy, 52, "black", BLUE, a1)
    fmid(c, sym, 480, 440 + dy, 90, "black", PURPLE, ep(t, C[sid + ".b"] if sid in ("07", "08") else C[sid + ".a"], 0.5))
    text(c, desc, 480, 580 + dy, 32, "black", INK, a_reg)
    if sid == "07":
        text(c, "o símbolo parece um U", 480, 650, 26, "black", INK2, ep(t, C["07.c"], 0.4))
    if sid == "08":
        text(c, "o U de cabeça para baixo", 480, 650, 26, "black", INK2, ep(t, C["08.b"], 0.4))
    if sid == "10":
        text(c, "retângulo = todo mundo que está sendo contado", 1150, 830, 24, "black", INK2, ep(t, C["10.a"], 0.4))
    # resumo das 4 no rodapé
    for i, op in enumerate(OPS):
        ai = ep(t, C[op[0]], 0.4)
        fmid(c, op[3], 260 + i * 120, 790, 34, "black", PURPLE if i == k else LIGHT, ai)


# ======================================================================
# c) por que se subtrai a interseção
# ======================================================================

def b_contagem(c, t, C, B):
    head(c, t, B["start"], "QUANTOS CONVITES?", "QUEM FOI CONTADO DUAS VEZES", PURPLE)
    card(c, *CARD_R)
    v = Venn2(1180, 540, 190, 230)
    if t < C["12"] - 0.2:
        festa_venn(c, t, v, 1, C["11"] - 5)
        tag(c, "n(A) = número de elementos de A", 520, 300, BLUE, ep(t, C["11.a"], 0.4), 26)
        fmid(c, "n(noiva) = 30", 520, 430, 50, "black", CA, ep(t, C["11.b"], 0.4))
        fmid(c, "n(noivo) = 25", 520, 520, 50, "black", CB, ep(t, C["11.b"] + 0.6, 0.4))
        return
    if t < C["13"] - 0.2:
        blink = ep(t, C["12.a"], 0.4) * (1 - prog(t, C["12.c"], 0.4))
        fant = ep(t, C["12.b"], 0.4) * (1 - ep(t, C["12.c"] + 0.3, 0.6))
        festa_venn(c, t, v, 1, C["12"] - 5, blink=blink, fantasma=fant)
        fmid(c, "30 + 25 = 55", 520, 320, 60, "black", INK, ep(t, C["12.t"], 0.4))
        tag(c, "o meio entrou 2×", 520, 430, AMBER, ep(t, C["12.b"], 0.4), 28)
        text(c, "uma na lista da noiva, outra na do noivo", 520, 500, 24, "black", INK2, ep(t, C["12.b"], 0.4))
        fmid(c, "− 5", 520, 590, 60, "black", RED, ep(t, C["12.c"], 0.4))
        fbox = ep(t, C["12.d"], 0.5)
        if fbox > 0:
            result_box(c, "50 convites", 520, 700, 44, fbox)
        return
    festa_venn(c, t, v, 1, C["13"] - 5)
    regra(c, "n(A ∪ B) = n(A) + n(B) − n(A ∩ B)", W / 2, 230, ep(t, C["13.a"], 0.5), 40, PURPLE, w=1200)
    ab = ep(t, C["13.b"], 0.5)
    if ab > 0:
        card(c, 220, 380, 600, 400, ab)
        for x, col in ((400, CA), (640, CB)):
            c.drawCircle(x, 560, 100, paint(col, ab * 0.12)); c.drawCircle(x, 560, 100, paint(col, ab, stroke=5))
        text(c, "ninguém em comum", 520, 710, 28, "black", INK, ab)
        tag(c, "DISJUNTOS: soma direto", 520, 420, BLUE, ep(t, C["13.c"], 0.4), 24)


# ======================================================================
# d) os "nenhum"
# ======================================================================

def b_nenhum(c, t, C, B):
    head(c, t, B["start"], "QUEM NÃO ESTÁ EM NENHUM", "FORA DOS CÍRCULOS", BLUE)
    card(c, *CARD_R)
    v = Venn2(1150, 500, 190, 230, rect_pad=80)
    v.pinta(c, "U", MEIO, ep(t, C["14.b"], 0.5), 0.18)
    v.pinta(c, "f", FORA, ep(t, C["14.c"], 0.5), 0.35)
    v.base(c, 1, "noiva", "noivo", universo=True, ua=ep(t, C["14.a"], 0.5))
    text(c, "cidade: 80 pessoas", 480, 330, 40, "black", INK, ep(t, C["14.a"], 0.5))
    text(c, "convidados: 50", 480, 420, 40, "black", MEIO, ep(t, C["14.b"], 0.5))
    fmid(c, "80 − 50 = 30", 480, 530, 56, "black", INK, ep(t, C["14.c"], 0.5))
    v.num(c, "f", "30", ep(t, C["14.c"] + 0.4, 0.5), FORA)
    v.num(c, "m", "50", ep(t, C["14.b"], 0.5) * 0, MEIO)
    tag(c, "os NENHUM: fora dos círculos, dentro do retângulo", W / 2, 806, AMBER, ep(t, C["14.d"], 0.5), 26)


# ======================================================================
# e-f) três conjuntos
# ======================================================================

def b_tres(c, t, C, B):
    head(c, t, B["start"], "E COM TRÊS GRUPOS?", "DE DENTRO PARA FORA", PURPLE)
    card(c, *CARD_R)
    v = Venn3(1200, 470, 170)
    a0 = ep(t, C["15.t"], 0.5)
    if t < C["16"] - 0.2:
        v.pinta(c, "m", MEIO, ep(t, C["15.b"], 0.4), 0.5)
        for k in ("fv", "fn", "vn"):
            v.pinta(c, k, AMBER, ep(t, C["15.c"], 0.4), 0.35)
        for k in ("f", "v", "n"):
            v.pinta(c, k, BLUE, ep(t, C["15.d"], 0.4), 0.18)
        v.base(c, a0, ("A", "B", "C"))
        text(c, "7 pedaços", 500, 300, 48, "black", INK, ep(t, C["15.a"], 0.4))
        tag(c, "MIOLO: nos três", 500, 420, MEIO, ep(t, C["15.b"], 0.4), 28)
        tag(c, "em exatamente dois", 500, 520, AMBER, ep(t, C["15.c"], 0.4), 28)
        tag(c, "em um só", 500, 620, BLUE, ep(t, C["15.d"], 0.4), 28)
        return
    if t < C["17"] - 0.2:
        v.base(c, 1, ("A", "B", "C"))
        pulse = 0.5 + 0.5 * math.sin(t * 6)
        v.pinta(c, "m", MEIO, ep(t, C["16.b"], 0.4) * pulse, 0.7)
        for k, (cx, cy) in enumerate(v.cs):
            ak = ep(t, C["16.c"] + 0.4 * k, 0.4)
            c.drawCircle(cx, cy, v.r, paint(RED, ak * 0.10))
        regra(c, "preencha DE DENTRO PARA FORA", 520, 300, ep(t, C["16.t"], 0.5), 32, PURPLE, w=640)
        text(c, "o miolo está escondido", 520, 450, 32, "black", MEIO, ep(t, C["16.b"], 0.4))
        text(c, "em TODOS os dados", 520, 500, 32, "black", MEIO, ep(t, C["16.b"], 0.4))
        tag(c, "pelas pontas: conta o miolo 2, 3 vezes", 520, 640, RED, ep(t, C["16.c"], 0.4), 24)
        return
    if t < C["18"] - 0.2:
        passos = [("17.a", "1. o miolo", ("m",), MEIO), ("17.b", "2. os pares − miolo", ("fv", "fn", "vn"), AMBER),
                  ("17.c", "3. os sozinhos − o que já foi posto", ("f", "v", "n"), BLUE), ("17.d", "4. some os 7 e compare", (), GREEN)]
        for k, (cue, s, regs, col) in enumerate(passos):
            a, dy = rise(t, C[cue])
            fmid(c, s, 230, 300 + k * 110 + dy, 34, "black", col, a, align="left")
            for r_ in regs:
                v.pinta(c, r_, col, a, 0.35)
        v.base(c, 1, ("A", "B", "C"))
        return
    v.base(c, 1, ("A", "B", "C"))
    tag(c, "fórmula: só para CONFERIR", 520, 280, GREEN, ep(t, C["18.t"], 0.4), 28)
    for k, (cue, s, col) in enumerate((("18.a", "+ os três grupos", INK), ("18.b", "− os pares", RED), ("18.c", "+ o trio", GREEN))):
        a, dy = rise(t, C[cue])
        fmid(c, s, 520, 420 + k * 100 + dy, 48, "black", col, a)


# ======================================================================
# g) "apenas"
# ======================================================================

def b_apenas(c, t, C, B):
    head(c, t, B["start"], "A PALAVRA QUE DERRUBA", "\"APENAS\"", AMBER)
    card(c, *CARD_R)
    v = Venn2(1180, 500, 210, 250)
    aa = ep(t, C["19.a"], 0.5) * (1 - prog(t, C["19.b"], 0.4))
    v.pinta(c, "A", CA, aa, 0.30)
    ab = ep(t, C["19.b"], 0.5)
    v.pinta(c, "a", AMBER, ab, 0.40)
    v.base(c, 1, "noiva", "noivo")
    v.num(c, "m", "5", 1, MEIO, 44)
    fmid(c, "amigos da noiva = 30", 230, 330, 40, "black", CA, ep(t, C["19.a"], 0.4), align="left")
    text(c, "o círculo INTEIRO", 230, 390, 28, "black", INK2, ep(t, C["19.a"], 0.4), align="left")
    apenas_txt(c, "amigos apenas da noiva", 230, 500, 40, INK, ab, sub=ease_io(prog(t, C["19.b"] + 0.2, 0.6)))
    fmid(c, "30 − 5 = 25", 230, 590, 50, "black", AMBER, ep(t, C["19.b"] + 1.2, 0.4), align="left")
    v.num(c, "a", "25", ep(t, C["19.b"] + 1.2, 0.4), AMBER)
    tag(c, "leu \"apenas\"? SUBLINHE", 500, 750, AMBER, ep(t, C["19.c"], 0.4), 28)


# ======================================================================
# recapitulação
# ======================================================================

FRASES = ["Quem está nos dois foi contado 2×: desconte uma",
          "Preencha de dentro para fora",
          "\"apenas A\" = só o pedaço de A que não toca em ninguém"]


def b_recap(c, t, C, B):
    sid = "20" if B["start"] < C["40"] - 1 else "40"
    head(c, t, B["start"], "AS 3 FRASES", "PARA GUARDAR", GREEN)
    card(c, *CARD_R)
    for k, (cue, col) in enumerate((("a", MEIO), ("b", PURPLE), ("c", AMBER))):
        a, d = rise(t, C[f"{sid}.{cue}"])
        y = 330 + k * 160 + d
        badge_num(c, k + 1, 230, y - 16, a, 32, bg=col)
        apenas_txt(c, FRASES[k], 290, y, 44, INK, a)


# ======================================================================
# erros
# ======================================================================

def b_erro1(c, t, C, B):
    head(c, t, B["start"], "ERRO 1", "ESQUECER DE SUBTRAIR O MEIO", RED)
    erro_tiles(c, t, [(C["21.a"], "O ERRO", ["!n(A) + n(B)"], RED),
                      (C["21.b"], "POR QUE PARECE CERTO", ["juntar", "é somar"], AMBER),
                      (C["21.c"], "A CORREÇÃO", ["o meio entrou 2×", "!− n(A ∩ B)"], GREEN)])


def b_erro2(c, t, C, B):
    head(c, t, B["start"], "ERRO 2", "DE FORA PARA DENTRO", RED)
    erro_tiles(c, t, [(C["22.a"], "O ERRO", ["começar pelos", "!grupos inteiros"], RED),
                      (C["22.b"], "POR QUE PARECE CERTO", ["o enunciado dá", "esses números primeiro"], AMBER),
                      (C["22.c"], "A CORREÇÃO", ["o miolo está", "dentro de todos", "!comece pelo miolo"], GREEN)])


def b_erro3(c, t, C, B):
    head(c, t, B["start"], "ERRO 3", "IGNORAR O \"APENAS\"", RED)
    erro_tiles(c, t, [(C["23.a"], "O ERRO", ["\"apenas A\" =", "!círculo inteiro"], RED),
                      (C["23.b"], "POR QUE PARECE CERTO", ["o número está", "pronto no enunciado"], AMBER),
                      (C["23.c"], "A CORREÇÃO", ["apenas = SEM", "!as interseções"], GREEN)])


def b_erro4(c, t, C, B):
    head(c, t, B["start"], "ERRO 4", "ESQUECER OS \"NENHUM\"", RED)
    erro_tiles(c, t, [(C["24.a"], "O ERRO", ["ignorar quem", "!não está em nada"], RED),
                      (C["24.b"], "POR QUE PARECE CERTO", ["eles não aparecem", "nos círculos"], AMBER),
                      (C["24.c"], "A CORREÇÃO", ["eles estão no TOTAL:", "!fora dos círculos"], GREEN)])


# ======================================================================
# questões
# ======================================================================

def alternativas(c, t, C, x, y, dy, alts, aok, size=36):
    """alts = [(letra, texto, cue_entrada, cue_risco_ou_None, porquê)]"""
    for k, (L, s, cue_in, cue_x, why) in enumerate(alts):
        a, d = rise(t, C[cue_in])
        yy = y + k * dy + d
        ok = cue_x is None
        if ok and aok > 0:
            rrect(c, x - 20, yy - 40, 640, dy - 8, 14, GREEN, 0.15 * aok)
        badge_num(c, L, x + 20, yy - 10, a, 22, bg=GREEN if ok and aok > 0.5 else INK)
        ax = ep(t, C[cue_x], 0.4) if cue_x else 0
        text(c, s, x + 60, yy + 2, size, "black", INK, a * (1 - 0.5 * ax), align="left")
        if ax > 0:
            strike(c, x + 56, yy - 10, x + 66 + text_w(s, "black", size), yy - 10, ax, RED, ax)
            apenas_txt(c, why, x + 200, yy - 2, 22, RED, ax)


def enunciado(c, t, linhas, x=180, y=290, size=28, dy=42):
    for k, (tc, s, col) in enumerate(linhas):
        apenas_txt(c, s, x, y + k * dy, size, col, ep(t, tc, 0.4))


Q1_ALTS = [("A", "70", "26.a", "30.a", "esqueceu os 90 de fora"), ("B", "90", "26.b", "30.b", "copiou o \"nenhum\""),
           ("C", "160", "26.c", None, ""), ("D", "180", "26.d", "30.d", "quem NÃO assina A"),
           ("E", "230", "26.e", "30.e", "320 − 90: sem desenho")]


def b_q1(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 1 · ESTILO ENEM", "DOIS SERVIÇOS DE STREAMING", BLUE)
    card(c, 140, 170, 760, 660)
    pill(c, "QUESTÃO", 170, 210, BLUE, size=22, bounds=(0, 1920))
    enunciado(c, t, [(C["25.e1"], "500 assinantes entrevistados", INK), (C["25.e2"], "320 assinam A · 250 assinam B", INK),
                     (C["25.e3"], "90 não assinam nenhum", INK), (C["25.e4"], "Quantos têm os dois?", BLUE)], y=275)
    alternativas(c, t, C, 190, 490, 66, Q1_ALTS, ep(t, C["28.r"], 0.5), 34)
    pause_badge(c, 1110, 700, ep(t, C["26.p"], 0.5) * (1 - prog(t, C["27.t"] - 0.3, 0.4)))
    # desenho
    ad = ep(t, C["27.t"], 0.5)
    card(c, 940, 170, 840, 660, ad)
    if ad <= 0:
        return
    v = Venn2(1360, 560, 140, 160, rect_pad=50)
    if t < C["28"] - 0.2:
        fmid(c, "320 + 250 = 570", 1360, 260, 48, "black", INK, ep(t, C["27.a"], 0.4))
        fmid(c, "570 > 500 !", 1360, 330, 44, "black", AMBER, ep(t, C["27.b"], 0.4))
        v.pinta(c, "m", MEIO, ep(t, C["27.d"], 0.4) * (0.6 + 0.4 * math.sin(t * 5)), 0.5)
        v.base(c, ad, "A", "B")
        tag(c, "o excesso = a interseção", 1360, 760, MEIO, ep(t, C["27.d"], 0.4), 26)
        return
    v.pinta(c, "f", FORA, ep(t, C["28.a"], 0.4), 0.35)
    v.pinta(c, "U", BLUE, ep(t, C["28.b"], 0.4) * (1 - ep(t, C["28.c"], 0.3)), 0.12)
    v.pinta(c, "m", MEIO, ep(t, C["28.c"], 0.4), 0.35)
    v.pinta(c, "a", CA, ep(t, C["29.a"], 0.4), 0.25)
    v.pinta(c, "b", CB, ep(t, C["29.b"], 0.4), 0.25)
    v.base(c, 1, "A", "B", universo=True)
    v.num(c, "f", "90", ep(t, C["28.a"], 0.4), FORA, 44)
    fmid(c, "500 − 90 = 410 nos círculos", 1360, 250, 34, "black", INK, ep(t, C["28.b"], 0.4))
    fmid(c, "570 − 410 = 160", 1360, 300, 40, "black", MEIO, ep(t, C["28.c"], 0.4))
    v.num(c, "m", "160", ep(t, C["28.c"] + 0.5, 0.4), MEIO, 44)
    v.num(c, "a", "160", ep(t, C["29.a"], 0.4), CA, 44)
    v.num(c, "b", "90", ep(t, C["29.b"], 0.4), CB, 44)
    fmid(c, "160 + 160 + 90 + 90 = 500 ✓", 1360, 790, 34, "black", GREEN, ep(t, C["29.c"], 0.4))


Q9_ALTS = [("A", "40", "31.a", "33.a", "é o meio"), ("B", "50", "31.b", "33.b", "é apenas Q"),
           ("C", "80", "31.c", None, ""), ("D", "120", "31.d", "33.d", "P inteiro: ignorou o apenas"),
           ("E", "170", "31.e", "33.e", "a união inteira")]


def b_q9(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 2 · ESTILO ENEM", "A ARMADILHA DO \"APENAS\"", AMBER)
    card(c, 140, 170, 760, 660)
    pill(c, "QUESTÃO", 170, 210, BLUE, size=22, bounds=(0, 1920))
    enunciado(c, t, [(C["31.e1"], "200 consumidores", INK), (C["31.e1"] + 1.5, "120 compram P · 90 compram Q", INK),
                     (C["31.e1"] + 3.0, "40 compram os dois", INK), (C["31.e2"], "Quantos compram apenas P?", BLUE)], y=275)
    alternativas(c, t, C, 190, 490, 66, Q9_ALTS, ep(t, C["32.r"], 0.5), 34)
    pause_badge(c, 1110, 700, ep(t, C["31.p"], 0.5) * (1 - prog(t, C["32.t"] - 0.3, 0.4)))
    ad = ep(t, C["32.t"], 0.5)
    card(c, 940, 170, 840, 660, ad)
    if ad <= 0:
        return
    v = Venn2(1360, 560, 140, 160, rect_pad=50)
    v.pinta(c, "m", MEIO, ep(t, C["32.a"], 0.4), 0.35)
    v.pinta(c, "a", AMBER, ep(t, C["32.b"], 0.4), 0.40)
    v.pinta(c, "b", CB, ep(t, C["32.c"], 0.4), 0.25)
    v.pinta(c, "f", FORA, ep(t, C["32.c"] + 0.8, 0.4), 0.35)
    v.base(c, ad, "P", "Q", universo=True)
    apenas_txt(c, "apenas P", 1360, 250, 44, INK, ep(t, C["32.t"], 0.4), align="center", sub=ease_io(prog(t, C["32.t"] + 0.5, 0.5)))
    v.num(c, "m", "40", ep(t, C["32.a"], 0.4), MEIO, 44)
    fmid(c, "120 − 40 = 80", 1360, 310, 38, "black", AMBER, ep(t, C["32.b"], 0.4))
    v.num(c, "a", "80", ep(t, C["32.b"] + 0.5, 0.4), AMBER, 48)
    v.num(c, "b", "50", ep(t, C["32.c"], 0.4), CB, 44)
    v.num(c, "f", "30", ep(t, C["32.c"] + 0.8, 0.4), FORA, 44)
    fmid(c, "80 + 40 + 50 + 30 = 200 ✓", 1360, 790, 34, "black", GREEN, ep(t, C["32.c"] + 1.6, 0.4))


Q2_ALTS = [("A", "0", "35.a", "39.a", "somou tudo: 150 > 100"), ("B", "5", "35.b", None, ""),
           ("C", "10", "35.c", "39.c", "é o miolo"), ("D", "15", "35.d", "39.d", "esqueceu de somar o trio"),
           ("E", "20", "35.e", "39.e", "é só futebol")]


def b_q2(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 3 · ESTILO ENEM", "TRÊS ESPORTES", BLUE)
    card(c, 140, 170, 760, 660)
    pill(c, "QUESTÃO", 170, 210, BLUE, size=22, bounds=(0, 1920))
    enunciado(c, t, [(C["34.e1"], "100 alunos", INK), (C["34.e1"] + 1.2, "Futebol 60 · Vôlei 50 · Natação 40", INK),
                     (C["34.e2"], "F e V 30 · F e N 20 · V e N 15", INK), (C["34.e3"], "os três: 10", INK),
                     (C["34.e4"], "Quantos não praticam nenhum?", BLUE)], y=270, size=27, dy=40)
    alternativas(c, t, C, 190, 510, 64, Q2_ALTS, ep(t, C["38.r"], 0.5), 34)
    pause_badge(c, 1110, 700, ep(t, C["35.p"], 0.5) * (1 - prog(t, C["36.t"] - 0.3, 0.4)))
    ad = ep(t, C["36.t"], 0.5)
    card(c, 940, 170, 840, 660, ad)
    if ad <= 0:
        return
    v = Venn3(1360, 505, 138)
    passos = [("m", "36.m", "10", MEIO), ("fv", "36.p1", "20", AMBER), ("fn", "36.p2", "10", AMBER), ("vn", "36.p3", "5", AMBER),
              ("f", "37.s1", "20", CA), ("v", "37.s2", "15", CB), ("n", "37.s3", "15", CC)]
    for k, cue, s, col in passos:
        v.pinta(c, k, col, ep(t, C[cue], 0.4), 0.30)
    v.pinta(c, "fora", FORA, ep(t, C["38.b"], 0.4), 0.35)
    v.base(c, ad, ("F", "V", "N"), universo=True)
    prox = ["36.p1", "36.p2", "36.p3", "37", "37.s2", "37.s3", "38"]
    for (k, cue, s, col), nx in zip(passos, prox):
        tc = C[cue] + 0.75 * (C[nx] - C[cue])      # o número aparece quando o resultado é dito
        v.num(c, k, s, ep(t, tc, 0.4), INK, 40)
    v.num(c, "fora", "5", ep(t, C["38.b"], 0.4), FORA, 44)
    fmid(c, "10+20+10+5+20+15+15 = 95", 1360, 222, 30, "black", INK, ep(t, C["38.a"], 0.4))
    fmid(c, "100 − 95 = 5", 1360, 803, 34, "black", GREEN, ep(t, C["38.b"], 0.4) * (1 - prog(t, C["38.c"], 0.3)))
    fmid(c, "fórmula: 150 − 65 + 10 = 95 ✓", 1360, 803, 30, "black", PURPLE, ep(t, C["38.c"], 0.4))


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    head(c, t, B["start"], "ÚLTIMO EPISÓDIO DO ASSUNTO", "REVISÃO GERAL", PURPLE)
    card(c, *CARD_R)
    itens = [("41.a", "sinais", "−(−3)"), ("41.b", "conjuntos numéricos", "√2"), ("41.c", "intervalos", "]2, 5]"), ("41.d", "Venn", "A ∩ B")]
    for k, (cue, s, sym) in enumerate(itens):
        a, dy = rise(t, C[cue])
        x = 230 + k * 380
        card(c, x, 240 + dy, 320, 320, a)
        fmid(c, sym, x + 160, 360 + dy, 60, "black", PURPLE, a)
        text(c, s, x + 160, 490 + dy, 30, "black", INK, a)
    pill(c, "pegadinhas + questões novas", W / 2, 720, AMBER, size=32, a=ep(t, C["41.e"], 0.5), anchor="center")


def b_cta(c, t, C, B):
    cta(c, t, C["42.like"], C["42.sub"], C["42.bell"], C["42.com"], C["42.bye"], "Você já tinha caído na pegadinha do \"apenas\"?")


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, festa=b_festa, operacoes=b_operacoes,
              contagem=b_contagem, nenhum=b_nenhum, tres=b_tres, apenas=b_apenas, recap=b_recap, erro1=b_erro1,
              erro2=b_erro2, erro3=b_erro3, erro4=b_erro4, q1=b_q1, q9=b_q9, q2=b_q2, ponte=b_ponte, cta=b_cta)
