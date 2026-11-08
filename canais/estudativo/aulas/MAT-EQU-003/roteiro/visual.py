"""Visual — Estudativo · MAT-EQU-003: juntar termos semelhantes.
Caixas de ovos fechadas são o x: três caixas e cinco caixas viram uma fila de oito, e os ovos quebrados ficam soltos.
Depois, termo e semelhante na expressão, a prova com x = 10, a expressão bagunçada, o erro do sinal e, no palco,
o atalho de circular os termos com x e sublinhar os números soltos.
Instantes: os cues de C[...] e, para cada palavra, pal(cena, palavra), lido da voz gravada em audio/tempos.json."""
import json
from pathlib import Path

import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Equações do 1º Grau")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-EQU-003_juntar_termos_semelhantes.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("caixas", "exemplo", "atalho", "questao", "fim"))
BR = "#FFFFFF"

assert 3 * 10 + 2 == 32 and 5 * 10 == 50
assert 5 - 2 == 3 and 6 + 1 == 7 and 5 * 10 + 6 - 2 * 10 + 1 == 37 == 3 * 10 + 7 and 7 * 10 + 7 == 77
assert 1 - 4 == -3 and -2 - 3 == -5
assert 6 - 1 == 5 and 7 - 2 == 5 and 60 + 7 - 10 - 2 == 55 == 5 * 10 + 5

_T = {s["id"]: s for s in json.load(open(Path(__file__).resolve().parents[1] / "audio" / "tempos.json", encoding="utf8"))["scenes"]}


def pal(sid, palavra, n=0):
    """instante em que a voz diz a palavra (n = qual ocorrência na cena)"""
    s = _T[sid]
    achou = [tk["t0"] for tk in s["tokens"] if tk["disp"].lower().strip(",.:;?!") == palavra]
    return s["start"] + achou[n]


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças desta aula ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def form(c, t, t0, s, x, y, size, cor=None, align="left"):
    E.formula_em(c, t, t0, s, x, y, size, "g", cor, align)


def fase(c, t, t0, t1, fn):
    if t0 - 0.01 <= t < t1 + 0.4:
        E.saida(c, t, t1, fn)


def fw(s, size):
    return E.formula(None, s, 0, 0, size, a=0) if s else 0.0


def trecho_x(s, trecho, x, size, align="left", n=0):
    """(x inicial, largura) de um trecho da fórmula s"""
    xi = x - fw(s, size) / 2 if align == "center" else x
    i0 = -1
    for _ in range(n + 1):
        i0 = s.find(trecho, i0 + 1)
    return xi + fw(s[:i0], size), fw(trecho, size) - size * 0.02


def realce(c, t, t0, s, trecho, x, y, size, cor=None, align="left", n=0, t1=None):
    a = ep(t, t0, 0.35) * (1 - ep(t, t1, 0.3) if t1 else 1)
    if a <= 0:
        return
    x0, w = trecho_x(s, trecho, x, size, align, n)
    pad = min(size * 0.14, 16)
    M.rrect(c, x0 - pad, y - size * 0.95, w + pad * 2, size * 1.25, size * 0.2, cor or COR, 0.16 * a)


def monta(c, t, pecas, x, y, size, align="left", cor=None):
    total = fw("".join(p[0] for p in pecas), size)
    x0 = x - total / 2 if align == "center" else x
    acc = ""
    for p in pecas:
        s, t0, cp = p[0], p[1], (p[2] if len(p) > 2 else cor)
        xo = x0 + fw(acc, size)
        E.foco(c, t, t0, 0.4, lambda a, s=s, xo=xo, cp=cp: E.formula(c, s, xo, y, size, cor=cp, a=a))
        acc += s
    return x0


def num_bola(c, s, cx, cy, r, size, a=1.0, cor=None, tinta=None):
    E.bola(c, cx, cy + 3, r, cor, a)
    centro(c, s, cx, cy + size * 0.36, size, "g", tinta or E.SOBRE, a)


def bola_em(c, t, t0, s, cx, cy, r, size, cor=None):
    E.foco(c, t, t0, 0.5, lambda p: num_bola(c, s, cx, cy, r * ease_back(prog(t, t0, 0.6)), size, p, cor, BR))


def caixa(c, cx, cy, a=1.0, k=1.0, rotulo=None):
    """caixa de ovos fechada (a tampa de gomos), na cor da matéria; rotulo escreve em cima dela"""
    if a <= 0:
        return
    w, h = 150 * k, 96 * k
    c.save(); c.translate(3, 6)
    M.rrect(c, cx - w / 2, cy - h / 2, w, h, 16 * k, "#000000", 0.18 * a)
    c.restore()
    M.rrect(c, cx - w / 2, cy - h / 2, w, h, 16 * k, E.COR, a)
    for i in range(3):  # os gomos da tampa
        gx = cx - w / 3 + i * w / 3
        c.drawOval(skia.Rect.MakeXYWH(gx - w * 0.14, cy - h * 0.34, w * 0.28, h * 0.42), M.paint(M.mix(E.COR, BR, 0.28), a))
    M.line(c, cx - w / 2 + 10 * k, cy + h * 0.22, cx + w / 2 - 10 * k, cy + h * 0.22, M.mix(E.COR, BR, 0.4), a, 4 * k)
    if rotulo:
        centro(c, rotulo, cx, cy + h * 0.15, 46 * k, "g", BR, a)


def ovo(c, cx, cy, a=1.0, k=1.0, quebrado=False):
    """ovo solto; quebrado ganha uma rachadura"""
    if a <= 0:
        return
    r = skia.Rect.MakeXYWH(cx - 30 * k, cy - 40 * k, 60 * k, 80 * k)
    c.drawOval(r, M.paint("#F6E7C8", a))
    c.drawOval(r, M.paint(TINTA2, a, stroke=3))
    if quebrado:
        pts = [(-26, -4), (-12, 8), (0, -6), (12, 8), (26, -4)]
        for (x0, y0), (x1, y1) in zip(pts, pts[1:]):
            M.line(c, cx + x0 * k, cy + y0 * k, cx + x1 * k, cy + y1 * k, ERRADO, a, 4)


def oval(c, t, t0, x, y, w, h, cor, d=0.5):
    """contorno oval que se fecha em volta de um termo"""
    p = ep(t, t0, d)
    if p <= 0:
        return
    pt = M.paint(cor, 1.0, stroke=6)
    path = skia.Path()
    path.addArc(skia.Rect.MakeXYWH(x, y, w, h), -90, 360 * p)
    c.drawPath(path, pt)


def sublinha(c, t, t0, x0, x1, y, cor, d=0.45):
    p = ep(t, t0, d)
    if p > 0:
        M.line(c, x0, y, lerp(x0, x1, p), y, cor, 1.0, 9)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    a_, b_, c_ = C["s01.a"], C["s01.b"], C["s01.c"]

    def conta():
        form(c, t, a_, "3x + 2", 330, 480, 200)
        form(c, t, b_, "= 5x", 330 + fw("3x + 2 ", 200), 480, 200, ERRADO)
        if t >= c_:
            E.risco(c, 1050, 520, 1500, 330, t, c_, largura=16)
        E.foco(c, t, c_, 0.45, lambda p: E.selo(c, 1660, 400, 80, False, p))
        E.frase(c, t, pal("s01", "e"), ps("um número só basta para", "i", 84) + ps("provar", "g", 80, COR), W / 2, 820, "center", 0.12)
    E.saida(c, t, C["s02"] - 0.1, conta)
    if t < C["s02"]:
        return
    a2, b2 = C["s02.a"], C["s02.b"]
    E.frase(c, t, a2, ps("até o fim desta aula, você", "i", 84), XE, 280, passo=0.12)
    E.frase(c, t, pal("s02", "encurta"), ps("encurta expressões", "g", 110, COR), XE, 450, passo=0.15)
    E.frase(c, t, pal("s02", "juntando"), ps("juntando o que é", "i", 104) + ps("parecido", "g", 96, COR), XE, 600, passo=0.12)
    E.foco(c, t, b2 - 0.2, 0.7, lambda p: E.bola(c, 1600, 840, 190 * ease_back(prog(t, b2 - 0.2, 0.7))), blur=0)
    E.foco(c, t, b2 + 0.2, 0.5, lambda p: (centro(c, "+ atalho", 1600, 830, 64, "g", BR, p), centro(c, "de prova", 1600, 900, 64, "i", BR, p)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    a_, b_, c_ = C["s03.a"], C["s03.b"], C["s03.c"]
    E.frase(c, t, C["s03"] + 0.4, ps("lembre de", "i", 92), XE, 400)
    E.foco(c, t, a_, 0.5, lambda p: E.escreve(c, "2", XE - 8, 720, 340, "g", COR, p))
    E.foco(c, t, a_ + 0.15, 0.5, lambda p: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, p))
    x, w = 880, 900
    p1 = ep(t, b_, 0.5)
    E.caixa_pontilhada(c, x, 170, w, 340, p1, prog_=p1)
    E.frase(c, t, b_ + 0.1, ps("número colado na letra é", "i", 64) + ps("vezes", "g", 60, COR), x + 44, 260, passo=0.1)
    form(c, t, pal("s03", "três"), "3x = 3 × x", x + 44, 380, 80)
    form(c, t, pal("s03", "xis", 2), "x = 1x", x + 44, 480, 80)
    p2 = ep(t, c_, 0.5)
    E.caixa_pontilhada(c, x, 560, w, 270, p2, prog_=p2)
    E.frase(c, t, c_ + 0.1, ps("somar e subtrair", "g", 64, COR) + ps("com sinal", "i", 70), x + 44, 660, passo=0.1)
    E.frase(c, t, pal("s03", "pensando"), ps("pensando em dívida e pagamento", "i", 64), x + 44, 760, passo=0.1)
    E.frase(c, t, pal("s03", "procure"), ps("faltou alguma? procure no canal", "i", 58, TINTA2), x + 44, 930, passo=0.1)


# ---------------- caixas de ovos ----------------
X0, DX = 400, 170


def b_caixas(c, t, C, b):
    a4, b4, c4, d4 = (C[f"s04.{k}"] for k in "abcd")
    a5, b5, c5, d5 = (C[f"s05.{k}"] for k in "abcd")
    a6, b6, c6, d6 = (C[f"s06.{k}"] for k in "abcd")

    # uma caixa sozinha: a quantidade que não se sabe
    def uma():
        E.foco(c, t, a4, 0.5, lambda p: caixa(c, W / 2, 470, p, 2.2))
        E.frase(c, t, pal("s04", "todas"), ps("todas com a", "i", 76) + ps("mesma quantidade", "g", 70, COR), W / 2, 760, "center", 0.12)
        E.frase(c, t, pal("s04", "você"), ps("quantos ovos? não se sabe", "i", 70, TINTA2), W / 2, 870, "center", 0.11)
        E.foco(c, t, b4, 0.5, lambda p: (num_bola(c, "x", W / 2 + 220, 330, 70, 90, p)))
    fase(c, t, C["s04"], c4 - 0.1, uma)
    if t < c4:
        return
    junta = ease_io(prog(t, a5 - 0.2, 0.9))
    for i in range(3):
        E.foco(c, t, c4 + i * 0.12, 0.4, lambda p, i=i: caixa(c, X0 + i * DX, lerp(250, 330, junta), p))
    for j in range(5):
        E.foco(c, t, d4 + j * 0.1, 0.4, lambda p, j=j: caixa(c, lerp(X0 + j * DX, X0 + (3 + j) * DX, junta), lerp(430, 330, junta), p))
    E.saida(c, t, a5 - 0.2, lambda: (form(c, t, c4 + 0.3, "3x", XE, 275, 80, COR), form(c, t, d4 + 0.3, "5x", XE, 455, 80, COR)))
    form(c, t, a5 + 0.6, "8x", XE, 355, 80, COR)
    # ovos quebrados, soltos ao lado das caixas
    for i in range(2):
        E.foco(c, t, a6 + i * 0.2, 0.45, lambda p, i=i: ovo(c, X0 + 6 * DX + i * 90, 470, p, 1.0, True))

    def conta5():
        L = "3x + 5x = 8x"
        realce(c, t, c5, L, "3", XE, 620, 130)
        realce(c, t, c5, L, "5", XE, 620, 130)
        realce(c, t, c5, L, "8", XE, 620, 130)
        form(c, t, b5, L, XE, 620, 130)
        E.frase(c, t, c5, ps("soma o número que multiplica a letra", "i", 72), XE, 780, passo=0.1)
        E.frase(c, t, d5, ps("a letra", "i", 80) + ps("fica igual", "g", 74, COR), XE, 890, passo=0.12)
        E.frase(c, t, pal("s05", "caixa"), ps("caixa + caixa = caixa", "i", 64, TINTA2), XE + 800, 890, passo=0.1)
    fase(c, t, b5, a6 - 0.1, conta5)

    def conta6():
        form(c, t, b6, "3x + 5x − 2", XE, 680, 120)
        L = "= 8x − 2"
        x0, w = trecho_x(L, "− 2", XE, 120)
        q = ep(t, d6, 0.45)
        E.caixa_pontilhada(c, x0 - 20, 760, w + 40, 150, q, ERRADO, prog_=q)
        form(c, t, c6, L, XE, 870, 120, COR)
        E.frase(c, t, d6, ps("não entra na conta das caixas", "i", 66), 900, 840, passo=0.1)
        E.frase(c, t, pal("s06", "são"), ps("são", "i", 70) + ps("ovos soltos", "g", 66, ERRADO), 900, 930, passo=0.12)
    fase(c, t, a6, 1e9, conta6)


# ---------------- regra ----------------
def b_regra(c, t, C, b):
    a_, b_, c_, d_ = (C[f"s07.{k}"] for k in "abcd")
    L, y, s = "3x + 5x − 2", 330, 160
    realce(c, t, b_, L, "3x", W / 2, y, s, align="center")
    realce(c, t, b_, L, "+ 5x", W / 2, y, s, align="center")
    realce(c, t, c_, L, "− 2", W / 2, y, s, TINTA2, "center")
    form(c, t, C["s07"] + 0.3, L, W / 2, y, s, None, "center")
    for i, tr in enumerate(("3x", "+ 5x", "− 2")):
        x0, w = trecho_x(L, tr, W / 2, s, "center")
        E.chave(c, x0, x0 + w, y + 50, COR, ep(t, a_ + i * 0.15, 0.5), 22, 5)
        E.foco(c, t, a_ + i * 0.15 + 0.2, 0.4, lambda p, x0=x0, w=w: centro(c, "termo", x0 + w / 2, y + 130, 50, "i", COR, p))
    E.frase(c, t, b_, ps("mesma letra:", "i", 80) + ps("semelhantes", "g", 76, COR) + ps("— só eles se juntam", "i", 80), W / 2, 620, "center", 0.12)
    E.frase(c, t, c_, ps("número sem letra só com", "i", 80) + ps("número sem letra", "g", 74, TINTA2), W / 2, 760, "center", 0.12)
    E.foco(c, t, d_, 0.5, lambda p: E.pilula(c, "com x²: mesmo expoente também (outra aula)", W / 2, 920, 52, estilo="b", fundo=TINTA, a=p))


# ---------------- prova: 3x + 2 não é 5x ----------------
def b_prova(c, t, C, b):
    a_, b_, c_, d_, e_, f_ = (C[f"s08.{k}"] for k in "abcdef")
    form(c, t, C["s08"] + 0.3, "3x + 2", XE, 220, 110, COR)
    dez = ep(t, c_, 0.4)
    for i in range(3):
        E.foco(c, t, a_ + i * 0.12, 0.4, lambda p, i=i: caixa(c, 640 + i * DX, 190, p, 1.0, "10" if dez > 0.5 else None))
    for i in range(2):
        E.foco(c, t, pal("s08", "dois", 1) + i * 0.15, 0.4, lambda p, i=i: ovo(c, 1150 + i * 80, 190, p, 0.9))
    E.foco(c, t, c_, 0.45, lambda p: E.escreve(c, "x = 10", 1400, 215, 80, "g", COR, p))
    form(c, t, b_, "5x", XE, 560, 110, ERRADO)
    form(c, t, d_ - 0.6, "3x + 2 = 3 × 10 + 2 =", XE, 400, 100)
    bola_em(c, t, d_, "32", XE + fw("3x + 2 = 3 × 10 + 2 = ", 100) + 80, 365, 80, 80, CERTO)
    E.saida(c, t, e_ - 0.5, lambda: E.frase(c, t, b_ + 0.2, ps("não dá 5 caixas", "i", 70, ERRADO), XE + 200, 550, passo=0.1))
    form(c, t, e_ - 0.4, "= 5 × 10 = 50", XE + fw("5x ", 110), 560, 110, ERRADO)
    E.foco(c, t, e_ + 0.4, 0.45, lambda p: E.selo(c, 1300, 520, 56, False, p))
    E.frase(c, t, f_, ps("3x + 2", "g", 100, CERTO) + ps("já é a resposta final", "i", 90), XE, 780, passo=0.13)
    E.frase(c, t, pal("s08", "não", 1), ps("não há o que juntar", "i", 80, TINTA2), XE, 900, passo=0.12)


# ---------------- exemplos ----------------
def b_exemplo(c, t, C, b):
    a9, b9, c9, d9, e9, f9 = (C[f"s09.{k}"] for k in "abcdef")
    L, y, s = "5x + 6 − 2x + 1", 300, 140

    def s09():
        E.frase(c, t, pal("s09", "veja"), ps("uma mais bagunçada", "i", 70, TINTA2), W / 2, 140, "center", 0.1)
        realce(c, t, b9, L, "5x", W / 2, y, s, align="center")
        realce(c, t, b9 + 0.5, L, "− 2x", W / 2, y, s, align="center")
        realce(c, t, d9, L, "+ 6", W / 2, y, s, TINTA2, "center")
        realce(c, t, d9 + 0.4, L, "+ 1", W / 2, y, s, TINTA2, "center")
        monta(c, t, [("5x", a9), (" + 6", pal("s09", "mais", 1)), (" − 2x", pal("s09", "menos")), (" + 1", pal("s09", "mais", 2))], W / 2, y, s, "center")
        E.frase(c, t, b9, ps("com x:", "g", 66, COR), XE, 520)
        form(c, t, c9, "5x − 2x = 3x", XE, 620, 110, COR)
        E.frase(c, t, d9, ps("números soltos:", "g", 66, TINTA2), 1060, 520)
        form(c, t, e9, "6 + 1 = 7", 1060, 620, 110)
        E.frase(c, t, f9 - 0.6, ps("resultado:", "i", 84), XE, 860, passo=0.1)
        form(c, t, f9, "3x + 7", XE + 400, 870, 150, CERTO)
    fase(c, t, C["s09"], C["s10"] - 0.1, s09)

    a0, b0, c0, d0, e0 = (C[f"s10.{k}"] for k in "abcde")

    def s10():
        E.frase(c, t, C["s10"] + 0.3, ps("pode dar", "i", 84) + ps("negativo", "g", 78, COR), XE, 180, passo=0.12)
        form(c, t, a0, "x − 4x", XE, 380, 130)
        E.foco(c, t, b0, 0.4, lambda p: E.escreve(c, "tem 1x, tira 4x", XE, 480, 64, "i", TINTA2, p))
        form(c, t, c0, "= −3x", XE + fw("x − 4x ", 130), 380, 130, COR)
        form(c, t, d0, "−2x − 3x", XE, 680, 130)
        E.foco(c, t, pal("s10", "é"), 0.4, lambda p: E.divida(c, 1300, 640, 230, 150, "2x", p))
        E.foco(c, t, pal("s10", "outra"), 0.4, lambda p: E.divida(c, 1580, 640, 230, 150, "3x", p))
        form(c, t, e0, "= −5x", XE + fw("−2x − 3x ", 130), 680, 130, COR)
        E.frase(c, t, pal("s10", "como"), ps("como na dívida", "i", 66, TINTA2), XE, 920, passo=0.1)
    fase(c, t, C["s10"], 1e9, s10)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    a_, b_, c_, d_, e_ = (C[f"s11.{k}"] for k in "abcde")
    L, y, s = "5x + 6 − 2x + 1", 380, 130
    E.frase(c, t, C["s11"] + 0.3, ps("cuidado", "g", 90, ERRADO) + ps("com o sinal da frente", "i", 90), XE, 180, passo=0.13)
    realce(c, t, b_, L, "5x", XE, y, s, ERRADO, t1=e_)
    realce(c, t, b_ + 0.3, L, "2x", XE, y, s, ERRADO, t1=e_)
    form(c, t, pal("s11", "em"), L, XE, y, s)
    x0, w = trecho_x(L, "− 2x", XE, s)
    q = ep(t, e_, 0.45)
    E.caixa_pontilhada(c, x0 - 18, y - 135, w + 36, 175, q, CERTO, prog_=q)
    E.foco(c, t, pal("s11", "escreve"), 0.45, lambda p: (E.escreve(c, "→", XE + fw(L, s) + 40, y - 10, 90, "g", ERRADO, p),
                                                       E.formula(c, "7x + 7", XE + fw(L, s) + 150, y, s, cor=ERRADO, a=p)))
    E.frase(c, t, pal("s11", "teste"), ps("teste com 10:", "i", 72, TINTA2), XE, 590, passo=0.1)
    E.frase(c, t, c_ - 0.8, ps("a original dá", "i", 80), XE, 720, passo=0.1)
    form(c, t, c_, "37", XE + 470, 725, 110, CERTO)
    E.frase(c, t, d_ - 0.8, ps("7x + 7 daria", "i", 80, ERRADO), 900, 720, passo=0.1)
    form(c, t, d_, "77", 1350, 725, 110, ERRADO)
    E.frase(c, t, e_, ps("o", "i", 80) + ps("menos", "g", 74, CERTO) + ps("estava ali: esses 2x", "i", 80) + ps("saem", "g", 74, CERTO), W / 2, 920, "center", 0.12)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    a2, b2, c2, d2, e2, f2 = (C[f"s12.{k}"] for k in "abcdef")
    AM = "#FFD500"

    def regras():
        E.frase(c, t, C["s12"] + 0.3, ps("agora, o atalho", "i", 80, CLARO), W / 2, 170, "center")
        E.frase(c, t, a2, ps("marque cada termo com o", "i", 88, BR) + ps("sinal da frente", "g", 84, BR), W / 2, 300, "center", 0.12)
        oval(c, t, b2, 280, 400, 150, 90, CLARO)
        E.frase(c, t, b2 + 0.2, ps("circule os termos com x", "b", 70, BR), 480, 470, passo=0.1)
        sublinha(c, t, c2, 285, 425, 590, AM)
        E.frase(c, t, c2 + 0.2, ps("sublinhe os números soltos", "b", 70, BR), 480, 590, passo=0.1)
        E.foco(c, t, d2, 0.45, lambda p: centro(c, "±", 355, 715, 90, "g", CLARO, p))
        E.frase(c, t, d2 + 0.2, ps("leve junto o sinal de cada um", "b", 70, BR), 480, 710, passo=0.1)
        E.frase(c, t, pal("s12", "depois"), ps("depois, junte o que tem", "i", 80, CLARO) + ps("a mesma marca", "g", 76, BR), W / 2, 880, "center", 0.12)
    fase(c, t, C["s12"], e2 - 0.15, regras)

    def exemplo():
        L, y, s = "5x + 6 − 2x + 1", 520, 150
        form(c, t, e2 - 0.1, L, W / 2, y, s, BR, "center")
        for tr, k in (("5x", 0), ("− 2x", 1)):
            x0, w = trecho_x(L, tr, W / 2, s, "center")
            oval(c, t, e2 + 0.5 + k * 0.8, x0 - 30, y - 150, w + 60, 190, CLARO)
        for tr, k in (("+ 6", 0), ("+ 1", 1)):
            x0, w = trecho_x(L, tr, W / 2, s, "center")
            sublinha(c, t, f2 + 0.3 + k * 0.5, x0 - 6, x0 + w + 6, y + 40, AM)
        E.foco(c, t, e2 + 0.6, 0.45, lambda p: E.formula(c, "circulados: 5x e −2x", 330, 800, 72, "b", CLARO, p))
        E.foco(c, t, f2 + 0.3, 0.45, lambda p: E.formula(c, "sublinhados: +6 e +1", 330, 910, 72, "b", AM, p))
    fase(c, t, e2 - 0.15, C["s13"] - 0.1, exemplo)

    a3, b3, c3 = C["s13.a"], C["s13.b"], C["s13.c"]

    def porque():
        E.frase(c, t, C["s13"] + 0.2, ps("funciona porque", "i", 84, CLARO), W / 2, 200, "center")
        E.frase(c, t, a3, ps("a ordem dos termos", "i", 84, CLARO) + ps("não muda o resultado", "g", 78, BR), W / 2, 330, "center", 0.12)
        form(c, t, a3 + 1.0, "5x − 2x + 6 + 1", W / 2, 490, 110, BR, "center")
        E.frase(c, t, b3, ps("desde que cada termo leve", "i", 80, CLARO) + ps("o próprio sinal", "g", 74, BR), W / 2, 640, "center", 0.12)
        E.frase(c, t, pal("s13", "é"), ps("como separar entradas e saídas de dinheiro", "i", 64, CLARO), W / 2, 750, "center", 0.08)
        E.foco(c, t, c3, 0.5, lambda p: E.pilula(c, "poucos termos? junte de olho", W / 2, 910, 60, estilo="b", fundo=E.COR, cor=BR, a=p))
    fase(c, t, C["s13"], 1e9, porque)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s14"] + 0.3, ps("hora de testar", "i", 72, COR), XE, 200)
    E.frase(c, t, pal("s14", "simplifique"), ps("simplifique", "i", 110), XE, 420)
    monta(c, t, [("6x", C["s14.a"]), (" + 7", pal("s14", "mais")), (" − x", pal("s14", "menos")), (" − 2", pal("s14", "menos", 1))], XE, 680, 150)
    E.relogio(c, t, C["s15.a"], 1490, 440, 200)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    a6, b6, c6, d6 = (C[f"s16.{k}"] for k in "abcd")
    L, y, s = "6x + 7 − x − 2", 230, 120
    realce(c, t, a6, L, "6x", XE, y, s)
    realce(c, t, a6 + 0.6, L, "− x", XE, y, s)
    realce(c, t, c6, L, "+ 7", XE, y, s, TINTA2)
    realce(c, t, c6 + 0.3, L, "− 2", XE, y, s, TINTA2)
    form(c, t, C["s16"] + 0.2, L, XE, y, s)

    def s16():
        E.frase(c, t, a6 - 0.3, ps("com x:", "g", 66, COR), XE, 420)
        form(c, t, a6, "6x − x", XE + 250, 425, 100)
        E.foco(c, t, pal("s16", "lembre"), 0.45, lambda p: E.formula(c, "x = 1x", 1250, 425, 80, cor=TINTA2, a=p))
        form(c, t, b6, "6 − 1 = 5  →  5x", XE + 250, 560, 100, COR)
        E.frase(c, t, c6 - 0.6, ps("soltos:", "g", 66, TINTA2), XE, 720)
        form(c, t, c6, "7 − 2 = 5", XE + 250, 725, 100)
        form(c, t, d6, "5x + 5", W / 2 + 200, 920, 150, CERTO, "center")
    fase(c, t, C["s16"], C["s17"] - 0.1, s16)

    a7, b7, c7 = C["s17.a"], C["s17.b"], C["s17.c"]

    def s17():
        form(c, t, C["s17"], "5x + 5", W - 170, y, 120, CERTO, "right")
        E.frase(c, t, C["s17"] + 0.3, ps("confira com 10:", "i", 72, TINTA2), XE, 420)
        form(c, t, a7, "60 + 7 − 10 − 2 = 55", XE, 570, 110)
        form(c, t, b7, "5 × 10 + 5 = 55", XE, 740, 110)
        E.foco(c, t, c7, 0.45, lambda p: E.selo(c, 820, 900, 64, True, p))
        E.frase(c, t, c7, ps("bateu", "g", 120, CERTO), 920, 940)
    fase(c, t, C["s17"], 1e9, s17)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    a1, b1 = C["s18.a"], C["s18.b"]

    def resumo():
        E.frase(c, t, C["s18"] + 0.3, ps("resumindo", "i", 96, COR), W / 2, 220, "center")
        E.foco(c, t, a1, 0.5, lambda p: num_bola(c, "1", 230, 430, 58, 66, p))
        E.frase(c, t, a1 + 0.1, ps("só se junta o que é", "i", 84) + ps("semelhante", "g", 76, COR), 320, 460, passo=0.12)
        E.foco(c, t, b1, 0.5, lambda p: num_bola(c, "2", 230, 650, 58, 66, p))
        E.frase(c, t, b1 + 0.1, ps("cada termo com", "i", 84) + ps("o seu sinal", "g", 76, COR), 320, 680, passo=0.12)
        form(c, t, b1 + 0.6, "3x + 5x − 2 = 8x − 2", 320, 860, 100, COR)
    E.saida(c, t, C["s19"] - 0.1, resumo)
    if t < C["s19"]:
        return
    a_, b_, c_, d_, e_ = (C[f"s19.{k}"] for k in "abcde")
    E.frase(c, t, C["s19"] + 0.2, ps("próxima aula", "i", 84), XE, 230)
    E.frase(c, t, a_, ps("abrir parênteses", "g", 110, COR), XE, 380)
    E.frase(c, t, a_ + 0.4, ps("com um número na frente", "i", 84), XE, 500, passo=0.12)
    monta(c, t, [("−2", b_), ("(", pal("s19", "abre", 1), COR), ("x − 5", pal("s19", "xis")), (")", pal("s19", "fecha"), COR)], XE, 680, 130)
    E.frase(c, t, c_, ps("sem errar", "i", 84) + ps("o sinal", "g", 78, COR), XE, 840, passo=0.12)
    E.foco(c, t, d_, 0.5, lambda p: E.pilula(c, "Inscreva-se", 1500, 330, 76, estilo="g", fundo=E.COR, cor=E.SOBRE, a=p))
    p = ease_io(prog(t, d_ + 0.3, 0.8))
    E.cursor(c, lerp(1780, 1640, p), lerp(620, 375, p), ep(t, d_ + 0.2, 0.4), TINTA)
    E.frase(c, t, e_, ps("bons", "i", 120) + ps("estudos!", "i", 120, COR), 1450, 760, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, caixas=b_caixas, regra=b_regra, prova=b_prova, exemplo=b_exemplo,
              erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
