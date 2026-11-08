"""Visual — Estudativo · MAT-RAZ-024: velocidade média em dois trechos.
Peças locais: estrada() e carro() (a mesma pista escura das MAT-RAZ-015 e 016, com a seta de ida ou de volta);
horas() é a fila de blocos de 1 hora (índigo = ida a 40, preto = volta a 60): mostra que o trecho lento ocupa mais tempo
e por isso pesa mais na média. Vermelho = erro, verde = conferido. Todo instante vem de C[...]; o que cai entre dois cues
usa lerp(C[a], C[b], f), que acompanha qualquer voz."""
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Razão e Proporção")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-RAZ-024_velocidade_media_em_dois_trechos.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("distancia", "porque", "iguais", "parada", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
ASFALTO = "#26262B"
# as contas da aula, conferidas
assert 120 / 40 == 3 and 120 / 60 == 2 and 240 / 5 == 48 and (40 + 60) / 2 == 50
assert 240 / 40 == 6 and 240 / 60 == 4 and 480 / 10 == 48 and 2 * 40 + 2 * 60 == 200 and 200 / 4 == 50
assert 2 + 0.5 + 0.5 == 3 and 150 / 3 == 50 and 150 / 2.5 == 60
assert 2 * 40 * 60 == 4800 and 4800 / 100 == 48
assert 180 / 90 == 2 and 180 / 60 == 3 and 360 / 5 == 72 and 2 * 90 * 60 == 10800 and 10800 / 150 == 72 and (90 + 60) / 2 == 75


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


def fcen(c, t, t0, s, cx, y, size, cor=None):
    E.formula_em(c, t, t0, s, cx, y, size, "g", cor, "center")


def bola_res(c, t, t0, s, cx, cy, r=130, size=70, cor=None):
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r, cor, a), centro(c, s, cx, cy + size * 0.36, size, "g", E.SOBRE, a)))


def carro(c, cx, base, a, cor=None, vira=False):
    """carro de lado, com a base em (cx, base); vira = andando para a esquerda"""
    if a <= 0:
        return
    cor = cor or E.COR
    tx = cx - 60 if vira else cx - 50  # a cabine fica um pouco para trás, no sentido da marcha
    M.rrect(c, tx, base - 92, 110, 50, 18, cor, a)
    M.rrect(c, tx + 14, base - 82, 38, 28, 6, BR, 0.9 * a)
    M.rrect(c, tx + 60, base - 82, 38, 28, 6, BR, 0.9 * a)
    M.rrect(c, cx - 100, base - 58, 200, 46, 18, cor, a)
    for dx in (-58, 58):
        c.drawCircle(cx + dx, base - 12, 17, M.paint(TINTA, a))
        c.drawCircle(cx + dx, base - 12, 6, M.paint(BR, a))


def estrada(c, x0, x1, y, a, pos=None, cor=None, vira=False):
    """pista escura de x0 a x1 (y = meio); pos = 0..1 põe o carro em cima (vira = volta)"""
    if a <= 0:
        return
    M.rrect(c, x0, y - 26, x1 - x0, 52, 26, ASFALTO, a)
    xx = x0 + 40
    while xx < x1 - 60:
        M.line(c, xx, y, xx + 34, y, BR, 0.75 * a, 4)
        xx += 70
    if pos is not None:
        p = M.clamp(pos)
        cx = lerp(x1 - 110, x0 + 110, p) if vira else lerp(x0 + 110, x1 - 110, p)
        carro(c, cx, y - 22, a, cor, vira)


def horas(c, t, x, y, w, h, grupos, rotulo=True):
    """fila de blocos de 1 hora. grupos = [(n, cor, t0, texto)] em sequência; cada bloco entra no seu t0"""
    i = 0
    for n, cor, t0, txt in grupos:
        for j in range(n):
            q = ep(t, t0 + j * 0.12, 0.35)
            if q > 0:
                xi = x + (i + j) * (w + 12)
                M.rrect(c, xi, y + (1 - q) * 20, w, h, 14, cor, q)
                if rotulo:
                    centro(c, "1 h", xi + w / 2, y + h / 2 + 16, 44, "g", M.on(cor), q)
        i += n


# ---------------- gancho ----------------
X0, X1 = 330, 1590


def b_gancho(c, t, C, b):
    a1, b1, c1, d1 = C["s01.a"], C["s01.b"], C["s01.c"], C["s01.d"]

    def cena():
        E.foco(c, t, C["s01"], 0.5, lambda a: (centro(c, "A", X0 - 70, 380, 64, "g", TINTA, a), centro(c, "B", X1 + 70, 380, 64, "g", TINTA, a)))
        E.foco(c, t, a1 - 0.6, 0.5, lambda a: estrada(c, X0, X1, 360, a, ease_io(prog(t, a1 - 0.6, max(1.0, b1 - a1)))))
        E.frase(c, t, a1, ps("ida a", "i", 66) + [("40 km/h", "g", 72, COR)], W / 2, 250, "center", 0.1)
        if t >= b1 - 0.3:
            E.foco(c, t, b1 - 0.3, 0.5, lambda a: estrada(c, X0, X1, 560, a, ease_io(prog(t, b1, max(1.0, c1 - b1))), TINTA, True))
        E.frase(c, t, b1, ps("volta a", "i", 66) + [("60 km/h", "g", 72)], W / 2, 680, "center", 0.1)
        E.frase(c, t, lerp(b1, c1, 0.4), ps("velocidade média da", "i", 66) + [("viagem toda?", "g", 70, COR)], W / 2, 820, "center", 0.1)
        E.linha(c, t, [("50?", "g", 120, ERRADO, c1)], 700, 1000, "center")
        if t >= lerp(c1, d1, 0.5):
            E.risco(c, 590, 1010, 810, 920, t, lerp(c1, d1, 0.5), TINTA, 10)
        bola_res(c, t, d1, "48", 1240, 960, 100, 90)
    E.saida(c, t, C["s02"] - 0.1, cena)

    if t >= C["s02"]:
        ta, tb = C["s02.a"], C["s02.b"]
        E.foco(c, t, tb - 0.2, 0.7, lambda a: E.bola(c, 1500, 540, 250 * ease_back(prog(t, tb - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, ps("até o fim desta aula", "i", 90), XE, 300, passo=0.14)
        E.frase(c, t, lerp(ta, tb, 0.15), [("entender", "g", 110, COR)] + ps("o 48", "i", 100), XE, 460, passo=0.14)
        E.frase(c, t, lerp(ta, tb, 0.45), ps("e resolver", "i", 84) + [("viagens em trechos", "g", 84, COR)], XE, 600, passo=0.12)
        E.foco(c, t, tb + 0.1, 0.5, lambda a: (centro(c, "+ atalho", 1500, 525, 80, "g", E.SOBRE, a),
                                               centro(c, "de prova", 1500, 610, 80, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    a3, b3, c3, e3 = C["s03.a"], C["s03.b"], C["s03.c"], C["s03.end"]
    E.frase(c, t, C["s03"] + 0.3, ps("você só precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, a3, 0.5, lambda a: E.escreve(c, "1", XE + 10, 720, 340, "g", COR, a))
    E.foco(c, t, a3 + 0.15, 0.5, lambda a: E.escreve(c, "coisa", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 960, 800
    p = ep(t, b3, 0.5)
    E.caixa_pontilhada(c, x, 170, w, 300, p, prog_=p)
    E.frase(c, t, b3 + 0.1, [("velocidade média", "i", 62)], x + 44, 260)
    E.formula_em(c, t, b3 + 0.4, "= f{distância total}{tempo total}", x + 44, 400, 60, "g", COR)
    E.cursor(c, x + w - 30, 440, ep(t, b3, 0.4))
    E.frase(c, t, c3 - 0.6, ps("o tempo de cada trecho:", "i", 56, TINTA2), x, 600, "left", 0.08)
    E.formula_em(c, t, c3, "tempo = f{distância}{velocidade}", x, 740, 64, "g", TINTA)
    E.frase(c, t, lerp(c3, e3, 0.6), ps("faltou?", "i", 54, COR) + ps("procure no canal", "i", 54, TINTA2), x, 960, "left", 0.1)


# ---------------- escolher a distância ----------------
def b_distancia(c, t, C, b):
    a4, b4 = C["s04.a"], C["s04.b"]
    E.frase(c, t, C["s04"] + 0.2, ps("o enunciado", "i", 76) + [("não diz a distância", "g", 76, COR)], W / 2, 200, "center", 0.12)
    E.frase(c, t, a4, ps("escolha uma que dê", "i", 76) + [("conta exata", "g", 80, COR)], W / 2, 360, "center", 0.12)
    E.frase(c, t, lerp(a4, b4, 0.4), ps("múltiplo de", "i", 66, TINTA2) + [("40", "g", 72)] + ps("e de", "i", 66, TINTA2) + [("60", "g", 72)], W / 2, 520, "center", 0.1)
    E.frase(c, t, lerp(a4, b4, 0.7), ps("40, 80,", "i", 56, TINTA2) + [("120", "g", 60, COR)] + ps("...  60,", "i", 56, TINTA2) + [("120", "g", 60, COR)],
            W / 2, 620, "center", 0.08)
    E.foco(c, t, b4, 0.5, lambda a: estrada(c, X0, X1, 830, a))
    if t >= b4:
        E.chave(c, X0 + 10, X1 - 10, 760, COR, ep(t, b4, 0.5), -22)
    fcen(c, t, b4 + 0.2, "120 km", W / 2, 720, 84, COR)


# ---------------- os dois trechos ----------------
def b_trechos(c, t, C, b):
    a5, b5 = C["s05.a"], C["s05.b"]
    a6, b6, c6 = C["s06.a"], C["s06.b"], C["s06.c"]
    # ida
    E.foco(c, t, C["s05"], 0.4, lambda a: estrada(c, X0, X1, 220, a, ease_io(prog(t, a5, 2.0))))
    E.foco(c, t, a5, 0.4, lambda a: E.escreve(c, "ida", 120, 236, 56, "i", COR, a))
    fcen(c, t, a5 + 0.3, "120 ÷ 40 = 3 h", 760, 360, 76, COR)
    horas(c, t, 1180, 300, 120, 80, [(3, E.COR, a5 + 0.9, "")])
    # volta
    E.foco(c, t, b5 - 0.3, 0.4, lambda a: estrada(c, X0, X1, 500, a, ease_io(prog(t, b5, 2.0)), TINTA, True))
    E.foco(c, t, b5, 0.4, lambda a: E.escreve(c, "volta", 100, 516, 56, "i", TINTA, a))
    fcen(c, t, b5 + 0.3, "120 ÷ 60 = 2 h", 760, 640, 76)
    horas(c, t, 1180, 580, 120, 80, [(2, TINTA, b5 + 0.9, "")])
    # total
    fcen(c, t, a6, "distância: 120 + 120 = 240 km", W / 2, 790, 64)
    fcen(c, t, b6, "tempo: 3 + 2 = 5 h", W / 2, 880, 64)
    fcen(c, t, c6, "240 ÷ 5 = 48 km/h", 800, 1010, 86, COR)
    E.foco(c, t, c6 + 1.2, 0.5, lambda a: E.selo(c, 1240, 980, 40, True, a))


# ---------------- por que não 50 ----------------
def b_porque(c, t, C, b):
    a7, b7, c7, d7 = C["s07.a"], C["s07.b"], C["s07.c"], C["s07.d"]

    def tempos():
        E.frase(c, t, C["s07"] + 0.2, ps("por que", "i", 80) + [("não 50?", "g", 84, ERRADO)], W / 2, 170, "center", 0.12)
        E.frase(c, t, lerp(C["s07"], a7, 0.6), ps("distâncias iguais,", "i", 66, TINTA2) + ps("mas", "i", 66) + [("tempos diferentes", "g", 70, COR)],
                W / 2, 300, "center", 0.1)
        x0, w = 300, 230
        horas(c, t, x0, 420, w, 120, [(3, E.COR, b7, ""), (2, TINTA, c7, "")])
        E.foco(c, t, b7 + 0.4, 0.5, lambda a: centro(c, "3 h a 40 (lento)", x0 + 1.5 * (w + 12), 620, 54, "i", COR, a))
        E.foco(c, t, c7 + 0.3, 0.5, lambda a: centro(c, "2 h a 60", x0 + 4 * (w + 12), 620, 54, "i", TINTA, a))
        E.frase(c, t, lerp(c7, d7, 0.4), ps("a velocidade menor", "i", 72) + [("pesa mais", "g", 76, COR)], W / 2, 790, "center", 0.12)
        E.frase(c, t, d7, ps("a média fica", "i", 72) + [("abaixo de 50", "g", 76, COR)], W / 2, 920, "center", 0.12)
    E.saida(c, t, C["s08"] - 0.1, tempos)
    if t < C["s08"]:
        return
    a8, b8, c8 = C["s08.a"], C["s08.b"], C["s08.c"]
    E.frase(c, t, C["s08"] + 0.2, ps("a distância escolhida", "i", 72) + [("não muda nada", "g", 76, COR)], W / 2, 180, "center", 0.12)
    fcen(c, t, a8, "ida de 240 km", W / 2, 340, 84)
    fcen(c, t, b8, "240 ÷ 40 = 6 h", 600, 500, 76, COR)
    fcen(c, t, b8 + 0.6, "240 ÷ 60 = 4 h", 1320, 500, 76)
    fcen(c, t, c8, "480 km em 10 h", W / 2, 680, 90)
    fcen(c, t, lerp(c8, C["s08.end"], 0.45), "480 ÷ 10 = 48 km/h", W / 2, 860, 100, COR)
    E.foco(c, t, lerp(c8, C["s08.end"], 0.6), 0.5, lambda a: E.selo(c, 1520, 828, 46, True, a))


# ---------------- tempos iguais ----------------
def b_iguais(c, t, C, b):
    a9, b9, c9, d9 = C["s09.a"], C["s09.b"], C["s09.c"], C["s09.d"]
    E.frase(c, t, C["s09"] + 0.2, ps("quando a média simples", "i", 72) + [("funciona?", "g", 76, COR)], W / 2, 170, "center", 0.12)
    E.frase(c, t, a9, [("tempos iguais", "g", 96, CERTO)], W / 2, 320, "center")
    x0, w = 300, 300
    horas(c, t, x0, 420, w, 120, [(2, E.COR, b9, ""), (2, TINTA, lerp(b9, c9, 0.5), "")])
    E.foco(c, t, b9 + 0.3, 0.5, lambda a: centro(c, "2 h a 40 = 80 km", x0 + (w + 12) - 6, 620, 52, "i", COR, a))
    E.foco(c, t, lerp(b9, c9, 0.5) + 0.3, 0.5, lambda a: centro(c, "2 h a 60 = 120 km", x0 + 3 * (w + 12) - 6, 620, 52, "i", TINTA, a))
    fcen(c, t, c9, "80 + 120 = 200 km em 4 h", W / 2, 790, 84)
    fcen(c, t, d9, "200 ÷ 4 = 50 km/h", W / 2, 930, 96, CERTO)
    E.frase(c, t, lerp(d9, C["s09.end"], 0.4), ps("cada velocidade", "i", 56, TINTA2) + [("pesou o mesmo", "g", 56)], W / 2, 1040, "center", 0.08)


# ---------------- trechos diferentes e parada ----------------
def b_parada(c, t, C, b):
    a0, b0, c0 = C["s10.a"], C["s10.b"], C["s10.c"]

    def metodo():
        E.frase(c, t, C["s10"] + 0.2, ps("trechos diferentes?", "i", 70) + ps("parada no meio?", "i", 70), W / 2, 200, "center", 0.1)
        E.frase(c, t, lerp(C["s10"], a0, 0.7), ps("o método", "i", 80) + [("não muda", "g", 84, COR)], W / 2, 340, "center", 0.12)
        E.passo(c, t, a0, 1, "some", "as distâncias", 500)
        E.passo(c, t, b0, 2, "some os tempos,", "inclusive o tempo parado", 700)
        E.passo(c, t, c0, 3, "e", "divida", 900)
    E.saida(c, t, C["s11"] - 0.1, metodo)
    if t < C["s11"]:
        return
    a1, b1, c1, d1, e1, f1 = C["s11.a"], C["s11.b"], C["s11.c"], C["s11.d"], C["s11.e"], C["s11.end"]
    x0, w = 480, 320  # 1 h = 320 px: 2 h andando, meia parado, meia andando
    def faixa(xa, ww, cor, t0, txt, sub, sub_cor):
        E.foco(c, t, t0, 0.5, lambda a: (M.rrect(c, xa, 330, ww - 10, 130, 16, cor, a), centro(c, txt, xa + ww / 2 - 5, 412, 46, "g", M.on(cor), a)))
        E.foco(c, t, t0 + 0.3, 0.5, lambda a: centro(c, sub, xa + ww / 2 - 5, 530, 44, "i", sub_cor, a))
    E.frase(c, t, C["s11"] + 0.2, ps("um exemplo", "i", 66, TINTA2), W / 2, 200, "center", 0.1)
    faixa(x0, 2 * w, E.COR, a1, "100 km em 2 h", "andando", COR)
    faixa(x0 + 2 * w, w / 2, CINZA, b1, "0", "parado", TINTA2)
    faixa(x0 + 2.5 * w, w / 2, TINTA, c1, "50 km", "meia hora", TINTA)
    fcen(c, t, d1, "tempo: 2 + 0,5 + 0,5 = 3 h", W / 2, 690, 76)
    fcen(c, t, lerp(d1, e1, 0.6), "150 km em 3 h", W / 2, 810, 76)
    fcen(c, t, e1, "= 50 km/h", 760, 950, 100, CERTO)
    E.foco(c, t, lerp(e1, f1, 0.4), 0.5, lambda a: (E.escreve(c, "sem a parada: 2,5 h", 1180, 920, 44, "i", ERRADO, a),
                                                     E.escreve(c, "daria 60", 1180, 980, 52, "g", ERRADO, a)))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    a2, b2, c2, e2 = C["s12.a"], C["s12.b"], C["s12.c"], C["s12.end"]
    E.frase(c, t, C["s12"] + 0.2, ps("o erro:", "i", 80) + [("a média das velocidades", "g", 84, ERRADO)], W / 2, 180, "center", 0.12)
    fcen(c, t, a2 + 0.6, "f{40 + 60}{2}", 760, 410, 110)
    fcen(c, t, b2, "= 50", 1080, 440, 120, ERRADO)
    E.foco(c, t, b2 + 0.5, 0.5, lambda a: E.selo(c, 1320, 405, 50, False, a))
    E.frase(c, t, lerp(b2, c2, 0.3), ps("só vale com", "i", 70) + [("tempos iguais", "g", 74, CERTO)], W / 2, 680, "center", 0.12)
    E.frase(c, t, c2, ps("na ida e volta, o que é igual é", "i", 64) + [("a distância", "g", 68, COR)], W / 2, 840, "center", 0.1)
    E.frase(c, t, lerp(c2, e2, 0.6), [("não o tempo", "g", 68, ERRADO)], W / 2, 950, "center")


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    a3, b3, c3, d3 = C["s13.a"], C["s13.b"], C["s13.c"], C["s13.d"]

    def formula():
        E.frase(c, t, C["s13"] + 0.1, ps("agora, o atalho", "i", 70, CLARO), W / 2, 160, "center", 0.12)
        E.frase(c, t, a3, ps("ida e volta,", "i", 72, CLARO) + [("mesma distância", "g", 76, BR)], W / 2, 290, "center", 0.12)
        E.frase(c, t, b3, [("o dobro do produto", "g", 80, BR)] + ps("÷ a soma", "i", 76, CLARO), W / 2, 450, "center", 0.12)
        fcen(c, t, c3, "2 × v1 × v2", W / 2, 680, 110, BR)
        if t >= d3 - 0.2:
            p = ep(t, d3 - 0.2, 0.4)
            c.drawRect(skia.Rect.MakeXYWH(W / 2 - 330 * p, 720, 660 * p, 9), M.paint(BR))
        fcen(c, t, d3, "v1 + v2", W / 2, 860, 110, CLARO)
    E.saida(c, t, C["s14"] - 0.1, formula)

    a4, b4, c4 = C["s14.a"], C["s14.b"], C["s14.c"]
    if C["s14"] <= t:
        def conta():
            fcen(c, t, a4, "2 × 40 × 60 = 4.800", W / 2, 300, 100, BR)
            fcen(c, t, b4, "40 + 60 = 100", W / 2, 500, 100, CLARO)
            fcen(c, t, c4, "4.800 ÷ 100 = 48 km/h", W / 2, 760, 110, BR)
            E.foco(c, t, c4 + 1.2, 0.5, lambda a: E.selo(c, 1730, 724, 46, True, a))
        E.saida(c, t, C["s15"] - 0.1, conta)

    if t < C["s15"]:
        return
    a5, b5, c5 = C["s15.a"], C["s15.b"], C["s15.c"]
    E.frase(c, t, a5, ps("é a mesma conta, com uma", "i", 66, CLARO) + [("letra na distância", "g", 70, BR)], W / 2, 240, "center", 0.1)
    E.frase(c, t, lerp(a5, b5, 0.6), ps("a letra", "i", 66, CLARO) + [("se cancela", "g", 70, BR)], W / 2, 360, "center", 0.1)
    E.foco(c, t, b5, 0.5, lambda a: E.selo(c, 330, 560, 50, False, a))
    E.frase(c, t, b5 + 0.1, ps("distâncias", "i", 72, CLARO) + [("diferentes?", "g", 76, BR)], 420, 585, "left", 0.1)
    E.frase(c, t, lerp(b5, c5, 0.5), ps("teve", "i", 72, CLARO) + [("parada?", "g", 76, BR)], 420, 710, "left", 0.1)
    E.frase(c, t, c5, ps("aí,", "i", 76, CLARO) + [("distância total ÷ tempo total", "g", 76, BR)], W / 2, 900, "center", 0.1)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    a6, b6, c6 = C["s16.a"], C["s16.b"], C["s16.c"]
    E.frase(c, t, C["s16"] + 0.2, ps("hora de testar", "i", 72, COR), XE, 180, passo=0.12)
    E.frase(c, t, a6 - 0.5, ps("o ônibus vai a", "i", 80) + [("90 km/h", "g", 88, COR)], XE, 380, passo=0.12)
    E.frase(c, t, b6 - 0.3, ps("e volta a", "i", 80) + [("60 km/h", "g", 88)], XE, 520, passo=0.12)
    E.frase(c, t, c6, ps("velocidade média", "i", 92) + [("da ida e volta?", "g", 92, COR)], XE, 740, passo=0.12)
    E.relogio(c, t, C["s17.a"], 1590, 430, 170)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    a8, b8, c8, d8 = C["s18.a"], C["s18.b"], C["s18.c"], C["s18.d"]

    def conta():
        E.foco(c, t, a8, 0.5, lambda a: E.pilula(c, "distância: 180 km", W / 2, 170, 60, "g", a=a))
        E.frase(c, t, a8 + 0.6, ps("múltiplo de 90 e de 60", "i", 52, TINTA2), W / 2, 280, "center", 0.08)
        fcen(c, t, b8, "ida: 180 ÷ 90 = 2 h", 620, 430, 72, COR)
        horas(c, t, 1180, 370, 120, 80, [(2, E.COR, b8 + 0.6, "")])
        fcen(c, t, c8, "volta: 180 ÷ 60 = 3 h", 620, 590, 72)
        horas(c, t, 1180, 530, 120, 80, [(3, TINTA, c8 + 0.6, "")])
        fcen(c, t, d8, "360 km em 5 h", W / 2, 780, 84)
        fcen(c, t, lerp(d8, C["s18.end"], 0.5), "360 ÷ 5 = 72 km/h", 760, 940, 96, COR)
        bola_res(c, t, lerp(d8, C["s18.end"], 0.7), "72 km/h", 1500, 900, 130, 56)
    E.saida(c, t, C["s19"] - 0.1, conta)
    if t < C["s19"]:
        return
    a9, b9, c9 = C["s19.a"], C["s19.b"], C["s19.c"]
    E.frase(c, t, C["s19"] + 0.2, ps("pelo", "i", 76) + [("atalho", "g", 80, COR)], W / 2, 180, "center", 0.12)
    fcen(c, t, a9, "2 × 90 × 60 = 10.800", W / 2, 360, 100)
    fcen(c, t, b9, "10.800 ÷ 150 = 72", W / 2, 540, 100, COR)
    E.foco(c, t, b9 + 1.0, 0.5, lambda a: E.selo(c, 1500, 506, 46, True, a))
    E.frase(c, t, c9, [("72", "g", 80, COR)] + ps("fica abaixo da média simples,", "i", 66) + [("75", "g", 80, TINTA2)], W / 2, 760, "center", 0.1)
    E.frase(c, t, lerp(c9, C["s19.end"], 0.6), ps("como devia", "i", 60, CERTO), W / 2, 880, "center", 0.1)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s20"] + 0.2, [("resumindo", "i", 92, COR)], W / 2, 190, "center")
        itens = (("s20.a", "velocidade média =", "distância total ÷ tempo total", COR), ("s20.b", "nunca", "a média das velocidades", ERRADO),
                 ("s20.c", "a não ser com", "tempos iguais", CERTO))
        for i, (k, l1, l2, cor) in enumerate(itens):
            y = 380 + i * 200
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 230, y - 30, 56, a=a), centro(c, str(i + 1), 230, y - 7, 64, "g", E.SOBRE, a)))
            E.frase(c, t, C[k] + 0.1, ps(l1, "i", 68) + [(l2, "g", 66, cor)], 320, y, "left", 0.1)
    E.saida(c, t, C["s21"] - 0.1, resumo)
    if t < C["s21"]:
        return
    a1, b1, c1, d1 = C["s21.a"], C["s21.b"], C["s21.c"], C["s21.d"]
    E.frase(c, t, C["s21"] + 0.2, ps("na próxima aula", "i", 84), XE, 240, passo=0.14)
    E.frase(c, t, a1, ps("massa e volume:", "i", 80), XE, 380, passo=0.12)
    E.frase(c, t, b1, [("densidade", "g", 140, COR)], XE, 530, passo=0.12)
    E.frase(c, t, lerp(b1, c1, 0.4), ps("boia ou afunda?", "i", 76), XE, 650, passo=0.12)
    E.foco(c, t, c1, 0.5, lambda a: E.pilula(c, "Inscreva-se", 1440, 790, 76, estilo="g", a=a, cor=E.SOBRE))
    p = ease_io(prog(t, c1 + 0.3, 0.8))
    E.cursor(c, lerp(1770, 1570, p), lerp(1020, 815, p), ep(t, c1 + 0.2, 0.4))
    E.frase(c, t, d1, [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 960, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, distancia=b_distancia, trechos=b_trechos, porque=b_porque, iguais=b_iguais,
              parada=b_parada, erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
