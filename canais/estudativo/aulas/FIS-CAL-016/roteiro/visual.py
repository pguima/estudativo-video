"""Visual — Estudativo · FIS-CAL-016: praticando propagação e termodinâmica (trilha Calor e Termodinâmica, prática).

Segue a linguagem visual da Física (cabeçalho do visual.py da FIS-CIN-001), a da trilha Calor e Termodinâmica (cabeçalho do
visual.py da FIS-CAL-001) e as peças da termodinâmica do cabeçalho do visual.py da FIS-CAL-011 (cilindro, máquina, ciclo, `fs`).
Cada situação: enunciado à esquerda com o número na esfera laranja, desenho à direita; na pausa, o relógio toma o lugar do
desenho. Na resposta, a conta empilhada à esquerda e o resultado na esfera (verde quando fecha a situação).
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
ARQUIVO_FINAL = "estudativo_FIS-CAL-016_praticando_propagacao_termodinamica.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("questao1", "questao2", "questao3", "questao4", "questao5", "fim"))
BR = "#FFFFFF"
FRIO = F.NEG
GELO = "#A9D8F5"
AGUA = "#5BA8E0"
LUZ = "#F2B705"

# todas as contas da aula
assert (300 - 100) * (5 - 2) == 600 and 300 * 3 == 900          # 2: ciclo (kPa × L = J); o erro: só a área de cima
assert 100 * (6 - 2) == 400 and 1000 - 400 == 600                # 3: isobárica; o erro dá 1000
assert 1 - 675 / 1500 == 0.55 and 427 + 273 == 700 and (427 - 77) / 700 == 0.5 and 55 > 50   # 4: motor impossível
assert round((1 - 77 / 427) * 100) == 82                          # 4: o erro de usar Celsius
assert 500 - 400 == 100                                          # 5: geladeira
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
def cabeca(c, t, t0, n, nome=None):
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, XE + 46, 190, 46, a=a), centro(c, str(n), XE + 46, 214, 60, "g", BR, a)))
    E.frase(c, t, t0 + 0.1, [("situação", "i", 76), (str(n), "g", 76, COR)], XE + 120, 220, passo=0.12)


def pausa(c, t, C, cena):
    if t >= C[cena]:
        E.relogio(c, t, C[cena + ".a"], cx=1460, cy=440, r=200)
        return True
    return False


def panela(c, t, x, y, w, h, a=1.0, fogo=True, corr=0.0):
    """panela com água no fogão: (x, y) = canto de baixo à esquerda; corr = corrente de convecção (0 a 1)"""
    if a <= 0:
        return
    M.rrect(c, x + 10, y - h + 30, w - 20, h - 40, 10, AGUA, a * 0.5)
    p = skia.Path()
    p.moveTo(x, y - h); p.lineTo(x, y); p.lineTo(x + w, y); p.lineTo(x + w, y - h)
    c.drawPath(p, M.paint("#9AA3AD", a, stroke=16))
    M.rrect(c, x + w, y - h + 20, 180, 26, 12, TINTA, a)
    M.rrect(c, x - 60, y + 50, w + 120, 26, 8, TINTA, a)
    if fogo:
        for k in range(5):
            fx = x + w * (0.15 + 0.175 * k)
            fh = 60 + 14 * math.sin(t * 7 + k)
            pth = skia.Path()
            pth.moveTo(fx - 22, y + 46); pth.quadTo(fx - 18, y + 46 - fh * 0.6, fx, y + 46 - fh); pth.quadTo(fx + 18, y + 46 - fh * 0.6, fx + 22, y + 46); pth.close()
            c.drawPath(pth, M.paint(E.COR, a))
    if corr > 0:
        cx, cy, rx, ry = x + w / 2, y - h / 2 + 10, w * 0.32, h * 0.3
        for i in range(60):
            g0 = math.pi / 2 + 2 * math.pi * corr * i / 60
            g1 = math.pi / 2 + 2 * math.pi * corr * (i + 1) / 60
            x0, y0 = cx + rx * math.cos(g0), cy + ry * math.sin(g0)
            x1, y1 = cx + rx * math.cos(g1), cy + ry * math.sin(g1)
            M.line(c, x0, y0, x1, y1, E.COR if x0 < cx else FRIO, a, 8, cap_round=True)


def mao(c, x, y, s, a=1.0):
    """mão aberta de lado, palma para a esquerda; (x, y) = meio da palma"""
    if a <= 0:
        return
    pele = "#E9B48C"
    M.rrect(c, x - s * 0.35, y - s * 0.55, s * 0.7, s * 1.1, s * 0.3, pele, a)
    for k in range(4):
        M.rrect(c, x - s * 0.95, y - s * 0.5 + k * s * 0.27, s * 0.75, s * 0.22, s * 0.11, pele, a)
    M.rrect(c, x - s * 0.1, y + s * 0.4, s * 0.5, s * 0.7, s * 0.2, pele, a)


# ---------------- abertura ----------------
def b_gancho(c, t, C, b):
    E.frase(c, t, C["s01.a"], [("cinco", "g", 110, COR), ("situações", "g", 110)], XE, 330, passo=0.15)
    E.frase(c, t, C["s01.a"] + 1.2, ps("criadas para esta aula", "i", 60, TINTA2), XE, 430, passo=0.08)
    for i, s in enumerate(("panela", "ciclo", "gás", "motor", "geladeira")):
        E.foco(c, t, C["s01.b"] + 0.3 * i, 0.4, lambda a, i=i, s=s: E.pilula(c, s, XE + 120 + i * 320, 580, 52, "g", fundo=E.COR if i % 2 == 0 else TINTA, a=a))
    E.frase(c, t, C["s01.c"], ps("pause e resolva", "i", 80) + [("antes", "g", 80, COR)], XE, 800, passo=0.12)


def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s02"], ps("você vai usar", "i", 80), XE, 200, passo=0.12)
    itens = (("s02.a", "condução · convecção · irradiação", None), ("s02.b", "τ = p · ΔV", None), ("s02.c", "Q = τ + ΔU", None),
             ("s02.d", "η = f{τ}{Q_q}", None), ("s02.e", "Carnot: η = 1 − f{T_f}{T_q}", None))
    for i, (k, s, _) in enumerate(itens):
        y = 340 + i * 140
        E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, XE + 40, y - 26, 36, a=a), centro(c, str(i + 1), XE + 40, y - 6, 44, "g", BR, a)))
        fs_em(c, t, C[k] + 0.1, s, XE + 110, y, 66 if i else 60)
    E.frase(c, t, lerp(C["s02.e"], C["s02.end"], 0.4), ps("travou?", "i", 56, COR) + ps("procure a aula no canal", "i", 56), 1250, 960, "left", 0.1)


# ---------------- situação 1: a panela ----------------
def b_questao1(c, t, C, b):
    cabeca(c, t, C["s03.a"], 1)
    E.frase(c, t, C["s03.a"] + 1.0, ps("panela de alumínio no fogo", "i", 62), XE, 340, passo=0.08)
    E.frase(c, t, C["s03.b"], [("a)", "g", 60, COR)] + ps("pelo fundo de metal?", "i", 62), XE, 500, passo=0.1)
    E.frase(c, t, C["s03.c"], [("b)", "g", 60, COR)] + ps("por toda a água?", "i", 62), XE, 620, passo=0.1)
    E.frase(c, t, C["s03.d"], [("c)", "g", 60, COR)] + ps("até a mão ao lado do fogão?", "i", 62), XE, 740, passo=0.1)
    if not pausa(c, t, C, "s04"):
        E.foco(c, t, C["s03.a"] + 0.5, 0.6, lambda a: panela(c, t, 1180, 800, 420, 300, a))
        E.foco(c, t, C["s03.d"], 0.5, lambda a: mao(c, 1800, 620, 90, a))


def b_resposta1(c, t, C, b):
    x, y, w, h = 1150, 820, 420, 300
    E.foco(c, t, C["s05"], 0.6, lambda a: panela(c, t, x, y, w, h, a, corr=ease_io(prog(t, C["s05.c"], 1.5))))
    E.foco(c, t, C["s05.g"], 0.5, lambda a: mao(c, 1800, 620, 90, a))
    for k in range(3):
        seta_calor(c, t, C["s05.a"] + 0.1 * k, (x + 100 + k * 110, y + 40), (x + 100 + k * 110, y - 30), None, d=0.4, amp=6, ondas=1.5)
    for k, dy in enumerate((-40, 20)):
        seta_calor(c, t, C["s05.h"] + 0.1 * k, (x + w + 30, y + dy), (1700, 620 + dy), None, d=0.6, amp=8, ondas=2)
    linhas = (("s05.b", "a)", "condução", "o metal não anda"), ("s05.e", "b)", "convecção", "a água circula"), ("s05.h", "c)", "irradiação", "chega como luz"))
    for i, (k, l, r, ex) in enumerate(linhas):
        y0 = 300 + i * 200
        E.frase(c, t, C[k], [(l, "g", 64, COR), (r, "g", 76)], XE, y0, passo=0.1)
        E.frase(c, t, C[k] + 0.5, ps(ex, "i", 54, TINTA2), XE + 80, y0 + 70, passo=0.06)
        E.foco(c, t, C[k] + 0.4, 0.4, lambda a, y0=y0, r=r: E.selo(c, XE + 120 + E.larg(r, "g", 76) + 70, y0 - 26, 34, True, a))
    E.foco(c, t, C["s05.f"], 0.4, lambda a: E.pilula(c, "só convecção? o calor atravessa o metal primeiro", W / 2, 1010, 44, "g", fundo=ERRADO, a=a))


# ---------------- situação 2: o ciclo ----------------
def grafico2(c, t, t0, area=None):
    P = F.grafico(c, t, t0, 1080, 260, 700, 520, 0, 6, 0, 350, "V (L)", "p (kPa)", 1, 100)
    if area:
        retangulo_area(c, t, area[0], P, 2, 5, area[1], 300, area[2], area[3])
    ciclo(c, t, t0 + 0.4, P, [(2, 300), (5, 300), (5, 100), (2, 100)], d=1.6)
    return P


def b_questao2(c, t, C, b):
    cabeca(c, t, C["s06.a"], 2)
    E.frase(c, t, C["s06.a"] + 1.0, ps("ciclo retangular,", "i", 62) + [("horário", "g", 60, COR)], XE, 340, passo=0.08)
    E.frase(c, t, C["s06.b"], ps("p: de", "i", 62) + [("100", "g", 62), ("a", "i", 62), ("300 kPa", "g", 62, COR)], XE, 480, passo=0.1)
    E.frase(c, t, C["s06.c"], ps("V: de", "i", 62) + [("2", "g", 62), ("a", "i", 62), ("5 L", "g", 62, COR)], XE, 600, passo=0.1)
    E.frase(c, t, C["s06.d"], [("τ", "g", 76, COR)] + ps("em cada volta", "i", 70) + [("=", "g", 76), ("?", "g", 76, COR)], XE, 780, passo=0.1)
    if not pausa(c, t, C, "s07"):
        grafico2(c, t, C["s06.a"] + 0.5)


def b_resposta2(c, t, C, b):
    if t < C["s09"]:
        P = grafico2(c, t, C["s08"], (C["s08.a"], 100, E.COR, 0.4))
        E.frase(c, t, C["s08.a"], [("τ", "g", 76, COR), ("=", "g", 76)] + ps("área de", "i", 76) + [("dentro", "g", 76, COR)], XE, 260, passo=0.12)
        E.foco(c, t, C["s08.b"], 0.4, lambda a: E.formula(c, "altura: 300 − 100 = 200 kPa", XE, 420, 58, "g", TINTA, a))
        E.foco(c, t, C["s08.c"], 0.4, lambda a: E.formula(c, "base: 5 − 2 = 3 L", XE, 520, 58, "g", TINTA, a))
        E.foco(c, t, C["s08.d"], 0.4, lambda a: E.formula(c, "kPa × L = J", XE, 660, 70, "g", COR, a))
        bola_txt(c, t, C["s08.e"], "600 J", 500, 860, 120, 66, CERTO)
        return
    P = grafico2(c, t, C["s09"] - 5, (C["s09"], 0, E.COR, 0.22))
    E.foco(c, t, C["s09.a"], 0.4, lambda a: E.formula(c, "300 × 3 = 900 J?", XE, 300, 80, "g", ERRADO, a))
    if t >= C["s09.a"] + 3.0:
        E.risco(c, XE - 10, 320, XE + 640, 240, t, C["s09.a"] + 3.0, largura=12)
    E.frase(c, t, C["s09.a"] + 1.6, ps("só o trabalho da ida", "i", 58, TINTA2), XE, 400, passo=0.08)
    E.foco(c, t, C["s09.b"], 0.4, lambda a: E.pilula(c, "horário: τ > 0", XE + 210, 560, 54, "g", fundo=CERTO, a=a))
    E.foco(c, t, C["s09.c"] - 1.2, 0.4, lambda a: E.formula(c, "ciclo: ΔU = 0, Q = τ", XE, 720, 66, "g", TINTA, a))
    E.foco(c, t, C["s09.c"], 0.4, lambda a: E.formula(c, "Q = 600 J", XE, 850, 84, "g", COR, a))


# ---------------- situação 3: a isobárica ----------------
def b_questao3(c, t, C, b):
    cabeca(c, t, C["s10.a"], 3)
    E.frase(c, t, C["s10.b"], ps("recebe", "i", 66) + [("1.000 J", "g", 66, COR)] + ps("de calor", "i", 66), XE, 360, passo=0.1)
    E.frase(c, t, C["s10.c"], ps("de", "i", 66) + [("2 L", "g", 66)] + ps("para", "i", 66) + [("6 L", "g", 66)], XE, 480, passo=0.1)
    E.frase(c, t, C["s10.d"], ps("a", "i", 66) + [("100 kPa", "g", 66, COR)] + ps("constante", "i", 66), XE, 600, passo=0.1)
    E.frase(c, t, C["s10.e"], [("ΔU", "g", 80, COR), ("=", "g", 80), ("?", "g", 80, COR)], XE, 780, passo=0.12)
    if not pausa(c, t, C, "s11"):
        fr = lerp(2 / 7, 6 / 7, ease_io(prog(t, C["s10.c"], 1.5)))
        E.foco(c, t, C["s10.a"] + 0.4, 0.6, lambda a: cilindro(c, t, 1320, 280, 360, 600, fr, a))
        seta_calor(c, t, C["s10.b"], (1500, 1060), (1500, 900), None, d=0.5, amp=10, ondas=2)


def b_resposta3(c, t, C, b):
    E.foco(c, t, C["s12.a"], 0.4, lambda a: E.pilula(c, "isobárica: nenhum termo some", XE + 330, 230, 52, "g", fundo=TINTA, a=a))
    passos(c, t, [(C["s12.b"], "τ = 100 × 4 = 400 J", TINTA), (C["s12.c"], "ΔU = Q − τ", TINTA2), (C["s12.d"], "ΔU = 1.000 − 400", TINTA)], XE, 400, 130, 72)
    bola_txt(c, t, C["s12.d"] + 1.2, "600 J", 1450, 520, 140, 74, CERTO)
    E.foco(c, t, C["s12.e"], 0.4, lambda a: E.pilula(c, "saldo positivo: esquentou", 1450, 730, 50, "g", fundo=E.COR, a=a))
    E.foco(c, t, C["s12.f"], 0.4, lambda a: E.formula(c, "1.000 J? esqueceu o trabalho", XE, 900, 62, "g", ERRADO, a))


# ---------------- situação 4: o motor ----------------
def b_questao4(c, t, C, b):
    cabeca(c, t, C["s13.a"], 4)
    E.frase(c, t, C["s13.b"], ps("recebe", "i", 62) + [("1.500 J", "g", 62, COR)] + ps("a", "i", 62) + [("427 °C", "g", 62, COR)], XE, 360, passo=0.1)
    E.frase(c, t, C["s13.c"], ps("joga", "i", 62) + [("675 J", "g", 62, FRIO)] + ps("a", "i", 62) + [("77 °C", "g", 62, FRIO)], XE, 480, passo=0.1)
    E.frase(c, t, C["s13.d"], [("η", "g", 76, COR), ("=", "g", 76), ("?", "g", 76, COR)], XE, 660, passo=0.12)
    E.frase(c, t, C["s13.e"], ps("o motor é", "i", 70) + [("possível?", "g", 68, COR)], XE, 790, passo=0.1)
    if not pausa(c, t, C, "s14"):
        maquina(c, t, dict(q=C["s13.b"], m=C["s13.b"], Qq=C["s13.b"] + 0.3, f=C["s13.c"], Qf=C["s13.c"] + 0.3, tau=C["s13.d"]),
                cx=1460, y0=160, y1=920, w=480, rot=dict(Qq="1.500 J", Qf="675 J", tau="?"), temps=("427 °C", "77 °C"))


def b_resposta4(c, t, C, b):
    if t < C["s16"]:
        fs_em(c, t, C["s15.a"], "η = 1 − f{Q_f}{Q_q}", XE, 330, 100)
        E.foco(c, t, C["s15.b"], 0.4, lambda a: E.formula(c, "f{675}{1.500} = 0,45", XE, 560, 84, "g", TINTA, a))
        E.foco(c, t, C["s15.c"], 0.4, lambda a: E.formula(c, "1 − 0,45", XE, 740, 84, "g", TINTA, a))
        bola_txt(c, t, C["s15.d"], "55 %", 1350, 560, 150, 84)
        return
    E.frase(c, t, C["s16"], ps("e o limite de Carnot?", "i", 70), XE, 220, passo=0.1)
    E.foco(c, t, C["s16.a"], 0.4, lambda a: E.formula(c, "diferença: 427 − 77 = 350", XE, 380, 66, "g", TINTA, a))
    fs_em(c, t, C["s16.b"], "T_q = 427 + 273 = 700 K", XE, 490, 66, cor=COR)
    E.foco(c, t, C["s16.c"], 0.4, lambda a: E.formula(c, "f{350}{700} = 50 %", XE, 650, 80, "g", TINTA, a))
    E.frase(c, t, C["s16.d"], [("55", "g", 84, ERRADO), (">", "g", 84), ("50", "g", 84, COR)], 1350, 420, "center", 0.12)
    E.foco(c, t, C["s16.e"], 0.5, lambda a: (E.pilula(c, "impossível", 1350, 560, 70, "g", fundo=ERRADO, a=a)))
    E.foco(c, t, C["s16.f"], 0.4, lambda a: E.formula(c, "em Celsius: limite ≈ 82 %, e o motor passaria", XE, 880, 56, "g", ERRADO, a))
    if t >= C["s16.f"] + 2.4:
        E.risco(c, XE - 10, 900, XE + 1230, 840, t, C["s16.f"] + 2.4, largura=10)


# ---------------- situação 5: a geladeira ----------------
def b_questao5(c, t, C, b):
    cabeca(c, t, C["s17.a"], 5)
    E.frase(c, t, C["s17.b"], ps("retira", "i", 66) + [("400 J", "g", 66, FRIO)] + ps("do interior", "i", 66), XE, 380, passo=0.1)
    E.frase(c, t, C["s17.c"], ps("a grade solta", "i", 66) + [("500 J", "g", 66, COR)], XE, 500, passo=0.1)
    E.frase(c, t, C["s17.d"], [("τ", "g", 76, COR)] + ps("do compressor", "i", 70) + [("=", "g", 76), ("?", "g", 76, COR)], XE, 680, passo=0.1)
    if not pausa(c, t, C, "s18"):
        maquina(c, t, dict(q=C["s17.b"], m=C["s17.b"], f=C["s17.b"], Qf=C["s17.b"] + 0.3, Qq=C["s17.c"], tau=C["s17.d"]),
                cx=1460, y0=160, y1=920, w=480, inv=True, rot=dict(Qf="400 J", Qq="500 J", tau="?"))


def b_resposta5(c, t, C, b):
    maquina(c, t, dict(q=C["s19"], m=C["s19"], f=C["s19"], Qf=C["s19"] + 0.2, Qq=C["s19"] + 0.4, tau=C["s19.c"]),
            cx=1460, y0=160, y1=920, w=480, inv=True, rot=dict(Qf="400 J", Qq="500 J", tau="100 J"))
    E.frase(c, t, C["s19.a"], ps("o lado quente é a", "i", 70) + [("soma", "g", 70, COR)], XE, 260, passo=0.1)
    E.foco(c, t, C["s19.b"], 0.4, lambda a: E.formula(c, "500 = 400 + τ", XE, 430, 90, "g", TINTA, a))
    bola_txt(c, t, C["s19.c"], "100 J", 520, 640, 120, 66, CERTO)
    E.frase(c, t, C["s19.d"], ps("a cozinha recebe", "i", 62) + [("mais", "g", 62, COR)] + ps("do que sai de dentro", "i", 62), XE, 880, passo=0.08)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def r():
        E.frase(c, t, C["s20"], [("resumindo", "i", 92, COR)], W / 2, 170, "center")
        itens = (("s20.a", "precisa de matéria? a matéria anda?"), ("s20.b", "gráfico p × V: τ = área"), ("s20.c", "sinal: a caixa (entra +, sai −)"),
                 ("s20.d", "toda máquina contra Carnot, em kelvin"))
        for i, (k, s) in enumerate(itens):
            y = 340 + i * 170
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 260, y - 26, 50, a=a), centro(c, str(i + 1), 260, y - 4, 56, "g", BR, a)))
            E.foco(c, t, C[k] + 0.1, 0.5, lambda a, s=s, y=y: E.formula(c, s, 360, y, 62, "g", TINTA, a))
    E.saida(c, t, C["s21"] - 0.1, r)
    if t < C["s21"]:
        return
    E.frase(c, t, C["s21.a"], ps("trilha de calor e termodinâmica:", "i", 70), XE, 300, passo=0.1)
    E.frase(c, t, C["s21.a"] + 1.6, [("completa", "g", 120, COR)], XE, 450)
    E.foco(c, t, C["s21.b"], 0.4, lambda a: E.pilula(c, "continue: Física do Zero", XE + 330, 620, 60, "g", fundo=TINTA, a=a))
    E.foco(c, t, C["s21.a"] + 0.6, 0.8, lambda a: E.simbolo(c, 700, 860, 140 * ease_back(prog(t, C["s21.a"] + 0.6, 0.8)), giro=12 * math.sin(t * 0.4)), blur=0)
    inscreva(c, t, C["s21.c"], C["s21.d"])


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, questao1=b_questao1, resposta1=b_resposta1, questao2=b_questao2, resposta2=b_resposta2,
              questao3=b_questao3, resposta3=b_resposta3, questao4=b_questao4, resposta4=b_resposta4, questao5=b_questao5,
              resposta5=b_resposta5, fim=b_fim)
