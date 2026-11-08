"""Visual — Estudativo · MAT-TRA-004: secante, cossecante e identidades (sec = 1/cos, cossec = 1/sen, cotg = cos/sen;
tg² + 1 = sec²; tg = 3/4 → sec = 5/4 → cos = 4/5; (1 − cos²)/sen = sen; erro (sen + cos)/sen ≠ cos; tg · cossec = sec;
questão tg = 5/12 → sec = 13/12 → cos = 12/13).
Cores da trigonometria (MAT-TRI-001, 008 e 010): seno em âmbar (OPO), cosseno em petróleo (ADJ). Cada razão nova herda a cor do
seu par: secante, inverso do cosseno, em petróleo; cossecante, inverso do seno, em âmbar; tangente e cotangente em magenta (TG).
O par é ligado por uma seta curva com a pílula "inverso". Fator que se corta leva o risco vermelho; parcela que não se corta,
o selo de erro. Atalho no palco escuro. Resposta final na pílula.
Peças locais: ps(), cf(), cf_em(), resp(), lista(), carta() (cartão de uma razão), par_inv() (seta "inverso" entre duas cartas).
Todo instante vem de C[...] (marcadores do roteiro), para acompanhar a voz real quando ela chegar."""
import math
from fractions import Fraction as F
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Trigonometria Avançada")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-TRA-004_secante_cossecante_e_identidades.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("novas", "identidade", "simplificar", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
OPO, ADJ, TG = "#D98A00", "#0E9AA7", "#C0187C"
OPO_ESC, ADJ_ESC, TG_ESC = "#F2B33D", "#3CC7D3", "#F062B5"
assert F(4, 5) * F(5, 4) == 1 and 1 + F(3, 4) ** 2 == F(25, 16) == F(5, 4) ** 2 and 1 / F(5, 4) == F(4, 5)
assert 1 + F(5, 12) ** 2 == F(169, 144) == F(13, 12) ** 2 and 1 / F(13, 12) == F(12, 13) and (6 + 4) / 2 == 3 + 2
s45 = math.sqrt(2) / 2
assert abs((s45 + s45) / s45 - 2) < 1e-12 and abs(s45 - 2) > 1


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


def risco_em(c, t, t0, x, y, w, h=60, cor=ERRADO):
    """risco curto sobre um termo (fator que se corta)"""
    if t >= t0:
        E.risco(c, x - w / 2, y + h * 0.35, x + w / 2, y - h * 0.65, t, t0, cor, 8)


def larg_f(s, size):
    return E.formula(None, s, 0, 0, size, "g", a=0)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    a1, b1, c1 = (C[f"s01.{k}"] for k in "abc")

    def um():
        cf_em(c, t, a1, [("f{1 − cos^2 x}{sen x}", TINTA)], W / 2 - 260, 520, 170, "center")
        E.foco(c, t, b1, 0.5, lambda a: E.formula(c, "=", W / 2 + 60, 520, 170, "g", TINTA, a))
        resp(c, t, b1 + 0.2, [("sen x", BR)], W / 2 + 420, 470, 120, 1.5, cor=OPO)
        E.frase(c, t, c1, ps("quem conhece as", "i", 66) + [("identidades", "g", 72, COR)] + ps("vê de longe", "i", 66), W / 2, 860, "center", 0.1)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t >= C["s02"]:
        ta, tb, tc = C["s02.a"], C["s02.b"], C["s02.c"]
        E.foco(c, t, tc - 0.2, 0.7, lambda a: E.bola(c, 1500, 560, 250 * ease_back(prog(t, tc - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, ps("até o fim desta aula", "i", 90), XE, 260, passo=0.14)
        E.frase(c, t, ta + 1.2, [("sec,", "g", 110, ADJ), ("cossec,", "g", 110, OPO), ("cotg", "g", 110, TG)], XE, 440, "left", 0.14)
        E.frase(c, t, tb, ps("simplificar", "i", 84) + [("expressões", "g", 90, COR)], XE, 620, "left", 0.12)
        E.foco(c, t, tc + 0.1, 0.5, lambda a: (centro(c, "+ atalho", 1500, 545, 80, "g", E.SOBRE, a),
                                               centro(c, "de prova", 1500, 630, 80, "i", E.SOBRE, a)))


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"] + 0.1, ps("você precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "2", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + E.larg("2", "g", 340) + 30, 700, 120, "i", TINTA, a))
    x, w = 860, 960
    p = ep(t, C["s03.b"], 0.5)
    E.caixa_pontilhada(c, x, 170, w, 330, p, prog_=p)
    E.frase(c, t, C["s03.b"] + 0.1, [("a relação fundamental", "i", 56)], x + 44, 250)
    cf_em(c, t, C["s03.b"] + 0.4, [("sen^2 x", OPO), (" + ", TINTA), ("cos^2 x", ADJ), (" = 1", TINTA)], x + 44, 350, 70)
    cf_em(c, t, C["s03.b"] + 1.6, [("tg x", TG), (" = ", TINTA), ("f{sen x}{cos x}", TINTA)], x + 44, 450, 66)
    p = ep(t, C["s03.c"], 0.5)
    E.caixa_pontilhada(c, x, 560, w, 300, p, prog_=p)
    E.frase(c, t, C["s03.c"] + 0.1, [("só se corta fator", "i", 56)], x + 44, 640)
    cf_em(c, t, C["s03.c"] + 0.5, [("f{x · 3}{x} = 3", CERTO)], x + 44, 770, 70)
    cf_em(c, t, C["s03.c"] + 1.2, [("f{x + 3}{x} ≠ 3", ERRADO)], x + 500, 770, 70)
    E.frase(c, t, C["s03.end"] - 2.4, ps("faltou alguma?", "i", 58, COR) + ps("procure no canal", "i", 58), 860, 980, "left", 0.12)


# ---------------- as novas razões ----------------
def b_novas(c, t, C, b):
    a4, b4, c4, d4 = (C[f"s04.{k}"] for k in "abcd")
    a5, b5, c5, d5, e5 = (C[f"s05.{k}"] for k in "abcde")

    def quatro():
        E.frase(c, t, C["s04"] + 0.1, ps("três nomes novos", "i", 66, COR), XE, 170, "left", 0.1)
        cf_em(c, t, a4, [("sec x", ADJ), (" = ", TINTA), ("f{1}{cos x}", ADJ)], XE, 340, 92)
        cf_em(c, t, b4, [("cossec x", OPO), (" = ", TINTA), ("f{1}{sen x}", OPO)], XE, 540, 92)
        cf_em(c, t, c4, [("cotg x", TG), (" = ", TINTA), ("f{1}{tg x}", TG), (" = ", TINTA), ("f{cos x}{sen x}", TG)], XE, 740, 92)
        X = 1420
        E.foco(c, t, d4, 0.5, lambda a: E.pilula(c, "o “co” aparece uma vez em cada dupla", X, 300, 44, "g", a=a, cor=E.SOBRE))
        for i, (n1, n2, cor) in enumerate((("sec", "cos", ADJ), ("cossec", "sen", OPO), ("cotg", "tg", TG))):
            y = 470 + i * 150
            E.foco(c, t, d4 + 0.8 + 0.6 * i, 0.5, lambda a, n1=n1, n2=n2, cor=cor, y=y: (
                E.escreve(c, n1, X - 30 - E.larg(n1, "g", 80), y, 80, "g", cor, a),
                E.escreve(c, "com", X - 10, y, 64, "i", TINTA2, a),
                E.escreve(c, n2, X + 120, y, 80, "g", cor, a)))
    E.saida(c, t, a5 - 0.1, quatro)
    if t < a5 - 0.1:
        return
    E.frase(c, t, a5, ps("cada uma é o", "i", 66) + [("inverso", "g", 72, COR)] + ps("de outra", "i", 66), W / 2, 190, "center", 0.1)
    E.frase(c, t, a5 + 1.4, ps("multiplicado por ela, dá 1", "i", 56, TINTA2), W / 2, 280, "center", 0.1)
    cf_em(c, t, b5, [("cos x = f{4}{5}", ADJ)], 560, 480, 96, "center")
    if t >= c5:
        q = ep(t, c5, 0.5)
        M.arrow(c, 820, 450, 1080, 450, TINTA2, q, 5, 18, q)
    cf_em(c, t, c5, [("sec x = f{5}{4}", ADJ)], 1360, 480, 96, "center")
    E.foco(c, t, c5 + 0.4, 0.4, lambda a: E.escreve(c, "de ponta-cabeça", 860, 400, 44, "i", TINTA2, a))
    cf_em(c, t, d5, [("f{4}{5} · f{5}{4} = f{20}{20} = 1", CERTO)], W / 2, 690, 84, "center")
    cf_em(c, t, e5, [("90°: cos = 0  →  sec não existe", ERRADO)], W / 2, 900, 66, "center")


# ---------------- a identidade ----------------
def b_identidade(c, t, C, b):
    a6, b6, c6 = (C[f"s06.{k}"] for k in "abc")
    a7, b7, c7, d7, e7 = (C[f"s07.{k}"] for k in "abcde")
    X0, sz = W / 2 - 160, 96
    cf_em(c, t, a6, [("sen^2 x", OPO), (" + ", TINTA), ("cos^2 x", ADJ), (" = 1", TINTA)], X0, 220, sz, "center")
    E.foco(c, t, b6, 0.5, lambda a: E.pilula(c, "÷ cos² x dos dois lados", 1560, 330, 44, "g", a=a, cor=E.SOBRE))
    partes = [("f{sen^2 x}{cos^2 x}", OPO), (" + ", TINTA), ("f{cos^2 x}{cos^2 x}", ADJ), (" = ", TINTA), ("f{1}{cos^2 x}", TINTA)]
    cf_em(c, t, b6 + 0.6, partes, X0, 460, sz, "center")
    E.foco(c, t, c6, 0.5, lambda a: E.formula(c, "(6 + 4) ÷ 2 = 3 + 2", 1560, 430, 50, "g", TINTA2, a, "center"))
    # o que cada parcela vira, embaixo dela
    ws = [larg_f(s, sz) for s, _ in partes]
    x = X0 - sum(ws) / 2
    cx = []
    for w in ws:
        cx.append(x + w / 2)
        x += w
    for i, (k, s, cor) in enumerate(((a7, "tg^2 x", TG), (b7, "1", TINTA), (c7, "sec^2 x", ADJ))):
        j = (0, 2, 4)[i]
        q = ep(t, k, 0.4)
        if q > 0:
            M.arrow(c, cx[j], 560, cx[j], 620, TINTA2, q, 4, 14, q)
        E.foco(c, t, k, 0.5, lambda a, s=s, cor=cor, j=j: E.formula(c, s, cx[j], 700, 80, "g", cor, a, "center"))
    resp(c, t, d7, [("tg^2 x", BR), (" + 1 = ", BR), ("sec^2 x", BR)], X0, 850, 80, 1.6, cor=COR)
    cf_em(c, t, e7, [("1 + ", TINTA), ("cotg^2 x", TG), (" = ", TINTA), ("cossec^2 x", OPO)], X0, 1000, 64, "center")


# ---------------- usar a identidade ----------------
def b_usar(c, t, C, b):
    a8, b8, c8, d8, e8 = (C[f"s08.{k}"] for k in "abcde")
    a9, b9, c9 = (C[f"s09.{k}"] for k in "abc")
    E.frase(c, t, C["s08"] + 0.1, ps("para que serve?", "i", 66, COR), XE, 170, "left", 0.1)
    cf_em(c, t, a8, [("tg x = f{3}{4}", TG)], XE, 330, 90)
    E.foco(c, t, a8 + 0.6, 0.5, lambda a: E.escreve(c, "1º quadrante", XE + 430, 320, 54, "i", TINTA2, a))
    cf_em(c, t, b8, [("cos x = ?", ADJ)], XE, 480, 90)
    X = 1060
    cf_em(c, t, c8, [("tg^2 x = f{9}{16}", TG)], X, 330, 80)
    cf_em(c, t, d8, [("1 + f{9}{16} = 1f{9}{16}", TINTA)], X, 500, 80)
    cf_em(c, t, e8, [("= f{25}{16} = ", TINTA), ("sec^2 x", ADJ)], X + 200, 660, 80)
    cf_em(c, t, a9, [("f{5}{4} · f{5}{4} = f{25}{16}", TINTA2)], X, 820, 64)
    resp(c, t, b9, [("sec x = f{5}{4}", BR)], 520, 760, 72, 2.2, cor=ADJ)
    resp(c, t, c9, [("cos x = f{4}{5}", BR)], 520, 960, 72, 2.2, cor=ADJ)


# ---------------- simplificar ----------------
def b_simplificar(c, t, C, b):
    a0, b0, c0 = (C[f"s10.{k}"] for k in "abc")
    a1, b1, c1, d1 = (C[f"s11.{k}"] for k in "abcd")
    E.frase(c, t, C["s10"] + 0.1, ps("a expressão do começo", "i", 64, COR), XE, 170, "left", 0.1)
    cf_em(c, t, a0, [("f{1 − cos^2 x}{sen x}", TINTA)], XE + 60, 400, 120)
    E.foco(c, t, b0, 0.5, lambda a: cf(c, [("sen^2 x + cos^2 x = 1", TINTA2)], 1050, 270, 60, a))
    E.foco(c, t, b0 + 0.8, 0.5, lambda a: cf(c, [("− cos^2 x", ERRADO), (" dos dois lados", TINTA2)], 1050, 350, 50, a))
    cf_em(c, t, c0, [("1 − cos^2 x", TINTA), (" = ", TINTA), ("sen^2 x", OPO)], 1050, 460, 72)
    cf_em(c, t, a1, [("= ", TINTA), ("f{sen^2 x}{sen x}", OPO)], XE, 680, 110)
    y2 = 680
    x2 = XE + 520
    cf_em(c, t, b1, [("= ", TINTA), ("f{sen x · sen x}{sen x}", OPO)], x2, y2, 110)
    if t >= c1:  # corta um seno em cima e um embaixo
        w_eq = larg_f("= ", 110)
        wfr = larg_f("f{sen x · sen x}{sen x}", 110)
        wcima = larg_f("sen x · sen x", 110 * 0.78)
        x_fr = x2 + w_eq
        xc_top = x_fr + (wfr - wcima) / 2 + larg_f("sen x · ", 110 * 0.78) + larg_f("sen x", 110 * 0.78) / 2
        risco_em(c, t, c1, xc_top, y2 - 110 * 0.46, larg_f("sen x", 110 * 0.78) + 10, 70)
        risco_em(c, t, c1 + 0.3, x_fr + wfr / 2, y2 + 110 * 0.46, larg_f("sen x", 110 * 0.78) + 10, 70)
        E.foco(c, t, c1, 0.4, lambda a: E.escreve(c, "fator: corta", x2 + 120, y2 + 170, 48, "g", CERTO, a))
    resp(c, t, d1, [("sen x", BR)], 1560, 870, 96, 1.5, cor=OPO)
    E.foco(c, t, d1 + 0.8, 0.5, lambda a: E.formula(c, "se sen x ≠ 0", 1460, 1000, 46, "g", TINTA2, a))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    a2, b2, c2, d2, e2, f2 = (C[f"s12.{k}"] for k in "abcdef")
    E.frase(c, t, a2, ps("o erro:", "i", 62) + [("cortar parcela", "g", 70, ERRADO)], W / 2, 180, "center", 0.1)
    x, y, sz = 360, 420, 120
    cf_em(c, t, b2, [("f{sen x + cos x}{sen x}", TINTA)], x, y, sz)
    wfr = larg_f("f{sen x + cos x}{sen x}", sz)
    if t >= c2:
        s_ = sz * 0.78
        x_top = x + (wfr - larg_f("sen x + cos x", s_)) / 2 + larg_f("sen x", s_) / 2
        risco_em(c, t, c2, x_top, y - sz * 0.46, larg_f("sen x", s_) + 10, 70)
        risco_em(c, t, c2 + 0.3, x + wfr / 2, y + sz * 0.46, larg_f("sen x", s_) + 10, 70)
    E.foco(c, t, c2 + 0.5, 0.5, lambda a: E.formula(c, "= cos x ?", x + wfr + 30, y, sz, "g", ERRADO, a))
    E.frase(c, t, c2 + 1.6, ps("teste com 45°:", "i", 60) + [("sen = cos", "g", 64, COR)], x, 660, "left", 0.1)
    cf_em(c, t, d2, [("f{sen 45° + sen 45°}{sen 45°} = 2", TINTA)], x, 820, 84)
    cf_em(c, t, e2, [("cos 45° = f{r{2}}{2} ≠ 2", ERRADO)], 1180, 820, 72)
    E.foco(c, t, e2 + 0.5, 0.5, lambda a: E.selo(c, 1780, 790, 40, False, a))
    E.foco(c, t, f2, 0.5, lambda a: E.pilula(c, "parcela não se corta", W / 2, 990, 56, "g", fundo=ERRADO, a=a))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    a3, b3, c3, d3, e3, f3 = (C[f"s13.{k}"] for k in "abcdef")
    a4, b4, c4 = (C[f"s14.{k}"] for k in "abc")

    def treze():
        E.frase(c, t, C["s13"] + 0.1, ps("agora o atalho", "i", 62, CLARO), W / 2, 170, "center", 0.1)
        E.frase(c, t, a3, ps("travou?", "i", 66, CLARO) + [("tudo em seno e cosseno", "g", 72, BR)], W / 2, 290, "center", 0.1)
        cf_em(c, t, b3, [("tg x", TG_ESC), (" · ", BR), ("cossec x", OPO_ESC)], W / 2, 450, 96, "center")
        y, sz = 680, 110
        partes = [("f{sen x}{cos x}", BR), (" · ", BR), ("f{1}{sen x}", BR)]
        E.foco(c, t, c3, 0.5, lambda a: cf(c, partes[:1], 520, y, sz, a))
        E.foco(c, t, d3, 0.5, lambda a: cf(c, partes[1:], 520 + larg_f("f{sen x}{cos x}", sz), y, sz, a))
        if t >= e3:
            w1 = larg_f("f{sen x}{cos x}", sz)
            ws = larg_f("sen x", sz * 0.78)
            risco_em(c, t, e3, 520 + w1 / 2, y - sz * 0.46, ws + 10, 70)
            x3 = 520 + w1 + larg_f(" · ", sz)
            risco_em(c, t, e3 + 0.3, x3 + larg_f("f{1}{sen x}", sz) / 2, y + sz * 0.46, ws + 10, 70)
        E.foco(c, t, f3, 0.5, lambda a: cf(c, [(" = ", BR), ("f{1}{cos x}", ADJ_ESC), (" = ", BR), ("sec x", ADJ_ESC)],
                                            520 + larg_f("f{sen x}{cos x} · f{1}{sen x}", sz), y, sz, a))
    E.saida(c, t, C["s14"] - 0.1, treze)
    if t < C["s14"] - 0.1:
        return
    E.frase(c, t, a4, ps("as seis razões são feitas de", "i", 64, CLARO) + [("seno e cosseno", "g", 70, BR)], W / 2, 330, "center", 0.1)
    E.frase(c, t, b4, ps("identidade pronta?", "i", 64, CLARO) + [("troque direto", "g", 70, BR)], W / 2, 560, "center", 0.1)
    E.foco(c, t, c4, 0.5, lambda a: cf(c, [("1 + tg^2 x", TG_ESC), ("  →  ", CLARO), ("sec^2 x", ADJ_ESC)], W / 2, 760, 100, a, "center"))


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    a5, b5, c5 = (C[f"s15.{k}"] for k in "abc")
    E.frase(c, t, C["s15"], ps("hora de testar", "i", 72, COR), XE, 170)
    cf_em(c, t, a5, [("tg x = f{5}{12}", TG)], XE, 420, 120)
    E.frase(c, t, b5, ps("x no", "i", 64) + [("1º quadrante", "g", 70, COR)], XE, 600, "left", 0.1)
    cf_em(c, t, c5, [("sec x = ?", ADJ)], XE, 790, 96)
    cf_em(c, t, c5 + 0.6, [("cos x = ?", ADJ)], XE + 560, 790, 96)
    E.relogio(c, t, C["s16.a"], 1500, 440, 170)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    a7, b7, c7 = (C[f"s17.{k}"] for k in "abc")
    a8, b8, c8 = (C[f"s18.{k}"] for k in "abc")
    E.frase(c, t, C["s17"] + 0.1, ps("vamos lá", "i", 62, COR), XE, 170, "left", 0.1)
    cf_em(c, t, a7, [("tg^2 x = f{25}{144}", TG)], XE, 340, 80)
    cf_em(c, t, b7, [("1 + f{25}{144} = 1f{25}{144}", TINTA)], XE, 510, 80)
    cf_em(c, t, c7, [("= f{169}{144} = ", TINTA), ("sec^2 x", ADJ)], XE + 220, 680, 80)
    cf_em(c, t, a8, [("f{13}{12} · f{13}{12} = f{169}{144}", TINTA2)], XE, 860, 66)
    resp(c, t, b8, [("sec x = f{13}{12}", BR)], 1480, 560, 76, 2.2, cor=ADJ)
    resp(c, t, c8, [("cos x = f{12}{13}", BR)], 1480, 800, 76, 2.2, cor=ADJ)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s19"] + 0.1, [("resumindo", "i", 92, COR)], W / 2, 190, "center")
        E.foco(c, t, C["s19.a"], 0.5, lambda a: cf(c, [("sec = f{1}{cos}", ADJ), ("    cossec = f{1}{sen}", OPO), ("    cotg = f{1}{tg}", TG)],
                                                   W / 2, 400, 72, a, "center"))
        E.foco(c, t, C["s19.b"], 0.5, lambda a: cf(c, [("1 + ", TINTA), ("tg^2", TG), (" = ", TINTA), ("sec^2", ADJ)], W / 2, 620, 90, a, "center"))
        E.frase(c, t, C["s19.c"], ps("na dúvida:", "i", 62) + [("seno e cosseno,", "g", 66, COR)] + ps("cortando só fator", "i", 62), W / 2, 840, "center", 0.1)
    E.saida(c, t, C["s20"] - 0.1, resumo)
    if t < C["s20"] - 0.1:
        return
    a0, b0, c0, d0, e0 = (C[f"s20.{k}"] for k in "abcde")
    E.frase(c, t, C["s20"], ps("na próxima aula", "i", 72), XE, 210, "left", 0.1)
    cf_em(c, t, a0, [("sen 75°", OPO)], XE, 400, 120)
    cf_em(c, t, b0, [("= sen(45° + 30°)", TINTA)], XE + 470, 400, 90)
    cf_em(c, t, c0, [("sen 2x", OPO), (" = ?", TINTA)], XE, 600, 110)
    E.foco(c, t, d0, 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 640, 76, estilo="g", a=a, cor=E.SOBRE))
    p = ease_io(prog(t, d0 + 0.3, 0.8))
    E.cursor(c, lerp(1850, 1650, p), lerp(880, 665, p), ep(t, d0 + 0.2, 0.4))
    E.frase(c, t, e0, [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 940, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, novas=b_novas, identidade=b_identidade, usar=b_usar, simplificar=b_simplificar,
              erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
