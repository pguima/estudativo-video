"""Visual — Estudativo · FIS-OPT-008: olho humano e defeitos da visão.
Segue a linguagem visual da trilha Óptica, escrita no cabeçalho do visual.py da FIS-OPT-001 (raio laranja, lente em
azul-vidro, imagem petróleo). Peça nova: olho em corte (olho_corte), com córnea, pupila, cristalino e a retina em petróleo;
o ponto onde os raios se encontram é marcado com uma bolinha: na retina = nítido, fora dela = borrado.
Todo instante vem de C[...] (marcadores do roteiro)."""
import math

import editorial as E
import fisica as F
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Física", "Óptica")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_FIS-OPT-008_olho_humano_defeitos_da_visao.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("olho", "miopia", "hiper", "astig", "atalho", "questao", "fim"))

# todas as contas da aula
assert 1 / -0.5 == -2                     # míope com ponto remoto a 50 cm: −2 graus
assert -1 / 0.25 == -4                    # atalho: ponto remoto de 25 cm, −4 graus
assert 40 / 100 == 0.4 and -1 / 0.4 == -2.5   # questão: 40 cm → −2,5 graus


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
def olho_corte(c, xf, cy, R, a=1.0, comp=1.0, curva=1.0, escuro=False, retina_cor=None):
    """olho em corte, de lado, olhando para a esquerda. xf = frente da córnea; comp = alongamento; curva = cristalino mais
    curvo (> 1). Devolve dict(xL = cristalino, xr = retina)"""
    rx = R * comp
    cx = xf + rx
    xL = xf + 0.32 * R
    xr = xf + 2 * rx
    if a <= 0:
        return dict(xL=xL, xr=xr)
    tinta = BR if escuro else TINTA
    ret = skia.Rect.MakeXYWH(cx - rx, cy - R, 2 * rx, 2 * R)
    c.drawOval(ret, M.paint("#FFFFFF" if not escuro else "#2A2A33", 0.9 * a))
    c.drawOval(ret, M.paint(tinta, a, stroke=6))
    # retina: o fundo do olho
    c.drawArc(ret, -55, 110, False, M.paint(retina_cor or F.VEL, a, stroke=14))
    # córnea: a janela da frente
    c.drawArc(skia.Rect.MakeXYWH(xf - 0.12 * R, cy - 0.45 * R, 0.5 * R, 0.9 * R), 110, 140, False, M.paint(VIDRO, a, stroke=10))
    # íris e pupila
    M.line(c, xL - 0.12 * R, cy - 0.62 * R, xL - 0.12 * R, cy - 0.2 * R, "#6B4A2E", a, 10)
    M.line(c, xL - 0.12 * R, cy + 0.2 * R, xL - 0.12 * R, cy + 0.62 * R, "#6B4A2E", a, 10)
    # cristalino
    w = 0.16 * R * curva
    c.drawOval(skia.Rect.MakeXYWH(xL - w / 2, cy - 0.34 * R, w, 0.68 * R), M.paint(VIDRO, 0.9 * a))
    c.drawOval(skia.Rect.MakeXYWH(xL - w / 2, cy - 0.34 * R, w, 0.68 * R), M.paint(tinta, a, stroke=3))
    return dict(xL=xL, xr=xr)


def raios_olho(c, t, t0, x0, xL, cy, xfoco, xfim, dys=(-70, 0, 70), fonte=None, d=1.2, depois=None):
    """raios que chegam (paralelos, ou de uma fonte perto), passam pelo cristalino em xL e se encontram em xfoco;
    depois = lista de alturas no cristalino (quando uma lente de correção já desviou os raios). Marca o encontro."""
    for k, dy in enumerate(dys):
        P0 = fonte if fonte else (x0, cy + dy)
        yL = cy + (depois[k] if depois else dy)
        Hh = (xL, yL)
        u = _u(Hh, (xfoco, cy))
        fim = (Hh[0] + u[0] * (xfim - xL) / max(0.2, u[0]), Hh[1] + u[1] * (xfim - xL) / max(0.2, u[0]))
        F.raio(c, t, t0 + 0.08 * k, [P0, Hh, fim] if fonte or not depois else [P0, Hh, fim], d=d, largura=4, setas=k == 0)
    E.foco(c, t, t0 + d, 0.3, lambda a: c.drawCircle(xfoco, cy, 13, M.paint(E.COR, a)))


def receita(c, cx, cy, grau, a=1.0, w=440):
    if a <= 0:
        return
    M.rrect(c, cx - w / 2, cy - 150, w, 300, 20, BR, a, shadow=True)
    E.escreve(c, "receita", cx - w / 2 + 40, cy - 80, 44, "i", TINTA2, a)
    M.line(c, cx - w / 2 + 40, cy - 60, cx + w / 2 - 40, cy - 60, FIO, a, 3)
    E.escreve(c, grau, cx - w / 2 + 40, cy + 80, 110, "g", COR, a)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def um():
        E.foco(c, t, C["s01.a"], 0.5, lambda a: receita(c, 620, 440, "−2,00", a))
        E.frase(c, t, C["s01.a"] + 0.3, [("miopia", "g", 70)], 620, 700, "center")
        E.foco(c, t, C["s01.b"], 0.5, lambda a: receita(c, 1300, 440, "+2,00", a))
        E.frase(c, t, C["s01.b"] + 0.3, [("hipermetropia", "g", 70)], 1300, 700, "center")
        if t >= C["s01.c"]:
            F.lente(c, t, C["s01.c"], 620, 860, 180, False, None)
            F.lente(c, t, C["s01.c"] + 0.2, 1300, 860, 180, True, None)
        E.frase(c, t, C["s01.c"], ps("o sinal diz", "i", 60) + [("a lente", "g", 60, COR)], W / 2, 220, "center", 0.12)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t >= C["s02"]:
        promessa(c, t, C, "s02", [("s02.b", "onde cai a imagem"), ("s02.c", "a lente que corrige")])


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    lembrete(c, t, C, "s03", [("s03.b", "convergente junta,", "divergente espalha"), ("s03.c", "o grau:", "1 ÷ f, com f em metros")])


# ---------------- o olho ----------------
XF, CYO, RO = 760, 600, 280


def b_olho(c, t, C, b):
    if t < C["s05"]:
        g = olho_corte(c, XF, CYO, RO, ep(t, C["s04"], 0.6))
        for k, (kk, s, x, y) in enumerate((("s04.a", "córnea", XF - 330, CYO - 150), ("s04.b", "pupila", g["xL"] - 120, CYO + 260),
                                            ("s04.c", "cristalino", g["xL"] - 60, CYO - RO - 30))):
            E.foco(c, t, C[kk], 0.4, lambda a, s=s, x=x, y=y: E.escreve(c, s, x, y, 52, "g", COR, a))
        E.foco(c, t, C["s04.a"], 0.4, lambda a: E.escreve(c, "janela da frente", XF - 330, CYO - 100, 38, "i", TINTA2, a))
        raios_olho(c, t, C["s04.d"], 200, g["xL"], CYO, g["xr"], g["xr"])
        E.frase(c, t, C["s04.d"], ps("juntos: uma lente", "i", 58) + [("convergente", "g", 58, COR)], XE, 980, passo=0.1)
        return
    if t < C["s06"]:
        g = olho_corte(c, XF, CYO, RO)
        raios_olho(c, t, C["s05"] - 1.0, 200, g["xL"], CYO, g["xr"], g["xr"], d=0.6)
        E.foco(c, t, C["s05.a"], 0.4, lambda a: E.escreve(c, "retina", g["xr"] + 30, CYO - 220, 56, "g", F.VEL, a))
        E.frase(c, t, C["s05.a"], ps("a imagem se forma na", "i", 60) + [("retina", "g", 60, F.VEL)], XE, 200, passo=0.1)
        imagem_i(c, t, C["s05.c"], g["xr"] - 12, CYO, -80, True)
        classifica(c, t, [(C["s05.b"], "real"), (C["s05.c"], "invertida"), (C["s05.d"], "menor")], XE, 980, 54)
        E.frase(c, t, C["s05.e"], ps("o", "i", 56) + [("cérebro", "g", 56, COR)] + ps("deixa de pé", "i", 56), 1250, 980, passo=0.1)
        return
    # s06: acomodação, pontos remoto e próximo
    curva = 1 + 0.9 * ease_io(prog(t, C["s06.a"], 1.0)) * (1 - ease_io(prog(t, C["s06.d"] - 0.6, 0.6)))
    g = olho_corte(c, 1000, 500, 220, curva=curva)
    E.frase(c, t, C["s06.a"], ps("cristalino mais", "i", 60) + [("curvo", "g", 60, COR)], XE, 200, passo=0.1)
    E.frase(c, t, C["s06.b"], ps("foco", "i", 60) + [("menor", "g", 60)], XE, 290, passo=0.1)
    pilula_esq(c, t, C["s06.c"], "acomodação", XE, 400, 56, E.COR)
    E.frase(c, t, C["s06.d"], [("ponto remoto:", "g", 52)] + ps("o mais longe nítido;", "i", 52) + [("normal: infinito", "g", 52, COR)], XE, 860, passo=0.08)
    E.frase(c, t, C["s06.e"], [("ponto próximo:", "g", 52)] + ps("o mais perto;", "i", 52) + [("normal: ≈ 25 cm", "g", 52, COR)], XE, 960, passo=0.08)


# ---------------- miopia ----------------
def b_miopia(c, t, C, b):
    xf, cy, R = 880, 560, 250
    if t < C["s09"]:
        g = olho_corte(c, xf, cy, R, ep(t, C["s07"], 0.5), comp=1.25)
        xfoco = xf + 2 * R  # foco do olho normal: cai antes da retina do olho comprido
        E.frase(c, t, C["s07.a"], [("miopia:", "g", 70, COR)] + ps("olho comprido", "i", 66), XE, 200, passo=0.12)
        if t < C["s08"]:
            raios_olho(c, t, C["s07.b"], 260, g["xL"], cy, xfoco, g["xr"])
            E.foco(c, t, C["s07.b"] + 1.2, 0.4, lambda a: centro(c, "antes da retina", xfoco, cy + 330, 50, "g", COR, a))
            E.foco(c, t, C["s07.c"], 0.4, lambda a: centro(c, "borrado", g["xr"] - 20, cy - 290, 46, "i", ERRADO, a))
            pilula_esq(c, t, C["s07.d"], "vê mal de longe", XE, 960, 54, E.COR)
            return
        # s08: lente divergente na frente
        xc = xf - 220
        F.lente(c, t, C["s08.a"], xc, cy, 300, False, None)
        E.foco(c, t, C["s08.a"] + 0.3, 0.4, lambda a: centro(c, "divergente", xc, cy + 230, 46, "g", COR, a))
        dys = (-70, 0, 70)
        dep = [dy * 1.18 for dy in dys]
        for k, dy in enumerate(dys):
            F.raio(c, t, C["s08.b"] + 0.08 * k, [(260, cy + dy), (xc, cy + dy), (g["xL"], cy + dep[k]), (g["xr"], cy)], d=1.4, largura=4, setas=k == 0)
        E.foco(c, t, C["s08.c"], 0.3, lambda a: c.drawCircle(g["xr"] - 8, cy, 13, M.paint(CERTO, a)))
        E.foco(c, t, C["s08.c"], 0.4, lambda a: centro(c, "na retina: nítido", g["xr"] - 20, cy - 290, 46, "g", CERTO, a))
        E.frase(c, t, C["s08.d"], ps("por isso o grau é", "i", 60) + [("negativo", "g", 60, COR)], XE, 960, passo=0.1)
        return
    # s09: a conta do míope
    E.frase(c, t, C["s09.a"], ps("ponto remoto a", "i", 64) + [("50 cm", "g", 64, COR)], XE, 220, passo=0.12)
    cx2, cy2, f2 = 1250, 560, 330
    F.lente(c, t, C["s09.b"], cx2, cy2, 320, False, None, eixo=(cx2 - 420, cx2 + 420))
    for k, dy in enumerate((-80, 80)):
        Hh = (cx2, cy2 + dy)
        u = _u((cx2 - f2, cy2), Hh)
        F.raio(c, t, C["s09.b"] + 0.3 + 0.1 * k, [(cx2 - 400, cy2 + dy), Hh, (Hh[0] + u[0] * 300, Hh[1] + u[1] * 300)], d=1.0, largura=5)
        prolonga(c, t, C["s09.c"], Hh, (cx2 - f2, cy2))
    eixo_pontos(c, t, C["s09.c"], cy2, [(cx2 - f2, "F")])
    E.segmento(c, t, C["s09.c"] + 0.4, (cx2 - f2, cy2 + 200), (cx2, cy2 + 200), "50 cm", cor=E.COR, largura=4, lado=-1, size=46)
    E.frase(c, t, C["s09.b"], ps("objeto distante:", "i", 52) + [("a imagem cai no foco", "g", 52)], XE, 330, passo=0.1)
    E.formula_em(c, t, C["s09.d"], "f = −0,5 m", XE, 560, 90, "g", TINTA)
    bola_txt(c, t, C["s09.e"], "−2 graus", XE + 220, 800, 140, 56)


# ---------------- hipermetropia e presbiopia ----------------
def b_hiper(c, t, C, b):
    xf, cy, R = 900, 560, 250
    if t < C["s11"]:
        g = olho_corte(c, xf, cy, R, ep(t, C["s10"], 0.5), comp=0.8)
        fonte = (xf - 520, cy)
        xfoco = g["xr"] + 170
        E.frase(c, t, C["s10.a"], [("hipermetropia:", "g", 66, COR)] + ps("olho curto", "i", 62), XE, 200, passo=0.12)
        E.foco(c, t, C["s10.b"] - 0.3, 0.4, lambda a: (M.line(c, fonte[0], cy, fonte[0], cy - 90, TINTA, a, 8), centro(c, "objeto perto", fonte[0], cy + 80, 40, "i", TINTA2, a)))
        raios_olho(c, t, C["s10.b"], 0, g["xL"], cy, xfoco, xfoco + 40, dys=(-60, 60), fonte=fonte)
        E.foco(c, t, C["s10.b"] + 1.2, 0.4, lambda a: centro(c, "depois da retina", xfoco, cy + 300, 48, "g", COR, a))
        pilula_esq(c, t, C["s10.c"], "vê mal de perto", XE, 880, 52, E.COR)
        if t >= C["s10.d"]:
            F.lente(c, t, C["s10.d"], xf - 200, cy, 300, True, None)
        E.frase(c, t, C["s10.d"], [("convergente,", "g", 58, COR)] + ps("grau positivo", "i", 60), XE, 990, passo=0.1)
        return
    E.frase(c, t, C["s11.a"], [("presbiopia,", "g", 70, COR)] + ps("a vista cansada", "i", 70), XE, 220, passo=0.12)
    E.frase(c, t, C["s11.b"], ps("o cristalino", "i", 60) + [("endurece", "g", 60)], XE, 360, passo=0.1)
    E.frase(c, t, C["s11.c"], ps("o ponto próximo", "i", 60) + [("se afasta", "g", 60, COR)], XE, 470, passo=0.1)
    E.foco(c, t, C["s11.c"] + 0.8, 0.4, lambda a: E.escreve(c, "de perto, a imagem cai depois da retina", XE, 560, 46, "i", TINTA2, a))
    E.frase(c, t, C["s11.d"], ps("estica o braço para", "i", 60) + [("ler", "g", 60)], XE, 700, passo=0.1)
    pilula_esq(c, t, C["s11.e"], "convergente: óculos de leitura", XE, 840, 52, E.COR)
    # o livro que se afasta
    q = ease_io(prog(t, C["s11.d"], 1.4))
    if t >= C["s11.a"]:
        a = ep(t, C["s11.a"], 0.5)
        olho(c, 1700, 520, 60, a, -1)
        xb = lerp(1500, 1180, q)
        M.rrect(c, xb - 60, 440, 120, 160, 8, "#F4F1E8", a)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(xb - 60, 440, 120, 160), 8, 8), M.paint(TINTA, a, stroke=4))
        for j in range(4):
            M.line(c, xb - 40, 480 + 30 * j, xb + 40, 480 + 30 * j, TINTA2, a, 4)


# ---------------- astigmatismo ----------------
def b_astig(c, t, C, b):
    E.frase(c, t, C["s12.a"], [("astigmatismo:", "g", 70, COR)] + ps("córnea irregular", "i", 66), XE, 200, passo=0.12)
    E.frase(c, t, C["s12.b"], ps("mais curva numa direção:", "i", 54) + [("bola de futebol americano", "g", 54)], XE, 300, passo=0.1)
    # bola redonda × bola oval
    if t >= C["s12.b"]:
        a = ep(t, C["s12.b"], 0.5)
        c.drawCircle(500, 560, 120, M.paint(VIDRO, 0.7 * a)); c.drawCircle(500, 560, 120, M.paint(TINTA, a, stroke=4))
        centro(c, "normal", 500, 730, 44, "i", TINTA2, a)
        c.drawOval(skia.Rect.MakeXYWH(760, 470, 280, 180), M.paint(VIDRO, 0.7 * a)); c.drawOval(skia.Rect.MakeXYWH(760, 470, 280, 180), M.paint(TINTA, a, stroke=4))
        centro(c, "astigmatismo", 900, 730, 44, "i", TINTA2, a)
    # linhas: verticais nítidas, horizontais borradas
    if t >= C["s12.c"]:
        a = ep(t, C["s12.c"], 0.5)
        for j in range(5):
            M.line(c, 1250 + 50 * j, 430, 1250 + 50 * j, 690, TINTA, a, 7)
        pt = skia.Paint(); pt.setImageFilter(skia.ImageFilters.Blur(7, 7)); pt.setAlphaf(a)
        c.saveLayer(None, pt)
        for j in range(5):
            M.line(c, 1550, 450 + 55 * j, 1810, 450 + 55 * j, TINTA, 1.0, 7)
        c.restore()
        centro(c, "nítidas", 1350, 760, 44, "g", CERTO, a); centro(c, "borradas", 1680, 760, 44, "g", ERRADO, a)
    # lente cilíndrica
    if t >= C["s12.d"]:
        a = ep(t, C["s12.d"], 0.5)
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeLinear([skia.Point(1150, 0), skia.Point(1450, 0)], [M.hexc(VIDRO, 0.4 * a), M.hexc("#FFFFFF", 0.9 * a), M.hexc(VIDRO, 0.4 * a)], [0, 0.5, 1]))
        c.drawRect(skia.Rect.MakeLTRB(1150, 860, 1450, 1000), p)
        c.drawRect(skia.Rect.MakeLTRB(1150, 860, 1450, 1000), M.paint(TINTA, a, stroke=3))
    E.frase(c, t, C["s12.d"], ps("correção: lente", "i", 60) + [("cilíndrica", "g", 60, COR)], XE, 950, passo=0.1)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    xf, cy, R = 1000, 600, 240
    E.frase(c, t, C["s13"], [("cuidado", "g", 96, ERRADO)], XE, 200)
    E.frase(c, t, C["s13.a"], ps("convergente para o", "i", 64) + [("míope?", "g", 64, ERRADO)], XE, 320, passo=0.12)
    g = olho_corte(c, xf, cy, R, ep(t, C["s13"], 0.5), comp=1.25)
    E.frase(c, t, C["s13.b"], ps("o olho já", "i", 56) + [("converge demais", "g", 56)], XE, 960, passo=0.1)
    if t >= C["s13.c"]:
        xc = xf - 220
        F.lente(c, t, C["s13.c"], xc, cy, 280, True, None)
        dys = (-70, 0, 70)
        xfoco = xf + 1.35 * R
        for k, dy in enumerate(dys):
            yL = cy + dy * 0.75
            u = _u((g["xL"], yL), (xfoco, cy))
            fim = (g["xL"] + u[0] * (g["xr"] - g["xL"]) / u[0], yL + u[1] * (g["xr"] - g["xL"]) / u[0])
            F.raio(c, t, C["s13.c"] + 0.08 * k, [(420, cy + dy), (xc, cy + dy), (g["xL"], yL), fim], d=1.4, largura=4, setas=k == 0)
        E.foco(c, t, C["s13.c"] + 1.4, 0.3, lambda a: c.drawCircle(xfoco, cy, 13, M.paint(ERRADO, a)))
    E.foco(c, t, C["s13.d"], 0.4, lambda a: centro(c, "ainda mais longe da retina", xf + 260, cy + 320, 46, "g", ERRADO, a))
    E.foco(c, t, C["s13.d"] + 0.6, 0.5, lambda a: E.selo(c, 1760, 330, 60, False, a))


# ---------------- atalho (palco) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    if t < C["s15"]:
        E.frase(c, t, C["s14"], ps("o atalho de prova", "i", 72, CLARO), W / 2, 170, "center")
        E.foco(c, t, C["s14.a"], 0.5, lambda a: (centro(c, "Míope", 700, 400, 120, "g", BR, a), centro(c, "→", 960, 400, 110, "g", CLARO, a),
                                                 centro(c, "Menos", 1240, 400, 120, "g", BR, a)))
        linhas = (("s14.b", "miopia", "divergente, grau −"), ("s14.c", "hipermetropia e presbiopia", "convergente, grau +"), ("s14.d", "astigmatismo", "cilíndrica"))
        for i, (k, l1, l2) in enumerate(linhas):
            y = 600 + 120 * i
            E.linha(c, t, [(l1 + ":", "g", 54, BR, C[k]), (l2, "i", 58, CLARO, C[k] + 0.3)], W / 2, y, "center")
        return
    E.frase(c, t, C["s15"], ps("a conta do", "i", 70, CLARO) + [("míope", "g", 70, BR)], W / 2, 190, "center", 0.12)
    E.formula_em(c, t, C["s15.a"], "grau = −f{1}{ponto remoto (m)}", W / 2, 400, 96, "g", BR, "center")
    E.foco(c, t, C["s15.b"], 0.4, lambda a: centro(c, "25 cm = 0,25 m  →  −1 ÷ 0,25 = −4", W / 2, 620, 66, "g", CLARO, a))
    E.frase(c, t, C["s15.c"], ps("a lente tem o", "i", 58, CLARO) + [("foco no ponto remoto", "g", 58, BR)], W / 2, 780, "center", 0.1)
    E.frase(c, t, C["s15.d"], [("hipermetropia:", "g", 54, BR)] + ps("essa conta não serve", "i", 58, CLARO), W / 2, 930, "center", 0.1)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s16"], ps("hora de testar", "i", 72, COR), XE, 190)
    E.frase(c, t, C["s16.a"], ps("enxerga nítido só até", "i", 66) + [("40 cm", "g", 66, COR)], XE, 360, passo=0.1)
    E.frase(c, t, C["s16.b"], ps("qual o", "i", 70) + [("defeito?", "g", 70, COR)], XE, 520, passo=0.12)
    E.frase(c, t, C["s16.c"], ps("que", "i", 70) + [("lente?", "g", 70, COR)], XE, 640, passo=0.12)
    E.frase(c, t, C["s16.d"], ps("qual o", "i", 70) + [("grau?", "g", 70, COR)], XE, 760, passo=0.12)
    if t < C["s17"]:
        E.foco(c, t, C["s16.a"], 0.5, lambda a: olho(c, 1650, 520, 70, a, -1))
        E.segmento(c, t, C["s16.a"] + 0.3, (1250, 640), (1580, 640), "40 cm", cor=E.COR, largura=4, lado=-1, size=46)
    questao_relogio(c, t, C, "s17")


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    E.frase(c, t, C["s18.a"], ps("não vê nítido de longe:", "i", 62) + [("miopia", "g", 62, COR)], XE, 230, passo=0.1)
    pilula_esq(c, t, C["s18.b"], "lente divergente", XE, 360, 54, E.COR)
    E.foco(c, t, C["s18.c"], 0.4, lambda a: E.formula(c, "40 cm = 0,4 m", XE, 540, 84, "g", TINTA, a))
    E.formula_em(c, t, C["s18.d"], "grau = −f{1}{0,4}", XE, 760, 96, "g", TINTA)
    bola_txt(c, t, C["s18.e"], "−2,5 graus", XE + 900, 730, 150, 56)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def r():
        resumo(c, t, C, "s19", [("s19.a", [("na retina:", "g"), ("real, invertida, menor", "i")]),
                                ("s19.b", [("miopia:", "g"), ("antes da retina:", "i"), ("divergente", "g", 58, COR)]),
                                ("s19.c", [("hipermetropia e presbiopia:", "g"), ("convergente", "g", 58, COR)]),
                                ("s19.d", [("astigmatismo:", "g"), ("cilíndrica", "g", 58, COR)])], y0=340, dy=170, size=58)
    E.saida(c, t, C["s20"] - 0.1, r)
    if t < C["s20"]:
        return
    proxima(c, t, C, "s20", [("as lentes", "i", 96), ("viram instrumentos", "g", 96, COR)], [("lupa, câmera,", "g", 64), ("microscópio e luneta", "i", 64)], None)


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, olho=b_olho, miopia=b_miopia, hiper=b_hiper, astig=b_astig,
              erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
