"""Visual — Função Exponencial, Episódio 4: exponencial ou afim? O teste da razão (tema claro).
Peças comuns da série em ../../comum.py (reexporta o 019/comum.py: expr com potências, alternativas, erro_cards, atalho,
selo, regra...).
Peças deste episódio: Plano (eixos com escala própria; curva() desenha y = f(x) aos poucos), corrida() (a tartaruga na reta
20 + 10t e a lebre na curva 2ᵗ, com o placar), tartaruga() e lebre() (ícones), tabela_ops() (tabela com as linhas de valores
e, embaixo de cada uma, a linha de operações entre vizinhos "−" / "÷", com a que se repete acendendo em verde),
perfil() (cartão de perfil de rede social com o contador de seguidores), linha() (texto com cor por trecho).
Cores com função: azul = definição · roxo = regra/fórmula · âmbar = armadilha · verde = atalho · vermelho = erro.
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
ARQUIVO_FINAL = "enem_matematica_exponencial_ep4_teste_razao.mp4"
CARD_R = K.CARD_R
GRADE = "#EEEEEA"
TART = "#3E9A5B"     # tartaruga (reta)
LEBRE = PURPLE       # lebre (curva)


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


def potencia(c, base, exp, cx, cy, size, a, col=None, prefixo="", col_pre=None):
    """'prefixo' + base^exp numa linha (expoente menor e alto), centrado em cx"""
    if a <= 0:
        return
    col = col or INK
    wp = ftext_w(prefixo, "black", size) if prefixo else 0
    wb = ftext_w(base, "black", size)
    we = ftext_w(exp, "black", size * 0.58)
    x = cx - (wp + wb + we + 4) / 2
    if prefixo:
        ftext(c, prefixo, x, cy + size * 0.36, size, "black", col_pre or INK, a, align="left")
        x += wp
    ftext(c, base, x, cy + size * 0.36, size, "black", col, a, align="left")
    ftext(c, exp, x + wb + 4, cy - size * 0.18, size * 0.58, "black", col, a, align="left")


class Plano:
    """plano cartesiano num retângulo (x0, y0, w, h) com faixas xr, yr próprias."""

    def __init__(s, x0, y0, w, h, xr, yr):
        s.x0, s.y0, s.w, s.h, s.xr, s.yr = x0, y0, w, h, xr, yr

    def px(s, x):
        return s.x0 + (x - s.xr[0]) / (s.xr[1] - s.xr[0]) * s.w

    def py(s, y):
        return s.y0 + s.h - (y - s.yr[0]) / (s.yr[1] - s.yr[0]) * s.h

    def eixos(s, c, a, xt=(), yt=(), size=22, rot=("t", "y")):
        if a <= 0:
            return
        for v in xt:
            line(c, s.px(v), s.y0, s.px(v), s.y0 + s.h, GRADE, a, 2)
        for v in yt:
            line(c, s.x0, s.py(v), s.x0 + s.w, s.py(v), GRADE, a, 2)
        oy, ox = s.y0 + s.h, s.x0
        arrow(c, s.x0, oy, s.x0 + s.w + 24, oy, INK2, a, 3, 12)
        arrow(c, ox, oy, ox, s.y0 - 22, INK2, a, 3, 12)
        text(c, rot[0], s.x0 + s.w + 22, oy + 36, 24, "black", GRAY, a)
        text(c, rot[1], ox - 22, s.y0 - 6, 24, "black", GRAY, a, align="right")
        for v in xt:
            text(c, f"{v:g}", s.px(v), oy + size + 10, size, "bold", INK2, a)
        for v in yt:
            if v:
                text(c, f"{v:g}", ox - 12, s.py(v) + size * 0.36, size, "bold", INK2, a, align="right")

    def curva(s, c, a, f, col, u=1.0, width=7, xa=None, xb=None, n=160):
        if a <= 0 or u <= 0:
            return
        xa = s.xr[0] if xa is None else xa
        xb = s.xr[1] if xb is None else xb
        xe = xa + (xb - xa) * clamp(u)
        c.save()
        c.clipRect(skia.Rect.MakeXYWH(s.x0, s.y0 - 4, s.w + 4, s.h + 8))
        path = skia.Path()
        for k in range(n + 1):
            x = xa + (xe - xa) * k / n
            y = max(min(f(x), s.yr[1] * 3), s.yr[0] - 5)
            (path.moveTo if k == 0 else path.lineTo)(s.px(x), s.py(y))
        c.drawPath(path, paint(col, a, stroke=width, cap_round=True))
        c.restore()


def tartaruga(c, cx, cy, s, a):
    """casco verde com cabeça e patinhas (anda na reta)"""
    if a <= 0:
        return
    for dx in (-0.32, 0.28):
        c.drawCircle(cx + dx * s, cy + 0.02 * s, 0.11 * s, paint("#7FBF8E", a))
    c.drawCircle(cx + 0.55 * s, cy - 0.12 * s, 0.15 * s, paint("#7FBF8E", a))
    c.drawCircle(cx + 0.6 * s, cy - 0.15 * s, 0.03 * s, paint(INK, a))
    p = skia.Path()
    p.addArc(skia.Rect.MakeXYWH(cx - 0.48 * s, cy - 0.46 * s, 0.96 * s, 0.9 * s), 180, 180)
    p.close()
    c.drawPath(p, paint(TART, a))
    for k in range(3):
        c.drawCircle(cx + (k - 1) * 0.24 * s, cy - 0.17 * s, 0.07 * s, paint("#2E7A47", a))


def lebre(c, cx, cy, s, a):
    """corpo oval cinza com orelhas compridas (anda na curva)"""
    if a <= 0:
        return
    col = "#8C8F99"
    for dx, ang in ((0.22, -12), (0.36, 8)):
        c.save(); c.translate(cx + dx * s, cy - 0.42 * s); c.rotate(ang)
        c.drawOval(skia.Rect.MakeXYWH(-0.07 * s, -0.34 * s, 0.14 * s, 0.4 * s), paint(col, a))
        c.restore()
    c.drawOval(skia.Rect.MakeXYWH(cx - 0.45 * s, cy - 0.22 * s, 0.7 * s, 0.42 * s), paint(col, a))
    c.drawCircle(cx + 0.3 * s, cy - 0.2 * s, 0.17 * s, paint(col, a))
    c.drawCircle(cx + 0.36 * s, cy - 0.24 * s, 0.035 * s, paint(INK, a))
    c.drawCircle(cx - 0.47 * s, cy - 0.06 * s, 0.08 * s, paint("#FFFFFF", a))


RETA = lambda t: 20 + 10 * t
CURVA = lambda t: 2 ** t


def corrida(c, pl, a, tn, aR=1.0, aC=1.0, placar=True, px_=1500, py_=300, bichos=True):
    """a reta 20 + 10t (tartaruga) e a curva 2ᵗ (lebre) até o instante tn, com o placar ao lado"""
    if a <= 0:
        return
    pl.eixos(c, a, (0, 2, 4, 6, 8), (20, 60, 100, 140))
    pl.curva(c, a * aR, RETA, TART, tn / pl.xr[1], xa=0, xb=pl.xr[1])
    pl.curva(c, a * aC, CURVA, LEBRE, tn / pl.xr[1], xa=0, xb=pl.xr[1])
    if aR > 0:
        text(c, "20 + 10t", pl.px(0) + 20, pl.py(20) - 18, 26, "black", TART, a * aR, align="left")
    if aC > 0:
        potencia(c, "2", "t", pl.px(0.5) + 34, pl.py(1) - 30, 30, a * aC, LEBRE)
    if bichos:
        yr, yc = min(RETA(tn), pl.yr[1]), min(CURVA(tn), pl.yr[1])
        tartaruga(c, pl.px(tn), pl.py(yr) - 30, 64, a * aR)
        lebre(c, pl.px(tn), pl.py(yc) - 34, 70, a * aC)
    if placar:
        k = int(math.floor(tn + 1e-6))
        rrect(c, px_ - 210, py_, 420, 260, 24, "#FFFFFF", a, shadow=True)
        text(c, f"passo t = {k}", px_, py_ + 52, 30, "black", INK2, a)
        r_, c_ = RETA(k), CURVA(k)
        lider = TART if r_ > c_ else LEBRE
        tartaruga(c, px_ - 140, py_ + 128, 50, a)
        ftext(c, f"{r_}", px_ + 120, py_ + 140, 54, "black", TART, a, align="right")
        lebre(c, px_ - 140, py_ + 212, 54, a)
        ftext(c, f"{c_}", px_ + 120, py_ + 224, 54, "black", LEBRE, a, align="right")
        c.drawCircle(px_ + 170, py_ + (122 if lider == TART else 206), 12, paint(lider, a))


VAL_AFIM = ["100", "150", "200", "250", "300"]
VAL_EXP = ["100", "150", "225", "337,5", "506,25"]
DIF_AFIM = ["+50", "+50", "+50", "+50"]
DIF_EXP = ["+50", "+75", "+112,5", "+168,75"]
RAZ_EXP = ["×1,5", "×1,5", "×1,5", "×1,5"]
RAZ_AFIM = ["×1,5", "×1,33", "×1,25", "×1,2"]


def tabela_ops(c, x, y, xs, linhas, a, cw=250, lw=250, rh=86, oh=64):
    """linhas = [(rótulo, cor, valores, alfas_valores, ops, a_ops, cor_ops, repete)]: abaixo de cada linha de valores, a
    linha de operações entre vizinhos (texto entre as colunas); repete=True acende a linha de operações em verde."""
    if a <= 0:
        return
    n = len(xs)
    tw = lw + n * cw
    th = rh + len(linhas) * (rh + oh)
    rrect(c, x, y, tw, th, 18, "#FFFFFF", a, shadow=True)
    rrect(c, x, y, tw, rh, 18, mix("#FFFFFF", INK, 0.06), a)
    text_mid(c, "t", x + lw / 2, y + rh / 2, 34, "black", INK, a)
    for k, v in enumerate(xs):
        text_mid(c, v, x + lw + cw * (k + 0.5), y + rh / 2, 34, "black", INK, a)
    yy = y + rh
    for rot_, col, vals, alfas, ops, aop, cop, rep in linhas:
        line(c, x + 14, yy, x + tw - 14, yy, LIGHT, a, 2)
        text_mid(c, rot_, x + lw / 2, yy + rh / 2, 32, "black", col, a)
        for k, v in enumerate(vals):
            ak = a * (alfas[k] if alfas else 1.0)
            if ak > 0:
                ftext(c, v, x + lw + cw * (k + 0.5), yy + rh / 2 + 13, 38, "black", col, ak)
        yo = yy + rh
        if ops and aop > 0:
            if rep:
                rrect(c, x + lw + cw * 0.5, yo + 6, cw * (n - 1), oh - 12, 16, mix("#FFFFFF", GREEN, 0.22), a * aop)
            for k, s_ in enumerate(ops):
                xm = x + lw + cw * (k + 1)
                ak = a * clamp(aop * len(ops) - k)
                ftext(c, s_, xm, yo + oh / 2 + 10, 28, "black", GREEN if rep else (cop or AMBER), ak)
        yy = yo + oh
    line(c, x + lw, y + 10, x + lw, y + th - 10, LIGHT, a, 2)


def perfil(c, cx, cy, nome, valores, n_vis, col, a, sub):
    """cartão de perfil com a lista de seguidores semana a semana"""
    if a <= 0:
        return
    rrect(c, cx - 330, cy - 200, 660, 400, 26, "#FFFFFF", a, shadow=True)
    c.drawCircle(cx - 250, cy - 120, 46, paint(mix("#FFFFFF", col, 0.35), a))
    c.drawCircle(cx - 250, cy - 132, 16, paint(col, a))
    c.drawOval(skia.Rect.MakeXYWH(cx - 280, cy - 110, 60, 36), paint(col, a))
    text(c, nome, cx - 180, cy - 128, 36, "black", INK, a, align="left")
    text(c, sub, cx - 180, cy - 86, 24, "bold", col, a, align="left")
    for k, v in enumerate(valores):
        ak = a * clamp(n_vis - k)
        if ak <= 0:
            continue
        x = cx - 220 + k * 220
        rrect(c, x - 90, cy - 20, 180, 150, 20, mix("#FFFFFF", col, 0.14), ak)
        text(c, f"semana {k + 1}", x, cy + 16, 22, "bold", INK2, ak)
        ftext(c, v, x, cy + 96, 50, "black", col, ak)


# ======================================================================
# abertura
# ======================================================================

def _tn(t, marcos):
    """instante da corrida: marcos = [(tempo_do_vídeo, t_da_corrida)] interpolados com suavidade"""
    v = marcos[0][1]
    for (t0, v0), (t1, v1) in zip(marcos, marcos[1:]):
        if t >= t0:
            v = v0 + (v1 - v0) * ease_io(clamp((t - t0) / max(t1 - t0, 1e-3)))
    return v


def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "FUNÇÃO EXPONENCIAL · EPISÓDIO 4", BLUE)
    card(c, *CARD_R)
    pl = Plano(260, 230, 900, 540, (0, 8), (0, 150))
    aa = ep(t, C["01.a"], 0.5)
    tn = _tn(t, [(C["01.a"], 0.0), (C["01.b"], 0.0), (C["01.b"] + 3.0, 6.0), (C["01.c"], 6.0), (C["01.c"] + 2.0, 7.0)])
    corrida(c, pl, aa, tn, placar=t >= C["01.b"], px_=1480, py_=300)
    if aa > 0 and t < C["01.b"]:
        rrect(c, 1270, 300, 420, 260, 24, "#FFFFFF", aa, shadow=True)
        text(c, "largada", 1480, 352, 30, "black", INK2, aa)
        linha(c, [("reta: ", INK2), ("20", TART)], 1480, 430, 46, aa)
        linha(c, [("curva: ", INK2), ("1", LEBRE)], 1480, 510, 46, aa)
    ac = ep(t, C["01.c"] + 2.0, 0.4)
    if ac > 0:
        selo(c, 1480, 640, ac, "ULTRAPASSOU!", GREEN, -4, 34)
    ad = ep(t, C["01.d"], 0.5)
    if ad > 0:
        regra(c, "E NUNCA MAIS PERDE", 1480, 760, ad, 34, GREEN)


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "FUNÇÃO EXPONENCIAL · EP. 4", "AO FINAL DESTA AULA", GREEN)
    a0 = ep(t, C["02"], 0.4)
    if a0 > 0:
        pill(c, "4º episódio da série de FUNÇÃO EXPONENCIAL", W / 2, 240, BLUE, size=30, a=a0, anchor="center")
    itens = [("02.a", "AFIM OU EXPONENCIAL?", "olhando só a tabela, em segundos", BLUE),
             ("02.b", "O FATOR", "o número que se repete na divisão", PURPLE)]
    for k, (cue, tit, sub, col) in enumerate(itens):
        ak = ep(t, C[cue], 0.5)
        if ak <= 0:
            continue
        x = 640 + k * 640
        rrect(c, x - 290, 330, 580, 330, 26, "#FFFFFF", ak, shadow=True)
        rrect(c, x - 290, 330, 580, 70, 26, col, ak * 0.16)
        badge_num(c, k + 1, x, 470, ak, 34, bg=col)
        text(c, tit, x, 570, 40, "black", col, ak)
        text(c, sub, x, 625, 26, "bold", INK2, ak)


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "DOIS LEMBRETES", "EM 30 SEGUNDOS", GREEN)
    a, d = rise(t, C["03.a"])
    if a > 0:
        y = 330 + d
        rrect(c, 260, y - 80, 1400, 160, 24, "#FFFFFF", a, shadow=True)
        pill(c, "série de Função afim", 300, y - 80, BLUE, size=22, a=a)
        linha(c, [("afim: ", INK2), ("SOMA", BLUE), (" sempre o mesmo valor   (+ · + · +)", INK)], 960, y + 10, 46, a)
    a, d = rise(t, C["03.b"])
    if a > 0:
        y = 560 + d
        rrect(c, 260, y - 80, 1400, 160, 24, "#FFFFFF", a, shadow=True)
        pill(c, "episódio 2", 300, y - 80, PURPLE, size=22, a=a)
        potencia(c, "Q₀ · a", "t", 760, y + 6, 60, a, PURPLE)
        linha(c, [("MULTIPLICA", PURPLE), (" pelo fator a cada passo", INK)], 1260, y + 8, 40, a)


def b_concreto(c, t, C, B):
    head(c, t, B["start"], "DOIS PERFIS DE REDE SOCIAL", "QUEM CRESCE COMO?", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["04.a"], 0.5)
    perfil(c, 560, 420, "@perfil.um", ["100", "200", "300"], (t - C["04.a"]) / 1.0 if aa > 0 else 0, BLUE, aa,
           "+100 por semana")
    ab = ep(t, C["04.b"], 0.5)
    perfil(c, 1360, 420, "@perfil.dois", ["100", "200", "400"], (t - C["04.b"]) / 1.0 if ab > 0 else 0, PURPLE, ab,
           "dobra toda semana")
    acc = ep(t, C["04.c"], 0.5)
    if acc > 0:
        rrect(c, 230, 660, 660, 130, 22, mix("#FFFFFF", BLUE, 0.12), acc)
        text(c, "MODELO AFIM", 560, 712, 32, "black", BLUE, acc)
        text(c, "soma o mesmo número", 560, 760, 26, "bold", INK2, acc)
        ac2 = ep(t, C["04.c"] + 2.4, 0.5)
        rrect(c, 1030, 660, 660, 130, 22, mix("#FFFFFF", PURPLE, 0.12), ac2)
        text(c, "MODELO EXPONENCIAL", 1360, 712, 32, "black", PURPLE, ac2)
        text(c, "multiplica pelo mesmo número", 1360, 760, 26, "bold", INK2, ac2)


# ======================================================================
# blocos a e b — a tabela, a diferença e a razão
# ======================================================================

XS = ["0", "1", "2", "3", "4"]


def _alfas(t, t0, n=5, passo=0.5, ini=0):
    return [1.0 if k < ini else clamp((t - t0 - (k - ini) * passo) / 0.4) for k in range(n)]


def b_tabela(c, t, C, B):
    head(c, t, B["start"], "QUANDO SÓ APARECE A TABELA", "QUAL É QUAL?", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["05.a"], 0.5)
    al_af = [1.0, 1.0] + _alfas(t, C["05.c"], 3)
    al_ex = [1.0, 1.0] + _alfas(t, C["05.d"], 3)
    if t < C["05.b"]:
        al_af = al_ex = [1.0, 0, 0, 0, 0]
    elif t < C["05.c"]:
        al_af = al_ex = [1.0, 1.0, 0, 0, 0]
    if t < C["05.d"]:
        al_ex = al_ex[:2] + [0, 0, 0]
    tabela_ops(c, 210, 260, XS, [("tabela 1", INK, VAL_AFIM, al_af, None, 0, None, False),
                                 ("tabela 2", INK, VAL_EXP, al_ex, None, 0, None, False)], a0, oh=40)
    if a0 > 0:
        pill(c, "começam iguais", 460 + 125, 236, BLUE, size=22, a=a0 * (1 - ep(t, C["05.b"], 0.3)), anchor="center")
    ab = ep(t, C["05.b"], 0.5)
    if ab > 0:
        pill(c, "mesmo 1º passo", 460 + 375, 236, BLUE, size=22, a=ab, anchor="center")
    ad = ep(t, C["05.d"] + 2.4, 0.5)
    if ad > 0:
        text_mid(c, "qual é afim? qual é exponencial?", 960, 760, 46, "black", AMBER, ad)


def b_diferenca(c, t, C, B):
    head(c, t, B["start"], "PRIMEIRO TESTE", "SUBTRAIA OS VIZINHOS", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["06"], 0.4)
    aa = ep(t, C["06.a"], 1.2)
    ac = ep(t, C["06.c"], 1.2)
    tabela_ops(c, 210, 220, XS, [("tabela 1", BLUE if t >= C["06.b"] else INK, VAL_AFIM, None, DIF_AFIM, aa, None,
                                  t >= C["06.b"]),
                                 ("tabela 2", INK, VAL_EXP, None, DIF_EXP, ac, AMBER, False)], a0)
    if a0 > 0:
        text(c, "−", 160, 220 + 86 + 86 + 44, 44, "black", GREEN, a0)
        text(c, "−", 160, 220 + 86 * 2 + 64 + 86 + 44, 44, "black", AMBER, a0)
    ab = ep(t, C["06.b"], 0.5)
    if ab > 0:
        rrect(c, 230, 690, 700, 110, 22, mix("#FFFFFF", BLUE, 0.12), ab)
        linha(c, [("DIFERENÇA CONSTANTE  →  ", INK), ("AFIM", BLUE)], 580, 745, 34, ab)
    acc = ep(t, C["06.c"] + 2.0, 0.5)
    if acc > 0:
        rrect(c, 990, 690, 700, 110, 22, mix("#FFFFFF", AMBER, 0.18), acc)
        text(c, "tabela 2: os saltos CRESCEM", 1340, 760, 32, "black", AMBER, acc)


def b_razao(c, t, C, B):
    head(c, t, B["start"], "SEGUNDO TESTE", "O TESTE DA RAZÃO", PURPLE)
    card(c, *CARD_R)
    a0 = ep(t, C["07"], 0.4)
    ab = ep(t, C["07.b"], 1.6)
    ad = ep(t, C["07.d"], 1.4)
    tabela_ops(c, 210, 220, XS, [("tabela 1", BLUE, VAL_AFIM, None, RAZ_AFIM, ad, RED, False),
                                 ("tabela 2", PURPLE if t >= C["07.c"] else INK, VAL_EXP, None, RAZ_EXP, ab, None,
                                  t >= C["07.c"])], a0)
    if a0 > 0:
        text(c, "÷", 160, 220 + 86 + 86 + 44, 44, "black", RED, a0 * ad)
        text(c, "÷", 160, 220 + 86 * 2 + 64 + 86 + 44, 44, "black", GREEN, a0 * ab)
    aa = ep(t, C["07.a"], 0.5)
    if aa > 0 and t < C["07.c"]:
        rrect(c, 300, 690, 1320, 110, 22, mix("#FFFFFF", BLUE, 0.12), aa)
        text(c, "TESTE DA RAZÃO: cada valor ÷ o ANTERIOR", 960, 760, 36, "black", BLUE, aa)
    acc = ep(t, C["07.c"], 0.5)
    if acc > 0 and t < C["07.e"]:
        rrect(c, 300, 690, 1320, 110, 22, mix("#FFFFFF", PURPLE, 0.12), acc)
        linha(c, [("RAZÃO CONSTANTE  →  ", INK), ("EXPONENCIAL", PURPLE), ("  ·  fator a = 1,5", INK)], 960, 745, 36, acc)
    ae = ep(t, C["07.e"], 0.5)
    if ae > 0:
        for k, (tit, op, col) in enumerate((("AFIM", "repete a SUBTRAÇÃO", BLUE), ("EXPONENCIAL", "repete a DIVISÃO", PURPLE))):
            x = 580 + k * 760
            rrect(c, x - 340, 680, 680, 130, 22, mix("#FFFFFF", col, 0.14), ae)
            text(c, tit, x, 728, 32, "black", col, ae)
            text(c, op, x, 778, 30, "black", INK, ae)


def b_atalho_razao(c, t, C, B):
    head(c, t, B["start"], "ATALHO", "O TESTE EM 3 PASSOS", GREEN)
    card(c, *CARD_R)
    a0 = ep(t, C["08"], 0.4)
    if a0 > 0:
        K.boxed(c, 260, 200, 1400, 470, GREEN, a0, 0.08)
        text(c, "ATALHO · TESTE DA RAZÃO", 960, 250, 24, "black", GREEN, a0, tracking=2)
    passos = [("08.a", "divida VIZINHO por VIZINHO", "nunca pelo primeiro valor"),
              ("08.b", "razão sempre igual?", "ela é o FATOR a"),
              ("08.c", "o valor em t = 0", "é o Q₀")]
    for k, (cue, s1, s2) in enumerate(passos):
        ak = ep(t, C[cue], 0.5)
        if ak <= 0:
            continue
        y = 330 + k * 115
        badge_num(c, k + 1, 360, y, ak, 32, bg=GREEN)
        text(c, s1, 420, y + 12, 40, "black", INK, ak, align="left")
        text(c, s2, 1600, y + 12, 32, "bold", GREEN, ak, align="right")
    acc = ep(t, C["08.c"] + 3.0, 0.5)
    if acc > 0:
        rrect(c, 560, 710, 800, 110, 24, mix("#FFFFFF", PURPLE, 0.14), acc)
        potencia(c, "1,5", "t", 960, 765, 64, acc, PURPLE, prefixo="f(t) = 100 · ", col_pre=INK)


# ======================================================================
# bloco c — a corrida
# ======================================================================

def b_corrida(c, t, C, B):
    head_seq(c, t, C, [("09", "E QUEM VENCE NO FIM?", "A TARTARUGA E A LEBRE AO CONTRÁRIO", AMBER),
                       ("10", "POR QUE NUNCA MAIS PERDE?", "A CURVA DOBRA", GREEN)])
    card(c, *CARD_R)
    pl = Plano(260, 240, 880, 530, (0, 8), (0, 150))
    a0 = ep(t, C["09"], 0.4)
    if t < C["10"]:
        tn = _tn(t, [(C["09.d"], 0.0), (C["09.d"] + 3.0, 6.0), (C["09.e"], 6.0), (C["09.e"] + 1.6, 7.0)])
        corrida(c, pl, a0, tn, aR=ep(t, C["09.b"], 0.6), aC=ep(t, C["09.c"], 0.6), placar=t >= C["09.d"],
                px_=1480, py_=290, bichos=True)
        aa = ep(t, C["09.a"], 0.5)
        if aa > 0 and t < C["09.d"]:
            rrect(c, 1270, 290, 420, 300, 24, mix("#FFFFFF", AMBER, 0.16), aa)
            text(c, "AO CONTRÁRIO", 1480, 350, 34, "black", AMBER, aa)
            tartaruga(c, 1380, 440, 70, aa)
            text(c, "reta: larga na frente", 1440, 450, 24, "bold", TART, aa, align="left")
            lebre(c, 1380, 530, 76, aa)
            text(c, "curva: vence no fim", 1440, 540, 24, "bold", LEBRE, aa, align="left")
        ae = ep(t, C["09.e"] + 1.6, 0.4)
        if ae > 0:
            selo(c, 1480, 680, ae, "ULTRAPASSOU!", GREEN, -4, 34)
        return
    corrida(c, pl, 1.0, 7.0, placar=False)
    aa = ep(t, C["10.a"], 0.5)
    if aa > 0:
        x6, x7 = pl.px(6), pl.px(7)
        line(c, x6, pl.py(80), x7, pl.py(80), TART, aa, 3, dash=(8, 6))
        line(c, x7, pl.py(80), x7, pl.py(90), TART, aa, 4)
        pill(c, "+10", x7 + 16, pl.py(86), TART, size=24, a=aa, bounds=(0, 1920))
    ab = ep(t, C["10.b"], 0.5)
    if ab > 0:
        x6, x7 = pl.px(6), pl.px(7)
        line(c, x6, pl.py(64), x7 - 30, pl.py(64), LEBRE, ab, 3, dash=(8, 6))
        line(c, x7 - 30, pl.py(64), x7 - 30, pl.py(128), LEBRE, ab, 5)
        pill(c, "+64", x7 - 120, pl.py(118), LEBRE, size=24, a=ab, bounds=(0, 1920))
    rrect(c, 1270, 260, 420, 230, 24, "#FFFFFF", aa, shadow=True)
    if aa > 0:
        text(c, "a cada passo", 1480, 310, 28, "bold", INK2, aa)
        tartaruga(c, 1360, 380, 50, aa)
        linha(c, [("+10, sempre", TART)], 1520, 390, 34, aa)
        lebre(c, 1360, 452, 54, ab)
        linha(c, [("dobra", LEBRE)], 1520, 462, 34, ab)
    acc = ep(t, C["10.c"], 0.5)
    if acc > 0:
        rrect(c, 1270, 520, 420, 170, 24, mix("#FFFFFF", GREEN, 0.14), acc)
        text(c, "passo t = 10", 1480, 568, 28, "bold", INK2, acc)
        linha(c, [("120", TART), ("  ×  ", INK2), ("1 024", LEBRE)], 1480, 635, 48, acc)
    ad = ep(t, C["10.d"], 0.5)
    if ad > 0:
        selo(c, 1480, 760, ad, "ULTRAPASSA QUALQUER RETA", GREEN, -3, 28)


# ======================================================================
# bloco d — três pontos; bloco e — progressão geométrica
# ======================================================================

def b_tres(c, t, C, B):
    head(c, t, B["start"], "BASTA CONFERIR DOIS PONTOS?", "A QUESTÃO 3 DO EPISÓDIO 2", AMBER)
    card(c, *CARD_R)
    aa = ep(t, C["11.a"], 0.5)
    x0, y0, lw, cw, rh = 330, 250, 360, 340, 96
    if aa > 0:
        rrect(c, x0, y0, lw + 3 * cw, rh * 3, 18, "#FFFFFF", aa, shadow=True)
        rrect(c, x0, y0, lw + 3 * cw, rh, 18, mix("#FFFFFF", INK, 0.06), aa)
        text_mid(c, "t", x0 + lw / 2, y0 + rh / 2, 34, "black", INK, aa)
        for k in range(3):
            text_mid(c, str(k), x0 + lw + cw * (k + 0.5), y0 + rh / 2, 34, "black", INK, aa)
        text_mid(c, "tabela", x0 + lw / 2, y0 + rh * 1.5, 32, "black", INK, aa)
        for k, v in enumerate(("50 000", "40 000", "32 000")):
            ftext(c, v, x0 + lw + cw * (k + 0.5), y0 + rh * 1.5 + 14, 40, "black", INK, aa)
    ab = ep(t, C["11.b"], 0.5)
    if ab > 0:
        line(c, x0 + 14, y0 + rh * 2, x0 + lw + 3 * cw - 14, y0 + rh * 2, LIGHT, ab, 2)
        text_mid(c, "50 000 − 10 000t", x0 + lw / 2, y0 + rh * 2.5, 28, "black", AMBER, ab)
        for k, v in enumerate(("50 000", "40 000")):
            ak = ep(t, C["11.b"] + 1.4 + k * 1.4, 0.4)
            ftext(c, v, x0 + lw + cw * (k + 0.5) - 20, y0 + rh * 2.5 + 14, 40, "black", AMBER, ak)
            check_icon(c, x0 + lw + cw * (k + 0.5) + 120, y0 + rh * 2.5, 22, ak, GREEN)
    acc = ep(t, C["11.c"], 0.5)
    if acc > 0:
        ftext(c, "30 000", x0 + lw + cw * 2.5 - 20, y0 + rh * 2.5 + 14, 40, "black", RED, acc)
        check_icon(c, x0 + lw + cw * 2.5 + 120, y0 + rh * 2.5, 22, acc, RED, "x")
        rrect(c, x0 + lw + cw * 2 + 8, y0 + rh + 8, cw - 16, rh * 2 - 16, 16, RED, acc * 0.10)
    ad = ep(t, C["11.d"], 0.5)
    if ad > 0:
        rrect(c, 330, 610, 1260, 160, 24, mix("#FFFFFF", AMBER, 0.18), ad)
        text(c, "concordam em DOIS pontos", 960, 672, 38, "black", INK, ad)
        text(c, "e brigam no TERCEIRO", 960, 730, 38, "black", RED, ad)


def b_atalho_tres(c, t, C, B):
    head(c, t, B["start"], "ATALHO", "TESTE TRÊS PONTOS", GREEN)
    card(c, *CARD_R)
    a0 = ep(t, C["12"], 0.4)
    if a0 > 0:
        K.boxed(c, 260, 200, 1400, 360, GREEN, a0, 0.08)
        text(c, "ATALHO · ANTES DE MARCAR A LEI", 960, 250, 24, "black", GREEN, a0, tracking=2)
    for k in range(3):
        ak = ep(t, C["12"] + 1.6 + k * 0.8, 0.4)
        x = 560 + k * 400
        rrect(c, x - 150, 300, 300, 150, 24, "#FFFFFF", ak, shadow=True)
        ftext(c, f"t = {k}", x, 395, 56, "black", GREEN, ak)
    ab = ep(t, C["12.b"], 0.5)
    if ab > 0:
        text(c, "valor inicial", 560, 510, 28, "bold", BLUE, ab)
        text(c, "o fator", 960, 510, 28, "bold", PURPLE, ab)
        text(c, "o fator de novo", 1360, 510, 28, "bold", PURPLE, ab)
    acc = ep(t, C["12.c"], 0.5)
    if acc > 0:
        selo(c, 960, 680, acc, "MENOS DE 1 MINUTO", GREEN, -3, 36)


def b_pg(c, t, C, B):
    head(c, t, B["start"], "ESSE PADRÃO TEM NOME?", "SÓ PARA CITAR", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["13.a"], 0.5)
    if aa > 0:
        vals = ["100", "150", "225", "337,5"]
        for k, v in enumerate(vals):
            ak = aa * ep(t, C["13.a"] + k * 0.5, 0.4)
            x = 480 + k * 320
            rrect(c, x - 120, 260, 240, 120, 22, mix("#FFFFFF", PURPLE, 0.12), ak)
            ftext(c, v, x, 340, 46, "black", PURPLE, ak)
            if k:
                text(c, "×1,5", x - 160, 250, 26, "black", GREEN, ak)
        rrect(c, 260, 450, 1400, 130, 22, mix("#FFFFFF", BLUE, 0.12), ep(t, C["13.a"] + 3.0, 0.5))
        linha(c, [("PROGRESSÃO GEOMÉTRICA: ", BLUE), ("cada termo = o anterior × o mesmo número", INK)], 960, 515, 34,
              ep(t, C["13.a"] + 3.0, 0.5))
    ab = ep(t, C["13.b"], 0.5)
    if ab > 0:
        pill(c, "tem série própria", W / 2, 680, PURPLE, size=34, a=ab, anchor="center")


# ======================================================================
# nós fazemos
# ======================================================================

def b_exercicio(c, t, C, B):
    head_seq(c, t, C, [("14", "SUA VEZ", "PAUSE E TENTE", GREEN), ("15", "VAMOS JUNTOS", "DIFERENÇA OU RAZÃO?", GREEN)])
    card(c, *CARD_R)
    xs = ["0", "1", "2", "3", "4"]
    vals = ["80", "120", "180", "270", "?" if t < C["15.d"] else "405"]
    aa = ep(t, C["14.a"], 0.5)
    al = _alfas(t, C["14.a"], 4, 0.8) + [ep(t, C["14.b"], 0.4)]
    dif = ["+40", "+60", "+90"]
    raz = ["×1,5", "×1,5", "×1,5", "×1,5" if t >= C["15.d"] else ""]
    ops_d = ep(t, C["15.a"], 1.0)
    ops_r = ep(t, C["15.b"], 1.4)
    linhas = [("valores", INK, vals, al, None, 0, None, False)]
    if t >= C["15"]:
        linhas = [("valores", PURPLE if t >= C["15.c"] else INK, vals, al, dif, ops_d, RED, False)]
    tabela_ops(c, 230, 240, xs, linhas, aa, cw=250, lw=230, oh=64)
    if t < C["15"]:
        ab = ep(t, C["14.b"], 0.5)
        if ab > 0:
            text_mid(c, "afim ou exponencial?  e o próximo valor?", 960, 520, 44, "black", AMBER, ab)
        pause_timer(c, t, C["14.end"] - 1.9, 960, 690)
        return
    if ops_d > 0:
        text(c, "−", 196, 240 + 86 * 2 + 44, 44, "black", RED, ops_d)
        pill(c, "não são iguais", 1640, 240 + 86 * 2 + 32, RED, size=22, a=ep(t, C["15.a"] + 2.0, 0.4), anchor="right",
             bounds=(0, 1920))
    if ops_r > 0:
        y = 240 + 86 * 2 + 64
        rrect(c, 230 + 230 + 125, y + 6, 250 * 4, 52, 16, mix("#FFFFFF", GREEN, 0.22), ops_r)
        text(c, "÷", 196, y + 44, 44, "black", GREEN, ops_r)
        for k, s_ in enumerate(raz):
            if s_:
                ftext(c, s_, 230 + 230 + 250 * (k + 1), y + 42, 28, "black", GREEN, clamp(ops_r * 4 - k))
    acc = ep(t, C["15.c"], 0.5)
    if acc > 0:
        rrect(c, 300, 600, 1320, 100, 22, mix("#FFFFFF", PURPLE, 0.12), acc)
        linha(c, [("RAZÃO CONSTANTE  →  ", INK), ("EXPONENCIAL", PURPLE), ("  ·  fator 1,5", INK)], 960, 650, 36, acc)
    ad = ep(t, C["15.d"], 0.5)
    if ad > 0:
        linha(c, [("próximo: 270 × 1,5 = ", INK), ("405", GREEN)], 960, 770, 50, ad)


# ======================================================================
# recap, erros
# ======================================================================

FRASES = ["Diferença constante é afim; razão constante é exponencial.",
          "Toda exponencial crescente acaba ultrapassando qualquer reta.",
          "Teste sempre três pontos, não dois."]


def b_recap(c, t, C, B):
    sid = which(t, C, ["16", "22"])
    frame(c, t, B["start"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "16" else "PARA FECHAR", PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 300 + k * 180 + d
        badge_num(c, k + 1, 260, y - 16, a, 36, bg=PURPLE)
        para(c, s, 320, y, 50, "black", INK, a, 1360, 60)


ERROS = [("Achar que DOIS pontos certos garantem a lei certa", "dois pontos bastam para desenhar uma reta",
          "2ᵗ e 1 + t dão 1 e 2 nos dois primeiros pontos; em t = 2, 4 contra 3: teste o terceiro"),
         ("Confundir o GANHO de uma semana com o TOTAL acumulado", "quem ganha mais parece estar na frente",
          "do passo 4 para o 5, a curva ganha 16 e a reta 10, mas o total é 32 contra 70: compare totais")]


def b_erros(c, t, C, B):
    K.erro_cards(c, t, C, ["17", "18"], ERROS)


# ======================================================================
# questão 5 (nós fazemos)
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


ALTS5 = [("A", "3 semanas.", "ganho semanal × total", RED), ("B", "4 semanas.", "comparou com os 1 000 iniciais", RED),
         ("C", "5 semanas.", "", GREEN), ("D", "6 semanas.", "contou hoje como 1ª semana", RED),
         ("E", "nenhum: B nunca ultrapassará A.", "", RED)]


def b_q5(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 5 · NÓS FAZEMOS", "LINEAR CONTRA EXPONENCIAL", GREEN)
    card(c, *CARD_R)
    a0 = ep(t, C["19.a"], 0.4)
    yend = _enunciado(c, [("Hoje, o perfil A de uma rede social tem 1 000 seguidores e ganha 300 novos seguidores por "
                           "semana, sempre o mesmo número. O perfil B tem hoje 100 seguidores, e esse número dobra a "
                           "cada semana. Mantidos esses ritmos, o menor número inteiro de semanas, contadas a partir de "
                           "hoje, ao fim do qual o perfil B terá mais seguidores que o perfil A é", INK)], a0, 236, 25)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0 * (1 - ep(t, C["20"], 0.3)),
         align="left")
    cues_in = {L: C[f"19.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"21.x{L.lower()}"] for L in "ABDE"}
    K.alternativas(c, t, C, ALTS5, 1000, 260, 680, 34, C["20.ok"], "C", cues_in, cues_x, gap=34)
    axe = ep(t, C["21.xe"], 0.4)
    if axe > 0:
        pill(c, "E: a exponencial sempre passa a reta", 1680, 730, RED, size=22, a=axe, anchor="right",
             bounds=(0, 1920))
    if t < C["20"]:
        pause_timer(c, t, C["19.end"] - 1.9, 540, yend + 100)
        return
    y0 = 206
    a1 = ep(t, C["20"], 0.4)
    _painel(c, y0, a1)
    if a1 > 0:
        linha(c, [("A = 1 000 + 300t", BLUE)], 540, y0 + 55, 32, a1)
        potencia(c, "2", "t", 540, y0 + 115, 34, ep(t, C["20"] + 2.4, 0.4), PURPLE, prefixo="B = 100 · ", col_pre=PURPLE)
    tx = [("20.a", "3", "1 900", "800"), ("20.b", "4", "2 200", "1 600"), ("20.c", "5", "2 500", "3 200")]
    yt = y0 + 175
    if a1 > 0:
        for j, s_ in enumerate(("t", "A", "B")):
            text(c, s_, 270 + j * 210, yt + 10, 30, "black", (INK, BLUE, PURPLE)[j], a1)
        line(c, 200, yt + 30, 880, yt + 30, LIGHT, a1, 2)
    for k, (cue, s_t, sa, sb) in enumerate(tx):
        ak = ep(t, C[cue], 0.4)
        if ak <= 0:
            continue
        y = yt + 90 + k * 80
        ok = k == 2
        if ok:
            rrect(c, 200, y - 50, 680, 76, 14, GREEN, 0.15 * ep(t, C["20.ok"], 0.4))
        text(c, s_t, 270, y, 34, "black", INK, ak)
        ftext(c, sa, 480, y, 34, "black", BLUE, ak)
        ftext(c, sb, 690, y, 34, "black", GREEN if ok else RED, ak)
        text(c, "B passa" if ok else "B perde", 840, y, 22, "bold", GREEN if ok else RED, ak, align="right")
    aok = ep(t, C["20.ok"], 0.4)
    if aok > 0:
        check_icon(c, 250, 790, 20, aok, GREEN)
        linha(c, [("5 semanas", GREEN)], 290, 792, 30, aok, align="left")


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "EQUAÇÕES EXPONENCIAIS", PURPLE)
    aa = ep(t, C["23.a"], 0.5)
    if aa > 0:
        potencia(c, "3", "t/2", W / 2, 320, 90, aa, PURPLE, prefixo="P(t) = 1 000 · ", col_pre=INK)
    ab = ep(t, C["23.b"], 0.5)
    if ab > 0:
        linha(c, [("P(t) = ", INK2), ("81 000", AMBER), ("   →   t = ?", INK)], W / 2, 480, 60, ab)
    acc = ep(t, C["23.c"], 0.5)
    if acc > 0:
        pill(c, "sem tentar um por um", W / 2, 610, GREEN, size=34, a=acc, anchor="center")
    ad = ep(t, C["23.d"], 0.5)
    if ad > 0:
        selo(c, W / 2, 740, ad, "PRÓXIMO EPISÓDIO", AMBER, -3, 40)


def b_cta(c, t, C, B):
    cta(c, t, C["24.like"], C["24.sub"], C["24.bell"], C["24.com"], C["24.bye"],
        "Você já viu alguma coisa crescer como a lebre, dobrando sem parar?", canal="no Estudativo",
        anki=C["24.anki"])


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, concreto=b_concreto, tabela=b_tabela,
              diferenca=b_diferenca, razao=b_razao, atalho_razao=b_atalho_razao, corrida=b_corrida, corrida2=b_corrida,
              tres=b_tres, atalho_tres=b_atalho_tres, pg=b_pg, exercicio=b_exercicio, recap=b_recap, erros=b_erros,
              q5=b_q5, ponte=b_ponte, cta=b_cta)
