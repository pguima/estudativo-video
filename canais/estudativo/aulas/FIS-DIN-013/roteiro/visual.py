"""Visual — Estudativo · FIS-DIN-013: praticando atrito, planos e curvas (cinco situações). Última aula da trilha de Dinâmica.
Linguagem visual da trilha de Dinâmica: cabeçalho do visual.py da FIS-DIN-001. Prática: cada situação tem a tela da
questão (texto à esquerda, desenho à direita, relógio na pausa) e a tela da resposta (contas uma por fala, resultado na esfera).
Todo instante vem de C[...]."""
import math
import re

import editorial as E
import fisica as F
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Física", "Dinâmica")
COR, CLARO = E.COR_TEXTO, E.CLARO
MARCA = ""
BACKGROUND = E.fundo
BR = "#FFFFFF"
ARQUIVO_FINAL = "estudativo_FIS-DIN-013_praticando_atrito_planos_e_curvas.mp4"
CORTINAS = E.carregar_cortinas(__file__, ("questao1", "questao2", "questao3", "atalho", "questao4", "questao5", "fim"))

# todas as contas da aula (g = 10 m/s²; rampa "sen 0,8 / cos 0,6")
assert 30 * 10 == 300 and round(0.4 * 300) == 120 and 150 > 120 and round(0.3 * 300) == 90 and (150 - 90) / 30 == 2
assert round(0.5 * 0.6, 9) == 0.3 and round(0.8 - 0.3, 9) == 0.5 and round(10 * 0.5, 9) == 5
assert round(10 * (0.6 - 0.5 * 0.8), 9) == 2  # o erro: trocar seno por cosseno
assert 2 * 10 == 20 and 0.5 * 30 == 15 and (20 - 15) / (3 + 2) == 1 and 15 + 3 * 1 == 18 and (20 - 18) / 2 == 1
assert round(0.5 * 10 * 45) == 225 and 225 ** 0.5 == 15 and round(15 * 3.6) == 54
assert (10 * 40) ** 0.5 == 20 and round(20 * 3.6) == 72
TH = math.degrees(math.asin(0.8))  # rampa da situação 2, cerca de 53°

def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças da trilha de Dinâmica (iguais em todas as aulas FIS-DIN; candidatas a fisica.py) ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def _partes_sub(s):
    return [(p, i % 2 == 1) for i, p in enumerate(re.split(r"_\{([^}]*)\}", s)) if p]


def sub(c, s, x, y, size, est="g", cor=None, a=1.0, align="left"):
    """fórmula com subscrito: "F_{R} = m · a", "F_{at} = μ · N". Aceita a escrita de E.formula nos trechos. Devolve a largura"""
    partes = _partes_sub(s)
    ws = [E.formula(None, p, 0, 0, size * (0.6 if b else 1), E._est(p, est), a=0) + (size * 0.03 if b else 0) for p, b in partes]
    w = sum(ws)
    if c is not None and a > 0:
        xi = x - w / 2 if align == "center" else x - w if align == "right" else x
        for (p, b), wi in zip(partes, ws):
            E.formula(c, p, xi, y + (size * 0.2 if b else 0), size * (0.6 if b else 1), E._est(p, est), cor or TINTA, a)
            xi += wi
    return w


def sub_em(c, t, t0, s, x, y, size, est="g", cor=None, align="left"):
    E.foco(c, t, t0, 0.5, lambda a: sub(c, s, x, y, size, est, cor, a, align))


def contas(c, t, linhas, x, y0, size=80, dy=None, align="left", est="g"):
    """uma conta por linha, cada uma na sua fala: linhas = [(instante, texto[, cor])]"""
    dy = dy or size * 1.35
    for i, li in enumerate(linhas):
        sub_em(c, t, li[0], li[1], x, y0 + i * dy, size, est, li[2] if len(li) > 2 else TINTA, align)


def bola_txt(c, t, t0, s, cx, cy, r, size, cor=None):
    """resposta na esfera: "20 m/s" com a unidade menor"""
    v, _, u = s.partition(" ")
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r * ease_back(prog(t, t0, 0.5)), cor, a),
                                     F.medida(c, v, u, cx, cy + size * 0.36, size, E.SOBRE, a, "center", cor_u=E.SOBRE)))


def troca(c, t, itens, fn):
    """um de cada vez: itens = [(instante, arg)], cada um sai quando o próximo chega; fn(arg, a) desenha"""
    for i, (ti, s) in enumerate(itens):
        fim = itens[i + 1][0] - 0.1 if i + 1 < len(itens) else 1e9
        if t >= ti - 0.01:
            E.saida(c, t, fim, lambda s=s, ti=ti: E.foco(c, t, ti, 0.45, lambda a: fn(s, a)), d=0.25)


def pilula_em(c, t, t0, s, cx, cy, size, fundo=None, est="g"):
    E.foco(c, t, t0, 0.4, lambda a: E.pilula(c, s, cx, cy, size, est, fundo=fundo, a=a, cor=BR))


def rot_vetor(c, s, cx, yb, size, cor, a):
    """letra de força (com subscrito: "F_{R}") e a setinha de vetor sobre a letra principal; cx = centro, yb = linha de base"""
    w = sub(None, s, 0, 0, size)
    if c is None or a <= 0:
        return w
    x0 = cx - w / 2
    sub(c, s, x0, yb, size, "g", cor, a)
    wb = sub(None, s.split("_{")[0], 0, 0, size)
    ys, hw, mx = yb - size * 0.98, wb / 2 + size * 0.04, x0 + wb / 2
    M.line(c, mx - hw, ys, mx + hw - size * 0.05, ys, cor, a, max(3, size * 0.07))
    F._cabeca(c, mx + hw + size * 0.06, ys, 1, 0, size * 0.2, cor, a)
    return w


def seta_f(c, t, t0, P, ang, comp, rot=None, cor=None, modulo=None, lpos=None, size=56, larg=9, escuro=False, d=0.5):
    """força que sai de P no ângulo ang (graus, 90 = para cima) com comp px; rótulo (letra e/ou módulo) com centro em lpos
    (x, linha de base). Sem lpos, o rótulo fica depois da ponta. Devolve a ponta"""
    dx, dy = F._dir(ang)
    B = (P[0] + dx * comp, P[1] + dy * comp)
    if t < t0:
        return B
    cor = cor or E.COR
    F.seta(c, *P, *B, cor, 1.0, larg, p=ease_out(prog(t, t0, d)))
    if rot or modulo:
        if lpos is None:
            lpos = (B[0] + dx * size * 1.1, B[1] + dy * size * 0.9 + size * 0.36)
        cr = (E.CLARO if escuro else E.COR_TEXTO) if cor == E.COR else cor
        tinta = BR if escuro else TINTA

        def lab(a):
            v, _, u = (modulo or "").partition(" ")
            w1 = rot_vetor(None, rot, 0, 0, size, cr, 0) if rot else 0
            w2 = F.medida(None, v, u, 0, 0, size * 0.8) if modulo else 0
            gap = size * 0.4 if rot and modulo else 0
            x0 = lpos[0] - (w1 + gap + w2) / 2
            if rot:
                rot_vetor(c, rot, x0 + w1 / 2, lpos[1], size, cr, a)
            if modulo:
                F.medida(c, v, u, x0 + w1 + gap, lpos[1], size * 0.8, tinta, a, escuro=escuro)
        E.foco(c, t, t0 + d * 0.7, 0.4, lab)
    return B


def lembrete(c, t, C, cena, itens):
    """'você precisa de N coisas' à esquerda e uma caixa por item, cada uma no seu cue: itens = [(cue, linha fina, linha forte)]"""
    n = len(itens)
    E.frase(c, t, C[cena] + 0.2, ps("você precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C[cena + ".a"], 0.5, lambda a: E.escreve(c, str(n), XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C[cena + ".a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 820, 1000
    h, gap, y0 = (230, 290, 200) if n == 2 else (200, 240, 120)
    for i, (k, l1, l2) in enumerate(itens):
        y = y0 + i * gap
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, h, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 56)], x + 44, y + h * 0.42)
        E.frase(c, t, C[k] + 0.3, [(l2, "g", 56, COR)], x + 44, y + h * 0.42 + 80)
    ult = itens[-1][0]
    E.frase(c, t, lerp(C[ult], C[cena + ".end"], 0.6), ps("faltou alguma?", "i", 52, COR) + ps("procure no canal", "i", 52),
            x, y0 + (n - 1) * gap + h + 90, "left", 0.12)


def promessa(c, t, C, cena, itens):
    """'até o fim da aula' + itens numerados (curtos) + a órbita da Física: itens = [(cue, texto, atraso)]"""
    tb = C[cena + ".a"] + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1500, 560, 300 * ease_back(prog(t, tb, 0.8)), giro=12 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, C[cena + ".a"], ps("até o fim da aula", "i", 88), XE, 260, passo=0.14)
    dy = 150 if len(itens) <= 3 else 128
    for i, (k, s, dt) in enumerate(itens):
        y = 430 + i * dy
        E.foco(c, t, C[k] + dt, 0.5, lambda a, i=i, y=y: (E.bola(c, XE + 40, y - 28, 38, a=a),
                                                       centro(c, str(i + 1), XE + 40, y - 6, 48, "g", BR, a)))
        E.frase(c, t, C[k] + dt + 0.1, [(s, "g", 72, COR if i == 0 else TINTA)], XE + 110, y)


def pausa(c, t, C, cena_p, desenho, cx=1460, cy=440):
    """na cena da pausa, o desenho da questão dá lugar ao relógio"""
    if t < C[cena_p]:
        desenho()
    else:
        E.relogio(c, t, C[cena_p + ".a"], cx=cx, cy=cy, r=200)


def cabeca_q(c, t, C, cena, texto="hora de testar"):
    E.frase(c, t, C[cena], ps(texto, "i", 72, COR), XE, 190)


def resumo(c, t, C, cena, itens, t_fim):
    """'resumindo' + itens numerados: itens = [(cue, partes de E.frase)]; some em t_fim"""
    def fn():
        E.frase(c, t, C[cena], [("resumindo", "i", 92, COR)], W / 2, 180, "center")
        dy = 170 if len(itens) <= 4 else 140
        for i, (k, partes) in enumerate(itens):
            y = 350 + i * dy
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 260, y - 26, 52, a=a), centro(c, str(i + 1), 260, y - 4, 60, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, partes, 360, y, passo=0.1)
    E.saida(c, t, t_fim - 0.1, fn)


def proxima(c, t, C, cena, linhas, insc, bons, desenho=None):
    """ponte para a próxima aula: linhas = [(instante, partes)], desenho(a) embaixo à esquerda; pílula Inscreva-se e despedida"""
    E.frase(c, t, C[cena], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    for i, (ti, partes) in enumerate(linhas):
        E.frase(c, t, ti, partes, XE, 400 + i * 140, passo=0.12)
    if desenho:
        desenho()
    E.foco(c, t, C[insc], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 420, 76, estilo="g", a=a))
    p = ease_io(prog(t, C[insc] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(720, 445, p), ep(t, C[insc] + 0.2, 0.4))
    E.frase(c, t, C[bons], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1570, 990, "center")


def formula_nova(c, t, t0, s, x, y, size, legendas, tl, size_l=54, dy=None):
    """fórmula nova: grande em tinta e, embaixo, cada letra em laranja + nome + (unidade do SI), cada linha em tl[i]"""
    sub_em(c, t, t0, s, x, y, size, "g", TINTA)
    dy = dy or size_l * 1.5
    for i, (letra, nome, unid) in enumerate(legendas):
        yy = y + size * 0.5 + size_l * 1.4 + i * dy

        def lin(a, letra=letra, nome=nome, unid=unid, yy=yy):
            wl = sub(c, letra, x, yy, size_l * 1.1, "g", COR, a)
            xx = x + max(wl, size_l * 0.9) + size_l * 0.5
            E.escreve(c, nome, xx, yy, size_l, "i", TINTA, a)
            if unid:
                E.formula(c, f"({unid})", xx + E.larg(nome, "i", size_l) + size_l * 0.4, yy, size_l * 0.9, "b", F.UNID, a)
        E.foco(c, t, tl[i], 0.5, lin)


def risca_em(c, t, t0, x0, y0, x1, y1, larg_=10):
    if t >= t0:
        E.risco(c, x0, y0, x1, y1, t, t0, largura=larg_)


# ---------------- desenhos de apoio ----------------
def pessoa(c, x, y, s, a=1.0, cor=None, inclina=0.0, braco=None, sentido=1):
    """pessoa de traço: pés em y, altura ~3,4·s. inclina = graus para a frente; braco = ângulo dos braços (graus, 0 = para a frente)"""
    if a <= 0:
        return
    cor = cor or TINTA2
    sg = 1 if sentido > 0 else -1
    g = math.radians(inclina) * sg
    quadril = (x, y - 1.5 * s)
    ombro = (quadril[0] + math.sin(g) * 1.3 * s, quadril[1] - math.cos(g) * 1.3 * s)
    cabeca = (ombro[0] + math.sin(g) * 0.55 * s, ombro[1] - math.cos(g) * 0.55 * s)
    lw = max(5, s * 0.2)
    for dx in (-0.35, 0.35):
        M.line(c, *quadril, x + dx * s + sg * s * 0.25 * (inclina / 30), y, cor, a, lw)
    M.line(c, *quadril, *ombro, cor, a, lw)
    br = math.radians(braco if braco is not None else -70)
    for k in (0, 0.18):
        M.line(c, *ombro, ombro[0] + sg * math.cos(br + k) * 1.2 * s, ombro[1] - math.sin(br + k) * 1.2 * s, cor, a, lw)
    c.drawCircle(*cabeca, 0.36 * s, M.paint(cor, a))


def polia(c, cx, cy, r, a=1.0, suporte=None):
    """roldana com eixo; suporte = (x, y) do ponto de fixação (desenha a haste até lá)"""
    if a <= 0:
        return
    if suporte:
        M.line(c, cx, cy, *suporte, TINTA2, a, 8)
    c.drawCircle(cx, cy, r, M.paint("#C9C9C4", a))
    c.drawCircle(cx, cy, r, M.paint(TINTA, a, stroke=6))
    c.drawCircle(cx, cy, r * 0.62, M.paint(TINTA2, a * 0.5, stroke=3))
    c.drawCircle(cx, cy, r * 0.16, M.paint(TINTA, a))


def balanca_chao(c, cx, y, w, texto, a=1.0):
    """balança de banheiro com o visor; y = topo da balança (onde a pessoa pisa)"""
    if a <= 0:
        return
    h = w * 0.16
    M.rrect(c, cx - w / 2, y, w, h, h * 0.35, "#E4E4E0", a)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2, y, w, h), h * 0.35, h * 0.35), M.paint(TINTA2, a, stroke=4))
    vw, vh = w * 0.42, h * 0.62
    M.rrect(c, cx - vw / 2, y + (h - vh) / 2, vw, vh, 8, "#1B1B20", a)
    v, _, u = texto.partition(" ")
    F.medida(c, v, u, cx, y + h / 2 + vh * 0.3, vh * 0.72, "#7CFFB2", a, "center", cor_u="#7CFFB2")


def elevador(c, x, y, w, h, a=1.0):
    """cabine de elevador com o cabo; (x, y) = canto de cima à esquerda"""
    if a <= 0:
        return
    M.line(c, x + w / 2, y - 260, x + w / 2, y, TINTA2, a, 6)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 14, 14), M.paint("#FFFFFF", 0.55 * a))
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 14, 14), M.paint(TINTA, a, stroke=6))


# ---------------- peças desta aula ----------------
MADEIRA = "#8B5E3C"


def pilulas(c, t, t0, itens, x, y, size, fundo, passo=0.3):
    """pílulas lado a lado, posicionadas pela largura de cada uma"""
    for i, s in enumerate(itens):
        w = E.larg(s, "g", size) + size * 1.1
        E.foco(c, t, t0 + passo * i, 0.4, lambda a, s=s, x=x, w=w: E.pilula(c, s, x + w / 2, y, size, "g", fundo=fundo, a=a))
        x += w + 24


def situacao(c, t, C, cena, n):
    E.frase(c, t, C[cena + ".a"], [("situação", "i", 72, TINTA2), (str(n), "g", 80, COR)], XE, 200, passo=0.12)


def mesa_polia(c, t, t0, x0, y, L, mA, mB, wA=190, hA=140, wB=140, hB=120):
    """mesa com bloco A, polia na borda e bloco B pendurado; devolve centros de A e B"""
    q = ep(t, t0, 0.5)
    pr = 32
    px, py = x0 + L, y - pr
    ax, ay = x0 + L * 0.4, y - hA / 2
    by = y + 150
    if q > 0:
        M.rrect(c, x0, y, L, 26, 6, MADEIRA, q)
        M.rrect(c, x0 + 30, y + 22, 26, 240, 5, "#6E4A2F", q)
        M.line(c, ax + wA / 2, py - pr, px, py - pr, TINTA2, q, 5)
        M.line(c, px + pr, py, px + pr, by - hB / 2, TINTA2, q, 5)
        polia(c, px, py, pr, q, (x0 + L - 10, y + 8))
        F.bloco(c, ax, ay, wA, hA, mA, TINTA2, q, size=44)
        F.bloco(c, px + pr, by, wB, hB, mB, E.COR, q, size=42)
    return (ax, ay), (px + pr, by)


def carro_tras(c, cx, yb, w, a=1.0):
    if a <= 0:
        return
    cor = E.COR
    h = w * 0.62
    for dx in (-0.36, 0.36):
        M.rrect(c, cx + dx * w - w * 0.09, yb - w * 0.2, w * 0.18, w * 0.2, 6, "#1B1B20", a)
    M.rrect(c, cx - w / 2, yb - h * 0.75, w, h * 0.55, w * 0.06, cor, a)
    p = skia.Path()
    p.moveTo(cx - w * 0.36, yb - h * 0.74); p.lineTo(cx - w * 0.26, yb - h); p.lineTo(cx + w * 0.26, yb - h); p.lineTo(cx + w * 0.36, yb - h * 0.74); p.close()
    c.drawPath(p, M.paint(E.mix(cor, "#000000", 0.12), a))
    M.rrect(c, cx - w * 0.24, yb - h * 0.96, w * 0.48, h * 0.18, 6, E.mix(cor, "#FFFFFF", 0.75), a)


def lombada(c, t, t0, cx, yb, R, meia):
    q = ep(t, t0, 0.6)
    if q <= 0:
        return
    ang = math.degrees(math.asin(meia / R))
    C0 = (cx, yb + R)
    c.drawArc(skia.Rect.MakeXYWH(C0[0] - R, C0[1] - R, 2 * R, 2 * R), -90 - ang, 2 * ang, False, M.paint(TINTA, q, stroke=8))
    yl = C0[1] - R * math.cos(math.radians(ang))
    M.line(c, cx - meia - 180, yl, cx - meia, yl, TINTA, q, 8)
    M.line(c, cx + meia, yl, cx + meia + 180, yl, TINTA, q, 8)


# ---------------- abertura ----------------
def b_gancho(c, t, C, b):
    E.frase(c, t, C["s01.a"], [("5", "g", 220, COR), ("situações", "i", 110)], XE, 400, passo=0.14)
    pilulas(c, t, C["s01.b"], ("atrito", "rampa", "blocos", "curvas"), XE, 560, 52, E.COR)
    E.foco(c, t, C["s01.c"], 0.6, lambda a: E.relogio(c, t, C["s01.c"], cx=1500, cy=430, r=160), blur=0)
    E.frase(c, t, C["s01.c"] + 2.4, ps("o fechamento da", "i", 66) + [("Dinâmica", "g", 66, COR)], XE, 820, passo=0.12)


def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s02.a"], ps("quatro ferramentas", "i", 76), XE, 200, passo=0.12)
    itens = (("s02.b", "atrito:", "F_{at} = μ · N"), ("s02.c", "rampa:", "seno puxa, cosseno aperta"), ("s02.d", "blocos:", "um corpo só"),
             ("s02.e", "curva:", "resultante = m · f{v^2}{R}"))
    for i, (k, l1, l2) in enumerate(itens):
        y = 380 + i * 160
        E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, XE + 40, y - 26, 40, a=a), centro(c, str(i + 1), XE + 40, y - 4, 50, "g", BR, a)))
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 62)], XE + 110, y)
        sub_em(c, t, C[k] + 0.3, l2, XE + 400, y, 62, "g", COR)


# ---------------- situação 1 ----------------
def b_questao1(c, t, C, b):
    situacao(c, t, C, "s03", 1)
    E.foco(c, t, C["s03.b"], 0.5, lambda a: (E.escreve(c, "caixa de", XE, 340, 62, "i", TINTA, a), F.medida(c, 30, "kg", XE + 270, 340, 76, COR, a),
                                             E.escreve(c, "parada", XE + 520, 340, 58, "i", TINTA2, a)))
    E.foco(c, t, C["s03.c"], 0.5, lambda a: sub(c, "μ_{e} = 0,4   μ_{c} = 0,3", XE, 470, 66, "g", TINTA, a))
    E.foco(c, t, C["s03.d"], 0.5, lambda a: (E.escreve(c, "empurra com", XE, 600, 60, "i", TINTA, a), F.medida(c, 150, "N", XE + 360, 600, 76, COR, a)))
    E.frase(c, t, C["s03.e"], ps("se move?", "g", 70, COR), XE, 760, passo=0.12)
    E.frase(c, t, C["s03.f"], [("a", "g", 70, F.ACEL), ("=", "g", 70), ("?", "g", 70, COR)], XE + 400, 760, passo=0.12)

    def desenho():
        E.foco(c, t, C["s03.b"], 0.5, lambda a: F.bloco(c, 1450, 650, 260, 200, "30 kg", TINTA2, a, size=54))
        if t >= C["s03.b"]:
            F.chao(c, 1100, 1800, 750, ep(t, C["s03.b"], 0.4))
        seta_f(c, t, C["s03.d"], (1580, 650), 0, 190, "F", modulo="150 N", lpos=(1680, 590), size=48)
    pausa(c, t, C, "s04", desenho)


def b_resposta1(c, t, C, b):
    contas(c, t, [(C["s05.a"], "N = 30 · 10 = 300 N"), (C["s05.b"], "F_{at,máx} = 0,4 · 300 = 120 N"), (C["s05.c"], "150 > 120: se move", CERTO),
                  (C["s05.d"], "F_{at} = 0,3 · 300 = 90 N"), (C["s05.e"], "F_{R} = 150 − 90 = 60 N"), (C["s05.f"], "a = 60 ÷ 30")], XE, 200, 62, 104)
    bola_txt(c, t, C["s05.f"] + 0.6, "2 m/s^2", 1500, 560, 160, 66)


# ---------------- situação 2 ----------------
def b_questao2(c, t, C, b):
    situacao(c, t, C, "s06", 2)
    E.frase(c, t, C["s06.b"], ps("um bloco desce a rampa", "i", 62), XE, 340, passo=0.1)
    E.foco(c, t, C["s06.b"] + 0.8, 0.5, lambda a: sub(c, "sen θ = 0,8   cos θ = 0,6", XE, 470, 64, "g", TINTA, a))
    E.foco(c, t, C["s06.c"], 0.5, lambda a: sub(c, "μ_{c} = 0,5", XE, 590, 64, "g", TINTA, a))
    E.frase(c, t, C["s06.d"], [("a", "g", 72, F.ACEL), ("=", "g", 72), ("?", "g", 72, COR)], XE, 760, passo=0.12)

    def desenho():
        R = F.plano_inclinado(c, t, C["s06.b"], 1220, 920, 480, TH)
        if t >= C["s06.b"] + 0.4:
            F.bloco_rampa(c, R, 0.55, 120, 90, None, ep(t, C["s06.b"] + 0.4, 0.4), TINTA2)
    pausa(c, t, C, "s07", desenho)


def b_resposta2(c, t, C, b):
    E.frase(c, t, C["s08"], ps("a massa nem foi dada: não precisa", "i", 58, TINTA2), XE, 200, passo=0.08)
    contas(c, t, [(C["s08.a"], "a = g · (sen θ − μ · cos θ)"), (C["s08.b"], "0,5 · 0,6 = 0,3"), (C["s08.c"], "0,8 − 0,3 = 0,5")], XE, 360, 72, 130)
    bola_txt(c, t, C["s08.d"], "5 m/s^2", 1500, 520, 160, 66)
    E.foco(c, t, C["s08.e"], 0.5, lambda a: sub(c, "trocou? 10 · (0,6 − 0,5 · 0,8) = 2", XE, 900, 62, "g", ERRADO, a))
    risca_em(c, t, C["s08.e"] + 1.6, XE - 10, 915, XE + 1080, 855)


# ---------------- situação 3 ----------------
def b_questao3(c, t, C, b):
    situacao(c, t, C, "s09", 3)
    E.foco(c, t, C["s09.b"], 0.5, lambda a: (E.escreve(c, "na mesa:", XE, 340, 60, "i", TINTA, a), F.medida(c, 3, "kg", XE + 260, 340, 72, COR, a),
                                             sub(c, "μ_{c} = 0,5", XE + 450, 340, 62, "g", TINTA, a)))
    E.foco(c, t, C["s09.c"], 0.5, lambda a: (E.escreve(c, "pendurado:", XE, 470, 60, "i", TINTA, a), F.medida(c, 2, "kg", XE + 310, 470, 72, COR, a)))
    E.frase(c, t, C["s09.c"] + 2.4, ps("o sistema já anda", "i", 54, TINTA2), XE, 580, passo=0.1)
    E.frase(c, t, C["s09.d"], [("a", "g", 72, F.ACEL), ("=", "g", 72), ("?", "g", 72, COR)], XE, 760, passo=0.12)
    E.frase(c, t, C["s09.e"], [("T", "g", 72), ("=", "g", 72), ("?", "g", 72, COR)], XE + 300, 760, passo=0.12)

    def desenho():
        mesa_polia(c, t, C["s09.b"], 1080, 520, 600, "3 kg", "2 kg")
    pausa(c, t, C, "s10", desenho)


def b_resposta3(c, t, C, b):
    A, B = mesa_polia(c, t, C["s11"], 1150, 420, 560, "3 kg", "2 kg")
    seta_f(c, t, C["s11.a"], (B[0], B[1] + 60), -90, 130, "P", modulo="20 N", lpos=(B[0] - 150, B[1] + 150), size=44)
    seta_f(c, t, C["s11.b"], (A[0] - 95, 414), 180, 110, "F_{at}", modulo="15 N", lpos=(A[0] - 120, 520), size=44)
    contas(c, t, [(C["s11.a"], "a favor: 20 N"), (C["s11.b"], "contra: 0,5 · 30 = 15 N"), (C["s11.c"], "a = (20 − 15) ÷ 5 = 1 m/s^2", F.ACEL),
                  (C["s11.d"], "T − 15 = 3 · 1"), (C["s11.f"], "pendurado: (20 − 18) ÷ 2 = 1", CERTO)], XE, 200, 60, 110)
    bola_txt(c, t, C["s11.e"], "18 N", 1500, 900, 110, 58)


# ---------------- atalho (palco) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    E.frase(c, t, C["s12"], ps("o atalho que une as três primeiras", "i", 68, CLARO), W / 2, 180, "center", 0.1)
    E.foco(c, t, C["s12.a"], 0.5, lambda a: sub(c, "a = f{a favor − contra}{massas que andam}", W / 2, 440, 100, "g", BR, a, "center"))
    for i, s in enumerate(("atrito", "P · sen θ", "peso pendurado")):
        E.foco(c, t, C["s12.c"] + 0.4 * i, 0.4, lambda a, i=i, s=s: E.pilula(c, s, 560 + i * 420, 700, 50, "g", fundo=E.COR, a=a))
    E.frase(c, t, C["s12.d"], ps("antes, no atrito:", "i", 60, CLARO) + ps("ele sai do lugar?", "g", 60, BR), W / 2, 900, "center", 0.1)


# ---------------- situação 4 ----------------
def b_questao4(c, t, C, b):
    situacao(c, t, C, "s13", 4)
    E.frase(c, t, C["s13.b"], ps("curva plana", "i", 64), XE, 340, passo=0.1)
    E.foco(c, t, C["s13.b"] + 0.6, 0.5, lambda a: sub(c, "R = 45 m", XE, 470, 76, "g", COR, a))
    E.foco(c, t, C["s13.c"], 0.5, lambda a: sub(c, "μ_{e} = 0,5", XE, 590, 76, "g", COR, a))
    E.frase(c, t, C["s13.d"], ps("velocidade máxima", "g", 64) + ps("em km/h?", "i", 64, COR), XE, 760, passo=0.12)

    def desenho():
        E.foco(c, t, C["s13.b"], 0.5, lambda a: carro_tras(c, 1450, 760, 300, a))
        if t >= C["s13.b"]:
            F.chao(c, 1100, 1800, 760, ep(t, C["s13.b"], 0.4))
        E.foco(c, t, C["s13.b"] + 0.5, 0.4, lambda a: E.pilula(c, "← centro da curva", 1350, 380, 40, "b", fundo=TINTA2, a=a))
    pausa(c, t, C, "s14", desenho)


def b_resposta4(c, t, C, b):
    E.frase(c, t, C["s15.a"], ps("o atrito estático faz a centrípeta", "i", 58, TINTA2), XE, 200, passo=0.08)
    contas(c, t, [(C["s15.b"], "v^2 = μ · g · R"), (C["s15.c"], "v^2 = 0,5 · 10 · 45 = 225"), (C["s15.d"], "v = r{225} = 15 m/s")], XE, 360, 74, 140)
    E.foco(c, t, C["s15.e"], 0.5, lambda a: sub(c, "15 · 3,6", XE, 840, 62, "g", TINTA2, a))
    bola_txt(c, t, C["s15.e"] + 0.4, "54 km/h", 1500, 560, 170, 62)


# ---------------- situação 5 ----------------
def b_questao5(c, t, C, b):
    situacao(c, t, C, "s16", 5)
    E.frase(c, t, C["s16.b"], ps("topo de uma lombada de", "i", 60), XE, 340, passo=0.1)
    E.foco(c, t, C["s16.b"] + 1.2, 0.5, lambda a: F.medida(c, 40, "m", XE, 470, 80, COR, a))
    E.frase(c, t, C["s16.c"], ps("maior velocidade", "g", 64), XE, 640, passo=0.12)
    E.frase(c, t, C["s16.c"] + 1.4, ps("sem perder o contato?", "i", 64, COR), XE, 740, passo=0.12)

    def desenho():
        lombada(c, t, C["s16.b"], 1450, 560, 360, 260)
        E.foco(c, t, C["s16.b"] + 0.4, 0.4, lambda a: F.carrinho(c, 1450, 560, 220, a=a))
    pausa(c, t, C, "s17", desenho)


def b_resposta5(c, t, C, b):
    contas(c, t, [(C["s18.a"], "P − N = m · f{v^2}{R}"), (C["s18.b"], "perder o contato: N = 0"), (C["s18.c"], "v = r{g · R}"), (C["s18.d"], "v = r{10 · 40} = r{400}")],
           XE, 220, 70, 140)
    bola_txt(c, t, C["s18.e"], "20 m/s", 1500, 420, 130, 58)
    E.foco(c, t, C["s18.e"] + 1.0, 0.4, lambda a: E.pilula(c, "72 km/h", 1500, 600, 50, "g", fundo=TINTA, a=a))
    E.foco(c, t, C["s18.c"] + 0.6, 0.4, lambda a: E.pilula(c, "a mesma do topo do looping", 1350, 900, 44, "b", fundo=E.COR, a=a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    resumo(c, t, C, "s19", (("s19.a", [("desenhe", "g", 64), ("as", "i", 66), ("forças", "i", 66)]),
                            ("s19.b", [("rampa:", "i", 66), ("decomponha", "g", 62, COR), ("o", "i", 66), ("peso", "i", 66)]),
                            ("s19.c", [("blocos:", "i", 66), ("um", "g", 62, COR), ("corpo", "g", 62, COR), ("só", "g", 62, COR)]),
                            ("s19.d", [("curva:", "i", 66), ("marque", "g", 62), ("o", "i", 66), ("centro", "g", 62, COR)])), C["s20"])
    if t < C["s20"]:
        return
    E.frase(c, t, C["s20.a"], ps("você fechou a", "i", 80), XE, 250, passo=0.12)
    E.frase(c, t, C["s20.a"] + 0.6, [("Dinâmica", "g", 130, COR)], XE, 420)
    pilulas(c, t, C["s20.b"], ("3 leis", "atrito", "rampas", "curvas"), XE, 560, 50, TINTA, 0.4)
    E.frase(c, t, lerp(C["s20.b"], C["s20.c"], 0.6), ps("a seguir: a trilha de", "i", 58, TINTA2) + [("energia", "g", 58, COR)], XE, 720, passo=0.1)
    E.foco(c, t, C["s20.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 420, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s20.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(720, 445, p), ep(t, C["s20.c"] + 0.2, 0.4))
    E.frase(c, t, C["s20.d"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1570, 990, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, questao1=b_questao1, resposta1=b_resposta1, questao2=b_questao2, resposta2=b_resposta2,
              questao3=b_questao3, resposta3=b_resposta3, atalho=b_atalho, questao4=b_questao4, resposta4=b_resposta4,
              questao5=b_questao5, resposta5=b_resposta5, fim=b_fim)
