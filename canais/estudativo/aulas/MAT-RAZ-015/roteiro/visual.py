"""Visual — Estudativo · MAT-RAZ-015: taxas e velocidade média.
Peças locais: estrada() é a pista escura com o ônibus que anda no ritmo da fala; horas() são blocos de 1 hora que se enchem
(o último pela metade: 30 min = 0,5 h); pacote() é o saco de 2 kg ou 3 kg da comparação de preço. Mesma tipografia e cores
das aulas vizinhas da trilha (índigo = o que está sendo calculado, vermelho = erro, verde = conferido).
Todo instante vem de C[...]; o que cai entre dois cues usa lerp(C[a], C[b], f), que acompanha qualquer voz."""
import math
from decimal import Decimal as D

import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Razão e Proporção")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-RAZ-015_taxas_e_velocidade_media.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("taxa", "velocidade", "tempo", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
ASFALTO = "#26262B"
# as contas da aula, conferidas
assert 12 * 40 == 480 and 30 / 2 == 15 and 50 / 2 == 25 and 72 / 3 == 24
assert D(180) / D("2.5") == 72 and 1800 / 25 == 72 and 240 / 80 == 3 and 80 * 3 == 240
assert 77 < 180 / 2.3 < 79 and D("0.3") * 60 == 18 and 360 / 5 == 72
assert D(45) / D("1.5") == 30 and 90 / 3 == 30 and 150 / 30 == 5 and 30 * 5 == 150


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


def onibus(c, cx, base, a, cor=None):
    """ônibus de lado, com a base em (cx, base)"""
    if a <= 0:
        return
    cor = cor or E.COR
    M.rrect(c, cx - 90, base - 78, 180, 66, 18, cor, a)
    for i in range(4):
        M.rrect(c, cx - 74 + i * 38, base - 68, 28, 24, 6, BR, 0.9 * a)
    for dx in (-50, 50):
        c.drawCircle(cx + dx, base - 12, 16, M.paint(TINTA, a))
        c.drawCircle(cx + dx, base - 12, 6, M.paint(BR, a))


def estrada(c, x0, x1, y, a, pos=None, cor=None):
    """pista escura de x0 a x1 (y = meio); pos = 0..1 põe o ônibus em cima"""
    if a <= 0:
        return
    M.rrect(c, x0, y - 30, x1 - x0, 60, 30, ASFALTO, a)
    xx = x0 + 40
    while xx < x1 - 60:
        M.line(c, xx, y, xx + 34, y, BR, 0.75 * a, 4)
        xx += 70
    if pos is not None:
        onibus(c, lerp(x0 + 100, x1 - 100, M.clamp(pos)), y - 26, a, cor)


def medida(c, t, t0, x0, x1, y, rot, cor=None, size=64):
    """chave acima de um trecho, com a medida em cima"""
    E.chave(c, x0, x1, y, cor or TINTA2, ep(t, t0, 0.5), -22)
    E.foco(c, t, t0 + 0.2, 0.5, lambda a: centro(c, rot, (x0 + x1) / 2, y - 44, size, "g", cor or TINTA, a))


def horas(c, x, y, w, h, n, cheio, a, rotulos=(), cor=None):
    """n blocos de 1 hora lado a lado (largura w cada); cheio = horas pintadas (2,5 enche dois e meio)"""
    if a <= 0:
        return
    cor = cor or E.COR
    for i in range(n):
        xi = x + i * (w + 16)
        M.rrect(c, xi, y, w, h, 16, BR, a)
        f = M.clamp(cheio - i)
        if f > 0:
            M.rrect(c, xi, y, w * f, h, 16, cor, a)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(xi, y, w, h), 16, 16), M.paint(TINTA, a, stroke=3))
    for i, s, q, est in rotulos:
        if q > 0:
            centro(c, s, x + i * (w + 16) + (w / 2 if i == int(i) else 0), y + h + 70, 52, est, TINTA, a * q)


def pacote(c, cx, cy, kg, cor, a):
    """saco de produto com o peso escrito"""
    if a <= 0:
        return
    p = skia.Path()
    p.moveTo(cx - 120, cy - 110); p.lineTo(cx + 120, cy - 110); p.lineTo(cx + 140, cy + 130); p.lineTo(cx - 140, cy + 130); p.close()
    c.drawPath(p, M.paint(cor, a))
    M.rrect(c, cx - 90, cy - 140, 180, 40, 14, cor, a)
    centro(c, kg, cx, cy + 40, 96, "g", BR, a)


def dois_lados(c, t, t0, esq, dir_, y, size=96, cor=TINTA, op=None, top=None):
    """'1 L —→ 12 km': as duas pontas e a seta com a pílula"""
    fcen(c, t, t0, esq, 620, y, size, cor)
    if op:
        E.ponte(c, t, t0 + 0.3, 820, 1100, y - size * 0.34, op, None, 44)
    elif t >= t0 + 0.3:
        p = ep(t, t0 + 0.3, 0.4)
        M.arrow(c, 820, y - size * 0.34, 1100, y - size * 0.34, TINTA2, p, 5, 18, p)
    fcen(c, t, top if top is not None else t0 + 0.6, dir_, 1350, y, size, COR)


# ---------------- gancho ----------------
X0, X1 = 260, 1660


def b_gancho(c, t, C, b):
    a1, b1, c1, d1 = C["s01.a"], C["s01.b"], C["s01.c"], C["s01.d"]

    def cena():
        E.frase(c, t, lerp(b1, c1, 0.45), ps("qual foi a", "i", 84) + [("velocidade?", "g", 88, COR)], W / 2, 180, "center", 0.12)
        E.foco(c, t, C["s01"], 0.5, lambda a: estrada(c, X0, X1, 540, a, ease_io(prog(t, a1, max(1.0, c1 - a1)))))
        medida(c, t, a1, X0, X1, 420, "180 km")
        E.frase(c, t, b1, ps("em", "i", 76) + [("2 h 30 min", "g", 84, COR)], W / 2, 680, "center", 0.12)
        E.linha(c, t, [("2 h 30 min", "g", 84, TINTA, c1 - 0.2), ("=", "g", 84, TINTA, c1), ("2,3 h", "g", 92, ERRADO, c1 + 0.2)], W / 2, 860, "center")
        if t >= d1 - 0.2:
            E.risco(c, W / 2 + 160, 880, W / 2 + 400, 780, t, d1 - 0.2, TINTA, 10)
        E.frase(c, t, d1, ps("errou", "i", 70) + [("antes da conta", "g", 72, ERRADO)], W / 2, 1000, "center", 0.12)
    E.saida(c, t, C["s02"] - 0.1, cena)

    if t >= C["s02"]:
        ta, tb = C["s02.a"], C["s02.b"]
        E.foco(c, t, tb - 0.2, 0.7, lambda a: E.bola(c, 1500, 540, 250 * ease_back(prog(t, tb - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, ps("até o fim desta aula", "i", 90), XE, 300, passo=0.14)
        E.frase(c, t, lerp(ta, tb, 0.15), [("ler", "g", 110, COR)] + ps("qualquer taxa", "i", 100), XE, 460, passo=0.14)
        E.frase(c, t, lerp(ta, tb, 0.4), [("velocidade média", "g", 92, COR)], XE, 600, passo=0.12)
        E.frase(c, t, lerp(ta, tb, 0.65), ps("e o", "i", 84) + [("tempo da viagem", "g", 84)], XE, 730, passo=0.12)
        E.foco(c, t, tb + 0.1, 0.5, lambda a: (centro(c, "+ atalho", 1500, 525, 80, "g", E.SOBRE, a),
                                               centro(c, "de prova", 1500, 610, 80, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"] + 0.3, ps("você só precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "4", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 225, 700, 120, "i", TINTA, a))
    x, w, hh = 960, 800, 170
    itens = (("s03.b", "o que é", "razão"), ("s03.c", "horas e minutos", "em hora decimal"), ("s03.d", "dividir por", "número com vírgula"),
             ("s03.e", "isolar uma letra", "numa fórmula"))
    for i, (k, l1, l2) in enumerate(itens):
        y = 90 + i * 205
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, hh, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 54)], x + 40, y + 72)
        E.frase(c, t, C[k] + 0.3, [(l2, "g", 54, COR)], x + 40, y + 140)
    alvo = [C[k] for k, _, _ in itens]
    ys = [90 + i * 205 + 150 for i in range(4)]
    py = ys[0]
    for j in range(1, 4):
        py = lerp(py, ys[j], ease_io(prog(t, alvo[j] - 0.35, 0.5)))
    E.cursor(c, x + w - 30, py, ep(t, C["s03.b"], 0.4))
    E.frase(c, t, lerp(C["s03.e"], C["s03.end"], 0.55), ps("faltou alguma?", "i", 54, COR) + ps("procure no canal", "i", 54, TINTA2), x, 1020, "left", 0.1)


# ---------------- taxa ----------------
def b_taxa(c, t, C, b):
    a4, b4, c4, d4 = C["s04.a"], C["s04.b"], C["s04.c"], C["s04.d"]

    def ideia():
        E.frase(c, t, C["s04"] + 0.3, [("razão:", "g", 72, COR)] + ps("comparar dois números pela divisão", "i", 66), W / 2, 200, "center", 0.1)
        E.foco(c, t, a4, 0.5, lambda a: E.pilula(c, "quilômetro", 700, 400, 64, "g", fundo=TINTA, a=a))
        E.foco(c, t, a4 + 0.2, 0.4, lambda a: centro(c, "e", 960, 422, 70, "i", TINTA, a))
        E.foco(c, t, a4 + 0.4, 0.5, lambda a: E.pilula(c, "litro", 1180, 400, 64, "g", fundo=TINTA, a=a))
        E.frase(c, t, lerp(a4, b4, 0.2), ps("tipos diferentes", "i", 56, TINTA2), W / 2, 520, "center", 0.1)
        E.frase(c, t, b4, ps("a razão vira", "i", 84) + [("taxa", "g", 140, COR)], W / 2, 720, "center", 0.12)
        E.linha(c, t, [("“por”", "g", 100, COR, c4), ("=", "g", 90, TINTA, d4 - 0.3), ("dividido por", "i", 100, TINTA, d4)], W / 2, 920, "center")
    E.saida(c, t, C["s05"] - 0.1, ideia)

    a5, b5, c5, d5 = C["s05.a"], C["s05.b"], C["s05.c"], C["s05.d"]
    if C["s05"] <= t:
        def litro():
            fcen(c, t, a5, "12 km/L", W / 2, 260, 150, COR)
            E.frase(c, t, a5 + 0.8, ps("12 km por litro = 12 km ÷ 1 L", "i", 56, TINTA2), W / 2, 360, "center", 0.06)
            dois_lados(c, t, b5, "1 L", "12 km", 560, 100)
            dois_lados(c, t, c5, "40 L", "480 km", 760, 100, op="× 40", top=d5 + 0.4)
            fcen(c, t, d5, "12 × 40 = 480", W / 2, 940, 84, TINTA)
        E.saida(c, t, C["s06"] - 0.1, litro)

    a6, b6, c6, d6 = C["s06.a"], C["s06.b"], C["s06.c"], C["s06.d"]
    if C["s06"] <= t:
        def quilo():
            fcen(c, t, a6, "R$ 30/kg", W / 2, 260, 150, COR)
            dois_lados(c, t, b6, "1 kg", "R$ 30", 500, 100)
            dois_lados(c, t, c6 - 0.4, "0,5 kg", "R$ 15", 700, 100, op="÷ 2", top=c6 + 0.2)
            E.frase(c, t, d6, ps("a taxa diz", "i", 76) + [("quanto vale 1 unidade", "g", 76, COR)], W / 2, 900, "center", 0.12)
            E.frase(c, t, lerp(d6, C["s06.end"], 0.6), ps("e serve para comparar", "i", 60, TINTA2), W / 2, 1010, "center", 0.1)
        E.saida(c, t, C["s07"] - 0.1, quilo)

    if t < C["s07"]:
        return
    a7, b7, c7, d7, e7 = (C[f"s07.{k}"] for k in "abcde")
    E.frase(c, t, lerp(b7, c7, 0.25), ps("qual", "i", 84) + [("compensa?", "g", 88, COR)], W / 2, 150, "center", 0.12)
    for cx, k, kg, preco, conta, ck, cor in ((560, a7, "2 kg", "R$ 50", "50 ÷ 2 = R$ 25/kg", c7, TINTA), (1360, b7, "3 kg", "R$ 72", "72 ÷ 3 = R$ 24/kg", d7, COR)):
        E.foco(c, t, k, 0.5, lambda a, cx=cx, kg=kg, cor=cor: pacote(c, cx, 380, kg, cor, a))
        fcen(c, t, k + 0.5, preco, cx, 640, 96, TINTA)
        fcen(c, t, ck, conta, cx, 800, 64, cor if cor == COR else TINTA)
    if t >= e7:
        p = ep(t, e7, 0.5)
        E.caixa_pontilhada(c, 1040, 220, 640, 620, p, CERTO, prog_=p)
    E.frase(c, t, e7 + 0.2, ps("o pacote maior", "i", 72) + [("sai mais barato", "g", 76, CERTO)], W / 2, 980, "center", 0.12)


# ---------------- velocidade média ----------------
def b_velocidade(c, t, C, b):
    a8, b8, c8, e8 = C["s08.a"], C["s08.b"], C["s08.c"], C["s08.end"]

    def ideia():
        fcen(c, t, a8 - 0.4, "km/h", 640, 270, 150, COR)
        E.frase(c, t, a8 + 0.4, ps("= km ÷ h", "i", 90), 880, 260, "left", 0.12)
        E.frase(c, t, b8 - 0.4, [("velocidade média", "g", 76, COR)], W / 2, 450, "center")
        fcen(c, t, b8 + 0.4, "= f{distância total}{tempo total}", W / 2, 600, 72)
        tr = lerp(b8, c8, 0.55)  # "o ônibus acelera e freia"
        if t >= tr:
            u = prog(t, tr, max(1.0, e8 - tr))
            pos = u if t >= c8 else M.clamp(u + 0.035 * math.sin(u * 26))  # acelera e freia; no "ritmo só" anda reto
            E.foco(c, t, tr, 0.5, lambda a: estrada(c, X0, X1, 880, a, pos))
        E.frase(c, t, c8, ps("como se fosse", "i", 64) + [("num ritmo só", "g", 66, COR)], W / 2, 1010, "center", 0.12)
    E.saida(c, t, C["s09"] - 0.1, ideia)

    a9, b9, c9 = C["s09.a"], C["s09.b"], C["s09.c"]
    if C["s09"] <= t:
        def tempo():
            E.frase(c, t, C["s09"] + 0.2, ps("o ônibus:", "i", 72) + [("180 km", "g", 76, COR)] + ps("em", "i", 72) + [("2 h 30 min", "g", 76)],
                    W / 2, 180, "center", 0.12)
            cheio = 2 * ep(t, a9, 0.8) + 0.5 * ep(t, b9, 0.6)
            rot = [(0, "1 h", ep(t, a9, 0.4), "g"), (1, "1 h", ep(t, a9 + 0.3, 0.4), "g"), (2, "30 min", ep(t, b9, 0.4), "g")]
            E.foco(c, t, a9 - 0.2, 0.5, lambda a: horas(c, 420, 300, 340, 150, 3, cheio, a, rot))
            E.foco(c, t, b9 + 0.5, 0.5, lambda a: centro(c, "meia hora = 0,5 h", 420 + 2 * 356 + 170, 590, 48, "i", COR, a))
            E.frase(c, t, c9 - 0.3, ps("tempo =", "i", 96) + [("2,5 h", "g", 120, COR)], W / 2, 820, "center", 0.12)
        E.saida(c, t, C["s10"] - 0.1, tempo)

    if t < C["s10"]:
        return
    a0, b0, c0 = C["s10.a"], C["s10.b"], C["s10.c"]
    fcen(c, t, a0, "180 ÷ 2,5", 700, 300, 120)
    E.foco(c, t, lerp(a0, b0, 0.4), 0.5, lambda a: E.pilula(c, "× 10 nos dois", 700, 430, 56, "g", a=a))
    fcen(c, t, b0, "1.800 ÷ 25", 700, 600, 120)
    fcen(c, t, c0, "= 72 km/h", 700, 820, 120, COR)
    bola_res(c, t, c0 + 0.6, "72 km/h", 1500, 560, 200, 84)


# ---------------- tempo ----------------
def b_tempo(c, t, C, b):
    a1, b1, c1, d1 = C["s11.a"], C["s11.b"], C["s11.c"], C["s11.d"]

    def isola():
        E.frase(c, t, C["s11"] + 0.2, ps("e quando a pergunta é o", "i", 76) + [("tempo?", "g", 80, COR)], W / 2, 170, "center", 0.12)
        E.linha(c, t, [("240 km", "g", 96, TINTA, a1), ("a", "i", 90, TINTA, b1 - 0.2), ("80 km/h", "g", 96, COR, b1)], W / 2, 340, "center")
        fcen(c, t, c1, "tempo = f{distância}{velocidade}", W / 2, 560, 90)
        fcen(c, t, d1, "f{240}{80} = 3 h", 760, 840, 120)
        bola_res(c, t, d1 + 1.0, "3 h", 1400, 800, 120, 90)
    E.saida(c, t, C["s12"] - 0.1, isola)
    if t < C["s12"]:
        return
    a2, b2, e2 = C["s12.a"], C["s12.b"], C["s12.end"]
    E.frase(c, t, C["s12"] + 0.2, ps("confira pelo", "i", 76) + [("outro lado", "g", 80, COR)], W / 2, 170, "center", 0.12)
    x0, x1 = 360, 1560
    seg = (x1 - x0) / 3
    pos = ease_io(prog(t, a2, max(1.0, b2 - a2)))
    E.foco(c, t, C["s12"] + 0.3, 0.5, lambda a: estrada(c, x0, x1, 480, a, pos))
    for i in range(3):
        k = lerp(a2, b2, i / 3)
        medida(c, t, k, x0 + i * seg + 10, x0 + (i + 1) * seg - 10, 370, "80 km", COR, 56)
        E.foco(c, t, k + 0.2, 0.5, lambda a, i=i: centro(c, "1 h", x0 + (i + 0.5) * seg, 600, 56, "i", TINTA, a))
    fcen(c, t, b2, "80 × 3 = 240 km", W / 2 - 40, 800, 104, CERTO)
    E.foco(c, t, b2 + 1.2, 0.5, lambda a: E.selo(c, W / 2 + 470, 765, 48, True, a))
    E.frase(c, t, lerp(b2, e2, 0.45), ps("a conferência pega a conta", "i", 58, TINTA2) + [("feita ao contrário", "g", 58)], W / 2, 980, "center", 0.08)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    a3, b3, c3, d3, e3 = C["s13.a"], C["s13.b"], C["s13.c"], C["s13.d"], C["s13.end"]
    E.frase(c, t, C["s13"] + 0.2, ps("o erro:", "i", 80) + [("30 min não é 0,3 h", "g", 84, ERRADO)], W / 2, 170, "center", 0.12)
    E.linha(c, t, [("2 h 30 min", "g", 96, TINTA, a3), ("→", "g", 90, TINTA, a3 + 0.5), ("2,3 h", "g", 96, ERRADO, a3 + 0.8)], W / 2, 350, "center")
    E.foco(c, t, a3 + 1.4, 0.5, lambda a: E.selo(c, 1560, 318, 46, False, a))
    E.linha(c, t, [("180 ÷ 2,3 = 78,26...", "g", 84, ERRADO, b3), ("perto de 78", "i", 72, ERRADO, c3)], W / 2, 520, "center")
    E.linha(c, t, [("0,3 h", "g", 96, TINTA, d3 - 0.4), ("=", "g", 90, TINTA, d3 - 0.2), ("18 min", "g", 96, COR, d3), ("não 30", "i", 80, ERRADO, d3 + 0.8)],
           W / 2, 720, "center")
    E.foco(c, t, lerp(d3, e3, 0.55), 0.5, lambda a: E.pilula(c, "1 hora = 60 minutos, não 10", W / 2, 900, 66, "g", a=a))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    a4, b4, c4, d4 = C["s14.a"], C["s14.b"], C["s14.c"], C["s14.d"]

    def dobra():
        E.frase(c, t, C["s14"] + 0.1, ps("agora, o atalho", "i", 70, CLARO), W / 2, 160, "center", 0.12)
        E.frase(c, t, a4, ps("tem meia hora?", "i", 92, CLARO) + [("dobre tudo", "g", 100, BR)], W / 2, 300, "center", 0.12)
        fcen(c, t, b4, "180 km em 2,5 h", W / 2, 470, 96, CLARO)
        if t >= c4 - 0.4:
            for x in (720, 1220):
                p = ep(t, c4 - 0.4, 0.4)
                M.arrow(c, x, 500, x, 580, BR, p, 5, 16, p)
                E.foco(c, t, c4 - 0.4, 0.4, lambda a, x=x: E.pilula(c, "× 2", x + 90, 545, 40, "g", a=a))
        fcen(c, t, c4, "360 km em 5 h", W / 2, 680, 96, BR)
        fcen(c, t, d4, "360 ÷ 5 = 72 km/h", W / 2, 900, 110, BR)
    E.saida(c, t, C["s15"] - 0.1, dobra)
    if t < C["s15"]:
        return
    a5, b5, c5, e5 = C["s15.a"], C["s15.b"], C["s15.c"], C["s15.end"]
    fcen(c, t, a5, "f{180}{2,5} = f{360}{5}", W / 2, 300, 110, BR)
    E.frase(c, t, a5 + 1.2, ps("dobrar os dois", "i", 66, CLARO) + [("não muda a velocidade", "g", 68, BR)], W / 2, 460, "center", 0.1)
    E.foco(c, t, b5, 0.5, lambda a: E.selo(c, 330, 650, 50, False, a))
    E.frase(c, t, b5 + 0.1, ps("os minutos", "i", 72, CLARO) + [("não fazem meia hora?", "g", 76, BR)], 420, 675, "left", 0.1)
    E.frase(c, t, c5, ps("como em", "i", 72, CLARO) + [("2 h 20 min", "g", 80, BR)], 420, 800, "left", 0.1)
    E.frase(c, t, lerp(c5, e5, 0.45), ps("aí,", "i", 80, CLARO) + [("converta e divida", "g", 84, BR)], W / 2, 960, "center", 0.12)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    a6, b6, c6, d6 = C["s16.a"], C["s16.b"], C["s16.c"], C["s16.d"]
    E.frase(c, t, C["s16"] + 0.2, ps("hora de testar", "i", 72, COR), XE, 180, passo=0.12)
    E.linha(c, t, [("a ciclista fez", "i", 80, TINTA, a6 - 0.6), ("45 km", "g", 88, COR, a6)], XE, 340)
    E.linha(c, t, [("em", "i", 80, TINTA, b6 - 0.2), ("1 h 30 min", "g", 88, COR, b6)], XE, 460)
    E.frase(c, t, c6, ps("velocidade média?", "g", 80), XE, 640, passo=0.12)
    E.frase(c, t, d6, ps("e o tempo para", "i", 80) + [("150 km?", "g", 84, COR)], XE, 790, passo=0.12)
    E.relogio(c, t, C["s17.a"], 1590, 430, 170)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    a8, b8, c8 = C["s18.a"], C["s18.b"], C["s18.c"]

    def vel():
        fcen(c, t, a8, "1 h 30 min = 1,5 h", W / 2, 230, 96)
        E.frase(c, t, lerp(a8, b8, 0.5), ps("pelo atalho,", "i", 70, TINTA2) + [("dobre tudo", "g", 72, COR)], W / 2, 380, "center", 0.1)
        fcen(c, t, b8, "90 km em 3 h", W / 2, 540, 104)
        fcen(c, t, c8, "90 ÷ 3 = 30 km/h", 760, 780, 104, COR)
        bola_res(c, t, c8 + 1.0, "30 km/h", 1500, 740, 150, 64)
    E.saida(c, t, C["s19"] - 0.1, vel)
    if t < C["s19"]:
        return
    a9, b9, c9 = C["s19.a"], C["s19.b"], C["s19.c"]
    fcen(c, t, a9, "tempo = f{distância}{velocidade}", W / 2, 280, 90)
    fcen(c, t, b9, "150 ÷ 30 = 5 h", 760, 560, 110, COR)
    bola_res(c, t, b9 + 1.0, "5 h", 1450, 520, 120, 90)
    fcen(c, t, c9, "30 × 5 = 150", W / 2 - 40, 840, 100, CERTO)
    E.foco(c, t, c9 + 1.2, 0.5, lambda a: E.selo(c, W / 2 + 330, 805, 46, True, a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s20"] + 0.2, [("resumindo", "i", 92, COR)], W / 2, 190, "center")
        itens = (("s20.a", "“por”", "= dividido"), ("s20.b", "velocidade média", "= distância total ÷ tempo total"),
                 ("s20.c", "minuto", "não é décimo de hora"))
        for i, (k, l1, l2) in enumerate(itens):
            y = 380 + i * 200
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 230, y - 30, 56, a=a), centro(c, str(i + 1), 230, y - 7, 64, "g", E.SOBRE, a)))
            E.frase(c, t, C[k] + 0.1, ps(l1, "i", 70) + [(l2, "g", 64, COR if i != 2 else ERRADO)], 320, y, "left", 0.1)
    E.saida(c, t, C["s21"] - 0.1, resumo)
    if t < C["s21"]:
        return
    a1, b1, c1, d1 = C["s21.a"], C["s21.b"], C["s21.c"], C["s21.d"]
    E.frase(c, t, C["s21"] + 0.2, ps("na próxima aula", "i", 84), XE, 240, passo=0.14)
    E.linha(c, t, [("km/h", "g", 140, COR, a1), ("→", "g", 120, TINTA, b1 - 0.3), ("m/s", "g", 140, COR, b1)], XE, 430)
    E.frase(c, t, lerp(b1, c1, 0.4), ps("com um número só", "i", 76), XE, 570, passo=0.12)
    E.foco(c, t, c1, 0.5, lambda a: E.pilula(c, "Inscreva-se", 1440, 790, 76, estilo="g", a=a, cor=E.SOBRE))
    p = ease_io(prog(t, c1 + 0.3, 0.8))
    E.cursor(c, lerp(1770, 1570, p), lerp(1020, 815, p), ep(t, c1 + 0.2, 0.4))
    E.frase(c, t, d1, [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 960, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, taxa=b_taxa, velocidade=b_velocidade, tempo=b_tempo, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
