"""Visual — Estudativo · FIS-MAG-007: transformadores e transmissão. Linguagem visual do Magnetismo: veja o visual.py da FIS-MAG-001.
O transformador é um anel de ferro cinza com a bobina primária (à esquerda) e a secundária (à direita) em tinta; o fluxo que
anda no ferro são setinhas laranja que trocam de sentido (corrente alternada). Perda nos fios = calor em vermelho.
Todo instante vem de C[...]."""
import math

import editorial as E
import fisica as F
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Física", "Magnetismo")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_FIS-MAG-007_transformadores_e_transmissao.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("transf", "potencia", "linha", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
FERRO = "#9AA0A8"

# todas as contas da aula
assert 220 * 60 / 1100 == 12 and 1100 / 60 == 220 / 12
assert 100e3 / 1e3 == 100 and 5 * 100 ** 2 == 50e3 and 50e3 / 100e3 == 0.5
assert 100e3 / 1e4 == 10 and 5 * 10 ** 2 == 500 and 50e3 / 500 == 100
assert 4000 / 200 == 20 and 11e3 * 20 == 220e3 and 20 ** 2 == 400
assert 10 ** 2 == 100  # tensão vezes dez, perda dividida por cem


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def lembrete2(c, t, C, cena, itens, desenhos):
    """lembrete de duas coisas (o mesmo da FIS-CIN-001)"""
    E.frase(c, t, C[cena] + 0.2, ps("lembre", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C[cena + ".a"], 0.5, lambda a: E.escreve(c, "2", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C[cena + ".a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 820, 1000
    for i, (k, l1, l2) in enumerate(itens):
        y = 230 + i * 290
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 230, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 58)], x + 44, y + 90)
        E.frase(c, t, C[k] + 0.3, [(l2, "g", 58, COR)], x + 44, y + 170)
        E.foco(c, t, C[k] + 0.6, 0.5, lambda a, i=i, y=y: desenhos[i](a, x + w - 170, y + 115))
    q1 = ease_io(prog(t, C[itens[1][0]] - 0.35, 0.5))
    E.cursor(c, x + w - 30, lerp(430, 720, q1), ep(t, C[itens[0][0]], 0.4))
    E.frase(c, t, lerp(C[itens[1][0]], C[cena + ".end"], 0.6), ps("faltou alguma?", "i", 56, COR) + ps("procure no canal", "i", 56), 820, 920, "left", 0.12)


def troca(c, t, itens, fn):
    for i, (ti, s) in enumerate(itens):
        fim = itens[i + 1][0] - 0.1 if i + 1 < len(itens) else 1e9
        if t >= ti - 0.01:
            E.saida(c, t, fim, lambda s=s, ti=ti: E.foco(c, t, ti, 0.45, lambda a: fn(s, a)), d=0.25)


def bola_txt(c, t, t0, s, cx, cy, r, size, cor=None):
    v, _, u = s.partition(" ")
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r * ease_back(prog(t, t0, 0.5)), cor, a),
                                     F.medida(c, v, u, cx, cy + size * 0.36, size, E.SOBRE, a, "center", cor_u=E.SOBRE)))


def transformador(c, t, cx, cy, w, h, n1, n2, a=1.0, a1=1.0, a2=1.0, fluxo=None, alterna=True):
    """anel de ferro (w x h) com a primária no lado esquerdo (n1 voltas) e a secundária no direito (n2 voltas).
    fluxo = instante em que as setinhas do fluxo começam a andar no ferro; alterna = elas trocam de sentido"""
    if a <= 0:
        return
    e = 70
    M.rrect(c, cx - w / 2, cy - h / 2, w, h, 20, FERRO, a)
    M.rrect(c, cx - w / 2 + e, cy - h / 2 + e, w - 2 * e, h - 2 * e, 10, E.PAPEL, a)
    for lado, n, ab in ((-1, n1, a1), (1, n2, a2)):
        if ab <= 0:
            continue
        xl = cx + lado * (w / 2 - e / 2)
        alto = h * 0.62
        for k in range(n):
            y = cy - alto / 2 + alto * (k + 0.5) / n
            M.line(c, xl - e / 2 - 14, y, xl + e / 2 + 14, y - 10, TINTA, a * ab, 7)
    if fluxo is not None and t >= fluxo:
        s = math.cos((t - fluxo) * 2.0) if alterna else 1.0
        q = ep(t, fluxo, 0.4) * a * min(1.0, abs(s) * 2)
        pts = [(cx - w / 2 + e / 2, cy + h / 2 - e / 2), (cx - w / 2 + e / 2, cy - h / 2 + e / 2),
               (cx + w / 2 - e / 2, cy - h / 2 + e / 2), (cx + w / 2 - e / 2, cy + h / 2 - e / 2)]
        if s < 0:
            pts = pts[::-1]
        F.corrente(c, t, fluxo, pts, cor=E.COR, espaco=150, a=q)


def torre(c, x, yb, s, a=1.0):
    """torre de transmissão simples"""
    if a <= 0:
        return
    for d in (-1, 1):
        M.line(c, x + d * s * 0.35, yb, x + d * s * 0.08, yb - s * 1.6, TINTA, a, 5)
    for k in range(4):
        y = yb - s * 0.4 * k
        M.line(c, x - s * 0.35 + s * 0.07 * k, y, x + s * 0.35 - s * 0.07 * k, y - s * 0.4, TINTA2, a, 3)
    M.line(c, x - s * 0.55, yb - s * 1.45, x + s * 0.55, yb - s * 1.45, TINTA, a, 6)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    if t < C["s02"]:
        y = 640
        E.foco(c, t, C["s01.a"], 0.5, lambda a: [torre(c, x, y + 200, 200, a) for x in (560, 1000, 1440)])
        if t >= C["s01.a"] + 0.4:
            for x0, x1 in ((560, 1000), (1000, 1440)):
                p = skia.Path(); p.moveTo(x0, y - 90); p.quadTo((x0 + x1) / 2, y - 30, x1, y - 90)
                c.drawPath(p, M.paint(TINTA, ep(t, C["s01.a"] + 0.4, 0.4), stroke=4))
        E.foco(c, t, C["s01.a"] + 0.2, 0.4, lambda a: E.pilula(c, "usina", 300, y + 100, 56, "g", fundo=TINTA, a=a))
        E.foco(c, t, C["s01.b"], 0.5, lambda a: E.pilula(c, "centenas de milhares de volts", 1000, 340, 56, "g", fundo=E.COR, a=a))
        E.foco(c, t, C["s01.c"], 0.5, lambda a: E.pilula(c, "tomada: 127 V ou 220 V", 1480, y + 280, 50, "g", fundo=TINTA, a=a))
        E.frase(c, t, C["s01.d"], ps("por que", "i", 80) + [("subir e baixar?", "g", 80, COR)], XE, 200, passo=0.12)
        return
    tb = C["s02.a"] + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1480, 540, 330 * ease_back(prog(t, tb, 0.8)), giro=12 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 88), XE, 280, passo=0.14)
    for i, (k, s, dt) in enumerate((("s02.a", "calcular a tensão", 1.2), ("s02.b", "por que tensão alta", 0))):
        y = 470 + i * 170
        E.foco(c, t, C[k] + dt, 0.5, lambda a, i=i, y=y: (E.bola(c, XE + 40, y - 30, 38, a=a), centro(c, str(i + 1), XE + 40, y - 8, 48, "g", BR, a)))
        E.frase(c, t, C[k] + dt + 0.1, [(s, "g", 74, COR if i == 0 else TINTA)], XE + 110, y)
    E.frase(c, t, C["s02.b"] + 0.8, ps("quase acaba com a perda", "i", 60, TINTA2), XE + 110, 760, passo=0.1)


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    def far(a, x, y):
        E.formula(c, "ε = f{ΔΦ}{Δt}", x + 10, y + 30, 56, "g", TINTA, a, "center")

    def pot(a, x, y):
        E.formula(c, "P = U · i", x - 20, y - 10, 46, "g", TINTA, a, "center")
        E.formula(c, "perda = r · i^2", x - 20, y + 60, 46, "g", TINTA, a, "center")
    lembrete2(c, t, C, "s03", (("s03.b", "Faraday:", "fluxo muda: tensão"), ("s03.c", "potência e perda:", "U · i  e  r · i²")), (far, pot))


# ---------------- o transformador ----------------
def b_transf(c, t, C, b):
    cx, cy, w, h = 1350, 580, 640, 560
    if t < C["s07"]:
        n1 = 8
        n2 = 4
        flux = C["s05.b"] if t >= C["s05"] else None
        transformador(c, t, cx, cy, w, h, n1, n2, ep(t, C["s04.a"], 0.5), ep(t, C["s04.c"], 0.4), ep(t, C["s04.d"], 0.4), flux)
        E.foco(c, t, C["s04.c"], 0.4, lambda a: centro(c, "primária", cx - w / 2 + 35, cy + h / 2 + 70, 50, "g", TINTA, a))
        E.foco(c, t, C["s04.d"], 0.4, lambda a: centro(c, "secundária", cx + w / 2 - 35, cy + h / 2 + 70, 50, "g", TINTA, a))
        E.foco(c, t, C["s04.a"], 0.4, lambda a: centro(c, "ferro", cx, cy - h / 2 - 30, 46, "i", TINTA2, a))
        if t < C["s05"]:
            E.frase(c, t, C["s04"], [("o", "i", 90), ("transformador", "g", 90, COR)], XE, 220)
            E.frase(c, t, C["s04.b"], ps("duas bobinas num", "i", 60) + [("anel de ferro", "g", 60)], XE, 380, passo=0.12)
            return
        if t < C["s06"]:
            E.frase(c, t, C["s05.a"], [("corrente", "g", 64, COR), ("alternada", "g", 64, COR)], XE, 220, passo=0.12)
            E.frase(c, t, C["s05.a"] + 0.6, ps("vai e volta o tempo todo", "i", 56, TINTA2), XE, 310, passo=0.1)
            E.frase(c, t, C["s05.b"], ps("campo muda o tempo todo", "i", 56), XE, 450, passo=0.1)
            E.frase(c, t, C["s05.c"], ps("o ferro leva o fluxo", "i", 56), XE, 550, passo=0.1)
            E.frase(c, t, C["s05.d"], [("Faraday:", "g", 56, COR), ("tensão na secundária", "i", 56)], XE, 650, passo=0.1)
            E.foco(c, t, C["s05.e"], 0.5, lambda a: E.pilula(c, "nenhum fio liga as duas", XE + 290, 800, 50, "g", fundo=TINTA, a=a))
            return
        E.frase(c, t, C["s06.a"], ps("cada espira: a", "i", 60) + [("mesma tensão", "g", 60, COR)], XE, 220, passo=0.1)
        E.frase(c, t, C["s06.b"], [("mais espiras,", "g", 60), ("mais tensão", "i", 64)], XE, 330, passo=0.12)
        E.formula_em(c, t, C["s06.c"], "f{U₁}{U₂} = f{N₁}{N₂}", XE, 560, 130, "g", TINTA)
        E.foco(c, t, C["s06.d"], 0.4, lambda a: E.escreve(c, "U: tensão (V)", XE, 760, 54, "b", TINTA2, a))
        E.foco(c, t, C["s06.e"], 0.4, lambda a: E.escreve(c, "N: número de espiras", XE, 840, 54, "b", TINTA2, a))
        return
    if t < C["s08"]:
        dados = (("s07.a", "U₁ = 220 V,   N₁ = 1.100"), ("s07.b", "N₂ = 60"))
        for i, (k, s) in enumerate(dados):
            E.foco(c, t, C[k], 0.5, lambda a, i=i, s=s: E.formula(c, s, XE, 230 + 110 * i, 66, "g", TINTA, a))
        troca(c, t, [(C["s07.c"], "f{220}{U₂} = f{1.100}{60}"), (C["s07.d"], "U₂ = f{220 · 60}{1.100}")],
              lambda s, a: E.formula(c, s, XE, 600, 110, "g", TINTA, a))
        bola_txt(c, t, C["s07.e"], "12 V", 1450, 560, 170, 100)
        E.foco(c, t, C["s07.e"] + 0.6, 0.4, lambda a: centro(c, "carregador antigo", 1450, 820, 50, "i", TINTA2, a))
        return
    E.frase(c, t, C["s08.a"], ps("com uma", "i", 76) + [("pilha?", "g", 76, ERRADO)], XE, 220, passo=0.12)
    transformador(c, t, cx, cy, w, h, 8, 4, 1, 1, 1, C["s08.b"], alterna=False)
    E.frase(c, t, C["s08.b"], [("contínua:", "g", 60), ("fluxo parado", "i", 64)], XE, 420, passo=0.12)
    E.foco(c, t, C["s08.c"], 0.5, lambda a: E.pilula(c, "não cria tensão", XE + 220, 580, 56, "g", fundo=ERRADO, a=a))


# ---------------- potência ----------------
def b_potencia(c, t, C, b):
    E.frase(c, t, C["s09"], ps("o que a prova", "i", 76) + [("mais cobra", "g", 76, COR)], XE, 220, passo=0.12)
    E.foco(c, t, C["s09.a"], 0.5, lambda a: E.pilula(c, "não cria energia", XE + 230, 360, 60, "g", fundo=TINTA, a=a))
    E.frase(c, t, C["s09.b"], ps("a potência que entra", "i", 64) + [("é a que sai", "g", 64, COR)], XE, 520, passo=0.12)
    E.formula_em(c, t, C["s09.c"], "U₁ · i₁ = U₂ · i₂", W / 2, 720, 130, "g", TINTA, "center")
    E.foco(c, t, C["s09.d"], 0.5, lambda a: E.formula(c, "U ↑   →   i ↓", W / 2, 920, 100, "g", COR, a, "center"))


# ---------------- transmissão ----------------
def b_linha(c, t, C, b):
    if t < C["s12"]:
        E.frase(c, t, C["s10"], ps("transmitir", "i", 70) + [("100 kW", "g", 70, COR)] + ps("numa linha de", "i", 70) + [("5 Ω", "g", 70)], XE, 200, passo=0.12)
        y1, y2 = 420, 760
        E.foco(c, t, C["s10.a"], 0.5, lambda a: (E.pilula(c, "usina", 300, y1, 46, "g", fundo=TINTA, a=a), E.pilula(c, "cidade", 1700, y1, 46, "g", fundo=TINTA, a=a),
                                                 M.line(c, 400, y1 - 20, 1600, y1 - 20, TINTA, a, 6)))
        E.foco(c, t, C["s10.b"], 0.5, lambda a: E.formula(c, "1.000 V:   i = f{100.000}{1.000} = 100 A", 520, y1 - 70, 54, "g", TINTA, a))
        E.foco(c, t, C["s10.c"], 0.5, lambda a: E.formula(c, "perda = 5 · 100^2", 520, y1 + 90, 54, "g", TINTA, a))
        E.foco(c, t, C["s10.d"], 0.5, lambda a: E.pilula(c, "50.000 W", 1250, y1 + 70, 54, "g", fundo=ERRADO, a=a))
        E.foco(c, t, C["s10.e"], 0.5, lambda a: E.escreve(c, "metade vira calor!", 1420, y1 + 90, 46, "i", ERRADO, a))
        if t >= C["s11"]:
            E.foco(c, t, C["s11.a"], 0.5, lambda a: (E.pilula(c, "usina", 300, y2, 46, "g", fundo=TINTA, a=a), E.pilula(c, "cidade", 1700, y2, 46, "g", fundo=TINTA, a=a),
                                                     M.line(c, 400, y2 - 20, 1600, y2 - 20, TINTA, a, 6)))
            E.foco(c, t, C["s11.b"], 0.5, lambda a: E.formula(c, "10.000 V:   i = 10 A", 520, y2 - 70, 54, "g", TINTA, a))
            E.foco(c, t, C["s11.c"], 0.5, lambda a: E.formula(c, "perda = 5 · 10^2", 520, y2 + 90, 54, "g", TINTA, a))
            E.foco(c, t, C["s11.d"], 0.5, lambda a: E.pilula(c, "500 W", 1250, y2 + 70, 54, "g", fundo=CERTO, a=a))
            E.foco(c, t, C["s11.e"], 0.5, lambda a: E.pilula(c, "tensão × 10  →  perda ÷ 100", W / 2, 1000, 56, "g", fundo=E.COR, a=a))
        return
    pos = ((330, 760), (640, 560), (1000, 760), (1360, 560), (1650, 760))
    for i, (k, s) in enumerate((("s12.a", "usina"), ("s12.a", "sobe a tensão"), ("s12.b", "corrente pequena"), ("s12.c", "baixa a tensão"), ("s12.c", "sua casa"))):
        x, y = pos[i]
        E.foco(c, t, C[k] + 0.25 * (i % 2), 0.5, lambda a, x=x, y=y, s=s, i=i: E.pilula(c, s, x, y, 48, "g", fundo=E.COR if i in (1, 3) else TINTA, a=a))
        if i:
            x0, y0 = pos[i - 1]
            E.foco(c, t, C[k] + 0.25 * (i % 2), 0.4, lambda a, x0=x0, y0=y0, x=x, y=y: F.seta(c, x0 + (x - x0) * 0.3, y0 + (y - y0) * 0.3 - 18, x0 + (x - x0) * 0.7, y0 + (y - y0) * 0.7 - 18, TINTA2, a, 6))
    E.frase(c, t, C["s12"], ps("o caminho da energia", "i", 76), XE, 260, passo=0.12)
    E.foco(c, t, C["s12.c"] + 0.6, 0.4, lambda a: E.escreve(c, "o transformador do poste", 1200, 480, 48, "i", TINTA2, a))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s13"], [("cuidado", "g", 96, ERRADO)], XE, 200)
    E.frase(c, t, C["s13.a"], ps("subiu a tensão,", "i", 64) + [("subiu a potência?", "g", 64, ERRADO)], XE, 320, passo=0.12)
    E.foco(c, t, C["s13.b"], 0.5, lambda a: E.formula(c, "U × 10", 500, 560, 110, "g", TINTA, a, "center"))
    E.foco(c, t, C["s13.b"] + 0.8, 0.5, lambda a: E.formula(c, "i ÷ 10", 1100, 560, 110, "g", TINTA, a, "center"))
    E.foco(c, t, C["s13.c"], 0.5, lambda a: E.pilula(c, "P = U · i: igual", W / 2 - 160, 760, 70, "g", fundo=CERTO, a=a))
    E.frase(c, t, C["s13.d"], ps("na vida real, ainda perde um pouco", "i", 54, TINTA2), XE, 940, passo=0.1)


# ---------------- atalho ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    if t < C["s15"]:
        E.frase(c, t, C["s14"], ps("agora, o atalho", "i", 76, CLARO), W / 2, 180, "center")
        E.frase(c, t, C["s14.a"], ps("a tensão", "i", 70, CLARO) + [("segue as espiras", "g", 70, BR)], W / 2, 360, "center", 0.12)
        E.foco(c, t, C["s14.b"], 0.5, lambda a: E.formula(c, "N × 10  →  U × 10", W / 2, 500, 90, "g", E.CLARO, a, "center"))
        E.frase(c, t, C["s14.c"], ps("a corrente", "i", 70, CLARO) + [("ao contrário", "g", 70, BR)], W / 2, 720, "center", 0.12)
        E.foco(c, t, C["s14.d"], 0.5, lambda a: E.formula(c, "i ÷ 10", W / 2, 860, 90, "g", E.CLARO, a, "center"))
        return
    E.frase(c, t, C["s15"], ps("a perda vai com", "i", 70, CLARO) + [("i²", "g", 70, BR)], W / 2, 200, "center", 0.12)
    E.foco(c, t, C["s15.a"], 0.5, lambda a: E.formula(c, "U × k", 640, 440, 120, "g", BR, a, "center"))
    E.foco(c, t, C["s15.b"], 0.5, lambda a: (F.seta(c, 840, 405, 1000, 405, E.CLARO, a, 9), E.formula(c, "perda ÷ k^2", 1380, 440, 120, "g", E.CLARO, a, "center")))
    E.foco(c, t, C["s15.c"], 0.5, lambda a: E.pilula(c, "tensão × 10: perda ÷ 100", W / 2, 650, 64, "g", fundo=E.COR, a=a))
    E.frase(c, t, C["s15.d"], ps("vale para a mesma potência e a mesma linha", "i", 54, CLARO), W / 2, 880, "center", 0.08)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s16"], ps("hora de testar", "i", 72, COR), XE, 180)
    if t < C["s17"]:
        E.foco(c, t, C["s16.a"], 0.5, lambda a: E.formula(c, "N₁ = 200,   N₂ = 4.000", XE, 360, 72, "g", TINTA, a))
        E.foco(c, t, C["s16.b"], 0.5, lambda a: E.formula(c, "U₁ = 11.000 V", XE, 490, 72, "g", TINTA, a))
        E.foco(c, t, C["s16.c"], 0.5, lambda a: E.formula(c, "U₂ = ?", XE, 650, 90, "g", COR, a))
        E.frase(c, t, C["s16.d"], ps("a perda cai", "i", 60) + [("quantas vezes?", "g", 60, COR)], XE, 820, passo=0.12)
        transformador(c, t, 1450, 560, 480, 460, 3, 9, ep(t, C["s16.a"], 0.5))
    else:
        E.relogio(c, t, C["s17.a"], cx=1460, cy=500, r=200)
        E.foco(c, t, C["s17"], 0.4, lambda a: E.formula(c, "N₁ = 200,  N₂ = 4.000", XE, 400, 60, "g", TINTA, a))
        E.foco(c, t, C["s17"] + 0.2, 0.4, lambda a: E.formula(c, "U₁ = 11.000 V", XE, 500, 60, "g", TINTA, a))
        E.frase(c, t, C["s17"] + 0.4, [("U₂?", "g", 60, COR), ("perda?", "g", 60, COR)], XE, 620, passo=0.12)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    if t < C["s19"]:
        E.foco(c, t, C["s18.a"], 0.5, lambda a: E.formula(c, "f{4.000}{200} = 20", XE, 330, 110, "g", TINTA, a))
        E.foco(c, t, C["s18.b"], 0.4, lambda a: E.pilula(c, "20 vezes mais espiras", XE + 280, 480, 50, "g", fundo=TINTA, a=a))
        E.foco(c, t, C["s18.c"], 0.5, lambda a: E.formula(c, "11.000 × 20", XE, 700, 100, "g", TINTA, a))
        bola_txt(c, t, C["s18.d"], "220.000 V", 1400, 600, 220, 80)
        return
    E.foco(c, t, C["s19.a"], 0.5, lambda a: E.formula(c, "U × 20", 560, 340, 110, "g", TINTA, a, "center"))
    E.foco(c, t, C["s19.b"], 0.5, lambda a: E.formula(c, "i ÷ 20", 1360, 340, 110, "g", TINTA, a, "center"))
    E.foco(c, t, C["s19.c"], 0.5, lambda a: E.formula(c, "perda ÷ 20^2", W / 2, 600, 120, "g", TINTA, a, "center"))
    E.foco(c, t, C["s19.d"], 0.5, lambda a: E.pilula(c, "400 vezes menor", W / 2, 820, 80, "g", fundo=CERTO, a=a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s20"], [("resumindo", "i", 92, COR)], W / 2, 180, "center")
        itens = (("s20.a", [("a tensão", "i", 74), ("segue as espiras", "g", 70)]),
                 ("s20.b", [("potência:", "g", 70), ("a que entra é a que sai", "i", 74)]),
                 ("s20.c", [("tensão alta:", "g", 70), ("menos perda", "i", 74)]))
        for i, (k, partes) in enumerate(itens):
            y = 360 + i * 170
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 300, y - 26, 52, a=a), centro(c, str(i + 1), 300, y - 4, 60, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, partes, 400, y, passo=0.12)
        E.frase(c, t, C["s20.d"], ps("próxima aula:", "i", 60, TINTA2) + [("questões de magnetismo", "g", 60, COR)], W / 2, 920, "center", 0.1)
    E.saida(c, t, C["s21"] - 0.1, resumo)
    if t < C["s21"]:
        return
    E.foco(c, t, C["s21.a"], 0.5, lambda a: E.pilula(c, "Inscreva-se", W / 2, 460, 90, estilo="g", a=a))
    p = ease_io(prog(t, C["s21.a"] + 0.3, 0.8))
    E.cursor(c, lerp(1300, 1080, p), lerp(800, 490, p), ep(t, C["s21.a"] + 0.2, 0.4))
    E.frase(c, t, C["s21.b"], [("bons", "i", 110), ("estudos!", "i", 110, COR)], W / 2, 760, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, transf=b_transf, potencia=b_potencia, linha=b_linha, erro=b_erro, atalho=b_atalho,
              questao=b_questao, resposta=b_resposta, fim=b_fim)
