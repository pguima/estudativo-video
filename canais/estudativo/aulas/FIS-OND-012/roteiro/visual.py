"""Visual — Estudativo · FIS-OND-012: praticando o espectro eletromagnético (prática, modelo da FIS-CIN-010).

Linguagem visual: a da trilha Ondas e Som, escrita na docstring do visual.py da FIS-OND-001 (que segue a da Física,
FIS-CIN-001). Um bloco por questão (q1..q5): enunciado à esquerda, ilustração à direita até o relógio de pausa,
resposta em conta de pilha com o resultado na esfera. espectro(), chirp() e os ícones vêm das FIS-OND-010 e 011.
Todo instante vem de C[...]."""
import math

import editorial as E
import fisica as F
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Física", "Ondas e Som")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_FIS-OND-012_praticando_espectro_eletromagnetico.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("metodo", "q1", "q2", "q3", "q4", "q5", "fim"))
BR = "#FFFFFF"

# todas as contas da aula: c = λ·f, c = 3 × 10^8 m/s
assert abs(3e8 / 2.4e9 - 0.125) < 1e-12 and abs(3 / 2.4 - 1.25) < 1e-12 and 8 - 9 == -1    # wi-fi: 12,5 cm
assert abs(500e-9 - 5e-7) < 1e-20 and abs(3 / 5 - 0.6) < 1e-12 and 8 + 7 == 15
assert abs(3e8 / 5e-7 - 6e14) < 1e3 and abs(0.6e15 - 6e14) < 1e3                         # verde: 6 × 10^14 Hz
assert abs(3 / 7.5 - 0.4) < 1e-12 and 8 - 14 == -6 and abs(3e8 / 7.5e14 - 4e-7) < 1e-18   # laser: 400 nm
assert abs(4e-7 / 1e-9 - 400) < 1e-6 and 400 <= 400 <= 700                                # na ponta violeta do visível


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




# ---------------- peças da prática ----------------
def enunciado(c, t, C, cena, num, linhas, x=XE):
    """cabeçalho "questão N" e as linhas do enunciado: linhas = [(cue, partes, y)]"""
    E.frase(c, t, C[cena], [("questão", "i", 70, COR), (str(num), "g", 76, COR)], x, 190, passo=0.15)
    for k, partes, y in linhas:
        E.frase(c, t, C[k], partes, x, y, passo=0.1)


def pausa(c, t, t0, aberto=None):
    """relógio de pausa à direita; antes dele, aberto() desenha a ilustração"""
    if t >= t0:
        E.relogio(c, t, t0, cx=1500, cy=440, r=190)
    elif aberto:
        aberto()


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    E.frase(c, t, C["s01"], ps("questão de espectro pede", "i", 76), XE, 220, passo=0.12)
    E.frase(c, t, C["s01.a"], [("uma", "i", 80), ("de", "i", 80), ("duas", "g", 84, COR), ("coisas", "i", 80)], XE, 330, passo=0.12)
    E.foco(c, t, C["s01.b"], 0.5, lambda a: (E.bola(c, XE + 40, 470, 38, a=a), centro(c, "1", XE + 40, 492, 48, "g", BR, a)))
    E.frase(c, t, C["s01.b"] + 0.1, ps("o nome da radiação", "g", 70), XE + 110, 500, passo=0.1)
    espectro(c, t, C["s01.b"] + 0.6, 160, 580, h=70, rotulos=False)
    E.foco(c, t, C["s01.c"], 0.5, lambda a: (E.bola(c, XE + 40, 750, 38, a=a), centro(c, "2", XE + 40, 772, 48, "g", BR, a)))
    E.formula_em(c, t, C["s01.c"] + 0.1, "a conta: c = λ · f", XE + 110, 780, 70, "g", TINTA)
    E.frase(c, t, C["s01.d"], [("5", "g", 90, COR), ("questões", "g", 76), ("dos", "i", 80), ("dois", "i", 80), ("tipos", "i", 80)], XE, 960, passo=0.12)


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s02"], ps("você vai usar", "i", 84), XE, 240, passo=0.12)
    espectro(c, t, C["s02.a"], 160, 380, h=90, rotulos=True, size=38)
    E.foco(c, t, C["s02.a"] + 1.6, 0.5, lambda a: (E.formula(c, "c = 3 × 10^{8}", XE, 720, 90, "g", COR, a),
                                                   E.formula(c, "m/s", XE + E.formula(None, "c = 3 × 10^{8}", 0, 0, 90, a=0) + 24, 720, 66, "b", F.UNID, a)))
    E.frase(c, t, C["s02.b"], [("e", "i", 70), ("o", "i", 70), ("uso", "g", 70, COR), ("e", "i", 70), ("o", "i", 70), ("risco", "g", 70, ERRADO),
                               ("de", "i", 70), ("cada", "i", 70), ("faixa", "i", 70)], XE, 860, passo=0.1)
    E.frase(c, t, lerp(C["s02.b"], C["s02.end"], 0.6), ps("faltou alguma?", "i", 56, COR) + ps("procure no canal", "i", 56), XE, 980, "left", 0.12)


# ---------------- método ----------------
def b_metodo(c, t, C, b):
    E.frase(c, t, C["s03"], [("o", "i", 76), ("método:", "g", 76, COR)] + ps("procure a pista", "i", 76), XE, 180, passo=0.12)
    linhas = (("s03.b", "comunicação ou forno", "rádio · micro-ondas"), ("s03.c", "calor ou controle remoto", "infravermelho"),
              ("s03.d", "pele queimada ou esteriliza", "ultravioleta"), ("s03.e", "atravessa o corpo", "raios X"),
              ("s03.f", "núcleo do átomo · cobalto", "gama"))
    for i, (k, pista, rad) in enumerate(linhas):
        y = 330 + i * 120
        E.frase(c, t, C[k], ps(pista, "i", 58), XE, y, passo=0.08)
        E.foco(c, t, C[k] + 0.6, 0.4, lambda a, y=y: E.escreve(c, "→", 1000, y, 60, "g", TINTA2, a))
        E.foco(c, t, C[k] + 0.8, 0.4, lambda a, y=y, rad=rad: E.escreve(c, rad, 1100, y, 64, "g", COR, a))
    E.foco(c, t, C["s03.g"], 0.5, lambda a: E.pilula(c, "na conta: divida c pelo dado", W / 2, 990, 56, "g", fundo=TINTA, a=a))


# ---------------- questão 1: wi-fi ----------------
def b_q1(c, t, C, b):
    if t < C["s05"]:
        enunciado(c, t, C, "s04", 1, (("s04.a", ps("roteador de wi-fi:", "i", 70), 360),))
        E.foco(c, t, C["s04.a"] + 0.8, 0.5, lambda a: (E.formula(c, "f = 2,4", XE, 500, 96, "g", COR, a), E.formula(c, "GHz", XE + E.formula(None, "f = 2,4", 0, 0, 96, a=0) + 22, 500, 70, "b", F.UNID, a)))
        E.foco(c, t, C["s04.a"] + 2.2, 0.4, lambda a: E.escreve(c, "giga = 1 bilhão", XE, 590, 54, "b", TINTA2, a))
        E.frase(c, t, C["s04.b"], [("λ", "g", 80, COR), ("=", "g", 80, TINTA2), ("?", "g", 80, COR)], XE, 760, passo=0.15)
        pausa(c, t, C["s04.c"], lambda: E.foco(c, t, C["s04.a"], 0.5, lambda a: wifi(c, 1500, 560, 180, a)))
        return
    conta(c, t, [(C["s05.a"], "f = 2,4 × 10^{9} Hz"), (C["s05.b"], "3 ÷ 2,4 = 1,25"), (C["s05.c"], "10^{8} ÷ 10^{9} = 10^{−1}")], XE, 260, 170, 86)
    E.foco(c, t, C["s05.c"] + 1.4, 0.4, lambda a: E.formula(c, "λ = 1,25 × 10^{−1} m = 0,125 m", XE, 790, 66, "b", TINTA2, a))
    bola_txt(c, t, C["s05.d"], "12,5 cm", 1520, 440, 170, 80)
    pilula(c, t, C["s05.e"], "micro-ondas", 1520, 720, 64, E.COR)


# ---------------- questão 2: luz verde ----------------
def b_q2(c, t, C, b):
    if t < C["s07"]:
        enunciado(c, t, C, "s06", 2, (("s06.a", ps("luz verde:", "i", 70) + [("λ = 500 nm", "g", 70, "#43A047")], 360),))
        E.foco(c, t, C["s06.b"], 0.5, lambda a: E.formula(c, "= 5 × 10^{−7} m", XE + 300, 490, 80, "g", TINTA, a))
        E.foco(c, t, C["s06.b"] - 0.6, 0.4, lambda a: E.escreve(c, "nano = 1 bilionésimo", XE, 590, 50, "b", TINTA2, a))
        E.frase(c, t, C["s06.c"], [("f", "g", 80, COR), ("=", "g", 80, TINTA2), ("?", "g", 80, COR)], XE, 760, passo=0.15)
        pausa(c, t, C["s06.d"], lambda: F.onda(c, t, C["s06.a"], 1150, 1800, 560, 60, 110, cor="#43A047", d=1.0))
        return
    conta(c, t, [(C["s07.a"], "f = f{3 × 10^{8}}{5 × 10^{−7}}"), (C["s07.a"] + 0.9, "3 ÷ 5 = 0,6"), (C["s07.b"], "10^{8} ÷ 10^{−7} = 10^{8 + 7} = 10^{15}"),
                 (C["s07.c"], "f = 0,6 × 10^{15} Hz")], XE, 220, 165, 76)
    bola_formula(c, t, C["s07.d"], "6 × 10^{14}", 1560, 470, 180, 62)
    E.foco(c, t, C["s07.d"] + 0.3, 0.4, lambda a: centro(c, "Hz", 1560, 720, 64, "b", F.UNID, a))
    E.frase(c, t, C["s07.d"] + 2.0, ps("a vírgula anda uma casa,", "i", 52) + ps("o expoente perde um", "i", 52), 1240, 980, "center", 0.08)


# ---------------- questão 3: qual radiação ----------------
def b_q3(c, t, C, b):
    sit = (("s08.a", "câmera do calor do corpo", pessoa_termica, 110), ("s08.b", "lâmpada que mata bactérias", None, 0),
           ("s08.c", "fonte de cobalto · radioterapia", nucleo, 80))
    respostas = (("s09.a", "infravermelho"), ("s09.b", "ultravioleta"), ("s09.c", "raios gama"))
    if t < C["s09"]:
        E.frase(c, t, C["s08"], [("questão", "i", 70, COR), ("3", "g", 76, COR)], XE, 190, passo=0.15)
        E.frase(c, t, C["s08"] + 1.0, ps("qual radiação?", "g", 64), XE, 290, passo=0.1)
    for i, (k, s, fn, sz) in enumerate(sit):
        y = 440 + i * 200 if t < C["s09"] else 280 + i * 220
        E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, XE + 40, y - 26, 38, a=a), centro(c, str(i + 1), XE + 40, y - 4, 48, "g", BR, a)))
        E.frase(c, t, C[k] + 0.1, ps(s, "g", 58), XE + 110, y, passo=0.08)
    if t < C["s09"]:
        def ilus():
            E.foco(c, t, C["s08.a"], 0.5, lambda a: pessoa_termica(c, 1300, 520, 110, a))
            E.foco(c, t, C["s08.b"], 0.5, lambda a: M.rrect(c, 1530, 470, 300, 60, 30, "#B04BFF", a))
            E.foco(c, t, C["s08.c"], 0.5, lambda a: nucleo(c, 1680, 760, 90, a))
        pausa(c, t, C["s08.d"], ilus)
        return
    for i, (k, r) in enumerate(respostas):
        y = 280 + i * 220
        E.foco(c, t, C[k], 0.4, lambda a, y=y, r=r: (E.escreve(c, "→", 1210, y, 64, "g", TINTA2, a), E.escreve(c, r, 1310, y, 68, "g", COR, a)))
    pilula(c, t, C["s09.d"], "não ioniza", 1520, 360, 46, CERTO, "b")
    pilula(c, t, C["s09.d"] + 1.0, "ioniza", 1440, 800, 46, ERRADO, "b")


# ---------------- questão 4: micro-ondas × raios X ----------------
def b_q4(c, t, C, b):
    E.frase(c, t, C["s10"], [("questão", "i", 70, COR), ("4", "g", 76, COR)], XE, 190, passo=0.15)
    E.frase(c, t, C["s10.a"], ps("no vácuo:", "i", 64), XE, 300, passo=0.1)
    cols = (900, 1450)
    if t < C["s11"]:  # antes da resposta: as duas ondas, lado a lado
        E.frase(c, t, C["s10.a"] + 0.4, [("micro-ondas", "g", 60), ("e", "i", 64), ("raios X", "g", 60, COR)], XE + 330, 300, passo=0.15)
    else:
        E.foco(c, t, C["s11"], 0.5, lambda a: (centro(c, "micro-ondas", cols[0], 420, 60, "g", TINTA, a), centro(c, "raios X", cols[1], 420, 60, "g", TINTA, a)))
        M.line(c, XE, 450, 1750, 450, TINTA2, ep(t, C["s11"], 0.4), 3)
    linhas = (("s10.b", "velocidade", "s11.a", ("=", "=")), ("s10.c", "frequência", "s11.b", ("menor", "MAIOR")), ("s10.d", "lambda", "s11.c", ("MAIOR", "menor")))
    for i, (kq, nome, kr, (r0, r1)) in enumerate(linhas):
        y = 580 + i * 150
        E.frase(c, t, C[kq], [(nome, "i", 66), ("?", "g", 66, COR)], XE, y, passo=0.1)
        if kr in C and t >= C[kr]:
            for x, r in zip(cols, (r0, r1)):
                cor = CERTO if r == "=" else (COR if r.isupper() else TINTA2)
                E.foco(c, t, C[kr], 0.4, lambda a, x=x, r=r, cor=cor, y=y: centro(c, "a mesma: c" if r == "=" else r.lower(), x, y, 62, "g", cor, a))
    if t < C["s11"]:
        def ilus():
            for i, (nome, lam, A_, cor) in enumerate((("micro-ondas", 260, 60, F.NEG), ("raios X", 22, 24, E.COR))):
                y = 470 + i * 260
                F.onda(c, t, C["s10.a"] + 0.6 + 0.4 * i, 1000, 1780, y, A_, lam, cor=cor, d=1.0)
                E.foco(c, t, C["s10.a"] + 0.6 + 0.4 * i, 0.4, lambda a, nome=nome, y=y: E.escreve(c, nome, 1000, y - 90, 50, "b", TINTA2, a))
        pausa(c, t, C["s10.e"], ilus)
    else:
        E.frase(c, t, C["s11.d"], [("raio X", "g", 56), ("mais", "i", 60), ("rápido?", "g", 56, ERRADO), ("pegadinha", "i", 60, ERRADO)], W / 2, 1010, "center", 0.12)


# ---------------- questão 5: o laser ----------------
def b_q5(c, t, C, b):
    if t < C["s13"]:
        enunciado(c, t, C, "s12", 5, (("s12.a", ps("um laser:", "i", 70), 360),))
        E.foco(c, t, C["s12.a"] + 0.6, 0.5, lambda a: E.formula(c, "f = 7,5 × 10^{14} Hz", XE, 500, 90, "g", COR, a))
        E.frase(c, t, C["s12.b"], [("λ", "g", 76, COR), ("em", "i", 76), ("nm?", "g", 76, COR)], XE, 680, passo=0.12)
        E.frase(c, t, C["s12.c"], [("é", "i", 76), ("visível?", "g", 76)], XE, 800, passo=0.12)
        pausa(c, t, C["s12.d"], lambda: E.foco(c, t, C["s12.a"], 0.5, lambda a: (M.rrect(c, 1250, 520, 260, 90, 20, TINTA, a),
                                                                               M.line(c, 1510, 565, 1850, 565, "#7C4DFF", a, 10))))
        return
    conta(c, t, [(C["s13.a"], "3 ÷ 7,5 = 0,4"), (C["s13.b"], "10^{8} ÷ 10^{14} = 10^{8 − 14} = 10^{−6}"),
                 (C["s13.c"], "λ = 0,4 × 10^{−6} = 4 × 10^{−7} m")], XE, 230, 160, 74)
    bola_txt(c, t, C["s13.d"], "400 nm", 1560, 330, 150, 70)
    X0, X1, Y = 260, 1660, 760
    q = ep(t, C["s13.e"], 0.5)
    if q > 0:
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeLinear([skia.Point(X0, 0), skia.Point(X1, 0)], [M.hexc(cc, q) for cc in ARCO_IRIS]))
        c.drawRect(skia.Rect.MakeXYWH(X0, Y, X1 - X0, 90), p)
        c.drawRect(skia.Rect.MakeXYWH(X1, Y, 140, 90), M.paint(E.mix(E.COR, "#FFFFFF", 0.5), q))
        E.foco(c, t, C["s13.e"] + 0.3, 0.4, lambda a: (centro(c, "700 nm", X0, Y + 150, 46, "b", TINTA2, a), centro(c, "400 nm", X1, Y + 150, 52, "g", COR, a),
                                                     centro(c, "UV", X1 + 70, Y + 60, 44, "g", TINTA, a)))
        F.seta(c, X1, Y - 110, X1, Y - 10, COR, q, 8)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    if t < C["s14.c"]:
        E.frase(c, t, C["s14"], [("resumindo", "i", 92, COR)], W / 2, 200, "center")
        for i, (k, s1, s2) in enumerate((("s14.a", "reconhecer:", "a pista do uso"), ("s14.b", "calcular:", "c ÷ o dado, cuidado nos expoentes"))):
            y = 420 + i * 200
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 300, y - 26, 52, a=a), centro(c, str(i + 1), 300, y - 4, 60, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, [(s1, "g", 70)], 400, y)
            E.frase(c, t, C[k] + 0.5, ps(s2, "i", 62, COR), 400, y + 90, passo=0.08)
        return
    tb = C["s14.c"] + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1500, 420, 260 * ease_back(prog(t, tb, 0.8)), giro=12 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, C["s14.c"], ps("você fechou a trilha", "i", 80), XE, 280, passo=0.12)
    E.frase(c, t, C["s14.c"] + 1.0, [("Ondas", "g", 110, COR), ("e", "i", 100), ("Som", "g", 110, COR)], XE, 420, passo=0.15)
    E.frase(c, t, C["s14.c"] + 2.0, ps("do pêndulo ao raio gama", "i", 66, TINTA2), XE, 530, passo=0.1)
    F.pendulo(c, t, C["s14.c"] + 2.0, 300, 600, 200, F.oscila(t, C["s14.c"] + 2.4, 20, 2.0), r=26)
    chirp(c, t, C["s14.c"] + 2.4, 420, 1100, 760, 40, l0=200, l1=14, d=1.2)
    E.foco(c, t, C["s14.d"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 820, 76, estilo="g", a=a))
    E.frase(c, t, C["s14.e"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1570, 1000, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, metodo=b_metodo, q1=b_q1, q2=b_q2, q3=b_q3, q4=b_q4, q5=b_q5, fim=b_fim)
