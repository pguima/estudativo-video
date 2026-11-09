"""Visual — Estudativo · FIS-MOD-003: espectros e níveis de energia.
Linguagem visual da trilha Física Moderna: veja o cabeçalho do visual.py da FIS-MOD-001. Aqui estreiam os NÍVEIS DE ENERGIA
(escada de linhas em tinta, n à esquerda, valor em eV à direita, o zero tracejado no alto; salto = seta laranja; o fóton
sai pelo lado com a cor da luz) e o ESPECTRO (faixa de 400 a 700 nm: emissão = linhas coloridas no fundo escuro, absorção =
arco-íris com linhas escuras nas mesmas posições). Todo instante vem de C[...]."""
import math

import editorial as E
import fisica as F
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Física", "Física Moderna")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_FIS-MOD-003_espectros_niveis_de_energia.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("niveis", "salto", "espectro", "erro", "atalho", "questao", "fim"))

# todas as contas da aula: hidrogênio, Eₙ = −13,6/n²
NIV = {n: -13.6 / n ** 2 for n in (1, 2, 3, 4)}
assert abs(NIV[2] + 3.4) < 1e-9 and abs(NIV[3] + 1.511) < 1e-3 and abs(NIV[4] + 0.85) < 1e-9
assert abs(-1.51 - (-3.4) - 1.89) < 1e-9                 # 3 → 2: 1,89 eV (vermelho)
assert abs(-3.4 - (-13.6) - 10.2) < 1e-9                 # 2 → 1: 10,2 eV (ultravioleta)
assert abs(-1.51 - (-13.6) - 12.09) < 1e-9               # 3 → 1: 12,09 eV
assert abs(-0.85 - (-3.4) - 2.55) < 1e-9 and 2.55 > 1.89  # 4 → 2: 2,55 eV, mais perto do violeta
assert 3 * 2 // 2 == 3 and 4 * 3 // 2 == 6               # linhas: n(n − 1)/2
assert abs(1240 / 1.89 - 656) < 1 and abs(1240 / 2.55 - 486) < 1   # 656 nm e 486 nm (hc ≈ 1.240 eV·nm)
assert 1868 + 27 == 1895


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- kit da trilha Física Moderna (o mesmo em todas as FIS-MOD; candidatas a fisica.py) ----------------
BR = "#FFFFFF"
LUZ = "#FFB000"   # brilho de fonte de luz (o mesmo da Óptica)
UV = "#8B3CF7"    # ultravioleta
VERM = "#D0202A"  # luz vermelha (não é o vermelho de "errado": vem sempre com a palavra "vermelha")


def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def cor_luz(nm):
    """cor aproximada de uma luz visível pelo comprimento de onda em nanômetros (380 a 750)"""
    pts = ((380, (0.55, 0.0, 0.9)), (440, (0.25, 0.1, 1.0)), (490, (0.0, 0.65, 1.0)), (510, (0.0, 0.85, 0.35)),
           (580, (1.0, 0.9, 0.0)), (620, (1.0, 0.45, 0.0)), (660, (0.95, 0.1, 0.05)), (750, (0.6, 0.0, 0.0)))
    nm = max(380, min(750, nm))
    for (a, ca), (b, cb) in zip(pts, pts[1:]):
        if nm <= b:
            f = (nm - a) / (b - a)
            r, g, bb = (ca[i] + (cb[i] - ca[i]) * f for i in range(3))
            return "#%02X%02X%02X" % (int(r * 255), int(g * 255), int(bb * 255))
    return "#990000"


def pacote(c, x, y, ang, cor, a=1.0, n=3, amp=22, lam=34, largura=5):
    """um fóton parado: n ondas com envelope, centradas em (x, y), andando no ângulo ang (graus, 0 = direita, 90 = cima)"""
    if a <= 0:
        return
    ux, uy = math.cos(math.radians(ang)), -math.sin(math.radians(ang))
    nx, ny = -uy, ux
    L = n * lam
    path = skia.Path()
    for i in range(61):
        s = -L / 2 + L * i / 60
        env = math.sin(math.pi * i / 60)
        d = amp * env * math.sin(2 * math.pi * s / lam)
        px, py = x + ux * s + nx * d, y + uy * s + ny * d
        path.moveTo(px, py) if i == 0 else path.lineTo(px, py)
    c.drawPath(path, M.paint(cor, a, stroke=largura, cap_round=True))
    F._cabeca(c, x + ux * (L / 2 + 16), y + uy * (L / 2 + 16), ux, uy, 20, cor, a)


def foton(c, t, t0, A, B, cor=None, d=1.0, n=3, amp=22, lam=34, largura=5, fica=False):
    """fóton que viaja de A até B entre t0 e t0 + d; some ao chegar (fica=True: para em B)"""
    if t < t0:
        return
    p = ease_io(prog(t, t0, d))
    if p >= 1 and not fica:
        return
    ang = math.degrees(math.atan2(-(B[1] - A[1]), B[0] - A[0]))
    a = min(1.0, prog(t, t0, 0.2)) * (1.0 if fica else 1 - max(0.0, (p - 0.85) / 0.15))
    pacote(c, lerp(A[0], B[0], p), lerp(A[1], B[1], p), ang, cor or E.COR, a, n, amp, lam, largura)


def jorro(c, t, t0, A, B, cor, periodo=0.5, d=1.1, t1=1e9, **kw):
    """fótons saindo de A para B um atrás do outro, de t0 até t1"""
    if t < t0:
        return
    k0 = int(max(0.0, t - t0 - d) // periodo)
    k = k0
    while t0 + k * periodo <= min(t, t1):
        foton(c, t, t0 + k * periodo, A, B, cor, d, **kw)
        k += 1


def eletron(c, cx, cy, r=26, a=1.0):
    """elétron: esferinha azul com o sinal de menos"""
    if a <= 0:
        return
    E.bola(c, cx, cy, r, F.NEG, a)
    M.line(c, cx - r * 0.42, cy, cx + r * 0.42, cy, BR, a, max(3, r * 0.2))


def lampada_fonte(c, cx, cy, r, cor=LUZ, a=1.0, t=0.0):
    """fonte de luz: esfera com brilho pulsando (a mesma linguagem da Óptica)"""
    if a <= 0:
        return
    p = skia.Paint(AntiAlias=True)
    k = r * (2.3 + 0.12 * math.sin(t * 4))
    p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), k, [M.hexc(cor, 0.55 * a), M.hexc(cor, 0.0)], [0.0, 1.0]))
    c.drawCircle(cx, cy, k, p)
    E.bola(c, cx, cy, r, cor, a)


def sol(c, cx, cy, r, a=1.0, t=0.0):
    """o Sol: fonte âmbar com raios em volta"""
    if a <= 0:
        return
    for i in range(12):
        g = math.radians(i * 30 + t * 8)
        M.line(c, cx + math.cos(g) * r * 1.25, cy + math.sin(g) * r * 1.25, cx + math.cos(g) * r * 1.6, cy + math.sin(g) * r * 1.6, LUZ, a, 8)
    lampada_fonte(c, cx, cy, r, LUZ, a, t)


def constante(c, t, t0, x, y, nome, simbolo, valor, size=64, w=None):
    """cartão de constante física: nome em itálico, símbolo laranja e valor em notação científica"""
    w = w or max(620, E.formula(None, valor, 0, 0, size, "g", a=0) + size * 2.4)
    hh = size * 3.1
    p = ep(t, t0, 0.5)
    if p <= 0:
        return
    E.caixa_pontilhada(c, x, y, w, hh, p, prog_=p)
    E.foco(c, t, t0 + 0.1, 0.4, lambda a: E.escreve(c, nome, x + 34, y + size * 1.0, size * 0.62, "i", TINTA2, a))
    E.foco(c, t, t0 + 0.3, 0.4, lambda a: (E.formula(c, simbolo, x + 34, y + size * 2.3, size, "g", COR, a),
                                            E.formula(c, valor, x + 34 + E.formula(None, simbolo + " ", 0, 0, size, "g", a=0), y + size * 2.3, size, "g", TINTA, a)))


def bola_txt(c, t, t0, v, u, cx, cy, r, size, cor=None):
    """resposta na esfera: número pesado e unidade menor"""
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r * ease_back(prog(t, t0, 0.5)), cor, a),
                                     F.medida(c, v, u, cx, cy + size * 0.36, size, E.SOBRE, a, "center", cor_u=E.SOBRE)))


def troca(c, t, itens, fn):
    """um de cada vez: itens = [(instante, arg)], cada um sai quando o próximo chega; fn(arg, a) desenha"""
    for i, (ti, s) in enumerate(itens):
        fim = itens[i + 1][0] - 0.1 if i + 1 < len(itens) else 1e9
        if t >= ti - 0.01:
            E.saida(c, t, fim, lambda s=s, ti=ti: E.foco(c, t, ti, 0.45, lambda a: fn(s, a)), d=0.25)


def promessa(c, t, C, cena, itens):
    """tela do "até o fim da aula": órbita à direita e três itens numerados. itens = [(cue, texto)]"""
    tb = C[cena + ".a"] + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1480, 540, 330 * ease_back(prog(t, tb, 0.8)), giro=12 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, C[cena + ".a"], ps("até o fim da aula", "i", 88), XE, 280, passo=0.14)
    for i, (k, s) in enumerate(itens):
        y = 450 + i * 160
        dt = 1.4 if i == 0 else 0
        E.foco(c, t, C[k] + dt, 0.5, lambda a, i=i, y=y: (E.bola(c, XE + 40, y - 30, 38, a=a), centro(c, str(i + 1), XE + 40, y - 8, 48, "g", BR, a)))
        E.frase(c, t, C[k] + dt + 0.1, [(s, "g", 76, COR if i == 0 else TINTA)], XE + 110, y)


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
        E.frase(c, t, C[k] + 0.3, [(l2, "g", 54, COR)], x + 44, y + 170)
        E.foco(c, t, C[k] + 0.6, 0.5, lambda a, i=i, y=y: desenhos[i](a, x + w - 190, y + 115))
    q1 = ease_io(prog(t, C[itens[1][0]] - 0.35, 0.5))
    E.cursor(c, x + w - 30, lerp(430, 720, q1), ep(t, C[itens[0][0]], 0.4))
    E.frase(c, t, lerp(C[itens[1][0]], C[cena + ".end"], 0.6), ps("faltou alguma?", "i", 56, COR) + ps("procure no canal", "i", 56), 820, 920, "left", 0.12)


def resumo(c, t, C, cena, itens, y0=350, dy=170):
    """resumo numerado: itens = [(cue, partes de E.frase)]"""
    E.frase(c, t, C[cena], [("resumindo", "i", 92, COR)], W / 2, 180, "center")
    for i, (k, partes) in enumerate(itens):
        y = y0 + i * dy
        E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 300, y - 26, 52, a=a), centro(c, str(i + 1), 300, y - 4, 60, "g", BR, a)))
        E.frase(c, t, C[k] + 0.1, partes, 400, y, passo=0.12)


def inscreva(c, t, C, cena):
    """inscreva-se com o cursor e "bons estudos!" (as duas últimas marcas da cena final)"""
    E.foco(c, t, C[cena + ".c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 420, 76, estilo="g", a=a))
    p = ease_io(prog(t, C[cena + ".c"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(720, 445, p), ep(t, C[cena + ".c"] + 0.2, 0.4))
    E.frase(c, t, C[cena + ".d"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1570, 990, "center")


def placa_metal(c, x, y, w, h, a=1.0, rotulo=None):
    """placa de metal vista de lado: retângulo cinza com reflexo"""
    if a <= 0:
        return
    M.rrect(c, x, y, w, h, 10, "#9AA0A8", a)
    M.rrect(c, x + 8, y + 8, w - 16, h * 0.18, 6, "#C9CED4", a)
    if rotulo:
        centro(c, rotulo, x + w / 2, y + h - 22, min(48, h * 0.4), "b", TINTA, a)


# ---------------- peças desta aula ----------------
LINHAS_H = (410, 434, 486, 656)  # linhas visíveis do hidrogênio (nm)
Y_NIV = {1: 900, 2: 560, 3: 420, 4: 350, 0: 250}


def escada(c, t, t0, x, w, niveis=(1, 2, 3), tn=None, zero=True, valores=True, size=46):
    """níveis do hidrogênio: uma linha por nível (tn = instante de cada uma), n à esquerda e o valor à direita"""
    for i, n in enumerate(niveis):
        ti = tn[i] if tn else t0 + 0.25 * i
        y = Y_NIV[n]
        q = ep(t, ti, 0.5)
        if q <= 0:
            continue
        M.line(c, x, y, x + w * ease_io(q), y, TINTA, 1.0, 6)
        E.foco(c, t, ti + 0.1, 0.4, lambda a, n=n, y=y: E.escreve(c, f"n = {n}", x - 150, y + 16, size, "g", TINTA2, a))
        if valores:
            v = {1: "−13,6", 2: "−3,4", 3: "−1,51", 4: "−0,85"}[n]
            E.foco(c, t, ti + 0.2, 0.4, lambda a, v=v, y=y: F.medida(c, v, "eV", x + w + 24, y + 16, size, COR, a))
    if zero and t >= t0:
        q = ep(t, t0, 0.5)
        M.line(c, x, Y_NIV[0], x + w, Y_NIV[0], TINTA2, q * 0.6, 4, dash=E.TRACO)
        E.foco(c, t, t0 + 0.2, 0.4, lambda a: (E.escreve(c, "0", x - 60, Y_NIV[0] + 16, size, "g", TINTA2, a),
                                               E.escreve(c, "solto", x + w + 24, Y_NIV[0] + 16, size * 0.9, "i", TINTA2, a)))


def salto(c, t, t0, x, n0, n1, cor_foton, d=0.6, foton_=True, sobe=False):
    """seta do nível n0 ao n1 em x; descendo, o fóton sai para a direita; subindo (sobe=True), o fóton chega da esquerda"""
    y0, y1 = Y_NIV[n0], Y_NIV[n1]
    if sobe:
        foton(c, t, t0, (x - 380, (y0 + y1) / 2), (x - 20, (y0 + y1) / 2), cor_foton, 0.8, n=3, amp=14, lam=24, largura=5)
        t0 += 0.8
    if t < t0:
        return
    F.seta(c, x, y0 + (-8 if sobe else 8), x, y1 + (8 if sobe else -8), E.COR, 1.0, 8, None, ease_io(prog(t, t0, d)))
    eletron(c, x, lerp(y0, y1, ease_io(prog(t, t0, d))) - 26, 20, 1.0)
    if foton_ and not sobe:
        foton(c, t, t0 + d * 0.8, (x + 30, (y0 + y1) / 2), (x + 380, (y0 + y1) / 2), cor_foton, 1.0, n=3, amp=14, lam=24, largura=5, fica=True)


def faixa(c, x, y, w, h, tipo, a=1.0, p=1.0, linhas=LINHAS_H, lw=10):
    """espectro de 400 a 700 nm: tipo "continuo" (arco-íris), "emissao" (linhas coloridas no escuro) ou "absorcao"
    (arco-íris com linhas escuras); p = quanto já se desenhou, da esquerda para a direita"""
    if a <= 0 or p <= 0:
        return
    nm_x = lambda nm: x + w * (nm - 400) / 300
    c.save(); c.clipRect(skia.Rect.MakeXYWH(x, y, w * p, h))
    if tipo == "emissao":
        M.rrect(c, x, y, w, h, 8, "#101015", a)
        for nm in linhas:
            M.rrect(c, nm_x(nm) - lw / 2, y, lw, h, 0, cor_luz(nm), a)
    else:
        n = 150
        for i in range(n):
            M.rrect(c, x + w * i / n, y, w / n + 1, h, 0, cor_luz(400 + 300 * i / n), a)
        if tipo == "absorcao":
            for nm in linhas:
                M.rrect(c, nm_x(nm) - lw / 2, y, lw, h, 0, "#101015", a)
    c.restore()


def tubo(c, cx, cy, w, h, cor, a=1.0, t=0.0):
    """tubo de gás aceso: cápsula com brilho"""
    if a <= 0:
        return
    p = skia.Paint(AntiAlias=True)
    k = w * 0.8
    p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), k, [M.hexc(cor, 0.45 * a), M.hexc(cor, 0.0)], [0.0, 1.0]))
    c.drawCircle(cx, cy, k, p)
    M.rrect(c, cx - w / 2, cy - h / 2, w, h, h / 2, E.mix(cor, "#FFFFFF", 0.35), a)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2, cy - h / 2, w, h), h / 2, h / 2), M.paint(TINTA2, a, stroke=3))


def prisma(c, cx, cy, s, a=1.0):
    """prisma de vidro visto de frente"""
    if a <= 0:
        return
    p = skia.Path()
    p.moveTo(cx, cy - s * 0.6); p.lineTo(cx + s * 0.55, cy + s * 0.4); p.lineTo(cx - s * 0.55, cy + s * 0.4); p.close()
    c.drawPath(p, M.paint("#7FC8E8", 0.45 * a))
    c.drawPath(p, M.paint(TINTA2, a, stroke=4))


def b_gancho(c, t, C, b):
    def um():
        E.foco(c, t, C["s01.a"], 0.7, lambda a: sol(c, 1450, 520, 170, a, t), blur=0)
        E.frase(c, t, C["s01.a"], ps("ninguém nunca foi ao", "i", 76) + [("Sol", "g", 76, COR)], XE, 260, passo=0.12)
        E.frase(c, t, C["s01.a"] + 1.6, ps("mas sabemos do que ele é feito", "i", 62, TINTA2), XE, 360, passo=0.1)
        E.frase(c, t, C["s01.b"], [("hélio:", "g", 80), ("1868", "g", 80, COR)] + ps("no Sol", "i", 76), XE, 540, passo=0.15)
        E.frase(c, t, C["s01.c"], [("1895", "g", 80, TINTA2)] + ps("na Terra", "i", 76), XE, 680, passo=0.15)
        E.foco(c, t, C["s01.c"] + 0.8, 0.4, lambda a: E.pilula(c, "quase 30 anos depois", XE + 760, 660, 42, "b", fundo=TINTA, a=a))
        E.frase(c, t, C["s01.d"], ps("a pista: as", "i", 76) + [("cores da luz", "g", 76, COR)], XE, 870, passo=0.12)
        faixa(c, 1100, 900, 700, 90, "absorcao", ep(t, C["s01.d"], 0.4), ease_io(prog(t, C["s01.d"] + 0.4, 1.0)))
    E.saida(c, t, C["s02"] - 0.1, um)
    if t >= C["s02"]:
        promessa(c, t, C, "s02", (("s02.a", "cada salto, uma cor"), ("s02.b", "emissão e absorção")))


def b_lembrete(c, t, C, b):
    def f1(a, x, y):
        pacote(c, x, y, 0, E.COR, a, n=3, amp=26, lam=44, largura=7)

    def f2(a, x, y):
        for k, yy in enumerate((y + 60, y, y - 40)):
            M.line(c, x - 100, yy, x + 100, yy, TINTA, a, 5)
        eletron(c, x, y - 22, 18, a)
    lembrete2(c, t, C, "s03", (("s03.b", "a energia do fóton é h vezes f:", "f maior, fóton mais forte"), ("s03.c", "modelo de Bohr:", "só certos níveis de energia")), (f1, f2))


# ---------------- os níveis ----------------
def b_niveis(c, t, C, b):
    E.frase(c, t, C["s04.a"], ps("degraus de uma", "i", 72) + [("escada", "g", 72, COR)], XE, 200, passo=0.12)
    E.frase(c, t, C["s04.a"] + 0.8, [("hidrogênio", "g", 64, TINTA2)], XE, 300)
    escada(c, t, C["s04.a"], 1000, 560, (1, 2, 3), tn=[C["s04.b"], C["s04.c"], C["s04.d"]], zero=False)
    if t >= C["s04.b"]:
        eletron(c, 1280, Y_NIV[1] - 26, 22, ep(t, C["s04.b"], 0.4))
    if t < C["s05"]:
        return
    escada(c, t, C["s05.a"], 1000, 560, (), zero=True)
    E.frase(c, t, C["s05"], ps("por que", "i", 76) + [("negativos?", "g", 76, COR)], XE, 430, passo=0.12)
    E.frase(c, t, C["s05.a"], [("zero", "g", 66)] + ps("= elétron solto", "i", 66), XE, 560, passo=0.12)
    E.frase(c, t, C["s05.b"], [("preso:", "g", 66)] + ps("menos que zero", "i", 66), XE, 670, passo=0.12)
    E.frase(c, t, C["s05.c"], ps("mais embaixo,", "i", 66) + [("mais preso", "g", 66, COR)], XE, 800, passo=0.12)
    if t >= C["s05.b"]:  # o elétron precisa de energia para subir até o zero
        F.seta(c, 1460, Y_NIV[1] - 10, 1460, Y_NIV[0] + 10, TINTA2, 1.0, 6, None, ease_io(prog(t, C["s05.b"] + 0.5, 0.8)))
        E.foco(c, t, C["s05.b"] + 1.0, 0.4, lambda a: E.escreve(c, "dar energia", 1480, 330, 40, "i", TINTA2, a))


# ---------------- o salto ----------------
def b_salto(c, t, C, b):
    x0, w = 1150, 460
    def s06():
        escada(c, t, C["s06"], x0, w, (1, 2, 3), zero=False, valores=False)
        E.frase(c, t, C["s06.a"], ps("o elétron", "i", 76) + [("desce", "g", 76, COR)], XE, 260, passo=0.12)
        E.frase(c, t, C["s06.b"], ps("e solta um", "i", 76) + [("fóton", "g", 76, COR)], XE, 380, passo=0.12)
        salto(c, t, C["s06.a"], 1300, 3, 2, VERM)
        E.frase(c, t, C["s06.c"], ps("energia do fóton =", "i", 60) + [("diferença", "g", 60, COR)], XE, 560, passo=0.1)
        E.foco(c, t, C["s06.d"], 0.5, lambda a: (E.escreve(c, "E de cima", XE, 720, 70, "g", TINTA, a), E.escreve(c, "−", XE + 330, 720, 70, "g", TINTA2, a),
                                                 E.escreve(c, "E de baixo", XE + 400, 720, 70, "g", TINTA, a)))
        E.foco(c, t, C["s06.e"], 0.5, lambda a: E.formula(c, "= h · f", XE, 850, 90, "g", COR, a))
    E.saida(c, t, C["s07"] - 0.1, s06)
    if C["s07"] <= t < C["s08"]:
        def s07():
            escada(c, t, C["s07"], x0, w, (1, 2, 3), zero=False)
            salto(c, t, C["s07"] + 0.3, 1250, 3, 2, VERM)
            E.frase(c, t, C["s07"], [("3", "g", 76, COR), ("→", "g", 76, TINTA2), ("2:", "g", 76, COR)], XE, 220, passo=0.12)
            E.formula_em(c, t, C["s07.a"], "−1,51 − (−3,4)", XE, 360, 84, "g", TINTA)
            E.foco(c, t, C["s07.b"], 0.5, lambda a: F.medida(c, "= 1,89", "eV", XE, 480, 84, TINTA, a))
            E.foco(c, t, C["s07.c"], 0.4, lambda a: E.pilula(c, "vermelho", XE + 560, 455, 46, "g", fundo=VERM, a=a))
            salto(c, t, C["s07.d"], 1450, 2, 1, UV)
            E.frase(c, t, C["s07.d"], [("2", "g", 76, COR), ("→", "g", 76, TINTA2), ("1:", "g", 76, COR)], XE, 680, passo=0.12)
            E.foco(c, t, C["s07.d"] + 0.8, 0.5, lambda a: F.medida(c, "10,2", "eV", XE + 300, 680, 84, TINTA, a))
            E.foco(c, t, C["s07.e"], 0.4, lambda a: E.pilula(c, "ultravioleta: o olho não vê", XE + 420, 800, 46, "g", fundo=UV, a=a))
        E.saida(c, t, C["s08"] - 0.1, s07)
    if t < C["s08"]:
        return
    E.frase(c, t, C["s08.a"], [("salto grande", "g", 70), ("→", "g", 70, TINTA2)] + ps("fóton forte, perto do", "i", 70) + [("violeta", "g", 70, cor_luz(410))],
            XE, 260, passo=0.1)
    E.frase(c, t, C["s08.b"], [("salto pequeno", "g", 70), ("→", "g", 70, TINTA2)] + ps("fóton fraco, perto do", "i", 70) + [("vermelho", "g", 70, VERM)],
            XE, 400, passo=0.1)
    E.frase(c, t, C["s08.c"], ps("degraus fixos:", "i", 70) + [("só algumas cores", "g", 70, COR)], XE, 600, passo=0.12)
    faixa(c, 260, 720, 1400, 150, "emissao", ep(t, C["s08.c"] + 0.6, 0.4), ease_io(prog(t, C["s08.c"] + 0.8, 1.2)))


# ---------------- emissão e absorção ----------------
def b_espectro(c, t, C, b):
    def s09():
        E.foco(c, t, C["s09"], 0.5, lambda a: tubo(c, 380, 330, 300, 90, "#E86A9A", a, t))
        E.foco(c, t, C["s09"] + 0.4, 0.5, lambda a: centro(c, "gás quente", 380, 450, 46, "i", TINTA2, a))
        if t >= C["s09"] + 0.6:
            F.poli(c, [(560, 330), (900, 330)], ease_io(prog(t, C["s09"] + 0.6, 0.5)), E.COR, 1.0, 6)
        E.foco(c, t, C["s09"] + 0.8, 0.5, lambda a: prisma(c, 1000, 340, 220, a))
        E.foco(c, t, C["s09"] + 1.0, 0.4, lambda a: centro(c, "prisma", 1000, 480, 46, "i", TINTA2, a))
        if t >= C["s09.a"] - 0.4:
            for k, nm in enumerate(LINHAS_H):
                yy = 300 + 22 * k
                F.poli(c, [(1080, 340), (1300, yy)], ease_io(prog(t, C["s09.a"] - 0.4, 0.5)), cor_luz(nm), 1.0, 4)
        faixa(c, 1320, 240, 460, 200, "emissao", ep(t, C["s09.a"], 0.4), ease_io(prog(t, C["s09.a"], 0.8)))
        E.frase(c, t, C["s09.a"], ps("poucas", "i", 70) + [("linhas coloridas", "g", 70, COR)] + ps("no escuro", "i", 70), XE, 640, passo=0.12)
        E.frase(c, t, C["s09.b"], [("espectro", "g", 96), ("de emissão", "g", 96, COR)], XE, 790, passo=0.15)
        E.frase(c, t, C["s09.c"], ps("cada elemento, uma", "i", 64) + [("impressão digital", "g", 62)], XE, 930, passo=0.1)
    E.saida(c, t, C["s10"] - 0.1, s09)
    if C["s10"] <= t < C["s11"]:
        def s10():
            E.foco(c, t, C["s10.a"], 0.5, lambda a: lampada_fonte(c, 260, 330, 60, "#FFF4D6", a, t))
            E.foco(c, t, C["s10.a"] + 0.3, 0.4, lambda a: centro(c, "luz branca", 260, 460, 44, "i", TINTA2, a))
            if t >= C["s10.a"] + 0.4:
                F.poli(c, [(340, 330), (1000, 330)], ease_io(prog(t, C["s10.a"] + 0.4, 0.6)), "#C9C2B0", 1.0, 10)
            E.foco(c, t, C["s10.a"] + 0.5, 0.5, lambda a: tubo(c, 640, 330, 260, 110, "#B9C4CF", a, 0))
            E.foco(c, t, C["s10.a"] + 0.7, 0.4, lambda a: centro(c, "gás frio", 640, 460, 44, "i", TINTA2, a))
            E.foco(c, t, C["s10.a"] + 0.8, 0.5, lambda a: prisma(c, 1000, 340, 220, a))
            faixa(c, 1200, 240, 600, 200, "absorcao", ep(t, C["s10.c"], 0.4), ease_io(prog(t, C["s10.c"], 0.9)))
            E.frase(c, t, C["s10.b"], ps("só o fóton que paga o", "i", 60) + [("salto exato", "g", 60, COR)], XE, 600, passo=0.1)
            E.frase(c, t, C["s10.d"], [("espectro", "g", 96), ("de absorção", "g", 96, COR)], XE, 760, passo=0.15)
            faixa(c, 1200, 480, 600, 120, "emissao", ep(t, C["s10.e"], 0.4), ease_io(prog(t, C["s10.e"], 0.6)))
            if t >= C["s10.e"] + 0.6:
                for nm in LINHAS_H:
                    xx = 1200 + 600 * (nm - 400) / 300
                    M.line(c, xx, 440, xx, 480, TINTA2, ep(t, C["s10.e"] + 0.6, 0.4), 3, dash=[6, 6])
            E.frase(c, t, C["s10.e"], ps("mesmas posições", "g", 64, COR), XE, 900, passo=0.12)
        E.saida(c, t, C["s11"] - 0.1, s10)
    if t < C["s11"]:
        return
    E.foco(c, t, C["s11"], 0.6, lambda a: sol(c, 380, 420, 150, a, t), blur=0)
    E.frase(c, t, C["s11.a"], ps("a luz do Sol tem", "i", 66) + [("linhas escuras", "g", 66)], 720, 280, passo=0.1)
    faixa(c, 720, 330, 1000, 110, "absorcao", ep(t, C["s11.a"], 0.4), ease_io(prog(t, C["s11.a"] + 0.3, 0.8)), linhas=(431, 486, 527, 589, 656), lw=6)
    E.frase(c, t, C["s11.b"], ps("num eclipse: uma", "i", 66) + [("linha amarela", "g", 66, "#C99A00")], 720, 620, passo=0.1)
    faixa(c, 720, 670, 1000, 110, "emissao", ep(t, C["s11.b"] + 0.5, 0.4), ease_io(prog(t, C["s11.b"] + 0.5, 0.8)), linhas=(588,), lw=10)
    E.frase(c, t, C["s11.c"], ps("de nenhum elemento conhecido", "i", 56, TINTA2), 720, 870, passo=0.08)
    E.frase(c, t, C["s11.d"], [("era", "i", 90), ("o hélio", "g", 90, COR)], 720, 1000, passo=0.15)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s12"], [("cuidado", "g", 96, ERRADO)], XE, 200)
    E.frase(c, t, C["s12.a"], ps("valor do nível", "i", 70) + [("≠", "g", 70, ERRADO)] + ps("diferença", "i", 70), XE + 480, 200, passo=0.1)
    escada(c, t, C["s12"] + 0.5, 1180, 420, (1, 2, 3), zero=False)
    E.frase(c, t, C["s12.b"], ps("fóton do nível 3:", "i", 66), XE, 380, passo=0.1)
    E.foco(c, t, C["s12.b"] + 0.8, 0.5, lambda a: F.medida(c, "1,51", "eV ?", XE + 500, 380, 84, ERRADO, a))
    if t >= C["s12.c"]:
        E.risco(c, XE + 480, 400, XE + 760, 320, t, C["s12.c"], largura=10)
    E.frase(c, t, C["s12.c"], ps("o fóton leva o", "i", 64) + [("tamanho do salto", "g", 64, COR)], XE, 520, passo=0.1)
    salto(c, t, C["s12.d"], 1300, 3, 2, VERM, foton_=False)
    E.foco(c, t, C["s12.d"], 0.5, lambda a: (E.escreve(c, "3 → 2:", XE, 680, 70, "g", TINTA, a), F.medida(c, "1,89", "eV", XE + 260, 680, 84, CERTO, a)))
    salto(c, t, C["s12.e"], 1480, 3, 1, UV, foton_=False)
    E.foco(c, t, C["s12.e"], 0.5, lambda a: (E.escreve(c, "3 → 1:", XE, 820, 70, "g", TINTA, a), F.medida(c, "12,09", "eV", XE + 260, 820, 84, CERTO, a)))
    E.frase(c, t, C["s12.e"] + 1.4, ps("mesma partida, fótons diferentes", "i", 56, TINTA2), XE, 950, passo=0.08)


# ---------------- atalho (palco escuro) ----------------
def escada_palco(c, t, t0, x, w, niveis):
    for i, n in enumerate(niveis):
        y = {1: 860, 2: 640, 3: 480, 4: 400}[n]
        q = ep(t, t0 + 0.15 * i, 0.4)
        M.line(c, x, y, x + w * q, y, BR, 1.0, 5) if q > 0 else None
        E.foco(c, t, t0 + 0.15 * i, 0.4, lambda a, n=n, y=y: E.escreve(c, f"n = {n}", x - 140, y + 14, 42, "g", CLARO, a))


def b_atalho(c, t, C, b):
    palco(c, t)
    E.frase(c, t, C["s13"], ps("agora, o atalho", "i", 70, CLARO), XE, 160)
    if t < C["s14"]:
        E.frase(c, t, C["s13.a"], ps("quantas", "i", 70, CLARO) + [("linhas diferentes?", "g", 66, BR)], XE, 280, passo=0.12)
        E.frase(c, t, C["s13.b"], ps("cada", "i", 60, CLARO) + [("par de níveis", "g", 60, E.COR)] + ps("= um salto", "i", 60, CLARO), XE, 380, passo=0.1)
        escada_palco(c, t, C["s13.b"], 1150, 560, (1, 2, 3))
        ys = {1: 860, 2: 640, 3: 480}
        for k, (a_, b_, dx) in enumerate(((3, 2, 120), (3, 1, 300), (2, 1, 480))):
            tk = C["s13.c"] + 0.7 * k
            F.seta(c, 1120 + dx, ys[a_] + 8, 1120 + dx, ys[b_] - 8, E.COR, 1.0, 8, None, ease_io(prog(t, tk, 0.5)))
            E.foco(c, t, tk + 0.3, 0.4, lambda a, a_=a_, b_=b_, k=k: E.escreve(c, f"{a_} → {b_}", XE, 560 + 110 * k, 64, "g", BR, a))
        E.foco(c, t, C["s13.d"], 0.5, lambda a: (E.bola(c, XE + 470, 680, 80, a=a), centro(c, "3", XE + 470, 708, 80, "g", BR, a)))
        E.foco(c, t, C["s13.d"] + 0.3, 0.4, lambda a: E.escreve(c, "linhas", XE + 580, 700, 60, "i", CLARO, a))
        return
    E.formula_em(c, t, C["s14.a"], "linhas = f{n · (n − 1)}{2}", W / 2, 400, 120, "g", BR, "center")
    E.frase(c, t, C["s14.a"] + 1.0, ps("n = nível de partida", "i", 60, CLARO), W / 2, 560, "center", 0.1)
    E.formula_em(c, t, C["s14.a"] + 1.8, "n = 3:  f{3 · 2}{2} = 3", W / 2, 720, 84, "g", E.COR, "center")
    E.frase(c, t, C["s14.b"], ps("é o número de", "i", 58, CLARO) + [("pares", "g", 58, BR)] + ps("de degraus", "i", 58, CLARO), W / 2, 870, "center", 0.1)
    E.frase(c, t, C["s14.c"], [("não", "g", 56, ERRADO)] + ps("dá a cor: para isso, a diferença de energia", "i", 56, CLARO), W / 2, 990, "center", 0.08)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s15"], ps("hora de testar", "i", 72, COR), XE, 200)
    E.frase(c, t, C["s15.a"], [("n = 4:", "g", 70)], XE, 330)
    E.foco(c, t, C["s15.a"] + 0.5, 0.5, lambda a: F.medida(c, "−0,85", "eV", XE + 240, 330, 76, COR, a))
    E.frase(c, t, C["s15.b"], ps("fóton do salto", "i", 66) + [("4 → 2?", "g", 66, COR)], XE, 470, passo=0.12)
    E.frase(c, t, C["s15.c"], ps("mais perto do", "i", 66) + [("violeta", "g", 64, cor_luz(410))] + ps("ou do", "i", 66) + [("vermelho", "g", 64, VERM)],
            XE, 610, passo=0.1)
    E.frase(c, t, C["s15.c"] + 1.2, ps("que o salto", "i", 66) + [("3 → 2?", "g", 64)], XE, 700, passo=0.1)
    E.frase(c, t, C["s15.d"], ps("linhas com elétrons no", "i", 66) + [("nível 4?", "g", 66, COR)], XE, 860, passo=0.1)
    if t < C["s16"]:
        escada(c, t, C["s15.a"], 1560, 260, (1, 2, 3, 4), zero=False, valores=False, size=36)
    else:
        E.relogio(c, t, C["s16.a"], cx=1500, cy=440, r=200)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    def s17():
        escada(c, t, C["s17"], 1100, 400, (1, 2, 3, 4), zero=False, valores=False)
        salto(c, t, C["s17.a"], 1250, 4, 2, cor_luz(486))
        E.formula_em(c, t, C["s17.a"], "−0,85 − (−3,4)", XE, 280, 90, "g", TINTA)
        E.foco(c, t, C["s17.b"], 0.5, lambda a: F.medida(c, "= 2,55", "eV", XE, 420, 96, TINTA, a))
        E.formula_em(c, t, C["s17.c"], "2,55 > 1,89", XE, 580, 90, "g", TINTA2)
        E.frase(c, t, C["s17.d"], ps("mais perto do", "i", 70) + [("violeta", "g", 70, cor_luz(410))], XE, 740, passo=0.12)
        E.foco(c, t, C["s17.d"] + 1.2, 0.4, lambda a: E.pilula(c, "azul-esverdeado, 486 nm", XE + 400, 860, 46, "g", fundo=cor_luz(486), a=a))
    E.saida(c, t, C["s18"] - 0.1, s17)
    if t < C["s18"]:
        return
    E.formula_em(c, t, C["s18.a"], "f{4 · 3}{2}", XE + 100, 330, 120, "g", TINTA, "center")
    E.foco(c, t, C["s18.b"], 0.4, lambda a: E.formula(c, "= f{12}{2}", XE + 220, 330, 120, "g", TINTA2, a))
    bola_txt(c, t, C["s18.c"], "6", "linhas", XE + 280, 640, 150, 90)
    ys = {1: 920, 2: 660, 3: 500, 4: 420}
    for n, y in ys.items():
        q = ep(t, C["s18"] + 0.2 * n, 0.4)
        M.line(c, 1000, y, 1760, y, TINTA, q, 5) if q > 0 else None
    for k, (a_, b_) in enumerate(((4, 3), (4, 2), (4, 1), (3, 2), (3, 1), (2, 1))):
        tk = C["s18.d"] + 0.45 * k
        F.seta(c, 1060 + 120 * k, ys[a_] + 8, 1060 + 120 * k, ys[b_] - 8, E.COR, 1.0, 7, None, ease_io(prog(t, tk, 0.4)))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def tela_resumo():
        resumo(c, t, C, "s19", (("s19.a", [("fóton", "g", 66), ("=", "g", 66, TINTA2), ("diferença", "g", 66, COR), ("entre os níveis", "i", 70)]),
                                ("s19.b", [("salto maior", "g", 66), ("→", "g", 66, TINTA2), ("mais violeta", "i", 70)]),
                                ("s19.c", [("emissão:", "g", 60), ("coloridas;", "i", 66), ("absorção:", "g", 60), ("escuras", "i", 66)])), y0=380, dy=200)
        faixa(c, 1300, 900, 300, 60, "emissao", ep(t, C["s19.c"] + 0.5, 0.4))
        faixa(c, 1300, 980, 300, 60, "absorcao", ep(t, C["s19.c"] + 0.8, 0.4))
    E.saida(c, t, C["s20"] - 0.1, tela_resumo)
    if t < C["s20"]:
        return
    E.frase(c, t, C["s20"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C["s20.a"], [("Dualidade", "g", 110, COR)], XE, 400)
    E.frase(c, t, C["s20.a"] + 0.4, [("onda-partícula", "g", 110, COR)], XE, 530)
    if t >= C["s20.a"]:
        F.onda(c, t, C["s20.a"] + 0.5, 300, 900, 760, 50, 120, E.COR, 1.0, velocidade=90, eixo=False)
    E.foco(c, t, C["s20.b"], 0.5, lambda a: eletron(c, 1000, 760, 34, a))
    inscreva(c, t, C, "s20")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, niveis=b_niveis, salto=b_salto, espectro=b_espectro, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
