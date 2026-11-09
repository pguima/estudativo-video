"""Visual — Estudativo · FIS-DIN-011: carro na curva (curva plana com atrito e curva inclinada sem atrito).
Linguagem visual da trilha de Dinâmica: cabeçalho do visual.py da FIS-DIN-001. Nesta aula o carro é visto DE TRÁS, com o
centro da curva à esquerda (pílula "centro ←"): P para baixo, N do chão, F_at ou a parte horizontal da normal para o centro.
Componentes da normal em laranja claro com tracejado, como na decomposição do peso (FIS-DIN-008). Todo instante vem de C[...]."""
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
ARQUIVO_FINAL = "estudativo_FIS-DIN-011_carro_na_curva.mp4"
CORTINAS = E.carregar_cortinas(__file__, ("plana", "inclinada", "erro", "atalho", "questao", "fim"))

# todas as contas da aula (g = 10 m/s²)
assert round(0.8 * 10 * 50) == 400 and 400 ** 0.5 == 20 and round(20 * 3.6) == 72
assert round(0.2 * 10 * 50) == 100 and 100 ** 0.5 == 10 and round(10 * 3.6) == 36 and 40 > 36
assert round(math.tan(math.radians(45)), 9) == 1 and 10 * 90 == 900 and 900 ** 0.5 == 30 and round(30 * 3.6) == 108
assert round(400 * 3.6) == 1440
assert round(0.5 * 10 * 125) == 625 and 625 ** 0.5 == 25 and round(25 * 3.6) == 90

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
CLARA = E.mix(E.COR, "#FFFFFF", 0.35)


def carro_tras(c, cx, yb, w, a=1.0, giro=0.0, cor=None):
    """carro visto de trás, apoiado em yb (centro da base em cx), girado giro graus (positivo = anti-horário na tela)"""
    if a <= 0:
        return
    cor = cor or E.COR
    c.save(); c.translate(cx, yb); c.rotate(-giro)
    h = w * 0.62
    for dx in (-0.36, 0.36):
        M.rrect(c, dx * w - w * 0.09, -w * 0.2, w * 0.18, w * 0.2, 6, "#1B1B20", a)
    M.rrect(c, -w / 2, -h * 0.75, w, h * 0.55, w * 0.06, cor, a)
    p = skia.Path()
    p.moveTo(-w * 0.36, -h * 0.74); p.lineTo(-w * 0.26, -h); p.lineTo(w * 0.26, -h); p.lineTo(w * 0.36, -h * 0.74); p.close()
    c.drawPath(p, M.paint(E.mix(cor, "#000000", 0.12), a))
    M.rrect(c, -w * 0.24, -h * 0.96, w * 0.48, h * 0.18, 6, E.mix(cor, "#FFFFFF", 0.75), a)
    for dx in (-0.4, 0.4):
        M.rrect(c, dx * w - w * 0.06, -h * 0.6, w * 0.12, h * 0.1, 4, "#FFE08A" if dx > 0 else "#FF8A8A", a)
    c.restore()


def centro_seta(c, t, t0, x, y):
    E.foco(c, t, t0, 0.4, lambda a: E.pilula(c, "← centro da curva", x, y, 40, "b", fundo=TINTA2, a=a))


def pista_inclinada(c, t, t0, cx, cy, L, ang):
    """corte da pista inclinada: sobe para a direita com ângulo ang, centro do trecho em (cx, cy); devolve (A, B)"""
    q = ep(t, t0, 0.6)
    dx, dy = math.cos(math.radians(ang)), -math.sin(math.radians(ang))
    A = (cx - dx * L / 2, cy - dy * L / 2)
    B = (cx + dx * L / 2, cy + dy * L / 2)
    if q > 0:
        p = skia.Path(); p.moveTo(*A); p.lineTo(*B); p.lineTo(B[0], A[1]); p.close()
        c.drawPath(p, M.paint(TINTA2, 0.12 * q))
        M.line(c, *A, *B, TINTA, q, 8)
        M.line(c, A[0], A[1], B[0] + 60, A[1], TINTA2, q * 0.6, 4, dash=E.TRACO)
    return A, B


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    if t < C["s02"]:
        def um():
            for i, (k, rot, v, cor, ok) in enumerate((("s01.a", "seco", "72 km/h", CERTO, True), ("s01.b", "chuva", "40 km/h", ERRADO, False))):
                x = 1050 + i * 430
                E.foco(c, t, C[k], 0.5, lambda a, x=x: carro_tras(c, x, 760, 260, a))
                if t >= C[k]:
                    F.chao(c, x - 190, x + 190, 760, ep(t, C[k], 0.4))
                    if i == 1:
                        for j in range(6):
                            yy = 360 + ((t * 300 + j * 70) % 380)
                            M.line(c, x - 150 + j * 60, yy, x - 162 + j * 60, yy + 30, "#3B8DB5", 0.6 * ep(t, C[k], 0.4), 4)
                E.foco(c, t, C[k] + 0.4, 0.4, lambda a, x=x, rot=rot, v=v: (centro(c, rot, x, 850, 50, "i", TINTA2, a), F.medida(c, *v.split(), x, 940, 60, TINTA, a, "center")))
                E.foco(c, t, C[k] + 1.0, 0.4, lambda a, x=x, ok=ok: E.selo(c, x + 150, 420, 44, ok, a))
            E.frase(c, t, C["s01.a"], ps("a mesma curva", "i", 72), XE, 250, passo=0.12)
            E.frase(c, t, C["s01.c"], ps("e as pistas de corrida", "i", 60), XE, 520, passo=0.1)
            E.frase(c, t, C["s01.c"] + 1.4, [("inclinadas", "g", 70, COR)], XE, 620)
        E.saida(c, t, C["s02"] - 0.1, um)
        return
    promessa(c, t, C, "s02", (("s02.b", "curva plana", 0), ("s02.c", "curva inclinada", 0)))


def b_lembrete(c, t, C, b):
    lembrete(c, t, C, "s03", (("s03.b", "centrípeta,", "m · v² ÷ R"), ("s03.c", "atrito estático máximo,", "μ · N"), ("s03.d", "decompor,", "com seno e cosseno")))


# ---------------- curva plana ----------------
def b_plana(c, t, C, b):
    cx, yb = 1400, 760
    if t < C["s06"]:
        E.foco(c, t, C["s04"], 0.5, lambda a: carro_tras(c, cx, yb, 300, a))
        if t >= C["s04"]:
            F.chao(c, cx - 360, cx + 360, yb, ep(t, C["s04"], 0.4))
        centro_seta(c, t, C["s04.a"], cx - 100, 300)
        seta_f(c, t, C["s04.b"], (cx - 100, yb - 4), 180, 240, "F_{at}", lpos=(cx - 260, yb + 80), size=50)
        if t < C["s05"]:
            E.frase(c, t, C["s04.a"], ps("curva plana:", "i", 66) + ps("quem segura?", "g", 64), XE, 230, passo=0.12)
            E.frase(c, t, C["s04.b"], ps("o atrito do pneu", "g", 64, COR), XE, 360, passo=0.1)
            E.frase(c, t, C["s04.c"], [("estático:", "g", 62)] + ps("não escorrega de lado", "i", 60), XE, 480, passo=0.1)
            return
        seta_f(c, t, C["s05"], (cx + 40, yb - 140), -90, 150, "P", lpos=(cx + 110, yb - 20), size=46)
        seta_f(c, t, C["s05"] + 0.3, (cx + 100, yb - 4), 90, 150, "N", lpos=(cx + 170, yb - 120), size=46)
        E.frase(c, t, C["s05.a"], ps("no limite:", "i", 60) + ps("atrito máximo = centrípeta", "g", 56), XE, 220, passo=0.1)
        sub_em(c, t, C["s05.b"], "μ · m · g = m · f{v^2}{R}", XE, 400, 84, "g", TINTA)
        if t >= C["s05.c"]:
            w0 = sub(None, "μ · ", 0, 0, 84)
            wm = sub(None, "m", 0, 0, 84)
            w1 = sub(None, "μ · m · g = ", 0, 0, 84)
            risca_em(c, t, C["s05.c"], XE + w0 - 6, 415, XE + w0 + wm + 6, 350, 8)
            risca_em(c, t, C["s05.c"] + 0.2, XE + w1 - 6, 415, XE + w1 + wm + 6, 350, 8)
        sub_em(c, t, C["s05.d"], "v^2 = μ · g · R", XE, 580, 90, "g", TINTA)
        sub_em(c, t, C["s05.e"], "v = r{μ · g · R}", XE, 760, 120, "g", COR)
        return
    if t < C["s07"]:
        E.frase(c, t, C["s06.a"], [("seco:", "g", 66, CERTO)], XE, 220)
        E.foco(c, t, C["s06.a"] + 0.4, 0.5, lambda a: sub(c, "μ = 0,8   R = 50 m", XE + 230, 220, 66, "g", TINTA, a))
        contas(c, t, [(C["s06.b"], "v^2 = 0,8 · 10 · 50 = 400"), (C["s06.c"], "v = r{400} = 20 m/s")], XE, 400, 80, 150)
        bola_txt(c, t, C["s06.d"], "72 km/h", 1450, 560, 170, 60, CERTO)
        E.foco(c, t, C["s06.d"], 0.5, lambda a: sub(c, "20 · 3,6", XE, 720, 66, "g", TINTA2, a))
        return
    E.frase(c, t, C["s07.a"], [("chuva:", "g", 66, ERRADO)], XE, 220)
    E.foco(c, t, C["s07.a"] + 0.4, 0.5, lambda a: sub(c, "μ = 0,2   R = 50 m", XE + 250, 220, 66, "g", TINTA, a))
    contas(c, t, [(C["s07.b"], "v^2 = 0,2 · 10 · 50 = 100"), (C["s07.c"], "v = r{100} = 10 m/s")], XE, 400, 80, 150)
    bola_txt(c, t, C["s07.d"], "36 km/h", 1450, 560, 170, 60, ERRADO)
    E.foco(c, t, C["s07.e"], 0.5, lambda a: E.pilula(c, "metade da velocidade", 1450, 830, 50, "g", fundo=TINTA, a=a))


# ---------------- curva inclinada ----------------
def b_inclinada(c, t, C, b):
    ang = 25
    cx, cy = 1350, 720
    A, B = pista_inclinada(c, t, C["s08"], cx, cy, 760, ang)
    E.foco(c, t, C["s08"] + 0.3, 0.5, lambda a: carro_tras(c, cx, cy, 200, a, giro=ang))
    if t >= C["s08"] + 0.3:
        E.angulo(c, t, C["s08"] + 0.6, A, (A[0] + 200, A[1]), B, "θ", r=120, size=50)
    centro_seta(c, t, C["s08"] + 0.6, cx - 120, 1010)
    nx, ny = F._dir(90 + ang)
    G = (cx + nx * 140, cy + ny * 140)
    L = 260
    Nt = (G[0] + nx * L, G[1] + ny * L)
    if t < C["s10"]:
        if t >= C["s08.b"]:
            M.line(c, G[0], G[1], G[0], G[1] - L - 30, TINTA2, 0.5 * ep(t, C["s08.b"], 0.4), 4, dash=E.TRACO)
        seta_f(c, t, C["s08.c"], G, 90 + ang, L, "N", lpos=(Nt[0] - 50, Nt[1] - 30), size=50)
        if t >= C["s08.d"]:
            M.line(c, *Nt, G[0], Nt[1], TINTA2, 0.5 * ep(t, C["s08.d"], 0.4), 3, dash=E.TRACO)
            F.seta(c, *G, G[0], Nt[1], CLARA, 1.0, 8, p=ease_out(prog(t, C["s08.d"], 0.5)))
            E.foco(c, t, C["s08.d"] + 0.3, 0.4, lambda a: sub(c, "N · cos θ", G[0] + 24, Nt[1] + 70, 46, "g", E.COR_TEXTO, a))
        if t >= C["s08.e"]:
            M.line(c, *Nt, Nt[0], G[1], TINTA2, 0.5 * ep(t, C["s08.e"], 0.4), 3, dash=E.TRACO)
            F.seta(c, *G, Nt[0], G[1], CLARA, 1.0, 8, p=ease_out(prog(t, C["s08.e"], 0.5)))
            E.foco(c, t, C["s08.e"] + 0.3, 0.4, lambda a: sub(c, "N · sen θ", Nt[0] - 20, G[1] - 20, 46, "g", E.COR_TEXTO, a, "right"))
        if t < C["s09"]:
            E.frase(c, t, C["s08.a"], ps("pista inclinada:", "i", 64), XE, 220, passo=0.12)
            E.frase(c, t, C["s08.b"], ps("a normal", "i", 62) + [("tomba", "g", 62, COR)] + ps("para o centro", "i", 62), XE, 330, passo=0.1)
            E.frase(c, t, C["s08.d"], ps("vertical:", "i", 56) + ps("segura o peso", "g", 54), XE, 470, passo=0.1)
            E.frase(c, t, C["s08.e"], ps("horizontal:", "i", 56) + ps("faz a centrípeta", "g", 54, COR), XE, 570, passo=0.1)
            E.frase(c, t, C["s08.e"] + 1.2, ps("sem precisar do atrito", "i", 50, TINTA2), XE, 660, passo=0.08)
            return
        contas(c, t, [(C["s09.a"], "N · cos θ = m · g"), (C["s09.b"], "N · sen θ = m · f{v^2}{R}")], XE, 240, 66, 150)
        E.foco(c, t, C["s09.c"], 0.5, lambda a: sub(c, "÷: f{sen θ}{cos θ} = tg θ", XE, 600, 62, "g", TINTA2, a))
        E.foco(c, t, C["s09.d"], 0.5, lambda a: sub(c, "tg θ = f{v^2}{g · R}", XE, 820, 100, "g", COR, a))
        return
    E.frase(c, t, C["s10.a"], [("θ = 45°", "g", 62, COR)], XE, 220)
    E.foco(c, t, C["s10.a"] + 0.6, 0.5, lambda a: sub(c, "R = 90 m", XE + 330, 220, 62, "g", TINTA, a))
    contas(c, t, [(C["s10.b"], "tg 45° = 1"), (C["s10.c"], "v^2 = 10 · 90 = 900"), (C["s10.d"], "v = 30 m/s")], XE, 380, 72, 120)
    bola_txt(c, t, C["s10.d"] + 0.6, "108 km/h", 520, 860, 130, 46)
    E.foco(c, t, C["s10.e"], 0.5, lambda a: E.pilula(c, "mesmo com a pista lisa", 1150, 960, 46, "g", fundo=E.COR, a=a))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s11"], [("cuidado", "g", 96, ERRADO)], XE, 200)
    E.frase(c, t, C["s11.a"], ps("esquecer a", "i", 70) + [("raiz", "g", 70, ERRADO)], XE, 330, passo=0.12)
    E.foco(c, t, C["s11.b"], 0.5, lambda a: sub(c, "0,8 · 10 · 50 = 400", XE, 500, 80, "g", TINTA, a))
    E.foco(c, t, C["s11.c"], 0.5, lambda a: sub(c, "v = 400 m/s ?", XE, 640, 80, "g", ERRADO, a))
    E.foco(c, t, C["s11.d"], 0.5, lambda a: sub(c, "mais de 1.400 km/h", XE + 700, 640, 60, "g", ERRADO, a))
    risca_em(c, t, C["s11.d"] + 1.0, XE - 10, 660, XE + 600, 580)
    E.foco(c, t, C["s11.e"], 0.5, lambda a: sub(c, "v^2 = 400  →  v = 20 m/s", XE, 840, 90, "g", CERTO, a))


# ---------------- atalho (palco) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def s12():
        E.frase(c, t, C["s12"], ps("agora, o atalho", "i", 76, CLARO), W / 2, 160, "center")
        E.frase(c, t, C["s12.a"], ps("curva plana:", "i", 60, CLARO), 300, 360)
        sub_em(c, t, C["s12.a"] + 0.4, "v = r{μ · g · R}", 800, 370, 100, "g", BR)
        E.frase(c, t, C["s12.b"], ps("inclinada, sem atrito:", "i", 60, CLARO), 300, 560)
        sub_em(c, t, C["s12.b"] + 0.4, "v = r{g · R · tg θ}", 900, 570, 100, "g", BR)
        E.frase(c, t, C["s12.c"], ps("a massa", "i", 66, CLARO) + ps("nunca entra", "g", 66, BR), W / 2, 820, "center", 0.12)
        E.frase(c, t, C["s12.d"], ps("moto ou caminhão: o mesmo limite", "i", 56, CLARO), W / 2, 930, "center", 0.1)
    E.saida(c, t, C["s13"] - 0.1, s12)
    if t < C["s13"]:
        return
    E.frase(c, t, C["s13.a"], ps("todas as forças da curva têm a massa:", "i", 60, CLARO) + ps("ela corta", "g", 60, BR), W / 2, 300, "center", 0.1)
    E.frase(c, t, C["s13.b"], [("não", "g", 62, ERRADO), ("compensa:", "i", 64, CLARO)] + ps("inclinada e com atrito", "i", 64, CLARO), W / 2, 540, "center", 0.12)
    E.frase(c, t, C["s13.c"], ps("decomponha o atrito também", "g", 62, BR), W / 2, 700, "center", 0.12)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    cabeca_q(c, t, C, "s14")
    E.frase(c, t, C["s14.a"], ps("curva plana", "i", 66), XE, 330, passo=0.12)
    E.foco(c, t, C["s14.a"] + 0.8, 0.5, lambda a: sub(c, "R = 125 m", XE, 460, 80, "g", COR, a))
    E.foco(c, t, C["s14.b"], 0.5, lambda a: sub(c, "μ_{e} = 0,5", XE, 590, 80, "g", COR, a))
    E.frase(c, t, C["s14.c"], ps("velocidade máxima", "g", 66) + ps("em km/h?", "i", 66, COR), XE, 780, passo=0.12)

    def desenho():
        E.foco(c, t, C["s14.a"], 0.5, lambda a: carro_tras(c, 1450, 760, 300, a))
        if t >= C["s14.a"]:
            F.chao(c, 1100, 1800, 760, ep(t, C["s14.a"], 0.4))
        centro_seta(c, t, C["s14.a"] + 0.5, 1350, 380)
    pausa(c, t, C, "s15", desenho)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    contas(c, t, [(C["s16.a"], "v^2 = 0,5 · 10 · 125"), (C["s16.b"], "0,5 · 10 = 5"), (C["s16.c"], "5 · 125 = 625"), (C["s16.d"], "v = r{625} = 25 m/s")],
           XE, 240, 76, 140)
    E.foco(c, t, C["s16.e"], 0.5, lambda a: sub(c, "25 · 3,6", XE, 860, 66, "g", TINTA2, a))
    bola_txt(c, t, C["s16.e"] + 0.4, "90 km/h", 1450, 560, 180, 66)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    resumo(c, t, C, "s17", (("s17.a", [("plana:", "i", 64), ("atrito", "g", 60, COR), ("estático,", "i", 64), ("v", "g", 60), ("=", "g", 60), ("√(μ·g·R)", "g", 60, COR)]),
                            ("s17.b", [("inclinada:", "i", 64), ("a", "i", 64), ("normal", "g", 60, COR), ("faz", "i", 64), ("o", "i", 64), ("papel", "i", 64)]),
                            ("s17.c", [("a", "i", 64), ("massa", "g", 60), ("nunca", "g", 60, COR), ("entra", "i", 64)])), C["s18"])
    if t < C["s18"]:
        return

    def desenho():
        cx, cy, r = 900, 1010, 115
        if t >= C["s18.a"]:
            pt = M.paint(TINTA2, ep(t, C["s18.a"], 0.5), stroke=12)
            c.drawArc(skia.Rect.MakeXYWH(cx - r, cy - 2 * r, 2 * r, 2 * r), 0, 360, False, pt)
        g = math.radians(-90 + 90 * max(0.0, t - C["s18.a"]))
        P = (cx + r * math.cos(g) * 0.92, cy - r - r * math.sin(g) * 0.92)
        E.foco(c, t, C["s18.c"], 0.4, lambda a: E.bola(c, *P, 30, a=a))
    proxima(c, t, C, "s18", ((C["s18.b"], [("Lombada", "g", 90, COR), ("e", "i", 90)]), (C["s18.c"], [("globo", "g", 90), ("da", "i", 90), ("morte", "g", 90, COR)])),
            "s18.e", "s18.f", desenho)


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, plana=b_plana, inclinada=b_inclinada, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
