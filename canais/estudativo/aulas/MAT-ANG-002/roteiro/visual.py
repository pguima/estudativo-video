"""Visual — Estudativo · MAT-ANG-002: ângulos complementares, suplementares e opostos pelo vértice.
Segue a linguagem da geometria plana definida na MAT-ANG-001 (lados em tinta, ângulo da vez na cor da matéria, ângulos iguais
com a mesma cor: 1ª família COR, 2ª família TINTA2; medidas na grotesca; resposta na esfera).
Peças locais: pt() dá o ponto na direção g (graus da matemática, anti-horário a partir da direita); ang() desenha o ângulo de g1 a g2
com rótulo próprio, que pode mudar de texto; voa() é a cunha que sai do lugar, gira/viaja e assenta no destino, deixando o contorno
tracejado na origem — é como um ângulo "se move" para provar uma igualdade. Todo instante vem de C[...]."""
import math
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Ângulos e Triângulos")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-ANG-002_complementares_suplementares_opostos.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("complemento", "opostos", "equacao", "atalho", "questao", "fim"))
BR = "#FFFFFF"
assert 90 - 35 == 55 and 180 - 110 == 70 and 180 - 50 == 130 and 180 - 130 == 50
assert 3 * 20 - 10 == 20 + 30 == 50 and 55 + 90 == 145 == 180 - 35
assert 3 * 40 + 60 == 180 and 40 + 40 == 80 and 2 * 40 + 20 == 100 and 80 + 100 == 180
assert 20 + 40 == 2 * 20 + 20 == 60  # quem iguala: x = 20, 60° e 60°, que não fecham 180°


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças desta aula ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def fcen(c, t, t0, s, cx, y, size, cor=None):
    E.formula_em(c, t, t0, s, cx, y, size, "g", cor, "center")


def bola_txt(c, t, t0, s, cx, cy, r, size, cor=None):
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r * ease_back(prog(t, t0, 0.5)), cor, a),
                                     centro(c, s, cx, cy + size * 0.36, size, "g", BR, a)))


def operacao(c, t, t0, op, x, y, escuro=False):
    """pílula da conta feita nos dois lados"""
    E.foco(c, t, t0, 0.5, lambda a: E.pilula(c, op, x, y - 30, 54, "g", a=a, cor=E.SOBRE))
    E.frase(c, t, t0 + 0.3, ps("nos dois lados", "i", 40, CLARO if escuro else TINTA2), x, y + 48, "center", 0.06)


def pt(V, L, g):
    """ponto a L de V na direção g (graus da matemática)"""
    return V[0] + L * math.cos(math.radians(g)), V[1] - L * math.sin(math.radians(g))


def raio(c, t, t0, V, L, g, cor=TINTA, d=0.6, largura=6, tracejado=False):
    if t >= t0:
        M.line(c, *V, *pt(V, L, g), cor, 1.0, largura, dash=E.TRACO if tracejado else None, progress=ease_io(prog(t, t0, d)))


def rotulo(c, V, g, r, s, cor, size, a, dentro=False):
    """medida na bissetriz g, afastada do arco o bastante para não tocar nele"""
    if a <= 0 or not s:
        return
    w = E.formula(None, s, 0, 0, size, "b", a=0)
    ux, uy = math.cos(math.radians(g)), -math.sin(math.radians(g))
    k = r * 0.55 if dentro else r + 16 + abs(ux) * w / 2 + abs(uy) * size * 0.4
    E.formula(c, s, V[0] + ux * k, V[1] + uy * k + size * 0.36, size, "b", cor, a, "center")


def ang(c, t, t0, V, g1, g2, rot=None, r=90, cor=None, size=52, tr=None, reto=None):
    """ângulo de g1 a g2 (anti-horário). rot = texto (ou função t → texto); entra em tr"""
    E.angulo(c, t, t0, V, pt(V, 10, g1), pt(V, 10, g2), None, r=r, cor=cor, reto=reto)
    if rot:
        s = rot(t) if callable(rot) else rot
        cr = cor or COR
        rr = r * 1.1 if (reto or abs(g2 - g1 - 90) < 0.6) else r
        E.foco(c, t, tr if tr is not None else t0 + 0.3, 0.4, lambda a: rotulo(c, V, (g1 + g2) / 2, rr, s, cr, size, a))


def cunha_m(c, V, g1, g2, r, cor, a=1.0, alfa=0.3, borda=6):
    """cunha de g1 a g2 (graus da matemática) em V"""
    if a <= 0:
        return
    ret = skia.Rect.MakeXYWH(V[0] - r, V[1] - r, 2 * r, 2 * r)
    path = skia.Path()
    path.moveTo(*V); path.arcTo(ret, -g1, -(g2 - g1), False); path.close()
    c.drawPath(path, M.paint(cor, alfa * a))
    if borda:
        p = M.paint(cor, a, stroke=borda, cap_round=True)
        p.setStrokeJoin(skia.Paint.kRound_Join)
        c.drawPath(path, p)


def voa(c, t, t0, d, V0, g1, g2, r, cor=None, V1=None, giro=0.0, fica=0.8):
    """o ângulo se move: a cunha sai de V0, gira `giro` graus e viaja até V1 em d segundos; fica `fica` s no destino e some.
    Na origem fica o contorno tracejado enquanto ela viaja"""
    if t < t0 or t > t0 + d + fica + 0.4:
        return
    cor = cor or E.COR
    V1 = V1 or V0
    p = ease_io(prog(t, t0, d))
    a = 1 - ep(t, t0 + d + fica, 0.4)
    ret = skia.Rect.MakeXYWH(V0[0] - r, V0[1] - r, 2 * r, 2 * r)
    tr = M.paint(cor, 0.8 * a, stroke=3)
    tr.setPathEffect(skia.DashPathEffect.Make([10, 8], 0))
    path = skia.Path(); path.moveTo(*V0); path.arcTo(ret, -g1, -(g2 - g1), False); path.close()
    c.drawPath(path, tr)
    lift = 1 + 0.08 * math.sin(math.pi * p)
    c.save()
    c.translate(lerp(V0[0], V1[0], p), lerp(V0[1], V1[1], p))
    c.rotate(-giro * p)
    c.scale(lift, lift)
    s = skia.Paint(AntiAlias=True, Color=M.hexc("#000000", 0.25 * a * math.sin(math.pi * p)))
    s.setMaskFilter(skia.MaskFilter.MakeBlur(skia.kNormal_BlurStyle, 10))
    path2 = skia.Path(); path2.moveTo(0, 0); path2.arcTo(skia.Rect.MakeXYWH(-r, -r, 2 * r, 2 * r), -g1, -(g2 - g1), False); path2.close()
    c.save(); c.translate(6, 12); c.drawPath(path2, s); c.restore()
    cunha_m(c, (0, 0), g1, g2, r, cor, a, alfa=0.55)
    c.restore()


def cruz(c, t, t0, V, L, th, cor=TINTA, d=0.7):
    """duas retas que se cruzam em V: uma deitada, outra na direção th"""
    if t >= t0:
        for i, g in enumerate((0, th)):
            q = ease_io(prog(t, t0 + 0.25 * i, d))
            M.line(c, *pt(V, L * q, g + 180), *pt(V, L * q, g), cor, 1.0, 6)
        c.drawCircle(*V, 11 * ease_back(prog(t, t0 + 0.3, 0.4)), M.paint(cor))


def folha(c, x, y, w, h, a=1.0):
    if a <= 0:
        return
    s = skia.Paint(AntiAlias=True, Color=M.hexc("#000000", 0.18 * a))
    s.setMaskFilter(skia.MaskFilter.MakeBlur(skia.kNormal_BlurStyle, 12))
    c.drawRect(skia.Rect.MakeXYWH(x + 8, y + 12, w, h), s)
    c.drawRect(skia.Rect.MakeXYWH(x, y, w, h), M.paint("#FFFFFF", a))
    for i in range(1, 9):
        M.line(c, x + w * 0.1, y + h * i / 9, x + w * 0.92, y + h * i / 9, FIO, a, 2)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    ka, kb, kc = C["s01.a"], C["s01.b"], C["s01.c"]

    def um():
        E.frase(c, t, ka, ps("complemento de", "i", 96) + [("35°?", "g", 110, COR)], W / 2, 280, "center", 0.15)
        E.foco(c, t, kb, 0.5, lambda a: centro(c, "145°", W / 2, 560, 220, "g", ERRADO, a))
        if t >= kb + 0.8:
            E.risco(c, W / 2 - 260, 590, W / 2 + 260, 390, t, kb + 0.8, largura=16)
        # as duas palavras trocam de lugar
        q = ease_io(prog(t, kc + 0.8, 0.9))
        x1, x2, y = lerp(640, 1280, q), lerp(1280, 640, q), 860 + 0 * q
        sobe = 60 * math.sin(math.pi * q)
        E.foco(c, t, kc, 0.5, lambda a: E.pilula(c, "complemento", x1, y - sobe, 64, "g", a=a, cor=E.SOBRE))
        E.foco(c, t, kc + 0.3, 0.5, lambda a: E.pilula(c, "suplemento", x2, y + sobe, 64, "g", fundo=TINTA, a=a))
    E.saida(c, t, C["s02"] - 0.1, um)

    if t >= C["s02"]:
        ta, tb, tc = C["s02.a"], C["s02.b"], C["s02.c"]
        E.foco(c, t, tc - 0.2, 0.7, lambda a: E.bola(c, 1500, 560, 250 * ease_back(prog(t, tc - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, ps("até o fim desta aula", "i", 90), XE, 300, passo=0.14)
        E.frase(c, t, lerp(ta, tb, 0.4), [("não confundir", "g", 96, COR)], XE, 450, passo=0.14)
        E.frase(c, t, lerp(ta, tb, 0.6), ps("complemento e suplemento", "i", 76), XE, 560, passo=0.12)
        E.frase(c, t, tb, [("achar", "g", 96)] + ps("ângulos escondidos", "i", 80), XE, 740, passo=0.14)
        E.foco(c, t, tc + 0.1, 0.5, lambda a: (centro(c, "+ atalho", 1500, 535, 80, "g", E.SOBRE, a),
                                               centro(c, "de prova", 1500, 620, 80, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"] + 0.3, ps("você só precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "2", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 960, 820
    itens = (("s03.b", "reto = 90°", "raso = 180°"), ("s03.c", "equação com x", "dos dois lados"))
    for i, (k, l1, l2) in enumerate(itens):
        y = 250 + i * 280
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 196, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "g" if i == 0 else "i", 60, TINTA if i else TINTA)], x + 44, y + 84)
        E.frase(c, t, C[k] + 0.3, [(l2, "g", 60, COR)], x + 44, y + 160)
    py = lerp(420, 700, ease_io(prog(t, C["s03.c"] - 0.35, 0.5)))
    E.cursor(c, x + w - 30, py, ep(t, C["s03.b"], 0.4))
    E.frase(c, t, C["s03.end"] - 2.4, ps("faltou alguma?", "i", 58, COR) + ps("procure no canal", "i", 58), x, 920, "left", 0.12)


# ---------------- complementares ----------------
def b_complemento(c, t, C, b):
    V, L, g = (330, 900), 600, 35
    X = 1400
    a4, b4, c4 = C["s04.a"], C["s04.b"], C["s04.c"]
    a5, b5, a6, b6, c6 = C["s05.a"], C["s05.b"], C["s06.a"], C["s06.b"], C["s06.c"]
    E.foco(c, t, C["s04"], 0.6, lambda a: folha(c, V[0], V[1] - L, L, L, a))
    raio(c, t, a4, V, L, 0, largura=8)
    raio(c, t, a4, V, L, 90, largura=8)
    E.angulo(c, t, a4, V, pt(V, 10, 0), pt(V, 10, 90), r=90) if t < c4 else None
    raio(c, t, b4, V, L * 0.95, g)
    if t >= c4:
        ang(c, t, c4, V, 0, g, "35°", r=200, tr=a6 - 0.3)
        ang(c, t, c4 + 0.3, V, g, 90, "55°", r=140, cor=TINTA2, tr=b6)
    E.frase(c, t, c4 + 0.6, ps("juntos:", "i", 70), V[0] + 20, 200, "left") if t < C["s06"] else None
    E.foco(c, t, c4 + 1.0, 0.5, lambda a: E.escreve(c, "90°", V[0] + 250, 200, 80, "g", COR, a)) if t < C["s06"] else None

    def defin():
        E.frase(c, t, a5, ps("somam 90°", "g", 76), X, 360, "center")
        E.frase(c, t, a5 + 0.4, [("complementares", "g", 96, COR)], X, 500, "center")
        E.frase(c, t, b5, ps("o que falta para", "i", 72), X, 680, "center", 0.12)
        E.frase(c, t, b5 + 0.8, ps("completar o reto", "i", 72) , X, 780, "center", 0.12)
    if t >= C["s05"]:
        E.saida(c, t, C["s06"] - 0.1, defin)
    if t >= C["s06"]:
        E.frase(c, t, C["s06"], ps("complemento de", "i", 76) + [("35°", "g", 80, COR)], X, 260, "center", 0.12)
        fcen(c, t, a6, "90 − 35 = 55", X, 440, 100)
        bola_txt(c, t, b6, "55°", X, 640, 115, 80, TINTA2)
        fcen(c, t, c6, "35 + 55 = 90", X, 880, 80, TINTA2)
        E.foco(c, t, c6 + 0.8, 0.4, lambda a: E.selo(c, X + 360, 852, 44, True, a))


# ---------------- suplementares ----------------
def b_suplemento(c, t, C, b):
    V, L = (600, 760), 440
    X = 1450
    a7, b7, c7, a8, b8, c8 = C["s07.a"], C["s07.b"], C["s07.c"], C["s08.a"], C["s08.b"], C["s08.c"]
    if t >= a7:
        q = ease_io(prog(t, a7, 0.8))
        M.line(c, *pt(V, L * q, 180), *pt(V, L * q, 0), TINTA, 1.0, 6)
        c.drawCircle(*V, 10 * ease_back(prog(t, a7 + 0.3, 0.4)), M.paint(TINTA))
    if t < b7 + 0.3:
        E.saida(c, t, b7, lambda: ang(c, t, a7 + 0.6, V, 0, 180, "180°", r=110))
    raio(c, t, b7, V, L * 0.95, 70)
    if t >= c7 - 0.4:
        ang(c, t, c7 - 0.4, V, 70, 180, "110°", r=120, tr=a8 - 0.4)
        ang(c, t, c7, V, 0, 70, "70°", r=90, cor=TINTA2, tr=c8)
    E.frase(c, t, c7 + 0.5, ps("lado a lado:", "i", 70), XE, 200, "left") if t < C["s08"] else None
    E.foco(c, t, c7 + 0.9, 0.5, lambda a: E.escreve(c, "180°", XE + 380, 200, 80, "g", COR, a)) if t < C["s08"] else None

    if t >= C["s08"]:
        E.frase(c, t, C["s08"], ps("somam 180°", "g", 72), X, 280, "center")
        E.frase(c, t, a8, [("suplementares", "g", 92, COR)], X, 410, "center")
        E.frase(c, t, a8 + 1.0, ps("suplemento de", "i", 70) + [("110°", "g", 74, COR)], X, 560, "center", 0.12)
        fcen(c, t, b8, "180 − 110 = 70", X, 700, 96)
        bola_txt(c, t, c8, "70°", X, 880, 105, 76, TINTA2)


# ---------------- opostos pelo vértice ----------------
def b_opostos(c, t, C, b):
    V, L = (600, 590), 440
    X = 1420
    a9, b9, a10, b10 = C["s09.a"], C["s09.b"], C["s10.a"], C["s10.b"]
    a11, b11, c11, e11 = C["s11.a"], C["s11.b"], C["s11.c"], C["s11.end"]
    a12, b12 = C["s12.a"], C["s12.b"]
    # "com qualquer medida": a tesoura abre e fecha, e as medidas acompanham
    t_mexe = c11 + 4.5
    th = 50 + 22 * math.sin(math.pi * 2 * M.clamp(prog(t, t_mexe, e11 - 1.2 - t_mexe))) if t_mexe < t < e11 - 1.2 else 50
    k = round(th)
    E.frase(c, t, C["s09"], ps("duas retas que se cruzam", "i", 70), W / 2, 130, "center", 0.12) if t < a10 else None
    cruz(c, t, a9, V, L, th)
    # os quatro ângulos: primeiro neutros, depois em duas famílias
    fam = ep(t, a10, 0.5)
    g_ = ((0, th), (th, 180), (180, 180 + th), (180 + th, 360))
    for i, (g1, g2) in enumerate(g_):
        if t >= b9 + 0.2 * i:
            cor = E.mix(CINZA, (E.COR if i % 2 == 0 else TINTA2), fam if i % 2 == 0 else ep(t, b10, 0.5))
            E.angulo(c, t, b9 + 0.2 * i, V, pt(V, 10, g1), pt(V, 10, g2), r=120 if i % 2 == 0 else 95, cor=cor)
    # medidas na prova
    tm = {0: a11, 1: b11, 2: c11, 3: c11 + 3}
    for i, (g1, g2) in enumerate(g_):
        s = f"{k}°" if i % 2 == 0 else f"{180 - k}°"
        cor = COR if i % 2 == 0 else TINTA2
        E.foco(c, t, tm[i], 0.4, lambda a, g1=g1, g2=g2, s=s, cor=cor, i=i: rotulo(c, V, (g1 + g2) / 2, 120 if i % 2 == 0 else 95, s, cor, 54, a))
    # a cunha de 50° gira meia volta em torno do vértice e cai em cima da oposta
    voa(c, t, c11 + 0.6, 1.4, V, 0, 50, 120, giro=180, fica=1.2)

    def def_():
        E.frase(c, t, a10, ps("de frente:", "i", 70), X, 360, "center", 0.12)
        E.frase(c, t, a10 + 0.6, ps("opostos pelo vértice", "g", 64, COR), X, 470, "center", 0.12)
        E.frase(c, t, b10, ps("mesma medida", "g", 80), X, 700, "center", 0.12)
    if t >= a10:
        E.saida(c, t, C["s11"] - 0.1, def_)

    def prova():
        E.frase(c, t, a11, ps("se um mede", "i", 70) + [("50°", "g", 74, COR)], X, 260, "center", 0.12)
        fcen(c, t, b11, "180 − 50 = 130", X, 430, 86, TINTA2)
        E.frase(c, t, b11 + 0.6, ps("o vizinho", "i", 56, TINTA2), X, 510, "center")
        fcen(c, t, c11, "180 − 130 = 50", X, 670, 86, COR)
        E.frase(c, t, c11 + 0.6, ps("o oposto", "i", 56, COR), X, 750, "center")
        E.frase(c, t, t_mexe, ps("com", "i", 70) + [("qualquer", "g", 72, COR)] + ps("medida", "i", 70), X, 930, "center", 0.12)
    if t >= C["s11"]:
        E.saida(c, t, C["s12"] - 0.1, prova)
    if t >= C["s12"]:
        E.frase(c, t, C["s12"], ps("a regra da", "i", 76) + [("tesoura", "g", 80, COR)], X, 280, "center", 0.12)
        E.frase(c, t, a12, ps("de frente:", "i", 72), X, 470, "center")
        E.frase(c, t, a12 + 0.5, [("iguais", "g", 96, COR)], X, 580, "center")
        E.frase(c, t, b12, ps("lado a lado:", "i", 72), X, 750, "center")
        E.frase(c, t, b12 + 0.5, [("somam 180°", "g", 96, TINTA2)], X, 860, "center")


# ---------------- com equação ----------------
def b_equacao(c, t, C, b):
    V, L, th = (470, 600), 360, 50
    X, PX = 1180, 1710
    a13, b13, c13 = C["s13.a"], C["s13.b"], C["s13.c"]
    a14, b14, c14, d14, e14 = C["s14.a"], C["s14.b"], C["s14.c"], C["s14.d"], C["s14.e"]
    a15, b15, c15 = C["s15.a"], C["s15.b"], C["s15.c"]
    cruz(c, t, C["s13"], V, L, th)
    ang(c, t, a13, V, 0, th, None, r=100)
    ang(c, t, b13, V, 180, 180 + th, None, r=100)
    ang(c, t, C["s13"] + 0.6, V, th, 180, None, r=76, cor=FIO)
    ang(c, t, C["s13"] + 0.8, V, 180 + th, 360, None, r=76, cor=FIO)
    um = ep(t, c15, 0.5)
    E.foco(c, t, a13, 0.4, lambda a: rotulo(c, V, th / 2, 100, "3x − 10", COR, 50, a * (1 - um)))
    E.foco(c, t, b13, 0.4, lambda a: rotulo(c, V, 180 + th / 2, 100, "x + 30", COR, 50, a * (1 - um)))
    E.foco(c, t, c15, 0.4, lambda a: (rotulo(c, V, th / 2, 100, "50°", COR, 56, a), rotulo(c, V, 180 + th / 2, 100, "50°", COR, 56, a)))
    E.frase(c, t, C["s13"], ps("com", "i", 70) + [("letra", "g", 72, COR)], V[0], 150, "center", 0.12)

    def contas():
        fcen(c, t, c13, "3x − 10 = x + 30", X, 220, 84)
        operacao(c, t, a14, "− x", PX, 330)
        fcen(c, t, b14, "2x − 10 = 30", X, 380, 84)
        operacao(c, t, c14, "+ 10", PX, 490)
        fcen(c, t, d14, "2x = 40", X, 540, 84)
        operacao(c, t, e14, "÷ 2", PX, 650)
        E.foco(c, t, e14 + 0.4, 0.5, lambda a: E.pilula(c, "x = 20", X, 680, 84, "g", a=a, cor=E.SOBRE))
    E.saida(c, t, C["s15"] - 0.1, contas)
    if t >= C["s15"]:
        E.frase(c, t, C["s15"], ps("x não é o ângulo", "i", 76), X, 220, "center", 0.12)
        fcen(c, t, a15, "3 · 20 − 10 = 50°", X, 400, 84)
        fcen(c, t, b15, "20 + 30 = 50°", X, 540, 84)
        bola_txt(c, t, c15, "50°", X, 760, 120, 84)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    a16, b16, c16 = C["s16.a"], C["s16.b"], C["s16.c"]
    a17, b17, c17, d17 = C["s17.a"], C["s17.b"], C["s17.c"], C["s17.d"]

    def erro():
        E.frase(c, t, C["s16"], ps("o erro do começo", "i", 80, ERRADO), W / 2, 180, "center", 0.12)
        fcen(c, t, a16, "180 − 35 = 145°", W / 2 - 300, 380, 96, ERRADO)
        if t >= c16:
            E.risco(c, W / 2 - 700, 400, W / 2 + 100, 300, t, c16, largura=12)
        E.foco(c, t, b16, 0.4, lambda a: E.pilula(c, "suplemento", W / 2 + 470, 350, 56, "g", fundo=TINTA, a=a))
        fcen(c, t, c16 + 0.4, "90 − 35 = 55°", W / 2 - 300, 560, 96, CERTO)
        E.foco(c, t, c16 + 0.4, 0.4, lambda a: E.pilula(c, "complemento", W / 2 + 470, 530, 56, "g", a=a, cor=E.SOBRE))
    E.saida(c, t, C["s17"] - 0.1, erro)
    if t >= C["s17"]:
        E.frase(c, t, C["s17"], ps("para não trocar", "i", 80, COR), W / 2, 180, "center", 0.12)
        E.frase(c, t, a17, [("C", "g", 150, COR)] + ps("vem antes de", "i", 80) + [("S", "g", 150, TINTA2)], W / 2, 420, "center", 0.2)
        E.frase(c, t, b17, [("90", "g", 130, COR)] + ps("vem antes de", "i", 80) + [("180", "g", 130, TINTA2)], W / 2, 640, "center", 0.2)
        E.foco(c, t, c17, 0.5, lambda a: E.pilula(c, "Complemento = 90°", 620, 860, 64, "g", a=a, cor=E.SOBRE))
        E.foco(c, t, d17, 0.5, lambda a: E.pilula(c, "Suplemento = 180°", 1300, 860, 64, "g", fundo=TINTA, a=a))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    V, L, g = (520, 780), 400, 35
    X = 1400
    a18, b18, c18 = C["s18.a"], C["s18.b"], C["s18.c"]
    a19, b19, c19 = C["s19.a"], C["s19.b"], C["s19.c"]
    if t >= C["s18"]:
        q = ease_io(prog(t, C["s18"], 0.8))
        M.line(c, *pt(V, L * q, 180), *pt(V, L * q, 0), BR, 1.0, 6)
        raio(c, t, C["s18"] + 0.4, V, L, g, BR)
        c.drawCircle(*V, 10, M.paint(BR))
    raio(c, t, a18, V, L * 0.85, 90, CLARO, tracejado=True, largura=4)
    ang(c, t, a18, V, 0, g, "35°", r=150, cor=BR, size=48)
    ang(c, t, lerp(a18, b18, 0.55), V, g, 90, "55°", r=100, cor=CLARO, size=48)
    ang(c, t, b18, V, 90, 180, "90°", r=90, cor=CLARO, size=48)
    if t >= c18:
        E.arco(c, V[0], V[1], 230, -180, 180 - g, CLARO, 7, ep(t, c18, 0.5))
        E.foco(c, t, c18 + 0.2, 0.4, lambda a: rotulo(c, V, (g + 180) / 2, 230, "145°", CLARO, 64, a))

    def regra():
        E.frase(c, t, a18, ps("ângulo agudo:", "i", 70, CLARO), X, 240, "center", 0.12)
        E.frase(c, t, a18 + 0.8, [("suplemento =", "g", 70, BR)], X, 350, "center")
        E.frase(c, t, a18 + 1.4, [("complemento + 90°", "g", 70, BR)], X, 450, "center")
        E.frase(c, t, lerp(a18, b18, 0.55), ps("complemento de", "i", 60, CLARO) + [("35°: 55°", "g", 64, BR)], X, 620, "center", 0.1)
        fcen(c, t, b18, "55 + 90 = 145°", X, 800, 96, BR)
    E.saida(c, t, C["s19"] - 0.1, regra)
    if t >= C["s19"]:
        fcen(c, t, a19, "180 = 90 + 90", X, 280, 96, BR)
        E.frase(c, t, b19, [("90° ou mais:", "g", 66, ERRADO)], X, 480, "center")
        E.frase(c, t, b19 + 0.6, ps("não tem complemento", "i", 66, CLARO), X, 570, "center", 0.12)
        E.frase(c, t, c19, ps("aí, direto:", "i", 66, CLARO), X, 740, "center", 0.12)
        fcen(c, t, c19 + 0.5, "180 − ângulo", X, 860, 90, BR)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    V, L, th = (1380, 640), 420, 80
    E.frase(c, t, C["s20"], ps("hora de testar", "i", 72, COR), XE, 200, passo=0.12)
    E.frase(c, t, C["s20"] + 1.5, ps("duas retas se cruzam", "i", 76), XE, 340, passo=0.12)
    E.frase(c, t, C["s20.a"], ps("lado a lado:", "i", 76), XE, 480, passo=0.12)
    fcen(c, t, C["s20.a"] + 0.6, "x + 40", XE + 160, 610, 90, COR)
    E.frase(c, t, C["s20.b"], ps("e", "i", 76), XE + 330, 610)
    fcen(c, t, C["s20.b"] + 0.3, "2x + 20", XE + 560, 610, 90, TINTA2)
    E.frase(c, t, C["s20.c"], ps("quanto mede", "i", 96) + [("cada um?", "g", 96, COR)], XE, 820, passo=0.14)

    def fig():
        cruz(c, t, C["s20"] + 1.5, V, L, th)
        ang(c, t, C["s20.a"], V, 0, th, "x + 40", r=80, size=50)
        ang(c, t, C["s20.b"], V, th, 180, "2x + 20", r=66, cor=TINTA2, size=50)
    E.saida(c, t, C["s21.a"] - 0.1, fig)
    E.relogio(c, t, C["s21.a"])


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    V, L, th = (430, 620), 340, 80
    X, PX = 1180, 1720
    a22, b22, c22, d22, e22 = C["s22.a"], C["s22.b"], C["s22.c"], C["s22.d"], C["s22.e"]
    a23, b23, c23, d23 = C["s23.a"], C["s23.b"], C["s23.c"], C["s23.d"]
    cruz(c, t, C["s22"], V, L, th)
    novo1, novo2 = ep(t, a23, 0.4), ep(t, b23, 0.4)
    ang(c, t, C["s22"] + 0.4, V, 0, th, None, r=110)
    ang(c, t, C["s22"] + 0.6, V, th, 180, None, r=85, cor=TINTA2)
    E.foco(c, t, C["s22"] + 0.6, 0.4, lambda a: rotulo(c, V, th / 2, 110, "x + 40", COR, 46, a * (1 - novo1)))
    E.foco(c, t, C["s22"] + 0.8, 0.4, lambda a: rotulo(c, V, (th + 180) / 2, 85, "2x + 20", TINTA2, 46, a * (1 - novo2)))
    E.foco(c, t, a23, 0.4, lambda a: rotulo(c, V, th / 2, 110, "80°", COR, 56, a))
    E.foco(c, t, b23, 0.4, lambda a: rotulo(c, V, (th + 180) / 2, 85, "100°", TINTA2, 56, a))
    if t >= a22:
        E.arco(c, V[0], V[1], 290, -180, 180, TINTA2, 4, ep(t, a22, 0.5) * (1 - ep(t, C["s23"], 0.4)))

    def contas():
        E.frase(c, t, a22, ps("lado a lado:", "i", 70) + [("somam 180°", "g", 72, COR)], X, 200, "center", 0.12)
        fcen(c, t, b22, "x + 40 + 2x + 20 = 180", X, 340, 72)
        fcen(c, t, c22, "3x + 60 = 180", X, 480, 80)
        operacao(c, t, d22, "− 60", PX, 560)
        fcen(c, t, d22 + 0.3, "3x = 120", X, 620, 80)
        operacao(c, t, e22, "÷ 3", PX, 720)
        E.foco(c, t, e22 + 0.4, 0.5, lambda a: E.pilula(c, "x = 40", X, 760, 80, "g", a=a, cor=E.SOBRE))
    E.saida(c, t, C["s23"] - 0.1, contas)
    if t >= C["s23"]:
        fcen(c, t, a23, "40 + 40 = 80°", X, 220, 80, COR)
        fcen(c, t, b23, "2 · 40 + 20 = 100°", X, 350, 80, TINTA2)
        fcen(c, t, c23, "80 + 100 = 180", X, 480, 80)
        E.foco(c, t, c23 + 0.8, 0.4, lambda a: E.selo(c, X + 380, 452, 44, True, a))
        E.frase(c, t, d23 - 2.5, ps("quem iguala, como se fossem opostos:", "i", 54, TINTA2), X, 680, "center", 0.08)
        fcen(c, t, d23, "60° e 60°", X, 810, 90, ERRADO)
        E.frase(c, t, d23 + 1.0, ps("não fecham a linha reta", "i", 60, ERRADO), X, 920, "center", 0.1)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s24"], [("resumindo", "i", 92, COR)], W / 2, 210, "center")
        itens = (("s24.a", "complementares: somam 90°"), ("s24.b", "suplementares: somam 180°"), ("s24.c", "opostos pelo vértice: iguais"))
        for i, (k, s) in enumerate(itens):
            y = 390 + i * 190
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 360, y - 30, 56, a=a), centro(c, str(i + 1), 360, y - 7, 64, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, [(s, "g", 80)], 460, y)
    E.saida(c, t, C["s25"] - 0.1, resumo)
    if t < C["s25"]:
        return
    E.frase(c, t, C["s25.a"] - 1.0, ps("próxima aula", "i", 84), XE, 300)
    E.frase(c, t, C["s25.a"], [("Retas", "g", 140, COR)], XE, 450)
    E.frase(c, t, C["s25.a"] + 0.3, [("paralelas", "g", 140, COR)], XE, 590)
    E.frase(c, t, C["s25.b"], ps("e os", "i", 76) + [("8 ângulos", "g", 76)] + ps("que surgem", "i", 76), XE, 720, passo=0.12)
    E.foco(c, t, C["s25.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1450, 400, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s25.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1780, 1580, p), lerp(720, 425, p), ep(t, C["s25.c"] + 0.2, 0.4))
    E.frase(c, t, C["s25.d"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 920, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, complemento=b_complemento, suplemento=b_suplemento, opostos=b_opostos,
              equacao=b_equacao, erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
