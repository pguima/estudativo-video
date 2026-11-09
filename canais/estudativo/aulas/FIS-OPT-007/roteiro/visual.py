"""Visual — Estudativo · FIS-OPT-007: equação das lentes e dioptria (o grau dos óculos).
Segue a linguagem visual da trilha Óptica, escrita no cabeçalho do visual.py da FIS-OPT-001. Contas em coluna (E.formula),
um passo por fala; resposta na esfera. Diagramas com raios_lente, que usa a mesma equação: a imagem desenhada cai onde
a conta manda (escalas indicadas em cada bloco).
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
ARQUIVO_FINAL = "estudativo_FIS-OPT-007_equacao_das_lentes_dioptria.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("equacao", "exemplo", "grau", "erro", "atalho", "questao", "fim"))


def _pl(f, p):
    return 1 / (Fr(1) / f - Fr(1) / p)


# todas as contas da aula
assert Fr(1, 10) - Fr(1, 6) == Fr(3, 30) - Fr(5, 30) == -Fr(2, 30) == -Fr(1, 15) and _pl(10, 6) == -15   # lupa
assert Fr(15, 6) == Fr(5, 2)                                                                                # A = 2,5
assert _pl(-15, 30) == Fr(-15 * 30, 30 + 15) == -10 and 15 * 30 == 450                                      # divergente
assert Fr(1) / Fr(1, 2) == 2 and Fr(1) / Fr(-1, 4) == -4                                                    # 50 cm → +2 di; −25 cm → −4 di
assert Fr(1, 50) == Fr(2, 100)                                                                              # o erro: 0,02
assert Fr(100, 4) == 25 and Fr(100) / Fr(5, 2) == 40 and Fr(100, 4) == 25                                   # atalho
assert _pl(25, 50) == 50 and 25 * 50 == 1250 and 1250 / 25 == 50 and -Fr(50, 50) == -1                      # questão


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
def diagrama(c, t, cx, cy, f, xo, ho, t_l, t_obj, ts, t_img, tipos=("par", "centro"), x0=None, x1=None, h=None):
    h = h or 420
    F.lente(c, t, t_l, cx, cy, h, f > 0, abs(f), eixo=(x0 if x0 is not None else cx - 800, x1 if x1 is not None else cx + 600))
    objeto_o(c, t, t_obj, xo, cy, ho)
    xi, hi = raios_lente(c, t, ts, cx, cy, f, xo, ho, tipos)
    imagem_i(c, t, t_img, xi, cy, hi, real=xi > cx)
    return xi, hi


def passos(c, t, linhas, x, y0, dy, size=80, escuro=False):
    for i, (ti, s, cor) in enumerate(linhas):
        E.formula_em(c, t, ti, s, x, y0 + i * dy, size, "g", cor or (BR if escuro else TINTA))


def receita(c, cx, cy, a=1.0, grau="+2,00"):
    """cartão de receita de óculos"""
    if a <= 0:
        return
    M.rrect(c, cx - 260, cy - 170, 520, 340, 20, BR, a, shadow=True)
    E.escreve(c, "receita", cx - 220, cy - 100, 44, "i", TINTA2, a)
    M.line(c, cx - 220, cy - 80, cx + 220, cy - 80, FIO, a, 3)
    E.escreve(c, "esférico", cx - 220, cy + 10, 40, "b", TINTA2, a)
    E.escreve(c, grau, cx - 220, cy + 110, 96, "g", COR, a)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def um():
        E.foco(c, t, C["s01.a"], 0.5, lambda a: receita(c, 1400, 360, a))
        E.frase(c, t, C["s01.a"], [("mais dois", "g", 84, COR), ("graus", "i", 84)], XE, 260, passo=0.12)
        E.frase(c, t, C["s01.b"], ps("é", "i", 70) + [("uma conta", "g", 70)], XE, 380, passo=0.12)
        E.foco(c, t, C["s01.c"], 0.5, lambda a: E.formula(c, "V = f{1}{f}", XE, 590, 120, "g", TINTA, a))
        E.foco(c, t, C["s01.c"] + 0.5, 0.4, lambda a: E.escreve(c, "f em metros", XE + 430, 580, 52, "i", COR, a))
        if t >= C["s01.d"]:
            F.lente(c, t, C["s01.d"], 1300, 820, 260, True, 250, eixo=(900, 1800))
            for k, dy in enumerate((-80, 80)):
                F.raio(c, t, C["s01.d"] + 0.3 + 0.1 * k, [(920, 820 + dy), (1300, 820 + dy), (1550, 820), (1700, 820 - dy * 150 / 250)], d=1.0, largura=5)
            E.segmento(c, t, C["s01.d"] + 0.8, (1300, 990), (1550, 990), "50 cm", cor=E.COR, largura=4, lado=-1, size=46)
            E.frase(c, t, C["s01.d"], [("convergente,", "g", 60), ("foco a", "i", 60), ("50 cm", "g", 60, COR)], XE, 820, passo=0.12)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t >= C["s02"]:
        promessa(c, t, C, "s02", [("s02.b", "a imagem de uma lente"), ("s02.c", "o grau dela")])


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    lembrete(c, t, C, "s03", [("s03.b", "equação dos espelhos:", "1/f = 1/p + 1/p' e o aumento"), ("s03.c", "as lentes:", "convergente e divergente")])


# ---------------- a equação ----------------
def b_equacao(c, t, C, b):
    if t < C["s05"]:
        cx, cy = 1250, 520
        diagrama(c, t, cx, cy, 200, cx - 300, 100, C["s04"], C["s04"] + 0.2, (C["s04"] + 0.4, C["s04"] + 0.7), C["s04"] + 1.6, x0=780, x1=1840, h=380)
        for i, (k, x0_, x1_, s, cor) in enumerate((("s04.b", cx - 300, cx, "p", TINTA), ("s04.c", cx, cx + 600, "p'", F.VEL), ("s04.d", cx, cx + 200, "f", E.COR))):
            E.segmento(c, t, C[k], (x0_, cy + 260 + 70 * i), (x1_, cy + 260 + 70 * i), s, cor=cor, largura=5, lado=-1, size=50)
        E.frase(c, t, C["s04.a"], ps("a", "i", 70) + [("mesma", "g", 70, COR)] + ps("dos espelhos", "i", 70), XE, 240, passo=0.12)
        E.formula_em(c, t, C["s04.a"] + 0.6, "f{1}{f} = f{1}{p} + f{1}{p'}", XE, 470, 100, "g", TINTA)
        E.formula_em(c, t, C["s04.e"], "A = −f{p'}{p}", XE, 720, 100, "g", TINTA)
        return
    E.formula_em(c, t, C["s05"] - 0.3, "f{1}{f} = f{1}{p} + f{1}{p'}", XE, 270, 90, "g", TINTA2)
    linhas = (("s05.a", "convergente: f > 0", ""), ("s05.b", "divergente: f < 0", ""),
              ("s05.c", "p' > 0", "real, do outro lado"), ("s05.d", "p' < 0", "virtual, do lado do objeto"))
    for i, (k, l, s) in enumerate(linhas):
        y = 480 + 120 * i
        E.foco(c, t, C[k], 0.4, lambda a, l=l, s=s, y=y, i=i: (E.formula(c, l, XE, y, 64, "g", (TINTA, TINTA, E.COR, F.VEL)[i], a),
                                                                E.escreve(c, s, XE + 300, y, 56, "i", TINTA2, a)))
    if t >= C["s05.c"] - 0.4:
        F.lente(c, t, C["s05.c"] - 0.4, 1500, 640, 340, True, None, eixo=(1150, 1850))
        E.foco(c, t, C["s05.c"], 0.4, lambda a: centro(c, "real", 1700, 880, 52, "g", E.COR, a))
        E.foco(c, t, C["s05.d"], 0.4, lambda a: centro(c, "virtual", 1300, 880, 52, "g", F.VEL, a))
        E.foco(c, t, C["s05.c"], 0.4, lambda a: centro(c, "luz →", 1250, 520, 44, "b", TINTA2, a))


# ---------------- exemplo ----------------
def b_exemplo(c, t, C, b):
    x = XE
    if t < C["s07"]:
        E.foco(c, t, C["s06.a"], 0.4, lambda a: E.formula(c, "lupa: f = 10", x, 230, 72, "g", COR, a))
        E.foco(c, t, C["s06.b"], 0.4, lambda a: E.formula(c, "p = 6", x + 600, 230, 72, "g", TINTA, a))
        passos(c, t, [(C["s06.c"], "f{1}{p'} = f{1}{10} − f{1}{6}", None),
                      (C["s06.e"], "= f{3}{30} − f{5}{30}", None),
                      (C["s06.f"], "= −f{2}{30} = −f{1}{15}", COR)], x, 440, 200, 86)
        pilula_em(c, t, C["s06.d"], "MMC (10, 6) = 30", 1400, 620, 50, E.COR)
        return
    if t < C["s08"]:
        cx, cy = 1520, 600
        diagrama(c, t, cx, cy, 300, cx - 180, 80, C["s07"] - 0.6, C["s07"] - 0.5, (C["s07"] - 0.4, C["s07"] - 0.2), C["s07.a"] + 0.4, x0=960, x1=1860, h=420)
        E.foco(c, t, C["s07.a"], 0.4, lambda a: E.formula(c, "p' = −15 cm", x, 260, 90, "g", TINTA, a))
        pilula_esq(c, t, C["s07.b"], "virtual, do lado do selo", x, 370, 44, F.VEL)
        E.formula_em(c, t, C["s07.c"], "A = −f{(−15)}{6}", x, 560, 90, "g", TINTA)
        E.formula_em(c, t, C["s07.d"], "= 2,5", x + 520, 560, 90, "g", COR)
        classifica(c, t, [(C["s07.e"], "direita"), (C["s07.e"] + 0.3, "2,5 vezes maior")], x, 760, 50)
        return
    cx, cy = 1450, 600
    diagrama(c, t, cx, cy, -300, cx - 600, 180, C["s08.a"], C["s08.c"], (C["s08.c"] + 0.3, C["s08.c"] + 0.6), C["s08.f"], x0=760, x1=1840, h=420)
    E.frase(c, t, C["s08.a"], [("divergente,", "g", 60, COR)] + ps("foco de 15 cm", "i", 60), x, 230, passo=0.1)
    E.foco(c, t, C["s08.b"], 0.4, lambda a: E.formula(c, "f = −15", x, 360, 76, "g", ERRADO, a))
    E.foco(c, t, C["s08.c"], 0.4, lambda a: E.formula(c, "p = 30", x + 340, 360, 76, "g", TINTA, a))
    E.formula_em(c, t, C["s08.d"], "p' = f{(−15) · 30}{30 + 15}", x, 560, 84, "g", TINTA)
    E.formula_em(c, t, C["s08.e"], "= f{−450}{45}", x, 760, 84, "g", TINTA)
    bola_txt(c, t, C["s08.f"], "−10 cm", x + 560, 730, 110, 56)
    classifica(c, t, [(C["s08.g"], "virtual"), (C["s08.g"] + 0.3, "direita"), (C["s08.g"] + 0.6, "menor")], x, 960, 50)


# ---------------- grau ----------------
def b_grau(c, t, C, b):
    if t < C["s10"]:
        E.frase(c, t, C["s09"], ps("o", "i", 76) + [("grau", "g", 76, COR)], XE, 230, passo=0.12)
        F.formula_legenda(c, t, C["s09.b"], "V = f{1}{f}", [("V", "vergência, o grau", "di"), ("f", "distância focal", "m")], XE + 40, 500, 150,
                          tl=[C["s09.a"] + 0.5, C["s09.c"]], size_l=56)
        pilula_esq(c, t, C["s09.c"] + 0.4, "f em metros", 1200, 470, 56, E.COR)
        E.frase(c, t, C["s09.d"], ps("unidade:", "i", 60) + [("dioptria (di)", "g", 60, COR)] + ps("= o grau da receita", "i", 60), XE, 960, passo=0.1)
        return
    if t < C["s11"]:
        x = XE
        E.foco(c, t, C["s10.a"], 0.4, lambda a: E.formula(c, "f = 50 cm = 0,5 m", x, 260, 76, "g", TINTA, a))
        E.formula_em(c, t, C["s10.b"], "V = f{1}{0,5}", x, 470, 96, "g", TINTA)
        bola_txt(c, t, C["s10.c"], "+2 di", x + 600, 440, 110, 60)
        E.foco(c, t, C["s10.d"], 0.4, lambda a: E.formula(c, "divergente, f = −25 cm", x, 680, 70, "g", TINTA, a))
        E.formula_em(c, t, C["s10.e"], "V = f{1}{−0,25}", x, 890, 96, "g", TINTA)
        bola_txt(c, t, C["s10.f"], "−4 di", x + 600, 860, 110, 60)
        return
    E.frase(c, t, C["s11.a"], ps("o sinal do grau é o", "i", 64) + [("sinal do foco", "g", 64, COR)], XE, 240, passo=0.12)
    E.frase(c, t, C["s11.b"], [("+", "g", 80, CERTO), ("convergente", "g", 64)], XE, 400, passo=0.12)
    E.frase(c, t, C["s11.c"], [("−", "g", 80, ERRADO), ("divergente", "g", 64)], XE, 520, passo=0.12)
    E.frase(c, t, C["s11.d"], ps("foco mais curto,", "i", 60) + [("lente mais forte", "g", 60, COR)], XE, 720, passo=0.12)
    if t >= C["s11.d"]:
        for k, (cx, f, rot) in enumerate(((1080, 280, "fraca"), (1620, 130, "forte"))):
            tk = C["s11.d"] + 0.3 + 0.5 * k
            if t < tk:
                continue
            F.lente(c, t, tk, cx, 880, 240, True, None, eixo=(cx - 200, cx + f + 60))
            eixo_pontos(c, t, tk + 0.3, 880, [(cx + f, "F'")])
            for j, dy in enumerate((-80, 80)):
                F.raio(c, t, tk + 0.2, [(cx - 180, 880 + dy), (cx, 880 + dy), (cx + f, 880)], d=0.8, largura=4, setas=False)
            E.foco(c, t, tk + 0.6, 0.4, lambda a, cx=cx, rot=rot: centro(c, rot, cx, 1050, 48, "g", COR, a))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s12"], [("cuidado", "g", 96, ERRADO)], XE, 200)
    E.frase(c, t, C["s12.a"], ps("o foco em", "i", 70) + [("centímetros", "g", 70, ERRADO)], XE, 330, passo=0.12)
    E.formula_em(c, t, C["s12.b"], "V = f{1}{50} = 0,02", XE, 560, 110, "g", ERRADO)
    E.foco(c, t, C["s12.c"], 0.5, lambda a: receita(c, 1450, 520, a, "+0,02?"))
    E.foco(c, t, C["s12.c"] + 0.8, 0.4, lambda a: E.selo(c, 1690, 380, 56, False, a))
    pilula_esq(c, t, C["s12.d"], "grau: sempre com f em metros", XE, 880, 52, E.COR)


# ---------------- atalho (palco) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    if t < C["s14"]:
        E.frase(c, t, C["s13"], ps("o atalho de prova", "i", 72, CLARO), W / 2, 170, "center")
        E.foco(c, t, C["s13.a"], 0.5, lambda a: centro(c, "f (cm) = 100 ÷ grau", W / 2, 360, 110, "g", BR, a))
        E.foco(c, t, C["s13.b"], 0.4, lambda a: centro(c, "+4 graus:  100 ÷ 4 = 25 cm", W / 2, 600, 72, "g", CLARO, a))
        E.foco(c, t, C["s13.c"], 0.4, lambda a: centro(c, "−2,5 graus:  100 ÷ 2,5 = 40 cm", W / 2, 760, 72, "g", CLARO, a))
        E.foco(c, t, C["s13.c"] + 1.2, 0.4, lambda a: E.pilula(c, "divergente", W / 2, 880, 50, "g", fundo=E.COR, a=a))
        return
    E.frase(c, t, C["s14.a"], ps("1 metro =", "i", 70, CLARO) + [("100 cm", "g", 70, BR)], W / 2, 260, "center", 0.12)
    E.frase(c, t, C["s14.b"], ps("a conversão já vem", "i", 62, CLARO) + [("dentro da conta", "g", 62, BR)], W / 2, 400, "center", 0.12)
    E.frase(c, t, C["s14.c"], ps("e o atalho dos espelhos", "i", 62, CLARO) + [("também vale", "g", 62, BR)], W / 2, 600, "center", 0.12)
    E.formula_em(c, t, C["s14.d"], "p' = f{f · p}{p − f}", W / 2, 820, 120, "g", BR, "center")


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s15"], ps("hora de testar", "i", 72, COR), XE, 190)
    E.foco(c, t, C["s15.a"], 0.4, lambda a: (E.escreve(c, "lente de", XE, 340, 64, "i", TINTA, a), E.escreve(c, "+4 graus", XE + 290, 340, 76, "g", COR, a)))
    E.frase(c, t, C["s15.b"], ps("distância", "i", 66) + [("focal?", "g", 66, COR)], XE, 500, passo=0.12)
    E.frase(c, t, C["s15.c"], [("convergente", "g", 60), ("ou", "i", 66), ("divergente?", "g", 60, COR)], XE, 620, passo=0.12)
    E.frase(c, t, C["s15.d"], ps("objeto a", "i", 62) + [("50 cm:", "g", 62, COR)] + ps("onde fica a imagem?", "i", 62), XE, 780, passo=0.1)
    if t < C["s16"]:
        E.foco(c, t, C["s15.a"], 0.5, lambda a: receita(c, 1450, 420, a, "+4,00"))
    questao_relogio(c, t, C, "s16")


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    x = XE
    if t < C["s18"]:
        E.foco(c, t, C["s17.a"], 0.4, lambda a: E.formula(c, "100 ÷ 4 = 25 cm", x, 260, 84, "g", TINTA, a))
        pilula_esq(c, t, C["s17.b"], "positivo: convergente", x, 370, 46, E.COR)
        E.formula_em(c, t, C["s17.c"], "p' = f{25 · 50}{50 − 25}", x, 580, 96, "g", TINTA)
        E.formula_em(c, t, C["s17.d"], "= f{1.250}{25}", x + 700, 580, 96, "g", TINTA)
        bola_txt(c, t, C["s17.e"], "50 cm", 1560, 550, 120, 64)
        return
    cx, cy = 960, 560
    diagrama(c, t, cx, cy, 300, cx - 600, 140, C["s18"] - 0.6, C["s18"] - 0.5, (C["s18"] - 0.4, C["s18"] - 0.2), C["s18.a"], x0=220, x1=1820, h=420)
    eixo_pontos(c, t, C["s18.c"], cy, [(cx - 600, "2F"), (cx + 600, "2F'")])
    pilula_esq(c, t, C["s18.a"], "real, do outro lado", XE, 230, 46, F.VEL)
    E.formula_em(c, t, C["s18.b"], "A = −f{50}{50} = −1", XE, 920, 90, "g", TINTA)
    classifica(c, t, [(C["s18.c"], "invertida"), (C["s18.c"] + 0.3, "mesmo tamanho")], 1000, 900, 50)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def r():
        resumo(c, t, C, "s19", [("s19.a", [("lentes:", "g"), ("a equação dos espelhos,", "i"), ("f > 0 converge, f < 0 diverge", "g", 56, COR)]),
                                ("s19.b", [("grau:", "g"), ("V = 1 ÷ f,", "g", 62, COR), ("f em metros", "i")])], y0=420, dy=220, size=56)
    E.saida(c, t, C["s20"] - 0.1, r)
    if t < C["s20"]:
        return

    def desenho():
        E.foco(c, t, C["s20.a"] + 0.3, 0.5, lambda a: olho(c, 620, 800, 110, a, 1))
    proxima(c, t, C, "s20", [("o olho", "g", 100, COR), ("humano", "i", 100)], [("miopia", "g", 72), ("e", "i", 72), ("hipermetropia", "g", 72)],
            desenho, k_insc="d", k_bons="e")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, equacao=b_equacao, exemplo=b_exemplo, grau=b_grau, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
