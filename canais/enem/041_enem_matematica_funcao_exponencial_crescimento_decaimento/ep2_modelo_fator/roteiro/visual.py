"""Visual — Função Exponencial, Episódio 2: o modelo Q₀ · aᵗ, da frase do enunciado ao fator (tema claro).
Peças comuns da série em ../../comum.py (reexporta o 019/comum.py: expr, math_w, erro_cards, atalho, pause_timer...).
Peças deste episódio: fm() (fórmula com texto, potência e índice: "Q₀ · aᵗ", "60 000 · 0,85ᵗ"), maquina() (a máquina de
tradução: frase → fator → lei), barra100() (a barra de 100% perdendo 15% e o que SOBRA em destaque), tabela_t() (testar
t = 0, 1, 2), carrinho/predios/bacterias (as três histórias), fantasia() (M = C · (1 + i)ᵗ tirando a fantasia),
alts() (alternativas com fórmulas), grafico_q6() (os pontos da Questão 6).
Cores com função: azul = definição · roxo = regra/fórmula · âmbar = armadilha · verde = atalho/dica · vermelho = erro.
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
fr = K.fr
frame, head_seq, which, para, boxed, regra, selo, pause_timer, chip = (K.frame, K.head_seq, K.which, K.para, K.boxed, K.regra,
                                                                        K.selo, K.pause_timer, K.chip)
fmid, ftext, ftext_w = K.fmid, K.ftext, K.ftext_w

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_exponencial_ep2_modelo_fator.mp4"
CARD_R = K.CARD_R
PAPEL = K.PAPEL


# ======================================================================
# tipografia: fórmula mista (texto + potência + índice)
# ======================================================================

def _fm_w(p, size):
    kind = p[2] if len(p) > 2 else "t"
    if kind == "m":
        return K.math_w(p[0], size)
    if kind == "sub":
        return text_w(p[0], "black", size * 0.56)
    return text_w(p[0], "black", size)


def fm_w(partes, size):
    return sum(_fm_w(p, size) for p in partes)


def fm(c, partes, cx, cy, size, a, align="center"):
    """partes = [(texto, cor[, tipo])]; tipo 't' texto (mantém espaços), 'm' expr (potência: '0,85^t'), 'sub' índice.
    centrada verticalmente em cy; devolve a largura"""
    tw = fm_w(partes, size)
    if a <= 0:
        return tw
    x = cx - tw / 2 if align == "center" else (cx - tw if align == "right" else cx)
    for p in partes:
        s_, col = p[0], p[1] or INK
        kind = p[2] if len(p) > 2 else "t"
        w_ = _fm_w(p, size)
        if kind == "m":
            K.expr(c, s_, x, cy, size, a, cores={i: col for i in range(12)}, align="left")
        elif kind == "sub":
            text(c, s_, x, cy + size * 0.36 + size * 0.16, size * 0.56, "black", col, a, align="left")
        else:
            text(c, s_, x, cy + size * 0.36, size, "black", col, a, align="left")
        x += w_
    return tw


def Q0(col=BLUE):
    return [("Q", col), ("0", col, "sub")]


def conferido(c, s, x, y, a, ok=True, size=32):
    if a <= 0:
        return
    check_icon(c, x, y - size * 0.32, size * 0.62, a, GREEN if ok else RED, "check" if ok else "x")
    ftext(c, s, x + size * 0.95, y, size, "black", GREEN if ok else RED, a, align="left")


def linha(c, partes, cx, cy, size, a, peso="black"):
    if a <= 0:
        return 0
    ws = [text_w(s_, peso, size) for s_, _ in partes]
    x = cx - sum(ws) / 2
    for (s_, col), w_ in zip(partes, ws):
        text(c, s_, x, cy + size * 0.36, size, peso, col or INK, a, align="left")
        x += w_
    return sum(ws)


# ======================================================================
# peças do episódio
# ======================================================================

def carrinho(c, cx, cy, s, a, col=BLUE):
    if a <= 0:
        return
    rrect(c, cx - s, cy - s * 0.25, 2 * s, s * 0.5, s * 0.18, col, a)
    rrect(c, cx - s * 0.55, cy - s * 0.62, s * 1.0, s * 0.45, s * 0.18, col, a)
    rrect(c, cx - s * 0.42, cy - s * 0.54, s * 0.36, s * 0.3, s * 0.06, "#DCE6FF", a)
    rrect(c, cx + 0.02 * s, cy - s * 0.54, s * 0.36, s * 0.3, s * 0.06, "#DCE6FF", a)
    for fx in (-0.55, 0.55):
        c.drawCircle(cx + fx * s, cy + s * 0.27, s * 0.22, paint(INK, a))
        c.drawCircle(cx + fx * s, cy + s * 0.27, s * 0.09, paint("#C9CED6", a))


def predios(c, cx, by, s, a, n=5, cresce=1.0):
    """prédios de uma cidade (base em by); cresce escala as alturas"""
    if a <= 0:
        return
    hs = [0.9, 1.4, 1.1, 1.7, 1.0, 1.3]
    w = s * 0.34
    x0 = cx - n * (w + 6) / 2
    for k in range(n):
        h = s * hs[k % len(hs)] * cresce
        x = x0 + k * (w + 6)
        rrect(c, x, by - h, w, h, 4, mix(GREEN, INK, 0.25 + 0.1 * (k % 2)), a)
        for j in range(int(h // (s * 0.28))):
            rrect(c, x + w * 0.25, by - h + 10 + j * s * 0.28, w * 0.5, s * 0.1, 2, "#FFFFFF", a * 0.7)


def bacterias(c, cx, cy, n, a, r=14, col=None, maxcols=9):
    """n bolinhas (bactérias) em grade centrada"""
    if a <= 0 or n <= 0:
        return
    col = col or PURPLE
    cols = min(n, maxcols)
    rows = math.ceil(n / cols)
    gap = r * 2.5
    for k in range(n):
        i, j = k % cols, k // cols
        x = cx + (i - (cols - 1) / 2) * gap
        y = cy + (j - (rows - 1) / 2) * gap
        c.drawCircle(x, y, r, paint(mix("#FFFFFF", col, 0.35), a))
        c.drawCircle(x, y, r, paint(col, a, stroke=3))


def maquina(c, cx, cy, a, entrada, fator, u=1.0, col=PURPLE):
    """a máquina de tradução: frase (entrada, à esquerda) → caixa com engrenagem → fator (à direita). u anima a passagem"""
    if a <= 0:
        return
    bw, bh = 300, 190
    x, y = cx - bw / 2, cy - bh / 2
    rrect(c, x, y, bw, bh, 26, mix("#FFFFFF", col, 0.12), a, shadow=True)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, bw, bh), 26, 26), paint(col, a, stroke=4))
    # engrenagem
    gx, gy, gr = cx, cy - 6, 46
    ang = u * 360
    c.save(); c.translate(gx, gy); c.rotate(ang)
    for k in range(8):
        c.save(); c.rotate(k * 45)
        rrect(c, -9, -gr - 12, 18, 24, 4, col, a)
        c.restore()
    c.drawCircle(0, 0, gr, paint(col, a))
    c.drawCircle(0, 0, gr * 0.42, paint(mix("#FFFFFF", col, 0.12), a))
    c.restore()
    text(c, "TRADUTOR", cx, y + bh - 14, 20, "black", col, a, tracking=2)
    # entrada
    ew = max(300, text_w(entrada, "black", 30) + 50)
    ex = x - 80 - ew
    k_in = clamp(u / 0.45)
    rrect(c, ex + 12 * k_in, cy - 40, ew, 80, 18, "#FFFFFF", a, shadow=True)
    text_mid(c, entrada, ex + 12 * k_in + ew / 2, cy, 30, "black", INK, a * (1 - 0.3 * k_in))
    arrow(c, x - 52, cy, x - 8, cy, GRAY, a, 4, 14)
    # saída
    k_out = ep(u, 0.55, 0.45)
    if k_out > 0:
        arrow(c, x + bw + 8, cy, x + bw + 52, cy, GRAY, a * k_out, 4, 14)
        fw = max(200, text_w(fator, "black", 56) + 60)
        rrect(c, x + bw + 60, cy - 50, fw, 100, 22, mix("#FFFFFF", GREEN, 0.14), a * k_out, shadow=True)
        text_mid(c, fator, x + bw + 60 + fw / 2, cy, 56, "black", GREEN, a * k_out)
        text(c, "FATOR", x + bw + 60 + fw / 2, cy + 84, 20, "black", GREEN, a * k_out, tracking=2)


def barra100(c, x, y, w, h, a, u, perde=15):
    """barra de 100%: o pedaço de 'perde'% sai (u: 0 → 1) e o que SOBRA fica em destaque"""
    if a <= 0:
        return
    ws = w * (100 - perde) / 100
    wp = w - ws
    hl = ep(u, 0.6, 0.4)
    rrect(c, x, y, ws, h, 12, mix(mix("#FFFFFF", BLUE, 0.25), GREEN, hl), a)
    k = ease_io(clamp(u / 0.6))
    rrect(c, x + ws + 30 * k, y + 60 * k, wp, h, 12, mix("#FFFFFF", RED, 0.45), a * (1 - 0.5 * k))
    text_mid(c, f"{perde}%", x + ws + 30 * k + wp / 2, y + 60 * k + h / 2, 32, "black", RED, a * (1 - 0.3 * k))
    text_mid(c, f"{100 - perde}% SOBRA" if hl > 0.5 else "100%", x + ws / 2, y + h / 2, 40, "black",
             "#FFFFFF" if hl > 0.5 else INK, a)


def tabela_t(c, x, y, linhas, a, alfas=None, cw=(150, 330), rh=64, size=34, col=PURPLE, tit=("t", "valor")):
    """tabela de teste: linhas = [(t, valor)]; alfas por linha"""
    if a <= 0:
        return
    w = sum(cw)
    rrect(c, x, y, w, rh, 12, mix("#FFFFFF", col, 0.16), a)
    text_mid(c, tit[0], x + cw[0] / 2, y + rh / 2, size * 0.8, "black", col, a)
    text_mid(c, tit[1], x + cw[0] + cw[1] / 2, y + rh / 2, size * 0.8, "black", col, a)
    for k, (tt, vv) in enumerate(linhas):
        ak = a * (alfas[k] if alfas else 1)
        if ak <= 0:
            continue
        yy = y + rh * (k + 1)
        rrect(c, x, yy + 3, w, rh - 6, 10, "#FFFFFF", ak, shadow=True)
        text_mid(c, str(tt), x + cw[0] / 2, yy + rh / 2, size, "black", INK2, ak)
        text_mid(c, vv, x + cw[0] + cw[1] / 2, yy + rh / 2, size, "black", INK, ak)


def gravata(c, cx, cy, s, a, col=None):
    if a <= 0:
        return
    col = col or PURPLE
    p = skia.Path()
    p.moveTo(cx - s * 0.18, cy); p.lineTo(cx + s * 0.18, cy); p.lineTo(cx + s * 0.1, cy + s * 0.22)
    p.lineTo(cx - s * 0.1, cy + s * 0.22); p.close()
    c.drawPath(p, paint(col, a))
    p2 = skia.Path()
    p2.moveTo(cx - s * 0.1, cy + s * 0.22); p2.lineTo(cx + s * 0.1, cy + s * 0.22); p2.lineTo(cx + s * 0.22, cy + s * 0.85)
    p2.lineTo(cx, cy + s); p2.lineTo(cx - s * 0.22, cy + s * 0.85); p2.close()
    c.drawPath(p2, paint(col, a))


def pergunta(c, s, cx, cy, a, col=PURPLE, size=40):
    if a <= 0:
        return
    w = ftext_w(s, "black", size) + 80
    rrect(c, cx - w / 2, cy - 40, w, 80, 40, mix("#FFFFFF", col, 0.10), a)
    fmid(c, s, cx, cy, size, "black", col, a)


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "FUNÇÃO EXPONENCIAL", BLUE)
    aa = ep(t, C["01.a"], 0.5)
    if aa > 0:
        rrect(c, 200, 230, 560, 400, 26, "#FFFFFF", aa, shadow=True)
        carrinho(c, 480, 400, 130, aa)
        text(c, "R$ 60 000", 480, 560, 52, "black", INK, aa)
        pill(c, "−15% do valor por ano", 480, 600, AMBER, size=26, a=ep(t, C["01.a"] + 1.4, 0.4), anchor="center")
    ab = ep(t, C["01.b"], 0.5)
    if ab > 0:
        rrect(c, 860, 250, 860, 150, 24, mix("#FFFFFF", RED, 0.08), ab)
        fm(c, [("60 000 × ", INK), ("0,15", RED), (" = R$ 9 000", INK)], 1290, 325, 56, ab)
        sx = ep(t, C["01.c"], 0.5)
        if sx > 0:
            strike(c, 920, 325, 1660, 325, sx, RED, sx)
            pill(c, "ERRADO", 1680, 260, RED, size=22, a=sx, anchor="right")
    acc = ep(t, C["01.c"] + 0.6, 0.5)
    if acc > 0:
        rrect(c, 860, 450, 860, 150, 24, mix("#FFFFFF", GREEN, 0.10), acc)
        fm(c, [("60 000 × ", INK), ("0,85", GREEN), (" = R$ 51 000", GREEN)], 1290, 525, 56, acc)
        conferido(c, "certo", 1560, 650, ep(t, C["01.c"] + 1.4, 0.4), True, 32)
    ad = ep(t, C["01.d"], 0.5)
    if ad > 0:
        selo(c, 1000, 760, ad, "UM NÚMERO ERRADO NA LEI", AMBER, -3, 36)


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "AO FINAL DESTA AULA", "VOCÊ VAI CONSEGUIR", GREEN)
    aa, d = rise(t, C["02.a"])
    if aa > 0:
        text(c, "transformar qualquer frase de enunciado", W / 2, 320 + d, 46, "black", INK, aa)
    frases = [("dobra", "2"), ("cresce 3%", "1,03"), ("perde 15%", "0,85")]
    for k, (fz, fa) in enumerate(frases):
        ak = ep(t, C["02.a"] + 2.2 + 0.8 * k, 0.4)
        x = 480 + k * 480
        chip(c, fz, x, 440, BLUE, ak, 36)
        arrow(c, x, 490, x, 540, GRAY, ak, 4, 14)
        chip(c, fa, x, 590, GREEN, ak * ep(t, C["02.b"], 0.4), 40)
    ab = ep(t, C["02.b"], 0.5)
    if ab > 0:
        rrect(c, 560, 680, 800, 110, 26, mix("#FFFFFF", PURPLE, 0.10), ab)
        fm(c, [("numa LEI pronta:  ", PURPLE)] + Q0(BLUE) + [(" · ", INK), ("a^t", PURPLE, "m")], W / 2, 735, 48, ab)


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "DOIS LEMBRETES", "RÁPIDOS", GREEN)
    aa = ep(t, C["03.a"], 0.5)
    if aa > 0:
        text(c, "série de Porcentagem", 560, 290, 28, "bold", GRAY, aa)
        rrect(c, 230, 340, 660, 110, 20, mix("#FFFFFF", GREEN, 0.10), aa)
        fm(c, [("aumentar i%  →  × ", INK), ("(1 + i)", GREEN)], 560, 395, 42, aa)
        a2 = ep(t, C["03.a"] + 3.0, 0.4)
        rrect(c, 230, 480, 660, 110, 20, mix("#FFFFFF", RED, 0.08), a2)
        fm(c, [("descontar i%  →  × ", INK), ("(1 − i)", RED)], 560, 535, 42, a2)
    line(c, 960, 260, 960, 760, "#E6E6E2", aa, 3)
    ab = ep(t, C["03.b"], 0.5)
    if ab > 0:
        text(c, "série de Juros compostos", 1370, 290, 28, "bold", GRAY, ab)
        rrect(c, 1060, 380, 620, 150, 24, "#FFFFFF", ab, shadow=True)
        K.expr(c, "M = C · (1+i)^t", 1370, 455, 64, ab, cores={i: PURPLE for i in range(8)})
        selo(c, 1370, 640, ep(t, C["03.b"] + 3.2, 0.4), "VAI VOLTAR DISFARÇADA", AMBER, -3, 30)


def b_concreto(c, t, C, B):
    head(c, t, B["start"], "TRÊS HISTÓRIAS", "O QUE ELAS TÊM EM COMUM?", BLUE)
    card(c, *CARD_R)
    a1 = ep(t, C["04.a"], 0.5)
    boxes = [(220, "CARRO", "perde valor todo ano", AMBER), (730, "CIDADE", "cresce todo ano", GREEN),
             (1240, "BACTÉRIAS", "triplicam a cada hora", PURPLE)]
    for k, (x, tit, sub, col) in enumerate(boxes):
        ak = ep(t, C["04." + "abc"[k]], 0.5)
        if ak <= 0:
            continue
        rrect(c, x, 220, 460, 400, 24, "#FFFFFF", ak, shadow=True)
        rrect(c, x, 220, 460, 60, 24, col, ak * 0.14)
        text(c, tit, x + 230, 262, 28, "black", col, ak)
        text(c, sub, x + 230, 590, 28, "black", INK, ak)
        if k == 0:
            g = ep(t, C["04.a"] + 0.5, 2.0)
            carrinho(c, x + 230, 420, lerp(120, 80, g), ak)
        elif k == 1:
            predios(c, x + 230, 520, 120, ak, 5, lerp(0.7, 1.2, ep(t, C["04.b"] + 0.4, 2.0)))
        else:
            n = [1, 3, 9][min(2, int(ep(t, C["04.c"] + 0.3, 2.4) * 3))]
            bacterias(c, x + 230, 420, n, ak, 16)
    ad = ep(t, C["04.d"], 0.5)
    if ad > 0:
        regra(c, "a cada passo:  × o MESMO número", W / 2, 720, ad, 40)


# ======================================================================
# bloco a — a lei geral
# ======================================================================

def b_lei(c, t, C, B):
    head_seq(c, t, C, [("05", "A LEI GERAL", "UMA RECEITA COM 2 INGREDIENTES", PURPLE),
                       ("06", "O FATOR CONTA A HISTÓRIA", "CRESCE OU DECAI?", BLUE)])
    card(c, *CARD_R)
    sid = which(t, C, ["05", "06"])
    if sid == "05":
        aa = ep(t, C["05.a"], 0.5)
        if aa > 0:
            text(c, "LEI = a fórmula que dá o valor em cada instante", W / 2, 250, 32, "black", BLUE, aa)
        ab = ep(t, C["05.b"], 0.5)
        hq = ep(t, C["05.c"], 0.5)
        ha = ep(t, C["05.d"], 0.5)
        if ab > 0:
            fm(c, [("Q(t) = ", INK)] + Q0(mix(INK, BLUE, hq)) + [(" · ", INK), ("a^t", mix(INK, PURPLE, ha), "m")],
               W / 2, 400, 120, ab)
        if hq > 0:
            rrect(c, 260, 520, 640, 150, 22, mix("#FFFFFF", BLUE, 0.08), hq)
            fm(c, Q0(BLUE) + [("  =  VALOR INICIAL", BLUE)], 580, 565, 34, hq)
            text(c, "quanto vale no instante t = 0", 580, 630, 26, "bold", GRAY, hq)
        if ha > 0:
            rrect(c, 1020, 520, 640, 150, 22, mix("#FFFFFF", PURPLE, 0.08), ha)
            text_mid(c, "a  =  FATOR", 1340, 565, 34, "black", PURPLE, ha)
            text(c, "multiplica o valor a cada passo", 1340, 630, 26, "bold", GRAY, ha)
        ae = ep(t, C["05.e"], 0.5)
        if ae > 0:
            pill(c, "RECEITA: de onde começa  +  por quanto multiplica", W / 2, 750, PURPLE, size=30, a=ae,
                 anchor="center")
        return
    # cena 06: as duas curvas
    for k, (cue, s, cond, col, up) in enumerate((("06.a", "CRESCIMENTO", "a > 1", GREEN, True),
                                                ("06.b", "DECAIMENTO", "0 < a < 1", RED, False))):
        ak = ep(t, C[cue], 0.5)
        if ak <= 0:
            continue
        x0 = 260 + k * 760
        rrect(c, x0, 230, 640, 470, 24, "#FFFFFF", ak, shadow=True)
        text(c, s, x0 + 320, 280, 34, "black", col, ak)
        text_mid(c, cond, x0 + 320, 340, 48, "black", INK, ak)
        gx, gy, gw, gh = x0 + 80, 640, 480, 230
        line(c, gx, gy, gx + gw, gy, INK2, ak, 3)
        line(c, gx, gy, gx, gy - gh - 20, INK2, ak, 3)
        g = ep(t, C[cue] + 0.4, 1.4)
        p = skia.Path()
        n = 40
        for i in range(n + 1):
            u = i / n * g
            v = (2 ** (u * 3) - 1) / 7 if up else (0.5 ** (u * 3))
            px, py = gx + u * gw, gy - 20 - v * (gh - 20) * (1 if up else 1)
            if i == 0:
                p.moveTo(px, py)
            else:
                p.lineTo(px, py)
        c.drawPath(p, paint(col, ak, stroke=6, cap_round=True))
    ab = ep(t, C["06.b"] + 2.6, 0.5)
    if ab > 0:
        pill(c, "bem perdendo valor = DEPRECIAÇÃO", 1340, 750, BLUE, size=26, a=ab, anchor="center")


# ======================================================================
# bloco b — a tabela de tradução
# ======================================================================

def b_traducao(c, t, C, B):
    head_seq(c, t, C, [("07", "A MÁQUINA DE TRADUÇÃO", "FRASE → FATOR → LEI", PURPLE),
                       ("08", "O FATOR É O QUE SOBRA", "PERDE 15% → FICA COM 85%", PURPLE),
                       ("09", "TRIPLICA A CADA HORA", "FATOR 3", PURPLE)])
    card(c, *CARD_R)
    sid = which(t, C, ["07", "08", "09"])
    if sid == "07":
        a0 = ep(t, C["07.a"], 0.5)
        u = ep(t, C["07.c"], 1.6)
        maquina(c, 900, 360, a0, "cresce 3% ao ano", "1,03", u)
        ab = ep(t, C["07.b"], 0.5)
        if ab > 0:
            pill(c, "TAXA = a porcentagem que muda a cada passo", 520, 530, BLUE, size=26, a=ab, anchor="center")
        acc = ep(t, C["07.c"], 0.5)
        if acc > 0:
            fm(c, [("1 + 0,03 = ", INK), ("1,03", GREEN)], 1340, 540, 44, acc)
        ad = ep(t, C["07.d"], 0.5)
        if ad > 0:
            rrect(c, 360, 640, 1200, 130, 26, mix("#FFFFFF", PURPLE, 0.10), ad)
            fm(c, [("P = ", INK), ("200 000", BLUE), (" · ", INK), ("1,03^t", GREEN, "m")], W / 2, 705, 70, ad)
        return
    if sid == "08":
        a0 = ep(t, C["08"], 0.5)
        if a0 > 0:
            text(c, "carro de R$ 60 000 · perde 15% ao ano", W / 2, 230, 34, "black", INK, a0)
        aa = ep(t, C["08.a"], 0.5)
        u = ep(t, C["08.a"] + 0.6, 1.8)
        barra100(c, 260, 290, 900, 110, aa, u)
        ab = ep(t, C["08.b"], 0.5)
        if ab > 0:
            fm(c, [("1 − 0,15 = ", INK), ("0,85", GREEN)], 1460, 345, 54, ab)
        acc = ep(t, C["08.c"], 0.5)
        if acc > 0:
            rrect(c, 230, 500, 900, 130, 26, mix("#FFFFFF", PURPLE, 0.10), acc)
            fm(c, [("V = ", INK), ("60 000", BLUE), (" · ", INK), ("0,85^t", GREEN, "m")], 680, 565, 66, acc)
        alf = [ep(t, C["08.d"], 0.4), ep(t, C["08.e"], 0.4), ep(t, C["08.f"], 0.4)]
        tabela_t(c, 1190, 470, [(0, "60 000"), (1, "51 000"), (2, "43 350")], ep(t, C["08.d"], 0.4), alf)
        for k in (1, 2):
            if alf[k] > 0:
                pill(c, "× 0,85", 1684, 534 + 64 * k, GREEN, size=22, a=alf[k], anchor="left")
        return
    a0 = ep(t, C["09"], 0.5)
    maquina(c, 900, 330, a0, "triplica a cada hora", "3", ep(t, C["09.a"], 1.2))
    ab = ep(t, C["09.b"], 0.5)
    if ab > 0:
        rrect(c, 230, 500, 900, 130, 26, mix("#FFFFFF", PURPLE, 0.10), ab)
        fm(c, [("N = ", INK), ("500", BLUE), (" · ", INK), ("3^t", GREEN, "m")], 680, 565, 70, ab)
    acc = ep(t, C["09.c"], 0.4)
    if acc > 0:
        alf = [acc, ep(t, C["09.c"] + 1.0, 0.4), ep(t, C["09.c"] + 2.0, 0.4)]
        tabela_t(c, 1190, 470, [(0, "500"), (1, "1 500"), (2, "4 500")], acc, alf)
        for k in (1, 2):
            if alf[k] > 0:
                pill(c, "× 3", 1684, 534 + 64 * k, GREEN, size=22, a=alf[k], anchor="left")


# ======================================================================
# bloco c — juros compostos de terno e gravata
# ======================================================================

def b_disfarce(c, t, C, B):
    head(c, t, B["start"], "VOCÊ JÁ VIU ISSO", "DISFARÇADO", PURPLE)
    card(c, *CARD_R)
    a0 = ep(t, C["10"], 0.5)
    if a0 > 0:
        text(c, "R$ 1 000 a juros compostos de 2% ao mês", W / 2, 240, 34, "black", INK, a0)
    aa = ep(t, C["10.a"], 0.5)
    if aa > 0:
        fm(c, [("M = ", INK), ("1 000", BLUE), (" · ", INK), ("1,02^t", GREEN, "m")], W / 2, 330, 64, aa)
    ab = ep(t, C["10.b"], 0.5)
    u = ep(t, C["10.c"], 1.6)
    if ab > 0:
        # a fórmula de Juros compostos, de terno e gravata
        cx, cy = W / 2, 520
        rrect(c, cx - 380, cy - 90, 760, 180, 30, mix("#FFFFFF", PURPLE, 0.10), ab)
        K.expr(c, "M = C · (1+i)^t", cx, cy, 80, ab * (1 - 0.15 * u), cores={0: INK, 1: INK, 2: BLUE, 3: INK, 4: GREEN})
        gravata(c, cx - 470, cy - 70, 140, ab * (1 - u))
        text(c, "série de Juros compostos", cx, cy + 130, 26, "bold", GRAY, ab * (1 - u))
    if u > 0:
        cx = W / 2
        # setas: C → Q₀ · (1 + i) → a
        arrow(c, 830, 610, 700, 700, BLUE, u, 5, 16)
        arrow(c, 1090, 610, 1220, 700, GREEN, u, 5, 16)
        rrect(c, 520, 700, 880, 110, 26, "#FFFFFF", u, shadow=True)
        fm(c, [("C → ", BLUE)] + Q0(BLUE) + [("     ·     (1 + i) → ", GREEN), ("a", GREEN)], cx, 755, 44, u)
    ad = ep(t, C["10.d"], 0.5)
    if ad > 0:
        selo(c, 1540, 290, ad, "EXPONENCIAL DE TERNO E GRAVATA", PURPLE, -4, 24)


# ======================================================================
# atalho e bloco d
# ======================================================================

def b_atalho(c, t, C, B):
    head(c, t, B["start"], "ATALHO", "TAXA VIRA FATOR", GREEN)
    card(c, *CARD_R)
    aa = ep(t, C["11.a"], 0.5)
    rows = [("ganhou i%", "1 + i", "cresce 3%  →  1,03"), ("perdeu i%", "1 − i", "perde 15%  →  0,85"),
            ("dobrou", "2", ""), ("triplicou", "3", "")]
    K.atalho(c, 260, 200, 1400, 90, "TRADUÇÃO DIRETA", [""], aa, 30)
    for k, (fz, fa, ex) in enumerate(rows):
        ak = ep(t, C["11.a"] + 0.9 * k, 0.4)
        if ak <= 0:
            continue
        x = 300 + k * 340
        rrect(c, x, 310, 300, 220, 22, "#FFFFFF", ak, shadow=True)
        text(c, fz, x + 150, 365, 32, "black", INK, ak)
        arrow(c, x + 150, 390, x + 150, 430, GRAY, ak, 4, 12)
        text_mid(c, "× " + fa, x + 150, 475, 48, "black", GREEN, ak)
        if ex:
            text(c, ex, x + 150, 520, 20, "bold", GRAY, ak)
    ab = ep(t, C["11.b"], 0.5)
    if ab > 0:
        boxed(c, 300, 590, 1320, 170, GREEN, ab, 0.08)
        text(c, "CONFIRA COM  t = 0", W / 2, 640, 26, "black", GREEN, ab, tracking=2)
        fm(c, [("a", INK), ("^0", INK, "m"), (" = 1   →   Q(0) = ", INK)] + Q0(BLUE) + [("  (o valor inicial)", GRAY)],
           W / 2, 705, 44, ab)


def b_sobra(c, t, C, B):
    head(c, t, B["start"], "COPIAR O NÚMERO DA FRASE?", "O FATOR É O QUE SOBRA", AMBER)
    card(c, *CARD_R)
    rows = [("12.a", "perde 15%", "× 0,15", "o carro fica com só 15% do preço", RED),
            ("12.b", "cresce 3%", "× 3", "a cidade TRIPLICA em 1 ano", RED),
            ("12.c", "cresce 3%", "× 0,03", "a cidade ENCOLHE para 3%", RED)]
    for k, (cue, fz, fa, why, col) in enumerate(rows):
        ak = ep(t, C[cue], 0.5)
        if ak <= 0:
            continue
        y = 260 + k * 150
        rrect(c, 230, y - 55, 1460, 110, 20, "#F7F7F5", ak)
        text_mid(c, fz, 400, y, 38, "black", INK, ak, align="center")
        text_mid(c, fa, 700, y, 48, "black", RED, ak)
        sx = ep(t, C[cue] + 1.0, 0.4)
        if sx > 0:
            strike(c, 620, y, 780, y, sx, RED, sx)
        text_mid(c, why, 1230, y, 32, "black", AMBER, ep(t, C[cue] + 0.8, 0.4))
    ad = ep(t, C["12.d"], 0.5)
    if ad > 0:
        regra(c, "o fator é o que SOBRA:  perde 15% → × 0,85  ·  cresce 3% → × 1,03", W / 2, 730, ad, 36)


# ======================================================================
# bloco e — dois pontos
# ======================================================================

def b_pontos(c, t, C, B):
    head_seq(c, t, C, [("13", "SÓ DOIS VALORES?", "ACHE O VALOR INICIAL E O FATOR", PURPLE),
                       ("14", "ATALHO", "DIVIDA UM PELO OUTRO", GREEN)])
    card(c, *CARD_R)
    aa = ep(t, C["13.a"], 0.5)
    if aa > 0:
        rrect(c, 260, 210, 1400, 100, 22, "#F7F7F5", aa)
        fm(c, [("f(0) = ", INK), ("5", BLUE), ("        f(2) = ", INK), ("45", GREEN)], W / 2, 260, 52, aa)
    sid = which(t, C, ["13", "14"])
    if sid == "13":
        steps = [("13.b", [("f(0) = 5   →   ", INK)] + Q0(BLUE) + [(" = 5", BLUE)]),
                 ("13.c", [("f(2):   5 · ", INK), ("a^2", PURPLE, "m"), (" = 45", INK)]),
                 ("13.d", [("÷ 5:   ", AMBER), ("a^2", PURPLE, "m"), (" = 9", INK)]),
                 ("13.e", [("a = 3", GREEN), ("    (a base é positiva: −3 não serve)", GRAY)])]
        for k, (cue, partes) in enumerate(steps):
            ak, d = rise(t, C[cue])
            fm(c, partes, W / 2, 390 + k * 105 + d, 46, ak)
        return
    ab = ep(t, C["14.a"], 0.5)
    if ab > 0:
        K.atalho(c, 260, 350, 1400, 140, "ATALHO", ["45 ÷ 5 = 9"], ab, 44)
    acc = ep(t, C["14.b"], 0.5)
    if acc > 0:
        # dois passos: 0 → 1 → 2
        xs = [560, 960, 1360]
        for k, (x, v) in enumerate(zip(xs, ("5", "15", "45"))):
            chip(c, f"x = {k}", x, 560, GRAY, acc, 26, fill=False)
            text_mid(c, v, x, 630, 52, "black", BLUE if k == 0 else GREEN, acc * (1 if k != 1 else ep(t, C["14.c"], 0.4)))
        for k in range(2):
            arrow(c, xs[k] + 70, 630, xs[k + 1] - 70, 630, PURPLE, acc, 4, 14)
            text_mid(c, "× a", (xs[k] + xs[k + 1]) / 2, 590, 30, "black", PURPLE, acc)
        pill(c, "2 passos:  a · a = 9  →  a = 3", W / 2, 700, PURPLE, size=28, a=acc, anchor="center")
    ad = ep(t, C["14.c"], 0.5)
    if ad > 0:
        fm(c, [("f(x) = ", INK), ("5", BLUE), (" · ", INK), ("3^x", GREEN, "m")], 760, 790, 52, ad)
        conferido(c, "bateu", 1160, 805, ep(t, C["14.c"] + 2.0, 0.4), True, 32)


# ======================================================================
# nós fazemos
# ======================================================================

def b_exercicio(c, t, C, B):
    head_seq(c, t, C, [("15", "SUA VEZ", "PAUSE E TENTE", GREEN), ("16", "VAMOS JUNTOS", "LEI E CONTA", GREEN)])
    card(c, *CARD_R)
    aa = ep(t, C["15.a"], 0.5)
    if aa > 0:
        rrect(c, 230, 210, 1460, 130, 24, "#F7F7F5", aa)
        text(c, "cidade de 50 000 habitantes · cresce 2% ao ano", W / 2, 262, 40, "black", INK, aa)
        text(c, "a lei?   e daqui a 2 anos?", W / 2, 316, 32, "black", PURPLE, aa)
    pause_timer(c, t, C["15.end"] - 1.9, W / 2, 560)
    if t < C["16"]:
        return
    a1 = ep(t, C["16.a"], 0.5)
    if a1 > 0:
        fm(c, [("P = ", INK), ("50 000", BLUE), (" · ", INK), ("1,02^t", GREEN, "m")], W / 2, 440, 66, a1)
    ab = ep(t, C["16.b"], 0.5)
    if ab > 0:
        fm(c, [("1,02^2", PURPLE, "m"), (" = 1 + 0,04 + 0,0004 = ", INK), ("1,0404", GREEN)], W / 2, 570, 46, ab)
        pill(c, "atalho da série de Juros", W / 2, 640, GREEN, size=24, a=ab, anchor="center")
    acc = ep(t, C["16.c"], 0.5)
    if acc > 0:
        linha(c, [("50 000 · 1,0404 = ", INK), ("52 020 habitantes", GREEN)], W / 2, 745, 54, acc)


# ======================================================================
# recap, erros
# ======================================================================

FRASES = ["Com o valor inicial e o fator, a lei sai sozinha.",
          "O fator é o que sobra: perder 15% é multiplicar por 0,85.",
          "Juros compostos são a mesma exponencial com outro nome."]


def b_recap(c, t, C, B):
    sid = which(t, C, ["17", "27"])
    frame(c, t, B["start"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "17" else "PARA FECHAR", PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 300 + k * 180 + d
        badge_num(c, k + 1, 260, y - 16, a, 36, bg=PURPLE)
        para(c, s, 320, y, 50, "black", INK, a, 1360, 60)


ERROS = [("Perde 15%  →  fator 0,15", "o 15 está escrito no enunciado",
          "o fator é o que SOBRA: 1 − 0,15 = 0,85"),
         ("Cresce 3%  →  fator 3", "é o número da frase",
          "fator 3 é TRIPLICAR: a taxa vira fator somando 1 → 1,03"),
         ("3 · 2ˣ  =  6ˣ", "3 · 2 = 6",
          "a potência vem ANTES: x = 2 dá 3 · 4 = 12, e não 6² = 36")]


def b_erros(c, t, C, B):
    K.erro_cards(c, t, C, ["18", "19", "20"], ERROS)


# ======================================================================
# questões do material
# ======================================================================

def _painel(c, y0, a, y1=830):
    rrect(c, 170, y0, 740, y1 - y0, 18, "#FFFFFF", a, shadow=True)


def alts(c, t, C, itens, x, y0, size, ok_cue, okL, cues_in, cues_x, gap=26, wmot=None):
    """alternativas com fórmula mista: itens = [(letra, partes_fm, motivo)]"""
    aok = ep(t, ok_cue, 0.5)
    y = y0
    hh = size * 1.7
    for L, partes, why in itens:
        a, d = rise(t, cues_in.get(L, 1e9))
        ok = L == okL
        ax = ep(t, cues_x.get(L, 1e9), 0.4) if not ok else 0
        if a > 0:
            if ok and aok > 0:
                rrect(c, x - 20, y - 10 + d, 720, hh + 20, 14, GREEN, 0.15 * aok)
            badge_num(c, L, x + 10, y + hh / 2 + d, a, 22, bg=GREEN if ok and aok > 0.5 else INK)
            cyy = y + d + hh / 2
            w_ = fm(c, partes, x + 50, cyy, size, a * (1 - 0.5 * ax), align="left")
            if ax > 0:
                strike(c, x + 46, cyy, x + 54 + w_, cyy, ax, RED, ax)
                if why:
                    pill(c, why, x + 700, cyy + size * 0.95, RED, size=18, a=ax, anchor="right", bounds=(0, 1920))
        y += hh + gap
    return y


ALTS3 = [("A", [("V = 50 000 − 10 000t", INK)], "em t = 2 dá 30 000"),
         ("B", [("V = 50 000 · ", INK), ("0,2^t", INK, "m")], "taxa de perda como fator"),
         ("C", [("V = 40 000 · ", INK), ("0,8^t", INK, "m")], "em t = 0 dá 40 000"),
         ("D", [("V = 50 000 · 0,8t", INK)], "produto: em t = 0 dá 0"),
         ("E", [("V = 50 000 · ", INK), ("0,8^t", INK, "m")], "")]


def b_q3(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 3 · EU FAÇO", "A LEI A PARTIR DA TABELA", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["21.a"], 0.4)
    y = 240
    for ln in K.wrap("Uma revista especializada publicou o valor de mercado estimado de um modelo de máquina agrícola ao "
                     "longo dos anos após a compra:", "black", 26, 700):
        text(c, ln, 190, y, 26, "black", INK, a0, align="left")
        y += 36
    # tabela do enunciado (vertical)
    vals = ["50 000", "40 000", "32 000", "25 600"]
    tabela_t(c, 200, y, list(zip(range(4), vals)), a0, None, cw=(220, 300), rh=52, size=28, col=BLUE,
             tit=("anos", "valor (R$)"))
    yq = y + 52 * 5 + 24
    ab = ep(t, C["21.b"], 0.4)
    for ln in K.wrap("A expressão que fornece o valor V, em reais, após t anos, compatível com todos os dados da tabela, é",
                     "black", 24, 700):
        text(c, ln, 190, yq, 24, "black", INK, ab, align="left")
        yq += 32
    # razões ao lado da tabela, na resolução
    for k, cue in enumerate(("22.a", "22.b", "22.c")):
        ak = ep(t, C[cue], 0.4)
        if ak > 0:
            yy = y + 52 * (k + 1) + 52
            pill(c, "× 0,8", 790, yy, GREEN, size=22, a=ak, anchor="center")
    ad = ep(t, C["22.d"], 0.4)
    if ad > 0:
        pill(c, "sempre × 0,8 → EXPONENCIAL (perde 20% ao ano)", 540, yq + 30, PURPLE, size=22, a=ad, anchor="center")
    ae = ep(t, C["22.e"], 0.4)
    if ae > 0:
        conferido(c, "t = 0 → 50 000", 230, yq + 90, ae, True, 26)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0 * (1 - ep(t, C["22"], 0.3)),
         align="left")
    cues_in = {L: C[f"21.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"23.x{L.lower()}"] for L in "ABCD"}
    alts(c, t, C, ALTS3, 1000, 250, 38, C["22.ok"], "E", cues_in, cues_x)


ALTS6 = [("A", [("16,5", INK)], "ligou por uma reta"), ("B", [("18", INK)], "3 · 2 · 3: produto"),
         ("C", [("24", INK)], ""), ("D", [("36", INK)], "supôs a = 3"), ("E", [("48", INK)], "12 · 4: dois passos")]


def grafico_q6(c, x, y, w, h, a, pts, a3=0.0, reta=0.0):
    """eixos com os pontos (0, 3), (2, 12) e, se a3 > 0, a curva até (3, 24)"""
    if a <= 0:
        return
    rrect(c, x, y, w, h, 18, "#FFFFFF", a, shadow=True)
    ox, oy = x + 70, y + h - 50
    sx, sy = (w - 120) / 3.2, (h - 90) / 26
    line(c, ox, oy, ox + 3.2 * sx, oy, INK2, a, 3)
    line(c, ox, oy, ox, oy - 26 * sy, INK2, a, 3)
    for k in range(4):
        text(c, str(k), ox + k * sx, oy + 32, 20, "bold", GRAY, a)
    if a3 > 0:
        p = skia.Path()
        for i in range(61):
            xx = 3 * i / 60 * a3
            yy = 3 * 2 ** xx
            px, py = ox + xx * sx, oy - yy * sy
            p.lineTo(px, py) if i else p.moveTo(px, py)
        c.drawPath(p, paint(GREEN, a, stroke=5, cap_round=True))
    if reta > 0:
        line(c, ox, oy - 3 * sy, ox + 3 * sx, oy - 16.5 * sy, RED, a * reta, 4, dash=(14, 10))
    for (px_, py_, lbl, al) in pts:
        if al <= 0:
            continue
        cx_, cy_ = ox + px_ * sx, oy - py_ * sy
        c.drawCircle(cx_, cy_, 11, paint("#FFFFFF", a * al)); c.drawCircle(cx_, cy_, 8, paint(BLUE, a * al))
        text(c, lbl, cx_ + 14, cy_ - 14, 22, "black", BLUE, a * al, align="left")


def b_q6(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 6 · VOCÊ FAZ", "LEI POR DOIS PONTOS", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["24.a"], 0.4)
    y = 240
    enun = ("O gráfico de uma função do tipo f(x) = k · aˣ, com k > 0 e a > 0, passa pelos pontos (0, 3) e (2, 12). "
            "O valor de f(3) é")
    for ln in K.wrap(enun, "black", 26, 700):
        ftext(c, ln, 190, y, 26, "black", INK, a0, align="left")
        y += 36
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0 * (1 - ep(t, C["25"], 0.3)),
         align="left")
    cues_in = {L: C[f"24.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"26.x{L.lower()}"] for L in "ABDE"}
    alts(c, t, C, ALTS6, 1000, 250, 40, C["25.ok"], "C", cues_in, cues_x)
    if t < C["25"]:
        grafico_q6(c, 200, y + 20, 680, 830 - y - 40, a0, [(0, 3, "(0, 3)", 1), (2, 12, "(2, 12)", 1)])
        pause_timer(c, t, C["24.end"] - 1.9, 760, y + 120)
        return
    y0 = y + 10
    _painel(c, y0, ep(t, C["25"], 0.4))
    fm(c, [("f(0) = k = ", INK), ("3", BLUE)], 540, y0 + 50, 34, ep(t, C["25.a"], 0.4))
    fm(c, [("3 · ", INK), ("a^2", PURPLE, "m"), (" = 12  →  ", INK), ("a^2", PURPLE, "m"), (" = 4  →  ", INK),
           ("a = 2", GREEN)], 540, y0 + 125, 32, ep(t, C["25.b"], 0.4))
    fm(c, [("f(3) = 3 · ", INK), ("2^3", PURPLE, "m"), (" = 3 · 8 = ", INK), ("24", GREEN)], 540, y0 + 200, 36,
       ep(t, C["25.c"], 0.4))
    ad = ep(t, C["25.d"], 0.4)
    if ad > 0:
        pill(c, "de x = 2 para x = 3: UM passo → 12 × 2 = 24", 540, y0 + 270, GREEN, size=22, a=ad, anchor="center")


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "DUPLICAÇÃO E MEIA-VIDA", PURPLE)
    aa = ep(t, C["28.a"], 0.5)
    if aa > 0:
        rrect(c, 260, 260, 640, 360, 26, "#FFFFFF", aa, shadow=True)
        n = 1 + int(ep(t, C["28.a"] + 0.6, 2.4) * 7)
        bacterias(c, 580, 420, min(16, 2 ** (n // 2)), aa, 16, PURPLE, 8)
        text(c, "1 000 bactérias", 580, 290 + 300, 32, "black", INK, aa)
        pill(c, "dobram a cada 30 min", 580, 660, PURPLE, size=26, a=aa, anchor="center")
    ab = ep(t, C["28.b"], 0.5)
    if ab > 0:
        text(c, "depois de 3 h:", 1330, 360, 40, "black", INK, ab)
        text_mid(c, "6 000 ?", 1330, 470, 110, "black", AMBER, ab)
    acc = ep(t, C["28.c"], 0.5)
    if acc > 0:
        strike(c, 1150, 470, 1510, 470, acc, RED, acc)
        selo(c, 1330, 600, acc, "NEM PERTO", RED, -4, 40)
    pill(c, "ep. 3 · duplicação e meia-vida: conte os intervalos", W / 2, 790, PURPLE, size=30, a=ep(t, C["28.d"], 0.5),
         anchor="center")


def b_cta(c, t, C, B):
    cta(c, t, C["29.like"], C["29.sub"], C["29.bell"], C["29.com"], C["29.bye"],
        "Você já tinha caído no fator 0,15?", canal="no Estudativo", anki=C["29.anki"])


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, concreto=b_concreto, lei=b_lei, traducao=b_traducao,
              disfarce=b_disfarce, atalho=b_atalho, sobra=b_sobra, pontos=b_pontos, exercicio=b_exercicio,
              recap=b_recap, erros=b_erros, q3=b_q3, q6=b_q6, ponte=b_ponte, cta=b_cta)
