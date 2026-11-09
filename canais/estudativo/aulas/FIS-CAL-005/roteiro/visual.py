"""Visual — Estudativo · FIS-CAL-005: trocas de calor no calorímetro.
Segue a linguagem visual da trilha Calor e Termodinâmica (cabeçalho do visual.py da FIS-CAL-001: quente laranja, frio azul,
no equilíbrio os dois ganham a mesma cor; seta ondulada do calor; contas empilhadas e resultado na esfera).
Peças próprias: calorimetro (recipiente de parede dupla com tampa e termômetro), copo_agua (copo com água tingida de quente
ou frio e a massa e a temperatura escritas), reta das temperaturas (E.reta) mostrando onde a final cai entre as duas.
Todo instante vem de C[...] (marcadores do roteiro)."""
import math

import editorial as E
import fisica as F
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Física", "Calor e Termodinâmica")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_FIS-CAL-005_trocas_de_calor_calorimetro.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("calorimetro", "exemplo", "atalho", "diferentes", "erro", "questao", "fim"))
BR = "#FFFFFF"
FRIO = F.NEG
GELO = "#A9D8F5"
AGUA = "#5BA8E0"
MEIO = "#B07AA0"

# todas as contas da aula
def final(*corpos):
    """temperatura de equilíbrio por soma dos calores = 0: corpos = (m, c, T0)"""
    return sum(m * c * T for m, c, T in corpos) / sum(m * c for m, c, _ in corpos)


assert final((200, 1, 80), (300, 1, 20)) == 44 and 200 * 80 == 16000 and 300 * 20 == 6000 and 16000 + 6000 == 22000 and 22000 / 500 == 44
assert (80 + 20) / 2 == 50 != 44 and final((100, 1, 80), (100, 1, 20)) == 50
assert math.isclose(final((200, 0.1, 100), (180, 1, 20)), 28) and math.isclose(200 * 0.1, 20) and 20 * 100 == 2000 and 180 * 20 == 3600
assert 2000 + 3600 == 5600 and 5600 / 200 == 28 and 1 / 0.1 == 10
assert math.isclose((200 * 80 + 300 * 20) / 500, 44)          # média ponderada só com as massas, mesma substância
assert not math.isclose((200 * 100 + 180 * 20) / 380, 28)     # com substâncias diferentes, ela erra (≈ 62)
assert final((300, 1, 90), (100, 1, 10)) == 70 and 300 * 90 == 27000 and 27000 + 1000 == 28000 and 28000 / 400 == 70
assert 6 * 2 + 8 * 3 == 36 and 36 / 5 == 7.2


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
def copo_agua(c, cx, yb, w, h, cor, a=1.0, nivel=0.7, rot=None):
    """copo com água tingida (laranja = quente, azul = fria); rot = (massa, temperatura) escritos embaixo"""
    if a <= 0:
        return
    M.rrect(c, cx - w / 2 + 8, yb - h * nivel, w - 16, h * nivel - 6, 12, cor, 0.55 * a)
    p = skia.Path()
    p.moveTo(cx - w / 2, yb - h); p.lineTo(cx - w / 2 + 10, yb); p.lineTo(cx + w / 2 - 10, yb); p.lineTo(cx + w / 2, yb - h)
    c.drawPath(p, M.paint(TINTA, a, stroke=6))
    if rot:
        F.medida(c, rot[0], "g", cx, yb + 70, 54, TINTA, a, "center")
        F.medida(c, rot[1], "°C", cx, yb + 140, 54, cor, a, "center")


def calorimetro(c, cx, yb, w, h, a=1.0):
    """recipiente isolado: parede dupla, tampa e termômetro atravessando a tampa"""
    if a <= 0:
        return
    M.rrect(c, cx - w / 2 - 30, yb - h - 10, w + 60, h + 40, 40, "#D9D9D2", a)
    M.rrect(c, cx - w / 2, yb - h + 20, w, h - 10, 26, "#F7F7F3", a)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2 - 30, yb - h - 10, w + 60, h + 40), 40, 40), M.paint(TINTA, a, stroke=6))
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2, yb - h + 20, w, h - 10), 26, 26), M.paint(TINTA2, a, stroke=4, ))
    M.rrect(c, cx - w / 2 - 50, yb - h - 50, w + 100, 50, 14, TINTA2, a)


def bloqueio(c, x, y, a=1.0):
    """seta curta barrada: o calor não passa"""
    if a <= 0:
        return
    F.seta(c, x - 60, y, x + 40, y, ERRADO, a, 7)
    M.line(c, x - 30, y - 34, x + 10, y + 34, ERRADO, a, 7)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def um():
        E.foco(c, t, C["s01.a"], 0.5, lambda a: copo_agua(c, 1000, 640, 220, 300, E.COR, a, rot=(200, 80)))
        E.foco(c, t, C["s01.b"], 0.5, lambda a: copo_agua(c, 1300, 640, 260, 300, FRIO, a, rot=(300, 20)))
        E.foco(c, t, C["s01.b"] + 0.8, 0.5, lambda a: (E.escreve(c, "+", 1140, 520, 90, "g", TINTA2, a), E.escreve(c, "=", 1470, 520, 90, "g", TINTA2, a)))
        E.foco(c, t, C["s01.b"] + 1.0, 0.5, lambda a: copo_agua(c, 1680, 640, 300, 360, MEIO, a, 0.8))
        E.frase(c, t, C["s01.a"], ps("misturando", "i", 76), XE, 230)
        E.frase(c, t, C["s01.c"], ps("a média:", "i", 70), XE, 400)
        E.foco(c, t, C["s01.c"] + 0.5, 0.5, lambda a: F.medida(c, 50, "°C", XE + 300, 400, 100, ERRADO, a))
        if t >= C["s01.d"]:
            E.risco(c, XE + 280, 420, XE + 560, 330, t, C["s01.d"], largura=10)
        E.frase(c, t, C["s01.e"], ps("fica em", "i", 70), XE, 580)
        E.foco(c, t, C["s01.e"] + 0.3, 0.5, lambda a: F.medida(c, 44, "°C", XE + 320, 580, 120, CERTO, a))
        E.foco(c, t, C["s01.e"] + 0.5, 0.5, lambda a: F.medida(c, "44", "°C", 1680, 860, 64, MEIO, a, "center"))
    E.saida(c, t, C["s02"] - 0.1, um)
    if t >= C["s02"]:
        promessa(c, t, C, "s02", (("s02.a", "temperatura final", COR), ("s02.b", "o atalho de cabeça", TINTA)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    def calor(a, x, y):
        E.formula(c, "Q = m · c · ΔT", x - 80, y + 4, 50, "g", TINTA, a, "center")
        E.formula(c, "cede: Q < 0", x - 80, y + 70, 44, "g", FRIO, a, "center")

    def media(a, x, y):
        E.formula(c, "f{6 · 2 + 8 · 3}{5} = 7,2", x - 90, y + 30, 50, "g", TINTA, a, "center")
    lembrete2(c, t, C, "s03", (("s03.b", "calor e o", "sinal do Q"), ("s03.c", "a média", "ponderada")), (calor, media))


# ---------------- calorímetro ----------------
def b_calorimetro(c, t, C, b):
    def s04():
        E.frase(c, t, C["s04.a"], [("calorímetro", "g", 96, COR)], XE, 230)
        E.frase(c, t, C["s04.a"] + 0.8, ps("recipiente isolado,", "i", 60) + ps("como uma garrafa térmica", "i", 60, TINTA2), XE, 330, passo=0.08)
        E.foco(c, t, C["s04.a"] + 0.3, 0.6, lambda a: calorimetro(c, 1300, 900, 760, 460, a))
        q = ease_io(prog(t, C["s04.e"] - 0.8, 2.0))
        cq, cf = E.mix(E.COR, MEIO, q), E.mix(FRIO, MEIO, q)
        E.foco(c, t, C["s04.c"], 0.5, lambda a: F.bloco(c, 1150, 760, 260, 200, None, cq, a))
        E.foco(c, t, C["s04.d"], 0.5, lambda a: F.bloco(c, 1450, 760, 260, 200, None, cf, a))
        seta_calor(c, t, C["s04.d"] + 0.3, (1100, 560), (1500, 560), "calor", a=1 - q, size=46, amp=12, ondas=2)
        E.foco(c, t, C["s04.b"], 0.4, lambda a: (bloqueio(c, 870, 700, a), bloqueio(c, 1770, 700, a)))
        E.frase(c, t, C["s04.b"], ps("o calor não entra", "i", 56) + ps("nem sai", "g", 54), XE, 470, passo=0.08)
        E.frase(c, t, C["s04.c"], [("quente", "g", 56, COR)] + ps("cede", "i", 60), XE, 600, passo=0.1)
        E.frase(c, t, C["s04.d"], [("frio", "g", 56, FRIO)] + ps("recebe", "i", 60), XE, 700, passo=0.1)
        E.foco(c, t, C["s04.e"], 0.5, lambda a: E.pilula(c, "equilíbrio térmico", XE + 290, 860, 60, "g", fundo=MEIO, a=a))
    E.saida(c, t, C["s05"] - 0.1, s04)
    if t < C["s05"]:
        return
    E.frase(c, t, C["s05.a"], ps("tudo o que o quente cede, o frio recebe", "i", 64), W / 2, 220, "center", 0.08)
    E.foco(c, t, C["s05.a"] + 1.6, 0.5, lambda a: (E.formula(c, "Q quente", 620, 480, 90, "g", COR, a, "center"),
                                                   E.formula(c, "−600 cal", 620, 600, 76, "b", TINTA2, a, "center")))
    E.foco(c, t, C["s05.a"] + 2.2, 0.5, lambda a: (E.escreve(c, "+", 935, 485, 90, "g", TINTA2, a),
                                                   E.formula(c, "Q frio", 1250, 480, 90, "g", FRIO, a, "center"),
                                                   E.formula(c, "+600 cal", 1250, 600, 76, "b", TINTA2, a, "center")))
    E.foco(c, t, C["s05.b"], 0.5, lambda a: (E.escreve(c, "=", 1500, 485, 90, "g", TINTA2, a), E.escreve(c, "0", 1600, 485, 110, "g", TINTA, a)))
    E.foco(c, t, C["s05.b"] + 0.3, 0.4, lambda a: E.escreve(c, "(exemplo)", 1180, 680, 40, "i", TINTA2, a))
    E.foco(c, t, C["s05.c"], 0.5, lambda a: E.pilula(c, "soma dos calores = 0", W / 2, 860, 76, "g", fundo=E.COR, a=a))


# ---------------- exemplo ----------------
def b_exemplo(c, t, C, b):
    def s06_07():
        E.frase(c, t, C["s06"] + 0.3, ps("temperatura final:", "i", 66) + [("T", "g", 66, COR)], XE, 200, passo=0.1)
        formula_em(c, t, C["s06.b"], "200 · 1 · (T − 80)", XE, 360, 76, cor=COR)
        formula_em(c, t, C["s06.c"], "+ 300 · 1 · (T − 20)", XE + 760, 360, 76, cor=FRIO)
        formula_em(c, t, C["s06.d"], "= 0", XE + 1580, 360, 76)
        E.foco(c, t, C["s06.b"] + 0.4, 0.4, lambda a: E.escreve(c, "água quente", XE, 440, 40, "i", TINTA2, a))
        E.foco(c, t, C["s06.c"] + 0.4, 0.4, lambda a: E.escreve(c, "água fria", XE + 800, 440, 40, "i", TINTA2, a))
        passos(c, t, [(C["s07.a"], "200T − 16.000 + 300T − 6.000 = 0", TINTA), (C["s07.c"], "500T = 22.000", TINTA)], XE, 590, 150, 76)
        bola_txt(c, t, C["s07.d"], "44 °C", 1520, 800, 150, 84)
    E.saida(c, t, C["s08"] - 0.1, s06_07)
    if t < C["s08"]:
        return
    E.frase(c, t, C["s08"], ps("repare", "i", 76), XE, 220)
    vx = E.reta(c, t, C["s08.a"] - 0.3, 260, 1660, 560, 10, 90, [20, 44, 80], tm=[C["s08.a"], C["s08.a"] + 0.6, C["s08.a"]])
    for v, cor, tk in ((20, FRIO, C["s08.a"]), (80, E.COR, C["s08.a"]), (44, MEIO, C["s08.a"] + 0.6)):
        E.foco(c, t, tk, 0.4, lambda a, v=v, cor=cor: E.bola(c, vx(v), 560, 26, cor, a))
    E.frase(c, t, C["s08.a"] + 1.0, ps("fica entre as duas", "i", 60), 960, 400, "center", 0.1)
    if t >= C["s08.b"]:
        E.chave(c, vx(20), vx(44), 640, MEIO, ep(t, C["s08.b"], 0.5), 30, 6)
        E.chave(c, vx(44), vx(80), 640, TINTA2, ep(t, C["s08.b"] + 0.4, 0.5), 30, 6)
    E.frase(c, t, C["s08.b"], ps("mais perto do", "i", 64) + [("20", "g", 64, FRIO)], 960, 790, "center", 0.1)
    E.frase(c, t, C["s08.c"], [("300 g", "g", 60, FRIO)] + ps("de fria contra", "i", 64) + [("200 g", "g", 60, COR)] + ps("de quente", "i", 64),
            960, 900, "center", 0.1)


# ---------------- atalho (palco) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def s09_10():
        E.frase(c, t, C["s09"], ps("agora, o atalho", "i", 70, CLARO), W / 2, 160, "center")
        E.frase(c, t, C["s09.a"], [("mesma substância:", "g", 64, BR)], W / 2, 280, "center")
        E.frase(c, t, C["s09.b"], [("média ponderada", "g", 64, CLARO)] + ps("com as massas", "i", 64, CLARO), W / 2, 380, "center", 0.1)
        E.foco(c, t, C["s10.a"], 0.5, lambda a: E.formula(c, "T = f{200 · 80 + 300 · 20}{200 + 300}", 600, 640, 96, "g", BR, a, "center"))
        passos_ = [(C["s10.a"] + 0.3, "200 · 80 = 16.000"), (C["s10.b"], "300 · 20 = 6.000"), (C["s10.c"], "soma: 22.000"), (C["s10.d"], "÷ 500")]
        for i, (ti, s) in enumerate(passos_):
            E.foco(c, t, ti, 0.4, lambda a, s=s, i=i: E.formula(c, s, 1180, 540 + i * 90, 60, "b", CLARO, a))
        E.foco(c, t, C["s10.e"], 0.5, lambda a: (E.bola(c, 1640, 900, 110, a=a), F.medida(c, 44, "°C", 1640, 925, 70, BR, a, "center", cor_u=BR)))
        E.frase(c, t, C["s10.e"] + 0.6, ps("sem equação", "i", 64, CLARO), 600, 920, "center")
    E.saida(c, t, C["s11"] - 0.1, s09_10)
    if t < C["s11"]:
        return
    E.frase(c, t, C["s11.a"], ps("funciona porque o", "i", 66, CLARO) + [("c", "g", 66, BR)] + ps("corta dos dois lados", "i", 66, CLARO), W / 2, 330, "center", 0.1)
    E.frase(c, t, C["s11.b"], [("não", "g", 64, ERRADO)] + ps("serve com substâncias diferentes", "i", 66, CLARO), W / 2, 560, "center", 0.1)
    E.frase(c, t, C["s11.b"] + 2.0, ps("aí, use a", "i", 66, CLARO) + [("soma = 0", "g", 66, BR)], W / 2, 720, "center", 0.1)


# ---------------- substâncias diferentes ----------------
def b_diferentes(c, t, C, b):
    def s12_13():
        E.frase(c, t, C["s12"], ps("substâncias diferentes", "i", 70), XE, 200, passo=0.1)
        E.foco(c, t, C["s12.a"], 0.5, lambda a: (F.bloco(c, 1250, 400, 220, 150, "metal", E.COR, a)))
        E.foco(c, t, C["s12.a"] + 0.4, 0.4, lambda a: E.formula(c, "200 g · 100 °C", 1400, 340, 50, "g", TINTA, a))
        E.foco(c, t, C["s12.b"], 0.4, lambda a: E.formula(c, "c = 0,1", 1400, 420, 50, "g", COR, a))
        E.foco(c, t, C["s12.c"], 0.5, lambda a: copo_agua(c, 1300, 900, 260, 260, FRIO, a))
        E.foco(c, t, C["s12.c"] + 0.4, 0.4, lambda a: E.formula(c, "180 g · 20 °C · c = 1", 1460, 780, 50, "g", FRIO, a))
        formula_em(c, t, C["s13.a"], "200 · 0,1 · (T − 100)", XE, 400, 66, cor=COR)
        formula_em(c, t, C["s13.b"], "+ 180 · 1 · (T − 20) = 0", XE, 510, 66, cor=FRIO)
        formula_em(c, t, C["s13.c"], "20T − 2.000 + 180T − 3.600 = 0", XE, 680, 60)
    E.saida(c, t, C["s14"] - 0.1, s12_13)
    if t < C["s14"]:
        return
    passos(c, t, [(C["s14"], "20T − 2.000 + 180T − 3.600 = 0", TINTA2), (C["s14.a"], "200T = 5.600", TINTA)], XE, 260, 150, 72)
    bola_txt(c, t, C["s14.b"], "28 °C", 1450, 380, 150, 84)
    vx = E.reta(c, t, C["s14.b"] + 0.4, 260, 1660, 760, 0, 110, [20, 28, 100], tm=[C["s14.b"] + 0.4] * 3)
    for v, cor in ((20, FRIO), (100, E.COR), (28, MEIO)):
        E.foco(c, t, C["s14.b"] + 0.5, 0.4, lambda a, v=v, cor=cor: E.bola(c, vx(v), 760, 24, cor, a))
    E.frase(c, t, C["s14.c"], ps("o c da água é", "i", 64) + [("10 vezes maior", "g", 60, FRIO)], 960, 950, "center", 0.1)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    def s15():
        E.frase(c, t, C["s15"], [("cuidado", "g", 96, ERRADO)], XE, 210)
        E.frase(c, t, C["s15.a"], ps("a média simples", "i", 76), XE + 480, 210, passo=0.1)
        formula_em(c, t, C["s15.b"], "f{80 + 20}{2} = 50", XE, 450, 110, cor=ERRADO)
        if t >= C["s15.c"]:
            E.risco(c, XE - 10, 470, XE + 640, 360, t, C["s15.c"], largura=12)
        E.frase(c, t, C["s15.c"], ps("só vale com", "i", 64) + [("massas iguais", "g", 60, COR)] + ps("da mesma substância", "i", 64), XE, 680, passo=0.1)
        E.frase(c, t, C["s15.d"], [("300 g", "g", 60, FRIO)] + ps("de fria puxa para baixo", "i", 64), XE, 820, passo=0.1)
    E.saida(c, t, C["s16"] - 0.1, s15)
    if t < C["s16"]:
        return
    E.frase(c, t, C["s16.a"], ps("massas iguais, aí sim:", "i", 70), XE, 230, passo=0.1)
    E.foco(c, t, C["s16.a"] + 0.6, 0.5, lambda a: (copo_agua(c, 1250, 520, 200, 240, E.COR, a, rot=(100, 80)), copo_agua(c, 1550, 520, 200, 240, FRIO, a, rot=(100, 20))))
    formula_em(c, t, C["s16.b"], "f{100 · 80 + 100 · 20}{200} = 50", XE, 440, 76, cor=CERTO)
    E.frase(c, t, C["s16.c"], ps("pesos iguais:", "i", 60) + [("média simples", "g", 56)], XE, 640, passo=0.1)
    E.foco(c, t, C["s16.d"], 0.5, lambda a: E.pilula(c, "mesma substância: a ponderada nunca erra", W / 2, 900, 56, "g", fundo=E.COR, a=a))


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s17"], ps("hora de testar", "i", 72, COR), XE, 200)
    E.foco(c, t, C["s17.a"], 0.5, lambda a: E.formula(c, "300 g de água a 90 °C", XE, 360, 76, "g", COR, a))
    E.foco(c, t, C["s17.b"], 0.5, lambda a: E.formula(c, "+ 100 g de água a 10 °C", XE, 490, 76, "g", FRIO, a))
    E.frase(c, t, C["s17.c"], ps("temperatura", "i", 76) + [("final?", "g", 76, COR)], XE, 680, passo=0.1)
    if t < C["s18"]:
        E.foco(c, t, C["s17.a"], 0.5, lambda a: calorimetro(c, 1450, 860, 500, 380, a))
    else:
        E.relogio(c, t, C["s18.a"], cx=1460, cy=440, r=200)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    E.frase(c, t, C["s19.a"], ps("mesma substância:", "i", 64) + [("média ponderada", "g", 60, COR)], XE, 200, passo=0.1)
    passos(c, t, [(C["s19.b"], "300 · 90 = 27.000", TINTA), (C["s19.c"], "100 · 10 = 1.000", TINTA), (C["s19.d"], "27.000 + 1.000 = 28.000", TINTA),
                  (C["s19.e"], "28.000 ÷ 400", TINTA2)], XE, 340, 125, 72)
    bola_txt(c, t, C["s19.f"], "70 °C", 1480, 450, 150, 84, CERTO)
    vx = E.reta(c, t, C["s19.f"] + 0.5, 260, 1660, 900, 0, 100, [10, 70, 90], tm=[C["s19.f"] + 0.5] * 3)
    for v, cor in ((10, FRIO), (90, E.COR), (70, MEIO)):
        E.foco(c, t, C["s19.f"] + 0.6, 0.4, lambda a, v=v, cor=cor: E.bola(c, vx(v), 900, 24, cor, a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def r():
        resumo(c, t, C, "s20", (("s20.a", [("calorímetro:", "g", 64), ("soma dos calores", "i", 68), ("= 0", "g", 64, COR)]),
                                ("s20.b", [("mesma substância:", "g", 64), ("média ponderada", "i", 68, COR)]),
                                ("s20.c", [("T final", "g", 64), ("entre as duas,", "i", 68), ("perto de quem tem mais", "i", 68, TINTA2)])))
    E.saida(c, t, C["s21"] - 0.1, r)
    if t < C["s21"]:
        return
    E.frase(c, t, C["s21"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C["s21.a"], [("Trocas", "g", 120, COR), ("com", "i", 110), ("gelo", "g", 120, FRIO)], XE, 410)
    E.foco(c, t, C["s21.a"] + 0.4, 0.5, lambda a: copo(c, 560, 960, 260, 340, a))
    E.frase(c, t, C["s21.b"], ps("derrete todo", "i", 70) + [("ou não?", "g", 66, COR)], XE, 560, passo=0.1)
    inscreva(c, t, C, "s21", "s21.c", "s21.d")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, calorimetro=b_calorimetro, exemplo=b_exemplo, atalho=b_atalho,
              diferentes=b_diferentes, erro=b_erro, questao=b_questao, resposta=b_resposta, fim=b_fim)
