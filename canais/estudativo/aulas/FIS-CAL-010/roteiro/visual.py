"""Visual — Estudativo · FIS-CAL-010: convecção e irradiação (trilha Calor e Termodinâmica).

Segue a linguagem visual da Física (cabeçalho do visual.py da FIS-CIN-001) e a da trilha Calor e Termodinâmica (cabeçalho do
visual.py da FIS-CAL-001): QUENTE = laranja, FRIO = azul (F.NEG); calor = seta ONDULADA laranja (seta_calor), sempre do
quente para o frio; partículas que tremem para a agitação. Nesta aula:
- CONVECÇÃO = o próprio fluido andando: laço de setas grossas (laco), laranja no trecho que sobe (ar quente) e azul no que
  desce (ar frio). O "pacote" de ar quente é uma bolha de partículas que cresce (mais espaço) e sobe.
- IRRADIAÇÃO = setas onduladas finas saindo do corpo em leque (raios), em laranja; infravermelho em vermelho-escuro (IV).
- Luz do Sol = seta reta amarela (LUZ). Vácuo = faixa escura com a pílula "vácuo".
Todo instante vem de C[...] (marcadores do roteiro), para acompanhar a voz real quando ela chegar."""
import math
import re

import editorial as E
import fisica as F
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Física", "Calor e Termodinâmica")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_FIS-CAL-010_conveccao_irradiacao.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("conveccao", "brisas", "irradiacao", "garrafa", "estufa", "atalho", "questao", "fim"))
BR = "#FFFFFF"
FRIO = F.NEG
GELO = "#A9D8F5"
AGUA = "#5BA8E0"
LUZ = "#F2B705"
IV = "#B3261E"
AREIA = "#E8C98A"

# a aula não tem contas: os fatos estão no cabeçalho do cenas.py
def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças da trilha (copiadas da FIS-CAL-001) ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def bola_txt(c, t, t0, s, cx, cy, r, size, cor=None):
    """resposta na esfera: "300 J" com a unidade menor"""
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


def formula_em(c, t, t0, s, x, y, size, est="g", cor=TINTA, align="left"):
    E.formula_em(c, t, t0, s, x, y, size, est, cor, align)


def passos(c, t, linhas, x, y0, dy=125, size=80, align="left"):
    """contas empilhadas: linhas = [(t0, fórmula, cor)]"""
    for i, (ti, s, cor) in enumerate(linhas):
        formula_em(c, t, ti, s, x, y0 + i * dy, size, cor=cor, align=align)


def tracejado(c, t, t0, x0, x1, y, cor=TINTA2, d=0.6, largura=4):
    if t >= t0:
        M.line(c, x0, y, x1, y, cor, 0.8, largura, dash=E.TRACO, progress=ease_io(prog(t, t0, d)))


def particulas(c, t, x, y, w, h, agit, cor, a=1.0, n=(6, 4), r=17, borda=True):
    """caixa com partículas que tremem; agit = 0 (quase paradas) a 1 (muito agitadas)"""
    if a <= 0:
        return
    if borda:
        M.rrect(c, x, y, w, h, 26, E.mix(cor, "#FFFFFF", 0.86), a)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 26, 26), M.paint(cor, a, stroke=4))
    nc, nl = n
    c.save()
    c.clipRect(skia.Rect.MakeXYWH(x + 4, y + 4, w - 8, h - 8), True)
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


def seta_reta(c, t, t0, A, B, rotulo=None, cor=TINTA, d=0.5, largura=12, size=56, lado=-1, escuro=False, cab=None):
    """seta grossa e reta (o TRABALHO, o vento, a luz), crescendo de A a B; rótulo no meio (acima com lado=-1)"""
    if t < t0:
        return
    F.seta(c, *A, *B, cor, 1.0, largura, cab, ease_io(prog(t, t0, d)))
    if rotulo:
        mx, my = (A[0] + B[0]) / 2, (A[1] + B[1]) / 2
        if abs(B[0] - A[0]) < abs(B[1] - A[1]):
            xl, yl, al = mx + lado * 34, my + size * 0.36, "right" if lado < 0 else "left"
        else:
            xl, yl, al = mx, (my - 34 if lado < 0 else my + 34 + size * 0.75), "center"
        E.foco(c, t, t0 + d * 0.6, 0.4, lambda q: E.formula(c, rotulo, xl, yl, size, "g", BR if escuro else cor, q, al))


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


def promessa(c, t, C, cena, itens, y0=450, dy=150, size=78):
    """'até o fim da aula' + itens numerados; itens = [(cue, texto)]. A órbita da Física gira à direita"""
    tb = C[cena + ".a"] + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1500, 540, 300 * ease_back(prog(t, tb, 0.8)), giro=12 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, C[cena + ".a"], ps("até o fim da aula", "i", 88), XE, 280, passo=0.14)
    for i, (k, s) in enumerate(itens):
        y = y0 + i * dy
        E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, XE + 40, y - 28, 38, a=a), centro(c, str(i + 1), XE + 40, y - 6, 48, "g", BR, a)))
        E.frase(c, t, C[k] + 0.1, [(s, "g", size, COR if i == 0 else TINTA)], XE + 110, y)


def resumo(c, t, C, itens, y0=350, dy=170, size=66):
    """resumindo: itens = [(cue, partes de E.frase)]"""
    E.frase(c, t, C[itens[0][0].split(".")[0]], [("resumindo", "i", 92, COR)], W / 2, 180, "center")
    for i, (k, partes) in enumerate(itens):
        y = y0 + i * dy
        E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 260, y - 26, 52, a=a), centro(c, str(i + 1), 260, y - 4, 60, "g", BR, a)))
        E.frase(c, t, C[k] + 0.1, partes, 360, y, passo=0.1)


def inscreva(c, t, ti, tb):
    """fim: pílula de inscrição com o cursor (ti) e 'bons estudos' (tb)"""
    E.foco(c, t, ti, 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 420, 76, estilo="g", a=a))
    p = ease_io(prog(t, ti + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(720, 445, p), ep(t, ti + 0.2, 0.4))
    E.frase(c, t, tb, [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1570, 990, "center")



# ---------------- peças desta aula ----------------
def laco(c, t, t0, cx, cy, rx, ry, d=1.4, largura=12):
    """corrente de convecção: elipse de setas que sobe pela esquerda (laranja, ar quente) e desce pela direita (azul, ar frio)"""
    q = ease_io(prog(t, t0, d))
    if q <= 0:
        return
    n = 90
    pt = lambda g: (cx + rx * math.cos(g), cy + ry * math.sin(g))
    for i in range(n):
        g0 = math.pi / 2 + 2 * math.pi * q * i / n
        g1 = math.pi / 2 + 2 * math.pi * q * (i + 1) / n
        (x0, y0), (x1, y1) = pt(g0), pt(g1)
        M.line(c, x0, y0, x1, y1, E.COR if x0 < cx else FRIO, 1.0, largura, cap_round=True)
    for k in range(4):
        f = (k + 0.5) / 4
        if q >= f:
            g = math.pi / 2 + 2 * math.pi * f
            x, y = pt(g)
            dx, dy = -rx * math.sin(g), ry * math.cos(g)
            L = math.hypot(dx, dy)
            F._cabeca(c, x + dx / L * 22, y + dy / L * 22, dx / L, dy / L, 44, E.COR if x < cx else FRIO, 1.0)


def bolha(c, t, cx, cy, r, agit, cor, a=1.0):
    """pacote de ar: círculo com partículas que tremem"""
    if a <= 0:
        return
    c.drawCircle(cx, cy, r, M.paint(E.mix(cor, BR, 0.85), a))
    c.save()
    pth = skia.Path(); pth.addCircle(cx, cy, r - 4)
    c.clipPath(pth, True)
    particulas(c, t, cx - r, cy - r, 2 * r, 2 * r, agit, cor, a, n=(3, 3), r=11, borda=False)
    c.restore()
    c.drawCircle(cx, cy, r, M.paint(cor, a, stroke=4))


def aquecedor(c, x, y, w, h, a=1.0, t=0.0):
    """aquecedor no chão: corpo com aletas e brilho laranja; (x, y) = canto de baixo à esquerda"""
    if a <= 0:
        return
    M.rrect(c, x, y - h, w, h, 14, "#3A3A46", a)
    for k in range(5):
        xx = x + 22 + k * (w - 44) / 4
        M.line(c, xx, y - h + 22, xx, y - 22, E.COR, a * (0.7 + 0.3 * math.sin(t * 4 + k)), 10, cap_round=True)


def ar_cond(c, x, y, w, a=1.0):
    """ar-condicionado de parede (split): (x, y) = canto de cima à esquerda"""
    if a <= 0:
        return
    M.rrect(c, x, y, w, w * 0.32, 18, "#F4F4F6", a)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, w * 0.32), 18, 18), M.paint(TINTA, a, stroke=5))
    for k in range(3):
        M.line(c, x + 30, y + w * 0.2 + k * 12, x + w - 30, y + w * 0.2 + k * 12, TINTA2, a, 4)


def ar_frio(c, t, t0, x, y0, y1, n=3, gap=70, cor=None):
    """ar frio descendo: setas onduladas azuis"""
    for k in range(n):
        seta_calor(c, t, t0 + 0.15 * k, (x + k * gap, y0), (x + k * gap, y1), None, cor or FRIO, amp=10, ondas=2)


def geladeira(c, x, y, w, h, a=1.0):
    """geladeira antiga aberta: congelador em cima, prateleiras em grade. (x, y) = canto de cima à esquerda"""
    if a <= 0:
        return
    M.rrect(c, x, y, w, h, 24, "#F4F4F6", a)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 24, 24), M.paint(TINTA, a, stroke=6))
    M.rrect(c, x + 24, y + 24, w - 48, h * 0.2, 12, GELO, a)
    centro(c, "congelador", x + w / 2, y + 24 + h * 0.1 + 14, 38, "b", TINTA, a)
    for k in range(3):
        yy = y + h * (0.42 + 0.18 * k)
        for j in range(9):
            xx = x + 30 + j * (w - 60) / 8
            c.drawCircle(xx, yy, 5, M.paint(TINTA2, a))
        M.line(c, x + 24, yy, x + w - 24, yy, TINTA2, a * 0.5, 3, dash=(10, 12))


def sol(c, t, cx, cy, r, a=1.0):
    if a <= 0:
        return
    for k in range(12):
        g = math.radians(30 * k + t * 10)
        M.line(c, cx + math.cos(g) * r * 1.2, cy + math.sin(g) * r * 1.2, cx + math.cos(g) * r * 1.5, cy + math.sin(g) * r * 1.5, LUZ, a, 9, cap_round=True)
    E.bola(c, cx, cy, r, LUZ, a)


def lua(c, cx, cy, r, a=1.0):
    if a <= 0:
        return
    c.drawCircle(cx, cy, r, M.paint("#F1EBD0", a))
    c.drawCircle(cx + r * 0.45, cy - r * 0.2, r * 0.9, M.paint("#1D2440", a))


def terra(c, cx, cy, r, a=1.0):
    if a <= 0:
        return
    E.bola(c, cx, cy, r, "#2F7FD0", a)
    for dx, dy, k in ((-0.3, -0.2, 0.35), (0.3, 0.3, 0.3), (0.1, -0.5, 0.2)):
        c.drawCircle(cx + dx * r, cy + dy * r, k * r, M.paint("#3FA45B", a))


def garrafa(c, t, x, y, w, h, a=1.0, cor_liq=None, vacuo=True):
    """garrafa térmica em corte: parede de fora, vácuo, parede espelhada de dentro, líquido e tampa. (x, y) = canto de cima"""
    if a <= 0:
        return
    cor_liq = cor_liq or E.COR
    g = 34
    M.rrect(c, x, y + 70, w, h - 70, 40, "#D9DDE3", a)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y + 70, w, h - 70), 40, 40), M.paint(TINTA, a, stroke=7))
    M.rrect(c, x + g * 0.5, y + 70 + g * 0.5, w - g, h - 70 - g, 34, "#0B0B14" if vacuo else "#F4F4F6", a)
    ix, iy, iw, ih = x + g, y + 70 + g, w - 2 * g, h - 70 - 2 * g
    M.rrect(c, ix, iy, iw, ih, 26, "#C9CED6", a)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(ix, iy, iw, ih), 26, 26), M.paint("#F4F6FA", a, stroke=6))
    M.rrect(c, ix + 8, iy + ih * 0.25, iw - 16, ih * 0.75 - 8, 20, cor_liq, a * 0.85)
    M.rrect(c, x + w * 0.2, y, w * 0.6, 84, 18, TINTA2, a)


def lareira(c, t, x, y, w, h, a=1.0):
    """lareira com fogo e chaminé: (x, y) = canto de baixo à esquerda da boca"""
    if a <= 0:
        return
    M.rrect(c, x - 40, y - h - 40, w + 80, h + 40, 10, "#9C4A2F", a)
    M.rrect(c, x + w * 0.3, 60, w * 0.4, y - h - 40 - 60, 6, "#9C4A2F", a)
    for j in range(int((y - h - 100) / 60)):
        M.line(c, x + w * 0.3, 60 + j * 60, x + w * 0.7, 60 + j * 60, "#7A3622", a, 3)
    M.rrect(c, x, y - h, w, h, 10, "#1B1B20", a)
    for k in range(3):
        fx = x + w * (0.3 + 0.2 * k)
        fh = h * (0.55 + 0.12 * math.sin(t * 6 + k * 2))
        p = skia.Path()
        p.moveTo(fx - 50, y - 10); p.quadTo(fx - 40, y - fh * 0.6, fx, y - fh); p.quadTo(fx + 40, y - fh * 0.6, fx + 50, y - 10); p.close()
        c.drawPath(p, M.paint(E.COR, a))
        p2 = skia.Path()
        p2.moveTo(fx - 22, y - 10); p2.quadTo(fx - 18, y - fh * 0.35, fx, y - fh * 0.55); p2.quadTo(fx + 18, y - fh * 0.35, fx + 22, y - 10); p2.close()
        c.drawPath(p2, M.paint(LUZ, a))


def rosto(c, cx, cy, r, a=1.0):
    """rosto de perfil, olhando para a esquerda"""
    if a <= 0:
        return
    pele = "#E9B48C"
    c.drawCircle(cx, cy, r, M.paint(pele, a))
    c.drawCircle(cx - r * 0.95, cy + r * 0.05, r * 0.18, M.paint(pele, a))
    c.drawCircle(cx - r * 0.45, cy - r * 0.25, r * 0.09, M.paint(TINTA, a))
    M.rrect(c, cx - r * 0.6, cy + r * 0.85, r * 1.3, r * 1.4, r * 0.4, "#3A3A46", a)


def raios(c, t, t0, cx, cy, r0, r1, angs, cor=None, amp=8):
    """irradiação em leque: setas onduladas saindo do centro (cx, cy) nos ângulos dados (graus, 0 = direita, 90 = cima)"""
    for k, g in enumerate(angs):
        dx, dy = math.cos(math.radians(g)), -math.sin(math.radians(g))
        seta_calor(c, t, t0 + 0.08 * k, (cx + dx * r0, cy + dy * r0), (cx + dx * r1, cy + dy * r1), None, cor or E.COR, d=0.5, amp=amp, ondas=2)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def um():
        E.frase(c, t, C["s01.a"], ps("por que o ar-condicionado", "i", 80), XE, 300, passo=0.12)
        E.frase(c, t, C["s01.a"] + 1.0, ps("fica no", "i", 80) + [("alto?", "g", 84, COR)], XE, 410, passo=0.12)
        if t >= C["s01.a"]:
            M.line(c, 1180, 130, 1180, 940, TINTA2, ep(t, C["s01.a"], 0.5), 4)
        E.foco(c, t, C["s01.a"] + 0.4, 0.6, lambda a: ar_cond(c, 1240, 170, 460, a))
        ar_frio(c, t, C["s01.a"] + 1.4, 1330, 360, 760, n=4, gap=95)
    E.saida(c, t, C["s01.b"] - 0.1, um)
    if C["s01.b"] - 0.1 <= t < C["s02"]:
        def dois():
            E.frase(c, t, C["s01.b"], ps("e como o calor do", "i", 80) + [("Sol", "g", 84, COR)], XE, 300, passo=0.12)
            E.frase(c, t, C["s01.b"] + 1.2, ps("chega até aqui?", "i", 80), XE, 410, passo=0.12)
            E.foco(c, t, C["s01.b"] + 0.3, 0.6, lambda a: sol(c, t, 1000, 700, 110, a))
            E.foco(c, t, C["s01.b"] + 0.6, 0.6, lambda a: terra(c, 1700, 700, 90, a))
            raios(c, t, C["s01.b"] + 1.4, 1000, 700, 190, 600, (8, 0, -8), amp=8)
            pilula_em(c, t, C["s01.c"], "nem ar no caminho", 1360, 880, 50, TINTA)
        E.saida(c, t, C["s02"] - 0.1, dois)
    if t >= C["s02"]:
        promessa(c, t, C, "s02", (("s02.b", "geladeira"), ("s02.c", "brisas"), ("s02.d", "garrafa térmica"), ("s02.e", "efeito estufa")),
                 y0=440, dy=140, size=74)


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    def conducao(a, x, y):
        for k in range(3):
            E.bola(c, x - 110 + k * 90, y, 26, E.mix(E.COR, FRIO, k / 2), a)
        F.seta(c, x - 120, y + 52, x + 90, y + 52, E.COR, a, 6)

    def densidade(a, x, y):
        M.rrect(c, x - 120, y - 20, 240, 90, 10, AGUA, a * 0.6)
        M.rrect(c, x - 30, y - 50, 60, 40, 8, "#C8A06A", a)
        F.seta(c, x + 90, y + 40, x + 90, y - 70, E.COR, a, 6)
    lembrete2(c, t, C, "s03", (("s03.b", "condução:", "partícula a partícula"), ("s03.c", "densidade:", "o menos denso sobe")), (conducao, densidade))


# ---------------- convecção ----------------
QX0, QX1, QY0, QY1 = 960, 1800, 170, 900  # o quarto


def quarto(c, t, t0):
    q = ep(t, t0, 0.5)
    if q <= 0:
        return
    c.drawRect(skia.Rect.MakeLTRB(QX0, QY0, QX1, QY1), M.paint(TINTA, q, stroke=6))
    aquecedor(c, QX0 + 60, QY1 - 4, 220, 120, q, t)


def b_conveccao(c, t, C, b):
    if t < C["s06"]:
        quarto(c, t, C["s04.a"])
        # o pacote de ar quente: esquenta (s04.b), cresce (s04.c) e sobe (s05.a); depois a corrente (s05.d)
        cx = QX0 + 170
        k = ep(t, C["s04.c"], 1.0)
        sobe = ease_io(prog(t, C["s05.a"], 2.4))
        r = lerp(70, 105, k)
        cy = lerp(QY1 - 230, QY0 + 150, sobe)
        cor = E.mix(FRIO, E.COR, ep(t, C["s04.b"], 1.0))
        a_b = ep(t, C["s04.b"] - 0.6, 0.5) * (1 - ep(t, C["s05.d"], 0.6))
        bolha(c, t, cx, cy, r, 0.2 + 0.6 * ep(t, C["s04.b"], 1.0), cor, a_b)
        if t >= C["s05.b"]:  # ar frio desce do outro lado
            q = ease_io(prog(t, C["s05.b"], 2.4))
            bolha(c, t, QX1 - 200, lerp(QY0 + 150, QY1 - 150, q), 70, 0.15, FRIO, ep(t, C["s05.b"], 0.5) * (1 - ep(t, C["s05.d"], 0.6)))
        if t >= C["s05.c"]:
            F.seta(c, QX1 - 260, QY1 - 70, QX0 + 330, QY1 - 70, FRIO, ep(t, C["s05.c"], 0.4) * (1 - ep(t, C["s05.d"], 0.6)), 8, p=ease_io(prog(t, C["s05.c"], 0.8)))
        laco(c, t, C["s05.d"], (QX0 + QX1) / 2, (QY0 + QY1) / 2 + 20, 300, 270, d=1.6)

        def s04():
            E.frase(c, t, C["s04.a"], [("aquecedor", "g", 76), ("no", "i", 80), ("chão", "i", 80)], XE, 260, passo=0.12)
            E.frase(c, t, C["s04.b"], ps("o ar perto dele", "i", 70) + [("esquenta", "g", 70, COR)], XE, 400, passo=0.1)
            E.frase(c, t, C["s04.c"], ps("mesmo ar,", "i", 70) + [("mais espaço", "g", 70, COR)], XE, 540, passo=0.1)
            E.frase(c, t, C["s04.d"], [("densidade", "g", 70), ("menor", "g", 70, COR)], XE, 700, passo=0.12)
            formula_em(c, t, C["s04.d"] + 0.5, "d = f{m}{V}", XE + 40, 860, 80)
        E.saida(c, t, C["s05"] - 0.1, s04)
        if t >= C["s05"]:
            E.frase(c, t, C["s05.a"], [("ar", "i", 84), ("quente", "g", 84, COR), ("sobe", "g", 84, COR)], XE, 300, passo=0.12)
            E.frase(c, t, C["s05.a"] + 1.0, ps("como uma rolha na água", "i", 56, TINTA2), XE, 390, passo=0.08)
            E.frase(c, t, C["s05.b"], [("ar", "i", 84), ("frio", "g", 84, FRIO), ("desce", "g", 84, FRIO)], XE, 540, passo=0.12)
            E.frase(c, t, C["s05.d"], [("corrente", "g", 76), ("de", "i", 80)], XE, 720, passo=0.12)
            E.frase(c, t, C["s05.d"] + 0.4, [("convecção", "g", 90, COR)], XE, 830)
        return
    if t < C["s07"]:
        E.frase(c, t, C["s06.a"], [("a", "i", 80), ("matéria", "g", 80, COR), ("anda", "g", 80, COR)] + ps("e leva o calor", "i", 80), W / 2, 220, "center", 0.12)
        # fluido: partículas passeando; sólido: presas
        x1, x2, y, w, h = 230, 1030, 400, 660, 360
        E.foco(c, t, C["s06.b"], 0.5, lambda a: (M.rrect(c, x1, y, w, h, 26, E.mix(E.COR, BR, 0.88), a),
                                                c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x1, y, w, h), 26, 26), M.paint(E.COR, a, stroke=4))))
        if t >= C["s06.b"]:
            a = ep(t, C["s06.b"], 0.5)
            for i in range(14):
                u = ((t - C["s06.b"]) * 0.12 + i / 14) % 1.0
                g = 2 * math.pi * u
                E.bola(c, x1 + w / 2 + math.cos(g) * (w * 0.38) + 10 * math.sin(i), y + h / 2 + math.sin(g) * (h * 0.33), 15, E.COR, a)
        E.frase(c, t, C["s06.b"] + 0.3, [("líquidos", "g", 60), ("e", "i", 64), ("gases", "g", 60)], x1 + w / 2, y + h + 90, "center", 0.12)
        pilula_em(c, t, C["s06.b"] + 1.4, "fluidos", x1 + w / 2, y + h + 180, 56, E.COR)
        E.foco(c, t, C["s06.c"], 0.5, lambda a: particulas(c, t, x2, y, w, h, 0.12, TINTA2, a, n=(6, 3), r=18))
        E.frase(c, t, C["s06.c"] + 0.3, [("sólido:", "g", 60), ("presas", "i", 64), ("no", "i", 64), ("lugar", "i", 64)], x2 + w / 2, y + h + 90, "center", 0.12)
        pilula_em(c, t, C["s06.c"] + 1.0, "sem convecção", x2 + w / 2, y + h + 180, 56, ERRADO)
        return
    # s07: ar-condicionado e geladeira
    E.frase(c, t, C["s07.a"], ps("por isso, no", "i", 70) + [("alto", "g", 70, COR)], W / 2, 170, "center", 0.12)
    E.foco(c, t, C["s07.a"] + 0.3, 0.6, lambda a: ar_cond(c, 220, 280, 420, a))
    ar_frio(c, t, C["s07.a"] + 1.0, 320, 460, 820, n=3, gap=110)
    E.foco(c, t, C["s07.a"] + 1.6, 0.4, lambda a: centro(c, "o frio desce e espalha", 430, 920, 48, "i", TINTA2, a))
    gx, gy, gw, gh = 860, 240, 440, 680
    E.foco(c, t, C["s07.b"], 0.6, lambda a: geladeira(c, gx, gy, gw, gh, a))
    for k in range(2):
        seta_calor(c, t, C["s07.b"] + 1.2 + 0.2 * k, (gx + 140 + k * 90, gy + 230), (gx + 140 + k * 90, gy + gh - 60), None, FRIO, amp=10, ondas=2)
    F.seta(c, gx + gw - 90, gy + gh - 60, gx + gw - 90, gy + 230, E.COR, ep(t, C["s07.c"], 0.4), 10, p=ease_io(prog(t, C["s07.c"], 0.9)))
    E.foco(c, t, C["s07.c"] + 0.6, 0.4, lambda a: E.escreve(c, "o ar mais quente sobe", gx + gw + 30, gy + 420, 46, "i", COR, a))
    E.foco(c, t, C["s07.b"] + 1.6, 0.4, lambda a: E.escreve(c, "o ar frio desce", gx + gw + 30, gy + 600, 46, "i", FRIO, a))
    pilula_em(c, t, C["s07.d"], "prateleira em grade: o ar passa", gx + gw / 2, gy + gh + 70, 46, TINTA)


# ---------------- brisas ----------------
def praia(c, t, noite, a=1.0):
    """terra à esquerda, mar à direita, céu de dia ou de noite (noite de 0 a 1)"""
    ceu = E.mix("#DCEFFB", "#1D2440", noite)
    c.drawRect(skia.Rect.MakeLTRB(0, 0, W, 760), M.paint(ceu, a))
    c.drawRect(skia.Rect.MakeLTRB(0, 760, 900, H), M.paint(AREIA, a))
    c.drawRect(skia.Rect.MakeLTRB(900, 790, W, H), M.paint(AGUA, a))
    for k in range(5):
        M.line(c, 960 + k * 190, 830 + 20 * (k % 2), 1060 + k * 190, 830 + 20 * (k % 2), BR, a * 0.6, 4)
    centro(c, "terra", 450, 940, 60, "g", TINTA, a)
    centro(c, "mar", 1400, 970, 60, "g", BR, a)


def circulacao(c, t, t0, dia=True, d=1.6):
    """brisa: o ar sobe sobre o lado quente, vai por cima, desce sobre o frio e volta junto ao chão"""
    xq, xf = (450, 1400) if dia else (1400, 450)
    s = 1 if xf > xq else -1
    seta_reta(c, t, t0, (xq, 690), (xq, 330), None, E.COR, d=0.6, largura=12)
    seta_reta(c, t, t0 + 0.6, (xq + s * 60, 280), (xf - s * 60, 280), None, TINTA2, d=0.7, largura=8)
    seta_reta(c, t, t0 + 1.2, (xf, 330), (xf, 690), None, FRIO, d=0.6, largura=12)


def b_brisas(c, t, C, b):
    noite = ep(t, C["s09.a"], 1.0) if t >= C["s09"] else 0
    praia(c, t, noite)
    if t < C["s09"]:
        sol(c, t, 1640, 170, 70)
        E.frase(c, t, C["s08"], [("de", "i", 76), ("dia", "g", 80, COR)], XE, 160)
        E.foco(c, t, C["s08.a"], 0.5, lambda a: (centro(c, "esquenta rápido", 450, 740, 46, "b", COR, a)))
        E.foco(c, t, C["s08.a"] + 1.4, 0.5, lambda a: centro(c, "precisa de muito calor", 1400, 760, 46, "b", FRIO, a))
        circulacao(c, t, C["s08.b"], dia=True)
        E.foco(c, t, C["s08.b"] + 0.3, 0.4, lambda a: E.escreve(c, "ar quente sobe", 500, 520, 48, "i", COR, a))
        seta_reta(c, t, C["s08.c"], (1300, 860), (620, 860), None, TINTA, d=0.8, largura=16)
        pilula_em(c, t, C["s08.d"], "brisa marítima: do mar para a terra", W / 2 - 20, 600, 46, TINTA)
        return
    lua(c, 1640, 170, 60, ep(t, C["s09.a"], 0.8))
    E.frase(c, t, C["s09.a"], [("à", "i", 76, BR), ("noite", "g", 80, CLARO)], XE, 160)
    E.foco(c, t, C["s09.b"], 0.5, lambda a: (centro(c, "esfria rápido", 450, 740, 46, "b", FRIO, a)))
    E.foco(c, t, C["s09.b"] + 1.0, 0.5, lambda a: centro(c, "fica mais quente", 1400, 760, 46, "b", E.CLARO, a))
    circulacao(c, t, C["s09.c"], dia=False)
    E.foco(c, t, C["s09.c"] + 0.3, 0.4, lambda a: E.escreve(c, "o ar sobe", 1450, 520, 48, "i", E.CLARO, a))
    seta_reta(c, t, C["s09.d"], (620, 860), (1300, 860), None, TINTA, d=0.8, largura=16)
    pilula_em(c, t, C["s09.d"] + 0.4, "brisa terrestre: da terra para o mar", W / 2 - 20, 600, 46, TINTA)


# ---------------- irradiação ----------------
def b_irradiacao(c, t, C, b):
    if t < C["s11"]:
        q = ep(t, C["s10.a"], 0.6)
        if q > 0:
            c.drawRect(skia.Rect.MakeLTRB(560, 330, 1500, 830), M.paint("#0B0B14", 0.92 * q))
        sol(c, t, 380, 580, 140, ep(t, C["s10"], 0.6))
        terra(c, 1680, 580, 110, ep(t, C["s10"] + 0.4, 0.6))
        pilula_em(c, t, C["s10.a"] + 0.3, "vácuo: sem matéria", 1030, 400, 50, TINTA2)
        E.frase(c, t, C["s10.b"], [("sem", "i", 58, BR), ("condução", "g", 58, BR), ("nem", "i", 58, BR), ("convecção", "g", 58, BR)], 1030, 780, "center", 0.12)
        if t >= C["s10.b"] + 1.2:
            E.risco(c, 700, 760, 1360, 720, t, C["s10.b"] + 1.2, largura=10)
        for k, dy in enumerate((-70, 0, 70)):
            seta_calor(c, t, C["s10.c"] + 0.12 * k, (560, 580 + dy), (1520, 580 + dy * 0.6), None, E.COR, d=1.0, amp=12, ondas=5)
        E.frase(c, t, C["s10.c"] + 0.2, [("irradiação", "g", 96, COR)], W / 2, 220, "center")
        E.frase(c, t, C["s10.d"], ps("viaja como a luz,", "i", 64) + [("sem", "g", 60), ("matéria", "g", 60, COR)], W / 2, 960, "center", 0.1)
        return

    def s11a():
        E.frase(c, t, C["s11.a"], [("todo", "i", 84), ("corpo", "i", 84), ("irradia", "g", 84, COR)], XE, 230, passo=0.12)
        E.frase(c, t, C["s11.b"], ps("mais quente,", "i", 66) + [("mais", "g", 64, COR), ("irradia", "g", 64, COR)], XE, 360, passo=0.1)
        for i, (cx, cor, n, ag) in enumerate(((1100, E.mix(E.COR, FRIO, 0.6), 4, 0.3), (1580, E.COR, 8, 0.9))):
            E.foco(c, t, C["s11.a"] + 0.4 + 0.3 * i, 0.5, lambda a, cx=cx, cor=cor: E.bola(c, cx, 330, 90, cor, a))
            raios(c, t, C["s11.b"] + 0.5 * i, cx, 330, 110, 230, [k * 360 / n for k in range(n)], amp=6)
        E.frase(c, t, C["s11.c"], ps("no dia a dia:", "i", 66) + [("infravermelho", "g", 66, IV)], XE, 620, passo=0.1)
        pilula_em(c, t, C["s11.c"] + 1.2, "uma luz que o olho não vê", XE + 520, 720, 50, IV)
    E.saida(c, t, C["s11.d"] - 0.1, s11a)
    if t < C["s11.d"]:
        return
    # escuro absorve, claro reflete
    E.frase(c, t, C["s11.d"], ps("a cor da", "i", 76) + [("superfície", "g", 76, COR)] + ps("importa", "i", 76), W / 2, 170, "center", 0.12)
    for i, (x, cor, nome, k) in enumerate(((330, "#1B1B20", "escura absorve", "s11.d"), (1080, "#F4F4F6", "clara reflete", "s11.e"))):
        E.foco(c, t, C[k], 0.5, lambda a, x=x, cor=cor: (M.rrect(c, x, 620, 520, 220, 16, cor, a),
                                                       c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, 620, 520, 220), 16, 16), M.paint(TINTA, a, stroke=5))))
        for j in range(3):
            seta_reta(c, t, C[k] + 0.3 + 0.1 * j, (x + 80 + j * 150, 260), (x + 160 + j * 150, 600), None, LUZ, d=0.6, largura=7)
        E.foco(c, t, C[k] + 0.4, 0.4, lambda a, x=x, nome=nome, i=i: centro(c, nome, x + 260, 930, 60, "g", COR if i == 0 else TINTA, a))
    if t >= C["s11.d"] + 1.0:
        c.drawRect(skia.Rect.MakeLTRB(334, 624, 846, 836), M.paint(E.COR, 0.35 * ep(t, C["s11.d"] + 1.0, 1.0)))
    for j in range(3):
        seta_reta(c, t, C["s11.e"] + 1.0 + 0.1 * j, (1240 + j * 150, 600), (1320 + j * 150, 300), None, LUZ, d=0.6, largura=7)


# ---------------- garrafa térmica ----------------
def b_garrafa(c, t, C, b):
    if t < C["s13"]:
        gx, gy, gw, gh = 1150, 170, 420, 800
        E.foco(c, t, C["s12"] + 0.3, 0.6, lambda a: garrafa(c, t, gx, gy, gw, gh, a))
        E.frase(c, t, C["s12.a"], ps("bloqueia os", "i", 76) + [("três", "g", 76, COR)], XE, 120, passo=0.12)
        itens = (("s12.b", "parede dupla com vácuo", gy + 500, gx + 17), ("s12.d", "espelhada: reflete", gy + 330, gx + 40), ("s12.e", "tampa: o ar não sai", gy + 42, gx + gw * 0.2))
        for k, s, y, xa in itens:
            E.foco(c, t, C[k], 0.4, lambda a, s=s, y=y, xa=xa: (M.line(c, 760, y, xa, y, TINTA, a, 4), c.drawCircle(xa, y, 9, M.paint(TINTA, a)),
                                                              E.pilula(c, s, 520, y, 42, "b", fundo=TINTA, a=a)))
        E.foco(c, t, C["s12.c"], 0.4, lambda a: E.formula(c, "sem condução e sem convecção", 520, gy + 600, 40, "b", COR, a, "center"))
        # a irradiação bate na parede espelhada e volta
        if t >= C["s12.d"] + 0.4:
            seta_calor(c, t, C["s12.d"] + 0.4, (gx + gw / 2, gy + 520), (gx + gw - 52, gy + 420), None, IV, d=0.4, amp=6, ondas=2)
            seta_calor(c, t, C["s12.d"] + 0.9, (gx + gw - 52, gy + 420), (gx + gw / 2 - 30, gy + 330), None, IV, d=0.4, amp=6, ondas=2)
        return
    E.frase(c, t, C["s13"], ps("o mesmo jeito para", "i", 74), W / 2, 200, "center", 0.12)
    E.foco(c, t, C["s13.a"], 0.6, lambda a: garrafa(c, t, 300, 300, 300, 560, a, E.COR))
    E.foco(c, t, C["s13.a"] + 0.4, 0.4, lambda a: centro(c, "café quente", 450, 950, 54, "g", COR, a))
    E.foco(c, t, C["s13.b"], 0.6, lambda a: garrafa(c, t, 1320, 300, 300, 560, a, AGUA))
    E.foco(c, t, C["s13.b"] + 0.4, 0.4, lambda a: centro(c, "suco gelado", 1470, 950, 54, "g", FRIO, a))
    pilula_em(c, t, C["s13.c"], "só atrasa a troca", W / 2, 600, 58, E.COR)


# ---------------- efeito estufa ----------------
def b_estufa(c, t, C, b):
    if t < C["s15.e"] - 0.1:
        # chão, atmosfera
        c.drawRect(skia.Rect.MakeLTRB(0, 860, W, H), M.paint("#7A5A3A", ep(t, C["s14"], 0.5)))
        if t >= C["s14.b"]:
            c.drawRect(skia.Rect.MakeLTRB(0, 860, W, H), M.paint(E.COR, 0.35 * ep(t, C["s14.b"], 1.0)))
        c.drawRect(skia.Rect.MakeLTRB(0, 330, W, 560), M.paint("#9FD3F0", 0.35 * ep(t, C["s14"], 0.5)))
        E.foco(c, t, C["s14"] + 0.3, 0.4, lambda a: E.escreve(c, "atmosfera", 1560, 380, 44, "i", TINTA2, a))
        sol(c, t, 230, 190, 62, ep(t, C["s14"], 0.5))
        for j in range(3):
            seta_reta(c, t, C["s14.a"] + 0.15 * j, (330 + j * 60, 220 + j * 20), (700 + j * 160, 840), None, LUZ, d=0.9, largura=8)
        E.foco(c, t, C["s14.a"] + 0.5, 0.4, lambda a: E.escreve(c, "luz do Sol", 560, 300, 48, "g", "#9A7400", a))
        # o chão irradia infravermelho para cima
        for j in range(4):
            x = 1000 + j * 170
            seta_calor(c, t, C["s14.c"] + 0.12 * j, (x, 850), (x, 600 if j % 2 == 0 else 360), None, IV, d=0.7, amp=10, ondas=3)
        E.foco(c, t, C["s14.c"] + 0.5, 0.4, lambda a: E.escreve(c, "infravermelho", 1050, 960, 50, "g", BR, a))
        # gases que seguram
        for j, (x, y, s) in enumerate(((1080, 450, "CO₂"), (1420, 480, "H₂O"), (1250, 400, "CO₂"))):
            E.foco(c, t, C["s14.d"] + 0.3 * j, 0.4, lambda a, x=x, y=y, s=s: (E.bola(c, x, y, 42, TINTA2, a), centro(c, s, x, y + 12, 32, "b", BR, a)))
        for j in (0, 2):
            x = 1000 + j * 170
            seta_calor(c, t, C["s14.e"] + 0.2 * j, (x + 30, 580), (x + 80, 840), None, IV, d=0.7, amp=10, ondas=3)
        E.frase(c, t, C["s14"] + 0.2, [("efeito", "i", 80), ("estufa", "g", 84, COR)], 420, 170)
        if t >= C["s15"]:
            pilula_em(c, t, C["s15.a"], "entra fácil, sai difícil", 1110, 280, 50, E.COR)
            pilula_em(c, t, C["s15.b"], "sem ele: fria demais para a vida", 1460, 120, 44, TINTA)
            E.foco(c, t, C["s15.c"], 0.4, lambda a: E.pilula(c, "o problema: o excesso", 1460, 195, 44, "b", fundo=ERRADO, a=a))
            if t >= C["s15.d"]:
                F.termometro(c, t, C["s15.d"], 1800, 760, 280, 40, 0, 50, (), "°C")
        return
    E.frase(c, t, C["s15.e"], ps("num carro fechado ao sol", "i", 74), W / 2, 220, "center", 0.12)
    E.foco(c, t, C["s15.e"], 0.5, lambda a: F.carrinho(c, 960, 820, 640, a=a))
    if t >= C["s15.e"]:
        F.chao(c, 500, 1420, 820, ep(t, C["s15.e"], 0.5))
    for j in range(3):
        seta_reta(c, t, C["s15.e"] + 0.8 + 0.12 * j, (600 + j * 80, 320), (860 + j * 80, 640), None, LUZ, d=0.6, largura=7)
    E.foco(c, t, C["s15.e"] + 1.6, 0.4, lambda a: E.pilula(c, "o ar quente fica preso", 1360, 450, 46, "b", fundo=E.COR, a=a))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s16"], [("cuidado", "g", 96, ERRADO)], XE, 200)
    E.frase(c, t, C["s16.a"], [("“o", "i", 90), ("calor", "i", 90), ("sobe”", "i", 90)], XE + 480, 200, passo=0.12)
    if t >= C["s16.a"] + 1.0:
        E.risco(c, XE + 470, 220, XE + 1010, 150, t, C["s16.a"] + 1.0, largura=12)
    E.frase(c, t, C["s16.b"], ps("quem sobe é o", "i", 66) + [("ar quente", "g", 64, COR)], XE, 360, passo=0.1)
    # o calor vai para qualquer lado: bola quente no meio, setas para todos os lados
    cx, cy = 600, 700
    E.foco(c, t, C["s16.c"], 0.5, lambda a: E.bola(c, cx, cy, 80, E.COR, a))
    raios(c, t, C["s16.c"] + 0.4, cx, cy, 100, 250, (0, 90, 180, 270, 45, 135, 225, 315), amp=6)
    E.frase(c, t, C["s16.c"] + 0.5, ps("do quente para o frio,", "i", 56) + [("qualquer lado", "g", 52, COR)], cx, 1000, "center", 0.08)
    # ferro de passar: o calor desce
    fx, fy = 1400, 640

    def ferro(a):
        p = skia.Path()
        p.moveTo(fx - 200, fy); p.lineTo(fx + 170, fy); p.quadTo(fx + 170, fy - 120, fx + 20, fy - 150); p.lineTo(fx - 200, fy - 150); p.close()
        c.drawPath(p, M.paint("#3A3A46", a))
        M.rrect(c, fx - 160, fy - 230, 220, 40, 20, TINTA2, a)
        M.rrect(c, fx - 360, fy + 160, 720, 40, 8, "#7FA7D9", a)
    E.foco(c, t, C["s16.d"], 0.5, ferro)
    for j in range(3):
        seta_calor(c, t, C["s16.d"] + 0.6 + 0.1 * j, (fx - 120 + j * 110, fy + 10), (fx - 120 + j * 110, fy + 150), None, E.COR, d=0.5, amp=8, ondas=1.5)
    E.foco(c, t, C["s16.d"] + 1.0, 0.4, lambda a: centro(c, "aqui, o calor desce", fx, 960, 54, "g", COR, a))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    if t < C["s18"]:
        E.frase(c, t, C["s17.a"], [("duas", "i", 80, CLARO), ("perguntas", "g", 80, BR)], W / 2, 150, "center")

        def caixa(cx, cy, s, a, cor="#1E1E2A"):
            w = E.larg(s, "g", 54) + 80
            M.rrect(c, cx - w / 2, cy - 60, w, 120, 26, cor, a)
            c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2, cy - 60, w, 120), 26, 26), M.paint(E.CLARO, a, stroke=3))
            centro(c, s, cx, cy + 20, 54, "g", BR, a)
        E.foco(c, t, C["s17.b"], 0.5, lambda a: caixa(500, 330, "1. precisa de matéria?", a))
        seta_reta(c, t, C["s17.c"] - 0.6, (500, 400), (500, 540), "não", E.CLARO, largura=8, size=44, lado=-1, escuro=True)
        E.foco(c, t, C["s17.c"], 0.5, lambda a: E.pilula(c, "IRRADIAÇÃO", 500, 610, 64, "g", fundo=E.COR, a=a))
        seta_reta(c, t, C["s17.d"] - 0.3, (800, 330), (1060, 330), "sim", E.CLARO, largura=8, size=44, escuro=True)
        E.foco(c, t, C["s17.d"], 0.5, lambda a: caixa(1340, 330, "2. a matéria anda?", a))
        seta_reta(c, t, C["s17.e"] - 0.6, (1240, 400), (1120, 540), None, E.CLARO, largura=8, escuro=True)
        E.foco(c, t, C["s17.e"] - 0.3, 0.4, lambda a: E.escreve(c, "sim", 1060, 480, 44, "g", BR, a))
        E.foco(c, t, C["s17.e"], 0.5, lambda a: E.pilula(c, "CONVECÇÃO", 1090, 610, 64, "g", fundo=E.COR, a=a))
        seta_reta(c, t, C["s17.f"] - 0.4, (1440, 400), (1600, 540), None, E.CLARO, largura=8, escuro=True)
        E.foco(c, t, C["s17.f"] - 0.2, 0.4, lambda a: E.escreve(c, "não", 1550, 470, 44, "g", BR, a))
        E.foco(c, t, C["s17.f"], 0.5, lambda a: E.pilula(c, "CONDUÇÃO", 1640, 610, 64, "g", fundo=E.COR, a=a))
        E.frase(c, t, C["s17.b"] + 1.2, ps("passa pelo vácuo ou chega de longe", "i", 50, CLARO), 500, 780, "center", 0.06)
        E.frase(c, t, C["s17.d"] + 1.0, ps("líquido ou gás circulando", "i", 50, CLARO), 1090, 780, "center", 0.06)
        return
    E.frase(c, t, C["s18.a"], ps("só", "i", 80, CLARO) + [("três", "g", 80, BR)] + ps("jeitos de o calor passar", "i", 80, CLARO), W / 2, 260, "center", 0.12)
    E.frase(c, t, C["s18.a"] + 1.6, ps("cada pergunta elimina um", "i", 64, CLARO), W / 2, 380, "center", 0.1)
    E.frase(c, t, C["s18.b"], [("não", "g", 64, ERRADO), ("compensa:", "i", 68, CLARO)] + ps("processos misturados", "i", 68, CLARO), W / 2, 600, "center", 0.1)
    E.foco(c, t, C["s18.b"] + 0.8, 0.6, lambda a: garrafa(c, t, 1560, 640, 200, 380, a))
    E.frase(c, t, C["s18.c"], ps("olhe cada", "i", 68, CLARO) + [("parte", "g", 66, BR)] + ps("separadamente", "i", 68, CLARO), W / 2 - 120, 780, "center", 0.1)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s19"], ps("hora de testar", "i", 72, COR), XE, 200)
    E.frase(c, t, C["s19.a"], ps("de frente para uma", "i", 70) + [("lareira", "g", 70, COR)], XE, 330, passo=0.1)
    E.frase(c, t, C["s19.b"], [("1.", "g", 66, COR)] + ps("o que esquenta seu rosto,", "i", 66), XE, 480, passo=0.1)
    E.frase(c, t, C["s19.b"] + 1.4, ps("a 2 m do fogo?", "i", 66), XE + 70, 570, passo=0.1)
    E.frase(c, t, C["s19.c"], [("2.", "g", 66, COR)] + ps("o que leva a fumaça", "i", 66), XE, 720, passo=0.1)
    E.frase(c, t, C["s19.c"] + 1.2, ps("pela chaminé?", "i", 66), XE + 70, 810, passo=0.1)
    if t < C["s20"]:
        E.foco(c, t, C["s19.a"], 0.6, lambda a: lareira(c, t, 1380, 900, 380, 300, a))
    else:
        E.relogio(c, t, C["s20.a"], cx=1460, cy=440, r=200)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    lx, ly, lw, lh = 1300, 900, 380, 300
    E.foco(c, t, C["s21"], 0.6, lambda a: lareira(c, t, lx, ly, lw, lh, a))
    if t < C["s22"]:
        E.frase(c, t, C["s21.a"], ps("precisa de matéria?", "i", 70), XE, 260, passo=0.1)
        E.foco(c, t, C["s21.a"] + 1.4, 0.5, lambda a: E.pilula(c, "não: chega como luz", XE + 290, 380, 50, "b", fundo=TINTA, a=a))
        E.foco(c, t, C["s21"] + 0.4, 0.5, lambda a: rosto(c, 650, 700, 75, a))
        bloqueado = t >= C["s21.c"]
        for j, dy in enumerate((-60, 0, 60)):
            fim = 1010 if bloqueado else 750
            seta_calor(c, t, C["s21.a"] + 0.8 + 0.1 * j, (lx - 40, 760 + dy), (fim if not bloqueado else 1030, 720 + dy * 0.5), None, E.COR, d=0.8, amp=10, ondas=3)
        E.frase(c, t, C["s21.b"], [("irradiação", "g", 96, COR)], XE, 520)
        if bloqueado:  # uma pessoa na frente faz sombra
            E.foco(c, t, C["s21.c"], 0.5, lambda a: (M.rrect(c, 960, 520, 90, 400, 40, "#3A3A46", a), c.drawCircle(1005, 470, 55, M.paint("#3A3A46", a))))
            E.foco(c, t, C["s21.c"] + 0.6, 0.4, lambda a: E.pilula(c, "faz sombra", 1005, 360, 44, "b", fundo=TINTA, a=a))
        return
    E.frase(c, t, C["s22.a"], ps("na chaminé, o ar", "i", 70) + [("esquenta", "g", 68, COR)], XE, 300, passo=0.1)
    E.frase(c, t, C["s22.b"], ps("menos denso,", "i", 70) + [("sobe", "g", 70, COR)], XE, 440, passo=0.1)
    for j in range(3):
        seta_reta(c, t, C["s22.b"] + 0.3 + 0.15 * j, (lx + lw * 0.42 + j * 30, 560 - j * 60), (lx + lw * 0.42 + j * 30, 140), None, E.COR, d=0.9, largura=9)
    E.frase(c, t, C["s22.c"], [("convecção", "g", 110, COR)], XE, 660)
    E.foco(c, t, C["s22.c"] + 0.4, 0.4, lambda a: E.selo(c, XE + 760, 620, 56, True, a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def r():
        resumo(c, t, C, (("s23.a", [("convecção:", "g", 66, COR), ("o", "i", 66), ("fluido", "i", 66), ("circula", "i", 66)]),
                         ("s23.b", [("irradiação:", "g", 66, COR), ("como", "i", 66), ("luz,", "i", 66), ("até", "i", 66), ("no", "i", 66), ("vácuo", "i", 66)]),
                         ("s23.c", [("condução:", "g", 66, COR), ("pela", "i", 66), ("matéria", "i", 66), ("parada", "i", 66)])), y0=380, dy=190)
    E.saida(c, t, C["s24"] - 0.1, r)
    if t < C["s24"]:
        return
    E.frase(c, t, C["s24"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C["s24.a"], [("o", "i", 110), ("gás", "g", 120, COR), ("faz", "i", 110), ("força", "g", 120, COR)], XE, 420)
    E.frase(c, t, C["s24.b"], ps("o trabalho de um gás", "i", 70), XE, 560, passo=0.1)
    E.foco(c, t, C["s24.b"], 0.6, lambda a: cil(c, t, 640, 680, 300, 300, lerp(0.4, 0.7, 0.5 + 0.5 * math.sin(t * 1.5)), a))
    inscreva(c, t, C["s24.c"], C["s24.d"])


def cil(c, t, x, y, w, h, frac, a=1.0):
    """cilindro simples com êmbolo (versão curta do cilindro da FIS-CAL-011)"""
    ye = y + h * (1 - frac)
    M.rrect(c, x + 8, ye, w - 16, y + h - ye - 8, 6, "#FFE3D3", a)
    particulas(c, t, x + 8, ye + 4, w - 16, y + h - ye - 12, 0.6, E.COR, a, n=(4, 2), r=12, borda=False)
    M.rrect(c, x + 8, ye - 40, w - 16, 40, 8, TINTA2, a)
    M.rrect(c, x + w / 2 - 10, ye - 160, 20, 120, 6, TINTA2, a)
    p = skia.Path()
    p.moveTo(x, y - 30); p.lineTo(x, y + h); p.lineTo(x + w, y + h); p.lineTo(x + w, y - 30)
    c.drawPath(p, M.paint(TINTA, a, stroke=8))


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, conveccao=b_conveccao, brisas=b_brisas, irradiacao=b_irradiacao, garrafa=b_garrafa,
              estufa=b_estufa, erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
