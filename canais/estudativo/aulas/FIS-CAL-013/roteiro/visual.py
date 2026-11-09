"""Visual — Estudativo · FIS-CAL-013: a primeira lei em cada transformação (trilha Calor e Termodinâmica).

Segue a linguagem visual da Física (cabeçalho do visual.py da FIS-CIN-001), a da trilha Calor e Termodinâmica (cabeçalho do
visual.py da FIS-CAL-001) e as peças da termodinâmica do cabeçalho do visual.py da FIS-CAL-011. Nesta aula:
- A LEI que perde um termo (`lei_zera`): "Q = τ + ΔU" em tinta; o termo que some é riscado em laranja e ganha um 0 embaixo.
- Cada transformação tem um título numerado (esfera laranja com o número) e o cilindro mostra o que fica parado.
- ADIABÁTICA = cilindro com parede grossa hachurada (isolante): o calor não atravessa.
Todo instante vem de C[...] (marcadores do roteiro), para acompanhar a voz real quando ela chegar."""
import math
import re

import editorial as E
import fisica as F
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Física", "Calor e Termodinâmica")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_FIS-CAL-013_primeira_lei_em_cada_transformacao.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("isotermica", "isovolumetrica", "adiabatica", "ciclo", "atalho", "questao", "fim"))
BR = "#FFFFFF"
FRIO = F.NEG
GELO = "#A9D8F5"
AGUA = "#5BA8E0"

# todas as contas da aula (Q = τ + ΔU)
Q = lambda tau, du: tau + du
assert Q(800, 0) == 800                       # isotérmica: ΔU = 0, Q = τ
assert Q(0, 200) == 200                       # isovolumétrica: τ = 0, Q = ΔU
assert Q(-300, 300) == 0                      # adiabática: Q = 0, ΔU = −τ = +300
assert Q(500, -500) == 0                      # questão: adiabática, τ = +500, ΔU = −500
assert (200 - 100) * (4 - 1) == 300           # o ciclo da aula anterior: área 300 kJ = Q do ciclo
def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças da trilha (copiadas da FIS-CAL-001) ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def bola_txt(c, t, t0, s, cx, cy, r, size, cor=None):
    """resposta na esfera: "300 J" com a unidade menor"""
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


def formula_em(c, t, t0, s, x, y, size, est="g", cor=TINTA, align="left"):
    E.formula_em(c, t, t0, s, x, y, size, est, cor, align)


def passos(c, t, linhas, x, y0, dy=125, size=80, align="left"):
    """contas empilhadas: linhas = [(t0, fórmula, cor)]"""
    for i, (ti, s, cor) in enumerate(linhas):
        formula_em(c, t, ti, s, x, y0 + i * dy, size, cor=cor, align=align)


def tracejado(c, t, t0, x0, x1, y, cor=TINTA2, d=0.6, largura=4):
    if t >= t0:
        M.line(c, x0, y, x1, y, cor, 0.8, largura, dash=E.TRACO, progress=ease_io(prog(t, t0, d)))


def particulas(c, t, x, y, w, h, agit, cor, a=1.0, n=(6, 4), r=17, borda=True):
    """caixa com partículas que tremem; agit = 0 (quase paradas) a 1 (muito agitadas)"""
    if a <= 0:
        return
    if borda:
        M.rrect(c, x, y, w, h, 26, E.mix(cor, "#FFFFFF", 0.86), a)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 26, 26), M.paint(cor, a, stroke=4))
    nc, nl = n
    c.save()
    c.clipRect(skia.Rect.MakeXYWH(x + 4, y + 4, w - 8, h - 8), True)
    amp = 3 + 26 * agit
    vel = 4 + 18 * agit
    for i in range(nc):
        for j in range(nl):
            k = i * 7 + j * 13
            px = x + w * (i + 0.5 + 0.25 * math.sin(k)) / nc + amp * math.sin(t * vel + k * 1.7)
            py = y + h * (j + 0.5 + 0.2 * math.cos(k * 1.3)) / nl + amp * math.cos(t * vel * 1.13 + k * 2.3)
            E.bola(c, px, py, r, cor, a)
    c.restore()


def seta_calor(c, t, t0, A, B, rotulo="calor", cor=None, d=0.7, size=50, a=1.0, ondas=3.0, amp=16, lado=-1, escuro=False):
    """seta ondulada de A até B (o calor passando); rótulo acima (lado=-1) ou abaixo (lado=1)"""
    if t < t0 or a <= 0:
        return
    cor = cor or E.COR
    p = ease_io(prog(t, t0, d))
    L = math.dist(A, B)
    ux, uy = (B[0] - A[0]) / L, (B[1] - A[1]) / L
    nx, ny = -uy, ux
    corpo = L - 34
    pts = []
    for i in range(61):
        s = corpo * p * i / 60
        o = amp * math.sin(2 * math.pi * ondas * s / corpo - t * 6)
        pts.append((A[0] + ux * s + nx * o, A[1] + uy * s + ny * o))
    F.poli(c, pts, 1.0, cor, a, 8)
    if p > 0.05:
        tip = (A[0] + ux * (corpo * p + 34), A[1] + uy * (corpo * p + 34))
        F._cabeca(c, tip[0], tip[1], ux, uy, 40, cor, a)
    if rotulo:
        mx, my = (A[0] + B[0]) / 2, (A[1] + B[1]) / 2
        yl = my - amp - 30 if lado < 0 else my + amp + 30 + size * 0.7
        E.foco(c, t, t0 + d * 0.6, 0.4, lambda q: E.formula(c, rotulo, mx, yl, size, "g", cor if not escuro else BR, q * a, "center"))


def seta_reta(c, t, t0, A, B, rotulo=None, cor=TINTA, d=0.5, largura=12, size=56, lado=-1, escuro=False, cab=None):
    """seta grossa e reta (o TRABALHO, o vento, a luz), crescendo de A a B; rótulo no meio (acima com lado=-1)"""
    if t < t0:
        return
    F.seta(c, *A, *B, cor, 1.0, largura, cab, ease_io(prog(t, t0, d)))
    if rotulo:
        mx, my = (A[0] + B[0]) / 2, (A[1] + B[1]) / 2
        if abs(B[0] - A[0]) < abs(B[1] - A[1]):
            xl, yl, al = mx + lado * 34, my + size * 0.36, "right" if lado < 0 else "left"
        else:
            xl, yl, al = mx, (my - 34 if lado < 0 else my + 34 + size * 0.75), "center"
        E.foco(c, t, t0 + d * 0.6, 0.4, lambda q: E.formula(c, rotulo, xl, yl, size, "g", BR if escuro else cor, q, al))


def lembrete2(c, t, C, cena, itens, desenhos):
    """lembrete de duas coisas: itens = [(cue, linha fina, linha forte)]; desenhos[i](a, x, y) desenha à direita da caixa"""
    E.frase(c, t, C[cena] + 0.2, ps("você precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C[cena + ".a"], 0.5, lambda a: E.escreve(c, "2", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C[cena + ".a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 820, 1000
    for i, (k, l1, l2) in enumerate(itens):
        y = 230 + i * 290
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 230, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 58)], x + 44, y + 90)
        E.frase(c, t, C[k] + 0.3, [(l2, "g", 58, COR)], x + 44, y + 170)
        E.foco(c, t, C[k] + 0.6, 0.5, lambda a, i=i, y=y: desenhos[i](a, x + w - 190, y + 115))
    q1 = ease_io(prog(t, C[itens[1][0]] - 0.35, 0.5))
    E.cursor(c, x + w - 30, lerp(430, 720, q1), ep(t, C[itens[0][0]], 0.4))
    E.frase(c, t, lerp(C[itens[1][0]], C[cena + ".end"], 0.6), ps("faltou alguma?", "i", 56, COR) + ps("procure no canal", "i", 56), 820, 920, "left", 0.12)


def promessa(c, t, C, cena, itens, y0=450, dy=150, size=78):
    """'até o fim da aula' + itens numerados; itens = [(cue, texto)]. A órbita da Física gira à direita"""
    tb = C[cena + ".a"] + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1500, 540, 300 * ease_back(prog(t, tb, 0.8)), giro=12 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, C[cena + ".a"], ps("até o fim da aula", "i", 88), XE, 280, passo=0.14)
    for i, (k, s) in enumerate(itens):
        y = y0 + i * dy
        E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, XE + 40, y - 28, 38, a=a), centro(c, str(i + 1), XE + 40, y - 6, 48, "g", BR, a)))
        E.frase(c, t, C[k] + 0.1, [(s, "g", size, COR if i == 0 else TINTA)], XE + 110, y)


def resumo(c, t, C, itens, y0=350, dy=170, size=66):
    """resumindo: itens = [(cue, partes de E.frase)]"""
    E.frase(c, t, C[itens[0][0].split(".")[0]], [("resumindo", "i", 92, COR)], W / 2, 180, "center")
    for i, (k, partes) in enumerate(itens):
        y = y0 + i * dy
        E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 260, y - 26, 52, a=a), centro(c, str(i + 1), 260, y - 4, 60, "g", BR, a)))
        E.frase(c, t, C[k] + 0.1, partes, 360, y, passo=0.1)


def inscreva(c, t, ti, tb):
    """fim: pílula de inscrição com o cursor (ti) e 'bons estudos' (tb)"""
    E.foco(c, t, ti, 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 420, 76, estilo="g", a=a))
    p = ease_io(prog(t, ti + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(720, 445, p), ep(t, ti + 0.2, 0.4))
    E.frase(c, t, tb, [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1570, 990, "center")

# ---------------- peças da termodinâmica (FIS-CAL-011 a 017; candidatas ao fisica.py) ----------------
GAS = "#FFE3D3"   # fundo do gás no cilindro


def cilindro(c, t, x, y, w, h, frac, a=1.0, agit=0.4, cor=None, haste=True):
    """cilindro em pé com gás embaixo e êmbolo por cima. (x, y) = canto de cima à esquerda; frac = parte ocupada pelo gás
    (0 a 1, de baixo para cima). Devolve o y da face de baixo do êmbolo"""
    if a <= 0:
        return y + h * (1 - frac)
    cor = cor or E.COR
    ye = y + h * (1 - frac)
    eh = 46
    M.rrect(c, x + 8, ye, w - 16, y + h - ye - 8, 6, GAS, a)
    particulas(c, t, x + 8, ye + 4, w - 16, y + h - ye - 12, agit, cor, a, n=(5, max(1, round(4 * frac + 0.4))), r=13, borda=False)
    M.rrect(c, x + 8, ye - eh, w - 16, eh, 8, TINTA2, a)
    if haste:
        M.rrect(c, x + w / 2 - 12, ye - eh - 150, 24, 150, 6, TINTA2, a)
    p = skia.Path()
    p.moveTo(x, y - 30); p.lineTo(x, y + h); p.lineTo(x + w, y + h); p.lineTo(x + w, y - 30)
    pt = M.paint(TINTA, a, stroke=8)
    pt.setStrokeJoin(skia.Paint.kRound_Join)
    c.drawPath(p, pt)
    return ye


def caixa_gas(c, x, y, w, h, a=1.0, t=0.0, agit=0.4, rotulo="gás", cor=None):
    """o gás como uma caixa (atalho do balanço): borda grossa, partículas e o nome"""
    if a <= 0:
        return
    cor = cor or E.COR
    particulas(c, t, x, y, w, h, agit, cor, a, n=(5, 3), r=14)
    E.pilula(c, rotulo, x + w / 2, y + h + 60, 46, "g", fundo=TINTA, a=a)


def fonte(c, cx, cy, w, h, nome, cor, a=1.0, temp=None, size=50):
    """fonte quente ou fria: faixa arredondada na cor (laranja = quente, azul = frio) com o nome e a temperatura"""
    if a <= 0:
        return
    M.rrect(c, cx - w / 2, cy - h / 2, w, h, 30, cor, a)
    if temp:
        centro(c, nome, cx, cy - 6, size, "g", BR, a)
        E.formula(c, temp, cx, cy + size * 1.0, size * 0.8, "b", BR, a, "center")
    else:
        centro(c, nome, cx, cy + size * 0.36, size, "g", BR, a)


def maquina(c, t, T, cx=1380, y0=150, y1=920, w=560, inv=False, rot=None, temps=(None, None), nome=None, escuro=False, k=1.0):
    """máquina térmica (inv=False) ou geladeira (inv=True) entre a fonte quente (em cima) e a fria (embaixo).
    T = instantes: dict(q=fonte quente, f=fonte fria, m=máquina, Qq=, tau=, Qf=). rot = rótulos das setas
    (padrão "Qq", "τ", "Qf"). Calor = seta ondulada laranja; trabalho = seta reta em tinta (entra na geladeira, sai do motor)"""
    rot = dict(dict(Qq="Q_q", tau="τ", Qf="Q_f"), **(rot or {}))
    hf = 150 * k
    yq, yf = y0 + hf / 2, y1 - hf / 2
    ym = (y0 + y1) / 2
    r = 105 * k
    tinta = BR if escuro else TINTA
    E.foco(c, t, T.get("q", 1e9), 0.5, lambda a: fonte(c, cx, yq, w, hf, "fonte quente", E.COR, a, temps[0]))
    E.foco(c, t, T.get("f", 1e9), 0.5, lambda a: fonte(c, cx, yf, w, hf, "fonte fria", FRIO, a, temps[1]))

    def corpo(a):
        E.bola(c, cx, ym, r, "#3A3A46" if not escuro else "#E8E8EE", a)
        centro(c, nome or ("geladeira" if inv else "máquina"), cx, ym + 16, 40 * k, "g", BR if not escuro else TINTA, a)
    E.foco(c, t, T.get("m", 1e9), 0.5, corpo)
    A1, B1 = (cx, y0 + hf + 12), (cx, ym - r - 12)
    A2, B2 = (cx, ym + r + 12), (cx, y1 - hf - 12)
    if inv:
        A1, B1, A2, B2 = B1, A1, B2, A2
    seta_calor(c, t, T.get("Qq", 1e9), A1, B1, None, d=0.6, amp=12, ondas=2)
    seta_calor(c, t, T.get("Qf", 1e9), A2, B2, None, d=0.6, amp=12, ondas=2)
    for key, (A, B) in (("Qq", (A1, B1)), ("Qf", (A2, B2))):
        if key in T:
            E.foco(c, t, T[key] + 0.4, 0.4, lambda a, key=key, A=A, B=B: fs(c, rot[key], cx - 60, (A[1] + B[1]) / 2 + 22, 56 * k, "g", E.COR if not escuro else E.CLARO, a, "right"))
    if "tau" in T:
        if inv:
            seta_reta(c, t, T["tau"], (cx + r + 260 * k, ym), (cx + r + 14, ym), rot["tau"], tinta, size=56 * k)
        else:
            seta_reta(c, t, T["tau"], (cx + r + 14, ym), (cx + r + 260 * k, ym), rot["tau"], tinta, size=56 * k)
    return dict(ym=ym, r=r, yq=yq, yf=yf)


def ciclo(c, t, t0, P, pts, d=1.6, cor=None, setas=True, largura=7):
    """caminho fechado no gráfico (valores, não pixels), desenhado no sentido dos pontos, com setas no meio de cada lado"""
    cor = cor or TINTA
    px = [P(*v) for v in pts] + [P(*pts[0])]
    q = ease_io(prog(t, t0, d))
    if q <= 0:
        return
    F.poli(c, px, q, cor, 1.0, largura)
    if setas:
        n = len(px) - 1
        for i in range(n):
            if q >= (i + 0.55) / n:
                (x0, y0), (x1, y1) = px[i], px[i + 1]
                L = math.dist((x0, y0), (x1, y1))
                F._cabeca(c, (x0 + x1) / 2 + (x1 - x0) / L * 16, (y0 + y1) / 2 + (y1 - y0) / L * 16, (x1 - x0) / L, (y1 - y0) / L, 34, cor, 1.0)
    for v in px[:-1]:
        c.drawCircle(*v, 11 * min(1, q * 3), M.paint(cor))


def retangulo_area(c, t, t0, P, x0, x1, y0, y1, cor=None, alfa=0.26, d=0.8):
    """pinta o retângulo de valores [x0, x1] × [y0, y1] da esquerda para a direita"""
    if t < t0:
        return
    cor = cor or E.COR
    p = ease_io(prog(t, t0, d))
    L, R = P.x(x0), P.x(x1)
    c.drawRect(skia.Rect.MakeLTRB(L, P.y(y1), lerp(L, R, p), P.y(y0)), M.paint(cor, alfa))


# ---- fórmula com índice embaixo (Q_q, T_f): E.formula ainda não tem índice; esta cópia de _medir/_desenhar acrescenta "_x" ----
def _sub_nos(nos):
    out = []
    for n in nos:
        if n[0] == "t":
            for i, pp in enumerate(re.split(r"_(\w)", n[1])):
                if i % 2 == 0:
                    if pp:
                        out.append(("t", pp))
                else:
                    out.append(("s", [("t", pp)]))
        elif n[0] == "e":
            out.append(("e", _sub_nos(n[1])))
        elif n[0] == "r":
            out.append(("r", _sub_nos(n[1]), n[2]))
        else:
            out.append((n[0], _sub_nos(n[1]), _sub_nos(n[2])))
    return out


def _med(nos, size, est):
    w = 0.0
    for n in nos:
        if n[0] == "t":
            w += E.larg(n[1], est, size) + E.APERTO[est] * size + size * 0.02
        elif n[0] in "es":
            w += _med(n[1], size * 0.58, est) + size * 0.04
        elif n[0] == "r":
            w += _med(n[1], size, est) + size * 0.62
        else:
            w += max(_med(n[1], size * 0.78, est), _med(n[2], size * 0.78, est)) + size * 0.22
    return w


def _des(c, nos, x, y, size, est, cor, a):
    for n in nos:
        if n[0] == "t":
            E.escreve(c, n[1], x, y, size, est, cor, a)
            x += E.larg(n[1], est, size) + E.APERTO[est] * size + size * 0.02
        elif n[0] in "es":
            _des(c, n[1], x + size * 0.02, y + (size * 0.13 if n[0] == "s" else -size * 0.42), size * 0.58, est, cor, a)
            x += _med(n[1], size * 0.58, est) + size * 0.04
        elif n[0] == "r":
            E.formula(c, "r{x}", x, y, size, est, cor, 0)
            x += _med(n[1], size, est) + size * 0.62
        else:
            s_ = size * 0.78
            wc, wb = _med(n[1], s_, est), _med(n[2], s_, est)
            w = max(wc, wb) + size * 0.12
            _des(c, n[1], x + (w - wc) / 2, y - size * 0.46, s_, est, cor, a)
            _des(c, n[2], x + (w - wb) / 2, y + size * 0.46, s_, est, cor, a)
            b = max(4, size * 0.07)
            c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y - size * 0.3 - b / 2, w, b), b / 2, b / 2), M.paint(cor, a))
            x += w + size * 0.1
    return x


def fs(c, s, x, y, size, est="g", cor=None, a=1.0, align="left"):
    """como E.formula, com índice: "η = 1 − f{T_f}{T_q}". Devolve a largura"""
    nos = _sub_nos(E._ler(s)[0])
    w = _med(nos, size, est)
    if a > 0 and c is not None:
        xi = x - w / 2 if align == "center" else x - w if align == "right" else x
        _des(c, nos, xi, y, size, est, cor or TINTA, a)
    return w


def fs_em(c, t, t0, s, x, y, size, est="g", cor=TINTA, align="left"):
    E.foco(c, t, t0, 0.5, lambda a: fs(c, s, x, y, size, est, cor, a, align))



# ---------------- peças desta aula ----------------
PARTES = ("Q", " = ", "τ", " + ", "ΔU")
IDX = {"Q": 0, "τ": 2, "ΔU": 4}


def lei_zera(c, t, t0, termo, tz, x, y, size=110, escuro=False, align="left"):
    """Q = τ + ΔU com o termo que some riscado em tz e um 0 laranja embaixo"""
    tinta = BR if escuro else TINTA
    ws = [E.formula(None, p, 0, 0, size, "g", a=0) for p in PARTES]
    x0 = x - sum(ws) / 2 if align == "center" else x
    E.foco(c, t, t0, 0.5, lambda a: [E.formula(c, p, x0 + sum(ws[:i]), y, size, "g", tinta, a) for i, p in enumerate(PARTES)])
    if termo and t >= tz:
        i = IDX[termo]
        xa, xb = x0 + sum(ws[:i]), x0 + sum(ws[:i + 1])
        E.risco(c, xa - 8, y + 8, xb + 8, y - size * 0.75, t, tz, cor=E.COR, largura=max(8, size * 0.09))
        E.foco(c, t, tz + 0.3, 0.4, lambda a: E.formula(c, "0", (xa + xb) / 2, y + size * 0.95, size * 0.75, "g", E.CLARO if escuro else COR, a, "center"))


def titulo(c, t, t0, n, nome, extra=None):
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, XE + 46, 190, 46, a=a), centro(c, str(n), XE + 46, 214, 60, "g", BR, a)))
    E.frase(c, t, t0 + 0.1, [(nome, "g", 84, COR)], XE + 120, 220)
    if extra:
        E.frase(c, t, extra[0], ps(extra[1], "i", 58, TINTA2), XE + 120, 300, passo=0.08)


def refri(c, t, x, y, s, a=1.0, fumaca=0.0):
    """garrafa de refrigerante aberta: (x, y) = base; fumaca de 0 a 1"""
    if a <= 0:
        return
    w, h = s * 0.5, s
    p = skia.Path()
    p.moveTo(x - w / 2, y); p.lineTo(x - w / 2, y - h * 0.55)
    p.cubicTo(x - w / 2, y - h * 0.75, x - w * 0.18, y - h * 0.78, x - w * 0.18, y - h * 0.92)
    p.lineTo(x - w * 0.18, y - h); p.lineTo(x + w * 0.18, y - h); p.lineTo(x + w * 0.18, y - h * 0.92)
    p.cubicTo(x + w * 0.18, y - h * 0.78, x + w / 2, y - h * 0.75, x + w / 2, y - h * 0.55)
    p.lineTo(x + w / 2, y); p.close()
    c.drawPath(p, M.paint("#7A3B12", a * 0.85))
    c.drawPath(p, M.paint(TINTA, a, stroke=5))
    M.rrect(c, x - w / 2 + 4, y - h * 0.5, w - 8, h * 0.2, 6, E.COR, a)
    for k in range(5):
        u = (t * 0.6 + k / 5) % 1.0
        c.drawCircle(x + 14 * math.sin(k * 2 + t * 2), y - h - 20 - u * 160, 22 + 30 * u, M.paint("#B8C2CC", a * fumaca * (1 - u) * 0.9))


def isolado(c, t, x, y, w, h, frac, a=1.0, agit=0.4, cor=None):
    """cilindro com parede isolante (hachurada) por fora: adiabática"""
    if a <= 0:
        return
    g = 34
    M.rrect(c, x - g, y - 30, g, h + 30 + g, 4, "#E9E2D0", a)
    M.rrect(c, x + w, y - 30, g, h + 30 + g, 4, "#E9E2D0", a)
    M.rrect(c, x - g, y + h, w + 2 * g, g, 4, "#E9E2D0", a)
    for k in range(int((h + 60) / 26)):
        yy = y - 20 + k * 26
        M.line(c, x - g + 4, yy + 18, x - 4, yy, TINTA2, a * 0.6, 3)
        M.line(c, x + w + 4, yy + 18, x + w + g - 4, yy, TINTA2, a * 0.6, 3)
    return cilindro(c, t, x, y, w, h, frac, a, agit, cor)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    if t < C["s02"]:
        E.foco(c, t, C["s01.a"], 0.6, lambda a: refri(c, t, 1440, 920, 520, a, ep(t, C["s01.b"], 0.8)))
        E.frase(c, t, C["s01.a"], ps("abra um", "i", 84) + [("refrigerante", "g", 84, COR)], XE, 300, passo=0.12)
        E.frase(c, t, C["s01.b"], ps("uma", "i", 72) + [("fumacinha", "g", 72)] + ps("no gargalo", "i", 72), XE, 440, passo=0.1)
        E.frase(c, t, C["s01.c"], ps("vapor de água que", "i", 62) + [("esfriou", "g", 60, FRIO)], XE, 560, passo=0.1)
        E.frase(c, t, C["s01.d"], ps("quem esfriou", "i", 84) + [("o gás?", "g", 84, COR)], XE, 760, passo=0.12)
        E.frase(c, t, C["s01.d"] + 1.6, ps("nada gelado encostou nele", "i", 56, TINTA2), XE, 860, passo=0.08)
        return
    promessa(c, t, C, "s02", (("s02.b", "qual termo vira zero"), ("s02.c", "quase sem conta")))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    def lei(a, x, y):
        E.formula(c, "Q = τ + ΔU", x - 60, y + 20, 56, "g", TINTA, a, "center")

    def temp(a, x, y):
        M.rrect(c, x + 110, y - 90, 26, 130, 13, BR, a)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x + 110, y - 90, 26, 130), 13, 13), M.paint(TINTA, a, stroke=4))
        M.rrect(c, x + 116, y - 40, 14, 80, 7, E.COR, a)
        c.drawCircle(x + 123, y + 60, 28, M.paint(E.COR, a))
    lembrete2(c, t, C, "s03", (("s03.b", "a primeira lei:", "calor, trabalho e U"), ("s03.c", "a energia interna", "acompanha a temperatura")), (lei, temp))


# ---------------- isotérmica ----------------
def b_isotermica(c, t, C, b):
    titulo(c, t, C["s04.a"], 1, "isotérmica", (C["s04.b"], "iso: igual  ·  térmica: temperatura"))
    lei_zera(c, t, C["s04.c"] - 0.6, "ΔU", C["s04.c"], XE, 520, 110)
    E.foco(c, t, C["s04.d"], 0.5, lambda a: E.formula(c, "Q = τ", XE, 800, 130, "g", COR, a))
    E.frase(c, t, C["s04.e"], ps("calor e trabalho iguais", "i", 56, TINTA2), XE, 900, passo=0.08)
    x, y, w, h = 1300, 380, 360, 480
    fr = lerp(0.35, 0.7, ease_io(prog(t, C["s05.a"], 2.5)))
    E.foco(c, t, C["s04.c"], 0.6, lambda a: cilindro(c, t, x, y, w, h, fr, a, 0.5))
    if t >= C["s04.c"]:
        F.termometro(c, t, C["s04.c"], x + w + 120, y + h, 300, 50, 0, 100, (), d=0.6)
    seta_calor(c, t, C["s05.a"], (x + w / 2, y + h + 200), (x + w / 2, y + h + 20), None, d=0.6, amp=12, ondas=2)
    E.foco(c, t, C["s05.a"] + 0.4, 0.4, lambda a: F.medida(c, 800, "J", x + w / 2 + 50, y + h + 150, 56, COR, a))
    if t >= C["s05.b"]:
        ye = y + h * (1 - fr)
        seta_reta(c, t, C["s05.b"], (x - 80, ye + 40), (x - 80, ye - 220), None, TINTA)
        E.foco(c, t, C["s05.b"] + 0.3, 0.4, lambda a: F.medida(c, 800, "J", x - 110, ye - 90, 56, TINTA, a, "right"))
    E.foco(c, t, C["s05.c"], 0.4, lambda a: E.pilula(c, "nada fica guardado: T não muda", x + w / 2, 260, 44, "g", fundo=TINTA, a=a))


# ---------------- isovolumétrica ----------------
def b_isovolumetrica(c, t, C, b):
    titulo(c, t, C["s06.a"], 2, "isovolumétrica", (C["s06.a"] + 1.4, "também chamada de isocórica"))
    if t < C["s07"]:
        E.frase(c, t, C["s06.b"], ps("volume igual:", "i", 66) + [("ΔV = 0", "g", 64, COR)], XE, 440, passo=0.1)
        E.foco(c, t, C["s06.c"], 0.4, lambda a: E.formula(c, "τ = p · ΔV = p · 0 = 0", XE, 560, 74, "g", TINTA, a))
        lei_zera(c, t, C["s06.d"] - 0.3, "τ", C["s06.d"], XE, 740, 110)
        E.foco(c, t, C["s06.e"], 0.5, lambda a: E.formula(c, "Q = ΔU", XE + 900, 740, 110, "g", COR, a))
        E.frase(c, t, C["s06.f"], ps("todo o calor fica no gás", "i", 58, TINTA2), XE, 960, passo=0.08)
        return
    # s07: recipiente rígido e o gráfico
    x, y, w, h = 300, 450, 380, 300
    ag = 0.3 + 0.6 * ep(t, C["s07.c"], 1.0)

    def rigido(a):
        particulas(c, t, x, y, w, h, ag, E.COR, a, n=(5, 3), r=16)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x - 10, y - 10, w + 20, h + 20), 30, 30), M.paint(TINTA, a, stroke=14))
    E.foco(c, t, C["s07.a"], 0.5, rigido)
    seta_calor(c, t, C["s07.a"] + 0.4, (x + w / 2, y + h + 230), (x + w / 2, y + h + 30), None, d=0.6, amp=12, ondas=2)
    E.foco(c, t, C["s07.a"] + 0.8, 0.4, lambda a: F.medida(c, 200, "J", x + w / 2 + 50, y + h + 170, 56, COR, a))
    E.foco(c, t, C["s07.b"], 0.4, lambda a: E.pilula(c, "rígido: volume parado", x + w / 2, y - 80, 44, "g", fundo=TINTA, a=a))
    E.foco(c, t, C["s07.c"], 0.4, lambda a: E.formula(c, "ΔU = +200 J", x + w + 80, y + h / 2 + 30, 70, "g", COR, a))
    P = F.grafico(c, t, C["s07.d"], 1180, 330, 600, 520, 0, 4, 0, 4, "V", "p", 1, 1, marcas_x=[], marcas_y=[])
    if t >= C["s07.d"] + 0.5:
        M.line(c, P.x(2), P.y(1), P.x(2), lerp(P.y(1), P.y(3), ease_io(prog(t, C["s07.d"] + 0.5, 0.8))), E.COR, 1.0, 10, cap_round=True)
    E.foco(c, t, C["s07.e"], 0.4, lambda a: E.pilula(c, "área zero: τ = 0", P.x(2), P.y(3.6), 46, "g", fundo=E.COR, a=a))


# ---------------- adiabática ----------------
def b_adiabatica(c, t, C, b):
    titulo(c, t, C["s08.a"], 3, "adiabática", (C["s08.b"], "o calor não atravessa: sem troca de calor"))
    if t < C["s09"]:
        x, y, w, h = 1340, 400, 320, 440
        E.foco(c, t, C["s08.c"], 0.6, lambda a: isolado(c, t, x, y, w, h, 0.55, a))
        E.foco(c, t, C["s08.c"] + 0.3, 0.4, lambda a: E.pilula(c, "bem isolado", x + w / 2, y - 260, 46, "g", fundo=TINTA, a=a))
        E.foco(c, t, C["s08.d"], 0.4, lambda a: E.pilula(c, "ou rápido demais", x + w / 2, y - 180, 46, "g", fundo=TINTA2, a=a))
        lei_zera(c, t, C["s08.e"] - 0.3, "Q", C["s08.e"], XE, 520, 110)
        E.foco(c, t, C["s08.f"], 0.5, lambda a: E.formula(c, "0 = τ + ΔU", XE, 800, 96, "g", TINTA, a))
        E.foco(c, t, C["s08.g"], 0.5, lambda a: E.formula(c, "ΔU = −τ", XE + 620, 800, 110, "g", COR, a))
        return
    if t < C["s10"]:
        E.frase(c, t, C["s09.a"], ps("expande e faz trabalho:", "i", 62), XE, 410, passo=0.08)
        E.frase(c, t, C["s09.a"] + 1.2, [("paga", "g", 60, COR)] + ps("com a energia interna", "i", 62), XE, 490, passo=0.08)
        E.frase(c, t, C["s09.b"], [("esfria", "g", 80, FRIO)], XE, 610)
        x, y, w, h = 1150, 430, 280, 400
        fr = lerp(0.4, 0.75, ease_io(prog(t, C["s09.a"], 2.0)))
        cor = E.mix(E.COR, FRIO, ep(t, C["s09.b"], 1.0))
        E.foco(c, t, C["s09.a"], 0.5, lambda a: isolado(c, t, x, y, w, h, fr, a, 0.5 - 0.35 * ep(t, C["s09.b"], 1.0), cor))
        E.foco(c, t, C["s09.c"], 0.6, lambda a: refri(c, t, 1640, 900, 400, a, 1.0))
        E.frase(c, t, C["s09.d"], ps("comprimido depressa:", "i", 62) + [("esquenta", "g", 60, COR)], XE, 760, passo=0.08)
        E.frase(c, t, C["s09.d"] + 1.8, ps("como o ar da bomba de pneu", "i", 54, TINTA2), XE, 860, passo=0.08)
        return
    E.frase(c, t, C["s10"], ps("exemplo:", "i", 62, TINTA2), XE, 400)
    passos(c, t, [(C["s10.a"], "comprimido: recebe 300 J", TINTA), (C["s10.b"], "τ = −300 J", FRIO), (C["s10.c"], "ΔU = −τ = −(−300)", TINTA)], XE, 520, 130, 70)
    bola_txt(c, t, C["s10.d"], "+300 J", 1450, 640, 140, 72)
    E.foco(c, t, C["s10.e"], 0.4, lambda a: E.pilula(c, "o gás esquenta", 1450, 870, 54, "g", fundo=E.COR, a=a))


# ---------------- ciclo e isobárica ----------------
def b_ciclo(c, t, C, b):
    if t < C["s12"]:
        titulo(c, t, C["s11.a"], 4, "ciclo", (C["s11.b"], "termina onde começou"))
        lei_zera(c, t, C["s11.c"] - 0.3, "ΔU", C["s11.c"], XE, 520, 110)
        E.foco(c, t, C["s11.d"], 0.5, lambda a: E.formula(c, "Q = τ", XE, 780, 120, "g", COR, a))
        P = F.grafico(c, t, C["s11.b"], 1200, 360, 600, 440, 0, 5, 0, 250, "V (m³)", "p (kPa)", 1, 50, marcas_x=[1, 4], marcas_y=[100, 200])
        retangulo_area(c, t, C["s11.e"], P, 1, 4, 100, 200, E.COR, 0.4)
        ciclo(c, t, C["s11.b"] + 0.4, P, [(1, 200), (4, 200), (4, 100), (1, 100)], d=1.6)
        E.foco(c, t, C["s11.e"] + 0.5, 0.4, lambda a: F.medida(c, 300, "kJ", P.x(2.5), P.y(150) + 18, 56, TINTA, a, "center"))
        E.foco(c, t, C["s11.f"], 0.5, lambda a: E.formula(c, "Q = 300 kJ", XE, 910, 84, "g", TINTA, a))
        E.frase(c, t, C["s11.f"] + 1.0, ps("o saldo de calor de cada volta", "i", 54, TINTA2), XE + 520, 910, passo=0.08)
        return
    E.frase(c, t, C["s12.a"], ps("e a", "i", 84) + [("isobárica?", "g", 84, COR)], XE, 260, passo=0.12)
    E.frase(c, t, C["s12.a"] + 1.0, ps("pressão constante", "i", 58, TINTA2), XE, 350, passo=0.08)
    E.foco(c, t, C["s12.b"], 0.5, lambda a: E.pilula(c, "nenhum termo some", XE + 330, 520, 60, "g", fundo=TINTA, a=a))
    lei_zera(c, t, C["s12.c"], None, 0, XE, 760, 130)
    E.frase(c, t, C["s12.d"], ps("use a lei", "i", 70) + [("inteira", "g", 70, COR)], XE, 930, passo=0.1)
    x, y, w, h = 1340, 380, 320, 480
    fr = lerp(0.35, 0.7, ease_io(prog(t, C["s12.c"], 2.0)))
    E.foco(c, t, C["s12.b"], 0.6, lambda a: cilindro(c, t, x, y, w, h, fr, a, 0.3 + 0.5 * ep(t, C["s12.c"], 1.5)))
    seta_calor(c, t, C["s12.c"], (x - 280, y + h - 80), (x - 20, y + h - 80), "Q", d=0.6, amp=12, ondas=2)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s13"], [("cuidado", "g", 96, ERRADO)], XE, 200)
    E.frase(c, t, C["s13.a"], [("“isotérmica", "i", 76), ("não", "i", 76), ("troca", "i", 76), ("calor”", "i", 76)], XE + 480, 200, passo=0.12)
    if t >= C["s13.b"]:
        E.risco(c, XE + 470, 220, XE + 1300, 150, t, C["s13.b"], largura=12)
    E.foco(c, t, C["s13.b"] + 0.4, 0.4, lambda a: E.formula(c, "isotérmica: Q = τ, e não zero", XE, 400, 70, "g", CERTO, a))
    E.frase(c, t, C["s13.c"], ps("a temperatura fica igual porque o calor", "i", 56) + [("sai como trabalho", "g", 54, COR)], XE, 520, passo=0.07)
    E.foco(c, t, C["s13.d"], 0.4, lambda a: E.formula(c, "adiabática: Q = 0", XE, 720, 90, "g", TINTA, a))
    E.frase(c, t, C["s13.e"], ps("e nela a", "i", 74) + [("temperatura", "g", 70, COR), ("muda", "g", 70, COR)], XE, 880, passo=0.1)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    if t < C["s15"]:
        E.frase(c, t, C["s14.a"], ps("o que", "i", 74, CLARO) + [("não", "g", 72, BR), ("muda", "g", 72, BR)] + ps("zera um termo", "i", 74, CLARO), W / 2, 200, "center", 0.12)
        linhas = (("s14.b", "temperatura parada", "ΔU = 0", "isotérmica"), ("s14.c", "volume parado", "τ = 0", "isovolumétrica"),
                  ("s14.d", "calor sem passar", "Q = 0", "adiabática"), ("s14.e", "voltou ao começo", "ΔU = 0", "ciclo"))
        for i, (k, l, r, nome) in enumerate(linhas):
            y = 380 + i * 160
            E.foco(c, t, C[k], 0.4, lambda a, l=l, y=y: E.formula(c, l, 900, y, 64, "g", BR, a, "right"))
            E.foco(c, t, C[k] + 0.2, 0.4, lambda a, y=y: E.formula(c, "→", 960, y, 64, "g", E.CLARO, a, "center"))
            E.foco(c, t, C[k] + 0.4, 0.4, lambda a, r=r, y=y: E.formula(c, r, 1030, y, 72, "g", E.CLARO, a))
            E.foco(c, t, C[k] + 0.6, 0.4, lambda a, nome=nome, y=y: E.escreve(c, nome, 1400, y, 52, "i", CLARO, a))
        return
    E.frase(c, t, C["s15.a"], ps("cada termo zera por", "i", 72, CLARO) + [("um", "g", 70, BR), ("motivo", "g", 70, BR)], W / 2, 220, "center", 0.12)
    for i, (s, ti) in enumerate((("ΔU: a temperatura", 0.8), ("τ: o volume", 2.8), ("Q: a troca de calor", 4.4))):
        E.foco(c, t, C["s15.a"] + ti, 0.4, lambda a, s=s, i=i: E.formula(c, s, W / 2, 390 + i * 120, 70, "g", BR, a, "center"))
    E.frase(c, t, C["s15.b"], [("não", "g", 64, ERRADO), ("compensa", "i", 68, CLARO), ("na", "i", 68, CLARO), ("isobárica:", "g", 64, BR)], W / 2, 830, "center", 0.12)
    E.frase(c, t, C["s15.c"], ps("faça a conta inteira", "i", 64, CLARO), W / 2, 950, "center", 0.1)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s16"], ps("hora de testar", "i", 72, COR), XE, 200)
    E.frase(c, t, C["s16.a"], [("expansão", "g", 76), ("adiabática", "g", 76, COR)], XE, 360, passo=0.15)
    E.frase(c, t, C["s16.b"], ps("o gás faz", "i", 74) + [("500 J", "g", 72, COR)] + ps("de trabalho", "i", 74), XE, 490, passo=0.1)
    E.frase(c, t, C["s16.c"], [("ΔU", "g", 80, COR), ("=", "g", 80), ("?", "g", 80, COR)], XE, 660, passo=0.12)
    E.frase(c, t, C["s16.d"], [("esquenta", "g", 70), ("ou", "i", 74), ("esfria?", "g", 70, COR)], XE, 800, passo=0.12)
    if t >= C["s17"]:
        E.relogio(c, t, C["s17.a"], cx=1460, cy=440, r=200)
    else:
        E.foco(c, t, C["s16.a"], 0.5, lambda a: isolado(c, t, 1340, 400, 300, 440, lerp(0.4, 0.7, ease_io(prog(t, C["s16.a"] + 0.3, 1.5))), a))


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    lei_zera(c, t, C["s18.a"] - 0.4, "Q", C["s18.a"], XE, 260, 96)
    passos(c, t, [(C["s18.b"], "expansão: τ = +500 J", TINTA), (C["s18.c"], "ΔU = −τ", TINTA)], XE, 520, 130, 72)
    bola_txt(c, t, C["s18.d"], "−500 J", 520, 860, 130, 70)
    x, y, w, h = 1300, 400, 300, 440
    fr = lerp(0.4, 0.7, ease_io(prog(t, C["s18.b"], 1.5)))
    cor = E.mix(E.COR, FRIO, ep(t, C["s18.e"], 1.0))
    E.foco(c, t, C["s18"], 0.5, lambda a: isolado(c, t, x, y, w, h, fr, a, 0.5 - 0.35 * ep(t, C["s18.e"], 1.0), cor))
    E.foco(c, t, C["s18.e"], 0.4, lambda a: E.pilula(c, "a energia interna caiu: esfria", x + w / 2, 960, 46, "g", fundo=FRIO, a=a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def r():
        resumo(c, t, C, (("s19.a", [("isotérmica", "g", 64), ("e", "i", 64), ("ciclo:", "g", 64), ("ΔU = 0", "g", 64, COR)]),
                         ("s19.b", [("isovolumétrica:", "g", 64), ("τ = 0", "g", 64, COR)]),
                         ("s19.c", [("adiabática:", "g", 64), ("Q = 0", "g", 64, COR)]),
                         ("s19.d", [("isobárica:", "g", 64), ("a", "i", 64), ("lei", "i", 64), ("inteira", "i", 64)])), y0=360, dy=160)
    E.saida(c, t, C["s20"] - 0.1, r)
    if t < C["s20"]:
        return
    E.frase(c, t, C["s20"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C["s20.a"], ps("o ciclo vira", "i", 96) + [("motor", "g", 104, COR)], XE, 410, passo=0.12)
    E.frase(c, t, C["s20.b"], ps("o rendimento de uma máquina térmica", "i", 58), XE, 530, passo=0.08)
    maquina(c, t, dict(q=C["s20.b"], m=C["s20.b"] + 0.3, f=C["s20.b"] + 0.5, Qq=C["s20.c"], tau=C["s20.c"] + 0.4, Qf=C["s20.c"] + 0.8),
            cx=700, y0=580, y1=1050, w=460, k=0.7)
    inscreva(c, t, C["s20.d"], C["s20.e"])


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, isotermica=b_isotermica, isovolumetrica=b_isovolumetrica, adiabatica=b_adiabatica,
              ciclo=b_ciclo, erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
