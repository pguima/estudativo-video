"""Visual — Estudativo · MAT-TRA-005: adição de arcos e arco duplo (sen 45° + sen 30° ≈ 1,2 > 1, impossível; sen(a + b) =
sen a cos b + sen b cos a; sen 75° = (√6 + √2)/4 ≈ 0,95; sen 2x = 2 sen x cos x, com 3/5 e 4/5 → 24/25; questão sen x = 5/13 →
cos x = 12/13 → sen 2x = 120/169).
Cores da trigonometria (MAT-TRI-001, 008, 010 e MAT-TRA-004): seno em âmbar (OPO), cosseno em petróleo (ADJ); o sinal do meio que
muda, em vermelho. A música "Minha terra tem palmeiras onde canta o sabiá" no palco escuro, verso a verso, cada um com a sua peça.
Resposta final na pílula; erro em vermelho, certo em verde.
Peças locais: ps(), cf(), cf_em(), resp(), lista(), larg_f().
Todo instante vem de C[...] (marcadores do roteiro), para acompanhar a voz real quando ela chegar."""
import math
from fractions import Fraction as F
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Trigonometria Avançada")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-TRA-005_adicao_de_arcos_e_arco_duplo.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("formula", "conta", "duplo", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
OPO, ADJ, TG = "#D98A00", "#0E9AA7", "#C0187C"
OPO_ESC, ADJ_ESC, TG_ESC = "#F2B33D", "#3CC7D3", "#F062B5"
S = lambda g: math.sin(math.radians(g))
Cs = lambda g: math.cos(math.radians(g))
assert S(45) + S(30) > 1.2 and abs(S(45) * Cs(30) + S(30) * Cs(45) - (math.sqrt(6) + math.sqrt(2)) / 4) < 1e-12 and abs(S(75) - (math.sqrt(6) + math.sqrt(2)) / 4) < 1e-12
assert (2.4 + 1.4) / 4 == 0.95 and 2 * F(3, 5) * F(4, 5) == F(24, 25) and 1 - F(25, 169) == F(144, 169) == F(12, 13) ** 2
assert 2 * F(5, 13) * F(12, 13) == F(120, 169) and abs(S(180)) < 1e-12 and 2 * S(90) == 2


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças gerais ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def cf(c, partes, x, y, size, a=1.0, align="left", est="g"):
    ws = [E.formula(None, s, 0, 0, size, est, a=0) for s, _ in partes]
    xx = x - sum(ws) / 2 if align == "center" else x - sum(ws) if align == "right" else x
    if c is not None and a > 0:
        for (s, cor), wi in zip(partes, ws):
            E.formula(c, s, xx, y, size, est, cor, a)
            xx += wi
    return sum(ws)


def cf_em(c, t, t0, partes, x, y, size, align="left"):
    E.foco(c, t, t0, 0.5, lambda a: cf(c, partes, x, y, size, a, align))


def resp(c, t, t0, partes, cx, cy, size=64, alto=1.75, cor=None):
    if isinstance(partes, str):
        partes = [(partes, BR)]

    def f(a):
        w = cf(None, partes, 0, 0, size) + size * 1.1
        h = size * alto
        M.rrect(c, cx - w / 2, cy - h / 2, w, h, h / 2, cor or E.COR, a, shadow=True)
        cf(c, partes, cx, cy + size * 0.36, size, a, "center")
    E.foco(c, t, t0, 0.5, f)


def lista(c, t, itens, x, y0, dy=150, size=60):
    for i, (t0, partes) in enumerate(itens):
        y = y0 + i * dy
        E.foco(c, t, t0, 0.5, lambda a, i=i, y=y: (E.bola(c, x + 40, y - size * 0.36, 40, a=a),
                                                   centro(c, str(i + 1), x + 40, y - size * 0.36 + 18, 50, "g", BR, a)))
        E.frase(c, t, t0 + 0.1, partes, x + 110, y, "left", 0.1)


def larg_f(s, size):
    return E.formula(None, s, 0, 0, size, "g", a=0)


SOMA = [("sen(a + b)", TINTA), (" = ", TINTA), ("sen a", OPO), (" · ", TINTA), ("cos b", ADJ), (" + ", TINTA), ("sen b", OPO), (" · ", TINTA), ("cos a", ADJ)]
SUB = [("sen(a − b)", TINTA), (" = ", TINTA), ("sen a", OPO), (" · ", TINTA), ("cos b", ADJ), (" − ", ERRADO), ("sen b", OPO), (" · ", TINTA), ("cos a", ADJ)]
COSS = [("cos(a + b)", TINTA), (" = ", TINTA), ("cos a", ADJ), (" · ", TINTA), ("cos b", ADJ), (" − ", ERRADO), ("sen a", OPO), (" · ", TINTA), ("sen b", OPO)]


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    a1, b1, c1, d1 = (C[f"s01.{k}"] for k in "abcd")

    def um():
        cf_em(c, t, a1, [("sen 75° = ?", OPO)], W / 2, 330, 150, "center")
        cf_em(c, t, b1, [("sen 45° + sen 30°", TINTA)], W / 2, 560, 100, "center")
        cf_em(c, t, c1, [("= f{r{2}}{2} + f{1}{2} ≈ 0,7 + 0,5 = 1,2", ERRADO)], W / 2, 740, 84, "center")
        E.frase(c, t, d1, ps("o seno", "i", 66) + [("nunca passa de 1", "g", 72, COR)], W / 2, 930, "center", 0.1)
        E.foco(c, t, d1 + 0.6, 0.5, lambda a: E.selo(c, W / 2 + 560, 710, 50, False, a))
    E.saida(c, t, C["s02"] - 0.1, um)
    if t >= C["s02"]:
        ta, tb, tc = C["s02.a"], C["s02.b"], C["s02.c"]
        E.foco(c, t, tc - 0.2, 0.7, lambda a: E.bola(c, 1500, 560, 250 * ease_back(prog(t, tc - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, ps("até o fim desta aula", "i", 90), XE, 260, passo=0.14)
        E.frase(c, t, ta + 1.2, [("sen(a + b)", "g", 120, OPO)], XE, 440, "left", 0.14)
        E.frase(c, t, tb, ps("o", "i", 90) + [("arco duplo", "g", 110, COR)], XE, 630, "left", 0.12)
        E.foco(c, t, tc + 0.1, 0.5, lambda a: (centro(c, "+ atalho", 1500, 545, 80, "g", E.SOBRE, a),
                                               centro(c, "de prova", 1500, 630, 80, "i", E.SOBRE, a)))


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"] + 0.1, ps("você precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "3", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + E.larg("3", "g", 340) + 30, 700, 120, "i", TINTA, a))
    x, w = 900, 900
    itens = (("s03.b", "a tabela de", "30°, 45° e 60°"), ("s03.c", "multiplicar raízes:", "r{2} · r{3} = r{6}"),
             ("s03.d", "a relação fundamental:", "sen^2 x + cos^2 x = 1"))
    for i, (k, l1, l2) in enumerate(itens):
        y = 170 + i * 240
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 196, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 60)], x + 44, y + 84)
        E.foco(c, t, C[k] + 0.3, 0.5, lambda a, l2=l2, y=y: E.formula(c, l2, x + 44, y + 166, 62, "g", COR, a))
    E.frase(c, t, C["s03.end"] - 2.4, ps("faltou alguma?", "i", 58, COR) + ps("procure no canal", "i", 58), 900, 1000, "left", 0.12)


# ---------------- as fórmulas ----------------
def b_formula(c, t, C, b):
    a4, b4, c4 = (C[f"s04.{k}"] for k in "abc")
    a5, b5, c5 = (C[f"s05.{k}"] for k in "abc")
    cf_em(c, t, a4, [("sen(a + b) ≠ sen a + sen b", ERRADO)], W / 2, 200, 76, "center")
    sz, y1 = 84, 380
    x0 = W / 2 - cf(None, SOMA, 0, 0, sz) / 2
    w5 = cf(None, SOMA[:5], 0, 0, sz)
    E.foco(c, t, b4, 0.5, lambda a: cf(c, SOMA[:5], x0, y1, sz, a))
    E.foco(c, t, c4, 0.5, lambda a: cf(c, SOMA[5:], x0 + w5, y1, sz, a))
    E.foco(c, t, a5, 0.5, lambda a: cf(c, SUB, x0, y1 + 170, sz, a))
    E.foco(c, t, a5 + 0.4, 0.5, lambda a: E.escreve(c, "só o sinal do meio muda", x0, y1 + 250, 48, "i", TINTA2, a))
    E.foco(c, t, b5, 0.5, lambda a: cf(c, COSS, x0, y1 + 420, sz, a))
    E.foco(c, t, c5, 0.5, lambda a: E.pilula(c, "no cosseno, o sinal do meio é o contrário", W / 2, y1 + 560, 50, "g", fundo=ERRADO, a=a))


# ---------------- seno de 75 ----------------
def b_conta(c, t, C, b):
    a6, b6, c6, d6 = (C[f"s06.{k}"] for k in "abcd")
    a7, b7, c7, d7 = (C[f"s07.{k}"] for k in "abcd")
    a8, b8, c8 = (C[f"s08.{k}"] for k in "abc")

    def contas():
        cf_em(c, t, a6, [("sen 75° = sen(45° + 30°)", TINTA)], XE, 190, 80)
        cf_em(c, t, b6, [("sen 45°", OPO), (" · ", TINTA), ("cos 30°", ADJ), (" = f{r{2}}{2} · f{r{3}}{2}", TINTA)], XE, 360, 76)
        E.foco(c, t, c6, 0.5, lambda a: E.formula(c, "em cima: r{2} · r{3} = r{6}", XE + 120, 470, 46, "b", TINTA2, a))
        E.foco(c, t, d6, 0.5, lambda a: E.formula(c, "embaixo: 2 · 2 = 4", XE + 700, 470, 46, "b", TINTA2, a))
        cf_em(c, t, d6 + 0.6, [("= f{r{6}}{4}", OPO)], 1500, 360, 80)
        cf_em(c, t, a7, [("sen 30°", OPO), (" · ", TINTA), ("cos 45°", ADJ), (" = f{1}{2} · f{r{2}}{2}", TINTA)], XE, 610, 76)
        cf_em(c, t, b7, [("= f{r{2}}{4}", OPO)], 1500, 610, 80)
        E.foco(c, t, c7, 0.5, lambda a: E.pilula(c, "quartos com quartos: junte em cima", W / 2, 760, 48, "g", a=a, cor=E.SOBRE))
        resp(c, t, d7, [("sen 75° = f{r{6} + r{2}}{4}", BR)], W / 2, 920, 76, 2.3, cor=OPO)
    E.saida(c, t, a8 - 0.1, contas)
    if t < a8 - 0.1:
        return
    resp(c, t, a8 - 0.1, [("sen 75° = f{r{6} + r{2}}{4}", BR)], W / 2, 240, 76, 2.3, cor=OPO)
    cf_em(c, t, a8, [("r{6} + r{2} ≠ r{8}", ERRADO)], W / 2, 470, 84, "center")
    cf_em(c, t, b8, [("≈ f{2,4 + 1,4}{4} = f{3,8}{4} = 0,95", TINTA)], W / 2, 660, 84, "center")
    E.frase(c, t, c8, ps("quase 1, mas menor:", "i", 62) + [("75° está perto de 90°", "g", 66, CERTO)], W / 2, 880, "center", 0.1)


# ---------------- arco duplo ----------------
def b_duplo(c, t, C, b):
    a9, b9, c9, d9 = (C[f"s09.{k}"] for k in "abcd")
    a0, b0, c0, d0, e0 = (C[f"s10.{k}"] for k in "abcde")

    def nove():
        cf_em(c, t, a9, [("2x = x + x", TINTA)], W / 2, 220, 100, "center")
        cf_em(c, t, b9, [("sen x", OPO), (" · ", TINTA), ("cos x", ADJ), (" + ", TINTA), ("sen x", OPO), (" · ", TINTA), ("cos x", ADJ)], W / 2, 430, 90, "center")
        E.foco(c, t, c9, 0.5, lambda a: E.escreve(c, "duas vezes a mesma coisa", W / 2 - 330, 540, 52, "i", TINTA2, a))
        resp(c, t, d9, [("sen 2x = 2 · ", BR), ("sen x", BR), (" · ", BR), ("cos x", BR)], W / 2, 750, 84, 1.7, cor=COR)
    E.saida(c, t, C["s10"] - 0.1, nove)
    if t < C["s10"] - 0.1:
        return
    resp(c, t, C["s10"] - 0.1, [("sen 2x = 2 · sen x · cos x", BR)], W / 2, 180, 64, 1.7, cor=COR)
    cf_em(c, t, a0, [("sen x = f{3}{5}", OPO), ("     ", TINTA), ("cos x = f{4}{5}", ADJ)], W / 2, 380, 84, "center")
    cf_em(c, t, b0, [("sen 2x = 2 · f{3}{5} · f{4}{5}", TINTA)], W / 2, 560, 84, "center")
    cf_em(c, t, c0, [("= f{2 · 3 · 4}{5 · 5}", TINTA2)], W / 2 - 200, 740, 76, "center")
    cf_em(c, t, d0, [("= f{24}{25}", OPO)], W / 2 + 200, 740, 84, "center")
    cf_em(c, t, e0, [("cos 2x = ", TINTA), ("cos^2 x", ADJ), (" − ", TINTA), ("sen^2 x", OPO)], W / 2, 940, 72, "center")


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    a1, b1, c1, d1, e1 = (C[f"s11.{k}"] for k in "abcde")
    E.frase(c, t, a1, ps("o erro:", "i", 62) + [("abrir o seno como parêntese", "g", 66, ERRADO)], W / 2, 190, "center", 0.1)
    cf_em(c, t, b1, [("sen(a + b) ≠ sen a + sen b", ERRADO)], W / 2, 380, 84, "center")
    cf_em(c, t, c1, [("sen 2x ≠ 2 · sen x", ERRADO)], W / 2, 540, 84, "center")
    E.frase(c, t, c1 + 1.2, ps("teste com", "i", 60) + [("x = 90°", "g", 64, COR)], W / 2, 690, "center", 0.1)
    cf_em(c, t, d1, [("sen 180° = 0", CERTO)], W / 2 - 360, 860, 80, "center")
    cf_em(c, t, e1, [("2 · sen 90° = 2", ERRADO)], W / 2 + 360, 860, 80, "center")
    E.foco(c, t, e1 + 0.6, 0.5, lambda a: E.formula(c, "≠", W / 2, 860, 90, "g", ERRADO, a, "center"))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    a2, b2, c2, d2 = (C[f"s12.{k}"] for k in "abcd")
    a3, b3, c3 = (C[f"s13.{k}"] for k in "abc")

    def doze():
        E.frase(c, t, C["s12"] + 0.1, ps("agora o atalho:", "i", 62, CLARO) + [("a música", "g", 70, BR)], W / 2, 170, "center", 0.1)
        versos = [("Minha terra", "sen a", OPO_ESC), ("tem palmeiras,", "cos b", ADJ_ESC), ("onde canta", "sen b", OPO_ESC), ("o sabiá", "cos a", ADJ_ESC)]
        for i, (v, f, cor) in enumerate(versos):
            x = 250 + i * 380
            ti = lerp(b2, c2, i / 4)
            E.foco(c, t, ti, 0.5, lambda a, v=v, x=x: E.escreve(c, v, x, 380, 62, "i", BR, a))
            tf = c2 + 0.5 * i
            E.foco(c, t, tf, 0.5, lambda a, f=f, x=x, cor=cor: E.formula(c, f, x + 40, 520, 86, "g", cor, a))
            if t >= tf:
                q = ep(t, tf, 0.4)
                M.arrow(c, x + 120, 410, x + 120, 450, CLARO, q, 4, 14, q)
        E.foco(c, t, c2 + 2.0, 0.5, lambda a: E.formula(c, "+", 250 + 380 * 2 - 70, 520, 86, "g", BR, a))
        E.foco(c, t, d2, 0.5, lambda a: cf(c, [("cosseno: ", CLARO), ("cos · cos", ADJ_ESC), (" e ", CLARO), ("sen · sen", OPO_ESC), (", sinal trocado", CLARO)],
                                           W / 2, 760, 64, a, "center"))
    E.saida(c, t, C["s13"] - 0.1, doze)
    if t < C["s13"] - 0.1:
        return
    E.frase(c, t, a3, ps("o ritmo guarda", "i", 66, CLARO) + [("a ordem das letras", "g", 72, BR)], W / 2, 330, "center", 0.1)
    E.frase(c, t, a3 + 1.4, ps("que importa na", "i", 60, CLARO) + [("subtração", "g", 66, BR)], W / 2, 440, "center", 0.1)
    E.frase(c, t, b3, ps("arco duplo:", "i", 64, CLARO) + [("sem música nova", "g", 70, BR)], W / 2, 640, "center", 0.1)
    E.foco(c, t, c3, 0.5, lambda a: E.pilula(c, "a = b = x", W / 2, 800, 64, "g", fundo=E.COR, a=a))


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    a4, b4, c4 = (C[f"s14.{k}"] for k in "abc")
    E.frase(c, t, C["s14"], ps("hora de testar", "i", 72, COR), XE, 170)
    cf_em(c, t, a4, [("sen x = f{5}{13}", OPO)], XE, 420, 120)
    E.frase(c, t, b4, ps("x no", "i", 64) + [("1º quadrante", "g", 70, COR)], XE, 600, "left", 0.1)
    cf_em(c, t, c4, [("sen 2x = ?", OPO)], XE, 790, 110)
    E.relogio(c, t, C["s15.a"], 1500, 440, 170)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    a6, b6, c6, d6 = (C[f"s16.{k}"] for k in "abcd")
    a7, b7, c7, d7 = (C[f"s17.{k}"] for k in "abcd")
    E.frase(c, t, C["s16"] + 0.1, ps("primeiro, o cosseno", "i", 62, COR), XE, 170, "left", 0.1)
    cf_em(c, t, a6, [("sen^2 x = f{25}{169}", OPO)], XE, 320, 72)
    cf_em(c, t, b6, [("cos^2 x = f{169}{169} − f{25}{169}", ADJ)], XE, 480, 72)
    cf_em(c, t, c6, [("= f{144}{169}", ADJ)], XE + 230, 630, 72)
    resp(c, t, d6, [("cos x = f{12}{13}", BR)], 380, 830, 66, 2.3, cor=ADJ)
    X = 1380
    cf_em(c, t, a7, [("sen 2x = 2 · f{5}{13} · f{12}{13}", TINTA)], X, 360, 72, "center")
    cf_em(c, t, b7, [("em cima: 2 · 5 · 12 = 120", TINTA2)], X, 520, 56, "center")
    cf_em(c, t, c7, [("embaixo: 13 · 13 = 169", TINTA2)], X, 620, 56, "center")
    resp(c, t, d7, [("sen 2x = f{120}{169}", BR)], X, 820, 72, 2.3, cor=OPO)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s18"] + 0.1, [("resumindo", "i", 92, COR)], W / 2, 190, "center")
        E.foco(c, t, C["s18.a"], 0.5, lambda a: cf(c, SOMA, W / 2, 380, 72, a, "center"))
        E.foco(c, t, C["s18.b"], 0.5, lambda a: cf(c, COSS, W / 2, 560, 72, a, "center"))
        E.foco(c, t, C["s18.c"], 0.5, lambda a: cf(c, [("sen 2x = 2 · ", TINTA), ("sen x", OPO), (" · ", TINTA), ("cos x", ADJ)], W / 2, 760, 84, a, "center"))
    E.saida(c, t, C["s19"] - 0.1, resumo)
    if t < C["s19"] - 0.1:
        return
    a9, b9, c9, d9 = (C[f"s19.{k}"] for k in "abcd")
    E.frase(c, t, C["s19"], ps("na próxima aula, o caminho inverso", "i", 66), XE, 210, "left", 0.1)
    cf_em(c, t, a9, [("sen x = f{1}{2}", OPO), ("   x = ?", TINTA)], XE, 420, 110)
    cf_em(c, t, b9, [("sen x > f{1}{2}", OPO), ("  onde?", TINTA)], XE, 640, 96)
    E.foco(c, t, c9, 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 400, 76, estilo="g", a=a, cor=E.SOBRE))
    p = ease_io(prog(t, c9 + 0.3, 0.8))
    E.cursor(c, lerp(1850, 1650, p), lerp(640, 425, p), ep(t, c9 + 0.2, 0.4))
    E.frase(c, t, d9, [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 940, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, formula=b_formula, conta=b_conta, duplo=b_duplo, erro=b_erro, atalho=b_atalho,
              questao=b_questao, resposta=b_resposta, fim=b_fim)
