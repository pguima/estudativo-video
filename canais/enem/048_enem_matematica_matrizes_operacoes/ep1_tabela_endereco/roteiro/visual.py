"""Visual — Matrizes e Operações, Episódio 1: matriz é uma tabela com endereço (tema claro).
Peças comuns da série em ../../comum.py (reexporta o 019/comum.py: expr, alternativas, erro_cards, atalho...).
Peças deste episódio: matriz() (matriz com colchetes, cores e fundos por casa), ind() (a com índice embaixo),
cinema() (a sala com fileiras e poltronas, o cursor que percorre a fileira), pixels() (imagem 0/1 que inverte e transpõe).
Cores com função: azul = definição · roxo = regra/fórmula · âmbar = armadilha · verde = atalho/dica · vermelho = erro.
"""
import importlib.util
import math
import re
from pathlib import Path
import skia
import motor
motor.set_theme("claro")
from motor import *  # noqa
from aula import *  # noqa

_p = Path(__file__).resolve().parents[2] / "comum.py"
_s = importlib.util.spec_from_file_location("comum048", _p)
K = importlib.util.module_from_spec(_s); _s.loader.exec_module(K)
K.usar_tempos(Path(__file__).resolve().parents[1] / "audio" / "tempos.json")
motor.set_theme("claro")
fr = K.fr
frame, head_seq, which, para, boxed, regra, selo, pause_timer, chip = (K.frame, K.head_seq, K.which, K.para, K.boxed, K.regra,
                                                                        K.selo, K.pause_timer, K.chip)
fmid, ftext, ftext_w = K.fmid, K.ftext, K.ftext_w

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_matrizes_ep1_tabela_endereco.mp4"
CARD_R = K.CARD_R
PAPEL = K.PAPEL
POLT = "#D9DEE7"

G4 = [[0, 3, 1, 1], [2, 0, 3, 2], [0, 1, 0, 1], [1, 3, 1, 0]]          # Questão 1
D4 = [["0", "120", "x", "200"], ["120", "0", "90", "y"], ["150", "90", "0", "60"], ["200", "140", "60", "0"]]  # Questão 5
M34 = [[4, 7, 1, 5], [2, 6, 9, 8], [5, 3, 0, 2]]                        # cinema: a23 = 9, a32 = 3
LEI = [[1, 0, -1], [3, 2, 1]]                                          # aij = 2i − j
G3 = [[0, 3, 2], [1, 0, 0], [1, 2, 0]]                                 # gols, 3 times (exemplo nosso)
D3 = [["0", "80", "?"], ["80", "0", "50"], ["120", "50", "0"]]          # distâncias, 3 cidades (exemplo nosso)
FIG = [[1, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0], [1, 1, 1, 1, 0, 0],
       [0, 0, 0, 0, 0, 0]]


def sg(v):
    """número com o sinal de menos tipográfico"""
    if isinstance(v, str):
        return v
    return ("−" + str(-v)) if v < 0 else str(v)


def ssg(v):
    """saldo com sinal: +2, 0, −3"""
    return "0" if v == 0 else ("+" + str(v) if v > 0 else "−" + str(-v))


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


def ind_w(base, sub, size):
    return ftext_w(base, "black", size) + ftext_w(sub, "black", size * 0.6) + size * 0.04


def ind(c, base, sub, x, cy, size, col, a, align="left", sub_col=None):
    """letra com índice embaixo (a₂₃, d₁₃, g_ij): desenha base e o índice menor e mais baixo; devolve a largura"""
    if a <= 0:
        return ind_w(base, sub, size)
    w = ind_w(base, sub, size)
    x0 = x - w / 2 if align == "center" else (x - w if align == "right" else x)
    wb = ftext_w(base, "black", size)
    fmid(c, base, x0 + wb / 2, cy, size, "black", col, a)
    ws = ftext_w(sub, "black", size * 0.6)
    fmid(c, sub, x0 + wb + size * 0.04 + ws / 2, cy + size * 0.32, size * 0.6, "black", sub_col or col, a)
    return w


def colchete(c, x, y0, y1, a, lado=1, col=INK, sw=5):
    """colchete da matriz: lado = 1 (esquerdo) ou −1 (direito)"""
    if a <= 0:
        return
    d = 16 * lado
    p = skia.Path(); p.moveTo(x + d, y0); p.lineTo(x, y0); p.lineTo(x, y1); p.lineTo(x + d, y1)
    c.drawPath(p, paint(col, a, stroke=sw))


def matriz(c, M, cx, cy, cw, ch, a, size=None, cor=None, fundo=None, alfa=None, bcol=INK, lin=None, col=None, lsize=None,
           lcol=GRAY):
    """matriz M (lista de linhas) centrada em (cx, cy), casas cw × ch.
    cor/alfa/fundo = dicionários {(i, j): ...} com i, j a partir de 0 (fundo = (cor, alfa)).
    lin = rótulos à esquerda de cada linha; col = rótulos acima de cada coluna. Devolve (x0, y0, w, h)."""
    if a <= 0:
        return (0, 0, 0, 0)
    m, n = len(M), len(M[0])
    size = size or ch * 0.5
    w, h = n * cw, m * ch
    x0, y0 = cx - w / 2, cy - h / 2
    for (i, j), (fc, fa) in (fundo or {}).items():
        if fa > 0:
            rrect(c, x0 + j * cw + 4, y0 + i * ch + 4, cw - 8, ch - 8, 12, fc, a * fa)
    for i in range(m):
        for j in range(n):
            v = M[i][j]
            if v is None:
                continue
            aa = a * (alfa or {}).get((i, j), 1.0)
            fmid(c, sg(v), x0 + (j + 0.5) * cw, y0 + (i + 0.5) * ch, size, "black", (cor or {}).get((i, j), INK), aa)
    colchete(c, x0 - 6, y0 - 4, y0 + h + 4, a, 1, bcol)
    colchete(c, x0 + w + 6, y0 - 4, y0 + h + 4, a, -1, bcol)
    ls = lsize or max(18, size * 0.5)
    if lin:
        for i, s_ in enumerate(lin):
            fmid(c, s_, x0 - 30 - ftext_w(s_, "black", ls) / 2, y0 + (i + 0.5) * ch, ls, "black", lcol, a)
    if col:
        for j, s_ in enumerate(col):
            fmid(c, s_, x0 + (j + 0.5) * cw, y0 - 30, ls, "black", lcol, a)
    return (x0, y0, w, h)


def faixa(c, x, y, w, h, col, a, r=14):
    """faixa translúcida (linha ou coluna em destaque)"""
    if a <= 0:
        return
    rrect(c, x, y, w, h, r, col, 0.16 * a)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), r, r), paint(col, a, stroke=4))


def conferido(c, s, x, y, a, ok=True, size=32):
    if a <= 0:
        return
    check_icon(c, x, y - size * 0.32, size * 0.62, a, GREEN if ok else RED, "check" if ok else "x")
    ftext(c, s, x + size * 0.95, y, size, "black", GREEN if ok else RED, a, align="left")


def objeto(c, x, y, w, h, tit, sub, a, col=BLUE):
    if a <= 0:
        return
    rrect(c, x, y, w, h, 24, "#FFFFFF", a, shadow=True)
    rrect(c, x, y, w, 60, 24, col, a * 0.14)
    text(c, tit, x + w / 2, y + 42, 28, "black", col, a)
    text(c, sub, x + w / 2, y + h - 30, 28, "black", INK, a)


# --- cinema -----------------------------------------------------------------------------------------------------------

CIN = dict(x=220, y=330, sw=118, sh=104, nf=3, np=4)


def assento(f, p):
    """centro da poltrona p da fileira f (1-indexadas)"""
    return (CIN["x"] + (p - 0.5) * CIN["sw"], CIN["y"] + (f - 0.5) * CIN["sh"])


def cinema(c, a, acesos=None):
    """a sala: tela em cima, 3 fileiras × 4 poltronas; acesos = {(f, p): (cor, alfa)}"""
    if a <= 0:
        return
    x, y, sw_, sh_ = CIN["x"], CIN["y"], CIN["sw"], CIN["sh"]
    w = CIN["np"] * sw_
    rrect(c, x + 10, y - 110, w - 20, 26, 13, "#3C4250", a)
    text(c, "TELA", x + w / 2, y - 60, 22, "black", GRAY, a, tracking=4)
    for f in range(1, CIN["nf"] + 1):
        fmid(c, f"fileira {f}", x - 70, y + (f - 0.5) * sh_, 22, "black", BLUE, a)
        for p in range(1, CIN["np"] + 1):
            cx, cy = assento(f, p)
            colr = POLT
            ac = (acesos or {}).get((f, p))
            rrect(c, cx - 42, cy - 34, 84, 62, 14, colr, a)
            rrect(c, cx - 42, cy - 34, 84, 18, 9, mix(POLT, INK, 0.12), a)
            if ac and ac[1] > 0:
                rrect(c, cx - 42, cy - 34, 84, 62, 14, ac[0], a * ac[1])
    for p in range(1, CIN["np"] + 1):
        cx, _ = assento(CIN["nf"], p)
        text(c, f"poltrona {p}", cx, y + CIN["nf"] * sh_ + 30, 18, "black", GREEN, a)


def caminho(c, t, t0, f, p, a, col):
    """o cursor entra pela esquerda da fileira f e anda até a poltrona p; devolve o progresso (0 → 1)"""
    u = ease_io(clamp((t - t0) / (0.6 + 0.35 * p)))
    x_ini = CIN["x"] - 20
    xf, yf = assento(f, p)
    x = lerp(x_ini, xf, u)
    if a > 0 and u > 0:
        line(c, x_ini, yf + 40, x, yf + 40, col, a, 6)
        cursor(c, x, yf + 6, a, 1.0 if u >= 1 else 0.0)
    return u


# --- pixels -----------------------------------------------------------------------------------------------------------

def pixels(c, P, x, y, s, a, inv=0.0, numeros=0.0, transp=False, on=INK, off="#FFFFFF"):
    """imagem preto e branco: P = matriz de 0/1; inv (0 → 1) troca 1 por 0; numeros mostra o 0/1 de cada casa"""
    if a <= 0:
        return
    n = len(P)
    for i in range(n):
        for j in range(n):
            v = P[j][i] if transp else P[i][j]
            val = v if inv < 0.5 else 1 - v
            cc = mix(off, on, (v * (1 - inv) + (1 - v) * inv))
            rrect(c, x + j * s + 2, y + i * s + 2, s - 4, s - 4, 6, cc, a)
            if numeros > 0:
                text_mid(c, str(val), x + (j + 0.5) * s, y + (i + 0.5) * s, s * 0.42, "black",
                         "#FFFFFF" if cc != off and val == 1 else GRAY, a * numeros)
    c.drawRect(skia.Rect.MakeXYWH(x, y, n * s, n * s), paint("#C9CED6", a, stroke=2))


# ======================================================================
# abertura
# ======================================================================

TIMES4 = ["time 1", "time 2", "time 3", "time 4"]
CONTRA4 = ["vs 1", "vs 2", "vs 3", "vs 4"]


def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "MATRIZES", BLUE)
    aa = ep(t, C["01.a"], 0.5)
    cx, cy, cw, ch = 560, 500, 110, 92
    x0, y0, w, h = cx - 2 * cw, cy - 2 * ch, 4 * cw, 4 * ch
    ab = ep(t, C["01.b"], 0.5)
    acc = ep(t, C["01.c"], 0.5)
    if aa > 0:
        faixa(c, x0 - 6, y0 + 2 * ch + 4, w + 12, ch - 8, BLUE, ab * (1 - acc))
        faixa(c, x0 + 2 * cw + 4, y0 - 6, cw - 8, h + 12, AMBER, ab * (1 - acc) + acc)
        faixa(c, x0 - 6, y0 + 2 * ch + 4, w + 12, ch - 8, RED, acc)
        matriz(c, G4, cx, cy, cw, ch, aa, 46, lin=TIMES4, col=CONTRA4, lsize=24)
    if ab > 0:
        rrect(c, 1080, 290, 620, 210, 24, "#FFFFFF", ab, shadow=True)
        text(c, "TIME 3", 1390, 340, 28, "black", INK2, ab)
        linha(c, [("marcou 2", BLUE), ("  ·  ", GRAY), ("sofreu 5", AMBER)], 1390, 390, 36, ab)
        linha(c, [("saldo  ", INK), ("−3", RED)], 1390, 460, 50, ab)
        pill(c, "o PIOR saldo", 1390, 540, RED, size=26, a=ab, anchor="center")
    if acc > 0:
        rrect(c, 1080, 600, 620, 150, 24, mix("#FFFFFF", AMBER, 0.10), acc)
        linha(c, [("coluna − linha  =  ", INK), ("+3", AMBER)], 1390, 650, 40, acc)
        text(c, "\"LÍDER\"", 1390, 720, 34, "black", AMBER, acc)
    ad = ep(t, C["01.d"], 0.5)
    if ad > 0:
        selo(c, 960, 800, ad, "A CONTA CERTA · A LEITURA ERRADA", RED, -2, 30)


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "AO FINAL DESTA AULA", "VOCÊ VAI CONSEGUIR", GREEN)
    rows = [("02.a", "ler qualquer tabela em forma de matriz", "sem trocar o endereço: linha primeiro"),
            ("02.b", "reconhecer os tipos de matriz", "quadrada · identidade · transposta · simétrica...")]
    for j, (cue, s, sub) in enumerate(rows):
        a, d = rise(t, C[cue])
        y = 360 + j * 220 + d
        check_icon(c, 300, y - 14, 34, a, GREEN)
        text(c, s, 360, y, 48, "black", INK, a, align="left")
        text(c, sub, 360, y + 60, 34, "bold", GRAY, a, align="left")


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "UM LEMBRETE", "CONTA COM SINAL", GREEN)
    aa = ep(t, C["03.a"], 0.5)
    if aa > 0:
        text(c, "série de Operações e conjuntos numéricos", W / 2, 260, 26, "bold", GRAY, aa)
        linha(c, [("2 − 5 = ", INK), ("−3", RED)], W / 2, 360, 90, aa)
        x0, x1, y = 420, 1500, 560
        line(c, x0, y, x1, y, INK2, aa, 4)
        step = (x1 - x0) / 9
        for k in range(10):
            v = k - 5
            xx = x0 + k * step
            line(c, xx, y - 14, xx, y + 14, INK2, aa, 3)
            fmid(c, sg(v), xx, y + 50, 28, "black", RED if v == -3 else (BLUE if v == 2 else INK2), aa)
        g = ep(t, C["03.a"] + 1.5, 1.6)
        xs = x0 + 7 * step
        xe = lerp(xs, x0 + 2 * step, g)
        if g > 0:
            arrow(c, xs, y - 50, xe, y - 50, AMBER, aa, 6, 18)
            pill(c, "tirou 5", (xs + xe) / 2, y - 100, AMBER, size=24, a=aa * g, anchor="center")
        c.drawCircle(xs, y, 14, paint(BLUE, aa))
        if g >= 1:
            c.drawCircle(xe, y, 14, paint(RED, aa))
    ab = ep(t, C["03.b"], 0.5)
    if ab > 0:
        pill(c, "saldo de gols pode ser NEGATIVO", W / 2, 750, BLUE, size=30, a=ab, anchor="center")


def tabelinha(c, x, y, a, linhas_, cols, cw=70, ch=40, size=20, cores=None):
    """mini tabela para os objetos do concreto"""
    if a <= 0:
        return
    for i, ln in enumerate(linhas_):
        for j, v in enumerate(ln):
            fill = "#F2F4F7" if i % 2 == 0 else "#FFFFFF"
            c.drawRect(skia.Rect.MakeXYWH(x + j * cw, y + i * ch, cw, ch), paint(fill, a))
            col = (cores or {}).get((i, j), INK2)
            text_mid(c, v, x + (j + 0.5) * cw, y + (i + 0.5) * ch, size, "black" if i == 0 or j == 0 else "bold", col, a)
    c.drawRect(skia.Rect.MakeXYWH(x, y, cols * cw, len(linhas_) * ch), paint("#C9CED6", a, stroke=2))


def b_concreto(c, t, C, B):
    head(c, t, B["start"], "TRÊS COISAS DO DIA A DIA", "O QUE ELAS TÊM EM COMUM?", BLUE)
    card(c, *CARD_R)
    a1 = ep(t, C["04.a"], 0.5)
    objeto(c, 220, 230, 460, 430, "CLASSIFICAÇÃO", "pontos, vitórias, gols", a1)
    tabelinha(c, 255, 320, a1, [["", "P", "V", "SG"], ["Leões", "19", "6", "+8"], ["Tigres", "16", "5", "+3"],
                                ["Águias", "11", "3", "−2"], ["Lobos", "6", "1", "−9"]], 4, cw=98, ch=46, size=22)
    a2 = ep(t, C["04.b"], 0.5)
    objeto(c, 730, 230, 460, 430, "DISTÂNCIAS", "guia rodoviário (km)", a2)
    tabelinha(c, 775, 320, a2, [["", "A", "B", "C"], ["A", "0", "80", "120"], ["B", "80", "0", "50"],
                                ["C", "120", "50", "0"]], 4, cw=92, ch=56, size=24,
              cores={(1, 1): GREEN, (2, 2): GREEN, (3, 3): GREEN})
    a3 = ep(t, C["04.c"], 0.5)
    objeto(c, 1240, 230, 460, 430, "FOTO AMPLIADA", "aparecem os quadradinhos", a3)
    if a3 > 0:
        z = ep(t, C["04.c"] + 0.4, 1.4)
        n = 6
        s = lerp(26, 38, z)
        x0, y0 = 1470 - n * s / 2, 470 - n * s / 2
        for i in range(n):
            for j in range(n):
                v = 0.5 + 0.5 * math.sin(i * 1.3 + j * 0.9)
                cc = mix("#F4D9B8", "#A8603A", v * 0.7)
                if 1 <= i <= 4 and 1 <= j <= 4 and (i + j) % 3 == 0:
                    cc = mix(cc, "#2E3A59", 0.5)
                rrect(c, x0 + j * s + (1 if z > 0.6 else 0), y0 + i * s + (1 if z > 0.6 else 0),
                      s - (2 if z > 0.6 else 0), s - (2 if z > 0.6 else 0), 2, cc, a3)
    ad = ep(t, C["04.d"], 0.5)
    if ad > 0:
        regra(c, "números em LINHAS e COLUNAS  =  MATRIZ", W / 2, 745, ad, 40, BLUE)


# ======================================================================
# bloco a — da tabela à matriz
# ======================================================================

M23 = [[4, 7, 1], [2, 6, 9]]


def b_definicao(c, t, C, B):
    head(c, t, B["start"], "O QUE É UMA MATRIZ", "LINHAS E COLUNAS", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["05.a"], 0.5)
    cx, cy, cw, ch = 640, 500, 150, 120
    x0, y0, w, h = cx - 1.5 * cw, cy - ch, 3 * cw, 2 * ch
    ab = ep(t, C["05.b"], 0.5)
    ab2 = ep(t, C["05.b"] + 2.2, 0.5)
    if aa > 0:
        text(c, "MATRIZ = tabela de números em linhas e colunas", W / 2, 250, 32, "black", BLUE, aa)
        faixa(c, x0 - 10, y0 + 6, w + 20, ch - 12, BLUE, ab)
        faixa(c, x0 + cw * 2 + 6, y0 - 10, cw - 12, h + 20, GREEN, ab2)
        matriz(c, M23, cx, cy, cw, ch, aa, 64)
    if ab > 0:
        text(c, "LINHA: deitada (horizontal)", 1290, 410, 32, "black", BLUE, ab, align="left")
        arrow(c, 1270, 400, x0 + w + 40, y0 + ch / 2 - 4, BLUE, ab, 4, 14)
        text(c, "COLUNA: em pé (vertical)", 1290, 520, 32, "black", GREEN, ab2, align="left")
        arrow(c, 1270, 510, x0 + w - 10, y0 + h + 20, GREEN, ab2, 4, 14)
    acc = ep(t, C["05.c"], 0.5)
    if acc > 0:
        regra(c, "ORDEM  m × n  =  m linhas e n colunas", 1440, 650, acc, 30)
    ad = ep(t, C["05.d"], 0.5)
    if ad > 0:
        text_mid(c, "2 × 3", cx, 740, 70, "black", PURPLE, ad)
        pill(c, "2 linhas · 3 colunas · LINHAS PRIMEIRO", cx, 810, PURPLE, size=24, a=ad, anchor="center")


# ======================================================================
# bloco b — o endereço (cinema)
# ======================================================================

def b_endereco(c, t, C, B):
    head_seq(c, t, C, [("06", "O ENDEREÇO", "LINHA i · COLUNA j", BLUE), ("07", "TROCOU A ORDEM?", "OUTRO LUGAR", AMBER)])
    card(c, *CARD_R)
    sid = which(t, C, ["06", "07"])
    mx, my, cw, ch = 1390, 480, 104, 92
    x0, y0 = mx - 2 * cw, my - 1.5 * ch
    if sid == "06":
        aa = ep(t, C["06.a"], 0.5)
        if aa > 0:
            wl = linha(c, [("cada número é um ", INK), ("ELEMENTO", BLUE), (":  ", INK)], 1100, 280, 30, aa,
                       align="left")
            ind(c, "a", "ij", 1100 + wl, 280, 46, BLUE, aa)
        ab = ep(t, C["06.b"], 0.5)
        if ab > 0:
            linha(c, [("i = LINHA", BLUE), ("    ·    ", GRAY), ("j = COLUNA", GREEN)], 1390, 770, 34, ab)
        acc = ep(t, C["06.c"], 0.5)
        u = caminho(c, t, C["06.d"], 2, 3, acc, GREEN) if t >= C["06.d"] else 0
        cinema(c, acc, {(2, 3): (GREEN, 0.75 * clamp((u - 0.98) * 50))})
        hl = clamp((u - 0.98) * 50)
        matriz(c, M34, mx, my, cw, ch, max(acc, ep(t, C["06.a"], 0.5)), 44,
               fundo={(1, 2): (GREEN, 0.35 * hl)}, cor={(1, 2): mix(INK, GREEN, hl)},
               lin=["linha 1", "linha 2", "linha 3"], lsize=20)
        if hl > 0:
            rrect(c, 1180, 650, 420, 80, 20, mix("#FFFFFF", GREEN, 0.10), hl)
            w_ = ind_w("a", "23", 50)
            ind(c, "a", "23", 1300 - w_ / 2, 690, 50, GREEN, hl)
            linha(c, [(" = 9", GREEN)], 1400, 690, 50, hl)
        return
    acc = 1.0
    hl_ok = 1.0
    u = caminho(c, t, C["07.a"], 3, 2, acc, AMBER)
    hl = clamp((u - 0.98) * 50)
    cinema(c, acc, {(2, 3): (GREEN, 0.45), (3, 2): (AMBER, 0.75 * hl)})
    matriz(c, M34, mx, my, cw, ch, 1.0, 44, fundo={(1, 2): (GREEN, 0.30 * hl_ok), (2, 1): (AMBER, 0.40 * hl)},
           cor={(1, 2): GREEN, (2, 1): mix(INK, AMBER, hl)}, lin=["linha 1", "linha 2", "linha 3"], lsize=20)
    if hl > 0:
        rrect(c, 1180, 650, 420, 80, 20, mix("#FFFFFF", AMBER, 0.12), hl)
        w_ = ind_w("a", "32", 50)
        ind(c, "a", "32", 1300 - w_ / 2, 690, 50, AMBER, hl)
        linha(c, [(" = 3", AMBER)], 1400, 690, 50, hl)
    ab = ep(t, C["07.b"], 0.5)
    if ab > 0:
        x = 1250
        w1 = ind(c, "a", "23", x, 280, 46, GREEN, ab)
        fmid(c, "≠", x + w1 + 50, 280, 46, "black", RED, ab)
        ind(c, "a", "32", x + w1 + 100, 280, 46, AMBER, ab)
    acc2 = ep(t, C["07.c"], 0.5)
    if acc2 > 0:
        regra(c, "primeiro a LINHA, depois a COLUNA", 1390, 790, acc2, 30)


# ======================================================================
# bloco c — lei de formação
# ======================================================================

def b_lei(c, t, C, B):
    head_seq(c, t, C, [("08", "LEI DE FORMAÇÃO", "A RECEITA DE CADA CASA", PURPLE),
                       ("09", "ATALHO", "ANDE PELA REGRA", GREEN)])
    card(c, *CARD_R)
    sid = which(t, C, ["08", "09"])
    mx, my, cw, ch = 1330, 540, 175, 135
    x0, y0 = mx - 1.5 * cw, my - ch
    if sid == "08":
        aa = ep(t, C["08.a"], 0.5)
        if aa > 0:
            text(c, "LEI DE FORMAÇÃO: a receita que diz quanto vale cada endereço", W / 2, 240, 30, "black", PURPLE, aa)
        ab = ep(t, C["08.b"], 0.5)
        if ab > 0:
            rrect(c, 230, 300, 640, 110, 22, mix("#FFFFFF", PURPLE, 0.08), ab)
            w_ = ind(c, "a", "ij", 300, 355, 56, PURPLE, ab)
            linha(c, [(" = 2i − j", PURPLE)], 300 + w_, 355, 56, ab, align="left")
            text(c, "ordem 2 × 3", 760, 368, 30, "black", INK2, ab)
        # casas aparecendo
        ts = [C["08.c"] + 2.2, C["08.c"] + 5.2, C["08.c"] + 7.6, C["08.d"] + 1.6, C["08.d"] + 2.4, C["08.d"] + 3.2]
        contas = ["2·1 − 1 = 1", "2·1 − 2 = 0", "2·1 − 3 = −1", "2·2 − 1 = 3", "2·2 − 2 = 2", "2·2 − 3 = 1"]
        alfa = {}
        for k, tk in enumerate(ts):
            alfa[(k // 3, k % 3)] = ep(t, tk, 0.4)
        am = ep(t, C["08.b"] + 0.5, 0.5)
        if am > 0:
            for i in range(2):
                for j in range(3):
                    if alfa[(i, j)] < 1:
                        ind(c, "a", f"{i + 1}{j + 1}", x0 + (j + 0.5) * cw, y0 + (i + 0.5) * ch, 34, GRAY,
                            am * (1 - alfa[(i, j)]), align="center")
            matriz(c, LEI, mx, my, cw, ch, am, 60, alfa=alfa, lin=["i = 1", "i = 2"], col=["j = 1", "j = 2", "j = 3"],
                   lsize=24)
        for k, tk in enumerate(ts):
            a_ = ep(t, tk, 0.4)
            if a_ <= 0:
                continue
            i, j = k // 3, k % 3
            y = 470 + k * 58
            w_ = ind(c, "a", f"{i + 1}{j + 1}", 260, y, 38, BLUE, a_)
            linha(c, [(" = " + contas[k], INK)], 260 + w_, y, 38, a_, align="left")
        return
    aa = ep(t, C["09.a"], 0.5)
    K.atalho(c, 220, 220, 760, 150, "ATALHO", ["calcule só a₁₁ e ande pela regra"], aa, 32)
    matriz(c, LEI, mx, my, cw, ch, 1.0, 60, lin=["i = 1", "i = 2"], col=["j = 1", "j = 2", "j = 3"], lsize=24)
    ab = ep(t, C["09.b"], 0.5)
    if ab > 0:
        for i in range(2):
            for j in range(2):
                xa, xb = x0 + (j + 0.5) * cw + 34, x0 + (j + 1.5) * cw - 34
                yy = y0 + (i + 0.5) * ch + (-46 if i == 0 else 46)
                arrow(c, xa, yy, xb, yy, AMBER, ab, 4, 12)
                fmid(c, "−1", (xa + xb) / 2, yy + (-20 if i == 0 else 22), 24, "black", AMBER, ab)
        text(c, "para a DIREITA: j aumenta → cai 1", 260, 470, 32, "black", AMBER, ab, align="left")
    acc = ep(t, C["09.c"], 0.5)
    if acc > 0:
        for j in range(3):
            xx = x0 + (j + 0.5) * cw - 58
            arrow(c, xx, y0 + ch * 0.5 - 6, xx, y0 + ch * 1.5 + 6, GREEN, acc, 4, 12)
            fmid(c, "+2", xx - 28, y0 + ch, 24, "black", GREEN, acc)
        text(c, "para BAIXO: i aumenta → sobe 2", 260, 560, 32, "black", GREEN, acc, align="left")
    ad = ep(t, C["09.d"], 0.5)
    if ad > 0:
        conferido(c, "1, 0, −1  e embaixo  3, 2, 1: quase sem conta", 260, 680, ad, True, 30)


# ======================================================================
# bloco d — os tipos
# ======================================================================

Q3 = [[2, 0, 5], [1, 3, 4], [6, 7, 8]]
TIPOS = [("11.a", "NULA", "tudo zero", [[0, 0], [0, 0]], BLUE),
         ("11.b", "DIAGONAL", "zero fora da diagonal", [[5, 0], [0, -2]], BLUE),
         ("11.c", "IDENTIDADE", "diagonal de 1", [[1, 0], [0, 1]], PURPLE),
         ("11.d", "TRIANGULAR", "zeros de um lado", [[3, 7], [0, 2]], BLUE)]


def b_tipos(c, t, C, B):
    head_seq(c, t, C, [("10", "MATRIZ QUADRADA", "AS DUAS DIAGONAIS", BLUE), ("11", "AS FAMÍLIAS", "DA MATRIZ QUADRADA", BLUE),
                       ("12", "TRANSPOSTA", "LINHAS VIRAM COLUNAS", PURPLE), ("13", "SIMÉTRICA", "O ESPELHO", PURPLE)])
    card(c, *CARD_R)
    sid = which(t, C, ["10", "11", "12", "13"])
    if sid == "10":
        aa = ep(t, C["10.a"], 0.5)
        mx, my, cw, ch = 760, 500, 140, 116
        x0, y0 = mx - 1.5 * cw, my - 1.5 * ch
        ab = ep(t, C["10.b"], 0.5)
        acc = ep(t, C["10.c"], 0.5)
        fundo = {}
        for k in range(3):
            fundo[(k, k)] = (BLUE, 0.35 * ab)
        for k in range(3):
            if (k, 2 - k) != (1, 1):
                fundo[(k, 2 - k)] = (AMBER, 0.35 * acc)
        matriz(c, Q3, mx, my, cw, ch, aa, 58, fundo=fundo)
        if ab > 0:
            line(c, x0 + 20, y0 + 20, x0 + lerp(20, 3 * cw - 20, ep(t, C["10.b"], 1.0)),
                 y0 + lerp(20, 3 * ch - 20, ep(t, C["10.b"], 1.0)), BLUE, ab, 6)
        if acc > 0:
            line(c, x0 + 20, y0 + 3 * ch - 20, x0 + lerp(20, 3 * cw - 20, ep(t, C["10.c"], 1.0)),
                 y0 + lerp(3 * ch - 20, 20, ep(t, C["10.c"], 1.0)), AMBER, acc, 6)
        if aa > 0:
            text(c, "QUADRADA: nº de linhas = nº de colunas", 1360, 300, 30, "black", BLUE, aa)
            text(c, "3 × 3", 1360, 360, 40, "black", INK, aa)
        if ab > 0:
            rrect(c, 1100, 430, 520, 120, 20, mix("#FFFFFF", BLUE, 0.08), ab)
            text(c, "DIAGONAL PRINCIPAL", 1360, 480, 28, "black", BLUE, ab)
            text(c, "desce · linha = coluna (i = j)", 1360, 525, 24, "bold", INK2, ab)
        if acc > 0:
            rrect(c, 1100, 590, 520, 120, 20, mix("#FFFFFF", AMBER, 0.10), acc)
            text(c, "DIAGONAL SECUNDÁRIA", 1360, 640, 28, "black", AMBER, acc)
            text(c, "a outra: sobe", 1360, 685, 24, "bold", INK2, acc)
        return
    if sid == "11":
        for k, (cue, nome, sub, M, col) in enumerate(TIPOS):
            a = ep(t, C[cue], 0.5)
            if a <= 0:
                continue
            x = 200 + k * 390
            rrect(c, x, 250, 350, 470, 24, "#FFFFFF", a, shadow=True)
            rrect(c, x, 250, 350, 64, 24, col, a * 0.14)
            text(c, nome, x + 175, 294, 28, "black", col, a)
            dg = {(0, 0): (BLUE, 0.25), (1, 1): (BLUE, 0.25)} if nome != "NULA" else {}
            matriz(c, M, x + 175, 470, 110, 100, a, 50, fundo=dg)
            text(c, sub, x + 175, 670, 24, "black", INK2, a)
        ac = ep(t, C["11.c"], 0.5)
        if ac > 0:
            pill(c, "identidade = diagonal com 1", W / 2, 790, PURPLE, size=26, a=ac, anchor="center")
        return
    if sid == "12":
        aa = ep(t, C["12.a"], 0.5)
        if aa > 0:
            text(c, "TRANSPOSTA: troca as linhas pelas colunas", W / 2, 240, 32, "black", PURPLE, aa)
        A = [[1, 2, 3], [4, 5, 6]]
        AT = [[1, 4], [2, 5], [3, 6]]
        ab = ep(t, C["12.b"], 0.5)
        cA = {(0, j): BLUE for j in range(3)}
        cA.update({(1, j): GREEN for j in range(3)})
        cT = {(i, 0): BLUE for i in range(3)}
        cT.update({(i, 1): GREEN for i in range(3)})
        matriz(c, A, 560, 500, 130, 110, max(aa, ab), 56, cor=cA if ab > 0 else None)
        g = ep(t, C["12.b"] + 1.6, 0.6)
        if g > 0:
            arrow(c, 820, 500, 960, 500, PURPLE, g, 6, 18)
            matriz(c, AT, 1240, 500, 130, 110, g, 56, cor=cT)
            text(c, "A", 560, 360, 36, "black", INK2, g)
            ind(c, "A", "t", 1240, 300, 40, INK2, g, align="center")
        acc = ep(t, C["12.c"], 0.5)
        if acc > 0:
            K.atalho(c, 1420, 380, 340, 240, "ATALHO", ["1ª linha", "vira a 1ª coluna"], acc, 30)
        ad = ep(t, C["12.d"], 0.5)
        if ad > 0:
            chip(c, "2 × 3", 560, 740, BLUE, ad, 40)
            arrow(c, 680, 740, 1100, 740, PURPLE, ad, 5, 16)
            chip(c, "3 × 2", 1240, 740, GREEN, ad, 40)
        return
    S = [[0, 8, 5], [8, 0, 3], [5, 3, 0]]
    mx, my, cw, ch = 760, 510, 140, 116
    x0, y0 = mx - 1.5 * cw, my - 1.5 * ch
    aa = ep(t, C["13.a"], 0.5)
    pares = [((0, 1), (1, 0)), ((0, 2), (2, 0)), ((1, 2), (2, 1))]
    fundo = {}
    for k, (p1, p2) in enumerate(pares):
        ak = ep(t, C["13.b"] + 0.8 + k * 1.3, 0.4)
        col = [BLUE, GREEN, AMBER][k]
        fundo[p1] = (col, 0.32 * ak)
        fundo[p2] = (col, 0.32 * ak)
    acc = ep(t, C["13.c"], 0.5)
    if acc > 0:
        for k in range(14):
            u0, u1 = k / 14, (k + 0.55) / 14
            line(c, x0 + lerp(0, 3 * cw, u0), y0 + lerp(0, 3 * ch, u0), x0 + lerp(0, 3 * cw, u1), y0 + lerp(0, 3 * ch, u1),
                 PURPLE, acc, 6)
    matriz(c, S, mx, my, cw, ch, aa, 58, fundo=fundo)
    if aa > 0:
        text(c, "SIMÉTRICA: igual à própria transposta", 1380, 300, 30, "black", PURPLE, aa)
        w_ = ind_w("a", "ij", 44)
        ind(c, "a", "ij", 1250, 380, 44, INK, aa)
        fmid(c, "=", 1250 + w_ + 40, 380, 44, "black", INK, aa)
        ind(c, "a", "ji", 1250 + w_ + 80, 380, 44, INK, aa)
    if acc > 0:
        selo(c, 1380, 560, acc, "A DIAGONAL É O ESPELHO", PURPLE, -3, 32)


# ======================================================================
# bloco e — o endereço tem significado
# ======================================================================

def b_contexto(c, t, C, B):
    head_seq(c, t, C, [("14", "DISTÂNCIAS", "A TABELA DO ESPELHO", BLUE), ("15", "GOLS", "LINHA FEZ · COLUNA SOFREU", BLUE),
                       ("16", "ATALHO", "ROTULE E CONFIRA", GREEN)])
    card(c, *CARD_R)
    sid = which(t, C, ["14", "15", "16"])
    mx, my, cw, ch = 720, 510, 150, 112
    x0, y0 = mx - 1.5 * cw, my - 1.5 * ch
    if sid == "14":
        aa = ep(t, C["14.a"], 0.5)
        acc = ep(t, C["14.c"], 0.5)
        ad = ep(t, C["14.d"], 0.5)
        g = ep(t, C["14.d"] + 2.4, 1.0)
        M = [r[:] for r in D3]
        M[0][2] = None
        fundo = {(0, 2): (BLUE, 0.30 * aa)}
        for k in range(3):
            fundo[(k, k)] = (GREEN, 0.30 * acc)
        fundo[(2, 0)] = (AMBER, 0.35 * ad)
        matriz(c, M, mx, my, cw, ch, aa, 46, fundo=fundo, lin=["cidade 1", "cidade 2", "cidade 3"],
               col=["até 1", "até 2", "até 3"], lsize=22)
        if aa > 0 and g < 1:
            fmid(c, "?", x0 + 2.5 * cw, y0 + 0.5 * ch, 46, "black", BLUE, aa * (1 - g))
            w_ = ind_w("d", "13", 44)
            ind(c, "d", "13", 1340 - w_ / 2, 300, 44, BLUE, aa)
            text(c, "distância de 1 até 3", 1340, 370, 26, "bold", INK2, aa)
        if ad > 0:
            xs, ys = x0 + 0.5 * cw, y0 + 2.5 * ch
            xe, ye = x0 + 2.5 * cw, y0 + 0.5 * ch
            fmid(c, "120", lerp(xs, xe, g), lerp(ys, ye, g), 46, "black", AMBER if g < 1 else GREEN, ad if g > 0 else 0)
            if g >= 1:
                rrect(c, x0 + 2 * cw + 4, y0 + 4, cw - 8, ch - 8, 12, GREEN, 0.25)
        ab = ep(t, C["14.b"], 0.5)
        if ab > 0:
            chip(c, "MÃO DUPLA: simétrica", 1340, 470, BLUE, ab, 30)
        if acc > 0:
            chip(c, "diagonal = 0", 1340, 570, GREEN, acc, 30)
        if ad > 0:
            pill(c, "valor apagado? COPIE DO ESPELHO", 1340, 680, AMBER, size=26, a=ad, anchor="center")
        return
    if sid == "15":
        aa = ep(t, C["15.a"], 0.5)
        ab = ep(t, C["15.b"], 0.5)
        ab2 = ep(t, C["15.b"] + 1.8, 0.5)
        acc = ep(t, C["15.c"], 0.5)
        ad = ep(t, C["15.d"], 0.5)
        faixa(c, x0 - 8, y0 + 6, 3 * cw + 16, ch - 12, BLUE, ab)
        faixa(c, x0 + 6, y0 - 8, cw - 12, 3 * ch + 16, AMBER, ab2)
        fundo = {(0, 1): (RED, 0.30 * ad), (1, 0): (RED, 0.30 * ad)}
        matriz(c, G3, mx, my, cw, ch, aa, 50, fundo=fundo, lin=["time 1", "time 2", "time 3"],
               col=["vs 1", "vs 2", "vs 3"], lsize=22)
        if aa > 0:
            w_ = ind_w("g", "ij", 42)
            ind(c, "g", "ij", 1150, 260, 42, BLUE, aa)
            text(c, "= gols do time i contra o time j", 1150 + w_ + 12, 272, 26, "black", INK2, aa, align="left")
        if ab > 0:
            text(c, "LINHA = o que o time FEZ", 1150, 380, 30, "black", BLUE, ab, align="left")
            text(c, "COLUNA = o que fizeram CONTRA ele", 1150, 440, 30, "black", AMBER, ab2, align="left")
        if acc > 0:
            rrect(c, 1140, 500, 560, 110, 20, "#FFFFFF", acc, shadow=True)
            text(c, "SALDO = linha − coluna", 1420, 540, 26, "black", PURPLE, acc)
            linha(c, [("time 1: 5 − 2 = ", INK), ("+3", GREEN)], 1420, 585, 32, acc)
        if ad > 0:
            linha(c, [("3 a 1", RED), ("  ≠  ", INK), ("1 a 3", RED)], 1420, 690, 44, ad)
            text(c, "a tabela de gols NÃO é simétrica", 1420, 760, 26, "black", RED, ad)
        return
    aa = ep(t, C["16.a"], 0.5)
    K.atalho(c, 220, 220, 1480, 130, "ATALHO", ["ROTULE antes de somar:  linha = fez  ·  coluna = sofreu"], aa, 34)
    ab = ep(t, C["16.b"], 0.5)
    if ab > 0:
        text(c, "todo gol marcado por um é SOFRIDO por outro  →  os saldos somam ZERO", W / 2, 430, 30, "black", INK, ab)
        sal = [3, -4, 1]
        for k, v in enumerate(sal):
            a_ = ep(t, C["16.c"] + k * 0.8, 0.4)
            chip(c, ssg(v), 640 + k * 230, 580, GREEN if v > 0 else RED, a_, 54)
            if k < 2:
                text_mid(c, "+", 755 + k * 230, 580, 50, "black", GRAY, a_)
        af = ep(t, C["16.c"] + 2.6, 0.4)
        if af > 0:
            text_mid(c, "=  0", 1380, 580, 64, "black", GREEN, af)
            conferido(c, "fechou", 860, 740, af, True, 34)


# ======================================================================
# bloco f — imagem digital
# ======================================================================

def b_pixels(c, t, C, B):
    head(c, t, B["start"], "IMAGEM DIGITAL", "CADA PIXEL É UM ELEMENTO", BLUE)
    card(c, *CARD_R)
    s = 58
    aa = ep(t, C["17.a"], 0.5)
    ab = ep(t, C["17.b"], 0.5)
    pixels(c, FIG, 230, 300, s, aa, numeros=ab)
    if aa > 0:
        text(c, "ORIGINAL", 230 + 3 * s, 270, 26, "black", INK2, aa)
        text(c, "PIXEL = o menor ponto da imagem", 230 + 3 * s, 700, 24, "black", BLUE, aa)
    if ab > 0:
        text(c, "1 = aceso   ·   0 = apagado", 230 + 3 * s, 745, 24, "black", INK2, ab)
    acc = ep(t, C["17.c"], 0.5)
    if acc > 0:
        u = ep(t, C["17.c"] + 0.6, 0.8)
        pixels(c, FIG, 760, 300, s, acc, inv=u, numeros=ab)
        text(c, "1 ↔ 0", 760 + 3 * s, 270, 26, "black", AMBER, acc)
        text(c, "as cores INVERTEM", 760 + 3 * s, 700, 24, "black", AMBER, acc)
    ad = ep(t, C["17.d"], 0.5)
    if ad > 0:
        pixels(c, FIG, 1290, 300, s, ad, transp=True, numeros=ab)
        for k in range(12):
            u0, u1 = k / 12, (k + 0.55) / 12
            line(c, 1290 + 6 * s * u0, 300 + 6 * s * u0, 1290 + 6 * s * u1, 300 + 6 * s * u1, PURPLE, ad, 4)
        ftext(c, "TRANSPOSTA", 1290 + 3 * s, 270 + 8, 26, "black", PURPLE, ad)
        text(c, "espelhada na diagonal", 1290 + 3 * s, 700, 24, "black", PURPLE, ad)
        text(c, "1ª linha → 1ª coluna", 1290 + 3 * s, 745, 24, "bold", INK2, ad)


# ======================================================================
# nós fazemos
# ======================================================================

def b_exercicio(c, t, C, B):
    head_seq(c, t, C, [("18", "SUA VEZ", "PAUSE E TENTE", GREEN), ("19", "VAMOS JUNTOS", "LINHA PRIMEIRO", GREEN)])
    card(c, *CARD_R)
    aa = ep(t, C["18.a"], 0.5)
    if aa > 0:
        rrect(c, 260, 210, 1400, 130, 24, "#F7F7F5", aa)
        w_ = ind(c, "a", "ij", 520, 275, 56, PURPLE, aa)
        x = 520 + w_
        x += linha(c, [(" = i + 2j  ·  2 × 2  ·  ", INK)], x, 275, 50, aa, align="left")
        w2 = ind(c, "a", "21", x, 275, 50, BLUE, aa)
        x += w2
        x += linha(c, [(" = ?   ", INK)], x, 275, 50, aa, align="left")
        w3 = ind(c, "a", "12", x, 275, 50, GREEN, aa)
        linha(c, [(" = ?", INK)], x + w3, 275, 50, aa, align="left")
    pause_timer(c, t, C["18.end"] - 1.9, W / 2, 560)
    if t < C["19"]:
        return
    a1 = ep(t, C["19.a"], 0.5)
    if a1 > 0:
        rrect(c, 260, 400, 680, 260, 24, "#FFFFFF", a1, shadow=True)
        w_ = ind(c, "a", "21", 300, 450, 44, BLUE, a1)
        linha(c, [(":  linha 2, coluna 1", INK2)], 300 + w_, 450, 32, a1, align="left")
        linha(c, [("2 + 2·1 = ", INK), ("4", BLUE)], 600, 560, 56, a1)
    a2 = ep(t, C["19.b"], 0.5)
    if a2 > 0:
        rrect(c, 980, 400, 680, 260, 24, "#FFFFFF", a2, shadow=True)
        w_ = ind(c, "a", "12", 1020, 450, 44, GREEN, a2)
        linha(c, [(":  linha 1, coluna 2", INK2)], 1020 + w_, 450, 32, a2, align="left")
        linha(c, [("1 + 2·2 = ", INK), ("5", GREEN)], 1320, 560, 56, a2)
    a3 = ep(t, C["19.c"], 0.5)
    if a3 > 0:
        regra(c, "endereços trocados, valores DIFERENTES", W / 2, 750, a3, 34)


# ======================================================================
# recap, erros
# ======================================================================

FRASES = ["Primeiro a linha, depois a coluna.",
          "Tabela de mão dupla é simétrica: a diagonal é o espelho.",
          "Linha é o que o time fez; coluna é o que ele sofreu."]


def b_recap(c, t, C, B):
    sid = which(t, C, ["20", "30"])
    frame(c, t, B["start"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "20" else "PARA FECHAR", PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 300 + k * 180 + d
        badge_num(c, k + 1, 260, y - 16, a, 36, bg=PURPLE)
        para(c, s, 320, y, 50, "black", INK, a, 1360, 60)


ERROS = [("Ler a₂₃ como linha 3, coluna 2", "os dois números estão ali, e a ordem parece detalhe",
          "na nossa 2 × 3 nem existe linha 3: o 1º índice é SEMPRE a linha"),
         ("A transposta de uma 2 × 3 continua 2 × 3", "os números são os mesmos",
          "as linhas viraram colunas: o tamanho gira junto → 3 × 2"),
         ("Tomar a COLUNA como gols marcados", "a soma da coluna parece tão boa quanto a da linha",
          "o time 1 (fez 5, sofreu 2) ficaria com −3! Rotule: linha é o que o time FEZ")]


def b_erros(c, t, C, B):
    K.erro_cards(c, t, C, ["21", "22", "23"], ERROS)


# ======================================================================
# questões do material
# ======================================================================

def ftext_sub(c, s, x, y, size, col, a):
    """texto alinhado à esquerda em que 'g_ij' vira g com o índice ij embaixo"""
    for k, pedaco in enumerate(re.split(r"(\w_\w+)", s)):
        if not pedaco:
            continue
        if k % 2:
            b, sb = pedaco.split("_")
            x += ind(c, b, sb, x, y - size * 0.36, size, col, a)
        else:
            ftext(c, pedaco, x, y, size, "black", col, a, align="left")
            x += ftext_w(pedaco, "black", size)


def _enunciado(c, linhas, a, y0=240, size=26, w=1000):
    y = y0
    for s, col in linhas:
        for ln in K.wrap(s, "black", size, w):
            ftext_sub(c, ln, 190, y, size, col, a)
            y += size + 10
        y += 6
    return y


ALTS1 = [("A", "o time 1.", "", GREEN), ("B", "o time 2.", "só quem mais marcou", RED),
         ("C", "o time 3.", "coluna − linha", RED), ("D", "o time 4.", "errou a coluna 4", RED),
         ("E", "os times 1 e 4, empatados.", "só marcados", RED)]


def b_q1(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 1 · EU FAÇO", "LER LINHAS E COLUNAS", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["24.a"], 0.4)
    yend = _enunciado(c, [("Em um torneio entre quatro times, os gols foram registrados na matriz G, em que g_ij é o "
                           "número de gols que o time i marcou contra o time j (a diagonal é zero, pois um time não "
                           "joga contra si mesmo). O saldo de gols é a diferença entre gols marcados e gols sofridos. "
                           "O time com o maior saldo de gols é", INK)], a0, 236, 26, 1000)
    ftext(c, "Questão do material de estudo (seção 12)", 190, 832, 18, "medium", GRAY, a0 * (1 - ep(t, C["25"], 0.3)),
          align="left")
    cues_in = {L: C[f"24.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"26.x{L.lower()}"] for L in "BCDE"}
    K.alternativas(c, t, C, ALTS1, 1240, 250, 470, 30, C["25.ok"], "A", cues_in, cues_x, gap=22)
    ab = ep(t, C["25.a"], 0.4)
    ab2 = ep(t, C["25.b"], 0.4)
    mx, my, cw, ch = 420, 610, 72, 56
    x0, y0 = mx - 2 * cw, my - 2 * ch
    if a0 > 0:
        faixa(c, x0 - 4, y0 + 4, 4 * cw + 8, ch - 8, BLUE, ab2)
        faixa(c, x0 + 4, y0 - 4, cw - 8, 4 * ch + 8, AMBER, ab2)
        matriz(c, G4, mx, my, cw, ch, ep(t, C["24.a"] + 3.0, 0.4), 30, lin=["1", "2", "3", "4"],
               col=["1", "2", "3", "4"], lsize=20)
        ftext(c, "G =", x0 - 110, my + 10, 30, "black", INK, ep(t, C["24.a"] + 3.0, 0.4), align="left")
    if ab > 0:
        ftext(c, "linha = MARCADOS", 640, 520, 22, "black", BLUE, ab, align="left")
        ftext(c, "coluna = SOFRIDOS", 640, 552, 22, "black", AMBER, ab, align="left")
    if ab2 > 0:
        rows = [("1", "5", "3", 2, "25.b"), ("2", "7", "7", 0, "25.c"), ("3", "2", "5", -3, "25.c"),
                ("4", "5", "4", 1, "25.c")]
        xs = [660, 760, 870, 990]
        hdr = ["time", "marc.", "sofr.", "saldo"]
        for k, hh in enumerate(hdr):
            ftext(c, hh, xs[k], 600, 20, "black", GRAY, ab2)
        for k, (tm, mm, ss, sal, cue) in enumerate(rows):
            a_ = ep(t, C[cue] + (0 if k <= 1 else (k - 1) * 2.2), 0.4) if k > 0 else ab2
            y = 640 + k * 42
            ftext(c, tm, xs[0], y, 24, "black", INK, a_)
            ftext(c, mm, xs[1], y, 24, "black", BLUE, a_)
            ftext(c, ss, xs[2], y, 24, "black", AMBER, a_)
            ftext(c, ssg(sal), xs[3], y, 26, "black", GREEN if sal > 0 else (RED if sal < 0 else INK2), a_)
        ad = ep(t, C["25.d"], 0.4)
        if ad > 0:
            linha(c, [("+2 + 0 − 3 + 1 = ", INK), ("0", GREEN), ("  ✓", GREEN)], 830, 820, 24, ad)


ALTS5 = [("A", "240", "y tratado como zero", RED), ("B", "350", "copiou o vizinho", RED),
         ("C", "380", "", GREEN), ("D", "440", "usou d₁₄ = 200", RED), ("E", "580", "somou a volta", RED)]


def b_q5(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 5 · VOCÊ FAZ", "TABELA SIMÉTRICA", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["27.a"], 0.4)
    yend = _enunciado(c, [("Uma transportadora registra as distâncias rodoviárias, em km, entre quatro cidades na "
                           "matriz D, em que d_ij é a distância entre as cidades i e j. As estradas são de mão dupla, e "
                           "dois valores foram apagados. Um caminhão faz o trajeto 1 → 3 → 2 → 4, sem voltar. A "
                           "distância percorrida, em km, é", INK)], a0, 236, 26, 1000)
    ftext(c, "Questão do material de estudo (seção 12)", 190, 832, 18, "medium", GRAY, a0 * (1 - ep(t, C["28"], 0.3)),
          align="left")
    cues_in = {L: C[f"27.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"29.x{L.lower()}"] for L in "ABDE"}
    K.alternativas(c, t, C, ALTS5, 1240, 250, 470, 30, C["28.ok"], "C", cues_in, cues_x, gap=22)
    mx, my, cw, ch = 470, 630, 92, 56
    x0, y0 = mx - 2 * cw, my - 2 * ch
    aa = ep(t, C["28.a"], 0.4)
    ab = ep(t, C["28.b"], 0.4)
    M = [r[:] for r in D4]
    cor = {(0, 2): AMBER, (1, 3): AMBER}
    if aa > 0.5:
        M[0][2] = "150"; cor[(0, 2)] = GREEN
    if ab > 0.5:
        M[1][3] = "140"; cor[(1, 3)] = GREEN
    fundo = {(2, 0): (BLUE, 0.3 * aa), (0, 2): (GREEN, 0.25 * aa), (3, 1): (BLUE, 0.3 * ab), (1, 3): (GREEN, 0.25 * ab)}
    acc = ep(t, C["28.c"], 0.4)
    for k, (i, j) in enumerate(((0, 2), (2, 1), (1, 3))):
        fundo[(i, j)] = (PURPLE, 0.3 * ep(t, C["28.c"] + 0.6 + k * 1.4, 0.4)) if acc > 0 else fundo.get((i, j), (INK, 0))
    am = ep(t, C["27.a"] + 3.0, 0.4)
    matriz(c, M, mx, my, cw, ch, am, 28, cor=cor, fundo=fundo, lin=["1", "2", "3", "4"], col=["1", "2", "3", "4"],
           lsize=20)
    ftext(c, "D =", x0 - 110, my + 10, 30, "black", INK, am, align="left")
    pause_timer(c, t, C["27.end"] - 1.9, 1000, 640)
    if t >= C["28"]:
        if aa > 0:
            linha(c, [("x = d₃₁ = ", INK), ("150", GREEN)], 980, 560, 28, aa)
        if ab > 0:
            linha(c, [("y = d₄₂ = ", INK), ("140", GREEN)], 980, 610, 28, ab)
        if acc > 0:
            linha(c, [("150 + 90 + 140 = ", INK), ("380 km", GREEN)], 980, 700, 30, acc)
            pill(c, "espelho: mão dupla", 980, 780, BLUE, size=22, a=acc, anchor="center")


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "CASA COM CASA", PURPLE)
    aa = ep(t, C["31.a"], 0.5)
    P1 = [[6, 8], [5, 9]]
    P2 = [[8, 6], [7, 9]]
    if aa > 0:
        text(c, "prova 1", 480, 300, 30, "black", BLUE, aa)
        matriz(c, P1, 480, 450, 120, 100, aa, 50, bcol=BLUE)
        a2 = ep(t, C["31.a"] + 1.4, 0.5)
        text_mid(c, "+", 720, 450, 70, "black", INK, a2)
        text(c, "prova 2", 960, 300, 30, "black", GREEN, a2)
        matriz(c, P2, 960, 450, 120, 100, a2, 50, bcol=GREEN)
    ab = ep(t, C["31.b"], 0.5)
    if ab > 0:
        text_mid(c, "→", 1200, 450, 70, "black", GRAY, ab)
        text(c, "médias?", 1450, 300, 30, "black", PURPLE, ab)
        matriz(c, [["?", "?"], ["?", "?"]], 1450, 450, 120, 100, ab, 50, cor={(i, j): PURPLE for i in range(2) for j in range(2)},
               bcol=PURPLE)
    acc = ep(t, C["31.c"], 0.5)
    if acc > 0:
        chip(c, "dá: CASA COM CASA", W / 2, 650, PURPLE, acc, 40)
    pill(c, "ep. 2 · igualdade, soma e número × matriz", W / 2, 790, PURPLE, size=30, a=ep(t, C["31.d"], 0.5),
         anchor="center")


def b_cta(c, t, C, B):
    cta(c, t, C["32.like"], C["32.sub"], C["32.bell"], C["32.com"], C["32.bye"],
        "Você já tinha trocado linha por coluna?", canal="no Estudativo", anki=C["32.anki"])


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, concreto=b_concreto, definicao=b_definicao,
              endereco=b_endereco, lei=b_lei, tipos=b_tipos, contexto=b_contexto, pixels=b_pixels, exercicio=b_exercicio,
              recap=b_recap, erros=b_erros, q1=b_q1, q5=b_q5, ponte=b_ponte, cta=b_cta)
