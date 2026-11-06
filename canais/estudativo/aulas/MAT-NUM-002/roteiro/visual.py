"""Visual — Estudativo · MAT-NUM-002: ler e comparar números grandes.
Identidade em _ferramentas/editorial.py. O número grande fica sempre em colunas fixas (peça local `pontos`), para o olho
comparar casa com casa, e os pontos são tratados como o que são: placas com nome (mil, milhão)."""
import math

import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco
import motor as M
import skia

E.usar("Matemática", "Números e Contas")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-NUM-002_ler_comparar_numeros_grandes.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("grupos", "leitura", "comparar", "atalho", "questao", "fim"))
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


def pontos(c, s, cx, y, size, cor=TINTA, a=1.0, cores=None, align="center"):
    """número com pontos em colunas fixas: dois números do mesmo tamanho ficam casa sobre casa. Devolve {índice: x do centro}"""
    cl, cp = E.larg("0", "g", size) * 1.14, E.larg("0", "g", size) * 0.5
    w = sum(cp if ch in ".," else cl for ch in s)
    x = cx - w / 2 if align == "center" else cx
    xs = {}
    for i, ch in enumerate(s):
        adv = cp if ch in ".," else cl
        xs[i] = x + adv / 2
        if a > 0:
            E.centro(c, ch, xs[i], y, size, "g", (cores or {}).get(i, cor), a)
        x += adv
    return xs


def preco(c, s, cx, y, size, cor=TINTA, a=1.0, cores=None, align="center", cor_rs=None):
    """R$ menor na frente de `pontos`"""
    wr = E.larg("R$", "g", size * 0.6) + size * 0.22
    cl, cp = E.larg("0", "g", size) * 1.14, E.larg("0", "g", size) * 0.5
    w = sum(cp if ch in ".," else cl for ch in s)
    x0 = cx - (w + wr) / 2 if align == "center" else cx
    E.escreve(c, "R$", x0, y, size * 0.6, "g", cor_rs or TINTA2, a)
    return pontos(c, s, x0 + wr, y, size, cor, a, cores, "left")


def faixa(c, x, y, w, h, a, cor=None):
    M.rrect(c, x, y, w, h, 18, cor or E.COR, 0.1 * a)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def premio():
        E.frase(c, t, C["s01.a"], [("este", "i", 104), ("prêmio", "g", 100, COR)], W / 2, 260, "center")
        cen = {}
        E.foco(c, t, C["s01.a"] + 0.2, 0.5, lambda a: cen.update(preco(c, "2.048.500", W / 2, 590, 210, a=a)))
        E.frase(c, t, C["s01.b"], [("trava", "g", 100, ERRADO), ("e", "i", 104), ("conta", "i", 104), ("casa", "i", 104), ("com", "i", 104), ("o", "i", 104), ("dedo", "i", 104)], W / 2, 880, "center", passo=0.12)
        # o dedo que anda de casa em casa
        if t >= C["s01.b"] and cen:
            d = [i for i in cen if "2.048.500"[i] != "."][::-1]
            f = (t - C["s01.b"]) * 2.4
            i0 = int(f) % len(d)
            x = lerp(cen[d[i0]], cen[d[(i0 + 1) % len(d)]], ease_io(min(1.0, (f - int(f)) * 2)))
            E.cursor(c, x - 6, 610 - 26 * abs(math.sin(f * math.pi)), ep(t, C["s01.b"], 0.3), escala=1.1)
    E.saida(c, t, C["s02"] - 0.1, premio)

    def precos():
        fim = C["s02.b"]
        cores = {3: ERRADO, 4: ERRADO} if t >= fim else None
        E.frase(c, t, C["s02.a"], [("qual", "i", 104), ("é", "i", 104), ("o", "i", 104), ("maior?", "g", 100, COR)], W / 2, 240, "center", passo=0.12)
        E.foco(c, t, C["s02.a"] + 0.2, 0.5, lambda a: preco(c, "1.099", 520, 560, 170, a=a, cores=cores))
        E.foco(c, t, C["s02.a"] + 0.5, 0.5, lambda a: preco(c, "1.101", 1400, 560, 170, a=a, cores=cores))
        E.frase(c, t, fim, [("erra", "g", 92, ERRADO), ("por", "i", 96), ("olhar", "i", 96), ("o", "i", 96), ("lugar", "i", 96), ("errado", "i", 96)], W / 2, 830, "center", passo=0.12)
    if C["s02"] <= t:
        E.saida(c, t, C["s03"] - 0.1, precos)

    if t >= C["s03"]:
        a_, b_ = C["s03.a"], C["s03.b"]
        E.foco(c, t, b_ - 0.2, 0.7, lambda a: E.bola(c, 1450, 520, 300 * ease_back(prog(t, b_ - 0.2, 0.7))), blur=0)
        E.frase(c, t, a_, [("até", "i", 92), ("o", "i", 92), ("fim", "i", 92), ("desta", "i", 92), ("aula", "i", 92)], XE, 340)
        E.frase(c, t, entre(a_, b_, 0.4), [("você", "i", 92), ("lê", "g", 108, COR)], XE, 500)
        E.frase(c, t, entre(a_, b_, 0.45), [("qualquer", "g", 108), ("número", "g", 108)], XE, 620)
        E.frase(c, t, entre(a_, b_, 0.75), [("e", "i", 92), ("compara", "g", 108, COR), ("sem", "i", 92), ("erro", "i", 92)], XE, 750)
        E.foco(c, t, b_ + 0.2, 0.5, lambda a: (E.escreve(c, "+ atalho", 1270, 505, 88, "g", E.SOBRE, a),
                                               E.escreve(c, "de prova", 1300, 595, 88, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    a_, fim = C["s04.a"], C["s04.end"]
    E.frase(c, t, C["s04"] + 0.1, [("para", "i", 84), ("acompanhar:", "i", 84)], W / 2, 170, "center", passo=0.12)
    E.frase(c, t, a_, [("uma", "i", 96), ("coisa:", "i", 96), ("o", "i", 96), ("algarismo", "i", 96), ("vale", "i", 96), ("pelo", "i", 96), ("lugar", "g", 92, COR)], W / 2, 320, "center", passo=0.14)
    E.quadro_casas(c, t, ("centena", "dezena", "unidade"), (C["s04.d"], C["s04.c"], C["s04.b"]),
                   [[("3", C["s04.d"]), ("5", C["s04.c"]), ("2", C["s04.b"])]], 420, 530, 360, 170, grossa=None)
    E.frase(c, t, entre(C["s04.d"], fim, 0.45), [("se", "i", 66, TINTA2), ("faltar,", "i", 66, TINTA2), ("procure", "i", 66, TINTA2), ("a", "i", 66, TINTA2), ("aula", "i", 66, TINTA2), ("no", "i", 66, TINTA2), ("canal", "i", 66, TINTA2)], W / 2, 920, "center", passo=0.08)


# ---------------- grupos ----------------
NUM, NSIZE, NY = "2048500", 200, 560
GRUPO = (0, 1, 1, 1, 2, 2, 2)


def cheio(c, t, abre, cores=None, a=1.0, y=NY):
    """os sete algarismos do prêmio; abre = 0..1 separa os grupos. Devolve o centro de cada algarismo"""
    cl = E.larg("0", "g", NSIZE) * 1.1
    gap = 100 * abre
    w = 7 * cl + 2 * gap
    x0 = W / 2 - w / 2
    xs = []
    for i, ch in enumerate(NUM):
        x = x0 + (i + 0.5) * cl + GRUPO[i] * gap
        xs.append(x)
        E.centro(c, ch, x, y, NSIZE, "g", (cores or {}).get(i, TINTA), a)
    return xs, cl, gap


def b_grupos(c, t, C, b):
    def mil():
        a_, b_, c_, d_, e_ = C["s05.a"], C["s05.b"], C["s05.c"], C["s05.d"], C["s05.e"]
        y = 250
        for i in range(10):
            E.foco(c, t, entre(C["s05"], a_, 0.5) + i * 0.08, 0.35, lambda q, i=i: nota(c, 300 + i * 30, y + (i % 2) * 10, 280, "100", q, TINTA), sobe=-12)
        E.sinal(c, t, a_ + 0.4, "=", 790, y, 100)
        E.foco(c, t, a_ + 0.6, 0.5, lambda q: preco(c, "1.000", 870, y + 44, 124, a=q, align="left", cor=COR))
        E.foco(c, t, b_, 0.45, lambda q: E.pilula(c, "milhar", 1640, y, 66, estilo="g", cor=E.SOBRE, a=q))
        y = 540
        E.frase(c, t, c_, [("mil", "g", 76, TINTA), ("grupos", "i", 82), ("de", "i", 82), ("mil", "i", 82)], XE + 20, y + 30, passo=0.14)
        E.sinal(c, t, d_ - 0.2, "=", 790, y, 100)
        E.foco(c, t, d_, 0.5, lambda q: pontos(c, "1.000.000", 870, y + 44, 124, COR, q, align="left"))
        E.foco(c, t, d_ + 0.2, 0.45, lambda q: E.pilula(c, "milhão", 1300, y + 118, 56, estilo="g", cor=E.SOBRE, a=q))
        y = 880
        E.frase(c, t, entre(d_, e_, 0.55), [("R$ 1.000", "g", 72, TINTA), ("por", "i", 84), ("mês:", "i", 84)], XE + 20, y + 28, passo=0.14)
        E.frase(c, t, e_, [("mais", "i", 104), ("de", "i", 104), ("80", "g", 112, COR), ("anos", "g", 104, COR)], 880, y + 36, passo=0.14)
    E.saida(c, t, C["s06"] - 0.1, mil)

    def separa():
        a_, b_, c_ = C["s06.a"], C["s06.b"], C["s06.c"]
        E.frase(c, t, a_, [("grupos", "g", 92, COR), ("de", "g", 92, COR), ("três", "g", 92, COR), ("algarismos", "i", 100)], W / 2, 190, "center", passo=0.12)
        abre = ease_io(prog(t, b_, 0.8))
        res = {}
        E.foco(c, t, C["s06"] + 0.1, 0.5, lambda q: res.update(zip("xcg", cheio(c, t, abre, a=q))))
        if not res:
            return
        xs, cl, gap = res["x"], res["c"], res["g"]
        # a seta vai da direita para a esquerda, e as chaves nascem na mesma ordem
        if t >= b_:
            p = ep(t, b_, 0.7)
            M.arrow(c, 1680, 300, 240, 300, E.COR, p, 6, 22, p)
        for k, (i0, i1) in enumerate(((4, 6), (1, 3), (0, 0))):
            q = ep(t, b_ + 0.3 + k * 0.45, 0.5)
            E.chave(c, xs[i0] - cl * 0.42, xs[i1] + cl * 0.42, NY + 30, E.COR, q, h=26, largura=7)
        # os pontos caem nos vãos
        for k, i in enumerate((4, 1)):
            q = ease_back(prog(t, c_ + k * 0.25, 0.5))
            if q > 0:
                E.centro(c, ".", xs[i] - cl / 2 - gap / 2, lerp(NY - 300, NY, q), NSIZE, "g", COR, M.clamp(q * 2))
        E.frase(c, t, c_ + 0.3, [("os", "i", 88), ("pontos", "g", 84, COR), ("fazem", "i", 88), ("essa", "i", 88), ("separação", "i", 88)], W / 2, 790, "center", passo=0.12)
        E.frase(c, t, entre(c_, C["s06.end"], 0.55), [("em", "i", 80), ("preço", "g", 74), ("e", "i", 80), ("em", "i", 80), ("salário", "g", 74)], W / 2, 920, "center", passo=0.12)
    if C["s06"] <= t:
        E.saida(c, t, C["s07"] - 0.1, separa)
    if t < C["s07"]:
        return

    a_, b_, c_ = C["s07.a"], C["s07.b"], C["s07.c"]
    xs, cl, gap = cheio(c, t, 1.0)
    d1, d2 = xs[4] - cl / 2 - gap / 2, xs[1] - cl / 2 - gap / 2
    E.centro(c, ".", d1, NY, NSIZE, "g", COR); E.centro(c, ".", d2, NY, NSIZE, "g", COR)
    E.frase(c, t, C["s07"] + 0.1, [("cada", "i", 88), ("ponto", "g", 84, COR), ("tem", "i", 88), ("um", "i", 88), ("nome", "i", 88)], W / 2, 170, "center", passo=0.12)
    for x, rot, nome, ti in ((d1, "primeiro ponto", "mil", a_), (d2, "segundo ponto", "milhão", b_)):
        p = ep(t, ti, 0.5)
        if p > 0:
            M.arrow(c, x, 350, x, 520, E.COR, p, 6, 20, p)
        E.foco(c, t, ti, 0.45, lambda q, x=x, nome=nome, rot=rot: (E.pilula(c, nome, x, 320, 66, estilo="g", cor=E.SOBRE, a=q), E.centro(c, rot, x, 250, 54, "i", TINTA2, q)))
    # dentro de cada grupo as casas se repetem
    nomes = ("unidade", "centena", "dezena", "unidade", "centena", "dezena", "unidade")
    for i, n in enumerate(nomes):
        E.foco(c, t, c_ + GRUPO[i] * 0.3 + (i % 3) * 0.08, 0.4, lambda q, i=i, n=n: E.centro(c, n, xs[i], 640, 42, "i", COR, q))
    E.frase(c, t, entre(c_, C["s07.end"], 0.6), [("um", "g", 84, COR), ("grupo", "g", 84, COR), ("de", "i", 92), ("cada", "i", 92), ("vez", "i", 92)], W / 2, 860, "center", passo=0.12)


# ---------------- leitura ----------------
def b_leitura(c, t, C, b):
    s, y = 190, 330
    n = "2.048.500"
    g0, g1, g2 = (0, 0), (2, 4), (6, 8)
    zero = t >= C["s09.a"]
    xs = pontos(c, n, W / 2, y, s, a=0)
    cl = E.larg("0", "g", s) * 1.14

    def banda(g, t0, t1):
        q = ep(t, t0, 0.4) * (1 - ep(t, t1, 0.4))
        if q > 0:
            faixa(c, xs[g[0]] - cl * 0.56, y - 170, xs[g[1]] - xs[g[0]] + cl * 1.12, 205, q)
    banda(g0, C["s08.a"], C["s09"])
    banda(g1, C["s09.a"], C["s10"])
    banda(g2, C["s10.a"], C["s10.c"])
    E.foco(c, t, C["s08"] + 0.1, 0.5, lambda a: pontos(c, n, W / 2, y, s, a=a, cores={2: CINZA} if zero else None))
    E.frase(c, t, entre(C["s08"], C["s08.a"], 0.65), [("a", "i", 80), ("leitura", "i", 80), ("começa", "i", 80), ("pela", "i", 80), ("esquerda", "g", 76, COR)], W / 2, 110, "center", passo=0.1)
    # zero na frente: a centena vazia não se fala
    E.saida(c, t, C["s09.b"], lambda: E.foco(c, t, C["s09.a"], 0.4, lambda a: E.pilula(c, "centena vazia", xs[2] + 40, y + 90, 50, a=a, cor=E.SOBRE)))
    E.saida(c, t, C["s10.c"], lambda: E.foco(c, t, C["s10.a"], 0.4, lambda a: E.pilula(c, "sem ponto depois, sem nome", xs[7] - 100, y + 90, 46, fundo=TINTA, a=a)))

    yl = 660
    itens = (("dois milhões", 390, C["s08.b"], xs[0]), ("quarenta e oito mil", 960, C["s09.c"], xs[3]), ("quinhentos", 1530, C["s10.b"], xs[7]))
    for txt, x, ti, xg in itens:
        p = ep(t, ti - 0.2, 0.4)
        if p > 0:
            M.arrow(c, xg, y + 150, x, yl - 86, FIO if t >= C["s10.c"] else E.COR, p, 5, 18, p)
        E.foco(c, t, ti, 0.45, lambda a, txt=txt, x=x: E.centro(c, txt, x, yl, 66, "g", COR, a))
    q = C["s10.c"]
    E.frase(c, t, q, [("dois", "g", 84), ("milhões,", "g", 84)], W / 2, 830, "center", passo=0.14)
    E.frase(c, t, entre(q, C["s10.end"], 0.3), [("quarenta", "g", 84), ("e", "g", 84), ("oito", "g", 84), ("mil", "g", 84), ("e", "i", 92), ("quinhentos", "g", 84)], W / 2, 950, "center", passo=0.12)


# ---------------- comparar ----------------
def b_comparar(c, t, C, b):
    def quantos():
        a_, b_, c_, fim = C["s11.a"], C["s11.b"], C["s11.c"], C["s11.end"]
        E.frase(c, t, a_, [("quem", "i", 104), ("tem", "i", 104), ("mais", "g", 96, COR), ("algarismos?", "g", 96, COR)], W / 2, 190, "center", passo=0.12)
        E.foco(c, t, b_, 0.45, lambda q: pontos(c, "1.000", 540, 530, 200, a=q))
        E.foco(c, t, b_ + 0.15, 0.45, lambda q: E.centro(c, "quatro algarismos", 540, 650, 68, "i", COR, q))
        E.foco(c, t, c_, 0.45, lambda q: pontos(c, "999", 1380, 530, 200, a=q))
        E.foco(c, t, c_ + 0.15, 0.45, lambda q: E.centro(c, "três algarismos", 1380, 650, 68, "i", TINTA2, q))
        r = 70 * ease_back(prog(t, entre(c_, fim, 0.2), 0.5))
        E.selo(c, 980, 480, r, True)
        E.frase(c, t, entre(c_, fim, 0.55), [("com", "i", 72, TINTA2), ("vírgula,", "i", 72, TINTA2), ("a", "i", 72, TINTA2), ("conversa", "i", 72, TINTA2), ("é", "i", 72, TINTA2), ("outra:", "i", 72, TINTA2), ("fica", "i", 72, TINTA2), ("para", "i", 72, TINTA2), ("outra", "i", 72, TINTA2), ("aula", "i", 72, TINTA2)], W / 2, 860, "center", passo=0.08)
    E.saida(c, t, C["s12"] - 0.1, quantos)

    def regra():
        E.frase(c, t, C["s12"] + 0.1, [("deu", "i", 104), ("empate?", "g", 96, COR)], W / 2, 230, "center")
        E.frase(c, t, C["s12.a"], [("casa", "g", 110), ("por", "i", 116), ("casa", "g", 110)], W / 2, 430, "center", passo=0.14)
        p = ep(t, C["s12.a"] + 0.2, 0.8)
        if p > 0:
            M.arrow(c, 400, 540, 1520, 540, E.COR, p, 7, 26, p)
        E.frase(c, t, C["s12.b"], [("a", "i", 104), ("primeira", "i", 104), ("casa", "i", 104), ("diferente", "g", 96, COR), ("decide", "g", 96, COR)], W / 2, 760, "center", passo=0.12)
    if C["s12"] <= t:
        E.saida(c, t, C["s13"] - 0.1, regra)

    def conta():
        a_, b_, c_, d_, e_ = C["s13.a"], C["s13.b"], C["s13.c"], C["s13.d"], C["s13.e"]
        x0, wc, y, size = 460, 250, 230, 150
        xs = [x0 + (i + 0.5) * wc for i in range(4)]
        q = ep(t, c_, 0.4) * (1 - ep(t, d_, 0.4))
        if q > 0:
            faixa(c, xs[0] - 118, 130, 236, 500, q)
        q = ep(t, d_, 0.4)
        if q > 0:
            faixa(c, xs[1] - 118, 130, 236, 500, q)
        um = COR if t >= d_ else TINTA
        E.quadro_casas(c, t, ("milhar", "centena", "dezena", "unidade"), (a_, a_, a_, a_),
                       [[("1", a_), ("0", a_), ("9", a_), ("9", a_)], [("1", b_), ("1", b_, um), ("0", b_), ("1", b_)]], x0, y, wc, size, h_lin=190, grossa=None)
        E.saida(c, t, c_, lambda: E.frase(c, t, entre(b_, c_, 0.4), [("quatro", "i", 84), ("algarismos", "i", 84), ("em", "i", 84), ("cada:", "i", 84), ("empate", "g", 80)], W / 2, 770, "center", passo=0.1))
        E.saida(c, t, d_, lambda: E.frase(c, t, c_ + 0.1, [("um", "i", 84), ("contra", "i", 84), ("um:", "i", 84), ("empate", "g", 80)], W / 2, 770, "center", passo=0.1))
        E.saida(c, t, e_, lambda: E.frase(c, t, d_ + 0.1, [("zero", "g", 80), ("contra", "i", 84), ("um", "g", 80, COR)], W / 2, 770, "center", passo=0.1))
        E.foco(c, t, e_, 0.5, lambda q: pontos(c, "1.101", 610, 860, 160, COR, q))
        E.frase(c, t, e_ + 0.2, [("é", "i", 120), ("maior", "g", 112, COR)], 910, 860)
        r = 62 * ease_back(prog(t, e_ + 0.4, 0.5))
        E.selo(c, 1380, 815, r, True)
    if C["s13"] <= t:
        E.saida(c, t, C["s14"] - 0.1, conta)
    if t < C["s14"]:
        return

    a_, b_, c_ = C["s14.a"], C["s14.b"], C["s14.c"]
    E.frase(c, t, C["s14"] + 0.1, [("por", "i", 96), ("que", "i", 96), ("a", "i", 96), ("esquerda", "g", 92, COR), ("manda?", "i", 96)], W / 2, 170, "center", passo=0.12)
    E.foco(c, t, a_, 0.45, lambda q: pontos(c, "1.101", 400, 400, 150, a=q))
    E.foco(c, t, a_ + 0.2, 0.5, lambda q: nota(c, 930, 345, 320, "100", q, TINTA))
    E.foco(c, t, a_ + 0.35, 0.45, lambda q: E.escreve(c, "depois do mil", 1130, 370, 72, "i", TINTA2, q))
    E.foco(c, t, entre(a_, b_, 0.45), 0.45, lambda q: pontos(c, "1.099", 400, 640, 150, a=q))
    E.foco(c, t, b_, 0.45, lambda q: E.centro(c, "R$ 99", 930, 640, 116, "g", ERRADO, q))
    E.foco(c, t, entre(b_, c_, 0.45), 0.45, lambda q: E.escreve(c, "não chega a cem", 1130, 620, 72, "i", TINTA2, q))
    E.frase(c, t, c_, [("uma", "g", 76, COR), ("nota", "g", 76, COR), ("só", "g", 76, COR), ("vale", "i", 84), ("mais", "i", 84), ("que", "i", 84), ("tudo", "i", 84), ("o", "i", 84), ("que", "i", 84), ("vem", "i", 84), ("depois", "i", 84)], W / 2, 860, "center", passo=0.1)


# ---------------- sinais ----------------
def sinal_grande(c, s, cx, cy, size, cor, a=1.0, flip=1.0):
    c.save(); c.translate(cx, cy); c.scale(flip, 1)
    E.centro(c, s, 0, size * 0.34, size, "g", cor, a)
    c.restore()


def b_sinais(c, t, C, b):
    def apresenta():
        a_, b_, c_, d_, e_ = C["s15.a"], C["s15.b"], C["s15.c"], C["s15.d"], C["s15.e"]
        E.frase(c, t, a_, [("dois", "g", 92, COR), ("sinais", "i", 100)], W / 2, 150, "center")
        yc = 360
        for x, s, nome, ti in ((560, ">", "maior que", b_), (1360, "<", "menor que", c_)):
            k = ease_back(prog(t, ti, 0.55))
            if k > 0:
                sinal_grande(c, s, x, yc, 340 * k, COR, M.clamp(k * 2))
            E.foco(c, t, ti + 0.15, 0.45, lambda q, x=x, nome=nome: E.centro(c, nome, x, 640, 84, "g", TINTA, q))
        # a abertura olha para o maior; a ponta, para o menor
        for x, s_, cor, ti in ((275, "maior", COR, d_), (1645, "maior", COR, d_), (800, "menor", TINTA2, e_), (1120, "menor", TINTA2, e_)):
            E.foco(c, t, ti + (0.2 if x > 1000 else 0), 0.45, lambda q, x=x, s_=s_, cor=cor: E.centro(c, s_, x, yc + 24, 72, "g", cor, q))
        E.frase(c, t, d_, [("a", "i", 92), ("abertura", "g", 84, COR), ("fica", "i", 92), ("para", "i", 92), ("o", "i", 92), ("maior", "g", 84, COR)], W / 2, 810, "center", passo=0.1)
        E.frase(c, t, e_, [("a", "i", 92), ("ponta", "g", 84), ("fica", "i", 92), ("para", "i", 92), ("o", "i", 92), ("menor", "g", 84)], W / 2, 930, "center", passo=0.1)
    E.saida(c, t, C["s16"] - 0.1, apresenta)
    if t < C["s16"]:
        return

    a_, b_, c_ = C["s16.a"], C["s16.b"], C["s16.c"]
    L, R, y1, y2, s = 480, 1440, 340, 620, 170
    E.foco(c, t, a_, 0.45, lambda q: (pontos(c, "1.101", L, y1, s, COR, q), pontos(c, "1.099", R, y1, s, a=q)))
    E.foco(c, t, a_ + 0.2, 0.45, lambda q: sinal_grande(c, ">", W / 2, y1 - 60, 190, TINTA, q))
    E.foco(c, t, a_ + 0.3, 0.45, lambda q: E.centro(c, "maior que", W / 2, y1 + 60, 54, "i", TINTA2, q))
    # a segunda linha nasce da primeira: os números trocam de lado e o sinal vira
    if t >= b_:
        q = ease_io(prog(t, b_, 1.0))
        arco = math.sin(q * math.pi) * 80
        pontos(c, "1.101", lerp(L, R, q), lerp(y1, y2, q) - arco, s, COR, M.clamp(q * 6))
        pontos(c, "1.099", lerp(R, L, q), lerp(y1, y2, q) + arco, s, TINTA, M.clamp(q * 6))
        flip = lerp(1, -1, q)
        sinal_grande(c, ">", W / 2, lerp(y1, y2, q) - 60, 190, TINTA, M.clamp(q * 6), flip if abs(flip) > 0.05 else 0.05)
        E.foco(c, t, b_ + 0.9, 0.45, lambda a: E.centro(c, "menor que", W / 2, y2 + 60, 54, "i", TINTA2, a))
    E.foco(c, t, c_, 0.5, lambda a: E.pilula(c, "a mesma informação", W / 2, 860, 80, estilo="g", cor=E.SOBRE, a=a))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    a_, b_, c_, d_ = C["s17.a"], C["s17.b"], C["s17.c"], C["s17.d"]
    E.frase(c, t, a_, [("olhar", "i", 104), ("o", "i", 104), ("fim", "g", 100, ERRADO), ("do", "i", 104), ("número", "i", 104)], W / 2, 170, "center", passo=0.12)
    cores = {3: ERRADO, 4: ERRADO} if t >= b_ else None
    E.foco(c, t, a_ + 0.2, 0.45, lambda q: pontos(c, "1.099", 520, 390, 170, a=q, cores=cores))
    E.foco(c, t, a_ + 0.4, 0.45, lambda q: pontos(c, "1.101", 520, 590, 170, a=q, cores=cores))
    E.linha(c, t, [("99", "g", 150, ERRADO, b_), ("contra", "i", 104, TINTA, b_ + 0.3), ("1", "g", 150, ERRADO, b_ + 0.6)], 1330, 500, "center")
    E.frase(c, t, c_, [("a", "i", 88), ("parte", "i", 88), ("que", "i", 88), ("menos", "g", 84, ERRADO), ("vale", "g", 84, ERRADO)], W / 2, 750, "center", passo=0.12)
    E.frase(c, t, d_, [("só", "i", 84), ("as", "i", 84), ("moedas,", "i", 84), ("ignorando", "g", 76), ("as", "g", 76), ("notas", "g", 76)], XE, 920, passo=0.12)
    fim_ = C["s17.end"]
    k = ease_back(prog(t, entre(d_, fim_, 0.3), 0.4))
    if k > 0:
        E.moeda(c, 1400, 890, 70 * k, "R$1", M.clamp(k * 2))
    E.foco(c, t, entre(d_, fim_, 0.45), 0.35, lambda q: nota(c, 1640, 890, 250, "100", q, TINTA))
    if t >= entre(d_, fim_, 0.65):
        E.risco(c, 1520, 955, 1760, 825, t, entre(d_, fim_, 0.65), largura=12, d=0.25)


# ---------------- atalho ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def conta_pontos():
        a_, b_, c_, d_, e_ = C["s18.a"], C["s18.b"], C["s18.c"], C["s18.d"], C["s18.e"]
        E.frase(c, t, a_, [("conte", "g", 92, BR), ("os", "g", 92, BR), ("pontos", "g", 92, CLARO), ("primeiro", "g", 92, BR)], W / 2, 170, "center", passo=0.12)
        E.frase(c, t, b_, [("mais", "i", 84, CLARO), ("pontos,", "i", 84, CLARO), ("número", "g", 76, BR), ("maior", "g", 76, BR)], W / 2, 280, "center", passo=0.12)
        s = 150
        x1, x2 = 640, 640
        res = {}
        E.foco(c, t, c_, 0.45, lambda q: pontos(c, "990.000", x1, 520, s, BR, q, cores={3: CLARO}))
        E.foco(c, t, c_ + 0.3, 0.45, lambda q: E.escreve(c, "um ponto", 1190, 505, 88, "i", CLARO, q))
        E.foco(c, t, d_, 0.45, lambda q: res.update(pontos(c, "1.000.010", x2, 760, s, BR, q, cores={1: CLARO, 5: CLARO})))
        E.foco(c, t, d_ + 0.3, 0.45, lambda q: E.escreve(c, "dois pontos", 1190, 745, 76, "g", BR, q))
        if res:
            ti = entre(d_, e_, 0.55)
            q = ep(t, ti, 0.45)
            E.chave(c, res[2] - 46, res[4] + 46, 785, CLARO, q, h=24, largura=6)
            E.foco(c, t, ti + 0.1, 0.4, lambda a: E.centro(c, "só zeros: não se fala", res[3], 880, 50, "i", CLARO, a))
        r = 66 * ease_back(prog(t, e_, 0.5))
        E.selo(c, 1730, 715, r, True)
    E.saida(c, t, C["s19"] - 0.1, conta_pontos)
    if t < C["s19"]:
        return
    a_, b_, c_ = C["s19.a"], C["s19.b"], C["s19.c"]
    E.frase(c, t, a_, [("cada", "i", 96, CLARO), ("ponto", "i", 96, CLARO), ("é", "i", 96, CLARO)], W / 2, 250, "center")
    E.frase(c, t, a_ + 0.5, [("um", "g", 96, BR), ("grupo", "g", 96, BR), ("de", "g", 96, BR), ("casas", "g", 96, BR), ("a", "g", 96, BR), ("mais", "g", 96, BR)], W / 2, 370, "center", passo=0.1)
    E.frase(c, t, b_, [("não", "g", 88, ERRADO), ("compensa", "g", 88, ERRADO), ("com", "i", 96, BR), ("pontos", "i", 96, BR), ("iguais", "i", 96, BR)], W / 2, 620, "center", passo=0.12)
    E.frase(c, t, c_, [("volte", "i", 96, CLARO), ("para", "i", 96, CLARO), ("casa", "g", 88, BR), ("por", "g", 88, BR), ("casa", "g", 88, BR)], W / 2, 770, "center", passo=0.12)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s20"], [("hora", "i", 72, COR), ("de", "i", 72, COR), ("testar", "i", 72, COR)], XE, 170)
    E.foco(c, t, C["s20.a"], 0.45, lambda q: preco(c, "1.040.698", XE, 330, 110, a=q, align="left"))
    E.foco(c, t, C["s20.b"], 0.45, lambda q: preco(c, "1.040.705", XE, 490, 110, a=q, align="left"))
    E.frase(c, t, C["s20.c"], [("leia", "g", 88, COR), ("cada", "i", 92), ("preço", "i", 92), ("em", "i", 92), ("voz", "i", 92), ("alta", "i", 92)], XE, 690, passo=0.1)
    E.frase(c, t, C["s20.d"], [("qual", "i", 92), ("é", "i", 92), ("maior?", "g", 88, COR), ("use", "i", 92), ("o", "i", 92), ("sinal", "i", 92)], XE, 830, passo=0.1)
    E.relogio(c, t, C["s21.a"], 1490, 400)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    def leitura():
        a_, b_ = C["s22.a"], C["s22.b"]
        E.foco(c, t, C["s22"] + 0.2, 0.45, lambda q: preco(c, "1.040.698", W / 2, 300, 140, a=q))
        E.frase(c, t, a_, [("um", "i", 72), ("milhão,", "i", 72), ("quarenta", "i", 72), ("mil,", "i", 72), ("seiscentos", "g", 64, COR), ("e", "g", 64, COR), ("noventa", "g", 64, COR), ("e", "g", 64, COR), ("oito", "g", 64, COR), ("reais", "i", 72)], W / 2, 420, "center", passo=0.13)
        E.foco(c, t, entre(a_, b_, 0.82), 0.45, lambda q: preco(c, "1.040.705", W / 2, 680, 140, a=q))
        E.frase(c, t, b_, [("um", "i", 72), ("milhão,", "i", 72), ("quarenta", "i", 72), ("mil,", "i", 72), ("setecentos", "g", 64, COR), ("e", "g", 64, COR), ("cinco", "g", 64, COR), ("reais", "i", 72)], W / 2, 800, "center", passo=0.13)
    E.saida(c, t, C["s23"] - 0.1, leitura)
    if t < C["s23"]:
        return

    a_, b_, c_ = C["s23.a"], C["s23.b"], C["s23.c"]
    s = 160
    n1, n2 = "1.040.698", "1.040.705"
    xs = pontos(c, n1, W / 2, 0, s, a=0)
    cl = E.larg("0", "g", s) * 1.14
    cols = [0, 2, 3, 4]  # as casas antes da centena: tudo empata
    prox = 6  # a casa da centena
    cin = {}
    for k, i in enumerate(cols):
        if t >= entre(a_, b_, (k + 1) / 5):
            cin[i] = CINZA
    if a_ <= t:
        f = M.clamp((t - a_) / max(0.1, b_ - a_))
        idx = min(len(cols) - 1, int(f * len(cols)))
        xb = xs[cols[idx]] if t < b_ else xs[prox]
        faixa(c, xb - cl * 0.55, 180, cl * 1.1, 400, 1.0, E.COR)
    cores1 = dict(cin); cores2 = dict(cin)
    if t >= b_:
        cores2[prox] = COR
    E.foco(c, t, C["s23"] + 0.1, 0.45, lambda q: pontos(c, n1, W / 2, 330, s, a=q, cores=cores1))
    E.foco(c, t, C["s23"] + 0.1, 0.45, lambda q: pontos(c, n2, W / 2, 530, s, a=q, cores=cores2))
    E.frase(c, t, entre(b_, c_, 0.4), [("o", "i", 80), ("sete", "g", 76, COR), ("decide,", "i", 80), ("mesmo", "i", 80), ("com", "i", 80), ("o", "i", 80), ("fim", "i", 80), ("menor", "i", 80)], W / 2, 680, "center", passo=0.1)
    E.foco(c, t, c_, 0.45, lambda q: (pontos(c, n2, 530, 860, 104, COR, q), E.centro(c, ">", 960, 858, 110, "g", TINTA, q), pontos(c, n1, 1390, 860, 104, a=q)))
    E.frase(c, t, c_ + 0.4, [("o", "i", 66, TINTA2), ("segundo", "i", 66, TINTA2), ("preço", "i", 66, TINTA2), ("é", "i", 66, TINTA2), ("maior", "i", 66, TINTA2)], W / 2, 985, "center", passo=0.1)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s24.a"], [("grupos", "g", 140, COR), ("de", "g", 140, COR), ("três", "g", 140, COR)], W / 2, 330, "center", passo=0.12)
        E.frase(c, t, C["s24.a"] + 0.5, [("para", "i", 120), ("ler", "i", 120)], W / 2, 460, "center")
        E.frase(c, t, C["s24.b"], [("esquerda", "g", 140, COR), ("primeiro", "g", 140, COR)], W / 2, 690, "center", passo=0.12)
        E.frase(c, t, C["s24.b"] + 0.5, [("para", "i", 120), ("comparar", "i", 120)], W / 2, 820, "center")
    E.saida(c, t, C["s25"] - 0.1, resumo)
    if t < C["s25"]:
        return
    E.frase(c, t, C["s25.a"] - 1.0, [("próxima", "i", 84), ("aula", "i", 84)], XE, 270)
    E.frase(c, t, C["s25.a"], [("somar", "g", 120, COR), ("de", "g", 120, COR), ("cabeça", "g", 120, COR)], XE, 410, passo=0.12)
    E.frase(c, t, C["s25.a"] + 0.6, [("completando", "i", 84), ("dez", "i", 84)], XE, 510)
    E.frase(c, t, C["s25.b"], [("armar", "i", 84), ("a", "i", 84), ("conta", "i", 84), ("com", "i", 84), ("o", "i", 84), ("vai", "g", 84, COR), ("um", "g", 84, COR)], XE, 640, passo=0.12)
    E.foco(c, t, C["s25.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1450, 560, 76, estilo="g", cor=E.SOBRE, a=a))
    p = ease_io(prog(t, C["s25.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1760, 1580, p), lerp(800, 585, p), ep(t, C["s25.c"] + 0.2, 0.4))
    E.frase(c, t, C["s25.d"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 880, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, grupos=b_grupos, leitura=b_leitura, comparar=b_comparar, sinais=b_sinais,
              erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
