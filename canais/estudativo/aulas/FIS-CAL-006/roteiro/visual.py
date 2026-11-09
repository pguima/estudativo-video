"""Visual — Estudativo · FIS-CAL-006: trocas de calor com gelo.
Segue a linguagem visual da trilha Calor e Termodinâmica (cabeçalho do visual.py da FIS-CAL-001: quente laranja, frio azul,
gelo azul-claro, água azul translúcida; contas empilhadas e resultado na esfera).
Peça própria: comparar — duas colunas lado a lado, "disponível" (laranja: o que a água quente cede até 0 °C) e "necessário"
(azul: o que o gelo pede para derreter inteiro), com o veredito embaixo. É o passo que decide o caso antes da conta.
copo_misto mostra o estado final: gelo boiando sobre a água, com as massas escritas.
Todo instante vem de C[...] (marcadores do roteiro)."""
import math

import editorial as E
import fisica as F
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Física", "Calor e Termodinâmica")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_FIS-CAL-006_trocas_de_calor_com_gelo.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("ideia", "caso1", "caso2", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
FRIO = F.NEG
GELO = "#A9D8F5"
AGUA = "#5BA8E0"
LF = 80  # calor latente de fusão do gelo, cal/g

# todas as contas da aula
def mistura(m_gelo, m_agua, T_agua, T_gelo=0.0):
    """devolve (temperatura final, gelo que sobra, água no fim) com a comparação antes da conta"""
    disp = m_agua * 1 * T_agua
    nec = m_gelo * 0.5 * (0 - T_gelo) + m_gelo * LF
    if disp >= nec:
        return (disp - nec) / (m_gelo + m_agua), 0, m_gelo + m_agua
    derrete = (disp - m_gelo * 0.5 * (0 - T_gelo)) / LF
    return 0, m_gelo - derrete, m_agua + derrete


assert 300 * 40 == 12000 and 100 * 80 == 8000 and mistura(100, 300, 40) == (10, 0, 400) and 4000 / 400 == 10
assert 8000 + 100 * 10 + 300 * (10 - 40) == 0
assert 100 * 40 == 4000 and 200 * 80 == 16000 and mistura(200, 100, 40) == (0, 150, 150) and 4000 / 80 == 50
assert 200 * 80 + 200 * (-40) + 100 * (-40 - 40) == 0          # o −40 absurdo do gancho
assert 100 * 0.5 * 10 == 500
assert 1 * 1 * 80 == 80 == 1 * LF and 100 * 40 / LF == 50       # macete do oitenta
assert 150 * 32 == 4800 and mistura(100, 150, 32) == (0, 40, 210) and 4800 / 80 == 60 and 150 * 32 / 80 == 60
assert 8000 + 250 * -12.8 + 0 == 4800 and math.isclose((4800 - 8000) / 250, -12.8)   # o erro na questão daria −12,8 °C


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
def comparar(c, t, td, tn, disp, nec, x, yb, h, vmax, rot_d=None, rot_n=None, w=170, gap=120, size=56, valores=True):
    """duas colunas crescendo: disponível (laranja) em td e necessário (azul) em tn; rótulos com o valor em cal"""
    for i, (ti, v, cor, nome, rot) in enumerate(((td, disp, E.COR, "disponível", rot_d), (tn, nec, FRIO, "necessário", rot_n))):
        q = ease_io(prog(t, ti, 0.8))
        if t < ti:
            continue
        xx = x + i * (w + gap)
        hh = h * v / vmax * q
        M.rrect(c, xx, yb - hh, w, hh, 14, cor, 0.95)
        E.foco(c, t, ti, 0.4, lambda a, xx=xx, nome=nome: centro(c, nome, xx + w / 2, yb + 60, 44, "i", TINTA2, a))
        if valores:
            E.foco(c, t, ti + 0.6, 0.4, lambda a, xx=xx, v=v, hh=h * v / vmax, cor=cor:
                   F.medida(c, f"{v:,}".replace(",", "."), "cal", xx + w / 2, yb - hh - 24, size, cor, a, "center"))
        if rot:
            E.foco(c, t, ti + 0.2, 0.4, lambda a, xx=xx, rot=rot: E.formula(c, rot, xx + w / 2, yb + 120, 40, "b", TINTA2, a, "center"))
    M.line(c, x - 30, yb, x + 2 * w + gap + 30, yb, TINTA, ep(t, td, 0.4), 5) if t >= td else None


def copo_misto(c, cx, yb, w, h, gelo_g, agua_g, a=1.0, temp="0 °C"):
    """copo com água e cubos de gelo boiando (gelo_g = 0: sem gelo); massas escritas ao lado"""
    if a <= 0:
        return
    nivel = 0.72
    M.rrect(c, cx - w / 2 + 8, yb - h * nivel, w - 16, h * nivel - 6, 12, AGUA, 0.55 * a)
    if gelo_g:
        for dx, g in ((-0.2, 8), (0.15, -10)):
            c.save(); c.translate(cx + dx * w, yb - h * nivel + 10); c.rotate(g)
            M.rrect(c, -w * 0.13, -w * 0.13, w * 0.26, w * 0.26, 8, GELO, a)
            c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(-w * 0.13, -w * 0.13, w * 0.26, w * 0.26), 8, 8), M.paint(FRIO, a, stroke=3))
            c.restore()
    p = skia.Path()
    p.moveTo(cx - w / 2, yb - h); p.lineTo(cx - w / 2 + 10, yb); p.lineTo(cx + w / 2 - 10, yb); p.lineTo(cx + w / 2, yb - h)
    c.drawPath(p, M.paint(TINTA, a, stroke=6))
    xr = cx + w / 2 + 30
    if gelo_g:
        F.medida(c, gelo_g, "g de gelo", xr, yb - h * 0.62, 60, FRIO, a)
    F.medida(c, agua_g, "g de água", xr, yb - h * 0.62 + (80 if gelo_g else 0), 60, AGUA, a)
    if temp:
        E.formula(c, temp, xr, yb - h * 0.62 + (170 if gelo_g else 90), 60, "g", TINTA, a)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def um():
        E.foco(c, t, C["s01.a"], 0.5, lambda a: copo(c, 1450, 900, 380, 460, a))
        E.foco(c, t, C["s01.a"] + 0.3, 0.4, lambda a: F.medida(c, 200, "g de gelo a 0 °C", 1150, 330, 62, FRIO, a))
        E.foco(c, t, C["s01.b"], 0.4, lambda a: F.medida(c, 100, "g de água a 40 °C", 1150, 410, 62, COR, a))
        E.frase(c, t, C["s01.a"], ps("gelo + água", "i", 80), XE, 230)
        E.frase(c, t, C["s01.b"] + 1.5, ps("tudo na soma = 0:", "i", 60, TINTA2), XE, 380, passo=0.1)
        E.foco(c, t, C["s01.c"], 0.5, lambda a: F.medida(c, "−40", "°C", XE, 560, 160, ERRADO, a))
        E.frase(c, t, C["s01.c"] + 1.6, ps("água líquida a −40?", "i", 64), XE, 720, passo=0.1)
        E.foco(c, t, C["s01.d"], 0.5, lambda a: (E.escreve(c, "impossível", XE, 860, 90, "g", ERRADO, a), E.selo(c, XE + 560, 830, 50, False, a)))
    E.saida(c, t, C["s02"] - 0.1, um)
    if t >= C["s02"]:
        promessa(c, t, C, "s02", (("s02.b", "decidir antes da conta", COR), ("s02.c", "o estado final", TINTA)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    def lat(a, x, y):
        E.formula(c, "Q = m · L", x - 60, y + 4, 56, "g", TINTA, a, "center")
        E.formula(c, "L = 80 cal/g", x - 60, y + 74, 44, "g", FRIO, a, "center")

    def soma(a, x, y):
        E.formula(c, "soma dos Q = 0", x - 80, y + 30, 54, "g", TINTA, a, "center")
    lembrete2(c, t, C, "s03", (("s03.b", "derreter o gelo:", "calor latente"), ("s03.c", "no calorímetro,", "soma = 0")), (lat, soma))


# ---------------- a ideia ----------------
def b_ideia(c, t, C, b):
    def s04():
        E.frase(c, t, C["s04"] + 0.4, ps("com gelo, a dúvida:", "i", 66, TINTA2), XE, 200, passo=0.1)
        E.frase(c, t, C["s04.a"], ps("tem calor para", "i", 76) + [("derreter tudo?", "g", 76, COR)], XE, 320, passo=0.1)
        for i, (k, s1, s2, cor, gelo_g) in enumerate((("s04.b", "sim", "só água, acima de 0 °C", E.COR, 0), ("s04.c", "não", "para em 0 °C", FRIO, 1))):
            x = 220 + i * 820
            p = ep(t, C[k], 0.5)
            E.caixa_pontilhada(c, x, 430, 700, 520, p, prog_=p)
            E.frase(c, t, C[k] + 0.1, [(s1, "g", 80, cor)], x + 50, 530)
            E.frase(c, t, C[k] + 0.3, ps(s2, "i", 52), x + 50, 610, passo=0.08)
            E.foco(c, t, C[k] + 0.5, 0.5, lambda a, x=x, gelo_g=gelo_g: _copinho(c, x + 190, 910, gelo_g, a))
        E.frase(c, t, C["s04.d"], [("gelo + água", "g", 52, FRIO)], 1370, 800)
    E.saida(c, t, C["s05"] - 0.1, s04)
    if t < C["s05"]:
        return
    E.frase(c, t, C["s05.a"], [("compare", "g", 84, COR)] + ps("antes da equação", "i", 84), XE, 220, passo=0.1)
    comparar(c, t, C["s05.b"], C["s05.c"], 1, 1, 1150, 880, 360, 1, "quente até 0 °C", "derreter o gelo", w=200, gap=160, valores=False)
    E.frase(c, t, C["s05.b"], [("disponível:", "g", 60, COR)], XE, 420)
    E.frase(c, t, C["s05.b"] + 0.6, ps("o que a água quente cede até 0 °C", "i", 50), XE, 500, passo=0.06)
    E.frase(c, t, C["s05.c"], [("necessário:", "g", 60, FRIO)], XE, 660)
    E.frase(c, t, C["s05.c"] + 0.6, ps("o que o gelo pede para derreter todo", "i", 50), XE, 740, passo=0.06)


def _copinho(c, cx, yb, gelo, a):
    """copo pequeno: com gelo boiando (gelo=1) ou só água"""
    w, h = 200, 240
    M.rrect(c, cx - w / 2 + 8, yb - h * 0.7, w - 16, h * 0.7 - 6, 12, AGUA, 0.55 * a)
    if gelo:
        for dx, g in ((-0.2, 8), (0.15, -10)):
            c.save(); c.translate(cx + dx * w, yb - h * 0.7 + 10); c.rotate(g)
            M.rrect(c, -26, -26, 52, 52, 8, GELO, a)
            c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(-26, -26, 52, 52), 8, 8), M.paint(FRIO, a, stroke=3))
            c.restore()
    p = skia.Path()
    p.moveTo(cx - w / 2, yb - h); p.lineTo(cx - w / 2 + 10, yb); p.lineTo(cx + w / 2 - 10, yb); p.lineTo(cx + w / 2, yb - h)
    c.drawPath(p, M.paint(TINTA, a, stroke=6))


# ---------------- caso 1: derrete tudo ----------------
def b_caso1(c, t, C, b):
    def s06_07():
        E.frase(c, t, C["s06"], [("caso 1", "g", 60, COR)], XE, 190)
        E.foco(c, t, C["s06.a"], 0.4, lambda a: E.formula(c, "100 g de gelo a 0 °C", XE + 260, 190, 56, "g", FRIO, a))
        E.foco(c, t, C["s06.b"], 0.4, lambda a: E.formula(c, "+ 300 g de água a 40 °C", XE + 920, 190, 56, "g", COR, a))
        comparar(c, t, C["s06.c"], C["s06.d"], 12000, 8000, 1200, 760, 420, 16000, "300 · 1 · 40", "100 · 80", w=190, gap=140)
        E.frase(c, t, C["s07.a"], [("12.000", "g", 70, COR), (">", "g", 70, TINTA2), ("8.000", "g", 70, FRIO)], XE, 380, passo=0.12)
        E.frase(c, t, C["s07.b"], [("derrete", "g", 66, CERTO), ("tudo", "g", 66, CERTO)], XE, 490)
        passos(c, t, [(C["s07.c"], "sobram 4.000 cal", TINTA), (C["s07.d"], "para 400 g, a partir de 0 °C", TINTA2),
                      (C["s07.e"], "ΔT = 4.000 ÷ 400 = 10", TINTA)], XE, 640, 110, 60)
        bola_txt(c, t, C["s07.e"] + 0.8, "10 °C", 1010, 560, 100, 60, CERTO)
    E.saida(c, t, C["s08"] - 0.1, s06_07)
    if t < C["s08"]:
        return
    E.frase(c, t, C["s08"], ps("conferindo com a", "i", 66) + [("soma = 0", "g", 66, COR)], XE, 220, passo=0.1)
    formula_em(c, t, C["s08.b"], "8.000", XE, 450, 76, cor=FRIO)
    formula_em(c, t, C["s08.b"] + 0.9, "+ 100 · T", XE + 260, 450, 76, cor=AGUA)
    formula_em(c, t, C["s08.b"] + 3.2, "+ 300 · (T − 40) = 0", XE + 650, 450, 76, cor=COR)
    E.foco(c, t, C["s08.b"] + 0.3, 0.4, lambda a: E.escreve(c, "derreter", XE, 530, 40, "i", TINTA2, a))
    E.foco(c, t, C["s08.b"] + 1.2, 0.4, lambda a: E.escreve(c, "a água do gelo, de 0 até T", XE + 260, 530, 40, "i", TINTA2, a))
    E.foco(c, t, C["s08.b"] + 3.5, 0.4, lambda a: E.escreve(c, "a água quente", XE + 650, 530, 40, "i", TINTA2, a))
    passos(c, t, [(C["s08.c"] - 0.6, "400T − 4.000 = 0", TINTA2)], XE, 700, 100, 76)
    E.foco(c, t, C["s08.c"], 0.5, lambda a: (E.formula(c, "T = 10 °C", XE, 860, 90, "g", CERTO, a), E.selo(c, XE + 560, 830, 50, True, a)))


# ---------------- caso 2: não derrete tudo ----------------
def b_caso2(c, t, C, b):
    def s09_10():
        E.frase(c, t, C["s09"], [("caso 2", "g", 60, COR)], XE, 190)
        E.foco(c, t, C["s09.a"], 0.4, lambda a: E.formula(c, "200 g de gelo a 0 °C", XE + 260, 190, 56, "g", FRIO, a))
        E.foco(c, t, C["s09.b"], 0.4, lambda a: E.formula(c, "+ 100 g de água a 40 °C", XE + 920, 190, 56, "g", COR, a))
        comparar(c, t, C["s09.c"], C["s09.d"], 4000, 16000, 1200, 860, 520, 16000, "100 · 1 · 40", "200 · 80", w=190, gap=140)
        E.frase(c, t, C["s10.a"], [("4.000", "g", 70, COR), ("<", "g", 70, TINTA2), ("16.000", "g", 70, FRIO)], XE, 380, passo=0.12)
        E.frase(c, t, C["s10.b"], ps("não derrete tudo", "g", 62, ERRADO), XE, 490, passo=0.1)
        E.frase(c, t, C["s10.c"], ps("termina em", "i", 62) + [("0 °C", "g", 62, FRIO)], XE, 590, passo=0.1)
        formula_em(c, t, C["s10.d"], "derrete: 4.000 ÷ 80 = 50 g", XE, 720, 60)
        E.foco(c, t, C["s10.e"], 0.5, lambda a: E.pilula(c, "150 g de gelo + 150 g de água, a 0 °C", XE + 470, 850, 44, "b", fundo=FRIO, a=a))
    E.saida(c, t, C["s11"] - 0.1, s09_10)
    if t < C["s11"]:
        return
    E.frase(c, t, C["s11"], ps("gelo", "i", 76) + [("abaixo de zero?", "g", 76, FRIO)], XE, 230, passo=0.1)
    E.frase(c, t, C["s11.a"], ps("o necessário ganha", "i", 64) + [("uma etapa antes", "g", 60)], XE, 380, passo=0.1)
    formula_em(c, t, C["s11.b"], "c do gelo = 0,5", XE, 520, 70, cor=FRIO)
    formula_em(c, t, C["s11.c"], "100 · 0,5 · 10 = 500 cal", XE, 680, 76)
    E.foco(c, t, C["s11.c"] + 0.3, 0.4, lambda a: E.escreve(c, "(100 g de gelo, de −10 °C a 0 °C)", XE, 750, 40, "i", TINTA2, a))
    E.frase(c, t, C["s11.d"], ps("some ao necessário e", "i", 64) + [("compare", "g", 60, COR)], XE, 900, passo=0.1)
    term(c, t, C["s11"] + 0.4, 1550, 900, 520, -10, -20, 20)
    marca(c, t, C["s11"] + 1.0, 1550, y_term(-10, 900, 520, -20, 20), "−10", "°C", 46, FRIO)
    marca(c, t, C["s11.a"] + 0.6, 1550, y_term(0, 900, 520, -20, 20), 0, "°C", 46)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s12"], [("cuidado", "g", 96, ERRADO)], XE, 210)
    E.foco(c, t, C["s12.a"], 0.5, lambda a: F.medida(c, "−40", "°C", XE, 420, 140, ERRADO, a))
    if t >= C["s12.a"] + 0.8:
        E.risco(c, XE - 10, 440, XE + 420, 330, t, C["s12.a"] + 0.8, largura=12)
    E.frase(c, t, C["s12.b"], ps("supôs que", "i", 66) + [("todo o gelo derreteu", "g", 62)], XE, 580, passo=0.1)
    E.frase(c, t, C["s12.b"] + 1.4, ps("e o calor não dava", "i", 66, TINTA2), XE, 680, passo=0.1)
    E.foco(c, t, C["s12.c"], 0.5, lambda a: E.pilula(c, "T < 0 °C com água líquida = pulou a comparação", W / 2, 880, 50, "g", fundo=ERRADO, a=a))
    E.foco(c, t, C["s12.a"], 0.5, lambda a: _copinho(c, 1500, 640, 1, a))


# ---------------- atalho (palco) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def s13():
        E.frase(c, t, C["s13"], ps("o macete do", "i", 76, CLARO) + [("80", "g", 84, BR)], W / 2, 180, "center", 0.12)
        E.foco(c, t, C["s13.a"], 0.5, lambda a: E.formula(c, "1 g de água a 80 °C → 0 °C", W / 2, 380, 76, "g", BR, a, "center"))
        E.foco(c, t, C["s13.a"] + 1.4, 0.5, lambda a: E.formula(c, "cede 1 · 1 · 80 = 80 cal", W / 2, 490, 64, "b", CLARO, a, "center"))
        E.foco(c, t, C["s13.b"], 0.5, lambda a: E.formula(c, "80 cal derretem 1 g de gelo", W / 2, 630, 76, "g", BR, a, "center"))
        E.frase(c, t, C["s13.c"], ps("água a 80 °C derrete", "i", 70, CLARO) + [("a mesma massa", "g", 66, BR)], W / 2, 850, "center", 0.1)
    E.saida(c, t, C["s14"] - 0.1, s13)
    if t < C["s14"]:
        return
    E.frase(c, t, C["s14.a"], ps("a 40 °C, metade:", "i", 70, CLARO) + [("derrete metade da sua massa", "g", 62, BR)], W / 2, 260, "center", 0.1)
    E.foco(c, t, C["s14.b"], 0.5, lambda a: E.formula(c, "100 g a 40 °C  →  derrete 50 g", W / 2, 470, 84, "g", BR, a, "center"))
    E.foco(c, t, C["s14.b"] + 1.4, 0.4, lambda a: E.escreve(c, "sem conta nenhuma", 1200, 560, 50, "i", CLARO, a))
    E.frase(c, t, C["s14.c"], [("não", "g", 60, ERRADO), ("compensa:", "i", 64, CLARO)] + ps("gelo abaixo de zero", "i", 64, CLARO), W / 2, 780, "center", 0.1)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s15"], ps("hora de testar", "i", 72, COR), XE, 200)
    E.foco(c, t, C["s15.a"], 0.5, lambda a: E.formula(c, "100 g de gelo a 0 °C", XE, 360, 76, "g", FRIO, a))
    E.foco(c, t, C["s15.b"], 0.5, lambda a: E.formula(c, "+ 150 g de água a 32 °C", XE, 490, 76, "g", COR, a))
    E.frase(c, t, C["s15.c"], [("a)", "g", 64, COR)] + ps("o gelo derrete todo?", "i", 68), XE, 660, passo=0.1)
    E.frase(c, t, C["s15.d"], [("b)", "g", 64, COR)] + ps("como termina a mistura?", "i", 68), XE, 780, passo=0.1)
    if t < C["s16"]:
        E.foco(c, t, C["s15.a"], 0.5, lambda a: _copinho(c, 1500, 640, 1, a))
    else:
        E.relogio(c, t, C["s16.a"], cx=1460, cy=440, r=200)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    def s17():
        comparar(c, t, C["s17.a"], C["s17.b"], 4800, 8000, 1200, 800, 460, 8000, "150 · 1 · 32", "100 · 80", w=190, gap=140)
        E.frase(c, t, C["s17.a"] + 1.4, [("4.800", "g", 70, COR), ("<", "g", 70, TINTA2), ("8.000", "g", 70, FRIO)], XE, 300, passo=0.12)
        E.frase(c, t, C["s17.c"], ps("falta calor:", "i", 64) + [("não derrete tudo", "g", 60, ERRADO)], XE, 450, passo=0.1)
        E.frase(c, t, C["s17.c"] + 1.6, ps("para em", "i", 64) + [("0 °C", "g", 64, FRIO)], XE, 560, passo=0.1)
    E.saida(c, t, C["s18"] - 0.1, s17)
    if t < C["s18"]:
        return
    E.frase(c, t, C["s18.a"], ps("quanto derrete?", "i", 70), XE, 220)
    formula_em(c, t, C["s18.b"], "4.800 ÷ 80 = 60 g", XE, 380, 84)
    formula_em(c, t, C["s18.c"], "gelo: 100 − 60 = 40 g", XE, 540, 70, cor=FRIO)
    formula_em(c, t, C["s18.c"] + 1.4, "água: 150 + 60 = 210 g", XE, 660, 70, cor=AGUA)
    E.foco(c, t, C["s18.d"], 0.5, lambda a: copo_misto(c, 1250, 920, 300, 360, 40, 210, a, "a 0 °C"))
    E.foco(c, t, C["s18.d"] + 0.5, 0.5, lambda a: E.selo(c, XE + 900, 380 - 30, 50, True, a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def r():
        resumo(c, t, C, "s19", (("s19.a", [("compare", "g", 66, COR), ("disponível", "i", 70), ("e", "i", 70), ("necessário", "i", 70)]),
                                ("s19.b", [("sobra:", "g", 66), ("derrete", "i", 70), ("tudo,", "i", 70), ("T > 0 °C", "g", 66, COR)]),
                                ("s19.c", [("falta:", "g", 66), ("para", "i", 70), ("em", "i", 70), ("0 °C,", "g", 66, FRIO), ("gelo + água", "i", 70)])))
    E.saida(c, t, C["s20"] - 0.1, r)
    if t < C["s20"]:
        return
    E.frase(c, t, C["s20"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C["s20.b"], [("Diagrama", "g", 120, COR), ("de", "i", 110), ("fases", "g", 120, COR)], XE, 410, passo=0.12)
    E.frase(c, t, C["s20.a"], ps("a pressão entra na história", "i", 64, TINTA2), XE, 540, passo=0.1)

    def panela(a):
        x, y = 560, 940
        M.rrect(c, x - 220, y - 220, 440, 220, 24, TINTA2, a)
        M.rrect(c, x - 240, y - 250, 480, 40, 14, TINTA, a)
        M.rrect(c, x - 20, y - 300, 40, 60, 10, E.COR, a)
    E.foco(c, t, C["s20.c"], 0.5, panela)
    E.foco(c, t, C["s20.c"] + 0.4, 0.4, lambda a: E.escreve(c, "panela de pressão", 860, 820, 50, "i", TINTA2, a))
    inscreva(c, t, C, "s20", "s20.d", "s20.e")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, ideia=b_ideia, caso1=b_caso1, caso2=b_caso2, erro=b_erro, atalho=b_atalho,
              questao=b_questao, resposta=b_resposta, fim=b_fim)
