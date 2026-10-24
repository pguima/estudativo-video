"""Visual — Logaritmos, Episódio 3: tirando a incógnita do expoente (equações com log e mudança de base) (tema claro).
Peças comuns da série em ../../comum.py (reexporta o 019/comum.py: expr com potências, alternativas, erro_cards, atalho,
selo, regra...).
Peças deste episódio: elevador() (o log como elevador: o expoente desce até a linha do número e vira fator na frente),
porao() (log_b a vira a fração log a ÷ log b: a base cai para o porão), eq() (linha com textos e frações de logs
empilhadas), Plano (eixos e curva), linha(), mx().
Logs com base usam dígitos subscritos (log₂ 10); potências no texto usam sobrescritos (2ˣ, 1,05ᵗ).
Cores com função: azul = definição · roxo = regra / fórmula / log · âmbar = armadilha / expoente · verde = atalho ·
vermelho = erro.
"""
import importlib.util
from pathlib import Path
import skia
import motor
motor.set_theme("claro")
from motor import *  # noqa
from aula import *  # noqa

_p = Path(__file__).resolve().parents[2] / "comum.py"
_s = importlib.util.spec_from_file_location("comum042", _p)
K = importlib.util.module_from_spec(_s); _s.loader.exec_module(K)
K.usar_tempos(Path(__file__).resolve().parents[1] / "audio" / "tempos.json")
motor.set_theme("claro")
frame, head_seq, which, para, regra, selo, pause_timer, chip = (K.frame, K.head_seq, K.which, K.para, K.regra, K.selo,
                                                                K.pause_timer, K.chip)
ftext, ftext_w = K.ftext, K.ftext_w

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_logaritmos_ep3_equacoes_mudanca_base.mp4"
CARD_R = K.CARD_R
GRADE = "#EEEEEA"


# ======================================================================
# peças do episódio
# ======================================================================

def ease(u):
    u = clamp(u)
    return u * u * (3 - 2 * u)


def lerp(a, b, u):
    return a + (b - a) * u


def tx(c, s, x, cy, size, col, a, peso="black"):
    """texto alinhado à esquerda, centrado verticalmente em cy"""
    if a > 0:
        ftext(c, s, x, cy + size * 0.36, size, peso, col or INK, a, align="left")
    return ftext_w(s, peso, size)


def linha(c, partes, cx, cy, size, a, peso="black", align="center"):
    """texto numa linha, com cor por trecho: partes = [(texto, cor)]"""
    if a <= 0:
        return 0
    ws = [ftext_w(s_, peso, size) for s_, _ in partes]
    x = cx - sum(ws) / 2 if align == "center" else cx
    for (s_, col), w_ in zip(partes, ws):
        tx(c, s_, x, cy, size, col, a, peso)
        x += w_
    return sum(ws)


def mx(c, s, cx, cy, size, a, col=None, align="center"):
    """expressão matemática de uma cor só (potências)"""
    n = len(s.split())
    return K.expr(c, s, cx, cy, size, a, cores={i: col or INK for i in range(n)}, align=align)


def defin(c, termo, s, x, y, w, a, col=None, size=30):
    """faixa de definição: TERMO: frase"""
    if a <= 0:
        return
    col = col or BLUE
    rrect(c, x, y, w, 70, 18, mix("#FFFFFF", col, 0.12), a)
    linha(c, [(termo, col), (": " + s, INK)], x + 28, y + 35, size, a, align="left")


def logb(c, base, arg, x, cy, size, a, col=None, colb=None):
    """log com base subscrita (qualquer letra): log_base arg, alinhado à esquerda"""
    w1 = tx(c, "log", x, cy, size, col or INK, a)
    w2 = tx(c, base, x + w1 + 2, cy + size * 0.32, size * 0.55, colb or AMBER, a)
    w3 = tx(c, " " + arg, x + w1 + w2 + 4, cy, size, col or INK, a)
    return w1 + w2 + w3 + 6


def _item_w(it, size):
    if it[0] == "L":
        return (ftext_w("log", "black", size) + ftext_w(it[1], "black", size * 0.55)
                + ftext_w(" " + it[2], "black", size) + 6)
    if it[0] == "f":
        fs = size * 0.86
        return max(ftext_w(it[1], "black", fs), ftext_w(it[2], "black", fs)) + size * 0.3
    return ftext_w(it[1], "black", size)


def eq(c, itens, cx, cy, size, a, align="center", alfas=None):
    """linha com textos e frações empilhadas. itens: ("t", texto, cor) ou ("f", num, den, cor_num, cor_den)"""
    if a <= 0:
        return 0
    ws = [_item_w(it, size) for it in itens]
    x = cx - sum(ws) / 2 if align == "center" else cx
    for k, (it, w_) in enumerate(zip(itens, ws)):
        ak = a * (alfas or {}).get(k, 1.0)
        if it[0] == "L":
            logb(c, it[1], it[2], x, cy, size, ak, it[3])
        elif it[0] == "f":
            fs = size * 0.86
            line(c, x + size * 0.1, cy, x + w_ - size * 0.1, cy, INK, ak, max(3, size * 0.07))
            text_mid(c, it[1], x + w_ / 2, cy - fs * 0.62, fs, "black", it[3] or INK, ak)
            text_mid(c, it[2], x + w_ / 2, cy + fs * 0.66, fs, "black", it[4] or INK, ak)
        else:
            tx(c, it[1], x, cy, size, it[2], ak)
        x += w_
    return sum(ws)


def caixa(c, x, y, w, h, col, a, r=22, fill=0.14):
    if a > 0:
        rrect(c, x, y, w, h, r, mix("#FFFFFF", col, fill), a)


class Plano:
    """plano cartesiano num retângulo (x0, y0, w, h) com faixas xr, yr."""

    def __init__(s, x0, y0, w, h, xr, yr):
        s.x0, s.y0, s.w, s.h, s.xr, s.yr = x0, y0, w, h, xr, yr

    def px(s, x):
        return s.x0 + (x - s.xr[0]) / (s.xr[1] - s.xr[0]) * s.w

    def py(s, y):
        return s.y0 + s.h - (y - s.yr[0]) / (s.yr[1] - s.yr[0]) * s.h

    def eixos(s, c, a, xt=(), yt=(), size=22, rot=("x", "y")):
        if a <= 0:
            return
        for v in xt:
            line(c, s.px(v), s.y0, s.px(v), s.y0 + s.h, GRADE, a, 2)
        for v in yt:
            line(c, s.x0, s.py(v), s.x0 + s.w, s.py(v), GRADE, a, 2)
        oy, ox = s.py(0), s.px(0)
        arrow(c, s.x0, oy, s.x0 + s.w + 24, oy, INK2, a, 3, 12)
        arrow(c, ox, s.y0 + s.h, ox, s.y0 - 22, INK2, a, 3, 12)
        text(c, rot[0], s.x0 + s.w + 22, oy + 36, 24, "black", GRAY, a)
        text(c, rot[1], ox - 22, s.y0 - 6, 24, "black", GRAY, a, align="right")
        f = lambda v: f"{v:g}".replace(".", ",")
        for v in xt:
            if v != 0:
                text(c, f(v), s.px(v), oy + size + 10, size, "bold", INK2, a)
        for v in yt:
            if v != 0:
                text(c, f(v), ox - 12, s.py(v) + size * 0.36, size, "bold", INK2, a, align="right")

    def curva(s, c, a, f, col, u=1.0, width=7, n=160):
        if a <= 0 or u <= 0:
            return
        xa, xb = s.xr[0], s.xr[0] + (s.xr[1] - s.xr[0]) * clamp(u)
        c.save()
        c.clipRect(skia.Rect.MakeXYWH(s.x0, s.y0 - 4, s.w, s.h + 8))
        path = skia.Path()
        for k in range(n + 1):
            x = xa + (xb - xa) * k / n
            y = max(min(f(x), s.yr[1] * 3), s.yr[0] - 5)
            (path.moveTo if k == 0 else path.lineTo)(s.px(x), s.py(y))
        c.drawPath(path, paint(col, a, stroke=width, cap_round=True))
        c.restore()

    def ponto(s, c, x, y, col, a, rot_=None, dx=18, dy=-30, size=22, r=9):
        if a <= 0:
            return
        c.drawCircle(s.px(x), s.py(y), r + 3, paint("#FFFFFF", a))
        c.drawCircle(s.px(x), s.py(y), r, paint(col, a))
        if rot_:
            pill(c, rot_, s.px(x) + dx, s.py(y) + dy, col, size=size, a=a, bounds=(0, 1920))


def elevador(c, t, t0, base_s, rhs_s, var, cx, cy, size, dur=3.4, a=1.0, logs=True):
    """O ELEVADOR: base^var = rhs → (log dos dois lados) → var · log base = log rhs.
    Antes de t0: a equação exponencial. Fase 1: os "log" aparecem. Fase 2: a cabine leva o expoente para o térreo
    (desce) e depois para a frente; o "·" aparece quando ele chega."""
    if a <= 0:
        return
    u = (t - t0) / dur
    pre = "log " if logs else ""
    sv = size
    w_var, w_dot = ftext_w(var, "black", sv), ftext_w(" · ", "black", sv)
    w_lb, w_eq, w_lr = ftext_w(pre + base_s, "black", sv), ftext_w(" = ", "black", sv), ftext_w(pre + rhs_s, "black", sv)
    total = w_var + w_dot + w_lb + w_eq + w_lr
    x = cx - total / 2
    x_var, x_dot, x_lb = x, x + w_var, x + w_var + w_dot
    x_eq = x_lb + w_lb
    x_lr = x_eq + w_eq
    a_log = a * ease(u / 0.25) if logs else 0
    w_pre = ftext_w(pre, "black", sv)
    ss = sv * 0.6
    # posições compactas (antes dos logs): base^var = rhs, centrado
    w_b, w_v = ftext_w(base_s, "black", sv), ftext_w(var, "black", ss)
    w_r = ftext_w(rhs_s, "black", sv)
    xc = cx - (w_b + w_v + 8 + w_eq + w_r) / 2
    ul = ease(u / 0.3)
    xb_ = lerp(xc, x_lb + w_pre, ul)
    xe_ = lerp(xc + w_b + w_v + 8, x_eq, ul)
    xr_ = lerp(xe_ + w_eq, x_lr + w_pre, ul) if ul < 1 else x_lr + w_pre
    if a_log > 0:
        tx(c, "log ", xb_ - w_pre, cy, sv, PURPLE, a_log)
        tx(c, "log ", xr_ - w_pre, cy, sv, PURPLE, a_log)
    tx(c, base_s, xb_, cy, sv, INK, a)
    tx(c, " = ", xe_, cy, sv, INK, a)
    tx(c, rhs_s, xr_, cy, sv, INK, a)
    # o expoente viajando
    xs = xb_ + w_b + 4
    ys = cy - sv * 0.5
    u1 = ease((u - 0.3) / 0.3)      # desce
    u2 = ease((u - 0.62) / 0.28)    # vai para a frente
    if u < 0.3:
        px_, py_, sz = xs, ys, ss
    else:
        px_ = lerp(xs, x_var, u2)
        py_ = lerp(ys, cy, u1)
        sz = lerp(ss, sv, u1)
    cab = a * clamp((u - 0.28) / 0.06) * (1 - clamp((u - 0.92) / 0.08))
    if cab > 0:
        line(c, xs + ss * 0.3, ys - sv * 0.55, xs + ss * 0.3, cy + sv * 0.55, PURPLE, cab * 0.5, 3, dash=(10, 8))
        wv = ftext_w(var, "black", sz)
        rrect(c, px_ - 12, py_ - sz * 0.75, wv + 24, sz * 1.5, 10, mix("#FFFFFF", PURPLE, 0.18), cab)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(px_ - 12, py_ - sz * 0.75, wv + 24, sz * 1.5), 10, 10),
                    paint(PURPLE, cab, stroke=4))
        pill(c, "log", px_ + wv / 2, py_ - sz * 0.75 - 22, PURPLE, size=18, a=cab, anchor="center", bounds=(0, 1920))
    tx(c, var, px_, py_, sz, AMBER, a)
    a_dot = a * ease((u - 0.86) / 0.14)
    if a_dot > 0:
        tx(c, " · ", x_dot, cy, sv, INK, a_dot)


def porao(c, t, t0, arg, base, cx, cy, size, dur=2.8, a=1.0, rot_=True):
    """O PORÃO: log_base arg → log arg / log base (a base cai para baixo da barra)."""
    if a <= 0:
        return
    u = (t - t0) / dur
    s_sub = size * 0.55
    w_log, w_sp = ftext_w("log", "black", size), ftext_w(" ", "black", size)
    w_sub, w_arg = ftext_w(base, "black", s_sub), ftext_w(arg, "black", size)
    tot0 = w_log + w_sub + w_sp + w_arg + 6
    x0 = cx - tot0 / 2
    w_num = ftext_w("log " + arg, "black", size)
    w_den = ftext_w("log " + base, "black", size)
    yn, yd = cy - size * 0.68, cy + size * 0.72
    u1 = ease(u / 0.5)
    # numerador: "log" + arg
    xl = lerp(x0, cx - w_num / 2, u1)
    yl = lerp(cy, yn, u1)
    tx(c, "log", xl, yl, size, PURPLE, a)
    xa = lerp(x0 + w_log + w_sub + w_sp + 6, cx - w_num / 2 + ftext_w("log ", "black", size), u1)
    tx(c, arg, xa, yl, size, INK, a)
    # a base desce para o porão
    xb = lerp(x0 + w_log + 3, cx - w_den / 2 + ftext_w("log ", "black", size), u1)
    yb = lerp(cy + size * 0.32, yd, u1)
    tx(c, base, xb, yb, lerp(s_sub, size, u1), AMBER, a)
    ab = a * ease((u - 0.35) / 0.3)
    if ab > 0:
        wbar = max(w_num, w_den) + 30
        line(c, cx - wbar / 2, cy, cx - wbar / 2 + wbar * ab, cy, INK, a, max(4, size * 0.07))
        tx(c, "log ", cx - w_den / 2, yd, size, PURPLE, ab)
    ar = a * ease((u - 0.8) / 0.2)
    if rot_ and ar > 0:
        pill(c, "a base vai para o porão", cx, yd + size * 0.95, AMBER, size=22, a=ar, anchor="center",
             bounds=(0, 1920))


def _enunciado(c, linhas, a, y0=250, size=28, w=700):
    y = y0
    for s, col in linhas:
        for ln in K.wrap(s, "black", size, w):
            text(c, ln, 190, y, size, "black", col, a, align="left")
            y += size + 12
        y += 8
    return y


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "LOGARITMOS · EPISÓDIO 3", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["01.a"], 0.5)
    if aa > 0:
        linha(c, [("5% ao ano", PURPLE), (" · em quanto tempo ", INK), ("DOBRA?", AMBER)], W / 2, 240, 46, aa)
    for k, (cue, rot_, anos, col, frac) in enumerate((("01.b", "JUROS SIMPLES", "20 anos", BLUE, 1.0),
                                                      ("01.c", "JUROS COMPOSTOS", "≈ 14,2 anos", GREEN, 14.2 / 20))):
        ak = ep(t, C[cue], 0.5)
        if ak <= 0:
            continue
        y = 340 + k * 120
        text(c, rot_, 560, y + 12, 30, "black", col, ak, align="right")
        wmax = 760
        rrect(c, 600, y - 30, wmax * frac * ease((t - C[cue]) / 1.0), 60, 14, col, ak * 0.85)
        text(c, anos, 600 + wmax * frac + 20, y + 12, 34, "black", INK, ak * clamp((t - C[cue] - 0.8) / 0.4),
             align="left")
    ad = ep(t, C["01.d"], 0.5)
    if ad > 0:
        elevador(c, t, C["01.d"] + 1.4, "1,05", "2", "t", W / 2, 690, 92, dur=3.0, a=ad)
        if t < C["01.d"] + 1.4:
            selo(c, 1500, 600, ad, "DERRUBAR O t", AMBER, -6, 28)


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "LOGARITMOS · EP. 3", "AO FINAL DESTA AULA", GREEN)
    a0 = ep(t, C["02"], 0.4)
    if a0 > 0:
        pill(c, "3º episódio da série de LOGARITMOS", W / 2, 240, BLUE, size=30, a=a0, anchor="center")
    itens = [("02.a", "QUALQUER", "equação exponencial", BLUE), ("02.b", "NÃO FECHA?", "na mesma base", AMBER),
             ("02.c", "OS LOGS DADOS", "pelo enunciado", PURPLE)]
    for k, (cue, tit, sub, col) in enumerate(itens):
        ak = ep(t, C[cue], 0.5)
        if ak <= 0:
            continue
        x = 440 + k * 520
        rrect(c, x - 230, 330, 460, 330, 26, "#FFFFFF", ak, shadow=True)
        rrect(c, x - 230, 330, 460, 70, 26, col, ak * 0.16)
        badge_num(c, k + 1, x, 470, ak, 34, bg=col)
        text(c, tit, x, 570, 40, "black", col, ak)
        text(c, sub, x, 625, 28, "bold", INK2, ak)


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "LEMBRETES", "EM 30 SEGUNDOS", GREEN)
    cards_ = [("03.a", "EPISÓDIO 2", [("t", "log Mᵏ = k · log M", PURPLE)], 260),
              ("03.b", "O KIT", [("t", "log 2 ≈ 0,301", BLUE)], 260),
              ("03.c", "FUNÇÃO EXPONENCIAL", [("t", "+8% → × 1,08", GREEN)], 260),
              ("03.d", "JUROS COMPOSTOS", [("t", "regra do 72", AMBER)], 260)]
    for k, (cue, tit, it, _) in enumerate(cards_):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        col = it[0][2]
        x, y = 240 + (k % 2) * 740, 250 + (k // 2) * 280 + d
        rrect(c, x, y, 700, 240, 24, "#FFFFFF", a, shadow=True)
        pill(c, tit, x + 30, y + 40, col, size=22, a=a, bounds=(0, 1920))
        eq(c, it, x + 350, y + 130, 52, a)
        if cue == "03.b":
            eq(c, [("t", "log 3 ≈ 0,477", BLUE)], x + 350, y + 195, 40, a)
        if cue == "03.c":
            eq(c, [("t", "−10% → × 0,9", RED)], x + 350, y + 195, 40, a)
        if cue == "03.d":
            eq(c, [("t", "dobra em ≈ 72 ÷ taxa", INK2)], x + 350, y + 195, 34, a)


def b_concreto(c, t, C, B):
    head(c, t, B["start"], "PERGUNTAS DE TEMPO", "QUANDO?", BLUE)
    card(c, *CARD_R)
    itens = [("04.a", "DINHEIRO", "dobra em quantos anos?", GREEN, "1,08ᵗ = 2"),
             ("04.b", "BACTÉRIAS", "chegam a 50 000 quando?", BLUE, "3ᵗ = 50"),
             ("04.c", "EQUIPAMENTO", "vale a metade quando?", RED, "0,9ᵗ = 0,5")]
    for k, (cue, tit, s_, col, e_) in enumerate(itens):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        x = 220 + k * 510
        rrect(c, x, 230 + d, 470, 340, 24, "#FFFFFF", a, shadow=True)
        text(c, tit, x + 235, 300 + d, 34, "black", col, a)
        text(c, s_, x + 235, 360 + d, 28, "bold", INK2, a)
        ad = ep(t, C["04.d"], 0.5)
        if ad > 0:
            text(c, e_, x + 235, 480 + d, 56, "black", INK, ad)
            pill(c, "t = ?", x + 235, 535 + d, AMBER, size=24, a=ad, anchor="center", bounds=(0, 1920))
    ad = ep(t, C["04.d"], 0.5)
    if ad > 0:
        regra(c, "A RESPOSTA ESTÁ NO EXPOENTE · E A BASE NÃO FECHA", W / 2, 700, ad, 34, PURPLE)


# ======================================================================
# bloco a — 2^x = 10 · gráfico · atalho
# ======================================================================

def b_elev1(c, t, C, B):
    head(c, t, B["start"], "O ELEVADOR", "LOG DOS DOIS LADOS", PURPLE)
    card(c, *CARD_R)
    a0 = ep(t, C["05"], 0.4)
    aa = ep(t, C["05.a"], 0.5)
    if aa > 0:
        pill(c, "10 não é potência de 2: a mesma base NÃO FECHA", W / 2, 220, AMBER, size=26, a=aa, anchor="center")
    ab = ep(t, C["05.b"], 0.5)
    if ab > 0:
        defin(c, "APLICAR LOG DOS DOIS LADOS", "escrever log na frente de cada lado", 300, 640, 1320, ab, BLUE, 30)
    # a equação: antes de {b} sem logs; o elevador começa em {c}
    t_go = C["05.c"] + 0.4
    if t < C["05.b"]:
        elevador(c, t, 1e9, "2", "10", "x", W / 2, 420, 110, a=a0)
    else:
        elevador(c, t, t_go, "2", "10", "x", W / 2, 420, 110, dur=3.4, a=a0)
        if t < t_go:
            for xx in (W / 2 - 330, W / 2 + 170):
                pill(c, "log", xx, 300, PURPLE, size=26, a=ep(t, C["05.b"] + 0.6, 0.4), anchor="center",
                     bounds=(0, 1920))
    acc = ep(t, C["05.c"], 0.5)
    if acc > 0:
        pill(c, "o log traz o expoente para o TÉRREO", W / 2, 560, PURPLE, size=28, a=acc, anchor="center")


def b_grafico(c, t, C, B):
    head(c, t, B["start"], "AGORA, DIVIDIR", "E ESTIMAR", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["06.a"], 0.5)
    if aa > 0:
        eq(c, [("t", "x = ", INK), ("f", "log 10", "log 2", INK, INK), ("t", " = ", INK), ("f", "1", "0,301", INK, INK),
               ("t", " ≈ 3,32", GREEN)], 1300, 280, 54, aa)
    ab = ep(t, C["06.b"], 0.5)
    if ab > 0:
        defin(c, "ESTIMAR", "chutar com critério, antes da conta", 960, 420, 680, ab, BLUE, 26)
    acc = ep(t, C["06.c"], 0.5)
    if acc > 0:
        linha(c, [("2³ = 8", BLUE), ("  <  10  <  ", AMBER), ("2⁴ = 16", BLUE)], 1300, 580, 44, acc)
    P = Plano(230, 230, 620, 540, (0, 4.6), (0, 18))
    ag = ep(t, C["06"], 0.5)
    P.eixos(c, ag, xt=(1, 2, 3, 4), yt=(4, 8, 10, 16))
    P.curva(c, ag, lambda x: 2 ** x, BLUE, u=ep(t, C["06"], 1.6))
    if ag > 0:
        pill(c, "y = 2ˣ", P.px(4.15), P.py(17.2), BLUE, size=22, a=ag, anchor="center", bounds=(0, 1920))
    if acc > 0:
        P.ponto(c, 3, 8, BLUE, acc, "8", dx=18, dy=20)
        P.ponto(c, 4, 16, BLUE, acc, "16", dx=-70, dy=-6)
    ad = ep(t, C["06.d"], 0.5)
    if ad > 0:
        line(c, P.x0, P.py(10), P.x0 + P.w, P.py(10), AMBER, ad, 4, dash=(14, 10))
        text(c, "y = 10", P.x0 + P.w - 50, P.py(10) - 16, 24, "black", AMBER, ad)
        xi = 3.3219
        line(c, P.px(xi), P.py(10), P.px(xi), P.py(0), GREEN, ad, 4, dash=(8, 8))
        P.ponto(c, xi, 10, GREEN, ad)
        pill(c, "x ≈ 3,32", P.px(xi), P.py(0) + 64, GREEN, size=24, a=ad, anchor="center", bounds=(0, 1920))
        regra(c, "ENTRE 3 E 4", 1300, 710, ad, 38, GREEN)


def b_atalho_est(c, t, C, B):
    head(c, t, B["start"], "ATALHO", "ESTIME PRIMEIRO", GREEN)
    card(c, *CARD_R)
    a0 = ep(t, C["07"], 0.4)
    K.atalho(c, 240, 200, 1440, 150, "ATALHO", ["ache as duas potências INTEIRAS que cercam o número"], a0, 36)
    aa = ep(t, C["07.a"], 0.5)
    if aa > 0:
        xa, xb, y = 420, 1500, 500
        line(c, xa, y, xb, y, INK2, aa, 4)
        for k, (lab, xx, col) in enumerate((("2³ = 8", xa + 160, BLUE), ("2⁴ = 16", xb - 160, BLUE))):
            line(c, xx, y - 22, xx, y + 22, INK2, aa, 4)
            pill(c, lab, xx, y - 64, col, size=28, a=aa, anchor="center")
        ab = ep(t, C["07.b"], 0.5)
        if ab > 0:
            rrect(c, xa + 160, y - 14, (xb - 160) - (xa + 160), 28, 14, GREEN, ab * 0.35)
            pill(c, "a resposta TEM de cair aqui", W / 2, y + 74, GREEN, size=28, a=ab, anchor="center")
    acc = ep(t, C["07.c"], 0.5)
    if acc > 0:
        regra(c, "SAIU FORA? ERROU UM PASSO", W / 2, 720, acc, 38, RED)


# ======================================================================
# bloco b — mudança de base (o porão) · bloco c — quem fica em cima
# ======================================================================

def b_porao(c, t, C, B):
    head(c, t, B["start"], "MUDANÇA DE BASE", "A BASE VAI PARA O PORÃO", PURPLE)
    card(c, *CARD_R)
    aa = ep(t, C["08.a"], 0.5)
    if aa > 0:
        defin(c, "MUDANÇA DE BASE", "reescrever o log como divisão de logs decimais", 300, 200, 1320, aa, BLUE, 30)
    ab = ep(t, C["08.b"], 0.5)
    if ab > 0:
        porao(c, t, C["08.c"], "a", "b", 620, 470, 84, a=ab)
    ad = ep(t, C["08.d"], 0.5)
    if ad > 0:
        rrect(c, 1020, 340, 600, 300, 24, "#FFFFFF", ad, shadow=True)
        text_mid(c, "log₂ 10", 1320, 400, 48, "black", INK, ad)
        eq(c, [("t", "= ", INK), ("f", "log 10", "log 2", INK, AMBER), ("t", " = ", INK), ("f", "1", "0,301", INK, INK)],
           1320, 510, 46, ad)
        pill(c, "≈ 3,32 · a mesma conta de antes", 1320, 610, GREEN, size=24, a=ad, anchor="center")


def b_porao2(c, t, C, B):
    head(c, t, B["start"], "MUDANÇA DE BASE", "QUALQUER BASE NO PORÃO", PURPLE)
    card(c, *CARD_R)
    aa = ep(t, C["09.a"], 0.5)
    if aa > 0:
        rrect(c, 640, 200, 640, 150, 24, "#FFFFFF", aa, shadow=True)
        text_mid(c, "log₄ 32", W / 2, 275, 76, "black", INK, aa)
    ab = ep(t, C["09.b"], 0.5)
    if ab > 0:
        eq(c, [("t", "= ", INK), ("f", "log₂ 32", "log₂ 4", INK, AMBER), ("t", " = ", INK), ("f", "5", "2", INK, AMBER)],
           W / 2, 500, 66, ab)
        pill(c, "porão na base 2: 32 = 2⁵ e 4 = 2²", W / 2, 640, PURPLE, size=26, a=ab, anchor="center")
    acc = ep(t, C["09.c"], 0.5)
    if acc > 0:
        caixa(c, 760, 700, 400, 110, GREEN, acc)
        text_mid(c, "= 2,5", W / 2, 755, 60, "black", GREEN, acc)


def b_emcima(c, t, C, B):
    head(c, t, B["start"], "QUEM FICA EM CIMA?", "NUMERADOR E DENOMINADOR", PURPLE)
    card(c, *CARD_R)
    aa = ep(t, C["10.a"], 0.5)
    if aa > 0:
        eq(c, [("f", "numerador", "denominador", BLUE, BLUE)], 460, 330, 50, aa)
        pill(c, "em cima", 760, 290, BLUE, size=22, a=aa, bounds=(0, 1920))
        pill(c, "embaixo", 760, 372, BLUE, size=22, a=aa, bounds=(0, 1920))
    ab = ep(t, C["10.b"], 0.5)
    if ab > 0:
        eq(c, [("L", "b", "a", INK), ("t", "  = ", INK), ("f", "log a", "log b", INK, AMBER)], 1360, 330, 50, ab)
        text(c, "em cima: o LOGARITMANDO · embaixo: a BASE", 1360, 470, 26, "black", INK2, ab)
    acc = ep(t, C["10.c"], 0.5)
    if acc > 0:
        rrect(c, 240, 540, 700, 230, 22, mix("#FFFFFF", GREEN, 0.12), acc)
        text(c, "log₂ 8 TEM de dar 3", 590, 590, 32, "black", GREEN, acc)
        eq(c, [("f", "0,903", "0,301", INK, INK), ("t", " = 3", GREEN)], 590, 690, 48, acc)
    ad = ep(t, C["10.d"], 0.5)
    if ad > 0:
        rrect(c, 980, 540, 700, 230, 22, mix("#FFFFFF", RED, 0.10), ad)
        text(c, "invertida", 1330, 590, 32, "black", RED, ad)
        eq(c, [("f", "0,301", "0,903", INK, INK), ("t", " = 1/3", RED)], 1330, 690, 48, ad)
        selo(c, 1600, 560, ad, "ERRADO", RED, 8, 24)
    ae = ep(t, C["10.e"], 0.5)
    if ae > 0:
        pill(c, "ATALHO · na dúvida, monte a fração com um caso que você sabe DE CABEÇA", W / 2, 810, GREEN, size=24,
             a=ae, anchor="center")


# ======================================================================
# bloco d — o capital que dobra · de onde vem a fórmula
# ======================================================================

def b_elev2(c, t, C, B):
    head(c, t, B["start"], "O GANCHO", "O CAPITAL QUE DOBRA", GREEN)
    card(c, *CARD_R)
    aa = ep(t, C["11.a"], 0.5)
    if aa > 0:
        pill(c, "5% ao ano → fator 1,05", W / 2, 220, GREEN, size=28, a=aa, anchor="center")
        elevador(c, t, C["11.b"], "1,05", "2", "t", W / 2, 360, 96, dur=3.2, a=aa)
    acc = ep(t, C["11.c"], 0.5)
    if acc > 0:
        pill(c, "em cima: o log do RESULTADO", 560, 500, PURPLE, size=24, a=acc, anchor="center", bounds=(0, 1920))
        eq(c, [("t", "t = ", AMBER), ("f", "log 2", "log 1,05", INK, INK), ("t", " = ", INK),
               ("f", "0,301", "0,0212", INK, INK)], 760, 650, 54, acc)
        a2 = ep(t, C["11.c"] + 3.0, 0.4)
        if a2 > 0:
            caixa(c, 1240, 590, 440, 120, GREEN, a2)
            text_mid(c, "≈ 14,2 anos", 1460, 650, 52, "black", GREEN, a2)


def b_formula(c, t, C, B):
    head(c, t, B["start"], "CONFERE?", "DE ONDE VEM A FÓRMULA", PURPLE)
    card(c, *CARD_R)
    aa = ep(t, C["12.a"], 0.5)
    if aa > 0:
        rrect(c, 240, 220, 700, 220, 24, "#FFFFFF", aa, shadow=True)
        text(c, "JUROS SIMPLES", 590, 280, 30, "black", BLUE, aa)
        text(c, "100% ÷ 5% = 20 anos", 590, 360, 40, "black", INK, aa)
        text(c, "compostos dobram ANTES", 590, 412, 24, "bold", GREEN, aa)
    ab = ep(t, C["12.b"], 0.5)
    if ab > 0:
        rrect(c, 980, 220, 700, 220, 24, mix("#FFFFFF", GREEN, 0.12), ab)
        text(c, "REGRA DO 72", 1330, 280, 30, "black", GREEN, ab)
        text(c, "72 ÷ 5 = 14,4", 1330, 360, 44, "black", INK, ab)
        text(c, "bem perto de 14,2", 1330, 412, 24, "bold", GREEN, ab)
    acc = ep(t, C["12.c"], 0.5)
    if acc > 0:
        rrect(c, 340, 500, 1240, 260, 26, mix("#FFFFFF", PURPLE, 0.10), acc)
        pill(c, "a fórmula do tempo · série de Juros compostos", W / 2, 540, PURPLE, size=24, a=acc, anchor="center")
        eq(c, [("t", "t = ", AMBER), ("f", "log (M/C)", "log (1 + i)", INK, INK)], W / 2, 660, 56, acc)


# ======================================================================
# bloco e — isole a potência · bloco f — decaimento · atalho do sinal
# ======================================================================

def b_isolar(c, t, C, B):
    head(c, t, B["start"], "ISOLE A POTÊNCIA", "ANTES DO LOG", AMBER)
    card(c, *CARD_R)
    aa = ep(t, C["13.a"], 0.5)
    sai = ep(t, C["13.b"] + 1.0, 0.8)
    if aa > 0:
        mx(c, "1000 · 3^t = 50000", W / 2, 260, 70, aa * (1 - 0.6 * sai), INK)
    ab = ep(t, C["13.b"], 0.5)
    if ab > 0:
        defin(c, "ISOLAR A POTÊNCIA", "deixá-la sozinha de um lado", 300, 330, 1320, ab, BLUE, 30)
        pill(c, "divida os dois lados por 1 000", W / 2, 450, AMBER, size=26, a=sai, anchor="center")
        caixa(c, 700, 490, 520, 120, GREEN, sai)
        mx(c, "3^t = 50", W / 2, 550, 70, sai, GREEN)
    acc = ep(t, C["13.c"], 0.5)
    if acc > 0:
        rrect(c, 300, 650, 1320, 150, 22, mix("#FFFFFF", AMBER, 0.12), acc)
        text(c, "log direto: log de um PRODUTO vira SOMA", W / 2, 700, 28, "black", AMBER, acc)
        linha(c, [("log (1 000 · 3ᵗ) = ", INK), ("3 + ", PURPLE), ("t · log 3", INK)], W / 2, 760, 40, acc)


def b_decai(c, t, C, B):
    head(c, t, B["start"], "QUANDO O VALOR CAI", "DECAIMENTO", RED)
    card(c, *CARD_R)
    aa = ep(t, C["14.a"], 0.5)
    if aa > 0:
        rrect(c, 240, 210, 640, 130, 22, "#FFFFFF", aa, shadow=True)
        text(c, "CELULAR · −25% ao ano", 560, 260, 30, "black", RED, aa)
        text(c, "vale a metade quando?", 560, 310, 28, "bold", INK2, aa)
    ab = ep(t, C["14.b"], 0.5)
    if ab > 0:
        pill(c, "fator MENOR que 1", 1300, 230, RED, size=24, a=ab, anchor="center")
        text_mid(c, "0,75ᵗ = 0,5", 1300, 300, 64, "black", INK, ab)
    acc = ep(t, C["14.c"], 0.5)
    if acc > 0:
        rrect(c, 240, 390, 1440, 170, 22, mix("#FFFFFF", AMBER, 0.10), acc)
        text(c, "entre 0 e 1 → log NEGATIVO", W / 2, 440, 30, "black", AMBER, acc)
        linha(c, [("log 0,75 = log 3 − 2 · log 2 = 0,477 − 0,602 = ", INK), ("−0,125", RED)], W / 2, 510, 34, acc)
    ad = ep(t, C["14.d"], 0.5)
    if ad > 0:
        eq(c, [("t", "t = ", AMBER), ("f", "log 0,5", "log 0,75", INK, INK), ("t", " = ", INK),
               ("f", "−0,301", "−0,125", RED, RED)], 760, 680, 52, ad)
        a2 = ep(t, C["14.d"] + 2.2, 0.4)
        if a2 > 0:
            caixa(c, 1200, 620, 480, 120, GREEN, a2)
            text_mid(c, "≈ 2,4 anos", 1440, 680, 52, "black", GREEN, a2)
            pill(c, "positivo", 1440, 770, GREEN, size=22, a=a2, anchor="center", bounds=(0, 1920))


def b_atalho_sinal(c, t, C, B):
    head(c, t, B["start"], "ATALHO", "O SINAL NO DECAIMENTO", GREEN)
    card(c, *CARD_R)
    a0 = ep(t, C["15"], 0.4)
    K.atalho(c, 240, 200, 1440, 150, "ATALHO", ["os DOIS logs são negativos: menos com menos dá MAIS"], a0, 36)
    aa = ep(t, C["15.a"], 0.5)
    if aa > 0:
        eq(c, [("f", "(−)", "(−)", RED, RED), ("t", "  =  ", INK), ("t", "(+)", GREEN)], W / 2, 500, 80, aa)
    ab = ep(t, C["15.b"], 0.5)
    if ab > 0:
        regra(c, "TEMPO NEGATIVO? UM SINAL SE PERDEU", W / 2, 720, ab, 38, RED)


# ======================================================================
# nós fazemos
# ======================================================================

def b_exercicio(c, t, C, B):
    head_seq(c, t, C, [("16", "SUA VEZ", "PAUSE E TENTE", GREEN), ("17", "VAMOS JUNTOS", "LOG DE 5 PELO KIT", GREEN)])
    card(c, *CARD_R)
    aa = ep(t, C["16.a"], 0.5)
    if aa > 0:
        rrect(c, 560, 200, 800, 150, 24, "#FFFFFF", aa, shadow=True)
        text_mid(c, "2ˣ = 5", 860, 275, 76, "black", INK, aa)
        pill(c, "log 2 = 0,30", 1180, 275, BLUE, size=26, a=aa, anchor="center")
    if t < C["17"]:
        ab = ep(t, C["16.b"], 0.5)
        if ab > 0:
            pill(c, "dica: 5 = 10 ÷ 2", W / 2, 440, GREEN, size=30, a=ab, anchor="center")
        pause_timer(c, t, C["16.end"] - 1.9, W / 2, 620)
        return
    a1 = ep(t, C["17.a"], 0.4)
    if a1 > 0:
        linha(c, [("log 5 = log 10 − log 2 = 1 − 0,30 = ", INK), ("0,70", PURPLE)], W / 2, 440, 40, a1)
    ab = ep(t, C["17.b"], 0.5)
    if ab > 0:
        eq(c, [("t", "x = ", AMBER), ("f", "log 5", "log 2", INK, AMBER), ("t", " = ", INK),
               ("f", "0,70", "0,30", INK, INK)], 760, 600, 54, ab)
        caixa(c, 1200, 545, 420, 110, GREEN, ep(t, C["17.b"] + 2.6, 0.4))
        text_mid(c, "≈ 2,33", 1410, 600, 54, "black", GREEN, ep(t, C["17.b"] + 2.6, 0.4))
    acc = ep(t, C["17.c"], 0.5)
    if acc > 0:
        linha(c, [("2² = 4", BLUE), ("  <  5  <  ", AMBER), ("2³ = 8", BLUE)], W / 2, 750, 40, acc)
        selo(c, 1560, 740, acc, "CONFERE", GREEN, -6, 26)


# ======================================================================
# recap
# ======================================================================

FRASES = ["Aplique log dos dois lados e o expoente desce.",
          "Isole a potência antes de aplicar o log.",
          "Na mudança de base, a base vai para baixo."]


def b_recap(c, t, C, B):
    sid = which(t, C, ["18", "34"])
    frame(c, t, B["start"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "18" else "PARA FECHAR", PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 300 + k * 180 + d
        badge_num(c, k + 1, 260, y - 16, a, 36, bg=PURPLE)
        para(c, s, 320, y, 50, "black", INK, a, 1360, 60)


# ======================================================================
# erros
# ======================================================================

ERROS = [("log₂ 10 = log 2 ÷ log 10",
          "o 2 aparece primeiro na leitura",
          "a base vai para o porão: log₂ 10 = log 10 ÷ log 2 ≈ 3,32"),
         ("log (1 000 · 3ᵗ) = 3t · log 3",
          "o log desce o expoente, e parece descer tudo junto",
          "log de produto é soma: 3 + t · log 3 (ou isole a potência antes)"),
         ("log 0,6 = 0,778",
          "os algarismos são os mesmos do log 6",
          "0,6 = 6 ÷ 10: tire 1 → log 0,6 = 0,778 − 1 = −0,222 (menor que 1: log negativo)")]


def b_erros(c, t, C, B):
    K.erro_cards(c, t, C, ["19", "20", "21"], ERROS)


# ======================================================================
# questões
# ======================================================================

def _questao(c, t, C, ids, titulo, sub, col, alts, ok_letra, enun, pausa=False, rodape=True):
    """layout padrão: enunciado à esquerda (até a cena da resolução), alternativas à direita."""
    s1, s2, s3 = ids
    head(c, t, B_start(C, s1), titulo, sub, col)
    card(c, *CARD_R)
    a0 = ep(t, C[f"{s1}.a"], 0.4)
    cues_in = {L: C[f"{s1}.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"{s3}.x{L.lower()}"] for L in "ABCDE" if L != ok_letra}
    K.alternativas(c, t, C, alts, 1000, 260, 680, 38, C[f"{s2}.ok"], ok_letra, cues_in, cues_x, gap=40)
    if rodape:
        text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY,
             a0 * (1 - ep(t, C[s2], 0.3)), align="left")
    if t < C[s2]:
        enun(c, a0)
        if pausa:
            pause_timer(c, t, C[f"{s1}.end"] - 1.9, 540, 720)
        return False
    rrect(c, 170, 206, 740, 624, 18, "#FFFFFF", ep(t, C[s2], 0.4), shadow=True)
    return True


def B_start(C, sid):
    return C[sid]


ALTS5 = [("A", "0,4", "inverteu a fração (2/5)", RED), ("B", "2", "parou na última semana inteira", RED),
         ("C", "2,5", "", GREEN), ("D", "8", "dividiu 32 por 4", RED), ("E", "28", "subtraiu 4 de 32", RED)]


def b_q5(c, t, C, B):
    def enun(c, a0):
        y = _enunciado(c, [("A área ocupada por uma colônia de fungos em uma placa de cultura quadruplica a cada semana, "
                            "segundo o modelo", INK)], a0, 236)
        text(c, "A(t) = A₀ · 4ᵗ", 540, y + 30, 46, "black", PURPLE, a0)
        _enunciado(c, [("com t em semanas. O tempo para que a área fique 32 vezes maior que a inicial, em semanas, é",
                        INK)], a0, y + 110)
    if not _questao(c, t, C, ("22", "23", "24"), "QUESTÃO 5 · EU FAÇO", "OS FUNGOS QUE QUADRUPLICAM", BLUE, ALTS5, "C",
                    enun):
        return
    y0 = 206
    a1 = ep(t, C["23"], 0.4)
    if a1 > 0:
        pill(c, "ESTIME: 4² = 16 < 32 < 64 = 4³", 540, y0 + 55, GREEN, size=24, a=a1, anchor="center",
             bounds=(170, 910))
    aa = ep(t, C["23.a"], 0.4)
    if aa > 0:
        pill(c, "CAMINHO 1 · mudança de base", 540, y0 + 140, PURPLE, size=22, a=aa, anchor="center", bounds=(170, 910))
        eq(c, [("t", "t = ", AMBER), ("f", "log₂ 32", "log₂ 4", INK, AMBER), ("t", " = ", INK),
               ("f", "5", "2", INK, AMBER)], 540, y0 + 250, 42, aa)
    ab = ep(t, C["23.b"], 0.4)
    if ab > 0:
        pill(c, "CAMINHO 2 · mesma base", 540, y0 + 360, PURPLE, size=22, a=ab, anchor="center", bounds=(170, 910))
        mx(c, "2^{2t} = 2^5", 540, y0 + 440, 46, ab, INK)
        caixa(c, 390, y0 + 500, 300, 90, GREEN, ab)
        text_mid(c, "t = 2,5", 540, y0 + 545, 40, "black", GREEN, ab)


ALTS6 = [("A", "0,28", "inverteu a divisão", RED), ("B", "1,22", "subtraiu os logs", RED), ("C", "3,54", "", GREEN),
         ("D", "16,7", "50 ÷ 3: linear", RED), ("E", "104", "50 ÷ log 3, sem log de 50", RED)]


def b_q6(c, t, C, B):
    def enun(c, a0):
        y = _enunciado(c, [("Uma cultura de bactérias tem população modelada por", INK)], a0, 236)
        text(c, "N(t) = 1 000 · 3ᵗ", 540, y + 30, 46, "black", PURPLE, a0)
        y = _enunciado(c, [("com t em horas. Use log 2 = 0,30 e log 3 = 0,48. O tempo, em horas, para que a população "
                            "atinja 50 000 bactérias é aproximadamente", INK)], a0, y + 110)
        ap = ep(t, C["25.p"], 0.4)
        if ap > 0:
            pill(c, "qual é o primeiro passo?", 540, y + 40, GREEN, size=26, a=ap, anchor="center", bounds=(170, 910))
    if not _questao(c, t, C, ("25", "26", "27"), "QUESTÃO 6 · NÓS FAZEMOS", "AS BACTÉRIAS", GREEN, ALTS6, "C", enun):
        return
    y0 = 206
    a1 = ep(t, C["26"], 0.4)
    if a1 > 0:
        pill(c, "ISOLE: divida por 1 000", 540, y0 + 50, AMBER, size=24, a=a1, anchor="center", bounds=(170, 910))
        text_mid(c, "3ᵗ = 50", 540, y0 + 125, 50, "black", INK, a1)
        text(c, "estime: 27 < 50 < 81 → entre 3 e 4", 540, y0 + 200, 24, "bold", GREEN, ep(t, C["26"] + 2.0, 0.4))
    aa = ep(t, C["26.a"], 0.4)
    if aa > 0:
        linha(c, [("log 50 = log (100/2) = 2 − 0,30 = ", INK), ("1,70", PURPLE)], 540, y0 + 290, 28, aa)
    ab = ep(t, C["26.b"], 0.4)
    if ab > 0:
        eq(c, [("t", "t = ", AMBER), ("f", "log 50", "log 3", INK, INK), ("t", " = ", INK),
               ("f", "1,70", "0,48", INK, INK)], 540, y0 + 420, 42, ab)
        caixa(c, 390, y0 + 500, 300, 90, GREEN, ab)
        text_mid(c, "≈ 3,54 h", 540, y0 + 545, 40, "black", GREEN, ab)


ALTS1 = [("A", "0,11", "inverteu a divisão", RED), ("B", "0,27", "subtraiu os logs", RED), ("C", "9", "", GREEN),
         ("D", "12,5", "juros simples (100 ÷ 8)", RED), ("E", "25", "2 ÷ 0,08, sem log", RED)]


def b_q1(c, t, C, B):
    def enun(c, a0):
        _enunciado(c, [("Um investidor aplicou um capital a juros compostos de 8% ao ano. Para estimar em quanto tempo o "
                        "capital dobra, ele usou as aproximações log 2 = 0,30 e log 1,08 = 0,033. O tempo encontrado, "
                        "em anos, foi aproximadamente", INK)], a0, 236)
    if not _questao(c, t, C, ("28", "29", "30"), "QUESTÃO 1 · VOCÊ FAZ", "O CAPITAL A 8% AO ANO", GREEN, ALTS1, "C",
                    enun, pausa=True):
        return
    y0 = 206
    aa = ep(t, C["29.a"], 0.4)
    if aa > 0:
        elevador(c, t, C["29.a"] + 1.4, "1,08", "2", "t", 540, y0 + 90, 50, dur=2.6, a=aa)
    ab = ep(t, C["29.b"], 0.4)
    if ab > 0:
        eq(c, [("t", "t = ", AMBER), ("f", "log 2", "log 1,08", INK, INK), ("t", " = ", INK),
               ("f", "0,30", "0,033", INK, INK)], 540, y0 + 250, 42, ab)
        caixa(c, 390, y0 + 340, 300, 90, GREEN, ab)
        text_mid(c, "≈ 9,1 anos", 540, y0 + 385, 38, "black", GREEN, ab)
    acc = ep(t, C["29.c"], 0.4)
    if acc > 0:
        rrect(c, 230, y0 + 470, 620, 110, 20, mix("#FFFFFF", GREEN, 0.12), acc)
        text(c, "REGRA DO 72", 540, y0 + 510, 22, "black", GREEN, acc)
        text(c, "72 ÷ 8 = 9 ✓", 540, y0 + 556, 34, "black", INK, acc)


ALTS8 = [("A", "0,15 ano", "inverteu a divisão", RED), ("B", "0,32 ano", "log 9 no lugar de log 0,9 (e sem sinal)", RED),
         ("C", "5 anos", "perda linear (50% ÷ 10%)", RED), ("D", "6,5 anos", "", GREEN),
         ("E", "10 anos", "metade = perder tudo (linear)", RED)]


def b_q8(c, t, C, B):
    def enun(c, a0):
        _enunciado(c, [("Um equipamento perde 10% de seu valor a cada ano, sempre em relação ao valor do ano anterior. "
                        "Considere log 2 = 0,301 e log 3 = 0,477. O tempo necessário para que o equipamento valha a "
                        "metade do preço de compra é de aproximadamente", INK)], a0, 236)
    if not _questao(c, t, C, ("31", "32", "33"), "QUESTÃO 8 · VOCÊ FAZ", "O EQUIPAMENTO QUE DESVALORIZA", RED, ALTS8,
                    "D", enun, pausa=True):
        return
    y0 = 206
    aa = ep(t, C["32.a"], 0.4)
    if aa > 0:
        pill(c, "fator 0,9 (menor que 1)", 540, y0 + 45, RED, size=22, a=aa, anchor="center", bounds=(170, 910))
        text_mid(c, "0,9ᵗ = 0,5", 540, y0 + 115, 50, "black", INK, aa)
    ab = ep(t, C["32.b"], 0.4)
    if ab > 0:
        linha(c, [("log 0,9 = 2 · 0,477 − 1 = ", INK), ("−0,046", RED)], 540, y0 + 205, 30, ab)
        linha(c, [("log 0,5 = ", INK), ("−0,301", RED)], 540, y0 + 265, 30, ep(t, C["32.b"] + 3.4, 0.4))
    acc = ep(t, C["32.c"], 0.4)
    if acc > 0:
        eq(c, [("t", "t = ", AMBER), ("f", "−0,301", "−0,046", RED, RED)], 540, y0 + 390, 46, acc)
        caixa(c, 390, y0 + 480, 300, 90, GREEN, acc)
        text_mid(c, "≈ 6,5 anos", 540, y0 + 525, 38, "black", GREEN, acc)
        pill(c, "dois negativos → tempo positivo", 540, y0 + 600, GREEN, size=20, a=acc, anchor="center",
             bounds=(170, 910))


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "EQUAÇÕES LOGARÍTMICAS", PURPLE)
    aa = ep(t, C["35.a"], 0.5)
    if aa > 0:
        rrect(c, 260, 240, 1400, 170, 26, "#FFFFFF", aa, shadow=True)
        text_mid(c, "log₂ x + log₂ (x − 2) = 3", W / 2, 325, 70, "black", INK, aa)
    ab = ep(t, C["35.b"], 0.5)
    if ab > 0:
        for k, s_ in enumerate(("raiz 1", "raiz 2")):
            x = 760 + k * 400
            rrect(c, x - 150, 480, 300, 120, 22, mix("#FFFFFF", AMBER, 0.14), ab)
            text_mid(c, s_ + " = ?", x, 540, 40, "black", AMBER, ab)
        selo(c, 1500, 470, ab, "SÓ UMA VALE", RED, -6, 28)
    acc = ep(t, C["35.c"], 0.5)
    if acc > 0:
        regra(c, "QUAL, E POR QUÊ?", W / 2, 700, acc, 44, PURPLE)
    ad = ep(t, C["35.d"], 0.5)
    if ad > 0:
        pill(c, "ep. 4 · equações logarítmicas e a condição de existência", W / 2, 800, PURPLE, size=26, a=ad,
             anchor="center")


def b_cta(c, t, C, B):
    cta(c, t, C["36.like"], C["36.sub"], C["36.bell"], C["36.com"], C["36.bye"],
        "Qual dos três erros clássicos você já cometeu?", canal="no Estudativo", anki=C["36.anki"])


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, concreto=b_concreto, elev1=b_elev1, grafico=b_grafico,
              atalho_est=b_atalho_est, porao=b_porao, porao2=b_porao2, emcima=b_emcima, elev2=b_elev2,
              formula=b_formula, isolar=b_isolar, decai=b_decai, atalho_sinal=b_atalho_sinal, exercicio=b_exercicio,
              recap=b_recap, erros=b_erros, q5=b_q5, q6=b_q6, q1=b_q1, q8=b_q8, ponte=b_ponte, cta=b_cta)
