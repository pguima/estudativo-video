"""Visual — Estudativo · FIS-CIN-003: decompor um vetor nos eixos.

Segue a LINGUAGEM VISUAL DA FÍSICA do cabeçalho de FIS-CIN-001 (peças em _ferramentas/fisica.py, importado como F).
Nesta aula: o vetor (velocidade ou deslocamento) em petróleo (F.VEL); as componentes mais claras, com o tracejado até os
eixos (F.componentes); o ângulo θ em laranja (E.angulo); a resultante do método dos eixos em laranja (E.COR) com a letra R.
Eixos x e y desenhados aqui (eixos()), porque o plano cartesiano não está no "Já ensinado" desta aula.
Todo instante vem de C[...] (marcadores do roteiro)."""
import math

import editorial as E
import fisica as F
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Física", "Cinemática")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_FIS-CIN-003_decompor_vetor_nos_eixos.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("decompor", "bola", "eixos", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"

# todas as contas da aula (sen 37° ≈ 0,6 e cos 37° ≈ 0,8, valores de prova)
assert 20 * 0.8 == 16 and round(20 * 0.6, 9) == 12 and 16 + 12 == 28 and 16 ** 2 + 12 ** 2 == 256 + 144 == 400 == 20 ** 2
assert 10 * 0.5 == 5 and abs(10 * math.sqrt(3) / 2 - 5 * math.sqrt(3)) < 1e-12
assert 10 * 0.8 == 8 and round(10 * 0.6, 9) == 6 and 8 + 0 == 8 and 6 + 9 == 15 and 8 ** 2 + 15 ** 2 == 64 + 225 == 289 and math.isqrt(289) == 17
assert 20 / 5 == 4 and 4 * 4 == 16 and 4 * 3 == 12 and 0.8 == 4 / 5 and 0.6 == 3 / 5
assert 25 / 5 == 5 and 5 * 4 == 20 and 5 * 3 == 15 and 15 ** 2 + 20 ** 2 == 25 ** 2
assert abs(math.sin(math.radians(37)) - 0.6) < 0.01 and abs(math.cos(math.radians(37)) - 0.8) < 0.01


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
def eixos(c, t, t0, O, x1, y1, tx=None, ty=None, nomes=("x", "y"), x0=None, y0=None, escuro=False):
    """eixo x de x0 até x1 e eixo y de y0 até y1, cruzando em O; cada um entra no seu instante"""
    tinta = BR if escuro else TINTA
    x0 = O[0] - 40 if x0 is None else x0
    y0 = O[1] + 40 if y0 is None else y0
    tx = t0 if tx is None else tx
    ty = t0 if ty is None else ty
    if t >= tx:
        M.arrow(c, x0, O[1], x1, O[1], tinta, 1.0, 5, 22, ep(t, tx, 0.6))
        E.foco(c, t, tx + 0.4, 0.4, lambda a: E.escreve(c, nomes[0], x1 - 10, O[1] + 66, 56, "i", tinta, a))
    if t >= ty:
        M.arrow(c, O[0], y0, O[0], y1, tinta, 1.0, 5, 22, ep(t, ty, 0.6))
        E.foco(c, t, ty + 0.4, 0.4, lambda a: E.escreve(c, nomes[1], O[0] - 64, y1 + 30, 56, "i", tinta, a))


def tri_fill(c, pts, a, cor=None):
    if a <= 0:
        return
    p = skia.Path(); p.moveTo(*pts[0])
    for q in pts[1:]:
        p.lineTo(*q)
    p.close()
    c.drawPath(p, M.paint(cor or E.COR, 0.16 * a))


def comp(c, t, t0, A, B, rot, cor=None, lado=1, size=48):
    """componente: seta mais clara com o rótulo"""
    cor = E.mix(cor or F.VEL, BR, 0.25)
    F.vetor(c, t, t0, A, B, None, rot, cor, 9, lado=lado, size=size)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def um():
        O, u = (1000, 880), 32
        B = (O[0] + 16 * u, O[1] - 12 * u)
        E.foco(c, t, C["s01.a"], 0.4, lambda a: F.chao(c, 860, 1820, O[1] + 36, a))
        E.foco(c, t, C["s01.a"], 0.4, lambda a: E.bola(c, O[0], O[1], 36, a=a))
        F.vetor(c, t, C["s01.a"] + 0.3, O, B, None, "20 m/s", F.VEL, 12, size=56)
        if t >= C["s01.a"] + 0.9:
            E.angulo(c, t, C["s01.a"] + 0.9, O, (O[0] + 200, O[1]), B, None, r=110)
        if t >= C["s01.b"]:
            M.line(c, *B, B[0], O[1], TINTA, 0.6, 4, dash=E.TRACO, progress=ep(t, C["s01.b"], 0.5))
        comp(c, t, C["s01.b"] + 0.3, O, (B[0], O[1]), "16 m/s", lado=1)
        if t >= C["s01.c"]:
            M.line(c, *B, O[0], B[1], TINTA, 0.6, 4, dash=E.TRACO, progress=ep(t, C["s01.c"], 0.5))
        comp(c, t, C["s01.c"] + 0.3, O, (O[0], B[1]), "12 m/s", lado=1)
        E.frase(c, t, C["s01.a"], [("chute:", "i", 76)], XE, 300)
        E.foco(c, t, C["s01.a"] + 0.3, 0.5, lambda a: F.medida(c, 20, "m/s", XE + 240, 300, 100, TINTA, a))
        E.frase(c, t, C["s01.b"], [("para a frente:", "i", 66), ("16", "g", 70, COR)], XE, 430, passo=0.12)
        E.frase(c, t, C["s01.c"], [("para cima:", "i", 66), ("12", "g", 70, COR)], XE, 530, passo=0.12)
        E.foco(c, t, C["s01.d"], 0.5, lambda a: E.formula(c, "16 + 12 = 28 ≠ 20", XE, 700, 84, "g", TINTA, a))
        pilula_em(c, t, lerp(C["s01.d"], C["s01.end"], 0.7), "e está certo", XE + 230, 830, 56, CERTO)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t >= C["s02"]:
        promessa(c, t, C, "s02", (("s02.b", "parte deitada: x", 0), ("s02.c", "parte em pé: y", 0), ("s02.d", "método dos eixos", 0)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    lembrete(c, t, C, "s03", (("s03.b", "ângulo reto:", "Pitágoras"), ("s03.c", "sen 37° = 0,6", "cos 37° = 0,8"),
                              ("s03.d", "ângulos notáveis:", "30°, 45°, 60°")))


# ---------------- decompor ----------------
def b_decompor(c, t, C, b):
    O, B = (1080, 860), (1640, 440)
    P = (B[0], O[1])
    eixos(c, t, 0, O, 1820, 300, C["s05.b"], C["s05.c"])
    if t >= C["s05.e"]:
        tri_fill(c, [O, P, B], ep(t, C["s05.e"], 0.5))
    F.vetor(c, t, C["s04"] + 0.4, O, B, "v", None, F.VEL, 12, lado=1, size=64)
    if t >= C["s05.d"]:
        q = ep(t, C["s05.d"], 0.6)
        M.line(c, *B, *P, TINTA, 0.6, 4, dash=E.TRACO, progress=q)
        M.line(c, *B, O[0], B[1], TINTA, 0.6, 4, dash=E.TRACO, progress=q)
    comp(c, t, C["s05.d"] + 0.4, O, P, None)
    comp(c, t, C["s05.d"] + 0.7, O, (O[0], B[1]), None)
    E.foco(c, t, C["s05.d"] + 0.9, 0.4, lambda a: (F.letra_vetor(c, "vx", (O[0] + P[0]) / 2, O[1] + 90, 56, F.VEL, a),
                                                  F.letra_vetor(c, "vy", O[0] - 70, (O[1] + B[1]) / 2 + 20, 56, F.VEL, a)))
    if t >= C["s06.a"]:
        E.angulo(c, t, C["s06.a"], O, (O[0] + 200, O[1]), B, "θ", r=110)
    pilula_em(c, t, C["s06.b"], "adjacente", (O[0] + P[0]) / 2, O[1] + 160, 40, TINTA)
    pilula_em(c, t, C["s06.d"], "oposto", P[0] + 110, (O[1] + B[1]) / 2, 40, TINTA)

    def s04():
        E.frase(c, t, C["s04"], ps("na soma:", "i", 66, TINTA2), XE, 260)
        E.frase(c, t, C["s04.a"], [("2", "g", 72), ("vetores", "i", 72), ("→", "g", 72, TINTA2), ("1", "g", 72)], XE, 360, passo=0.12)
        E.frase(c, t, C["s04.b"], [("decompor:", "g", 84, COR)], XE, 540)
        E.frase(c, t, C["s04.c"], [("1", "g", 72), ("vetor", "i", 72), ("→", "g", 72, TINTA2), ("2", "g", 72)], XE, 650, passo=0.12)
        E.frase(c, t, C["s04.c"] + 1.4, ps("um em cada eixo", "i", 60, TINTA2), XE, 740, passo=0.1)
        E.frase(c, t, C["s04.d"], [("componentes", "g", 84, COR)], XE, 900)
    E.saida(c, t, C["s05"] - 0.1, s04)
    if C["s05"] <= t < C["s06"]:
        def s05():
            E.frase(c, t, C["s05.b"], [("x", "g", 80, COR), ("deitado", "i", 76)], XE, 300, passo=0.14)
            E.frase(c, t, C["s05.c"], [("y", "g", 80, COR), ("em", "i", 76), ("pé", "i", 76)], XE, 420, passo=0.14)
            E.frase(c, t, C["s05.e"], ps("triângulo retângulo:", "i", 60, TINTA2), XE, 600, passo=0.1)
            E.frase(c, t, C["s05.f"], [("vetor", "g", 66), ("=", "g", 66, TINTA2), ("hipotenusa", "i", 70)], XE, 720, passo=0.12)
            E.frase(c, t, C["s05.f"] + 1.2, [("componentes", "g", 66), ("=", "g", 66, TINTA2), ("catetos", "i", 70)], XE, 830, passo=0.12)
        E.saida(c, t, C["s06"] - 0.1, s05)
    if t < C["s06"]:
        return
    E.frase(c, t, C["s06"], [("θ", "g", 80, COR), ("=", "g", 76, TINTA2), ("ângulo", "i", 76), ("com", "i", 76), ("o", "i", 76), ("x", "g", 76)], XE, 260, passo=0.12)
    E.formula_em(c, t, C["s06.c"], "vx = v · cos θ", XE, 470, 96, "g", TINTA)
    E.frase(c, t, C["s06.b"], ps("encosta no ângulo", "i", 54, TINTA2), XE, 560, passo=0.1)
    E.formula_em(c, t, C["s06.e"], "vy = v · sen θ", XE, 740, 96, "g", TINTA)
    E.frase(c, t, C["s06.d"], ps("de frente para o ângulo", "i", 54, TINTA2), XE, 830, passo=0.1)


# ---------------- a bola e o notável ----------------
def b_bola(c, t, C, b):
    def s07():
        O, u = (1200, 880), 30
        B = (O[0] + 16 * u, O[1] - 12 * u)
        E.foco(c, t, C["s07"], 0.4, lambda a: (F.chao(c, 1060, 1840, O[1] + 36, a), E.bola(c, O[0], O[1], 34, a=a)))
        F.vetor(c, t, C["s07.a"], O, B, None, "20 m/s", F.VEL, 12, size=54)
        if t >= C["s07.a"] + 0.5:
            E.angulo(c, t, C["s07.a"] + 0.5, O, (O[0] + 200, O[1]), B, "37°", r=110)
        comp(c, t, C["s07.b"], O, (B[0], O[1]), "16 m/s", lado=1)
        comp(c, t, C["s07.c"], O, (O[0], B[1]), "12 m/s", lado=1)
        E.formula_em(c, t, C["s07.b"], "vx = 20 · 0,8 = 16", XE, 300, 80, "g", TINTA)
        E.formula_em(c, t, C["s07.c"], "vy = 20 · 0,6 = 12", XE, 430, 80, "g", TINTA)
        E.formula_em(c, t, C["s07.d"], "16^2 + 12^2", XE, 620, 72, "g", TINTA2)
        E.formula_em(c, t, C["s07.d"] + 1.2, "= 256 + 144 = 400", XE, 720, 72, "g", TINTA2)
        E.formula_em(c, t, C["s07.e"], "= 20^2", XE, 830, 84, "g", CERTO)
        E.foco(c, t, C["s07.e"] + 0.4, 0.4, lambda a: E.selo(c, XE + 420, 800, 50, True, a))
    E.saida(c, t, C["s08"] - 0.1, s07)
    if t < C["s08"]:
        return
    E.frase(c, t, C["s08"], [("16", "g", 70), ("+", "g", 70, TINTA2), ("12", "g", 70), ("≠", "g", 70, ERRADO), ("20", "g", 70)], XE, 230, passo=0.12)
    E.frase(c, t, C["s08.a"], ps("catetos não se somam em fila", "i", 60, TINTA2), XE, 330, passo=0.1)
    O = (1180, 900)
    B = (O[0] + 260, O[1] - 450)
    if t >= C["s08.b"]:
        eixos(c, t, C["s08.b"], O, 1720, 360)
    F.vetor(c, t, C["s08.b"] + 0.3, O, B, None, "10", F.VEL, 12, size=56)
    if t >= C["s08.b"] + 0.8:
        E.angulo(c, t, C["s08.b"] + 0.8, O, (O[0] + 200, O[1]), B, "60°", r=100)
    comp(c, t, C["s08.c"], O, (B[0], O[1]), "5", lado=-1)
    comp(c, t, C["s08.d"], O, (O[0], B[1]), "5√3", lado=1)
    E.formula_em(c, t, C["s08.c"], "x = 10 · f{1}{2} = 5", XE, 560, 80, "g", TINTA)
    E.formula_em(c, t, C["s08.d"], "y = 10 · f{r{3}}{2} = 5r{3}", XE, 800, 80, "g", TINTA)


# ---------------- método dos eixos ----------------
def b_eixos(c, t, C, b):
    def s09():
        E.frase(c, t, C["s09.a"], ps("somar vetores inclinados:", "i", 72), XE, 220, passo=0.1)
        E.frase(c, t, C["s09.a"] + 1.2, [("método", "g", 84, COR), ("dos", "i", 84), ("eixos", "g", 84, COR)], XE, 330, passo=0.12)
        for i, (k, s) in enumerate((("s09.b", "decomponha cada vetor"), ("s09.c", "some todos os x"), ("s09.d", "some todos os y"), ("s09.e", "feche com Pitágoras"))):
            y = 500 + i * 130
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, XE + 40, y - 28, 40, a=a), centro(c, str(i + 1), XE + 40, y - 6, 50, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, ps(s, "g", 64), XE + 110, y, passo=0.1)
        E.frase(c, t, C["s09.d"] + 1.4, [("←", "g", 56, ERRADO), ("e", "i", 56), ("↓", "g", 56, ERRADO), ("entram", "i", 56), ("com", "i", 56), ("menos", "g", 56, ERRADO)],
                1100, 640, "left", 0.1)
    E.saida(c, t, C["s10"] - 0.1, s09)
    if t < C["s10"]:
        return
    u = 36
    O = (1280, 990)
    A = (O[0] + 8 * u, O[1] - 6 * u)
    Bp = (A[0], A[1] - 9 * u)
    E.frase(c, t, C["s10"], [("drone:", "i", 70), ("2", "g", 70), ("deslocamentos", "i", 70)], XE, 200, passo=0.12)
    F.vetor(c, t, C["s10.b"], O, A, None, "10 m", F.VEL, 11, lado=-1, size=50)
    if t >= C["s10.b"] + 0.5:
        E.angulo(c, t, C["s10.b"] + 0.5, O, (O[0] + 160, O[1]), A, None, r=90)
        M.line(c, O[0], O[1], O[0] + 200, O[1], TINTA, 0.5, 3, dash=E.TRACO)
    F.vetor(c, t, C["s10.c"], A, Bp, None, "9 m", F.VEL, 11, lado=-1, size=50)
    F.vetor(c, t, C["s10.g"], O, Bp, "R", None, E.COR, 12, lado=1, size=60)
    E.frase(c, t, C["s10.b"], [("10 m", "g", 60, F.VEL), ("a", "i", 60), ("37°,", "g", 60)], XE, 300, passo=0.12)
    E.frase(c, t, C["s10.c"], [("9 m", "g", 60, F.VEL), ("para", "i", 60), ("cima", "i", 60)], XE + 480, 300, passo=0.12)
    E.formula_em(c, t, C["s10.d"], "x: 8 + 0 = 8", XE, 440, 80, "g", TINTA)
    E.formula_em(c, t, C["s10.e"], "y: 6 + 9 = 15", XE, 560, 80, "g", TINTA)
    E.formula_em(c, t, C["s10.f"], "R = r{64 + 225} = r{289}", XE, 710, 80, "g", TINTA)
    bola_txt(c, t, C["s10.g"], "17 m", XE + 280, 890, 110, 64)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s11"], [("cuidado", "g", 96, ERRADO)], XE, 200)
    E.frase(c, t, C["s11.a"], ps("cosseno sempre no x?", "i", 72), XE + 480, 200, passo=0.12)
    for i, (x0, kt, chao) in enumerate(((330, C["s11.a"] + 0.8, True), (1130, C["s11.b"], False))):
        O = (x0, 740)
        B = (x0 + 330, 740 - 250) if chao else (x0 + 250, 740 - 330)
        E.foco(c, t, kt, 0.5, lambda a, O=O: (M.line(c, O[0] - 20, O[1], O[0] + 520, O[1], TINTA, a, 4), M.line(c, O[0], O[1] + 20, O[0], O[1] - 390, TINTA, a, 4)))
        F.vetor(c, t, kt + 0.2, O, B, None, None, F.VEL, 11)
        if t >= kt + 0.6:
            ref = (O[0] + 180, O[1]) if chao else (O[0], O[1] - 180)
            E.angulo(c, t, kt + 0.6, O, ref, B, "37°", r=110, size=40)
        tc = kt + 0.9 if chao else C["s11.c"]
        sx, sy = ("cos", "sen") if chao else ("sen", "cos")
        E.foco(c, t, tc, 0.5, lambda a, O=O, sx=sx, sy=sy: (E.formula(c, f"x: v · {sx}", O[0] + 20, O[1] + 85, 56, "g", TINTA, a),
                                                          E.formula(c, f"y: v · {sy}", O[0] + 20, O[1] + 160, 56, "g", TINTA, a)))
        E.foco(c, t, kt + 0.1, 0.4, lambda a, O=O, chao=chao: centro(c, "ângulo com o chão" if chao else "ângulo com a vertical", O[0] + 260, 310, 50, "i", TINTA2, a))
    E.frase(c, t, C["s11.d"], ps("o cosseno fica com o eixo que", "i", 54, TINTA2) + [("encosta", "g", 54, COR)] + ps("no ângulo", "i", 54, TINTA2),
            W / 2, 1020, "center", 0.08)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def s12():
        E.frase(c, t, C["s12"], ps("agora, o atalho", "i", 76, CLARO), W / 2, 150, "center")
        E.frase(c, t, C["s12.a"], [("37°", "g", 72, BR), ("e", "i", 72, CLARO), ("53°", "g", 72, BR), ("=", "g", 72, CLARO), ("3 · 4 · 5", "g", 72, BR)],
                W / 2, 270, "center", 0.14)
        O, P, Q = (1180, 820), (1660, 820), (1660, 460)
        E.foco(c, t, C["s12.a"] + 0.6, 0.5, lambda a: F.poli(c, [O, P, Q, O], 1.0, BR, a, 6))
        E.foco(c, t, C["s12.a"] + 0.9, 0.4, lambda a: (centro(c, "4", 1420, 900, 60, "g", CLARO, a), centro(c, "3", 1720, 660, 60, "g", CLARO, a),
                                                      centro(c, "5", 1370, 600, 60, "g", CLARO, a)))
        if t >= C["s12.a"] + 1.0:
            E.angulo(c, t, C["s12.a"] + 1.0, O, P, Q, "37°", r=90, cor=CLARO, size=40)
            E.angulo(c, t, C["s12.a"] + 1.4, Q, O, P, "53°", r=70, cor=CLARO, size=40)
        E.frase(c, t, C["s12.b"], [("÷ 5", "g", 70, BR)], XE, 470)
        E.frase(c, t, C["s12.c"], [("4", "g", 70, BR)] + ps("partes: eixo que encosta", "i", 60, CLARO), XE, 590, passo=0.1)
        E.frase(c, t, C["s12.d"], [("3", "g", 70, BR)] + ps("partes: o outro", "i", 60, CLARO), XE, 700, passo=0.1)
        E.frase(c, t, lerp(C["s12.d"], C["s12.e"], 0.6), ps("com 53°, ao contrário", "i", 52, CLARO), XE, 790, passo=0.08)
        E.frase(c, t, C["s12.e"], [("20 ÷ 5 = 4", "g", 64, BR), ("→", "g", 64, CLARO), ("16", "g", 64, BR), ("e", "i", 64, CLARO), ("12", "g", 64, BR)], XE, 930, passo=0.14)
    E.saida(c, t, C["s13"] - 0.1, s12)
    if t < C["s13"]:
        return
    E.formula_em(c, t, C["s13.a"], "0,8 = f{4}{5}     0,6 = f{3}{5}", W / 2, 380, 110, "g", BR, "center")
    E.frase(c, t, C["s13.b"], [("não", "g", 66, ERRADO), ("serve:", "i", 70, CLARO), ("30°,", "g", 66, BR), ("45°,", "g", 66, BR), ("60°", "g", 66, BR)], W / 2, 680, "center", 0.12)
    E.frase(c, t, C["s13.b"] + 1.6, ps("aí, use a tabela dos notáveis", "i", 64, CLARO), W / 2, 800, "center", 0.1)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s14"], ps("hora de testar", "i", 72, COR), XE, 200)
    E.frase(c, t, C["s14.a"], [("chute:", "i", 72)], XE, 340)
    E.foco(c, t, C["s14.a"] + 0.3, 0.5, lambda a: F.medida(c, 25, "m/s", XE + 230, 340, 96, COR, a))
    E.frase(c, t, C["s14.b"], [("37°", "g", 72), ("com", "i", 72), ("o", "i", 72), ("chão", "i", 72)], XE, 460, passo=0.12)
    E.frase(c, t, C["s14.c"], [("componentes", "g", 72), ("x", "g", 72, COR), ("e", "i", 72), ("y?", "g", 72, COR)], XE, 620, passo=0.12)
    E.frase(c, t, C["s14.d"], ps("e se o 37° fosse", "i", 62) + [("com a vertical?", "g", 60, COR)], XE, 780, passo=0.1)
    if t < C["s15"]:
        O, u = (1250, 860), 22
        B = (O[0] + 20 * u, O[1] - 15 * u)
        E.foco(c, t, C["s14.a"], 0.4, lambda a: (F.chao(c, 1100, 1840, O[1] + 36, a), E.bola(c, O[0], O[1], 34, a=a)))
        F.vetor(c, t, C["s14.a"] + 0.3, O, B, None, "25 m/s", F.VEL, 12, size=54)
        if t >= C["s14.b"]:
            E.angulo(c, t, C["s14.b"], O, (O[0] + 200, O[1]), B, "37°", r=110)
    else:
        E.relogio(c, t, C["s15.a"], cx=1460, cy=440, r=200)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    def s16():
        O, u = (1220, 880), 22
        B = (O[0] + 20 * u, O[1] - 15 * u)
        E.foco(c, t, C["s16"], 0.4, lambda a: (F.chao(c, 1080, 1840, O[1] + 36, a), E.bola(c, O[0], O[1], 34, a=a)))
        F.vetor(c, t, C["s16"] + 0.2, O, B, None, "25 m/s", F.VEL, 12, size=50)
        if t >= C["s16.b"]:
            E.angulo(c, t, C["s16.b"], O, (O[0] + 200, O[1]), B, "37°", r=110)
        comp(c, t, C["s16.c"], O, (B[0], O[1]), "20 m/s", lado=1)
        comp(c, t, C["s16.d"], O, (O[0], B[1]), "15 m/s", lado=1)
        E.formula_em(c, t, C["s16.a"], "25 ÷ 5 = 5", XE, 260, 90, "g", TINTA)
        E.frase(c, t, C["s16.b"], ps("ângulo com o chão: encosta no", "i", 54, TINTA2) + [("x", "g", 56, COR)], XE, 380, passo=0.08)
        E.formula_em(c, t, C["s16.c"], "x: 5 · 4 = 20", XE, 520, 90, "g", TINTA)
        E.formula_em(c, t, C["s16.d"], "y: 5 · 3 = 15", XE, 660, 90, "g", TINTA)
        E.frase(c, t, C["s16.e"], [("15 · 20 · 25", "g", 64, CERTO), ("=", "g", 64, TINTA2), ("3 · 4 · 5", "g", 64), ("× 5", "g", 64, COR)], XE, 830, passo=0.14)
    E.saida(c, t, C["s17"] - 0.1, s16)
    if t < C["s17"]:
        return
    O = (1250, 900)
    B = (O[0] + 15 * 22, O[1] - 20 * 22)
    E.foco(c, t, C["s17"], 0.4, lambda a: (M.line(c, O[0] - 20, O[1], O[0] + 520, O[1], TINTA, a, 4), M.line(c, O[0], O[1] + 20, O[0], O[1] - 520, TINTA, a, 4)))
    F.vetor(c, t, C["s17"] + 0.2, O, B, None, "25 m/s", F.VEL, 12, size=50)
    if t >= C["s17.a"]:
        E.angulo(c, t, C["s17.a"], O, (O[0], O[1] - 200), B, "37°", r=120)
    comp(c, t, C["s17.b"], O, (O[0], B[1]), "20 m/s", lado=1)
    comp(c, t, C["s17.c"], O, (B[0], O[1]), "15 m/s", lado=-1)
    E.frase(c, t, C["s17"], ps("ângulo com a vertical:", "i", 64), XE, 260, passo=0.1)
    E.frase(c, t, C["s17.a"], ps("encosta no", "i", 64) + [("y", "g", 70, COR)], XE, 370, passo=0.1)
    E.formula_em(c, t, C["s17.b"], "y: 5 · 4 = 20", XE, 560, 90, "g", TINTA)
    E.formula_em(c, t, C["s17.c"], "x: 5 · 3 = 15", XE, 700, 90, "g", TINTA)
    pilula_em(c, t, C["s17.c"] + 0.8, "tudo troca", XE + 260, 860, 56, E.COR)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def s18():
        resumo(c, t, C, "s18", (("s18.a", [("componentes", "g", 70, COR), ("=", "g", 70, TINTA2), ("catetos", "i", 70)]),
                                ("s18.b", [("encosta", "i", 70), ("no", "i", 70), ("ângulo:", "i", 70), ("cosseno", "g", 70, COR)]),
                                ("s18.c", [("some", "i", 70), ("x,", "g", 70, COR), ("some", "i", 70), ("y,", "g", 70, COR), ("Pitágoras", "g", 70)])))
    E.saida(c, t, C["s19"] - 0.1, s18)
    if t < C["s19"]:
        return
    E.frase(c, t, C["s19"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C["s19.a"], [("lançamento", "g", 110, COR)], XE, 400)
    E.frase(c, t, C["s19.a"] + 0.5, [("oblíquo", "g", 110, COR)], XE, 530)
    O = (330, 940)
    pts = [(O[0] + k * 9, O[1] - (k * 9) * 0.75 + (k * 9) ** 2 * 0.0014) for k in range(0, 61)]
    if t >= C["s19.a"] + 0.6:
        F.poli(c, pts, ease_io(prog(t, C["s19.a"] + 0.6, 1.2)), TINTA2, 1.0, 4, dash=E.TRACO)
    F.vetor(c, t, C["s19.a"] + 0.4, O, (O[0] + 240, O[1] - 180), None, None, F.VEL, 10)
    comp(c, t, C["s19.b"], O, (O[0] + 240, O[1]), None)
    E.foco(c, t, C["s19.b"] + 0.3, 0.4, lambda a: E.escreve(c, "para a frente", O[0] + 270, O[1] + 14, 44, "i", TINTA2, a))
    comp(c, t, C["s19.c"], O, (O[0], O[1] - 180), None)
    E.foco(c, t, C["s19.c"] + 0.3, 0.4, lambda a: E.escreve(c, "para cima", O[0] - 70, O[1] - 210, 44, "i", TINTA2, a))
    fim_inscreva(c, t, C, "s19", "s19.d", "s19.e")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, decompor=b_decompor, bola=b_bola, eixos=b_eixos, erro=b_erro, atalho=b_atalho,
              questao=b_questao, resposta=b_resposta, fim=b_fim)
