"""Visual — Estudativo · FIS-CAL-008: praticando temperatura, dilatação e calorimetria (aula prática, 5 situações).
Segue a linguagem visual da trilha Calor e Termodinâmica (cabeçalho do visual.py da FIS-CAL-001) e reaproveita as peças das
aulas do módulo, copiadas aqui: termômetros alinhados pelos pontos fixos (001), cubo da dilatação (002), comparar disponível ×
necessário (006) e o diagrama de fases esquemático (007). Cada situação: enunciado com o desenho à direita, relógio de pausa,
resolução com as contas empilhadas e a resposta na esfera verde; o erro típico aparece riscado.
Todo instante vem de C[...] (marcadores do roteiro)."""
import math

import editorial as E
import fisica as F
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Física", "Calor e Termodinâmica")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_FIS-CAL-008_praticando_temperatura_dilatacao_calorimetria.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("questao1", "questao2", "questao3", "questao4", "questao5", "fim"))
BR = "#FFFFFF"
FRIO = F.NEG
GELO = "#A9D8F5"
AGUA = "#5BA8E0"
LF = 80

# todas as contas da aula
X = lambda c: 20 + (220 - 20) * c / 100
assert X(50) == 120 and 220 - 20 == 200 and 200 / 2 == 100 and (120 - 20) / 200 == 50 / 100
assert math.isclose(3 * 2e-5, 6e-5) and 500 * 100 == 50000 == 5 * 10 ** 4 and 5 * 6 == 30 and 4 - 5 == -1
assert math.isclose(500 * 6e-5 * 100, 3) and math.isclose(500 * 2e-5 * 100, 1)
Tf = (200 * 0.1 * 300 + 380 * 1 * 20) / (200 * 0.1 + 380)
assert math.isclose(Tf, 34) and math.isclose(200 * 0.1, 20) and 20 * 300 == 6000 and 380 * 20 == 7600 and 6000 + 7600 == 13600 and 13600 / 400 == 34
disp, nec = 200 * 50, 100 * 0.5 * 10 + 100 * LF
assert disp == 10000 and nec == 8500 and disp - nec == 1500 and 1500 / 300 == 5
assert 88 < 100                                       # La Paz: pressão menor que 1 atm, ebulição abaixo de 100 °C


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


# ---------------- peças copiadas das aulas do módulo ----------------
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



def situacao(c, t, C, cena, n):
    E.frase(c, t, C[cena + ".a"], [("situação", "i", 70, TINTA2), (str(n), "g", 80, COR)], XE, 200)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    E.frase(c, t, C["s01.a"], [("5", "g", 200, COR), ("situações", "i", 110)], XE, 360, passo=0.15)
    E.frase(c, t, C["s01.a"] + 1.2, ps("criadas para esta aula", "i", 60, TINTA2), XE, 470, passo=0.1)
    nomes = ("escalas", "dilatação", "calorímetro", "gelo", "diagrama")
    for i, s in enumerate(nomes):
        x = 300 + i * 330
        E.foco(c, t, C["s01.a"] + 2.0 + 0.3 * i, 0.4, lambda a, i=i, x=x, s=s: (E.bola(c, x, 680, 60, a=a), centro(c, str(i + 1), x, 704, 64, "g", BR, a),
                                                                               centro(c, s, x, 800, 44, "i", TINTA2, a)))
    E.frase(c, t, C["s01.b"], [("pause", "g", 70, COR)] + ps("e resolva antes da resposta", "i", 70), XE, 960, passo=0.1)


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s02"], ps("você vai usar", "i", 80), XE, 200)
    itens = (("s02.a", "f{C}{100} = f{X − 20}{200}"), ("s02.b", "ΔL = L₀ · α · ΔT"), ("s02.c", "Q = m · c · ΔT"), ("s02.d", "Q = m · L"), ("s02.e", "soma dos Q = 0"))
    for i, (k, s) in enumerate(itens):
        x, y = (XE, 1000)[i % 2], 380 + (i // 2) * 210
        E.foco(c, t, C[k], 0.5, lambda a, s=s, x=x, y=y: E.formula(c, s, x, y, 80 if "f{" not in s else 70, "g", TINTA, a))
    E.frase(c, t, lerp(C["s02.e"], C["s02.end"], 0.4), ps("travou?", "i", 54, COR) + ps("procure a aula no canal", "i", 54), 1000, 840, passo=0.1)


# ---------------- 1: escala inventada ----------------
YB, HT = 940, 600


def termos(c, t, t0, nivel, tm=None):
    """termômetros Celsius (0 a 100) e X (20 a 220) alinhados; nivel = valor em Celsius"""
    for i, (nome, cx, vmin, vmax, g, f, u) in enumerate((("Celsius", 1220, -20, 120, 0, 100, "°C"), ("escala X", 1600, -20, 260, 20, 220, "°X"))):
        v = None if nivel is None else (nivel if i == 0 else X(nivel))
        term(c, t, t0, cx, YB, HT, v, vmin, vmax)
        E.foco(c, t, t0, 0.4, lambda a, nome=nome, cx=cx: centro(c, nome, cx + 30, 280, 46, "g", TINTA, a))
        tm_ = tm or (t0 + 0.4, t0 + 0.4)
        marca(c, t, tm_[i], cx, y_term(0, YB, HT, -20, 120), g, u, 42, acima=True)
        marca(c, t, tm_[i], cx, y_term(100, YB, HT, -20, 120), f, u, 42, acima=True)
    tracejado(c, t, t0 + 0.3, 1080, 1860, y_term(0, YB, HT, -20, 120), FRIO)
    tracejado(c, t, t0 + 0.3, 1080, 1860, y_term(100, YB, HT, -20, 120), E.COR)


def b_questao1(c, t, C, b):
    situacao(c, t, C, "s03", 1)
    E.frase(c, t, C["s03.a"] + 0.8, ps("escala X:", "i", 64), XE, 330)
    E.frase(c, t, C["s03.b"], ps("gelo derrete a", "i", 56) + [("20 °X", "g", 56, FRIO)], XE, 450, passo=0.1)
    E.frase(c, t, C["s03.c"], ps("água ferve a", "i", 56) + [("220 °X", "g", 56, COR)], XE, 550, passo=0.1)
    E.frase(c, t, C["s03.d"], [("50 °C", "g", 70, COR)] + ps("= quantos °X?", "i", 70), XE, 720, passo=0.1)
    if t < C["s04"]:
        termos(c, t, C["s03.a"] + 0.5, None, (C["s03.b"], C["s03.c"]))
    else:
        E.relogio(c, t, C["s04.a"], cx=1460, cy=500, r=200)


def b_resposta1(c, t, C, b):
    termos(c, t, C["s05"] - 0.3, 50 if t >= C["s05.c"] else None)
    yg, yf, ym = y_term(0, YB, HT, -20, 120), y_term(100, YB, HT, -20, 120), y_term(50, YB, HT, -20, 120)
    cota_v(c, t, C["s05.a"], 1150, yg, yf, "100", TINTA, lado=-1, size=48)
    cota_v(c, t, C["s05.b"], 1530, yg, yf, "200", TINTA, lado=-1, size=48)
    marca(c, t, C["s05.c"] + 0.6, 1220, ym, 50, "°C", 42, COR)
    marca(c, t, C["s05.f"], 1600, ym, 120, "°X", 42, COR)

    def s05():
        E.frase(c, t, C["s05.c"], ps("50 °C = metade do caminho", "i", 56), XE, 260, passo=0.08)
        passos(c, t, [(C["s05.d"], "metade de 200 = 100", TINTA), (C["s05.e"], "a partir do gelo: 20 + 100", TINTA2)], XE, 420, 120, 64)
        bola_txt(c, t, C["s05.f"], "120 °X", 500, 800, 140, 70, CERTO)
    E.saida(c, t, C["s06"] - 0.1, s05)
    if t < C["s06"]:
        return
    formula_em(c, t, C["s06.a"], "f{X − 20}{200} = f{50}{100}", XE, 360, 90)
    E.foco(c, t, C["s06.a"] + 1.4, 0.4, lambda a: E.formula(c, "X − 20 = 100  →  X = 120", XE, 560, 64, "g", CERTO, a))
    E.foco(c, t, C["s06.b"], 0.5, lambda a: E.formula(c, "esqueceu o 20: 100 °X", XE, 760, 64, "g", ERRADO, a))
    if t >= C["s06.c"]:
        E.risco(c, XE - 10, 780, XE + 700, 700, t, C["s06.c"], largura=10)


# ---------------- 2: dilatação volumétrica ----------------
def b_questao2(c, t, C, b):
    situacao(c, t, C, "s07", 2)
    E.frase(c, t, C["s07.b"], ps("bloco de metal:", "i", 64), XE, 340, passo=0.1)
    E.foco(c, t, C["s07.b"] + 0.5, 0.5, lambda a: F.medida(c, 500, "cm^3", XE + 480, 340, 76, TINTA, a))
    formula_em(c, t, C["s07.c"], "α = 2 · 10^{−5} °C^{−1}", XE, 480, 70)
    E.frase(c, t, C["s07.d"], ps("esquenta", "i", 64) + [("100 °C", "g", 64, COR)], XE, 640, passo=0.1)
    E.frase(c, t, C["s07.d"] + 0.8, ps("quanto aumenta o volume?", "i", 64), XE, 750, passo=0.1)
    if t < C["s08"]:
        E.cubo(c, t, C["s07.b"], 1300, 900, 340, None)
    else:
        E.relogio(c, t, C["s08.a"], cx=1460, cy=360, r=180)


def b_resposta2(c, t, C, b):
    def s09():
        E.frase(c, t, C["s09"], ps("é volume:", "i", 64) + [("γ = 3α", "g", 64, COR)], XE, 220, passo=0.1)
        formula_em(c, t, C["s09.b"], "γ = 6 · 10^{−5} °C^{−1}", XE + 640, 220, 64, cor=COR)
        passos(c, t, [(C["s09.c"], "ΔV = 500 · 100 · 6 · 10^{−5}", TINTA), (C["s09.d"], "500 · 100 = 5 · 10^4", TINTA2),
                      (C["s09.e"], "5 · 6 = 30", TINTA2), (C["s09.f"], "10^4 · 10^{−5} = 10^{−1}", TINTA2)], XE, 400, 135, 70)
        E.cubo(c, t, C["s09"], 1400, 860, 280, None)
    E.saida(c, t, C["s10"] - 0.1, s09)
    if t < C["s10"]:
        return
    formula_em(c, t, C["s10.a"], "ΔV = 30 · 0,1", XE, 360, 90)
    bola_txt(c, t, C["s10.a"] + 1.2, "3 cm^3", 1450, 380, 150, 80, CERTO)
    E.foco(c, t, C["s10.b"], 0.5, lambda a: E.formula(c, "com α no lugar de γ: 1 cm^3", XE, 640, 70, "g", ERRADO, a))
    if t >= C["s10.c"]:
        E.risco(c, XE - 10, 660, XE + 900, 580, t, C["s10.c"], largura=10)
    E.frase(c, t, C["s10.c"], ps("três vezes menos", "i", 60, TINTA2), XE, 800, passo=0.1)


# ---------------- 3: metal na água ----------------
def copo_simples(c, cx, yb, w, h, cor, a=1.0):
    if a <= 0:
        return
    M.rrect(c, cx - w / 2 + 8, yb - h * 0.72, w - 16, h * 0.72 - 6, 12, cor, 0.55 * a)
    p = skia.Path()
    p.moveTo(cx - w / 2, yb - h); p.lineTo(cx - w / 2 + 10, yb); p.lineTo(cx + w / 2 - 10, yb); p.lineTo(cx + w / 2, yb - h)
    c.drawPath(p, M.paint(TINTA, a, stroke=6))


def b_questao3(c, t, C, b):
    situacao(c, t, C, "s11", 3)
    E.foco(c, t, C["s11.b"], 0.5, lambda a: E.formula(c, "metal: 200 g a 300 °C", XE, 360, 70, "g", COR, a))
    E.foco(c, t, C["s11.c"], 0.5, lambda a: E.formula(c, "c = 0,1", XE + 60, 460, 60, "g", COR, a))
    E.foco(c, t, C["s11.d"], 0.5, lambda a: E.formula(c, "água: 380 g a 20 °C", XE, 600, 70, "g", FRIO, a))
    E.frase(c, t, C["s11.e"], ps("temperatura", "i", 70) + [("final?", "g", 70, COR)], XE, 780, passo=0.1)
    if t < C["s12"]:
        E.foco(c, t, C["s11.b"], 0.5, lambda a: F.bloco(c, 1450, 380, 240, 160, "metal", E.COR, a))
        E.foco(c, t, C["s11.d"], 0.5, lambda a: copo_simples(c, 1450, 920, 340, 320, FRIO, a))
    else:
        E.relogio(c, t, C["s12.a"], cx=1460, cy=460, r=200)


def b_resposta3(c, t, C, b):
    E.frase(c, t, C["s13.a"], ps("substâncias diferentes:", "i", 60) + [("soma dos Q = 0", "g", 60, COR)], XE, 220, passo=0.1)
    formula_em(c, t, C["s13.b"], "200 · 0,1 · (T − 300)", XE, 380, 70, cor=COR)
    formula_em(c, t, C["s13.c"], "+ 380 · 1 · (T − 20) = 0", XE + 800, 380, 70, cor=FRIO)
    passos(c, t, [(C["s14.a"], "20T − 6.000 + 380T − 7.600 = 0", TINTA), (C["s14.b"], "400T = 13.600", TINTA)], XE, 580, 150, 72)
    bola_txt(c, t, C["s14.c"], "34 °C", 1500, 760, 150, 84, CERTO)


# ---------------- 4: gelo abaixo de zero ----------------
def b_questao4(c, t, C, b):
    situacao(c, t, C, "s15", 4)
    E.foco(c, t, C["s15.b"], 0.5, lambda a: E.formula(c, "100 g de gelo a −10 °C", XE, 360, 70, "g", FRIO, a))
    E.foco(c, t, C["s15.c"], 0.5, lambda a: E.formula(c, "+ 200 g de água a 50 °C", XE, 480, 70, "g", COR, a))
    E.foco(c, t, C["s15.d"], 0.5, lambda a: E.formula(c, "c do gelo = 0,5 · L = 80 cal/g", XE, 600, 56, "b", TINTA2, a))
    E.frase(c, t, C["s15.e"], ps("derrete tudo?", "i", 66) + [("T final?", "g", 66, COR)], XE, 780, passo=0.1)
    if t < C["s16"]:
        E.foco(c, t, C["s15.b"], 0.5, lambda a: copo(c, 1450, 900, 360, 440, a))
    else:
        E.relogio(c, t, C["s16.a"], cx=1460, cy=460, r=200)


def b_resposta4(c, t, C, b):
    def s17():
        E.frase(c, t, C["s17"] + 0.4, [("compare", "g", 64, COR)], XE, 220)
        formula_em(c, t, C["s17.a"], "disponível: 200 · 50 = 10.000", XE, 360, 60, cor=COR)
        formula_em(c, t, C["s17.b"], "gelo até 0: 100 · 0,5 · 10 = 500", XE, 500, 56, cor=FRIO)
        formula_em(c, t, C["s17.c"], "derreter: 100 · 80 = 8.000", XE, 600, 56, cor=FRIO)
        formula_em(c, t, C["s17.d"], "necessário: 8.500", XE, 730, 60, cor=FRIO)
        comparar(c, t, C["s17.a"], C["s17.d"], 10000, 8500, 1330, 900, 520, 10000, w=180, gap=120)
    E.saida(c, t, C["s18"] - 0.1, s17)
    if t < C["s18"]:
        return
    E.frase(c, t, C["s18.a"], [("10.000", "g", 70, COR), (">", "g", 70, TINTA2), ("8.500:", "g", 70, FRIO)] + ps("derrete tudo", "g", 62, CERTO), XE, 260, passo=0.1)
    passos(c, t, [(C["s18.b"], "sobram 1.500 cal", TINTA), (C["s18.c"], "300 g de água, a partir de 0 °C", TINTA2),
                  (C["s18.d"], "ΔT = 1.500 ÷ 300 = 5", TINTA)], XE, 440, 140, 66)
    bola_txt(c, t, C["s18.d"] + 1.0, "5 °C", 1500, 600, 140, 84, CERTO)


# ---------------- 5: diagrama de fases ----------------
def b_questao5(c, t, C, b):
    situacao(c, t, C, "s19", 5)
    E.frase(c, t, C["s19.b"], [("La Paz,", "g", 70), ("Bolívia", "i", 70)], XE, 340, passo=0.1)
    E.frase(c, t, C["s19.b"] + 1.0, ps("mais de 3.500 m de altitude", "i", 54, TINTA2), XE, 430, passo=0.08)
    E.frase(c, t, C["s19.c"], ps("a água ferve a", "i", 64) + [("≈ 88 °C", "g", 64, FRIO)], XE, 580, passo=0.1)
    E.frase(c, t, C["s19.d"], ps("explique com o", "i", 64) + [("diagrama de fases", "g", 60, COR)], XE, 740, passo=0.1)
    if t < C["s20"]:
        E.foco(c, t, C["s19.b"], 0.5, lambda a: montanha(c, 1150, 900, 620, 480, a))
    else:
        E.relogio(c, t, C["s20.a"], cx=1460, cy=460, r=200)


def b_resposta5(c, t, C, b):
    D = Diagrama(1010, 200, 800, 720)
    t0 = C["s21"]
    D.eixos(c, t, t0)
    D.regioes(c, t, t0, t0, t0, size=48)
    D.curvas(c, t, t0, t0, t0, rot=False)
    D.isobara(c, t, t0 + 0.3, 0.42, "1 atm", [("vap", "100 °C", t0 + 0.6)], cor=TINTA2, d=0.4)
    D.isobara(c, t, C["s21.b"], 0.33, "La Paz", [("vap", "≈ 88 °C", C["s21.d"], True)], cor=FRIO)
    E.frase(c, t, C["s21"] + 0.4, ps("lá no alto,", "i", 60) + [("menos ar", "g", 56)], XE, 260, passo=0.1)
    E.frase(c, t, C["s21.a"], [("p < 1 atm", "g", 64, FRIO)], XE, 380)
    E.frase(c, t, C["s21.b"], ps("a linha", "i", 60) + [("desce", "g", 56)], XE, 500, passo=0.1)
    E.frase(c, t, C["s21.c"], ps("cruza a vaporização", "i", 56) + [("antes", "g", 56)], XE, 620, passo=0.1)
    E.frase(c, t, C["s21.e"], ps("pressão menor:", "i", 56) + [("ebulição mais fria", "g", 52, FRIO)], XE, 800, passo=0.1)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def r():
        resumo(c, t, C, "s22", (("s22.a", [("escala nova:", "g", 60), ("proporção a partir do gelo", "i", 64)]),
                                ("s22.b", [("volume:", "g", 60), ("γ = 3α", "g", 60, COR)]),
                                ("s22.c", [("substâncias diferentes:", "g", 60), ("soma dos Q = 0", "i", 64, COR)]),
                                ("s22.d", [("com gelo:", "g", 60), ("compare antes", "i", 64, COR)])), y0=340, dy=170)
    E.saida(c, t, C["s23"] - 0.1, r)
    if t < C["s23"]:
        return
    E.frase(c, t, C["s23"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C["s23.a"], [("Condução", "g", 120, COR)], XE, 410)
    E.frase(c, t, C["s23.a"] + 0.5, [("de", "i", 110), ("calor", "g", 120, COR)], XE, 540)

    def maos(a):
        M.rrect(c, 300, 760, 300, 200, 20, "#9AA0A6", a)
        M.rrect(c, 700, 760, 300, 200, 20, "#8B5E3C", a)
        E.escreve(c, "metal", 350, 1010, 50, "i", TINTA, a)
        E.escreve(c, "madeira", 730, 1010, 50, "i", TINTA, a)
    E.foco(c, t, C["s23.b"], 0.5, maos)
    E.foco(c, t, C["s23.b"] + 1.0, 0.4, lambda a: E.pilula(c, "mesma temperatura", 650, 700, 44, "b", fundo=TINTA, a=a))
    inscreva(c, t, C, "s23", "s23.c", "s23.d")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, questao1=b_questao1, resposta1=b_resposta1, questao2=b_questao2, resposta2=b_resposta2,
              questao3=b_questao3, resposta3=b_resposta3, questao4=b_questao4, resposta4=b_resposta4, questao5=b_questao5,
              resposta5=b_resposta5, fim=b_fim)
