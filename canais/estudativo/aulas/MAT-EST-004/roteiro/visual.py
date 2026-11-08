"""Visual — Estudativo · MAT-EST-004: gráfico de setores (porcentagem ↔ ângulo).
Mesma linguagem da Estatística definida em MAT-EST-001 (docstring de lá): cada categoria com a sua cor de E._paleta (aqui o
transporte de MAT-EST-002: ônibus, carro, bicicleta, a pé, nas mesmas cores de lá e de MAT-EST-003); tabela (quadro()) que
entra célula a célula no marcador em que a fala diz o número; conta da vez à direita; resposta na esfera; atalho no palco.
Novo nesta aula (para copiar nas próximas):
- PIZZA = E.pizza(cores=CATS, rotulos=False) girando do alto no sentido do relógio; o nome e a % de cada setor entram por fora
  no marcador da fala (rot_fora()), porque o rótulo do E.pizza entra junto com o giro.
- ÂNGULO DO SETOR = arco perto do centro e o valor em graus dentro do setor (ang_centro()); 90° vira o quadradinho do ângulo
  reto. Setor da vez com contorno grosso em tinta (contorno()).
- FATIA SOLTA = fatia(): um setor de qualquer ângulo sobre o disco cinza (disco()), para o erro (fatia fininha em vermelho) e
  para o caminho de volta (72° dentro da volta, a volta riscada em 5 fatias iguais).
- RODA DE 10% (roda10()): no palco escuro, o círculo cortado em 10 fatias de 36°, que acendem conforme a conta.
Sem voz ainda: todo instante vem de C[...] (marcadores do roteiro), para acompanhar a voz real quando ela chegar."""
import math
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Estatística")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-EST-004_grafico_de_setores.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("setores", "volta", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
PAPEL = E.PAPEL
VAZIO = E.mix(FIO, PAPEL, 0.35)      # disco sem dado
CATS = E._paleta(4)                  # ônibus, carro, bicicleta, a pé (as cores de MAT-EST-002 e 003)
PIZ = [("ônibus", 40), ("carro", 25), ("bicicleta", 20), ("a pé", 15)]
ANG = [v * 360 // 100 for _, v in PIZ]
INI = [-90 + sum(ANG[:i]) for i in range(4)]       # início de cada setor (graus do skia: do alto, no sentido do relógio)
FRUTA = [("banana", 30), ("maçã", 15), ("", 55)]
assert ANG == [144, 90, 72, 54] and sum(ANG) == 360 and 40 * 360 == 14400 and 14400 // 100 == 144
assert 8 * 360 / 100 == 28.8 and 8 / 20 == 0.4 and 360 // 10 == 36 and 2 * 36 == 72 and 4 * 36 == 144 and 36 + 18 == 54
assert 72 * 5 == 360 and 20 * 20 // 100 == 4 and 3 * 36 == 108 and 54 / 360 == 0.15 and 200 // 10 == 20 and 20 + 10 == 30


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças comuns ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    """uma frase, palavra a palavra (palavra com %, °, ² ou → vai na grotesca)"""
    return [(w, "g" if any(ch in w for ch in "%°²³→") else est, size * (0.92 if any(ch in w for ch in "%°²³→") and est != "g" else 1), cor) for w in txt.split()]


def fcen(c, t, t0, s, cx, y, size, cor=None):
    E.formula_em(c, t, t0, s, cx, y, size, "g", cor, "center")


def bola_txt(c, t, t0, s, cx, cy, r, size, cor=None):
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r * ease_back(prog(t, t0, 0.5)), cor, a),
                                     E.formula(c, s, cx, cy + size * 0.36, size, "g", E.SOBRE, a, "center")))


def fase(c, t, t0, t1, fn):
    if t0 - 0.01 <= t < t1 + 0.4:
        E.saida(c, t, t1, fn)


def quadro(c, t, x, y, colunas, linhas, total=None, size=58, h_lin=None, cores=None, t_fio=None):
    """tabela de dados (MAT-EST-001). colunas = [(título, largura, t0)]; linhas = [[(texto, t0[, cor]), ...], ...];
    total = [(texto, t0[, cor]), ...] depois de um fio grosso; cores = cor de cada linha (bolinha antes da 1ª coluna)"""
    h_lin = h_lin or size * 1.55
    xs = [x]
    for _, w, _ in colunas:
        xs.append(xs[-1] + w)
    larg = xs[-1] - x
    t_cab = min(ti for _, _, ti in colunas)
    p = ease_io(prog(t, t_fio if t_fio is not None else t_cab, 0.6))
    if p > 0:
        M.line(c, x, y + 20, x + larg * p, y + 20, TINTA, 1, 3)
    for k, (tit, w, ti) in enumerate(colunas):
        cx = xs[k] + w / 2
        E.foco(c, t, ti, 0.45, lambda a, tit=tit, cx=cx: centro(c, tit, cx, y - 6, size * 0.78, "i", TINTA2, a))
    bases = []
    for j, lin in enumerate(linhas):
        yy = y + 20 + h_lin * (j + 1) - h_lin * 0.3
        bases.append(yy)
        for k, cel in enumerate(lin):
            s, ti, *cc = cel
            if s == "":
                continue
            cx = xs[k] + colunas[k][1] / 2
            if k == 0 and cores:
                E.foco(c, t, ti, 0.4, lambda a, yy=yy, j=j: c.drawCircle(xs[0] + 22, yy - size * 0.34, size * 0.24, M.paint(cores[j], a)))
                cx += 22
            E.foco(c, t, ti, 0.4, lambda a, s=s, cx=cx, yy=yy, cc=cc, k=k: centro(c, s, cx, yy, size, "b" if k == 0 else "g", cc[0] if cc else TINTA, a))
    if total:
        yf = y + 20 + h_lin * len(linhas) + 8
        tt = min(cel[1] for cel in total if cel[0] != "")
        q = ease_io(prog(t, tt, 0.5))
        if q > 0:
            M.line(c, x, yf, x + larg * q, yf, TINTA, 1, 6)
        yy = yf + h_lin * 0.72
        bases.append(yy)
        for k, cel in enumerate(total):
            s, ti, *cc = cel
            if s == "":
                continue
            cx = xs[k] + colunas[k][1] / 2 + (22 if k == 0 and cores else 0)
            E.foco(c, t, ti, 0.4, lambda a, s=s, cx=cx, cc=cc, k=k: centro(c, s, cx, yy, size, "i" if k == 0 else "g", cc[0] if cc else TINTA, a))
    return bases


# ================= peças do gráfico de setores (copiar nas próximas aulas) =================
def _u(g):
    return math.cos(math.radians(g)), math.sin(math.radians(g))


def disco(c, cx, cy, r, a=1.0, cor=None, borda=TINTA):
    """o círculo inteiro, vazio (ou numa cor só)"""
    if a <= 0:
        return
    c.drawCircle(cx, cy, r, M.paint(cor or VAZIO, a))
    c.drawCircle(cx, cy, r, M.paint(borda, a, stroke=3))


def fatia(c, cx, cy, r, ini, varre, cor, a=1.0, borda=None, lw=6):
    """um setor solto: ini e varre em graus do skia (−90 = alto, sentido do relógio)"""
    if a <= 0 or varre <= 0:
        return
    p = skia.Path()
    p.moveTo(cx, cy)
    p.arcTo(skia.Rect.MakeXYWH(cx - r, cy - r, 2 * r, 2 * r), ini, varre, False)
    p.close()
    c.drawPath(p, M.paint(cor, a))
    sep = M.paint(borda or PAPEL, a, stroke=lw if borda else 5)
    sep.setStrokeJoin(skia.Paint.kRound_Join)
    c.drawPath(p, sep)


def contorno(c, t, t0, cx, cy, r, ini, varre, cor=TINTA, lw=9):
    """o setor da vez: contorno grosso que se fecha"""
    p = ease_io(prog(t, t0, 0.5))
    if p <= 0:
        return
    path = skia.Path()
    path.moveTo(cx, cy)
    path.arcTo(skia.Rect.MakeXYWH(cx - r, cy - r, 2 * r, 2 * r), ini, varre, False)
    path.close()
    pt = M.paint(cor, p, stroke=lw)
    pt.setStrokeJoin(skia.Paint.kRound_Join)
    c.drawPath(path, pt)


def ang_centro(c, t, t0, cx, cy, ini, varre, rotulo, cor=TINTA, r=70, dist=None, size=50):
    """o ângulo no centro do setor: arco perto do centro (90° = quadradinho) e o valor em graus na bissetriz"""
    p = ease_io(prog(t, t0, 0.5))
    if p <= 0:
        return
    if abs(varre - 90) < 0.01:
        u1, u2 = _u(ini), _u(ini + 90)
        s = r * 0.62
        pa = skia.Path()
        pa.moveTo(cx + u1[0] * s, cy + u1[1] * s)
        pa.lineTo(cx + (u1[0] + u2[0]) * s, cy + (u1[1] + u2[1]) * s)
        pa.lineTo(cx + u2[0] * s, cy + u2[1] * s)
        c.drawPath(pa, M.paint(cor, p, stroke=6))
    else:
        E.arco(c, cx, cy, r, ini, varre * p, cor, 6)
    ux, uy = _u(ini + varre / 2)
    d = dist or r + 30 + size * 0.9
    E.foco(c, t, t0 + 0.25, 0.4, lambda a: centro(c, rotulo, cx + ux * d, cy + uy * d + size * 0.36, size, "g", cor, a))


def rot_fora(c, t, t0, cx, cy, r, ini, varre, nome, valor, cor, size=44):
    """nome e valor do setor por fora, na bissetriz (mesma conta de lugar do E.pizza)"""
    ux, uy = _u(ini + varre / 2)
    px, py = cx + ux * (r + 28), cy + uy * (r + 28)
    w1 = max(E.larg(nome, "b", size), E.larg(valor, "g", size * 1.2))
    k = min(abs(ux) * w1 / 2, w1 / 2) + abs(uy) * size * 0.95
    lx, ly = px + ux * k, py + uy * k
    tv = cor if M.lum(cor) < 0.4 else E.mix(cor, "#000000", 0.4)
    E.foco(c, t, t0, 0.45, lambda a: (centro(c, nome, lx, ly - size * 0.62 + size * 0.36, size, "b", TINTA, a),
                                      centro(c, valor, lx, ly + size * 0.62 + size * 0.42, size * 1.2, "g", tv, a)), sobe=6)


def sobre(cor):
    return BR if M.lum(cor) < 0.5 else TINTA


def roda10(c, t, t0, cx, cy, r, n, a=1.0, cor=None):
    """o círculo cortado em 10 fatias de 36° (palco escuro); n = quantas fatias acesas (pode ser 1,5)"""
    if a <= 0:
        return
    cor = cor or E.mix(E.COR, BR, 0.2)
    c.drawCircle(cx, cy, r, M.paint("#1B1B2B", a))
    cheias = int(n + 1e-9)
    for i in range(cheias):
        fatia(c, cx, cy, r, -90 + 36 * i, 36, cor, a)
    if n - cheias > 0.01:
        fatia(c, cx, cy, r, -90 + 36 * cheias, 36 * (n - cheias), E.mix(cor, BR, 0.35), a)
    for i in range(10):
        q = ep(t, t0 + 0.05 * i, 0.4) * a
        ux, uy = _u(-90 + 36 * i)
        M.line(c, cx, cy, cx + ux * r, cy + uy * r, CLARO, q, 3)
    c.drawCircle(cx, cy, r, M.paint(BR, a, stroke=4))


# ---------------- a pizza do transporte ----------------
PX, PY, PR = 560, 570, 270


def pizza_tr(c, t, t0, d=1.2, cx=PX, cy=PY, r=PR):
    E.pizza(c, t, t0, PIZ, cx, cy, r, cores=CATS, rotulos=False, d=d)


def rotulos_tr(c, t, ts, cx=PX, cy=PY, r=PR):
    for i, ((nome, v), ti) in enumerate(zip(PIZ, ts)):
        rot_fora(c, t, ti, cx, cy, r, INI[i], ANG[i], nome, f"{v}%", CATS[i])


def angulos_tr(c, t, ts, cx=PX, cy=PY, r=PR):
    """o ângulo de cada setor dentro dele (ts[i] = None: ainda não)"""
    for i, ti in enumerate(ts):
        if ti is not None:
            ang_centro(c, t, ti, cx, cy, INI[i], ANG[i], f"{ANG[i]}°", sobre(CATS[i]), 62, r * 0.62)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    a1, b1, c1, d1 = (C[f"s01.{k}"] for k in "abcd")
    cx, cy, r = 600, 590, 300

    def um():
        E.foco(c, t, a1, 0.5, lambda a: disco(c, cx, cy, r, a))
        q = ease_io(prog(t, b1, 0.8))
        fatia(c, cx, cy, r, -90, 90 * q, E.COR)
        E.foco(c, t, b1 + 0.6, 0.4, lambda a: centro(c, "25%", cx + 120, cy - 100, 64, "g", BR, a))
        E.saida(c, t, d1, lambda: (fatia(c, cx, cy, r, 165, 25 * ease_io(prog(t, c1, 0.6)), E.mix(ERRADO, PAPEL, 0.35), 1, ERRADO, 5),
                                   E.foco(c, t, c1 + 0.4, 0.4, lambda a: E.pilula(c, "25°?", cx - r - 40, cy - 150, 48, "g", fundo=ERRADO, a=a))))
        ang_centro(c, t, d1, cx, cy, -90, 90, "", BR, 90)
        E.foco(c, t, d1 + 0.3, 0.5, lambda a: E.pilula(c, "90°", cx + 170, cy - r - 60, 60, "g", fundo=TINTA, a=a))
        X = 1440
        E.frase(c, t, a1, ps("num gráfico de", "i", 60) + [("pizza", "g", 66, COR)], X, 240, "center", 0.1)
        E.frase(c, t, b1, ps("uma fatia vale", "i", 64) + [("25%", "g", 72, COR)], X, 360, "center", 0.1)
        E.frase(c, t, b1 + 1.4, [("quantos graus?", "g", 72)], X, 470, "center", 0.1)
        E.frase(c, t, c1, [("25°?", "g", 70, ERRADO)] + ps("fininha demais", "i", 56, ERRADO), X, 620, "center", 0.1)
        bola_txt(c, t, d1, "90°", X - 120, 830, 120, 84)
        E.frase(c, t, d1 + 0.8, ps("o canto", "i", 56), X + 140, 815, "left", 0.1)
        E.frase(c, t, d1 + 1.3, ps("da folha", "i", 56), X + 140, 885, "left", 0.1)
    E.saida(c, t, C["s02"] - 0.1, um)

    if t >= C["s02"]:
        ta, tb = C["s02.a"], C["s02.b"]
        E.foco(c, t, tb - 0.2, 0.7, lambda a: E.bola(c, 1560, 600, 240 * ease_back(prog(t, tb - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, ps("até o fim desta aula", "i", 88), XE, 280, passo=0.14)
        E.frase(c, t, ta + 1.4, [("porcentagem", "g", 96, COR)] + ps("→ ângulo", "i", 88), XE, 430, passo=0.14)
        E.frase(c, t, ta + 3.6, [("ângulo", "g", 96, COR)] + ps("→ porcentagem", "i", 88), XE, 580, passo=0.14)
        E.foco(c, t, tb + 0.1, 0.5, lambda a: (centro(c, "+ atalho", 1560, 575, 80, "g", E.SOBRE, a),
                                               centro(c, "de prova", 1560, 660, 80, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"] + 0.3, ps("você só precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "3", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w, hh = 980, 820, 200
    itens = (("s03.b", "uma volta inteira:", "360°"), ("s03.c", "frequência relativa:", "% do total"), ("s03.d", "a regra de três", None))
    for i, (k, l1, l2) in enumerate(itens):
        y = 180 + i * 240
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, hh, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, ps(l1, "i", 56), x + 44, y + 84, "left", 0.1)
        if l2:
            E.formula_em(c, t, C[k] + 0.6, l2, x + w - 60, y + 160, 60, "g", COR, "right")
    alvo = [180 + i * 240 + 170 for i in range(3)]
    q1 = ease_io(prog(t, C["s03.c"] - 0.35, 0.5))
    q2 = ease_io(prog(t, C["s03.d"] - 0.35, 0.5))
    E.cursor(c, x + w - 30, lerp(lerp(alvo[0], alvo[1], q1), alvo[2], q2), ep(t, C["s03.b"], 0.4))
    E.frase(c, t, lerp(C["s03.d"], C["s03.end"], 0.6), ps("faltou?", "i", 54, COR) + ps("procure no canal", "i", 54), x, 950, "left", 0.1)


# ---------------- o gráfico de setores ----------------
def b_setores(c, t, C, b):
    a4, b4, c4, d4 = (C[f"s04.{k}"] for k in "abcd")
    a5, b5, c5, d5, e5 = (C[f"s05.{k}"] for k in "abcde")
    E.saida(c, t, c4 + 1.0, lambda: (E.foco(c, t, b4, 0.5, lambda a: disco(c, PX, PY, PR, a, E.mix(E.COR, PAPEL, 0.75))),
                                     E.foco(c, t, b4 + 0.4, 0.4, lambda a: (centro(c, "100%", PX, PY + 10, 110, "g", COR, a),
                                                                            centro(c, "o total", PX, PY + 90, 52, "i", TINTA2, a)))))
    pizza_tr(c, t, c4)
    E.saida(c, t, d4 + 1.6, lambda: (contorno(c, t, c4 + 1.3, PX, PY, PR, INI[1], ANG[1]),
                                     E.foco(c, t, c4 + 1.5, 0.4, lambda a: E.pilula(c, "setor", PX + 40, PY + PR + 70, 46, "g", fundo=TINTA, a=a))))
    E.saida(c, t, C["s05"], lambda: (contorno(c, t, d4, PX, PY, PR, INI[0], ANG[0], TINTA, 11),
                                     contorno(c, t, d4 + 0.6, PX, PY, PR, INI[3], ANG[3], TINTA2, 7)))
    X = 1480

    def um():
        E.frase(c, t, a4, ps("nome oficial:", "i", 58), X, 260, "center", 0.1)
        E.frase(c, t, a4 + 0.6, [("gráfico de setores", "g", 76, COR)], X, 360, "center", 0.1)
        E.frase(c, t, b4, ps("círculo inteiro =", "i", 56) + [("100%", "g", 60, COR)], X, 520, "center", 0.1)
        E.frase(c, t, c4, ps("cada fatia = um", "i", 56) + [("setor", "g", 60, COR)], X, 640, "center", 0.1)
        E.frase(c, t, d4, ps("maior a parte,", "i", 56) + [("maior a fatia", "g", 60, COR)], X, 760, "center", 0.1)
    fase(c, t, C["s04"], C["s05"] - 0.1, um)
    if t < C["s05"] - 0.1:
        return
    ts = (b5, c5, d5, e5)
    rotulos_tr(c, t, ts)
    E.frase(c, t, a5, ps("as", "i", 56) + [("20 pessoas:", "g", 60, COR)] + ps("como vão ao trabalho", "i", 52), 1480, 250, "center", 0.1)
    linhas = [[(n, ti), (f"{v}%", ti + 0.3, COR)] for (n, v), ti in zip(PIZ, ts)]
    quadro(c, t, 1180, 400, [("transporte", 340, a5 + 0.6), ("%", 220, a5 + 0.8)], linhas, size=56, cores=CATS)


# ---------------- porcentagem para ângulo ----------------
def b_angulo(c, t, C, b):
    a6, b6, c6 = C["s06.a"], C["s06.b"], C["s06.c"]
    a7, b7, c7 = C["s07.a"], C["s07.b"], C["s07.c"]
    pizza_tr(c, t, -9)
    rotulos_tr(c, t, (-9,) * 4)
    X = 1480

    def um():
        ang_centro(c, t, a6, PX, PY, INI[0], ANG[0], "?", BR, 62, PR * 0.62, 64)
        E.frase(c, t, a6, ps("o", "i", 60) + [("ângulo", "g", 66, COR)] + ps("no centro", "i", 60), X, 260, "center", 0.1)
        E.foco(c, t, b6, 0.5, lambda a: disco(c, X - 330, 500, 70, a, E.mix(E.COR, PAPEL, 0.6)))
        if t >= b6:
            E.arco(c, X - 330, 500, 92, -90, 359.9 * ease_io(prog(t, b6 + 0.3, 1.0)), E.COR, 8)
        fcen(c, t, b6 + 0.4, "100% → 360°", X + 80, 530, 84, COR)
        E.frase(c, t, b6 + 1.4, ps("a volta inteira", "i", 50, TINTA2), X + 80, 620, "center", 0.1)
        E.frase(c, t, c6, ps("ângulo da fatia =", "i", 56), X, 780, "center", 0.1)
        E.foco(c, t, c6 + 0.8, 0.5, lambda q: E.pilula(c, "a mesma % de 360°", X, 880, 56, "g", a=q, cor=E.SOBRE))
    fase(c, t, C["s06"], C["s07"] - 0.1, um)
    if t < C["s07"] - 0.1:
        return
    contorno(c, t, a7, PX, PY, PR, INI[1], ANG[1])
    ang_centro(c, t, b7 + 0.6, PX, PY, INI[1], ANG[1], "90°", sobre(CATS[1]), 62, PR * 0.62, 56)
    E.frase(c, t, a7, ps("carro:", "i", 60) + [("25%", "g", 66, COR)], X, 270, "center", 0.1)
    fcen(c, t, a7 + 1.4, "25% = f{1}{4}", X, 420, 76)
    E.frase(c, t, a7 + 2.2, ps("da pizza", "i", 50, TINTA2), X + 240, 420, "left", 0.1)
    fcen(c, t, b7, "360 ÷ 4 = 90°", X, 620, 84, COR)
    E.foco(c, t, c7, 0.5, lambda q: E.pilula(c, "um quarto de volta: o canto da folha", X, 800, 46, "g", a=q, cor=E.SOBRE))


# ---------------- regra de três ----------------
XP3, XD3, YT3, DY3 = 1250, 1640, 250, 140


def b_regra3(c, t, C, b):
    a8, b8, c8, d8, e8 = (C[f"s08.{k}"] for k in "abcde")
    a9, b9, c9 = C["s09.a"], C["s09.b"], C["s09.c"]
    pizza_tr(c, t, -9)
    rotulos_tr(c, t, (-9,) * 4)
    angulos_tr(c, t, (e8, -9, a9, b9))
    E.saida(c, t, C["s09"], lambda: contorno(c, t, C["s08"] + 0.1, PX, PY, PR, INI[0], ANG[0]))

    def um():
        E.foco(c, t, C["s08"] + 0.1, 0.5, lambda a: centro(c, "ônibus: 40% = quantos graus?", W / 2 + 470, 140, 46, "i", TINTA2, a))
        for x, nome in ((XP3, "%"), (XD3, "graus")):
            E.foco(c, t, a8, 0.5, lambda a, x=x, nome=nome: (centro(c, nome, x, YT3, 60, "i", TINTA2, a),
                                                              M.line(c, x - 150, YT3 + 30, x + 150, YT3 + 30, FIO, a, 3)))
        fcen(c, t, b8, "100", XP3, YT3 + DY3, 100)
        fcen(c, t, b8 + 0.5, "360", XD3, YT3 + DY3, 100)
        fcen(c, t, c8, "40", XP3, YT3 + 2 * DY3, 100)
        fcen(c, t, c8 + 0.5, "x", XD3, YT3 + 2 * DY3, 100, COR)
        p = ep(t, d8 - 0.3, 0.6)
        if p > 0:
            M.line(c, XP3 + 110, YT3 + DY3 - 30, XD3 - 90, YT3 + 2 * DY3 - 40, E.COR, 1, 7, progress=p)
            M.line(c, XP3 + 110, YT3 + 2 * DY3 - 40, XD3 - 110, YT3 + DY3 - 30, E.COR, 1, 7, progress=p)
        fcen(c, t, d8, "100x = 40 · 360 = 14.400", (XP3 + XD3) / 2, 700, 64)
        fcen(c, t, e8, "x = 14.400 ÷ 100", (XP3 + XD3) / 2 - 140, 860, 64)
        bola_txt(c, t, e8 + 0.6, "144°", 1740, 840, 105, 68)
    fase(c, t, C["s08"], C["s09"] - 0.1, um)
    if t < C["s09"] - 0.1:
        return
    X = 1480
    E.frase(c, t, C["s09"] + 0.1, ps("pela mesma conta", "i", 60), X, 250, "center", 0.1)
    E.frase(c, t, a9, ps("bicicleta:", "i", 58) + [("72°", "g", 66, COR)], X, 400, "center", 0.1)
    E.frase(c, t, b9, ps("a pé:", "i", 58) + [("54°", "g", 66, COR)], X, 520, "center", 0.1)
    fcen(c, t, c9, "144 + 90 + 72 + 54 = 360", X, 700, 62)
    E.foco(c, t, c9 + 1.4, 0.5, lambda a: E.selo(c, X - 200, 860, 44, True, a))
    E.frase(c, t, c9 + 1.5, [("a pizza fecha", "g", 60, CERTO)], X - 130, 882, "left", 0.1)


# ---------------- ângulo para porcentagem ----------------
VX, VY, VR = 520, 580, 290


def b_volta(c, t, C, b):
    a0, b0, c0 = C["s10.a"], C["s10.b"], C["s10.c"]
    a1, b1, c1, d1 = (C[f"s11.{k}"] for k in "abcd")
    E.foco(c, t, C["s10"], 0.5, lambda a: disco(c, VX, VY, VR, a))
    fatia(c, VX, VY, VR, -90, 72 * ease_io(prog(t, a0, 0.6)), CATS[2])
    ang_centro(c, t, a0 + 0.4, VX, VY, -90, 72, "72°", sobre(CATS[2]), 62, VR * 0.62, 56)
    if t >= b1:   # a volta riscada em 5 fatias de 72°
        for i in range(1, 5):
            ux, uy = _u(-90 + 72 * i)
            M.line(c, VX, VY, VX + ux * VR, VY + uy * VR, TINTA, ep(t, b1 + 0.15 * i, 0.4), 4, dash=E.TRACO)
        E.foco(c, t, b1 + 0.9, 0.4, lambda a: centro(c, "5 fatias iguais", VX, VY + VR + 90, 50, "i", COR, a))
    X = 1440
    E.frase(c, t, C["s10"] + 0.1, ps("o caminho de volta", "i", 58, TINTA2), X, 200, "center", 0.1)
    E.frase(c, t, a0, ps("uma fatia de", "i", 60) + [("72°", "g", 66, COR)], X, 300, "center", 0.1)
    E.frase(c, t, a0 + 1.2, [("quantos %?", "g", 66)], X, 390, "center", 0.1)

    def conta10():
        fcen(c, t, b0, "f{parte}{total}", X, 600, 76)
        E.frase(c, t, c0, ps("total = a volta inteira,", "i", 50) + [("360°", "g", 54, COR)], X, 820, "center", 0.1)
    fase(c, t, b0, a1 - 0.1, conta10)
    if t < a1 - 0.1:
        return
    E.foco(c, t, a1, 0.5, lambda a: E.fracao(c, "72", "360", 1060, 600, 96, TINTA, a))
    E.pontes(c, t, 1160, 1400, 600, 96, "÷ 72", b1, b1 + 0.6)
    E.foco(c, t, b1 + 1.2, 0.5, lambda a: E.fracao(c, "1", "5", 1480, 600, 96, COR, a))
    fcen(c, t, c1, "= 20%", 1680, 635, 80, COR)
    fcen(c, t, d1, "20% de 20 = 4", X - 160, 870, 64)
    bola_txt(c, t, d1 + 0.8, "4", 1680, 850, 80, 76)
    E.frase(c, t, d1 + 1.4, ps("pessoas: a bicicleta", "i", 46, TINTA2), 1680, 980, "center", 0.08)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    a2, b2, c2 = C["s12.a"], C["s12.b"], C["s12.c"]
    a3, b3, c3 = C["s13.a"], C["s13.b"], C["s13.c"]
    disco(c, VX, VY, VR, ep(t, C["s12"], 0.5))
    certo = ease_io(prog(t, c3, 0.9))
    varre = lerp(28.8 * ease_io(prog(t, c2, 0.6)), 144, certo)
    if varre > 0:
        fatia(c, VX, VY, VR, -90, varre, E.mix(E.mix(ERRADO, PAPEL, 0.3), E.COR, certo), 1, E.mix(ERRADO, TINTA, certo), 5)
    E.saida(c, t, c3, lambda: E.foco(c, t, c2 + 0.4, 0.4, lambda a: E.pilula(c, "28,8°", VX + 150, VY - VR - 50, 50, "g", fundo=ERRADO, a=a)))
    ang_centro(c, t, c3 + 0.8, VX, VY, -90, 144, "144°", BR, 62, VR * 0.6, 60)
    X = 1440

    def um():
        E.frase(c, t, C["s12"] + 0.2, [("erro comum:", "g", 64, ERRADO)], X, 230, "center", 0.1)
        E.frase(c, t, a2, ps("usar o número de", "i", 54) + [("pessoas", "g", 58)], X, 340, "center", 0.1)
        E.frase(c, t, a2 + 1.0, ps("como se fosse", "i", 54) + [("%", "g", 58, ERRADO)], X, 420, "center", 0.1)
        E.frase(c, t, lerp(a2, b2, 0.6), ps("8 pessoas de ônibus", "i", 52, TINTA2), X, 540, "center", 0.1)
        fcen(c, t, b2, "8% de 360 = 28,8°", X, 680, 70, ERRADO)
        E.frase(c, t, c2 + 1.0, ps("fininha demais para", "i", 52) + [("8 em 20", "g", 56)], X, 840, "center", 0.1)
    fase(c, t, C["s12"], C["s13"] - 0.1, um)
    if t < C["s13"] - 0.1:
        return
    E.frase(c, t, a3, [("8", "g", 64, COR)] + ps("= frequência", "i", 58) + [("absoluta", "g", 62, COR)], X, 270, "center", 0.1)
    E.frase(c, t, a3 + 1.2, ps("em pessoas", "i", 50, TINTA2), X, 350, "center", 0.1)
    E.frase(c, t, b3 - 0.6, ps("primeiro, a relativa:", "i", 54), X, 500, "center", 0.1)
    fcen(c, t, b3, "8 ÷ 20 = 0,4 = 40%", X, 610, 70, COR)
    E.frase(c, t, c3, ps("só então o ângulo:", "i", 54), X - 120, 820, "center", 0.1)
    bola_txt(c, t, c3 + 0.6, "144°", X + 270, 800, 110, 70)


# ---------------- atalho (palco escuro) ----------------
RX, RY, RR = 520, 600, 290


def b_atalho(c, t, C, b):
    palco(c, t)
    a4, b4, c4, d4 = (C[f"s14.{k}"] for k in "abcd")
    a5, b5, c5, d5, e5 = (C[f"s15.{k}"] for k in "abcde")
    if t < C["s15"]:
        n = 0 if t < a4 else 1 if t < b4 else 2 if t < c4 else 4 if t < d4 else 1.5
    else:
        n = 0 if t < b5 else 2 if t < c5 else 1
    E.foco(c, t, C["s14"] + 0.1, 0.5, lambda a: roda10(c, t, C["s14"] + 0.1, RX, RY, RR, n, a), blur=0)
    E.foco(c, t, a4 + 0.3, 0.4, lambda a: E.pilula(c, "36°", RX + 90, RY - RR - 60, 46, "g", a=a, cor=E.SOBRE))
    X = 1400

    def um():
        E.frase(c, t, C["s14"] + 0.2, ps("o atalho:", "i", 64, CLARO), X, 190, "center", 0.1)
        fcen(c, t, a4, "10% = 36°", X, 340, 110, BR)
        E.frase(c, t, a4 + 1.6, ps("360 ÷ 10", "i", 52, CLARO), X, 420, "center", 0.1)
        fcen(c, t, b4, "20%: 2 · 36 = 72°", X, 570, 70, BR)
        fcen(c, t, c4, "40%: 4 · 36 = 144°", X, 700, 70, BR)
        fcen(c, t, d4, "15%: 36 + 18 = 54°", X, 830, 70, BR)
        E.frase(c, t, d4 + 1.4, ps("18 = metade de 36", "i", 48, CLARO), X, 920, "center", 0.1)
    fase(c, t, C["s14"], C["s15"] - 0.1, um)
    if t < C["s15"] - 0.1:
        return
    E.frase(c, t, C["s15"] + 0.2, ps("na volta:", "i", 62, CLARO), X, 200, "center", 0.1)
    E.frase(c, t, a5, ps("quantos", "i", 62, CLARO) + [("36", "g", 68, BR)] + ps("cabem?", "i", 62, CLARO), X, 290, "center", 0.1)
    fcen(c, t, b5, "72 = 2 · 36 → 20%", X, 430, 72, BR)
    E.frase(c, t, c5, ps("porque", "i", 56, CLARO) + [("10% = 1 décimo", "g", 60, BR)] + ps("da volta", "i", 56, CLARO), X, 570, "center", 0.1)
    E.foco(c, t, d5, 0.5, lambda a: E.selo(c, X - 330, 720, 44, False, a))
    E.frase(c, t, d5 + 0.1, ps("quebrada,", "i", 56, CLARO) + [("37%:", "g", 60, BR)] + ps("não compensa", "i", 56, CLARO), X - 260, 742, "left", 0.1)
    E.foco(c, t, e5, 0.5, lambda a: E.pilula(c, "vá de regra de três", X, 880, 60, "g", a=a, cor=E.SOBRE))


# ---------------- questão ----------------
FX, FY, FR = 1440, 560, 230
FCOR = [CATS[0], CATS[1], E.mix(FIO, PAPEL, 0.2)]
FINI = [-90, 18, 72]
FANG = [108, 54, 198]
assert sum(FANG) == 360 and [v * 360 // 100 for _, v in FRUTA] == FANG


def frutas(c, t, t0, cx, cy, r, d=1.0):
    E.pizza(c, t, t0, FRUTA, cx, cy, r, cores=FCOR, rotulos=False, d=d)


def b_questao(c, t, C, b):
    a6, b6, c6, d6 = (C[f"s16.{k}"] for k in "abcd")
    E.frase(c, t, C["s16"] + 0.1, ps("hora de testar", "i", 72, COR), XE, 180, passo=0.12)
    E.frase(c, t, a6, [("200", "g", 64, COR)] + ps("pessoas: fruta preferida", "i", 58), XE, 300, passo=0.1)
    E.frase(c, t, b6, [("1)", "g", 60, COR)] + ps("banana:", "i", 58) + [("30%", "g", 62)] + ps("→ quantos graus?", "i", 58), XE, 470, passo=0.1)
    E.frase(c, t, c6, [("2)", "g", 60, COR)] + ps("maçã:", "i", 58) + [("54°", "g", 62)] + ps("→ quantos %?", "i", 58), XE, 600, passo=0.1)
    E.frase(c, t, d6, [("3)", "g", 60, COR)] + ps("quantas pessoas: maçã?", "i", 58), XE, 730, passo=0.1)

    def pz():
        frutas(c, t, a6 + 0.4, FX, FY, FR)
        rot_fora(c, t, b6, FX, FY, FR, FINI[0], FANG[0], "banana", "30%", FCOR[0])
        ang_centro(c, t, b6 + 0.4, FX, FY, FINI[0], FANG[0], "?", BR, 56, FR * 0.6, 60)
        rot_fora(c, t, c6, FX, FY, FR, FINI[1], FANG[1], "maçã", "? %", FCOR[1])
        ang_centro(c, t, c6 + 0.4, FX, FY, FINI[1], FANG[1], "54°", TINTA, 56, FR * 0.66, 44)
    E.saida(c, t, C["s17.a"] - 0.1, pz)
    E.relogio(c, t, C["s17.a"], 1410, 520, 200)


# ---------------- resposta ----------------
QX, QY, QR = 520, 580, 270


def b_resposta(c, t, C, b):
    a8, b8 = C["s18.a"], C["s18.b"]
    a9, b9, c9, d9 = (C[f"s19.{k}"] for k in "abcd")
    frutas(c, t, C["s18"] - 0.6, QX, QY, QR, 0.6)
    rot_fora(c, t, C["s18"] - 0.3, QX, QY, QR, FINI[0], FANG[0], "banana", "30%", FCOR[0])
    ang_centro(c, t, b8 + 0.6, QX, QY, FINI[0], FANG[0], "108°", BR, 56, QR * 0.6, 58)
    rot_fora(c, t, C["s18"] - 0.3, QX, QY, QR, FINI[1], FANG[1], "maçã", "54°", FCOR[1])
    E.foco(c, t, b9, 0.5, lambda a: E.pilula(c, "= 15%", QX + 430, QY + QR + 40, 44, "g", fundo=TINTA, a=a))
    X = 1440

    def um():
        E.frase(c, t, C["s18"] + 0.1, [("1)", "g", 60, COR)] + ps("banana", "i", 60), X, 260, "center", 0.1)
        fcen(c, t, a8, "30% = 3 · 10%", X, 440, 76)
        fcen(c, t, b8, "3 · 36 = 108°", X - 150, 640, 76)
        bola_txt(c, t, b8 + 0.8, "108°", X + 260, 620, 100, 62)
    fase(c, t, C["s18"], C["s19"] - 0.1, um)
    if t < C["s19"] - 0.1:
        return
    E.frase(c, t, C["s19"] + 0.1, [("2)", "g", 56, COR)] + ps("maçã", "i", 56), X, 200, "center", 0.1)
    fcen(c, t, a9, "54 ÷ 360 = 0,15 = 15%", X, 320, 64, COR)
    fcen(c, t, b9 + 1.2, "36 + 18 = 10% + 5%", X, 430, 54, TINTA2)
    E.frase(c, t, c9 - 0.6, [("3)", "g", 56, COR)] + ps("pessoas", "i", 56), X, 580, "center", 0.1)
    fcen(c, t, c9, "10% de 200 = 20", X, 690, 58)
    fcen(c, t, lerp(c9, d9, 0.55), "5% de 200 = 10", X, 790, 58)
    fcen(c, t, d9, "20 + 10 = 30", X - 140, 930, 64)
    bola_txt(c, t, d9 + 0.6, "30", X + 230, 910, 90, 72)
    E.frase(c, t, d9 + 1.0, ps("pessoas", "i", 44, TINTA2), X + 230, 1045, "center", 0.1)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s20"], [("resumindo", "i", 92, COR)], W / 2, 210, "center")
        itens = (("s20.a", ps("a pizza inteira:", "i", 64) + [("100% = 360°", "g", 70, COR)]),
                 ("s20.b", ps("% → ângulo:", "i", 64) + [("a %", "g", 70, COR)] + ps("de 360", "i", 64)),
                 ("s20.c", ps("ângulo → %:", "i", 64) + [("÷ 360", "g", 70, COR)]))
        for i, (k, partes) in enumerate(itens):
            y = 420 + i * 190
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 200, y - 25, 52, a=a), centro(c, str(i + 1), 200, y - 4, 60, "g", E.SOBRE, a)))
            E.frase(c, t, C[k] + 0.1, partes, 290, y, "left", 0.1)
    E.saida(c, t, C["s21"] - 0.1, resumo)
    if t < C["s21"]:
        return
    a1, b1, c1, d1, e1 = (C[f"s21.{k}"] for k in "abcde")
    E.frase(c, t, C["s21"] + 0.2, ps("na próxima aula", "i", 80), XE, 250, passo=0.12)
    E.frase(c, t, a1, ps("o", "i", 84) + [("histograma", "g", 110, COR)], XE, 400)
    E.histograma(c, t, a1 + 0.4, [10, 20, 30, 40, 50, 60], [2, 7, 7, 3, 1], 260, 470, 620, 280, vmax=8, marcas=[0, 4, 8], size=34, valores=False)
    E.frase(c, t, b1, ps("quantos numa", "i", 52) + [("faixa", "g", 56, COR)], 1000, 600, "left", 0.1)
    E.frase(c, t, c1, ps("por que não é", "i", 52) + [("barras", "g", 56, COR)], 1000, 700, "left", 0.1)
    E.foco(c, t, d1, 0.5, lambda a: E.pilula(c, "Inscreva-se", 1550, 380, 76, estilo="g", a=a, cor=E.SOBRE))
    p = ease_io(prog(t, d1 + 0.3, 0.8))
    E.cursor(c, lerp(1830, 1680, p), lerp(700, 405, p), ep(t, d1 + 0.2, 0.4))
    E.frase(c, t, e1, [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 1000, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, setores=b_setores, angulo=b_angulo, regra3=b_regra3, volta=b_volta,
              erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
