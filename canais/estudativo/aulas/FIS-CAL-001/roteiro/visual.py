"""Visual — Estudativo · FIS-CAL-001: temperatura e escalas termométricas. Primeira aula da trilha Calor e Termodinâmica.

Segue a linguagem visual da Física (cabeçalho do visual.py da FIS-CIN-001: medida = número + unidade, fórmula com legenda,
conversão com F.fila, certo/errado, atalho no palco). LINGUAGEM VISUAL DA TRILHA CALOR E TERMODINÂMICA (FIS-CAL-*):
- QUENTE = laranja (E.COR), FRIO = azul (F.NEG). Corpo quente laranja, corpo frio azul; no equilíbrio, os dois ganham a
  mesma cor intermediária (E.mix). Gelo = azul-claro (GELO) com brilho branco; água líquida = azul translúcido (AGUA).
- TEMPERATURA: F.termometro (líquido laranja) com a marca e a medida ao lado ("40 °C"). Várias escalas = termômetros lado a
  lado com os pontos fixos (gelo derretendo, água fervendo) em tracejados horizontais que atravessam todos (peça `escalas`).
- TEMPERATURA = AGITAÇÃO: `particulas` — caixa com bolinhas que tremem; quanto mais quente, mais tremem (laranja); frio,
  quase paradas (azul).
- CALOR: `seta_calor` — seta ONDULADA laranja com "calor" (ou "Q") escrito, sempre do quente para o frio. Calor nunca fica
  "dentro" do corpo na tela: só aparece passando.
- VARIAÇÃO: Δ em laranja; a subida no termômetro é marcada por `cota_v` (colchete vertical) com o valor "ΔC = 10 °C".
- FÓRMULA NOVA: F.formula_legenda (letra laranja + nome + unidade). Escalas na tela com as letras C, F e K (sem índice).
- CONTA: passos empilhados à esquerda (E.formula, tinta), resultado na esfera (bola_txt: laranja; verde na resposta).
- Unidade de calor: cal (cinza-tinta, como toda unidade). Gráficos T × Q e T × t com F.grafico; patamar de mudança de
  estado pintado com a cor do estado (gelo/água) e a etapa escrita em cima.
- Atalho no palco escuro (E.palco) com CLARO e branco; questão com E.relogio; texto à esquerda (XE), desenho à direita.
Todo instante vem de C[...] (marcadores do roteiro), para acompanhar a voz real quando ela chegar."""
import math

import editorial as E
import fisica as F
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Física", "Calor e Termodinâmica")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_FIS-CAL-001_temperatura_escalas_termometricas.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("calor", "escalas", "formula", "variacao", "atalho", "questao", "fim"))
BR = "#FFFFFF"
FRIO = F.NEG
GELO = "#A9D8F5"
AGUA = "#5BA8E0"

# todas as contas da aula
c_de_f = lambda f: (f - 32) * 5 / 9
f_de_c = lambda c: c * 9 / 5 + 32
assert c_de_f(104) == 40 and (104 - 32) == 72 and 72 / 9 == 8 and 8 * 5 == 40
assert 212 - 32 == 180 and 100 / 20 == 5 and 180 / 20 == 9
assert f_de_c(25) == 77 and 25 / 5 == 5 and 5 * 9 == 45 and 45 + 32 == 77 and 25 + 273 == 298 and 27 + 273 == 300
assert f_de_c(25) - 32 == (212 - 32) / 4 and 25 == 100 / 4                       # um quarto do caminho nas duas
assert 10 / 5 * 9 == 18 and f_de_c(10) == 50 and f_de_c(20) == 68 and f_de_c(30) == 86 and 86 - 68 == 18
assert f_de_c(-40) == -40 and 32 + 5 * 9 == 77
assert c_de_f(59) == 15 and 59 - 32 == 27 and 27 / 9 == 3 and 3 * 5 == 15 and 18 / 9 * 5 == 10
assert round(c_de_f(100), 1) == 37.8  # (não usado na fala: por isso o gancho usa 104 °F)


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças desta aula (e da trilha) ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def bola_txt(c, t, t0, s, cx, cy, r, size, cor=None):
    """resposta na esfera: "40 °C" com a unidade menor"""
    v, _, u = s.partition(" ")
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r * ease_back(prog(t, t0, 0.5)), cor, a),
                                     F.medida(c, v, u, cx, cy + size * 0.36, size, E.SOBRE, a, "center", cor_u=E.SOBRE)))


def pilula_em(c, t, t0, s, cx, cy, size, fundo=None, est="g"):
    E.foco(c, t, t0, 0.4, lambda a: E.pilula(c, s, cx, cy, size, est, fundo=fundo, a=a, cor=BR))


def formula_em(c, t, t0, s, x, y, size, est="g", cor=TINTA, align="left"):
    E.formula_em(c, t, t0, s, x, y, size, est, cor, align)


def y_term(v, yb, h, vmin, vmax):
    """altura (pixel) do valor v num F.termometro de bulbo em yb e altura h"""
    base_t, topo = yb - 24, yb - h
    return base_t - (v - vmin) / (vmax - vmin) * (base_t - topo - 16)


def term(c, t, t0, cx, yb, h, v, vmin, vmax, escuro=False):
    """termômetro cujo nível v é controlado por quem chama (sobe do vmin em 0,8 s a partir de t0)"""
    if t < t0:
        return
    F.termometro(c, t, t0, cx, yb, h, lerp(vmin, v, ease_io(prog(t, t0, 0.8))) if v is not None else vmin, vmin, vmax, (), d=0.001, escuro=escuro)


def marca(c, t, t0, cx, y, valor, unid, size=44, cor=None, escuro=False, acima=False):
    """traço e medida à direita de um termômetro em cx, na altura y (acima=True: o texto fica sobre a linha tracejada)"""
    def fn(a):
        M.line(c, cx + 30, y, cx + 56, y, BR if escuro else TINTA, a, 4)
        F.medida(c, valor, unid, cx + 64, y - 14 if acima else y + size * 0.36, size, cor, a, escuro=escuro)
    E.foco(c, t, t0, 0.4, fn, sobe=6)


def tracejado(c, t, t0, x0, x1, y, cor=TINTA2, d=0.6, largura=4):
    if t >= t0:
        M.line(c, x0, y, x1, y, cor, 0.8, largura, dash=E.TRACO, progress=ease_io(prog(t, t0, d)))


def cota_v(c, t, t0, x, y0, y1, rotulo=None, cor=None, lado=-1, size=52, d=0.5, est="g"):
    """colchete vertical de y0 a y1 em x, aberto para o lado oposto a `lado`; rótulo (fórmula) do lado `lado`"""
    q = ep(t, t0, d)
    if q <= 0:
        return
    cor = cor or E.COR
    k = 22 * -lado
    ym = (y0 + y1) / 2
    a_, b_ = lerp(ym, y0, q), lerp(ym, y1, q)
    p = skia.Path()
    p.moveTo(x + k, a_); p.lineTo(x, a_); p.lineTo(x, b_); p.lineTo(x + k, b_)
    c.drawPath(p, M.paint(cor, q, stroke=6, cap_round=True))
    if rotulo:
        E.foco(c, t, t0 + 0.3, 0.4, lambda a: E.formula(c, rotulo, x + lado * 26, ym + size * 0.36, size, est, cor, a,
                                                        "right" if lado < 0 else "left"))


def particulas(c, t, x, y, w, h, agit, cor, a=1.0, n=(6, 4), r=17, borda=True):
    """caixa com partículas que tremem; agit = 0 (quase paradas) a 1 (muito agitadas)"""
    if a <= 0:
        return
    if borda:
        M.rrect(c, x, y, w, h, 26, E.mix(cor, "#FFFFFF", 0.86), a)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 26, 26), M.paint(cor, a, stroke=4))
    nc, nl = n
    c.save()
    c.clipRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x + 4, y + 4, w - 8, h - 8), 22, 22), True)
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


def xicara(c, x, y, s, a=1.0, t=0.0, vapor=True):
    """xícara de café com a base em (x, y); s = largura da boca"""
    if a <= 0:
        return
    w, h = s, s * 0.8
    p = skia.Path()
    p.moveTo(x - w / 2, y - h); p.lineTo(x + w / 2, y - h)
    p.cubicTo(x + w / 2, y - h * 0.2, x + w * 0.3, y, x, y)
    p.cubicTo(x - w * 0.3, y, x - w / 2, y - h * 0.2, x - w / 2, y - h)
    p.close()
    c.drawPath(p, M.paint("#FFFFFF", a))
    c.drawPath(p, M.paint(TINTA, a, stroke=6))
    c.drawOval(skia.Rect.MakeLTRB(x - w / 2 + 8, y - h - 14, x + w / 2 - 8, y - h + 14), M.paint("#6B3A1E", a))
    c.drawArc(skia.Rect.MakeXYWH(x + w * 0.38, y - h * 0.85, w * 0.3, h * 0.45), -80, 200, False, M.paint(TINTA, a, stroke=10))
    if vapor:
        for k in range(3):
            xx = x - w * 0.22 + k * w * 0.22
            pts = [(xx + 12 * math.sin(t * 3 + k + i * 0.5), y - h - 40 - i * 9) for i in range(14)]
            F.poli(c, pts, 1.0, E.COR, a * 0.75, 6)


def copo(c, x, y, w, h, a=1.0, gelo=True):
    """copo de água gelada com a base em (x, y)"""
    if a <= 0:
        return
    M.rrect(c, x - w / 2 + 6, y - h * 0.75, w - 12, h * 0.75 - 6, 10, AGUA, a * 0.55)
    if gelo:
        for dx, dy, g in ((-0.18, 0.62, 8), (0.12, 0.58, -12), (-0.02, 0.45, 20)):
            c.save(); c.translate(x + dx * w, y - dy * h); c.rotate(g)
            M.rrect(c, -w * 0.15, -w * 0.15, w * 0.3, w * 0.3, 8, GELO, a)
            c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(-w * 0.15, -w * 0.15, w * 0.3, w * 0.3), 8, 8), M.paint(FRIO, a, stroke=3))
            c.restore()
    p = skia.Path()
    p.moveTo(x - w / 2, y - h); p.lineTo(x - w / 2 + 8, y); p.lineTo(x + w / 2 - 8, y); p.lineTo(x + w / 2, y - h)
    c.drawPath(p, M.paint(TINTA, a, stroke=6))


def mao(c, x, y, s, a=1.0):
    """mão aberta de lado, com a palma virada para a esquerda; (x, y) = meio da palma"""
    if a <= 0:
        return
    pele, borda = "#E9B48C", "#9A6040"
    M.rrect(c, x - s * 0.35, y - s * 0.55, s * 0.7, s * 1.1, s * 0.3, pele, a)
    for k in range(4):
        yy = y - s * 0.5 + k * s * 0.27
        M.rrect(c, x - s * 0.95, yy, s * 0.75, s * 0.22, s * 0.11, pele, a)
    M.rrect(c, x - s * 0.1, y + s * 0.4, s * 0.5, s * 0.7, s * 0.2, pele, a)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x - s * 0.35, y - s * 0.55, s * 0.7, s * 1.1), s * 0.3, s * 0.3), M.paint(borda, a * 0.6, stroke=3))


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


# ---------------- gancho ----------------
def painel(c, x, y, w, h, texto, a=1.0, t=0.0):
    """painel de rua de LED: fundo escuro, número laranja brilhando"""
    if a <= 0:
        return
    M.rrect(c, x + w / 2 - 14, y + h, 28, 260, 6, TINTA2, a)
    M.rrect(c, x - 16, y - 16, w + 32, h + 32, 30, "#2A2A30", a)
    M.rrect(c, x, y, w, h, 20, "#0B0B10", a)
    for i in range(0, int(w), 22):
        for j in range(0, int(h), 22):
            c.drawCircle(x + 11 + i, y + 11 + j, 2.2, M.paint("#1C1C24", a))
    brilho = 0.85 + 0.15 * math.sin(t * 3)
    v, _, u = texto.partition(" ")
    F.medida(c, v, u, x + w / 2, y + h / 2 + 80, 220, E.COR, a * brilho, "center", cor_u=E.CLARO)


def b_gancho(c, t, C, b):
    def um():
        E.foco(c, t, C["s01.a"] + 0.2, 0.6, lambda a: painel(c, 1010, 250, 760, 340, "104 °F" if t >= C["s01.c"] else "104 °", a, t))
        E.frase(c, t, C["s01.a"], ps("painel da rua:", "i", 76), XE, 300, passo=0.12)
        E.foco(c, t, C["s01.b"], 0.5, lambda a: E.escreve(c, "104 graus", XE, 450, 120, "g", TINTA, a))
        E.frase(c, t, C["s01.b"] + 1.4, [("ninguém", "i", 70), ("ferve", "g", 66, ERRADO)], XE, 580)
        E.foco(c, t, C["s01.c"], 0.5, lambda a: F.medida(c, 104, "°F", XE, 790, 130, TINTA, a))
        E.foco(c, t, C["s01.d"], 0.5, lambda a: (E.escreve(c, "=", XE + 430, 790, 130, "g", TINTA2, a),
                                                 F.medida(c, 40, "°C", XE + 560, 790, 130, COR, a)))
        E.frase(c, t, C["s01.d"] + 1.2, ps("um dia quente, só isso", "i", 60, TINTA2), XE, 920, passo=0.12)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t < C["s02"]:
        return
    tb = C["s02.a"] + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1480, 540, 330 * ease_back(prog(t, tb, 0.8)), giro=12 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 88), XE, 280, passo=0.14)
    itens = (("s02.b", "temperatura ≠ calor"), ("s02.c", "°C   °F   K"))
    for i, (k, s) in enumerate(itens):
        y = 470 + i * 180
        E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, XE + 40, y - 30, 38, a=a), centro(c, str(i + 1), XE + 40, y - 8, 48, "g", BR, a)))
        E.frase(c, t, C[k] + 0.1, [(s, "g", 84, COR if i == 0 else TINTA)], XE + 110, y)


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    def prop(a, x, y):
        E.formula(c, "f{x}{6} = f{4}{3}", x - 40, y + 30, 64, "g", TINTA, a, "center")

    def kelvin(a, x, y):
        E.formula(c, "27 °C = 300 K", x - 90, y + 20, 50, "g", TINTA, a, "center")
    lembrete2(c, t, C, "s03", (("s03.b", "resolver uma", "proporção"), ("s03.c", "a escala", "Kelvin")), (prop, kelvin))


# ---------------- temperatura e calor ----------------
def b_calor(c, t, C, b):
    def s04():
        E.frase(c, t, C["s04"] + 1.4, [("temperatura", "g", 100, COR)], XE, 230)
        E.frase(c, t, C["s04.a"], ps("mede a", "i", 70) + [("agitação", "g", 66)] + ps("das partículas", "i", 70), XE, 340, passo=0.12)
        for k, x, cor, ag, nome, cola in (("s04.b", 230, E.COR, 1.0, "café quente", "muito agitadas"), ("s04.c", 1010, FRIO, 0.08, "água gelada", "quase paradas")):
            E.foco(c, t, C[k], 0.5, lambda a, x=x, cor=cor, ag=ag: particulas(c, t, x, 450, 680, 400, ag, cor, a))
            E.foco(c, t, C[k] + 0.3, 0.4, lambda a, x=x, nome=nome, cor=cor: E.escreve(c, nome, x, 940, 60, "g", cor, a))
            E.foco(c, t, C[k] + 0.6, 0.4, lambda a, x=x, cola=cola: E.escreve(c, cola, x + 400 if cola[0] == "m" else x + 420, 940, 46, "i", TINTA2, a))
    E.saida(c, t, C["s05"] - 0.1, s04)
    if C["s05"] <= t < C["s06"]:
        def s05():
            E.frase(c, t, C["s05.a"], [("calor", "g", 100, COR)], XE, 230)
            E.frase(c, t, C["s05.b"], ps("é a energia que", "i", 70) + [("passa", "g", 66)], XE, 340, passo=0.12)
            E.frase(c, t, C["s05.c"], [("do", "i", 66), ("mais quente", "g", 62, COR), ("→", "g", 62, TINTA2), ("para o", "i", 66), ("mais frio", "g", 62, FRIO)],
                    XE, 450, passo=0.15)
            E.foco(c, t, C["s05.c"] + 0.5, 0.6, lambda a: xicara(c, 760, 930, 300, a, t))
            E.foco(c, t, C["s05.d"], 0.5, lambda a: mao(c, 1340, 780, 150, a))
            seta_calor(c, t, C["s05.d"] + 0.5, (920, 790), (1170, 790), "calor", d=0.7, size=52)
            E.foco(c, t, C["s05.d"] + 0.3, 0.4, lambda a: E.escreve(c, "café", 690, 1010, 48, "i", TINTA2, a))
            E.foco(c, t, C["s05.d"] + 0.6, 0.4, lambda a: E.escreve(c, "sua mão", 1270, 1010, 48, "i", TINTA2, a))
        E.saida(c, t, C["s06"] - 0.1, s05)
    if C["s06"] <= t < C["s07"]:
        def s06():
            q = ease_io(prog(t, C["s06.a"], 2.2))
            ta, tf_ = lerp(80, 50, q), lerp(20, 50, q)
            ca, cb = E.mix(E.COR, "#B07AA0", q), E.mix(FRIO, "#B07AA0", q)
            E.foco(c, t, C["s06"], 0.5, lambda a: (F.bloco(c, 760, 600, 400, 300, None, ca, a), F.bloco(c, 1160, 600, 400, 300, None, cb, a)))
            E.foco(c, t, C["s06"] + 0.2, 0.4, lambda a: (F.medida(c, round(ta), "°C", 760, 625, 90, E.SOBRE, a, "center", cor_u=E.SOBRE),
                                                         F.medida(c, round(tf_), "°C", 1160, 625, 90, E.SOBRE, a, "center", cor_u=E.SOBRE)))
            seta_calor(c, t, C["s06"] + 0.4, (700, 380), (1220, 380), "calor", a=1 - q, size=50)
            if t >= C["s06"]:
                F.chao(c, 480, 1440, 750, ep(t, C["s06"], 0.5))
            E.frase(c, t, C["s06.a"] + 0.4, ps("temperaturas iguais:", "i", 64), XE, 880, passo=0.12)
            E.foco(c, t, C["s06.b"], 0.5, lambda a: E.pilula(c, "equilíbrio térmico", 1130, 860, 66, "g", fundo=E.COR, a=a))
            # o termômetro encostado no bloco da direita sobe até a mesma temperatura
            term(c, t, C["s06.c"] - 0.6, 1520, 740, 460, 50, 0, 100)
            if t >= C["s06.c"]:
                marca(c, t, C["s06.c"] + 0.6, 1520, y_term(50, 740, 460, 0, 100), 50, "°C", 48)
        E.saida(c, t, C["s07"] - 0.1, s06)
    if t < C["s07"]:
        return
    E.frase(c, t, C["s07"], ps("cuidado com a frase", "i", 70, TINTA2), XE, 230, passo=0.12)
    E.foco(c, t, C["s07.a"], 0.5, lambda a: E.escreve(c, "“esse corpo tem muito calor”", XE, 390, 80, "i", TINTA, a))
    if t >= C["s07.a"] + 1.6:
        E.risco(c, XE - 20, 400, XE + 1000, 330, t, C["s07.a"] + 1.6, largura=12)
    E.frase(c, t, C["s07.b"], ps("o corpo tem", "i", 80) + [("temperatura", "g", 80, CERTO)], XE, 600, passo=0.12)
    E.foco(c, t, C["s07.b"] + 0.8, 0.5, lambda a: E.selo(c, 1500, 570, 60, True, a))
    E.frase(c, t, C["s07.c"], [("calor", "g", 80, COR)] + ps("só existe", "i", 80) + [("passando", "g", 80)], XE, 780, passo=0.12)
    seta_calor(c, t, C["s07.c"] + 1.2, (XE + 60, 900), (XE + 760, 900), None, size=40)


# ---------------- escalas ----------------
YB, HT = 940, 660
ESC = (("Celsius", 880, -20, 120, (0, 100), "°C"), ("Fahrenheit", 1220, -4, 248, (32, 212), "°F"), ("Kelvin", 1560, 253, 393, (273, 373), "K"))


def b_escalas(c, t, C, b):
    yg, yf = y_term(0, YB, HT, -20, 120), y_term(100, YB, HT, -20, 120)

    def s08_09():
        E.frase(c, t, C["s08"] + 1.0, [("dois", "i", 76), ("pontos fixos", "g", 76, COR)], XE, 190)
        E.frase(c, t, C["s08.b"], ps("gelo derretendo", "i", 50), XE, yg + 16, passo=0.1)
        E.frase(c, t, C["s08.c"], ps("água fervendo", "i", 50), XE, yf + 16, passo=0.1)
        E.frase(c, t, C["s08.c"] + 0.8, ps("(nível do mar)", "i", 40, TINTA2), XE, yf + 70, passo=0.1)
        tracejado(c, t, C["s08.b"] + 0.3, 600, 1800, yg, FRIO)
        tracejado(c, t, C["s08.c"] + 0.3, 600, 1800, yf, E.COR)
        tks = (C["s08.d"], C["s09.a"], C["s09.d"])
        tms = ((C["s08.d"] + 0.6, C["s08.d"] + 1.0), (C["s09.b"], C["s09.c"]), (C["s09.e"], C["s09.e"] + 1.2))
        for (nome, cx, vmin, vmax, (g, f), u), tk, (tg, tf) in zip(ESC, tks, tms):
            term(c, t, tk, cx, YB, HT, None, vmin, vmax)
            E.foco(c, t, tk, 0.4, lambda a, nome=nome, cx=cx: centro(c, nome, cx + 40, 200, 46, "g", TINTA, a))
            marca(c, t, tg, cx, yg, g, u, 44, acima=True)
            marca(c, t, tf, cx, yf, f, u, 44, acima=True)
        pilula_em(c, t, C["s09.d"] + 0.4, "SI", 1600, 130, 40, E.COR)
    E.saida(c, t, C["s10"] - 0.1, s08_09)
    if t < C["s10"]:
        return
    E.frase(c, t, C["s10.a"], [("zero", "g", 100, COR), ("absoluto", "g", 100, COR)], XE, 260, passo=0.15)
    E.frase(c, t, C["s10.a"] + 0.9, ps("a menor agitação possível", "i", 60), XE, 360, passo=0.1)
    E.foco(c, t, C["s10.a"] + 1.2, 0.5, lambda a: particulas(c, t, XE, 420, 520, 200, 0.0, FRIO, a, n=(7, 3), r=14))
    E.foco(c, t, C["s10.b"], 0.5, lambda a: (F.medida(c, 0, "K", XE, 750, 96, COR, a), E.escreve(c, "≈", XE + 200, 750, 96, "g", TINTA2, a),
                                             F.medida(c, "−273", "°C", XE + 300, 750, 96, TINTA, a)))
    yb, h = 950, 760
    term(c, t, C["s10.a"], 1450, yb, h, 300, 0, 400)
    for v, tv in ((0, C["s10.b"]), (273, C["s10.b"] + 0.6), (373, C["s10.b"] + 0.9)):
        marca(c, t, tv, 1450, y_term(v, yb, h, 0, 400), v, "K", 44)
    pilula_em(c, t, C["s10.c"], "sem valor negativo", XE + 250, 840, 46, FRIO, "b")
    E.foco(c, t, C["s10.d"], 0.5, lambda a: F.medida(c, 300, "K", XE, 990, 84, CERTO, a))
    E.foco(c, t, C["s10.d"] + 0.8, 0.5, lambda a: F.medida(c, 300, "°K", XE + 420, 990, 84, ERRADO, a))
    if t >= C["s10.d"] + 1.3:
        E.risco(c, XE + 400, 1005, XE + 720, 925, t, C["s10.d"] + 1.3, largura=10)


# ---------------- a fórmula ----------------
def b_formula(c, t, C, b):
    yb, h = 960, 640
    ESC2 = (("C", 1240, -20, 120, 0, 100, 25, "°C"), ("F", 1620, -4, 248, 32, 212, 77, "°F"))
    yg, yf, yq = y_term(0, yb, h, -20, 120), y_term(100, yb, h, -20, 120), y_term(25, yb, h, -20, 120)

    def s11_12():
        E.frase(c, t, C["s11"] + 1.4, ps("de uma escala para outra:", "i", 64), XE, 200, passo=0.1)
        E.frase(c, t, C["s11.a"], ps("uma", "i", 90) + [("proporção", "g", 90, COR)], XE, 320)
        tracejado(c, t, C["s11.a"] + 0.4, 1060, 1860, yg, FRIO)
        tracejado(c, t, C["s11.a"] + 0.4, 1060, 1860, yf, E.COR)
        for i, (nome, cx, vmin, vmax, g, f, q, u) in enumerate(ESC2):
            tq = C["s11.b"] if i == 0 else C["s11.c"]
            term(c, t, C["s11.a"] + 0.2 * i, cx, yb, h, q if t >= tq else vmin, vmin, vmax)
            E.foco(c, t, C["s11.a"] + 0.2 * i, 0.4, lambda a, u=u, cx=cx: centro(c, u, cx, 230, 60, "g", TINTA, a))
            marca(c, t, C["s11.a"] + 0.5, cx, yg, g, u, 40, acima=True)
            marca(c, t, C["s11.a"] + 0.5, cx, yf, f, u, 40, acima=True)
            marca(c, t, tq + 0.8, cx, yq, q, u, 40, COR)
            cota_v(c, t, tq + 0.4, cx - 50, yg, yq, "f{1}{4}", lado=-1, size=50)
        cota_v(c, t, C["s12.a"], 1240 - 130, yg, yf, "100", TINTA, lado=-1, size=50)
        cota_v(c, t, C["s12.b"], 1620 - 130, yg, yf, "180", TINTA, lado=-1, size=50)
        E.foco(c, t, C["s12.b"] + 0.3, 0.4, lambda a: E.formula(c, "212 − 32 = 180", XE, 520, 56, "b", TINTA2, a))
        formula_em(c, t, C["s12.c"], "f{C}{100} = f{F − 32}{180}", XE, 760, 104)
    E.saida(c, t, C["s13"] - 0.1, s11_12)
    if t < C["s13"]:
        return
    E.foco(c, t, C["s13.a"], 0.5, lambda a: E.formula(c, "100 ÷ 20 = 5", XE, 200, 60, "b", TINTA2, a))
    E.foco(c, t, C["s13.a"] + 0.5, 0.5, lambda a: E.formula(c, "180 ÷ 20 = 9", XE + 520, 200, 60, "b", TINTA2, a))
    formula_em(c, t, C["s13.b"], "f{C}{5} = f{F − 32}{9}", XE, 440, 130)
    w0 = E.formula(None, "f{C}{5} = f{F − 32}{9}", 0, 0, 130, a=0)
    formula_em(c, t, C["s13.e"], " = f{K − 273}{5}", XE + w0, 440, 130, cor=TINTA)
    F.formula_legenda(c, t, C["s13.b"], "", [("C", "temperatura em Celsius", "°C"), ("F", "temperatura em Fahrenheit", "°F"),
                                             ("K", "temperatura em Kelvin", "K")], XE, 470, size=130, tl=[C["s13.c"], C["s13.d"], C["s13.e"] + 0.5], size_l=56)


# ---------------- exemplos ----------------
def passos(c, t, linhas, x, y0, dy=125, size=80):
    """contas empilhadas: linhas = [(t0, fórmula, cor)]"""
    for i, (ti, s, cor) in enumerate(linhas):
        formula_em(c, t, ti, s, x, y0 + i * dy, size, cor=cor)


def b_exemplos(c, t, C, b):
    def s14():
        E.foco(c, t, C["s14.a"], 0.5, lambda a: (F.medida(c, 104, "°F", XE, 230, 110, TINTA, a), E.escreve(c, "→  ? °C", XE + 420, 230, 90, "g", COR, a)))
        passos(c, t, [(C["s14.b"], "104 − 32 = 72", TINTA), (C["s14.c"], "72 ÷ 9 = 8", TINTA), (C["s14.d"], "f{C}{5} = 8", TINTA),
                      (C["s14.d"] + 1.4, "C = 5 · 8", TINTA2)], XE, 420, 150, 84)
        E.foco(c, t, C["s14.a"] + 0.4, 0.5, lambda a: painel(c, 1180, 210, 560, 250, "104 °F", a, t))
        bola_txt(c, t, C["s14.e"], "40 °C", 1460, 780, 150, 84)
    E.saida(c, t, C["s15"] - 0.1, s14)
    if t < C["s15"]:
        return
    E.foco(c, t, C["s15.a"], 0.5, lambda a: (F.medida(c, 25, "°C", XE, 230, 110, TINTA, a), E.escreve(c, "→  ? °F", XE + 380, 230, 90, "g", COR, a)))
    passos(c, t, [(C["s15.b"], "25 ÷ 5 = 5", TINTA), (C["s15.b"] + 1.6, "f{F − 32}{9} = 5", TINTA), (C["s15.c"], "F − 32 = 5 · 9 = 45", TINTA),
                  (C["s15.d"], "F = 45 + 32", TINTA2)], XE, 420, 150, 80)
    bola_txt(c, t, C["s15.d"] + 0.6, "77 °F", 1460, 500, 150, 84)
    E.foco(c, t, C["s15.e"], 0.5, lambda a: E.formula(c, "25 + 273 = 298 K", 1460, 870, 70, "g", TINTA, a, "center"))
    pilula_em(c, t, C["s15.e"] + 0.6, "Kelvin: some 273", 1460, 970, 44, E.COR, "b")


# ---------------- variação ----------------
def b_variacao(c, t, C, b):
    yb, h, vmin, vmax = 960, 700, 0, 40
    y20, y30 = y_term(20, yb, h, vmin, vmax), y_term(30, yb, h, vmin, vmax)
    v = lerp(20, 30, ease_io(prog(t, C["s16.a"] + 0.4, 1.4)))
    term(c, t, C["s16"], 1500, yb, h, v, vmin, vmax)
    marca(c, t, C["s16"] + 0.6, 1500, y20, 20, "°C", 44)
    marca(c, t, C["s16.a"] + 1.6, 1500, y30, 30, "°C", 44, COR)
    cota_v(c, t, C["s16.a"] + 1.8, 1440, y30, y20, "ΔC = 10 °C", lado=-1, size=54)

    def s16():
        E.frase(c, t, C["s16.a"], ps("subiu", "i", 84) + [("10 °C", "g", 84, COR)], XE, 240)
        E.frase(c, t, C["s16.a"] + 1.4, ps("quanto em", "i", 84) + [("°F?", "g", 84)], XE, 360)
        E.frase(c, t, C["s16.b"], ps("não é temperatura:", "i", 64, TINTA2) + [("variação", "g", 64, COR)], XE, 520, passo=0.12)
        E.foco(c, t, C["s16.c"], 0.6, lambda a: E.escreve(c, "Δ", XE, 860, 300, "g", COR, a))
        E.frase(c, t, C["s16.c"] + 0.5, ps("delta =", "i", 64) + ps("variação", "g", 60), XE + 260, 780, passo=0.12)
    E.saida(c, t, C["s17"] - 0.1, s16)
    if t < C["s17"]:
        return
    E.foco(c, t, C["s17.a"], 0.5, lambda a: E.formula(c, "f{C}{5} = f{F − 32}{9}", XE, 250, 80, "g", TINTA2, a))
    xr = XE + E.formula(None, "f{C}{5} = f{F ", 0, 0, 80, a=0)
    if t >= C["s17.a"] + 0.8:
        E.risco(c, xr - 10, 225, xr + 150, 160, t, C["s17.a"] + 0.8, largura=10)
    E.frase(c, t, C["s17.a"] + 1.2, ps("o 32 some", "i", 56, ERRADO), XE + 500, 240, passo=0.1)
    formula_em(c, t, C["s17.b"], "f{ΔC}{5} = f{ΔF}{9}", XE, 520, 120, cor=TINTA)
    passos(c, t, [(C["s17.c"], "10 ÷ 5 = 2", TINTA), (C["s17.d"], "2 · 9 = 18", TINTA)], XE, 720, 120, 76)
    bola_txt(c, t, C["s17.e"], "18 °F", 900, 760, 110, 64)
    E.foco(c, t, C["s17.f"], 0.5, lambda a: E.formula(c, "ΔK = ΔC = 10 K", XE, 990, 64, "g", COR, a))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    def s18():
        E.frase(c, t, C["s18"], [("cuidado", "g", 96, ERRADO)], XE, 210)
        E.frase(c, t, C["s18.a"], ps("a fórmula da temperatura", "i", 66) + ps("numa variação", "g", 62), XE, 340, passo=0.1)
        E.frase(c, t, C["s18.a"] + 2.0, ps("subiu", "i", 76) + [("10 °C", "g", 76, COR)], XE, 500)
        formula_em(c, t, C["s18.b"], "f{10}{5} = f{F − 32}{9}", XE, 700, 100)
        E.foco(c, t, C["s18.c"], 0.5, lambda a: F.medida(c, "50", "°F?", XE, 900, 110, ERRADO, a))
        if t >= C["s18.c"] + 1.0:
            E.risco(c, XE - 20, 920, XE + 380, 820, t, C["s18.c"] + 1.0, largura=12)
    E.saida(c, t, C["s19"] - 0.1, s18)
    if t < C["s19"]:
        return
    yb, h = 960, 640
    for i, (cx, vmin, vmax, a0, a1, u, tk) in enumerate(((1100, 0, 40, 20, 30, "°C", C["s19.a"]), (1560, 32, 104, 68, 86, "°F", C["s19.b"]))):
        v = lerp(a0, a1, ease_io(prog(t, tk + 0.8, 1.2)))
        term(c, t, tk, cx, yb, h, v, vmin, vmax)
        y0, y1 = y_term(a0, yb, h, vmin, vmax), y_term(a1, yb, h, vmin, vmax)
        marca(c, t, tk + 0.4, cx, y0, a0, u, 44)
        marca(c, t, tk + 1.6, cx, y1, a1, u, 44, COR)
        cota_v(c, t, (C["s19.a"] + 2.0) if i == 0 else C["s19.c"], cx - 60, y1, y0, "10" if i == 0 else "18", lado=-1, size=64)
    E.frase(c, t, C["s19"] + 0.2, ps("um dia que", "i", 70) + [("esquenta", "g", 70, COR)], XE, 230)
    E.frase(c, t, C["s19.c"] + 0.4, [("18,", "g", 110, CERTO)], XE, 560)
    E.frase(c, t, C["s19.c"] + 1.0, ps("não", "i", 90) + [("50", "g", 100, ERRADO)], XE, 720)
    E.foco(c, t, C["s19.c"] + 1.4, 0.5, lambda a: E.selo(c, XE + 470, 530, 60, True, a))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    cs, fs = (0, 5, 10, 15, 20, 25), (32, 41, 50, 59, 68, 77)
    assert all(f_de_c(a) == b_ for a, b_ in zip(cs, fs))
    xs = [460 + i * 240 for i in range(6)]
    yc, yf = 460, 770

    def s20():
        E.frase(c, t, C["s20.a"], ps("conte de", "i", 84, CLARO) + [("5 em 5", "g", 90, BR)], W / 2, 180, "center", 0.15)
        E.foco(c, t, C["s20.b"], 0.4, lambda a: (E.escreve(c, "°C", 190, yc + 20, 64, "g", CLARO, a), E.escreve(c, "°F", 190, yf + 20, 64, "g", CLARO, a)))
        # tempo de cada coluna: a 1ª e a 2ª em s20.b/c, as outras nos saltos (s20.d)
        tcol = [C["s20.c"], C["s20.b"] + 0.4] + [C["s20.d"] + 0.5 * k for k in range(1, 5)]
        for i, (a_, f_) in enumerate(zip(cs, fs)):
            E.foco(c, t, tcol[i], 0.4, lambda q, i=i, a_=a_, f_=f_: (centro(c, str(a_), xs[i], yc + 24, 76, "g", BR, q),
                                                                     centro(c, str(f_), xs[i], yf + 24, 76, "g", BR, q)))
            if i:
                E.salto(c, t, tcol[i], xs[i - 1] + 40, xs[i] - 40, yc - 60, 70, E.COR, "+5", 0.5, 6, 44)
                E.salto(c, t, tcol[i] + 0.15, xs[i - 1] + 40, xs[i] - 40, yf - 60, 70, CLARO, "+9", 0.5, 6, 44)
        q = ep(t, C["s20.c"], 0.4)
        if q > 0:
            c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(xs[0] - 90, yc - 60, 180, yf - yc + 120), 30, 30), M.paint(E.COR, q, stroke=6))
        E.foco(c, t, C["s20.d"] + 0.3, 0.4, lambda a: E.pilula(c, "5 saltos", xs[5], yf + 130, 46, "g", fundo=E.COR, a=a))
        E.foco(c, t, C["s20.e"], 0.5, lambda a: centro(c, "5 · 9 = 45", 760, 990, 76, "g", CLARO, a))
        E.foco(c, t, C["s20.f"], 0.5, lambda a: centro(c, "32 + 45 = 77", 1340, 990, 76, "g", BR, a))
    E.saida(c, t, C["s21"] - 0.1, s20)
    if t < C["s21"]:
        return
    E.frase(c, t, C["s21.a"], ps("é a proporção de", "i", 76, CLARO) + [("5", "g", 84, BR), ("para", "i", 76, CLARO), ("9", "g", 84, BR)], W / 2, 220, "center", 0.12)
    E.frase(c, t, C["s21.b"] - 0.6, [("bônus:", "i", 64, CLARO)], W / 2, 410, "center")
    E.foco(c, t, C["s21.b"], 0.5, lambda a: (F.medida(c, "−40", "°C", W / 2 - 80, 560, 120, BR, a, "right", escuro=True),
                                             centro(c, "=", W / 2, 555, 120, "g", CLARO, a),
                                             F.medida(c, "−40", "°F", W / 2 + 80, 560, 120, BR, a, "left", escuro=True)))
    E.frase(c, t, C["s21.c"], [("não", "g", 64, ERRADO), ("compensa:", "i", 66, CLARO)] + [("37 °C", "g", 64, BR)] + [("→", "g", 60, CLARO)] + ps("use a fórmula", "i", 66, CLARO),
            W / 2, 830, "center", 0.12)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s22"], ps("hora de testar", "i", 72, COR), XE, 200)
    E.frase(c, t, C["s22.a"], ps("termômetro da rua:", "i", 70), XE, 330, passo=0.1)
    E.foco(c, t, C["s22.a"] + 0.6, 0.5, lambda a: F.medida(c, 59, "°F", XE + 640, 330, 100, COR, a))
    E.frase(c, t, C["s22.b"], [("a)", "g", 66, COR)] + ps("quanto em", "i", 70) + [("°C?", "g", 70)], XE, 480, passo=0.12)
    E.frase(c, t, C["s22.c"], ps("à tarde, sobe", "i", 70) + [("18 °F", "g", 70, COR)], XE, 640, passo=0.12)
    E.frase(c, t, C["s22.d"], [("b)", "g", 66, COR)] + ps("subiu quanto em", "i", 70) + [("°C", "g", 70), ("e", "i", 70), ("K?", "g", 70)], XE, 790, passo=0.12)
    if t < C["s23"]:
        term(c, t, C["s22.a"], 1560, 960, 640, 59, 32, 104)
        marca(c, t, C["s22.a"] + 0.8, 1560, y_term(59, 960, 640, 32, 104), 59, "°F", 48, COR)
    else:
        E.relogio(c, t, C["s23.a"], cx=1500, cy=440, r=200)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    def s24():
        E.frase(c, t, C["s24"], [("a)", "g", 76, COR)], XE, 220)
        passos(c, t, [(C["s24.a"], "59 − 32 = 27", TINTA), (C["s24.b"], "27 ÷ 9 = 3", TINTA), (C["s24.b"] + 1.6, "f{C}{5} = 3  →  C = 15", TINTA)],
               XE, 400, 160, 84)
        bola_txt(c, t, C["s24.c"], "15 °C", 1480, 600, 150, 84, CERTO)
    E.saida(c, t, C["s25"] - 0.1, s24)
    if t < C["s25"]:
        return
    E.frase(c, t, C["s25"], [("b)", "g", 76, COR)] + ps("variação: o 32 não entra", "i", 66), XE, 220, passo=0.1)
    passos(c, t, [(C["s25.b"], "f{18}{9} = 2", TINTA), (C["s25.c"], "2 · 5 = 10", TINTA)], XE, 450, 200, 90)
    bola_txt(c, t, C["s25.d"], "10 °C", 1180, 600, 130, 76, CERTO)
    bola_txt(c, t, C["s25.e"], "10 K", 1560, 600, 130, 76, CERTO)


# ---------------- fechamento ----------------
def ponte(c, t, t0, x, y, w, a=1.0):
    """ponte vista de lado: dois tabuleiros com a fresta (junta de dilatação) no meio"""
    q = ep(t, t0, 0.6)
    if q <= 0:
        return
    for k, (x0, x1) in enumerate(((x, x + w / 2 - 10), (x + w / 2 + 10, x + w))):
        M.rrect(c, x0, y, x1 - x0, 40, 6, TINTA2, q)
    for px in (x + w * 0.2, x + w * 0.8):
        M.rrect(c, px - 22, y + 40, 44, 200, 6, CINZA, q)
    c.drawCircle(x + w / 2, y + 20, 46 + 4 * math.sin(t * 4), M.paint(E.COR, q * ep(t, t0 + 0.6, 0.4), stroke=6))


def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s26"], [("resumindo", "i", 92, COR)], W / 2, 180, "center")
        itens = (("s26.a", [("temperatura", "g", 66), ("=", "g", 66, TINTA2), ("agitação;", "i", 70), ("calor", "g", 66, COR), ("=", "g", 66, TINTA2), ("passando", "i", 70)]),
                 ("s26.b", [("converter:", "g", 66), ("f{C}{5} = f{F − 32}{9}", "f", 66)]),
                 ("s26.c", [("variação:", "g", 66), ("o", "i", 70), ("32", "g", 66, COR), ("sai", "i", 70)]))
        for i, (k, partes) in enumerate(itens):
            y = 380 + i * 210
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 260, y - 26, 52, a=a), centro(c, str(i + 1), 260, y - 4, 60, "g", BR, a)))
            if partes[1][1] == "f":
                E.frase(c, t, C[k] + 0.1, [partes[0]], 360, y)
                formula_em(c, t, C[k] + 0.5, partes[1][0], 360 + E.larg(partes[0][0], "g", 66) + 40, y, 76)
            else:
                E.frase(c, t, C[k] + 0.1, partes, 360, y, passo=0.12)
    E.saida(c, t, C["s27"] - 0.1, resumo)
    if t < C["s27"]:
        return
    E.frase(c, t, C["s27"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C["s27.a"], [("Dilatação", "g", 130, COR)], XE, 410)
    E.frase(c, t, C["s27.a"] + 0.5, [("térmica", "g", 130, COR)], XE, 550)
    ponte(c, t, C["s27.b"], 260, 720, 900)
    E.foco(c, t, C["s27.b"] + 0.9, 0.4, lambda a: E.escreve(c, "a fresta da ponte", 560, 680, 44, "i", TINTA2, a))
    E.foco(c, t, C["s27.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 420, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s27.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(720, 445, p), ep(t, C["s27.c"] + 0.2, 0.4))
    E.frase(c, t, C["s27.d"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1570, 990, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, calor=b_calor, escalas=b_escalas, formula=b_formula, exemplos=b_exemplos,
              variacao=b_variacao, erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
