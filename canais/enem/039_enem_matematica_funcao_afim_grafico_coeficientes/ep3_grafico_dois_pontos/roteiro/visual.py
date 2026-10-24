"""Visual — Função Afim, Episódio 3: o gráfico (crescente, decrescente, constante) e a lei a partir de dois pontos (tema claro).
Peças comuns da série em ../../comum.py (reexporta o 019/comum.py: alternativas, erro_cards, atalho, selo, regra...).
Peças deste episódio: Plano (eixos com escala própria em x e em y; px/py convertem), escadinha() (degraus de 1 que sobem a),
prego() (ponto como prego que segura a régua), roteiro4() (os 4 passos fixos no canto: a · b · lei · conferir),
termometro() (tubo com as marcas de gelo e fervura), linha() (texto com cor por trecho, mantém o espaço de milhar).
Cores com função: azul = b, onde a reta nasce / definição · roxo = a, a taxa / regra · âmbar = armadilha · verde = atalho ·
vermelho = erro.
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
_s = importlib.util.spec_from_file_location("comum039", _p)
K = importlib.util.module_from_spec(_s); _s.loader.exec_module(K)
K.usar_tempos(Path(__file__).resolve().parents[1] / "audio" / "tempos.json")
motor.set_theme("claro")
frame, head_seq, which, para, regra, selo, pause_timer, chip = (K.frame, K.head_seq, K.which, K.para, K.regra, K.selo,
                                                                K.pause_timer, K.chip)
fmid, ftext, ftext_w = K.fmid, K.ftext, K.ftext_w

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_funcao_afim_ep3_grafico_dois_pontos.mp4"
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


def lei_ab(c, cx, cy, size, a, av, bv, x="x", f="f(x)", align="center"):
    """f(x) = ax + b com o a em roxo e o b em azul; av e bv já formatados (bv com sinal: '+ 5', '− 3')"""
    return linha(c, [(f + " = ", INK), (av, PURPLE), (x, INK), (" " + bv, BLUE)], cx, cy, size, a, align=align)


def defin(c, termo, s, x, y, w, a, col=None, size=30):
    """faixa de definição: TERMO: frase"""
    if a <= 0:
        return
    col = col or BLUE
    rrect(c, x, y, w, 70, 18, mix("#FFFFFF", col, 0.12), a)
    linha(c, [(termo, col), (": " + s, INK)], x + 28, y + 35, size, a, align="left")


class Plano:
    """plano cartesiano num retângulo (x0, y0, w, h) com faixas xr, yr próprias (escala dos eixos)."""

    def __init__(s, x0, y0, w, h, xr, yr):
        s.x0, s.y0, s.w, s.h, s.xr, s.yr = x0, y0, w, h, xr, yr

    def px(s, x):
        return s.x0 + (x - s.xr[0]) / (s.xr[1] - s.xr[0]) * s.w

    def py(s, y):
        return s.y0 + s.h - (y - s.yr[0]) / (s.yr[1] - s.yr[0]) * s.h

    def eixos(s, c, a, xt=(), yt=(), size=22, grade=True, fundo=True, col_y=None, col_x=None, rot=("x", "y")):
        if a <= 0:
            return
        if fundo:
            rrect(c, s.x0 - 60, s.y0 - 30, s.w + 90, s.h + 80, 18, "#FFFFFF", a, shadow=True)
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
        for v in xt:
            if v == 0 and s.yr[0] < 0:
                continue
            text(c, f"{v:g}".replace(".", ","), s.px(v), oy + size + 10, size, "bold", col_x or INK2, a)
        for v in yt:
            if v == 0 and s.xr[0] < 0:
                continue
            text(c, f"{v:g}".replace(".", ","), ox - 12, s.py(v) + size * 0.36, size, "bold", col_y or INK2, a,
                 align="right")

    def reta(s, c, a, m, b, col, u=1.0, width=7):
        """y = m·x + b recortada no retângulo; u = quanto já foi desenhado (0..1)"""
        if a <= 0 or u <= 0:
            return
        c.save()
        c.clipRect(skia.Rect.MakeXYWH(s.x0, s.y0, s.w, s.h))
        xa, xb = s.xr[0], s.xr[1]
        xb_ = xa + (xb - xa) * u
        line(c, s.px(xa), s.py(m * xa + b), s.px(xb_), s.py(m * xb_ + b), col, a, width, cap_round=True)
        c.restore()

    def ponto(s, c, x, y, col, a, rot_=None, dx=18, dy=-30, size=22):
        if a <= 0:
            return
        c.drawCircle(s.px(x), s.py(y), 12, paint("#FFFFFF", a))
        c.drawCircle(s.px(x), s.py(y), 9, paint(col, a))
        if rot_:
            pill(c, rot_, s.px(x) + dx, s.py(y) + dy, col, size=size, a=a, bounds=(0, 1920))


def escadinha(c, P, x0, y0, passos, m, a, col_h=None, col_v=None, prog_=1.0, rot=True, size=24):
    """degraus sobre a reta a partir de (x0, y0): cada um anda 1 em x e sobe m em y (prog_ = 0..1 desenha aos poucos)"""
    if a <= 0:
        return
    col_h, col_v = col_h or INK2, col_v or PURPLE
    for k in range(passos):
        u = clamp(prog_ * passos - k)
        if u <= 0:
            break
        xa, ya = x0 + k, y0 + k * m
        uh, uv = clamp(u * 2), clamp(u * 2 - 1)
        line(c, P.px(xa), P.py(ya), P.px(xa + uh), P.py(ya), col_h, a, 5, dash=(10, 8))
        if uv > 0:
            line(c, P.px(xa + 1), P.py(ya), P.px(xa + 1), P.py(ya + m * uv), col_v, a, 6)
            if rot and k == 0:
                text(c, "1", P.px(xa + 0.5), P.py(ya) + 34, size, "black", INK2, a * uv)


def prego(c, P, x, y, a, col=None):
    """ponto desenhado como um prego (cabeça + sombra)"""
    if a <= 0:
        return
    col = col or INK
    px_, py_ = P.px(x), P.py(y)
    s_ = 0.6 + 0.4 * ease_back(clamp(a))
    c.save(); c.translate(px_, py_); c.scale(s_, s_)
    c.drawCircle(3, 4, 18, paint("#000000", a * 0.15))
    c.drawCircle(0, 0, 17, paint("#8A909C", a))
    c.drawCircle(0, 0, 11, paint(col, a))
    c.drawCircle(-4, -4, 4, paint("#FFFFFF", a * 0.7))
    c.restore()


PASSOS = [("1", "a"), ("2", "b"), ("3", "lei"), ("4", "conferir")]


def roteiro4(c, a, ativo=0, x=980, y=200, w=700):
    """os quatro passos fixos num canto (caixa x..x+w centrada em y); ativo = 1..4 destaca o passo atual"""
    if a <= 0:
        return
    rrect(c, x, y - 32, w, 64, 18, mix("#FFFFFF", INK, 0.04), a, stroke=2, stroke_color=LIGHT)
    ws = [42 + text_w(s_, "black", 26) for _, s_ in PASSOS]
    gap = (w - 40 - sum(ws)) / 3
    xx = x + 20
    for k, ((n_, s_), w_) in enumerate(zip(PASSOS, ws)):
        on_ = (k + 1) == ativo
        col = PURPLE if k == 0 else BLUE if k == 1 else GREEN if k == 3 else INK
        badge_num(c, n_, xx + 16, y, a, 17, bg=col if on_ else LIGHT)
        text(c, s_, xx + 42, y + 9, 26, "black", col if on_ else GRAY, a, align="left")
        xx += w_ + gap


def termometro(c, cx, ytop, h, a, nome, gelo, ferv, col, nivel=0.0):
    """tubo com bulbo; marcas de gelo (embaixo) e fervura (em cima); nivel = 0..1 do líquido"""
    if a <= 0:
        return
    w = 54
    rrect(c, cx - w / 2, ytop, w, h, w / 2, "#FFFFFF", a, shadow=True, stroke=3, stroke_color="#C9CCD3")
    c.drawCircle(cx, ytop + h + 30, 46, paint("#FFFFFF", a))
    c.drawCircle(cx, ytop + h + 30, 46, paint("#C9CCD3", a, stroke=3))
    c.drawCircle(cx, ytop + h + 30, 34, paint(RED, a))
    yb = ytop + h - 30
    yt = ytop + 50
    yl = yb - (yb - yt) * nivel
    rrect(c, cx - 12, yl, 24, ytop + h + 10 - yl, 12, RED, a)
    for yy, v in ((yb, gelo), (yt, ferv)):
        line(c, cx + w / 2 + 6, yy, cx + w / 2 + 40, yy, INK2, a, 4)
        text(c, v, cx + w / 2 + 52, yy + 12, 34, "black", col, a, align="left")
    text(c, nome, cx, ytop - 24, 34, "black", col, a)


# ======================================================================
# abertura
# ======================================================================

def dois_graficos(c, a, ab_rot=0.0, conta=0.0, conta2=0.0, y0=250, h=420):
    """os dois gráficos do gancho: esquerda y 0–10 (a = 2, parece íngreme); direita y 0–100 (a = 10, parece deitada)"""
    if a <= 0:
        return
    PE = Plano(300, y0, 520, h, (0, 5), (0, 10))
    PD = Plano(1140, y0, 520, h, (0, 5), (0, 100))
    PE.eixos(c, a, xt=range(0, 6), yt=range(0, 11, 2), col_y=mix(INK2, AMBER, ab_rot))
    PD.eixos(c, a, xt=range(0, 6), yt=range(0, 101, 20), col_y=mix(INK2, AMBER, ab_rot))
    PE.reta(c, a, 2, 0, PURPLE)
    PD.reta(c, a, 10, 0, PURPLE)
    if ab_rot > 0:
        for P in (PE, PD):
            rrect(c, P.x0 - 58, P.y0 - 10, 46, P.h + 20, 12, AMBER, 0.14 * ab_rot)
    if conta > 0:
        line(c, PE.px(0), PE.py(0), PE.px(5), PE.py(0), INK2, conta, 5, dash=(10, 8))
        line(c, PE.px(5), PE.py(0), PE.px(5), PE.py(10), PURPLE, conta, 6)
        pill(c, "sobe 10", PE.px(5) - 20, PE.py(5), PURPLE, size=24, a=conta, anchor="right", bounds=(0, 1920))
        linha(c, [("a = 10 ÷ 5 = ", INK), ("2", PURPLE)], PE.px(2.5), y0 + h + 110, 40, conta)
    if conta2 > 0:
        line(c, PD.px(0), PD.py(0), PD.px(5), PD.py(0), INK2, conta2, 5, dash=(10, 8))
        line(c, PD.px(5), PD.py(0), PD.px(5), PD.py(50), PURPLE, conta2, 6)
        pill(c, "sobe 50", PD.px(5) - 20, PD.py(25), PURPLE, size=24, a=conta2, anchor="right", bounds=(0, 1920))
        linha(c, [("a = 50 ÷ 5 = ", INK), ("10", PURPLE)], PD.px(2.5), y0 + h + 110, 40, conta2)
    return PE, PD


def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "FUNÇÃO AFIM · EPISÓDIO 3", BLUE)
    aa = ep(t, C["01.a"], 0.5)
    ab = ep(t, C["01.b"], 0.5)
    dois_graficos(c, aa, ab_rot=ab, conta=ep(t, C["01.b"] + 1.4, 0.5), conta2=ep(t, C["01.b"] + 2.4, 0.5), y0=230,
                  h=400)
    if aa > 0:
        pill(c, "parece MUITO mais íngreme", 560, 205, AMBER, size=24, a=aa * (1 - ab), anchor="center")
    if ab > 0:
        selo(c, 1330, 300, ab, "SOBE MAIS RÁPIDO", GREEN, -3, 26)
    acc = ep(t, C["01.c"], 0.5)
    if acc > 0:
        regra(c, "OLHO ENGANA · CONTA NÃO", W / 2, 815, acc, 40)


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "FUNÇÃO AFIM · EP. 3", "AO FINAL DESTA AULA", GREEN)
    a0 = ep(t, C["02"], 0.4)
    if a0 > 0:
        pill(c, "3º episódio da série de FUNÇÃO AFIM", W / 2, 240, BLUE, size=30, a=a0, anchor="center")
    itens = [("02.a", "SINAL DE a", "e o VALOR de b, no gráfico", PURPLE), ("02.b", "A LEI", "a partir de 2 pontos", BLUE),
             ("02.c", "CONFERIR", "com o outro ponto", GREEN)]
    for k, (cue, tit, sub, col) in enumerate(itens):
        ak = ep(t, C[cue], 0.5)
        if ak <= 0:
            continue
        x = 440 + k * 520
        rrect(c, x - 230, 330, 460, 330, 26, "#FFFFFF", ak, shadow=True)
        rrect(c, x - 230, 330, 460, 70, 26, col, ak * 0.16)
        badge_num(c, k + 1, x, 470, ak, 34, bg=col)
        text(c, tit, x, 570, 42, "black", col, ak)
        text(c, sub, x, 625, 28, "bold", INK2, ak)


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "DOIS LEMBRETES", "EM 30 SEGUNDOS", GREEN)
    aa = ep(t, C["03.a"], 0.5)
    if aa > 0:
        pill(c, "série de Conceito de Função", 300, 250, BLUE, size=22, a=aa, bounds=(0, 1920))
        P = Plano(380, 330, 420, 380, (0, 5), (0, 5))
        P.eixos(c, aa, xt=range(0, 6), yt=range(0, 6))
        line(c, P.px(3), P.py(0), P.px(3), P.py(2), BLUE, aa, 4, dash=(8, 7))
        line(c, P.px(0), P.py(2), P.px(3), P.py(2), BLUE, aa, 4, dash=(8, 7))
        P.ponto(c, 3, 2, BLUE, ep(t, C["03.a"] + 2.6, 0.4), "(3, 2)")
        text(c, "x: o deitado", 940, 470, 34, "black", INK, ep(t, C["03.a"] + 0.8, 0.4), align="left")
        text(c, "y: o em pé", 940, 530, 34, "black", INK, ep(t, C["03.a"] + 1.6, 0.4), align="left")
        linha(c, [("par ordenado: ", INK2), ("(x, y)", BLUE)], 940, 600, 34, ep(t, C["03.a"] + 2.6, 0.4), align="left")
    ab = ep(t, C["03.b"], 0.5)
    if ab > 0:
        rrect(c, 920, 660, 760, 140, 24, mix("#FFFFFF", PURPLE, 0.10), ab)
        pill(c, "episódio 2", 940, 660, PURPLE, size=22, a=ab, bounds=(0, 1920))
        linha(c, [("a = ", PURPLE)], 1150, 735, 56, ab)
        K.fr(c, "Δy", "Δx", 1260, 735, 50, PURPLE, ab)
        text(c, "quanto y muda ÷ quanto x mudou", 1330, 745, 24, "bold", INK2, ab, align="left")


def b_escada(c, t, C, B):
    head(c, t, B["start"], "A RETA É UMA ESCADA", "DA ESQUERDA PARA A DIREITA", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["04.t"], 0.5)
    P = Plano(260, 230, 760, 540, (0, 6), (0, 12))
    P.eixos(c, aa, xt=range(0, 7), yt=range(0, 13, 2), fundo=False)
    if aa > 0:
        arrow(c, 300, 205, 520, 205, GRAY, aa, 3, 12)
        text(c, "leia assim", 540, 214, 24, "bold", GRAY, aa, align="left")
    ua = ep(t, C["04.a"], 1.0)
    P.reta(c, aa, 2, 1, PURPLE, u=ua)
    escadinha(c, P, 0, 1, 5, 2, ep(t, C["04.b"], 0.4), prog_=ep(t, C["04.b"], 3.0))
    ab = ep(t, C["04.b"], 0.5)
    if ab > 0:
        rrect(c, 1100, 250, 580, 210, 24, "#FFFFFF", ab, shadow=True)
        text(c, "CADA DEGRAU", 1390, 310, 30, "black", INK, ab)
        linha(c, [("anda ", INK2), ("1", INK), ("  ·  sobe ", INK2), ("a", PURPLE)], 1390, 390, 48, ab)
    acc = ep(t, C["04.c"], 0.5)
    if acc > 0:
        Q = Plano(1180, 520, 260, 170, (0, 4), (0, 8))
        rrect(c, 1100, 490, 580, 230, 24, "#FFFFFF", acc, shadow=True)
        Q.reta(c, acc, -1.5, 7, RED, width=6)
        for k in range(3):
            line(c, Q.px(k), Q.py(7 - 1.5 * k), Q.px(k + 1), Q.py(7 - 1.5 * k), INK2, acc, 4, dash=(8, 6))
            line(c, Q.px(k + 1), Q.py(7 - 1.5 * k), Q.px(k + 1), Q.py(7 - 1.5 * (k + 1)), RED, acc, 5)
        text(c, "a negativo:", 1560, 590, 28, "black", INK, acc)
        text(c, "o degrau DESCE", 1560, 640, 28, "black", RED, acc)
    ad = ep(t, C["04.d"], 0.5)
    defin(c, "INCLINAÇÃO", "o quanto a reta sobe", 1100, 750, 580, ad, size=28)


# ======================================================================
# bloco a — o sinal de a
# ======================================================================

def b_sinal(c, t, C, B):
    head(c, t, B["start"], "O SINAL DO a", "SOBE, DEITA OU DESCE", PURPLE)
    card(c, *CARD_R)
    a0 = ep(t, C["05.t"], 0.5)
    P = Plano(250, 220, 640, 560, (-1, 5), (-3, 7))
    P.eixos(c, a0, xt=range(-1, 6), yt=range(-2, 8, 2), fundo=False)
    tb, tc, td = C["05.b"], C["05.c"], C["05.d"]
    # a gira em torno de (0, 2): 1,5 → 0 → −1,5
    m = 1.5 * ep(t, tb, 0.8) - 1.5 * ep(t, tc, 1.0) - 1.5 * ep(t, td, 1.0)
    col = GREEN if t < tc else (INK if t < td else RED)
    if t >= tc:
        P.reta(c, a0, 1.5, 2, GREEN, width=4)
    if t >= td:
        P.reta(c, a0, 0, 2, INK, width=4)
    P.reta(c, ep(t, tb, 0.5), m, 2, col)
    P.ponto(c, 0, 2, BLUE, ep(t, C["05.a"], 0.4), "b", dx=-60)
    aa = ep(t, C["05.a"], 0.5)
    if aa > 0:
        rrect(c, 980, 210, 700, 100, 22, mix("#FFFFFF", PURPLE, 0.10), aa)
        text_mid(c, "quem decide: o SINAL do a", 1330, 260, 36, "black", PURPLE, aa)
    rows = [("05.b", "a > 0", "SOBE", "CRESCENTE", "x aumenta → y aumenta", GREEN),
            ("05.c", "a = 0", "DEITADA", "CONSTANTE", "o y não muda", INK),
            ("05.d", "a < 0", "DESCE", "DECRESCENTE", "x aumenta → y diminui", RED)]
    for k, (cue, cond, mov, nome, sub, colr) in enumerate(rows):
        ak = ep(t, C[cue], 0.5)
        if ak <= 0:
            continue
        y = 340 + k * 160
        rrect(c, 980, y, 700, 140, 22, "#FFFFFF", ak, shadow=True)
        rrect(c, 980, y, 16, 140, 8, colr, ak)
        text(c, cond, 1030, y + 60, 44, "black", PURPLE, ak, align="left")
        text(c, mov, 1030, y + 112, 26, "black", colr, ak, align="left")
        text(c, "função " + nome.lower(), 1240, y + 58, 32, "black", colr, ak, align="left")
        text(c, sub, 1240, y + 106, 26, "bold", INK2, ak, align="left")


# ======================================================================
# bloco b — o tamanho de a e o b
# ======================================================================

def b_tamanho(c, t, C, B):
    head(c, t, B["start"], "O TAMANHO DO a E O b", "ÍNGREME OU DESLIZANDO", PURPLE)
    card(c, *CARD_R)
    a0 = ep(t, C["06.t"], 0.5)
    P = Plano(250, 220, 640, 560, (-1, 5), (-3, 9))
    P.eixos(c, a0, xt=range(-1, 6), yt=range(-2, 10, 2), fundo=False)
    tc = C["06.c"]
    aa = ep(t, C["06.a"], 0.5)
    if t < tc:
        for k, (m, ak) in enumerate(((0.5, aa), (1, ep(t, C["06.a"] + 1.0, 0.4)), (3, ep(t, C["06.b"], 0.5)))):
            P.reta(c, ak, m, 1, mix(PURPLE, "#FFFFFF", 0.45 - 0.2 * k), width=5 + 2 * k)
            if ak > 0:
                xl = min(4.2, (8.5 - 1) / m)
                pill(c, f"a = {m:g}".replace(".", ","), P.px(xl) + 10, P.py(m * xl + 1), PURPLE, size=22, a=ak,
                     bounds=(0, 1920))
    else:
        # o b desliza: a reta y = 2x + b sobe e desce
        u = t - tc
        bv = 1 + 2.5 * math.sin(min(u, 5.5) * 1.15)
        ac = ep(t, tc, 0.4)
        for gb in (-1, 3.5):
            P.reta(c, ac * 0.5, 2, gb, LIGHT, width=4)
        P.reta(c, ac, 2, bv, PURPLE)
        P.ponto(c, 0, bv, BLUE, ac, None)
        ad = ep(t, C["06.d"], 0.5)
        if ad > 0:
            pill(c, "b: onde NASCE", P.px(0) + 22, P.py(bv) + 34, BLUE, size=24, a=ad, bounds=(0, 1920))
            xa = 2.4
            arrow(c, P.px(xa), P.py(2 * xa + bv), P.px(xa + 0.7), P.py(2 * (xa + 0.7) + bv), PURPLE, ad, 6, 18)
            pill(c, "a: para onde APONTA", P.px(xa) - 14, P.py(2 * xa + bv) - 6, PURPLE, size=24, a=ad, anchor="right",
                 bounds=(0, 1920))
    if aa > 0:
        rrect(c, 980, 220, 700, 200, 22, "#FFFFFF", aa, shadow=True)
        text(c, "MÓDULO DE a  ·  |a|", 1330, 280, 32, "black", BLUE, aa)
        text(c, "o número sem o sinal", 1330, 330, 28, "bold", INK2, aa)
        linha(c, [("|−4| = ", INK), ("4", PURPLE)], 1330, 385, 40, aa)
    ab = ep(t, C["06.b"], 0.5)
    if ab > 0:
        regra(c, "|a| MAIOR → RETA MAIS EM PÉ", 1330, 480, ab, 30)
    acc = ep(t, tc, 0.5)
    if acc > 0:
        rrect(c, 980, 560, 700, 120, 22, mix("#FFFFFF", BLUE, 0.10), acc)
        text_mid(c, "o b só DESLOCA (sobe ou desce)", 1330, 620, 32, "black", BLUE, acc)
    ad = ep(t, C["06.d"], 0.5)
    if ad > 0:
        linha(c, [("b", BLUE), (" = onde nasce  ·  ", INK2), ("a", PURPLE), (" = para onde aponta", INK2)], 1330, 740, 32, ad)


def b_contexto(c, t, C, B):
    head(c, t, B["start"], "E NUMA QUESTÃO?", "O GRÁFICO EM CONTEXTO", BLUE)
    card(c, *CARD_R)
    rows = [("07.a", "a > 0", "reta SOBE", "a conta que cresce com o consumo", 1.0, 1),
            ("07.b", "a < 0", "reta DESCE", "vela · reservatório · carro", -1.0, 1),
            ("07.c", "|a| maior", "mais ÍNGREME", "a tarifa por km mais cara", 2.6, 0.4),
            ("07.d", "b maior", "mais ALTA no eixo y", "parte fixa maior", 0.6, 3)]
    for k, (cue, cond, graf, ctx, m, b0) in enumerate(rows):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        y = 210 + k * 150 + d
        rrect(c, 220, y, 1480, 130, 22, "#FFFFFF", a, shadow=True)
        text(c, cond, 260, y + 82, 44, "black", PURPLE if "a" in cond else BLUE, a, align="left")
        Q = Plano(560, y + 20, 160, 90, (0, 4), (0, 5))
        line(c, Q.x0, Q.y0 + Q.h, Q.x0 + Q.w, Q.y0 + Q.h, LIGHT, a, 3)
        line(c, Q.x0, Q.y0 + Q.h, Q.x0, Q.y0, LIGHT, a, 3)
        Q.reta(c, a, m, b0 if m >= 0 else 4.6, PURPLE if k < 3 else BLUE, width=5)
        if k == 3:
            Q.reta(c, a * 0.6, m, 0.6, LIGHT, width=4)
        text(c, graf, 780, y + 78, 32, "black", INK, a, align="left")
        text(c, ctx, 1680, y + 78, 28, "bold", INK2, a, align="right")


def b_olhadas(c, t, C, B):
    head(c, t, B["start"], "ATALHO", "LEIA O GRÁFICO EM DUAS OLHADAS", GREEN)
    card(c, *CARD_R)
    aa = ep(t, C["08.a"], 0.5)
    K.atalho(c, 1000, 200, 700, 150, "ATALHO", ["2 olhadas: b e a"], aa, 40)
    a0 = ep(t, C["08.t"], 0.5)
    P = Plano(300, 230, 560, 540, (0, 4), (0, 14))
    P.eixos(c, a0, xt=range(0, 5), yt=range(0, 15, 2), fundo=False)
    P.reta(c, a0, 2, 5, PURPLE)
    ab = ep(t, C["08.b"], 0.5)
    if ab > 0:
        c.drawCircle(P.px(0), P.py(5), 26, paint(BLUE, ab * 0.25))
        P.ponto(c, 0, 5, BLUE, ab, "b = 5", dx=24, dy=48)
        rrect(c, 1000, 390, 700, 120, 22, mix("#FFFFFF", BLUE, 0.10), ab)
        linha(c, [("1ª: corta o eixo vertical  →  ", INK), ("b", BLUE)], 1350, 450, 32, ab)
    acc = ep(t, C["08.c"], 0.5)
    if acc > 0:
        escadinha(c, P, 0, 5, 1, 2, acc, prog_=ep(t, C["08.c"], 1.2))
        pill(c, "sobe 2", P.px(1) + 16, P.py(6), PURPLE, size=24, a=ep(t, C["08.c"] + 1.2, 0.4), bounds=(0, 1920))
        rrect(c, 1000, 540, 700, 120, 22, mix("#FFFFFF", PURPLE, 0.10), acc)
        linha(c, [("2ª: anda 1, quanto subiu  →  ", INK), ("a", PURPLE)], 1350, 600, 32, acc)
    ad = ep(t, C["08.d"], 0.5)
    if ad > 0:
        rrect(c, 1000, 690, 700, 110, 22, "#FFFFFF", ad, shadow=True)
        lei_ab(c, 1350, 745, 50, ad, "2", "+ 5")


# ======================================================================
# bloco c — a escala
# ======================================================================

def b_escala(c, t, C, B):
    head(c, t, B["start"], "A ESCALA DOS EIXOS", "OS GRÁFICOS DO COMEÇO", AMBER)
    aa = ep(t, C["09.a"], 0.5)
    dois_graficos(c, ep(t, C["09.t"], 0.5), ab_rot=aa, conta=ep(t, C["09.b"], 0.5), conta2=ep(t, C["09.c"], 0.5), y0=290,
                  h=330)
    if aa > 0:
        defin(c, "ESCALA DOS EIXOS", "quanto vale cada pedacinho do eixo", 360, 150, 1200, aa, AMBER, 28)
    ad = ep(t, C["09.d"], 0.5)
    if ad > 0:
        regra(c, "A OLHO, SÓ NO MESMO PAR DE EIXOS", W / 2, 815, ad, 36)


# ======================================================================
# bloco d — a lei a partir de dois pontos
# ======================================================================

def b_pregos(c, t, C, B):
    sid = which(t, C, ["10", "11"])
    head_seq(c, t, C, [("10", "DOIS PONTOS BASTAM", "COMO 2 PREGOS SEGURAM A RÉGUA", BLUE),
                       ("11", "A LEI EM 4 PASSOS", "(2, 11) e (5, 20)", BLUE)])
    card(c, *CARD_R)
    a0 = ep(t, C["10.t"], 0.5)
    P = Plano(260, 230, 600, 540, (0, 6), (0, 24))
    P.eixos(c, a0, xt=range(0, 7), yt=range(0, 25, 4), fundo=False)
    aa = ep(t, C["10.a"], 0.5)
    prego(c, P, 2, 11, aa, BLUE)
    prego(c, P, 5, 20, ep(t, C["10.a"] + 0.5, 0.4), BLUE)
    # a régua cai sobre os pregos
    ur = ep(t, C["10.a"] + 1.2, 0.8)
    if ur > 0:
        c.save()
        c.clipRect(skia.Rect.MakeXYWH(P.x0, P.y0, P.w, P.h))
        x1, x2 = 0.3, 5.9
        line(c, P.px(x1), P.py(3 * x1 + 5) - 40 * (1 - ur), P.px(x2), P.py(3 * x2 + 5) - 40 * (1 - ur),
             mix(PURPLE, "#FFFFFF", 0.15), ur, 12)
        c.restore()
    ab = ep(t, C["10.b"], 0.5)
    if ab > 0:
        pill(c, "(2, 11)", P.px(2) - 20, P.py(11) - 36, BLUE, size=24, a=ab, anchor="right", bounds=(0, 1920))
        pill(c, "(5, 20)", P.px(5) - 26, P.py(20) - 38, BLUE, size=24, a=ab, anchor="right", bounds=(0, 1920))
    # a escadinha: degrau horizontal 3, vertical 9
    acc = ep(t, C["10.c"], 0.5)
    if acc > 0:
        uh = ep(t, C["10.c"] + 1.0, 0.8)
        uv = ep(t, C["10.c"] + 2.6, 0.8)
        line(c, P.px(2), P.py(11), P.px(2 + 3 * uh), P.py(11), INK2, acc, 6, dash=(12, 8))
        if uh > 0:
            text(c, "anda 3", P.px(3.5), P.py(11) + 40, 26, "black", INK, uh)
        if uv > 0:
            line(c, P.px(5), P.py(11), P.px(5), P.py(11 + 9 * uv), PURPLE, acc, 7)
            text(c, "sobe 9", P.px(5) + 18, P.py(15.5) + 10, 26, "black", PURPLE, uv, align="left")
    ad = ep(t, C["10.d"], 0.5)
    if ad > 0 and sid == "10":
        escadinha(c, P, 2, 11, 3, 3, ad * 0.8, col_h=GREEN, col_v=GREEN, prog_=ep(t, C["10.d"] + 1.6, 1.6), rot=False)
    # coluna da direita: o roteiro dos 4 passos
    roteiro4(c, ep(t, C["10.b"], 0.5), 1 if t < C["11.a"] else 2 if t < C["11.b"] else 3 if t < C["11.c"] else 4)
    if acc > 0:
        rrect(c, 980, 255, 700, 135, 22, mix("#FFFFFF", PURPLE, 0.08), acc)
        badge_num(c, 1, 1020, 322, acc, 22, bg=PURPLE)
        text(c, "a = ", 1070, 343, 48, "black", PURPLE, acc, align="left")
        K.fr(c, "20 − 11", "5 − 2", 1290, 322, 40, INK, acc)
        if ad > 0:
            linha(c, [("= ", INK)], 1420, 322, 44, ad)
            K.fr(c, "9", "3", 1475, 322, 44, INK, ad)
            linha(c, [("= ", INK), ("3", PURPLE)], 1570, 322, 48, ad)
    if sid == "10":
        if ad > 0:
            pill(c, "3 degraus · cada um sobe 3", 1330, 440, GREEN, size=26, a=ep(t, C["10.d"] + 1.6, 0.4),
                 anchor="center")
        return
    a1 = ep(t, C["11.a"], 0.5)
    if a1 > 0:
        rrect(c, 980, 410, 700, 140, 22, mix("#FFFFFF", BLUE, 0.08), a1)
        badge_num(c, 2, 1020, 480, a1, 22, bg=BLUE)
        linha(c, [("11 = 3 · 2 + ", INK), ("b", BLUE)], 1070, 450, 38, a1, align="left")
        linha(c, [("11 = 6 + b  →  ", INK2), ("b = 5", BLUE)], 1070, 510, 38, ep(t, C["11.a"] + 2.4, 0.4), align="left")
    a2 = ep(t, C["11.b"], 0.5)
    if a2 > 0:
        rrect(c, 980, 570, 700, 100, 22, "#FFFFFF", a2, shadow=True)
        badge_num(c, 3, 1020, 620, a2, 22, bg=INK)
        lei_ab(c, 1070, 620, 46, a2, "3", "+ 5", align="left")
    a3 = ep(t, C["11.c"], 0.5)
    if a3 > 0:
        rrect(c, 980, 690, 700, 110, 22, mix("#FFFFFF", GREEN, 0.12), a3)
        badge_num(c, 4, 1020, 745, a3, 22, bg=GREEN)
        linha(c, [("f(5) = 3 · 5 + 5 = ", INK), ("20", GREEN)], 1070, 745, 38, a3, align="left")
        check_icon(c, 1630, 745, 24, ep(t, C["11.c"] + 2.6, 0.4), GREEN)
        P.ponto(c, 5, 20, GREEN, ep(t, C["11.c"] + 2.6, 0.4), None)


def b_quarto(c, t, C, B):
    head(c, t, B["start"], "ATALHO", "O QUARTO PASSO É O SEGURO", GREEN)
    card(c, *CARD_R)
    roteiro4(c, ep(t, C["12.t"], 0.4), 4, 560, 785, 800)
    aa = ep(t, C["12.a"], 0.5)
    K.atalho(c, 260, 200, 1400, 150, "ATALHO", ["o ponto que você NÃO usou confere a lei"], aa, 40)
    ab = ep(t, C["12.b"], 0.5)
    if ab > 0:
        for k, (pt, uso, col) in enumerate((("(2, 11)", "usado para achar o b", BLUE),
                                            ("(5, 20)", "livre: a PROVA REAL", GREEN))):
            x = 600 + k * 720
            rrect(c, x - 320, 410, 640, 200, 24, "#FFFFFF", ab, shadow=True)
            text(c, pt, x, 490, 56, "black", col, ab)
            text(c, uso, x, 560, 30, "bold", INK2, ab)
    acc = ep(t, C["12.c"], 0.5)
    if acc > 0:
        regra(c, "NÃO PASSOU? ERRO DE SINAL OU DE FRAÇÃO", W / 2, 680, acc, 34, RED)


# ======================================================================
# bloco e — atalhos do b
# ======================================================================

def b_atalhob(c, t, C, B):
    head(c, t, B["start"], "QUANDO x = 0", "O b JÁ VEM DE PRESENTE", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["13.a"], 0.5)
    P = Plano(300, 240, 460, 440, (0, 4), (0, 12))
    P.eixos(c, ep(t, C["13.t"], 0.5), xt=range(0, 5), yt=range(0, 13, 2), fundo=False)
    if aa > 0:
        P.reta(c, aa, 2, 4, PURPLE)
        c.drawCircle(P.px(0), P.py(4), 26, paint(BLUE, aa * 0.25))
        P.ponto(c, 0, 4, BLUE, aa, "(0, 4) → b = 4", dx=24, dy=50)
    ab = ep(t, C["13.b"], 0.5)
    if ab > 0:
        rrect(c, 900, 230, 780, 330, 24, "#FFFFFF", ab, shadow=True)
        pill(c, "OUTRO CAMINHO: o sistema", 930, 230, PURPLE, size=24, a=ab, bounds=(0, 1920))
        linha(c, [("5", INK), ("a", PURPLE), (" + ", INK), ("b", BLUE), (" = 20", INK)], 1290, 330, 48, ab)
        linha(c, [("2", INK), ("a", PURPLE), (" + ", INK), ("b", BLUE), (" = 11", INK)], 1290, 410, 48, ab)
    acc = ep(t, C["13.c"], 0.5)
    if acc > 0:
        line(c, 1120, 455, 1460, 455, INK, acc, 4)
        text(c, "−", 1090, 425, 48, "black", INK, acc)
        linha(c, [("3", INK), ("a", PURPLE), (" = 9", INK), ("   (o b some)", INK2)], 1290, 510, 44, acc)
        pill(c, "série de Sistemas de equações lineares", 1290, 640, PURPLE, size=24, a=acc, anchor="center")


# ======================================================================
# bloco f — os termômetros
# ======================================================================

def b_termometro(c, t, C, B):
    head(c, t, B["start"], "DOIS TERMÔMETROS", "A FÓRMULA É UMA RETA", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["14.a"], 0.5)
    nivel = 0.5 + 0.5 * math.sin((t - C["14.a"]) * 0.9) if t >= C["14.a"] else 0.0
    termometro(c, 340, 280, 400, aa, "°C", "0", "100", INK, nivel)
    termometro(c, 620, 280, 400, ep(t, C["14.a"] + 0.6, 0.5), "°F", "32", "212", PURPLE, nivel)
    defin(c, "ESCALA TERMOMÉTRICA", "um jeito de numerar a temperatura", 190, 760, 740, aa, BLUE, 22)
    ab = ep(t, C["14.b"], 0.5)
    if ab > 0:
        for k, (onde, pt) in enumerate((("gelo derretendo", "(0, 32)"), ("água fervendo", "(100, 212)"))):
            y = 230 + k * 120
            rrect(c, 960, y, 720, 100, 22, "#FFFFFF", ab, shadow=True)
            text(c, onde, 1000, y + 62, 30, "bold", INK2, ab, align="left")
            text(c, pt, 1640, y + 64, 40, "black", BLUE, ab, align="right")
    acc = ep(t, C["14.c"], 0.5)
    if acc > 0:
        rrect(c, 960, 480, 720, 140, 22, mix("#FFFFFF", PURPLE, 0.08), acc)
        linha(c, [("b = ", INK), ("32", BLUE)], 1080, 550, 40, acc)
        text(c, "a = ", 1240, 564, 40, "black", PURPLE, acc, align="left")
        K.fr(c, "180", "100", 1370, 550, 38, INK, acc)
        linha(c, [("= ", INK), ("1,8", PURPLE)], 1500, 550, 40, acc)
    ad = ep(t, C["14.d"], 0.5)
    if ad > 0:
        rrect(c, 960, 650, 720, 150, 22, "#FFFFFF", ad, shadow=True)
        linha(c, [("F = ", INK), ("1,8", PURPLE), ("C", INK), (" + 32", BLUE)], 1320, 705, 52, ad)
        text(c, "a fórmula decorada = reta por 2 pontos", 1320, 775, 24, "bold", INK2, ad)


def b_tangente(c, t, C, B):
    head(c, t, B["start"], "UM RECADO", "SÓ PARA CITAR", GRAY)
    card(c, *CARD_R)
    aa = ep(t, C["15.a"], 0.5)
    P = Plano(320, 260, 480, 420, (0, 5), (0, 5))
    P.eixos(c, ep(t, C["15.t"], 0.5), xt=range(0, 6), yt=range(0, 6), fundo=False, grade=False)
    if aa > 0:
        P.reta(c, aa, 0.8, 0.5, PURPLE)
        P.reta(c, aa, 0.8, 2.3, PURPLE)
        r = 70
        x0, y0 = P.px(-0.5 / 0.8 + 0.0001), P.py(0)
        ang = math.degrees(math.atan2(P.py(0) - P.py(0.8), P.px(1) - P.px(0)))
        arc = skia.Path(); arc.addArc(skia.Rect.MakeXYWH(P.px(0) - r, P.py(0.5) - r, 2 * r, 2 * r), -ang, ang)
        c.drawPath(arc, paint(AMBER, aa, stroke=5))
        text(c, "ângulo", P.px(0) + r + 16, P.py(0.5) - 6, 24, "black", AMBER, aa, align="left")
        rrect(c, 920, 260, 760, 240, 24, "#FFFFFF", aa, shadow=True)
        text(c, "a = tangente do ângulo", 1300, 340, 36, "black", PURPLE, aa)
        text(c, "mesmo a  →  retas PARALELAS", 1300, 420, 32, "bold", INK2, aa)
    ab = ep(t, C["15.b"], 0.5)
    if ab > 0:
        pill(c, "série própria · Geometria Analítica", 1300, 580, GRAY, size=30, a=ab, anchor="center")


# ======================================================================
# nós fazemos
# ======================================================================

def b_exercicio(c, t, C, B):
    head_seq(c, t, C, [("16", "SUA VEZ", "PAUSE E TENTE", GREEN), ("17", "VAMOS JUNTOS", "OS QUATRO PASSOS", GREEN)])
    card(c, *CARD_R)
    aa = ep(t, C["16.a"], 0.5)
    P = Plano(300, 240, 520, 520, (0, 4), (0, 12))
    P.eixos(c, aa, xt=range(0, 5), yt=range(0, 13, 2), fundo=False)
    P.ponto(c, 1, 4, BLUE, aa, "(1, 4)")
    P.ponto(c, 3, 10, BLUE, ep(t, C["16.a"] + 0.8, 0.4), "(3, 10)", dx=-120)
    if aa > 0 and t < C["17"]:
        rrect(c, 980, 270, 700, 150, 22, "#FFFFFF", aa, shadow=True)
        text_mid(c, "f(x) = ?", 1330, 345, 64, "black", AMBER, aa)
    roteiro4(c, ep(t, C["16.b"], 0.5), 0 if t < C["17"] else 1 if t < C["17.b"] else 2 if t < C["17.c"] else 3 if t < C["17.d"] else 4)
    if t < C["17"]:
        pause_timer(c, t, C["16.end"] - 1.9, 1330, 560)
        return
    aa2 = ep(t, C["17.a"], 0.5)
    if aa2 > 0:
        escadinha(c, P, 1, 4, 2, 3, aa2, prog_=ep(t, C["17.a"], 2.0))
        rrect(c, 980, 255, 700, 135, 22, mix("#FFFFFF", PURPLE, 0.08), aa2)
        badge_num(c, 1, 1020, 322, aa2, 22, bg=PURPLE)
        text(c, "a = ", 1070, 342, 46, "black", PURPLE, aa2, align="left")
        K.fr(c, "10 − 4", "3 − 1", 1270, 322, 38, INK, aa2)
        linha(c, [("= ", INK)], 1390, 322, 44, aa2)
        K.fr(c, "6", "2", 1440, 322, 42, INK, aa2)
        linha(c, [("= ", INK), ("3", PURPLE)], 1530, 322, 46, aa2)
    ab = ep(t, C["17.b"], 0.5)
    if ab > 0:
        rrect(c, 980, 410, 700, 110, 22, mix("#FFFFFF", BLUE, 0.08), ab)
        badge_num(c, 2, 1020, 465, ab, 22, bg=BLUE)
        linha(c, [("4 = 3 · 1 + b  →  ", INK), ("b = 1", BLUE)], 1070, 465, 38, ab, align="left")
    acc = ep(t, C["17.c"], 0.5)
    if acc > 0:
        P.reta(c, acc, 3, 1, PURPLE, u=ep(t, C["17.c"], 1.0))
        rrect(c, 980, 540, 700, 110, 22, "#FFFFFF", acc, shadow=True)
        badge_num(c, 3, 1020, 595, acc, 22, bg=INK)
        lei_ab(c, 1070, 595, 46, acc, "3", "+ 1", align="left")
    ad = ep(t, C["17.d"], 0.5)
    if ad > 0:
        rrect(c, 980, 670, 700, 110, 22, mix("#FFFFFF", GREEN, 0.12), ad)
        badge_num(c, 4, 1020, 725, ad, 22, bg=GREEN)
        linha(c, [("f(3) = 3 · 3 + 1 = ", INK), ("10", GREEN)], 1070, 725, 38, ad, align="left")
        check_icon(c, 1630, 725, 24, ep(t, C["17.d"] + 2.0, 0.4), GREEN)


# ======================================================================
# recap, erros
# ======================================================================

FRASES = ["a positivo sobe; a negativo desce; a zero fica deitado.",
          "b é onde a reta corta o eixo vertical.",
          "Dois pontos dão a lei; o terceiro dado confere."]


def b_recap(c, t, C, B):
    sid = which(t, C, ["18", "28"])
    frame(c, t, B["start"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "18" else "PARA FECHAR", PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 300 + k * 180 + d
        badge_num(c, k + 1, 260, y - 16, a, 36, bg=PURPLE)
        para(c, s, 320, y, 50, "black", INK, a, 1360, 60)


ERROS = [("Trocar a e b: a reta nasce no 5 e sobe 2, e a pessoa escreve f(x) = 5x + 2",
          "o 5 aparece primeiro, e os dois números estão ali",
          "o b é onde nasce e o a é o degrau: f(x) = 2x + 5"),
         ("Comparar inclinações A OLHO em gráficos com escalas diferentes",
          "a reta mais em pé PARECE subir mais rápido",
          "a escala engana: calcule Δy ÷ Δx em cada gráfico"),
         ("Inverter a fração: (0, 2) e (2, 8) → a = 2 ÷ 6 = 1/3",
          "os dois números estão certos; só trocaram de andar",
          "é y sobre x: a = 6 ÷ 2 = 3; e a conferência pega o erro na hora")]


def b_erros(c, t, C, B):
    K.erro_cards(c, t, C, ["19", "20", "21"], ERROS)


# ======================================================================
# questões do material
# ======================================================================

def _enunciado(c, linhas, a, y0=250, size=30, w=700):
    y = y0
    for s, col in linhas:
        for ln in K.wrap(s, "black", size, w):
            text(c, ln, 190, y, size, "black", col, a, align="left")
            y += size + 12
        y += 8
    return y


def _painel(c, y0, a):
    rrect(c, 170, y0, 740, 830 - y0, 18, "#FFFFFF", a, shadow=True)


ALTS6 = [("A", "f(x) = 2x − 3", "", GREEN), ("B", "f(x) = −3x + 2", "trocou a e b", RED),
         ("C", "f(x) = 0,5x − 3", "inverteu a fração", RED), ("D", "f(x) = 2x + 3", "sinal do b", RED),
         ("E", "f(x) = −2x − 3", "sinal do a", RED)]


def b_q6(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 6 · EU FAÇO", "LEI A PARTIR DO GRÁFICO", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["22.a"], 0.4)
    yend = _enunciado(c, [("O gráfico de uma função afim f é uma reta que corta o eixo vertical no ponto (0, −3) e passa "
                           "pelo ponto (2, 1). A lei dessa função é", INK)], a0, 236, 28)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0 * (1 - ep(t, C["23"], 0.3)),
         align="left")
    cues_in = {L: C[f"22.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"24.x{L.lower()}"] for L in "BCDE"}
    K.alternativas(c, t, C, ALTS6, 1000, 260, 680, 38, C["23.ok"], "A", cues_in, cues_x, gap=40)
    if t < C["23"]:
        if a0 > 0:
            Q = Plano(300, yend + 40, 360, 300, (-1, 3), (-4, 2))
            Q.eixos(c, a0, xt=range(-1, 4), yt=range(-4, 3, 2), fundo=False, size=20)
            Q.ponto(c, 0, -3, BLUE, a0, "(0, −3)", dx=20, dy=10, size=20)
            Q.ponto(c, 2, 1, BLUE, a0, "(2, 1)", dx=-90, dy=-26, size=20)
            Q.reta(c, a0, 2, -3, PURPLE, width=5)
        pause_timer(c, t, C["22.end"] - 1.9, 780, yend + 200)
        return
    y0 = 236 - 30
    _painel(c, y0, ep(t, C["23"], 0.4))
    roteiro4(c, ep(t, C["23"], 0.4), 2 if t < C["23.b"] else 1 if t < C["23.c"] else 3 if t < C["23.d"] else 4, 190,
             y0 + 50, 700)
    y0 += 60
    aa = ep(t, C["23.a"], 0.4)
    if aa > 0:
        linha(c, [("(0, −3): x = 0  →  ", INK2), ("b = −3", BLUE)], 540, y0 + 70, 36, aa)
    ab = ep(t, C["23.b"], 0.4)
    if ab > 0:
        text(c, "a = ", 300, y0 + 190, 44, "black", PURPLE, ab, align="left")
        K.fr(c, "1 − (−3)", "2 − 0", 500, y0 + 172, 36, INK, ab)
        linha(c, [("= ", INK)], 630, y0 + 172, 40, ab)
        K.fr(c, "4", "2", 680, y0 + 172, 40, INK, ab)
        linha(c, [("= ", INK), ("2", PURPLE)], 770, y0 + 172, 44, ab)
    acc = ep(t, C["23.c"], 0.4)
    if acc > 0:
        lei_ab(c, 540, y0 + 300, 50, acc, "2", "− 3")
    ad = ep(t, C["23.d"], 0.4)
    if ad > 0:
        rrect(c, 200, y0 + 370, 680, 100, 18, mix("#FFFFFF", GREEN, 0.12), ad)
        linha(c, [("f(2) = 2 · 2 − 3 = ", INK), ("1", GREEN)], 540, y0 + 420, 36, ad)
        check_icon(c, 840, y0 + 420, 22, ep(t, C["23.d"] + 2.0, 0.4), GREEN)
    if t >= C["24"]:
        pill(c, "a reta SOBE de −3 para 1: a > 0", 540, y0 + 520, AMBER, size=24, a=ep(t, C["24.xe"], 0.4),
             anchor="center", bounds=(170, 910))


ALTS5 = [("A", "18,5 °E.", "esqueceu o b", RED), ("B", "28,5 °E.", "", GREEN), ("C", "47 °E.", "37 + 10: sem a taxa", RED),
         ("D", "74 °E.", "taxa invertida (2), sem b", RED), ("E", "84 °E.", "taxa invertida + b", RED)]


def b_q5(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 5 · VOCÊ FAZ", "UMA ESCALA TERMOMÉTRICA NOVA", GREEN)
    card(c, *CARD_R)
    a0 = ep(t, C["25.a"], 0.4)
    yend = _enunciado(c, [("Um estudante criou uma escala termométrica E que marca 10 °E no ponto de fusão do gelo (0 °C) e "
                           "60 °E no ponto de ebulição da água (100 °C), ao nível do mar. A relação entre as escalas é "
                           "afim. Uma pessoa com temperatura corporal de 37 °C teria, nessa escala,", INK)], a0, 236, 27)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0 * (1 - ep(t, C["26"], 0.3)),
         align="left")
    cues_in = {L: C[f"25.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"27.x{L.lower()}"] for L in "ACDE"}
    K.alternativas(c, t, C, ALTS5, 1000, 260, 680, 38, C["26.ok"], "B", cues_in, cues_x, gap=40)
    if t < C["26"]:
        pause_timer(c, t, C["25.end"] - 1.9, 540, yend + 140)
        return
    y0 = 236 - 30
    _painel(c, y0, ep(t, C["26"], 0.4))
    roteiro4(c, ep(t, C["26"], 0.4), 2 if t < C["26.b"] else 1 if t < C["26.c"] else 3 if t < C["26.d"] else 4, 190,
             y0 + 50, 700)
    y0 += 60
    aa = ep(t, C["26.a"], 0.4)
    if aa > 0:
        linha(c, [("(0, 10) e (100, 60)", INK)], 540, y0 + 60, 34, aa)
        linha(c, [("x = 0  →  ", INK2), ("b = 10", BLUE)], 540, y0 + 125, 36, ep(t, C["26.a"] + 1.4, 0.4))
    ab = ep(t, C["26.b"], 0.4)
    if ab > 0:
        text(c, "a = ", 330, y0 + 230, 44, "black", PURPLE, ab, align="left")
        K.fr(c, "60 − 10", "100 − 0", 530, y0 + 212, 34, INK, ab)
        linha(c, [("= ", INK), ("0,5", PURPLE)], 700, y0 + 212, 44, ab)
    acc = ep(t, C["26.c"], 0.4)
    if acc > 0:
        linha(c, [("E = ", INK), ("0,5", PURPLE), ("C", INK), (" + 10", BLUE)], 540, y0 + 320, 44, acc)
        linha(c, [("0,5 · 37 + 10 = 18,5 + 10 = ", INK2), ("28,5", GREEN)], 540, y0 + 390, 32,
              ep(t, C["26.c"] + 2.2, 0.4))
    ad = ep(t, C["26.d"], 0.4)
    if ad > 0:
        rrect(c, 200, y0 + 450, 680, 100, 18, mix("#FFFFFF", GREEN, 0.12), ad)
        linha(c, [("fervura: 0,5 · 100 + 10 = ", INK), ("60", GREEN)], 540, y0 + 500, 32, ad)
        check_icon(c, 850, y0 + 500, 22, ep(t, C["26.d"] + 2.0, 0.4), GREEN)


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "LUCRO OU PREJUÍZO?", PURPLE)
    aa = ep(t, C["29.a"], 0.5)
    if aa > 0:
        rrect(c, 260, 240, 640, 160, 24, "#FFFFFF", aa, shadow=True)
        text(c, "CUSTO FIXO", 580, 295, 28, "black", BLUE, aa)
        text(c, "R$ 12.000,00", 580, 365, 52, "black", BLUE, aa)
        ab0 = ep(t, C["29.a"] + 2.0, 0.5)
        rrect(c, 1020, 240, 640, 160, 24, "#FFFFFF", ab0, shadow=True)
        text(c, "LUCRA POR CAMISETA", 1340, 295, 28, "black", PURPLE, ab0)
        text(c, "R$ 20,00", 1340, 365, 52, "black", PURPLE, ab0)
    ab = ep(t, C["29.b"], 0.5)
    if ab > 0:
        rrect(c, 460, 450, 1000, 170, 26, mix("#FFFFFF", AMBER, 0.20), ab)
        text_mid(c, "600 camisetas: tem LUCRO?", W / 2, 535, 54, "black", INK, ab)
    acc = ep(t, C["29.c"], 0.5)
    if acc > 0:
        selo(c, W / 2, 700, acc, "A RESPOSTA NÃO É SIM", AMBER, -4, 40)
    pill(c, "ep. 4 · estudo do sinal, lucro e comparação de planos", W / 2, 810, PURPLE, size=26,
         a=ep(t, C["29.d"], 0.5), anchor="center")


def b_cta(c, t, C, B):
    cta(c, t, C["30.like"], C["30.sub"], C["30.bell"], C["30.com"], C["30.bye"],
        "Qual fórmula que você decorou é, na verdade, uma reta?", canal="no Estudativo", anki=C["30.anki"])


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, escada=b_escada, sinal=b_sinal, tamanho=b_tamanho,
              contexto=b_contexto, olhadas=b_olhadas, escala=b_escala, pregos=b_pregos, quarto=b_quarto,
              atalhob=b_atalhob, termometro=b_termometro, tangente=b_tangente, exercicio=b_exercicio, recap=b_recap,
              erros=b_erros, q6=b_q6, q5=b_q5, ponte=b_ponte, cta=b_cta)
