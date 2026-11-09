"""Visual — Estudativo · FIS-MOD-011: E = m·c².
Linguagem visual da trilha Física Moderna: veja o cabeçalho do visual.py da FIS-MOD-001. Aqui: núcleo = cacho de esferas
(próton laranja com "+", nêutron cinza); a massa que some aparece na balança de dois pratos (E.balanca) e vira um brilho
âmbar (LUZ). c² em laranja; energia em joule com F.medida. Todo instante vem de C[...]."""
import math

import editorial as E
import fisica as F
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Física", "Física Moderna")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_FIS-MOD-011_e_igual_mc2.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("joule", "formula", "massa", "erro", "atalho", "questao", "fim"))

# todas as contas da aula
c2 = (3e8) ** 2
assert c2 == 9e16 and 3 ** 2 == 9 and 8 * 2 == 16
assert abs(0.1 * 9.8 * 1 - 0.98) < 1e-12                          # maçã de 100 g a 1 m ≈ 1 J
assert 1 * c2 == 9e16 and 9e16 == 90e6 * 1e9                      # 90 milhões de bilhões
assert abs(6.3e13 / c2 - 0.7e-3) < 1e-6                           # Hiroshima (~15 kt ≈ 6,3 × 10¹³ J): ~0,7 g
assert abs(7e-3 * c2 - 6.3e14) < 1e3 and 7 * 9 == 63               # fusão: 6,3 × 10¹⁴ J por kg
assert abs(7e-3 * 3e8 - 2.1e6) < 1e-6 and abs(6.3e14 / 2.1e6 - 3e8) < 1   # o erro: 2,1 × 10⁶ J, 300 milhões de vezes menos
assert abs(1e-3 * c2 - 9e13) < 1                                  # 1 g → 9 × 10¹³ J
assert abs(0.9e-3 - 9e-4) < 1e-15 and 9 * 9 == 81 and -4 + 16 == 12 and abs(9e-4 * c2 - 8.1e13) < 1   # questão
assert 7.5 < 7 / 0.9 < 8                                           # "quase oito"
assert 4.26e9 / 1e3 > 4e6                                          # Sol: ~4 milhões de toneladas por segundo


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


def bola_txt_f(c, t, t0, v, u, cx, cy, h, size, cor=None):
    """resultado com potência de dez numa pílula larga laranja (a esfera não cabe a notação científica)"""
    w = E.formula(None, v + " " + u, 0, 0, size, "g", a=0) + size * 1.4

    def d(a):
        q = ease_back(prog(t, t0, 0.5))
        rr = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w * q / 2, cy - h / 2, w * q, h), h / 2, h / 2)
        c.drawRRect(rr, M.paint(cor or E.COR, a))
        wv = E.formula(None, v + " ", 0, 0, size, "g", a=0)
        x0 = cx - (wv + E.formula(None, u, 0, 0, size * 0.75, "b", a=0)) / 2
        E.formula(c, v, x0, cy + size * 0.36, size, "g", E.SOBRE, a)
        E.formula(c, u, x0 + wv, cy + size * 0.36, size * 0.75, "b", E.SOBRE, a)
    E.foco(c, t, t0, 0.5, d)


# ---------------- peças desta aula ----------------
def nucleo(c, cx, cy, n_p, n_n, r=22, a=1.0):
    """núcleo: prótons (laranja, +) e nêutrons (cinza) num cacho"""
    if a <= 0:
        return
    tot = n_p + n_n
    pts = [(0, 0)] if tot == 1 else [(math.cos(2 * math.pi * k / tot) * r * 0.9, math.sin(2 * math.pi * k / tot) * r * 0.9) for k in range(tot)]
    for k, (dx, dy) in enumerate(pts):
        prot = k % 2 == 0 if n_p == n_n else k < n_p
        E.bola(c, cx + dx, cy + dy, r, E.COR if prot else "#9AA0A8", a)
        if prot:
            centro(c, "+", cx + dx, cy + dy + r * 0.38, r * 1.1, "g", BR, a)


def brilho(c, cx, cy, r, a=1.0):
    if a <= 0:
        return
    p = skia.Paint(AntiAlias=True)
    p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(LUZ, 0.8 * a), M.hexc(LUZ, 0.0)], [0.0, 1.0]))
    c.drawCircle(cx, cy, r, p)


def maca(c, cx, cy, r, a=1.0):
    if a <= 0:
        return
    E.bola(c, cx, cy, r, "#D7263D", a)
    M.line(c, cx, cy - r * 0.9, cx + r * 0.15, cy - r * 1.35, "#6B4226", a, max(4, r * 0.12))
    p = skia.Path(); p.addOval(skia.Rect.MakeXYWH(cx + r * 0.15, cy - r * 1.45, r * 0.6, r * 0.3))
    c.drawPath(p, M.paint("#2FA84F", a))


def b_gancho(c, t, C, b):
    def um():
        E.foco(c, t, C["s01.a"], 0.7, lambda a: sol(c, 1450, 520, 200, a, t), blur=0)
        E.frase(c, t, C["s01.a"], ps("a cada segundo, o Sol fica", "i", 70), XE, 260, passo=0.1)
        E.frase(c, t, C["s01.b"], [("4 milhões", "g", 96, COR), ("de toneladas", "g", 76)], XE, 400, passo=0.15)
        E.frase(c, t, C["s01.b"] + 1.0, [("mais leve", "g", 96)], XE, 520)
        E.frase(c, t, C["s01.c"], [("não", "g", 64, ERRADO)] + ps("escapa como poeira", "i", 64), XE, 680, passo=0.1)
        E.frase(c, t, C["s01.d"], ps("vira", "i", 76) + [("luz e calor", "g", 76, COR)], XE, 800, passo=0.12)
        E.foco(c, t, C["s01.e"], 0.5, lambda a: E.formula(c, "E = m · c^2", XE, 960, 90, "g", TINTA, a))
    E.saida(c, t, C["s02"] - 0.1, um)
    if t >= C["s02"]:
        promessa(c, t, C, "s02", (("s02.a", "usar E = m · c²"), ("s02.b", "a energia da massa perdida")))


def b_lembrete(c, t, C, b):
    def f1(a, x, y):
        E.formula(c, "c = 3 × 10^8 m/s", x - 40, y + 20, 48, "g", TINTA, a, "center")

    def f2(a, x, y):
        nucleo(c, x - 70, y, 1, 1, 18, a); centro(c, "+", x - 5, y + 18, 44, "g", TINTA2, a); nucleo(c, x + 60, y, 1, 1, 18, a)
    lembrete2(c, t, C, "s03", (("s03.b", "a velocidade da luz:", "o limite de tudo"), ("s03.c", "fissão quebra, fusão junta:", "núcleos")), (f1, f2))


# ---------------- o joule ----------------
def b_joule(c, t, C, b):
    E.frase(c, t, C["s04"], ps("antes, a unidade", "i", 76), XE, 220)
    E.frase(c, t, C["s04.a"], ps("energia no SI:", "i", 76) + [("joule", "g", 90, COR), ("(J)", "b", 66, TINTA2)], XE, 380, passo=0.12)
    u = ease_io(prog(t, C["s04.c"], 1.2))
    E.foco(c, t, C["s04.b"], 0.5, lambda a: maca(c, 1300, 900 - 300 * u, 50, a))
    E.foco(c, t, C["s04.b"], 0.5, lambda a: F.chao(c, 1150, 1450, 960, a))
    E.foco(c, t, C["s04.c"], 0.5, lambda a: (M.line(c, 1500, 960, 1500, 640, TINTA2, a, 4, dash=E.TRACO), E.escreve(c, "1 m", 1530, 820, 56, "g", TINTA2, a)))
    E.frase(c, t, C["s04.b"], ps("1 J: erguer uma", "i", 66) + [("maçã de 100 g", "g", 62, "#D7263D")], XE, 560, passo=0.1)
    E.frase(c, t, C["s04.c"], ps("até", "i", 66) + [("1 metro", "g", 62)], XE, 660, passo=0.1)
    E.foco(c, t, C["s04.d"], 0.5, lambda a: E.pilula(c, "pouca coisa", XE + 260, 820, 56, "g", fundo=TINTA, a=a))


# ---------------- a fórmula ----------------
def b_formula(c, t, C, b):
    def s05():
        E.frase(c, t, C["s05"] + 0.2, [("1905", "g", 120, TINTA), ("Einstein", "g", 84, COR)], XE, 240, passo=0.3)
        E.frase(c, t, C["s05.a"], [("massa", "g", 76), ("e", "i", 80), ("energia", "g", 76)] + ps("são a mesma coisa", "i", 72), XE, 380, passo=0.12)
        F.formula_legenda(c, t, C["s05.b"], "E = m · c^2", [("m", "massa", "kg"), ("c", "velocidade da luz", "m/s"), ("E", "energia", "J")],
                          XE, 600, 150, tl=[C["s05.d"], C["s05.e"], C["s05.f"]], size_l=56)
    E.saida(c, t, C["s06"] - 0.1, s05)
    if C["s06"] <= t < C["s07"]:
        def s06():
            E.frase(c, t, C["s06.a"], ps("o segredo:", "i", 76) + [("c²", "g", 90, COR)], XE, 220, passo=0.12)
            E.formula_em(c, t, C["s06.b"], "(3 × 10^8)^2", XE, 420, 110, "g", TINTA)
            E.formula_em(c, t, C["s06.c"], "3^2 = 9", XE + 80, 580, 84, "g", TINTA2)
            E.formula_em(c, t, C["s06.d"], "(10^8)^2 = 10^{16}", XE + 80, 710, 84, "g", TINTA2)
            bola_txt_f(c, t, C["s06.e"], "c^2 = 9 × 10^{16}", "m²/s²", 1300, 520, 120, 80)
            E.frase(c, t, C["s06.f"], ps("um número", "i", 66) + [("gigante", "g", 66, COR)] + ps("multiplicando a massa", "i", 66), XE, 900, passo=0.1)
        E.saida(c, t, C["s07"] - 0.1, s06)
    if t < C["s07"]:
        return
    E.frase(c, t, C["s07.a"], [("1 kg", "g", 90)] + ps("virando energia:", "i", 76), XE, 240, passo=0.12)
    bola_txt_f(c, t, C["s07.a"] + 1.2, "9 × 10^{16}", "J", 1300, 220, 110, 76)
    E.frase(c, t, C["s07.b"], [("90 milhões de bilhões", "g", 66, COR)] + ps("de maçãs erguidas", "i", 66), XE, 440, passo=0.12)
    for i in range(12):
        E.foco(c, t, C["s07.b"] + 0.5 + 0.06 * i, 0.3, lambda a, i=i: maca(c, 300 + 110 * i, 580, 34, a))
    E.frase(c, t, C["s07.c"], ps("Hiroshima:", "i", 70) + [("menos de 1 grama", "g", 70, ERRADO)] + ps("virou energia", "i", 70), XE, 820, passo=0.12)


# ---------------- massa perdida ----------------
def b_massa(c, t, C, b):
    def s08():
        E.frase(c, t, C["s08"], ps("de onde sai a massa?", "i", 76), XE, 200)
        incl = 0.0 if t < C["s08.c"] else -0.5 * ep(t, C["s08.c"], 0.8)
        esq = lambda c_, x, y: (nucleo(c_, x - 40, y - 30, 1, 1, 22), nucleo(c_, x + 40, y - 30, 1, 1, 22))
        dir_ = lambda c_, x, y: (nucleo(c_, x, y - 40, 2, 2, 24) if t >= C["s08.b"] else None)
        E.foco(c, t, C["s08.a"], 0.5, lambda a: E.balanca(c, 1400, 640, esq, dir_, incl, a, 60))
        E.frase(c, t, C["s08.a"], ps("pese o que", "i", 66) + [("entra", "g", 66)], XE, 360, passo=0.1)
        E.frase(c, t, C["s08.b"], ps("pese o que", "i", 66) + [("sai", "g", 66)], XE, 470, passo=0.1)
        E.frase(c, t, C["s08.c"], ps("o que sai pesa", "i", 66) + [("menos", "g", 66, COR)], XE, 600, passo=0.1)
        E.frase(c, t, C["s08.d"], [("defeito", "g", 80, COR), ("de massa", "g", 80, COR)], XE, 760, passo=0.15)
        E.foco(c, t, C["s08.e"], 0.6, lambda a: brilho(c, 1710, 520, 220, a * (0.7 + 0.3 * math.sin(t * 5))))
        E.frase(c, t, C["s08.e"], ps("some da balança e vira", "i", 60) + [("energia", "g", 60, COR)], XE, 900, passo=0.1)
    E.saida(c, t, C["s09"] - 0.1, s08)
    if C["s09"] <= t < C["s10"]:
        def s09():
            E.frase(c, t, C["s09.a"], [("fusão:", "g", 76), ("hidrogênio", "i", 76), ("→", "g", 76, TINTA2), ("hélio", "i", 76)], XE, 220, passo=0.12)
            E.frase(c, t, C["s09.b"], ps("somem uns", "i", 70) + [("7 g", "g", 76, COR)] + ps("a cada", "i", 70) + [("1 kg", "g", 76)], XE, 360, passo=0.12)
            E.formula_em(c, t, C["s09.c"], "7 g = 7 × 10^{−3} kg", XE, 520, 84, "g", TINTA2)
            E.formula_em(c, t, C["s09.d"], "E = 7 × 10^{−3} · 9 × 10^{16}", XE, 680, 84, "g", TINTA)
            E.formula_em(c, t, C["s09.e"], "= 63 × 10^{13}", XE + 80, 820, 84, "g", TINTA2)
            bola_txt_f(c, t, C["s09.f"], "6,3 × 10^{14}", "J", 1400, 820, 110, 76)
        E.saida(c, t, C["s10"] - 0.1, s09)
    if t < C["s10"]:
        return
    for i, (k, nome, desc) in enumerate((("s10.a", "fissão", "usina nuclear"), ("s10.b", "fogueira", "nenhuma balança percebe"))):
        y = 300 + 220 * i
        E.frase(c, t, C[k], [(nome + ":", "g", 76, COR if i == 0 else TINTA)] + ps(desc, "i", 70), XE, y, passo=0.12)
    E.frase(c, t, C["s10.d"], ps("a diferença é o", "i", 70) + [("tamanho", "g", 70, COR)], XE, 760, passo=0.12)
    for i, (rot, h_, cor, k) in enumerate((("nuclear", 360, E.COR, "s10.e"), ("queima", 6, TINTA2, "s10.e"))):
        q = ease_io(prog(t, C[k] + 0.3 * i, 0.8))
        if q > 0:
            M.rrect(c, 1250 + 220 * i, 900 - h_ * q, 140, max(4, h_ * q), 10, cor, 1.0)
            E.foco(c, t, C[k] + 0.3 * i, 0.4, lambda a, rot=rot, i=i: centro(c, rot, 1320 + 220 * i, 960, 46, "g", TINTA, a))
    E.frase(c, t, C["s10.e"] + 0.8, ps("massa transformada por quilo", "i", 48, TINTA2), 1280, 1030, passo=0.06)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s11"], [("cuidado", "g", 96, ERRADO)], XE, 200)
    E.frase(c, t, C["s11.a"], ps("esquecer o", "i", 76) + [("quadrado", "g", 76, ERRADO)], XE + 480, 200, passo=0.12)
    E.formula_em(c, t, C["s11.b"], "7 × 10^{−3} · 3 × 10^8", W / 2, 380, 90, "g", TINTA, "center")
    E.formula_em(c, t, C["s11.c"], "= 2,1 × 10^6 J ?", W / 2, 520, 90, "g", ERRADO, "center")
    if t >= C["s11.d"]:
        E.risco(c, W / 2 - 320, 540, W / 2 + 320, 460, t, C["s11.d"], largura=12)
    E.frase(c, t, C["s11.d"], [("300 milhões", "g", 66, ERRADO)] + ps("de vezes menos", "i", 66), W / 2, 650, "center", 0.12)
    E.frase(c, t, C["s11.e"], ps("confira pela unidade:", "i", 66, COR), XE, 800)
    E.foco(c, t, C["s11.f"], 0.5, lambda a: (E.formula(c, "kg · m/s", XE, 930, 70, "g", ERRADO, a), E.escreve(c, "≠", XE + 360, 930, 70, "g", TINTA2, a)))
    E.foco(c, t, C["s11.f"] + 1.6, 0.5, lambda a: (E.escreve(c, "J =", XE + 460, 930, 70, "g", TINTA, a), E.formula(c, "kg · m^2/s^2", XE + 600, 930, 70, "g", CERTO, a)))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    E.frase(c, t, C["s12"], ps("agora, o atalho", "i", 70, CLARO), W / 2, 160, "center")
    if t < C["s13"]:
        E.frase(c, t, C["s12.a"], ps("decore:", "i", 70, CLARO), W / 2 - 360, 320, "center")
        E.foco(c, t, C["s12.a"] + 0.4, 0.5, lambda a: E.formula(c, "c^2 = 9 × 10^{16}", W / 2 - 120, 320, 96, "g", E.COR, a))
        E.frase(c, t, C["s12.b"], ps("massa em kg:", "i", 64, CLARO), W / 2, 470, "center")
        E.frase(c, t, C["s12.c"], [("número", "g", 70, BR), ("× 9", "g", 80, E.COR)], W / 2, 590, "center", 0.15)
        E.frase(c, t, C["s12.d"], [("expoente", "g", 70, BR), ("+ 16", "g", 80, E.COR)], W / 2, 710, "center", 0.15)
        E.formula_em(c, t, C["s12.e"], "1 g = 10^{−3} kg  →  9 × 10^{−3 + 16}", W / 2, 860, 72, "g", CLARO, "center")
        E.foco(c, t, C["s12.f"], 0.5, lambda a: E.formula(c, "= 9 × 10^{13} J", W / 2, 980, 84, "g", BR, a, "center"))
        return
    E.frase(c, t, C["s13.a"], [("E", "g", 90, BR)] + ps("proporcional à", "i", 70, CLARO) + [("massa", "g", 90, BR)], W / 2, 380, "center", 0.12)
    E.frase(c, t, C["s13.b"], [("2×", "g", 90, E.COR), ("massa", "g", 76, BR), ("→", "g", 76, CLARO), ("2×", "g", 90, E.COR), ("energia", "g", 76, BR)], W / 2, 540, "center", 0.12)
    E.frase(c, t, C["s13.c"], [("grama", "g", 66, ERRADO), ("ou", "i", 66, CLARO), ("tonelada?", "g", 66, ERRADO)], W / 2, 760, "center", 0.12)
    E.frase(c, t, C["s13.d"], ps("antes, passe para", "i", 66, CLARO) + [("kg", "g", 76, BR)], W / 2, 880, "center", 0.12)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s14"], ps("hora de testar", "i", 72, COR), XE, 200)
    E.frase(c, t, C["s14.a"], [("fissão", "g", 72)] + ps("de", "i", 70) + [("1 kg", "g", 72)] + ps("de urânio-235", "i", 70), XE, 340, passo=0.12)
    E.frase(c, t, C["s14.b"], ps("somem", "i", 70) + [("0,9 g", "g", 76, COR)], XE, 470, passo=0.12)
    E.frase(c, t, C["s14.c"], ps("quanta", "i", 70) + [("energia?", "g", 70, COR)], XE, 620, passo=0.12)
    E.frase(c, t, C["s14.d"], ps("fusão, com", "i", 64) + [("7 g", "g", 64)] + ps("por quilo:", "i", 64), XE, 770, passo=0.1)
    E.frase(c, t, C["s14.d"] + 1.2, [("quantas vezes mais?", "g", 64, COR)], XE, 870, passo=0.1)
    if t < C["s15"]:
        E.foco(c, t, C["s14.a"], 0.5, lambda a: nucleo(c, 1500, 460, 6, 6, 40, a))
    else:
        E.relogio(c, t, C["s15.a"], cx=1500, cy=440, r=200)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    def s16():
        E.formula_em(c, t, C["s16.a"], "0,9 g = 9 × 10^{−4} kg", XE, 260, 90, "g", TINTA)
        E.formula_em(c, t, C["s16.b"], "9 × 9 = 81", XE + 80, 420, 84, "g", TINTA2)
        E.formula_em(c, t, C["s16.c"], "−4 + 16 = 12", XE + 80, 560, 84, "g", TINTA2)
        E.formula_em(c, t, C["s16.d"], "81 × 10^{12} J", XE, 740, 90, "g", TINTA)
        bola_txt_f(c, t, C["s16.e"], "8,1 × 10^{13}", "J", 1400, 740, 110, 76)
    E.saida(c, t, C["s17"] - 0.1, s16)
    if t < C["s17"]:
        return
    E.frase(c, t, C["s17.a"], ps("pela proporção:", "i", 76, COR), XE, 220)
    E.frase(c, t, C["s17.b"], [("7 g", "g", 90, COR)] + ps("contra", "i", 80) + [("0,9 g", "g", 90)], XE, 380, passo=0.15)
    E.formula_em(c, t, C["s17.c"], "7 ÷ 0,9 ≈ 7,8", XE, 560, 96, "g", TINTA)
    E.foco(c, t, C["s17.d"], 0.5, lambda a: E.pilula(c, "fusão: quase 8 vezes mais por quilo", W / 2, 780, 60, "g", fundo=E.COR, a=a))
    for i, (h_, cor) in enumerate(((560, E.COR), (72, TINTA2))):
        q = ease_io(prog(t, C["s17.b"] + 0.4 * i, 0.8))
        if q > 0:
            M.rrect(c, 1350 + 200 * i, 640 - h_ * 0.7 * q, 140, h_ * 0.7 * q, 10, cor, 1.0)
            E.foco(c, t, C["s17.b"] + 0.4 * i, 0.4, lambda a, i=i: centro(c, ("fusão", "fissão")[i], 1420 + 200 * i, 700, 44, "g", TINTA, a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def tela_resumo():
        resumo(c, t, C, "s18", (("s18.a", [("massa é energia:", "i", 70), ("E = m · c²", "g", 76, COR)]),
                                ("s18.b", [("c² = 9 × 10¹⁶", "g", 76)]),
                                ("s18.c", [("fissão e fusão:", "i", 70), ("a massa que some", "g", 66, COR)])), y0=380, dy=200)
    E.saida(c, t, C["s19"] - 0.1, tela_resumo)
    if t < C["s19"]:
        return
    E.frase(c, t, C["s19"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C["s19.a"], [("Semicondutores", "g", 104, COR)], XE, 400)
    E.frase(c, t, C["s19.a"] + 0.4, [("e transistores", "g", 104, COR)], XE, 520)
    E.frase(c, t, C["s19.b"], ps("silício, diodo e transistor:", "i", 60) + [("o celular", "g", 60)], XE, 700, passo=0.1)
    E.foco(c, t, C["s19.b"] + 0.5, 0.5, lambda a: (M.rrect(c, 400, 780, 260, 200, 20, "#2A2A30", a),
                                                  [M.rrect(c, 380, 800 + 30 * k, 20, 10, 2, "#9AA0A8", a) for k in range(6)],
                                                  [M.rrect(c, 660, 800 + 30 * k, 20, 10, 2, "#9AA0A8", a) for k in range(6)],
                                                  centro(c, "Si", 530, 905, 70, "g", BR, a)))
    inscreva(c, t, C, "s19")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, joule=b_joule, formula=b_formula, massa=b_massa, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
