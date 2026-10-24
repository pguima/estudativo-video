"""Visual — Equações e Inequações do 1º Grau, Episódio 4: comparar planos, o ponto de equilíbrio (tema claro).
Peças comuns da série em ../../comum.py (reexporta o 019/comum.py: expr, alternativas, erro_cards, atalho...).
Peças deste episódio: carro() e corrida() (dois carrinhos numa pista: B larga na frente, A corre mais rápido e os dois se
emparelham no km 100 com o selo EQUILÍBRIO), tabela() (os custos dos dois planos em 50, 100 e 200 km, preenchidos aos
poucos), retas() (o cruzamento só como ilustração, citando Função afim), frac() (fração com texto livre, para o atalho).
Cores com função: azul = definição · roxo = regra/fórmula · âmbar = armadilha · verde = atalho/dica · vermelho = erro.
"""
import importlib.util
from pathlib import Path
import skia
import motor
motor.set_theme("claro")
from motor import *  # noqa
from aula import *  # noqa

_p = Path(__file__).resolve().parents[2] / "comum.py"
_s = importlib.util.spec_from_file_location("comum035", _p)
K = importlib.util.module_from_spec(_s); _s.loader.exec_module(K)
K.usar_tempos(Path(__file__).resolve().parents[1] / "audio" / "tempos.json")
motor.set_theme("claro")
frame, head_seq, which, para, boxed, regra, selo, pause_timer, chip = (K.frame, K.head_seq, K.which, K.para, K.boxed, K.regra,
                                                                        K.selo, K.pause_timer, K.chip)
fmid, ftext, ftext_w, expr = K.fmid, K.ftext, K.ftext_w, K.expr

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_equacoes_ep4_ponto_equilibrio.mp4"
CARD_R = K.CARD_R
COR_A = BLUE
COR_B = "#E0731F"


def custo_a(x):
    return 90 + 0.5 * x


def custo_b(x):
    return 60 + 0.8 * x


def brl(v):
    s = f"{v:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    return "R$ " + s


# ======================================================================
# peças do episódio
# ======================================================================

def linha(c, partes, cx, cy, size, a, peso="black", align="center"):
    """texto numa linha com cor por trecho: partes = [(texto, cor)]."""
    ws = [ftext_w(s_, peso, size) for s_, _ in partes]
    x = cx - sum(ws) / 2 if align == "center" else cx
    for (s_, col), w_ in zip(partes, ws):
        if a > 0:
            fmid(c, s_, x, cy, size, peso, col or INK, a, align="left")
        x += w_


def frac(c, num, den, cx, cy, size, a, col_n=None, col_d=None):
    """fração empilhada com texto livre; devolve a largura"""
    if a <= 0:
        return 0
    w = max(ftext_w(num, "black", size), ftext_w(den, "black", size)) + 30
    fmid(c, num, cx, cy - size * 0.62, size, "black", col_n or INK, a)
    line(c, cx - w / 2, cy, cx + w / 2, cy, INK, a, max(3, size * 0.07))
    fmid(c, den, cx, cy + size * 0.68, size, "black", col_d or INK, a)
    return w


def carro(c, cx, cy, s, col, a, rot=""):
    """carrinho visto de lado, centrado em (cx, cy), comprimento ~ 2s"""
    if a <= 0:
        return
    rrect(c, cx - s, cy - s * 0.32, 2 * s, s * 0.52, s * 0.18, col, a, shadow=True)
    p = skia.Path()
    p.moveTo(cx - s * 0.55, cy - s * 0.3); p.lineTo(cx - s * 0.3, cy - s * 0.72)
    p.lineTo(cx + s * 0.35, cy - s * 0.72); p.lineTo(cx + s * 0.62, cy - s * 0.3); p.close()
    c.drawPath(p, paint(col, a))
    rrect(c, cx - s * 0.24, cy - s * 0.64, s * 0.24, s * 0.28, s * 0.05, "#DDEBF7", a)
    rrect(c, cx + s * 0.06, cy - s * 0.64, s * 0.3, s * 0.28, s * 0.05, "#DDEBF7", a)
    for wx in (-0.55, 0.58):
        c.drawCircle(cx + s * wx, cy + s * 0.22, s * 0.24, paint(INK, a))
        c.drawCircle(cx + s * wx, cy + s * 0.22, s * 0.1, paint("#C8CDD3", a))
    if rot:
        fmid(c, rot, cx + s * 0.05, cy - s * 0.04, s * 0.42, "black", "#FFFFFF", a)


def _pos(v):
    """posição na pista: v = km − custo (quanto MENOR o custo, mais à frente)"""
    return 330 + (v + 95) * 12.4


def corrida(c, km, a, y0=330, gap=230, selo_eq=0.0):
    """duas faixas; o carro está em _pos(km − custo). B (60 + 0,8x) larga na frente; A (90 + 0,5x) corre mais rápido."""
    if a <= 0:
        return
    for k, (nome, col, f) in enumerate((("B", COR_B, custo_b), ("A", COR_A, custo_a))):
        y = y0 + k * gap
        rrect(c, 260, y + 40, 1440, 22, 11, "#D9DCD6", a)
        for xx in range(300, 1700, 90):
            rrect(c, xx, y + 46, 44, 10, 5, "#FFFFFF", a)
        x = _pos(km - f(km))
        carro(c, x, y - 8, 78, col, a, nome)
        pill(c, brl(f(km)), x, y - 110, col, size=28, a=a, anchor="center", bounds=(0, 1920))
    rrect(c, 1500, 180, 200, 70, 18, mix("#FFFFFF", INK, 0.06), a)
    fmid(c, f"km {km:.0f}", 1600, 215, 34, "black", INK, a)
    if selo_eq > 0:
        selo(c, _pos(km - custo_a(km)) + 260, y0 + gap / 2 - 20, selo_eq, "EQUILÍBRIO", GREEN, -4, 36)


TAB_X = [380, 760, 1160, 1560]


def tabela(c, t, a, cel, y0=280, rh=110, hl=None, fs=1.0):
    """custos de A e B em 50, 100 e 200 km. cel = {(linha, coluna): instante de entrada}; hl = coluna em destaque"""
    if a <= 0:
        return
    w = 1520
    rrect(c, 200, y0 - 60, w, rh * 3 + 70, 22, "#FFFFFF", a, shadow=True)
    for j, s in enumerate(("", "50 km", "100 km", "200 km")):
        if s:
            text(c, s, TAB_X[j], y0 + 12, 34 * fs, "black", GRAY, a)
    for i, (nome, col, f) in enumerate((("A  90 + 0,50 por km", COR_A, custo_a), ("B  60 + 0,80 por km", COR_B, custo_b))):
        y = y0 + rh * (i + 1)
        rrect(c, 220, y - 42 * fs, 14, 84 * fs, 7, col, a)
        text(c, nome, 250, y + 12 * fs, 30 * fs, "black", col, a, align="left")
        for j, km in enumerate((50, 100, 200)):
            t0 = cel.get((i, j))
            if t0 is None:
                continue
            ac = a * ep(t, t0, 0.4)
            if ac <= 0:
                continue
            other = (custo_b if i == 0 else custo_a)(km)
            win = f(km) < other
            tie = abs(f(km) - other) < 1e-9
            colv = GREEN if win else (PURPLE if tie else INK2)
            if hl == j:
                rrect(c, TAB_X[j + 1] - 150, y - 40 * fs, 300, 80 * fs, 16, mix("#FFFFFF", colv, 0.14), ac)
            text(c, brl(f(km)), TAB_X[j + 1], y + 12 * fs, 38 * fs, "black", colv, ac)
    line(c, 220, y0 + rh * 0.5 + 6, 200 + w - 20, y0 + rh * 0.5 + 6, "#E6E6E2", a, 3)


def retas(c, a, u=1.0, x0=300, y0=780, w=760, h=460):
    """ilustração: as duas retas (custo × km, de 0 a 200) cruzando no km 100"""
    if a <= 0:
        return
    px = lambda km: x0 + km / 200 * w
    py = lambda v: y0 - (v - 40) / 200 * h
    line(c, x0, y0, x0 + w + 30, y0, INK2, a, 3)
    line(c, x0, y0, x0, y0 - h - 20, INK2, a, 3)
    text(c, "km", x0 + w + 40, y0 + 10, 24, "bold", GRAY, a, align="left")
    text(c, "R$", x0 - 14, y0 - h - 30, 24, "bold", GRAY, a, align="right")
    for nome, col, f in (("A", COR_A, custo_a), ("B", COR_B, custo_b)):
        k1 = 200 * u
        line(c, px(0), py(f(0)), px(k1), py(f(k1)), col, a, 6)
        if u > 0.95:
            text(c, nome, px(200) + 16, py(f(200)) + 10, 30, "black", col, a, align="left")
    if u > 0.6:
        ac = a * clamp((u - 0.6) / 0.3)
        c.drawCircle(px(100), py(140), 13, paint(PURPLE, ac))
        line(c, px(100), py(140), px(100), y0, PURPLE, ac * 0.6, 2)
        text(c, "100", px(100), y0 + 36, 24, "black", PURPLE, ac)


# ======================================================================
# abertura
# ======================================================================

def cartaz(c, cx, cy, nome, l1, l2, col, a, w=520):
    if a <= 0:
        return
    rrect(c, cx - w / 2, cy - 130, w, 260, 26, "#FFFFFF", a, shadow=True)
    rrect(c, cx - w / 2, cy - 130, w, 70, 26, col, a)
    rrect(c, cx - w / 2, cy - 90, w, 30, 0, col, a)
    fmid(c, nome, cx, cy - 95, 34, "black", "#FFFFFF", a)
    fmid(c, l1, cx, cy - 10, 36, "black", INK, a)
    fmid(c, l2, cx, cy + 60, 36, "black", INK, a)


def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "QUAL PLANO COMPENSA?", BLUE)
    cartaz(c, 560, 360, "GRÁFICA P", "taxa R$ 120,00", "+ R$ 0,35 por cartaz", COR_A, ep(t, C["01.a"], 0.5))
    cartaz(c, 1360, 360, "GRÁFICA Q", "sem taxa", "R$ 0,50 por cartaz", COR_B, ep(t, C["01.b"], 0.5))
    acc = ep(t, C["01.c"], 0.5)
    if acc > 0:
        linha(c, [("800 cartazes:  ", INK), ("R$ 400,00", PURPLE), ("  =  ", INK), ("R$ 400,00", PURPLE)], W / 2, 600,
              46, acc)
    ad = ep(t, C["01.d"], 0.5)
    if ad > 0:
        text(c, "A PARTIR DE QUANTOS CARTAZES P É MAIS BARATA?", W / 2, 720, 40, "black", INK, ad)
    ae = ep(t, C["01.e"], 0.5)
    if ae > 0:
        selo(c, W / 2, 840, ae, "NÃO É 800", RED, -4, 52)


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "AO FINAL", "VOCÊ VAI CONSEGUIR", GREEN)
    rows = [("02.a", "achar o ponto de equilíbrio em uma linha", "diferença das taxas ÷ diferença dos preços"),
            ("02.b", "dizer qual plano compensa antes e depois dele", "antes: taxa fixa menor · depois: preço menor")]
    for j, (cue, s, sub) in enumerate(rows):
        a, d = rise(t, C[cue])
        y = 360 + j * 200 + d
        check_icon(c, 300, y - 14, 34, a, GREEN)
        text(c, s, 360, y, 48, "black", INK, a, align="left")
        ftext(c, sub, 360, y + 58, 32, "bold", GRAY, a, align="left")


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "DOIS LEMBRETES", "RÁPIDOS", GREEN)
    aa = ep(t, C["03.a"], 0.5)
    if aa > 0:
        text(c, "EQUAÇÃO", 560, 290, 34, "black", PURPLE, aa)
        text(c, "episódio 1", 560, 334, 24, "bold", GRAY, aa)
        text(c, "a mesma coisa nos dois lados", 560, 410, 26, "bold", INK2, aa)
        expr(c, "3x + 4 = 19", 560, 530, 70, aa)
        expr(c, "x = 5", 560, 650, 70, ep(t, C["03.a"] + 2.0, 0.4), cores={2: GREEN})
    ab = ep(t, C["03.b"], 0.5)
    if ab > 0:
        text(c, "INEQUAÇÃO", 1360, 290, 34, "black", BLUE, ab)
        text(c, "episódio 3", 1360, 334, 24, "bold", GRAY, ab)
        text(c, "resposta inteira: o próximo inteiro", 1360, 410, 26, "bold", INK2, ab)
        expr(c, "x > 82,5", 1360, 530, 70, ab)
        a2 = ep(t, C["03.b"] + 3.0, 0.4)
        if a2 > 0:
            rrect(c, 1170, 600, 380, 100, 22, mix("#FFFFFF", GREEN, 0.16), a2)
            fmid(c, "menor inteiro: 83", 1360, 650, 40, "black", GREEN, a2)
    line(c, 960, 250, 960, 760, "#E6E6E2", ab, 3)


# ======================================================================
# concreto: as locadoras
# ======================================================================

def b_locadoras(c, t, C, B):
    head_seq(c, t, C, [("04", "DUAS LOCADORAS", "TAXA FIXA · PREÇO POR UNIDADE", BLUE),
                       ("05", "QUAL É MAIS BARATA?", "50 km E 200 km", BLUE)])
    card(c, *CARD_R)
    sid = which(t, C, ["04", "05"])
    if sid == "04":
        for k, (cue, nome, fixo, un, col) in enumerate((("04.a", "LOCADORA A", "R$ 90,00", "R$ 0,50", COR_A),
                                                         ("04.b", "LOCADORA B", "R$ 60,00", "R$ 0,80", COR_B))):
            a = ep(t, C[cue], 0.5)
            if a <= 0:
                continue
            cx = 560 + k * 800
            rrect(c, cx - 320, 240, 640, 330, 26, "#FFFFFF", a, shadow=True)
            carro(c, cx - 190, 330, 70, col, a, nome[-1])
            text(c, nome, cx + 60, 345, 40, "black", col, a, align="left")
            sf = ep(t, C["04.c"], 0.4)
            su = ep(t, C["04.d"], 0.4)
            rrect(c, cx - 290, 405, 580, 66, 16, mix("#FFFFFF", BLUE, 0.16 * sf), a)
            text(c, "diária", cx - 260, 450, 30, "bold", GRAY, a, align="left")
            text(c, fixo, cx + 260, 450, 38, "black", INK, a, align="right")
            rrect(c, cx - 290, 485, 580, 66, 16, mix("#FFFFFF", BLUE, 0.16 * su), a)
            text(c, "por km", cx - 260, 530, 30, "bold", GRAY, a, align="left")
            text(c, un, cx + 260, 530, 38, "black", INK, a, align="right")
        acc = ep(t, C["04.c"], 0.5)
        if acc > 0:
            rrect(c, 240, 620, 1440, 90, 20, mix("#FFFFFF", BLUE, 0.10), acc)
            linha(c, [("TAXA FIXA", BLUE), (": paga mesmo sem sair do lugar", INK)], W / 2, 665, 34, acc)
        ad = ep(t, C["04.d"], 0.5)
        if ad > 0:
            rrect(c, 240, 730, 1440, 90, 20, mix("#FFFFFF", BLUE, 0.10), ad)
            linha(c, [("PREÇO POR UNIDADE", BLUE), (": cobrado a cada km", INK)], W / 2, 775, 34, ad)
        return
    aa = ep(t, C["05"], 0.4)
    tabela(c, t, aa, {(0, 0): C["05.a"], (1, 0): C["05.a"] + 3.0, (0, 2): C["05.b"], (1, 2): C["05.b"] + 3.2})
    if ep(t, C["05.a"] + 5.0, 0.4) > 0:
        pill(c, "B ganha", TAB_X[1], 640, GREEN, size=28, a=ep(t, C["05.a"] + 5.0, 0.4), anchor="center")
    if ep(t, C["05.b"] + 5.2, 0.4) > 0:
        pill(c, "A ganha", TAB_X[3], 640, GREEN, size=28, a=ep(t, C["05.b"] + 5.2, 0.4), anchor="center")
    acc = ep(t, C["05.c"], 0.5)
    if acc > 0:
        fmid(c, "?", TAB_X[2], 440, 140, "black", AMBER, acc)
        selo(c, W / 2, 770, acc, "A RESPOSTA VIROU. ONDE?", AMBER, -2, 40)


# ======================================================================
# a corrida
# ======================================================================

def b_corrida(c, t, C, B):
    head(c, t, B["start"], "A CORRIDA DOS PLANOS", "QUEM ULTRAPASSA?", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["06.a"], 0.5)
    km = 100 * ep(t, C["06.b"] + 1.0, max(1.0, C["06.d"] - C["06.b"] - 1.0))
    km = round(km + 60 * ep(t, C["06.e"], 3.0))
    corrida(c, km, aa, selo_eq=ep(t, C["06.d"], 0.5) * (1 - ep(t, C["06.e"], 0.4)))
    if ep(t, C["06.a"] + 1.5, 0.4) > 0 and t < C["06.b"]:
        pill(c, "taxa menor: larga na frente", 900, 230, COR_B, size=28, a=ep(t, C["06.a"] + 1.5, 0.4), anchor="center")
    ab = ep(t, C["06.b"], 0.5) * (1 - ep(t, C["06.d"], 0.4))
    if ab > 0:
        pill(c, "preço por km menor: corre mais rápido", 900, 230, COR_A, size=28, a=ab, anchor="center")
    ad = ep(t, C["06.d"], 0.5)
    if ad > 0:
        rrect(c, 240, 760, 1440, 70, 18, mix("#FFFFFF", BLUE, 0.10), ad)
        linha(c, [("PONTO DE EQUILÍBRIO", BLUE), (": os dois custam exatamente o mesmo", INK)], W / 2, 795, 30, ad)
    ae = ep(t, C["06.e"], 0.5)
    if ae > 0:
        rrect(c, 240, 680, 1440, 66, 18, mix("#FFFFFF", BLUE, 0.10), ae)
        linha(c, [("COMPENSAR", BLUE), (": custar MENOS que o outro", INK)], W / 2, 713, 30, ae)


# ======================================================================
# bloco a — equação · bloco b — inequação
# ======================================================================

def _passos(c, t, rows, x, y0, size, dy, xnota=1660):
    for k, (t0, ex, nota, col) in enumerate(rows):
        a, d = rise(t, t0)
        if a <= 0:
            continue
        y = y0 + k * dy + d
        expr(c, ex, x, y, size, a, align="left")
        if nota:
            pill(c, nota, xnota, y, col or PURPLE, size=24, a=a, anchor="right", bounds=(0, 1920))


def b_equacao(c, t, C, B):
    head(c, t, B["start"], "BLOCO A · CUSTOS IGUAIS", "UMA EQUAÇÃO", PURPLE)
    card(c, *CARD_R)
    rows = [(C["07.a"], "90 + 0,5x = 60 + 0,8x", "custo de A = custo de B", BLUE),
            (C["07.b"], "30 = 0,3x", "− 60 e − 0,5x nos dois lados", PURPLE),
            (C["07.c"], "x = 100 km", "÷ 0,3 nos dois lados", PURPLE)]
    _passos(c, t, rows, 260, 270, 64, 105)
    ad = ep(t, C["07.d"], 0.5)
    if ad > 0:
        cel = {(0, 0): 0, (1, 0): 0, (0, 2): 0, (1, 2): 0, (0, 1): C["07.d"] + 1.0, (1, 1): C["07.d"] + 3.0}
        tabela(c, t, ad, cel, y0=600, rh=55, hl=1, fs=0.62)
        text(c, "CONFIRA OS DOIS", TAB_X[0] - 60, 612, 20, "black", GREEN, ad, tracking=2)
        pill(c, "EMPATE", TAB_X[2], 812, PURPLE, size=24, a=ep(t, C["07.d"] + 4.0, 0.4), anchor="center")


def b_inequacao(c, t, C, B):
    head(c, t, B["start"], "BLOCO B · B MAIS BARATA", "UMA INEQUAÇÃO", PURPLE)
    card(c, *CARD_R)
    rows = [(C["08.a"], "60 + 0,8x < 90 + 0,5x", "troque = por <", BLUE),
            (C["08.b"], "0,3x < 30", "as mesmas contas", PURPLE),
            (C["08.b"] + 2.4, "x < 100 km", "B mais barata", GREEN)]
    _passos(c, t, rows, 260, 280, 64, 115)
    acc = ep(t, C["08.c"], 0.5)
    if acc > 0:
        rrect(c, 260, 590, 660, 200, 22, mix("#FFFFFF", PURPLE, 0.10), acc)
        text(c, "km 100: R$ 140 = R$ 140", 590, 650, 32, "black", INK, acc)
        text(c, "NO EMPATE NINGUÉM", 590, 712, 34, "black", PURPLE, acc)
        text(c, "É MAIS BARATO", 590, 756, 34, "black", PURPLE, acc)
    ad = ep(t, C["08.d"], 0.5)
    if ad > 0:
        rrect(c, 980, 590, 680, 200, 22, mix("#FFFFFF", GREEN, 0.12), ad)
        text(c, "A mais barata: depois de 100", 1320, 650, 30, "black", INK, ad)
        text(c, "a partir de 101 km", 1320, 730, 46, "black", GREEN, ad)
        text(c, "(km inteiros: R$ 140,50 × R$ 140,80)", 1320, 772, 22, "bold", GRAY, ad)


# ======================================================================
# bloco c — a leitura (gráfico só como ilustração)
# ======================================================================

def b_leitura(c, t, C, B):
    head(c, t, B["start"], "BLOCO C · A LEITURA", "ANTES E DEPOIS DO 100", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["09.a"], 0.5)
    if aa > 0:
        rrect(c, 1120, 250, 560, 210, 22, mix("#FFFFFF", COR_B, 0.10), aa)
        text(c, "ANTES DE 100 km", 1400, 310, 30, "black", COR_B, aa)
        text(c, "pesa a TAXA FIXA", 1400, 370, 32, "black", INK, aa)
        text(c, "B ganha", 1400, 425, 30, "black", GREEN, aa)
    ab = ep(t, C["09.b"], 0.5)
    if ab > 0:
        rrect(c, 1120, 490, 560, 210, 22, mix("#FFFFFF", COR_A, 0.10), ab)
        text(c, "DEPOIS DE 100 km", 1400, 550, 30, "black", COR_A, ab)
        text(c, "pesa o PREÇO POR km", 1400, 610, 32, "black", INK, ab)
        text(c, "A ganha", 1400, 665, 30, "black", GREEN, ab)
    acc = ep(t, C["09.c"], 0.5)
    retas(c, acc, ep(t, C["09.c"], 2.0), x0=300, y0=730, w=640, h=440)
    if acc > 0:
        pill(c, "só ilustração · o gráfico vem na série de Função afim", W / 2, 800, PURPLE, size=24, a=acc,
             anchor="center")


# ======================================================================
# bloco d — o atalho da diferença
# ======================================================================

def b_atalho(c, t, C, B):
    head(c, t, B["start"], "BLOCO D · ATALHO", "O PONTO DE EQUILÍBRIO EM UMA LINHA", GREEN)
    card(c, *CARD_R)
    aa = ep(t, C["10.a"], 0.5)
    if aa > 0:
        rrect(c, 240, 240, 680, 150, 22, mix("#FFFFFF", COR_B, 0.10), aa)
        text(c, "B larga na frente", 580, 290, 28, "bold", GRAY, aa)
        text(c, "90 − 60 = R$ 30,00", 580, 355, 44, "black", COR_B, aa)
    ab = ep(t, C["10.b"], 0.5)
    if ab > 0:
        rrect(c, 1000, 240, 680, 150, 22, mix("#FFFFFF", COR_A, 0.10), ab)
        text(c, "A tira por km", 1340, 290, 28, "bold", GRAY, ab)
        text(c, "0,80 − 0,50 = R$ 0,30", 1340, 355, 44, "black", COR_A, ab)
    acc = ep(t, C["10.c"], 0.5)
    if acc > 0:
        w = frac(c, "R$ 30,00", "R$ 0,30 por km", 760, 520, 50, acc, COR_B, COR_A)
        fmid(c, "=  100 km", 760 + w / 2 + 40, 520, 64, "black", GREEN, acc, align="left")
    ad = ep(t, C["10.d"], 0.5)
    if ad > 0:
        boxed(c, 240, 640, 1440, 170, GREEN, ad, 0.08)
        text(c, "ATALHO DA DIFERENÇA", W / 2, 684, 22, "black", GREEN, ad, tracking=2)
        frac(c, "diferença das taxas fixas", "diferença dos preços por unidade", W / 2, 750, 34, ad)


# ======================================================================
# bloco e — mesma tarifa: nunca empatam
# ======================================================================

def b_mesmatarifa(c, t, C, B):
    head(c, t, B["start"], "BLOCO E · MESMA TARIFA", "NUNCA EMPATAM", RED)
    card(c, *CARD_R)
    aa = ep(t, C["11.a"], 0.5)
    if aa > 0:
        mv = ep(t, C["11.a"], 4.0)
        for k, (nome, col, dx) in enumerate((("B", COR_B, 220), ("A", COR_A, 0))):
            y = 330 + k * 170
            rrect(c, 260, y + 40, 1440, 18, 9, "#D9DCD6", aa)
            carro(c, 420 + dx + 900 * mv, y, 64, col, aa, nome)
        pill(c, "mesma velocidade: a distância não muda", W / 2, 230, AMBER, size=28, a=aa, anchor="center")
    ab = ep(t, C["11.b"], 0.5)
    if ab > 0:
        rrect(c, 260, 610, 680, 190, 22, mix("#FFFFFF", RED, 0.08), ab)
        text(c, "Q6 do episódio 1", 600, 660, 26, "bold", GRAY, ab)
        text(c, "40 + 3x = 3x + 36", 600, 715, 38, "black", INK, ab)
        text(c, "0x = −4", 600, 770, 40, "black", RED, ab)
    acc = ep(t, C["11.c"], 0.5)
    if acc > 0:
        rrect(c, 980, 610, 680, 190, 22, mix("#FFFFFF", RED, 0.08), acc)
        w = frac(c, "diferença das taxas", "0", 1180, 700, 30, acc, INK, RED)
        text(c, "não existe", 1450, 690, 34, "black", RED, acc)
        text(c, "NUNCA EMPATAM", 1450, 740, 30, "black", RED, acc)


# ======================================================================
# nós fazemos
# ======================================================================

def b_exercicio(c, t, C, B):
    head_seq(c, t, C, [("12", "SUA VEZ", "PAUSE E TENTE", GREEN), ("13", "VAMOS JUNTOS", "PELO ATALHO", GREEN)])
    card(c, *CARD_R)
    aa = ep(t, C["12.a"], 0.5)
    ab = ep(t, C["12.b"], 0.5)
    rrect(c, 240, 230, 690, 120, 20, mix("#FFFFFF", COR_A, 0.10), aa)
    text(c, "ESTACIONAMENTO A", 585, 270, 24, "black", COR_A, aa, tracking=1)
    text(c, "R$ 12,00 + R$ 3,00 por hora", 585, 325, 34, "black", INK, aa)
    rrect(c, 990, 230, 690, 120, 20, mix("#FFFFFF", COR_B, 0.10), ab)
    text(c, "ESTACIONAMENTO B", 1335, 270, 24, "black", COR_B, ab, tracking=1)
    text(c, "R$ 4,00 + R$ 5,00 por hora", 1335, 325, 34, "black", INK, ab)
    acc = ep(t, C["12.c"], 0.5) * (1 - ep(t, C["13"], 0.3))
    if acc > 0:
        text(c, "empatam em quantas horas?  ·  qual compensa para 6 horas?", W / 2, 430, 34, "black", INK, acc)
    pause_timer(c, t, C["12.end"] - 1.9, W / 2, 600)
    if t < C["13"]:
        return
    a1 = ep(t, C["13.a"], 0.5)
    if a1 > 0:
        w = frac(c, "12 − 4 = 8", "5 − 3 = 2", 520, 520, 46, a1, PURPLE, PURPLE)
        fmid(c, "=  4 horas", 520 + w / 2 + 30, 520, 56, "black", GREEN, ep(t, C["13.a"] + 6.0, 0.4), align="left")
    a2 = ep(t, C["13.b"], 0.5)
    if a2 > 0:
        rrect(c, 240, 640, 690, 160, 22, mix("#FFFFFF", GREEN, 0.12), a2)
        text(c, "CONFIRA OS DOIS · 4 h", 585, 680, 20, "black", GREEN, a2, tracking=2)
        text(c, "A: 12 + 12 = R$ 24,00", 585, 730, 32, "black", COR_A, a2)
        text(c, "B: 4 + 20 = R$ 24,00", 585, 778, 32, "black", COR_B, a2)
    a3 = ep(t, C["13.c"], 0.5)
    if a3 > 0:
        rrect(c, 990, 450, 690, 350, 22, "#FFFFFF", a3, shadow=True)
        text(c, "6 HORAS", 1335, 510, 26, "black", GRAY, a3, tracking=2)
        text(c, "A: 12 + 18 = R$ 30,00", 1335, 590, 40, "black", GREEN, a3)
        text(c, "B: 4 + 30 = R$ 34,00", 1335, 660, 40, "black", INK2, a3)
        pill(c, "A COMPENSA", 1335, 745, GREEN, size=32, a=ep(t, C["13.c"] + 3.0, 0.4), anchor="center")


# ======================================================================
# recap, erros
# ======================================================================

FRASES = ["Taxa fixa menor ganha no começo; preço por unidade menor ganha no fim.",
          "Equilíbrio = diferença das taxas ÷ diferença dos preços.",
          "No empate ninguém é mais barato."]


def b_recap(c, t, C, B):
    sid = which(t, C, ["14", "24"])
    frame(c, t, B["start"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "14" else "PARA FECHAR", PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 300 + k * 180 + d
        badge_num(c, k + 1, 260, y - 16, a, 36, bg=PURPLE)
        para(c, s, 320, y, 52, "black", INK, a, 1360, 62)


ERROS = [("“A é mais barata a partir de 100 km”", "o 100 é o número que a conta deu",
          "no km 100 os dois custam R$ 140,00: mais barata só a partir de 101 km"),
         ("30 ÷ 0,8 = 37,5 km  (ou 30 ÷ 1,30)", "os dois números estão no enunciado",
          "o que fecha a distância é a DIFERENÇA: 30 ÷ 0,3 = 100 · em 37,5 km A e B não empatam"),
         ("90 + 60 = 0,3x  →  x = 500 km", "passar para o outro lado parece só mudar de lugar",
          "quem soma passa SUBTRAINDO: 90 − 60 = 0,3x · em 500 km: R$ 340 × R$ 460")]


def b_erros(c, t, C, B):
    K.erro_cards(c, t, C, ["15", "16", "17"], ERROS)


# ======================================================================
# questões 1 e 2 do material
# ======================================================================

def _enunciado(c, s, a, y0=250, size=29, w=720):
    y = y0
    for ln in K.wrap(s, "black", size, w):
        text(c, ln, 190, y, size, "black", INK, a, align="left")
        y += size + 12
    return y


def _painel(c, a, y0=230):
    rrect(c, 170, y0, 760, 830 - y0, 18, "#FFFFFF", a, shadow=True)


ALTS1 = [("A", "30", "30 ÷ 1 (soma das tarifas)", RED),
         ("B", "50", "30 ÷ 0,6 (tarifa do Beta só)", RED),
         ("C", "70", "70 ÷ 1 (somou tudo)", RED),
         ("D", "150", "", GREEN),
         ("E", "350", "70 ÷ 0,2 (sinal trocado)", RED)]


def b_q1(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 1 · EU FAÇO", "PLANOS DE TELEFONIA", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["18.a"], 0.4) * (1 - ep(t, C["19"], 0.4))
    yend = _enunciado(c, "Uma operadora oferece dois planos de telefonia. No plano Alfa, paga-se uma mensalidade de R$ 50,00 "
                         "mais R$ 0,40 por minuto de ligação. No plano Beta, a mensalidade é de R$ 20,00 e o minuto custa "
                         "R$ 0,60. O número de minutos mensais para o qual os dois planos custam o mesmo valor é", a0)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0, align="left")
    cues_in = {L: C[f"18.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"20.x{L.lower()}"] for L in "ABCE"}
    K.alternativas(c, t, C, ALTS1, 1000, 260, 680, 34, C["19.ok"], "D", cues_in, cues_x, gap=34)
    pause_timer(c, t, C["18.end"] - 1.9, 540, yend + 100)
    if t >= C["19"]:
        ap = ep(t, C["19"], 0.4)
        _painel(c, ap)
        text(c, "o mesmo valor → EMPATE → equação", 550, 285, 26, "black", PURPLE, ap)
        rows = [(C["19.a"], "50 + 0,4x = 20 + 0,6x", "", None), (C["19.a"] + 3.4, "30 = 0,2x", "", None),
                (C["19.a"] + 5.0, "x = 150", "", None)]
        _passos(c, t, rows, 230, 360, 44, 72)
        ab = ep(t, C["19.b"], 0.4)
        if ab > 0:
            rrect(c, 200, 570, 700, 100, 18, mix("#FFFFFF", GREEN, 0.12), ab)
            text(c, "ATALHO", 240, 602, 18, "black", GREEN, ab, align="left", tracking=2)
            text(c, "(50 − 20) ÷ (0,60 − 0,40) = 30 ÷ 0,2 = 150", 550, 650, 28, "black", INK, ab)
        acc = ep(t, C["19.c"], 0.4)
        if acc > 0:
            rrect(c, 200, 690, 700, 120, 18, mix("#FFFFFF", GREEN, 0.10), acc)
            text(c, "Alfa: 50 + 60 = R$ 110,00", 550, 735, 28, "black", INK2, acc)
            text(c, "Beta: 20 + 90 = R$ 110,00", 550, 785, 28, "black", INK2, acc)


ALTS2 = [("A", "240", "120 ÷ 0,50", RED),
         ("B", "343", "120 ÷ 0,35", RED),
         ("C", "480", "usou 0,25", RED),
         ("D", "800", "o empate", AMBER),
         ("E", "801", "", GREEN)]


def b_q2(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 2 · VOCÊ FAZ", "A PARTIR DE QUANTOS", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["21.a"], 0.4) * (1 - ep(t, C["22"], 0.4))
    yend = _enunciado(c, "A gráfica P cobra R$ 120,00 de taxa de arte mais R$ 0,35 por cartaz impresso. A gráfica Q não cobra "
                         "taxa, mas cobra R$ 0,50 por cartaz. O menor número de cartazes para o qual a gráfica P fica mais "
                         "barata que a Q é", a0)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0, align="left")
    cues_in = {L: C[f"21.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"23.x{L.lower()}"] for L in "ABCD"}
    K.alternativas(c, t, C, ALTS2, 1000, 260, 680, 34, C["22.ok"], "E", cues_in, cues_x, gap=34)
    pause_timer(c, t, C["21.end"] - 1.9, 540, yend + 100)
    if t >= C["22"]:
        ap = ep(t, C["22"], 0.4)
        _painel(c, ap)
        text(c, "MAIS BARATA → inequação", 550, 285, 26, "black", PURPLE, ap)
        rows = [(C["22.a"], "120 + 0,35n < 0,5n", "", None), (C["22.a"] + 4.2, "120 < 0,15n", "", None),
                (C["22.a"] + 6.4, "n > 800", "", None)]
        _passos(c, t, rows, 230, 360, 44, 72)
        ab = ep(t, C["22.b"], 0.4)
        if ab > 0:
            rrect(c, 200, 570, 700, 100, 18, mix("#FFFFFF", GREEN, 0.12), ab)
            text(c, "ATALHO · sem taxa em Q", 240, 602, 18, "black", GREEN, ab, align="left", tracking=2)
            text(c, "120 ÷ (0,50 − 0,35) = 120 ÷ 0,15 = 800", 550, 650, 28, "black", INK, ab)
        acc = ep(t, C["22.c"], 0.4)
        if acc > 0:
            rrect(c, 200, 690, 700, 120, 18, mix("#FFFFFF", GREEN, 0.10), acc)
            text(c, "800: P = R$ 400,00 · Q = R$ 400,00 (empate)", 550, 735, 24, "black", PURPLE, acc)
            text(c, "801: P = R$ 400,35 · Q = R$ 400,50", 550, 785, 24, "black", GREEN, acc)


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "REVISÃO", PURPLE)
    itens = [("25.a", "juntamos tudo", BLUE), ("25.b", "caçamos as pegadinhas", AMBER),
             ("25.c", "equações na Física e nos juros", PURPLE)]
    for k, (cue, s, col) in enumerate(itens):
        a, d = rise(t, C[cue])
        y = 330 + k * 150 + d
        badge_num(c, k + 1, 520, y - 14, a, 32, bg=col)
        text(c, s, 580, y, 52, "black", INK, a, align="left")
    ac = ep(t, C["25.c"], 0.5)
    if ac > 0:
        linha(c, [("M = C(1 + it)", PURPLE), ("    ·    ", GRAY), ("v = v₀ + at", PURPLE)], W / 2, 790, 40, ac)


def b_cta(c, t, C, B):
    cta(c, t, C["26.like"], C["26.sub"], C["26.bell"], C["26.com"], C["26.bye"],
        "Qual plano você já escolheu sem fazer essa conta?", canal="no Estudativo", anki=C["26.anki"])


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, locadoras=b_locadoras, corrida=b_corrida,
              equacao=b_equacao, inequacao=b_inequacao, leitura=b_leitura, atalho=b_atalho, mesmatarifa=b_mesmatarifa,
              exercicio=b_exercicio, recap=b_recap, erros=b_erros, q1=b_q1, q2=b_q2, ponte=b_ponte, cta=b_cta)
