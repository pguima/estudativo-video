"""Visual — Estudativo · MAT-FRA-003: frações equivalentes e simplificação.
Identidade em _ferramentas/editorial.py. A ideia central é UMA barra recortada na frente do aluno: 1/2 vira 2/4, os cortes
voltam, e 1/2 vira 3/6, com a parte pintada sempre do mesmo tamanho. × e ÷ aparecem como pontes em cima e embaixo."""
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, fr, sinal, palco, barra, chave, ponte, pontes, frac_q, centro
import motor as M

E.usar("Matemática", "Frações e Decimais")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-FRA-003_fracoes_equivalentes_simplificacao.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("barras", "simplificar", "atalho", "questao", "fim"))


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças desta aula ----------------
def numeros(c, t, t0, x, y, w, h, n, pintados, size=64):
    """conta os pedaços, um a um, dentro da barra"""
    for i in range(n):
        s, cx = str(i + 1), x + w * (i + 0.5) / n
        cor = "#FFFFFF" if i < pintados else TINTA
        E.foco(c, t, t0 + i * 0.14, 0.3, lambda a, s=s, cx=cx, cor=cor: E.escreve(
            c, s, cx - E.larg(s, "g", size) / 2, y + h / 2 + size * 0.36, size, "g", cor, a), sobe=8, blur=8)


def fica(c, t, t0, t1, partes, x, y, align="left", passo=0.2):
    """frase que entra em t0 e sai em t1"""
    E.saida(c, t, t1, lambda: E.frase(c, t, t0, partes, x, y, align, passo))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def inicio():
        s, cy = 250, 410
        anda = ep(t, C["s01.b"] - 0.2, 0.6)
        fr(c, t, C["s01.a"], 18, 24, lerp(960, 610, anda), cy, s)
        sinal(c, t, C["s01.b"] - 0.1, "=", 1000, cy - 20, 190)
        E.foco(c, t, C["s01.b"], 0.5, lambda a: E.bola(c, 1370, cy + 4, 270, a=a * ease_back(prog(t, C["s01.b"], 0.6))), blur=0)
        fr(c, t, C["s01.b"] + 0.1, 3, 4, 1370, cy, 210, "#FFFFFF")
        fica(c, t, 3.36, C["s01.b"] - 0.25, [("parece", "i", 88), ("difícil,", "g", 80), ("né?", "i", 88)], W / 2, 880, "center")
        E.frase(c, t, C["s01.b"] + 0.1, [("três", "i", 92), ("quartos", "i", 92), ("disfarçados", "g", 84, COR)], W / 2, 880, "center", passo=0.3)
    E.saida(c, t, C["s02"] + 0.25, inicio)

    if t >= C["s02"] + 0.3:
        E.foco(c, t, C["s02.c"] - 0.2, 0.7, lambda a: E.bola(c, 1450, 520, 300 * ease_back(prog(t, C["s02.c"] - 0.2, 0.7))), blur=0)
        E.frase(c, t, C["s02"] + 0.35, [("até", "i", 84), ("o", "i", 84), ("fim", "i", 84), ("da", "i", 84), ("aula", "i", 84)], XE, 280)
        E.frase(c, t, C["s02.a"] + 0.8, [("frações", "g", 96), ("que", "i", 104), ("valem", "i", 104)], XE, 450, passo=0.3)
        E.frase(c, t, C["s02.a"] + 1.9, [("a", "i", 104, COR), ("mesma", "i", 104, COR), ("coisa", "i", 104, COR)], XE, 560)
        E.frase(c, t, C["s02.b"] + 1.0, [("a", "i", 104), ("forma", "i", 104)], XE, 730)
        E.frase(c, t, C["s02.b"] + 1.7, [("mais", "g", 96, COR), ("simples", "g", 96, COR)], XE, 840)
        E.foco(c, t, C["s02.c"] + 0.2, 0.5, lambda a: (E.escreve(c, "+ atalho", 1290, 505, 84, "g", "#FFFFFF", a),
                                                      E.escreve(c, "de prova", 1310, 590, 84, "i", "#FFFFFF", a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"] + 0.35, [("para", "i", 84), ("acompanhar,", "i", 84)], XE, 310)
    E.frase(c, t, C["s03"] + 1.4, [("você", "i", 84), ("precisa", "i", 84), ("de", "i", 84)], XE, 410)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "3", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 235, 700, 120, "i", TINTA, a))
    E.frase(c, t, 27.8, [("procure", "i", 56), ("a", "i", 56), ("aula", "i", 56), ("no", "i", 56), ("canal", "g", 52, COR)], XE, 840, passo=0.14)
    x, w = 960, 780
    itens = (("s03.b", "Saber o que é", "uma fração"), ("s03.c", "As regras de", "divisibilidade"), ("s03.d", "Achar", "o MDC"))
    for i, (k, l1, l2) in enumerate(itens):
        y = 190 + i * 240
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 196, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 62)], x + 44, y + 84)
        E.frase(c, t, C[k] + 0.3, [(l2, "g", 62, COR)], x + 44, y + 160)
    alvo = [(x + w - 30, 190 + i * 240 + 170) for i in range(3)]
    q1, q2 = ease_io(prog(t, C["s03.c"] - 0.35, 0.5)), ease_io(prog(t, C["s03.d"] - 0.35, 0.5))
    E.cursor(c, alvo[0][0], lerp(lerp(alvo[0][1], alvo[1][1], q1), alvo[2][1], q2), ep(t, C["s03.b"], 0.4))


# ---------------- a mesma barra ----------------
BX, BW, BY, BH = 500, 1200, 430, 240  # a barra grande
R1, R2, R3, RH = 265, 445, 625, 140  # as três linhas da comparação: mesma largura, então a parte pintada se compara a olho


def b_barras(c, t, C, b):
    volta = C["s06"] + 1.9  # "a barra de dois pedaços": os cortes de quatro recolhem
    corta = C["s06"] + 3.75  # "corte cada um em três"
    mv = ep(t, C["s07.a"] + 0.2, 0.7)
    y, h = lerp(BY, R3, mv), lerp(BH, RH, mv)

    # título de cada momento
    fica(c, t, C["s04.a"] - 0.3, C["s05"] + 0.8, [("uma", "i", 88), ("barra", "g", 80, COR), ("em", "i", 88), ("dois", "i", 88), ("pedaços", "i", 88), ("iguais", "i", 88)],
         W / 2, 220, "center", 0.45)
    fica(c, t, C["s05.a"], C["s06"] + 0.3, [("cortar", "i", 88), ("cada", "i", 88), ("pedaço", "i", 88), ("em", "i", 88), ("dois", "g", 80, COR)], W / 2, 220, "center", 0.25)
    fica(c, t, C["s06"] + 1.35, corta - 0.2, [("volte", "i", 88), ("para", "i", 88), ("dois", "g", 80, COR), ("pedaços", "i", 88)], W / 2, 220, "center", 0.3)
    fica(c, t, corta, C["s07"] + 0.2, [("corte", "i", 88), ("cada", "i", 88), ("um", "i", 88), ("em", "i", 88), ("três", "g", 80, COR)], W / 2, 220, "center", 0.25)

    # a barra
    enche = ep(t, C["s04.b"], 0.6)
    meio = ep(t, C["s04"] + 1.95, 0.5)
    quartos = [(p, ep(t, C["s05.a"] + d, 0.5) * (1 - ep(t, volta, 0.6))) for p, d in ((0.25, 0), (0.75, 0.6))]
    sextos = [(p, ep(t, corta + d, 0.45)) for p, d in ((1 / 6, 0.1), (2 / 6, 0.4), (4 / 6, 0.95), (5 / 6, 1.25))]
    cortes = [(0.5, meio)] + quartos + sextos

    def linha(yy, cs, q=1.0):
        barra(c, BX, yy, BW, RH, 0.5, cs, q)
    if t >= C["s07.a"] + 0.9:  # as outras duas nascem na fala, com a mesma largura
        E.foco(c, t, C["s07.a"] + 1.08, 0.5, lambda q: linha(R1, [(0.5, 1)], q))
        E.foco(c, t, C["s07.a"] + 2.2, 0.5, lambda q: linha(R2, [(0.25, 1), (0.5, 1), (0.75, 1)], q))
        E.foco(c, t, C["s07.a"] + 1.08, 0.5, lambda q: E.fracao(c, 1, 2, 320, R1 + RH / 2, 74, COR, q))
        E.foco(c, t, C["s07.a"] + 2.2, 0.5, lambda q: E.fracao(c, 2, 4, 320, R2 + RH / 2, 74, COR, q))
    barra(c, BX, y, BW, h, 0.5, cortes, ep(t, C["s04.a"], 0.5), enche=enche)

    # rótulo da barra, com os nomes que ela vai ganhando (o último desce e encolhe junto com a barra)
    cx, cy = lerp(300, 320, mv), y + h / 2
    s = lerp(140, 74, mv)
    E.saida(c, t, C["s05.d"] - 0.3, lambda: fr(c, t, C["s04.c"], 1, 2, cx, cy, s, COR), 0.3)
    E.saida(c, t, volta - 0.3, lambda: fr(c, t, C["s05.d"], 2, 4, cx, cy, s, COR), 0.3)
    E.saida(c, t, C["s06.c"] - 0.3, lambda: fr(c, t, volta, 1, 2, cx, cy, s, COR), 0.3)
    fr(c, t, C["s06.c"], 3, 6, cx, cy, s, COR)

    # contagem dos pedaços: colchete em cima = total, colchete embaixo = pintados
    def total(t0, t1, txt):
        def fn():
            q = ep(t, t0, 0.4)
            chave(c, BX, BX + BW, BY - 6, TINTA2, q, -16, 4, abre=False)
            E.foco(c, t, t0, 0.4, lambda a: E.escreve(c, txt, BX + BW / 2 - E.larg(txt, "b", 62) / 2, BY - 44, 62, "b", TINTA, a))
        E.saida(c, t, t1, fn)

    def pint(t0, t1, txt):
        def fn():
            q = ep(t, t0, 0.4)
            chave(c, BX, BX + BW / 2, BY + BH + 8, COR, q, 16, 4, abre=False)
            E.foco(c, t, t0, 0.4, lambda a: E.escreve(c, txt, BX + BW / 4 - E.larg(txt, "b", 62) / 2, BY + BH + 104, 62, "b", COR, a))
        E.saida(c, t, t1, fn)

    total(C["s04"] + 2.7, C["s05.a"] - 0.2, "2 pedaços")
    pint(C["s04.b"], C["s05.a"] - 0.2, "1 pintado")
    total(C["s05.b"], C["s06"] + 0.5, "4 pedaços")
    pint(C["s05.c"], C["s06"] + 0.5, "2 pintados")
    total(C["s06.a"], C["s07"], "6 pedaços")
    pint(C["s06.b"], C["s07"], "3 pintados")
    E.saida(c, t, C["s06"] + 0.5, lambda: numeros(c, t, C["s05.b"], BX, BY, BW, BH, 4, 2))
    E.saida(c, t, C["s07"], lambda: numeros(c, t, C["s06.a"], BX, BY, BW, BH, 6, 3))

    # a pergunta: o que mudou? nada.
    if t >= C["s07"]:
        E.frase(c, t, C["s07"] + 0.3, [("o", "i", 80), ("que", "i", 80), ("mudou", "g", 72, COR), ("na", "i", 80), ("parte", "i", 80), ("pintada?", "i", 80)],
                XE, 170, passo=0.2)
        E.frase(c, t, C["s07.a"], [("nada.", "g", 104, COR)], 1290, 172)
        E.saida(c, t, C["s07.b"] - 0.15, lambda: E.foco(c, t, C["s07"] + 1.1, 0.5, lambda a: E.caixa_pontilhada(c, BX - 12, y - 12, BW / 2 + 24, h + 24, a, COR)))
        p = ep(t, C["s07.b"], 0.6)
        E.caixa_pontilhada(c, BX - 14, R1 - 14, BW / 2 + 28, R3 + RH - R1 + 28, p, COR, prog_=p)
        fica(c, t, C["s07.b"], C["s07.c"] - 1.6, [("a", "i", 76), ("mesma", "g", 68, COR), ("quantidade,", "i", 76), ("com", "i", 76), ("nomes", "i", 76), ("diferentes", "i", 76)],
             W / 2, 900, "center", 0.32)
        E.frase(c, t, C["s07.c"] - 1.44, [("frações", "i", 116), ("equivalentes", "g", 112, COR)], W / 2, 925, "center", passo=1.44)


# ---------------- a regra ----------------
def b_regra(c, t, C, b):
    def regra():
        E.frase(c, t, C["s08"] + 0.35, [("a", "i", 84), ("regra", "g", 76, COR), ("aparece", "i", 84), ("na", "i", 84), ("hora", "i", 84)], W / 2, 150, "center")
        x, w, y, h = 360, 1200, 205, 110
        cortar = C["s08"] + 2.45
        qs = [(0.5, 1), (0.25, ep(t, cortar, 0.5)), (0.75, ep(t, cortar + 0.4, 0.5))]
        E.foco(c, t, C["s08"] + 0.2, 0.5, lambda a: barra(c, x, y, w, h, 0.5, qs, a))
        s, cy, x0, x1 = 150, 535, 660, 1260
        fr(c, t, C["s08"] + 0.5, 1, 2, x0, cy, s, COR)
        frac_q(c, t, C["s08.a"], 2, 4, C["s08.b"], C["s08.a"], x1, cy, s)
        pontes(c, t, x0 + 110, x1 - 110, cy, s, "× 2", C["s08.b"], C["s08.a"])
        # de onde vem cada número
        E.frase(c, t, C["s08.b"], [("pintados", "i", 62)], 170, cy - s * 0.565 + 20)
        E.frase(c, t, C["s08.a"], [("pedaços", "i", 62)], 170, cy + s * 0.535 + 20)
        E.frase(c, t, C["s08.a"] + 0.3, [("4 no total", "b", 56, TINTA2)], 1370, cy + s * 0.535 + 20)
        E.frase(c, t, C["s08.b"] + 0.3, [("2 pintados", "b", 56, TINTA2)], 1370, cy - s * 0.565 + 20)
        E.frase(c, t, C["s08.c"], [("multiplique", "g", 84, COR), ("em", "i", 90), ("cima", "i", 90), ("e", "i", 90), ("embaixo", "i", 90)], W / 2, 830, "center", 0.3)
        E.frase(c, t, C["s08.c"] + 2.2, [("pelo", "i", 90), ("mesmo", "g", 84, COR), ("número", "g", 84, COR)], W / 2, 945, "center", 0.25)
    E.saida(c, t, C["s09"] - 0.1, regra)
    if t < C["s09"]:
        return

    E.frase(c, t, C["s09"] + 0.35, [("vamos", "i", 84), ("usar", "i", 84), ("a", "i", 84), ("regra", "g", 76, COR)], W / 2, 170, "center")
    s, cy, x0, x1 = 170, 480, 520, 1400
    fr(c, t, C["s09.a"], 3, 5, x0, cy, s)
    sobre = C["s09.d"]
    do_cinco = C["s09"] + 5.38  # "do cinco para o vinte"
    if t < sobre + 0.5:
        E.foco(c, t, C["s09.a"] + 1.5, 0.5, lambda a: E.fracao(c, 12 if t >= C["s09.c"] + 1.3 else "?", 20, x1, cy, s, COR if t >= C["s09.c"] + 1.3 else CINZA, a))
    E.resultado(c, t, sobre, 12, 20, x1, cy, 124, 190)
    ponte(c, t, C["s09.c"], x0 + 110, x1 - 205, cy - s * 0.565, "× 4", size=60)
    if t < C["s09.b"] + 0.7:
        ponte(c, t, do_cinco, x0 + 110, x1 - 205, cy + s * 0.535, "× ?", size=60)
    else:
        ponte(c, t, C["s09.b"] + 0.2, x0 + 110, x1 - 205, cy + s * 0.535, "× 4", size=60)
    E.frase(c, t, C["s09.b"] + 0.7, [("5 × 4 = 20", "b", 72, TINTA2)], W / 2, 830, "center")
    E.frase(c, t, C["s09.c"], [("3 × 4 = 12", "b", 72, COR)], W / 2, 925, "center")


# ---------------- simplificar ----------------
def b_simplificar(c, t, C, b):
    def volta():
        E.frase(c, t, C["s10"] + 0.35, [("simplificar", "g", 104, COR), ("é", "i", 104), ("o", "i", 104), ("caminho", "i", 104), ("de", "i", 104), ("volta", "i", 104)],
                W / 2, 190, "center")
        E.frase(c, t, C["s10.a"], [("divida", "g", 66), ("em", "i", 72), ("cima", "i", 72), ("e", "i", 72), ("embaixo", "i", 72), ("pelo", "i", 72), ("mesmo", "i", 72), ("número", "i", 72)],
                W / 2, 310, "center", 0.2)
        s, cy, x0, x1 = 170, 610, 560, 1360
        fr(c, t, C["s10.b"], 6, 8, x0, cy, s)
        pontes(c, t, x0 + 110, x1 - 190, cy, s, "÷ 2", C["s10.c"], C["s10.c"], size=60)
        E.resultado(c, t, C["s10.d"], 3, 4, x1, cy, 124, 160)
        E.frase(c, t, C["s10"] + 7.6, [("6", "g", 72), ("e", "i", 76), ("8", "g", 72), ("são", "i", 76), ("pares", "g", 72, COR)], W / 2, 900, "center", 0.17)
    E.saida(c, t, C["s11"] - 0.1, volta)
    if t < C["s11"]:
        return

    E.frase(c, t, C["s11"] + 0.35, [("quando", "i", 108), ("parar?", "g", 100, COR)], W / 2, 190, "center")
    E.frase(c, t, C["s11.a"], [("quando", "i", 70), ("só", "i", 70), ("o", "i", 70), ("1", "g", 66, COR), ("dividir", "i", 70), ("o", "i", 70), ("de", "i", 70), ("cima", "i", 70),
                                ("e", "i", 70), ("o", "i", 70), ("de", "i", 70), ("baixo", "i", 70)], W / 2, 310, "center", 0.2)
    em = C["s11"] + 5.6  # "em três quartos"
    x0, cy = 480, 570
    fr(c, t, em, 3, 4, x0, cy, 180, COR)
    # os divisores de cada um: o 1 é o único que aparece nos dois
    x1, y1, y2, s = 800, 530, 700, 72
    so = C["s11"] + 6.9  # "só o número um divide o três e o quatro"
    E.foco(c, t, so, 0.4, lambda a: E.escreve(c, "divide o 3:", x1, y1, s, "i", TINTA, a))
    E.foco(c, t, so + 1.2, 0.4, lambda a: E.escreve(c, "divide o 4:", x1, y2, s, "i", TINTA, a))
    x2 = x1 + 340
    for yy, nums, t0 in ((y1, ("1", "3"), so + 0.2), (y2, ("1", "2", "4"), so + 1.4)):
        for j, n in enumerate(nums):
            xx = x2 + j * 130
            E.foco(c, t, t0, 0.4, lambda a, n=n, xx=xx: (E.bola(c, xx + 20, yy - 26, 52, a=a) if n == "1" else None,
                                                          E.escreve(c, n, xx + 20 - E.larg(n, "g", s) / 2, yy, s, "g", "#FFFFFF" if n == "1" else TINTA, a)))
    E.frase(c, t, C["s11"] + 9.4 + 0.1, [("não", "i", 72), ("simplifica", "i", 72), ("mais", "i", 72)], XE + 30, 855, passo=0.24)
    E.frase(c, t, C["s11.b"], [("irredutível", "g", 130, COR)], 790, 870)


# ---------------- degrau a degrau ----------------
def b_degraus(c, t, C, b):
    def degraus():
        E.frase(c, t, C["s12"] + 0.35, [("voltando", "i", 88), ("à", "i", 88), ("do", "i", 88), ("começo", "g", 80, COR)], W / 2, 170, "center")
        s, cy, x0, x1, x2 = 150, 450, 340, 960, 1570
        fr(c, t, C["s12.a"], 18, 24, x0, cy, s)
        pontes(c, t, x0 + 135, x1 - 125, cy, s, "÷ 2", C["s12.b"], C["s12.b"])
        fr(c, t, C["s12.c"], 9, 12, x1, cy, s)
        pontes(c, t, x1 + 125, x2 - 180, cy, s, "÷ 3", C["s13.a"], C["s13.a"])
        E.resultado(c, t, C["s13.b"], 3, 4, x2, cy, 124, 162)
        fica(c, t, C["s12"] + 4.33, C["s13"] + 0.9, [("18", "g", 72), ("e", "i", 76), ("24", "g", 72), ("são", "i", 76), ("pares", "g", 72, COR)], W / 2, 800, "center", 0.17)
        fica(c, t, C["s13"] + 1.1, C["s13"] + 8.5, [("9", "g", 72), ("e", "i", 76), ("1 + 2 = 3", "g", 72), ("são", "i", 76), ("múltiplos", "i", 76), ("de", "i", 76), ("3", "g", 72, COR)],
             W / 2, 800, "center", 0.25)
        E.frase(c, t, C["s13"] + 8.65, [("funcionou,", "i", 84), ("mas", "i", 84), ("foram", "i", 84), ("2 passos", "g", 78, COR)], W / 2, 800, "center", 0.4)
    E.saida(c, t, C["s14"] - 0.1, degraus)
    if t < C["s14"]:
        return

    E.frase(c, t, C["s14"] + 0.35, [("em", "i", 104), ("um", "g", 96, COR), ("passo", "i", 104), ("só?", "i", 104)], W / 2, 180, "center")
    E.frase(c, t, C["s14.a"], [("divida", "i", 80), ("pelo", "i", 80), ("MDC", "g", 74, COR)], XE, 320)
    E.frase(c, t, C["s14.a"] + 1.7, [("o", "i", 64), ("maior", "i", 64), ("número", "i", 64), ("que", "i", 64), ("divide", "i", 64), ("os", "i", 64), ("dois", "i", 64)], 720, 320, passo=0.17)
    p = ep(t, C["s14"] + 6.31, 0.5)
    E.caixa_pontilhada(c, 700, 400, 520, 96, p, prog_=p)
    E.foco(c, t, C["s14"] + 6.31, 0.5, lambda a: E.escreve(c, "MDC(18, 24)", 732, 468, 60, "b", TINTA, a))
    E.foco(c, t, C["s14.b"], 0.4, lambda a: E.escreve(c, "= 6", 1100, 468, 60, "g", COR, a))
    s, cy, x0, x1 = 170, 690, 500, 1420
    fr(c, t, C["s14"] + 1.0, 18, 24, x0, cy, s)
    tn, td = C["s14"] + 11.17, C["s14"] + 14.25  # "três" e "quatro" na fala
    if t < C["s14"] + 15.4:
        frac_q(c, t, C["s14.b"], 3, 4, tn, td, x1, cy, s)
    E.resultado(c, t, C["s14"] + 15.37, 3, 4, x1, cy, 134, 176)
    ponte(c, t, C["s14.c"], x0 + 150, x1 - 190, cy - s * 0.565, "÷ 6", size=60)
    ponte(c, t, C["s14.d"], x0 + 150, x1 - 190, cy + s * 0.535, "÷ 6", size=60)
    y = 965
    E.foco(c, t, C["s14.c"], 0.4, lambda a: E.escreve(c, "18 ÷ 6", 500, y, 64, "b", TINTA2, a))
    E.foco(c, t, tn, 0.4, lambda a: E.escreve(c, "= 3", 730, y, 64, "g", COR, a))
    E.foco(c, t, C["s14.d"], 0.4, lambda a: E.escreve(c, "24 ÷ 6", 1120, y, 64, "b", TINTA2, a))
    E.foco(c, t, td, 0.4, lambda a: E.escreve(c, "= 4", 1350, y, 64, "g", COR, a))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    def alerta():
        E.frase(c, t, C["s15"] + 0.35, [("cuidado", "g", 110, ERRADO)], W / 2, 170, "center")
        E.frase(c, t, C["s15.a"] - 0.6, [("só", "i", 84), ("vale", "i", 84), ("multiplicar", "g", 76, COR), ("ou", "i", 84), ("dividir", "g", 76, COR)], W / 2, 300, "center", 0.3)
        E.frase(c, t, C["s15.b"] - 0.8, [("tem", "i", 76), ("gente", "i", 76), ("que", "i", 76), ("soma", "g", 70, ERRADO), ("em", "i", 76), ("cima", "i", 76), ("e", "i", 76), ("embaixo", "i", 76)],
                W / 2, 420, "center", 0.27)
        s, cy, x0, x1 = 150, 680, 620, 1300
        fr(c, t, C["s15.c"], 1, 2, x0, cy, s, COR)
        pontes(c, t, x0 + 110, x1 - 110, cy, s, "+ 1", C["s15"] + 9.07, C["s15"] + 9.07, ERRADO, 60)
        fr(c, t, C["s15.d"], 2, 3, x1, cy, s, ERRADO)
    E.saida(c, t, C["s16"] - 0.1, alerta)
    if t < C["s16"]:
        return

    E.frase(c, t, C["s16.a"], [("dois", "g", 82, ERRADO), ("terços", "g", 82, ERRADO), ("é", "i", 90), ("mais", "i", 90), ("que", "i", 90), ("metade", "i", 90)], W / 2, 175, "center", 0.18)
    x, w, h, y1, y2 = 480, 1140, 130, 260, 430
    E.foco(c, t, C["s16.a"] + 0.2, 0.5, lambda a: (barra(c, x, y1, w, h, 1 / 2, [(0.5, 1)], a), E.fracao(c, 1, 2, 320, y1 + h / 2, 76, COR, a)))
    E.foco(c, t, C["s16.a"] + 0.5, 0.5, lambda a: (barra(c, x, y2, w, h, 2 / 3, [(1 / 3, 1), (2 / 3, 1)], a, ERRADO),
                                                   E.fracao(c, 2, 3, 320, y2 + h / 2, 76, ERRADO, a)))
    p = ep(t, C["s16.a"] + 1.2, 0.5)
    M.line(c, x + w / 2, y1 - 16, x + w / 2, y2 + h + 16, TINTA, p, 5, dash=[14, 11], cap_round=False)
    E.frase(c, t, C["s16"] + 3.1, [("a", "i", 76), ("quantidade", "i", 76), ("mudou", "g", 70, ERRADO)], W / 2, 690, "center")
    E.frase(c, t, C["s16.b"], [("somar", "g", 76, ERRADO), ("não", "i", 84), ("mantém", "i", 84), ("a", "i", 84), ("fração", "i", 84)], W / 2, 830, "center", 0.3)
    E.frase(c, t, C["s16"] + 7.16, [("multiplicar", "g", 76, CERTO), ("e", "i", 84), ("dividir", "g", 76, CERTO), ("mantêm", "i", 84)], W / 2, 950, "center", 0.38)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    BR = "#FFFFFF"

    def titulo():
        E.frase(c, t, C["s17"] + 0.35, [("o", "i", 90, CLARO), ("atalho", "i", 90, CLARO), ("prometido", "i", 90, CLARO)], W / 2, 240, "center")
        E.frase(c, t, C["s17.a"], [("o", "i", 180, BR), ("teste", "i", 180, BR), ("da", "i", 180, BR), ("cruz", "g", 170, BR)], W / 2, 490, "center", 0.25)
        E.foco(c, t, C["s17"] + 3.87, 0.5, lambda a: E.pilula(c, "produto cruzado", W / 2, 640, 60, estilo="b", fundo=E.COR, cor=BR, a=a))
        E.frase(c, t, C["s17"] + 6.13, [("diz", "i", 76, CLARO), ("se", "i", 76, CLARO), ("duas", "i", 76, CLARO), ("frações", "i", 76, CLARO), ("são", "i", 76, CLARO), ("equivalentes", "g", 70, BR)],
                W / 2, 810, "center", 0.25)
        E.frase(c, t, C["s17"] + 8.43, [("sem", "i", 76, CLARO), ("simplificar", "g", 70, BR), ("nada", "i", 76, CLARO)], W / 2, 920, "center", 0.3)
    E.saida(c, t, C["s18"] - 0.1, titulo)
    if t < C["s18"]:
        return

    s, xa, xb, y = 190, 420, 990, 500
    fr(c, t, C["s18.a"], 2, 3, xa, y, s, BR)
    fr(c, t, C["s18.a"] + 1.2, 8, 12, xb, y, s, BR)
    E.frase(c, t, C["s18.a"] + 2.2, [("são", "i", 84, CLARO), ("equivalentes?", "g", 78, BR)], W / 2, 170, "center")
    ny, dy = y - s * 0.565, y + s * 0.535
    cruzes = ((xa + 70, ny + 10, xb - 130, dy - 10, "s18.b", "2 × 12 =", 300), (xa + 70, dy - 10, xb - 100, ny + 10, "s18.c", "3 × 8 =", 480))
    igual = t >= C["s18.d"]
    tx = 1210
    for x0, y0, x1, y1, k, txt, ty in cruzes:
        p = ep(t, C[k], 0.6)
        if p > 0:
            M.line(c, x0, y0, x1, y1, CERTO if igual else CLARO, 1.0, 8, progress=p)
        E.foco(c, t, C[k], 0.45, lambda a: E.escreve(c, txt, tx, ty + 130, 72, "b", BR, a))
        E.foco(c, t, C[k] + 1.2, 0.4, lambda a: E.escreve(c, "24", tx + 340, ty + 130, 84, "g", CLARO if not igual else CERTO, a))
    r = 62
    c.drawCircle((xa + xb) / 2, y, r, M.paint("#0A0820"))
    if not igual:
        sinal(c, t, C["s18.a"] + 0.6, "?", (xa + xb) / 2, y - 3, 110, CLARO)
    else:
        sinal(c, t, C["s18.d"], "=", (xa + xb) / 2, y - 3, 110, CERTO)
    E.frase(c, t, C["s18.d"], [("deu", "i", 84, BR), ("igual,", "i", 84, BR), ("são", "i", 84, BR), ("equivalentes", "g", 78, CERTO)], W / 2, 850, "center", 0.3)
    E.frase(c, t, C["s18"] + 12.37, [("deu", "i", 66, CLARO), ("diferente,", "i", 66, CLARO), ("não", "g", 60, ERRADO), ("são", "g", 60, ERRADO)], W / 2, 960, "center", 0.3)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s19"] + 0.3, [("hora", "i", 76, COR), ("de", "i", 76, COR), ("testar", "i", 76, COR)], XE, 190)
    E.frase(c, t, C["s19.a"] - 0.5, [("simulado", "i", 88), ("de", "i", 88), ("40", "g", 100, COR), ("questões", "i", 88)], XE, 370, passo=0.25)
    E.frase(c, t, C["s19.b"] - 0.4, [("acertou", "i", 88), ("30", "g", 100, COR)], XE, 520, passo=0.4)
    E.frase(c, t, C["s19.c"], [("que", "i", 116), ("fração", "i", 116, COR), ("ela", "i", 116), ("acertou?", "g", 108)], XE, 770, passo=0.25)
    E.frase(c, t, C["s19"] + 7.65, [("na", "i", 84), ("forma", "i", 84), ("mais", "i", 84), ("simples", "g", 76, COR)], XE, 900, passo=0.2)
    # relógio de pausa: enche em 3 segundos
    t0 = C["s20.a"]
    r = 190 * ease_back(prog(t, t0, 0.6))
    if r > 0:
        cx, cy = 1490, 340
        E.bola(c, cx, cy, r)
        f = M.clamp(prog(t, t0 + 0.8, 3.0))
        if f > 0:
            E.arco(c, cx, cy, r + 34, -90, 360 * f, TINTA, 10)
        for dx in (-40, 40):
            M.rrect(c, cx + dx - 20, cy - 72, 40, 144, 11, "#FFFFFF", ep(t, t0 + 0.2, 0.4))
        E.foco(c, t, t0 + 0.2, 0.5, lambda a: E.escreve(c, "pause o vídeo", cx - E.larg("pause o vídeo", "i", 60) / 2, cy + r + 104, 60, "i", TINTA, a))


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    C21 = C["s21"]
    s, cy, x0, x1 = 130, 280, 420, 1030
    fr(c, t, C["s21.a"], 30, 40, x0, cy, s)
    E.foco(c, t, C21 + 3.65, 0.4, lambda a: E.escreve(c, "acertos", 130, cy - s * 0.565 + 18, 56, "i", COR, a))
    E.foco(c, t, C21 + 4.95, 0.4, lambda a: E.escreve(c, "total", 190, cy + s * 0.535 + 18, 56, "i", TINTA, a))
    pontes(c, t, x0 + 115, x1 - 170, cy, s, "÷ 10", C["s21.c"], C["s21.d"], size=52)
    tn, td = C21 + 11.65, C21 + 14.25  # "três" e "quatro" na fala
    if t < C["s21.e"]:
        frac_q(c, t, C["s21.c"], 3, 4, tn, td, x1, cy, s)
    E.resultado(c, t, C["s21.e"], 3, 4, x1, cy, 112, 150, CERTO)
    p = ep(t, C21 + 6.45, 0.5)
    xm = 1200
    E.caixa_pontilhada(c, xm, 150, 540, 96, p, prog_=p)
    E.foco(c, t, C21 + 6.45, 0.5, lambda a: E.escreve(c, "MDC(30, 40)", xm + 24, 216, 54, "b", TINTA, a))
    E.foco(c, t, C["s21.b"], 0.4, lambda a: E.escreve(c, "= 10", xm + 370, 216, 54, "g", COR, a))
    E.frase(c, t, C["s21.e"] + 0.4, [("da", "i", 84, CERTO), ("prova", "g", 78, CERTO)], xm + 10, 350)

    # a mesma barra: 40 pedaços com 30 pintados viram 4 pedaços com 3 pintados
    x, w, y, h = 300, 1320, 590, 170
    junta = 1 - ep(t, C["s21.d"] + 2.4, 0.8)
    cortes = [(i / 40, 1 if i % 10 == 0 else junta) for i in range(1, 40)]
    E.foco(c, t, C21 + 0.35, 0.5, lambda a: barra(c, x, y, w, h, 0.75, cortes, a, largura=3, enche=ep(t, C["s21.a"] + 0.5, 0.8)))
    E.saida(c, t, C["s21.d"] + 2.3, lambda: E.foco(c, t, C["s21.a"] + 0.7, 0.45, lambda a: centro(c, "30 de 40 questões", W / 2, y + h + 96, 64, "b", COR, a)))
    if t >= C["s21.d"] + 2.7:
        E.foco(c, t, C["s21.d"] + 2.7, 0.45, lambda a: centro(c, "3 de 4: a mesma parte da prova", W / 2, y + h + 96, 64, "b", CERTO, a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s22"] + 0.35, [("resumindo", "i", 92, COR)], W / 2, 190, "center")
        ball = lambda i, y, a: (E.bola(c, 460, y, 56, a=a), E.escreve(c, str(i), 460 - E.larg(str(i), "g", 64) / 2, y + 23, 64, "g", "#FFFFFF", a))
        E.foco(c, t, C["s22.a"], 0.5, lambda a: ball(1, 370, a))
        E.frase(c, t, C["s22.a"] + 0.1, [("×", "g", 84, COR), ("ou", "i", 88), ("÷", "g", 84, COR), ("em", "i", 88), ("cima", "i", 88), ("e", "i", 88), ("embaixo", "i", 88)], 560, 400, passo=0.2)
        E.frase(c, t, C["s22.a"] + 2.2, [("pelo", "i", 88), ("mesmo", "i", 88), ("número", "i", 88)], 560, 510, passo=0.2)
        E.frase(c, t, C["s22.a"] + 3.3, [("não", "i", 88), ("muda", "g", 80, COR), ("a", "i", 88), ("fração", "i", 88)], 560, 620, passo=0.2)
        E.foco(c, t, C["s22.b"], 0.5, lambda a: ball(2, 760, a))
        E.frase(c, t, C["s22.b"] + 0.3, [("MDC", "g", 96, COR), ("simplifica", "i", 96)], 560, 790, passo=0.4)
        E.frase(c, t, C["s22.b"] + 1.3, [("em", "i", 96), ("um", "g", 88), ("passo", "i", 96), ("só", "i", 96)], 560, 900, passo=0.2)
    E.saida(c, t, C["s23"] - 0.1, resumo)
    if t < C["s23"]:
        return
    E.frase(c, t, C["s23"] + 0.6, [("próxima", "i", 84), ("aula", "i", 84)], XE, 330)
    E.frase(c, t, C["s23.a"], [("Frações", "g", 130, COR), ("maiores", "g", 130, COR)], XE, 490)
    E.frase(c, t, C["s23.a"] + 0.9, [("que", "i", 120), ("1", "g", 130, COR), ("e", "i", 120), ("número", "g", 130, COR), ("misto", "g", 130, COR)], XE, 640)
    E.foco(c, t, C["s23.b"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1430, 310, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s23.b"] + 0.3, 0.8))
    E.cursor(c, lerp(1760, 1560, p), lerp(560, 335, p), ep(t, C["s23.b"] + 0.2, 0.4))
    E.frase(c, t, C["s23.c"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 880, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, barras=b_barras, regra=b_regra, simplificar=b_simplificar, degraus=b_degraus,
              erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
