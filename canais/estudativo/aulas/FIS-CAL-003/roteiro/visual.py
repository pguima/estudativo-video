"""Visual — Estudativo · FIS-CAL-003: calor sensível, Q = m·c·ΔT.
Segue a linguagem visual da trilha Calor e Termodinâmica (cabeçalho do visual.py da FIS-CAL-001: quente laranja, frio azul,
termômetro, seta ondulada do calor, fórmula com legenda, contas empilhadas e resultado na esfera) e a da Física (FIS-CIN-001).
Peças próprias: praia (areia, mar e sol), o "que macete" (letras da fórmula com a sílaba embaixo) e as faixas de temperatura
do litoral e do deserto (faixa_temp).
Todo instante vem de C[...] (marcadores do roteiro)."""
import math

import editorial as E
import fisica as F
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Física", "Calor e Termodinâmica")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_FIS-CAL-003_calor_sensivel.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("caloria", "formula", "exemplo", "praia", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
FRIO = F.NEG
GELO = "#A9D8F5"
AGUA = "#5BA8E0"
AREIA = "#E8C77A"

# todas as contas da aula
Q = lambda m, c, dT: m * c * dT
assert 80 - 20 == 60 and Q(500, 1, 60) == 30000 and 30000 / 1000 == 30
assert Q(500, 1, 20 - 80) == -30000
assert 1000 * 1 == 1000 and 1000 / 1000 == 1 and math.isclose(1000 * 0.2, 200) and 1000 / 200 == 5
assert math.isclose(Q(0.5, 1, 60), 30) and Q(500, 1, 60) / Q(0.5, 1, 60) == 1000
assert 400 * 1 == 400 and 12000 / 400 == 30 and 25 + 30 == 55


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças desta aula (e da trilha) ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def bola_txt(c, t, t0, s, cx, cy, r, size, cor=None):
    """resposta na esfera: "40 °C" com a unidade menor"""
    v, _, u = s.partition(" ")
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r * ease_back(prog(t, t0, 0.5)), cor, a),
                                     F.medida(c, v, u, cx, cy + size * 0.36, size, E.SOBRE, a, "center", cor_u=E.SOBRE)))


def pilula_em(c, t, t0, s, cx, cy, size, fundo=None, est="g"):
    E.foco(c, t, t0, 0.4, lambda a: E.pilula(c, s, cx, cy, size, est, fundo=fundo, a=a, cor=BR))


def formula_em(c, t, t0, s, x, y, size, est="g", cor=TINTA, align="left"):
    E.formula_em(c, t, t0, s, x, y, size, est, cor, align)


def y_term(v, yb, h, vmin, vmax):
    """altura (pixel) do valor v num F.termometro de bulbo em yb e altura h"""
    base_t, topo = yb - 24, yb - h
    return base_t - (v - vmin) / (vmax - vmin) * (base_t - topo - 16)


def term(c, t, t0, cx, yb, h, v, vmin, vmax, escuro=False):
    """termômetro cujo nível v é controlado por quem chama (sobe do vmin em 0,8 s a partir de t0)"""
    if t < t0:
        return
    F.termometro(c, t, t0, cx, yb, h, lerp(vmin, v, ease_io(prog(t, t0, 0.8))) if v is not None else vmin, vmin, vmax, (), d=0.001, escuro=escuro)


def marca(c, t, t0, cx, y, valor, unid, size=44, cor=None, escuro=False, acima=False):
    """traço e medida à direita de um termômetro em cx, na altura y (acima=True: o texto fica sobre a linha tracejada)"""
    def fn(a):
        M.line(c, cx + 30, y, cx + 56, y, BR if escuro else TINTA, a, 4)
        F.medida(c, valor, unid, cx + 64, y - 14 if acima else y + size * 0.36, size, cor, a, escuro=escuro)
    E.foco(c, t, t0, 0.4, fn, sobe=6)


def tracejado(c, t, t0, x0, x1, y, cor=TINTA2, d=0.6, largura=4):
    if t >= t0:
        M.line(c, x0, y, x1, y, cor, 0.8, largura, dash=E.TRACO, progress=ease_io(prog(t, t0, d)))


def cota_v(c, t, t0, x, y0, y1, rotulo=None, cor=None, lado=-1, size=52, d=0.5, est="g"):
    """colchete vertical de y0 a y1 em x, aberto para o lado oposto a `lado`; rótulo (fórmula) do lado `lado`"""
    q = ep(t, t0, d)
    if q <= 0:
        return
    cor = cor or E.COR
    k = 22 * -lado
    ym = (y0 + y1) / 2
    a_, b_ = lerp(ym, y0, q), lerp(ym, y1, q)
    p = skia.Path()
    p.moveTo(x + k, a_); p.lineTo(x, a_); p.lineTo(x, b_); p.lineTo(x + k, b_)
    c.drawPath(p, M.paint(cor, q, stroke=6, cap_round=True))
    if rotulo:
        E.foco(c, t, t0 + 0.3, 0.4, lambda a: E.formula(c, rotulo, x + lado * 26, ym + size * 0.36, size, est, cor, a,
                                                        "right" if lado < 0 else "left"))


def particulas(c, t, x, y, w, h, agit, cor, a=1.0, n=(6, 4), r=17, borda=True):
    """caixa com partículas que tremem; agit = 0 (quase paradas) a 1 (muito agitadas)"""
    if a <= 0:
        return
    if borda:
        M.rrect(c, x, y, w, h, 26, E.mix(cor, "#FFFFFF", 0.86), a)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 26, 26), M.paint(cor, a, stroke=4))
    nc, nl = n
    c.save()
    c.clipRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x + 4, y + 4, w - 8, h - 8), 22, 22), True)
    amp = 3 + 26 * agit
    vel = 4 + 18 * agit
    for i in range(nc):
        for j in range(nl):
            k = i * 7 + j * 13
            px = x + w * (i + 0.5 + 0.25 * math.sin(k)) / nc + amp * math.sin(t * vel + k * 1.7)
            py = y + h * (j + 0.5 + 0.2 * math.cos(k * 1.3)) / nl + amp * math.cos(t * vel * 1.13 + k * 2.3)
            E.bola(c, px, py, r, cor, a)
    c.restore()


def seta_calor(c, t, t0, A, B, rotulo="calor", cor=None, d=0.7, size=50, a=1.0, ondas=3.0, amp=16, lado=-1, escuro=False):
    """seta ondulada de A até B (o calor passando); rótulo acima (lado=-1) ou abaixo (lado=1)"""
    if t < t0 or a <= 0:
        return
    cor = cor or E.COR
    p = ease_io(prog(t, t0, d))
    L = math.dist(A, B)
    ux, uy = (B[0] - A[0]) / L, (B[1] - A[1]) / L
    nx, ny = -uy, ux
    corpo = L - 34
    pts = []
    for i in range(61):
        s = corpo * p * i / 60
        o = amp * math.sin(2 * math.pi * ondas * s / corpo - t * 6)
        pts.append((A[0] + ux * s + nx * o, A[1] + uy * s + ny * o))
    F.poli(c, pts, 1.0, cor, a, 8)
    if p > 0.05:
        tip = (A[0] + ux * (corpo * p + 34), A[1] + uy * (corpo * p + 34))
        F._cabeca(c, tip[0], tip[1], ux, uy, 40, cor, a)
    if rotulo:
        mx, my = (A[0] + B[0]) / 2, (A[1] + B[1]) / 2
        yl = my - amp - 30 if lado < 0 else my + amp + 30 + size * 0.7
        E.foco(c, t, t0 + d * 0.6, 0.4, lambda q: E.formula(c, rotulo, mx, yl, size, "g", cor if not escuro else BR, q * a, "center"))


def xicara(c, x, y, s, a=1.0, t=0.0, vapor=True):
    """xícara de café com a base em (x, y); s = largura da boca"""
    if a <= 0:
        return
    w, h = s, s * 0.8
    p = skia.Path()
    p.moveTo(x - w / 2, y - h); p.lineTo(x + w / 2, y - h)
    p.cubicTo(x + w / 2, y - h * 0.2, x + w * 0.3, y, x, y)
    p.cubicTo(x - w * 0.3, y, x - w / 2, y - h * 0.2, x - w / 2, y - h)
    p.close()
    c.drawPath(p, M.paint("#FFFFFF", a))
    c.drawPath(p, M.paint(TINTA, a, stroke=6))
    c.drawOval(skia.Rect.MakeLTRB(x - w / 2 + 8, y - h - 14, x + w / 2 - 8, y - h + 14), M.paint("#6B3A1E", a))
    c.drawArc(skia.Rect.MakeXYWH(x + w * 0.38, y - h * 0.85, w * 0.3, h * 0.45), -80, 200, False, M.paint(TINTA, a, stroke=10))
    if vapor:
        for k in range(3):
            xx = x - w * 0.22 + k * w * 0.22
            pts = [(xx + 12 * math.sin(t * 3 + k + i * 0.5), y - h - 40 - i * 9) for i in range(14)]
            F.poli(c, pts, 1.0, E.COR, a * 0.75, 6)


def copo(c, x, y, w, h, a=1.0, gelo=True):
    """copo de água gelada com a base em (x, y)"""
    if a <= 0:
        return
    M.rrect(c, x - w / 2 + 6, y - h * 0.75, w - 12, h * 0.75 - 6, 10, AGUA, a * 0.55)
    if gelo:
        for dx, dy, g in ((-0.18, 0.62, 8), (0.12, 0.58, -12), (-0.02, 0.45, 20)):
            c.save(); c.translate(x + dx * w, y - dy * h); c.rotate(g)
            M.rrect(c, -w * 0.15, -w * 0.15, w * 0.3, w * 0.3, 8, GELO, a)
            c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(-w * 0.15, -w * 0.15, w * 0.3, w * 0.3), 8, 8), M.paint(FRIO, a, stroke=3))
            c.restore()
    p = skia.Path()
    p.moveTo(x - w / 2, y - h); p.lineTo(x - w / 2 + 8, y); p.lineTo(x + w / 2 - 8, y); p.lineTo(x + w / 2, y - h)
    c.drawPath(p, M.paint(TINTA, a, stroke=6))


def mao(c, x, y, s, a=1.0):
    """mão aberta de lado, com a palma virada para a esquerda; (x, y) = meio da palma"""
    if a <= 0:
        return
    pele, borda = "#E9B48C", "#9A6040"
    M.rrect(c, x - s * 0.35, y - s * 0.55, s * 0.7, s * 1.1, s * 0.3, pele, a)
    for k in range(4):
        yy = y - s * 0.5 + k * s * 0.27
        M.rrect(c, x - s * 0.95, yy, s * 0.75, s * 0.22, s * 0.11, pele, a)
    M.rrect(c, x - s * 0.1, y + s * 0.4, s * 0.5, s * 0.7, s * 0.2, pele, a)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x - s * 0.35, y - s * 0.55, s * 0.7, s * 1.1), s * 0.3, s * 0.3), M.paint(borda, a * 0.6, stroke=3))


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
        E.foco(c, t, C[k] + 0.6, 0.5, lambda a, i=i, y=y: desenhos[i](a, x + w - 190, y + 115))
    q1 = ease_io(prog(t, C[itens[1][0]] - 0.35, 0.5))
    E.cursor(c, x + w - 30, lerp(430, 720, q1), ep(t, C[itens[0][0]], 0.4))
    E.frase(c, t, lerp(C[itens[1][0]], C[cena + ".end"], 0.6), ps("faltou alguma?", "i", 56, COR) + ps("procure no canal", "i", 56), 820, 920, "left", 0.12)


def passos(c, t, linhas, x, y0, dy=125, size=80):
    """contas empilhadas: linhas = [(t0, fórmula, cor)]"""
    for i, (ti, s, cor) in enumerate(linhas):
        formula_em(c, t, ti, s, x, y0 + i * dy, size, cor=cor)


def troca(c, t, itens, fn):
    """um de cada vez: itens = [(instante, arg)], cada um sai quando o próximo chega; fn(arg, a) desenha"""
    for i, (ti, s) in enumerate(itens):
        fim = itens[i + 1][0] - 0.1 if i + 1 < len(itens) else 1e9
        if t >= ti - 0.01:
            E.saida(c, t, fim, lambda s=s, ti=ti: E.foco(c, t, ti, 0.45, lambda a: fn(s, a)), d=0.25)


def promessa(c, t, C, cena, itens, y0=470, dy=180):
    """tela "até o fim da aula": símbolo da Física à direita e itens numerados [(cue, texto, cor)]"""
    tb = C[cena + ".a"] + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1480, 540, 330 * ease_back(prog(t, tb, 0.8)), giro=12 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, C[cena + ".a"], ps("até o fim da aula", "i", 88), XE, 280, passo=0.14)
    for i, (k, s, cor) in enumerate(itens):
        y = y0 + i * dy
        E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, XE + 40, y - 30, 38, a=a), centro(c, str(i + 1), XE + 40, y - 8, 48, "g", BR, a)))
        E.frase(c, t, C[k] + 0.1, [(s, "g", 80, cor)], XE + 110, y)


def resumo(c, t, C, cena, itens, y0=380, dy=200):
    """tela "resumindo": itens = [(cue, partes de E.frase)]"""
    E.frase(c, t, C[cena], [("resumindo", "i", 92, COR)], W / 2, 180, "center")
    for i, (k, partes) in enumerate(itens):
        y = y0 + i * dy
        E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 230, y - 26, 52, a=a), centro(c, str(i + 1), 230, y - 4, 60, "g", BR, a)))
        E.frase(c, t, C[k] + 0.1, partes, 330, y, passo=0.1)


def inscreva(c, t, C, cena, k_insc, k_bons):
    E.foco(c, t, C[k_insc], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 420, 76, estilo="g", a=a))
    p = ease_io(prog(t, C[k_insc] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(720, 445, p), ep(t, C[k_insc] + 0.2, 0.4))
    E.frase(c, t, C[k_bons], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1570, 990, "center")


def sol(c, cx, cy, r, a=1.0, t=0.0):
    """sol: esfera amarela com raios girando"""
    if a <= 0:
        return
    for k in range(10):
        g = math.radians(36 * k + t * 20)
        M.line(c, cx + math.cos(g) * r * 1.3, cy + math.sin(g) * r * 1.3, cx + math.cos(g) * r * 1.65, cy + math.sin(g) * r * 1.65, "#F5A623", a, max(4, r * 0.12))
    E.bola(c, cx, cy, r, "#FFC21A", a)


# ---------------- peças desta aula ----------------
def praia(c, t, t0, x, y, w, h, sol_=True):
    """areia à esquerda, mar à direita, sol em cima"""
    q = ep(t, t0, 0.6)
    if q <= 0:
        return
    M.rrect(c, x, y, w * 0.5 + 20, h, 24, AREIA, q)
    M.rrect(c, x + w * 0.5, y, w * 0.5, h, 24, AGUA, 0.75 * q)
    for k in range(3):
        yy = y + 30 + k * 40
        pts = [(x + w * 0.55 + i * 12, yy + 6 * math.sin(i * 0.6 + t * 2)) for i in range(int(w * 0.4 / 12))]
        F.poli(c, pts, 1.0, BR, 0.6 * q, 4)
    if sol_:
        sol(c, x + w * 0.5, y - 170, 60, q, t)


def faixa_temp(c, t, t0, x, ytop, ybot, nome, cor, a=1.0):
    """faixa vertical entre a temperatura da noite (embaixo) e a do dia (em cima)"""
    q = ep(t, t0, 0.6) * a
    if q <= 0:
        return
    yb, yt = ybot, lerp(ybot, ytop, ease_io(prog(t, t0, 1.0)))
    M.rrect(c, x - 50, yt, 100, yb - yt, 30, cor, 0.85 * q)
    E.foco(c, t, t0 + 0.4, 0.4, lambda a_: (E.escreve(c, "dia", x + 80, ytop + 20, 44, "i", TINTA2, a_),
                                            E.escreve(c, "noite", x + 80, ybot, 44, "i", TINTA2, a_)))
    E.foco(c, t, t0, 0.4, lambda a_: centro(c, nome, x, 950, 56, "g", TINTA, a_))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def um():
        praia(c, t, C["s01.a"], 760, 720, 1100, 200)
        E.frase(c, t, C["s01.a"], ps("meio-dia na praia", "i", 80), XE, 230, passo=0.12)
        term(c, t, C["s01.b"], 980, 690, 420, 55, 0, 60)
        E.foco(c, t, C["s01.b"] + 0.6, 0.4, lambda a: E.pilula(c, "areia: queima", 980, 220, 50, "g", fundo=E.COR, a=a))
        term(c, t, C["s01.c"], 1640, 690, 420, 24, 0, 60)
        E.foco(c, t, C["s01.c"] + 0.6, 0.4, lambda a: E.pilula(c, "mar: fresco", 1640, 220, 50, "g", fundo=FRIO, a=a))
        if t >= C["s01.d"]:
            for xx in (1010, 1580):
                seta_calor(c, t, C["s01.d"], (1310, 640), (xx, 560 if xx < 1300 else 560), None, d=0.6, amp=10, ondas=2)
        E.frase(c, t, C["s01.d"], ps("o mesmo sol", "i", 70) + ps("nas duas", "g", 66), XE, 380, passo=0.1)
        E.frase(c, t, C["s01.d"] + 1.6, ps("por que só", "i", 70) + [("a areia?", "g", 70, COR)], XE, 520, passo=0.1)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t >= C["s02"]:
        promessa(c, t, C, "s02", (("s02.a", "a areia e o mar", COR), ("s02.b", "quanto calor", TINTA)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    def calor(a, x, y):
        seta_calor(c, 1e9, 0, (x - 200, y + 20), (x + 60, y + 20), None, a=a, amp=10, ondas=2)
        E.formula(c, "ΔT", x + 90, y + 40, 60, "g", COR, a)

    def isola(a, x, y):
        E.formula(c, "v = f{d}{t} → d = v · t", x - 120, y + 30, 50, "g", TINTA, a, "center")
    lembrete2(c, t, C, "s03", (("s03.b", "calor e", "variação ΔT"), ("s03.c", "isolar uma", "letra")), (calor, isola))


# ---------------- caloria ----------------
def gota(c, cx, cy, r, a=1.0, rot="1 g"):
    if a <= 0:
        return
    p = skia.Path()
    p.moveTo(cx, cy - r * 1.6)
    p.cubicTo(cx + r * 0.6, cy - r * 0.8, cx + r, cy - r * 0.2, cx + r, cy + r * 0.2)
    p.cubicTo(cx + r, cy + r * 0.8, cx + r * 0.5, cy + r, cx, cy + r)
    p.cubicTo(cx - r * 0.5, cy + r, cx - r, cy + r * 0.8, cx - r, cy + r * 0.2)
    p.cubicTo(cx - r, cy - r * 0.2, cx - r * 0.6, cy - r * 0.8, cx, cy - r * 1.6)
    c.drawPath(p, M.paint(AGUA, a))
    F.medida(c, rot.split()[0], rot.split()[1], cx, cy + r * 0.35, r * 0.6, BR, a, "center", cor_u=BR)


def b_caloria(c, t, C, b):
    def s04():
        E.frase(c, t, C["s04"], ps("primeiro, a unidade", "i", 70, TINTA2), XE, 200, passo=0.1)
        E.frase(c, t, C["s04.a"], [("caloria", "g", 110, COR)], XE, 340)
        E.foco(c, t, C["s04.a"] + 0.4, 0.4, lambda a: E.pilula(c, "cal", XE + 640, 305, 64, "g", fundo=TINTA, a=a))
        E.foco(c, t, C["s04.b"], 0.5, lambda a: gota(c, XE + 120, 560, 90, a))
        E.foco(c, t, C["s04.b"] + 0.8, 0.4, lambda a: E.formula(c, "+1 °C", XE + 280, 590, 90, "g", COR, a))
        term(c, t, C["s04.b"] + 0.6, XE + 660, 700, 300, 21, 20, 22)
        E.frase(c, t, C["s04.b"] + 1.6, ps("1 cal: 1 g de água sobe 1 °C", "i", 54, TINTA2), XE, 820, passo=0.08)
        E.foco(c, t, C["s04.c"], 0.5, lambda a: E.formula(c, "1 kcal = 1.000 cal", 1200, 420, 76, "g", TINTA, a))

        def rotulo(a):
            x, y = 1250, 560
            M.rrect(c, x, y, 520, 300, 20, BR, a)
            c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, 520, 300), 20, 20), M.paint(TINTA, a, stroke=4))
            E.escreve(c, "INFORMAÇÃO NUTRICIONAL", x + 30, y + 60, 30, "b", TINTA, a)
            M.line(c, x + 30, y + 85, x + 490, y + 85, TINTA, a, 3)
            E.escreve(c, "valor energético", x + 30, y + 150, 40, "i", TINTA, a)
            F.medida(c, 250, "kcal", x + 30, y + 240, 70, E.COR, a)
        E.foco(c, t, C["s04.c"] + 0.6, 0.5, rotulo)
    E.saida(c, t, C["s05"] - 0.1, s04)
    if t < C["s05"]:
        return
    E.frase(c, t, C["s05.a"], ps("no Sistema Internacional:", "i", 70), XE, 300, passo=0.1)
    E.foco(c, t, C["s05.a"] + 1.0, 0.5, lambda a: E.escreve(c, "joule", XE, 480, 130, "g", TINTA, a))
    E.foco(c, t, C["s05.a"] + 1.4, 0.4, lambda a: E.pilula(c, "aula de energia", XE + 640, 440, 50, "b", fundo=TINTA2, a=a))
    E.frase(c, t, C["s05.b"], ps("a prova dá a conversão;", "i", 66) + ps("aqui:", "i", 66) + [("caloria", "g", 66, COR)], XE, 700, passo=0.1)


# ---------------- a fórmula ----------------
def panela(c, cx, y, w, a=1.0, cheia=True):
    if a <= 0:
        return
    h = w * 0.55
    M.rrect(c, cx - w / 2, y - h, w, h, 18, TINTA2, a)
    M.rrect(c, cx - w / 2 - 40, y - h + 10, 40, 16, 6, TINTA2, a)
    M.rrect(c, cx + w / 2, y - h + 10, 40, 16, 6, TINTA2, a)
    if cheia:
        M.rrect(c, cx - w / 2 + 10, y - h + 10, w - 20, 24, 8, AGUA, a)


def b_formula(c, t, C, b):
    def s06():
        E.frase(c, t, C["s06"], ps("quanto calor para esquentar?", "i", 70), XE, 200, passo=0.1)
        E.frase(c, t, C["s06.a"], ps("depende de", "i", 70) + [("3 coisas", "g", 70, COR)], XE, 320, passo=0.1)
        itens = (("s06.b", "massa", 1), ("s06.c", "quanto sobe", 2), ("s06.d", "material", 3))
        for i, (k, s, n) in enumerate(itens):
            x = 380 + i * 580
            E.foco(c, t, C[k], 0.5, lambda a, s=s, x=x, i=i: (E.bola(c, x - 150, 870, 40, a=a), centro(c, str(i + 1), x - 150, 888, 48, "g", BR, a),
                                                              E.escreve(c, s, x - 90, 890, 60, "g", TINTA, a)))
            if n == 1:
                E.foco(c, t, C[k] + 0.3, 0.5, lambda a, x=x: (panela(c, x - 40, 760, 300, a), xicara(c, x + 220, 760, 120, a, t, False)))
            elif n == 2:
                E.foco(c, t, C[k] + 0.3, 0.5, lambda a, x=x: E.formula(c, "ΔT", x + 20, 700, 160, "g", COR, a, "center"))
            else:
                E.foco(c, t, C[k] + 0.3, 0.5, lambda a, x=x: (M.rrect(c, x - 140, 540, 150, 200, 20, AREIA, a), M.rrect(c, x + 40, 540, 150, 200, 20, AGUA, a)))
    E.saida(c, t, C["s07"] - 0.1, s06)
    if C["s07"] <= t < C["s09"]:
        def s07_08():
            formula_em(c, t, C["s07.a"], "Q = m · c · ΔT", XE, 300, 130)
            F.formula_legenda(c, t, C["s07.a"], "", [("Q", "calor", "cal"), ("m", "massa", "g"), ("ΔT", "variação de temperatura", "°C"),
                                                     ("c", "calor específico", "f{cal}{g · °C}")],
                              XE, 300, size=130, tl=[C["s07.b"], C["s07.c"], C["s07.d"], C["s08.a"]], size_l=58, dy=92)
            E.foco(c, t, C["s08.b"], 0.4, lambda a: E.escreve(c, "por grama, por grau", XE + 470, 860, 46, "i", TINTA2, a))
            E.foco(c, t, C["s08.c"], 0.5, lambda a: (M.rrect(c, 1340, 380, 120, 120, 20, AGUA, a), E.formula(c, "c = 1", 1500, 465, 76, "g", TINTA, a)))
            E.foco(c, t, C["s08.d"], 0.5, lambda a: (M.rrect(c, 1340, 560, 120, 120, 20, AREIA, a), E.formula(c, "c = 0,2", 1500, 645, 76, "g", TINTA, a)))
            E.foco(c, t, C["s08.c"] + 0.3, 0.4, lambda a: E.escreve(c, "água", 1340, 360, 44, "i", TINTA2, a))
            E.foco(c, t, C["s08.d"] + 0.3, 0.4, lambda a: E.escreve(c, "areia", 1340, 540, 44, "i", TINTA2, a))
            E.foco(c, t, C["s08.e"], 0.5, lambda a: E.pilula(c, "calor sensível: muda a temperatura", 1500, 980, 44, "b", fundo=E.COR, a=a))
        E.saida(c, t, C["s09"] - 0.1, s07_08)
    if t < C["s09"]:
        return
    E.frase(c, t, C["s09"], ps("leia em voz alta", "i", 76), W / 2, 220, "center")
    for i, (letra, sil) in enumerate((("Q", "que"), ("m", "ma"), ("c", "ce"), ("ΔT", "te"))):
        x = 520 + i * 300 + (30 if i == 3 else 0)
        ti = C["s09.a"] + 0.45 * i
        E.foco(c, t, ti, 0.4, lambda a, letra=letra, x=x: E.formula(c, letra, x, 520, 170, "g", TINTA, a, "center"))
        E.foco(c, t, C["s09.b"] + 0.25 * i, 0.4, lambda a, sil=sil, x=x: centro(c, sil, x, 700, 110, "g", COR, a))
    for i, s in enumerate(("=", "·", "·")):
        E.foco(c, t, C["s09.a"] + 0.2 + 0.45 * i, 0.4, lambda a, i=i, s=s: centro(c, s, 670 + i * 300, 510, 110, "g", TINTA2, a))
    E.frase(c, t, C["s09.b"] + 1.2, [("que", "g", 100, COR), ("macete!", "g", 100, COR)], W / 2, 900, "center")


# ---------------- exemplo ----------------
def b_exemplo(c, t, C, b):
    def s10_11():
        E.frase(c, t, C["s10.a"], ps("meio litro de água:", "i", 70), XE, 220, passo=0.1)
        E.foco(c, t, C["s10.a"] + 0.6, 0.5, lambda a: F.medida(c, 500, "g", XE + 620, 220, 90, TINTA, a))
        E.foco(c, t, C["s10.b"], 0.5, lambda a: E.formula(c, "20 °C → 80 °C", XE, 340, 76, "g", COR, a))
        passos(c, t, [(C["s11.a"], "ΔT = 80 − 20 = 60", TINTA), (C["s11.b"], "Q = 500 · 1 · 60", TINTA)], XE, 540, 150, 84)
        bola_txt(c, t, C["s11.c"], "30.000 cal", 1440, 560, 190, 76)
        E.foco(c, t, C["s11.d"], 0.5, lambda a: E.formula(c, "= 30 kcal", 1440, 860, 80, "g", TINTA, a, "center"))
        E.foco(c, t, C["s10.a"], 0.5, lambda a: panela(c, 1500, 330, 320, a))
    E.saida(c, t, C["s12"] - 0.1, s10_11)
    if t < C["s12"]:
        return
    E.frase(c, t, C["s12"], ps("e se esfriasse?", "i", 76), XE, 220, passo=0.1)
    E.foco(c, t, C["s12"] + 0.8, 0.5, lambda a: E.formula(c, "80 °C → 20 °C", XE, 340, 76, "g", FRIO, a))
    formula_em(c, t, C["s12.a"], "ΔT = 20 − 80 = −60", XE, 520, 84)
    formula_em(c, t, C["s12.b"], "Q = −30.000 cal", XE, 680, 84)
    E.foco(c, t, C["s12.c"], 0.5, lambda a: E.pilula(c, "Q < 0: cedeu calor", 1400, 520, 60, "g", fundo=FRIO, a=a))
    E.foco(c, t, C["s12.d"], 0.5, lambda a: E.pilula(c, "Q > 0: recebeu calor", 1400, 700, 60, "g", fundo=E.COR, a=a))


# ---------------- praia ----------------
def b_praia(c, t, C, b):
    def s13_14():
        E.frase(c, t, C["s13"] + 0.4, ps("a praia, em números", "i", 70), XE, 190, passo=0.1)
        formula_em(c, t, C["s13.c"], "ΔT = f{Q}{m · c}", 1560, 220, 90, align="center")
        for i, (nome, cor, mc, dt, tk) in enumerate((("água", AGUA, "1.000 · 1 = 1.000", "1.000 ÷ 1.000 = 1 °C", C["s14.a"]),
                                                     ("areia", AREIA, "1.000 · 0,2 = 200", "1.000 ÷ 200 = 5 °C", C["s14.b"]))):
            x = XE + i * 820
            E.foco(c, t, C["s13.a"] + 0.4 * i, 0.5, lambda a, x=x, cor=cor, nome=nome: (M.rrect(c, x, 330, 180, 180, 24, cor, a),
                                                                                          E.escreve(c, nome, x + 210, 400, 64, "g", TINTA, a),
                                                                                          F.medida(c, "1.000", "g", x + 210, 480, 56, TINTA2, a)))
            E.foco(c, t, C["s13.b"] + 0.3 * i, 0.4, lambda a, x=x: F.medida(c, "1.000", "cal", x, 620, 64, COR, a))
            formula_em(c, t, tk, "m · c = " + mc, x, 760, 60, cor=TINTA2)
            formula_em(c, t, tk + 1.2, "ΔT = " + dt, x, 880, 60)
        if t >= C["s14.c"]:
            E.foco(c, t, C["s14.c"], 0.5, lambda a: E.pilula(c, "mesmo calor: a areia esquenta 5 vezes mais", W / 2, 1000, 50, "g", fundo=E.COR, a=a))
    E.saida(c, t, C["s15"] - 0.1, s13_14)
    if t < C["s15"]:
        return
    E.frase(c, t, C["s15.a"], ps("a água esquenta", "i", 66) + [("devagar", "g", 62, FRIO)] + ps("e esfria", "i", 66) + [("devagar", "g", 62, FRIO)],
            XE, 220, passo=0.1)
    faixa_temp(c, t, C["s15.b"], 700, 480, 680, "litoral", AGUA)
    faixa_temp(c, t, C["s15.c"], 1300, 330, 860, "deserto", AREIA)
    E.foco(c, t, C["s15.b"] + 0.8, 0.4, lambda a: E.escreve(c, "pouca diferença", 520, 780, 44, "i", TINTA2, a))
    E.foco(c, t, C["s15.c"] + 0.8, 0.4, lambda a: E.escreve(c, "diferença enorme", 1420, 640, 44, "i", ERRADO, a))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s16"], [("cuidado", "g", 96, ERRADO)], XE, 200)
    E.frase(c, t, C["s16.a"], ps("com as unidades", "i", 76), XE + 450, 200, passo=0.1)
    E.foco(c, t, C["s16.b"], 0.5, lambda a: E.formula(c, "c em f{cal}{g · °C}  →  m em g", XE, 380, 76, "g", TINTA, a))
    formula_em(c, t, C["s16.c"], "Q = 0,5 · 1 · 60", XE, 600, 84, cor=ERRADO)
    E.foco(c, t, C["s16.d"], 0.5, lambda a: F.medida(c, 30, "cal", XE + 750, 600, 84, ERRADO, a))
    if t >= C["s16.d"] + 0.8:
        E.risco(c, XE - 10, 620, XE + 1000, 540, t, C["s16.d"] + 0.8, largura=10)
    E.foco(c, t, C["s16.d"] + 0.6, 0.5, lambda a: (E.formula(c, "Q = 500 · 1 · 60", XE, 800, 84, "g", CERTO, a),
                                                   F.medida(c, "30.000", "cal", XE + 750, 800, 84, CERTO, a)))
    E.foco(c, t, C["s16.e"], 0.5, lambda a: E.pilula(c, "1.000 vezes menos", 1500, 960, 54, "g", fundo=ERRADO, a=a))


# ---------------- atalho (palco) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    E.frase(c, t, C["s17"], ps("agora, o atalho:", "i", 70, CLARO) + [("proporção", "g", 70, BR)], W / 2, 170, "center", 0.12)
    E.foco(c, t, C["s17.a"], 0.5, lambda a: E.formula(c, "Q = m · c · ΔT", W / 2, 360, 130, "g", BR, a, "center"))
    E.foco(c, t, C["s17.b"], 0.5, lambda a: (E.formula(c, "c ÷ 5", 600, 560, 90, "g", CLARO, a, "center"),
                                             E.escreve(c, "→", 820, 555, 90, "g", BR, a),
                                             E.formula(c, "ΔT × 5", 1100, 560, 90, "g", BR, a, "center")))
    E.foco(c, t, C["s17.b"] + 0.6, 0.4, lambda a: E.escreve(c, "mesmo Q e mesma m", 1380, 550, 44, "i", CLARO, a))
    E.foco(c, t, C["s17.c"], 0.5, lambda a: (E.formula(c, "m × 2", 600, 720, 90, "g", CLARO, a, "center"),
                                             E.escreve(c, "→", 820, 715, 90, "g", BR, a),
                                             E.formula(c, "Q × 2", 1100, 720, 90, "g", BR, a, "center")))
    E.frase(c, t, C["s17.d"], ps("é tudo", "i", 64, CLARO) + [("multiplicação", "g", 60, BR)], W / 2, 860, "center", 0.1)
    E.frase(c, t, C["s17.e"], [("não", "g", 56, ERRADO), ("compensa:", "i", 60, CLARO)] + ps("valor exato", "i", 60, CLARO) + [("→", "g", 56, CLARO)] + ps("faça a conta", "i", 60, CLARO),
            W / 2, 980, "center", 0.1)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s18"], ps("hora de testar", "i", 72, COR), XE, 200)
    E.frase(c, t, C["s18.a"], ps("panela com", "i", 70), XE, 340, passo=0.1)
    E.foco(c, t, C["s18.a"] + 0.4, 0.5, lambda a: (F.medida(c, 400, "g", XE + 400, 340, 84, TINTA, a), E.escreve(c, "de água", XE + 680, 340, 70, "i", TINTA, a)))
    E.foco(c, t, C["s18.a"] + 1.4, 0.5, lambda a: F.medida(c, 25, "°C", XE, 460, 84, FRIO, a))
    E.frase(c, t, C["s18.b"], ps("recebe", "i", 70), XE, 600)
    E.foco(c, t, C["s18.b"] + 0.3, 0.5, lambda a: F.medida(c, "12.000", "cal", XE + 280, 600, 84, COR, a))
    E.frase(c, t, C["s18.c"], ps("temperatura", "i", 70) + [("final?", "g", 70, COR)], XE, 760, passo=0.1)
    if t < C["s19"]:
        E.foco(c, t, C["s18.a"], 0.5, lambda a: panela(c, 1460, 760, 420, a))
        seta_calor(c, t, C["s18.b"] + 0.3, (1460, 990), (1460, 800), None, amp=12, ondas=2)
        E.foco(c, t, C["s18.b"] + 0.8, 0.4, lambda a: E.escreve(c, "calor", 1510, 920, 50, "g", COR, a))
    else:
        E.relogio(c, t, C["s19.a"], cx=1460, cy=440, r=200)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    passos(c, t, [(C["s20.a"], "ΔT = f{Q}{m · c}", TINTA), (C["s20.b"], "m · c = 400 · 1 = 400", TINTA2),
                  (C["s20.b"] + 1.6, "ΔT = 12.000 ÷ 400 = 30", TINTA), (C["s20.e"], "T = 25 + 30", TINTA2)], XE, 260, 175, 84)
    E.foco(c, t, C["s20.d"], 0.5, lambda a: E.pilula(c, "30 °C é quanto subiu", 1450, 330, 54, "g", fundo=ERRADO, a=a))
    bola_txt(c, t, C["s20.f"], "55 °C", 1450, 650, 160, 90, CERTO)


# ---------------- fechamento ----------------
def cubo_gelo(c, cx, cy, s, a=1.0, derrete=0.0):
    if a <= 0:
        return
    h = s * (1 - 0.6 * derrete)
    M.rrect(c, cx - s / 2, cy - h, s, h, 18, GELO, a)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - s / 2, cy - h, s, h), 18, 18), M.paint(FRIO, a, stroke=4))
    if derrete > 0:
        c.drawOval(skia.Rect.MakeLTRB(cx - s * (0.6 + 0.4 * derrete), cy - 12, cx + s * (0.6 + 0.4 * derrete), cy + 18), M.paint(AGUA, a * 0.6))


def b_fim(c, t, C, b):
    def r():
        resumo(c, t, C, "s21", (("s21.a", [("que macete:", "i", 70), ("Q = m · c · ΔT", "g", 66, COR)]),
                                ("s21.b", [("c", "g", 66, COR), ("alto", "i", 70), ("(água):", "i", 70), ("esquenta", "i", 70), ("devagar", "g", 66)]),
                                ("s21.c", [("massa", "i", 70), ("em", "i", 70), ("gramas", "g", 66, COR)])))
    E.saida(c, t, C["s22"] - 0.1, r)
    if t < C["s22"]:
        return
    E.frase(c, t, C["s22"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C["s22.b"], [("Calor", "g", 130, COR)], XE, 410)
    E.frase(c, t, C["s22.b"] + 0.5, [("latente", "g", 130, COR)], XE, 550)
    E.foco(c, t, C["s22.a"], 0.5, lambda a: cubo_gelo(c, 520, 900, 200, a, ease_io(prog(t, C["s22.a"] + 0.5, 2.0))))
    term(c, t, C["s22.a"], 860, 940, 300, 0, -20, 40)
    E.foco(c, t, C["s22.a"] + 0.8, 0.4, lambda a: E.pilula(c, "parado em 0 °C", 860, 590, 44, "b", fundo=FRIO, a=a))
    inscreva(c, t, C, "s22", "s22.c", "s22.d")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, caloria=b_caloria, formula=b_formula, exemplo=b_exemplo, praia=b_praia,
              erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
