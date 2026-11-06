"""Visual — Estudativo · MAT-FRA-007: somar e subtrair com denominadores iguais.
Identidade em _ferramentas/editorial.py. A barra de chocolate é a animação central: todos os pedaços têm a mesma escala e a
soma acontece à vista. Azul = a primeira parte, preto = a segunda, vermelho = erro, verde = certo.
Peças só desta aula: fr2, maca, dedo."""
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, fr, sinal, palco, tablete, chocolate, chave, centro
import motor as M
import skia

E.usar("Matemática", "Frações e Decimais")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-FRA-007_somar_fracoes_denominadores_iguais.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("barra", "exemplos", "inteiro", "atalho", "questao"))
BR = E.SOBRE


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças desta aula ----------------
def fr2(c, n, d, cx, cy, size, corn, cord, a=1.0):
    """fração com o número de baixo em outra cor"""
    E.fracao(c, n, d, cx, cy, size, corn, a)
    centro(c, str(d), cx, cy + size * 0.9, size, "g", cord, a)


def maca(c, cx, cy, r, cor, a=1.0):
    """maçã: todas com o mesmo tamanho, para a soma ficar à vista"""
    M.line(c, cx, cy - r * 0.82, cx + r * 0.12, cy - r * 1.32, TINTA2, a, r * 0.13)
    folha = skia.Path()
    folha.moveTo(cx + r * 0.12, cy - r * 1.0)
    folha.quadTo(cx + r * 0.55, cy - r * 1.5, cx + r * 0.95, cy - r * 1.18)
    folha.quadTo(cx + r * 0.55, cy - r * 0.86, cx + r * 0.12, cy - r * 1.0)
    c.drawPath(folha, M.paint(cor, a))
    E.bola(c, cx, cy, r, cor, a)


def dedo(c, cx, y, w=170):
    """dedo que tampa o denominador: sobe da borda de baixo, com a unha para cima"""
    pele = E.mix(CLARO, "#FFFFFF", 0.45)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2, y, w, H + 200 - y), w * 0.46, w * 0.46), M.paint(pele))
    un = w * 0.68
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - un / 2, y + w * 0.1, un, un * 1.1), un * 0.42, un * 0.42), M.paint("#FFFFFF", 0.85))
    for dy in (w * 1.32, w * 1.46):
        M.line(c, cx - w * 0.3, y + dy, cx + w * 0.3, y + dy, CLARO, 0.8, 4)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    s1, s2 = C["s01"], C["s02"]

    def conta():
        y = 430
        fr(c, t, C["s01.a"], 2, 7, 430, y, 230)
        p = ease_back(prog(t, C["s01.b"] - 0.1, 0.55))
        if p > 0:
            E.mais(c, 695, y, 92 * p, giro=(1 - p) * 90)
        fr(c, t, C["s01.b"] + 0.28, 3, 7, 950, y, 230)
        sinal(c, t, C["s01.c"] - 0.2, "=", 1195, y, 190)
        fr(c, t, C["s01.c"], 5, 14, 1490, y, 230, ERRADO if t > C["s01.c"] + 0.9 else None)
        if t > s1 + 7.6:
            E.risco(c, 1310, 590, 1670, 270, t, s1 + 7.6, largura=20)
        E.saida(c, t, s1 + 6.4, lambda: E.frase(c, t, s1 + 3.2, [("se", "i", 84), ("a", "i", 84), ("sua", "i", 84), ("resposta", "i", 84), ("foi...", "i", 84)],
                                                 W / 2, 870, "center", passo=0.16))
        E.frase(c, t, s1 + 6.6, [("uma", "i", 90), ("coisa", "i", 90), ("que", "i", 90), ("não", "g", 80, ERRADO), ("se", "i", 90), ("soma", "g", 80, ERRADO)],
                W / 2, 870, "center", passo=0.17)
    E.saida(c, t, s2 - 0.05, conta)

    def boa():
        E.frase(c, t, s2 + 0.3, [("a", "i", 84, COR), ("boa", "i", 84, COR), ("notícia", "i", 84, COR)], W / 2, 300, "center", passo=0.15)
        E.frase(c, t, s2 + 1.8, [("a", "i", 104), ("regra", "i", 104), ("certa", "i", 104), ("tem", "i", 104)], W / 2, 450, "center", passo=0.17)
        E.frase(c, t, C["s02.a"], [("só", "i", 190), ("duas", "g", 170, COR), ("partes", "g", 170, COR)], W / 2, 690, "center", passo=0.16)
    if t >= s2:
        E.saida(c, t, s2 + 4.0, boa)

    if t >= s2 + 4.0:
        E.frase(c, t, s2 + 4.2, [("até", "i", 96), ("o", "i", 96), ("fim", "i", 96), ("da", "i", 96), ("aula", "i", 96)], XE, 300, passo=0.16)
        E.frase(c, t, s2 + 6.3, [("somar", "g", 132)], XE, 460)
        E.frase(c, t, s2 + 7.3, [("subtrair", "g", 132)], XE, 610)
        E.frase(c, t, s2 + 8.2, [("e", "i", 96), ("descobrir", "i", 96, COR)], XE, 740)
        p = ease_back(prog(t, C["s02.b"] - 0.2, 0.7))
        if p > 0:
            E.bola(c, 1370, 510, 320 * p)
        E.foco(c, t, C["s02.b"] + 0.1, 0.5, lambda a: (centro(c, "quanto", 1370, 440, 100, "g", BR, a), centro(c, "falta para", 1370, 540, 100, "i", BR, a),
                                                      centro(c, "1 inteiro", 1370, 660, 100, "g", BR, a)))


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    s3 = C["s03"]
    E.frase(c, t, s3 + 0.3, [("só", "i", 80), ("precisa", "i", 80), ("lembrar", "i", 80), ("de", "i", 80), ("uma", "g", 72, COR), ("coisa", "g", 72, COR)], XE, 170, passo=0.15)
    cx, cy, s = 430, 510, 300
    den = ep(t, C["s03.a"], 0.4)
    num = ep(t, C["s03.b"], 0.4)
    E.foco(c, t, s3 + 0.5, 0.6, lambda a: fr2(c, 2, 7, cx, cy, s, E.mix(TINTA, COR, num), E.mix(TINTA, COR, den * (1 - num)), a))
    # denominador: as partes iguais da barra
    if t >= C["s03.a"]:
        p = ep(t, C["s03.a"], 0.5)
        M.arrow(c, 590, 700, 760, 470, COR if t < C["s03.b"] else FIO, p, 4, 16, p)
    E.frase(c, t, C["s03.a"], [("denominador", "g", 82, COR)], 800, 470)
    E.frase(c, t, s3 + 3.5, [("o", "i", 66), ("número", "i", 66), ("de", "i", 66), ("baixo", "i", 66)], 800, 544, passo=0.12)
    E.frase(c, t, s3 + 4.8, [("partes", "g", 58), ("iguais", "g", 58), ("do", "i", 66), ("inteiro", "i", 66)], 800, 622, passo=0.16)
    # numerador: quantas você pegou
    if t >= C["s03.b"]:
        p = ep(t, C["s03.b"], 0.5)
        M.arrow(c, 590, 320, 760, 250, COR, p, 4, 16, p)
    E.frase(c, t, C["s03.b"], [("numerador", "g", 82, COR)], 800, 270)
    E.frase(c, t, s3 + 10.2, [("o", "i", 66), ("de", "i", 66), ("cima:", "i", 66), ("as", "i", 66), ("partes", "g", 58), ("que", "i", 66), ("pegou", "i", 66)], 800, 350, passo=0.13)
    # a barra acompanha: corta em 7 e pinta 2
    bx, by, bw, bh = 800, 680, 930, 130
    q = ep(t, s3 + 5.8, 0.5)
    chocolate(c, bx, by, bw, bh, 7, ((0, COR, prog(t, s3 + 11.1, 0.4)), (1, COR, prog(t, s3 + 11.3, 0.4))), q, ep(t, s3 + 6.0, 0.9))
    E.foco(c, t, s3 + 13.8, 0.5, lambda a: E.pilula(c, "aula no canal: o que é uma fração", W / 2, 950, 50, a=a, cor=BR))


# ---------------- a barra de chocolate ----------------
BX, BW, BY, BH = 260, 1400, 300, 200


def b_barra(c, t, C, b):
    s4, s5, s6 = C["s04"], C["s05"], C["s06"]
    lp = BW / 7
    E.saida(c, t, s5 - 0.3, lambda: E.frase(c, t, s4 + 0.3, [("imagine", "i", 84), ("uma", "i", 84), ("barra", "i", 84), ("de", "i", 84), ("chocolate", "g", 76, COR)],
                                             W / 2, 190, "center", passo=0.17))
    E.saida(c, t, s6 - 0.1, lambda: E.frase(c, t, s5 + 3.5, [("quantos", "i", 84), ("pedaços", "i", 84), ("comeu?", "g", 76, COR)], W / 2, 190, "center", passo=0.17))

    ped = []
    if C["s04.c"] <= t < C["s05.a"] + 0.35:
        ped.append((0, CLARO, prog(t, C["s04.c"], 0.4)))
    ped += [(i, COR, prog(t, C["s05.a"] + i * 0.22, 0.4)) for i in (0, 1)]
    ped += [(i, TINTA, prog(t, C["s05.b"] + (i - 2) * 0.22, 0.4)) for i in (2, 3, 4)]
    chocolate(c, BX, BY, BW, BH, 7, ped, ep(t, C["s04.a"], 0.5), ep(t, C["s04.b"] - 0.1, 0.9))

    # numeração dos pedaços: primeiro por grupo; no "cinco pedaços", a contagem corrida
    for i in range(5):
        cx = BX + lp * (i + 0.5)
        t0 = C["s05.a"] + i * 0.22 if i < 2 else C["s05.b"] + (i - 2) * 0.22
        tc = C["s06.a"] - 0.15 + i * 0.13
        if t < tc:
            E.foco(c, t, t0 + 0.1, 0.3, lambda a, i=i: centro(c, str(i + 1 if i < 2 else i - 1), cx, BY + 130, 92, "g", BR, a), sobe=0, blur=6)
        else:
            E.foco(c, t, tc, 0.25, lambda a, i=i: centro(c, str(i + 1), cx, BY + 130, 92, "g", BR, a), sobe=0, blur=6)

    # um pedaço = um sétimo
    def um():
        chave(c, BX + 8, BX + lp - 8, BY + BH + 16, COR, ep(t, C["s04.c"], 0.4))
        E.foco(c, t, C["s04.c"] + 0.1, 0.5, lambda a: E.fracao(c, 1, 7, BX + lp / 2, 680, 120, COR, a))
        E.frase(c, t, C["s04.c"] + 0.4, [("cada", "i", 76), ("pedaço", "i", 76), ("é", "i", 76), ("um", "i", 76), ("sétimo", "g", 68, COR)], BX + lp + 40, 695, passo=0.14)
    E.saida(c, t, C["s05.a"] - 0.15, um)

    yc = BY + BH + 16

    def grupos():
        chave(c, BX + 8, BX + lp * 2 - 8, yc, COR, ep(t, C["s05.a"], 0.4))
        chave(c, BX + lp * 2 + 8, BX + lp * 5 - 8, yc, TINTA, ep(t, C["s05.b"], 0.4))
        E.foco(c, t, C["s05.a"] + 0.1, 0.4, lambda a: centro(c, "2 pedaços", BX + lp, yc + 86, 60, "i", COR, a))
        E.foco(c, t, C["s05.b"] + 0.1, 0.4, lambda a: centro(c, "mais 3", BX + lp * 3.5, yc + 86, 60, "i", TINTA, a))
    E.saida(c, t, C["s06.a"] - 0.1, grupos, d=0.3)
    chave(c, BX + 8, BX + lp * 5 - 8, yc, COR, ep(t, C["s06.a"] + 0.2, 0.45))
    E.foco(c, t, C["s06.a"] + 0.3, 0.4, lambda a: centro(c, "5 pedaços", BX + lp * 2.5, yc + 90, 66, "g", COR, a))

    # a conta acompanha os pedaços
    y, s = 770, 110
    cd = E.mix(TINTA, COR, ep(t, C["s06.c"], 0.4))
    E.foco(c, t, C["s05.a"] + 0.2, 0.5, lambda a: fr2(c, 2, 7, 430, y, s, COR, COR, a))
    sinal(c, t, C["s05.b"] - 0.2, "+", 600, y, 90)
    E.foco(c, t, C["s05.b"] + 0.2, 0.5, lambda a: fr2(c, 3, 7, 770, y, s, TINTA, cd, a))
    sinal(c, t, s5 + 3.5, "=", 945, y, 90)
    E.saida(c, t, C["s06.b"] - 0.1, lambda: sinal(c, t, s5 + 3.7, "?", 1130, y, 130, CINZA), d=0.25)
    E.foco(c, t, C["s06.b"], 0.5, lambda a: (E.bola(c, 1130, y + 3, 136, a=a), E.fracao(c, 5, 7, 1130, y, 106, BR, a)))

    # o denominador não muda
    p = ep(t, s6 + 4.9, 0.5)
    chave(c, BX, BX + BW, BY - 16, COR, p, h=-22)
    E.foco(c, t, s6 + 5.1, 0.5, lambda a: centro(c, "continua cortada em 7", W / 2, BY - 60, 70, "i", TINTA, a))
    E.frase(c, t, C["s06.c"], [("o", "i", 76), ("denominador", "g", 68, COR), ("não", "i", 76), ("mudou", "i", 76)], W / 2, 970, "center", passo=0.15)


# ---------------- regra ----------------
def b_regra(c, t, C, b):
    s7, s8 = C["s07"], C["s08"]

    def regra():
        E.frase(c, t, s7 + 0.3, [("essa", "i", 100), ("é", "i", 100), ("toda", "i", 100), ("a", "i", 100), ("regra", "g", 90, COR)], W / 2, 220, "center", passo=0.17)
        E.frase(c, t, C["s07.a"], [("soma", "g", 96, COR), ("os", "i", 104), ("de", "i", 104), ("cima", "i", 104)], XE, 530, passo=0.16)
        E.frase(c, t, C["s07.b"], [("repete", "g", 96), ("o", "i", 104), ("de", "i", 104), ("baixo", "i", 104)], XE, 730, passo=0.14)
        cx, y, s = 1130, 575, 170
        E.foco(c, t, C["s07.a"], 0.5, lambda a: E.fracao(c, "2 + 3", " ", cx, y, s, COR, a))
        E.foco(c, t, C["s07.b"], 0.5, lambda a: centro(c, "7", cx, y + s * 0.9, s, "g", TINTA, a))
        sinal(c, t, C["s07.b"] + 0.5, "=", 1425, y, 130)
        E.foco(c, t, C["s07.b"] + 0.7, 0.5, lambda a: fr2(c, 5, 7, 1590, y, s, COR, TINTA, a))
    E.saida(c, t, s8 - 0.1, regra)
    if t < s8:
        return

    E.frase(c, t, s8 + 0.3, [("pense", "i", 80, COR), ("assim", "i", 80, COR)], XE, 150, passo=0.15)
    xs = {"a": (315, 435), "b": (655, 775, 895), "r": (1125, 1245, 1365, 1485, 1605)}
    tb, tr = s8 + 2.4, C["s08.b"]
    y1, y2, r = 290, 640, 52
    cores_r = (COR, COR, TINTA, TINTA, TINTA)

    def linha(y, desenha, ta, tb_, tr_, rot, passo_=0.15):
        for i, x in enumerate(xs["a"]):
            E.foco(c, t, ta + i * passo_, 0.4, lambda a, x=x: desenha(x, y, COR, a))
        sinal(c, t, tb_ - 0.2, "+", 545, y, 80)
        for i, x in enumerate(xs["b"]):
            E.foco(c, t, tb_ + i * passo_, 0.4, lambda a, x=x: desenha(x, y, TINTA, a))
        sinal(c, t, tr_ - 0.2, "=", 1015, y, 80)
        for i, x in enumerate(xs["r"]):
            E.foco(c, t, tr_ + i * passo_ * 0.6, 0.4, lambda a, x=x, i=i: desenha(x, y, cores_r[i], a))
        for tt, cx, s, cor in ((ta, 375, rot[0], COR), (tb_, 775, rot[1], TINTA), (tr_, 1365, rot[2], COR)):
            E.foco(c, t, tt + 0.2, 0.4, lambda a: centro(c, s, cx, y + 118, 56, "i", cor, a))

    t2 = s8 + 7.0
    c.save(); c.translate(0, lerp(170, 0, ep(t, t2 - 0.6, 0.6)))  # as maçãs ficam no meio até a segunda linha chegar
    linha(y1, lambda x, y, cor, a: maca(c, x, y, r, cor, a), C["s08.a"], tb, tr, ("2 maçãs", "3 maçãs", "5 maçãs"))
    E.frase(c, t, s8 + 4.6, [("a", "i", 72), ("maçã", "i", 72), ("não", "g", 64, COR), ("muda", "i", 72), ("de", "i", 72), ("tamanho", "i", 72)], W / 2, 500, "center", passo=0.13)
    c.restore()
    linha(y2, lambda x, y, cor, a: tablete(c, x - 54, y - 54, 108, 108, cor, a), t2, t2 + 0.25, t2 + 0.5, ("2 sétimos", "3 sétimos", "5 sétimos"), passo_=0.08)
    E.saida(c, t, C["s08.c"] - 0.15, lambda: E.frase(c, t, t2, [("o", "i", 76), ("sétimo", "g", 68, COR), ("também", "i", 76), ("não", "i", 76)], W / 2, 900, "center", passo=0.15), d=0.3)
    E.frase(c, t, C["s08.c"], [("ele", "i", 76), ("só", "i", 76), ("diz", "i", 76), ("o", "i", 76), ("tamanho", "g", 68, COR), ("do", "i", 76), ("pedaço", "i", 76)], W / 2, 900, "center", passo=0.13)


# ---------------- exemplos ----------------
def b_exemplos(c, t, C, b):
    s9, s10 = C["s09"], C["s10"]
    bx, by, bw, bh = 260, 700, 1400, 150

    def um():
        E.frase(c, t, s9 + 0.3, [("vamos", "i", 88, COR), ("treinar", "i", 88, COR)], W / 2, 190, "center")
        y, s = 450, 130
        fr(c, t, C["s09.a"], 3, 10, 520, y, s, COR)
        sinal(c, t, s9 + 2.3, "+", 720, y, 96)
        fr(c, t, s9 + 2.7, 4, 10, 920, y, s)
        sinal(c, t, C["s09.b"], "=", 1120, y, 96)
        E.foco(c, t, C["s09.c"], 0.5, lambda a: (E.bola(c, 1340, y + 3, 150, a=a), E.fracao(c, 7, 10, 1340, y, 118, BR, a)))
        ped = [(i, COR, prog(t, C["s09.a"] + 0.3 + i * 0.15, 0.4)) for i in range(3)]
        ped += [(i + 3, TINTA, prog(t, s9 + 2.9 + i * 0.15, 0.4)) for i in range(4)]
        chocolate(c, bx, by, bw, bh, 10, ped, ep(t, C["s09.a"], 0.5), ep(t, C["s09.a"], 0.6))
        E.foco(c, t, s9 + 4.2, 0.4, lambda a: centro(c, "3 + 4 = 7", 620, 960, 72, "g", COR, a))
        E.frase(c, t, s9 + 5.9, [("repete", "i", 76), ("o", "i", 76), ("10", "g", 70)], 900, 960, passo=0.12)
    E.saida(c, t, s10 - 0.1, um)
    if t < s10:
        return

    E.frase(c, t, s10 + 0.3, [("com", "i", 88), ("três", "g", 80, COR), ("frações,", "i", 88), ("é", "i", 88), ("igual", "i", 88)], W / 2, 190, "center", passo=0.17)
    y, s = 450, 120
    fr(c, t, C["s10.a"], 1, 11, 300, y, s, COR)
    sinal(c, t, s10 + 3.6, "+", 505, y, 84)
    fr(c, t, s10 + 3.7, 2, 11, 710, y, s)
    sinal(c, t, s10 + 5.0, "+", 915, y, 84)
    fr(c, t, s10 + 5.1, 3, 11, 1120, y, s, TINTA2)
    sinal(c, t, C["s10.b"] - 0.2, "=", 1310, y, 96)
    E.foco(c, t, C["s10.c"], 0.5, lambda a: (E.bola(c, 1525, y + 3, 145, a=a), E.fracao(c, 6, 11, 1525, y, 112, BR, a)))
    ped = [(0, COR, prog(t, C["s10.a"] + 0.3, 0.4))]
    ped += [(i + 1, TINTA, prog(t, s10 + 3.9 + i * 0.15, 0.4)) for i in range(2)]
    ped += [(i + 3, "#7A7A82", prog(t, s10 + 5.3 + i * 0.15, 0.4)) for i in range(3)]
    chocolate(c, bx, by, bw, bh, 11, ped, ep(t, C["s10.a"], 0.5), ep(t, C["s10.a"], 0.6))
    E.foco(c, t, s10 + 6.7, 0.4, lambda a: centro(c, "1 + 2 + 3 = 6", W / 2, 960, 72, "g", COR, a))


# ---------------- subtrair ----------------
def b_subtrair(c, t, C, b):
    s = C["s11"]
    E.frase(c, t, s + 0.3, [("com", "i", 84), ("subtração,", "g", 76, COR), ("a", "i", 84), ("ideia", "i", 84), ("é", "i", 84), ("a", "i", 84), ("mesma", "i", 84)],
            W / 2, 180, "center", passo=0.14)
    y, z = 420, 130
    fr(c, t, C["s11.a"], 5, 8, 560, y, z, COR)
    sinal(c, t, s + 3.5, "−", 760, y, 96)
    fr(c, t, s + 3.6, 2, 8, 960, y, z, ERRADO if t >= C["s11.c"] else None)
    sinal(c, t, s + 7.1, "=", 1160, y, 96)
    E.foco(c, t, C["s11.d"], 0.5, lambda a: (E.bola(c, 1370, y + 3, 150, a=a), E.fracao(c, 3, 8, 1370, y, 118, BR, a)))

    bx, by, bw, bh = 260, 660, 1400, 170
    lp = bw / 8
    tira = ep(t, C["s11.c"] + 0.1, 0.55)
    ped = [(i, COR, prog(t, C["s11.b"] + i * 0.12, 0.35)) for i in range(3)]
    if tira < 1:
        ped += [(i, ERRADO if t >= C["s11.c"] else COR, prog(t, C["s11.b"] + i * 0.12, 0.35) * (1 - tira), -120 * tira) for i in (3, 4)]
    chocolate(c, bx, by, bw, bh, 8, ped, ep(t, s + 0.6, 0.5), ep(t, s + 0.8, 0.7))
    yc = by + bh + 16
    chave(c, bx + lp * 3 + 8, bx + lp * 5 - 8, yc, ERRADO, ep(t, C["s11.c"], 0.4))
    E.foco(c, t, C["s11.c"] + 0.1, 0.4, lambda a: centro(c, "tirou 2", bx + lp * 4, yc + 90, 66, "g", ERRADO, a))
    chave(c, bx + 8, bx + lp * 3 - 8, yc, CERTO, ep(t, s + 7.1, 0.4))
    E.foco(c, t, s + 7.2, 0.4, lambda a: centro(c, "sobraram 3", bx + lp * 1.5, yc + 90, 66, "g", CERTO, a))


# ---------------- quanto falta para o inteiro ----------------
def b_inteiro(c, t, C, b):
    s12, s13 = C["s12"], C["s13"]
    bx, by, bw, bh = 230, 390, 1460, 190
    lp = bw / 9
    E.saida(c, t, C["s12.a"] - 0.15, lambda: E.frase(c, t, s12 + 0.3, [("a", "i", 76, COR), ("parte", "i", 76, COR), ("que", "i", 76, COR), ("mais", "i", 76, COR), ("aparece", "i", 76, COR), ("em", "i", 76, COR), ("problema", "i", 76, COR)],
                                              W / 2, 560, "center", passo=0.16), d=0.3)
    # a pergunta nasce no meio e sobe para abrir espaço para a barra
    q = ep(t, s12 + 5.3, 0.7)
    Y0, k = 560, lerp(1.0, 0.8, q)
    c.save(); c.translate(W / 2, lerp(Y0, 215, q)); c.scale(k, k); c.translate(-W / 2, -Y0)
    E.frase(c, t, C["s12.a"], [("quanto", "i", 120), ("falta", "g", 108, COR), ("para", "i", 120)], W / 2, 500, "center", passo=0.17)
    E.frase(c, t, C["s12.a"] + 0.7, [("completar", "i", 120), ("1", "g", 108, COR), ("inteiro?", "g", 108, COR)], W / 2, 640, "center", passo=0.17)
    c.restore()

    # 9/9 pintados; em "cinco nonos", 4 pedaços saem e sobram 5
    apaga = [ep(t, C["s13.a"] + (i - 5) * 0.08, 0.3) for i in range(9)]
    ped = [(i, COR, prog(t, C["s12.b"] + i * 0.09, 0.3)) for i in range(5)]
    ped += [(i, COR, prog(t, C["s12.b"] + i * 0.09, 0.3) * (1 - apaga[i])) for i in range(5, 9)]
    chocolate(c, bx, by, bw, bh, 9, ped, ep(t, s12 + 5.5, 0.5), ep(t, s12 + 5.6, 0.8))
    yc = by + bh + 16
    y, s = 790, 110

    def inteiro():
        chave(c, bx + 8, bx + bw - 8, yc, COR, ep(t, C["s12.b"] + 0.2, 0.5))
        E.foco(c, t, C["s12.b"] + 0.3, 0.5, lambda a: fr2(c, 9, 9, 760, y, s, COR, COR, a))
        sinal(c, t, C["s12.b"] + 0.7, "=", 930, y, 96)
        E.foco(c, t, C["s12.b"] + 0.9, 0.5, lambda a: E.escreve(c, "a barra inteira", 1010, y + 26, 84, "i", TINTA, a))
    E.saida(c, t, C["s13.a"] - 0.15, inteiro, d=0.3)

    chave(c, bx + 8, bx + lp * 5 - 8, yc, COR, ep(t, C["s13.a"], 0.4))
    E.foco(c, t, C["s13.a"] + 0.1, 0.5, lambda a: E.fracao(c, 5, 9, 450, y, s, COR, a))
    E.foco(c, t, C["s13.a"] + 0.3, 0.5, lambda a: E.escreve(c, "você tem", 530, y + 22, 66, "i", TINTA, a))
    chave(c, bx + lp * 5 + 8, bx + bw - 8, yc, CERTO, ep(t, s13 + 2.1, 0.4))
    E.foco(c, t, s13 + 2.1, 0.5, lambda a: E.caixa_pontilhada(c, bx + lp * 5 + 8, by + 10, lp * 4 - 16, bh - 20, a, CERTO))
    if t < C["s13.c"] - 0.1:
        E.foco(c, t, s13 + 2.2, 0.4, lambda a: centro(c, "?", bx + lp * 7, y + 40, 120, "g", CERTO, a))
    E.foco(c, t, C["s13.b"], 0.5, lambda a: centro(c, "9 − 5 = 4", 950, y + 26, 76, "g", COR, a))
    E.foco(c, t, C["s13.c"], 0.5, lambda a: (E.bola(c, 1510, y + 3, 136, CERTO, a), E.fracao(c, 4, 9, 1510, y, 104, BR, a)))
    E.foco(c, t, C["s13.c"] + 0.2, 0.5, lambda a: centro(c, "faltam", 1275, y + 26, 72, "i", CERTO, a))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    s14, s15 = C["s14"], C["s15"]
    bx, bw, bh = 430, 1200, 150
    lp7, lp14 = bw / 7, bw / 14
    meio = bx + bw / 2

    def conta():
        E.frase(c, t, s14 + 0.3, [("o", "i", 84), ("erro", "g", 76, ERRADO), ("do", "i", 84), ("começo", "i", 84)], W / 2, 170, "center", passo=0.15)
        y, s = 385, 130
        ver = ep(t, C["s14.a"], 0.4)
        E.foco(c, t, s14 + 0.8, 0.5, lambda a: fr2(c, 2, 7, 470, y, s, TINTA, E.mix(TINTA, ERRADO, ver), a))
        sinal(c, t, s14 + 1.0, "+", 640, y, 96)
        E.foco(c, t, s14 + 1.2, 0.5, lambda a: fr2(c, 3, 7, 810, y, s, TINTA, E.mix(TINTA, ERRADO, ver), a))
        sinal(c, t, C["s14.b"] - 0.2, "=", 985, y, 96)
        fr(c, t, C["s14.b"], 5, 14, 1190, y, s, ERRADO)
        E.foco(c, t, C["s14.a"] + 0.3, 0.4, lambda a: E.escreve(c, "7 + 7 = 14", 1360, y + 118, 56, "b", ERRADO, a))
        E.foco(c, t, C["s14.a"], 0.4, lambda a: E.escreve(c, "somou", 1360, y - 40, 66, "i", ERRADO, a))
        E.foco(c, t, C["s14.a"] + 0.15, 0.4, lambda a: E.escreve(c, "os de baixo", 1360, y + 30, 66, "i", ERRADO, a))
    E.saida(c, t, s15 - 0.1, conta)

    # a barra de catorze entra na fala e sobe para dar lugar à de sete
    sobe = ep(t, s15, 0.6)
    y14 = lerp(640, 560, sobe)
    t14 = s14 + 6.8
    ped = [(i, ERRADO, prog(t, t14 + 0.3 + i * 0.12, 0.35)) for i in range(5)]
    chocolate(c, bx, y14, bw, bh, 14, ped, ep(t, t14, 0.5), ep(t, t14 + 0.1, 0.6))
    E.foco(c, t, t14, 0.5, lambda a: E.fracao(c, 5, 14, 290, y14 + 70, 72, ERRADO, a))
    E.saida(c, t, s15 - 0.1, lambda: E.frase(c, t, s14 + 9.2, [("pedaços", "i", 84), ("bem", "i", 84), ("menores", "g", 76, ERRADO)], W / 2, 900, "center", passo=0.2))

    if t < s15:
        return
    E.frase(c, t, s15 + 0.3, [("olhe", "i", 84), ("para", "i", 84), ("a", "i", 84), ("barra", "i", 84)], XE, 180, passo=0.15)
    y7 = 330
    ped7 = [(i, COR, prog(t, C["s15.a"] + 0.1 + i * 0.12, 0.35)) for i in range(5)]
    chocolate(c, bx, y7, bw, bh, 7, ped7, ep(t, C["s15.a"], 0.5), ep(t, C["s15.a"], 0.5))
    E.foco(c, t, C["s15.a"], 0.5, lambda a: E.fracao(c, 5, 7, 290, y7 + 70, 72, COR, a))
    # a metade vale para as duas barras: é a mesma escala
    p = ep(t, s15 + 3.3, 0.5)
    M.line(c, meio, 300, meio, lerp(300, 742, p), TINTA, p, 4, dash=[14, 10])
    E.foco(c, t, s15 + 3.4, 0.4, lambda a: E.pilula(c, "metade", meio, 265, 42, estilo="b", fundo=TINTA, cor=BR, a=a))
    chave(c, bx + 6, bx + lp14 * 7 - 6, 725, ERRADO, ep(t, s15 + 7.4, 0.4), h=18, largura=4)
    E.foco(c, t, s15 + 7.5, 0.4, lambda a: centro(c, "metade seria 7", bx + lp14 * 3.5, 806, 58, "i", ERRADO, a))

    def duas():
        E.frase(c, t, s15 + 3.0, [("5", "g", 64, COR), ("de", "i", 70), ("7", "g", 64, COR), ("passam", "i", 70), ("da", "i", 70), ("metade", "g", 64, COR)], 1000, 800, passo=0.1)
        E.frase(c, t, C["s15.b"], [("5", "g", 64, ERRADO), ("de", "i", 70), ("14", "g", 64, ERRADO), ("não", "i", 70), ("chegam", "i", 70)], 1000, 890, passo=0.38)
    E.saida(c, t, s15 + 8.4, duas, d=0.3)
    E.frase(c, t, s15 + 8.5, [("você", "i", 78), ("comeu", "i", 78), ("mais", "g", 70, COR), ("da", "i", 78), ("metade", "i", 78)], W / 2, 900, "center", passo=0.14)
    E.frase(c, t, s15 + 10.5, [("e", "i", 78), ("a", "i", 78), ("conta", "i", 78), ("diz", "i", 78), ("menos", "g", 70, ERRADO)], W / 2, 990, "center", passo=0.14)
    if t >= s15 + 12.6:
        E.risco(c, 215, y14 + 145, 365, y14 - 15, t, s15 + 12.6, largura=12)
    E.foco(c, t, s15 + 11.8, 0.5, lambda a: E.pilula(c, "sinal claro de erro", 1380, 175, 58, estilo="g", fundo=ERRADO, cor=BR, a=a))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    s16, s17 = C["s16"], C["s17"]

    def primeiro():
        E.frase(c, t, s16 + 0.3, [("por", "i", 90, CLARO), ("fim,", "i", 90, CLARO), ("dois", "g", 80, BR), ("atalhos", "g", 80, BR)], W / 2, 170, "center", passo=0.17)
        E.foco(c, t, C["s16.a"], 0.5, lambda a: (E.bola(c, XE + 50, 300, 50, a=a), centro(c, "1", XE + 50, 322, 62, "g", BR, a)))
        E.frase(c, t, s16 + 3.5, [("tampe", "g", 84, BR), ("o", "i", 92, CLARO), ("denominador", "g", 84, BR)], XE + 130, 330, passo=0.15)
        y, s = 640, 170
        for n, x in ((2, 450), (3, 910)):
            fr(c, t, s16 + 2.6, n, 7, x, y, s, BR)
        sinal(c, t, s16 + 2.8, "+", 680, y, 120, BR)
        sinal(c, t, s16 + 5.9, "=", 1150, y, 120, BR)
        E.foco(c, t, s16 + 6.2, 0.5, lambda a: E.fracao(c, 5, " ", 1400, y, s, CLARO, a))
        E.foco(c, t, s16 + 7.1, 0.5, lambda a: centro(c, "7", 1400, y + s * 0.9, s, "g", CLARO, a))
        sai = ease_io(prog(t, s16 + 7.0, 0.5))
        for x, d in ((450, 0.0), (910, 0.12)):
            ent = ease_io(prog(t, s16 + 3.5 + d, 0.55))
            if ent > 0 and sai < 1:
                dedo(c, x, lerp(H + 40, 654, ent) + (H + 40 - 654) * sai)
        E.frase(c, t, s16 + 5.2, [("só", "i", 76, CLARO), ("os", "i", 76, CLARO), ("de", "i", 76, CLARO), ("cima:", "i", 76, CLARO), ("2 + 3 = 5", "g", 70, BR)], XE + 130, 430, passo=0.13)
        E.foco(c, t, s16 + 7.7, 0.4, lambda a: E.pilula(c, "pronto!", 1640, 640, 52, estilo="g", fundo=COR, cor=BR, a=a))
    if t < s17:
        E.saida(c, t, s17 - 0.15, primeiro)

    if t < s17 - 0.1:
        return
    q = ep(t, C["s17.b"] - 0.5, 0.5)
    k = lerp(1.35, 1.0, q)
    c.save(); c.translate(XE, lerp(540, 240, q)); c.scale(k, k); c.translate(-XE, -240)
    E.foco(c, t, C["s17.a"], 0.5, lambda a: (E.bola(c, XE + 50, 190, 50, a=a), centro(c, "2", XE + 50, 212, 62, "g", BR, a)))
    E.frase(c, t, s17 + 1.5, [("de", "i", 86, CLARO), ("cima", "g", 76, BR), ("igual", "i", 86, CLARO), ("ao", "i", 86, CLARO), ("de", "i", 86, CLARO), ("baixo", "g", 76, BR)], XE + 130, 195, passo=0.13)
    E.frase(c, t, s17 + 4.0, [("deu", "i", 86, CLARO), ("um", "i", 86, CLARO), ("inteiro", "g", 76, BR)], XE + 130, 290, passo=0.13)
    c.restore()
    y, s = 500, 120
    fr(c, t, C["s17.b"], 3, 7, 400, y, s, CLARO)
    sinal(c, t, s17 + 6.4, "+", 560, y, 90, BR)
    fr(c, t, s17 + 6.5, 4, 7, 720, y, s, BR)
    sinal(c, t, C["s17.c"] - 0.2, "=", 885, y, 90, BR)
    fr(c, t, C["s17.c"], 7, 7, 1050, y, s, BR)
    sinal(c, t, C["s17.d"] - 0.3, "=", 1220, y, 90, BR)
    E.foco(c, t, C["s17.e"], 0.5, lambda a: (E.bola(c, 1430, y + 3, 130, a=a), centro(c, "1", 1430, y + 50, 150, "g", BR, a)))
    bx, by, bw, bh = 260, 700, 1400, 170
    ped = [(i, CLARO, prog(t, C["s17.b"] + 0.2 + i * 0.13, 0.35)) for i in range(3)]
    ped += [(i + 3, "#FFFFFF", prog(t, s17 + 6.7 + i * 0.13, 0.35)) for i in range(4)]
    chocolate(c, bx, by, bw, bh, 7, ped, ep(t, C["s17.b"], 0.4), 1.0, escuro=True)
    chave(c, bx, bx + bw, by + bh + 16, CLARO, ep(t, C["s17.d"], 0.5))
    E.foco(c, t, C["s17.d"] + 0.1, 0.4, lambda a: centro(c, "a barra inteira", W / 2, by + bh + 104, 64, "i", BR, a))


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    s = C["s18"]
    E.frase(c, t, s + 0.3, [("hora", "i", 72, COR), ("de", "i", 72, COR), ("testar", "i", 72, COR)], XE, 190)
    E.frase(c, t, s + 2.4, [("pagou", "i", 92)], XE, 380)
    E.foco(c, t, C["s18.a"], 0.5, lambda a: E.fracao(c, 2, 5, 505, 345, 88, COR, a))
    E.frase(c, t, s + 3.4, [("da", "i", 92), ("dívida", "g", 76), ("no", "i", 92), ("1º", "g", 76), ("mês", "i", 92)], 590, 380, passo=0.13)
    E.frase(c, t, s + 4.7, [("e", "i", 92)], XE + 240, 580)
    E.foco(c, t, C["s18.b"], 0.5, lambda a: E.fracao(c, 1, 5, 505, 545, 88, TINTA, a))
    E.frase(c, t, s + 5.5, [("no", "i", 92), ("2º", "g", 76), ("mês", "i", 92)], 590, 580, passo=0.1)
    E.frase(c, t, C["s18.c"], [("que", "i", 112), ("fração", "i", 112), ("ainda", "i", 112), ("falta", "g", 100, COR), ("pagar?", "g", 100, COR)], XE, 850, passo=0.3)
    # relógio de pausa: enche em 3 segundos
    t0 = C["s19.a"]
    r = 190 * ease_back(prog(t, t0, 0.6))
    if r > 0:
        cx, cy = 1520, 400
        E.bola(c, cx, cy, r)
        f = M.clamp(prog(t, t0 + 0.8, 3.0))
        if f > 0:
            E.arco(c, cx, cy, r + 30, -90, 360 * f, TINTA, 10)
        for dx in (-40, 40):
            M.rrect(c, cx + dx - 20, cy - 72, 40, 144, 11, BR, ep(t, t0 + 0.2, 0.4))
        E.foco(c, t, t0 + 0.2, 0.5, lambda a: centro(c, "pause o vídeo", cx, 700, 60, "i", TINTA, a))


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    s = C["s20"]
    x, w, y, h = 300, 1320, 600, 170
    lp = w / 5
    ped = [(i, COR, prog(t, C["s20.a"] + 0.2 + i * 0.14, 0.35)) for i in range(2)]
    ped += [(2, TINTA, prog(t, s + 3.9, 0.35))]
    chocolate(c, x, y, w, h, 5, ped, ep(t, s + 0.3, 0.5), ep(t, s + 0.4, 0.6))
    yy, z = 300, 110
    E.saida(c, t, s + 6.0, lambda: E.frase(c, t, s + 1.3, [("o", "i", 66, COR), ("que", "i", 66, COR), ("já", "i", 66, COR), ("foi", "i", 66, COR), ("pago", "i", 66, COR)], W / 2, 130, "center", passo=0.12), d=0.3)
    E.frase(c, t, s + 6.2, [("a", "i", 66), ("dívida", "i", 66), ("inteira", "i", 66)], W / 2, 130, "center", passo=0.14)

    def pago():
        fr(c, t, C["s20.a"], 2, 5, 620, yy, z, COR)
        sinal(c, t, s + 3.7, "+", 790, yy, 90)
        fr(c, t, s + 3.9, 1, 5, 960, yy, z)
        sinal(c, t, C["s20.b"] - 0.2, "=", 1130, yy, 90)
        fr(c, t, C["s20.b"], 3, 5, 1300, yy, z, COR)
    E.saida(c, t, C["s20.c"] - 0.25, pago, d=0.3)

    yc = y + h + 16
    chave(c, x + 8, x + lp * 3 - 8, yc, COR, ep(t, C["s20.b"], 0.4))
    E.foco(c, t, C["s20.b"] + 0.1, 0.4, lambda a: centro(c, "pago", x + lp * 1.5, yc + 88, 66, "i", COR, a))
    chave(c, x, x + w, y - 16, TINTA, ep(t, C["s20.c"], 0.4), h=-20)
    fr(c, t, C["s20.c"], 5, 5, 540, yy, z)
    sinal(c, t, C["s20.d"] - 0.1, "−", 710, yy, 90)
    fr(c, t, C["s20.d"], 3, 5, 880, yy, z, COR)
    sinal(c, t, s + 9.8, "=", 1050, yy, 90)
    E.foco(c, t, C["s20.e"], 0.5, lambda a: (E.bola(c, 1240, yy + 3, 136, CERTO, a), E.fracao(c, 2, 5, 1240, yy, 104, BR, a)))
    E.foco(c, t, s + 9.8, 0.4, lambda a: E.escreve(c, "5 − 3 = 2", 1415, yy + 22, 62, "b", COR, a))
    E.foco(c, t, C["s20.e"], 0.5, lambda a: (E.caixa_pontilhada(c, x + lp * 3 + 8, y + 10, lp * 2 - 16, h - 20, a, CERTO),
                                              centro(c, "faltam", x + lp * 4, yc + 88, 72, "g", CERTO, a)))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s21"] + 0.3, [("resumindo", "i", 92, COR)], W / 2, 170, "center")
        E.frase(c, t, C["s21"] + 1.3, [("com", "i", 72), ("denominadores", "i", 72), ("iguais", "g", 64, COR)], W / 2, 270, "center", passo=0.16)
        itens = ((C["s21.a"], "soma ou subtrai os de cima"), (C["s21.b"], "repete o de baixo"), (C["s21.c"], "cima = baixo: 1 inteiro"))
        for i, (t0, s) in enumerate(itens):
            y = 450 + i * 190
            E.foco(c, t, t0, 0.5, lambda a, i=i: (E.bola(c, 250, y - 30, 56, a=a), centro(c, str(i + 1), 250, y - 7, 64, "g", BR, a)))
            E.frase(c, t, t0 + 0.1, [(s, "g", 92)], 350, y)
    E.saida(c, t, C["s22"] - 0.1, resumo)
    if t < C["s22"]:
        return
    s = C["s22"]
    E.frase(c, t, s + 0.3, [("próxima", "i", 84), ("aula", "i", 84)], XE, 210)
    E.frase(c, t, s + 1.6, [("Denominadores", "g", 124, COR)], XE, 350)
    E.frase(c, t, C["s22.a"], [("diferentes", "g", 124, COR)], XE, 480)
    y, z = 680, 88
    fr(c, t, s + 4.8, 1, 2, 250, y, z)
    sinal(c, t, s + 5.3, "+", 365, y, 76)
    fr(c, t, s + 5.5, 1, 3, 480, y, z)
    sinal(c, t, s + 6.1, "=", 600, y, 76)
    fr(c, t, s + 6.3, 2, 5, 720, y, z, ERRADO)
    if t >= s + 6.9:
        E.risco(c, 655, 765, 785, 595, t, s + 6.9, largura=10)
    E.foco(c, t, C["s22.b"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1440, 450, 84, estilo="g", cor=BR, a=a))
    p = ease_io(prog(t, C["s22.b"] + 0.3, 0.8))
    E.cursor(c, lerp(1770, 1672, p), lerp(760, 492, p), ep(t, C["s22.b"] + 0.2, 0.4), cor=TINTA)
    E.frase(c, t, C["s22.c"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 930, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, barra=b_barra, regra=b_regra, exemplos=b_exemplos, subtrair=b_subtrair,
              inteiro=b_inteiro, erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
