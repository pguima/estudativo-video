"""Visual — Estudativo · MAT-DIV-003: números primos e fatoração.
Peças da aula: cadeiras que se arrumam em fileiras (primo = só uma fila) e a tabela de divisões sucessivas do kit em uma coluna (montar + tabela + passos + produto).
Todo instante vem de C[...]: fala sem cue usa um ponto entre dois cues (lerp), para continuar certo com a voz real."""
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro, linha, montar, tabela, seta_primo, passos, produto
import motor as M
import skia

E.usar("Matemática", "Divisibilidade, MMC e MDC")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-DIV-003_primos_fatoracao.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("primo", "fatorar", "atalho", "questao", "fim"))
BR = "#FFFFFF"

T360 = montar((360,), (2, 2, 2, 3, 3, 5))
T126 = montar((126,), (2, 3, 3, 7))
G360 = dict(xs=(380,), xb=540, xp=640, y0=190, dy=118, s=92)  # tabela de uma coluna, 7 linhas
G126 = dict(xs=(380,), xb=540, xp=640, y0=270, dy=150, s=108)  # 5 linhas


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças desta aula ----------------
def num_bola(c, s, cx, cy, r, size, a=1.0, cor=None, tinta=None):
    """número dentro da esfera"""
    E.bola(c, cx, cy + 3, r, cor, a)
    centro(c, s, cx, cy + size * 0.36, size, "g", tinta or E.SOBRE, a)


def bola_entra(c, t, t0, s, cx, cy, r, size, cor=None, tinta=None):
    """esfera com número que chega com salto em t0"""
    q = ease_back(prog(t, t0, 0.5))
    if q > 0.05:
        num_bola(c, s, cx, cy, r * q, max(2, round(size * q)), 1.0, cor, tinta)


def bloco(c, x, y, w, h, r, cor, a=1.0, stroke=None):
    if a > 0:
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), r, r), M.paint(cor, a, stroke=stroke))


def cadeira(c, cx, cy, s, cor, a=1.0):
    w = s * 0.72
    bloco(c, cx - w * 0.36, cy - w * 0.56, w * 0.72, w * 0.56, w * 0.14, cor, a)  # encosto
    bloco(c, cx - w / 2, cy + w * 0.08, w, w * 0.3, w * 0.1, cor, a)  # assento
    bloco(c, cx - w * 0.42, cy + w * 0.3, w * 0.12, w * 0.24, w * 0.04, cor, a)  # pés
    bloco(c, cx + w * 0.3, cy + w * 0.3, w * 0.12, w * 0.24, w * 0.04, cor, a)


def arranjo(n, lin, col, box):
    """posição de n cadeiras em lin × col, centradas em box = (x, y, w, h)"""
    x, y, w, h = box
    lado = min(w / col, h / lin, 150)
    x0, y0 = x + (w - lado * col) / 2, y + (h - lado * lin) / 2
    return [(x0 + lado * (j + 0.5), y0 + lado * (i + 0.5)) for i in range(lin) for j in range(col)][:n], lado


def cadeiras(c, t, n, t0, etapas, box, cor=None):
    """n cadeiras que se rearrumam: etapas = [(instante, linhas, colunas)]"""
    pos, lado = arranjo(n, *etapas[0][1:], box)
    for ti, lin, col in etapas[1:]:
        if t < ti:
            break
        q, (dest, l2) = ease_io(prog(t, ti, 0.65)), arranjo(n, lin, col, box)
        pos = [(lerp(a, x, q), lerp(b, y, q)) for (a, b), (x, y) in zip(pos, dest)]
        lado = lerp(lado, l2, q)
    for i, (x, y) in enumerate(pos):
        cadeira(c, x, y, lado, cor or E.COR, ep(t, t0 + i * 0.03, 0.3))


def rotulos(c, t, leg, fim, cx, y, size=84):
    """legenda que troca a cada arrumação: leg = [(instante, texto)]"""
    for i, (ti, s) in enumerate(leg):
        u = leg[i + 1][0] - 0.15 if i + 1 < len(leg) else fim
        if t < u + 0.3:
            E.saida(c, t, u, lambda ti=ti, s=s: E.foco(c, t, ti, 0.4, lambda a: centro(c, s, cx, y, size, "i", TINTA, a)), d=0.2)


def relogio(c, t, t0):
    """relógio de pausa: enche em 3 segundos"""
    r = 210 * ease_back(prog(t, t0, 0.6))
    if r > 0:
        cx, cy = 1490, 440
        E.bola(c, cx, cy, r)
        f = M.clamp(prog(t, t0 + 0.8, 3.0))
        if f > 0:
            E.arco(c, cx, cy, r + 34, -90, 360 * f, TINTA, 10)
        for dx in (-44, 44):
            M.rrect(c, cx + dx - 22, cy - 80, 44, 160, 12, E.SOBRE, ep(t, t0 + 0.2, 0.4))
        E.foco(c, t, t0 + 0.2, 0.5, lambda a: centro(c, "pause o vídeo", cx, cy + r + 120, 64, "i", TINTA, a))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def pergunta():
        a_, b_ = C["s01.a"], C["s01.b"]
        bola_entra(c, t, a_, "91", 620, 560, 300, 300)
        E.frase(c, t, a_ + 0.4, [("é", "i", 130), ("primo?", "g", 130, COR)], 1020, 500, passo=0.2)
        E.frase(c, t, lerp(a_, b_, 0.45), [("tem", "i", 80), ("cara", "i", 80), ("de", "i", 80), ("primo", "i", 80)], 1020, 650, passo=0.14)
        E.frase(c, t, lerp(a_, b_, 0.72), [("muita", "i", 80), ("gente", "i", 80), ("diz", "i", 80), ("que", "i", 80), ("sim", "i", 80)], 1020, 750, passo=0.14)
        E.frase(c, t, b_, [("e", "i", 120), ("erra", "g", 120, ERRADO)], 1020, 920, passo=0.16)
    E.saida(c, t, C["s02"] - 0.1, pergunta)

    if t >= C["s02"]:
        s0, a_, b_, c_ = C["s02"], C["s02.a"], C["s02.b"], C["s02.c"]
        q = ease_back(prog(t, c_ - 0.2, 0.7))
        if q > 0:
            E.bola(c, 1480, 540, 290 * q)
        E.frase(c, t, s0 + 0.3, [("até", "i", 90), ("o", "i", 90), ("fim", "i", 90), ("da", "i", 90), ("aula", "i", 90)], XE, 300)
        E.frase(c, t, a_, [("por", "i", 110), ("que", "i", 110), ("91", "g", 110, COR), ("não", "g", 110), ("é", "i", 110)], XE, 480, passo=0.15)
        E.frase(c, t, b_, [("desmontar", "g", 110, COR)], XE, 650)
        E.frase(c, t, b_ + 0.5, [("qualquer", "i", 96), ("número", "i", 96)], XE, 770, passo=0.15)
        E.frase(c, t, b_ + 0.9, [("em", "i", 96), ("primos", "g", 96, COR)], XE, 880, passo=0.15)
        E.foco(c, t, c_ + 0.2, 0.5, lambda a: (centro(c, "+ atalho", 1480, 525, 84, "g", E.SOBRE, a),
                                              centro(c, "de prova", 1480, 610, 84, "i", E.SOBRE, a)))


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"] + 0.35, [("para", "i", 84), ("acompanhar,", "i", 84)], XE, 310)
    E.frase(c, t, lerp(C["s03"], C["s03.a"], 0.65), [("lembre", "i", 84), ("de", "i", 84)], XE, 420)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "2", XE - 8, 730, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 710, 120, "i", TINTA, a))
    x, w = 960, 780
    for i, (k, l1, l2) in enumerate((("s03.b", "As regras de", "divisibilidade"), ("s03.c", "A divisão por", "dois algarismos"))):
        y = 240 + i * 250
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 196, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 62)], x + 44, y + 84)
        E.frase(c, t, C[k] + 0.3, [(l2, "g", 62, COR)], x + 44, y + 160)
    q = ease_io(prog(t, C["s03.c"] - 0.35, 0.5))
    E.cursor(c, x + w - 30, lerp(410, 660, q), ep(t, C["s03.b"], 0.4))
    E.frase(c, t, lerp(C["s03.c"], C["s03.end"], 0.4), [("procure", "i", 62), ("a", "i", 62), ("aula", "i", 62), ("no", "i", 62), ("canal", "i", 62)], x, 860, passo=0.14)


# ---------------- o que é primo ----------------
AREA = (150, 180, 1000, 620)


def b_primo(c, t, C, b):
    def doze():
        a_, b_, c_ = C["s04.a"], C["s04.b"], C["s04.c"]
        E.frase(c, t, C["s04"] + 0.25, [("cadeiras", "i", 80), ("em", "i", 80), ("fileiras", "i", 80), ("iguais", "g", 74, COR)], XE, 150, passo=0.14)
        cadeiras(c, t, 12, a_, [(None, 3, 4), (b_, 2, 6), (c_, 3, 4)], (130, 200, 960, 640))
        linha(c, t, [("12", "g", 170, COR, a_), ("cadeiras", "i", 110, TINTA, a_ + 0.3)], 1140, 400)
        E.frase(c, t, a_ + 0.5, [("várias", "i", 84), ("arrumações", "g", 66)], 1140, 520, passo=0.2)
        rotulos(c, t, [(b_, "2 fileiras de 6"), (c_, "3 fileiras de 4")], C["s05"], 1470, 720, 84)
        rotulos(c, t, [(b_, "2 × 6 = 12"), (c_, "3 × 4 = 12")], C["s05"], 1470, 840, 84)
    E.saida(c, t, C["s05"] - 0.1, doze)

    def sete():
        a_, b_, c_ = C["s05.a"], C["s05.b"], C["s05.c"]
        cadeiras(c, t, 7, a_, [(None, 1, 7), (c_, 7, 1)], (140, 150, 1060, 760))
        linha(c, t, [("7", "g", 170, COR, a_), ("cadeiras", "i", 110, TINTA, a_ + 0.3)], 1230, 400)
        E.frase(c, t, a_ + 0.5, [("não", "g", 84, ERRADO), ("tem", "i", 90), ("jeito", "i", 90)], 1230, 520, passo=0.16)
        rotulos(c, t, [(b_, "1 fileira de 7"), (c_, "7 fileiras de 1")], C["s06"], 1510, 680, 84)
        u = lerp(c_, C["s05.end"], 0.5)
        E.frase(c, t, u, [("só", "i", 76), ("se", "i", 76), ("divide", "i", 76), ("por", "i", 76)], 1230, 800, passo=0.12)
        E.frase(c, t, u + 0.5, [("1", "g", 72, COR), ("e", "i", 76), ("por", "i", 76), ("ele", "g", 72, COR), ("mesmo", "g", 72, COR)], 1230, 890, passo=0.14)
    if t >= C["s05"]:
        E.saida(c, t, C["s06"] - 0.1, sete)

    def nome():
        a_, b_, c_, d_, e_ = C["s06.a"], C["s06.b"], C["s06.c"], C["s06.d"], C["s06.e"]
        E.frase(c, t, a_, [("número", "i", 150), ("primo", "g", 170, COR)], W / 2, 280, "center")
        E.frase(c, t, b_, [("exatamente", "g", 90), ("2", "g", 96, COR), ("divisores:", "g", 90)], W / 2, 440, "center", passo=0.16)
        E.frase(c, t, b_ + 0.7, [("o", "i", 90), ("1", "g", 90, COR), ("e", "i", 90), ("ele", "i", 90), ("mesmo", "i", 90)], W / 2, 550, "center", passo=0.14)
        # dois lados: o 7 e o 12
        bola_entra(c, t, c_, "7", 440, 760, 130, 150, CERTO, BR)
        E.frase(c, t, c_ + 0.3, [("é", "i", 96), ("primo", "g", 90, CERTO)], 630, 790, passo=0.14)
        bola_entra(c, t, d_, "12", 1130, 760, 130, 130, ERRADO, BR)
        E.frase(c, t, d_ + 0.3, [("não", "g", 90, ERRADO), ("é", "i", 96)], 1320, 750, passo=0.14)
        E.frase(c, t, lerp(d_, e_, 0.5), [("6", "g", 66), ("divisores", "i", 70)], 1320, 840, passo=0.14)
        E.frase(c, t, e_, [("composto", "g", 84, COR)], 1130, 975)
    if t >= C["s06"]:
        E.saida(c, t, C["s07"] - 0.1, nome)

    def casos():
        a_, b_, c_ = C["s07.a"], C["s07.b"], C["s07.c"]
        E.frase(c, t, a_, [("atenção", "g", 96, COR), ("a", "i", 100), ("estes", "i", 100), ("casos", "i", 100)], W / 2, 200, "center", passo=0.14)
        bola_entra(c, t, b_, "1", 400, 460, 150, 170, ERRADO, BR)
        E.frase(c, t, b_ + 0.3, [("não", "g", 92, ERRADO), ("é", "i", 96), ("primo", "i", 96)], 620, 440, passo=0.14)
        E.frase(c, t, b_ + 0.7, [("um", "i", 80), ("divisor", "i", 80), ("só", "g", 76)], 620, 545, passo=0.14)
        bola_entra(c, t, c_, "2", 400, 790, 150, 170, CERTO, BR)
        E.frase(c, t, c_ + 0.3, [("é", "i", 96), ("primo", "g", 92, CERTO)], 620, 720, passo=0.14)
        E.frase(c, t, c_ + 0.7, [("o", "i", 80), ("único", "g", 76, COR), ("primo", "i", 80), ("par", "g", 76, COR)], 620, 825, passo=0.14)
        E.frase(c, t, lerp(c_, C["s07.end"], 0.55), [("outro", "i", 72), ("par", "i", 72), ("também", "i", 72), ("se", "i", 72), ("divide", "i", 72), ("por", "i", 72), ("2", "g", 68)], 620, 925, passo=0.12)
    if t >= C["s07"]:
        E.saida(c, t, C["s08"] - 0.1, casos)

    if t >= C["s08"]:
        a_, fim = C["s08.a"], C["s08.end"]
        E.frase(c, t, C["s08"] + 0.2, [("os", "i", 100), ("primeiros", "i", 100), ("primos", "g", 96, COR)], W / 2, 200, "center", passo=0.14)
        for i, n in enumerate((2, 3, 5, 7, 11, 13, 17, 19, 23, 29)):
            x, y = 330 + (i % 5) * 315, 400 + (i // 5) * 240
            bola_entra(c, t, lerp(a_, fim, 0.72 * i / 10), str(n), x, y, 100, 92)
        E.frase(c, t, lerp(a_, fim, 0.78), [("vale", "i", 88), ("ter", "i", 88), ("na", "i", 88), ("cabeça", "g", 82, COR)], W / 2, 870 + 60, "center", passo=0.14)


# ---------------- testar o 91 ----------------
def selo(c, cx, cy, r, ok, a=1.0):
    """sim ou não numa esfera verde ou vermelha"""
    if a <= 0 or r <= 1:
        return
    E.bola(c, cx, cy, r, CERTO if ok else ERRADO, a)
    k, w = r * 0.42, max(5, r * 0.16)
    if ok:
        M.line(c, cx - k, cy + k * 0.05, cx - k * 0.2, cy + k * 0.8, BR, a, w)
        M.line(c, cx - k * 0.2, cy + k * 0.8, cx + k, cy - k * 0.7, BR, a, w)
    else:
        M.line(c, cx - k * 0.8, cy - k * 0.8, cx + k * 0.8, cy + k * 0.8, BR, a, w)
        M.line(c, cx + k * 0.8, cy - k * 0.8, cx - k * 0.8, cy + k * 0.8, BR, a, w)


def selo_entra(c, t, t0, cx, cy, r, ok):
    selo(c, cx, cy, r * ease_back(prog(t, t0, 0.5)), ok, ep(t, t0, 0.2))


def teste_linha(c, t, t0, d, nota, y, ok=False, cor=None):
    """uma linha do teste: ÷ d, o motivo e o resultado"""
    E.foco(c, t, t0, 0.4, lambda a: E.pilula(c, f"÷ {d}", 700, y - 26, 62, estilo="g", fundo=E.COR, cor=BR, a=a))
    E.frase(c, t, t0 + 0.15, [(nota, "i", 72, cor or TINTA)], 830, y)
    selo_entra(c, t, t0 + 0.4, 1740, y - 26, 48, ok)


def b_teste(c, t, C, b):
    a_, b_, c_, d_ = C["s09.a"], C["s09.b"], C["s09.c"], C["s09.d"]
    a2, b2, c2, d2 = C["s10.a"], C["s10.b"], C["s10.c"], C["s10.d"]
    bola_entra(c, t, a_, "91", 360, 330, 170, 170)
    E.frase(c, t, lerp(a_, b_, 0.3), [("primos,", "g", 72, COR)], 200, 620)
    E.frase(c, t, lerp(a_, b_, 0.3) + 0.3, [("em", "i", 76), ("ordem", "i", 76)], 200, 710, passo=0.14)
    E.frase(c, t, C["s09"] + 0.2, [("como", "i", 84), ("testar?", "i", 84)], 640, 170, passo=0.14)
    teste_linha(c, t, b_, 2, "não: é ímpar", 310)
    teste_linha(c, t, c_, 3, "não: a soma dá 10", 470)
    teste_linha(c, t, d_, 5, "não termina em 0 nem 5", 630)
    E.foco(c, t, a2, 0.4, lambda a: E.pilula(c, "÷ 7", 700, 764, 62, estilo="g", fundo=E.COR, cor=BR, a=a))
    linha(c, t, [("91", "g", 76, TINTA, b2 - 0.3), ("÷", "g", 62, CINZA, b2 - 0.2), ("7", "g", 76, TINTA, b2 - 0.1), ("=", "g", 62, CINZA, b2), ("13", "g", 76, COR, b2 + 0.1),
                 ("sem", "i", 76, TINTA, b2 + 0.3), ("resto", "g", 72, CERTO, b2 + 0.45)], 830, 790)
    selo_entra(c, t, b2 + 0.5, 1740, 764, 48, True)
    linha(c, t, [("91", "g", 110, TINTA, c2), ("=", "g", 90, CINZA, c2 + 0.15), ("7", "g", 110, COR, c2 + 0.3), ("×", "g", 90, CINZA, c2 + 0.45), ("13", "g", 110, COR, c2 + 0.6)], 200, 950)
    E.foco(c, t, d2, 0.5, lambda a: E.pilula(c, "91 não é primo", 1320, 915, 84, estilo="g", fundo=ERRADO, cor=BR, a=a))


# ---------------- fatorar ----------------
def tempos_360(C):
    a, b, c_, d = C["s13.a"], C["s13.b"], C["s13.c"], C["s13.d"]
    e, f, g = C["s14.a"], C["s14.b"], C["s14.c"]
    ti = [b, c_, d, e, f, g]
    tp = [x + 0.1 for x in ti]
    tn = [[a]] + [[x + 0.5] for x in ti]
    tb = [a] + ti
    return tp, tn, tb, ti


def b_fatorar(c, t, C, b):
    def termos():
        a_, b_, c_ = C["s11.a"], C["s11.b"], C["s11.c"]
        E.frase(c, t, C["s11"] + 0.2, [("todo", "i", 88), ("número", "i", 88), ("composto", "g", 82, COR)], XE, 200, passo=0.14)
        E.frase(c, t, a_ - 0.2, [("pode", "i", 88), ("ser", "i", 88)], XE, 310, passo=0.14)
        E.frase(c, t, a_, [("desmontado", "g", 130, COR)], XE, 440)
        E.frase(c, t, a_ + 0.6, [("em", "i", 110), ("primos", "g", 110)], XE, 570, passo=0.14)
        # 12 = 2 × 2 × 3, à direita, marca o que é fator
        x = 1130
        v = lerp(a_, b_, 0.55)
        linha(c, t, [("12", "g", 120, TINTA, v), ("=", "g", 96, CINZA, v + 0.15)], x, 300)
        for i, n in enumerate((2, 2, 3)):
            bola_entra(c, t, v + 0.3 + i * 0.15, str(n), x + 300 + i * 150, 260, 66, 70)
        E.frase(c, t, b_, [("cada", "i", 72), ("número", "i", 72), ("é", "i", 72), ("um", "i", 72)], x, 460, passo=0.13)
        E.frase(c, t, b_ + 0.5, [("fator", "g", 110, COR)], x, 570)
        E.frase(c, t, c_, [("fatorar:", "g", 92, COR)], XE, 760)
        E.frase(c, t, c_ + 0.4, [("escrever", "i", 84), ("como", "i", 84), ("multiplicação", "g", 78), ("só", "g", 78, COR), ("de", "g", 78, COR), ("primos", "g", 78, COR)], XE, 880, passo=0.14)
    E.saida(c, t, C["s12"] - 0.1, termos)

    def metodo():
        a_, b_, c_, fim = C["s12.a"], C["s12.b"], C["s12.c"], C["s12.end"]
        E.frase(c, t, a_ - 0.2, [("o", "i", 88), ("método:", "i", 88)], W / 2, 170, "center", passo=0.14)
        E.frase(c, t, a_, [("divisões", "g", 120, COR), ("sucessivas", "g", 120, COR)], W / 2, 310, "center", passo=0.2)
        E.passo(c, t, b_, 1, "divida pelo", "menor primo que conseguir", 500)
        E.passo(c, t, lerp(b_, c_, 0.55), 2, "repita com", "o resultado", 680)
        E.passo(c, t, c_, 3, "pare quando", "chegar em 1", 860)
    if t >= C["s12"]:
        E.saida(c, t, C["s13"] - 0.1, metodo)

    if t < C["s13"]:
        return
    tp, tn, tb, ti = tempos_360(C)
    a_ = C["s13.a"]
    fim_tab = lerp(C["s14.c"], C["s14.end"], 0.55)
    tabela(c, t, T360, tn, tp, tb, G360, cor_fim=CERTO if t >= fim_tab else None)
    for i in range(6):
        seta_primo(c, t, ti[i], ti[i + 1] if i < 5 else C["s15"], i, G360)

    X = 1000
    E.saida(c, t, C["s13.b"] - 0.2, lambda: E.frase(c, t, a_, [("é", "i", 110), ("par", "g", 110, COR)], X + 100, 520, passo=0.14), d=0.3)
    # as contas de cada passo, no painel do kit
    passos(c, t, T360, ti, tp, tn, C["s15"] - 0.1)
    u = C["s14"] + 0.2
    E.saida(c, t, C["s14.a"] - 0.1, lambda: (E.frase(c, t, u, [("45", "g", 84), ("é", "i", 88), ("ímpar:", "i", 88)], 1150, 820, passo=0.13),
                                             E.frase(c, t, u + 0.5, [("soma", "i", 80), ("dá", "i", 80), ("9,", "i", 80), ("use", "i", 80), ("o", "i", 80), ("3", "g", 76, COR)], 1150, 920, passo=0.12)), d=0.3)
    E.saida(c, t, C["s15"] - 0.1, lambda: E.frase(c, t, fim_tab, [("chegou", "i", 80), ("em", "i", 80), ("1:", "g", 76), ("acabou", "g", 76, CERTO)], 1150, 860, passo=0.16))

    if t >= C["s15"]:
        a_, b_, c_, d_ = C["s15.a"], C["s15.b"], C["s15.c"], C["s15.d"]
        g = G360
        p = ep(t, a_ + 0.3, 0.5)
        E.caixa_pontilhada(c, g["xp"] - 66, g["y0"] - g["s"] * 0.95, 132, g["dy"] * 5 + g["s"] * 1.2, p, COR, prog_=p)
        X = 800
        E.frase(c, t, a_, [("a", "i", 80), ("coluna", "g", 74, COR), ("dos", "i", 80), ("divisores", "g", 74, COR)], X, 200, passo=0.14)
        produto(c, t, T360, [lerp(b_, c_, 0.62 * i / 6) for i in range(6)], X + 40, 370, g, 84, 140)
        E.frase(c, t, lerp(b_, c_, 0.75), [("para", "i", 72), ("conferir:", "i", 72)], X, 530, passo=0.14)
        linha(c, t, [("8", "g", 110, COR, c_), ("×", "g", 90, CINZA, c_ + 0.15), ("9", "g", 110, COR, c_ + 0.3), ("=", "g", 90, CINZA, c_ + 0.45), ("72", "g", 110, TINTA, c_ + 0.6)], X, 690)
        linha(c, t, [("72", "g", 110, TINTA, d_), ("×", "g", 90, CINZA, d_ + 0.15), ("5", "g", 110, COR, d_ + 0.3), ("=", "g", 90, CINZA, d_ + 0.45), ("360", "g", 110, CERTO, d_ + 0.6)], X, 840)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    s0, a_, b_, c_, d_ = C["s16"], C["s16.a"], C["s16.b"], C["s16.c"], C["s16.d"]
    linha(c, t, [("o", "i", 76, TINTA, s0 + 0.2), ("erro", "g", 70, ERRADO, s0 + 0.3), ("mais", "i", 76, TINTA, s0 + 0.45), ("comum:", "i", 76, TINTA, s0 + 0.55)], W / 2, 170, "center")
    E.frase(c, t, a_, [("parar", "g", 96, ERRADO), ("em", "i", 100), ("números", "i", 100), ("que", "i", 100), ("não", "g", 96, ERRADO), ("são", "i", 100), ("primos", "i", 100)], W / 2, 290, "center", passo=0.13)
    linha(c, t, [("360", "g", 150, TINTA, b_), ("=", "g", 120, CINZA, b_ + 0.2)], 330, 520)
    x10, x36 = 980, 1400
    bola_entra(c, t, b_ + 0.4, "10", x10, 470, 110, 110, ERRADO, BR)
    E.foco(c, t, b_ + 0.5, 0.4, lambda a: centro(c, "×", 1190, 505, 100, "g", CINZA, a))
    bola_entra(c, t, b_ + 0.6, "36", x36, 470, 110, 110, ERRADO, BR)
    E.frase(c, t, lerp(b_, c_, 0.6), [("a", "i", 72), ("conta", "i", 72), ("está", "i", 72), ("certa", "g", 68, CERTO)], 330, 650, passo=0.13)
    # 10 e 36 ainda se desmontam
    for cx, ns, ti in ((x10, (2, 5), c_), (x36, (2, 2, 3, 3), c_ + 0.3)):
        for i, n in enumerate(ns):
            bola_entra(c, t, ti + i * 0.12, str(n), cx + (i - (len(ns) - 1) / 2) * 96, 680, 44, 52, CERTO, BR)
        p = ep(t, ti, 0.4)
        if p > 0:
            M.line(c, cx, 585, cx, 625, TINTA2, p, 5)
    E.frase(c, t, c_ + 0.2, [("ainda", "i", 76), ("se", "i", 76), ("desmontam", "g", 72, COR)], W / 2, 830, "center", passo=0.14)
    E.frase(c, t, d_, [("todo", "i", 92), ("fator", "i", 92), ("é", "i", 92), ("primo?", "g", 86, CERTO), ("aí", "i", 92), ("sim,", "i", 92), ("terminou", "g", 86, CERTO)], W / 2, 960, "center", passo=0.13)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def regra():
        s0, a_ = C["s17"], C["s17.a"]
        E.frase(c, t, s0 + 0.25, [("agora,", "i", 90, CLARO), ("o", "i", 90, CLARO), ("atalho", "i", 90, CLARO)], W / 2, 210, "center")
        E.frase(c, t, lerp(s0, a_, 0.55), [("testar", "i", 84, BR), ("se", "i", 84, BR), ("é", "i", 84, BR), ("primo,", "i", 84, BR), ("sem", "g", 78, BR), ("perder", "g", 78, BR), ("tempo", "g", 78, BR)], W / 2, 340, "center", passo=0.13)
        E.frase(c, t, a_, [("pare", "g", 180, CLARO), ("quando", "i", 150, BR)], W / 2, 570, "center")
        E.frase(c, t, a_ + 0.6, [("o", "i", 110, BR), ("resultado", "g", 104, CLARO), ("ficar", "i", 110, BR)], W / 2, 730, "center", passo=0.16)
        E.frase(c, t, a_ + 1.1, [("menor", "g", 104, CLARO), ("que", "i", 110, BR), ("o", "i", 110, BR), ("divisor", "g", 104, CLARO)], W / 2, 870, "center", passo=0.16)
    E.saida(c, t, C["s18"] - 0.1, regra)

    def exemplo():
        a_, b_, c_, d_, e_ = C["s18.a"], C["s18.b"], C["s18.c"], C["s18.d"], C["s18.e"]
        bola_entra(c, t, a_, "97", 300, 300, 130, 130, E.COR, BR)
        E.frase(c, t, lerp(a_, b_, 0.45), [("2,", "g", 76, BR), ("3", "g", 76, BR), ("e", "i", 80, CLARO), ("5", "g", 76, BR)], XE, 530, passo=0.12)
        E.frase(c, t, lerp(a_, b_, 0.6), [("não", "i", 80, CLARO), ("dividem", "i", 80, CLARO)], XE, 630, passo=0.12)
        X = 660
        linha(c, t, [("97", "g", 96, BR, b_), ("÷", "g", 80, CLARO, b_ + 0.1), ("7", "g", 96, BR, b_ + 0.2), ("=", "g", 80, CLARO, b_ + 0.3), ("13", "g", 96, BR, b_ + 0.4), ("e", "i", 88, CLARO, b_ + 0.5), ("sobra", "i", 88, CLARO, b_ + 0.6)], X, 220)
        v = lerp(b_, c_, 0.5)
        E.frase(c, t, v, [("13", "g", 80, BR), ("é", "i", 84, CLARO), ("maior", "g", 80, CERTO), ("que", "i", 84, CLARO), ("7:", "g", 80, BR), ("continue", "i", 84, CLARO)], X, 330, passo=0.13)
        linha(c, t, [("97", "g", 96, BR, c_), ("÷", "g", 80, CLARO, c_ + 0.1), ("11", "g", 96, BR, c_ + 0.2), ("=", "g", 80, CLARO, c_ + 0.3), ("8", "g", 96, BR, c_ + 0.4), ("e", "i", 88, CLARO, c_ + 0.5), ("sobra", "i", 88, CLARO, c_ + 0.6)], X, 520)
        E.frase(c, t, d_, [("8", "g", 80, BR), ("é", "i", 84, CLARO), ("menor", "g", 80, ERRADO), ("que", "i", 84, CLARO), ("11:", "g", 80, BR), ("pare", "g", 80, BR)], X, 630, passo=0.13)
        E.frase(c, t, e_, [("97", "g", 150, BR), ("é", "i", 150, CLARO), ("primo", "g", 150, CLARO)], W / 2, 880, "center", passo=0.16)
    if t >= C["s18"]:
        E.saida(c, t, C["s19"] - 0.1, exemplo)

    def porque():
        a_, b_, fim = C["s19.a"], C["s19.b"], C["s19.end"]
        E.frase(c, t, C["s19"] + 0.25, [("por", "i", 90, CLARO), ("que", "i", 90, CLARO), ("funciona?", "i", 90, CLARO)], W / 2, 190, "center", passo=0.14)
        E.frase(c, t, a_, [("divisores", "i", 104, BR), ("vêm", "i", 104, BR), ("em", "i", 104, BR), ("pares", "g", 100, CLARO)], W / 2, 340, "center", passo=0.14)
        E.frase(c, t, lerp(a_, b_, 0.5), [("divisor", "i", 80, CLARO), ("maior?", "g", 76, BR), ("o", "i", 80, CLARO), ("par", "i", 80, CLARO), ("dele", "i", 80, CLARO), ("seria", "i", 80, CLARO), ("menor", "g", 76, BR)], W / 2, 490, "center", passo=0.13)
        E.frase(c, t, b_, [("e", "i", 88, CLARO), ("você", "i", 88, CLARO), ("já", "g", 84, BR), ("teria", "g", 84, BR), ("testado", "g", 84, BR)], W / 2, 610, "center", passo=0.14)
        u = lerp(b_, fim, 0.3)
        E.frase(c, t, u, [("só", "i", 88, CLARO), ("precisa", "i", 88, CLARO), ("testar", "i", 88, CLARO), ("primos", "g", 84, BR)], W / 2, 790, "center", passo=0.14)
        E.frase(c, t, lerp(b_, fim, 0.62), [("não", "i", 76, CLARO), ("divide", "i", 76, CLARO), ("por", "i", 76, CLARO), ("2?", "g", 72, BR), ("também", "i", 76, CLARO), ("não", "i", 76, CLARO), ("divide", "i", 76, CLARO), ("por", "i", 76, CLARO), ("4", "g", 72, BR)], W / 2, 900, "center", passo=0.12)
    if t >= C["s19"]:
        E.saida(c, t, C["s20"] - 0.1, porque)

    if t >= C["s20"]:
        s0, a_, b_, c_ = C["s20"], C["s20.a"], C["s20.b"], C["s20.c"]
        E.frase(c, t, s0 + 0.25, [("quando", "i", 96, CLARO), ("não", "g", 90, BR), ("compensa?", "g", 90, BR)], W / 2, 200, "center", passo=0.14)
        E.foco(c, t, a_, 0.5, lambda q: num_bola(c, "1", 220, 370, 56, 64, q, E.COR, BR))
        E.frase(c, t, a_ + 0.1, [("é", "i", 76, CLARO), ("par,", "i", 76, CLARO), ("termina", "i", 76, CLARO), ("em", "i", 76, CLARO), ("5", "g", 72, BR)], 310, 380, passo=0.13)
        E.frase(c, t, lerp(a_, b_, 0.55), [("ou", "i", 76, CLARO), ("a", "i", 76, CLARO), ("soma", "i", 76, CLARO), ("dá", "i", 76, CLARO), ("múltiplo", "i", 76, CLARO), ("de", "i", 76, CLARO), ("3", "g", 72, BR)], 310, 480, passo=0.12)
        E.frase(c, t, b_, [("as", "g", 76, BR), ("regras", "g", 76, BR), ("já", "g", 76, BR), ("resolveram", "g", 76, BR)], 310, 580, passo=0.14)
        E.foco(c, t, c_, 0.5, lambda q: num_bola(c, "2", 220, 750, 56, 64, q, E.COR, BR))
        E.frase(c, t, c_ + 0.1, [("números", "i", 76, CLARO), ("enormes", "i", 76, CLARO)], 310, 760, passo=0.14)
        E.frase(c, t, lerp(c_, C["s20.end"], 0.5), [("longo", "g", 76, BR), ("demais", "g", 76, BR), ("à", "i", 76, CLARO), ("mão", "i", 76, CLARO)], 310, 860, passo=0.14)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    s0, a_, fim = C["s21"], C["s21.a"], C["s21.end"]
    E.frase(c, t, s0 + 0.3, [("hora", "i", 72, COR), ("de", "i", 72, COR), ("testar", "i", 72, COR)], XE, 200)
    E.frase(c, t, a_, [("escreva", "i", 110)], XE, 380)
    linha(c, t, [("126", "g", 200, TINTA, lerp(a_, fim, 0.2))], XE, 590)
    E.frase(c, t, lerp(a_, fim, 0.4), [("como", "i", 100), ("multiplicação", "g", 90, COR)], XE, 730, passo=0.15)
    E.frase(c, t, lerp(a_, fim, 0.65), [("de", "i", 100), ("primos", "g", 110, COR)], XE, 860, passo=0.15)
    relogio(c, t, C["s22.a"])


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    a_, b_, c_, d_ = C["s23.a"], C["s23.b"], C["s23.c"], C["s23.d"]
    a2, b2, c2 = C["s24.a"], C["s24.b"], C["s24.c"]
    ini = C["s23"] + 0.2
    ti = [a_, b_, c_, d_]
    tp = [x + 0.1 for x in ti]
    tn = [[ini]] + [[x + 0.5] for x in ti]
    tb = [ini] + ti
    g = G126
    tabela(c, t, T126, tn, tp, tb, g, cor_fim=CERTO if t >= d_ + 0.5 else None)
    for i in range(4):
        seta_primo(c, t, ti[i], ti[i + 1] if i < 3 else C["s24"], i, g)
    passos(c, t, T126, ti, tp, tn, C["s24"] - 0.1)
    X = 1150
    E.saida(c, t, a_ + 1.2, lambda: E.frase(c, t, ini + 0.1, [("é", "i", 96), ("par", "g", 96, COR)], X, 700), d=0.3)
    E.saida(c, t, b_ + 1.0, lambda: E.frase(c, t, lerp(a_, b_, 0.55), [("6", "g", 84), ("+", "g", 84, CINZA), ("3", "g", 84), ("=", "g", 84, CINZA), ("9", "g", 84, COR)], X, 700, passo=0.12), d=0.3)

    if t >= C["s24"]:
        p = ep(t, a2 - 0.2, 0.5)
        E.caixa_pontilhada(c, g["xp"] - 78, g["y0"] - g["s"] * 0.95, 156, g["dy"] * 3 + g["s"] * 1.2, p, COR, prog_=p)
        X = 840
        E.frase(c, t, C["s24"] + 0.2, [("resposta", "i", 88, COR)], X, 220)
        produto(c, t, T126, [lerp(a2, b2, 0.62 * i / 4) for i in range(4)], X + 40, 410, g, 104, 190)
        E.frase(c, t, lerp(a2, b2, 0.72), [("conferindo:", "i", 72)], X, 570)
        linha(c, t, [("2", "g", 110, COR, b2), ("×", "g", 90, CINZA, b2 + 0.15), ("9", "g", 110, COR, b2 + 0.3), ("=", "g", 90, CINZA, b2 + 0.45), ("18", "g", 110, TINTA, b2 + 0.6)], X, 730)
        linha(c, t, [("18", "g", 110, TINTA, c2), ("×", "g", 90, CINZA, c2 + 0.15), ("7", "g", 110, COR, c2 + 0.3), ("=", "g", 90, CINZA, c2 + 0.45), ("126", "g", 110, CERTO, c2 + 0.6)], X, 880)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        a_, b_ = C["s25.a"], C["s25.b"]
        E.frase(c, t, C["s25"] + 0.25, [("resumindo", "i", 96, COR)], W / 2, 210, "center")
        y = 430
        E.foco(c, t, a_, 0.5, lambda q: num_bola(c, "1", 220, y - 28, 56, 64, q))
        E.frase(c, t, a_ + 0.1, [("primo", "g", 80, COR), ("tem", "i", 84), ("exatamente", "i", 84), ("dois", "g", 80, COR), ("divisores", "i", 84)], 310, y, passo=0.14)
        y = 680
        E.foco(c, t, b_, 0.5, lambda q: num_bola(c, "2", 220, y - 28, 56, 64, q))
        E.frase(c, t, b_ + 0.1, [("fatorar", "g", 80, COR), ("é", "i", 84), ("dividir", "i", 84), ("pelo", "i", 84), ("menor", "g", 80, COR), ("primo", "g", 80, COR)], 310, y, passo=0.14)
        E.frase(c, t, b_ + 1.0, [("até", "i", 84), ("chegar", "i", 84), ("em", "i", 84), ("1", "g", 80, COR)], 310, y + 110, passo=0.14)
    E.saida(c, t, C["s26"] - 0.1, resumo)
    if t < C["s26"]:
        return
    s0 = C["s26"]
    E.frase(c, t, s0 + 0.3, [("próxima", "i", 84), ("aula", "i", 84)], XE, 240)
    E.frase(c, t, lerp(s0, C["s26.a"], 0.3), [("a", "i", 76), ("fatoração", "g", 70, COR), ("vira", "i", 76), ("ferramenta", "i", 76)], XE, 350, passo=0.14)
    E.frase(c, t, C["s26.a"], [("MDC", "g", 200, COR)], XE, 560)
    E.frase(c, t, C["s26.a"] + 0.5, [("o", "i", 84), ("maior", "g", 80), ("divisor", "i", 84), ("em", "i", 84), ("comum", "i", 84)], XE, 690, passo=0.16)
    E.foco(c, t, C["s26.b"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1400, 400, 76, estilo="g", fundo=E.COR, cor=E.SOBRE, a=a))
    p = ease_io(prog(t, C["s26.b"] + 0.3, 0.8))
    E.cursor(c, lerp(1700, 1560, p), lerp(720, 445, p), ep(t, C["s26.b"] + 0.2, 0.4), TINTA)
    E.frase(c, t, C["s26.c"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 900, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, primo=b_primo, teste=b_teste, fatorar=b_fatorar, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
