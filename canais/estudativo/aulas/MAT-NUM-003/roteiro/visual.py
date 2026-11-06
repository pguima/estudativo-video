"""Visual — Estudativo · MAT-NUM-003: somar de cabeça e com a conta armada.
Identidade em _ferramentas/editorial.py. O completar dez acontece num quadro de dez moedas (peça local `completar`), e a conta armada
passa por E.armada, que refaz a conta. A conta errada de 724 é desenhada à mão, porque E.armada não aceita resultado errado."""
import math

import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco
import motor as M
import skia

E.usar("Matemática", "Números e Contas")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-NUM-003_somar_cabeca_conta_armada.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("dez", "armar", "atalho", "questao", "fim"))
BR = "#FFFFFF"


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


def entre(a, b, f):
    """instante proporcional entre dois cues: sobrevive à troca do tempo provisório pela voz real"""
    return a + (b - a) * f


# ---------------- peças locais ----------------
def nota(c, cx, cy, w, s, a=1.0, cor=None, giro=0.0):
    """nota de dinheiro didática: retângulo com o valor, sem imitar cédula real"""
    if a <= 0:
        return
    cor = cor or E.COR
    h = w * 0.5
    c.save(); c.translate(cx, cy); c.rotate(giro)
    sombra = skia.Paint(AntiAlias=True, Color=M.hexc("#000000", 0.22 * a))
    sombra.setMaskFilter(skia.MaskFilter.MakeBlur(skia.kNormal_BlurStyle, max(3, w * 0.03)))
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(-w / 2 + 3, -h / 2 + 7, w, h), w * 0.04, w * 0.04), sombra)
    M.rrect(c, -w / 2, -h / 2, w, h, w * 0.04, cor, a)
    m = w * 0.045
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(-w / 2 + m, -h / 2 + m, w - 2 * m, h - 2 * m), w * 0.025, w * 0.025), M.paint(E.SOBRE, 0.45 * a, stroke=max(2, w * 0.008)))
    size = h * 0.5
    E.centro(c, "R$ " + s, 0, size * 0.36, size, "g", E.SOBRE, a)
    c.restore()


def conta(c, t, partes, x, y, align="center"):
    """E.linha com tudo no mesmo tamanho: partes = [(texto, cor, t0), ...], size vem no 4º campo opcional"""
    return E.linha(c, t, [(p[0], "g", p[3] if len(p) > 3 else 96, p[1], p[2]) for p in partes], x, y, align)


def completar(c, t, n1, n2, ta, tb, tv, x0=250, y0=300, xp=1130):
    """o quadro de dez moedas: n1 já dentro, n2 na pilha ao lado. tb = as casas vazias acendem, tv = as moedas que faltam voam para o quadro.
    A primeira linha tem cinco casas: o olho vê o dez sem contar."""
    passo_, r = 132, 58
    falta = 10 - n1
    casa_ = lambda i: (x0 + (i % 5) * passo_, y0 + (i // 5) * passo_)
    pil = lambda i: (xp + (i % 4) * passo_ * 0.92, y0 + (i // 4) * passo_)
    # moldura
    a = ep(t, ta, 0.45)
    if a > 0:
        M.rrect(c, x0 - 76, y0 - 76, 5 * passo_ + 20, 2 * passo_ + 20, 22, E.VAZIO, a)
        for i in range(10):
            x, y = casa_(i)
            acesa = i >= n1 and t >= tb
            c.drawCircle(x, y, r, M.paint(E.COR if acesa else FIO, a * ep(t, tb, 0.3) if acesa else a, stroke=4 if acesa else 3))
    for i in range(n1):
        k = ease_back(prog(t, ta + 0.05 * i, 0.4))
        if k > 0:
            x, y = casa_(i)
            E.moeda(c, x, y, r * k, "1", M.clamp(k * 2))
    for i in range(n2):
        ti = ta + 0.3 + 0.05 * i
        k = ease_back(prog(t, ti, 0.4))
        if k <= 0:
            continue
        x, y = pil(i)
        q, j = 0, i - (n2 - falta)
        if j >= 0:  # as últimas da pilha vão completar o dez
            q = ease_io(prog(t, tv + j * 0.22, 0.65))
            xd, yd = casa_(n1 + j)
            x, y = lerp(x, xd, q), lerp(y, yd, q) - math.sin(q * math.pi) * 70
        E.moeda(c, x, y, r * k, "1", M.clamp(k * 2), cor=E.COR if q >= 1 else TINTA)


def faixa(c, x, y, w, h, a):
    M.rrect(c, x, y, w, h, 18, E.COR, 0.08 * a)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def oito():
        E.foco(c, t, C["s01.a"], 0.5, lambda a: E.centro(c, "8 + 7", W / 2, 560, 340, "g", TINTA, a))
        E.foco(c, t, C["s01.b"], 0.45, lambda a: E.pilula(c, "sem problema", W / 2, 720, 72, a=a, cor=E.SOBRE))
        E.frase(c, t, entre(C["s01.b"], C["s02"], 0.3), [("existe", "i", 96), ("um", "i", 96), ("caminho", "i", 96), ("mais", "g", 92, COR), ("rápido", "g", 92, COR)], W / 2, 900, "center", passo=0.12)
    E.saida(c, t, C["s02"] - 0.1, oito)

    def erro():
        E.foco(c, t, C["s02.a"], 0.5, lambda a: E.centro(c, "478 + 356", W / 2, 400, 210, "g", TINTA, a))
        E.foco(c, t, C["s02.b"], 0.5, lambda a: E.centro(c, "= 724", W / 2, 640, 210, "g", ERRADO, a))
        E.frase(c, t, C["s02.c"], [("sumiram", "i", 100), ("R$ 110", "g", 100, ERRADO), ("no", "i", 100), ("caminho", "i", 100)], W / 2, 880, "center", passo=0.12)
    if C["s02"] <= t:
        E.saida(c, t, C["s03"] - 0.1, erro)

    if t >= C["s03"]:
        a_, b_ = C["s03.a"], C["s03.b"]
        E.foco(c, t, b_ - 0.2, 0.7, lambda a: E.bola(c, 1450, 520, 300 * ease_back(prog(t, b_ - 0.2, 0.7))), blur=0)
        E.frase(c, t, a_, [("até", "i", 92), ("o", "i", 92), ("fim", "i", 92), ("desta", "i", 92), ("aula", "i", 92)], XE, 340)
        E.frase(c, t, entre(a_, b_, 0.3), [("você", "i", 92), ("soma", "g", 116, COR)], XE, 500)
        E.frase(c, t, entre(a_, b_, 0.45), [("de", "i", 100), ("cabeça", "g", 108)], XE, 620)
        E.frase(c, t, entre(a_, b_, 0.65), [("e", "i", 100), ("com", "i", 100), ("a", "i", 100), ("conta", "g", 92), ("armada", "g", 92)], XE, 740, passo=0.1)
        E.foco(c, t, b_ + 0.2, 0.5, lambda a: (E.escreve(c, "+ atalho", 1270, 505, 88, "g", E.SOBRE, a),
                                               E.escreve(c, "de prova", 1300, 595, 88, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    a_, b_, c_, fim = C["s04.a"], C["s04.b"], C["s04.c"], C["s04.end"]
    E.frase(c, t, a_, [("você", "i", 88), ("só", "i", 88), ("precisa", "i", 88), ("de", "i", 88), ("uma", "g", 84, COR), ("troca", "g", 84, COR)], W / 2, 170, "center", passo=0.1)
    for i in range(10):
        k = ease_back(prog(t, entre(b_, c_, 0.05 + i * 0.05), 0.4))
        if k > 0:
            E.moeda(c, 400 + (i % 5) * 112, 300 + (i // 5) * 112, 50 * k, "1", M.clamp(k * 2))
    E.sinal(c, t, entre(b_, c_, 0.6), "=", 1090, 350, 110)
    E.foco(c, t, entre(b_, c_, 0.68), 0.5, lambda a: nota(c, 1400, 355, 380, "10", a))
    for i in range(10):
        E.foco(c, t, entre(c_, fim, 0.03 + i * 0.035), 0.35, lambda a, i=i: nota(c, 420 + i * 44, 640 + (i % 2) * 10, 280, "10", a), sobe=-12)
    E.sinal(c, t, entre(c_, fim, 0.42), "=", 1090, 650, 110)
    E.foco(c, t, entre(c_, fim, 0.48), 0.5, lambda a: nota(c, 1400, 655, 380, "100", a, TINTA))
    E.frase(c, t, entre(c_, fim, 0.72), [("se", "i", 66, TINTA2), ("faltar,", "i", 66, TINTA2), ("procure", "i", 66, TINTA2), ("a", "i", 66, TINTA2), ("aula", "i", 66, TINTA2), ("no", "i", 66, TINTA2), ("canal", "i", 66, TINTA2)], W / 2, 900, "center", passo=0.08)


# ---------------- completar dez ----------------
def b_dez(c, t, C, b):
    def juntar():
        a_, b_, c_ = C["s05.a"], C["s05.b"], C["s05.c"]
        E.frase(c, t, a_, [("somar", "i", 150), ("é", "i", 150), ("juntar", "g", 150, COR)], W / 2, 320, "center", passo=0.14)
        E.linha(c, t, [("parcela", "g", 104, TINTA, b_), ("+", "g", 104, TINTA, b_ + 0.3), ("parcela", "g", 104, TINTA, b_ + 0.5), ("=", "g", 104, TINTA, c_ - 0.2), ("total", "g", 104, COR, c_)], W / 2, 610, "center")
        E.frase(c, t, entre(b_, c_, 0.45), [("como", "i", 80), ("as", "i", 80), ("parcelas", "i", 80), ("de", "i", 80), ("uma", "i", 80), ("compra", "i", 80)], W / 2, 790, "center", passo=0.1)
    E.saida(c, t, C["s06"] - 0.1, juntar)

    def facil():
        a_, b_ = C["s06.a"], C["s06.b"]
        E.frase(c, t, C["s06"] + 0.1, [("o", "i", 96), ("mais", "i", 96), ("fácil", "i", 96), ("de", "i", 96), ("somar", "i", 96)], W / 2, 210, "center", passo=0.1)
        k = ease_back(prog(t, a_, 0.6))
        if k > 0:
            E.bola(c, W / 2, 470, 190 * k, a=M.clamp(k * 2))
            E.foco(c, t, a_ + 0.2, 0.4, lambda q: E.centro(c, "10", W / 2, 540, 200, "g", E.SOBRE, q))
        E.frase(c, t, entre(a_, b_, 0.3), [("10", "g", 104), ("+", "g", 104), ("5:", "g", 104), ("responde", "i", 104), ("na", "i", 104), ("hora", "i", 104)], W / 2, 790, "center", passo=0.1)
        E.frase(c, t, b_, [("chegar", "g", 96, COR), ("no", "g", 96, COR), ("dez", "g", 96, COR), ("primeiro", "i", 104)], W / 2, 930, "center", passo=0.12)
    if C["s06"] <= t:
        E.saida(c, t, C["s07"] - 0.1, facil)

    def oito_sete():
        a_, b_, c_, d_, e_, f_ = C["s07.a"], C["s07.b"], C["s07.c"], C["s07.d"], C["s07.e"], C["s07.f"]
        completar(c, t, 8, 7, a_ + 0.2, b_, c_ + 0.3)
        E.saida(c, t, C["s08"] - 0.1, lambda: (E.foco(c, t, a_, 0.45, lambda q: E.centro(c, "8 + 7", 514, 165, 130, "g", TINTA, q)),
                                               E.frase(c, t, b_, [("faltam", "i", 88), ("dois", "g", 84, COR)], 1320, 170, "center", passo=0.12)))
        E.saida(c, t, d_ - 0.1, lambda: E.foco(c, t, c_, 0.45, lambda q: E.pilula(c, "tire de dentro do 7", 1400, 640, 54, a=q, cor=E.SOBRE)))
        E.foco(c, t, d_, 0.45, lambda q: E.centro(c, "7 = 2 + 5", 1400, 720, 96, "g", TINTA, q))
        E.foco(c, t, e_, 0.45, lambda q: E.centro(c, "8 + 2 = 10", 560, 720, 96, "g", COR, q))
        E.foco(c, t, f_, 0.45, lambda q: E.centro(c, "10 + 5 = 15", W / 2, 890, 130, "g", COR, q))
        E.frase(c, t, C["s08.a"], [("você", "i", 84), ("só", "i", 84), ("passou", "i", 84), ("duas", "g", 80, COR), ("moedas", "g", 80, COR)], W / 2, 150, "center", passo=0.1)
        E.frase(c, t, C["s08.b"], [("o", "i", 84), ("total", "g", 80, CERTO), ("não", "g", 80, CERTO), ("mudou", "g", 80, CERTO)], W / 2, 1000, "center", passo=0.1)
    if C["s07"] <= t:
        E.saida(c, t, C["s08.c"] - 0.1, oito_sete)
    if t < C["s08.c"]:
        return

    c_, d_, e_, f_ = C["s08.c"], C["s08.d"], C["s08.e"], C["s08.f"]
    E.foco(c, t, c_, 0.45, lambda q: E.centro(c, "6 + 7", 514, 165, 130, "g", TINTA, q))
    completar(c, t, 6, 7, c_ + 0.1, d_, e_ + 0.2)
    E.frase(c, t, d_, [("faltam", "i", 88), ("quatro", "g", 84, COR)], 1320, 170, "center", passo=0.12)
    E.foco(c, t, e_, 0.45, lambda q: E.centro(c, "7 = 4 + 3", 1400, 720, 96, "g", TINTA, q))
    E.foco(c, t, f_, 0.45, lambda q: E.centro(c, "10 + 3 = 13", W / 2, 890, 130, "g", COR, q))


# ---------------- conta armada ----------------
XV, Y0, ST = 750, 370, 150
XP = 1360  # centro do painel da direita


def colunas(s="478"):
    return E._centros(s, XV, ST)


def banda(c, t, x, t0, t1, nome=""):
    """a coluna da vez, com o nome da casa em cima: três nomes fixos lado a lado não cabem na largura da coluna"""
    q = ep(t, t0, 0.3) * (1 - ep(t, t1 - 0.25, 0.25))
    if q > 0:
        faixa(c, x - 74, 90, 148, 690, q)
        E.centro(c, nome, x, 140, 46, "i", COR, q)


def b_armar(c, t, C, b):
    xs = colunas()

    def montagem():
        banda(c, t, xs[2], C["s09.b"], C["s09.c"], "unidade"); banda(c, t, xs[1], C["s09.c"], C["s09.d"], "dezena"); banda(c, t, xs[0], C["s09.d"], C["s10"], "centena")
        banda(c, t, xs[2], C["s10.b"], C["s12"], "unidade"); banda(c, t, xs[1], C["s12"], C["s13"], "dezena"); banda(c, t, xs[0], C["s13"], C["s13.c"], "centena")
        a_ = C["s09.a"]
        E.armada(c, t, ["478", "356"], "+", "834", (a_ + 0.2, entre(a_, C["s09.b"], 0.8)), (C["s11.c"], C["s12.d"], C["s13.b"]), XV, Y0, ST,
                 vai=[(1, "1", C["s11.d"]), (2, "1", C["s12.e"])])

        # s09: o título; s10: de que lado se começa e a primeira conta
        def titulo():
            E.frase(c, t, a_, [("conta", "g", 110, COR), ("armada", "g", 110, COR)], XP, 300, "center")
            E.frase(c, t, C["s09.b"], [("casa", "i", 88), ("embaixo", "i", 88), ("de", "i", 88), ("casa", "i", 88)], XP, 440, "center", passo=0.12)
            E.frase(c, t, entre(C["s09.d"], C["s09.end"], 0.3), [("moeda", "g", 72), ("com", "i", 80), ("moeda,", "g", 72)], XP, 620, "center", passo=0.12)
            E.frase(c, t, entre(C["s09.d"], C["s09.end"], 0.6), [("nota", "g", 72), ("com", "i", 80), ("nota", "g", 72)], XP, 720, "center", passo=0.12)
        E.saida(c, t, C["s10"] - 0.1, titulo)

        def direita():
            E.frase(c, t, C["s10.a"], [("da", "i", 80), ("direita", "g", 76, COR), ("para", "i", 80), ("a", "i", 80), ("esquerda", "g", 76, COR)], XP, 240, "center", passo=0.1)
            p = ep(t, C["s10.a"] + 0.3, 0.6)
            if p > 0:
                M.arrow(c, 1660, 300, 1060, 300, E.COR, p, 6, 22, p)
            conta(c, t, [("8 + 6", TINTA, C["s10.b"], 130), ("=", TINTA, C["s10.c"] - 0.2, 130), ("14", COR, C["s10.c"], 130)], XP, 540)
        if C["s10"] <= t:
            E.saida(c, t, C["s11"] - 0.1, direita)

        def catorze():
            a, b_, c_, d_ = C["s11.a"], C["s11.b"], C["s11.c"], C["s11.d"]
            E.frase(c, t, a, [("nenhuma", "i", 64), ("casa", "i", 64), ("guarda", "i", 64), ("mais", "i", 64), ("que", "i", 64), ("nove", "g", 60, COR)], XP - 20, 170, "center", passo=0.08)
            cx, cy = 1190, 590
            une = ease_io(prog(t, b_, 0.6))
            for i in range(14):
                x, y = 1030 + (i % 7) * 104, 300 + (i // 7) * 104
                k = ease_back(prog(t, C["s11"] + 0.03 * i, 0.4))
                if i < 10:
                    if une < 1 and k > 0:
                        E.moeda(c, lerp(x, cx, une), lerp(y, cy, une), 46 * k, "1", M.clamp(k * 2) * (1 - une))
                elif k > 0:
                    E.moeda(c, x, y, 46 * k, "1", M.clamp(k * 2) * (1 - ep(t, c_, 0.5)))
                    if t >= c_:  # as quatro que sobram descem para perto do quatro
                        pass
            sobe = ease_io(prog(t, d_, 0.7))
            if t >= b_ + 0.2:
                nota(c, lerp(cx, xs[1], sobe), lerp(cy, 210, sobe) - math.sin(sobe * math.pi) * 60, lerp(280, 110, sobe), "10", ep(t, b_ + 0.2, 0.3) * (1 - ep(t, d_ + 0.5, 0.25)))
            E.foco(c, t, c_, 0.45, lambda q: (E.moeda(c, 1420, cy - 44, 46, "1", q), E.moeda(c, 1524, cy - 44, 46, "1", q), E.moeda(c, 1420, cy + 60, 46, "1", q), E.moeda(c, 1524, cy + 60, 46, "1", q)))
            E.foco(c, t, c_ + 0.1, 0.4, lambda q: E.centro(c, "sobram 4", 1470, 760, 64, "i", TINTA2, q))
            E.frase(c, t, d_, [("é", "i", 96), ("o", "i", 96), ("famoso", "i", 96), ("vai", "g", 96, COR), ("um", "g", 96, COR)], XP, 910, "center", passo=0.12)
        if C["s11"] <= t:
            E.saida(c, t, C["s12"] - 0.1, catorze)

        def dezenas():
            a, b_, c_, d_, e_ = C["s12.a"], C["s12.b"], C["s12.c"], C["s12.d"], C["s12.e"]
            conta(c, t, [("7 + 5", TINTA, a, 110), ("=", TINTA, a + 0.3, 110), ("12", TINTA, a + 0.5, 110)], XP, 270)
            conta(c, t, [("+ 1", COR, b_, 110), ("=", TINTA, b_ + 0.3, 110), ("13", COR, b_ + 0.5, 110)], XP, 420)
            E.frase(c, t, entre(b_, c_, 0.4), [("treze", "g", 72), ("notas", "i", 80), ("de", "i", 80), ("dez", "i", 80)], XP, 560, "center", passo=0.1)
            E.foco(c, t, c_, 0.45, lambda q: nota(c, XP, 690, 260, "100", q, TINTA))
            E.frase(c, t, d_, [("fica", "i", 88), ("o", "i", 88), ("três", "g", 84)], 1000, 900, passo=0.1)
            E.frase(c, t, e_, [("vai", "g", 84, COR), ("um", "g", 84, COR)], 1400, 900, passo=0.1)
        if C["s12"] <= t:
            E.saida(c, t, C["s13"] - 0.1, dezenas)

        def centenas():
            a, b_, c_ = C["s13.a"], C["s13.b"], C["s13.c"]
            conta(c, t, [("4 + 3", TINTA, a, 110), ("=", TINTA, a + 0.3, 110), ("7", TINTA, a + 0.5, 110)], XP, 270)
            conta(c, t, [("+ 1", COR, b_, 110), ("=", TINTA, b_ + 0.3, 110), ("8", COR, b_ + 0.5, 110)], XP, 420)
            E.foco(c, t, c_, 0.5, lambda q: E.pilula(c, "resultado", XP, 590, 60, a=q, cor=E.SOBRE))
            E.foco(c, t, c_ + 0.15, 0.5, lambda q: E.centro(c, "834", XP, 800, 200, "g", COR, q))
        if C["s13"] <= t:
            centenas()
    E.saida(c, t, C["s14"] - 0.1, montagem)
    if t < C["s14"]:
        return

    a, b_, c_, d_, e_ = C["s14.a"], C["s14.b"], C["s14.c"], C["s14.d"], C["s14.e"]
    x = XE + 30
    E.frase(c, t, a, [("a", "i", 96), ("casa", "i", 96), ("deu", "i", 96), ("10", "g", 96, COR), ("ou", "g", 96, COR), ("mais?", "g", 96, COR)], x, 230, passo=0.1)
    E.frase(c, t, b_ - 0.5, [("fica", "i", 76), ("o", "i", 76), ("da", "i", 76), ("direita", "i", 76)], x + 60, 340, passo=0.08)
    E.frase(c, t, b_, [("e", "i", 76), ("vai", "g", 76, COR), ("um", "g", 76, COR)], x + 640, 340, passo=0.1)
    E.frase(c, t, c_, [("deu", "i", 96), ("9", "g", 96), ("ou", "g", 96), ("menos?", "g", 96)], x, 530, passo=0.1)
    E.frase(c, t, c_ + 0.5, [("escreve", "i", 76), ("direto,", "i", 76), ("não", "g", 72), ("vai", "g", 72), ("nada", "g", 72)], x + 60, 640, passo=0.08)
    E.frase(c, t, d_, [("na", "i", 96), ("última", "i", 96), ("casa", "i", 96), ("da", "i", 96), ("esquerda?", "g", 96)], x, 830, passo=0.1)
    E.frase(c, t, e_, [("escreva", "i", 76), ("o", "i", 76), ("número", "g", 72, COR), ("inteiro", "g", 72, COR)], x + 60, 940, passo=0.1)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    a, b_, c_, d_, e_ = C["s15.a"], C["s15.b"], C["s15.c"], C["s15.d"], C["s15.e"]
    s, xv, y0, dy = 140, 700, 400, 170
    t0 = C["s15"] + 0.1
    xs = E._centros("478", xv, s)
    E.foco(c, t, t0, 0.45, lambda q: E.numero(c, "478", xv, y0, s, "g", TINTA, q))
    E.foco(c, t, t0 + 0.2, 0.45, lambda q: (E.numero(c, "356", xv, y0 + dy, s, "g", TINTA, q), E.centro(c, "+", xs[0] - 150, y0 + dy, s, "g", TINTA, q)))
    if t >= t0 + 0.3:
        M.line(c, xs[0] - 200, y0 + dy + 44, xv + 40, y0 + dy + 44, TINTA, 1.0, 6, progress=ep(t, t0 + 0.3, 0.5))
    E.foco(c, t, t0 + 0.5, 0.45, lambda q: E.numero(c, "724", xv, y0 + 2 * dy + 20, s, "g", ERRADO, q))
    # o um que devia ter subido, e não subiu
    for x, ti in ((xs[1], b_), (xs[0], entre(b_, c_, 0.5))):
        E.foco(c, t, ti, 0.4, lambda q, x=x: (E.centro(c, "1", x, y0 - 130, 80, "g", ERRADO, q), E.caixa_pontilhada(c, x - 48, y0 - 200, 96, 96, q, ERRADO)))
        if t >= ti + 0.3:
            E.risco(c, x - 42, y0 - 112, x + 42, y0 - 196, t, ti + 0.3, largura=9)
    E.frase(c, t, a, [("vai", "g", 80, ERRADO), ("um", "g", 80, ERRADO), ("esquecido", "i", 84), ("duas", "g", 80, ERRADO), ("vezes", "g", 80, ERRADO)], W / 2, 130, "center", passo=0.1)
    x = 1330
    E.foco(c, t, entre(b_, c_, 0.86), 0.4, lambda q: E.centro(c, "sem refazer:", x, 300, 72, "i", TINTA2, q))
    E.foco(c, t, c_, 0.45, lambda q: E.centro(c, "400 + 300 = 700", x, 420, 84, "g", TINTA, q))
    E.foco(c, t, d_, 0.45, lambda q: E.centro(c, "70 + 50 = 120", x, 540, 84, "g", TINTA, q))
    E.frase(c, t, entre(d_, e_, 0.4), [("juntos,", "i", 80), ("passam", "i", 80), ("de", "i", 80), ("800", "g", 84, COR)], x, 680, "center", passo=0.1)
    E.frase(c, t, e_, [("não", "i", 80), ("pode", "i", 80), ("ser", "i", 80), ("tão", "g", 76, ERRADO), ("pequeno", "g", 76, ERRADO)], x, 820, "center", passo=0.1)


# ---------------- atalho ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def redondo():
        a, b_, c_, d_, e_, f_ = C["s16.a"], C["s16.b"], C["s16.c"], C["s16.d"], C["s16.e"], C["s16.f"]
        E.frase(c, t, a, [("complete", "g", 92, BR), ("o", "g", 92, BR), ("número", "g", 92, BR), ("redondo", "g", 92, CLARO)], W / 2, 150, "center", passo=0.12)
        E.expressao(c, t, [("199 + 47", "199", c_), ("200 + 46", None), ("246", None)], (e_, f_), 560, 400, 150, empilha=210, escuro=True, t0=b_)
        x = 1320
        E.foco(c, t, c_, 0.45, lambda q: E.centro(c, "199 + 1 = 200", x, 370, 92, "g", CLARO, q))
        E.foco(c, t, d_, 0.45, lambda q: E.centro(c, "47 = 1 + 46", x, 500, 92, "g", BR, q))
        k = ease_back(prog(t, f_, 0.5))
        if k > 0:
            E.selo(c, 860, 775, 66 * k, True)
    E.saida(c, t, C["s17"] - 0.1, redondo)
    if t < C["s17"]:
        return
    a, b_, c_, d_ = C["s17.a"], C["s17.b"], C["s17.c"], C["s17.d"]
    E.frase(c, t, a, [("você", "i", 84, CLARO), ("só", "i", 84, CLARO), ("passou", "i", 84, CLARO), ("um", "g", 80, BR), ("real", "g", 80, BR), ("de", "i", 84, CLARO), ("um", "i", 84, CLARO), ("lado", "i", 84, CLARO), ("para", "i", 84, CLARO), ("o", "i", 84, CLARO), ("outro", "i", 84, CLARO)], W / 2, 240, "center", passo=0.09)
    E.frase(c, t, b_, [("não", "g", 84, ERRADO), ("compensa", "g", 84, ERRADO), ("longe", "i", 92, BR), ("de", "i", 92, BR), ("um", "i", 92, BR), ("redondo", "i", 92, BR)], W / 2, 470, "center", passo=0.1)
    E.foco(c, t, c_, 0.45, lambda q: E.centro(c, "436 + 257", W / 2, 680, 150, "g", BR, q))
    E.frase(c, t, d_, [("arme", "g", 104, CLARO), ("a", "g", 104, CLARO), ("conta", "g", 104, CLARO)], W / 2, 860, "center", passo=0.12)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s18"], [("hora", "i", 72, COR), ("de", "i", 72, COR), ("testar", "i", 72, COR)], XE, 170)
    E.linha(c, t, [("R$ 267", "g", 116, TINTA, C["s18.a"]), ("no", "i", 104, TINTA2, C["s18.a"] + 0.3), ("mercado", "i", 104, TINTA2, C["s18.a"] + 0.4)], XE, 370)
    E.linha(c, t, [("R$ 175", "g", 116, TINTA, C["s18.b"]), ("na", "i", 104, TINTA2, C["s18.b"] + 0.3), ("farmácia", "i", 104, TINTA2, C["s18.b"] + 0.4)], XE, 530)
    E.frase(c, t, C["s18.c"], [("quanto", "i", 108), ("gastou", "i", 108)], XE, 730)
    E.frase(c, t, C["s18.c"] + 0.5, [("ao", "g", 110, COR), ("todo?", "g", 110, COR)], XE, 860)
    E.relogio(c, t, C["s19.a"], 1490, 400)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    xs = E._centros("267", XV, ST)
    banda(c, t, xs[2], C["s20.a"], C["s20.d"], "unidade"); banda(c, t, xs[1], C["s20.d"], C["s21"], "dezena"); banda(c, t, xs[0], C["s21"], C["s21.c"], "centena")
    t0 = C["s20"] + 0.1
    E.armada(c, t, ["267", "175"], "+", "442", (t0, t0 + 0.2), (C["s20.b"], C["s20.f"], C["s21.b"]), XV, Y0, ST,
             vai=[(1, "1", C["s20.c"]), (2, "1", C["s20.g"])])
    x1, x2 = 1060, 1490
    conta(c, t, [("7 + 5", TINTA, C["s20.a"], 84), ("=", TINTA, C["s20.a"] + 0.3, 84), ("12", COR, C["s20.a"] + 0.5, 84)], x1, 280, "left")
    conta(c, t, [("6 + 7", TINTA, C["s20.d"], 84), ("=", TINTA, C["s20.d"] + 0.3, 84), ("13", TINTA, C["s20.d"] + 0.5, 84)], x1, 430, "left")
    conta(c, t, [("+ 1", COR, C["s20.e"], 84), ("=", TINTA, C["s20.e"] + 0.2, 84), ("14", COR, C["s20.e"] + 0.4, 84)], x2, 430, "left")
    conta(c, t, [("2 + 1", TINTA, C["s21.a"], 84), ("=", TINTA, C["s21.a"] + 0.3, 84), ("3", TINTA, C["s21.a"] + 0.5, 84)], x1, 580, "left")
    conta(c, t, [("+ 1", COR, C["s21.b"], 84), ("=", TINTA, C["s21.b"] + 0.2, 84), ("4", COR, C["s21.b"] + 0.4, 84)], x2, 580, "left")
    k = ease_back(prog(t, C["s21.c"], 0.55))
    if k > 0:
        E.foco(c, t, C["s21.c"], 0.5, lambda q: (E.pilula(c, "R$ 442", 1380, 790, 120, estilo="g", fundo=CERTO, a=q)))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s22.a"], [("de", "i", 110), ("cabeça,", "i", 110), ("complete", "g", 104, COR), ("o", "g", 104, COR), ("dez", "g", 104, COR)], W / 2, 300, "center", passo=0.12)
        E.frase(c, t, C["s22.b"], [("na", "i", 110), ("conta", "i", 110), ("armada,", "i", 110), ("casa", "g", 104, COR), ("com", "g", 104, COR), ("casa", "g", 104, COR)], W / 2, 530, "center", passo=0.12)
        E.frase(c, t, C["s22.c"], [("a", "i", 110), ("cada", "i", 110), ("dez,", "i", 110), ("vai", "g", 104, COR), ("um", "g", 104, COR)], W / 2, 760, "center", passo=0.12)
    E.saida(c, t, C["s23"] - 0.1, resumo)
    if t < C["s23"]:
        return
    E.frase(c, t, C["s23.a"] - 1.0, [("próxima", "i", 84), ("aula", "i", 84)], XE, 270)
    E.frase(c, t, C["s23.a"], [("subtrair", "g", 120, COR)], XE, 410)
    E.frase(c, t, C["s23.b"], [("conferir", "i", 84), ("com", "i", 84), ("uma", "i", 84), ("soma", "i", 84)], XE, 520, passo=0.1)
    E.frase(c, t, C["s23.c"], [("pedir", "g", 84), ("emprestado", "g", 84)], XE, 640, passo=0.1)
    E.foco(c, t, C["s23.d"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1400, 400, 76, estilo="g", cor=E.SOBRE, a=a))
    p = ease_io(prog(t, C["s23.d"] + 0.3, 0.8))
    E.cursor(c, lerp(1760, 1530, p), lerp(720, 425, p), ep(t, C["s23.d"] + 0.2, 0.4))
    E.frase(c, t, C["s23.e"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 880, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, dez=b_dez, armar=b_armar, erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
