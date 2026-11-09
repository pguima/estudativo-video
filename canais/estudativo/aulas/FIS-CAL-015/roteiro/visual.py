"""Visual — Estudativo · FIS-CAL-015: Carnot, o rendimento máximo (trilha Calor e Termodinâmica).

Segue a linguagem visual da Física (cabeçalho do visual.py da FIS-CIN-001), a da trilha Calor e Termodinâmica (cabeçalho do
visual.py da FIS-CAL-001) e as peças da termodinâmica do cabeçalho do visual.py da FIS-CAL-011 (máquina térmica, `fs` para
índice). Nesta aula:
- AS DUAS FONTES como dois termômetros lado a lado: o da fonte quente em laranja, o da fria em azul, com a temperatura em
  °C ao lado e, na conversão, em K (laranja).
- O LIMITE DE CARNOT numa régua de rendimento (`regua`) de 0 a 100 %: a marca de Carnot é uma linha laranja; a máquina
  testada é uma seta: abaixo da linha = possível (verde), acima = impossível (vermelho).
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
ARQUIVO_FINAL = "estudativo_FIS-CAL-015_carnot_rendimento_maximo.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("carnot", "exemplo", "temperaturas", "atalho", "questao", "fim"))
BR = "#FFFFFF"
FRIO = F.NEG
GELO = "#A9D8F5"
AGUA = "#5BA8E0"

# todas as contas da aula (η máx = 1 − Tf/Tq, em kelvin)
K = lambda c: c + 273
assert K(327) == 600 and K(27) == 300 and 1 - 300 / 600 == 0.5 and 60 > 50
assert round((1 - 27 / 327) * 100) == 92                       # o erro: Celsius
assert (327 - 27) / K(327) == 0.5                              # atalho: diferença sobre a quente
assert K(227) == 500 and (227 - 27) / 500 == 0.4 and abs((1 - 300 / 500) - 0.4) < 1e-12 and 45 > 40
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
def fontes(c, t, t0, x, yb, tq, tf, h=380, gap=260, tk=None, kq=None, kf=None):
    """os dois termômetros: quente (laranja) e fria (azul), com °C ao lado; tk = instante do kelvin (kq, kf)"""
    if t < t0:
        return
    F.termometro(c, t, t0, x, yb, h, 85, 0, 100, (), d=0.8)
    F.termometro(c, t, t0 + 0.3, x + gap, yb, h, 25, 0, 100, (), cor=FRIO, d=0.8)
    if tq is not None:
        E.foco(c, t, t0 + 0.6, 0.4, lambda a: (F.medida(c, tq, "°C", x, yb + 110, 52, COR, a, "center"),
                                               F.medida(c, tf, "°C", x + gap, yb + 110, 52, FRIO, a, "center")))
    if tk is not None:
        E.foco(c, t, tk[0], 0.4, lambda a: F.medida(c, kq, "K", x, yb + 190, 56, TINTA, a, "center"))
        E.foco(c, t, tk[1], 0.4, lambda a: F.medida(c, kf, "K", x + gap, yb + 190, 56, TINTA, a, "center"))


def regua(c, t, t0, x, y, h, carnot, testes=(), size=44):
    """régua vertical de rendimento (0 a 100 %): linha de Carnot em laranja e setas das máquinas testadas.
    testes = [(instante, valor em %, rótulo)]"""
    q = ep(t, t0, 0.5)
    if q <= 0:
        return
    yv = lambda v: y + h - h * v / 100
    M.rrect(c, x - 18, y, 36, h, 18, E.mix(TINTA, BR, 0.88), q)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x - 18, y, 36, h), 18, 18), M.paint(TINTA, q, stroke=4))
    for v in (0, 50, 100):
        E.escreve(c, f"{v} %", x - 140, yv(v) + 14, 40, "b", TINTA2, q)
    M.rrect(c, x - 14, yv(carnot), 28, h * carnot / 100, 14, E.COR, q * 0.5)
    M.line(c, x - 70, yv(carnot), x + 70, yv(carnot), E.COR, q, 8)
    E.escreve(c, "Carnot", x + 90, yv(carnot) + 14, size, "g", COR, q)
    for (ti, v, rot) in testes:
        ok = v < carnot
        cor = CERTO if ok else ERRADO
        E.foco(c, t, ti, 0.4, lambda a, v=v, cor=cor, rot=rot, ok=ok: (
            F.seta(c, x + 260, yv(v), x + 40, yv(v), cor, a, 8),
            E.escreve(c, rot, x + 280, yv(v) + 16, size, "g", cor, a),
            E.selo(c, x + 280 + E.larg(rot, "g", size) + 60, yv(v) - 2, 34, ok, a)))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    if t < C["s02"]:
        E.frase(c, t, C["s01.a"], ps("um inventor e seu", "i", 80) + [("motor", "g", 80, COR)], XE, 280, passo=0.12)
        fontes(c, t, C["s01.b"], 1300, 760, 327, 27)
        E.foco(c, t, C["s01.b"], 0.4, lambda a: E.escreve(c, "fonte quente", 1200, 300, 40, "b", COR, a))
        E.foco(c, t, C["s01.c"], 0.4, lambda a: E.escreve(c, "fonte fria", 1480, 300, 40, "b", FRIO, a))
        E.foco(c, t, C["s01.d"], 0.5, lambda a: E.formula(c, "η = 60 %", XE, 500, 130, "g", TINTA, a))
        E.frase(c, t, C["s01.e"], ps("é mentira?", "i", 84) + [("sem", "g", 76), ("abrir", "g", 76, COR)], XE, 720, passo=0.12)
        E.frase(c, t, C["s01.e"] + 1.4, ps("o motor", "i", 84), XE, 830, passo=0.12)
        return
    promessa(c, t, C, "s02", (("s02.b", "o rendimento máximo"), ("s02.c", "testar a máquina")))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    def rend(a, x, y):
        fs(c, "η = 1 − f{Q_f}{Q_q}", x - 60, y + 20, 52, "g", TINTA, a, "center")

    def kel(a, x, y):
        E.formula(c, "+ 273", x - 20, y + 20, 64, "g", TINTA, a, "center")
    lembrete2(c, t, C, "s03", (("s03.b", "o rendimento:", "um menos a razão"), ("s03.c", "de Celsius para kelvin:", "some 273")), (rend, kel))


# ---------------- Carnot ----------------
def b_carnot(c, t, C, b):
    if t < C["s05"]:
        E.frase(c, t, C["s04"] + 0.3, [("1824", "g", 150, TINTA)], XE, 300)
        E.frase(c, t, C["s04.a"], [("Sadi", "g", 80), ("Carnot", "g", 80, COR)], XE, 430, passo=0.12)
        E.frase(c, t, C["s04.a"] + 0.8, ps("engenheiro francês", "i", 58, TINTA2), XE, 510, passo=0.08)
        E.frase(c, t, C["s04.b"], ps("o melhor rendimento possível", "i", 60), XE, 660, passo=0.08)
        E.frase(c, t, C["s04.b"] + 1.4, ps("entre duas fontes?", "i", 60), XE, 740, passo=0.08)
        E.foco(c, t, C["s04.c"], 0.5, lambda a: E.pilula(c, "só depende das temperaturas", 1400, 330, 54, "g", fundo=E.COR, a=a))
        fontes(c, t, C["s04.c"] + 0.4, 1300, 860, None, None, h=340)
        E.foco(c, t, C["s04.d"], 0.4, lambda a: (E.pilula(c, "combustível", XE + 230, 920, 50, "g", fundo=TINTA2, a=a),
                                                E.pilula(c, "tamanho do motor", XE + 730, 920, 50, "g", fundo=TINTA2, a=a)))
        if t >= C["s04.d"] + 0.8:
            E.risco(c, XE + 60, 945, XE + 980, 895, t, C["s04.d"] + 0.8, largura=10)
        return
    if t < C["s06"]:
        E.frase(c, t, C["s05.a"], ps("a máquina ideal:", "i", 76) + [("Carnot", "g", 80, COR)], XE, 260, passo=0.12)
        E.frase(c, t, C["s05.b"], [("2", "g", 76, COR), ("isotérmicas", "g", 70), ("+", "g", 70, TINTA2), ("2", "g", 76, COR), ("adiabáticas", "g", 70)], XE, 420, passo=0.12)
        E.frase(c, t, C["s05.b"] + 1.6, ps("sem atrito, sem perdas além do", "i", 56, TINTA2), XE, 510, passo=0.08)
        E.foco(c, t, C["s05.b"] + 2.6, 0.4, lambda a: fs(c, "Q_f", XE + 830, 510, 56, "g", TINTA2, a))
        fs_em(c, t, C["s05.c"], "f{Q_f}{Q_q} = f{T_f}{T_q}", XE, 790, 150, cor=TINTA)
        E.foco(c, t, C["s05.c"] + 0.6, 0.4, lambda a: E.escreve(c, "calores", XE + 20, 960, 46, "i", TINTA2, a))
        E.foco(c, t, C["s05.c"] + 0.9, 0.4, lambda a: E.escreve(c, "temperaturas", XE + 400, 960, 46, "i", TINTA2, a))
        return
    E.foco(c, t, C["s06.a"] - 0.3, 0.4, lambda a: E.pilula(c, "rendimento máximo (Carnot)", XE + 330, 230, 52, "g", fundo=E.COR, a=a))
    fs_em(c, t, C["s06.a"], "η = 1 − f{T_f}{T_q}", XE, 470, 170)
    for i, (k, l, n) in enumerate((("s06.b", "T_f", "temperatura da fonte fria (K)"), ("s06.c", "T_q", "temperatura da fonte quente (K)"))):
        E.foco(c, t, C[k], 0.4, lambda a, l=l, n=n, i=i: (fs(c, l, XE, 680 + i * 100, 64, "g", COR, a),
                                                         E.escreve(c, n, XE + 130, 680 + i * 100, 56, "i", TINTA, a)))
    E.foco(c, t, C["s06.d"], 0.4, lambda a: E.pilula(c, "em kelvin", XE + 1220, 690, 60, "g", fundo=TINTA, a=a))
    E.foco(c, t, C["s06.e"], 0.4, lambda a: E.formula(c, "máquina real: η < η de Carnot", XE, 960, 66, "g", COR, a))


# ---------------- exemplo ----------------
def b_exemplo(c, t, C, b):
    if t < C["s09"]:
        E.frase(c, t, C["s07"], ps("testando o inventor", "i", 66, TINTA2), XE, 200)
        fs_em(c, t, C["s07.a"], "T_q = 327 + 273", XE, 340, 72)
        E.foco(c, t, C["s07.b"], 0.4, lambda a: E.formula(c, "= 600 K", XE + 620, 340, 72, "g", COR, a))
        fs_em(c, t, C["s07.c"], "T_f = 27 + 273", XE, 460, 72)
        E.foco(c, t, C["s07.d"], 0.4, lambda a: E.formula(c, "= 300 K", XE + 620, 460, 72, "g", FRIO, a))
        E.foco(c, t, C["s08.a"], 0.4, lambda a: E.formula(c, "f{300}{600} = 0,5", XE, 640, 80, "g", TINTA, a))
        E.foco(c, t, C["s08.b"], 0.4, lambda a: E.formula(c, "η = 1 − 0,5", XE, 800, 80, "g", TINTA, a))
        bola_txt(c, t, C["s08.c"], "50 %", XE + 700, 770, 100, 64)
        regua(c, t, C["s08.c"] + 0.3, 1300, 220, 700, 50, [(C["s08.e"], 60, "60 %")])
        E.foco(c, t, C["s08.d"], 0.4, lambda a: E.pilula(c, "nem a ideal passa de 50 %", XE + 400, 960, 50, "g", fundo=E.COR, a=a))
        return
    E.frase(c, t, C["s09"], [("o", "i", 80), ("teste", "g", 80, COR)], XE, 220)
    linhas = (("s09.a", "η menor que Carnot", "possível", CERTO), ("s09.b", "η maior que Carnot", "impossível", ERRADO), ("s09.c", "η igual a Carnot", "só a ideal", TINTA2))
    for i, (k, l, r, cor) in enumerate(linhas):
        y = 420 + i * 180
        E.foco(c, t, C[k], 0.4, lambda a, l=l, y=y: E.formula(c, l, XE, y, 70, "g", TINTA, a))
        E.foco(c, t, C[k] + 0.4, 0.4, lambda a, r=r, y=y, cor=cor: E.pilula(c, r, XE + 1050, y - 26, 60, "g", fundo=cor, a=a))


# ---------------- temperaturas ----------------
def b_temperaturas(c, t, C, b):
    E.frase(c, t, C["s10.a"], ps("como", "i", 80) + [("melhorar", "g", 80, COR)] + ps("a máquina?", "i", 80), XE, 230, passo=0.12)
    x, yb = 1300, 820
    if t >= C["s10.b"]:
        F.termometro(c, t, C["s10.b"], x, yb, 420, lerp(60, 92, ease_io(prog(t, C["s10.b"] + 0.3, 1.0))), 0, 100, (), d=0.01)
        E.foco(c, t, C["s10.b"], 0.4, lambda a: E.escreve(c, "mais quente", x - 110, yb + 110, 44, "g", COR, a))
    if t >= C["s10.c"]:
        F.termometro(c, t, C["s10.c"], x + 300, yb, 420, lerp(40, 8, ease_io(prog(t, C["s10.c"] + 0.3, 1.0))), 0, 100, (), cor=FRIO, d=0.01)
        E.foco(c, t, C["s10.c"], 0.4, lambda a: E.escreve(c, "mais fria", x + 210, yb + 110, 44, "g", FRIO, a))
    E.frase(c, t, C["s10.b"], ps("fonte quente", "i", 64) + [("mais quente", "g", 62, COR)], XE, 380, passo=0.08)
    E.frase(c, t, C["s10.c"], ps("ou fonte fria", "i", 64) + [("mais fria", "g", 62, FRIO)], XE, 480, passo=0.08)
    fs_em(c, t, C["s10.d"], "100 % só com T_f = 0 K", XE, 640, 74)
    E.foco(c, t, C["s10.e"], 0.4, lambda a: E.pilula(c, "zero absoluto: não dá para atingir", XE + 470, 740, 50, "g", fundo=TINTA, a=a))
    E.foco(c, t, C["s10.f"], 0.4, lambda a: E.formula(c, "nenhuma máquina chega a 100 %", XE, 880, 64, "g", COR, a))
    E.frase(c, t, C["s10.g"], ps("usinas modernas: vapor cada vez mais quente", "i", 54, TINTA2), XE, 990, passo=0.06)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s11"], [("cuidado", "g", 96, ERRADO)], XE, 200)
    E.frase(c, t, C["s11.a"], ps("usar", "i", 76) + [("graus", "g", 76, ERRADO), ("Celsius", "g", 76, ERRADO)], XE + 480, 200, passo=0.12)
    E.foco(c, t, C["s11.b"], 0.4, lambda a: E.formula(c, "1 − f{27}{327}", W / 2 - 200, 470, 120, "g", TINTA, a, "center"))
    E.foco(c, t, C["s11.c"], 0.4, lambda a: E.formula(c, "≈ 92 %?", W / 2 + 330, 470, 120, "g", ERRADO, a, "center"))
    if t >= C["s11.d"]:
        E.risco(c, W / 2 + 90, 500, W / 2 + 570, 380, t, C["s11.d"], largura=12)
    E.frase(c, t, C["s11.d"], ps("e o motor de 60 % pareceria", "i", 64) + [("possível", "g", 62, ERRADO)], W / 2, 690, "center", 0.08)
    E.frase(c, t, C["s11.e"], ps("em Celsius, o zero", "i", 66) + [("não", "g", 64, ERRADO)] + ps("é o zero de verdade", "i", 66), W / 2, 860, "center", 0.08)
    E.foco(c, t, C["s11.e"] + 2.0, 0.4, lambda a: E.pilula(c, "use kelvin", W / 2, 980, 56, "g", fundo=CERTO, a=a))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    E.frase(c, t, C["s12"], ps("o atalho de prova", "i", 70, CLARO), W / 2, 160, "center")
    if t < C["s13"]:
        E.frase(c, t, C["s12.a"], ps("a diferença sobre a", "i", 70, CLARO) + [("quente", "g", 70, BR)], W / 2, 300, "center", 0.12)
        E.foco(c, t, C["s12.b"], 0.5, lambda a: fs(c, "η = f{T_q − T_f}{T_q}", W / 2, 560, 160, "g", BR, a, "center"))
        E.foco(c, t, C["s12.c"], 0.4, lambda a: E.pilula(c, "a diferença é a mesma em °C e em K", W / 2, 800, 56, "g", fundo=E.COR, a=a))
        E.frase(c, t, C["s12.c"] + 2.4, ps("o 273 se cancela", "i", 62, CLARO), W / 2, 930, "center", 0.1)
        return
    E.foco(c, t, C["s13.a"], 0.4, lambda a: E.formula(c, "327 − 27 = 300", W / 2, 360, 100, "g", BR, a, "center"))
    E.foco(c, t, C["s13.a"] + 1.4, 0.4, lambda a: centro(c, "direto dos graus Celsius", W / 2, 450, 50, "i", CLARO, a))
    E.foco(c, t, C["s13.b"], 0.4, lambda a: fs(c, "só a quente em kelvin: T_q = 600 K", W / 2, 580, 76, "g", E.CLARO, a, "center"))
    E.foco(c, t, C["s13.c"], 0.4, lambda a: E.formula(c, "f{300}{600} = 50 %", W / 2, 780, 110, "g", BR, a, "center"))
    E.frase(c, t, C["s13.d"], [("não", "g", 56, ERRADO), ("compensa:", "i", 60, CLARO)] + ps("as duas já em kelvin", "i", 60, CLARO), W / 2, 960, "center", 0.1)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s14"], ps("hora de testar", "i", 72, COR), XE, 200)
    E.frase(c, t, C["s14"] + 0.8, ps("numa usina", "i", 72), XE, 320, passo=0.1)
    E.frase(c, t, C["s14.a"], ps("quente:", "i", 70) + [("227 °C", "g", 70, COR)], XE, 450, passo=0.1)
    E.frase(c, t, C["s14.b"], ps("fria:", "i", 70) + [("27 °C", "g", 70, FRIO)], XE, 560, passo=0.1)
    E.frase(c, t, C["s14.c"], [("η", "g", 76, COR), ("máximo", "i", 80), ("=", "g", 76), ("?", "g", 76, COR)], XE, 720, passo=0.12)
    E.frase(c, t, C["s14.d"], [("45 %", "g", 70), ("é", "i", 74), ("possível?", "g", 70, COR)], XE, 850, passo=0.12)
    if t >= C["s15"]:
        E.relogio(c, t, C["s15.a"], cx=1460, cy=440, r=200)
    else:
        fontes(c, t, C["s14.a"], 1300, 760, 227, 27)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    if t < C["s17"]:
        E.frase(c, t, C["s16"], ps("com o atalho", "i", 66, TINTA2), XE, 200)
        E.foco(c, t, C["s16.a"], 0.4, lambda a: E.formula(c, "diferença: 227 − 27 = 200", XE, 360, 72, "g", TINTA, a))
        fs_em(c, t, C["s16.b"], "T_q = 227 + 273 = 500 K", XE, 500, 72, cor=COR)
        E.foco(c, t, C["s16.c"], 0.4, lambda a: E.formula(c, "f{200}{500} = 0,4", XE, 680, 84, "g", TINTA, a))
        bola_txt(c, t, C["s16.e"], "40 %", 1400, 600, 150, 84)
        return
    regua(c, t, C["s17"], 1300, 200, 700, 40, [(C["s17.a"], 45, "45 %")])
    E.frase(c, t, C["s17.a"], [("45", "g", 90, ERRADO), (">", "g", 90), ("40", "g", 90, COR)], XE, 300, passo=0.12)
    E.frase(c, t, C["s17.b"], ps("o projeto é", "i", 76) + [("impossível", "g", 76, ERRADO)], XE, 440, passo=0.12)
    E.foco(c, t, C["s17.c"], 0.4, lambda a: E.formula(c, "1 − f{300}{500} = 1 − 0,6 = 0,4", XE, 680, 70, "g", TINTA2, a))
    E.foco(c, t, C["s17.c"], 0.4, lambda a: E.escreve(c, "pela fórmula completa", XE, 580, 50, "i", TINTA2, a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def r():
        E.frase(c, t, C["s18"], [("resumindo", "i", 92, COR)], W / 2, 180, "center")
        for i, (k, s) in enumerate((("s18.a", "η máximo = 1 − f{T_f}{T_q}"), ("s18.b", "sempre em kelvin"), ("s18.c", "nenhuma máquina real passa dele"))):
            y = 390 + i * 200
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 260, y - 26, 52, a=a), centro(c, str(i + 1), 260, y - 4, 60, "g", BR, a)))
            fs_em(c, t, C[k] + 0.1, s, 360, y, 70, cor=COR if i == 0 else TINTA)
    E.saida(c, t, C["s19"] - 0.1, r)
    if t < C["s19"]:
        return
    E.frase(c, t, C["s19"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C["s19.a"], ps("a máquina", "i", 90) + [("ao", "g", 90, COR), ("contrário", "g", 90, COR)], XE, 410, passo=0.12)
    E.frase(c, t, C["s19.b"], [("geladeira", "g", 70)], XE, 540)
    E.frase(c, t, C["s19.c"], ps("e", "i", 70) + [("entropia", "g", 70, COR)], XE + 370, 540, passo=0.1)
    maquina(c, t, dict(q=C["s19.a"], m=C["s19.a"], f=C["s19.a"], Qq=C["s19.a"] + 0.4, Qf=C["s19.a"] + 0.4, tau=C["s19.a"] + 0.6),
            cx=700, y0=600, y1=1050, w=460, k=0.7, inv=True)
    inscreva(c, t, C["s19.d"], C["s19.e"])


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, carnot=b_carnot, exemplo=b_exemplo, temperaturas=b_temperaturas, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
