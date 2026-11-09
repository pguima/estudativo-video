"""Visual — Estudativo · FIS-CIN-006: encontro e ultrapassagem.

Segue a LINGUAGEM VISUAL DA FÍSICA do cabeçalho de FIS-CIN-001 (peças em _ferramentas/fisica.py, importado como F).
Nesta aula: a estrada é a pista numerada (F.pista); cada móvel tem a seta de velocidade em petróleo (F.VEL) com o módulo;
o ponto de encontro é a esfera laranja na pista. A função de cada móvel fica embaixo, uma linha por móvel, e a conta de
igualar desce linha a linha (conta()). Trem e túnel desenhados aqui (trem(), tunel(), caminhao()), na escala da cena.
Todo instante vem de C[...] (marcadores do roteiro)."""
import math

import editorial as E
import fisica as F
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Física", "Cinemática")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_FIS-CIN-006_encontro_e_ultrapassagem.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("frente", "atras", "trem", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"

# todas as contas da aula
assert 60 * 2 == 120 and 300 - 90 * 2 == 120 and 60 + 90 == 150 and 300 / 150 == 2
assert 100 * 3 == 300 and 60 + 80 * 3 == 300 and 100 - 80 == 20 and 60 / 20 == 3
assert 400 + 200 == 600 and 600 / 20 == 30 and 400 / 20 == 20
assert 8 * 40 == 320 and 120 + 5 * 40 == 320 and 8 - 5 == 3 and 120 / 3 == 40


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças gerais (copiadas entre as aulas FIS-CIN) ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def bola_txt(c, t, t0, s, cx, cy, r, size, cor=None):
    """resposta na esfera: "20 m/s" com a unidade menor"""
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


def lembrete(c, t, C, cena, itens, desenhos=None):
    """'você precisa de N coisas': itens = [(cue, linha fina, linha forte)]; desenhos[i](a, x, y) à direita de cada caixa"""
    n = len(itens)
    E.frase(c, t, C[cena] + 0.2, ps("você precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C[cena + ".a"], 0.5, lambda a: E.escreve(c, str(n), XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C[cena + ".a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 820, 1000
    h, gap, s1 = (230, 290, 58) if n == 2 else (196, 236, 52)
    y0 = 520 - (h + gap * (n - 1)) / 2
    for i, (k, l1, l2) in enumerate(itens):
        y = y0 + i * gap
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, h, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", s1)], x + 44, y + h * 0.4)
        E.frase(c, t, C[k] + 0.3, [(l2, "g", s1, COR)], x + 44, y + h * 0.74)
        if desenhos:
            E.foco(c, t, C[k] + 0.6, 0.5, lambda a, i=i, y=y: desenhos[i](a, x + w - 150, y + h / 2))
    ult = itens[-1][0]
    E.frase(c, t, lerp(C[ult], C[cena + ".end"], 0.6), ps("faltou alguma?", "i", 56, COR) + ps("procure no canal", "i", 56), 820, 990, "left", 0.12)


def promessa(c, t, C, cena, itens, titulo="até o fim da aula"):
    """gancho: a órbita à direita e a lista numerada; itens = [(cue, texto, atraso)]"""
    tb = C[cena + ".a"] + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1480, 540, 330 * ease_back(prog(t, tb, 0.8)), giro=12 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, C[cena + ".a"], ps(titulo, "i", 88), XE, 280, passo=0.14)
    for i, (k, s, dt) in enumerate(itens):
        y = 450 + i * 160
        E.foco(c, t, C[k] + dt, 0.5, lambda a, i=i, y=y: (E.bola(c, XE + 40, y - 30, 38, a=a),
                                                        centro(c, str(i + 1), XE + 40, y - 8, 48, "g", BR, a)))
        E.frase(c, t, C[k] + dt + 0.1, [(s, "g", 80, COR if i == 0 else TINTA)], XE + 110, y)


def fim_inscreva(c, t, C, cena, k_insc, k_bons):
    E.foco(c, t, C[k_insc], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 420, 76, estilo="g", a=a))
    p = ease_io(prog(t, C[k_insc] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(720, 445, p), ep(t, C[k_insc] + 0.2, 0.4))
    E.frase(c, t, C[k_bons], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1570, 990, "center")


def resumo(c, t, C, cena, itens):
    """resumo numerado: itens = [(cue, partes de E.frase)]"""
    E.frase(c, t, C[cena], [("resumindo", "i", 92, COR)], W / 2, 180, "center")
    for i, (k, partes) in enumerate(itens):
        y = 360 + i * 190
        E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 300, y - 26, 52, a=a), centro(c, str(i + 1), 300, y - 4, 60, "g", BR, a)))
        E.frase(c, t, C[k] + 0.1, partes, 400, y, passo=0.12)


# ---------------- peças desta aula ----------------
def conta(c, t, linhas, x, y0, size=90, dy=None, cor=TINTA):
    """linhas de conta, uma por instante: linhas = [(instante, texto[, cor])]"""
    dy = dy or size * 1.35
    for i, l in enumerate(linhas):
        E.formula_em(c, t, l[0], l[1], x, y0 + i * dy, size, "g", l[2] if len(l) > 2 else cor)


def caminhao(c, x, y, w=300, a=1.0):
    """caminhão de lado andando para a direita: centro em x, rodas em y"""
    if a <= 0:
        return
    r = w * 0.09
    base = y - r * 1.6
    M.rrect(c, x - w / 2, base - w * 0.36, w * 0.68, w * 0.36, 8, E.mix(E.COR, "#000000", 0.18), a)
    M.rrect(c, x - w / 2 + w * 0.7, base - w * 0.27, w * 0.3, w * 0.27, 12, E.COR, a)
    M.rrect(c, x - w / 2 + w * 0.8, base - w * 0.22, w * 0.15, w * 0.1, 5, E.mix(E.COR, BR, 0.75), a)
    for wx in (x - w * 0.35, x - w * 0.15, x + w * 0.35):
        c.drawCircle(wx, y - r, r, M.paint("#1B1B20", a))
        c.drawCircle(wx, y - r, r * 0.45, M.paint("#9A9AA2", a))


def trem(c, x0, x1, y, a=1.0):
    """trem de x0 (traseira) a x1 (frente), rodas em y"""
    if a <= 0:
        return
    n = 3
    L = (x1 - x0) / n
    for k in range(n):
        xa = x0 + k * L
        M.rrect(c, xa + 4, y - 120, L - 8, 100, 16 if k < n - 1 else 30, E.COR, a)
        for j in range(3):
            M.rrect(c, xa + 18 + j * (L - 30) / 3, y - 104, (L - 30) / 3 - 14, 34, 6, E.mix(E.COR, BR, 0.75), a)
        for wx in (xa + L * 0.25, xa + L * 0.75):
            c.drawCircle(wx, y - 14, 14, M.paint("#1B1B20", a))
    c.drawCircle(x1 - 10, y - 60, 9, M.paint("#FFE08A", a))


def tunel(c, x0, x1, y, a=1.0, frente=False):
    """túnel: a montanha atrás (frente=False) ou só a boca por cima do trem (frente=True)"""
    if a <= 0:
        return
    h = 210
    if not frente:
        p = skia.Path()
        p.moveTo(x0 - 80, y); p.quadTo(x0 - 20, y - h - 70, (x0 + x1) / 2, y - h - 90); p.quadTo(x1 + 20, y - h - 70, x1 + 80, y); p.close()
        c.drawPath(p, M.paint("#8E8E86", 0.45 * a))
        M.rrect(c, x0, y - h + 30, x1 - x0, h - 30, 14, "#3A3A40", 0.85 * a)
    else:
        M.rrect(c, x0, y - h + 30, x1 - x0, h - 30, 14, "#3A3A40", 0.55 * a)
        for xx in (x0, x1):
            M.line(c, xx, y - h + 30, xx, y, TINTA, a, 6)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def um():
        y = 640
        vx = F.pista(c, t, C["s01.a"], 260, 1660, y, 0, 300, list(range(0, 301, 60)), "km", size=36)
        q = ease_io(prog(t, C["s01.d"] + 0.3, 2.0))
        E.foco(c, t, C["s01.b"], 0.4, lambda a: F.carrinho(c, vx(lerp(0, 120, q)), y, 170, a=a))
        E.foco(c, t, C["s01.c"], 0.4, lambda a: F.carrinho(c, vx(lerp(300, 120, q)) + (90 if q > 0.99 else 0) * 0, y, 170, a=a, sentido=-1))
        if t < C["s01.d"] + 0.3:
            F.vetor(c, t, C["s01.b"] + 0.3, (vx(0), y - 200), (vx(0) + 200, y - 200), None, "60 km/h", F.VEL, 10, size=48)
            F.vetor(c, t, C["s01.c"] + 0.3, (vx(300), y - 200), (vx(300) - 300, y - 200), None, "90 km/h", F.VEL, 10, lado=-1, size=48)
        q2 = ep(t, C["s01.a"] + 0.6, 0.5)
        if q2 > 0:
            M.line(c, vx(0), y + 150, vx(300), y + 150, TINTA2, q2, 3)
            centro(c, "300 km", (vx(0) + vx(300)) / 2, y + 130, 50, "b", TINTA2, q2)
        E.frase(c, t, C["s01.a"], ps("duas cidades, 300 km", "i", 70), XE, 230, passo=0.12)
        E.frase(c, t, C["s01.b"], ps("saem ao mesmo tempo, de frente", "i", 56, TINTA2), XE, 320, passo=0.1)
        bola_txt(c, t, C["s01.d"] + 2.0, "2 h", 1500, 300, 110, 76)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t >= C["s02"]:
        promessa(c, t, C, "s02", (("s02.a", "onde e quando", 1.4), ("s02.b", "pela fórmula", 0), ("s02.c", "pelo atalho", 0), ("s02.d", "trem e túnel", 0)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    lembrete(c, t, C, "s03", (("s03.b", "função horária:", "s = s₀ + v · t"), ("s03.c", "equação:", "a letra dos dois lados")))


# ---------------- de frente ----------------
def b_frente(c, t, C, b):
    def s04():
        E.frase(c, t, C["s04.a"], [("móvel", "g", 84, COR), ("=", "g", 80, TINTA2)] + ps("corpo que se move", "i", 80), XE, 250, passo=0.12)
        E.frase(c, t, C["s04.b"] - 0.8, [("encontro:", "g", 76)], XE, 440)
        E.frase(c, t, C["s04.b"], [("mesma", "g", 76, COR), ("posição", "g", 76, COR)], XE + 420, 440, passo=0.12)
        E.frase(c, t, C["s04.c"], [("mesmo", "g", 76, COR), ("instante", "g", 76, COR)], XE + 420, 550, passo=0.12)
        E.formula_em(c, t, C["s04.d"], "sA = sB", W / 2, 800, 150, "g", TINTA, "center")
        E.frase(c, t, C["s04.d"] + 0.8, ps("escreva as duas funções e iguale", "i", 60, TINTA2), W / 2, 930, "center", 0.1)
    E.saida(c, t, C["s05"] - 0.1, s04)
    if t < C["s05"]:
        return
    y = 430
    vx = F.pista(c, t, C["s05"], 260, 1660, y, 0, 300, list(range(0, 301, 60)), "km", size=36)
    if t < C["s06.d"] + 0.4:
        E.saida(c, t, C["s06.d"], lambda: (F.vetor(c, t, C["s05.a"], (vx(150) - 150, y - 230), (vx(150) + 150, y - 230), None, None, TINTA2, 6),
                                           E.foco(c, t, C["s05.a"] + 0.3, 0.4, lambda a: E.escreve(c, "sentido +", vx(150) + 170, y - 216, 44, "i", TINTA2, a))))
    fim = C["s06.d"]
    q = ease_io(prog(t, fim, 1.6))
    E.foco(c, t, C["s05.b"], 0.4, lambda a: F.carrinho(c, vx(lerp(0, 120, q)), y, 160, a=a))
    E.foco(c, t, C["s05.c"], 0.4, lambda a: F.carrinho(c, vx(lerp(300, 120, q)), y, 160, a=a, sentido=-1))
    if t < fim:
        E.foco(c, t, C["s05.b"] + 0.3, 0.4, lambda a: (centro(c, "A", vx(0), y - 140, 50, "g", COR, a), centro(c, "+60", vx(0), y - 190, 40, "b", F.VEL, a)))
        E.foco(c, t, C["s05.c"] + 0.3, 0.4, lambda a: (centro(c, "B", vx(300), y - 140, 50, "g", COR, a), centro(c, "−90", vx(300), y - 190, 40, "b", F.VEL, a)))
    else:
        bola_txt(c, t, fim + 1.4, "km 120", vx(120), y - 200, 90, 40)
    E.formula_em(c, t, C["s05.b"] + 0.6, "sA = 60t", XE, 660, 76, "g", TINTA2)
    E.formula_em(c, t, C["s05.c"] + 2.4, "sB = 300 − 90t", XE, 770, 76, "g", TINTA2)
    conta(c, t, [(C["s06.a"], "60t = 300 − 90t"), (C["s06.b"], "150t = 300")], 900, 660, 76, 110)
    bola_txt(c, t, C["s06.c"], "2 h", 1640, 720, 90, 64)
    E.formula_em(c, t, C["s06.d"], "sA = 60 · 2 = 120 km", 900, 960, 70, "g", COR)


# ---------------- um atrás do outro ----------------
def b_atras(c, t, C, b):
    y = 520
    vx = F.pista(c, t, C["s07"], 260, 1660, y, 0, 320, list(range(0, 321, 40)), "km", size=34)
    E.frase(c, t, C["s07.a"], [("mesmo", "g", 76, COR), ("sentido", "g", 76, COR)], XE, 200, passo=0.12)
    q = ease_io(prog(t, C["s08.e"], 1.8))
    E.foco(c, t, C["s07.b"], 0.4, lambda a: caminhao(c, vx(lerp(60, 300, q)), y, 260, a))
    E.foco(c, t, C["s07.c"], 0.4, lambda a: F.carrinho(c, vx(lerp(0, 300, q)) - (110 if q > 0.98 else 0) * 0, y, 160, a=a))
    if t < C["s08.e"]:
        E.foco(c, t, C["s07.b"] + 0.3, 0.4, lambda a: F.medida(c, 80, "km/h", vx(60), y - 230, 50, F.VEL, a, "center"))
        E.foco(c, t, C["s07.c"] + 0.3, 0.4, lambda a: F.medida(c, 100, "km/h", vx(0), y - 160, 50, F.VEL, a, "center"))
        q2 = ep(t, C["s07.c"] + 0.6, 0.4)
        if q2 > 0:
            M.line(c, vx(0), y + 130, vx(60), y + 130, TINTA2, q2, 3)
            centro(c, "60 km", vx(30), y + 180, 44, "b", TINTA2, q2)
    else:
        bola_txt(c, t, C["s08.e"] + 1.6, "300 km", vx(300) - 140, y - 250, 95, 44)
    E.saida(c, t, C["s08"] - 0.1, lambda: E.frase(c, t, C["s07.end"] - 2.2, ps("alcançar = começo da ultrapassagem", "i", 54, TINTA2), 1060, 200, "left", 0.08))
    E.frase(c, t, C["s08"], ps("origem no carro", "i", 52, TINTA2), XE, 690, passo=0.1)
    E.formula_em(c, t, C["s08.a"], "carro: s = 100t", XE, 790, 72, "g", TINTA2)
    E.formula_em(c, t, C["s08.b"], "caminhão: s = 60 + 80t", XE, 900, 72, "g", TINTA2)
    E.formula_em(c, t, C["s08.c"], "20t = 60", 1080, 820, 90, "g", TINTA)
    bola_txt(c, t, C["s08.d"], "3 h", 1580, 820, 95, 66)


# ---------------- trem e túnel ----------------
K = 1.4  # pixels por metro
T0, T1 = 760, 760 + 400 * K
YT = 760


def b_trem(c, t, C, b):
    E.foco(c, t, C["s09.b"], 0.5, lambda a: tunel(c, T0, T1, YT, a))
    if t >= C["s09"]:
        M.line(c, 120, YT, 1840, YT, TINTA, ep(t, C["s09"], 0.4), 6)
    # a traseira anda de T0 − trem até T1 durante s10
    q = ease_io(prog(t, C["s10.a"], max(1.0, C["s10.c"] - C["s10.a"])))
    xr = lerp(T0 - 200 * K, T1, q)
    E.foco(c, t, C["s09.a"], 0.5, lambda a: trem(c, xr, xr + 200 * K, YT, a))
    E.foco(c, t, C["s09.b"], 0.5, lambda a: tunel(c, T0, T1, YT, a, frente=True))
    E.saida(c, t, C["s10.a"], lambda: E.foco(c, t, C["s09.a"] + 0.3, 0.4, lambda a: E.pilula(c, "trem 200 m", T0 - 100 * K, YT + 80, 44, "g", fundo=E.COR, a=a)))
    E.foco(c, t, C["s09.b"] + 0.3, 0.4, lambda a: E.pilula(c, "túnel 400 m", (T0 + T1) / 2, YT - 310, 44, "g", fundo=TINTA, a=a))
    E.frase(c, t, C["s09.c"], [("20", "g", 70), ("m/s", "b", 56, F.UNID)], XE, 230, passo=0.12)
    E.frase(c, t, C["s09.d"], ps("atravessar: da frente entrar", "i", 60), XE + 330, 230, passo=0.1)
    E.frase(c, t, C["s09.d"] + 1.6, ps("até a traseira sair", "i", 60), XE + 330, 320, passo=0.1)
    if t >= C["s10"]:
        E.foco(c, t, C["s10"], 0.4, lambda a: (c.drawCircle(T0 - 200 * K, YT - 70, 18, M.paint(F.VEL, a)), centro(c, "traseira", T0 - 200 * K, YT - 110, 40, "i", F.VEL, a)))
        q2 = ep(t, C["s10.b"], 0.5)
        if q2 > 0:
            yy = YT + 160
            for xa, xb, s in ((T0 - 200 * K, T0, "200"), (T0, T1, "400")):
                M.line(c, xa + 6, yy, xb - 6, yy, F.VEL, q2, 5)
                for xx in (xa, xb):
                    M.line(c, xx, yy - 16, xx, yy + 16, F.VEL, q2, 5)
                centro(c, s + " m", (xa + xb) / 2, yy + 60, 46, "b", F.VEL, q2)
        E.formula_em(c, t, C["s10.b"] + 0.4, "400 + 200 = 600 m", XE, 440, 70, "g", TINTA)
        E.formula_em(c, t, C["s10.c"], "600 ÷ 20", XE, 550, 76, "g", TINTA)
        bola_txt(c, t, C["s10.c"] + 1.0, "30 s", 1660, 450, 90, 60)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s11"], [("cuidado", "g", 96, ERRADO)], XE, 200)
    E.frase(c, t, C["s11.a"], ps("esquecer o trem", "i", 72), XE + 480, 200, passo=0.12)
    tunel(c, T0, T1, YT, 1.0)
    M.line(c, 120, YT, 1840, YT, TINTA, 1.0, 6)
    trem(c, T1 - 200 * K, T1, YT)
    tunel(c, T0, T1, YT, 1.0, frente=True)
    E.foco(c, t, C["s11.b"], 0.5, lambda a: E.formula(c, "400 ÷ 20 = 20 s ?", XE, 380, 90, "g", ERRADO, a))
    E.foco(c, t, C["s11.c"], 0.4, lambda a: E.pilula(c, "a frente sai", T1 + 40, YT - 300, 46, "g", fundo=TINTA, a=a))
    E.foco(c, t, C["s11.d"], 0.4, lambda a: E.pilula(c, "o trem ainda está dentro", (T0 + T1) / 2, YT + 110, 46, "g", fundo=ERRADO, a=a))
    if t >= C["s11.d"] + 0.6:
        E.risco(c, XE - 10, 400, XE + 760, 320, t, C["s11.d"] + 0.6, largura=10)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def s12():
        E.frase(c, t, C["s12"], ps("agora, o atalho", "i", 76, CLARO), W / 2, 160, "center")
        E.frase(c, t, C["s12.a"], [("velocidade", "g", 84, BR), ("relativa", "g", 84, BR)], W / 2, 290, "center", 0.14)
        y1, y2 = 460, 640
        E.foco(c, t, C["s12.b"], 0.5, lambda a: (F.seta(c, 360, y1, 600, y1, CLARO, a, 11), F.seta(c, 960, y1, 720, y1, CLARO, a, 11)))
        E.frase(c, t, C["s12.b"] + 0.4, [("de", "i", 70, CLARO), ("frente:", "i", 70, CLARO), ("some", "g", 70, BR)], 1100, y1 + 24, "left", 0.12)
        E.foco(c, t, C["s12.c"], 0.5, lambda a: (F.seta(c, 360, y2, 600, y2, CLARO, a, 11), F.seta(c, 720, y2, 960, y2, CLARO, a, 11)))
        E.frase(c, t, C["s12.c"] + 0.4, [("mesmo", "i", 70, CLARO), ("sentido:", "i", 70, CLARO), ("subtraia", "g", 70, BR)], 1100, y2 + 24, "left", 0.12)
        E.formula_em(c, t, C["s12.d"], "tempo = f{distância entre eles}{velocidade relativa}", W / 2, 880, 74, "g", BR, "center")
    E.saida(c, t, C["s13"] - 0.1, s12)
    if C["s13"] <= t < C["s14"]:
        def s13():
            E.frase(c, t, C["s13"], [("cidades:", "i", 70, CLARO)], XE, 300)
            E.formula_em(c, t, C["s13.a"], "60 + 90 = 150", XE + 330, 300, 80, "g", BR)
            E.formula_em(c, t, C["s13.b"], "300 ÷ 150 = 2 h", XE + 330, 420, 80, "g", CLARO)
            E.frase(c, t, C["s13.c"] - 0.6, [("caminhão:", "i", 70, CLARO)], XE, 620)
            E.formula_em(c, t, C["s13.c"], "100 − 80 = 20", XE + 330, 620, 80, "g", BR)
            E.formula_em(c, t, C["s13.d"], "60 ÷ 20 = 3 h", XE + 330, 740, 80, "g", CLARO)
            E.frase(c, t, lerp(C["s13.d"], C["s13.end"], 0.5), ps("sem montar equação", "i", 64, CLARO), W / 2, 930, "center", 0.12)
        E.saida(c, t, C["s14"] - 0.1, s13)
    if t < C["s14"]:
        return
    E.frase(c, t, C["s14.a"], ps("é olhar de dentro de um dos móveis:", "i", 66, CLARO) + [("referencial", "g", 66, BR)], W / 2, 260, "center", 0.1)
    E.foco(c, t, C["s14.b"], 0.5, lambda a: (caminhao(c, 1300, 600, 300, a), F.carrinho(c, 700, 600, 200, a=a)))
    F.vetor(c, t, C["s14.b"] + 0.4, (620, 430), (820, 430), None, "20 km/h", CLARO, 10, size=50, escuro=True)
    E.frase(c, t, C["s14.c"], [("não", "g", 64, ERRADO), ("compensa:", "i", 66, CLARO)] + ps("saídas em instantes diferentes", "i", 66, CLARO), W / 2, 860, "center", 0.1)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s15"], ps("hora de testar", "i", 72, COR), XE, 200)
    y = 520
    vx = F.pista(c, t, C["s15"] + 0.4, 260, 1660, y, 0, 400, list(range(0, 401, 80)), "m", size=36)
    E.foco(c, t, C["s15.a"], 0.4, lambda a: (F.carrinho(c, vx(0), y, 150, a=a), centro(c, "A", vx(0), y - 130, 50, "g", COR, a)))
    E.foco(c, t, C["s15.a"] + 0.4, 0.4, lambda a: F.medida(c, 8, "m/s", vx(0), y - 190, 48, F.VEL, a, "center"))
    E.foco(c, t, C["s15.b"], 0.4, lambda a: (F.carrinho(c, vx(120), y, 150, a=a), centro(c, "B", vx(120), y - 130, 50, "g", COR, a)))
    E.foco(c, t, C["s15.b"] + 0.4, 0.4, lambda a: F.medida(c, 5, "m/s", vx(120), y - 190, 48, F.VEL, a, "center"))
    E.frase(c, t, C["s15.b"] + 1.0, ps("mesmo sentido", "i", 56, TINTA2), 1000, 330, "left", 0.1)
    E.frase(c, t, C["s15.c"], [("quando", "g", 76, COR), ("e", "i", 76), ("onde", "g", 76, COR)] + ps("A alcança B?", "i", 76), XE, 860, passo=0.12)
    if t >= C["s16"]:
        E.relogio(c, t, C["s16.a"], cx=1560, cy=750, r=105)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    E.formula_em(c, t, C["s17.a"], "sA = 8t", XE, 260, 84, "g", TINTA2)
    E.formula_em(c, t, C["s17.b"], "sB = 120 + 5t", XE, 380, 84, "g", TINTA2)
    conta(c, t, [(C["s17.c"], "8t = 120 + 5t"), (C["s17.c"] + 1.6, "3t = 120")], XE, 540, 84, 120)
    bola_txt(c, t, C["s17.d"], "40 s", 980, 600, 100, 64)
    E.formula_em(c, t, C["s18.a"], "8 · 40 = 320 m", 1180, 300, 84, "g", COR)
    q = ep(t, C["s18.b"], 0.5)
    if q > 0:
        M.rrect(c, 1180, 470, 640, 330, 30, E.COR, 0.12 * q)
        centro(c, "atalho", 1500, 530, 50, "i", COR, q)
    E.formula_em(c, t, C["s18.b"], "8 − 5 = 3", 1500, 640, 80, "g", TINTA, "center")
    E.formula_em(c, t, C["s18.c"], "120 ÷ 3 = 40 s", 1500, 760, 80, "g", TINTA, "center")


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def s19():
        resumo(c, t, C, "s19", (("s19.a", [("encontro:", "g", 64), ("iguale", "i", 64), ("as", "i", 64), ("funções", "g", 64, COR)]),
                                ("s19.b", [("de", "i", 64), ("frente:", "i", 64), ("some", "g", 64, COR)]),
                                ("s19.c", [("um", "i", 64), ("atrás", "i", 64), ("do", "i", 64), ("outro:", "i", 64), ("subtraia", "g", 64, COR)]),
                                ("s19.d", [("trem:", "i", 64), ("túnel", "g", 64), ("+", "g", 64, COR), ("ele", "g", 64), ("mesmo", "g", 64)])))
    E.saida(c, t, C["s20"] - 0.1, s19)
    if t < C["s20"]:
        return
    E.frase(c, t, C["s20"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C["s20.a"], ps("a velocidade muda:", "i", 76), XE, 400, passo=0.12)
    E.frase(c, t, C["s20.b"], [("aceleração", "g", 120, COR)], XE, 560)
    for i in range(4):
        F.vetor(c, t, C["s20.b"] + 0.3 + 0.25 * i, (XE + 20, 680 + i * 80), (XE + 140 + 110 * i, 680 + i * 80), None, None, F.VEL, 9)
    fim_inscreva(c, t, C, "s20", "s20.c", "s20.d")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, frente=b_frente, atras=b_atras, trem=b_trem, erro=b_erro, atalho=b_atalho,
              questao=b_questao, resposta=b_resposta, fim=b_fim)
