"""Visual — Estudativo · MAT-CNT-017: sorteios sucessivos com e sem reposição.
Mesma linguagem da trilha Contagem e Probabilidade (MAT-CNT-001 a 016): igual_bola() com o resultado na esfera, E.bola nas cores da
urna da MAT-CNT-011 (azul e vermelha), linha() com contas e frações numa linha (MAT-CNT-013), E.pontes com "− 1".
Peças desta aula:
- urna(): pote de vidro visto de frente; bolas_urna() as bolas dentro, cada uma podendo sair para fora da urna e voltar
  (com reposição a bola volta; sem reposição ela fica de lado, no prato "fora").
- lampada(): lâmpada boa (acesa) ou queimada, para a questão.
Sem voz ainda: todo instante vem de C[...] (cenas e marcadores), nunca de segundos fixos."""
import math
from fractions import Fraction as Fr
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Contagem e Probabilidade")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-CNT-017_com_sem_reposicao.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("com", "sem", "regra", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
AZUL, VERM = "#3D7DD8", "#D94B3D"
AMARELO = "#FFC93C"
URNA = [AZUL, AZUL, AZUL, VERM, VERM]
assert Fr(3, 5) * Fr(3, 5) == Fr(9, 25) and Fr(9, 25) * 100 == 36 and Fr(3, 5) * Fr(2, 4) == Fr(6, 20) == Fr(3, 10) and Fr(3, 10) * 100 == 30
assert Fr(2, 5) * Fr(2, 5) == Fr(4, 25) and Fr(4, 25) * 100 == 16 and Fr(2, 5) * Fr(1, 4) == Fr(2, 20) == Fr(1, 10)
assert Fr(3, 5) * Fr(3, 4) == Fr(9, 20) and 3 * 2 * 1 == 6 and 5 * 4 * 3 == 60 and Fr(6, 60) == Fr(1, 10) == Fr(3, 5) * Fr(2, 4) * Fr(1, 3)
assert Fr(7, 10) ** 2 == Fr(49, 100) and Fr(7, 10) * Fr(6, 9) == Fr(42, 90) == Fr(7, 15) and 46 < 700 / 15 < 47


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças da trilha (MAT-CNT-002 a 016) ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    """uma frase, palavra a palavra, no mesmo estilo"""
    return [(w, est, size, cor) for w in txt.split()]


def igual_bola(c, t, t0, x, y, txt, r=120, size=None, cor=None, escuro=False, t_igual=None):
    """'=' em x e o resultado numa esfera à direita; y = centro. Devolve o centro da esfera."""
    size = size or r * (0.72 if len(txt) <= 2 else 0.56 if len(txt) == 3 else 0.46 if len(txt) == 4 else 0.38)
    E.sinal(c, t, t0 - 0.2 if t_igual is None else t_igual, "=", x, y, r * 0.75, BR if escuro else TINTA)
    bx = x + r * 0.55 + r
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, bx, y, r, cor, a), centro(c, txt, bx, y + size * 0.36, size, "g", E.SOBRE, a)))
    return bx


def nota(c, t, t0, x, y, txt, size=46, cor=TINTA2, estilo="b"):
    E.foco(c, t, t0, 0.45, lambda a: centro(c, txt, x, y, size, estilo, cor, a))


def larg_parte(p, size):
    return E.larg(p, "g", size) if isinstance(p, str) else max(E.larg(str(p[0]), "g", size), E.larg(str(p[1]), "g", size)) + size * 0.2


def linha(c, t, x, y, size, partes, align="left", gap=None):
    """conta numa linha: partes = [(texto ou (n, d), instante[, cor])]; y = altura da barra das frações. Devolve o x de cada parte e o fim"""
    gap = size * 0.28 if gap is None else gap
    ws = [larg_parte(p[0], size) for p in partes]
    tot = sum(ws) + gap * (len(partes) - 1)
    xx = x - tot / 2 if align == "center" else x - tot if align == "right" else x
    xs = []
    for (p, t0, *cor), w in zip(partes, ws):
        cor = cor[0] if cor else TINTA
        xs.append(xx)
        if isinstance(p, str):
            E.foco(c, t, t0, 0.45, lambda a, p=p, xx=xx, cor=cor: E.escreve(c, p, xx, y + size * 0.34, size, "g", cor, a))
        else:
            E.fr(c, t, t0, p[0], p[1], xx + w / 2, y, size, cor)
        xx += w + gap
    return xs, xx - gap


def pil_esq(c, t, t0, x, y, txt, size=46, fundo=None, cor=BR):
    """pílula com a borda esquerda em x"""
    w = E.larg(txt, "g", size) + size * 1.1
    E.foco(c, t, t0, 0.45, lambda a: E.pilula(c, txt, x + w / 2, y, size, estilo="g", fundo=fundo or TINTA2, cor=cor, a=a))


def fracao_partes(c, t, cx, y, size, cima, baixo, tcima, tbaixo, cor=None):
    """fração cujo de cima e o de baixo entram em instantes diferentes; y = barra (MAT-CNT-016)"""
    w = max(E.larg(cima, "g", size), E.larg(baixo, "g", size)) + size * 0.3
    E.foco(c, t, min(tcima, tbaixo), 0.45, lambda a: c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2, y - size * 0.045, w, size * 0.09), 4, 4),
                                                                 M.paint(cor or TINTA, a)))
    E.foco(c, t, tcima, 0.45, lambda a: centro(c, cima, cx, y - size * 0.2, size, "g", cor or TINTA, a))
    E.foco(c, t, tbaixo, 0.45, lambda a: centro(c, baixo, cx, y + size * 0.9, size, "g", cor or TINTA, a))
    return w


# ---------------- peças desta aula: a urna ----------------
def urna(c, cx, cy, w, h, a=1.0, escuro=False):
    """pote de vidro visto de frente; (cx, cy) = centro do corpo"""
    if a <= 0:
        return
    pa = skia.Path()
    gw = w * 0.56
    top = cy - h / 2
    pa.moveTo(cx - gw / 2, top)
    pa.lineTo(cx - gw / 2, top + h * 0.1)
    pa.cubicTo(cx - w / 2, top + h * 0.14, cx - w / 2, top + h * 0.2, cx - w / 2, top + h * 0.3)
    pa.lineTo(cx - w / 2, cy + h / 2 - w * 0.16)
    pa.quadTo(cx - w / 2, cy + h / 2, cx - w / 2 + w * 0.16, cy + h / 2)
    pa.lineTo(cx + w / 2 - w * 0.16, cy + h / 2)
    pa.quadTo(cx + w / 2, cy + h / 2, cx + w / 2, cy + h / 2 - w * 0.16)
    pa.lineTo(cx + w / 2, top + h * 0.3)
    pa.cubicTo(cx + w / 2, top + h * 0.2, cx + w / 2, top + h * 0.14, cx + gw / 2, top + h * 0.1)
    pa.lineTo(cx + gw / 2, top)
    c.drawPath(pa, M.paint(BR, (0.1 if escuro else 0.55) * a))
    c.drawPath(pa, M.paint(CLARO if escuro else TINTA2, a, stroke=6))
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - gw / 2 - 12, top - 14, gw + 24, 22), 10, 10), M.paint(CLARO if escuro else TINTA2, a))


def vagas(cx, cy, w, h, n):
    """lugares das bolas dentro da urna, de baixo para cima"""
    r = w * 0.13
    base = cy + h / 2 - r * 1.35
    out = []
    for k in range(n):
        lin, col = (k // 3, k % 3)
        nl = min(3, n - lin * 3)
        x = cx + (col - (nl - 1) / 2) * r * 2.25
        out.append((x, base - lin * r * 2.1))
    return out, r


def bolas_urna(c, t, t0, cx, cy, w, h, cores=URNA, mov=None, apaga=None):
    """as bolas da urna. mov = {índice: [(instante, (x, y) ou None = de volta ao lugar)]}; apaga = índice → alfa. Devolve as posições"""
    pos, r = vagas(cx, cy, w, h, len(cores))
    agora = []
    for i, cor in enumerate(cores):
        x, y = pos[i]
        for ti, alvo in (mov or {}).get(i, []):
            if t >= ti:
                q = ease_io(prog(t, ti, 0.7))
                ax, ay = alvo if alvo is not None else pos[i]
                x, y = lerp(x, ax, q), lerp(y, ay, q) - math.sin(math.pi * q) * 80
        al = apaga(i) if apaga else 1.0
        E.foco(c, t, t0 + 0.06 * i, 0.4, lambda a, x=x, y=y, cor=cor, al=al: E.bola(c, x, y, r, cor, a * al), sobe=8)
        agora.append((x, y))
    return agora, r


def prato(c, cx, cy, w, a=1.0, rotulo="fora", escuro=False):
    """o lugar onde a bola que saiu fica de lado"""
    if a <= 0:
        return
    p = M.paint(CLARO if escuro else TINTA2, a, stroke=4)
    p.setPathEffect(skia.DashPathEffect.Make([10, 8], 0))
    c.drawRoundRect(skia.Rect.MakeXYWH(cx - w / 2, cy - w * 0.32, w, w * 0.64), 24, 24, p)
    centro(c, rotulo, cx, cy + w * 0.32 + 50, 42, "i", CLARO if escuro else TINTA2, a)


def lampada(c, cx, cy, s, boa=True, a=1.0):
    """lâmpada de altura ~s: boa = amarela e acesa; queimada = cinza com o filamento partido"""
    if a <= 0:
        return
    r = s * 0.3
    if boa:
        g = skia.Paint(AntiAlias=True)
        g.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy - s * 0.12), r * 1.9, [M.hexc(AMARELO, 0.45 * a), M.hexc(AMARELO, 0)], [0, 1]))
        c.drawCircle(cx, cy - s * 0.12, r * 1.9, g)
    vidro = AMARELO if boa else "#B9B9C0"
    c.drawCircle(cx, cy - s * 0.12, r, M.paint(vidro, a))
    c.drawRect(skia.Rect.MakeXYWH(cx - r * 0.5, cy + s * 0.08, r, s * 0.1), M.paint(vidro, a))
    for k in range(3):
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - r * 0.55, cy + s * 0.18 + k * s * 0.07, r * 1.1, s * 0.055), 4, 4), M.paint(TINTA2, a))
    if not boa:
        M.line(c, cx - r * 0.4, cy - s * 0.12, cx - r * 0.05, cy - s * 0.2, TINTA2, a, 4)
        M.line(c, cx + r * 0.05, cy - s * 0.06, cx + r * 0.4, cy - s * 0.12, TINTA2, a, 4)


# ---------------- gancho ----------------
UX, UY, UW, UH = 430, 600, 420, 460


def b_gancho(c, t, C, b):
    def pergunta():
        E.foco(c, t, C["s01.a"], 0.5, lambda a: urna(c, UX, UY, UW, UH, a))
        pos, r = bolas_urna(c, t, C["s01.a"] + 0.2, UX, UY, UW, UH,
                            mov={0: [(C["s01.b"] + 0.2, (UX + 380, 330))], 1: [(C["s01.b"] + 0.5, (UX + 500, 330))]})
        E.frase(c, t, C["s01.a"] + 0.3, [("3", "g", 80, AZUL), ("azuis", "i", 72), ("e", "i", 72), ("2", "g", 80, VERM), ("vermelhas", "i", 72)], 960, 200, passo=0.12)
        E.frase(c, t, C["s01.b"], [("tire", "i", 72), ("2", "g", 80, COR), ("bolas:", "i", 72), ("ambas", "i", 72), ("azuis?", "g", 80, AZUL)], 960, 470, passo=0.12)
        E.foco(c, t, C["s01.c"], 0.5, lambda a: E.pilula(c, "a 1ª volta antes da 2ª?", 1380, 620, 52, estilo="g", a=a))
        E.foco(c, t, C["s01.d"] - 0.4, 0.45, lambda a: E.escreve(c, "volta:", 960, 830, 64, "i", TINTA, a))
        E.foco(c, t, C["s01.d"], 0.5, lambda a: E.escreve(c, "36%", 1160, 835, 90, "g", COR, a))
        E.foco(c, t, C["s01.e"] - 0.4, 0.45, lambda a: E.escreve(c, "não volta:", 960, 960, 64, "i", TINTA, a))
        E.foco(c, t, C["s01.e"], 0.5, lambda a: E.escreve(c, "30%", 1270, 965, 90, "g", COR, a))
    E.saida(c, t, C["s02"] - 0.1, pergunta)

    if t >= C["s02"]:
        E.foco(c, t, C["s02.b"] - 0.2, 0.7, lambda a: E.bola(c, 1480, 520, 300 * ease_back(prog(t, C["s02.b"] - 0.2, 0.7))), blur=0)
        E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 96), XE, 300)
        E.frase(c, t, C["s02.a"] + 0.9, [("sorteios", "g", 116, COR)], XE, 450)
        E.frase(c, t, C["s02.a"] + 1.3, [("em", "i", 100), ("sequência", "g", 116)], XE, 600)
        pil_esq(c, t, C["s02.a"] + 2.6, XE, 760, "devolvendo ou não", 50)
        E.foco(c, t, C["s02.b"] + 0.2, 0.5, lambda a: (E.centro(c, "+ atalho", 1480, 490, 88, "g", BR, a),
                                                      E.centro(c, "de prova", 1480, 600, 88, "g", BR, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"] + 0.1, [("você", "i", 84), ("vai", "i", 84), ("usar", "i", 84), ("duas", "g", 88, COR), ("coisas", "i", 84)], W / 2, 190, "center")
    for k, x, titulo in (("s03.b", 200, "independentes"), ("s03.c", 1000, "condicional")):
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, 290, 720, 620, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(titulo, "g", 64, COR)], x + 360, 400, "center")
    E.foco(c, t, C["s03.b"] + 0.5, 0.45, lambda a: E.centro(c, "multiplique as chances", 560, 580, 52, "i", TINTA2, a))
    E.foco(c, t, C["s03.b"] + 1.0, 0.45, lambda a: E.centro(c, "P(A e B) =", 560, 710, 64, "g", TINTA, a))
    E.foco(c, t, C["s03.b"] + 1.3, 0.45, lambda a: E.centro(c, "P(A) × P(B)", 560, 800, 64, "g", COR, a))
    E.foco(c, t, C["s03.c"] + 0.5, 0.45, lambda a: E.pilula(c, "a pista vira", 1360, 620, 56, estilo="g", a=a))
    E.foco(c, t, C["s03.c"] + 0.8, 0.45, lambda a: E.pilula(c, "o novo total", 1360, 730, 56, estilo="g", a=a))
    E.frase(c, t, lerp(C["s03.c"], C["s03.end"], 0.8), ps("faltou alguma? procure no canal", "i", 52, TINTA2), W / 2, 1010, "center", passo=0.1)


# ---------------- com reposição ----------------
CX_U, CY_U = 380, 640
XP = 800


def b_com(c, t, C, b):
    E.frase(c, t, C["s04.a"], [("com", "g", 84, COR), ("reposição", "g", 84, COR)], W / 2, 170, "center", passo=0.15)
    E.foco(c, t, C["s04.b"], 0.45, lambda a: E.centro(c, "repor = devolver a bola antes do próximo sorteio", W / 2, 260, 48, "i", TINTA2, a))
    E.foco(c, t, C["s04"] + 0.3, 0.5, lambda a: urna(c, CX_U, CY_U, 400, 440, a))
    dim = (lambda i: 1.0 if URNA[i] == AZUL else 0.35) if t >= C["s04.c"] else None
    bolas_urna(c, t, C["s04"] + 0.5, CX_U, CY_U, 400, 440, mov={0: [(C["s04.d"] + 0.6, (CX_U + 320, 380)), (C["s05.a"], None)]}, apaga=dim)
    linha(c, t, XP, 430, 100, [("1ª:", C["s04.c"] - 0.2), ((3, 5), C["s04.d"], AZUL)])
    nota(c, t, C["s05.a"] + 0.3, CX_U, 920, "a urna fica igual", 48, COR)
    linha(c, t, XP + 400, 430, 100, [("2ª:", C["s05.b"] - 0.2), ((3, 5), C["s05.b"], AZUL)])
    E.foco(c, t, C["s05.c"], 0.5, lambda a: E.pilula(c, "independentes", XP + 470, 620, 50, estilo="g", a=a))
    y = 830
    xs, xf = linha(c, t, XP, y, 100, [((3, 5), C["s05.d"]), ("×", C["s05.d"] + 0.3), ((3, 5), C["s05.d"] + 0.5), ("=", C["s05.d"] + 1.0),
                                       ((9, 25), C["s05.d"] + 1.2, COR)])
    igual_bola(c, t, C["s05.e"], xf + 50, y, "36%", r=100, cor=CERTO)


# ---------------- sem reposição ----------------
def b_sem(c, t, C, b):
    def urna_sem():
        E.frase(c, t, C["s06.a"], [("sem", "g", 84, COR), ("reposição", "g", 84, COR)], W / 2, 170, "center", passo=0.15)
        E.foco(c, t, C["s06"] + 0.3, 0.5, lambda a: urna(c, CX_U, CY_U, 400, 440, a))
        E.foco(c, t, C["s06.b"], 0.5, lambda a: prato(c, CX_U + 380, 400, 170, a))
        dim = None
        if C["s06.c"] <= t < C["s07"]:
            dim = lambda i: 1.0 if URNA[i] == AZUL else 0.35
        elif C["s07.b"] <= t:
            dim = lambda i: 1.0 if (URNA[i] == AZUL and i != 0) else 0.35
        bolas_urna(c, t, C["s06"] + 0.5, CX_U, CY_U, 400, 440, mov={0: [(C["s07"] + 0.1, (CX_U + 380, 400))]}, apaga=dim)
        linha(c, t, XP + 180, 400, 96, [("1ª:", C["s06.c"] - 0.2), ((3, 5), C["s06.c"], AZUL)])
        E.foco(c, t, C["s07"] + 0.6, 0.45, lambda a: E.escreve(c, "saiu azul: a pista", XP + 600, 420, 54, "i", TINTA2, a))
        E.foco(c, t, C["s07.a"], 0.45, lambda a: (E.escreve(c, "sobram", XP + 180, 600, 56, "i", TINTA, a), E.escreve(c, "4 bolas", XP + 400, 602, 64, "g", TINTA, a)))
        E.foco(c, t, C["s07.b"], 0.45, lambda a: (E.escreve(c, "só", XP + 690, 600, 56, "i", TINTA, a), E.escreve(c, "2 azuis", XP + 780, 602, 64, "g", AZUL, a)))
        linha(c, t, XP + 180, 780, 96, [("2ª:", C["s07.c"] - 0.2), ((2, 4), C["s07.c"], AZUL)])
    E.saida(c, t, C["s08"] - 0.1, urna_sem)
    if C["s08"] <= t < C["s09"]:
        def conta():
            E.frase(c, t, C["s08"] + 0.1, [("sem", "g", 84, COR), ("reposição", "g", 84, COR)], W / 2, 170, "center", passo=0.15)
            y = 470
            xs, xf = linha(c, t, W / 2, y, 110, [((3, 5), C["s08.a"]), ("×", C["s08.a"] + 0.3), ((2, 4), C["s08.a"] + 0.5), ("=", C["s08.a"] + 1.0),
                                                   ((6, 20), C["s08.a"] + 1.2), ("=", C["s08.b"] - 0.2), ((3, 10), C["s08.b"], COR),
                                                   ("=", C["s08.c"] - 0.2), ("30%", C["s08.c"], COR)], "center")
            nota(c, t, C["s08.b"] + 0.3, (xs[4] + xs[6]) / 2 + 60, y + 160, "÷ 2", 44, TINTA2)
            E.frase(c, t, C["s08.d"], ps("cada azul que sai deixa a urna com menos azuis", "i", 56, TINTA2), W / 2, 880, "center", passo=0.08)
            E.foco(c, t, C["s08.c"] + 0.6, 0.45, lambda a: E.centro(c, "com reposição era 36%: caiu", W / 2, 760, 52, "b", TINTA2, a))
        E.saida(c, t, C["s09"] - 0.1, conta)
    if t < C["s09"]:
        return
    E.frase(c, t, C["s09.a"], [("teste:", "i", 76), ("2", "g", 84, VERM), ("vermelhas", "g", 84, VERM)], W / 2, 170, "center", passo=0.12)
    E.foco(c, t, C["s09.b"] - 0.3, 0.45, lambda a: E.escreve(c, "com:", 200, 420, 64, "g", COR, a))
    xs, xf = linha(c, t, 420, 400, 96, [((2, 5), C["s09.b"]), ("×", C["s09.b"] + 0.3), ((2, 5), C["s09.b"] + 0.5), ("=", C["s09.b"] + 1.0),
                                         ((4, 25), C["s09.b"] + 1.2), ("= 16%", C["s09.b"] + 2.2, COR)])
    E.foco(c, t, C["s09.c"] - 0.3, 0.45, lambda a: E.escreve(c, "sem:", 200, 690, 64, "g", COR, a))
    xs, xf = linha(c, t, 420, 670, 96, [((2, 5), C["s09.c"]), ("×", C["s09.c"] + 0.3), ((1, 4), C["s09.c"] + 0.5), ("=", C["s09.c"] + 1.0),
                                         ((2, 20), C["s09.c"] + 1.2), ("=", C["s09.d"] - 0.2), ((1, 10), C["s09.d"]), ("= 10%", C["s09.d"] + 1.2, COR)])
    E.foco(c, t, C["s09.e"], 0.5, lambda a: E.pilula(c, "sem reposição: eventos dependentes", W / 2, 950, 54, estilo="g", fundo=TINTA2, a=a))


# ---------------- regra ----------------
def b_regra(c, t, C, b):
    def duas():
        E.frase(c, t, C["s10.a"], ps("multiplique as chances de cada tirada", "i", 68), W / 2, 180, "center", passo=0.1)
        E.frase(c, t, C["s10.b"], [("o", "i", 64, TINTA2), ("que", "i", 64, TINTA2), ("muda", "i", 64, TINTA2), ("é", "i", 64, TINTA2), ("a", "i", 64, TINTA2),
                                   ("urna", "g", 70, COR)], W / 2, 290, "center", passo=0.1)
        E.foco(c, t, C["s10.c"], 0.5, lambda a: urna(c, 520, 640, 330, 360, a))
        bolas_urna(c, t, C["s10.c"] + 0.2, 520, 640, 330, 360)
        nota(c, t, C["s10.c"] + 0.4, 520, 900, "com: fica igual", 54, COR)
        E.foco(c, t, C["s10.d"], 0.5, lambda a: (urna(c, 1250, 640, 330, 360, a), prato(c, 1580, 560, 140, a)))
        pos, r = vagas(1250, 640, 330, 360, 5)
        for i in range(1, 5):
            E.foco(c, t, C["s10.d"] + 0.2 + 0.06 * i, 0.4, lambda a, i=i: E.bola(c, pos[i][0], pos[i][1], r, URNA[i], a))
        E.foco(c, t, C["s10.d"] + 0.6, 0.4, lambda a: E.bola(c, 1580, 560, r, AZUL, a))
        nota(c, t, C["s10.d"] + 0.4, 1330, 900, "sem: perde a bola que saiu", 54, COR)
    E.saida(c, t, C["s11"] - 0.1, duas)
    if t < C["s11"]:
        return
    E.frase(c, t, C["s11"] + 0.1, ps("detalhe de prova", "i", 72, TINTA2), W / 2, 180, "center")
    E.foco(c, t, C["s11"] + 0.3, 0.5, lambda a: urna(c, 520, 640, 380, 420, a))
    bolas_urna(c, t, C["s11"] + 0.4, 520, 640, 380, 420, mov={0: [(C["s11.a"] + 0.2, (480, 300))], 3: [(C["s11.a"] + 0.2, (570, 300))]})
    E.foco(c, t, C["s11.a"], 0.5, lambda a: E.pilula(c, "tirar 2 de uma vez", 1300, 480, 60, estilo="g", fundo=TINTA2, a=a))
    E.foco(c, t, C["s11.b"], 0.5, lambda a: E.pilula(c, "= sem reposição", 1300, 640, 60, estilo="g", a=a))
    nota(c, t, C["s11.b"] + 1.4, 1300, 800, "a 1ª não volta antes da 2ª", 50, TINTA2, "i")


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s12"] + 0.1, [("cuidado", "g", 90, ERRADO), ("com", "i", 84), ("isto", "i", 84)], W / 2, 160, "center")
    E.foco(c, t, C["s12"] + 0.3, 0.5, lambda a: (urna(c, CX_U, CY_U, 400, 440, a), prato(c, CX_U + 380, 420, 170, a)))
    pos, r = vagas(CX_U, CY_U, 400, 440, 5)
    for i in range(1, 5):
        E.foco(c, t, C["s12"] + 0.5 + 0.06 * i, 0.4, lambda a, i=i: E.bola(c, pos[i][0], pos[i][1], r, URNA[i], a))
    E.foco(c, t, C["s12"] + 0.6, 0.4, lambda a: E.bola(c, CX_U + 380, 420, r, AZUL, a))
    E.foco(c, t, C["s12.a"], 0.45, lambda a: E.pilula(c, "tira só do total", XP + 520, 330, 50, estilo="g", fundo=ERRADO, a=a))
    y = 520
    xs, xf = linha(c, t, XP + 150, y, 100, [((3, 5), C["s12.b"]), ("×", C["s12.b"] + 0.3), ((3, 4), C["s12.b"] + 0.5, ERRADO), ("=", C["s12.c"] - 0.2),
                                             ((9, 20), C["s12.c"], ERRADO)])
    if t >= C["s12.e"]:
        E.risco(c, xs[2] - 10, y + 110, xs[2] + 90, y - 110, t, C["s12.e"], largura=11)
        E.risco(c, xs[4] - 10, y + 110, xs[4] + 120, y - 110, t, C["s12.e"] + 0.2, largura=11)
    E.foco(c, t, C["s12.d"], 0.45, lambda a: E.centro(c, "a que saiu era azul", CX_U + 380, 300, 46, "b", AZUL, a))
    E.foco(c, t, C["s12.e"], 0.45, lambda a: E.escreve(c, "sai de cima e de baixo:", XP + 150, 790, 56, "i", TINTA, a))
    linha(c, t, XP + 150, 920, 100, [((3, 5), C["s12.e"] + 0.3), ("×", C["s12.e"] + 0.5), ((2, 4), C["s12.e"] + 0.7, CERTO)])
    E.foco(c, t, C["s12.e"] + 1.0, 0.4, lambda a: E.selo(c, XP + 520, 920, 46, True, a))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def desce():
        E.frase(c, t, C["s13.a"], [("sem", "i", 72, CLARO), ("reposição,", "i", 72, CLARO), ("mesma", "g", 78, BR), ("cor:", "g", 78, BR)], W / 2, 200, "center", passo=0.1)
        E.frase(c, t, C["s13.b"], [("desce", "g", 78, BR), ("1", "g", 84, CLARO), ("em", "i", 72, CLARO), ("cima", "i", 72, CLARO), ("e", "i", 72, CLARO),
                                   ("1", "g", 84, CLARO), ("embaixo", "i", 72, CLARO)], W / 2, 310, "center", passo=0.1)
        E.foco(c, t, C["s13.c"], 0.45, lambda a: (E.bola(c, 760, 450, 30, AZUL, a), E.bola(c, 840, 450, 30, AZUL, a), E.bola(c, 920, 450, 30, AZUL, a),
                                                  E.escreve(c, "3 azuis seguidas", 980, 468, 54, "i", CLARO, a)))
        tds = [C["s13.d"], C["s13.d"] + 0.6, C["s13.d"] + 1.2]
        xsf = [600, 960, 1320]
        for (n, d), x, td in zip(((3, 5), (2, 4), (1, 3)), xsf, tds):
            E.fr(c, t, td, n, d, x, 660, 130, BR)
        for k in range(2):
            E.pontes(c, t, xsf[k] + 70, xsf[k + 1] - 70, 660, 130, "− 1", tds[k + 1] - 0.3, tds[k + 1] - 0.1, cor=E.COR, size=36)
    E.saida(c, t, C["s14"] - 0.1, desce)
    if C["s14"] <= t < C["s15"]:
        def produto():
            E.formula_em(c, t, C["s14"] + 0.1, "f{3}{5} × f{2}{4} × f{1}{3}", 560, 330, 96, "g", BR)
            E.formula_em(c, t, C["s14.a"] + 0.2, "em cima: 3 × 2 × 1 = 6", 400, 540, 72, "g", BR)
            E.formula_em(c, t, C["s14.b"], "embaixo: 5 × 4 × 3 = 60", 400, 670, 72, "g", BR)
            linha(c, t, 400, 850, 100, [((6, 60), C["s14.c"], BR), ("=", C["s14.c"] + 0.6, BR), ((1, 10), C["s14.c"] + 0.8, CLARO)])
        E.saida(c, t, C["s15"] - 0.1, produto)
    if t < C["s15"]:
        return
    E.frase(c, t, C["s15.a"], ps("cada bola que sai é daquela cor e do total", "i", 60, CLARO), W / 2, 200, "center", passo=0.08)
    E.foco(c, t, C["s15.b"], 0.5, lambda a: E.pilula(c, "não vale quando a cor muda", W / 2, 350, 54, estilo="g", fundo=ERRADO, a=a))
    E.foco(c, t, C["s15.c"], 0.45, lambda a: (E.bola(c, 640, 540, 34, AZUL, a), E.escreve(c, "e depois", 700, 558, 54, "i", CLARO, a),
                                              E.bola(c, 960, 540, 34, VERM, a)))
    linha(c, t, 560, 760, 110, [((3, 5), C["s15.c"] + 0.6, BR), ("×", C["s15.d"] - 0.2, CLARO), ((2, 4), C["s15.d"], BR)])
    E.foco(c, t, C["s15.e"], 0.5, lambda a: E.escreve(c, "só o total desceu", 1100, 790, 64, "g", CLARO, a))
    nota(c, t, C["s15.d"] + 0.8, 1300, 650, "nenhuma vermelha saiu", 46, CLARO, "i")


# ---------------- questão ----------------
def lampadas(c, t, t0, x, y, passo, s, tq=None, tdim=None):
    """10 lâmpadas em linha; as 3 últimas viram queimadas em tq; tdim apaga as queimadas"""
    for k in range(10):
        ruim = k >= 7 and tq is not None and t >= tq
        al = 0.35 if (ruim and tdim is not None and t >= tdim) else 1.0
        E.foco(c, t, t0 + 0.05 * k, 0.4, lambda a, k=k, ruim=ruim, al=al: lampada(c, x + k * passo, y, s, not ruim, a * al))


def b_questao(c, t, C, b):
    E.frase(c, t, C["s16"] + 0.1, [("hora", "i", 72, COR), ("de", "i", 72, COR), ("testar", "i", 72, COR)], XE, 170)
    lampadas(c, t, C["s16.a"], XE + 50, 380, 100, 150, tq=C["s16.b"])
    E.foco(c, t, C["s16.a"] + 0.4, 0.45, lambda a: E.escreve(c, "10 lâmpadas", XE, 590, 64, "g", COR, a))
    E.foco(c, t, C["s16.b"] + 0.3, 0.45, lambda a: E.escreve(c, "3 queimadas", XE + 440, 590, 64, "g", ERRADO, a))
    E.frase(c, t, C["s16.c"], ps("tire 2, uma depois da outra", "i", 62), XE, 700, passo=0.1)
    E.frase(c, t, C["s16.d"], [("chance", "i", 64), ("de", "i", 64), ("ambas", "g", 70, COR), ("funcionarem?", "g", 70)], XE, 830, passo=0.1)
    E.foco(c, t, C["s16.d"] + 1.6, 0.45, lambda a: E.escreve(c, "com e sem reposição", XE, 920, 56, "i", TINTA2, a))
    E.relogio(c, t, C["s17.a"], 1500, 560, 190)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    lampadas(c, t, C["s18"], 300, 230, 90, 120, tq=C["s18"], tdim=C["s18.a"])
    E.foco(c, t, C["s18.a"], 0.45, lambda a: E.escreve(c, "funcionam 7 das 10", 1270, 250, 56, "g", CERTO, a))
    E.foco(c, t, C["s18.b"], 0.45, lambda a: E.escreve(c, "com:", 200, 500, 64, "g", COR, a))
    xs, xf = linha(c, t, 400, 480, 96, [((7, 10), C["s18.b"] + 0.4), ("×", C["s18.b"] + 0.7), ((7, 10), C["s18.b"] + 0.9), ("=", C["s18.c"] - 0.2),
                                         ((49, 100), C["s18.c"])])
    igual_bola(c, t, C["s18.d"], xf + 50, 480, "49%", r=95, cor=CERTO)
    E.foco(c, t, C["s19.a"], 0.45, lambda a: E.escreve(c, "sem:", 200, 840, 64, "g", COR, a))
    nota(c, t, C["s19.b"], 560, 690, "2ª: 6 boas em 9", 48, TINTA2)
    xs, xf = linha(c, t, 400, 820, 96, [((7, 10), C["s19.c"]), ("×", C["s19.c"] + 0.3), ((6, 9), C["s19.c"] + 0.5), ("=", C["s19.c"] + 1.0),
                                         ((42, 90), C["s19.c"] + 1.2)])
    E.pontes(c, t, xf + 15, xf + 175, 820, 96, "÷ 6", C["s19.d"] - 0.6, C["s19.d"] - 0.3, size=36)
    E.resultado(c, t, C["s19.d"], 7, 15, xf + 300, 820, 84, 105, CERTO)
    nota(c, t, C["s19.d"] + 1.0, xf + 300, 990, "pouco menos de 47%", 44, TINTA2, "i")


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s20"], [("resumindo", "i", 92, COR)], W / 2, 190, "center")
        E.foco(c, t, C["s20.a"], 0.5, lambda a: E.pilula(c, "multiplique as chances de cada tirada", W / 2, 380, 60, estilo="g", a=a))
        E.frase(c, t, C["s20.b"], ps("sem reposição: a bola que saiu sai do total e da sua cor", "i", 58, TINTA2), W / 2, 560, "center", passo=0.08)
        E.fr(c, t, C["s20.b"] + 1.6, 3, 5, 820, 780, 120, AZUL)
        E.pontes(c, t, 900, 1020, 780, 120, "− 1", C["s20.b"] + 2.0, C["s20.b"] + 2.2, size=36)
        E.fr(c, t, C["s20.b"] + 2.4, 2, 4, 1100, 780, 120, AZUL)
    E.saida(c, t, C["s21"] - 0.1, resumo)
    if t < C["s21"]:
        return
    E.frase(c, t, C["s21"] + 0.1, ps("próxima aula", "i", 84), XE, 280)
    E.frase(c, t, C["s21.a"], [("árvore", "g", 84, COR), ("de", "i", 76), ("probabilidades", "g", 84, COR)], XE, 410, passo=0.12)
    E.arvore(c, t, C["s21.a"] + 0.5, [("A", "V"), ("A", "V")], XE, 460, 620, 420, ramos=[["f{3}{5}", "f{2}{5}"], None], size=44, size_ramo=44,
             tn=[C["s21.a"] + 0.6, C["s21.b"]])
    E.foco(c, t, C["s21.b"], 0.45, lambda a: E.escreve(c, "soma os caminhos", XE + 800, 640, 56, "i", TINTA2, a))
    E.foco(c, t, C["s21.c"], 0.45, lambda a: E.escreve(c, "e a genética dos pais", XE + 800, 730, 56, "g", COR, a))
    E.foco(c, t, C["s21.d"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1560, 330, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s21.d"] + 0.3, 0.8))
    E.cursor(c, lerp(1850, 1690, p), lerp(560, 355, p), ep(t, C["s21.d"] + 0.2, 0.4))
    E.frase(c, t, C["s21.e"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 980, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, com=b_com, sem=b_sem, regra=b_regra, erro=b_erro, atalho=b_atalho,
              questao=b_questao, resposta=b_resposta, fim=b_fim)
