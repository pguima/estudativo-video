"""Visual — Empréstimos, Financiamentos e Parcelamentos, Episódio 5: Revisão geral, pegadinhas e treino (tema claro).
Peças comuns da série em ../../comum.py (reexporta o 019/comum.py: alternativas, pause_timer, selo, chip...).
Índice visual da revisão: os 4 ícones dos episódios (icone()): guichê de câmbio · etiqueta partida · fatias da dívida
com a escadinha dos juros · caixa da Price. Guichê e moedinha no mesmo traço do visual.py do ep1.
Em cada questão inédita, uma LINHA DO TEMPO em miniatura (mini_linha()).
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
_s = importlib.util.spec_from_file_location("comum032", _p)
K = importlib.util.module_from_spec(_s); _s.loader.exec_module(K)
K.usar_tempos(Path(__file__).resolve().parents[1] / "audio" / "tempos.json")
motor.set_theme("claro")
frame, head_seq, which, para, boxed, selo, pause_timer, chip = (K.frame, K.head_seq, K.which, K.para, K.boxed, K.selo,
                                                                 K.pause_timer, K.chip)
fmid, ftext = K.fmid, K.ftext

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_emprestimos_ep5_revisao.mp4"
CARD_R = K.CARD_R
OURO = "#F4C542"
JURO = "#F08A3C"   # laranja dos juros (como no ep4)


def ftw(s, size, peso="black"):
    return K.ftext_w(s, peso, size)


# ======================================================================
# peças (mesmo traço dos episódios 1–4)
# ======================================================================

def moeda(c, x, y, r, s, col, a):
    """moedinha dourada com o valor (ep1)"""
    if a <= 0:
        return
    c.drawCircle(x, y + 5, r, paint("#000000", a * 0.10))
    c.drawCircle(x, y, r, paint(OURO, a))
    c.drawCircle(x, y, r - 7, paint(mix(OURO, "#FFFFFF", 0.45), a))
    c.drawCircle(x, y, r, paint(col, a, stroke=6))
    text(c, "R$", x, y - r * 0.22, r * 0.36, "black", INK2, a)
    text(c, s, x, y + r * 0.42, r * 0.44, "black", INK, a)


def guiche(c, x, y, fator, a, col=None):
    """guichê de câmbio (ep1): casinha com o letreiro "÷ fator" """
    if a <= 0:
        return
    col = col or PURPLE
    rrect(c, x - 70, y - 62, 140, 124, 14, mix("#FFFFFF", col, 0.10), a)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x - 70, y - 62, 140, 124), 14, 14), paint(col, a, stroke=4))
    rrect(c, x - 82, y - 86, 164, 34, 10, col, a)
    text(c, "CÂMBIO", x, y - 61, 20, "black", "#FFFFFF", a, tracking=2)
    text(c, "÷ " + fator, x, y + 14, 30, "black", col, a)


def etiqueta_partida(c, cx, cy, a, w=300, h=150):
    """etiqueta partida ao meio (ep2): a ENTRADA fica, a PARCELA viaja"""
    if a <= 0:
        return
    for k, (s1, col) in enumerate((("ENTRADA", BLUE), ("PARCELA", AMBER))):
        x = cx - w / 2 - 14 + k * (w / 2 + 28)
        rrect(c, x, cy - h / 2, w / 2, h, 18, "#FFF7E0", a, shadow=True, stroke=4, stroke_color=col)
        text(c, s1, x + w / 4, cy + 8, 22, "black", col, a)
    arrow(c, cx + w / 4 + 14, cy + h / 2 + 18, cx + w / 4 + 104, cy + h / 2 + 18, AMBER, a, 4, 12)
    text(c, "fica", cx - w / 4 - 14, cy + h / 2 + 30, 22, "bold", BLUE, a)


def fatias(c, cx, cy, a, n=5, w=340, h=56):
    """ep3: a dívida em fatias iguais (azul) e a escadinha dos juros (laranja) por cima"""
    if a <= 0:
        return
    fw_ = w / n
    x0 = cx - w / 2
    for k in range(n):
        x = x0 + k * fw_
        rrect(c, x + 3, cy, fw_ - 6, h, 8, mix("#FFFFFF", BLUE, 0.55), a)
        hj = 22 * (n - k)
        rrect(c, x + 10, cy - hj - 6, fw_ - 20, hj, 6, JURO, a * 0.9)


def caixa_price(c, cx, cy, a, n=5, w=340, h=150):
    """ep4: a parcela é uma caixa de tamanho fixo; dentro, o juro (laranja) encolhe e a amortização (azul) cresce"""
    if a <= 0:
        return
    fw_ = w / n
    x0 = cx - w / 2
    for k in range(n):
        x = x0 + k * fw_
        hj = h * (0.45 - 0.08 * k)
        rrect(c, x + 4, cy - h / 2, fw_ - 8, h, 8, mix("#FFFFFF", BLUE, 0.55), a)
        rrect(c, x + 4, cy - h / 2, fw_ - 8, hj, 8, JURO, a * 0.9)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x + 4, cy - h / 2, fw_ - 8, h), 8, 8), paint(INK2, a, stroke=3))


def icone(c, k, cx, cy, s=1.0, a=1.0):
    """os 4 ícones da série (índice da revisão), em escala s em volta de (cx, cy)"""
    if a <= 0:
        return
    c.save(); c.translate(cx, cy); c.scale(s, s)
    if k == 0:      # ep1 guichê de câmbio
        moeda(c, -120, 0, 48, "1.210", PURPLE, a)
        arrow(c, -64, 0, -14, 0, INK2, a, 4, 12)
        guiche(c, 70, 10, "1,21", a)
    elif k == 1:    # ep2 etiqueta partida
        etiqueta_partida(c, 0, -10, a)
    elif k == 2:    # ep3 fatias + escadinha
        fatias(c, 0, 10, a)
    elif k == 3:    # ep4 caixa da Price
        caixa_price(c, 0, 0, a)
    c.restore()


def mini_linha(c, x0, x1, y, n, marcas, a, pagos=0):
    """linha do tempo em miniatura: marcas = [(data, valor em cima, rótulo embaixo, cor)]; pagos = datas 1..pagos verdes"""
    if a <= 0:
        return
    line(c, x0 - 20, y, x1 + 20, y, INK2, a, 4)
    passo = (x1 - x0) / n
    dic = {m[0]: m for m in marcas}
    for k in range(n + 1):
        x = x0 + k * passo
        col = GREEN if 1 <= k <= pagos else (dic[k][3] if k in dic else LIGHT)
        c.drawCircle(x, y, 9 if k in dic else 6, paint(col, a))
        if k in dic:
            _, cima, baixo, colm = dic[k]
            if cima:
                sz = 26
                while ftw(cima, sz) > max(passo * 2.2, 120):
                    sz -= 1
                fmid(c, cima, x, y - 30, sz, "black", colm, a)
            if baixo:
                text(c, baixo, x, y + 38, 19, "bold", GRAY, a)
    if pagos:
        xm = x0 + (pagos + 1) / 2 * passo
        text(c, f"{pagos} fatias pagas", xm, y + 38, 19, "black", GREEN, a)


def anuncio(c, cx, cy, a, w=560, h=320, carimbo=0.0):
    """cartaz '5× SEM JUROS' (ep2) com a letrinha do à vista"""
    if a <= 0:
        return
    rrect(c, cx - w / 2, cy - h / 2, w, h, 26, RED, a, shadow=True)
    text(c, "5×", cx, cy - 40, 110, "black", "#FFFFFF", a)
    text(c, "SEM JUROS!", cx, cy + 46, 58, "black", "#FFE680", a)
    text(c, "ou R$ 1.350,00 à vista", cx + w / 2 - 24, cy + h / 2 - 22, 22, "bold", "#FFFFFF", a, align="right")
    if carimbo > 0:
        selo(c, cx, cy + h / 2 + 50, a * carimbo, "PREÇO COM FANTASIA", AMBER, -6, 34)


def conferido(c, s, x, y, a, ok=True, size=30):
    if a <= 0:
        return
    check_icon(c, x, y - size * 0.32, size * 0.62, a, GREEN if ok else RED, "check" if ok else "x")
    ftext(c, s, x + size * 0.95, y, size, "black", GREEN if ok else RED, a, align="left")


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "REVISÃO FINAL", BLUE)
    aa = ep(t, C["01.a"], 0.5)
    ab = ep(t, C["01.b"], 0.5)
    anuncio(c, 640, 470, aa, carimbo=ab)
    if aa > 0:
        text(c, "toda compra a prazo", 1340, 380, 40, "black", INK, aa)
        text(c, "é um EMPRÉSTIMO DISFARÇADO", 1340, 440, 40, "black", RED, aa)
    if ab > 0:
        boxed(c, 1050, 520, 580, 110, GREEN, ab, 0.08)
        text_mid(c, "preço real: o À VISTA", 1340, 575, 38, "black", GREEN, ab)
    ac = ep(t, C["01.c"], 0.5)
    chip(c, "9 FRASES", 800, 800, AMBER, ac, 36)
    chip(c, "5 QUESTÕES", 1120, 800, GREEN, ep(t, C["01.c"] + 0.6, 0.4), 36)


COBRA = [("02.a", "TAXA ESCONDIDA", "entrada + uma parcela", 1, AMBER),
         ("02.b", "VALOR HOJE", "parcelas futuras · quitação", 0, PURPLE),
         ("02.c", "JURO × AMORTIZAÇÃO", "SAC e Price", 3, BLUE),
         ("02.d", "DÍVIDA QUE CRESCE", "cartão · cheque especial", None, RED)]


def b_cobra(c, t, C, B):
    frame(c, t, B["start"], "SEÇÃO 01", "O QUE A PROVA COBRA", BLUE)
    for k, (cue, tit, sub, ic, col) in enumerate(COBRA):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        x = 330 + k * 420
        rrect(c, x - 190, 240 + d, 380, 500, 24, mix("#F7F7F5", col, 0.08), a)
        if ic is not None:
            icone(c, ic, x, 420 + d, 0.82 if ic != 0 else 0.7, a)
        else:
            rrect(c, x - 120, 350 + d, 240, 150, 16, RED, a, shadow=True)
            rrect(c, x - 120, 380 + d, 240, 30, 0, INK, a * 0.85)
            text(c, "× 1,1 × 1,1 …", x, 470 + d, 28, "black", "#FFFFFF", a)
        text(c, tit, x, 620 + d, 30, "black", col, a)
        para(c, sub, x, 668 + d, 24, "bold", INK2, a, 340, 30, align="center")


INDICE = [("EP. 1", "câmbio entre datas · × para o futuro, ÷ para hoje · juro = aluguel"),
          ("EP. 2", "a entrada não viaja · o “sem juros” fantasiado"),
          ("EP. 3", "fatias iguais de dívida · a escadinha dos juros"),
          ("EP. 4", "Price: a caixa de tamanho fixo")]
IND_CUES = ["03.a", "03.b", "04.a", "04.b"]
IND_POS = [(560, 190), (1360, 190), (560, 505), (1360, 505)]


def b_indice(c, t, C, B):
    frame(c, t, B["start"], "ANTES DE COBRAR", "UMA FRASE POR EPISÓDIO", PURPLE)
    for k, (ep_, s) in enumerate(INDICE):
        a = ep(t, C[IND_CUES[k]], 0.5)
        if a <= 0:
            continue
        nxt = C[IND_CUES[k + 1]] if k + 1 < len(IND_CUES) else C["04.end"]
        on_ = 1.0 if C[IND_CUES[k]] - 0.05 <= t < nxt else 0.0
        x, y = IND_POS[k]
        rrect(c, x - 360, y, 720, 290, 22, mix("#F7F7F5", PURPLE, 0.10 * on_), a)
        if on_:
            c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x - 360, y, 720, 290), 22, 22), paint(PURPLE, a, stroke=4))
        pill(c, ep_, x - 330, y + 28, PURPLE if on_ else INK2, size=20, a=a, bounds=(0, 1920))
        icone(c, k, x - 165, y + 150, (0.62, 0.62, 0.7, 0.62)[k], a)
        lns = s.split(" · ")
        for j, ln in enumerate(lns):
            sz = 26
            while text_w(ln, "black", sz) > 310:
                sz -= 1
            text(c, ln, x + 190, y + 150 + (j - (len(lns) - 1) / 2) * 38, sz, "black", INK if on_ else INK2, a)


ONDE = [("05.a", "CASA PRÓPRIA", "SAC", BLUE), ("05.b", "CREDIÁRIO", "Price", BLUE),
        ("05.c", "CARTÃO · CHEQUE ESPECIAL", "juros compostos", RED), ("05.d", "SOMA DOS JUROS DO SAC", "Progressão aritmética", PURPLE),
        ("05.e", "À VISTA OU A PRAZO?", "próxima série", GREEN)]


def b_onde(c, t, C, B):
    frame(c, t, B["start"], "NA VIDA E NAS OUTRAS SÉRIES", "ONDE ISSO APARECE", BLUE)
    for k, (cue, tit, sub, col) in enumerate(ONDE):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        x = 300 + k * 330
        rrect(c, x - 150, 260 + d, 300, 420, 24, mix("#F7F7F5", col, 0.08), a)
        para(c, tit, x, 360 + d, 28, "black", INK, a, 260, 36, align="center")
        boxed(c, x - 125, 520 + d, 250, 90, col, a, 0.12)
        sz = 30
        while text_w(sub, "black", sz) > 230:
            sz -= 1
        text_mid(c, sub, x, 565 + d, sz, "black", col, a)


def b_habitos(c, t, C, B):
    frame(c, t, B["start"], "ESTRATÉGIA DE PROVA", "TRÊS HÁBITOS", GREEN)
    cues = ("06.a", "06.b", "06.c")
    for k in range(3):
        a, d = rise(t, C[cues[k]])
        if a <= 0:
            continue
        x = 400 + k * 560
        col = (GREEN, PURPLE, BLUE)[k]
        rrect(c, x - 250, 230 + d, 500, 540, 24, mix("#F7F7F5", col, 0.08), a)
        badge_num(c, k + 1, x, 290 + d, a, 30, bg=col)
        if k == 0:
            mini_linha(c, x - 170, x + 170, 450 + d, 2, [(0, "entrada", "hoje", BLUE), (2, "parcela", "depois", PURPLE)], a)
            text(c, "DESENHE A", x, 600 + d, 32, "black", col, a)
            text(c, "LINHA DO TEMPO", x, 645 + d, 32, "black", col, a)
            text(c, "10 segundos", x, 715 + d, 26, "bold", INK2, a)
        elif k == 1:
            fmid(c, "?", x, 440 + d, 140, "black", col, a)
            text(c, "QUANTO SE DEVE", x, 600 + d, 32, "black", col, a)
            text(c, "AGORA?", x, 645 + d, 32, "black", col, a)
            text(c, "juros só sobre o saldo", x, 715 + d, 26, "bold", INK2, a)
        else:
            fatias(c, x - 105, 450 + d, a, n=4, w=180, h=40)
            caixa_price(c, x + 110, 430 + d, a, n=4, w=180, h=110)
            text(c, "SAC: 1ª LINHA", x, 600 + d, 32, "black", col, a)
            text(c, "PRICE: O FATOR", x, 645 + d, 32, "black", col, a)
            text(c, "o fator vem no enunciado", x, 715 + d, 26, "bold", INK2, a)


# ======================================================================
# verdadeiro ou falso
# ======================================================================

def b_vf_intro(c, t, C, B):
    frame(c, t, B["start"], "PAUSE E RESPONDA", "VERDADEIRO OU FALSO?", AMBER)
    a0 = ep(t, C["07"], 0.5)
    chip(c, "V", 820, 360, GREEN, a0, 90)
    fmid(c, "ou", W / 2, 360, 50, "black", GRAY, a0)
    chip(c, "F", 1100, 360, RED, a0, 90)
    aa = ep(t, C["07.a"], 0.5)
    for k in range(9):
        badge_num(c, k + 1, W / 2 - 4 * 90 + k * 90, 560, ep(t, C["07.a"] + 0.12 * k, 0.3), 30, bg=INK2)
    text(c, "os erros que mais custam pontos", W / 2, 650, 32, "bold", INK2, aa)
    pill(c, "pause ANTES da resposta", W / 2, 750, AMBER, size=30, a=ep(t, C["07.b"], 0.5), anchor="center")


# (contexto, afirmação, verdadeira?, por que engana, regra certa, versão certa, ícone)
VF = [
    ("entrada + parcela", "800 à vista ou 300 + 560: taxa = 60 ÷ 800", False, "800 é o preço do produto",
     "a entrada não viaja: divida pelo financiado", "60 ÷ 500 = 12%", 1),
    ("“sem juros”", "6 × 100 ou 540 à vista: tem juros", True, "o cartaz jura que não tem",
     "o preço real é o à vista", "600 − 540 = 60 de juros", 1),
    ("datas diferentes", "550 (1 mês) + 605 (2 meses) = 1.155 hoje", False, "a soma está certa",
     "cada parcela passa pelo câmbio", "500 + 500 = 1.000", 0),
    ("trazer a hoje", "cada parcela ÷ o fator do SEU prazo", True, "dá vontade de usar um prazo só",
     "1 mês: ÷ 1,1 · 2 meses: ÷ 1,21", "cada uma pelo seu prazo", 0),
    ("saldo devedor", "SAC de 6.000 a 2%: pagou 1.120, deve 4.880", False, "você pagou 1.120",
     "120 eram aluguel: só a amortização abate", "6.000 − 1.000 = 5.000", 2),
    ("juros do SAC", "juros de 120 todo mês, nas 6 parcelas", False, "a taxa é sempre a mesma",
     "o saldo cai: os juros descem a escadinha", "120 + 100 + … + 20 = 420", 2),
    ("Price", "na Price, a amortização é constante", False, "alguma coisa é constante",
     "na Price, constante é a parcela (a caixa)", "fatias iguais = SAC", 3),
    ("SAC × Price", "mesma taxa e prazo: SAC paga menos juros", True, "a taxa é igual",
     "no SAC o saldo cai mais depressa", "saldo menor → juro menor", 3),
    ("rotativo", "2 meses a 10%: dívida × 1,20", False, "10 + 10 = 20",
     "juros compostos: 1,1 × 1,1", "× 1,21", 0),
]
VF_IDS = [f"{8 + k:02d}" for k in range(9)]


def b_vf(c, t, C, B):
    sid = which(t, C, VF_IDS)
    n = VF_IDS.index(sid)
    ctx, conta, ver, engana, regra_, fix, ic = VF[n]
    head(c, t, C[sid], f"VERDADEIRO OU FALSO? · {n + 1} DE 9", "PAUSE E RESPONDA", AMBER)
    card(c, *CARD_R)
    q = lambda x: C[f"{sid}.{x}"]
    for k in range(9):
        badge_num(c, k + 1, W / 2 - 4 * 66 + k * 66, 200, 1, 20, bg=AMBER if k == n else LIGHT)
    a0 = ep(t, q("t"), 0.5)
    icone(c, ic, 330, 420, 0.62, a0)
    text(c, ctx.upper(), 960, 310, 30, "black", INK2, a0)
    ar = ep(t, q("r"), 0.4)
    sz = 50
    while ftw(conta, sz) > 800:
        sz -= 2
    fmid(c, conta, 980, 410, sz, "black", INK, a0)
    if ar > 0 and not ver:
        w = ftw(conta, sz)
        strike(c, 980 - w / 2 - 10, 415, 980 + w / 2 + 10, 415, ar, RED, ar)
    pause_timer(c, t, q("p"), 1660, 410, a=1 - ar)
    selo(c, 1640, 470, ar, "VERDADEIRO" if ver else "FALSO", GREEN if ver else RED, -6, 40)
    ae = ep(t, q("e"), 0.5)
    if ae > 0:
        if ver:
            pill(c, "PARECE FALSO PORQUE...", 230, 560, AMBER, size=26, a=ae, bounds=(0, 1920))
        else:
            selo(c, 350, 560, ae, "PEGADINHA", AMBER, -5, 30)
        text(c, engana, 640 if ver else 520, 572, 34, "bold", INK2, ae, align="left")
    ag = ep(t, q("g"), 0.5)
    if ag > 0:
        boxed(c, 200, 640, 1520, 170, GREEN, ag, 0.07)
        para(c, regra_, 240, 710, 30, "black", GREEN, ag, 760)
        szf = 42
        while ftw(fix, szf) > 600:
            szf -= 2
        fmid(c, fix, 1340, 725, szf, "black", GREEN, ag)


def b_vf_placar(c, t, C, B):
    frame(c, t, B["start"], "QUANTAS VOCÊ ACERTOU?", "O PLACAR", AMBER)
    aa = ep(t, C["17.a"], 0.5)
    for k, v in enumerate(VF):
        a = aa * ep(t, C["17.a"] + 0.12 * k, 0.3)
        x = W / 2 - 4 * 150 + k * 150
        badge_num(c, k + 1, x, 260, a, 26, bg=INK2)
        chip(c, "V" if v[2] else "F", x, 360, GREEN if v[2] else RED, a, 50)
    text(c, "6 falsas · 3 verdadeiras", W / 2, 490, 40, "black", INK, aa)
    ab = ep(t, C["17.b"], 0.5)
    chip(c, "AGORA: 5 QUESTÕES INÉDITAS", W / 2, 620, GREEN, ab, 44)
    text(c, "desenhe a linha do tempo antes da conta", W / 2, 740, 32, "black", PURPLE, ab)


# ======================================================================
# as 5 questões inéditas
# ======================================================================
# enun: (cue, texto, destaque?) · linha: (n, marcas, pagos) · passos: (cue, texto) · confere: (cue, texto)

Q = {
    "q1": dict(ids=("18", "19"), titulo="ENTRADA + UMA PARCELA", ok="E", asz=34,
               enun=[("a", "Um celular custa R$ 2.400,00 à vista, ou R$ 1.000,00 de entrada mais R$ 1.540,00 em 30 dias.",
                      False), ("b", "A taxa mensal de juros do parcelamento é", True)],
               alts=[("A", "0%", "acreditou no anúncio", RED), ("B", "≈ 5,5%", "÷ 2.540 (a prazo)", AMBER),
                     ("C", "≈ 5,8%", "÷ 2.400 (à vista)", AMBER), ("D", "≈ 9,1%", "÷ 1.540 (parcela)", AMBER),
                     ("E", "10%", "", GREEN)],
               linha=(1, [(0, "1.000", "hoje", BLUE), (1, "1.540", "30 dias", PURPLE)], 0),
               passos=[("a", "financiado: 2.400 − 1.000 = 1.400"), ("b", "juros 140 → 140 ÷ 1.400 = 10%")],
               confere=("v", "a certa é a MAIOR candidata")),
    "q2": dict(ids=("20", "21"), titulo="A 5ª PARCELA DO SAC", ok="D", asz=34,
               enun=[("a", "Um empréstimo de R$ 24.000,00 é pago no SAC, em 12 parcelas, a 2% ao mês.", False),
                     ("b", "O valor da 5ª parcela é", True)],
               alts=[("A", "R$ 320,00", "só os juros", AMBER), ("B", "R$ 2.000,00", "só a fatia", AMBER),
                     ("C", "R$ 2.280,00", "tirou 5 fatias", RED), ("D", "R$ 2.320,00", "", GREEN),
                     ("E", "R$ 2.480,00", "juros sobre 24.000", RED)],
               linha=(6, [(0, "24.000", "hoje", BLUE), (5, "5ª ?", "", AMBER)], 4),
               passos=[("d", "fatia: 24.000 ÷ 12 = 2.000"), ("a", "saldo: 24.000 − 4 × 2.000 = 16.000"),
                       ("b", "2.000 + 2% × 16.000 = 2.320")],
               confere=None),
    "q3": dict(ids=("22", "23"), titulo="O SALDO NA PRICE", ok="B", asz=32,
               enun=[("a", "Um financiamento de R$ 8.000,00 na Price tem 12 parcelas de R$ 733,44, a 1,5% ao mês.",
                      False), ("b", "Depois da 1ª parcela, o saldo devedor é", True)],
               alts=[("A", "R$ 8.120,00", "somou os juros", RED), ("B", "R$ 7.386,56", "", GREEN),
                     ("C", "R$ 7.333,33", "fatia do SAC", AMBER), ("D", "R$ 7.266,56", "abateu a parcela toda", RED),
                     ("E", "R$ 613,44", "é a amortização", AMBER)],
               linha=(4, [(0, "8.000", "hoje", BLUE), (1, "733,44", "mês 1", PURPLE)], 0),
               passos=[("d", "deve agora: 8.000"), ("a", "juros: 1,5% × 8.000 = 120"),
                       ("b", "amortização: 733,44 − 120 = 613,44"), ("b", "saldo: 8.000 − 613,44 = 7.386,56")],
               confere=None),
    "q4": dict(ids=("24", "25"), titulo="O CHEQUE ESPECIAL", ok="C", asz=34,
               enun=[("a", "Uma conta fica com saldo negativo de R$ 1.000,00 no cheque especial, a 8% ao mês, por 2 "
                      "meses, sem nenhum pagamento.", False), ("b", "A dívida passa a ser", True)],
               alts=[("A", "R$ 1.080,00", "um mês só", AMBER), ("B", "R$ 1.160,00", "juros simples", RED),
                     ("C", "R$ 1.166,40", "", GREEN), ("D", "R$ 1.259,71", "um mês a mais", AMBER),
                     ("E", "R$ 2.166,40", "somou os 1.000", RED)],
               linha=(2, [(0, "−1.000", "hoje", RED), (2, "?", "2 meses", AMBER)], 0),
               passos=[("a", "1,08² = 1,1664"), ("b", "1.000 × 1,1664 = 1.166,40")],
               confere=("v", "um pouco acima do simples (1.160)")),
    "q5": dict(ids=("26", "27"), titulo="O “SEM JUROS”", ok="A", asz=27,
               enun=[("a", "Uma TV custa 5 × R$ 300,00 “sem juros” ou R$ 1.350,00 à vista.", False),
                     ("b", "Qual afirmação é correta?", True)],
               alts=[("A", "Há R$ 150,00 de juros embutidos; o preço real é R$ 1.350,00.", "", GREEN),
                     ("B", "Não há juros, pois o anúncio diz “sem juros”.", "", RED),
                     ("C", "Não há juros, pois o total parcelado é igual à etiqueta.", "", RED),
                     ("D", "O preço real é R$ 1.500,00, e o desconto à vista é de 15%.", "", AMBER),
                     ("E", "Há R$ 150,00 de juros, mas só para quem atrasa.", "", AMBER)], aw=560,
               fora={"B": ("acreditou no cartaz", RED), "C": ("comparou com a etiqueta", RED),
                     "D": ("preço real errado", AMBER), "E": ("juros ≠ multa", AMBER)},
               linha=(5, [(0, "1.350", "à vista", BLUE)] + [(k, "300", "", PURPLE) for k in range(1, 6)], 0),
               passos=[("d", "preço real = à vista"), ("a", "1.500 − 1.350 = 150 de juros")],
               confere=None),
}


def faz_questao(nome):
    d = Q[nome]
    s1, s2 = d["ids"]
    num = int(nome[1])

    def bloco(c, t, C, B):
        head(c, t, B["start"], f"QUESTÃO {num} DE 5 · INÉDITA", d["titulo"], BLUE)
        card(c, *CARD_R)
        a0 = ep(t, C[s1], 0.5)
        pill(c, "QUESTÃO EXTRA DA SÉRIE (ESTILO ENEM)", 180, 200, BLUE, size=20, a=a0, bounds=(0, 1920))
        text(c, "Situação hipotética, elaborada para fins didáticos.", 180, 828, 18, "medium", GRAY, a0, align="left")
        sol = ep(t, C[s2], 0.5)
        cues_in = {L: C[f"{s1}.l{L.lower()}"] for L in "ABCDE"}
        cues_x = {L: C[f"{s2}.x{L.lower()}"] for L in "ABCDE" if L != d["ok"]}
        y = 280
        for cue, s, dest in d["enun"]:
            a = ep(t, C[f"{s1}.{cue}"], 0.4) * (1 - sol)
            h = para(c, s, 180, y + 22, 30, "black" if dest else "bold", BLUE if dest else INK, a, 600, 40)
            y += h + 18
        pause_timer(c, t, C[f"{s1}.end"] - 1.9, 500, 760)
        aw = d.get("aw", 820)
        K.alternativas(c, t, C, d["alts"], 880, 230, aw, d["asz"], C[f"{s2}.ok"], d["ok"], cues_in, cues_x, gap=14)
        if d.get("fora"):   # motivos fora da lista, à direita (as alternativas da Q5 são frases longas)
            yy_ = 230
            for L, s_, _, _ in d["alts"]:
                hh = len(K.wrap(s_, "bold", d["asz"], aw - 70)) * (d["asz"] + 8) + 10
                if L in d["fora"]:
                    why, colw = d["fora"][L]
                    pill(c, why, 1500, yy_ + hh / 2, colw, size=20, a=ep(t, cues_x[L], 0.4), bounds=(0, 1920))
                yy_ += hh + 14
        if sol > 0:
            ad = ep(t, C[f"{s2}.d"], 0.4) * sol
            if ad > 0:
                boxed(c, 160, 240, 670, 170, PURPLE, ad, 0.06)
                pill(c, "LINHA DO TEMPO", 180, 240, PURPLE, size=18, a=ad, bounds=(0, 1920))
                n, marcas, pagos = d["linha"]
                mini_linha(c, 240, 750, 335, n, marcas, ad, pagos)
            yy = 470
            for j, (cue, s) in enumerate(d["passos"]):
                a = ep(t, C[f"{s2}.{cue}"], 0.4) * sol
                last = j == len(d["passos"]) - 1
                sz = 34
                while ftw(s, sz) > 640:
                    sz -= 2
                ftext(c, s, 180, yy, sz, "black", GREEN if last else INK, a, align="left")
                yy += 62
            if d["confere"]:
                cue, s = d["confere"]
                conferido(c, s, 190, yy + 6, ep(t, C[f"{s2}.{cue}"], 0.4) * sol, True, 28)
            result_box(c, f"Letra {d['ok']}", 1290, 760, 38, ep(t, C[f"{s2}.ok"], 0.5), GREEN)
    return bloco


# ======================================================================
# checklist, meta, ponte e CTA
# ======================================================================

CHECK = [("28.b", "EP. 1", ["levar e trazer com o fator", "parcelas: cada uma pelo seu prazo", "quitação antecipada",
                            "rotativo: juros compostos"]),
         ("28.c", "EP. 2", ["valor financiado", "taxa de entrada + parcela", "os juros do “sem juros”"]),
         ("29.a", "EP. 3", ["saldo · juros · amortização", "a tabela do SAC", "qualquer parcela sem montar todas",
                            "juros do SAC somados em PA"]),
         ("29.b", "EP. 4", ["Price com o fator dado", "SAC × Price"])]


def b_checklist(c, t, C, B):
    frame(c, t, B["start"], "CHECKLIST DE DOMÍNIO", "MARQUE SÓ O QUE EXPLICA EM VOZ ALTA", GREEN)
    aa = ep(t, C["28.a"], 0.5) * (1 - ep(t, C["28.b"], 0.4))
    pill(c, "explicar em voz alta, sem consultar nada", W / 2, 470, GREEN, size=34, a=aa, anchor="center")
    for k, (cue, ep_, itens) in enumerate(CHECK):
        a = ep(t, C[cue], 0.5)
        if a <= 0:
            continue
        col_ = 0 if k < 2 else 1
        x = 170 if col_ == 0 else 990
        y0 = 190 + sum(len(CHECK[j][2]) * 46 + 34 for j in range(0 if col_ == 0 else 2, k))
        pill(c, ep_, x, y0 + 18, PURPLE, size=20, a=a, bounds=(0, 1920))
        for j, it in enumerate(itens):
            yy = y0 + 18 + j * 46
            rrect(c, x + 110, yy - 15, 30, 30, 7, "#FFFFFF", a, stroke=3, stroke_color=INK2)
            K.ftext(c, it, x + 158, yy + 10, 27, "bold", INK, a, align="left")
    ae = ep(t, C["29.c"], 0.5)
    if ae > 0:
        boxed(c, 990, 690, 720, 100, AMBER, ae, 0.10)
        text_mid(c, "não marcou? reveja o episódio", 1350, 740, 32, "black", INK, ae)


def b_meta(c, t, C, B):
    frame(c, t, B["start"], "ANTES DE DIZER “DOMINADO”", "A META", GREEN)
    aa = ep(t, C["30.a"], 0.5)
    ab = ep(t, C["30.b"], 0.5)
    for i in range(20):
        r_, k = divmod(i, 10)
        a = aa * ep(t, C["30.a"] + 0.04 * i, 0.2)
        ok = ab > 0 and i < 14
        x, y = 230 + k * 82, 240 + r_ * 86
        rrect(c, x, y, 66, 70, 12, mix("#E6E6E2", GREEN, ab if ok else 0), a)
        if ok:
            check_icon(c, x + 33, y + 35, 18, ab, "#FFFFFF")
        else:
            text_mid(c, str(i + 1), x + 33, y + 35, 24, "black", INK2, a)
    text(c, "20 questões", 1450, 290, 52, "black", INK, aa)
    text(c, "14 acertos = 70%", 1450, 380, 46, "black", GREEN, ab)
    ac = ep(t, C["30.c"], 0.5)
    if ac > 0:
        boxed(c, 230, 520, 1460, 250, AMBER, ac, 0.10)
        etiqueta_partida(c, 520, 625, ac, w=260, h=120)
        fatias(c, 1400, 650, ac, n=4, w=240, h=44)
        text_mid(c, "comece por", W / 2, 590, 30, "bold", INK2, ac)
        text_mid(c, "ENTRADA + PARCELA", W / 2, 645, 36, "black", INK, ac)
        text_mid(c, "e TABELA DO SAC", W / 2, 700, 36, "black", INK, ac)


def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "SÉRIE COMPLETA", "PRÓXIMO ASSUNTO", PURPLE)
    aa = ep(t, C["31.a"], 0.5)
    text(c, "PRÓXIMO ASSUNTO", W / 2, 250, 28, "black", GRAY, aa, tracking=2)
    text(c, "Comparação de propostas", W / 2, 330, 60, "black", PURPLE, aa)
    text(c, "e tomada de decisão", W / 2, 400, 48, "black", PURPLE, aa)
    ab = ep(t, C["31.b"], 0.5)
    pill(c, "fecha a Matemática Financeira", W / 2, 490, GREEN, size=30, a=ab, anchor="center")
    ac = ep(t, C["31.c"], 0.5)
    chip(c, "À VISTA", 700, 640, BLUE, ac, 40)
    fmid(c, "ou", 900, 640, 40, "black", GRAY, ac)
    chip(c, "PARCELADO", 1110, 640, AMBER, ac, 40)
    chip(c, "PLANO A × PLANO B", W / 2, 760, PURPLE, ep(t, C["31.c"] + 0.8, 0.4), 36)


def b_cta(c, t, C, B):
    cta(c, t, C["32.like"], C["32.sub"], C["32.bell"], C["32.com"], C["32.bye"], "Qual pegadinha te pegou?",
        canal="no Estudativo", anki=C["32.anki"])


BLOCKS = dict(hook=b_hook, cobra=b_cobra, indice=b_indice, onde=b_onde, habitos=b_habitos,
              vf_intro=b_vf_intro, vf=b_vf, vf_placar=b_vf_placar, q1=faz_questao("q1"), q2=faz_questao("q2"),
              q3=faz_questao("q3"), q4=faz_questao("q4"), q5=faz_questao("q5"), checklist=b_checklist, meta=b_meta,
              ponte=b_ponte, cta=b_cta)
