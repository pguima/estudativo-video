"""Visual — Sistemas de Equações Lineares, Episódio 1: o que é um sistema, do texto ao sistema e a substituição (tema claro).
Peças comuns da série em ../../comum.py (reexporta o 019/comum.py: expr, alternativas, erro_cards, atalho...).
Peças deste episódio: cercado() (o sítio com 10 cabeças: galinhas e coelhos), tentativas() (a tabela (0, 10) … (10, 0) com o
contador de patas; só o (6, 4) acende verde em 28), etiqueta() (as etiquetas das incógnitas no canto, com unidade),
peca_troca() (a peça "m" sai da equação e a peça "(30 − c)" encaixa, com os parênteses piscando), estrada() (a rodovia da Q9).
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
_s = importlib.util.spec_from_file_location("comum037", _p)
K = importlib.util.module_from_spec(_s); _s.loader.exec_module(K)
K.usar_tempos(Path(__file__).resolve().parents[1] / "audio" / "tempos.json")
motor.set_theme("claro")
frame, head_seq, which, para, boxed, regra, selo, pause_timer, chip = (K.frame, K.head_seq, K.which, K.para, K.boxed, K.regra,
                                                                        K.selo, K.pause_timer, K.chip)
fmid, ftext, ftext_w, expr = K.fmid, K.ftext, K.ftext_w, K.expr

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_sistemas_ep1_texto_substituicao.mp4"
CARD_R = K.CARD_R
GALINHA = "#F2E6CF"
CRISTA = "#D9473B"
COELHO = "#B9B2A8"
CERCA = "#A97F48"
GRAMA = "#E4F1DC"


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


def galinha(c, cx, cy, s, a):
    if a <= 0:
        return
    c.drawCircle(cx, cy, s * 0.5, paint(GALINHA, a))
    c.drawCircle(cx, cy, s * 0.5, paint("#C9B48E", a, stroke=2))
    for k in (-1, 0, 1):
        c.drawCircle(cx + k * s * 0.12, cy - s * 0.52, s * 0.1, paint(CRISTA, a))
    p = skia.Path(); p.moveTo(cx + s * 0.46, cy - s * 0.04); p.lineTo(cx + s * 0.68, cy + s * 0.04)
    p.lineTo(cx + s * 0.46, cy + s * 0.12); p.close()
    c.drawPath(p, paint(AMBER, a))
    c.drawCircle(cx + s * 0.18, cy - s * 0.1, s * 0.06, paint(INK, a))


def coelho(c, cx, cy, s, a):
    if a <= 0:
        return
    for k in (-1, 1):
        c.drawOval(skia.Rect.MakeXYWH(cx + k * s * 0.2 - s * 0.1, cy - s * 1.0, s * 0.2, s * 0.6), paint(COELHO, a))
        c.drawOval(skia.Rect.MakeXYWH(cx + k * s * 0.2 - s * 0.05, cy - s * 0.92, s * 0.1, s * 0.44), paint("#E8B7B7", a))
    c.drawCircle(cx, cy, s * 0.5, paint(COELHO, a))
    c.drawCircle(cx, cy, s * 0.5, paint("#8E877E", a, stroke=2))
    for k in (-1, 1):
        c.drawCircle(cx + k * s * 0.17, cy - s * 0.08, s * 0.06, paint(INK, a))
    c.drawCircle(cx, cy + s * 0.12, s * 0.07, paint("#E8B7B7", a))


def cabeca(c, cx, cy, s, a):
    """cabeça ainda sem tipo (só a contagem)"""
    if a <= 0:
        return
    c.drawCircle(cx, cy, s * 0.5, paint("#FFFFFF", a))
    c.drawCircle(cx, cy, s * 0.5, paint(INK2, a, stroke=3))
    fmid(c, "?", cx, cy, s * 0.5, "black", GRAY, a)


def cercado(c, x, y, w, h, a, g=None, cc=None, s=70):
    """o sítio: cerca de madeira com 10 cabeças. g/cc = quantas galinhas e coelhos mostrar (None = cabeças '?')"""
    if a <= 0:
        return
    rrect(c, x, y, w, h, 24, GRAMA, a)
    for k in range(int(w // 60) + 1):
        xx = x + k * (w / int(w // 60))
        rrect(c, xx - 6, y - 24, 12, 40, 4, CERCA, a)
        rrect(c, xx - 6, y + h - 16, 12, 40, 4, CERCA, a)
    line(c, x, y - 8, x + w, y - 8, CERCA, a, 6)
    line(c, x, y + h + 4, x + w, y + h + 4, CERCA, a, 6)
    for k in range(10):
        cx = x + w * (0.1 + 0.2 * (k % 5))
        cy = y + h * (0.32 if k < 5 else 0.74)
        if g is None:
            cabeca(c, cx, cy, s, a)
        elif k < g:
            galinha(c, cx, cy, s, a)
        else:
            coelho(c, cx, cy, s, a)


def tentativas(c, t, x0, y, a, t_rev, dur, t_win, cw=138):
    """tabela (g, c) de (0, 10) a (10, 0) e o contador de patas; as colunas aparecem de t_rev a t_rev + dur;
    em t_win só o (6, 4) fica verde (28) e as outras apagam."""
    if a <= 0:
        return
    aw = ep(t, t_win, 0.5)
    text(c, "galinhas, coelhos", x0 - 30, y + 8, 24, "black", GRAY, a, align="right")
    text(c, "patas", x0 - 30, y + 118, 24, "black", GRAY, a, align="right")
    for g in range(11):
        cc = 10 - g
        ak = a * ep(t, t_rev + dur * g / 11, 0.3)
        if ak <= 0:
            continue
        xx = x0 + g * cw
        win = g == 6
        dim = 1 - 0.65 * aw if not win else 1
        col = mix(INK, GREEN, aw) if win else INK
        if win and aw > 0:
            rrect(c, xx - 6, y - 40, cw - 12, 200, 18, GREEN, 0.14 * aw)
        text(c, f"({g}, {cc})", xx + cw / 2 - 6, y + 10, 30, "black", col, ak * dim)
        n = 2 * g + 4 * cc
        text(c, f"{n}", xx + cw / 2 - 6, y + 120, 44, "black", GREEN if win and aw > 0 else INK2, ak * dim)


def etiqueta(c, letra, desc, x, y, a, col=None):
    """etiqueta da incógnita, no canto da tela: [ m ] = meias (ingressos)"""
    if a <= 0:
        return
    col = col or BLUE
    w = ftext_w(desc, "bold", 24) + 110
    rrect(c, x, y - 28, w, 56, 16, mix("#FFFFFF", col, 0.10), a)
    rrect(c, x + 8, y - 20, 50, 40, 10, col, a)
    fmid(c, letra, x + 33, y, 28, "black", "#FFFFFF", a)
    ftext(c, desc, x + 72, y + 9, 24, "bold", INK2, a, align="left")
    return w


def etiquetas(c, itens, x, y, a, dy=66):
    for k, (L, d) in enumerate(itens):
        etiqueta(c, L, d, x, y + k * dy, a)


def passos(c, t, rows, x, y0, size, dy, a_mult=1.0, xnota=None):
    """linhas da conta: rows = [(instante, partes_ou_expr, nota, cor_da_nota)]; partes = [(texto, cor)] vai por linha()"""
    xnota = xnota or 1660
    for k, (t0, ex, nota, col) in enumerate(rows):
        a, d = rise(t, t0)
        a *= a_mult
        if a <= 0:
            continue
        yy = y0 + k * dy + d
        if isinstance(ex, list):
            linha(c, ex, x, yy, size, a, align="left")
        else:
            expr(c, ex, x, yy, size, a, align="left")
        if nota:
            pill(c, nota, xnota, yy, col or PURPLE, size=24, a=a, anchor="right", bounds=(0, 1920))


def chave(c, x, y0, y1, a, col=None):
    """a chave { do sistema"""
    if a <= 0:
        return
    col = col or PURPLE
    m = (y0 + y1) / 2
    p = skia.Path()
    p.moveTo(x + 16, y0); p.quadTo(x, y0, x, y0 + 20); p.lineTo(x, m - 16); p.quadTo(x, m, x - 14, m)
    p.quadTo(x, m, x, m + 16); p.lineTo(x, y1 - 20); p.quadTo(x, y1, x + 16, y1)
    c.drawPath(p, paint(col, a, stroke=5, cap_round=True))


def sistema(c, l1, l2, x, y, size, a, dy=None, cols=(None, None), rot=None):
    """sistema de 2 equações com chave; l1/l2 = partes (linha) ou expr; rot = rótulos à direita"""
    if a <= 0:
        return
    dy = dy or size * 1.5
    chave(c, x - 24, y - size * 0.75, y + dy + size * 0.6, a)
    for k, ln in enumerate((l1, l2)):
        yy = y + k * dy
        if isinstance(ln, list):
            linha(c, ln, x, yy, size, a, align="left")
        else:
            expr(c, ln, x, yy, size, a, align="left", cores={i: cols[k] for i in range(12)} if cols[k] else None)
        if rot:
            pill(c, rot[k], x + (rot[2] if len(rot) > 2 else 620), yy, GRAY, size=22, a=a, anchor="left", bounds=(0, 1920))


def peca_troca(c, t, t0, x, y, size, a):
    """substituição: '4c + 2m = 100' → a peça m sobe e sai; a peça (30 − c) desce e encaixa, com os parênteses piscando"""
    if a <= 0:
        return
    u = ep(t, t0, 1.2)
    v = ep(t, t0 + 1.0, 1.2)
    pre = "4c + 2"
    wpre = ftext_w(pre, "black", size)
    linha(c, [(pre, INK)], x, y, size, a, align="left")
    xm = x + wpre
    # peça m: sai para cima
    am = a * (1 - u)
    if am > 0:
        rrect(c, xm - 6, y - size * 0.62 - 90 * u, ftext_w("m", "black", size) + 12, size * 1.2, 12, mix("#FFFFFF", RED, 0.14), am)
        fmid(c, "m", xm, y - 90 * u, size, "black", RED, am, align="left")
    # peça (30 − c): desce e encaixa
    body = "(30 − c)"
    wb = ftext_w(body, "black", size)
    ap = a * v
    if ap > 0:
        yy = y - 120 * (1 - v)
        pisca = 0.5 + 0.5 * math.cos((t - t0 - 2.2) * 7) if t > t0 + 2.2 else 1
        rrect(c, xm - 6, yy - size * 0.62, wb + 12, size * 1.2, 12, mix("#FFFFFF", GREEN, 0.16), ap)
        wp = ftext_w("(", "black", size)
        fmid(c, "(", xm, yy, size, "black", mix(GREEN, AMBER, 1 - pisca), ap, align="left")
        fmid(c, "30 − c", xm + wp, yy, size, "black", GREEN, ap, align="left")
        fmid(c, ")", xm + wb - ftext_w(")", "black", size), yy, size, "black", mix(GREEN, AMBER, 1 - pisca), ap,
             align="left")
    xr = xm + (wb if v > 0.5 else ftext_w("m", "black", size))
    linha(c, [(" = 100", INK)], xr + 8, y, size, a, align="left")


def estrada(c, x0, x1, y, a, tcar=0.0, tbus=0.0, marca=None):
    """rodovia do km 0 ao km 200 (escala); carro sai do km 20 indo para a direita, ônibus do km 200 indo para a esquerda.
    tcar/tbus em horas (0 → 1). marca = km destacado (verde)."""
    if a <= 0:
        return
    km = lambda k: x0 + (x1 - x0) * k / 200
    rrect(c, x0 - 30, y - 34, x1 - x0 + 60, 68, 20, "#5C6672", a)
    for k in range(0, 200, 12):
        line(c, km(k), y, km(k + 6), y, "#FFFFFF", a, 4)
    for k in (20, 80, 200):
        line(c, km(k), y - 34, km(k), y - 48, GRAY, a, 3)
        text(c, f"km {k}", km(k), y - 56, 20, "black", GREEN if k == marca else GRAY, a)
    pc = km(20 + 60 * tcar)
    pb = km(200 - 120 * tbus)
    # carro na faixa de cima, ônibus na de baixo (não se cobrem no encontro)
    rrect(c, pc - 34, y - 30, 68, 26, 8, BLUE, a)
    fmid(c, "carro", pc, y - 17, 16, "black", "#FFFFFF", a)
    rrect(c, pb - 40, y + 4, 80, 26, 8, AMBER, a)
    fmid(c, "ônibus", pb, y + 17, 16, "black", "#FFFFFF", a)
    if tcar < 0.95:
        arrow(c, pc + 38, y - 17, pc + 70, y - 17, "#FFFFFF", a, 3, 10)
        arrow(c, pb - 44, y + 17, pb - 76, y + 17, "#FFFFFF", a, 3, 10)


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "SISTEMAS DE EQUAÇÕES", BLUE)
    aa = ep(t, C["01.a"], 0.5)
    if aa > 0:
        rrect(c, 360, 230, 1200, 130, 26, "#FFFFFF", aa, shadow=True)
        text(c, "“Pedro tem o dobro das moedas de Júlia.”", W / 2, 312, 46, "black", INK, aa)
    ab = ep(t, C["01.b"], 0.5)
    if ab > 0:
        rrect(c, 330, 420, 560, 170, 26, mix("#FFFFFF", RED, 0.10), ab)
        check_icon(c, 400, 488, 40, ab, RED, "x")
        linha(c, [("2P = J", RED)], 650, 505, 90, ab)
        text(c, "metade escreve assim", 610, 570, 24, "bold", GRAY, ab)
    acc = ep(t, C["01.c"], 0.5)
    if acc > 0:
        rrect(c, 1030, 420, 560, 170, 26, mix("#FFFFFF", AMBER, 0.12), acc)
        text(c, "TESTE COM NÚMEROS", 1310, 470, 22, "black", AMBER, acc, tracking=2)
        linha(c, [("J = 5  →  P = 10", INK)], 1310, 525, 44, acc)
        linha(c, [("10 = 2 · 5", GREEN)], 1310, 570, 32, acc)
    ad = ep(t, C["01.d"], 0.5)
    if ad > 0:
        rrect(c, 610, 660, 700, 170, 30, mix("#FFFFFF", GREEN, 0.16), ad)
        check_icon(c, 690, 728, 44, ad, GREEN)
        linha(c, [("P = 2J", GREEN)], 1000, 745, 110, ad)


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "AO FINAL", "VOCÊ VAI CONSEGUIR", GREEN)
    rows = [("02.a", "transformar um texto em sistema", "“10 cabeças e 28 patas”  →  2 equações"),
            ("02.b", "resolver pela substituição sem perder sinal", "2(30 − c) = 60 − 2c")]
    for j, (cue, s, sub) in enumerate(rows):
        a, d = rise(t, C[cue])
        y = 360 + j * 200 + d
        check_icon(c, 300, y - 14, 34, a, GREEN)
        text(c, s, 360, y, 50, "black", INK, a, align="left")
        ftext(c, sub, 360, y + 60, 34, "bold", GRAY, a, align="left")


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "DOIS LEMBRETES", "RÁPIDOS", GREEN)
    aa = ep(t, C["03.a"], 0.5)
    if aa > 0:
        text(c, "A ETIQUETA DO X", 560, 280, 34, "black", BLUE, aa)
        text(c, "série de Equações do 1º grau", 560, 324, 24, "bold", GRAY, aa)
        text(c, "antes de montar, diga o que a letra conta", 560, 400, 24, "bold", INK2, aa)
        etiqueta(c, "c", "nº de carros (veículos)", 380, 520, ep(t, C["03.a"] + 1.6, 0.4))
        etiqueta(c, "m", "nº de motos (veículos)", 380, 600, ep(t, C["03.a"] + 2.2, 0.4))
    ab = ep(t, C["03.b"], 0.5)
    if ab > 0:
        text(c, "A DISTRIBUTIVA", 1360, 280, 34, "black", PURPLE, ab)
        text(c, "série de Expressões Algébricas", 1360, 324, 24, "bold", GRAY, ab)
        text(c, "o número da frente multiplica CADA termo", 1360, 400, 24, "bold", INK2, ab)
        linha(c, [("2(30 − c)", INK)], 1360, 520, 70, ep(t, C["03.b"] + 2.5, 0.4))
        linha(c, [("= 60 ", PURPLE), ("− 2c", PURPLE)], 1360, 640, 70, ep(t, C["03.b"] + 4.5, 0.4))
    line(c, 960, 240, 960, 760, "#E6E6E2", ab, 3)


# ======================================================================
# concreto: o sítio
# ======================================================================

def b_sitio(c, t, C, B):
    head_seq(c, t, C, [("04", "UM SÍTIO", "10 CABEÇAS", BLUE), ("05", "A SEGUNDA PISTA", "28 PATAS", BLUE)])
    sid = which(t, C, ["04", "05"])
    if sid == "04":
        aa = ep(t, C["04.a"], 0.5)
        cercado(c, 260, 270, 760, 360, aa)
        pill(c, "10 cabeças", 640, 700, INK, size=34, a=aa, anchor="center")
        ab = ep(t, C["04.b"], 0.5)
        opts = [("1 galinha · 9 coelhos", 0.0), ("2 galinhas · 8 coelhos", 1.6), ("6 galinhas · 4 coelhos", 3.0)]
        for k, (s, dt) in enumerate(opts):
            a, d = rise(t, C["04.b"] + dt)
            if a <= 0:
                continue
            y = 330 + k * 120 + d
            rrect(c, 1120, y - 44, 560, 88, 20, "#FFFFFF", a, shadow=True)
            text(c, s, 1400, y + 12, 34, "black", INK, a)
        acc = ep(t, C["04.c"], 0.5)
        if acc > 0:
            selo(c, 1400, 730, acc, "MUITAS RESPOSTAS", AMBER, -3, 36)
        return
    aa = ep(t, C["05.a"], 0.5)
    if aa > 0:
        galinha(c, 520, 290, 70, aa)
        text(c, "2 patas", 600, 302, 34, "black", INK, aa, align="left")
        coelho(c, 1180, 300, 70, aa)
        text(c, "4 patas", 1260, 312, 34, "black", INK, aa, align="left")
        pill(c, "28 patas", W / 2, 400, BLUE, size=34, a=aa, anchor="center")
    tentativas(c, t, 330, 520, ep(t, C["05.b"], 0.4), C["05.b"] + 0.4, max(2.5, C["05.c"] - C["05.b"] - 0.6), C["05.c"],
               cw=138)
    ad = ep(t, C["05.d"], 0.5)
    if ad > 0:
        regra(c, "a segunda informação ESCOLHEU uma resposta só", W / 2, 790, ad, 32, GREEN)


# ======================================================================
# bloco a — definição
# ======================================================================

def b_definicao(c, t, C, B):
    head_seq(c, t, C, [("06", "O NOME DE CADA COISA", "INCÓGNITA · SISTEMA · PAR", BLUE),
                       ("07", "O SÍTIO EM EQUAÇÕES", "CONFIRA NAS DUAS", PURPLE)])
    card(c, *CARD_R)
    sid = which(t, C, ["06", "07"])
    if sid == "06":
        rows = [("06.a", "INCÓGNITA", "cada valor escondido (g = galinhas, c = coelhos)"),
                ("06.b", "SISTEMA LINEAR", "equações do 1º grau que valem AO MESMO TEMPO"),
                ("06.c", "PAR ORDENADO", "a resposta em dupla, numa ordem combinada: (6, 4)"),
                ("06.d", "SOLUÇÃO DO SISTEMA", "o par que satisfaz TODAS as equações")]
        for k, (cue, tit, s) in enumerate(rows):
            a, d = rise(t, C[cue])
            if a <= 0:
                continue
            y = 250 + k * 140 + d
            rrect(c, 220, y, 1480, 116, 22, mix("#FFFFFF", BLUE, 0.07), a)
            rrect(c, 220, y, 12, 116, 6, BLUE, a)
            text(c, tit, 270, y + 72, 34, "black", BLUE, a, align="left")
            text(c, s, 1660, y + 70, 30, "bold", INK2, a, align="right")
        return
    etiquetas(c, [("g", "nº de galinhas"), ("c", "nº de coelhos")], 1360, 260, ep(t, C["07"], 0.4))
    aa = ep(t, C["07.a"], 0.5)
    ab = ep(t, C["07.b"], 0.5)
    chave(c, 300, 270, 470, ab)
    linha(c, [("g + c = 10", INK)], 340, 300, 64, aa, align="left")
    pill(c, "cabeças", 1000, 300, GRAY, size=24, a=aa, anchor="center")
    linha(c, [("2g + 4c = 28", INK)], 340, 430, 64, ab, align="left")
    pill(c, "patas", 1000, 430, GRAY, size=24, a=ab, anchor="center")
    acc = ep(t, C["07.c"], 0.5)
    if acc > 0:
        rrect(c, 300, 520, 1320, 120, 22, mix("#FFFFFF", GREEN, 0.10), acc)
        text(c, "TESTE (6, 4)", 340, 595, 26, "black", GREEN, acc, align="left", tracking=2)
        conferido(c, "6 + 4 = 10", 640, 595, ep(t, C["07.c"] + 1.2, 0.4), True, 34)
        conferido(c, "12 + 16 = 28", 1040, 595, ep(t, C["07.c"] + 2.6, 0.4), True, 34)
    ad = ep(t, C["07.d"], 0.5)
    if ad > 0:
        regra(c, "duas incógnitas pedem DUAS PISTAS: uma equação por informação", W / 2, 750, ad, 32)


# ======================================================================
# bloco c — testar é permitido
# ======================================================================

def b_testar(c, t, C, B):
    head(c, t, B["start"], "TESTAR AS ALTERNATIVAS", "NAS DUAS EQUAÇÕES", GREEN)
    card(c, *CARD_R)
    aa = ep(t, C["08.a"], 0.5)
    if aa > 0:
        sistema(c, "g + c = 10", "2g + 4c = 28", 300, 300, 50, aa)
        K.atalho(c, 980, 230, 680, 170, "ATALHO", ["teste o par nas DUAS equações"], aa, 32)
    for k, (cue, par, e1, ok1, e2, ok2) in enumerate(
            [("08.b", "(10, 2)", "10 + 2 = 12", False, "20 + 8 = 28", True),
             ("08.c", "(4, 6)", "4 + 6 = 10", True, "8 + 24 = 32", False)]):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        y = 480 + k * 130 + d
        rrect(c, 260, y - 50, 1400, 100, 22, "#FFFFFF", a, shadow=True)
        text(c, par, 340, y + 14, 44, "black", AMBER, a, align="left")
        conferido(c, e1, 620, y + 12, a, ok1, 34)
        conferido(c, e2, 1100, y + 12, a, ok2, 34)
    ad = ep(t, C["08.d"], 0.5)
    if ad > 0:
        selo(c, W / 2, 790, ad, "FECHA SÓ UMA? É A ARMADILHA", AMBER, -2, 34)


# ======================================================================
# bloco d — o molde
# ======================================================================

MOLDE = [("ingressos", "i + m = 400", "40i + 20m = 11 200"),
         ("veículos", "c + m = 30", "4c + 2m = 100"),
         ("café", "a + b = 60", "30a + 45b = 40 · 60")]


def b_molde(c, t, C, B):
    head_seq(c, t, C, [("09", "O MOLDE", "UMA CONTA, OUTRA SOMA VALORES", PURPLE),
                       ("10", "ATÉ PROVA COM NOTA NEGATIVA", "+5 POR ACERTO · −2 POR ERRO", PURPLE)])
    card(c, *CARD_R)
    sid = which(t, C, ["09", "10"])
    if sid == "09":
        aa = ep(t, C["09.a"], 0.5)
        ab = ep(t, C["09.b"], 0.5)
        if aa > 0:
            rrect(c, 560, 230, 520, 90, 20, mix("#FFFFFF", BLUE, 0.12), aa)
            text(c, "EQUAÇÃO DAS QUANTIDADES", 820, 270, 22, "black", BLUE, aa, tracking=1)
            text(c, "conta: cabeças, ingressos, veículos", 820, 304, 20, "bold", INK2, aa)
        if ab > 0:
            rrect(c, 1120, 230, 560, 90, 20, mix("#FFFFFF", PURPLE, 0.12), ab)
            text(c, "EQUAÇÃO DOS VALORES", 1400, 270, 22, "black", PURPLE, ab, tracking=1)
            text(c, "soma valores: patas, reais, rodas", 1400, 304, 20, "bold", INK2, ab)
        for k, (nome, q, v) in enumerate(MOLDE):
            a, d = rise(t, C["09.c"] + 1.6 * k)
            if a <= 0:
                continue
            y = 410 + k * 110 + d
            rrect(c, 240, y - 44, 1440, 88, 18, "#FFFFFF", a, shadow=True)
            text(c, nome, 270, y + 12, 32, "black", GRAY, a, align="left")
            linha(c, [(q, BLUE)], 820, y, 40, a)
            linha(c, [(v, PURPLE)], 1400, y, 40, a)
        ad = ep(t, C["09.d"], 0.5)
        if ad > 0:
            regra(c, "uma equação CONTA, a outra SOMA VALORES", W / 2, 790, ad, 34)
        return
    etiquetas(c, [("a", "nº de acertos (questões)"), ("e", "nº de erros (questões)")], 1240, 260, ep(t, C["10"], 0.4))
    aa = ep(t, C["10.a"], 0.5)
    if aa > 0:
        text(c, "20 questões · +5 por acerto · −2 por erro · nota 51", 260, 280, 30, "bold", INK2, aa, align="left")
    ab = ep(t, C["10.b"], 0.5)
    chave(c, 300, 370, 540, ab)
    linha(c, [("a + e = 20", BLUE)], 340, 400, 60, ab, align="left")
    linha(c, [("5a − 2e = 51", PURPLE)], 340, 520, 60, ep(t, C["10.b"] + 2.0, 0.4), align="left")
    acc = ep(t, C["10.c"], 0.5)
    if acc > 0:
        rrect(c, 300, 610, 1320, 170, 24, mix("#FFFFFF", GREEN, 0.12), acc)
        linha(c, [("13 acertos", GREEN), ("  e  ", INK), ("7 erros", GREEN)], W / 2, 660, 50, acc)
        conferido(c, "5 · 13 − 2 · 7 = 65 − 14 = 51", 620, 735, ep(t, C["10.c"] + 1.8, 0.4), True, 34)


# ======================================================================
# bloco e — frases de comparação
# ======================================================================

def b_comparacao(c, t, C, B):
    head(c, t, B["start"], "FRASES DE COMPARAÇÃO", "TRADUZA E TESTE", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["11.a"], 0.5)
    if aa > 0:
        text(c, "“Pedro tem o dobro de Júlia”", 520, 280, 36, "black", INK, aa)
        linha(c, [("P = 2J", GREEN)], 520, 380, 80, ep(t, C["11.a"] + 2.2, 0.4))
    ab = ep(t, C["11.b"], 0.5)
    if ab > 0:
        K.selo_teste(c, 520, 500, ab, True, "TESTE: J = 5, P = 10")
    acc = ep(t, C["11.c"], 0.5)
    if acc > 0:
        text(c, "“se Pedro der 6 moedas a Júlia,", 1380, 280, 34, "black", INK, acc)
        text(c, "ficam iguais”", 1380, 326, 34, "black", INK, acc)
    ad = ep(t, C["11.d"], 0.5)
    if ad > 0:
        pill(c, "quem dá PERDE", 1220, 430, RED, size=28, a=ad, anchor="center")
        pill(c, "quem recebe GANHA", 1560, 430, GREEN, size=28, a=ad, anchor="center")
        linha(c, [("P − 6", RED), (" = ", INK), ("J + 6", GREEN)], 1380, 540, 80, ep(t, C["11.d"] + 2.0, 0.4))
        regra(c, "a troca mexe nos DOIS lados", 1380, 690, ep(t, C["11.d"] + 3.6, 0.4), 30)
    line(c, 960, 240, 960, 760, "#E6E6E2", acc, 3)


# ======================================================================
# bloco f — substituição
# ======================================================================

def b_substituicao(c, t, C, B):
    head_seq(c, t, C, [("12", "MÉTODO DA SUBSTITUIÇÃO", "PASSO 1: ISOLE UMA LETRA", PURPLE),
                       ("13", "PASSO 2: TROQUE A PEÇA", "COM PARÊNTESES E TUDO", PURPLE)])
    card(c, *CARD_R)
    etiquetas(c, [("c", "nº de carros"), ("m", "nº de motos")], 1380, 240, ep(t, C["12"], 0.4))
    sid = which(t, C, ["12", "13"])
    if sid == "12":
        aa = ep(t, C["12.a"], 0.5)
        if aa > 0:
            text(c, "30 veículos · 100 rodas", 260, 270, 30, "bold", GRAY, aa, align="left")
            sistema(c, [("c + m = 30", BLUE)], [("4c + 2m = 100", PURPLE)], 300, 380, 60, aa, dy=110)
        ab = ep(t, C["12.b"], 0.5)
        if ab > 0:
            rrect(c, 960, 360, 700, 140, 22, mix("#FFFFFF", BLUE, 0.08), ab)
            text(c, "SUBSTITUIÇÃO", 1310, 405, 24, "black", BLUE, ab, tracking=2)
            text(c, "isole uma letra e troque na outra", 1310, 460, 30, "bold", INK2, ab)
        acc = ep(t, C["12.c"], 0.5)
        if acc > 0:
            rrect(c, 300, 600, 900, 140, 24, mix("#FFFFFF", GREEN, 0.12), acc)
            linha(c, [("m = 30 − c", GREEN)], 750, 670, 76, acc)
            pill(c, "da 1ª equação", 1340, 670, GRAY, size=24, a=acc, anchor="center")
        return
    a0 = ep(t, C["13"], 0.4)
    linha(c, [("m = 30 − c", GREEN)], 300, 280, 44, a0, align="left")
    aa = ep(t, C["13.a"], 0.4)
    peca_troca(c, t, C["13.a"] + 0.6, 300, 400, 64, aa)
    rows = [(C["13.c"], [("4c + ", INK), ("60 − 2c", PURPLE), (" = 100", INK)], "distributiva", PURPLE),
            (C["13.c"] + 3.0, [("2c = 40", INK)], "− 60 nos dois lados", PURPLE),
            (C["13.c"] + 4.6, [("c = 20", GREEN)], "÷ 2", PURPLE)]
    passos(c, t, rows, 300, 510, 52, 80, xnota=1200)
    ad = ep(t, C["13.d"], 0.5)
    if ad > 0:
        rrect(c, 1260, 520, 400, 230, 22, mix("#FFFFFF", GREEN, 0.12), ad)
        linha(c, [("m = 30 − 20 = 10", INK)], 1460, 570, 32, ad)
        text(c, "CONFIRA", 1460, 640, 18, "black", GREEN, ad, tracking=2)
        conferido(c, "80 + 20 = 100", 1310, 700, ep(t, C["13.d"] + 1.6, 0.4), True, 30)


# ======================================================================
# bloco g — tudo de um tipo
# ======================================================================

def b_umtipo(c, t, C, B):
    head(c, t, B["start"], "ATALHO", "TUDO DE UM TIPO", GREEN)
    card(c, *CARD_R)
    aa = ep(t, C["14.a"], 0.5)
    # 30 veículos: começam motos; a partir de 14.d, 20 viram carros
    vira = ep(t, C["14.d"], 1.5)
    if aa > 0:
        for k in range(30):
            x = 300 + (k % 15) * 88
            y = 300 + (k // 15) * 110
            car = k < 20 and vira > (k / 20)
            col = BLUE if car else AMBER
            rrect(c, x - 34, y - 26, 68, 52, 12, mix("#FFFFFF", col, 0.2), aa)
            fmid(c, "4" if car else "2", x, y, 28, "black", col, aa)
        text(c, "rodas de cada veículo", W / 2, 460, 22, "bold", GRAY, aa)
        linha(c, [("todas motos: 30 · 2 = ", INK), ("60 rodas", AMBER)], W / 2, 520, 40, ep(t, C["14.a"] + 2.4, 0.4))
    ab = ep(t, C["14.b"], 0.5)
    if ab > 0:
        linha(c, [("100 − 60 = ", INK), ("faltam 40", RED)], W / 2, 590, 40, ab)
    acc = ep(t, C["14.c"], 0.5)
    if acc > 0:
        pill(c, "trocar 1 moto por 1 carro = +2 rodas", W / 2, 660, BLUE, size=30, a=acc, anchor="center")
    ad = ep(t, C["14.d"], 0.5)
    if ad > 0:
        K.atalho(c, 460, 700, 1000, 120, "ATALHO", ["40 ÷ 2 = 20 carros"], ad, 40)


# ======================================================================
# nós fazemos
# ======================================================================

def b_exercicio(c, t, C, B):
    head_seq(c, t, C, [("15", "SUA VEZ", "PAUSE E TENTE", GREEN), ("16", "VAMOS JUNTOS", "SUBSTITUIÇÃO E ATALHO", GREEN)])
    card(c, *CARD_R)
    aa = ep(t, C["15.a"], 0.5)
    if aa > 0:
        rrect(c, 330, 230, 1260, 110, 22, "#FFFFFF", aa, shadow=True)
        text(c, "25 veículos (carros e motos) · 70 rodas · quantos carros?", W / 2, 300, 38, "black", INK, aa)
    pause_timer(c, t, C["15.end"] - 1.9, W / 2, 560)
    if t < C["16"]:
        return
    etiquetas(c, [("c", "nº de carros"), ("m", "nº de motos")], 1380, 400, ep(t, C["16"], 0.4))
    ab = ep(t, C["16.a"], 0.5)
    sistema(c, [("c + m = 25", BLUE)], [("4c + 2m = 70", PURPLE)], 300, 420, 46, ab, dy=80)
    rows = [(C["16.b"], [("4c + ", INK), ("2(25 − c)", AMBER), (" = 70", INK)], "", None),
            (C["16.b"] + 2.6, [("2c = 20  →  ", INK), ("c = 10", GREEN), ("  ·  m = 15", INK)], "", None)]
    passos(c, t, rows, 300, 610, 40, 70)
    acc = ep(t, C["16.c"], 0.5)
    if acc > 0:
        K.atalho(c, 1000, 560, 640, 150, "TUDO DE UM TIPO", ["todas motos: 50 rodas · faltam 20", "20 ÷ 2 = 10 carros"],
                 acc, 26)
    ad = ep(t, C["16.d"], 0.5)
    if ad > 0:
        conferido(c, "40 + 30 = 70 rodas", 1040, 770, ad, True, 32)


# ======================================================================
# recap, erros
# ======================================================================

FRASES = ["Uma equação por informação.",
          "Uma equação conta, a outra soma valores.",
          "Substituiu? Ponha parênteses."]


def b_recap(c, t, C, B):
    sid = which(t, C, ["17", "31"])
    frame(c, t, B["start"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "17" else "PARA FECHAR", PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 300 + k * 180 + d
        badge_num(c, k + 1, 260, y - 16, a, 36, bg=PURPLE)
        para(c, s, 320, y, 58, "black", INK, a, 1360, 66)


ERROS = [("“Pedro tem o dobro de Júlia”  →  2P = J", "o 2 aparece perto do Pedro na frase",
          "teste com números (J = 5, P = 10): o 2 multiplica quem tem MENOS → P = 2J"),
         ("2(30 − c) = 60 − c", "o 2 parece encostado só no 30",
          "o coeficiente multiplica TUDO: 60 − 2c (com o erro, 13,3 carros: não existe)"),
         ("“se Pedro der 6 moedas”  →  P − 6 = J", "a frase só fala do Pedro dando",
          "quem recebe também muda: P − 6 = J + 6"),
         ("achou os carros, mas a pergunta era das motos", "o número que você achou está nas alternativas",
          "releia a pergunta e olhe a etiqueta antes de marcar")]


def b_erros(c, t, C, B):
    K.erro_cards(c, t, C, ["18", "19", "20", "21"], ERROS)


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


ALTS1 = [("A", "120", "400 − 280", RED),
         ("B", "160", "são as inteiras", RED),
         ("C", "cerca de 187", "11 200 ÷ 60: sem sentido", RED),
         ("D", "240", "", GREEN),
         ("E", "280", "todos pagando inteira", RED)]


def b_q1(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 1 · EU FAÇO", "INTEIRAS E MEIAS", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["22.a"], 0.4) * (1 - ep(t, C["23"], 0.4))
    _enunciado(c, [("Um teatro vendeu 400 ingressos para uma sessão, alguns pelo preço inteiro de R$ 40,00 e os demais pela "
                    "meia-entrada de R$ 20,00. A arrecadação total foi de R$ 11.200,00. O número de meias-entradas "
                    "vendidas foi", INK)], a0, 250, 30)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0, align="left")
    cues_in = {L: C[f"22.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"24.x{L.lower()}"] for L in "ABCE"}
    K.alternativas(c, t, C, ALTS1, 1000, 260, 680, 34, C["23.ok"], "D", cues_in, cues_x, gap=34)
    if t >= C["23"]:
        ap = ep(t, C["23"], 0.4)
        _painel(c, ap)
        etiqueta(c, "i", "inteiras (ingressos)", 200, 275, ap)
        etiqueta(c, "m", "meias (ingressos)", 560, 275, ap)
        rows = [(C["23.a"], [("i + m = 400", BLUE)], "", None),
                (C["23.a"] + 3.0, [("40i + 20m = 11 200", PURPLE)], "", None),
                (C["23.b"], [("40(400 − m)", AMBER), (" = 16 000 − 40m", INK)], "", None),
                (C["23.c"], [("16 000 − 20m = 11 200", INK)], "", None),
                (C["23.c"] + 4.0, [("20m = 4 800  →  ", INK), ("m = 240", GREEN)], "", None)]
        passos(c, t, rows, 210, 370, 34, 70)
        ad = ep(t, C["23.d"], 0.4)
        if ad > 0:
            rrect(c, 200, 720, 700, 90, 18, mix("#FFFFFF", GREEN, 0.10), ad)
            conferido(c, "6 400 + 4 800 = 11 200", 240, 778, ad, True, 30)


ALTS5 = [("A", "6", "só as transferidas", RED),
         ("B", "12", "é a Júlia", RED),
         ("C", "18", "depois da troca", RED),
         ("D", "24", "", GREEN),
         ("E", "36", "o total dos dois", RED)]


def b_q5(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 5 · NÓS FAZEMOS", "TROCA DE MOEDAS", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["25.a"], 0.4) * (1 - ep(t, C["26"], 0.4))
    yend = _enunciado(c, [("Pedro tem o dobro do número de moedas de Júlia. Se Pedro der 6 de suas moedas a Júlia, os dois "
                           "ficarão com a mesma quantidade. Quantas moedas Pedro tem?", INK)], a0, 250, 30)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0, align="left")
    cues_in = {L: C[f"25.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"27.x{L.lower()}"] for L in "ABCE"}
    K.alternativas(c, t, C, ALTS5, 1000, 260, 680, 34, C["26.ok"], "D", cues_in, cues_x, gap=34)
    pause_timer(c, t, C["25.end"] - 1.9, 540, yend + 120)
    if t >= C["26"]:
        ap = ep(t, C["26"], 0.4)
        _painel(c, ap)
        etiqueta(c, "P", "moedas de Pedro", 200, 275, ap)
        etiqueta(c, "J", "moedas de Júlia", 560, 275, ap)
        rows = [(C["26.a"], [("P = 2J", BLUE)], "", None),
                (C["26.a"] + 2.4, [("P − 6", RED), (" = ", INK), ("J + 6", GREEN)], "", None),
                (C["26.b"], [("2J − 6 = J + 6", INK)], "", None),
                (C["26.b"] + 3.4, [("J = 12", INK)], "", None),
                (C["26.c"], [("P = 24", GREEN)], "", None)]
        passos(c, t, rows, 210, 370, 40, 72)
        ad = ep(t, C["26.d"], 0.4)
        if ad > 0:
            rrect(c, 200, 730, 700, 80, 18, mix("#FFFFFF", GREEN, 0.10), ad)
            conferido(c, "24 − 6 = 18 = 12 + 6", 240, 782, ad, True, 30)


ALTS9 = [("A", "km 60", "o que o carro ANDOU", RED),
         ("B", "km 80", "", GREEN),
         ("C", "km 110", "ponto médio", RED),
         ("D", "km 140", "trocou as velocidades", RED),
         ("E", "km 180", "distância inicial", RED)]


def b_q9(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 9 · VOCÊ FAZ", "ENCONTRO NA ESTRADA", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["28.a"], 0.4) * (1 - ep(t, C["29"], 0.4))
    yend = _enunciado(c, [("Às 8 h, um carro passa pelo km 20 de uma rodovia, a 60 km/h, no sentido crescente da "
                           "quilometragem. No mesmo instante, um ônibus passa pelo km 200, a 120 km/h, no sentido contrário. "
                           "Mantidas as velocidades, os dois se cruzarão no", INK)], a0, 250, 28)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0, align="left")
    cues_in = {L: C[f"28.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"30.x{L.lower()}"] for L in "ACDE"}
    K.alternativas(c, t, C, ALTS9, 1000, 260, 680, 34, C["29.ok"], "B", cues_in, cues_x, gap=34)
    ah = ep(t, C["28.h"], 0.4) * (1 - ep(t, C["29"], 0.4))
    if ah > 0:
        pill(c, "posição = onde começou ± o que andou", 540, yend + 30, GREEN, size=22, a=ah, anchor="center")
    pause_timer(c, t, C["28.end"] - 1.9, 540, yend + 150)
    if t >= C["29"]:
        ap = ep(t, C["29"], 0.4)
        _painel(c, ap)
        etiqueta(c, "t", "horas depois das 8 h", 200, 275, ap)
        rows = [(C["29.a"], [("carro: ", GRAY), ("20 + 60t", BLUE)], "", None),
                (C["29.b"], [("ônibus: ", GRAY), ("200 − 120t", AMBER)], "", None),
                (C["29.c"], [("20 + 60t = 200 − 120t", INK)], "", None),
                (C["29.c"] + 3.6, [("180t = 180  →  ", INK), ("t = 1 h", GREEN)], "", None),
                (C["29.d"], [("20 + 60 = ", INK), ("km 80", GREEN)], "", None)]
        passos(c, t, rows, 210, 360, 34, 62)
        tt = ep(t, C["29.c"] + 3.6, 2.0)
        estrada(c, 250, 860, 770, ep(t, C["29.a"], 0.4), tt, tt, 80 if tt > 0.95 else None)


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "O MÉTODO DA ADIÇÃO", PURPLE)
    aa = ep(t, C["32.a"], 0.5)
    if aa > 0:
        rrect(c, 360, 260, 1200, 230, 26, "#FFFFFF", aa, shadow=True)
        linha(c, [("2 sanduíches + 1 suco = ", INK), ("R$ 31,00", BLUE)], W / 2, 340, 48, aa)
        linha(c, [("1 sanduíche + 2 sucos = ", INK), ("R$ 26,00", BLUE)], W / 2, 430, 48, ep(t, C["32.a"] + 2.2, 0.4))
    ab = ep(t, C["32.b"], 0.5)
    if ab > 0:
        selo(c, W / 2, 580, ab, "UM DE CADA = ?", AMBER, -3, 44)
    acc = ep(t, C["32.c"], 0.5)
    if acc > 0:
        text(c, "em UMA linha, sem achar o preço de nenhum", W / 2, 690, 36, "black", GREEN, acc)
    pill(c, "ep. 2 · o método da adição", W / 2, 790, PURPLE, size=32, a=ep(t, C["32.d"], 0.5), anchor="center")


def b_cta(c, t, C, B):
    cta(c, t, C["33.like"], C["33.sub"], C["33.bell"], C["33.com"], C["33.bye"],
        "Qual desses 4 erros você já cometeu?", canal="no Estudativo", anki=C["33.anki"])


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, sitio=b_sitio, definicao=b_definicao, testar=b_testar,
              molde=b_molde, comparacao=b_comparacao, substituicao=b_substituicao, umtipo=b_umtipo,
              exercicio=b_exercicio, recap=b_recap, erros=b_erros, q1=b_q1, q5=b_q5, q9=b_q9, ponte=b_ponte, cta=b_cta)
