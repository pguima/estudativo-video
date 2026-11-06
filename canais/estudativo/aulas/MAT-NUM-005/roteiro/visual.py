"""Visual — Estudativo · MAT-NUM-005: tabuada com macetes: 2, 5, 9 e 10.
Identidade em _ferramentas/editorial.py. Peças locais: `sala` (cadeiras em grade que giram, para a ordem não importar),
`tabuada` (a tabela inteira que vai sendo pintada) e `nota` (retângulo simples, não copia cédula)."""
import math

import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco
import motor as M
import skia

E.usar("Matemática", "Números e Contas")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-NUM-005_tabuada_macetes_2_5_9_10.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("vezes", "dez", "nove", "mapa", "atalho", "questao", "fim"))
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
def nota(c, cx, cy, w, s, a=1.0, cor=None, giro=0.0):
    """nota de dinheiro didática: retângulo com o valor, sem imitar cédula real"""
    if a <= 0:
        return
    cor = cor or E.COR
    h = w * 0.5
    c.save(); c.translate(cx, cy); c.rotate(giro)
    sombra = skia.Paint(AntiAlias=True, Color=M.hexc("#000000", 0.22 * a))
    sombra.setMaskFilter(skia.MaskFilter.MakeBlur(skia.kNormal_BlurStyle, max(3, w * 0.03)))
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(-w / 2 + 3, -h / 2 + 7, w, h), w * 0.04, w * 0.04), sombra)
    M.rrect(c, -w / 2, -h / 2, w, h, w * 0.04, cor, a)
    m = w * 0.045
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(-w / 2 + m, -h / 2 + m, w - 2 * m, h - 2 * m), w * 0.025, w * 0.025), M.paint(E.SOBRE, 0.45 * a, stroke=max(2, w * 0.008)))
    size = h * 0.5
    E.centro(c, "R$ " + s, 0, size * 0.36, size, "g", E.SOBRE, a)
    c.restore()


def cadeira(c, cx, cy, s, cor, a=1.0):
    """cadeira vista de frente: encosto, assento e dois pés"""
    if a <= 0:
        return
    M.rrect(c, cx - s * 0.3, cy - s * 0.5, s * 0.6, s * 0.5, s * 0.08, cor, a)
    M.rrect(c, cx - s * 0.38, cy + s * 0.02, s * 0.76, s * 0.17, s * 0.06, cor, a)
    M.line(c, cx - s * 0.28, cy + s * 0.15, cx - s * 0.3, cy + s * 0.5, cor, a, max(3, s * 0.08))
    M.line(c, cx + s * 0.28, cy + s * 0.15, cx + s * 0.3, cy + s * 0.5, cor, a, max(3, s * 0.08))


def sala(c, t, cx, cy, fil, col, passo_, s, ta, gira=0.0, cor=TINTA, conta_t=None, conta_d=1.6):
    """cadeiras em grade: entram fileira a fileira; gira = 0..1 vira a sala 90° e as cadeiras seguem em pé. conta_t = onde a contagem corre"""
    ang = gira * math.pi / 2
    co, se = math.cos(ang), math.sin(ang)
    for i in range(fil):
        for j in range(col):
            x, y = (j - (col - 1) / 2) * passo_, (i - (fil - 1) / 2) * passo_
            ti = ta + i * 0.16 + j * 0.04
            k = ease_back(prog(t, ti, 0.45))
            if k <= 0.01:
                continue
            xr, yr = x * co - y * se, x * se + y * co
            tinta = cor
            sal = 1.0
            if conta_t is not None and t >= conta_t:
                n = i * col + j
                f = (t - conta_t) / conta_d * fil * col - n
                if f >= 0:
                    tinta = E.COR
                    sal = 1 + 0.28 * max(0.0, 1 - f * 1.5)
            cadeira(c, cx + xr, cy + yr, s * k * sal, tinta, M.clamp(k * 2))


CEL = 82


def resolvida(i, j):
    return i in (2, 5, 9, 10) or j in (2, 5, 9, 10)


def tabuada(c, t, x, y, ta, tb=1e9, tu=1e9, td=1e9):
    """a tabela do 1 ao 10. tb = pinta as contas com 2, 5, 9 ou 10; tu = as de vezes um; td = realça o que sobrou"""
    for i in range(0, 11):
        for j in range(0, 11):
            q = ep(t, ta + (i + j) * 0.025, 0.3)
            if q <= 0:
                continue
            xc, yc = x + j * CEL, y + i * CEL
            if i == 0 and j == 0:
                continue
            if i == 0 or j == 0:
                E.centro(c, str(i or j), xc + CEL / 2, yc + 58, 44, "b", COR, q)
                continue
            fundo, tinta = E.VAZIO, TINTA2
            if resolvida(i, j):
                p = ep(t, tb + (i + j) * 0.03, 0.3)
                fundo, tinta = E.mix(E.VAZIO, E.COR, p), E.mix(TINTA2, E.SOBRE, p)
            elif i == 1 or j == 1:
                p = ep(t, tu + (i + j) * 0.03, 0.3)
                fundo, tinta = E.mix(E.VAZIO, CLARO, p), E.mix(TINTA2, TINTA, p)
            M.rrect(c, xc + 2, yc + 2, CEL - 4, CEL - 4, 8, fundo, q)
            sobra = not resolvida(i, j) and i != 1 and j != 1
            if sobra and t >= td:
                c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(xc + 3, yc + 3, CEL - 6, CEL - 6), 8, 8), M.paint(TINTA, ep(t, td + (i + j) * 0.02, 0.3), stroke=4))
            E.centro(c, str(i * j), xc + CEL / 2, yc + 56, 40, "b", tinta, q)


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
        E.foco(c, t, C["s01.a"], 0.5, lambda a: E.centro(c, "9 × 7", W / 2, 500, 340, "g", TINTA, a))
        E.frase(c, t, C["s01.b"], [("não", "g", 92), ("é", "g", 92), ("falta", "g", 92), ("de", "g", 92), ("capacidade", "g", 92, COR)], W / 2, 720, "center", passo=0.12)
        E.frase(c, t, entre(C["s01.b"], C["s02"], 0.5), [("mandaram", "i", 84), ("decorar,", "i", 84), ("ninguém", "i", 84), ("mostrou", "i", 84), ("o", "i", 84), ("caminho", "g", 80)], W / 2, 860, "center", passo=0.1)
    E.saida(c, t, C["s02"] - 0.1, trava)
    if t < C["s02"]:
        return
    a_, b_, c_ = C["s02.a"], C["s02.b"], C["s02.c"]
    E.foco(c, t, c_ - 0.2, 0.7, lambda a: E.bola(c, 1450, 620, 280 * ease_back(prog(t, c_ - 0.2, 0.7))), blur=0)
    E.frase(c, t, a_, [("até", "i", 92), ("o", "i", 92), ("fim", "i", 92), ("desta", "i", 92), ("aula", "i", 92), ("as", "i", 92), ("tabuadas", "i", 92), ("do", "i", 92)], XE, 200, passo=0.12)
    for i, s in enumerate(("2", "5", "9", "10")):
        bola_num(c, t, entre(a_, b_, 0.4 + i * 0.12), s, 280 + i * 230, 390, 100)
    E.frase(c, t, b_, [("mais", "g", 96, COR), ("da", "g", 96, COR), ("metade", "g", 96, COR)], XE, 630, passo=0.12)
    E.frase(c, t, b_ + 0.5, [("da", "i", 96), ("tabuada", "i", 96)], XE, 750)
    E.foco(c, t, c_ + 0.2, 0.5, lambda a: (E.escreve(c, "+ atalho", 1280, 605, 84, "g", E.SOBRE, a),
                                           E.escreve(c, "de prova", 1305, 695, 84, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    a_, b_, c_, fim = C["s03.a"], C["s03.b"], C["s03.c"], C["s03.end"]
    E.frase(c, t, a_, [("você", "i", 96), ("só", "i", 96), ("precisa", "i", 96), ("de", "i", 96), ("duas", "g", 92, COR), ("coisas", "g", 92, COR)], W / 2, 220, "center", passo=0.1)
    bola_num(c, t, b_, "+", 560, 520, 130, 170)
    E.foco(c, t, b_ + 0.1, 0.45, lambda q: E.centro(c, "somar", 560, 750, 84, "g", TINTA, q))
    bola_num(c, t, c_, "−", 1360, 520, 130, 170)
    E.foco(c, t, c_ + 0.1, 0.45, lambda q: E.centro(c, "subtrair", 1360, 750, 84, "g", TINTA, q))
    E.frase(c, t, entre(c_, fim, 0.45), [("de", "i", 80), ("cabeça", "i", 80)], W / 2, 750, "center")
    E.frase(c, t, entre(c_, fim, 0.65), [("se", "i", 66, TINTA2), ("faltar", "i", 66, TINTA2), ("alguma,", "i", 66, TINTA2), ("procure", "i", 66, TINTA2), ("no", "i", 66, TINTA2), ("canal", "i", 66, TINTA2)], W / 2, 920, "center", passo=0.08)


# ---------------- o que é vezes ----------------
def b_vezes(c, t, C, b):
    def parcelas():
        a_, b_, c_, d_, e_, f_ = C["s04.a"], C["s04.b"], C["s04.c"], C["s04.d"], C["s04.e"], C["s04.f"]
        E.frase(c, t, a_, [("o", "i", 92), ("que", "i", 92), ("quer", "i", 92), ("dizer", "i", 92), ("vezes?", "g", 88, COR)], W / 2, 160, "center", passo=0.1)
        xs = (480, 800, 1120, 1440)
        for i, x in enumerate(xs):
            q = ease_back(prog(t, b_ + i * 0.16, 0.5))
            if q > 0.01:
                nota(c, x, lerp(260, 330, q), 270, "3", M.clamp(q * 2), giro=(1 - q) * -8)
        E.linha(c, t, [("3", "g", 150, TINTA, c_), ("+", "g", 150, TINTA, entre(c_, d_, 0.2)), ("3", "g", 150, TINTA, entre(c_, d_, 0.25)), ("+", "g", 150, TINTA, entre(c_, d_, 0.45)),
                       ("3", "g", 150, TINTA, entre(c_, d_, 0.5)), ("+", "g", 150, TINTA, entre(c_, d_, 0.7)), ("3", "g", 150, TINTA, entre(c_, d_, 0.75)), ("=", "g", 150, TINTA, d_ - 0.15), ("12", "g", 170, COR, d_)], W / 2, 620, "center")
        E.frase(c, t, e_, [("o", "i", 96), ("3", "g", 92, COR), ("repetido", "i", 96), ("4", "g", 92, COR), ("vezes", "i", 96)], W / 2, 790, "center", passo=0.12)
        E.linha(c, t, [("4", "g", 130, TINTA, f_), ("×", "g", 150, COR, f_ + 0.2), ("3", "g", 130, TINTA, f_ + 0.4)], W / 2, 960, "center")
    E.saida(c, t, C["s05"] - 0.1, parcelas)

    def cadeiras():
        a_, b_, c_, d_ = C["s05.a"], C["s05.b"], C["s05.c"], C["s05.d"]
        cx, cy = 560, 520
        gira = ease_io(prog(t, b_, 1.1))
        sala(c, t, cx, cy, 4, 3, 150, 112, a_, gira, TINTA, conta_t=c_)
        x = 1040
        E.saida(c, t, b_, lambda: E.frase(c, t, a_ + 0.1, [("4", "g", 120, COR), ("fileiras", "i", 110)], x, 300, passo=0.12))
        E.saida(c, t, b_, lambda: E.frase(c, t, a_ + 0.5, [("com", "i", 96), ("3", "g", 96), ("cadeiras", "i", 96)], x, 420, passo=0.12))
        E.frase(c, t, b_ + 0.3, [("3", "g", 120, COR), ("fileiras", "i", 110)], x, 300, passo=0.12)
        E.frase(c, t, b_ + 0.5, [("com", "i", 96), ("4", "g", 96), ("cadeiras", "i", 96)], x, 420, passo=0.12)
        # a contagem corre junto com as cadeiras
        if t >= c_:
            n = min(12, int((t - c_) / 1.6 * 12) + 1)
            cor = COR
            E.foco(c, t, c_, 0.3, lambda q: E.centro(c, str(n), 1480, 690, 230, "g", cor, q))
            E.frase(c, t, c_ + 0.2, [("cadeiras", "i", 92)], x, 660)
        E.frase(c, t, d_, [("a", "i", 96), ("ordem", "g", 92, COR), ("não", "g", 92, COR), ("muda", "g", 92, COR)], x, 850, passo=0.12)
        conta(c, t, "4 × 3 = 3 × 4", x, 970, d_ + 0.5, TINTA, 84, "left")
    if C["s05"] <= t:
        E.saida(c, t, C["s06"] - 0.1, cadeiras)
    if t < C["s06"]:
        return

    a_, fim = C["s06.a"], C["s06.end"]
    tabuada(c, t, 850, 90, a_)
    E.frase(c, t, a_, [("tabuada", "g", 120, COR)], XE, 380)
    E.frase(c, t, a_ + 0.5, [("é", "i", 84), ("a", "i", 84), ("tabela", "i", 84)], XE, 490)
    E.frase(c, t, a_ + 0.9, [("dessas", "i", 84), ("contas", "i", 84)], XE, 585)
    E.frase(c, t, entre(a_, fim, 0.6), [("não", "i", 80), ("precisa", "i", 80), ("entrar", "i", 80)], XE, 740)
    E.frase(c, t, entre(a_, fim, 0.75), [("na", "g", 84), ("marra", "g", 84)], XE, 840)


# ---------------- dez ----------------
def b_dez(c, t, C, b):
    a_, b_, c_, d_, e_, f_ = C["s07.a"], C["s07.b"], C["s07.c"], C["s07.d"], C["s07.e"], C["s07.f"]
    E.frase(c, t, a_, [("a", "i", 100), ("mais", "i", 100), ("fácil:", "i", 100), ("a", "i", 100), ("do", "i", 100), ("10", "g", 104, COR)], XE, 170, passo=0.1)
    E.linha(c, t, [("7 × 10", "g", 130, TINTA, b_), ("=", "g", 130, TINTA, c_ - 0.15), ("70", "g", 150, COR, c_)], XE, 380)
    for i in range(7):
        E.foco(c, t, b_ + 0.2 + i * 0.1, 0.35, lambda q, i=i: nota(c, 300 + i * 66, 560 + (i % 2) * 10, 290, "10", q), sobe=-12)
    E.foco(c, t, d_, 0.45, lambda q: E.pilula(c, "um zero no fim", 560, 800, 76, estilo="g", cor=E.SOBRE, a=q))
    x0, wc = 1090, 300
    E.quadro_casas(c, t, ("dezena", "unidade"), (e_, f_), [[("7", e_), ("0", f_, COR)]], x0, 360, wc, 190, grossa=None)
    E.frase(c, t, e_ + 0.3, [("sete", "g", 80, COR), ("dezenas", "i", 88)], x0 + wc, 720, "center", passo=0.12)
    E.frase(c, t, f_ + 0.2, [("unidade", "i", 84), ("vazia", "g", 80, COR)], x0 + wc, 840, "center", passo=0.12)


# ---------------- dois ----------------
def fila(c, t, n, x, y, r, ti, cor=None):
    for i in range(n):
        k = ease_back(prog(t, ti + i * 0.06, 0.35))
        if k > 0.01:
            E.moeda(c, x + i * (2 * r + 14), y, r * k, "1", M.clamp(k * 2), cor=cor)


def b_dois(c, t, C, b):
    a_, b_, c_, d_, e_, f_ = C["s08.a"], C["s08.b"], C["s08.c"], C["s08.d"], C["s08.e"], C["s08.f"]
    E.frase(c, t, a_, [("a", "i", 96), ("do", "i", 96), ("2", "g", 96, COR), ("é", "i", 96), ("o", "i", 96), ("dobro", "g", 96, COR)], XE, 170, passo=0.1)
    E.frase(c, t, a_ + 0.9, [("o", "i", 72, TINTA2), ("número", "i", 72, TINTA2), ("somado", "i", 72, TINTA2), ("com", "i", 72, TINTA2), ("ele", "i", 72, TINTA2), ("mesmo", "i", 72, TINTA2)], XE, 270, passo=0.08)
    conta(c, t, "6 × 2 = 2 × 6", XE, 430, b_, TINTA, 92, "left")
    conta(c, t, "6 + 6", XE, 560, c_, TINTA, 104, "left")
    conta(c, t, "= 12", XE + 340, 560, d_, COR, 120, "left")
    fila(c, t, 6, 1040, 400, 42, c_)
    fila(c, t, 6, 1040, 500, 42, c_ + 0.3, TINTA)
    conta(c, t, "8 × 2", XE, 740, e_, TINTA, 92, "left")
    conta(c, t, "8 + 8", XE, 870, entre(e_, f_, 0.4), TINTA, 104, "left")
    conta(c, t, "= 16", XE + 340, 870, f_, COR, 120, "left")
    fila(c, t, 8, 1040, 720, 42, entre(e_, f_, 0.4))
    fila(c, t, 8, 1040, 820, 42, entre(e_, f_, 0.4) + 0.3, TINTA)


# ---------------- cinco ----------------
def b_cinco(c, t, C, b):
    def regra():
        a_, b_, c_ = C["s09.a"], C["s09.b"], C["s09.c"]
        E.frase(c, t, C["s09"] + 0.1, [("a", "i", 88), ("do", "i", 88), ("5", "g", 88, COR), ("usa", "i", 88), ("a", "i", 88), ("do", "i", 88), ("10", "g", 88, COR)], W / 2, 150, "center", passo=0.1)
        E.foco(c, t, a_, 0.45, lambda q: nota(c, 560, 320, 380, "10", q))
        E.sinal(c, t, a_ + 0.4, "=", 870, 320, 100)
        E.foco(c, t, a_ + 0.6, 0.4, lambda q: nota(c, 1090, 320, 280, "5", q))
        E.foco(c, t, a_ + 0.8, 0.4, lambda q: nota(c, 1400, 320, 280, "5", q))
        E.foco(c, t, a_ + 1.0, 0.4, lambda q: E.centro(c, "metade", 1245, 490, 76, "g", COR, q))
        for i in range(7):
            E.foco(c, t, b_ + i * 0.1, 0.35, lambda q, i=i: nota(c, 290 + i * 46, 660 + (i % 2) * 8, 260, "5", q), sobe=-12)
        E.frase(c, t, b_ + 0.9, [("=", "g", 84), ("metade", "g", 84, COR), ("de", "i", 88), ("7", "g", 84), ("notas", "i", 88), ("de", "i", 88), ("10", "g", 84)], 760, 690, passo=0.1)
        E.frase(c, t, c_, [("faça", "i", 96), ("× 10", "g", 92), ("e", "i", 96), ("corte", "g", 92, COR), ("ao", "g", 92, COR), ("meio", "g", 92, COR)], W / 2, 900, "center", passo=0.12)
    E.saida(c, t, C["s10"] - 0.1, regra)
    if t < C["s10"]:
        return
    a_, b_, c_, d_, e_, f_, g_ = C["s10.a"], C["s10.b"], C["s10.c"], C["s10.d"], C["s10.e"], C["s10.f"], C["s10.g"]
    conta(c, t, "7 × 5", 500, 220, a_, COR, 140)
    conta(c, t, "× 10 = 70", 500, 370, b_, TINTA, 88)
    conta(c, t, "metade de 60 = 30", 500, 500, c_, TINTA, 76)
    conta(c, t, "metade de 10 = 5", 500, 620, d_, TINTA, 76)
    conta(c, t, "30 + 5", 340, 830, e_ - 0.2, TINTA, 96)
    bola_num(c, t, e_, "35", 720, 800, 130)
    conta(c, t, "8 × 5", 1380, 220, f_, COR, 140)
    conta(c, t, "× 10 = 80", 1380, 370, entre(f_, g_, 0.4), TINTA, 88)
    conta(c, t, "metade", 1200, 830, g_ - 0.3, TINTA, 96)
    bola_num(c, t, g_, "40", 1580, 800, 130)


# ---------------- nove ----------------
def b_nove(c, t, C, b):
    def regra():
        a_, b_, c_, d_, e_, fim = C["s11.a"], C["s11.b"], C["s11.c"], C["s11.d"], C["s11.e"], C["s11.end"]
        E.frase(c, t, a_, [("9", "g", 92, COR), ("vezes", "i", 96), ("é", "i", 96), ("10", "g", 92), ("vezes", "i", 96), ("menos", "g", 92, COR), ("1", "g", 92, COR), ("vez", "i", 96)], W / 2, 160, "center", passo=0.1)
        y = 340
        for i in range(10):
            x = 225 + i * 163
            q = ease_back(prog(t, b_ + i * 0.09, 0.45))
            if q <= 0.01:
                continue
            sai = ease_io(prog(t, d_ + 0.1, 0.7)) if i == 9 else 0
            nota(c, x, lerp(280, y, q) - sai * 150, 160, "7", M.clamp(q * 2) * (1 - sai), ERRADO if sai > 0 else None, giro=sai * 18)
        E.foco(c, t, entre(b_, c_, 0.7), 0.4, lambda q: E.centro(c, "9 parcelas de R$ 7", 800, 500, 60, "i", TINTA2, q))
        conta(c, t, "10 × 7 = 70", W / 2, 640, c_, TINTA, 120)
        E.linha(c, t, [("70", "g", 120, TINTA, d_), ("−", "g", 120, ERRADO, d_ + 0.15), ("7", "g", 120, ERRADO, d_ + 0.3), ("=", "g", 120, TINTA, e_ - 0.15), ("63", "g", 150, COR, e_)], W / 2, 810, "center")
        E.frase(c, t, entre(e_, fim, 0.5), [("confira:", "i", 76, TINTA2), ("63", "g", 72), ("+", "g", 72), ("7", "g", 72), ("=", "g", 72), ("70", "g", 72, CERTO)], W / 2, 950, "center", passo=0.1)
    E.saida(c, t, C["s12"] - 0.1, regra)
    if t < C["s12"]:
        return
    a_, b_ = C["s12.a"], C["s12.b"]
    conta(c, t, "9 × 4", W / 2, 320, a_, COR, 190)
    conta(c, t, "10 × 4 = 40", W / 2, 520, entre(a_, b_, 0.3), TINTA, 110)
    E.linha(c, t, [("40", "g", 110, TINTA, entre(a_, b_, 0.75)), ("−", "g", 110, ERRADO, entre(a_, b_, 0.8)), ("4", "g", 110, ERRADO, entre(a_, b_, 0.85)), ("=", "g", 110, TINTA, b_ - 0.1), ("36", "g", 140, COR, b_)], W / 2, 700, "center")


# ---------------- a tabela inteira ----------------
def b_mapa(c, t, C, b):
    a_, b_, c_, d_ = C["s13.a"], C["s13.b"], C["s13.c"], C["s13.d"]
    tabuada(c, t, 850, 90, a_, b_, c_, d_)
    E.frase(c, t, a_, [("a", "i", 96), ("tabuada", "g", 92, COR)], XE, 230)
    E.frase(c, t, a_ + 0.4, [("inteira", "g", 92, COR)], XE, 330)
    E.frase(c, t, b_, [("com", "i", 76), ("2,", "g", 72), ("5,", "g", 72), ("9", "g", 72), ("ou", "i", 76), ("10:", "g", 72)], XE, 470, passo=0.1)
    E.frase(c, t, b_ + 0.5, [("resolvida", "g", 92, COR)], XE, 570)
    E.frase(c, t, c_, [("vezes", "i", 76), ("1:", "g", 72)], XE, 690, passo=0.1)
    E.frase(c, t, c_ + 0.4, [("o", "i", 76), ("próprio", "i", 76), ("número", "i", 76)], XE, 780, passo=0.1)
    E.frase(c, t, d_, [("sobrou", "i", 80), ("bem", "g", 76, COR), ("menos", "g", 76, COR)], XE, 910, passo=0.12)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    a_, b_, c_, d_ = C["s14.a"], C["s14.b"], C["s14.c"], C["s14.d"]
    E.frase(c, t, a_, [("somar", "g", 92, ERRADO), ("no", "i", 96), ("lugar", "i", 96), ("de", "i", 96), ("multiplicar", "g", 92)], W / 2, 170, "center", passo=0.1)
    E.linha(c, t, [("6 × 2", "g", 150, TINTA, a_ + 0.6), ("=", "g", 150, TINTA, b_ - 0.15), ("8", "g", 170, ERRADO, b_)], W / 2, 410, "center")
    r = 66 * ease_back(prog(t, b_ + 0.3, 0.5))
    E.selo(c, 1420, 350, r, False)
    conta(c, t, "8 é 6 + 2", W / 2, 570, c_, ERRADO, 104)
    ti = entre(c_, d_, 0.4)
    E.frase(c, t, ti, [("o", "i", 84), ("2", "g", 80, COR), ("repetido", "i", 84), ("6", "g", 80, COR), ("vezes", "i", 84)], W / 2, 700, "center", passo=0.1)
    E.linha(c, t, [("2", "g", 110, TINTA, ti + 0.3), ("+", "g", 110, TINTA, ti + 0.4), ("2", "g", 110, TINTA, ti + 0.5), ("+", "g", 110, TINTA, ti + 0.6), ("2", "g", 110, TINTA, ti + 0.7), ("+", "g", 110, TINTA, ti + 0.8),
                   ("2", "g", 110, TINTA, ti + 0.9), ("+", "g", 110, TINTA, ti + 1.0), ("2", "g", 110, TINTA, ti + 1.1), ("+", "g", 110, TINTA, ti + 1.2), ("2", "g", 110, TINTA, ti + 1.3), ("=", "g", 110, TINTA, d_ - 0.1), ("12", "g", 130, CERTO, d_)], W / 2, 870, "center")


# ---------------- atalho ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def casas():
        a_, b_, c_, d_ = C["s15.a"], C["s15.b"], C["s15.c"], C["s15.d"]
        E.frase(c, t, C["s15"] + 0.1, [("o", "i", 84, CLARO), ("atalho", "g", 80, BR), ("do", "i", 84, CLARO), ("9", "g", 80, BR)], W / 2, 130, "center")
        E.foco(c, t, a_, 0.45, lambda q: E.centro(c, "9 × 7", W / 2, 310, 180, "g", BR, q))
        s = 340
        junta = ease_io(prog(t, d_, 0.7))
        x1, x2 = lerp(620, 790, junta), lerp(1300, 1130, junta)
        cor = BR if junta > 0.5 else CLARO
        E.foco(c, t, b_ + 0.1, 0.45, lambda q: E.centro(c, "6", x1, 700, s, "g", cor, q))
        E.foco(c, t, c_ + 0.1, 0.45, lambda q: E.centro(c, "3", x2, 700, s, "g", cor, q))
        q = 1 - junta
        E.foco(c, t, b_, 0.45, lambda a: E.centro(c, "7 − 1 = 6", 620, 860, 76, "g", CLARO, a * q))
        E.foco(c, t, c_, 0.45, lambda a: E.centro(c, "do 6 até o 9: 3", 1300, 860, 76, "g", CLARO, a * q))
        E.frase(c, t, d_ + 0.3, [("sessenta", "i", 92, BR), ("e", "i", 92, BR), ("três", "i", 92, BR)], W / 2, 900, "center", passo=0.12)
    E.saida(c, t, C["s16"] - 0.1, casas)
    if t < C["s16"]:
        return
    a_, b_, c_, d_, e_, f_, g_ = C["s16.a"], C["s16.b"], C["s16.c"], C["s16.d"], C["s16.e"], C["s16.f"], C["s16.g"]
    E.foco(c, t, a_, 0.45, lambda q: E.centro(c, "70 − 7", 440, 240, 150, "g", BR, q))
    E.frase(c, t, b_, [("a", "i", 72, CLARO), ("dezena", "i", 72, CLARO), ("cai", "i", 72, CLARO), ("de", "i", 72, CLARO), ("7", "g", 72, BR), ("para", "i", 72, CLARO), ("6", "g", 72, BR)], 790, 180, passo=0.08)
    E.frase(c, t, c_, [("do", "i", 72, CLARO), ("7", "g", 72, BR), ("até", "i", 72, CLARO), ("o", "i", 72, CLARO), ("10:", "g", 72, BR), ("3", "g", 80, BR)], 790, 300, passo=0.08)
    E.frase(c, t, d_, [("do", "i", 72, CLARO), ("6", "g", 72, BR), ("até", "i", 72, CLARO), ("o", "i", 72, CLARO), ("9:", "g", 72, BR), ("o", "i", 72, CLARO), ("mesmo", "i", 72, CLARO), ("3", "g", 80, BR)], 790, 420, passo=0.08)
    E.frase(c, t, e_, [("não", "g", 80, ERRADO), ("compensa", "g", 80, ERRADO), ("fora", "i", 88, BR), ("da", "i", 88, BR), ("tabuada", "i", 88, BR)], W / 2, 640, "center", passo=0.1)
    E.frase(c, t, f_, [("9 × 12:", "g", 76, BR), ("tirar", "i", 80, CLARO), ("um", "i", 80, CLARO), ("dá", "i", 80, CLARO), ("11,", "g", 76, BR), ("e", "i", 80, CLARO), ("11", "g", 76, BR), ("passa", "i", 80, CLARO), ("de", "i", 80, CLARO), ("9", "g", 76, BR)], W / 2, 780, "center", passo=0.08)
    E.frase(c, t, g_, [("volte", "i", 84, CLARO), ("para", "i", 84, CLARO), ("10", "g", 80, BR), ("vezes", "g", 80, BR), ("menos", "g", 80, BR), ("1", "g", 80, BR), ("vez", "g", 80, BR)], W / 2, 910, "center", passo=0.1)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s17"], [("hora", "i", 72, COR), ("de", "i", 72, COR), ("testar", "i", 72, COR)], XE, 170)
    E.frase(c, t, C["s17.a"], [("9", "g", 100, COR), ("caixas", "i", 100), ("com", "i", 100), ("8", "g", 100, COR), ("garrafas", "i", 100)], XE, 360, passo=0.1)
    E.frase(c, t, C["s17.b"], [("5", "g", 100, COR), ("caixas", "i", 100), ("com", "i", 100), ("6", "g", 100, COR), ("garrafas", "i", 100)], XE, 510, passo=0.1)
    E.frase(c, t, C["s17.c"], [("quantas", "i", 104), ("garrafas", "i", 104)], XE, 730, passo=0.1)
    E.frase(c, t, C["s17.c"] + 0.6, [("ao", "g", 104, COR), ("todo?", "g", 104, COR)], XE, 850, passo=0.1)
    E.relogio(c, t, C["s18.a"], 1520, 400, r=190)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    a_, b_, c_, d_, e_, f_ = C["s19.a"], C["s19.b"], C["s19.c"], C["s19.d"], C["s19.e"], C["s19.f"]
    conta(c, t, "9 × 8", 500, 210, a_, COR, 140)
    conta(c, t, "10 × 8 = 80", 500, 360, entre(a_, b_, 0.3), TINTA, 92)
    E.foco(c, t, entre(a_, b_, 0.75), 0.4, lambda q: E.centro(c, "80 − 8", 340, 540, 92, "g", TINTA, q))
    bola_num(c, t, b_, "72", 730, 510, 100)
    conta(c, t, "5 × 6", 1380, 210, c_, COR, 140)
    conta(c, t, "10 × 6 = 60", 1380, 360, entre(c_, d_, 0.35), TINTA, 92)
    E.foco(c, t, entre(c_, d_, 0.75), 0.4, lambda q: E.centro(c, "metade", 1230, 540, 84, "i", TINTA, q))
    bola_num(c, t, d_, "30", 1600, 510, 100)
    conta(c, t, "72 + 30 =", 680, 800, e_, TINTA, 130)
    bola_num(c, t, f_, "102", 1180, 750, 150, cor=CERTO)
    E.foco(c, t, f_ + 0.3, 0.4, lambda q: E.escreve(c, "garrafas", 1360, 790, 96, "i", TINTA, q))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s20.a"], [("vezes", "i", 110), ("é", "i", 110), ("soma", "g", 104, COR), ("repetida", "g", 104, COR)], W / 2, 280, "center", passo=0.12)
        E.frase(c, t, C["s20.b"], [("× 5", "g", 104), ("é", "i", 110), ("metade", "g", 104, COR), ("de", "i", 110), ("× 10", "g", 104)], W / 2, 520, "center", passo=0.12)
        E.frase(c, t, C["s20.c"], [("× 9", "g", 104), ("é", "i", 110), ("× 10", "g", 104), ("menos", "g", 104, COR), ("uma", "g", 104, COR), ("vez", "g", 104, COR)], W / 2, 760, "center", passo=0.12)
    E.saida(c, t, C["s21"] - 0.1, resumo)
    if t < C["s21"]:
        return
    E.frase(c, t, C["s21.a"] - 1.0, [("próxima", "i", 84), ("aula", "i", 84)], XE, 270)
    E.frase(c, t, C["s21.a"], [("as", "g", 100, COR), ("tabuadas", "g", 100, COR)], XE, 400, passo=0.12)
    E.frase(c, t, C["s21.a"] + 0.5, [("que", "g", 100, COR), ("faltam", "g", 100, COR)], XE, 510, passo=0.12)
    E.frase(c, t, C["s21.b"], [("dobrando", "g", 84), ("o", "i", 84), ("que", "i", 84), ("já", "i", 84), ("sabe", "i", 84)], XE, 640, passo=0.1)
    E.foco(c, t, C["s21.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1400, 400, 76, estilo="g", cor=E.SOBRE, a=a))
    p = ease_io(prog(t, C["s21.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1760, 1530, p), lerp(720, 425, p), ep(t, C["s21.c"] + 0.2, 0.4))
    E.frase(c, t, C["s21.d"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 880, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, vezes=b_vezes, dez=b_dez, dois=b_dois, cinco=b_cinco, nove=b_nove, mapa=b_mapa,
              erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
