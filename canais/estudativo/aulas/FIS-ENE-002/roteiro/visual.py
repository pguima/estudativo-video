"""Visual — Estudativo · FIS-ENE-002: potência e rendimento.

Linguagem visual: a da Física (cabeçalho do visual.py da FIS-CIN-001) e a da trilha Energia e Colisões (cabeçalho do
visual.py da FIS-ENE-001). Nesta aula: o rendimento é um fluxo (peça fluxo): a potência recebida entra em tinta, a útil
sai em laranja e a dissipada desce em cinza, com a espessura proporcional ao valor.
Todo instante vem de C[...] (marcadores do roteiro)."""
import math

import editorial as E
import fisica as F
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Física", "Energia e Colisões")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_FIS-ENE-002_potencia_e_rendimento.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("potencia", "unidades", "rendimento", "atalho", "questao", "fim"))
BR = "#FFFFFF"

# todas as contas da aula
assert 6000 / 60 == 100 and 6000 / 240 == 25 and 100 * 735 == 73500 and 73500 / 1000 == 73.5 and 100 * 746 / 1000 == 74.6
assert 800 / 1000 == 0.8 and 1000 / 800 == 1.25 and 1000 - 800 == 200 and 1000 * 20 == 20000
assert 30000 / 20 == 1500 and 1500 / 2000 == 0.75 and 2000 - 1500 == 500


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças da trilha ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def bola_txt(c, t, t0, s, cx, cy, r, size, cor=None):
    """resposta na esfera: "250 J" com a unidade menor"""
    v, _, u = s.partition(" ")
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r * ease_back(prog(t, t0, 0.5)), cor, a),
                                     F.medida(c, v, u, cx, cy + size * 0.36, size, E.SOBRE, a, "center", cor_u=E.SOBRE)))


def troca(c, t, itens, fn):
    """um de cada vez: itens = [(instante, arg)], cada um sai quando o próximo chega; fn(arg, a) desenha"""
    for i, (ti, s) in enumerate(itens):
        fim = itens[i + 1][0] - 0.1 if i + 1 < len(itens) else 1e9
        if t >= ti - 0.01:
            E.saida(c, t, fim, lambda s=s, ti=ti: E.foco(c, t, ti, 0.45, lambda a: fn(s, a)), d=0.25)


def pilula_em(c, t, t0, s, cx, cy, size, fundo=None, est="g"):
    E.foco(c, t, t0, 0.4, lambda a: E.pilula(c, s, cx, cy, size, est, fundo=fundo, a=a, cor=BR))


def sinal_tau(c, t, t0, tipo, cx, cy, size=48):
    """pílula do sinal do trabalho: + ajuda (laranja), − atrapalha (azul), 0 perpendicular (cinza)"""
    txt, fundo = {"+": ("τ > 0", E.COR), "-": ("τ < 0", F.NEG), "0": ("τ = 0", TINTA2)}[tipo]
    pilula_em(c, t, t0, txt, cx, cy, size, fundo)


def lembrete(c, t, C, cena, itens, desenhos=()):
    """lembrete de 2 ou 3 coisas: itens = [(cue, linha fina, linha forte, linha de fórmula ou None)]"""
    n = len(itens)
    E.frase(c, t, C[cena] + 0.2, ps("você precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C[cena + ".a"], 0.5, lambda a: E.escreve(c, str(n), XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C[cena + ".a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 820, 1000
    hs = [200 + (70 if it[3] else 0) for it in itens]
    gap = 40 if n == 2 else 30
    y = 120 + (800 - sum(hs) - gap * (n - 1)) / 2
    for i, (k, l1, l2, l3) in enumerate(itens):
        h = hs[i]
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, h, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 56)], x + 44, y + 82)
        E.frase(c, t, C[k] + 0.3, [(l2, "g", 56, COR)], x + 44, y + 160)
        if l3:
            E.foco(c, t, C[k] + 0.9, 0.5, lambda a, l3=l3, y=y: E.formula(c, l3, x + 44, y + 240, 46, "b", TINTA2, a))
        if i < len(desenhos) and desenhos[i]:
            E.foco(c, t, C[k] + 0.6, 0.5, lambda a, i=i, y=y, h=h: desenhos[i](a, x + w - 160, y + 105))
        y += h + gap
    E.frase(c, t, lerp(C[itens[-1][0]], C[cena + ".end"], 0.7), ps("faltou alguma?", "i", 54, COR) + ps("procure no canal", "i", 54),
            820, 1000, "left", 0.12)


# ---------------- desenhos desta aula ----------------
def caixas(c, cx, yb, k, a=1.0):
    """pilha de três caixas de papelão com a base em yb"""
    if a <= 0:
        return
    for i, (dx, w) in enumerate(((0, 150), (10, 130), (-6, 110))):
        y = yb - 90 * k * (i + 1)
        F.bloco(c, cx + dx * k, y + 45 * k, w * k, 86 * k, None, "#C08A55", a)
        M.line(c, cx + dx * k - w * k / 2 + 8, y + 45 * k, cx + dx * k + w * k / 2 - 8, y + 45 * k, "#8A5E33", a, 3)


def escada(c, x, yb, n, passo, alto, a=1.0):
    """escada subindo para a direita a partir de (x, yb)"""
    if a <= 0:
        return
    pts = [(x, yb)]
    for i in range(n):
        pts += [(x + i * passo, yb - (i + 1) * alto), (x + (i + 1) * passo, yb - (i + 1) * alto)]
    F.poli(c, pts, 1.0, TINTA, a, 6)


def fluxo(c, t, t0, x, y, total, util, txt_total, txt_util, txt_perda, t_util=None, t_perda=None, esc=0.32, rot_maq="motor"):
    """rendimento como fluxo: banda que entra (total), sai à direita (útil, laranja) e desce (perda, cinza)"""
    q = ep(t, t0, 0.5)
    if q <= 0:
        return
    hT, hU = total * esc, util * esc
    hP = hT - hU
    xm, wm = x + 360, 220
    p = ease_io(prog(t, t0, 0.7))
    c.drawRect(skia.Rect.MakeXYWH(x, y - hT / 2, (xm - x) * p, hT), M.paint(TINTA2, 0.85 * q))
    E.foco(c, t, t0, 0.4, lambda a: (F.medida(c, *txt_total.split(" ", 1), x, y - hT / 2 - 24, 56, TINTA, a),
                                     E.escreve(c, "recebe", x, y - hT / 2 - 90, 48, "i", TINTA2, a)))
    M.rrect(c, xm, y - hT / 2 - 40, wm, hT + 80, 26, TINTA, q)
    E.foco(c, t, t0 + 0.2, 0.4, lambda a: centro(c, rot_maq, xm + wm / 2, y + 16, 48, "g", BR, a))
    tu = t_util if t_util is not None else t0 + 0.8
    pu = ease_io(prog(t, tu, 0.7))
    if pu > 0:
        c.drawRect(skia.Rect.MakeXYWH(xm + wm, y - hT / 2, 360 * pu, hU), M.paint(E.COR, 0.95))
        F._cabeca(c, xm + wm + 360 * pu + max(40, hU * 0.8), y - hT / 2 + hU / 2, 1, 0, max(40, hU * 0.8), E.COR, pu)
        E.foco(c, t, tu + 0.4, 0.4, lambda a: (F.medida(c, *txt_util.split(" ", 1), xm + wm + 40, y - hT / 2 - 24, 56, COR, a),
                                                E.escreve(c, "útil", xm + wm + 40, y - hT / 2 - 90, 48, "i", COR, a)))
    tp = t_perda if t_perda is not None else tu + 0.6
    pp = ease_io(prog(t, tp, 0.7))
    if pp > 0 and hP > 0:
        xs = xm + wm + 40
        c.drawRect(skia.Rect.MakeXYWH(xs, y - hT / 2 + hU, hP, 0), M.paint(CINZA, 0.8))
        c.drawRect(skia.Rect.MakeXYWH(xm + wm, y - hT / 2 + hU, 40 + hP, hP), M.paint(CINZA, 0.8))
        c.drawRect(skia.Rect.MakeXYWH(xs, y - hT / 2 + hU + hP, hP, 200 * pp), M.paint(CINZA, 0.8))
        F._cabeca(c, xs + hP / 2, y - hT / 2 + hU + hP + 200 * pp + max(36, hP * 1.0), 0, 1, max(36, hP * 1.0), CINZA, pp)
        E.foco(c, t, tp + 0.4, 0.4, lambda a: (F.medida(c, *txt_perda.split(" ", 1), xs + hP + 30, y + hT / 2 + 150, 52, TINTA2, a),
                                                E.escreve(c, "calor", xs + hP + 30, y + hT / 2 + 210, 46, "i", TINTA2, a)))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def um():
        for i, (k, tempo, seg) in enumerate((("s01.b", "1 min", 15), ("s01.c", "4 min", 60))):
            x = 260 + i * 820
            E.foco(c, t, C["s01.a"] + 0.2 * i, 0.5, lambda a, x=x: (escada(c, x, 760, 4, 110, 90, a), caixas(c, x + 470, 400, 0.8, a)))
            E.foco(c, t, C["s01.a"] + 0.3, 0.4, lambda a, x=x: E.escreve(c, "caixas iguais", x, 860, 50, "i", TINTA2, a))
            E.foco(c, t, C[k], 0.5, lambda a, x=x, tempo=tempo, seg=seg, i=i: F.cronometro(c, x + 120, 280, 95, seg, a, tempo, cor=E.COR if i == 0 else TINTA2))
        E.frase(c, t, C["s01.a"], ps("o mesmo andar", "i", 70), W / 2, 150, "center", 0.12)
        E.frase(c, t, C["s01.d"], [("mesmo", "g", 76), ("trabalho", "g", 76, COR)], W / 2, 990, "center", 0.12)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t >= C["s02"]:
        tb = C["s02.b"]
        E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1480, 560, 300 * ease_back(prog(t, tb, 0.8)), giro=12 * math.sin(t * 0.4)), blur=0)
        E.frase(c, t, C["s02"], [("muda", "i", 90), ("a", "i", 90), ("potência", "g", 110, COR)], XE, 250)
        itens = (("s02.b", "watt"), ("s02.c", "rendimento em %"), ("s02.d", "kW, cv e hp"))
        for i, (k, s) in enumerate(itens):
            y = 470 + i * 160
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, XE + 40, y - 30, 38, a=a), centro(c, str(i + 1), XE + 40, y - 8, 48, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, [(s, "g", 80, TINTA)], XE + 110, y)


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    lembrete(c, t, C, "s03", (("s03.b", "o trabalho de uma força,", "em joule (J)", None),
                              ("s03.c", "porcentagem,", "a parte de cem", None),
                              ("s03.d", "os prefixos,", "quilo = 1.000", None)),
             (lambda a, x, y: E.formula(c, "τ = F · d · cos θ", x - 220, y + 15, 50, "g", TINTA2, a),
              lambda a, x, y: E.formula(c, "80% = f{80}{100}", x - 160, y + 25, 54, "g", TINTA2, a)))


# ---------------- potência ----------------
def b_potencia(c, t, C, b):
    def s04():
        E.frase(c, t, C["s04.a"], [("potência", "g", 100, COR)], XE, 240)
        E.frase(c, t, C["s04.a"] + 0.6, ps("a rapidez com que um trabalho é feito", "i", 62), XE, 340, passo=0.1)
        F.formula_legenda(c, t, C["s04.c"], "P = f{τ}{Δt}", [("P", "potência", "W"), ("τ", "trabalho", "J"), ("Δt", "intervalo de tempo", "s")],
                          XE, 560, 130, tl=[C["s04.c"] + 0.7, C["s04.c"] + 1.1, C["s04.d"]])
        E.frase(c, t, C["s04.b"], [("trabalho", "i", 60, TINTA2), ("÷", "g", 60, TINTA2), ("tempo", "i", 60, TINTA2)], 1150, 560)
        E.foco(c, t, C["s04.d"] + 1.2, 0.5, lambda a: E.formula(c, "Δt = t fim − t começo", 1150, 700, 58, "b", TINTA, a))
    E.saida(c, t, C["s05"] - 0.1, s04)
    if C["s05"] <= t < C["s06"]:
        def s05():
            E.foco(c, t, C["s05.a"], 0.5, lambda a: E.formula(c, "J/s", XE, 380, 150, "g", TINTA, a))
            wj = E.formula(None, "J/s", 0, 0, 150, "g", a=0)
            E.foco(c, t, C["s05.b"], 0.5, lambda a: E.formula(c, " = W", XE + wj, 380, 150, "g", COR, a))
            E.frase(c, t, C["s05.b"] + 0.4, [("watt", "i", 90)], XE + wj + 380, 380)
            E.foco(c, t, C["s05.c"], 0.5, lambda a: F.medida(c, 10, "W", XE, 700, 120, COR, a))
            E.frase(c, t, C["s05.c"] + 0.5, [("=", "g", 70), ("10 J", "g", 70), ("a", "i", 74), ("cada", "i", 74), ("segundo", "g", 70, COR)], XE + 330, 690, passo=0.12)
            for k in range(10):
                E.foco(c, t, C["s05.c"] + 1.2 + 0.12 * k, 0.3, lambda a, k=k: E.bola(c, 1050 + 70 * k, 860, 26, a=a))
        E.saida(c, t, C["s06"] - 0.1, s05)
    if t < C["s06"]:
        return
    E.frase(c, t, C["s06"], [("as", "i", 70), ("caixas:", "i", 70), ("τ", "g", 70, COR), ("=", "g", 70)], XE, 190, passo=0.12)
    E.foco(c, t, C["s06.a"], 0.5, lambda a: F.medida(c, "6.000", "J", XE + 380, 190, 70, TINTA, a))
    for i, (kb, kr, tempo, conta, res) in enumerate((("s06.b", "s06.c", "1 min = 60 s", "f{6.000}{60}", "100 W"),
                                                     ("s06.d", "s06.e", "4 min = 240 s", "f{6.000}{240}", "25 W"))):
        x = 470 + i * 980
        E.foco(c, t, C[kb], 0.5, lambda a, x=x, tempo=tempo: E.formula(c, tempo, x, 360, 64, "g", TINTA2, a, "center"))
        E.foco(c, t, C[kr], 0.5, lambda a, x=x, conta=conta: E.formula(c, "P = " + conta, x, 560, 96, "g", TINTA, a, "center"))
        bola_txt(c, t, C[kr] + 0.9, res, x, 790, 120 if i == 0 else 90, 70 if i == 0 else 56, E.COR if i == 0 else TINTA2)
    if t >= C["s06.b"]:
        M.line(c, W / 2, 300, W / 2, 900, FIO, ep(t, C["s06.b"], 0.4), 3)
    E.frase(c, t, C["s06.f"], [("4×", "g", 60, TINTA), ("o", "i", 62), ("tempo", "i", 62), ("→", "g", 60, TINTA2)], 560, 1000, "left", 0.1)
    E.foco(c, t, C["s06.f"] + 0.6, 0.4, lambda a: E.formula(c, "1/4 da potência", 960, 1000, 60, "g", COR, a))


# ---------------- unidades ----------------
def b_unidades(c, t, C, b):
    def s07():
        E.frase(c, t, C["s07"], ps("potências grandes:", "i", 72), XE, 210, passo=0.12)
        linhas = (("s07.a", "1 kW", "= 1.000 W", "quilowatt", False), ("s07.b", "1 cv", "≈ 735 W", "cavalo-vapor", True), ("s07.c", "1 hp", "≈ 746 W", "do inglês horsepower", True))
        for i, (k, u, v, nome, fora) in enumerate(linhas):
            y = 400 + i * 200
            E.foco(c, t, C[k], 0.5, lambda a, u=u, y=y: E.formula(c, u, XE + 40, y, 110, "g", COR, a))
            E.foco(c, t, C[k] + 0.3, 0.5, lambda a, v=v, y=y: E.formula(c, v, XE + 360, y, 110, "g", TINTA, a))
            E.foco(c, t, C[k] + 0.6, 0.4, lambda a, nome=nome, y=y: E.escreve(c, nome, XE + 1000, y - 10, 54, "i", TINTA2, a))
            if fora:
                pilula_em(c, t, C[k] + 0.9, "fora do SI", XE + 1200, y + 50, 36, ERRADO)
    E.saida(c, t, C["s08"] - 0.1, s07)
    if t < C["s08"]:
        return
    E.foco(c, t, C["s08.a"], 0.5, lambda a: F.medida(c, 100, "cv", XE, 300, 110, COR, a))
    E.foco(c, t, C["s08.b"], 0.5, lambda a: E.formula(c, "= 100 · 735", XE + 400, 300, 100, "g", TINTA, a))
    E.foco(c, t, C["s08.c"], 0.5, lambda a: E.formula(c, "= 73.500 W", XE + 400, 460, 100, "g", TINTA, a))
    bola_txt(c, t, C["s08.d"], "73,5 kW", 1560, 400, 150, 66)
    E.foco(c, t, C["s08.e"], 0.5, lambda a: E.formula(c, "100 hp = 100 · 746 = 74.600 W = 74,6 kW", W / 2, 720, 64, "g", TINTA2, a, "center"))
    pilula_em(c, t, C["s08.f"], "na prova: use o valor do enunciado", W / 2, 900, 50, TINTA)


# ---------------- rendimento ----------------
def b_rendimento(c, t, C, b):
    def s09():
        E.frase(c, t, C["s09"], ps("nenhuma máquina aproveita", "i", 70) + [("tudo", "g", 66, COR)], XE, 200, passo=0.12)
        fluxo(c, t, C["s09.a"], 260, 520, 1000, 800, "1.000 W", "800 W", "200 W", t_util=C["s09.b"], t_perda=C["s09.c"])
        pilula_em(c, t, C["s09.d"], "dissipada: a que se perde", 1450, 960, 48, TINTA2)
    E.saida(c, t, C["s10"] - 0.1, s09)
    if C["s10"] <= t < C["s11"]:
        def s10():
            E.frase(c, t, C["s10.a"], [("rendimento", "g", 90, COR), ("=", "g", 90), ("útil", "i", 96), ("÷", "g", 90), ("total", "i", 96)], XE, 220, passo=0.14)
            F.formula_legenda(c, t, C["s10.b"], "η = f{P útil}{P total}", [("η", "rendimento (eta)", None)], XE, 480, 120, tl=[C["s10.b"] + 1.6])
            E.foco(c, t, C["s10.c"], 0.5, lambda a: E.formula(c, "η = f{800}{1.000}", 1100, 480, 110, "g", TINTA, a))
            E.foco(c, t, C["s10.d"], 0.5, lambda a: E.formula(c, "= 0,8", 1100, 720, 110, "g", TINTA, a))
            bola_txt(c, t, C["s10.e"], "80 %", 1600, 690, 120, 70)
        E.saida(c, t, C["s11"] - 0.1, s10)
    if t < C["s11"]:
        return
    E.frase(c, t, C["s11"], ps("repare", "i", 84, COR), XE, 220)
    E.frase(c, t, C["s11.a"], [("sem", "g", 72), ("unidade:", "g", 72)], XE, 400, passo=0.12)
    E.foco(c, t, C["s11.a"] + 0.6, 0.5, lambda a: E.formula(c, "f{W}{W}", 900, 400, 90, "g", TINTA2, a))
    E.frase(c, t, C["s11.b"], ps("com joule no lugar do watt:", "i", 64) + [("igual", "g", 60)], XE, 590, passo=0.1)
    E.foco(c, t, C["s11.b"] + 1.2, 0.5, lambda a: E.formula(c, "η = f{τ útil}{τ total}", 1250, 600, 70, "g", TINTA2, a))
    E.frase(c, t, C["s11.c"], [("nunca", "i", 80), ("passa", "i", 80), ("de", "i", 80), ("100 %", "g", 90, COR)], XE, 860, passo=0.12)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s12"], [("cuidado", "g", 96, ERRADO)], XE, 200)
    E.frase(c, t, C["s12.a"], ps("dividir ao contrário", "i", 76), XE + 480, 200, passo=0.12)
    E.foco(c, t, C["s12.b"], 0.5, lambda a: E.formula(c, "η = f{1.000}{800} = 1,25", 560, 480, 100, "g", ERRADO, a, "center"))
    E.foco(c, t, C["s12.c"], 0.5, lambda a: E.formula(c, "= 125 %", 560, 680, 120, "g", ERRADO, a, "center"))
    if t >= C["s13.a"]:
        E.risco(c, 330, 690, 790, 580, t, C["s13.a"], largura=12)
    E.frase(c, t, C["s13.a"], [("mais", "i", 64), ("de", "i", 64), ("100 %:", "g", 60), ("impossível", "g", 60, ERRADO)], 560, 850, "center", 0.12)
    E.frase(c, t, C["s13.b"], ps("o útil é o", "i", 66) + [("menor", "g", 62, COR)], 1450, 360, "center", 0.12)
    E.foco(c, t, C["s13.c"], 0.5, lambda a: E.formula(c, "η = f{800}{1.000} = 80 %", 1450, 560, 90, "g", CERTO, a, "center"))
    E.foco(c, t, C["s13.c"] + 0.4, 0.5, lambda a: E.selo(c, 1450, 760, 60, True, a))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def s14():
        E.frase(c, t, C["s14"], ps("agora, o atalho", "i", 76, CLARO), W / 2, 170, "center")
        E.frase(c, t, C["s14"] + 1.0, ps("força e velocidade constantes, para o mesmo lado", "i", 56, CLARO), W / 2, 300, "center", 0.08)
        E.frase(c, t, C["s14.a"], [("potência", "g", 76, BR), ("=", "g", 76, CLARO), ("força", "g", 76, BR), ("×", "g", 76, CLARO), ("velocidade", "g", 76, BR)],
                W / 2, 470, "center", 0.12)
        E.foco(c, t, C["s14.b"], 0.6, lambda a: (E.bola(c, W / 2, 740, 230 * ease_back(prog(t, C["s14.b"], 0.6)), a=a),
                                                 E.formula(c, "P = F · v", W / 2, 775, 96, "g", BR, a, "center")))
    E.saida(c, t, C["s15"] - 0.1, s14)
    if t < C["s15"]:
        return
    E.foco(c, t, C["s15.a"], 0.5, lambda a: E.formula(c, "P = f{τ}{Δt} = f{F · d}{Δt}", 330, 260, 80, "g", BR, a))
    E.foco(c, t, C["s15.b"], 0.5, lambda a: E.formula(c, "= F · v", 1240, 260, 80, "g", CLARO, a))
    E.foco(c, t, C["s15.b"] + 0.4, 0.4, lambda a: E.formula(c, "d ÷ Δt = v", 1240, 360, 50, "b", CLARO, a))
    y = 640
    if t >= C["s15.c"]:
        F.chao(c, 260, 1000, y, ep(t, C["s15.c"], 0.4), True)
    E.foco(c, t, C["s15.c"], 0.5, lambda a: F.carrinho(c, 600, y, 300, a=a))
    F.vetor(c, t, C["s15.c"] + 0.4, (780, y - 200), (1000, y - 200), "v", "20 m/s", F.VEL, 9, escuro=True, size=50)
    E.foco(c, t, C["s15.c"] + 1.0, 0.4, lambda a: F.medida(c, "1.000", "N", 300, y - 200, 56, BR, a, escuro=True))
    E.foco(c, t, C["s15.c"] + 1.0, 0.4, lambda a: E.escreve(c, "F =", 180, y - 200, 56, "g", CLARO, a))
    E.foco(c, t, C["s15.d"], 0.5, lambda a: E.formula(c, "P = 1.000 · 20 = 20.000 W = 20 kW", W / 2, y + 130, 70, "g", BR, a, "center"))
    E.frase(c, t, C["s15.e"], ps("velocidade muda?", "i", 60, CLARO) + [("F · v", "g", 56, BR)] + ps("= potência daquele instante", "i", 60, CLARO),
            W / 2, 880, "center", 0.1)
    E.frase(c, t, C["s15.e"] + 2.4, ps("para a média:", "i", 60, CLARO) + [("τ ÷ Δt", "g", 56, BR)], W / 2, 980, "center", 0.1)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s16"], ps("hora de testar", "i", 72, COR), XE, 200)
    E.frase(c, t, C["s16.a"], [("recebe", "i", 72), ("2.000 W", "g", 68)], XE, 360, passo=0.12)
    E.frase(c, t, C["s16.b"], [("em", "i", 72), ("20 s", "g", 68)], XE, 470, passo=0.12)
    E.frase(c, t, C["s16.c"], [("trabalho", "i", 72), ("útil:", "i", 72), ("30.000 J", "g", 68, COR)], XE, 580, passo=0.12)
    E.frase(c, t, C["s16.d"], [("potência", "i", 70), ("útil?", "g", 66, COR)], XE, 760, passo=0.12)
    E.frase(c, t, C["s16.d"] + 1.2, [("rendimento?", "g", 66, COR)], XE, 860)
    if t < C["s17"]:
        E.foco(c, t, C["s16.a"], 0.5, lambda a: (M.rrect(c, 1250, 380, 360, 300, 40, TINTA, a), centro(c, "motor", 1430, 550, 64, "g", BR, a)))
        E.foco(c, t, C["s16.a"] + 0.3, 0.5, lambda a: F.seta(c, 1000, 530, 1240, 530, TINTA2, a, 16))
    else:
        E.relogio(c, t, C["s17.a"], cx=1460, cy=440, r=200)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    def s18():
        E.frase(c, t, C["s18.a"], [("potência", "i", 70), ("útil", "g", 66, COR), ("=", "g", 66), ("τ útil", "g", 66), ("÷", "g", 66), ("Δt", "g", 66)], XE, 240, passo=0.12)
        E.foco(c, t, C["s18.b"], 0.5, lambda a: E.formula(c, "P útil = f{30.000}{20}", W / 2, 500, 110, "g", TINTA, a, "center"))
        bola_txt(c, t, C["s18.c"], "1.500 W", W / 2, 790, 140, 64)
    E.saida(c, t, C["s19"] - 0.1, s18)
    if t < C["s19"]:
        return
    E.foco(c, t, C["s19.a"], 0.5, lambda a: E.formula(c, "η = f{1.500}{2.000}", XE, 280, 96, "g", TINTA, a))
    E.foco(c, t, C["s19.b"], 0.5, lambda a: E.formula(c, "= 0,75 =", XE + 620, 280, 96, "g", TINTA, a))
    bola_txt(c, t, C["s19.b"] + 0.6, "75 %", 1580, 250, 110, 64)
    fluxo(c, t, C["s19.a"] + 0.3, 260, 640, 2000, 1500, "2.000 W", "1.500 W", "500 W", t_util=C["s19.a"] + 0.9, t_perda=C["s19.c"], esc=0.14)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s20"], [("resumindo", "i", 92, COR)], W / 2, 180, "center")
        itens = (("s20.a", [("P = τ ÷ Δt", "g", 70), ("em", "i", 70), ("watt", "g", 70, COR)]),
                 ("s20.b", [("1 kW = 1.000 W", "g", 70), ("·", "g", 70, TINTA2), ("1 cv ≈ 735 W", "g", 70)]),
                 ("s20.c", [("η = útil ÷ total,", "g", 70), ("nunca", "i", 70), ("> 100 %", "g", 70, COR)]))
        for i, (k, partes) in enumerate(itens):
            y = 380 + i * 190
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 300, y - 26, 52, a=a), centro(c, str(i + 1), 300, y - 4, 60, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, partes, 400, y, passo=0.12)
    E.saida(c, t, C["s21"] - 0.1, resumo)
    if t < C["s21"]:
        return
    E.frase(c, t, C["s21"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C["s21.a"], [("energia", "g", 120, COR), ("cinética", "g", 120, COR)], XE, 420)
    E.frase(c, t, C["s21.a"] + 0.6, ps("a energia do movimento", "i", 64, TINTA2), XE, 520, passo=0.1)
    E.frase(c, t, C["s21.b"], [("2×", "g", 100), ("a", "i", 90), ("velocidade", "i", 90), ("→", "g", 90, TINTA2), ("4×", "g", 100, COR)], XE, 720, passo=0.14)
    E.foco(c, t, C["s21.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 420, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s21.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(720, 445, p), ep(t, C["s21.c"] + 0.2, 0.4))
    E.frase(c, t, C["s21.d"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1570, 990, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, potencia=b_potencia, unidades=b_unidades, rendimento=b_rendimento, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
