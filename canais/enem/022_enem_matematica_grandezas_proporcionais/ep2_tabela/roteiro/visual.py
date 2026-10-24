"""Visual — Grandezas Proporcionais, Episódio 2: Reconhecer a proporcionalidade numa tabela (iniciantes, tema claro).
Peças comuns da série em ../../comum.py (reexporta o 019/comum.py: expr com frações, fichas, alternativas, erro_cards...).
Peças deste episódio: tabela() com a COLUNA AUXILIAR nascendo linha por linha (verde = igual, vermelho = diferente) e a lupa.
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
_s = importlib.util.spec_from_file_location("comum022", _p)
K = importlib.util.module_from_spec(_s); _s.loader.exec_module(K)
K.usar_tempos(Path(__file__).resolve().parents[1] / "audio" / "tempos.json")
motor.set_theme("claro")
expr, fr = K.expr, K.fr
frame, head_seq, which, para, boxed, regra, selo, pause_timer, chip = (K.frame, K.head_seq, K.which, K.para, K.boxed, K.regra,
                                                                        K.selo, K.pause_timer, K.chip)
fmid, ftext = K.fmid, K.ftext

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_grandezas_ep2_tabela.mp4"
CARD_R = K.CARD_R
CAB = "#F1F1EC"     # fundo do cabeçalho da tabela
AUXF = "#F4EFFC"    # fundo da coluna auxiliar


# ======================================================================
# peças do episódio
# ======================================================================

def lupa(c, cx, cy, a, r=34, rot=-35):
    """lupa de detetive: lente + cabo"""
    if a <= 0:
        return
    c.save(); c.translate(cx, cy); c.rotate(rot)
    c.drawCircle(0, 0, r, paint("#FFFFFF", a * 0.35))
    c.drawCircle(0, 0, r, paint(INK, a, stroke=7))
    rrect(c, r - 2, -8, r * 1.35, 16, 8, AMBER, a)
    c.restore()


def aux_col(vals, ts, alvo, tv):
    """coluna auxiliar: vals = textos; ts = instante de cada linha; alvo = cor final de cada valor; tv = instante do veredito"""
    return dict(vals=vals, ts=ts, alvo=alvo, tv=tv)


def tabela(c, t, x, y, cab, linhas, a, aux=(), ts_lin=None, w=(190, 190), wa=200, rh=76, size=42, lupa_ts=None,
           lupa_col=None):
    """tabela de valores com até 2 colunas auxiliares (aux = lista de dicts de aux_col; cab da auxiliar = 'op').
    ts_lin = instante em que cada linha aparece (None = todas com a tabela). lupa_ts = instantes por linha para a lupa
    (ela passa linha a linha ao lado da coluna lupa_col). Devolve a largura total."""
    if a <= 0:
        return 0
    n = len(linhas)
    ws = list(w) + [wa] * len(aux)
    W_ = sum(ws)
    H_ = rh * (n + 1)
    rrect(c, x, y, W_, H_, 18, "#FFFFFF", a, shadow=True)
    # fundo do cabeçalho e das auxiliares
    c.save(); c.clipRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, W_, H_), 18, 18), True)
    c.drawRect(skia.Rect.MakeXYWH(x, y, W_, rh), paint(CAB, a))
    xx = x + sum(w)
    for k, ax in enumerate(aux):
        aa = a * ep(t, ax["ts"][0] - 0.4, 0.4)
        c.drawRect(skia.Rect.MakeXYWH(xx, y, wa, H_), paint(AUXF, aa))
        xx += wa
    c.restore()
    # linhas da grade
    for i in range(1, n + 1):
        line(c, x + 12, y + i * rh, x + W_ - 12, y + i * rh, "#E4E4DF", a, 2)
    xx = x
    for k, wk in enumerate(ws[:-1]):
        xx += wk
        line(c, xx, y + 10, xx, y + H_ - 10, "#E4E4DF", a, 2)
    # cabeçalho
    xx = x
    for k, s in enumerate(cab):
        ftext(c, s, xx + ws[k] / 2, y + rh * 0.66, size * 0.72, "black", INK2, a)
        xx += ws[k]
    for k, ax in enumerate(aux):
        aa = a * ep(t, ax["ts"][0] - 0.4, 0.4)
        fmid(c, ax["op"], xx + wa / 2, y + rh / 2, size * 0.9, "black", PURPLE, aa)
        xx += wa
    # valores
    for i, row in enumerate(linhas):
        al = a * (ep(t, ts_lin[i], 0.35) if ts_lin else 1.0)
        cy = y + (i + 1) * rh + rh * 0.66
        xx = x
        for k, s in enumerate(row):
            ftext(c, s, xx + ws[k] / 2, cy, size, "black", INK, al)
            xx += ws[k]
        for ax in aux:
            if i < len(ax["vals"]) and ax["vals"][i]:
                av = a * ep(t, ax["ts"][i], 0.3)
                if av > 0:
                    col = mix(INK, ax["alvo"][i], ep(t, ax["tv"], 0.4))
                    sc = 1 + 0.18 * math.sin(math.pi * prog(t, ax["ts"][i], 0.35))
                    c.save(); c.translate(xx + wa / 2, cy - size * 0.35); c.scale(sc, sc)
                    ftext(c, ax["vals"][i], 0, size * 0.35, size, "black", col, av)
                    c.restore()
            xx += wa
    # lupa passando linha a linha
    if lupa_ts:
        r = sum(ep(t, ti, 0.35) for ti in lupa_ts[1:])
        al = a * ep(t, lupa_ts[0] - 0.2, 0.3)
        lx = x + (lupa_col if lupa_col is not None else W_ + 60)
        lupa(c, lx, y + rh * 1.5 + r * rh, al)
    return W_


def veredito(c, cx, cy, s, col, a, size=34):
    chip(c, s, cx, cy, col, a, size)


def lin_ts(C, sid, n, pref="r"):
    return [C[f"{sid}.{pref}{i + 1}"] for i in range(n)]


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "PROPORCIONAL OU NÃO?", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["01.a"], 0.5)
    tabela(c, t, 330, 260, ["x", "y"], [["1", "12"], ["2", "6"], ["3", "4"]], aa, w=(180, 180), rh=86, size=46)
    if aa > 0:
        for k in range(3):
            fmid(c, "?", 330 + 360 + 40, 260 + 86 * (k + 1) + 43, 46, "black", AMBER, aa * ep(t, C["01.a"] + 0.4 + 0.25 * k, 0.4))
        text(c, "tabela de valores: o formato que MAIS cai", 510, 700, 30, "black", BLUE, aa)
    ab = ep(t, C["01.b"], 0.5)
    if ab > 0:
        for k, (op, nome) in enumerate((("÷", "conta 1"), ("×", "conta 2"))):
            x = 1180 + k * 300
            rrect(c, x - 120, 280, 240, 240, 36, PURPLE, ab * 0.12)
            fmid(c, op, x, 380, 130, "black", PURPLE, ab)
            text(c, nome, x, 490, 30, "black", INK2, ab)
        selo(c, 1330, 650, ep(t, C["01.b"] + 0.8, 0.5), "RESOLVE TODAS EM SEGUNDOS", GREEN, -3, 32)


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "AO FINAL DESTA AULA", "VOCÊ VAI CONSEGUIR", GREEN)
    rows = [("02.a", "bater o olho numa tabela e decidir", "direta · inversa · nenhuma"),
            ("02.b", "e ainda achar o k", "o número que não muda")]
    for j, (cue, s, sub) in enumerate(rows):
        a, d = rise(t, C[cue])
        y = 330 + j * 200 + d
        check_icon(c, 300, y - 14, 34, a, GREEN)
        text(c, s, 360, y, 50, "black", INK, a, align="left")
        text(c, sub, 360, y + 56, 32, "bold", GRAY, a, align="left")
    lupa(c, 1520, 520, ep(t, C["02.a"], 0.5), 70)


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "LEMBRETE RELÂMPAGO", "DO EPISÓDIO 1", GREEN)
    aa = ep(t, C["03.a"], 0.5)
    if aa > 0:
        text(c, "DIRETA", 560, 260, 34, "black", BLUE, aa)
        text(c, "QUOCIENTE constante", 560, 310, 28, "bold", INK2, aa)
        text(c, "quociente = resultado da divisão", 560, 352, 24, "bold", GRAY, aa)
        fr(c, "preço", "quilos", 440, 480, 50, INK, aa)
        ftext(c, "= R$/kg", 640, 498, 46, "black", PURPLE, aa, align="left")
        chip(c, "a etiqueta do mercado", 560, 620, BLUE, aa, 28)
    ab = ep(t, C["03.b"], 0.5)
    if ab > 0:
        text(c, "INVERSA", 1360, 260, 34, "black", PURPLE, ab)
        text(c, "PRODUTO constante", 1360, 310, 28, "bold", INK2, ab)
        text(c, "produto = resultado da multiplicação", 1360, 352, 24, "bold", GRAY, ab)
        ftext(c, "velocidade × tempo = 240", 1360, 498, 46, "black", INK, ab)
        chip(c, "o bolo da viagem de 240 km", 1360, 620, PURPLE, ab, 28)
    line(c, 960, 230, 960, 700, "#E6E6E2", aa, 3)
    acc = ep(t, C["03.c"], 0.5)
    regra(c, "k = o número que NÃO muda", W / 2, 760, acc, 40)


# ======================================================================
# a tabela do cotidiano e o teste 1
# ======================================================================

ARROZ = [["1", "5"], ["2", "10"], ["3", "15"], ["4", "20"]]


def b_arroz(c, t, C, B):
    frame(c, t, B["start"], "UMA TABELA DO MERCADO", "QUILOS E PREÇO", BLUE)
    ts = lin_ts(C, "04", 4)
    tabela(c, t, 300, 210, ["quilos", "R$"], ARROZ, ep(t, C["04"], 0.5), ts_lin=ts, rh=100, size=50, w=(220, 220))
    aa = ep(t, C["04.a"], 0.5)
    if aa > 0:
        boxed(c, 900, 230, 720, 170, BLUE, aa, 0.08)
        text(c, "TABELA DE VALORES", 1260, 290, 36, "black", BLUE, aa)
        text(c, "uma coluna para cada grandeza", 1260, 345, 30, "bold", INK2, aa)
    ab = ep(t, C["04.b"], 0.5)
    if ab > 0:
        # destaca a 2ª linha (2 kg, R$ 10)
        rrect(c, 290, 210 + 100 * 2 + 6, 460, 88, 16, AMBER, ab * 0.18)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(290, 210 + 100 * 2 + 6, 460, 88), 16, 16), paint(AMBER, ab, stroke=4))
        boxed(c, 900, 460, 720, 230, AMBER, ab, 0.08)
        text(c, "PAR ORDENADO", 1260, 520, 36, "black", AMBER, ab)
        text(c, "dois valores que andam juntos,", 1260, 575, 30, "bold", INK2, ab)
        text(c, "sempre na mesma ordem", 1260, 615, 30, "bold", INK2, ab)
        ftext(c, "(2; 10)", 1260, 672, 40, "black", INK, ab)


def b_teste1(c, t, C, B):
    frame(c, t, B["start"], "TESTE 1 DO DETETIVE", "DIVIDIR", PURPLE)
    ts = lin_ts(C, "05", 4)
    a0 = ep(t, C["05"], 0.5)
    vals = ["5", "5", "5", "5"]
    tabela(c, t, 300, 210, ["quilos", "R$"], ARROZ, a0, aux=[dict(aux_col(vals, ts, [GREEN] * 4, C["05.v"]), op="R$ ÷ kg")],
           rh=100, size=50, w=(220, 220), wa=240, lupa_ts=ts)
    aa = ep(t, C["05.a"], 0.5)
    if aa > 0:
        chip(c, "TESTE 1: segunda coluna ÷ primeira", 1340, 260, PURPLE, aa, 30)
        text(c, "linha por linha", 1340, 330, 28, "bold", INK2, aa)
    av = ep(t, C["05.v"], 0.5)
    if av > 0:
        boxed(c, 1080, 400, 520, 150, GREEN, av, 0.08)
        text(c, "quociente NÃO muda", 1340, 455, 34, "black", GREEN, av)
        text(c, "→ DIRETA", 1340, 512, 44, "black", GREEN, av)
    ak = ep(t, C["05.k"], 0.5)
    if ak > 0:
        ftext(c, "k = 5", 1340, 660, 70, "black", PURPLE, ak)
        text(c, "R$ 5 por quilo: a etiqueta", 1340, 730, 30, "bold", INK2, ak)


# ======================================================================
# teste 2 (torneiras)
# ======================================================================

TORN = [["1", "12"], ["2", "6"], ["3", "4"], ["4", "3"]]


def b_torneira(c, t, C, B):
    head_seq(c, t, C, [("06", "UMA CAIXA-D'ÁGUA", "TESTE 1 FALHOU", AMBER), ("07", "TESTE 2 DO DETETIVE", "MULTIPLICAR", PURPLE)])
    card(c, *CARD_R)
    sid = which(t, C, ["06", "07"])
    ts6 = lin_ts(C, "06", 4)
    a0 = ep(t, C["06"], 0.5)
    div = dict(aux_col(["12", "3", "", ""], [C["06.d1"], C["06.d2"], 1e9, 1e9], [RED, RED, RED, RED], C["06.v"]), op="÷")
    aux = [div]
    lupa_ts = [C["06.d1"], C["06.d2"]] if sid == "06" else None
    if sid == "07":
        ts7 = lin_ts(C, "07", 4)
        aux.append(dict(aux_col(["12", "12", "12", "12"], ts7, [GREEN] * 4, C["07.v"]), op="×"))
        lupa_ts = ts7
    tabela(c, t, 260, 205, ["torneiras", "horas"], TORN, a0, aux=aux, ts_lin=ts6, rh=100, size=48, w=(230, 200), wa=180,
           lupa_ts=lupa_ts)
    if sid == "06":
        av = ep(t, C["06.v"], 0.5)
        if av > 0:
            selo(c, 1420, 330, av, "MUDOU!", RED, -6, 40)
            text(c, "não é direta", 1420, 440, 36, "black", RED, av)
        ae = ep(t, C["06.e"], 0.5)
        if ae > 0:
            boxed(c, 1170, 530, 500, 200, AMBER, ae, 0.08)
            text(c, "muita gente para aqui…", 1420, 600, 32, "black", AMBER, ae)
            text(c, "o detetive, NÃO", 1420, 665, 40, "black", INK, ae)
        return
    aa = ep(t, C["07"], 0.5)
    chip(c, "TESTE 2: multiplicar", 1420, 260, PURPLE, aa, 30)
    av = ep(t, C["07.v"], 0.5)
    if av > 0:
        boxed(c, 1180, 400, 480, 150, GREEN, av, 0.08)
        text(c, "produto NÃO muda", 1420, 455, 34, "black", GREEN, av)
        text(c, "→ INVERSA", 1420, 512, 44, "black", GREEN, av)
    ak = ep(t, C["07.k"], 0.5)
    if ak > 0:
        ftext(c, "k = 12", 1420, 660, 70, "black", PURPLE, ak)
        text(c, "12 h de UMA torneira sozinha", 1420, 730, 28, "bold", INK2, ak)


# ======================================================================
# nenhuma das duas
# ======================================================================

def b_nenhuma(c, t, C, B):
    frame(c, t, B["start"], "E SE NENHUM DER CERTO?", "O ESTACIONAMENTO", AMBER)
    ts = lin_ts(C, "08", 3)
    tb, tc = C["08.b"], C["08.c"]
    div = dict(aux_col(["7", "4,5", "≈ 3,7"], [tb + 0.3, tb + 0.9, tb + 1.5], [RED] * 3, C["08.v"]), op="÷")
    mul = dict(aux_col(["7", "18", "33"], [tc + 0.3, tc + 0.9, tc + 1.5], [RED] * 3, C["08.v"]), op="×")
    tabela(c, t, 230, 220, ["horas", "R$"], [["1", "7"], ["2", "9"], ["3", "11"]], ep(t, C["08.a"], 0.5), aux=[div, mul],
           ts_lin=ts, rh=110, size=50, w=(200, 200), wa=220)
    av = ep(t, C["08.v"], 0.5)
    if av > 0:
        boxed(c, 1130, 250, 540, 200, RED, av, 0.08)
        text(c, "nenhum é constante", 1400, 320, 34, "black", RED, av)
        text(c, "NÃO há proporcionalidade", 1400, 385, 34, "black", INK, av)
    ax = ep(t, C["08.x"], 0.5)
    if ax > 0:
        selo(c, 1400, 600, ax, "REGRA DE TRÊS PROIBIDA", RED, -5, 34)


# ======================================================================
# o hábito: a coluna auxiliar
# ======================================================================

def b_auxiliar(c, t, C, B):
    frame(c, t, B["start"], "O HÁBITO QUE ECONOMIZA TEMPO", "A COLUNA AUXILIAR", GREEN)
    a0 = ep(t, C["09"], 0.5)
    ta = C["09.a"]
    aux = [dict(aux_col(["5", "5", "5"], [ta + 0.6, ta + 1.0, ta + 1.4], [GREEN] * 3, C["09.b"]), op="÷")]
    tabela(c, t, 260, 230, ["x", "y"], [["2", "10"], ["3", "15"], ["6", "30"]], a0, aux=aux, rh=100, size=48, w=(190, 190),
           wa=220)
    aa = ep(t, ta, 0.5)
    if aa > 0:
        text(c, "← escreva na MARGEM", 1000, 300, 32, "black", PURPLE, aa, align="left")
        text(c, "quociente ou produto, linha a linha", 1000, 350, 26, "bold", INK2, aa, align="left")
    ab = ep(t, C["09.b"], 0.5)
    if ab > 0:
        check_icon(c, 1020, 455, 22, ab, GREEN)
        text(c, "qual é a relação: DIRETA", 1060, 466, 32, "black", INK, ab, align="left")
    acc = ep(t, C["09.c"], 0.5)
    if acc > 0:
        check_icon(c, 1020, 535, 22, acc, GREEN)
        ftext(c, "quanto vale o k: 5", 1060, 546, 32, "black", INK, acc, align="left")
    ad = ep(t, C["09.d"], 0.5)
    if ad > 0:
        K.atalho(c, 300, 668, 1320, 140, "ATALHO", ["a coluna auxiliar mostra a relação E o k, que costuma ser a próxima pergunta"],
                 ad, 30)


# ======================================================================
# teste todas as linhas
# ======================================================================

def b_todas(c, t, C, B):
    frame(c, t, B["start"], "QUANTAS LINHAS TESTAR?", "UMA SÓ ENGANA", AMBER)
    ts = lin_ts(C, "10", 3)
    aux = [dict(aux_col(["3", "3", "4"], ts, [GREEN, GREEN, RED], ts[2]), op="÷")]
    tabela(c, t, 300, 220, ["x", "y"], [["2", "6"], ["4", "12"], ["5", "20"]], ep(t, C["10.a"], 0.5), aux=aux, rh=110,
           size=52, w=(200, 200), wa=220, lupa_ts=ts)
    a2 = ep(t, C["10.r2"] + 0.6, 0.5) * (1 - ep(t, C["10.r3"], 0.3))
    if a2 > 0:
        text(c, "parece direta…", 1340, 330, 40, "black", AMBER, a2)
    a3 = ep(t, C["10.r3"], 0.4)
    if a3 > 0:
        selo(c, 1340, 330, a3, "QUATRO!", RED, -6, 40)
        text(c, "não é direta", 1340, 430, 34, "black", RED, a3)
    av = ep(t, C["10.v"], 0.5)
    if av > 0:
        boxed(c, 1050, 500, 580, 130, BLUE, av, 0.08)
        text(c, "uma linha sozinha SEMPRE dá um número", 1340, 552, 26, "black", INK, av)
        text(c, "a prova é o número se REPETIR", 1340, 600, 30, "black", BLUE, av)
    ak = ep(t, C["10.k"], 0.5)
    if ak > 0:
        K.atalho(c, 1050, 660, 580, 140, "ATALHO", ["teste TODAS as linhas"], ak, 36)


# ======================================================================
# nós fazemos
# ======================================================================

EX = [("A", [["2", "30"], ["4", "15"], ["6", "10"]], "15 · 3,75 · 1,67", RED, "60 · 60 · 60", GREEN, "INVERSA · k = 60", PURPLE),
      ("B", [["2", "14"], ["3", "21"], ["7", "49"]], "7 · 7 · 7", GREEN, "", None, "DIRETA · k = 7", GREEN),
      ("C", [["1", "8"], ["2", "10"], ["4", "14"]], "8 · 5 · 3,5", RED, "8 · 20 · 56", RED, "NENHUMA", RED)]


def b_exercicio(c, t, C, B):
    head_seq(c, t, C, [("11", "SUA VEZ", "PAUSE E TESTE", GREEN), ("12", "VAMOS CONFERIR", "OS DOIS TESTES", GREEN)])
    card(c, *CARD_R)
    conf = t >= C["12"]
    for k, (L, rows, dv, dcol, mv, mcol, ver, vcol) in enumerate(EX):
        a = ep(t, C[f"11.{'abc'[k]}"], 0.5)
        cx = 420 + k * 540
        if a <= 0:
            continue
        text(c, f"TABELA {L}", cx, 225, 30, "black", INK2, a)
        tabela(c, t, cx - 140, 250, ["x", "y"], rows, a, w=(140, 140), rh=66, size=38)
        if not conf:
            continue
        cd = {"A": "12.a", "B": "12.b", "C": "12.c"}[L]
        cm = {"A": "12.a2", "C": "12.c2"}.get(L)
        a1 = ep(t, C[cd], 0.4)
        if a1 > 0:
            fmid(c, "÷", cx - 200, 560, 34, "black", PURPLE, a1)
            ftext(c, dv, cx + 20, 572, 32, "black", dcol, a1)
        if cm and mv:
            a2 = ep(t, C[cm], 0.4)
            if a2 > 0:
                fmid(c, "×", cx - 200, 625, 34, "black", PURPLE, a2)
                ftext(c, mv, cx + 20, 637, 32, "black", mcol, a2)
        tv = C[cm] + 2.6 if cm else C[cd] + 2.2
        av = ep(t, tv, 0.4)
        chip(c, ver, cx, 715, vcol, av, 30)
    if not conf:
        pause_timer(c, t, C["11.end"] - 1.9, W / 2, 680)


# ======================================================================
# recap, erros
# ======================================================================

FRASES = ["Divide: constante? Direta.", "Multiplica: constante? Inversa.", "Teste todas as linhas, nunca uma só."]


def b_recap(c, t, C, B):
    sid = which(t, C, ["13", "20"])
    frame(c, t, B["start"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "13" else "PARA FECHAR", PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 300 + k * 170 + d
        badge_num(c, k + 1, 260, y - 16, a, 36, bg=PURPLE)
        para(c, s, 320, y, 50, "black", INK, a, 1340, 58)


ERROS = [("Testar uma linha só e chamar aquele número de k", "a conta deu um número bonito",
          "uma linha sozinha sempre dá algum número: só a repetição em TODAS prova a relação"),
         ("Desistir depois do primeiro teste", "a divisão não deu constante e parece que não há relação",
          "falta o teste 2: multiplique. A relação pode ser INVERSA"),
         ("Regra de três numa tabela sem proporcionalidade", "os números crescem juntos",
          "regra de três só com quociente ou produto constante; nenhum dos dois? PROIBIDA")]


def b_erros(c, t, C, B):
    K.erro_cards(c, t, C, ["14", "15", "16"], ERROS)


# ======================================================================
# Questão 1 do material
# ======================================================================

def _enunciado(c, linhas, a, y0=250, size=34, w=640):
    y = y0
    for s, col in linhas:
        for ln in K.wrap(s, "black", size, w):
            text(c, ln, 190, y, size, "black", col, a, align="left")
            y += size + 12
        y += 8
    return y


ENUN_Q1 = ("Um estudo registrou os seguintes pares de valores para duas grandezas x e y: (3; 40), (5; 24), (8; 15) e (12; 10).",
           "Sobre essas grandezas, é correto afirmar que")
ALTS1 = [("A", "são diretamente proporcionais, com k = 120", "produto constante é INVERSA", RED),
         ("B", "são inversamente proporcionais, com k = 120", "", GREEN),
         ("C", "são diretamente proporcionais, com k = 13", "testou só a 1ª linha", RED),
         ("D", "são inversamente proporcionais, com k = 43", "somou 3 + 40", RED),
         ("E", "não guardam relação de proporcionalidade", "desistiu no 1º teste", RED)]
Q1 = [["3", "40"], ["5", "24"], ["8", "15"], ["12", "10"]]


def b_q1(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO · RECONHECER PELA TABELA", "PAUSE E TENTE", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["17.a"], 0.4)
    _enunciado(c, [(ENUN_Q1[0], INK), (ENUN_Q1[1], BLUE)], a0, 240, 32, 660)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0, align="left")
    cues_in = {L: C[f"17.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"19.x{L.lower()}"] for L in "ACDE"}
    if t >= C["17.qa"] - 0.3:
        alts = [(L, txt, "", col) for L, txt, why, col in ALTS1]
        K.alternativas(c, t, C, alts, 960, 220, 720, 28, C["18.ok"], "B", cues_in, cues_x, gap=40)
        # motivo do erro logo abaixo de cada alternativa riscada (o texto do material é longo demais para a etiqueta ao lado)
        for j, (L, txt, why, col) in enumerate(ALTS1):
            ax = ep(t, cues_x.get(L, 1e9), 0.4)
            if why and ax > 0:
                pill(c, why, 1680, 220 + j * 86 + 64, col, size=20, a=ax, anchor="right", bounds=(0, 1920))
    if t < C["18"]:
        pause_timer(c, t, C["17.end"] - 1.9, 520, 640)
        return
    ra = ep(t, C["18"], 0.4)
    rrect(c, 160, 488, 740, 340, 18, "#FFFFFF", ra, shadow=True)
    div = dict(aux_col(["≈ 13,3", "4,8", "", ""], [C["18.d1"], C["18.d2"], 1e9, 1e9], [RED] * 4, C["18.b"]), op="y ÷ x")
    mul = dict(aux_col(["120"] * 4, lin_ts(C, "18", 4), [GREEN] * 4, C["18.v"]), op="x · y")
    tabela(c, t, 190, 500, ["x", "y"], Q1, ra, aux=[div, mul], w=(130, 130), wa=190, rh=52, size=32)
    av = ep(t, C["18.v"], 0.4)
    if av > 0:
        chip(c, "INVERSA · k = 120", 530, 795, GREEN, av, 28)
    ab = ep(t, C["18.b"], 0.4) * (1 - av)
    if ab > 0:
        chip(c, "÷ mudou: não é direta", 530, 795, RED, ab, 26)


# ======================================================================
# ponte e CTA
# ======================================================================

def _eixos(c, x, y, w, h, a):
    arrow(c, x, y + h, x + w, y + h, INK2, a, 4, 12)
    arrow(c, x, y + h, x, y, INK2, a, 4, 12)


def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "O GRÁFICO DE CADA RELAÇÃO", PURPLE)
    aa = ep(t, C["21.a"], 0.5)
    ab = ep(t, C["21.b"], 0.8)
    acc = ep(t, C["21.c"], 0.8)
    xs = [300, 790, 1280]
    for k, x in enumerate(xs):
        _eixos(c, x, 250, 360, 300, aa)
    if ab > 0:
        line(c, 300, 550, 300 + 330 * ab, 550 - 270 * ab, GREEN, 1, 7)
        text(c, "direta", 480, 620, 32, "black", GREEN, ab)
        p = skia.Path()
        for i in range(61):
            u = i / 60
            xx = 790 + 30 + u * 320
            yy = 550 - min(290, 9000 / (xx - 790 + 1e-6) * 0.9)
            p.moveTo(xx, yy) if i == 0 else p.lineTo(xx, yy)
        c.save(); c.clipRect(skia.Rect.MakeXYWH(790, 240, 360 * ab, 320))
        c.drawPath(p, paint(BLUE, 1, stroke=7, cap_round=True))
        c.restore()
        text(c, "inversa", 970, 620, 32, "black", BLUE, ab)
    if acc > 0:
        line(c, 1280, 470, 1280 + 330 * acc, 470 - 200 * acc, AMBER, 1, 7)
        fmid(c, "?", 1600, 330, 80, "black", AMBER, acc)
        text(c, "a reta que engana", 1460, 620, 32, "black", AMBER, acc)
    pill(c, "ep. 3 · o gráfico e a armadilha da parcela fixa", W / 2, 760, PURPLE, size=32, a=ep(t, C["21.d"], 0.5),
         anchor="center")


def b_cta(c, t, C, B):
    cta(c, t, C["22.like"], C["22.sub"], C["22.bell"], C["22.com"], C["22.bye"], "Você já desistiu depois do 1º teste?",
        canal="no Estudativo", anki=C["22.anki"])


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, arroz=b_arroz, teste1=b_teste1, torneira=b_torneira,
              nenhuma=b_nenhuma, auxiliar=b_auxiliar, todas=b_todas, exercicio=b_exercicio, recap=b_recap, erros=b_erros,
              q1=b_q1, ponte=b_ponte, cta=b_cta)
