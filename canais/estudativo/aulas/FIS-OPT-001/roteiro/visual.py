"""Visual — Estudativo · FIS-OPT-001: luz em linha reta, sombra e câmara escura. Primeira aula da trilha Óptica.

LINGUAGEM VISUAL DA ÓPTICA (todas as FIS-OPT copiam daqui; a da Física inteira está no visual.py da FIS-CIN-001):
- Matéria: E.usar("Física", "Óptica"). Papel claro, uma cor forte por tela (laranja), texto à esquerda (XE) e desenho à direita.
- RAIO DE LUZ = laranja (E.COR), traço cheio com seta no meio (F.raio), que avança no instante da fala. PROLONGAMENTO de raio
  (o caminho que o olho "imagina" para trás) = tracejado cinza (TINTA2), sem seta (prolonga). Nunca desenhe prolongamento em laranja.
- NORMAL = tracejado em tinta (F.normal). Ângulos medidos dela: arco laranja com a letra (i, r, L) em grotesca.
- OBJETO = seta em tinta (objeto_o). IMAGEM = seta petróleo (F.VEL): cheia se real, tracejada se virtual (imagem_i).
  As palavras da imagem (real/virtual, direita/invertida, maior/menor) entram em pílulas petróleo, uma por fala (classifica).
- SUPERFÍCIES: espelho em tinta com hachura do lado de trás (F.espelho_plano, espelho_curvo); lente e água/vidro em azul-vidro
  claro (VIDRO, F.lente). Eixo principal tracejado; F em laranja, C, V e O em tinta, com a letra embaixo (eixo_pontos).
- FONTE DE LUZ = esfera âmbar com brilho (lampada_fonte, sol). Olho de quem vê = olho(). Sombra = cinza-escuro; penumbra = cinza claro.
- Contas: a equação dos espelhos e das lentes sai de raios desenhados pela própria conta (raios_espelho, raios_lente usam gauss),
  então o desenho nunca contradiz o número. Resposta final na esfera laranja (bola_txt), unidade menor (F.medida).
- Certo = verde, errado = vermelho com risco, como no canal. Atalho no palco escuro (palco). Questão com E.relogio.
Todo instante vem de C[...] (marcadores do roteiro), para acompanhar a voz real quando ela chegar."""
import math

import editorial as E
import fisica as F
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Física", "Óptica")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_FIS-OPT-001_luz_em_linha_reta_sombra_camara_escura.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("reta", "sombra", "eclipse", "camara", "atalho", "questao", "fim"))

# todas as contas da aula
assert 2 * 30 / 3 == 20                                   # poste 2 m / sombra 3 m → prédio de sombra 30 m tem 20 m
assert 6 * 100 == 600 and 30 * 100 == 3000                # para centímetro
assert 600 * 20 / 3000 == 4 and 6 * 20 / 30 == 4          # imagem de 4 cm (o erro dá "4 m")
assert 3000 / 20 == 150 and 600 / 150 == 4                # atalho: 150 vezes menor
assert 18 * 100 == 1800 and 1800 / 15 == 120 and 5 * 120 == 600   # questão: poste de 6 m
assert 5 / 600 == 15 / 1800


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
def arvore(c, x, yb, h, a=1.0, inverte=False, sx=1.0):
    """árvore de altura h com o pé em (x, yb); inverte = de cabeça para baixo (pé em yb, copa para baixo); sx estreita"""
    if a <= 0:
        return
    c.save(); c.translate(x, yb)
    c.scale(sx, -1 if inverte else 1)
    w = h * 0.12
    M.rrect(c, -w / 2, -h * 0.45, w, h * 0.45, w * 0.3, "#8B5E3C", a)
    for dx, dy, r in ((0, -0.68, 0.3), (-0.16, -0.55, 0.2), (0.16, -0.55, 0.2)):
        c.drawCircle(dx * h, dy * h, r * h, M.paint("#3E8E4A", a))
    c.restore()


def caixa(c, x0, y0, x1, y1, furo, a=1.0):
    """caixa (câmara escura) de lado, com o furo na face da esquerda em y = furo"""
    if a <= 0:
        return
    c.drawRect(skia.Rect.MakeLTRB(x0, y0, x1, y1), M.paint("#2A2A33", 0.08 * a))
    pt = M.paint(TINTA, a, stroke=7)
    M.line(c, x0, y0, x1, y0, TINTA, a, 7); M.line(c, x0, y1, x1, y1, TINTA, a, 7); M.line(c, x1, y0, x1, y1, TINTA, a, 7)
    M.line(c, x0, y0, x0, furo - 10, TINTA, a, 7); M.line(c, x0, furo + 10, x0, y1, TINTA, a, 7)


def camara(c, t, C, t_cx, t_topo, t_pe, t_img, xa, ya_pe, ha, x0, y0, x1, y1, furo, inv_rot=None):
    """árvore, caixa e os dois raios que se cruzam no furo; devolve (y da imagem do topo, y da imagem do pé)"""
    E.foco(c, t, t_cx, 0.5, lambda a: (arvore(c, xa, ya_pe, ha, a), caixa(c, x0, y0, x1, y1, furo, a)))
    topo, pe, Hf = (xa, ya_pe - ha), (xa, ya_pe), (x0, furo)
    k = (x1 - x0) / (x0 - xa)
    yi_topo, yi_pe = furo + (furo - topo[1]) * k, furo + (furo - pe[1]) * k
    F.raio(c, t, t_topo, [topo, Hf, (x1, yi_topo)], d=1.0, largura=5)
    F.raio(c, t, t_pe, [pe, Hf, (x1, yi_pe)], d=1.0, largura=5)
    E.foco(c, t, t_img, 0.5, lambda a: _img_inv(c, x1 - (yi_topo - yi_pe) * 0.46 * 0.4 - 10, yi_pe, yi_topo, a))
    return yi_topo, yi_pe


def fr_txt(c, cima, baixo, cx, y, size, a):
    """fração escrita em palavras: duas linhas centradas e o traço"""
    w = max(E.larg(cima, "b", size), E.larg(baixo, "b", size)) + 20
    centro(c, cima, cx, y - 14, size, "b", TINTA, a)
    M.line(c, cx - w / 2, y + 4, cx + w / 2, y + 4, TINTA, a, 4)
    centro(c, baixo, cx, y + size + 16, size, "b", TINTA, a)


def _img_inv(c, x, y_pe, y_topo, a):
    """árvore invertida: o pé em y_pe (em cima) e o topo em y_topo (embaixo)"""
    arvore(c, x, y_pe, y_topo - y_pe, a, inverte=True, sx=0.4)


def bola_sombra(c, cx, cy, r, a=1.0):
    E.bola(c, cx, cy, r, E.COR, a)


def _tang(S, O, r):
    """ângulos (rad) das duas tangentes da fonte S ao círculo (O, r)"""
    phi = math.atan2(O[1] - S[1], O[0] - S[0])
    al = math.asin(min(0.999, r / math.dist(S, O)))
    return phi - al, phi + al


def _na_parede(S, ang, xp):
    return S[1] + math.tan(ang) * (xp - S[0])


def parede(c, xp, y0, y1, a=1.0):
    if a <= 0:
        return
    M.rrect(c, xp, y0, 26, y1 - y0, 6, "#E9E6DE", a)
    M.line(c, xp, y0, xp, y1, TINTA, a, 5)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def um():
        E.frase(c, t, C["s01.a"], ps("uma caixa com um", "i", 80) + [("furinho", "g", 80, COR)], XE, 210, passo=0.12)
        E.frase(c, t, C["s01.b"], ps("mostra a árvore inteira", "i", 64, TINTA2), XE, 310, passo=0.1)
        camara(c, t, C, C["s01.a"] + 0.3, C["s01.b"], C["s01.b"] + 0.5, C["s01.c"], 380, 920, 460, 1120, 470, 1640, 860, 665)
        pilula_em(c, t, C["s01.c"] + 0.4, "de cabeça para baixo", 1380, 945, 46, E.COR)
        E.frase(c, t, C["s01.d"], ps("e a altura da árvore?", "i", 60) + [("proporção", "g", 60, COR)], XE, 1020, "left", 0.1)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t >= C["s02"]:
        promessa(c, t, C, "s02", [("s02.b", "sombra e penumbra"), ("s02.c", "eclipses"), ("s02.d", "câmara escura")])


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    lembrete(c, t, C, "s03", [("s03.b", "semelhança de triângulos:", "lados proporcionais")], yf=1010)
    yc = 840
    q = ep(t, C["s03.c"], 0.4)
    if q > 0:
        M.line(c, 820, yc, 1820, yc, TINTA, q, 5)
    # poste 2 m, sombra 3 m · prédio ?, sombra 30 m (fora de escala, mesmo formato)
    for k, (x, h, s, ts, rh, rs) in enumerate(((880, 120, 180, C["s03.c"], "2 m", "3 m"), (1300, 300, 450, C["s03.d"], None, "30 m"))):
        if t < ts:
            continue
        a = ep(t, ts, 0.5)
        if k == 0:
            M.rrect(c, x - 8, yc - h, 16, h, 6, TINTA, a)
        else:
            M.rrect(c, x - 60, yc - h, 120, h, 8, "#8C8C99", a)
            for j in range(4):
                for i in range(2):
                    M.rrect(c, x - 40 + 48 * i, yc - h + 30 + 64 * j, 32, 36, 4, BR, a * 0.9)
        xb = x + (8 if k == 0 else 60)
        M.rrect(c, xb, yc - 6, s * ease_io(prog(t, ts + 0.3, 0.6)), 12, 6, "#3B3B45", a * 0.85)
        M.line(c, x, yc - h, xb + s, yc, LUZ, a * ep(t, ts + 0.8, 0.4), 4, dash=E.TRACO)
        E.foco(c, t, ts + 0.5, 0.4, lambda a, x=x, h=h, rh=rh: E.escreve(c, rh, x - 120 - (60 if k else 0), yc - h / 2, 50, "b", TINTA, a) if rh else None)
        E.foco(c, t, ts + 0.9, 0.4, lambda a, xb=xb, s=s, rs=rs: centro(c, rs, xb + s / 2, yc + 60, 50, "b", TINTA2, a))
    E.foco(c, t, C["s03.e"], 0.5, lambda a: E.escreve(c, "20 m", 1060, 700, 72, "g", COR, a))


# ---------------- luz em linha reta ----------------
def b_reta(c, t, C, b):
    def s04():
        E.frase(c, t, C["s04"], ps("num meio igual em todo lugar", "i", 60, TINTA2), XE, 200, passo=0.1)
        E.frase(c, t, C["s04.a"], ps("a luz anda em", "i", 90) + [("linha reta", "g", 90, COR)], XE, 320, passo=0.12)
        S = (560, 680)
        E.foco(c, t, C["s04.a"], 0.5, lambda a: lampada_fonte(c, *S, 34, a))
        for i in range(7):
            g = math.radians(-60 + 20 * i)
            F.raio(c, t, C["s04.a"] + 0.3 + 0.08 * i, [S, (S[0] + 330 * math.cos(g), S[1] + 330 * math.sin(g))], d=0.6, largura=5)
        # o que está atrás da parede: o raio do objeto até o olho para na parede
        if t >= C["s04.b"]:
            a = ep(t, C["s04.b"], 0.5)
            E.foco(c, t, C["s04.b"], 0.5, lambda a: (E.bola(c, 1150, 700, 46, E.COR, a), parede(c, 1380, 520, 900, a), olho(c, 1700, 700, 46, a, -1)))
            F.raio(c, t, C["s04.b"] + 0.6, [(1196, 700), (1378, 700)], d=0.6, largura=5)
            E.foco(c, t, C["s04.b"] + 1.2, 0.4, lambda a: (M.line(c, 1440, 650, 1530, 750, ERRADO, a, 10), M.line(c, 1530, 650, 1440, 750, ERRADO, a, 10)))
            E.foco(c, t, C["s04.b"] + 1.4, 0.4, lambda a: centro(c, "não chega ao olho", 1430, 980, 46, "i", TINTA2, a))
    E.saida(c, t, C["s05"] - 0.1, s04)
    if t < C["s05"]:
        return
    E.frase(c, t, C["s05.a"], ps("uma reta com seta:", "i", 76), XE, 230, passo=0.12)
    E.frase(c, t, C["s05.b"], [("raio de luz", "g", 90, COR)], XE, 350)
    F.raio(c, t, C["s05.b"], [(1060, 300), (1760, 300)], d=0.8, largura=8)
    E.foco(c, t, C["s05.b"] + 0.8, 0.4, lambda a: centro(c, "para onde a luz vai", 1530, 380, 44, "i", TINTA2, a))
    # pontual e extensa
    E.foco(c, t, C["s05.c"], 0.5, lambda a: lampada_fonte(c, 620, 700, 22, a))
    E.foco(c, t, C["s05.c"] + 0.2, 0.4, lambda a: (centro(c, "fonte", 620, 860, 56, "i", TINTA, a), centro(c, "pontual", 620, 930, 60, "g", COR, a)))

    def extensa(a):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(1380, 700), 380, [M.hexc(LUZ, 0.45 * a), M.hexc(LUZ, 0.0)], [0, 1]))
        c.drawCircle(1380, 700, 380, p)
        M.rrect(c, 1180, 680, 400, 40, 20, LUZ, a)
    E.foco(c, t, C["s05.d"], 0.5, extensa)
    E.foco(c, t, C["s05.d"] + 0.2, 0.4, lambda a: (centro(c, "fonte", 1380, 860, 56, "i", TINTA, a), centro(c, "extensa", 1380, 930, 60, "g", COR, a)))


# ---------------- sombra e penumbra ----------------
def b_sombra(c, t, C, b):
    O, r, xp, y0, y1 = (900, 640), 80, 1520, 300, 990

    def s06():
        S = (430, 640)
        E.frase(c, t, C["s06"], ps("fonte pontual", "i", 70), XE, 200)
        E.foco(c, t, C["s06.a"], 0.5, lambda a: (lampada_fonte(c, *S, 26, a), bola_sombra(c, *O, r, a), parede(c, xp, y0, y1, a)))
        g1, g2 = _tang(S, O, r)
        ya, yb = _na_parede(S, g1, xp), _na_parede(S, g2, xp)
        F.raio(c, t, C["s06.b"], [S, (xp, ya)], d=0.8, largura=4)
        F.raio(c, t, C["s06.b"] + 0.3, [S, (xp, yb)], d=0.8, largura=4)
        q = ep(t, C["s06.c"], 0.5)
        if q > 0:
            M.rrect(c, xp - 4, ya, 34, yb - ya, 4, "#2A2A33", q)
            pilula_em(c, t, C["s06.c"], "sombra", xp + 190, (ya + yb) / 2, 50, "#2A2A33")
        E.frase(c, t, lerp(C["s06.c"], C["s06.end"], 0.4), ps("borda", "i", 64) + [("nítida", "g", 64, COR)], XE, 330, passo=0.12)
    E.saida(c, t, C["s07"] - 0.1, s06)
    if t < C["s07"]:
        return
    A, B = (430, 560), (430, 720)
    E.frase(c, t, C["s07"], ps("fonte extensa", "i", 70), XE, 200)
    E.foco(c, t, C["s07.a"], 0.5, lambda a: (M.rrect(c, A[0] - 16, A[1] - 10, 32, B[1] - A[1] + 20, 16, LUZ, a), bola_sombra(c, *O, r, a), parede(c, xp, y0, y1, a)))
    sh = []
    for k, S in enumerate((A, B)):
        g1, g2 = _tang(S, O, r)
        ya, yb = _na_parede(S, g1, xp), _na_parede(S, g2, xp)
        sh.append((ya, yb))
        F.raio(c, t, C["s07.a"] + 0.6 + 0.4 * k, [S, (xp, ya)], d=0.8, largura=3)
        F.raio(c, t, C["s07.a"] + 0.6 + 0.4 * k, [S, (xp, yb)], d=0.8, largura=3)
    um0, um1 = max(sh[0][0], sh[1][0]), min(sh[0][1], sh[1][1])
    pe0, pe1 = min(sh[0][0], sh[1][0]), max(sh[0][1], sh[1][1])
    qp, qu = ep(t, C["s07.c"], 0.5), ep(t, C["s07.b"], 0.5)
    if qp > 0:
        M.rrect(c, xp - 4, pe0, 34, um0 - pe0, 4, "#9C9AA6", qp)
        M.rrect(c, xp - 4, um1, 34, pe1 - um1, 4, "#9C9AA6", qp)
    if qu > 0:
        M.rrect(c, xp - 4, um0, 34, um1 - um0, 4, "#2A2A33", qu)
    pilula_em(c, t, C["s07.b"] + 0.2, "sombra", xp + 190, (um0 + um1) / 2, 50, "#2A2A33")
    pilula_em(c, t, C["s07.d"], "penumbra", xp + 215, (um1 + pe1) / 2, 50, "#8C8A96")
    pilula_em(c, t, C["s07.d"] + 0.2, "penumbra", xp + 215, (pe0 + um0) / 2, 50, "#8C8A96")
    E.frase(c, t, C["s07.c"] + 0.3, ps("luz de", "i", 58) + [("parte", "g", 58, COR)] + ps("da fonte", "i", 58), XE, 330, passo=0.12)


# ---------------- eclipses ----------------
def cena_eclipse(c, t, ts, ordem, cores, raios, xs, sombra_em, rot_meio):
    """três astros em linha; o do meio faz a sombra (umbra escura e penumbra clara) sobre o terceiro"""
    cy = 620
    for i, (nome, x, r, cor, ti) in enumerate(zip(ordem, xs, raios, cores, ts)):
        E.foco(c, t, ti, 0.5, lambda a, x=x, r=r, cor=cor, nome=nome: (sol(c, x, cy, r, a) if nome == "Sol" else E.bola(c, x, cy, r, cor, a),
                                                                      centro(c, nome, x, cy + max(r, 60) + 70, 52, "g", TINTA, a)))
    tm = ts[1]
    q = ep(t, sombra_em, 0.6)
    if q > 0:
        xm, rm, xf = xs[1], raios[1], xs[2]
        alvo_r = raios[2]
        # penumbra: cunha que abre; umbra: cone que fecha
        p = skia.Path(); p.moveTo(xm, cy - rm); p.lineTo(xf, cy - rm * 2.4); p.lineTo(xf, cy + rm * 2.4); p.lineTo(xm, cy + rm); p.close()
        c.drawPath(p, M.paint("#2A2A33", 0.16 * q))
        p2 = skia.Path(); p2.moveTo(xm, cy - rm); p2.lineTo(xf - alvo_r * 0.3, cy - rm * 0.45); p2.lineTo(xf - alvo_r * 0.3, cy + rm * 0.45); p2.lineTo(xm, cy + rm); p2.close()
        c.drawPath(p2, M.paint("#2A2A33", 0.55 * q))


def b_eclipse(c, t, C, b):
    def s08():
        E.frase(c, t, C["s08"], [("eclipse", "i", 84), ("do Sol", "g", 84, COR)], XE, 200)
        E.frase(c, t, C["s08.a"], [("Sol", "g", 56), ("·", "g", 56, TINTA2), ("Lua", "g", 56, COR), ("·", "g", 56, TINTA2), ("Terra", "g", 56)], XE, 300, passo=0.15)
        cena_eclipse(c, t, (C["s08"] + 0.4, C["s08.a"], C["s08.a"] + 0.4), ("Sol", "Lua", "Terra"), (LUZ, "#B9B7C2", "#2F7FC1"),
                     (170, 40, 150), (330, 1000, 1640), C["s08.b"], "Lua")
        pilula_em(c, t, C["s08.c"], "total", 1420, 520, 46, "#2A2A33")
        pilula_em(c, t, C["s08.d"], "parcial", 1420, 760, 46, "#8C8A96")
    E.saida(c, t, C["s09"] - 0.1, s08)
    if t < C["s09"]:
        return
    E.frase(c, t, C["s09"], [("eclipse", "i", 84), ("da Lua", "g", 84, COR)], XE, 200)
    E.frase(c, t, C["s09.a"], [("Sol", "g", 56), ("·", "g", 56, TINTA2), ("Terra", "g", 56, COR), ("·", "g", 56, TINTA2), ("Lua", "g", 56)], XE, 300, passo=0.15)
    cena_eclipse(c, t, (C["s09"] + 0.3, C["s09.a"], C["s09.a"] + 0.4), ("Sol", "Terra", "Lua"), (LUZ, "#2F7FC1", "#B9B7C2"),
                 (170, 120, 46), (330, 1000, 1620), C["s09.b"], "Terra")
    if t >= C["s09.b"]:  # a Lua escurece
        E.bola(c, 1620, 620, 46, "#5A3A30", 0.85 * ep(t, C["s09.b"] + 0.4, 0.8))
    E.frase(c, t, C["s09.c"], ps("o do meio faz a", "i", 54) + [("sombra", "g", 54, COR)], XE + 980, 200, passo=0.1)
    E.frase(c, t, C["s09.d"], ps("o nome é de quem", "i", 54) + [("some", "g", 54, COR)], XE + 980, 290, passo=0.1)


# ---------------- câmara escura ----------------
GEO = dict(xa=440, ya=900, ha=480, x0=1080, y0=400, x1=1640, y1=860, furo=630)


def _geo():
    g = GEO
    k = (g["x1"] - g["x0"]) / (g["x0"] - g["xa"])
    yt = g["furo"] + (g["furo"] - (g["ya"] - g["ha"])) * k
    yp = g["furo"] + (g["furo"] - g["ya"]) * k
    return yt, yp


def b_camara(c, t, C, b):
    g = GEO
    yt, yp = _geo()

    def cena_cx(t_cx, t_topo, t_pe, t_img):
        camara(c, t, C, t_cx, t_topo, t_pe, t_img, g["xa"], g["ya"], g["ha"], g["x0"], g["y0"], g["x1"], g["y1"], g["furo"])

    def s10():
        E.frase(c, t, C["s10.a"], [("câmara", "g", 80, COR), ("escura", "g", 80, COR)], XE, 200)
        E.frase(c, t, C["s10.a"] + 0.6, ps("caixa fechada com um furo", "i", 58, TINTA2), XE, 290, passo=0.1)
        cena_cx(C["s10.a"], C["s10.b"], C["s10.d"], C["s10.e"])
        E.foco(c, t, C["s10.c"], 0.4, lambda a: E.escreve(c, "embaixo", g["x1"] + 30, yt + 15, 44, "i", TINTA2, a))
        E.foco(c, t, C["s10.d"] + 0.6, 0.4, lambda a: E.escreve(c, "em cima", g["x1"] + 30, yp + 15, 44, "i", TINTA2, a))
        pilula_em(c, t, C["s10.e"] + 0.2, "invertida", (g["x0"] + g["x1"]) / 2, g["y1"] + 90, 50, F.VEL)
    E.saida(c, t, C["s11"] - 0.1, s10)
    if C["s11"] <= t < C["s12"]:
        def s11():
            T0 = C["s11"] - 1.0
            cena_cx(T0, T0, T0, T0)
            q = ep(t, C["s11.a"], 0.6)
            if q > 0:
                for pts in (((g["xa"], g["ya"] - g["ha"]), (g["xa"], g["ya"]), (g["x0"], g["furo"])), ((g["x1"], yt), (g["x1"], yp), (g["x0"], g["furo"]))):
                    p = skia.Path(); p.moveTo(*pts[0]); p.lineTo(*pts[1]); p.lineTo(*pts[2]); p.close()
                    c.drawPath(p, M.paint(E.COR, 0.22 * q))
            E.frase(c, t, C["s11.a"], ps("dois triângulos", "i", 70) + [("semelhantes", "g", 70, COR)], XE, 200, passo=0.12)
            E.foco(c, t, C["s11.b"], 0.5, lambda a: fr_txt(c, "altura da imagem", "altura do objeto", 640, 975, 48, a))
            E.foco(c, t, C["s11.c"], 0.5, lambda a: (centro(c, "=", 1040, 995, 70, "g", TINTA2, a),
                                                     fr_txt(c, "profundidade da caixa", "distância até o objeto", 1440, 975, 48, a)))
        E.saida(c, t, C["s12"] - 0.1, s11)
    if C["s12"] <= t < C["s13"]:
        def s12():
            T0 = C["s12"] - 1.0
            cena_cx(T0, T0, T0, T0)
            # cotas: o (árvore), i (imagem), p (árvore→furo), p' (profundidade)
            imagem_i(c, t, C["s12.b"], g["x1"] + 50, yp, -(yt - yp), True)
            E.foco(c, t, C["s12.b"] + 0.3, 0.4, lambda a: E.escreve(c, "i", g["x1"] + 80, (yt + yp) / 2 + 22, 70, "g", F.VEL, a))
            objeto_o(c, t, C["s12.c"], g["xa"] - 250, g["ya"], g["ha"])
            E.foco(c, t, C["s12.c"] + 0.3, 0.4, lambda a: E.escreve(c, "o", g["xa"] - 230, g["ya"] - g["ha"] / 2 + 22, 70, "g", TINTA, a))
            E.segmento(c, t, C["s12.d"], (g["x0"], g["y1"] + 70), (g["x1"], g["y1"] + 70), "p'", cor=TINTA2, largura=4, lado=-1, size=52)
            E.segmento(c, t, C["s12.e"], (g["xa"], g["ya"] + 70), (g["x0"], g["ya"] + 70), "p", cor=TINTA2, largura=4, lado=-1, size=52)
            E.formula_em(c, t, C["s12.a"], "f{i}{o} = f{p'}{p}", XE, 300, 120, "g", TINTA)
        E.saida(c, t, C["s13"] - 0.1, s12)
    if t < C["s13"]:
        return
    # s13: o exemplo
    E.formula_em(c, t, C["s13"], "f{i}{o} = f{p'}{p}", XE, 250, 96, "g", TINTA2)
    linhas = (("s13.a", "o", "6 m"), ("s13.b", "p", "30 m"), ("s13.c", "p'", "20 cm"))
    for i, (k, l, v) in enumerate(linhas):
        y = 450 + 120 * i
        E.foco(c, t, C[k], 0.4, lambda a, l=l, v=v, y=y: (E.formula(c, l + " =", XE, y, 70, "g", COR, a), F.medida(c, *v.split(" "), XE + 200, y, 70, TINTA, a)))
    E.foco(c, t, C["s13.d"], 0.4, lambda a: (E.escreve(c, "→ 600 cm", XE + 420, 450, 62, "b", COR, a)))
    E.foco(c, t, C["s13.d"] + 1.4, 0.4, lambda a: (E.escreve(c, "→ 3.000 cm", XE + 420, 570, 62, "b", COR, a)))
    E.formula_em(c, t, C["s13.e"], "f{i}{600} = f{20}{3.000}", 1080, 470, 96, "g", TINTA)
    E.formula_em(c, t, lerp(C["s13.e"], C["s13.f"], 0.5), "i = f{600 · 20}{3.000}", 1080, 720, 84, "g", TINTA)
    bola_txt(c, t, C["s13.f"], "4 cm", 1560, 860, 120, 70)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s14"], [("cuidado", "g", 96, ERRADO)], XE, 200)
    E.frase(c, t, C["s14.a"], ps("misturar unidades", "i", 76), XE + 480, 200, passo=0.12)
    E.formula_em(c, t, C["s14.b"], "f{i}{6} = f{20}{30}", XE + 40, 470, 110, "g", TINTA)
    E.foco(c, t, C["s14.b"] + 1.0, 0.4, lambda a: (E.pilula(c, "cm", 780, 370, 40, "b", fundo=ERRADO, a=a), E.pilula(c, "m", 780, 540, 40, "b", fundo=ERRADO, a=a)))
    E.foco(c, t, C["s14.c"], 0.5, lambda a: E.escreve(c, "i = 4 m ?", XE + 40, 720, 110, "g", ERRADO, a))
    if t >= C["s14.c"] + 0.8:
        E.risco(c, XE + 20, 740, XE + 560, 640, t, C["s14.c"] + 0.8, largura=12)
    # a árvore de 4 m não cabe na caixa
    E.foco(c, t, C["s14.d"], 0.5, lambda a: (caixa(c, 1180, 560, 1640, 860, 710, a), arvore(c, 1560, 860, 600, a * 0.9)))
    E.foco(c, t, C["s14.d"] + 0.6, 0.4, lambda a: E.selo(c, 1760, 360, 60, False, a))
    pilula_em(c, t, C["s14.e"], "mesma unidade em cima e embaixo", W / 2, 960, 50, E.COR)


# ---------------- atalho (palco) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def s15():
        E.frase(c, t, C["s15"], ps("agora, o atalho", "i", 76, CLARO), W / 2, 170, "center")
        E.frase(c, t, C["s15.a"], [("distância", "g", 80, BR), ("÷", "g", 80, CLARO), ("profundidade", "g", 80, BR)], W / 2, 330, "center", 0.15)
        E.foco(c, t, C["s15.b"], 0.5, lambda a: centro(c, "3.000 ÷ 20 = 150", W / 2, 500, 100, "g", BR, a))
        E.frase(c, t, C["s15.c"], ps("a imagem é", "i", 70, CLARO) + [("150 vezes menor", "g", 70, BR)], W / 2, 650, "center", 0.12)
        E.foco(c, t, C["s15.d"], 0.5, lambda a: centro(c, "600 cm ÷ 150 =", W / 2 - 150, 860, 84, "g", CLARO, a))
        bola_txt(c, t, C["s15.d"] + 0.8, "4 cm", W / 2 + 330, 835, 110, 64)
    E.saida(c, t, C["s16"] - 0.1, s15)
    if t < C["s16"]:
        return
    E.frase(c, t, C["s16.a"], ps("triângulos semelhantes:", "i", 64, CLARO) + [("tudo encolhe igual", "g", 64, BR)], W / 2, 190, "center", 0.12)
    # aproxime a caixa: a imagem cresce
    E.frase(c, t, C["s16.b"], ps("caixa mais perto,", "i", 60, CLARO) + [("imagem maior", "g", 60, BR)], W / 2, 330, "center", 0.12)
    if t >= C["s16.b"]:
        a = ep(t, C["s16.b"], 0.5)
        q = ease_io(prog(t, C["s16.b"] + 0.6, 1.6))
        xa, ya, ha = 520, 840, 330
        x0 = lerp(1250, 950, q)
        x1, furo = x0 + 260, 700
        k = (x1 - x0) / (x0 - xa)
        yt, yp = furo + (furo - (ya - ha)) * k, furo + (furo - ya) * k
        arvore(c, xa, ya, ha, a)
        M.line(c, x0, furo - 130, x0, furo - 10, BR, a, 6); M.line(c, x0, furo + 10, x0, furo + 150, BR, a, 6)
        M.line(c, x0, furo - 130, x1, furo - 130, BR, a, 6); M.line(c, x0, furo + 150, x1, furo + 150, BR, a, 6); M.line(c, x1, furo - 130, x1, furo + 150, BR, a, 6)
        M.line(c, xa, ya - ha, x1, yt, E.COR, a, 4); M.line(c, xa, ya, x1, yp, E.COR, a, 4)
        M.line(c, x1 - 6, yp, x1 - 6, yt, CLARO, a, 12)
    E.frase(c, t, C["s16.c"], [("divisão não exata?", "g", 56, BR)] + ps("monte a proporção", "i", 58, CLARO), W / 2, 980, "center", 0.12)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s17"], ps("hora de testar", "i", 72, COR), XE, 190)
    E.foco(c, t, C["s17.a"], 0.4, lambda a: (E.escreve(c, "caixa:", XE, 330, 62, "i", TINTA, a), F.medida(c, 15, "cm", XE + 230, 330, 72, COR, a)))
    E.foco(c, t, C["s17.b"], 0.4, lambda a: (E.escreve(c, "distância:", XE, 450, 62, "i", TINTA, a), F.medida(c, 18, "m", XE + 330, 450, 72, COR, a)))
    E.foco(c, t, C["s17.c"], 0.4, lambda a: (E.escreve(c, "imagem:", XE, 570, 62, "i", TINTA, a), F.medida(c, 5, "cm", XE + 270, 570, 72, COR, a)))
    E.frase(c, t, C["s17.d"], ps("altura do", "i", 74) + [("poste?", "g", 74, COR)], XE, 730, passo=0.12)
    E.frase(c, t, C["s17.e"], [("direita", "g", 64), ("ou", "i", 70), ("invertida?", "g", 64, COR)], XE, 860, passo=0.15)
    if t < C["s18"]:
        def cena(a):
            M.rrect(c, 1140, 420, 16, 440, 6, TINTA, a)
            c.drawCircle(1148, 420, 22, M.paint(LUZ, a))
            caixa(c, 1500, 560, 1760, 760, 660, a)
            M.line(c, 1040, 860, 1840, 860, TINTA, a, 5)
        E.foco(c, t, C["s17.b"], 0.5, cena)
    questao_relogio(c, t, C, "s18")


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    def s19():
        E.frase(c, t, C["s19.a"], [("18 m", "g", 76), ("=", "g", 76, TINTA2), ("1.800 cm", "g", 76, COR)], XE, 230, passo=0.15)
        E.foco(c, t, C["s19.b"], 0.5, lambda a: E.escreve(c, "1.800 ÷ 15 = 120", XE, 400, 90, "g", TINTA, a))
        E.frase(c, t, C["s19.b"] + 1.2, ps("o poste é", "i", 58, TINTA2) + [("120 vezes maior", "g", 58, COR)], XE, 500, passo=0.1)
        E.foco(c, t, C["s19.c"], 0.5, lambda a: E.escreve(c, "5 × 120 = 600 cm", XE, 680, 90, "g", TINTA, a))
        bola_txt(c, t, C["s19.d"], "6 m", 1500, 560, 170, 100)
    E.saida(c, t, C["s20"] - 0.1, s19)
    if t < C["s20"]:
        return
    E.frase(c, t, C["s20"], ps("e a imagem é", "i", 80), XE, 260)
    pilula_em(c, t, C["s20.a"], "INVERTIDA", XE + 300, 420, 84, F.VEL)
    E.frase(c, t, C["s20.b"], ps("os raios se", "i", 64) + [("cruzam no furo", "g", 64, COR)], XE, 610, passo=0.12)
    camara(c, t, C, C["s20"] + 0.2, C["s20.b"], C["s20.b"] + 0.3, C["s20.b"] + 1.0, 1030, 940, 260, 1380, 640, 1760, 880, 760)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def r():
        resumo(c, t, C, "s21", [("s21.a", [("luz em", "i"), ("linha reta", "g", 62, COR)]),
                                ("s21.b", [("sombra:", "g"), ("nenhum raio;", "i"), ("penumbra:", "g"), ("parte", "i")]),
                                ("s21.c", [("câmara:", "g"), ("invertida,", "i"), ("i ÷ o = p' ÷ p", "g", 62, COR)])], y0=380, dy=200)
    E.saida(c, t, C["s22"] - 0.1, r)
    if t < C["s22"]:
        return

    def desenho():
        y = 900
        F.espelho_plano(c, t, C["s22.b"], (330, y), (1050, y), lado=-1)
        F.normal(c, t, C["s22.b"] + 0.3, (690, y), 90, 150)
        F.raio(c, t, C["s22.b"] + 0.6, [(450, y - 200), (690, y), (930, y - 200)], d=1.0)
    proxima(c, t, C, "s22", [("a luz", "i", 100), ("bate e volta", "g", 100, COR)], [("reflexão", "g", 80), ("e espelho plano", "i", 80)], desenho)


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, reta=b_reta, sombra=b_sombra, eclipse=b_eclipse, camara=b_camara,
              erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
