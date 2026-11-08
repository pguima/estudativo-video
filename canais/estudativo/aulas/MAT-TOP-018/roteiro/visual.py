"""Visual — Estudativo · MAT-TOP-018: praticando bases, algarismos significativos, troncos e homotetia (aula de prática).

Reúne as linguagens das quatro aulas do bloco: o quadro de casas 16 8 4 2 1 da MAT-TOP-014 (1 em índigo, 0 em cinza, resto em
âmbar); os algarismos coloridos pelo papel da MAT-TOP-015 (índigo = significativo, âmbar = estimado, cinza = só marca a vírgula,
vermelho = sai no arredondamento); a pirâmide cortada da MAT-TOP-016 (ponta em âmbar, tronco em índigo); e a lanterna da
MAT-TOP-017 (centro com halo âmbar, raios tracejados, original em tinta, imagem em índigo). Atalho (1 − k³) no palco escuro."""
import math
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Matemática", "Tópicos Avançados")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-TOP-018_praticando_bases_troncos_homotetia.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("questao1", "questao2", "questao3", "atalho", "questao4", "fim"))
BR = "#FFFFFF"
EST = "#D98A00"
PONTA = "#D98A00"
LUZ = "#D98A00"
C_ESC = "#3CC7D3"
assert int("11010", 2) == 26 and divmod(200, 60) == (3, 20)
assert round(1.2 * 3.456, 4) == 4.1472 and abs(250 * 8 / 125 - 16) < 1e-9 and 250 - 16 == 234 and abs(250 * 117 / 125 - 234) < 1e-9
assert 5 * 4 == 20 and 12 * 16 == 192 and 12 * 4 == 48 and 16 / 250 < 0.1


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


def titulo(c, t, t0, s):
    E.frase(c, t, t0, ps(s, "i", 66, COR), XE, 190)


def larg_digitos(s, size):
    return sum(E.larg(ch, "g", size) for ch in s) + size * 0.03 * (len(s) - 1)


def digitos(c, s, x, y, size, cores=None, a=1.0, padrao=TINTA):
    xx, xs = x, []
    for i, ch in enumerate(s):
        wc = E.larg(ch, "g", size)
        if a > 0:
            E.escreve(c, ch, xx, y, size, "g", (cores or {}).get(i, padrao), a)
        xs.append(xx + wc / 2)
        xx += wc + size * 0.03
    return xs


def num_base(c, s, b, x, y, size, cor=TINTA, a=1.0):
    w = E.larg(s, "g", size)
    E.escreve(c, s, x, y, size, "g", cor, a)
    E.escreve(c, b, x + w + 6, y + size * 0.22, size * 0.45, "g", cor, a)
    return w + E.larg(b, "g", size * 0.45) + 6


VAL = (16, 8, 4, 2, 1)


def casas(c, t, t0, x, y, w, size=60):
    for i, v in enumerate(VAL):
        cx = x + (i + 0.5) * w
        E.foco(c, t, t0 + 0.05 * i, 0.4, lambda a, v=v, cx=cx: (M.rrect(c, cx - w * 0.42, y - size * 1.05, w * 0.84, size * 1.4, 20, COR, 0.12 * a),
                                                                 E.centro(c, str(v), cx, y, size, "g", COR, a)))


def pausa(c, t, t0, cx=1460, cy=470, r=190):
    E.relogio(c, t, t0, cx=cx, cy=cy, r=r)


def _proj(x, y, z, cx, cy, k):
    return cx + (x + 0.45 * z) * k, cy - (y + 0.30 * z) * k


def pir_px(c, cx, cy, k, L, l, h, a=1.0, cor=None, largura=6):
    if a <= 0:
        return
    cor = cor or COR
    P = lambda x, y, z: _proj(x, y, z, cx, cy, k)
    B = [P(-L / 2, 0, -L / 2), P(L / 2, 0, -L / 2), P(L / 2, 0, L / 2), P(-L / 2, 0, L / 2)]
    T = [P(-l / 2, h, -l / 2), P(l / 2, h, -l / 2), P(l / 2, h, l / 2), P(-l / 2, h, l / 2)]
    for face, f in (((B[0], B[1], T[1], T[0]), 0.80), ((B[1], B[2], T[2], T[1]), 0.70)):
        path = skia.Path(); path.addPoly(list(face), True)
        c.drawPath(path, M.paint(E.mix(cor, "#FFFFFF", f), a))
    if l > 0:
        path = skia.Path(); path.addPoly(T, True)
        c.drawPath(path, M.paint(E.mix(cor, "#FFFFFF", 0.62), a))
    oc = M.paint(TINTA, 0.55 * a, stroke=largura - 2, cap_round=True)
    oc.setPathEffect(skia.DashPathEffect.Make(E.TRACO, 0))
    for p_, q_ in ((B[2], B[3]), (B[3], B[0]), (B[3], T[3])):
        c.drawLine(*p_, *q_, oc)
    for p_, q_ in ((B[0], B[1]), (B[1], B[2]), (B[0], T[0]), (B[1], T[1]), (B[2], T[2])):
        M.line(c, *p_, *q_, TINTA, a, largura)
    if l > 0:
        for i in range(4):
            M.line(c, *T[i], *T[(i + 1) % 4], TINTA, a, largura)


def corte_pir(c, cx, cy, k, h_corte, l, a=1.0):
    P = lambda x, y, z: _proj(x, y, z, cx, cy, k)
    m = l / 2 + 0.6
    pts = [P(-m, h_corte, -m), P(m, h_corte, -m), P(m, h_corte, m), P(-m, h_corte, m)]
    path = skia.Path(); path.addPoly(pts, True)
    pt = M.paint(PONTA, a, stroke=5)
    pt.setPathEffect(skia.DashPathEffect.Make([14, 10], 0))
    c.drawPath(path, pt)


def tri(c, pts, p=1.0, cor=TINTA, fundo=None, largura=6, a=1.0):
    if p <= 0 or a <= 0:
        return
    if fundo is not None:
        path = skia.Path(); path.addPoly(list(pts), True)
        c.drawPath(path, M.paint(fundo, 0.16 * a * min(1, p * 1.5)))
    seq = list(pts) + [pts[0]]
    for i in range(len(pts)):
        f = max(0.0, min(1.0, len(pts) * p - i))
        if f > 0:
            M.line(c, *seq[i], *seq[i + 1], cor, a, largura, progress=f)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    E.frase(c, t, C["s01.a"], [("4", "g", 200, COR), ("situações", "i", 150)], XE, 330)
    itens = ("bases de contagem", "algarismos significativos", "troncos", "homotetia")
    for i, s in enumerate(itens):
        x = XE + (i % 2) * 820
        y = 520 + (i // 2) * 140
        t0 = C["s01.b"] + 0.8 * i if i < 2 else C["s01.c"] + 0.6 * (i - 2)
        E.foco(c, t, t0, 0.5, lambda a, x=x, y=y, i=i: (E.bola(c, x + 34, y - 26, 34, a=a),
                                                       E.escreve(c, str(i + 1), x + 34 - E.larg(str(i + 1), "g", 40) / 2, y - 12, 40, "g", BR, a)))
        E.frase(c, t, t0 + 0.1, [(s, "g", 64)], x + 100, y)
    E.foco(c, t, C["s01.d"], 0.5, lambda a: E.pilula(c, "pause e resolva", W / 2, 930, 60, "g", a=a))


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s02.a"], [("as", "i", 80), ("ferramentas", "g", 80, COR)], W / 2, 170, "center")
    itens = (("s02.b", "base 2:", "16  8  4  2  1"), ("s02.c", "medidas:", "manda a com menos significativos"),
             ("s02.d", "tronco:", "inteiro − ponta  (ponta: × k^3)"), ("s02.e", "homotetia:", "comprimento × k,  área × k^2"))
    for i, (k, l1, f) in enumerate(itens):
        y = 330 + i * 160
        E.frase(c, t, C[k], [(l1, "g", 62, COR)], XE + 40, y)
        E.foco(c, t, C[k] + 0.5, 0.5, lambda a, f=f, y=y: E.formula(c, f, 620, y, 60, "b", TINTA, a))
    E.frase(c, t, C["s03"] - 2.4, ps("travou? procure a aula no canal", "i", 50, TINTA2), W / 2, 1000, "center", passo=0.1)


# ---------------- situação 1: bases ----------------
X1, W1 = 470, 196


def b_questao1(c, t, C, b):
    titulo(c, t, C["s03"], "situação 1")
    E.foco(c, t, C["s03.a"], 0.5, lambda a: num_base(c, "11010", "2", XE, 400, 150, TINTA, a))
    E.frase(c, t, C["s03.b"], [("na", "i", 70), ("base", "i", 70), ("10?", "g", 76, COR)], XE + 620, 400)
    E.frase(c, t, C["s03.c"], [("200", "g", 110), ("minutos", "i", 90), ("=", "i", 90), ("?", "g", 110, COR)], XE, 640)
    if t >= C["s04"]:
        pausa(c, t, C["s04.a"], 1500, 700, 150)


def b_resposta1(c, t, C, b):
    titulo(c, t, C["s05"], "situação 1")

    def s05():
        casas(c, t, C["s05.a"], X1, 380, W1, 66)
        for j, d in enumerate("11010"):
            cx = X1 + (j + 0.5) * W1
            E.foco(c, t, C["s05.a"] + 0.3 + 0.12 * j, 0.4, lambda a, d=d, cx=cx: E.centro(c, d, cx, 570, 130, "g", COR if d == "1" else CINZA, a))
        if t >= C["s05.b"]:
            for i_, j in enumerate((0, 1, 3)):
                q = ep(t, C["s05.b"] + 0.3 * i_, 0.4)
                c.drawCircle(X1 + (j + 0.5) * W1, 525, 90, M.paint(COR, 0.12 * q))
        conta_em(c, t, C["s05.b"] + 0.4, [("16 + 8 + 2 = ", TINTA)], 640, 800, 92)
        bola_txt(c, t, C["s05.c"], "26", 1300, 770, 80, 86)
    E.saida(c, t, C["s06"] - 0.1, s05)
    if t < C["s06"]:
        return
    conta_em(c, t, C["s06.a"], [("200 ÷ 60 = ", TINTA), ("3", COR), (", resto ", TINTA), ("20", EST)], XE, 420, 92)
    E.foco(c, t, C["s06.a"] + 1.4, 0.4, lambda a: (E.pilula(c, "horas", XE + 480, 520, 40, "g", fundo=COR, a=a),
                                                  E.pilula(c, "minutos", XE + 870, 520, 40, "g", fundo=EST, a=a)))
    bola_txt(c, t, C["s06.b"], "3 h 20 min", 1440, 640, 200, 70, CERTO)


# ---------------- situação 2: significativos ----------------
def b_questao2(c, t, C, b):
    titulo(c, t, C["s07"], "situação 2")
    E.frase(c, t, C["s07.a"], [("1)", "g", 64, COR), ("significativos", "i", 70), ("de", "i", 70)], XE, 340)
    E.foco(c, t, C["s07.a"] + 0.6, 0.5, lambda a: digitos(c, "0,00250", XE + 80, 480, 120, a=a))
    E.frase(c, t, C["s07.b"], [("2)", "g", 64, COR)], XE, 680)
    E.foco(c, t, C["s07.b"] + 0.2, 0.4, lambda a: E.escreve(c, "1,2 × 3,456 = ?", XE + 100, 680, 100, "g", TINTA, a))
    E.frase(c, t, C["s07.b"] + 2.4, ps("com os significativos certos", "i", 56, TINTA2), XE + 100, 780, passo=0.1)
    if t >= C["s08"]:
        pausa(c, t, C["s08.a"], 1500, 470, 180)


def b_resposta2(c, t, C, b):
    titulo(c, t, C["s09"], "situação 2")

    def s09():
        s = "0,00250"
        cc = {}
        if t >= C["s09.a"]:
            cc.update({0: CINZA, 1: CINZA, 2: CINZA, 3: CINZA})
        if t >= C["s09.b"]:
            cc.update({4: COR, 5: COR, 6: EST})
        digitos(c, s, 330, 480, 180, cc, ep(t, C["s09"], 0.4))
        E.foco(c, t, C["s09.a"] + 0.3, 0.4, lambda a: E.pilula(c, "só marcam a vírgula", 560, 580, 42, "g", fundo=CINZA, a=a))
        E.foco(c, t, C["s09.c"], 0.4, lambda a: E.pilula(c, "3 significativos", 1250, 720, 64, "g", fundo=CERTO, a=a))
    E.saida(c, t, C["s10"] - 0.1, s09)
    if t < C["s10"]:
        return
    s = "4,1472"
    cc = {}
    if t >= C["s10.d"]:
        cc = {0: COR, 2: EST, 3: ERRADO, 4: ERRADO, 5: ERRADO}
    E.foco(c, t, C["s10.a"], 0.4, lambda a: E.escreve(c, "1,2 × 3,456 =", 260, 400, 96, "g", TINTA, a))
    E.foco(c, t, C["s10.a"] + 0.6, 0.4, lambda a: digitos(c, s, 1000, 400, 110, cc, a))
    E.foco(c, t, C["s10.b"], 0.4, lambda a: E.pilula(c, "2 signif.", 330, 500, 42, "g", a=a))
    E.foco(c, t, C["s10.c"], 0.4, lambda a: E.pilula(c, "4 signif.", 650, 500, 42, "g", fundo=TINTA, a=a))
    E.frase(c, t, C["s10.d"], ps("o seguinte é 4: não sobe", "i", 62), XE, 700, passo=0.1)
    bola_txt(c, t, C["s10.e"], "4,1", 1300, 700, 120, 100, CERTO)


# ---------------- situação 3: tronco ----------------
PK, PCX, PCY = 62, 1330, 900


def b_questao3(c, t, C, b):
    titulo(c, t, C["s11"], "situação 3")
    pir_px(c, PCX, PCY, PK, 6, 0, 10, ep(t, C["s11.a"], 0.5))
    if t >= C["s11.b"]:
        corte_pir(c, PCX, PCY, PK, 6, 2.4, ep(t, C["s11.b"], 0.4))
    E.frase(c, t, C["s11.a"], [("pirâmide:", "i", 70), ("V = 250", "g", 70, COR)], XE, 360)
    E.frase(c, t, C["s11.b"], ps("corte a 2/5 da altura,", "i", 62), XE, 500, passo=0.1)
    E.frase(c, t, C["s11.b"] + 1.2, ps("contando do vértice", "i", 62), XE, 590, passo=0.1)
    E.frase(c, t, C["s11.c"], [("tronco?", "g", 80, COR)], XE, 760)
    if t >= C["s12"]:
        pausa(c, t, C["s12.a"], 760, 760, 90)


def b_resposta3(c, t, C, b):
    titulo(c, t, C["s13"], "situação 3")
    s = ease_io(prog(t, C["s13.c"], 0.8))
    if s <= 0:
        pir_px(c, PCX, PCY, PK, 6, 0, 10)
        corte_pir(c, PCX, PCY, PK, 6, 2.4)
    else:
        pir_px(c, PCX, PCY, PK, 6, 2.4, 6)
        pir_px(c, PCX, PCY - 6 * PK - 110 * s, PK, 2.4, 0, 4, 1.0, PONTA)
    P = lambda x, y, z: _proj(x, y, z, PCX, PCY, PK)
    E.foco(c, t, C["s13.c"] + 0.4, 0.4, lambda a: E.pilula(c, "16", P(0, 7.8, 0)[0], P(0, 7.8, 0)[1] - 110, 52, "g", fundo=PONTA, a=a))
    E.foco(c, t, C["s13.d"], 0.4, lambda a: E.pilula(c, "234", P(0, 2.4, 0)[0] + 20, P(0, 2.4, 0)[1] + 10, 56, "g", fundo=COR, a=a))
    conta_em(c, t, C["s13.a"], [("k = f{2}{5}", PONTA)], XE, 350, 76)
    conta_em(c, t, C["s13.b"], [("(f{2}{5})^3 = f{8}{125}", TINTA)], XE, 500, 76)
    conta_em(c, t, C["s13.c"], [("250 · f{8}{125} = ", TINTA), ("16", PONTA)], XE, 660, 76)
    conta_em(c, t, C["s13.d"], [("250 − 16 = ", TINTA)], XE, 820, 80)
    bola_txt(c, t, C["s13.d"] + 0.4, "234", XE + 520, 795, 85, 70, CERTO)
    E.frase(c, t, C["s13.e"], ps("a ponta: nem 1/10 do total", "i", 52, TINTA2), XE, 960, passo=0.1)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def s14():
        E.frase(c, t, C["s14"], ps("agora, um atalho", "i", 76, CLARO), W / 2, 190, "center")
        E.frase(c, t, C["s14.a"], [("fração", "i", 84, CLARO), ("do", "i", 84, CLARO), ("tronco", "g", 84, BR), ("=", "g", 84, CLARO), ("1", "g", 84, BR),
                                   ("−", "g", 84, BR), ("k³", "g", 84, C_ESC)], W / 2, 380, "center", passo=0.15)
        conta_em(c, t, C["s14.b"], [("1 − f{8}{125} = f{117}{125}", BR)], W / 2, 600, 96, "center")
        conta_em(c, t, C["s14.c"], [("250 · f{117}{125} = ", BR), ("234", C_ESC)], W / 2, 820, 96, "center")
    E.saida(c, t, C["s15"] - 0.1, s14)
    if t < C["s15"]:
        return
    E.frase(c, t, C["s15"], [("por", "i", 70, CLARO), ("que", "i", 70, CLARO), ("funciona", "g", 70, BR)], W / 2, 220, "center")
    E.frase(c, t, C["s15.a"], [("inteiro", "g", 70, BR), ("=", "i", 72, CLARO), ("1;", "g", 70, BR), ("ponta", "g", 70, PONTA), ("=", "i", 72, CLARO),
                               ("k³", "g", 70, C_ESC)], W / 2, 400, "center")
    E.frase(c, t, C["s15.b"], [("não", "g", 66, ERRADO), ("compensa:", "i", 70, CLARO), ("pediu", "i", 70, CLARO), ("a", "i", 70, CLARO), ("ponta", "g", 66, PONTA),
                               ("também", "i", 70, CLARO)], W / 2, 640, "center", passo=0.12)
    E.frase(c, t, C["s15.b"] + 2.4, ps("aí, ponta primeiro, depois a subtração", "i", 60, CLARO), W / 2, 760, "center", passo=0.1)


# ---------------- situação 4: homotetia ----------------
O4 = (1180, 600)



def cena4(c, t, t0, tr, ti):
    a = ep(t, t0, 0.5)
    if a > 0:
        M.rrect(c, O4[0] - 140, O4[1] - 36, 140, 72, 16, TINTA, a)
        c.drawCircle(*O4, 40, M.paint(LUZ, 0.9 * a))
    # o recorte, perto da lanterna, e a sombra, quatro vezes maior, na parede
    o = ((1280, 560), (1330, 560), (1330, 620), (1280, 620))
    im = tuple((O4[0] + 4 * (x - O4[0]), O4[1] + 4 * (y - O4[1])) for x, y in o)
    tri(c, o, ep(t, t0 + 0.3, 0.6), TINTA, TINTA, 6)
    for i, Q in enumerate(im):
        p = ease_io(prog(t, tr + 0.1 * i, 0.6))
        if p > 0:
            M.line(c, *O4, lerp(O4[0], Q[0], p), lerp(O4[1], Q[1], p), LUZ, 0.85, 4, dash=E.TRACO)
    tri(c, im, ease_io(prog(t, ti, 0.7)), COR, COR, 8)
    return o, im


def b_questao4(c, t, C, b):
    titulo(c, t, C["s16"], "última situação")
    o, im = cena4(c, t, C["s16.a"], C["s16.b"], C["s16.b"] + 0.6)
    E.frase(c, t, C["s16.a"], ps("lanterna e sombra", "i", 62), XE, 330)
    E.frase(c, t, C["s16.b"], [("razão", "i", 66), ("k = 4", "g", 66, COR)], XE, 440)
    E.frase(c, t, C["s16.c"], [("recorte:", "i", 62), ("5 cm", "g", 62)], XE, 590)
    E.frase(c, t, C["s16.d"], [("área", "i", 62), ("12 cm²", "g", 62)], XE + 450, 590)
    E.frase(c, t, C["s16.e"], [("sombra:", "i", 70), ("largura?", "g", 66, COR), ("área?", "g", 66, COR)], XE, 760)
    if t >= C["s17"]:
        pausa(c, t, C["s17.a"], 760, 920 - 40, 60)


def b_resposta4(c, t, C, b):
    titulo(c, t, C["s18"], "última situação")
    o, im = cena4(c, t, C["s18"] - 3, C["s18"] - 3, C["s18"] - 3)
    E.foco(c, t, C["s18.b"], 0.4, lambda a: E.pilula(c, "20 cm", (im[0][0] + im[1][0]) / 2, im[0][1] - 40, 44, "g", fundo=COR, a=a))
    E.foco(c, t, C["s18.d"], 0.4, lambda a: E.pilula(c, "192 cm²", (im[0][0] + im[1][0]) / 2, (im[0][1] + im[2][1]) / 2, 48, "g", fundo=CERTO, a=a))
    conta_em(c, t, C["s18.a"], [("comprimento: × 4", TINTA2)], XE, 330, 56)
    conta_em(c, t, C["s18.b"], [("5 · 4 = ", TINTA), ("20 cm", COR)], XE, 440, 76)
    conta_em(c, t, C["s18.c"], [("área: × k^2 = × 16", TINTA2)], XE, 580, 56)
    conta_em(c, t, C["s18.d"], [("12 · 16 = ", TINTA), ("192 cm²", CERTO)], XE, 690, 76)
    conta_em(c, t, C["s18.e"], [("12 · 4 = 48", ERRADO)], XE, 860, 66)
    if t >= C["s18.e"] + 1.0:
        E.risco(c, XE - 10, 880, XE + 420, 810, t, C["s18.e"] + 1.0, largura=10)
    E.frase(c, t, C["s18.f"], ps("cresce na largura e na altura", "i", 52, TINTA2), XE, 960, passo=0.1)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s19"], [("resumindo", "i", 92, COR)], W / 2, 190, "center")
        itens = (("s19.a", [("base", "i", 66), ("2:", "g", 64, COR), ("some", "i", 66), ("as", "i", 66), ("casas", "i", 66), ("com", "i", 66), ("1", "g", 64, COR)]),
                 ("s19.b", [("medidas:", "g", 64), ("manda", "i", 66), ("a", "i", 66), ("mais", "i", 66), ("pobre", "g", 64)]),
                 ("s19.c", [("tronco:", "g", 64, COR), ("tire", "i", 66), ("a", "i", 66), ("ponta", "g", 64, PONTA)]),
                 ("s19.d", [("homotetia:", "g", 64, COR), ("área", "i", 66), ("×", "g", 64), ("k²", "g", 64, COR)]))
        for i, (k, partes) in enumerate(itens):
            y = 360 + i * 160
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 240, y - 24, 52, a=a),
                                                         E.escreve(c, str(i + 1), 240 - E.larg(str(i + 1), "g", 60) / 2, y - 3, 60, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, partes, 340, y, passo=0.12)
    E.saida(c, t, C["s20"] - 0.1, resumo)
    if t < C["s20"]:
        return
    E.frase(c, t, C["s20.a"], [("trilha", "i", 90), ("concluída:", "g", 90, CERTO)], XE, 330)
    E.frase(c, t, C["s20.a"] + 0.8, [("Tópicos", "g", 130, COR), ("Avançados", "g", 130, COR)], XE, 500)
    E.frase(c, t, C["s20.a"] + 2.4, ps("travou? procure a aula no canal", "i", 58, TINTA2), XE, 620, passo=0.1)
    E.foco(c, t, C["s20.b"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1450, 760, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s20.b"] + 0.3, 0.8))
    E.cursor(c, lerp(1780, 1580, p), lerp(960, 785, p), ep(t, C["s20.b"] + 0.2, 0.4))
    E.frase(c, t, C["s20.c"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 960, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, questao1=b_questao1, resposta1=b_resposta1, questao2=b_questao2, resposta2=b_resposta2,
              questao3=b_questao3, resposta3=b_resposta3, atalho=b_atalho, questao4=b_questao4, resposta4=b_resposta4, fim=b_fim)
