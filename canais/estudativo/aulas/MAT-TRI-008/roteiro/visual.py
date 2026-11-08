"""Visual — Estudativo · MAT-TRI-008: seno e cosseno lidos no ciclo (sen 90° = 1, cos 180° = −1), sinais por quadrante e "to, se, ta, co".
Linguagem da trigonometria (MAT-TRI-001 e 007): o seno é o cateto oposto e o cosseno o adjacente, então guardam as cores fixas —
seno em âmbar (OPO), cosseno em petróleo (ADJ; ADJ_ESC no palco escuro), o raio = hipotenusa em índigo (HIP). O seno é sempre um
traço vertical (a altura de P) e o cosseno um traço horizontal (no eixo x). Sinais: "+" em verde e "−" em vermelho, na tabela
dos quatro quadrantes, que se preenche no tempo da fala. Resposta na pílula; erro em vermelho; atalho no palco escuro.
A figura não mente: P está de verdade no ângulo dito (30°, 90°, 180°, 200°, 270°) e as alturas e larguras são as do ciclo de raio 1.
Peças locais: ciclo() (eixos, circunferência, −1 e 1), leitura() (arco, P, raio, sen e cos de um ângulo que pode girar),
meio_plano() (metade do ciclo pintada), tabela_sinais() (sen, cos e tg nos 4 quadrantes), resp(), pilula().
Todo instante vem de C[...] (marcadores do roteiro), para acompanhar a voz real quando ela chegar."""
import math
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Trigonometria")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-TRI-008_seno_cosseno_e_tangente_no_ciclo.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("leitura", "eixos", "sinais", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
AMBAR = "#D98A00"
HIP, OPO, ADJ = E.COR, AMBAR, "#0E9AA7"      # cor fixa de cada lado da trigonometria
ADJ_ESC = "#3CC7D3"
S = lambda g: math.sin(math.radians(g))
Cs = lambda g: math.cos(math.radians(g))
assert abs(S(30) - 0.5) < 1e-12 and abs(S(90) - 1) < 1e-12 and abs(Cs(90)) < 1e-12 and abs(Cs(180) + 1) < 1e-12 and abs(S(180)) < 1e-12
assert S(200) < 0 and Cs(200) < 0 and S(200) / Cs(200) > 0 and 180 < 200 < 270 and abs(S(270) + 1) < 1e-12
SINAIS = {"sen": "++−−", "cos": "+−−+", "tg": "+−+−"}
for q, g in enumerate((45, 135, 225, 315)):
    assert (S(g) > 0) == (SINAIS["sen"][q] == "+") and (Cs(g) > 0) == (SINAIS["cos"][q] == "+") and (S(g) / Cs(g) > 0) == (SINAIS["tg"][q] == "+")


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def fcen(c, t, t0, s, cx, y, size, cor=None):
    E.formula_em(c, t, t0, s, cx, y, size, "g", cor, "center")


def resp(c, t, t0, s, cx, cy, size=76, alto=1.75, cor=None):
    def f(a):
        w = E.formula(c, s, 0, 0, size, a=0) + size * 1.1
        h = size * alto
        M.rrect(c, cx - w / 2, cy - h / 2, w, h, h / 2, cor or E.COR, a, shadow=True)
        E.formula(c, s, cx, cy + size * 0.36, size, "g", BR, a, "center")
    E.foco(c, t, t0, 0.5, f)


def pilula(c, t, t0, s, cx, cy, size=64):
    E.foco(c, t, t0, 0.5, lambda a: E.pilula(c, s, cx, cy, size, "g", a=a, cor=E.SOBRE))


def pt(cx, cy, r, ang):
    return cx + r * Cs(ang), cy - r * S(ang)


def ciclo(c, t, t0, cx, cy, r, escuro=False, tq=None, marcas=True):
    if t < t0:
        return
    tinta = BR if escuro else TINTA
    q = ep(t, t0, 0.6)
    M.arrow(c, cx - r - 70, cy, cx + r + 90, cy, tinta, q, 4, 20, q)
    M.arrow(c, cx, cy + r + 70, cx, cy - r - 90, tinta, q, 4, 20, q)
    c.drawArc(skia.Rect.MakeXYWH(cx - r, cy - r, 2 * r, 2 * r), 0, -360 * ease_io(prog(t, t0 + 0.2, 0.9)), False, M.paint(tinta, 1.0, stroke=5))
    sec = CLARO if escuro else TINTA2
    E.foco(c, t, t0 + 0.6, 0.4, lambda a: (E.escreve(c, "x", cx + r + 70, cy + 56, 50, "i", sec, a),
                                           E.escreve(c, "y", cx + 22, cy - r - 66, 50, "i", sec, a)))
    if marcas:
        for s, X, Y in (("1", cx + r + 14, cy + 52), ("−1", cx - r - 74, cy + 52), ("1", cx - 44, cy - r - 12), ("−1", cx - 74, cy + r + 52)):
            E.foco(c, t, t0 + 0.7, 0.4, lambda a, s=s, X=X, Y=Y: E.escreve(c, s, X, Y, 44, "b", tinta, a))
    if tq is not None:
        for i, ang in enumerate((45, 135, 225, 315)):
            X, Y = pt(cx, cy, r * 0.62, ang)
            E.foco(c, t, tq + 0.12 * i, 0.4, lambda a, i=i, X=X, Y=Y: centro(c, f"{i + 1}º", X, Y + 20, 54, "g", CINZA if not escuro else CLARO, a))


def leitura(c, t, cx, cy, r, ang, tp, tsen=None, tcos=None, traio=None, tri=None, proj=None, escuro=False, rot=True, cor_sen=None, cor_cos=None,
            lado=True, size=50):
    """o ponto P no ângulo ang (graus, pode mudar com t): arco desde 0, P, linhas de chamada, sen (vertical, âmbar) e cos (no eixo x,
    petróleo). lado = o seno no lado vertical do triângulo; proj = instante em que o seno aparece também no eixo y"""
    if t < tp:
        return
    tinta = BR if escuro else TINTA
    cs, cc = cor_sen or OPO, cor_cos or (ADJ_ESC if escuro else ADJ)
    q = ep(t, tp, 0.4)
    P = pt(cx, cy, r, ang)
    ra = r * 0.2
    if abs(ang) > 0.5:
        path = skia.Path(); path.moveTo(cx, cy); path.arcTo(skia.Rect.MakeXYWH(cx - ra, cy - ra, 2 * ra, 2 * ra), 0, -ang, False); path.close()
        c.drawPath(path, M.paint(E.COR, 0.18 * q))
        c.drawArc(skia.Rect.MakeXYWH(cx - r, cy - r, 2 * r, 2 * r), 0, -ang, False, M.paint(E.COR if not escuro else CLARO, q, stroke=9, cap_round=True))
    if tri is not None and t >= tri:
        path = skia.Path(); path.addPoly([(cx, cy), (P[0], cy), P], True)
        c.drawPath(path, M.paint(E.COR, 0.12 * ep(t, tri, 0.5)))
        if abs(S(ang)) > 0.08 and abs(Cs(ang)) > 0.08:
            E.angulo(c, t, tri, (P[0], cy), (cx, cy), P, r=32, preenche=0.0)
    if traio is not None and t >= traio:
        M.line(c, cx, cy, *P, HIP if not escuro else CLARO, 1.0, 8, progress=ep(t, traio, 0.5))
    if tcos is not None and t >= tcos:
        k = ep(t, tcos, 0.5)
        M.line(c, *P, P[0], cy, tinta, 0.6 * k, 3, dash=E.TRACO)
        if abs(Cs(ang)) > 0.01:
            M.line(c, cx, cy, P[0], cy, cc, 1.0, 13, progress=k, cap_round=False)
            if rot:
                E.foco(c, t, tcos + 0.3, 0.4, lambda a: centro(c, "cos", (cx + P[0]) / 2, cy + (62 if S(ang) >= 0 else -26), size, "g", cc, a))
    if tsen is not None and t >= tsen:
        k = ep(t, tsen, 0.5)
        if abs(S(ang)) > 0.01:
            if lado:
                M.line(c, P[0], cy, *P, cs, 1.0, 13, progress=k, cap_round=False)
            if rot:
                E.foco(c, t, tsen + 0.3, 0.4, lambda a: E._cola(c, "sen", P[0], (cy + P[1]) / 2, 1, 0, 22, size, "g", cs, a))
    if proj is not None and t >= proj and abs(S(ang)) > 0.01:
        k = ep(t, proj, 0.5)
        M.line(c, *P, cx, P[1], tinta, 0.6 * k, 3, dash=E.TRACO)
        M.line(c, cx, cy, cx, P[1], cs, 1.0, 13, progress=k, cap_round=False)
    kP = ease_back(prog(t, tp, 0.4))
    c.drawCircle(*P, 15 * kP, M.paint(E.COR if not escuro else CLARO))
    c.drawCircle(*P, 15 * kP, M.paint(BR if not escuro else "#07070F", 1.0, stroke=3))
    no_eixo = min(ang % 90, 90 - ang % 90) < 3
    dP = math.radians(ang - 135 if no_eixo else ang + 25)   # em cima de um eixo, o nome vai para dentro do ciclo
    E.foco(c, t, tp + 0.1, 0.4, lambda a: E._cola(c, "P", *P, math.cos(dP), -math.sin(dP), 18, 56, "g", tinta, a))
    return P


def meio_plano(c, cx, cy, r, ini, varre, cor, a):
    """pedaço do ciclo pintado (ini, varre em graus, anti-horário)"""
    if a <= 0:
        return
    path = skia.Path(); path.moveTo(cx, cy)
    path.arcTo(skia.Rect.MakeXYWH(cx - r, cy - r, 2 * r, 2 * r), -ini, -varre, False); path.close()
    c.drawPath(path, M.paint(cor, 0.16 * a))


def tabela_sinais(c, t, x, y, t0, cel, cw=150, rh=110, size=64, escuro=False):
    """linhas sen, cos, tg; colunas 1º a 4º. cel = {(função, quadrante 0..3): instante}; o sinal vem de SINAIS"""
    q = ep(t, t0, 0.5)
    if q <= 0:
        return
    tinta = BR if escuro else TINTA
    w0 = 140
    for j in range(4):
        centro(c, f"{j + 1}º", x + w0 + j * cw + cw / 2, y, 52, "g", COR if not escuro else CLARO, q)
    M.line(c, x, y + 26, x + w0 + 4 * cw, y + 26, TINTA2 if not escuro else CLARO, q, 3)
    for i, f in enumerate(("sen", "cos", "tg")):
        yy = y + 26 + rh * i + rh / 2
        cor_f = OPO if f == "sen" else (ADJ if not escuro else ADJ_ESC) if f == "cos" else tinta
        E.escreve(c, f, x + 6, yy + size * 0.36, size * 0.9, "g", cor_f, q)
        for j in range(4):
            t1 = cel.get((f, j))
            if t1 is None:
                continue
            s = SINAIS[f][j]
            E.foco(c, t, t1, 0.35, lambda a, s=s, j=j, yy=yy: centro(c, s, x + w0 + j * cw + cw / 2, yy + size * 0.36, size * 1.1, "g",
                                                                     CERTO if s == "+" else ERRADO, a))


# ---------------- gancho ----------------
GX, GY_, GR = 1380, 560, 280


def b_gancho(c, t, C, b):
    a1, b1, c1, d1 = (C[f"s01.{k}"] for k in "abcd")

    def um():
        E.foco(c, t, a1, 0.5, lambda a: E.formula(c, "cos 180°", XE, 440, 180, "g", TINTA, a))
        E.frase(c, t, a1 + 1.4, ps("nenhum triângulo retângulo", "i", 56, TINTA2), XE, 560, "left", 0.08)
        E.frase(c, t, a1 + 2.4, ps("tem ângulo de 180°", "i", 56, TINTA2), XE, 640, "left", 0.08)
        E.frase(c, t, b1, ps("mesmo assim,", "i", 64) + [("existe:", "g", 68, COR)], XE, 790, "left", 0.1)
        E.foco(c, t, c1, 0.5, lambda a: E.formula(c, "= −1", XE + 560, 940, 150, "g", ADJ, a))
        ciclo(c, t, d1 - 0.6, GX, GY_, GR, marcas=False)
        ang = lerp(0, 180, ease_io(prog(t, d1, 1.2)))
        leitura(c, t, GX, GY_, GR, ang, d1, tcos=d1, rot=False)
        E.foco(c, t, d1 + 1.0, 0.4, lambda a: E.escreve(c, "−1", GX - GR - 80, GY_ + 60, 56, "g", ADJ, a))
    E.saida(c, t, C["s02"] - 0.1, um)
    if t >= C["s02"]:
        ta, tb = C["s02.a"], C["s02.b"]
        E.foco(c, t, tb - 0.2, 0.7, lambda a: E.bola(c, 1500, 560, 250 * ease_back(prog(t, tb - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, ps("até o fim desta aula", "i", 90), XE, 280, passo=0.14)
        E.frase(c, t, lerp(ta, tb, 0.3), [("seno", "g", 100, OPO)] + ps("e", "i", 90) + [("cosseno", "g", 100, ADJ)], XE, 440, passo=0.14)
        E.frase(c, t, lerp(ta, tb, 0.6), ps("direto no", "i", 84) + [("ciclo", "g", 96, COR)], XE, 590, passo=0.14)
        E.foco(c, t, tb + 0.1, 0.5, lambda a: (centro(c, "+ sinais", 1500, 545, 80, "g", E.SOBRE, a),
                                               centro(c, "com macete", 1500, 630, 72, "i", E.SOBRE, a)))


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"] + 0.3, ps("você precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "2", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 860, 960
    kb, kc = C["s03.b"], C["s03.c"]
    p = ep(t, kb, 0.5)
    E.caixa_pontilhada(c, x, 170, w, 340, p, prog_=p)
    E.foco(c, t, kb + 0.2, 0.5, lambda a: E.formula(c, "sen = f{oposto}{hipotenusa}", x + 44, 300, 62, "g", TINTA, a))
    E.foco(c, t, lerp(kb, kc, 0.55), 0.5, lambda a: E.formula(c, "cos = f{adjacente}{hipotenusa}", x + 44, 450, 62, "g", TINTA, a))
    p = ep(t, kc, 0.5)
    E.caixa_pontilhada(c, x, 570, w, 260, p, prog_=p)
    E.frase(c, t, kc + 0.1, [("o ciclo:", "i", 60)] + [("raio 1", "g", 62, COR)], x + 44, 660)
    E.frase(c, t, kc + 1.0, ps("partida à direita, giro anti-horário", "i", 52, TINTA2), x + 44, 760, "left", 0.08)
    E.cursor(c, x + w - 30, lerp(480, 800, ease_io(prog(t, kc - 0.35, 0.5))), ep(t, kb, 0.4))
    E.frase(c, t, C["s03.end"] - 2.4, ps("faltou alguma?", "i", 58, COR) + ps("procure no canal", "i", 58), x, 1000, "left", 0.12)


# ---------------- leitura ----------------
CX, CY, CR = 590, 560, 330


def b_leitura(c, t, C, b):
    a4, b4, c4, d4 = (C[f"s04.{k}"] for k in "abcd")
    a5, b5, c5, d5 = (C[f"s05.{k}"] for k in "abcd")
    a6, b6, c6, d6 = (C[f"s06.{k}"] for k in "abcd")
    X = 1420
    ciclo(c, t, C["s04"] - 0.3, CX, CY, CR)
    ang = lerp(48, 30, ease_io(prog(t, c6 - 0.6, 0.9)))
    P = leitura(c, t, CX, CY, CR, ang, a4, tsen=a5, tcos=c5, traio=d4, tri=c4, proj=a6)
    if t >= b4 and t < a5:  # a linha que desce de P
        M.line(c, *pt(CX, CY, CR, ang), pt(CX, CY, CR, ang)[0], CY, TINTA, 1.0, 5, dash=E.TRACO, progress=ep(t, b4, 0.6))
    E.foco(c, t, d4 + 0.3, 0.4, lambda a: E._meio(c, "1", (CX + P[0]) / 2 - 30, (CY + P[1]) / 2 - 24, 54, "g", HIP, a))
    if t >= c6:
        E.foco(c, t, c6 + 0.4, 0.4, lambda a: (M.line(c, CX - 14, CY - CR / 2, CX + 14, CY - CR / 2, OPO, a, 5),
                                               E.formula(c, "f{1}{2}", CX - 70, CY - CR / 2 + 20, 50, "g", OPO, a, "center")))

    def quatro():
        E.frase(c, t, a4, ps("arco no", "i", 60) + [("1º quadrante", "g", 64, COR)], X, 220, "center", 0.1)
        E.frase(c, t, a4 + 1.2, ps("com a ponta em", "i", 60) + [("P", "g", 64)], X, 310, "center", 0.1)
        E.frase(c, t, b4, ps("desça de P até o", "i", 60) + [("eixo x", "g", 64)], X, 450, "center", 0.1)
        E.frase(c, t, c4, [("triângulo retângulo", "g", 66, COR)], X, 590, "center", 0.1)
        E.frase(c, t, d4, [("hipotenusa", "g", 64, HIP)] + ps("= raio =", "i", 60) + [("1", "g", 66, HIP)], X, 730, "center", 0.1)
    E.saida(c, t, C["s05"] - 0.1, quatro)

    def cinco():
        fcen(c, t, a5, "sen = f{oposto}{1}", X, 260, 80, OPO)
        E.frase(c, t, b5, ps("=", "b", 60) + [("a altura de P", "g", 64, OPO)], X, 410, "center", 0.1)
        fcen(c, t, c5, "cos = f{adjacente}{1}", X, 610, 80, ADJ)
        E.frase(c, t, d5, ps("=", "b", 60) + [("a horizontal de P", "g", 64, ADJ)], X, 760, "center", 0.1)
    if t >= C["s05"] - 0.1:
        E.saida(c, t, C["s06"] - 0.1, cinco)
    if t < C["s06"] - 0.1:
        return
    E.frase(c, t, a6, [("sen", "g", 72, OPO)] + ps("→ eixo vertical,", "b", 54) + [("y", "i", 66)], X, 240, "center", 0.1)
    E.frase(c, t, b6, [("cos", "g", 72, ADJ)] + ps("→ eixo horizontal,", "b", 54) + [("x", "i", 66)], X, 380, "center", 0.1)
    E.frase(c, t, c6, ps("em 30°, P na altura", "i", 58) + [("1/2", "g", 64, OPO)], X, 560, "center", 0.1)
    resp(c, t, d6, "sen 30° = f{1}{2}", X, 740, 70, 2.4, cor=OPO)


# ---------------- pontos nos eixos ----------------
def b_eixos(c, t, C, b):
    a7, b7, c7, d7 = (C[f"s07.{k}"] for k in "abcd")
    a8, b8, c8, d8 = (C[f"s08.{k}"] for k in "abcd")
    X = 1420
    ciclo(c, t, C["s07"] - 0.3, CX, CY, CR)
    ang = lerp(lerp(30, 90, ease_io(prog(t, b7 - 0.4, 1.0))), 180, ease_io(prog(t, a8 - 0.2, 1.2)))
    P = leitura(c, t, CX, CY, CR, ang, C["s07"], tsen=C["s07"], tcos=C["s07"], lado=False, proj=C["s07"], rot=False)
    if b7 <= t < a8 + 0.6:
        E.foco(c, t, c7, 0.4, lambda a: E.escreve(c, "sen = 1", CX + 30, CY - CR / 2, 50, "g", OPO, a))
    if t >= b8:
        E.foco(c, t, b8, 0.4, lambda a: E.escreve(c, "cos = −1", CX - CR + 10, CY + 64, 50, "g", ADJ, a))
    if t >= d8:  # a faixa de −1 a 1
        k = ep(t, d8, 0.6)
        c.drawRect(skia.Rect.MakeXYWH(CX - CR, CY - CR, 2 * CR, 2 * CR), M.paint(COR, k, stroke=4))
        E.escreve(c, "tudo entre −1 e 1", 150, CY + CR + 130, 46, "b", COR, k)

    def sete():
        E.frase(c, t, a7, ps("vale para", "i", 60) + [("qualquer arco", "g", 64, COR)], X, 220, "center", 0.1)
        E.frase(c, t, a7 + 1.4, ps("mesmo sem triângulo", "i", 54, TINTA2), X, 300, "center", 0.08)
        E.frase(c, t, b7, [("90°:", "g", 64, COR)] + ps("P no topo", "i", 60), X, 440, "center", 0.1)
        fcen(c, t, c7, "sen 90° = 1", X, 600, 90, OPO)
        fcen(c, t, d7, "cos 90° = 0", X, 760, 90, ADJ)
    E.saida(c, t, C["s08"] - 0.1, sete)
    if t < C["s08"] - 0.1:
        return
    E.frase(c, t, a8, [("180°:", "g", 64, COR)] + ps("P à esquerda, no −1", "i", 58), X, 220, "center", 0.1)
    fcen(c, t, b8, "cos 180° = −1", X, 380, 86, ADJ)
    fcen(c, t, c8, "sen 180° = 0", X, 530, 86, OPO)
    E.frase(c, t, c8 + 1.2, ps("nenhuma altura", "i", 52, TINTA2), X, 610, "center", 0.08)
    E.foco(c, t, d8, 0.5, lambda a: E.caixa_pontilhada(c, X - 330, 700, 660, 250, a, COR, prog_=ep(t, d8, 0.6)))
    fcen(c, t, d8 + 0.2, "−1 ≤ sen ≤ 1", X, 800, 72, OPO)
    fcen(c, t, d8 + 0.6, "−1 ≤ cos ≤ 1", X, 905, 72, ADJ)


# ---------------- sinais ----------------
def b_sinais(c, t, C, b):
    a9, b9, c9 = (C[f"s09.{k}"] for k in "abc")
    a0, b0, c0 = (C[f"s10.{k}"] for k in "abc")
    a1, b1, c1, d1 = (C[f"s11.{k}"] for k in "abcd")
    cx, cy, r = 470, 560, 280
    ciclo(c, t, C["s09"] - 0.3, cx, cy, r, tq=C["s09"], marcas=False)
    # o que está sendo explicado, pintado no ciclo
    k9 = ep(t, a9, 0.5) * (1 - ep(t, C["s10"] - 0.3, 0.4))
    meio_plano(c, cx, cy, r, 0, 180, CERTO, k9)
    meio_plano(c, cx, cy, r, 180, 180, ERRADO, k9 * ep(t, c9, 0.4))
    if k9 > 0:
        M.arrow(c, cx + r + 120, cy + 120, cx + r + 120, cy - 140, OPO, k9, 8, 26, 1.0)
        E.escreve(c, "sen", cx + r + 150, cy - 40, 54, "g", OPO, k9)
    k0 = ep(t, a0, 0.5) * (1 - ep(t, C["s11"] - 0.3, 0.4))
    meio_plano(c, cx, cy, r, -90, 180, CERTO, k0)
    meio_plano(c, cx, cy, r, 90, 180, ERRADO, k0 * ep(t, c0, 0.4))
    if k0 > 0:
        M.arrow(c, cx - 140, cy + r + 110, cx + 160, cy + r + 110, ADJ, k0, 8, 26, 1.0)
        E.escreve(c, "cos", cx + 180, cy + r + 128, 54, "g", ADJ, k0)
    k1 = ep(t, b1, 0.5)
    for ini in (0, 180):
        meio_plano(c, cx, cy, r, ini, 90, CERTO, k1)
    for ini in (90, 270):
        meio_plano(c, cx, cy, r, ini, 90, ERRADO, k1 * ep(t, c1, 0.4))
    # tabela
    X0, Y0 = 1000, 260
    cel = {}
    for j, tk in ((0, b9), (1, b9 + 0.3), (2, c9), (3, c9 + 0.3)):
        cel[("sen", j)] = tk
    for j, tk in ((0, b0), (3, b0 + 0.3), (1, c0), (2, c0 + 0.3)):
        cel[("cos", j)] = tk
    for j, tk in ((0, b1), (2, b1 + 0.3), (1, c1), (3, c1 + 0.3)):
        cel[("tg", j)] = tk
    tabela_sinais(c, t, X0, Y0, C["s09"], cel, 190, 120, 62)
    if t < C["s10"] - 0.1:
        E.frase(c, t, a9, ps("acima do eixo x:", "i", 52) + [("altura +", "g", 56, CERTO)], X0, 720, "left", 0.08)
    if C["s10"] - 0.1 <= t < C["s11"] - 0.1:
        E.frase(c, t, a0, ps("à direita do eixo y:", "i", 52) + [("horizontal +", "g", 56, CERTO)], X0, 720, "left", 0.08)
    if t >= C["s11"] - 0.1:
        E.foco(c, t, a1, 0.5, lambda a: E.formula(c, "tg = f{sen}{cos}", X0, 760, 64, "g", TINTA, a))
        E.frase(c, t, b1, ps("iguais", "i", 50) + [("+", "g", 56, CERTO)] + ps("· diferentes", "i", 50) + [("−", "g", 56, ERRADO)], X0 + 470, 760, "left", 0.08)
        E.foco(c, t, d1, 0.5, lambda a: E.formula(c, "tg 90° = f{1}{0}", X0, 940, 64, "g", ERRADO, a))
        E.frase(c, t, d1 + 1.2, [("não existe", "g", 58, ERRADO)], X0 + 470, 935, "left", 0.1)
        E.frase(c, t, d1 + 0.6, ps("cos 90° = 0", "b", 44, TINTA2), X0 + 470, 875, "left", 0.08)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    a2, b2, c2, d2 = (C[f"s12.{k}"] for k in "abcd")
    X = 1420
    ciclo(c, t, C["s12"] - 0.3, CX, CY, CR)
    leitura(c, t, CX, CY, CR, 180, C["s12"], rot=False)
    if t >= b2:  # a leitura errada: a horizontal
        k = ep(t, b2, 0.5) * (1 - ep(t, c2, 0.4))
        M.line(c, CX, CY, CX - CR, CY, ERRADO, k, 13, cap_round=False)
        E.escreve(c, "−1?", CX - CR + 20, CY + 66, 54, "g", ERRADO, k)
    if t >= c2:  # a altura de P: zero
        k = ep(t, c2, 0.5)
        P = pt(CX, CY, CR, 180)
        c.drawCircle(*P, 34, M.paint(CERTO, 1.0 * k, stroke=5))
        E.escreve(c, "altura 0", P[0] + 40, P[1] + 110, 50, "g", CERTO, k)
    if t >= d2:  # sobe e desce, vai e vem
        k = ep(t, d2, 0.5)
        M.arrow(c, CX + 40, CY, CX + 40, CY - 220, OPO, k, 8, 24, k)
        M.arrow(c, CX + 40, CY, CX + 40, CY + 220, OPO, k, 8, 24, k)
        M.arrow(c, CX, CY + 40, CX + 220, CY + 40, ADJ, k, 8, 24, k)
        M.arrow(c, CX, CY + 40, CX - 220, CY + 40, ADJ, k, 8, 24, k)
    E.frase(c, t, a2, ps("o erro:", "i", 62) + [("trocar os eixos", "g", 66, ERRADO)], X, 220, "center", 0.1)
    fcen(c, t, b2, "sen 180° = −1", X - 40, 380, 84, ERRADO)
    E.foco(c, t, b2 + 0.5, 0.5, lambda a: E.selo(c, X + 300, 350, 40, False, a))
    E.frase(c, t, c2 - 1.4, ps("seno é", "i", 58) + [("altura", "g", 62, OPO)], X, 510, "center", 0.1)
    fcen(c, t, c2, "sen 180° = 0", X - 40, 640, 84, CERTO)
    E.foco(c, t, c2 + 0.5, 0.5, lambda a: E.selo(c, X + 290, 610, 40, True, a))
    E.foco(c, t, d2, 0.5, lambda a: E.caixa_pontilhada(c, X - 380, 740, 760, 230, a, COR, prog_=ep(t, d2, 0.6)))
    E.frase(c, t, d2 + 0.1, [("seno", "g", 64, OPO)] + ps("sobe e desce", "i", 60), X, 830, "center", 0.1)
    E.frase(c, t, d2 + 0.8, [("cosseno", "g", 64, ADJ)] + ps("vai e vem", "i", 60), X, 925, "center", 0.1)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    a3, b3, c3, d3, e3 = (C[f"s13.{k}"] for k in "abcde")
    a4, b4, c4, d4, e4 = (C[f"s14.{k}"] for k in "abcde")
    cx, cy, r = 560, 580, 300
    ciclo(c, t, C["s13"] - 0.3, cx, cy, r, escuro=True, marcas=False)
    palavras = (("TO", "todos", b3, 45, BR), ("SE", "só seno", c3, 135, OPO), ("TA", "só tangente", d3, 225, BR), ("CO", "só cosseno", e3, 315, ADJ_ESC))
    for sil, nome, tk, ang, cor in palavras:
        X, Y = pt(cx, cy, r * 0.58, ang)
        E.foco(c, t, tk, 0.4, lambda a, X=X, Y=Y, sil=sil, nome=nome, cor=cor: (
            centro(c, sil, X, Y + 10, 96, "g", cor, a), centro(c, nome, X, Y + 70, 44, "i", CLARO, a)))
    arco_k = ep(t, b3, 0.4)
    if arco_k > 0:
        rr = r + 50
        c.drawArc(skia.Rect.MakeXYWH(cx - rr, cy - rr, 2 * rr, 2 * rr), -20, -320 * ease_io(prog(t, b3, e3 - b3 + 0.6)), False, M.paint(CLARO, arco_k * 0.7, stroke=5))
    X = 1440

    def treze():
        E.frase(c, t, C["s13"] + 0.2, ps("o macete dos sinais", "i", 64, CLARO), X, 220, "center", 0.1)
        E.foco(c, t, a3, 0.5, lambda a: centro(c, "to · se · ta · co", X, 400, 96, "g", BR, a))
        E.frase(c, t, e3 + 0.6, ps("na ordem do anti-horário", "i", 56, CLARO), X, 540, "center", 0.1)
    E.saida(c, t, C["s14"] - 0.1, treze)
    if t < C["s14"] - 0.1:
        return
    E.frase(c, t, a4, [("sen", "g", 64, OPO)] + ps("positivo em cima", "i", 58, CLARO), X, 220, "center", 0.1)
    E.frase(c, t, b4, [("cos", "g", 64, ADJ_ESC)] + ps("positivo à direita", "i", 58, CLARO), X, 330, "center", 0.1)
    E.frase(c, t, c4, [("tg", "g", 64, BR)] + ps("segue a regra de sinais", "i", 58, CLARO), X, 440, "center", 0.1)
    E.foco(c, t, d4, 0.5, lambda a: E.selo(c, X - 440, 610, 40, False, a))
    E.frase(c, t, d4, [("90°, 180°:", "g", 62, BR)] + ps("em cima dos eixos", "i", 54, CLARO), X + 30, 630, "center", 0.1)
    E.frase(c, t, d4 + 2.0, ps("um deles é zero, e", "i", 54, CLARO) + [("zero não tem sinal", "g", 56, BR)], X, 740, "center", 0.1)
    E.frase(c, t, e4, ps("aí,", "i", 66, CLARO) + [("leia no ciclo", "g", 72, BR)], X, 900, "center", 0.1)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    a5, b5, c5 = C["s15.a"], C["s15.b"], C["s15.c"]
    E.frase(c, t, C["s15"] + 0.2, ps("hora de testar", "i", 72, COR), XE, 200, passo=0.12)
    E.foco(c, t, a5, 0.5, lambda a: centro(c, "1", XE + 30, 380, 60, "g", COR, a))
    E.frase(c, t, a5, ps("no arco de", "i", 68) + [("200°", "g", 76, COR)], XE + 100, 380, "left", 0.1)
    E.frase(c, t, b5, ps("o sinal de", "i", 62) + [("sen,", "g", 66, OPO), ("cos", "g", 66, ADJ)] + ps("e", "i", 62) + [("tg", "g", 66)], XE + 100, 480, "left", 0.1)
    E.foco(c, t, c5, 0.5, lambda a: centro(c, "2", XE + 30, 640, 60, "g", COR, a))
    E.frase(c, t, c5, ps("quanto dá", "i", 68) + [("sen 270°?", "g", 76, OPO)], XE + 100, 640, "left", 0.1)
    E.relogio(c, t, C["s16.a"], 1560, 440, 170)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    a7, b7, c7, d7, e7 = (C[f"s17.{k}"] for k in "abcde")
    a8, b8, c8 = (C[f"s18.{k}"] for k in "abc")
    cx, cy, r = 560, 560, 300
    ciclo(c, t, C["s17"] - 0.3, cx, cy, r, tq=a7)
    ang = lerp(200, 270, ease_io(prog(t, a8 - 0.2, 1.0)))
    leitura(c, t, cx, cy, r, ang, a7, tsen=b7, tcos=c7, rot=t < C["s18"])
    if a7 <= t < C["s18"]:
        meio_plano(c, cx, cy, r, 180, 90, E.COR, ep(t, a7, 0.5))
    X = 1400

    def dezessete():
        E.frase(c, t, a7, [("200°:", "g", 66, COR)] + ps("entre 180° e 270°", "i", 56), X, 200, "center", 0.1)
        E.frase(c, t, a7 + 1.6, [("3º quadrante", "g", 64, COR)], X, 290, "center", 0.1)
        E.frase(c, t, b7, ps("embaixo:", "i", 58) + [("sen", "g", 64, OPO), ("−", "g", 72, ERRADO)], X, 430, "center", 0.1)
        E.frase(c, t, c7, ps("à esquerda:", "i", 58) + [("cos", "g", 64, ADJ), ("−", "g", 72, ERRADO)], X, 540, "center", 0.1)
        E.foco(c, t, d7, 0.5, lambda a: E.formula(c, "tg = f{−}{−} =", X - 40, 690, 72, "g", TINTA, a, "center"))
        E.foco(c, t, d7 + 0.6, 0.4, lambda a: centro(c, "+", X + 150, 700, 96, "g", CERTO, a))
        E.frase(c, t, e7, ps("macete: no 3º,", "i", 56) + [("só a tangente", "g", 60, COR)], X, 860, "center", 0.1)
    E.saida(c, t, C["s18"] - 0.1, dezessete)
    if t < C["s18"] - 0.1:
        return
    E.frase(c, t, a8, [("270°:", "g", 66, COR)] + ps("o ponto mais baixo", "i", 58), X, 260, "center", 0.1)
    E.frase(c, t, b8, ps("altura", "i", 62) + [("−1", "g", 72, OPO)], X, 430, "center", 0.1)
    resp(c, t, c8, "sen 270° = −1", X, 620, 76, cor=OPO)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s19"] + 0.2, [("resumindo", "i", 92, COR)], W / 2, 200, "center")
        itens = (("s19.a", "seno é a altura,", "eixo vertical", OPO), ("s19.b", "cosseno é a horizontal,", "eixo x", ADJ),
                 ("s19.c", "sinais:", "to, se, ta, co", COR))
        for i, (k, l1, l2, cor) in enumerate(itens):
            y = 380 + i * 200
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 230, y - 30, 56, a=a),
                                                         E.centro(c, str(i + 1), 230, y - 7, 64, "g", E.SOBRE, a)))
            E.frase(c, t, C[k] + 0.1, ps(l1, "i", 68) + [(l2, "g", 70, cor)], 320, y, "left", 0.1)
    t_fim = min(C["s20"] + 1.2, C["s20.a"] - 0.4)
    E.saida(c, t, t_fim, resumo)
    if t < t_fim:
        return
    a0, b0, c0 = C["s20.a"], C["s20.b"], C["s20.c"]
    E.frase(c, t, t_fim + 0.1, ps("na próxima aula", "i", 80), XE, 220, passo=0.12)
    E.foco(c, t, a0, 0.5, lambda a: E.formula(c, "sen 150°   cos 240°", XE, 370, 84, "g", COR, a))
    E.frase(c, t, b0, ps("viram um ângulo do", "i", 66) + [("1º quadrante", "g", 72, COR)], XE, 500, passo=0.1)
    E.frase(c, t, c0, ps("e o", "i", 66) + [("sinal", "g", 72, COR)] + ps("se ajusta", "i", 66), XE, 620, passo=0.1)
    E.foco(c, t, C["s20.d"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1440, 790, 76, estilo="g", a=a, cor=E.SOBRE))
    p = ease_io(prog(t, C["s20.d"] + 0.3, 0.8))
    E.cursor(c, lerp(1770, 1570, p), lerp(1030, 815, p), ep(t, C["s20.d"] + 0.2, 0.4))
    E.frase(c, t, C["s20.e"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 980, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, leitura=b_leitura, eixos=b_eixos, sinais=b_sinais, erro=b_erro, atalho=b_atalho,
              questao=b_questao, resposta=b_resposta, fim=b_fim)
