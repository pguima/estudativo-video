"""Visual — Estudativo · FIS-DIN-007: força de atrito, estático e cinético, e o freio ABS.
Linguagem visual da trilha de Dinâmica: cabeçalho do visual.py da FIS-DIN-001. Nesta aula: F_at sai da base do corpo,
rente ao chão, contra o deslizamento; o gráfico atrito × força aplicada mostra a rampa do estático até μe·N e a queda para
μc·N. Todo instante vem de C[...]."""
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
ARQUIVO_FINAL = "estudativo_FIS-DIN-007_forca_de_atrito_estatico_e_cinetico.mp4"
CORTINAS = E.carregar_cortinas(__file__, ("atrito", "estatico", "cinetico", "abs", "erro", "atalho", "questao", "fim"))

# todas as contas da aula (g = 10 m/s²)
assert 40 * 10 == 400 and round(0.6 * 400) == 240 and round(0.4 * 400) == 160
assert 300 - 160 == 140 and 140 / 40 == 3.5
assert round(0.8 * 10) == 8 and 20 ** 2 / (2 * 8) == 25 and 20 ** 2 / (2 * 5) == 40 and 40 - 25 == 15
assert 200 - 240 == -40  # o erro: sobraria 40 N para trás
assert 50 * 10 == 500 and 0.5 * 500 == 250 and 200 < 250

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
def armario(c, cx, yb, w, h, a=1.0, cor="#8B5E3C"):
    """armário de pé com a base em yb"""
    if a <= 0:
        return
    M.rrect(c, cx - w / 2, yb - h, w, h, 10, cor, a)
    M.line(c, cx, yb - h + 12, cx, yb - 12, "#5E3D24", a, 4)
    for d in (-1, 1):
        c.drawCircle(cx + d * 22, yb - h * 0.5, 7, M.paint("#E0C08A", a))


def lupa(c, cx, cy, r, a=1.0):
    """detalhe ampliado do contato: duas superfícies serrilhadas que se prendem"""
    if a <= 0:
        return
    c.save()
    pth = skia.Path(); pth.addCircle(cx, cy, r)
    c.clipPath(pth, doAntiAlias=True)
    c.drawCircle(cx, cy, r, M.paint("#FFFFFF", a))
    for k, (y0, cor, d) in enumerate(((cy, "#8B5E3C", -1), (cy, "#7A7A80", 1))):
        p = skia.Path()
        p.moveTo(cx - r, y0 + d * r)
        x = cx - r
        i = 0
        while x <= cx + r + 30:
            yy = y0 + (14 if (i + k) % 2 else -14)
            p.lineTo(x, yy)
            x += 28
            i += 1
        p.lineTo(cx + r, y0 + d * r)
        p.close()
        c.drawPath(p, M.paint(cor, a))
    c.restore()
    c.drawCircle(cx, cy, r, M.paint(TINTA, a, stroke=6))


def roda(c, cx, cy, r, a=1.0, giro=0.0):
    if a <= 0:
        return
    c.drawCircle(cx, cy, r, M.paint("#1B1B20", a))
    c.drawCircle(cx, cy, r * 0.5, M.paint("#9A9AA2", a))
    for k in range(5):
        g = math.radians(giro + k * 72)
        M.line(c, cx, cy, cx + math.cos(g) * r * 0.48, cy + math.sin(g) * r * 0.48, "#1B1B20", a, 4)


def caixa_atrito(c, t, t0, cx, yb, w, h, rot, empurra, atrito, cor=None):
    """bloco no chão com a força aplicada (empurra = (t, comp, rótulo/módulo)) e o atrito na base (atrito = (t, comp, módulo))"""
    E.foco(c, t, t0, 0.5, lambda a: F.bloco(c, cx, yb - h / 2, w, h, rot, cor or TINTA2, a, size=min(56, h * 0.36)))
    if t >= t0:
        F.chao(c, cx - w * 1.7, cx + w * 1.7, yb, ep(t, t0, 0.4))
    if empurra:
        ti, comp, mod = empurra
        seta_f(c, t, ti, (cx + w / 2, yb - h / 2), 0, comp, "F", modulo=mod, lpos=(cx + w / 2 + comp / 2 + 30, yb - h / 2 - 50), size=50)
    if atrito:
        ti, comp, mod = atrito
        seta_f(c, t, ti, (cx - w / 2 + 10, yb - 6), 180, comp, "F_{at}", modulo=mod, lpos=(cx - w / 2 - comp / 2 - 30, yb + 70), size=50)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    if t < C["s02"]:
        def um():
            yb = 860
            dx = 0 if t < C["s01.b"] else min(260, 0.5 * 200 * (t - C["s01.b"]) ** 2)
            E.foco(c, t, C["s01.a"], 0.5, lambda a: (armario(c, 1350 + dx, yb, 240, 420, a), pessoa(c, 1080 + dx, yb, 90, a, inclina=30, braco=10)))
            if t >= C["s01.a"]:
                F.chao(c, 900, 1850, yb, ep(t, C["s01.a"], 0.4))
            E.frase(c, t, C["s01.a"], [("parado:", "i", 72), ("difícil", "g", 72, ERRADO)], XE, 280, passo=0.12)
            E.frase(c, t, C["s01.b"], [("deslizando:", "i", 72), ("mais", "g", 72, CERTO), ("fácil", "g", 72, CERTO)], XE, 420, passo=0.12)
            E.frase(c, t, C["s01.c"], ps("e o mesmo motivo explica o", "i", 56, TINTA2), XE, 620, passo=0.08)
            pilula_em(c, t, C["s01.c"] + 0.8, "freio ABS", XE + 200, 740, 70, E.COR)
        E.saida(c, t, C["s02"] - 0.1, um)
        return
    promessa(c, t, C, "s02", (("s02.b", "calcular o atrito", 0), ("s02.c", "se move ou não", 0), ("s02.d", "o freio ABS", 0)))


def b_lembrete(c, t, C, b):
    lembrete(c, t, C, "s03", (("s03.b", "a normal,", "no chão plano, N = m · g"), ("s03.c", "segunda lei,", "resultante = m × a")))


# ---------------- atrito ----------------
def b_atrito(c, t, C, b):
    if t < C["s05"]:
        E.frase(c, t, C["s04.a"], [("atrito", "g", 100, COR)] + ps("= o chão contra o deslizamento", "i", 64), XE, 230, passo=0.12)
        caixa_atrito(c, t, C["s04.a"], 1100, 700, 260, 200, None, (C["s04.a"] + 0.6, 200, None), (C["s04.b"], 200, None))
        E.frase(c, t, C["s04.b"], ps("paralelo ao chão", "i", 58, TINTA2), XE, 900, passo=0.1)
        E.frase(c, t, C["s04.c"], ps("contra o deslizamento", "g", 58), XE, 990, passo=0.1)
        E.foco(c, t, C["s04.d"], 0.6, lambda a: lupa(c, 1620, 330, 150, a))
        if t >= C["s04.d"]:
            M.line(c, 1000, 700, 1500, 420, TINTA2, ep(t, C["s04.d"], 0.4) * 0.6, 3, dash=E.TRACO)
        E.foco(c, t, C["s04.d"] + 0.6, 0.4, lambda a: E.escreve(c, "asperezas que se prendem", 1440, 540, 40, "i", TINTA2, a))
        return
    E.frase(c, t, C["s05.a"], ps("depende de duas coisas", "i", 72), XE, 220, passo=0.12)
    formula_nova(c, t, C["s05.b"], "F_{at} = μ · N", XE, 420, 150, (("N", "normal: o quanto aperta", "N"), ("μ", "o material, sem unidade", None)),
                 (C["s05.b"] + 0.5, C["s05.c"]))
    E.foco(c, t, C["s05.d"], 0.5, lambda a: E.pilula(c, "μ = 0,4  (só um número)", 1450, 520, 54, "g", fundo=TINTA, a=a))


# ---------------- estático ----------------
def b_estatico(c, t, C, b):
    if t < C["s07"]:
        E.frase(c, t, C["s06.a"], ps("parado:", "i", 72) + [("estático", "g", 72, COR)], XE, 220, passo=0.12)
        E.frase(c, t, C["s06.b"], [("ele", "i", 72), ("se", "i", 72), ("ajusta", "g", 72, COR)], XE, 340, passo=0.12)
        k = 2.0 if t >= C["s06.d"] else 1.0
        mod = "200 N" if k > 1 else "100 N"
        caixa_atrito(c, t, C["s06.a"], 1300, 760, 260, 200, None, (C["s06.c"], 100 * k, mod), (C["s06.c"] + 0.4, 100 * k, mod))
        E.foco(c, t, C["s06.e"], 0.5, lambda a: sub(c, "até o máximo: F_{at,máx} = μ_{e} · N", XE, 970, 70, "g", COR, a))
        return
    E.frase(c, t, C["s07.a"], [("armário", "i", 72)], XE, 210)
    E.foco(c, t, C["s07.a"] + 0.3, 0.5, lambda a: F.medida(c, 40, "kg", XE + 300, 210, 76, COR, a))
    contas(c, t, [(C["s07.b"], "N = 40 · 10 = 400 N"), (C["s07.c"], "μ_{e} = 0,6"), (C["s07.d"], "F_{at,máx} = 0,6 · 400 = 240 N", COR)], XE, 360, 70, 110)
    yb = 900
    E.foco(c, t, C["s07.a"], 0.5, lambda a: armario(c, 1500, yb, 200, 340, a))
    if t >= C["s07.a"]:
        F.chao(c, 1150, 1850, yb, ep(t, C["s07.a"], 0.4))
    seta_f(c, t, C["s07.e"], (1600, yb - 170), 0, 160, "F", modulo="200 N", lpos=(1700, yb - 230), size=46)
    seta_f(c, t, C["s07.f"], (1410, yb - 6), 180, 160, "F_{at}", modulo="200 N", lpos=(1300, yb + 70), size=46)
    E.frase(c, t, C["s07.f"], [("200", "g", 64), ("<", "g", 64, COR), ("240:", "g", 64)] + ps("não se move", "g", 60, CERTO), XE, 740, passo=0.1)
    E.frase(c, t, C["s07.g"], ps("para sair:", "i", 60) + ps("mais de 240 N", "g", 60, COR), XE, 860, passo=0.1)


# ---------------- cinético ----------------
def b_cinetico(c, t, C, b):
    if t < C["s09"]:
        E.frase(c, t, C["s08.a"], ps("deslizando:", "i", 72) + [("cinético", "g", 72, COR)], XE, 220, passo=0.12)
        E.foco(c, t, C["s08.b"], 0.5, lambda a: sub(c, "F_{at} = μ_{c} · N", XE, 370, 90, "g", TINTA, a))
        E.frase(c, t, C["s08.b"] + 1.2, ps("sempre o mesmo valor", "i", 54, TINTA2), XE, 460, passo=0.1)
        E.foco(c, t, C["s08.c"], 0.5, lambda a: sub(c, "μ_{c} < μ_{e}", XE, 620, 96, "g", COR, a))
        E.frase(c, t, lerp(C["s08.c"], C["s08.end"], 0.5), ps("mais fácil depois que anda", "i", 52, TINTA2), XE, 730, passo=0.08)
        P = F.grafico(c, t, C["s08.a"] + 0.4, 1020, 300, 760, 560, 0, 400, 0, 300, "força aplicada (N)", "atrito (N)", 100, 100)
        E.curva(c, t, C["s08.a"] + 1.0, P, lambda x: x, 0, 240, d=1.0)
        if t >= C["s08.c"]:
            M.line(c, P.x(240), P.y(240), P.x(240), P.y(160), E.COR, ep(t, C["s08.c"], 0.4), 5, dash=E.TRACO)
        E.curva(c, t, C["s08.c"] + 0.3, P, lambda x: 160, 240, 400, d=0.8)
        E.foco(c, t, C["s08.a"] + 1.8, 0.4, lambda a: E.pilula(c, "estático: se ajusta", P.x(110), P.y(250), 34, "b", fundo=TINTA2, a=a))
        E.foco(c, t, C["s08.c"] + 0.8, 0.4, lambda a: E.pilula(c, "cinético: constante", P.x(320), P.y(210), 34, "b", fundo=E.COR, a=a))
        return
    E.frase(c, t, C["s09"], ps("no armário", "i", 66), XE, 210)
    contas(c, t, [(C["s09.a"], "μ_{c} = 0,4"), (C["s09.b"], "F_{at} = 0,4 · 400 = 160 N"), (C["s09.d"], "F_{R} = 300 − 160 = 140 N"), (C["s09.e"], "a = 140 ÷ 40")],
           XE, 360, 70, 120)
    bola_txt(c, t, C["s09.e"] + 1.0, "3,5 m/s^2", 1550, 860, 140, 54)
    yb = 640
    dx = 0 if t < C["s09.c"] else min(160, 0.5 * 120 * (t - C["s09.c"]) ** 2)
    E.foco(c, t, C["s09"], 0.5, lambda a: armario(c, 1300 + dx, yb, 180, 300, a))
    if t >= C["s09"]:
        F.chao(c, 1100, 1850, yb, ep(t, C["s09"], 0.4))
    seta_f(c, t, C["s09.c"], (1390 + dx, yb - 150), 0, 200, "F", modulo="300 N", lpos=(1490 + dx, yb - 210), size=44)
    seta_f(c, t, C["s09.b"], (1220 + dx, yb - 6), 180, 110, "F_{at}", modulo="160 N", lpos=(1120 + dx, yb + 60), size=44)


# ---------------- ABS ----------------
def b_abs(c, t, C, b):
    if t < C["s11"]:
        E.frase(c, t, C["s10"], ps("agora, o freio", "i", 72) + [("ABS", "g", 72, COR)], XE, 200, passo=0.12)
        for i, (k, tit, sub_, giro_on, cor, nome) in enumerate((("s10.a", "sem ABS:", "a roda trava e desliza", False, ERRADO, "cinético: menor"),
                                                                ("s10.c", "com ABS:", "a roda gira, sem deslizar", True, CERTO, "estático: maior"))):
            x = 170 + i * 820
            p = ep(t, C[k], 0.5)
            E.caixa_pontilhada(c, x, 300, 760, 640, p, prog_=p)
            E.frase(c, t, C[k] + 0.1, [(tit, "g", 60, cor)], x + 40, 390)
            E.frase(c, t, C[k] + 0.5, ps(sub_, "i", 48), x + 40, 470, passo=0.06)
            g = (t - C[k]) * 400 if (giro_on and t >= C[k]) else 0
            E.foco(c, t, C[k] + 0.6, 0.5, lambda a, x=x, g=g: roda(c, x + 380, 680, 120, a, g))
            if t >= C[k] + 0.6:
                F.chao(c, x + 120, x + 640, 800, ep(t, C[k] + 0.6, 0.4))
                if not giro_on:
                    for j in range(4):
                        M.line(c, x + 140 + j * 50, 810, x + 180 + j * 50, 810, TINTA2, 0.6 * ep(t, C[k] + 0.6, 0.4), 6)
            tk = C["s10.b"] if i == 0 else C["s10.e"]
            E.foco(c, t, tk, 0.5, lambda a, x=x, nome=nome, cor=cor: E.pilula(c, nome, x + 380, 890, 46, "g", fundo=cor, a=a))
        return
    E.foco(c, t, C["s11.a"], 0.5, lambda a: sub(c, "a = μ · g", XE, 220, 96, "g", TINTA, a))
    E.frase(c, t, C["s11.a"] + 0.8, ps("(você vê no atalho)", "i", 46, TINTA2), XE + 520, 210, passo=0.08)
    vx = lambda d: 360 + d * 32
    for i, (k, kd, rot, mu, d, cor) in enumerate((("s11.b", "s11.c", "com ABS", "μ = 0,8 → a = 8", 25, CERTO), ("s11.d", "s11.e", "travado", "μ = 0,5 → a = 5", 40, ERRADO))):
        y = 500 + i * 260
        E.frase(c, t, C[k], [(rot, "g", 54, cor)], XE, y - 90)
        E.foco(c, t, C[k] + 0.3, 0.5, lambda a, mu=mu, y=y: sub(c, mu, XE + 330, y - 90, 50, "g", TINTA2, a))
        if t >= C[k]:
            M.line(c, vx(0), y, vx(45), y, TINTA, ep(t, C[k], 0.4), 5)
        q = ease_out(prog(t, C[kd] - 0.8, 1.2))
        E.foco(c, t, C[k] + 0.2, 0.4, lambda a, q=q, d=d, y=y: F.carrinho(c, lerp(vx(0), vx(d), q), y, 180, a=a))
        if t >= C[kd]:
            E.foco(c, t, C[kd], 0.4, lambda a, d=d, y=y, cor=cor: (M.line(c, vx(d), y - 140, vx(d), y + 20, cor, a, 5),
                                                                 F.medida(c, d, "m", vx(d) + 20, y + 70, 56, cor, a)))
    E.foco(c, t, C["s11.f"], 0.5, lambda a: E.pilula(c, "15 m de diferença", 1500, 960, 56, "g", fundo=E.COR, a=a))
    E.foco(c, t, C["s11.b"] + 1.0, 0.5, lambda a: sub(c, "d = v^2 ÷ (2 · a)", 1320, 220, 64, "g", TINTA2, a))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s12"], [("cuidado", "g", 96, ERRADO)], XE, 200)
    E.frase(c, t, C["s12.a"], ps("usar", "i", 64) + [("μe · N", "g", 60, ERRADO)] + ps("sempre", "i", 64), XE, 330, passo=0.12)
    yb = 760
    E.foco(c, t, C["s12.b"], 0.5, lambda a: armario(c, 1350, yb, 220, 360, a))
    if t >= C["s12.b"]:
        F.chao(c, 1000, 1800, yb, ep(t, C["s12.b"], 0.4))
    seta_f(c, t, C["s12.b"] + 0.3, (1460, yb - 180), 0, 160, "F", modulo="200 N", lpos=(1560, yb - 240), size=46)
    seta_f(c, t, C["s12.c"], (1250, yb - 6), 180, 192, "F_{at}", modulo="240 N", cor=ERRADO, lpos=(1140, yb + 70), size=46)
    E.foco(c, t, C["s12.c"], 0.5, lambda a: sub(c, "F_{at} = 240 N ?", XE, 500, 76, "g", ERRADO, a))
    E.frase(c, t, C["s12.d"], ps("sobrariam", "i", 58) + [("40 N", "g", 56, ERRADO)] + ps("para trás:", "i", 58), XE, 640, passo=0.1)
    E.frase(c, t, C["s12.d"] + 1.6, ps("andaria sozinho para trás", "i", 58, TINTA2), XE, 730, passo=0.1)
    E.foco(c, t, C["s12.e"], 0.5, lambda a: sub(c, "μ · N é só o limite", XE, 900, 80, "g", CERTO, a))


# ---------------- atalho (palco) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def s13():
        E.frase(c, t, C["s13"], ps("agora, o atalho", "i", 76, CLARO), W / 2, 160, "center")
        E.frase(c, t, C["s13.a"], ps("chão plano, só o atrito freando", "i", 62, CLARO), W / 2, 310, "center", 0.1)
        E.foco(c, t, C["s13.b"], 0.5, lambda a: sub(c, "a = μ · g", W / 2, 520, 180, "g", BR, a, "center"))
        E.frase(c, t, C["s13.c"], ps("a massa nem entra", "g", 62, BR), W / 2, 680, "center", 0.12)
        E.foco(c, t, C["s13.d"], 0.5, lambda a: sub(c, "μ = 0,5  →  a = 5 m/s^2", W / 2, 860, 84, "g", CLARO, a, "center"))
        E.frase(c, t, C["s13.e"], ps("para qualquer carro", "i", 56, CLARO), W / 2, 970, "center", 0.1)
    E.saida(c, t, C["s14"] - 0.1, s13)
    if t < C["s14"]:
        return
    E.frase(c, t, C["s14.a"], ps("funciona porque", "i", 64, CLARO), W / 2, 230, "center", 0.1)
    E.foco(c, t, C["s14.a"] + 0.4, 0.5, lambda a: sub(c, "a = f{μ · m · g}{m} = μ · g", W / 2, 420, 100, "g", BR, a, "center"))
    E.frase(c, t, C["s14.b"], ps("a massa corta", "g", 60, BR), W / 2, 580, "center", 0.1)
    E.frase(c, t, C["s14.c"], [("não", "g", 60, ERRADO), ("compensa:", "i", 62, CLARO)] + ps("outra força empurrando junto", "i", 62, CLARO), W / 2, 790, "center", 0.1)
    E.frase(c, t, C["s14.d"], ps("ou normal diferente do peso", "i", 62, CLARO), W / 2, 900, "center", 0.1)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    cabeca_q(c, t, C, "s15")
    E.foco(c, t, C["s15.a"], 0.5, lambda a: (E.escreve(c, "caixa", XE, 330, 64, "i", TINTA, a), F.medida(c, 50, "kg", XE + 200, 330, 76, COR, a),
                                             E.escreve(c, "parada", XE + 450, 330, 60, "i", TINTA2, a)))
    E.foco(c, t, C["s15.b"], 0.5, lambda a: sub(c, "μ_{e} = 0,5", XE, 460, 72, "g", TINTA, a))
    E.foco(c, t, C["s15.c"], 0.5, lambda a: sub(c, "μ_{c} = 0,3", XE + 400, 460, 72, "g", TINTA, a))
    E.foco(c, t, C["s15.d"], 0.5, lambda a: (E.escreve(c, "empurra com", XE, 590, 60, "i", TINTA, a), F.medida(c, 200, "N", XE + 360, 590, 76, COR, a)))
    E.frase(c, t, C["s15.e"], ps("se move?", "g", 72, COR), XE, 760, passo=0.12)
    E.frase(c, t, C["s15.f"], [("atrito", "g", 72), ("=", "g", 72), ("?", "g", 72, COR)], XE, 880, passo=0.12)

    def desenho():
        caixa_atrito(c, t, C["s15.a"], 1480, 760, 260, 200, "50 kg", (C["s15.d"], 160, "200 N"), None)
    pausa(c, t, C, "s16", desenho)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    contas(c, t, [(C["s17.a"], "N = 50 · 10 = 500 N"), (C["s17.b"], "F_{at,máx} = 0,5 · 500 = 250 N"), (C["s17.c"], "200 < 250")], XE, 220, 72, 120)
    E.frase(c, t, C["s17.d"], ps("não se move", "g", 70, CERTO), XE, 620, passo=0.12)
    E.foco(c, t, C["s17.d"] + 0.3, 0.4, lambda a: E.selo(c, XE + 520, 595, 40, True, a))
    bola_txt(c, t, C["s17.e"], "200 N", 1500, 420, 150, 70)
    pilula_em(c, t, C["s17.e"] + 0.6, "atrito estático", 1500, 640, 46, TINTA)
    E.foco(c, t, C["s17.f"], 0.5, lambda a: sub(c, "μ_{c} = 0,3: só para confundir", XE, 860, 66, "g", TINTA2, a))
    risca_em(c, t, C["s17.f"] + 0.8, XE - 10, 875, XE + 330, 815)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    resumo(c, t, C, "s18", (("s18.a", [("parado:", "i", 64), ("se", "i", 64), ("ajusta", "g", 60, COR), ("até", "i", 64), ("μe · N", "g", 60)]),
                            ("s18.b", [("deslizando:", "i", 64), ("μc · N", "g", 60, COR)]),
                            ("s18.c", [("ABS:", "g", 60, COR), ("estático,", "i", 64), ("o", "i", 64), ("maior", "g", 60)])), C["s19"])
    if t < C["s19"]:
        return

    def desenho():
        R = F.plano_inclinado(c, t, C["s19.a"], 330, 960, 640, 30)
        if t >= C["s19.a"] + 0.6:
            E.foco(c, t, C["s19.a"] + 0.6, 0.5, lambda a: F.bloco_rampa(c, R, 0.55, 150, 110, None, a))
        if t >= C["s19.b"]:
            cxy = F.bloco_rampa(c, R, 0.55, 150, 110, None, 0)
            seta_f(c, t, C["s19.b"], cxy, -90, 160, "P", lpos=(cxy[0] + 60, cxy[1] + 200), size=46)
    proxima(c, t, C, "s19", ((C["s19.a"], [("Plano", "g", 110, COR), ("inclinado", "g", 110)]),), "s19.d", "s19.e", desenho)


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, atrito=b_atrito, estatico=b_estatico, cinetico=b_cinetico, abs=b_abs,
              erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
