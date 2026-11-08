"""Visual — Estudativo · MAT-EQU-021: praticando sistemas de equações (quatro problemas de preço e quantidade).
Cada problema: enunciado com relógio de pausa, depois a resposta com a conta que a voz faz. Soma e subtração de equações
aparecem armadas em colunas (conta_sis). Peças locais: copo, pao, conta_sis, destaca."""
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Equações do 1º Grau")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-EQU-021_praticando_sistemas.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("questao1", "questao2", "questao3", "questao4", "fim"))
BR = "#FFFFFF"
# as contas da aula
assert 5 + 4 == 9 and 2 * 5 + 4 == 14 and 14 - 9 == 5
assert 3 * 30 == 90 and 90 + 2 * 30 == 150 and 150 / 5 == 30
assert 3 * 9 + 2 * 2 == 31 and 2 * 9 + 3 * 2 == 24 and 55 / 5 == 11 and 72 - 62 == 10 and 31 * 2 == 62 and 24 * 3 == 72
assert 50 * 8 == 400 and 520 - 400 == 120 and 120 / 4 == 30 and 30 * 12 + 20 * 8 == 520


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças desta aula ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def cen(c, t, t0, s, cx, y, size, cor=None, est="g"):
    E.foco(c, t, t0, 0.5, lambda a: centro(c, s, cx, y, size, est, cor or TINTA, a))


def fcen(c, t, t0, s, cx, y, size, cor=None):
    E.formula_em(c, t, t0, s, cx, y, size, "g", cor, "center")


def selo_em(c, t, t0, cx, cy, r, ok=True):
    E.foco(c, t, t0, 0.5, lambda a: E.selo(c, cx, cy, r * ease_back(prog(t, t0, 0.5)), ok, a), blur=0)


def destaca(c, s, sub, x, y, size, cor, a, n=0):
    """realce translúcido atrás de um trecho de uma linha escrita em x (borda), y (base)"""
    if a <= 0:
        return
    i0 = -1
    for _ in range(n + 1):
        i0 = s.find(sub, i0 + 1)
    ap = E.APERTO["g"] * size
    x0 = x + (E.larg(s[:i0], "g", size) + ap if i0 > 0 else 0)
    w = E.larg(sub, "g", size)
    M.rrect(c, x0 - size * 0.14, y - size * 0.92, w + size * 0.28, size * 1.2, size * 0.2, cor, 0.2 * a)


def conta_sis(c, t, cols, linhas, tl, op, top, res, y0, size, dy, marcas=()):
    """duas equações armadas em colunas, com o sinal da operação, a barra e o resultado. res = [(coluna, texto, t0[, cor])]"""
    n = len(linhas)
    ys = [y0 + i * dy for i in range(n)] + [y0 + n * dy + size * 0.2]
    for (li, ci, t0, cor) in marcas:
        q = ep(t, t0, 0.35)
        if q > 0:
            w = E.larg(linhas[li][ci] if li < n else next(r[1] for r in res if r[0] == ci), "g", size)
            M.rrect(c, cols[ci] - w / 2 - size * 0.16, ys[li] - size * 0.92, w + size * 0.32, size * 1.2, size * 0.2, cor, 0.22 * q)
    for i, (lin, ti) in enumerate(zip(linhas, tl)):
        for x, s in zip(cols, lin):
            if s:
                cen(c, t, ti, s, x, ys[i], size, TINTA)
    xo = cols[0] - size * 1.05
    cen(c, t, top, op, xo, ys[n - 1], size, COR)
    p = ep(t, top + 0.15, 0.5)
    if p > 0:
        yb = ys[n - 1] + size * 0.42
        M.line(c, xo - size * 0.4, yb, lerp(xo - size * 0.4, cols[-1] + size * 0.8, p), yb, TINTA, 1.0, 6)
    for r in res:
        cen(c, t, r[2], r[1], cols[r[0]], ys[n], size, r[3] if len(r) > 3 else TINTA)
    return ys


def copo(c, cx, cy, s, cor, a=1.0):
    """copo de suco com canudo"""
    if a <= 0:
        return
    p = skia.Path()
    p.moveTo(cx - s * 0.3, cy - s * 0.4); p.lineTo(cx + s * 0.3, cy - s * 0.4); p.lineTo(cx + s * 0.22, cy + s * 0.45); p.lineTo(cx - s * 0.22, cy + s * 0.45); p.close()
    c.drawPath(p, M.paint(cor, a))
    M.line(c, cx + s * 0.08, cy - s * 0.3, cx + s * 0.2, cy - s * 0.62, cor, a, max(4, s * 0.07))
    M.rrect(c, cx - s * 0.24, cy - s * 0.3, s * 0.48, s * 0.1, s * 0.05, BR, 0.5 * a)


def pao(c, cx, cy, s, cor, a=1.0):
    """pão de queijo: bolinha com pintas"""
    if a <= 0:
        return
    E.bola(c, cx, cy + s * 0.08, s * 0.38, cor, a)
    for dx, dy in ((-0.12, -0.05), (0.1, 0.0), (0.0, 0.18), (-0.15, 0.2), (0.17, 0.2)):
        c.drawCircle(cx + s * dx, cy + s * dy, s * 0.035, M.paint(BR, 0.55 * a))


def compra(c, t, t0, itens, x, y, s, gap, cor_pao=TINTA2):
    """fila de ícones: itens = "cp" (c = copo, p = pão); devolve o x depois do último"""
    for i, k in enumerate(itens):
        cx = x + i * gap
        E.foco(c, t, t0 + i * 0.12, 0.4, lambda a, k=k, cx=cx: (copo if k == "c" else pao)(c, cx, y, s, COR if k == "c" else cor_pao, a))
    return x + len(itens) * gap


def problema(c, t, t0, n, rot):
    E.foco(c, t, t0, 0.4, lambda a: E.pilula(c, f"problema {n}", XE + 150, 150, 52, estilo="g", a=a), sobe=8)
    E.frase(c, t, t0 + 0.3, ps(rot, "i", 64, TINTA2), XE + 340, 168, passo=0.08)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    ka, kb = C["s01.a"], C["s01.b"]
    E.frase(c, t, ka, [("4", "g", 220, COR)] + ps("problemas", "i", 130), XE, 360, passo=0.15)
    E.frase(c, t, ka + 0.8, ps("de preço e quantidade", "i", 84), XE, 480, passo=0.1)
    E.frase(c, t, ka + 2.2, ps("criados para esta aula, com preços inventados", "i", 52, TINTA2), XE, 560, passo=0.06)
    for i in range(4):
        E.foco(c, t, ka + 0.4 + i * 0.15, 0.5, lambda a, i=i: (E.bola(c, 1250 + i * 150, 330, 58, a=a),
                                                               centro(c, str(i + 1), 1250 + i * 150, 355, 70, "g", BR, a)))
    E.foco(c, t, kb, 0.5, lambda a: E.bola(c, XE + 70, 760, 70 * ease_back(prog(t, kb, 0.5)), a=a), blur=0)
    E.foco(c, t, kb + 0.1, 0.4, lambda a: [M.rrect(c, XE + 70 + dx - 11, 730, 22, 60, 6, BR, a) for dx in (-17, 17)])
    E.frase(c, t, kb + 0.2, [("pause", "g", 84, COR)] + ps("e resolva antes da resposta", "i", 84), XE + 170, 790, passo=0.12)
    E.frase(c, t, lerp(kb, C["s01.end"], 0.55), ps("errar aqui", "i", 70) + [("não custa nada", "g", 66, CERTO)] + ps("e ensina mais", "i", 70), XE + 170, 920, passo=0.1)


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s02"] + 0.2, ps("você tem", "i", 84), XE, 380)
    E.foco(c, t, C["s02.a"], 0.5, lambda a: E.escreve(c, "3", XE - 8, 690, 340, "g", COR, a))
    E.foco(c, t, C["s02.a"] + 0.15, 0.5, lambda a: E.escreve(c, "ferramentas", XE + 210, 670, 100, "i", TINTA, a))
    x, w = 960, 780
    itens = (("s02.b", "método da", "substituição"), ("s02.c", "método da", "adição"), ("s02.d", "o atalho de", "supor um tipo só"))
    for i, (k, l1, l2) in enumerate(itens):
        y = 150 + i * 240
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 196, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 62)], x + 44, y + 84)
        E.frase(c, t, C[k] + 0.3, [(l2, "g", 62, COR)], x + 44, y + 160)
    alvo = [(x + w - 30, 150 + i * 240 + 170) for i in range(3)]
    q1, q2 = ease_io(prog(t, C["s02.c"] - 0.35, 0.5)), ease_io(prog(t, C["s02.d"] - 0.35, 0.5))
    E.cursor(c, alvo[0][0], lerp(lerp(alvo[0][1], alvo[1][1], q1), alvo[2][1], q2), ep(t, C["s02.b"], 0.4))
    E.foco(c, t, C["s02.e"], 0.5, lambda a: E.pilula(c, "regra de ouro: confira nas duas", 540, 850, 50, estilo="g", fundo=CERTO, a=a), sobe=8)
    E.frase(c, t, lerp(C["s02.e"], C["s02.end"], 0.6), ps("travou? procure a aula no canal", "i", 56, TINTA2), XE, 980, passo=0.08)


# ---------------- problema 1 ----------------
def b_questao1(c, t, C, b):
    ka, kb, kc, kd = (C[f"s03.{k}"] for k in "abcd")
    problema(c, t, ka, 1, "na padaria")
    s, gap = 120, 150
    xe = compra(c, t, kb, "cp", XE + 80, 380, s, gap)
    E.frase(c, t, kb + 0.5, [("=", "g", 100), ("R$ 9", "g", 100, COR)], xe, 410, passo=0.12)
    E.frase(c, t, kb + 0.2, ps("1 suco + 1 pão de queijo", "i", 50, TINTA2), XE + 20, 500, passo=0.06)
    xe = compra(c, t, kc, "ccp", XE + 80, 650, s, gap)
    E.frase(c, t, kc + 0.6, [("=", "g", 100), ("R$ 14", "g", 100, COR)], xe, 680, passo=0.12)
    E.frase(c, t, kc + 0.2, ps("2 sucos + 1 pão de queijo", "i", 50, TINTA2), XE + 20, 770, passo=0.06)
    E.frase(c, t, kd, ps("quanto custa", "i", 84) + [("um suco?", "g", 84, COR)], XE, 930, passo=0.12)
    E.relogio(c, t, C["s04.a"])


def b_resposta1(c, t, C, b):
    ka, kb, kc, kd, ke, kf, kg = (C[f"s05.{k}"] for k in "abcdefg")

    def um():
        E.linha(c, t, [("x", "g", 84, COR, ka), ("= preço do suco", "i", 66, TINTA, ka + 0.3)], XE, 190)
        E.linha(c, t, [("y", "g", 84, COR, kb), ("= preço do pão de queijo", "i", 66, TINTA, kb + 0.3)], XE, 290)
        E.sistema(c, t, kc, ["x + y = 9", "2x + y = 14"], XE + 80, 500, 100, tl=(kc, kd))
        cols = (1180, 1300, 1420, 1540, 1670)
        conta_sis(c, t, cols, [["2x", "+", "y", "=", "14"], ["x", "+", "y", "=", "9"]], (ke, ke + 0.2), "−", ke + 0.4,
                  [(0, "x", kf, COR), (1, "+", kf), (2, "0", kf, COR), (3, "=", kf), (4, "5", kf, COR)], 470, 96, 140,
                  marcas=[(0, 2, ke + 0.6, COR), (1, 2, ke + 0.6, COR)])
        E.foco(c, t, lerp(kd, ke, 0.4), 0.4, lambda a: E.pilula(c, "o pão aparece 1 vez em cada", 1420, 300, 46, estilo="b", a=a), sobe=8)
        E.foco(c, t, kg, 0.5, lambda a: (E.bola(c, 640, 880, 90, CERTO, a), centro(c, "R$ 5", 640, 902, 56, "g", BR, a)))
        E.frase(c, t, kg + 0.2, ps("o", "i", 84) + [("suco", "g", 84, CERTO)] + ps("custa 5 reais", "i", 84), 760, 910, passo=0.12)
    E.saida(c, t, C["s06"] - 0.1, um)
    if t < C["s06"]:
        return
    a6, b6, c6, d6, e6 = (C[f"s06.{k}"] for k in "abcde")
    E.frase(c, t, C["s06"] + 0.1, ps("repare no", "i", 76) + [("atalho", "g", 76, COR)], XE, 160, passo=0.12)
    s, gap = 100, 125
    x0 = XE + 70
    xe = compra(c, t, C["s06"] + 0.3, "cp", x0, 310, s, gap)
    E.foco(c, t, C["s06"] + 0.6, 0.4, lambda a: E.escreve(c, "= R$ 9", xe, 340, 84, "g", TINTA, a))
    xe2 = compra(c, t, a6 - 0.3, "cpc", x0, 480, s, gap)
    E.foco(c, t, a6, 0.4, lambda a: E.escreve(c, "= R$ 14", xe2, 510, 84, "g", TINTA, a))
    E.foco(c, t, a6 + 0.3, 0.5, lambda a: (E.caixa_pontilhada(c, x0 + 2 * gap - 70, 410, 140, 150, a, COR),
                                           centro(c, "1 suco a mais", x0 + 2 * gap, 610, 46, "b", COR, a)))
    fcen(c, t, b6, "14 − 9 = 5", 1450, 400, 110, COR)
    E.foco(c, t, b6 + 0.4, 0.4, lambda a: centro(c, "a diferença é o suco", 1450, 480, 56, "i", TINTA2, a))
    E.foco(c, t, c6, 0.4, lambda a: E.pilula(c, "só quando as compras diferem num item só", W / 2, 700, 46, estilo="b", fundo=TINTA, a=a), sobe=8)
    fcen(c, t, d6, "pão: 9 − 5 = 4", 560, 870, 92)
    fcen(c, t, e6, "2 × 5 + 4 = 14", 1360, 870, 92)
    selo_em(c, t, e6 + 1.6, 840, 990, 46)
    E.frase(c, t, e6 + 1.7, [("bateu", "g", 64, CERTO)], 905, 1012)


# ---------------- problema 2 ----------------
def b_questao2(c, t, C, b):
    ka, kb, kc, kd = (C[f"s07.{k}"] for k in "abcd")
    problema(c, t, ka, 2, "na loja")
    E.frase(c, t, kb, [("calça", "g", 96, COR)] + ps("custa", "i", 84) + [("3 ×", "g", 96)] + ps("a camiseta", "i", 84), XE, 400, passo=0.12)
    E.frase(c, t, kc, [("1 calça + 2 camisetas", "g", 84)], XE, 580, passo=0.12)
    E.frase(c, t, kc + 0.8, [("=", "g", 96), ("R$ 150", "g", 96, COR)], XE, 700, passo=0.12)
    E.frase(c, t, kd, ps("quanto custa", "i", 84) + [("a calça?", "g", 84, COR)], XE, 900, passo=0.12)
    E.relogio(c, t, C["s08.a"])


def b_resposta2(c, t, C, b):
    ka, kb, kc, kd = (C[f"s09.{k}"] for k in "abcd")
    a10, b10, c10, d10, e10, f10 = (C[f"s10.{k}"] for k in "abcdef")
    E.linha(c, t, [("x", "g", 84, COR, ka), ("= calça", "i", 66, TINTA, ka + 0.3)], XE, 170)
    E.linha(c, t, [("y", "g", 84, COR, kb), ("= camiseta", "i", 66, TINTA, kb + 0.3)], XE + 420, 170)

    def conta():
        fcen(c, t, kc, "x = 3y", 560, 400, 120, COR)
        E.foco(c, t, lerp(kc, kd, 0.3), 0.4, lambda a: E.pilula(c, "calça sozinha: substituição", 560, 500, 46, estilo="b", a=a), sobe=8)
        tm = lerp(kc, kd, 0.62)
        s = "x + 2y = 150"
        w = E.formula(c, s, 0, 0, 100, a=0)
        destaca(c, s, "x", 1380 - w / 2, 400, 100, COR, ep(t, tm + 0.6, 0.4))
        fcen(c, t, tm, s, 1380, 400, 100)
        E.foco(c, t, tm + 0.6, 0.4, lambda a: centro(c, "troque a calça", 1380, 490, 52, "i", TINTA2, a))
        fcen(c, t, kd, "3y + 2y = 150", W / 2, 690, 110)
    E.saida(c, t, a10 - 0.1, conta)
    if t < a10 - 0.1:
        return
    fcen(c, t, a10, "5y = 150", 560, 370, 110)
    fcen(c, t, b10, "y = 30", 1360, 370, 110, COR)
    E.foco(c, t, b10 + 0.3, 0.4, lambda a: centro(c, "camiseta: R$ 30", 1360, 450, 52, "i", TINTA2, a))
    E.foco(c, t, c10, 0.4, lambda a: E.pilula(c, "a pergunta é a calça!", 560, 560, 52, estilo="g", fundo=ERRADO, a=a), sobe=8)
    E.foco(c, t, d10, 0.5, lambda a: (E.bola(c, 1450, 600, 110, CERTO, a), centro(c, "R$ 90", 1450, 625, 64, "g", BR, a)))
    fcen(c, t, d10 - 0.6, "x = 3 × 30", 1050, 620, 84)
    fcen(c, t, e10, "90 + 2 × 30 = 150", 560, 850, 92)
    fcen(c, t, f10, "90 = 3 × 30", 1360, 850, 92)
    selo_em(c, t, f10 + 0.8, 840, 980, 46)
    E.frase(c, t, f10 + 0.9, [("bateu", "g", 64, CERTO)] + ps("nas duas", "i", 64), 905, 1002, passo=0.1)


# ---------------- problema 3 ----------------
def b_questao3(c, t, C, b):
    ka, kb, kc, kd = (C[f"s11.{k}"] for k in "abcd")
    problema(c, t, ka, 3, "na papelaria")
    E.frase(c, t, kb, [("3 cadernos + 2 canetas", "g", 66)] + [("= R$ 31", "g", 66, COR)], XE, 400, passo=0.2)
    E.frase(c, t, kc, [("2 cadernos + 3 canetas", "g", 66)] + [("= R$ 24", "g", 66, COR)], XE, 560, passo=0.2)
    E.frase(c, t, kd, ps("quanto custam,", "i", 76) + [("juntos,", "i", 76)], XE, 780, passo=0.1)
    E.frase(c, t, kd + 1.0, [("1 caderno + 1 caneta?", "g", 84, COR)], XE, 900)
    E.relogio(c, t, C["s12.a"])


def b_resposta3(c, t, C, b):
    ka, kb, kc, kd = (C[f"s13.{k}"] for k in "abcd")
    cols = (560, 690, 820, 950, 1090)

    def soma():
        E.frase(c, t, C["s13"], ps("x = caderno · y = caneta", "i", 56, TINTA2), XE, 150, passo=0.06)
        E.foco(c, t, ka, 0.4, lambda a: E.pilula(c, "pergunta: x + y", 1500, 300, 60, estilo="g", a=a), sobe=8)
        ys = conta_sis(c, t, cols, [["3x", "+", "2y", "=", "31"], ["2x", "+", "3y", "=", "24"]], (C["s13"] + 0.3, C["s13"] + 0.5), "+", kb,
                       [(0, "5x", kc, COR), (1, "+", kc), (2, "5y", kc, COR), (3, "=", kc), (4, "55", kc, COR)], 360, 100, 150)
        E.ponte(c, t, kd - 0.6, 1200, 1380, ys[2] - 30, "÷ 5", None, 50)
        E.foco(c, t, kd, 0.5, lambda a: (E.bola(c, 1620, ys[2] - 30, 170, CERTO, a), E.formula(c, "x + y = 11", 1620, ys[2] + 2, 70, cor=BR, a=a, align="center")))
        E.frase(c, t, kd + 0.6, ps("caderno + caneta =", "i", 70) + [("R$ 11", "g", 72, CERTO)], W / 2, 980, "center", 0.1)
    E.saida(c, t, C["s14"] - 0.1, soma)
    if C["s14"] - 0.1 <= t:
        a14, b14, c14, d14 = (C[f"s14.{k}"] for k in "abcd")

        def cada():
            E.frase(c, t, C["s14"], ps("para conferir,", "i", 72) + [("ache cada preço", "g", 72, COR)], XE, 150, passo=0.1)
            sx, sy, sz = 230, 330, 88
            E.sistema(c, t, C["s14"] + 0.2, ["3x + 2y = 31", "2x + 3y = 24"], sx, sy, sz)
            y2 = sy + sz * 1.45
            E.ponte(c, t, a14, 780, 1020, sy - 30, "× 2", None, 48)
            E.ponte(c, t, a14 + 1.0, 780, 1020, y2 - 30, "× 3", None, 48)
            xn = 1080
            tq = lerp(a14, b14, 0.45)
            destaca(c, "6x + 4y = 62", "6x", xn, sy, sz, COR, ep(t, tq, 0.4))
            destaca(c, "6x + 9y = 72", "6x", xn, y2, sz, COR, ep(t, tq + 0.2, 0.4))
            E.formula_em(c, t, a14 + 0.4, "6x + 4y = 62", xn, sy, sz)
            E.formula_em(c, t, a14 + 1.4, "6x + 9y = 72", xn, y2, sz)
            E.foco(c, t, b14 - 0.8, 0.4, lambda a: E.pilula(c, "72 − 62: subtraia", W / 2, 610, 48, estilo="b", a=a), sobe=8)
            fcen(c, t, b14, "5y = 10", W / 2, 750, 110)
            fcen(c, t, c14, "y = 2", 560, 920, 110, COR)
            E.foco(c, t, c14 + 0.3, 0.4, lambda a: centro(c, "caneta", 560, 990, 48, "i", TINTA2, a))
            fcen(c, t, d14, "x = 11 − 2 = 9", 1300, 920, 110, COR)
            E.foco(c, t, d14 + 0.3, 0.4, lambda a: centro(c, "caderno", 1300, 990, 48, "i", TINTA2, a))
        E.saida(c, t, C["s15"] - 0.1, cada)
    if t < C["s15"]:
        return
    a15, b15, c15 = (C[f"s15.{k}"] for k in "abc")
    E.frase(c, t, C["s15"], [("conferindo", "i", 76, COR)], XE, 160)
    E.foco(c, t, C["s15"] + 0.2, 0.4, lambda a: (E.pilula(c, "x = 9", 1340, 135, 50, estilo="g", a=a), E.pilula(c, "y = 2", 1580, 135, 50, estilo="g", a=a)))
    fcen(c, t, a15, "3 × 9 + 2 × 2 = 27 + 4 = 31", W / 2, 380, 92)
    fcen(c, t, b15, "2 × 9 + 3 × 2 = 18 + 6 = 24", W / 2, 540, 92)
    selo_em(c, t, b15 + 1.8, 760, 670, 46)
    E.frase(c, t, b15 + 1.9, [("bateu", "g", 64, CERTO)] + ps("nas duas", "i", 64), 825, 692, passo=0.1)
    E.frase(c, t, c15, ps("com o atalho:", "i", 80) + [("x + y = 11", "g", 84, COR)] + ps("direto", "i", 80), W / 2, 900, "center", 0.12)


# ---------------- problema 4 ----------------
def b_questao4(c, t, C, b):
    ka, kb, kc, kd = (C[f"s16.{k}"] for k in "abcd")
    E.foco(c, t, ka, 0.4, lambda a: E.pilula(c, "último problema", XE + 180, 150, 52, estilo="g", a=a), sobe=8)
    E.frase(c, t, ka + 0.6, ps("junta tudo", "i", 64, TINTA2), XE + 430, 168)
    E.frase(c, t, kb, [("50", "g", 130, COR)] + ps("lanches", "i", 110), XE, 400, passo=0.14)
    E.frase(c, t, kb + 1.6, ps("uns de", "i", 76) + [("R$ 8", "g", 80, COR)] + ps("e outros de", "i", 76) + [("R$ 12", "g", 80, COR)], XE, 520, passo=0.12)
    E.frase(c, t, kc, ps("total", "i", 84) + [("R$ 520", "g", 100, COR)], XE, 700, passo=0.14)
    E.frase(c, t, kd, ps("quantos de", "i", 84) + [("R$ 12?", "g", 90, COR)], XE, 900, passo=0.12)
    E.relogio(c, t, C["s17.a"])


def b_resposta4(c, t, C, b):
    ka, kb, kc = (C[f"s18.{k}"] for k in "abc")

    def monta():
        E.frase(c, t, C["s18"] + 0.3, ps("x = lanches de R$ 8 · y = lanches de R$ 12", "i", 56, TINTA2), XE, 160, passo=0.05)
        E.sistema(c, t, ka, ["x + y = 50", "8x + 12y = 520"], XE + 80, 420, 110, tl=(ka, kb + 1.2))
        E.foco(c, t, ka + 0.3, 0.4, lambda a: E.pilula(c, "quantidades", 1360, 380, 52, estilo="b", a=a), sobe=8)
        E.foco(c, t, kb + 0.3, 0.4, lambda a: E.pilula(c, "dinheiro", 1360, 380 + 160, 52, estilo="b", fundo=TINTA, a=a), sobe=8)
        E.foco(c, t, kc, 0.4, lambda a: E.pilula(c, "total de coisas e só dois tipos: vale o atalho", W / 2, 820, 50, estilo="g", fundo=CERTO, a=a), sobe=8)
    E.saida(c, t, C["s19"] - 0.1, monta)
    if C["s19"] - 0.1 <= t:
        a19, b19, c19, d19, e19, f19 = (C[f"s19.{k}"] for k in "abcdef")

        def atalho():
            E.frase(c, t, C["s19"], ps("suponha", "i", 76) + [("todos de R$ 8", "g", 76, COR)], XE, 170, passo=0.12)
            fcen(c, t, b19, "50 × 8 = 400", 560, 370, 96)
            fcen(c, t, c19, "520 − 400 = 120", 1360, 370, 96)
            E.foco(c, t, c19 + 0.3, 0.4, lambda a: centro(c, "faltam R$ 120", 1360, 450, 52, "i", TINTA2, a))
            E.foco(c, t, d19, 0.4, lambda a: E.pilula(c, "trocar 8 por 12: +R$ 4", W / 2, 590, 52, estilo="b", a=a), sobe=8)
            fcen(c, t, e19, "120 ÷ 4 = 30", W / 2, 780, 110)
            E.foco(c, t, f19, 0.5, lambda a: (E.bola(c, 700, 930, 80, CERTO, a), centro(c, "30", 700, 955, 70, "g", BR, a)))
            E.frase(c, t, f19 + 0.2, ps("lanches de", "i", 80) + [("R$ 12", "g", 84, CERTO)], 810, 960, passo=0.12)
        E.saida(c, t, C["s20"] - 0.1, atalho)
    if t < C["s20"]:
        return
    a20, b20, c20, d20 = (C[f"s20.{k}"] for k in "abcd")
    E.foco(c, t, C["s20"], 0.4, lambda a: E.pilula(c, "30 de R$ 12", 330, 160, 52, estilo="g", a=a), sobe=8)
    fcen(c, t, C["s20"] + 0.6, "50 − 30 = 20", 560, 360, 100)
    E.foco(c, t, a20, 0.4, lambda a: centro(c, "20 lanches de R$ 8", 560, 450, 56, "g", COR, a))
    E.frase(c, t, b20 - 0.8, [("conferindo", "i", 72, COR)], 1100, 170)
    fcen(c, t, b20, "30 × 12 = 360", 1360, 360, 96)
    fcen(c, t, c20, "20 × 8 = 160", 1360, 560, 96)
    fcen(c, t, d20, "360 + 160 = 520", W / 2, 790, 120, COR)
    selo_em(c, t, d20 + 1.0, 800, 950, 56)
    E.frase(c, t, d20 + 1.1, [("bateu", "g", 72, CERTO)] + ps("nas duas", "i", 72), 880, 975, passo=0.1)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s21"], [("resumindo", "i", 92, COR)], W / 2, 210, "center")
        for i, (k, s) in enumerate((("s21.a", "quantidades e valores"), ("s21.b", "o caminho pelo formato"), ("s21.c", "confira nas duas"))):
            y = 390 + i * 190
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 360, y - 30, 56, a=a),
                                                         E.escreve(c, str(i + 1), 360 - E.larg(str(i + 1), "g", 64) / 2, y - 7, 64, "g", "#FFFFFF", a)))
            E.frase(c, t, C[k] + 0.1, [(s, "g", 96)], 460, y)
    E.saida(c, t, C["s22"] - 0.1, resumo)
    if t < C["s22"]:
        return
    E.frase(c, t, C["s22"] + 0.2, ps("você fecha a trilha de", "i", 84), XE, 330, passo=0.1)
    E.frase(c, t, C["s22.a"], [("Equações do", "g", 130, COR)], XE, 490)
    E.frase(c, t, C["s22.a"] + 0.4, [("1º grau", "g", 130, COR)], XE, 640)
    E.foco(c, t, C["s22.b"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1500, 400, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s22.b"] + 0.3, 0.8))
    E.cursor(c, lerp(1800, 1630, p), lerp(720, 425, p), ep(t, C["s22.b"] + 0.2, 0.4))
    E.frase(c, t, C["s22.c"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 900, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, questao1=b_questao1, resposta1=b_resposta1, questao2=b_questao2,
              resposta2=b_resposta2, questao3=b_questao3, resposta3=b_resposta3, questao4=b_questao4, resposta4=b_resposta4,
              fim=b_fim)
