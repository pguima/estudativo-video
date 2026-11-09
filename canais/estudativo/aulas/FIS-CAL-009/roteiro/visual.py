"""Visual — Estudativo · FIS-CAL-009: condução de calor (lei de Fourier como proporção).
Segue a linguagem visual da trilha Calor e Termodinâmica (cabeçalho do visual.py da FIS-CAL-001: quente laranja, frio azul,
partículas que tremem, seta ondulada do calor, fórmula com legenda). Novas convenções da propagação de calor:
- FLUXO de calor (Φ) = setas onduladas atravessando o material; mais fluxo = mais setas e mais grossas (peça fluxo_setas).
- PAREDE (peça parede_calor): placa vista de frente em perspectiva, face quente laranja à esquerda, fria azul à direita,
  com as cotas da espessura L e da área A. É a figura de Fourier: Φ = k·A·ΔT / L.
- PROPORÇÃO: "A × 2 → Φ × 2" com a seta e o fator em pílula (verde quando o fluxo sobe, azul quando cai).
- Condutor = metal cinza; isolante = madeira, isopor, lã e ar parado.
Todo instante vem de C[...] (marcadores do roteiro)."""
import math
from fractions import Fraction as Fr

import editorial as E
import fisica as F
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Física", "Calor e Termodinâmica")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_FIS-CAL-009_conducao_de_calor.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("conducao", "fourier", "metal", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
FRIO = F.NEG
METAL = "#9AA0A6"
MADEIRA = "#8B5E3C"

# todas as contas da aula: Φ = k·A·ΔT/L lido como proporção (fator = o que muda em cima ÷ o que muda embaixo)
fator = lambda A=1, dT=1, L=1, k=1: Fr(k) * Fr(A) * Fr(dT) / Fr(L)
assert fator(A=2) == 2 and fator(dT=2) == 2 and fator(L=2) == Fr(1, 2)
assert fator(A=3, L=2) == Fr(3, 2) == 1.5
assert fator(L=2, dT=Fr(1, 2)) == Fr(1, 4)                  # a questão: quatro vezes menor
assert fator(L=2, dT=Fr(1, 2)) != 1                         # o erro "não muda" não acerta


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
def porta(c, x, y, w, h, a=1.0):
    """porta de madeira com maçaneta de metal; (x, y) = canto de cima à esquerda"""
    if a <= 0:
        return
    M.rrect(c, x, y, w, h, 10, MADEIRA, a)
    for k in range(2):
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x + 40, y + 50 + k * h * 0.48, w - 80, h * 0.4), 8, 8), M.paint("#6E4A2F", a, stroke=6))
    M.rrect(c, x + w - 150, y + h * 0.5 - 18, 110, 36, 18, METAL, a)
    c.drawCircle(x + w - 60, y + h * 0.5, 30, M.paint(METAL, a))
    c.drawCircle(x + w - 60, y + h * 0.5, 30, M.paint(TINTA2, a, stroke=4))


def colher_panela(c, t, t0, x, y, a=1.0, aquece=0.0):
    """panela no fogo com uma colher de metal; aquece de 0 a 1 pinta a colher de laranja da ponta até o cabo"""
    if a <= 0:
        return
    M.rrect(c, x - 200, y - 200, 400, 200, 22, TINTA2, a)
    for k in range(3):
        cx = x - 100 + k * 100
        p = skia.Path(); p.moveTo(cx, y + 80); p.cubicTo(cx + 30, y + 50, cx + 20, y + 20, cx, y + 10); p.cubicTo(cx - 20, y + 20, cx - 30, y + 50, cx, y + 80)
        c.drawPath(p, M.paint(E.COR, a * (0.8 + 0.2 * math.sin(t * 8 + k))))
    A, B = (x + 40, y - 150), (x + 330, y - 470)
    n = 30
    for i in range(n):
        f0, f1 = i / n, (i + 1) / n
        quente = aquece * 1.3 - f0
        cor = E.mix(METAL, E.COR, max(0.0, min(1.0, quente * 2)))
        M.line(c, lerp(A[0], B[0], f0), lerp(A[1], B[1], f0), lerp(A[0], B[0], f1), lerp(A[1], B[1], f1), cor, a, 20)


def cadeia(c, t, t0, x, y, n, dx, r, a=1.0, vel=0.9):
    """fila de partículas: a agitação chega de uma em uma, da esquerda para a direita, e ninguém sai do lugar"""
    if a <= 0:
        return
    for i in range(n):
        ag = ease_io(prog(t, t0 + i / vel * 0.5, 0.6))
        amp = 3 + 18 * ag
        px = x + i * dx + amp * math.sin(t * 16 + i)
        py = y + amp * math.cos(t * 13 + i * 2)
        M.line(c, x + i * dx, y + r + 22, x + i * dx, y + r + 40, TINTA2, a * 0.6, 4)
        E.bola(c, px, py, r, E.mix(FRIO, E.COR, ag), a)


def parede_calor(c, t, t0, x, y, esp, alt, prof=180, a=1.0, rot=True):
    """placa em perspectiva: face quente (esquerda) laranja e fria (direita) azul; cotas da espessura L e da área A"""
    q = ep(t, t0, 0.6) * a
    if q <= 0:
        return
    dx, dy = prof * 0.6, -prof * 0.5
    frente = skia.Path(); frente.addRect(skia.Rect.MakeXYWH(x, y, esp, alt))
    topo = skia.Path(); topo.moveTo(x, y); topo.lineTo(x + dx, y + dy); topo.lineTo(x + esp + dx, y + dy); topo.lineTo(x + esp, y); topo.close()
    lado = skia.Path(); lado.moveTo(x + esp, y); lado.lineTo(x + esp + dx, y + dy); lado.lineTo(x + esp + dx, y + alt + dy); lado.lineTo(x + esp, y + alt); lado.close()
    c.drawPath(lado, M.paint(FRIO, 0.85 * q))
    c.drawPath(topo, M.paint("#E3DCD2", q))
    sh = skia.Paint(AntiAlias=True)
    sh.setShader(skia.GradientShader.MakeLinear([skia.Point(x, 0), skia.Point(x + esp, 0)], [M.hexc(E.COR, q), M.hexc(FRIO, q)]))
    c.drawPath(frente, sh)
    for p in (frente, topo, lado):
        c.drawPath(p, M.paint(TINTA, q, stroke=4))
    if rot:
        E.chave(c, x, x + esp, y + alt + 18, TINTA2, q, 22, 5)
        E.foco(c, t, t0 + 0.3, 0.4, lambda a_: E.formula(c, "L", x + esp / 2, y + alt + 100, 60, "g", COR, a_, "center"))


def fluxo_setas(c, t, t0, x0, x1, ys, larg=8, a=1.0, cor=None):
    for i, y in enumerate(ys):
        seta_calor(c, t, t0 + 0.12 * i, (x0, y), (x1, y), None, cor=cor, a=a, amp=10, ondas=2, d=0.6)


def fator_linha(c, t, t0, y, esq, dir_, sobe, x=XE, size=76, escuro=False):
    """ "A × 2 → Φ × 2" com o resultado numa pílula verde (sobe) ou azul (cai)"""
    tinta = BR if escuro else TINTA
    E.foco(c, t, t0, 0.5, lambda a: E.formula(c, esq, x, y, size, "g", tinta, a))
    E.foco(c, t, t0 + 0.4, 0.4, lambda a: E.escreve(c, "→", x + 330, y - 4, size, "g", TINTA2 if not escuro else CLARO, a))
    E.foco(c, t, t0 + 0.6, 0.5, lambda a: E.pilula(c, dir_, x + 600, y - size * 0.35, size * 0.72, "g", fundo=CERTO if sobe else FRIO, a=a))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def um():
        E.foco(c, t, C["s01.a"], 0.5, lambda a: porta(c, 1150, 160, 560, 860, a))
        E.foco(c, t, C["s01.a"] + 0.6, 0.4, lambda a: E.pilula(c, "metal", 1590, 470, 44, "g", fundo=TINTA2, a=a))
        E.foco(c, t, C["s01.b"], 0.4, lambda a: E.pilula(c, "madeira", 1330, 300, 44, "g", fundo="#6E4A2F", a=a))
        E.frase(c, t, C["s01.a"], ps("de manhã cedo:", "i", 70), XE, 230, passo=0.1)
        E.frase(c, t, C["s01.c"], ps("o metal parece", "i", 70) + [("mais frio", "g", 70, FRIO)], XE, 400, passo=0.1)
        E.frase(c, t, C["s01.d"], ps("mas os dois estão a", "i", 60), XE, 580, passo=0.1)
        E.foco(c, t, C["s01.d"] + 1.0, 0.5, lambda a: F.medida(c, 20, "°C", XE, 760, 160, TINTA, a))
        E.foco(c, t, C["s01.d"] + 1.4, 0.5, lambda a: E.pilula(c, "mesma temperatura", XE + 250, 880, 52, "g", fundo=E.COR, a=a))
    E.saida(c, t, C["s02"] - 0.1, um)
    if t >= C["s02"]:
        promessa(c, t, C, "s02", (("s02.a", "o engano do metal", COR), ("s02.b", "a lei de Fourier", TINTA)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    def calor(a, x, y):
        seta_calor(c, 1e9, 0, (x - 220, y + 20), (x + 60, y + 20), None, a=a, amp=10, ondas=2)
        E.escreve(c, "cal", x + 80, y + 40, 50, "b", TINTA2, a)

    def prop(a, x, y):
        E.formula(c, "R = k · f{L}{A}", x - 60, y + 30, 60, "g", TINTA, a, "center")
    lembrete2(c, t, C, "s03", (("s03.b", "calor, medido em", "calorias"), ("s03.c", "fórmula como", "proporção")), (calor, prop))


# ---------------- condução ----------------
def b_conducao(c, t, C, b):
    def s04():
        E.frase(c, t, C["s04.a"], ps("o calor viaja de", "i", 70) + [("3 jeitos", "g", 70, COR)], XE, 200, passo=0.1)
        for i, s in enumerate(("condução", "convecção", "irradiação")):
            x = XE + 160 + i * 380
            E.foco(c, t, C["s04.b"] + 0.4 * i, 0.4, lambda a, i=i, x=x, s=s: E.pilula(c, s, x, 330, 50, "g", fundo=E.COR if i == 0 else CINZA, a=a))
        aq = ease_io(prog(t, C["s04.d"] - 0.6, 2.5))
        E.foco(c, t, C["s04.c"], 0.5, lambda a: colher_panela(c, t, C["s04.c"], 900, 960, a, aq))
        E.frase(c, t, C["s04.c"], ps("colher na panela quente", "i", 56), XE, 520, passo=0.1)
        E.frase(c, t, C["s04.d"], ps("o cabo", "i", 60) + [("esquenta", "g", 60, COR)], XE, 640, passo=0.1)
    E.saida(c, t, C["s05"] - 0.1, s04)
    if C["s05"] <= t < C["s06"]:
        def s05():
            E.frase(c, t, C["s05"] + 0.2, ps("dentro da colher", "i", 60, TINTA2), XE, 200, passo=0.1)
            cadeia(c, t, C["s05.a"], 300, 470, 9, 170, 34)
            E.foco(c, t, C["s05.a"], 0.4, lambda a: E.escreve(c, "ponta quente", 230, 380, 44, "i", COR, a))
            E.frase(c, t, C["s05.b"], ps("esbarram nas vizinhas", "i", 60), XE, 700, passo=0.1)
            E.frase(c, t, C["s05.c"], ps("a", "i", 64) + [("agitação", "g", 60, COR)] + ps("passa adiante", "i", 64), XE, 800, passo=0.1)
            E.frase(c, t, C["s05.d"], [("nenhuma", "g", 60)] + ps("sai do lugar", "i", 64), XE, 900, passo=0.1)
            E.foco(c, t, C["s05.e"], 0.5, lambda a: E.pilula(c, "condução", 1500, 860, 76, "g", fundo=E.COR, a=a))
        E.saida(c, t, C["s06"] - 0.1, s05)
    if t < C["s06"]:
        return
    for i, (k, nome, cor, itens) in enumerate((("s06.a", "condutores", CERTO, (("metais", METAL),)),
                                              ("s06.b", "isolantes", FRIO, (("madeira", MADEIRA), ("isopor", "#F2F2F2"), ("lã", "#D8C3A5"), ("ar parado", "#CFE8F5"))))):
        x = 230 + i * 820
        E.frase(c, t, C[k], [(nome, "g", 80, cor)], x, 260)
        for j, (s, cc) in enumerate(itens):
            y = 380 + j * 150
            E.foco(c, t, C[k] + 0.4 + 0.4 * j, 0.4, lambda a, x=x, y=y, s=s, cc=cc: (M.rrect(c, x, y, 110, 110, 18, cc, a),
                                                                                     c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, 110, 110), 18, 18), M.paint(TINTA2, a, stroke=3)),
                                                                                     E.escreve(c, s, x + 150, y + 75, 56, "i", TINTA, a)))


# ---------------- Fourier ----------------
def b_fourier(c, t, C, b):
    def s07():
        E.frase(c, t, C["s07.a"], [("fluxo", "g", 90, COR), ("de", "i", 90), ("calor", "g", 90, COR)], XE, 230, passo=0.12)
        E.frase(c, t, C["s07.b"], ps("quanto calor atravessa a cada segundo", "i", 56), XE, 340, passo=0.08)
        formula_em(c, t, C["s07.c"], "Φ = f{Q}{t}", XE, 560, 130)
        F.formula_legenda(c, t, C["s07.c"], "", [("Φ", "fluxo de calor", "cal/s"), ("Q", "calor", "cal"), ("t", "tempo", "s")],
                          XE, 560, size=130, tl=[C["s07.d"], C["s07.c"] + 0.6, C["s07.c"] + 1.0], size_l=56)
        E.foco(c, t, C["s07.a"] + 0.4, 0.5, lambda a: parede_calor(c, t, C["s07.a"] + 0.4, 1350, 380, 160, 420, rot=False))
        fluxo_setas(c, t, C["s07.b"], 1180, 1700, (480, 590, 700))
    E.saida(c, t, C["s08"] - 0.1, s07)
    if t < C["s08"]:
        return
    parede_calor(c, t, C["s08.a"], 1250, 300, 220, 460)
    E.foco(c, t, C["s08.a"] + 0.4, 0.4, lambda a: (E.escreve(c, "quente", 1040, 280, 48, "g", COR, a), E.escreve(c, "frio", 1650, 280, 48, "g", FRIO, a)))
    fluxo_setas(c, t, C["s08.a"] + 0.6, 1060, 1720, (420, 530, 640))
    E.foco(c, t, C["s09.a"], 0.4, lambda a: E.formula(c, "A", 1250 + 220 + 54, 300 + 230 - 30, 70, "g", BR, a, "center"))
    formula_em(c, t, C["s08.b"], "Φ = f{k · A · ΔT}{L}", XE, 330, 120)
    if C["s08.b"] <= t < C["s10"]:
        F.formula_legenda(c, t, C["s08.b"], "", [("A", "área", "m^2"), ("L", "espessura", "m"), ("ΔT", "diferença entre os lados", "°C"),
                                                 ("k", "condutividade térmica", None)],
                          XE, 330, size=120, tl=[C["s09.a"], C["s09.b"], C["s09.c"], C["s09.d"]], size_l=52, dy=78)
        E.foco(c, t, C["s09.e"], 0.4, lambda a: E.escreve(c, "metal: k grande · isopor: k pequeno", XE, 900, 46, "i", TINTA2, a))
    if t < C["s10"]:
        return
    fator_linha(c, t, C["s10.a"], 560, "A × 2", "Φ × 2", True)
    fator_linha(c, t, C["s10.b"], 700, "ΔT × 2", "Φ × 2", True)
    fator_linha(c, t, C["s10.c"], 840, "L × 2", "Φ ÷ 2", False)
    E.frase(c, t, C["s10.d"], ps("parede grossa", "g", 56) + ps("segura o calor", "i", 60), XE, 990, passo=0.1)


# ---------------- o metal engana ----------------
def b_metal(c, t, C, b):
    def s11():
        E.foco(c, t, C["s11.a"], 0.5, lambda a: mao(c, 960, 300, 110, a))
        E.foco(c, t, C["s11.a"] + 0.3, 0.4, lambda a: E.formula(c, "pele: ≈ 33 °C", 1000, 470, 54, "g", COR, a, "center"))
        E.foco(c, t, C["s11.b"], 0.5, lambda a: (M.rrect(c, 640, 700, 300, 200, 20, METAL, a), M.rrect(c, 1060, 700, 300, 200, 20, MADEIRA, a)))
        E.foco(c, t, C["s11.b"] + 0.3, 0.4, lambda a: (E.escreve(c, "metal · 20 °C", 640, 960, 48, "g", TINTA, a), E.escreve(c, "madeira · 20 °C", 1060, 960, 48, "g", TINTA, a)))
        if t >= C["s11.c"]:
            fluxo_setas(c, t, C["s11.c"], 760, 760 + 1, ())
            for k, (x, n) in enumerate(((790, 4), (1210, 1))):
                for j in range(n):
                    xx = x + (j - (n - 1) / 2) * 50
                    seta_calor(c, t, C["s11.c"] + 0.15 * j + (0 if k == 0 else 0.5), (xx, 520), (xx, 680), None, amp=8, ondas=2, d=0.5 if k == 0 else 1.4)
        E.frase(c, t, C["s11.c"], ps("o calor sai da mão", "i", 56), XE, 240, passo=0.1)
        E.frase(c, t, C["s11.d"], ps("metal:", "i", 56) + [("muito mais depressa", "g", 52, COR)], XE, 340, passo=0.1)
    E.saida(c, t, C["s12"] - 0.1, s11)
    if t < C["s12"]:
        return
    E.frase(c, t, C["s12.a"], ps("a pele não mede a", "i", 70) + [("temperatura do objeto", "g", 64)], XE, 300, passo=0.1)
    E.frase(c, t, C["s12.b"], ps("ela sente a", "i", 70) + [("rapidez", "g", 70, COR)] + ps("da perda de calor", "i", 70), XE, 460, passo=0.1)
    E.frase(c, t, C["s12.c"], ps("perdeu rápido:", "i", 70) + [("parece frio", "g", 70, FRIO)], XE, 620, passo=0.1)
    E.foco(c, t, C["s12.d"], 0.5, lambda a: E.pilula(c, "por isso o metal engana", W / 2, 840, 70, "g", fundo=E.COR, a=a))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s13"], [("cuidado", "g", 96, ERRADO)], XE, 210)
    E.frase(c, t, C["s13.a"], ps("“o cobertor", "i", 76) + [("esquenta”", "g", 70)], XE, 360, passo=0.1)
    if t >= C["s13.a"] + 1.6:
        E.risco(c, XE - 10, 375, XE + 720, 300, t, C["s13.a"] + 1.6, largura=10)
    E.frase(c, t, C["s13.b"], ps("o calor vem do", "i", 60) + [("seu corpo", "g", 56, COR)], XE, 520, passo=0.1)
    E.frase(c, t, C["s13.c"], ps("o ar parado deixa sair", "i", 60) + [("devagar", "g", 56, FRIO)], XE, 640, passo=0.1)

    def cama(a):
        M.rrect(c, 1100, 720, 700, 60, 14, TINTA2, a)
        c.drawCircle(1180, 640, 60, M.paint("#E9B48C", a))
        M.rrect(c, 1240, 600, 560, 130, 50, "#C9A0DC", a)
        for k in range(5):
            c.drawCircle(1300 + k * 110, 640, 10, M.paint(BR, a * 0.7))
    E.foco(c, t, C["s13.a"], 0.5, cama)
    if t >= C["s13.c"]:
        seta_calor(c, t, C["s13.c"], (1500, 590), (1500, 430), None, amp=6, ondas=1.5, d=1.6)
    E.foco(c, t, C["s13.d"], 0.5, lambda a: E.pilula(c, "cobertor sobre o gelo: o gelo não esquenta", W / 2, 900, 50, "g", fundo=FRIO, a=a))


# ---------------- atalho (palco) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    E.frase(c, t, C["s14"], ps("agora, o atalho", "i", 70, CLARO), W / 2, 160, "center")
    E.frase(c, t, C["s14.a"], ps("não calcule o fluxo:", "i", 64, CLARO) + [("calcule o fator", "g", 64, BR)], W / 2, 280, "center", 0.1)
    E.foco(c, t, C["s14.a"] + 1.4, 0.5, lambda a: E.formula(c, "Φ = f{k · A · ΔT}{L}", W / 2, 470, 110, "g", BR, a, "center"))
    E.foco(c, t, C["s14.a"] + 2.4, 0.4, lambda a: (E.escreve(c, "em cima: multiplica", 1300, 430, 46, "i", CLARO, a),
                                                   E.escreve(c, "embaixo: divide", 1300, 520, 46, "i", CLARO, a)))
    E.foco(c, t, C["s14.b"], 0.5, lambda a: E.formula(c, "A × 3,  L × 2", W / 2, 700, 84, "g", BR, a, "center"))
    E.foco(c, t, C["s14.c"], 0.5, lambda a: E.formula(c, "Φ × f{3}{2} = Φ × 1,5", W / 2, 840, 84, "g", CLARO, a, "center"))
    E.frase(c, t, C["s14.d"], [("não", "g", 52, ERRADO)] + ps("compensa: pede o fluxo em números", "i", 56, CLARO), W / 2, 1000, "center", 0.08)


# ---------------- questão ----------------
def caixa_isopor(c, cx, cy, w, h, esp, a=1.0):
    if a <= 0:
        return
    M.rrect(c, cx - w / 2, cy - h / 2, w, h, 16, "#F7F7F3", a)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2, cy - h / 2, w, h), 16, 16), M.paint(TINTA2, a, stroke=4))
    M.rrect(c, cx - w / 2 + esp, cy - h / 2 + esp, w - 2 * esp, h - 2 * esp, 10, "#CFE8F5", a)
    for k in range(2):
        c.drawCircle(cx - 40 + k * 80, cy, 26, M.paint(FRIO, a * 0.6))


def b_questao(c, t, C, b):
    E.frase(c, t, C["s15"], ps("hora de testar", "i", 72, COR), XE, 200)
    E.frase(c, t, C["s15"] + 1.0, ps("caixa de isopor:", "i", 66), XE, 330, passo=0.1)
    E.frase(c, t, C["s15.a"], [("espessura", "i", 64), ("× 2", "g", 64, COR)], XE, 470, passo=0.1)
    E.frase(c, t, C["s15.b"], [("diferença de temperatura", "i", 60), ("÷ 2", "g", 64, COR)], XE, 600, passo=0.1)
    E.frase(c, t, C["s15.c"], ps("e o", "i", 70) + [("fluxo?", "g", 70, COR)], XE, 780, passo=0.1)
    if t < C["s16"]:
        esp = lerp(30, 60, ease_io(prog(t, C["s15.a"] + 0.3, 0.8)))
        E.foco(c, t, C["s15"] + 1.0, 0.5, lambda a: caixa_isopor(c, 1450, 560, 480, 340, esp, a))
    else:
        E.relogio(c, t, C["s16.a"], cx=1460, cy=440, r=200)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    formula_em(c, t, C["s17"] + 0.3, "Φ = f{k · A · ΔT}{L}", XE, 260, 100)
    fator_linha(c, t, C["s17.a"], 470, "L × 2", "÷ 2", False)
    fator_linha(c, t, C["s17.b"], 620, "ΔT ÷ 2", "÷ 2", False)
    E.foco(c, t, C["s17.c"], 0.5, lambda a: E.formula(c, "2 · 2 = 4", XE, 800, 84, "g", TINTA, a))
    bola_txt(c, t, C["s17.d"], "Φ ÷ 4", 1500, 560, 160, 84, CERTO)
    E.foco(c, t, C["s17.d"] + 0.6, 0.4, lambda a: centro(c, "quatro vezes menor", 1500, 800, 54, "i", TINTA, a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def r():
        resumo(c, t, C, "s18", (("s18.a", [("condução:", "g", 64), ("a agitação passa adiante", "i", 68)]),
                                ("s18.b", [("Φ = k · A · ΔT ÷ L", "g", 66, COR)]),
                                ("s18.c", [("metal", "g", 64), ("tira o calor", "i", 68), ("mais depressa", "g", 64, FRIO)])))
    E.saida(c, t, C["s19"] - 0.1, r)
    if t < C["s19"]:
        return
    E.frase(c, t, C["s19"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C["s19.a"], [("Convecção", "g", 120, COR)], XE, 410)
    E.frase(c, t, C["s19.b"], [("e", "i", 110), ("irradiação", "g", 120, COR)], XE, 550)
    E.foco(c, t, C["s19.b"], 0.5, lambda a: sol(c, 600, 850, 80, a, t))
    E.foco(c, t, C["s19.a"] + 0.3, 0.5, lambda a: [E.arco(c, 1000, 850, 110, 200 + t * 60 + 180 * k, 140, E.COR if k == 0 else FRIO, 12, a) for k in range(2)])
    inscreva(c, t, C, "s19", "s19.c", "s19.d")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, conducao=b_conducao, fourier=b_fourier, metal=b_metal, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
