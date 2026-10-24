"""Visual — Função Exponencial, Episódio 3: duplicação e meia-vida, conte os intervalos (tema claro).
Peças comuns da série em ../../comum.py (reexporta o 019/comum.py: expr com potências e frações, alternativas, erro_cards,
atalho, selo, regra...).
Peças deste episódio: relogio() (o relógio que "apita" a cada intervalo, com o contador de apitos), barras() (as barras da
meia-vida, 100% → 50% → 25% → 12,5%), pizza() (a pizza que SOBROU, cortada pela metade a cada meia-vida), cortes() (o
denominador dividido por 2 até chegar a 1), cadeia() (fichas com setas ×2 ou ÷2), Plano (eixos + curva), linha().
Cores com função: azul = definição · roxo = regra / fórmula · âmbar = armadilha · verde = atalho · vermelho = erro.
"""
import importlib.util
import math
from pathlib import Path
import skia
import motor
motor.set_theme("claro")
from motor import *  # noqa
from aula import *  # noqa

_p = Path(__file__).resolve().parents[2] / "comum.py"
_s = importlib.util.spec_from_file_location("comum041", _p)
K = importlib.util.module_from_spec(_s); _s.loader.exec_module(K)
K.usar_tempos(Path(__file__).resolve().parents[1] / "audio" / "tempos.json")
motor.set_theme("claro")
frame, head_seq, which, para, regra, selo, pause_timer, chip = (K.frame, K.head_seq, K.which, K.para, K.regra, K.selo,
                                                                K.pause_timer, K.chip)
ftext, ftext_w = K.ftext, K.ftext_w

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_exponencial_ep3_duplicacao_meia_vida.mp4"
CARD_R = K.CARD_R
GRADE = "#EEEEEA"


# ======================================================================
# peças do episódio
# ======================================================================

def linha(c, partes, cx, cy, size, a, peso="black", align="center"):
    """texto numa linha, com cor por trecho: partes = [(texto, cor)] (mantém espaços)"""
    if a <= 0:
        return 0
    ws = [ftext_w(s_, peso, size) for s_, _ in partes]
    x = cx - sum(ws) / 2 if align == "center" else cx
    for (s_, col), w_ in zip(partes, ws):
        ftext(c, s_, x, cy + size * 0.36, size, peso, col or INK, a, align="left")
        x += w_
    return sum(ws)


def mx(c, s, cx, cy, size, a, col=None, align="center"):
    """expressão matemática de uma cor só (potências, frações)"""
    n = len(s.split())
    return K.expr(c, s, cx, cy, size, a, cores={i: col or INK for i in range(n)}, align=align)


def defin(c, termo, s, x, y, w, a, col=None, size=28):
    """faixa de definição: TERMO: frase"""
    if a <= 0:
        return
    col = col or BLUE
    rrect(c, x, y, w, 70, 18, mix("#FFFFFF", col, 0.12), a)
    linha(c, [(termo, col), (": " + s, INK)], x + 28, y + 35, size, a, align="left")


def ease_out(u):
    return 1 - (1 - clamp(u)) ** 3


def relogio(c, cx, cy, r, a, n_float, col=PURPLE, total=None, rot_="apitos"):
    """relógio: o ponteiro dá uma volta por intervalo; a cada volta completa o contador sobe (apito).
    n_float = quantos intervalos já passaram (fracionário)."""
    if a <= 0:
        return
    n_float = max(0.0, n_float)
    raw = n_float
    if total is not None:
        n_float = min(n_float, total)
    n = int(n_float + 1e-6)
    frac = n_float - n
    c.drawCircle(cx, cy, r + 10, paint("#FFFFFF", a))
    c.drawCircle(cx, cy, r + 10, paint(INK2, a, stroke=6))
    for k in range(12):
        ang = k * math.pi / 6
        r0 = r - (22 if k % 3 == 0 else 12)
        line(c, cx + r0 * math.sin(ang), cy - r0 * math.cos(ang), cx + (r - 2) * math.sin(ang),
             cy - (r - 2) * math.cos(ang), GRAY, a, 4 if k % 3 == 0 else 2)
    # setor já percorrido no intervalo atual
    if frac > 0.001:
        rect = skia.Rect.MakeXYWH(cx - r + 6, cy - r + 6, 2 * r - 12, 2 * r - 12)
        c.drawArc(rect, -90, 360 * frac, True, paint(col, a * 0.16))
    ang = 2 * math.pi * frac
    line(c, cx, cy, cx + (r - 30) * math.sin(ang), cy - (r - 30) * math.cos(ang), col, a, 8)
    c.drawCircle(cx, cy, 12, paint(col, a))
    # apito: anel que pulsa logo depois de cada volta
    if n >= 1 and raw - n < 0.35:
        u = (raw - n) / 0.35
        c.drawCircle(cx, cy, r + 18 + 50 * u, paint(AMBER, a * (1 - u), stroke=8))
        text(c, "APITO!", cx, cy - r - 40 - 30 * u, 30, "black", AMBER, a * (1 - u))
    badge_num(c, n, cx + r * 0.85, cy + r * 0.85, a, 34, bg=col)
    if rot_:
        text(c, rot_, cx + r * 0.85, cy + r * 0.85 + 70, 22, "black", col, a)


def barras(c, x, base, a, n_float, w=150, gap=60, hmax=420, col=PURPLE, rot=True, ncol=4):
    """barras da meia-vida: 100% → 50% → 25% → 12,5% (n_float = quantas barras já apareceram)"""
    if a <= 0:
        return
    line(c, x - 20, base, x + ncol * (w + gap) - gap + 20, base, INK2, a, 4)
    for k in range(ncol):
        u = clamp(n_float - k)
        if u <= 0:
            break
        h = hmax / 2 ** k * ease_out(u)
        xx = x + k * (w + gap)
        rrect(c, xx, base - h, w, h, 12, mix("#FFFFFF", col, 0.55 - 0.08 * k), a)
        v = f"{100 / 2 ** k:g}".replace(".", ",") + "%"
        text(c, v, xx + w / 2, base - h - 18, 34, "black", col, a * u)
        if rot and k > 0:
            text(c, "÷2", xx - gap / 2, base - hmax / 2 ** k - 70, 24, "black", GRAY, a * u)


def pizza(c, cx, cy, r, a, n_float, col=AMBER):
    """pizza que SOBROU: depois de n cortes resta 1/2ⁿ (fatia colorida); o pedaço que sai fica tracejado"""
    if a <= 0:
        return
    n = int(n_float + 1e-6)
    frac = n_float - n
    rect = skia.Rect.MakeXYWH(cx - r, cy - r, 2 * r, 2 * r)
    c.drawCircle(cx, cy, r, paint(LIGHT, a * 0.5, stroke=4))
    resto = 1 / 2 ** n
    # a parte que está saindo (metade do que sobrou), some durante o corte
    if frac > 0:
        c.drawArc(rect, -90, 360 * resto, True, paint(mix("#FFFFFF", col, 0.30), a * (1 - frac)))
    novo = resto / 2 if frac > 0 else resto
    c.drawArc(rect, -90, 360 * novo, True, paint(mix("#FFFFFF", col, 0.65), a))
    c.drawArc(rect, -90, 360 * novo, True, paint(col, a, stroke=4))
    if frac > 0:
        ang = math.radians(-90 + 360 * novo)
        line(c, cx, cy, cx + r * math.cos(ang), cy + r * math.sin(ang), RED, a, 5)


def cadeia(c, vals, x, y, a_list, op="×2", col=PURPLE, w=170, gap=70, size=40):
    """fichas lado a lado com setas e o rótulo da operação entre elas; a_list = alfa de cada ficha"""
    for k, v in enumerate(vals):
        ak = a_list[k]
        if ak <= 0:
            continue
        xx = x + k * (w + gap)
        chip(c, v, xx + w / 2, y, col, ak, size=size, w=w)
        if k > 0:
            arrow(c, xx - gap + 8, y, xx - 8, y, GRAY, ak, 4, 12)
            text(c, op, xx - gap / 2, y - 40, 24, "black", GRAY, ak)


class Plano:
    """plano cartesiano num retângulo (x0, y0, w, h) com faixas xr, yr próprias."""

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
        for v in xt:
            if v:
                text(c, f"{v:g}", s.px(v), oy + size + 10, size, "bold", INK2, a)
        for v in yt:
            if v:
                text(c, f"{v:g}", ox - 12, s.py(v) + size * 0.36, size, "bold", INK2, a, align="right")

    def curva(s, c, a, f, col, u=1.0, width=7, n=160):
        if a <= 0 or u <= 0:
            return
        xa, xb = s.xr[0], s.xr[0] + (s.xr[1] - s.xr[0]) * clamp(u)
        c.save()
        c.clipRect(skia.Rect.MakeXYWH(s.x0, s.y0 - 4, s.w, s.h + 8))
        path = skia.Path()
        for k in range(n + 1):
            x = xa + (xb - xa) * k / n
            (path.moveTo if k == 0 else path.lineTo)(s.px(x), s.py(f(x)))
        c.drawPath(path, paint(col, a, stroke=width, cap_round=True))
        c.restore()


def caixa(c, x, y, w, h, a, col=None, alpha=0.10, shadow=False):
    if a <= 0:
        return
    if col:
        rrect(c, x, y, w, h, 22, mix("#FFFFFF", col, alpha), a)
    else:
        rrect(c, x, y, w, h, 22, "#FFFFFF", a, shadow=shadow)


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "FUNÇÃO EXPONENCIAL · EPISÓDIO 3", PURPLE)
    aa = ep(t, C["01.a"], 0.5)
    n = 1.0
    if t >= C["01.b"]:
        n = 1 + clamp((t - C["01.b"]) / 1.2) * 2
    if t >= C["01.d"]:
        n = 3 + clamp((t - C["01.d"]) / 0.8)
    barras(c, 260, 820, aa, n, w=170, gap=80, hmax=520, rot=False)
    if aa > 0:
        for k, s_ in enumerate(("hoje", "30 anos", "60 anos", "90 anos")):
            text(c, s_, 260 + k * 250 + 85, 870, 26, "bold", GRAY, aa * clamp(n - k))
        caixa(c, 1300, 250, 420, 130, aa, PURPLE)
        text(c, "perde METADE", 1510, 305, 36, "black", PURPLE, aa)
        text(c, "a cada 30 anos", 1510, 352, 28, "bold", INK2, aa)
    ab = ep(t, C["01.b"], 0.5)
    if ab > 0 and t < C["01.c"] + 0.4:
        selo(c, 1510, 500, ab, "60 ANOS: ACABOU?", AMBER, -5, 34)
    acc = ep(t, C["01.c"], 0.5)
    if acc > 0:
        caixa(c, 1300, 440, 420, 120, acc, GREEN)
        mx(c, "resta 1/4", 1510, 500, 48, acc, GREEN)
    ad = ep(t, C["01.d"], 0.5)
    if ad > 0:
        caixa(c, 1300, 590, 420, 120, ad, GREEN)
        mx(c, "90 anos: 1/8", 1510, 650, 48, ad, GREEN)
    ae = ep(t, C["01.e"], 0.5)
    if ae > 0:
        regra(c, "NUNCA CHEGA A ZERO", 1510, 790, ae, 40, RED)


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "FUNÇÃO EXPONENCIAL · EP. 3", "AO FINAL DESTA AULA", GREEN)
    a0 = ep(t, C["02"], 0.4)
    if a0 > 0:
        pill(c, "3º episódio da série de FUNÇÃO EXPONENCIAL", W / 2, 240, PURPLE, size=30, a=a0, anchor="center")
    itens = [("02.a", "DOBRA A CADA", "bactérias, dinheiro", BLUE), ("02.b", "MEIA-VIDA", "remédio, radioatividade", PURPLE),
             ("02.c", "CONTE OS INTERVALOS", "sem fórmula decorada", GREEN)]
    for k, (cue, tit, sub, col) in enumerate(itens):
        ak = ep(t, C[cue], 0.5)
        if ak <= 0:
            continue
        x = 440 + k * 520
        rrect(c, x - 230, 330, 460, 330, 26, "#FFFFFF", ak, shadow=True)
        rrect(c, x - 230, 330, 460, 70, 26, col, ak * 0.16)
        badge_num(c, k + 1, x, 470, ak, 34, bg=col)
        text(c, tit, x, 570, 36 if len(tit) > 14 else 40, "black", col, ak)
        text(c, sub, x, 625, 28, "bold", INK2, ak)


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "TRÊS LEMBRETES", "EM 30 SEGUNDOS", GREEN)
    aa = ep(t, C["03.a"], 0.5)
    if aa > 0:
        pill(c, "episódio 2", 260, 240, BLUE, size=22, a=aa, bounds=(0, 1920))
        caixa(c, 240, 280, 1440, 200, aa, shadow=True)
        K.expr(c, "Q(t) = Q₀ · a^t", 700, 380, 80, aa, cores={2: BLUE, 4: PURPLE})
        text(c, "Q₀ = valor do começo", 1300, 360, 30, "black", BLUE, aa)
        text(c, "a = fator", 1300, 420, 30, "black", PURPLE, aa)
    ab = ep(t, C["03.b"], 0.5)
    if ab > 0:
        pill(c, "série de Potenciação", 260, 530, BLUE, size=22, a=ab, bounds=(0, 1920))
        caixa(c, 240, 570, 680, 220, ab, shadow=True)
        K.expr(c, "2^6 = 64", 580, 690, 80, ab, cores={0: PURPLE, 2: GREEN})
    acc = ep(t, C["03.c"], 0.5)
    if acc > 0:
        caixa(c, 1000, 570, 680, 220, acc, shadow=True)
        K.expr(c, "(1/2)^4 = 1/16", 1340, 680, 70, acc, cores={0: PURPLE, 2: GREEN})


def b_concreto(c, t, C, B):
    head(c, t, B["start"], "TRÊS CENAS REAIS", "O QUE ELAS TÊM EM COMUM?", BLUE)
    card(c, *CARD_R)
    itens = [("04.a", "BACTÉRIAS", "dobram de tempos em tempos", "×2", GREEN),
             ("04.b", "REMÉDIO", "sai do sangue, metade de cada vez", "÷2", BLUE),
             ("04.c", "CÉSIO-137", "Goiânia, 1987", "÷2", RED)]
    for k, (cue, tit, sub, op, col) in enumerate(itens):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        x = 220 + k * 500
        rrect(c, x, 220 + d, 460, 480, 26, "#FFFFFF", a, shadow=True)
        rrect(c, x, 220 + d, 460, 90, 26, col, a * 0.16)
        text(c, tit, x + 230, 282 + d, 40, "black", col, a)
        text_mid(c, op, x + 230, 470 + d, 150, "black", col, a)
        for j, ln in enumerate(K.wrap(sub, "bold", 28, 400)):
            text(c, ln, x + 230, 630 + d + j * 38, 28, "bold", INK2, a)
    ad = ep(t, C["04.d"], 0.5)
    if ad > 0:
        regra(c, "A MESMA CONTA", W / 2, 790, ad, 40, PURPLE)


# ======================================================================
# bloco a — duplicação · bloco b — bactérias · atalho
# ======================================================================

def b_duplicacao(c, t, C, B):
    head(c, t, B["start"], "DOBRA A CADA T", "O TEMPO DE DUPLICAÇÃO", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["05.a"], 0.5)
    if aa > 0:
        defin(c, "TEMPO DE DUPLICAÇÃO (T)", "o tempo para a quantidade dobrar", 220, 210, 1480, aa, BLUE, 30)
    ab = ep(t, C["05.b"], 0.5)
    if ab > 0:
        caixa(c, 220, 320, 900, 220, ab, PURPLE, 0.08)
        K.expr(c, "Q(t) = Q₀ · 2^{t/T}", 670, 440, 86, ab, cores={2: BLUE, 4: PURPLE})
    acc = ep(t, C["05.c"], 0.5)
    if acc > 0:
        pill(c, "t/T = CONTADOR DE APITOS", 670, 590, PURPLE, size=30, a=acc, anchor="center")
        n = 0.0
        if t >= C["05.d"]:
            n = (t - C["05.d"]) / 1.1
        relogio(c, 1440, 470, 170, acc, n, total=3)
    ad = ep(t, C["05.d"], 0.5)
    if ad > 0:
        caixa(c, 220, 660, 900, 140, ad, GREEN)
        linha(c, [("T = 30 min · passaram 90 min → ", INK), ("3 apitos", GREEN)], 670, 730, 36, ad)


def b_bacterias(c, t, C, B):
    head(c, t, B["start"], "1 000 BACTÉRIAS", "DOBRAM A CADA 30 MIN · 3 h DEPOIS?", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["06.a"], 0.5)
    if aa > 0:
        caixa(c, 200, 210, 760, 110, aa, BLUE)
        linha(c, [("1º  ", BLUE), ("3 h = ", INK), ("180 min", BLUE)], 580, 265, 44, aa)
    ab = ep(t, C["06.b"], 0.5)
    if ab > 0:
        caixa(c, 200, 340, 760, 110, ab, PURPLE)
        linha(c, [("2º  ", PURPLE), ("180 ÷ 30 = ", INK), ("6 apitos", PURPLE)], 580, 395, 44, ab)
    acc = ep(t, C["06.c"], 0.5)
    n = (t - C["06.c"]) / 1.25 if t >= C["06.c"] else 0.0
    relogio(c, 1420, 420, 160, max(ab, acc), n, total=6)
    if acc > 0:
        k = int(min(6, max(0.0, n) + 1e-6))
        pop = 1000 * 2 ** k
        caixa(c, 1150, 660, 540, 130, acc, GREEN)
        text(c, f"{pop:,}".replace(",", " ") + " bactérias", 1420, 742, 50, "black", GREEN, acc)
        vals = ["1 000"] + [f"{1000 * 2 ** j:,}".replace(",", " ") for j in range(1, 7)]
        for j in range(7):
            aj = acc * (1.0 if j <= k else 0.0)
            if aj <= 0:
                continue
            xx, yy = 230 + (j % 4) * 180, 490 + (j // 4) * 80
            chip(c, vals[j], xx + 75, yy, GREEN if j == 6 else INK2, aj, size=28, w=160)
    ad = ep(t, C["06.d"], 0.5)
    if ad > 0:
        caixa(c, 200, 720, 900, 110, ad, PURPLE, 0.10)
        K.expr(c, "1 000 · 2^6 = 1 000 · 64", 650, 775, 46, ad, cores={2: PURPLE})
    ae = ep(t, C["06.e"], 0.5)
    if ae > 0:
        selo(c, 580, 668, ae, "6 INTERVALOS → ×64", PURPLE, -3, 28)


def b_atalho_dup(c, t, C, B):
    head(c, t, B["start"], "ATALHO", "QUALQUER “DOBRA A CADA”", GREEN)
    card(c, *CARD_R)
    a0 = ep(t, C["07"], 0.4)
    K.atalho(c, 240, 200, 1440, 130, "ATALHO", ["converta · divida · conte os apitos"], a0, 40)
    passos = [("07.a", "1", "CONVERTA", "mesma unidade do intervalo"), ("07.b", "2", "DIVIDA", "tempo ÷ intervalo = apitos"),
              ("07.c", "3", "DOBRE", "um apito de cada vez")]
    for k, (cue, nn, tit, sub) in enumerate(passos):
        ak = ep(t, C[cue], 0.5)
        if ak <= 0:
            continue
        x = 240 + k * 490
        caixa(c, x, 370, 460, 180, ak, shadow=True)
        badge_num(c, nn, x + 60, 460, ak, 30, bg=GREEN)
        text(c, tit, x + 270, 445, 40, "black", GREEN, ak)
        text(c, sub, x + 270, 500, 24, "bold", INK2, ak)
    acc = ep(t, C["07.c"], 0.5)
    vals = ["2", "4", "8", "16", "32", "64"]
    cadeia(c, vals, 330, 650, [ep(t, C["07.c"] + 2.0 + 0.45 * j, 0.3) for j in range(6)], "×2", GREEN, w=140, gap=70)
    ad = ep(t, C["07.d"], 0.5)
    if ad > 0:
        regra(c, "6 APITOS = × 64", W / 2, 790, ad, 40, GREEN)


# ======================================================================
# bloco c — meia-vida · bloco d — césio · bloco e — barras e pizza
# ======================================================================

def b_meiavida(c, t, C, B):
    head(c, t, B["start"], "O CAMINHO CONTRÁRIO", "A MEIA-VIDA", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["08.a"], 0.5)
    if aa > 0:
        defin(c, "ISÓTOPO RADIOATIVO", "versão instável de um elemento", 220, 210, 1480, aa, BLUE, 28)
        aa2 = ep(t, C["08.a"] + 3.4, 0.4)
        defin(c, "DECAIMENTO", "o desfazer sozinho do isótopo", 220, 295, 1480, aa2, BLUE, 28)
    ab = ep(t, C["08.b"], 0.5)
    if ab > 0:
        defin(c, "MEIA-VIDA (T)", "o tempo para restar METADE", 220, 380, 1480, ab, PURPLE, 30)
    acc = ep(t, C["08.c"], 0.5)
    if acc > 0:
        caixa(c, 220, 490, 1000, 220, acc, PURPLE, 0.08)
        K.expr(c, "Q(t) = Q₀ · (1/2)^{t/T}", 720, 600, 80, acc, cores={2: BLUE, 4: PURPLE})
        pill(c, "remédio: 1 meia-vida → metade da dose", 1460, 560, BLUE, size=24, a=ep(t, C["08.c"] + 2.0, 0.4),
             anchor="center", bounds=(1230, 1700))
        pill(c, "o mesmo contador, agora ÷ 2", 720, 760, PURPLE, size=28, a=ep(t, C["08.c"] + 5.5, 0.4), anchor="center")


def b_cesio(c, t, C, B):
    head(c, t, B["start"], "CÉSIO-137", "MEIA-VIDA ≈ 30 ANOS · E EM 90 ANOS?", RED)
    card(c, *CARD_R)
    aa = ep(t, C["09.a"], 0.5)
    if aa > 0:
        caixa(c, 200, 220, 860, 120, aa, PURPLE)
        linha(c, [("90 anos ÷ 30 anos = ", INK), ("3 meias-vidas", PURPLE)], 630, 280, 42, aa)
    n = (t - C["09.a"]) / 1.0 if t >= C["09.a"] else 0
    relogio(c, 1450, 400, 150, aa, n, col=RED, total=3, rot_="meias-vidas")
    ab = ep(t, C["09.b"], 0.5)
    if ab > 0:
        caixa(c, 200, 370, 860, 170, ab, PURPLE, 0.08)
        K.expr(c, "(1/2)^3 = 1/8", 630, 455, 76, ab, cores={0: PURPLE, 2: GREEN})
    acc = ep(t, C["09.c"], 0.5)
    if acc > 0:
        pizza(c, 630, 690, 110, acc, 3)
        text(c, "resta 1/8", 830, 680, 40, "black", AMBER, acc, align="left")
        text(c, "pouco, mas NÃO é zero", 830, 730, 28, "black", RED, acc, align="left")
    ad = ep(t, C["09.d"], 0.5)
    if ad > 0:
        caixa(c, 1210, 640, 480, 140, ad, GREEN)
        mx(c, "60 anos: 2 → 1/4", 1450, 710, 44, ad, GREEN)


def b_barras(c, t, C, B):
    head(c, t, B["start"], "POR QUE NUNCA ZERA?", "METADE DO QUE SOBROU", PURPLE)
    card(c, *CARD_R)
    marcos = [C["10.a"], C["10.b"], C["10.c"], C["10.c"] + 3.6]
    n = sum(ep(t, m, 0.6) for m in marcos)
    sid_f = t >= C["10.f"]
    if not sid_f:
        barras(c, 240, 800, ep(t, C["10.a"], 0.4), n, w=150, gap=60, hmax=500)
    ad = ep(t, C["10.d"], 0.5)
    if ad > 0 and not sid_f:
        cortes_n = clamp((t - C["10.d"]) / 3.0) * 3
        pizza(c, 1420, 470, 210, ad, cortes_n)
        text(c, "a pizza que SOBROU", 1420, 740, 34, "black", AMBER, ad)
    ae = ep(t, C["10.e"], 0.5)
    if ae > 0 and not sid_f:
        regra(c, "METADE DE UM PEDAÇO AINDA É UM PEDAÇO", W / 2, 860, ae, 32, GREEN)
    af = ep(t, C["10.f"], 0.5)
    if af > 0:
        P = Plano(300, 230, 1100, 520, (0, 7), (0, 110))
        P.eixos(c, af, xt=range(1, 8), yt=(25, 50, 100), rot=("meias-vidas", "%"))
        P.curva(c, af, lambda x: 100 * 0.5 ** x, PURPLE, u=ep(t, C["10.f"], 1.6))
        rrect(c, P.x0, P.py(0) - 9, P.w, 18, 9, AMBER, af * 0.16)
        line(c, P.x0, P.py(0), P.x0 + P.w, P.py(0), AMBER, af, 4, dash=(16, 10))
        pill(c, "parede invisível · episódio 1", P.x0 + P.w - 10, P.py(0) - 40, AMBER, size=22, a=af, anchor="right",
             bounds=(0, 1920))
        selo(c, 1580, 300, af, "GRUDA, SEM TOCAR", AMBER, 5, 28)


# ======================================================================
# bloco f — caminho inverso · atalho · bloco g — PG
# ======================================================================

def b_inverso(c, t, C, B):
    head(c, t, B["start"], "O CAMINHO INVERSO", "DERAM A FRAÇÃO · PEDEM O TEMPO", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["11"], 0.4)
    if a0 > 0:
        pill(c, "césio-137 · meia-vida ≈ 30 anos", W / 2, 230, RED, size=28, a=a0, anchor="center")
    for k, (cue_a, cue_b, fr, pot, nmv, conta, res) in enumerate(
            (("11.a", "11.b", "1/8", "(1/2)^3", "3 meias-vidas", "3 · 30 anos", "90 anos"),
             ("11.c", "11.c", "1/16", "(1/2)^4", "4 meias-vidas", "4 · 30 anos", "120 anos"))):
        aa = ep(t, C[cue_a], 0.5)
        if aa <= 0:
            continue
        y = 300 + k * 260
        caixa(c, 200, y, 1520, 220, aa, shadow=True)
        text(c, "resta", 290, y + 120, 30, "bold", INK2, aa)
        mx(c, fr, 420, y + 110, 70, aa, AMBER)
        arrow(c, 500, y + 110, 570, y + 110, GRAY, aa, 4, 12)
        mx(c, pot, 700, y + 110, 64, aa, PURPLE)
        text(c, nmv, 700, y + 195, 26, "black", PURPLE, aa)
        ab = ep(t, C[cue_b] + (0 if k == 0 else 3.0), 0.5)
        if ab > 0:
            arrow(c, 860, y + 110, 930, y + 110, GRAY, ab, 4, 12)
            text(c, conta, 1110, y + 125, 44, "black", INK, ab)
            arrow(c, 1300, y + 110, 1370, y + 110, GRAY, ab, 4, 12)
            chip(c, res, 1530, y + 110, GREEN, ab, size=42, w=280)


def cortes(c, cx, y, a, n_float, den=16):
    """o denominador dividido por 2 até chegar a 1, com o contador de cortes"""
    if a <= 0:
        return
    vals = []
    v = den
    while v >= 1:
        vals.append(v)
        v //= 2
    w, gap = 170, 90
    x0 = cx - (len(vals) * w + (len(vals) - 1) * gap) / 2
    for k, v in enumerate(vals):
        ak = a * clamp(n_float - k + 1)
        if ak <= 0:
            continue
        xx = x0 + k * (w + gap)
        chip(c, str(v), xx + w / 2, y, AMBER if k == 0 else (GREEN if v == 1 else INK2), ak, size=46, w=w)
        if k > 0:
            arrow(c, xx - gap + 10, y, xx - 10, y, GRAY, ak, 4, 12)
            text(c, "÷2", xx - gap / 2, y - 46, 24, "black", GRAY, ak)
            badge_num(c, k, xx - gap / 2, y + 66, ak, 22, bg=GREEN)


def b_atalho_inv(c, t, C, B):
    head(c, t, B["start"], "ATALHO", "QUANTAS MEIAS-VIDAS PASSARAM?", GREEN)
    card(c, *CARD_R)
    a0 = ep(t, C["12"], 0.4)
    K.atalho(c, 240, 200, 1440, 130, "ATALHO", ["divida o denominador por 2 até chegar a 1"], a0, 38)
    aa = ep(t, C["12.a"], 0.5)
    if aa > 0:
        mx(c, "1/16", 340, 470, 80, aa, AMBER)
        text(c, "denominador", 340, 580, 24, "black", AMBER, aa)
    n = clamp((t - C["12.b"]) / 4.5) * 5 if t >= C["12.b"] else (1 if aa > 0 else 0)
    cortes(c, 1080, 470, aa, n, 16)
    acc = ep(t, C["12.c"], 0.5)
    if acc > 0:
        regra(c, "4 CORTES = 4 MEIAS-VIDAS", W / 2, 660, acc, 38, GREEN)
        ac2 = ep(t, C["12.c"] + 2.4, 0.4)
        if ac2 > 0:
            linha(c, [("com o 8:  8 → 4 → 2 → 1  =  ", INK2), ("3 cortes", GREEN)], W / 2, 735, 32, ac2)
    ad = ep(t, C["12.d"], 0.5)
    if ad > 0:
        pill(c, "depois: × a duração de cada meia-vida", W / 2, 810, PURPLE, size=28, a=ad, anchor="center")


def b_pg(c, t, C, B):
    head(c, t, B["start"], "UM DETALHE PARA O FUTURO", "PROGRESSÃO GEOMÉTRICA", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["13.a"], 0.5)
    cadeia(c, ["1 000", "2 000", "4 000", "8 000"], 360, 380, [ep(t, C["13.a"] + 0.5 * j, 0.3) for j in range(4)], "×2",
           PURPLE, w=220, gap=90, size=40)
    if aa > 0:
        defin(c, "PROGRESSÃO GEOMÉTRICA", "cada número é o anterior × o mesmo fator", 220, 520, 1480,
              ep(t, C["13.a"] + 3.0, 0.4), BLUE, 28)
    ab = ep(t, C["13.b"], 0.5)
    if ab > 0:
        pill(c, "tem série própria · aqui, basta contar os apitos", W / 2, 700, PURPLE, size=30, a=ab, anchor="center")


# ======================================================================
# nós fazemos
# ======================================================================

def b_exercicio(c, t, C, B):
    head_seq(c, t, C, [("14", "SUA VEZ", "PAUSE E TENTE", GREEN), ("15", "VAMOS JUNTOS", "CONTE OS APITOS", GREEN)])
    card(c, *CARD_R)
    aa = ep(t, C["14.a"], 0.5)
    if aa > 0:
        caixa(c, 240, 210, 1440, 150, aa, BLUE)
        linha(c, [("120 g", BLUE), ("  ·  meia-vida ", INK), ("10 anos", PURPLE), ("  ·  depois de ", INK),
                  ("30 anos", PURPLE), ("?", INK)], W / 2, 285, 46, aa)
    if t < C["15"]:
        pause_timer(c, t, C["14.end"] - 1.9, W / 2, 560)
        return
    a1 = ep(t, C["15.a"], 0.5)
    if a1 > 0:
        caixa(c, 240, 390, 1440, 110, a1, PURPLE)
        linha(c, [("30 anos ÷ 10 anos = ", INK), ("3 meias-vidas", PURPLE)], W / 2, 445, 42, a1)
    ab = ep(t, C["15.b"], 0.5)
    vals = ["120 g", "60 g", "30 g", "15 g"]
    cadeia(c, vals, 380, 600, [ep(t, C["15.b"] + 0.8 * j, 0.3) for j in range(4)], "÷2", AMBER, w=220, gap=90, size=42)
    if ab > 0:
        pizza(c, 1700, 600, 60, ab, min(3.0, clamp((t - C["15.b"]) / 3.0) * 3))
    acc = ep(t, C["15.c"], 0.5)
    if acc > 0:
        K.expr(c, "120 · 1/8 = 15", W / 2, 760, 48, acc, cores={0: INK, 2: AMBER, 4: GREEN})
    ad = ep(t, C["15.d"], 0.5)
    if ad > 0:
        selo(c, 1560, 760, ad, "MENOS, MAS NÃO ZERO", GREEN, -4, 24)


# ======================================================================
# recap, erros
# ======================================================================

FRASES = ["Primeiro conte os intervalos, depois escreva a potência.",
          "Cada meia-vida corta pela metade o que existe naquele momento.",
          "Duplicações se multiplicam: 6 dobras são ×64, não ×12."]


def b_recap(c, t, C, B):
    sid = which(t, C, ["16", "29"])
    frame(c, t, B["start"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "16" else "PARA FECHAR", PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 300 + k * 180 + d
        badge_num(c, k + 1, 260, y - 16, a, 36, bg=PURPLE)
        para(c, s, 320, y, 50, "black", INK, a, 1360, 60)


ERROS = [("2 meias-vidas → não sobra NADA (0%)",
          "metade mais metade dá um inteiro",
          "a 2ª metade é do que SOBROU: 100% → 50% → 25%"),
         ("Dobrou 6 vezes → ficou 12 vezes maior",
          "dobrar é × 2, e 6 × 2 = 12",
          "cada dobra age sobre a anterior: 2⁶ = × 64"),
         ("Contar o começo como apito: 7 duplicações → 128 000",
          "a lista 0, 30, 60, … 180 min tem 7 instantes",
          "o relógio apita quando o intervalo TERMINA: 180 ÷ 30 = 6 apitos")]


def b_erros(c, t, C, B):
    K.erro_cards(c, t, C, ["17", "18", "19"], ERROS)


# ======================================================================
# questões
# ======================================================================

def _enunciado(c, linhas, a, y0=250, size=30, w=720):
    y = y0
    for s, col in linhas:
        for ln in K.wrap(s, "black", size, w):
            text(c, ln, 190, y, size, "black", col, a, align="left")
            y += size + 12
        y += 8
    return y


def _passos(c, t, itens, y0=230):
    """painel da resolução: itens = [(cue_t, partes_da_linha)]"""
    y = y0
    for tt, partes, size in itens:
        ak = ep(t, tt, 0.4)
        if ak > 0:
            linha(c, partes, 190, y, size, ak, align="left")
        y += size + 44
    return y


ALTS1 = [("A", "3 000", "500 · 6: linear", RED), ("B", "6 000", "500 · 2 · 6: somou as dobras", RED),
         ("C", "16 000", "contou 5 apitos", RED), ("D", "32 000", "", GREEN), ("E", "64 000", "contou o começo: 7", RED)]


def b_q1(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 1 · EU FAÇO", "A CULTURA QUE DOBRA", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["20.a"], 0.4)
    cues_in = {L: C[f"20.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"22.x{L.lower()}"] for L in "ABCE"}
    K.alternativas(c, t, C, ALTS1, 1080, 260, 600, 38, C["21.ok"], "D", cues_in, cues_x, gap=40)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0 * (1 - ep(t, C["21"], 0.3)),
         align="left")
    if t < C["21"]:
        _enunciado(c, [("Uma cultura começa com 500 bactérias, e a população dobra a cada 20 minutos, enquanto houver "
                        "nutrientes. Supondo que os nutrientes não se esgotem, o número de bactérias 2 horas após o "
                        "início do experimento será", INK)], a0, 250, 30)
        return
    a1 = ep(t, C["21"], 0.4)
    rrect(c, 160, 206, 820, 624, 18, "#FFFFFF", a1, shadow=True)
    _passos(c, t, [(C["21.a"], [("converta: ", GRAY), ("2 h = 120 min", BLUE)], 36),
                   (C["21.b"], [("apitos: ", GRAY), ("120 ÷ 20 = 6", PURPLE)], 36)], 270)
    ac = ep(t, C["21.c"], 0.4)
    if ac > 0:
        K.expr(c, "500 · 2^6 = 500 · 64", 570, 470, 46, ac, cores={2: PURPLE})
        text(c, "= 32 000", 570, 560, 56, "black", GREEN, ac)
    relogio(c, 830, 690, 80, ep(t, C["21.b"], 0.4), (t - C["21.b"]) / 0.5, total=6, rot_=None)
    ad = ep(t, C["21.d"], 0.4)
    if ad > 0:
        linha(c, [("16 000 ", GRAY), ("<  32 000  <", GREEN), (" 64 000", GRAY)], 450, 700, 32, ad)
        text(c, "um apito a menos · um a mais", 450, 760, 22, "bold", INK2, ad)


ALTS2 = [("A", "2,5 mg", "uma meia-vida a mais", RED), ("B", "5 mg", "", GREEN), ("C", "10 mg", "parou na 3ª", RED),
         ("D", "20 mg", "80 ÷ 4, e não ÷ 16", RED), ("E", "40 mg", "uma meia-vida só", RED)]


def b_q2(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 2 · NÓS FAZEMOS", "O IODO-131", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["23.a"], 0.4)
    cues_in = {L: C[f"23.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"25.x{L.lower()}"] for L in "ACDE"}
    K.alternativas(c, t, C, ALTS2, 1080, 260, 600, 38, C["24.ok"], "B", cues_in, cues_x, gap=40)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0 * (1 - ep(t, C["24"], 0.3)),
         align="left")
    if t < C["24"]:
        _enunciado(c, [("O iodo-131, usado em exames e tratamentos da tireoide, tem meia-vida de 8 dias. Um laboratório "
                        "recebeu uma amostra com 80 mg desse isótopo. Considerando apenas o decaimento radioativo, a massa "
                        "de iodo-131 restante na amostra após 32 dias será", INK)], a0, 250, 30)
        pause_timer(c, t, C["23.end"] - 1.9, 560, 740)
        return
    a1 = ep(t, C["24"], 0.4)
    rrect(c, 160, 206, 820, 624, 18, "#FFFFFF", a1, shadow=True)
    _passos(c, t, [(C["24.a"], [("dias e dias · apitos: ", GRAY), ("32 ÷ 8 = 4", PURPLE)], 34)], 270)
    ab = ep(t, C["24.b"], 0.4)
    if ab > 0:
        vals = ["80", "40", "20", "10", "5"]
        for j, v in enumerate(vals):
            aj = ep(t, C["24.b"] + 0.7 * j, 0.3)
            xx = 230 + j * 150
            chip(c, v, xx + 55, 420, GREEN if j == 4 else AMBER, aj, size=36, w=110)
            if j > 0:
                text(c, "÷2", xx - 20, 375, 20, "black", GRAY, aj)
        text(c, "em miligramas", 570, 490, 24, "bold", GRAY, ab)
    acc = ep(t, C["24.c"], 0.4)
    if acc > 0:
        K.expr(c, "80 · (1/2)^4 = 80/16 = 5", 570, 560, 44, acc, cores={0: INK, 2: PURPLE, 6: GREEN})
        linha(c, [("5 mg: ", GREEN), ("menos que 80, mais que 0", INK2)], 570, 690, 30, ep(t, C["24.c"] + 3.0, 0.4))


ALTS8 = [("A", "1 432,5", "dividiu 5 730 por 4", RED), ("B", "11 460", "2 meias-vidas", RED),
         ("C", "17 190", "3 meias-vidas", RED), ("D", "22 920", "", GREEN), ("E", "91 680", "16 meias-vidas?", RED)]


def b_q8(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 8 · VOCÊ FAZ", "DATAÇÃO POR CARBONO-14", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["26.a"], 0.4)
    cues_in = {L: C[f"26.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"28.x{L.lower()}"] for L in "ABCE"}
    K.alternativas(c, t, C, ALTS8, 1080, 260, 600, 38, C["27.ok"], "D", cues_in, cues_x, gap=40)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0 * (1 - ep(t, C["27"], 0.3)),
         align="left")
    if t < C["27"]:
        y = _enunciado(c, [("O carbono-14 tem meia-vida de aproximadamente 5 730 anos. Em um sítio arqueológico, "
                            "encontrou-se um fragmento de madeira com", INK)], a0, 250, 30)
        mx(c, "1/16", 260, y + 30, 56, a0, AMBER)
        _enunciado(c, [("da quantidade de carbono-14 de uma madeira viva. A idade aproximada do fragmento, em anos, "
                        "é", INK)], a0, y + 110, 30)
        pause_timer(c, t, C["26.end"] - 2.4, 560, 760)
        return
    a1 = ep(t, C["27"], 0.4)
    rrect(c, 160, 206, 820, 624, 18, "#FFFFFF", a1, shadow=True)
    aa = ep(t, C["27.a"], 0.4)
    if aa > 0:
        pill(c, "caminho INVERSO: deram a fração", 570, 260, BLUE, size=26, a=aa, anchor="center", bounds=(160, 980))
    ab = ep(t, C["27.b"], 0.4)
    if ab > 0:
        vals = ["16", "8", "4", "2", "1"]
        for j, v in enumerate(vals):
            aj = ep(t, C["27.b"] + 0.6 * j, 0.3)
            xx = 230 + j * 150
            chip(c, v, xx + 55, 390, AMBER if j == 0 else (GREEN if j == 4 else INK2), aj, size=36, w=110)
            if j > 0:
                badge_num(c, j, xx - 20, 450, aj, 18, bg=GREEN)
        text(c, "4 cortes = 4 meias-vidas", 570, 520, 32, "black", PURPLE, ep(t, C["27.b"] + 3.0, 0.4))
    acc = ep(t, C["27.c"], 0.4)
    if acc > 0:
        text(c, "4 · 5 730 anos", 570, 610, 44, "black", INK, acc)
        text(c, "= 22 920 anos", 570, 680, 52, "black", GREEN, acc)
    ad = ep(t, C["27.d"], 0.4)
    if ad > 0:
        text(c, "sobrou pouquinho → passou MUITO tempo", 570, 770, 24, "black", INK2, ad)


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "QUEM VENCE?", PURPLE)
    aa = ep(t, C["30.a"], 0.5)
    if aa > 0:
        rrect(c, 260, 240, 640, 260, 24, "#FFFFFF", aa, shadow=True)
        text(c, "PERFIL A", 580, 300, 34, "black", BLUE, aa)
        text(c, "+300", 580, 400, 80, "black", BLUE, aa)
        text(c, "seguidores por semana", 580, 460, 26, "bold", INK2, aa)
    ab = ep(t, C["30.b"], 0.5)
    if ab > 0:
        rrect(c, 1020, 240, 640, 260, 24, "#FFFFFF", ab, shadow=True)
        text(c, "PERFIL B", 1340, 300, 34, "black", PURPLE, ab)
        text(c, "×2", 1340, 400, 80, "black", PURPLE, ab)
        text(c, "começa com 100", 1340, 460, 26, "bold", INK2, ab)
    acc = ep(t, C["30.c"], 0.5)
    if acc > 0:
        rrect(c, 460, 540, 1000, 140, 26, mix("#FFFFFF", AMBER, 0.20), acc)
        text_mid(c, "quem vence, e QUANDO?", W / 2, 610, 56, "black", INK, acc)
    pill(c, "ep. 4 · exponencial ou afim? o teste da razão", W / 2, 760, PURPLE, size=26, a=ep(t, C["30.d"], 0.5),
         anchor="center")


def b_cta(c, t, C, B):
    cta(c, t, C["31.like"], C["31.sub"], C["31.bell"], C["31.com"], C["31.bye"],
        "Você já tinha ouvido falar do césio de Goiânia?", canal="no Estudativo", anki=C["31.anki"])


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, concreto=b_concreto, duplicacao=b_duplicacao,
              bacterias=b_bacterias, atalho_dup=b_atalho_dup, meiavida=b_meiavida, cesio=b_cesio, barras=b_barras,
              inverso=b_inverso, atalho_inv=b_atalho_inv, pg=b_pg, exercicio=b_exercicio, recap=b_recap, erros=b_erros,
              q1=b_q1, q2=b_q2, q8=b_q8, ponte=b_ponte, cta=b_cta)
