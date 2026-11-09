"""Visual — Estudativo · FIS-DIN-004: peso e força normal (no chão e no elevador).
Linguagem visual da trilha de Dinâmica: cabeçalho do visual.py da FIS-DIN-001. Nesta aula: P sai do centro do corpo para
baixo, N sai do ponto de contato para cima; o visor da balança (verde) mostra "kg" = N ÷ 10; a aceleração do elevador em
violeta ao lado da cabine. Todo instante vem de C[...]."""
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
ARQUIVO_FINAL = "estudativo_FIS-DIN-004_peso_e_forca_normal.mp4"
CORTINAS = E.carregar_cortinas(__file__, ("peso", "normal", "elevador", "erro", "atalho", "questao", "fim"))

# todas as contas da aula (g = 10 m/s²; Lua: 1,6 m/s²)
assert 60 * 10 == 600 and round(60 * 1.6) == 96
assert 600 + 60 * 2 == 720 and 720 / 10 == 72 and 60 * (10 + 2) == 720
assert 600 - 60 * 2 == 480 and 480 / 10 == 48 and 60 * (10 - 2) == 480
assert 50 * (10 + 2) == 600 and 600 / 10 == 60 and 50 * (10 - 2) / 10 == 40

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
def cabine(c, t, t0, x, y, kg, dy=0.0, w=420, h=560, pessoa_s=78):
    """elevador com balança e pessoa; (x, y) = canto de cima à esquerda; kg = texto do visor. Devolve (pé, centro do corpo)"""
    yy = y + dy
    piso = yy + h - 30
    bw = 220
    def fn(a):
        elevador(c, x, yy, w, h, a)
        balanca_chao(c, x + w / 2, piso - bw * 0.16, bw, kg, a)
        pessoa(c, x + w / 2, piso - bw * 0.16, pessoa_s, a, braco=-80)
        # visor da balança em tamanho grande, ao lado da cabine
        M.rrect(c, x - 260, yy + 60, 220, 104, 18, "#1B1B20", a)
        v, _, u = kg.partition(" ")
        F.medida(c, v, u, x - 150, yy + 136, 64, "#7CFFB2", a, "center", cor_u="#7CFFB2")
        E.escreve(c, "visor", x - 250, yy + 40, 36, "i", TINTA2, a)
    E.foco(c, t, t0, 0.5, fn)
    pe = (x + w / 2, piso - bw * 0.16)
    return pe, (x + w / 2, pe[1] - pessoa_s * 2.0)


def terra(c, cx, cy, r, a=1.0):
    if a <= 0:
        return
    E.bola(c, cx, cy, r, "#2F7FD8", a)
    for dx, dy, k in ((-0.3, -0.2, 0.3), (0.25, 0.2, 0.22), (0.1, -0.45, 0.15)):
        c.drawCircle(cx + dx * r, cy + dy * r, k * r, M.paint("#2FA84F", 0.8 * a))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    if t < C["s02"]:
        def um():
            dy = -90 * ease_io(prog(t, C["s01.b"], 2.0))
            kg = "72 kg" if t >= C["s01.c"] else "60 kg"
            pe, cm = cabine(c, t, C["s01.a"], 1250, 320, kg, dy)
            F.vetor(c, t, C["s01.b"], (1760, 760 + dy), (1760, 560 + dy), "a", None, F.ACEL, 9, size=52)
            E.frase(c, t, C["s01.a"], ps("balança no elevador", "i", 76), XE, 240, passo=0.12)
            E.frase(c, t, C["s01.b"], [("arranca", "g", 72), ("para", "i", 76), ("cima", "g", 72, COR)], XE, 380, passo=0.12)
            E.foco(c, t, C["s01.c"], 0.5, lambda a: (E.escreve(c, "marca", XE, 530, 70, "i", TINTA, a), F.medida(c, 72, "kg", XE + 230, 530, 96, COR, a)))
            E.frase(c, t, C["s01.d"], ps("sua massa:", "i", 64), XE, 700, passo=0.1)
            E.foco(c, t, C["s01.d"] + 0.4, 0.5, lambda a: F.medida(c, 60, "kg", XE + 340, 700, 80, CERTO, a))
            E.frase(c, t, C["s01.d"] + 1.6, ps("o que a balança", "i", 70) + [("mede?", "g", 70, COR)], XE, 880, passo=0.12)
        E.saida(c, t, C["s02"] - 0.1, um)
        return
    promessa(c, t, C, "s02", (("s02.b", "calcular o peso", 0), ("s02.c", "peso não é massa", 0), ("s02.d", "a força normal", 0)))


def b_lembrete(c, t, C, b):
    lembrete(c, t, C, "s03", (("s03.b", "segunda lei,", "resultante = m × a"), ("s03.c", "ação e reação,", "em corpos diferentes"),
                              ("s03.d", "queda livre,", "g = 10 m/s²")))


# ---------------- peso ----------------
def b_peso(c, t, C, b):
    if t < C["s05"]:
        E.frase(c, t, C["s04.a"], [("peso", "g", 100, COR), ("=", "g", 90, TINTA2)] + ps("a Terra puxa", "i", 90), XE, 240, passo=0.12)
        E.frase(c, t, C["s04.b"], ps("sempre para baixo, na vertical", "i", 56, TINTA2), XE, 340, passo=0.1)
        E.foco(c, t, C["s04.a"], 0.6, lambda a: terra(c, 1400, 1500, 560, a), blur=0)
        yb = 560 + (0.5 * 140 * max(0.0, t - C["s04.c"]) ** 2 if t >= C["s04.c"] else 0)
        yb = min(yb, 800)
        E.foco(c, t, C["s04.a"] + 0.4, 0.5, lambda a: F.bloco(c, 1400, yb, 170, 130, None, E.COR, a))
        seta_f(c, t, C["s04.b"], (1400, yb), -90, 190, "P", lpos=(1470, yb + 160))
        if t >= C["s04.c"]:
            F.vetor(c, t, C["s04.c"] + 0.2, (1640, 420), (1640, 620), "g", None, F.ACEL, 9, size=50)
            E.frase(c, t, C["s04.c"], ps("solto, cai com", "i", 60) + [("a = g", "g", 60, F.ACEL)], XE, 520, passo=0.1)
        sub_em(c, t, C["s04.d"], "P = m · g", XE, 780, 150, "g", TINTA)
        return
    if t < C["s06"]:
        formula_nova(c, t, C["s05"] - 0.2, "P = m · g", XE, 280, 150, (("P", "peso", "N"), ("m", "massa", "kg"), ("g", "10", "m/s^2")),
                     (C["s05.a"], C["s05.b"], C["s05.c"]))
        E.foco(c, t, C["s05.d"], 0.5, lambda a: (pessoa(c, 1400, 800, 90, a), F.medida(c, 60, "kg", 1400, 440, 64, TINTA, a, "center")))
        if t >= C["s05.d"]:
            F.chao(c, 1150, 1650, 800, ep(t, C["s05.d"], 0.4))
        seta_f(c, t, C["s05.d"] + 0.5, (1480, 600), -90, 170, "P", lpos=(1560, 760))
        E.foco(c, t, C["s05.e"], 0.5, lambda a: sub(c, "60 · 10", 1140, 960, 76, "g", TINTA2, a, "center"))
        bola_txt(c, t, C["s05.e"] + 0.6, "600 N", 1640, 920, 110, 56)
        return
    E.frase(c, t, C["s06.a"], [("massa", "g", 84, COR), ("≠", "g", 84, TINTA2), ("peso", "g", 84, COR)], XE, 220, passo=0.12)
    E.frase(c, t, C["s06.b"], ps("massa: quanto de matéria, em kg; a mesma em todo lugar", "i", 50, TINTA2), XE, 320, passo=0.06)
    for i, (k, lugar, g, P) in enumerate((("s06.b", "Terra", "g = 10", "600 N"), ("s06.c", "Lua", "g ≈ 1,6", "96 N"))):
        x = 200 + i * 800
        p = ep(t, C[k] + 0.6, 0.5)
        E.caixa_pontilhada(c, x, 400, 720, 600, p, prog_=p)
        E.foco(c, t, C[k] + 0.7, 0.5, lambda a, x=x, lugar=lugar, g=g: (E.escreve(c, lugar, x + 40, 490, 70, "g", TINTA, a),
                                                                       sub(c, g, x + 680, 490, 50, "g", TINTA2, a, "right")))
        E.foco(c, t, C[k] + 1.0, 0.5, lambda a, x=x: (E.escreve(c, "massa", x + 40, 640, 54, "i", TINTA, a), F.medida(c, 60, "kg", x + 320, 640, 72, TINTA, a)))
        tk = C["s06.d"] if i else C[k] + 1.4
        E.foco(c, t, tk, 0.5, lambda a, x=x, P=P, i=i: (E.escreve(c, "peso", x + 40, 800, 54, "i", TINTA, a),
                                                        F.medida(c, *P.split(), x + 320, 800, 90, COR if i else TINTA, a)))
    E.foco(c, t, C["s06.d"] + 0.6, 0.4, lambda a: E.pilula(c, "60 × 1,6 = 96", 1360, 920, 44, "b", fundo=TINTA2, a=a))


# ---------------- normal ----------------
def b_normal(c, t, C, b):
    cx, cy = 1350, 600
    E.foco(c, t, C["s07.a"], 0.5, lambda a: F.bloco(c, cx, cy, 260, 200, None, TINTA2, a))
    if t >= C["s07.a"]:
        F.chao(c, cx - 450, cx + 450, cy + 100, ep(t, C["s07.a"], 0.4))
    seta_f(c, t, C["s07.a"] + 0.6, (cx - 40, cy), -90, 280, "P", lpos=(cx - 110, cy + 300))
    seta_f(c, t, C["s07.b"], (cx + 50, cy - 100), 90, 280, "N", lpos=(cx + 120, cy - 330))
    if t < C["s08"]:
        E.frase(c, t, C["s07.a"], ps("corpo parado no chão", "i", 72), XE, 230, passo=0.12)
        E.frase(c, t, C["s07.c"], [("força", "i", 84), ("normal", "g", 84, COR)], XE, 400)
        E.frase(c, t, C["s07.d"], [("normal", "g", 64), ("=", "g", 64, TINTA2), ("perpendicular", "i", 70)], XE, 520, passo=0.12)
        if t >= C["s07.d"] + 0.5:
            q = ep(t, C["s07.d"] + 0.5, 0.4)
            x0, y0 = cx + 170, cy + 100
            M.line(c, x0, y0 - 50, x0 + 50, y0 - 50, E.COR, q, 5)
            M.line(c, x0 + 50, y0 - 50, x0 + 50, y0, E.COR, q, 5)
            M.line(c, x0, y0, x0, y0 - 160, E.COR, q, 4, dash=E.TRACO)
        E.frase(c, t, C["s07.d"] + 1.0, ps("sai da superfície em ângulo reto", "i", 52, TINTA2), XE, 620, passo=0.08)
        return
    E.frase(c, t, C["s08.a"], ps("parado:", "i", 70) + ps("resultante zero", "g", 66, COR), XE, 230, passo=0.12)
    E.frase(c, t, C["s08.b"], [("N", "g", 110, COR), ("=", "g", 110, TINTA2), ("P", "g", 110, COR)], XE, 400, passo=0.12)
    E.frase(c, t, C["s08.b"] + 0.8, ps("no chão plano, sem mais nada", "i", 50, TINTA2), XE, 480, passo=0.08)
    E.frase(c, t, C["s08.c"], [("não", "g", 64, ERRADO)] + ps("são ação e reação", "i", 64), XE, 640, passo=0.1)
    E.foco(c, t, C["s08.d"], 0.4, lambda a: E.pilula(c, "as duas no mesmo corpo", XE + 300, 740, 46, "b", fundo=TINTA, a=a))
    E.frase(c, t, C["s08.e"], ps("par do peso:", "i", 56, TINTA2) + ps("o corpo puxa a Terra", "g", 54), XE, 880, passo=0.1)
    E.foco(c, t, C["s08.e"] + 0.4, 0.6, lambda a: terra(c, 1700, 1200, 230, a), blur=0)
    seta_f(c, t, C["s08.e"] + 0.8, (1700, 970), 90, 120, None)


# ---------------- elevador ----------------
def b_elevador(c, t, C, b):
    x, y = 1280, 300
    if t < C["s10"]:
        pe, cm = cabine(c, t, C["s09"], x, y, "60 kg")
        E.frase(c, t, C["s09.a"], ps("a balança mede", "i", 72) + [("a", "i", 72), ("normal", "g", 70, COR)], XE, 240, passo=0.12)
        seta_f(c, t, C["s09.a"] + 0.4, (pe[0] + 50, pe[1]), 90, 170, "N", lpos=(pe[0] + 130, pe[1] - 150), size=52)
        E.frase(c, t, C["s09.b"], [("÷", "g", 80, COR), ("10", "g", 80, COR)] + ps("e mostra em quilos", "i", 70), XE, 420, passo=0.12)
        E.foco(c, t, C["s09.c"], 0.5, lambda a: sub(c, "parado: N = 600 N → 60 kg", XE, 600, 70, "g", TINTA, a))
        return
    if t < C["s11"]:
        def s10():
            dy = -60 * ease_io(prog(t, C["s10.a"], 1.5))
            kg = "72 kg" if t >= C["s10.e"] else "60 kg"
            pe, cm = cabine(c, t, C["s10"], x, y, kg, dy)
            F.vetor(c, t, C["s10.a"], (1780, 700 + dy), (1780, 520 + dy), "a", None, F.ACEL, 9, size=50)
            seta_f(c, t, C["s10.b"], (pe[0] + 50, pe[1]), 90, 210, "N", lpos=(pe[0] + 130, pe[1] - 190), size=52)
            seta_f(c, t, C["s10.b"] + 0.3, (pe[0] - 50, cm[1]), -90, 175, "P", lpos=(pe[0] - 120, cm[1] + 175), size=52)
            E.frase(c, t, C["s10.a"], [("a", "g", 70, F.ACEL), ("=", "g", 70), ("2", "g", 70, F.ACEL), ("m/s²", "b", 54, F.UNID)] + ps("para cima", "i", 70), XE, 230, passo=0.12)
            contas(c, t, [(C["s10.b"], "N − P = m · a"), (C["s10.c"], "N − 600 = 60 · 2"), (C["s10.d"], "N = 720 N", COR)], XE, 400, 80, 130)
            E.foco(c, t, C["s10.e"], 0.5, lambda a: E.pilula(c, "mostra 72 kg", XE + 260, 860, 54, "g", fundo=CERTO, a=a))
        E.saida(c, t, C["s11"] - 0.1, s10)
        return
    kg = "48 kg" if t >= C["s11.e"] else "60 kg"
    pe, cm = cabine(c, t, C["s11"], x, y, kg)
    F.vetor(c, t, C["s11.a"], (1780, 520), (1780, 700), "a", None, F.ACEL, 9, size=50, lado=-1)
    seta_f(c, t, C["s11.b"], (pe[0] - 50, cm[1]), -90, 175, "P", lpos=(pe[0] - 120, cm[1] + 175), size=52)
    seta_f(c, t, C["s11.b"] + 0.3, (pe[0] + 50, pe[1]), 90, 140, "N", lpos=(pe[0] + 130, pe[1] - 120), size=52)
    E.frase(c, t, C["s11.a"], [("a", "g", 70, F.ACEL), ("=", "g", 70), ("2", "g", 70, F.ACEL), ("m/s²", "b", 54, F.UNID)] + ps("para baixo", "i", 70), XE, 230, passo=0.12)
    contas(c, t, [(C["s11.b"], "P − N = m · a"), (C["s11.c"], "600 − N = 120"), (C["s11.d"], "N = 480 N", COR)], XE, 400, 80, 130)
    E.foco(c, t, C["s11.e"], 0.5, lambda a: E.pilula(c, "mostra 48 kg", XE + 260, 860, 54, "g", fundo=E.COR, a=a))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s12"], [("cuidado", "g", 96, ERRADO)], XE, 200)
    E.frase(c, t, C["s12.a"], ps("subindo,", "i", 66) + ps("sempre marca mais?", "g", 62), XE, 330, passo=0.12)
    E.foco(c, t, C["s12.a"] + 1.2, 0.4, lambda a: E.selo(c, XE + 920, 310, 44, False, a))
    dy = -((t - C["s12.b"]) * 40 % 120) if t >= C["s12.b"] else 0
    pe, cm = cabine(c, t, C["s12"], 1280, 340, "60 kg", dy)
    F.vetor(c, t, C["s12.b"], (1780, 760 + dy), (1780, 560 + dy), "v", None, F.VEL, 9, size=50)
    E.frase(c, t, C["s12.b"], ps("velocidade constante:", "i", 60) + [("a = 0", "g", 60, F.ACEL)], XE, 480, passo=0.1)
    E.foco(c, t, C["s12.c"], 0.5, lambda a: sub(c, "N = P → 60 kg", XE, 620, 76, "g", CERTO, a))
    E.frase(c, t, C["s12.d"], ps("manda a", "i", 64) + [("aceleração,", "g", 62, F.ACEL)], XE, 800, passo=0.1)
    E.frase(c, t, C["s12.d"] + 1.2, ps("não o movimento", "i", 64, TINTA2), XE, 900, passo=0.1)


# ---------------- atalho (palco) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def s13():
        E.frase(c, t, C["s13"], ps("agora, o atalho", "i", 76, CLARO), W / 2, 160, "center")
        E.frase(c, t, C["s13.a"], [("a", "g", 70, CLARO), ("para", "i", 70, CLARO), ("cima:", "i", 70, CLARO)], 330, 380, passo=0.12)
        sub_em(c, t, C["s13.b"], "N = m · (g + a)", 820, 380, 100, "g", BR)
        E.frase(c, t, C["s13.c"], [("a", "g", 70, CLARO), ("para", "i", 70, CLARO), ("baixo:", "i", 70, CLARO)], 330, 580, passo=0.12)
        sub_em(c, t, C["s13.d"], "N = m · (g − a)", 820, 580, 100, "g", BR)
        sub_em(c, t, C["s13.e"], "60 · 12 = 720 N", W / 2, 840, 96, "g", CLARO, "center")
        E.frase(c, t, C["s13.e"] + 1.0, ps("numa conta só", "i", 56, CLARO), W / 2, 950, "center", 0.1)
    E.saida(c, t, C["s14"] - 0.1, s13)
    if t < C["s14"]:
        return
    E.frase(c, t, C["s14.a"], ps("a normal segura o peso", "i", 60, CLARO) + ps("e dá a aceleração", "g", 58, BR), W / 2, 220, "center", 0.1)
    E.frase(c, t, C["s14.b"], ps("caiu livre:", "i", 66, CLARO) + [("a = g", "g", 66, BR)], W / 2, 420, "center", 0.12)
    E.foco(c, t, C["s14.c"], 0.5, lambda a: sub(c, "N = m · (g − g) = 0", W / 2, 560, 90, "g", BR, a, "center"))
    pilula_em(c, t, C["s14.c"] + 0.8, "você flutua", W / 2, 680, 50, E.COR)
    E.frase(c, t, C["s14.d"], [("não", "g", 60, ERRADO), ("compensa:", "i", 62, CLARO)] + ps("sentido de a desconhecido", "i", 62, CLARO), W / 2, 870, "center", 0.1)
    E.frase(c, t, C["s14.d"] + 2.4, ps("desenhe as forças", "g", 60, BR), W / 2, 970, "center", 0.1)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    cabeca_q(c, t, C, "s15")
    E.frase(c, t, C["s15.a"], [("pessoa", "i", 70)], XE, 330)
    E.foco(c, t, C["s15.a"] + 0.3, 0.5, lambda a: F.medida(c, 50, "kg", XE + 260, 330, 76, COR, a))
    E.frase(c, t, C["s15.a"] + 1.0, ps("elevador", "i", 64) + [("desce", "g", 64)], XE, 460, passo=0.12)
    E.frase(c, t, C["s15.b"], ps("e vai", "i", 64) + [("freando", "g", 64, COR)], XE, 570, passo=0.12)
    E.foco(c, t, C["s15.c"], 0.5, lambda a: (E.escreve(c, "aceleração", XE, 700, 60, "i", TINTA, a), F.medida(c, 2, "m/s^2", XE + 330, 700, 76, F.ACEL, a)))
    E.frase(c, t, C["s15.d"], ps("a balança marca", "i", 72) + [("? kg", "g", 72, COR)], XE, 880, passo=0.12)

    def desenho():
        dy = (t - C["s15.a"]) * 20 if t >= C["s15.a"] else 0
        pe, cm = cabine(c, t, C["s15.a"], 1300, 300, "? kg", min(dy, 80))
        F.vetor(c, t, C["s15.b"], (1800, 420 + min(dy, 80)), (1800, 620 + min(dy, 80)), "v", None, F.VEL, 9, size=50)
    pausa(c, t, C, "s16", desenho)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    E.frase(c, t, C["s17.a"], ps("desce freando:", "i", 62) + [("v", "g", 62, F.VEL), ("para", "i", 62), ("baixo,", "i", 62), ("diminuindo", "g", 58)], XE, 200, passo=0.1)
    F.vetor(c, t, C["s17.a"] + 0.4, (1600, 280), (1600, 450), "v", None, F.VEL, 9, size=48)
    E.frase(c, t, C["s17.b"], [("a", "g", 70, F.ACEL), ("para", "i", 70), ("cima", "g", 70, F.ACEL)], XE, 330, passo=0.12)
    F.vetor(c, t, C["s17.b"] + 0.3, (1750, 450), (1750, 280), "a", None, F.ACEL, 9, size=48, lado=-1)
    contas(c, t, [(C["s17.c"], "N = 50 · (10 + 2)"), (C["s17.d"], "N = 50 · 12 = 600 N")], XE, 500, 84, 140)
    bola_txt(c, t, C["s17.e"], "60 kg", 1500, 640, 140, 64, CERTO)
    E.foco(c, t, C["s17.e"] + 1.4, 0.5, lambda a: sub(c, "50 · (10 − 2) → 40 kg", XE, 920, 66, "g", ERRADO, a))
    risca_em(c, t, C["s17.e"] + 2.4, XE - 10, 935, XE + 700, 870)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    resumo(c, t, C, "s18", (("s18.a", [("peso:", "i", 66), ("P", "g", 62, COR), ("=", "g", 62), ("m", "g", 62, COR), ("·", "g", 62), ("g,", "g", 62, COR), ("em", "i", 66), ("N", "g", 62)]),
                            ("s18.b", [("massa", "g", 62, COR), ("em", "i", 66), ("kg,", "g", 62), ("não", "i", 66), ("muda", "i", 66)]),
                            ("s18.c", [("normal", "g", 62, COR), ("muda", "i", 66), ("com", "i", 66), ("a", "i", 66), ("aceleração", "i", 66)])), C["s19"])
    if t < C["s19"]:
        return

    def desenho():
        E.foco(c, t, C["s19.c"], 0.5, lambda a: (F.teto(c, 450, 750, 640, a), F.mola(c, 600, 640, 600, 820, 7, 40, TINTA2, a),
                                                 F.bloco(c, 600, 880, 130, 110, None, E.COR, a)))
        seta_f(c, t, C["s19.c"] + 0.4, (680, 840), 90, 120, "F_{el}", lpos=(780, 760), size=48)
        E.foco(c, t, C["s19.b"], 0.5, lambda a: (F.teto(c, 900, 1150, 640, a), M.line(c, 1025, 640, 1025, 820, TINTA2, a, 5), F.bloco(c, 1025, 880, 130, 110, None, E.COR, a)))
        E.foco(c, t, C["s19.b"] + 0.4, 0.4, lambda a: rot_vetor(c, "T", 1100, 760, 48, E.COR_TEXTO, a))
    proxima(c, t, C, "s19", ((C["s19.a"], [("Tração", "g", 100, COR), ("e", "i", 100), ("mola", "g", 100, COR)]),), "s19.e", "s19.f", desenho)


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, peso=b_peso, normal=b_normal, elevador=b_elevador, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
