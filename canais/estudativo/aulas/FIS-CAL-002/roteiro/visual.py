"""Visual — Estudativo · FIS-CAL-002: dilatação térmica.
Segue a linguagem visual da trilha Calor e Termodinâmica (cabeçalho do visual.py da FIS-CAL-001: quente laranja, frio azul,
partículas que tremem, termômetro, fórmula com legenda, contas empilhadas e resultado na esfera) e a da Física (FIS-CIN-001).
Peças próprias: barra que cresce com o ΔL em laranja (barra_dl), trilho que entorta (trilho), lâmina bimetálica que curva
(lamina), lago com a camada de gelo (lago), chapa com furo que dilata (chapa_furo).
Todo instante vem de C[...] (marcadores do roteiro)."""
import math

import editorial as E
import fisica as F
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Física", "Calor e Termodinâmica")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_FIS-CAL-002_dilatacao_termica.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("ideia", "formula", "exemplo", "atalho", "fenomenos", "erro", "questao", "fim"))
BR = "#FFFFFF"
FRIO = F.NEG
GELO = "#A9D8F5"
AGUA = "#5BA8E0"

# todas as contas da aula
dl = lambda L0, a, dT: L0 * a * dT
assert math.isclose(dl(20, 1.2e-5, 50), 1.2e-2) and 20 * 50 == 1000 == 10 ** 3 and 3 - 5 == -2
assert math.isclose(dl(20, 1.2e-5, 50) * 100, 1.2)                      # 1,2 cm
assert 70 - 20 == 50 and 2 * 50 == 100 == 10 ** 2 and 2 - 5 == -3
assert math.isclose(dl(2, 2.4e-5, 50), 2.4e-3) and math.isclose(dl(2, 2.4e-5, 50) * 1000, 2.4)   # 2,4 mm
assert math.isclose(2 * 2.4e-5, 4.8e-5)                                   # beta = 2 alfa
assert 10 ** -3 == 0.001


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
def tabuleiro(c, x0, x1, y, a=1.0, cor=TINTA2, h=44):
    M.rrect(c, x0, y, x1 - x0, h, 8, cor, a)


def ponte(c, t, t0, x, y, w, fresta=24, a=1.0, racha=0.0):
    """ponte vista de lado: dois tabuleiros com a fresta no meio e dois pilares; racha > 0 desenha trincas vermelhas"""
    q = ep(t, t0, 0.6) * a
    if q <= 0:
        return
    meio = x + w / 2
    tabuleiro(c, x, meio - fresta / 2, y, q)
    tabuleiro(c, meio + fresta / 2, x + w, y, q)
    for px in (x + w * 0.18, x + w * 0.82):
        M.rrect(c, px - 26, y + 44, 52, 240, 8, CINZA, q)
    M.line(c, x - 60, y + 284, x + w + 60, y + 284, TINTA2, q, 5)
    if racha > 0:
        for k, dx in enumerate((-0.2, 0.0, 0.2)):
            xx = meio + dx * w
            pts = [(xx, y - 4), (xx + 14, y + 12), (xx - 10, y + 26), (xx + 8, y + 48)]
            F.poli(c, pts, racha, ERRADO, q, 6)


def trilho(c, x, y, w, curva=0.0, a=1.0, cor=TINTA2):
    """trilho de lado (barra fina) com dormentes; curva > 0 faz a barra entortar para cima no meio"""
    if a <= 0:
        return
    for k in range(9):
        xx = x + 20 + k * (w - 40) / 8
        M.rrect(c, xx - 14, y + 10, 28, 30, 4, "#8B5E3C", a)
    pts = [(x + w * i / 60, y - curva * math.sin(math.pi * i / 60) ** 2) for i in range(61)]
    F.poli(c, pts, 1.0, cor, a, 16)


def barra_dl(c, t, t0, x, y, w, h, dl_px, tc, rot_l0="L₀", rot_dl="ΔL", size=56):
    """barra de comprimento w (o L0) que, a partir de tc, ganha o pedaço laranja dl_px (o ΔL) na ponta"""
    q = ep(t, t0, 0.5)
    if q <= 0:
        return
    M.rrect(c, x, y, w, h, 10, CINZA, q)
    g = dl_px * ease_io(prog(t, tc, 1.0)) if t >= tc else 0
    if g > 0:
        M.rrect(c, x + w - 10, y, g + 10, h, 10, E.COR, q)
    E.chave(c, x, x + w, y + h + 16, TINTA2, q, 22, 5)
    E.foco(c, t, t0 + 0.3, 0.4, lambda a: E.formula(c, rot_l0, x + w / 2, y + h + 100, size, "g", TINTA, a, "center"))
    if t >= tc + 0.8:
        E.foco(c, t, tc + 0.8, 0.4, lambda a: E.formula(c, rot_dl, x + w + dl_px / 2, y - 26, size, "g", COR, a, "center"))


def lamina(c, cx, cy, L, curv, a=1.0, esp=34):
    """lâmina bimetálica presa à esquerda em (cx, cy): tira laranja (α maior) em cima e azul (α menor) embaixo.
    curv de 0 (reta) a 1 (curvada para baixo, para o lado da azul)"""
    if a <= 0:
        return
    k = 0.0001 + curv * 0.0012  # curvatura (1/raio)
    R = 1 / k
    for i, (cor, off) in enumerate(((E.COR, -esp / 2), (FRIO, esp / 2))):
        r = R - off
        pts = []
        for j in range(61):
            s = L * j / 60
            ang = s / R
            pts.append((cx + r * math.sin(ang), cy + R - r * math.cos(ang)))
        F.poli(c, pts, 1.0, cor, a, esp)
    M.rrect(c, cx - 60, cy - 70, 60, 140, 8, TINTA2, a)


def lago(c, t, t0, x, y, w, h, a=1.0):
    """corte de um lago: gelo em cima (0 °C), água no meio e água a 4 °C no fundo, com um peixe"""
    q = ep(t, t0, 0.6) * a
    if q <= 0:
        return
    M.rrect(c, x, y, w, h, 30, AGUA, 0.35 * q)
    M.rrect(c, x, y + h - 130, w, 130, 30, "#2F6FB0", 0.45 * q)
    return q


def peixe(c, x, y, s, a=1.0, t=0.0):
    if a <= 0:
        return
    x += 20 * math.sin(t * 1.3)
    c.drawOval(skia.Rect.MakeXYWH(x - s, y - s * 0.45, 2 * s, s * 0.9), M.paint(E.COR, a))
    p = skia.Path(); p.moveTo(x + s * 0.8, y); p.lineTo(x + s * 1.5, y - s * 0.5); p.lineTo(x + s * 1.5, y + s * 0.5); p.close()
    c.drawPath(p, M.paint(E.COR, a))
    c.drawCircle(x - s * 0.5, y - s * 0.1, s * 0.12, M.paint(BR, a))


def chapa_furo(c, cx, cy, w, h, r, k=1.0, a=1.0):
    """chapa laranja com um furo; k = fator de dilatação (1 = fria)"""
    if a <= 0:
        return
    W_, H_, R_ = w * k, h * k, r * k
    path = skia.Path()
    path.addRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - W_ / 2, cy - H_ / 2, W_, H_), 24, 24))
    path.addCircle(cx, cy, R_)
    path.setFillType(skia.PathFillType.kEvenOdd)
    c.drawPath(path, M.paint(E.COR, a))
    c.drawCircle(cx, cy, R_, M.paint(TINTA, a, stroke=4))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def um():
        E.frase(c, t, C["s01.a"], ps("uma ponte de concreto", "i", 76), XE, 220, passo=0.12)
        E.frase(c, t, C["s01.b"], ps("tem uma", "i", 76) + [("fresta", "g", 80, COR)], XE, 340, passo=0.12)
        ponte(c, t, C["s01.a"] + 0.3, 260, 620, 1400, 30)
        q = ep(t, C["s01.b"] + 0.3, 0.4)
        if q > 0:
            c.drawCircle(960, 642, 70 + 6 * math.sin(t * 4), M.paint(E.COR, q, stroke=7))
        E.foco(c, t, C["s01.b"] + 1.6, 0.4, lambda a: E.pilula(c, "não é defeito", 1420, 330, 50, "b", fundo=CERTO, a=a))
        E.frase(c, t, C["s01.c"], ps("sem ela, no verão:", "i", 64, TINTA2) + [("racharia", "g", 64, ERRADO)], XE, 470, passo=0.1)
        if t >= C["s01.c"] + 0.6:
            E.foco(c, t, C["s01.c"] + 0.6, 0.4, lambda a: sol(c, 1700, 180, 60, a, t))
    E.saida(c, t, C["s02"] - 0.1, um)
    if t >= C["s02"]:
        promessa(c, t, C, "s02", (("s02.b", "quanto cresce", COR), ("s02.c", "três fenômenos", TINTA)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    def var(a, x, y):
        E.formula(c, "ΔC = ΔK", x - 40, y + 26, 70, "g", TINTA, a, "center")

    def pot(a, x, y):
        E.formula(c, "10^{−3} = 0,001", x - 80, y + 26, 60, "g", TINTA, a, "center")
    lembrete2(c, t, C, "s03", (("s03.b", "a variação de", "temperatura"), ("s03.c", "as potências", "de dez")), (var, pot))


# ---------------- por que dilata ----------------
def b_ideia(c, t, C, b):
    E.frase(c, t, C["s04"], ps("por que crescem?", "i", 84), XE, 220, passo=0.12)
    ag = ease_io(prog(t, C["s04.a"], 1.5))
    w = lerp(620, 760, ease_io(prog(t, C["s04.b"], 1.6)))
    E.foco(c, t, C["s04"] + 0.8, 0.5, lambda a: particulas(c, t, 1000, 340, w, 400, lerp(0.15, 1.0, ag), E.mix(FRIO, E.COR, ag), a, n=(6, 4)))
    if t >= C["s04"] + 0.8:
        E.foco(c, t, C["s04"] + 1.0, 0.4, lambda a: (M.line(c, 1000, 790, 1620, 790, TINTA2, a, 4, dash=E.TRACO),
                                                     E.escreve(c, "antes", 1000, 850, 44, "i", TINTA2, a)))
    E.frase(c, t, C["s04.a"], ps("mais agitadas", "i", 70), XE, 400, passo=0.1)
    E.frase(c, t, C["s04.b"], [("se", "i", 70), ("afastam", "g", 66)], XE, 510)
    E.frase(c, t, C["s04.c"], ps("o material", "i", 70) + [("aumenta", "g", 66, COR)], XE, 620, passo=0.1)
    E.foco(c, t, C["s04.d"], 0.5, lambda a: E.pilula(c, "dilatação térmica", XE + 330, 820, 76, "g", fundo=E.COR, a=a))


# ---------------- a fórmula ----------------
def b_formula(c, t, C, b):
    def s05_06():
        barra_dl(c, t, C["s05.a"], 900, 200, 640, 60, 160, C["s05.a"] + 0.8)
        formula_em(c, t, C["s05.b"], "ΔL = L₀ · α · ΔT", XE, 480, 120)
        F.formula_legenda(c, t, C["s05.b"], "", [("ΔL", "quanto cresceu", "m"), ("L₀", "comprimento inicial", "m"),
                                                ("ΔT", "variação de temperatura", "°C"), ("α", "coeficiente de dilatação linear", "°C^{−1}")],
                          XE, 480, size=120, tl=[C["s06.a"], C["s06.b"], C["s06.c"], C["s06.d"]], size_l=56)
        E.foco(c, t, C["s06.e"], 0.5, lambda a: E.pilula(c, "°C⁻¹ = por grau Celsius", 1480, 920, 46, "b", fundo=TINTA, a=a))
    E.saida(c, t, C["s07"] - 0.1, s05_06)
    if t < C["s07"]:
        return
    E.frase(c, t, C["s07"], ps("cada material tem o seu", "i", 70) + [("α", "g", 76, COR)], XE, 220, passo=0.1)
    E.foco(c, t, C["s07.a"], 0.5, lambda a: E.pilula(c, "aço", XE + 70, 360, 56, "g", fundo=TINTA, a=a))
    formula_em(c, t, C["s07.a"] + 0.3, "α = 1,2 · 10^{−5} °C^{−1}", XE + 200, 385, 96)
    E.frase(c, t, C["s07.b"], ps("dilatação", "i", 70) + [("pequena", "g", 66)], XE, 600, passo=0.1)
    E.frase(c, t, C["s07.c"], ps("força", "i", 70) + [("enorme", "g", 66, ERRADO)], XE, 760, passo=0.1)
    cv = 90 * ease_io(prog(t, C["s07.c"] + 0.4, 1.0))
    E.foco(c, t, C["s07.b"] + 0.3, 0.5, lambda a: trilho(c, 900, 780, 860, cv, a))
    if t >= C["s07.c"] + 0.2:
        for x in (880, 1780):
            M.rrect(c, x - 20, 680, 40, 140, 6, TINTA, ep(t, C["s07.c"] + 0.2, 0.3))


# ---------------- exemplo ----------------
def b_exemplo(c, t, C, b):
    def s08_09():
        E.foco(c, t, C["s08.a"], 0.5, lambda a: trilho(c, 1060, 330, 700, 0, a))
        E.foco(c, t, C["s08.a"] + 0.4, 0.4, lambda a: F.medida(c, 20, "m", 1410, 440, 64, TINTA, a, "center"))
        E.foco(c, t, C["s08.b"], 0.5, lambda a: sol(c, 1700, 170, 56, a, t))
        E.foco(c, t, C["s08.b"] + 0.3, 0.4, lambda a: E.formula(c, "ΔT = 50 °C", 1300, 190, 60, "g", COR, a, "center"))
        E.frase(c, t, C["s08"] + 0.4, [("trilho", "i", 76), ("de", "i", 76), ("aço", "g", 76)], XE, 220)
        E.foco(c, t, C["s08.a"] + 0.6, 0.4, lambda a: E.formula(c, "α = 1,2 · 10^{−5} °C^{−1}", XE, 320, 56, "b", TINTA2, a))
        passos(c, t, [(C["s09.a"], "ΔL = 20 · 50 · 1,2 · 10^{−5}", TINTA), (C["s09.b"], "20 · 50 = 1.000 = 10^3", TINTA2),
                      (C["s09.d"], "10^3 · 10^{−5} = 10^{−2}", TINTA2), (C["s09.e"], "ΔL = 1,2 · 10^{−2} m", TINTA)], XE, 520, 135, 76)
        bola_txt(c, t, C["s09.f"], "1,2 cm", 1500, 760, 150, 80)
    E.saida(c, t, C["s10"] - 0.1, s08_09)
    if t < C["s10"]:
        return
    E.frase(c, t, C["s10"] + 0.3, ps("preso nas pontas, sem folga:", "i", 64), XE, 220, passo=0.1)
    cv = 110 * ease_io(prog(t, C["s10.a"], 1.0))
    E.foco(c, t, C["s10"] + 0.5, 0.5, lambda a: trilho(c, 300, 470, 1300, cv, a))
    for x in (280, 1620):
        M.rrect(c, x - 20, 380, 40, 140, 6, TINTA, ep(t, C["s10"] + 0.5, 0.3)) if t >= C["s10"] + 0.5 else None
    E.foco(c, t, C["s10.a"] + 0.6, 0.4, lambda a: E.pilula(c, "entorta", 960, 300, 60, "g", fundo=ERRADO, a=a))
    E.frase(c, t, C["s10.b"], [("juntas", "g", 80, COR), ("de", "i", 84), ("dilatação", "g", 80, COR)], XE, 700, passo=0.12)
    E.foco(c, t, C["s10.b"] + 0.5, 0.5, lambda a: (trilho(c, 300, 920, 640, 0, a), trilho(c, 980, 920, 640, 0, a)))
    q = ep(t, C["s10.b"] + 1.0, 0.4)
    if q > 0:
        c.drawCircle(960, 920, 54 + 5 * math.sin(t * 4), M.paint(E.COR, q, stroke=6))
        E.escreve(c, "folga", 1030, 870, 46, "i", TINTA2, q)


# ---------------- atalho (palco) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def s11():
        E.frase(c, t, C["s11"], ps("agora, o atalho", "i", 76, CLARO), W / 2, 160, "center")
        cols = ((420, "linha", "α", C["s11"] + 1.0, 1), (960, "chapa", "β = 2α", C["s11.a"], 2), (1500, "bloco", "γ = 3α", C["s11.b"], 3))
        for x, nome, fs, tk, n in cols:
            def fig(a, x=x, n=n):
                cy = 470
                if n == 1:
                    M.rrect(c, x - 180, cy - 14, 360, 28, 8, CLARO, a)
                    F.seta(c, x + 190, cy, x + 280, cy, E.COR, a, 8)
                elif n == 2:
                    M.rrect(c, x - 140, cy - 140, 280, 280, 12, CLARO, a)
                    F.seta(c, x + 150, cy, x + 240, cy, E.COR, a, 8)
                    F.seta(c, x, cy - 150, x, cy - 240, E.COR, a, 8)
                else:
                    E.cubo(c, t, tk, x - 130, cy + 130, 230, None, cor=CLARO)
            E.foco(c, t, tk, 0.5, fig)
            E.foco(c, t, tk + 0.2, 0.4, lambda a, x=x, nome=nome: centro(c, nome, x, 720, 56, "i", CLARO, a))
        E.foco(c, t, C["s11.c"], 0.5, lambda a: E.formula(c, "β = 2α", 960, 880, 110, "g", BR, a, "center"))
        E.foco(c, t, C["s11.d"], 0.5, lambda a: E.formula(c, "γ = 3α", 1500, 880, 110, "g", BR, a, "center"))
        E.foco(c, t, C["s11"] + 1.2, 0.5, lambda a: E.formula(c, "α", 420, 880, 110, "g", CLARO, a, "center"))
    E.saida(c, t, C["s12"] - 0.1, s11)
    if t < C["s12"]:
        return
    E.foco(c, t, C["s12.a"], 0.5, lambda a: E.formula(c, "ΔA = A₀ · β · ΔT", W / 2, 330, 110, "g", BR, a, "center"))
    E.foco(c, t, C["s12.b"], 0.5, lambda a: E.formula(c, "ΔV = V₀ · γ · ΔT", W / 2, 520, 110, "g", BR, a, "center"))
    E.frase(c, t, C["s12.c"], ps("decore uma,", "i", 70, CLARO) + [("troque a letra", "g", 66, BR)], W / 2, 700, "center", 0.12)
    E.frase(c, t, C["s12.d"], ps("deu β ou γ?", "g", 60, ERRADO) + ps("use direto", "i", 66, CLARO), W / 2, 880, "center", 0.12)


# ---------------- fenômenos ----------------
def b_fenomenos(c, t, C, b):
    def s13():
        E.foco(c, t, C["s13"], 0.4, lambda a: E.escreve(c, "1  juntas  ✓", XE, 200, 50, "b", TINTA2, a))
        E.frase(c, t, C["s13.a"], [("2", "g", 80, COR), ("lâmina", "g", 80), ("bimetálica", "g", 80)], XE, 330, passo=0.12)
        cv = ease_io(prog(t, C["s13.d"], 1.4))
        E.foco(c, t, C["s13.b"], 0.5, lambda a: lamina(c, 1150, 430, 620, cv, a))
        E.foco(c, t, C["s13.b"] + 0.4, 0.4, lambda a: (E.escreve(c, "α maior", 1350, 380, 46, "g", COR, a),
                                                       E.escreve(c, "α menor", 1350, 520, 46, "g", FRIO, a)) if cv < 0.05 else None)
        E.frase(c, t, C["s13.c"], [("α maior", "g", 56, COR)] + ps("cresce mais", "i", 60), XE, 520, passo=0.1)
        E.frase(c, t, C["s13.d"], ps("curva para o lado", "i", 60) + ps("da que cresce menos", "g", 56, FRIO), XE, 640, passo=0.1)
        E.foco(c, t, C["s13.c"], 0.4, lambda a: sol(c, 1750, 200, 46, a, t))
        E.frase(c, t, C["s13.e"], ps("ferro de passar · pisca-pisca", "i", 56, TINTA2), XE, 900, passo=0.1)
    E.saida(c, t, C["s14"] - 0.1, s13)
    if t < C["s14"]:
        return
    E.frase(c, t, C["s14.a"], [("3", "g", 80, COR), ("a", "i", 84), ("água", "g", 80), ("é", "i", 84), ("do", "i", 84), ("contra", "g", 80, COR)], XE, 200, passo=0.12)

    def s14():
        P = F.grafico(c, t, C["s14.b"] - 0.4, 260, 330, 760, 560, 0, 10, 0.99, 1.01, "T (°C)", "V", passo=2,
                      marcas_y=[], size=40)
        f = lambda x: 1.0 + 0.00025 * (x - 4) ** 2 - 0.0035
        E.curva(c, t, C["s14.b"], P, f, 0, 10, d=1.6)
        E.ponto(c, t, C["s14.c"], P, 4, f(4), "4 °C", guias=True)
        E.foco(c, t, C["s14.b"] + 0.6, 0.4, lambda a: E.escreve(c, "encolhe", P.x(0.4), P.y(f(1)) - 30, 44, "i", FRIO, a))
        E.foco(c, t, C["s14.c"] + 0.6, 0.4, lambda a: E.pilula(c, "menor volume · mais densa", 1440, 600, 46, "b", fundo=E.COR, a=a))
    E.saida(c, t, C["s15"] - 0.1, s14)
    if t < C["s15"]:
        return
    x, y, w, h = 1000, 330, 800, 560
    q = lago(c, t, C["s15"], x, y, w, h)
    if q:
        E.foco(c, t, C["s15.a"], 0.4, lambda a: (E.escreve(c, "4 °C", x + 40, y + h - 50, 50, "g", BR, a), peixe(c, x + 500, y + h - 70, 40, a, t)))
        hb = 90 * ep(t, C["s15.b"], 0.8)
        if hb > 0:
            M.rrect(c, x, y, w, hb, 20, GELO, 1.0)
            c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, hb), 20, 20), M.paint(FRIO, 1.0, stroke=4))
            E.foco(c, t, C["s15.b"] + 0.6, 0.4, lambda a: E.escreve(c, "gelo · 0 °C", x + 40, y + 62, 46, "g", TINTA, a))
    E.frase(c, t, C["s15.a"], ps("a 4 °C", "g", 64) + ps("desce ao fundo", "i", 66), XE, 400, passo=0.1)
    E.frase(c, t, C["s15.b"], ps("em cima,", "i", 66) + [("congela", "g", 64, FRIO)], XE, 530, passo=0.1)
    E.frase(c, t, C["s15.c"], ps("o gelo", "i", 66) + [("boia:", "g", 64)] + ps("vira tampa", "i", 66), XE, 660, passo=0.1)
    E.frase(c, t, C["s15.d"], ps("os peixes", "i", 66) + [("vivem", "g", 64, CERTO)], XE, 790, passo=0.1)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s16"], [("cuidado", "g", 96, ERRADO)], XE, 200)
    E.frase(c, t, C["s16.a"], ps("chapa com furo", "i", 72), XE, 330, passo=0.1)
    k = lerp(1.0, 1.22, ease_io(prog(t, C["s16.d"], 1.4)))
    E.foco(c, t, C["s16.a"], 0.5, lambda a: chapa_furo(c, 1350, 470, 420, 300, 80, k, a))
    if t >= C["s16.d"]:
        E.foco(c, t, C["s16.d"] + 0.2, 0.4, lambda a: sol(c, 1720, 220, 46, a, t))
    E.frase(c, t, C["s16.b"], ps("o furo", "i", 72) + [("diminui?", "g", 70)], XE, 480, passo=0.1)
    if t >= C["s16.c"]:
        E.risco(c, XE + 250, 490, XE + 580, 420, t, C["s16.c"], largura=10)
    E.frase(c, t, C["s16.d"], ps("o furo", "i", 72) + [("aumenta", "g", 70, CERTO)], XE, 620, passo=0.1)
    E.foco(c, t, C["s16.d"] + 0.8, 0.5, lambda a: E.selo(c, XE + 640, 595, 50, True, a))

    def pote(a):
        x, y = 1350, 980
        M.rrect(c, x - 130, y - 180, 260, 180, 30, "#CFE8F5", a)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x - 130, y - 180, 260, 180), 30, 30), M.paint(TINTA2, a, stroke=4))
        M.rrect(c, x - 110, y - 225, 220, 50, 12, E.COR, a)
    E.foco(c, t, C["s16.e"], 0.5, pote)
    E.frase(c, t, C["s16.e"] + 0.4, ps("tampa de metal:", "i", 56) + [("dilata mais", "g", 54, COR)] + ps("que o vidro", "i", 56), XE, 900, passo=0.1)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s17"], ps("hora de testar", "i", 72, COR), XE, 200)
    E.frase(c, t, C["s17.a"], [("barra", "i", 70), ("de", "i", 70), ("alumínio:", "g", 66)], XE, 320)
    E.foco(c, t, C["s17.a"] + 0.4, 0.5, lambda a: F.medida(c, 2, "m", XE + 560, 320, 80, COR, a))
    formula_em(c, t, C["s17.b"], "α = 2,4 · 10^{−5} °C^{−1}", XE, 450, 70)
    E.foco(c, t, C["s17.c"], 0.5, lambda a: E.formula(c, "20 °C → 70 °C", XE, 570, 70, "g", TINTA, a))
    E.frase(c, t, C["s17.d"], [("a)", "g", 64, COR)] + ps("quanto cresce?", "i", 68), XE, 720, passo=0.1)
    E.frase(c, t, C["s17.e"], [("b)", "g", 64, COR)] + ps("qual é o", "i", 68) + [("β?", "g", 64)], XE, 840, passo=0.1)
    if t < C["s18"]:
        E.foco(c, t, C["s17.a"], 0.5, lambda a: M.rrect(c, 1150, 520, 600, 50, 10, CINZA, a))
    else:
        E.relogio(c, t, C["s18.a"], cx=1460, cy=440, r=200)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    E.frase(c, t, C["s19"], [("a)", "g", 76, COR)], XE, 200)
    passos(c, t, [(C["s19.a"], "ΔT = 70 − 20 = 50", TINTA), (C["s19.b"], "2 · 50 = 100 = 10^2", TINTA2),
                  (C["s19.d"], "10^2 · 10^{−5} = 10^{−3}", TINTA2), (C["s19.e"], "ΔL = 2,4 · 10^{−3} m", TINTA)], XE, 330, 135, 76)
    bola_txt(c, t, C["s19.f"], "2,4 mm", 1480, 470, 150, 80, CERTO)
    E.frase(c, t, C["s20"], [("b)", "g", 76, COR)], XE, 920)
    formula_em(c, t, C["s20.a"], "β = 2α", XE + 120, 920, 80)
    formula_em(c, t, C["s20.b"], "= 4,8 · 10^{−5} °C^{−1}", XE + 120 + E.formula(None, "β = 2α ", 0, 0, 80, a=0), 920, 80, cor=CERTO)


# ---------------- fechamento ----------------
def praia(c, t, t0, x, y, w, h):
    q = ep(t, t0, 0.6)
    if q <= 0:
        return
    M.rrect(c, x, y, w * 0.5, h, 20, "#E8C77A", q)
    M.rrect(c, x + w * 0.5, y, w * 0.5, h, 20, AGUA, 0.7 * q)
    sol(c, x + w * 0.5, y - 120, 50, q, t)


def b_fim(c, t, C, b):
    def r():
        resumo(c, t, C, "s21", (("s21.a", [("ΔL = L₀ · α · ΔT", "g", 70)]),
                                ("s21.b", [("área:", "i", 70), ("2α;", "g", 66, COR), ("volume:", "i", 70), ("3α", "g", 66, COR)]),
                                ("s21.c", [("o", "i", 70), ("furo", "g", 66), ("cresce", "i", 70), ("junto", "g", 66, COR)])))
    E.saida(c, t, C["s22"] - 0.1, r)
    if t < C["s22"]:
        return
    E.frase(c, t, C["s22"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C["s22.a"], [("Calor", "g", 130, COR)], XE, 410)
    E.frase(c, t, C["s22.a"] + 0.5, [("sensível", "g", 130, COR)], XE, 550)
    praia(c, t, C["s22.b"], 260, 820, 900, 150)
    E.foco(c, t, C["s22.b"] + 0.6, 0.4, lambda a: (E.escreve(c, "areia", 300, 800, 44, "i", TINTA, a), E.escreve(c, "mar", 760, 800, 44, "i", TINTA, a)))
    inscreva(c, t, C, "s22", "s22.c", "s22.d")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, ideia=b_ideia, formula=b_formula, exemplo=b_exemplo, atalho=b_atalho,
              fenomenos=b_fenomenos, erro=b_erro, questao=b_questao, resposta=b_resposta, fim=b_fim)
