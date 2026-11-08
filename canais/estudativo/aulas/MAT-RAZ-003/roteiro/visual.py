"""Visual — Estudativo · MAT-RAZ-003: o truque do k.
Peças locais: fila() é a fila de pacotinhos iguais (a barra cortada em k pedaços, mesma linguagem de MAT-RAZ-013/014: o 1º número
na cor da matéria, o 2º em preto, o 3º em cinza), com o que vai dentro de cada pacotinho escrito no meio (?, k, 8...);
troca() faz a equação evoluir no lugar. Na tela a letra é "k" (a voz diz "cá").
Instantes: cues C[...] e, dentro da frase, a palavra falada (PW, lida de audio/tempos.json)."""
import json
import unicodedata
from pathlib import Path

import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Razão e Proporção")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-RAZ-003_truque_do_k.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("ideia", "resolver", "atalho", "questao", "fim"))
BR = "#FFFFFF"
# as contas da aula, conferidas
assert 3 + 5 == 8 and 64 // 8 == 8 and 3 * 8 == 24 and 5 * 8 == 40 and 24 + 40 == 64 and 24 / 40 == 3 / 5
assert 40 - 24 == 16 and 16 // 2 == 8
assert 2 + 3 + 5 == 10 and 50 // 10 == 5 and (2 * 5, 3 * 5, 5 * 5) == (10, 15, 25)
assert round(3 * 64 / 5, 1) == 38.4 and round(64 - 38.4, 1) == 25.6
assert 5 + 2 == 7 and 1400 // 7 == 200 and 2 * 200 == 400 and 5 * 200 == 1000 and 1000 + 400 == 1400

_TEMPOS = json.loads((Path(__file__).resolve().parents[1] / "audio" / "tempos.json").read_text(encoding="utf-8"))


def _n(s):
    return "".join(ch for ch in unicodedata.normalize("NFD", s.lower()) if ch.isalnum())


def PW(sid, palavra, n=1):
    """instante em que a voz diz a n-ésima `palavra` da cena sid"""
    for s in _TEMPOS["scenes"]:
        if s["id"] == sid:
            k = 0
            for tk in s["tokens"]:
                if _n(tk["disp"]) == _n(palavra):
                    k += 1
                    if k == n:
                        return s["start"] + tk["t0"]
    raise KeyError((sid, palavra, n))


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças desta aula ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    """uma frase, palavra a palavra, no mesmo estilo"""
    return [(w, est, size, cor) for w in txt.split()]


def fcen(c, t, t0, s, cx, y, size, cor=None):
    E.formula_em(c, t, t0, s, cx, y, size, "g", cor, "center")


def bola_res(c, t, t0, s, cx, cy, r=140, size=84, cor=None):
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r, cor, a), E.formula(c, s, cx, cy + size * 0.36, size, "g", E.SOBRE, a, "center")))


def troca(c, t, estados, cx, y, size):
    """equação que evolui no lugar: estados = [(t0, fórmula, cor)]; cada uma sai quando a próxima entra"""
    for i, (t0, s, cor) in enumerate(estados):
        if t < t0:
            break
        t1 = estados[i + 1][0] if i + 1 < len(estados) else 1e9
        E.saida(c, t, t1 - 0.15, lambda t0=t0, s=s, cor=cor: fcen(c, t, t0, s, cx, y, size, cor), d=0.3)


def fila(c, t, t0, n, x, y, pw, h, cor, rot=None, size=54, escuro=False, gap=10, passo=0.08):
    """n pacotinhos iguais (largura pw) lado a lado, entrando um por um a partir de t0.
    rot(i) devolve o texto de dentro do pacotinho i (ou None)"""
    for i in range(n):
        q = ep(t, t0 + i * passo, 0.4)
        if q <= 0:
            continue
        k = ease_back(prog(t, t0 + i * passo, 0.4))
        px = x + i * (pw + gap)
        ww, hh = pw * k, h * k
        cx, cy = px + pw / 2, y + h / 2
        M.rrect(c, cx - ww / 2, cy - hh / 2, ww, hh, 14, cor, q)
        if not escuro:
            M.line(c, cx - ww / 2 + 12, cy - hh / 2 + 10, cx + ww / 2 - 12, cy - hh / 2 + 10, BR, q * 0.35, 3)
        s = rot(i) if rot else None
        if s:
            centro(c, s, cx, cy + size * 0.36, size, "g", BR, q)
    return n * (pw + gap) - gap


def larg_fila(n, pw, gap=10):
    return n * (pw + gap) - gap


def rotulo_tempo(t, mudas):
    """texto de dentro conforme o tempo: mudas = [(t0, texto), ...] em ordem"""
    s = None
    for t0, txt in mudas:
        if t >= t0:
            s = txt
    return s


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    a1, b1, c1 = C["s01.a"], C["s01.b"], C["s01.c"]

    def cena():
        E.frase(c, t, a1, ps("razão", "i", 84) + [("3 para 5", "g", 96, COR)], W / 2, 220, "center", 0.12)
        E.frase(c, t, b1, ps("e somam", "i", 84) + [("64", "g", 96, COR)], W / 2, 350, "center", 0.12)
        tq = PW("s01", "Quais")
        for cx, v, cor in ((760, "3", COR), (1160, "5", TINTA)):
            if t < c1:
                E.foco(c, t, tq, 0.5, lambda a, cx=cx: (M.rrect(c, cx - 110, 470, 220, 200, 24, CINZA, a * 0.25),
                                                        centro(c, "?", cx, 620, 150, "g", CINZA, a)))
            else:
                E.foco(c, t, c1 if v == "3" else PW("s01", "cinco", 2), 0.5, lambda a, cx=cx, v=v, cor=cor: (
                    M.rrect(c, cx - 110, 470, 220, 200, 24, cor, a), centro(c, v, cx, 620, 150, "g", BR, a)))
        E.foco(c, t, PW("s01", "Somam", 2), 0.5, lambda a: E.formula(c, "3 + 5 = 8", W / 2, 820, 96, "g", ERRADO, a, "center"))
        E.foco(c, t, PW("s01", "nao"), 0.5, lambda a: E.pilula(c, "não é 64", 1380, 790, 52, "g", fundo=ERRADO, a=a))
        E.frase(c, t, PW("s01", "Com"), ps("com", "i", 70) + [("1 letra só,", "g", 70, COR)] + ps("em uma linha", "i", 70), W / 2, 980, "center", 0.12)
    E.saida(c, t, C["s02"] - 0.1, cena)

    if t >= C["s02"]:
        ta, tb = C["s02.a"], C["s02.b"]
        E.foco(c, t, tb - 0.2, 0.7, lambda a: E.bola(c, 1500, 540, 250 * ease_back(prog(t, tb - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, ps("até o fim desta aula", "i", 90), XE, 330, passo=0.14)
        E.frase(c, t, PW("s02", "divide"), ps("dividir", "i", 84) + [("qualquer total", "g", 96, COR)], XE, 490, passo=0.12)
        E.frase(c, t, PW("s02", "numa"), ps("numa", "i", 84) + [("razão dada", "g", 84, COR)], XE, 640, passo=0.12)
        E.foco(c, t, tb + 0.1, 0.5, lambda a: (centro(c, "+ atalho", 1500, 525, 80, "g", E.SOBRE, a),
                                               centro(c, "de prova", 1500, 610, 80, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"] + 0.3, ps("você precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "2", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 960, 800
    itens = (("s03.b", "o que é", "razão e proporção"), ("s03.c", "transformar o problema", "em equação"))
    for i, (k, l1, l2) in enumerate(itens):
        y = 280 + i * 260
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 196, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 60)], x + 44, y + 84)
        E.frase(c, t, C[k] + 0.3, [(l2, "g", 60, COR)], x + 44, y + 160)
    q1 = ease_io(prog(t, C["s03.c"] - 0.35, 0.5))
    E.cursor(c, x + w - 30, lerp(450, 710, q1), ep(t, C["s03.b"], 0.4))
    E.frase(c, t, PW("s03", "faltar"), ps("faltou alguma?", "i", 58, COR) + ps("procure no canal", "i", 58), 960, 960, "left", 0.12)


# ---------------- a ideia: pacotinhos ----------------
PX, PW1, PH = 430, 150, 110  # filas grandes da ideia


def b_ideia(c, t, C, b):
    a4, b4, c4, d4 = C["s04.a"], C["s04.b"], C["s04.c"], C["s04.d"]
    a5, b5, c5, d5, e5 = C["s05.a"], C["s05.b"], C["s05.c"], C["s05.d"], C["s05.e"]
    E.saida(c, t, C["s05"] - 0.1, lambda: (
        E.frase(c, t, a4, ps("a cada", "i", 80) + [("3", "g", 84, COR)] + ps("de um,", "i", 80) + [("5", "g", 84, TINTA)] + ps("do outro", "i", 80),
                W / 2, 170, "center", 0.12),
        E.frase(c, t, b4, ps("pense em", "i", 70) + [("pacotinhos iguais", "g", 70, COR)], W / 2, 280, "center", 0.12)))
    if t >= C["s05"]:
        E.frase(c, t, C["s05"] + 0.3, ps("por que não usar", "i", 80) + [("a cruz?", "g", 80, COR)], W / 2, 170, "center", 0.12)
        E.saida(c, t, b5 - 0.2, lambda: E.frase(c, t, a5, ps("nenhum número", "i", 66) + [("é conhecido", "g", 66, ERRADO)], W / 2, 280, "center", 0.12))
        E.foco(c, t, b5, 0.5, lambda a: E.pilula(c, "tamanho do pacotinho = k", W / 2, 270, 56, "g", a=a))
    tn = PW("s05", "Nao", 2)
    rot = lambda i: rotulo_tempo(t, [(tn, "?"), (b5, "k")])
    y1, y2 = 400, 600
    E.foco(c, t, c4, 0.5, lambda a: E.escreve(c, "1º número", XE, y1 + 72, 50, "i", COR, a))
    fila(c, t, c4, 3, PX, y1, PW1, PH, E.COR, rot, 64)
    E.foco(c, t, d4, 0.5, lambda a: E.escreve(c, "2º número", XE, y2 + 72, 50, "i", TINTA, a))
    fila(c, t, d4, 5, PX, y2, PW1, PH, TINTA, rot, 64)
    xr = PX + larg_fila(5, PW1) + 60
    E.foco(c, t, c5, 0.5, lambda a: E.escreve(c, "= 3k", PX + larg_fila(3, PW1) + 50, y1 + 85, 90, "g", COR, a))
    E.foco(c, t, d5, 0.5, lambda a: E.escreve(c, "= 5k", xr, y2 + 85, 90, "g", TINTA, a))
    fcen(c, t, e5, "f{3k}{5k} = f{3}{5}", W / 2, 920, 84, TINTA)


# ---------------- resolver ----------------
RX, RW, RH = 300, 120, 96
R1, R2 = 230, 360


def _rot_resolver(t, C):
    """o que vai dentro dos pacotinhos durante o bloco: k, depois 8 (s07, s08), k de novo na diferença e 8 quando sai"""
    return rotulo_tempo(t, [(0, "k"), (PW("s07", "Cada"), "8"), (C["s09"], "k"), (PW("s09", "oito", 1), "8")])


def b_resolver(c, t, C, b):
    a6, b6, c6 = C["s06.a"], C["s06.b"], C["s06.c"]
    a7, b7 = C["s07.a"], C["s07.b"]
    a8, b8, c8 = C["s08.a"], C["s08.b"], C["s08.c"]
    a9, b9, c9, d9, e9 = C["s09.a"], C["s09.b"], C["s09.c"], C["s09.d"], C["s09.e"]
    rot = lambda i: _rot_resolver(t, C)
    t0 = C["s06"] + 0.2
    fila(c, t, t0, 3, RX, R1, RW, RH, E.COR, rot, 54)
    fila(c, t, t0 + 0.3, 5, RX, R2, RW, RH, TINTA, rot, 54)
    xr = RX + larg_fila(5, RW) + 40  # à direita das filas
    # soma 64: chave vertical à direita das duas filas (até a diferença)
    ts = PW("s06", "somam")

    def soma():
        p = ep(t, ts, 0.5)
        if p > 0:
            M.line(c, xr, R1, xr, R2 + RH, TINTA2, p, 5)
            M.line(c, xr - 18, R1, xr, R1, TINTA2, p, 5)
            M.line(c, xr - 18, R2 + RH, xr, R2 + RH, TINTA2, p, 5)
        E.foco(c, t, ts + 0.3, 0.5, lambda a: E.escreve(c, "juntos: 64", xr + 30, (R1 + R2 + RH) / 2 + 22, 64, "g", TINTA, a))
    E.saida(c, t, a7 - 0.1, soma)

    # s06: a equação
    def equacao():
        troca(c, t, [(a6, "3k + 5k = 64", TINTA), (b6, "8k = 64", TINTA), (c6, "k = 64 ÷ 8", TINTA)], 760, 700, 110)
        bola_res(c, t, PW("s06", "ca", 4), "k = 8", 1450, 670, 120, 76)
    E.saida(c, t, C["s07"] - 0.1, equacao)

    # s07 e s08: os números e a conferência
    def numeros():
        E.foco(c, t, a7, 0.5, lambda a: E.formula(c, "3 · 8 = 24", RX + larg_fila(3, RW) + 40, R1 + 70, 76, "g", COR, a))
        E.foco(c, t, b7, 0.5, lambda a: E.formula(c, "5 · 8 = 40", xr, R2 + 70, 76, "g", TINTA, a))
        fcen(c, t, a8, "24 + 40 = 64", 540, 760, 90, TINTA)
        E.foco(c, t, a8 + 1.2, 0.5, lambda a: E.selo(c, 900, 730, 40, True, a))
        E.foco(c, t, b8, 0.5, lambda a: E.fracao(c, 24, 40, 1180, 730, 110, TINTA, a))
        E.pontes(c, t, 1280, 1460, 730, 110, "÷ 8", PW("s08", "dividindo"), PW("s08", "dividindo") + 0.3, size=40)
        E.foco(c, t, c8, 0.5, lambda a: E.fracao(c, 3, 5, 1560, 730, 110, CERTO, a))
        E.foco(c, t, PW("s08", "Bateu"), 0.5, lambda a: E.selo(c, 1760, 720, 46, True, a))
    if t >= C["s07"]:
        E.saida(c, t, C["s09"] - 0.1, numeros)

    # s09: a diferença são 2 pacotinhos
    if t >= C["s09"]:
        x0 = RX + 3 * (RW + 10) - 4
        x1 = RX + larg_fila(5, RW) + 4
        E.foco(c, t, a9, 0.5, lambda a: E.pilula(c, "a diferença", 1500, 260, 56, "g", a=a))
        p = ep(t, PW("s09", "dezesseis"), 0.5)
        E.caixa_pontilhada(c, x0, R2 - 14, x1 - x0, RH + 28, p, E.COR, prog_=p)
        E.foco(c, t, PW("s09", "dezesseis") + 0.2, 0.5, lambda a: E.escreve(c, "16 a mais", x1 + 30, R2 + 70, 60, "g", COR, a))
        troca(c, t, [(b9, "5k − 3k = 16", TINTA), (c9, "2k = 16", TINTA)], 760, 700, 110)
        bola_res(c, t, PW("s09", "ca", 4), "k = 8", 1450, 670, 120, 76)
        E.frase(c, t, d9, ps("os mesmos", "i", 70) + [("24", "g", 76, COR)] + ps("e", "i", 70) + [("40", "g", 76, TINTA)], W / 2, 900, "center", 0.12)
        E.foco(c, t, e9, 0.5, lambda a: E.pilula(c, "2 pacotinhos", (x0 + x1) / 2, R2 + RH + 70, 46, "g", a=a))


# ---------------- três números ----------------
def b_tres(c, t, C, b):
    a10, b10, c10, d10, e10 = C["s10.a"], C["s10.b"], C["s10.c"], C["s10.d"], C["s10.e"]
    E.frase(c, t, a10, ps("e com", "i", 84) + [("3 números?", "g", 84, COR)], W / 2, 160, "center", 0.12)
    E.frase(c, t, b10, ps("razão", "i", 66) + [("2 : 3 : 5,", "g", 70, COR)] + ps("soma", "i", 66) + [("50", "g", 70, COR)], W / 2, 270, "center", 0.12)
    rot = lambda i: rotulo_tempo(t, [(0, "k"), (d10, "5")])
    x, pw, h = 300, 110, 90
    ys = (350, 470, 590)
    for (n, cor, t0), y in zip(((2, E.COR, PW("s10", "dois", 2)), (3, TINTA, PW("s10", "tres", 3)), (5, CINZA, PW("s10", "cinco", 2))), ys):
        fila(c, t, t0, n, x, y, pw, h, cor, rot, 50)
    for (v, cor, t0), y, n in zip((("= 10", COR, e10), ("= 15", TINTA, PW("s10", "quinze")), ("= 25", TINTA2, PW("s10", "vinte"))), ys, (2, 3, 5)):
        E.foco(c, t, t0, 0.5, lambda a, v=v, cor=cor, y=y, n=n: E.escreve(c, v, x + larg_fila(n, pw) + 40, y + 70, 76, "g", cor, a))
    troca(c, t, [(c10, "2k + 3k + 5k = 50", TINTA), (PW("s10", "dez"), "10k = 50", TINTA)], 760, 860, 96)
    bola_res(c, t, d10, "k = 5", 1500, 830, 110, 70)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    a11, b11, c11, d11 = C["s11.a"], C["s11.b"], C["s11.c"], C["s11.d"]
    a12, b12, c12 = C["s12.a"], C["s12.b"], C["s12.c"]
    E.frase(c, t, C["s11"] + 0.4, ps("o erro", "i", 90) + [("mais comum", "g", 90, ERRADO)], W / 2, 170, "center", 0.12)
    E.linha(c, t, [("3 para 5", "g", 70, COR, a11), ("não é", "i", 70, TINTA, a11 + 0.4), ("3/5 do total", "g", 70, ERRADO, PW("s11", "quintos"))], W / 2, 290, "center")
    fcen(c, t, b11, "f{3}{5} · 64 =", 760, 480, 100, TINTA)
    E.foco(c, t, c11, 0.5, lambda a: E.pilula(c, "38,4", 1200, 450, 80, "g", fundo=ERRADO, a=a))
    E.foco(c, t, d11, 0.5, lambda a: (E.escreve(c, "sobram", 1050, 610, 56, "i", TINTA, a)))
    E.foco(c, t, d11 + 0.2, 0.5, lambda a: E.pilula(c, "25,6", 1400, 590, 64, "g", fundo=TINTA, a=a))
    E.foco(c, t, a12, 0.5, lambda a: E.escreve(c, "o 1º devia ser o menor", 300, 640, 54, "i", ERRADO, a))
    E.foco(c, t, PW("s12", "maior"), 0.5, lambda a: E.selo(c, 1600, 450, 44, False, a))
    # 8 partes do total
    x, w, y, h = 420, 1080, 720, 110
    n = 8
    tb = b12
    for i in range(n):
        cor = E.COR if i < 3 else TINTA
        ti = tb + 0.3 + i * 0.07
        E.foco(c, t, ti, 0.35, lambda a, i=i, cor=cor: M.rrect(c, x + i * w / n + 4, y, w / n - 8, h, 14, cor, a))
    E.foco(c, t, tb, 0.5, lambda a: E.escreve(c, "total", XE, y + 72, 52, "i", TINTA2, a))
    E.foco(c, t, PW("s12", "oito") , 0.5, lambda a: E.pilula(c, "3 + 5 = 8 partes", 1700, y + 55, 40, "g", fundo=TINTA, a=a))
    E.chave(c, x + 6, x + 3 * w / n - 6, y + h + 12, COR, ep(t, c12, 0.5), 22)
    fcen(c, t, c12 + 0.2, "f{3}{8} do total", x + 1.5 * w / n + 60, y + h + 190, 64, COR)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    a13, b13, c13, d13, e13, f13 = C["s13.a"], C["s13.b"], C["s13.c"], C["s13.d"], C["s13.e"], C["s13.f"]

    def partes8():
        E.frase(c, t, C["s13"] + 0.3, ps("o atalho:", "i", 76, CLARO), W / 2, 150, "center", 0.12)
        E.frase(c, t, a13, ps("divida o total pelo", "i", 76, CLARO) + ps("número de partes", "g", 76, BR), W / 2, 260, "center", 0.12)
        x, pw, y, h = 380, 140, 430, 120
        rot = lambda i: rotulo_tempo(t, [(PW("s13", "oito", 3), "8")])
        fila(c, t, b13, 3, x, y, pw, h, E.COR, rot, 56, escuro=True)
        fila(c, t, b13 + 0.3, 5, x + 3 * (pw + 10), y, pw, h, CLARO, rot, 56, escuro=True)
        E.foco(c, t, b13 + 0.8, 0.5, lambda a: E.pilula(c, "8 partes", x + larg_fila(8, pw) + 130, y + 60, 46, "g", fundo=CLARO, cor="#07070F", a=a))
        fcen(c, t, c13, "64 ÷ 8 = 8", W / 2, 380, 70, CLARO)
        x3 = x + larg_fila(3, pw)
        E.chave(c, x + 6, x3 - 6, y + h + 16, CLARO, ep(t, d13, 0.5), 22)
        E.foco(c, t, d13 + 0.2, 0.5, lambda a: centro(c, "3 · 8 = 24", (x + x3) / 2, y + h + 110, 64, "g", BR, a))
        x5 = x + larg_fila(8, pw)
        E.chave(c, x3 + 16, x5 - 6, y + h + 16, CLARO, ep(t, e13, 0.5), 22)
        E.foco(c, t, e13 + 0.2, 0.5, lambda a: centro(c, "5 · 8 = 40", (x3 + x5) / 2, y + h + 110, 64, "g", BR, a))
        E.foco(c, t, PW("s13", "Sem"), 0.5, lambda a: E.pilula(c, "sem equação", W / 2, 850, 56, "g", a=a))
        fcen(c, t, f13, "f{3}{8} de 64:  64 ÷ 8 · 3 = 24", W / 2, 990, 64, CLARO)
    E.saida(c, t, C["s14"] - 0.1, partes8)

    if t >= C["s14"]:
        a14, b14, c14 = C["s14.a"], C["s14.b"], C["s14.c"]
        E.frase(c, t, a14, ps("somar as partes =", "i", 76, CLARO) + ps("juntar os k", "g", 76, BR), W / 2, 260, "center", 0.12)
        fcen(c, t, PW("s14", "oito"), "3k + 5k = 8k:  8 partes", W / 2, 400, 76, BR)
        E.frase(c, t, b14, ps("não compensa se", "i", 66, CLARO) + ps("mistura outras contas", "g", 66, BR), W / 2, 590, "center", 0.12)
        E.foco(c, t, PW("s14", "dobro"), 0.5, lambda a: E.pilula(c, "2 · 1º + 2º", W / 2, 690, 50, "g", fundo=ERRADO, cor=BR, a=a))
        E.frase(c, t, c14, ps("aí,", "i", 90, CLARO) + ps("escreva com k", "g", 90, BR), W / 2, 880, "center", 0.12)
        E.frase(c, t, PW("s14", "monte"), ps("e monte a equação", "i", 66, CLARO), W / 2, 980, "center", 0.12)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    a15, b15, c15 = C["s15.a"], C["s15.b"], C["s15.c"]
    E.frase(c, t, C["s15"] + 0.3, ps("hora de testar", "i", 72, COR), XE, 200)
    E.frase(c, t, a15, ps("farinha e açúcar", "i", 80), XE, 340, passo=0.12)
    E.frase(c, t, PW("s15", "razao"), ps("na razão", "i", 80) + [("5 para 2", "g", 84, COR)], XE, 460, passo=0.12)
    E.frase(c, t, b15, ps("juntos:", "i", 80) + [("1.400 g", "g", 84, COR)], XE, 600, passo=0.12)
    E.frase(c, t, c15, ps("quantos gramas de", "i", 76) + [("açúcar?", "g", 80, COR)], XE, 800, passo=0.12)
    E.relogio(c, t, C["s16.a"], 1500, 470, 200)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    a17, b17, c17, d17 = C["s17.a"], C["s17.b"], C["s17.c"], C["s17.d"]
    a18, b18, c18, d18, e18 = C["s18.a"], C["s18.b"], C["s18.c"], C["s18.d"], C["s18.e"]
    x, pw, h = 420, 120, 96
    y1, y2 = 200, 330
    rot = lambda i: rotulo_tempo(t, [(0, "k"), (PW("s17", "duzentos"), "200")])
    E.foco(c, t, a17 - 0.4, 0.5, lambda a: E.escreve(c, "farinha", XE, y1 + 64, 50, "i", TINTA, a))
    fila(c, t, a17 - 0.3, 5, x, y1, pw, h, TINTA, rot, 40)
    E.foco(c, t, b17 - 0.4, 0.5, lambda a: E.escreve(c, "açúcar", XE, y2 + 64, 50, "i", COR, a))
    fila(c, t, b17 - 0.3, 2, x, y2, pw, h, E.COR, rot, 40)
    xf = x + larg_fila(5, pw) + 40
    E.foco(c, t, a17 + 0.2, 0.5, lambda a: E.formula(c, "5k", xf, y1 + 70, 76, "g", TINTA, a))
    E.foco(c, t, b17 + 0.2, 0.5, lambda a: E.formula(c, "2k", x + larg_fila(2, pw) + 40, y2 + 70, 76, "g", COR, a))

    def eq():
        troca(c, t, [(c17, "7k = 1.400", TINTA), (d17, "k = 1.400 ÷ 7", TINTA)], 760, 640, 104)
        bola_res(c, t, PW("s17", "duzentos"), "k = 200", 1450, 610, 130, 56)
    E.saida(c, t, C["s18"] - 0.1, eq)

    def contas():
        fcen(c, t, a18, "açúcar: 2 · 200 = 400 g", 760, 560, 76, COR)
        fcen(c, t, b18, "farinha: 5 · 200 = 1.000 g", 760, 690, 76, TINTA)
        fcen(c, t, c18, "1.000 + 400 = 1.400", 760, 850, 76, TINTA)
        E.foco(c, t, PW("s18", "Bateu"), 0.5, lambda a: E.selo(c, 1250, 825, 44, True, a))
    if t >= C["s18"]:
        E.saida(c, t, d18 - 0.3, contas)
    if t >= d18:
        E.frase(c, t, PW("s18", "atalho"), ps("pelo atalho:", "i", 66, COR), 760, 560, "center")
        fcen(c, t, d18, "5 + 2 = 7 partes", 760, 680, 80, TINTA)
        fcen(c, t, PW("s18", "Mil", 4), "1.400 ÷ 7 = 200 por parte", 760, 810, 70, TINTA)
        E.foco(c, t, PW("s18", "Duas"), 0.5, lambda a: E.escreve(c, "2 partes de açúcar", 1260, 930, 50, "i", COR, a))
    bola_res(c, t, a18 + 1.5, "400 g", 1600, 700, 130, 70, CERTO)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s19"], [("resumindo", "i", 92, COR)], W / 2, 230, "center")
        itens = (("s19.a", "3 para 5: os números são 3k e 5k"), ("s19.b", "ache o k e multiplique"))
        for i, (k, s) in enumerate(itens):
            y = 470 + i * 220
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 260, y - 30, 56, a=a), centro(c, str(i + 1), 260, y - 7, 64, "g", E.SOBRE, a)))
            E.frase(c, t, C[k] + 0.1, [(s, "g", 76)], 360, y)
    E.saida(c, t, C["s20"] - 0.1, resumo)
    if t < C["s20"]:
        return
    a20, b20, c20, d20, e20 = C["s20.a"], C["s20.b"], C["s20.c"], C["s20.d"], C["s20.e"]
    E.frase(c, t, C["s20"] + 0.2, ps("próxima aula", "i", 84), XE, 280)
    E.frase(c, t, a20, [("grandezas", "g", 110, COR)], XE, 420)
    E.frase(c, t, PW("s20", "juntas"), ps("que andam", "i", 70) + [("juntas", "g", 70, COR)], XE, 530, passo=0.12)
    E.frase(c, t, PW("s20", "contrario"), ps("ou", "i", 70) + [("ao contrário", "g", 70, COR)], XE, 630, passo=0.12)
    E.linha(c, t, [("quilos e preço", "i", 60, TINTA2, b20), ("·", "i", 60, TINTA2, c20), ("velocidade e tempo", "i", 60, TINTA2, c20)], XE, 740)
    E.foco(c, t, d20, 0.5, lambda a: E.pilula(c, "Inscreva-se", 1430, 400, 76, estilo="g", a=a))
    p = ease_io(prog(t, d20 + 0.3, 0.8))
    E.cursor(c, lerp(1760, 1560, p), lerp(720, 425, p), ep(t, d20 + 0.2, 0.4))
    E.frase(c, t, e20, [("bons", "i", 120), ("estudos!", "i", 120, COR)], W / 2, 940, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, ideia=b_ideia, resolver=b_resolver, tres=b_tres, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
