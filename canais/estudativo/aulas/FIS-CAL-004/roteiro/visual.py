"""Visual — Estudativo · FIS-CAL-004: calor latente e curva de aquecimento.
Segue a linguagem visual da trilha Calor e Termodinâmica (cabeçalho do visual.py da FIS-CAL-001: quente laranja, frio azul,
termômetro, partículas que tremem, seta ondulada do calor, fórmula com legenda, contas empilhadas e resultado na esfera).
CURVA DE AQUECIMENTO (padrão da trilha): F.grafico com T no eixo vertical; rampa = trecho inclinado (m·c·ΔT), patamar =
trecho horizontal (m·L), cada trecho desenhado no instante da sua etapa, com a conta escrita ao lado na cor da etapa.
Peças próprias: fogo (chamas), panela_fervendo, arrumacao (partículas presas numa grade que se soltam), gota de suor.
Todo instante vem de C[...] (marcadores do roteiro)."""
import math

import editorial as E
import fisica as F
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Física", "Calor e Termodinâmica")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_FIS-CAL-004_calor_latente_curva_aquecimento.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("patamar", "formula", "suor", "curva", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
FRIO = F.NEG
GELO = "#A9D8F5"
AGUA = "#5BA8E0"

# todas as contas da aula
Qs = lambda m, c, dT: m * c * dT
Ql = lambda m, L: m * L
e1, e2, e3 = Qs(100, 0.5, 20), Ql(100, 80), Qs(100, 1, 40)
assert (e1, e2, e3) == (1000, 8000, 4000) and e1 + e2 + e3 == 13000
e4, e5 = Qs(100, 1, 60), Ql(100, 540)
assert (e4, e5) == (6000, 54000) and e5 > e1 + e2 + e3 + e4
assert Qs(100, 1, 60) == 6000 and 6000 < 13000 / 2
assert 6 < 540 / 80 < 7
assert Ql(50, 80) == 4000 and Qs(50, 1, 20) == 1000 and 4000 + 1000 == 5000


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
def fogo(c, cx, y, s, a=1.0, t=0.0):
    """chamas com a base em (cx, y); s = altura"""
    if a <= 0:
        return
    for k, (dx, k_h, cor) in enumerate(((-0.45, 0.7, E.COR), (0.0, 1.0, E.COR), (0.45, 0.75, E.COR), (0.0, 0.55, "#FFC21A"))):
        h = s * k_h * (1 + 0.08 * math.sin(t * 9 + k * 2))
        w = s * 0.42
        x = cx + dx * s
        p = skia.Path()
        p.moveTo(x, y - h)
        p.cubicTo(x + w * 0.9, y - h * 0.45, x + w * 0.7, y, x, y)
        p.cubicTo(x - w * 0.7, y, x - w * 0.9, y - h * 0.45, x, y - h)
        c.drawPath(p, M.paint(cor, a * (0.9 if k < 3 else 1.0)))


def panela_fervendo(c, cx, y, w, a=1.0, t=0.0):
    """panela com água e bolhas; base em y"""
    if a <= 0:
        return
    h = w * 0.55
    M.rrect(c, cx - w / 2 + 8, y - h + 30, w - 16, h - 40, 14, AGUA, 0.5 * a)
    for k in range(7):
        ph = (t * 0.9 + k * 0.37) % 1
        bx = cx - w * 0.35 + (k * 0.11 % 0.7) * w
        c.drawCircle(bx, y - 20 - ph * (h - 60), 8 + 6 * ph, M.paint(BR, a * (1 - ph), stroke=3))
    p = skia.Path()
    p.moveTo(cx - w / 2, y - h); p.lineTo(cx - w / 2, y - 14); p.quadTo(cx - w / 2, y, cx - w / 2 + 14, y)
    p.lineTo(cx + w / 2 - 14, y); p.quadTo(cx + w / 2, y, cx + w / 2, y - 14); p.lineTo(cx + w / 2, y - h)
    c.drawPath(p, M.paint(TINTA2, a, stroke=10))
    for d in (-1, 1):
        M.rrect(c, cx + d * (w / 2 + 25) - 25, y - h + 20, 50, 16, 6, TINTA2, a)


def arrumacao(c, t, x, y, w, h, solta, cor, a=1.0):
    """partículas em grade (sólido) que se soltam e se espalham conforme `solta` vai de 0 a 1; a agitação é a mesma"""
    if a <= 0:
        return
    M.rrect(c, x, y, w, h, 26, E.mix(cor, BR, 0.86), a)
    nc, nl = 6, 4
    c.save()
    c.clipRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x + 4, y + 4, w - 8, h - 8), 22, 22), True)
    for i in range(nc):
        for j in range(nl):
            k = i * 7 + j * 13
            gx, gy = x + w * (i + 0.5) / nc, y + h * (j + 0.5) / nl
            lx = x + w * (0.1 + 0.8 * ((k * 0.618) % 1))
            ly = y + h * (0.1 + 0.8 * ((k * 0.377) % 1))
            px, py = lerp(gx, lx, solta) + 6 * math.sin(t * 9 + k), lerp(gy, ly, solta) + 6 * math.cos(t * 10 + k)
            E.bola(c, px, py, 17, cor, a)
    if solta < 0.3:
        for i in range(nc):
            for j in range(nl):
                gx, gy = x + w * (i + 0.5) / nc, y + h * (j + 0.5) / nl
                if i + 1 < nc:
                    M.line(c, gx + 18, gy, gx + w / nc - 18, gy, cor, a * (1 - solta / 0.3) * 0.5, 3)
                if j + 1 < nl:
                    M.line(c, gx, gy + 18, gx, gy + h / nl - 18, cor, a * (1 - solta / 0.3) * 0.5, 3)
    c.restore()


def curva_aq(c, t, P, trechos):
    """trechos = [(t0, (Q0, T0), (Q1, T1), cor)]: cada pedaço da curva cresce no seu instante"""
    for t0, (x0, y0), (x1, y1), cor in trechos:
        q = ease_io(prog(t, t0, 0.8))
        if q > 0:
            M.line(c, P.x(x0), P.y(y0), lerp(P.x(x0), P.x(x1), q), lerp(P.y(y0), P.y(y1), q), cor, 1.0, 9)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def um():
        E.frase(c, t, C["s01.a"], ps("água fervendo", "i", 80), XE, 230, passo=0.12)
        E.foco(c, t, C["s01.a"], 0.5, lambda a: panela_fervendo(c, 1250, 760, 520, a, t))
        s = lerp(110, 200, ease_io(prog(t, C["s01.b"], 0.8))) if t >= C["s01.b"] else 110
        E.foco(c, t, C["s01.a"] + 0.2, 0.5, lambda a: fogo(c, 1250, 900, s, a, t))
        term(c, t, C["s01.a"] + 0.4, 1700, 860, 560, 100, 0, 120)
        marca(c, t, C["s01.a"] + 1.2, 1700, y_term(100, 860, 560, 0, 120), 100, "°C", 48, COR)
        E.frase(c, t, C["s01.b"], ps("mais fogo:", "i", 70) + [("sobe?", "g", 70)], XE, 380, passo=0.1)
        E.frase(c, t, C["s01.c"], [("não", "g", 110, ERRADO)], XE, 540)
        E.frase(c, t, C["s01.d"], ps("fica em", "i", 66) + [("100 °C", "g", 66, COR)], XE, 680, passo=0.1)
        E.frase(c, t, C["s01.d"] + 0.8, ps("até a última gota", "i", 60, TINTA2), XE, 780, passo=0.1)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t >= C["s02"]:
        promessa(c, t, C, "s02", (("s02.b", "para onde vai o calor", COR), ("s02.c", "somar as etapas", TINTA)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    def formula(a, x, y):
        E.formula(c, "Q = m · c · ΔT", x - 60, y + 26, 56, "g", TINTA, a, "center")

    def curvinha(a, x, y):
        pts = [(x - 200, y + 70), (x - 130, y + 20), (x - 50, y + 20), (x + 20, y - 40), (x + 100, y - 40)]
        F.poli(c, pts, 1.0, E.COR, a, 7)
    lembrete2(c, t, C, "s03", (("s03.b", "o macete do", "que macete"), ("s03.c", "curva de", "aquecimento")), (formula, curvinha))


# ---------------- o patamar ----------------
def b_patamar(c, t, C, b):
    def s04():
        E.frase(c, t, C["s04"] + 0.3, ps("curva de aquecimento da água", "i", 66), XE, 190, passo=0.1)
        P = F.grafico(c, t, C["s04.a"] - 0.3, 360, 300, 1300, 600, 0, 10, -20, 120, "tempo", "T (°C)", passo=20, passo_y=20,
                      marcas_x=[], marcas_y=[0, 100], size=40)
        curva_aq(c, t, P, [(C["s04.a"], (0, -20), (1.2, 0), E.COR), (C["s04.b"], (1.2, 0), (3.6, 0), FRIO),
                           (C["s04.c"], (3.6, 0), (5.6, 100), E.COR), (C["s04.d"], (5.6, 100), (9.6, 100), FRIO)])
        E.foco(c, t, C["s04.b"] + 0.5, 0.4, lambda a: E.pilula(c, "patamar", P.x(2.4), P.y(0) - 60, 44, "g", fundo=FRIO, a=a))
        E.foco(c, t, C["s04.d"] + 0.5, 0.4, lambda a: E.pilula(c, "patamar", P.x(7.6), P.y(100) - 60, 44, "g", fundo=FRIO, a=a))
        E.frase(c, t, lerp(C["s04.d"], C["s05"], 0.4), ps("o fogo continua ligado:", "i", 56, TINTA2) + [("para onde vai o calor?", "g", 54, COR)],
                XE, 1000, passo=0.08)
    E.saida(c, t, C["s05"] - 0.1, s04)
    if t < C["s05"]:
        return
    E.frase(c, t, C["s05.a"], ps("vai para", "i", 76) + [("mudar o estado", "g", 76, COR)], XE, 220, passo=0.1)
    solta = ease_io(prog(t, C["s05.b"], 2.4))
    E.foco(c, t, C["s05.a"] + 0.6, 0.5, lambda a: arrumacao(c, t, XE, 340, 760, 480, solta, FRIO, a))
    E.foco(c, t, C["s05.a"] + 0.8, 0.4, lambda a: E.escreve(c, "gelo: presas" if solta < 0.5 else "água: soltas", XE, 890, 54, "g", FRIO, a))
    seta_calor(c, t, C["s05.b"] - 0.3, (1100, 600), (960, 600), "calor", size=46, amp=12, ondas=2)
    E.frase(c, t, C["s05.b"], ps("o calor", "i", 64) + [("separa", "g", 60)] + ps("as partículas", "i", 64), 1140, 450, passo=0.1)
    E.frase(c, t, C["s05.c"], ps("agitação igual:", "i", 60), 1140, 580, passo=0.1)
    E.frase(c, t, C["s05.c"] + 0.5, [("temperatura igual", "g", 60, COR)], 1140, 670)
    term(c, t, C["s05.c"] + 0.4, 1640, 1010, 260, 0, -20, 40)
    marca(c, t, C["s05.c"] + 1.0, 1640, y_term(0, 1010, 260, -20, 40), 0, "°C", 46)


# ---------------- a fórmula ----------------
def b_formula(c, t, C, b):
    def s06_07():
        E.frase(c, t, C["s06"] + 0.3, ps("muda o estado, não a temperatura:", "i", 60, TINTA2), XE, 190, passo=0.08)
        E.frase(c, t, C["s06.a"], [("calor", "g", 110, COR), ("latente", "g", 110, COR)], XE, 330, passo=0.15)
        E.frase(c, t, C["s06.b"], ps("latente = escondido:", "i", 56) + ps("o termômetro não mostra", "i", 56, TINTA2), XE, 430, passo=0.08)
        formula_em(c, t, C["s07.a"], "Q = m · L", XE, 640, 130)
        F.formula_legenda(c, t, C["s07.a"], "", [("Q", "calor", "cal"), ("m", "massa", "g"), ("L", "calor latente", "cal/g")],
                          XE, 640, size=130, tl=[C["s07.b"], C["s07.c"], C["s07.d"]], size_l=56)
        E.foco(c, t, C["s07.e"], 0.4, lambda a: E.escreve(c, "por grama, para mudar de estado", XE + 560, 1000, 46, "i", TINTA2, a))
        E.foco(c, t, C["s06.b"] + 0.3, 0.5, lambda a: E.formula(c, "?", 1500, 700, 300, "g", FIO, a, "center"))
    E.saida(c, t, C["s08"] - 0.1, s06_07)
    if t < C["s08"]:
        return
    E.frase(c, t, C["s08"], ps("na água", "i", 76), XE, 210)
    for i, (k, nome, val, cor) in enumerate((("s08.a", "derreter o gelo", "80", FRIO), ("s08.b", "ferver a água", "540", E.COR))):
        y = 380 + i * 200
        E.foco(c, t, C[k], 0.5, lambda a, nome=nome, y=y: E.escreve(c, nome, XE, y, 64, "i", TINTA, a))
        E.foco(c, t, C[k] + 0.4, 0.5, lambda a, val=val, y=y, cor=cor: F.medida(c, val, "cal/g", XE + 620, y, 100, cor, a))
    E.frase(c, t, C["s08.c"], ps("na volta (congelar, condensar):", "i", 60) + ps("o mesmo calor sai", "g", 56), XE, 820, passo=0.08)
    E.foco(c, t, C["s08.d"], 0.5, lambda a: E.pilula(c, "Q < 0", 1500, 930, 70, "g", fundo=FRIO, a=a))


# ---------------- o suor ----------------
def b_suor(c, t, C, b):
    E.frase(c, t, C["s09.a"], ps("por que o", "i", 76) + [("suor", "g", 80, COR)] + ps("resfria?", "i", 76), XE, 220, passo=0.1)
    E.foco(c, t, C["s09.a"] + 0.5, 0.5, lambda a: M.rrect(c, 900, 760, 900, 200, 40, "#E9B48C", a))
    E.foco(c, t, C["s09.a"] + 0.6, 0.4, lambda a: E.escreve(c, "pele", 940, 900, 50, "i", "#7A4A2A", a))
    sobe = ease_io(prog(t, C["s09.b"] + 0.4, 2.0))
    for k, dx in enumerate((-180, 60, 300)):
        x = 1350 + dx
        if t >= C["s09.a"] + 0.8:
            def gota_(a, x=x, k=k):
                y = lerp(730, 380 - 40 * k, sobe)
                r = 34 * (1 - 0.5 * sobe)
                c.drawCircle(x, y, r, M.paint(AGUA, a * (1 - 0.6 * sobe)))
            E.foco(c, t, C["s09.a"] + 0.8 + 0.15 * k, 0.4, gota_)
    E.frase(c, t, C["s09.b"], ps("para evaporar, precisa de", "i", 56) + [("calor latente", "g", 54, COR)], XE, 360, passo=0.08)
    if t >= C["s09.c"]:
        for dx in (-180, 60, 300):
            seta_calor(c, t, C["s09.c"], (1350 + dx, 800), (1350 + dx, 640), None, amp=8, ondas=1.5, d=0.6)
    E.frase(c, t, C["s09.c"], ps("e tira esse calor", "i", 56) + [("da pele", "g", 54)], XE, 470, passo=0.08)
    E.frase(c, t, C["s09.d"], ps("pele que perde calor", "i", 64) + [("esfria", "g", 64, FRIO)], XE, 640, passo=0.1)


# ---------------- curva completa ----------------
def b_curva(c, t, C, b):
    def s10_13():
        E.frase(c, t, C["s10"] + 0.3, ps("juntando tudo", "i", 60, TINTA2), XE, 180)
        E.foco(c, t, C["s10.a"], 0.5, lambda a: E.formula(c, "100 g de gelo a −20 °C", XE, 270, 60, "g", FRIO, a))
        E.foco(c, t, C["s10.b"], 0.5, lambda a: E.formula(c, "→ água a 40 °C", XE + 690, 270, 60, "g", COR, a))
        P = F.grafico(c, t, C["s10.c"], 1000, 380, 760, 520, 0, 14000, -20, 40, "Q (cal)", "T (°C)", passo=1000, passo_y=20,
                      marcas_x=[], marcas_y=[-20, 0, 20, 40], size=36)
        curva_aq(c, t, P, [(C["s11.a"], (0, -20), (1000, 0), FRIO), (C["s12.a"], (1000, 0), (9000, 0), GELO),
                           (C["s13.a"], (9000, 0), (13000, 40), E.COR)])
        etapas = ((C["s11.a"], C["s11.d"], "1  gelo: −20 → 0", "100 · 0,5 · 20 = 1.000", FRIO),
                  (C["s12.a"], C["s12.c"], "2  derrete em 0 °C", "100 · 80 = 8.000", "#2F7DB5"),
                  (C["s13.a"], C["s13.b"], "3  água: 0 → 40", "100 · 1 · 40 = 4.000", COR))
        for i, (ta, tc, l1, l2, cor) in enumerate(etapas):
            y = 400 + i * 170
            E.foco(c, t, ta, 0.4, lambda a, l1=l1, y=y, cor=cor: E.escreve(c, l1, XE, y, 52, "g", cor, a))
            formula_em(c, t, tc, l2, XE + 50, y + 75, 56, "b", TINTA)
        E.foco(c, t, C["s11.b"], 0.4, lambda a: E.pilula(c, "rampa: m · c · ΔT", 1320, 840, 44, "b", fundo=TINTA, a=a))
        E.foco(c, t, C["s11.c"], 0.4, lambda a: E.pilula(c, "c do gelo = 0,5", 1500, 340, 44, "g", fundo=FRIO, a=a))
        E.foco(c, t, C["s12.b"], 0.4, lambda a: E.pilula(c, "patamar: m · L", P.x(5000), P.y(0) - 60, 44, "b", fundo="#2F7DB5", a=a))
        formula_em(c, t, C["s13.c"], "1.000 + 8.000 + 4.000 =", XE, 1010, 60, "g", TINTA2)
        E.foco(c, t, C["s13.d"], 0.5, lambda a: F.medida(c, "13.000", "cal", XE + 720, 1010, 72, COR, a))
    E.saida(c, t, C["s14"] - 0.1, s10_13)
    if t < C["s14"]:
        return
    E.frase(c, t, C["s14"], ps("e até virar vapor?", "i", 70), XE, 200, passo=0.1)
    dados = [("gelo", 1000, FRIO), ("derrete", 8000, "#2F7DB5"), ("0 → 40", 4000, E.COR), ("40 → 100", 6000, E.COR), ("ferve", 54000, E.COR)]
    vis = 3 + (1 if t >= C["s14.a"] else 0) + (1 if t >= C["s14.b"] else 0)
    E.colunas(c, t, C["s14"] + 0.3, dados[:vis], 260, 330, 1200, 560, vmax=56000, destaque=(4,) if t >= C["s14.c"] else (0, 1, 2, 3, 4),
              fmt=lambda v: f"{v:,}".replace(",", "."), size=40)
    E.foco(c, t, C["s14.c"], 0.5, lambda a: E.pilula(c, "só a fervura > todo o resto", 1500, 230, 50, "g", fundo=E.COR, a=a))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s15"], [("cuidado", "g", 96, ERRADO)], XE, 210)
    E.frase(c, t, C["s15.a"], ps("uma conta só, de −20 a 40", "i", 70), XE, 360, passo=0.1)
    formula_em(c, t, C["s15.b"], "100 · 1 · 60 = 6.000 cal", XE, 540, 96, cor=ERRADO)
    if t >= C["s15.c"]:
        E.risco(c, XE - 10, 560, XE + 1180, 470, t, C["s15.c"], largura=12)
    E.frase(c, t, C["s15.c"], ps("faltou o", "i", 66) + [("patamar", "g", 62)] + ps("e o c do gelo é", "i", 66) + [("0,5", "g", 62)], XE, 720, passo=0.1)
    E.foco(c, t, C["s15.c"] + 2.0, 0.5, lambda a: (F.medida(c, "6.000", "", XE, 900, 90, ERRADO, a), E.escreve(c, "<  metade de", XE + 300, 900, 70, "i", TINTA, a),
                                                   F.medida(c, "13.000", "", XE + 780, 900, 90, CERTO, a)))


# ---------------- atalho (palco) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    E.frase(c, t, C["s16"], ps("agora, o atalho da curva", "i", 70, CLARO), W / 2, 160, "center", 0.1)
    x0, y0 = 300, 640
    trechos = [((x0, y0 + 140), (x0 + 200, y0), C["s16.a"]), ((x0 + 200, y0), (x0 + 500, y0), C["s16.b"]),
               ((x0 + 500, y0), (x0 + 700, y0 - 200), C["s16.a"] + 0.4), ((x0 + 700, y0 - 200), (x0 + 1300, y0 - 200), C["s16.b"] + 0.4)]
    for (A, B, tk) in trechos:
        q = ease_io(prog(t, tk, 0.6))
        if q > 0:
            M.line(c, *A, lerp(A[0], B[0], q), lerp(A[1], B[1], q), E.COR if A[1] != B[1] else CLARO, 1.0, 9)
    E.foco(c, t, C["s16.a"] + 0.3, 0.4, lambda a: (E.formula(c, "m · c · ΔT", x0 - 20, y0 + 50, 52, "g", E.COR, a, "right"),
                                                   E.formula(c, "m · c · ΔT", x0 + 560, y0 - 90, 52, "g", E.COR, a, "right")))
    E.foco(c, t, C["s16.b"] + 0.3, 0.4, lambda a: (E.formula(c, "m · L", x0 + 350, y0 + 70, 56, "g", BR, a, "center"),
                                                   E.formula(c, "m · L", x0 + 1000, y0 - 130, 56, "g", BR, a, "center")))
    E.frase(c, t, C["s16.c"], ps("uma conta por pedaço,", "i", 60, CLARO) + [("e some", "g", 60, BR)], W / 2, 330, "center", 0.1)
    E.foco(c, t, C["s16.d"], 0.5, lambda a: E.formula(c, "540 ≈ 7 · 80  →  fervura ≈ 7 × fusão", W / 2, 960, 64, "g", BR, a, "center"))


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s17"], ps("hora de testar", "i", 72, COR), XE, 200)
    E.foco(c, t, C["s17.a"], 0.5, lambda a: E.formula(c, "50 g de gelo a 0 °C", XE, 360, 76, "g", FRIO, a))
    E.foco(c, t, C["s17.b"], 0.5, lambda a: E.formula(c, "→ água a 20 °C", XE, 500, 76, "g", COR, a))
    E.frase(c, t, C["s17.c"], ps("quanto", "i", 76) + [("calor?", "g", 76, COR)], XE, 680, passo=0.1)
    E.foco(c, t, C["s17.c"] + 0.6, 0.4, lambda a: E.escreve(c, "L = 80 cal/g · c da água = 1", XE, 820, 46, "b", TINTA2, a))
    if t < C["s18"]:
        E.foco(c, t, C["s17.a"], 0.5, lambda a: (M.rrect(c, 1360, 420, 220, 220, 24, GELO, a),
                                                 c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(1360, 420, 220, 220), 24, 24), M.paint(FRIO, a, stroke=5))))
    else:
        E.relogio(c, t, C["s18.a"], cx=1460, cy=440, r=200)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    E.frase(c, t, C["s19"] + 0.4, ps("já em 0 °C: começa no patamar", "i", 60, TINTA2), XE, 220, passo=0.1)
    passos(c, t, [(C["s19.a"], "derreter: 50 · 80 = 4.000", TINTA), (C["s19.b"], "esquentar: 50 · 1 · 20 = 1.000", TINTA)], XE, 420, 170, 76)
    formula_em(c, t, C["s19.c"], "4.000 + 1.000 =", XE, 780, 76, "g", TINTA2)
    bola_txt(c, t, C["s19.c"] + 0.4, "5.000 cal", 1440, 700, 180, 76, CERTO)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def r():
        resumo(c, t, C, "s20", (("s20.a", [("patamar:", "g", 66), ("muda", "i", 70), ("o", "i", 70), ("estado,", "i", 70), ("T", "g", 66, COR), ("parada", "i", 70)]),
                                ("s20.b", [("Q = m · L", "g", 70, COR)]),
                                ("s20.c", [("curva:", "g", 66), ("uma", "i", 70), ("conta", "i", 70), ("por", "i", 70), ("etapa", "g", 66, COR)])))
    E.saida(c, t, C["s21"] - 0.1, r)
    if t < C["s21"]:
        return
    E.frase(c, t, C["s21"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C["s21.a"], [("Trocas", "g", 120, COR), ("de", "i", 110), ("calor", "g", 120, COR)], XE, 410)
    E.frase(c, t, C["s21.a"] + 0.5, ps("no calorímetro", "i", 90), XE, 540)
    q = ease_io(prog(t, C["s21.b"], 2.0))
    cq, cf = E.mix(E.COR, "#B07AA0", q), E.mix(FRIO, "#B07AA0", q)
    E.foco(c, t, C["s21.a"] + 0.4, 0.5, lambda a: (F.bloco(c, 500, 820, 260, 200, None, cq, a), F.bloco(c, 760, 820, 260, 200, None, cf, a)))
    seta_calor(c, t, C["s21.a"] + 0.8, (460, 660), (820, 660), None, a=1 - q, amp=10, ondas=2)
    inscreva(c, t, C, "s21", "s21.c", "s21.d")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, patamar=b_patamar, formula=b_formula, suor=b_suor, curva=b_curva,
              erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
