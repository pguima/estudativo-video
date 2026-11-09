"""Visual — Estudativo · FIS-OND-001: oscilações, pêndulo e mola. Primeira aula da trilha Ondas e Som.

Segue a LINGUAGEM VISUAL DA FÍSICA (docstring do visual.py da FIS-CIN-001: grandeza em itálico + letra pesada laranja,
medida = número pesado + unidade cinza, fórmula nova com F.formula_legenda, certo/errado, atalho no palco escuro).

LINGUAGEM VISUAL DA TRILHA ONDAS E SOM (FIS-OND-*; as aulas seguintes copiam daqui):
- OSCILADOR: o que oscila (bola do pêndulo, bloco da mola, fonte que balança a corda) é laranja (COR); teto, parede, chão,
  fio e mola em tinta. O vai e volta é animado de verdade (F.oscila), com a posição de equilíbrio em linha tracejada e a
  amplitude como cota com a letra A. O período aparece com F.cronometro ou com a letra T pesada.
- ONDA: F.onda em laranja sobre eixo tracejado. Crista e vale com rótulo em itálico cinza; a amplitude é a seta vertical
  do eixo à crista (A); o comprimento de onda é a cota de crista a crista, com λ na grotesca pesada laranja.
  Segunda onda (interferência) em azul F.NEG; a soma, em tinta. Onda longitudinal = faixas verticais que se apertam e se
  afastam (compressão e rarefação), não senoide.
- SOM: fonte com frentes de onda em arcos concêntricos laranja (Doppler: os círculos saem de pontos que andam).
  Grave/agudo = onda mais espaçada/apertada; forte/fraco = onda mais alta/baixa, sempre lado a lado para comparar.
- ESPECTRO: uma faixa horizontal com as sete regiões (rádio → gama), a frequência crescendo para a direita (seta),
  o arco-íris só na fatia da luz visível; ionizante marcado com a pílula vermelha.
- CONTA: em pilha, uma linha por fala (conta()), em tinta, com o passo da vez em laranja; o resultado final na esfera
  laranja (bola_txt). Letra grega (λ, π, Δ) e o sinal "=" sempre na grotesca ("g" ou "b"): a itálica não tem esses glifos.
- PROPORÇÃO (raiz, dobro, metade): setas com a pílula "×4", "×2" (pílula()), como as pontes da Matemática.
Todo instante vem de C[...] (marcadores do roteiro), para acompanhar a voz real quando ela chegar."""
import math

import editorial as E
import fisica as F
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Física", "Ondas e Som")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_FIS-OND-001_oscilacoes_pendulo_e_mola.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("oscilar", "pendulo", "mola", "atalho", "questao", "fim"))
BR = "#FFFFFF"

# todas as contas da aula (π = 3 quando a prova manda; raiz conferida pelo quadrado)
assert abs(0.4 / 10 - 0.04) < 1e-12 and abs(0.2 * 0.2 - 0.04) < 1e-12 and abs(2 * 3 * 0.2 - 1.2) < 1e-12
assert abs(0.5 / 50 - 0.01) < 1e-12 and abs(0.1 * 0.1 - 0.01) < 1e-12 and abs(2 * 3 * 0.1 - 0.6) < 1e-12
assert abs(1.6 / 10 - 0.16) < 1e-12 and abs(0.4 * 0.4 - 0.16) < 1e-12 and abs(6 * 0.4 - 2.4) < 1e-12 and abs(2.4 - 2 * 1.2) < 1e-12
assert abs(math.pi ** 2 - 10) < 0.14 and abs(2 * math.pi * math.sqrt(1 / 10) - 2) < 0.02 and abs(2 * math.pi * math.sqrt(4 / 10) - 4) < 0.03
assert abs(9 / 100 - 0.09) < 1e-12 and abs(0.3 * 0.3 - 0.09) < 1e-12 and abs(6 * 0.3 - 1.8) < 1e-12
assert abs(36 / 100 - 0.36) < 1e-12 and abs(0.6 * 0.6 - 0.36) < 1e-12 and abs(6 * 0.6 - 3.6) < 1e-12 and abs(3.6 - 2 * 1.8) < 1e-12


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças desta aula ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def bola_txt(c, t, t0, s, cx, cy, r, size, cor=None):
    """resposta na esfera: "1,2 s" com a unidade menor"""
    v, _, u = s.partition(" ")
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r * ease_back(prog(t, t0, 0.5)), cor, a),
                                     F.medida(c, v, u, cx, cy + size * 0.36, size, E.SOBRE, a, "center", cor_u=E.SOBRE)))


def conta(c, t, linhas, x, y0, dy, size, align="left", escuro=False):
    """conta em pilha: linhas = [(instante, fórmula[, cor])]; a linha da vez fica laranja até a próxima chegar"""
    tinta = BR if escuro else TINTA
    for i, ln in enumerate(linhas):
        ti, s = ln[0], ln[1]
        prox = linhas[i + 1][0] if i + 1 < len(linhas) else 1e9
        cor = ln[2] if len(ln) > 2 else ((CLARO if escuro else COR) if t < prox else tinta)
        E.formula_em(c, t, ti, s, x, y0 + i * dy, size, "g", cor, align)


def pilula(c, t, t0, s, cx, cy, size, fundo=None, est="g"):
    E.foco(c, t, t0, 0.4, lambda a: E.pilula(c, s, cx, cy, size, est, fundo=fundo, a=a, cor=BR))


def lembrete2(c, t, C, cena, itens, desenhos):
    """lembrete de duas coisas: itens = [(cue, linha fina, linha forte)]; desenhos[i](a, x, y) desenha à direita da caixa"""
    E.frase(c, t, C[cena] + 0.2, ps("você precisa de", "i", 84), XE, 410, passo=0.14)
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


def pendulo_vivo(c, t, t0, px, py, L, amp, periodo, r=40, rotulo=None, a_eq=0.0, tl=None):
    """pêndulo que já oscila (ângulo = F.oscila); a_eq > 0 mostra a vertical tracejada do equilíbrio"""
    ang = F.oscila(t, t0 + 0.6, amp, periodo)
    if a_eq > 0:
        M.line(c, px, py, px, py + L + r + 30, TINTA2, 0.5 * a_eq, 4, dash=E.TRACO)
    F.pendulo(c, t, t0, px, py, L, ang, r=r)
    if rotulo:
        g = math.radians(ang)
        bx, by = px + L * math.sin(g), py + L * math.cos(g)
        E.foco(c, t, t0 + 0.8, 0.4, lambda a: E._meio(c, rotulo, bx, by, r * 0.62, "g", E.SOBRE, a))
    return ang


def mola_bloco(c, t, t0, xp, y, x_eq, amp, periodo, w=170, h=130, rotulo=None, a=1.0, parado=False):
    """parede em xp, mola até o bloco e bloco que oscila em volta de x_eq sobre o chão em y; devolve o x do centro"""
    if t < t0:
        return x_eq
    q = ep(t, t0, 0.5) * a
    x = x_eq if parado else x_eq + F.oscila(t, t0 + 0.6, amp, periodo)
    F.parede(c, xp, y - 260, y, -1, q)
    F.chao(c, xp - 10, x_eq + amp + w + 120, y, q)
    F.mola(c, xp, y - h / 2, x - w / 2, y - h / 2, voltas=9, larg_=46, a=q, largura=6)
    F.bloco(c, x, y - h / 2, w, h, rotulo, a=q, size=46)
    return x


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def um():
        for i, (k, m) in enumerate((("s01.b", "1 kg"), ("s01.c", "10 kg"))):
            px = 1180 + i * 420
            if t >= C[k]:
                pendulo_vivo(c, t, C[k] if i == 0 else C["s01.b"] + 0.02, px, 170, 520, 22, 2.0, r=48 + 22 * i, rotulo=m)
        E.frase(c, t, C["s01.a"], ps("duas bolas,", "i", 84), XE, 300, passo=0.12)
        E.frase(c, t, C["s01.a"] + 0.7, ps("mesmo", "i", 84) + [("fio", "g", 84, COR)], XE, 410, passo=0.12)
        E.frase(c, t, C["s01.d"], ps("qual vai e volta", "i", 70), XE, 600, passo=0.1)
        E.frase(c, t, C["s01.d"] + 0.6, [("mais", "g", 80), ("depressa?", "g", 80, COR)], XE, 700, passo=0.12)
        E.frase(c, t, C["s01.e"], [("nenhuma", "g", 120, CERTO)], XE, 880)
        E.frase(c, t, C["s01.e"] + 0.8, ps("mesmo tempo", "i", 70, TINTA2), XE, 970, passo=0.12)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t < C["s02"]:
        return
    tb = C["s02.a"] + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1480, 540, 330 * ease_back(prog(t, tb, 0.8)), giro=12 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 88), XE, 280, passo=0.14)
    E.frase(c, t, C["s02.a"] + 1.0, [("o tempo do", "i", 74), ("vai e volta", "g", 74, COR)], XE, 400, passo=0.14)
    for i, (k, s) in enumerate((("s02.b", "no pêndulo"), ("s02.c", "na mola"))):
        y = 580 + i * 160
        E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, XE + 40, y - 30, 38, a=a), centro(c, str(i + 1), XE + 40, y - 8, 48, "g", BR, a)))
        E.frase(c, t, C[k] + 0.1, [(s, "g", 84)], XE + 110, y)
    E.frase(c, t, lerp(C["s02.c"], C["s02.end"], 0.5), ps("o que muda e o que não muda", "i", 60, TINTA2), XE, 920, passo=0.1)


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    def periodo(a, x, y):
        F.cronometro(c, x - 30, y - 30, 70, 15, a, "")

    def hooke(a, x, y):
        F.parede(c, x - 150, y - 60, y + 40, -1, a)
        F.mola(c, x - 150, y - 10, x + 20, y - 10, voltas=6, larg_=34, a=a, largura=5)
        F.bloco(c, x + 70, y - 10, 90, 80, a=a)
    lembrete2(c, t, C, "s03", (("s03.b", "o período T,", "o tempo de uma volta"), ("s03.c", "a força da mola,", "F = k · x")), (periodo, hooke))


# ---------------- oscilação ----------------
def b_oscilar(c, t, C, b):
    px, py, L = 1340, 170, 560
    if t < C["s05"]:
        def s04():
            E.frase(c, t, C["s04"], ps("vai e volta,", "i", 84), XE, 280, passo=0.12)
            E.frase(c, t, C["s04"] + 1.2, ps("sempre pelo mesmo caminho", "i", 60, TINTA2), XE, 370, passo=0.1)
            E.frase(c, t, C["s04.a"], [("está", "i", 84), ("oscilando", "g", 84, COR)], XE, 490, passo=0.12)
            amp = 24
            ang = pendulo_vivo(c, t, C["s04"], px, py, L, amp, 2.4, r=46, a_eq=ep(t, C["s04.b"], 0.5))
            E.foco(c, t, C["s04.c"], 0.5, lambda a: E.pilula(c, "equilíbrio", px, py + L + 120, 44, "b", fundo=TINTA, a=a))
            E.frase(c, t, C["s04.c"], ps("posição de", "i", 70) + [("equilíbrio", "g", 70)], XE, 690, passo=0.12)
            if t >= C["s04.d"]:  # amplitude: arco do meio até o extremo
                q = ep(t, C["s04.d"], 0.6)
                E.arco(c, px, py, L + 70, 90, -amp * q, COR, 7, 1.0)
                g = math.radians(amp)
                E.foco(c, t, C["s04.d"] + 0.4, 0.4, lambda a: E._meio(c, "A", px + (L + 120) * math.sin(g / 2), py + (L + 120) * math.cos(g / 2), 72, "g", COR, a))
                M.line(c, px, py, px + (L + 40) * math.sin(g), py + (L + 40) * math.cos(g), TINTA2, 0.5 * q, 4, dash=E.TRACO)
            E.frase(c, t, C["s04.d"], ps("maior afastamento:", "i", 64), XE, 860, passo=0.1)
            E.frase(c, t, C["s04.d"] + 0.8, [("amplitude", "g", 84, COR), ("A", "g", 84, COR)], XE, 970, passo=0.2)
        E.saida(c, t, C["s05"] - 0.1, s04)
        return
    # s05: uma oscilação completa = 4 trechos; o período T
    cx, y = 1180, 560
    xs = (cx, cx + 360, cx, cx - 360, cx)
    M.line(c, cx - 420, y + 90, cx + 420, y + 90, TINTA2, 0.5 * ep(t, C["s05"], 0.4), 4) if t >= C["s05"] else None
    for k, x in enumerate((cx - 360, cx, cx + 360)):
        E.foco(c, t, C["s05"] + 0.1 * k, 0.4, lambda a, x=x: M.line(c, x, y + 70, x, y + 110, TINTA2, a, 4))
    ti = C["s05"] + 0.2
    for k in range(4):  # as quatro partes da volta
        tk = lerp(ti, C["s05.b"] - 0.3, k / 4)
        q = ease_io(prog(t, tk, 0.5))
        if q > 0:
            yy = y - 40 - 50 * k
            F.seta(c, xs[k], yy, lerp(xs[k], xs[k + 1], q), yy, COR if k == 3 else TINTA, 1.0, 7, 26, 1.0)
    fx = cx
    if t < C["s05.b"]:
        tt = (t - ti) / (C["s05.b"] - 0.3 - ti) * 4
        k = max(0, min(3, int(tt)))
        fx = lerp(xs[k], xs[k + 1], ease_io(max(0.0, min(1.0, tt - k)))) if tt > 0 else cx
    E.bola(c, fx, y + 50, 40, a=ep(t, C["s05"], 0.4))
    E.frase(c, t, C["s05.a"], ps("uma oscilação", "i", 76) + [("completa", "g", 76)], XE, 250, passo=0.12)
    E.frase(c, t, C["s05.b"], [("período", "i", 84), ("T", "g", 96, COR)], XE, 820, passo=0.15)
    E.foco(c, t, C["s05.b"] + 0.5, 0.5, lambda a: F.cronometro(c, 1620, 820, 80, 12, a, ""))
    E.foco(c, t, C["s05.c"], 0.5, lambda a: E.pilula(c, "movimento harmônico simples", W / 2, 990, 52, "g", fundo=E.COR, a=a))


# ---------------- pêndulo ----------------
def b_pendulo(c, t, C, b):
    if t < C["s07"]:
        px, py, L = 1300, 150, 560
        E.frase(c, t, C["s06.a"], [("pêndulo", "g", 110, COR)], XE, 330)
        E.frase(c, t, C["s06.a"] + 0.7, ps("uma bolinha num fio", "i", 70), XE, 440, passo=0.12)
        # a bola sai do meio, é solta em s06.b e oscila
        if t < C["s06.b"]:
            ang = 26 * ease_io(prog(t, C["s06.a"] + 1.4, 0.8))
            F.pendulo(c, t, C["s06.a"], px, py, L, ang, r=48)
        else:
            ang = F.oscila(t, C["s06.b"], 26, 2.4)
            F.pendulo(c, t, C["s06.a"], px, py, L, ang, r=48)
            g = math.radians(ang)
            P = (px + L * math.sin(g), py + L * math.cos(g))
            F.vetor(c, t, C["s06.b"], (P[0], P[1] + 52), (P[0], P[1] + 230), "P", None, E.COR, 9, lado=-1)
        E.frase(c, t, C["s06.b"], ps("o", "i", 70) + [("peso", "g", 70)] + ps("puxa de volta", "i", 70), XE, 640, passo=0.12)
        E.frase(c, t, C["s06.c"], ps("e sobe do", "i", 70) + [("outro lado", "g", 70, COR)], XE, 760, passo=0.12)
        return
    if t < C["s08"]:
        def s07():
            F.formula_legenda(c, t, C["s07.a"], "T = 2π · r{f{L}{g}}", [("L", "comprimento do fio", "m"), ("g", "gravidade: 10", "m/s^2"),
                                                                     ("π", "número fixo, perto de 3,14", None)],
                              XE, 330, 140, tl=[C["s07.b"], C["s07.c"], C["s07.d"]], size_l=58)
            E.foco(c, t, C["s07.a"] + 0.6, 0.5, lambda a: F.pendulo(c, 99, 0, 1560, 150, 420, 14, r=42))
            pilula(c, t, C["s07.e"], "prova: use π = 3", 1560, 840, 56, E.COR)
        E.saida(c, t, C["s08"] - 0.1, s07)
        return
    if t < C["s09"]:
        def s08():
            E.formula(c, "T = 2π · r{f{L}{g}}", W / 2, 300, 110, "g", TINTA, ep(t, C["s08"], 0.4), "center")
            E.frase(c, t, C["s08.a"], ps("não está na fórmula:", "i", 70), W / 2, 450, "center", 0.12)
            E.foco(c, t, C["s08.b"], 0.5, lambda a: E.escreve(c, "massa", W / 2 - 220, 600, 120, "g", ERRADO, a))
            if t >= C["s08.b"] + 0.5:
                E.risco(c, W / 2 - 240, 610, W / 2 + 230, 520, t, C["s08.b"] + 0.5, largura=12)
            E.frase(c, t, C["s08.c"], [("pesada:", "g", 56), ("mais", "i", 60), ("força", "g", 56, COR)], W / 2 - 420, 760, "center", 0.12)
            E.frase(c, t, C["s08.c"] + 1.4, [("e", "i", 60), ("mais", "i", 60), ("difícil", "g", 56, COR), ("de", "i", 60), ("mover", "i", 60)], W / 2 + 380, 760, "center", 0.12)
            E.foco(c, t, C["s08.c"] + 2.4, 0.4, lambda a: centro(c, "uma compensa a outra", W / 2, 860, 56, "i", TINTA2, a))
            pilula(c, t, C["s08.d"], "a amplitude também não entra (abertura pequena)", W / 2, 980, 46, TINTA, "b")
        E.saida(c, t, C["s09"] - 0.1, s08)
        return
    # s09: o pêndulo de 0,4 m
    E.foco(c, t, C["s09"], 0.5, lambda a: E.formula(c, "T = 2π · r{f{L}{g}}", XE, 220, 84, "g", TINTA2, a))
    E.foco(c, t, C["s09.a"], 0.5, lambda a: F.medida(c, "0,4", "m", 1450, 230, 84, COR, a))
    E.foco(c, t, C["s09.a"], 0.5, lambda a: E.escreve(c, "L =", 1290, 230, 84, "g", TINTA, a))
    conta(c, t, [(C["s09.b"], "0,4 ÷ 10 = 0,04"), (C["s09.c"], "r{0,04} = 0,2"), (C["s09.d"], "T = 2 · 3 · 0,2")], XE, 420, 170, 100)
    E.foco(c, t, C["s09.c"] + 1.0, 0.4, lambda a: E.formula(c, "(0,2 · 0,2 = 0,04)", XE + 720, 590, 58, "b", TINTA2, a))
    bola_txt(c, t, C["s09.e"], "1,2 s", 1500, 760, 150, 84)


# ---------------- mola ----------------
def b_mola(c, t, C, b):
    xp, yc = 980, 760
    if t < C["s11"]:
        E.frase(c, t, C["s10.a"], [("mola", "g", 110, COR)], XE, 300)
        E.frase(c, t, C["s10.a"] + 0.6, ps("bloco, mola e chão liso", "i", 64), XE, 400, passo=0.1)
        if t >= C["s10.a"]:
            if t < C["s10.b"]:  # puxa
                q = ease_io(prog(t, C["s10.a"] + 1.4, 0.8))
                mola_bloco(c, t, C["s10.a"], xp, yc, 1390 + 170 * q, 0, 2.6, parado=True)
            else:
                # solto em s10.b: começa no extremo (+170) e oscila
                x = 1390 + 170 * math.cos(2 * math.pi * (t - C["s10.b"]) / 2.6)
                F.parede(c, xp, yc - 260, yc, -1)
                F.chao(c, xp - 10, 1390 + 170 + 290, yc)
                F.mola(c, xp, yc - 65, x - 85, yc - 65, voltas=9, larg_=46, largura=6)
                F.bloco(c, x, yc - 65, 170, 130)
            M.line(c, 1390, yc - 210, 1390, yc + 50, TINTA2, 0.45 * ep(t, C["s10.a"] + 0.6, 0.4), 4, dash=E.TRACO)
        E.frase(c, t, C["s10.b"], ps("a mola", "i", 70) + [("puxa", "g", 70)] + ps("de volta", "i", 70), XE, 560, passo=0.12)
        E.frase(c, t, C["s10.c"], [("aperta", "g", 70)] + ps("e ela", "i", 70) + [("empurra", "g", 70, COR)], XE, 680, passo=0.12)
        return
    if t < C["s12"]:
        def s11():
            F.formula_legenda(c, t, C["s11.a"], "T = 2π · r{f{m}{k}}", [("m", "massa do bloco", "kg"), ("k", "constante da mola", "N/m")],
                              XE, 300, 140, tl=[C["s11.b"], C["s11.c"]], size_l=58)
            pilula(c, t, C["s11.c"] + 1.6, "mola dura, k grande", XE + 300, 640, 46, TINTA, "b")
            E.frase(c, t, C["s11.d"], [("a", "i", 70), ("massa", "g", 70, CERTO), ("entra", "g", 70, CERTO)], XE, 800, passo=0.12)
            E.frase(c, t, C["s11.e"], [("a", "i", 70), ("gravidade", "g", 70, ERRADO), ("não", "g", 70, ERRADO), ("entra", "g", 70, ERRADO)], XE, 920, passo=0.12)
            E.foco(c, t, C["s11.a"] + 0.6, 0.5, lambda a: (F.parede(c, 1240, 330, 590, -1, a), F.chao(c, 1230, 1800, 590, a),
                                                         F.mola(c, 1240, 525, 1480, 525, voltas=7, larg_=40, a=a, largura=5),
                                                         F.bloco(c, 1560, 525, 160, 130, "m", a=a, size=60)))
            if t >= C["s11.e"]:  # pendurada: mesmo período
                q = ep(t, C["s11.e"] + 0.4, 0.5)
                F.teto(c, 1550, 1790, 690, q)
                F.mola(c, 1670, 690, 1670, 860, voltas=6, larg_=40, a=q, largura=5)
                F.bloco(c, 1670, 920, 130, 110, "m", a=q, size=52)
        E.saida(c, t, C["s12"] - 0.1, s11)
        return
    E.foco(c, t, C["s12"], 0.5, lambda a: E.formula(c, "T = 2π · r{f{m}{k}}", XE, 220, 84, "g", TINTA2, a))
    E.foco(c, t, C["s12.a"], 0.5, lambda a: (E.escreve(c, "m =", 1200, 200, 72, "g", TINTA, a), F.medida(c, "0,5", "kg", 1340, 200, 72, COR, a)))
    E.foco(c, t, C["s12.b"], 0.5, lambda a: (E.escreve(c, "k =", 1200, 300, 72, "g", TINTA, a), F.medida(c, "50", "N/m", 1340, 300, 72, COR, a)))
    conta(c, t, [(C["s12.c"], "0,5 ÷ 50 = 0,01"), (C["s12.d"], "r{0,01} = 0,1"), (C["s12.e"], "T = 2 · 3 · 0,1")], XE, 470, 160, 100)
    E.foco(c, t, C["s12.d"] + 0.8, 0.4, lambda a: E.formula(c, "(0,1 · 0,1 = 0,01)", XE + 700, 630, 58, "b", TINTA2, a))
    bola_txt(c, t, C["s12.f"], "0,6 s", 1500, 760, 150, 84)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s13"], [("cuidado", "g", 96, ERRADO)], XE, 190)

    def errado():
        E.frase(c, t, C["s13.a"], [("2", "g", 110), ("L", "g", 110, COR), ("→", "g", 110, TINTA2), ("2", "g", 110), ("T?", "g", 110, ERRADO)], XE, 400, passo=0.2)
        if t >= C["s13.a"] + 1.4:
            E.risco(c, XE - 10, 410, XE + 640, 300, t, C["s13.a"] + 1.4, largura=12)
        E.foco(c, t, C["s13.b"], 0.5, lambda a: E.formula(c, "T = 2π · r{f{L}{g}}", 1100, 400, 110, "g", TINTA, a))
        q = ep(t, C["s13.b"] + 0.5, 0.4)
        if q > 0:
            E.caixa_pontilhada(c, 1440, 280, 200, 170, q, prog_=q)
            E.foco(c, t, C["s13.b"] + 0.7, 0.4, lambda a: centro(c, "dentro da raiz", 1540, 520, 46, "i", COR, a))
        E.frase(c, t, C["s13.c"], [("4", "g", 110, CERTO), ("L", "g", 110, COR), ("→", "g", 110, TINTA2), ("2", "g", 110, CERTO), ("T", "g", 110)], XE, 700, passo=0.2)
    E.saida(c, t, C["s13.d"] - 0.1, errado)
    if t < C["s13.d"]:
        return
    E.foco(c, t, C["s13.d"], 0.5, lambda a: (E.escreve(c, "L =", XE, 360, 84, "g", TINTA, a), F.medida(c, "1,6", "m", XE + 170, 360, 84, COR, a),
                                             E.escreve(c, "(4 × 0,4)", XE + 500, 360, 60, "b", TINTA2, a)))
    conta(c, t, [(C["s13.e"], "1,6 ÷ 10 = 0,16 → r{0,16} = 0,4"), (C["s13.f"], "T = 6 · 0,4 = 2,4 s")], XE, 540, 180, 90)
    E.frase(c, t, C["s13.f"] + 1.4, [("2,4", "g", 90, CERTO), ("=", "g", 90, TINTA2), ("2", "g", 90), ("×", "g", 90, TINTA2), ("1,2", "g", 90)], XE, 920, passo=0.15)
    bola_txt(c, t, C["s13.f"] + 2.2, "×2", 1560, 880, 120, 90, CERTO)


# ---------------- atalho (palco) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    if t < C["s15"]:
        def s14():
            E.frase(c, t, C["s14"], ps("agora, o atalho", "i", 76, CLARO), W / 2, 170, "center")
            E.frase(c, t, C["s14.a"], [("o", "i", 80, CLARO), ("período", "g", 80, BR), ("anda", "i", 80, CLARO), ("com", "i", 80, CLARO), ("a", "i", 80, CLARO),
                                       ("raiz", "g", 80, BR)], W / 2, 320, "center", 0.12)
            for i, (k, de, para) in enumerate((("s14.b", "×4", "×2"), ("s14.c", "×9", "×3"))):
                y = 520 + i * 190
                E.foco(c, t, C[k], 0.5, lambda a, y=y, de=de: (E.escreve(c, "L ou m", 520, y + 25, 64, "i", CLARO, a),
                                                              E.pilula(c, de, 920, y, 70, "g", fundo=E.COR, a=a, cor=BR)))
                E.foco(c, t, C[k] + 0.5, 0.5, lambda a, y=y, para=para: (F.seta(c, 1030, y, 1230, y, CLARO, a, 8), E.escreve(c, "T", 1290, y + 30, 80, "g", BR, a),
                                                                        E.pilula(c, para, 1460, y, 70, "g", fundo=CERTO, a=a, cor=BR)))
            E.frase(c, t, C["s14.d"], [("×2", "g", 64, ERRADO)] + ps("no fio? não é quadrado:", "i", 64, CLARO) + [("faça a conta", "g", 60, BR)],
                    W / 2, 960, "center", 0.1)
        E.saida(c, t, C["s15"] - 0.1, s14)
        return
    E.frase(c, t, C["s15"], ps("e mais um", "i", 76, CLARO), W / 2, 170, "center")
    E.foco(c, t, C["s15.a"], 0.5, lambda a: E.formula(c, "π · π ≈ 9,87 ≈ 10 = g", W / 2, 340, 96, "g", BR, a, "center"))
    E.foco(c, t, C["s15.b"], 0.5, lambda a: E.formula(c, "T ≈ 2 · r{L}", W / 2, 560, 140, "g", BR, a, "center"))
    E.foco(c, t, C["s15.b"] + 0.6, 0.4, lambda a: centro(c, "na Terra, L em metros", W / 2, 680, 52, "i", CLARO, a))
    for i, (k, l_, tt) in enumerate((("s15.c", "1 m", "≈ 2 s"), ("s15.d", "4 m", "≈ 4 s"))):
        x = 620 + i * 680
        E.foco(c, t, C[k], 0.5, lambda a, x=x, l_=l_, tt=tt: (E.pilula(c, l_, x - 120, 830, 60, "g", fundo=E.COR, a=a, cor=BR),
                                                             E.escreve(c, tt, x + 10, 852, 72, "g", BR, a)))
    E.frase(c, t, lerp(C["s15.d"], C["s15.end"], 0.4), ps("só estimativa:", "i", 56, CLARO) + [("com π = 3,", "b", 52, BR), ("faça a conta", "b", 52, BR)], W / 2, 990, "center", 0.1)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s16"], ps("hora de testar", "i", 72, COR), XE, 200)
    E.frase(c, t, C["s16.a"], [("bloco", "i", 76)], XE, 350)
    E.foco(c, t, C["s16.a"] + 0.3, 0.5, lambda a: F.medida(c, 9, "kg", XE + 230, 350, 90, COR, a))
    E.frase(c, t, C["s16.a"] + 1.4, [("mola", "i", 76)], XE, 470)
    E.foco(c, t, C["s16.a"] + 1.7, 0.5, lambda a: F.medida(c, 100, "N/m", XE + 230, 470, 90, COR, a))
    pilula(c, t, C["s16.b"], "π = 3", XE + 140, 580, 52, TINTA)
    E.frase(c, t, C["s16.c"], [("período", "g", 76), ("T?", "g", 76, COR)], XE, 730, passo=0.12)
    E.frase(c, t, C["s16.d"], ps("e com", "i", 70) + [("36 kg?", "g", 70, COR)], XE, 860, passo=0.12)
    if t < C["s17"]:
        E.foco(c, t, C["s16.a"], 0.6, lambda a: (F.parede(c, 1080, 400, 700, -1, a), F.chao(c, 1070, 1820, 700, a),
                                                 F.mola(c, 1080, 625, 1440, 625, voltas=8, larg_=44, a=a, largura=6),
                                                 F.bloco(c, 1540, 625, 200, 150, "9 kg", a=a, size=52)))
    else:
        E.relogio(c, t, C["s17.a"], cx=1460, cy=440, r=200)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    def s18():
        E.foco(c, t, C["s18"], 0.5, lambda a: E.formula(c, "T = 2π · r{f{m}{k}}", XE, 220, 84, "g", TINTA2, a))
        conta(c, t, [(C["s18.a"], "9 ÷ 100 = 0,09"), (C["s18.b"], "r{0,09} = 0,3"), (C["s18.c"], "T = 2 · 3 · 0,3")], XE, 420, 170, 100)
        E.foco(c, t, C["s18.b"] + 1.0, 0.4, lambda a: E.formula(c, "(0,3 · 0,3 = 0,09)", XE + 700, 590, 58, "b", TINTA2, a))
        bola_txt(c, t, C["s18.d"], "1,8 s", 1500, 760, 150, 84)
    E.saida(c, t, C["s19"] - 0.1, s18)
    if t < C["s19"]:
        return
    E.frase(c, t, C["s19"], [("36", "g", 90), ("kg", "b", 66, F.UNID)], XE, 260, passo=0.1)
    E.foco(c, t, C["s19.a"], 0.5, lambda a: E.pilula(c, "×4 na massa", XE + 480, 232, 56, "g", fundo=E.COR, a=a))
    E.frase(c, t, C["s19.b"], [("período", "i", 76), ("×2", "g", 80, CERTO)], XE, 420, passo=0.12)
    E.foco(c, t, C["s19.c"], 0.5, lambda a: F.medida(c, "3,6", "s", XE, 600, 140, CERTO, a))
    conta(c, t, [(C["s19.d"], "36 ÷ 100 = 0,36 → r{0,36} = 0,6"), (C["s19.e"], "T = 6 · 0,6 = 3,6 s")], XE, 800, 150, 80)
    E.foco(c, t, C["s19.e"] + 0.6, 0.5, lambda a: E.selo(c, 1640, 820, 80, True, a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s20"], [("resumindo", "i", 92, COR)], W / 2, 180, "center")
        itens = (("s20.a", "pêndulo:", "T = 2π · r{f{L}{g}}", "sem a massa"),
                 ("s20.b", "mola:", "T = 2π · r{f{m}{k}}", "sem a gravidade"),
                 ("s20.c", "×4 na raiz:", "2T", ""))
        for i, (k, s1, f_, s2) in enumerate(itens):
            y = 380 + i * 220
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 300, y - 26, 52, a=a), centro(c, str(i + 1), 300, y - 4, 60, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, [(s1, "g", 70)], 400, y)
            E.formula_em(c, t, C[k] + 0.4, f_, 820, y, 84, "g", COR)
            if s2:
                E.frase(c, t, C[k] + 0.9, ps(s2, "i", 60, TINTA2), 1400, y, passo=0.1)
    E.saida(c, t, C["s21"] - 0.1, resumo)
    if t < C["s21"]:
        return
    E.frase(c, t, C["s21"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C["s21.a"], [("o", "i", 100), ("vai e volta", "g", 110, COR), ("viaja", "g", 110)], XE, 400, passo=0.15)
    F.onda(c, t, C["s21.b"], XE, 1250, 640, 70, 270, d=1.2, velocidade=120)
    E.foco(c, t, C["s21.b"] + 0.4, 0.4, lambda a: E.escreve(c, "ondas", XE, 820, 80, "g", TINTA, a))
    E.formula_em(c, t, C["s21.c"], "v = λ · f", XE + 330, 820, 90, "g", COR)
    E.foco(c, t, C["s21.d"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 420, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s21.d"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(720, 445, p), ep(t, C["s21.d"] + 0.2, 0.4))
    E.frase(c, t, C["s21.e"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1570, 990, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, oscilar=b_oscilar, pendulo=b_pendulo, mola=b_mola, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
