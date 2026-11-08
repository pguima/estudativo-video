"""Visual — Estudativo · MAT-EQU-020: montar sistema a partir do problema.
O molde aparece em três passos (o que cada letra conta, a equação das quantidades, a dos valores). No atalho, os 30 veículos
são ícones: todos começam motos e 20 viram carros, um por troca. Peças locais: carro, moto, ingresso, cedula, frota."""
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro, passo
import motor as M
import skia

E.usar("Matemática", "Equações do 1º Grau")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-EQU-020_montar_sistema_do_problema.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("teatro", "resolver", "atalho", "questao", "fim"))
BR = "#FFFFFF"
# as contas da aula
assert 70 + 80 == 150 and 40 * 70 + 20 * 80 == 4400 and 20 * 150 == 3000 and (4400 - 3000) / 20 == 70
assert 30 * 2 == 60 and 100 - 60 == 40 and 40 / 2 == 20 and 20 * 4 + 10 * 2 == 100
assert 25 * 10 == 250 and 380 - 250 == 130 and 130 / 10 == 13 and 13 * 20 + 12 * 10 == 380 and 13 + 12 == 25


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças desta aula ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def cen(c, t, t0, s, cx, y, size, cor=None, est="g"):
    E.foco(c, t, t0, 0.5, lambda a: centro(c, s, cx, y, size, est, cor or TINTA, a))


def fcen(c, t, t0, s, cx, y, size, cor=None):
    E.formula_em(c, t, t0, s, cx, y, size, "g", cor, "center")


def selo_em(c, t, t0, cx, cy, r, ok=True):
    E.foco(c, t, t0, 0.5, lambda a: E.selo(c, cx, cy, r * ease_back(prog(t, t0, 0.5)), ok, a), blur=0)


def carro(c, cx, cy, s, cor, a=1.0, fundo="#07070F"):
    """carro de lado: corpo, cabine e duas rodas à vista"""
    if a <= 0:
        return
    M.rrect(c, cx - s * 0.25, cy - s * 0.4, s * 0.5, s * 0.3, s * 0.1, cor, a)
    M.rrect(c, cx - s * 0.5, cy - s * 0.18, s, s * 0.3, s * 0.1, cor, a)
    for dx in (-0.28, 0.28):
        c.drawCircle(cx + s * dx, cy + s * 0.13, s * 0.14, M.paint(fundo, a))
        c.drawCircle(cx + s * dx, cy + s * 0.13, s * 0.1, M.paint(cor, a))


def moto(c, cx, cy, s, cor, a=1.0):
    """moto de lado: duas rodas, quadro e guidão"""
    if a <= 0:
        return
    r = s * 0.17
    w = max(3, s * 0.07)
    for dx in (-0.32, 0.32):
        c.drawCircle(cx + s * dx, cy + s * 0.1, r, M.paint(cor, a, stroke=w))
    p = skia.Path()
    p.moveTo(cx - s * 0.36, cy - s * 0.1); p.lineTo(cx - s * 0.12, cy - s * 0.2); p.lineTo(cx + s * 0.16, cy - s * 0.2)
    p.lineTo(cx + s * 0.2, cy - s * 0.04); p.lineTo(cx + s * 0.02, cy + s * 0.12); p.lineTo(cx - s * 0.14, cy + s * 0.12); p.close()
    c.drawPath(p, M.paint(cor, a))
    M.line(c, cx + s * 0.16, cy - s * 0.3, cx + s * 0.32, cy + s * 0.1, cor, a, w)
    M.line(c, cx + s * 0.08, cy - s * 0.32, cx + s * 0.24, cy - s * 0.32, cor, a, w)
    c.drawCircle(cx - s * 0.32, cy + s * 0.1, s * 0.05, M.paint(cor, a))
    c.drawCircle(cx + s * 0.32, cy + s * 0.1, s * 0.05, M.paint(cor, a))


def ingresso(c, cx, cy, s, cor, a=1.0):
    """ingresso com recortes nas pontas"""
    if a <= 0:
        return
    M.rrect(c, cx - s * 0.5, cy - s * 0.28, s, s * 0.56, s * 0.06, cor, a)
    for dx in (-0.5, 0.5):
        c.drawCircle(cx + s * dx, cy, s * 0.1, M.paint(E.PAPEL, a))
    M.line(c, cx + s * 0.22, cy - s * 0.2, cx + s * 0.22, cy + s * 0.2, E.PAPEL, a, 3, dash=[6, 6])


def cedula(c, cx, cy, s, valor, cor, a=1.0, rot=0):
    """cédula com o valor no meio"""
    if a <= 0:
        return
    c.save(); c.translate(cx, cy); c.rotate(rot)
    M.rrect(c, -s * 0.5, -s * 0.26, s, s * 0.52, s * 0.05, cor, a)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(-s * 0.44, -s * 0.2, s * 0.88, s * 0.4), s * 0.03, s * 0.03), M.paint(BR, 0.5 * a, stroke=3))
    centro(c, valor, 0, s * 0.11, s * 0.3, "g", BR, a)
    c.restore()


def frota(c, t, t0, trocas, x0, y0, passo_x=100, passo_y=128, s=82, a=1.0):
    """30 veículos em 3 fileiras de 10; trocas = instante em que o i-ésimo vira carro (lista)"""
    for i in range(30):
        cx, cy = x0 + (i % 10) * passo_x, y0 + (i // 10) * passo_y
        ti = t0 + i * 0.03
        ent = ep(t, ti, 0.4) * a
        if ent <= 0:
            continue
        q = ep(t, trocas[i], 0.35) if i < len(trocas) else 0
        if q < 1:
            moto(c, cx, cy, s, CLARO, ent * (1 - q))
        if q > 0:
            k = ease_back(q)
            c.save(); c.translate(cx, cy); c.scale(k, k)
            carro(c, 0, 0, s, BR, ent * q)
            c.restore()


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    ka, kb, kc = C["s01.a"], C["s01.b"], C["s01.c"]

    def um():
        E.frase(c, t, ka, [("30", "g", 150, COR)] + ps("veículos", "i", 120), XE, 300, passo=0.15)
        for i in range(5):
            E.foco(c, t, ka + 0.6 + i * 0.12, 0.4, lambda a, i=i: (carro if i % 2 else moto)(c, 960 + i * 175, 255, 130, TINTA, a, **({"fundo": E.PAPEL} if i % 2 else {})))
        E.frase(c, t, kb, [("100", "g", 150, COR)] + ps("rodas", "i", 120), XE, 520, passo=0.15)
        E.frase(c, t, lerp(kb, kc, 0.4), ps("quantos são os", "i", 96) + [("carros?", "g", 100)], XE, 700, passo=0.12)
        E.frase(c, t, kc, ps("sem escrever", "i", 84) + [("letra nenhuma", "g", 84, COR)], W / 2, 900, "center", 0.12)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t >= C["s02"]:
        ta, tb = C["s02.a"], C["s02.b"]
        E.foco(c, t, tb - 0.2, 0.7, lambda a: E.bola(c, 1490, 540, 250 * ease_back(prog(t, tb - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, ps("até o fim desta aula", "i", 90), XE, 330, passo=0.14)
        E.frase(c, t, lerp(ta, tb, 0.35), ps("problema de texto", "i", 96), XE, 490, passo=0.14)
        E.frase(c, t, lerp(ta, tb, 0.6), ps("vira", "i", 96) + [("sistema", "g", 120, COR)], XE, 650, passo=0.14)
        E.foco(c, t, tb + 0.2, 0.5, lambda a: (centro(c, "+ atalho", 1490, 525, 80, "g", E.SOBRE, a),
                                               centro(c, "de prova", 1490, 610, 80, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"] + 0.3, ps("você precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "2", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 240, 700, 120, "i", TINTA, a))
    x, w = 900, 860
    itens = (("s03.b", "montar uma equação:", "o que não sabe vira letra"), ("s03.c", "resolver um sistema", "por substituição"))
    for i, (k, l1, l2) in enumerate(itens):
        y = 220 + i * 260
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 196, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 62)], x + 44, y + 84)
        E.frase(c, t, C[k] + 0.3, [(l2, "g", 60, COR)], x + 44, y + 160)
    py = lerp(390, 650, ease_io(prog(t, C["s03.c"] - 0.35, 0.5)))
    E.cursor(c, x + w - 30, py, ep(t, C["s03.b"], 0.4))
    E.frase(c, t, lerp(C["s03.c"], C["s03.end"], 0.62), ps("faltou alguma?", "i", 62, COR) + ps("procure no canal", "i", 62), x, 820, "left", 0.12)


# ---------------- o problema do teatro ----------------
def b_teatro(c, t, C, b):
    ka, kb, kc, kd, ke = (C[f"s04.{k}"] for k in "abcde")
    E.frase(c, t, C["s04"] + 0.2, ps("um teatro", "i", 84) + [("(preços inventados)", "i", 56, TINTA2)], XE, 170, passo=0.12)
    E.foco(c, t, ka, 0.5, lambda a: ingresso(c, XE + 90, 330, 170, COR, a))
    E.frase(c, t, ka + 0.2, [("150", "g", 120, COR)] + ps("ingressos", "i", 100), XE + 220, 370, passo=0.14)
    E.frase(c, t, ka + 1.4, ps("inteiras e meias-entradas", "i", 64, TINTA2), XE + 220, 450, passo=0.08)
    E.frase(c, t, kb, ps("inteira", "i", 84) + [("R$ 40", "g", 100, COR)], XE, 610, passo=0.14)
    E.frase(c, t, kc, ps("meia", "i", 84) + [("R$ 20", "g", 100, COR)], XE, 760, passo=0.14)
    E.frase(c, t, kd, ps("total", "i", 84) + [("R$ 4.400", "g", 100, COR)], XE, 910, passo=0.14)
    E.foco(c, t, ke, 0.5, lambda a: E.caixa_pontilhada(c, 1040, 560, 800, 380, a))
    E.frase(c, t, ke, ps("quantas", "i", 84) + [("inteiras?", "g", 84, COR)], 1090, 700, passo=0.14)
    E.frase(c, t, ke + 0.8, ps("quantas", "i", 84) + [("meias?", "g", 84, COR)], 1090, 860, passo=0.14)


# ---------------- montar: o molde em três passos ----------------
def b_montar(c, t, C, b):
    a5, b5, c5, d5 = (C[f"s05.{k}"] for k in "abcd")
    a6, b6 = C["s06.a"], C["s06.b"]
    a7, b7, c7, d7 = (C[f"s07.{k}"] for k in "abcd")
    a8, b8, c8 = C["s08.a"], C["s08.b"], C["s08.c"]

    def passos():
        passo(c, t, a5, 1, "diga o que", "cada letra conta", 200)
        passo(c, t, a6, 2, "uma equação para", "as quantidades", 520)
        passo(c, t, a7, 3, "uma equação para", "o dinheiro", 820)
        xr = 1000
        E.linha(c, t, [("x", "g", 96, COR, b5), ("= número de inteiras", "i", 76, TINTA, b5 + 0.3)], xr, 190)
        E.linha(c, t, [("y", "g", 96, COR, c5), ("= número de meias", "i", 76, TINTA, c5 + 0.3)], xr, 300)
        E.foco(c, t, d5, 0.4, lambda a: E.pilula(c, "contam ingressos, não reais", xr + 330, 390, 44, estilo="b", a=a), sobe=8)
        E.frase(c, t, lerp(a6, b6, 0.55), ps("ingressos com ingressos", "i", 60, TINTA2), xr, 505, passo=0.08)
        fcen(c, t, b6, "x + y = 150", xr + 330, 625, 110)
        xs = E.linha(c, t, [("40x", "g", 88, TINTA, b7), ("+", "g", 88, TINTA, c7 - 0.2), ("20y", "g", 88, TINTA, c7),
                            ("= 4.400", "g", 88, TINTA, d7 + 1.5)], xr, 860)
        E.foco(c, t, b7 + 0.2, 0.4, lambda a: centro(c, "inteiras", xs[0] + E.larg("40x", "g", 88) / 2, 935, 44, "i", TINTA2, a))
        E.foco(c, t, c7 + 0.2, 0.4, lambda a: centro(c, "meias", xs[2] + E.larg("20y", "g", 88) / 2, 935, 44, "i", TINTA2, a))
        E.foco(c, t, lerp(a7, b7, 0.45), 0.4, lambda a: E.pilula(c, "cada inteira: R$ 40 · cada meia: R$ 20", xr + 400, 740, 40, estilo="b", fundo=TINTA, a=a), sobe=8)
    E.saida(c, t, a8 - 0.1, passos)
    if t < a8 - 0.1:
        return
    sx, sy, sz = 300, 400, 110
    E.sistema(c, t, a8, ["x + y = 150", "40x + 20y = 4.400"], sx, sy, sz)
    E.frase(c, t, a8 + 0.3, ps("esse é o", "i", 80) + [("sistema", "g", 80, COR)], XE, 170, passo=0.12)
    E.foco(c, t, b8, 0.4, lambda a: E.pilula(c, "conta as coisas", 1560, sy - 40, 52, estilo="b", a=a), sobe=8)
    E.foco(c, t, c8, 0.4, lambda a: E.pilula(c, "soma os valores", 1560, sy + sz * 1.45 - 40, 52, estilo="b", fundo=TINTA, a=a), sobe=8)
    tm = lerp(c8, C["s08.end"], 0.25)
    E.frase(c, t, tm, ps("total de coisas", "i", 70) + [("+", "g", 70, COR)] + ps("total em dinheiro", "i", 70) + [("= este molde", "g", 70, COR)], W / 2, 900, "center", 0.12)


# ---------------- resolver por substituição ----------------
def b_resolver(c, t, C, b):
    a9, b9, c9, d9, e9 = (C[f"s09.{k}"] for k in "abcde")

    def conta():
        E.sistema(c, t, C["s09"], ["x + y = 150", "40x + 20y = 4.400"], 200, 160, 64)
        E.frase(c, t, C["s09"] + 0.2, ps("por", "i", 64) + [("substituição", "g", 64, COR)], 1180, 180, passo=0.12)
        fcen(c, t, a9, "y = 150 − x", 1420, 270, 84, COR)
        tm = lerp(a9, b9, 0.45)
        fcen(c, t, tm, "40x + 20 · (150 − x) = 4.400", W / 2, 450, 92)
        E.foco(c, t, tm + 0.8, 0.4, lambda a: centro(c, "o 20 multiplica cada termo do parêntese", W / 2, 530, 46, "i", TINTA2, a))
        fcen(c, t, b9, "40x + 3.000 − 20x = 4.400", W / 2, 650, 92)
        E.foco(c, t, lerp(b9, c9, 0.5), 0.4, lambda a: E.pilula(c, "− 3.000 nos dois lados", W / 2, 735, 44, estilo="b", a=a), sobe=8)
        fcen(c, t, c9, "20x = 1.400", 700, 860, 100)
        fcen(c, t, d9, "x = 70", 700, 1000, 110, COR)
        fcen(c, t, lerp(d9, e9, 0.45), "y = 150 − 70", 1380, 860, 92)
        fcen(c, t, e9, "y = 80", 1380, 1000, 110, COR)
    E.saida(c, t, C["s10"] - 0.1, conta)
    if t < C["s10"]:
        return
    a10, b10, c10, d10 = (C[f"s10.{k}"] for k in "abcd")
    E.frase(c, t, C["s10"], [("conferindo", "i", 84, COR)], XE, 170)
    E.foco(c, t, C["s10"] + 0.3, 0.4, lambda a: (E.pilula(c, "70 inteiras", 1180, 145, 52, estilo="g", a=a), E.pilula(c, "80 meias", 1560, 145, 52, estilo="g", a=a)))
    fcen(c, t, a10, "70 + 80 = 150", 560, 380, 96)
    E.foco(c, t, a10 + 0.4, 0.4, lambda a: centro(c, "ingressos", 560, 460, 52, "i", TINTA2, a))
    fcen(c, t, b10, "70 × 40 = 2.800", 1360, 380, 96)
    fcen(c, t, c10, "80 × 20 = 1.600", 1360, 560, 96)
    fcen(c, t, d10, "2.800 + 1.600 = 4.400", W / 2, 790, 110, COR)
    selo_em(c, t, d10 + 1.0, 760, 930, 56)
    E.frase(c, t, d10 + 1.1, [("bateu", "g", 72, CERTO)] + ps("nas duas", "i", 72), 840, 955, "left", 0.12)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    a11, b11 = C["s11.a"], C["s11.b"]
    a12, b12, c12 = C["s12.a"], C["s12.b"], C["s12.c"]
    E.frase(c, t, C["s11"], [("cuidado", "g", 110, ERRADO)] + ps("com a montagem", "i", 90), W / 2, 200, "center", 0.14)
    E.frase(c, t, a11, ps("misturar", "i", 84) + [("coisas diferentes", "g", 84, ERRADO)], W / 2, 340, "center", 0.12)
    s, size, cx, y = "x + y = 4.400", 150, W / 2, 580
    w = E.formula(c, s, 0, 0, size, a=0)
    x0 = cx - w / 2
    fcen(c, t, b11, s, cx, y, size, ERRADO)
    wl = E.formula(c, "x + y", 0, 0, size, a=0)
    wr = E.formula(c, "4.400", 0, 0, size, a=0)
    E.chave(c, x0, x0 + wl, y + 40, TINTA2, ep(t, a12, 0.5))
    E.foco(c, t, a12, 0.4, lambda a: centro(c, "ingressos", x0 + wl / 2, y + 140, 64, "g", TINTA, a))
    E.chave(c, x0 + w - wr, x0 + w, y + 40, TINTA2, ep(t, b12, 0.5))
    E.foco(c, t, b12, 0.4, lambda a: centro(c, "reais", x0 + w - wr / 2, y + 140, 64, "g", TINTA, a))
    if t >= lerp(b12, c12, 0.3):
        E.saida(c, t, c12 - 0.1, lambda: E.frase(c, t, lerp(b12, c12, 0.3), [("4.400 ingressos?", "g", 80, ERRADO)] + ps("o teatro vendeu 150", "i", 76), W / 2, 880, "center", 0.12))
    E.frase(c, t, c12, ps("cada equação fala de", "i", 84) + [("uma coisa só", "g", 84, CERTO)], W / 2, 880, "center", 0.12)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    a13, b13, c13 = C["s13.a"], C["s13.b"], C["s13.c"]
    a14, b14, c14, d14, e14 = (C[f"s14.{k}"] for k in "abcde")
    a15, b15, c15, d15 = (C[f"s15.{k}"] for k in "abcd")
    a16, b16, c16, d16 = (C[f"s16.{k}"] for k in "abcd")
    x0, y0 = 230, 440
    # a primeira troca na fala, as outras 19 em sequência depois de "vinte trocas"
    trocas = [a14 + 0.3] + [c14 + 0.4 + i * 0.12 for i in range(19)]

    def tela():
        def titulo():
            E.frase(c, t, C["s13"] + 0.2, [("agora,", "i", 100, CLARO), ("o atalho", "g", 110, BR)], W / 2, 420, "center", 0.14)
            E.frase(c, t, C["s13"] + 1.4, ps("de volta aos veículos", "i", 80, CLARO), W / 2, 560, "center", 0.1)
        E.saida(c, t, a13 - 0.2, titulo)
        E.frase(c, t, a13, ps("suponha:", "i", 76, CLARO) + [("todos são motos", "g", 76, BR)], XE, 170, passo=0.12)
        frota(c, t, a13 + 0.3, trocas, x0, y0)
        xr = 1560
        fcen(c, t, b13, "30 × 2 = 60", xr, 300, 76, BR)
        E.foco(c, t, b13 + 0.3, 0.4, lambda a: centro(c, "rodas", xr, 362, 50, "i", CLARO, a))
        fcen(c, t, c13, "100 − 60 = 40", xr, 470, 76, BR)
        E.foco(c, t, c13 + 0.3, 0.4, lambda a: centro(c, "faltam 40 rodas", xr, 532, 50, "i", CLARO, a))
        E.foco(c, t, a14 + 0.2, 0.4, lambda a: E.caixa_pontilhada(c, x0 - 56, y0 - 60, 112, 110, a, CLARO))
        E.frase(c, t, a14, ps("1 troca:", "i", 66, CLARO) + [("ainda 30 veículos", "g", 62, BR)], XE, 830, passo=0.1)
        E.foco(c, t, b14, 0.4, lambda a: E.pilula(c, "+2 rodas", x0, y0 - 110, 44, estilo="g", a=a), sobe=8)
        E.foco(c, t, lerp(b14, c14, 0.4), 0.4, lambda a: E.escreve(c, "carro 4, moto 2: 4 − 2 = 2", XE, 940, 54, "b", CLARO, a))
        fcen(c, t, c14, "40 ÷ 2 = 20", xr, 640, 76, BR)
        E.foco(c, t, c14 + 0.3, 0.4, lambda a: centro(c, "trocas", xr, 702, 50, "i", CLARO, a))
        E.foco(c, t, d14, 0.5, lambda a: (E.bola(c, 1440, 860, 86, a=a), centro(c, "20", 1440, 885, 70, "g", BR, a),
                                          centro(c, "carros", 1440, 1000, 46, "i", CLARO, a)))
        E.foco(c, t, e14, 0.5, lambda a: (E.bola(c, 1690, 860, 86, CLARO, a), centro(c, "10", 1690, 885, 70, "g", "#07070F", a),
                                          centro(c, "motos", 1690, 1000, 46, "i", CLARO, a)))
    E.saida(c, t, C["s15"] - 0.1, tela)

    def confere():
        frota(c, t, -10, trocas, x0 + 220, y0 - 140, a=1.0)
        E.frase(c, t, C["s15"], [("conferindo", "i", 76, CLARO)], XE, 150)
        fcen(c, t, a15, "20 × 4 = 80", 560, 720, 96, BR)
        fcen(c, t, b15, "10 × 2 = 20", 1360, 720, 96, BR)
        fcen(c, t, c15, "80 + 20 = 100", 960, 880, 120, CLARO)
        E.frase(c, t, d15, ps("a resposta do sistema,", "i", 70, CLARO) + [("feita de cabeça", "g", 70, BR)], W / 2, 1010, "center", 0.1)
    if C["s15"] - 0.1 <= t:
        E.saida(c, t, C["s16"] - 0.1, confere)
    if t < C["s16"]:
        return
    E.frase(c, t, C["s16"], ps("funciona porque", "i", 76, CLARO), XE, 180)
    E.frase(c, t, a16, ps("o total de veículos", "i", 72, BR) + [("não muda", "g", 72, BR)], XE + 60, 290, passo=0.1)
    E.frase(c, t, b16, ps("cada troca:", "i", 72, BR) + [("sempre +2 rodas", "g", 72, BR)], XE + 60, 390, passo=0.1)
    E.frase(c, t, lerp(b16, c16, 0.6), ps("não compensa quando", "i", 76, CLARO), XE, 560)
    E.frase(c, t, c16, ps("falta o", "i", 72, BR) + [("total de coisas", "g", 72, BR)], XE + 60, 670, passo=0.1)
    E.frase(c, t, d16, ps("há", "i", 72, BR) + [("mais de dois tipos", "g", 72, BR)], XE + 60, 770, passo=0.1)
    E.frase(c, t, lerp(d16, C["s16.end"], 0.5), ps("aí,", "i", 84, CLARO) + [("monte o sistema", "g", 84, CLARO)], W / 2, 930, "center", 0.12)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    ka, kb, kc = C["s17.a"], C["s17.b"], C["s17.c"]
    E.frase(c, t, C["s17"], ps("hora de testar", "i", 72, COR), XE, 200)
    E.frase(c, t, ka, [("25", "g", 120, COR)] + ps("cédulas", "i", 100), XE, 380, passo=0.14)
    E.foco(c, t, ka + 1.0, 0.5, lambda a: cedula(c, 300, 520, 220, "10", TINTA2, a, -4))
    E.foco(c, t, ka + 1.4, 0.5, lambda a: cedula(c, 580, 520, 220, "20", E.COR, a, 3))
    E.frase(c, t, kb, ps("total", "i", 84) + [("R$ 380", "g", 100, COR)], XE, 760, passo=0.14)
    E.frase(c, t, kc, ps("monte o sistema:", "i", 72) + [("quantas de R$ 20?", "g", 72, COR)], XE, 920, passo=0.12)
    E.relogio(c, t, C["s18.a"])


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    a19, b19, c19, d19 = (C[f"s19.{k}"] for k in "abcd")

    def monta():
        E.linha(c, t, [("x", "g", 96, COR, a19), ("= cédulas de R$ 10", "i", 76, TINTA, a19 + 0.3)], XE, 220)
        E.linha(c, t, [("y", "g", 96, COR, b19), ("= cédulas de R$ 20", "i", 76, TINTA, b19 + 0.3)], XE, 340)
        E.sistema(c, t, c19, ["x + y = 25", "10x + 20y = 380"], XE + 80, 560, 110, tl=(c19, d19))
        E.foco(c, t, c19 + 0.3, 0.4, lambda a: E.pilula(c, "quantidades", 1350, 520, 52, estilo="b", a=a), sobe=8)
        E.foco(c, t, d19 + 0.3, 0.4, lambda a: E.pilula(c, "dinheiro", 1350, 520 + 160, 52, estilo="b", fundo=TINTA, a=a), sobe=8)
    E.saida(c, t, C["s20"] - 0.1, monta)
    if t < C["s20"] - 0.1:
        return
    a20, b20, c20, d20, e20, f20 = (C[f"s20.{k}"] for k in "abcdef")

    def atalho():
        E.frase(c, t, C["s20"], ps("pelo atalho,", "i", 76) + [("todas de R$ 10", "g", 76, COR)], XE, 170, passo=0.12)
        for i in range(5):
            E.foco(c, t, a20 + i * 0.1, 0.4, lambda a, i=i: cedula(c, 1250 + i * 135, 150, 120, "10", TINTA2, a, -6 + i * 3))
        fcen(c, t, b20, "25 × 10 = 250", 560, 380, 96)
        fcen(c, t, c20, "380 − 250 = 130", 1360, 380, 96)
        E.foco(c, t, c20 + 0.3, 0.4, lambda a: centro(c, "faltam R$ 130", 1360, 460, 52, "i", TINTA2, a))
        E.foco(c, t, d20, 0.4, lambda a: E.pilula(c, "trocar 10 por 20: +R$ 10", W / 2, 590, 52, estilo="b", a=a), sobe=8)
        fcen(c, t, e20, "130 ÷ 10 = 13", W / 2, 780, 110)
        E.foco(c, t, f20, 0.5, lambda a: (E.bola(c, 740, 930, 80, CERTO, a), centro(c, "13", 740, 955, 70, "g", BR, a)))
        E.frase(c, t, f20 + 0.2, ps("cédulas de", "i", 80) + [("R$ 20", "g", 84, CERTO)], 850, 960, passo=0.12)
    E.saida(c, t, C["s21"] - 0.1, atalho)
    if t < C["s21"]:
        return
    a21, b21, c21, d21, e21 = (C[f"s21.{k}"] for k in "abcde")
    E.foco(c, t, C["s21"], 0.4, lambda a: E.pilula(c, "13 de R$ 20", 330, 160, 52, estilo="g", a=a), sobe=8)
    fcen(c, t, C["s21"] + 0.5, "25 − 13 = 12", 560, 360, 100)
    E.foco(c, t, a21, 0.4, lambda a: centro(c, "12 cédulas de R$ 10", 560, 450, 56, "g", COR, a))
    E.frase(c, t, b21 - 0.6, [("conferindo", "i", 72, COR)], 1100, 170)
    fcen(c, t, b21, "13 + 12 = 25", 1400, 360, 96)
    fcen(c, t, c21, "13 × 20 = 260", 560, 640, 96)
    fcen(c, t, d21, "12 × 10 = 120", 1360, 640, 96)
    fcen(c, t, e21, "260 + 120 = 380", W / 2, 840, 120, COR)
    selo_em(c, t, e21 + 1.0, 860, 970, 56)
    E.frase(c, t, e21 + 1.1, [("bateu", "g", 72, CERTO)], 940, 995)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s22"], [("resumindo", "i", 92, COR)], W / 2, 210, "center")
        for i, (k, s) in enumerate((("s22.a", "o que cada letra conta"), ("s22.b", "equação das quantidades"), ("s22.c", "equação dos valores"))):
            y = 390 + i * 190
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 330, y - 30, 56, a=a),
                                                         E.escreve(c, str(i + 1), 330 - E.larg(str(i + 1), "g", 64) / 2, y - 7, 64, "g", "#FFFFFF", a)))
            E.frase(c, t, C[k] + 0.1, [(s, "g", 96)], 430, y)
    E.saida(c, t, C["s23"] - 0.1, resumo)
    if t < C["s23"]:
        return
    E.frase(c, t, C["s23"] + 0.2, ps("próxima aula", "i", 84), XE, 330)
    E.frase(c, t, C["s23.a"], [("Praticando:", "g", 130, COR)], XE, 490)
    E.frase(c, t, C["s23.a"] + 0.4, [("sistemas", "g", 130, COR)], XE, 640)
    E.frase(c, t, C["s23.a"] + 1.5, ps("preços e quantidades, pelo caminho mais curto", "i", 56, TINTA2), XE, 750, "left", 0.06)
    E.foco(c, t, C["s23.b"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1500, 400, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s23.b"] + 0.3, 0.8))
    E.cursor(c, lerp(1800, 1630, p), lerp(720, 425, p), ep(t, C["s23.b"] + 0.2, 0.4))
    E.frase(c, t, C["s23.c"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 920, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, teatro=b_teatro, montar=b_montar, resolver=b_resolver,
              erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
