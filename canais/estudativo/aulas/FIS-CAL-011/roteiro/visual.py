"""Visual — Estudativo · FIS-CAL-011: trabalho de um gás (trilha Calor e Termodinâmica).

Segue a linguagem visual da Física (cabeçalho do visual.py da FIS-CIN-001) e a da trilha Calor e Termodinâmica (cabeçalho do
visual.py da FIS-CAL-001). Peças novas da termodinâmica, usadas de 011 a 017 (copiadas em cada visual.py):
- GÁS = `cilindro`: cilindro em pé, gás embaixo (fundo rosado com partículas laranja que tremem), êmbolo cinza com haste.
  O êmbolo sobe na expansão e desce na compressão; a pressão do gás = setinhas laranja empurrando o êmbolo por baixo.
- TRABALHO = seta reta e grossa em tinta (`seta_reta`); CALOR = seta ondulada laranja (`seta_calor`), como na trilha.
- GRÁFICO p × V: F.grafico com "V (L)" ou "V (m³)" deitado e "p (kPa)" em pé; a ÁREA do trabalho em laranja translúcido
  (E.area / `retangulo_area`); o CICLO é um caminho fechado em tinta com setas no meio de cada lado (`ciclo`). Área do caminho
  de cima em laranja, do de baixo em azul, e a de dentro (o saldo) em laranja forte.
- Fórmula com índice (Q_q, T_f): `fs`, cópia de E.formula com "_x" para índice (E.formula ainda não tem índice).
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
ARQUIVO_FINAL = "estudativo_FIS-CAL-011_trabalho_de_um_gas.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("formula", "exemplo", "grafico", "ciclo", "atalho", "questao", "fim"))
BR = "#FFFFFF"
FRIO = F.NEG
GELO = "#A9D8F5"
AGUA = "#5BA8E0"

# todas as contas da aula
assert 100_000 * 3 / 1000 == 300 and 5 - 2 == 3 and 100_000 * 3 == 300_000 and 300_000 / 300 == 1000
assert (300 + 100) * (3 - 1) / 2 == 400 and (200 - 100) * (4 - 1) == 300
assert 100 * 3 == 300 and 200 * (1 - 4) == -600 and 1000 * 0.001 == 1
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
def empurra(c, t, x, ye, w, a=1.0, n=4):
    """a pressão do gás: setinhas laranja empurrando o êmbolo por baixo"""
    if a <= 0:
        return
    for k in range(n):
        xx = x + w * (k + 0.5) / n
        dy = 6 * math.sin(t * 6 + k)
        F.seta(c, xx, ye + 90 + dy, xx, ye + 14 + dy, E.COR, a, 7, 24)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    if t < C["s02"]:
        x, y, w, h = 1250, 330, 400, 560
        fr = lerp(0.35, 0.7, ease_io(prog(t, C["s01.b"], 2.0)))
        E.foco(c, t, C["s01.a"], 0.6, lambda a: cilindro(c, t, x, y, w, h, fr, a, agit=0.3 + 0.6 * ep(t, C["s01.b"], 1.0)))
        if t >= C["s01.c"]:
            ye = y + h * (1 - fr)
            seta_reta(c, t, C["s01.c"], (x + w + 80, ye + 60), (x + w + 80, ye - 200), "F", E.COR, lado=1, largura=12, size=64)
        E.frase(c, t, C["s01.a"], ps("no motor, quem empurra", "i", 80), XE, 320, passo=0.12)
        E.frase(c, t, C["s01.a"] + 1.4, ps("o", "i", 80) + [("pistão?", "g", 80, COR)], XE, 430, passo=0.12)
        E.frase(c, t, C["s01.b"], [("um", "i", 110), ("gás", "g", 120, COR)], XE, 620)
        E.frase(c, t, C["s01.c"], ps("e gás que empurra", "i", 70) + [("faz trabalho", "g", 70, COR)], XE, 790, passo=0.1)
        return
    promessa(c, t, C, "s02", (("s02.b", "o trabalho de um gás"), ("s02.c", "o trabalho no gráfico")))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    def trab(a, x, y):
        E.formula(c, "τ = F · d", x - 60, y + 20, 64, "g", TINTA, a, "center")

    def pres(a, x, y):
        E.formula(c, "p = f{F}{A}", x - 40, y + 20, 64, "g", TINTA, a, "center")
    lembrete2(c, t, C, "s03", (("s03.b", "trabalho, em joule:", "força × distância"), ("s03.c", "pressão, em pascal:", "força ÷ área")), (trab, pres))


# ---------------- a fórmula ----------------
CX, CY, CW, CH = 1260, 330, 440, 560


def b_formula(c, t, C, b):
    fr = lerp(0.42, 0.68, ease_io(prog(t, C["s05.a"], 1.2)))
    ye0 = CY + CH * (1 - 0.42)
    ye = CY + CH * (1 - fr)
    if t < C["s06"]:
        E.foco(c, t, C["s04.a"], 0.6, lambda a: cilindro(c, t, CX, CY, CW, CH, fr, a))
        E.saida(c, t, C["s05.a"] - 0.1, lambda: pilula_em(c, t, C["s04.b"] + 0.3, "êmbolo (pistão)", CX + CW / 2, 200, 46, TINTA2))
        E.saida(c, t, C["s05.c"] - 0.1, lambda: E.foco(c, t, C["s04.c"], 0.4, lambda a: empurra(c, t, CX + 8, ye, CW - 16, a)))
        # a fatia de volume que o gás ganhou
        if t >= C["s05.c"]:
            q = ep(t, C["s05.c"], 0.6)
            c.drawRect(skia.Rect.MakeLTRB(CX + 8, ye, CX + CW - 8, ye0), M.paint(E.COR, 0.35 * q))
            E.foco(c, t, C["s05.d"], 0.4, lambda a: E.formula(c, "ΔV", CX + CW / 2, (ye + ye0) / 2 + 22, 60, "g", COR, a, "center"))
        if t >= C["s05.a"]:
            q = ep(t, C["s05.a"], 0.5)
            M.line(c, CX - 40, ye0, CX - 40, ye, TINTA, q, 5)
            for yy in (ye0, ye):
                M.line(c, CX - 58, yy, CX - 22, yy, TINTA, q, 5)
            E.foco(c, t, C["s05.a"] + 0.4, 0.4, lambda a: E.escreve(c, "d", CX - 110, (ye + ye0) / 2 + 22, 64, "g", TINTA, a))
        E.foco(c, t, C["s04.d"] + 0.3, 0.4, lambda a: E.escreve(c, "área A", CX + CW + 30, ye + 10, 46, "i", TINTA2, a))

        def s04():
            E.frase(c, t, C["s04.a"], ps("gás preso num", "i", 76) + [("cilindro", "g", 76, COR)], XE, 260, passo=0.12)
            E.frase(c, t, C["s04.c"], ps("o gás empurra com", "i", 66) + [("pressão p", "g", 66, COR)], XE, 420, passo=0.1)
            formula_em(c, t, C["s04.d"], "p = f{F}{A}   →   F = p · A", XE, 590, 76)
        E.saida(c, t, C["s05"] - 0.1, s04)
        if t >= C["s05"]:
            formula_em(c, t, C["s05"] + 0.3, "τ = F · d", XE, 300, 80, cor=TINTA2)
            formula_em(c, t, C["s05.b"], "τ = p · A · d", XE, 440, 96)
            formula_em(c, t, C["s05.c"], "A · d = ΔV", XE, 600, 96, cor=COR)
            formula_em(c, t, C["s05.e"], "ΔV = final − inicial", XE, 780, 64, cor=TINTA2)
        return
    # s06: a fórmula com a legenda
    E.frase(c, t, C["s06"], ps("fica assim", "i", 76, TINTA2), XE, 200)
    F.formula_legenda(c, t, C["s06.a"], "τ = p · ΔV", [("τ", "trabalho", "J"), ("p", "pressão", "Pa"), ("ΔV", "variação de volume", "m^3")],
                      XE, 380, 150, tl=[C["s06.b"], C["s06.c"], C["s06.d"]], size_l=56)
    pilula_em(c, t, C["s06.e"], "vale com pressão constante: isobárica", XE + 470, 900, 50, E.COR)
    E.foco(c, t, C["s06"], 0.6, lambda a: cilindro(c, t, CX, CY, CW, CH, 0.68, a))
    if t >= C["s06.d"]:
        c.drawRect(skia.Rect.MakeLTRB(CX + 8, CY + CH * 0.32, CX + CW - 8, CY + CH * 0.58), M.paint(E.COR, 0.35 * ep(t, C["s06.d"], 0.5)))
        E.foco(c, t, C["s06.d"], 0.4, lambda a: E.formula(c, "ΔV", CX + CW / 2, CY + CH * 0.45 + 22, 60, "g", COR, a, "center"))


# ---------------- exemplo ----------------
def b_exemplo(c, t, C, b):
    if t < C["s08.c"]:
        def conta():
            passos(c, t, [(C["s07.a"], "p = 100.000 Pa", TINTA), (C["s07.b"], "V: 2 L → 5 L", TINTA), (C["s07.c"], "ΔV = 5 − 2 = 3 L", COR)], XE, 260, 120, 72)
            formula_em(c, t, C["s07.d"], "1 m^3 = 1.000 L", XE, 650, 64, cor=TINTA2)
            formula_em(c, t, C["s07.e"], "3 L = 0,003 m^3", XE, 760, 72, cor=COR)
            formula_em(c, t, C["s08.a"], "τ = 100.000 · 0,003", XE, 900, 72)
        conta()
        x, y, w, h = 1280, 300, 400, 600
        fr = lerp(2 / 6, 5 / 6, ease_io(prog(t, C["s07.b"], 1.6)))
        E.foco(c, t, C["s07"] + 0.3, 0.6, lambda a: cilindro(c, t, x, y, w, h, fr, a))
        E.foco(c, t, C["s07.b"] + 1.6, 0.4, lambda a: (F.medida(c, 5, "L", x + w + 30, y + h * (1 - 5 / 6) + 20, 56, TINTA, a)))
        E.foco(c, t, C["s07.b"], 0.4, lambda a: F.medida(c, 2, "L", x + w + 30, y + h * (1 - 2 / 6) + 20, 56, TINTA2, a))
        bola_txt(c, t, C["s08.b"], "300 J", 1480, 200, 110, 64)
        return
    E.frase(c, t, C["s08.c"] - 1.5, ps("o sinal conta uma história", "i", 76), W / 2, 180, "center", 0.12)
    cols = (("s08.c", "expansão", (0.35, 0.65), "ΔV > 0", "τ > 0: o gás faz", CERTO),
            ("s08.d", "compressão", (0.65, 0.35), "ΔV < 0", "τ < 0: o gás recebe", ERRADO),
            ("s08.e", "volume parado", (0.5, 0.5), "ΔV = 0", "τ = 0", TINTA))
    for i, (k, nome, (f0, f1), dv, tau, cor) in enumerate(cols):
        x = 230 + i * 560
        fr = lerp(f0, f1, ease_io(prog(t, C[k] + 0.4, 1.2)))
        E.foco(c, t, C[k], 0.5, lambda a, x=x, fr=fr: cilindro(c, t, x + 60, 330, 300, 380, fr, a))
        E.frase(c, t, C[k], [(nome, "g", 60, COR if i < 2 else TINTA)], x + 210, 800, "center")
        E.foco(c, t, C[k] + 0.6, 0.4, lambda a, x=x, dv=dv: E.formula(c, dv, x + 210, 890, 60, "g", TINTA, a, "center"))
        E.foco(c, t, C[k] + 1.0, 0.4, lambda a, x=x, tau=tau, cor=cor: E.formula(c, tau, x + 210, 980, 50, "g", cor if cor != TINTA else TINTA2, a, "center"))
        if i == 1 and t >= C[k] + 0.4:
            seta_reta(c, t, C[k] + 0.4, (x + 210, 120 + 160), (x + 210, 120 + 260), None, TINTA, largura=10)


# ---------------- gráfico ----------------
GX, GY, GW, GH = 960, 200, 820, 600


def b_grafico(c, t, C, b):
    if t < C["s10"]:
        P = F.grafico(c, t, C["s09.a"] - 0.3, GX, GY, GW, GH, 0, 6, 0, 150, "V (L)", "p (kPa)", 1, 50)
        f = lambda v: 100
        if t >= C["s09.c"]:
            M.line(c, P.x(2), P.y(100), lerp(P.x(2), P.x(5), ease_io(prog(t, C["s09.c"], 0.8))), P.y(100), E.COR, 1.0, 8, cap_round=True)
        E.area(c, t, C["s09.d"], P, f, 2, 5, alfa=0.3)
        if t >= C["s09.e"]:
            q = ep(t, C["s09.e"], 0.5)
            E.segmento(c, t, C["s09.e"], (P.x(2), P.y(0) + 70), (P.x(5), P.y(0) + 70), None, cor=TINTA, largura=4, pontas=True, d=0.5)
            E.foco(c, t, C["s09.e"] + 0.3, 0.4, lambda a: E.formula(c, "ΔV = 3 L", P.x(3.5), P.y(0) + 130, 48, "g", TINTA, a, "center"))
            E.foco(c, t, C["s09.e"], 0.4, lambda a: E.formula(c, "p", P.x(5) + 30, P.y(50) + 18, 56, "g", COR, a))
        E.foco(c, t, C["s09.f"], 0.5, lambda a: F.medida(c, 300, "J", P.x(3.5), P.y(50) + 20, 64, TINTA, a, "center"))
        E.frase(c, t, C["s09"], [("gráfico", "i", 80), ("p × V", "g", 80, COR)], XE, 260)
        E.frase(c, t, C["s09.c"], ps("pressão constante:", "i", 56) + [("reta deitada", "g", 54)], XE, 420, passo=0.08)
        E.frase(c, t, C["s09.d"], ps("área embaixo:", "i", 56) + [("retângulo", "g", 54, COR)], XE, 540, passo=0.08)
        formula_em(c, t, C["s09.f"], "área = p · ΔV = τ", XE, 720, 72, cor=COR)
        return
    P = F.grafico(c, t, C["s10"] + 0.2, GX, GY, GW, GH, 0, 4, 0, 350, "V (m³)", "p (kPa)", 1, 100)
    f = lambda v: 100 * v
    E.frase(c, t, C["s10.a"], [("τ", "g", 90, COR), ("=", "g", 90), ("área", "g", 90, COR)], XE, 280, passo=0.15)
    E.frase(c, t, C["s10.a"] + 1.2, ps("embaixo da linha", "i", 62), XE, 380, passo=0.1)
    E.curva(c, t, C["s10.b"], P, f, 1, 3, d=0.8, cor=E.COR)
    E.ponto(c, t, C["s10.c"], P, 1, 100, None, guias=True)
    E.ponto(c, t, C["s10.c"] + 0.4, P, 3, 300, None, guias=True)
    E.area(c, t, C["s10.d"], P, f, 1, 3, alfa=0.3)
    E.foco(c, t, C["s10.b"] + 0.5, 0.4, lambda a: E.pilula(c, "trapézio", P.x(2), P.y(330), 44, "b", fundo=E.COR, a=a))
    if t >= C["s11"]:
        formula_em(c, t, C["s11.a"], "A = f{(B + b) · h}{2}", XE, 560, 76)
        formula_em(c, t, C["s11.b"], "B + b = 300 + 100", XE, 720, 60, cor=TINTA2)
        formula_em(c, t, C["s11.c"], "h = ΔV = 3 − 1 = 2", XE, 810, 60, cor=TINTA2)
        formula_em(c, t, C["s11.d"], "f{400 · 2}{2} = 400", XE, 940, 64)
        bola_txt(c, t, C["s11.e"], "400 kJ", P.x(2), P.y(110), 105, 52)


# ---------------- ciclo ----------------
def b_ciclo(c, t, C, b):
    P = F.grafico(c, t, C["s12"] + 0.2, GX, GY, GW, GH, 0, 5, 0, 250, "V (m³)", "p (kPa)", 1, 50)
    fora = 1 - ep(t, C["s13.a"], 0.5)
    if fora > 0:
        if t >= C["s12.d"]:
            c.save()
            retangulo_area(c, t, C["s12.d"], P, 1, 4, 0, 200, E.COR, 0.22 * fora)
            c.restore()
        if t >= C["s12.f"]:
            retangulo_area(c, t, C["s12.f"], P, 1, 4, 0, 100, FRIO, 0.3 * fora)
    retangulo_area(c, t, C["s13.a"], P, 1, 4, 100, 200, E.COR, 0.45)
    ciclo(c, t, C["s12.b"], P, [(1, 200), (4, 200), (4, 100), (1, 100)], d=1.8, largura=8)
    if t >= C["s12.c"]:
        M.line(c, P.x(1), P.y(200), P.x(4), P.y(200), E.COR, ep(t, C["s12.c"], 0.4) * (1 - ep(t, C["s12.e"], 0.4)), 12, cap_round=True)
    if t >= C["s12.e"]:
        M.line(c, P.x(1), P.y(100), P.x(4), P.y(100), FRIO, ep(t, C["s12.e"], 0.4) * (1 - ep(t, C["s13.a"], 0.4)), 12, cap_round=True)
    E.foco(c, t, C["s12.c"] + 0.4, 0.4, lambda a: E.escreve(c, "ida", P.x(2.3), P.y(200) - 24, 46, "g", COR, a * fora))
    E.foco(c, t, C["s12.e"] + 0.4, 0.4, lambda a: E.escreve(c, "volta", P.x(2.2), P.y(100) + 60, 46, "g", FRIO, a * fora))
    if t < C["s13"]:
        E.frase(c, t, C["s12.a"], ps("vai e volta:", "i", 76) + [("ciclo", "g", 80, COR)], XE, 260, passo=0.12)
        E.frase(c, t, C["s12.c"], [("ida,", "g", 64, COR)] + ps("por cima:", "i", 66), XE, 440, passo=0.1)
        E.frase(c, t, C["s12.d"], ps("o gás", "i", 66) + [("faz", "g", 64, COR)] + ps("a área de cima", "i", 66), XE, 530, passo=0.1)
        E.frase(c, t, C["s12.e"], [("volta,", "g", 64, FRIO)] + ps("por baixo:", "i", 66), XE, 700, passo=0.1)
        E.frase(c, t, C["s12.f"], ps("o gás", "i", 66) + [("recebe", "g", 64, FRIO)] + ps("a de baixo", "i", 66), XE, 790, passo=0.1)
        return
    E.frase(c, t, C["s13.a"], [("τ", "g", 80, COR), ("=", "g", 80)] + ps("área de", "i", 84) + [("dentro", "g", 80, COR)], XE, 260, passo=0.12)
    E.foco(c, t, C["s13.b"], 0.4, lambda a: E.formula(c, "altura: 200 − 100 = 100", XE, 420, 54, "g", TINTA2, a))
    E.foco(c, t, C["s13.c"], 0.4, lambda a: E.formula(c, "base: 4 − 1 = 3", XE, 510, 54, "g", TINTA2, a))
    E.foco(c, t, C["s13.d"], 0.4, lambda a: E.formula(c, "100 · 3 = 300 kJ", XE, 620, 72, "g", TINTA, a))
    E.foco(c, t, C["s13.e"], 0.4, lambda a: (E.pilula(c, "horário: τ > 0, motor", XE + 300, 780, 48, "g", fundo=CERTO, a=a)))
    E.foco(c, t, C["s13.f"], 0.4, lambda a: (E.pilula(c, "anti-horário: τ < 0", XE + 260, 900, 48, "g", fundo=ERRADO, a=a)))
    bola_txt(c, t, C["s13.d"] + 0.4, "300 kJ", P.x(2.5), P.y(150), 92, 50)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s14"], [("cuidado", "g", 96, ERRADO)], XE, 200)
    E.frase(c, t, C["s14.a"], [("pascal", "g", 76), ("×", "g", 76, TINTA2), ("litro", "g", 76)], XE + 480, 200, passo=0.12)
    formula_em(c, t, C["s14.b"], "100.000 Pa × 3 L", W / 2, 420, 100, align="center")
    E.foco(c, t, C["s14.c"], 0.5, lambda a: E.escreve(c, "= 300.000 J?", W / 2 - 330, 580, 110, "g", ERRADO, a))
    if t >= C["s14.c"] + 0.8:
        E.risco(c, W / 2 - 340, 600, W / 2 + 340, 490, t, C["s14.c"] + 0.8, largura=12)
    E.frase(c, t, C["s14.d"], [("1.000", "g", 76, ERRADO), ("vezes", "i", 80), ("mais", "i", 80), ("que", "i", 80), ("300 J", "g", 76, CERTO)], W / 2, 780, "center", 0.12)
    formula_em(c, t, C["s14.e"], "1 L = 0,001 m^3", W / 2, 930, 72, cor=TINTA2, align="center")


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    E.frase(c, t, C["s15"], ps("o atalho de prova", "i", 70, CLARO), W / 2, 160, "center")
    if t < C["s16"]:
        E.foco(c, t, C["s15.a"], 0.5, lambda a: E.formula(c, "kPa × L = J", W / 2, 400, 170, "g", BR, a, "center"))
        E.foco(c, t, C["s15.b"], 0.4, lambda a: E.formula(c, "100.000 Pa = 100 kPa", W / 2, 600, 72, "g", CLARO, a, "center"))
        E.foco(c, t, C["s15.c"], 0.4, lambda a: E.formula(c, "100 kPa × 3 L = 300 J", W / 2, 760, 90, "g", BR, a, "center"))
        E.foco(c, t, C["s15.c"] + 1.4, 0.4, lambda a: E.pilula(c, "sem converter nada", W / 2, 900, 52, "g", fundo=E.COR, a=a))
        return
    E.foco(c, t, C["s16"], 0.4, lambda a: E.formula(c, "kPa × L = J", W / 2, 330, 120, "g", BR, a, "center"))
    E.foco(c, t, C["s16.a"], 0.4, lambda a: (E.formula(c, "quilo: × 1.000", 560, 520, 72, "g", CLARO, a, "center")))
    E.foco(c, t, C["s16.b"], 0.4, lambda a: (E.formula(c, "litro: ÷ 1.000", 1360, 520, 72, "g", CLARO, a, "center")))
    E.foco(c, t, C["s16.c"], 0.4, lambda a: E.pilula(c, "um cancela o outro", W / 2, 650, 56, "g", fundo=E.COR, a=a))
    E.frase(c, t, C["s16.d"], [("não", "g", 60, ERRADO), ("compensa:", "i", 64, CLARO), ("atm", "g", 60, BR), ("ou", "i", 64, CLARO), ("cm³", "g", 60, BR)], W / 2, 830, "center", 0.12)
    E.frase(c, t, C["s16.d"] + 2.4, ps("converta para pascal e metro cúbico", "i", 56, CLARO), W / 2, 940, "center", 0.08)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s17"], ps("hora de testar", "i", 72, COR), XE, 200)
    E.frase(c, t, C["s17.a"], ps("pressão constante:", "i", 70), XE, 340, passo=0.1)
    E.foco(c, t, C["s17.a"] + 0.4, 0.4, lambda a: F.medida(c, 200, "kPa", XE + 560, 340, 84, COR, a))
    E.frase(c, t, C["s17.b"], ps("de", "i", 70) + [("4 L", "g", 70)] + ps("para", "i", 70) + [("1 L", "g", 70)], XE, 470, passo=0.12)
    E.frase(c, t, C["s17.c"], [("τ", "g", 76, COR), ("=", "g", 76), ("?", "g", 76, COR)], XE, 640, passo=0.12)
    E.frase(c, t, C["s17.d"], [("fez", "g", 66), ("ou", "i", 70), ("recebeu?", "g", 66, COR)], XE, 780, passo=0.12)
    if t < C["s18"]:
        fr = lerp(0.8, 0.2, ease_io(prog(t, C["s17.b"] + 0.3, 1.6)))
        E.foco(c, t, C["s17.a"], 0.6, lambda a: cilindro(c, t, 1300, 330, 380, 560, fr, a))
    else:
        E.relogio(c, t, C["s18.a"], cx=1460, cy=440, r=200)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    passos(c, t, [(C["s19.a"], "ΔV = final − inicial", TINTA2), (C["s19.b"], "ΔV = 1 − 4 = −3 L", TINTA),
                  (C["s19.c"], "τ = 200 kPa · (−3 L)", TINTA)], XE, 250, 140, 72)
    bola_txt(c, t, C["s19.d"], "−600 J", 560, 760, 130, 68)
    x, y, w, h = 1300, 330, 380, 560
    fr = lerp(0.8, 0.2, ease_io(prog(t, C["s19.b"], 1.6)))
    E.foco(c, t, C["s19"], 0.6, lambda a: cilindro(c, t, x, y, w, h, fr, a))
    if t >= C["s20"]:
        ye = y + h * (1 - fr)
        seta_reta(c, t, C["s20.a"], (x - 120, ye - 260), (x - 120, ye - 40), None, TINTA, largura=12)
        E.foco(c, t, C["s20.a"] + 0.3, 0.4, lambda a: E.pilula(c, "compressão", x + w / 2, 230, 50, "g", fundo=TINTA, a=a))
        E.frase(c, t, C["s20.b"], ps("o gás", "i", 66) + [("recebeu", "g", 64, COR), ("600 J", "g", 64)], 560, 990, "center", 0.12)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def r():
        resumo(c, t, C, (("s21.a", [("τ = p · ΔV", "g", 70, COR)]),
                         ("s21.b", [("gráfico", "i", 66), ("p × V:", "g", 66), ("τ", "g", 66, COR), ("=", "g", 66), ("área", "g", 66, COR)]),
                         ("s21.c", [("ciclo:", "g", 66), ("a", "i", 66), ("área", "i", 66), ("de", "i", 66), ("dentro", "g", 66, COR)])), y0=380, dy=190)
    E.saida(c, t, C["s22"] - 0.1, r)
    if t < C["s22"]:
        return
    E.frase(c, t, C["s22"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C["s22.a"], ps("para onde vai o", "i", 90) + [("calor?", "g", 96, COR)], XE, 400, passo=0.12)
    gx, gy = 330, 620
    E.foco(c, t, C["s22.a"] + 0.6, 0.5, lambda a: caixa_gas(c, gx, gy, 300, 220, a, t, 0.5))
    seta_calor(c, t, C["s22.a"] + 1.0, (gx - 220, gy + 110), (gx - 20, gy + 110), "Q", d=0.6, amp=10, ondas=2)
    seta_reta(c, t, C["s22.b"], (gx + 320, gy + 110), (gx + 560, gy + 110), "τ", TINTA)
    E.foco(c, t, C["s22.b"] + 1.0, 0.4, lambda a: E.formula(c, "+ ΔU", gx + 150, gy - 40, 60, "g", COR, a, "center"))
    inscreva(c, t, C["s22.c"], C["s22.d"])


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, formula=b_formula, exemplo=b_exemplo, grafico=b_grafico, ciclo=b_ciclo,
              erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
