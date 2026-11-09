"""Visual — Estudativo · FIS-DIN-005: tração e força elástica (lei de Hooke e dinamômetro).
Linguagem visual da trilha de Dinâmica: cabeçalho do visual.py da FIS-DIN-001. Nesta aula: T sai do corpo ao longo do fio;
F_el sai do ponto onde a mola toca o corpo; tamanho natural da mola em tracejado cinza e a deformação x numa cota laranja.
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
ARQUIVO_FINAL = "estudativo_FIS-DIN-005_tracao_e_forca_elastica.mp4"
CORTINAS = E.carregar_cortinas(__file__, ("tracao", "diagrama", "hooke", "dinamometro", "erro", "atalho", "questao", "fim"))

# todas as contas da aula (g = 10 m/s²)
assert 2 * 10 == 20 and 3 * 10 == 30 and 30 / 2 == 15
assert 200 * 0.1 == 20
assert 3 * 10 / 500 == 0.06
assert 25 - 20 == 5
assert 4 * 5 / 2 == 10  # 2 kg → 4 cm, então 5 kg → 10 cm
assert 4 * 10 == 40 and 38 - 30 == 8 and round(40 / 0.08) == 500

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
def peixe(c, cx, cy, s, a=1.0):
    """peixe pendurado pela boca (cabeça para cima), centro em (cx, cy)"""
    if a <= 0:
        return
    c.drawOval(skia.Rect.MakeXYWH(cx - s * 0.45, cy - s, s * 0.9, s * 2), M.paint("#6C8FA8", a))
    p = skia.Path(); p.moveTo(cx, cy + s * 0.85); p.lineTo(cx - s * 0.5, cy + s * 1.45); p.lineTo(cx + s * 0.5, cy + s * 1.45); p.close()
    c.drawPath(p, M.paint("#56768C", a))
    c.drawCircle(cx + s * 0.15, cy - s * 0.6, s * 0.09, M.paint(TINTA, a))


def dinamometro(c, x, ytop, L, a=1.0, marcas=True):
    """balança de gancho: argola em ytop, tubo transparente com a mola (comprimento L) e o gancho na ponta. Devolve o y do gancho"""
    if a <= 0:
        return ytop + 60 + L + 60
    c.drawCircle(x, ytop, 16, M.paint(TINTA2, a, stroke=6))
    tw, th = 90, 420
    M.rrect(c, x - tw / 2, ytop + 16, tw, th, 18, "#FFFFFF", 0.55 * a)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x - tw / 2, ytop + 16, tw, th), 18, 18), M.paint(TINTA, a, stroke=4))
    if marcas:
        for k in range(9):
            yk = ytop + 60 + 40 * k
            M.line(c, x + tw / 2 - 22, yk, x + tw / 2 - 6, yk, TINTA2, a * 0.7, 3)
    F.mola(c, x, ytop + 30, x, ytop + 60 + L, 8, 40, TINTA2, a, 4, 14)
    M.line(c, x - 30, ytop + 60 + L, x + 30, ytop + 60 + L, E.COR, a, 7)
    M.line(c, x, ytop + 60 + L, x, ytop + th + 60, TINTA2, a, 6)
    gy = ytop + th + 60
    pt = M.paint(TINTA2, a, stroke=6)
    c.drawArc(skia.Rect.MakeXYWH(x - 22, gy - 4, 44, 44), 180, -250, False, pt)
    return gy + 30


def lustre(c, cx, yfio, a=1.0):
    """luminária pendurada; yfio = ponta de baixo do fio"""
    if a <= 0:
        return
    p = skia.Path(); p.moveTo(cx - 25, yfio); p.lineTo(cx + 25, yfio); p.lineTo(cx + 110, yfio + 110); p.lineTo(cx - 110, yfio + 110); p.close()
    c.drawPath(p, M.paint(E.COR, a))
    c.drawCircle(cx, yfio + 120, 30, M.paint("#FFE08A", a))


def cota(c, t, t0, x, y0, y1, rot, cor=None, lado=1, size=50):
    """cota vertical de y0 a y1 em x, com o rótulo ao lado"""
    q = ep(t, t0, 0.5)
    if q <= 0:
        return
    cor = cor or E.COR
    M.line(c, x, y0, x, lerp(y0, y1, q), cor, 1.0, 5)
    for yy in (y0, y1):
        M.line(c, x - 14, yy, x + 14, yy, cor, q, 5)
    E.foco(c, t, t0 + 0.4, 0.4, lambda a: sub(c, rot, x + lado * 30, (y0 + y1) / 2 + size * 0.36, size, "g", cor, a, "left" if lado > 0 else "right"))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    if t < C["s02"]:
        def um():
            E.foco(c, t, C["s01.a"], 0.5, lambda a: F.teto(c, 1250, 1550, 160, a))
            L = 140 + 60 * ease_out(prog(t, C["s01.a"] + 0.6, 0.8))
            def d(a):
                gy = dinamometro(c, 1400, 180, L, a)
                peixe(c, 1400, gy + 130, 110, a)
            E.foco(c, t, C["s01.a"], 0.5, d)
            if t >= C["s01.b"]:
                q = 0.5 + 0.5 * math.sin((t - C["s01.b"]) * 5)
                c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(1340, 190, 120, 440), 22, 22), M.paint(E.COR, (0.4 + 0.5 * q) * ep(t, C["s01.b"], 0.3), stroke=6))
            E.frase(c, t, C["s01.a"], ps("na feira:", "i", 76), XE, 240, passo=0.12)
            E.frase(c, t, C["s01.a"] + 0.6, ps("balança de gancho", "g", 72), XE, 350, passo=0.12)
            E.frase(c, t, C["s01.b"], ps("dentro, só uma", "i", 70) + [("mola", "g", 70, COR)], XE, 520, passo=0.12)
            E.frase(c, t, C["s01.c"], ps("como a mola", "i", 76) + [("mede", "g", 76, COR), ("força?", "g", 76)], XE, 900, passo=0.12)
        E.saida(c, t, C["s02"] - 0.1, um)
        return
    promessa(c, t, C, "s02", (("s02.b", "fios e molas", 0), ("s02.c", "lei de Hooke", 0)))


def b_lembrete(c, t, C, b):
    lembrete(c, t, C, "s03", (("s03.b", "o peso,", "P = m · g, com g = 10"), ("s03.c", "corpo parado,", "resultante zero")))


# ---------------- tração ----------------
def b_tracao(c, t, C, b):
    if t < C["s05"]:
        E.frase(c, t, C["s04.a"], ps("fio esticado", "i", 80) + [("puxa", "g", 80, COR)], XE, 240, passo=0.12)
        E.frase(c, t, C["s04.b"], [("tração,", "g", 96, COR), ("letra", "i", 90), ("T", "g", 96, COR)], XE, 380, passo=0.12)
        E.foco(c, t, C["s04.a"], 0.5, lambda a: (F.teto(c, 1250, 1550, 220, a), M.line(c, 1400, 220, 1400, 640, TINTA2, a, 6),
                                                 F.bloco(c, 1400, 720, 200, 160, None, TINTA2, a)))
        seta_f(c, t, C["s04.b"], (1400, 640), 90, 200, "T", lpos=(1490, 560))
        E.frase(c, t, C["s04.c"], [("só", "g", 70), ("puxa,", "g", 70, CERTO), ("nunca", "i", 74), ("empurra", "i", 74, ERRADO)], XE, 540, passo=0.12)
        E.frase(c, t, C["s04.d"], ps("sai do corpo, ao longo do fio", "i", 58, TINTA2), XE, 660, passo=0.1)
        return
    E.frase(c, t, C["s05.a"], [("fio", "i", 80), ("ideal", "g", 80, COR)], XE, 240, passo=0.12)
    E.frase(c, t, C["s05.a"] + 0.6, ps("sem massa, não estica", "i", 58, TINTA2), XE, 330, passo=0.1)
    E.frase(c, t, C["s05.b"], [("mesma", "g", 66, COR), ("tração", "i", 70)] + ps("no fio todo", "i", 70), XE, 470, passo=0.12)
    E.foco(c, t, C["s05.c"], 0.5, lambda a: (F.teto(c, 1250, 1550, 200, a), M.line(c, 1400, 200, 1400, 520, TINTA2, a, 5), lustre(c, 1400, 520, a),
                                             F.medida(c, 2, "kg", 1580, 600, 60, TINTA, a)))
    seta_f(c, t, C["s05.c"] + 1.0, (1400, 660), -90, 180, "P", modulo="20 N", lpos=(1400, 920))
    seta_f(c, t, C["s05.d"], (1400, 510), 90, 180, "T", modulo="20 N", lpos=(1560, 380))
    E.frase(c, t, C["s05.c"], ps("lustre parado:", "i", 64), XE, 680, passo=0.1)
    E.foco(c, t, C["s05.d"] + 0.6, 0.5, lambda a: sub(c, "T = P = 20 N", XE, 800, 84, "g", COR, a))


# ---------------- diagrama de corpo livre ----------------
def b_diagrama(c, t, C, b):
    if t < C["s07"]:
        E.frase(c, t, C["s06.a"], [("diagrama", "g", 80, COR)] + ps("de corpo livre", "i", 84), XE, 230, passo=0.12)
        for i, (k, l1, l2) in enumerate((("s06.b", "corpo", "sozinho"), ("s06.c", "o peso,", "sempre"), ("s06.d", "uma força", "por contato"))):
            y = 420 + i * 150
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, XE + 40, y - 26, 40, a=a), centro(c, str(i + 1), XE + 40, y - 4, 50, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, [(l1, "g", 64), (l2, "i", 68, COR)], XE + 110, y, passo=0.12)
        cx, cy = 1420, 600
        E.foco(c, t, C["s06.b"], 0.5, lambda a: F.bloco(c, cx, cy, 220, 170, None, TINTA2, a))
        if t >= C["s06.b"] + 0.3:
            p = ep(t, C["s06.b"] + 0.3, 0.5)
            E.caixa_pontilhada(c, cx - 180, cy - 150, 360, 300, p, prog_=p)
        seta_f(c, t, C["s06.c"], (cx, cy), -90, 230, "P", lpos=(cx + 60, cy + 270))
        E.foco(c, t, C["s06.d"] + 0.8, 0.4, lambda a: E.escreve(c, "fio · chão · mola", 1250, 980, 50, "i", TINTA2, a))
        return
    if t < C["s08"]:
        def s07():
            E.frase(c, t, C["s07.a"], ps("vaso de", "i", 72), XE, 230, passo=0.12)
            E.foco(c, t, C["s07.a"] + 0.4, 0.5, lambda a: F.medida(c, 3, "kg", XE + 270, 230, 76, COR, a))
            E.frase(c, t, C["s07.a"] + 1.0, ps("dois fios, retos para cima", "i", 56, TINTA2), XE, 330, passo=0.1)
            cx, cy = 1350, 640
            E.foco(c, t, C["s07.a"], 0.5, lambda a: (F.teto(c, cx - 250, cx + 250, 200, a), M.line(c, cx - 80, 200, cx - 80, cy - 80, TINTA2, a, 5),
                                                     M.line(c, cx + 80, 200, cx + 80, cy - 80, TINTA2, a, 5), F.bloco(c, cx, cy, 240, 160, "3 kg", E.COR, a, size=54)))
            seta_f(c, t, C["s07.b"], (cx, cy + 80), -90, 170, "P", modulo="30 N", lpos=(cx, cy + 330))
            seta_f(c, t, C["s07.c"], (cx - 80, cy - 80), 90, 130, "T", lpos=(cx - 170, cy - 170))
            seta_f(c, t, C["s07.c"] + 0.3, (cx + 80, cy - 80), 90, 130, "T", lpos=(cx + 170, cy - 170))
            E.frase(c, t, C["s07.b"], [("P", "g", 76, COR), ("=", "g", 76), ("30", "g", 76), ("N", "b", 56, F.UNID)], XE, 520, passo=0.1)
            E.foco(c, t, C["s07.c"], 0.5, lambda a: sub(c, "T + T = 30", XE, 660, 80, "g", TINTA, a))
            E.foco(c, t, C["s07.d"], 0.5, lambda a: sub(c, "T = 15 N", XE, 800, 96, "g", COR, a))
        E.saida(c, t, C["s08"] - 0.1, s07)
        return
    E.frase(c, t, C["s08.a"], ps("caixa no chão liso, puxada por um fio", "i", 60), XE, 230, passo=0.1)
    cx, cy = 900, 620
    E.foco(c, t, C["s08.a"], 0.5, lambda a: (F.bloco(c, cx, cy, 240, 180, None, TINTA2, a), M.line(c, cx + 120, cy, cx + 600, cy, TINTA2, a, 5)))
    if t >= C["s08.a"]:
        F.chao(c, cx - 400, cx + 700, cy + 90, ep(t, C["s08.a"], 0.4))
    seta_f(c, t, C["s08.b"], (cx - 40, cy), -90, 220, "P", lpos=(cx - 110, cy + 270))
    seta_f(c, t, C["s08.c"], (cx + 40, cy - 90), 90, 220, "N", lpos=(cx + 110, cy - 260))
    seta_f(c, t, C["s08.d"], (cx + 120, cy - 30), 0, 220, "T", lpos=(cx + 280, cy - 70))
    pilula_em(c, t, C["s08.e"], "3 forças: P, N e T", 1450, 900, 56, E.COR)


# ---------------- força elástica e Hooke ----------------
def mola_h(c, t, t0, x0, y, xn, xf, natural=True, d=0.6, rotulo=None, tr=None):
    """mola horizontal presa na parede em x0; o ponto da mão vai de xn (natural) a xf"""
    q = ease_io(prog(t, t0, d))
    xe = lerp(xn, xf, q)
    a = ep(t, t0 - 0.6, 0.4)
    if a <= 0:
        return xe
    F.parede(c, x0, y - 120, y + 120, -1, a)
    F.mola(c, x0, y, xe, y, 9, 50, TINTA2, a, 5, 24)
    c.drawCircle(xe, y, 18, M.paint(E.COR, a))
    if natural and abs(xf - xn) > 1:
        M.line(c, xn, y - 90, xn, y + 90, TINTA2, a * 0.6, 4, dash=E.TRACO)
        E.foco(c, t, t0 - 0.3, 0.4, lambda b_: E.escreve(c, "natural", xn - 70, y - 110, 36, "i", TINTA2, b_))
    return xe


def b_hooke(c, t, C, b):
    if t < C["s10"]:
        E.frase(c, t, C["s09"], ps("agora, a", "i", 76) + [("mola", "g", 76, COR)], XE, 220, passo=0.12)
        xe = mola_h(c, t, C["s09.a"], 700, 450, 1150, 1400)
        seta_f(c, t, C["s09.a"] + 0.7, (xe, 380), 180, 160, "F_{el}", lpos=(xe - 80, 320), size=50)
        E.frase(c, t, C["s09.a"], [("esticou:", "i", 56), ("puxa", "g", 56, COR)], XE, 470, passo=0.1)
        if t >= C["s09.b"]:
            xe2 = mola_h(c, t, C["s09.b"], 700, 760, 1150, 950)
            seta_f(c, t, C["s09.b"] + 0.7, (xe2, 690), 0, 160, "F_{el}", lpos=(xe2 + 80, 630), size=50)
        E.frase(c, t, C["s09.b"], [("apertou:", "i", 56), ("empurra", "g", 56, COR)], XE, 780, passo=0.1)
        E.frase(c, t, C["s09.c"], [("força", "i", 76), ("elástica", "g", 76, COR)], XE, 960, passo=0.12)
        E.frase(c, t, C["s09.d"], ps("volta ao tamanho natural", "i", 52, TINTA2), 1150, 960, "left", 0.08)
        return
    if t < C["s11"]:
        E.frase(c, t, C["s10"], ps("lei de", "i", 72) + [("Hooke", "g", 72, COR)], XE, 200, passo=0.12)
        formula_nova(c, t, C["s10.a"], "F = k · x", XE, 400, 150, (("x", "deformação", "m"), ("k", "constante elástica", "N/m")),
                     (C["s10.b"], C["s10.c"]))
        xe = mola_h(c, t, C["s10.b"], 1150, 470, 1450, 1700, natural=True)
        if t >= C["s10.b"] + 0.6:
            q = ep(t, C["s10.b"] + 0.6, 0.4)
            M.line(c, 1450, 600, 1700, 600, E.COR, q, 5)
            for xx in (1450, 1700):
                M.line(c, xx, 585, xx, 615, E.COR, q, 5)
            E.foco(c, t, C["s10.b"] + 0.9, 0.4, lambda a: E.escreve(c, "x", 1560, 680, 64, "g", COR, a))
        E.foco(c, t, C["s10.d"], 0.5, lambda a: E.pilula(c, "mola dura: k grande", 1450, 860, 50, "g", fundo=TINTA, a=a))
        return
    E.frase(c, t, C["s11.a"], ps("mola de", "i", 70), XE, 220, passo=0.12)
    E.foco(c, t, C["s11.a"] + 0.4, 0.5, lambda a: F.medida(c, 200, "N/m", XE + 260, 220, 80, COR, a))
    E.foco(c, t, C["s11.b"], 0.5, lambda a: (E.escreve(c, "esticada", XE, 340, 64, "i", TINTA, a), F.medida(c, 10, "cm", XE + 280, 340, 80, COR, a)))
    contas(c, t, [(C["s11.c"], "10 cm = 0,1 m"), (C["s11.d"], "F = 200 · 0,1")], XE, 520, 84, 150)
    bola_txt(c, t, C["s11.e"], "20 N", 1450, 640, 150, 76)


# ---------------- dinamômetro ----------------
def b_dinamometro(c, t, C, b):
    E.frase(c, t, C["s12.a"], [("dinamômetro", "g", 84, COR)], XE, 200)
    L = 140 + 120 * ease_out(prog(t, C["s12.c"], 1.0))
    xd = 1450
    E.foco(c, t, C["s12"], 0.5, lambda a: F.teto(c, xd - 150, xd + 150, 160, a))
    E.foco(c, t, C["s12"], 0.5, lambda a: dinamometro(c, xd, 180, L, a))
    gy = 180 + 420 + 60 + 30
    E.foco(c, t, C["s12.b"], 0.5, lambda a: (peixe(c, xd, gy + 130, 110, a), F.medida(c, 3, "kg", xd + 120, gy + 140, 56, TINTA, a)))
    seta_f(c, t, C["s12.c"], (xd - 90, gy + 140), -90, 150, "P", modulo="30 N", lpos=(xd - 200, gy + 330), size=48)
    if t >= C["s12.c"] + 1.0:
        M.line(c, xd - 120, 240, xd - 120, 240 + 140, TINTA2, 0.6, 4, dash=E.TRACO)
        cota(c, t, C["s12.f"], xd + 90, 240 + 140, 240 + L, "x = 6 cm", E.COR, 1, 46)
    E.frase(c, t, C["s12.b"], ps("peixe de", "i", 60), XE, 330, passo=0.1)
    E.foco(c, t, C["s12.b"] + 0.4, 0.5, lambda a: F.medida(c, 3, "kg", XE + 250, 330, 70, COR, a))
    E.foco(c, t, C["s12.c"], 0.5, lambda a: sub(c, "F_{el} = P = 30 N", XE, 460, 76, "g", TINTA, a))
    E.foco(c, t, C["s12.d"], 0.5, lambda a: (E.escreve(c, "k =", XE, 590, 70, "g", TINTA, a), F.medida(c, 500, "N/m", XE + 130, 590, 70, COR, a)))
    contas(c, t, [(C["s12.e"], "x = 30 ÷ 500"), (C["s12.f"], "x = 0,06 m = 6 cm", COR)], XE, 720, 76, 120)
    E.frase(c, t, C["s12.g"], ps("a escala marca a força pelo quanto esticou", "i", 46, TINTA2), XE, 1000, passo=0.06)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s13"], [("cuidado", "g", 96, ERRADO)], XE, 200)
    E.frase(c, t, C["s13.a"], ps("tamanho da mola", "i", 66) + [("≠", "g", 66, ERRADO)] + ps("deformação", "g", 62), XE, 330, passo=0.12)
    y0, k = 410, 18  # 1 cm = 18 px
    E.foco(c, t, C["s13.b"], 0.5, lambda a: (F.teto(c, 930, 1170, y0, a), F.mola(c, 1050, y0, 1050, y0 + 20 * k, 8, 44, TINTA2, a, 5, 18)))
    E.foco(c, t, C["s13.b"] + 0.4, 0.5, lambda a: (F.teto(c, 1330, 1570, y0, a), F.mola(c, 1450, y0, 1450, y0 + 25 * k, 8, 44, TINTA2, a, 5, 18),
                                                   F.bloco(c, 1450, y0 + 25 * k + 50, 110, 100, None, E.COR, a)))
    cota(c, t, C["s13.b"] + 0.2, 960, y0, y0 + 20 * k, "20 cm", TINTA2, -1, 46)
    cota(c, t, C["s13.c"], 1640, y0, y0 + 25 * k, "25 cm", ERRADO, 1, 46)
    risca_em(c, t, C["s13.c"] + 0.8, 1660, y0 + 12.5 * k + 20, 1800, y0 + 12.5 * k - 40, 8)
    if t >= C["s13.d"]:
        M.line(c, 1330, y0 + 20 * k, 1570, y0 + 20 * k, TINTA2, 0.6, 4, dash=E.TRACO)
    cota(c, t, C["s13.d"], 1370, y0 + 20 * k, y0 + 25 * k, "x", CERTO, -1, 50)
    E.foco(c, t, C["s13.c"], 0.5, lambda a: sub(c, "x = 25 cm", XE, 520, 80, "g", ERRADO, a))
    risca_em(c, t, C["s13.c"] + 0.8, XE - 10, 540, XE + 420, 470)
    contas(c, t, [(C["s13.d"], "x = 25 − 20 = 5 cm", CERTO), (C["s13.e"], "x = 0,05 m", CERTO)], XE, 680, 76, 130)


# ---------------- atalho (palco) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def s14():
        E.frase(c, t, C["s14"], ps("agora, o atalho", "i", 76, CLARO), W / 2, 160, "center")
        E.frase(c, t, C["s14.a"], ps("na mesma mola:", "i", 64, CLARO) + [("F", "g", 64, BR), ("e", "i", 64, CLARO), ("x", "g", 64, BR)] + ps("proporcionais", "g", 62, BR),
                W / 2, 310, "center", 0.12)
        E.foco(c, t, C["s14.b"], 0.5, lambda a: (F.medida(c, 2, "kg", 640, 540, 110, BR, a, "right", escuro=True), E.escreve(c, "→", 700, 540, 100, "g", CLARO, a),
                                                 F.medida(c, 4, "cm", 830, 540, 110, BR, a, escuro=True)))
        E.foco(c, t, C["s14.c"], 0.5, lambda a: (F.medida(c, 5, "kg", 640, 720, 110, BR, a, "right", escuro=True), E.escreve(c, "→", 700, 720, 100, "g", CLARO, a),
                                                 F.medida(c, 10, "cm", 830, 720, 110, E.CLARO, a, escuro=True)))
        E.foco(c, t, C["s14.c"] + 0.6, 0.4, lambda a: E.pilula(c, "× 2,5", 1300, 630, 56, "g", fundo=E.COR, a=a))
        E.frase(c, t, C["s14.d"], ps("sem calcular o k", "g", 64, BR), W / 2, 920, "center", 0.12)
    E.saida(c, t, C["s15"] - 0.1, s14)
    if t < C["s15"]:
        return
    E.frase(c, t, C["s15.a"], ps("funciona porque", "i", 64, CLARO), W / 2, 260, "center", 0.1)
    E.foco(c, t, C["s15.a"] + 0.5, 0.5, lambda a: sub(c, "F = k · x  é proporção direta", W / 2, 400, 80, "g", BR, a, "center"))
    E.frase(c, t, C["s15.b"], [("não", "g", 62, ERRADO), ("compensa:", "i", 64, CLARO)] + ps("a questão pede o k", "i", 64, CLARO), W / 2, 620, "center", 0.12)
    E.frase(c, t, C["s15.c"], ps("ou troca de mola", "i", 64, CLARO) + [("→", "g", 64, CLARO), ("calcule", "g", 64, BR)], W / 2, 760, "center", 0.12)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    cabeca_q(c, t, C, "s16")
    E.foco(c, t, C["s16.a"], 0.5, lambda a: (E.escreve(c, "mola de", XE, 340, 64, "i", TINTA, a), F.medida(c, 30, "cm", XE + 250, 340, 76, COR, a)))
    E.foco(c, t, C["s16.b"], 0.5, lambda a: (E.escreve(c, "com", XE, 480, 64, "i", TINTA, a), F.medida(c, 4, "kg", XE + 140, 480, 76, COR, a),
                                             E.escreve(c, "pendurado", XE + 330, 480, 64, "i", TINTA, a)))
    E.foco(c, t, C["s16.c"], 0.5, lambda a: (E.escreve(c, "passa a", XE, 620, 64, "i", TINTA, a), F.medida(c, 38, "cm", XE + 250, 620, 76, COR, a)))
    E.frase(c, t, C["s16.d"], ps("constante elástica:", "i", 70) + [("k = ?", "g", 70, COR)], XE, 800, passo=0.12)

    def desenho():
        y0, k = 280, 13
        E.foco(c, t, C["s16.a"], 0.5, lambda a: (F.teto(c, 1190, 1410, y0, a), F.mola(c, 1300, y0, 1300, y0 + 30 * k, 9, 44, TINTA2, a, 5, 18)))
        cota(c, t, C["s16.a"] + 0.3, 1380, y0, y0 + 30 * k, "30 cm", TINTA2, 1, 44)
        E.foco(c, t, C["s16.b"], 0.5, lambda a: (F.teto(c, 1560, 1780, y0, a), F.mola(c, 1670, y0, 1670, y0 + 38 * k, 9, 44, TINTA2, a, 5, 18),
                                                 F.bloco(c, 1670, y0 + 38 * k + 55, 120, 110, "4 kg", E.COR, a, size=40)))
        cota(c, t, C["s16.c"], 1750, y0, y0 + 38 * k, "38 cm", E.COR, 1, 44)
    pausa(c, t, C, "s17", desenho)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    E.frase(c, t, C["s18"], ps("parado:", "i", 70, COR), XE, 200)
    contas(c, t, [(C["s18.a"], "F_{el} = P = 4 · 10 = 40 N"), (C["s18.b"], "x = 38 − 30 = 8 cm"), (C["s18.c"], "x = 0,08 m"),
                  (C["s18.d"], "k = F ÷ x"), (C["s18.e"], "k = 40 ÷ 0,08")], XE, 330, 72, 118)
    bola_txt(c, t, C["s18.f"], "500 N/m", 1500, 620, 190, 70)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    resumo(c, t, C, "s19", (("s19.a", [("fio", "i", 66), ("só", "i", 66), ("puxa:", "i", 66), ("mesma", "g", 62, COR), ("tração", "g", 62)]),
                            ("s19.b", [("diagrama:", "i", 66), ("peso", "g", 62, COR), ("+", "g", 62), ("um", "i", 66), ("por", "i", 66), ("contato", "g", 62)]),
                            ("s19.c", [("mola:", "i", 66), ("F", "g", 62, COR), ("=", "g", 62), ("k", "g", 62, COR), ("·", "g", 62), ("x,", "g", 62, COR), ("x", "g", 62), ("em", "i", 66), ("metros", "g", 62)])),
           C["s20"])
    if t < C["s20"]:
        return

    def desenho():
        E.foco(c, t, C["s20.b"], 0.5, lambda a: F.carrinho(c, 620, 900, 320, a=a))
        if t >= C["s20.b"]:
            F.chao(c, 380, 900, 900, ep(t, C["s20.b"], 0.4))
        seta_f(c, t, C["s20.b"] + 0.4, (800, 820), 0, 180, None)
        seta_f(c, t, C["s20.b"] + 0.7, (440, 820), 180, 120, None)
    proxima(c, t, C, "s20", ((C["s20.a"], [("Praticando", "g", 100, COR)]), (C["s20.a"] + 0.8, [("as", "i", 84), ("três", "i", 84), ("leis", "g", 80)])),
            "s20.c", "s20.d", desenho)


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, tracao=b_tracao, diagrama=b_diagrama, hooke=b_hooke, dinamometro=b_dinamometro,
              erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
