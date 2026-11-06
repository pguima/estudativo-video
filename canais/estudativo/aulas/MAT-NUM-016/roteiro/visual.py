"""Visual — Estudativo · MAT-NUM-016: somar e subtrair inteiros.
Identidade em _ferramentas/editorial.py. A imagem central é a de MAT-FRA-016: tirar uma dívida é como ganhar (E.divida, com cancela).
Peças locais: nota (cédula) e ponto."""
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco
import motor as M
import skia

E.usar("Matemática", "Números e Contas")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-NUM-016_somar_subtrair_inteiros.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("divida", "tirar", "fila", "atalho", "questao", "fim"))
BR = "#FFFFFF"
sn = lambda v: str(v).replace("-", "−")  # o menos da tela


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


def pal(s, estilo="i", size=84, cor=TINTA):
    """frase em palavras, para entrar uma a uma"""
    return [(p, estilo, size, cor) for p in s.split()]


def bola_txt(c, t, t0, s, cx, cy, r, size, cor=CERTO):
    """o resultado na esfera"""
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r, cor, a), E.centro(c, s, cx, cy + size * 0.35, size, "g", M.on(cor), a)))


def ponto(c, t, t0, x, y, cor=None, r=24):
    """ponto marcado na reta"""
    k = ease_back(prog(t, t0, 0.5))
    if k > 0:
        E.bola(c, x, y, r * k, cor)


def nota(c, x, y, w, h, s, a=1.0):
    """cédula na cor da matéria (peça local, a mesma de MAT-FRA-015)"""
    if a <= 0:
        return
    M.rrect(c, x, y, w, h, 22, E.COR, a)
    r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x + 16, y + 16, w - 32, h - 32), 12, 12)
    c.drawRRect(r, M.paint(E.SOBRE, 0.55 * a, stroke=4))
    E.centro(c, s, x + w / 2, y + h / 2 + h * 0.13, h * 0.38, "g", E.SOBRE, a)


def cartao(c, t, t0, x, y, w, h, l1, l2, cor=None):
    """cartão pontilhado da regra"""
    p = ep(t, t0, 0.5)
    E.caixa_pontilhada(c, x, y, w, h, p, prog_=p)
    E.frase(c, t, t0 + 0.1, [(l1, "g", 76, cor or COR)], x + 50, y + 110)
    E.frase(c, t, t0 + 0.3, pal(l2, size=72), x + 50, y + 210, passo=0.08)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def conta():
        ka, kb, kc = C["s01.a"], C["s01.b"], C["s01.c"]
        y, s = 410, 180
        E.foco(c, t, ka, 0.5, lambda a: E.escreve(c, "3 − (−5)", XE, y, s, "g", TINTA, a))
        E.foco(c, t, kb, 0.5, lambda a: E.escreve(c, "= −2", 1020, y, s, "g", ERRADO, a))
        tr = lerp(kb, kc, 0.45)
        E.risco(c, 1170, y + 20, 1480, y - 150, t, tr, largura=16)
        E.frase(c, t, tr, pal("você caiu na", size=92) + [("armadilha", "g", 92, ERRADO)], XE, 620, passo=0.12)
        E.frase(c, t, kc - 0.3, pal("a resposta é", size=110), XE, 840)
        bola_txt(c, t, kc, "8", 870, 800, 130, 160)
    E.saida(c, t, C["s02"] - 0.1, conta)
    if t >= C["s02"]:
        ta, tb, tc = C["s02.a"], C["s02.b"], C["s02.c"]
        E.foco(c, t, tc - 0.2, 0.7, lambda a: E.bola(c, 1490, 520, 280 * ease_back(prog(t, tc - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, pal("até o fim desta aula", size=90), XE, 330)
        E.frase(c, t, lerp(ta, tb, 0.45), [("inteiros", "g", 124)], XE, 480)
        E.frase(c, t, lerp(ta, tb, 0.7), pal("pensando em", size=100), XE, 610, passo=0.12)
        E.frase(c, t, tb, [("dívida", "g", 100, COR)] + pal("e", size=96) + [("pagamento", "g", 100, COR)], XE, 760, passo=0.12)
        E.foco(c, t, tc + 0.2, 0.5, lambda a: (E.centro(c, "+ atalho", 1490, 505, 84, "g", E.SOBRE, a),
                                               E.centro(c, "de prova", 1490, 590, 84, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    ka, kb, kc = C["s03.a"], C["s03.b"], C["s03.c"]
    E.frase(c, t, C["s03"] + 0.1, pal("você só precisa de"), XE, 410)
    E.foco(c, t, ka, 0.5, lambda a: E.escreve(c, "2", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, ka + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 240, 700, 120, "i", TINTA, a))
    x, w = 960, 780
    for y, k, l1, l2 in ((230, kb, "a reta", "numérica"), (510, kc, "o oposto", "do outro lado do zero")):
        p = ep(t, k, 0.5)
        E.caixa_pontilhada(c, x, y, w, 196, p, prog_=p)
        E.frase(c, t, k + 0.1, [(l1, "i", 62)], x + 44, y + 84)
        E.frase(c, t, k + 0.3, [(l2, "g", 62, COR)], x + 44, y + 160)
    E.frase(c, t, lerp(kc, C["s03.end"], 0.5), pal("o oposto de", size=66) + [("5", "g", 66)] + pal("é", size=66) + [("−5", "g", 66, COR)], x + 44, 810, passo=0.08)
    py = lerp(400, 680, ease_io(prog(t, kc - 0.35, 0.5)))
    E.cursor(c, x + w - 30, py, ep(t, kb, 0.4))


# ---------------- dívida e pagamento ----------------
def b_divida(c, t, C, b):
    def ideia():
        ka, kb, kc = C["s04.a"], C["s04.b"], C["s04.c"]
        E.frase(c, t, ka, pal("número negativo é", size=88) + [("dívida", "g", 88, ERRADO)], XE, 250, passo=0.1)
        E.foco(c, t, ka + 0.4, 0.5, lambda a: E.divida(c, 1440, 220, 320, 170, "−", a, topo="deve"))
        E.frase(c, t, kb, pal("número positivo é", size=88) + [("pagamento", "g", 88, COR)], XE, 430, passo=0.1)
        E.foco(c, t, kb + 0.4, 0.5, lambda a: E.moeda(c, 1440, 410, 86, "+", a))
        E.foco(c, t, kc, 0.5, lambda a: E.centro(c, "−8 + 5", W / 2, 720, 190, "g", TINTA, a))
        E.frase(c, t, lerp(kc, C["s04.end"], 0.55), pal("você deve", size=88) + [("8", "g", 92, ERRADO)] + pal("e paga", size=88) + [("5", "g", 92, COR)], W / 2, 890, "center", passo=0.1)
    E.saida(c, t, C["s05"] - 0.1, ideia)

    def reta1():
        ka, kb, kc, kd, ke = C["s05.a"], C["s05.b"], C["s05.c"], C["s05.d"], C["s05.e"]
        E.foco(c, t, C["s05"], 0.5, lambda a: E.centro(c, "−8 + 5", W / 2, 180, 120, "g", TINTA, a))
        y = 470
        vx = E.reta(c, t, C["s05"], 280, 1620, y, -9, 1, range(-9, 2), fmt=sn, size=46)
        ponto(c, t, ka, vx(-8), y, ERRADO)
        E.salto(c, t, kb, vx(-8), vx(-3), y, 150, rotulo="+5", size=72)
        ponto(c, t, kb + 0.7, vx(-3), y, TINTA)
        E.frase(c, t, kc, pal("a dívida é maior:", size=84) + pal("você ainda deve", "g", 76, ERRADO), W / 2, 690, "center", passo=0.1)
        E.foco(c, t, kd, 0.5, lambda a: E.centro(c, "8 − 5 = 3", 640, 860, 130, "g", TINTA, a))
        E.frase(c, t, ke - 0.4, pal("ainda é dívida:", size=76), 1140, 860, "center", passo=0.1)
        bola_txt(c, t, ke, "−3", 1560, 820, 120, 110, ERRADO)
    if C["s05"] - 0.1 <= t:
        E.saida(c, t, C["s06"] - 0.1, reta1)

    def reta2():
        ka, kb = C["s06.a"], C["s06.b"]
        E.frase(c, t, C["s06"] + 0.1, pal("pagamento maior:", size=88) + [("sobra", "g", 88, CERTO), ("dinheiro", "g", 88, CERTO)], W / 2, 180, "center", passo=0.1)
        E.foco(c, t, ka, 0.5, lambda a: E.centro(c, "−3 + 7", 760, 380, 160, "g", TINTA, a))
        E.foco(c, t, kb, 0.5, lambda a: E.escreve(c, "= +4", 1120, 380, 160, "g", CERTO, a))
        y = 660
        vx = E.reta(c, t, ka, 300, 1620, y, -4, 5, range(-4, 6), fmt=sn, size=46)
        ponto(c, t, ka, vx(-3), y, ERRADO)
        E.salto(c, t, lerp(ka, kb, 0.4), vx(-3), vx(4), y, 130, rotulo="+7", size=72)
        ponto(c, t, kb, vx(4), y, CERTO)
        E.frase(c, t, lerp(ka, kb, 0.55), pal("deve", size=80) + [("3", "g", 84, ERRADO)] + pal("e paga", size=80) + [("7", "g", 84, COR)] + pal("· a diferença é", size=80) + [("4", "g", 84)], W / 2, 900, "center", passo=0.1)
    if C["s06"] - 0.1 <= t:
        E.saida(c, t, C["s07"] - 0.1, reta2)

    def reta3():
        ka, kb, kc, kd = C["s07.a"], C["s07.b"], C["s07.c"], C["s07.d"]
        E.frase(c, t, C["s07"] + 0.1, pal("e", size=88) + [("dívida", "g", 88, ERRADO)] + pal("com", size=88) + [("dívida?", "g", 88, ERRADO)], W / 2, 180, "center", passo=0.1)
        E.foco(c, t, ka, 0.5, lambda a: E.centro(c, "−4 − 6", 530, 400, 150, "g", TINTA, a))
        E.foco(c, t, kd, 0.5, lambda a: E.escreve(c, "= −10", 820, 400, 150, "g", ERRADO, a))
        E.foco(c, t, ka + 0.3, 0.5, lambda a: E.divida(c, 1390, 350, 240, 160, "R$ 4", a, topo="deve"))
        E.foco(c, t, kb, 0.5, lambda a: E.divida(c, 1650, 350, 240, 160, "R$ 6", a, topo="deve"))
        y = 670
        vx = E.reta(c, t, ka, 300, 1620, y, -11, 1, range(-11, 2), fmt=sn, size=46)
        ponto(c, t, ka, vx(-4), y, ERRADO)
        E.salto(c, t, kc, vx(-4), vx(-10), y, 130, ERRADO, "−6", size=72)
        ponto(c, t, kc + 0.7, vx(-10), y, ERRADO)
        E.frase(c, t, kc, pal("na reta, só anda para a", size=80) + [("esquerda", "g", 80, ERRADO)], W / 2, 900, "center", passo=0.1)
    if C["s07"] - 0.1 <= t:
        E.saida(c, t, C["s08"] - 0.1, reta3)

    if t >= C["s08"]:
        ka, kb, kc = C["s08.a"], C["s08.b"], C["s08.c"]
        E.frase(c, t, C["s08"] + 0.1, pal("a", size=92) + [("regra", "g", 92, COR)], W / 2, 180, "center")
        cartao(c, t, ka, 190, 280, 1540, 270, "sinais iguais", "some e mantenha o sinal")
        cartao(c, t, kb, 190, 590, 1540, 270, "sinais diferentes", "tire o menor do maior, sem o sinal")
        E.frase(c, t, kc, pal("e fique com o", size=80) + [("sinal", "g", 80, COR)] + pal("de quem for", size=80) + [("maior", "g", 80, COR)], W / 2, 970, "center", passo=0.1)


# ---------------- tirar uma dívida ----------------
def b_tirar(c, t, C, b):
    def bolso():
        ka, kb, kc, kd = C["s09.a"], C["s09.b"], C["s09.c"], C["s09.d"]
        ca, cb, cc = C["s10.a"], C["s10.b"], C["s10.c"]
        E.foco(c, t, ka, 0.5, lambda a: E.centro(c, "3 − (−5)", W / 2, 200, 130, "g", TINTA, a))
        E.saida(c, t, kb - 0.1, lambda: E.frase(c, t, lerp(ka, kb, 0.55), pal("o parêntese só impede que os sinais encostem", size=70), W / 2, 330, "center", passo=0.08))
        E.frase(c, t, kb, pal("tirar um negativo é", size=84) + [("tirar", "g", 84, COR), ("uma", "g", 84, COR), ("dívida", "g", 84, COR)], W / 2, 330, "center", passo=0.1)
        y = 620
        E.foco(c, t, kc, 0.5, lambda a: nota(c, 200, y - 125, 460, 250, "R$ 8", a))
        E.foco(c, t, kc + 0.2, 0.5, lambda a: E.centro(c, "no bolso", 430, y + 200, 66, "i", TINTA, a))
        canc = ease_io(prog(t, ca, 0.6))
        E.foco(c, t, kd, 0.5, lambda a: E.divida(c, 950, y, 400, 240, "R$ 5", a, canc))
        E.foco(c, t, kd + 0.2, 0.5, lambda a: E.centro(c, "cancelada" if t >= ca else "a dívida", 950, y + 200, 66, "i", ERRADO if t < ca else TINTA, a))
        ts = lerp(kc, kd, 0.0)
        E.foco(c, t, ts - 0.3, 0.5, lambda a: E.centro(c, "saldo", 1500, y - 150, 80, "i", TINTA, a))
        E.saida(c, t, cb, lambda: E.foco(c, t, ts - 0.2, 0.5, lambda a: E.centro(c, "3", 1500, y + 110, 280, "g", TINTA, a)))
        E.foco(c, t, cb, 0.5, lambda a: E.centro(c, "8", 1500, y + 110, 280, "g", CERTO, a))
        E.frase(c, t, cc, [("tirar", "g", 92, COR), ("uma", "g", 92, COR), ("dívida", "g", 92, COR)] + pal("é como", size=92) + [("ganhar", "g", 92, CERTO)], W / 2, 960, "center", passo=0.1)
    E.saida(c, t, C["s11"] - 0.1, bolso)

    def oposto():
        ka, kb, kc, kd, ke = C["s11.a"], C["s11.b"], C["s11.c"], C["s11.d"], C["s11.e"]
        E.frase(c, t, ka, pal("subtrair é", size=92) + [("somar", "g", 92, COR), ("o", "g", 92, COR), ("oposto", "g", 92, COR)], W / 2, 170, "center", passo=0.1)
        tb_ = lerp(kb, kc, 0.75)
        E.expressao(c, t, [("3 − (−5)", "− (−5)", kb), ("3 + 5", "+ 5", tb_), ("8", "8", kc)], [tb_, kc], 500, 330, 120, empilha=140, t0=kb)
        E.frase(c, t, kd, pal("confira:", size=76) + [("8 + (−5) = 3", "g", 90)], 1250, 340, "center", passo=0.1)
        E.foco(c, t, lerp(kd, ke, 0.7), 0.5, lambda a: E.selo(c, 1250, 460, 60, True, a))
        y = 790
        vx = E.reta(c, t, ke, 300, 1620, y, 0, 9, range(0, 10), fmt=sn, size=46)
        ponto(c, t, ke, vx(3), y)
        E.salto(c, t, ke + 0.5, vx(3), vx(8), y, 130, CERTO, "tira a dívida: +5", size=64)
        ponto(c, t, ke + 1.2, vx(8), y, CERTO)
    if C["s11"] - 0.1 <= t:
        E.saida(c, t, C["s12"] - 0.1, oposto)

    if t >= C["s12"]:
        ka, kb, kc = C["s12.a"], C["s12.b"], C["s12.c"]
        fim = C["s12.end"]
        s, y, size, cx = "3 − (−5)", 400, 170, W / 2 - 200
        E.frase(c, t, C["s12"] + 0.1, pal("e o", size=88) + [("−2", "g", 88, ERRADO)] + pal("do começo?", size=88), W / 2, 180, "center", passo=0.1)
        E.foco(c, t, ka, 0.5, lambda a: E.centro(c, s, cx, y, size, "g", TINTA, a))
        i = s.find("−5")
        x = cx - E.larg(s, "g", size) / 2 + E.larg(s[:i], "g", size) + E.larg("−", "g", size) / 2
        if t >= kb:
            E.corta(c, t, kb, x, y - size * 0.34, size)
        E.foco(c, t, ka + 0.4, 0.5, lambda a: E.escreve(c, "→ 3 − 5", cx + 370, y, 120, "g", ERRADO, a))
        E.frase(c, t, kb, pal("jogou fora um dos sinais de", size=84) + [("menos", "g", 84, ERRADO)], W / 2, 620, "center", passo=0.1)
        E.frase(c, t, lerp(kb, kc, 0.45), pal("aquela conta seria gastar 5 reais", size=76), W / 2, 760, "center", passo=0.09)
        E.frase(c, t, kc, pal("aqui, a dívida", size=88) + [("deixou", "g", 88, CERTO), ("de", "g", 88, CERTO), ("existir", "g", 88, CERTO)], W / 2, 910, "center", passo=0.1)


# ---------------- em fila ----------------
def b_fila(c, t, C, b):
    ka, kb, kc, kd = C["s13.a"], C["s13.b"], C["s13.c"], C["s13.d"]
    fim = C["s13.end"]
    E.frase(c, t, C["s13"] + 0.1, pal("e várias contas", size=88) + [("em", "g", 88, COR), ("fila?", "g", 88, COR)], W / 2, 170, "center", passo=0.1)
    tp = [lerp(kb, kc, 0.75), lerp(kc, kd, 0.75), lerp(kd, fim, 0.72)]
    E.expressao(c, t, [("5 − 8 + 3 − 2", "5 − 8", kb), ("−3 + 3 − 2", "−3 + 3", kc), ("0 − 2", "0 − 2", kd), ("−2", "−2", tp[2])], tp, 640, 340, 124, empilha=165, t0=ka)
    x = 1190
    for i, (s, cor, f) in enumerate((("tem 5", TINTA, 0.22), ("gasta 8", ERRADO, 0.32), ("recebe 3", COR, 0.42), ("gasta 2", ERRADO, 0.52))):
        E.foco(c, t, lerp(ka, kb, f), 0.45, lambda a, i=i, s=s, cor=cor: E.escreve(c, s, x + (i % 2) * 340, 320 + (i // 2) * 110, 72, "b", cor, a))
    E.frase(c, t, lerp(ka, kb, 0.72), pal("da esquerda para a direita,", size=62) , x, 610, passo=0.07)
    E.frase(c, t, lerp(ka, kb, 0.8), pal("acompanhando o", size=62) + [("saldo", "g", 62, COR)], x, 690, passo=0.07)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    ka, kb, kc, kd = C["s14.a"], C["s14.b"], C["s14.c"], C["s14.d"]
    y, size = 420, 170
    E.frase(c, t, C["s14"] + 0.1, [("cuidado", "g", 92, ERRADO)] + pal("com este erro", size=88), W / 2, 190, "center", passo=0.1)
    E.foco(c, t, ka, 0.5, lambda a: E.escreve(c, "−8 + 5", 300, y, size, "g", TINTA, a))
    E.foco(c, t, kb, 0.5, lambda a: E.escreve(c, "= −13", 910, y, size, "g", ERRADO, a))
    E.frase(c, t, kc, pal("pagou 5 e a dívida", size=92) + [("aumentou?", "g", 92, ERRADO)], W / 2, 610, "center", passo=0.1)
    E.foco(c, t, lerp(kc, kd, 0.75), 0.5, lambda a: E.selo(c, 1620, y - 60, 84, False, a))
    E.risco(c, 1090, y + 20, 1520, y - 150, t, lerp(kc, kd, 0.75), largura=16)
    E.frase(c, t, kd, [("pagamento", "g", 92, COR)] + pal("diminui a dívida", size=92), W / 2, 770, "center", passo=0.1)
    E.foco(c, t, lerp(kd, C["s14.end"], 0.6), 0.5, lambda a: E.centro(c, "a conta certa é a diferença", W / 2, 910, 84, "i", CERTO, a))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def separa():
        ka, kb, kc, kd, ke = C["s15.a"], C["s15.b"], C["s15.c"], C["s15.d"], C["s15.e"]
        E.frase(c, t, C["s15"] + 0.1, pal("agora, o atalho:", size=76, cor=CLARO), W / 2, 150, "center", passo=0.1)
        E.frase(c, t, ka, pal("separe", size=110, cor=BR) + [("entradas", "g", 110, BR)] + pal("e", size=110, cor=BR) + [("saídas", "g", 110, BR)], W / 2, 280, "center", passo=0.1)
        E.foco(c, t, lerp(ka, kb, 0.72), 0.5, lambda a: E.centro(c, "5 − 8 + 3 − 2", W / 2, 440, 110, "g", CLARO, a))
        E.frase(c, t, kb, pal("entraram", size=76, cor=CLARO), 480, 590, "center")
        E.foco(c, t, kb + 0.2, 0.5, lambda a: E.centro(c, "5 + 3 = 8", 480, 730, 120, "g", BR, a))
        E.frase(c, t, kc, pal("saíram", size=76, cor=CLARO), 1440, 590, "center")
        E.foco(c, t, kc + 0.2, 0.5, lambda a: E.centro(c, "8 + 2 = 10", 1440, 730, 120, "g", BR, a))
        E.foco(c, t, kd, 0.5, lambda a: E.centro(c, "8 − 10 =", 830, 930, 120, "g", BR, a))
        bola_txt(c, t, ke, "−2", 1190, 885, 100, 96, CERTO)
    E.saida(c, t, C["s16"] - 0.1, separa)

    if t >= C["s16"]:
        ka, kb, kc = C["s16.a"], C["s16.b"], C["s16.c"]
        E.frase(c, t, C["s16"] + 0.1, pal("funciona porque", size=84, cor=CLARO), W / 2, 180, "center")
        E.foco(c, t, ka, 0.5, lambda a: E.selo(c, 290, 340, 72, True, a))
        E.frase(c, t, ka, pal("a", size=76, cor=CLARO) + [("ordem", "g", 76, BR)] + pal("não muda o saldo final", size=76, cor=CLARO), 400, 365, passo=0.1)
        E.foco(c, t, kb, 0.5, lambda a: E.selo(c, 290, 560, 72, True, a))
        E.frase(c, t, kb, pal("cada número leva o", size=76, cor=CLARO) + [("sinal", "g", 76, BR)], 400, 545, passo=0.1)
        E.frase(c, t, kb + 0.8, pal("que está na frente dele", size=76, cor=CLARO), 400, 640, passo=0.1)
        E.foco(c, t, kc, 0.5, lambda a: E.selo(c, 290, 800, 72, False, a))
        E.frase(c, t, kc, pal("com", size=76, cor=CLARO) + [("dois", "g", 76, BR), ("números", "g", 76, BR)] + pal("só, não compensa", size=76, cor=CLARO), 400, 825, passo=0.1)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    ka, kb, kc, kd, ke = C["s17.a"], C["s17.b"], C["s17.c"], C["s17.d"], C["s17.e"]
    E.frase(c, t, C["s17"], pal("hora de testar", size=72, cor=COR), XE, 170)
    E.frase(c, t, ka - 0.2, pal("saldo:", size=88) + [("−12", "g", 92, ERRADO)] + pal("reais", size=88), XE, 310, passo=0.1)
    E.frase(c, t, kb, pal("deposita", size=88) + [("20", "g", 92, COR)] + pal("reais", size=88), XE, 430, passo=0.1)
    E.frase(c, t, kc, pal("gasta", size=88) + [("15", "g", 92, ERRADO)] + pal("reais", size=88), XE, 550, passo=0.1)
    E.frase(c, t, kd, pal("banco", size=88) + [("cancela", "g", 88, COR)] + pal("dívida de", size=88) + [("6", "g", 92, ERRADO)], XE, 670, passo=0.1)
    E.frase(c, t, ke, pal("qual é o", size=110) + [("saldo", "g", 110, COR), ("final?", "g", 110, COR)], XE, 860, passo=0.1)
    E.relogio(c, t, C["s18.a"], 1500, 400, 200)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    ka, kb, kc, kd, ke = C["s19.a"], C["s19.b"], C["s19.c"], C["s19.d"], C["s19.e"]
    tp = [lerp(ka, kb, 0.7), lerp(kb, kc, 0.55), kd, ke]
    E.expressao(c, t, [("−12 + 20 − 15 − (−6)", "−12 + 20", ka), ("8 − 15 − (−6)", "8 − 15", kb), ("−7 − (−6)", "− (−6)", kc), ("−7 + 6", "−7 + 6", kd), ("−1", "−1", ke)],
                tp, 700, 200, 104, empilha=150, t0=C["s19"])
    tc = kc - 0.5
    E.frase(c, t, tc, pal("cancelar é", size=76) + [("tirar", "g", 76, COR)], 1490, 300, "center", passo=0.1)
    E.frase(c, t, tc + 0.3, pal("uma dívida", size=76), 1490, 400, "center", passo=0.1)
    E.foco(c, t, kc, 0.5, lambda a: E.divida(c, 1490, 570, 340, 200, "R$ 6", a, ease_io(prog(t, kc + 0.5, 0.6))))
    E.frase(c, t, ke + 0.2, pal("saldo final:", size=80) + [("−1", "g", 92, COR)] + pal("real", size=80), 1490, 840, "center", passo=0.1)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s20"], [("resumindo", "i", 92, COR)], W / 2, 210, "center")
        for i, (k, s) in enumerate((("s20.a", "dívida com dívida: soma"), ("s20.b", "dívida com pagamento: diferença"), ("s20.c", "tirar uma dívida é como ganhar"))):
            y = 390 + i * 190
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 300, y - 30, 56, a=a), E.centro(c, str(i + 1), 300, y - 7, 64, "g", E.SOBRE, a)))
            E.frase(c, t, C[k] + 0.1, [(s, "g", 80)], 400, y)
    E.saida(c, t, C["s21"] - 0.1, resumo)
    if t < C["s21"]:
        return
    E.frase(c, t, C["s21"] + 0.1, pal("próxima aula"), XE, 270)
    E.frase(c, t, C["s21.a"], [("multiplicar", "g", 110, COR)] + pal("e", size=100) + [("dividir", "g", 110, COR)] + pal("com sinal", size=100), XE, 410, passo=0.12)
    E.frase(c, t, C["s21.b"], pal("a", size=96) + [("regra", "g", 110), ("de", "g", 110), ("sinais", "g", 110)], XE, 550, passo=0.12)
    E.frase(c, t, C["s21.c"], pal("com a ideia de", size=88) + [("cancelar", "g", 88, COR), ("dívida", "g", 88, COR)], XE, 680, passo=0.12)
    E.foco(c, t, C["s21.d"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1500, 790, 76, estilo="g", a=a, cor=E.SOBRE))
    p = ease_io(prog(t, C["s21.d"] + 0.3, 0.8))
    E.cursor(c, lerp(1800, 1630, p), lerp(990, 815, p), ep(t, C["s21.d"] + 0.2, 0.4))
    E.frase(c, t, C["s21.e"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], 700, 900, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, divida=b_divida, tirar=b_tirar, fila=b_fila, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
