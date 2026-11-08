"""Visual — Estudativo · MAT-ANG-001: ângulos, medir em graus e classificar. Primeira aula de Geometria Plana.

LINGUAGEM VISUAL DA GEOMETRIA PLANA (as próximas aulas de ângulos e triângulos copiam daqui):
- Linhas, lados e ponteiros em tinta preta (TINTA). Linha auxiliar ou "fantasma" tracejada em TINTA2.
- O ângulo da vez é sempre um arco com a cunha clara na cor da matéria (E.angulo ou cunha()). Ângulo reto = quadradinho.
- Ângulos iguais têm a mesma cor: a 1ª família em COR (índigo), a 2ª em TINTA2 (cinza escuro). Vermelho só para erro, verde para certo.
- A parte que "sobra" ou "falta" (o lado maior do relógio, o pedaço que completa) vai em cinza (TINTA2, cunha bem clara).
- Medidas na grotesca ("g" ou "b"): a itálica não tem "°". Resposta final numa esfera (bola), como no resto do curso.
- Um ângulo que "se move" para provar algo: a cunha sai do lugar, viaja e assenta no destino, deixando o contorno tracejado
  no lugar de onde saiu (a peça voa() aparece a partir da MAT-ANG-002).
Peças locais desta aula: mostrador() e ponteiros() desenham o relógio; cunha() pinta um pedaço de volta; folha() é a folha de papel.
Todo instante vem de C[...] (marcadores do roteiro), para acompanhar a voz real quando ela chegar."""
import math
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Ângulos e Triângulos")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-ANG-001_angulos_medir_e_classificar.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("graus", "tipos", "atalho", "questao", "fim"))
BR = "#FFFFFF"
assert 360 // 2 == 180 and 360 // 4 == 90 and 90 // 3 == 30 and 12 * 30 == 360
assert 2 * 30 == 60 and 4 * 30 == 120 and (12 - 10) * 30 == 60 and 5 * 30 == 150 and 180 - 30 == 150


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças desta aula ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    """uma frase, palavra a palavra, no mesmo estilo"""
    return [(w, est, size, cor) for w in txt.split()]


def fcen(c, t, t0, s, cx, y, size, cor=None):
    E.formula_em(c, t, t0, s, cx, y, size, "g", cor, "center")


def bola_txt(c, t, t0, s, cx, cy, r, size, cor=None):
    """resposta na esfera"""
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r * ease_back(prog(t, t0, 0.5)), cor, a),
                                     centro(c, s, cx, cy + size * 0.36, size, "g", BR, a)))


def hora(cx, cy, rr, h):
    """ponto do mostrador na hora h, a rr do centro"""
    a = math.radians(h * 30)
    return cx + rr * math.sin(a), cy - rr * math.cos(a)


def tela(h):
    """ângulo de tela (graus, horário a partir da direita, como o skia) da hora h"""
    return h * 30 - 90


def cunha(c, cx, cy, r, ini, varre, cor=None, a=1.0, alfa=0.22, borda=5):
    """pedaço de volta pintado: de `ini` girando `varre` graus (ângulos de tela)"""
    if a <= 0 or abs(varre) < 0.2:
        return
    cor = cor or E.COR
    ret = skia.Rect.MakeXYWH(cx - r, cy - r, 2 * r, 2 * r)
    path = skia.Path()
    if abs(varre) >= 359.5:
        path.addCircle(cx, cy, r)
    else:
        path.moveTo(cx, cy); path.arcTo(ret, ini, varre, False); path.close()
    c.drawPath(path, M.paint(cor, alfa * a))
    if borda:
        c.drawArc(ret, ini, varre, False, M.paint(cor, a, stroke=borda, cap_round=True))


def mostrador(c, cx, cy, r, a=1.0, numeros=(12, 3, 6, 9), escuro=False, size=None):
    """mostrador de relógio: disco, 12 tracinhos (os de 12, 3, 6 e 9 mais fortes) e os números"""
    if a <= 0:
        return
    tinta = BR if escuro else TINTA
    s = skia.Paint(AntiAlias=True, Color=M.hexc("#000000", (0.0 if escuro else 0.16) * a))
    s.setMaskFilter(skia.MaskFilter.MakeBlur(skia.kNormal_BlurStyle, 14))
    c.drawCircle(cx + 6, cy + 12, r, s)
    c.drawCircle(cx, cy, r, M.paint("#15132E" if escuro else "#FFFFFF", a))
    c.drawCircle(cx, cy, r, M.paint(tinta, a, stroke=max(4, r * 0.025)))
    for h in range(12):
        forte = h % 3 == 0
        M.line(c, *hora(cx, cy, r * (0.84 if forte else 0.89), h), *hora(cx, cy, r * 0.95, h), tinta, a, max(3, r * (0.024 if forte else 0.012)))
    size = size or r * 0.17
    for n in numeros:
        x, y = hora(cx, cy, r * 0.68, n % 12)
        centro(c, str(n), x, y + size * 0.36, size, "g", tinta, a)


def ponteiros(c, cx, cy, r, hg, hp, a=1.0, pg=1.0, pp=1.0, escuro=False, kg=0.6, kp=0.42):
    """ponteiro grande na hora hg (12 = minuto zero) e pequeno na hora hp; pg e pp fazem cada um crescer"""
    if a <= 0:
        return
    tinta = BR if escuro else TINTA
    if pg > 0:
        M.line(c, cx, cy, *hora(cx, cy, r * kg, hg), tinta, a, max(5, r * 0.03), progress=pg)
    if pp > 0:
        M.line(c, cx, cy, *hora(cx, cy, r * kp, hp), tinta, a, max(7, r * 0.05), progress=pp)
    c.drawCircle(cx, cy, max(7, r * 0.045), M.paint(tinta, a))


def pulso(c, cx, cy, r, a=1.0):
    """relógio de pulso: mostrador pequeno com a pulseira"""
    if a <= 0:
        return
    for dy in (-1, 1):
        y0 = cy + dy * r * 0.7 - (r * 1.5 if dy < 0 else 0)
        M.rrect(c, cx - r * 0.62, y0, r * 1.24, r * 1.5, r * 0.25, "#C8C8CE", a)
    mostrador(c, cx, cy, r, a, numeros=())


def folha(c, x, y, w, h, a=1.0):
    """folha de papel com sombra; o canto de baixo à esquerda é (x, y + h)"""
    if a <= 0:
        return
    s = skia.Paint(AntiAlias=True, Color=M.hexc("#000000", 0.2 * a))
    s.setMaskFilter(skia.MaskFilter.MakeBlur(skia.kNormal_BlurStyle, 12))
    c.drawRect(skia.Rect.MakeXYWH(x + 8, y + 12, w, h), s)
    c.drawRect(skia.Rect.MakeXYWH(x, y, w, h), M.paint("#FFFFFF", a))
    for i in range(1, 8):
        yy = y + h * i / 8
        M.line(c, x + w * 0.12, yy, x + w * 0.9, yy, FIO, a, 2)
    c.drawRect(skia.Rect.MakeXYWH(x, y, w, h), M.paint(CINZA, a, stroke=2))


def angulo_relogio(c, t, t0, cx, cy, r, hg, hp, rotulo=None, ra=None, size=56, cor=None):
    """o ângulo entre os ponteiros, com arco (ou quadradinho no reto)"""
    E.angulo(c, t, t0, (cx, cy), hora(cx, cy, r * 0.8, hg), hora(cx, cy, r * 0.56, hp), rotulo, r=ra or r * 0.3, size=size, cor=cor)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    cx, cy, r = 600, 560, 300
    ka, kb, kc, kd = C["s01.a"], C["s01.b"], C["s01.c"], C["s01.d"]

    def um():
        E.foco(c, t, ka, 0.6, lambda a: mostrador(c, cx, cy, r, a))
        ponteiros(c, cx, cy, r, 12, 3, 1.0, ep(t, ka + 0.4, 0.5), ep(t, ka + 0.7, 0.5))
        E.saida(c, t, kd, lambda: (E.frase(c, t, ka + 0.3, [("3", "g", 120, COR), ("horas", "g", 110)], 1060, 260, "left", 0.15),
                                   E.frase(c, t, ka + 0.8, ps("em ponto", "i", 90), 1060, 360, "left", 0.15)))
        angulo_relogio(c, t, kb, cx, cy, r, 12, 3, ra=110)
        E.saida(c, t, kd, lambda: E.foco(c, t, kc, 0.6, lambda a: (folha(c, 1180, 430, 360, 440, a),
                                                                   E.angulo(c, t, kc + 0.4, (1180, 870), (1540, 870), (1180, 430), r=90))))
        E.saida(c, t, kd, lambda: E.foco(c, t, lerp(kc, kd, 0.45), 0.5, lambda a: E.pilula(c, "quanto mede?", cx, 970, 60, "g", a=a, cor=E.SOBRE)))
        E.foco(c, t, lerp(kc, kd, 0.45), 0.5, lambda a: centro(c, "?", cx + 150, cy - 110, 110, "g", COR, a))
        # parede x pulso
        E.foco(c, t, kd, 0.6, lambda a: (pulso(c, 1500, 560, 120, a), ponteiros(c, 1500, 560, 120, 12, 3, a)))
        E.foco(c, t, kd + 0.3, 0.5, lambda a: (centro(c, "parede", cx, 990, 64, "i", TINTA, a), centro(c, "pulso", 1500, 990, 64, "i", TINTA, a)))
        E.frase(c, t, kd + 1.4, [("maior?", "g", 84, COR)], 1110, 590, "center")
    E.saida(c, t, C["s02"] - 0.1, um)

    if t >= C["s02"]:
        ta, tb, tc = C["s02.a"], C["s02.b"], C["s02.c"]
        E.foco(c, t, tc - 0.2, 0.7, lambda a: E.bola(c, 1500, 560, 250 * ease_back(prog(t, tc - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, ps("até o fim desta aula", "i", 90), XE, 300, passo=0.14)
        E.frase(c, t, lerp(ta, tb, 0.35), [("medir", "g", 110, COR)] + ps("ângulos", "i", 100), XE, 460, passo=0.14)
        E.frase(c, t, lerp(ta, tb, 0.6), ps("em", "i", 100) + [("graus", "g", 110, COR)], XE, 590, passo=0.14)
        E.frase(c, t, tb, [("dar nome", "g", 96)] + ps("a cada tipo", "i", 90), XE, 760, passo=0.14)
        E.foco(c, t, tc + 0.1, 0.5, lambda a: (centro(c, "+ atalho", 1500, 535, 80, "g", E.SOBRE, a),
                                               centro(c, "de prova", 1500, 620, 80, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"] + 0.3, ps("você só precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "1", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisa", XE + 200, 700, 120, "i", TINTA, a))
    x, y, w = 960, 260, 840
    p = ep(t, C["s03.b"], 0.5)
    E.caixa_pontilhada(c, x, y, w, 196, p, prog_=p)
    E.frase(c, t, C["s03.b"] + 0.1, [("calcular a", "i", 60)], x + 44, y + 84)
    E.frase(c, t, C["s03.b"] + 0.3, [("fração de uma quantidade", "g", 54, COR)], x + 44, y + 160)
    E.cursor(c, x + w - 30, y + 170, ep(t, C["s03.b"], 0.4))
    t1 = lerp(C["s03.b"], C["s03.end"], 0.4)
    E.foco(c, t, t1, 0.5, lambda a: E.pilula(c, "divide pelo de baixo", x + w / 2, 600, 52, a=a, cor=E.SOBRE))
    E.foco(c, t, t1 + 1.0, 0.5, lambda a: E.pilula(c, "multiplica pelo de cima", x + w / 2, 720, 52, fundo=TINTA, a=a))
    E.frase(c, t, C["s03.end"] - 2.4, ps("faltou?", "i", 58, COR) + ps("procure no canal", "i", 58), x, 920, "left", 0.12)


# ---------------- o que é ângulo ----------------
def b_ideia(c, t, C, b):
    E.frase(c, t, C["s04"], ps("o que é um", "i", 90) + [("ângulo?", "g", 90, COR)], W / 2, 180, "center", 0.14)
    V, L, ab = (760, 820), 680, 40
    a4, a5, b5, c5 = C["s04.a"], C["s05.a"], C["s05.b"], C["s05.c"]
    # o lado de cima gira na fala de "o quanto um lado girou"
    gira = ab * (1 - ease_io(prog(t, c5 + 0.4, 0.6))) + ab * ease_io(prog(t, c5 + 1.0, 1.4)) if t >= c5 + 0.4 else ab
    A = (V[0] + L, V[1])
    B = (V[0] + L * math.cos(math.radians(gira)), V[1] - L * math.sin(math.radians(gira)))
    if t >= a4:
        p1, p2 = ease_io(prog(t, a4, 0.7)), ease_io(prog(t, a4 + 0.3, 0.7))
        grosso = 6 + 5 * (ep(t, b5, 0.3) - ep(t, b5 + 1.8, 0.4))
        M.line(c, *V, *A, TINTA, 1.0, grosso, progress=p1)
        M.line(c, *V, *B, TINTA, 1.0, grosso, progress=p2)
        c.drawCircle(*V, 12 * ease_back(prog(t, a4, 0.4)), M.paint(TINTA))
    # como os ponteiros: um relógio pequeno ao lado
    tr = lerp(a4, C["s04.end"], 0.45)
    E.saida(c, t, C["s05"], lambda: E.foco(c, t, tr, 0.6, lambda a: (mostrador(c, 330, 560, 170, a), ponteiros(c, 330, 560, 170, 12, 2, a))))
    # vértice
    if t >= a5:
        k = ep(t, a5, 0.4)
        pulsa = 1 + 0.5 * math.sin(min(1, prog(t, a5, 0.9)) * math.pi)
        c.drawCircle(*V, 16 * pulsa * k, M.paint(COR))
        E.foco(c, t, a5 + 0.2, 0.5, lambda a: E.escreve(c, "vértice", V[0] - 330, V[1] + 100, 76, "g", COR, a))
        M.arrow(c, V[0] - 110, V[1] + 70, V[0] - 30, V[1] + 20, COR, k, 5, 16, k)
    # lados
    E.foco(c, t, b5 + 0.1, 0.5, lambda a: E.escreve(c, "lado", A[0] - 200, A[1] + 90, 70, "i", TINTA, a))
    E.foco(c, t, b5 + 0.4, 0.5, lambda a: E.escreve(c, "lado", V[0] + 130, V[1] - 330, 70, "i", TINTA, a))
    # ângulo = abertura
    E.angulo(c, t, c5, V, A, B, r=190, preenche=0.22)
    E.frase(c, t, c5 + 0.3, [("ângulo", "g", 76, COR)] + ps("= abertura", "i", 76), 1080, 700, "left", 0.15)


# ---------------- graus ----------------
def b_graus(c, t, C, b):
    cx, cy, r = 560, 580, 290
    X = 1400
    a6, b6, c6 = C["s06.a"], C["s06.b"], C["s06.c"]
    a7, b7, c7 = C["s07.a"], C["s07.b"], C["s07.c"]
    a8, b8, c8 = C["s08.a"], C["s08.b"], C["s08.c"]
    ret = skia.Rect.MakeXYWH(cx - r, cy - r, 2 * r, 2 * r)
    # uma volta: o raio gira desde o 12, como o ponteiro
    q = ease_io(prog(t, b6, 2.2))
    if q > 0:
        some = ep(t, a7, 0.5)
        cunha(c, cx, cy, r, -90, 360 * q, a=1 - some, alfa=0.16, borda=0)
        c.drawArc(ret, -90, 360 * q, False, M.paint(TINTA, 1.0, stroke=6, cap_round=True))
        ang = math.radians(-90 + 360 * q)
        if t < a7:
            M.line(c, cx, cy, cx + r * math.cos(ang), cy + r * math.sin(ang), TINTA, 1.0, 7)
        c.drawCircle(cx, cy, 11, M.paint(TINTA))
    # meia volta e um quarto
    meia = ep(t, b7, 0.8) * (1 - ep(t, a8, 0.5))
    if meia > 0:
        cunha(c, cx, cy, r, -90, 180 * ease_io(prog(t, b7, 0.8)), a=meia, alfa=0.22, borda=7)
        M.line(c, cx, cy - r, cx, cy + r, TINTA, meia, 6)
    if t >= a8:
        cunha(c, cx, cy, r, -90, 90 * ease_io(prog(t, a8 + 0.3, 0.8)), a=1, alfa=0.22, borda=7)
        M.line(c, cx, cy, cx, cy - r, TINTA, 1, 6)
        M.line(c, cx, cy, cx + r, cy, TINTA, 1, 6)
        E.foco(c, t, c8, 0.6, lambda a: folha(c, cx + 4, cy - 214, 166, 210, a))
        E.angulo(c, t, b8 - 0.2, (cx, cy), (cx + r, cy), (cx, cy - r), r=80)

    def volta():
        E.frase(c, t, a6, ps("o", "i", 110) + [("grau", "g", 120, COR)], X, 300, "center")
        E.frase(c, t, b6 + 0.8, ps("uma volta inteira", "i", 80), X, 480, "center", 0.12)
        x0 = X - (E.larg("360", "g", 170) + E.larg("°", "g", 170)) / 2
        E.foco(c, t, b6 + 2.0, 0.5, lambda a: (E.escreve(c, "360", x0, 700, 170, "g", TINTA, a),
                                               E.escreve(c, "°", x0 + E.larg("360", "g", 170) + 4, 700, 170, "g", COR, a)))
        xg = x0 + E.larg("360", "g", 170) - 6
        p = ep(t, c6, 0.5)
        E.caixa_pontilhada(c, xg, 548, 84, 84, p, COR, prog_=p)
        E.cursor(c, xg + 70, 620, ep(t, c6, 0.4))
    E.saida(c, t, a7 - 0.1, volta)

    def metade():
        E.frase(c, t, a7, ps("fração de", "i", 80) + [("360°", "g", 84, COR)], X, 300, "center", 0.12)
        E.frase(c, t, b7, ps("meia volta", "i", 84), X, 470, "center", 0.12)
        fcen(c, t, lerp(b7, c7, 0.45), "360 ÷ 2 = 180", X, 620, 90)
        bola_txt(c, t, c7, "180°", X, 820, 125, 76)
    if t >= a7 - 0.1:
        E.saida(c, t, a8 - 0.1, metade)

    if t >= a8 - 0.1:
        fcen(c, t, a8, "f{1}{4} de volta", X, 320, 90)
        fcen(c, t, lerp(a8, b8, 0.4), "360 ÷ 4 = 90", X, 500, 84, TINTA2)
        fcen(c, t, lerp(a8, b8, 0.8), "90 × 1 = 90", X, 620, 84, TINTA2)
        bola_txt(c, t, b8, "90°", X, 800, 115, 80)
        E.frase(c, t, c8 + 0.4, ps("o canto da folha", "i", 64), X, 990, "center", 0.12)


# ---------------- o relógio ----------------
def b_relogio(c, t, C, b):
    cx, cy, r = 600, 560, 360
    X = 1400
    a9, a10, b10, c10, d10, a11, b11 = C["s09.a"], C["s10.a"], C["s10.b"], C["s10.c"], C["s10.d"], C["s11.a"], C["s11.b"]
    E.foco(c, t, C["s09"], 0.5, lambda a: mostrador(c, cx, cy, r, a))
    # 12, 3, 6, 9 cortam em quatro
    q = ep(t, a9, 0.7)
    if q > 0 and t < a10:
        for h0 in (12, 3):
            M.line(c, *hora(cx, cy, r * 0.5, h0), *hora(cx, cy, r * 0.5, h0 + 6), COR, q, 5, dash=E.TRACO, progress=q)
        for i, h0 in enumerate((0, 3, 6, 9)):
            cunha(c, cx, cy, r * 0.5, tela(h0), 90, a=q * (1 if i % 2 == 0 else 0.55), alfa=0.18, borda=0)
    E.saida(c, t, a10, lambda: E.frase(c, t, a9, [("4", "g", 120, COR)] + ps("partes iguais", "i", 90), X, 560, "center", 0.14))
    # 3 horas
    ponteiros(c, cx, cy, r, 12, 3, 1.0, ep(t, a10, 0.6), ep(t, b10, 0.6))
    if t >= c10:
        cunha(c, cx, cy, r * 0.62, tela(12), 90 * ease_io(prog(t, c10, 0.8)), alfa=0.24, borda=0)
    if t >= a11:
        cunha(c, cx, cy, r * 0.62, tela(3), 270 * ease_io(prog(t, a11, 1.0)), TINTA2, alfa=0.1, borda=0)
        E.arco(c, cx, cy, r * 0.3, tela(3), 270 * ease_io(prog(t, a11, 1.0)), TINTA2, 5)
    angulo_relogio(c, t, d10 - 0.3, cx, cy, r, 12, 3, ra=110)

    def tres():
        E.frase(c, t, a10, ps("grande no", "i", 76) + [("12", "g", 84, COR)], X, 300, "center", 0.12)
        E.frase(c, t, b10, ps("pequeno no", "i", 76) + [("3", "g", 84, COR)], X, 420, "center", 0.12)
        fcen(c, t, c10, "f{1}{4} de volta", X, 610, 96)
        bola_txt(c, t, d10, "90°", X, 830, 120, 84)
    if t >= a10:
        E.saida(c, t, C["s11"] - 0.1, tres)
    if t >= C["s11"]:
        E.frase(c, t, a11, ps("o outro lado:", "i", 76, TINTA2), X, 380, "center", 0.12)
        E.frase(c, t, a11 + 0.6, [("a parte maior", "g", 84, TINTA2)], X, 490, "center")
        E.frase(c, t, b11, ps("entre os ponteiros", "i", 76), X, 700, "center", 0.12)
        E.frase(c, t, b11 + 0.6, ps("vale o", "i", 96) + [("menor", "g", 104, COR)], X, 830, "center", 0.12)


# ---------------- os tipos ----------------
def b_tipos(c, t, C, b):
    y0, L = 520, 280
    E.frase(c, t, C["s12"], [("90°", "g", 84, COR)] + ps("é a régua", "i", 84), W / 2, 150, "center", 0.14)

    def raio(V, g):
        return V[0] + L * math.cos(math.radians(g)), V[1] - L * math.sin(math.radians(g))
    tipos = (  # coluna, vértice, abertura, nome, medida, instante, relógio (hora do pequeno, instante)
        (300, (160, y0), 45, "agudo", "menor que 90°", C["s13.a"], (1, C["s13.b"])),
        (740, (610, y0), 90, "reto", "igual a 90°", C["s12.a"], None),
        (1210, (1210, y0), 130, "obtuso", "entre 90° e 180°", C["s14.a"], (4, C["s14.b"])),
        (1680, (1680, y0), 180, "raso", "igual a 180°", C["s15.a"], (6, C["s15.c"])),
    )
    for cx, V, g, nome, med, t0, rel in tipos:
        A = (V[0] + L if g < 180 else V[0] + 150, V[1])
        B = raio(V, g) if g < 180 else (V[0] - 150, V[1])
        if t >= t0:
            M.line(c, *V, *A, TINTA, 1.0, 6, progress=ease_io(prog(t, t0, 0.5)))
            M.line(c, *V, *B, TINTA, 1.0, 6, progress=ease_io(prog(t, t0 + 0.2, 0.5)))
            c.drawCircle(*V, 9, M.paint(TINTA))
        if g == 90:  # o reto chega com arco e troca pelo quadradinho na fala
            E.saida(c, t, C["s12.b"], lambda V=V, A=A, B=B: E.angulo(c, t, t0 + 0.6, V, A, B, r=90, reto=False))
            E.foco(c, t, C["s12.b"], 0.5, lambda a, V=V, A=A, B=B: E.angulo(c, t, C["s12.b"], V, A, B, r=90, reto=True))
        else:
            E.angulo(c, t, t0 + 0.6, V, A, B, r=80)
        E.frase(c, t, t0 + 0.4, [(nome, "g", 80, COR)], cx, 650, "center")
        E.frase(c, t, t0 + 0.9, [(med, "b", 40, TINTA2)], cx, 715, "center")
        if rel:
            hp, tr = rel
            E.foco(c, t, tr, 0.6, lambda a, hp=hp, cx=cx: (mostrador(c, cx - 50, 890, 105, a, numeros=()),
                                                          ponteiros(c, cx - 50, 890, 105, 12, hp, a),
                                                          E.escreve(c, f"{hp} h", cx + 75, 910, 52, "b", TINTA, a)))
    E.foco(c, t, C["s15.b"], 0.5, lambda a: E.pilula(c, "linha reta", 1680, 350, 44, a=a, cor=E.SOBRE))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    cx, cy, r = 560, 640, 300
    px, py, pr = 1420, 640, 110
    a16, b16, c16, a17, b17, c17 = C["s16.a"], C["s16.b"], C["s16.c"], C["s17.a"], C["s17.b"], C["s17.c"]
    E.frase(c, t, C["s16"], [("cuidado", "g", 96, ERRADO)] + ps("com este erro", "i", 90), W / 2, 140, "center", 0.14)
    E.saida(c, t, b17, lambda: E.frase(c, t, a16, ps("lado maior,", "i", 70) + [("ângulo maior?", "g", 66, ERRADO)], W / 2, 250, "center", 0.12))
    E.frase(c, t, b17, ps("mede a", "i", 70) + [("abertura,", "g", 66, COR)] + ps("não o comprimento", "i", 70), W / 2, 250, "center", 0.12)
    E.foco(c, t, b16, 0.6, lambda a: (mostrador(c, cx, cy, r, a), ponteiros(c, cx, cy, r, 12, 3, a)))
    E.foco(c, t, b16 + 0.3, 0.5, lambda a: centro(c, "parede", cx, 1020, 60, "i", TINTA, a))
    # o de pulso: na fala de "esticar os lados", os ponteiros crescem e o ângulo continua 90°
    est = ease_io(prog(t, c17, 1.2))
    E.foco(c, t, c16, 0.6, lambda a: pulso(c, px, py, pr, a))
    E.foco(c, t, c16, 0.6, lambda a: ponteiros(c, px, py, pr, 12, 3, a, kg=lerp(0.6, 2.9, est), kp=lerp(0.42, 2.9, est)))
    E.foco(c, t, c16 + 0.3, 0.5, lambda a: centro(c, "pulso", px, 1020, 60, "i", TINTA, a))
    angulo_relogio(c, t, a17, cx, cy, r, 12, 3, "90°", ra=100, size=60)
    E.angulo(c, t, a17 + 0.4, (px, py), (px, py - 50), (px + 50, py), "90°", r=60, size=60, afasta=40)
    E.frase(c, t, c17 + 1.0, ps("não muda", "i", 66) + [("nada", "g", 64, COR)], 1560, 900, "center", 0.12)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    cx, cy, r = 600, 560, 340
    X = 1390
    a18, b18 = C["s18.a"], C["s18.b"]
    a19, b19, c19, d19 = C["s19.a"], C["s19.b"], C["s19.c"], C["s19.d"]
    a20, b20, c20 = C["s20.a"], C["s20.b"], C["s20.c"]
    E.foco(c, t, C["s18"], 0.5, lambda a: mostrador(c, cx, cy, r, a, numeros=range(1, 13), escuro=True, size=50))
    # 1 hora = 30°
    if C["s18"] <= t < C["s19"] + 0.4:
        a_ = 1 - ep(t, C["s19"], 0.4)
        cunha(c, cx, cy, r * 0.84, tela(0), 30 * ease_io(prog(t, a18, 0.6)), CLARO, a_, alfa=0.45, borda=0)
        for i in (1, 2):
            if t >= b18:
                cunha(c, cx, cy, r * 0.84, tela(i), 30 * ease_io(prog(t, b18 + 0.3 * i, 0.5)), CLARO, a_, alfa=0.45 if i == 2 else 0.25, borda=0)
        for i in range(3):
            ti = a18 + 0.5 if i == 0 else b18 + 0.3 * i + 0.4
            E.foco(c, t, ti, 0.4, lambda a, i=i: centro(c, "30°", *(lambda p: (p[0], p[1] + 16))(hora(cx, cy, r * 0.52, i + 0.5)), 44, "b", BR, a * a_))

    def hora_cheia():
        E.frase(c, t, a18, [("1 hora", "g", 110, BR)], X, 330, "center")
        E.frase(c, t, a18 + 0.6, [("= 30°", "g", 130, CLARO)], X, 480, "center")
        fcen(c, t, b18 + 0.8, "90 ÷ 3 = 30", X, 720, 96, BR)
    E.saida(c, t, C["s19"] - 0.1, hora_cheia)

    # a regra e os exemplos: o ponteiro pequeno anda de 2 para 4 e para 10
    if C["s19"] <= t < C["s20"] + 0.5:
        def hp_(tt):
            h = 2 + 2 * ease_io(prog(tt, c19, 0.7))
            return h + 6 * ease_io(prog(tt, d19, 1.0))
        hp = hp_(t)
        al = 1 - ep(t, C["s20"], 0.5)
        if t >= b19:
            if hp <= 6:
                cunha(c, cx, cy, r * 0.6, tela(0), hp * 30, CLARO, al * ep(t, b19, 0.5), alfa=0.4, borda=6)
            else:
                cunha(c, cx, cy, r * 0.6, tela(hp), (12 - hp) * 30, CLARO, al, alfa=0.4, borda=6)
        ponteiros(c, cx, cy, r, 12, hp, ep(t, b19 - 0.3, 0.4) * al, escuro=True)

        def regra():
            E.frase(c, t, a19, ps("conte as horas", "i", 70, CLARO), X, 250, "center", 0.12)
            E.frase(c, t, a19 + 0.8, ps("pelo lado curto", "i", 70, CLARO), X, 340, "center", 0.12)
            E.frase(c, t, a19 + 1.6, [("× 30", "g", 110, BR)], X, 470, "center")
            E.frase(c, t, b19, [("às 2:", "i", 66, CLARO), ("2 × 30 = 60°", "g", 70, BR)], X, 640, "center", 0.2)
            E.frase(c, t, c19, [("às 4:", "i", 66, CLARO), ("4 × 30 = 120°", "g", 70, BR)], X, 770, "center", 0.2)
            E.frase(c, t, d19, [("às 10:", "i", 66, CLARO), ("2 × 30 = 60°", "g", 70, BR)], X, 900, "center", 0.2)
        E.saida(c, t, C["s20"] - 0.1, regra)

    if t >= C["s20"]:
        # 12 partes iguais
        q = ep(t, a20, 0.8)
        for h in range(6):
            M.line(c, *hora(cx, cy, r * 0.84, h), *hora(cx, cy, r * 0.84, h + 6), CLARO, q * (1 - 0.6 * ep(t, c20, 0.5)), 3, dash=E.TRACO, progress=q)
        E.frase(c, t, a20, [("12", "g", 110, CLARO)] + ps("partes iguais", "i", 84, BR), X, 300, "center", 0.14)
        E.foco(c, t, b20, 0.5, lambda a: E.pilula(c, "só em hora cheia", X, 470, 60, "g", a=a, cor=E.SOBRE))
        # 3 e meia: o pequeno sai do 3
        if t >= c20 - 0.6:
            k = ease_io(prog(t, c20 - 0.6, 1.0))
            fantasma = ep(t, c20 + 0.4, 0.4)
            if fantasma > 0:
                M.line(c, cx, cy, *hora(cx, cy, r * 0.56, 3), CLARO, fantasma * 0.8, 6, dash=E.TRACO)
            ponteiros(c, cx, cy, r, 6 * k, 3 + 0.5 * k, ep(t, c20 - 0.6, 0.4), escuro=True)
            E.frase(c, t, c20 - 0.4, [("3h30", "g", 96, BR)], X, 680, "center")
            E.frase(c, t, c20 + 0.5, ps("a conta", "i", 84, BR) + [("muda", "g", 90, ERRADO)], X, 830, "center", 0.14)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s21"], ps("hora de testar", "i", 72, COR), XE, 200, passo=0.12)
    E.frase(c, t, C["s21.a"], ps("às", "i", 96) + [("5 horas", "g", 100, COR)], XE, 400, passo=0.14)
    E.frase(c, t, C["s21.a"] + 0.9, ps("em ponto", "i", 96), XE, 520, passo=0.14)
    E.frase(c, t, lerp(C["s21.a"], C["s21.b"], 0.5), ps("o menor ângulo?", "i", 96), XE, 680, passo=0.14)
    E.frase(c, t, C["s21.b"], ps("e o", "i", 96) + [("nome?", "g", 100, COR)], XE, 830, passo=0.14)
    E.saida(c, t, C["s22.a"] - 0.1, lambda: E.foco(c, t, C["s21.a"], 0.6, lambda a: (mostrador(c, 1420, 560, 300, a), ponteiros(c, 1420, 560, 300, 12, 5, a))))
    E.relogio(c, t, C["s22.a"])


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    cx, cy, r = 600, 560, 340
    X = 1400
    a23, b23, c23, a24, b24, c24 = C["s23.a"], C["s23.b"], C["s23.c"], C["s24.a"], C["s24.b"], C["s24.c"]
    mostrador(c, cx, cy, r, ep(t, C["s23"], 0.4))
    # as cinco horas acendem uma a uma, do 12 até o 5
    for i in range(5):
        ti = a23 + 0.25 * i
        if t >= ti:
            cunha(c, cx, cy, r * 0.62, tela(i), 30 * ease_io(prog(t, ti, 0.3)), alfa=0.32 if i % 2 == 0 else 0.2, borda=0)
            E.foco(c, t, ti, 0.3, lambda a, i=i: centro(c, str(i + 1), *(lambda p: (p[0], p[1] + 16))(hora(cx, cy, r * 0.45, i + 0.5)), 44, "b", COR, a))
    # conferência: a meia volta até o 6 e a hora que falta
    if t >= a24:
        M.line(c, cx, cy, *hora(cx, cy, r * 0.56, 6), TINTA2, ep(t, a24, 0.4), 7, dash=E.TRACO)
        E.arco(c, cx, cy, r * 0.8, tela(0), 180 * ease_io(prog(t, a24, 0.8)), TINTA2, 6)
    if t >= b24:
        cunha(c, cx, cy, r * 0.62, tela(5), 30 * ease_io(prog(t, b24, 0.4)), TINTA2, alfa=0.35, borda=6)
    ponteiros(c, cx, cy, r, 12, 5, ep(t, C["s23"], 0.4))

    def conta():
        E.frase(c, t, a23, [("5", "g", 110, COR)] + ps("horas", "i", 100), X, 300, "center")
        fcen(c, t, b23, "5 × 30 = 150°", X, 480, 100)
        bola_txt(c, t, c23, "obtuso", X, 730, 150, 64, CERTO)
    E.saida(c, t, C["s24"] - 0.1, conta)
    if t >= C["s24"]:
        fcen(c, t, a24, "6 h = 180°", X, 300, 96, TINTA2)
        E.frase(c, t, b24, ps("falta", "i", 84) + [("1 h = 30°", "g", 84, TINTA2)], X, 450, "center", 0.12)
        fcen(c, t, c24 - 0.2, "180 − 30 = 150°", X, 620, 100)
        E.foco(c, t, c24 + 0.8, 0.5, lambda a: E.selo(c, X, 820, 100 * ease_back(prog(t, c24 + 0.8, 0.5)), True, a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s25"], [("resumindo", "i", 92, COR)], W / 2, 210, "center")
        itens = (("s25.a", "1 volta = 360°"), ("s25.b", "canto da folha = 90°"), ("s25.c", "90° separa agudo e obtuso"))
        for i, (k, s) in enumerate(itens):
            y = 390 + i * 190
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 400, y - 30, 56, a=a),
                                                         centro(c, str(i + 1), 400, y - 7, 64, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, [(s, "g", 84)], 500, y)
    E.saida(c, t, C["s26"] - 0.1, resumo)
    if t < C["s26"]:
        return
    E.frase(c, t, C["s26.a"] - 1.0, ps("próxima aula", "i", 84), XE, 300)
    E.frase(c, t, C["s26.a"], [("Pares de", "g", 140, COR)], XE, 450)
    E.frase(c, t, C["s26.a"] + 0.3, [("ângulos", "g", 140, COR)], XE, 590)
    E.frase(c, t, C["s26.b"], ps("e retas que se cruzam", "i", 76), XE, 720, passo=0.12)
    E.foco(c, t, C["s26.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1450, 400, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s26.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1780, 1580, p), lerp(720, 425, p), ep(t, C["s26.c"] + 0.2, 0.4))
    E.frase(c, t, C["s26.d"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 920, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, ideia=b_ideia, graus=b_graus, relogio=b_relogio, tipos=b_tipos,
              erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
