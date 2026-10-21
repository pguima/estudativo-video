"""Visual — Operações e Conjuntos Numéricos, Episódio 3: Intervalos reais — a bolinha cheia e a bolinha vazia (iniciantes, tema claro)
Cores com função: azul = definição · roxo = regra · âmbar = armadilha · verde = entra/dica · vermelho = não entra/erro.
Peças próprias deste episódio:
- colchete(): o colchete desenhado como um BRAÇO que gira — virado para o número abraça (verde), para fora empurra (vermelho).
- RetaI: a reta numérica com o trecho do intervalo pintado e as bolinhas que ENCHEM (entra) ou ESVAZIAM (não entra).
- Todo intervalo aparece nas três formas ao mesmo tempo: frase em português · colchetes (+ inequação) · reta.
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
ARQUIVO_FINAL = "enem_matematica_conjuntos_ep3_intervalos.mp4"
CARD_R = (140, 150, 1640, 690)
SYM = "C:/Windows/Fonts/seguisym.ttf"
FAIXA = "#3B6CF6"     # cor do trecho pintado


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
# texto matemático com fonte reserva
# ======================================================================

@lru_cache(None)
def _symfont(size):
    f = skia.Font(skia.Typeface.MakeFromFile(SYM), size)
    f.setEmbolden(True); f.setSubpixel(True); f.setEdging(skia.Font.Edging.kAntiAlias)
    return f


@lru_cache(None)
def _has(ch, peso):
    return font(peso, 40).textToGlyphs(ch)[0] != 0


def _pieces(s, peso, size):
    cur, cur_sym = "", None
    for ch in s:
        sym = not _has(ch, peso)
        if cur and sym != cur_sym:
            yield cur, (_symfont(size) if cur_sym else font(peso, size))
            cur = ""
        cur += ch; cur_sym = sym
    if cur:
        yield cur, (_symfont(size) if cur_sym else font(peso, size))


def ftext_w(s, peso, size):
    return sum(f.measureText(p) for p, f in _pieces(s, peso, size))


def ftext(c, s, x, y, size, peso="black", color=None, a=1.0, align="center"):
    if a <= 0:
        return 0
    color = INK if color is None else color
    w = ftext_w(s, peso, size)
    xx = x - w / 2 if align == "center" else x - w if align == "right" else x
    for p, f in _pieces(s, peso, size):
        c.drawString(p, xx, y, f, paint(color, a))
        xx += f.measureText(p)
    return w


def fmid(c, s, x, cy, size, peso="black", color=None, a=1.0, align="center"):
    return ftext(c, s, x, cy + size * 0.36, size, peso, color, a, align)


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
            ftext(c, ln.lstrip("!"), x + cw / 2, y + 250 + j * 60, 46 if big else 32, "black",
                  (RED if k == 0 else GREEN if k == 2 else INK) if big else INK, a)


# ======================================================================
# colchete-braço e notação
# ======================================================================

def colchete(c, x, cy, h, d, a, col=None, w=None):
    """d = direção das pontas (+1 = para a direita, −1 = para a esquerda; passa por 0 ao girar)"""
    if a <= 0:
        return
    col = INK if col is None else col
    w = w or max(5, h * 0.09)
    p = paint(col, a, stroke=w, cap_round=True)
    p.setStrokeJoin(skia.Paint.kRound_Join)
    k = h * 0.30 * d
    path = skia.Path()
    path.moveTo(x + k, cy - h / 2); path.lineTo(x, cy - h / 2); path.lineTo(x, cy + h / 2); path.lineTo(x + k, cy + h / 2)
    c.drawPath(path, p)


def notacao(c, cx, cy, size, A, B, hugL, hugR, a, rotulos=0.0):
    """intervalo com colchetes animados. hugL/hugR ∈ [0,1]: 1 = abraça (entra), 0 = empurra (não entra)"""
    if a <= 0:
        return
    s = f"{A}, {B}"
    w = ftext_w(s, "black", size)
    gap = size * 0.32
    xl, xr = cx - w / 2 - gap, cx + w / 2 + gap
    h = size * 1.15
    dL = lerp(-1, 1, ease_io(clamp(hugL)))
    dR = lerp(1, -1, ease_io(clamp(hugR)))
    cl = mix(RED, GREEN, clamp(hugL))
    cr = mix(RED, GREEN, clamp(hugR))
    colchete(c, xl, cy, h, dL, a, cl)
    colchete(c, xr, cy, h, dR, a, cr)
    fmid(c, s, cx, cy, size, "black", INK, a)
    if rotulos > 0:
        for x, hug in ((xl, hugL), (xr, hugR)):
            lab = "abraça: entra" if hug > 0.5 else "empurra: fora"
            text(c, lab, x, cy + h / 2 + 40, 22, "black", GREEN if hug > 0.5 else RED, a * rotulos)


# ======================================================================
# reta com intervalo
# ======================================================================

class RetaI:
    def __init__(self, x0, x1, y, lo, hi, ticks):
        self.x0, self.x1, self.y, self.lo, self.hi, self.ticks = x0, x1, y, lo, hi, ticks

    def X(self, v):
        if v == "+inf":
            return self.x1 + 30
        if v == "-inf":
            return self.x0 - 30
        return lerp(self.x0, self.x1, (v - self.lo) / (self.hi - self.lo))

    def base(self, c, a):
        if a <= 0:
            return
        y = self.y
        arrow(c, self.x0 - 50, y, self.x1 + 60, y, LIGHT, a, 5, 16)
        for v, lab in self.ticks:
            x = self.X(v)
            line(c, x, y - 12, x, y + 12, INK2, a, 3)
            text(c, lab, x, y + 54, 30, "black", INK, a)

    def faixa(self, c, va, vb, a, prog_=1.0, col=FAIXA):
        if a <= 0 or prog_ <= 0:
            return
        xa, xb = self.X(va), self.X(vb)
        xe = lerp(xa, xb, prog_)
        rrect(c, min(xa, xe), self.y - 8, abs(xe - xa), 16, 8, col, a * 0.85)
        if vb in ("+inf", "-inf") and prog_ > 0.95:
            arrow(c, xb - 30 * (1 if vb == "+inf" else -1), self.y, xb + 25 * (1 if vb == "+inf" else -1), self.y, col, a, 8, 26)
        if va in ("+inf", "-inf") and prog_ > 0.05:
            arrow(c, xa + 30 * (1 if va == "+inf" else -1), self.y, xa - 25 * (1 if va == "+inf" else -1), self.y, col, a, 8, 26)

    def bola(self, c, v, cheia, a, col=FAIXA, r=17):
        """cheia ∈ [0,1]: 0 = vazia, 1 = cheia"""
        if a <= 0:
            return
        x = self.X(v)
        c.drawCircle(x, self.y, r, paint("#FFFFFF", a))
        c.drawCircle(x, self.y, r, paint(col, a, stroke=5))
        if cheia > 0:
            c.drawCircle(x, self.y, r * clamp(cheia), paint(col, a))


def frase(c, s, cx, cy, a, size=40):
    if a <= 0:
        return
    w = ftext_w(s, "black", size) + 80
    rrect(c, cx - w / 2, cy - 38, w, 76, 22, BLUE, a * 0.10)
    fmid(c, '"' + s + '"', cx, cy, size, "black", BLUE, a)


def tres_formas(c, t, a, fr, A, B, hugL, hugR, reta, va, vb, a_frase=1.0, a_nota=1.0, a_reta=1.0, prog_=1.0,
                ineq=None, a_ineq=0.0, rot=0.0, nota_x=None, y_fr=245, y_nota=395, bolas=True):
    """as três formas do mesmo intervalo, empilhadas: português · colchetes (+ inequação) · reta"""
    frase(c, fr, W / 2, y_fr, a * a_frase)
    nx = nota_x if nota_x is not None else (W / 2 - 300 if ineq else W / 2)
    notacao(c, nx, y_nota, 84, A, B, hugL, hugR, a * a_nota, rot)
    if ineq:
        fmid(c, ineq, W / 2 + 360, y_nota, 70, "black", PURPLE, a * a_ineq)
    reta.base(c, a * a_reta)
    reta.faixa(c, va, vb, a * a_reta, prog_)
    if bolas:
        if va not in ("+inf", "-inf"):
            reta.bola(c, va, hugL, a * a_reta)
        if vb not in ("+inf", "-inf"):
            reta.bola(c, vb, hugR, a * a_reta)


def T07(lo, hi, step=1):
    return [(v, str(v)) for v in range(lo, hi + 1, step)]


# ======================================================================
# gancho, promessa, pré-requisitos
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "INTERVALOS REAIS · EPISÓDIO 3", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["01.a"], 0.5)
    r = RetaI(330, 1590, 470, 0, 6, T07(0, 6))
    r.base(c, a0)
    r.faixa(c, 1, 4, a0, ease_io(prog(t, C["01.a"] + 0.3, 0.8)))
    pisca = 0.5 + 0.5 * math.cos((t - C["01.a"]) * 3.2) if t < C["01.c"] else 0
    r.bola(c, 1, 1, a0)
    r.bola(c, 4, pisca, a0)
    ab = ep(t, C["01.b"], 0.5)
    text(c, "vazia ou cheia?", r.X(4), 380, 34, "black", AMBER, a0)
    pill(c, "muda a alternativa correta", W / 2, 640, RED, size=32, a=ab, anchor="center")
    pill(c, "nunca mais erre isso", W / 2, 760, GREEN, size=32, a=ep(t, C["01.c"], 0.5), anchor="center")


def b_promessa(c, t, C, B):
    head(c, t, B["start"], "AO FINAL DESTA AULA", "TRÊS JEITOS DE ESCREVER", GREEN)
    itens = [("02.b", "em português", None), ("02.c", "com colchetes", None), ("02.d", "na reta", None)]
    for k, (cue, s, _) in enumerate(itens):
        a, dy = rise(t, C[cue])
        if a <= 0:
            continue
        x = 230 + k * 500
        card(c, x, 220 + dy, 460, 460, a)
        badge_num(c, k + 1, x + 230, 300 + dy, a, 34, bg=[BLUE, PURPLE, GREEN][k])
        text(c, s, x + 230, 620 + dy, 38, "black", INK, a)
        if k == 0:
            fmid(c, '"de 2 a 5"', x + 230, 460 + dy, 50, "black", BLUE, a)
        elif k == 1:
            notacao(c, x + 230, 460 + dy, 64, "2", "5", 1, 1, a)
        else:
            r = RetaI(x + 70, x + 390, 460 + dy, 1, 6, [])
            r.base(c, a)
            r.faixa(c, 2, 5, a)
            r.bola(c, 2, 1, a); r.bola(c, 5, 1, a)
    text(c, "o mesmo intervalo, de três jeitos", W / 2, 790, 32, "black", INK2, ep(t, C["02.d"] + 0.8, 0.5))


def b_prereq(c, t, C, B):
    card(c, *CARD_R)
    if t < C["04"] - 0.2:
        head(c, t, B["start"], "LEMBRETE 1", "A RETA REAL NÃO TEM BURACOS", BLUE)
        a0 = ep(t, C["03.a"], 0.5)
        r = RetaI(330, 1590, 420, 0, 4, T07(0, 4))
        r.base(c, a0)
        ab = ep(t, C["03.b"], 0.5)
        x2, x3 = r.X(2), r.X(3)
        rrect(c, x2, 412, x3 - x2, 16, 8, AMBER, ab * 0.5)
        for k, (v, s) in enumerate(((2.5, "2,5"), (math.sqrt(5), "√5 ≈ 2,24"))):
            ak = ep(t, C["03.b"] + 0.7 + 0.7 * k, 0.4)
            c.drawCircle(r.X(v), 420, 10, paint(AMBER, ak))
            fmid(c, s, r.X(v), 340 - 40 * k, 34, "black", AMBER, ak)
        text(c, "entre 2 e 3: INFINITOS números", W / 2, 660, 38, "black", AMBER, ep(t, C["03.b"] + 2.2, 0.5))
        return
    head(c, t, C["04"], "LEMBRETE 2", "OS SINAIS DE MENOR E MAIOR", BLUE)
    sinais = [("04.a", "<", "menor que", "2 < 5"), ("04.b", "≤", "menor ou igual", "5 ≤ 5"),
              ("04.c", ">", "maior que", "5 > 2"), ("04.c", "≥", "maior ou igual", "5 ≥ 5")]
    for k, (cue, sym, s, ex) in enumerate(sinais):
        a, dy = rise(t, C[cue] + (0.9 if k == 3 else 0))
        if a <= 0:
            continue
        x = 260 + k * 400
        card(c, x - 160, 230 + dy, 320, 440, a)
        fmid(c, sym, x, 360 + dy, 120, "black", PURPLE, a)
        text(c, s, x, 500 + dy, 30, "black", INK, a)
        fmid(c, ex, x, 590 + dy, 44, "black", INK2, a)
    text(c, "o tracinho embaixo = \"ou igual\"", W / 2, 760, 32, "black", BLUE, ep(t, C["04.b"] + 1.0, 0.5))


# ======================================================================
# a) fechado · b) aberto · c) semiaberto
# ======================================================================

R27 = lambda: RetaI(330, 1590, 620, 0, 7, T07(0, 7))


def b_fechado(c, t, C, B):
    head(c, t, B["start"], "INTERVALO FECHADO", "AS DUAS PONTAS ENTRAM", BLUE)
    card(c, *CARD_R)
    r = R27()
    hugL = ep(t, C["07.b"], 0.7)
    hugR = ep(t, C["07.c"], 0.7)
    a_nota = ep(t, C["07.t"], 0.5)
    tres_formas(c, t, 1, "de 2 a 5", "2", "5", hugL if t > C["07.t"] else ep(t, C["05.a"], 0.4),
                hugR if t > C["07.t"] else ep(t, C["05.b"], 0.4), r, 2, 5,
                a_frase=ep(t, C["05.t"], 0.5), a_nota=a_nota, a_reta=ep(t, C["05.t"] + 0.4, 0.5),
                prog_=ease_io(prog(t, C["05.c"], 0.8)), ineq="2 ≤ x ≤ 5", a_ineq=ep(t, C["08.b"], 0.5),
                rot=ep(t, C["07.c"], 0.4), nota_x=W / 2 - 300)
    # rótulos de definição (azul)
    if t < C["07"]:
        tag(c, "intervalo = pedaço da reta", 520, 780, BLUE, ep(t, C["06.t"], 0.4), 24)
        tag(c, "extremos = as pontas", 960, 780, BLUE, ep(t, C["06.a"], 0.4), 24)
        tag(c, "fechado = as duas entram", 1400, 780, BLUE, ep(t, C["06.b"], 0.4), 24)
        if C["06.c"] <= t:
            for v in (2, 5):
                c.drawCircle(r.X(v), 620, 34 + 6 * math.sin(t * 6), paint(GREEN, ep(t, C["06.c"], 0.4), stroke=4))
            text(c, "bolinha cheia = entra", W / 2, 530, 30, "black", GREEN, ep(t, C["06.c"], 0.4))
    elif t < C["08"]:
        text(c, "o colchete é um BRAÇO", W / 2 - 300, 290 + 0, 26, "black", PURPLE, ep(t, C["07.a"], 0.4) * 0)
        tag(c, "colchete = braço: virado para o número, ABRAÇA", W / 2, 780, PURPLE, ep(t, C["07.a"], 0.4), 26)
    else:
        tag(c, "x = qualquer número do intervalo", 600, 780, BLUE, ep(t, C["08.a"], 0.4), 24)
        tag(c, "inequação: sinal de menor no lugar do igual", 1300, 780, BLUE, ep(t, C["08.c"], 0.4), 24)
    # a frase cheia "2 entra" / "5 entra" no começo
    if t < C["06"]:
        for v, cue in ((2, "05.a"), (5, "05.b")):
            a = ep(t, C[cue], 0.4)
            text(c, "entra", r.X(v), 560, 26, "black", GREEN, a)


def b_aberto(c, t, C, B):
    head(c, t, B["start"], "INTERVALO ABERTO", "NENHUMA PONTA ENTRA", BLUE)
    card(c, *CARD_R)
    r = R27()
    vaz = ep(t, C["10.a"], 0.7)          # bolinhas esvaziam
    emp = ep(t, C["10.b"], 0.9)          # braços viram para fora
    hug_b = 1 - emp
    bolas_hug = 1 - vaz
    frase(c, "acima de 2 e abaixo de 5", W / 2, 245, ep(t, C["09.t"], 0.5))
    notacao(c, W / 2 - 300, 395, 84, "2", "5", hug_b, hug_b, ep(t, C["10.b"] - 0.3, 0.4), ep(t, C["10.b"] + 0.6, 0.4))
    fmid(c, "2 < x < 5", W / 2 + 360, 395, 70, "black", PURPLE, ep(t, C["10.c"], 0.5))
    a_r = ep(t, C["09.a"], 0.5)
    r.base(c, a_r)
    r.faixa(c, 2, 5, a_r, ease_io(prog(t, C["09.a"] + 0.3, 0.8)))
    r.bola(c, 2, bolas_hug, a_r)
    r.bola(c, 5, bolas_hug, a_r)
    if t < C["10"]:
        for v in (2, 5):
            text(c, f"{v} °C: não aguenta", r.X(v), 560, 24, "black", RED, ep(t, C["09.b"] + (0 if v == 2 else 1.2), 0.4))
    tag(c, "aberto = nenhuma ponta entra · bolinhas VAZIAS", W / 2, 780, BLUE, ep(t, C["10.a"], 0.4) * (1 - prog(t, C["11.t"], 0.3)), 24)
    a11 = ep(t, C["11.a"], 0.5)
    if a11 > 0:
        fmid(c, "=", W / 2 + 120, 395, 70, "black", INK2, a11)
        fmid(c, "(2, 5)", W / 2 + 360, 520, 70, "black", INK, a11)
        text(c, "parênteses: também braços para fora", W / 2, 780, 30, "black", BLUE, ep(t, C["11.b"], 0.4))


def b_semiaberto(c, t, C, B):
    head(c, t, B["start"], "INTERVALO SEMIABERTO", "SÓ UMA PONTA ENTRA", BLUE)
    card(c, *CARD_R)
    r = RetaI(330, 1590, 620, 0, 300, [(0, "0"), (100, "100"), (200, "200"), (300, "300")])
    a_r = ep(t, C["12.a"], 0.5)
    r.base(c, a_r)
    # faixas da conta de luz
    for k, (va, vb) in enumerate(((0, 100), (100, 200), (200, 300))):
        ak = a_r * ep(t, C["12.a"] + 0.3 * k, 0.4)
        x0, x1 = r.X(va), r.X(vb)
        col = [GRAY, FAIXA, GRAY][k]
        if k != 1:
            rrect(c, x0 + 6, 540, x1 - x0 - 12, 30, 10, col, ak * 0.15)
            text_mid(c, f"faixa {k + 1}", (x0 + x1) / 2, 555, 22, "black", INK2, ak)
    ab = ep(t, C["12.b"], 0.4)
    x0, x1 = r.X(100), r.X(200)
    rrect(c, x0 + 6, 540, x1 - x0 - 12, 30, 10, FAIXA, ab * 0.2)
    text_mid(c, "faixa 2", (x0 + x1) / 2, 555, 22, "black", FAIXA, ab)
    r.faixa(c, 100, 200, ab, ease_io(prog(t, C["12.b"], 0.8)))
    r.bola(c, 100, ep(t, C["12.c"], 0.5), ab)
    r.bola(c, 200, 0, ab)
    text(c, "vai para a faixa 3", r.X(200), 700, 24, "black", RED, ep(t, C["12.d"], 0.4) * (1 - prog(t, C["13.t"], 0.3)))
    frase(c, "de 100 até antes de 200", W / 2, 245, ep(t, C["12.b"], 0.5))
    an = ep(t, C["13.t"], 0.5)
    notacao(c, W / 2 - 300, 395, 84, "100", "200", ep(t, C["13.a"], 0.7), 0, an, ep(t, C["13.b"] + 0.5, 0.4))
    fmid(c, "100 ≤ x < 200", W / 2 + 380, 395, 64, "black", PURPLE, ep(t, C["13.b"] + 0.8, 0.5))
    tag(c, "semiaberto = só uma ponta entra", W / 2, 790, BLUE, an, 24)


# ======================================================================
# d) infinito · e) a regra
# ======================================================================

R18 = lambda: RetaI(330, 1500, 620, 0, 40, [(0, "0"), (10, "10"), (18, "18"), (30, "30"), (40, "40")])


def b_infinito(c, t, C, B):
    head(c, t, B["start"], "E SEM PONTA DO OUTRO LADO?", "O INFINITO", BLUE)
    card(c, *CARD_R)
    r = R18()
    a_r = ep(t, C["14.a"], 0.5)
    frase(c, "a partir de 18", W / 2, 245, ep(t, C["14.a"], 0.5))
    if t < C["14.a"] + 3:
        tag(c, "PROIBIDO PARA MENORES DE 18", W / 2, 245, RED, ep(t, C["14.a"], 0.3) * (1 - prog(t, C["14.a"] + 2.6, 0.4)), 30)
    r.base(c, a_r)
    r.faixa(c, 18, "+inf", ep(t, C["14.b"], 0.4), ease_io(prog(t, C["14.b"] + 0.3, 1.6)))
    r.bola(c, 18, ep(t, C["14.b"], 0.5), ep(t, C["14.b"], 0.4))
    text(c, "não tem limite →", r.X(32), 560, 28, "black", FAIXA, ep(t, C["14.c"], 0.5))
    a15 = ep(t, C["15.t"], 0.5)
    if t < C["15.b"]:
        fmid(c, "∞", W / 2, 400, 120, "black", BLUE, a15)
        text(c, "infinito: \"não tem fim\" · um 8 deitado", W / 2, 490, 30, "black", BLUE, ep(t, C["15.a"], 0.4))
    else:
        notacao(c, W / 2 - 300, 395, 84, "18", "+∞", ep(t, C["15.b"], 0.7), 0, ep(t, C["15.b"] - 0.2, 0.4), ep(t, C["15.c"], 0.4))
        fmid(c, "x ≥ 18", W / 2 + 360, 395, 70, "black", PURPLE, ep(t, C["15.d"], 0.5))


def b_infinito_regra(c, t, C, B):
    head(c, t, B["start"], "REGRA SEM EXCEÇÃO", "O INFINITO É SEMPRE ABERTO", PURPLE)
    card(c, *CARD_R)
    a0 = ep(t, C["16.t"], 0.5)
    # o braço do infinito tenta abraçar e volta (16.c)
    tenta = math.sin(math.pi * prog(t, C["16.c"], 1.4)) * 0.75 if t > C["16.c"] else 0
    notacao(c, W / 2, 360, 110, "18", "+∞", 1, tenta, a0)
    xr = W / 2 + ftext_w("18, +∞", "black", 110) / 2 + 36
    c.drawCircle(xr, 360, 90, paint(RED, ep(t, C["16.t"] + 0.6, 0.4) * (0.5 + 0.5 * math.sin(t * 5)), stroke=4))
    tag(c, "∞ NÃO é um número", W / 2 - 330, 560, BLUE, ep(t, C["16.b"], 0.4), 28)
    tag(c, "não dá para abraçar o que nunca acaba", W / 2 + 280, 560, AMBER, ep(t, C["16.c"], 0.4), 28)
    regra(c, "o lado do infinito é SEMPRE ABERTO", W / 2, 740, ep(t, C["16.d"], 0.5), 40, PURPLE)


# ======================================================================
# f) gráficos
# ======================================================================

def b_graficos(c, t, C, B):
    head(c, t, B["start"], "NO ENEM", "BOLINHAS EM GRÁFICOS", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["17.a"], 0.5)
    ox, oy, w, h = 330, 760, 900, 520
    arrow(c, ox, oy, ox + w, oy, INK2, a0, 4, 14)
    arrow(c, ox, oy, ox, oy - h, INK2, a0, 4, 14)
    # função "em degraus": primeiro trecho termina em bolinha cheia; o segundo começa em bolinha vazia
    p1 = ((ox + 60, oy - 140), (ox + 420, oy - 140))
    p2 = ((ox + 420, oy - 360), (ox + 820, oy - 360))
    pr = ease_io(prog(t, C["17.a"] + 0.3, 1.0))
    line(c, *p1[0], *p1[1], FAIXA, a0, 7, progress=pr)
    line(c, *p2[0], *p2[1], FAIXA, a0, 7, progress=pr)
    ab = ep(t, C["17.b"], 0.5)
    c.drawCircle(*p1[1], 18, paint(FAIXA, a0))
    c.drawCircle(*p2[0], 18, paint("#FFFFFF", a0)); c.drawCircle(*p2[0], 18, paint(FAIXA, a0, stroke=5))
    c.drawCircle(*p1[1], 36, paint(GREEN, ab, stroke=4))
    text(c, "cheia: faz parte", 1450, 560, 34, "black", GREEN, ab)
    ac = ep(t, C["17.c"], 0.5)
    c.drawCircle(*p2[0], 36, paint(RED, ac, stroke=4))
    text(c, "vazia: ficou de fora", 1450, 360, 34, "black", RED, ac)


# ======================================================================
# recapitulação
# ======================================================================

FRASES = ["Colchete virado para o número: entra. Para fora: não",
          "Bolinha cheia entra; bolinha vazia não",
          "Infinito é sempre aberto"]


def b_recap(c, t, C, B):
    sid = "18" if B["start"] < C["30"] - 1 else "30"
    head(c, t, B["start"], "AS 3 FRASES", "PARA GUARDAR", GREEN)
    card(c, *CARD_R)
    for k, (cue, col) in enumerate((("a", PURPLE), ("b", FAIXA), ("c", GREEN))):
        a, d = rise(t, C[f"{sid}.{cue}"])
        y = 330 + k * 160 + d
        badge_num(c, k + 1, 230, y - 16, a, 32, bg=col)
        ftext(c, FRASES[k], 290, y, 46, "black", INK, a, align="left")
        # ícones à direita
        if k == 0:
            colchete(c, 1640, y - 16, 70, 1, a, GREEN); colchete(c, 1720, y - 16, 70, -1, a, RED)
        elif k == 1:
            c.drawCircle(1640, y - 16, 20, paint(FAIXA, a))
            c.drawCircle(1720, y - 16, 20, paint("#FFFFFF", a)); c.drawCircle(1720, y - 16, 20, paint(FAIXA, a, stroke=5))


# ======================================================================
# erros
# ======================================================================

def b_erro1(c, t, C, B):
    head(c, t, B["start"], "ERRO 1", "FECHAR O INFINITO", RED)
    erro_tiles(c, t, [(C["19.a"], "O ERRO", ["![−∞, 5]"], RED),
                      (C["19.b"], "POR QUE PARECE CERTO", ["o outro lado", "está fechado"], AMBER),
                      (C["19.c"], "A CORREÇÃO", ["infinito não", "se abraça", "!]−∞, 5]"], GREEN)])


def b_erro2(c, t, C, B):
    head(c, t, B["start"], "ERRO 2", "BOLINHA VAZIA \"ENTRA\"?", RED)
    erro_tiles(c, t, [(C["20.a"], "O ERRO", ["vazia =", "!ponto incluído"], RED),
                      (C["20.b"], "POR QUE PARECE CERTO", ["a linha CHEGA", "até a bolinha"], AMBER),
                      (C["20.c"], "A CORREÇÃO", ["chegar perto", "não é entrar", "!vazia: fora"], GREEN)])


def b_erro3(c, t, C, B):
    head(c, t, B["start"], "ERRO 3", "ACIMA DE × A PARTIR DE", RED)
    erro_tiles(c, t, [(C["21.a"], "O ERRO", ["\"acima de\" =", "!\"a partir de\""], RED),
                      (C["21.b"], "POR QUE PARECE CERTO", ["no dia a dia", "falamos igual"], AMBER),
                      (C["21.c"], "A CORREÇÃO", ["acima de 100: x > 100", "a partir de 18: x ≥ 18", "!100 fica fora"], GREEN)])


# ======================================================================
# exercício
# ======================================================================

EXS = [("22.a", "23.a", "a partir de 60 anos", "60", "+∞", 1, 0, (40, 80, [(40, "40"), (60, "60"), (80, "80")]), 60, "+inf"),
       ("22.b", "24.b", "de 10 a 20, contando os dois", "10", "20", 1, 1, (0, 30, [(0, "0"), (10, "10"), (20, "20"), (30, "30")]), 10, 20),
       ("22.c", "24.c", "abaixo de zero", "−∞", "0", 0, 0, (-20, 20, [(-20, "−20"), (-10, "−10"), (0, "0"), (10, "10"), (20, "20")]), "-inf", 0)]


def b_exercicio(c, t, C, B):
    head(c, t, B["start"], "SUA VEZ", "TRADUZA PARA COLCHETES E RETA", GREEN)
    card(c, *CARD_R)
    for k, (cq, cr, fr, A, B_, hL, hR, (lo, hi, ticks), va, vb) in enumerate(EXS):
        a, dy = rise(t, C[cq])
        y = 250 + k * 190 + dy
        badge_num(c, k + 1, 200, y, a, 26, bg=GREEN)
        fmid(c, '"' + fr + '"', 250, y, 32, "black", BLUE, a, align="left")
        ar = ep(t, C[cr], 0.5)
        notacao(c, 900, y, 50, A, B_, hL, hR, ar)
        r = RetaI(1150, 1640, y + 6, lo, hi, [(v, l) for v, l in ticks])
        r.base(c, ar)
        r.faixa(c, va, vb, ar, ease_io(prog(t, C[cr] + 0.3, 0.8)))
        for v, h in ((va, hL), (vb, hR)):
            if v not in ("+inf", "-inf"):
                r.bola(c, v, h, ar, r=13)
    if C["24.c"] < t:
        text(c, "0 °C não está abaixo de zero", 1395, 770, 24, "black", RED, ep(t, C["24.c"] + 2.5, 0.4))
    pause_badge(c, W / 2 - 230, 780, ep(t, C["22.p"], 0.5) * (1 - prog(t, C["23.t"] - 0.3, 0.4)), "PAUSE E TRADUZA")


# ======================================================================
# questão inédita
# ======================================================================

ALTS = [("A", "[20, +∞[", "a partir de 20", "26.a", "29.a", "leu a bolinha vazia como incluída"),
        ("B", "]20, +∞]", "acima de 20", "26.b", "29.b", "fechou o infinito"),
        ("C", "]20, +∞[", "acima de 20", "26.c", None, ""),
        ("D", "]20, +∞[", "a partir de 20", "27.d", "29.d", "acima de ≠ a partir de"),
        ("E", "[20, +∞]", "a partir de 20", "27.e", "29.e", "dois erros juntos")]


def b_questao(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO ESTILO ENEM", "A TARIFA DE ÁGUA", BLUE)
    card(c, 140, 180, 700, 640)
    pill(c, "QUESTÃO", 170, 224, BLUE, size=22, bounds=(0, 1920))
    text(c, "Tarifa mais cara de água", 180, 300, 32, "black", INK, ep(t, C["25.e1"], 0.5), align="left")
    text(c, "conforme o consumo do mês (m³):", 180, 345, 28, "black", INK2, ep(t, C["25.e1"], 0.5), align="left")
    a2 = ep(t, C["25.e2"], 0.5)
    r = RetaI(230, 720, 500, 0, 40, [(0, "0"), (10, "10"), (20, "20"), (30, "30")])
    r.base(c, a2)
    r.faixa(c, 20, "+inf", a2, ease_io(prog(t, C["25.e2"] + 0.3, 1.0)))
    r.bola(c, 20, 0, a2)
    text(c, "Qual alternativa descreve essa faixa?", 180, 640, 28, "black", INK, ep(t, C["25.e3"], 0.5), align="left")
    # leitura da resolução
    for k, (cue, s, col) in enumerate((("28.r1", "vazia no 20: o 20 NÃO entra", RED),
                                       ("28.r2", "seta: até +∞, sempre aberto", PURPLE),
                                       ("28.r3", "\"acima de 20\"", BLUE))):
        a = ep(t, C[cue], 0.4)
        ftext(c, s, 180, 700 + k * 40, 24, "black", col, a, align="left")
    # alternativas
    card(c, 880, 180, 900, 640, ep(t, C["26.t"], 0.5))
    aok = ep(t, C["28.r"], 0.5)
    for k, (L, nota, fr, cue_in, cue_x, why) in enumerate(ALTS):
        a, d = rise(t, C[cue_in])
        y = 270 + k * 112 + d
        ok = cue_x is None
        if ok and aok > 0:
            rrect(c, 905, y - 44, 850, 92, 14, GREEN, 0.15 * aok)
        badge_num(c, L, 945, y, a, 24, bg=GREEN if ok and aok > 0.5 else INK)
        ax = ep(t, C[cue_x], 0.4) if cue_x else 0
        ftext(c, nota, 990, y + 14, 40, "black", INK, a * (1 - 0.5 * ax), align="left")
        ftext(c, fr, 1230, y + 12, 30, "black", INK2, a * (1 - 0.5 * ax), align="left")
        if ax > 0:
            strike(c, 986, y + 2, 1500, y + 2, ax, RED, ax)
            ftext(c, why, 1230, y + 42, 22, "black", RED, ax, align="left")
    pause_badge(c, 260, 680, ep(t, C["27.p"], 0.5) * (1 - prog(t, C["28.t"] - 0.3, 0.4)))
    pill(c, "RESPOSTA: C", 1610, 230, GREEN, size=26, a=aok, anchor="center", bounds=(0, 1920))


# ======================================================================
# ponte e CTA
# ======================================================================

def pessoa(c, x, y, col, a, s=1.0):
    if a <= 0:
        return
    c.drawCircle(x, y - 34 * s, 16 * s, paint(col, a))
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x - 22 * s, y - 14 * s, 44 * s, 50 * s), 18 * s, 18 * s), paint(col, a))


def b_ponte(c, t, C, B):
    head(c, t, B["start"], "PRÓXIMO EPISÓDIO", "O DIAGRAMA DE VENN", PURPLE)
    card(c, *CARD_R)
    a0 = ep(t, C["31.t"], 0.5)
    r = RetaI(380, 1540, 300, 0, 7, T07(0, 7))
    r.base(c, a0 * (1 - 0.6 * ep(t, C["31.a"], 0.5)))
    r.faixa(c, 2, 5, a0 * (1 - 0.6 * ep(t, C["31.a"], 0.5)))
    text(c, "conjuntos de NÚMEROS", W / 2, 220, 30, "black", INK2, a0)
    aa = ep(t, C["31.a"], 0.5)
    c.drawCircle(850, 590, 140, paint(BLUE, aa * 0.10)); c.drawCircle(850, 590, 140, paint(BLUE, aa, stroke=5))
    c.drawCircle(1070, 590, 140, paint(AMBER, aa * 0.10)); c.drawCircle(1070, 590, 140, paint(AMBER, aa, stroke=5))
    for k, (x, y, col) in enumerate(((780, 590, BLUE), (830, 660, BLUE), (960, 610, PURPLE), (1140, 590, AMBER), (1090, 660, AMBER))):
        pessoa(c, x, y, col, aa * ep(t, C["31.a"] + 0.2 * k, 0.4), 0.9)
    text(c, "conjuntos de PESSOAS", W / 2, 420, 32, "black", PURPLE, aa)
    pill(c, "cai quase todo ano no ENEM", W / 2, 790, AMBER, size=28, a=ep(t, C["31.b"], 0.5) * (1 - prog(t, C["31.c"] - 0.2, 0.3)), anchor="center")
    pill(c, "EPISÓDIO 4: DIAGRAMA DE VENN", W / 2, 790, PURPLE, size=30, a=ep(t, C["31.c"], 0.5), anchor="center")


def b_cta(c, t, C, B):
    cta(c, t, C["32.like"], C["32.sub"], C["32.bell"], C["32.com"], C["32.bye"], "Frete grátis acima de R$ 100: a compra de 100 ganha?")


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, fechado=b_fechado, aberto=b_aberto,
              semiaberto=b_semiaberto, infinito=b_infinito, infinito_regra=b_infinito_regra, graficos=b_graficos,
              recap=b_recap, erro1=b_erro1, erro2=b_erro2, erro3=b_erro3, exercicio=b_exercicio, questao=b_questao,
              ponte=b_ponte, cta=b_cta)
