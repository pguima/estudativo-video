"""Visual — Expressões Algébricas e Produtos Notáveis, Episódio 1: linguagem algébrica, valor numérico e operações com
polinômios (tema claro).
Peças comuns da série em ../../comum.py (reexporta o 019/comum.py: expr, alternativas, erro_cards, atalho...).
Peças deste episódio: app() (tela do aplicativo de transporte), caixinha() (a letra que abre e recebe o número já de
parênteses), maca()/banana() (termos semelhantes = frutas iguais), parenteses() + apertos() (a distributiva como aperto de
mão, com os 4 arcos), espelho() (o menos antes do parêntese virando os sinais), folha_caixa() (a folha 30 × 20 da Q6).
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
_s = importlib.util.spec_from_file_location("comum034", _p)
K = importlib.util.module_from_spec(_s); _s.loader.exec_module(K)
K.usar_tempos(Path(__file__).resolve().parents[1] / "audio" / "tempos.json")
motor.set_theme("claro")
fr = K.fr
frame, head_seq, which, para, boxed, regra, selo, pause_timer, chip = (K.frame, K.head_seq, K.which, K.para, K.boxed, K.regra,
                                                                        K.selo, K.pause_timer, K.chip)
fmid, ftext, ftext_w, expr = K.fmid, K.ftext, K.ftext_w, K.expr

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_expressoes_ep1_linguagem_polinomios.mp4"
CARD_R = K.CARD_R
MACA = "#E2483D"
BANANA = "#F2C531"
CAIXA = "#D9B47A"
CAIXA2 = "#C49A5A"


# ======================================================================
# peças do episódio
# ======================================================================

def linha(c, partes, cx, cy, size, a, peso="black", align="center"):
    """texto numa linha com cor por trecho: partes = [(texto, cor)]. Devolve [(x_ini, largura)] de cada trecho."""
    ws = [ftext_w(s_, peso, size) for s_, _ in partes]
    x = cx - sum(ws) / 2 if align == "center" else cx
    pos = []
    for (s_, col), w_ in zip(partes, ws):
        if a > 0:
            fmid(c, s_, x, cy, size, peso, col or INK, a, align="left")
        pos.append((x, w_))
        x += w_
    return pos


def conferido(c, s, x, y, a, ok=True, size=32):
    if a <= 0:
        return
    check_icon(c, x, y - size * 0.32, size * 0.62, a, GREEN if ok else RED, "check" if ok else "x")
    ftext(c, s, x + size * 0.95, y, size, "black", GREEN if ok else RED, a, align="left")


def app(c, x, y, a, linhas_on=(1, 1)):
    """celular com o aplicativo de transporte: tarifa e duas corridas de exemplo"""
    if a <= 0:
        return
    w, h = 360, 560
    rrect(c, x, y, w, h, 46, INK, a, shadow=True)
    rrect(c, x + 14, y + 14, w - 28, h - 28, 34, "#FFFFFF", a)
    rrect(c, x + w / 2 - 50, y + 26, 100, 14, 7, INK, a)
    text(c, "SUA CORRIDA", x + w / 2, y + 92, 24, "black", GRAY, a, tracking=2)
    rrect(c, x + 34, y + 120, w - 68, 130, 20, mix("#FFFFFF", BLUE, 0.10), a)
    text(c, "R$ 6,00 fixos", x + w / 2, y + 172, 34, "black", INK, a)
    text(c, "+ R$ 2,50 por km", x + w / 2, y + 222, 30, "black", BLUE, a)
    for k, (km, val) in enumerate((("2 km", "R$ 11,00"), ("10 km", "R$ 31,00"))):
        ak = a * linhas_on[k]
        if ak <= 0:
            continue
        yy = y + 300 + k * 110
        rrect(c, x + 34, yy, w - 68, 90, 18, "#F4F4F2", ak)
        text(c, km, x + 60, yy + 56, 30, "black", INK2, ak, align="left")
        text(c, val, x + w - 60, yy + 56, 30, "black", GREEN, ak, align="right")


def caixinha(c, cx, cy, s, a, abre=0.0, conteudo="", desce=0.0, rotulo="x", col_cont=None):
    """caixinha com a letra na frente; abre (0 → 1) levanta a tampa; o conteúdo (ex.: '(−2)') desce para dentro"""
    if a <= 0:
        return
    w, h = s * 1.6, s * 1.1
    x0, y0 = cx - w / 2, cy - h / 2
    rrect(c, x0, y0, w, h, s * 0.12, CAIXA, a, shadow=True)
    c.drawRect(skia.Rect.MakeXYWH(x0, y0 + h * 0.18, w, h * 0.06), paint(CAIXA2, a))
    fmid(c, rotulo, cx, cy + h * 0.14, s * 0.7, "black", "#FFFFFF", a)
    # tampa: gira em torno da dobradiça da esquerda
    ang = 115 * ease_io(clamp(abre))
    c.save(); c.translate(x0 + w, y0); c.rotate(ang)
    rrect(c, -w - s * 0.06, -s * 0.22, w + s * 0.12, s * 0.24, s * 0.06, CAIXA2, a)
    c.restore()
    if conteudo and desce > 0:
        yy = lerp(cy - s * 2.0, y0 - s * 0.42, ease_io(clamp(desce)))
        rrect(c, cx - s * 0.62, yy - s * 0.4, s * 1.24, s * 0.8, s * 0.2, "#FFFFFF", a * clamp(desce * 3))
        fmid(c, conteudo, cx, yy, s * 0.56, "black", col_cont or RED, a * clamp(desce * 3))


def maca(c, cx, cy, r, a, rot=""):
    if a <= 0:
        return
    c.drawCircle(cx - r * 0.32, cy, r * 0.78, paint(MACA, a))
    c.drawCircle(cx + r * 0.32, cy, r * 0.78, paint(MACA, a))
    line(c, cx, cy - r * 0.6, cx + r * 0.12, cy - r * 1.05, "#6B4A2B", a, r * 0.14)
    c.save(); c.translate(cx + r * 0.36, cy - r * 0.9); c.rotate(-25)
    c.drawOval(skia.Rect.MakeXYWH(-r * 0.3, -r * 0.13, r * 0.6, r * 0.26), paint(GREEN, a))
    c.restore()
    c.drawCircle(cx - r * 0.42, cy - r * 0.25, r * 0.16, paint("#FFFFFF", a * 0.45))
    if rot:
        fmid(c, rot, cx, cy + r * 0.12, r * 0.62, "black", "#FFFFFF", a)


def banana(c, cx, cy, r, a, rot=""):
    if a <= 0:
        return
    p = skia.Path()
    p.moveTo(cx - r * 1.05, cy - r * 0.35)
    p.quadTo(cx, cy + r * 1.0, cx + r * 1.05, cy - r * 0.35)
    c.drawPath(p, paint(BANANA, a, stroke=r * 0.62, cap_round=True))
    c.drawPath(p, paint("#D9A520", a * 0.5, stroke=r * 0.06))
    for sx in (-1, 1):
        c.drawCircle(cx + sx * r * 1.05, cy - r * 0.35, r * 0.13, paint("#5A3E1E", a))
    if rot:
        fmid(c, rot, cx, cy + r * 0.25, r * 0.5, "black", INK, a)


def parenteses(c, A, B, cx, cy, size, a, colA=BLUE, colB=GREEN):
    """(A0 ± A1)(B0 ± B1); A = [termo0, sinal1, termo1]. Devolve os centros x dos 4 termos [A0, A1, B0, B1]."""
    partes = [("(", INK), (A[0], colA), (f" {A[1]} ", INK), (A[2], colA), (")(", INK),
              (B[0], colB), (f" {B[1]} ", INK), (B[2], colB), (")", INK)]
    pos = linha(c, partes, cx, cy, size, a)
    return [pos[i][0] + pos[i][1] / 2 for i in (1, 3, 5, 7)]


def apertos(c, xs, cy, size, alfas, u=None):
    """os 4 apertos de mão: A0→B0, A0→B1 (arcos por cima), A1→B0, A1→B1 (por baixo). alfas = 4 valores."""
    pares = [(0, 2, -1, 1.0), (0, 3, -1, 1.55), (1, 2, 1, 1.0), (1, 3, 1, 1.55)]
    cols = [PURPLE, PURPLE, AMBER, AMBER]
    for k, (i, j, sg, hh) in enumerate(pares):
        al = alfas[k]
        if al <= 0:
            continue
        x1, x2 = xs[i], xs[j]
        y = cy + sg * size * 0.62
        top = y + sg * size * 0.75 * hh
        p = skia.Path(); p.moveTo(x1, y); p.quadTo((x1 + x2) / 2, top, x2, y)
        c.drawPath(p, paint(cols[k], al, stroke=5, cap_round=True))
        # mãozinha que viaja pelo arco
        g = clamp(al * 1.4 - 0.2)
        px = (1 - g) ** 2 * x1 + 2 * (1 - g) * g * (x1 + x2) / 2 + g ** 2 * x2
        py = (1 - g) ** 2 * y + 2 * (1 - g) * g * top + g ** 2 * y
        c.drawCircle(px, py, 10, paint(cols[k], al))
        badge_num(c, k + 1, (x1 + x2) / 2, (y + top) / 2 + sg * 6, al, 17, bg=cols[k])


def produtos(c, itens, cx, cy, size, alfas, cols=None, gap=30):
    """fichas dos 4 produtos em linha"""
    cols = cols or [PURPLE, PURPLE, AMBER, AMBER]
    ws = [max(size * 2.2, ftext_w(s_, "black", size) + size * 0.9) for s_ in itens]
    x = cx - (sum(ws) + gap * (len(ws) - 1)) / 2
    for k, (s_, w_) in enumerate(zip(itens, ws)):
        al = alfas[k]
        if al > 0:
            rrect(c, x, cy - size * 0.8, w_, size * 1.6, size * 0.35, mix("#FFFFFF", cols[k], 0.14), al)
            c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, cy - size * 0.8, w_, size * 1.6), size * 0.35,
                                              size * 0.35), paint(cols[k], al, stroke=3))
            fmid(c, s_, x + w_ / 2, cy, size, "black", INK, al)
        x += w_ + gap


def folha_caixa(c, x, y, u, a, mostra_x=True, fundo=0.0):
    """folha 30 × 20 (u px por cm) com um quadrado de lado x (3 cm no desenho) em cada canto; fundo realça o miolo"""
    if a <= 0:
        return
    w, h, q = 30 * u, 20 * u, 3 * u
    rrect(c, x, y, w, h, 6, PAPEL_CX, a, shadow=True)
    for (qx, qy) in ((x, y), (x + w - q, y), (x, y + h - q), (x + w - q, y + h - q)):
        c.drawRect(skia.Rect.MakeXYWH(qx, qy, q, q), paint(mix("#FFFFFF", RED, 0.25), a))
        c.drawRect(skia.Rect.MakeXYWH(qx, qy, q, q), paint(RED, a, stroke=3))
    if fundo > 0:
        c.drawRect(skia.Rect.MakeXYWH(x + q, y + q, w - 2 * q, h - 2 * q), paint(mix("#FFFFFF", GREEN, 0.3), a * fundo))
        c.drawRect(skia.Rect.MakeXYWH(x + q, y + q, w - 2 * q, h - 2 * q), paint(GREEN, a * fundo, stroke=4))
        fmid(c, "fundo", x + w / 2, y + h / 2, u * 1.6, "black", GREEN, a * fundo)
    c.drawRect(skia.Rect.MakeXYWH(x, y, w, h), paint(CAIXA2, a, stroke=3))
    fmid(c, "30 cm", x + w / 2, y - 22, 24, "black", INK2, a)
    fmid(c, "20 cm", x - 48, y + h / 2, 24, "black", INK2, a)
    if mostra_x:
        fmid(c, "x", x + q / 2, y + q / 2, u * 1.4, "black", RED, a)
        fmid(c, "x", x + w - q / 2, y + h - q / 2, u * 1.4, "black", RED, a)


PAPEL_CX = "#EFE3C8"


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
    head(c, t, B["start"], "MATEMÁTICA ENEM", "EXPRESSÕES ALGÉBRICAS", BLUE)
    rows = [("01.a", "o dobro de um número, aumentado de 3", "2x + 3", "2·5 + 3 = 13", BLUE),
            ("01.b", "o dobro da soma de um número com 3", "2(x+3)", "2·(5+3) = 16", PURPLE)]
    for k, (cue, frase, ex, val, col) in enumerate(rows):
        a = ep(t, C[cue], 0.5)
        if a <= 0:
            continue
        y = 260 + k * 220
        rrect(c, 200, y, 1520, 180, 26, "#FFFFFF", a, shadow=True)
        rrect(c, 200, y, 14, 180, 7, col, a)
        text(c, f"“{frase}”", 250, y + 70, 40, "black", INK, a, align="left")
        expr(c, ex, 250, y + 132, 54, a, cores={i: col for i in range(5)}, align="left")
        ac = ep(t, C["01.c"] + 1.2 * k, 0.5)
        if ac > 0:
            rrect(c, 1250, y + 40, 420, 100, 20, mix("#FFFFFF", GREEN if k == 0 else AMBER, 0.14), ac)
            text(c, "com x = 5", 1460, y + 76, 22, "bold", GRAY, ac)
            text(c, val, 1460, y + 122, 38, "black", INK, ac)
    ad = ep(t, C["01.d"], 0.5)
    if ad > 0:
        selo(c, W / 2, 760, ad, "NO ENEM, AS DUAS ESTÃO NAS ALTERNATIVAS", AMBER, -2, 36)


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "AO FINAL DESTA AULA", "VOCÊ VAI CONSEGUIR", GREEN)
    rows = [("02.a", "traduzir frases em expressões", "“o dobro da soma” → 2(x + 3)"),
            ("02.b", "calcular o valor sem errar sinal", "x = −2  →  sempre (−2)"),
            ("02.c", "multiplicar polinômios sem perder termo", "(2x + 3)(x − 4): 4 produtos")]
    for j, (cue, s, sub) in enumerate(rows):
        a, d = rise(t, C[cue])
        y = 320 + j * 170 + d
        check_icon(c, 300, y - 14, 34, a, GREEN)
        text(c, s, 360, y, 48, "black", INK, a, align="left")
        ftext(c, sub, 360, y + 56, 32, "bold", GRAY, a, align="left")


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "DOIS LEMBRETES", "RÁPIDOS", GREEN)
    aa = ep(t, C["03.a"], 0.5)
    if aa > 0:
        text(c, "SINAIS", 560, 280, 34, "black", BLUE, aa)
        text(c, "série de Operações", 560, 324, 24, "bold", GRAY, aa)
        linha(c, [("(−) · (−) = ", INK), ("+", GREEN)], 560, 410, 52, aa)
        a2 = ep(t, C["03.a"] + 2.0, 0.4)
        expr(c, "-3^2 = -9", 560, 530, 64, a2, cores={2: RED})
        text(c, "o quadrado pega só o 3", 560, 600, 24, "bold", GRAY, a2)
        a3 = ep(t, C["03.a"] + 4.2, 0.4)
        expr(c, "(-3)^2 = 9", 560, 690, 64, a3, cores={2: GREEN})
    ab = ep(t, C["03.b"], 0.5)
    if ab > 0:
        text(c, "POTÊNCIAS", 1360, 280, 34, "black", PURPLE, ab)
        text(c, "série de Potenciação", 1360, 324, 24, "bold", GRAY, ab)
        expr(c, "x^2 · x^3 = x^5", 1360, 450, 64, ab, cores={4: GREEN})
        text(c, "soma os expoentes", 1360, 520, 24, "bold", GRAY, ab)
        a2 = ep(t, C["03.b"] + 2.6, 0.4)
        expr(c, "(3x)^2 = 9x^2", 1360, 640, 64, a2, cores={2: GREEN})
        text(c, "o expoente pega o 3 também", 1360, 710, 24, "bold", GRAY, a2)
    line(c, 960, 240, 960, 760, "#E6E6E2", ab, 3)


def b_concreto(c, t, C, B):
    head(c, t, B["start"], "UM APLICATIVO DE TRANSPORTE", "A MESMA REGRA PARA QUALQUER DISTÂNCIA", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["04.a"], 0.5)
    app(c, 260, 220, aa, (ep(t, C["04.b"], 0.4), ep(t, C["04.b"] + 2.0, 0.4)))
    ab = ep(t, C["04.b"], 0.5)
    if ab > 0:
        linha(c, [("6 + 2,5 · ", INK), ("2", BLUE), (" = 11", GREEN)], 1150, 320, 52, ab)
        linha(c, [("6 + 2,5 · ", INK), ("10", BLUE), (" = 31", GREEN)], 1150, 420, 52, ep(t, C["04.b"] + 2.0, 0.4))
    acc = ep(t, C["04.c"], 0.5)
    if acc > 0:
        pill(c, "a regra é a mesma · só muda a distância", 1150, 510, AMBER, size=28, a=acc, anchor="center")
    ad = ep(t, C["04.d"], 0.5)
    if ad > 0:
        rrect(c, 760, 580, 780, 200, 26, mix("#FFFFFF", BLUE, 0.08), ad)
        pos = linha(c, [("6 + 2,5", INK), ("x", RED)], 1150, 650, 96, ad)
        xx = pos[1][0] + pos[1][1] / 2
        arrow(c, xx + 70, 740, xx + 10, 690, RED, ad, 4, 14)
        text(c, "qualquer distância", xx + 80, 755, 28, "black", RED, ad, align="left")


# ======================================================================
# bloco a — vocabulário
# ======================================================================

def b_vocab(c, t, C, B):
    head_seq(c, t, C, [("05", "VOCABULÁRIO", "VARIÁVEL · EXPRESSÃO · TERMO", BLUE),
                       ("06", "UM TERMO POR DENTRO", "COEFICIENTE · PARTE LITERAL", BLUE)])
    card(c, *CARD_R)
    sid = which(t, C, ["05", "06"])
    if sid == "05":
        a0 = ep(t, C["05"], 0.5)
        pos = linha(c, [("6", INK), (" + ", INK), ("2,5", INK), ("x", RED)], W / 2, 400, 130, a0)
        aa = ep(t, C["05.a"], 0.5)
        if aa > 0:
            xx = pos[3][0] + pos[3][1] / 2
            arrow(c, xx + 150, 280, xx + 30, 340, RED, aa, 5, 16)
            text(c, "VARIÁVEL", xx + 160, 270, 34, "black", RED, aa, align="left")
            text(c, "guarda um número que pode mudar", xx + 160, 306, 22, "bold", GRAY, aa, align="left")
        ab = ep(t, C["05.b"], 0.5)
        if ab > 0:
            x0, x1 = pos[0][0], pos[3][0] + pos[3][1]
            line(c, x0, 500, x1, 500, BLUE, ab, 5)
            line(c, x0, 485, x0, 500, BLUE, ab, 5); line(c, x1, 485, x1, 500, BLUE, ab, 5)
            text(c, "EXPRESSÃO ALGÉBRICA", W / 2, 550, 34, "black", BLUE, ab)
            text(c, "números + letras + operações", W / 2, 590, 24, "bold", GRAY, ab)
        acc = ep(t, C["05.c"], 0.5)
        if acc > 0:
            for (xs, ws) in (pos[0], (pos[2][0], pos[2][1] + pos[3][1])):
                c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(xs - 16, 320, ws + 32, 160), 20, 20),
                            paint(PURPLE, acc, stroke=5))
            pill(c, "TERMO: cada pedaço separado por + ou −   →   2 termos", W / 2, 700, PURPLE, size=30, a=acc,
                 anchor="center")
        return
    aa = ep(t, C["06.a"], 0.5)
    pos = linha(c, [("−5", INK), ("x²", INK)], W / 2, 420, 170, aa)
    ab = ep(t, C["06.b"], 0.5)
    if ab > 0:
        x0, w0 = pos[0]
        rrect(c, x0 - 14, 320, w0 + 28, 200, 22, BLUE, ab * 0.12)
        xl = x0 + w0 / 2 - 230
        line(c, x0 + w0 / 2, 525, xl, 575, BLUE, ab, 4)
        text(c, "COEFICIENTE", xl, 615, 36, "black", BLUE, ab)
        text(c, "o número da frente, COM o sinal", xl, 657, 24, "bold", GRAY, ab)
        ftext(c, "−5", xl, 720, 44, "black", BLUE, ab)
    acc = ep(t, C["06.c"], 0.5)
    if acc > 0:
        x1, w1 = pos[1]
        rrect(c, x1 - 14, 320, w1 + 28, 200, 22, GREEN, acc * 0.12)
        xr = x1 + w1 / 2 + 230
        line(c, x1 + w1 / 2, 525, xr, 575, GREEN, acc, 4)
        text(c, "PARTE LITERAL", xr, 615, 36, "black", GREEN, acc)
        text(c, "a parte com letra", xr, 657, 24, "bold", GRAY, acc)
        ftext(c, "x²", xr, 720, 44, "black", GREEN, acc)


# ======================================================================
# bloco b — tradução
# ======================================================================

def b_traducao(c, t, C, B):
    head_seq(c, t, C, [("07", "FRASE → EXPRESSÃO", "A ORDEM MANDA", BLUE), ("08", "MAIS TRADUÇÕES", "AS QUE MAIS CAEM", BLUE),
                       ("09", "ATALHO", "TESTE COM UM NÚMERO", GREEN)])
    card(c, *CARD_R)
    sid = which(t, C, ["07", "08", "09"])
    if sid == "07":
        rows = [("07.a", "o dobro de um número, aumentado de 3", ["dobra", "soma"], "2x + 3", BLUE),
                ("07.b", "o dobro da SOMA de um número com 3", ["soma (antes!)", "dobra"], "2(x+3)", PURPLE)]
        for k, (cue, frase, passos, ex, col) in enumerate(rows):
            a = ep(t, C[cue], 0.5)
            if a <= 0:
                continue
            y = 230 + k * 250
            rrect(c, 200, y, 1520, 210, 24, "#FFFFFF", a, shadow=True)
            text(c, f"“{frase}”", 240, y + 60, 36, "black", INK, a, align="left")
            for j, ps in enumerate(passos):
                aj = ep(t, C[cue] + 1.0 + 1.0 * j, 0.4)
                chip(c, f"{j + 1}º {ps}", 360 + j * 300, y + 140, AMBER if "antes" in ps else GRAY, aj, 28)
            ax = ep(t, C[cue] + 3.0, 0.4)
            expr(c, ex, 1420, y + 140, 80, ax, cores={i: col for i in range(5)})
            if k == 1 and ax > 0:
                pill(c, "o que vem antes vai entre PARÊNTESES", 1420, y + 60, AMBER, size=22, a=ax, anchor="center")
        acc = ep(t, C["07.c"], 0.5)
        if acc > 0:
            regra(c, "frases parecidas, contas diferentes", W / 2, 775, acc, 34, RED)
        return
    if sid == "08":
        rows = [("08.a", "o quadrado de um número, menos 1", "x^2 - 1", "≠ (x − 1)²"),
                ("08.b", "a metade de um número somada a seu triplo", "x/2 + 3x", "dois termos semelhantes"),
                ("08.c", "dois números consecutivos", "n  e  n+1", "pares: 2n e 2n + 2"),
                ("08.d", "R$ 6,00 fixos mais R$ 2,50 por km", "6 + 2,5x", "parte fixa + parte que varia")]
        a0 = ep(t, C["08"], 0.4)
        text(c, "FRASE", 220, 230, 22, "black", GRAY, a0, align="left", tracking=2)
        text(c, "EXPRESSÃO", 1040, 230, 22, "black", GRAY, a0, tracking=2)
        text(c, "ATENÇÃO", 1460, 230, 22, "black", GRAY, a0, tracking=2)
        for k, (cue, frase, ex, nota) in enumerate(rows):
            a = ep(t, C[cue], 0.5)
            if a <= 0:
                continue
            y = 260 + k * 140
            rrect(c, 200, y, 1520, 120, 18, "#F7F7F5" if k % 2 == 0 else "#FFFFFF", a)
            para(c, frase, 220, y + 52, 30, "black", INK, a, 640, 36)
            expr(c, ex.replace("  e  ", " e "), 1040, y + 60, 50, a, cores={i: BLUE for i in range(8)})
            ftext(c, nota, 1460, y + 72, 26, "black", AMBER if k == 0 else GRAY, a)
        return
    aa = ep(t, C["09.a"], 0.5)
    K.atalho(c, 260, 220, 1400, 120, "ATALHO", ["teste a tradução com um número (ex.: 5)"], aa, 36)
    if aa > 0:
        rrect(c, 260, 380, 660, 300, 22, "#FFFFFF", aa, shadow=True)
        text(c, "a FRASE, em palavras", 590, 430, 26, "black", GRAY, aa)
        text(c, "o dobro de 5 → 10", 590, 510, 36, "black", INK, ep(t, C["09.a"] + 1.4, 0.4))
        text(c, "aumentado de 3 → 13", 590, 580, 36, "black", INK, ep(t, C["09.a"] + 2.4, 0.4))
    ab = ep(t, C["09.b"], 0.5)
    if ab > 0:
        rrect(c, 1000, 380, 660, 300, 22, "#FFFFFF", ab, shadow=True)
        text(c, "a EXPRESSÃO", 1330, 430, 26, "black", GRAY, ab)
        expr(c, "2·5 + 3 = 13", 1330, 540, 60, ab, cores={4: GREEN})
        conferido(c, "deu o mesmo: tradução certa", 1080, 640, ep(t, C["09.b"] + 1.6, 0.4), True, 28)


# ======================================================================
# bloco c — valor numérico (a caixinha)
# ======================================================================

def b_valor(c, t, C, B):
    head_seq(c, t, C, [("10", "VALOR NUMÉRICO", "TROQUE A LETRA PELO NÚMERO", BLUE),
                       ("11", "UM TERMO DE CADA VEZ", "x = −2", PURPLE), ("12", "SEM PARÊNTESES?", "A ARMADILHA", AMBER)])
    card(c, *CARD_R)
    sid = which(t, C, ["10", "11", "12"])
    if sid == "10":
        aa = ep(t, C["10.a"], 0.5)
        if aa > 0:
            text(c, "VALOR NUMÉRICO = o resultado quando a letra vira número", W / 2, 260, 34, "black", BLUE, aa)
        ab = ep(t, C["10.b"], 0.5)
        caixinha(c, 560, 600, 150, ab, ep(t, C["10.b"] + 1.6, 0.6), "(−2)", ep(t, C["10.b"] + 2.4, 1.2))
        if ab > 0:
            pill(c, "SEMPRE de parênteses", 560, 760, RED, size=28, a=ep(t, C["10.b"] + 3.6, 0.4), anchor="center")
        acc = ep(t, C["10.c"], 0.5)
        if acc > 0:
            rrect(c, 900, 400, 800, 260, 24, "#FFFFFF", acc, shadow=True)
            expr(c, "3x^2 - 2x + 1", 1300, 490, 72, acc)
            linha(c, [("com  ", GRAY), ("x = −2", RED)], 1300, 590, 48, acc)
        return
    if sid == "11":
        a0 = ep(t, C["11"], 0.4)
        expr(c, "3·(-2)^2 - 2·(-2) + 1", W / 2, 270, 66, a0, cores={0: BLUE, 2: PURPLE, 4: AMBER})
        rows = [("11.a", "3·(-2)^2 = 3·4 = 12", BLUE, "(−2)·(−2) = +4"),
                ("11.b", "-2·(-2) = +4", PURPLE, "menos com menos: mais"),
                ("11.c", "+1", AMBER, "")]
        for k, (cue, ex, col, nota) in enumerate(rows):
            a, d = rise(t, C[cue])
            if a <= 0:
                continue
            y = 400 + k * 110 + d
            badge_num(c, k + 1, 300, y, a, 24, bg=col)
            expr(c, ex, 360, y, 56, a, align="left", cores={i: col for i in range(9)})
            if nota:
                ftext(c, nota, 1640, y + 12, 28, "bold", GRAY, a, align="right")
        ad = ep(t, C["11.d"], 0.5)
        if ad > 0:
            rrect(c, 560, 715, 800, 100, 24, mix("#FFFFFF", GREEN, 0.14), ad)
            linha(c, [("12 + 4 + 1 = ", INK), ("17", GREEN)], W / 2, 765, 60, ad)
        return
    aa = ep(t, C["12.a"], 0.5)
    if aa > 0:
        rrect(c, 260, 230, 1400, 230, 24, mix("#FFFFFF", RED, 0.06), aa)
        text(c, "SEM os parênteses", 300, 290, 28, "black", RED, aa, align="left")
        expr(c, "3·-2^2 = 3·(-4) = -12", W / 2, 380, 64, aa, cores={2: RED, 4: RED})
    ab = ep(t, C["12.b"], 0.5)
    if ab > 0:
        pz = linha(c, [("−12 + 4 + 1 = ", INK), ("−7", RED)], 700, 540, 60, ab)
        strike(c, pz[1][0] - 8, 540, pz[1][0] + pz[1][1] + 8, 540, ab, RED, 1)
        linha(c, [("o certo era ", GRAY), ("17", GREEN)], 1300, 540, 44, ab)
    acc = ep(t, C["12.c"], 0.5)
    K.atalho(c, 360, 610, 1200, 170, "ATALHO DE SEGURANÇA", ["negativo? escreva os PARÊNTESES primeiro, depois o número"], acc,
             32)


# ======================================================================
# bloco d — termos semelhantes (as frutas)
# ======================================================================

def b_semelhantes(c, t, C, B):
    head_seq(c, t, C, [("13", "TERMOS SEMELHANTES", "FRUTAS IGUAIS", BLUE), ("14", "JUNTANDO AS FRUTAS", "3x² + 2x − x² + 5x", PURPLE)])
    card(c, *CARD_R)
    sid = which(t, C, ["13", "14"])
    if sid == "13":
        aa = ep(t, C["13.a"], 0.5)
        if aa > 0:
            for k in range(3):
                maca(c, 280 + k * 90, 330, 40, aa)
            fmid(c, "+", 590, 330, 60, "black", INK, aa)
            for k in range(2):
                maca(c, 680 + k * 90, 330, 40, aa)
            fmid(c, "=", 900, 330, 60, "black", INK, aa)
            a2 = ep(t, C["13.a"] + 1.6, 0.4)
            for k in range(5):
                maca(c, 1000 + k * 90, 330, 40, a2)
            text(c, "5 maçãs", 1180, 420, 32, "black", GREEN, a2)
            a3 = ep(t, C["13.a"] + 3.0, 0.4)
            if a3 > 0:
                maca(c, 440, 520, 40, a3)
                fmid(c, "+", 540, 520, 60, "black", INK, a3)
                banana(c, 650, 520, 50, a3)
                fmid(c, "≠", 780, 520, 60, "black", RED, a3)
                text(c, "1 fruta só?  não!", 1000, 535, 36, "black", RED, a3)
        ab = ep(t, C["13.b"], 0.5)
        if ab > 0:
            rrect(c, 260, 620, 1400, 170, 24, mix("#FFFFFF", BLUE, 0.08), ab)
            text(c, "TERMOS SEMELHANTES = mesma PARTE LITERAL", W / 2, 680, 38, "black", BLUE, ab)
            maca(c, 520, 742, 28, ab); ftext(c, "= x²", 560, 756, 30, "black", INK, ab, align="left")
            banana(c, 860, 742, 34, ab); ftext(c, "= x", 910, 756, 30, "black", INK, ab, align="left")
            text(c, "só eles se juntam", 1360, 756, 30, "black", GREEN, ab)
        return
    a0 = ep(t, C["14.a"], 0.5)
    toks = ["3x²", " + 2x", " − x²", " + 5x"]
    cols = [MACA, "#C98A00", MACA, "#C98A00"]
    pos = linha(c, list(zip(toks, cols)), W / 2, 280, 76, a0)
    if a0 > 0:
        for k, (x_, w_) in enumerate(pos):
            if k % 2 == 0:
                maca(c, x_ + w_ / 2, 360, 24, a0)
            else:
                banana(c, x_ + w_ / 2 + 20, 355, 28, a0)
    ab = ep(t, C["14.b"], 0.5)
    if ab > 0:
        rrect(c, 260, 420, 680, 150, 22, mix("#FFFFFF", MACA, 0.10), ab)
        maca(c, 320, 495, 30, ab)
        linha(c, [("3x² − x² = ", INK), ("2x²", MACA)], 640, 495, 46, ab)
        a2 = ep(t, C["14.b"] + 2.4, 0.4)
        rrect(c, 980, 420, 680, 150, 22, mix("#FFFFFF", BANANA, 0.22), a2)
        banana(c, 1050, 490, 34, a2)
        linha(c, [("2x + 5x = ", INK), ("7x", "#C98A00")], 1360, 495, 46, a2)
    acc = ep(t, C["14.c"], 0.5)
    if acc > 0:
        linha(c, [("= ", INK), ("2x² + 7x", GREEN)], W / 2, 650, 80, acc)
    ad = ep(t, C["14.d"], 0.5)
    if ad > 0:
        pos2 = linha(c, [("≠ 9x³", RED)], 1500, 760, 56, ad)
        strike(c, pos2[0][0] - 8, 760, pos2[0][0] + pos2[0][1] + 8, 760, ad, RED, 1)
        text(c, "frutas diferentes não se juntam", 760, 775, 32, "black", RED, ad)


# ======================================================================
# bloco e — o espelho
# ======================================================================

def b_espelho(c, t, C, B):
    head(c, t, B["start"], "O MENOS ANTES DO PARÊNTESE", "UM ESPELHO", PURPLE)
    card(c, *CARD_R)
    aa = ep(t, C["15.a"], 0.5)
    pos = linha(c, [("5 ", INK), ("−", RED), (" (", INK), ("x", BLUE), (" − 3", BLUE), (")", INK)], W / 2, 320, 110, aa)
    ab = ep(t, C["15.b"], 0.5)
    if ab > 0:
        # o espelho passa sobre o parêntese
        u = ep(t, C["15.b"] + 0.4, 1.4)
        x0 = pos[2][0]; x1 = pos[5][0] + pos[5][1]
        xm = lerp(x0, x1, u)
        if 0 < u < 1:
            rrect(c, xm - 10, 230, 20, 180, 10, mix("#FFFFFF", PURPLE, 0.4), ab)
            c.drawCircle(xm, 320, 120 * (1 - abs(0.5 - u) * 2) + 10, paint("#FFFFFF", ab * 0.25))
        a2 = ep(t, C["15.b"] + 1.6, 0.4)
        pos2 = linha(c, [("5", INK), (" − x", PURPLE), (" + 3", PURPLE)], W / 2, 520, 100, a2)
        if a2 > 0:
            for k in (1, 2):
                x_, w_ = pos2[k]
                c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x_ + 10, 450, w_ - 10, 140), 18, 18),
                            paint(PURPLE, a2, stroke=4))
            text(c, "x  →  −x", pos2[1][0] + pos2[1][1] / 2, 640, 28, "black", PURPLE, a2)
            text(c, "−3  →  +3", pos2[2][0] + pos2[2][1] / 2, 640, 28, "black", PURPLE, a2)
    acc = ep(t, C["15.c"], 0.5)
    if acc > 0:
        linha(c, [("= ", INK), ("8 − x", GREEN)], W / 2, 740, 80, acc)
        pill(c, "vira TODOS os sinais", 1500, 740, PURPLE, size=28, a=acc, anchor="center")


# ======================================================================
# bloco f — distributiva (o aperto de mão)
# ======================================================================

DIST_A, DIST_B = ["2x", "+", "3"], ["x", "−", "4"]


def b_distributiva(c, t, C, B):
    head_seq(c, t, C, [("16", "MULTIPLICAR POLINÔMIOS", "DISTRIBUTIVA", PURPLE), ("17", "OS 4 APERTOS DE MÃO", "(2x + 3)(x − 4)", PURPLE),
                       ("18", "ATALHO", "TESTE COM x = 1", GREEN)])
    card(c, *CARD_R)
    sid = which(t, C, ["16", "17", "18"])
    if sid == "16":
        aa = ep(t, C["16.a"], 0.5)
        if aa > 0:
            rrect(c, 260, 220, 1400, 110, 22, mix("#FFFFFF", BLUE, 0.08), aa)
            linha(c, [("POLINÔMIO", BLUE), (" = soma de termos:   2x + 3   ·   2x² − 5x − 12", INK)], W / 2, 275, 36, aa)
        ab = ep(t, C["16.b"], 0.5)
        if ab > 0:
            regra(c, "DISTRIBUTIVA: cada termo de um × cada termo do outro", W / 2, 400, ab, 34)
        acc = ep(t, C["16.c"], 0.5)
        if acc > 0:
            xs = parenteses(c, DIST_A, DIST_B, W / 2, 600, 96, acc)
            al = [ep(t, C["16.c"] + 1.4 + 0.6 * k, 0.6) for k in range(4)]
            apertos(c, xs, 600, 96, [acc * v for v in al])
            pill(c, "2 × 2 = 4 apertos de mão", 1560, 600, GREEN, size=28, a=al[3], anchor="center")
        return
    if sid == "17":
        a0 = ep(t, C["17"], 0.4)
        xs = parenteses(c, DIST_A, DIST_B, W / 2, 380, 96, a0)
        al = [ep(t, C[f"17.{q}"], 0.6) for q in "abcd"]
        apertos(c, xs, 380, 96, [a0 * v for v in al])
        produtos(c, ["2x²", "−8x", "+3x", "−12"], W / 2, 600, 46, al)
        ae = ep(t, C["17.e"], 0.5)
        if ae > 0:
            # as frutas iguais (−8x e +3x) se juntam
            rrect(c, 560, 680, 800, 120, 24, mix("#FFFFFF", GREEN, 0.14), ae)
            linha(c, [("2x²", INK), (" − 5x", AMBER), (" − 12", INK)], W / 2, 740, 70, ae)
            pill(c, "−8x + 3x = −5x", 1560, 600, AMBER, size=26, a=ae, anchor="center")
        return
    aa = ep(t, C["18.a"], 0.5)
    K.atalho(c, 260, 210, 1400, 120, "ATALHO", ["teste com x = 1 antes e depois"], aa, 36)
    if aa > 0:
        rrect(c, 260, 370, 660, 300, 22, "#FFFFFF", aa, shadow=True)
        text(c, "NO COMEÇO", 590, 420, 26, "black", GRAY, aa)
        expr(c, "(2+3)(1-4)", 590, 510, 56, ep(t, C["18.a"] + 1.4, 0.4))
        linha(c, [("5 · (−3) = ", INK), ("−15", PURPLE)], 590, 600, 48, ep(t, C["18.a"] + 3.0, 0.4))
    ab = ep(t, C["18.b"], 0.5)
    if ab > 0:
        rrect(c, 1000, 370, 660, 300, 22, "#FFFFFF", ab, shadow=True)
        text(c, "NO RESULTADO", 1330, 420, 26, "black", GRAY, ab)
        linha(c, [("2 − 5 − 12 = ", INK), ("−15", PURPLE)], 1330, 540, 48, ab)
        conferido(c, "bateu", 1240, 630, ep(t, C["18.b"] + 1.6, 0.4), True, 30)
    acc = ep(t, C["18.c"], 0.5)
    if acc > 0:
        pill(c, "não bateu?  sumiu um aperto ou virou um sinal", W / 2, 750, AMBER, size=28, a=acc, anchor="center")


# ======================================================================
# nós fazemos
# ======================================================================

EX_A, EX_B = ["x", "+", "2"], ["3x", "−", "1"]


def b_exercicio(c, t, C, B):
    head_seq(c, t, C, [("19", "SUA VEZ", "PAUSE E TENTE", GREEN), ("20", "VAMOS JUNTOS", "4 APERTOS DE MÃO", GREEN)])
    card(c, *CARD_R)
    aa = ep(t, C["19.a"], 0.5)
    text(c, "DESENVOLVA", W / 2, 250, 28, "black", GRAY, aa * (1 - ep(t, C["20"], 0.3)), tracking=2)
    xs = parenteses(c, EX_A, EX_B, W / 2, 360, 96, aa)
    pause_timer(c, t, C["19.end"] - 1.9, W / 2, 580)
    if t < C["20"]:
        return
    al = [ep(t, C["20.a"], 0.6), ep(t, C["20.a"] + 2.2, 0.6), ep(t, C["20.b"], 0.6), ep(t, C["20.b"] + 2.0, 0.6)]
    apertos(c, xs, 360, 96, al)
    produtos(c, ["3x²", "−x", "+6x", "−2"], W / 2, 590, 46, al)
    acc = ep(t, C["20.c"], 0.5)
    if acc > 0:
        rrect(c, 560, 670, 800, 110, 24, mix("#FFFFFF", GREEN, 0.14), acc)
        linha(c, [("3x²", INK), (" + 5x", AMBER), (" − 2", INK)], W / 2, 725, 66, acc)
    ad = ep(t, C["20.d"], 0.5)
    if ad > 0:
        conferido(c, "x = 1: 3 · 2 = 6  e  3 + 5 − 2 = 6", 1380, 800, ad, True, 26)


# ======================================================================
# recap, erros
# ======================================================================

FRASES = ["Negativo entra na conta sempre de parênteses.",
          "Só se somam termos semelhantes.",
          "Na distributiva, todos cumprimentam todos."]


def b_recap(c, t, C, B):
    sid = which(t, C, ["21", "33"])
    frame(c, t, B["start"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "21" else "PARA FECHAR", PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 300 + k * 180 + d
        badge_num(c, k + 1, 260, y - 16, a, 36, bg=PURPLE)
        para(c, s, 320, y, 54, "black", INK, a, 1360, 64)


ERROS = [("−2² = +4", "menos com menos dá mais",
          "sem parênteses, o quadrado pega só o 2: −2² = −4  ·  (−2)² = +4"),
         ("5 − (x − 3) = 5 − x − 3", "o menos parece grudado só no primeiro termo",
          "o espelho vira TODOS os sinais: 5 − x + 3 = 8 − x"),
         ("2x + 3x² = 5x³", "2 + 3 = 5, e o expoente parece somar",
          "não são semelhantes (maçã com banana): fica 2x + 3x²"),
         ("(3x)² = 3x²", "o quadrado está colado no x",
          "o expoente está fora do parêntese: eleva o 3 também → 9x²"),
         ("“o dobro da soma” = 2x + 3", "as palavras aparecem nessa ordem",
          "a soma acontece primeiro: 2(x + 3)")]


def b_erros(c, t, C, B):
    K.erro_cards(c, t, C, ["22", "23", "24", "25", "26"], ERROS)


# ======================================================================
# questões do material
# ======================================================================

def _enunciado(c, linhas, a, y0=250, size=30, w=720):
    y = y0
    for s, col in linhas:
        for ln in K.wrap(s, "black", size, w):
            text(c, ln, 190, y, size, "black", col, a, align="left")
            y += size + 12
        y += 8
    return y


def _painel(c, a, y0=230):
    rrect(c, 170, y0, 760, 830 - y0, 18, "#FFFFFF", a, shadow=True)


ALTS1 = [("A", "2,5x + 13,5", "só a 2ª corrida", RED), ("B", "5x + 13,5", "1 tarifa fixa só", RED),
         ("C", "5x + 19,5", "", GREEN), ("D", "5x + 15", "esqueceu 3 km × 2,50", RED),
         ("E", "17x + 25,5", "R$ 6 por km também", RED)]


def b_q1(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 1 · EU FAÇO", "TRADUZIR O ENUNCIADO", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["27.a"], 0.4) * (1 - ep(t, C["28"], 0.4))
    yend = _enunciado(c, [("Um aplicativo de transporte cobra, por corrida, uma tarifa fixa de R$ 6,00 mais R$ 2,50 por "
                           "quilômetro rodado. Em um dia, uma pessoa fez duas corridas: a primeira de x quilômetros e a "
                           "segunda 3 quilômetros mais longa que a primeira. A expressão que dá o valor total pago pelas "
                           "duas corridas, em reais, é", INK)], a0, 230, 27)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0, align="left")
    cues_in = {L: C[f"27.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"29.x{L.lower()}"] for L in "ABDE"}
    K.alternativas(c, t, C, ALTS1, 1000, 250, 680, 40, C["28.ok"], "C", cues_in, cues_x, gap=30)
    pause_timer(c, t, C["27.end"] - 1.9, 540, yend + 90)
    if t >= C["28"]:
        ap = ep(t, C["28"], 0.4)
        _painel(c, ap)
        text(c, "UMA INFORMAÇÃO DE CADA VEZ", 550, 280, 24, "black", GRAY, ap, tracking=2)
        rows = [("28.a", [("tarifas: 2 · 6 = ", INK), ("12", BLUE)]),
                ("28.b", [("km: x + (x + 3) = ", INK), ("2x + 3", BLUE)]),
                ("28.c", [("2,5 · (2x + 3) = ", INK), ("5x + 7,5", BLUE)]),
                ("28.d", [("12 + 5x + 7,5 = ", INK), ("5x + 19,5", GREEN)])]
        for k, (cue, partes) in enumerate(rows):
            linha(c, partes, 550, 360 + k * 85, 38, ep(t, C[cue], 0.4))
        ae = ep(t, C["28.e"], 0.4)
        if ae > 0:
            rrect(c, 200, 700, 700, 110, 18, mix("#FFFFFF", GREEN, 0.10), ae)
            text(c, "teste x = 2: corridas de 11 + 18,50", 550, 742, 26, "black", INK2, ae)
            conferido(c, "29,50 dos dois jeitos", 380, 790, ae, True, 26)


ALTS6 = [("A", "=600 - 4x^2", "inclui as abas", RED), ("B", "=600 - 100x", "esqueceu +4x²", RED),
         ("C", "=x^2 - 50x + 600", "tirou x uma vez só", RED), ("D", "=600 - 100x - 4x^2", "sinal errado", RED),
         ("E", "=4x^2 - 100x + 600", "", GREEN)]


def b_q6(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 6 · VOCÊ FAZ", "A ÁREA DO FUNDO DA CAIXA", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["30.a"], 0.4) * (1 - ep(t, C["31"], 0.4))
    yend = _enunciado(c, [("De uma folha retangular de papelão de 30 cm por 20 cm, recortam-se quatro quadrados de lado x "
                           "centímetros, um em cada canto. Dobrando as abas, obtém-se uma caixa sem tampa. A área do fundo "
                           "dessa caixa, em cm², é", INK)], a0, 230, 27)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0, align="left")
    folha_caixa(c, 330, yend + 50, 14, a0)
    cues_in = {L: C[f"30.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"32.x{L.lower()}"] for L in "ABCD"}
    K.alternativas(c, t, C, ALTS6, 1000, 240, 680, 36, C["31.ok"], "E", cues_in, cues_x, gap=26)
    ap_ = ep(t, C["30.p"], 0.4) * (1 - ep(t, C["31"], 0.4))
    if ap_ > 0:
        pill(c, "área do retângulo = comprimento × largura", 1340, 800, PURPLE, size=22, a=ap_, anchor="center")
    pause_timer(c, t, C["30.end"] - 1.9, 860, yend + 200)
    if t >= C["31"]:
        ap = ep(t, C["31"], 0.4)
        _painel(c, ap)
        folha_caixa(c, 340, 290, 14, ap, True, ep(t, C["31.a"], 0.5))
        aa = ep(t, C["31.a"], 0.5)
        if aa > 0:
            text(c, "30 − 2x", 550, 600, 30, "black", GREEN, aa)
            text(c, "20 − 2x", 830, 470, 26, "black", GREEN, aa, align="left")
        linha(c, [("(30 − 2x)(20 − 2x) = 600 − 60x − 40x", INK)], 550, 650, 28, ep(t, C["31.b"], 0.4))
        ac = ep(t, C["31.c"], 0.4)
        if ac > 0:
            linha(c, [("(−2x)·(−2x) = ", INK), ("+4x²", GREEN)], 550, 705, 34, ac)
        linha(c, [("= ", INK), ("4x² − 100x + 600", GREEN)], 550, 760, 36, ep(t, C["31.d"], 0.4))
        conferido(c, "x = 1: 28 · 18 = 504 = 4 − 100 + 600", 200, 808, ep(t, C["31.e"], 0.4), True, 22)


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "O ERRO MAIS FAMOSO", PURPLE)
    aa = ep(t, C["34.a"], 0.5)
    u = 56
    x0, y0 = 300, 250
    if aa > 0:
        for i in range(7):
            for j in range(7):
                if i < 3 and j < 3:
                    col = mix("#FFFFFF", BLUE, 0.35)
                elif i >= 3 and j >= 3:
                    col = mix("#FFFFFF", GREEN, 0.35)
                else:
                    col = "#FFFFFF"
                c.drawRect(skia.Rect.MakeXYWH(x0 + i * u, y0 + j * u, u, u), paint(col, aa))
                c.drawRect(skia.Rect.MakeXYWH(x0 + i * u, y0 + j * u, u, u), paint(LIGHT, aa, stroke=2))
        c.drawRect(skia.Rect.MakeXYWH(x0, y0, 7 * u, 7 * u), paint(INK, aa, stroke=4))
        text(c, "3", x0 + 1.5 * u, y0 - 16, 30, "black", BLUE, aa)
        text(c, "4", x0 + 5 * u, y0 - 16, 30, "black", GREEN, aa)
        text(c, "lado 3 + 4: quantos quadradinhos?", 1220, 330, 40, "black", INK, aa)
    ab = ep(t, C["34.b"], 0.5)
    if ab > 0:
        linha(c, [("3² + 4² = ", INK), ("25", AMBER), ("?", AMBER)], 1220, 450, 60, ab)
        g = ep(t, C["34.b"] + 2.4, 0.5)
        if g > 0:
            for (rx, ry, rw, rh) in ((3, 0, 4, 3), (0, 3, 3, 4)):
                c.drawRect(skia.Rect.MakeXYWH(x0 + rx * u, y0 + ry * u, rw * u, rh * u), paint(mix("#FFFFFF", RED, 0.45), g))
                c.drawRect(skia.Rect.MakeXYWH(x0 + rx * u, y0 + ry * u, rw * u, rh * u), paint(RED, g, stroke=4))
            fmid(c, "12", x0 + 5 * u, y0 + 1.5 * u, 40, "black", RED, g)
            fmid(c, "12", x0 + 1.5 * u, y0 + 5 * u, 40, "black", RED, g)
            linha(c, [("faltaram ", RED), ("24", RED), ("  (7² = 49)", GRAY)], 1220, 560, 52, g)
    pill(c, "ep. 2 · produtos notáveis e o sonho do calouro", W / 2, 790, PURPLE, size=30, a=ep(t, C["34.c"], 0.5),
         anchor="center")


def b_cta(c, t, C, B):
    cta(c, t, C["35.like"], C["35.sub"], C["35.bell"], C["35.com"], C["35.bye"],
        "Qual desses 5 erros você já cometeu?", canal="no Estudativo", anki=C["35.anki"])


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, concreto=b_concreto, vocab=b_vocab, traducao=b_traducao,
              valor=b_valor, semelhantes=b_semelhantes, espelho=b_espelho, distributiva=b_distributiva,
              exercicio=b_exercicio, recap=b_recap, erros=b_erros, q1=b_q1, q6=b_q6, ponte=b_ponte, cta=b_cta)
