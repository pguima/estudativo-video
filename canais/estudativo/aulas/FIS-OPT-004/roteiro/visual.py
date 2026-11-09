"""Visual — Estudativo · FIS-OPT-004: índice de refração e lei de Snell.
Segue a linguagem visual da trilha Óptica, escrita no cabeçalho do visual.py da FIS-OPT-001: raio laranja, normal tracejada,
ângulos medidos da normal em arco laranja; meio mais refringente pintado em azul-vidro (VIDRO), mais forte quanto maior o n.
Os ângulos desenhados são os da conta (60° → 30°, 45° → 30°).
Todo instante vem de C[...] (marcadores do roteiro)."""
import math

import editorial as E
import fisica as F
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Física", "Óptica")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_FIS-OPT-004_indice_de_refracao_lei_de_snell.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("refracao", "indice", "snell", "erro", "atalho", "questao", "fim"))

sen = lambda g: math.sin(math.radians(g))
# todas as contas da aula
assert 300000 / 200000 == 1.5                                              # vidro: n = 1,5
assert abs(1 * sen(60) / math.sqrt(3) - 0.5) < 1e-12 and abs(math.degrees(math.asin(0.5)) - 30) < 1e-9   # 60° → 30°
assert abs(sen(60) - math.sqrt(3) / 2) < 1e-12
assert 200000 / 300000 < 1 and abs(200000 / 300000 - 2 / 3) < 1e-12        # o erro: v/c = 2/3
assert 300000 / 2 == 150000                                                # índice 2: metade da velocidade
assert abs(1 * sen(45) / math.sqrt(2) - 0.5) < 1e-12 and abs(sen(45) - math.sqrt(2) / 2) < 1e-12   # questão: 45° → 30°
assert abs(math.degrees(math.asin(sen(50) / 1.33)) - 35.2) < 0.1           # desenho da água (n ≈ 1,33)


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
def meios(c, t, t0, x0, x1, cy, y0, y1, n1, n2, alfa=0.35, escuro=False, rot=True):
    """dois meios separados pela linha cy: o de cima até y0, o de baixo até y1; rótulos n1/n2 à direita"""
    q = ep(t, t0, 0.5)
    if q <= 0:
        return
    c.drawRect(skia.Rect.MakeLTRB(x0, cy, x1, y1), M.paint(VIDRO, alfa * q))
    M.line(c, x0, cy, x1, cy, BR if escuro else TINTA, q, 5)
    if rot:
        tinta = BR if escuro else TINTA
        E.formula(c, n1, x1 - 20, cy - 40, 50, "b", tinta, q, "right")
        E.formula(c, n2, x1 - 20, cy + 80, 50, "b", tinta, q, "right")


def snell(c, t, ti, tr, P, i_deg, r_deg, L=420, rot_i="i", rot_r="r", ta=None, escuro=False, size=56):
    """raio que chega a i_deg da normal (vindo de cima, da esquerda) e sai a r_deg; ângulos marcados (ta = instantes)"""
    gi, gr = math.radians(i_deg), math.radians(r_deg)
    A = (P[0] - L * math.sin(gi), P[1] - L * math.cos(gi))
    B = (P[0] + L * math.sin(gr), P[1] + L * math.cos(gr))
    F.normal(c, t, min(ti, tr) - 0.3, P, 90, L * 0.95, escuro=escuro)
    F.raio(c, t, ti, [A, P], d=0.7)
    F.raio(c, t, tr, [P, B], d=0.7)
    ta = ta or (ti + 0.7, tr + 0.7)
    if rot_i:
        E.angulo(c, t, ta[0], P, A, (P[0], P[1] - 300), rot_i, r=110, size=size)
    if rot_r:
        E.angulo(c, t, ta[1], P, (P[0], P[1] + 300), B, rot_r, r=110, size=size)
    return A, B


# ---------------- gancho ----------------
def copo_grande(c, cx, yb, a=1.0, quebrado=True):
    if a <= 0:
        return
    w, h, ya = 440, 560, yb - 320
    c.drawRect(skia.Rect.MakeLTRB(cx - w / 2, ya, cx + w / 2, yb), M.paint(VIDRO, 0.45 * a))
    M.line(c, cx - w / 2, yb - h, cx - w / 2, yb, TINTA, a, 6); M.line(c, cx + w / 2, yb - h, cx + w / 2, yb, TINTA, a, 6)
    M.line(c, cx - w / 2, yb, cx + w / 2, yb, TINTA, a, 6)
    M.line(c, cx - w / 2, ya, cx + w / 2, ya, TINTA2, a * 0.6, 3)
    M.line(c, cx - 200, ya - 350, cx - 20, ya, "#E8B23A", a, 22)
    M.line(c, cx - 20, ya, cx + 76, ya + 150, "#E8B23A", a, 22)  # a parte de dentro, como o olho vê (mais rasa)


def b_gancho(c, t, C, b):
    def um():
        E.foco(c, t, C["s01.a"], 0.6, lambda a: copo_grande(c, 1350, 940, a))
        E.frase(c, t, C["s01.a"], ps("o lápis parece", "i", 80) + [("quebrado", "g", 80, COR)], XE, 260, passo=0.12)
        E.frase(c, t, C["s01.b"], ps("ele", "i", 80) + [("não quebrou", "g", 80)], XE, 400, passo=0.12)
        if t >= C["s01.b"] + 0.4:  # o lápis de verdade continua reto (tracejado)
            M.line(c, 1330, 620, 1431, 817, TINTA2, ep(t, C["s01.b"] + 0.4, 0.5), 6, dash=[14, 10])
        E.frase(c, t, C["s01.c"], ps("quem mudou de caminho foi", "i", 60) + [("a luz", "g", 60, COR)], XE, 560, passo=0.1)
        F.raio(c, t, C["s01.b"] + 1.0, [(1431, 817), (1500, 620), (1667, 279)], d=1.0, largura=6)
        prolonga(c, t, C["s01.b"] + 2.0, (1500, 620), (1426, 770))
        E.foco(c, t, C["s01.b"] + 1.6, 0.4, lambda a: olho(c, 1720, 240, 40, a, -1))
    E.saida(c, t, C["s02"] - 0.1, um)
    if t >= C["s02"]:
        promessa(c, t, C, "s02", [("s02.b", "índice de refração"), ("s02.c", "lei de Snell"), ("s02.d", "para onde entorta")])


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    def nor(a, x, y):
        M.line(c, x - 150, y + 40, x + 120, y + 40, TINTA, a, 5)
        M.line(c, x - 15, y + 40, x - 15, y - 90, TINTA2, a, 4, dash=E.TRACO)
        M.rrect(c, x - 15, y + 8, 32, 32, 0, E.COR, 0.4 * a)

    def senos(a, x, y):
        E.formula(c, "f{1}{2}  f{r{2}}{2}  f{r{3}}{2}", x - 60, y + 30, 48, "g", TINTA, a, "center")
    lembrete(c, t, C, "s03", [("s03.b", "a normal:", "a 90° da superfície"), ("s03.c", "seno de 30°, 45° e 60°:", "os ângulos notáveis")], (nor, senos))


# ---------------- refração ----------------
def b_refracao(c, t, C, b):
    P, cy = (1300, 600), 600
    if t < C["s05"]:
        meios(c, t, C["s04.a"], 800, 1820, cy, 200, 1000, "ar", "água")
        E.frase(c, t, C["s04.a"], [("do ar", "g", 64), ("para a", "i", 64), ("água", "g", 64, COR)], XE, 240, passo=0.12)
        E.frase(c, t, C["s04.b"], ps("a velocidade", "i", 64) + [("muda", "g", 64, COR)], XE, 360, passo=0.12)
        E.frase(c, t, C["s04.c"], [("refração", "g", 110, COR)], XE, 530)
        snell(c, t, C["s04.d"], C["s04.d"] + 0.7, P, 50, 35.2, rot_i=None, rot_r=None)
        E.frase(c, t, C["s04.d"] + 0.4, ps("chegou inclinada:", "i", 52, TINTA2) + [("muda de direção", "g", 52)], XE, 700, passo=0.1)
        F.raio(c, t, C["s04.e"], [(1650, 230), (1650, 970)], d=1.0, largura=6)
        E.frase(c, t, C["s04.e"] + 0.2, ps("pela normal:", "i", 52, TINTA2) + [("segue reto", "g", 52)], XE, 810, passo=0.1)
        return
    # s05: o carrinho que entra na grama de lado
    cy2 = 640
    q = ep(t, C["s05"], 0.5)
    c.drawRect(skia.Rect.MakeLTRB(980, 200, 1840, cy2), M.paint("#D9D6CC", 0.5 * q))
    c.drawRect(skia.Rect.MakeLTRB(980, cy2, 1840, 960), M.paint("#7DBE6A", 0.55 * q))
    E.foco(c, t, C["s05.a"], 0.4, lambda a: (E.escreve(c, "piso liso", 1010, 260, 46, "i", TINTA, a), E.escreve(c, "grama", 1010, 930, 46, "i", TINTA, a)))
    # eixo com duas rodas: posições fantasmas que viram ao cruzar
    traj = [((1160, 300), 50), ((1300, 440), 50), ((1430, 580), 50), ((1540, 720), 35), ((1620, 860), 30)]
    for k, ((x, y), ang) in enumerate(traj):
        tk = C["s05.a"] + 0.5 + 0.55 * k
        a = ep(t, tk, 0.3) * (0.35 if t > tk + 0.6 and k < len(traj) - 1 else 1.0)
        if a <= 0:
            continue
        g = math.radians(ang)
        dx, dy = 110 * math.cos(g), -110 * math.sin(g)
        M.line(c, x - dx, y - dy, x + dx, y + dy, TINTA, a, 8)
        for s_ in (-1, 1):
            c.drawCircle(x + s_ * dx, y + s_ * dy, 20, M.paint(E.COR, a))
    pilula_em(c, t, C["s05.b"], "a roda que entra primeiro freia", 1410, 1020, 40, TINTA)
    E.frase(c, t, C["s05.c"], ps("e o carrinho", "i", 64) + [("vira", "g", 64, COR)], XE, 300, passo=0.12)
    E.frase(c, t, C["s05.d"], ps("a luz:", "i", 60, TINTA2) + [("entra no meio lento", "g", 54)], XE, 450, passo=0.1)
    E.frase(c, t, C["s05.d"] + 0.8, [("e entorta", "g", 60, COR)], XE, 540)


# ---------------- índice ----------------
def b_indice(c, t, C, b):
    if t < C["s07"]:
        def s06():
            E.foco(c, t, C["s06.a"], 0.4, lambda a: (E.escreve(c, "no vácuo:", XE, 250, 60, "i", TINTA, a),
                                                     F.medida(c, "300.000", "km/s", XE + 320, 250, 80, COR, a)))
            E.foco(c, t, C["s06.b"], 0.4, lambda a: E.escreve(c, "= c", XE + 1050, 250, 80, "g", TINTA, a))
            E.frase(c, t, C["s06.c"], ps("quantas vezes a luz é", "i", 60) + [("mais lenta", "g", 60, COR)], XE, 400, passo=0.1)
            F.formula_legenda(c, t, C["s06.d"], "n = f{c}{v}", [("n", "índice de refração", "sem unidade"), ("c", "velocidade no vácuo", "km/s"),
                                                                ("v", "velocidade no meio", "km/s")], XE + 100, 600, 130, size_l=50)
        E.saida(c, t, C["s07"] - 0.1, s06)
        return
    if t < C["s08"]:
        def s07():
            E.foco(c, t, C["s07.a"], 0.4, lambda a: (E.escreve(c, "vidro:", XE, 250, 60, "i", TINTA, a),
                                                     F.medida(c, "200.000", "km/s", XE + 220, 250, 80, TINTA, a)))
            if t < C["s07.d"]:
                E.formula_em(c, t, C["s07.b"], "n = f{300.000 km/s}{200.000 km/s}", XE, 500, 90, "g", TINTA)
            else:
                E.formula_em(c, t, C["s07.d"], "n = f{300.000}{200.000}", XE, 500, 90, "g", TINTA)
            bola_txt(c, t, C["s07.c"], "1,5", 1500, 470, 130, 90)
            E.frase(c, t, C["s07.d"] + 0.6, ps("km/s corta com km/s:", "i", 56) + [("sem unidade", "g", 56, COR)], XE, 760, passo=0.1)
        E.saida(c, t, C["s08"] - 0.1, s07)
        return
    linhas = (("s08.a", "vácuo", "1"), ("s08.a", "ar", "≈ 1"), ("s08.b", "água", "≈ 1,3"), ("s07", "vidro", "≈ 1,5"))
    E.frase(c, t, C["s08"], [("n", "g", 80, COR)] + ps("de cada meio", "i", 76), XE, 220, passo=0.12)
    for i, (k, s, v) in enumerate(linhas):
        y = 360 + 100 * i
        ti = C[k] + (0.5 if s == "ar" else 0) if k != "s07" else C["s08.b"] + 0.6
        E.foco(c, t, ti, 0.4, lambda a, s=s, v=v, y=y: (E.escreve(c, s, XE, y, 60, "i", TINTA, a), E.escreve(c, v, XE + 280, y, 64, "g", TINTA, a)))
    E.foco(c, t, C["s08.c"], 0.4, lambda a: E.formula(c, "n ≥ 1", 1100, 420, 120, "g", COR, a))
    E.foco(c, t, C["s08.c"] + 0.6, 0.4, lambda a: E.escreve(c, "nada é mais rápido que a luz no vácuo", 1100, 510, 40, "i", TINTA2, a))
    E.frase(c, t, C["s08.d"], [("n maior", "g", 60), ("→", "g", 60, TINTA2), ("luz mais lenta", "i", 64)], XE, 840, passo=0.12)
    pilula_esq(c, t, C["s08.e"], "mais refringente", XE, 950, 50, E.COR)


# ---------------- Snell ----------------
P0, CY = (1400, 600), 600


def cena_snell(c, t, t0, ti, tr, ta=None):
    meios(c, t, t0, 960, 1840, CY, 200, 1000, "ar: n = 1", "vidro: n = r{3}", alfa=0.4)
    return snell(c, t, ti, tr, P0, 60, 30, ta=ta)


def b_snell(c, t, C, b):
    if t < C["s10"]:
        cena_snell(c, t, C["s09"], C["s09.a"], C["s09.b"])
        E.frase(c, t, C["s09.a"], [("i", "g", 70, COR)] + ps("incidência, no meio 1", "i", 60), XE, 300, passo=0.1)
        E.frase(c, t, C["s09.b"], [("r", "g", 70, COR)] + ps("refração, no meio 2", "i", 60), XE, 420, passo=0.1)
        pilula_esq(c, t, C["s09.c"], "medidos da normal", XE, 560, 48, TINTA)
        return
    if t < C["s11"]:
        T0 = C["s10"] - 0.6
        cena_snell(c, t, T0, T0, T0, (T0, T0))
        E.frase(c, t, C["s10"], [("lei", "i", 76), ("de Snell", "g", 76, COR)], XE, 240)
        E.formula_em(c, t, C["s10.a"], "n₁ · sen i", XE, 450, 84, "g", TINTA)
        E.formula_em(c, t, C["s10.b"], "= n₂ · sen r", XE, 570, 84, "g", TINTA)
        E.frase(c, t, C["s10.c"], ps("o produto", "i", 56) + [("índice × seno", "g", 56, COR)] + ps("é o mesmo", "i", 56), XE, 750, passo=0.1)
        return
    T0 = C["s11"] - 0.6
    cena_snell(c, t, T0, T0, T0, (T0, T0))
    if t < C["s13"]:
        E.foco(c, t, C["s11.a"], 0.4, lambda a: E.formula(c, "n₁ = 1", XE, 230, 66, "g", TINTA, a))
        E.foco(c, t, C["s11.b"], 0.4, lambda a: E.formula(c, "n₂ = r{3}", XE + 330, 230, 66, "g", TINTA, a))
        E.foco(c, t, C["s11.c"], 0.4, lambda a: E.formula(c, "i = 60°", XE + 700, 230, 66, "g", COR, a))
        E.formula_em(c, t, C["s11.d"], "1 · f{r{3}}{2} = r{3} · sen r", XE, 420, 84, "g", TINTA)
        E.formula_em(c, t, C["s12.a"], "÷ r{3} dos dois lados", XE, 515, 44, "b", TINTA2)
        E.formula_em(c, t, C["s12.b"], "sen r = f{1}{2}", XE, 620, 90, "g", TINTA)
        bola_txt(c, t, C["s12.c"], "30°", XE + 700, 590, 100, 76)
        E.frase(c, t, C["s12.d"], [("60°", "g", 64), ("→", "g", 64, TINTA2), ("30°", "g", 64, COR)], XE, 830, passo=0.15)
        pilula_esq(c, t, C["s12.e"], "se aproximou da normal", XE, 940, 46, E.COR)
        return
    E.frase(c, t, C["s13.a"], ps("entrou no mais refringente:", "i", 54) + [("aproxima", "g", 54, COR)], XE, 300, passo=0.1)
    E.frase(c, t, C["s13.b"], ps("saiu para o menos refringente:", "i", 54) + [("afasta", "g", 54, COR)], XE, 420, passo=0.1)
    E.frase(c, t, C["s13.c"], ps("o lápis:", "i", 54) + [("a luz sai da água e se afasta", "g", 48)], XE, 560, passo=0.1)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s14"], [("cuidado", "g", 96, ERRADO)], XE, 200)
    E.frase(c, t, C["s14.a"], ps("virar a fração do", "i", 70) + [("índice", "g", 70, ERRADO)], XE, 330, passo=0.12)
    E.foco(c, t, C["s14.b"], 0.4, lambda a: E.formula(c, "n = f{v}{c}", XE, 540, 120, "g", ERRADO, a))
    E.formula_em(c, t, C["s14.c"], "= f{200.000}{300.000} = f{2}{3}", XE + 420, 540, 90, "g", TINTA)
    E.frase(c, t, C["s14.d"], ps("luz mais rápida que no", "i", 64) + [("vácuo?", "g", 64, ERRADO)], XE, 760, passo=0.12)
    E.foco(c, t, C["s14.d"] + 0.8, 0.5, lambda a: E.selo(c, 1700, 520, 70, False, a))
    pilula_esq(c, t, C["s14.e"], "deu menos que 1? fração de cabeça para baixo", XE, 920, 46, E.COR)


# ---------------- atalho (palco) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    if t < C["s16"]:
        E.frase(c, t, C["s15"], ps("o atalho de prova", "i", 72, CLARO), W / 2, 170, "center")
        E.frase(c, t, C["s15.a"], [("maior", "i", 90, CLARO), ("índice,", "g", 90, BR), ("menor", "i", 90, CLARO), ("ângulo", "g", 90, BR)], W / 2, 330, "center", 0.15)
        E.foco(c, t, C["s15.b"], 0.4, lambda a: centro(c, "n · sen  =  n · sen", W / 2, 480, 70, "g", CLARO, a))
        # gangorra: n grande ↔ seno pequeno
        if t >= C["s15.c"]:
            a = ep(t, C["s15.c"], 0.5)
            for k, (x, hn, hs) in enumerate(((760, 120, 260), (1160, 260, 120))):
                M.rrect(c, x - 60, 860 - hn, 50, hn, 8, E.COR, a)
                M.rrect(c, x + 10, 860 - hs, 50, hs, 8, CLARO, a)
                centro(c, "n", x - 35, 910, 44, "g", BR, a); centro(c, "sen", x + 35, 910, 40, "g", BR, a)
            centro(c, "meio 1", 760, 970, 40, "i", CLARO, a); centro(c, "meio 2", 1160, 970, 40, "i", CLARO, a)
        E.frase(c, t, C["s15.d"], ps("sem conta:", "i", 54, CLARO) + [("corte o raio que entorta errado", "g", 50, BR)], W / 2, 1040, "center", 0.1)
        return
    E.frase(c, t, C["s16.a"], [("índice", "g", 76, BR), ("e", "i", 80, CLARO), ("velocidade:", "g", 76, BR), ("ao contrário", "i", 80, CLARO)], W / 2, 220, "center", 0.12)
    E.foco(c, t, C["s16.b"], 0.4, lambda a: centro(c, "n × 2  →  v ÷ 2", W / 2, 420, 96, "g", BR, a))
    E.foco(c, t, C["s16.c"], 0.4, lambda a: (centro(c, "n = 2", W / 2 - 330, 620, 80, "g", BR, a), centro(c, "→", W / 2, 620, 80, "g", CLARO, a)))
    E.foco(c, t, C["s16.c"] + 0.3, 0.4, lambda a: F.medida(c, "150.000", "km/s", W / 2 + 80, 620, 80, BR, a, escuro=True))
    E.frase(c, t, C["s16.d"], ps("ângulo exato:", "i", 60, CLARO) + [("só com a lei de Snell", "g", 60, BR)], W / 2, 860, "center", 0.12)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s17"], ps("hora de testar", "i", 72, COR), XE, 190)
    E.frase(c, t, C["s17.a"], ps("do ar para um líquido de", "i", 60) + [("n = √2", "g", 60, COR)], XE, 340, passo=0.1)
    E.frase(c, t, C["s17.b"], ps("chegando a", "i", 60) + [("45°", "g", 60, COR)] + ps("da normal", "i", 60), XE, 450, passo=0.1)
    E.frase(c, t, C["s17.c"], ps("ângulo de", "i", 70) + [("refração?", "g", 70, COR)], XE, 620, passo=0.12)
    E.frase(c, t, C["s17.d"], [("aproxima", "g", 62), ("ou", "i", 66), ("afasta?", "g", 62, COR)], XE, 750, passo=0.15)
    if t < C["s18"]:
        P = (1450, 640)
        meios(c, t, C["s17.a"], 1100, 1820, P[1], 300, 1000, "ar", "n = r{2}")
        gi = math.radians(45)
        F.normal(c, t, C["s17.b"], P, 90, 330)
        F.raio(c, t, C["s17.b"] + 0.2, [(P[0] - 330 * math.sin(gi), P[1] - 330 * math.cos(gi)), P], d=0.7)
        E.angulo(c, t, C["s17.b"] + 0.9, P, (P[0] - 300 * math.sin(gi), P[1] - 300 * math.cos(gi)), (P[0], P[1] - 300), "45°", r=110, size=46)
    questao_relogio(c, t, C, "s18")


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    P = (1450, 600)
    meios(c, t, C["s19"], 1060, 1840, P[1], 200, 1000, "ar", "n = r{2}")
    snell(c, t, C["s19"] + 0.3, C["s19.d"], P, 45, 30, rot_i="45°", rot_r="30°", ta=(C["s19"] + 1.0, C["s19.d"] + 0.7), size=46)
    E.formula_em(c, t, C["s19.a"], "1 · f{r{2}}{2}", XE, 300, 84, "g", TINTA)
    E.formula_em(c, t, C["s19.b"], "= r{2} · sen r", XE + 300, 300, 84, "g", TINTA)
    E.formula_em(c, t, C["s19.c"], "sen r = f{1}{2}", XE, 500, 84, "g", TINTA)
    bola_txt(c, t, C["s19.d"], "30°", XE + 640, 470, 100, 76)
    E.frase(c, t, C["s20.a"], [("45°", "g", 60), ("→", "g", 60, TINTA2), ("30°:", "g", 60, COR), ("aproximou", "g", 60, COR)], XE, 720, passo=0.12)
    E.frase(c, t, C["s20.b"], ps("maior índice, menor ângulo", "i", 56, TINTA2), XE, 830, passo=0.1)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def r():
        resumo(c, t, C, "s21", [("s21.a", [("n = c ÷ v", "g", 62, COR), ("e nunca menor que 1", "i")]),
                                ("s21.b", [("n₁ · sen i = n₂ · sen r", "g", 62, COR)]),
                                ("s21.c", [("maior índice,", "i"), ("menor ângulo", "g"), ("com a normal", "i")])], y0=380, dy=200)
    E.saida(c, t, C["s22"] - 0.1, r)
    if t < C["s22"]:
        return

    def desenho():
        if t < C["s22.b"]:
            return
        P = (700, 780)
        meios(c, t, C["s22.b"], 300, 1100, P[1], 560, 1000, "", "", alfa=0.5, rot=False)
        F.normal(c, t, C["s22.b"] + 0.2, P, 90, 200)
        F.raio(c, t, C["s22.b"] + 0.3, [(500, 1000), P, (900, 1000 - 0)], d=1.2)
    proxima(c, t, C, "s22", [("a luz", "i", 100), ("fica presa", "g", 100, COR)], [("reflexão total", "g", 72), ("e as cores", "i", 72)], desenho, k_insc="d", k_bons="e")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, refracao=b_refracao, indice=b_indice, snell=b_snell, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
