"""Visual — Comparação de Propostas e Tomada de Decisão, Episódio 2: planos com parte fixa e variável, o ponto de
equilíbrio (tema claro).
Peças comuns da série em ../../comum.py (reexporta o 019/comum.py: alternativas, erro_cards, atalho, mdraw...).
Peças deste episódio: grafico() (as duas retas A e B, que se cruzam em 100 min / R$ 100,00, com as regiões "A vence" em
azul e "B vence" em verde), cofrinho() (a "dívida" de R$ 30,00 do plano B sendo paga de R$ 0,30 em R$ 0,30 a cada
minuto até zerar no minuto 100), plano_card() (o folheto de um plano: fixo + preço por unidade), tabela() (as
propostas organizadas: fixo, por unidade, custo), passos() (as linhas de uma conta, uma por vez), linha(), caixa().
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
_s = importlib.util.spec_from_file_location("comum033", _p)
K = importlib.util.module_from_spec(_s); _s.loader.exec_module(K)
K.usar_tempos(Path(__file__).resolve().parents[1] / "audio" / "tempos.json")
motor.set_theme("claro")
frame, head_seq, which, para, regra, selo, pause_timer = (K.frame, K.head_seq, K.which, K.para, K.regra, K.selo,
                                                         K.pause_timer)

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_propostas_ep2_ponto_equilibrio.mp4"
CARD_R = K.CARD_R
COL_A, COL_B = BLUE, GREEN


# ======================================================================
# peças do episódio
# ======================================================================

def linha(c, partes, cx, cy, size, a, peso="black", align="center"):
    """texto numa linha, com cor por trecho: partes = [(texto, cor)] (mantém espaços)"""
    if a <= 0:
        return 0
    ws = [text_w(s_, peso, size) for s_, _ in partes]
    x = cx - sum(ws) / 2 if align == "center" else cx
    for (s_, col), w_ in zip(partes, ws):
        text(c, s_, x, cy + size * 0.36, size, peso, col or INK, a, align="left")
        x += w_
    return sum(ws)


def caixa(c, cx, cy, tit, val, col, a, w=360, sub=None, h=140):
    """cartão de valor: título pequeno em cima, valor grande embaixo"""
    if a <= 0:
        return
    rrect(c, cx - w / 2, cy - h / 2, w, h, 22, "#FFFFFF", a, shadow=True)
    rrect(c, cx - w / 2, cy - h / 2, w, 46, 22, col, a * 0.16)
    text(c, tit, cx, cy - h / 2 + 33, 24, "black", col, a)
    size = 44
    while text_w(val, "black", size) > w - 30:
        size -= 2
    text_mid(c, val, cx, cy + 22, size, "black", INK, a)
    if sub:
        text(c, sub, cx, cy + h / 2 + 34, 24, "bold", GRAY, a)


def plano_card(c, cx, cy, nome, fixo, unit, col, a, w=520, h=300, sel_fixo=0.0, sel_unit=0.0):
    """o folheto de um plano: nome, parte fixa e preço por unidade (com realce opcional em cada parte)"""
    if a <= 0:
        return
    rrect(c, cx - w / 2, cy - h / 2, w, h, 26, "#FFFFFF", a, shadow=True, stroke=4, stroke_color=col)
    rrect(c, cx - w / 2, cy - h / 2, w, 70, 26, col, a * 0.9)
    text_mid(c, nome, cx, cy - h / 2 + 35, 36, "black", "#FFFFFF", a)
    for k, (val, rot, sel, cc) in enumerate(((fixo, "por mês (fixo)", sel_fixo, BLUE),
                                            (unit, "por minuto", sel_unit, PURPLE))):
        y = cy - h / 2 + 130 + k * 92
        if sel > 0:
            rrect(c, cx - w / 2 + 20, y - 42, w - 40, 80, 16, cc, a * sel * 0.14)
        text_mid(c, val, cx - w / 2 + 40, y, 46, "black", INK, a, align="left")
        text_mid(c, rot, cx + w / 2 - 36, y, 26, "bold", GRAY, a, align="right")


def frac(c, num, den, cx, cy, size, a, col_n=None, col_d=None, peso="black"):
    """fração empilhada com texto livre (aceita espaços): numerador, barra e denominador centrados em cx; devolve a largura"""
    if a <= 0:
        return 0
    w = max(text_w(num, peso, size), text_w(den, peso, size)) + 24
    text_mid(c, num, cx, cy - size * 0.72, size, peso, col_n or INK, a)
    line(c, cx - w / 2, cy, cx + w / 2, cy, INK, a, max(3, size * 0.07))
    text_mid(c, den, cx, cy + size * 0.78, size, peso, col_d or INK, a)
    return w


def passos(c, linhas, cx, y0, size, t, a=1.0, dy=None, align="center"):
    """linhas de conta, cada uma com o seu instante: linhas = [(t0, partes)]"""
    dy = dy or size * 1.55
    for k, (t0, partes) in enumerate(linhas):
        aa = a * ep(t, t0, 0.45)
        if aa > 0:
            linha(c, partes, cx, y0 + k * dy, size, aa, align=align)


def tabela(c, x, y, cab, rows, a, colw, rh=74, size=32, cores=None):
    """tabela das propostas: cab = títulos; rows = listas de células; cores = cor de cada linha (barra lateral)"""
    if a <= 0:
        return
    w = sum(colw)
    rrect(c, x, y, w, rh * (len(rows) + 1) + 10, 20, "#FFFFFF", a, shadow=True)
    rrect(c, x, y, w, rh, 20, PURPLE, a * 0.12)
    xx = x
    for s_, cw in zip(cab, colw):
        text_mid(c, s_, xx + cw / 2, y + rh / 2, 24, "black", PURPLE, a)
        xx += cw
    for i, row in enumerate(rows):
        yy = y + rh * (i + 1) + rh / 2
        if cores and cores[i]:
            rrect(c, x + 8, yy - rh / 2 + 10, 10, rh - 20, 5, cores[i], a)
        xx = x
        for j, (s_, cw) in enumerate(zip(row, colw)):
            sz = size
            while text_w(s_, "black", sz) > cw - 20 and sz > 18:
                sz -= 2
            text_mid(c, s_, xx + cw / 2, yy, sz, "black", (cores[i] if (cores and j == 0 and cores[i]) else INK), a)
            xx += cw
        if i < len(rows) - 1:
            line(c, x + 20, yy + rh / 2, x + w - 20, yy + rh / 2, LIGHT, a, 2)


# --- o gráfico das duas retas -----------------------------------------
GX, GY, GW, GH = 300, 230, 900, 520      # área do gráfico (origem em GX, GY + GH)
XMAX, YMAX = 200, 160


def _px(m):
    return GX + GW * m / XMAX


def _py(v):
    return GY + GH - GH * v / YMAX


def grafico(c, a, ua=1.0, ub=1.0, cruz=0.0, regioes=0.0, marcas=(), gx=None):
    """eixos (minutos × R$), a reta A (50 + 0,5x) e a reta B (80 + 0,2x) desenhadas até a fração ua/ub;
    cruz = destaque do cruzamento (100 min, R$ 100); regioes = as faixas "A vence" e "B vence";
    marcas = [(minutos, alfa)] com as linhas tracejadas de teste e os custos de cada plano."""
    if a <= 0:
        return
    rrect(c, GX - 120, GY - 60, GW + 220, GH + 150, 24, "#FFFFFF", a, shadow=True)
    if regioes > 0:
        rrect(c, _px(0), GY, _px(100) - _px(0), GH, 0, COL_A, a * regioes * 0.10)
        rrect(c, _px(100), GY, _px(200) - _px(100), GH, 0, COL_B, a * regioes * 0.12)
        text(c, "A VENCE", (_px(0) + _px(100)) / 2, GY + 50, 34, "black", COL_A, a * regioes)
        text(c, "B VENCE", (_px(100) + _px(200)) / 2, GY + 50, 34, "black", COL_B, a * regioes)
    line(c, GX, GY + GH, GX + GW + 30, GY + GH, INK2, a, 4)
    line(c, GX, GY + GH, GX, GY - 20, INK2, a, 4)
    for m in (0, 50, 100, 150, 200):
        line(c, _px(m), GY + GH - 8, _px(m), GY + GH + 8, INK2, a, 3)
        text(c, str(m), _px(m), GY + GH + 40, 24, "bold", GRAY, a)
    text(c, "minutos", GX + GW, GY + GH + 78, 24, "black", GRAY, a, align="right")
    for v in (0, 50, 100, 150):
        line(c, GX - 8, _py(v), GX + 8, _py(v), INK2, a, 3)
        text(c, f"R$ {v}", GX - 18, _py(v) + 9, 22, "bold", GRAY, a, align="right")
    for f, u, col, nome in ((lambda m: 50 + 0.5 * m, ua, COL_A, "A"), (lambda m: 80 + 0.2 * m, ub, COL_B, "B")):
        if u <= 0:
            continue
        m1 = XMAX * clamp(u)
        line(c, _px(0), _py(f(0)), _px(m1), _py(f(m1)), col, a, 7)
        c.drawCircle(_px(0), _py(f(0)), 9, paint(col, a))
        if u >= 0.999:
            pill(c, f"plano {nome}", _px(200) + 14, _py(f(200)), col, size=24, a=a, anchor="left", bounds=(0, 1920))
    for m, am in marcas:
        if am <= 0:
            continue
        va, vb = 50 + 0.5 * m, 80 + 0.2 * m
        line(c, _px(m), GY + GH, _px(m), _py(max(va, vb)) - 10, INK2, a * am, 3, dash=(10, 8))
        for v, col in ((va, COL_A), (vb, COL_B)):
            c.drawCircle(_px(m), _py(v), 11, paint(col, a * am))
            pill(c, f"R$ {v:g}", _px(m) + (20 if v == min(va, vb) else -20), _py(v), col, size=22, a=a * am,
                 anchor="left" if v == min(va, vb) else "right", bounds=(0, 1920))
    if cruz > 0:
        x, y = _px(100), _py(100)
        line(c, x, GY + GH, x, y, PURPLE, a * cruz, 3, dash=(10, 8))
        line(c, GX, y, x, y, PURPLE, a * cruz, 3, dash=(10, 8))
        c.drawCircle(x, y, 22 * (0.8 + 0.2 * ease_back(clamp(cruz))), paint(PURPLE, a * cruz * 0.25))
        c.drawCircle(x, y, 12, paint(PURPLE, a * cruz))
        pill(c, "100 min · R$ 100", x, y - 52, PURPLE, size=26, a=a * cruz, anchor="center", bounds=(0, 1920))


# --- o cofrinho da dívida ---------------------------------------------
def porco(c, cx, cy, s, a, col=AMBER):
    """um cofrinho estilizado (porquinho) de escala s"""
    if a <= 0:
        return
    body = mix("#FFFFFF", col, 0.35)
    c.drawOval(skia.Rect.MakeXYWH(cx - 150 * s, cy - 100 * s, 300 * s, 200 * s), paint(body, a))
    c.drawOval(skia.Rect.MakeXYWH(cx - 150 * s, cy - 100 * s, 300 * s, 200 * s), paint(col, a, stroke=6 * s))
    c.drawCircle(cx + 150 * s, cy + 5 * s, 34 * s, paint(body, a))
    c.drawCircle(cx + 150 * s, cy + 5 * s, 34 * s, paint(col, a, stroke=6 * s))
    for dx in (-10, 10):
        c.drawCircle(cx + (150 + dx) * s, cy + 5 * s, 6 * s, paint(col, a))
    for lx in (-90, -30, 40, 100):
        rrect(c, cx + lx * s - 18 * s, cy + 80 * s, 36 * s, 50 * s, 8 * s, col, a)
    path = skia.Path()
    path.moveTo(cx + 70 * s, cy - 90 * s); path.lineTo(cx + 105 * s, cy - 135 * s); path.lineTo(cx + 115 * s, cy - 80 * s)
    path.close()
    c.drawPath(path, paint(body, a)); c.drawPath(path, paint(col, a, stroke=5 * s))
    c.drawCircle(cx + 95 * s, cy - 30 * s, 9 * s, paint(INK, a))
    rrect(c, cx - 50 * s, cy - 96 * s, 100 * s, 14 * s, 7 * s, INK, a)
    c.drawArc(skia.Rect.MakeXYWH(cx - 205 * s, cy - 40 * s, 60 * s, 60 * s), 90, 220, False,
              paint(col, a, stroke=6 * s, cap_round=True))


def cofrinho(c, cx, cy, t, t0, a, dur=6.0):
    """a dívida de R$ 30,00 do plano B sendo paga de R$ 0,30 em R$ 0,30, minuto a minuto, até zerar no minuto 100"""
    if a <= 0:
        return
    u = clamp((t - t0) / dur) if t >= t0 else 0.0
    m = int(round(100 * ease_io(u)))
    divida = 30 - 0.3 * m
    porco(c, cx, cy, 1.0, a)
    text_mid(c, "DÍVIDA DO B", cx - 230, cy - 120, 28, "black", AMBER, a)
    cor = GREEN if m >= 100 else RED
    text_mid(c, f"R$ {divida:.2f}".replace(".", ","), cx - 10, cy + 5, 58, "black", cor, a)
    bw = 420
    rrect(c, cx - bw / 2, cy + 175, bw, 26, 13, LIGHT, a)
    rrect(c, cx - bw / 2, cy + 175, bw * (1 - m / 100), 26, 13, RED, a)
    text_mid(c, f"minuto {m}", cx, cy + 245, 36, "black", INK, a)
    if 0 < u < 1:
        k = (t - t0) * 6 % 1
        yy = cy - 210 + 110 * k
        c.drawCircle(cx, yy, 20, paint("#F4C542", a * (1 - k)))
        text_mid(c, "0,30", cx, yy, 16, "black", INK, a * (1 - k))
    if m >= 100:
        selo(c, cx, cy - 60, a * ep(t, t0 + dur, 0.4), "ZEROU!", GREEN, -8, 40)


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "QUAL PLANO É MELHOR?", BLUE)
    aa = ep(t, C["01.a"], 0.5)
    plano_card(c, 560, 420, "PLANO R$ 50", "R$ 50,00", "+ R$ 0,50", COL_A, aa, w=500, h=280)
    plano_card(c, 1360, 420, "PLANO R$ 80", "R$ 80,00", "+ R$ 0,20", COL_B, ep(t, C["01.a"] + 1.2, 0.5), w=500, h=280)
    ab = ep(t, C["01.b"], 0.5)
    if ab > 0:
        pill(c, "60 min → vence este", 560, 640, COL_A, size=32, a=ab, anchor="center", bounds=(0, 1920))
        check_icon(c, 560, 715, 30, ab, COL_A)
    acc = ep(t, C["01.c"], 0.5)
    if acc > 0:
        pill(c, "150 min → vence este", 1360, 640, COL_B, size=32, a=acc, anchor="center", bounds=(0, 1920))
        check_icon(c, 1360, 715, 30, acc, COL_B)
    ad = ep(t, C["01.d"], 0.5)
    if ad > 0:
        rrect(c, 760, 760, 400, 90, 22, mix("#FFFFFF", PURPLE, 0.12), ad, shadow=True)
        text_mid(c, "em que minuto muda?", 960, 805, 34, "black", PURPLE, ad)


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "AO FINAL DESTA AULA", "VOCÊ VAI CONSEGUIR", GREEN)
    itens = [("02.a", "achar o ponto de equilíbrio entre dois planos", PURPLE),
             ("02.b", "dizer qual vale em cada faixa de uso", GREEN),
             ("02.c", "não errar o \"a partir de\"", AMBER)]
    for k, (cue, s, col) in enumerate(itens):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        y = 260 + k * 190 + d
        rrect(c, 260, y, 1400, 150, 24, mix("#FFFFFF", col, 0.08), a, shadow=True)
        check_icon(c, 340, y + 75, 30, a, col)
        text_mid(c, s, 400, y + 75, 44, "black", INK, a, align="left")


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "2 LEMBRETES", "RÁPIDOS", GREEN)
    cards = [("03.a", "PREÇO × QUANTIDADE", ["R$ 0,50 por minuto", "× 60 minutos", "= R$ 30,00"]),
             ("03.b", "ISOLAR O x", ["o que faço de um lado", "faço do outro", "x + 5 = 8 → x = 8 − 5 = 3"])]
    for k, (cue, tag, ls) in enumerate(cards):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        x = 250 + k * 740
        rrect(c, x, 270 + d, 680, 460, 24, "#FFFFFF", a, shadow=True)
        pill(c, tag, x + 340, 330 + d, GREEN, size=26, a=a, anchor="center", bounds=(0, 1920))
        for j, s in enumerate(ls):
            col = PURPLE if j == 2 else INK2
            text_mid(c, s, x + 340, 460 + j * 90 + d, 40 if j < 2 else 42, "black", col, a)


def b_concreto(c, t, C, B):
    head_seq(c, t, C, [("04", "O FOLHETO DA OPERADORA", "FIXO + POR MINUTO", BLUE),
                       ("05", "A MESMA BRIGA", "EM TODO LUGAR", BLUE)])
    card(c, *CARD_R)
    sid = which(t, C, ["04", "05"])
    if sid == "04":
        aa = ep(t, C["04.a"], 0.5)
        sf = ep(t, C["04.b"], 0.5)
        su = ep(t, C["04.c"], 0.5)
        plano_card(c, 520, 380, "PLANO A", "R$ 50,00", "+ R$ 0,50", COL_A, aa, sel_fixo=sf, sel_unit=su)
        plano_card(c, 1100, 380, "PLANO B", "R$ 80,00", "+ R$ 0,20", COL_B, ep(t, C["04.a"] + 2.6, 0.5),
                   sel_fixo=sf, sel_unit=su)
        defs = [("04.b", "PARTE FIXA", "paga mesmo sem usar nada", BLUE),
                ("04.c", "PARTE VARIÁVEL", "preço por unidade × consumo", PURPLE)]
        for k, (cue, nome, sig, col) in enumerate(defs):
            a, d = rise(t, C[cue])
            if a <= 0:
                continue
            y = 590 + k * 120 + d
            rrect(c, 280, y, 1100, 100, 20, mix("#FFFFFF", col, 0.08), a)
            text_mid(c, nome, 320, y + 50, 36, "black", col, a, align="left")
            text_mid(c, sig, 760, y + 50, 32, "bold", INK2, a, align="left")
        if su > 0:
            pill(c, "consumo = quanto você usou", 1570, 760, BLUE, size=24, a=ep(t, C["04.c"] + 3.0, 0.4),
                 anchor="center", bounds=(0, 1920))
        return
    exs = [("05.a", "LOCADORA", "diária cara + km livre", "diária barata + R$ por km"),
           ("05.b", "ESTACIONAMENTO", "mensalidade", "diária")]
    for k, (cue, nome, alto, baixo) in enumerate(exs):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        y = 240 + k * 230 + d
        rrect(c, 230, y, 1460, 190, 24, "#FFFFFF", a, shadow=True)
        text_mid(c, nome, 290, y + 95, 40, "black", BLUE, a, align="left")
        rrect(c, 760, y + 30, 420, 130, 18, mix("#FFFFFF", COL_B, 0.10), a)
        text_mid(c, alto, 970, y + 95, 30, "black", INK, a)
        text_mid(c, "×", 1215, y + 95, 44, "black", GRAY, a)
        rrect(c, 1250, y + 30, 420, 130, 18, mix("#FFFFFF", COL_A, 0.10), a)
        text_mid(c, baixo, 1460, y + 95, 30, "black", INK, a)
    acc = ep(t, C["05.c"], 0.5)
    if acc > 0:
        regra(c, "fixo baixo  ×  preço por unidade baixo", W / 2, 760, acc, 38, AMBER)


# ======================================================================
# bloco a — a fórmula do custo
# ======================================================================

def b_formula(c, t, C, B):
    head(c, t, B["start"], "A FÓRMULA DO CUSTO", "FIXO + POR UNIDADE × CONSUMO", PURPLE)
    card(c, *CARD_R)
    aa = ep(t, C["06.a"], 0.5)
    if aa > 0:
        rrect(c, 260, 220, 1400, 140, 24, mix("#FFFFFF", PURPLE, 0.10), aa, shadow=True)
        linha(c, [("custo = ", INK), ("parte fixa", BLUE), (" + ", INK), ("preço por unidade", PURPLE),
                  (" · x", INK)], W / 2, 290, 50, aa)
        pill(c, "x = consumo", W / 2, 400, BLUE, size=28, a=ep(t, C["06.a"] + 3.4, 0.4), anchor="center",
             bounds=(0, 1920))
    ab = ep(t, C["06.b"], 0.5)
    if ab > 0:
        rrect(c, 300, 470, 600, 120, 22, mix("#FFFFFF", COL_A, 0.10), ab)
        linha(c, [("A = ", COL_A), ("50 + 0,5x", INK)], 600, 530, 52, ab)
    acc = ep(t, C["06.c"], 0.5)
    if acc > 0:
        rrect(c, 1020, 470, 600, 120, 22, mix("#FFFFFF", COL_B, 0.10), acc)
        linha(c, [("B = ", COL_B), ("80 + 0,2x", INK)], 1320, 530, 52, acc)
    ad = ep(t, C["06.d"], 0.5)
    if ad > 0:
        linha(c, [("60 min no A: ", INK2), ("50 + 0,5 · 60 = 50 + 30 = ", INK), ("R$ 80", COL_A)], W / 2, 690, 42, ad)


# ======================================================================
# bloco b — o empate (igualar e isolar) e o gráfico
# ======================================================================

def b_empate(c, t, C, B):
    head_seq(c, t, C, [("07", "O PONTO DE EQUILÍBRIO", "IGUALE OS CUSTOS", PURPLE),
                       ("08", "ISOLE O x", "PASSO A PASSO", PURPLE)])
    card(c, *CARD_R)
    aa = ep(t, C["07.a"], 0.5)
    if aa > 0:
        rrect(c, 230, 200, 1460, 110, 22, mix("#FFFFFF", BLUE, 0.08), aa)
        linha(c, [("PONTO DE EQUILÍBRIO", BLUE), (" (empate): o consumo em que os dois custam o mesmo", INK2)],
              W / 2, 255, 32, aa)
    ls = [(C["07.b"], [("50 + 0,5x", COL_A), (" = ", INK), ("80 + 0,2x", COL_B)]),
          (C["07.c"], [("50 + 0,5x − 0,2x = 80", INK), ("   (− 0,2x dos dois lados)", GRAY)]),
          (C["07.c"] + 3.2, [("50 + 0,3x = 80", INK)]),
          (C["08.a"], [("0,3x = 80 − 50 = ", INK), ("30", PURPLE), ("   (− 50 dos dois lados)", GRAY)]),
          (C["08.b"], [("x = 30 ÷ 0,3 = ", INK), ("100 minutos", PURPLE), ("   (÷ 0,3 dos dois lados)", GRAY)])]
    passos(c, ls, W / 2, 350, 42, t, dy=72)
    acc = ep(t, C["08.c"], 0.5)
    if acc > 0:
        caixa(c, 700, 785, "PLANO A", "50 + 50 = R$ 100", COL_A, acc, 460, h=110)
        caixa(c, 1220, 785, "PLANO B", "80 + 20 = R$ 100", COL_B, acc, 460, h=110)


def b_grafico(c, t, C, B):
    head(c, t, B["start"], "O CRUZAMENTO DAS RETAS", "ANTES E DEPOIS DO EMPATE", PURPLE)
    a0 = ep(t, C["09.t"], 0.4)
    ua = ep(t, C["09.a"] + 0.3, 2.0)
    ub = ep(t, C["09.a"] + 3.0, 2.0)
    cruz = ep(t, C["09.b"], 0.6)
    reg = ep(t, C["09.c"], 0.6)
    grafico(c, a0, ua, ub, cruz, reg)
    for cue, s, col, y in (("09.c", "antes: vence o FIXO BAIXO", COL_A, 330),
                           ("09.d", "depois: vence o PREÇO POR MINUTO BAIXO", COL_B, 520)):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        rrect(c, 1420, y + d, 380, 150, 20, mix("#FFFFFF", col, 0.12), a, shadow=True)
        para(c, s, 1445, y + 60 + d, 30, "black", col, a, 340, 38)


# ======================================================================
# bloco c — o teste dos dois lados
# ======================================================================

def b_teste(c, t, C, B):
    head(c, t, B["start"], "O TESTE", "UM VALOR DE CADA LADO", GREEN)
    grafico(c, 1.0, 1.0, 1.0, 0.0, 0.6,
            marcas=[(60, ep(t, C["10.a"], 0.5)), (150, ep(t, C["10.b"], 0.5))])
    for cue, s1, s2, col, y in (("10.a", "60 min", "A 80 × B 92", COL_A, 260),
                                ("10.b", "150 min", "A 125 × B 110", COL_B, 450)):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        rrect(c, 1420, y + d, 380, 160, 20, "#FFFFFF", a, shadow=True)
        text(c, s1, 1610, y + 55 + d, 34, "black", INK2, a)
        text(c, s2, 1610, y + 105 + d, 32, "black", INK, a)
        pill(c, "A melhor" if col == COL_A else "B melhor", 1610, y + 150 + d, col, size=22, a=a, anchor="center",
             bounds=(0, 1920))
    acc = ep(t, C["10.c"], 0.5)
    if acc > 0:
        K.atalho(c, 1400, 660, 420, 180, "REGRA DE OURO", ["teste um valor", "ACIMA do empate"], acc, 30)


# ======================================================================
# bloco d — o cofrinho e o atalho
# ======================================================================

def b_cofrinho(c, t, C, B):
    head_seq(c, t, C, [("11", "A DÍVIDA DO PLANO B", "PAGA DE R$ 0,30 EM R$ 0,30", AMBER),
                       ("12", "ATALHO", "DIFERENÇA ÷ DIFERENÇA", GREEN)])
    card(c, *CARD_R)
    sid = which(t, C, ["11", "12"])
    if sid == "11":
        aa = ep(t, C["11.a"], 0.5)
        if aa > 0:
            linha(c, [("fixo do B − fixo do A = 80 − 50 = ", INK), ("R$ 30 de dívida", AMBER)], 960, 230, 38, aa)
        cofrinho(c, 620, 530, t, C["11.c"], aa, dur=5.0)
        ab = ep(t, C["11.b"], 0.5)
        if ab > 0:
            rrect(c, 1060, 380, 600, 240, 22, mix("#FFFFFF", GREEN, 0.10), ab, shadow=True)
            text(c, "a cada minuto, o B cobra", 1360, 450, 32, "bold", INK2, ab)
            linha(c, [("0,50 − 0,20 = ", INK), ("R$ 0,30", GREEN)], 1360, 520, 46, ab)
            text(c, "a menos que o A", 1360, 590, 32, "bold", INK2, ab)
        acc = ep(t, C["11.c"] + 5.2, 0.5)
        if acc > 0:
            pill(c, "30 ÷ 0,30 = 100 minutos", 1360, 720, PURPLE, size=34, a=acc, anchor="center", bounds=(0, 1920))
        return
    aa = ep(t, C["12.a"], 0.5)
    if aa > 0:
        K.atalho(c, 260, 210, 1400, 260, "ATALHO · PONTO DE EQUILÍBRIO", [""], aa, 40)
        text_mid(c, "equilíbrio =", 640, 365, 46, "black", INK, aa)
        frac(c, "diferença dos fixos", "diferença dos preços por unidade", 1100, 365, 40, aa, BLUE, PURPLE)
    ab = ep(t, C["12.b"], 0.5)
    if ab > 0:
        frac(c, "80 − 50", "0,50 − 0,20", 620, 590, 50, ab, BLUE, PURPLE)
        text_mid(c, "=", 820, 590, 56, "black", INK, ab)
        frac(c, "30", "0,3", 940, 590, 56, ab, BLUE, PURPLE)
        text_mid(c, "= 100 minutos", 1260, 590, 56, "black", GREEN, ab)
    acc = ep(t, C["12.c"], 0.5)
    if acc > 0:
        rrect(c, 560, 700, 800, 110, 22, mix("#FFFFFF", GREEN, 0.10), acc)
        linha(c, [("30 ÷ 0,3 = ", INK), ("300 ÷ 3", GREEN), (" = 100", INK)], W / 2, 755, 44, acc)


# ======================================================================
# bloco e — o "a partir de"
# ======================================================================

def b_apartir(c, t, C, B):
    head_seq(c, t, C, [("13", "NO EMPATE, NINGUÉM GANHA", "\"MAIS BARATO\" COMEÇA DEPOIS", AMBER),
                       ("14", "VARIÁVEL INTEIRA", "DIAS, UNIDADES, VIAGENS", AMBER)])
    card(c, *CARD_R)
    sid = which(t, C, ["13", "14"])
    if sid == "13":
        y = 520
        x0, x1 = 300, 1620
        aa = ep(t, C["13.a"], 0.5)
        if aa > 0:
            line(c, x0, y, x1, y, INK2, aa, 6)
            xm = (x0 + x1) / 2
            for k, m in enumerate(range(96, 105)):
                x = xm + (m - 100) * 140
                line(c, x, y - 16, x, y + 16, INK2, aa, 3)
                text(c, str(m), x, y + 56, 28, "black", PURPLE if m == 100 else GRAY, aa)
            c.drawCircle(xm, y, 18, paint(PURPLE, aa))
            pill(c, "EMPATE · R$ 100 = R$ 100", xm, y - 90, PURPLE, size=30, a=aa, anchor="center", bounds=(0, 1920))
            text(c, "ninguém ganha", xm, y - 160, 30, "black", AMBER, aa)
        ab = ep(t, C["13.b"], 0.6)
        if ab > 0:
            xm = (x0 + x1) / 2
            rrect(c, xm + 30, y - 22, (x1 - xm - 30) * ab, 44, 22, COL_B, 0.85)
            text(c, "B mais barato →", xm + 380, y + 140, 38, "black", COL_B, ab)
            text(c, "acima de 100 minutos", xm + 380, y + 190, 30, "bold", INK2, ab)
        return
    aa = ep(t, C["14.a"], 0.5)
    if aa > 0:
        rrect(c, 260, 210, 1400, 110, 22, mix("#FFFFFF", BLUE, 0.08), aa)
        linha(c, [("VARIÁVEL INTEIRA", BLUE), (": não aceita vírgula (dias, unidades, viagens)", INK2)], W / 2, 265,
              34, aa)
    for k, (cue, emp, resp, nota_) in enumerate((("14.b", "empate: 20 dias", "21 dias", "o primeiro inteiro depois"),
                                                 ("14.c", "empate: 16,7 dias", "17 dias", "arredonde PARA CIMA"))):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        x = 300 + k * 700
        rrect(c, x, 380 + d, 620, 380, 24, "#FFFFFF", a, shadow=True)
        text_mid(c, emp, x + 310, 450 + d, 40, "black", INK2, a)
        arrow(c, x + 310, 500 + d, x + 310, 570 + d, AMBER, a, 6, 20)
        text_mid(c, resp, x + 310, 630 + d, 64, "black", GREEN, a)
        pill(c, nota_, x + 310, 715 + d, AMBER, size=26, a=a, anchor="center", bounds=(0, 1920))


# ======================================================================
# bloco f — decisões que dependem do uso; bloco g — o critério
# ======================================================================

USOS = [("15.a", "ESTACIONAMENTO", "dias de uso"), ("15.b", "LOCADORA", "quilômetros"),
        ("15.c", "TRANSPORTE", "viagens no mês"), ("15.d", "APARELHO ECONÔMICO", "horas de uso")]


def b_uso(c, t, C, B):
    head_seq(c, t, C, [("15", "DECISÕES QUE DEPENDEM DO USO", "O QUE DECIDE?", BLUE),
                       ("16", "A PERGUNTA É SEMPRE A MESMA", "EM QUE CONSUMO EMPATAM?", PURPLE),
                       ("17", "NEM TUDO É DINHEIRO", "O CRITÉRIO É DO ENUNCIADO", AMBER)])
    card(c, *CARD_R)
    sid = which(t, C, ["15", "16", "17"])
    if sid == "15":
        for k, (cue, nome, decide) in enumerate(USOS):
            a, d = rise(t, C[cue])
            if a <= 0:
                continue
            x = 220 + (k % 2) * 760
            y = 240 + (k // 2) * 280 + d
            rrect(c, x, y, 720, 230, 24, "#FFFFFF", a, shadow=True)
            text_mid(c, nome, x + 360, y + 70, 38, "black", BLUE, a)
            text_mid(c, "decide:", x + 360, y + 130, 28, "bold", GRAY, a)
            text_mid(c, decide, x + 360, y + 180, 40, "black", PURPLE, a)
        return
    if sid == "16":
        aa = ep(t, C["16.a"], 0.5)
        if aa > 0:
            regra(c, "em que consumo as opções se igualam?", W / 2, 300, aa, 46)
        ab = ep(t, C["16.b"], 0.5)
        if ab > 0:
            rrect(c, 330, 440, 1260, 300, 26, "#FFFFFF", ab, shadow=True)
            text(c, "RESPOSTA CERTA, MUITAS VEZES:", W / 2, 510, 30, "black", GRAY, ab)
            text_mid(c, "DEPENDE DO USO", W / 2, 590, 72, "black", GREEN, ab)
            text(c, "uma até tal ponto · a outra a partir dele", W / 2, 690, 34, "bold", INK2, ab)
        return
    aa = ep(t, C["17.a"], 0.5)
    for k, s in enumerate(("risco", "conveniência")):
        if aa > 0:
            x = 420 + k * 380
            rrect(c, x - 160, 260, 320, 110, 22, mix("#FFFFFF", GRAY, 0.10), aa)
            text_mid(c, s, x, 315, 40, "black", INK2, aa)
    if aa > 0:
        text(c, "pesam na vida real", 610, 430, 30, "bold", GRAY, aa)
    ab = ep(t, C["17.b"], 0.5)
    if ab > 0:
        rrect(c, 1050, 230, 620, 520, 26, "#FFFFFF", ab, shadow=True)
        text(c, "NA PROVA", 1360, 300, 34, "black", AMBER, ab)
        text_mid(c, "\"menor custo\"", 1360, 420, 52, "black", PURPLE, ab)
        text(c, "o enunciado define", 1360, 540, 32, "bold", INK2, ab)
        text(c, "o critério", 1360, 585, 32, "bold", INK2, ab)
        selo(c, 1360, 670, ab, "RESPONDA POR ELE", AMBER, -5, 30)


# ======================================================================
# nós fazemos — o táxi
# ======================================================================

def b_exercicio(c, t, C, B):
    head_seq(c, t, C, [("18", "SUA VEZ", "PAUSE E TENTE", GREEN), ("19", "VAMOS JUNTOS", "DIFERENÇA ÷ DIFERENÇA", GREEN)])
    card(c, *CARD_R)
    aa = ep(t, C["18.a"], 0.5)
    tabela(c, 330, 200, ["TÁXI", "FIXO", "POR KM", "CUSTO"],
           [["A", "R$ 6,00", "R$ 2,50", "6 + 2,5x"], ["B", "R$ 12,00", "R$ 2,00", "12 + 2x"]], aa,
           [200, 340, 340, 380], cores=[COL_A, COL_B])
    if t < C["19"]:
        ab = ep(t, C["18.b"], 0.5)
        if ab > 0:
            text_mid(c, "a partir de quantos km o B é mais barato?", W / 2, 520, 44, "black", INK, ab)
        pause_timer(c, t, C["18.end"] - 1.9, W / 2, 680)
        return
    ls = [(C["19.a"], [("fixos: 12 − 6 = ", INK), ("6", AMBER), ("   ·   por km: 2,50 − 2,00 = ", INK), ("0,50", GREEN)]),
          (C["19.b"], [("6 ÷ 0,5 = ", INK), ("12 km", PURPLE), ("  (empate)", GRAY)]),
          (C["19.c"], [("teste 20 km:  A = 6 + 50 = ", INK), ("56", COL_A), ("   B = 12 + 40 = ", INK), ("52", COL_B)])]
    passos(c, ls, W / 2, 500, 38, t, dy=80)
    ad = ep(t, C["19.d"], 0.5)
    if ad > 0:
        pill(c, "acima de 12 km, o B é mais barato", W / 2, 790, GREEN, size=34, a=ad, anchor="center",
             bounds=(0, 1920))


# ======================================================================
# recap, erros
# ======================================================================

FRASES = ["Iguale os custos para achar o ponto de equilíbrio.",
          "Abaixo do equilíbrio vence o fixo baixo; acima, o preço por unidade baixo.",
          "No empate, os dois custam o mesmo: \"mais barato\" começa depois."]


def b_recap(c, t, C, B):
    sid = which(t, C, ["20", "33"])
    frame(c, t, B["start"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "20" else "PARA FECHAR", PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 300 + k * 180 + d
        badge_num(c, k + 1, 260, y - 16, a, 36, bg=PURPLE)
        para(c, s, 320, y, 50, "black", INK, a, 1360, 60)


ERROS = [("Escolher um plano sem olhar o consumo: \"o A tem fixo menor, é sempre melhor\"",
          "R$ 50 é menos que R$ 80",
          "depende do uso: acima de 100 minutos, o A perde"),
         ("Dividir a diferença dos fixos por um preço só: 30 ÷ 0,5 = 60",
          "o 0,5 está ali, no plano A",
          "divida pela diferença dos preços: 30 ÷ (0,50 − 0,20) = 30 ÷ 0,3 = 100"),
         ("Arredondar o empate para baixo: passe R$ 150 × R$ 4,40 por viagem → empate 34,1 → \"34\"",
          "34 é o inteiro mais perto",
          "34 viagens = R$ 149,60: o passe ainda não compensa. Resposta: 35")]


def b_erros(c, t, C, B):
    K.erro_cards(c, t, C, ["21", "22", "23"], ERROS)


# ======================================================================
# questões
# ======================================================================

def _enunciado(c, s, a, y0=240, size=28, w=700):
    y = y0
    for ln in K.wrap(s, "black", size, w):
        text(c, ln, 190, y, size, "black", INK, a, align="left")
        y += size + 12
    return y + 8


def _fonte(c, t, a0, t_fim):
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0 * (1 - ep(t, t_fim, 0.3)),
         align="left")


ALTS1 = [("A", "60", "30 ÷ 0,5 (só o preço do A)", RED), ("B", "100", "", GREEN),
         ("C", "150", "30 ÷ 0,2 (só o preço do B)", RED), ("D", "260", "130 ÷ 0,5 (soma dos fixos)", RED),
         ("E", "400", "80 ÷ 0,2 (sem comparar)", RED)]


def b_q1(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 1 · EU FAÇO", "OS PLANOS DE TELEFONIA", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["24.a"], 0.4)
    yend = _enunciado(c, "Uma operadora oferece dois planos mensais. No plano A, o cliente paga R$ 50,00 fixos mais "
                      "R$ 0,50 por minuto de ligação. No plano B, paga R$ 80,00 fixos mais R$ 0,20 por minuto. O plano "
                      "B passa a ser mais vantajoso que o plano A quando o consumo mensal, em minutos, for superior a",
                      a0)
    _fonte(c, t, a0, C["25"])
    cues_in = {L: C[f"24.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"26.x{L.lower()}"] for L in "ACDE"}
    K.alternativas(c, t, C, ALTS1, 1000, 250, 680, 40, C["25.ok"], "B", cues_in, cues_x, gap=40)
    if t < C["25"]:
        return
    y0 = yend + 4
    rrect(c, 170, y0, 740, 830 - y0, 18, "#FFFFFF", ep(t, C["25"], 0.4), shadow=True)
    ls = [(C["25.a"], [("0,3x = 30 → x = ", INK), ("100", PURPLE)]),
          (C["25.b"], [("150 min: A ", INK2), ("125", COL_A), (" · B ", INK2), ("110", COL_B)]),
          (C["25.b"] + 3.0, [("acima de 100: ", INK2), ("B ganha", COL_B)])]
    passos(c, ls, 540, y0 + 60, 32, t, dy=62)


ALTS6 = [("A", "80 km", "60 ÷ 0,75 (um dia só)", RED), ("B", "160 km", "120 ÷ 0,75 (sem a diária de B)", RED),
         ("C", "240 km", "", GREEN), ("D", "480 km", "360 ÷ 0,75 (sem a diária de B)", RED),
         ("E", "720 km", "540 ÷ 0,75 (somou as diárias)", RED)]


def b_q6(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 6 · NÓS FAZEMOS", "AS LOCADORAS DO FERIADO", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["27.a"], 0.4)
    yend = _enunciado(c, "Para uma viagem de 3 dias, uma família compara duas locadoras. A locadora A cobra R$ 120,00 "
                      "por dia, com quilometragem livre. A locadora B cobra R$ 60,00 por dia mais R$ 0,75 por "
                      "quilômetro rodado. A locadora A será mais vantajosa se a família rodar mais de", a0, size=27)
    _fonte(c, t, a0, C["28"])
    cues_in = {L: C[f"27.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {"A": C["29.xa"], "B": C["29.xb"], "D": C["29.xb"] + 1.2, "E": C["29.xe"]}
    K.alternativas(c, t, C, ALTS6, 1000, 250, 680, 38, C["28.ok"], "C", cues_in, cues_x, gap=36)
    if t < C["28"]:
        pause_timer(c, t, C["27.end"] - 1.9, 540, 720)
        return
    y0 = yend + 4
    if t < C["29.c"]:
        tabela(c, 180, y0, ["", "3 DIAS", "CUSTO"], [["A", "3 · 120", "360"], ["B", "3 · 60 = 180", "180 + 0,75x"]],
               ep(t, C["28.a"], 0.4), [80, 300, 340], rh=56, size=28, cores=[COL_A, COL_B])
        ls = [(C["28.b"], [("0,75x = 180 → x = ", INK), ("240 km", PURPLE)]),
              (C["28.c"], [("300 km: B ", INK2), ("405", COL_B), (" · A ", INK2), ("360", COL_A)])]
        passos(c, ls, 540, y0 + 230, 30, t, dy=56)
        return
    acc = ep(t, C["29.c"], 0.4)
    K.atalho(c, 180, y0, 720, 820 - y0, "ATALHO · ÷ 0,75",
             ["0,75 = 3/4", "180 ÷ 0,75 = 180 × 4 ÷ 3 = 240"], acc, 30)


ALTS9 = [("A", "10", "300 ÷ 30 (diária da mensalidade)", RED), ("B", "12", "o próprio empate", AMBER),
         ("C", "13", "", GREEN), ("D", "20", "dias úteis? não foi dito", RED),
         ("E", "25", "o valor da diária", RED)]


def b_q9(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 9 · VOCÊ FAZ", "MENSALISTA OU DIARISTA?", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["30.a"], 0.4)
    yend = _enunciado(c, "Um estacionamento cobra R$ 25,00 por dia de uso ou R$ 300,00 pela mensalidade, que permite "
                      "usar todos os dias do mês. O número mínimo de dias de uso no mês para que a mensalidade seja "
                      "mais barata que o pagamento por diárias é", a0)
    _fonte(c, t, a0, C["31"])
    cues_in = {L: C[f"30.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"32.x{L.lower()}"] for L in "ABDE"}
    K.alternativas(c, t, C, ALTS9, 1000, 250, 680, 40, C["31.ok"], "C", cues_in, cues_x, gap=40)
    if t < C["31"]:
        pause_timer(c, t, C["30.end"] - 2.4, 540, 720, dur=2.1)
        return
    y0 = yend + 4
    rrect(c, 170, y0, 740, 830 - y0, 18, "#FFFFFF", ep(t, C["31"], 0.4), shadow=True)
    ls = [(C["31.a"], [("25d = 300 → d = ", INK), ("12", AMBER), (" (empate)", GRAY)]),
          (C["31.b"], [("12 dias: R$ 300 = R$ 300", INK2)]),
          (C["31.c"], [("13 dias: ", INK2), ("R$ 325", RED), (" > R$ 300", INK2)])]
    passos(c, ls, 540, y0 + 60, 32, t, dy=60)
    ab = ep(t, C["31.b"] + 2.2, 0.4)
    if ab > 0:
        selo(c, 815, y0 + 150, ab, "AINDA NÃO", AMBER, -6, 24)


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "CUSTOS ESCONDIDOS", PURPLE)
    caixa(c, 660, 400, "APLICAÇÃO 1", "12% ao ano", BLUE, ep(t, C["34.a"], 0.5), 520, sub="com imposto", h=170)
    caixa(c, 1260, 400, "APLICAÇÃO 2", "10% ao ano", GREEN, ep(t, C["34.b"], 0.5), 520, sub="isenta", h=170)
    acc = ep(t, C["34.c"], 0.5)
    if acc > 0:
        text_mid(c, "A DE 12% GANHA?", W / 2, 640, 64, "black", AMBER, acc)
    ad = ep(t, C["34.d"], 0.5)
    if ad > 0:
        pill(c, "ep. 3 · investimentos líquidos", W / 2, 760, PURPLE, size=32, a=ad, anchor="center",
             bounds=(0, 1920))


def b_cta(c, t, C, B):
    cta(c, t, C["35.like"], C["35.sub"], C["35.bell"], C["35.com"], C["35.bye"],
        "Qual plano você usa? Ele vale a pena para o seu consumo?", canal="no Estudativo", anki=C["35.anki"])


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, concreto=b_concreto, formula=b_formula,
              empate=b_empate, grafico=b_grafico, teste=b_teste, cofrinho=b_cofrinho, apartir=b_apartir, uso=b_uso,
              exercicio=b_exercicio, recap=b_recap, erros=b_erros, q1=b_q1, q6=b_q6, q9=b_q9, ponte=b_ponte,
              cta=b_cta)
