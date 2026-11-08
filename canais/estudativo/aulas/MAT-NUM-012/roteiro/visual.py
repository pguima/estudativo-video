"""Visual — Estudativo · MAT-NUM-012: praticando números e as quatro operações (3.040.500 > 3.004.950; 1.000 − 368 = 999 − 367 = 632;
48 × 5 = 480 ÷ 2 = 240 e 99 × 7 = 700 − 7 = 693, total 933; 1.288 ÷ 23 = 56; 500 ÷ 42 = 11 com resto 38 → 12 ônibus).
Linguagem de cada parte, como nas aulas de origem: grupos de três casas em caixas (MAT-NUM-002), conta armada com E.armada
(MAT-NUM-004), atalhos de multiplicar em linha (MAT-NUM-007 e 009), divisão na chave com E.conta_div e os testes do palpite AO LADO
da chave (MAT-NUM-010). Cada questão: título "questão n", a pergunta e o relógio de pausa; a resposta passo a passo; erro em
vermelho, certo em verde; resposta final na pílula da cor da matéria.
Peças locais: ps(), cf(), resp(), lista(), titulo(), pergunta(), grupos() (número em grupos de três casas).
Todo instante vem de C[...] (marcadores do roteiro), para acompanhar a voz real quando ela chegar."""
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Números e Contas")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-NUM-012_praticando_quatro_operacoes.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("q1", "q2", "q3", "q4", "q5", "fim"))
BR = "#FFFFFF"
assert 3040500 > 3004950 and 1000 - 368 == 999 - 367 == 632 and 632 + 368 == 1000
assert 48 * 5 == 480 // 2 == 240 and 99 * 7 == 700 - 7 == 693 and 240 + 693 == 933
assert 23 * 6 == 138 and 23 * 5 == 115 and 128 - 115 == 13 and 23 * 56 == 1288 and 23 * 10 == 230 and 23 * 100 == 2300
assert 500 // 42 == 11 and 500 % 42 == 38 and 42 * 11 == 462 and 42 * 2 == 84 > 80


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças gerais ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def cf(c, partes, x, y, size, a=1.0, align="left", est="g"):
    ws = [E.formula(None, s, 0, 0, size, est, a=0) for s, _ in partes]
    xx = x - sum(ws) / 2 if align == "center" else x - sum(ws) if align == "right" else x
    if c is not None and a > 0:
        for (s, cor), wi in zip(partes, ws):
            E.formula(c, s, xx, y, size, est, cor, a)
            xx += wi
    return sum(ws)


def cf_em(c, t, t0, partes, x, y, size, align="left"):
    E.foco(c, t, t0, 0.5, lambda a: cf(c, partes, x, y, size, a, align))


def resp(c, t, t0, partes, cx, cy, size=64, alto=1.75, cor=None):
    if isinstance(partes, str):
        partes = [(partes, BR)]

    def f(a):
        w = cf(None, partes, 0, 0, size) + size * 1.1
        h = size * alto
        M.rrect(c, cx - w / 2, cy - h / 2, w, h, h / 2, cor or E.COR, a, shadow=True)
        cf(c, partes, cx, cy + size * 0.36, size, a, "center")
    E.foco(c, t, t0, 0.5, f)


def lista(c, t, itens, x, y0, dy=130, size=58):
    for i, (t0, partes) in enumerate(itens):
        y = y0 + i * dy
        E.foco(c, t, t0, 0.5, lambda a, i=i, y=y: (E.bola(c, x + 36, y - size * 0.36, 36, a=a),
                                                   centro(c, str(i + 1), x + 36, y - size * 0.36 + 16, 46, "g", BR, a)))
        E.frase(c, t, t0 + 0.1, partes, x + 100, y, "left", 0.1)


def titulo(c, t, t0, n, nome, x=XE, y=150):
    E.frase(c, t, t0, ps("questão", "i", 64, COR) + [(str(n), "g", 72, COR)] + ps(f"· {nome}", "i", 56, TINTA2), x, y, "left", 0.1)


def relogio(c, t, t0, X=1500, Y=470):
    E.relogio(c, t, t0, X, Y, 170)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    a1, b1, c1 = C["s01.a"], C["s01.b"], C["s01.c"]
    E.foco(c, t, a1, 0.5, lambda a: E.escreve(c, "5", XE - 8, 520, 340, "g", COR, a))
    E.foco(c, t, a1 + 0.15, 0.5, lambda a: E.escreve(c, "questões", XE + 215, 500, 110, "i", TINTA, a))
    nomes = ("ler", "subtrair", "multiplicar", "dividir", "escolher a conta")
    for i, s in enumerate(nomes):
        x, y = 1180 + (i % 2) * 420, 220 + (i // 2) * 150
        if i == 4:
            x = 1390
        E.foco(c, t, lerp(a1 + 0.8, b1, 0.12 + 0.17 * i), 0.5, lambda a, s=s, x=x, y=y: E.pilula(c, s, x, y, 56, "g", a=a, cor=E.SOBRE))
    E.frase(c, t, b1, ps("em cada uma,", "i", 62) + [("pause e resolva", "g", 66, COR)], XE, 760, "left", 0.1)
    E.frase(c, t, b1 + 1.4, ps("antes de ver a resposta", "i", 62), XE, 860, "left", 0.1)
    E.frase(c, t, c1, ps("errar aqui", "i", 56, TINTA2) + [("não custa nada", "g", 58, CERTO)], XE, 990, "left", 0.1)


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    k = {x: C[f"s02.{x}"] for x in "abcde"}
    E.frase(c, t, C["s02"] + 0.1, ps("você vai usar", "i", 70, COR), XE, 180, "left", 0.1)
    lista(c, t, [(k["a"], [("ler e comparar", "g", 62)] + ps("números grandes", "i", 58)),
                 (k["b"], [("somar e subtrair", "g", 62)]),
                 (k["c"], [("multiplicar", "g", 62)]),
                 (k["d"], [("dividir,", "g", 62)] + ps("até por dois algarismos", "i", 58)),
                 (k["e"], [("escolher a conta", "g", 62, COR)] + ps("pelo sentido", "i", 58))], XE, 340, 135, 58)
    E.frase(c, t, C["s02.end"] - 2.4, ps("travou?", "i", 56, COR) + ps("procure a aula no canal", "i", 56), XE, 1010, "left", 0.12)


# ---------------- questão 1: ler e comparar ----------------
def pos_grupos(s, x, size):
    """[(x0, x1)] de cada grupo de três casas, sem desenhar"""
    xx, pos = x, []
    for g in s.split("."):
        w = E.larg(g, "g", size)
        pos.append((xx, xx + w))
        xx += w + E.larg(".", "g", size) + 4
    return pos


def grupos(c, s, x, y, size, cores=None, a=1.0, caixas=None):
    """número com ponto, escrito por grupos; cores = {índice do grupo: cor}; caixas = {índice: (cor, a)} desenha a caixa pontilhada do grupo.
    Devolve [(x0, x1)] de cada grupo"""
    gs = s.split(".")
    xx, pos = x, []
    for i, g in enumerate(gs):
        w = E.larg(g, "g", size)
        if caixas and i in caixas:
            cor_, q = caixas[i]
            if q > 0:
                E.caixa_pontilhada(c, xx - 14, y - size * 0.86, w + 28, size * 1.12, q * a, cor_, prog_=q)
        E.escreve(c, g, xx, y, size, "g", (cores or {}).get(i, TINTA), a)
        pos.append((xx, xx + w))
        xx += w
        if i < len(gs) - 1:
            E.escreve(c, ".", xx, y, size, "g", TINTA, a)
            xx += E.larg(".", "g", size) + 4
    return pos


N1, N2 = "3.040.500", "3.004.950"


def b_q1(c, t, C, b):
    a3, b3, c3, d3 = (C[f"s03.{k}"] for k in "abcd")
    titulo(c, t, a3, 1, "ler e comparar")
    E.frase(c, t, b3, ps("prêmio", "i", 60, TINTA2) + [("A", "g", 64, COR)], XE, 390, "left", 0.1)
    E.foco(c, t, b3 + 0.3, 0.5, lambda a: grupos(c, N1, XE, 520, 130, a=a))
    E.frase(c, t, b3 + 0.8, ps("prêmio", "i", 60, TINTA2) + [("B", "g", 64, COR)], XE, 680, "left", 0.1)
    E.foco(c, t, b3 + 1.1, 0.5, lambda a: grupos(c, N2, XE, 810, 130, a=a))
    E.frase(c, t, c3, ps("qual é o", "i", 64) + [("maior?", "g", 70, COR)], XE, 960, "left", 0.1)
    E.frase(c, t, d3, ps("leia em", "i", 56, TINTA2) + [("voz alta", "g", 60)], 1290, 960, "left", 0.1)
    relogio(c, t, C["s04.a"], 1500, 470)


def b_r1(c, t, C, b):
    k5 = {x: C[f"s05.{x}"] for x in "abcdef"}
    k6 = {x: C[f"s06.{x}"] for x in "ab"}
    y1, y2, size, x0 = 330, 520, 130, 400

    def comparar():
        E.frase(c, t, C["s05"] + 0.1, ps("vamos lá", "i", 62, COR), XE, 150, "left", 0.1)
        cx1 = {} if t < k5["c"] else {0: (TINTA2, ep(t, k5["c"], 0.5))}
        if t >= k5["d"]:
            cx1[1] = (CERTO, ep(t, k5["d"], 0.5))
        cx2 = dict(cx1)
        if 1 in cx2:
            cx2[1] = (ERRADO, cx2[1][1])
        cor1 = {1: CERTO} if t >= k5["e"] else {}
        cor2 = {1: ERRADO} if t >= k5["e"] else {}
        E.foco(c, t, C["s05"], 0.5, lambda a: (E.escreve(c, "A", XE + 40, y1, 80, "g", COR, a), grupos(c, N1, x0, y1, size, cor1, a, cx1)))
        E.foco(c, t, C["s05"] + 0.2, 0.5, lambda a: (E.escreve(c, "B", XE + 40, y2, 80, "g", COR, a), grupos(c, N2, x0, y2, size, cor2, a, cx2)))
        # os pontos contados
        P1 = pos_grupos(N1, x0, size)
        for P_, y in ((P1, y1), (P1, y2)):
            for i in range(2):
                xp = P_[i][1] + 14
                k = ease_back(prog(t, k5["a"] + 0.25 * i, 0.4)) * (1 - ep(t, k5["b"], 0.4))
                if k > 0:
                    c.drawCircle(xp, y + 24, 28 * k, M.paint(COR, 0.25))
        E.foco(c, t, k5["a"], 0.5, lambda a: E.escreve(c, "2 pontos e 2 pontos: empate", x0, 680, 54, "i", TINTA2, a * (1 - ep(t, k5["b"], 0.4))))
        E.frase(c, t, k5["b"], ps("grupo por grupo,", "i", 58) + [("da esquerda", "g", 60, COR)], x0, 680, "left", 0.1)
        E.foco(c, t, k5["c"], 0.5, lambda a: E.escreve(c, "milhões: 3 = 3", x0, 800, 60, "b", TINTA2, a))
        E.foco(c, t, k5["d"], 0.5, lambda a: E.escreve(c, "milhares: 40 mil > 4 mil", x0, 900, 60, "b", CERTO, a))
        E.frase(c, t, k5["f"], ps("olhou o fim,", "i", 58, ERRADO) + [("950?", "g", 62, ERRADO)] + ps("pegadinha", "i", 58, ERRADO), x0, 1010, "left", 0.1)
    E.saida(c, t, C["s06"] - 0.1, comparar)
    if t < C["s06"] - 0.1:
        return
    a6, b6 = k6["a"], k6["b"]
    E.frase(c, t, a6 - 0.6, ps("o maior é o", "i", 66) + [("A", "g", 72, COR)], XE, 200, "left", 0.1)
    E.foco(c, t, a6, 0.5, lambda a: grupos(c, N1, XE, 400, 170, {0: COR, 1: COR, 2: COR}, a))
    nomes = (("três milhões,", 0), ("quarenta mil,", 1), ("quinhentos", 2))
    P_ = pos_grupos(N1, XE, 170)
    for j, (s, i) in enumerate(nomes):
        x0_, x1_ = P_[i]
        ti = b6 + 1.0 + 0.9 * j
        q = ep(t, ti, 0.4)
        if q > 0:
            E.chave(c, x0_, x1_, 450, COR, q, 26)
    resp(c, t, a6 + 0.8, "três milhões, quarenta mil e quinhentos", W / 2, 640, 62, 1.9)
    E.frase(c, t, b6, ps("um grupo de cada vez,", "i", 58) + [("o nome do grupo no fim", "g", 60, COR)], W / 2, 820, "center", 0.1)
    for j, (s, i) in enumerate(nomes):
        E.frase(c, t, b6 + 1.0 + 0.9 * j, [(s, "g", 64, COR if j < 2 else TINTA)], 360 + 450 * j, 950, "left", 0.1)


# ---------------- questão 2: subtrair por cima do zero ----------------
def b_q2(c, t, C, b):
    a7, b7, c7, d7 = (C[f"s07.{k}"] for k in "abcd")
    titulo(c, t, a7, 2, "subtrair")
    E.frase(c, t, b7, ps("na conta:", "i", 64), XE, 400, "left", 0.1)
    E.foco(c, t, b7 + 0.3, 0.5, lambda a: E.escreve(c, "R$ 1.000", XE + 340, 410, 110, "g", TINTA, a))
    E.frase(c, t, c7, ps("boleto:", "i", 64), XE, 600, "left", 0.1)
    E.foco(c, t, c7 + 0.3, 0.5, lambda a: E.escreve(c, "R$ 368", XE + 340, 610, 110, "g", ERRADO, a))
    E.frase(c, t, d7, ps("quanto", "i", 76) + [("sobrou?", "g", 84, COR)], XE, 840, "left", 0.1)
    relogio(c, t, C["s08.a"], 1500, 470)


def b_r2(c, t, C, b):
    k9 = {x: C[f"s09.{x}"] for x in "abcd"}
    k0 = {x: C[f"s10.{x}"] for x in "abcdef"}
    xv, y0, size = 760, 400, 130
    # 1.000 − 368: os três zeros que pedem empréstimo

    def primeira():
        E.foco(c, t, k9["a"], 0.5, lambda a: (E.numero(c, "1000", xv, y0, size, "g", TINTA, a),
                                              E.numero(c, "368", xv, y0 + size * 1.22, size, "g", TINTA, a),
                                              E.escreve(c, "−", xv - 5.4 * E.casa(size), y0 + size * 1.22, size, "g", TINTA, a)))
        if t >= k9["a"] + 0.3:
            yl = y0 + size * 1.22 + size * 0.32
            M.line(c, xv - 5.6 * E.casa(size), yl, xv + 0.4 * E.casa(size), yl, TINTA, ep(t, k9["a"] + 0.3, 0.4), 6)
        for i in range(3):
            q = ep(t, k9["b"] + 0.2 * i, 0.4)
            if q > 0:
                cx = xv - (i + 0.5) * E.casa(size)
                c.drawCircle(cx, y0 - size * 0.36, size * 0.52, M.paint(ERRADO, q, stroke=6))
        E.frase(c, t, k9["b"], ps("empréstimo", "i", 58) + [("por cima de 3 zeros", "g", 60, ERRADO)], 1200, 330, "left", 0.1)
    E.saida(c, t, k9["c"], primeira)
    if t >= k9["c"]:
        E.frase(c, t, k9["c"], [("−1", "g", 76, COR)] + ps("de cada número", "i", 62), 1180, 300, "left", 0.1)
        E.armada(c, t, ["999", "367"], "−", "632", (k9["d"], k9["d"] + 0.4), (k0["a"], k0["b"], k0["c"]), xv, y0, size, tl=k9["d"] + 0.6)
        E.foco(c, t, k9["d"] + 0.8, 0.5, lambda a: E.escreve(c, "sem empréstimo", 1180, 430, 58, "g", CERTO, a))
    resp(c, t, k0["d"], "sobraram R$ 632", 1450, 600, 64)
    E.frase(c, t, k0["e"], ps("a", "i", 54, TINTA2) + [("distância", "g", 58, COR)] + ps("entre eles não muda", "i", 54, TINTA2), 1450, 760, "center", 0.1)
    cf_em(c, t, k0["f"], [("632 + 368 = 1.000", CERTO)], 1450, 900, 70, "center")


# ---------------- questão 3: atalhos de multiplicar ----------------
def b_q3(c, t, C, b):
    a1, b1, c1, d1 = (C[f"s11.{k}"] for k in "abcd")
    titulo(c, t, a1, 3, "multiplicar")
    E.foco(c, t, b1, 0.5, lambda a: E.escreve(c, "48", XE, 420, 130, "g", COR, a))
    E.frase(c, t, b1 + 0.3, ps("ingressos de", "i", 60) + [("R$ 5", "g", 70)], XE + 200, 410, "left", 0.1)
    E.foco(c, t, c1, 0.5, lambda a: E.escreve(c, "99", XE, 620, 130, "g", COR, a))
    E.frase(c, t, c1 + 0.3, ps("ingressos de", "i", 60) + [("R$ 7", "g", 70)], XE + 200, 610, "left", 0.1)
    E.frase(c, t, d1, ps("quanto", "i", 72) + [("arrecadou?", "g", 80, COR)], XE, 840, "left", 0.1)
    relogio(c, t, C["s12.a"], 1500, 470)


def b_r3(c, t, C, b):
    k3 = {x: C[f"s13.{x}"] for x in "abcd"}
    k4 = {x: C[f"s14.{x}"] for x in "abcde"}
    E.frase(c, t, k3["a"], ps("grupos iguais:", "i", 62) + [("multiplicação", "g", 66, COR)], XE, 170, "left", 0.1)
    # 48 × 5
    cf_em(c, t, k3["b"], [("48 × 5", TINTA)], XE, 340, 96)
    E.foco(c, t, k3["b"] + 0.6, 0.5, lambda a: E.pilula(c, "× 5 = × 10 ÷ 2", 1060, 310, 50, "g", a=a, cor=E.SOBRE))
    cf_em(c, t, k3["c"], [("48 × 10 = 480", TINTA2)], XE + 60, 470, 70)
    cf_em(c, t, k3["d"], [("480 ÷ 2 = ", TINTA2), ("240", COR)], XE + 60, 580, 70)
    # 99 × 7
    cf_em(c, t, k4["a"], [("99 × 7", TINTA)], XE, 730, 96)
    E.foco(c, t, k4["a"] + 0.6, 0.5, lambda a: E.pilula(c, "99 = 100 − 1", 1060, 700, 50, "g", a=a, cor=E.SOBRE))
    cf_em(c, t, k4["b"], [("100 × 7 = 700", TINTA2)], XE + 60, 860, 70)
    cf_em(c, t, k4["c"], [("700 − 7 = ", TINTA2), ("693", COR)], XE + 60, 970, 70)
    # junta
    X = 1580
    E.frase(c, t, k4["d"], ps("junte", "i", 64, COR), X, 480, "center", 0.1)
    cf_em(c, t, k4["d"] + 0.5, [("240 + 693", TINTA)], X, 620, 86, "center")
    resp(c, t, k4["e"], "R$ 933", X, 790, 84)


# ---------------- questão 4: dividir por dois algarismos ----------------
D_1288 = E.dividir("1288", 23, 0)
assert D_1288["quociente"] == "56" and D_1288["resto"] == 0


def b_q4(c, t, C, b):
    a5, b5, c5, d5 = (C[f"s15.{k}"] for k in "abcd")
    titulo(c, t, a5, 4, "dividir")
    E.frase(c, t, b5, ps("prêmio de", "i", 64), XE, 400, "left", 0.1)
    E.foco(c, t, b5 + 0.3, 0.5, lambda a: E.escreve(c, "R$ 1.288", XE + 330, 410, 110, "g", TINTA, a))
    E.frase(c, t, c5, ps("entre", "i", 64), XE, 600, "left", 0.1)
    E.foco(c, t, c5 + 0.3, 0.5, lambda a: E.escreve(c, "23 pessoas", XE + 200, 610, 100, "g", COR, a))
    E.frase(c, t, d5, ps("quanto para", "i", 72) + [("cada uma?", "g", 80, COR)], XE, 840, "left", 0.1)
    relogio(c, t, C["s16.a"], 1500, 470)


def b_r4(c, t, C, b):
    k7 = {x: C[f"s17.{x}"] for x in "abcd"}
    k8 = {x: C[f"s18.{x}"] for x in "abcdef"}
    k9 = {x: C[f"s19.{x}"] for x in "abcdef"}
    X = 1180

    def tamanho():
        E.frase(c, t, k7["a"], ps("repartir igualmente:", "i", 62) + [("divisão", "g", 66, COR)], XE, 200, "left", 0.1)
        cf_em(c, t, k7["b"], [("23 × 10 = 230", TINTA2)], XE, 400, 84)
        cf_em(c, t, k7["c"], [("23 × 100 = 2.300", TINTA2)], XE, 540, 84)
        cf_em(c, t, k7["c"] + 1.6, [("230 < 1.288 < 2.300", COR)], XE, 700, 84)
        resp(c, t, k7["d"], "resultado com 2 algarismos", W / 2, 880, 60)
    E.saida(c, t, C["s18"] - 0.1, tamanho)
    if t < C["s18"] - 0.1:
        return
    x, y, size = 200, 330, 120
    E.conta_div(c, t, D_1288, (k8["e"], k9["b"] + 0.2), (k9["a"], k9["d"]), C["s18"], x, y, size, ts=(k8["f"],))
    # o primeiro pedaço
    q = ep(t, k8["a"], 0.4) * (1 - ep(t, k9["a"], 0.4))
    if q > 0:
        E.caixa_pontilhada(c, x - 10, y - size * 0.92, E.casa(size) * 3 + 20, size * 1.15, q, COR, prog_=q)
    # os testes do palpite, ao lado da chave

    def testes1():
        cf_em(c, t, k8["b"], [("12 ÷ 2 = 6", TINTA2)], X, 300, 70)
        cf_em(c, t, k8["c"], [("23 × 6 = 138", ERRADO)], X, 420, 70)
        E.foco(c, t, k8["c"] + 0.8, 0.5, lambda a: E.escreve(c, "passou de 128", X, 500, 48, "i", ERRADO, a))
        E.frase(c, t, k8["d"], ps("palpite alto:", "i", 54) + [("baixe um", "g", 58, COR)], X, 600, "left", 0.1)
        cf_em(c, t, k8["e"], [("23 × 5 = 115", CERTO)], X, 720, 70)
        cf_em(c, t, k8["f"], [("128 − 115 = 13", TINTA2)], X, 840, 64)
    E.saida(c, t, k9["a"], testes1)
    if t >= k9["a"]:
        cf_em(c, t, k9["b"] - 0.4, [("13 ÷ 2 = 6", TINTA2)], X, 300, 70)
        cf_em(c, t, k9["c"], [("23 × 6 = 138", CERTO)], X, 420, 70)
        E.foco(c, t, k9["d"], 0.5, lambda a: E.escreve(c, "sobra zero", X, 500, 52, "g", CERTO, a))
        resp(c, t, k9["e"], "R$ 56 cada", 1560, 660, 66)
        cf_em(c, t, k9["f"], [("23 × 56 = 1.288", CERTO)], 1560, 840, 64, "center")
        E.foco(c, t, k9["f"] + 0.3, 0.5, lambda a: E.escreve(c, "prova real", 1430, 930, 46, "i", TINTA2, a))


# ---------------- questão 5: o resto decide ----------------
D_500 = E.dividir("500", 42, 0)
assert D_500["quociente"] == "11" and D_500["resto"] == 38


def onibus(c, cx, cy, w, h, cor, a, txt=None):
    M.rrect(c, cx - w / 2, cy - h / 2, w, h, h * 0.22, cor, a)
    for i in range(3):
        M.rrect(c, cx - w / 2 + w * (0.1 + 0.27 * i), cy - h * 0.32, w * 0.2, h * 0.3, 6, BR, a * 0.9)
    for dx in (-0.28, 0.28):
        c.drawCircle(cx + w * dx, cy + h / 2, h * 0.14, M.paint(TINTA, a))
    if txt:
        centro(c, txt, cx, cy + h * 0.32, h * 0.3, "g", BR, a)


def b_q5(c, t, C, b):
    a0, b0, c0, d0 = (C[f"s20.{k}"] for k in "abcd")
    titulo(c, t, a0, 5, "qual conta?")
    E.foco(c, t, b0, 0.5, lambda a: E.escreve(c, "500", XE, 430, 130, "g", COR, a))
    E.frase(c, t, b0 + 0.3, ps("alunos", "i", 70), XE + 290, 420, "left", 0.1)
    E.foco(c, t, c0, 0.5, lambda a: onibus(c, XE + 120, 600, 220, 110, COR, a, "42"))
    E.frase(c, t, c0 + 0.3, ps("lugares por ônibus", "i", 60), XE + 280, 630, "left", 0.1)
    E.frase(c, t, d0, ps("quantos", "i", 72) + [("ônibus?", "g", 80, COR)], XE, 840, "left", 0.1)
    relogio(c, t, C["s21.a"], 1500, 470)


def b_r5(c, t, C, b):
    k2 = {x: C[f"s22.{x}"] for x in "abcd"}
    k3 = {x: C[f"s23.{x}"] for x in "abcdef"}

    def conta():
        E.frase(c, t, C["s22"] + 0.1, ps("grupos de 42 em 500:", "i", 60) + [("divisão", "g", 64, COR)], XE, 170, "left", 0.1)
        E.conta_div(c, t, D_500, (k2["b"] + 0.4, k2["d"]), (k2["c"], k2["d"] + 0.5), k2["a"], 300, 380, 120, ts=(k2["b"] + 1.0,))
        cf_em(c, t, k2["c"] + 1.0, [("42 × 2 = 84", ERRADO)], 1350, 420, 70)
        E.foco(c, t, k2["c"] + 1.6, 0.5, lambda a: E.escreve(c, "passa de 80", 1350, 500, 48, "i", ERRADO, a))
        cf_em(c, t, k2["d"], [("42 × 1 = 42", CERTO)], 1350, 620, 70)
        cf_em(c, t, k2["d"] + 0.6, [("80 − 42 = 38", TINTA2)], 1350, 730, 64)
    E.saida(c, t, C["s23"] - 0.1, conta)
    if t < C["s23"] - 0.1:
        return
    cf_em(c, t, k3["a"], [("500 ÷ 42 = 11, resto 38", TINTA)], W / 2, 210, 80, "center")
    E.foco(c, t, k3["b"], 0.5, lambda a: (E.escreve(c, "11 ônibus?", XE, 340, 66, "g", ERRADO, a)))
    if t >= k3["b"] + 0.6:
        E.risco(c, XE - 10, 350, XE + 330, 290, t, k3["b"] + 0.6, largura=10)
    # 11 ônibus cheios + os 38 que ficam
    for i in range(11):
        cx, cy = 230 + (i % 6) * 150, 500 + (i // 6) * 130
        E.foco(c, t, k3["c"] + 0.08 * i, 0.4, lambda a, cx=cx, cy=cy: onibus(c, cx, cy, 120, 64, COR, a))
    E.foco(c, t, k3["c"] + 0.6, 0.5, lambda a: E.escreve(c, "11 × 42 = 462", 1150, 520, 66, "g", TINTA2, a))
    E.foco(c, t, k3["d"], 0.5, lambda a: (E.bola(c, 1460, 690, 90, ERRADO, a), centro(c, "38", 1460, 712, 70, "g", BR, a)))
    E.foco(c, t, k3["d"] + 0.4, 0.5, lambda a: E.escreve(c, "ficariam na escola", 1150, 840, 52, "i", ERRADO, a))
    E.foco(c, t, k3["e"], 0.5, lambda a: onibus(c, 230 + 5 * 150, 630, 120, 64, CERTO, a, "+1"))
    resp(c, t, k3["e"] + 0.3, "12 ônibus", 560, 820, 72, cor=CERTO)
    E.frase(c, t, k3["f"], ps("o resto", "i", 62) + [("não some:", "g", 66, COR)] + ps("a história decide", "i", 62), W / 2, 990, "center", 0.1)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s24"] + 0.1, [("resumindo", "i", 92, COR)], W / 2, 200, "center")
        itens = (("s24.a", "escolha a conta", "pelo sentido"), ("s24.b", "use o atalho", "quando o número ajuda"),
                 ("s24.c", "confira com", "a conta inversa"))
        for i, (k, l1, l2) in enumerate(itens):
            y = 380 + i * 200
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 230, y - 30, 56, a=a),
                                                         centro(c, str(i + 1), 230, y - 7, 64, "g", E.SOBRE, a)))
            E.frase(c, t, C[k] + 0.1, ps(l1, "i", 68) + [(l2, "g", 70, COR)], 320, y, "left", 0.1)
    E.saida(c, t, C["s25"] - 0.1, resumo)
    if t < C["s25"] - 0.1:
        return
    a5, b5, c5, d5, e5 = (C[f"s25.{k}"] for k in "abcde")
    E.frase(c, t, C["s25"], ps("na próxima aula", "i", 72), XE, 230, "left", 0.1)
    cf_em(c, t, a5, [("2 + 3 × 4", TINTA)], XE, 420, 120)
    E.frase(c, t, b5, ps("qual conta vem", "i", 64) + [("primeiro?", "g", 70, COR)], XE, 580, "left", 0.1)
    cf_em(c, t, c5, [("( )  [ ]", COR)], XE, 740, 110)
    E.foco(c, t, d5, 0.5, lambda a: E.pilula(c, "Inscreva-se", 1440, 420, 76, estilo="g", a=a, cor=E.SOBRE))
    p = ease_io(prog(t, d5 + 0.3, 0.8))
    E.cursor(c, lerp(1770, 1570, p), lerp(660, 445, p), ep(t, d5 + 0.2, 0.4))
    E.frase(c, t, e5, [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 960, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, q1=b_q1, r1=b_r1, q2=b_q2, r2=b_r2, q3=b_q3, r3=b_r3, q4=b_q4, r4=b_r4,
              q5=b_q5, r5=b_r5, fim=b_fim)
