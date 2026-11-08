"""Visual — Estudativo · MAT-TOP-014: bases de contagem, binária e sexagesimal.

Linguagem: o quadro de casas é a peça central. Na base dez, as casas recebem o nome (centena, dezena, unidade); na base
dois, o valor de cada casa (16, 8, 4, 2, 1) com "× 2" entre elas. O algarismo 1 da base dois sai em índigo (a casa conta) e o
0 em cinza (não conta). A base fica embaixo, à direita do número (1011₂). Os restos das divisões ficam numa coluna à direita,
em âmbar, com a seta que sobe. Erro em vermelho, certo em verde, atalho no palco escuro.
Peças locais: binario() (algarismos numa linha de casas), casas() (cabeçalho 16 8 4 2 1), divisoes() (escada de divisões por 2),
relogio_60() (mostrador com o ponteiro dos minutos)."""
import math
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Matemática", "Tópicos Avançados")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-TOP-014_bases_binaria_e_sexagesimal.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("base10", "base2", "divisoes", "base60", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
RESTO = "#D98A00"


def bin2dec(s):
    return sum(int(d) * 2 ** i for i, d in enumerate(reversed(s)))


def passos2(n):
    out = []
    while n > 0:
        out.append((n, n // 2, n % 2))
        n //= 2
    return out


assert bin2dec("1011") == 11 and bin2dec("1101") == 13 and bin2dec("10110") == 22 and bin2dec("11001") == 25
assert passos2(13) == [(13, 6, 1), (6, 3, 0), (3, 1, 1), (1, 0, 1)] and divmod(90, 60) == (1, 30) and divmod(150, 60) == (2, 30)
assert 8 > 4 + 2 + 1 and 25 - 16 == 9 and 9 - 8 == 1


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def conta(c, partes, x, y, size, a=1.0, align="left", est="g"):
    ws = [E.formula(None, s, 0, 0, size, est, a=0) for s, _ in partes]
    w = sum(ws)
    xx = x - w / 2 if align == "center" else x - w if align == "right" else x
    if a > 0:
        for (s, cor), wi in zip(partes, ws):
            E.formula(c, s, xx, y, size, est, cor, a)
            xx += wi
    return w


def conta_em(c, t, t0, partes, x, y, size, align="left"):
    E.foco(c, t, t0, 0.5, lambda a: conta(c, partes, x, y, size, a, align))


def bola_txt(c, t, t0, s, cx, cy, r, size, cor=None):
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r * ease_back(prog(t, t0, 0.5)), cor, a),
                                     E.formula(c, s, cx, cy + size * 0.36, size, "g", BR, a, "center")))


VAL = (16, 8, 4, 2, 1)


def casas(c, t, t0, x, y, w, size=60, passo=0.25, escuro=False, dobra=None):
    """cabeçalho 16 8 4 2 1, entrando da direita para a esquerda; dobra = instante das setinhas "×2" """
    cor = CLARO if escuro else COR
    for i, v in enumerate(VAL):
        cx = x + (i + 0.5) * w
        ti = t0 + passo * (4 - i)
        E.foco(c, t, ti, 0.4, lambda a, v=v, cx=cx: (M.rrect(c, cx - w * 0.42, y - size * 1.05, w * 0.84, size * 1.4, 20, cor, 0.12 * a),
                                                     E.centro(c, str(v), cx, y, size, "g", cor, a)))
        if dobra is not None and i < 4:
            E.foco(c, t, dobra + 0.15 * (3 - i), 0.4, lambda a, i=i: E.centro(c, "× 2", x + (i + 1) * w, y - size * 1.25, 34, "b",
                                                                            "#FFFFFF" if escuro else TINTA2, a))


def binario(c, t, t0, s, x, y, w, size=110, passo=0.15, escuro=False, cores=None, alinha_dir=True):
    """algarismos de s nas casas (alinhados à direita das 5 casas): 1 em índigo, 0 em cinza"""
    n = len(s)
    ini = 5 - n if alinha_dir else 0
    for j, d in enumerate(s):
        cx = x + (ini + j + 0.5) * w
        cor = (cores or {}).get(j) or ((CLARO if escuro else COR) if d == "1" else (CINZA if not escuro else "#77778A"))
        E.foco(c, t, t0 + passo * j, 0.4, lambda a, d=d, cx=cx, cor=cor: E.centro(c, d, cx, y, size, "g", cor, a))


def num_base(c, s, b, x, y, size, cor=TINTA, a=1.0, align="left"):
    """número com a base pequena embaixo, à direita"""
    w = E.larg(s, "g", size)
    ws = E.larg(b, "g", size * 0.45)
    xx = x - (w + ws + 6) / 2 if align == "center" else x
    E.escreve(c, s, xx, y, size, "g", cor, a)
    E.escreve(c, b, xx + w + 6, y + size * 0.22, size * 0.45, "g", cor, a)
    return w + ws + 6


def num_base_em(c, t, t0, s, b, x, y, size, cor=TINTA, align="left"):
    E.foco(c, t, t0, 0.5, lambda a: num_base(c, s, b, x, y, size, cor, a, align))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def cena():
        num_base_em(c, t, C["s01.a"], "1011", "", W / 2, 400, 230, TINTA, "center")
        E.frase(c, t, C["s01.a"] + 1.2, [("mil", "i", 80, TINTA2), ("e", "i", 80, TINTA2), ("onze?", "i", 80, TINTA2)], W / 2, 560, "center")
        if t >= C["s01.b"]:
            E.risco(c, W / 2 - 260, 575, W / 2 + 260, 500, t, C["s01.b"], largura=12)
        E.foco(c, t, C["s01.b"] + 0.3, 0.5, lambda a: E.pilula(c, "computador: 11", W / 2, 680, 64, "g", a=a))
        E.foco(c, t, C["s01.c"], 0.5, lambda a: conta(c, [("90 min = ", TINTA), ("1 h 30 min", COR)], W / 2, 900, 96, a, "center"))
    E.saida(c, t, C["s02"] - 0.1, cena)
    if t >= C["s02"]:
        E.foco(c, t, C["s02.b"] - 0.2, 0.7, lambda a: E.bola(c, 1480, 540, 290 * ease_back(prog(t, C["s02.b"] - 0.2, 0.7))), blur=0)
        E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 90), XE, 300)
        E.frase(c, t, C["s02.a"] + 1.0, [("base", "i", 110), ("10", "g", 130, COR), ("e", "i", 110), ("base", "i", 110), ("2", "g", 130, COR)], XE, 470)
        E.frase(c, t, C["s02.a"] + 3.0, [("e", "i", 100), ("a", "i", 100), ("base", "i", 100), ("60", "g", 120, COR)], XE, 630)
        E.frase(c, t, C["s02.a"] + 4.0, ps("do relógio", "i", 80, TINTA2), XE, 750)
        E.foco(c, t, C["s02.b"] + 0.2, 0.5, lambda a: (E.escreve(c, "+ atalho", 1320, 525, 84, "g", BR, a),
                                                      E.escreve(c, "de prova", 1340, 610, 84, "i", BR, a)))


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.linha(c, t, [("você", "i", 84, TINTA, C["s03"]), ("precisa", "i", 84, TINTA, C["s03"] + 0.2), ("de", "i", 84, TINTA, C["s03"] + 0.4),
                   ("três", "g", 80, COR, C["s03.a"]), ("coisas", "i", 84, TINTA, C["s03.a"] + 0.2)], W / 2, 190, "center")
    itens = (("s03.b", [("casas:", "i", 64), ("centena,", "g", 60), ("dezena,", "g", 60), ("unidade", "g", 60)], "cada uma vale 10 da direita"),
             ("s03.c", [("dividir", "g", 60), ("com", "i", 64), ("resto", "g", 60, COR)], "17 ÷ 5 = 3, resto 2"),
             ("s03.d", [("potência", "g", 60, COR)], "2^3 = 2 · 2 · 2 = 8"))
    for i, (k, partes, f) in enumerate(itens):
        y = 300 + i * 220
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, 200, y, 1520, 190, p, prog_=p)
        E.frase(c, t, C[k], partes, 250, y + 80)
        E.foco(c, t, C[k] + 1.0, 0.5, lambda a, f=f, y=y: E.formula(c, f, 250, y + 160, 54, "b", TINTA2, a))
    E.frase(c, t, C["s04"] - 2.4, ps("faltou alguma? procure no canal", "i", 50, TINTA2), W / 2, 1000, "center", passo=0.1)


# ---------------- base dez ----------------
def cubinho(c, x, y, s, cor, a=1.0):
    M.rrect(c, x, y, s, s, 4, cor, a)


def b_base10(c, t, C, b):
    u = 22
    # s04: dez cubinhos viram uma barra; dez barras viram uma placa
    def grupos():
        X0, Y0 = 1000, 330
        jun = ep(t, C["s04.b"], 0.8)
        for i in range(10):
            xi = lerp(X0 + (i % 5) * (u + 18), X0, jun)
            yi = lerp(Y0 + (i // 5) * (u + 18), Y0 + i * u, jun)
            E.foco(c, t, C["s04.a"] + 0.05 * i, 0.3, lambda a, xi=xi, yi=yi: cubinho(c, xi, yi, u - 2, COR, a))
        E.foco(c, t, C["s04.b"] + 0.6, 0.4, lambda a: E.escreve(c, "1 dezena", X0 + 50, Y0 + 130, 54, "g", COR, a))
        if t >= C["s04.c"]:
            for j in range(10):
                q = ep(t, C["s04.c"] + 0.06 * j, 0.3)
                for i in range(10):
                    cubinho(c, 1400 + j * u, Y0 + i * u, u - 2, COR, q)
            E.foco(c, t, C["s04.c"] + 0.8, 0.4, lambda a: E.escreve(c, "1 centena", 1400, Y0 + 290, 54, "g", COR, a))
        E.frase(c, t, C["s04.a"], [("grupos", "i", 80), ("de", "i", 80), ("10", "g", 90, COR)], XE, 360)
        E.frase(c, t, C["s04.b"], ps("10 unidades viram 1 dezena", "i", 58), XE, 480, passo=0.1)
        E.frase(c, t, C["s04.c"], ps("10 dezenas viram 1 centena", "i", 58), XE, 570, passo=0.1)
        E.frase(c, t, C["s04.d"], [("base", "i", 110), ("10", "g", 120, COR)], XE, 780)
        E.frase(c, t, C["s04.d"] + 1.0, ps("algarismos de 0 a 9", "i", 60, TINTA2), XE, 880, passo=0.1)
    E.saida(c, t, C["s05"] - 0.1, grupos)
    if t < C["s05"]:
        return
    x, w = 560, 270
    E.quadro_casas(c, t, ["centena", "dezena", "unidade"], [C["s05"]] * 3,
                   [[("3", C["s05.a"], COR), ("5", C["s05.b"], COR), ("2", C["s05.c"], COR)]], x, 330, w, size=140, grossa=None)
    for i, (k, s) in enumerate((("s05.a", "3 × 100"), ("s05.b", "5 × 10"), ("s05.c", "2 × 1"))):
        E.foco(c, t, C[k] + 0.3, 0.4, lambda a, i=i, s=s: E.centro(c, s, x + (i + 0.5) * w, 640, 52, "b", TINTA2, a))
    E.frase(c, t, C["s05.d"], [("algarismo", "i", 66), ("×", "g", 66, COR), ("valor", "i", 66), ("da", "i", 66), ("casa", "g", 66)], W / 2, 860, "center")


# ---------------- base dois ----------------
X2, W2 = 470, 196


def b_base2(c, t, C, b):
    E.frase(c, t, C["s06.a"], [("base", "i", 90), ("2:", "g", 100, COR), ("grupos", "i", 90), ("de", "i", 90), ("2", "g", 100, COR)], W / 2, 190, "center")

    def s06():
        E.frase(c, t, C["s06.b"], [("só", "i", 80), ("0", "g", 100, CINZA), ("e", "i", 80), ("1", "g", 100, COR)], W / 2, 360, "center")
        casas(c, t, C["s06.d"] - 0.6, X2, 640, W2, 80, 0.3, dobra=C["s06.c"] + 1.6)
        E.frase(c, t, C["s06.c"], [("cada", "i", 66), ("casa", "i", 66), ("=", "i", 66), ("o", "i", 66), ("dobro", "g", 66, COR)], W / 2, 860, "center")
        E.frase(c, t, C["s06.d"] + 2.4, [("potências", "i", 60, TINTA2), ("de", "i", 60, TINTA2), ("2", "g", 60, COR)], W / 2, 960, "center")
    E.saida(c, t, C["s07"] - 0.1, s06)
    if t < C["s07"]:
        return
    casas(c, t, C["s07"], X2, 400, W2, 70, 0.05)
    binario(c, t, C["s07.a"], "1011", X2, 590, W2, 130, 0.2)
    if t >= C["s07.c"]:
        for j, v in ((1, 8), (3, 2), (4, 1)):
            q = ep(t, C["s07.c"] + 0.2 * (j > 1) + 0.2 * (j > 3), 0.4)
            cx = X2 + (j + 0.5) * W2
            c.drawCircle(cx, 548, 92, M.paint(COR, 0.12 * q))
    E.foco(c, t, C["s07.b"], 0.4, lambda a: (M.arrow(c, X2 + 5 * W2 + 20, 700, X2 + W2 + 40, 700, TINTA2, a, 5, 18, ep(t, C["s07.b"], 0.8)),
                                            E.escreve(c, "da direita", X2 + 5 * W2 - 300, 760, 44, "i", TINTA2, a)))
    conta_em(c, t, C["s07.c"] + 0.4, [("8 + 2 + 1 = ", TINTA)], 700, 880, 96)
    bola_txt(c, t, C["s07.d"], "11", 1320, 848, 82, 90)
    if t >= C["s08"]:
        def nota():
            num_base(c, "1011", "2", 580, 1020 - 30, 76, COR, ep(t, C["s08.a"], 0.4))
            E.foco(c, t, C["s08.b"], 0.4, lambda a: E.escreve(c, "=  11", 860, 990, 76, "g", TINTA, a))
            E.foco(c, t, C["s08.b"] + 0.2, 0.4, lambda a: E.escreve(c, "10", 860 + E.larg("=  11", "g", 76) + 6, 1007, 34, "g", TINTA, a))
        nota()


# ---------------- de dez para dois: divisões ----------------
def divisoes(c, t, ts, x, y, dy=120, size=76, tr=None, cor_seta=None, sobe=True):
    """escada de divisões por 2 do 13: ts = instante de cada linha; tr = instante da seta dos restos"""
    for i, (n, q, r) in enumerate(passos2(13)):
        yy = y + i * dy
        E.foco(c, t, ts[i], 0.4, lambda a, n=n, q=q, yy=yy: E.formula(c, f"{n} ÷ 2 = {q}", x + 380, yy, size, "g", TINTA, a, "right"))
        E.foco(c, t, ts[i] + 0.4, 0.4, lambda a, r=r, yy=yy: (E.escreve(c, "resto", x + 450, yy, size * 0.6, "i", TINTA2, a),
                                                             E.escreve(c, str(r), x + 640, yy, size * 1.1, "g", RESTO, a)))
    if tr is not None and t >= tr:
        p = ep(t, tr, 0.9)
        ya, yb = y + 3 * dy + 10, y - size - 10
        if not sobe:
            ya, yb = yb + 20, ya + 30
        M.arrow(c, x + 760, ya, x + 760, yb, cor_seta or CERTO, p, 8, 26, p)


def b_divisoes(c, t, C, b):
    E.frase(c, t, C["s09.a"], [("13", "g", 90, COR), ("na", "i", 80), ("base", "i", 80), ("2", "g", 90, COR)], XE, 200)
    E.frase(c, t, C["s09.b"], ps("divida por 2 e anote o resto", "i", 54, TINTA2), XE, 290, passo=0.1)
    divisoes(c, t, [C["s09.c"], C["s09.d"], C["s09.e"], C["s09.f"]], XE, 430, tr=C["s10.c"])
    E.frase(c, t, C["s10"], ps("chegou a 0: pare", "i", 50, TINTA2), XE, 960, passo=0.1)
    E.foco(c, t, C["s10.b"], 0.4, lambda a: E.pilula(c, "unidade", XE + 650, 322, 36, "g", fundo=RESTO, a=a))
    E.frase(c, t, C["s10.c"], [("de", "i", 66), ("baixo", "g", 66, CERTO), ("para", "i", 66), ("cima", "g", 66, CERTO)], 1140, 430)
    if t >= C["s10.d"]:
        for j, d in enumerate("1101"):
            E.foco(c, t, C["s10.d"] + 0.2 * j, 0.4, lambda a, j=j, d=d: E.escreve(c, d, 1140 + j * 110, 640, 150, "g", COR if d == "1" else CINZA, a))
        E.foco(c, t, C["s10.d"] + 1.0, 0.4, lambda a: E.escreve(c, "2", 1140 + 4 * 110 + 4, 670, 60, "g", COR, a))
    conta_em(c, t, C["s10.e"], [("8 + 4 + 1 = ", TINTA), ("13", CERTO)], 1140, 820, 80)


# ---------------- base sessenta ----------------
def relogio_60(c, cx, cy, r, a, ang):
    if a <= 0:
        return
    c.drawCircle(cx, cy, r, M.paint("#FFFFFF", a))
    c.drawCircle(cx, cy, r, M.paint(TINTA, a, stroke=8))
    for i in range(60):
        th = math.radians(90 - 6 * i)
        l = 26 if i % 5 == 0 else 12
        M.line(c, cx + (r - 14) * math.cos(th), cy - (r - 14) * math.sin(th), cx + (r - 14 - l) * math.cos(th), cy - (r - 14 - l) * math.sin(th),
               TINTA if i % 5 == 0 else CINZA, a, 5 if i % 5 == 0 else 3)
    th = math.radians(90 - ang)
    M.line(c, cx, cy, cx + (r - 50) * math.cos(th), cy - (r - 50) * math.sin(th), COR, a, 10)
    c.drawCircle(cx, cy, 14, M.paint(TINTA, a))


def b_base60(c, t, C, b):
    def s11():
        a = ep(t, C["s11.a"], 0.5)
        # o ponteiro dá uma volta: 60 minutos
        ang = 360 * ease_io(prog(t, C["s11.d"] - 0.4, 1.6))
        relogio_60(c, 1400, 560, 300, a, ang)
        E.frase(c, t, C["s11.a"], [("base", "i", 110), ("60", "g", 130, COR)], XE, 330)
        E.frase(c, t, C["s11.b"], ps("grupos de 60", "i", 70), XE, 460)
        conta_em(c, t, C["s11.c"], [("60 s = ", TINTA), ("1 min", COR)], XE, 600, 80)
        conta_em(c, t, C["s11.d"], [("60 min = ", TINTA), ("1 h", COR)], XE, 720, 80)
        E.frase(c, t, C["s11.d"] + 2.0, ps("vem da antiga Mesopotâmia", "i", 54, TINTA2), XE, 860, passo=0.1)
    E.saida(c, t, C["s12"] - 0.1, s11)
    if t < C["s12"]:
        return
    E.frase(c, t, C["s12"], [("90", "g", 110, COR), ("minutos", "i", 100)], XE, 300)
    E.frase(c, t, C["s12.a"], ps("quantos grupos de 60?", "i", 66), XE, 430, passo=0.1)
    conta_em(c, t, C["s12.b"], [("90 ÷ 60 = ", TINTA), ("1", COR), (", resto ", TINTA), ("30", RESTO)], XE, 590, 92)
    E.foco(c, t, C["s12.c"], 0.4, lambda a: (E.pilula(c, "hora", XE + 480, 690, 40, "g", fundo=COR, a=a),
                                            E.pilula(c, "minutos", XE + 870, 690, 40, "g", fundo=RESTO, a=a)))
    bola_txt(c, t, C["s12.d"], "1 h 30 min", 1420, 560, 210, 76)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s13"], [("cuidado", "g", 96, ERRADO)], XE, 200)
    divisoes(c, t, [C["s13"] + 0.3 + 0.15 * i for i in range(4)], XE, 400, dy=110, size=68, tr=C["s13.a"], cor_seta=ERRADO, sobe=False)
    E.frase(c, t, C["s13.a"], [("de", "i", 60), ("cima", "g", 60, ERRADO), ("para", "i", 60), ("baixo?", "g", 60, ERRADO)], 1140, 380)
    E.foco(c, t, C["s13.b"], 0.4, lambda a: num_base(c, "1011", "2", 1140, 560, 130, ERRADO, a))
    E.foco(c, t, C["s13.c"], 0.4, lambda a: E.escreve(c, "= 11, não 13", 1140, 690, 66, "g", ERRADO, a))
    if t >= C["s13.c"] + 0.8:
        E.risco(c, 1130, 580, 1530, 440, t, C["s13.c"] + 0.8, largura=12)
    E.foco(c, t, C["s14.a"], 0.4, lambda a: E.pilula(c, "1º resto = unidade", XE + 600, 300, 40, "g", fundo=RESTO, a=a))
    E.frase(c, t, C["s14.c"], [("de", "i", 60), ("baixo", "g", 60, CERTO), ("para", "i", 60), ("cima:", "g", 60, CERTO)], 1140, 830)
    E.foco(c, t, C["s14.c"] + 0.8, 0.4, lambda a: num_base(c, "1101", "2", 1140, 980, 110, CERTO, a))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    x, w = 470, 196

    def s15():
        E.frase(c, t, C["s15"], ps("agora, o atalho", "i", 76, CLARO), W / 2, 170, "center")
        casas(c, t, C["s15.a"], x, 400, w, 70, 0.25, escuro=True)
        E.frase(c, t, C["s15.b"], [("13", "g", 80, BR), ("→", "g", 70, CLARO), ("a", "i", 70, CLARO), ("maior", "g", 70, BR), ("que", "i", 70, CLARO),
                                   ("cabe", "i", 70, CLARO)], W / 2, 270, "center")
        regs = (("s15.b", "1", "13 − 8 = 5"), ("s15.c", "1", "5 − 4 = 1"), ("s15.d", "0", "não cabe"), ("s15.e", "1", "1 − 1 = 0"))
        for j, (k, d, s) in enumerate(regs):
            cx = x + (j + 1.5) * w
            E.foco(c, t, C[k] + 0.2, 0.4, lambda a, d=d, cx=cx: E.centro(c, d, cx, 600, 130, "g", BR if d == "1" else "#77778A", a))
            E.foco(c, t, C[k] + 0.6, 0.4, lambda a, s=s, cx=cx: E.centro(c, s, cx, 710, 42, "b", CLARO, a))
        E.foco(c, t, C["s15.b"] + 0.2, 0.4, lambda a: E.centro(c, "0", x + 0.5 * w, 600, 130, "g", "#77778A", a * 0.6))
        E.foco(c, t, C["s15.f"], 0.5, lambda a: num_base(c, "1101", "2", W / 2, 900, 130, C_ESC, a, "center"))
    E.saida(c, t, C["s16"] - 0.1, s15)
    if t < C["s16"]:
        return
    E.frase(c, t, C["s16"], [("por", "i", 70, CLARO), ("que", "i", 70, CLARO), ("funciona", "g", 70, BR)], W / 2, 200, "center")
    E.frase(c, t, C["s16.a"], ps("cada casa é maior que todas as da direita juntas", "i", 58, CLARO), W / 2, 330, "center", passo=0.08)
    conta_em(c, t, C["s16.a"] + 2.0, [("8 > 4 + 2 + 1 = 7", BR)], W / 2, 480, 96, "center")
    E.frase(c, t, C["s16.b"], [("não", "g", 72, ERRADO), ("compensa:", "i", 76, CLARO), ("número", "i", 76, CLARO), ("grande", "g", 72, BR)],
            W / 2, 700, "center")
    E.frase(c, t, C["s16.b"] + 2.4, ps("aí, as divisões são mais seguras", "i", 60, CLARO), W / 2, 820, "center", passo=0.1)


C_ESC = "#3CC7D3"


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s17"], ps("hora de testar", "i", 72, COR), XE, 200)
    E.frase(c, t, C["s17.a"], [("1)", "g", 64, COR)], XE, 380)
    E.foco(c, t, C["s17.a"] + 0.2, 0.4, lambda a: E.escreve(c, "= ?", XE + 130 + num_base(c, "10110", "2", XE + 110, 380, 96, TINTA, a), 380, 96, "g", TINTA, a))
    E.frase(c, t, C["s17.b"], [("2)", "g", 64, COR), ("25", "g", 96), ("na", "i", 80), ("base", "i", 80), ("2", "g", 96, COR)], XE, 560)
    E.frase(c, t, C["s17.c"], [("3)", "g", 64, COR), ("150", "g", 96), ("min", "i", 80), ("=", "i", 80), ("?", "g", 96, COR)], XE, 740)
    if t >= C["s18"]:
        E.relogio(c, t, C["s18.a"], cx=1440, cy=470, r=190)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    x, w = 470, 196

    def s19():
        casas(c, t, C["s19.a"], x, 340, w, 66, 0.05)
        binario(c, t, C["s19.a"] + 0.3, "10110", x, 520, w, 120, 0.12)
        if t >= C["s19.b"]:
            for j in (0, 2, 3):
                q = ep(t, C["s19.b"] + 0.25 * (j > 0) + 0.25 * (j > 2), 0.4)
                c.drawCircle(x + (j + 0.5) * w, 482, 88, M.paint(COR, 0.12 * q))
        conta_em(c, t, C["s19.b"] + 0.4, [("16 + 4 + 2 = ", TINTA)], 640, 800, 92)
        bola_txt(c, t, C["s19.c"], "22", 1300, 770, 80, 86)
    E.saida(c, t, C["s20"] - 0.1, s19)
    if t < C["s20"]:
        return

    def s20():
        casas(c, t, C["s20"], x, 340, w, 66, 0.05)
        regs = (("s20.a", 0, "1", "25 − 16 = 9"), ("s20.b", 1, "1", "9 − 8 = 1"), ("s20.c", 2, "0", "não"), ("s20.c", 3, "0", "não"),
                ("s20.d", 4, "1", "1 − 1 = 0"))
        for k, j, d, s in regs:
            cx = x + (j + 0.5) * w
            E.foco(c, t, C[k] + 0.2 * (j == 3), 0.4, lambda a, d=d, cx=cx: E.centro(c, d, cx, 530, 120, "g", COR if d == "1" else CINZA, a))
            E.foco(c, t, C[k] + 0.4, 0.4, lambda a, s=s, cx=cx: E.centro(c, s, cx, 640, 42, "b", TINTA2, a))
        E.foco(c, t, C["s20.e"], 0.5, lambda a: num_base(c, "11001", "2", W / 2, 860, 130, CERTO, a, "center"))
    E.saida(c, t, C["s21"] - 0.1, s20)
    if t < C["s21"]:
        return
    E.frase(c, t, C["s21"], [("150", "g", 110, COR), ("minutos", "i", 100)], XE, 320)
    conta_em(c, t, C["s21.a"], [("150 ÷ 60 = ", TINTA), ("2", COR), (", resto ", TINTA), ("30", RESTO)], XE, 520, 92)
    bola_txt(c, t, C["s21.b"], "2 h 30 min", 1420, 600, 210, 76, CERTO)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s22"], [("resumindo", "i", 92, COR)], W / 2, 200, "center")
        itens = (("s22.a", [("a", "i", 72), ("base", "g", 70), ("=", "i", 72), ("o", "i", 72), ("tamanho", "i", 72), ("do", "i", 72), ("grupo", "g", 70, COR)]),
                 ("s22.b", [("base", "i", 72), ("2:", "g", 70, COR), ("as", "i", 72), ("casas", "i", 72), ("dobram", "g", 70)]),
                 ("s22.c", [("divida", "g", 70), ("por", "i", 72), ("2,", "g", 70), ("restos", "i", 72), ("de", "i", 72), ("baixo", "g", 70, COR), ("para", "i", 72), ("cima", "g", 70, COR)]))
        for i, (k, partes) in enumerate(itens):
            y = 400 + i * 200
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 240, y - 26, 56, a=a),
                                                         E.escreve(c, str(i + 1), 240 - E.larg(str(i + 1), "g", 64) / 2, y - 3, 64, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, partes, 340, y, passo=0.12)
    E.saida(c, t, C["s23"] - 0.1, resumo)
    if t < C["s23"]:
        return
    E.frase(c, t, C["s23"], [("próxima", "i", 84), ("aula", "i", 84)], XE, 290)
    E.frase(c, t, C["s23.a"], [("Algarismos", "g", 130, COR)], XE, 450)
    E.frase(c, t, C["s23.a"] + 0.4, [("significativos", "g", 130, COR)], XE, 590)
    E.foco(c, t, C["s23.b"], 0.5, lambda a: E.formula(c, "2,5 × 3,14 → 7,9", XE, 730, 72, "g", TINTA2, a))
    E.foco(c, t, C["s23.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1450, 300, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s23.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1780, 1580, p), lerp(620, 325, p), ep(t, C["s23.c"] + 0.2, 0.4))
    E.frase(c, t, C["s23.d"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 920, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, base10=b_base10, base2=b_base2, divisoes=b_divisoes, base60=b_base60, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
