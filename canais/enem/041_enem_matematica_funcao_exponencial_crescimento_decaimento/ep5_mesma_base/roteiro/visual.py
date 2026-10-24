"""Visual — Função Exponencial, Episódio 5: equações e inequações exponenciais, mesma base (tema claro).
Peças comuns da série em ../../comum.py (reexporta o 019/comum.py: expr com potências e frações, alternativas, erro_cards,
atalho, selo, regra...).
Peças deste episódio: Plano (eixos e curva, como no ep. 1), traduz() (um número que se desfaz em fichas da base e se junta
na potência: 81 → 3 3 3 3 → 3⁴), balanca() (a balança com uma potência em cada prato; equilibra quando os expoentes são
iguais), embalagem() (a caixa em volta do número da frente, que sai), pacotes() (2ˣ como pacote), linha() e mx().
Números com milhar usam espaço rígido (NB) para o expr não partir o token.
Cores com função: azul = definição / base · roxo = regra / expoente · âmbar = armadilha · verde = atalho · vermelho = erro.
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
ARQUIVO_FINAL = "enem_matematica_exponencial_ep5_mesma_base.mp4"
CARD_R = K.CARD_R
GRADE = "#EEEEEA"
NB = " "
MIL = f"1{NB}000"
OITENTA_MIL = f"81{NB}000"


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


def defin(c, termo, s, x, y, w, a, col=None, size=30):
    """faixa de definição: TERMO: frase"""
    if a <= 0:
        return
    col = col or BLUE
    rrect(c, x, y, w, 70, 18, mix("#FFFFFF", col, 0.12), a)
    linha(c, [(termo, col), (": " + s, INK)], x + 28, y + 35, size, a, align="left")


def ease_out(u):
    return 1 - (1 - clamp(u)) ** 3


class Plano:
    """plano cartesiano num retângulo (x0, y0, w, h) com faixas xr, yr próprias (igual ao do ep. 1)."""

    def __init__(s, x0, y0, w, h, xr, yr):
        s.x0, s.y0, s.w, s.h, s.xr, s.yr = x0, y0, w, h, xr, yr

    def px(s, x):
        return s.x0 + (x - s.xr[0]) / (s.xr[1] - s.xr[0]) * s.w

    def py(s, y):
        return s.y0 + s.h - (y - s.yr[0]) / (s.yr[1] - s.yr[0]) * s.h

    def eixos(s, c, a, xt=(), yt=(), size=22, grade=True, rot=("x", "y")):
        if a <= 0:
            return
        if grade:
            for v in xt:
                line(c, s.px(v), s.y0, s.px(v), s.y0 + s.h, GRADE, a, 2)
            for v in yt:
                line(c, s.x0, s.py(v), s.x0 + s.w, s.py(v), GRADE, a, 2)
        oy = s.py(0) if s.yr[0] <= 0 <= s.yr[1] else s.y0 + s.h
        ox = s.px(0) if s.xr[0] <= 0 <= s.xr[1] else s.x0
        arrow(c, s.x0, oy, s.x0 + s.w + 24, oy, INK2, a, 3, 12)
        arrow(c, ox, s.y0 + s.h, ox, s.y0 - 22, INK2, a, 3, 12)
        text(c, rot[0], s.x0 + s.w + 22, oy + 36, 24, "black", GRAY, a)
        text(c, rot[1], ox - 22, s.y0 - 6, 24, "black", GRAY, a, align="right")
        f = lambda v: f"{v:g}".replace(".", ",").replace("-", "−")
        for v in xt:
            if v != 0:
                text(c, f(v), s.px(v), oy + size + 10, size, "bold", INK2, a)
        for v in yt:
            if v != 0:
                text(c, f(v), ox - 12, s.py(v) + size * 0.36, size, "bold", INK2, a, align="right")

    def curva(s, c, a, f, col, u=1.0, width=7, xa=None, xb=None, n=160):
        if a <= 0 or u <= 0:
            return
        xa = s.xr[0] if xa is None else xa
        xb = s.xr[1] if xb is None else xb
        xe = xa + (xb - xa) * clamp(u)
        c.save()
        c.clipRect(skia.Rect.MakeXYWH(s.x0, s.y0 - 4, s.w, s.h + 8))
        path = skia.Path()
        for k in range(n + 1):
            x = xa + (xe - xa) * k / n
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


def traduz(c, t, t0, num, base, n, cx, cy, size=70, col=None, dur=2.4):
    """o número `num` se desfaz em n fichas da `base`, que se juntam na potência base^n (a animação do 81 → 3⁴)."""
    col = col or BLUE
    u = clamp((t - t0) / dur)
    if t < t0 - 0.01:
        return
    # fase 1 (0–0,25): o número some · fase 2 (0,2–0,6): as fichas aparecem espalhadas · fase 3 (0,6–1): juntam-se
    a_num = 1 - clamp(u / 0.25)
    if a_num > 0:
        text_mid(c, num, cx, cy, size, "black", INK, a_num)
    a_f = clamp((u - 0.2) / 0.2) * (1 - clamp((u - 0.85) / 0.15))
    junta = ease_out(clamp((u - 0.6) / 0.3))
    gap0, gap1 = size * 1.25, size * 0.25
    gap = gap0 + (gap1 - gap0) * junta
    for k in range(n):
        x = cx + (k - (n - 1) / 2) * gap
        chip(c, str(base), x, cy, col, a_f, size=int(size * 0.6), w=int(size * 0.95))
    a_p = clamp((u - 0.85) / 0.15)
    if a_p > 0:
        mx(c, f"{base}^{n}", cx, cy, size * 1.15, a_p, col)


def balanca(c, cx, cy, esq, dir_, a, tilt=0.0, col_e=None, col_d=None, size=56, w=560, alt=190):
    """balança de dois pratos: esq/dir_ = expressões; tilt em −1..1 (0 = equilibrada)."""
    if a <= 0:
        return
    ang = tilt * 0.16
    dx, dy = math.cos(ang) * w / 2, math.sin(ang) * w / 2
    # base e coluna
    rrect(c, cx - 90, cy + alt, 180, 22, 11, INK2, a)
    line(c, cx, cy + alt, cx, cy, INK2, a, 8)
    c.drawCircle(cx, cy, 14, paint(INK2, a))
    # travessão
    line(c, cx - dx, cy - dy, cx + dx, cy + dy, INK2, a, 8)
    for sx, s_, col in ((-1, esq, col_e or BLUE), (1, dir_, col_d or BLUE)):
        px_, py_ = cx + sx * dx, cy + sx * dy
        line(c, px_, py_, px_ - 90, py_ + 90, GRAY, a, 3)
        line(c, px_, py_, px_ + 90, py_ + 90, GRAY, a, 3)
        rrect(c, px_ - 130, py_ + 88, 260, 16, 8, INK2, a)
        rrect(c, px_ - 120, py_ - 6, 240, 92, 18, "#FFFFFF", a, shadow=True)
        mx(c, s_, px_, py_ + 40, size, a, col)


def embalagem(c, x, y, w, h, a, sai=0.0, rot_="embalagem"):
    """caixa tracejada âmbar em volta do número da frente; sai = 0..1 (sobe e some)"""
    if a <= 0:
        return
    aa = a * (1 - sai)
    yy = y - 90 * ease_out(sai)
    rrect(c, x, yy, w, h, 16, AMBER, aa * 0.14)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, yy, w, h), 16, 16), paint(AMBER, aa, stroke=4))
    if rot_:
        pill(c, rot_, x + w / 2, yy - 26, AMBER, size=20, a=aa, anchor="center", bounds=(0, 1920))


def pacote(c, cx, cy, a, rot_="2ˣ", col=None, w=150, h=120):
    """um pacote (caixinha com fita) com o rótulo"""
    if a <= 0:
        return
    col = col or PURPLE
    rrect(c, cx - w / 2, cy - h / 2, w, h, 14, mix("#FFFFFF", col, 0.22), a, shadow=True)
    line(c, cx, cy - h / 2, cx, cy + h / 2, col, a, 5)
    line(c, cx - w / 2, cy - h * 0.1, cx + w / 2, cy - h * 0.1, col, a, 5)
    mx(c, rot_, cx, cy + h * 0.22, 40, a, col)


def _enunciado(c, linhas, a, y0=250, size=30, w=700):
    y = y0
    for s, col in linhas:
        for ln in K.wrap(s, "black", size, w):
            text(c, ln, 190, y, size, "black", col, a, align="left")
            y += size + 12
        y += 8
    return y


def passos(c, t, itens, x, y0, size, dy, align="left"):
    """lista de passos de conta: itens = [(t_entrada, expr, cor)]"""
    for k, (t0, s_, col) in enumerate(itens):
        a, d = rise(t, t0)
        if a > 0:
            mx(c, s_, x, y0 + k * dy + d, size, a, col, align=align)


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "FUNÇÃO EXPONENCIAL · EPISÓDIO 5", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["01.a"], 0.5)
    sai = ep(t, C["01.c"], 1.0)
    if aa > 0:
        K.expr(c, f"{MIL} · 3^{{t/2}} = {OITENTA_MIL}", W / 2, 300, 84, aa,
               cores={0: AMBER, 1: AMBER, 2: INK, 3: PURPLE}, alfas={0: 1 - sai, 1: 1 - sai, 2: 1 - sai})
    ab = ep(t, C["01.b"], 0.5)
    if ab > 0 and t < C["01.c"] + 0.4:
        selo(c, 1500, 210, ab, "SE PERDE", RED, 6, 30)
        strike(c, 560, 300, 1360, 300, ab * 0.8, RED)
    if t >= C["01.c"]:
        embalagem(c, 330, 245, 330, 112, 1.0, sai, "divida por 1 000")
        acc = ep(t, C["01.c"] + 0.9, 0.5)
        if acc > 0:
            K.expr(c, "3^{t/2} =", 900, 520, 80, acc, cores={0: PURPLE, 1: INK}, align="right")
            if t < C["01.c"] + 2.2:
                text_mid(c, "81", 1060, 520, 80, "black", INK, acc)
        traduz(c, t, C["01.c"] + 2.2, "81", 3, 4, 1060, 520, 80, BLUE, dur=2.4)
    ad = ep(t, C["01.d"], 0.5)
    if ad > 0:
        rrect(c, 640, 650, 640, 140, 26, mix("#FFFFFF", GREEN, 0.14), ad)
        mx(c, "t = 8", W / 2, 720, 84, ad, GREEN)
        selo(c, 1400, 650, ad, "DE CABEÇA", GREEN, -5, 26)


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "FUNÇÃO EXPONENCIAL · EP. 5", "AO FINAL DESTA AULA", GREEN)
    a0 = ep(t, C["02"], 0.4)
    if a0 > 0:
        pill(c, "5º episódio da série de FUNÇÃO EXPONENCIAL", W / 2, 240, BLUE, size=30, a=a0, anchor="center")
    itens = [("02.a", "EQUAÇÕES", "e inequações exponenciais", BLUE), ("02.b", "MESMA BASE", "tudo traduzido", PURPLE),
             ("02.c", "O SINAL VIRA?", "saber quando", AMBER)]
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
    a0 = ep(t, C["03"], 0.4)
    if a0 > 0:
        pill(c, "série de Potenciação e radiciação", 260, 230, BLUE, size=22, a=a0, bounds=(0, 1920))
    rows = [("03.a", [("4", "2^2"), ("8", "2^3"), ("32", "2^5")], BLUE),
            ("03.b", [("9", "3^2"), ("27", "3^3"), ("81", "3^4")], PURPLE)]
    for j, (cue, pares, col) in enumerate(rows):
        a = ep(t, C[cue], 0.5)
        if a <= 0:
            continue
        y = 330 + j * 150
        rrect(c, 240, y - 60, 1000, 120, 22, "#FFFFFF", a, shadow=True)
        for k, (n_, p_) in enumerate(pares):
            K.expr(c, f"{n_} = {p_}", 400 + k * 330, y, 52, a, cores={0: INK, 2: col})
    acc = ep(t, C["03.c"], 0.5)
    if acc > 0:
        rrect(c, 240, 580, 480, 140, 22, "#FFFFFF", acc, shadow=True)
        K.expr(c, "1/8 = 2^{-3}", 480, 650, 52, acc, cores={0: INK, 2: AMBER})
    ad = ep(t, C["03.d"], 0.5)
    if ad > 0:
        rrect(c, 760, 580, 480, 140, 22, "#FFFFFF", ad, shadow=True)
        K.expr(c, "(a^m)^n = a^{m·n}", 1000, 650, 52, ad, cores={0: INK, 2: PURPLE})
    ae = ep(t, C["03.e"], 0.5)
    if ae > 0:
        P = Plano(1330, 300, 360, 380, (-2, 2), (-0.3, 4.5))
        P.eixos(c, ae, grade=False)
        P.curva(c, ae, lambda x: 2 ** x, BLUE, u=ep(t, C["03.e"], 1.0), width=6)
        P.curva(c, ae, lambda x: 0.5 ** x, PURPLE, u=ep(t, C["03.e"] + 0.6, 1.0), width=6)
        pill(c, "base > 1 sobe", 1520, 730, BLUE, size=22, a=ae, anchor="center")
        pill(c, "0 < base < 1 desce", 1520, 780, PURPLE, size=22, a=ae, anchor="center")


# ======================================================================
# concreto · bloco a — a ideia
# ======================================================================

def b_concreto(c, t, C, B):
    head(c, t, B["start"], "PERGUNTAS DE VERDADE", "QUANDO?", BLUE)
    card(c, *CARD_R)
    for k, (cue, tit, s_, col) in enumerate((("04.a", "AVES NA RESERVA", f"quando chega a {OITENTA_MIL}?", GREEN),
                                             ("04.b", "REMÉDIO NO SANGUE", "quando cai a 50 mg/L?", RED))):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        x = 300 + k * 680
        rrect(c, x, 230 + d, 640, 220, 24, "#FFFFFF", a, shadow=True)
        text(c, tit, x + 320, 300 + d, 34, "black", col, a)
        text(c, s_, x + 320, 380 + d, 36, "bold", INK, a)
    acc = ep(t, C["04.c"], 0.5)
    if acc > 0:
        K.expr(c, "3^{?}", 760, 545, 80, acc, cores={0: PURPLE})
        K.expr(c, "(1/2)^{?}", 1160, 545, 80, acc, cores={0: PURPLE})
        pill(c, "o que procuramos está NO EXPOENTE", W / 2, 670, PURPLE, size=28, a=acc, anchor="center")
    ad = ep(t, C["04.d"], 0.5)
    if ad > 0:
        defin(c, "EQUAÇÃO EXPONENCIAL", "a incógnita está no expoente", 380, 730, 1160, ad, BLUE, 30)


def b_ideia(c, t, C, B):
    head(c, t, B["start"], "A IDEIA", "MESMA BASE DOS DOIS LADOS", PURPLE)
    card(c, *CARD_R)
    aa = ep(t, C["05.a"], 0.5)
    if aa > 0:
        defin(c, "MESMA BASE", "o mesmo número sendo multiplicado", 380, 200, 1160, aa, BLUE, 30)
    ab = ep(t, C["05.b"], 0.5)
    if ab > 0:
        # duas "fotos" idênticas
        for k in range(2):
            x = 360 + k * 420
            rrect(c, x, 330, 340, 260, 16, "#FFFFFF", ab, shadow=True)
            rrect(c, x + 18, 348, 304, 180, 10, mix("#FFFFFF", BLUE, 0.12), ab)
            mx(c, "3^{■}", x + 170, 440, 90, ab, BLUE)
            text(c, "foto " + str(k + 1), x + 170, 570, 24, "bold", GRAY, ab)
        text_mid(c, "=", 740, 460, 80, "black", INK, ab)
        ab2 = ep(t, C["05.b"] + 2.2, 0.5)
        if ab2 > 0:
            regra(c, "EXPOENTES IGUAIS", 1420, 460, ab2, 40, PURPLE)
    acc = ep(t, C["05.c"], 0.5)
    if acc > 0:
        defin(c, "INJETORA", "x diferentes dão potências diferentes", 380, 680, 1160, acc, BLUE, 30)


# ======================================================================
# bloco b — a tabela da seção 07 · atalho
# ======================================================================

def _tab_ex(c, t, C, sid, eq, traducao, igual, res, col_res=GREEN, extra=None):
    aa = ep(t, C[f"{sid}.a"], 0.5)
    if aa > 0:
        rrect(c, 380, 200, 1160, 140, 24, "#FFFFFF", aa, shadow=True)
        mx(c, eq, W / 2, 270, 72, aa, INK)
    ab = ep(t, C[f"{sid}.b"], 0.5)
    if ab > 0:
        K.expr(c, traducao, W / 2, 430, 64, ab, cores={i: BLUE for i in range(12)})
    acc = ep(t, C[f"{sid}.c"], 0.5)
    if acc > 0:
        balanca(c, W / 2, 560, igual[0], igual[1], acc, tilt=0.0, size=52)
    ad = ep(t, C[f"{sid}.d"], 0.5)
    if ad > 0:
        rrect(c, 1380, 640, 340, 130, 24, mix("#FFFFFF", col_res, 0.14), ad)
        mx(c, res, 1550, 705, 60, ad, col_res)
        if extra:
            pill(c, extra, 1550, 800, col_res, size=22, a=ad, anchor="center", bounds=(0, 1920))


def b_tab1(c, t, C, B):
    head(c, t, B["start"], "1º EXEMPLO", "A MESMA BASE", BLUE)
    card(c, *CARD_R)
    _tab_ex(c, t, C, "06", "2^{x+1} = 32", "32 = 2^5", ("2^{x+1}", "2^5"), "x = 4")
    acc = ep(t, C["06.c"], 0.5)
    if acc > 0:
        K.expr(c, "x + 1 = 5", 440, 705, 50, acc, cores={i: PURPLE for i in range(5)})


def b_tab2(c, t, C, B):
    head(c, t, B["start"], "BASES DIFERENTES?", "FILHOS DO 3", PURPLE)
    card(c, *CARD_R)
    aa = ep(t, C["07.a"], 0.5)
    if aa > 0:
        rrect(c, 380, 200, 1160, 140, 24, "#FFFFFF", aa, shadow=True)
        mx(c, "9^x = 27", W / 2, 270, 72, aa, INK)
    ab = ep(t, C["07.b"], 0.5)
    if ab > 0:
        traduz(c, t, C["07.b"] + 0.6, "9", 3, 2, 640, 430, 64, BLUE, dur=2.2)
        traduz(c, t, C["07.b"] + 2.2, "27", 3, 3, 1280, 430, 64, BLUE, dur=2.2)
    acc = ep(t, C["07.c"], 0.5)
    if acc > 0:
        K.expr(c, "(3^2)^x = 3^{2x}", 640, 580, 56, acc, cores={0: INK, 2: PURPLE})
        pill(c, "potência de potência: multiplica", 640, 660, PURPLE, size=22, a=acc, anchor="center")
    ad = ep(t, C["07.d"], 0.5)
    if ad > 0:
        balanca(c, 1180, 600, "3^{2x}", "3^3", ad, size=44, w=420)
        K.expr(c, "2x = 3", 640, 760, 52, ad, cores={0: PURPLE, 2: PURPLE})
        rrect(c, 1460, 720, 300, 110, 22, mix("#FFFFFF", GREEN, 0.14), ad)
        mx(c, "x = 3/2", 1610, 775, 50, ad, GREEN)


def b_tab3(c, t, C, B):
    head(c, t, B["start"], "E COM FRAÇÃO?", "EXPOENTE NEGATIVO", AMBER)
    card(c, *CARD_R)
    aa = ep(t, C["08.a"], 0.5)
    if aa > 0:
        rrect(c, 380, 200, 1160, 150, 24, "#FFFFFF", aa, shadow=True)
        mx(c, "4^x = 1/8", W / 2, 275, 72, aa, INK)
    ab = ep(t, C["08.b"], 0.5)
    if ab > 0:
        K.expr(c, "4 = 2^2", 620, 440, 60, ab, cores={0: INK, 2: BLUE})
        K.expr(c, "1/8 = 2^{-3}", 1300, 440, 60, ab, cores={0: INK, 2: AMBER})
    acc = ep(t, C["08.c"], 0.5)
    if acc > 0:
        balanca(c, W / 2, 560, "2^{2x}", "2^{-3}", acc, size=48, w=520)
    ad = ep(t, C["08.d"], 0.5)
    if ad > 0:
        rrect(c, 1380, 640, 340, 130, 24, mix("#FFFFFF", GREEN, 0.14), ad)
        mx(c, "x = -3/2", 1550, 705, 54, ad, GREEN)
        pill(c, "resultado < 1 → x negativo", 1550, 800, AMBER, size=20, a=ad, anchor="center", bounds=(0, 1920))


def b_atalho_base(c, t, C, B):
    head(c, t, B["start"], "ATALHO", "ACHE A MENOR BASE", GREEN)
    card(c, *CARD_R)
    a0 = ep(t, C["09"], 0.4)
    K.atalho(c, 240, 200, 1440, 150, "ATALHO", ["qual é o MENOR número que gera os dois lados?"], a0, 38)
    for j, (cue, nums, base, col) in enumerate((("09.b", ["4", "8", "16", "32"], "2", BLUE),
                                                ("09.b", ["9", "27", "81"], "3", PURPLE))):
        a = ep(t, C[cue] + 1.8 * j, 0.5)
        if a <= 0:
            continue
        y = 450 + j * 140
        for k, n_ in enumerate(nums):
            chip(c, n_, 420 + k * 170, y, col, a, size=40, w=130)
        arrow(c, 1110, y, 1240, y, col, a, 5, 16)
        rrect(c, 1270, y - 52, 220, 104, 20, mix("#FFFFFF", col, 0.16), a)
        text_mid(c, "base " + base, 1380, y, 40, "black", col, a)
    acc = ep(t, C["09.c"], 0.5)
    if acc > 0:
        regra(c, "TRADUZA CADA NÚMERO ANTES DE QUALQUER CONTA", W / 2, 790, acc, 34, GREEN)


# ======================================================================
# bloco c — isole a potência · atalho
# ======================================================================

def b_isolar(c, t, C, B):
    head(c, t, B["start"], "ISOLE A POTÊNCIA", "TIRE A EMBALAGEM", AMBER)
    card(c, *CARD_R)
    aa = ep(t, C["10.a"], 0.5)
    sai = ep(t, C["10.c"], 1.0)
    if aa > 0:
        K.expr(c, f"{MIL} · 3^{{t/2}} = {OITENTA_MIL}", W / 2, 270, 70, aa,
               cores={0: AMBER, 1: AMBER, 2: INK, 3: PURPLE}, alfas={0: 1 - sai, 1: 1 - sai, 2: 1 - sai})
    ab = ep(t, C["10.b"], 0.5)
    if ab > 0:
        embalagem(c, 448, 222, 270, 98, ab, sai, "embalagem")
        defin(c, "ISOLAR A POTÊNCIA", "deixá-la sozinha de um lado", 380, 380, 1160, ab * (1 - sai), BLUE, 30)
    acc = ep(t, C["10.c"], 0.5)
    if acc > 0:
        pill(c, "divida os dois lados por 1 000", W / 2, 390, AMBER, size=26, a=acc, anchor="center")
        K.expr(c, "3^{t/2} = 81", W / 2, 490, 72, acc, cores={0: PURPLE, 2: INK})
    ad = ep(t, C["10.d"], 0.5)
    if ad > 0:
        rrect(c, 300, 560, 1320, 70, 20, mix("#FFFFFF", PURPLE, 0.10), ad)
        text_mid(c, "cada lado é UMA potência só, da mesma base?", W / 2, 595, 30, "black", PURPLE, ad)
        balanca(c, 760, 680, "3^{t/2}", "3^4", ep(t, C["10.d"] + 2.4, 0.5), size=44, w=440, alt=110)
    ae = ep(t, C["10.e"], 0.5)
    if ae > 0:
        K.expr(c, "t/2 = 4", 1320, 720, 52, ae, cores={0: PURPLE, 2: PURPLE})
        rrect(c, 1500, 680, 240, 90, 20, mix("#FFFFFF", GREEN, 0.14), ae)
        mx(c, "t = 8", 1620, 725, 46, ae, GREEN)


def b_atalho_conf(c, t, C, B):
    head(c, t, B["start"], "ATALHO", "CONFIRA DEVOLVENDO", GREEN)
    card(c, *CARD_R)
    a0 = ep(t, C["11"], 0.4)
    K.atalho(c, 240, 200, 1440, 150, "ATALHO", ["devolva a resposta na equação"], a0, 40)
    passos(c, t, [(C["11.a"], "t = 8  →  8/2 = 4", PURPLE), (C["11.a"] + 1.6, "3^4 = 81", BLUE),
                  (C["11.b"], f"81 · {MIL} = {OITENTA_MIL}", GREEN)], W / 2, 450, 60, 120, align="center")
    ab = ep(t, C["11.b"] + 1.2, 0.4)
    if ab > 0:
        selo(c, 1520, 690, ab, "BATEU", GREEN, -6, 34)


# ======================================================================
# bloco d — duas potências somadas · atalho
# ======================================================================

def b_evidencia(c, t, C, B):
    head(c, t, B["start"], "DUAS POTÊNCIAS SOMADAS", "COLOQUE EM EVIDÊNCIA", PURPLE)
    card(c, *CARD_R)
    aa = ep(t, C["12.a"], 0.5)
    if aa > 0:
        rrect(c, 380, 200, 1160, 140, 24, "#FFFFFF", aa, shadow=True)
        K.expr(c, "2^x + 2^{x+1} = 24", W / 2, 270, 70, aa, cores={0: PURPLE, 2: PURPLE})
    ab = ep(t, C["12.b"], 0.5)
    if ab > 0:
        K.expr(c, "2^{x+1} = 2 · 2^x", W / 2, 420, 60, ab, cores={0: PURPLE, 2: GREEN, 4: PURPLE})
    acc = ep(t, C["12.c"], 0.5)
    if acc > 0:
        defin(c, "EM EVIDÊNCIA", "o que se repete vai para fora do parêntese", 380, 490, 1160, acc, BLUE, 28)
        K.expr(c, "2^x · (1+2) = 24", W / 2, 640, 60, ep(t, C["12.c"] + 2.4, 0.4), cores={0: PURPLE})
    ad = ep(t, C["12.d"], 0.5)
    if ad > 0:
        K.expr(c, "2^x = 8 = 2^3", 760, 760, 54, ad, cores={0: PURPLE, 4: BLUE})
        rrect(c, 1240, 710, 300, 100, 20, mix("#FFFFFF", GREEN, 0.14), ad)
        mx(c, "x = 3", 1390, 760, 50, ad, GREEN)


def b_atalho_pacote(c, t, C, B):
    head(c, t, B["start"], "ATALHO", "PENSE EM PACOTES", GREEN)
    card(c, *CARD_R)
    a0 = ep(t, C["13"], 0.4)
    K.atalho(c, 240, 200, 1440, 150, "ATALHO", ["2ˣ = 1 pacote  ·  2ˣ⁺¹ = 2 pacotes"], a0, 40)
    aa = ep(t, C["13.a"], 0.5)
    pacote(c, 480, 500, aa)
    if aa > 0:
        text(c, "2ˣ", 480, 610, 30, "black", PURPLE, aa)
    ab = ep(t, C["13.b"], 0.5)
    if ab > 0:
        text_mid(c, "+", 640, 500, 70, "black", INK, ab)
        pacote(c, 800, 500, ab)
        pacote(c, 980, 500, ab)
        text(c, "2ˣ⁺¹", 890, 610, 30, "black", PURPLE, ab)
    acc = ep(t, C["13.c"], 0.5)
    if acc > 0:
        text_mid(c, "= 24", 1200, 500, 70, "black", INK, acc)
        rrect(c, 1360, 430, 360, 140, 22, mix("#FFFFFF", GREEN, 0.14), acc)
        text_mid(c, "3 pacotes = 24", 1540, 475, 32, "black", INK, acc)
        text_mid(c, "1 pacote = 8", 1540, 530, 36, "black", GREEN, acc)


# ======================================================================
# bloco e — quando não fecha
# ======================================================================

def b_naofecha(c, t, C, B):
    head(c, t, B["start"], "QUANDO NÃO FECHA", "A PROMESSA DO LOGARITMO", AMBER)
    card(c, *CARD_R)
    aa = ep(t, C["14.a"], 0.5)
    if aa > 0:
        rrect(c, 640, 200, 640, 140, 24, "#FFFFFF", aa, shadow=True)
        mx(c, "2^x = 10", W / 2, 270, 72, aa, INK)
    ab = ep(t, C["14.b"], 0.5)
    if ab > 0:
        xa, xb, y = 420, 1500, 520
        line(c, xa, y, xb, y, INK2, ab, 4)
        for v, lab, col in ((3, "2³ = 8", BLUE), (4, "2⁴ = 16", BLUE)):
            xx = xa + (v - 2.5) / 2 * (xb - xa)
            line(c, xx, y - 20, xx, y + 20, INK2, ab, 4)
            text(c, str(v), xx, y + 60, 34, "black", INK, ab)
            pill(c, lab, xx, y - 60, col, size=26, a=ab, anchor="center")
        x10 = xa + (math.log2(10) - 2.5) / 2 * (xb - xa)
        c.drawCircle(x10, y, 16, paint(AMBER, ab))
        pill(c, "x = ?", x10, y + 110, AMBER, size=28, a=ab, anchor="center")
    acc = ep(t, C["14.c"], 0.5)
    if acc > 0:
        regra(c, "VALOR EXATO: LOGARITMO · PRÓXIMA SÉRIE", W / 2, 760, acc, 36, AMBER)


# ======================================================================
# bloco f — inequações · ladeira · atalho
# ======================================================================

def b_ineq1(c, t, C, B):
    head(c, t, B["start"], "INEQUAÇÕES", "BASE MAIOR QUE 1", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["15.a"], 0.5)
    if aa > 0:
        defin(c, "INEQUAÇÃO", "a resposta é uma faixa de valores", 380, 200, 1160, aa, BLUE, 30)
    ab = ep(t, C["15.b"], 0.5)
    if ab > 0:
        defin(c, "SENTIDO DA DESIGUALDADE", "se o sinal é de maior ( > ) ou de menor ( < )", 380, 300, 1160, ab, BLUE,
              28)
    acc = ep(t, C["15.c"], 0.5)
    if acc > 0:
        K.expr(c, "2^x > 16 = 2^4", W / 2, 470, 72, acc, cores={0: BLUE, 2: INK, 4: BLUE})
    ad = ep(t, C["15.d"], 0.5)
    if ad > 0:
        pill(c, "base 2 > 1 → o sinal SE MANTÉM", W / 2, 570, BLUE, size=28, a=ad, anchor="center")
        rrect(c, 760, 640, 400, 130, 24, mix("#FFFFFF", GREEN, 0.14), ad)
        mx(c, "x > 4", W / 2, 705, 64, ad, GREEN)


def b_ineq2(c, t, C, B):
    head(c, t, B["start"], "INEQUAÇÕES", "BASE ENTRE 0 E 1", AMBER)
    card(c, *CARD_R)
    aa = ep(t, C["16.a"], 0.5)
    if aa > 0:
        rrect(c, 380, 200, 1160, 150, 24, "#FFFFFF", aa, shadow=True)
        K.expr(c, "(1/3)^x > 9", W / 2, 275, 72, aa, cores={0: PURPLE, 2: INK})
    ab = ep(t, C["16.b"], 0.5)
    if ab > 0:
        K.expr(c, "9 = (1/3)^{-2}", W / 2, 440, 64, ab, cores={0: INK, 2: PURPLE})
        pill(c, "expoente negativo inverte a fração", W / 2, 530, PURPLE, size=24, a=ab, anchor="center")
    acc = ep(t, C["16.c"], 0.5)
    if acc > 0:
        gira = ep(t, C["16.c"] + 0.6, 1.0)
        cx_, cy_ = 700, 690
        c.save()
        c.translate(cx_, cy_)
        c.rotate(180 * gira)
        text_mid(c, ">", 0, 0, 120, "black", AMBER, acc)
        c.restore()
        text(c, "o sinal VIRA", 700, 800, 28, "black", AMBER, acc)
        rrect(c, 960, 620, 560, 140, 24, mix("#FFFFFF", GREEN, 0.14), ep(t, C["16.c"] + 1.6, 0.4))
        mx(c, "x < -2", 1240, 690, 70, ep(t, C["16.c"] + 1.6, 0.4), GREEN)


def b_ladeira(c, t, C, B):
    head(c, t, B["start"], "POR QUE O SINAL VIRA?", "A LADEIRA", PURPLE)
    card(c, *CARD_R)
    P = Plano(260, 220, 880, 560, (-3.5, 1.5), (-1, 30))
    aa = ep(t, C["17.a"], 0.5)
    P.eixos(c, aa, xt=(-3, -2, -1, 1), yt=(9, 27))
    P.curva(c, aa, lambda x: (1 / 3) ** x, PURPLE, u=ep(t, C["17.a"], 1.4))
    if aa > 0:
        pill(c, "(1/3)ˣ: uma ladeira descendo", P.px(-0.4), P.py(24), PURPLE, size=24, a=aa, bounds=(0, 1920))
    ab = ep(t, C["17.b"], 0.5)
    if ab > 0:
        rrect(c, 1200, 230, 520, 170, 22, mix("#FFFFFF", PURPLE, 0.10), ab)
        text(c, "MAIS ALTO", 1460, 295, 36, "black", PURPLE, ab)
        text(c, "= mais para trás (menor x)", 1460, 355, 26, "bold", INK2, ab)
    acc = ep(t, C["17.c"], 0.5)
    if acc > 0:
        line(c, P.x0, P.py(9), P.x0 + P.w, P.py(9), AMBER, acc, 4, dash=(14, 10))
        text(c, "9", P.x0 + P.w + 30, P.py(9) + 10, 28, "black", AMBER, acc)
        P.ponto(c, -2, 9, AMBER, acc, "(−2, 9)", dx=26, dy=-46)
        xa = P.px(-3.5)
        rrect(c, xa, P.py(30), P.px(-2) - xa, P.py(9) - P.py(30), 0, GREEN, acc * 0.12)
        arrow(c, P.px(-2) - 10, P.py(0) + 40, P.px(-3.4), P.py(0) + 40, GREEN, acc, 6, 18)
        pill(c, "acima do 9 → à esquerda do −2", 1200, 470, GREEN, size=26, a=acc, bounds=(0, 1920))
    ad = ep(t, C["17.d"], 0.5)
    if ad > 0:
        P.ponto(c, -3, 27, GREEN, ad, None)
        rrect(c, 1200, 560, 520, 150, 22, "#FFFFFF", ad, shadow=True)
        K.expr(c, "(1/3)^{-3} = 27 > 9", 1460, 635, 44, ad, cores={0: PURPLE, 2: GREEN})
        selo(c, 1610, 760, ad, "CONFERE", GREEN, -6, 26)


def b_atalho_sinal(c, t, C, B):
    head(c, t, B["start"], "ATALHO", "OLHE A BASE", GREEN)
    card(c, *CARD_R)
    a0 = ep(t, C["18"], 0.4)
    K.atalho(c, 240, 200, 1440, 150, "ATALHO", ["antes de comparar os expoentes, olhe a base"], a0, 38)
    ab = ep(t, C["18.b"], 0.5)
    if ab > 0:
        for k, (tit, s_, col) in enumerate((("BASE > 1", "COPIE o sinal", BLUE), ("0 < BASE < 1", "VIRE o sinal", AMBER))):
            ak = ep(t, C["18.b"] + 1.8 * k, 0.5)
            x = 300 + k * 680
            rrect(c, x, 420, 640, 200, 24, mix("#FFFFFF", col, 0.12), ak)
            text(c, tit, x + 320, 490, 40, "black", col, ak)
            text(c, s_, x + 320, 570, 40, "black", INK, ak)
    acc = ep(t, C["18.c"], 0.5)
    if acc > 0:
        pill(c, "na dúvida: TESTE UM NÚMERO da sua resposta", W / 2, 720, GREEN, size=30, a=acc, anchor="center")


# ======================================================================
# nós fazemos
# ======================================================================

def b_exercicio(c, t, C, B):
    head_seq(c, t, C, [("19", "SUA VEZ", "PAUSE E TENTE", GREEN), ("20", "VAMOS JUNTOS", "FILHOS DO 2", GREEN)])
    card(c, *CARD_R)
    aa = ep(t, C["19.a"], 0.5)
    if aa > 0:
        rrect(c, 640, 200, 640, 150, 24, "#FFFFFF", aa, shadow=True)
        mx(c, "8^x = 32", W / 2, 275, 76, aa, INK)
    if t < C["20"]:
        ab = ep(t, C["19.b"], 0.5)
        if ab > 0:
            pill(c, "dica: ache a menor base dos dois", W / 2, 440, GREEN, size=28, a=ab, anchor="center")
        pause_timer(c, t, C["19.end"] - 1.9, W / 2, 620)
        return
    a1 = ep(t, C["20.a"], 0.4)
    if a1 > 0:
        traduz(c, t, C["20.a"] + 0.8, "8", 2, 3, 640, 450, 60, BLUE, dur=2.0)
        traduz(c, t, C["20.a"] + 2.4, "32", 2, 5, 1280, 450, 60, BLUE, dur=2.2)
    ab = ep(t, C["20.b"], 0.5)
    if ab > 0:
        balanca(c, 760, 590, "2^{3x}", "2^5", ab, size=44, w=440)
    acc = ep(t, C["20.c"], 0.5)
    if acc > 0:
        K.expr(c, "3x = 5", 1400, 600, 56, acc, cores={0: PURPLE, 2: PURPLE})
        rrect(c, 1250, 660, 300, 130, 22, mix("#FFFFFF", GREEN, 0.14), acc)
        mx(c, "x = 5/3", 1400, 725, 54, acc, GREEN)
        pill(c, "fração também é resposta", 1400, 820, GREEN, size=20, a=ep(t, C["20.c"] + 1.6, 0.4), anchor="center")


# ======================================================================
# recap
# ======================================================================

FRASES = ["Mesma base dos dois lados: iguale os expoentes.",
          "Isole a potência antes de comparar expoentes.",
          "Base entre 0 e 1 inverte a desigualdade."]


def b_recap(c, t, C, B):
    sid = which(t, C, ["21", "32"])
    frame(c, t, B["start"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "21" else "PARA FECHAR", PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 300 + k * 180 + d
        badge_num(c, k + 1, 260, y - 16, a, 36, bg=PURPLE)
        para(c, s, 320, y, 50, "black", INK, a, 1360, 60)


# ======================================================================
# bloco g — em contexto (exemplo NOSSO: o cloro da piscina)
# ======================================================================

def b_contexto(c, t, C, B):
    head(c, t, B["start"], "EM CONTEXTO", "O CLORO DA PISCINA", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["22.a"], 0.5)
    P = Plano(260, 250, 640, 480, (0, 13), (0, 9))
    if aa > 0:
        P.eixos(c, aa, xt=(3, 6, 9, 12), yt=(1, 2, 4, 8), rot=("t (h)", "mg/L"))
        P.curva(c, aa, lambda x: 8 * 0.5 ** (x / 3), BLUE, u=ep(t, C["22.a"] + 0.8, 2.4))
        for k, (x, y) in enumerate(((0, 8), (3, 4), (6, 2), (9, 1))):
            P.ponto(c, x, y, BLUE, ep(t, C["22.a"] + 1.0 + 0.6 * k, 0.3))
        line(c, P.x0, P.py(1), P.x0 + P.w, P.py(1), AMBER, aa, 4, dash=(14, 10))
        pill(c, "age acima de 1 mg/L", P.px(10.5), P.py(1) - 34, AMBER, size=20, a=aa, anchor="center",
             bounds=(0, 1920))
    ab = ep(t, C["22.b"], 0.5)
    if ab > 0:
        rrect(c, 960, 230, 760, 130, 22, "#FFFFFF", ab, shadow=True)
        K.expr(c, "8 · (1/2)^{t/3} > 1", 1340, 295, 54, ab, cores={0: AMBER, 2: PURPLE})
    acc = ep(t, C["22.c"], 0.5)
    if acc > 0:
        pill(c, "divida por 8: tire a embalagem", 1340, 400, AMBER, size=24, a=acc, anchor="center")
        K.expr(c, "(1/2)^{t/3} > (1/2)^3", 1340, 490, 54, acc, cores={0: PURPLE, 2: PURPLE})
    ad = ep(t, C["22.d"], 0.5)
    if ad > 0:
        pill(c, "base 1/2 entre 0 e 1 → o sinal VIRA", 1340, 590, AMBER, size=24, a=ad, anchor="center")
        K.expr(c, "t/3 < 3", 1160, 690, 52, ad, cores={0: PURPLE, 2: PURPLE})
        rrect(c, 1360, 640, 360, 110, 22, mix("#FFFFFF", GREEN, 0.14), ad)
        mx(c, "t < 9 h", 1540, 695, 52, ad, GREEN)
        rrect(c, P.x0, P.y0, P.px(9) - P.x0, P.h, 0, GREEN, ad * 0.10)


# ======================================================================
# erros
# ======================================================================

ERROS = [("1 000 · 3ᵗ = 81 000: comparar expoentes com o número NA FRENTE",
          "a potência de três está ali, pedindo comparação",
          "o mil é a embalagem: divida por mil antes → 3ᵗ = 81 = 3⁴ → t = 4"),
         ("(1/3)ˣ > 9  ⇒  x > −2",
          "em todas as outras contas o sinal foi copiado",
          "base entre 0 e 1: a ladeira desce e o sinal VIRA → x < −2"),
         ("2ˣ⁺¹ lido como 2ˣ + 1",
          "o “+ 1” está escrito ali… mas está no EXPOENTE",
          "2ˣ⁺¹ = 2 · 2ˣ: um pacote a mais, não uma unidade a mais")]


def b_erros(c, t, C, B):
    K.erro_cards(c, t, C, ["23", "24", "25"], ERROS)


# ======================================================================
# questão 4 (eu faço) · questão 7 (você faz)
# ======================================================================

ALTS4 = [("A", "4 anos", "esqueceu de dividir o expoente por 2", RED), ("B", "8 anos", "", GREEN),
         ("C", "27 anos", "dividiu 81 por 3 (como se fosse 3t)", RED), ("D", "54 anos", "expoente como produto", RED),
         ("E", "162 anos", "igualou o expoente ao valor", RED)]


def b_q4(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 4 · EU FAÇO", "AS AVES DA RESERVA", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["26.a"], 0.4)
    cues_in = {L: C[f"26.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"28.x{L.lower()}"] for L in "ACDE"}
    K.alternativas(c, t, C, ALTS4, 1000, 260, 680, 38, C["27.ok"], "B", cues_in, cues_x, gap=40)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0 * (1 - ep(t, C["27"], 0.3)),
         align="left")
    if t < C["27"]:
        yend = _enunciado(c, [("Um estudo projetou que a população de uma espécie de ave em uma reserva, após t anos de "
                               "um programa de proteção, seria dada por", INK)], a0, 236, 28)
        K.expr(c, f"P(t) = {MIL} · 3^{{t/2}}", 540, yend + 30, 46, a0, cores={2: AMBER, 3: AMBER, 5: PURPLE})
        y2 = _enunciado(c, [("Segundo esse modelo, a população atingirá", INK)], a0, yend + 110, 28)
        text(c, "81 000 aves após", 190, y2, 28, "black", INK, a0, align="left")
        return
    y0 = 206
    a1 = ep(t, C["27"], 0.4)
    rrect(c, 170, y0, 740, 830 - y0, 18, "#FFFFFF", a1, shadow=True)
    pill(c, "EQUAÇÃO · número na frente", 540, y0 + 50, BLUE, size=24, a=a1, anchor="center", bounds=(170, 910))
    aa = ep(t, C["27.a"], 0.4)
    if aa > 0:
        K.expr(c, f"{MIL} · 3^{{t/2}} = {OITENTA_MIL}", 540, y0 + 140, 40, aa, cores={0: AMBER, 1: AMBER, 3: PURPLE})
        pill(c, "divida por 1 000", 540, y0 + 210, AMBER, size=22, a=aa, anchor="center", bounds=(170, 910))
        K.expr(c, "3^{t/2} = 81", 540, y0 + 280, 46, ep(t, C["27.a"] + 1.4, 0.4), cores={0: PURPLE})
    ab = ep(t, C["27.b"], 0.4)
    if ab > 0:
        K.expr(c, "3^{t/2} = 3^4", 540, y0 + 390, 46, ab, cores={0: PURPLE, 2: BLUE})
    acc = ep(t, C["27.c"], 0.4)
    if acc > 0:
        K.expr(c, "t/2 = 4", 380, y0 + 510, 44, acc, cores={0: PURPLE, 2: PURPLE})
        rrect(c, 560, y0 + 460, 300, 100, 20, mix("#FFFFFF", GREEN, 0.14), acc)
        text_mid(c, "t = 8 anos", 710, y0 + 510, 40, "black", GREEN, acc)


ALTS7 = [("A", "7 h", "queda linear", RED), ("B", "8 h", "parou em 100", RED), ("C", "12 h", "", GREEN),
         ("D", "16 h", "meia-vida a mais", RED), ("E", "32 h", "8 como nº de meias-vidas", RED)]


def b_q7(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 7 · VOCÊ FAZ", "QUANDO REPETIR A DOSE", GREEN)
    card(c, *CARD_R)
    a0 = ep(t, C["29.a"], 0.4)
    cues_in = {L: C[f"29.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"31.x{L.lower()}"] for L in "ABDE"}
    K.alternativas(c, t, C, ALTS7, 1000, 260, 680, 38, C["30.ok"], "C", cues_in, cues_x, gap=40)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0 * (1 - ep(t, C["30"], 0.3)),
         align="left")
    if t < C["30"]:
        _enunciado(c, [("Logo após a administração de um medicamento, sua concentração no sangue de um paciente é de "
                        "400 mg/L. A partir daí, a concentração cai pela metade a cada 4 horas. O médico orientou que "
                        "uma nova dose seja dada quando a concentração atingir 50 mg/L. A nova dose deve ser dada, após "
                        "a primeira, em", INK)], a0, 236, 28)
        pause_timer(c, t, C["29.end"] - 1.9, 540, 700)
        return
    y0 = 206
    a1 = ep(t, C["30"], 0.4)
    rrect(c, 170, y0, 740, 830 - y0, 18, "#FFFFFF", a1, shadow=True)
    aa = ep(t, C["30.a"], 0.4)
    if aa > 0:
        pill(c, "CAMINHO 1 · conte as metades", 540, y0 + 45, GREEN, size=22, a=aa, anchor="center", bounds=(170, 910))
        for k, v in enumerate(("400", "200", "100", "50")):
            ak = ep(t, C["30.a"] + 0.6 + 0.5 * k, 0.3)
            chip(c, v, 260 + k * 190, y0 + 125, BLUE if k < 3 else GREEN, ak, size=36, w=130)
            if k > 0:
                text(c, "metade", 165 + k * 190, y0 + 85, 18, "black", GRAY, ak)
        ak = ep(t, C["30.a"] + 3.0, 0.4)
        if ak > 0:
            linha(c, [("3 meias-vidas · 3 × 4 = ", INK), ("12 h", GREEN)], 540, y0 + 210, 32, ak)
    ab = ep(t, C["30.b"], 0.4)
    if ab > 0:
        pill(c, "CAMINHO 2 · a equação", 540, y0 + 280, PURPLE, size=22, a=ab, anchor="center", bounds=(170, 910))
        K.expr(c, "400 · (1/2)^{t/4} = 50", 540, y0 + 360, 40, ab, cores={0: AMBER, 2: PURPLE})
        K.expr(c, "(1/2)^{t/4} = 1/8 = (1/2)^3", 540, y0 + 460, 38, ep(t, C["30.b"] + 2.6, 0.4),
               cores={0: PURPLE, 4: BLUE})
    acc = ep(t, C["30.c"], 0.4)
    if acc > 0:
        K.expr(c, "t/4 = 3", 380, y0 + 560, 42, acc, cores={0: PURPLE, 2: PURPLE})
        rrect(c, 560, y0 + 515, 300, 90, 20, mix("#FFFFFF", GREEN, 0.14), acc)
        text_mid(c, "t = 12 h", 710, y0 + 560, 38, "black", GREEN, acc)


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "A REVISÃO", PURPLE)
    aa = ep(t, C["33.a"], 0.5)
    if aa > 0:
        regra(c, "JUNTAMOS TUDO", W / 2, 280, aa, 44, PURPLE)
    ab = ep(t, C["33.b"], 0.5)
    if ab > 0:
        selo(c, W / 2, 420, ab, "PEGADINHAS", AMBER, -4, 40)
    acc = ep(t, C["33.c"], 0.5)
    for k, (s_, col) in enumerate((("BIOLOGIA", GREEN), ("QUÍMICA", BLUE), ("FÍSICA", PURPLE))):
        ak = ep(t, C["33.c"] + 0.5 * k, 0.4) if acc > 0 else 0
        if ak > 0:
            x = 560 + k * 400
            rrect(c, x - 170, 540, 340, 130, 24, mix("#FFFFFF", col, 0.14), ak)
            text_mid(c, s_, x, 605, 38, "black", col, ak)
    pill(c, "ep. 6 · revisão da Função exponencial", W / 2, 760, PURPLE, size=26, a=acc, anchor="center")


def b_cta(c, t, C, B):
    cta(c, t, C["34.like"], C["34.sub"], C["34.bell"], C["34.com"], C["34.bye"],
        "Qual dos três erros clássicos você já cometeu?", canal="no Estudativo", anki=C["34.anki"])


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, concreto=b_concreto, ideia=b_ideia, tab1=b_tab1,
              tab2=b_tab2, tab3=b_tab3, atalho_base=b_atalho_base, isolar=b_isolar, atalho_conf=b_atalho_conf,
              evidencia=b_evidencia, atalho_pacote=b_atalho_pacote, naofecha=b_naofecha, ineq1=b_ineq1,
              ineq2=b_ineq2, ladeira=b_ladeira, atalho_sinal=b_atalho_sinal, exercicio=b_exercicio, recap=b_recap,
              contexto=b_contexto, erros=b_erros, q4=b_q4, q7=b_q7, ponte=b_ponte, cta=b_cta)
