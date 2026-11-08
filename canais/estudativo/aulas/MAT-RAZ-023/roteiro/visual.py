"""Visual — Estudativo · MAT-RAZ-023: praticando escalas (fim da trilha Razão e Proporção).
Aula de prática no mesmo molde da MAT-RAZ-019: cinco situações, cada uma com enunciado (com relógio de pausa) e resposta.
Peças locais: barra() é a escala gráfica da MAT-RAZ-021; sala() é a planta em quadradinhos da MAT-RAZ-022; trecho() marca um
pedaço medido. Todo instante vem de C[...]."""
from decimal import Decimal as D

import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Razão e Proporção")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-RAZ-023_praticando_escalas.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("questao1", "questao2", "questao3", "questao4", "questao5", "fim"))
BR = "#FFFFFF"

assert 6 * 500000 == 3000000 and 3000000 // 100000 == 30 and 500000 // 100000 == 5 and 6 * 5 == 30
assert 6 * 100 == 600 and 600 // 50 == 12 and D(6) / 50 == D("0.12")
assert 8 // 2 == 4 and 4 * 3 == 12 and 3 * 100000 == 300000 and 300000 // 2 == 150000 and 8 * 150000 == 1200000 and 1200000 // 100000 == 12
assert 200 // 100 == 2 and 4 * 2 == 8 and 3 * 2 == 6 and 8 * 6 == 48 and 4 * 3 == 12 and 200 ** 2 == 40000
assert 12 * 40000 == 480000 and 480000 // 10000 == 48 and D(12 * 200) / 10000 == D("0.24")
assert 20 ** 3 == 8000 and 2 * 8000 == 16000 and 16000 // 1000 == 16


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


def fcen(c, t, t0, s, cx, y, size, cor=None, est="g"):
    E.formula_em(c, t, t0, s, cx, y, size, est, cor, "center")


def fesq(c, t, t0, s, x, y, size, cor=None, est="g"):
    E.formula_em(c, t, t0, s, x, y, size, est, cor, "left")


def bola_res(c, t, t0, s, cx, cy, r=130, size=80, cor=None):
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r, cor, a), centro(c, s, cx, cy + size * 0.36, size, "g", E.SOBRE, a)))


def pil(c, t, t0, s, cx, cy, size=52, fundo=None):
    E.foco(c, t, t0, 0.5, lambda a: E.pilula(c, s, cx, cy, size, "g", fundo=fundo, a=a, cor=E.SOBRE if fundo is None else BR))


def selo_em(c, t, t0, cx, cy, ok=True, r=44):
    E.foco(c, t, t0, 0.5, lambda a: E.selo(c, cx, cy, r, ok, a))


def titulo_sit(c, t, t0, n, nome):
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, XE + 50, 170, 56, a=a), centro(c, str(n), XE + 50, 193, 64, "g", E.SOBRE, a)))
    E.frase(c, t, t0 + 0.15, [("situação", "i", 72, COR), (nome, "g", 72)], XE + 130, 195, "left", 0.12)


def enunciado(c, t, C, n, nome, cena, linhas, pausa):
    """linhas = [(instante, partes, y)]; pausa = instante do relógio"""
    titulo_sit(c, t, C[cena + ".a"], n, nome)
    for t0, partes, y in linhas:
        E.frase(c, t, t0, partes, XE, y, "left", 0.1)
    E.relogio(c, t, pausa, 1570, 470, 170)


def cab(c, t, t0, n, nome):
    """cabeçalho pequeno da resposta"""
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, XE + 30, 110, 36, a=a), centro(c, str(n), XE + 30, 125, 42, "g", E.SOBRE, a),
                                      E.escreve(c, nome, XE + 85, 126, 46, "i", TINTA2, a)))


def barra(c, x, y, n, tr, a=1.0, rotulos=None, size=46, h=26):
    """escala gráfica: n trechos de `tr` px, alternando cheio e vazio"""
    if a <= 0:
        return
    for i in range(n):
        r = skia.Rect.MakeXYWH(x + i * tr, y, tr, h)
        c.drawRect(r, M.paint(TINTA if i % 2 == 0 else "#FFFFFF", a))
        c.drawRect(r, M.paint(TINTA, a, stroke=4))
    for i, s in enumerate(rotulos or ()):
        centro(c, s, x + i * tr, y + h + size * 1.2, size, "b", TINTA, a)


def trecho(c, t, t0, x0, x1, y, rot, cor=None, size=46, cima=True):
    q = ep(t, t0, 0.5)
    if q <= 0:
        return
    cor = cor or E.COR
    E.chave(c, x0, x1, y, cor, q, -22 if cima else 22, 5)
    E.foco(c, t, t0 + 0.2, 0.4, lambda a: centro(c, rot, (x0 + x1) / 2, y + (-48 if cima else 48 + size * 0.7), size, "g", cor, a))


def sala(c, x, y, cols, lins, u, a=1.0, pinta=0.0):
    """planta em quadradinhos de u px"""
    if a <= 0:
        return
    w, h = cols * u, lins * u
    c.drawRect(skia.Rect.MakeXYWH(x, y, w, h), M.paint("#FFFFFF", a * 0.9))
    n = cols * lins
    for k in range(int(n * pinta + 0.999)):
        i, j = k % cols, k // cols
        c.drawRect(skia.Rect.MakeXYWH(x + i * u + 3, y + j * u + 3, u - 6, u - 6), M.paint(E.COR, a * 0.85 * min(1.0, n * pinta - k)))
    for i in range(1, cols):
        M.line(c, x + i * u, y, x + i * u, y + h, FIO, a, 3)
    for j in range(1, lins):
        M.line(c, x, y + j * u, x + w, y + j * u, FIO, a, 3)
    c.drawRect(skia.Rect.MakeXYWH(x, y, w, h), M.paint(TINTA, a, stroke=6))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    a1, b1, c1 = C["s01.a"], C["s01.b"], C["s01.c"]
    E.foco(c, t, a1, 0.5, lambda a: E.escreve(c, "5", XE - 8, 470, 340, "g", COR, a))
    E.frase(c, t, a1 + 0.2, ps("situações", "i", 120), XE + 215, 450, "left")
    E.frase(c, t, lerp(a1, b1, 0.35), ps("mapas, plantas e maquetes", "i", 60, TINTA2), XE + 10, 560, "left", 0.1)
    nomes = ("distância no mapa", "corredor na planta", "trilha e barra", "área do apartamento", "volume na maquete")
    for i, s in enumerate(nomes):
        ti = lerp(a1, b1, 0.5 + i * 0.1)
        y = 190 + i * 150
        E.foco(c, t, ti, 0.5, lambda a, i=i, s=s, y=y: (E.bola(c, 1000, y, 44, a=a), centro(c, str(i + 1), 1000, y + 18, 50, "g", E.SOBRE, a),
                                                         E.escreve(c, s, 1070, y + 22, 62, "g", TINTA, a)))
    E.foco(c, t, b1, 0.5, lambda a: E.pilula(c, "pause · resolva · confira", 520, 760, 54, "g", a=a, cor=E.SOBRE))
    E.frase(c, t, c1, ps("o que derruba:", "i", 64) + [("unidade e quadrado", "g", 64, ERRADO)], XE, 930, "left", 0.1)


# ---------------- ferramentas ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s02"] + 0.2, ps("você vai usar", "i", 80), XE, 410, passo=0.14)
    E.foco(c, t, C["s02"] + 0.6, 0.5, lambda a: E.escreve(c, "4", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s02"] + 0.75, 0.5, lambda a: E.escreve(c, "ferramentas", XE + 215, 700, 100, "i", TINTA, a))
    x, w = 930, 860
    itens = (("s02.a", "escala:", "desenho sobre real, mesma unidade"), ("s02.b", "papel → real multiplica,", "real → papel divide"),
             ("s02.c", "escala gráfica:", "mede com a régua"), ("s02.d", "área ao quadrado,", "volume ao cubo"))
    for i, (k, l1, l2) in enumerate(itens):
        y = 90 + i * 215
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 180, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "b" if "→" in l1 else "i", 52)], x + 40, y + 76)
        E.frase(c, t, C[k] + 0.3, [(l2, "g", 52, COR)], x + 40, y + 148)
    E.frase(c, t, lerp(C["s02.d"], C["s02.end"], 0.55), ps("travou?", "i", 54, COR) + ps("procure a aula no canal", "i", 54), XE, 960, "left", 0.1)


# ---------------- situação 1: distância no mapa ----------------
def b_questao1(c, t, C, b):
    k = lambda s: C["s03." + s]
    enunciado(c, t, C, 1, "distância no mapa", "s03", [
        (k("b"), ps("escala", "i", 80) + [("1 : 500.000", "g", 80, COR)], 400),
        (k("c"), ps("no mapa:", "i", 80) + [("6 cm", "g", 80, COR)], 540),
        (k("d"), ps("distância real", "i", 88) + [("em km?", "g", 88, COR)], 800)], C["s04.a"])


def b_resposta1(c, t, C, b):
    a5, b5, c5, d5 = (C[f"s05.{k}"] for k in "abcd")
    cab(c, t, C["s05"], 1, "distância no mapa")
    E.frase(c, t, C["s05"] + 0.4, ps("do papel para o real:", "i", 72) + [("multiplica", "g", 76, COR)], W / 2, 250, "center", 0.1)
    fcen(c, t, a5, "6 × 500.000 = 3.000.000 cm", W / 2, 430, 96)
    pil(c, t, b5 - 0.6, "vírgula 5 casas ←", 620, 590, 50, TINTA)
    fesq(c, t, b5, "= 30 km", 900, 620, 110, COR)
    E.frase(c, t, c5 - 0.4, ps("pelo", "i", 70) + [("atalho:", "g", 70, COR)], 420, 820, "center", 0.1)
    fesq(c, t, c5, "1 cm = 5 km", 640, 830, 88)
    fesq(c, t, d5, "6 × 5 =", 640, 970, 88)
    bola_res(c, t, d5 + 0.5, "30 km", 1130, 940, 115, 64, CERTO)


# ---------------- situação 2: corredor na planta ----------------
def b_questao2(c, t, C, b):
    k = lambda s: C["s06." + s]
    enunciado(c, t, C, 2, "corredor na planta", "s06", [
        (k("b"), ps("corredor:", "i", 80) + [("6 m", "g", 80, COR)], 400),
        (k("c"), ps("planta", "i", 80) + [("1 : 50", "g", 80, COR)], 540),
        (k("d"), ps("quantos", "i", 88) + [("cm no papel?", "g", 88, COR)], 800)], C["s07.a"])


def b_resposta2(c, t, C, b):
    a8, b8, c8 = C["s08.a"], C["s08.b"], C["s08.c"]
    a9, b9, c9 = C["s09.a"], C["s09.b"], C["s09.c"]
    cab(c, t, C["s08"], 2, "corredor na planta")

    def certo():
        pil(c, t, C["s08"] + 0.4, "primeiro, a mesma unidade", W / 2, 250, 54)
        fcen(c, t, a8, "6 m = 600 cm", W / 2, 430, 100)
        E.frase(c, t, b8 - 0.6, ps("do real para o papel:", "i", 70) + [("divide", "g", 74, COR)], W / 2, 570, "center", 0.1)
        fcen(c, t, b8, "600 ÷ 50 = 12 cm", W / 2, 720, 110, COR)
        E.frase(c, t, c8, ps("desenho", "i", 70) + [("menor", "g", 74, CERTO)] + ps("que o real:", "i", 70) + [("12 cm < 6 m", "g", 74, CERTO)], W / 2, 900, "center", 0.1)
        selo_em(c, t, c8 + 0.8, 1640, 875)
    E.saida(c, t, a9 - 0.1, certo)
    if t < a9 - 0.1:
        return
    E.frase(c, t, a9, [("o erro:", "g", 80, ERRADO)] + ps("dividir sem converter", "i", 76), W / 2, 300, "center", 0.12)
    fcen(c, t, a9 + 0.8, "6 ÷ 50", 700, 520, 120, ERRADO)
    fcen(c, t, b9, "= 0,12 cm?", 1180, 520, 120, ERRADO)
    E.frase(c, t, lerp(b9, c9, 0.35), ps("um", "i", 66, ERRADO) + [("risquinho", "g", 66, ERRADO)] + ps("no papel", "i", 66, ERRADO), W / 2, 680, "center", 0.1)
    tr = lerp(b9, c9, 0.6)
    if t >= tr:
        E.risco(c, 520, 560, 1440, 440, t, tr, largura=14)
    pil(c, t, c9, "converta antes de dividir", W / 2, 870, 64)


# ---------------- situação 3: trilha e escala gráfica ----------------
U3 = 110


def b_questao3(c, t, C, b):
    k = lambda s: C["s10." + s]
    titulo_sit(c, t, k("a"), 3, "trilha e barra")
    E.frase(c, t, k("b") - 0.8, ps("na barra,", "i", 76) + [("0 a 3 km", "g", 76, COR)] + ps("mede", "i", 76) + [("2 cm", "g", 76, COR)], XE, 360, "left", 0.1)
    E.foco(c, t, k("b"), 0.5, lambda a: barra(c, XE + 10, 420, 2, 2 * U3, a, ("0", "3", "6 km"), 40))
    E.frase(c, t, k("c"), ps("trilha no mapa:", "i", 76) + [("8 cm", "g", 76, COR)], XE, 640, "left", 0.1)
    E.frase(c, t, k("d"), ps("comprimento", "i", 80) + [("real?", "g", 80, COR)], XE, 800, "left", 0.1)
    E.frase(c, t, k("e"), ps("e a", "i", 80) + [("escala numérica?", "g", 80, COR)], XE, 920, "left", 0.1)
    E.relogio(c, t, C["s11.a"], 1570, 470, 170)


def b_resposta3(c, t, C, b):
    a12, b12 = C["s12.a"], C["s12.b"]
    a13, b13, c13, d13 = (C[f"s13.{k}"] for k in "abcd")
    cab(c, t, C["s12"], 3, "trilha e barra")
    x0, y0 = XE + 10, 300
    E.foco(c, t, C["s12"] + 0.2, 0.5, lambda a: barra(c, x0, y0, 4, 2 * U3, a, None, 40))
    E.foco(c, t, C["s12"] + 0.4, 0.4, lambda a: centro(c, "trilha: 8 cm = 4 trechos de 2 cm", x0 + 4 * U3, y0 - 40, 50, "b", TINTA2, a))
    for i in range(4):
        trecho(c, t, a12 + 0.25 * i, x0 + i * 2 * U3 + 6, x0 + (i + 1) * 2 * U3 - 6, y0 + 40, "3 km", E.COR, 44, cima=False)
    fesq(c, t, b12, "4 × 3 = 12 km", 1240, 360, 90, CERTO)
    fesq(c, t, a13, "3 km = 300.000 cm", XE, 600, 76)
    fesq(c, t, b13, "real ÷ desenho: 300.000 ÷ 2 = 150.000", XE, 720, 60)
    bola_res(c, t, c13, "1 : 150.000", 1640, 680, 160, 50)
    fesq(c, t, d13, "8 × 150.000 = 1.200.000 cm = 12 km", XE, 920, 66, TINTA2)
    selo_em(c, t, lerp(d13, C["s13.end"], 0.5), 1500, 895)


# ---------------- situação 4: área do apartamento ----------------
def b_questao4(c, t, C, b):
    k = lambda s: C["s14." + s]
    enunciado(c, t, C, 4, "área do apartamento", "s14", [
        (k("b"), ps("planta", "i", 80) + [("1 : 200", "g", 80, COR)], 400),
        (k("c"), ps("retângulo de", "i", 80) + [("4 cm × 3 cm", "g", 80, COR)], 540),
        (k("d"), ps("área real", "i", 88) + [("em m²?", "g", 88, COR)], 800)], C["s15.a"])


def b_resposta4(c, t, C, b):
    a16, b16, c16, d16, e16 = (C[f"s16.{k}"] for k in "abcde")
    a17, b17, c17, d17, e17 = (C[f"s17.{k}"] for k in "abcde")
    cab(c, t, C["s16"], 4, "área do apartamento")
    u, x0, y0 = 90, 230, 330
    E.foco(c, t, C["s16"] + 0.2, 0.6, lambda a: sala(c, x0, y0, 4, 3, u, a, pinta=ep(t, e16, 1.2)))
    real_b, real_h = ep(t, c16, 0.4), ep(t, d16, 0.4)
    E.foco(c, t, C["s16"] + 0.4, 0.4, lambda a: (centro(c, "4 cm", x0 + 2 * u, y0 + 3 * u + 70, 56, "g", TINTA, a * (1 - real_b)),
                                                  E.escreve(c, "3 cm", x0 - 140, y0 + 1.5 * u + 20, 56, "g", TINTA, a * (1 - real_h))))
    E.foco(c, t, c16, 0.4, lambda a: centro(c, "8 m", x0 + 2 * u, y0 + 3 * u + 70, 56, "g", E.COR, a))
    E.foco(c, t, d16, 0.4, lambda a: E.escreve(c, "6 m", x0 - 120, y0 + 1.5 * u + 20, 56, "g", E.COR, a))
    xr = 820

    def lados():
        pil(c, t, a16, "converta os lados, não a área", xr + 420, 260, 52)
        fesq(c, t, b16, "1 cm = 200 cm = 2 m", xr, 420, 76)
        fesq(c, t, c16, "4 cm → 8 m", xr, 550, 76)
        fesq(c, t, d16, "3 cm → 6 m", xr + 480, 550, 76)
        fesq(c, t, e16, "8 × 6 = 48 m²", xr, 720, 110, CERTO)
    E.saida(c, t, C["s17"] - 0.1, lados)
    if t < C["s17"] - 0.1:
        return
    E.frase(c, t, C["s17"] + 0.2, ps("pela escala", "i", 62) + [("ao quadrado:", "g", 62, COR)], xr, 280, "left", 0.1)
    fesq(c, t, a17, "papel: 4 × 3 = 12 cm²", xr, 400, 70)
    fesq(c, t, b17, "× 200² = × 40.000", xr, 510, 70)
    fesq(c, t, c17, "= 480.000 cm²", xr, 620, 70)
    fesq(c, t, d17, "= 48 m²", xr + 520, 620, 80, CERTO)
    fesq(c, t, e17, "12 × 200 = 2.400 cm² = 0,24 m²?", xr, 790, 58, ERRADO)
    E.frase(c, t, e17 + 0.8, ps("um apartamento do tamanho de", "i", 52, ERRADO) + [("um tapetinho", "g", 52, ERRADO)], xr, 880, "left", 0.08)
    tr = lerp(e17, C["s17.end"], 0.55)
    if t >= tr:
        E.risco(c, xr - 10, 805, xr + 1000, 745, t, tr, largura=10)


# ---------------- situação 5: volume na maquete ----------------
def b_questao5(c, t, C, b):
    k = lambda s: C["s18." + s]
    enunciado(c, t, C, 5, "volume na maquete", "s18", [
        (k("b"), ps("maquete", "i", 80) + [("1 : 20", "g", 80, COR)], 400),
        (k("c"), ps("reservatório guarda", "i", 80) + [("2 L", "g", 80, COR)], 540),
        (k("d"), ps("quantos", "i", 88) + [("m³ no real?", "g", 88, COR)], 800)], C["s19.a"])


def b_resposta5(c, t, C, b):
    a20, b20, c20 = C["s20.a"], C["s20.b"], C["s20.c"]
    a21, b21 = C["s21.a"], C["s21.b"]
    cab(c, t, C["s20"], 5, "volume na maquete")
    E.frase(c, t, C["s20"] + 0.4, ps("litro é volume, e", "i", 66) + [("não temos os lados", "g", 66)], W / 2, 250, "center", 0.1)
    pil(c, t, a20, "escala ao cubo", W / 2, 370, 60)
    fcen(c, t, b20, "20 × 20 × 20 = 20³ = 8.000", W / 2, 540, 96)
    fcen(c, t, c20, "2 L × 8.000 = 16.000 L", W / 2, 690, 96)
    fesq(c, t, lerp(C["s21"], a21, 0.5), "1 m³ = 1.000 L", XE, 870, 72, TINTA2)
    fesq(c, t, a21, "16.000 ÷ 1.000 =", 760, 870, 80)
    bola_res(c, t, a21 + 0.6, "16 m³", 1560, 850, 120, 66, CERTO)
    E.frase(c, t, b21, ps("volume real = volume da maquete", "i", 52, TINTA2) + [("× 8.000,", "g", 52, COR)] + ps("em qualquer unidade", "i", 52, TINTA2), W / 2, 1020, "center", 0.08)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s22"] + 0.2, [("resumindo", "i", 92, COR)], W / 2, 200, "center")
        itens = (("s22.a", "tudo na", "mesma unidade"), ("s22.b", "comprimento direto,", "área², volume³"),
                 ("s22.c", "confira se faz sentido", "no mundo real"))
        for i, (k, l1, l2) in enumerate(itens):
            y = 380 + i * 200
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 230, y - 30, 56, a=a), centro(c, str(i + 1), 230, y - 7, 64, "g", E.SOBRE, a)))
            E.frase(c, t, C[k] + 0.1, ps(l1, "i", 72) + [(l2, "g", 72, COR if i == 0 else TINTA)], 320, y, "left", 0.1)
    E.saida(c, t, C["s23"] - 0.1, resumo)
    if t < C["s23"]:
        return

    def trilha():
        E.frase(c, t, C["s23"] + 0.2, ps("trilha", "i", 84), W / 2, 420, "center")
        E.frase(c, t, C["s23"] + 0.6, [("razão e proporção", "g", 110, COR)], W / 2, 560, "center")
        E.foco(c, t, C["s23"] + 1.4, 0.5, lambda a: E.selo(c, W / 2, 720, 60, True, a))
        E.frase(c, t, C["s23"] + 1.6, ps("completa", "i", 84, CERTO), W / 2, 870, "center")
    E.saida(c, t, C["s23.a"] - 0.6, trilha)
    if t < C["s23.a"] - 0.6:
        return
    a0, b0, c0 = C["s23.a"], C["s23.b"], C["s23.c"]
    E.frase(c, t, a0 - 0.5, ps("na próxima aula, trilha nova", "i", 80), XE, 220, passo=0.12)
    E.frase(c, t, a0, [("porcentagem", "g", 130, COR)], XE, 380)
    E.frase(c, t, b0, [("25%", "g", 80, COR)] + ps("= 25 em cada 100", "b", 70), XE, 510, passo=0.1)
    E.foco(c, t, c0, 0.5, lambda a: E.formula(c, "25% = f{25}{100} = 0,25", XE, 670, 80, "g", TINTA, a))
    E.foco(c, t, C["s23.d"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1440, 760, 76, estilo="g", a=a, cor=E.SOBRE))
    p = ease_io(prog(t, C["s23.d"] + 0.3, 0.8))
    E.cursor(c, lerp(1770, 1570, p), lerp(970, 785, p), ep(t, C["s23.d"] + 0.2, 0.4))
    E.frase(c, t, C["s23.e"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 990, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, questao1=b_questao1, resposta1=b_resposta1, questao2=b_questao2,
              resposta2=b_resposta2, questao3=b_questao3, resposta3=b_resposta3, questao4=b_questao4, resposta4=b_resposta4,
              questao5=b_questao5, resposta5=b_resposta5, fim=b_fim)
