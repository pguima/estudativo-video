"""Visual — Polinômios e Equações Polinomiais, Episódio 1: polinômio, grau, valor numérico e modelagem (tema claro).
Peças comuns da série em ../../comum.py (reexporta o 019/comum.py: expr, alternativas, erro_cards, selo, regra, pause_timer...).
Peças deste episódio: folha() (o papelão com os 4 quadrados de lado x que somem dos cantos), caixa_iso() (a caixa sem
tampa em perspectiva, com as três medidas nas arestas), predio() (os andares x³, x², x, x⁰ com o mais alto aceso),
raiox() (a lente que passa sobre P(x) e deixa só os coeficientes), nota() (as duas notas fiscais da identidade).
Cores com função: azul = definição · roxo = regra/fórmula · âmbar = armadilha · verde = atalho · vermelho = erro.
"""
import importlib.util
from pathlib import Path
import skia
import motor
motor.set_theme("claro")
from motor import *  # noqa
from aula import *  # noqa

_p = Path(__file__).resolve().parents[2] / "comum.py"
_s = importlib.util.spec_from_file_location("comum050", _p)
K = importlib.util.module_from_spec(_s); _s.loader.exec_module(K)
K.usar_tempos(Path(__file__).resolve().parents[1] / "audio" / "tempos.json")
motor.set_theme("claro")
frame, head_seq, which, para, regra, selo, pause_timer = (K.frame, K.head_seq, K.which, K.para, K.regra, K.selo,
                                                          K.pause_timer)
ftext, ftext_w, expr, math_w = K.ftext, K.ftext_w, K.expr, K.math_w

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_polinomios_ep1_grau_valor_modelagem.mp4"
CARD_R = K.CARD_R
PAPELAO = "#D9B98C"
PAPELAO_D = "#B8925E"
PAPELAO_E = "#C9A473"


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


def poly(c, pts, col, a, stroke=None):
    if a <= 0:
        return
    p = skia.Path()
    p.moveTo(*pts[0])
    for q in pts[1:]:
        p.lineTo(*q)
    p.close()
    c.drawPath(p, paint(col, a))
    if stroke:
        c.drawPath(p, paint(stroke[0], a, stroke=stroke[1]))


def cartao(c, x, y, w, h, a, col=None, fill=False):
    if a <= 0:
        return
    rrect(c, x, y, w, h, 24, mix("#FFFFFF", col, 0.10) if (fill and col) else "#FFFFFF", a, shadow=True)


def defin(c, termo, s, x, y, w, a, col=None, size=30):
    """faixa de definição: TERMO: frase"""
    if a <= 0:
        return
    col = col or BLUE
    rrect(c, x, y, w, 76, 18, mix("#FFFFFF", col, 0.12), a)
    linha(c, [(termo, col), (": " + s, INK)], x + 28, y + 38, size, a, align="left")


def folha(c, cx, cy, w, h, xr, a, corte=0.0, rot=True, med=None):
    """papelão visto de cima; corte 0 → 1 apaga os 4 quadrados de lado xr dos cantos (tracejados em vermelho);
    med = (rótulo do comprimento, rótulo da largura)"""
    if a <= 0:
        return
    x0, y0 = cx - w / 2, cy - h / 2
    rrect(c, x0, y0, w, h, 6, PAPELAO, a, shadow=True)
    for (qx, qy) in ((x0, y0), (x0 + w - xr, y0), (x0, y0 + h - xr), (x0 + w - xr, y0 + h - xr)):
        if corte > 0:
            rrect(c, qx, qy, xr, xr, 0, BG, a * corte)
        rrect(c, qx + 2, qy + 2, xr - 4, xr - 4, 0, RED, a * (0.25 + 0.35 * (1 - corte)), )
        c.drawRect(skia.Rect.MakeXYWH(qx + 2, qy + 2, xr - 4, xr - 4), paint(RED, a, stroke=3))
    if rot:
        text(c, "x", x0 + xr / 2, y0 - 14, 30, "black", RED, a)
        text(c, "x", x0 - 22, y0 + xr / 2 + 10, 30, "black", RED, a)
    if corte > 0.5:
        for xx in (x0 + xr, x0 + w - xr):
            line(c, xx, y0 + xr, xx, y0 + h - xr, PAPELAO_D, a * corte, 3)
        for yy in (y0 + xr, y0 + h - xr):
            line(c, x0 + xr, yy, x0 + w - xr, yy, PAPELAO_D, a * corte, 3)
    if med:
        text(c, med[0], cx, y0 + h + 46, 32, "black", INK, a)
        text(c, med[1], x0 + w + 18, cy + 12, 32, "black", INK, a, align="left")


def caixa_iso(c, cx, cy, L, P, H, a, rots=None, alfa_rot=1.0):
    """caixa sem tampa em perspectiva: L = comprimento (frente), P = profundidade, H = altura"""
    if a <= 0:
        return
    dx, dy = P * 0.62, -P * 0.42
    x0, y0 = cx - (L + dx) / 2, cy + (H - dy) / 2      # canto frontal inferior esquerdo
    A = (x0, y0); B = (x0 + L, y0); Cc = (x0 + L + dx, y0 + dy); D = (x0 + dx, y0 + dy)
    At, Bt, Ct, Dt = [(px, py - H) for px, py in (A, B, Cc, D)]
    poly(c, [D, Cc, Ct, Dt], PAPELAO_D, a)                       # fundo de trás (interior)
    poly(c, [A, D, Dt, At], PAPELAO_D, a)                        # lado esquerdo (interior)
    poly(c, [A, B, Cc, D], mix(PAPELAO_D, "#000000", 0.08), a)   # fundo
    poly(c, [B, Cc, Ct, Bt], PAPELAO_E, a, (PAPELAO_D, 3))       # lado direito
    poly(c, [A, B, Bt, At], PAPELAO, a, (PAPELAO_D, 3))          # frente
    if rots and alfa_rot > 0:
        r1, r2, r3 = rots
        ar = a * alfa_rot
        pill(c, r1, (A[0] + B[0]) / 2, A[1] + 44, PURPLE, size=28, a=ar, anchor="center", bounds=(0, 1920))
        pill(c, r2, (B[0] + Cc[0]) / 2 + 30, (B[1] + Cc[1]) / 2 + 26, PURPLE, size=28, a=ar, anchor="left",
             bounds=(0, 1920))
        pill(c, r3, A[0] - 26, (A[1] + At[1]) / 2, RED, size=28, a=ar, anchor="right", bounds=(0, 1920))


def predio(c, x, ybase, andares, a, alto=None, w=300, h=86, col=None):
    """prédio de baixo para cima: andares = [(rótulo, coeficiente)], o índice `alto` fica aceso"""
    if a <= 0:
        return
    col = col or PURPLE
    n = len(andares)
    rrect(c, x - 20, ybase - 4, w + 40, 12, 6, INK2, a)
    for k, (rot, coef) in enumerate(andares):
        y = ybase - (k + 1) * h
        on = alto == k
        vazio = coef in ("0", "")
        rrect(c, x, y + 4, w, h - 8, 14, mix("#FFFFFF", col, 0.30) if on else ("#F3F1EA" if vazio else "#FFFFFF"),
              a, shadow=not vazio)
        if not vazio:
            c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y + 4, w, h - 8), 14, 14),
                        paint(col if on else GRAY, a, stroke=4 if on else 2))
        expr(c, rot, x + 80, y + h / 2, 40, a * (0.4 if vazio else 1), cores={0: col if on else INK2})
        ftext(c, coef if coef else "—", x + w - 40, y + h / 2 + 16, 40, "black", GRAY if vazio else (col if on else INK),
              a, align="right")
    if alto is not None and alto < n:
        y = ybase - (alto + 1) * h
        pill(c, "o mais alto", x + w + 24, y + h / 2, col, size=24, a=a, anchor="left", bounds=(0, 1920))


def raiox(c, cx, cy, termos, a, prog, size=56, col=None, sinais=None):
    """P(x) em tokens; a lente (prog 0 → 1) varre da esquerda para a direita e, por onde passou, cada termo vira só o
    coeficiente (em verde). termos = [(termo, coeficiente)] separados por sinais = [' ', '−', '+', ...]"""
    if a <= 0:
        return
    col = col or GREEN
    toks = []
    for k, (tm, cf) in enumerate(termos):
        if k:
            toks.append(((sinais or [])[k - 1], (sinais or [])[k - 1]))
        toks.append((tm, cf))
    ws = [max(math_w(tm, size), math_w(cf, size)) for tm, cf in toks]
    gap = size * 0.32
    total = sum(ws) + gap * (len(ws) - 1)
    x = cx - total / 2
    lx = cx - total / 2 - 60 + (total + 120) * prog
    for (tm, cf), w_ in zip(toks, ws):
        mid = x + w_ / 2
        passou = prog > 0 and lx > mid
        expr(c, cf if passou else tm, mid, cy, size, a, cores={0: col} if (passou and tm != cf) else None)
        x += w_ + gap
    if 0 < prog < 1:
        c.drawCircle(lx, cy, size * 1.05, paint(mix("#FFFFFF", BLUE, 0.20), a * 0.5))
        c.drawCircle(lx, cy, size * 1.05, paint(BLUE, a, stroke=6))
        line(c, lx + size * 0.75, cy + size * 0.75, lx + size * 1.5, cy + size * 1.5, BLUE, a, 12)
        pill(c, "x = 1", lx, cy - size * 1.5, BLUE, size=24, a=a, anchor="center", bounds=(0, 1920))


def nota(c, x, y, w, titulo, itens, a, acesos=(), col=None):
    """nota fiscal: itens = [(rótulo, valor)]; acesos = índices destacados"""
    if a <= 0:
        return
    col = col or PURPLE
    h = 110 + 74 * len(itens)
    rrect(c, x, y, w, h, 12, "#FFFFFF", a, shadow=True)
    for k in range(0, w, 28):
        c.drawCircle(x + k + 14, y + h, 8, paint(BG, a))
    text(c, titulo, x + w / 2, y + 56, 30, "black", INK2, a, tracking=2)
    line(c, x + 24, y + 80, x + w - 24, y + 80, GRAY, a, 2)
    for k, (rot, val) in enumerate(itens):
        yy = y + 120 + 74 * k
        if k in acesos:
            rrect(c, x + 14, yy - 34, w - 28, 66, 12, mix("#FFFFFF", col, 0.22), a)
        expr(c, rot, x + 90, yy, 34, a, cores={0: INK2})
        expr(c, val, x + w - 40, yy, 40, a, align="right", cores={0: col if k in acesos else INK})


# dados
P_RX = [("2x^3", "2"), ("5x^2", "5"), ("x", "1"), ("7", "7")]
S_RX = ["−", "+", "+"]


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "POLINÔMIOS · EPISÓDIO 1", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["01.a"], 0.5)
    if aa > 0:
        expr(c, "(x^2−3x+3)^{20}", 960, 300, 110, aa, cores={0: PURPLE})
        # o começo e o fim do desenvolvimento DE VERDADE (coeficientes conferidos em ../trabalho/conferir_contas.py)
        ab0 = ep(t, C["01.a"] + 2.5, 1.2)
        linhas_ = ["x^{40} − 60x^{39} + 1770x^{38} − 34200x^{37} + ...",
                   "... + 685734265530x^2 − 69735688020x + 3486784401"]
        for i, ln in enumerate(linhas_):
            ai = ep(t, C["01.a"] + 2.5 + 0.6 * i, 0.6)
            expr(c, ln, 960, 490 + i * 80, 40, ai * 0.7)
        pill(c, "dezenas de termos", 960, 405, AMBER, size=28, a=ab0, anchor="center")
    ab = ep(t, C["01.b"], 0.5)
    if ab > 0:
        rrect(c, 520, 690, 880, 100, 22, mix("#FFFFFF", BLUE, 0.12), ab)
        text_mid(c, "soma de TODOS os coeficientes = ?", 960, 740, 44, "black", INK, ab)
    acc = ep(t, C["01.c"], 0.5)
    if acc > 0:
        selo(c, 1560, 700, acc, "UMA LINHA: 1", GREEN, -6, 46)


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "POLINÔMIOS · EP. 1", "AO FINAL DESTA AULA", GREEN)
    a0 = ep(t, C["02"], 0.4)
    if a0 > 0:
        pill(c, "1º episódio da série de POLINÔMIOS", W / 2, 240, BLUE, size=28, a=a0, anchor="center")
    itens = [("02.a", "RECONHECER", "um polinômio", BLUE), ("02.b", "O GRAU", "o andar mais alto", PURPLE),
             ("02.c", "DE GRAÇA", "P(0) e P(1)", GREEN), ("02.d", "A CAIXA", "o polinômio do volume", AMBER)]
    for k, (cue, tit, sb, col) in enumerate(itens):
        ak = ep(t, C[cue], 0.5)
        if ak <= 0:
            continue
        x = 330 + k * 420
        rrect(c, x - 190, 340, 380, 320, 26, "#FFFFFF", ak, shadow=True)
        rrect(c, x - 190, 340, 380, 70, 26, col, ak * 0.16)
        badge_num(c, k + 1, x, 470, ak, 34, bg=col)
        text(c, tit, x, 570, 42, "black", col, ak)
        text(c, sb, x, 625, 28, "bold", INK2, ak)


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "TRÊS LEMBRETES", "EM 30 SEGUNDOS", GREEN)
    a, d = rise(t, C["03.a"])
    if a > 0:
        y = 300 + d
        cartao(c, 260, y - 75, 1400, 150, a)
        pill(c, "Expressões algébricas", 300, y - 75, BLUE, size=22, a=a)
        expr(c, "3x^2 + 5x^2 = 8x^2", 640, y, 50, a)
        expr(c, "(a+b)(c+d) = ac + ad + bc + bd", 1260, y, 40, a)
    a, d = rise(t, C["03.b"])
    if a > 0:
        y = 500 + d
        cartao(c, 260, y - 75, 1400, 150, a)
        pill(c, "parênteses no negativo", 300, y - 75, AMBER, size=22, a=a)
        expr(c, "(−2)^2 = 4", 960, y, 60, a, cores={2: GREEN})
    a, d = rise(t, C["03.c"])
    if a > 0:
        y = 700 + d
        cartao(c, 260, y - 75, 1400, 150, a)
        pill(c, "Potenciação", 300, y - 75, GREEN, size=22, a=a)
        expr(c, "1^{20} = 1^{100} = 1", 960, y, 60, a)


# ======================================================================
# concreto — a caixa de papelão
# ======================================================================

def b_caixa(c, t, C, B):
    head(c, t, B["start"], "A CAIXA DE PAPELÃO", "O VOLUME DEPENDE DO RECORTE", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["04"], 0.5)
    corte = ep(t, C["04.a"] + 1.0, 1.2)
    dobra = ep(t, C["04.b"], 1.0)
    folha(c, 640, 480, 640, 400, 90, a0 * (1 - dobra), corte, rot=corte > 0)
    caixa_iso(c, 640, 520, 460, 280, 90 + 40 * 0, dobra)
    if dobra > 0:
        pill(c, "caixa sem tampa", 640, 260, BLUE, size=28, a=dobra, anchor="center")
    acc = ep(t, C["04.c"], 0.5)
    if acc > 0:
        cartao(c, 1120, 300, 520, 170, acc)
        text_mid(c, "V depende de x", 1380, 385, 50, "black", PURPLE, acc)
    ad = ep(t, C["04.d"], 0.5)
    if ad > 0:
        rrect(c, 1120, 520, 520, 120, 22, mix("#FFFFFF", BLUE, 0.14), ad)
        text_mid(c, "isso é um POLINÔMIO", 1380, 580, 44, "black", BLUE, ad)


# ======================================================================
# bloco a — o que é polinômio, grau, o que não é
# ======================================================================

def b_definicao(c, t, C, B):
    head(c, t, B["start"], "O QUE É POLINÔMIO", "AS PEÇAS DE UM POLINÔMIO", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["05.a"], 0.5)
    defin(c, "POLINÔMIO", "soma de termos com x elevado a naturais (0, 1, 2, 3...)", 260, 200, 1400, aa, BLUE, 30)
    ab, acc, ad = ep(t, C["05.b"], 0.5), ep(t, C["05.c"], 0.5), ep(t, C["05.d"], 0.5)
    cores = {}
    if ab > 0:
        cores.update({0: PURPLE, 2: PURPLE, 4: PURPLE})
    if acc > 0:
        cores[6] = GREEN
    if ad > 0:
        cores[0] = AMBER
    expr(c, "2x^3 − 5x^2 + x + 7", 960, 450, 96, aa, cores=cores)
    if ab > 0:
        pill(c, "COEFICIENTES: os números que multiplicam o x", 760, 600, PURPLE, size=28, a=ab, anchor="center")
    if acc > 0:
        pill(c, "TERMO INDEPENDENTE: o 7, sem x", 1370, 330, GREEN, size=28, a=acc, anchor="center")
    if ad > 0:
        pill(c, "COEFICIENTE DOMINANTE: o da maior potência", 760, 690, AMBER, size=28, a=ad, anchor="center")


def b_grau(c, t, C, B):
    head(c, t, B["start"], "O GRAU", "O ANDAR MAIS ALTO", PURPLE)
    card(c, *CARD_R)
    aa = ep(t, C["06.a"], 0.5)
    ab = ep(t, C["06.b"], 0.5)
    ad = ep(t, C["06.d"], 0.5)
    some = ep(t, C["06.d"] + 6.0, 0.6)
    if ad <= 0:
        and_ = [("x^0", "0"), ("x", "360"), ("x^2", "−78"), ("x^3", "4")]
        alto = 3 if ab > 0 else None
    else:
        and_ = [("x^0", "−1"), ("x", "5"), ("x^2", "m − 2" if some < 0.5 else "0")]
        alto = (2 if some < 0.5 else 1) if ab > 0 else None
    predio(c, 300, 790, and_, aa, alto, w=380)
    if ab > 0:
        defin(c, "GRAU", "o maior expoente com coeficiente ≠ 0", 800, 210, 860, ab * (1 - ad), BLUE, 30)
    acc = ep(t, C["06.c"], 0.5) * (1 - ad)
    if acc > 0:
        expr(c, "4x^3 − 78x^2 + 360x", 1230, 430, 62, acc, cores={0: PURPLE})
        pill(c, "GRAU 3", 1230, 560, PURPLE, size=40, a=acc, anchor="center")
    if ad > 0:
        expr(c, "(m−2)x^2 + 5x − 1", 1230, 300, 58, ad, cores={0: AMBER})
        cartao(c, 900, 400, 660, 130, ad)
        linha(c, [("m ≠ 2  →  ", INK), ("grau 2", PURPLE)], 1230, 465, 46, ad)
        if some > 0:
            cartao(c, 900, 570, 660, 130, some)
            linha(c, [("m = 2  →  o andar some  →  ", INK), ("grau 1", RED)], 1230, 635, 40, some)


def b_nao_poli(c, t, C, B):
    head(c, t, B["start"], "NÃO É POLINÔMIO", "EXPOENTE SÓ NATURAL", RED)
    card(c, *CARD_R)
    for k, (cue, f, e, why) in enumerate((("07.a", "x^2 + 1/x", "1/x = x^{-1}", "expoente negativo"),
                                          ("07.b", "√{x} + 3", "√{x} = x^{1/2}", "expoente fração"))):
        ak, d = rise(t, C[cue])
        if ak <= 0:
            continue
        x = 300 + k * 700
        cartao(c, x, 230 + d, 620, 420, ak)
        expr(c, f, x + 310, 330 + d, 70, ak)
        expr(c, e, x + 310, 460 + d, 54, ak, cores={2: RED})
        pill(c, why, x + 310, 570 + d, RED, size=28, a=ak, anchor="center")
        selo(c, x + 560, 260 + d, ak, "NÃO", RED, 8, 34)
    acc = ep(t, C["07.c"], 0.5)
    if acc > 0:
        regra(c, "expoentes: 0, 1, 2, 3, ...  (naturais)", 960, 740, acc, 40, PURPLE)


def b_atalho_ordem(c, t, C, B):
    head(c, t, B["start"], "ATALHO", "ORGANIZE ANTES DE LER", GREEN)
    card(c, *CARD_R)
    a0 = ep(t, C["08"], 0.4)
    if a0 > 0:
        K.boxed(c, 260, 200, 1400, 600, GREEN, a0, 0.08)
        text(c, "ATALHO · DO MAIOR PARA O MENOR EXPOENTE", 960, 250, 24, "black", GREEN, a0, tracking=2)
    aa = ep(t, C["08.a"], 0.5)
    v = ep(t, C["08.a"] + 1.5, 1.0)
    if aa > 0:
        expr(c, "5x + 7 − x^4 + 2x^2", 960, 400, 64, aa * (1 - v), cores={2: RED})
        expr(c, "−x^4 + 2x^2 + 5x + 7", 960, 400, 64, v, cores={0: PURPLE})
        arrow(c, 960, 470, 960, 530, GREEN, aa, 5, 16)
    ab = ep(t, C["08.b"], 0.5)
    if ab > 0:
        pill(c, "o andar mais alto na FRENTE: grau 4", 960, 600, PURPLE, size=34, a=ab, anchor="center")


# ======================================================================
# bloco b — valor numérico e raiz
# ======================================================================

def b_valor(c, t, C, B):
    head(c, t, B["start"], "VALOR NUMÉRICO", "TROCAR x POR UM NÚMERO", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["09.a"], 0.5)
    defin(c, "VALOR NUMÉRICO", "P(a) = trocar x por a", 260, 200, 1400, aa, BLUE, 32)
    ab = ep(t, C["09.b"], 0.5)
    if ab > 0:
        expr(c, "P(x) = x^2 − 5x + 6", 960, 360, 64, ab)
        cartao(c, 260, 450, 680, 180, ab)
        expr(c, "P(4) = 16 − 20 + 6", 600, 510, 46, ab)
        text(c, "= 2", 600, 600, 50, "black", INK, ab)
    acc = ep(t, C["09.c"], 0.5)
    if acc > 0:
        cartao(c, 980, 450, 680, 180, acc, GREEN, True)
        expr(c, "P(2) = 4 − 10 + 6", 1320, 510, 46, acc)
        text(c, "= 0", 1320, 600, 50, "black", GREEN, acc)
    ad = ep(t, C["09.d"], 0.5)
    if ad > 0:
        regra(c, "RAIZ: o número que faz P dar ZERO · 2 é raiz", 960, 715, ad, 36, PURPLE)


# ======================================================================
# bloco c — o raio X
# ======================================================================

def b_raiox(c, t, C, B):
    head(c, t, B["start"], "DOIS VALORES DE GRAÇA", "O RAIO X DO POLINÔMIO", GREEN)
    card(c, *CARD_R)
    aa = ep(t, C["10.a"], 0.5)
    prog = clamp((t - C["10.b"] - 0.6) / 3.0)
    ae = ep(t, C["10.e"], 0.5)
    raiox(c, 960, 330, P_RX, aa * (1 - ae), prog, 76, sinais=S_RX)
    acc = ep(t, C["10.c"], 0.5) * (1 - ae)
    if acc > 0:
        rrect(c, 520, 450, 880, 120, 22, mix("#FFFFFF", GREEN, 0.16), acc)
        linha(c, [("P(1) = 2 − 5 + 1 + 7 = ", INK), ("5", GREEN)], 960, 510, 52, acc)
    ad = ep(t, C["10.d"], 0.5) * (1 - ae)
    if ad > 0:
        pill(c, "P(1) = SOMA DOS COEFICIENTES", 960, 660, GREEN, size=36, a=ad, anchor="center")
    if ae > 0:
        termos = [("2x^3", "0"), ("5x^2", "0"), ("x", "0"), ("7", "7")]
        raiox(c, 960, 330, termos, ae, 1.0, 76, col=GRAY, sinais=S_RX)
        rrect(c, 520, 450, 880, 120, 22, mix("#FFFFFF", BLUE, 0.16), ae)
        linha(c, [("P(0) = ", INK), ("7", BLUE)], 960, 510, 56, ae)
        pill(c, "P(0) = TERMO INDEPENDENTE", 960, 660, BLUE, size=36, a=ae, anchor="center")


def b_raiox_pot(c, t, C, B):
    head(c, t, B["start"], "PARA QUE SERVE", "SEM DESENVOLVER NADA", GREEN)
    card(c, *CARD_R)
    aa = ep(t, C["11.a"], 0.5)
    if aa > 0:
        expr(c, "(3x−2)^{10}", 960, 320, 100, aa, cores={0: PURPLE})
        text(c, "soma dos coeficientes = ?", 960, 450, 40, "black", INK2, aa)
    ab = ep(t, C["11.b"], 0.5)
    if ab > 0:
        selo(c, 1480, 300, ab * (1 - ep(t, C["11.c"], 0.4)), "desenvolver? NÃO", AMBER, -6, 34)
    acc = ep(t, C["11.c"], 0.5)
    if acc > 0:
        rrect(c, 460, 540, 1000, 140, 24, mix("#FFFFFF", GREEN, 0.16), acc)
        expr(c, "(3·1−2)^{10} = 1^{10} = 1", 960, 610, 64, acc, cores={4: GREEN})


def b_atalho_raiox(c, t, C, B):
    head(c, t, B["start"], "ATALHO", "TROQUE x POR 1 OU POR 0", GREEN)
    card(c, *CARD_R)
    a0 = ep(t, C["12"], 0.4)
    if a0 > 0:
        K.boxed(c, 260, 200, 1400, 600, GREEN, a0, 0.08)
        text(c, "ATALHO · O RAIO X", 960, 250, 24, "black", GREEN, a0, tracking=2)
    for k, (cue, q, r, col) in enumerate((("12.a", "soma dos coeficientes?", "x = 1", GREEN),
                                          ("12.b", "termo independente?", "x = 0", BLUE))):
        ak, d = rise(t, C[cue])
        if ak <= 0:
            continue
        y = 370 + k * 170 + d
        rrect(c, 340, y - 60, 1240, 120, 22, "#FFFFFF", ak, shadow=True)
        text(c, q, 400, y + 14, 44, "black", INK, ak, align="left")
        pill(c, r, 1500, y, col, size=44, a=ak, anchor="right", bounds=(0, 1920))
    acc = ep(t, C["12.c"], 0.5)
    if acc > 0:
        text(c, "sem desenvolver NADA", 960, 740, 40, "black", GREEN, acc)


# ======================================================================
# bloco d — o grau nas operações · bloco e — identidade · bloco f — modelar
# ======================================================================

def b_operacoes(c, t, C, B):
    head(c, t, B["start"], "O GRAU NAS CONTAS", "PRODUTO · SOMA · POTÊNCIA", PURPLE)
    card(c, *CARD_R)
    itens = [("13.a", "PRODUTO", "grau 3 × grau 2", "grau 5", PURPLE),
             ("13.b", "SOMA", "(x^2+1) + (−x^2+3x) = 3x + 1", "pode CAIR", AMBER),
             ("13.c", "POTÊNCIA", "(x^2−3x+3)^{20}", "2 · 20 = 40", PURPLE)]
    for k, (cue, tit, f, r, col) in enumerate(itens):
        ak, d = rise(t, C[cue])
        if ak <= 0:
            continue
        y = 300 + k * 170 + d
        rrect(c, 260, y - 65, 1400, 140, 22, "#FFFFFF", ak, shadow=True)
        rrect(c, 260, y - 65, 14, 140, 7, col, ak)
        text(c, tit, 310, y + 14, 36, "black", col, ak, align="left")
        expr(c, f, 900, y, 44, ak)
        pill(c, r, 1620, y, col, size=32, a=ak, anchor="right", bounds=(0, 1920))


def b_identidade(c, t, C, B):
    head(c, t, B["start"], "POLINÔMIOS IDÊNTICOS", "DUAS NOTAS FISCAIS", PURPLE)
    card(c, *CARD_R)
    aa = ep(t, C["14.a"], 0.5)
    defin(c, "IDÊNTICOS", "iguais para todo x: coeficiente com coeficiente", 260, 190, 1400, aa * (1 - ep(t, C["14.d"], 0.4)),
          BLUE, 30)
    ab = ep(t, C["14.b"], 0.5)
    t0 = C["14.c"]
    acesos = tuple(k for k, dt in enumerate((0.0, 2.6, 5.6)) if t >= t0 + dt)
    nota(c, 300, 300, 560, "NOTA 1", [("x^2", "a"), ("x", "b − 1"), ("x^0", "3")], ab, acesos)
    nota(c, 1060, 300, 560, "NOTA 2", [("x^2", "2"), ("x", "5"), ("x^0", "c")], ab, acesos)
    for k in acesos:
        yy = 420 + 74 * k
        ak = ep(t, t0 + (0.0, 2.6, 5.6)[k], 0.4)
        arrow(c, 870, yy, 1050, yy, PURPLE, ak, 4, 14)
        res = ["a = 2", "b = 6", "c = 3"][k]
        pill(c, res, 960, yy - 34, GREEN, size=24, a=ak, anchor="center", bounds=(0, 1920))
    ad = ep(t, C["14.d"], 0.5)
    if ad > 0:
        regra(c, "POLINÔMIO NULO: todos os coeficientes iguais a zero", 960, 740, ad, 34, PURPLE)


def b_modelar(c, t, C, B):
    head(c, t, B["start"], "MODELAR", "TRÊS MEDIDAS DE GRAU 1", PURPLE)
    card(c, *CARD_R)
    a0 = ep(t, C["15"], 0.5)
    aa = ep(t, C["15.a"], 0.5)
    caixa_iso(c, 600, 520, 440, 260, 130, a0, ("grau 1", "grau 1", "grau 1"), aa)
    ab = ep(t, C["15.b"], 0.5)
    if ab > 0:
        cartao(c, 1040, 300, 620, 130, ab)
        text_mid(c, "V = comprimento · largura · altura", 1350, 365, 34, "black", INK, ab)
    acc = ep(t, C["15.c"], 0.5)
    if acc > 0:
        rrect(c, 1040, 480, 620, 160, 22, mix("#FFFFFF", PURPLE, 0.14), acc)
        text_mid(c, "1 + 1 + 1 = GRAU 3", 1350, 560, 52, "black", PURPLE, acc)


# ======================================================================
# nós fazemos
# ======================================================================

def b_exercicio(c, t, C, B):
    head_seq(c, t, C, [("16", "SUA VEZ", "PAUSE E TENTE", GREEN), ("17", "VAMOS JUNTOS", "O RAIO X E OS PARÊNTESES",
                                                                       GREEN)])
    card(c, *CARD_R)
    aa = ep(t, C["16.a"], 0.5)
    expr(c, "P(x) = x^3 − 4x^2 + 2x + 5", 960, 290, 70, aa)
    ab = ep(t, C["16.b"], 0.5)
    sol = t >= C["17"]
    res = [("17.a", "P(0)", "= 5", "o termo independente"), ("17.b", "P(1)", "= 1 − 4 + 2 + 5 = 4", "soma dos coeficientes"),
           ("17.c", "P(−1)", "= −1 − 4 − 2 + 5 = −2", "com parênteses")]
    for k, (cue, q, r, sb) in enumerate(res):
        y = 430 + k * 125
        if ab > 0:
            cartao(c, 300, y - 50, 1320, 104, ab)
            expr(c, q, 420, y, 46, ab, cores={0: PURPLE})
        ak = ep(t, C[cue], 0.5) if sol else 0
        if ak > 0:
            expr(c, r, 560, y, 44, ak, align="left", cores={len(r.split()) - 1: GREEN})
            text(c, sb, 1580, y + 12, 26, "bold", INK2, ak, align="right")
        elif ab > 0:
            text(c, "= ?", 560, y + 16, 44, "black", GRAY, ab, align="left")
    if not sol:
        pause_timer(c, t, C["16.end"] - 1.9, 1700, 290)


# ======================================================================
# recap e erro
# ======================================================================

FRASES = ["Grau é o maior expoente que sobrevive.",
          "P(1) soma os coeficientes; P(0) dá o termo independente.",
          "Idênticos: coeficiente com coeficiente."]


def b_recap(c, t, C, B):
    sid = which(t, C, ["18", "27"])
    frame(c, t, B["start"] if sid == "18" else C["27"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "18" else "PARA FECHAR",
          PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 300 + k * 180 + d
        badge_num(c, k + 1, 260, y - 16, a, 36, bg=PURPLE)
        para(c, s, 320, y, 50, "black", INK, a, 1360, 60)


ERROS = [("soma dos coeficientes = P(0)  (responde 7)",
          "o zero parece o número que \"some com tudo\"",
          "ele some com os coeficientes também: a soma é P(1) = 5.")]


def b_erros(c, t, C, B):
    K.erro_cards(c, t, C, ["19"], ERROS)


# ======================================================================
# questão 1 (eu faço) e questão 8 (você faz)
# ======================================================================

ALTS1 = [("A", "= x^3 − 39x^2 + 360x", "tirou x uma vez só", RED), ("B", "= 4x^2 − 78x + 360", "só o fundo", RED),
         ("C", "= 4x^3 + 78x^2 + 360x", "sinal do meio", RED), ("D", "= 4x^3 − 78x^2 + 360x", "", GREEN),
         ("E", "= 4x^3 − 78x^2 + 360", "360 sem o x", RED)]


def b_q1(c, t, C, B):
    sid = which(t, C, ["20", "21", "22", "24"])
    heads = {"20": "MODELAR O VOLUME", "21": "EU FAÇO", "22": "CONFIRO COM NÚMEROS", "24": "AS ARMADILHAS"}
    head(c, t, B["start"] if sid == "20" else C[sid], "QUESTÃO 1 · ESTILO ENEM", heads[sid], PURPLE)
    card(c, *CARD_R)
    cues_in = {L: C[f"20.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"24.x{L.lower()}"] for L in "ABCE"}
    K.alternativas(c, t, C, ALTS1, 1110, 250, 620, 28, C["21.ok"], "D", cues_in, cues_x, gap=26)
    a0 = ep(t, C["20.a"], 0.4)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0, align="left")
    if sid == "20":
        folha(c, 620, 450, 560, 350, 76, a0, 0.0, med=("24 cm", "15 cm"))
        ab = ep(t, C["20.b"], 0.5)
        if ab > 0:
            text(c, "V(x) = ?", 620, 790, 46, "black", PURPLE, ab)
        return
    if sid == "21":
        dob = ep(t, C["21.a"] + 0.4, 1.0)
        folha(c, 620, 400, 520, 325, 70, ep(t, C["21"], 0.4) * (1 - dob), 1.0, rot=True)
        caixa_iso(c, 620, 380, 430, 260, 100, dob, ("24 − 2x", "15 − 2x", "x"), ep(t, C["21.a"] + 1.6, 0.5))
        ab = ep(t, C["21.b"], 0.5)
        if ab > 0:
            rrect(c, 170, 610, 900, 80, 18, mix("#FFFFFF", BLUE, 0.12), ab)
            expr(c, "(24−2x)(15−2x) = 360 − 78x + 4x^2", 620, 650, 34, ab)
        acc = ep(t, C["21.c"], 0.5)
        if acc > 0:
            rrect(c, 170, 710, 900, 90, 18, mix("#FFFFFF", PURPLE, 0.14), acc)
            expr(c, "x · (...) = 4x^3 − 78x^2 + 360x", 620, 755, 38, acc, cores={0: RED})
        return
    if sid == "22":
        aa = ep(t, C["22.a"], 0.5)
        cartao(c, 170, 250, 880, 170, aa)
        if aa > 0:
            linha(c, [("x = 1:  ", BLUE), ("22 · 13 · 1 = 286", INK)], 650, 310, 40, aa)
            linha(c, [("4 − 78 + 360 = ", INK), ("286", GREEN)], 650, 380, 40, aa)
        ab = ep(t, C["22.b"], 0.5)
        if ab > 0:
            selo(c, 650, 480, ab, "B e E TAMBÉM DÃO 286", AMBER, -3, 32)
        acc = ep(t, C["22.c"], 0.5)
        if acc > 0:
            cartao(c, 170, 560, 880, 220, acc, GREEN, True)
            linha(c, [("x = 2:  ", BLUE), ("20 · 11 · 2 = 440", INK)], 650, 620, 40, acc)
            linha(c, [("D: ", INK), ("440", GREEN), ("   B: ", INK), ("220", RED), ("   E: ", INK), ("80", RED)],
                  650, 700, 40, acc)
        return
    # 24: armadilhas — a caixa com as medidas
    caixa_iso(c, 600, 470, 430, 260, 100, ep(t, C["24"], 0.4), ("24 − 2x", "15 − 2x", "x"), 1.0)


def b_atalho_dois(c, t, C, B):
    head(c, t, B["start"], "ATALHO", "CONFIRA COM DOIS NÚMEROS", GREEN)
    card(c, *CARD_R)
    a0 = ep(t, C["23"], 0.4)
    if a0 > 0:
        K.boxed(c, 260, 200, 1400, 600, GREEN, a0, 0.08)
        text(c, "ATALHO · TESTE COM 1 E COM 2", 960, 250, 24, "black", GREEN, a0, tracking=2)
    aa = ep(t, C["23.a"], 0.5)
    if aa > 0:
        for k, (s_, col) in enumerate((("x = 1", BLUE), ("x = 2", PURPLE))):
            x = 680 + k * 560
            rrect(c, x - 220, 360, 440, 160, 26, "#FFFFFF", aa, shadow=True)
            text_mid(c, s_, x, 440, 70, "black", col, aa)
    ab = ep(t, C["23.b"], 0.5)
    if ab > 0:
        pill(c, "um número só pode coincidir POR ACASO", 960, 640, AMBER, size=34, a=ab, anchor="center")


ALTS8 = [("A", "= 1", "", GREEN), ("B", "= 40", "é o grau", RED), ("C", "= 3^{20}", "é P(0)", RED),
         ("D", "= 4^{20}", "só os positivos", RED), ("E", "= 7^{20}", "é P(−1)", RED)]


def b_q8(c, t, C, B):
    sid = which(t, C, ["25", "26"])
    head(c, t, B["start"] if sid == "25" else C["26"], "QUESTÃO 8 · ESTILO ENEM",
         "VOCÊ FAZ" if sid == "25" else "VAMOS CONFERIR", GREEN)
    card(c, *CARD_R)
    cues_in = {L: C[f"25.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"26.x{L.lower()}"] for L in "BCDE"}
    K.alternativas(c, t, C, ALTS8, 1300, 260, 420, 40, C["26.ok"], "A", cues_in, cues_x, gap=34)
    a0 = ep(t, C["25.a"], 0.4)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0, align="left")
    if a0 > 0:
        expr(c, "P(x) = (x^2−3x+3)^{20}", 680, 320, 66, a0, cores={2: PURPLE})
        text(c, "soma de todos os coeficientes = ?", 680, 440, 38, "black", INK, a0)
    if sid == "25":
        pause_timer(c, t, C["25.end"] - 1.9, 680, 620)
        return
    aa = ep(t, C["26.a"], 0.5)
    if aa > 0:
        rrect(c, 230, 540, 900, 150, 24, mix("#FFFFFF", GREEN, 0.16), aa)
        expr(c, "P(1) = (1−3+3)^{20} = 1^{20} = 1", 680, 615, 50, aa, cores={6: GREEN})


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "DIVISÃO E O TEOREMA DO RESTO", PURPLE)
    aa = ep(t, C["28.a"], 0.5)
    if aa > 0:
        cartao(c, 360, 260, 1200, 170, aa)
        linha(c, [("2x³ − x + 5", PURPLE), ("   ÷   ", INK), ("x + 1", BLUE)], 960, 345, 64, aa)
        text(c, "resto = ?   sem fazer a divisão?", 960, 520, 44, "black", INK, aa)
    ab = ep(t, C["28.b"], 0.5)
    if ab > 0:
        pill(c, "troque x por UM ÚNICO NÚMERO", 960, 640, GREEN, size=40, a=ab, anchor="center")
    acc = ep(t, C["28.c"], 0.5)
    if acc > 0:
        selo(c, 960, 770, acc, "PRÓXIMO EPISÓDIO", PURPLE, -3, 40)


def b_cta(c, t, C, B):
    cta(c, t, C["29.like"], C["29.sub"], C["29.bell"], C["29.com"], C["29.bye"],
        "Você já conhecia o truque do P(1)?", canal="no Estudativo", anki=C["29.anki"])


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, caixa=b_caixa, definicao=b_definicao, grau=b_grau,
              nao_poli=b_nao_poli, atalho_ordem=b_atalho_ordem, valor=b_valor, raiox=b_raiox, raiox_pot=b_raiox_pot,
              atalho_raiox=b_atalho_raiox, operacoes=b_operacoes, identidade=b_identidade, modelar=b_modelar,
              exercicio=b_exercicio, recap=b_recap, erros=b_erros, q1=b_q1, atalho_dois=b_atalho_dois, q8=b_q8,
              ponte=b_ponte, cta=b_cta)
