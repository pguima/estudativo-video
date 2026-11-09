"""Visual — Estudativo · FIS-OPT-002: reflexão e espelho plano.
Segue a linguagem visual da trilha Óptica, escrita no cabeçalho do visual.py da FIS-OPT-001 (raio laranja, normal tracejada,
objeto em tinta, imagem petróleo tracejada quando virtual, espelho em tinta com hachura atrás).
Todo instante vem de C[...] (marcadores do roteiro)."""
import math

import editorial as E
import fisica as F
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Física", "Óptica")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_FIS-OPT-002_reflexao_espelho_plano.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("reflexao", "lei", "imagem", "altura", "atalho", "questao", "fim"))

# todas as contas da aula
assert 90 - 30 == 60                                       # 30° com o espelho → incidência de 60°
assert 2 + 2 == 4                                          # 2 m na frente + 2 m atrás
assert 180 / 2 == 90 and 170 / 2 == 85                     # altura mínima e borda de baixo
assert (180 + 170) / 2 - 170 / 2 == 180 / 2                # do ponto do pé ao ponto da cabeça: metade da altura
assert 160 / 2 == 80 and 150 / 2 == 75                     # questão


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças da trilha Óptica (as mesmas em todas as FIS-OPT; candidatas a fisica.py) ----------------
BR = "#FFFFFF"
LUZ = "#FFB000"  # brilho de fonte de luz (lâmpada, Sol)
VIDRO = "#7FC8E8"  # vidro, água e lente


def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def bola_txt(c, t, t0, s, cx, cy, r, size, cor=None):
    """resposta na esfera: "20 m/s" com a unidade menor; sem unidade, só o texto"""
    v, _, u = s.partition(" ")
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r * ease_back(prog(t, t0, 0.5)), cor, a),
                                     F.medida(c, v, u, cx, cy + size * 0.36, size, E.SOBRE, a, "center", cor_u=E.SOBRE)))


def troca(c, t, itens, fn):
    """um de cada vez: itens = [(instante, arg)], cada um sai quando o próximo chega; fn(arg, a) desenha"""
    for i, (ti, s) in enumerate(itens):
        fim = itens[i + 1][0] - 0.1 if i + 1 < len(itens) else 1e9
        if t >= ti - 0.01:
            E.saida(c, t, fim, lambda s=s, ti=ti: E.foco(c, t, ti, 0.45, lambda a: fn(s, a)), d=0.25)


def pilula_em(c, t, t0, s, cx, cy, size, fundo=None, est="g", cor=BR):
    E.foco(c, t, t0, 0.4, lambda a: E.pilula(c, s, cx, cy, size, est, fundo=fundo, a=a, cor=cor))


def pilula_esq(c, t, t0, s, x, cy, size, fundo=None, est="g"):
    """pílula com a borda esquerda em x"""
    w = E.larg(s, est, size) + size * 1.1
    pilula_em(c, t, t0, s, x + w / 2, cy, size, fundo, est)
    return w


def lembrete(c, t, C, cena, itens, desenhos=None, yf=930):
    """o que você precisa saber: itens = [(cue, linha fina, linha forte)]; desenhos[i](a, x, y) à direita da caixa"""
    n = len(itens)
    E.frase(c, t, C[cena] + 0.2, ps("você precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C[cena + ".a"], 0.5, lambda a: E.escreve(c, str(n), XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C[cena + ".a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisa" if n == 1 else "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 800, 1020
    hs = 230
    for i, (k, l1, l2) in enumerate(itens):
        y = (230 + i * 290) if n > 1 else 200
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, hs, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 56)], x + 44, y + 90)
        E.frase(c, t, C[k] + 0.3, [(l2, "g", 54, COR)], x + 44, y + 170)
        if desenhos:
            E.foco(c, t, C[k] + 0.6, 0.5, lambda a, i=i, y=y: desenhos[i](a, x + w - 170, y + hs / 2))
    if n > 1:
        q1 = ease_io(prog(t, C[itens[1][0]] - 0.35, 0.5))
        E.cursor(c, x + w - 30, lerp(430, 720, q1), ep(t, C[itens[0][0]], 0.4))
    E.frase(c, t, lerp(C[itens[-1][0]], C[cena + ".end"], 0.6), ps("faltou?", "i", 56, COR) + ps("procure no canal", "i", 56), 800, yf, "left", 0.12)


def promessa(c, t, C, cena, itens, giro=12):
    """até o fim da aula: itens = [(cue, texto)] numerados, com a órbita à direita"""
    tb = C[cena + ".a"] + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1500, 560, 300 * ease_back(prog(t, tb, 0.8)), giro=giro * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, C[cena + ".a"], ps("até o fim da aula", "i", 84), XE, 260, passo=0.14)
    for i, (k, s) in enumerate(itens):
        y = 420 + i * 150
        E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, XE + 40, y - 28, 38, a=a), centro(c, str(i + 1), XE + 40, y - 6, 48, "g", BR, a)))
        E.frase(c, t, C[k] + 0.1, [(s, "g", 70, COR if i == 0 else TINTA)], XE + 110, y)


def resumo(c, t, C, cena, itens, y0=350, dy=170, size=62):
    """resumindo: itens = [(cue, partes de E.frase)] com esferas numeradas"""
    E.frase(c, t, C[cena], [("resumindo", "i", 92, COR)], W / 2, 190, "center")
    for i, (k, partes) in enumerate(itens):
        y = y0 + i * dy
        E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 250, y - 24, 50, a=a), centro(c, str(i + 1), 250, y - 2, 58, "g", BR, a)))
        E.frase(c, t, C[k] + 0.1, [(p[0], p[1], size if len(p) < 3 else p[2], *(p[3:] if len(p) > 3 else ())) for p in partes], 340, y, passo=0.1)


def proxima(c, t, C, cena, l1, l2, desenho=None, k_insc="c", k_bons="d"):
    """próxima aula + inscreva-se + bons estudos; desenho(a) ilustra embaixo à esquerda"""
    E.frase(c, t, C[cena], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C[cena + ".a"], l1, XE, 400, passo=0.12)
    E.frase(c, t, C[cena + ".a"] + 0.5, l2, XE, 530, passo=0.12)
    if desenho:
        desenho()
    E.foco(c, t, C[cena + "." + k_insc], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 420, 76, estilo="g", a=a))
    p = ease_io(prog(t, C[cena + "." + k_insc] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(720, 445, p), ep(t, C[cena + "." + k_insc] + 0.2, 0.4))
    E.frase(c, t, C[cena + "." + k_bons], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1570, 990, "center")


def questao_relogio(c, t, C, cena_pausa, cx=1460, cy=440, r=200):
    if t >= C[cena_pausa]:
        E.relogio(c, t, C[cena_pausa + ".a"], cx=cx, cy=cy, r=r)


# fontes de luz e o olho de quem vê
def lampada_fonte(c, cx, cy, r, a=1.0):
    """fonte de luz pequena com brilho"""
    if a <= 0:
        return
    p = skia.Paint(AntiAlias=True)
    p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r * 3.2, [M.hexc(LUZ, 0.55 * a), M.hexc(LUZ, 0.0)], [0, 1]))
    c.drawCircle(cx, cy, r * 3.2, p)
    E.bola(c, cx, cy, r, LUZ, a)


def sol(c, cx, cy, r, a=1.0):
    if a <= 0:
        return
    p = skia.Paint(AntiAlias=True)
    p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r * 1.8, [M.hexc(LUZ, 0.45 * a), M.hexc(LUZ, 0.0)], [0.4, 1]))
    c.drawCircle(cx, cy, r * 1.8, p)
    E.bola(c, cx, cy, r, LUZ, a)


def olho(c, x, y, s, a=1.0, olha=1):
    """olho visto de lado; olha = 1 para a direita, −1 para a esquerda; (x, y) = pupila"""
    if a <= 0:
        return
    c.save(); c.translate(x, y); c.scale(olha, 1)
    p = skia.Path()
    p.moveTo(-s * 1.6, 0); p.quadTo(-s * 0.5, -s * 1.1, s * 0.6, 0); p.quadTo(-s * 0.5, s * 1.1, -s * 1.6, 0); p.close()
    c.drawPath(p, M.paint(BR, a))
    pt = M.paint(TINTA, a, stroke=max(3, s * 0.12)); pt.setStrokeJoin(skia.Paint.kRound_Join)
    c.drawPath(p, pt)
    c.drawCircle(-s * 0.25, 0, s * 0.42, M.paint(F.VEL, a))
    c.drawCircle(-s * 0.15, 0, s * 0.2, M.paint(TINTA, a))
    c.restore()


def objeto_o(c, t, t0, x, yb, h, rotulo=None, d=0.5):
    """objeto (o que emite ou reflete a luz): seta em tinta"""
    F.objeto(c, t, t0, x, yb, h, cor=TINTA, rotulo=rotulo, d=d)


def imagem_i(c, t, t0, x, yb, h, real=True, rotulo=None, d=0.5):
    """imagem: seta petróleo, cheia se real, tracejada se virtual"""
    F.objeto(c, t, t0, x, yb, h, cor=F.VEL, rotulo=rotulo, tracejado=not real, d=d)


def prolonga(c, t, t0, A, B, d=0.6):
    """prolongamento de raio (para trás): tracejado cinza, sem seta"""
    F.raio(c, t, t0, [A, B], cor=TINTA2, d=d, largura=4, setas=False, tracejado=True)


def _u(A, B):
    dx, dy = B[0] - A[0], B[1] - A[1]
    n = math.hypot(dx, dy) or 1.0
    return dx / n, dy / n


def gauss(f, p):
    """posição da imagem pela equação 1/f = 1/p + 1/p' (o atalho f·p/(p − f))"""
    return f * p / (p - f)


def eixo_pontos(c, t, t0, cy, pts, escuro=False):
    """pontos marcados no eixo: pts = [(x, "F"), ...]; F em laranja, o resto em tinta"""
    tinta = BR if escuro else TINTA
    for x, s in pts:
        E.foco(c, t, t0, 0.4, lambda a, x=x, s=s: (c.drawCircle(x, cy, 10, M.paint(E.COR if s.startswith("F") else tinta, a)),
                                                    E._meio(c, s, x, cy + 50, 46, "b", tinta, a)))


def espelho_curvo(c, t, t0, vx, cy, R, meia, concavo=True):
    """espelho esférico desenhado como arco da circunferência de raio R (pixels): vértice em (vx, cy), luz vinda da esquerda,
    meia = meia altura. Devolve o centro (Cx, cy). Hachura do lado de trás."""
    Cx = vx - R if concavo else vx + R
    q = ep(t, t0, 0.6)
    if q <= 0:
        return Cx
    g = math.degrees(math.asin(min(0.99, meia / R)))
    a0, varre = ((-g, 2 * g) if concavo else (180 - g, 2 * g))
    ret = skia.Rect.MakeXYWH(Cx - R, cy - R, 2 * R, 2 * R)
    for i in range(14):
        ang = math.radians(a0 + varre * (i + 0.5) / 14)
        px, py = Cx + R * math.cos(ang), cy + R * math.sin(ang)
        k = 1 if concavo else -1
        nx, ny = math.cos(ang) * k, math.sin(ang) * k
        M.line(c, px, py, px + nx * 26 - ny * 12, py + ny * 26 + nx * 12, TINTA2, 0.55 * q, 3)
    c.drawArc(ret, a0 + varre * (1 - ease_io(q)) / 2, varre * ease_io(q), False, M.paint(TINTA, 1.0, stroke=8, cap_round=True))
    return Cx


def _bate_circ(P, d, Cx, cy, R, concavo):
    """ponto em que o raio P + s·d encontra a superfície do espelho"""
    fx, fy = P[0] - Cx, P[1] - cy
    b = 2 * (d[0] * fx + d[1] * fy)
    k = fx * fx + fy * fy - R * R
    disc = math.sqrt(max(0.0, b * b - 4 * k))
    s = (-b + disc) / 2 if concavo else (-b - disc) / 2
    return (P[0] + s * d[0], P[1] + s * d[1])


def raios_espelho(c, t, ts, vx, cy, f, xo, ho, concavo=True, tipos=("par", "foco"), passa=170, volta=380):
    """raios notáveis de um espelho esférico (f em pixels, sempre positivo aqui): saem da ponta do objeto (xo, cy − ho),
    cada um no seu instante ts[i]. Devolve (xi, hi): a ponta da imagem pela equação, real se xi < vx."""
    R = 2 * f
    Cx = vx - R if concavo else vx + R
    Fx = vx - f if concavo else vx + f
    p = vx - xo
    pl = gauss(f if concavo else -f, p)
    xi, hi = vx - pl, -pl / p * ho
    Q, P = (xi, cy - hi), (xo, cy - ho)
    real = pl > 0
    for tipo, t0 in zip(tipos, ts):
        if tipo == "par":
            d = (1.0, 0.0)
        else:
            alvo = (Fx, cy) if tipo == "foco" else (Cx, cy)
            d = _u(P, alvo)
            if d[0] < 0:
                d = (-d[0], -d[1])
        Hh = _bate_circ(P, d, Cx, cy, R, concavo)
        if real:
            u = _u(Hh, Q)
            fim = (Q[0] + u[0] * passa, Q[1] + u[1] * passa)
            F.raio(c, t, t0, [P, Hh, fim], d=1.3)
        else:
            u = _u(Q, Hh)
            fim = (Hh[0] + u[0] * volta, Hh[1] + u[1] * volta)
            F.raio(c, t, t0, [P, Hh, fim], d=1.3)
            prolonga(c, t, t0 + 1.2, Hh, Q)
    return xi, hi


def raios_lente(c, t, ts, cx, cy, f, xo, ho, tipos=("par", "centro"), passa=170, volta=380):
    """raios notáveis de uma lente fina em x = cx (f em pixels, negativo na divergente), da ponta do objeto (xo, cy − ho).
    Devolve (xi, hi), com a imagem real se xi > cx."""
    p = cx - xo
    pl = gauss(f, p)
    xi, hi = cx + pl, -pl / p * ho
    Q, P = (xi, cy - hi), (xo, cy - ho)
    real = pl > 0
    for tipo, t0 in zip(tipos, ts):
        if tipo == "par":
            Hh = (cx, P[1])
        elif tipo == "centro":
            Hh = (cx, cy)
        else:  # pelo foco da frente (convergente) ou mirando o foco de trás (divergente)
            Fx = cx - f
            d = _u(P, (Fx, cy))
            if d[0] < 0:
                d = (-d[0], -d[1])
            s = (cx - P[0]) / d[0]
            Hh = (cx, P[1] + s * d[1])
        if real:
            u = _u(Hh, Q)
            fim = (Q[0] + u[0] * passa, Q[1] + u[1] * passa)
        else:
            u = _u(Q, Hh)
            fim = (Hh[0] + u[0] * volta, Hh[1] + u[1] * volta)
        F.raio(c, t, t0, [P, Hh, fim], d=1.3)
        if not real:
            prolonga(c, t, t0 + 1.2, Hh, Q)
    return xi, hi


def classifica(c, t, itens, x, y, size=50):
    """as três palavras da imagem em pílulas lado a lado: itens = [(instante, texto)]; devolve o x final"""
    for ti, s in itens:
        w = E.larg(s, "g", size) + size * 1.1
        pilula_em(c, t, ti, s, x + w / 2, y, size, F.VEL)
        x += w + 24
    return x

# ---------------- peças desta aula ----------------
def pessoa(c, x, yb, h, a=1.0, cor=None, olha=1, tracejada=False):
    """pessoa de pé com o pé em (x, yb) e altura h; o olho (a 170/180 da altura) fica do lado para onde ela olha"""
    if a <= 0:
        return
    cor = cor or TINTA
    r = h * 0.065
    hy = yb - h + r
    if tracejada:
        pt = M.paint(cor, a, stroke=5); pt.setPathEffect(skia.DashPathEffect.Make([12, 9], 0))
        c.drawCircle(x, hy, r, pt)
        M.line(c, x, hy + r, x, yb - h * 0.45, cor, a, 5, dash=[12, 9])
        for dx in (-1, 1):
            M.line(c, x, yb - h * 0.45, x + dx * h * 0.08, yb, cor, a, 5, dash=[12, 9])
            M.line(c, x, yb - h * 0.75, x + dx * h * 0.1, yb - h * 0.5, cor, a, 5, dash=[12, 9])
        return
    c.drawCircle(x, hy, r, M.paint(cor, a))
    M.rrect(c, x - h * 0.07, hy + r * 1.1, h * 0.14, h * 0.38, h * 0.05, cor, a)
    for dx in (-1, 1):
        M.line(c, x + dx * h * 0.03, yb - h * 0.46, x + dx * h * 0.05, yb, cor, a, max(6, h * 0.045))
        M.line(c, x + dx * h * 0.06, yb - h * 0.78, x + dx * h * 0.1, yb - h * 0.5, cor, a, max(5, h * 0.035))
    c.drawCircle(x + olha * r * 0.55, yb - h * 170 / 180, max(3, r * 0.18), M.paint(BR, a))


def espelho_v(c, t, t0, x, y0, y1, lado=1):
    """espelho vertical com a hachura atrás (lado = 1: hachura à direita)"""
    F.espelho_plano(c, t, t0, (x, y1), (x, y0), lado=lado)


def ambulancia(c, x, y, size, a=1.0, espelhada=False):
    if a <= 0:
        return
    s = "AMBULÂNCIA"
    w = E.larg(s, "g", size)
    c.save()
    if espelhada:
        c.translate(x + w / 2, 0); c.scale(-1, 1); c.translate(-(x + w / 2), 0)
    M.rrect(c, x - 24, y - size * 0.95, w + 48, size * 1.3, 14, BR, a)
    E.escreve(c, s, x, y, size, "g", ERRADO, a)
    c.restore()


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def um():
        E.frase(c, t, C["s01.a"], ps("corpo inteiro no", "i", 76) + [("espelho", "g", 76, COR)], XE, 220, passo=0.12)
        E.frase(c, t, C["s01.b"], ps("do seu tamanho?", "i", 76), XE, 340, passo=0.12)
        E.foco(c, t, C["s01.c"], 0.4, lambda a: E.escreve(c, "não", XE, 520, 150, "g", COR, a))
        E.frase(c, t, C["s01.d"], [("metade", "g", 80, COR)] + ps("da sua altura", "i", 80), XE, 660, passo=0.12)
        E.frase(c, t, C["s01.e"], ps("e a distância", "i", 64) + [("não muda nada", "g", 64)], XE, 800, passo=0.12)
        yb, h = 960, 600
        E.foco(c, t, C["s01.a"], 0.5, lambda a: pessoa(c, 1250, yb, h, a))
        # espelho do tamanho da pessoa que encolhe para a metade
        q = ease_io(prog(t, C["s01.d"], 1.0))
        topo = lerp(yb - h, yb - (h + h * 170 / 180) / 2, q)
        base = lerp(yb, yb - h * 170 / 180 / 2, q)
        if t >= C["s01.a"] + 0.3:
            espelho_v(c, t, C["s01.a"] + 0.3, 1620, topo, base)
        if t >= C["s01.d"] + 1.0:
            E.foco(c, t, C["s01.d"] + 1.0, 0.4, lambda a: (M.line(c, 1700, topo, 1700, base, E.COR, a, 6),
                                                         E.escreve(c, "h ÷ 2", 1730, (topo + base) / 2 + 20, 56, "g", COR, a)))
    E.saida(c, t, C["s02"] - 0.1, um)
    if t >= C["s02"]:
        promessa(c, t, C, "s02", [("s02.b", "lei da reflexão"), ("s02.c", "imagem no espelho"), ("s02.d", "espelho mínimo")])


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    def raio_(a, x, y):
        M.line(c, x - 130, y + 40, x + 100, y - 40, E.COR, a, 6)
        F._cabeca(c, x - 10, y - 5, *_u((x - 130, y + 40), (x + 100, y - 40)), 26, E.COR, a)

    def reto(a, x, y):
        M.line(c, x - 80, y + 60, x + 100, y + 60, TINTA, a, 6); M.line(c, x - 80, y + 60, x - 80, y - 90, TINTA, a, 6)
        M.rrect(c, x - 80, y + 20, 40, 40, 0, E.COR, a * 0.3)
        E.escreve(c, "90°", x - 20, y + 10, 50, "g", COR, a)
    lembrete(c, t, C, "s03", [("s03.b", "a luz anda em linha reta:", "raio com seta"), ("s03.c", "ângulos em graus:", "o reto tem 90°")], (raio_, reto))


# ---------------- reflexão ----------------
def b_reflexao(c, t, C, b):
    E.frase(c, t, C["s04.a"], ps("bate e volta para o mesmo meio:", "i", 64), XE, 200, passo=0.1)
    E.frase(c, t, C["s04.b"], [("reflexão", "g", 110, COR)], XE, 340)
    y = 820
    # lisa: regular
    q = ep(t, C["s04.c"], 0.5)
    if q > 0:
        M.rrect(c, 230, y, 680, 22, 4, "#C9D3DC", q); M.line(c, 230, y, 910, y, TINTA, q, 5)
    for i in range(3):
        x = 440 + 110 * i
        F.raio(c, t, C["s04.c"] + 0.2 + 0.15 * i, [(x - 220, y - 330), (x, y), (x + 220, y - 330)], d=1.0, largura=5)
    E.foco(c, t, C["s04.c"] + 0.6, 0.4, lambda a: (centro(c, "superfície lisa", 570, y + 90, 50, "b", TINTA, a), centro(c, "paralelos voltam paralelos", 570, y + 150, 44, "i", TINTA2, a)))
    # áspera: difusa
    if t >= C["s04.d"]:
        a = ep(t, C["s04.d"], 0.5)
        p = skia.Path(); p.moveTo(1060, y)
        for k in range(1, 18):
            p.lineTo(1060 + k * 40, y + (14 if k % 2 else -14))
        pt = M.paint(TINTA, a, stroke=5); pt.setStrokeJoin(skia.Paint.kRound_Join)
        c.drawPath(p, pt)
    for i, ang in enumerate((150, 110, 60, 30)):
        x = 1220 + 110 * i
        g = math.radians(ang)
        F.raio(c, t, C["s04.d"] + 0.2 + 0.12 * i, [(x - 220, y - 330), (x, y), (x + 260 * math.cos(g), y - 260 * math.sin(g))], d=1.0, largura=5)
    E.foco(c, t, C["s04.d"] + 0.6, 0.4, lambda a: (centro(c, "superfície áspera", 1400, y + 90, 50, "b", TINTA, a), centro(c, "cada raio para um lado", 1400, y + 150, 44, "i", TINTA2, a)))
    E.frase(c, t, C["s04.e"], ps("você vê de", "i", 56, TINTA2) + [("qualquer canto", "g", 56, COR)], 1060, 340, passo=0.1)


# ---------------- a lei ----------------
P0 = (1230, 820)


def cena_lei(c, t, t_esp, t_norm, reto=None):
    F.espelho_plano(c, t, t_esp, (730, P0[1]), (1730, P0[1]), lado=-1)
    F.normal(c, t, t_norm, P0, 90, 430)
    if reto is not None and t >= reto:
        E.angulo(c, t, reto, P0, (P0[0] + 200, P0[1]), (P0[0], P0[1] - 200), None, r=70, cor=TINTA2)


def b_lei(c, t, C, b):
    def s05():
        E.frase(c, t, C["s05.a"], [("a", "i", 90), ("normal", "g", 90, COR)], XE, 300)
        E.frase(c, t, C["s05.b"], [("90°", "g", 70), ("do", "i", 70), ("espelho", "i", 70)], XE, 420, passo=0.12)
        E.foco(c, t, C["s05.b"] + 0.3, 0.4, lambda a: E.escreve(c, "onde o raio bate", XE, 520, 52, "i", TINTA2, a))
        cena_lei(c, t, C["s05"], C["s05.a"], C["s05.b"])
    E.saida(c, t, C["s06"] - 0.1, s05)
    if C["s06"] <= t < C["s07"]:
        def s06():
            T0 = C["s06"] - 0.6
            cena_lei(c, t, T0, T0)
            A = (P0[0] - 330, P0[1] - 400)
            B = (P0[0] + 330, P0[1] - 400)
            N = (P0[0], P0[1] - 300)
            F.raio(c, t, C["s06.a"], [A, P0], d=0.8)
            E.angulo(c, t, C["s06.a"] + 0.8, P0, A, N, "i", r=120, size=56)
            F.raio(c, t, C["s06.b"], [P0, B], d=0.8)
            E.angulo(c, t, C["s06.b"] + 0.8, P0, N, B, "r", r=120, size=56)
            E.frase(c, t, C["s06.a"], [("incidência", "g", 64), ("i", "g", 64, COR)], XE, 300, passo=0.12)
            E.frase(c, t, C["s06.b"], [("reflexão", "g", 64), ("r", "g", 64, COR)], XE, 410, passo=0.12)
            E.foco(c, t, C["s06.c"], 0.5, lambda a: E.formula(c, "r = i", XE, 600, 150, "g", COR, a))
            pilula_esq(c, t, C["s06.d"], "mesmo plano", XE, 760, 50, TINTA)
        E.saida(c, t, C["s07"] - 0.1, s06)
    if t < C["s07"]:
        return
    # s07: o erro de medir pelo espelho
    T0 = C["s07"] - 0.6
    cena_lei(c, t, T0, T0)
    g = math.radians(150)
    A = (P0[0] + 470 * math.cos(g), P0[1] - 470 * math.sin(g))
    F.raio(c, t, C["s07"], [A, P0], d=0.8)
    E.frase(c, t, C["s07"], [("cuidado", "g", 90, ERRADO)], XE, 260)
    E.frase(c, t, C["s07.a"], ps("medir do", "i", 64) + [("espelho", "g", 64, ERRADO)], XE, 380, passo=0.12)
    E.angulo(c, t, C["s07.b"], P0, (P0[0] - 300, P0[1]), A, "30°", r=170, cor=ERRADO, size=48)
    E.angulo(c, t, C["s07.c"], P0, A, (P0[0], P0[1] - 300), "60°", r=110, size=50)
    E.foco(c, t, C["s07.c"], 0.5, lambda a: E.escreve(c, "i = 90 − 30 = 60°", XE, 560, 76, "g", TINTA, a))
    pilula_esq(c, t, C["s07.d"], "sempre a partir da normal", XE, 720, 46, E.COR)


# ---------------- a imagem ----------------
XM = 1060  # espelho vertical


def b_imagem(c, t, C, b):
    if t < C["s10"]:
        def s08_09():
            O, Oi = (760, 640), (2 * XM - 760, 640)
            espelho_v(c, t, C["s08"] - 0.4, XM, 240, 960)
            E.foco(c, t, C["s08"], 0.4, lambda a: (E.bola(c, *O, 26, TINTA, a), centro(c, "objeto", O[0], O[1] + 80, 44, "i", TINTA2, a)))
            for i, yh in enumerate((462, 505, 548)):
                Hh = (XM, yh)
                u = _u(Oi, Hh)
                fim = (Hh[0] + u[0] * 700, Hh[1] + u[1] * 700)
                F.raio(c, t, C["s08.b"] + 0.25 * i, [O, Hh, fim], d=1.3, largura=5)
                prolonga(c, t, C["s08.c"] + 0.3 * i, Hh, Oi)
            E.foco(c, t, C["s08.c"] - 0.3, 0.4, lambda a: olho(c, 400, 210, 40, a, 1))
            E.foco(c, t, C["s08.d"], 0.5, lambda a: (E.bola(c, *Oi, 24, F.VEL, a * 0.75), centro(c, "imagem", Oi[0], Oi[1] + 80, 48, "g", F.VEL, a)))
            E.frase(c, t, C["s08.a"], ps("atrás do", "i", 70) + [("espelho?", "g", 70, COR)], 1180, 230, passo=0.12)
            E.frase(c, t, C["s08.c"], ps("o olho segue", "i", 54, TINTA2) + ps("para trás", "g", 54), 1180, 330, passo=0.1)
            if t >= C["s09"]:
                pilula_em(c, t, C["s09.a"], "VIRTUAL", 1500, 860, 70, F.VEL)
                E.foco(c, t, C["s09.a"] + 0.6, 0.4, lambda a: centro(c, "só prolongamentos", 1500, 970, 46, "i", TINTA2, a))
        E.saida(c, t, C["s10"] - 0.1, s08_09)
        return
    # s10–s11: simétrica
    yb, h, xo = 820, 300, 640
    xi = 2 * XM - xo
    espelho_v(c, t, C["s10"] - 0.4, XM, 300, 900)
    if t < C["s11"]:
        objeto_o(c, t, C["s10"], xo, yb, h)
        imagem_i(c, t, C["s10.a"], xi, yb, h, real=False)
        E.segmento(c, t, C["s10.b"], (xo, yb + 70), (XM, yb + 70), "d", cor=TINTA2, largura=4, lado=-1, size=52)
        E.segmento(c, t, C["s10.b"] + 0.5, (XM, yb + 70), (xi, yb + 70), "d", cor=TINTA2, largura=4, lado=-1, size=52)
        E.frase(c, t, C["s10.a"], [("simétrica", "g", 76, COR)], XE, 200)
        classifica(c, t, [(C["s10.c"], "mesmo tamanho"), (C["s10.d"], "direita")], XE, 300, 44)
        if t >= C["s10.e"]:
            E.foco(c, t, C["s10.e"], 0.4, lambda a: (M.line(c, xo - 60, yb - h * 0.6, xo + 60, yb - h * 0.6, TINTA, a, 6),
                                                     E.escreve(c, "D", xo + 70, yb - h * 0.6 + 18, 44, "g", TINTA, a),
                                                     M.line(c, xi - 60, yb - h * 0.6, xi + 60, yb - h * 0.6, F.VEL, a, 6),
                                                     E.escreve(c, "D", xi - 100, yb - h * 0.6 + 18, 44, "g", F.VEL, a)))
        E.foco(c, t, C["s10.f"], 0.5, lambda a: ambulancia(c, 1260, 300, 64, a, espelhada=True))
        E.foco(c, t, C["s10.f"] + 1.4, 0.5, lambda a: ambulancia(c, 1260, 420, 64, a))
        return
    pessoa(c, xo, yb, h, 1.0)
    E.foco(c, t, C["s11.b"], 0.5, lambda a: pessoa(c, xi, yb, h, a, F.VEL, -1, tracejada=True))
    E.segmento(c, t, C["s11.a"], (xo, yb + 70), (XM, yb + 70), "2 m", cor=TINTA2, largura=4, lado=-1, size=52)
    E.segmento(c, t, C["s11.b"], (XM, yb + 70), (xi, yb + 70), "2 m", cor=TINTA2, largura=4, lado=-1, size=52)
    E.segmento(c, t, C["s11.c"], (xo, yb + 170), (xi, yb + 170), "4 m", cor=E.COR, largura=6, lado=-1, size=60)
    E.frase(c, t, C["s11.a"], ps("você a", "i", 70) + [("2 m", "g", 70, COR)], XE, 220, passo=0.12)
    E.frase(c, t, C["s11.c"], ps("você e a imagem:", "i", 70) + [("4 m", "g", 70, COR)], XE + 820, 220, passo=0.12)


# ---------------- altura mínima ----------------
K = 3.0  # pixels por centímetro
XP, YB, XS = 470, 980, 1000  # pessoa, chão, espelho


def cena_altura(c, t, tp, tpe, tca, tesp=None, escuro=False, xp=XP, xs=XS):
    hp, ho = 180 * K, 170 * K
    pe, olho_, topo = (xp, YB), (xp + 10, YB - ho), (xp, YB - hp)
    E.foco(c, t, tp, 0.5, lambda a: pessoa(c, xp, YB, hp, a, BR if escuro else TINTA))
    if t >= tp:
        M.line(c, xp - 300, YB, xs + 300, YB, BR if escuro else TINTA, ep(t, tp, 0.4), 4)
    y_pe, y_ca = YB - ho / 2, YB - (hp + ho) / 2
    F.raio(c, t, tpe, [pe, (xs, y_pe), olho_], d=1.2, largura=5)
    F.raio(c, t, tca, [topo, (xs, y_ca), olho_], d=1.2, largura=5)
    if tesp is not None and t >= tesp:
        espelho_v(c, t, tesp, xs, y_ca, y_pe)
    return y_pe, y_ca


def b_altura(c, t, C, b):
    xt = 1180
    if t < C["s13"]:
        cena_altura(c, t, C["s12.a"], C["s12.b"], C["s12.c"])
        if t >= C["s12.a"]:
            M.line(c, XS, 260, XS, YB, TINTA2, 0.35 * ep(t, C["s12.a"], 0.4), 4, dash=E.TRACO)
        E.frase(c, t, C["s12.a"], [("180 cm", "g", 70, COR)] + ps("de altura", "i", 70), xt, 300, passo=0.12)
        E.frase(c, t, C["s12.a"] + 0.8, ps("olhos a", "i", 60, TINTA2) + [("170 cm", "g", 60)], xt, 400, passo=0.12)
        E.frase(c, t, C["s12.b"], ps("luz do", "i", 60) + [("pé", "g", 60, COR)] + ps("sobe até o olho", "i", 60), xt, 560, passo=0.1)
        E.frase(c, t, C["s12.c"], ps("luz da", "i", 60) + [("cabeça", "g", 60, COR)] + ps("desce", "i", 60), xt, 680, passo=0.1)
        return
    T0 = C["s13"] - 0.6
    y_pe, y_ca = cena_altura(c, t, T0, T0, T0, C["s13.a"])
    q = ep(t, C["s13.a"] + 0.4, 0.5)
    if q > 0:
        M.line(c, XS, y_ca, XS, y_pe, E.COR, q, 14)
    E.segmento(c, t, C["s13.b"], (XS + 90, y_ca), (XS + 90, y_pe), None, cor=E.COR, largura=4)
    E.foco(c, t, C["s13.c"], 0.5, lambda a: F.medida(c, 90, "cm", XS + 130, (y_ca + y_pe) / 2 + 30, 76, COR, a))
    E.segmento(c, t, C["s13.d"], (XS + 90, y_pe + 14), (XS + 90, YB), None, cor=TINTA2, largura=4)
    E.foco(c, t, C["s13.e"], 0.5, lambda a: F.medida(c, 85, "cm", XS + 130, (y_pe + YB) / 2 + 30, 64, TINTA, a))
    xt2 = 1380
    E.frase(c, t, C["s13.b"], [("metade", "g", 66, COR)] + ps("da altura", "i", 66), xt2, 260, passo=0.12)
    E.foco(c, t, C["s13.c"], 0.4, lambda a: E.escreve(c, "180 ÷ 2 = 90 cm", xt2, 370, 60, "g", TINTA, a))
    E.frase(c, t, C["s13.d"], [("borda", "g", 60), ("de", "i", 60), ("baixo:", "i", 60)], xt2, 560, passo=0.1)
    E.foco(c, t, C["s13.e"], 0.4, lambda a: E.escreve(c, "170 ÷ 2 = 85 cm", xt2, 660, 60, "g", TINTA, a))


# ---------------- atalho (palco) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    h = 420
    ybb = 900

    def cena(xp, xs, a_img, a_cone, t_):
        xi = 2 * xs - xp
        pessoa(c, xp, ybb, h, 1.0, BR, 1)
        M.line(c, xs, 330, xs, ybb, CLARO, 0.35, 4, dash=E.TRACO)
        pessoa(c, xi, ybb, h, a_img, CLARO, -1, tracejada=True)
        M.line(c, xp - 200, ybb, xi + 200, ybb, BR, 1.0, 3)
        ey = ybb - h * 170 / 180
        if a_cone > 0:
            p = skia.Path(); p.moveTo(xp + 8, ey); p.lineTo(xi, ybb - h); p.lineTo(xi, ybb); p.close()
            c.drawPath(p, M.paint(E.COR, 0.22 * a_cone))
            M.line(c, xp + 8, ey, xi, ybb - h, E.COR, a_cone, 4); M.line(c, xp + 8, ey, xi, ybb, E.COR, a_cone, 4)
            ya, yb_ = lerp(ey, ybb - h, 0.5), lerp(ey, ybb, 0.5)
            M.line(c, xs, ya, xs, yb_, BR, a_cone, 14)
        return xi

    if t < C["s15"]:
        E.frase(c, t, C["s14"], ps("o atalho, e o", "i", 70, CLARO) + [("motivo", "g", 70, BR)], W / 2, 170, "center", 0.12)
        a_img = ep(t, C["s14.a"], 0.5)
        cena(560, 960, a_img, ep(t, C["s14.c"], 0.6), t)
        E.foco(c, t, C["s14.b"], 0.4, lambda a: pilula_em(c, t, C["s14.b"], "espelho no meio do caminho", 960, 280, 44, E.COR))
        E.frase(c, t, C["s14.d"], ps("corte na", "i", 60, CLARO) + [("metade da distância", "g", 60, BR)], W / 2, 1010, "center", 0.1)
        return
    q = ease_io(prog(t, C["s15.b"], 2.0))
    xp = lerp(560, 360, q)
    cena(xp, 960, 1.0, 1.0, t)
    E.frase(c, t, C["s15.a"], ps("semelhança:", "i", 60, CLARO) + [("metade da altura", "g", 60, BR)], W / 2, 170, "center", 0.12)
    E.frase(c, t, C["s15.c"], ps("afastou?", "i", 56, CLARO) + [("a metade não muda", "g", 56, BR)], W / 2, 280, "center", 0.1)
    E.foco(c, t, C["s15.d"], 0.5, lambda a: centro(c, "mínimo = altura ÷ 2", W / 2, 975, 66, "g", BR, a))
    E.foco(c, t, C["s15.e"], 0.5, lambda a: centro(c, "borda de baixo = olhos ÷ 2", W / 2, 1050, 46, "b", CLARO, a))


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s16"], ps("hora de testar", "i", 72, COR), XE, 190)
    E.foco(c, t, C["s16.a"], 0.4, lambda a: (E.escreve(c, "altura:", XE, 340, 62, "i", TINTA, a), F.medida(c, 160, "cm", XE + 250, 340, 72, COR, a)))
    E.foco(c, t, C["s16.b"], 0.4, lambda a: (E.escreve(c, "olhos:", XE, 460, 62, "i", TINTA, a), F.medida(c, 150, "cm", XE + 250, 460, 72, COR, a)))
    E.frase(c, t, C["s16.c"], ps("altura mínima do", "i", 66) + [("espelho?", "g", 66, COR)], XE, 640, passo=0.12)
    E.frase(c, t, C["s16.d"], [("borda de baixo:", "g", 62)] + ps("a que altura?", "i", 66), XE, 770, passo=0.12)
    if t < C["s17"]:
        E.foco(c, t, C["s16.a"], 0.5, lambda a: (pessoa(c, 1420, 960, 160 * 3.2, a), espelho_v(c, t, C["s16.a"], 1720, 380, 820)))
        if t >= C["s16.a"]:
            M.line(c, 1200, 960, 1820, 960, TINTA, ep(t, C["s16.a"], 0.4), 4)
    questao_relogio(c, t, C, "s17")


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    E.frase(c, t, C["s18.a"], [("mínimo", "g", 64)] + ps("= metade da altura", "i", 64), XE, 230, passo=0.12)
    E.foco(c, t, C["s18.b"], 0.5, lambda a: E.escreve(c, "160 ÷ 2 =", XE, 400, 96, "g", TINTA, a))
    bola_txt(c, t, C["s18.b"] + 1.0, "80 cm", XE + 680, 370, 110, 64)
    E.frase(c, t, C["s18.c"], [("borda", "g", 64)] + ps("= metade dos olhos", "i", 64), XE, 600, passo=0.12)
    E.foco(c, t, C["s18.d"], 0.5, lambda a: E.escreve(c, "150 ÷ 2 =", XE, 770, 96, "g", TINTA, a))
    bola_txt(c, t, C["s18.d"] + 1.0, "75 cm", XE + 680, 740, 110, 64)
    pilula_em(c, t, C["s18.e"], "a distância não entrou na conta", 1440, 960, 46, F.VEL)
    if t >= C["s18.a"]:
        y_pe, y_ca = YB - 150 * 3.0 / 2, YB - (160 + 150) * 3.0 / 2
        a = ep(t, C["s18.a"], 0.5)
        pessoa(c, 1300, 900, 160 * 3.0, a)
        M.line(c, 1150, 900, 1800, 900, TINTA, a, 4)
        espelho_v(c, t, C["s18.a"] + 0.2, 1650, 900 - 155 * 3.0, 900 - 75 * 3.0)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def r():
        resumo(c, t, C, "s19", [("s19.a", [("r = i,", "g", 62, COR), ("medidos da", "i"), ("normal", "g")]),
                                ("s19.b", [("imagem:", "g"), ("virtual,", "i"), ("simétrica,", "i"), ("mesmo tamanho", "i")]),
                                ("s19.c", [("espelho mínimo:", "g"), ("metade da altura", "g", 62, COR)])], y0=380, dy=200)
    E.saida(c, t, C["s20"] - 0.1, r)
    if t < C["s20"]:
        return

    def desenho():
        for k, (cx, conc, tk, nome) in enumerate(((520, True, "s20.b", "maquiagem"), (900, False, "s20.c", "retrovisor"))):
            if t >= C[tk]:
                espelho_curvo(c, t, C[tk], cx, 790, 260, 150, conc)
                E.foco(c, t, C[tk] + 0.3, 0.4, lambda a, cx=cx, nome=nome: centro(c, nome, cx - 30, 1010, 46, "i", TINTA2, a))
    proxima(c, t, C, "s20", [("o espelho", "i", 100), ("fica curvo", "g", 100, COR)], [("maquiagem", "g", 72), ("e", "i", 72), ("retrovisor", "g", 72)],
            desenho, k_insc="d", k_bons="e")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, reflexao=b_reflexao, lei=b_lei, imagem=b_imagem, altura=b_altura,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
