"""Visual — Estudativo · FIS-CIN-004: referencial, posição e deslocamento.

Segue a LINGUAGEM VISUAL DA FÍSICA do cabeçalho de FIS-CIN-001 (peças em _ferramentas/fisica.py, importado como F).
Nesta aula: a POSIÇÃO é um ponto na pista numerada (F.pista), o carro anda com F.movel; o DESLOCAMENTO é uma seta
petróleo (F.VEL) do começo ao fim, com "Δs = ..."; a DISTÂNCIA PERCORRIDA são as setas de cada trecho, empilhadas, em
cinza-tinta, somadas sem sinal. Ônibus, pessoa, hodômetro e pista de atletismo desenhados aqui.
Todo instante vem de C[...] (marcadores do roteiro)."""
import math

import editorial as E
import fisica as F
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Física", "Cinemática")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_FIS-CIN-004_referencial_posicao_deslocamento.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("referencial", "posicao", "distancia", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"

# todas as contas da aula
assert 80 - 30 == 50 and 30 - 80 == -50 and (80 - 30) + (80 - 50) == 50 + 30 == 80 and 50 - 30 == 20
assert 60 - (-20) == 80 and 60 - 40 == 20 and 80 + 20 == 100 and 40 - (-20) == 40 + 20 == 60


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças gerais (copiadas entre as aulas FIS-CIN) ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


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


def lembrete(c, t, C, cena, itens, desenhos=None):
    """'você precisa de N coisas': itens = [(cue, linha fina, linha forte)]; desenhos[i](a, x, y) à direita de cada caixa"""
    n = len(itens)
    E.frase(c, t, C[cena] + 0.2, ps("você precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C[cena + ".a"], 0.5, lambda a: E.escreve(c, str(n), XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C[cena + ".a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 820, 1000
    h, gap, s1 = (230, 290, 58) if n == 2 else (196, 236, 52)
    y0 = 520 - (h + gap * (n - 1)) / 2
    for i, (k, l1, l2) in enumerate(itens):
        y = y0 + i * gap
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, h, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", s1)], x + 44, y + h * 0.4)
        E.frase(c, t, C[k] + 0.3, [(l2, "g", s1, COR)], x + 44, y + h * 0.74)
        if desenhos:
            E.foco(c, t, C[k] + 0.6, 0.5, lambda a, i=i, y=y: desenhos[i](a, x + w - 150, y + h / 2))
    ult = itens[-1][0]
    E.frase(c, t, lerp(C[ult], C[cena + ".end"], 0.6), ps("faltou alguma?", "i", 56, COR) + ps("procure no canal", "i", 56), 820, 990, "left", 0.12)


def promessa(c, t, C, cena, itens, titulo="até o fim da aula"):
    """gancho: a órbita à direita e a lista numerada; itens = [(cue, texto, atraso)]"""
    tb = C[cena + ".a"] + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1480, 540, 330 * ease_back(prog(t, tb, 0.8)), giro=12 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, C[cena + ".a"], ps(titulo, "i", 88), XE, 280, passo=0.14)
    for i, (k, s, dt) in enumerate(itens):
        y = 450 + i * 160
        E.foco(c, t, C[k] + dt, 0.5, lambda a, i=i, y=y: (E.bola(c, XE + 40, y - 30, 38, a=a),
                                                        centro(c, str(i + 1), XE + 40, y - 8, 48, "g", BR, a)))
        E.frase(c, t, C[k] + dt + 0.1, [(s, "g", 80, COR if i == 0 else TINTA)], XE + 110, y)


def fim_inscreva(c, t, C, cena, k_insc, k_bons):
    E.foco(c, t, C[k_insc], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 420, 76, estilo="g", a=a))
    p = ease_io(prog(t, C[k_insc] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(720, 445, p), ep(t, C[k_insc] + 0.2, 0.4))
    E.frase(c, t, C[k_bons], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1570, 990, "center")


def resumo(c, t, C, cena, itens):
    """resumo numerado: itens = [(cue, partes de E.frase)]"""
    E.frase(c, t, C[cena], [("resumindo", "i", 92, COR)], W / 2, 180, "center")
    for i, (k, partes) in enumerate(itens):
        y = 360 + i * 190
        E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 300, y - 26, 52, a=a), centro(c, str(i + 1), 300, y - 4, 60, "g", BR, a)))
        E.frase(c, t, C[k] + 0.1, partes, 400, y, passo=0.12)


# ---------------- peças desta aula ----------------
def onibus(c, x, y, w=520, a=1.0):
    """ônibus de lado: (x, y) = canto de baixo à esquerda (rodas tocando y)"""
    if a <= 0:
        return
    h = w * 0.36
    r = w * 0.07
    M.rrect(c, x, y - h - r * 0.8, w, h, 22, E.COR, a)
    for k in range(5):
        M.rrect(c, x + 30 + k * (w - 60) / 5, y - h - r * 0.8 + 22, (w - 60) / 5 - 14, h * 0.4, 8, E.mix(E.COR, BR, 0.75), a)
    for wx in (x + w * 0.2, x + w * 0.8):
        c.drawCircle(wx, y - r, r, M.paint("#1B1B20", a))
        c.drawCircle(wx, y - r, r * 0.45, M.paint("#9A9AA2", a))


def pessoa(c, x, y, h=120, a=1.0, cor=TINTA):
    """bonequinho de pé com os pés em y"""
    if a <= 0:
        return
    c.drawCircle(x, y - h * 0.86, h * 0.13, M.paint(cor, a))
    M.line(c, x, y - h * 0.72, x, y - h * 0.35, cor, a, h * 0.07)
    M.line(c, x, y - h * 0.35, x - h * 0.16, y, cor, a, h * 0.07)
    M.line(c, x, y - h * 0.35, x + h * 0.16, y, cor, a, h * 0.07)
    M.line(c, x - h * 0.2, y - h * 0.55, x + h * 0.2, y - h * 0.55, cor, a, h * 0.07)


def cota(c, x0, x1, y, txt, a, cor=TINTA2, size=44):
    """linha de medida com pontas e rótulo em cima"""
    if a <= 0 or abs(x1 - x0) < 4:
        return
    M.line(c, x0, y, x1, y, cor, a, 3)
    for xx in (x0, x1):
        M.line(c, xx, y - 14, xx, y + 14, cor, a, 3)
    centro(c, txt, (x0 + x1) / 2, y - 20, size, "i", cor, a)


def hodometro(c, cx, cy, km, a=1.0):
    if a <= 0:
        return
    M.rrect(c, cx - 230, cy - 60, 460, 120, 20, "#1B1B20", a)
    s = f"{int(km):06d}"
    for i, ch in enumerate(s):
        x = cx - 200 + i * 62
        M.rrect(c, x, cy - 44, 54, 88, 8, "#2E2E36", a)
        centro(c, ch, x + 27, cy + 22, 62, "g", E.COR if i >= 4 else BR, a)
    centro(c, "km", cx + 300, cy + 18, 48, "b", TINTA2, a)


def trecho(c, t, t0, vx, v0, v1, y, rot, cor=TINTA2, lado=1, size=50):
    F.vetor(c, t, t0, (vx(v0), y), (vx(v1), y), None, rot, cor, 9, lado=lado, size=size)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def um():
        yb = 860
        F.chao(c, 80, 1840, yb, ep(t, C["s01"], 0.5)) if t >= C["s01"] else None
        x = lerp(500, 900, ease_io(prog(t, C["s01.a"], 6.0)))
        E.foco(c, t, C["s01.a"], 0.5, lambda a: onibus(c, x, yb, 620, a))
        E.foco(c, t, C["s01.a"] + 0.4, 0.4, lambda a: pessoa(c, x + 330, yb - 90, 110, a, BR))
        E.foco(c, t, C["s01.a"] + 0.8, 0.4, lambda a: pessoa(c, 1620, yb, 150, a))
        E.frase(c, t, C["s01.a"], ps("você no ônibus", "i", 70), XE, 220, passo=0.12)
        E.foco(c, t, C["s01.b"], 0.4, lambda a: E.pilula(c, "parado?", 330, 360, 64, "g", fundo=TINTA, a=a))
        E.foco(c, t, C["s01.c"], 0.4, lambda a: E.pilula(c, "em movimento?", 770, 360, 64, "g", fundo=TINTA, a=a))
        E.foco(c, t, C["s01.d"], 0.4, lambda a: E.pilula(c, "as duas certas", 1500, 220, 64, "g", fundo=CERTO, a=a))
        E.frase(c, t, C["s01.e"], ps("depende de", "i", 72) + [("quem olha", "g", 72, COR)], 1500, 360, "center", 0.12)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t >= C["s02"]:
        promessa(c, t, C, "s02", (("s02.a", "quem está parado", 1.6), ("s02.b", "distância percorrida", 0), ("s02.c", "deslocamento", 0)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    def seta_p(a, x, y):
        F.seta(c, x - 90, y + 30, x + 70, y - 30, F.VEL, a, 9)

    def conta(a, x, y):
        E.formula(c, "30 − 80 = −50", x - 30, y + 20, 48, "g", TINTA, a, "center")
    lembrete(c, t, C, "s03", (("s03.b", "grandeza vetorial:", "direção e sentido"), ("s03.c", "inteiros:", "negativos também")), (seta_p, conta))


# ---------------- referencial ----------------
def b_referencial(c, t, C, b):
    def s04():
        yb = 880
        F.chao(c, 80, 1840, yb, 1.0)
        x = lerp(200, 980, ease_io(prog(t, C["s04"], max(1.0, C["s05"] - C["s04"] - 0.3))))
        onibus(c, x, yb, 620)
        mx, px = x + 520, x + 300  # motorista e passageiro
        pessoa(c, mx, yb - 90, 110, 1.0, BR)
        pessoa(c, px, yb - 90, 110, 1.0, BR)
        pessoa(c, 1720, yb, 150)
        E.frase(c, t, C["s04"], [("para", "i", 66), ("o", "i", 66), ("motorista:", "i", 66), ("parado", "g", 66, COR)], XE, 220, passo=0.12)
        q = ep(t, C["s04.b"], 0.4)
        cota(c, px, mx, yb - 290, "não muda", q, COR)
        E.frase(c, t, C["s04.c"], [("para", "i", 66), ("a", "i", 66), ("calçada:", "i", 66), ("em movimento", "g", 66, COR)], XE, 330, passo=0.12)
        q2 = ep(t, C["s04.d"], 0.4)
        cota(c, px, 1720, yb + 70, "muda", q2, ERRADO)
    E.saida(c, t, C["s05"] - 0.1, s04)
    if t < C["s05"]:
        return
    E.frase(c, t, C["s05.a"], [("referencial", "g", 120, COR)], XE, 260)
    E.frase(c, t, C["s05.a"] + 0.6, ps("= quem olha, a base para medir", "i", 62, TINTA2), XE, 360, passo=0.1)
    E.frase(c, t, C["s05.b"], [("movimento:", "g", 64)] + ps("a posição muda com o tempo", "i", 66), XE, 520, passo=0.1)
    E.frase(c, t, C["s05.c"], [("repouso:", "g", 64)] + ps("a posição não muda", "i", 66), XE, 630, passo=0.1)
    E.frase(c, t, C["s05.d"], ps("parado em relação", "i", 76) + [("a quê?", "g", 76, COR)], XE, 820, passo=0.12)
    tb = lerp(C["s05.d"], C["s05.end"], 0.55)
    E.foco(c, t, tb, 0.6, lambda a: (E.bola(c, 1600, 800, 120, "#2F7BD0", a), E.arco(c, 1600, 800, 170, 200 + 40 * t, 120, TINTA2, 6, a)))


# ---------------- posição ----------------
def b_posicao(c, t, C, b):
    y = 640
    vx = F.pista(c, t, C["s06.a"], 260, 1660, y, -20, 80, list(range(-20, 81, 10)), "km", size=36)
    q = ep(t, C["s06.b"], 0.5)
    if q > 0:
        c.drawCircle(vx(0), y, 16, M.paint(E.COR, q))
    pilula_em(c, t, C["s06.b"] + 0.2, "origem", vx(0), y - 240, 44, TINTA)
    if t >= C["s06.b"] + 0.2:
        M.line(c, vx(0), y - 210, vx(0), y - 20, TINTA, 0.6 * ep(t, C["s06.b"] + 0.2, 0.4), 3, dash=E.TRACO)
    E.foco(c, t, C["s06.d"], 0.5, lambda a: F.carrinho(c, vx(30), y, 200, a=a))
    E.foco(c, t, C["s06.d"] + 0.4, 0.4, lambda a: E.pilula(c, "km 30", vx(30), y - 200, 44, "g", fundo=E.COR, a=a))
    qn = ep(t, C["s06.e"], 0.5)
    if qn > 0:
        M.rrect(c, vx(-20) - 40, y - 26, vx(0) - vx(-20) + 40, 52, 26, F.NEG, 0.22 * qn)
        centro(c, "negativas", (vx(-20) + vx(0)) / 2, y + 150, 46, "i", F.NEG, qn)
    E.frase(c, t, C["s06.a"], [("posição", "g", 84, COR)] + ps("= um número na reta", "i", 70), XE, 230, passo=0.12)
    E.frase(c, t, C["s06.c"], ps("onde o corpo está, com a unidade", "i", 58, TINTA2), XE, 330, passo=0.1)
    E.foco(c, t, C["s06.f"], 0.5, lambda a: E.formula(c, "s = 30 km", W / 2, 940, 110, "g", COR, a, "center"))


# ---------------- deslocamento ----------------
def b_deslocamento(c, t, C, b):
    y = 760
    vx = F.pista(c, t, C["s07"], 260, 1660, y, 0, 90, list(range(0, 91, 10)), "km", size=36)
    E.frase(c, t, C["s07.a"], [("deslocamento", "g", 84, COR)], XE, 210)
    E.formula_em(c, t, C["s07.b"], "Δs = s final − s inicial", XE, 330, 70, "g", TINTA)
    E.frase(c, t, C["s07.d"], [("Δ", "g", 66, COR), ("=", "g", 66, TINTA2), ("variação:", "i", 66), ("final", "g", 60), ("−", "g", 60, TINTA2), ("inicial", "g", 60)], XE, 440, passo=0.1)
    if t < C["s08"]:
        pos = lambda s: 30 + 50 * ease_io(min(1.0, s / 2.0))
        F.movel(c, t, C["s07.f"], vx, y, pos, w=180) if t >= C["s07.e"] else None
        E.foco(c, t, C["s07.e"], 0.4, lambda a: F.carrinho(c, vx(30), y, 180, a=a) if t < C["s07.f"] else None)
        F.vetor(c, t, C["s07.g"], (vx(30), y - 190), (vx(80), y - 190), None, "Δs = 50 km", F.VEL, 11, size=52)
        E.formula_em(c, t, C["s07.g"], "80 − 30 = 50", 1480, 450, 72, "g", TINTA, "center")
        return
    pos = lambda s: 80 - 50 * ease_io(min(1.0, s / 2.0))
    F.movel(c, t, C["s08"] + 0.3, vx, y, pos, w=180)
    F.vetor(c, t, C["s08.a"], (vx(80), y - 190), (vx(30), y - 190), None, "Δs = −50 km", F.VEL, 11, lado=-1, size=52)
    E.formula_em(c, t, C["s08.a"], "30 − 80 = −50", 1480, 450, 72, "g", TINTA, "center")
    E.frase(c, t, C["s08.b"], [("sinal", "i", 56), ("−", "g", 56, COR), ("=", "g", 56, TINTA2)] + ps("o sentido em que os números diminuem", "i", 56), W / 2, 980, "center", 0.08)


# ---------------- distância ----------------
def b_distancia(c, t, C, b):
    def s09():
        E.frase(c, t, C["s09.a"], [("distância", "g", 90, COR), ("percorrida", "g", 90, COR)], XE, 260, passo=0.14)
        E.frase(c, t, C["s09.b"], ps("tudo o que andou, trecho por trecho", "i", 66), XE, 400, passo=0.1)
        km = 80 * ease_io(prog(t, C["s09.b"] + 0.8, 2.0))
        E.foco(c, t, C["s09.b"] + 0.4, 0.5, lambda a: hodometro(c, 960, 640, km, a))
        E.frase(c, t, C["s09.c"], [("nunca", "g", 72), ("negativa", "g", 72, ERRADO)], W / 2, 900, "center", 0.12)
    E.saida(c, t, C["s10"] - 0.1, s09)
    if C["s10"] <= t < C["s11"]:
        def s10():
            y = 820
            vx = F.pista(c, t, C["s10"], 260, 1660, y, 0, 90, list(range(0, 91, 10)), "km", size=36)
            for k, v in (("s10.a", 30), ("s10.b", 80), ("s10.c", 50)):
                E.foco(c, t, C[k], 0.4, lambda a, v=v: (c.drawCircle(vx(v), y, 16, M.paint(E.COR, a)), centro(c, str(v), vx(v), y - 34, 44, "g", COR, a)))
            trecho(c, t, C["s10.d"], vx, 30, 80, 580, "ida: 50 km")
            trecho(c, t, C["s10.d"] + 0.9, vx, 80, 50, 660, "volta: 30 km", lado=-1)
            E.foco(c, t, C["s10.e"], 0.5, lambda a: E.formula(c, "distância = 50 + 30 = 80 km", XE, 250, 74, "g", TINTA, a))
            F.vetor(c, t, C["s10.f"], (vx(30), 470), (vx(50), 470), None, "Δs = 20 km", F.VEL, 12, size=52)
            E.foco(c, t, C["s10.f"] + 0.4, 0.5, lambda a: E.formula(c, "deslocamento = 50 − 30 = 20 km", XE, 360, 74, "g", F.VEL, a))
        E.saida(c, t, C["s11"] - 0.1, s10)
    if t < C["s11"]:
        return
    cx, cy, rw, rh = 1300, 600, 520, 300
    E.foco(c, t, C["s11.a"], 0.5, lambda a: (M.rrect(c, cx - rw, cy - rh, 2 * rw, 2 * rh, rh, "#C4512A", 0.25 * a),
                                             M.rrect(c, cx - rw + 70, cy - rh + 70, 2 * rw - 140, 2 * rh - 140, rh - 70, "#F3F3F0", a)))
    q = ease_io(prog(t, C["s11.a"] + 0.6, max(1.0, C["s11.c"] - C["s11.a"] - 0.4)))
    # o atleta dá uma volta: percorre o contorno de baixo, no sentido anti-horário
    L = 2 * (2 * rw - 2 * rh + 0.0) + 2 * math.pi * (rh - 35)
    s = q * L
    rr = rh - 35
    reta = 2 * rw - 2 * rh
    if s < reta / 2:
        P = (cx + s, cy + rr)
    elif s < reta / 2 + math.pi * rr:
        g = (s - reta / 2) / rr
        P = (cx + reta / 2 + rr * math.sin(g), cy + rr * math.cos(g))
    elif s < 1.5 * reta + math.pi * rr:
        P = (cx + reta / 2 - (s - reta / 2 - math.pi * rr), cy - rr)
    elif s < 1.5 * reta + 2 * math.pi * rr:
        g = (s - 1.5 * reta - math.pi * rr) / rr
        P = (cx - reta / 2 - rr * math.sin(g), cy - rr * math.cos(g))
    else:
        P = (cx + s - 2 * reta - 2 * math.pi * rr, cy + rr)
    E.foco(c, t, C["s11.a"] + 0.4, 0.4, lambda a: E.bola(c, *P, 28, a=a))
    E.foco(c, t, C["s11.a"] + 0.4, 0.4, lambda a: (M.line(c, cx, cy + rh - 70, cx, cy + rh, TINTA, a, 5), centro(c, "largada e chegada", cx, cy + rh + 60, 44, "i", TINTA2, a)))
    E.frase(c, t, C["s11.a"], ps("uma volta na pista", "i", 70), XE, 220, passo=0.12)
    E.frase(c, t, C["s11.b"], [("distância:", "i", 66), ("400 m", "g", 66, COR)], XE, 820, passo=0.12)
    E.frase(c, t, C["s11.c"], [("deslocamento:", "i", 66), ("0", "g", 66, F.VEL)], XE, 930, passo=0.12)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s12"], [("cuidado", "g", 96, ERRADO)], XE, 200)
    E.frase(c, t, C["s12.a"], ps("posição não é o quanto andou", "i", 66), XE + 480, 200, passo=0.1)
    y = 640
    vx = F.pista(c, t, C["s12.a"] + 0.6, 260, 1660, y, 0, 90, list(range(0, 91, 10)), "km", size=36)
    E.foco(c, t, C["s12.b"], 0.5, lambda a: F.carrinho(c, vx(80), y, 180, a=a))
    E.foco(c, t, C["s12.b"] + 0.3, 0.4, lambda a: E.pilula(c, "km 80", vx(80), y - 190, 44, "g", fundo=E.COR, a=a))
    E.foco(c, t, C["s12.c"], 0.5, lambda a: E.escreve(c, "andou 80 km?", XE, 900, 90, "g", ERRADO, a))
    if t >= C["s12.d"]:
        E.risco(c, XE - 10, 910, XE + 620, 830, t, C["s12.d"] - 0.3, largura=11)
    E.foco(c, t, C["s12.d"] - 0.6, 0.4, lambda a: (c.drawCircle(vx(30), y, 16, M.paint(TINTA, a)), centro(c, "saiu do 30", vx(30), y - 60, 44, "i", TINTA2, a)))
    F.vetor(c, t, C["s12.d"], (vx(30), y - 140), (vx(80), y - 140), None, "50 km", F.VEL, 11, size=52)
    E.frase(c, t, C["s12.e"], [("km 80", "g", 66, COR), ("=", "g", 66, TINTA2), ("endereço", "i", 72)], 1100, 900, "left", 0.12)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def s13():
        E.frase(c, t, C["s13"], ps("agora, o atalho", "i", 76, CLARO), W / 2, 160, "center")
        E.frase(c, t, C["s13.a"], [("deslocamento:", "g", 70, BR)] + ps("ignore o caminho", "i", 70, CLARO), XE, 330, passo=0.12)
        E.formula_em(c, t, C["s13.b"], "final − inicial", XE + 60, 450, 84, "g", CLARO)
        E.frase(c, t, C["s13.c"], [("distância:", "g", 70, BR)] + ps("corte onde o corpo vira", "i", 70, CLARO), XE, 640, passo=0.12)
        E.formula_em(c, t, C["s13.d"], "some os trechos, todos +", XE + 60, 760, 84, "g", CLARO)
        # um caminho com volta, cortado no ponto de virada
        y = 930
        q = ease_io(prog(t, C["s13.c"] + 0.4, 1.0))
        if q > 0:
            F.poli(c, [(700, y), (1500, y), (1500, y - 50), (1100, y - 50)], q, BR, 1.0, 6)
        if t >= C["s13.c"] + 1.4:
            E.foco(c, t, C["s13.c"] + 1.4, 0.4, lambda a: (M.line(c, 1500, y - 90, 1500, y + 40, E.COR, a, 8), E.escreve(c, "corte", 1530, y - 40, 44, "i", CLARO, a)))
    E.saida(c, t, C["s14"] - 0.1, s13)
    if t < C["s14"]:
        return
    E.frase(c, t, C["s14.a"], ps("o deslocamento só depende do", "i", 70, CLARO) + [("começo", "g", 66, BR), ("e", "i", 70, CLARO), ("do", "i", 70, CLARO), ("fim", "g", 66, BR)],
            W / 2, 300, "center", 0.1)
    E.frase(c, t, C["s14.b"], [("sem", "i", 76, CLARO), ("volta?", "g", 76, BR)], W / 2, 560, "center", 0.12)
    E.formula_em(c, t, C["s14.c"], "distância = deslocamento sem o sinal", W / 2, 720, 70, "g", BR, "center")
    E.frase(c, t, lerp(C["s14.c"], C["s14.end"], 0.6), ps("uma conta só resolve as duas", "i", 62, CLARO), W / 2, 860, "center", 0.1)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s15"], ps("hora de testar", "i", 72, COR), XE, 200)
    y = 520
    vx = F.pista(c, t, C["s15"] + 0.5, 300, 1620, y, -20, 60, list(range(-20, 61, 20)), "m", size=40)
    for k, v in (("s15.a", -20), ("s15.b", 60), ("s15.c", 40)):
        E.foco(c, t, C[k], 0.4, lambda a, v=v: (c.drawCircle(vx(v), y, 18, M.paint(E.COR, a)), centro(c, E._num(v), vx(v), y - 40, 50, "g", COR, a)))
    q = ease_io(prog(t, C["s15.b"], 1.2))
    if q > 0:
        F.poli(c, [(vx(-20), y - 110), (vx(60), y - 110), (vx(60), y - 170), (vx(40), y - 170)], q if t < C["s15.c"] else min(1.0, 0.8 + 0.2 * ep(t, C["s15.c"], 0.5)),
               TINTA2, 1.0, 5, dash=E.TRACO)
    E.frase(c, t, C["s15.d"], [("distância", "g", 72), ("percorrida?", "g", 72, COR)], XE, 800, passo=0.12)
    E.frase(c, t, C["s15.e"], [("deslocamento?", "g", 72, F.VEL)], XE, 920)
    if t >= C["s16"]:
        E.relogio(c, t, C["s16.a"], cx=1520, cy=770, r=130)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    y = 660
    vx = F.pista(c, t, C["s17"], 300, 1620, y, -20, 60, list(range(-20, 61, 20)), "m", size=40)
    for v in (-20, 60, 40):
        E.foco(c, t, C["s17"] + 0.3, 0.4, lambda a, v=v: c.drawCircle(vx(v), y, 16, M.paint(E.COR, a)))
    if t < C["s18"]:
        trecho(c, t, C["s17.b"], vx, -20, 60, y - 260, "ida: 80 m")
        trecho(c, t, C["s17.c"], vx, 60, 40, y - 150, "volta: 20 m", lado=-1)
        E.formula_em(c, t, C["s17.b"] + 0.5, "60 − (−20) = 80", XE, 230, 70, "g", TINTA2)
        E.formula_em(c, t, C["s17.d"], "80 + 20 =", XE, 900, 90, "g", TINTA)
        bola_txt(c, t, C["s17.d"] + 0.8, "100 m", 960, 870, 110, 60)
        return
    F.vetor(c, t, C["s18"] + 0.3, (vx(-20), y - 200), (vx(40), y - 200), None, "Δs = 60 m", F.VEL, 12, size=56)
    E.formula_em(c, t, C["s18.a"], "40 − (−20)", XE, 900, 90, "g", TINTA)
    E.formula_em(c, t, C["s18.b"], "= 40 + 20", XE + 450, 900, 90, "g", TINTA)
    bola_txt(c, t, C["s18.c"], "60 m", 1560, 870, 110, 64, F.VEL)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def s19():
        resumo(c, t, C, "s19", (("s19.a", [("movimento", "g", 70), ("depende", "i", 70), ("do", "i", 70), ("referencial", "g", 70, COR)]),
                                ("s19.b", [("deslocamento:", "g", 70, F.VEL), ("final", "i", 70), ("−", "g", 70), ("inicial", "i", 70)]),
                                ("s19.c", [("distância:", "g", 70, COR), ("a", "i", 70), ("soma", "i", 70), ("de", "i", 70), ("tudo", "i", 70)])))
    E.saida(c, t, C["s20"] - 0.1, s19)
    if t < C["s20"]:
        return
    E.frase(c, t, C["s20"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C["s20.a"], ps("velocidade constante", "i", 76), XE, 400, passo=0.12)
    E.frase(c, t, C["s20.b"], [("função", "g", 110, COR), ("horária", "g", 110, COR)], XE, 560, passo=0.14)
    E.formula_em(c, t, C["s20.b"] + 0.8, "s = s₀ + v · t", XE, 760, 110, "g", TINTA)
    fim_inscreva(c, t, C, "s20", "s20.c", "s20.d")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, referencial=b_referencial, posicao=b_posicao, deslocamento=b_deslocamento,
              distancia=b_distancia, erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
