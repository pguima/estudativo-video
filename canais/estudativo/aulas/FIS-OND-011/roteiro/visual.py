"""Visual — Estudativo · FIS-OND-011: rádio, micro-ondas, raios X e outros usos.

Linguagem visual: a da trilha Ondas e Som, escrita na docstring do visual.py da FIS-OND-001 (que segue a da Física,
FIS-CIN-001). Cada faixa do espectro abre com topo(): a faixa no alto, só a região da vez acesa. Peças espectro(),
atomo() e os ícones radio/forno/lampada/raiox/sol vêm da FIS-OND-010; os ícones novos (torre, tv, celular, wifi, radar,
agua, controle, pessoa_termica, protetor, microbio, nota, braco, avental, nucleo) são desta aula. Todo instante vem de C[...]."""
import math

import editorial as E
import fisica as F
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Física", "Ondas e Som")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_FIS-OND-011_radio_micro_ondas_raios_x_e_outros_usos.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("radio", "infra", "xgama", "atalho", "questao", "fim"))
BR = "#FFFFFF"

# a aula não tem conta; os números citados conferem: forno 2,45 GHz → λ ≈ 12 cm
assert abs(3e8 / 2.45e9 - 0.1224) < 1e-3
FAIXAS_USO = {"controle remoto": "infravermelho", "radiografia": "raios X", "protetor solar": "ultravioleta", "forno": "micro-ondas"}
ORDEM = ("rádio", "micro-ondas", "infravermelho", "visível", "ultravioleta", "raios X", "gama")
assert all(v in ORDEM for v in FAIXAS_USO.values())


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças da trilha (copiadas da FIS-OND-001) ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def bola_txt(c, t, t0, s, cx, cy, r, size, cor=None):
    """resposta na esfera: "3 m" com a unidade menor"""
    v, _, u = s.partition(" ")
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r * ease_back(prog(t, t0, 0.5)), cor, a),
                                     F.medida(c, v, u, cx, cy + size * 0.36, size, E.SOBRE, a, "center", cor_u=E.SOBRE)))


def bola_formula(c, t, t0, s, cx, cy, r, size, cor=None):
    """resposta na esfera escrita como fórmula ("3 × 10^{18}")"""
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r * ease_back(prog(t, t0, 0.5)), cor, a),
                                     E.formula(c, s, cx, cy + size * 0.36, size, "g", E.SOBRE, a, "center")))


def conta(c, t, linhas, x, y0, dy, size, align="left", escuro=False):
    """conta em pilha: linhas = [(instante, fórmula[, cor])]; a linha da vez fica laranja até a próxima chegar"""
    tinta = BR if escuro else TINTA
    for i, ln in enumerate(linhas):
        ti, s = ln[0], ln[1]
        prox = linhas[i + 1][0] if i + 1 < len(linhas) else 1e9
        cor = ln[2] if len(ln) > 2 else ((CLARO if escuro else COR) if t < prox else tinta)
        E.formula_em(c, t, ti, s, x, y0 + i * dy, size, "g", cor, align)


def pilula(c, t, t0, s, cx, cy, size, fundo=None, est="g"):
    E.foco(c, t, t0, 0.4, lambda a: E.pilula(c, s, cx, cy, size, est, fundo=fundo, a=a, cor=BR))


def lembrete3(c, t, C, cena, itens, desenhos):
    """lembrete de três coisas: itens = [(cue, linha fina, linha forte)]; desenhos[i](a, x, y) à direita da caixa"""
    E.frase(c, t, C[cena] + 0.2, ps("você precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C[cena + ".a"], 0.5, lambda a: E.escreve(c, "3", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C[cena + ".a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w, hh = 820, 1000, 200
    for i, (k, l1, l2) in enumerate(itens):
        y = 150 + i * 240
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, hh, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 54)], x + 44, y + 80)
        E.frase(c, t, C[k] + 0.3, [(l2, "g", 54, COR)], x + 44, y + 155)
        E.foco(c, t, C[k] + 0.6, 0.5, lambda a, i=i, y=y: desenhos[i](a, x + w - 170, y + hh / 2))
    q = ease_io(prog(t, C[itens[1][0]] - 0.35, 0.5))
    q2 = ease_io(prog(t, C[itens[2][0]] - 0.35, 0.5))
    E.cursor(c, x + w - 30, 330 + 240 * q + 240 * q2, ep(t, C[itens[0][0]], 0.4))
    E.frase(c, t, lerp(C[itens[2][0]], C[cena + ".end"], 0.6), ps("faltou alguma?", "i", 56, COR) + ps("procure no canal", "i", 56), 820, 960, "left", 0.12)


# ---------------- peças desta aula ----------------
FAIXAS = (("rádio", 300), ("micro-ondas", 240), ("infravermelho", 240), ("visível", 110), ("ultravioleta", 240), ("raios X", 220), ("gama", 250))
ARCO_IRIS = ["#E53935", "#FB8C00", "#FDD835", "#43A047", "#1E88E5", "#3949AB", "#8E24AA"]


def espectro(c, t, ts, x0, y, w=1600, h=100, rotulos=True, size=40, escuro=False, apaga=(), a=1.0):
    """faixa do espectro, rádio → gama, com a frequência crescendo para a direita. ts = instante de cada região
    (lista de 7) ou um só (entram em fila). apaga = índices que ficam apagados. Devolve [(x_ini, x_fim)] de cada região"""
    if not isinstance(ts, (list, tuple)):
        ts = [ts + 0.12 * i for i in range(7)]
    k = w / sum(L for _, L in FAIXAS)
    xs, x = [], x0
    tinta = BR if escuro else TINTA
    for i, (nome, L) in enumerate(FAIXAS):
        xa, xb = x, x + L * k
        xs.append((xa, xb))
        x = xb
        q = ep(t, ts[i], 0.5) * a * (0.25 if i in apaga else 1.0)
        if q <= 0:
            continue
        r = skia.Rect.MakeXYWH(xa, y + h * 0.5 * (1 - ease_back(min(1, q / max(a, 1e-6)))), xb - xa, h * ease_back(min(1, q / max(a, 1e-6))))
        if nome == "visível":
            p = skia.Paint(AntiAlias=True)
            p.setShader(skia.GradientShader.MakeLinear([skia.Point(xa, 0), skia.Point(xb, 0)], [M.hexc(cc, q) for cc in ARCO_IRIS]))
            c.drawRect(r, p)
        else:
            tom = E.mix(E.COR, "#FFFFFF", 0.85 - 0.1 * i) if not escuro else E.mix(E.COR, "#07070F", 0.75 - 0.08 * i)
            c.drawRect(r, M.paint(tom, q))
        M.line(c, xb, y, xb, y + h, tinta, 0.5 * q, 2)
        if rotulos:
            yy = y + h + 52 if i % 2 == 0 else y + h + 104
            if nome == "visível":
                yy = y - 26
            E.foco(c, t, ts[i] + 0.1, 0.4, lambda aa, nome=nome, xa=xa, xb=xb, yy=yy, q=q: centro(c, nome, (xa + xb) / 2, yy, size, "b", tinta, aa * q / max(a, 1e-6) * a), sobe=6)
    return xs


def chirp(c, t, t0, x0, x1, y, A, l0=330, l1=14, d=1.4, cor=None, largura=6):
    """onda com o lambda diminuindo da esquerda (l0) para a direita (l1), desenhada da esquerda para a direita"""
    if t < t0:
        return
    pts, fase = [], 0.0
    n = int(x1 - x0)
    for i in range(n + 1):
        u = i / n
        lam = l0 * (l1 / l0) ** u
        fase += 2 * math.pi / lam
        pts.append((x0 + i, y - A * math.sin(fase)))
    F.poli(c, pts, ease_io(prog(t, t0, d)), cor or E.COR, 1.0, largura)


def atomo(c, cx, cy, r, a=1.0, sai=0.0, cor_e=None):
    """núcleo laranja, órbita em tinta e um elétron azul; sai de 0 a 1 leva o elétron para fora, para cima e à direita"""
    if a <= 0:
        return
    pt = M.paint(TINTA2, 0.6 * a, stroke=4)
    c.drawOval(skia.Rect.MakeXYWH(cx - r, cy - r * 0.45, 2 * r, r * 0.9), pt)
    c.save(); c.translate(cx, cy); c.rotate(60)
    c.drawOval(skia.Rect.MakeXYWH(-r, -r * 0.45, 2 * r, r * 0.9), pt)
    c.restore()
    E.bola(c, cx, cy, r * 0.28, E.COR, a)
    for ang in (200, 330):
        g = math.radians(ang)
        E.bola(c, cx + r * math.cos(g), cy + r * 0.45 * math.sin(g), r * 0.1, cor_e or F.NEG, a)
    g = math.radians(20)
    ex, ey = cx + r * math.cos(g), cy + r * 0.45 * math.sin(g)
    s = ease_out(sai)
    E.bola(c, lerp(ex, ex + r * 1.3, s), lerp(ey, ey - r * 0.9, s), r * 0.1, cor_e or F.NEG, a)
    if s > 0.05:
        E._meio(c, "−", lerp(ex, ex + r * 1.3, s), lerp(ey, ey - r * 0.9, s) - r * 0.22, r * 0.18, "g", F.NEG, a * s)


def radio(c, cx, cy, s, a=1.0):
    if a <= 0:
        return
    M.line(c, cx + s * 0.6, cy - s * 0.55, cx + s * 1.0, cy - s * 1.25, TINTA, a, 6)
    M.rrect(c, cx - s, cy - s * 0.6, 2 * s, s * 1.2, s * 0.2, TINTA, a)
    c.drawCircle(cx - s * 0.45, cy, s * 0.35, M.paint(E.COR, a))
    c.drawCircle(cx - s * 0.45, cy, s * 0.12, M.paint(TINTA, a))
    for k in range(3):
        M.line(c, cx + s * 0.15, cy - s * 0.25 + k * s * 0.25, cx + s * 0.8, cy - s * 0.25 + k * s * 0.25, BR, a * 0.8, 4)


def forno(c, cx, cy, s, a=1.0):
    if a <= 0:
        return
    M.rrect(c, cx - s * 1.2, cy - s * 0.7, s * 2.4, s * 1.4, s * 0.12, TINTA, a)
    M.rrect(c, cx - s * 1.05, cy - s * 0.55, s * 1.55, s * 1.1, s * 0.08, "#3A3A44", a)
    for i in range(7):
        for j in range(5):
            c.drawCircle(cx - s * 0.95 + i * s * 0.22, cy - s * 0.43 + j * s * 0.22, s * 0.035, M.paint(E.COR, 0.7 * a))
    for k in range(3):
        c.drawCircle(cx + s * 0.85, cy - s * 0.35 + k * s * 0.3, s * 0.08, M.paint(BR, a))


def lampada(c, cx, cy, s, a=1.0):
    if a <= 0:
        return
    p = skia.Paint(AntiAlias=True)
    p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy - s * 0.2), s * 1.6, [M.hexc("#FFD54F", 0.55 * a), M.hexc("#FFD54F", 0)], [0, 1]))
    c.drawCircle(cx, cy - s * 0.2, s * 1.6, p)
    c.drawCircle(cx, cy - s * 0.2, s * 0.7, M.paint("#FFC107", a))
    M.rrect(c, cx - s * 0.32, cy + s * 0.4, s * 0.64, s * 0.5, s * 0.08, TINTA2, a)
    for k in range(3):
        M.line(c, cx - s * 0.32, cy + s * 0.5 + k * s * 0.13, cx + s * 0.32, cy + s * 0.5 + k * s * 0.13, BR, a * 0.7, 3)


def raiox(c, cx, cy, s, a=1.0):
    """filme de radiografia com um osso claro"""
    if a <= 0:
        return
    M.rrect(c, cx - s * 0.8, cy - s, s * 1.6, s * 2, s * 0.1, "#1C2430", a)
    for dy in (-1, 1):
        for dx in (-1, 1):
            c.drawCircle(cx + dx * s * 0.16, cy + dy * s * 0.62, s * 0.19, M.paint("#F2F2F2", a))
    M.rrect(c, cx - s * 0.13, cy - s * 0.62, s * 0.26, s * 1.24, s * 0.05, "#F2F2F2", a)


def sol(c, cx, cy, r, a=1.0, giro=0.0):
    if a <= 0:
        return
    for k in range(12):
        g = math.radians(k * 30 + giro)
        M.line(c, cx + math.cos(g) * r * 1.25, cy + math.sin(g) * r * 1.25, cx + math.cos(g) * r * 1.6, cy + math.sin(g) * r * 1.6, "#FFB300", a, 7)
    E.bola(c, cx, cy, r, "#FFB300", a)


def setas_espectro(c, t, tf, tl, x0, x1, y, size=48, escuro=False):
    """frequência crescendo para a direita (laranja) e lambda crescendo para a esquerda (tinta)"""
    tinta = BR if escuro else TINTA
    q = ease_io(prog(t, tf, 0.6))
    if q > 0:
        F.seta(c, x0, y, lerp(x0, x1, q), y, E.COR if not escuro else CLARO, 1.0, 7, 28)
        E.foco(c, t, tf + 0.3, 0.4, lambda a: E.escreve(c, "frequência maior", x1 - 420, y - 22, size, "b", E.COR if not escuro else CLARO, a))
    q = ease_io(prog(t, tl, 0.6))
    if q > 0:
        F.seta(c, x1, y + 80, lerp(x1, x0, q), y + 80, tinta, 1.0, 7, 28)
        E.foco(c, t, tl + 0.3, 0.4, lambda a: E.formula(c, "λ maior", x0 + 30, y + 58, size, "b", tinta, a))


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
        E.foco(c, t, C[k] + 0.6, 0.5, lambda a, i=i, y=y: desenhos[i](a, x + w - 170, y + 115))
    q1 = ease_io(prog(t, C[itens[1][0]] - 0.35, 0.5))
    E.cursor(c, x + w - 30, lerp(430, 720, q1), ep(t, C[itens[0][0]], 0.4))
    E.frase(c, t, lerp(C[itens[1][0]], C[cena + ".end"], 0.6), ps("faltou alguma?", "i", 56, COR) + ps("procure no canal", "i", 56), 820, 920, "left", 0.12)


# ---------------- ícones desta aula ----------------
def torre(c, cx, cy, s, a=1.0, t=0.0):
    """torre de transmissão com ondas saindo do alto; (cx, cy) = pé"""
    if a <= 0:
        return
    top = (cx, cy - s * 2)
    for dx in (-1, 1):
        M.line(c, cx + dx * s * 0.55, cy, top[0], top[1], TINTA, a, 7)
    for k in range(1, 4):
        y = cy - s * 0.5 * k
        w = s * 0.55 * (1 - k / 4)
        M.line(c, cx - w, y, cx + w, y, TINTA, a, 4)
    for k in range(3):
        r = s * (0.35 + 0.3 * k + 0.1 * ((t * 1.5) % 1))
        E.arco(c, top[0], top[1], r, -60, 120, E.COR, 6, a * (1 - k / 3.5))
        E.arco(c, top[0], top[1], r, 120, 120, E.COR, 6, a * (1 - k / 3.5))


def tv(c, cx, cy, s, a=1.0):
    if a <= 0:
        return
    M.rrect(c, cx - s, cy - s * 0.65, 2 * s, s * 1.3, s * 0.12, TINTA, a)
    M.rrect(c, cx - s * 0.88, cy - s * 0.53, s * 1.76, s * 1.06, s * 0.06, E.mix(E.COR, "#FFFFFF", 0.55), a)
    M.line(c, cx - s * 0.4, cy + s * 0.9, cx + s * 0.4, cy + s * 0.9, TINTA, a, 8)
    M.line(c, cx, cy + s * 0.65, cx, cy + s * 0.9, TINTA, a, 8)


def celular(c, cx, cy, s, a=1.0):
    if a <= 0:
        return
    M.rrect(c, cx - s * 0.55, cy - s, s * 1.1, s * 2, s * 0.16, TINTA, a)
    M.rrect(c, cx - s * 0.46, cy - s * 0.85, s * 0.92, s * 1.62, s * 0.08, E.mix(E.COR, "#FFFFFF", 0.6), a)
    c.drawCircle(cx, cy + s * 0.88, s * 0.06, M.paint(BR, a))


def wifi(c, cx, cy, s, a=1.0):
    if a <= 0:
        return
    for k in range(3):
        E.arco(c, cx, cy, s * (0.4 + 0.33 * k), -135, 90, E.COR, max(5, s * 0.12), a)
    c.drawCircle(cx, cy, s * 0.12, M.paint(E.COR, a))


def radar(c, cx, cy, s, a=1.0):
    if a <= 0:
        return
    M.line(c, cx, cy, cx, cy + s * 0.8, TINTA, a, 8)
    M.line(c, cx - s * 0.5, cy + s * 0.8, cx + s * 0.5, cy + s * 0.8, TINTA, a, 8)
    p = skia.Path()
    p.addArc(skia.Rect.MakeXYWH(cx - s, cy - s * 1.2, 2 * s, 2 * s), 20, 140)
    c.drawPath(p, M.paint(TINTA, a, stroke=10))
    M.line(c, cx, cy - s * 0.2, cx + s * 0.5, cy - s * 0.85, TINTA, a, 5)


def agua(c, cx, cy, s, ang=0.0, a=1.0):
    """molécula de água: oxigênio azul e dois hidrogênios brancos, girada ang graus"""
    if a <= 0:
        return
    c.save(); c.translate(cx, cy); c.rotate(ang)
    for g in (-52, 52):
        r = math.radians(g + 90)
        hx, hy = math.cos(r) * s * 0.75, math.sin(r) * s * 0.75
        M.line(c, 0, 0, hx, hy, TINTA2, a, 4)
        c.drawCircle(hx, hy, s * 0.32, M.paint("#FFFFFF", a))
        c.drawCircle(hx, hy, s * 0.32, M.paint(TINTA2, a, stroke=3))
    E.bola(c, 0, 0, s * 0.5, "#1E88E5", a)
    c.restore()


def controle(c, cx, cy, s, a=1.0, pisca=0.0):
    if a <= 0:
        return
    M.rrect(c, cx - s * 0.4, cy - s, s * 0.8, s * 2, s * 0.25, TINTA, a)
    c.drawCircle(cx, cy - s * 0.7, s * 0.1, M.paint("#3A3A44", a))
    for i in range(3):
        for j in range(4):
            c.drawCircle(cx - s * 0.2 + i * s * 0.2, cy - s * 0.2 + j * s * 0.25, s * 0.06, M.paint(BR, a * 0.8))
    if pisca > 0:
        g = skia.Paint(AntiAlias=True)
        g.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy - s * 0.7), s * 0.5, [M.hexc("#B04BFF", 0.8 * a * pisca), M.hexc("#B04BFF", 0)], [0, 1]))
        c.drawCircle(cx, cy - s * 0.7, s * 0.5, g)


def pessoa_termica(c, cx, cy, s, a=1.0):
    """silhueta numa imagem de câmera térmica: quente no meio, frio na borda"""
    if a <= 0:
        return
    M.rrect(c, cx - s * 1.1, cy - s * 1.5, s * 2.2, s * 3, s * 0.1, "#1A1446", a)
    for (x, y, r) in ((cx, cy - s * 0.85, s * 0.42), (cx, cy + s * 0.3, s * 0.75)):
        g = skia.Paint(AntiAlias=True)
        g.setShader(skia.GradientShader.MakeRadial(skia.Point(x, y), r, [M.hexc("#FFF176", a), M.hexc("#FF7043", a), M.hexc("#8E24AA", a)], [0, 0.55, 1]))
        if r > s * 0.5:
            c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x - r * 0.8, y - r, r * 1.6, r * 2.2), r * 0.5, r * 0.5), g)
        else:
            c.drawCircle(x, y, r, g)


def protetor(c, cx, cy, s, a=1.0):
    if a <= 0:
        return
    M.rrect(c, cx - s * 0.45, cy - s, s * 0.9, s * 1.8, s * 0.2, "#FFB300", a)
    M.rrect(c, cx - s * 0.3, cy + s * 0.75, s * 0.6, s * 0.35, s * 0.06, TINTA, a)
    E._meio(c, "FPS", cx, cy - s * 0.15, s * 0.3, "g", TINTA, a)


def microbio(c, cx, cy, s, a=1.0):
    if a <= 0:
        return
    for k in range(10):
        g = math.radians(k * 36)
        M.line(c, cx + math.cos(g) * s * 0.6, cy + math.sin(g) * s * 0.6, cx + math.cos(g) * s, cy + math.sin(g) * s, "#2FA84F", a, 6)
    E.bola(c, cx, cy, s * 0.65, "#2FA84F", a)


def nota(c, cx, cy, s, a=1.0, brilho=0.0):
    """nota de dinheiro; brilho > 0 acende o desenho escondido sob a luz negra"""
    if a <= 0:
        return
    M.rrect(c, cx - s * 1.4, cy - s * 0.65, s * 2.8, s * 1.3, s * 0.08, "#9CC9A0" if brilho < 0.5 else "#2B1F4A", a)
    c.drawCircle(cx + s * 0.7, cy, s * 0.38, M.paint(TINTA2, 0.4 * a, stroke=4))
    if brilho > 0:
        for k in range(4):
            M.line(c, cx - s * 1.1, cy - s * 0.35 + k * s * 0.22, cx - s * 0.1, cy - s * 0.35 + k * s * 0.22, "#B9FF4F", a * brilho, 6)
        c.drawCircle(cx + s * 0.7, cy, s * 0.3, M.paint("#B9FF4F", a * brilho, stroke=6))


def braco(c, cx, cy, s, a=1.0, osso=1.0):
    """braço deitado com o osso por dentro (osso = opacidade do osso)"""
    if a <= 0:
        return
    M.rrect(c, cx - s * 1.6, cy - s * 0.38, s * 3.2, s * 0.76, s * 0.38, "#E8B18C", a)
    if osso > 0:
        for dx in (-1, 1):
            for dy in (-1, 1):
                c.drawCircle(cx + dx * s * 1.2, cy + dy * s * 0.12, s * 0.15, M.paint("#FFFFFF", a * osso))
        M.rrect(c, cx - s * 1.2, cy - s * 0.1, s * 2.4, s * 0.2, s * 0.05, "#FFFFFF", a * osso)


def avental(c, cx, cy, s, a=1.0):
    if a <= 0:
        return
    p = skia.Path()
    p.moveTo(cx - s * 0.4, cy - s); p.lineTo(cx + s * 0.4, cy - s); p.lineTo(cx + s * 0.75, cy + s); p.lineTo(cx - s * 0.75, cy + s); p.close()
    c.drawPath(p, M.paint("#5A5F6B", a))
    E._meio(c, "Pb", cx, cy + s * 0.1, s * 0.4, "g", BR, a)


def nucleo(c, cx, cy, s, a=1.0):
    if a <= 0:
        return
    for k, (dx, dy) in enumerate(((0, 0), (0.5, 0.2), (-0.45, 0.25), (0.1, -0.5), (-0.3, -0.35), (0.4, -0.3), (-0.1, 0.5))):
        E.bola(c, cx + dx * s, cy + dy * s, s * 0.35, E.COR if k % 2 else F.NEG, a)


def topo(c, t, t0, i, rot=None):
    """faixa do espectro no alto, só com a região i acesa e o nome dela em cima"""
    xs = espectro(c, t, t0, 160, 90, h=56, rotulos=False, apaga=tuple(k for k in range(7) if k != i))
    xa, xb = xs[i]
    q = ep(t, t0 + 0.3, 0.4)
    if q > 0:
        c.drawRect(skia.Rect.MakeXYWH(xa - 3, 87, xb - xa + 6, 62), M.paint(E.COR, q, stroke=6))
    E.foco(c, t, t0 + 0.3, 0.4, lambda a: centro(c, rot or FAIXAS[i][0], (xa + xb) / 2, 210, 48, "g", COR, a))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def um():
        E.frase(c, t, C["s01.a"], [("celular", "g", 80), ("e", "i", 84), ("raio X", "g", 80, COR)], XE, 230, passo=0.15)
        E.frase(c, t, C["s01.a"] + 1.0, ps("ondas da mesma família", "i", 70), XE, 340, passo=0.1)
        E.foco(c, t, C["s01.b"], 0.5, lambda a: (raiox(c, 650, 640, 140, a), avental(c, 900, 680, 150, a)))
        E.frase(c, t, C["s01.b"] + 0.3, ps("avental de chumbo", "b", 54), 420, 930, passo=0.1)
        E.foco(c, t, C["s01.c"], 0.5, lambda a: celular(c, 1450, 640, 150, a))
        E.frase(c, t, C["s01.c"] + 0.3, [("nada?", "g", 70, COR)], 1450, 930, "center")
    E.saida(c, t, C["s02"] - 0.1, um)
    if t < C["s02"]:
        return
    tb = C["s02.a"] + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1520, 540, 300 * ease_back(prog(t, tb, 0.8)), giro=12 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 88), XE, 280, passo=0.14)
    E.frase(c, t, C["s02.a"] + 1.0, ps("cada faixa do espectro", "i", 70), XE, 400, passo=0.12)
    for i, (k, s) in enumerate((("s02.b", "o seu uso"), ("s02.c", "o seu risco"))):
        y = 580 + i * 170
        E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, XE + 40, y - 30, 38, a=a), centro(c, str(i + 1), XE + 40, y - 8, 48, "g", BR, a)))
        E.frase(c, t, C[k] + 0.1, [(s, "g", 90, ERRADO if i else COR)], XE + 110, y)


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    def ordem(a, x, y):
        espectro(c, 99, 0, x - 260, y - 30, w=360, h=60, rotulos=False, a=a)

    def ion(a, x, y):
        atomo(c, x - 30, y, 70, a, 0.6)
    lembrete2(c, t, C, "s03", (("s03.b", "a ordem do espectro,", "do rádio ao gama"), ("s03.c", "ionizante:", "arranca elétrons")), (ordem, ion))


# ---------------- rádio ----------------
def b_radio(c, t, C, b):
    topo(c, t, C["s04"], 0)
    E.frase(c, t, C["s04.a"], ps("as mais compridas:", "i", 66), XE, 380, passo=0.1)
    E.frase(c, t, C["s04.a"] + 0.9, ps("de metros a quilômetros", "g", 66, COR), XE, 480, passo=0.1)
    E.foco(c, t, C["s04.a"], 0.5, lambda a: torre(c, 1480, 640, 170, a, t))
    E.foco(c, t, C["s04.b"], 0.5, lambda a: (radio(c, 400, 720, 90, a), centro(c, "som do rádio", 400, 900, 52, "i", TINTA, a)))
    E.foco(c, t, C["s04.c"], 0.5, lambda a: (tv(c, 860, 720, 100, a), centro(c, "TV aberta", 860, 900, 52, "i", TINTA, a)))
    pilula(c, t, C["s04.d"], "não ionizam", 1480, 920, 60, CERTO)


# ---------------- micro-ondas ----------------
def b_micro(c, t, C, b):
    topo(c, t, C["s05"], 1)
    if t < C["s06"]:
        def s05():
            E.frase(c, t, C["s05.a"], ps("lambda de", "i", 66) + [("centímetros", "g", 66, COR)], XE, 380, passo=0.1)
            for i, (fn, nome) in enumerate(((celular, "celular"), (wifi, "wi-fi"), (radar, "radar"))):
                cx = 360 + i * 330
                y = 600 if i else 590
                E.foco(c, t, C["s05.b"] + 0.4 * i, 0.5, lambda a, fn=fn, cx=cx, y=y, nome=nome: (fn(c, cx, y, 90, a), centro(c, nome, cx, 780, 50, "i", TINTA, a)))
            E.foco(c, t, C["s05.c"], 0.5, lambda a: (forno(c, 1460, 600, 170, a), centro(c, "forno", 1460, 820, 56, "g", TINTA, a)))
            if t >= C["s05.d"]:  # as moléculas de água giram para lá e para cá
                q = ep(t, C["s05.d"], 0.5)
                for k, dx in enumerate((-180, -60, 60, 180)):
                    agua(c, 1460 + dx, 930 + (16 if k % 2 else -16), 46, 40 * math.sin(t * 12 + k), q)
            E.frase(c, t, C["s05.d"], [("a", "i", 56), ("água", "g", 56, "#1E88E5"), ("gira", "i", 56), ("e", "i", 56), ("esquenta", "g", 56, COR)], XE, 920, passo=0.12)
        E.saida(c, t, C["s06"] - 0.1, s05)
        return
    # s06: a grade da porta, não ioniza, desligou acabou
    def grade(a):
        x0, y0 = 300, 360
        M.rrect(c, x0, y0, 520, 360, 16, "#3A3A44", a)
        for i in range(14):
            for j in range(10):
                c.drawCircle(x0 + 30 + i * 35, y0 + 30 + j * 34, 9, M.paint("#A9A9B5", a))
    E.foco(c, t, C["s06.a"], 0.5, grade)
    F.onda(c, t, C["s06.a"] + 0.4, 880, 1720, 540, 60, 240, d=1.0, tl=C["s06.a"] + 1.2, rot_lambda="λ ≈ 12 cm")
    E.foco(c, t, C["s06.a"] + 2.0, 0.4, lambda a: centro(c, "furos de poucos milímetros", 560, 790, 50, "i", TINTA, a))
    pilula(c, t, C["s06.b"], "não ionizam", 560, 900, 56, CERTO)
    E.frase(c, t, C["s06.c"], [("desligou:", "i", 60), ("nada", "g", 60, COR), ("fica", "g", 60), ("na", "i", 60), ("comida", "i", 60)], 1300, 790, "center", 0.12)
    E.foco(c, t, C["s06.d"], 0.5, lambda a: (celular(c, 1220, 940, 60, a), E.escreve(c, "bem mais fracas", 1310, 960, 54, "b", TINTA2, a)))


# ---------------- infravermelho ----------------
def b_infra(c, t, C, b):
    topo(c, t, C["s07"], 2)
    E.foco(c, t, C["s07.a"], 0.5, lambda a: sol(c, 300, 450, 80, a, t * 8))
    E.frase(c, t, C["s07.a"] + 0.3, ps("a pele sente como", "i", 56), 450, 440, passo=0.1)
    E.frase(c, t, C["s07.a"] + 1.0, [("calor", "g", 66, COR)], 450, 520)
    E.foco(c, t, C["s07.b"], 0.5, lambda a: (pessoa_termica(c, 1000, 560, 150, a), centro(c, "câmera térmica", 1000, 840, 50, "i", TINTA, a)))
    pisca = 1.0 if (t * 3) % 1 < 0.5 else 0.2
    E.foco(c, t, C["s07.c"], 0.5, lambda a: (controle(c, 1500, 560, 150, a, pisca), centro(c, "controle remoto", 1500, 840, 50, "i", TINTA, a)))
    E.frase(c, t, C["s07.d"], ps("o olho não vê;", "i", 56) + ps("muitas câmeras de celular mostram", "b", 50, COR), W / 2, 980, "center", 0.08)


# ---------------- visível e ultravioleta ----------------
def b_ultra(c, t, C, b):
    if t < C["s08.b"]:
        topo(c, t, C["s08"], 3, "luz visível")
        E.frase(c, t, C["s08.a"], ps("a faixa que o olho percebe", "i", 70), XE, 420, passo=0.1)
        for i, s in enumerate(("lâmpadas", "telas", "laser")):
            E.foco(c, t, C["s08.a"] + 1.2 + 0.3 * i, 0.4, lambda a, i=i, s=s: E.pilula(c, s, 400 + i * 380, 600, 60, "g", fundo=TINTA, a=a))
        lampada(c, 1500, 640, 120, ep(t, C["s08.a"], 0.5))
        return
    topo(c, t, C["s08.b"] - 0.1, 4)
    if t < C["s09"]:
        def s08():
            E.foco(c, t, C["s08.b"], 0.5, lambda a: sol(c, 350, 500, 100, a, t * 8))
            for k in range(3):  # raios UV descendo até a pele
                x = 560 + k * 120
                F.vetor(c, t, C["s08.b"] + 0.3 + 0.15 * k, (x, 420), (x + 120, 720), None, None, "#8E24AA", 8)
            q = ep(t, C["s08.b"] + 0.4, 0.4)
            M.rrect(c, 520, 740, 600, 60, 20, "#E8B18C", q) if q > 0 else None
            E.foco(c, t, C["s08.b"] + 0.6, 0.4, lambda a: centro(c, "pele", 820, 860, 50, "i", TINTA, a))
            pilula(c, t, C["s08.c"], "queima · câncer de pele", 1420, 420, 56, ERRADO)
            E.foco(c, t, C["s08.d"], 0.5, lambda a: protetor(c, 1420, 680, 130, a))
            E.frase(c, t, C["s08.d"] + 0.4, ps("barra ou absorve o UV", "b", 50, TINTA), 1420, 940, "center", 0.1)
        E.saida(c, t, C["s09"] - 0.1, s08)
        return
    E.foco(c, t, C["s09.a"], 0.5, lambda a: microbio(c, 400, 480, 110, a))
    if t >= C["s09.a"] + 0.6:
        E.risco(c, 270, 610, 530, 350, t, C["s09.a"] + 0.6, largura=12)
    E.frase(c, t, C["s09.a"], [("mata", "g", 64, COR), ("micróbios", "i", 66)], 230, 720, passo=0.12)
    E.foco(c, t, C["s09.b"], 0.5, lambda a: (M.rrect(c, 820, 440, 360, 70, 35, "#B04BFF", a), centro(c, "lâmpada UV", 1000, 600, 54, "i", TINTA, a)))
    E.frase(c, t, C["s09.b"] + 0.5, ps("água e material de hospital", "b", 46, TINTA2), 1000, 680, "center", 0.08)
    brilho = ep(t, C["s09.c"] + 0.6, 0.6)
    E.foco(c, t, C["s09.c"], 0.5, lambda a: nota(c, 1560, 480, 140, a, brilho))
    E.frase(c, t, C["s09.c"] + 0.5, ps("nota sob a", "i", 56) + [("luz negra", "g", 56, "#8E24AA")], 1560, 780, "center", 0.1)


# ---------------- raios X e gama ----------------
def b_xgama(c, t, C, b):
    if t < C["s11"]:
        topo(c, t, C["s10"], 5)

        def s10():
            osso = 0.15 + 0.85 * ep(t, C["s10.b"], 0.5)
            E.foco(c, t, C["s10.a"], 0.5, lambda a: braco(c, 650, 560, 160, a, osso))
            for k in range(5):  # raios X atravessam
                x = 450 + k * 100
                F.vetor(c, t, C["s10.a"] + 0.3 + 0.1 * k, (x, 330), (x, 470), None, None, "#3949AB", 7)
            E.frase(c, t, C["s10.a"], ps("atravessam pele e músculo", "i", 54), 250, 760, passo=0.08)
            E.frase(c, t, C["s10.b"], [("o", "i", 56), ("osso", "g", 56, COR), ("barra:", "i", 56), ("cálcio,", "b", 50), ("mais", "i", 56), ("prótons", "b", 50)], 250, 850, passo=0.1)
            E.foco(c, t, C["s10.c"], 0.5, lambda a: (raiox(c, 1240, 560, 170, a), centro(c, "o osso fica claro", 1240, 830, 48, "i", TINTA, a)))
            pilula(c, t, C["s10.d"], "IONIZANTE", 1620, 380, 54, ERRADO)
            E.foco(c, t, C["s10.d"] + 0.8, 0.4, lambda a: centro(c, "dose pequena", 1620, 480, 44, "b", TINTA2, a))
            E.foco(c, t, C["s10.e"], 0.5, lambda a: avental(c, 1620, 680, 140, a))
            E.foco(c, t, C["s10.e"] + 0.3, 0.4, lambda a: centro(c, "avental de chumbo", 1620, 870, 44, "b", TINTA, a))
        E.saida(c, t, C["s11"] - 0.1, s10)
        return
    topo(c, t, C["s11"], 6)
    E.foco(c, t, C["s11.a"], 0.5, lambda a: nucleo(c, 360, 520, 110, a))
    F.onda(c, t, C["s11.a"] + 0.5, 500, 900, 520, 26, 30, d=0.8, eixo=False)
    E.foco(c, t, C["s11.a"] + 0.6, 0.4, lambda a: E._meio(c, "γ", 700, 440, 70, "g", COR, a))
    E.frase(c, t, C["s11.a"], ps("do núcleo do átomo", "i", 54), 230, 760, passo=0.1)
    pilula(c, t, C["s11.a"] + 2.5, "os mais ionizantes", 520, 880, 54, ERRADO)
    E.foco(c, t, C["s11.b"], 0.5, lambda a: (E.pilula(c, "radioterapia", 1400, 420, 60, "g", fundo=E.COR, a=a), E.escreve(c, "destrói células do câncer", 1130, 520, 50, "i", TINTA, a)))
    E.foco(c, t, C["s11.c"], 0.5, lambda a: (E.pilula(c, "esteriliza", 1400, 680, 60, "g", fundo=TINTA, a=a), E.escreve(c, "alimentos e material de hospital", 1060, 780, 48, "i", TINTA, a)))
    E.frase(c, t, C["s11.c"] + 1.4, [("nada", "g", 56, CERTO), ("fica", "g", 56, CERTO), ("radioativo", "g", 56, CERTO)], 1400, 900, "center", 0.12)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s12"], [("cuidado", "g", 96, ERRADO)], XE, 190)
    E.frase(c, t, C["s12.a"], ps("toda radiação é", "i", 70) + [("perigosa", "g", 70, ERRADO), ("do", "i", 70), ("mesmo", "i", 70), ("jeito?", "i", 70)], XE, 320, passo=0.1)
    if t >= C["s12.a"] + 2.2:
        E.risco(c, XE + 540, 330, XE + 1260, 260, t, C["s12.a"] + 2.2, largura=10)
    xs = espectro(c, t, C["s12.b"], 160, 540, h=80, rotulos=True, size=38)
    E.foco(c, t, C["s12.b"] + 0.8, 0.4, lambda a: centro(c, "radiação: todas, do rádio ao gama", W / 2, 450, 48, "b", TINTA2, a))
    xu = (xs[4][0] + xs[4][1]) / 2
    q = ep(t, C["s12.c"], 0.5)
    if q > 0:
        E.chave(c, xu, 1755, 790, ERRADO, q, 26, 6)
        E.foco(c, t, C["s12.c"] + 0.3, 0.4, lambda a: centro(c, "danificam as células", (xu + 1755) / 2, 880, 54, "g", ERRADO, a))
    E.foco(c, t, C["s12.d"], 0.5, lambda a: (forno(c, 330, 940, 70, a), celular(c, 520, 940, 60, a)))
    E.frase(c, t, C["s12.d"] + 0.4, [("micro-ondas:", "b", 54), ("não", "g", 58, CERTO), ("ionizam", "g", 58, CERTO)], 620, 965)


# ---------------- atalho (palco) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    E.frase(c, t, C["s13"], ps("agora, o atalho", "i", 76, CLARO), W / 2, 150, "center")
    xs = espectro(c, t, C["s13.a"], 160, 300, h=90, rotulos=True, size=38, escuro=True)
    xv0, xv1 = xs[3]
    q = ep(t, C["s13.a"] + 0.6, 0.5)
    if q > 0:
        M.line(c, (xv0 + xv1) / 2, 300, (xv0 + xv1) / 2, 860, BR, q, 4, dash=E.TRACO)
        E.foco(c, t, C["s13.a"] + 0.8, 0.4, lambda a: centro(c, "luz visível no meio", (xv0 + xv1) / 2, 560, 46, "b", BR, a))
    E.frase(c, t, C["s13.b"], [("abaixo:", "i", 60, CLARO)], 200, 640)
    E.frase(c, t, C["s13.b"] + 1.5, [("comunicam", "g", 64, BR), ("e", "i", 64, CLARO), ("aquecem", "g", 64, BR)], 200, 730, passo=0.15)
    E.frase(c, t, C["s13.c"], [("acima:", "i", 60, CLARO)], 1060, 640)
    E.frase(c, t, C["s13.c"] + 1.5, [("esterilizam,", "g", 54, BR), ("atravessam,", "g", 54, BR)], 1060, 730, passo=0.15)
    E.frase(c, t, C["s13.c"] + 2.0, [("ionizam", "g", 64, ERRADO)], 1060, 810)
    E.frase(c, t, C["s13.d"], [("cuidado:", "g", 52, CLARO)] + ps("o UV fraco não ioniza, mas queima", "i", 54, BR), W / 2, 980, "center", 0.08)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s14"], ps("hora de testar", "i", 72, COR), XE, 180)
    E.frase(c, t, C["s14"] + 1.4, ps("qual radiação?", "g", 64), XE, 280, passo=0.1)
    itens = (("s14.a", "controle remoto"), ("s14.b", "radiografia do braço"), ("s14.c", "protetor solar"), ("s14.d", "forno da pizza"))
    for i, (k, s) in enumerate(itens):
        y = 430 + i * 130
        E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, XE + 40, y - 26, 38, a=a), centro(c, str(i + 1), XE + 40, y - 4, 48, "g", BR, a)))
        E.frase(c, t, C[k] + 0.1, [(s, "g", 64)], XE + 110, y)
    E.frase(c, t, C["s14.e"], ps("qual delas", "i", 66) + [("ioniza?", "g", 66, ERRADO)], XE, 990, passo=0.12)
    if t >= C["s15"]:
        E.relogio(c, t, C["s15.a"], cx=1460, cy=440, r=200)
    else:
        for i, (k, fn, cx, cy, s_) in enumerate((("s14.a", controle, 1250, 420, 110), ("s14.b", raiox, 1600, 420, 120),
                                                  ("s14.c", protetor, 1250, 800, 110), ("s14.d", forno, 1600, 800, 100))):
            E.foco(c, t, C[k], 0.5, lambda a, fn=fn, cx=cx, cy=cy, s_=s_: fn(c, cx, cy, s_, a))
            E.foco(c, t, C[k], 0.5, lambda a, i=i, cx=cx, cy=cy: (E.bola(c, cx - 150, cy - 110, 32, a=a), centro(c, str(i + 1), cx - 150, cy - 92, 40, "g", BR, a)))


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    itens = (("s16.a", "controle remoto", "infravermelho", controle), ("s16.b", "radiografia", "raios X", raiox),
             ("s16.c", "protetor solar", "ultravioleta", protetor), ("s16.d", "forno", "micro-ondas", forno))
    for i, (k, s, r, fn) in enumerate(itens):
        y = 250 + i * 160
        E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, XE + 40, y - 26, 38, a=a), centro(c, str(i + 1), XE + 40, y - 4, 48, "g", BR, a)))
        E.frase(c, t, C[k], [(s, "i", 60)], XE + 110, y)
        E.foco(c, t, C[k] + 0.5, 0.4, lambda a, r=r, y=y: (E.escreve(c, "→", 760, y, 60, "g", TINTA2, a), E.escreve(c, r, 860, y, 64, "g", COR, a)))
    pilula(c, t, C["s16.e"], "IONIZA: só o raio X", 1500, 400, 58, ERRADO)
    E.frase(c, t, C["s16.e"] + 1.4, ps("UV que chega à pele:", "i", 50), 1500, 540, "center", 0.08)
    E.frase(c, t, C["s16.e"] + 2.2, [("não", "g", 50, CERTO), ("ioniza,", "g", 50, CERTO), ("mas", "i", 54), ("queima", "g", 50, ERRADO)], 1500, 620, "center", 0.1)
    E.frase(c, t, C["s16.f"], [("controle", "b", 50), ("e", "i", 54), ("forno:", "b", 50), ("não", "g", 50, CERTO), ("ionizam", "g", 50, CERTO)], 1500, 900, "center", 0.1)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s17"], [("resumindo", "i", 92, COR)], W / 2, 170, "center")
        itens = (("s17.a", "rádio e micro-ondas:", "comunicam"), ("s17.b", "infravermelho:", "calor e controle"),
                 ("s17.c", "ultravioleta:", "queima e esteriliza"), ("s17.d", "raios X e gama:", "atravessam e ionizam"))
        for i, (k, s1, s2) in enumerate(itens):
            y = 340 + i * 170
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 300, y - 26, 52, a=a), centro(c, str(i + 1), 300, y - 4, 60, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, [(s1, "g", 64)], 400, y)
            E.frase(c, t, C[k] + 0.5, ps(s2, "i", 66, ERRADO if i == 3 else COR), 1100, y, passo=0.1)
    E.saida(c, t, C["s18"] - 0.1, resumo)
    if t < C["s18"]:
        return
    E.frase(c, t, C["s18"], [("próxima", "i", 80), ("aula:", "i", 80), ("praticando", "g", 84, COR)], XE, 250, passo=0.15)
    E.frase(c, t, C["s18.a"], ps("reconhecer a radiação", "g", 70), XE, 430, passo=0.12)
    E.formula_em(c, t, C["s18.b"], "calcular f e λ: c = λ · f", XE, 560, 70, "g", COR)
    espectro(c, t, C["s18.a"] + 0.3, 160, 680, w=1300, h=70, rotulos=True, size=36)
    E.foco(c, t, C["s18.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 420, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s18.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(720, 445, p), ep(t, C["s18.c"] + 0.2, 0.4))
    E.frase(c, t, C["s18.d"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1570, 990, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, radio=b_radio, micro=b_micro, infra=b_infra, ultra=b_ultra, xgama=b_xgama,
              erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
