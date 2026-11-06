"""Visual — Estudativo · MAT-NUM-009: dividir por um algarismo, com e sem resto.
Identidade em _ferramentas/editorial.py. As garrafas entram nas caixas e mostram o resto; a chave é E.conta_div na forma curta: sob o
dividendo, só o resto com o algarismo que desce. Peças locais: garrafa, nota (retângulo simples), desce (seta do algarismo) e resto.
Em s05 os nomes ficam fora da chave de propósito: o roteiro só apresenta a chave em s08."""
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco
import motor as M
import skia

E.usar("Matemática", "Números e Contas")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-NUM-009_dividir_por_um_algarismo.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("nomes", "chave", "zero", "atalho", "questao", "fim"))
BR = "#FFFFFF"


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


def bola_txt(c, t, t0, s, cx, cy, r, size, cor=CERTO):
    """o resultado na esfera"""
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r, cor, a), E.centro(c, s, cx, cy + size * 0.35, size, "g", M.on(cor), a)))


def lin(c, t, t0, s, x, y, size=64, estilo="b", cor=None):
    """uma linha do painel ao lado da conta"""
    E.foco(c, t, t0, 0.4, lambda a: E.escreve(c, s, x, y, size, estilo, cor or TINTA, a))


def igual(c, t, t0, t1, s1, s2, x, y, size=66, estilo="b", cor=None, cor2=None):
    """conta em duas partes: a pergunta em t0 e o resultado só em t1, quando a voz chega nele"""
    lin(c, t, t0, s1, x, y, size, estilo, cor)
    lin(c, t, t1, s2, x + E.larg(s1 + " ", estilo, size), y, size, estilo, cor2 or cor or COR)


def lista(c, t, C, ini, ta, n, itens):
    E.frase(c, t, C[ini] + 0.7, [("você", "i", 84), ("só", "i", 84), ("precisa", "i", 84), ("de", "i", 84)], XE, 410)
    E.foco(c, t, C[ta], 0.5, lambda a: E.escreve(c, str(n), XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C[ta] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 960, 780
    y0, dy = (280, 260) if len(itens) == 2 else (190, 240)
    for i, (k, l1, l2) in enumerate(itens):
        y = y0 + i * dy
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 196, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 62)], x + 44, y + 84)
        E.frase(c, t, C[k] + 0.3, [(l2, "g", 62, COR)], x + 44, y + 160)
    px = x + w - 30
    py = y0 + 170
    for i, (k, _, _) in enumerate(itens[1:], 1):
        py = lerp(py, y0 + i * dy + 170, ease_io(prog(t, C[k] - 0.35, 0.5)))
    E.cursor(c, px, py, ep(t, C[itens[0][0]], 0.4))


def resto(c, t, t0, x, y, size, linha, col, s):
    """o resto sozinho quando ele é zero: E.conta_div só escreve a linha com o algarismo que desce, e o 0 de "sobra zero" não entra nela.
    linha = linha de baixo (0 = a primeira), col = coluna do último algarismo"""
    cl, dy = E.casa(size), size * 1.12
    for m, ch in enumerate(s):
        i = col - (len(s) - 1 - m)
        E.foco(c, t, t0, 0.4, lambda a, ch=ch, i=i: E.centro(c, ch, x + (i + 0.5) * cl, y + (linha + 1) * dy, size, "g", TINTA, a))


def centros_q(Q, D, size):
    """centro de cada algarismo do quociente, a partir do que E.conta_div devolve"""
    q = D["quociente"]
    return E._centros(q, Q["xq"] + len(q) * E.larg("0", "g", size) * 1.1 + size * 0.17, size)


def desce(c, t, t0, x, y, size, col, linha):
    """seta curta: o algarismo do dividendo desce até a linha de baixo, e some"""
    dy = size * 1.12
    px = x + (col + 0.5) * E.casa(size)
    p = ep(t, t0, 0.4)
    a = p * (1 - ep(t, t0 + 1.0, 0.4))
    if a > 0:
        M.arrow(c, px + size * 0.46, y - size * 0.3, px + size * 0.46, y + (linha + 1) * dy - size * 0.3, COR, a, 5, 16, p)


def garrafa(c, x, y, w, h, a):
    """garrafa simples na cor da matéria: corpo e gargalo"""
    if a <= 0:
        return
    M.rrect(c, x + w * 0.33, y, w * 0.34, h * 0.3, 5, E.COR, a)
    M.rrect(c, x, y + h * 0.24, w, h * 0.76, w * 0.26, E.COR, a)


def nota(c, x, y, w, h, s, a, size=44):
    """nota simples na cor da matéria: retângulo com o valor, nunca cópia de cédula real"""
    if a <= 0:
        return
    M.rrect(c, x, y, w, h, 7, E.COR, a)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x + 5, y + 5, w - 10, h - 10), 3, 3), M.paint(E.SOBRE, 0.5 * a, stroke=2))
    E.centro(c, s, x + w / 2, y + h / 2 + size * 0.36, size, "g", E.SOBRE, a)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def tudo():
        ka, kb, kc, kd, ke = C["s01.a"], C["s01.b"], C["s01.c"], C["s01.d"], C["s01.e"]
        E.linha(c, t, [("R$ 612", "g", 120, COR, ka), ("para", "i", 110, TINTA, kb - 0.3), ("3 pessoas", "g", 120, TINTA, kb)], W / 2, 240, "center")
        E.linha(c, t, [("R$ 24", "g", 170, ERRADO, kc), ("para cada", "i", 130, TINTA, kc + 0.8)], W / 2, 470, "center")
        E.foco(c, t, kd, 0.5, lambda a: E.escreve(c, "3 × 24 =", 500, 680, 110, "g", TINTA, a))
        E.frase(c, t, lerp(kd, ke, 0.5), [("só", "i", 120), ("72", "g", 120, ERRADO)], 1000, 680, passo=0.25)
        E.frase(c, t, ke, [("faltou", "i", 120), ("um", "g", 110, COR), ("zero", "g", 110, COR)], W / 2, 900, "center", passo=0.2)
    E.saida(c, t, C["s02"] - 0.1, tudo)
    if t >= C["s02"]:
        ta, tb = C["s02.a"], C["s02.b"]
        E.foco(c, t, tb - 0.2, 0.7, lambda a: E.bola(c, 1500, 520, 270 * ease_back(prog(t, tb - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, [("até", "i", 90), ("o", "i", 90), ("fim", "i", 90), ("desta", "i", 90), ("aula", "i", 90)], XE, 340)
        E.frase(c, t, lerp(ta, tb, 0.33), [("dividir", "g", 120)], XE, 490)
        E.frase(c, t, lerp(ta, tb, 0.38), [("com", "i", 100), ("e", "i", 100), ("sem", "i", 100), ("resto", "g", 100, COR)], XE, 620, passo=0.2)
        E.frase(c, t, lerp(ta, tb, 0.6), [("tirar", "i", 92), ("a", "i", 92), ("prova", "g", 84), ("real", "g", 84)], XE, 780, passo=0.2)
        E.foco(c, t, tb + 0.2, 0.5, lambda a: (E.centro(c, "+ atalho", 1500, 505, 84, "g", E.SOBRE, a),
                                               E.centro(c, "de prova", 1500, 590, 84, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    lista(c, t, C, "s03", "s03.a", 3, (("s03.b", "a", "tabuada"), ("s03.c", "saber", "subtrair"), ("s03.d", "multiplicar", "por um algarismo")))


# ---------------- nomes e resto ----------------
GW, GH, GY = 52, 170, 372


def garrafas(c, t, C):
    """17 garrafas em fila; na fala das caixas, 15 entram em 3 caixas de 5 e 2 ficam de fora"""
    ka, kc = C["s04.a"], C["s04.c"]
    for i in range(17):
        x0 = XE + i * 92
        cx = i // 5
        x1 = XE + cx * 378 + 18 + (i % 5) * 64 if i < 15 else 1340 + (i - 15) * 74
        x = lerp(x0, x1, ease_io(prog(t, kc + i * 0.03, 0.8)))
        E.foco(c, t, ka + i * 0.05, 0.35, lambda a, x=x: garrafa(c, x, GY, GW, GH, a))
    q = ep(t, kc + 0.6, 0.5)
    if q > 0:
        for j in range(3):
            E.caixa_pontilhada(c, XE + j * 378, GY - 22, 348, GH + 44, q, TINTA, prog_=q)


def b_nomes(c, t, C, b):
    def fala4():
        ka, kb, kcc, kd = C["s04.a"], C["s04.b"], C["s04.c"], C["s04.d"]
        E.frase(c, t, C["s04"] + 0.1, [("dividir", "g", 76, COR), ("é", "i", 84), ("repartir", "i", 84), ("em", "i", 84), ("partes", "i", 84), ("iguais", "g", 76)], W / 2, 170, "center", passo=0.3)
        E.frase(c, t, lerp(C["s04"], ka, 0.42), [("ou", "i", 72), ("ver", "i", 72), ("quantas", "i", 72), ("vezes", "i", 72), ("um", "i", 72), ("número", "i", 72), ("cabe", "g", 64, COR), ("no", "i", 72), ("outro", "i", 72)], W / 2, 280, "center", passo=0.3)
        garrafas(c, t, C)
        lin(c, t, ka, "17 garrafas", XE, 700, 76, "g", COR)
        lin(c, t, kb, "caixas que levam 5", 900, 700, 76, "b")
        lin(c, t, kcc, "3 caixas, com 15 garrafas", XE, 830, 70, "b")
        lin(c, t, kd, "sobram 2", 1160, 830, 76, "g", COR)
    E.saida(c, t, C["s05"] - 0.1, fala4)

    def fala5():
        E.frase(c, t, C["s05"] + 0.1, [("cada", "i", 84), ("número", "i", 84), ("tem", "i", 84), ("um", "i", 84), ("nome", "g", 76, COR)], W / 2, 170, "center", passo=0.2)
        for i, (k, n, nome, oque) in enumerate((("s05.a", "17", "Dividendo", "o que vai ser dividido"), ("s05.b", "5", "Divisor", "o que divide"),
                                                ("s05.c", "3", "Quociente", "o resultado"), ("s05.d", "2", "Resto", "o que sobra"))):
            y = 320 + i * 135
            E.foco(c, t, C[k], 0.45, lambda a, n=n, y=y: E.centro(c, n, 320, y, 110, "g", COR, a))
            lin(c, t, C[k] + 0.1, nome, 450, y, 84, "g")
            lin(c, t, C[k] + 0.3, oque, 950, y, 76, "i", TINTA2)
        lin(c, t, C["s05.e"], "17 ÷ 5 = 3, com resto 2", 450, 910, 76, "g", COR)
    if t >= C["s05"]:
        E.saida(c, t, C["s06"] - 0.1, fala5)

    if t >= C["s06"]:
        ka, kb = C["s06.a"], C["s06.b"]
        E.frase(c, t, C["s06"] + 0.1, [("o", "i", 80), ("resto", "g", 72, COR), ("tem", "i", 80), ("uma", "i", 80), ("regra", "i", 80)], W / 2, 170, "center", passo=0.2)
        E.frase(c, t, ka, [("sempre", "i", 110), ("menor", "g", 110, COR), ("que", "i", 110), ("o", "i", 110), ("divisor", "g", 110)], W / 2, 350, "center", passo=0.25)
        t5 = lerp(ka, kb, 0.6)
        xc = W / 2 - 174
        for i in range(5):
            E.foco(c, t, t5 + i * 0.1, 0.35, lambda a, i=i: garrafa(c, xc + 18 + i * 64, 500, GW, GH, a))
        q = ep(t, kb, 0.5)
        if q > 0:
            E.caixa_pontilhada(c, xc, 478, 348, GH + 44, q, TINTA, prog_=q)
        E.frase(c, t, kb, [("daria", "i", 88), ("para", "i", 88), ("fechar", "i", 88), ("mais", "g", 80, COR), ("uma", "g", 80, COR), ("caixa", "g", 80, COR)], W / 2, 830, "center", passo=0.2)


# ---------------- prova real ----------------
def b_prova(c, t, C, b):
    ka, kb, kcc, kd = C["s07.a"], C["s07.b"], C["s07.c"], C["s07.d"]
    E.frase(c, t, ka, [("prova", "g", 170, COR), ("real", "g", 170, COR)], W / 2, 320, "center", passo=0.2)
    pp = lerp(kb, kcc, 0.3)
    E.linha(c, t, [("quociente × divisor", "g", 76, TINTA, kb), ("+ resto", "g", 76, COR, kb + 0.9), ("=", "g", 76, TINTA, pp), ("dividendo", "g", 76, TINTA, pp)], W / 2, 500, "center")
    igual(c, t, kcc, lerp(kcc, kd, 0.65), "3 × 5 =", "15", 620, 680, 100)
    igual(c, t, kd, lerp(kd, C["s07.end"], 0.25), "15 + 2 =", "17", 620, 810, 100)
    E.foco(c, t, lerp(kd, C["s07.end"], 0.45), 0.5, lambda a: E.selo(c, 1240, 760, 84, True, a))


# ---------------- conta na chave ----------------
D_78 = E.dividir("78", 3, 0)
D_612 = E.dividir("612", 3, 0)


def b_chave(c, t, C, b):
    ka, kb, kcc, kd = C["s08.a"], C["s08.b"], C["s08.c"], C["s08.d"]

    def esqueleto():
        xb, yt, ym = 900, 330, 560
        E.frase(c, t, C["s08"] + 0.1, [("com", "i", 84), ("número", "i", 84), ("maior", "g", 76, COR)], W / 2, 170, "center", passo=0.2)
        if t >= ka:
            p = ep(t, ka, 0.6)
            M.line(c, xb, yt, xb, ym, TINTA, 1.0, 9, progress=p)
            M.line(c, xb, ym, xb + 520, ym, TINTA, 1.0, 9, progress=p)
        E.frase(c, t, ka + 0.2, [("a", "i", 84), ("chave", "g", 76, COR)], xb + 110, 300)
        E.foco(c, t, kb, 0.45, lambda a: E.escreve(c, "dividendo", xb - E.larg("dividendo", "g", 96) - 50, 530, 96, "g", TINTA, a))
        E.foco(c, t, kcc, 0.45, lambda a: E.escreve(c, "divisor", xb + 50, 530, 96, "g", COR, a))
        E.foco(c, t, kd, 0.45, lambda a: E.escreve(c, "quociente", xb + 50, 670, 96, "g", TINTA, a))
    E.saida(c, t, C["s09"] - 0.1, esqueleto)
    if t < C["s09"]:
        return

    x, y, size = 210, 380, 120
    xp = 860
    a9, b9, c9 = C["s09.a"], C["s09.b"], C["s09.c"]
    d10 = {k: C["s10." + k] for k in "abcde"}
    d11 = {k: C["s11." + k] for k in "abcde"}
    E.linha(c, t, [("R$ 78", "g", 84, COR, a9), ("para", "i", 92, TINTA, a9 + 0.6), ("3 pessoas", "g", 84, TINTA, a9 + 0.8)], W / 2, 170, "center")
    E.conta_div(c, t, D_78, (lerp(b9, c9, 0.33), lerp(d11["a"], d11["b"], 0.6)), (d10["a"] + 0.2, d11["b"]), a9, x, y, size, ts=(c9,))
    desce(c, t, d10["a"], x, y, size, 1, 0)

    def fala9():
        igual(c, t, b9, lerp(b9, c9, 0.33), "7 ÷ 3 =", "2", xp, 340, 84)
        lin(c, t, lerp(b9, c9, 0.42), "porque 3 × 2 = 6", xp, 450, 70, "i", TINTA)
        lin(c, t, c9, "sobra 1", xp, 570, 84, "g", COR)
        E.frase(c, t, lerp(c9, C["s09.end"], 0.6), [("embaixo,", "i", 72), ("só", "i", 72), ("o", "i", 72), ("que", "i", 72), ("sobrou", "g", 64, COR)], xp, 720, passo=0.14)
    E.saida(c, t, C["s10"] - 0.1, fala9)

    def fala10():
        igual(c, t, d10["a"], lerp(d10["a"], d10["b"], 0.3), "desça o 8:", "18", xp, 310, 72)
        lin(c, t, d10["b"], "7 notas de R$ 10", xp, 420, 66)
        some = 1 - 0.75 * ep(t, d10["c"], 0.4)
        for i in range(7):
            E.foco(c, t, d10["b"] + i * 0.1, 0.35, lambda a, i=i: nota(c, xp + i * 124, 456, 112, 70, "10", a * (1 if i == 6 else some)))
        lin(c, t, d10["c"], "sobrou 1 nota", xp, 620, 66, "g", COR)
        lin(c, t, d10["d"], "vira 10 moedas de R$ 1", xp, 730, 66)
        lin(c, t, d10["e"], "mais 8 moedas: 18", xp, 840, 66, "g", COR)
        for i in range(18):
            E.foco(c, t, (d10["d"] + i * 0.06) if i < 10 else (d10["e"] + (i - 10) * 0.06), 0.3, lambda a, i=i: E.moeda(c, xp + 26 + i * 49, 910, 23, "", a, cor=E.COR if i < 10 else TINTA))
    if t >= C["s10"]:
        E.saida(c, t, C["s11"] - 0.1, fala10)

    if t >= C["s11"]:
        igual(c, t, d11["a"], lerp(d11["a"], d11["b"], 0.6), "18 ÷ 3 =", "6", xp, 340, 84)
        lin(c, t, d11["b"], "sobra 0", xp + 480, 340, 84, "g", CERTO)
        bola_txt(c, t, d11["c"], "R$ 26", xp + 130, 540, 124, 70)
        E.frase(c, t, d11["c"] + 0.4, [("para", "i", 76), ("cada", "i", 76), ("pessoa", "i", 76)], xp + 290, 565, passo=0.15)
        E.frase(c, t, d11["d"], [("exata:", "g", 72, COR), ("não", "i", 80), ("tem", "i", 80), ("resto", "i", 80)], xp, 750, passo=0.18)
        igual(c, t, d11["e"], lerp(d11["e"], C["s11.end"], 0.55), "3 × 26 =", "78", xp, 880, 84)


# ---------------- o zero no meio ----------------
def b_zero(c, t, C, b):
    x, y, size = 190, 340, 110
    xp = 1010
    a2, b2, c2, d2 = C["s12.a"], C["s12.b"], C["s12.c"], C["s12.d"]
    p = {k: C["s13." + k] for k in "abcdef"}
    t1 = lerp(c2, d2, 0.45)
    t12 = lerp(p["b"], p["c"], 0.4)
    t4 = lerp(p["c"], p["d"], 0.6)
    E.frase(c, t, a2, [("612", "g", 84, COR), ("÷", "g", 84), ("3", "g", 84)], W / 2, 170, "center", passo=0.16)
    Q = E.conta_div(c, t, D_612, (lerp(b2, c2, 0.6), p["a"] + 0.6, t4), (t1, t12, p["d"]), a2, x, y, size)
    resto(c, t, c2, x, y, size, 0, 0, "0")
    desce(c, t, t1, x, y, size, 1, 0)
    desce(c, t, p["b"], x, y, size, 2, 1)
    cen = centros_q(Q, D_612, size)
    if t >= p["a"] + 0.6:
        q = ep(t, p["a"] + 0.6, 0.3)
        E.caixa_pontilhada(c, cen[1] - 50, Q["y_q"] - 96, 100, 116, q, COR, prog_=q)

    def fala12():
        igual(c, t, b2, lerp(b2, c2, 0.6), "6 ÷ 3 =", "2", xp, 340, 80)
        lin(c, t, c2, "sobra 0", xp, 460, 80, "b", CERTO)
        lin(c, t, t1, "desça o 1", xp, 580, 72)
        lin(c, t, d2, "1 ÷ 3 não dá", xp, 700, 80, "b", ERRADO)
    E.saida(c, t, C["s13"] - 0.1, fala12)
    if t >= C["s13"]:
        E.frase(c, t, C["s13"] + 0.1, [("não", "g", 76, ERRADO), ("pule", "g", 76, ERRADO), ("essa", "i", 84), ("casa", "i", 84)], xp, 320, passo=0.14)
        lin(c, t, p["a"], "zero no quociente", xp, 430, 70, "g", COR)
        igual(c, t, p["b"], t12, "desça o 2:", "12", xp, 540, 70)
        igual(c, t, p["c"], t4, "12 ÷ 3 =", "4", xp, 650, 70)
        lin(c, t, p["d"], "sobra 0", xp + 480, 650, 70, "b", CERTO)
        bola_txt(c, t, p["e"], "204", xp + 110, 820, 112, 84)
        igual(c, t, p["f"], lerp(p["f"], C["s13.end"], 0.55), "3 × 204 =", "612", xp + 260, 845, 64)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    ka, kb, kcc, kd = C["s14.a"], C["s14.b"], C["s14.c"], C["s14.d"]
    x, y, wc, s = 170, 350, 220, 104
    E.frase(c, t, ka, [("pular", "g", 100, ERRADO), ("esse", "i", 110), ("zero", "g", 100, ERRADO)], W / 2, 180, "center", passo=0.16)
    E.quadro_casas(c, t, ("centena", "dezena", "unidade"), (ka, ka, ka), [[("2", ka + 0.2), ("0", ka + 0.2, COR), ("4", ka + 0.2)],
                   [("", 0), ("2", lerp(kb, kcc, 0.55), ERRADO), ("4", lerp(kb, kcc, 0.55), ERRADO)]], x, y, wc, s, 150, grossa=None)
    if t >= kb:
        q = ep(t, kb, 0.3)
        E.caixa_pontilhada(c, x + wc + 54, y + 14, 112, 118, q, COR, prog_=q)
    xp = 930
    E.frase(c, t, kb, [("nenhuma", "g", 72, COR), ("dezena", "g", 72, COR)], xp, 420, passo=0.16)
    E.frase(c, t, kb + 0.8, [("deu", "i", 80), ("para", "i", 80), ("repartir", "i", 80)], xp, 510, passo=0.16)
    E.frase(c, t, kcc - 0.6, [("o", "i", 90), ("200", "g", 90, ERRADO), ("vira", "i", 90), ("20", "g", 90, ERRADO)], xp, 650, passo=0.25)
    E.frase(c, t, kd, [("desceu", "g", 76, COR), ("um", "i", 84), ("algarismo,", "i", 84), ("escreva", "g", 76, COR), ("um", "i", 84), ("algarismo", "i", 84)], W / 2, 830, "center", passo=0.3)
    E.frase(c, t, lerp(kd, C["s14.end"], 0.72), [("nem", "i", 84), ("que", "i", 84), ("seja", "i", 84), ("zero", "g", 76, COR)], W / 2, 940, "center", passo=0.2)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def cinco():
        ka, kb, kcc, kd = C["s15.a"], C["s15.b"], C["s15.c"], C["s15.d"]
        E.frase(c, t, C["s15"] + 0.1, [("agora,", "i", 76, CLARO), ("o", "i", 76, CLARO), ("atalho:", "i", 76, CLARO)], W / 2, 170, "center", passo=0.1)
        E.frase(c, t, ka, [("vezes", "i", 120, CLARO), ("5", "g", 130, BR)], W / 2, 320, "center", passo=0.2)
        E.frase(c, t, ka + 0.7, [("é", "i", 96, CLARO), ("vezes", "i", 96, CLARO), ("10,", "g", 100, BR), ("dividido", "i", 96, CLARO), ("por", "i", 96, CLARO), ("2", "g", 100, BR)], W / 2, 460, "center", passo=0.25)
        y = 720
        E.foco(c, t, kb, 0.5, lambda a: E.centro(c, "46 × 5", 300, y + 34, 100, "g", BR, a))
        E.ponte(c, t, kcc, 510, 770, y, "× 10", CLARO, 60)
        E.foco(c, t, kcc + 0.9, 0.5, lambda a: E.centro(c, "460", 930, y + 40, 110, "g", BR, a))
        E.ponte(c, t, kd, 1090, 1350, y, "÷ 2", CLARO, 60)
        E.foco(c, t, lerp(kd, C["s15.end"], 0.5), 0.5, lambda a: E.centro(c, "230", 1530, y + 50, 150, "g", CLARO, a))
    E.saida(c, t, C["s16"] - 0.1, cinco)
    if t >= C["s16"]:
        ka, kb = C["s16.a"], C["s16.b"]
        E.frase(c, t, ka, [("5", "g", 170, CLARO), ("é", "i", 150, BR), ("a", "i", 150, BR), ("metade", "g", 130, BR), ("de", "i", 150, BR), ("10", "g", 170, CLARO)], W / 2, 340, "center", passo=0.2)
        E.frase(c, t, lerp(ka, kb, 0.55), [("só", "i", 84, CLARO), ("vale", "i", 84, CLARO), ("para", "i", 84, CLARO), ("vezes", "i", 84, CLARO), ("5", "g", 84, BR)], W / 2, 510, "center", passo=0.2)
        E.foco(c, t, kb, 0.5, lambda a: E.selo(c, 300, 700, 72, False, a))
        E.frase(c, t, kb + 0.1, [("não", "i", 80, CLARO), ("compensa", "i", 80, CLARO), ("se", "i", 80, CLARO), ("a", "i", 80, CLARO), ("metade", "g", 72, BR), ("não", "i", 80, CLARO), ("sai", "i", 80, CLARO), ("de", "i", 80, CLARO), ("cabeça", "g", 72, BR)], 410, 725, passo=0.15)
        E.frase(c, t, kb + 2.3, [("aí,", "i", 84, CLARO), ("arme", "g", 76, BR), ("a", "g", 76, BR), ("conta", "g", 76, BR)], 410, 850, passo=0.12)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s17"] + 0.1, [("hora", "i", 72, COR), ("de", "i", 72, COR), ("testar", "i", 72, COR)], XE, 200)
    E.frase(c, t, C["s17.a"] - 0.8, [("a", "i", 92), ("padaria", "i", 92), ("assou", "i", 92)], XE, 340, passo=0.25)
    E.frase(c, t, C["s17.a"], [("423", "g", 104, COR), ("pães", "g", 92)], XE, 470, passo=0.3)
    E.frase(c, t, C["s17.b"], [("4", "g", 104, COR), ("pães", "g", 92), ("em", "i", 92), ("cada", "i", 92), ("saco", "i", 92)], XE, 600, passo=0.2)
    E.frase(c, t, C["s17.c"], [("quantos", "i", 92), ("sacos", "g", 84, COR), ("cheios?", "g", 84, COR)], XE, 770, passo=0.22)
    E.frase(c, t, lerp(C["s17.c"], C["s17.end"], 0.5), [("quantos", "i", 92), ("pães", "g", 84, COR), ("sobram?", "g", 84, COR)], XE, 880, passo=0.22)
    E.relogio(c, t, C["s18.a"], 1490, 400, 200)


# ---------------- resposta ----------------
D_423 = E.dividir("423", 4, 0)


def b_resposta(c, t, C, b):
    x, y, size = 190, 340, 110
    xp = 1010
    a9, b9, c9, d9 = C["s19.a"], C["s19.b"], C["s19.c"], C["s19.d"]
    p = {k: C["s20." + k] for k in "abcdefg"}
    t2 = lerp(b9, c9, 0.45)
    t5 = lerp(p["b"], p["c"], 0.6)
    E.frase(c, t, C["s19"] + 0.1, [("423", "g", 84, COR), ("÷", "g", 84), ("4", "g", 84)], W / 2, 170, "center", passo=0.16)
    Q = E.conta_div(c, t, D_423, (lerp(a9, b9, 0.6), d9 + 0.6, t5), (t2, p["a"] + 0.5, p["c"]), C["s19"] + 0.1, x, y, size)
    resto(c, t, b9, x, y, size, 0, 0, "0")
    desce(c, t, t2, x, y, size, 1, 0)
    desce(c, t, p["a"], x, y, size, 2, 1)
    cen = centros_q(Q, D_423, size)
    if t >= d9 + 0.6:
        q = ep(t, d9 + 0.6, 0.3)
        E.caixa_pontilhada(c, cen[1] - 50, Q["y_q"] - 96, 100, 116, q, COR, prog_=q)

    def fala19():
        igual(c, t, a9, lerp(a9, b9, 0.6), "4 ÷ 4 =", "1", xp, 340, 80)
        lin(c, t, b9, "sobra 0", xp, 460, 80, "b", CERTO)
        lin(c, t, t2, "desça o 2", xp, 580, 72)
        lin(c, t, c9, "2 ÷ 4 não dá", xp, 690, 80, "b", ERRADO)
        lin(c, t, d9, "zero no quociente", xp, 810, 70, "g", COR)
    E.saida(c, t, C["s20"] - 0.1, fala19)
    if t >= C["s20"]:
        igual(c, t, p["a"], p["a"] + 0.5, "desça o 3:", "23", xp, 330, 72)
        igual(c, t, p["b"], t5, "23 ÷ 4 =", "5", xp, 440, 72)
        lin(c, t, p["c"], "sobram 3", xp + 480, 440, 72, "b", COR)
        bola_txt(c, t, p["d"], "105", xp + 110, 610, 112, 84)
        E.frase(c, t, p["d"] + 0.3, [("sacos", "i", 76), ("cheios", "i", 76)], xp + 260, 600, passo=0.15)
        E.frase(c, t, p["e"], [("sobram", "i", 76), ("3", "g", 76, COR), ("pães", "i", 76)], xp + 260, 680, passo=0.15)
        igual(c, t, p["f"], lerp(p["f"], p["g"], 0.6), "4 × 105 =", "420", xp, 810, 72)
        igual(c, t, p["g"], lerp(p["g"], C["s20.end"], 0.6), "420 + 3 =", "423", xp, 910, 72)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s21"], [("resumindo", "i", 92, COR)], W / 2, 210, "center")
        for i, (k, s) in enumerate((("s21.a", "comece pela esquerda"), ("s21.b", "desça um algarismo de cada vez"), ("s21.c", "não pule o zero"))):
            y = 390 + i * 190
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 260, y - 24, 56, a=a),
                                                         E.centro(c, str(i + 1), 260, y - 1, 64, "g", E.SOBRE, a)))
            E.frase(c, t, C[k] + 0.1, [(s, "g", 74)], 350, y)
    E.saida(c, t, C["s22"] - 0.1, resumo)
    if t < C["s22"]:
        return
    E.frase(c, t, lerp(C["s22"], C["s22.a"], 0.75), [("próxima", "i", 84), ("aula", "i", 84)], XE, 280)
    E.frase(c, t, C["s22.a"], [("divisor", "g", 140, COR), ("de", "i", 130), ("dois", "g", 140, COR)], XE, 430, passo=0.2)
    E.frase(c, t, C["s22.a"] + 0.6, [("algarismos", "g", 140, COR)], XE, 570)
    E.frase(c, t, C["s22.b"], [("estimar", "g", 76), ("cada", "i", 84), ("algarismo", "i", 84), ("do", "i", 84), ("resultado", "i", 84)], XE, 690, passo=0.15)
    E.foco(c, t, C["s22.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1440, 790, 76, estilo="g", a=a, cor=E.SOBRE))
    p = ease_io(prog(t, C["s22.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1770, 1570, p), lerp(1000, 815, p), ep(t, C["s22.c"] + 0.2, 0.4))
    E.frase(c, t, C["s22.d"], [("bons", "i", 120), ("estudos!", "i", 120, COR)], XE, 900)


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, nomes=b_nomes, prova=b_prova, chave=b_chave, zero=b_zero, erro=b_erro, atalho=b_atalho,
              questao=b_questao, resposta=b_resposta, fim=b_fim)
