"""Visual — Estudativo · FIS-OPT-006: lentes, convergente e divergente, e a imagem pelos raios notáveis.
Segue a linguagem visual da trilha Óptica, escrita no cabeçalho do visual.py da FIS-OPT-001 (raio laranja, prolongamento
tracejado cinza, objeto em tinta, imagem petróleo, lente em azul-vidro com F e F' laranja). Os raios dos diagramas são
calculados (raios_lente): a imagem cai onde a equação manda, mesmo sem a conta aparecer nesta aula.
Todo instante vem de C[...] (marcadores do roteiro)."""
import math

import editorial as E
import fisica as F
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Física", "Óptica")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_FIS-OPT-006_lentes_convergente_divergente.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("tipos", "raios", "convergente", "divergente", "atalho", "questao", "fim"))


def _g(f, p):
    return f * p / (p - f)


# os desenhos seguem a equação das lentes (a conta é da FIS-OPT-007)
assert _g(200, 120) < 0 and abs(_g(200, 120) / 120) > 1      # lupa: virtual, direita, maior
assert _g(200, 520) > 0 and abs(_g(200, 520) / 520) < 1      # paisagem: real, invertida, menor
assert _g(230, 600) > 0 and abs(_g(230, 600) / 600) < 1      # além de 2F: câmera
assert _g(260, 150) < 0 and abs(_g(260, 150) / 150) > 1      # dentro do foco: lupa
assert _g(230, 350) > 0 and abs(_g(230, 350) / 350) > 1      # entre F e 2F: projetor
assert _g(-260, 450) < 0 and abs(_g(-260, 450) / 450) < 1    # divergente: virtual, direita, menor


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
def diagrama(c, t, cx, cy, f, xo, ho, t_l, t_obj, ts, t_img, tipos=("par", "centro"), x0=None, x1=None, h=None, dois_f=False):
    """lente, eixo, focos, objeto, raios e imagem; devolve (xi, hi)"""
    h = h or 420
    F.lente(c, t, t_l, cx, cy, h, f > 0, abs(f), eixo=(x0 if x0 is not None else cx - 800, x1 if x1 is not None else cx + 600))
    if dois_f:
        eixo_pontos(c, t, t_l + 0.4, cy, [(cx - 2 * abs(f), "2F"), (cx + 2 * abs(f), "2F'")])
    objeto_o(c, t, t_obj, xo, cy, ho)
    xi, hi = raios_lente(c, t, ts, cx, cy, f, xo, ho, tipos)
    imagem_i(c, t, t_img, xi, cy, hi, real=xi > cx)
    return xi, hi


def perfil(c, cx, cy, h, xl, xr, offL, offR, a=1.0, escuro=False):
    """corte de uma lente: borda esquerda em xl e direita em xr (relativas a cx); off = quanto a face se curva
    (negativo = barriga para a esquerda, positivo = para a direita)"""
    if a <= 0:
        return
    p = skia.Path()
    p.moveTo(cx + xl, cy - h / 2); p.lineTo(cx + xr, cy - h / 2)
    p.quadTo(cx + xr + offR, cy, cx + xr, cy + h / 2)
    p.lineTo(cx + xl, cy + h / 2)
    p.quadTo(cx + xl + offL, cy, cx + xl, cy - h / 2)
    p.close()
    c.drawPath(p, M.paint(VIDRO, 0.55 * a))
    pt = M.paint(BR if escuro else TINTA, a, stroke=5); pt.setStrokeJoin(skia.Paint.kRound_Join)
    c.drawPath(p, pt)


PERFIS = dict(biconvexa=(-14, 14, -90, 90), plano_convexa=(-14, 14, 0, 110), concavo_convexa=(-24, 12, 50, 120),
              biconcava=(-60, 60, 80, -80), plano_concava=(-45, 45, 0, -90), convexo_concava=(-45, 60, -40, -110))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def um():
        cy = 600
        E.frase(c, t, C["s01.a"], ps("perto:", "i", 60) + [("grande e de pé", "g", 60, COR)], XE, 220, passo=0.12)
        diagrama(c, t, 620, cy, 200, 500, 80, C["s01.a"], C["s01.a"] + 0.3, (C["s01.a"] + 0.6, C["s01.a"] + 1.0), C["s01.a"] + 2.2, x0=200, x1=960, h=360)
        E.frase(c, t, C["s01.b"], ps("longe:", "i", 60) + [("pequena e invertida", "g", 60, COR)], 1060, 220, passo=0.12)
        diagrama(c, t, 1420, cy, 200, 900, 150, C["s01.b"], C["s01.b"] + 0.3, (C["s01.b"] + 0.6, C["s01.b"] + 1.0), C["s01.b"] + 2.2, x0=860, x1=1840, h=360)
        E.frase(c, t, C["s01.c"], ps("a lente é a", "i", 60) + [("mesma", "g", 60)], XE, 960, passo=0.12)
        E.frase(c, t, C["s01.d"], ps("mudou", "i", 60) + [("a distância", "g", 60, COR)], 1060, 960, passo=0.12)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t >= C["s02"]:
        promessa(c, t, C, "s02", [("s02.b", "convergente ou divergente"), ("s02.c", "a imagem pelos raios")])


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    lembrete(c, t, C, "s03", [("s03.b", "no vidro, o raio:", "aproxima e, ao sair, afasta"), ("s03.c", "raios notáveis:", "real cruza, virtual prolonga")])


# ---------------- tipos ----------------
def b_tipos(c, t, C, b):
    if t < C["s05"]:
        E.frase(c, t, C["s04.a"], [("lente:", "g", 76, COR)] + ps("vidro com face curva", "i", 70), XE, 240, passo=0.12)
        E.foco(c, t, C["s04.a"] + 0.4, 0.6, lambda a: perfil(c, 1200, 620, 520, *PERFIS["biconvexa"], a=a))
        F.raio(c, t, C["s04.b"], [(700, 470), (1121, 470), (1279, 505), (1700, 700)], d=1.4)
        E.foco(c, t, C["s04.b"] + 0.5, 0.4, lambda a: centro(c, "entra", 1100, 430, 44, "i", TINTA2, a))
        E.foco(c, t, C["s04.b"] + 0.9, 0.4, lambda a: centro(c, "sai", 1320, 470, 44, "i", TINTA2, a))
        E.frase(c, t, C["s04.b"], ps("refrata", "i", 64) + [("duas vezes", "g", 64, COR)], XE, 360, passo=0.12)
        return
    if t < C["s06"]:
        y = 560
        for k, (nome, cx, ks, perf, conv) in enumerate((("convergente", 600, ("s05.a", "s05.b", "s05.c"), "biconvexa", True),
                                                        ("divergente", 1340, ("s05.d", "s05.e", "s05.f"), "biconcava", False))):
            E.foco(c, t, C[ks[0]], 0.5, lambda a, cx=cx, perf=perf: perfil(c, cx, y, 360, *PERFIS[perf], a=a))
            for j, dy in enumerate((-110, 0, 110)):
                if conv:
                    pts = [(cx - 380, y + dy), (cx, y + dy), (cx + 230, y), (cx + 330, y - dy * 100 / 230)]
                else:
                    pts = [(cx - 380, y + dy), (cx, y + dy), (cx + 330, y + dy + dy * 330 / 230)]
                F.raio(c, t, C[ks[1]] + 0.1 * j, pts, d=1.0, largura=5)
            E.frase(c, t, C[ks[0]], [("bordas", "i", 54), ("finas" if conv else "grossas", "g", 54)], cx, y - 260, "center", 0.12)
            E.foco(c, t, C[ks[1]] + 0.5, 0.4, lambda a, cx=cx, conv=conv: centro(c, "junta" if conv else "espalha", cx, y + 290, 52, "i", TINTA, a))
            E.foco(c, t, C[ks[2]], 0.4, lambda a, cx=cx, nome=nome: centro(c, nome, cx, y + 380, 70, "g", COR, a))
        pilula_em(c, t, C["s05.g"], "vale para vidro no ar; num meio mais refringente, inverte", W / 2, 1020, 40, TINTA)
        return
    cx, cy, f = 900, 600, 300
    F.lente(c, t, C["s06"] - 0.4, cx, cy, 440, True, None, eixo=(260, 1820))
    eixo_pontos(c, t, C["s06.a"], cy, [(cx, "O")])
    E.foco(c, t, C["s06.a"] + 0.3, 0.4, lambda a: E.escreve(c, "eixo principal", 280, cy - 30, 44, "i", TINTA2, a))
    eixo_pontos(c, t, C["s06.b"], cy, [(cx - f, "F"), (cx + f, "F'")])
    E.segmento(c, t, C["s06.b"] + 0.4, (cx - f, cy + 230), (cx, cy + 230), "f", cor=E.COR, largura=4, lado=-1, size=48)
    E.segmento(c, t, C["s06.b"] + 0.6, (cx, cy + 230), (cx + f, cy + 230), "f", cor=E.COR, largura=4, lado=-1, size=48)
    for j, dy in enumerate((-150, -75, 75, 150)):
        F.raio(c, t, C["s06.c"] + 0.1 * j, [(cx - 560, cy + dy), (cx, cy + dy), (cx + f, cy), (cx + f + 200, cy - dy * 200 / f)], d=1.0, largura=4)
    E.frase(c, t, C["s06.c"], ps("convergente:", "i", 56) + [("encontram no F'", "g", 56, COR)], XE, 220, passo=0.1)
    E.frase(c, t, C["s06.d"], ps("divergente:", "i", 56) + [("parecem vir do F", "g", 56, COR)], XE, 320, passo=0.1)
    if t >= C["s06.d"]:  # mini divergente
        x2, y2, f2 = 1500, 260, 170
        F.lente(c, t, C["s06.d"], x2, y2, 220, False, f2)
        for j, dy in enumerate((-60, 60)):
            Hh = (x2, y2 + dy)
            u = _u((x2 - f2, y2), Hh)
            F.raio(c, t, C["s06.d"] + 0.3 + 0.1 * j, [(x2 - 260, y2 + dy), Hh, (Hh[0] + u[0] * 230, Hh[1] + u[1] * 230)], d=1.0, largura=4)
            prolonga(c, t, C["s06.d"] + 1.2, Hh, (x2 - f2, y2))


# ---------------- raios notáveis ----------------
def b_raios(c, t, C, b):
    cx, cy, f = 1240, 560, 280
    F.lente(c, t, C["s07"] - 0.4, cx, cy, 500, True, f, eixo=(620, 1840))
    E.frase(c, t, C["s07"], ps("raios", "i", 70) + [("notáveis", "g", 70, COR)], XE, 220, passo=0.12)
    linhas = (("s07.a", "1", "paralelo → pelo F'"), ("s07.c", "2", "pelo centro → reto"), ("s08.a", "3", "pelo F → paralelo"))
    for i, (k, n, s) in enumerate(linhas):
        y = 380 + 110 * i
        E.foco(c, t, C[k], 0.4, lambda a, n=n, y=y: (E.bola(c, XE + 30, y - 20, 32, a=a), centro(c, n, XE + 30, y - 2, 40, "g", BR, a)))
        E.frase(c, t, C[k] + 0.1, [(s, "b", 46)], XE + 80, y)
    F.raio(c, t, C["s07.a"], [(680, cy - 200), (cx, cy - 200), (cx + f, cy), (cx + f + 260, cy + 200 * 260 / f)], d=1.2, largura=5)
    F.raio(c, t, C["s07.c"], [(760, cy - 170), (cx, cy), (cx + 560, cy + 170 * 560 / (cx - 760))], d=1.2, largura=5)
    P3 = (cx - f - 160, cy + 90)
    yh = cy + 90 - 90 * (f + 160) / 160
    F.raio(c, t, C["s08.a"], [P3, (cx, yh), (1840, yh)], d=1.2, largura=5)
    # divergente: o paralelo sai como se viesse do F
    if t >= C["s07.b"]:
        x2, y2, f2 = 560, 820, 170
        E.foco(c, t, C["s07.b"], 0.3, lambda a: E.escreve(c, "divergente:", XE, 690, 46, "i", TINTA2, a))
        F.lente(c, t, C["s07.b"], x2, y2, 220, False, f2, eixo=(XE, 900))
        Hh = (x2, y2 - 70)
        u = _u((x2 - f2, y2), Hh)
        F.raio(c, t, C["s07.b"] + 0.2, [(XE + 20, y2 - 70), Hh, (Hh[0] + u[0] * 300, Hh[1] + u[1] * 300)], d=1.0, largura=4)
        prolonga(c, t, C["s07.b"] + 1.0, Hh, (x2 - f2, y2))
    E.frase(c, t, C["s08.b"], [("dois raios", "g", 56)] + ps("bastam:", "i", 56), 1060, 960, passo=0.1)
    E.frase(c, t, C["s08.c"], ps("o cruzamento é a", "i", 56) + [("ponta da imagem", "g", 56, COR)], 1060, 1040, passo=0.1)


# ---------------- convergente: casos ----------------
def b_convergente(c, t, C, b):
    cy = 580
    if t < C["s10"]:
        def s09():
            E.frase(c, t, C["s09.a"], ps("objeto além de", "i", 60) + [("2F", "g", 60, COR)], XE, 200, passo=0.12)
            diagrama(c, t, 1240, cy, 230, 1240 - 600, 170, C["s09"] - 0.4, C["s09.a"], (C["s09.b"], C["s09.c"]), C["s09.d"], x0=560, x1=1840, dois_f=True)
            classifica(c, t, [(C["s09.e"], "real"), (C["s09.f"], "invertida"), (C["s09.g"], "menor")], XE, 960, 54)
            pilula_em(c, t, C["s09.h"], "câmera do celular", 1560, 960, 50, E.COR)
        E.saida(c, t, C["s10"] - 0.1, s09)
        return
    if t < C["s11"]:
        def s10():
            E.frase(c, t, C["s10.a"], ps("objeto entre", "i", 60) + [("F", "g", 60, COR), ("e a lente", "i", 60)], XE, 200, passo=0.12)
            diagrama(c, t, 1240, cy, 260, 1240 - 150, 110, C["s10"] - 0.4, C["s10.a"], (C["s10.b"], C["s10.b"] + 0.4), C["s10.c"] + 1.2, x0=560, x1=1840)
            classifica(c, t, [(C["s10.d"], "virtual"), (C["s10.e"], "direita"), (C["s10.f"], "maior")], XE, 960, 54)
            pilula_em(c, t, C["s10.g"], "lupa", 1560, 960, 56, E.COR)
        E.saida(c, t, C["s11"] - 0.1, s10)
        return
    E.frase(c, t, C["s11.a"], ps("o ponto", "i", 60) + [("2F", "g", 60, COR)] + ps("faz o papel do C", "i", 60), XE, 200, passo=0.12)
    diagrama(c, t, 900, cy, 230, 900 - 350, 110, C["s11"] - 0.4, C["s11.b"], (C["s11.b"] + 0.3, C["s11.b"] + 0.6), C["s11.b"] + 1.6, x0=300, x1=1840, dois_f=True)
    classifica(c, t, [(C["s11.b"] + 1.6, "real"), (C["s11.b"] + 1.9, "invertida"), (C["s11.b"] + 2.2, "maior")], XE, 960, 54)
    pilula_em(c, t, C["s11.c"], "projetor", 1600, 960, 56, E.COR)


# ---------------- divergente ----------------
def b_divergente(c, t, C, b):
    cy = 580
    E.frase(c, t, C["s12"], [("divergente", "g", 70, COR)], XE, 200)
    diagrama(c, t, 1240, cy, -260, 1240 - 450, 200, C["s12"], C["s12"] + 0.3, (C["s12.a"], C["s12.b"]), C["s12.c"] + 0.8, x0=560, x1=1840)
    E.frase(c, t, C["s12.c"], ps("só os", "i", 56) + [("prolongamentos", "g", 56)] + ps("se cruzam", "i", 56), XE, 820, passo=0.1)
    classifica(c, t, [(C["s12.d"], "virtual"), (C["s12.e"], "direita"), (C["s12.f"], "menor")], XE, 960, 54)
    pilula_em(c, t, C["s12.f"] + 0.5, "como o espelho convexo", 1560, 960, 44, TINTA)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s13"], [("cuidado", "g", 96, ERRADO)], XE, 200)
    E.frase(c, t, C["s13.a"], ps("o tipo da lente", "i", 64) + [("não decide", "g", 64, ERRADO)] + ps("a imagem", "i", 64), XE, 320, passo=0.12)
    E.frase(c, t, C["s13.b"], [("convergente:", "g", 56)] + ps("real ou virtual", "i", 60), XE, 430, passo=0.12)
    pilula_esq(c, t, C["s13.c"], "quem decide: o objeto em relação ao foco", XE, 540, 44, E.COR)
    cy = 820
    diagrama(c, t, 620, cy, 160, 520, 60, C["s13.d"], C["s13.d"], (C["s13.d"] + 0.2, C["s13.d"] + 0.4), C["s13.d"] + 1.4, x0=240, x1=920, h=260)
    diagrama(c, t, 1460, cy, 160, 1060, 120, C["s13.d"] + 1.2, C["s13.d"] + 1.2, (C["s13.d"] + 1.4, C["s13.d"] + 1.6), C["s13.d"] + 2.6, x0=1000, x1=1840, h=260)


# ---------------- atalho (palco) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    if t < C["s15"]:
        E.frase(c, t, C["s14"], ps("o atalho da", "i", 70, CLARO) + [("forma", "g", 70, BR)], W / 2, 160, "center", 0.12)
        E.frase(c, t, C["s14.a"], ps("olhe a", "i", 60, CLARO) + [("última palavra", "g", 60, BR)], W / 2, 260, "center", 0.12)
        for lin, (ks, nomes, tipo) in enumerate(((("s14.b", "s14.c"), ("biconvexa", "plano-convexa", "côncavo-convexa"), "convergente"),
                                                  (("s14.d", "s14.e"), ("bicôncava", "plano-côncava", "convexo-côncava"), "divergente"))):
            y = 470 + 330 * lin
            for k, nome in enumerate(nomes):
                x = 330 + 360 * k
                chave = nome.replace("-", "_").replace("ô", "o")
                E.foco(c, t, C[ks[0]] + 0.3 * k, 0.4, lambda a, x=x, chave=chave, y=y: perfil(c, x, y, 170, *PERFIS[chave], a=a, escuro=True))
                E.foco(c, t, C[ks[0]] + 0.3 * k + 0.2, 0.4, lambda a, x=x, nome=nome, y=y: centro(c, nome, x, y + 140, 40, "b", CLARO, a))
            E.foco(c, t, C[ks[1]], 0.4, lambda a, y=y, tipo=tipo: E.pilula(c, tipo, 1600, y, 56, "g", fundo=E.COR, a=a))
        return
    E.frase(c, t, C["s15.a"], ps("a última palavra é a face", "i", 60, CLARO) + [("mais curva", "g", 60, BR)], W / 2, 240, "center", 0.12)
    E.foco(c, t, C["s15.a"] + 0.5, 0.5, lambda a: perfil(c, W / 2, 470, 260, *PERFIS["concavo_convexa"], a=a, escuro=True))
    E.foco(c, t, C["s15.a"] + 0.9, 0.4, lambda a: centro(c, "convexa manda: meio grosso", W / 2, 680, 48, "b", CLARO, a))
    E.frase(c, t, C["s15.b"], ps("só vale com a lente num meio de", "i", 54, CLARO) + [("índice menor", "g", 54, BR)], W / 2, 800, "center", 0.1)
    E.linha(c, t, [("imagem, com uma lente só:", "i", 56, CLARO, C["s15.c"]), ("real = invertida, virtual = direita", "g", 52, BR, C["s15.d"])], W / 2, 950, "center")


# ---------------- questão ----------------
def slide(c, cx, cy, s, a=1.0, invertido=False):
    if a <= 0:
        return
    M.rrect(c, cx - s * 0.6, cy - s * 0.6, s * 1.2, s * 1.2, 10, BR, a)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - s * 0.6, cy - s * 0.6, s * 1.2, s * 1.2), 10, 10), M.paint(TINTA, a, stroke=4))
    c.save(); c.translate(cx, cy)
    if invertido:
        c.rotate(180)
    E.centro(c, "A", 0, s * 0.35, s, "g", E.COR, a)
    c.restore()


def b_questao(c, t, C, b):
    E.frase(c, t, C["s16"], ps("hora de testar:", "i", 72, COR) + [("projetor", "g", 72)], XE, 190, passo=0.12)
    E.frase(c, t, C["s16.a"], ps("slide entre", "i", 62) + [("F", "g", 62, COR), ("e", "i", 62), ("2F", "g", 62, COR)], XE, 340, passo=0.12)
    E.frase(c, t, C["s16.b"], ps("como é a", "i", 70) + [("imagem na tela?", "g", 66, COR)], XE, 500, passo=0.12)
    E.frase(c, t, C["s16.c"], ps("como pôr o slide para sair", "i", 58) + [("de pé?", "g", 58, COR)], XE, 640, passo=0.1)
    if t < C["s17"]:
        cx, cy, f = 1500, 640, 160
        F.lente(c, t, C["s16.a"], cx, cy, 300, True, f, eixo=(1080, 1840))
        eixo_pontos(c, t, C["s16.a"] + 0.4, cy, [(cx - 2 * f, "2F")])
        objeto_o(c, t, C["s16.a"] + 0.6, cx - 240, cy, 80)
    questao_relogio(c, t, C, "s17")


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    cy = 520
    diagrama(c, t, 900, cy, 230, 900 - 350, 110, C["s18"], C["s18"] + 0.2, (C["s18"] + 0.4, C["s18"] + 0.7), C["s18.a"] + 0.6, x0=300, x1=1840, dois_f=True)
    classifica(c, t, [(C["s18.b"], "real"), (C["s18.c"], "invertida"), (C["s18.d"], "maior")], XE, 880, 54)
    E.frase(c, t, C["s18.e"], ps("só imagem", "i", 54) + [("real", "g", 54, F.VEL)] + ps("aparece numa tela", "i", 54), XE, 1000, passo=0.1)
    E.foco(c, t, C["s18.f"], 0.5, lambda a: slide(c, 1500, 900, 110, a, invertido=True))
    E.foco(c, t, C["s18.f"] + 0.3, 0.4, lambda a: E.escreve(c, "slide de cabeça para baixo", 1240, 1040, 44, "b", TINTA, a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def r():
        resumo(c, t, C, "s19", [("s19.a", [("bordas finas:", "g"), ("convergente;", "i"), ("grossas:", "g"), ("divergente", "i")]),
                                ("s19.b", [("dois raios notáveis", "g"), ("acham a imagem", "i")]),
                                ("s19.c", [("divergente:", "g"), ("virtual, direita, menor", "i", 62, COR)])], y0=380, dy=200)
    E.saida(c, t, C["s20"] - 0.1, r)
    if t < C["s20"]:
        return

    def desenho():
        E.formula_em(c, t, C["s20.a"] + 0.5, "f{1}{f} = f{1}{p} + f{1}{p'}", XE, 800, 100, "g", TINTA)
        E.formula_em(c, t, C["s20.b"] + 0.3, "V = f{1}{f}", XE + 720, 800, 100, "g", COR)
    proxima(c, t, C, "s20", [("a conta", "i", 100), ("da lente", "g", 100, COR)], [("e o", "i", 80), ("grau dos óculos", "g", 80)], desenho)


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, tipos=b_tipos, raios=b_raios, convergente=b_convergente, divergente=b_divergente,
              erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
