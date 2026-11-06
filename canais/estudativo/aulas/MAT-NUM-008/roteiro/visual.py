"""Visual — Estudativo · MAT-NUM-008: multiplicar por dois algarismos.
Identidade em _ferramentas/editorial.py. As cadeiras do auditório, separadas pelo corredor, viram os dois blocos; cada bloco vira
uma linha de E.conta_mult. Peça local: cadeiras (a grade de 34 fileiras de 26). Painel à direita: o passo que a voz está dizendo."""
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco
import motor as M
import skia

E.usar("Matemática", "Números e Contas")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-NUM-008_multiplicar_por_dois_algarismos.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("blocos", "conta", "atalho", "questao", "fim"))
BR = "#FFFFFF"


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


def bola_txt(c, t, t0, s, cx, cy, r, size, cor=CERTO):
    """o resultado na esfera"""
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r, cor, a), E.centro(c, s, cx, cy + size * 0.35, size, "g", M.on(cor), a)))


def lin(c, t, t0, s, x, y, size=64, estilo="b", cor=None):
    """uma linha do painel ao lado da conta"""
    E.foco(c, t, t0, 0.4, lambda a: E.escreve(c, s, x, y, size, estilo, cor or TINTA, a))


def igual(c, t, t0, t1, s1, s2, x, y, size=66, estilo="b", cor=None, cor2=None):
    """conta em duas partes: a pergunta em t0 e o resultado só em t1, quando a voz chega nele"""
    lin(c, t, t0, s1, x, y, size, estilo, cor)
    lin(c, t, t1, s2, x + E.larg(s1 + " ", estilo, size), y, size, estilo, cor2 or cor or COR)


def lista(c, t, C, ini, ta, n, itens):
    E.frase(c, t, C[ini] + 0.7, [("você", "i", 84), ("só", "i", 84), ("precisa", "i", 84), ("de", "i", 84)], XE, 410)
    E.foco(c, t, C[ta], 0.5, lambda a: E.escreve(c, str(n), XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C[ta] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 960, 780
    y0, dy = (280, 260) if len(itens) == 2 else (190, 240)
    for i, (k, l1, l2) in enumerate(itens):
        y = y0 + i * dy
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 196, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 62)], x + 44, y + 84)
        E.frase(c, t, C[k] + 0.3, [(l2, "g", 62, COR)], x + 44, y + 160)
    px = x + w - 30
    py = y0 + 170
    for i, (k, _, _) in enumerate(itens[1:], 1):
        py = lerp(py, y0 + i * dy + 170, ease_io(prog(t, C[k] - 0.35, 0.5)))
    E.cursor(c, px, py, ep(t, C[itens[0][0]], 0.4))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def tudo():
        ka, kb, kc, kd = C["s01.a"], C["s01.b"], C["s01.c"], C["s01.d"]
        E.linha(c, t, [("34 fileiras", "g", 110, COR, ka), ("com", "i", 100, TINTA, kb - 0.3), ("26", "g", 110, TINTA, kb), ("cadeiras", "i", 100, TINTA, kb + 0.3)], W / 2, 250, "center")
        E.foco(c, t, kc, 0.5, lambda a: E.centro(c, "272 cadeiras", W / 2, 490, 170, "g", ERRADO, a))
        E.frase(c, t, lerp(kc, kd, 0.42), [("sumiram", "i", 100), ("mais", "i", 100), ("de", "i", 100), ("600", "g", 100, ERRADO)], W / 2, 680, "center", passo=0.25)
        E.frase(c, t, kd, [("um", "i", 180), ("zero", "g", 170, COR)], W / 2, 900, "center", passo=0.2)
    E.saida(c, t, C["s02"] - 0.1, tudo)
    if t >= C["s02"]:
        ta, tb = C["s02.a"], C["s02.b"]
        E.foco(c, t, tb - 0.2, 0.7, lambda a: E.bola(c, 1500, 520, 270 * ease_back(prog(t, tb - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, [("até", "i", 90), ("o", "i", 90), ("fim", "i", 90), ("desta", "i", 90), ("aula", "i", 90)], XE, 340)
        E.frase(c, t, lerp(ta, tb, 0.35), [("multiplicar", "g", 110)], XE, 490)
        E.frase(c, t, lerp(ta, tb, 0.42), [("por", "i", 100), ("dois", "g", 100, COR)], XE, 620, passo=0.25)
        E.frase(c, t, lerp(ta, tb, 0.47), [("algarismos", "g", 100, COR)], XE, 740)
        E.frase(c, t, lerp(ta, tb, 0.6), [("sem", "i", 84), ("perder", "i", 84), ("o", "i", 84), ("zero", "g", 76)], XE, 870, passo=0.22)
        E.foco(c, t, tb + 0.2, 0.5, lambda a: (E.centro(c, "+ atalho", 1500, 505, 84, "g", E.SOBRE, a),
                                               E.centro(c, "de prova", 1500, 590, 84, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    lista(c, t, C, "s03", "s03.a", 2, (("s03.b", "multiplicar por um algarismo,", "com vai um"), ("s03.c", "acrescentar o zero", "quando é vezes 10")))


# ---------------- a ideia: dois blocos ----------------
GX, GY, GC, GL = 330, 270, 28, 17  # as cadeiras: 26 colunas de 34 fileiras, com o corredor entre a 20ª e a 21ª


def cadeiras(c, gap, a, ag, ap):
    """34 fileiras de 26 cadeiras; gap = largura do corredor; ag e ap = força do bloco grande e do pequeno"""
    if a <= 0:
        return
    for j in range(34):
        y = GY + j * GL
        for i in range(26):
            x = GX + i * GC + (gap if i >= 20 else 0)
            c.drawRect(skia.Rect.MakeXYWH(x, y, GC - 7, GL - 6), M.paint(E.COR if i < 20 else TINTA, a * (ag if i < 20 else ap)))


def b_blocos(c, t, C, b):
    ka, kb = C["s04.a"], C["s04.b"]
    pa, pb, pc = C["s05.a"], C["s05.b"], C["s05.c"]
    tc = lerp(C["s04"], ka, 0.4)
    gap = 60 * ease_io(prog(t, tc, 0.7))
    xr = GX + 20 * GC + gap
    fg = 1 - 0.75 * (ep(t, pa, 0.4) - ep(t, pb, 0.4))
    fp = 1 - 0.75 * (ep(t, pb, 0.4) - ep(t, pc, 0.4))
    E.frase(c, t, C["s04"] + 0.1, [("antes", "i", 76), ("da", "i", 76), ("conta,", "i", 76), ("pense", "i", 76), ("nas", "i", 76), ("cadeiras", "g", 68, COR)], W / 2, 130, "center", passo=0.25)
    E.foco(c, t, C["s04"] + 0.8, 0.6, lambda a: cadeiras(c, gap, a, fg, fp))
    E.foco(c, t, ka, 0.45, lambda a: E.centro(c, "20", GX + 10 * GC, 245, 76, "g", COR, a))
    E.foco(c, t, kb, 0.45, lambda a: E.centro(c, "6", xr + 3 * GC, 245, 76, "g", TINTA, a))
    E.foco(c, t, tc, 0.45, lambda a: (E.centro(c, "34", 240, 570, 90, "g", TINTA, a), E.centro(c, "fileiras", 240, 630, 54, "i", TINTA, a)))
    if t >= pa:
        q = ep(t, pa, 0.3)
        E.caixa_pontilhada(c, xr - 12, GY - 12, 6 * GC + 20, 34 * GL + 20, q * (1 - ep(t, pb, 0.3)), TINTA, prog_=q)
    if t >= pb:
        q = ep(t, pb, 0.3)
        E.caixa_pontilhada(c, GX - 12, GY - 12, 20 * GC + 16, 34 * GL + 20, q * (1 - ep(t, pc, 0.3)), COR, prog_=q)
    xp = 1190
    lin(c, t, pa, "bloco pequeno", xp, 340, 66, "i")
    lin(c, t, pa + 0.3, "34 × 6", xp, 440, 92, "g", TINTA)
    lin(c, t, pb, "bloco grande", xp, 570, 66, "i")
    lin(c, t, pb + 0.3, "34 × 20", xp, 670, 92, "g", COR)
    lin(c, t, pc, "some os blocos", xp, 800, 66, "g", COR)
    E.frase(c, t, lerp(pc, C["s05.end"], 0.42), [("duas", "g", 62), ("linhas", "i", 70)], xp, 900, passo=0.2)


# ---------------- conta armada ----------------
XV, Y0, SZ, XP = 640, 330, 112, 1010


def b_conta(c, t, C, b):
    k7 = {x: C["s07." + x] for x in "abcdef"}
    k9 = {x: C["s09." + x] for x in "abcd"}
    k10 = {x: C["s10." + x] for x in "abc"}
    t20 = lerp(k7["e"], k7["f"], 0.62)
    t8, t6 = lerp(k9["b"], k9["c"], 0.65), lerp(k9["c"], k9["d"], 0.6)
    tsome = k9["a"] + 1.4
    E.frase(c, t, C["s06.a"], [("arme", "i", 76), ("a", "i", 76), ("conta", "g", 68, COR)], W / 2, 130, "center")
    Q = E.conta_mult(c, t, 34, 26, (C["s06.a"], C["s06.b"]), [[k7["c"], t20, t20 + 0.25], [t8, t6]], XV, Y0, SZ, tz=(C["s08.c"],),
                     tr=(k10["c"], k10["c"] + 0.2, k10["c"] + 0.4), tsoma=k10["a"], vai=[(1, "2", k7["c"] + 0.45, tsome)])
    if k9["a"] <= t < tsome:  # risca o vai um que já foi usado
        E.corta(c, t, k9["a"], Q["px"](1), Y0 - SZ * 0.92 - 20, SZ * 0.5, cor=ERRADO)
    lin(c, t, lerp(k7["f"], C["s07.end"], 0.35), "bloco pequeno", XV + 40, Q["ys"][0], 54, "i", TINTA)
    lin(c, t, lerp(k9["d"], C["s09.end"], 0.45), "bloco grande", XV + 40, Q["ys"][1], 54, "i", COR)

    def fala6():
        lin(c, t, C["s06.a"] + 0.4, "34 em cima", XP, 340, 72)
        lin(c, t, C["s06.b"], "26 embaixo", XP, 460, 72)
        lin(c, t, lerp(C["s06.b"], C["s06.end"], 0.3), "unidade embaixo de unidade", XP, 580, 62, "i", COR)
    E.saida(c, t, C["s07"] - 0.1, fala6)

    def fala7():
        lin(c, t, k7["a"], "1ª linha: tudo vezes 6", XP, 300, 66, "g", COR)
        igual(c, t, k7["b"], lerp(k7["b"], k7["c"], 0.6), "6 × 4 =", "24", XP, 410, 72)
        lin(c, t, k7["c"], "escreva o 4, e o 2 sobe", XP, 510, 62)
        igual(c, t, k7["d"], lerp(k7["d"], k7["e"], 0.6), "6 × 3 =", "18", XP, 630, 72)
        igual(c, t, k7["e"], t20, "com o 2 que subiu:", "20", XP, 730, 62)
        lin(c, t, k7["f"], "204", XP, 860, 96, "g", COR)
    if t >= C["s07"]:
        E.saida(c, t, C["s08"] - 0.1, fala7)

    def fala8():
        lin(c, t, C["s08.a"], "2ª linha: o 2 do 26", XP, 300, 66, "g", COR)
        lin(c, t, lerp(C["s08.a"], C["s08.b"], 0.55), "esse 2 não vale 2", XP, 420, 72)
        lin(c, t, C["s08.b"], "vale 20", XP, 530, 92, "g", COR)
        lin(c, t, lerp(C["s08.b"], C["s08.c"], 0.5), "vezes 2 e vezes 10", XP, 660, 72, "i")
        lin(c, t, C["s08.c"], "a linha começa com zero", XP, 780, 62, "g", COR)
    if t >= C["s08"]:
        E.saida(c, t, C["s09"] - 0.1, fala8)

    def fala9():
        lin(c, t, k9["a"], "risque o 2 que subiu", XP, 320, 66, "b", ERRADO)
        lin(c, t, lerp(k9["a"], k9["b"], 0.75), "ele já foi usado", XP, 420, 62, "i")
        igual(c, t, k9["b"], t8, "2 × 4 =", "8", XP, 550, 76)
        igual(c, t, k9["c"], t6, "2 × 3 =", "6", XP, 670, 76)
        lin(c, t, k9["d"], "680", XP, 810, 96, "g", COR)
    if t >= C["s09"]:
        E.saida(c, t, C["s10"] - 0.1, fala9)

    if t >= C["s10"]:
        lin(c, t, k10["a"], "some as linhas", XP, 330, 72, "i", COR)
        lin(c, t, k10["b"], "204 + 680", XP, 450, 84)
        bola_txt(c, t, k10["c"], "884", 1190, 660, 130, 96)
        lin(c, t, k10["c"] + 0.4, "cadeiras", XP + 350, 685, 72, "i")


# ---------------- conferir trocando a ordem ----------------
def b_conferir(c, t, C, b):
    k = {x: C["s11." + x] for x in "abcdefghi"}
    t8, t7 = lerp(k["e"], k["f"], 0.45), k["g"]
    E.frase(c, t, k["a"], [("troque", "g", 72, COR), ("a", "i", 80), ("ordem", "i", 80)], W / 2, 130, "center", passo=0.16)
    E.conta_mult(c, t, 26, 34, (k["b"], k["b"] + 0.7), [[k["c"] + 0.6, k["c"] + 0.8, k["c"] + 1.0], [t8, t7 + 0.3]], XV, Y0, SZ, tz=(k["d"],),
                 tr=(k["i"] + 0.5, k["i"] + 0.7, k["i"] + 0.9), tsoma=lerp(k["h"], k["i"], 0.65), vai=[(1, "1", lerp(k["e"], k["f"], 0.8), t7 + 0.3)])
    igual(c, t, k["c"] - 0.8, k["c"], "vezes 4:", "104", XP, 300, 70)
    lin(c, t, k["d"] - 0.8, "vezes 30:", XP, 410, 70)
    lin(c, t, k["d"], "o zero primeiro", XP + 330, 410, 62, "g", COR)
    igual(c, t, k["e"], lerp(k["e"], k["f"], 0.3), "3 × 6 =", "18", XP, 520, 70)
    lin(c, t, lerp(k["e"], k["f"], 0.45), "escreva o 8, e o 1 sobe", XP, 610, 60)
    igual(c, t, k["f"], lerp(k["f"], k["g"], 0.5), "3 × 2 =", "6", XP, 720, 70)
    igual(c, t, lerp(k["f"], k["g"], 0.7), k["g"], "com o 1 que subiu:", "7", XP, 810, 60)
    lin(c, t, k["h"], "780", XP + 600, 720, 84, "g", COR)
    bola_txt(c, t, k["i"] + 0.5, "884", 1330, 945, 92, 70)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    ka, kb, kcc, kd = C["s12.a"], C["s12.b"], C["s12.c"], C["s12.d"]
    xv, y, s = 620, 380, 120
    xp = 880
    E.frase(c, t, ka, [("esquecer", "g", 92, ERRADO), ("o", "i", 100), ("zero", "g", 92, ERRADO)], W / 2, 170, "center", passo=0.16)
    E.foco(c, t, kb - 0.3, 0.5, lambda a: E.numero(c, "204", xv, y, s, "g", TINTA, a))

    def monta(a):
        E.numero(c, "68", xv, y + 145, s, "g", TINTA, a)
        E.escreve(c, "+", xv - 3.4 * s * 0.72, y + 145, s, "g", TINTA, a)
    E.foco(c, t, kb, 0.5, monta)
    if t >= kb:
        M.line(c, xv - 3.5 * s * 0.72, y + 180, xv + 10, y + 180, TINTA, 1.0, 6, progress=ep(t, kb + 0.2, 0.5))
    E.foco(c, t, kcc, 0.5, lambda a: E.numero(c, "272", xv, y + 325, s, "g", ERRADO, a))
    E.frase(c, t, lerp(kcc, kd, 0.2), [("multiplicou", "i", 76), ("por", "i", 76), ("2", "g", 76, ERRADO)], xp, 360, passo=0.2)
    E.frase(c, t, lerp(kcc, kd, 0.55), [("e", "i", 76), ("valia", "i", 76), ("20", "g", 76, CERTO)], xp, 470, passo=0.2)
    E.frase(c, t, kd, [("quase", "i", 68), ("todo", "i", 68), ("o", "i", 68), ("bloco", "g", 60, ERRADO), ("grande", "g", 60, ERRADO), ("sumiu", "i", 68)], xp, 600, passo=0.2)
    fim = C["s12.end"]
    E.frase(c, t, lerp(kd, fim, 0.42), [("o", "i", 68), ("zero", "g", 60, COR), ("guarda", "i", 68), ("a", "i", 68), ("casa", "i", 68), ("das", "i", 68), ("unidades", "i", 68)], xp, 740, passo=0.2)
    E.frase(c, t, lerp(kd, fim, 0.72), [("e", "i", 68), ("empurra", "i", 68), ("o", "i", 68), ("resto", "i", 68), ("para", "i", 68), ("as", "i", 68), ("dezenas", "g", 60)], xp, 840, passo=0.14)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def tamanho():
        ka, kb, kcc, kd, ke = C["s13.a"], C["s13.b"], C["s13.c"], C["s13.d"], C["s13.e"]
        E.frase(c, t, C["s13"] + 0.1, [("agora,", "i", 76, CLARO), ("o", "i", 76, CLARO), ("atalho:", "i", 76, CLARO)], W / 2, 150, "center", passo=0.1)
        E.frase(c, t, ka, [("confira", "i", 120, CLARO), ("pelo", "i", 120, CLARO), ("tamanho", "g", 110, BR)], W / 2, 300, "center", passo=0.16)
        E.frase(c, t, lerp(ka, kb, 0.5), [("o", "i", 72, CLARO), ("redondo", "g", 64, BR), ("mais", "i", 72, CLARO), ("perto", "i", 72, CLARO)], W / 2, 420, "center", passo=0.2)
        for yy, tk, s in ((590, kb, "34"), (760, kcc, "26")):
            E.foco(c, t, tk, 0.5, lambda a, yy=yy, s=s: E.centro(c, s, 340, yy + 45, 130, "g", BR, a))
            q = ep(t, tk + 0.3, 0.4)
            if q > 0:
                M.arrow(c, 470, yy, 640, yy, CLARO, q, 6, 20, q)
            E.foco(c, t, tk + 0.5, 0.5, lambda a, yy=yy: E.centro(c, "30", 780, yy + 45, 130, "g", CLARO, a))
        xr = 1020
        E.foco(c, t, kd, 0.5, lambda a: E.escreve(c, "3 × 3 =", xr, 610, 90, "g", BR, a))
        E.foco(c, t, lerp(kd, ke, 0.4), 0.5, lambda a: E.escreve(c, "9", xr + E.larg("3 × 3 = ", "g", 90), 610, 90, "g", CLARO, a))
        E.frase(c, t, lerp(kd, ke, 0.55), [("um", "i", 72, CLARO), ("zero", "g", 66, BR), ("de", "i", 72, CLARO), ("cada", "i", 72, CLARO), ("30", "g", 66, BR)], xr, 720, passo=0.18)
        E.foco(c, t, ke, 0.5, lambda a: E.escreve(c, "900", xr, 900, 190, "g", CLARO, a))
    E.saida(c, t, C["s14"] - 0.1, tamanho)
    if t >= C["s14"]:
        ka, kb, kcc, kd = C["s14.a"], C["s14.b"], C["s14.c"], C["s14.d"]
        E.foco(c, t, ka, 0.5, lambda a: E.selo(c, 300, 240, 72, True, a))
        E.frase(c, t, ka + 0.1, [("884", "g", 100, BR), ("está", "i", 92, CLARO), ("perto", "i", 92, CLARO), ("de", "i", 92, CLARO), ("900", "g", 100, BR)], 410, 272, passo=0.3)
        E.foco(c, t, kb, 0.5, lambda a: E.selo(c, 300, 410, 72, False, a))
        E.frase(c, t, kb + 0.1, [("272,", "g", 100, BR), ("nem", "i", 92, CLARO), ("de", "i", 92, CLARO), ("longe", "i", 92, CLARO)], 410, 442, passo=0.25)
        E.frase(c, t, kcc, [("arredondar", "g", 68, BR), ("muda", "i", 76, CLARO), ("pouco", "i", 76, CLARO), ("cada", "i", 76, CLARO), ("número", "i", 76, CLARO)], W / 2, 600, "center", passo=0.2)
        E.frase(c, t, lerp(kcc, kd, 0.55), [("muda", "i", 76, CLARO), ("pouco", "i", 76, CLARO), ("o", "i", 76, CLARO), ("resultado", "g", 68, BR)], W / 2, 695, "center", passo=0.2)
        E.frase(c, t, kd, [("não", "g", 66, BR), ("compensa", "g", 66, BR), ("com", "i", 72, CLARO), ("opções", "i", 72, CLARO), ("muito", "i", 72, CLARO), ("próximas", "i", 72, CLARO)], W / 2, 840, "center", passo=0.25)
        E.frase(c, t, lerp(kd, C["s14.end"], 0.72), [("arme", "g", 76, BR), ("a", "g", 76, BR), ("conta", "g", 76, BR)], W / 2, 950, "center", passo=0.2)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s15"] + 0.1, [("hora", "i", 72, COR), ("de", "i", 72, COR), ("testar", "i", 72, COR)], XE, 200)
    E.frase(c, t, lerp(C["s15"], C["s15.a"], 0.5), [("um", "i", 92), ("mercado", "i", 92), ("recebeu", "i", 92)], XE, 400, passo=0.25)
    E.frase(c, t, C["s15.a"], [("27", "g", 104, COR), ("caixas", "g", 92)], XE, 530, passo=0.2)
    E.frase(c, t, C["s15.b"], [("com", "i", 92), ("38", "g", 104, COR), ("latas", "g", 92), ("cada", "i", 92)], XE, 660, passo=0.2)
    E.frase(c, t, C["s15.c"], [("quantas", "i", 100), ("latas", "g", 90, COR), ("no", "i", 100), ("total?", "g", 90, COR)], XE, 850, passo=0.22)
    E.relogio(c, t, C["s16.a"], 1490, 400, 200)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    x7 = {x: C["s17." + x] for x in "abcdef"}
    x8 = {x: C["s18." + x] for x in "abcdefghij"}
    xv, y0, sz, xp = 700, 300, 106, 1040
    t26 = lerp(x7["e"], x7["f"], 0.6)
    t16 = x8["c"]
    t7 = x8["e"] + 0.9
    t1 = lerp(x8["g"], x8["h"], 0.6)
    t2 = lerp(x8["h"], x8["i"], 0.3)
    t10 = lerp(x8["i"], x8["j"], 0.75)
    E.frase(c, t, C["s17"] + 0.1, [("vamos", "i", 72), ("lá", "i", 72, COR)], W / 2, 110, "center")
    E.conta_mult(c, t, 38, 27, (x7["a"], x7["a"] + 0.9), [[x7["c"], t26, t26 + 0.25], [t16, t7]], xv, y0, sz, tz=(x8["a"],),
                 tr=(t1, t2, t10, t10 + 0.2), tsoma=lerp(x8["f"], x8["g"], 0.6),
                 vai=[(1, "5", x7["c"] + 0.5, t26), (1, "1", x8["c"] + 0.5, t7)])

    def fala17():
        lin(c, t, lerp(C["s17"], x7["b"], 0.72), "1ª linha, vezes 7", xp, 280, 66, "g", COR)
        igual(c, t, x7["b"], lerp(x7["b"], x7["c"], 0.6), "7 × 8 =", "56", xp, 400, 76)
        lin(c, t, x7["c"], "escreva o 6, e o 5 sobe", xp, 500, 60)
        igual(c, t, x7["d"], lerp(x7["d"], x7["e"], 0.6), "7 × 3 =", "21", xp, 620, 76)
        igual(c, t, x7["e"] - 1.0, t26, "com o 5 que subiu:", "26", xp, 720, 60)
        lin(c, t, x7["f"], "266", xp, 850, 96, "g", COR)
    E.saida(c, t, C["s18"] - 0.1, fala17)

    def fala18a():
        lin(c, t, C["s18"] + 0.1, "2ª linha, vezes 20", xp, 280, 66, "g", COR)
        lin(c, t, x8["a"], "o zero primeiro", xp, 380, 66, "b", COR)
        igual(c, t, x8["b"], lerp(x8["b"], x8["c"], 0.6), "2 × 8 =", "16", xp, 500, 76)
        lin(c, t, x8["c"], "escreva o 6, e o 1 sobe", xp, 600, 60)
        igual(c, t, x8["d"], lerp(x8["d"], x8["e"], 0.6), "2 × 3 =", "6", xp, 720, 76)
        igual(c, t, x8["e"] - 1.0, x8["e"], "com o 1 que subiu:", "7", xp, 820, 60)
        lin(c, t, x8["f"], "760", xp, 940, 96, "g", COR)
    if t >= C["s18"]:
        E.saida(c, t, x8["g"] - 1.1, fala18a)
    if t >= x8["g"] - 1.0:
        lin(c, t, x8["g"] - 0.9, "some as linhas", xp, 280, 66, "g", COR)
        igual(c, t, x8["g"], t1, "6 + 0 =", "6", xp, 390, 72)
        igual(c, t, x8["h"], t2, "6 + 6 =", "12: fica o 2, vai um", xp, 490, 60)
        igual(c, t, x8["i"], lerp(x8["i"], x8["j"], 0.35), "2 + 7 =", "9", xp, 600, 72)
        igual(c, t, lerp(x8["i"], x8["j"], 0.45), t10, "com o 1 que veio:", "10", xp, 700, 60)
        bola_txt(c, t, x8["j"], "1.026", 1270, 870, 124, 72)
        E.frase(c, t, x8["j"] + 0.4, [("latas", "i", 80)], 1420, 895)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s19"], [("resumindo", "i", 92, COR)], W / 2, 210, "center")
        for i, (k, s) in enumerate((("s19.a", "uma linha para as unidades"), ("s19.b", "outra para as dezenas, com zero"), ("s19.c", "some as linhas"))):
            y = 390 + i * 190
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 260, y - 24, 56, a=a),
                                                         E.centro(c, str(i + 1), 260, y - 1, 64, "g", E.SOBRE, a)))
            E.frase(c, t, C[k] + 0.1, [(s, "g", 70)], 350, y)
    E.saida(c, t, C["s20"] - 0.1, resumo)
    if t < C["s20"]:
        return
    E.frase(c, t, C["s20"] + 0.1, [("próxima", "i", 84), ("aula", "i", 84)], XE, 280)
    E.frase(c, t, C["s20.a"], [("dividir", "g", 150, COR)], XE, 430)
    E.frase(c, t, C["s20.a"] + 0.4, [("por", "i", 92), ("um", "i", 92), ("algarismo", "g", 84)], XE, 545, passo=0.15)
    E.frase(c, t, C["s20.b"], [("o", "i", 84), ("resto", "g", 76, COR)], XE, 660, passo=0.2)
    E.frase(c, t, C["s20.c"], [("e", "i", 84), ("a", "i", 84), ("prova", "g", 76, COR), ("real", "g", 76, COR)], XE + 260, 660, passo=0.15)
    E.foco(c, t, C["s20.d"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1440, 710, 76, estilo="g", a=a, cor=E.SOBRE))
    p = ease_io(prog(t, C["s20.d"] + 0.3, 0.8))
    E.cursor(c, lerp(1770, 1570, p), lerp(960, 735, p), ep(t, C["s20.d"] + 0.2, 0.4))
    E.frase(c, t, C["s20.e"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 900, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, blocos=b_blocos, conta=b_conta, conferir=b_conferir, erro=b_erro, atalho=b_atalho,
              questao=b_questao, resposta=b_resposta, fim=b_fim)
