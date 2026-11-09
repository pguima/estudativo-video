"""Visual — Estudativo · FIS-OPT-005: reflexão total, dispersão e cor.
Segue a linguagem visual da trilha Óptica, escrita no cabeçalho do visual.py da FIS-OPT-001 (raio laranja, normal tracejada,
ângulos da normal em arco laranja, vidro em azul-vidro). Exceção desta aula: na dispersão e na cor dos objetos, cada raio
leva a cor que ele representa (vermelho, verde, azul, violeta), porque a cor é o assunto.
Os raios do ângulo limite seguem a lei de Snell com n = 2 (15° → 31°, 25° → 58°, 30° → 90°, 45° → reflexão total).
Todo instante vem de C[...] (marcadores do roteiro)."""
import math

import editorial as E
import fisica as F
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Física", "Óptica")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_FIS-OPT-005_reflexao_total_dispersao_cor.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("limite", "usos", "cores", "objeto", "atalho", "questao", "fim"))

sen = lambda g: math.sin(math.radians(g))
asen = lambda v: math.degrees(math.asin(v))
# todas as contas da aula
assert abs(asen(1 / 2) - 30) < 1e-9                                   # n = 2 → L = 30°
assert abs(sen(90) - 1) < 1e-12                                       # seno de 90° = 1
assert 2 / 1 == 2 > 1                                                 # o erro: seno igual a 2
assert abs(1 / math.sqrt(2) - math.sqrt(2) / 2) < 1e-12 and abs(asen(1 / math.sqrt(2)) - 45) < 1e-9   # questão: L = 45°
assert 60 > 45
assert abs(asen(2 * sen(15)) - 31.2) < 0.1 and abs(asen(2 * sen(25)) - 57.7) < 0.1                     # raios do desenho
assert 2 * sen(45) > 1                                                # 45° > L: não sai


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
VERM, VERDE, AZUL, VIOL = "#E0302B", "#2FA84F", "#2F6FE0", "#7B3FE4"
ESPECTRO = ("#E0302B", "#F28C1E", "#F2C81E", "#2FA84F", "#2F8FE0", "#2F4FC0", "#7B3FE4")


def meios(c, t, t0, x0, x1, cy, y0, y1, alfa=0.4, rot=("ar", "vidro"), escuro=False):
    """ar em cima, vidro embaixo da linha cy"""
    q = ep(t, t0, 0.5)
    if q <= 0:
        return
    c.drawRect(skia.Rect.MakeLTRB(x0, cy, x1, y1), M.paint(VIDRO, alfa * q))
    M.line(c, x0, cy, x1, cy, BR if escuro else TINTA, q, 5)
    if rot:
        tinta = BR if escuro else TINTA
        E.formula(c, rot[0], x1 - 20, cy - 30, 48, "b", tinta, q, "right")
        E.formula(c, rot[1], x1 - 20, cy + 70, 48, "b", tinta, q, "right")


def saindo(c, t, t0, P, i_deg, n=2.0, L=380, a_fim=1.0, rot=None, d=0.7):
    """raio no vidro (de baixo) que chega a P com i_deg da normal: sai refratado ou reflete por inteiro"""
    gi = math.radians(i_deg)
    A = (P[0] - L * math.sin(gi), P[1] + L * math.cos(gi))
    s_ = n * math.sin(gi)
    if s_ < 0.9999:
        gr = math.asin(s_)
        B = (P[0] + L * math.sin(gr), P[1] - L * math.cos(gr))
    elif s_ <= 1.0001:
        B = (P[0] + L * 1.1, P[1] - 2)
    else:
        B = (P[0] + L * math.sin(gi), P[1] + L * math.cos(gi))
    if t < t0:
        return A, B
    c.saveLayer(None, M.paint(BR, a_fim)) if a_fim < 1 else None
    F.raio(c, t, t0, [A, P, B], d=d, largura=5)
    c.restore() if a_fim < 1 else None
    return A, B


def fibra(c, t, t0, pts_meio, larg_=70, a=1.0, luz=True, n_zig=9):
    """fio de vidro curvo (polilinha do eixo) com a luz em zigue-zague por dentro"""
    q = ep(t, t0, 0.6)
    if q <= 0:
        return
    pt = M.paint(VIDRO, 0.6 * q * a, stroke=larg_, cap_round=True); pt.setStrokeJoin(skia.Paint.kRound_Join)
    p = skia.Path(); p.moveTo(*pts_meio[0])
    for P in pts_meio[1:]:
        p.lineTo(*P)
    c.drawPath(p, pt)
    pt2 = M.paint(TINTA2, q * a, stroke=3); pt2.setStrokeJoin(skia.Paint.kRound_Join)
    for lado in (-1, 1):
        q2 = skia.Path()
        for k, P in enumerate(pts_meio):
            A_, B_ = pts_meio[max(0, k - 1)], pts_meio[min(len(pts_meio) - 1, k + 1)]
            ux, uy = _u(A_, B_)
            Q = (P[0] - uy * lado * larg_ / 2, P[1] + ux * lado * larg_ / 2)
            q2.moveTo(*Q) if k == 0 else q2.lineTo(*Q)
        c.drawPath(q2, pt2)
    if not luz:
        return
    # zigue-zague: pontos alternados entre as paredes, ao longo do eixo
    comp = [math.dist(pts_meio[i], pts_meio[i + 1]) for i in range(len(pts_meio) - 1)]
    tot = sum(comp)
    zz = []
    for k in range(n_zig + 1):
        alvo = tot * k / n_zig
        ac = 0
        for i, L in enumerate(comp):
            if ac + L >= alvo:
                f = (alvo - ac) / L
                P = (lerp(pts_meio[i][0], pts_meio[i + 1][0], f), lerp(pts_meio[i][1], pts_meio[i + 1][1], f))
                ux, uy = _u(pts_meio[i], pts_meio[i + 1])
                lado = 0 if k == 0 or k == n_zig else (1 if k % 2 else -1)
                zz.append((P[0] - uy * lado * larg_ * 0.42, P[1] + ux * lado * larg_ * 0.42))
                break
            ac += L
    F.raio(c, t, t0 + 0.6, zz, d=2.2, largura=5)


def camiseta(c, cx, cy, w, cor, a=1.0, contorno=False):
    if a <= 0:
        return
    s = w / 2
    p = skia.Path()
    p.moveTo(cx - s * 0.35, cy - s); p.lineTo(cx - s, cy - s * 0.7); p.lineTo(cx - s * 1.25, cy - s * 0.15); p.lineTo(cx - s * 0.75, cy + s * 0.05)
    p.lineTo(cx - s * 0.7, cy + s); p.lineTo(cx + s * 0.7, cy + s); p.lineTo(cx + s * 0.75, cy + s * 0.05); p.lineTo(cx + s * 1.25, cy - s * 0.15)
    p.lineTo(cx + s, cy - s * 0.7); p.lineTo(cx + s * 0.35, cy - s); p.quadTo(cx, cy - s * 0.7, cx - s * 0.35, cy - s); p.close()
    c.drawPath(p, M.paint(cor, a))
    pt = M.paint(TINTA, a, stroke=4); pt.setStrokeJoin(skia.Paint.kRound_Join)
    c.drawPath(p, pt)


def seta_cor(c, t, t0, A, B, cor, d=0.5, largura=7):
    if t < t0:
        return
    F.seta(c, *A, *B, cor, 1.0, largura, 26, ease_out(prog(t, t0, d)))


# ---------------- gancho ----------------
CURVA = [(260, 860), (520, 820), (780, 700), (980, 520), (1180, 380), (1440, 320), (1760, 330)]


def b_gancho(c, t, C, b):
    def um():
        fibra(c, t, C["s01.a"], CURVA, 90, luz=False)
        if t >= C["s01.c"]:
            fibra(c, t, C["s01.c"] - 0.6, CURVA, 90, a=0.0)
        E.frase(c, t, C["s01.a"], ps("um fio de vidro,", "i", 70) + [("fino como um cabelo", "g", 64, COR)], XE, 200, passo=0.1)
        E.frase(c, t, C["s01.b"], ps("faz", "i", 64) + [("curva", "g", 64)], 1080, 620, passo=0.12)
        E.frase(c, t, C["s01.c"], ps("e a luz", "i", 64) + [("não escapa", "g", 64, COR)], 1080, 720, passo=0.12)
        E.frase(c, t, C["s01.d"], [("reflexão total", "g", 100, COR)], XE, 1010)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t >= C["s02"]:
        promessa(c, t, C, "s02", [("s02.b", "ângulo limite"), ("s02.c", "fibra, miragem, arco-íris"), ("s02.d", "a cor dos objetos")])


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    def snell_(a, x, y):
        pass

    def afasta(a, x, y):
        M.line(c, x - 150, y, x + 110, y, TINTA, a, 5)
        c.drawRect(skia.Rect.MakeLTRB(x - 150, y, x + 110, y + 90), M.paint(VIDRO, 0.5 * a))
        M.line(c, x - 20, y - 90, x - 20, y + 90, TINTA2, a, 3, dash=E.TRACO)
        M.line(c, x - 70, y + 80, x - 20, y, E.COR, a, 5); M.line(c, x - 20, y, x + 90, y - 70, E.COR, a, 5)
    lembrete(c, t, C, "s03", [("s03.b", "lei de Snell:", "n₁ · sen i = n₂ · sen r"), ("s03.c", "saindo para n menor:", "afasta da normal")], (snell_, afasta))


# ---------------- ângulo limite ----------------
P0, CY = (1320, 560), 560


def cena_limite(c, t, t0):
    meios(c, t, t0, 880, 1840, CY, 160, 1000, rot=("ar", "vidro: n = 2"))
    F.normal(c, t, t0 + 0.2, P0, 90, 380)


def b_limite(c, t, C, b):
    if t < C["s06"]:
        cena_limite(c, t, C["s04"] if t < C["s05"] else C["s05"] - 0.6)
        if t < C["s05"]:
            E.frase(c, t, C["s04.a"], ps("do vidro para o", "i", 64) + [("ar", "g", 64, COR)], XE, 260, passo=0.12)
            saindo(c, t, C["s04.b"], P0, 15, a_fim=0.35 if t > C["s04.c"] else 1.0)
            E.frase(c, t, C["s04.b"], ps("se afasta da", "i", 60) + [("normal", "g", 60)], XE, 380, passo=0.1)
            E.frase(c, t, C["s04.c"], [("aumente", "g", 60, COR)] + ps("o ângulo", "i", 60), XE, 520, passo=0.1)
            saindo(c, t, C["s04.d"], P0, 25)
            E.frase(c, t, C["s04.d"], ps("o raio vai", "i", 60) + [("deitando", "g", 60, COR)], XE, 640, passo=0.1)
            return
        T0 = C["s05"] - 0.6
        saindo(c, t, T0, P0, 15, a_fim=0.25)
        saindo(c, t, T0, P0, 25, a_fim=0.25)
        if t < C["s05.c"]:
            A, _ = saindo(c, t, C["s05.a"], P0, 30)
            E.angulo(c, t, C["s05.b"], P0, (P0[0], P0[1] + 300), A, "L", r=120, size=60)
        else:
            saindo(c, t, C["s05"] - 0.6, P0, 30, a_fim=0.35)
            A, _ = saindo(c, t, C["s05.c"], P0, 45, d=0.9)
            E.angulo(c, t, C["s05.c"] + 0.4, P0, (P0[0], P0[1] + 300), A, "45°", r=140, size=48)
        E.frase(c, t, C["s05.a"], ps("sai deitado:", "i", 60) + [("90°", "g", 60, COR)], XE, 260, passo=0.1)
        E.frase(c, t, C["s05.b"], [("ângulo limite", "g", 70, COR), ("L", "g", 70)], XE, 380, passo=0.12)
        E.frase(c, t, C["s05.c"], [("acima dele:", "g", 60)] + ps("não sai", "i", 64), XE, 530, passo=0.1)
        E.frase(c, t, C["s05.d"], ps("volta toda para dentro", "i", 60, TINTA2), XE, 630, passo=0.1)
        E.frase(c, t, C["s05.e"], [("reflexão total", "g", 90, COR)], XE, 820)
        return
    if t < C["s07"]:
        E.frase(c, t, C["s06"], ps("a conta: Snell com o raio a", "i", 64) + [("90°", "g", 64, COR)], XE, 220, passo=0.1)
        E.formula_em(c, t, C["s06.a"], "n maior · sen L = n menor · sen 90°", XE, 400, 76, "g", TINTA)
        E.formula_em(c, t, C["s06.b"], "sen 90° = 1", XE, 560, 76, "g", COR)
        E.frase(c, t, C["s06.b"] + 0.8, ps("o cateto oposto fica do tamanho da hipotenusa", "i", 46, TINTA2), XE + 560, 555, passo=0.06)
        E.formula_em(c, t, C["s06.c"], "sen L = f{n menor}{n maior}", XE, 800, 110, "g", TINTA)
        return
    if t < C["s08"]:
        cena_limite(c, t, C["s07"] - 0.6)
        A, _ = saindo(c, t, C["s07"] - 0.4, P0, 30)
        E.angulo(c, t, C["s07.c"], P0, (P0[0], P0[1] + 300), A, "30°", r=120, size=50)
        E.foco(c, t, C["s07.a"], 0.4, lambda a: E.formula(c, "n = 2  →  ar", XE, 260, 70, "g", TINTA, a))
        E.formula_em(c, t, C["s07.b"], "sen L = f{1}{2}", XE, 440, 96, "g", TINTA)
        bola_txt(c, t, C["s07.c"], "30°", XE + 560, 410, 100, 76)
        E.frase(c, t, C["s07.d"], [("mais de 30°:", "g", 58)] + ps("fica preso", "i", 62, COR), XE, 680, passo=0.1)
        return
    E.frase(c, t, C["s08.a"], [("duas", "g", 84, COR)] + ps("condições", "i", 84), XE, 240, passo=0.12)
    for i, (k, s1, s2) in enumerate((("s08.b", "do n maior", "para o n menor"), ("s08.c", "ângulo maior", "que o limite"))):
        y = 430 + 150 * i
        E.foco(c, t, C[k], 0.4, lambda a, i=i, y=y: (E.bola(c, XE + 40, y - 26, 40, a=a), centro(c, str(i + 1), XE + 40, y - 4, 50, "g", BR, a)))
        E.frase(c, t, C[k] + 0.1, [(s1, "g", 66), (s2, "i", 70)], XE + 110, y, passo=0.12)
    E.frase(c, t, C["s08.d"], [("ar → vidro:", "g", 64)] + ps("nunca", "i", 70, ERRADO), XE, 820, passo=0.12)
    E.foco(c, t, C["s08.d"] + 0.6, 0.4, lambda a: E.selo(c, XE + 760, 800, 50, False, a))


# ---------------- usos ----------------
def b_usos(c, t, C, b):
    if t < C["s10"]:
        pts = [(220, 760), (560, 760), (900, 700), (1180, 560), (1420, 520), (1780, 520)]
        fibra(c, t, C["s09.a"], pts, 120, luz=False)
        if t >= C["s09.b"]:
            fibra(c, t, C["s09.b"] - 0.6, pts, 120, a=0.0, n_zig=11)
        E.frase(c, t, C["s09.a"], [("fibra óptica", "g", 84, COR)], XE, 240)
        E.frase(c, t, C["s09.b"], ps("bate na parede", "i", 58) + [("acima do limite", "g", 58)], XE, 360, passo=0.1)
        E.frase(c, t, C["s09.c"], ps("reflete por inteiro:", "i", 58) + [("zigue-zague", "g", 58, COR)], XE, 460, passo=0.1)
        E.frase(c, t, C["s09.d"], ps("chega do outro lado,", "i", 54, TINTA2) + [("mesmo com curva", "g", 54)], XE, 960, passo=0.1)
        return
    # miragem
    yr = 880
    q = ep(t, C["s10.a"], 0.5)
    if q > 0:
        M.rrect(c, 200, yr, 1640, 90, 0, "#3B3B45", q)
        for k in range(8):
            M.rrect(c, 260 + k * 210, yr + 38, 110, 12, 4, BR, q * 0.8)
    E.frase(c, t, C["s10.a"], [("miragem", "g", 84, COR)] + ps("no asfalto quente", "i", 70), XE, 220, passo=0.12)
    if t >= C["s10.b"]:  # ar quente: índice menor perto do chão
        a = ep(t, C["s10.b"], 0.6)
        for k in range(5):
            c.drawRect(skia.Rect.MakeLTRB(200, yr - 40 * (k + 1), 1840, yr - 40 * k), M.paint(E.COR, 0.05 * (5 - k) * a))
        E.foco(c, t, C["s10.b"], 0.4, lambda a: E.escreve(c, "ar quente: n menor", 220, yr - 220, 46, "i", TINTA, a))
    pts = [(420, 330), (700, 560), (900, 720), (1040, 800), (1140, 830), (1240, 815), (1360, 770), (1700, 610)]
    F.raio(c, t, C["s10.c"], pts, d=2.0, largura=6)
    E.foco(c, t, C["s10.d"], 0.4, lambda a: olho(c, 1740, 590, 40, a, -1))
    prolonga(c, t, C["s10.e"], (1700, 610), (1060, 890))
    pilula_em(c, t, C["s10.e"] + 0.4, "o céu no chão: parece água", 1060, 1010, 44, F.VEL)
    E.foco(c, t, C["s10.e"] + 0.2, 0.5, lambda a: c.drawOval(skia.Rect.MakeXYWH(930, yr + 4, 260, 40), M.paint("#7FB8E8", 0.8 * a)))


# ---------------- dispersão e arco-íris ----------------
def b_cores(c, t, C, b):
    if t < C["s12"]:
        E.frase(c, t, C["s11.a"], ps("luz branca:", "i", 64) + [("todas as cores", "g", 64)], XE, 220, passo=0.12)
        # prisma
        Ap, Bp, Cp = (1150, 330), (880, 800), (1420, 800)
        q = ep(t, C["s11.a"], 0.5)
        if q > 0:
            p = skia.Path(); p.moveTo(*Ap); p.lineTo(*Bp); p.lineTo(*Cp); p.close()
            c.drawPath(p, M.paint(VIDRO, 0.5 * q))
            pt = M.paint(TINTA, q, stroke=5); pt.setStrokeJoin(skia.Paint.kRound_Join); c.drawPath(p, pt)
        Eh, Xh = (1000, 560), (1290, 610)
        F.raio(c, t, C["s11.a"] + 0.3, [(420, 640), Eh], d=0.7, largura=9, cor="#9A9AA6")
        F.raio(c, t, C["s11.b"], [Eh, Xh], d=0.6, largura=7, cor="#C9C9D2")
        for k, cor in enumerate(ESPECTRO):
            ang = math.radians(18 + 6 * k)
            F.raio(c, t, C["s11.b"] + 0.6 + 0.05 * k, [Xh, (Xh[0] + 520 * math.cos(ang), Xh[1] + 520 * math.sin(ang))], d=0.8, largura=6, cor=cor, setas=False)
        E.frase(c, t, C["s11.c"], [("violeta:", "g", 56, VIOL)] + ps("maior índice, desvia mais", "i", 54), XE, 900, passo=0.08)
        E.frase(c, t, C["s11.d"], [("vermelho:", "g", 56, VERM)] + ps("menor índice, desvia menos", "i", 54), XE, 990, passo=0.08)
        E.frase(c, t, C["s11.e"], [("dispersão", "g", 84, COR)], XE, 360)
        return
    # gota de chuva
    O, r = (1000, 560), 230
    E.frase(c, t, C["s12.a"], [("arco-íris:", "g", 70, COR)] + ps("cada gota", "i", 70), XE, 200, passo=0.12)
    E.foco(c, t, C["s12.a"], 0.5, lambda a: (c.drawCircle(*O, r, M.paint(VIDRO, 0.45 * a)), c.drawCircle(*O, r, M.paint(TINTA, a, stroke=4))))
    pa = lambda g: (O[0] + r * math.cos(math.radians(g)), O[1] + r * math.sin(math.radians(g)))
    A, Bk, D = pa(-55), pa(175), pa(70)
    F.raio(c, t, C["s12.b"] - 0.6, [(1700, A[1]), A], d=0.6, largura=7, cor="#9A9AA6")
    F.raio(c, t, C["s12.b"], [A, Bk], d=0.6, largura=6, cor="#C9C9D2")
    F.raio(c, t, C["s12.c"], [Bk, D], d=0.6, largura=6, cor="#C9C9D2")
    for k, cor in enumerate(ESPECTRO):
        ang = math.radians(22 + 2.2 * k)
        F.raio(c, t, C["s12.d"] + 0.05 * k, [D, (D[0] + 640 * math.cos(ang), D[1] + 640 * math.sin(ang))], d=0.8, largura=5, cor=cor, setas=False)
    E.foco(c, t, C["s12.b"] + 0.2, 0.4, lambda a: E.escreve(c, "refrata", A[0] + 30, A[1] - 30, 44, "i", TINTA2, a))
    E.foco(c, t, C["s12.c"] + 0.2, 0.4, lambda a: E.escreve(c, "reflete", Bk[0] - 200, Bk[1] + 10, 44, "i", TINTA2, a))
    E.foco(c, t, C["s12.d"] + 0.2, 0.4, lambda a: E.escreve(c, "refrata", D[0] - 220, D[1] + 30, 44, "i", TINTA2, a))
    E.foco(c, t, C["s12.e"], 0.5, lambda a: (sol(c, 1780, A[1] - 120, 60, a), olho(c, 1680, 900, 40, a, -1)))
    E.frase(c, t, C["s12.e"], ps("o Sol nas", "i", 60) + [("costas", "g", 60, COR)], XE, 330, passo=0.1)


# ---------------- cor dos objetos ----------------
def b_objeto(c, t, C, b):
    y = 640
    if t < C["s14"]:
        E.frase(c, t, C["s13.a"], ps("o objeto não tem", "i", 64) + [("luz própria", "g", 64)], XE, 200, passo=0.1)
        E.frase(c, t, C["s13.b"], [("reflete", "g", 60, COR)] + ps("umas e", "i", 60) + [("absorve", "g", 60)] + ps("as outras", "i", 60), XE, 300, passo=0.1)
        for k, (cx, cor, kk, refl) in enumerate(((520, VERM, "s13.c", (VERM,)), (1000, "#F4F4F0", "s13.d", (VERM, VERDE, AZUL)), (1480, "#1E1E24", "s13.e", ()))):
            E.foco(c, t, C[kk], 0.5, lambda a, cx=cx, cor=cor: camiseta(c, cx, y + 60, 260, cor, a))
            for j, cj in enumerate((VERM, VERDE, AZUL)):
                seta_cor(c, t, C[kk] + 0.3 + 0.1 * j, (cx - 230 + 40 * j, y - 300), (cx - 100 + 40 * j, y - 120), cj)
            for j, cj in enumerate(refl):
                seta_cor(c, t, C[kk] + 0.9 + 0.1 * j, (cx + 60 + 40 * j, y - 120), (cx + 170 + 40 * j, y - 300), cj)
            nome = ("reflete o vermelho", "reflete todas", "absorve todas")[k]
            E.foco(c, t, C[kk] + 0.8, 0.4, lambda a, cx=cx, nome=nome: centro(c, nome, cx, y + 280, 46, "i", TINTA, a))
        return
    E.frase(c, t, C["s14.a"], ps("luz só", "i", 66) + [("azul", "g", 66, AZUL)], XE, 220, passo=0.12)
    E.foco(c, t, C["s14.a"], 0.5, lambda a: camiseta(c, 600, y + 60, 280, VERM, a))
    seta_cor(c, t, C["s14.a"] + 0.4, (380, y - 320), (520, y - 120), AZUL)
    seta_cor(c, t, C["s14.a"] + 0.6, (440, y - 330), (580, y - 130), AZUL)
    q = ep(t, C["s14.c"], 0.6)
    if q > 0:
        camiseta(c, 600, y + 60, 280, "#1E1E24", q)
    E.frase(c, t, C["s14.b"], ps("não tem vermelho para refletir", "i", 48, TINTA2), 600, y + 300, "center", 0.06)
    pilula_em(c, t, C["s14.c"], "parece preta", 600, y + 390, 50, "#1E1E24")
    E.frase(c, t, C["s14.d"], [("branca", "g", 60)] + ps("sob luz", "i", 60) + [("vermelha", "g", 60, VERM)], 1100, 220, passo=0.12)
    E.foco(c, t, C["s14.d"], 0.5, lambda a: camiseta(c, 1440, y + 60, 280, "#F4F4F0", a))
    seta_cor(c, t, C["s14.d"] + 0.4, (1220, y - 320), (1360, y - 120), VERM)
    q2 = ep(t, C["s14.d"] + 1.0, 0.6)
    if q2 > 0:
        camiseta(c, 1440, y + 60, 280, "#E86A66", q2)
        seta_cor(c, t, C["s14.d"] + 1.0, (1500, y - 120), (1640, y - 320), VERM)
    pilula_em(c, t, C["s14.d"] + 1.2, "parece vermelha", 1440, y + 390, 50, VERM)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s15"], [("cuidado", "g", 96, ERRADO)], XE, 200)
    E.frase(c, t, C["s15.a"], ps("virar a fração do", "i", 70) + [("ângulo limite", "g", 70, ERRADO)], XE, 330, passo=0.12)
    E.foco(c, t, C["s15.b"], 0.4, lambda a: E.formula(c, "sen L = f{n maior}{n menor}", XE, 540, 100, "g", ERRADO, a))
    E.formula_em(c, t, C["s15.c"], "= f{2}{1} = 2", XE + 830, 540, 100, "g", TINTA)
    E.frase(c, t, C["s15.d"], ps("o seno nunca passa de", "i", 64) + [("1", "g", 64, ERRADO)], XE, 780, passo=0.12)
    E.foco(c, t, C["s15.d"] + 0.6, 0.5, lambda a: E.selo(c, 1700, 510, 70, False, a))
    pilula_esq(c, t, C["s15.e"], "deu mais que 1? fração de cabeça para baixo", XE, 920, 46, E.COR)


# ---------------- atalho (palco) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    if t < C["s17"]:
        E.frase(c, t, C["s16"], ps("os atalhos de prova", "i", 72, CLARO), W / 2, 170, "center")
        E.foco(c, t, C["s16.a"], 0.4, lambda a: centro(c, "sen L = menor ÷ maior", W / 2, 330, 84, "g", BR, a))
        E.frase(c, t, C["s16.b"], ps("cor sob luz colorida:", "i", 60, CLARO), W / 2, 480, "center")
        E.frase(c, t, C["s16.c"], ps("reflete a cor da luz", "i", 56, CLARO) + [("→", "g", 56, CLARO), ("essa cor", "g", 56, BR)], W / 2, 590, "center", 0.1)
        E.frase(c, t, C["s16.d"], ps("não reflete", "i", 56, CLARO) + [("→", "g", 56, CLARO), ("preto", "g", 56, BR)], W / 2, 680, "center", 0.1)
        E.frase(c, t, C["s16.e"], [("violeta", "g", 66, "#B48CFF"), ("desvia mais,", "i", 66, CLARO), ("vermelho", "g", 66, "#FF6A5E"), ("desvia menos", "i", 66, CLARO)],
                W / 2, 880, "center", 0.12)
        return
    E.frase(c, t, C["s17"], ps("o objeto só devolve a luz que", "i", 66, CLARO) + [("recebe", "g", 66, BR)], W / 2, 260, "center", 0.1)
    E.foco(c, t, C["s17.a"], 0.4, lambda a: centro(c, "não cria cor nenhuma", W / 2, 400, 76, "g", BR, a))
    E.frase(c, t, C["s17.b"], [("cuidado:", "g", 60, BR)] + ps("luz misturada, como a amarela de lâmpada", "i", 56, CLARO), W / 2, 640, "center", 0.08)
    E.frase(c, t, C["s17.c"], ps("leia o que a questão diz sobre a", "i", 60, CLARO) + [("luz", "g", 60, BR)], W / 2, 800, "center", 0.1)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s18"], ps("hora de testar", "i", 72, COR), XE, 190)
    E.frase(c, t, C["s18.a"], ps("de um cristal de", "i", 62) + [("n = √2", "g", 62, COR)] + ps("para o ar", "i", 62), XE, 340, passo=0.1)
    E.frase(c, t, C["s18.b"], ps("qual o", "i", 72) + [("ângulo limite?", "g", 70, COR)], XE, 500, passo=0.12)
    E.frase(c, t, C["s18.c"], ps("chegando a", "i", 62) + [("60°:", "g", 62, COR)] + ps("sai ou reflete?", "i", 62), XE, 660, passo=0.1)
    if t < C["s19"]:
        meios(c, t, C["s18.a"], 1180, 1820, 560, 300, 940, rot=("ar", "n = r{2}"))
        P = (1480, 560)
        F.normal(c, t, C["s18.c"], P, 90, 300)
        g = math.radians(60)
        F.raio(c, t, C["s18.c"] + 0.2, [(P[0] - 320 * math.sin(g), P[1] + 320 * math.cos(g)), P], d=0.6)
    questao_relogio(c, t, C, "s19")


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    if t < C["s21"]:
        E.formula_em(c, t, C["s20.a"], "sen L = f{menor}{maior}", XE, 300, 96, "g", TINTA2)
        E.formula_em(c, t, C["s20.b"], "sen L = f{1}{r{2}}", XE, 520, 100, "g", TINTA)
        E.formula_em(c, t, C["s20.c"], "= f{r{2}}{2}", XE + 520, 520, 100, "g", TINTA)
        bola_txt(c, t, C["s20.d"], "45°", 1500, 480, 130, 90)
        return
    meios(c, t, C["s21"] - 0.6, 1000, 1840, CY, 200, 1000, rot=("ar", "n = r{2}"))
    F.normal(c, t, C["s21"] - 0.5, P0, 90, 380)
    A, _ = saindo(c, t, C["s21"] - 0.4, P0, 60, n=math.sqrt(2), d=0.9)
    E.angulo(c, t, C["s21"], P0, (P0[0], P0[1] + 300), A, "60°", r=130, size=48)
    E.frase(c, t, C["s21.a"], [("60°", "g", 66, COR), (">", "g", 66, TINTA2), ("45°", "g", 66)], XE, 300, passo=0.15)
    E.frase(c, t, C["s21.a"] + 1.0, ps("e vai do", "i", 56) + [("n maior para o menor", "g", 54)], XE, 410, passo=0.1)
    E.frase(c, t, C["s21.b"], [("reflexão total", "g", 84, COR)], XE, 600)
    E.foco(c, t, C["s21.b"] + 0.6, 0.4, lambda a: E.escreve(c, "o raio não sai", XE, 700, 60, "i", TINTA, a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def r():
        resumo(c, t, C, "s22", [("s22.a", [("sen L = menor ÷ maior", "g", 62, COR)]),
                                ("s22.b", [("total:", "g"), ("do n maior para o menor,", "i"), ("acima do limite", "i")]),
                                ("s22.c", [("cor:", "g"), ("só aparece se o objeto", "i"), ("reflete", "g", 62, COR)])], y0=380, dy=200)
    E.saida(c, t, C["s23"] - 0.1, r)
    if t < C["s23"]:
        return

    def desenho():
        if t >= C["s23.b"]:
            F.lente(c, t, C["s23.b"], 700, 820, 300, True, 200, eixo=(330, 1100))
            for k, dy in enumerate((-90, 0, 90)):
                F.raio(c, t, C["s23.b"] + 0.3 + 0.1 * k, [(360, 820 + dy), (700, 820 + dy), (900, 820)], d=1.0, largura=5)
    proxima(c, t, C, "s23", [("o vidro", "i", 100), ("ganha curva", "g", 100, COR)], [("as", "i", 80), ("lentes", "g", 80)], desenho)


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, limite=b_limite, usos=b_usos, cores=b_cores, objeto=b_objeto,
              erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
