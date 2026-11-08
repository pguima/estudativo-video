"""Visual — Estudativo · MAT-EST-015: boxplot e amplitude.
Mesma linguagem da Estatística definida em MAT-EST-001 (docstring de lá) e dos quartis de MAT-EST-014 (as mesmas onze notas
em fichas, pílulas Q1, Q2 e Q3, E.reta de 0 a 10). Conta da vez à direita, resposta na esfera, atalho no palco escuro.
Novo nesta aula (para copiar nas próximas):
- BOXPLOT (boxplot()): caixa de Q1 a Q3 na cor da matéria clara, com borda forte; traço grosso da mediana; bigodes até o
  mínimo e o máximo com a ponta em T. Tudo sobre E.reta, na mesma escala. Cada parte entra no seu marcador.
- PEDAÇOS: a faixa atrás de cada um dos quatro pedaços acende (pedacos=[(i, t, cor)]), com "≈ 25%" em cima (rotulos_pedacos()).
- AMPLITUDE = COLCHETE acima do desenho, de ponta a ponta, com o número (E.chave + rótulo; amplitude()).
- DUAS TURMAS = dois boxplots, um sobre o outro, na mesma reta, com o nome à esquerda.
Sem voz ainda: todo instante vem de C[...] (marcadores do roteiro), para acompanhar a voz real quando ela chegar."""
import math
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Estatística")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-EST-015_boxplot_e_amplitude.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("cinco", "amplitude", "pedacos", "atalho", "turmas", "questao", "fim"))
BR = "#FFFFFF"
PAPEL = E.PAPEL
NOTAS = [2, 3, 4, 4, 5, 6, 7, 7, 8, 9, 10]
CINCO = (2, 4, 6, 8, 10)
MANHA, NOITE = (4, 5, 6, 7, 8), (1, 4, 6, 8, 10)
CENTRO, BAIRRO = (2, 3, 4, 5, 7), (1, 2, 3, 6, 12)
assert (NOTAS[0], NOTAS[2], NOTAS[5], NOTAS[8], NOTAS[10]) == CINCO and 10 - 2 == 8 and 8 - 4 == 4
assert MANHA[4] - MANHA[0] == 4 and NOITE[4] - NOITE[0] == 9 and MANHA[2] == NOITE[2] == 6
assert CENTRO[4] - CENTRO[0] == 5 and BAIRRO[4] - BAIRRO[0] == 11 and BAIRRO[2] == 3 and CENTRO[2] == 4
PED = ["mín → Q1", "Q1 → Q2", "Q2 → Q3", "Q3 → máx"]


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças comuns ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    """uma frase, palavra a palavra (palavra com %, ², ³, → ou ≈ vai na grotesca)"""
    return [(w, "g" if any(ch in w for ch in "%²³→≈") else est, size * (0.92 if any(ch in w for ch in "%²³→≈") and est != "g" else 1), cor) for w in txt.split()]


def fcen(c, t, t0, s, cx, y, size, cor=None):
    E.formula_em(c, t, t0, s, cx, y, size, "g", cor, "center")


def bola_txt(c, t, t0, s, cx, cy, r, size, cor=None):
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r * ease_back(prog(t, t0, 0.5)), cor, a),
                                     E.formula(c, s, cx, cy + size * 0.36, size, "g", E.SOBRE, a, "center")))


def fase(c, t, t0, t1, fn):
    if t0 - 0.01 <= t < t1 + 0.4:
        E.saida(c, t, t1, fn)


def ficha(c, s, cx, cy, size, a=1.0, cor=None, borda=None):
    """um dado da lista: pílula branca com borda fina (cor = fundo aceso)"""
    if a <= 0:
        return
    w = E.larg(s, "b", size) + size * 1.1
    h = size * 1.55
    rr = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2, cy - h / 2, w, h), h / 2, h / 2)
    c.drawRRect(rr, M.paint(cor or BR, a))
    c.drawRRect(rr, M.paint(borda or (cor or FIO), a, stroke=3))
    centro(c, s, cx, cy + size * 0.36, size, "b", (BR if cor and M.lum(cor) < 0.5 else TINTA), a)


# ================= o boxplot (copiar nas próximas aulas) =================
def boxplot(c, t, vx, y, cinco, t_caixa, t_med=None, t_b1=None, t_b2=None, h=110, cor=None, escuro=False, pedacos=(), a=1.0):
    """caixa e bigodes sobre a reta vx. cinco = (mín, Q1, Q2, Q3, máx). t_caixa / t_med / t_b1 (bigode de baixo) / t_b2 = instantes
    (None = já pronto junto com a caixa). pedacos = [(i, t, cor)] acende a faixa do pedaço i (0 = mín→Q1 ... 3 = Q3→máx)"""
    mn, q1, q2, q3, mx = cinco
    k = cor or E.COR
    tinta = BR if escuro else TINTA
    t_med = t_caixa if t_med is None else t_med
    t_b1 = t_caixa if t_b1 is None else t_b1
    t_b2 = t_caixa if t_b2 is None else t_b2
    xs = [mn, q1, q2, q3, mx]
    for tb, de, ate in ((t_b1, q1, mn), (t_b2, q3, mx)):
        p = ease_io(prog(t, tb, 0.5))
        if p > 0:
            xe = lerp(vx(de), vx(ate), p)
            M.line(c, vx(de), y, xe, y, tinta, a, 6)
            if p > 0.9:
                M.line(c, vx(ate), y - h * 0.28, vx(ate), y + h * 0.28, tinta, a * ep(t, tb + 0.45, 0.2), 6)
    p = ease_io(prog(t, t_caixa, 0.6))
    if p > 0:
        m = (vx(q1) + vx(q3)) / 2
        xl, xr = lerp(m, vx(q1), p), lerp(m, vx(q3), p)
        r = skia.Rect.MakeXYWH(xl, y - h / 2, xr - xl, h)
        c.drawRect(r, M.paint(E.mix(k, "#07070F" if escuro else PAPEL, 0.55 if escuro else 0.72), a))
    for i, ti, cc in pedacos:   # a faixa de cada pedaço, por cima do fundo da caixa
        q = ep(t, ti, 0.4)
        if q > 0:
            c.drawRect(skia.Rect.MakeXYWH(vx(xs[i]), y - h / 2 - 26, vx(xs[i + 1]) - vx(xs[i]), h + 52), M.paint(cc, (0.45 if escuro else 0.32) * q * a))
    if p > 0:
        c.drawRect(r, M.paint(k if not escuro else BR, a, stroke=6))
    p = ep(t, t_med, 0.4)
    if p > 0:
        M.line(c, vx(q2), y - h / 2, vx(q2), lerp(y - h / 2, y + h / 2, p), tinta if not escuro else BR, a, 10)


def rotulos_pedacos(c, t, ts, vx, y, cinco, s="≈ 25%", size=44, cor=None):
    """o rótulo em cima de cada pedaço, no instante ts[i]"""
    for i, ti in enumerate(ts):
        if ti is None:
            continue
        x = (vx(cinco[i]) + vx(cinco[i + 1])) / 2
        E.foco(c, t, ti, 0.4, lambda a, x=x: centro(c, s, x, y, size, "g", cor or COR, a))


def amplitude(c, t, t0, x0, x1, y, rot, cor=None, size=56):
    """colchete acima, de x0 a x1, com o número no meio"""
    p = ep(t, t0, 0.5)
    if p <= 0:
        return
    E.chave(c, x0, x1, y, cor or E.COR, p, -30, 6)
    E.foco(c, t, t0 + 0.3, 0.4, lambda a: E.pilula(c, rot, (x0 + x1) / 2, y - 30 - size * 0.9, size, "g", fundo=cor or E.COR, a=a))


def cinco_pilulas(c, t, ts, vx, y, cinco, nomes=("mín", "Q1", "Q2", "Q3", "máx"), size=40, escuro=False):
    """o nome e o valor de cada um dos cinco números, embaixo da reta"""
    for i, (ti, v, n) in enumerate(zip(ts, cinco, nomes)):
        if ti is None:
            continue
        E.foco(c, t, ti, 0.4, lambda a, v=v, n=n: E.pilula(c, f"{n} = {E._num(v)}", vx(v), y, size, "g", fundo=E.COR if not escuro else BR,
                                                         cor=E.SOBRE if not escuro else "#07070F", a=a))


VX0, VX1 = 260, 1660


def reta10(c, t, t0, y, escuro=False, vmax=10, marcas=None, rotulo=None, x1=VX1):
    vx = E.reta(c, t, t0, VX0, x1, y, 0, vmax, marcas or list(range(0, vmax + 1)), escuro=escuro, size=40)
    if rotulo:
        E.foco(c, t, t0 + 0.3, 0.4, lambda a: E.escreve(c, rotulo, x1 + 80, y + 14, 40, "i", BR if escuro else TINTA2, a))
    return vx


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    a1, b1, c1 = C["s01.a"], C["s01.b"], C["s01.c"]

    def um():
        E.frase(c, t, a1, ps("duas turmas,", "i", 64) + ps("a mesma mediana:", "i", 64) + [("6", "g", 76, COR)], W / 2, 190, "center", 0.1)
        vx = reta10(c, t, a1, 820)
        for k, (nome, cinco) in enumerate((("manhã", MANHA), ("noite", NOITE))):
            y = 430 + 220 * k
            E.foco(c, t, a1 + 0.4, 0.4, lambda a, y=y, nome=nome: E.escreve(c, nome, 60, y + 16, 48, "i", TINTA2, a))
            boxplot(c, t, vx, y, cinco, b1 + 0.3 * k, t_med=a1 + 0.5)
        if t >= a1 + 0.5:
            M.line(c, vx(6), 330, vx(6), 820, COR, ep(t, a1 + 0.5, 0.5), 4, dash=E.TRACO)
        E.frase(c, t, b1, ps("parecidas?", "i", 56, TINTA2) + [("nem um pouco", "g", 60, ERRADO)], 1460, 300, "center", 0.08)
        E.foco(c, t, c1, 0.5, lambda a: E.pilula(c, "o boxplot", W / 2, 1000, 60, "g", a=a, cor=E.SOBRE))
    E.saida(c, t, C["s02"] - 0.1, um)

    if t >= C["s02"]:
        ta, tb = C["s02.a"], C["s02.b"]
        E.foco(c, t, tb - 0.2, 0.7, lambda a: E.bola(c, 1560, 600, 240 * ease_back(prog(t, tb - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, ps("até o fim desta aula", "i", 88), XE, 280, passo=0.14)
        E.frase(c, t, ta + 1.4, ps("ler um", "i", 88) + [("boxplot", "g", 100, COR)], XE, 420, passo=0.14)
        E.frase(c, t, ta + 2.6, ps("e a", "i", 88) + [("amplitude", "g", 100, COR)], XE, 560, passo=0.14)
        E.foco(c, t, tb + 0.1, 0.5, lambda a: (centro(c, "+ atalho", 1560, 575, 80, "g", E.SOBRE, a),
                                               centro(c, "de prova", 1560, 660, 80, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"] + 0.3, ps("você só precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "1", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisa:", XE + 175, 700, 120, "i", TINTA, a))
    E.frase(c, t, C["s03.a"] + 0.6, [("os quartis", "g", 90, COR)], XE, 860)
    x, w = 900, 900
    itens = (("s03.b", "Q1", "mediana da metade de baixo"), ("s03.c", "Q2", "a própria mediana"), ("s03.d", "Q3", "mediana da metade de cima"))
    for i, (k, l1, l2) in enumerate(itens):
        y = 220 + i * 230
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 180, p, prog_=p)
        E.foco(c, t, C[k] + 0.1, 0.4, lambda a, l1=l1, y=y: E.pilula(c, l1, x + 100, y + 90, 54, "g", a=a, cor=E.SOBRE))
        E.frase(c, t, C[k] + 0.3, ps(l2, "i", 52), x + 190, y + 108, "left", 0.08)
    alvo = [220 + i * 230 + 150 for i in range(3)]
    q1 = ease_io(prog(t, C["s03.c"] - 0.35, 0.5))
    q2 = ease_io(prog(t, C["s03.d"] - 0.35, 0.5))
    E.cursor(c, x + w - 30, lerp(lerp(alvo[0], alvo[1], q1), alvo[2], q2), ep(t, C["s03.b"], 0.4))
    E.frase(c, t, lerp(C["s03.d"], C["s03.end"], 0.6), ps("faltou?", "i", 50, COR) + ps("procure no canal", "i", 50), x, 960, "left", 0.1)


# ---------------- os cinco números ----------------
def b_cinco(c, t, C, b):
    a4, b4, c4, d4, e4, f4, g4 = (C[f"s04.{k}"] for k in "abcdefg")
    E.frase(c, t, a4, ps("as", "i", 60) + [("11 notas", "g", 64, COR)] + ps("da aula de quartis", "i", 60), W / 2, 190, "center", 0.1)
    passo = 150
    x0 = W / 2 - passo * 5
    idx = (0, 2, 5, 8, 10)
    ts = (c4, d4, e4, f4, g4)
    for i, v in enumerate(NOTAS):
        cor = E.COR if i in idx and t >= ts[idx.index(i)] else None
        E.foco(c, t, a4 + 0.05 * i, 0.4, lambda a, i=i, v=v, cor=cor: ficha(c, str(v), x0 + passo * i, 380, 64, a, cor), sobe=10)
    E.frase(c, t, b4, ps("cabem em", "i", 60) + [("5 números", "g", 66, COR)], W / 2, 560, "center", 0.1)
    for k, (ti, n, v) in enumerate(zip(ts, ("menor nota", "1º quartil", "mediana", "3º quartil", "maior nota"), CINCO)):
        x = 330 + 315 * k
        bola_txt(c, t, ti, str(v), x, 760, 90, 90)
        E.foco(c, t, ti + 0.1, 0.4, lambda a, x=x, n=n: centro(c, n, x, 910, 44, "i", TINTA2, a))
        if t >= ti:
            p = ep(t, ti, 0.5)
            M.line(c, x0 + passo * idx[k], 430, lerp(x0 + passo * idx[k], x, p), lerp(430, 660, p), E.mix(E.COR, PAPEL, 0.5), p, 3, dash=E.TRACO)


# ---------------- o desenho ----------------
BY = 560   # a linha do boxplot grande


def b_desenho(c, t, C, b):
    a5, b5, c5 = C["s05.a"], C["s05.b"], C["s05.c"]
    a6, b6, c6, d6 = (C[f"s06.{k}"] for k in "abcd")
    E.foco(c, t, C["s05"], 0.4, lambda a: E.formula(c, "2 · 4 · 6 · 8 · 10", W / 2, 200, 64, "g", COR, a, "center"))
    vx = reta10(c, t, a5, 800)
    boxplot(c, t, vx, BY, CINCO, b5, t_med=c5, t_b1=b6, t_b2=c6, h=150)
    cinco_pilulas(c, t, [b6 + 0.4, b5 + 0.4, c5 + 0.3, b5 + 0.6, c6 + 0.4], vx, 400, CINCO)

    def um():
        E.frase(c, t, a5, ps("sobre uma", "i", 50, TINTA2) + [("reta com escala", "g", 54, TINTA2)], W / 2, 960, "center", 0.08)
        E.frase(c, t, b5 + 0.6, [("caixa:", "g", 52, COR)] + ps("de Q1 a Q3", "i", 50) + ps("·", "g", 50) + [("traço:", "g", 52, COR)] + ps("a mediana", "i", 50),
                W / 2, 1030, "center", 0.06)
    fase(c, t, C["s05"], C["s06"] - 0.1, um)
    if t < C["s06"] - 0.1:
        return
    E.frase(c, t, a6, ps("duas hastes:", "i", 54) + [("os bigodes", "g", 58, COR)], W / 2, 960, "center", 0.08)
    E.foco(c, t, d6, 0.5, lambda a: E.pilula(c, "caixa e bigodes", W / 2, 1035, 46, "g", a=a, cor=E.SOBRE))


# ---------------- amplitude ----------------
def b_amplitude(c, t, C, b):
    a7, b7, c7, d7, e7 = (C[f"s07.{k}"] for k in "abcde")
    a8, b8, c8, d8 = (C[f"s08.{k}"] for k in "abcd")
    vx = reta10(c, t, C["s07"] - 1, 800)
    ped = [(1, d8, E.COR), (2, d8, E.COR)]
    boxplot(c, t, vx, BY, CINCO, C["s07"] - 1, h=150, pedacos=ped)
    cinco_pilulas(c, t, [C["s07"] - 1] * 5, vx, 920, CINCO, size=36)

    def um():
        E.frase(c, t, a7, [("amplitude", "g", 70, COR)] + ps("= maior − menor", "i", 64), 560, 200, "center", 0.1)
        fcen(c, t, b7, "10 − 2 = 8", 1360, 200, 80)
        amplitude(c, t, c7, vx(2), vx(10), 440, "8")
        E.frase(c, t, d7, ps("um número só:", "i", 52) + [("8", "g", 60, COR)], 1360, 290, "center", 0.08)
        E.foco(c, t, e7, 0.4, lambda a: E.escreve(c, "de 2 a 10", 330, 300, 56, "g", ERRADO, a))
        if t >= e7 + 0.4:
            E.risco(c, 320, 285, 600, 265, t, e7 + 0.4, largura=9)
    fase(c, t, C["s07"], C["s08"] - 0.1, um)
    if t < C["s08"] - 0.1:
        return
    E.frase(c, t, a8, ps("a", "i", 60) + [("largura da caixa", "g", 66, COR)] + ps("também conta", "i", 60), W / 2, 200, "center", 0.1)
    amplitude(c, t, b8, vx(4), vx(8), 440, "8 − 4 = 4")
    E.frase(c, t, c8, [("amplitude interquartil", "g", 60, COR)], W / 2, 300, "center", 0.08)
    E.frase(c, t, d8, ps("o espalhamento da", "i", 50, TINTA2) + [("metade do meio", "g", 54, COR)], W / 2, 1035, "center", 0.08)


# ---------------- pedaços e o erro ----------------
def b_pedacos(c, t, C, b):
    a9, b9 = C["s09.a"], C["s09.b"]
    a0, b0, c0 = C["s10.a"], C["s10.b"], C["s10.c"]
    if t < C["s10"] - 0.1 + 0.4:
        def um():
            vx = reta10(c, t, C["s09"] - 1, 800)
            cores = [E.COR, CLARO, E.COR, CLARO]
            ped = [(i, a9 + 0.6 * i, cores[i]) for i in range(4)]
            boxplot(c, t, vx, BY, CINCO, C["s09"] - 1, h=150, pedacos=ped)
            E.frase(c, t, a9, [("4 pedaços", "g", 70, COR)], W / 2, 200, "center")
            for i in range(4):
                x = (vx(CINCO[i]) + vx(CINCO[i + 1])) / 2
                E.foco(c, t, a9 + 0.6 * i, 0.4, lambda a, x=x, i=i: centro(c, PED[i], x, 700, 38, "b", TINTA2, a))
            rotulos_pedacos(c, t, [b9 + 0.2 * i for i in range(4)], vx, 440, CINCO, size=52)
            E.frase(c, t, b9 + 1.0, ps("cada pedaço:", "i", 54) + [("≈ 1/4 dos dados", "g", 58, COR)], W / 2, 960, "center", 0.08)
        fase(c, t, C["s09"], C["s10"] - 0.1, um)
    if t < C["s10"] - 0.1:
        return
    # o erro: a turma da noite, com bigodes de tamanhos diferentes
    vx = reta10(c, t, C["s10"], 800)
    boxplot(c, t, vx, BY, NOITE, C["s10"], h=150, pedacos=[(0, b0, E.COR), (3, b0, E.COR)])
    cinco_pilulas(c, t, [C["s10"] + 0.3] * 5, vx, 920, NOITE, size=36)
    E.frase(c, t, C["s10"] + 0.2, [("erro comum:", "g", 60, ERRADO)], W / 2, 190, "center")
    E.frase(c, t, a0, ps("o bigode mais comprido", "i", 54) + [("tem mais dados?", "g", 58, ERRADO)], W / 2, 280, "center", 0.08)
    rotulos_pedacos(c, t, [b0, None, None, b0 + 0.2], vx, 440, NOITE, size=52)
    E.foco(c, t, a0 + 1.8, 0.4, lambda a: E.selo(c, 1650, 262, 36, False, a))
    E.frase(c, t, c0, ps("o comprido só mostra valores", "i", 50, TINTA2) + [("mais espalhados", "g", 54, COR)], W / 2, 1035, "center", 0.08)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    a1, b1, c1, d1, e1 = (C[f"s11.{k}"] for k in "abcde")
    a2, b2, c2 = C["s12.a"], C["s12.b"], C["s12.c"]
    vx = reta10(c, t, C["s11"], 820, escuro=True)
    acesos = [(i, c1 + 0.2 * (i - 1), CLARO) for i in (1, 2, 3)] if t < d1 else [(i, e1 + 0.2 * (i - 1), CLARO) for i in (1, 2)]
    boxplot(c, t, vx, 600, CINCO, C["s11"] + 0.2, h=150, escuro=True, pedacos=acesos)
    cinco_pilulas(c, t, [C["s11"] + 0.4] * 5, vx, 940, CINCO, size=36, escuro=True)

    def um():
        E.frase(c, t, C["s11"] + 0.2, ps("o atalho:", "i", 60, CLARO) + [("conte os pedaços", "g", 66, BR)], W / 2, 170, "center", 0.1)
        E.frase(c, t, b1, ps("mais que Q1?", "i", 56, CLARO), 560, 300, "center", 0.08)
        E.foco(c, t, c1, 0.4, lambda a: E.pilula(c, "3 pedaços = 75%", 560, 390, 50, "g", fundo=BR, cor="#07070F", a=a))
        E.frase(c, t, d1, ps("dentro da caixa?", "i", 56, CLARO), 1360, 300, "center", 0.08)
        E.foco(c, t, e1, 0.4, lambda a: E.pilula(c, "2 pedaços = 50%", 1360, 390, 50, "g", fundo=BR, cor="#07070F", a=a))
    fase(c, t, C["s11"], C["s12"] - 0.1, um)
    if t < C["s12"] - 0.1:
        return
    E.frase(c, t, a2, ps("os pedaços têm a", "i", 54, CLARO) + [("mesma quantidade de dados", "g", 58, BR)], W / 2, 190, "center", 0.08)
    E.frase(c, t, a2 + 1.6, ps("mesmo com tamanhos diferentes", "i", 50, CLARO), W / 2, 270, "center", 0.08)
    E.foco(c, t, b2, 0.4, lambda a: E.selo(c, 420, 380, 36, False, a))
    E.frase(c, t, b2 + 0.1, ps("valor fora dos 5 números?", "i", 50, CLARO), 480, 398, "left", 0.08)
    E.foco(c, t, c2, 0.4, lambda a: E.pilula(c, "só uma estimativa", 1420, 380, 48, "g", fundo=BR, cor="#07070F", a=a))


# ---------------- comparar turmas ----------------
TY1, TY2, TR = 400, 700, 900


def turmas(c, t, t0, tm, tn, vx, rot_t=None):
    for k, (nome, cinco, ti) in enumerate((("manhã", MANHA, tm), ("noite", NOITE, tn))):
        y = (TY1, TY2)[k]
        E.foco(c, t, t0, 0.4, lambda a, y=y, nome=nome: E.escreve(c, nome, 50, y + 16, 50, "i", TINTA2, a))
        boxplot(c, t, vx, y, cinco, ti, h=120, pedacos=[(3, rot_t, E.COR)] if (k == 1 and rot_t is not None) else ())


def b_turmas(c, t, C, b):
    a3, b3, c3, d3 = (C[f"s13.{k}"] for k in "abcd")
    a4, b4, c4, d4, e4 = (C[f"s14.{k}"] for k in "abcde")
    vx = reta10(c, t, a3, TR)
    turmas(c, t, a3, b3, c3, vx, rot_t=e4)
    if t >= d3:
        M.line(c, vx(6), 320, vx(6), TR, COR, ep(t, d3, 0.5), 4, dash=E.TRACO)

    def um():
        E.frase(c, t, a3, ps("uma sobre a outra,", "i", 56) + [("na mesma escala", "g", 60, COR)], W / 2, 190, "center", 0.08)
        E.frase(c, t, b3 + 0.3, ps("manhã: de 4 a 8, caixa de 5 a 7", "i", 46, TINTA2), 1000, 300, "center", 0.06)
        E.frase(c, t, c3 + 0.3, ps("noite: de 1 a 10, caixa de 4 a 8", "i", 46, TINTA2), 1000, 595, "center", 0.06)
        E.foco(c, t, d3, 0.4, lambda a: E.pilula(c, "mesma mediana: 6", vx(6), 1045, 42, "g", a=a, cor=E.SOBRE))
    fase(c, t, C["s13"], C["s14"] - 0.1, um)
    if t < C["s14"] - 0.1:
        return
    amplitude(c, t, a4, vx(4), vx(8), TY1 - 80, "8 − 4 = 4", size=44)
    amplitude(c, t, b4, vx(1), vx(10), TY2 - 80, "10 − 1 = 9", cor=TINTA2, size=44)
    E.foco(c, t, c4, 0.4, lambda a: E.pilula(c, "manhã: homogênea", 1620, TY1, 44, "g", a=a, cor=E.SOBRE))
    E.foco(c, t, d4, 0.4, lambda a: E.pilula(c, "noite: espalhada", 1450, TY2 + 135, 42, "g", fundo=TINTA2, a=a))
    E.frase(c, t, e4, ps("noite:", "i", 50) + [("≈ 25%", "g", 50, COR)] + ps("tiraram 8 ou mais (Q3 = 8)", "i", 46), W / 2, 1055, "center", 0.06)


# ---------------- questão ----------------
QY1, QY2, QR = 330, 520, 680


def lojas(c, t, t0, vx, ped=(), a=1.0):
    for k, (nome, cinco) in enumerate((("centro", CENTRO), ("bairro", BAIRRO))):
        y = (QY1, QY2)[k]
        E.foco(c, t, t0, 0.4, lambda a_, y=y, nome=nome: E.escreve(c, nome, 40, y + 16, 46, "i", TINTA2, a_))
        boxplot(c, t, vx, y, cinco, t0 + 0.2 * k, h=110, pedacos=[p[1:] for p in ped if p[0] == k], a=a)


def b_questao(c, t, C, b):
    a5, b5, c5, d5 = (C[f"s15.{k}"] for k in "abcd")
    E.frase(c, t, C["s15"] + 0.1, ps("hora de testar:", "i", 64, COR) + ps("tempo de entrega, em dias", "i", 56), XE, 170, passo=0.1)
    vx = reta10(c, t, a5, QR, vmax=12, rotulo="dias", x1=1480)
    lojas(c, t, a5 + 0.3, vx)
    E.frase(c, t, b5, [("1)", "g", 54, COR)] + ps("a amplitude de cada loja", "i", 52), XE, 840, passo=0.08)
    E.frase(c, t, c5, [("2)", "g", 54, COR)] + ps("pelo menos metade em até", "i", 52) + [("3 dias:", "g", 54)] + ps("qual loja?", "i", 52), XE, 920, passo=0.08)
    E.frase(c, t, d5, [("3)", "g", 54, COR)] + ps("qual é", "i", 52) + [("mais previsível?", "g", 54)], XE, 1000, passo=0.08)
    E.relogio(c, t, C["s16.a"], 1740, 850, 82)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    a7, b7, c7, d7, e7 = (C[f"s17.{k}"] for k in "abcde")
    a8, b8, c8 = C["s18.a"], C["s18.b"], C["s18.c"]
    vx = reta10(c, t, C["s17"] - 1, QR, vmax=12, rotulo="dias", x1=1480)
    ped = [(0, i, a8 + 0.2 * i, E.COR) for i in range(4)] if t >= b8 else []
    ped += [(1, 3, c8, ERRADO)] if t >= c8 else []
    lojas(c, t, C["s17"] - 1, vx, ped)
    amplitude(c, t, a7, vx(2), vx(7), QY1 - 70, "7 − 2 = 5", size=40)
    amplitude(c, t, b7, vx(1), vx(12), QY2 - 70, "12 − 1 = 11", cor=TINTA2, size=40)
    for k, (v, y) in enumerate(((4, QY1), (3, QY2))):
        E.foco(c, t, d7 + 0.3 * k, 0.4, lambda a, v=v, y=y: c.drawCircle(vx(v), y, 18, M.paint(ERRADO if v == 4 else CERTO, a)))

    def um():
        E.frase(c, t, c7, ps("metade em até 3 dias? pergunta de", "i", 52) + [("mediana", "g", 56, COR)], W / 2, 840, "center", 0.08)
        E.frase(c, t, d7, ps("bairro:", "i", 52) + [("3", "g", 56, CERTO)] + ps("· centro:", "i", 52) + [("4", "g", 56, ERRADO)], W / 2, 920, "center", 0.08)
        E.foco(c, t, e7, 0.4, lambda a: E.pilula(c, "resposta: a loja do bairro", W / 2, 1010, 50, "g", a=a, cor=E.SOBRE))
    fase(c, t, C["s17"], C["s18"] - 0.1, um)
    if t < C["s18"] - 0.1:
        return
    E.foco(c, t, a8, 0.4, lambda a: E.pilula(c, "mais previsível: a do centro", W / 2, 850, 52, "g", a=a, cor=E.SOBRE))
    E.frase(c, t, b8, ps("caixa e bigodes", "i", 50) + [("curtos", "g", 54, COR)], W / 2, 940, "center", 0.08)
    E.frase(c, t, c8, ps("no bairro, o bigode chega a", "i", 50) + [("12 dias", "g", 54, ERRADO)], W / 2, 1020, "center", 0.08)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s19"], [("resumindo", "i", 92, COR)], W / 2, 210, "center")
        itens = (("s19.a", [("boxplot:", "g", 66, COR)] + ps("os cinco números", "i", 62)),
                 ("s19.b", [("cada pedaço:", "g", 66, COR)] + ps("≈ 1/4 dos dados", "i", 62)),
                 ("s19.c", [("amplitude:", "g", 66, COR)] + ps("maior ponta − menor", "i", 62)))
        for i, (k, partes) in enumerate(itens):
            y = 420 + i * 190
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 200, y - 25, 52, a=a), centro(c, str(i + 1), 200, y - 4, 60, "g", E.SOBRE, a)))
            E.frase(c, t, C[k] + 0.1, partes, 290, y, "left", 0.1)
    E.saida(c, t, C["s20"] - 0.1, resumo)
    if t < C["s20"]:
        return
    a0, b0, c0, d0, e0 = (C[f"s20.{k}"] for k in "abcde")
    E.frase(c, t, a0, ps("a amplitude", "i", 70) + [("só olha as pontas", "g", 76, COR)], XE, 250, passo=0.12)
    E.frase(c, t, b0, ps("na próxima aula,", "i", 60) + [("todos os dados", "g", 66, COR)], XE, 390, passo=0.1)
    E.frase(c, t, b0 + 1.2, ps("quanto cada valor se afasta da média", "i", 50, TINTA2), XE, 470, passo=0.08)
    E.frase(c, t, c0, [("desvio médio, variância", "g", 64, COR)], XE, 610, passo=0.1)
    E.frase(c, t, c0 + 0.8, ps("e", "i", 60) + [("desvio padrão", "g", 64, COR)], XE, 700, passo=0.1)
    E.foco(c, t, d0, 0.5, lambda a: E.pilula(c, "Inscreva-se", 1550, 380, 76, estilo="g", a=a, cor=E.SOBRE))
    p = ease_io(prog(t, d0 + 0.3, 0.8))
    E.cursor(c, lerp(1830, 1680, p), lerp(700, 405, p), ep(t, d0 + 0.2, 0.4))
    E.frase(c, t, e0, [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 980, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, cinco=b_cinco, desenho=b_desenho, amplitude=b_amplitude, pedacos=b_pedacos,
              erro=b_pedacos, atalho=b_atalho, turmas=b_turmas, questao=b_questao, resposta=b_resposta, fim=b_fim)
