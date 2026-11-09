"""Visual — Estudativo · FIS-OPT-009: lupa, câmera, microscópio e luneta.
Segue a linguagem visual da trilha Óptica, escrita no cabeçalho do visual.py da FIS-OPT-001 (raio laranja, prolongamento
tracejado cinza, objeto em tinta, imagem petróleo: cheia se real, tracejada se virtual). Nos instrumentos de duas lentes, a
imagem real do meio (petróleo cheia) vira o objeto da ocular; a final sai tracejada. Os raios são calculados (raios_lente)
com a equação das lentes, então cada imagem cai onde a conta manda.
Todo instante vem de C[...] (marcadores do roteiro)."""
import math

import editorial as E
import fisica as F
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Física", "Óptica")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_FIS-OPT-009_lupa_camera_microscopio_luneta.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("simples", "duas", "micro", "luneta", "atalho", "questao", "fim"))


def _g(f, p):
    return f * p / (p - f)


# todas as contas da aula
assert 40 * 10 == 400 and 100 / 2 == 50 and 40 * 15 == 600
# os desenhos seguem a equação das lentes
assert 1220 - (520 + _g(120, 160)) == 220 and _g(120, 160) == 480 and -480 / 160 == -3                      # objetiva do microscópio: real, invertida, 3×
assert _g(400, 220) < 0 and abs(_g(400, 220) / 220) > 1             # ocular: lupa (virtual, maior)
assert _g(200, 150) == -600 and 600 / 150 == 4                       # ocular da luneta: virtual, 4×
assert _g(240, 120) < 0 and _g(240, 900) > 0 and abs(_g(240, 900) / 900) < 1   # lupa e câmera


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
def lua(c, cx, cy, r, a=1.0):
    if a <= 0:
        return
    E.bola(c, cx, cy, r, "#C9C9D2", a)
    for dx, dy, k in ((-0.3, -0.2, 0.18), (0.25, 0.15, 0.12), (-0.05, 0.4, 0.1)):
        c.drawCircle(cx + dx * r, cy + dy * r, k * r, M.paint("#8C8C99", 0.5 * a))


def celula(c, cx, cy, r, a=1.0):
    if a <= 0:
        return
    c.drawOval(skia.Rect.MakeXYWH(cx - r * 1.3, cy - r, r * 2.6, r * 2), M.paint("#B6E3B0", 0.8 * a))
    c.drawOval(skia.Rect.MakeXYWH(cx - r * 1.3, cy - r, r * 2.6, r * 2), M.paint("#3E8E4A", a, stroke=4))
    c.drawCircle(cx + r * 0.2, cy, r * 0.35, M.paint("#3E8E4A", 0.8 * a))


def dupla(c, t, t0, x1, x2, y, f1, f2, h1, h2, a_rot=None, escuro=False):
    """duas lentes convergentes no mesmo eixo, com os focos marcados"""
    F.lente(c, t, t0, x1, y, h1, True, f1, eixo=(x1 - 280, x2 + 240), escuro=escuro)
    F.lente(c, t, t0 + 0.2, x2, y, h2, True, f2, escuro=escuro)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def um():
        E.frase(c, t, C["s01.a"], ps("o mesmo jeito:", "i", 64) + [("duas lentes convergentes", "g", 60, COR)], XE, 200, passo=0.1)
        # microscópio: objetiva de foco curto
        y1, y2 = 470, 800
        if t >= C["s01.b"]:
            F.lente(c, t, C["s01.b"], 760, y1, 150, True, 70, eixo=(560, 1500))
            F.lente(c, t, C["s01.b"] + 0.2, 1300, y1, 220, True, 170)
            E.foco(c, t, C["s01.b"], 0.5, lambda a: celula(c, 620, y1, 34, a))
            E.foco(c, t, C["s01.b"] + 0.3, 0.4, lambda a: E.escreve(c, "microscópio", XE, y1 + 15, 56, "g", TINTA, a))
        if t >= C["s01.c"]:
            F.lente(c, t, C["s01.c"], 760, y2, 230, True, None, eixo=(560, 1500))
            F.lente(c, t, C["s01.c"] + 0.2, 1300, y2, 160, True, 100)
            E.foco(c, t, C["s01.c"], 0.5, lambda a: lua(c, 1720, y2 - 20, 90, a))
            E.foco(c, t, C["s01.c"] + 0.3, 0.4, lambda a: E.escreve(c, "luneta", XE, y2 + 15, 56, "g", TINTA, a))
        pilula_em(c, t, C["s01.d"], "foco curto", 760, y1 - 140, 40, E.COR)
        pilula_em(c, t, C["s01.d"] + 0.3, "foco curto", 1300, y2 - 150, 40, E.COR)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t >= C["s02"]:
        tb = C["s02.a"] + 0.4
        E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1500, 560, 300 * ease_back(prog(t, tb, 0.8)), giro=12 * math.sin(t * 0.4)), blur=0)
        E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 84), XE, 240, passo=0.14)
        for i, (k, s) in enumerate((("s02.b", "lupa"), ("s02.c", "câmera"), ("s02.d", "microscópio"), ("s02.e", "luneta"))):
            y = 390 + i * 140
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, XE + 40, y - 28, 38, a=a), centro(c, str(i + 1), XE + 40, y - 6, 48, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, [(s, "g", 70, COR if i == 0 else TINTA)], XE + 110, y)


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    lembrete(c, t, C, "s03", [("s03.b", "na lente convergente,", "o lugar do objeto decide")], yf=1010)
    linhas = (("s03.b", "objeto longe", "real, invertida, menor"), ("s03.c", "entre F e 2F", "real, invertida, maior"), ("s03.d", "dentro do foco", "virtual, direita, maior"))
    for i, (k, l1, l2) in enumerate(linhas):
        y = 560 + 120 * i
        E.linha(c, t, [(l1 + ":", "g", 50, TINTA, C[k] + 0.4), (l2, "i", 54, TINTA2, C[k] + 0.7)], 820, y)


# ---------------- lupa e câmera ----------------
def b_simples(c, t, C, b):
    cy = 560
    if t < C["s05"]:
        def s04():
            E.frase(c, t, C["s04.a"], [("lupa:", "g", 70, COR)] + ps("objeto dentro do foco", "i", 64), XE, 200, passo=0.12)
            F.lente(c, t, C["s04.a"], 1300, cy, 420, True, 240, eixo=(700, 1840))
            objeto_o(c, t, C["s04.a"] + 0.3, 1300 - 120, cy, 90)
            xi, hi = raios_lente(c, t, (C["s04.a"] + 0.6, C["s04.a"] + 1.0), 1300, cy, 240, 1180, 90)
            imagem_i(c, t, C["s04.b"], xi, cy, hi, False)
            classifica(c, t, [(C["s04.b"], "virtual"), (C["s04.b"] + 0.3, "direita"), (C["s04.b"] + 0.6, "maior")], XE, 900, 52)
            E.frase(c, t, C["s04.c"], ps("longe da letra:", "i", 54, TINTA2) + [("vira real e invertida", "g", 52)], XE, 1010, passo=0.1)
        E.saida(c, t, C["s05"] - 0.1, s04)
        return
    E.frase(c, t, C["s05.a"], [("câmera:", "g", 70, COR)] + ps("objeto longe", "i", 64), XE, 200, passo=0.12)
    cx = 1250
    F.lente(c, t, C["s05.a"], cx, cy, 400, True, 240, eixo=(240, 1800))
    objeto_o(c, t, C["s05.a"] + 0.3, cx - 900, cy, 220)
    xi, hi = raios_lente(c, t, (C["s05.a"] + 0.6, C["s05.a"] + 1.0), cx, cy, 240, cx - 900, 220)
    imagem_i(c, t, C["s05.b"], xi, cy, hi, True)
    classifica(c, t, [(C["s05.b"], "real"), (C["s05.b"] + 0.3, "invertida"), (C["s05.b"] + 0.6, "menor")], XE, 900, 52)
    q = ep(t, C["s05.c"], 0.5)
    if q > 0:
        M.rrect(c, xi + 4, cy - 170, 26, 340, 6, "#2A2A33", q)
        E.foco(c, t, C["s05.c"], 0.4, lambda a: centro(c, "sensor", xi + 17, cy + 230, 48, "g", TINTA, a))
    if t >= C["s05.d"]:
        a = ep(t, C["s05.d"], 0.4)
        F.seta(c, cx - 30, cy - 260, cx - 120, cy - 260, E.COR, a, 7, 24)
        F.seta(c, cx + 30, cy - 260, cx + 120, cy - 260, E.COR, a, 7, 24)
    E.frase(c, t, C["s05.d"], ps("para focar, a lente", "i", 54) + [("anda", "g", 54, COR)], XE, 1010, passo=0.1)


# ---------------- duas lentes ----------------
def b_duas(c, t, C, b):
    cy = 560
    E.frase(c, t, C["s06.a"], [("duas lentes,", "g", 66, COR)] + ps("uma atrás da outra", "i", 64), XE, 200, passo=0.12)
    dupla(c, t, C["s06.a"], 640, 1360, cy, 150, 320, 340, 340)
    objeto_o(c, t, C["s06.a"] + 0.4, 640 - 220, cy, 70)
    xi, hi = raios_lente(c, t, (C["s06.b"] - 0.6, C["s06.b"] - 0.3), 640, cy, 150, 420, 70, passa=60)
    imagem_i(c, t, C["s06.b"], xi, cy, hi, True)
    E.foco(c, t, C["s06.b"] + 0.4, 0.4, lambda a: centro(c, "imagem real", xi, cy + 260, 46, "g", F.VEL, a))
    E.foco(c, t, C["s06.c"], 0.4, lambda a: centro(c, "vira o objeto da segunda", xi, cy + 320, 46, "i", TINTA, a))
    E.foco(c, t, C["s06.d"], 0.4, lambda a: centro(c, "objetiva", 640, cy - 230, 54, "g", COR, a))
    E.foco(c, t, C["s06.e"], 0.4, lambda a: centro(c, "ocular", 1360, cy - 230, 54, "g", COR, a))
    E.foco(c, t, C["s06.e"] + 0.3, 0.4, lambda a: olho(c, 1700, cy, 40, a, -1))


# ---------------- microscópio ----------------
MX1, MF1, MX2, MF2, MCY = 520, 120, 1220, 400, 560


def micro(c, t, t_l, t_o, t_r1, t_i1, t_r2, t_i2, escuro=False):
    dupla(c, t, t_l, MX1, MX2, MCY, MF1, MF2, 260, 360)
    objeto_o(c, t, t_o, MX1 - 160, MCY, 50)
    x1, h1 = raios_lente(c, t, t_r1, MX1, MCY, MF1, MX1 - 160, 50, passa=40)
    imagem_i(c, t, t_i1, x1, MCY, h1, True)
    if t_r2 is not None:
        x2, h2 = raios_lente(c, t, t_r2, MX2, MCY, MF2, x1, h1, volta=320)
        imagem_i(c, t, t_i2, x2, MCY, h2, False)
        return x1, h1, x2, h2
    return x1, h1, None, None


def b_micro(c, t, C, b):
    if t < C["s09"]:
        if t < C["s08"]:
            micro(c, t, C["s07.a"], C["s07.b"], (C["s07.b"] + 0.3, C["s07.b"] + 0.6), C["s07.c"], None, None)
            E.frase(c, t, C["s07.a"], [("microscópio:", "g", 64, COR)] + ps("objetiva de foco curto", "i", 60), XE, 200, passo=0.1)
            E.foco(c, t, C["s07.b"], 0.4, lambda a: centro(c, "lâmina", MX1 - 160, MCY + 80, 44, "i", TINTA2, a))
            classifica(c, t, [(C["s07.c"], "real"), (C["s07.c"] + 0.3, "invertida"), (C["s07.c"] + 0.6, "maior")], XE, 960, 52)
            return
        T0 = C["s08"] - 0.8
        x1, h1, x2, h2 = micro(c, t, T0, T0, (T0, T0), T0, (C["s08.b"], C["s08.b"] + 0.4), C["s08.c"])
        E.frase(c, t, C["s08.a"], [("ocular", "g", 64, COR)] + ps("= uma lupa sobre a imagem", "i", 60), XE, 200, passo=0.1)
        eixo_pontos(c, t, C["s08.b"], MCY, [(MX2 - MF2, "F")])
        classifica(c, t, [(C["s08.d"], "virtual"), (C["s08.d"] + 0.3, "invertida"), (C["s08.d"] + 0.6, "muito maior")], XE, 960, 52)
        return
    E.frase(c, t, C["s09.a"], ps("aumento total =", "i", 70) + [("produto", "g", 70, COR)], XE, 260, passo=0.12)
    E.foco(c, t, C["s09.b"], 0.4, lambda a: (E.escreve(c, "objetiva: 40×", XE, 460, 76, "g", TINTA, a)))
    E.foco(c, t, C["s09.b"] + 0.8, 0.4, lambda a: (E.escreve(c, "ocular: 10×", XE, 580, 76, "g", TINTA, a)))
    E.foco(c, t, C["s09.c"], 0.4, lambda a: E.escreve(c, "40 × 10 =", XE, 800, 100, "g", TINTA, a))
    bola_txt(c, t, C["s09.c"] + 0.8, "400×", XE + 760, 770, 130, 80)


# ---------------- luneta ----------------
LX1, LF1, LX2, LF2, LCY = 420, 750, 1320, 200, 600
TAN = 70 / 750  # inclinação dos raios da Lua: a imagem da objetiva fica 70 px abaixo do eixo, no foco


def luneta(c, t, t_l, t_r1, t_i1, t_r2, t_i2):
    F.lente(c, t, t_l, LX1, LCY, 380, True, None, eixo=(160, 1860))
    F.lente(c, t, t_l + 0.2, LX2, LCY, 280, True, None)
    eixo_pontos(c, t, t_l + 0.4, LCY, [(LX1 + LF1, "F")])
    # raios paralelos e inclinados, vindos da Lua, que se juntam no foco da objetiva
    for k, dy in enumerate((-120, 0, 120)):
        yl = LCY + dy
        P0 = (LX1 - 260, yl - 260 * TAN)
        F.raio(c, t, t_r1 + 0.1 * k, [P0, (LX1, yl), (LX1 + LF1, LCY + 70)], d=1.2, largura=4, setas=k == 1)
    imagem_i(c, t, t_i1, LX1 + LF1, LCY, -70, True)
    if t_r2 is not None:
        x2, h2 = raios_lente(c, t, t_r2, LX2, LCY, LF2, LX1 + LF1, -70, volta=300)
        imagem_i(c, t, t_i2, x2, LCY, h2, False)


def b_luneta(c, t, C, b):
    if t < C["s12"]:
        E.foco(c, t, C["s10.b"], 0.5, lambda a: lua(c, 200, 300, 70, a))
        if t < C["s11"]:
            luneta(c, t, C["s10.a"], C["s10.b"] + 0.3, C["s10.c"], None, None)
            E.frase(c, t, C["s10.a"], [("luneta:", "g", 64, COR)] + ps("objetiva de foco longo", "i", 60), XE + 300, 200, passo=0.1)
            classifica(c, t, [(C["s10.c"], "real"), (C["s10.c"] + 0.3, "invertida"), (C["s10.c"] + 0.6, "menor")], XE, 960, 52)
            E.foco(c, t, C["s10.d"], 0.4, lambda a: centro(c, "perto do foco", LX1 + LF1, LCY + 260, 46, "g", F.VEL, a))
            return
        T0 = C["s11"] - 0.8
        luneta(c, t, T0, T0, T0, (C["s11.a"], C["s11.a"] + 0.4), C["s11.b"])
        E.frase(c, t, C["s11.a"], [("ocular:", "g", 64, COR)] + ps("a lupa", "i", 60), XE + 300, 200, passo=0.1)
        classifica(c, t, [(C["s11.b"], "virtual"), (C["s11.b"] + 0.3, "invertida")], XE, 960, 52)
        E.frase(c, t, C["s11.c"], ps("menor que a Lua, mas", "i", 50) + [("perto do olho", "g", 50, COR)], 1000, 960, passo=0.1)
        return
    E.frase(c, t, C["s12.a"], ps("quantas vezes", "i", 70) + [("maior?", "g", 70, COR)], XE, 240, passo=0.12)
    E.formula_em(c, t, C["s12.b"], "f{f objetiva}{f ocular}", XE, 470, 90, "g", TINTA)
    E.formula_em(c, t, C["s12.c"], "= f{100 cm}{2 cm}", XE + 560, 470, 90, "g", TINTA)
    bola_txt(c, t, C["s12.d"], "50×", 1560, 440, 120, 80)
    E.frase(c, t, C["s12.e"], ps("telescópio refletor:", "i", 56) + [("espelho côncavo", "g", 56, COR)], XE, 800, passo=0.1)
    if t >= C["s12.e"]:
        espelho_curvo(c, t, C["s12.e"] + 0.3, 1700, 840, 360, 150, True)
        for k, dy in enumerate((-100, 100)):
            F.raio(c, t, C["s12.e"] + 0.6 + 0.1 * k, [(1250, 840 + dy), (1700 - 15, 840 + dy), (1520, 840)], d=1.0, largura=4)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s13"], [("cuidado", "g", 96, ERRADO)], XE, 200)
    E.frase(c, t, C["s13.a"], ps("a ocular é lupa, então", "i", 60) + [("final direita?", "g", 60, ERRADO)], XE, 320, passo=0.1)
    cy = 700
    objeto_o(c, t, C["s13.b"], 400, cy, 160)
    E.foco(c, t, C["s13.b"], 0.4, lambda a: centro(c, "objeto", 400, cy + 70, 44, "i", TINTA2, a))
    F.seta(c, 520, cy - 80, 700, cy - 80, TINTA2, ep(t, C["s13.d"], 0.4), 6, 22) if t >= C["s13.d"] else None
    imagem_i(c, t, C["s13.d"], 820, cy, -140, True)
    E.foco(c, t, C["s13.d"] + 0.2, 0.4, lambda a: centro(c, "objetiva: já invertida", 820, cy + 200, 44, "g", F.VEL, a))
    F.seta(c, 940, cy - 80, 1120, cy - 80, TINTA2, ep(t, C["s13.c"], 0.4), 6, 22) if t >= C["s13.c"] else None
    imagem_i(c, t, C["s13.e"], 1300, cy, -260, False)
    E.foco(c, t, C["s13.c"], 0.4, lambda a: centro(c, "a lupa mantém", 1060, cy - 120, 44, "i", TINTA, a))
    E.foco(c, t, C["s13.e"] + 0.2, 0.4, lambda a: centro(c, "final: invertida", 1300, cy + 320, 50, "g", COR, a))
    E.foco(c, t, C["s13.e"] + 0.6, 0.5, lambda a: E.selo(c, 1700, 600, 60, True, a))


# ---------------- atalho (palco) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    if t < C["s15"]:
        E.frase(c, t, C["s14"], ps("o atalho:", "i", 70, CLARO) + [("conte as imagens reais", "g", 70, BR)], W / 2, 180, "center", 0.12)
        E.frase(c, t, C["s14.b"], ps("cada imagem real", "i", 56, CLARO) + [("vira tudo de cabeça para baixo", "g", 54, BR)], W / 2, 300, "center", 0.1)
        linhas = (("s14.c", "lupa", 0, "direita"), ("s14.d", "câmera e projetor", 1, "invertida"), ("s14.e", "microscópio e luneta", 1, "invertida"))
        for i, (k, nome, n, fim) in enumerate(linhas):
            y = 500 + 160 * i
            E.foco(c, t, C[k], 0.4, lambda a, nome=nome, y=y: E.escreve(c, nome, 300, y, 60, "g", BR, a))
            E.foco(c, t, C[k] + 0.3, 0.4, lambda a, n=n, y=y: (centro(c, str(n), 1080, y, 80, "g", E.CLARO, a), centro(c, "real" if n == 1 else "reais", 1080, y + 50, 34, "i", CLARO, a)))
            E.foco(c, t, C[k] + 0.6, 0.4, lambda a, fim=fim, y=y: E.pilula(c, fim, 1520, y - 20, 56, "g", fundo=E.COR if fim == "invertida" else F.VEL, a=a))
        return
    E.frase(c, t, C["s15.a"], ps("real: raios", "i", 66, CLARO) + [("cruzados", "g", 66, BR)], W / 2, 300, "center", 0.12)
    E.frase(c, t, C["s15.b"], ps("virtual da lupa:", "i", 66, CLARO) + [("de pé em relação ao que recebe", "g", 60, BR)], W / 2, 480, "center", 0.12)
    E.frase(c, t, C["s15.c"], ps("não serve com", "i", 62, CLARO) + [("prismas:", "g", 62, BR)] + ps("o binóculo", "i", 62, CLARO), W / 2, 720, "center", 0.12)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s16"], ps("hora de testar:", "i", 72, COR) + [("microscópio", "g", 72)], XE, 190, passo=0.12)
    E.foco(c, t, C["s16.a"], 0.4, lambda a: (E.escreve(c, "objetiva:", XE, 360, 62, "i", TINTA, a), E.escreve(c, "40×", XE + 300, 360, 76, "g", COR, a)))
    E.foco(c, t, C["s16.b"], 0.4, lambda a: (E.escreve(c, "ocular:", XE, 480, 62, "i", TINTA, a), E.escreve(c, "15×", XE + 300, 480, 76, "g", COR, a)))
    E.frase(c, t, C["s16.c"], ps("aumento", "i", 70) + [("total?", "g", 70, COR)], XE, 660, passo=0.12)
    E.frase(c, t, C["s16.d"], [("real", "g", 58), ("ou", "i", 62), ("virtual?", "g", 58, COR), ("direita", "g", 58), ("ou", "i", 62), ("invertida?", "g", 58, COR)],
            XE, 800, passo=0.12)
    questao_relogio(c, t, C, "s17")


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    E.frase(c, t, C["s18.a"], ps("aumento total =", "i", 64) + [("produto", "g", 64, COR)], XE, 230, passo=0.12)
    E.foco(c, t, C["s18.b"], 0.4, lambda a: E.escreve(c, "40 × 15 =", XE, 420, 100, "g", TINTA, a))
    bola_txt(c, t, C["s18.b"] + 0.9, "600×", XE + 760, 390, 130, 80)
    E.frase(c, t, C["s18.c"], ps("ocular é lupa:", "i", 60) + [("virtual", "g", 60, F.VEL)], XE, 640, passo=0.1)
    E.frase(c, t, C["s18.d"], ps("uma imagem real no meio:", "i", 60), XE, 780, passo=0.1)
    pilula_esq(c, t, C["s18.e"], "invertida", XE + 760, 760, 60, F.VEL)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def r():
        resumo(c, t, C, "s19", [("s19.a", [("lupa:", "g"), ("virtual e direita", "i")]),
                                ("s19.b", [("câmera:", "g"), ("real e invertida", "i")]),
                                ("s19.c", [("microscópio e luneta:", "g"), ("final virtual e invertida", "i", 58, COR)])], y0=380, dy=200)
    E.saida(c, t, C["s20"] - 0.1, r)
    if t < C["s20"]:
        return
    proxima(c, t, C, "s20", [("hora de", "i", 100), ("praticar", "g", 100, COR)], [("espelhos, lentes", "g", 64), ("e olho", "i", 64)], None)


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, simples=b_simples, duas=b_duas, micro=b_micro, luneta=b_luneta,
              erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
