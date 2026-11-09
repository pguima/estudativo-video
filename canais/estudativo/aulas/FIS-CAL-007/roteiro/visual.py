"""Visual — Estudativo · FIS-CAL-007: diagrama de fases.
Segue a linguagem visual da trilha Calor e Termodinâmica (cabeçalho do visual.py da FIS-CAL-001).
DIAGRAMA DE FASES (peça `Diagrama`, esquemático, sem escala): T no eixo de baixo, p no eixo da esquerda; regiões pintadas de
leve (sólido azul-claro, líquido azul, vapor cinza); curvas de fusão, vaporização e sublimação em tinta, desenhadas no
instante da fala; ponto triplo laranja pulsando. A LINHA DE PRESSÃO (isóbara) é tracejada laranja, e cada cruzamento com uma
curva ganha uma bolinha e a temperatura escrita: é o "ande para a direita" do atalho. agua=True tomba a curva de fusão para
a esquerda; agua=False tomba para a direita (gás carbônico e a maioria das substâncias).
Todo instante vem de C[...] (marcadores do roteiro)."""
import math

import editorial as E
import fisica as F
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Física", "Calor e Termodinâmica")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_FIS-CAL-007_diagrama_de_fases.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("diagrama", "leitura", "panela", "fusao", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
FRIO = F.NEG
GELO = "#A9D8F5"
AGUA = "#5BA8E0"

# fatos e contas da aula (o diagrama é esquemático; os valores vêm do roteiro)
assert 120 > 100 > 70                  # panela de pressão (≈ 2 atm) > nível do mar (1 atm) > topo do Everest
assert 1 < 5 < 10 and 0.2 < 0.5 < 1    # comparações com o ponto triplo (gás carbônico; questão)


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


# ---------------- o diagrama de fases ----------------
class Diagrama:
    """diagrama esquemático na caixa (x, y, w, h). u (0 a 1) = temperatura, v (0 a 1) = pressão, para cima"""
    TP = (0.3, 0.25)

    def __init__(self, x, y, w, h, agua=True, escuro=False):
        self.x, self.y, self.w, self.h, self.agua, self.escuro = x, y, w, h, agua, escuro
        self.tinta = BR if escuro else TINTA

    def px(self, u, v):
        return self.x + u * self.w, self.y + (1 - v) * self.h

    # curvas em função do parâmetro
    def sub(self, k):          # k de 0 a 1, do canto até o ponto triplo
        u = 0.02 + 0.28 * k
        return u, 0.25 * k ** 2

    def vap(self, k):          # do ponto triplo até o fim
        u = 0.3 + 0.62 * k
        return u, 0.25 + 0.65 * k ** 1.6

    def fus(self, k):          # do ponto triplo para cima
        v = 0.25 + 0.73 * k
        return 0.3 + (-0.06 if self.agua else 0.08) * k, v

    def u_vap(self, v):
        return 0.3 + 0.62 * ((v - 0.25) / 0.65) ** (1 / 1.6)

    def u_fus(self, v):
        return 0.3 + (-0.06 if self.agua else 0.08) * (v - 0.25) / 0.73

    def u_sub(self, v):
        return 0.02 + 0.28 * math.sqrt(v / 0.25)

    def curva(self, c, t, t0, fn, cor=None, larg=7, d=0.8):
        q = ease_io(prog(t, t0, d))
        if q <= 0:
            return
        pts = [self.px(*fn(q * i / 60)) for i in range(61)]
        F.poli(c, pts, 1.0, cor or self.tinta, 1.0, larg)

    def eixos(self, c, t, t0, rot=True):
        q = ep(t, t0, 0.5)
        if q <= 0:
            return
        x0, y0 = self.px(0, 0)
        F.seta(c, x0, y0, x0 + self.w + 40, y0, self.tinta, q, 5, 22)
        F.seta(c, x0, y0, x0, self.y - 40, self.tinta, q, 5, 22)
        if rot:
            E.escreve(c, "temperatura", x0 + self.w - 230, y0 + 60, 42, "i", TINTA2 if not self.escuro else CLARO, q)
            E.escreve(c, "pressão", x0 - 40, self.y - 60, 42, "i", TINTA2 if not self.escuro else CLARO, q)

    def regioes(self, c, t, ts, tl, tv, rot=True, size=56):
        """pinta as regiões (ts = sólido, tl = líquido, tv = vapor)"""
        cores = (GELO, AGUA, "#C9C9CF")
        for k, (ti, nome, cor) in enumerate(((ts, "sólido", cores[0]), (tl, "líquido", cores[1]), (tv, "vapor", cores[2]))):
            q = ep(t, ti, 0.6)
            if q <= 0:
                continue
            p = skia.Path()
            if k == 0:
                p.moveTo(*self.px(0, 0)); p.lineTo(*self.px(0.02, 0))
                for i in range(41): p.lineTo(*self.px(*self.sub(i / 40)))
                for i in range(41): p.lineTo(*self.px(*self.fus(i / 40)))
                p.lineTo(*self.px(0, 0.98))
            elif k == 1:
                for i in range(41): p.lineTo(*self.px(*self.fus(i / 40))) if i else p.moveTo(*self.px(*self.fus(0)))
                p.lineTo(*self.px(1, 0.98)); p.lineTo(*self.px(1, 0.9))
                for i in range(40, -1, -1): p.lineTo(*self.px(*self.vap(i / 40)))
            else:
                p.moveTo(*self.px(0.02, 0))
                for i in range(41): p.lineTo(*self.px(*self.sub(i / 40)))
                for i in range(41): p.lineTo(*self.px(*self.vap(i / 40)))
                p.lineTo(*self.px(1, 0.9)); p.lineTo(*self.px(1, 0))
            p.close()
            c.drawPath(p, M.paint(cor, 0.35 * q))
            if rot:
                pos = ((0.12, 0.62), (0.62, 0.68), (0.66, 0.15))[k]
                E.foco(c, t, ti, 0.4, lambda a, pos=pos, nome=nome, cor=cor: centro(c, nome, *self.px(*pos), size, "g",
                                                                                     E.mix(cor, self.tinta, 0.55), a))

    def curvas(self, c, t, tf, tv, tsub, rot=True, size=40):
        self.curva(c, t, tf, self.fus)
        self.curva(c, t, tv, self.vap)
        self.curva(c, t, tsub, self.sub)
        if rot:
            for ti, nome, (u, v), ang in ((tf, "fusão", self.fus(0.75), -82 if self.agua else -76), (tv, "vaporização", self.vap(0.62), -30),
                                          (tsub, "sublimação", self.sub(0.55), -28)):
                def r(a, nome=nome, u=u, v=v, ang=ang):
                    x, y = self.px(u, v)
                    c.save(); c.translate(x + (18 if nome != "fusão" else -18), y - 16); c.rotate(ang)
                    E.escreve(c, nome, 0 if nome != "fusão" else 0, 0, size, "i", TINTA2 if not self.escuro else CLARO, a)
                    c.restore()
                E.foco(c, t, ti + 0.5, 0.4, r, sobe=0)

    def triplo(self, c, t, t0, rot=None, pulsa=True):
        q = ep(t, t0, 0.4)
        if q <= 0:
            return
        x, y = self.px(*self.TP)
        E.bola(c, x, y, 18, E.COR, q)
        if pulsa:
            c.drawCircle(x, y, 34 + 6 * math.sin(t * 5), M.paint(E.COR, q * 0.8, stroke=5))
        if rot:
            E.foco(c, t, t0 + 0.2, 0.4, lambda a: E.formula(c, rot, x + 40, y + 70, 44, "g", COR if not self.escuro else BR, a))

    def isobara(self, c, t, t0, v, rot=None, cruza=(), cor=None, d=1.0, size=44):
        """linha de pressão tracejada em v; cruza = [(tipo, texto, t)] com tipo "fus", "vap" ou "sub" """
        q = ease_io(prog(t, t0, d))
        if q <= 0:
            return
        cor = cor or E.COR
        x0, y0 = self.px(0, v)
        M.line(c, x0, y0, x0 + (self.w + 10) * q, y0, cor, 0.95, 5, dash=E.TRACO)
        if rot:  # o nome da pressão fica na ponta direita, embaixo da linha
            E.foco(c, t, t0, 0.4, lambda a: E.formula(c, rot, x0 + self.w, y0 + size + 6, size, "g", cor, a, "right"))
        for item in cruza:
            tipo, txt, ti = item[:3]
            esq = len(item) > 3 and item[3]
            u = {"fus": self.u_fus, "vap": self.u_vap, "sub": self.u_sub}[tipo](v)
            x, y = self.px(u, v)
            E.foco(c, t, ti, 0.4, lambda a, x=x, y=y: E.bola(c, x, y, 16, cor, a), blur=0)
            if txt:
                E.foco(c, t, ti + 0.2, 0.4, lambda a, x=x, y=y, txt=txt, esq=esq:
                       E.formula(c, txt, x - 14 if esq else x + 14, y - 26, size, "g", cor, a, "right" if esq else "left"))

    def ponto_andando(self, c, t, t0, v, u1, d=2.0, cor=None):
        q = ease_io(prog(t, t0, d))
        if q <= 0:
            return
        x, y = self.px(lerp(0.04, u1, q), v)
        E.bola(c, x, y, 20, cor or E.COR, 1.0)


def montanha(c, x, y, w, h, a=1.0):
    if a <= 0:
        return
    p = skia.Path(); p.moveTo(x, y); p.lineTo(x + w * 0.5, y - h); p.lineTo(x + w, y); p.close()
    c.drawPath(p, M.paint("#8A8A90", a))
    p2 = skia.Path(); p2.moveTo(x + w * 0.38, y - h * 0.76); p2.lineTo(x + w * 0.5, y - h); p2.lineTo(x + w * 0.62, y - h * 0.76); p2.close()
    c.drawPath(p2, M.paint(BR, a))


def panela_pressao(c, cx, yb, w, a=1.0, t=0.0):
    if a <= 0:
        return
    h = w * 0.5
    M.rrect(c, cx - w / 2, yb - h, w, h, 24, TINTA2, a)
    M.rrect(c, cx - w / 2 - 20, yb - h - 30, w + 40, 40, 14, TINTA, a)
    M.rrect(c, cx - 18, yb - h - 90, 36, 64, 10, E.COR, a)
    for k in range(3):
        ph = (t * 0.8 + k * 0.33) % 1
        c.drawCircle(cx + 10 * math.sin(ph * 6), yb - h - 110 - ph * 120, 12 + 14 * ph, M.paint(BR, a * (1 - ph) * 0.9))
        c.drawCircle(cx + 10 * math.sin(ph * 6), yb - h - 110 - ph * 120, 12 + 14 * ph, M.paint(CINZA, a * (1 - ph) * 0.6, stroke=3))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def um():
        for i, (k, nome, temp, fn) in enumerate((("s01.a", "topo do Everest", "≈ 70 °C", lambda a: montanha(c, 260, 760, 560, 380, a)),
                                                   ("s01.b", "panela de pressão", "≈ 120 °C", lambda a: panela_pressao(c, 1450, 760, 380, a, t)))):
            x = 220 + i * 900
            E.foco(c, t, C[k], 0.5, fn)
            E.foco(c, t, C[k] + 0.3, 0.4, lambda a, x=x, nome=nome: E.escreve(c, nome, x + 40, 860, 56, "i", TINTA, a))
            E.foco(c, t, C[k] + 0.6, 0.4, lambda a, x=x, temp=temp, i=i: E.formula(c, "água ferve a " + temp, x + 40, 960, 60, "g", FRIO if i == 0 else COR, a))
        E.frase(c, t, C["s01.b"] + 2.0, ps("a mesma água", "i", 70), XE, 220)
        E.frase(c, t, C["s01.c"], ps("mudou", "i", 76) + [("a pressão", "g", 80, COR)], XE, 330, passo=0.1)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t >= C["s02"]:
        promessa(c, t, C, "s02", (("s02.b", "o diagrama de fases", COR), ("s02.c", "a panela de pressão", TINTA)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    def atm(a, x, y):
        E.formula(c, "nível do mar: 1 atm", x - 140, y + 26, 46, "g", TINTA, a, "center")

    def sub(a, x, y):
        E.formula(c, "sólido → gás", x - 70, y + 26, 54, "g", TINTA, a, "center")
    lembrete2(c, t, C, "s03", (("s03.b", "a", "pressão"), ("s03.c", "mudanças de estado:", "sublimação")), (atm, sub))


# ---------------- o diagrama ----------------
def b_diagrama(c, t, C, b):
    D = Diagrama(1010, 200, 800, 720)
    D.eixos(c, t, C["s04.a"])
    E.frase(c, t, C["s04"] + 0.2, [("diagrama", "g", 84, COR), ("de", "i", 84), ("fases", "g", 84, COR)], XE, 220, passo=0.12)
    if C["s04"] <= t < C["s05"]:
        def s04():
            E.frase(c, t, C["s04.a"], ps("embaixo:", "i", 56) + [("temperatura", "g", 56)], XE, 380, passo=0.1)
            E.frase(c, t, C["s04.b"], ps("à esquerda:", "i", 56) + [("pressão", "g", 56)], XE, 480, passo=0.1)
            E.frase(c, t, C["s04.c"], ps("cada ponto: uma situação", "i", 56), XE, 620, passo=0.08)
            E.frase(c, t, C["s04.d"], ps("diz o", "i", 56) + [("estado", "g", 56, COR)], XE, 720, passo=0.1)
            q = ep(t, C["s04.c"], 0.5)
            if q > 0:
                x, y = D.px(0.6, 0.6)
                M.line(c, x, y, D.x, y, TINTA2, q * 0.8, 3, dash=E.TRACO)
                M.line(c, x, y, x, D.y + D.h, TINTA2, q * 0.8, 3, dash=E.TRACO)
                E.bola(c, x, y, 20, E.COR, q)
        E.saida(c, t, C["s05"] - 0.1, s04)
    if t < C["s05"]:
        return
    D.regioes(c, t, C["s05.b"], C["s05.c"], C["s05.d"])
    E.frase(c, t, C["s05.a"], [("3", "g", 64, COR)] + ps("regiões", "i", 64), XE, 380, passo=0.1)
    D.curvas(c, t, C["s06.b"], C["s06.c"], C["s06.d"])
    E.frase(c, t, C["s06.a"], [("3", "g", 64, COR)] + ps("curvas", "i", 64), XE, 480, passo=0.1)
    E.frase(c, t, C["s06.e"], ps("na curva:", "i", 56) + [("dois estados", "g", 54)], XE, 600, passo=0.1)
    E.frase(c, t, C["s06.e"] + 0.8, ps("(o patamar)", "i", 50, TINTA2), XE, 680, passo=0.1)
    D.triplo(c, t, C["s07.a"])
    E.frase(c, t, C["s07.a"], [("ponto", "g", 64, COR), ("triplo:", "g", 64, COR)], XE, 820, passo=0.1)
    E.frase(c, t, C["s07.b"], ps("os três convivem", "i", 56), XE, 910, passo=0.1)
    E.foco(c, t, C["s07.c"], 0.4, lambda a: E.pilula(c, "água: pressão bem menor que 1 atm", XE + 360, 1010, 40, "b", fundo=TINTA, a=a))


# ---------------- leitura a 1 atm ----------------
def b_leitura(c, t, C, b):
    D = Diagrama(1010, 200, 800, 720)
    D.eixos(c, t, C["s08"] - 0.5)
    D.regioes(c, t, C["s08"] - 0.5, C["s08"] - 0.5, C["s08"] - 0.5, size=48)
    D.curvas(c, t, C["s08"] - 0.5, C["s08"] - 0.5, C["s08"] - 0.5, rot=False)
    D.triplo(c, t, C["s08"] - 0.5, pulsa=False)
    E.frase(c, t, C["s08"], ps("o diagrama da", "i", 70) + [("água", "g", 70, FRIO)], XE, 220, passo=0.1)
    v1 = 0.42
    D.isobara(c, t, C["s08.a"], v1, "1 atm", [("fus", "0 °C", C["s08.c"]), ("vap", "100 °C", C["s08.d"])])
    D.ponto_andando(c, t, C["s08.b"], v1, 0.8, d=3.0)
    E.frase(c, t, C["s08.a"], ps("linha em", "i", 60) + [("1 atm", "g", 60, COR)], XE, 380, passo=0.1)
    E.frase(c, t, C["s08.b"], ps("para a direita =", "i", 56) + [("esquentar", "g", 56)], XE, 480, passo=0.1)
    E.frase(c, t, C["s08.c"], ps("cruza a fusão:", "i", 56) + [("0 °C", "g", 56, COR)], XE, 620, passo=0.1)
    E.frase(c, t, C["s08.d"], ps("cruza a vaporização:", "i", 56) + [("100 °C", "g", 56, COR)], XE, 720, passo=0.1)
    E.foco(c, t, C["s08.d"] + 1.6, 0.4, lambda a: E.pilula(c, "os pontos fixos da Celsius", XE + 330, 860, 46, "b", fundo=TINTA, a=a))


# ---------------- panela de pressão ----------------
def b_panela(c, t, C, b):
    D = Diagrama(1010, 200, 800, 720)
    t0 = C["s09"] - 0.5
    D.eixos(c, t, t0)
    D.regioes(c, t, t0, t0, t0, size=48)
    D.curvas(c, t, t0, t0, t0, rot=False)
    D.isobara(c, t, t0, 0.42, "1 atm", [("vap", "100 °C", t0)], cor=TINTA2, d=0.3)
    D.isobara(c, t, C["s09.b"], 0.55, "2 atm", [("vap", "≈ 120 °C", C["s09.d"])])
    E.frase(c, t, C["s09"], ps("panela de pressão:", "i", 64), XE, 220, passo=0.1)
    E.frase(c, t, C["s09.a"], ps("cerca de", "i", 60) + [("2 atm", "g", 60, COR)], XE, 330, passo=0.1)
    E.frase(c, t, C["s09.b"], ps("a linha sobe", "i", 60), XE, 440, passo=0.1)
    E.frase(c, t, C["s09.c"], ps("ferve mais à direita:", "i", 56) + [("≈ 120 °C", "g", 56, COR)], XE, 540, passo=0.1)
    E.frase(c, t, C["s10.a"], ps("água líquida", "i", 56) + [("mais quente", "g", 56, COR)], XE, 660, passo=0.1)
    E.frase(c, t, C["s10.b"], ps("cozinha", "i", 56) + [("mais rápido", "g", 56, CERTO)], XE, 750, passo=0.1)
    D.isobara(c, t, C["s10.c"], 0.33, "montanha", [("vap", "< 100 °C", C["s10.d"], True)], cor=FRIO, size=40)
    E.frase(c, t, C["s10.c"], ps("montanha:", "i", 54) + [("ferve abaixo de 100 °C", "g", 48, FRIO)], XE, 880, passo=0.1)
    E.frase(c, t, C["s10.d"] + 0.8, ps("o macarrão demora mais", "i", 50, TINTA2), XE, 960, passo=0.1)


# ---------------- fusão e gelo-seco ----------------
def b_fusao(c, t, C, b):
    def s11():
        E.frase(c, t, C["s11"], ps("repare na curva de", "i", 66) + [("fusão", "g", 66, COR)], XE, 200, passo=0.1)
        for i, (agua, nome, tk) in enumerate(((True, "água", C["s11.a"]), (False, "gás carbônico", C["s11.c"]))):
            D = Diagrama(240 + i * 860, 330, 600, 460, agua=agua)
            t0 = C["s11"] + 0.3 + 0.3 * i
            D.eixos(c, t, t0, rot=False)
            D.curva(c, t, t0, D.vap, CINZA, 5)
            D.curva(c, t, t0, D.sub, CINZA, 5)
            D.curva(c, t, tk, D.fus, E.COR, 10)
            E.foco(c, t, t0, 0.4, lambda a, i=i, nome=nome: E.escreve(c, nome, 240 + i * 860, 880, 56, "g", FRIO if i == 0 else TINTA, a))
            E.foco(c, t, tk + 0.5, 0.4, lambda a, i=i: E.escreve(c, "tomba para a esquerda" if i == 0 else "tomba para a direita",
                                                                 240 + i * 860, 950, 44, "i", COR, a))
        E.foco(c, t, C["s11.b"], 0.4, lambda a: E.pilula(c, "mais pressão → o gelo derrete abaixo de 0 °C", W / 2, 1030, 40, "b", fundo=FRIO, a=a))
    E.saida(c, t, C["s12"] - 0.1, s11)
    if t < C["s12"]:
        return
    D = Diagrama(1010, 200, 800, 720, agua=False)
    t0 = C["s12"] + 0.2
    D.eixos(c, t, t0)
    D.regioes(c, t, t0, t0, t0, size=48)
    D.curvas(c, t, t0, t0, t0, rot=False)
    D.triplo(c, t, C["s12.a"], "5,1 atm")
    D.isobara(c, t, C["s12.b"], 0.12, "1 atm", [("sub", "", C["s12.c"])])
    E.frase(c, t, C["s12"], [("gás", "g", 70), ("carbônico", "g", 70)], XE, 220, passo=0.1)
    E.frase(c, t, C["s12.a"], ps("ponto triplo:", "i", 56) + [("> 5 atm", "g", 56, COR)], XE, 360, passo=0.1)
    E.frase(c, t, C["s12.b"], ps("em 1 atm, passa", "i", 56) + [("por baixo", "g", 56)], XE, 470, passo=0.1)
    E.frase(c, t, C["s12.c"], ps("só cruza a", "i", 56) + [("sublimação", "g", 56, COR)], XE, 580, passo=0.1)
    E.foco(c, t, C["s12.d"], 0.5, lambda a: E.pilula(c, "gelo-seco: sólido → gás", XE + 300, 760, 54, "g", fundo=E.COR, a=a))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s13"], [("cuidado", "g", 96, ERRADO)], XE, 210)
    E.frase(c, t, C["s13.a"], ps("na panela de pressão,", "i", 66) + [("ferve mais rápido?", "g", 62)], XE, 360, passo=0.1)
    if t >= C["s13.b"]:
        E.risco(c, XE + 600, 375, XE + 1180, 300, t, C["s13.b"], largura=10)
    E.frase(c, t, C["s13.b"], ps("demora", "i", 70) + [("mais", "g", 66, ERRADO)] + ps("para ferver", "i", 70), XE, 530, passo=0.1)
    E.frase(c, t, C["s13.c"], ps("precisa chegar a", "i", 64) + [("≈ 120 °C", "g", 62, COR)], XE, 650, passo=0.1)
    E.frase(c, t, C["s13.d"], ps("o que acelera é o", "i", 70) + [("cozimento", "g", 66, CERTO)], XE, 820, passo=0.1)
    E.foco(c, t, C["s13.a"], 0.5, lambda a: panela_pressao(c, 1550, 980, 380, a, t))


# ---------------- atalho (palco) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    D = Diagrama(980, 240, 820, 640, escuro=True)
    t0 = C["s14"]
    D.eixos(c, t, t0)
    D.curvas(c, t, t0, t0, t0, rot=False)
    D.triplo(c, t, t0 + 0.3, pulsa=False)
    E.frase(c, t, C["s14"], ps("agora, o atalho", "i", 70, CLARO), XE, 200)
    D.isobara(c, t, C["s14.a"], 0.5, None, [("fus", "", C["s14.b"]), ("vap", "", C["s14.b"] + 0.5)], cor=E.CLARO)
    D.ponto_andando(c, t, C["s14.a"] + 0.6, 0.5, 0.9, d=2.5, cor=E.CLARO)
    E.frase(c, t, C["s14.a"], ps("trace a pressão,", "i", 60, CLARO) + [("ande para a direita", "g", 56, BR)], XE, 340, passo=0.08)
    E.frase(c, t, C["s14.b"], ps("cada curva:", "i", 60, CLARO) + [("uma mudança", "g", 56, BR)], XE, 470, passo=0.08)
    E.frase(c, t, C["s14.c"], [("pressão ↑", "g", 60, BR), ("ebulição ↑", "g", 60, E.CLARO)], XE, 640, passo=0.15)
    D.isobara(c, t, C["s14.d"], 0.12, None, [("sub", "", C["s14.d"] + 0.8)], cor=FRIO)
    E.frase(c, t, C["s14.d"], ps("abaixo do triplo:", "i", 56, CLARO) + [("sólido → gás", "g", 56, BR)], XE, 800, passo=0.08)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s15"], ps("hora de testar", "i", 72, COR), XE, 200)
    E.frase(c, t, C["s15.a"], ps("ponto triplo:", "i", 60), XE, 330, passo=0.1)
    E.foco(c, t, C["s15.a"] + 0.4, 0.5, lambda a: E.formula(c, "0,5 atm · 20 °C", XE, 430, 66, "g", COR, a))
    E.frase(c, t, C["s15.b"], [("a)", "g", 60, COR)] + ps("aquece o sólido em", "i", 60) + [("1 atm", "g", 60)], XE, 580, passo=0.1)
    E.frase(c, t, C["s15.c"], ps("o que acontece?", "i", 60), XE + 70, 670, passo=0.1)
    E.frase(c, t, C["s15.d"], [("b)", "g", 60, COR)] + ps("e em", "i", 60) + [("0,2 atm?", "g", 60)], XE, 800, passo=0.1)
    if t < C["s16"]:
        D = Diagrama(1150, 260, 640, 520, agua=False)
        D.eixos(c, t, C["s15.a"], rot=False)
        D.curvas(c, t, C["s15.a"], C["s15.a"], C["s15.a"], rot=False)
        D.triplo(c, t, C["s15.a"] + 0.4)
    else:
        E.relogio(c, t, C["s16.a"], cx=1460, cy=440, r=200)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    D = Diagrama(1010, 200, 800, 720, agua=False)
    t0 = C["s17"]
    D.eixos(c, t, t0)
    D.regioes(c, t, t0, t0, t0, size=48)
    D.curvas(c, t, t0, t0, t0, rot=False)
    D.triplo(c, t, t0, "0,5 atm")
    D.isobara(c, t, C["s17.a"], 0.42, "1 atm", [("fus", "funde", C["s17.c"]), ("vap", "ferve", C["s17.c"] + 0.8)])
    E.frase(c, t, C["s17.a"], [("a)", "g", 60, COR), ("1 > 0,5", "g", 60)], XE, 250, passo=0.1)
    E.frase(c, t, C["s17.b"], ps("acima do triplo:", "i", 54), XE, 340, passo=0.1)
    E.frase(c, t, C["s17.c"], ps("derrete e depois ferve", "g", 50, CERTO), XE, 430, passo=0.1)
    D.isobara(c, t, C["s18.a"], 0.12, "0,2 atm", [("sub", "sublima", C["s18.c"], True)], cor=FRIO)
    E.frase(c, t, C["s18.a"], [("b)", "g", 60, COR), ("0,2 < 0,5", "g", 60)], XE, 600, passo=0.1)
    E.frase(c, t, C["s18.b"], ps("abaixo do triplo:", "i", 54), XE, 690, passo=0.1)
    E.frase(c, t, C["s18.d"], ps("vira gás direto", "g", 50, CERTO), XE, 780, passo=0.1)
    E.frase(c, t, C["s18.e"], ps("sem passar por líquido", "i", 50, TINTA2), XE, 860, passo=0.1)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def r():
        resumo(c, t, C, "s19", (("s19.a", [("região", "g", 64), ("= estado;", "i", 68), ("curva", "g", 64), ("= mudança", "i", 68)]),
                                ("s19.b", [("ponto triplo:", "g", 64, COR), ("os três convivem", "i", 68)]),
                                ("s19.c", [("mais pressão:", "g", 64), ("ebulição", "i", 68), ("mais quente", "g", 64, COR)])))
    E.saida(c, t, C["s20"] - 0.1, r)
    if t < C["s20"]:
        return
    E.frase(c, t, C["s20"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C["s20.a"], [("Praticando", "g", 120, COR)], XE, 410)
    E.frase(c, t, C["s20.b"], ps("escalas · dilatação · trocas de calor", "i", 52), XE, 530, passo=0.06)
    E.frase(c, t, C["s20.b"] + 1.6, ps("com e sem gelo · diagrama de fases", "i", 52), XE, 610, passo=0.06)
    for i in range(5):
        E.foco(c, t, C["s20.b"] + 0.3 * i, 0.4, lambda a, i=i: (E.bola(c, 300 + i * 160, 820, 56, a=a), centro(c, str(i + 1), 300 + i * 160, 842, 60, "g", BR, a)))
    inscreva(c, t, C, "s20", "s20.c", "s20.d")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, diagrama=b_diagrama, leitura=b_leitura, panela=b_panela, fusao=b_fusao,
              erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
