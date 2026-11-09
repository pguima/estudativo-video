"""Visual — Estudativo · FIS-OPT-011: equação dos espelhos (Gauss) e aumento.
Segue a linguagem visual da trilha Óptica, escrita no cabeçalho do visual.py da FIS-OPT-001. As contas aparecem como uma
coluna de passos (E.formula), um passo por fala; a resposta vai na esfera. Os diagramas usam raios_espelho, que aplica a
mesma equação: a imagem desenhada cai onde a conta manda (escala: 12 px por centímetro).
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
ARQUIVO_FINAL = "estudativo_FIS-OPT-011_equacao_dos_espelhos_aumento.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("equacao", "exemplo", "aumento", "convexo", "atalho", "questao", "fim"))


def _pl(f, p):
    return 1 / (Fr(1) / f - Fr(1) / p)


# todas as contas da aula
assert Fr(1, 20) - Fr(1, 30) == Fr(3, 60) - Fr(2, 60) == Fr(1, 60) and _pl(20, 30) == 60       # gancho: p' = 60 cm
assert -Fr(60, 30) == -2                                                                         # A = −2
assert -Fr(1, 20) - Fr(1, 30) == -Fr(3, 60) - Fr(2, 60) == -Fr(5, 60) == -Fr(1, 12) and _pl(-20, 30) == -12   # convexo
assert Fr(12, 30) == Fr(2, 5)                                                                    # A = +2/5
assert _pl(20, 30) == Fr(20 * 30, 30 - 20) and 20 * 30 == 600 and 600 / 10 == 60                 # atalho
assert _pl(-20, 30) == Fr(-20 * 30, 30 + 20) and -600 / 50 == -12                                # atalho no convexo
assert _pl(30, 15) == -30 and 30 * 15 == 450 and 15 - 30 == -15 and 450 / -15 == -30             # questão
assert -Fr(-30, 15) == 2


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
K = 12  # px por cm


def eixo(c, t, t0, x0, x1, cy, escuro=False):
    if t >= t0:
        M.line(c, x0, cy, x1, cy, BR if escuro else TINTA, 0.5, 3, dash=E.TRACO, progress=ease_io(prog(t, t0, 0.6)))


def diagrama(c, t, vx, cy, f, xo, ho, concavo, t_esp, t_obj, ts, t_img, tipos=("par", "foco"), x0=None, x1=None, pontos=True):
    R = 2 * f
    eixo(c, t, t_esp, x0 if x0 is not None else vx - 1.6 * R, x1 if x1 is not None else vx + 300, cy)
    espelho_curvo(c, t, t_esp, vx, cy, R, min(300, R * 0.75), concavo)
    if pontos:
        Fx, Cx = (vx - f, vx - R) if concavo else (vx + f, vx + R)
        eixo_pontos(c, t, t_esp + 0.3, cy, [(Fx, "F"), (Cx, "C"), (vx, "V")])
    objeto_o(c, t, t_obj, xo, cy, ho)
    xi, hi = raios_espelho(c, t, ts, vx, cy, f, xo, ho, concavo, tipos)
    imagem_i(c, t, t_img, xi, cy, hi, real=concavo and xi < vx)
    return xi, hi


def passos(c, t, linhas, x, y0, dy, size=80, escuro=False):
    """coluna de contas: linhas = [(instante, fórmula, cor)]"""
    for i, (ti, s, cor) in enumerate(linhas):
        E.formula_em(c, t, ti, s, x, y0 + i * dy, size, "g", cor or (BR if escuro else TINTA))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def um():
        cy, vx = 520, 1720
        diagrama(c, t, vx, cy, 20 * K, vx - 30 * K, 110, True, C["s01"], C["s01.b"], (C["s01.c"] - 0.8, C["s01.c"] - 0.4), C["s01.c"], x0=860, x1=1820)
        E.foco(c, t, C["s01.a"], 0.4, lambda a: (E.formula(c, "f =", XE, 230, 70, "g", COR, a), F.medida(c, 20, "cm", XE + 140, 230, 70, TINTA, a)))
        E.foco(c, t, C["s01.b"], 0.4, lambda a: (E.formula(c, "p =", XE, 340, 70, "g", COR, a), F.medida(c, 30, "cm", XE + 140, 340, 70, TINTA, a)))
        classifica(c, t, [(C["s01.c"], "real"), (C["s01.c"] + 0.3, "invertida"), (C["s01.c"] + 0.6, "maior")], XE, 960, 50)
        E.foco(c, t, C["s01.d"], 0.4, lambda a: (E.formula(c, "p' =", XE, 520, 76, "g", COR, a), F.medida(c, 60, "cm", XE + 170, 520, 76, TINTA, a)))
        E.foco(c, t, C["s01.e"], 0.4, lambda a: E.escreve(c, "2 vezes maior", XE, 640, 66, "g", COR, a))
        E.segmento(c, t, C["s01.d"], (vx - 60 * K, cy + 280), (vx, cy + 280), "60 cm", cor=E.COR, largura=4, lado=-1, size=48)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t >= C["s02"]:
        promessa(c, t, C, "s02", [("s02.b", "onde fica a imagem"), ("s02.c", "o aumento"), ("s02.d", "o sinal do convexo")])


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    def esp(a, x, y):
        c.drawArc(skia.Rect.MakeXYWH(x - 120, y - 100, 200, 200), -40, 80, False, M.paint(TINTA, a, stroke=6))
        M.line(c, x - 150, y, x + 90, y, TINTA2, a, 3, dash=E.TRACO)
        M.line(c, x - 120, y - 50, x + 70, y - 50, E.COR, a, 5)

    def frac(a, x, y):
        E.formula(c, "f{1}{2} + f{1}{3} = f{5}{6}", x - 120, y + 20, 56, "g", TINTA, a, "center")
    lembrete(c, t, C, "s03", [("s03.b", "raios notáveis:", "o tipo de imagem"), ("s03.c", "somar frações:", "pelo MMC")], (esp, frac))


# ---------------- a equação ----------------
def b_equacao(c, t, C, b):
    cy, vx = 560, 1700
    if t < C["s05"]:
        diagrama(c, t, vx, cy, 20 * K, vx - 30 * K, 110, True, C["s04"], C["s04"] + 0.2, (C["s04"] + 0.3, C["s04"] + 0.6), C["s04"] + 1.0, x0=820, x1=1820)
        for i, (k, x_, s, cor) in enumerate((("s04.a", vx - 20 * K, "f", E.COR), ("s04.b", vx - 30 * K, "p", TINTA), ("s04.c", vx - 60 * K, "p'", F.VEL))):
            E.segmento(c, t, C[k], (x_, cy + 250 + 70 * i), (vx, cy + 250 + 70 * i), s, cor=cor, largura=5, lado=-1, size=52)
        E.frase(c, t, C["s04"], ps("três distâncias", "i", 70), XE, 220, passo=0.12)
        E.frase(c, t, C["s04"] + 0.6, ps("a partir do", "i", 60, TINTA2) + [("espelho", "g", 60)], XE, 320, passo=0.1)
        for i, (k, l, s) in enumerate((("s04.a", "f", "distância focal"), ("s04.b", "p", "do objeto"), ("s04.c", "p'", "da imagem"))):
            E.foco(c, t, C[k], 0.4, lambda a, l=l, s=s, i=i: (E.formula(c, l, XE, 470 + 90 * i, 64, "g", COR, a), E.escreve(c, s, XE + 90, 470 + 90 * i, 54, "i", TINTA, a)))
        pilula_esq(c, t, C["s04.d"], "mesma unidade nas três", XE, 790, 44, E.COR)
        return
    if t < C["s06"]:
        E.frase(c, t, C["s05"], ps("equação dos espelhos", "i", 76) + [("(Gauss)", "g", 60, TINTA2)], W / 2, 250, "center", 0.12)
        s, y = 170, 640
        partes = ["f{1}{f}", " = f{1}{p}", " + f{1}{p'}"]
        ws = [E.formula(None, p_, 0, 0, s, "g", a=0) for p_ in partes]
        x = W / 2 - sum(ws) / 2
        for p_, w_, k in zip(partes, ws, ("s05.a", "s05.b", "s05.c")):
            E.formula_em(c, t, C[k], p_, x, y, s, "g", COR if k == "s05.a" else TINTA)
            x += w_
        return
    E.formula_em(c, t, C["s06"] - 0.3, "f{1}{f} = f{1}{p} + f{1}{p'}", XE, 270, 100, "g", TINTA2)
    linhas = (("s06.a", "p > 0", "objeto na frente", TINTA), ("s06.b", "côncavo: f > 0", "", CERTO), ("s06.c", "convexo: f < 0", "", ERRADO),
              ("s06.d", "p' > 0", "real, na frente", E.COR), ("s06.e", "p' < 0", "virtual, atrás", F.VEL))
    for i, (k, l, s, cor) in enumerate(linhas):
        y = 470 + 110 * i
        E.foco(c, t, C[k], 0.4, lambda a, l=l, s=s, y=y, cor=cor: (E.formula(c, l, XE, y, 66, "g", cor if cor not in (CERTO, ERRADO) else TINTA, a),
                                                                    E.escreve(c, s, XE + 520, y, 58, "i", TINTA2, a)))
    # espelho de lado: frente (real) e atrás (virtual)
    q = ep(t, C["s06.d"] - 0.5, 0.5)
    if q > 0:
        espelho_curvo(c, t, C["s06.d"] - 0.5, 1560, 640, 520, 300, True)
        E.foco(c, t, C["s06.d"], 0.4, lambda a: centro(c, "frente: real", 1280, 980, 48, "g", COR, a))
        E.foco(c, t, C["s06.e"], 0.4, lambda a: centro(c, "atrás: virtual", 1720, 980, 48, "g", F.VEL, a))


# ---------------- exemplo ----------------
def b_exemplo(c, t, C, b):
    x = XE
    E.foco(c, t, C["s07.a"], 0.4, lambda a: E.formula(c, "f = 20   p = 30", x, 230, 72, "g", COR, a))
    passos(c, t, [(lerp(C["s07.a"], C["s07.b"], 0.55), "f{1}{p'} = f{1}{f} − f{1}{p}", TINTA2),
                  (C["s07.b"], "f{1}{p'} = f{1}{20} − f{1}{30}", None),
                  (C["s07.d"], "f{1}{p'} = f{3}{60} − f{2}{60}", None),
                  (C["s07.e"], "f{1}{p'} = f{1}{60}", COR)], x, 420, 190, 86)
    pilula_em(c, t, C["s07.c"], "MMC (20, 30) = 60", 1280, 600, 50, E.COR)
    bola_txt(c, t, C["s07.f"], "60 cm", 1500, 830, 140, 76)
    E.foco(c, t, C["s07.f"] + 0.5, 0.4, lambda a: (E.formula(c, "p' =", 1110, 856, 80, "g", TINTA, a)))
    pilula_em(c, t, C["s07.f"] + 1.0, "positivo: real", 1500, 1020, 44, F.VEL)


# ---------------- aumento ----------------
def b_aumento(c, t, C, b):
    if t < C["s09"]:
        E.frase(c, t, C["s08"], [("o", "i", 80), ("aumento", "g", 80, COR)], XE, 230)
        E.foco(c, t, C["s08.a"], 0.4, lambda a: E.formula(c, "A", XE, 520, 180, "g", COR, a))
        E.formula_em(c, t, C["s08.b"], "= f{i}{o}", XE + 150, 520, 150, "g", TINTA)
        E.formula_em(c, t, C["s08.c"], "= −f{p'}{p}", XE + 450, 520, 150, "g", TINTA)
        objeto_o(c, t, C["s08.b"], 1350, 800, 220)
        E.foco(c, t, C["s08.b"] + 0.3, 0.4, lambda a: E.escreve(c, "o", 1380, 720, 64, "g", TINTA, a))
        imagem_i(c, t, C["s08.b"] + 0.3, 1620, 800, 440, True)
        E.foco(c, t, C["s08.b"] + 0.6, 0.4, lambda a: E.escreve(c, "i", 1650, 620, 64, "g", F.VEL, a))
        M.line(c, 1200, 800, 1800, 800, TINTA2, ep(t, C["s08.b"], 0.4), 3) if t >= C["s08.b"] else None
        return
    E.formula_em(c, t, C["s09.a"], "A = −f{60}{30}", XE, 330, 130, "g", TINTA)
    E.formula_em(c, t, C["s09.b"], "= −2", XE + 690, 330, 130, "g", COR)
    E.foco(c, t, C["s09.c"], 0.4, lambda a: (E.escreve(c, "−", XE + 820, 470, 90, "g", COR, a), E.escreve(c, "→", XE + 900, 470, 70, "g", TINTA2, a)))
    pilula_em(c, t, C["s09.c"] + 0.3, "invertida", XE + 1160, 445, 50, F.VEL)
    E.foco(c, t, C["s09.d"], 0.4, lambda a: (E.escreve(c, "2", XE + 820, 590, 90, "g", COR, a), E.escreve(c, "→", XE + 900, 590, 70, "g", TINTA2, a)))
    pilula_em(c, t, C["s09.d"] + 0.3, "2 vezes maior", XE + 1190, 565, 50, F.VEL)
    E.frase(c, t, C["s09.e"], [("A > 0", "g", 64), ("→", "g", 64, TINTA2), ("direita", "i", 70)], XE, 790, passo=0.15)
    E.frase(c, t, C["s09.f"], [("A entre 0 e 1, sem o sinal", "g", 56), ("→", "g", 56, TINTA2), ("menor", "i", 64)], XE, 920, passo=0.15)


# ---------------- convexo ----------------
def b_convexo(c, t, C, b):
    x = XE
    vx, cy = 1520, 360
    if t < C["s11"]:
        E.frase(c, t, C["s10.a"], ps("retrovisor, foco de", "i", 64) + [("20 cm", "g", 64)], x, 220, passo=0.1)
        E.foco(c, t, C["s10.b"], 0.4, lambda a: E.formula(c, "f = −20", x, 360, 90, "g", ERRADO, a))
        E.foco(c, t, C["s10.c"], 0.4, lambda a: E.formula(c, "p = 30", x + 440, 360, 90, "g", TINTA, a))
        passos(c, t, [(C["s10.d"], "f{1}{p'} = −f{1}{20} − f{1}{30}", None),
                      (C["s10.e"], "= −f{3}{60} − f{2}{60}", None),
                      (C["s10.f"], "= −f{5}{60} = −f{1}{12}", COR)], x, 560, 180, 84)
        return
    diagrama(c, t, vx, cy + 280, 20 * K, vx - 30 * K, 200, False, C["s11"] - 0.6, C["s11"] - 0.5, (C["s11"] - 0.4, C["s11"] - 0.2), C["s11.a"] + 0.3,
             ("par", "centro"), x0=1050, x1=1840)
    E.foco(c, t, C["s11.a"], 0.4, lambda a: E.formula(c, "p' = −12 cm", x, 260, 96, "g", TINTA, a))
    pilula_esq(c, t, C["s11.b"], "virtual, atrás do espelho", x, 370, 44, F.VEL)
    E.formula_em(c, t, C["s11.c"], "A = −f{(−12)}{30}", x, 580, 96, "g", TINTA)
    E.formula_em(c, t, C["s11.d"], "= +f{2}{5}", x + 560, 580, 96, "g", COR)
    classifica(c, t, [(C["s11.e"], "direita"), (C["s11.e"] + 0.3, "menor")], x, 800, 54)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s12"], [("cuidado", "g", 96, ERRADO)], XE, 200)
    E.frase(c, t, C["s12.a"], ps("esquecer o", "i", 72) + [("sinal do convexo", "g", 72, ERRADO)], XE, 330, passo=0.12)
    E.foco(c, t, C["s12.b"], 0.4, lambda a: E.formula(c, "f = +20", XE, 520, 100, "g", ERRADO, a))
    E.foco(c, t, C["s12.c"], 0.4, lambda a: E.formula(c, "→  p' = +60 :  real?", XE + 420, 520, 84, "g", TINTA, a))
    E.foco(c, t, C["s12.d"], 0.5, lambda a: E.selo(c, 1700, 490, 70, False, a))
    E.frase(c, t, C["s12.d"], [("convexo", "g", 70), ("nunca", "i", 76), ("dá imagem real", "g", 70, ERRADO)], XE, 720, passo=0.12)
    pilula_esq(c, t, C["s12.e"], "antes do número, escreva o sinal", XE, 900, 50, E.COR)


# ---------------- atalho (palco) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    if t < C["s14"]:
        E.frase(c, t, C["s13"], ps("o atalho de prova", "i", 76, CLARO), W / 2, 180, "center")
        if t < C["s13.b"]:
            E.formula_em(c, t, C["s13.a"], "p' = f · p", 560, 440, 130, "g", BR)
        E.foco(c, t, C["s13.b"], 0.4, lambda a: E.formula(c, "p' = f{f · p}{p − f}", 560, 440, 130, "g", BR, a))
        E.formula_em(c, t, C["s13.c"], "f{20 · 30}{30 − 20}", 560, 760, 100, "g", CLARO)
        E.formula_em(c, t, C["s13.d"], "= f{600}{10}", 1000, 760, 100, "g", CLARO)
        bola_txt(c, t, C["s13.e"], "60 cm", 1560, 720, 130, 70)
        E.foco(c, t, lerp(C["s13.e"], C["s13.end"], 0.5), 0.4, lambda a: centro(c, "sem MMC", 1560, 920, 56, "g", BR, a))
        return
    E.frase(c, t, C["s14.a"], ps("é a mesma equação,", "i", 60, CLARO) + [("subtraída e virada", "g", 60, BR)], W / 2, 170, "center", 0.12)
    E.formula_em(c, t, C["s14.a"] + 0.8, "f{1}{p'} = f{p − f}{f · p}   →   p' = f{f · p}{p − f}", W / 2, 360, 84, "g", BR, "center")
    E.frase(c, t, C["s14.b"], [("convexo:", "g", 60, BR)] + ps("cuidado com o sinal", "i", 62, CLARO), XE, 560, passo=0.12)
    E.formula_em(c, t, C["s14.c"], "f{(−20) · 30}{30 − (−20)}", XE, 760, 90, "g", BR)
    E.formula_em(c, t, C["s14.d"], "= f{−600}{50}", XE + 640, 760, 90, "g", CLARO)
    bola_txt(c, t, C["s14.e"], "−12 cm", XE + 1200, 730, 120, 62)
    E.foco(c, t, C["s14.f"], 0.5, lambda a: centro(c, "deu o raio de curvatura? f = R ÷ 2", W / 2, 990, 56, "g", BR, a))


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s15"], ps("hora de testar", "i", 72, COR), XE, 190)
    E.frase(c, t, C["s15"] + 0.6, ps("espelho de maquiagem:", "i", 64) + [("côncavo", "g", 64)], XE, 320, passo=0.1)
    E.foco(c, t, C["s15.a"], 0.4, lambda a: (E.escreve(c, "foco:", XE, 450, 62, "i", TINTA, a), F.medida(c, 30, "cm", XE + 190, 450, 72, COR, a)))
    E.foco(c, t, C["s15.b"], 0.4, lambda a: (E.escreve(c, "rosto a", XE, 570, 62, "i", TINTA, a), F.medida(c, 15, "cm", XE + 240, 570, 72, COR, a)))
    E.frase(c, t, C["s15.c"], [("onde", "g", 72, COR)] + ps("está a imagem?", "i", 72), XE, 740, passo=0.12)
    E.frase(c, t, C["s15.d"], ps("qual o", "i", 72) + [("aumento?", "g", 72, COR)], XE, 860, passo=0.12)
    if t < C["s16"]:
        cy, vx = 600, 1700
        eixo(c, t, C["s15.a"], 1100, 1820, cy)
        espelho_curvo(c, t, C["s15.a"], vx, cy, 2 * 30 * 8, 300, True)
        eixo_pontos(c, t, C["s15.a"] + 0.3, cy, [(vx - 30 * 8, "F")])
        objeto_o(c, t, C["s15.b"], vx - 15 * 8, cy, 110)
    questao_relogio(c, t, C, "s16")


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    x = XE
    if t < C["s18"]:
        E.formula_em(c, t, C["s17.a"], "p' = f{30 · 15}{15 − 30}", x, 330, 110, "g", TINTA)
        E.formula_em(c, t, C["s17.b"], "= f{450}{−15}", x + 720, 330, 110, "g", TINTA)
        bola_txt(c, t, C["s17.c"], "−30 cm", 1560, 300, 130, 66)
        pilula_esq(c, t, C["s17.d"], "virtual, atrás do espelho", x, 560, 52, F.VEL)
        return
    cy, vx = 640, 1540
    diagrama(c, t, vx, cy, 30 * 8, vx - 15 * 8, 110, True, C["s18"] - 0.6, C["s18"] - 0.5, (C["s18"] - 0.4, C["s18"] - 0.2), C["s18.a"],
             ("par", "foco"), x0=1000, x1=1840)
    E.formula_em(c, t, C["s18.a"], "A = −f{(−30)}{15}", x, 330, 100, "g", TINTA)
    E.formula_em(c, t, C["s18.b"], "= +2", x + 600, 330, 100, "g", COR)
    classifica(c, t, [(C["s18.c"], "direita"), (C["s18.c"] + 0.3, "2 vezes maior")], x, 520, 52)
    E.frase(c, t, C["s18.d"], ps("rosto entre o", "i", 60) + [("F", "g", 60, COR)] + ps("e o espelho", "i", 60), x, 720, passo=0.1)


# ---------------- fechamento ----------------
def copo(c, cx, yb, a=1.0):
    """copo com água e um lápis que parece quebrado na superfície"""
    if a <= 0:
        return
    w, h, ya = 240, 330, yb - 200
    c.drawRect(skia.Rect.MakeLTRB(cx - w / 2, ya, cx + w / 2, yb), M.paint(VIDRO, 0.45 * a))
    M.line(c, cx - w / 2, yb - h, cx - w / 2, yb, TINTA, a, 5); M.line(c, cx + w / 2, yb - h, cx + w / 2, yb, TINTA, a, 5)
    M.line(c, cx - w / 2, yb, cx + w / 2, yb, TINTA, a, 5)
    M.line(c, cx + 150, yb - h - 90, cx + 20, ya, "#E8B23A", a, 16)
    M.line(c, cx + 50, ya, cx - 60, yb - 30, "#E8B23A", a, 16)


def b_fim(c, t, C, b):
    def r():
        resumo(c, t, C, "s19", [("s19.a", [("1/f = 1/p + 1/p'", "g", 66, COR)]),
                                ("s19.b", [("côncavo:", "g"), ("f > 0;", "i"), ("convexo:", "g"), ("f < 0", "i")]),
                                ("s19.c", [("A = −p' ÷ p:", "g", 62, COR), ("sinal de menos = invertida", "i")])], y0=380, dy=200)
    E.saida(c, t, C["s20"] - 0.1, r)
    if t < C["s20"]:
        return
    E.foco(c, t, C["s20.c"], 0.5, lambda a: copo(c, 600, 980, a))
    proxima(c, t, C, "s20", [("a luz", "i", 100), ("muda de meio", "g", 100, COR)], [("índice de refração", "g", 70), ("e Snell", "i", 70)],
            None, k_insc="d", k_bons="e")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, equacao=b_equacao, exemplo=b_exemplo, aumento=b_aumento, convexo=b_convexo,
              erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
