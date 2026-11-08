"""Visual — Estudativo · MAT-POT-014: ordem de grandeza.
A distância entre potências de dez se mede em vezes, então as retas de 3,16 ficam em escala de vezes: 1, 3,16 e 10 igualmente espaçados.
Peças locais: plateia em pontos, faixa da reta. Todo instante vem de C[...]: entre dois cues, lerp(C[a], C[b], f)."""
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, passo, palco, centro
import motor as M
import skia

E.usar("Matemática", "Potências e Raízes")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-POT-014_ordem_de_grandeza.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("vezes", "virada", "metodo", "atalho", "questao", "fim"))
BR = "#FFFFFF"
assert 5000 - 1000 == 4000 and 10000 - 5000 == 5000 and 5000 / 1000 == 5 and 10000 / 5000 == 2
assert 9.9 < 3.16 * 3.16 < 10 and 5.5 == (1 + 10) / 2 and -4 + 1 == -3 and 0.001 > 0.0007


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças desta aula ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    """uma frase, palavra a palavra, no mesmo estilo"""
    return [(w, est, size, cor) for w in txt.split()]


def cen(c, t, t0, s, cx, y, size, cor=None, est="g"):
    E.foco(c, t, t0, 0.5, lambda a: centro(c, s, cx, y, size, est, cor or TINTA, a))


def fcen(c, t, t0, s, cx, y, size, cor=None):
    E.formula_em(c, t, t0, s, cx, y, size, "g", cor, "center")


def plateia(c, x, y, w, h, n, cor, a=1.0, cheio=1.0):
    """plateia em pontos: n pessoas em fileiras dentro de x..x+w; cheio = 0..1 enche da frente para o fundo"""
    if a <= 0:
        return
    col = max(1, round((n * w / h) ** 0.5))
    lin = -(-n // col)
    px, py = w / col, h / lin
    r = max(2.0, min(px, py) * 0.36)
    p = M.paint(cor, a)
    for i in range(int(n * cheio)):
        c.drawCircle(x + (i % col + 0.5) * px, y + h - (i // col + 0.5) * py, r, p)


def faixa(c, x0, x1, y, h, cor, a):
    """trecho da reta pintado de leve: o lado de cada potência"""
    M.rrect(c, x0, y - h / 2, x1 - x0, h, 12, cor, 0.16 * a)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    ka, kb, kc, kd, ke = C["s01.a"], C["s01.b"], C["s01.c"], C["s01.d"], C["s01.e"]
    ts = lerp(kc, kd, 0.34)

    def um():
        E.linha(c, t, [("5.000", "g", 110, COR, ka), ("está mais perto de", "i", 72, TINTA, ka + 0.4), ("1.000", "g", 84, TINTA, kb), ("ou de", "i", 72, TINTA, lerp(kb, kc, 0.5)), ("10.000?", "g", 84, TINTA, kc)], W / 2, 220, "center")
        x0, x1, y = 300, 1640, 590
        fm = lambda v: f"{v:,}".replace(",", ".")
        vx = E.reta(c, t, ka, x0, x1, y, 1000, 10000, (1000, 5000, 10000), fm, size=62, tm=(kb, ka + 0.2, kc))
        E.salto(c, t, ts, vx(5000), vx(1000), y - 26, 150, TINTA2, "diferença 4.000", size=56)
        E.salto(c, t, lerp(ts, kd, 0.5), vx(5000), vx(10000), y - 26, 150, TINTA2, "diferença 5.000", size=56)
        E.linha(c, t, [("em", "i", 90, TINTA, kd - 0.2), ("ordem de grandeza,", "g", 84, COR, kd), ("a resposta é", "i", 90, TINTA, lerp(kd, ke, 0.6)), ("dez mil", "g", 96, CERTO, ke)], W / 2, 860, "center")
    E.saida(c, t, C["s02"] - 0.1, um)
    if t >= C["s02"]:
        ta, tb = C["s02.a"], C["s02.b"]
        E.foco(c, t, tb - 0.2, 0.7, lambda a: E.bola(c, 1490, 540, 250 * ease_back(prog(t, tb - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, ps("até o fim desta aula", "i", 90), XE, 300, passo=0.14)
        E.frase(c, t, lerp(ta, tb, 0.38), [("entender", "g", 110, COR)] + ps("por quê", "i", 100), XE, 470)
        E.frase(c, t, lerp(ta, tb, 0.55), ps("achar a ordem de grandeza", "i", 80), XE, 610, passo=0.1)
        E.frase(c, t, lerp(ta, tb, 0.72), ps("de", "i", 80) + [("qualquer número", "g", 84, COR)], XE, 720, passo=0.12)
        E.foco(c, t, tb + 0.2, 0.5, lambda a: (centro(c, "+ atalho", 1490, 525, 80, "g", E.SOBRE, a),
                                               centro(c, "de prova", 1490, 610, 80, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"] + 0.3, ps("você precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "2", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 240, 700, 120, "i", TINTA, a))
    x, w = 960, 780
    itens = (("s03.b", "escrever em", "notação científica"), ("s03.c", "saber o que é", "raiz quadrada"))
    for i, (k, l1, l2) in enumerate(itens):
        y = 240 + i * 260
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 196, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 62)], x + 44, y + 84)
        E.frase(c, t, C[k] + 0.3, [(l2, "g", 62, COR)], x + 44, y + 160)
    py = lerp(410, 670, ease_io(prog(t, C["s03.c"] - 0.35, 0.5)))
    E.cursor(c, x + w - 30, py, ep(t, C["s03.b"], 0.4))
    E.frase(c, t, lerp(C["s03.c"], C["s03.end"], 0.55), ps("faltou alguma?", "i", 62, COR) + ps("procure no canal", "i", 62), 960, 800, "left", 0.12)


# ---------------- o que é ----------------
def b_oque(c, t, C, b):
    ka, kb, kc, kd = C["s04.a"], C["s04.b"], C["s04.c"], C["s04.d"]
    E.frase(c, t, ka, [("ordem de grandeza", "g", 110, COR)], W / 2, 170, "center")
    E.frase(c, t, lerp(ka, kb, 0.22), ps("a potência de 10", "g", 76) + ps("mais próxima de um número", "i", 80), W / 2, 290, "center", 0.1)
    E.frase(c, t, lerp(ka, kb, 0.6), ps("diz o tamanho da coisa, sem o valor exato", "i", 72), W / 2, 400, "center", 0.09)
    for k, n, s, x in ((kb, 30, "dezenas?", 200), (kc, 300, "centenas?", 720), (kd, 2400, "milhares?", 1240)):
        E.foco(c, t, k, 0.5, lambda a, n=n, x=x, k=k: plateia(c, x, 500, 480, 300, n, E.COR, a, E.clamp(prog(t, k, 0.7))))
        cen(c, t, k + 0.1, s, x + 240, 910, 84, COR)


# ---------------- medir em vezes ----------------
def b_vezes(c, t, C, b):
    ka, kb, kc, kd, ke, kf = C["s05.a"], C["s05.b"], C["s05.c"], C["s05.d"], C["s05.e"], C["s05.f"]

    def um():
        E.frase(c, t, C["s05"] + 0.1, ps("o que é", "i", 84) + [("mais próxima?", "g", 84, COR)], W / 2, 150, "center", 0.14)
        y = 320
        cen(c, t, ka - 0.2, "1.000", 330, y + 30, 90)
        E.ponte(c, t, ka, 480, 700, y, "× 10", None, 56)
        cen(c, t, ka + 0.2, "10.000", 900, y + 30, 90)
        E.ponte(c, t, ka + 0.3, 1080, 1300, y, "× 10", None, 56)
        cen(c, t, ka + 0.5, "100.000", 1520, y + 30, 90)
        E.frase(c, t, kb, ps("a distância se mede", "i", 84) + [("em vezes,", "g", 84, COR)] + ps("não em subtração", "i", 84), W / 2, 530, "center", 0.12)
        y2 = 780
        cen(c, t, kc, "1.000", 360, y2 + 34, 110)
        E.ponte(c, t, kd - 0.2, 560, 760, y2, "× 5", None, 60)
        cen(c, t, kd - 0.1, "5.000", 960, y2 + 34, 110)
        E.ponte(c, t, lerp(ke, kf, 0.9), 1170, 1370, y2, "× 2", None, 60)
        cen(c, t, kf - 0.1, "10.000", 1590, y2 + 34, 110)
    E.saida(c, t, C["s06"] - 0.1, um)
    if t >= C["s06"]:
        a6, b6 = C["s06.a"], C["s06.b"]
        E.frase(c, t, C["s06"] + 0.1, [("× 2", "g", 130, CERTO)] + ps("é menos que", "i", 96) + [("× 5", "g", 130, TINTA)], W / 2, 250, "center", 0.2)
        E.frase(c, t, a6, [("5.000", "g", 100, COR)] + ps("está mais perto de", "i", 92) + [("10.000", "g", 100, COR)], W / 2, 490, "center", 0.14)
        E.frase(c, t, lerp(a6, b6, 0.72), ps("a ordem de grandeza de 5.000 é", "i", 76), W / 2, 660, "center", 0.1)
        E.formula_em(c, t, b6, "10^4", W / 2, 880, 200, "g", COR, "center")


# ---------------- ponto de virada ----------------
def b_virada(c, t, C, b):
    x0, x1, y = 300, 1620, 480
    xm = (x0 + x1) / 2

    def meio():
        ka, kb, kc, kd = C["s07.a"], C["s07.b"], C["s07.c"], C["s07.d"]
        E.frase(c, t, C["s07"] + 0.1, ps("onde o número", "i", 80) + [("muda de lado?", "g", 80, COR)], W / 2, 150, "center", 0.12)
        E.frase(c, t, ka, ps("o meio do caminho entre", "i", 76) + [("1", "g", 80, COR)] + ps("e", "i", 76) + [("10,", "g", 80, COR)] + ps("medido", "i", 76) + [("em vezes", "g", 76, COR)], W / 2, 280, "center", 0.09)
        cen(c, t, ka + 0.3, "1", x0, y + 34, 130)
        cen(c, t, ka + 0.5, "10", x1, y + 34, 130)
        cen(c, t, ka + 0.7, "?", xm, y + 34, 130, CINZA)
        E.ponte(c, t, kb, x0 + 110, xm - 90, y, "× ?", None, 60)
        E.ponte(c, t, kc, xm + 90, x1 - 130, y, "× ?", None, 60)
        E.frase(c, t, kd, ps("esse número vezes ele mesmo", "i", 84), W / 2, 720, "center", 0.11)
        fcen(c, t, lerp(kd, C["s07.end"], 0.6), "? × ? = 10", W / 2, 890, 130, COR)
    E.saida(c, t, C["s08"] - 0.1, meio)

    def raiz():
        ka, kb, kc, kd = C["s08.a"], C["s08.b"], C["s08.c"], C["s08.d"]
        E.frase(c, t, C["s08"] + 0.1, ps("número vezes ele mesmo dando 10", "i", 76), W / 2, 170, "center", 0.11)
        cen(c, t, ka - 0.1, "é a raiz quadrada de 10", W / 2, 280, 76, COR)
        fcen(c, t, ka, "r{10}", 620, 500, 190)
        fcen(c, t, kb, "≈ 3,16", 1200, 500, 170, COR)
        fcen(c, t, kc, "3,16 × 3,16", 750, 790, 130)
        E.frase(c, t, kd, ps("=", "g", 120) + ps("quase", "i", 120) + [("10", "g", 130, CERTO)], 1170, 790, "left", 0.12)
    if C["s08"] - 0.1 <= t:
        E.saida(c, t, C["s09"] - 0.1, raiz)

    if t >= C["s09"]:
        ka, kb, kc = C["s09.a"], C["s09.b"], C["s09.c"]
        tu = lerp(kc, C["s09.end"], 0.48)
        yr = 480
        pos = {0: "1", 1: "3,16", 2: "10"}
        E.foco(c, t, ka, 0.5, lambda a: E.pilula(c, "ponto de virada", W / 2, 180, 96, "g", a=a, cor=E.SOBRE))
        vx = lambda v: x0 + v / 2 * (x1 - x0)
        for k, v0, v1 in ((kb, 0, 1), (kc, 1, 2)):
            E.foco(c, t, k, 0.4, lambda a, v0=v0, v1=v1: faixa(c, vx(v0), vx(v1), yr - 26, 80, E.COR, a), blur=4)
        E.reta(c, t, ka - 0.2, x0, x1, yr, 0, 2, (0, 1, 2), lambda v: pos[v], size=76, tm=(ka - 0.1, ka, ka - 0.1))
        E.frase(c, t, kb, ps("até", "i", 62) + [("3,16", "g", 62, COR)], vx(0.5), 400 - 20, "center", 0.08)
        E.frase(c, t, kb + 0.5, ps("mais perto do", "i", 62) + [("1", "g", 68, COR)], vx(0.5), 680, "center", 0.08)
        E.frase(c, t, kc, ps("depois dele", "i", 62), vx(1.5), 400 - 20, "center", 0.08)
        E.frase(c, t, kc + 0.5, ps("mais perto do", "i", 62) + [("10", "g", 68, COR)], vx(1.5), 680, "center", 0.08)
        E.frase(c, t, tu, ps("trocar a frente por 10 é", "i", 80) + [("subir o expoente em 1", "g", 76, COR)], W / 2, 880, "center", 0.1)


# ---------------- método ----------------
def b_metodo(c, t, C, b):
    def passos():
        ka, kb, kc = C["s10.a"], C["s10.b"], C["s10.c"]
        a1, b1, c1, d1 = C["s11.a"], C["s11.b"], C["s11.c"], C["s11.d"]
        E.frase(c, t, ka - 0.1, ps("o método tem", "i", 72) + [("dois passos", "g", 72, COR)], XE, 130, "left", 0.11)
        passo(c, t, kb, 1, "escreva em", "notação científica", 240)
        fcen(c, t, kc, "5.000 = 5 × 10^3", 1250, 270, 110, COR)
        passo(c, t, a1, 2, "compare a frente", "com 3,16", 520)
        E.foco(c, t, b1, 0.5, lambda a: (E.selo(c, 860, 480, 40, True, a)))
        E.frase(c, t, b1, ps("passou:", "i", 72) + [("o expoente sobe 1", "g", 66, COR)], 920, 505, passo=0.1)
        E.foco(c, t, c1, 0.5, lambda a: (E.selo(c, 860, 600, 40, False, a)))
        E.frase(c, t, c1, ps("não passou:", "i", 72) + [("o expoente fica", "g", 66)], 920, 625, passo=0.1)
        E.frase(c, t, d1 - 0.8, [("5", "g", 120, COR)] + ps("passa:", "i", 110), 560, 880, "left", 0.14)
        E.formula_em(c, t, d1, "10^4", 1000, 880, 200, "g", COR)
    E.saida(c, t, C["s12"] - 0.1, passos)
    if t >= C["s12"]:
        ka, kb, kc, kd = C["s12.a"], C["s12.b"], C["s12.c"], C["s12.d"]
        E.frase(c, t, C["s12"] + 0.1, ps("veja a", "i", 84) + [("virada", "g", 84, COR)] + ps("acontecendo", "i", 84), W / 2, 170, "center", 0.12)
        for y, k0, k1, n, s, f, ok, r in ((430, ka, kb, "3.000", "3 × 10^3", "3 não passa", False, "10^3"), (760, kc, kd, "4.000", "4 × 10^3", "4 passa", True, "10^4")):
            cor = CERTO if ok else TINTA2
            fcen(c, t, k0, f"{n} = {s}", 620, y, 110)
            E.frase(c, t, lerp(k0, k1, 0.55), ps(f, "i", 72, cor), 620, y + 110, "center", 0.1)
            E.foco(c, t, k1, 0.5, lambda a, r=r, y=y: (E.bola(c, 1420, y - 40, 130, a=a), E.formula(c, r, 1420, y + 5, 110, "g", E.SOBRE, a, "center")))


# ---------------- aviso ----------------
def b_aviso(c, t, C, b):
    ka, kb, kc = C["s13.a"], C["s13.b"], C["s13.c"]
    t1, t2 = lerp(ka, kb, 0.5), lerp(ka, kb, 0.72)
    E.frase(c, t, C["s13"] + 0.1, ps("um aviso", "i", 84, COR), W / 2, 150, "center", 0.12)
    E.frase(c, t, ka, ps("alguns materiais usam", "i", 84) + [("5,5", "g", 110, COR)], W / 2, 290, "center", 0.11)
    E.frase(c, t, t1, ps("o meio medido", "i", 76) + [("por subtração", "g", 72)], W / 2, 410, "center", 0.11)
    E.frase(c, t, t2, ps("por esse critério, 5.000 ficaria em", "i", 72), 870, 530, "center", 0.09)
    E.formula_em(c, t, t2 + 1.0, "10^3", 1330, 530, 96, "g", COR)
    E.foco(c, t, kb, 0.5, lambda a: (E.bola(c, 300, 690, 52, a=a), centro(c, "1", 300, 712, 60, "g", E.SOBRE, a)))
    E.frase(c, t, kb, ps("a prova disse qual usar?", "i", 76) + [("siga a prova", "g", 80, COR)], 380, 710, "left", 0.1)
    E.foco(c, t, kc, 0.5, lambda a: (E.bola(c, 300, 850, 52, a=a), centro(c, "2", 300, 872, 60, "g", E.SOBRE, a)))
    E.frase(c, t, kc, ps("não disse?", "i", 76) + [("fique com 3,16", "g", 80, COR)], 380, 870, "left", 0.1)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    ka, kb, kc = C["s14.a"], C["s14.b"], C["s14.c"]
    a5, b5, c5, d5 = C["s15.a"], C["s15.b"], C["s15.c"], C["s15.d"]
    fm = lambda v: str(v).replace("-", "−")

    def um():
        E.frase(c, t, C["s14"] + 0.1, ps("cuidado com os", "i", 80) + [("números pequenos", "g", 76, ERRADO)], W / 2, 170, "center", 0.11)
        fcen(c, t, ka, "0,0007", 600, 420, 140)
        E.frase(c, t, kb - 0.3, ps("=", "g", 100), 900, 420, "left")
        E.cientifica(c, t, kb, "7", -4, 1000, 420, 140, cor=COR)
        E.frase(c, t, lerp(kb, kc, 0.45), ps("7 passa, então o expoente sobe", "i", 84), W / 2, 620, "center", 0.11)
        E.foco(c, t, kc, 0.5, lambda a: (E.formula(c, "10^{−5}", W / 2 - 60, 880, 170, "g", ERRADO, a, "center"), E.selo(c, W / 2 + 230, 820, 66, False, a)))
        E.frase(c, t, lerp(kc, C["s14.end"], 0.5), ps("porque 5 parece mais que 4", "i", 66, ERRADO), W / 2, 1000, "center", 0.1)
    E.saida(c, t, C["s15"] - 0.1, um)
    if t < C["s15"]:
        return
    x0, x1, y = 340, 1600, 340
    vx = E.reta(c, t, C["s15"], x0, x1, y, -6, -2, (-5, -4, -3), fm, size=76, tm=(a5 - 0.3, C["s15"] + 0.1, b5))
    E.frase(c, t, a5, ps("−5 é", "g", 84, ERRADO) + ps("descer", "i", 90), 560, 150, "center", 0.11)
    E.salto(c, t, a5, vx(-4), vx(-5), y - 24, 90, ERRADO, largura=7)
    E.salto(c, t, b5, vx(-4), vx(-3), y - 24, 90, CERTO, largura=7)
    fcen(c, t, b5, "−4 + 1 = −3", 1320, 150, 96, CERTO)
    E.formula_em(c, t, c5, "10^{−3}", 700, 680, 200, "g", COR, "center")
    fcen(c, t, lerp(c5, d5, 0.55), "= 0,001", 1230, 680, 150, COR)
    E.frase(c, t, d5, ps("pertinho de", "i", 92) + [("0,0007", "g", 100, TINTA)], W / 2, 880, "center", 0.12)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def regra():
        ka, kb, kc, kd = C["s16.a"], C["s16.b"], C["s16.c"], C["s16.d"]
        te = lerp(kd, C["s16.end"], 0.5)
        E.frase(c, t, C["s16"] + 0.1, ps("agora, o atalho", "i", 76, CLARO), W / 2, 150, "center", 0.11)
        E.frase(c, t, ka, ps("olhe só o", "i", 100, CLARO) + [("primeiro algarismo", "g", 96, BR)], W / 2, 280, "center", 0.14)
        for k, s, f, y, cor in ((kb, "1 ou 2", "o expoente fica", 470, BR), (kc, "de 4 a 9", "sobe", 610, CLARO), (kd, "3", "olhe o algarismo seguinte", 750, BR)):
            E.foco(c, t, k, 0.5, lambda a, s=s, y=y: E.pilula(c, s, 460, y - 26, 72, "g", a=a, cor=E.SOBRE))
            E.frase(c, t, k + 0.1, [(f, "g", 76, cor)], 730, y)
        E.frase(c, t, te, ps("depois do 3:", "i", 72, CLARO) + [("0", "g", 76, BR)] + ps("fica,", "i", 72, CLARO) + [("de 2 para cima", "g", 72, BR)] + ps("sobe", "i", 72, CLARO), W / 2, 910, "center", 0.11)
    E.saida(c, t, C["s17"] - 0.1, regra)
    if t < C["s17"]:
        return
    ka, kb = C["s17.a"], C["s17.b"]
    E.frase(c, t, C["s17"] + 0.1, ps("o ponto de virada está", "i", 90, CLARO), W / 2, 240, "center", 0.12)
    E.frase(c, t, ka, ps("entre", "i", 100, CLARO) + [("3", "g", 170, BR)] + ps("e", "i", 100, CLARO) + [("4", "g", 170, BR)], W / 2, 440, "center", 0.16)
    E.foco(c, t, kb, 0.5, lambda a: E.selo(c, 290, 690, 66, False, a))
    E.frase(c, t, kb + 0.1, ps("não compensa quando a frente começa com", "i", 66, CLARO), 390, 670, "left", 0.08)
    E.frase(c, t, lerp(kb, C["s17.end"], 0.42), [("3,1", "g", 96, BR)], 390, 780)
    E.frase(c, t, lerp(kb, C["s17.end"], 0.62), ps("aí,", "i", 80, CLARO) + [("compare com 3,16", "g", 76, BR)] + ps("com calma", "i", 80, CLARO), W / 2, 910, "center", 0.11)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s18"] + 0.1, ps("hora de testar", "i", 72, COR), XE, 170, passo=0.12)
    ka, kb, kc = C["s18.a"], C["s18.b"], C["s18.c"]
    E.frase(c, t, ka - 0.5, ps("o mundo tem cerca de", "i", 76), XE, 310, passo=0.1)
    E.frase(c, t, ka + 0.2, [("8 bilhões", "g", 110, COR)] + ps("de pessoas", "i", 80), XE, 430, passo=0.12)
    E.frase(c, t, kb - 0.6, ps("uma cidade tem", "i", 76), XE, 570, passo=0.1)
    E.frase(c, t, kb + 0.2, [("25 mil", "g", 110, COR)] + ps("habitantes", "i", 80), XE, 690, passo=0.12)
    E.frase(c, t, kc, ps("qual é a", "i", 84) + [("ordem de grandeza", "g", 84, COR)] + ps("de cada número?", "i", 84), W / 2 + 20, 880, "center", 0.1)
    E.relogio(c, t, C["s19.a"], 1520, 330, 170)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    ka, kb = C["s20.a"], C["s20.b"]
    a1, b1 = C["s21.a"], C["s21.b"]
    for y, k0, k1, s, f, ok, r, end in ((280, ka, kb, "8 bilhões = 8 × 10^9", "8 passa, o expoente sobe", True, "10^{10}", None), (700, a1, b1, "25 mil = 2,5 × 10^4", "2,5 não passa, o expoente fica", False, "10^4", None)):
        fcen(c, t, k0, s, 740, y, 104)
        E.frase(c, t, lerp(k0, k1, 0.62), ps(f, "i", 74, CERTO if ok else TINTA2), 740, y + 120, "center", 0.1)
        E.foco(c, t, k1, 0.5, lambda a, r=r, y=y: (E.bola(c, 1520, y - 30, 160, a=a), E.formula(c, r, 1520, y + 20, 120, "g", E.SOBRE, a, "center")))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s22"], [("resumindo", "i", 92, COR)], W / 2, 210, "center")
        for i, (k, s) in enumerate((("s22.a", "escreva em notação científica"), ("s22.b", "compare a frente com 3,16"), ("s22.c", "suba o expoente se passar"))):
            y = 390 + i * 190
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 260, y - 30, 56, a=a),
                                                         E.centro(c, str(i + 1), 260, y - 7, 64, "g", E.SOBRE, a)))
            E.frase(c, t, C[k] + 0.1, [(s, "g", 84)], 350, y)
    E.saida(c, t, C["s23"] - 0.1, resumo)
    if t < C["s23"]:
        return
    a3, b3 = C["s23.a"], C["s23.b"]
    E.frase(c, t, C["s23"] + 0.1, ps("na próxima aula", "i", 84), XE, 240, passo=0.14)
    E.frase(c, t, a3, [("praticar", "g", 130, COR)] + ps("tudo isso", "i", 110), XE, 390, passo=0.14)
    E.frase(c, t, lerp(a3, b3, 0.25), ps("fazer contas e comparar medidas enormes e minúsculas", "i", 66), XE, 500, passo=0.07)
    E.frase(c, t, b3 - 0.4, ps("como", "i", 80) + [("a distância até o Sol", "g", 80, COR)], XE, 620, passo=0.1)
    E.foco(c, t, C["s23.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1440, 750, 76, estilo="g", a=a, cor=E.SOBRE))
    p = ease_io(prog(t, C["s23.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1770, 1570, p), lerp(990, 775, p), ep(t, C["s23.c"] + 0.2, 0.4))
    E.frase(c, t, C["s23.d"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 930, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, oque=b_oque, vezes=b_vezes, virada=b_virada, metodo=b_metodo, aviso=b_aviso,
              erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
