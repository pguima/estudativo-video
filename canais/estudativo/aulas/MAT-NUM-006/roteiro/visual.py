"""Visual — Estudativo · MAT-NUM-006: tabuada com macetes: 3, 4, 6, 7 e 8.
Identidade em _ferramentas/editorial.py. Peças locais: `sala` (cadeiras em grade, com cor por fileira) e `corrente` (o número salta
em arco e cresce a cada dobrada: é a alma desta aula)."""
import math

import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco
import motor as M
import skia

E.usar("Matemática", "Números e Contas")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-NUM-006_tabuada_macetes_3_4_6_7_8.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("ideia", "tres", "sete", "mapa", "atalho", "questao", "fim"))
BR = "#FFFFFF"


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


def entre(a, b, f):
    """instante proporcional entre dois cues: sobrevive à troca do tempo provisório pela voz real"""
    return a + (b - a) * f


# ---------------- peças locais ----------------
def cadeira(c, cx, cy, s, cor, a=1.0):
    """cadeira vista de frente: encosto, assento e dois pés"""
    if a <= 0:
        return
    M.rrect(c, cx - s * 0.3, cy - s * 0.5, s * 0.6, s * 0.5, s * 0.08, cor, a)
    M.rrect(c, cx - s * 0.38, cy + s * 0.02, s * 0.76, s * 0.17, s * 0.06, cor, a)
    M.line(c, cx - s * 0.28, cy + s * 0.15, cx - s * 0.3, cy + s * 0.5, cor, a, max(3, s * 0.08))
    M.line(c, cx + s * 0.28, cy + s * 0.15, cx + s * 0.3, cy + s * 0.5, cor, a, max(3, s * 0.08))


def sala(c, t, cx, cy, fil, col, passo_, s, ta, cores=None, dx=0.0):
    """cadeiras em grade, entrando fileira a fileira. cores = {fileira: cor}"""
    for i in range(fil):
        for j in range(col):
            x, y = (j - (col - 1) / 2) * passo_, (i - (fil - 1) / 2) * passo_
            k = ease_back(prog(t, ta + i * 0.14 + j * 0.03, 0.4))
            if k > 0.01:
                cadeira(c, cx + x + dx, cy + y, s * k, (cores or {}).get(i, TINTA), M.clamp(k * 2))


def corrente(c, t, vals, ts, x0, y, dx, r0=90, cor_fim=None, escuro=False, rot="dobro", voo=110):
    """a corrente de dobros: cada número sai do anterior num salto em arco e pousa maior. ts = instante de cada número; voo = altura do salto"""
    n = len(vals)
    raio = lambda i: r0 * (1 + 0.16 * i)
    for i in range(1, n):
        ti = ts[i]
        if t < ti - 0.25:
            continue
        xp, xq = x0 + (i - 1) * dx, x0 + i * dx
        ra, rb = raio(i - 1), raio(i)
        E.salto(c, t, ti - 0.25, xp + ra * 0.3, xq - rb * 0.3, y - max(ra, rb) * 0.86, 70, cor=CLARO if escuro else E.COR, d=0.55, largura=6)
        E.foco(c, t, ti, 0.35, lambda a, xp=xp, xq=xq, ra=ra, rb=rb: E.centro(c, rot, (xp + xq) / 2, y - max(ra, rb) * 0.86 - 94, 50, "i", CLARO if escuro else COR, a), sobe=6)
    for i in range(n):
        ti = ts[i]
        q = ease_io(prog(t, ti - 0.25, 0.55))
        if q <= 0:
            continue
        x = x0 + i * dx
        if i:
            xa = lerp(x - dx, x, q)
            ya = y - math.sin(q * math.pi) * voo
        else:
            xa, ya = x, y
        k = ease_back(prog(t, ti - 0.25, 0.55))
        r = raio(i) * (lerp(0.45, 1.0, k) if i else k)
        # o anterior dá um pulso quando solta o número novo
        if i + 1 < n and t >= ts[i + 1] - 0.25:
            r *= 1 + 0.1 * max(0.0, math.sin(prog(t, ts[i + 1] - 0.25, 0.4) * math.pi))
        cor = cor_fim if (cor_fim and i == n - 1) else None
        E.bola(c, xa, ya, r, cor)
        s = str(vals[i])
        size = r * (1.08 if len(s) == 1 else 0.98)
        E.centro(c, s, xa, ya + size * 0.36, size, "g", E.SOBRE)


def bola_num(c, t, t0, s, cx, cy, r, size=None, cor=None):
    k = ease_back(prog(t, t0, 0.5))
    if k <= 0.01:
        return
    E.bola(c, cx, cy, r * k, cor, M.clamp(k * 2))
    size = size or r * (1.0 if len(s) <= 2 else 0.8)
    E.foco(c, t, t0 + 0.12, 0.35, lambda a: E.centro(c, s, cx, cy + size * 0.36, size, "g", E.SOBRE, a))


def conta(c, t, s, x, y, t0, cor=TINTA, size=96, align="center"):
    w = E.larg(s, "g", size)
    xx = x - w / 2 if align == "center" else x
    E.foco(c, t, t0, 0.45, lambda a: E.escreve(c, s, xx, y, size, "g", cor, a))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def trava():
        E.foco(c, t, C["s01.a"], 0.5, lambda a: E.centro(c, "7 × 8", W / 2, 500, 340, "g", TINTA, a))
        E.frase(c, t, C["s01.b"], [("na", "i", 96), ("hora", "i", 96), ("do", "i", 96), ("aperto:", "i", 96), ("chuta", "g", 92, ERRADO)], W / 2, 720, "center", passo=0.1)
        E.frase(c, t, C["s01.c"], [("hoje,", "i", 84), ("sai", "i", 84), ("dobrando", "g", 80, COR), ("o", "i", 84), ("que", "i", 84), ("você", "i", 84), ("já", "i", 84), ("sabe", "i", 84)], W / 2, 860, "center", passo=0.1)
    E.saida(c, t, C["s02"] - 0.1, trava)
    if t < C["s02"]:
        return
    a_, b_, c_ = C["s02.a"], C["s02.b"], C["s02.c"]

    def quinze():
        E.frase(c, t, C["s02"] + 0.2, [("tirando", "i", 84), ("as", "i", 84), ("tabuadas", "i", 84), ("do", "i", 84), ("1,", "g", 80), ("2,", "g", 80), ("5,", "g", 80), ("9", "g", 80), ("e", "i", 84), ("10", "g", 80)], W / 2, 230, "center", passo=0.14)
        E.frase(c, t, a_, [("sobram", "i", 116), ("só", "i", 116), ("15", "g", 130, COR), ("contas", "g", 116, COR)], W / 2, 400, "center", passo=0.12)
        for i in range(15):
            k = ease_back(prog(t, a_ + 0.5 + i * 0.06, 0.35))
            if k > 0.01:
                E.bola(c, 480 + (i % 5) * 240, 550 + (i // 5) * 130, 48 * k, a=M.clamp(k * 2))
    E.saida(c, t, b_ - 0.1, quinze)
    if t >= b_:
        E.foco(c, t, c_ - 0.2, 0.7, lambda a: E.bola(c, 1450, 520, 300 * ease_back(prog(t, c_ - 0.2, 0.7))), blur=0)
        E.frase(c, t, b_, [("até", "i", 92), ("o", "i", 92), ("fim", "i", 92), ("desta", "i", 92), ("aula", "i", 92)], XE, 400)
        E.frase(c, t, entre(b_, c_, 0.5), [("você", "i", 92), ("fecha", "g", 120, COR)], XE, 560)
        E.frase(c, t, entre(b_, c_, 0.7), [("todas", "g", 120, COR)], XE, 690)
        E.foco(c, t, c_ + 0.2, 0.5, lambda a: (E.escreve(c, "+ atalho", 1270, 505, 88, "g", E.SOBRE, a),
                                               E.escreve(c, "de prova", 1300, 595, 88, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    a_, b_, c_, fim = C["s03.a"], C["s03.b"], C["s03.c"], C["s03.end"]
    E.frase(c, t, a_, [("você", "i", 96), ("só", "i", 96), ("precisa", "i", 96), ("de", "i", 96), ("duas", "g", 92, COR), ("coisas", "g", 92, COR)], W / 2, 200, "center", passo=0.1)
    E.frase(c, t, b_, [("o", "i", 104), ("dobro,", "g", 100, COR), ("a", "i", 104), ("tabuada", "i", 104), ("do", "i", 104), ("2", "g", 100)], W / 2, 430, "center", passo=0.1)
    E.frase(c, t, c_, [("a", "i", 104), ("ordem", "g", 100, COR), ("não", "g", 100, COR), ("muda", "g", 100, COR), ("o", "i", 104), ("resultado", "i", 104)], W / 2, 640, "center", passo=0.1)
    E.frase(c, t, entre(c_, fim, 0.6), [("se", "i", 66, TINTA2), ("faltar", "i", 66, TINTA2), ("alguma,", "i", 66, TINTA2), ("procure", "i", 66, TINTA2), ("no", "i", 66, TINTA2), ("canal", "i", 66, TINTA2)], W / 2, 880, "center", passo=0.08)


# ---------------- por que dobrar funciona ----------------
def b_ideia(c, t, C, b):
    a_, b2, c_, d_, e_, f_ = C["s04.a"], C["s04.b"], C["s04.c"], C["s04.d"], C["s04.e"], C["s04.f"]
    y, p, s, x1, x2 = 380, 84, 68, 510, 1400
    E.frase(c, t, a_, [("2", "g", 92, COR), ("fileiras", "i", 96), ("com", "i", 96), ("7", "g", 92, COR), ("cadeiras", "i", 96)], W / 2, 150, "center", passo=0.1)
    sala(c, t, x1, y, 2, 7, p, s, a_ + 0.2)
    # a sala igual chega pela direita
    chega = ease_io(prog(t, c_, 0.9))
    if t >= c_:
        sala(c, t, x2, y, 2, 7, p, s, c_ - 0.1, dx=lerp(420, 0, chega))
    # as quatro fileiras se contam
    for i, (x, f) in enumerate(((x1, 0), (x1, 1), (x2, 0), (x2, 1))):
        ti = d_ + i * 0.2
        yy = y + (f - 0.5) * p
        E.foco(c, t, ti, 0.35, lambda q, x=x, yy=yy, i=i: E.centro(c, str(i + 1), x - 3.5 * p - 34, yy + 18, 54, "g", COR, q), sobe=6)
    E.foco(c, t, b2, 0.45, lambda q: E.centro(c, "14", x1, 620, 130, "g", TINTA, q))
    E.foco(c, t, b2 + 0.2, 0.4, lambda q: E.centro(c, "cadeiras", x1, 700, 60, "i", TINTA2, q))
    E.foco(c, t, d_ + 0.8, 0.45, lambda q: E.centro(c, "4 fileiras", x2, 620, 110, "g", COR, q))
    E.foco(c, t, e_, 0.45, lambda q: E.centro(c, "o dobro de cadeiras", x2, 710, 68, "i", TINTA, q))
    E.frase(c, t, f_, [("dobrou", "g", 96, COR), ("as", "i", 104), ("fileiras,", "i", 104), ("dobrou", "g", 96, COR), ("o", "i", 104), ("resultado", "i", 104)], W / 2, 910, "center", passo=0.12)


# ---------------- quatro e oito ----------------
def b_quatro(c, t, C, b):
    a_, b_, c_, d_ = C["s05.a"], C["s05.b"], C["s05.c"], C["s05.d"]
    E.frase(c, t, a_, [("vezes", "i", 104), ("4", "g", 100, COR), ("é", "i", 104), ("dobrar", "g", 100, COR), ("2", "g", 100, COR), ("vezes", "i", 104)], W / 2, 180, "center", passo=0.1)
    conta(c, t, "4 × 7", W / 2, 370, b_, TINTA, 150)
    corrente(c, t, (7, 14, 28), (entre(b_, c_, 0.45), c_, d_), 420, 690, 540, 110, cor_fim=CERTO)


def b_oito(c, t, C, b):
    a_, b_, c_, d_, e_, f_, fim = C["s06.a"], C["s06.b"], C["s06.c"], C["s06.d"], C["s06.e"], C["s06.f"], C["s06.end"]
    E.frase(c, t, a_, [("vezes", "i", 96), ("8", "g", 92, COR), ("é", "i", 96), ("dobrar", "g", 92, COR), ("3", "g", 92, COR), ("vezes", "i", 96)], W / 2, 150, "center", passo=0.1)
    E.frase(c, t, b_, [("8", "g", 72), ("é", "i", 76), ("o", "i", 76), ("dobro", "i", 76), ("de", "i", 76), ("4", "g", 72)], W / 2, 250, "center", passo=0.08)
    conta(c, t, "8 × 6", W / 2, 380, c_, TINTA, 120)
    x0, dx, y = 330, 420, 640
    corrente(c, t, (6, 12, 24, 48), (entre(c_, d_, 0.6), d_, e_, f_), x0, y, dx, 86, cor_fim=CERTO)
    for i, (s, f_i) in enumerate((("uma: vezes 2", 0.2), ("duas: vezes 4", 0.45), ("três: vezes 8", 0.7))):
        E.foco(c, t, entre(f_, fim, f_i), 0.4, lambda q, i=i, s=s: E.centro(c, s, x0 + (i + 1) * dx, 880, 58, "b", COR, q))
    E.frase(c, t, entre(f_, fim, 0.1), [("cada", "i", 72, TINTA2), ("dobrada", "i", 72, TINTA2), ("conta", "i", 72, TINTA2)], W / 2, 990, "center", passo=0.1)


# ---------------- três e seis ----------------
def b_tres(c, t, C, b):
    a_, b_, c_, d_, e_, f_, g_ = C["s07.a"], C["s07.b"], C["s07.c"], C["s07.d"], C["s07.e"], C["s07.f"], C["s07.g"]
    E.frase(c, t, C["s07"] + 0.1, [("o", "i", 84), ("3", "g", 80, COR), ("não", "i", 84), ("vem", "i", 84), ("de", "i", 84), ("dobrar", "i", 84)], W / 2, 150, "center", passo=0.1)
    sala(c, t, 420, 450, 3, 7, 74, 60, a_, {0: E.COR, 1: E.COR, 2: TINTA})
    E.foco(c, t, a_ + 0.8, 0.4, lambda q: E.centro(c, "2 fileiras + 1", 420, 660, 72, "g", COR, q))
    E.frase(c, t, b_, [("o", "i", 72), ("dobro", "g", 66, COR), ("mais", "g", 66, COR), ("uma", "g", 66, COR), ("vez", "g", 66, COR)], XE, 860, passo=0.1)
    x1, x2 = 1030, 1530
    for x, tt, s0, s1, s2, t0, t1, t2 in ((x1, "3 × 7", "dobro de 7: 14", "14 + 7 = 21", "21", c_, d_, e_), (x2, "3 × 8", "dobro de 8: 16", "16 + 8 = 24", "24", f_, entre(f_, g_, 0.45), g_)):
        conta(c, t, tt, x, 380, t0, COR, 120)
        conta(c, t, s0, x, 520, t1, TINTA, 58)
        conta(c, t, s1, x, 630, t2 - 0.1, TINTA, 76)
        bola_num(c, t, t2, s2, x, 800, 100)


def b_seis(c, t, C, b):
    a_, b_, c_, d_, e_, f_ = C["s08.a"], C["s08.b"], C["s08.c"], C["s08.d"], C["s08.e"], C["s08.f"]
    E.frase(c, t, a_, [("o", "i", 92), ("6", "g", 88, COR), ("é", "i", 92), ("o", "i", 92), ("dobro", "g", 88, COR), ("do", "i", 92), ("3", "g", 88, COR)], W / 2, 150, "center", passo=0.1)
    E.frase(c, t, b_, [("faça", "i", 92), ("× 3", "g", 88), ("e", "i", 92), ("dobre", "g", 88, COR)], W / 2, 270, "center", passo=0.1)
    for x0, tt, s0, v0, v1, t0, tm, t2 in ((270, "6 × 7", "3 × 7 = 21", 21, 42, c_, entre(c_, d_, 0.5), d_), (1090, "6 × 6", "3 × 6 = 18", 18, 36, e_, entre(e_, f_, 0.5), f_)):
        conta(c, t, tt, x0 + 200, 430, t0, COR, 110)
        conta(c, t, s0, x0 + 200, 540, tm - 0.2, TINTA, 66)
        corrente(c, t, (v0, v1), (tm, t2), x0, 800, 380, 92, cor_fim=CERTO)


# ---------------- sete ----------------
def b_sete(c, t, C, b):
    def quase():
        a_, b_, c_, d_ = C["s09.a"], C["s09.b"], C["s09.c"], C["s09.d"]
        E.frase(c, t, C["s09"] + 0.1, [("e", "i", 84), ("a", "i", 84), ("tabuada", "i", 84), ("do", "i", 84), ("7?", "g", 84, COR)], W / 2, 150, "center", passo=0.1)
        E.frase(c, t, a_, [("a", "i", 84), ("maior", "g", 80, COR), ("parte", "g", 80, COR), ("você", "i", 84), ("já", "i", 84), ("fez", "i", 84)], W / 2, 270, "center", passo=0.1)
        for n in range(1, 11):
            i = n - 1
            x, y = 180 + (i % 5) * 312, 360 + (i // 5) * 170
            falta = n in (7, 8)
            ti = c_ if n == 7 else d_ if n == 8 else a_ + 0.3 + i * 0.1
            q = ease_back(prog(t, ti, 0.45))
            if q <= 0.01:
                continue
            a = M.clamp(q * 2)
            if falta:
                M.rrect(c, x, y, 290, 130, 18, E.VAZIO, a)
                c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, 290, 130), 18, 18), M.paint(ERRADO, a, stroke=5))
            else:
                M.rrect(c, x, y, 290, 130, 18, E.COR, a)
            E.centro(c, f"7 × {n}", x + 145, y + 92, 72, "g", ERRADO if falta else E.SOBRE, a)
        E.frase(c, t, b_, [("7 × 4", "g", 92, COR), ("=", "g", 92), ("4 × 7", "g", 92, COR)], W / 2, 790, "center", passo=0.14)
        E.frase(c, t, entre(c_, d_, 0.1), [("só", "i", 92), ("faltam", "i", 92), ("duas", "g", 88, ERRADO)], W / 2, 920, "center", passo=0.12)
    E.saida(c, t, C["s10"] - 0.1, quase)

    def sete_sete():
        a_, b_, c_, d_, e_ = C["s10.a"], C["s10.b"], C["s10.c"], C["s10.d"], C["s10.e"]
        sala(c, t, 470, 560, 7, 7, 76, 60, a_ + 0.1, {0: E.COR, 1: E.COR, 2: E.COR, 3: E.COR, 4: E.COR, 5: TINTA, 6: TINTA})
        x = 1300
        conta(c, t, "7 × 7", x, 240, a_, TINTA, 150)
        E.frase(c, t, b_, [("5", "g", 84, COR), ("fileiras", "i", 88), ("+", "g", 84), ("2", "g", 84), ("fileiras", "i", 88)], x, 380, "center", passo=0.1)
        conta(c, t, "5 × 7 = 35", x, 530, c_, COR, 100)
        conta(c, t, "2 × 7 = 14", x, 660, d_, TINTA, 100)
        conta(c, t, "35 + 14 =", 1190, 860, e_ - 0.1, TINTA, 88)
        bola_num(c, t, e_, "49", 1580, 830, 120, cor=CERTO)
    if C["s10"] <= t:
        E.saida(c, t, C["s11"] - 0.1, sete_sete)
    if t < C["s11"]:
        return

    a_, b_, c_, d_, e_, f_, fim = C["s11.a"], C["s11.b"], C["s11.c"], C["s11.d"], C["s11.e"], C["s11.f"], C["s11.end"]
    E.linha(c, t, [("7 × 8", "g", 120, TINTA, a_), ("=", "g", 120, TINTA, b_ - 0.15), ("8 × 7", "g", 120, COR, b_)], W / 2, 190, "center")
    corrente(c, t, (7, 14, 28, 56), (entre(b_, c_, 0.5), c_, d_, e_), 330, 500, 420, 82, cor_fim=CERTO)
    for i, n in enumerate("5678"):
        E.foco(c, t, f_ + i * 0.28, 0.35, lambda q, i=i, n=n: E.centro(c, n, 690 + i * 170, 810, 170, "g", COR if i < 2 else TINTA, q))
    E.frase(c, t, entre(f_, fim, 0.42), [("56", "g", 76, COR), ("é", "i", 80), ("7 × 8", "g", 76)], W / 2, 900, "center", passo=0.1)
    E.frase(c, t, entre(f_, fim, 0.65), [("só", "i", 64, TINTA2), ("coincidência,", "i", 64, TINTA2), ("mas", "i", 64, TINTA2), ("ajuda", "i", 64, TINTA2), ("a", "i", 64, TINTA2), ("lembrar", "i", 64, TINTA2)], W / 2, 990, "center", passo=0.08)


# ---------------- as quinze contas ----------------
LADOS = (3, 4, 6, 7, 8)


def grupo(a, b_):
    if 4 in (a, b_) or 8 in (a, b_):
        return 0
    if 3 in (a, b_):
        return 1
    if 6 in (a, b_):
        return 2
    return 3


def b_mapa(c, t, C, b):
    a_, b_, c_, d_, e_ = C["s12.a"], C["s12.b"], C["s12.c"], C["s12.d"], C["s12.e"]
    tg = (b_, c_, d_, e_)
    fundo = (E.COR, TINTA, CLARO, E.VAZIO)
    texto = (E.SOBRE, BR, TINTA, E.COR)
    E.frase(c, t, a_, [("as", "i", 92), ("15", "g", 92, COR), ("contas", "g", 92, COR)], XE, 220, passo=0.12)
    ctd = 0
    for i, m in enumerate(LADOS):
        for j, n in enumerate(LADOS):
            if j < i:
                continue
            g = grupo(m, n)
            q = ease_back(prog(t, a_ + 0.2 + ctd * 0.07, 0.35))
            ctd += 1
            if q <= 0.01:
                continue
            x, y = 770 + j * 196, 130 + i * 168
            pinta = ep(t, tg[g] + 0.1 + (i + j) * 0.04, 0.4)
            M.rrect(c, x, y, 180, 140, 16, E.mix(E.VAZIO, fundo[g], pinta), M.clamp(q * 2))
            c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, 180, 140), 16, 16), M.paint(E.COR if g == 3 and pinta > 0.5 else FIO, M.clamp(q * 2), stroke=6 if g == 3 and pinta > 0.5 else 3))
            E.centro(c, f"{m} × {n}", x + 90, y + 90, 56, "g", E.mix(TINTA, texto[g], pinta), M.clamp(q * 2))
    y = 370
    E.frase(c, t, b_, [("tem", "i", 68), ("4", "g", 64, COR), ("ou", "i", 68), ("8?", "g", 64, COR), ("dobre", "g", 64, COR)], XE, y, passo=0.1)
    E.frase(c, t, c_, [("tem", "i", 68), ("3?", "g", 64), ("dobro", "g", 64), ("+", "g", 64), ("uma", "g", 64), ("vez", "g", 64)], XE, y + 130, passo=0.1)
    E.frase(c, t, d_, [("tem", "i", 68), ("6?", "g", 64, COR), ("× 3", "g", 64), ("e", "i", 68), ("dobre", "g", 64)], XE, y + 260, passo=0.1)
    E.frase(c, t, e_, [("7 × 7:", "g", 64, COR), ("5", "g", 64), ("+", "g", 64), ("2", "g", 64)], XE, y + 390, passo=0.1)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    a_, b_, c_, d_ = C["s13.a"], C["s13.b"], C["s13.c"], C["s13.d"]
    E.frase(c, t, a_, [("dobrar", "i", 96), ("uma", "g", 92, ERRADO), ("vez", "g", 92, ERRADO), ("a", "g", 92, ERRADO), ("menos", "g", 92, ERRADO)], W / 2, 160, "center", passo=0.1)
    conta(c, t, "8 × 6", 600, 300, a_ + 0.6, TINTA, 110)
    x0, dx, y = 300, 300, 590
    corrente(c, t, (6, 12, 24), (a_ + 0.9, entre(a_, b_, 0.65), b_), x0, y, dx, 78, cor_fim=ERRADO)
    r = 62 * ease_back(prog(t, b_ + 0.4, 0.5))
    E.selo(c, x0 + 2 * dx + 170, y - 80, r, False)
    conta(c, t, "24 = 4 × 6", 600, 860, c_, ERRADO, 100)
    conta(c, t, "5 × 6 = 30", 1440, 460, d_, COR, 100)
    E.frase(c, t, d_ + 0.5, [("8 × 6", "g", 76), ("não", "i", 80), ("pode", "i", 80)], 1440, 600, "center", passo=0.1)
    E.frase(c, t, d_ + 0.9, [("dar", "i", 80), ("menos", "g", 76, ERRADO), ("que", "i", 80), ("isso", "i", 80)], 1440, 700, "center", passo=0.1)


# ---------------- atalho ----------------
def casa_num(c, t, s, x, y, ti, size=300, cor=BR):
    E.foco(c, t, ti, 0.45, lambda a: E.centro(c, s, x, y, size, "g", cor, a))


def b_atalho(c, t, C, b):
    palco(c, t)

    def seis():
        a_, b_, c_, d_, e_, f_ = C["s14.a"], C["s14.b"], C["s14.c"], C["s14.d"], C["s14.e"], C["s14.f"]
        E.frase(c, t, C["s14"] + 0.1, [("o", "i", 80, CLARO), ("atalho", "g", 76, BR), ("do", "i", 80, CLARO), ("6", "g", 76, BR)], W / 2, 120, "center")
        for cx, tt, ti in ((520, "6 × 8", a_), (1400, "6 × 4", e_)):
            E.foco(c, t, ti, 0.45, lambda q, cx=cx, tt=tt: E.centro(c, tt, cx, 300, 150, "g", BR, q))
        j1 = ease_io(prog(t, d_, 0.6))
        casa_num(c, t, "4", lerp(340, 400, j1), 640, b_ + 0.1, cor=BR if j1 > 0.5 else CLARO)
        casa_num(c, t, "8", lerp(720, 640, j1), 640, c_ + 0.1, cor=BR if j1 > 0.5 else CLARO)
        E.foco(c, t, b_, 0.45, lambda q: E.centro(c, "metade do 8", 340, 780, 66, "b", CLARO, q * (1 - j1)))
        E.foco(c, t, c_, 0.45, lambda q: E.centro(c, "o próprio 8", 720, 780, 66, "b", CLARO, q * (1 - j1)))
        ti = entre(e_, f_, 0.55)
        j2 = ease_io(prog(t, f_ + 0.2, 0.6))
        casa_num(c, t, "2", lerp(1220, 1280, j2), 640, ti, cor=BR if j2 > 0.5 else CLARO)
        casa_num(c, t, "4", lerp(1600, 1520, j2), 640, f_, cor=BR if j2 > 0.5 else CLARO)
        E.foco(c, t, ti, 0.45, lambda q: E.centro(c, "metade do 4", 1220, 780, 66, "b", CLARO, q * (1 - j2)))
        E.foco(c, t, f_, 0.45, lambda q: E.centro(c, "o próprio 4", 1600, 780, 66, "b", CLARO, q * (1 - j2)))
        E.frase(c, t, d_ + 0.2, [("quarenta", "i", 76, BR), ("e", "i", 76, BR), ("oito", "i", 76, BR)], 520, 800, "center", passo=0.1)
        E.frase(c, t, f_ + 0.4, [("vinte", "i", 76, BR), ("e", "i", 76, BR), ("quatro", "i", 76, BR)], 1400, 800, "center", passo=0.1)
    E.saida(c, t, C["s15"] - 0.1, seis)
    if t < C["s15"]:
        return
    a_, b_, c_, d_, e_ = C["s15.a"], C["s15.b"], C["s15.c"], C["s15.d"], C["s15.e"]
    E.frase(c, t, a_, [("6", "g", 92, BR), ("vezes", "i", 96, CLARO), ("é", "i", 96, CLARO), ("5", "g", 92, BR), ("vezes", "i", 96, CLARO), ("mais", "g", 92, CLARO), ("1", "g", 92, BR), ("vez", "i", 96, CLARO)], W / 2, 170, "center", passo=0.1)
    conta(c, t, "5 × 8 = 40", 560, 340, b_, BR, 100)
    conta(c, t, "40 + 8 = 48", 1340, 340, c_, CLARO, 100)
    E.frase(c, t, entre(c_, d_, 0.45), [("só", "i", 84, BR), ("serve", "i", 84, BR), ("com", "i", 84, BR), ("2,", "g", 80, CLARO), ("4,", "g", 80, CLARO), ("6", "g", 80, CLARO), ("e", "i", 84, BR), ("8", "g", 80, CLARO)], W / 2, 500, "center", passo=0.1)
    E.frase(c, t, d_, [("não", "g", 84, ERRADO), ("compensa", "g", 84, ERRADO), ("em", "i", 92, BR), ("6 × 7", "g", 84, BR)], W / 2, 670, "center", passo=0.1)
    E.frase(c, t, entre(d_, e_, 0.35), [("o", "i", 76, CLARO), ("7", "g", 72, BR), ("não", "i", 76, CLARO), ("se", "i", 76, CLARO), ("corta", "i", 76, CLARO), ("ao", "i", 76, CLARO), ("meio", "i", 76, CLARO), ("sem", "i", 76, CLARO), ("sobrar", "i", 76, CLARO)], W / 2, 780, "center", passo=0.08)
    E.frase(c, t, e_, [("faça", "i", 92, CLARO), ("× 3", "g", 88, BR), ("e", "i", 92, CLARO), ("dobre", "g", 88, BR)], W / 2, 910, "center", passo=0.1)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s16"], [("hora", "i", 72, COR), ("de", "i", 72, COR), ("testar", "i", 72, COR)], XE, 170)
    E.frase(c, t, C["s16.a"], [("8", "g", 96, COR), ("fileiras", "i", 96), ("com", "i", 96), ("8", "g", 96, COR), ("cadeiras", "i", 96)], XE, 360, passo=0.1)
    E.frase(c, t, C["s16.b"], [("6", "g", 96, COR), ("fileiras", "i", 96), ("com", "i", 96), ("4", "g", 96, COR), ("cadeiras", "i", 96)], XE, 510, passo=0.1)
    E.frase(c, t, C["s16.c"], [("quantas", "i", 104), ("cadeiras", "i", 104)], XE, 730, passo=0.1)
    E.frase(c, t, C["s16.c"] + 0.6, [("ao", "g", 104, COR), ("todo?", "g", 104, COR)], XE, 850, passo=0.1)
    E.relogio(c, t, C["s17.a"], 1530, 400, r=180)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    def primeira():
        a_, b_, c_, d_ = C["s18.a"], C["s18.b"], C["s18.c"], C["s18.d"]
        conta(c, t, "8 × 8", W / 2, 240, a_, TINTA, 150)
        E.frase(c, t, a_ + 0.6, [("dobre", "g", 76, COR), ("o", "i", 80), ("8", "g", 76), ("três", "g", 76, COR), ("vezes", "i", 80)], W / 2, 360, "center", passo=0.1)
        corrente(c, t, (8, 16, 32, 64), (entre(a_, b_, 0.6), b_, c_, d_), 330, 640, 420, 96, cor_fim=CERTO)
    E.saida(c, t, C["s19"] - 0.1, primeira)
    if t < C["s19"]:
        return
    a_, b_, c_, d_, e_ = C["s19.a"], C["s19.b"], C["s19.c"], C["s19.d"], C["s19.e"]
    E.linha(c, t, [("6 × 4", "g", 104, TINTA, a_), ("=", "g", 104, TINTA, a_ + 0.6), ("4 × 6", "g", 104, COR, a_ + 0.8)], W / 2, 170, "center")
    corrente(c, t, (6, 12, 24), (entre(a_, b_, 0.7), b_, c_), 430, 460, 520, 92, cor_fim=CERTO)
    conta(c, t, "64 + 24 =", 690, 860, d_, TINTA, 130)
    bola_num(c, t, e_, "88", 1180, 810, 130, cor=CERTO)
    E.foco(c, t, e_ + 0.3, 0.4, lambda q: E.escreve(c, "cadeiras", 1340, 850, 96, "i", TINTA, q))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s20.a"], [("× 4,", "g", 104), ("dobre", "g", 104, COR), ("duas", "g", 104, COR), ("vezes", "i", 110)], W / 2, 280, "center", passo=0.12)
        E.frase(c, t, C["s20.b"], [("× 8,", "g", 104), ("dobre", "g", 104, COR), ("três", "g", 104, COR), ("vezes", "i", 110)], W / 2, 520, "center", passo=0.12)
        E.frase(c, t, C["s20.c"], [("× 6,", "g", 104), ("faça", "i", 110), ("× 3", "g", 104), ("e", "i", 110), ("dobre", "g", 104, COR)], W / 2, 760, "center", passo=0.12)
    E.saida(c, t, C["s21"] - 0.1, resumo)
    if t < C["s21"]:
        return
    E.frase(c, t, C["s21.a"] - 1.0, [("próxima", "i", 84), ("aula", "i", 84)], XE, 270)
    E.frase(c, t, C["s21.a"], [("× 10", "g", 112, COR), ("e", "i", 100), ("× 100", "g", 112, COR)], XE, 400, passo=0.12)
    E.frase(c, t, C["s21.a"] + 0.6, [("de", "i", 84), ("cabeça", "i", 84)], XE, 500)
    E.frase(c, t, C["s21.b"], [("número", "g", 76), ("maior", "g", 76), ("por", "i", 84), ("um", "i", 84), ("algarismo,", "i", 84)], XE, 630, passo=0.1)
    E.frase(c, t, C["s21.b"] + 0.8, [("com", "i", 84), ("a", "i", 84), ("conta", "i", 84), ("armada", "i", 84)], XE, 730, passo=0.1)
    E.foco(c, t, C["s21.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1460, 400, 76, estilo="g", cor=E.SOBRE, a=a))
    p = ease_io(prog(t, C["s21.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1760, 1590, p), lerp(720, 425, p), ep(t, C["s21.c"] + 0.2, 0.4))
    E.frase(c, t, C["s21.d"], [("bons", "i", 120), ("estudos!", "i", 120, COR)], W / 2, 920, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, ideia=b_ideia, quatro=b_quatro, oito=b_oito, tres=b_tres, seis=b_seis, sete=b_sete,
              mapa=b_mapa, erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
