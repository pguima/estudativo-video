"""Visual — Estudativo · MAT-CNT-019: praticando probabilidade (4 situações).
Mesma linguagem das práticas da trilha (MAT-CNT-010): decisao() com a faixa das ferramentas no alto, que acende a escolhida;
enunciado() com "situação n" na esfera e o relógio de pausa. Peças das aulas 011 a 018: pessoa() (005/015), cartao() da MAT-CNT-013,
bolinha() da MAT-CNT-014, gene() e E.arvore com fração nos galhos da MAT-CNT-018, linha() com contas e frações numa linha (013).
Sem voz ainda: todo instante vem de C[...] (cenas e marcadores), nunca de segundos fixos."""
import math
from fractions import Fraction as Fr
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Contagem e Probabilidade")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-CNT-019_praticando_probabilidade.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("lembrete", "questao1", "atalho", "questao2", "questao3", "questao4", "fim"))
BR = "#FFFFFF"
AMBAR = "#E8920C"
OPCOES = ("conto", "complementar", "somo", "multiplico", "novo total")
assert 7 * 6 == 42 and 42 // 2 == 21 and 3 * 2 == 6 and 6 // 2 == 3 and Fr(3, 21) == Fr(1, 7) == Fr(3, 7) * Fr(2, 6) and Fr(6, 42) == Fr(1, 7)
assert Fr(3, 4) ** 3 == Fr(27, 64) and 64 - 27 == 37 and Fr(1, 2) < Fr(37, 64) < Fr(3, 5)
M4 = [n for n in range(1, 51) if n % 4 == 0]
M6 = [n for n in range(1, 51) if n % 6 == 0]
AMBOS = [n for n in M4 if n in M6]
assert len(M4) == 12 and len(M6) == 8 and AMBOS == [12, 24, 36, 48] == [n for n in range(1, 51) if n % 12 == 0]
assert 12 + 8 == 20 and 20 - 4 == 16 and Fr(16, 50) * 100 == 32 and [n for n in range(1, 51) if n % 24 == 0] == [24, 48]
assert 1 * Fr(1, 2) == Fr(1, 2) and Fr(1, 2) * Fr(1, 2) == Fr(1, 4)


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças da trilha ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    """uma frase, palavra a palavra, no mesmo estilo"""
    return [(w, est, size, cor) for w in txt.split()]


def igual_bola(c, t, t0, x, y, txt, r=120, size=None, cor=None, escuro=False, t_igual=None):
    """'=' em x e o resultado numa esfera à direita; y = centro. Devolve o centro da esfera."""
    size = size or r * (0.72 if len(txt) <= 2 else 0.56 if len(txt) == 3 else 0.46 if len(txt) == 4 else 0.38)
    E.sinal(c, t, t0 - 0.2 if t_igual is None else t_igual, "=", x, y, r * 0.75, BR if escuro else TINTA)
    bx = x + r * 0.55 + r
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, bx, y, r, cor, a), centro(c, txt, bx, y + size * 0.36, size, "g", E.SOBRE, a)))
    return bx


def nota(c, t, t0, x, y, txt, size=46, cor=TINTA2, estilo="b"):
    E.foco(c, t, t0, 0.45, lambda a: centro(c, txt, x, y, size, estilo, cor, a))


def larg_parte(p, size):
    return E.larg(p, "g", size) if isinstance(p, str) else max(E.larg(str(p[0]), "g", size), E.larg(str(p[1]), "g", size)) + size * 0.2


def linha(c, t, x, y, size, partes, align="left", gap=None):
    """conta numa linha: partes = [(texto ou (n, d), instante[, cor])]; y = altura da barra das frações. Devolve o x de cada parte e o fim"""
    gap = size * 0.28 if gap is None else gap
    ws = [larg_parte(p[0], size) for p in partes]
    tot = sum(ws) + gap * (len(partes) - 1)
    xx = x - tot / 2 if align == "center" else x - tot if align == "right" else x
    xs = []
    for (p, t0, *cor), w in zip(partes, ws):
        cor = cor[0] if cor else TINTA
        xs.append(xx)
        if isinstance(p, str):
            E.foco(c, t, t0, 0.45, lambda a, p=p, xx=xx, cor=cor: E.escreve(c, p, xx, y + size * 0.34, size, "g", cor, a))
        else:
            E.fr(c, t, t0, p[0], p[1], xx + w / 2, y, size, cor)
        xx += w + gap
    return xs, xx - gap


def pessoa(c, cx, cy, h, cor, a=1.0, mulher=False):
    """boneco simples (MAT-CNT-005 / 015): a mulher tem o tronco em saia"""
    if a <= 0:
        return
    c.drawCircle(cx, cy - h * 0.36, h * 0.17, M.paint(cor, a))
    if mulher:
        pa = skia.Path()
        pa.moveTo(cx - h * 0.16, cy - h * 0.14); pa.lineTo(cx + h * 0.16, cy - h * 0.14)
        pa.lineTo(cx + h * 0.3, cy + h * 0.38); pa.lineTo(cx - h * 0.3, cy + h * 0.38); pa.close()
        c.drawPath(pa, M.paint(cor, a))
    else:
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - h * 0.25, cy - h * 0.14, h * 0.5, h * 0.52), h * 0.2, h * 0.2), M.paint(cor, a))


def gene(c, cx, cy, letra, size=60, a=1.0):
    """a versão do gene numa pílula (MAT-CNT-018): A dominante (cor da matéria), a recessiva (âmbar)"""
    E.pilula(c, letra, cx, cy, size, estilo="g", fundo=E.COR if letra == "A" else AMBAR, a=a)


def bolinha(c, cx, cy, r, n, a=1.0, cor=None, anel=None):
    """bolinha numerada da urna (MAT-CNT-014)"""
    if a <= 0:
        return
    c.drawCircle(cx, cy, r, M.paint(cor or BR, a))
    c.drawCircle(cx, cy, r, M.paint(anel or TINTA2, a, stroke=8 if anel else 3))
    centro(c, str(n), cx, cy + r * 0.3, r * 0.8, "g", BR if cor else TINTA, a)


def cartao(c, t, t0, x, y, nome, terr=None, n=4, w=420):
    """questão de prova com n alternativas e só uma certa (MAT-CNT-013); terr = instante em que as erradas ficam vermelhas"""
    def f(a):
        r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, 180), 22, 22)
        c.drawRRect(r, M.paint(BR, a))
        c.drawRRect(r, M.paint(TINTA, a, stroke=4))
        E.escreve(c, nome, x + 24, y + 52, 40, "b", TINTA2, a)
    E.foco(c, t, t0, 0.45, f)
    for i, L in enumerate("ABCD"[:n]):
        cx, cy = x + 70 + i * 95, y + 118
        q = ep(t, terr, 0.4) if terr is not None else 0

        def letra(a, cx=cx, cy=cy, L=L, i=i, q=q):
            cor = CERTO if i == 1 else ERRADO
            c.drawCircle(cx, cy, 36, M.paint(M.mix(BR, cor, 0.85 * q) if q > 0 else BR, a))
            c.drawCircle(cx, cy, 36, M.paint(M.mix(TINTA, cor, q), a, stroke=4))
            centro(c, L, cx, cy + 14, 40, "g", BR if q > 0.5 else TINTA, a)
        E.foco(c, t, t0 + 0.15 + 0.05 * i, 0.4, letra)


# ---------------- peças das práticas (MAT-CNT-010) ----------------
def decisao(c, t, t0, escolha=None, te=None, n=None):
    """faixa do alto: o número da situação à esquerda e as ferramentas à direita; em te a escolhida acende"""
    if n is not None:
        E.foco(c, t, t0, 0.4, lambda a: E.pilula(c, f"situação {n}", XE + 130, 105, 40, estilo="g", fundo=TINTA2, a=a))
    xs = (700, 930, 1170, 1400, 1650)
    for i, (op, x) in enumerate(zip(OPCOES, xs)):
        q = ep(t, te, 0.4) if (te is not None and escolha is not None) else 0.0
        if op == escolha:
            fundo, alfa = M.mix(TINTA2, E.COR, q), 1.0
        else:
            fundo, alfa = TINTA2, 1 - 0.65 * q
        E.foco(c, t, t0 + 0.08 * i, 0.4, lambda a, op=op, x=x, fundo=fundo, alfa=alfa: E.pilula(c, op, x, 105, 34, estilo="b", fundo=fundo, a=a * alfa))


def enunciado(c, t, C, k, n, linhas, relogio):
    """tela de pergunta: 'situação n' grande e o texto em linhas [(t0, partes)], relógio de pausa à direita"""
    E.frase(c, t, C[k + ".a"], [("situação", "i", 80, COR)], XE, 250)
    E.foco(c, t, C[k + ".a"] + 0.3, 0.5, lambda a: (E.bola(c, XE + 370, 222, 60, a=a), centro(c, str(n), XE + 370, 247, 72, "g", BR, a)))
    for i, (t0, partes) in enumerate(linhas):
        E.frase(c, t, t0, partes, XE, 420 + i * 120, passo=0.12)
    E.relogio(c, t, relogio, 1500, 600, 190)


def xs_pilulas(size, gap=40):
    """centros das pílulas das ferramentas, numa linha centrada, com o mesmo espaço entre elas"""
    ws = [E.larg(op, "g", size) + size * 1.1 for op in OPCOES]
    x = W / 2 - (sum(ws) + gap * (len(ws) - 1)) / 2
    out = []
    for w in ws:
        out.append(x + w / 2)
        x += w + gap
    return out


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    E.frase(c, t, C["s01.a"], [("4", "g", 140, COR), ("situações", "g", 140)], W / 2, 270, "center")
    E.frase(c, t, C["s01.a"] + 1.0, ps("criadas para esta aula", "i", 64, TINTA2), W / 2, 380, "center", passo=0.12)
    E.frase(c, t, C["s01.b"], [("o", "i", 66), ("difícil", "i", 66), ("é", "i", 66), ("escolher", "i", 66), ("a", "i", 66), ("ferramenta", "g", 72, COR)],
            W / 2, 500, "center", passo=0.1)
    for i, (op, x) in enumerate(zip(OPCOES, xs_pilulas(48))):
        E.foco(c, t, C["s01.b"] + 0.8 + 0.2 * i, 0.4, lambda a, op=op, x=x: E.pilula(c, op, x, 630, 48, estilo="g", a=a))
    E.relogio(c, t, C["s01.c"], W / 2, 850, 90)


# ---------------- lembrete: o guia ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s02"] + 0.1, [("a", "i", 76), ("palavra", "i", 76), ("da", "i", 76), ("pergunta", "i", 76), ("é", "i", 76), ("a", "i", 76),
                                   ("pista", "g", 82, COR)], W / 2, 170, "center", passo=0.1)
    linhas = (("s02.a", "pelo menos um?", "complementar", "1 − P(nenhum)"), ("s02.b", "a palavra “ou”?", "somo", "e tiro o comum"),
              ("s02.c", "“e”, em sequência?", "multiplico", "as chances"), ("s02.d", "sabendo que?", "novo total", "a pista"))
    tn = lerp(C["s02.d"], C["s02.end"], 0.3)
    for i, (k, perg, op, dica) in enumerate(linhas + ((None, "nenhuma dessas?", "conto", "favoráveis ÷ possíveis"),)):
        y = 310 + i * 135
        tk = C[k] if k else tn
        E.frase(c, t, tk, ps(perg, "i", 56), XE, y + 20, passo=0.08)
        E.foco(c, t, tk + 0.4, 0.45, lambda a, op=op, y=y: E.pilula(c, op, 1050, y, 46, estilo="g", a=a))
        E.foco(c, t, tk + 0.7, 0.45, lambda a, dica=dica, y=y: E.escreve(c, dica, 1290, y + 17, 48, "b", TINTA2, a))
    E.frase(c, t, lerp(C["s02.d"], C["s02.end"], 0.75), ps("travou? procure a aula no canal", "i", 50, TINTA2), W / 2, 1020, "center", passo=0.1)


# ---------------- situação 1 ----------------
def b_questao1(c, t, C, b):
    enunciado(c, t, C, "s03", 1, [(C["s03.b"], [("4", "g", 80, COR), ("homens", "i", 72), ("e", "i", 72), ("3", "g", 80, COR), ("mulheres", "i", 72)]),
                                  (C["s03.c"], ps("2 sorteadas para uma comissão", "i", 72)),
                                  (C["s03.d"], [("chance", "i", 72), ("de", "i", 72), ("ambas", "g", 80, COR), ("mulheres?", "g", 80, COR)])], C["s04.a"])


def grupo(c, t, t0, cx, y, h, passo, tm=None):
    """4 homens e 3 mulheres; em tm as mulheres acendem"""
    for k in range(7):
        mulher = k >= 4
        x = cx + (k - 3) * passo
        cor = E.COR if (mulher and tm is not None and t >= tm) else TINTA
        E.foco(c, t, t0 + 0.06 * k, 0.4, lambda a, x=x, mulher=mulher, cor=cor: pessoa(c, x, y, h, cor, a, mulher))


def b_resposta1(c, t, C, b):
    decisao(c, t, C["s05"], "conto", C["s05"] + 1.0, n=1)
    grupo(c, t, C["s05"] + 0.3, W / 2, 300, 150, 120, tm=C["s05.d"])
    E.foco(c, t, C["s05.a"], 0.5, lambda a: E.pilula(c, "a ordem não importa: combinação", W / 2, 440, 46, estilo="g", fundo=TINTA2, a=a))
    linha(c, t, 220, 580, 76, [("possíveis:", C["s05.b"] - 0.3), ("7 × 6 = 42", C["s05.b"]), ("÷ 2 = 21", C["s05.c"], COR)])
    linha(c, t, 220, 720, 76, [("favoráveis:", C["s05.d"] - 0.3), ("3 × 2 = 6", C["s05.d"]), ("÷ 2 = 3", C["s05.e"], COR)])
    xs, xf = linha(c, t, 220, 900, 100, [("P =", C["s05.f"]), ((3, 21), C["s05.f"] + 0.2)])
    E.pontes(c, t, xf + 15, xf + 175, 900, 100, "÷ 3", C["s05.g"] - 0.6, C["s05.g"] - 0.3, size=36)
    E.resultado(c, t, C["s05.g"], 1, 7, xf + 290, 900, 90, 100, CERTO)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def sem():
        E.frase(c, t, C["s06.a"], [("trate", "i", 74, CLARO), ("como", "i", 74, CLARO), ("sorteio", "g", 80, BR), ("sem", "g", 80, BR), ("reposição", "g", 80, BR)],
                W / 2, 200, "center", passo=0.12)
        linha(c, t, 320, 420, 90, [("1ª mulher:", C["s06.b"], CLARO), ((3, 7), C["s06.b"] + 0.3, BR)])
        linha(c, t, 1020, 420, 90, [("2ª mulher:", C["s06.c"], CLARO), ((2, 6), C["s06.c"] + 0.3, BR)])
        xs, xf = linha(c, t, W / 2, 680, 100, [((3, 7), C["s06.d"], BR), ("×", C["s06.d"] + 0.3, CLARO), ((2, 6), C["s06.d"] + 0.5, BR), ("=", C["s06.d"] + 1.0, CLARO),
                                               ((6, 42), C["s06.d"] + 1.2, BR), ("=", C["s06.d"] + 2.2, CLARO), ((1, 7), C["s06.d"] + 2.4, CLARO)], "center")
        E.foco(c, t, C["s06.e"], 0.5, lambda a: E.pilula(c, "2 de uma vez = sem reposição", W / 2, 920, 54, estilo="g", fundo=E.COR, a=a))
    E.saida(c, t, C["s07"] - 0.1, sem)
    if t < C["s07"]:
        return
    E.foco(c, t, C["s07.a"], 0.5, lambda a: E.pilula(c, "não compensa quando a pergunta mistura", W / 2, 190, 52, estilo="g", fundo=ERRADO, a=a))
    E.frase(c, t, C["s07.b"], [("1", "g", 80, BR), ("homem", "i", 74, CLARO), ("e", "i", 74, CLARO), ("1", "g", 80, BR), ("mulher", "i", 74, CLARO)],
            W / 2, 360, "center", passo=0.12)
    # dois caminhos na árvore
    raiz = (520, 680)
    cam = (((900, 560, "homem"), (1300, 560, "mulher")), ((900, 800, "mulher"), (1300, 800, "homem")))
    q = ease_io(prog(t, C["s07.c"], 0.6))
    if q > 0:
        c.drawCircle(*raiz, 10, M.paint(BR))
        for (a1, a2) in cam:
            M.line(c, raiz[0] + 14, raiz[1], lerp(raiz[0] + 14, a1[0] - 110, q), lerp(raiz[1], a1[1], q), BR, 1, 6)
            q2 = ease_io(prog(t, C["s07.c"] + 0.4, 0.5))
            if q2 > 0:
                M.line(c, a1[0] + 110, a1[1], lerp(a1[0] + 110, a2[0] - 110, q2), a2[1], BR, 1, 6)
    for k, (a1, a2) in enumerate(cam):
        E.foco(c, t, C["s07.c"] + 0.3, 0.4, lambda a, a1=a1: centro(c, a1[2], a1[0], a1[1] + 18, 50, "g", BR, a))
        E.foco(c, t, C["s07.c"] + 0.7, 0.4, lambda a, a2=a2: centro(c, a2[2], a2[0], a2[1] + 18, 50, "g", BR, a))
    nota(c, t, C["s07.c"] + 1.0, 1640, 690, "2 caminhos", 56, CLARO, "i")
    E.foco(c, t, C["s07.d"], 0.5, lambda a: E.pilula(c, "esqueceu um? erra pela metade", W / 2, 990, 50, estilo="g", fundo=ERRADO, a=a))


# ---------------- situação 2 ----------------
def b_questao2(c, t, C, b):
    enunciado(c, t, C, "s08", 2, [(C["s08.b"], [("chuta", "i", 72), ("3", "g", 80, COR), ("questões", "i", 72)]),
                                  (C["s08.c"], [("4", "g", 80, COR), ("alternativas,", "i", 72), ("só", "i", 72), ("1", "g", 80), ("certa", "i", 72)]),
                                  (C["s08.d"], [("chance", "i", 72), ("de", "i", 72), ("acertar", "i", 72)]),
                                  (C["s08.d"] + 0.6, [("pelo", "g", 80, COR), ("menos", "g", 80, COR), ("uma?", "g", 80, COR)])], C["s09.a"])


def b_resposta2(c, t, C, b):
    decisao(c, t, C["s10"], "complementar", C["s10"] + 1.0, n=2)
    for k in range(3):
        cartao(c, t, C["s10"] + 0.3 + 0.15 * k, 200 + k * 520, 200, f"questão {k + 1}", C["s10.b"] + 0.2 * k)

    def nenhum():
        E.foco(c, t, C["s10.a"], 0.5, lambda a: E.pilula(c, "calcule o nenhum", W / 2, 470, 50, estilo="g", fundo=TINTA2, a=a))
        linha(c, t, 260, 640, 90, [("errar uma:", C["s10.b"]), ((3, 4), C["s10.b"] + 0.3, ERRADO)])
        E.formula_em(c, t, C["s10.c"], "errar as 3: (f{3}{4})^3 =", 260, 880, 84, "g", TINTA)
        wp = E.formula(None, "errar as 3: (f{3}{4})^3 =", 0, 0, 84, "g", a=0)
        E.foco(c, t, C["s10.c"] + 1.0, 0.45, lambda a: E.fracao(c, 27, 64, 260 + wp + 90, 850, 84, ERRADO, a))
    E.saida(c, t, C["s11"] - 0.1, nenhum)
    if t < C["s11"]:
        return
    E.foco(c, t, C["s11"] + 0.1, 0.45, lambda a: E.escreve(c, "tire do inteiro:", 260, 520, 56, "i", TINTA2, a))
    E.formula_em(c, t, C["s11.a"], "64 − 27 = 37", 700, 525, 84, "g", TINTA)
    xs, xf = linha(c, t, 260, 720, 100, [("P(pelo menos 1) =", C["s11.b"]), ((37, 64), C["s11.b"] + 0.3, CERTO)])
    E.foco(c, t, C["s11.c"], 0.5, lambda a: E.pilula(c, "pouco mais da metade", xf + 300, 720, 46, estilo="g", a=a))
    E.frase(c, t, C["s11.d"], ps("contar direto: 1, 2 ou 3 certas = 3 contas", "i", 52, TINTA2), 260, 950, passo=0.08)


# ---------------- situação 3 ----------------
def b_questao3(c, t, C, b):
    enunciado(c, t, C, "s12", 3, [(C["s12.b"], [("urna:", "i", 72), ("50", "g", 80, COR), ("bolinhas,", "i", 72), ("de", "i", 72), ("1", "g", 80),
                                                ("a", "i", 72), ("50", "g", 80)]),
                                  (C["s12.c"], [("chance", "i", 72), ("de", "i", 72), ("um", "i", 72), ("múltiplo", "g", 80)]),
                                  (C["s12.c"] + 1.0, [("de", "i", 72), ("4", "g", 80, COR), ("ou", "i", 72), ("de", "i", 72), ("6?", "g", 80, COR)])], C["s13.a"])


def b_resposta3(c, t, C, b):
    decisao(c, t, C["s14"], "somo", C["s14"] + 1.0, n=3)
    t4, t6, tamb = C["s14.b"], C["s14.c"], C["s14.d"]
    gx, gy, gp, gr = 170, 240, 76, 31
    for n in range(1, 51):
        i, j = (n - 1) // 10, (n - 1) % 10
        cx, cy = gx + j * gp, gy + i * gp
        cor = E.COR if (n % 4 == 0 and t >= t4 + 0.3) else None
        anel = AMBAR if (n % 6 == 0 and t >= t6 + 0.3) else None
        E.foco(c, t, C["s14"] + 0.3 + 0.01 * n, 0.35, lambda a, cx=cx, cy=cy, n=n, cor=cor, anel=anel: bolinha(c, cx, cy, gr, n, a, cor, anel), sobe=6)
    te = [C["s14.e"], lerp(C["s14.e"], C["s14.end"], 0.12), lerp(C["s14.e"], C["s14.end"], 0.33), lerp(C["s14.e"], C["s14.end"], 0.55)]
    for n, tk in zip(AMBOS, te):
        i, j = (n - 1) // 10, (n - 1) % 10
        if t >= tk:
            q = ep(t, tk, 0.4)
            E.caixa_pontilhada(c, gx + j * gp - 38, gy + i * gp - 38, 76, 76, q, ERRADO, q)
    XP = 1000

    def listas():
        E.foco(c, t, C["s14.a"], 0.5, lambda a: E.pilula(c, "some e tire a parte em comum", XP + 400, 280, 44, estilo="g", fundo=TINTA2, a=a))
        E.foco(c, t, t4, 0.45, lambda a: (E.bola(c, XP + 26, 420, 24, E.COR, a), E.escreve(c, "múltiplos de 4:", XP + 70, 440, 56, "i", TINTA, a),
                                          E.escreve(c, "12", XP + 480, 442, 68, "g", COR, a)))
        E.foco(c, t, t6, 0.45, lambda a: (c.drawCircle(XP + 26, 530, 24, M.paint(AMBAR, a, stroke=8)), E.escreve(c, "múltiplos de 6:", XP + 70, 550, 56, "i", TINTA, a),
                                          E.escreve(c, "8", XP + 480, 552, 68, "g", AMBAR, a)))
        E.foco(c, t, tamb, 0.45, lambda a: E.escreve(c, "dos dois: múltiplos do MMC = 12", XP + 70, 660, 50, "b", ERRADO, a))
        E.foco(c, t, te[0], 0.45, lambda a: E.escreve(c, "12, 24, 36, 48", XP + 70, 760, 64, "g", ERRADO, a))
    E.saida(c, t, C["s15"] - 0.1, listas)
    if t < C["s15"]:
        return
    E.formula_em(c, t, C["s15.a"], "12 + 8 = 20", XP, 420, 80, "g", TINTA)
    E.formula_em(c, t, C["s15.b"], "20 − 4 = 16", XP, 540, 80, "g", TINTA)
    xs, xf = linha(c, t, XP, 690, 90, [("P =", C["s15.c"]), ((16, 50), C["s15.c"] + 0.2, COR)])
    igual_bola(c, t, C["s15.d"], xf + 40, 690, "32%", r=90, cor=CERTO)
    E.foco(c, t, C["s15.e"], 0.5, lambda a: E.pilula(c, "armadilha: múltiplos do MMC = 12, não de 4 × 6 = 24", W / 2, 980, 48, estilo="g", fundo=ERRADO, a=a))


# ---------------- situação 4 ----------------
def b_questao4(c, t, C, b):
    E.frase(c, t, C["s16.a"], [("última:", "i", 80, COR), ("genética", "g", 84, COR)], XE, 220, passo=0.12)
    E.foco(c, t, C["s16.b"], 0.45, lambda a: E.escreve(c, "a característica só aparece com", XE, 360, 54, "i", TINTA, a))
    E.foco(c, t, C["s16.b"] + 0.8, 0.45, lambda a: (gene(c, XE + 40, 422, "a", 50, a), E.escreve(c, "do pai e", XE + 100, 440, 54, "i", TINTA, a),
                                                    gene(c, XE + 360, 422, "a", 50, a), E.escreve(c, "da mãe (recessiva)", XE + 420, 440, 54, "i", TINTA, a)))
    E.foco(c, t, C["s16.c"], 0.45, lambda a: (E.escreve(c, "mãe:", XE, 580, 64, "i", TINTA, a), gene(c, XE + 230, 558, "A", 54, a), gene(c, XE + 360, 558, "a", 54, a)))
    E.foco(c, t, C["s16.d"], 0.45, lambda a: (E.escreve(c, "pai:", XE, 700, 64, "i", TINTA, a), gene(c, XE + 230, 678, "a", 54, a), gene(c, XE + 360, 678, "a", 54, a),
                                              E.escreve(c, "mostra a característica", XE + 470, 698, 44, "b", TINTA2, a)))
    E.frase(c, t, C["s16.e"], [("1", "g", 70, COR), ("filho", "i", 64), ("com", "i", 64), ("ela?", "g", 70)], XE, 850, passo=0.1)
    E.frase(c, t, C["s16.f"], [("2", "g", 70, COR), ("filhos,", "i", 64), ("ambos?", "g", 70)], XE, 950, passo=0.1)
    E.relogio(c, t, C["s17.a"], 1560, 600, 180)


def b_resposta4(c, t, C, b):
    decisao(c, t, C["s18"], "multiplico", C["s18"] + 1.0, n=4)
    dest = (("a", "a"),) if t >= C["s18.c"] else ()
    pos = E.arvore(c, t, C["s18"] + 0.6, [("a",), ("A", "a")], 160, 230, 760, 520, ramos=[["1"], ["f{1}{2}", "f{1}{2}"]],
                   folha=lambda cam: "".join(cam), tn=[C["s18.a"], C["s18.b"]], tf=C["s18.b"] + 0.5, destaque=dest, size=56, size_ramo=44)
    nota(c, t, C["s18.a"], 330, 210, "pai passa", 44, TINTA2, "i")
    nota(c, t, C["s18.b"], 640, 210, "mãe passa", 44, TINTA2, "i")
    XP = 1080

    def um():
        linha(c, t, XP, 420, 96, [("1", C["s18.c"]), ("×", C["s18.c"] + 0.3), ((1, 2), C["s18.c"] + 0.5), ("=", C["s18.c"] + 0.9),
                                  ((1, 2), C["s18.c"] + 1.1, COR)])
        E.foco(c, t, C["s18.d"], 0.5, lambda a: E.pilula(c, "50%", XP + 250, 600, 72, estilo="g", fundo=CERTO, a=a))
    E.saida(c, t, C["s19"] - 0.1, um)
    if t < C["s19"]:
        return
    E.foco(c, t, C["s19.a"], 0.5, lambda a: E.pilula(c, "cada nascimento é independente", XP + 330, 380, 44, estilo="g", fundo=TINTA2, a=a))
    E.foco(c, t, C["s19.b"] - 0.2, 0.45, lambda a: E.escreve(c, "2 filhos:", XP, 540, 64, "g", TINTA, a))
    linha(c, t, XP, 680, 100, [((1, 2), C["s19.b"]), ("×", C["s19.b"] + 0.3), ((1, 2), C["s19.b"] + 0.5), ("=", C["s19.b"] + 0.9), ((1, 4), C["s19.b"] + 1.1, COR)])
    E.frase(c, t, C["s19.c"], ps("o 1º filho não muda a chance do 2º", "i", 54, TINTA2), 160, 900, passo=0.08)
    E.frase(c, t, lerp(C["s19.c"], C["s19.end"], 0.5), ps("como a moeda que não tem memória", "i", 54, COR), 160, 990, passo=0.08)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s20"], [("resumindo", "i", 92, COR)], W / 2, 190, "center")
        E.frase(c, t, C["s20.a"], ps("leia a palavra que manda na pergunta", "i", 66), W / 2, 400, "center", passo=0.1)
        E.frase(c, t, C["s20.b"], [("escolha", "g", 74, COR), ("a", "i", 66), ("ferramenta", "g", 74, COR), ("antes", "i", 66), ("da", "i", 66), ("conta", "i", 66)],
                W / 2, 540, "center", passo=0.1)
        for i, (op, x) in enumerate(zip(OPCOES, xs_pilulas(46))):
            E.foco(c, t, C["s20.b"] + 1.0 + 0.15 * i, 0.4, lambda a, op=op, x=x: E.pilula(c, op, x, 720, 46, estilo="g", a=a))
    E.saida(c, t, C["s21"] - 0.1, resumo)
    if t < C["s21"]:
        return
    E.foco(c, t, C["s21"] + 0.1, 0.5, lambda a: E.pilula(c, "trilha de contagem e probabilidade: concluída!", W / 2, 150, 46, estilo="g", fundo=CERTO, a=a))
    E.frase(c, t, C["s21.a"] - 0.4, ps("próxima trilha", "i", 76), XE, 330)
    E.frase(c, t, C["s21.a"], [("geometria", "g", 84, COR), ("analítica", "g", 84, COR)], XE, 450, passo=0.12)
    E.frase(c, t, C["s21.b"], ps("distância entre dois pontos", "i", 60), XE, 560, passo=0.08)
    A, B = (XE + 80, 900), (XE + 520, 650)
    if t >= C["s21.b"] + 0.5:
        q = ease_io(prog(t, C["s21.b"] + 0.5, 0.6))
        M.line(c, A[0], A[1], lerp(A[0], B[0], q), lerp(A[1], B[1], q), E.COR, 1, 8)
        for P_, nome in ((A, "A"), (B, "B")):
            c.drawCircle(*P_, 14, M.paint(TINTA))
    if t >= C["s21.c"]:
        q = ep(t, C["s21.c"], 0.6)
        p = M.paint(TINTA2, q, stroke=5)
        p.setPathEffect(skia.DashPathEffect.Make([12, 10], 0))
        pa = skia.Path(); pa.moveTo(*A); pa.lineTo(B[0], A[1]); pa.lineTo(*B)
        c.drawPath(pa, p)
        c.drawRect(skia.Rect.MakeXYWH(B[0] - 34, A[1] - 34, 34, 34), M.paint(TINTA2, q, stroke=4))
        E.foco(c, t, C["s21.c"] + 0.2, 0.4, lambda a: E.escreve(c, "triângulo retângulo", XE + 620, 800, 50, "b", TINTA2, a))
    E.foco(c, t, C["s21.d"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1560, 400, 76, estilo="g", a=a))
    p_ = ease_io(prog(t, C["s21.d"] + 0.3, 0.8))
    E.cursor(c, lerp(1850, 1690, p_), lerp(640, 425, p_), ep(t, C["s21.d"] + 0.2, 0.4))
    E.frase(c, t, C["s21.e"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], 1380, 980, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, questao1=b_questao1, resposta1=b_resposta1, atalho=b_atalho, questao2=b_questao2, resposta2=b_resposta2,
              questao3=b_questao3, resposta3=b_resposta3, questao4=b_questao4, resposta4=b_resposta4, fim=b_fim)
