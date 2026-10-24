"""Visual — Função Composta e Função Inversa, Episódio 1: composição (máquinas em fila e a ordem que importa) (tema claro).
Peças comuns da série em ../../comum.py (reexporta o 019/comum.py: expr, alternativas, erro_cards, atalho...).
Peças deste episódio: maquina() (caixa com funil e regra), esteira(), bola() (o número viajando), etiqueta() e carimbo()
(o caixa da loja), linha().
Cores com função: azul = definição · roxo = regra/fórmula · âmbar = armadilha · verde = atalho/dica · vermelho = erro.
A máquina g é AZUL e a máquina f é ROXA em todo o episódio.
"""
import importlib.util
from pathlib import Path
import skia
import motor
motor.set_theme("claro")
from motor import *  # noqa
from aula import *  # noqa

_p = Path(__file__).resolve().parents[2] / "comum.py"
_s = importlib.util.spec_from_file_location("comum045", _p)
K = importlib.util.module_from_spec(_s); _s.loader.exec_module(K)
K.usar_tempos(Path(__file__).resolve().parents[1] / "audio" / "tempos.json")
motor.set_theme("claro")
frame, head_seq, which, para, regra, selo, pause_timer, chip = (K.frame, K.head_seq, K.which, K.para, K.regra, K.selo,
                                                                 K.pause_timer, K.chip)
fmid, ftext, ftext_w = K.fmid, K.ftext, K.ftext_w

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_composta_inversa_ep1_maquinas_em_fila.mp4"
CARD_R = K.CARD_R
COL_G, COL_F = BLUE, PURPLE


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


def maquina(c, cx, cy, nome, lei, col, a, brilho=0.0, w=300, h=210):
    """máquina: corpo colorido, funil de entrada à esquerda, bocal de saída à direita, nome grande e a regra"""
    if a <= 0:
        return
    x, y = cx - w / 2, cy - h / 2
    # funil
    p = skia.Path(); p.moveTo(x - 60, cy - 60); p.lineTo(x, cy - 28); p.lineTo(x, cy + 28); p.lineTo(x - 60, cy + 60)
    p.close()
    c.drawPath(p, paint(mix("#FFFFFF", col, 0.35), a))
    # bocal
    rrect(c, x + w - 4, cy - 26, 56, 52, 8, mix("#FFFFFF", col, 0.35), a)
    rrect(c, x, y, w, h, 28, mix("#FFFFFF", col, 0.12 + 0.25 * brilho), a, shadow=True)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 28, 28), paint(col, a, stroke=6))
    fmid(c, nome, cx, cy - h * 0.16, h * 0.36, "black", col, a)
    sz = 34
    while K.math_w(lei, sz) > w - 30 and sz > 18:
        sz -= 2
    K.expr(c, lei, cx, cy + h * 0.26, sz, a, cores={i: INK for i in range(12)})


def esteira(c, x0, x1, y, a):
    if a <= 0:
        return
    rrect(c, x0, y - 9, x1 - x0, 18, 9, "#D5D8DE", a)
    for k in range(int((x1 - x0) // 40) + 1):
        c.drawCircle(x0 + 10 + k * 40, y, 5, paint("#9AA0AA", a))


def bola(c, x, y, s, col, a, r=46):
    if a <= 0:
        return
    c.drawCircle(x, y, r, paint("#FFFFFF", a))
    c.drawCircle(x, y, r, paint(col, a, stroke=6))
    sz = r * 0.95
    while ftext_w(s, "black", sz) > r * 1.6 and sz > 16:
        sz -= 2
    fmid(c, s, x, y, sz, "black", col, a)


def viagem(c, t, t0, xs, y, nums, cols, dur=1.6):
    """o número passa pelas máquinas: xs = [x_entrada, x_m1, x_m2, x_saida]; nums = [entra, meio, sai].
    Etapa 1 (t0): entra e some na 1ª máquina; etapa 2 (t0 + dur): sai o meio e entra na 2ª; etapa 3: sai o resultado."""
    u1 = ep(t, t0, dur)
    if t >= t0:
        if u1 < 1:
            bola(c, lerp(xs[0], xs[1], ease_io(u1)), y, nums[0], INK, 1 - ep(t, t0 + dur * 0.75, dur * 0.25))
    return u1


def etiqueta(c, cx, cy, preco, a, w=300, h=120, col=None):
    if a <= 0:
        return
    col = col or AMBER
    x, y = cx - w / 2, cy - h / 2
    p = skia.Path(); p.moveTo(x + h * 0.35, y); p.lineTo(x + w, y); p.lineTo(x + w, y + h); p.lineTo(x + h * 0.35, y + h)
    p.lineTo(x, cy); p.close()
    c.drawPath(p, paint(col, a))
    c.drawCircle(x + h * 0.30, cy, h * 0.09, paint("#FFFFFF", a))
    fmid(c, preco, cx + h * 0.15, cy, h * 0.34, "black", "#FFFFFF", a)


def carimbo(c, cx, cy, s, col, a, size=34):
    if a <= 0:
        return
    w = ftext_w(s, "black", size) + size * 1.4
    h = max(72, size * 1.9)
    rrect(c, cx - w / 2, cy - h / 2, w, h, 14, mix("#FFFFFF", col, 0.10), a)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2, cy - h / 2, w, h), 14, 14), paint(col, a, stroke=5))
    fmid(c, s, cx, cy, size, "black", col, a)


def rotulo(c, s, cx, cy, col, a, size=26):
    pill(c, s, cx, cy, col, size=size, a=a, anchor="center")


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "FUNÇÃO COMPOSTA", BLUE)
    aa = ep(t, C["01.a"], 0.5)
    etiqueta(c, 420, 450, "R$ 150,00", aa, 380, 150)
    carimbo(c, 900, 360, "CUPOM −R$ 20", RED, ep(t, C["01.a"] + 1.6, 0.4), 38)
    carimbo(c, 900, 540, "−10%", RED, ep(t, C["01.a"] + 2.8, 0.4), 38)
    ab = ep(t, C["01.b"], 0.4)
    if ab > 0:
        chip(c, "TANTO FAZ A ORDEM?", 1440, 450, AMBER, ab * (1 - ep(t, C["01.c"], 0.4)), 40)
    acc = ep(t, C["01.c"], 0.5)
    if acc > 0:
        for k, (s_, col) in enumerate((("R$ 117,00", RED), ("R$ 115,00", GREEN))):
            a = ep(t, C["01.c"] + k * 1.6, 0.4)
            rrect(c, 1240, 320 + k * 190, 420, 150, 24, "#FFFFFF", a, shadow=True)
            text(c, f"ORDEM {k + 1}", 1450, 360 + k * 190, 24, "black", GRAY, a)
            fmid(c, s_, 1450, 425 + k * 190, 58, "black", col, a)
    ad = ep(t, C["01.d"], 0.5)
    if ad > 0:
        regra(c, "qual ordem pedir no caixa?", W / 2, 770, ad, 40, BLUE)


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "AO FINAL DESTA AULA", "VOCÊ VAI CONSEGUIR", GREEN)
    a, d = rise(t, C["02.a"])
    check_icon(c, 300, 346 + d, 34, a, GREEN)
    text(c, "calcular f(g(x)) em um número", 360, 360 + d, 50, "black", INK, a, align="left")
    ab, db = rise(t, C["02.b"])
    check_icon(c, 300, 486 + db, 34, ab, GREEN)
    text(c, "montar a LEI DA COMPOSTA", 360, 500 + db, 50, "black", INK, ab, align="left")
    acc = ep(t, C["02.c"], 0.5)
    if acc > 0:
        maquina(c, 760, 690, "g", "2x + 1", COL_G, acc, 0, 220, 150)
        arrow(c, 900, 690, 1020, 690, INK2, acc, 5)
        maquina(c, 1150, 690, "f", "x^2 - 1", COL_F, acc, 0, 220, 150)
        pill(c, "sem trocar a ordem", 1500, 690, AMBER, size=28, a=acc, anchor="center")


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "TRÊS LEMBRETES", "RÁPIDOS", GREEN)
    aa = ep(t, C["03.a"], 0.5)
    if aa > 0:
        text(c, "Conceito de Função", 400, 270, 26, "bold", GRAY, aa)
        K.expr(c, "f(x) = x^2 - 1", 400, 360, 54, aa)
        K.expr(c, "f(5) = 5^2 - 1 = 24", 400, 460, 54, ep(t, C["03.a"] + 1.6, 0.4), cores={2: INK, 6: GREEN})
        text(c, "troque o x por 5", 400, 540, 28, "black", BLUE, ep(t, C["03.a"] + 1.6, 0.4))
    ab = ep(t, C["03.b"], 0.5)
    if ab > 0:
        text(c, "uma EXPRESSÃO inteira", 1000, 270, 26, "bold", GRAY, ab)
        K.expr(c, "f(2x+1) = (2x+1)^2 - 1", 1000, 380, 50, ab, cores={0: INK, 2: AMBER})
        pill(c, "sempre ENTRE PARÊNTESES", 1000, 470, AMBER, size=26, a=ab, anchor="center")
    acc = ep(t, C["03.c"], 0.5)
    if acc > 0:
        text(c, "Expressões algébricas", 1560, 270, 26, "bold", GRAY, acc)
        K.expr(c, "(2x+1)^2", 1560, 370, 54, acc)
        K.expr(c, "= 4x^2 + 4x + 1", 1560, 470, 46, acc, cores={3: GREEN})
        text(c, "com o termo do meio", 1560, 540, 28, "black", GREEN, acc)
    line(c, 700, 240, 700, 760, "#E6E6E2", ab, 3)
    line(c, 1300, 240, 1300, 760, "#E6E6E2", acc, 3)


def b_concreto(c, t, C, B):
    head(c, t, B["start"], "UMA ETAPA ALIMENTA A OUTRA", "FÁBRICA E CAIXA", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["04.a"], 0.5)
    if aa > 0:
        text(c, "FÁBRICA", 520, 250, 30, "black", BLUE, aa)
        esteira(c, 180, 860, 520, aa)
        for k, (nome, col) in enumerate((("CORTA", COL_G), ("PINTA", COL_F))):
            x = 370 + k * 300
            rrect(c, x - 100, 360, 200, 130, 22, mix("#FFFFFF", col, 0.14), aa, shadow=True)
            fmid(c, nome, x, 425, 34, "black", col, aa)
        u = ep(t, C["04.b"], 2.4)
        xx = lerp(200, 820, u)
        cor = "#C9B48A" if xx < 650 else PURPLE
        lw = 90 if xx < 400 else 60
        rrect(c, xx - lw / 2, 470, lw, 40, 8, cor, ep(t, C["04.b"], 0.3))
    acc = ep(t, C["04.c"], 0.5)
    if acc > 0:
        text(c, "CAIXA DA LOJA", 1380, 250, 30, "black", BLUE, acc)
        etiqueta(c, 1380, 370, "R$ 150,00", acc, 330, 120)
        carimbo(c, 1230, 540, "CUPOM", RED, acc, 32)
        carimbo(c, 1530, 540, "−10%", RED, acc, 32)
        text_mid(c, "preço final:  R$ ?", 1380, 660, 40, "black", AMBER, ep(t, C["04.c"] + 1.4, 0.4))
    line(c, 960, 240, 960, 720, "#E6E6E2", acc, 3)
    ad = ep(t, C["04.d"], 0.5)
    if ad > 0:
        regra(c, "o que sai de uma etapa ENTRA na outra", W / 2, 770, ad, 38, BLUE)


# ======================================================================
# bloco a — definição
# ======================================================================

def b_definicao(c, t, C, B):
    head_seq(c, t, C, [("05", "FUNÇÃO COMPOSTA", "f DE g DE x", BLUE), ("06", "COMO SE LÊ", "DE DENTRO PARA FORA", PURPLE)])
    card(c, *CARD_R)
    sid = which(t, C, ["05", "06"])
    aa = ep(t, C["05.a"], 0.5)
    if aa > 0:
        linha(c, [("f", COL_F), ("(", INK), ("g", COL_G), ("(x)", INK), (")", INK)], W / 2, 330, 120, aa)
        if sid == "05":
            text(c, "uma função aplicada ao RESULTADO de outra", W / 2, 450, 34, "black", INK, aa)
    if sid == "05":
        ab = ep(t, C["05.b"], 0.5)
        if ab > 0:
            linha(c, [("f ∘ g", INK), ("   lê-se  ", GRAY), ("“f bola g”", BLUE)], W / 2, 540, 50, ab)
        acc = ep(t, C["05.c"], 0.5)
        if acc > 0:
            rotulo(c, "g = FUNÇÃO DE DENTRO: age 1º", 640, 660, COL_G, acc, 28)
            rotulo(c, "f = FUNÇÃO DE FORA: age 2º", 1280, 660, COL_F, ep(t, C["05.c"] + 1.8, 0.4), 28)
        return
    ab = ep(t, C["06.a"], 0.5)
    if ab > 0:
        text(c, "escreve:  f  →  g", 700, 470, 40, "black", GRAY, ab)
        text(c, "age:  g  →  f", 1220, 470, 40, "black", GREEN, ab)
    ac = ep(t, C["06.b"], 0.5)
    if ac > 0:
        arrow(c, 1080, 400, 820, 400, GREEN, ac, 6, progress=ep(t, C["06.b"], 1.0))
        pill(c, "de dentro para fora", W / 2, 560, GREEN, size=30, a=ac, anchor="center")
    ad = ep(t, C["06.c"], 0.5)
    if ad > 0:
        rrect(c, 380, 640, 1160, 120, 22, mix("#FFFFFF", AMBER, 0.14), ad)
        text_mid(c, "o que sai de g precisa estar no DOMÍNIO de f", W / 2, 700, 36, "black", AMBER, ad)


# ======================================================================
# bloco b — os valores passando pelas máquinas
# ======================================================================

def _fila(c, t, C, sid, ordem):
    """ordem = 'gf' (g primeiro) ou 'fg'. Cues: b = entra e sai o do meio, c = sai o resultado."""
    y = 470
    X1, X2 = 720, 1260
    a0 = ep(t, C[sid], 0.4)
    esteira(c, 220, 1720, y + 140, a0)
    m1, m2 = (("g", "2x + 1", COL_G), ("f", "x^2 - 1", COL_F)) if ordem == "gf" else \
        (("f", "x^2 - 1", COL_F), ("g", "2x + 1", COL_G))
    nums = ("2", "5", "24") if ordem == "gf" else ("2", "3", "7")
    tb = C[f"{sid}.b"] if sid == "07" else C[f"{sid}.a"]
    tc = C[f"{sid}.c"] if sid == "07" else C[f"{sid}.b"]
    on1 = ep(t, tb + 0.8, 0.3) * (1 - ep(t, tb + 2.6, 0.3))
    on2 = ep(t, tc + 0.8, 0.3) * (1 - ep(t, tc + 2.6, 0.3))
    maquina(c, X1, y, *m1[:2], m1[2], a0, on1)
    maquina(c, X2, y, *m2[:2], m2[2], a0, on2)
    # entrada
    if t < tb:
        bola(c, 330, y, nums[0], INK, a0)
    else:
        u = ep(t, tb, 1.0)
        if u < 1:
            bola(c, lerp(330, X1 - 170, ease_io(u)), y, nums[0], INK, 1 - ep(t, tb + 0.8, 0.2))
    # meio
    if t >= tb + 1.4:
        u = ep(t, tc, 1.0) if t >= tc else 0
        x = lerp(X1 + 230, X2 - 170, ease_io(u)) if t >= tc else X1 + 230
        bola(c, (X1 + X2) / 2 if t < tc else x, y + (0 if t >= tc else 0), nums[1], m1[2],
             ep(t, tb + 1.4, 0.4) * (1 - ep(t, tc + 0.8, 0.2)))
    # saída
    if t >= tc + 1.4:
        bola(c, 1640, y, nums[2], m2[2], ep(t, tc + 1.4, 0.4), 56)
    return y


def b_maquinas(c, t, C, B):
    head_seq(c, t, C, [("07", "MÁQUINAS EM FILA", "PRIMEIRO g, DEPOIS f", COL_G), ("08", "TROCANDO A ORDEM", "PRIMEIRO f, DEPOIS g", COL_F)])
    card(c, *CARD_R)
    sid = which(t, C, ["07", "08"])
    if sid == "07":
        aa = ep(t, C["07.a"], 0.5)
        _fila(c, t, C, "07", "gf")
        if aa > 0:
            K.expr(c, "g(x) = 2x + 1", 600, 260, 40, aa, cores={0: COL_G})
            K.expr(c, "f(x) = x^2 - 1", 1320, 260, 40, aa, cores={0: COL_F})
        ad = ep(t, C["07.d"], 0.5)
        if ad > 0:
            regra(c, "f(g(2)) = f(5) = 24", W / 2, 770, ad, 44)
        return
    _fila(c, t, C, "08", "fg")
    acc = ep(t, C["08.c"], 0.5)
    if acc > 0:
        regra(c, "g(f(2)) = g(3) = 7     ≠     f(g(2)) = 24", W / 2, 770, acc, 40, RED)


# ======================================================================
# bloco c — número antes de lei
# ======================================================================

def b_numero(c, t, C, B):
    head(c, t, B["start"], "ATALHO", "NÚMERO ANTES DE LEI", GREEN)
    card(c, *CARD_R)
    K.expr(c, "f(g(3)) = ?", W / 2, 250, 60, ep(t, C["09"], 0.4))
    aa = ep(t, C["09.a"], 0.5)
    K.atalho(c, 360, 320, 1200, 130, "ATALHO", ["pediu um número? calcule a de dentro e jogue o número na de fora"], aa, 32)
    ab = ep(t, C["09.b"], 0.5)
    if ab > 0:
        bola(c, 520, 560, "1º", COL_G, ab, 40)
        K.expr(c, "g(3) = 2·3 + 1 = 7", 960, 560, 52, ab, cores={0: COL_G, 6: GREEN})
    acc = ep(t, C["09.c"], 0.5)
    if acc > 0:
        bola(c, 520, 680, "2º", COL_F, acc, 40)
        K.expr(c, "f(7) = 7^2 - 1 = 48", 960, 680, 52, acc, cores={0: COL_F, 6: GREEN})
    ad = ep(t, C["09.d"], 0.5)
    if ad > 0:
        selo(c, 1560, 640, ad, "2 PASSOS CURTOS", GREEN, -5, 30)


# ======================================================================
# bloco d — a lei da composta
# ======================================================================

def b_lei(c, t, C, B):
    head_seq(c, t, C, [("10", "LEI DA COMPOSTA", "f(g(x))", COL_F), ("11", "A OUTRA ORDEM", "g(f(x))", COL_G)])
    card(c, *CARD_R)
    sid = which(t, C, ["10", "11"])
    X = 320
    if sid == "10":
        aa = ep(t, C["10.a"], 0.5)
        if aa > 0:
            text(c, "LEI DA COMPOSTA: a regra que liga a entrada direto à saída", W / 2, 250, 32, "black", BLUE, aa)
        ab = ep(t, C["10.b"], 0.5)
        if ab > 0:
            K.expr(c, "f(x) = x^2 - 1", X, 360, 44, ab, cores={0: COL_F}, align="left")
            K.expr(c, "f(g(x)) = (2x+1)^2 - 1", X, 470, 56, ep(t, C["10.b"] + 1.2, 0.4), cores={0: COL_F, 2: COL_G},
                   align="left")
            pill(c, "troque cada x pela g INTEIRA, entre parênteses", 1320, 470, AMBER, size=24,
                 a=ep(t, C["10.b"] + 1.8, 0.4), anchor="center")
        acc = ep(t, C["10.c"], 0.5)
        if acc > 0:
            K.expr(c, "= 4x^2 + 4x + 1 - 1", X + 270, 580, 50, acc, cores={3: GREEN}, align="left")
            pill(c, "termo do meio", 1320, 580, GREEN, size=24, a=acc, anchor="center")
        ad = ep(t, C["10.d"], 0.5)
        if ad > 0:
            regra(c, "f(g(x)) = 4x² + 4x", W / 2, 720, ad, 50)
        return
    ab = ep(t, C["11.a"], 0.5)
    if ab > 0:
        K.expr(c, "g(x) = 2x + 1", X, 300, 44, ab, cores={0: COL_G}, align="left")
        K.expr(c, "g(f(x)) = 2·(x^2-1) + 1", X, 410, 56, ep(t, C["11.a"] + 1.0, 0.4), cores={0: COL_G, 2: COL_F},
               align="left")
    acc = ep(t, C["11.b"], 0.5)
    if acc > 0:
        K.expr(c, "= 2x^2 - 2 + 1 = 2x^2 - 1", X + 270, 520, 50, acc, cores={6: GREEN, 7: GREEN, 8: GREEN},
               align="left")
    ad = ep(t, C["11.c"], 0.5)
    if ad > 0:
        rrect(c, 300, 610, 1320, 170, 24, "#FFFFFF", ad, shadow=True)
        linha(c, [("4x² + 4x", COL_F), ("   ≠   ", RED), ("2x² − 1", COL_G)], W / 2, 660, 50, ad)
        linha(c, [("x = 2:   ", GRAY), ("24", COL_F), ("   e   ", GRAY), ("7", COL_G)], W / 2, 735, 40,
              ep(t, C["11.c"] + 1.6, 0.4))


def b_comuta(c, t, C, B):
    head(c, t, B["start"], "COMUTATIVA?", "A ORDEM IMPORTA", COL_F)
    card(c, *CARD_R)
    aa = ep(t, C["12.a"], 0.5)
    if aa > 0:
        text(c, "COMUTATIVA = a ordem não muda o resultado", W / 2, 260, 34, "black", BLUE, aa)
        linha(c, [("2 + 3 = 3 + 2", GREEN)], W / 2, 340, 52, aa)
    ab = ep(t, C["12.b"], 0.5)
    if ab > 0:
        linha(c, [("f ∘ g", COL_F), ("  ≠  ", RED), ("g ∘ f", COL_G)], W / 2, 450, 64, ab)
        text(c, "em geral, a composição NÃO é comutativa", W / 2, 520, 30, "black", INK, ab)
    acc = ep(t, C["12.c"], 0.5)
    if acc > 0:
        for k, (s1, s2, ok) in enumerate((("MEIA", "SAPATO", True), ("SAPATO", "MEIA", False))):
            a = ep(t, C["12.c"] + k * 2.0, 0.4)
            x = 560 + k * 800
            rrect(c, x - 330, 590, 660, 160, 24, mix("#FFFFFF", GREEN if ok else RED, 0.10), a)
            linha(c, [("1º ", GRAY), (s1, INK), ("   →   2º ", GRAY), (s2, INK)], x - 20, 650, 36, a)
            check_icon(c, x + 270, 650, 26, a, GREEN if ok else RED, "check" if ok else "x")
            text(c, "tudo certo" if ok else "não dá", x, 720, 30, "black", GREEN if ok else RED, a)


def b_atalho(c, t, C, B):
    head(c, t, B["start"], "ATALHO", "CONFIRA A LEI COM UM NÚMERO", GREEN)
    card(c, *CARD_R)
    aa = ep(t, C["13.a"], 0.5)
    K.atalho(c, 360, 230, 1200, 130, "ATALHO", ["montou a lei? teste com um número que você já conhece"], aa, 32)
    ab = ep(t, C["13.b"], 0.5)
    if ab > 0:
        K.expr(c, "f(g(x)) = 4x^2 + 4x", W / 2, 450, 50, ab, cores={0: COL_F})
        K.expr(c, "x = 2:  4·4 + 4·2 = 24", W / 2, 560, 52, ep(t, C["13.b"] + 1.0, 0.4), cores={7: GREEN})
    acc = ep(t, C["13.c"], 0.5)
    if acc > 0:
        bola(c, 700, 690, "24", COL_F, acc, 50)
        text_mid(c, "=  o 24 das máquinas", 1040, 690, 40, "black", INK, acc)
        selo(c, 1450, 690, ep(t, C["13.c"] + 1.4, 0.4), "BATEU", GREEN, -5, 36)


def b_produto(c, t, C, B):
    head(c, t, B["start"], "ARMADILHA", "COMPOR NÃO É MULTIPLICAR", AMBER)
    card(c, *CARD_R)
    aa = ep(t, C["14.a"], 0.5)
    if aa > 0:
        K.expr(c, "f(2) = 3", 620, 300, 50, aa, cores={0: COL_F})
        K.expr(c, "g(2) = 5", 1300, 300, 50, aa, cores={0: COL_G})
        K.expr(c, "f(2) · g(2) = 3 · 5 = 15", W / 2, 420, 58, ep(t, C["14.a"] + 1.4, 0.4), cores={8: AMBER})
    ab = ep(t, C["14.b"], 0.5)
    if ab > 0:
        linha(c, [("15", AMBER), ("   ≠   ", RED), ("f(g(2)) = 24", COL_F)], W / 2, 540, 54, ab)
    acc = ep(t, C["14.c"], 0.5)
    if acc > 0:
        regra(c, "compor = o resultado de uma ENTRA na outra", W / 2, 700, acc, 38)


# ======================================================================
# nós fazemos
# ======================================================================

def b_exercicio(c, t, C, B):
    head_seq(c, t, C, [("15", "SUA VEZ", "PAUSE E TENTE", GREEN), ("16", "VAMOS JUNTOS", "DE DENTRO PARA FORA", GREEN)])
    card(c, *CARD_R)
    aa = ep(t, C["15.a"], 0.5)
    if aa > 0:
        K.expr(c, "f(x) = 3x", 600, 260, 46, aa, cores={0: COL_F})
        K.expr(c, "g(x) = x + 4", 1320, 260, 46, aa, cores={0: COL_G})
    ab = ep(t, C["15.b"], 0.5)
    if ab > 0:
        K.expr(c, "f(g(1)) = ?", 600, 380, 54, ab)
        K.expr(c, "g(f(1)) = ?", 1320, 380, 54, ab)
    pause_timer(c, t, C["15.end"] - 1.9, W / 2, 560)
    if t < C["16"]:
        return
    a1 = ep(t, C["16.a"], 0.4)
    if a1 > 0:
        K.expr(c, "g(1) = 5", 600, 500, 44, a1, cores={0: COL_G})
        K.expr(c, "f(5) = 15", 600, 590, 50, ep(t, C["16.a"] + 3.0, 0.4), cores={0: COL_F, 2: GREEN})
    a2 = ep(t, C["16.b"], 0.4)
    if a2 > 0:
        K.expr(c, "f(1) = 3", 1320, 500, 44, a2, cores={0: COL_F})
        K.expr(c, "g(3) = 7", 1320, 590, 50, ep(t, C["16.b"] + 3.0, 0.4), cores={0: COL_G, 2: GREEN})
    acc = ep(t, C["16.c"], 0.5)
    if acc > 0:
        regra(c, "15  ≠  7: ordens diferentes, resultados diferentes", W / 2, 730, acc, 36)


# ======================================================================
# recap, erros
# ======================================================================

FRASES = ["O que sai de uma máquina entra na outra.",
          "Leia de dentro para fora: a de dentro age primeiro.",
          "Trocou a ordem, trocou o resultado."]


def b_recap(c, t, C, B):
    sid = which(t, C, ["17", "29"])
    frame(c, t, B["start"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "17" else "PARA FECHAR", PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 300 + k * 180 + d
        badge_num(c, k + 1, 260, y - 16, a, 36, bg=PURPLE)
        para(c, s, 320, y, 50, "black", INK, a, 1360, 60)


ERROS = [("Em f(g(x)), aplicar a f primeiro", "a gente lê da esquerda para a direita, e o f vem antes",
          "a de dentro age primeiro: comece pela g"),
         ("Achar que f(g(x)) = g(f(x))", "na soma e na multiplicação a ordem não importa",
          "a composição não é comutativa: com x = 2, 24 contra 7"),
         ("Multiplicar f(x) · g(x) em vez de substituir", "f(g) lembra f vezes g, como 2(3) lembra 2 × 3",
          "compor é colocar uma DENTRO da outra: o produto deu 15, a composta, 24"),
         ("Em f(2x + 1), elevar só o x: 2x² + 1 − 1", "na f, o quadrado está grudado no x",
          "o x virou a expressão INTEIRA: (2x + 1)² − 1")]


def b_erros(c, t, C, B):
    K.erro_cards(c, t, C, ["18", "19", "20", "21"], ERROS)


# ======================================================================
# questões
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


ALTS2 = [("A", "9", "ordem trocada: g(f(2))", RED), ("B", "10", "somou: 3 + 7", RED), ("C", "21", "multiplicou: 3 · 7", RED),
         ("D", "24", "sem o termo do meio", RED), ("E", "48", "", GREEN)]


def b_q2(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 2 · EU FAÇO", "COMPOSTA EM UM PONTO", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["22.a"], 0.4)
    yend = _enunciado(c, [("Considere as funções f(x) = x² − 1 e g(x) = 2x + 3, definidas para todo x real. O valor de "
                           "f(g(2)) é", INK)], a0, 240, 30)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0 * (1 - ep(t, C["23"], 0.3)),
         align="left")
    cues_in = {L: C[f"22.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"24.x{L.lower()}"] for L in "ABCD"}
    K.alternativas(c, t, C, ALTS2, 1000, 250, 680, 44, C["23.ok"], "E", cues_in, cues_x, gap=34)
    pause_timer(c, t, C["22.end"] - 1.9, 540, yend + 140)
    if C["23"] <= t < C["24"]:
        y0 = yend + 4
        _painel(c, y0, ep(t, C["23"], 0.4))
        pill(c, "pediu um número → número antes de lei", 540, y0 + 50, GREEN, size=24, a=ep(t, C["23"], 0.4),
             anchor="center")
        K.expr(c, "g(2) = 2·2 + 3 = 7", 540, y0 + 150, 42, ep(t, C["23.a"], 0.4), cores={0: COL_G, 6: GREEN})
        K.expr(c, "f(7) = 49 - 1 = 48", 540, y0 + 250, 42, ep(t, C["23.b"], 0.4), cores={0: COL_F, 6: GREEN})
    if t >= C["24"]:
        y0 = yend + 4
        _painel(c, y0, ep(t, C["24"], 0.4))
        text(c, "cada errada = um erro clássico", 540, y0 + 60, 28, "black", AMBER, ep(t, C["24"], 0.4))
        ad = ep(t, C["24.xd"], 0.4)
        if ad > 0:
            K.expr(c, "(2x+3)^2 ≠ 4x^2 + 9", 540, y0 + 170, 40, ad, cores={1: RED})
            K.expr(c, "16 + 9 - 1 = 24", 540, y0 + 260, 38, ad, cores={6: RED})


ALTS6 = [("A", "O preço final é o mesmo nas duas ordens.", "", RED),
         ("B", "Aplicar o cupom antes é R$ 2,00 mais barato.", "", RED),
         ("C", "Aplicar o cupom antes é R$ 18,00 mais barato.", "", RED),
         ("D", "Aplicar a porcentagem antes é R$ 2,00 mais barato.", "", GREEN),
         ("E", "Aplicar a porcentagem antes é R$ 20,00 mais barato.", "", RED)]
POR_QUE6 = [("xa", "A: achou que a composição comuta"), ("xb", "B: inverteu a conclusão"),
            ("xc", "C: 18 é o que o cupom vale, não a diferença"), ("xe", "E: o cupom inteiro não é a diferença")]


def _caixa(c, t, C, y0):
    """as duas ordens no caixa, lado a lado: 150 → cupom → 130 → −10% → 117 · 150 → −10% → 135 → cupom → 115"""
    for k, (rot, passos, fim, col, cue) in enumerate((
            ("CUPOM ANTES", (("−R$ 20", "130"), ("−10%", "117")), "R$ 117,00", RED, "26.a"),
            ("PORCENTAGEM ANTES", (("−10%", "135"), ("−R$ 20", "115")), "R$ 115,00", GREEN, "26.b"))):
        a = ep(t, C[cue], 0.4)
        if a <= 0:
            continue
        y = y0 + 70 + k * 190
        text(c, rot, 540, y - 6, 24, "black", col, a)
        x = 230
        fmid(c, "150", x + 30, y + 60, 36, "black", INK, a)
        for j, (cb, val) in enumerate(passos):
            aj = ep(t, C[cue] + 1.2 + j * 1.8, 0.4)
            carimbo(c, x + 175 + j * 260, y + 60, cb, RED, aj, 24)
            fmid(c, val, x + 290 + j * 260, y + 60, 36, "black", INK if j == 0 else col, aj)
        linha(c, [(fim, col)], 540, y + 120, 30, ep(t, C[cue] + 4.4, 0.4))


def b_q6(c, t, C, B):
    head_seq(c, t, C, [("25", "QUESTÃO 6 · VOCÊ FAZ", "A ORDEM DOS DESCONTOS", GREEN),
                       ("26", "CONFERINDO", "DUAS MÁQUINAS", BLUE), ("27", "POR QUE R$ 2,00?", "AS DUAS LEIS", PURPLE),
                       ("28", "AS ERRADAS", "E A SÉRIE DE DESCONTOS", AMBER)])
    card(c, *CARD_R)
    a0 = ep(t, C["25.a"], 0.4)
    enun = ("Uma loja oferece, para um produto de R$ 150,00, um cupom que abate R$ 20,00 do preço e uma promoção de 10% "
            "de desconto. O sistema permite aplicar os dois benefícios, em qualquer ordem, sempre sobre o valor "
            "resultante da etapa anterior. Comparando as duas ordens possíveis, conclui-se que")
    sid = which(t, C, ["25", "26", "27", "28"])
    yend = _enunciado(c, [(enun, INK)], a0 * (1 - ep(t, C["26"], 0.3)), 240, 24) if sid == "25" else 240
    if sid == "25":
        text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0, align="left")
    cues_in = {L: C[f"25.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"28.x{L.lower()}"] for L in "ABCE"}
    K.alternativas(c, t, C, ALTS6, 1000, 240, 690, 26, C["26.ok"], "D", cues_in, cues_x, gap=22)
    pause_timer(c, t, C["25.end"] - 1.9, 540, yend + 120)
    if sid == "26":
        y0 = 230
        _painel(c, y0, ep(t, C["26"], 0.4))
        K.expr(c, "c(p) = p - 20", 360, y0 + 40, 30, ep(t, C["26"], 0.4), cores={0: RED})
        K.expr(c, "d(p) = 0,9p", 720, y0 + 40, 30, ep(t, C["26"], 0.4), cores={0: RED})
        _caixa(c, t, C, y0 + 60)
        acc = ep(t, C["26.c"], 0.4)
        if acc > 0:
            selo(c, 700, y0 + 520, acc, "R$ 2,00 MAIS BARATO", GREEN, -4, 26)
    elif sid == "27":
        y0 = 230
        _painel(c, y0, ep(t, C["27"], 0.4))
        aa = ep(t, C["27.a"], 0.4)
        if aa > 0:
            text(c, "cupom antes", 540, y0 + 60, 26, "black", RED, aa)
            K.expr(c, "d(c(p)) = 0,9·(p-20) = 0,9p - 18", 540, y0 + 120, 30, aa, cores={6: RED})
            text(c, "porcentagem antes", 540, y0 + 210, 26, "black", GREEN, ep(t, C["27.a"] + 2.0, 0.4))
            K.expr(c, "c(d(p)) = 0,9p - 20", 540, y0 + 270, 32, ep(t, C["27.a"] + 2.0, 0.4), cores={4: GREEN})
        ab = ep(t, C["27.b"], 0.4)
        if ab > 0:
            pill(c, "os 10% caem também sobre o cupom: ele vale só R$ 18", 540, y0 + 360, AMBER, size=20, a=ab,
                 anchor="center")
        acc = ep(t, C["27.c"], 0.4)
        if acc > 0:
            K.atalho(c, 200, y0 + 420, 680, 140, "ATALHO DE CAIXA", ["porcentagem primeiro, cupom depois"], acc, 28)
    elif sid == "28":
        y0 = 230
        _painel(c, y0, ep(t, C["28"], 0.4))
        for k, (cue, s_) in enumerate(POR_QUE6):
            a = ep(t, C["28." + cue], 0.4)
            if a > 0:
                check_icon(c, 215, y0 + 52 + k * 52, 16, a, RED, "x")
                text(c, s_, 245, y0 + 60 + k * 52, 22, "black", INK, a, align="left")
        aa = ep(t, C["28.a"], 0.4)
        if aa > 0:
            text(c, "série de Descontos:", 540, y0 + 300, 24, "black", GRAY, aa)
            K.expr(c, "0,8 · 0,9 = 0,9 · 0,8", 540, y0 + 360, 34, aa)
            pill(c, "% com %: COMUTA", 360, y0 + 440, GREEN, size=24, a=aa, anchor="center")
        ab = ep(t, C["28.b"], 0.4)
        if ab > 0:
            pill(c, "R$ com %: NÃO COMUTA", 720, y0 + 440, RED, size=24, a=ab, anchor="center")
            text(c, "as duas aulas não se contradizem", 540, y0 + 530, 24, "black", INK2, ab)


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "COMPOSIÇÃO EM CONTEXTO", PURPLE)
    aa = ep(t, C["30.a"], 0.5)
    if aa > 0:
        maquina(c, 600, 450, "h", "horas → peças", COL_G, aa, 0, 340, 200)
        arrow(c, 800, 450, 1000, 450, INK2, aa, 5)
        maquina(c, 1240, 450, "R$", "peças → custo", COL_F, aa, 0, 340, 200)
        linha(c, [("40 peças/h", COL_G), ("     ·     ", GRAY), ("R$ 3,00 por peça + custo fixo", COL_F)], W / 2, 620,
              34, aa)
    ab = ep(t, C["30.b"], 0.5)
    if ab > 0:
        rrect(c, 520, 670, 880, 90, 24, mix("#FFFFFF", AMBER, 0.16), ab)
        text_mid(c, "custo em função das HORAS = ?", W / 2, 715, 40, "black", AMBER, ab)
    pill(c, "ep. 2 · composição em contexto", W / 2, 810, PURPLE, size=30, a=ep(t, C["30.c"], 0.5), anchor="center")


def b_cta(c, t, C, B):
    cta(c, t, C["31.like"], C["31.sub"], C["31.bell"], C["31.com"], C["31.bye"],
        "Onde a ordem das etapas muda o resultado?", canal="no Estudativo", anki=C["31.anki"])


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, concreto=b_concreto, definicao=b_definicao,
              maquinas=b_maquinas, numero=b_numero, lei=b_lei, comuta=b_comuta, atalho=b_atalho, produto=b_produto,
              exercicio=b_exercicio, recap=b_recap, erros=b_erros, q2=b_q2, q6=b_q6, ponte=b_ponte, cta=b_cta)
