"""Visual — Estudativo · QUI-TER-006: energia de ativação e catalisador.

Segue a LINGUAGEM VISUAL DA QUÍMICA (QUI-MIS-001), da trilha (QUI-TER-001) e da Cinética (QUI-TER-004).
Nesta aula entra o CAMINHO DA REAÇÃO com morro: Q.energia (reagentes, topo = complexo ativado, produtos); Ea na pílula turquesa
à esquerda do pico, ΔH fora da caixa à direita (azul < 0, âmbar > 0). O caminho com catalisador é o tracejado mais baixo.
Valores sempre como marcas do eixo (marcas_eixo), nunca como energia absoluta. A seta errada (medida do zero) sai em vermelho
com risco. Peça candidata ao kit: marcas_eixo (números no eixo do Q.energia) e seta de Ea com catalisador (seta_ea).
Todo instante vem de C[...] (marcadores do roteiro)."""
import math

import editorial as E
import quimica as Q
import fisica as F
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Química", "Termoquímica e Cinética")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_QUI-TER-006_energia_ativacao_catalisador.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("ativacao", "exemplo", "catalisador", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
AZUL, AMBAR = Q.ELETRON, "#E8A317"

assert 130 - 50 == 80 and 10 - 50 == -40 and 130 - 10 == 120
assert 100 - 30 == 70 and 70 - 30 == 40 and 60 - 30 == 30
assert Q.lados("2 CO + O2 -> 2 CO2")[0] == Q.lados("2 CO + O2 -> 2 CO2")[1]

GX, GY, GW, GH = 260, 230, 1000, 560


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças desta aula ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def bola_txt(c, t, t0, s, cx, cy, r, size, cor=None):
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r * ease_back(prog(t, t0, 0.5)), cor, a),
                                     E.formula(c, s, cx, cy + size * 0.36, size, "g", E.SOBRE, a, "center")))


def pilula_em(c, t, t0, s, cx, cy, size, fundo=None, est="g", cor=BR):
    E.foco(c, t, t0, 0.4, lambda a: E.pilula(c, s, cx, cy, size, est, fundo=fundo, a=a, cor=cor))


def lista(c, t, itens, x, y0, dy):
    for i, (ti, partes) in enumerate(itens):
        y = y0 + i * dy
        E.foco(c, t, ti, 0.5, lambda a, i=i, y=y: (E.bola(c, x + 40, y - 26, 44, a=a), centro(c, str(i + 1), x + 40, y - 4, 54, "g", E.SOBRE, a)))
        E.frase(c, t, ti + 0.1, partes, x + 110, y, passo=0.12)


def marcas_eixo(c, t, t0, Y, vals, x=GX, size=44, escuro=False):
    """números das marcas no eixo de pé do Q.energia"""
    if Y is None:
        return
    tinta = "#9AA0A8" if escuro else TINTA2
    for v in vals:
        E.foco(c, t, t0, 0.4, lambda a, v=v: (M.line(c, x - 14, Y(v), x + 14, Y(v), tinta, a, 4),
                                              E.formula(c, str(v), x - 26, Y(v) + size * 0.36, size, "g", tinta, a, "right")))


def seta_ea(c, t, t0, Y, v0, v1, x, cor=None, rot=None, size=46):
    """seta vertical de v0 a v1 no x dado (Ea com catalisador, ou a seta errada)"""
    if Y is None or t < t0:
        return
    cor = cor or E.COR
    p = ep(t, t0, 0.4)
    F.seta(c, x, Y(v0), x, Y(v1) + 6, cor, p, 7, 24, ease_out(prog(t, t0, 0.6)))
    if rot:
        E.foco(c, t, t0 + 0.3, 0.4, lambda a: E.formula(c, rot, x + 20, (Y(v0) + Y(v1)) / 2 + size * 0.36, size, "g", cor, a))


def fosforo(c, x, y, ang, a=1.0, t=0.0, aceso=True):
    """palito de fósforo com a cabeça em (x, y)"""
    if a <= 0:
        return
    dx, dy = math.cos(math.radians(ang)), math.sin(math.radians(ang))
    M.line(c, x, y, x + dx * 260, y + dy * 260, "#D9A066", a, 16)
    c.drawCircle(x, y, 20, M.paint("#B3261E", a))
    if aceso:
        f = 1 + 0.08 * math.sin(t * 9)
        pth = skia.Path(); pth.moveTo(x, y - 90 * f); pth.cubicTo(x + 40, y - 40, x + 30, y + 10, x, y + 10); pth.cubicTo(x - 30, y + 10, x - 40, y - 40, x, y - 90 * f)
        c.drawPath(pth, M.paint("#F59F00", a))


def papel(c, cx, cy, w, h, a=1.0, queima=0.0, t=0.0):
    if a <= 0:
        return
    M.rrect(c, cx - w / 2, cy - h / 2, w, h, 8, "#FFFFFF", a, shadow=True)
    for k in range(6):
        M.line(c, cx - w / 2 + 40, cy - h / 2 + 60 + k * 50, cx + w / 2 - 40, cy - h / 2 + 60 + k * 50, "#C9D6E3", a, 3)
    if queima > 0:
        hh = h * queima
        M.rrect(c, cx - w / 2, cy + h / 2 - hh, w, hh, 8, "#3A2A20", a * 0.85)
        for k in range(5):
            x0 = cx - w / 2 + 30 + k * (w - 60) / 4
            f = 1 + 0.1 * math.sin(t * 8 + k)
            yb = cy + h / 2 - hh
            pth = skia.Path(); pth.moveTo(x0, yb - 70 * f); pth.cubicTo(x0 + 26, yb - 30, x0 + 22, yb, x0, yb); pth.cubicTo(x0 - 22, yb, x0 - 26, yb - 30, x0, yb - 70 * f)
            c.drawPath(pth, M.paint("#F59F00", a))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def um():
        q = ep(t, C["s01.c"] + 0.5, 3.0)
        E.foco(c, t, C["s01.a"], 0.5, lambda a: papel(c, 1350, 540, 460, 560, a, 0.6 * q, t))
        E.foco(c, t, C["s01.c"], 0.4, lambda a: fosforo(c, 1180, 860, 30, a, t))
        E.frase(c, t, C["s01.a"], ps("parado no ar, o papel", "i", 66), XE, 260, passo=0.1)
        E.frase(c, t, C["s01.a"] + 1.2, [("não", "g", 66, ERRADO)] + ps("pega fogo sozinho", "i", 66), XE, 350, passo=0.1)
        E.frase(c, t, C["s01.b"], ps("mesmo que queimar", "i", 60, TINTA2) + [("libere energia", "g", 56, AZUL)], XE, 470, passo=0.1)
        E.frase(c, t, C["s01.c"], ps("basta um", "i", 66) + [("fósforo", "g", 62, COR)], XE, 640, passo=0.1)
        E.frase(c, t, C["s01.d"], ps("para que serve esse", "i", 66) + [("empurrão?", "g", 62, COR)], XE, 820, passo=0.1)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t < C["s02"]:
        return
    tb = C["s02"] + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1640, 640, 220 * ease_back(prog(t, tb, 0.8)), giro=8 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, C["s02.a"], [("energia", "g", 100, COR), ("de", "i", 100), ("ativação", "g", 100, COR)], XE, 300, passo=0.14)
    lista(c, t, [(C["s02.a"] + 1.0, [("achar", "i", 74), ("no", "i", 74), ("diagrama", "g", 70)]),
                 (C["s02.b"], [("como", "i", 74), ("o", "i", 74), ("catalisador", "g", 70), ("acelera", "i", 74)]),
                 (C["s02.c"], [("sem", "i", 74), ("mudar", "i", 74), ("o", "i", 74), ("ΔH", "g", 70, COR)])], XE, 480, 170)


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], ps("você vai usar", "i", 80, TINTA2), XE, 220, passo=0.12)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.formula(c, "ΔH = chegada − partida", XE, 420, 96, "g", TINTA, a))
    E.frase(c, t, C["s03.b"], [("colisão efetiva:", "g", 64, COR)] + ps("energia mínima e posição certa", "i", 68), XE, 640, passo=0.1)


# ---------------- energia de ativação ----------------
def b_ativacao(c, t, C, b):
    if t < C["s05"]:
        def s04():
            E.frase(c, t, C["s04.a"], ps("a energia mínima se chama", "i", 70), XE, 220, passo=0.1)
            E.frase(c, t, C["s04.a"] + 1.4, [("energia de ativação", "g", 100, COR)], XE, 360)
            # o morro e a bola que precisa subir
            pts = [(300 + k * 14, 860 - 380 * math.exp(-((k * 14 - 680) / 240) ** 2)) for k in range(100)]
            if t >= C["s04.b"]:
                F.poli(c, pts, ease_io(prog(t, C["s04.b"], 1.0)), TINTA, 1, 8)
            if t >= C["s04.c"]:
                u = 0.35 * math.sin((t - C["s04.c"]) * 2.2) ** 2
                i = int(u * 99)
                E.bola(c, pts[i][0], pts[i][1] - 34, 34)
                E.foco(c, t, C["s04.c"], 0.4, lambda a: E.escreve(c, "sem energia, não passa", XE, 980, 56, "i", TINTA, a))
            E.foco(c, t, C["s04.d"], 0.4, lambda a: E.escreve(c, "mesmo que, no fim, libere energia", XE + 700, 980, 56, "i", TINTA2, a))
        E.saida(c, t, C["s05"] - 0.1, s04)
        return
    Y = Q.energia(c, t, C["s05.a"], GX, GY, GW, GH, er=60, ep_=20, pico=100, ea=C["s06.a"], dh=C["s06.b"])
    E.foco(c, t, C["s05.d"], 0.4, lambda a: (E.pilula(c, "complexo ativado", GX + GW / 2, GY - 10, 46, "g", fundo=TINTA, a=a)))
    E.foco(c, t, C["s05.e"], 0.4, lambda a: E.escreve(c, "um arranjo instável, no meio da troca de ligações", GX, 960, 50, "i", TINTA2, a))
    if t >= C["s06.c"]:
        pilula_em(c, t, C["s06.c"], "o fósforo dá a energia da subida", 1500, 160, 44, E.COR)
    if t >= C["s06.d"]:
        pilula_em(c, t, C["s06.d"], "depois, a queima empurra o resto", 1500, 1030, 44, AZUL)


# ---------------- exemplo ----------------
def b_exemplo(c, t, C, b):
    Y = Q.energia(c, t, C["s07"], GX, GY, GW, GH - 60, er=50, ep_=10, pico=130, ea=C["s07.d"], dh=C["s07.f"], sinal=False)
    marcas_eixo(c, t, C["s07.a"], Y, [50], size=44)
    if t >= C["s07.b"]:
        marcas_eixo(c, t, C["s07.b"], Y, [130])
    if t >= C["s07.c"]:
        marcas_eixo(c, t, C["s07.c"], Y, [10])
    E.foco(c, t, C["s07.e"], 0.5, lambda a: E.formula(c, "Ea = 130 − 50 = 80 kJ", GX, 900, 66, "g", COR, a))
    E.foco(c, t, C["s07.g"], 0.5, lambda a: E.formula(c, "ΔH = 10 − 50 = −40 kJ", GX + 820, 900, 66, "g", AZUL, a))
    pilula_em(c, t, C["s08.b"], "morro baixo: rápida", 560, 1020, 46, E.COR)
    pilula_em(c, t, C["s08.d"], "morro alto: lenta", 1300, 1020, 46, TINTA)


# ---------------- catalisador ----------------
EQC = "2 CO + O2 -> 2 CO2"


def b_catalisador(c, t, C, b):
    if t < C["s11"]:
        Y = Q.energia(c, t, C["s09"] - 1.2, GX, GY, GW, GH, er=50, ep_=10, pico=130, cat=90 if t >= C["s09.c"] else None, sinal=False,
                      dh=C["s10.c"])
        E.frase(c, t, C["s09.a"], [("catalisador", "g", 70, COR)] + ps("= caminho mais baixo", "b", 56), XE, 150, passo=0.12)
        pilula_em(c, t, C["s09.c"] + 0.4, "tracejado: com catalisador", 1560, 330, 42, TINTA)
        if t >= C["s09.d"]:
            seta_ea(c, t, C["s09.d"], Y, 50, 90, GX + GW * 0.40, rot="menor")
        pilula_em(c, t, C["s09.e"], "a reação acelera", 1560, 1000, 44, E.COR)
        if t >= C["s10.b"]:
            pilula_em(c, t, C["s10.b"], "patamares iguais", 420, 1000, 44, TINTA)
        if t >= C["s10.d"]:
            pilula_em(c, t, C["s10.d"], "sai inteiro: não é gasto", 970, 1000, 44, TINTA2)
        return
    E.frase(c, t, C["s11.a"], [("enzimas", "g", 80, COR)] + ps("os catalisadores do corpo", "i", 70), XE, 230, passo=0.12)
    E.frase(c, t, C["s11.b"], ps("na saliva, uma enzima quebra o amido do pão:", "i", 58, TINTA2), XE, 340, passo=0.08)
    E.frase(c, t, C["s11.b"] + 2.0, [("adocicado", "g", 56, COR)] + ps("na boca", "i", 58), XE, 420, passo=0.1)
    E.frase(c, t, C["s11.c"], [("no carro", "g", 76, COR)] + ps("platina, paládio e ródio", "i", 64), XE, 600, passo=0.12)
    Q.formula_em(c, t, C["s11.d"], EQC, XE, 780, 96, cores={"CO2": E.COR})
    E.foco(c, t, C["s11.d"] + 0.5, 0.4, lambda a: (E.escreve(c, "tóxico", XE + 110, 860, 46, "b", ERRADO, a)))
    for k in range(3):
        E.foco(c, t, C["s11.c"] + 0.4 + 0.2 * k, 0.4, lambda a, k=k: E.bola(c, 1460 + k * 130, 610, 46, ("#C0C0C8", "#9AA0A8", "#7D8AA6")[k], a))
    E.foco(c, t, C["s11.c"] + 1.0, 0.4, lambda a: centro(c, "Pt   Pd   Rh", 1590, 700, 44, "g", TINTA2, a))


# ---------------- erro comum ----------------
def b_erro(c, t, C, b):
    Y = Q.energia(c, t, C["s12"] - 1.2, GX, GY, GW, GH - 60, er=50, ep_=10, pico=130, sinal=False)
    marcas_eixo(c, t, C["s12"] - 1.0, Y, [10, 50, 130])
    E.frase(c, t, C["s12"], [("cuidado", "g", 80, ERRADO)], 1400, 230)
    if t >= C["s12.a"]:
        seta_ea(c, t, C["s12.a"], Y, 0, 130, GX + GW * 0.38, cor=ERRADO, rot="130?")
        if t >= C["s12.b"] + 0.6:
            E.risco(c, GX + GW * 0.33, Y(40), GX + GW * 0.47, Y(100), t, C["s12.b"] + 0.6, largura=9)
    E.foco(c, t, C["s12.b"], 0.4, lambda a: E.escreve(c, "medida do zero do eixo", 1400, 330, 48, "i", ERRADO, a))
    if t >= C["s12.c"]:
        seta_ea(c, t, C["s12.c"], Y, 50, 130, GX + GW * 0.52, cor=E.COR, rot="80")
    E.foco(c, t, C["s12.d"], 0.5, lambda a: E.formula(c, "Ea = 130 − 50 = 80", 1380, 520, 56, "g", COR, a))
    E.foco(c, t, C["s12.d"] + 0.4, 0.4, lambda a: E.selo(c, 1500, 630, 40, True, a))
    E.frase(c, t, C["s12.c"], ps("a reação começa nos reagentes", "i", 56), GX, 960, passo=0.1)


# ---------------- atalho (palco) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    E.frase(c, t, C["s13"], ps("o atalho para ler qualquer diagrama", "i", 70, CLARO), W / 2, 170, "center", 0.1)
    linhas = ((C["s13.a"], "Ea = topo − reagentes", E.CLARO), (C["s13.b"], "ΔH = produtos − reagentes", BR), (C["s13.c"], "catalisador: só abaixa o topo", BR))
    for k, (tt, s, cor) in enumerate(linhas):
        E.foco(c, t, tt, 0.5, lambda a, k=k, s=s, cor=cor: E.formula(c, s, W / 2, 360 + k * 150, 76, "g", cor, a, "center"))
    E.frase(c, t, C["s13.d"], ps("as duas contas partem dos", "i", 60, CLARO) + [("reagentes", "g", 56, BR)], W / 2, 800, "center", 0.1)
    if t >= C["s14"]:
        E.frase(c, t, C["s14.a"], ps("reação de volta?", "i", 60, CLARO), XE, 950, passo=0.1)
        E.foco(c, t, C["s14.b"], 0.5, lambda a: E.formula(c, "Ea = topo − produtos", 700, 950, 60, "g", AMBAR, a))
        E.foco(c, t, C["s14.c"], 0.5, lambda a: E.formula(c, "130 − 10 = 120", 1350, 950, 60, "g", BR, a))


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s15"], ps("hora de testar", "i", 72, COR), XE, 150)
    Y = Q.energia(c, t, C["s15.a"] - 0.4, GX, GY + 20, GW - 200, GH, er=30, ep_=60, pico=100,
                  cat=70 if t >= C["s15.d"] else None, sinal=False)
    marcas_eixo(c, t, C["s15.a"], Y, [30])
    if t >= C["s15.b"]:
        marcas_eixo(c, t, C["s15.b"], Y, [60])
    if t >= C["s15.c"]:
        marcas_eixo(c, t, C["s15.c"], Y, [100])
    if t >= C["s15.d"]:
        marcas_eixo(c, t, C["s15.d"], Y, [70])
    E.frase(c, t, C["s15.e"], ps("Ea sem catalisador?", "b", 48), 1340, 360, passo=0.1)
    E.frase(c, t, C["s15.e"] + 0.8, ps("Ea com catalisador?", "b", 48), 1340, 440, passo=0.1)
    E.frase(c, t, C["s15.e"] + 1.6, ps("e o ΔH?", "b", 48), 1340, 520, passo=0.1)
    E.relogio(c, t, C["s16.a"], cx=1560, cy=720, r=110)


def b_resposta(c, t, C, b):
    Y = Q.energia(c, t, C["s17"] - 2.0, GX, GY + 20, GW - 200, GH, er=30, ep_=60, pico=100, cat=70, sinal=False, ea=C["s17.a"],
                  dh=C["s17.e"])
    marcas_eixo(c, t, C["s17"] - 1.8, Y, [30, 60, 70, 100])
    if t >= C["s17.c"]:
        seta_ea(c, t, C["s17.c"], Y, 30, 70, GX + (GW - 200) * 0.62, cor=TINTA, rot="40")
    E.foco(c, t, C["s17.b"], 0.4, lambda a: E.formula(c, "sem: 100 − 30 = 70", 1380, 360, 52, "g", COR, a))
    E.foco(c, t, C["s17.d"], 0.4, lambda a: E.formula(c, "com: 70 − 30 = 40", 1380, 470, 52, "g", TINTA, a))
    E.foco(c, t, C["s17.f"], 0.4, lambda a: E.formula(c, "ΔH = 60 − 30 = +30", 1380, 640, 52, "g", AMBAR, a))
    pilula_em(c, t, C["s17.g"], "endotérmica, com ou sem catalisador", 1000, 1020, 48, AMBAR)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s18"], [("resumindo", "i", 92, COR)], W / 2, 180, "center")
        E.foco(c, t, C["s18.a"], 0.5, lambda a: E.formula(c, "Ea = topo − reagentes", W / 2, 420, 100, "g", TINTA, a, "center"))
        E.frase(c, t, C["s18.b"], [("catalisador", "g", 70, COR)] + ps("abaixa a subida, sem mexer no", "i", 74) + [("ΔH", "g", 70)], W / 2, 640, "center", 0.1)
    E.saida(c, t, C["s19"] - 0.1, resumo)
    if t < C["s19"]:
        return
    E.frase(c, t, C["s19"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C["s19.a"], [("lei", "g", 110, COR), ("da", "i", 110), ("velocidade", "g", 110, COR)], XE, 420)
    E.foco(c, t, C["s19.a"] + 0.6, 0.5, lambda a: E.formula(c, "v = k · [A]^x · [B]^y", XE, 580, 80, "g", TINTA, a))
    E.frase(c, t, C["s19.b"], ps("a ordem de cada reagente, numa tabela", "i", 60, TINTA2), XE, 700, passo=0.1)
    E.foco(c, t, C["s19.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 820, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s19.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(1020, 845, p), ep(t, C["s19.c"] + 0.2, 0.4))
    E.frase(c, t, C["s19.d"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], XE, 920)


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, ativacao=b_ativacao, exemplo=b_exemplo, catalisador=b_catalisador, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
