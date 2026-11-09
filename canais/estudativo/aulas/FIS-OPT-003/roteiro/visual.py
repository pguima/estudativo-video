"""Visual — Estudativo · FIS-OPT-003: espelhos esféricos, côncavo e convexo.
Segue a linguagem visual da trilha Óptica, escrita no cabeçalho do visual.py da FIS-OPT-001 (raio laranja, prolongamento
tracejado cinza, objeto em tinta, imagem petróleo, espelho em tinta com hachura atrás, F laranja e C/V em tinta no eixo).
Os raios dos diagramas são calculados (raios_espelho), e a imagem cai onde a equação dos espelhos manda.
Todo instante vem de C[...] (marcadores do roteiro)."""
import math

import editorial as E
import fisica as F
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Física", "Óptica")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_FIS-OPT-003_espelhos_esfericos_concavo_convexo.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("tipos", "raios", "concavo", "convexo", "atalho", "questao", "fim"))


def _g(f, p):
    return f * p / (p - f)


# os desenhos seguem a equação dos espelhos (a aula só usa o tipo de imagem; a conta é da FIS-OPT-011)
assert _g(230, 640) > 0 and abs(_g(230, 640) / 640) < 1          # além de C (R = 460): real, invertida, menor
assert _g(230, 140) < 0 and abs(_g(230, 140) / 140) > 1          # entre F e V: virtual, direita, maior
assert _g(230, 350) > 0 and abs(_g(230, 350) / 350) > 1          # entre C e F: real, invertida, maior
assert _g(230, 460) == 460                                       # no C: imagem no C, mesmo tamanho
assert _g(-230, 400) < 0 and abs(_g(-230, 400) / 400) < 1        # convexo: virtual, direita, menor
assert 460 / 2 == 230                                            # f = R / 2


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
def eixo(c, t, t0, x0, x1, cy, escuro=False):
    if t >= t0:
        M.line(c, x0, cy, x1, cy, BR if escuro else TINTA, 0.5, 3, dash=E.TRACO, progress=ease_io(prog(t, t0, 0.6)))


def diagrama(c, t, vx, cy, f, xo, ho, concavo, t_esp, t_obj, ts, t_img, tipos=("par", "foco"), x0=None, x1=None, pontos=True):
    """espelho, eixo, F/C/V, objeto, raios e imagem; devolve (xi, hi)"""
    R = 2 * f
    eixo(c, t, t_esp, x0 if x0 is not None else vx - 1.6 * R, x1 if x1 is not None else vx + 300, cy)
    espelho_curvo(c, t, t_esp, vx, cy, R, min(320, R * 0.75), concavo)
    if pontos:
        Fx, Cx = (vx - f, vx - R) if concavo else (vx + f, vx + R)
        eixo_pontos(c, t, t_esp + 0.3, cy, [(Fx, "F"), (Cx, "C"), (vx, "V")])
    objeto_o(c, t, t_obj, xo, cy, ho)
    xi, hi = raios_espelho(c, t, ts, vx, cy, f, xo, ho, concavo, tipos)
    imagem_i(c, t, t_img, xi, cy, hi, real=concavo and xi < vx)
    return xi, hi


def colher(c, cx, cy, a=1.0):
    """colher vista de frente, com um rosto pequeno de cabeça para baixo"""
    if a <= 0:
        return
    M.rrect(c, cx - 22, cy + 150, 44, 330, 22, "#A9A9B3", a)
    p = skia.Paint(AntiAlias=True)
    p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx - 30, cy - 40), 230, [M.hexc("#F2F2F5", a), M.hexc("#9A9AA6", a)], [0, 1]))
    c.drawOval(skia.Rect.MakeXYWH(cx - 130, cy - 190, 260, 360), p)
    c.drawOval(skia.Rect.MakeXYWH(cx - 130, cy - 190, 260, 360), M.paint(TINTA2, a, stroke=4))
    # rosto invertido: boca em cima, olhos embaixo
    c.drawCircle(cx, cy, 52, M.paint("#F1C9A5", a))
    c.drawCircle(cx - 18, cy + 14, 6, M.paint(TINTA, a)); c.drawCircle(cx + 18, cy + 14, 6, M.paint(TINTA, a))
    c.drawArc(skia.Rect.MakeXYWH(cx - 20, cy - 34, 40, 30), 180, 180, False, M.paint(TINTA, a, stroke=4))
    c.drawArc(skia.Rect.MakeXYWH(cx - 56, cy - 56, 112, 112), 20, 140, False, M.paint("#5B3A29", a, stroke=14))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def um():
        cy = 640
        # côncavo de maquiagem: objeto dentro do foco → imagem virtual, maior
        E.frase(c, t, C["s01.a"], ps("maquiagem:", "i", 64) + [("aumenta", "g", 64, COR)], XE, 220, passo=0.12)
        diagrama(c, t, 560, cy, 200, 440, 110, True, C["s01.a"], C["s01.a"] + 0.3, (C["s01.a"] + 0.6, C["s01.a"] + 1.0), C["s01.a"] + 2.0,
                 ("par", "centro"), x0=200, x1=900, pontos=False)
        E.frase(c, t, C["s01.b"], ps("garagem:", "i", 64) + [("tudo pequeno", "g", 64, COR)], 1060, 220, passo=0.12)
        diagrama(c, t, 1500, cy, 200, 1180, 200, False, C["s01.b"], C["s01.b"] + 0.3, (C["s01.b"] + 0.6, C["s01.b"] + 1.0), C["s01.b"] + 2.0,
                 ("par", "centro"), x0=1050, x1=1820, pontos=False)
        E.frase(c, t, C["s01.c"], ps("pedaços de uma", "i", 60) + [("esfera", "g", 60, COR)], XE, 980, passo=0.12)
        E.frase(c, t, C["s01.d"], ps("muda o lado que", "i", 60) + [("brilha", "g", 60, COR)], 1060, 980, passo=0.12)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t >= C["s02"]:
        promessa(c, t, C, "s02", [("s02.b", "espelho côncavo"), ("s02.c", "espelho convexo"), ("s02.d", "só com dois raios")])


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    def lei(a, x, y):
        M.line(c, x - 140, y + 60, x + 140, y + 60, TINTA, a, 5)
        M.line(c, x, y + 60, x, y - 80, TINTA2, a, 3, dash=E.TRACO)
        M.line(c, x - 110, y - 60, x, y + 60, E.COR, a, 5); M.line(c, x, y + 60, x + 110, y - 60, E.COR, a, 5)

    def virt(a, x, y):
        M.line(c, x - 60, y + 60, x - 60, y - 70, TINTA, a, 5)
        M.line(c, x - 60, y - 70, x - 160, y + 20, E.COR, a, 5)
        M.line(c, x - 60, y - 70, x + 110, y + 50, TINTA2, a, 4, dash=[12, 9])
        c.drawCircle(x + 110, y + 50, 12, M.paint(F.VEL, a))
    lembrete(c, t, C, "s03", [("s03.b", "lei da reflexão:", "r = i, medidos da normal"), ("s03.c", "imagem virtual:", "pelos prolongamentos")], (lei, virt))


# ---------------- côncavo e convexo ----------------
def b_tipos(c, t, C, b):
    O, R = (560, 620), 290
    if t < C["s05"]:
        q = ep(t, C["s04.a"], 0.5)
        if q > 0:
            p = skia.Paint(AntiAlias=True)
            p.setShader(skia.GradientShader.MakeRadial(skia.Point(O[0] - 80, O[1] - 90), R * 1.3, [M.hexc("#FFFFFF", q), M.hexc("#B9C3CC", q)], [0, 1]))
            c.drawCircle(*O, R, p)
            c.drawCircle(*O, R, M.paint(TINTA, q, stroke=5))
            E.frase(c, t, C["s04.a"], ps("bola espelhada", "i", 60), O[0], O[1] + R + 110, "center", 0.12)
        if t >= C["s04.b"]:
            c.drawArc(skia.Rect.MakeXYWH(O[0] - R, O[1] - R, 2 * R, 2 * R), -32, 64 * ease_io(prog(t, C["s04.b"], 0.6)), False, M.paint(E.COR, 1.0, stroke=14))
            E.foco(c, t, C["s04.b"] + 0.4, 0.4, lambda a: E.escreve(c, "uma tampinha", O[0] + 60, O[1] - R - 30, 50, "i", COR, a))
        # côncavo e convexo, cada um com o lado que reflete virado para a luz
        if t >= C["s04.c"]:
            espelho_curvo(c, t, C["s04.c"], 1420, 450, 260, 170, True)
            E.frase(c, t, C["s04.c"] + 0.3, [("côncavo", "g", 70, COR)], 1180, 360, "right")
            E.foco(c, t, C["s04.c"] + 0.5, 0.4, lambda a: E.escreve(c, "brilha por dentro", 1460, 470, 46, "i", TINTA2, a))
        E.frase(c, t, C["s04.d"], [("côncavo", "g", 56), ("=", "g", 56, TINTA2), ("caverna", "g", 56, COR)], 1420, 650, "center", 0.12)
        if t >= C["s04.e"]:
            espelho_curvo(c, t, C["s04.e"], 1300, 860, 260, 150, False)
            E.frase(c, t, C["s04.e"] + 0.3, [("convexo", "g", 70, COR)], 1180, 880, "right")
            E.foco(c, t, C["s04.e"] + 0.5, 0.4, lambda a: E.escreve(c, "brilha por fora", 1420, 880, 46, "i", TINTA2, a))
        return
    # s05: os pontos do espelho
    vx, cy, Rr = 1560, 640, 640
    eixo(c, t, C["s05.c"], 180, 1800, cy)
    espelho_curvo(c, t, C["s05"] - 0.4, vx, cy, Rr, 330, True)
    eixo_pontos(c, t, C["s05.a"], cy, [(vx - Rr, "C")])
    eixo_pontos(c, t, C["s05.b"], cy, [(vx, "V")])
    eixo_pontos(c, t, C["s05.d"], cy, [(vx - Rr / 2, "F")])
    E.foco(c, t, C["s05.a"], 0.4, lambda a: E.escreve(c, "centro de curvatura", vx - Rr - 150, cy - 40, 44, "i", TINTA2, a))
    E.foco(c, t, C["s05.b"], 0.4, lambda a: E.escreve(c, "vértice", vx + 40, cy - 40, 44, "i", TINTA2, a))
    E.foco(c, t, C["s05.c"] + 0.3, 0.4, lambda a: E.escreve(c, "eixo principal", 220, cy - 30, 44, "i", TINTA2, a))
    E.foco(c, t, C["s05.d"], 0.4, lambda a: E.escreve(c, "foco", vx - Rr / 2 - 40, cy - 40, 44, "i", COR, a))
    E.segmento(c, t, C["s05.e"], (vx - Rr, cy + 150), (vx, cy + 150), "R", cor=TINTA2, largura=4, lado=-1, size=52)
    E.segmento(c, t, C["s05.e"] + 0.6, (vx - Rr / 2, cy + 250), (vx, cy + 250), "f", cor=E.COR, largura=5, lado=-1, size=56)
    E.foco(c, t, C["s05.e"] + 1.0, 0.5, lambda a: E.formula(c, "f = f{R}{2}", XE, 300, 110, "g", COR, a))
    E.frase(c, t, C["s05.e"] + 1.2, ps("metade do raio de curvatura", "i", 54, TINTA2), XE, 430, passo=0.1)


# ---------------- raios notáveis ----------------
def _raio_par(c, t, t0, vx, cy, f, y, comp=260, d=1.2, x0=None):
    R = 2 * f
    P = (x0 if x0 is not None else vx - 1050, y)
    Hh = _bate_circ(P, (1.0, 0.0), vx - R, cy, R, True)
    u = _u(Hh, (vx - f, cy))
    F.raio(c, t, t0, [P, Hh, (vx - f + u[0] * comp, cy + u[1] * comp)], d=d, largura=5)


def b_raios(c, t, C, b):
    vx, cy, f = 1640, 600, 330
    R = 2 * f
    if t < C["s07"]:
        eixo(c, t, C["s06"] - 0.5, 300, 1800, cy)
        espelho_curvo(c, t, C["s06"] - 0.5, vx, cy, R, 330, True)
        eixo_pontos(c, t, C["s06"] - 0.3, cy, [(vx - f, "F"), (vx - R, "C")])
        E.frase(c, t, C["s06"], ps("por que", "i", 70) + [("foco?", "g", 70, COR)], XE, 220, passo=0.12)
        for i, y in enumerate((cy - 250, cy - 150, cy + 150, cy + 250)):
            _raio_par(c, t, C["s06.a"] + 0.2 * i, vx, cy, f, y)
        E.frase(c, t, C["s06.b"], ps("todos passam pelo", "i", 60) + [("foco", "g", 60, COR)], XE, 330, passo=0.1)
        pilula_esq(c, t, C["s06.c"], "forno solar", XE, 960, 52, E.COR)
        E.foco(c, t, C["s06.c"] + 0.5, 0.4, lambda a: (M.rrect(c, vx - f - 70, cy - 50, 140, 60, 12, TINTA, a), M.rrect(c, vx - f - 90, cy - 62, 180, 16, 8, TINTA, a)))
        return
    # s07–s08: os três raios notáveis
    eixo(c, t, C["s07"] - 0.5, 700, 1800, cy)
    espelho_curvo(c, t, C["s07"] - 0.5, vx, cy, R, 330, True)
    eixo_pontos(c, t, C["s07"] - 0.3, cy, [(vx - f, "F"), (vx - R, "C")])
    E.frase(c, t, C["s07.a"], ps("raios", "i", 70) + [("notáveis", "g", 70, COR)], XE, 220, passo=0.12)
    linhas = (("s07.b", "1", "paralelo → pelo F"), ("s07.c", "2", "pelo F → paralelo"), ("s07.d", "3", "pelo C → volta igual"))
    for i, (k, n, s) in enumerate(linhas):
        y = 380 + 120 * i
        E.foco(c, t, C[k], 0.4, lambda a, n=n, y=y: (E.bola(c, XE + 30, y - 20, 32, a=a), centro(c, n, XE + 30, y - 2, 40, "g", BR, a)))
        E.frase(c, t, C[k] + 0.1, [(s, "b", 46)], XE + 80, y)
    # 1: paralelo
    _raio_par(c, t, C["s07.b"], vx, cy, f, cy - 230, comp=330, x0=760)
    # 2: pelo foco → paralelo (de baixo)
    P2 = (vx - f - 300, cy - 200)
    d2 = _u(P2, (vx - f, cy))
    H2 = _bate_circ(P2, d2, vx - R, cy, R, True)
    F.raio(c, t, C["s07.c"], [P2, H2, (vx - 900, H2[1])], d=1.4, largura=5)
    # 3: pelo centro → volta
    P3 = (vx - R - 200, cy - 120)
    d3 = _u(P3, (vx - R, cy))
    H3 = _bate_circ(P3, d3, vx - R, cy, R, True)
    F.raio(c, t, C["s07.d"], [P3, H3], d=0.9, largura=5)
    F.raio(c, t, C["s07.d"] + 0.9, [H3, P3], d=0.9, largura=5, setas=True)
    E.foco(c, t, C["s07.d"] + 1.6, 0.4, lambda a: E.escreve(c, "normal", H3[0] - 160, H3[1] + 60, 40, "i", TINTA2, a))
    E.frase(c, t, C["s08.a"], [("bastam", "i", 64), ("dois", "g", 64, COR)], XE, 820, passo=0.12)
    E.frase(c, t, C["s08.b"], ps("o cruzamento é a", "i", 56) + [("ponta da imagem", "g", 56, COR)], XE, 920, passo=0.1)


# ---------------- côncavo: os casos ----------------
def b_concavo(c, t, C, b):
    cy = 600
    if t < C["s10"]:
        def s09():
            E.frase(c, t, C["s09.a"], ps("objeto além do", "i", 64) + [("C", "g", 64, COR)], XE, 200, passo=0.12)
            diagrama(c, t, 1640, cy, 230, 1000, 170, True, C["s09"] - 0.4, C["s09.a"], (C["s09.b"], C["s09.c"]), C["s09.d"], ("par", "foco"), x0=700)
            classifica(c, t, [(C["s09.e"], "real"), (C["s09.f"], "invertida"), (C["s09.g"], "menor")], XE, 960, 54)
        E.saida(c, t, C["s10"] - 0.1, s09)
        return
    if t < C["s11"]:
        def s10():
            E.frase(c, t, C["s10.a"], ps("objeto entre", "i", 64) + [("F", "g", 64, COR), ("e", "i", 64), ("espelho", "g", 64, COR)], XE, 200, passo=0.12)
            diagrama(c, t, 1300, cy, 230, 1160, 110, True, C["s10"] - 0.4, C["s10.a"], (C["s10.b"], C["s10.b"] + 0.5), C["s10.c"] + 1.2, ("par", "foco"), x0=500, x1=1800)
            classifica(c, t, [(C["s10.d"], "virtual"), (C["s10.e"], "direita"), (C["s10.f"], "maior")], XE, 960, 54)
            pilula_em(c, t, C["s10.g"], "maquiagem", 1640, 230, 50, E.COR)
        E.saida(c, t, C["s11"] - 0.1, s10)
        return
    # s11: os outros casos, no mapa do eixo
    mapa(c, t, C["s11"], 900, [C["s11.a"], C["s11.b"], C["s11.c"]], ("C", "CF", "F"))
    E.frase(c, t, C["s11"], ps("os outros", "i", 70) + [("casos", "g", 70, COR)], XE, 220, passo=0.12)
    linhas = (("s11.a", "no C:", "real, invertida, igual"), ("s11.b", "entre C e F:", "real, invertida, maior"), ("s11.c", "no F:", "sem imagem nítida"))
    for i, (k, l1, l2) in enumerate(linhas):
        y = 380 + 130 * i
        E.frase(c, t, C[k], [(l1, "g", 60), (l2, "i", 62, TINTA2)], XE, y, passo=0.12)


def mapa(c, t, t0, y, ts, quais, escuro=False, x0=260, x1=1720):
    """eixo com C, F e V e as regiões do côncavo acendendo"""
    tinta, tinta2 = (BR, CLARO) if escuro else (TINTA, TINTA2)
    xC, xF, xV = 860, 1300, 1640
    q = ep(t, t0, 0.5)
    if q <= 0:
        return xC, xF, xV
    M.line(c, x0, y, xV, y, tinta, q, 4)
    M.line(c, xV, y - 90, xV, y + 90, tinta, q, 8)
    for x, s in ((xC, "C"), (xF, "F"), (xV, "V")):
        c.drawCircle(x, y, 12, M.paint(E.COR if s == "F" else tinta, q))
        E._meio(c, s, x, y + 54, 48, "b", tinta, q)
    regioes = dict(C=(xC - 6, xC + 6), CF=(xC, xF), F=(xF - 6, xF + 6), FV=(xF, xV), alem=(x0, xC))
    for k, ti in zip(quais, ts):
        a = ep(t, ti, 0.4)
        if a > 0:
            x_a, x_b = regioes[k]
            M.rrect(c, x_a, y - 24, x_b - x_a, 48, 12, E.COR, 0.35 * a)
    return xC, xF, xV


# ---------------- convexo ----------------
def b_convexo(c, t, C, b):
    cy, vx, f = 600, 1150, 230
    if t < C["s13"]:
        eixo(c, t, C["s12"] - 0.4, 300, 1800, cy)
        espelho_curvo(c, t, C["s12"] - 0.4, vx, cy, 2 * f, 340, False)
        eixo_pontos(c, t, C["s12.a"], cy, [(vx + f, "F"), (vx + 2 * f, "C"), (vx, "V")])
        E.frase(c, t, C["s12.a"], ps("no convexo, o foco fica", "i", 60) + [("atrás", "g", 60, COR)], XE, 200, passo=0.1)
        P = (vx - 650, cy - 200)
        Hh = _bate_circ(P, (1.0, 0.0), vx + 2 * f, cy, 2 * f, False)
        u = _u((vx + f, cy), Hh)
        F.raio(c, t, C["s12.b"], [P, Hh, (Hh[0] + u[0] * 520, Hh[1] + u[1] * 520)], d=1.3)
        prolonga(c, t, C["s12.c"], Hh, (vx + f, cy))
        P2 = (vx - 650, cy - 330)
        d2 = _u(P2, (vx + 2 * f, cy))
        H2 = _bate_circ(P2, d2, vx + 2 * f, cy, 2 * f, False)
        F.raio(c, t, C["s12.d"], [P2, H2], d=0.8)
        F.raio(c, t, C["s12.d"] + 0.8, [H2, P2], d=0.8)
        prolonga(c, t, C["s12.d"] + 0.8, H2, (vx + 2 * f, cy))
        E.frase(c, t, C["s12.c"], ps("o", "i", 54, TINTA2) + [("prolongamento", "g", 54)] + ps("passa por F", "i", 54, TINTA2), XE, 960, passo=0.1)
        return
    E.frase(c, t, C["s13.a"], ps("os raios sempre se", "i", 60) + [("abrem", "g", 60, COR)], XE, 200, passo=0.1)
    diagrama(c, t, vx, cy, f, 700, 200, False, C["s13"] - 0.6, C["s13"] - 0.4, (C["s13"] - 0.2, C["s13.a"]), C["s13.a"] + 1.3, ("par", "centro"), x0=300, x1=1800)
    classifica(c, t, [(C["s13.b"], "virtual"), (C["s13.c"], "direita"), (C["s13.d"], "menor")], XE, 960, 54)
    pilula_em(c, t, C["s13.e"], "retrovisor · garagem", 1560, 220, 48, E.COR)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s14"], [("cuidado", "g", 96, ERRADO)], XE, 200)
    E.frase(c, t, C["s14.a"], ps("o côncavo", "i", 68) + [("sempre aumenta?", "g", 64, ERRADO)], XE, 330, passo=0.12)
    E.foco(c, t, C["s14.b"], 0.6, lambda a: colher(c, 1460, 470, a))
    E.foco(c, t, C["s14.b"] + 0.4, 0.4, lambda a: centro(c, "dentro da colher", 1460, 1010, 46, "i", TINTA2, a))
    E.frase(c, t, C["s14.c"], ps("você aparece", "i", 60) + [("pequeno e de cabeça para baixo", "g", 50, COR)], XE, 470, passo=0.1)
    E.frase(c, t, C["s14.d"], ps("objeto longe, além do C:", "i", 56), XE, 620, passo=0.1)
    classifica(c, t, [(C["s14.d"] + 0.8, "real"), (C["s14.d"] + 1.1, "invertida"), (C["s14.d"] + 1.4, "menor")], XE, 720, 48)
    pilula_esq(c, t, C["s14.e"], "quem decide é a posição do objeto", XE, 880, 46, E.COR)


# ---------------- atalho (palco) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    y = 640
    if t < C["s16"]:
        E.frase(c, t, C["s15"], ps("o atalho do", "i", 72, CLARO) + [("côncavo", "g", 72, BR)], W / 2, 170, "center", 0.12)
        xC, xF, xV = mapa(c, t, C["s15"], y, [], (), escuro=True)
        # F: fronteira da natureza
        if t >= C["s15.a"]:
            M.line(c, xF, y - 260, xF, y - 24, E.COR, ep(t, C["s15.a"], 0.4), 6)
            E.foco(c, t, C["s15.a"], 0.4, lambda a: centro(c, "natureza", xF, y - 280, 48, "g", CLARO, a))
        E.foco(c, t, C["s15.b"], 0.5, lambda a: centro(c, "real e invertida", (260 + xF) / 2, y - 120, 52, "g", BR, a))
        E.foco(c, t, C["s15.c"], 0.5, lambda a: (centro(c, "virtual, direita", (xF + xV) / 2, y - 160, 44, "g", BR, a),
                                                 centro(c, "e maior", (xF + xV) / 2, y - 105, 44, "g", BR, a)))
        if t >= C["s15.d"]:
            M.line(c, xC, y + 100, xC, y + 260, CLARO, ep(t, C["s15.d"], 0.4), 6)
            E.foco(c, t, C["s15.d"], 0.4, lambda a: centro(c, "tamanho", xC, y + 300, 48, "g", CLARO, a))
        E.foco(c, t, C["s15.e"], 0.5, lambda a: centro(c, "menor", (260 + xC) / 2, y + 160, 56, "g", BR, a))
        E.foco(c, t, C["s15.f"], 0.5, lambda a: centro(c, "maior", (xC + xF) / 2, y + 160, 56, "g", BR, a))
        return
    E.frase(c, t, C["s16"], ps("num espelho só:", "i", 70, CLARO), W / 2, 220, "center")
    E.foco(c, t, C["s16.a"], 0.5, lambda a: (E.pilula(c, "real", 700, 400, 70, "g", fundo=E.COR, a=a), centro(c, "↔", 960, 425, 80, "g", CLARO, a),
                                             E.pilula(c, "invertida", 1240, 400, 70, "g", fundo=E.COR, a=a)))
    E.foco(c, t, C["s16.b"], 0.5, lambda a: (E.pilula(c, "virtual", 700, 580, 70, "g", fundo=F.VEL, a=a), centro(c, "↔", 960, 605, 80, "g", CLARO, a),
                                             E.pilula(c, "direita", 1240, 580, 70, "g", fundo=F.VEL, a=a)))
    E.frase(c, t, lerp(C["s16.b"], C["s16.c"], 0.4), ps("os raios cruzados trocam", "i", 54, CLARO) + [("cima e baixo", "g", 54, BR)], W / 2, 740, "center", 0.1)
    E.frase(c, t, C["s16.c"], [("convexo:", "g", 66, BR)] + ps("virtual, direita e menor", "i", 70, CLARO), W / 2, 920, "center", 0.12)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s17"], ps("hora de testar", "i", 72, COR), XE, 190)
    E.frase(c, t, C["s17.a"], ps("objeto entre", "i", 66) + [("C", "g", 66, COR), ("e", "i", 66), ("F", "g", 66, COR)], XE, 340, passo=0.12)
    E.frase(c, t, C["s17.a"] + 0.6, ps("de um côncavo", "i", 66), XE, 440, passo=0.12)
    E.frase(c, t, C["s17.b"], [("como", "i", 76), ("é a imagem?", "g", 72, COR)], XE, 600, passo=0.12)
    E.frase(c, t, C["s17.c"], ps("e se fosse", "i", 66) + [("convexo?", "g", 66, COR)], XE, 740, passo=0.12)
    if t < C["s18"]:
        cy, vx, f = 640, 1680, 200
        eixo(c, t, C["s17.a"], 1000, 1800, cy)
        espelho_curvo(c, t, C["s17.a"], vx, cy, 2 * f, 260, True)
        eixo_pontos(c, t, C["s17.a"] + 0.3, cy, [(vx - f, "F"), (vx - 2 * f, "C")])
        objeto_o(c, t, C["s17.a"] + 0.6, vx - 300, cy, 120)
    questao_relogio(c, t, C, "s18")


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    cy = 560
    diagrama(c, t, 1680, cy, 230, 1680 - 350, 120, True, C["s19"], C["s19"] + 0.2, (C["s19.a"], C["s19.a"] + 0.5), C["s19.b"], ("par", "foco"), x0=900, x1=1800)
    E.frase(c, t, C["s19.a"], ps("mais longe que o", "i", 56) + [("F", "g", 56, COR)], XE, 220, passo=0.1)
    classifica(c, t, [(C["s19.b"], "real"), (C["s19.b"] + 0.4, "invertida")], XE, 320, 50)
    E.frase(c, t, C["s19.c"], ps("mais perto que o", "i", 56) + [("C", "g", 56, COR)], XE, 470, passo=0.1)
    classifica(c, t, [(C["s19.d"], "maior")], XE, 570, 50)
    E.frase(c, t, C["s19.e"], [("convexo:", "g", 60)] + ps("virtual, direita, menor", "i", 62, TINTA2), XE, 980, passo=0.12)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def r():
        resumo(c, t, C, "s20", [("s20.a", [("F", "g", 62, COR), ("no meio entre", "i"), ("C", "g"), ("e", "i"), ("V:", "g"), ("f = R ÷ 2", "g", 62, COR)]),
                                ("s20.b", [("dois raios notáveis", "g"), ("acham a imagem", "i")]),
                                ("s20.c", [("convexo:", "g"), ("virtual, direita, menor", "i")])], y0=380, dy=200)
    E.saida(c, t, C["s21"] - 0.1, r)
    if t < C["s21"]:
        return

    def desenho():
        E.formula_em(c, t, C["s21.b"] + 0.4, "f{1}{f} = f{1}{p} + f{1}{p'}", XE, 800, 110, "g", TINTA)
    proxima(c, t, C, "s21", [("onde", "g", 96, COR), ("fica a imagem", "i", 96)], [("e quantas vezes", "i", 80), ("maior", "g", 80, COR)], desenho)


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, tipos=b_tipos, raios=b_raios, concavo=b_concavo, convexo=b_convexo,
              erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
