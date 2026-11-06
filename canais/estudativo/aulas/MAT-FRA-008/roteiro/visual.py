"""Visual — Estudativo · MAT-FRA-008: somar e subtrair com denominadores diferentes (piloto do visual editorial).
Identidade em _ferramentas/editorial.py: papel claro, tipografia mista e índigo da Matemática. Sem legenda embaixo: as
palavras-chave entram na tela no tempo da fala. Azul = a primeira parte, preto = a segunda, vermelho = erro, verde = certo."""
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, fr, sinal, passo, corrida, palco
import motor as M
import skia

E.usar("Matemática", "Frações e Decimais")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-FRA-008_somar_fracoes_denominadores_diferentes.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("barras", "metodo", "atalho", "questao", "fim"))


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def conta():
        sobe = ep(t, C["s02"] + 0.1, 0.8)
        cy, k = lerp(470, 240, sobe), lerp(1.0, 0.62, sobe)
        c.save(); c.translate(W / 2, cy); c.scale(k, k); c.translate(-W / 2, 0)
        fr(c, t, C["s01.a"], 1, 2, 500, 0, 230)
        p = ease_back(prog(t, C["s01.b"] - 0.1, 0.55))
        if p > 0:
            E.mais(c, 760, 0, 92 * p, giro=(1 - p) * 90)
        fr(c, t, C["s01.b"] + 0.2, 1, 3, 1020, 0, 230)
        sinal(c, t, C["s01.c"], "=", 1250, 0, 190)
        fr(c, t, C["s01.c"], 2, 5, 1490, 0, 230, ERRADO if t > C["s01.c"] + 0.9 else None)
        if t > C["s02.b"]:
            E.risco(c, 1350, 150, 1630, -150, t, C["s02.b"], largura=20)
        c.restore()
        E.saida(c, t, C["s02"], lambda: E.frase(c, t, C["s01.c"] + 1.0, [("o", "i", 74), ("erro", "g", 66, ERRADO), ("mais", "i", 74),
                                                                          ("comum", "i", 74)], W / 2, 900, "center"))
        # as duas barras mostram que 2/5 é menor que 1/2, sem conta
        x, w = 640, 860
        E.foco(c, t, C["s02.a"], 0.5, lambda q: (E.fracao(c, 1, 2, 520, 500, 64, COR, q),
                                                  E.barra_fatias(c, x, 468, w, 100, 2, 1, COR, q)))
        E.foco(c, t, C["s02.a"] + 0.5, 0.5, lambda q: (E.fracao(c, 2, 5, 520, 680, 64, ERRADO, q),
                                                        E.barra_fatias(c, x, 648, w, 100, 5, 2, ERRADO, q)))
        E.frase(c, t, C["s02.b"], [("somou,", "i", 76), ("e", "i", 76), ("diminuiu?", "g", 70, ERRADO)], W / 2, 900, "center")
    E.saida(c, t, C["s03"] - 0.1, conta)

    if t >= C["s03"]:
        c.save()
        E.foco(c, t, C["s03.b"] - 0.2, 0.7, lambda a: E.bola(c, 1450, 520, 300 * ease_back(prog(t, C["s03.b"] - 0.2, 0.7))), blur=0)
        E.frase(c, t, C["s03.a"], [("até", "i", 96), ("o", "i", 96), ("fim", "i", 96), ("da", "i", 96), ("aula", "i", 96)], XE, 380)
        E.frase(c, t, C["s03.a"] + 1.0, [("somar", "g", 132)], XE, 530)
        E.frase(c, t, C["s03.a"] + 1.3, [("e", "i", 120), ("subtrair", "g", 132)], XE, 680)
        E.frase(c, t, C["s03.a"] + 1.8, [("quaisquer", "i", 96), ("frações", "i", 96, COR)], XE, 800)
        E.foco(c, t, C["s03.b"] + 0.2, 0.5, lambda a: (E.escreve(c, "+ atalho", 1290, 505, 84, "g", "#FFFFFF", a),
                                                      E.escreve(c, "de prova", 1310, 590, 84, "i", "#FFFFFF", a)))
        c.restore()


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s04"], [("você", "i", 84), ("só", "i", 84), ("precisa", "i", 84), ("de", "i", 84)], XE, 410)
    E.foco(c, t, C["s04.a"], 0.5, lambda a: E.escreve(c, "3", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s04.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 960, 780
    itens = (("s04.b", "Somar com o", "mesmo denominador"), ("s04.c", "Trocar por fração", "equivalente"), ("s04.d", "Achar", "o MMC"))
    for i, (k, l1, l2) in enumerate(itens):
        y = 190 + i * 240
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 196, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 62)], x + 44, y + 84)
        E.frase(c, t, C[k] + 0.3, [(l2, "g", 62, COR)], x + 44, y + 160)
    alvo = [(C[k], x + w - 30, 190 + i * 240 + 170) for i, (k, _, _) in enumerate(itens)]
    px = alvo[0][1]
    q1, q2 = ease_io(prog(t, C["s04.c"] - 0.35, 0.5)), ease_io(prog(t, C["s04.d"] - 0.35, 0.5))
    py = lerp(lerp(alvo[0][2], alvo[1][2], q1), alvo[2][2], q2)
    E.cursor(c, px, py, ep(t, C["s04.b"], 0.4))


# ---------------- por que não dá para somar direto ----------------
BX, BW, BH = 450, 1080, 150


def linhas(c, x, y, w, h, n, pintadas, p):
    for i in range(1, n):
        lx = x + w * i / n
        M.line(c, lx, y + 2, lx, y + 2 + (h - 4) * p, "#FFFFFF" if i < pintadas or (pintadas and i == pintadas) else FIO, 1.0, 4)


def b_barras(c, t, C, b):
    y1, y2 = 300, 540
    mudou = ep(t, C["s08.a"] - 0.2, 0.9)  # as duas barras viram uma só
    if t < C["s07"]:
        E.frase(c, t, C["s05"], [("por", "i", 80), ("que", "i", 80), ("não", "g", 72), ("dá", "i", 80), ("para", "i", 80),
                                 ("somar", "i", 80), ("direto?", "i", 80, COR)], W / 2, 190, "center", passo=0.13)
    else:
        E.frase(c, t, C["s07.a"], [("o", "i", 80), ("mesmo", "g", 72, COR), ("tamanho", "i", 80), ("de", "i", 80), ("pedaço", "i", 80)],
                W / 2, 190, "center")
    enche1 = ep(t, C["s06.a"], 0.6)
    enche2 = ep(t, C["s06.b"], 0.6)

    # barra de cima
    a1 = ep(t, C["s05.a"], 0.5)
    E.barra_fatias(c, BX, y1, BW, BH, 2, 1, COR, a1, ep(t, C["s05.b"], 0.5), enche1)
    if t >= C["s07.b"]:
        linhas(c, BX, y1, BW, BH, 6, 3, ep(t, C["s07.b"], 0.5))
    # barra de baixo: a parte pintada sobe e encosta na de cima
    a2 = ep(t, C["s05.a"] + 0.2, 0.5) * (1 - ep(t, C["s08.a"] + 0.6, 0.3))
    E.barra_fatias(c, BX, y2, BW, BH, 3, 1, TINTA, a2, ep(t, C["s05.c"], 0.5), 0 if mudou > 0 else enche2)
    if t >= C["s07.b"] and a2 > 0:
        linhas(c, BX, y2, BW, BH, 6, 2, ep(t, C["s07.b"] + 0.1, 0.5))
    if mudou > 0:
        px, py = lerp(BX, BX + BW / 2, mudou), lerp(y2, y1, mudou)
        c.drawRect(skia.Rect.MakeXYWH(px, py, BW / 3, BH), M.paint(TINTA))
        M.line(c, px + BW / 6, py, px + BW / 6, py + BH, "#FFFFFF", 1.0, 4)

    # rótulos à esquerda
    def rot(cy, n, d, troca, nn, dd, cor):
        q = ep(t, troca, 0.5)
        if t < troca + 0.2:
            E.fracao(c, n, d, 300, cy, 70, cor, 1 - q)
        E.foco(c, t, troca, 0.5, lambda a: E.fracao(c, nn, dd, 300, cy, 70, cor, a))

    if t < C["s08.a"] - 0.2:
        E.foco(c, t, C["s06.a"], 0.5, lambda a: rot(y1 + 72, 1, 2, C["s07.c"], 3, 6, COR))
        E.foco(c, t, C["s06.b"], 0.5, lambda a: rot(y2 + 72, 1, 3, C["s07.d"], 2, 6, TINTA))
    if C["s05.b"] <= t < C["s06.a"]:
        M.text(c, "2 partes", 300, y1 + 90, 34, "medium", TINTA2, ep(t, C["s05.b"], 0.4))
    if C["s05.c"] <= t < C["s06.b"]:
        M.text(c, "3 partes", 300, y2 + 90, 34, "medium", TINTA2, ep(t, C["s05.c"], 0.4))
    if C["s06.c"] <= t < C["s07"] - 0.2:
        E.frase(c, t, C["s06.c"], [("pedaços", "i", 78), ("diferentes", "g", 70, ERRADO)], W / 2, 860, "center")
    if C["s07.b"] <= t < C["s08.a"] - 0.2:
        E.frase(c, t, C["s07.b"], [("6", "g", 76, COR), ("partes", "i", 78), ("em", "i", 78), ("cada", "i", 78), ("barra", "i", 78)],
                W / 2, 860, "center")
    if t >= C["s08.a"] - 0.1:
        yy = 620
        fr(c, t, C["s08.a"], 3, 6, 620, yy, 112, COR)
        sinal(c, t, C["s08.a"] + 0.5, "+", 790, yy, 92, TINTA)
        fr(c, t, C["s08.a"] + 0.8, 2, 6, 960, yy, 112, TINTA)
        sinal(c, t, C["s08.b"] - 0.2, "=", 1130, yy, 92, TINTA)
        E.foco(c, t, C["s08.b"], 0.5, lambda a: (E.bola(c, 1320, yy + 5, 142, a=a), E.fracao(c, 5, 6, 1320, yy, 112, "#FFFFFF", a)))
        E.frase(c, t, C["s08.b"] + 1.5, [("só", "i", 66), ("contamos", "i", 66), ("os", "i", 66), ("pedaços", "g", 58, COR)], W / 2, 930, "center")


# ---------------- método ----------------
def b_metodo(c, t, C, b):
    E.saida(c, t, C["s10"] - 0.1, lambda: E.frase(c, t, C["s09.a"], [("três", "i", 210), ("passos", "g", 200, COR)], W / 2, 600, "center"))
    if t < C["s10"]:
        return
    passo(c, t, C["s10.a"], 1, "achar o", "denominador comum", 200)
    passo(c, t, C["s11.a"], 2, "reescrever", "cada fração", 500)
    passo(c, t, C["s12.a"], 3, "somar os de cima", "repetir o de baixo", 880)
    p = ep(t, C["s10.c"], 0.5)
    E.caixa_pontilhada(c, XE + 108, 282, 420, 100, p, prog_=p)
    E.foco(c, t, C["s10.c"], 0.5, lambda a: E.escreve(c, "MMC(2, 3) = 6", XE + 134, 350, 50, "b", COR, a))
    E.foco(c, t, C["s11.b"], 0.5, lambda a: E.pilula(c, "divide pelo de baixo", XE + 300, 640, 46, a=a))
    E.foco(c, t, C["s11.c"], 0.5, lambda a: E.pilula(c, "multiplica pelo de cima", XE + 330, 730, 46, fundo=TINTA, a=a))

    x1, x2, xm = 1040, 1470, 1255
    s, y1, y2, y3 = 104, 215, 540, 850
    fr(c, t, C["s10"], 1, 2, x1, y1, s, COR)
    sinal(c, t, C["s10"] + 0.2, "+", xm, y1 - 15, 84)
    fr(c, t, C["s10"] + 0.3, 1, 3, x2, y1, s)
    # segunda linha: primeiro só o 6 embaixo; os de cima entram na fala
    for x, n, ca, cb, cor in ((x1, 3, "s11.d", "s11.e", COR), (x2, 2, "s11.f", "s11.g", TINTA)):
        a = ep(t, C["s11.a"], 0.5)
        M.arrow(c, x, y1 + 115, x, y2 - 118, FIO, a, 4, 14, a)
        E.foco(c, t, C[ca], 0.4, lambda q, ca=ca: E.escreve(c, f"6 ÷ {2 if ca == 's11.d' else 3} = {n}", x + 26, y1 + 168, 42, "m", TINTA2, q))
        E.foco(c, t, C[cb], 0.4, lambda q: E.escreve(c, f"{n} × 1 = {n}", x + 26, y1 + 220, 42, "b", COR, q))
        if t >= C["s10.c"]:
            E.foco(c, t, C["s11.a"], 0.5, lambda q: E.fracao(c, n if t >= C[cb] else "?", 6, x, y2, s, cor if t >= C[cb] else CINZA, q))
    sinal(c, t, C["s11.a"] + 0.2, "+", xm, y2 - 15, 84)
    sinal(c, t, C["s12.b"] - 0.3, "=", 1085, y3 - 15, 84)
    E.foco(c, t, C["s12.b"], 0.5, lambda a: (E.bola(c, 1270, y3 + 3, 130, a=a), E.fracao(c, 5, 6, 1270, y3, s, "#FFFFFF", a)))


# ---------------- subtração e simplificação: a conta corrida ----------------
def b_subtrair(c, t, C, b):
    E.frase(c, t, C["s13"], [("com", "i", 84), ("subtração", "g", 76, COR), ("é", "i", 84), ("igual", "i", 84)], W / 2, 200, "center")
    corrida(c, t, 490, 3, 4, "−", 1, 6, C["s13.a"], C["s14.a"], 12, ("12 ÷ 4 = 3", C["s14.b"], "3 × 3 = 9"), None,
            ("12 ÷ 6 = 2", C["s14.d"], "2 × 1 = 2"), None, 9, 2, 12, 7, 12, (C["s14.c"], C["s14.e"]), C["s15.b"])
    E.frase(c, t, C["s15.b"] + 1.2, [("sem", "i", 62), ("divisor", "i", 62), ("comum:", "i", 62), ("está", "i", 62), ("pronto", "g", 54, CERTO)],
            W / 2, 880, "center")


def b_simplificar(c, t, C, b):
    E.frase(c, t, C["s16.a"], [("às", "i", 84), ("vezes,", "i", 84), ("dá", "i", 84), ("para", "i", 84), ("simplificar", "g", 76, COR)],
            W / 2, 180, "center")
    corrida(c, t, 395, 1, 6, "+", 3, 10, C["s16.b"], C["s16.c"], 30, ("30 ÷ 6 = 5", C["s16.d"], "5 × 1 = 5"), None,
            ("30 ÷ 10 = 3", C["s16.e"], "3 × 3 = 9"), None, 5, 9, 30, 14, 30, (C["s16.d"], C["s16.e"]), C["s17.a"], s=104)
    y = 830
    if t >= C["s17.b"]:
        p = ep(t, C["s17.b"] + 0.3, 0.5)
        fr(c, t, C["s17.b"], 14, 30, 740, y, 88, TINTA)
        M.arrow(c, 860, y, 1040, y, COR, p, 4, 14, p)
        E.foco(c, t, C["s17.b"] + 0.3, 0.4, lambda a: E.pilula(c, "÷ 2 nos dois", 950, y - 66, 38, estilo="b", a=a))
        E.foco(c, t, C["s17.c"], 0.5, lambda a: E.fracao(c, 7, 15, 1160, y, 100, CERTO, a))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s18"], [("cuidado", "g", 110, ERRADO), ("com", "i", 100), ("isto", "i", 100)], W / 2, 200, "center")
    certo = t >= C["s19.b"]
    y, xa, xb = 400, 760, 1160
    fr(c, t, C["s18"] + 1.6, 1, 2, xa, y, 124, COR)
    sinal(c, t, C["s18"] + 2.0, "=", 960, y - 18, 100)
    E.saida(c, t, C["s19.a"], lambda: E.frase(c, t, C["s18.a"], [("esquece", "i", 92), ("do", "i", 92), ("numerador", "g", 82, ERRADO)], W / 2, 760, "center"))
    if t < C["s18.b"]:
        fr(c, t, C["s18"] + 2.2, "?", 6, xb, y, 124, CINZA)
    elif not certo:
        fr(c, t, C["s18.b"], 1, 6, xb, y, 124, ERRADO)
        if t >= C["s19.a"] - 0.1:
            E.risco(c, xb - 95, y + 120, xb + 95, y - 140, t, C["s19.a"] - 0.1, largura=14)
    else:
        fr(c, t, C["s19.b"], 3, 6, xb, y, 124, CERTO)
    x, w = 500, 920
    E.foco(c, t, C["s19.a"], 0.5, lambda a: E.barra_fatias(c, x, 630, w, 96, 2, 1, COR, a))
    if not certo:
        E.foco(c, t, C["s19.a"] + 0.3, 0.5, lambda a: E.barra_fatias(c, x, 770, w, 96, 6, 1, ERRADO, a))
    else:
        E.foco(c, t, C["s19.b"], 0.5, lambda a: E.barra_fatias(c, x, 770, w, 96, 6, 3, CERTO, a))
    E.foco(c, t, C["s19.a"], 0.5, lambda a: E.fracao(c, 1, 2, 400, 660, 54, COR, a))
    E.foco(c, t, C["s19.a"] + 0.3, 0.5, lambda a: E.fracao(c, 3 if certo else 1, 6, 400, 800, 54, CERTO if certo else ERRADO, a))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    BR = "#FFFFFF"

    def titulo():
        E.frase(c, t, C["s20"], [("agora,", "i", 90, CLARO), ("o", "i", 90, CLARO), ("atalho", "i", 90, CLARO)], W / 2, 400, "center")
        E.frase(c, t, C["s20.a"], [("a", "i", 230, BR), ("borboleta", "g", 200, BR)], W / 2, 640, "center")
    E.saida(c, t, C["s21"] - 0.1, titulo)

    def cruz():
        s, xa, xb, y = 170, 400, 860, 560
        fr(c, t, C["s21"], 1, 2, xa, y, s, BR)
        fr(c, t, C["s21"] + 0.3, 1, 3, xb, y, s, BR)
        cruzes = ((xa + 70, y - 90, xb - 70, y + 90, "s21.a", "1 × 3 = 3", 250), (xa + 70, y + 90, xb - 70, y - 90, "s21.b", "2 × 1 = 2", 690))
        for x0, y0, x1, y1, k, txt, tx in cruzes:
            p = ep(t, C[k], 0.6)
            if p > 0:
                M.line(c, x0, y0, x1, y1, CLARO, 1.0, 7, progress=p)
            E.foco(c, t, C[k], 0.45, lambda a: E.escreve(c, txt, tx, 280, 62, "b", CLARO, a))
        c.drawCircle((xa + xb) / 2, y, 62, M.paint("#0A0820"))
        sinal(c, t, C["s21"] + 0.2, "+", (xa + xb) / 2, y - 3, 110, BR)
        sinal(c, t, C["s21.c"] - 0.4, "=", 1040, y - 15, 110, BR)
        cn, yn = 1300, y
        E.foco(c, t, C["s21.c"] - 0.2, 0.5, lambda a: E.escreve(c, "3 + 2", cn - E.larg("3 + 2", "g", 96) / 2, yn - 40, 96, "g", BR, a))
        E.foco(c, t, C["s21.c"], 0.4, lambda a: c.drawRect(skia.Rect.MakeXYWH(cn - 170, yn - 3, 340, 7), M.paint(BR, a)))
        E.foco(c, t, C["s21.d"], 0.5, lambda a: E.escreve(c, "2 × 3", cn - E.larg("2 × 3", "g", 96) / 2, yn + 106, 96, "g", BR, a))
        sinal(c, t, C["s21.e"] - 0.2, "=", 1510, y - 15, 110, BR)
        E.foco(c, t, C["s21.e"], 0.5, lambda a: E.fracao(c, 5, 6, 1640, y, 150, CLARO, a))
    if C["s21"] <= t:
        E.saida(c, t, C["s22"] - 0.1, cruz)

    def porque():
        E.frase(c, t, C["s22.a"], [("o", "i", 74, CLARO), ("produto", "g", 68, BR), ("dos", "i", 74, CLARO), ("denominadores", "g", 68, BR)], W / 2, 240, "center", passo=0.18)
        E.frase(c, t, C["s22.a"] + 1.2, [("vira", "i", 74, CLARO), ("o", "i", 74, CLARO), ("denominador", "i", 74, CLARO), ("comum", "i", 74, CLARO)], W / 2, 340, "center", passo=0.18)
        y = 620
        fr(c, t, C["s22.b"] - 1.8, 3, 4, 420, y, 130, BR)
        sinal(c, t, C["s22.b"] - 1.5, "−", 575, y - 15, 110, BR)
        fr(c, t, C["s22.b"] - 1.3, 1, 6, 730, y, 130, BR)
        sinal(c, t, C["s22.b"] - 0.2, "=", 900, y - 15, 110, BR)
        fr(c, t, C["s22.b"], 14, 24, 1110, y, 130, BR)
        if t >= C["s22.c"]:
            p = ep(t, C["s22.c"], 0.5)
            M.arrow(c, 1270, y, 1390, y, CLARO, p, 5, 16, p)
        fr(c, t, C["s22.c"] + 0.2, 7, 12, 1560, y, 130, CLARO)
    if C["s22"] <= t:
        E.saida(c, t, C["s23"] - 0.1, porque)

    if C["s23"] <= t:
        E.frase(c, t, C["s23.a"], [("denominadores", "i", 92, CLARO), ("pequenos", "i", 92, CLARO)], W / 2, 300, "center", passo=0.16)
        E.frase(c, t, C["s23.a"] + 0.6, [("borboleta", "g", 150, BR)], W / 2, 460, "center")
        E.frase(c, t, C["s23.b"], [("denominadores", "i", 92, CLARO), ("grandes", "i", 92, CLARO)], W / 2, 690, "center", passo=0.16)
        E.frase(c, t, C["s23.b"] + 0.6, [("MMC", "g", 150, BR)], W / 2, 850, "center")


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s24"], [("hora", "i", 72, COR), ("de", "i", 72, COR), ("testar", "i", 72, COR)], XE, 200)
    E.frase(c, t, C["s24.a"], [("gastou", "i", 92)], XE, 380)
    E.foco(c, t, C["s24.a"] + 0.2, 0.5, lambda a: E.fracao(c, 1, 4, 520, 345, 88, COR, a))
    E.frase(c, t, C["s24.a"] + 0.4, [("com", "i", 92), ("aluguel", "g", 76)], 620, 380)
    E.frase(c, t, C["s24.b"], [("e", "i", 92)], XE + 200, 580)
    E.foco(c, t, C["s24.b"] + 0.2, 0.5, lambda a: E.fracao(c, 1, 3, 520, 545, 88, TINTA, a))
    E.frase(c, t, C["s24.b"] + 0.4, [("com", "i", 92), ("mercado", "g", 76)], 620, 580)
    E.frase(c, t, C["s24.c"], [("que", "i", 120), ("fração", "i", 120), ("sobrou?", "g", 112, COR)], XE, 830)
    # relógio de pausa: enche em 3 segundos
    t0 = C["s25.a"]
    r = 210 * ease_back(prog(t, t0, 0.6))
    if r > 0:
        cx, cy = 1510, 440
        E.bola(c, cx, cy, r)
        f = M.clamp(prog(t, t0 + 0.8, 3.0))
        if f > 0:
            E.arco(c, cx, cy, r + 34, -90, 360 * f, TINTA, 10)
        for dx in (-44, 44):
            M.rrect(c, cx + dx - 22, cy - 80, 44, 160, 12, "#FFFFFF", ep(t, t0 + 0.2, 0.4))
        E.foco(c, t, t0 + 0.2, 0.5, lambda a: E.escreve(c, "pause o vídeo", cx - E.larg("pause o vídeo", "i", 60) / 2, cy + r + 110, 60, "i", TINTA, a))


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    x, w, y, h = 300, 1320, 610, 170
    fatia = w / 12
    a_ = ep(t, C["s26"], 0.5)
    E.barra_fatias(c, x, y, w, h, 12, 0, COR, a_)
    p1 = ep(t, C["s26.b"], 0.6)
    p2 = ep(t, C["s26.b"] + 0.9, 0.6)
    r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 14, 14)
    c.save(); c.clipRRect(r, True)
    c.drawRect(skia.Rect.MakeXYWH(x, y, fatia * 3 * p1, h), M.paint(COR))
    c.drawRect(skia.Rect.MakeXYWH(x + fatia * 3, y, fatia * 4 * p2, h), M.paint(TINTA))
    c.restore()
    for i in range(1, 12):
        lx = x + fatia * i
        M.line(c, lx, y, lx, y + h, "#FFFFFF" if lx < x + fatia * 7 and t > C["s26.b"] else FIO, a_, 3)
    c.drawRRect(r, M.paint(TINTA, a_, stroke=3))
    E.foco(c, t, C["s26.b"] + 0.3, 0.4, lambda a: E.escreve(c, "aluguel", x + 20, y + h + 58, 50, "i", COR, a))
    E.foco(c, t, C["s26.b"] + 1.2, 0.4, lambda a: E.escreve(c, "mercado", x + fatia * 3 + 20, y + h + 58, 50, "i", TINTA, a))

    yy = 300

    def primeira():
        fr(c, t, C["s26.a"], 1, 4, 330, yy, 100, COR)
        sinal(c, t, C["s26.a"] + 0.2, "+", 460, yy - 15, 80)
        fr(c, t, C["s26.a"] + 0.4, 1, 3, 590, yy, 100)
        sinal(c, t, C["s26.b"] - 0.2, "=", 725, yy - 15, 80)
        fr(c, t, C["s26.b"], 3, 12, 860, yy, 100, COR)
        sinal(c, t, C["s26.b"] + 0.5, "+", 1000, yy - 15, 80)
        fr(c, t, C["s26.b"] + 0.7, 4, 12, 1140, yy, 100)
        sinal(c, t, C["s26.c"] - 0.2, "=", 1285, yy - 15, 80)
        fr(c, t, C["s26.c"], 7, 12, 1430, yy, 100, COR)
        E.foco(c, t, C["s26.c"] + 0.4, 0.4, lambda a: E.escreve(c, "gastou", 1525, yy + 15, 60, "i", TINTA2, a))
    E.saida(c, t, C["s27.b"] - 0.2, primeira)

    if t >= C["s27.a"]:
        E.foco(c, t, C["s27.a"], 0.5, lambda a: (E.caixa_pontilhada(c, x + fatia * 7 - 6, y - 16, fatia * 5 + 12, h + 32, a, CERTO),
                                                  E.escreve(c, "sobrou", x + fatia * 7 + 180, y + h + 58, 56, "g", CERTO, a)))
    fr(c, t, C["s27.b"], 12, 12, 620, yy, 100)
    sinal(c, t, C["s27.b"] + 0.5, "−", 790, yy - 15, 80)
    fr(c, t, C["s27.b"] + 0.7, 7, 12, 960, yy, 100, COR)
    sinal(c, t, C["s27.c"] - 0.2, "=", 1130, yy - 15, 80)
    E.foco(c, t, C["s27.c"], 0.5, lambda a: (E.bola(c, 1320, yy + 3, 136, CERTO, a), E.fracao(c, 5, 12, 1320, yy, 94, "#FFFFFF", a)))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s28"], [("resumindo", "i", 92, COR)], W / 2, 210, "center")
        for i, (k, s, e) in enumerate((("s28.a", "mesmo denominador", "g"), ("s28.b", "troca as frações", "g"), ("s28.c", "soma os de cima", "g"))):
            y = 390 + i * 190
            E.foco(c, t, C[k], 0.5, lambda a, i=i: (E.bola(c, 470, y - 30, 56, a=a),
                                                    E.escreve(c, str(i + 1), 470 - E.larg(str(i + 1), "g", 64) / 2, y - 7, 64, "g", "#FFFFFF", a)))
            E.frase(c, t, C[k] + 0.1, [(s, e, 100)], 570, y)
    E.saida(c, t, C["s29"] - 0.1, resumo)
    if t < C["s29"]:
        return
    E.frase(c, t, C["s29.a"] - 1.0, [("próxima", "i", 84), ("aula", "i", 84)], XE, 330)
    E.frase(c, t, C["s29.a"], [("Multiplicar", "g", 150, COR)], XE, 490)
    E.frase(c, t, C["s29.a"] + 0.3, [("frações", "g", 150, COR)], XE, 640)
    E.foco(c, t, C["s29.b"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1430, 400, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s29.b"] + 0.3, 0.8))
    E.cursor(c, lerp(1760, 1560, p), lerp(720, 425, p), ep(t, C["s29.b"] + 0.2, 0.4))
    E.frase(c, t, C["s29.c"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 900, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, barras=b_barras, metodo=b_metodo, subtrair=b_subtrair,
              simplificar=b_simplificar, erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
