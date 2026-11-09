"""Visual — Estudativo · FIS-OPT-010: praticando espelhos, lentes e olho (aula de prática, 5 questões).
Segue a linguagem visual da trilha Óptica, escrita no cabeçalho do visual.py da FIS-OPT-001. Cada questão tem a mesma forma:
pílula "questão N", dados à esquerda e um desenho pequeno à direita; na pausa, o relógio; na resposta, a conta em coluna
e o resultado na esfera. Os diagramas de espelho e lente usam a mesma equação da conta (raios_espelho, raios_lente).
Todo instante vem de C[...] (marcadores do roteiro)."""
import math
from fractions import Fraction as Fr

import editorial as E
import fisica as F
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Física", "Óptica")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_FIS-OPT-010_praticando_espelhos_lentes_olho.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("q1", "q2", "q3", "q4", "q5", "fim"))


def _pl(f, p):
    return Fr(f) * p / (p - f)


# todas as contas da aula
assert 190 / 2 == 95 and 180 / 2 == 90                                                # questão 1
assert _pl(-2, 8) == Fr(-16, 10) == Fr(-8, 5) and -_pl(-2, 8) / 8 == Fr(1, 5)          # questão 2: −1,6 m e 0,2
assert -2 * 8 == -16 and 8 - (-2) == 10
assert abs(math.degrees(math.asin(1 / 2)) - 30) < 1e-9 and 40 > 30 and 20 < 30         # questão 3
assert _pl(12, 8) == -24 and 12 * 8 == 96 and 8 - 12 == -4 and -_pl(12, 8) / 8 == 3    # questão 4
assert 100 / 5 == 20 and abs(1 / 0.2 - 5) < 1e-12                                      # questão 5


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
def pessoa(c, x, yb, h, a=1.0, cor=None):
    if a <= 0:
        return
    cor = cor or TINTA
    r = h * 0.065
    hy = yb - h + r
    c.drawCircle(x, hy, r, M.paint(cor, a))
    M.rrect(c, x - h * 0.07, hy + r * 1.1, h * 0.14, h * 0.38, h * 0.05, cor, a)
    for dx in (-1, 1):
        M.line(c, x + dx * h * 0.03, yb - h * 0.46, x + dx * h * 0.05, yb, cor, a, max(6, h * 0.045))
        M.line(c, x + dx * h * 0.06, yb - h * 0.78, x + dx * h * 0.1, yb - h * 0.5, cor, a, max(5, h * 0.035))


def selo_q(c, t, t0, n):
    pilula_esq(c, t, t0, f"questão {n}", XE, 190, 50, E.COR)


def receita(c, cx, cy, grau, a=1.0, w=440):
    if a <= 0:
        return
    M.rrect(c, cx - w / 2, cy - 150, w, 300, 20, BR, a, shadow=True)
    E.escreve(c, "receita", cx - w / 2 + 40, cy - 80, 44, "i", TINTA2, a)
    M.line(c, cx - w / 2 + 40, cy - 60, cx + w / 2 - 40, cy - 60, FIO, a, 3)
    E.escreve(c, grau, cx - w / 2 + 40, cy + 80, 110, "g", COR, a)


def eixo(c, t, t0, x0, x1, cy):
    if t >= t0:
        M.line(c, x0, cy, x1, cy, TINTA, 0.5, 3, dash=E.TRACO, progress=ease_io(prog(t, t0, 0.6)))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def um():
        E.frase(c, t, C["s01.a"], [("5", "g", 220, COR), ("questões", "i", 120)], XE, 420, passo=0.2)
        E.frase(c, t, C["s01.b"], ps("do espelho aos", "i", 80) + [("óculos", "g", 80, COR)], XE, 580, passo=0.12)
        E.frase(c, t, C["s01.c"], [("pause,", "g", 64), ("tente,", "g", 64), ("confira", "g", 64, COR)], XE, 760, passo=0.2)
        E.frase(c, t, C["s01.d"], ps("o caminho e o", "i", 60) + [("atalho", "g", 60, COR)], XE, 870, passo=0.12)
        E.foco(c, t, C["s01.a"] + 0.4, 0.8, lambda a: E.simbolo(c, 1500, 560, 300 * ease_back(prog(t, C["s01.a"] + 0.4, 0.8)), giro=12 * math.sin(t * 0.4)), blur=0)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t < C["s02"]:
        return
    E.frase(c, t, C["s02.a"], ps("três", "i", 80) + [("lembretes", "g", 80, COR)], XE, 220, passo=0.12)
    linhas = (("s02.b", [("um espelho ou uma lente só:", "i", 54), ("real = invertida, virtual = direita", "g", 52)]),
              ("s02.c", [("côncavo e convergente:", "i", 58), ("f > 0", "g", 64, CERTO)]),
              ("s02.d", [("convexo e divergente:", "i", 58), ("f < 0", "g", 64, ERRADO)]),
              ("s02.e", [("ângulos:", "i", 58), ("a partir da normal", "g", 58, COR)]))
    for i, (k, partes) in enumerate(linhas):
        y = 400 + 150 * i
        E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, XE + 40, y - 24, 38, a=a), centro(c, str(i + 1), XE + 40, y - 2, 46, "g", BR, a)))
        E.frase(c, t, C[k] + 0.1, partes, XE + 110, y, passo=0.1)


# ---------------- 1: espelho plano ----------------
def b_q1(c, t, C, b):
    selo_q(c, t, C["s03.a"], 1)
    E.frase(c, t, C["s03.b"], ps("clientes de até", "i", 62) + [("190 cm", "g", 62, COR)] + ps("se veem inteiros", "i", 62), XE, 340, passo=0.1)
    E.frase(c, t, C["s03.c"], ps("altura mínima do", "i", 62) + [("espelho?", "g", 62, COR)], XE, 470, passo=0.1)
    E.frase(c, t, C["s03.d"], ps("se afastar:", "i", 58) + [("espelho maior?", "g", 58, COR)], XE, 590, passo=0.1)
    E.frase(c, t, C["s03.e"], ps("olhos a", "i", 58) + [("180 cm:", "g", 58, COR)] + ps("borda de baixo?", "i", 58), XE, 710, passo=0.1)
    if t < C["s04"]:
        E.foco(c, t, C["s03.b"], 0.5, lambda a: (pessoa(c, 1450, 960, 520, a), F.espelho_plano(c, t, C["s03.b"], (1760, 830), (1760, 450), lado=1)))
        if t >= C["s03.b"]:
            M.line(c, 1250, 960, 1840, 960, TINTA, ep(t, C["s03.b"], 0.4), 4)
    questao_relogio(c, t, C, "s04")


def b_r1(c, t, C, b):
    E.frase(c, t, C["s05.a"], [("mínimo", "g", 64)] + ps("= metade da altura", "i", 64), XE, 220, passo=0.12)
    E.foco(c, t, C["s05.b"], 0.4, lambda a: E.escreve(c, "190 ÷ 2 =", XE, 380, 90, "g", TINTA, a))
    bola_txt(c, t, C["s05.b"] + 1.0, "95 cm", XE + 640, 350, 110, 60)
    E.frase(c, t, C["s05.c"], [("afastou?", "g", 60)] + ps("não precisa de espelho maior", "i", 60), XE, 560, passo=0.1)
    E.frase(c, t, C["s05.d"], ps("a imagem se afasta junto,", "i", 54, TINTA2) + [("o espelho segue no meio", "g", 52)], XE, 660, passo=0.08)
    pilula_esq(c, t, C["s05.e"], "a metade não muda", XE, 760, 46, E.COR)
    E.frase(c, t, C["s05.f"], [("borda", "g", 60)] + ps("= metade dos olhos:", "i", 60), XE, 920, passo=0.1)
    E.foco(c, t, C["s05.g"], 0.4, lambda a: E.escreve(c, "180 ÷ 2 = 90 cm", XE + 760, 920, 70, "g", COR, a))


# ---------------- 2: retrovisor convexo ----------------
def b_q2(c, t, C, b):
    selo_q(c, t, C["s06.a"], 2)
    E.frase(c, t, C["s06.b"], ps("retrovisor", "i", 62) + [("convexo,", "g", 62, COR)] + ps("foco de", "i", 62) + [("2 m", "g", 62, COR)], XE, 340, passo=0.1)
    E.frase(c, t, C["s06.c"], ps("carro a", "i", 62) + [("8 m", "g", 62, COR)] + ps("atrás", "i", 62), XE, 460, passo=0.1)
    E.frase(c, t, C["s06.d"], [("onde", "g", 62, COR)] + ps("fica a imagem?", "i", 62), XE, 600, passo=0.1)
    E.frase(c, t, C["s06.e"], ps("quantas vezes", "i", 62) + [("menor?", "g", 62, COR)], XE, 720, passo=0.1)
    if t < C["s07"]:
        if t >= C["s06.b"]:
            espelho_curvo(c, t, C["s06.b"], 1700, 620, 520, 220, False)
            eixo(c, t, C["s06.b"], 1100, 1840, 620)
        E.foco(c, t, C["s06.c"], 0.5, lambda a: F.carrinho(c, 1250, 620, 200, a=a))
    questao_relogio(c, t, C, "s07")


def b_r2(c, t, C, b):
    x = XE
    if t < C["s09"]:
        E.foco(c, t, C["s08.a"], 0.4, lambda a: E.formula(c, "convexo: f = −2", x, 230, 72, "g", ERRADO, a))
        E.formula_em(c, t, C["s08.b"], "p' = f{f · p}{p − f}", x, 430, 90, "g", TINTA2)
        E.formula_em(c, t, C["s08.c"], "= f{(−2) · 8}{8 − (−2)}", x, 650, 90, "g", TINTA)
        E.formula_em(c, t, C["s08.d"], "= f{−16}{10}", x + 720, 650, 90, "g", TINTA)
        bola_txt(c, t, C["s08.e"], "−1,6 m", 1560, 620, 120, 60)
        pilula_esq(c, t, C["s08.e"] + 0.6, "virtual, atrás do espelho", x, 880, 46, F.VEL)
        return
    vx, cy, f = 1660, 560, 200
    eixo(c, t, C["s09"] - 0.6, 760, 1860, cy)
    espelho_curvo(c, t, C["s09"] - 0.6, vx, cy, 2 * f, 300, False)
    objeto_o(c, t, C["s09"] - 0.5, vx - 4 * f, cy, 160)
    xi, hi = raios_espelho(c, t, (C["s09"] - 0.4, C["s09"] - 0.2), vx, cy, f, vx - 4 * f, 160, False, ("par", "centro"))
    imagem_i(c, t, C["s09.a"], xi, cy, hi, False)
    E.formula_em(c, t, C["s09.a"], "A = −f{(−1,6)}{8}", x, 300, 90, "g", TINTA)
    E.formula_em(c, t, C["s09.b"], "= 0,2", x + 560, 300, 90, "g", COR)
    classifica(c, t, [(C["s09.c"], "direita"), (C["s09.c"] + 0.3, "5 vezes menor")], x, 500, 50)
    E.frase(c, t, C["s09.d"], ps("objetos", "i", 54) + [("mais perto do que parecem", "g", 54, COR)], x, 900, passo=0.1)
    E.foco(c, t, C["s09.d"] + 1.0, 0.4, lambda a: E.escreve(c, "a imagem pequena engana o cérebro", x, 990, 46, "i", TINTA2, a))


# ---------------- 3: ângulo limite ----------------
def b_q3(c, t, C, b):
    selo_q(c, t, C["s10.a"], 3)
    E.frase(c, t, C["s10.b"], ps("de um material de", "i", 62) + [("n = 2", "g", 62, COR)] + ps("para o ar", "i", 62), XE, 340, passo=0.1)
    E.frase(c, t, C["s10.c"], ps("chegando a", "i", 62) + [("40°", "g", 62, COR)] + ps("da normal", "i", 62), XE, 460, passo=0.1)
    E.frase(c, t, C["s10.d"], [("sai", "g", 66, COR), ("ou", "i", 70), ("reflete por inteiro?", "g", 66)], XE, 620, passo=0.12)
    if t < C["s11"]:
        P, cy = (1450, 520), 520
        q = ep(t, C["s10.b"], 0.5)
        if q > 0:
            c.drawRect(skia.Rect.MakeLTRB(1100, cy, 1820, 900), M.paint(VIDRO, 0.45 * q))
            M.line(c, 1100, cy, 1820, cy, TINTA, q, 5)
            E.formula(c, "ar", 1800, cy - 30, 48, "b", TINTA, q, "right"); E.formula(c, "n = 2", 1800, cy + 70, 48, "b", TINTA, q, "right")
        F.normal(c, t, C["s10.c"], P, 90, 300)
        g = math.radians(40)
        A = (P[0] - 330 * math.sin(g), P[1] + 330 * math.cos(g))
        F.raio(c, t, C["s10.c"] + 0.2, [A, P], d=0.6)
        E.angulo(c, t, C["s10.c"] + 0.8, P, (P[0], P[1] + 300), A, "40°", r=110, size=44)
    questao_relogio(c, t, C, "s11")


def b_r3(c, t, C, b):
    x = XE
    E.formula_em(c, t, C["s12.a"], "sen L = f{menor}{maior}", x, 260, 84, "g", TINTA2)
    E.formula_em(c, t, C["s12.b"], "= f{1}{2}", x + 600, 260, 84, "g", TINTA)
    E.foco(c, t, C["s12.c"], 0.4, lambda a: E.formula(c, "L =", 1250, 262, 84, "g", TINTA, a))
    bola_txt(c, t, C["s12.c"], "30°", 1500, 240, 110, 76)
    E.frase(c, t, C["s12.d"], [("40°", "g", 70, COR), (">", "g", 70, TINTA2), ("30°", "g", 70)] + ps("e vai do n maior para o menor", "i", 56), x, 520, passo=0.1)
    pilula_esq(c, t, C["s12.e"], "reflexão total: não sai", x, 640, 54, E.COR)
    E.frase(c, t, C["s12.f"], ps("a 20°, abaixo do limite:", "i", 56) + [("sairia", "g", 56)], x, 820, passo=0.1)


# ---------------- 4: lupa ----------------
def b_q4(c, t, C, b):
    selo_q(c, t, C["s13.a"], 4)
    E.frase(c, t, C["s13.b"], [("lupa:", "g", 62, COR)] + ps("convergente, foco de", "i", 62) + [("12 cm", "g", 62, COR)], XE, 340, passo=0.1)
    E.frase(c, t, C["s13.c"], ps("selo a", "i", 62) + [("8 cm", "g", 62, COR)], XE, 460, passo=0.1)
    E.frase(c, t, C["s13.d"], [("onde", "g", 62, COR)] + ps("fica a imagem?", "i", 62), XE, 600, passo=0.1)
    E.frase(c, t, C["s13.e"], ps("quantas vezes", "i", 62) + [("maior?", "g", 62, COR)], XE, 720, passo=0.1)
    if t < C["s14"]:
        if t >= C["s13.b"]:
            F.lente(c, t, C["s13.b"], 1550, 560, 340, True, 12 * 20, eixo=(1100, 1840))
        objeto_o(c, t, C["s13.c"], 1550 - 8 * 20, 560, 80)
    questao_relogio(c, t, C, "s14")


def b_r4(c, t, C, b):
    x = XE
    if t < C["s16"]:
        E.foco(c, t, C["s15.a"], 0.4, lambda a: E.formula(c, "convergente: f = +12", x, 230, 72, "g", CERTO, a))
        E.formula_em(c, t, C["s15.b"], "p' = f{12 · 8}", x, 450, 90, "g", TINTA) if t < C["s15.c"] else None
        E.formula_em(c, t, C["s15.c"], "p' = f{12 · 8}{8 − 12} = f{96}{−4}", x, 450, 90, "g", TINTA)
        bola_txt(c, t, C["s15.d"], "−24 cm", 1500, 420, 120, 60)
        pilula_esq(c, t, C["s15.e"], "virtual, do lado do selo", x, 700, 50, F.VEL)
        return
    cx, cy = 1560, 560
    F.lente(c, t, C["s16"] - 0.6, cx, cy, 380, True, 240, eixo=(860, 1840))
    objeto_o(c, t, C["s16"] - 0.5, cx - 160, cy, 70)
    xi, hi = raios_lente(c, t, (C["s16"] - 0.4, C["s16"] - 0.2), cx, cy, 240, cx - 160, 70)
    imagem_i(c, t, C["s16.a"], xi, cy, hi, False)
    E.formula_em(c, t, C["s16.a"], "A = −f{(−24)}{8}", x, 300, 90, "g", TINTA)
    E.formula_em(c, t, C["s16.b"], "= 3", x + 540, 300, 90, "g", COR)
    classifica(c, t, [(C["s16.c"], "direita"), (C["s16.c"] + 0.3, "3 vezes maior")], x, 500, 50)
    E.frase(c, t, C["s16.d"], ps("objeto dentro do foco:", "i", 56) + [("imagem de lupa", "g", 56, COR)], x, 900, passo=0.1)


# ---------------- 5: óculos ----------------
def b_q5(c, t, C, b):
    selo_q(c, t, C["s17.a"], 5)
    E.frase(c, t, C["s17.b"], ps("receita:", "i", 62) + [("−5 graus", "g", 62, COR)], XE, 340, passo=0.1)
    E.frase(c, t, C["s17.c"], ps("que", "i", 66) + [("lente?", "g", 66, COR)], XE, 480, passo=0.12)
    E.frase(c, t, C["s17.d"], ps("qual o", "i", 66) + [("foco?", "g", 66, COR)], XE, 600, passo=0.12)
    E.frase(c, t, C["s17.e"], ps("que", "i", 66) + [("defeito", "g", 66, COR)] + ps("corrige?", "i", 66), XE, 720, passo=0.12)
    if t < C["s18"]:
        E.foco(c, t, C["s17.b"], 0.5, lambda a: receita(c, 1450, 480, "−5,00", a))
    questao_relogio(c, t, C, "s18")


def b_r5(c, t, C, b):
    x = XE
    E.frase(c, t, C["s19.a"], ps("grau negativo:", "i", 62) + [("divergente", "g", 62, COR)], x, 230, passo=0.1)
    E.foco(c, t, C["s19.b"], 0.4, lambda a: E.formula(c, "f (cm) = 100 ÷ grau", x, 400, 76, "g", TINTA2, a))
    E.foco(c, t, C["s19.c"], 0.4, lambda a: E.formula(c, "100 ÷ 5 = 20 cm", x, 560, 90, "g", TINTA, a))
    bola_txt(c, t, C["s19.d"], "−20 cm", 1500, 530, 120, 60)
    E.frase(c, t, C["s19.e"], [("míope,", "g", 64, COR), ("menos:", "g", 64)] + ps("corrige a miopia", "i", 64), x, 780, passo=0.12)
    E.foco(c, t, C["s19.e"] + 1.2, 0.4, lambda a: E.escreve(c, "só vê nítido até 20 cm", x, 880, 50, "i", TINTA2, a))
    E.foco(c, t, C["s19.f"], 0.4, lambda a: E.escreve(c, "confira: 1 ÷ 0,2 m = 5", x, 990, 56, "b", TINTA, a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def r():
        E.frase(c, t, C["s20.a"], ps("todas saíram com um", "i", 76) + [("atalho", "g", 76, COR)], W / 2, 200, "center", 0.12)
        itens = (("s20.b", "espelho plano: metade da altura"), ("s20.c", "p' = f · p ÷ (p − f)"), ("s20.d", "sen L = menor ÷ maior"), ("s20.e", "f (cm) = 100 ÷ grau"))
        for i, (k, s) in enumerate(itens):
            y = 380 + 160 * i
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 300, y - 24, 48, a=a), centro(c, str(i + 1), 300, y - 2, 56, "g", BR, a)))
            E.foco(c, t, C[k] + 0.1, 0.5, lambda a, s=s, y=y: E.escreve(c, s, 390, y, 64, "g", TINTA, a))
    E.saida(c, t, C["s21"] - 0.1, r)
    if t < C["s21"]:
        return
    E.frase(c, t, C["s21.a"], [("errou", "i", 90), ("alguma?", "g", 90, COR)], XE, 300)
    E.frase(c, t, C["s21.a"] + 0.8, ps("procure no canal a aula do assunto", "i", 60), XE, 430, passo=0.1)
    E.frase(c, t, C["s21.a"] + 1.6, ps("e refaça a questão", "i", 60), XE, 520, passo=0.1)
    E.foco(c, t, C["s21.b"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 420, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s21.b"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(720, 445, p), ep(t, C["s21.b"] + 0.2, 0.4))
    E.frase(c, t, C["s21.c"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1570, 990, "center")


BLOCKS = dict(gancho=b_gancho, q1=b_q1, r1=b_r1, q2=b_q2, r2=b_r2, q3=b_q3, r3=b_r3, q4=b_q4, r4=b_r4, q5=b_q5, r5=b_r5, fim=b_fim)
