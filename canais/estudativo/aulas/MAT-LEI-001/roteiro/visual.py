"""Visual — Estudativo · MAT-LEI-001: achar a pergunta e os dados úteis.

Linguagem da trilha Leitura de Problemas (as peças abaixo de "linguagem da trilha" servem a todas as aulas MAT-LEI):
- enunciado(): o problema num cartão branco com fio da cor da matéria. Os números são escritos em grotesca; a pergunta fica numa
  linha própria. marca = marca-texto da cor da matéria (dado útil), aponta = caixa pontilhada (dado em dúvida),
  risca = traço vermelho e número cinza (dado que não entra na conta).
- onibus() e pessoa(): ícones simples para a quantidade que só existe inteira.
Todo instante vem de C[...] (marcadores do roteiro) ou de pal() (a palavra na voz real)."""
import json
from pathlib import Path
import re
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Leitura de Problemas")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-LEI-001_achar_a_pergunta_e_os_dados_uteis.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("conta", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
# as contas da aula, conferidas
assert 7 * 40 == 280 and 292 - 280 == 12 and 120 // 40 == 3 and 292 / 40 == 7.3 and 8 * 40 == 320 and 320 >= 292
assert 50 // 3 == 16 and 17 * 3 == 51 and 16 * 3 == 48
assert 45 / 4 == 11.25 and 11 * 4 == 44 and 45 - 44 == 1 and 12 * 4 == 48


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- instante de uma palavra na voz ----------------
_T = json.loads((Path(__file__).resolve().parents[1] / "audio" / "tempos.json").read_text(encoding="utf-8"))
_TOK = {s["id"]: (s["start"], s["tokens"]) for s in _T["scenes"]}


def pal(sid, palavra, n=1):
    """instante em que a n-ésima ocorrência de `palavra` começa na cena sid"""
    st, toks = _TOK[sid]
    k = 0
    for tk in toks:
        if tk["disp"].lower().strip(".,:;!?") == palavra:
            k += 1
            if k == n:
                return st + tk["t0"]
    raise KeyError((sid, palavra, n))


# ---------------- peças gerais ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    """uma frase, palavra a palavra, no mesmo estilo"""
    return [(w, est, size, cor) for w in txt.split()]


def fcen(c, t, t0, s, cx, y, size, cor=None):
    E.formula_em(c, t, t0, s, cx, y, size, "g", cor, "center")


def bola_txt(c, t, t0, s, cx, cy, r, size, cor=None):
    """o resultado na esfera"""
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r, cor, a), centro(c, s, cx, cy + size * 0.36, size, "g", M.on(cor or E.COR), a)))


# ---------------- linguagem da trilha Leitura de Problemas ----------------
_PEDACO = re.compile(r"\[([^|\]]+)\|(\w+)\]")


def _tokens(txt):
    """'Uma escola tem [8 turmas|tur].' -> [('Uma', None), ('escola', None), ('tem', None), ('8 turmas', 'tur'), ('.', None)]"""
    out, i = [], 0
    for m in _PEDACO.finditer(txt):
        out += [(w, None) for w in txt[i:m.start()].split()]
        out.append((m.group(1), m.group(2)))
        i = m.end()
    out += [(w, None) for w in txt[i:].split()]
    return out


def _layout(linha, x, size, pergunta):
    """x de cada pedaço da linha; pontuação cola no pedaço anterior"""
    pos, xx = [], x
    for j, (s, k) in enumerate(linha):
        est = "b" if (k or pergunta) else "i"
        sz = size * 0.9 if est == "b" else size
        if j and not s[0] in ".,:;?!":
            xx += size * 0.25
        w = E.larg(s, est, sz)
        pos.append((s, k, est, sz, xx, xx + w))
        xx += w
    return pos


def enunciado(c, t, x, y, w, linhas, size=60, dy=None, t_card=None, marca=None, risca=None, aponta=None):
    """o problema num cartão. linhas = [(t0, "texto com [número|chave]"[, True se for a pergunta])].
    marca / risca / aponta = {chave: instante}; a chave "q" marca a pergunta inteira. Devolve {chave: (x0, x1, base)}"""
    marca, risca, aponta = marca or {}, risca or {}, aponta or {}
    dy = dy or size * 1.62
    pad = size * 0.85
    h = pad * 2 + size * 1.05 + dy * (len(linhas) - 1)
    t_card = linhas[0][0] - 0.3 if t_card is None else t_card

    def cartao(a):
        r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 26, 26)
        s = skia.Paint(AntiAlias=True, Color=M.hexc("#000000", 0.10 * a))
        s.setMaskFilter(skia.MaskFilter.MakeBlur(skia.kNormal_BlurStyle, 18))
        c.save(); c.translate(6, 14); c.drawRRect(r, s); c.restore()
        c.drawRRect(r, M.paint(BR, a))
        c.save(); c.clipRRect(r, True)
        c.drawRect(skia.Rect.MakeXYWH(x, y, 14, h), M.paint(E.COR, a))
        c.restore()
    E.foco(c, t, t_card, 0.5, cartao, blur=8)
    onde = {}
    for i, ln in enumerate(linhas):
        t0, txt = ln[0], ln[1]
        pergunta = len(ln) > 2 and ln[2]
        base = y + pad + size * 0.78 + i * dy
        pos = _layout(_tokens(txt), x + pad + 14, size, pergunta)
        if pergunta:
            onde["q"] = (pos[0][4], pos[-1][5], base)
        for s, k, est, sz, x0, x1 in pos:
            if k:
                onde[k] = (x0, x1, base)
        if t < t0:
            continue
        # marca-texto atrás dos pedaços úteis
        for k, (x0, x1, b_) in list(onde.items()):
            if b_ != base or k not in marca or t < marca[k]:
                continue
            p = ease_io(prog(t, marca[k], 0.45))
            M.rrect(c, x0 - 12, base - size * 0.8, (x1 - x0 + 24) * p, size * 1.08, 12, E.COR, 0.16)

        def texto(a, pos=pos, pergunta=pergunta):
            for s, k, est, sz, x0, x1 in pos:
                kk = "q" if pergunta else k
                cor = TINTA
                if kk and kk in marca and t >= marca[kk]:
                    cor = COR
                if kk and kk in risca and t >= risca[kk] + 0.2:
                    cor = CINZA
                E.escreve(c, s, x0, base, sz, est, cor, a)
        E.foco(c, t, t0, 0.5, texto, sobe=10)
    for k, ta in aponta.items():
        if k in onde and t >= ta and (k not in risca or t < risca[k] + 0.4):
            x0, x1, b_ = onde[k]
            q = ep(t, ta, 0.35) * (1 - ep(t, risca.get(k, 1e9), 0.4))
            E.caixa_pontilhada(c, x0 - 14, b_ - size * 0.86, x1 - x0 + 28, size * 1.16, q, ERRADO, prog_=ep(t, ta, 0.35))
    for k, tr in risca.items():
        if k in onde and t >= tr:
            x0, x1, b_ = onde[k]
            E.risco(c, x0 - 10, b_ - size * 0.3, x1 + 10, b_ - size * 0.3, t, tr, ERRADO, 8)
    return onde


def onibus(c, x, y, w, cor=None, a=1.0, frac=1.0, rotulo=None):
    """ônibus de lado; (x, y) = canto de cima à esquerda; frac < 1 corta o ônibus (o pedaço que não existe)"""
    if a <= 0:
        return
    cor = cor or E.COR
    h = w * 0.5
    c.save()
    c.clipRect(skia.Rect.MakeXYWH(x - 4, y - 4, w * frac + 4, h + w * 0.2))
    M.rrect(c, x, y, w, h, w * 0.08, cor, a)
    for i in range(4):
        M.rrect(c, x + w * 0.06 + i * w * 0.225, y + h * 0.14, w * 0.18, h * 0.34, 6, BR, 0.85 * a)
    c.drawRect(skia.Rect.MakeXYWH(x, y + h * 0.62, w, h * 0.06), M.paint(BR, 0.35 * a))
    for fx in (0.22, 0.78):
        c.drawCircle(x + w * fx, y + h, w * 0.085, M.paint(TINTA, a))
        c.drawCircle(x + w * fx, y + h, w * 0.035, M.paint(CINZA, a))
    if rotulo:
        centro(c, rotulo, x + w / 2, y + h * 0.9, w * 0.2, "g", BR, a)
    c.restore()
    if frac < 1:
        M.line(c, x + w * frac, y - 10, x + w * frac, y + h + w * 0.12, ERRADO, a, 5, dash=[10, 8])


def pessoa(c, cx, base, h, cor=TINTA, a=1.0):
    """bonequinho de pé, com os pés em base"""
    if a <= 0:
        return
    c.drawCircle(cx, base - h * 0.84, h * 0.15, M.paint(cor, a))
    M.rrect(c, cx - h * 0.17, base - h * 0.64, h * 0.34, h * 0.64, h * 0.12, cor, a)


def lista(c, t, C, ini, itens, n_txt):
    """'você só precisa de N coisas' com as caixas pontilhadas"""
    E.frase(c, t, C[ini] + 0.5, ps("você só precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C[itens[0][0]] - 0.4, 0.5, lambda a: E.escreve(c, n_txt, XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C[itens[0][0]] - 0.25, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 960, 800
    y0, dy = (250, 280) if len(itens) == 2 else (170, 240)
    for i, (k, l1, l2) in enumerate(itens):
        y = y0 + i * dy
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 196, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 60)], x + 44, y + 84)
        E.frase(c, t, C[k] + 0.3, [(l2, "g", 60, COR)], x + 44, y + 160)
    py = y0 + 170
    for i, (k, _, _) in enumerate(itens[1:], 1):
        py = lerp(py, y0 + i * dy + 170, ease_io(prog(t, C[k] - 0.35, 0.5)))
    E.cursor(c, x + w - 30, py, ep(t, C[itens[0][0]], 0.4))


# ---------------- gancho ----------------
OX, OW, OG = 196, 190, 210  # ônibus: primeiro x, largura, passo


def b_gancho(c, t, C, b):
    a1, b1, c1, d1 = C["s01.a"], C["s01.b"], C["s01.c"], C["s01.d"]

    def cena():
        E.linha(c, t, [("292", "g", 120, TINTA, a1), ("pessoas", "i", 104, TINTA, a1 + 0.4), ("·", "g", 104, CINZA, b1 - 0.3),
                       ("40", "g", 120, COR, b1), ("por ônibus", "i", 104, TINTA, b1 + 0.3)], W / 2, 220, "center")
        E.linha(c, t, [("292 ÷ 40 =", "g", 150, TINTA, pal("s01", "conta")), ("7,3", "g", 150, COR, c1)], W / 2, 470, "center")
        for i in range(8):
            fr_ = 1.0 if i < 7 else 0.3
            ti = c1 + 0.4 + 0.1 * i + (0.4 if i == 7 else 0)
            E.foco(c, t, ti, 0.45, lambda a, i=i, fr_=fr_: onibus(c, OX + i * OG, 640, OW, a=a, frac=fr_))
        xp = OX + 7 * OG
        q = ep(t, d1, 0.4)
        E.caixa_pontilhada(c, xp - 18, 618, OW * 0.3 + 36, 160, q, ERRADO, prog_=q)
        E.linha(c, t, [("ninguém contrata", "i", 88, TINTA, pal("s01", "ninguém")), ("0,3", "g", 96, ERRADO, d1),
                       ("de ônibus", "i", 88, ERRADO, d1 + 0.3)], W / 2, 920, "center")
    E.saida(c, t, C["s02"] - 0.1, cena)
    if t >= C["s02"]:
        ta, tb = C["s02.a"], C["s02.b"]
        E.foco(c, t, tb - 0.2, 0.7, lambda a: E.bola(c, 1500, 540, 250 * ease_back(prog(t, tb - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, ps("até o fim desta aula", "i", 86), XE, 290, passo=0.12)
        E.frase(c, t, pal("s02", "achar"), ps("achar a", "i", 86) + [("pergunta", "g", 92, COR)], XE, 450, passo=0.12)
        E.frase(c, t, pal("s02", "separar"), ps("separar os", "i", 86) + [("números", "g", 92, COR)], XE, 590, passo=0.12)
        E.frase(c, t, pal("s02", "resposta"), ps("e dar uma resposta", "i", 80), XE, 730, passo=0.1)
        E.frase(c, t, pal("s02", "faz"), [("que faz sentido", "g", 86, COR)], XE, 850, passo=0.1)
        E.foco(c, t, tb + 0.1, 0.5, lambda a: (centro(c, "+ atalho", 1500, 525, 80, "g", E.SOBRE, a),
                                               centro(c, "de prova", 1500, 610, 80, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    lista(c, t, C, "s03", (("s03.a", "escolher a conta", "pela história"), ("s03.b", "continuar a divisão", "depois da vírgula")), "2")
    E.frase(c, t, pal("s03", "se"), ps("faltou alguma?", "i", 58, COR) + ps("procure no canal", "i", 58), 960, 1000, "left", 0.12)


# ---------------- passo 1: a pergunta primeiro ----------------
LINHAS = ("Uma escola tem [8 turmas|tur].", "Para o passeio, se inscreveram [292 pessoas|pes].", "O passeio dura [6 horas|hor],",
          "a entrada custa [R$ 15|rea],", "e cada ônibus leva [40 passageiros|pas].", "Quantos ônibus a escola precisa contratar?")
CX, CY, CW = 250, 120, 1420


def linhas_escola(C):
    return [(C["s05.a"], LINHAS[0]), (C["s05.b"], LINHAS[1]), (C["s05.c"], LINHAS[2]), (C["s05.d"], LINHAS[3]),
            (C["s05.e"], LINHAS[4]), (C["s06.b"], LINHAS[5], True)]


def b_pergunta(c, t, C, b):
    a4, b4 = C["s04.a"], C["s04.b"]

    def longo():
        # um texto comprido: linhas cinza; o olho desce até a pergunta, lá no fim
        x, y, w = 250, 170, 760
        E.foco(c, t, C["s04"] + 0.3, 0.5, lambda a: M.rrect(c, x, y, w, 760, 26, BR, a, shadow=True))
        larg_ = (0.92, 0.85, 0.95, 0.7, 0.9, 0.88, 0.6, 0.93, 0.8, 0.55)
        sobe = ease_io(prog(t, b4 + 0.3, 0.8))
        for i, f in enumerate(larg_):
            ti = C["s04"] + 0.4 + i * 0.12
            ultima = i == len(larg_) - 1
            yy = lerp(y + 60 + i * 68, y + 60, sobe) if ultima else y + 60 + i * 68 + (68 * sobe if i else 68 * sobe)
            cor = (E.COR if t >= b4 else TINTA2) if ultima else FIO
            E.foco(c, t, ti, 0.4, lambda a, yy=yy, f=f, cor=cor: M.rrect(c, x + 50, yy, (w - 100) * f, 26, 13, cor, a), blur=4)
        # o olho que lê do começo ao fim
        if pal("s04", "quem") <= t < b4:
            q = ease_io(prog(t, pal("s04", "quem"), a4 - pal("s04", "quem")))
            E.cursor(c, x + w - 40, lerp(y + 60, y + 60 + 9 * 68, q), ep(t, pal("s04", "quem"), 0.3))
        E.foco(c, t, b4 + 0.9, 0.4, lambda a: E.pilula(c, "a pergunta", x + w / 2, y - 10, 46, "g", a=a, cor=E.SOBRE))
        xr = 1110
        E.frase(c, t, C["s04"] + 0.4, ps("problema de prova", "i", 76), xr, 300, passo=0.1)
        E.frase(c, t, pal("s04", "longo"), [("é longo", "g", 80)], xr, 400)
        E.frase(c, t, a4, [("cansado", "g", 76, ERRADO)] + ps("e", "i", 76) + [("confuso", "g", 76, ERRADO)], xr, 560, passo=0.25)
        E.frase(c, t, b4, ps("leia a", "i", 84), xr, 740)
        E.frase(c, t, b4 + 0.3, [("pergunta", "g", 92, COR)], xr, 850)
        E.frase(c, t, b4 + 0.6, [("primeiro", "g", 92, COR)], xr, 960)
    E.saida(c, t, C["s05"] - 0.1, longo)
    if t < C["s05"] - 0.1:
        return
    E.frase(c, t, C["s05"], ps("o problema inteiro", "i", 58, TINTA2), CX, 90, passo=0.1)
    onde = enunciado(c, t, CX, CY + 20, CW, linhas_escola(C), size=60, marca={"q": C["s06.c"]})
    a6 = C["s06.a"]
    if a6 <= t < C["s06.c"] + 0.5:
        E.cursor(c, CX + CW - 70, CY + 20 + 51 + 5 * 97 + 30, ep(t, a6, 0.3) * (1 - ep(t, C["s06.c"], 0.4)))
    E.foco(c, t, C["s06.c"] + 0.2, 0.5, lambda a: E.pilula(c, "procuro: um número de ônibus", W / 2, 990, 56, "g", a=a, cor=E.SOBRE))


# ---------------- passo 2: marcar os dados úteis ----------------
def b_dados(c, t, C, b):
    a7, b7, c7 = C["s07.a"], C["s07.b"], C["s07.c"]
    a8, b8, c8, d8 = C["s08.a"], C["s08.b"], C["s08.c"], C["s08.d"]
    enunciado(c, t, CX, CY + 20, CW, linhas_escola(C), size=60, t_card=C["s07"] - 9,
              marca={"q": C["s06.c"], "pes": b7, "pas": c7}, aponta={"tur": a8, "hor": b8, "rea": c8}, risca={"tur": d8, "hor": d8 + 0.15, "rea": d8 + 0.3})
    E.saida(c, t, a7 - 0.2, lambda: E.pilula(c, "procuro: um número de ônibus", W / 2, 990, 56, "g", cor=E.SOBRE))

    def passo2():
        E.frase(c, t, a7, ps("marque só o que", "i", 60) + [("a pergunta usa", "g", 60, COR)], W / 2, 1005, "center", 0.1)
    E.saida(c, t, a8 - 0.2, passo2)
    tp = pal("s08", "prova")
    E.saida(c, t, tp - 0.2, lambda: E.frase(c, t, pal("s08", "nenhum"), ps("não mudam o número de ônibus", "i", 60, ERRADO), W / 2, 1005, "center", 0.1))
    E.frase(c, t, tp, [("número a mais", "g", 60, ERRADO)] + ps("de propósito", "i", 62), W / 2, 1005, "center", 0.12)


# ---------------- passo 3: a conta e o sentido ----------------
def b_conta(c, t, C, b):
    a9, b9, c9 = C["s09.a"], C["s09.b"], C["s09.c"]

    def divisao():
        E.frase(c, t, C["s09"] + 0.3, ps("passo 3:", "i", 66, TINTA2) + [("a conta", "g", 66, COR)], XE, 150, passo=0.12)
        E.frase(c, t, pal("s09", "repartir"), ps("292 pessoas em grupos de 40:", "i", 62), XE, 250, passo=0.08)
        E.frase(c, t, a9, [("divisão", "g", 66, COR)], XE + 820, 250)
        D = E.dividir("292", 40, 1)
        E.conta_div(c, t, D, [b9, c9], [pal("s09", "vira"), c9 + 0.4], pal("s09", "quantos"), 220, 470, 130,
                    tv=pal("s09", "continuando"), ts=[pal("s09", "sobram")])
        xr = 1520
        fcen(c, t, pal("s09", "sete", 2), "7 × 4 = 28", xr, 400, 66, TINTA2)
        fcen(c, t, pal("s09", "duzentos", 2), "7 × 40 = 280", xr, 520, 76)
        fcen(c, t, pal("s09", "sobram"), "292 − 280 = 12", xr, 640, 76)
        fcen(c, t, c9, "120 ÷ 40 = 3", xr, 760, 76)
        bola_txt(c, t, pal("s09", "resultado") + 0.3, "7,3", xr, 910, 92, 84)
    E.saida(c, t, C["s10"] - 0.1, divisao)
    if t < C["s10"]:
        return
    a0, b0, c0, d0 = C["s10.a"], C["s10.b"], C["s10.c"], C["s10.d"]
    a1, b1 = C["s11.a"], C["s11.b"]
    E.frase(c, t, a0 - 0.6, ps("a pergunta pede", "i", 76) + [("ônibus", "g", 80, COR)] + ps("e ônibus vem", "i", 76) + [("inteiro", "g", 80, COR)],
            W / 2, 170, "center", 0.12)
    ox, ow, og = 150, 180, 206
    for i in range(7):
        E.foco(c, t, b0 + 0.08 * i, 0.4, lambda a, i=i: onibus(c, ox + i * og, 300, ow, a=a, rotulo="40"))
    # os 12 que sobram, na calçada; depois chega o 8º ônibus
    t8 = pal("s11", "mais")
    xc = ox + 7 * og + ow / 2
    chega = ease_io(prog(t, t8, 0.8))
    for k in range(12):
        px, py = xc - 60 + (k % 4) * 40, 400 + (k // 4) * 82
        E.foco(c, t, d0 + 0.05 * k, 0.3, lambda a, px=px, py=py: pessoa(c, px, py, 68, ERRADO, a * (1 - chega)), blur=4)
    if t >= t8:
        onibus(c, lerp(W + 40, ox + 7 * og, chega), 300, ow, CERTO, ep(t, t8, 0.3), rotulo="12")
    fcen(c, t, c0, "7 × 40 = 280 pessoas", 800, 640, 84)
    E.saida(c, t, a1 - 0.3, lambda: E.frase(c, t, d0, [("12 pessoas", "g", 76, ERRADO)] + ps("na calçada", "i", 76, ERRADO), 800, 750, "center", 0.12))
    E.foco(c, t, t8 + 0.3, 0.5, lambda a: E.escreve(c, "+1", ox + 7 * og + ow - 30, 290, 64, "g", CERTO, a))
    bola_txt(c, t, a1, "8", 400, 860, 105, 120, CERTO)
    E.frase(c, t, a1 + 0.2, [("ônibus", "g", 76, CERTO)], 535, 890)
    fcen(c, t, b1, "8 × 40 = 320", 1300, 850, 92)
    E.frase(c, t, pal("s11", "trezentos") + 0.5, ps("lugares", "i", 70), 1300, 945, "center")
    E.frase(c, t, pal("s11", "cabe"), [("cabe todo mundo", "g", 64, CERTO)], 1300, 1035, "center")


# ---------------- erro comum ----------------
def b_erro(c, t, C, b):
    a2, b2, c2 = C["s12.a"], C["s12.b"], C["s12.c"]
    tr = pal("s12", "regra", 2)

    def arredonda():
        E.frase(c, t, C["s12"] + 0.4, ps("o erro:", "i", 80) + [("arredondar como decimal", "g", 76, ERRADO)], W / 2, 190, "center", 0.12)
        E.linha(c, t, [("7,3", "g", 170, TINTA, a2), ("→", "g", 150, CINZA, pal("s12", "fica")), ("7", "g", 170, ERRADO, pal("s12", "fica") + 0.3)],
                W / 2, 470, "center")
        E.frase(c, t, pal("s12", "menos"), ps("3 é menos que 5", "i", 60, TINTA2), W / 2, 580, "center", 0.1)
        E.frase(c, t, b2, [("12 pessoas", "g", 80, ERRADO)] + ps("ficam para trás", "i", 80, ERRADO), W / 2, 790, "center", 0.12)
        E.foco(c, t, b2 + 0.8, 0.5, lambda a: E.selo(c, W / 2 + 560, 760, 56, False, a))
    E.saida(c, t, tr - 0.2, arredonda)
    if tr - 0.2 <= t < C["s13"] - 0.1:
        def duas():
            caixas = ((520, tr, "regra do 5", pal("s12", "achar"), "acha o valor mais próximo", pal("s12", "como"), [("preço, medida", "i", 66, TINTA2)]),
                      (1400, pal("s12", "quando"), "coisas inteiras", pal("s12", "quem"), "quem decide é", c2, [("a pergunta", "g", 84, COR)]))
            for x, t0, l1, t2, l2, t3, l3 in caixas:
                p = ep(t, t0, 0.5)
                E.caixa_pontilhada(c, x - 380, 230, 760, 620, p, prog_=p)
                E.frase(c, t, t0, [(l1, "g", 84, COR if x > 1000 else TINTA)], x, 380, "center")
                E.frase(c, t, t2, ps(l2, "i", 62), x, 540, "center", 0.1)
                E.frase(c, t, t3, l3, x, 690, "center", 0.1)
        E.saida(c, t, C["s13"] - 0.2, duas)
    if t < C["s13"] - 0.1:
        return
    a3, b3, c3, d3, e3, f3 = (C[f"s13.{k}"] for k in "abcdef")

    def pacotes():
        E.frase(c, t, C["s13"] + 0.3, ps("às vezes, a pergunta manda", "i", 76) + [("descer", "g", 80, COR)], W / 2, 170, "center", 0.1)
        E.linha(c, t, [("R$ 50", "g", 90, TINTA, a3), ("·", "g", 90, CINZA, pal("s13", "quantos")), ("pacotes de", "i", 86, TINTA, pal("s13", "pacotes")),
                       ("R$ 3", "g", 90, TINTA, pal("s13", "três"))], W / 2, 320, "center")
        E.linha(c, t, [("50 ÷ 3 =", "g", 110, TINTA, b3), ("16,666...", "g", 110, COR, pal("s13", "dezesseis"))], W / 2, 500, "center")
        E.linha(c, t, [("regra do 5:", "i", 70, TINTA2, pal("s13", "regra")), ("17?", "g", 80, TINTA2, pal("s13", "subir"))], W / 2, 620, "center")
        fcen(c, t, pal("s13", "dezessete"), "17 × 3 = 51", 720, 790, 100, ERRADO)
        E.frase(c, t, c3, [("não dá", "g", 80, ERRADO)] + ps("para pagar", "i", 80, ERRADO), 1350, 790, "center", 0.12)
        bola_txt(c, t, d3, "16", 960, 930, 80, 90, CERTO)
        E.frase(c, t, d3 + 0.2, [("pacotes", "g", 64, CERTO)], 1060, 955)
    E.saida(c, t, e3 - 0.2, pacotes)
    if t < e3 - 0.2:
        return
    for x, t0, l1, l2, seta in ((520, e3, "precisa caber", "todo mundo?", "sobe"), (1400, f3, "o dinheiro", "não chega?", "desce")):
        p = ep(t, t0, 0.5)
        E.caixa_pontilhada(c, x - 380, 200, 760, 700, p, prog_=p)
        E.frase(c, t, t0, ps(l1, "i", 80), x, 360, "center", 0.1)
        E.frase(c, t, t0 + 0.4, ps(l2, "i", 80), x, 460, "center", 0.1)
        q = ep(t, pal("s13", seta), 0.5)
        if q > 0:
            y0, y1 = (760, 580) if seta == "sobe" else (580, 760)
            M.arrow(c, x - 170, y0, x - 170, lerp(y0, y1, q), COR, q, 12, 40, 1.0)
        E.foco(c, t, pal("s13", seta), 0.5, lambda a, x=x, seta=seta: E.escreve(c, seta, x - 100, 710, 120, "g", COR, a))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    a4, b4, c4 = C["s14.a"], C["s14.b"], C["s14.c"]
    a5, b5 = C["s15.a"], C["s15.b"]

    def topo():
        E.frase(c, t, C["s14"] + 0.3, ps("agora, o atalho", "i", 70, CLARO), W / 2, 150, "center", 0.1)
        E.frase(c, t, a4, ps("resposta inteira?", "i", 84, CLARO), W / 2, 280, "center", 0.12)
        E.frase(c, t, pal("s14", "troque"), ps("troque a divisão pela", "i", 84, CLARO) + [("tabuada", "g", 90, BR)], W / 2, 400, "center", 0.12)
    E.saida(c, t, a5 - 0.3, topo)

    def reta():
        y = 640
        vx = E.reta(c, t, pal("s14", "procure"), 260, 1600, y, 240, 360, [240, 280, 320, 360], escuro=True, size=54,
                    tm=[pal("s14", "procure") + 0.3, b4, c4, pal("s14", "procure") + 0.4])
        x92 = vx(292)
        tp = pal("s14", "duzentos")
        E.foco(c, t, tp, 0.4, lambda a: (c.drawCircle(x92, y, 18, M.paint(CLARO, a)), centro(c, "292", x92, y - 50, 64, "g", CLARO, a)))
        E.foco(c, t, b4 + 0.3, 0.4, lambda a: centro(c, "7 × 40", vx(280), y + 170, 60, "g", BR, a))
        E.foco(c, t, c4 + 0.3, 0.4, lambda a: centro(c, "8 × 40", vx(320), y + 170, 60, "g", BR, a))
        if t >= pal("s15", "vizinhos"):
            for v in (280, 320):
                q = ep(t, pal("s15", "vizinhos"), 0.4)
                E.caixa_pontilhada(c, vx(v) - 120, y + 110, 240, 90, q, CLARO, prog_=q)
        E.frase(c, t, pal("s15", "pergunta"), ps("e a", "i", 72, CLARO) + [("pergunta escolhe", "g", 72, BR)], W / 2, 980, "center", 0.12)
    E.saida(c, t, b5 - 0.3, reta)
    if t >= a5:
        E.saida(c, t, b5 - 0.3, lambda: E.frase(c, t, a5, ps("dividir é perguntar", "i", 80, CLARO) + [("quantos grupos cabem", "g", 80, BR)], W / 2, 300, "center", 0.12))
    if t >= b5 - 0.2:
        E.foco(c, t, b5, 0.5, lambda a: E.selo(c, 360, 460, 60, False, a))
        E.frase(c, t, b5, ps("não compensa:", "i", 76, CLARO), 460, 430, "left", 0.1)
        E.frase(c, t, b5 + 0.4, ps("divisor difícil de", "i", 76, CLARO) + [("multiplicar de cabeça", "g", 76, BR)], 460, 530, "left", 0.1)
        E.frase(c, t, pal("s15", "faça"), ps("aí,", "i", 90, CLARO) + [("faça a divisão", "g", 96, BR)], W / 2, 780, "center", 0.12)


# ---------------- questão ----------------
def linhas_tinta(C):
    return [(C["s16.a"], "Para pintar [3 cômodos|com], uma pessoa"), (pal("s16", "precisa"), "precisa de [45 litros|lit] de tinta."),
            (C["s16.b"], "A tinta vem em latas de [4 litros|lat],"), (C["s16.c"], "que custam [R$ 120|pre] cada."),
            (C["s16.d"], "A pintura vai levar [2 dias|dia]."), (C["s16.e"], "Quantas latas ela precisa comprar?", True)]


def b_questao(c, t, C, b):
    E.frase(c, t, C["s16"] + 0.2, ps("hora de testar", "i", 64, COR), XE, 110, passo=0.12)
    enunciado(c, t, XE, 160, 1180, linhas_tinta(C), size=58)
    E.relogio(c, t, C["s17.a"], 1580, 440, 170)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    a8, b8, c8 = C["s18.a"], C["s18.b"], C["s18.c"]
    a9, b9, c9, d9 = C["s19.a"], C["s19.b"], C["s19.c"], C["s19.d"]
    tr = pal("s18", "risque")

    def cartao():
        enunciado(c, t, XE, 160, 1180, linhas_tinta(C), size=58, t_card=C["s18"] - 9,
                  marca={"q": a8, "lit": b8, "lat": pal("s18", "quatro")},
                  aponta={"com": c8, "pre": pal("s18", "cento"), "dia": pal("s18", "dois")}, risca={"com": tr, "pre": tr + 0.15, "dia": tr + 0.3})
        E.foco(c, t, a8 + 0.2, 0.5, lambda a: E.pilula(c, "procuro: latas", 1600, 300, 56, "g", a=a, cor=E.SOBRE))
    E.saida(c, t, C["s19"] - 0.1, cartao)
    if t < C["s19"] - 0.1:
        return
    E.linha(c, t, [("45 ÷ 4 =", "g", 110, TINTA, a9), ("11,25", "g", 110, COR, pal("s19", "onze"))], W / 2, 200, "center")
    E.frase(c, t, pal("s19", "regra"), ps("a regra do 5 mandaria descer", "i", 58, TINTA2), W / 2, 300, "center", 0.08)
    y = 560
    vx = E.reta(c, t, pal("s19", "pela"), 330, 1590, y, 40, 52, [40, 44, 48, 52], size=54, tm=[pal("s19", "pela") + 0.3, b9, c9, pal("s19", "pela") + 0.4])
    x45 = vx(45)
    E.foco(c, t, pal("s19", "pela") + 0.5, 0.4, lambda a: (c.drawCircle(x45, y, 18, M.paint(E.COR, a)), centro(c, "45 L", x45, y - 50, 60, "g", COR, a)))
    E.foco(c, t, b9 + 0.3, 0.4, lambda a: centro(c, "11 latas", vx(44), y + 170, 58, "g", TINTA, a))
    E.foco(c, t, c9 + 0.2, 0.4, lambda a: centro(c, "12 latas", vx(48), y + 170, 58, "g", CERTO, a))
    tf = pal("s19", "falta")
    if t >= tf:
        E.chave(c, vx(44), vx(45), y - 140, ERRADO, ep(t, tf, 0.4), 22)
        E.foco(c, t, tf + 0.2, 0.4, lambda a: centro(c, "falta 1 L", (vx(44) + vx(45)) / 2 - 40, y - 180, 54, "b", ERRADO, a))
    E.frase(c, t, pal("s19", "a", 2), ps("a tinta precisa dar para tudo:", "i", 64), 330, 930, "left", 0.08)
    E.frase(c, t, pal("s19", "sobe"), [("sobe", "g", 72, COR)], 1180, 930)
    bola_txt(c, t, d9, "12", 1560, 900, 90, 100, CERTO)
    E.frase(c, t, d9 + 0.2, [("latas", "g", 60, CERTO)], 1670, 925)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s20"] + 0.2, [("resumindo", "i", 92, COR)], W / 2, 200, "center")
        itens = (("s20.a", "pergunta", "primeiro"), ("s20.b", "risque", "o que não serve"), ("s20.c", "confira", "se faz sentido no mundo real"))
        for i, (k, l1, l2) in enumerate(itens):
            y = 380 + i * 200
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 230, y - 30, 56, a=a), centro(c, str(i + 1), 230, y - 7, 64, "g", E.SOBRE, a)))
            E.frase(c, t, C[k] + 0.1, [(l1, "g", 76, COR)] + ps(l2, "i", 74), 320, y, "left", 0.1)
    E.saida(c, t, C["s21"] - 0.1, resumo)
    if t < C["s21"]:
        return
    a1, b1, c1, d1, e1 = (C[f"s21.{k}"] for k in "abcde")
    E.frase(c, t, C["s21"] + 0.2, ps("na próxima aula", "i", 84), XE, 240, passo=0.14)
    E.frase(c, t, pal("s21", "palavras"), [("palavras que", "g", 96, COR)] + ps("mudam a conta", "i", 92), XE, 390, passo=0.12)
    x = XE
    for s, k in (("a mais que", a1), ("do restante", b1), ("no mínimo", c1)):
        w = E.larg(s, "b", 56) + 56 * 1.1
        E.foco(c, t, k, 0.4, lambda a, s=s, x=x, w=w: E.pilula(c, s, x + w / 2, 540, 56, "b", a=a, cor=E.SOBRE))
        x += w + 30
    E.foco(c, t, d1, 0.5, lambda a: E.pilula(c, "Inscreva-se", 1440, 750, 76, estilo="g", a=a, cor=E.SOBRE))
    p = ease_io(prog(t, d1 + 0.3, 0.8))
    E.cursor(c, lerp(1770, 1570, p), lerp(990, 775, p), ep(t, d1 + 0.2, 0.4))
    E.frase(c, t, e1, [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 930, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, pergunta=b_pergunta, dados=b_dados, conta=b_conta, erro=b_erro, atalho=b_atalho,
              questao=b_questao, resposta=b_resposta, fim=b_fim)
