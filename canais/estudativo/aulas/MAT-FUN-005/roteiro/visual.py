"""Visual — Estudativo · MAT-FUN-005: domínio pela fórmula.

Linguagem visual da trilha Funções (MAT-FUN-001 a 004): entrada em índigo (ENT), saída em preto (SAI); o domínio na reta é o
trecho índigo de E.intervalo (bolinha aberta = fica fora, fechada = entra), e a resposta em intervalo sai em índigo.
Nesta aula: os "vilões" do domínio (divisão por zero e raiz quadrada de negativo) são cartões escuros com o símbolo em vermelho;
o lugar que cada vilão vigia (o denominador, o radicando) ganha um realce vermelho na fórmula (realce()).
Peças locais: realce(), vilao(), tx() (símbolos ℝ e cia., que a fonte da casa não tem; a mesma solução da MAT-CON-004)."""
import math
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Matemática", "Funções")
COR, CLARO = E.COR_TEXTO, E.CLARO
ENT, SAI = COR, TINTA
ARQUIVO_FINAL = "estudativo_MAT-FUN-005_dominio_pela_formula.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("regra", "divisao", "raiz", "atalho", "questao", "fim"))
BR = "#FFFFFF"
assert 6 / 2 == 3 and 3 * 2 == 6 and math.sqrt(7 - 3) == 2 and math.sqrt(0) == 0
assert math.isclose(-(8 ** (1 / 3)), -2) and 6 - 2 * 3 == 0 and 6 - 2 * 0 == 6 and -4 + 4 == 0


# ---------------- símbolos de conjunto (a fonte da casa não tem ∈ ⊂ ∪ ∩ ℕ ℤ ℚ ℝ: desenhados aqui) ----------------
_TRACO = dict(g=0.15, b=0.1, m=0.075, i=0.052, s=0.052)
_DESENHA = "∈∉⊂⊄⊃∪∩∅"
_DUPLA = "ℕℤℚℝ"
_FM = skia.FontMgr()
_CM = _FM.makeFromFile("C:/Windows/Fonts/cambria.ttc", 1)


def _f2(size, est):
    f = skia.Font(_CM, size * 1.08)
    f.setSubpixel(True)
    f.setEdging(skia.Font.Edging.kAntiAlias)
    f.setEmbolden(est in "gb")
    return f


def _wsimb(ch, size, est):
    if ch in _DESENHA:
        return size * 0.78
    f = _f2(size, est)
    return f.measureText(ch) + size * 0.04


def _simb(c, ch, x, y, size, est, cor, a):
    sw = size * _TRACO[est]
    if ch in _DUPLA:
        f = _f2(size, est)
        p = M.paint(cor, a)
        if est in "gb":
            p.setStyle(skia.Paint.kStrokeAndFill_Style); p.setStrokeWidth(size * (0.025 if est == "g" else 0.012))
        c.drawString(ch, x + size * 0.02, y, f, p)
        return
    x0, x1 = x + size * 0.1 + sw / 2, x + size * 0.68 - sw / 2
    top, bot = y - size * 0.68 + sw / 2, y - size * 0.02 - sw / 2
    r = (bot - top) / 2
    pa = skia.Path()
    if ch in "∈∉⊂⊄":
        pa.moveTo(x1, top); pa.lineTo(x0 + r, top)
        pa.arcTo(skia.Rect.MakeLTRB(x0, top, x0 + 2 * r, bot), -90, -180, False)
        pa.lineTo(x1, bot)
        if ch in "∈∉":
            pa.moveTo(x0, (top + bot) / 2); pa.lineTo(x1 - sw * 0.3, (top + bot) / 2)
    elif ch == "⊃":
        pa.moveTo(x0, top); pa.lineTo(x1 - r, top)
        pa.arcTo(skia.Rect.MakeLTRB(x1 - 2 * r, top, x1, bot), -90, 180, False)
        pa.lineTo(x0, bot)
    elif ch == "∪":
        rr = (x1 - x0) / 2
        pa.moveTo(x0, top); pa.lineTo(x0, bot - rr)
        pa.arcTo(skia.Rect.MakeLTRB(x0, bot - 2 * rr, x1, bot), 180, -180, False)
        pa.lineTo(x1, top)
    elif ch == "∩":
        rr = (x1 - x0) / 2
        pa.moveTo(x0, bot); pa.lineTo(x0, top + rr)
        pa.arcTo(skia.Rect.MakeLTRB(x0, top, x1, top + 2 * rr), 180, 180, False)
        pa.lineTo(x1, bot)
    elif ch == "∅":
        cx, cy, rr = (x0 + x1) / 2 + size * 0.02, (top + bot) / 2, (bot - top) / 2 + size * 0.02
        pa.addCircle(cx, cy, rr)
        pa.moveTo(cx + rr * 0.95, cy - rr * 1.25); pa.lineTo(cx - rr * 0.95, cy + rr * 1.25)
    if ch in "∉⊄":
        pa.moveTo(x0 + (x1 - x0) * 0.82, top - size * 0.1); pa.lineTo(x0 + (x1 - x0) * 0.18, bot + size * 0.1)
    p = M.paint(cor, a, stroke=sw)
    p.setStrokeCap(skia.Paint.kButt_Cap); p.setStrokeJoin(skia.Paint.kMiter_Join)
    c.drawPath(pa, p)


def _pedacos(s):
    out, cur = [], ""
    for ch in s:
        if ch in _DESENHA or ch in _DUPLA:
            if cur:
                out.append(cur); cur = ""
            out.append(ch)
        else:
            cur += ch
    if cur:
        out.append(cur)
    return out


def tw(s, est, size):
    """largura de um texto que pode ter símbolos de conjunto"""
    return sum(_wsimb(p, size, est) if len(p) == 1 and (p in _DESENHA or p in _DUPLA) else E.larg(p, est, size) for p in _pedacos(s))


def tx(c, s, x, y, size, est="g", cor=None, a=1.0, align="left"):
    """como E.escreve, com ∈ ∉ ⊂ ⊄ ∪ ∩ ℕ ℤ ℚ ℝ; align left/center/right"""
    if a <= 0:
        return
    cor = cor or TINTA
    w = tw(s, est, size)
    x = x - w / 2 if align == "center" else x - w if align == "right" else x
    for p in _pedacos(s):
        if len(p) == 1 and (p in _DESENHA or p in _DUPLA):
            _simb(c, p, x, y, size, est, cor, a)
            x += _wsimb(p, size, est)
        else:
            E.escreve(c, p, x, y, size, est, cor, a)
            x += E.larg(p, est, size)


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças da trilha ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def txe(c, t, t0, s, x, y, size, est="g", cor=None, align="left"):
    E.foco(c, t, t0, 0.5, lambda a: tx(c, s, x, y, size, est, cor, a, align))


def fml(c, t, t0, s, x, y, size, cor=None, align="left"):
    E.formula_em(c, t, t0, s, x, y, size, "g", cor, align)


def _w(s, size):
    return E.formula(None, s, 0, 0, size, a=0)


def realce(c, t, t0, prefixo, tipo, miolo, x, y, size, cor=None, align="left", total=None, d=0.4):
    """moldura vermelha leve no denominador (tipo "f", miolo = (cima, baixo)) ou no radicando (tipo "r", miolo = o de dentro)
    da fórmula prefixo + f{..}{..} / r{..}, escrita em (x, y, size): é o lugar que o vilão vigia"""
    q = ep(t, t0, d)
    if q <= 0:
        return
    if align == "center":
        x -= _w(total, size) / 2
    x0 = x + _w(prefixo, size) if prefixo else x
    if tipo == "f":
        cima, baixo = miolo
        s_ = size * 0.78
        wc, wb = _w(cima, s_), _w(baixo, s_)
        w = max(wc, wb) + size * 0.12
        rx, ry, rw, rh = x0 + (w - wb) / 2 - size * 0.1, y + size * 0.46 - s_ * 0.8, wb + size * 0.14, s_ * 1.02
    else:
        dentro = _w(miolo, size)
        rx, ry, rw, rh = x0 + size * 0.5, y - size * 0.86, dentro + size * 0.16, size * 1.0
    M.rrect(c, rx, ry, rw, rh, size * 0.14, cor or ERRADO, 0.16 * q)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(rx, ry, rw, rh), size * 0.14, size * 0.14), M.paint(cor or ERRADO, q, stroke=4))


def vilao(c, x, y, w, h, simb, txt, a, sub=None, size=56):
    """cartão escuro de um vilão do domínio: símbolo vermelho à esquerda, nome em branco à direita"""
    if a <= 0:
        return
    s = skia.Paint(AntiAlias=True, Color=M.hexc("#000000", 0.25 * a))
    s.setMaskFilter(skia.MaskFilter.MakeBlur(skia.kNormal_BlurStyle, 12))
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x + 8, y + 14, w, h), 30, 30), s)
    M.rrect(c, x, y, w, h, 30, "#1C1C24", a)
    E.formula(c, simb, x + 120, y + h / 2 + 36, 100, "g", ERRADO, a, "center")
    E.escreve(c, txt, x + 240, y + h / 2 + (0 if sub else 20), size, "g", BR, a)
    if sub:
        E.formula(c, sub, x + 240, y + h / 2 + 80, 70, "g", BR, a)


def anel(c, t, t0, X, Y, r=40, cor=ERRADO, largura=6):
    q = ease_out(prog(t, t0, 0.5))
    if q > 0:
        E.arco(c, X, Y, r, -90, 360 * q, cor, largura)


def bola_x(c, t, t0, X, Y, ok, r=34):
    E.foco(c, t, t0, 0.4, lambda a: E.selo(c, X, Y, r, ok, a))


def pingo(c, t, t0, X, Y, cor):
    k = ease_back(prog(t, t0, 0.4))
    if k > 0:
        c.drawCircle(X, Y, 14 * k, M.paint(cor))


RX0, RX1 = 300, 1620  # a reta de sempre


# ---------------- gancho ----------------
F1 = "f(x) = f{1}{x − 2}"


def b_gancho(c, t, C, b):
    def cena1():
        fml(c, t, C["s01.a"], F1, W / 2, 330, 150, align="center")
        realce(c, t, C["s01.a"] + 2.0, "f(x) = ", "f", ("1", "x − 2"), W / 2, 330, 150, ENT, "center", F1)
        E.foco(c, t, C["s01.b"], 0.5, lambda a: E.pilula(c, "x = 2", 400, 660, 66, "g", fundo=ENT, a=a))
        fml(c, t, C["s01.c"], "f{1}{2 − 2} = f{1}{0}", 700, 690, 110)
        a = ep(t, C["s01.d"], 0.5)  # a calculadora
        if a > 0:
            M.rrect(c, 1420, 520, 360, 300, 30, TINTA, a)
            M.rrect(c, 1450, 550, 300, 110, 14, "#1E2A1E", a)
            E.escreve(c, "ERRO", 1490, 640, 80, "g", ERRADO, a)
            for i in range(3):
                for j in range(2):
                    M.rrect(c, 1460 + i * 98, 690 + j * 64, 80, 48, 10, "#3C3C46", a)
        E.frase(c, t, C["s01.e"], [("o", "i", 80), ("2", "g", 84, ENT), ("não", "g", 80, ERRADO), ("pode", "i", 80), ("entrar", "i", 80)], W / 2, 960, "center")
    E.saida(c, t, C["s02"] - 0.1, cena1)
    if t >= C["s02"]:
        E.foco(c, t, C["s02.b"] - 0.2, 0.7, lambda a: E.bola(c, 1480, 540, 290 * ease_back(prog(t, C["s02.b"] - 0.2, 0.7))), blur=0)
        E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 90), XE, 300)
        E.frase(c, t, C["s02.a"] + 1.0, [("domínio", "g", 120, ENT)], XE, 450)
        E.frase(c, t, C["s02.a"] + 1.6, [("pela", "i", 110), ("fórmula", "g", 120)], XE, 580)
        E.frase(c, t, C["s02.a"] + 3.4, [("em", "i", 90), ("intervalo", "g", 90, COR)], XE, 730)
        E.foco(c, t, C["s02.b"] + 0.2, 0.5, lambda a: (E.escreve(c, "+ atalho", 1320, 525, 84, "g", BR, a),
                                                      E.escreve(c, "de prova", 1340, 610, 84, "i", BR, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], [("você", "i", 84), ("precisa", "i", 84), ("de", "i", 84)], XE, 410)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "3", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 900, 860
    itens = (("s03.b", "domínio:", "o que pode entrar"), ("s03.c", "inequação, virando o sinal:", "−2x ≥ −6 → x ≤ 3"),
             ("s03.d", "raiz de negativo:", "r{−4} fora da reta"))
    for i, (k, l1, l2) in enumerate(itens):
        y = 190 + i * 240
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 196, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 60)], x + 44, y + 80)
        fml(c, t, C[k] + 0.3, l2, x + 44, y + 162, 62, COR)
    alvo = [x + w - 30, 190 + 170, 430 + 170, 670 + 170]
    q1, q2 = ease_io(prog(t, C["s03.c"] - 0.35, 0.5)), ease_io(prog(t, C["s03.d"] - 0.35, 0.5))
    E.cursor(c, alvo[0], lerp(lerp(alvo[1], alvo[2], q1), alvo[3], q2), ep(t, C["s03.b"], 0.4))


# ---------------- a regra ----------------
def b_regra(c, t, C, b):
    E.frase(c, t, C["s04"], ps("só a fórmula, sem história", "i", 64, TINTA2), W / 2, 170, "center", 0.1)
    E.frase(c, t, C["s04.a"], [("domínio:", "g", 72, ENT), ("todo", "i", 76), ("real", "g", 72), ("que", "i", 76), ("deixa", "i", 76), ("a", "i", 76),
                               ("conta", "i", 76), ("funcionar", "g", 72)], W / 2, 310, "center", 0.12)

    def exemplos():
        fml(c, t, C["s04.b"], "x + 5", 300, 500, 80)
        fml(c, t, C["s04.b"] + 0.3, "3x", 640, 500, 80)
        fml(c, t, C["s04.b"] + 0.6, "x^2", 880, 500, 80)
        E.foco(c, t, C["s04.b"] + 0.9, 0.4, lambda a: E.pilula(c, "qualquer número entra", 1380, 470, 46, "g", fundo=CERTO, a=a))
    E.saida(c, t, C["s04.c"] - 0.1, exemplos)
    E.frase(c, t, C["s04.c"], [("só", "i", 80), ("2", "g", 90, ERRADO), ("coisas", "i", 80), ("barram", "g", 76, ERRADO)], W / 2, 520, "center")
    E.foco(c, t, C["s04.d"], 0.5, lambda a: vilao(c, 200, 640, 720, 220, "÷ 0", "dividir por zero", a))
    E.foco(c, t, C["s04.e"], 0.5, lambda a: vilao(c, 1000, 640, 720, 220, "r{−}", "raiz de negativo", a))


# ---------------- por que não divide por zero ----------------
def b_zero(c, t, C, b):
    E.frase(c, t, C["s05"], ps("por que não se divide por zero?", "i", 76), W / 2, 190, "center", 0.12)
    fml(c, t, C["s05.a"], "6 ÷ 2 = 3", 300, 400, 110)
    E.frase(c, t, C["s05.a"] + 1.6, [("porque", "i", 70, TINTA2), ("3 × 2 = 6", "g", 76, CERTO)], 1000, 400)
    fml(c, t, C["s05.b"], "6 ÷ 0 = ?", 300, 600, 110, ERRADO)
    E.frase(c, t, C["s05.b"] + 1.6, [("seria", "i", 70, TINTA2), ("? × 0 = 6", "g", 76, ERRADO)], 1000, 600)
    E.frase(c, t, C["s05.c"], [("mas", "i", 80), ("todo", "i", 80), ("número", "i", 80), ("×", "g", 80), ("0", "g", 84), ("=", "g", 80), ("0", "g", 84)],
            W / 2, 820, "center")
    E.foco(c, t, C["s05.d"], 0.5, lambda a: E.pilula(c, "esse número não existe", W / 2, 960, 56, "g", fundo=ERRADO, a=a))


# ---------------- divisão ----------------
F2 = "f{1}{x − 2}"


def b_divisao(c, t, C, b):
    def s06():
        fml(c, t, C["s06.a"], F2, 480, 420, 170, align="center")
        realce(c, t, C["s06.b"], "", "f", ("1", "x − 2"), 480, 420, 170, ERRADO, "center", F2)
        E.foco(c, t, C["s06.b"] + 0.3, 0.4, lambda a: E.escreve(c, "≠ 0", 480 + _w(F2, 170) / 2 + 30, 560, 90, "g", ERRADO, a))
        fml(c, t, C["s06.c"], "x − 2 ≠ 0", 1060, 360, 100)
        E.foco(c, t, C["s06.d"], 0.4, lambda a: E.pilula(c, "+ 2", 1480, 500, 44, "g", fundo=TINTA2, a=a))
        fml(c, t, C["s06.d"], "x ≠ 2", 1060, 540, 120, ENT)
        E.frase(c, t, C["s06.e"], [("qualquer", "i", 80), ("real", "g", 76), ("entra,", "i", 80), ("menos", "i", 80), ("o", "i", 80), ("2", "g", 90, ERRADO)],
                W / 2, 860, "center")
    E.saida(c, t, C["s07"] - 0.1, s06)
    if t < C["s07"]:
        return
    fml(c, t, C["s07"], "x ≠ 2", W / 2, 230, 110, ENT, "center")
    y = 520
    vx = E.reta(c, t, C["s07"], RX0, RX1, y, -2, 6, list(range(-2, 7)), E._num, size=48)
    E.intervalo(c, t, C["s07.a"], vx, y, None, 2)
    E.intervalo(c, t, C["s07.a"] + 0.3, vx, y, 2, None)
    anel(c, t, C["s07.b"], vx(2), y, 36)
    E.foco(c, t, C["s07.b"], 0.4, lambda a: centro(c, "furo", vx(2), 430, 50, "b", ERRADO, a))
    E.frase(c, t, C["s07.c"], [("2", "g", 70, ENT), ("partes", "i", 70)], W / 2, 690, "center")
    txe(c, t, C["s07.d"], "]−∞, 2[", 560, 840, 110, "g", ENT, "center")
    E.frase(c, t, C["s07.e"] - 0.4, [("ou", "i", 80)], W / 2, 840, "center")
    txe(c, t, C["s07.e"], "]2, +∞[", 1360, 840, 110, "g", ENT, "center")
    E.foco(c, t, C["s07.f"], 0.4, lambda a: centro(c, "aberto no 2", W / 2, 940, 48, "b", TINTA2, a))
    E.foco(c, t, C["s07.g"], 0.4, lambda a: E.pilula(c, "a união é outra aula", 1560, 1010, 38, "b", fundo=TINTA2, a=a))


# ---------------- raiz ----------------
F3 = "f(x) = r{x − 3}"


def b_raiz(c, t, C, b):
    def s08():
        fml(c, t, C["s08.a"], F3, W / 2, 320, 160, align="center")
        realce(c, t, C["s08.b"], "f(x) = ", "r", "x − 3", W / 2, 320, 160, ERRADO, "center", F3)
        E.frase(c, t, C["s08.c"], [("dentro:", "i", 72), ("não", "g", 72, ERRADO), ("pode", "i", 72), ("ser", "i", 72), ("negativo", "g", 72, ERRADO)],
                W / 2, 520, "center")
        fml(c, t, C["s08.d"], "r{0} = 0", 640, 690, 96)
        E.frase(c, t, C["s08.d"] + 0.4, [("zero", "g", 66, CERTO), ("pode", "i", 66)], 1040, 680)
        fml(c, t, C["s08.e"], "x − 3 ≥ 0", W / 2, 900, 120, ENT, "center")
    E.saida(c, t, C["s09"] - 0.1, s08)
    if t < C["s09"]:
        return
    fml(c, t, C["s09"], "x − 3 ≥ 0", 300, 230, 96)
    E.foco(c, t, C["s09.a"], 0.4, lambda a: E.pilula(c, "+ 3", 860, 200, 44, "g", fundo=TINTA2, a=a))
    fml(c, t, C["s09.a"], "x ≥ 3", 1060, 230, 110, ENT)
    y = 500
    vx = E.reta(c, t, C["s09.a"] + 0.6, RX0, RX1, y, -1, 7, list(range(-1, 8)), E._num, size=48)
    E.intervalo(c, t, C["s09.b"], vx, y, 3, None, fecha_ini=True)
    txe(c, t, C["s09.b"], "[3, +∞[", 300, 700, 110, "g", ENT)
    anel(c, t, C["s09.c"], vx(3), y, 36, ENT)
    E.foco(c, t, C["s09.c"], 0.4, lambda a: centro(c, "fechado: o 3 entra", vx(3), 410, 48, "b", ENT, a))
    fml(c, t, C["s09.d"], "x = 7: r{4} = 2", 1000, 680, 76)
    bola_x(c, t, C["s09.d"] + 0.8, 1640, 655, True)
    fml(c, t, C["s09.e"], "x = 2: r{−1}", 1000, 830, 76, ERRADO)
    bola_x(c, t, C["s09.e"] + 0.8, 1640, 805, False)
    pingo(c, t, C["s09.d"], vx(7), y, CERTO)
    pingo(c, t, C["s09.e"], vx(2), y, ERRADO)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s10.a"], [("tratar", "i", 76), ("a", "i", 76), ("raiz", "g", 72), ("como", "i", 76), ("a", "i", 76), ("divisão", "g", 72, ERRADO)],
            W / 2, 170, "center")

    def errado():
        fml(c, t, C["s10.a"] + 0.4, "r{x − 3}", 260, 380, 110)
        fml(c, t, C["s10.b"], "x − 3 ≠ 0", 760, 340, 90, ERRADO)
        fml(c, t, C["s10.c"], "x ≠ 3", 760, 480, 90, ERRADO)
        E.frase(c, t, C["s10.d"], [("o", "i", 64), ("2", "g", 70, ERRADO), ("entraria:", "i", 64)], 1260, 340)
        fml(c, t, C["s10.d"] + 0.6, "r{2 − 3} = r{−1}", 1260, 480, 76, ERRADO)
        if t > C["s10.d"] + 1.2:
            E.risco(c, 740, 500, 1080, 410, t, C["s10.d"] + 1.2, largura=10)
    E.saida(c, t, C["s10.e"] - 0.2, errado)
    E.foco(c, t, C["s10.e"], 0.5, lambda a: vilao(c, 150, 420, 780, 300, "f{1}{x}", "embaixo da divisão", a, "≠ 0", 46))
    E.foco(c, t, C["s10.f"], 0.5, lambda a: vilao(c, 990, 420, 780, 300, "r{x}", "dentro da raiz", a, "≥ 0", 46))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def s11():
        E.frase(c, t, C["s11"], ps("agora, o atalho", "i", 72, CLARO), W / 2, 150, "center")
        E.frase(c, t, C["s11.a"], [("procure", "i", 92, CLARO), ("os", "i", 92, CLARO), ("vilões", "g", 92, BR)], W / 2, 290, "center")
        for k, y, simb, l1, l2 in (("s11.b", 380, "f{1}{x}", "divisão com x embaixo?", "o de baixo ≠ 0"),
                                   ("s11.c", 600, "r{x}", "raiz quadrada com x dentro?", "o de dentro ≥ 0")):
            a = ep(t, C[k], 0.5)
            if a > 0:
                M.rrect(c, 260, y, 1400, 180, 30, "#FFFFFF", 0.08 * a)
                E.formula(c, simb, 400, y + 120, 96, "g", ERRADO, a, "center")
            E.frase(c, t, C[k], [(l1, "i", 64, CLARO)], 560, y + 80)
            E.foco(c, t, C[k] + 1.2, 0.5, lambda a, l2=l2, y=y: E.formula(c, l2, 560, y + 152, 64, "g", BR, a))
        E.frase(c, t, C["s11.d"], [("nenhum", "i", 76, CLARO), ("vilão?", "g", 76, BR)], 300, 920)
        E.foco(c, t, C["s11.e"], 0.5, lambda a: tx(c, "D = ℝ", 900, 925, 110, "g", CERTO, a))
        E.frase(c, t, C["s11.e"] + 0.4, ps("todos os reais", "i", 60, CLARO), 1300, 920)
    E.saida(c, t, C["s12"] - 0.1, s11)
    if t < C["s12"]:
        return
    E.frase(c, t, C["s12.a"], ps("só esses lugares quebram a conta", "i", 76, CLARO), W / 2, 200, "center", 0.1)
    E.foco(c, t, C["s12.b"], 0.5, lambda a: E.formula(c, "r3{−8} = −2", 300, 420, 100, "g", BR, a))
    E.frase(c, t, C["s12.b"] + 0.6, [("raiz", "i", 60, CLARO), ("cúbica:", "i", 60, CLARO), ("não", "g", 60, CERTO), ("barra", "g", 60, CERTO)], 960, 405)
    E.foco(c, t, C["s12.b"] + 4.6, 0.5, lambda a: E.formula(c, "r4{−16}", 300, 590, 100, "g", BR, a))
    E.frase(c, t, C["s12.b"] + 5.0, [("raiz", "i", 60, CLARO), ("quarta:", "i", 60, CLARO), ("barra", "g", 60, ERRADO)], 960, 575)
    E.frase(c, t, C["s12.c"], [("não", "g", 64, ERRADO), ("compensa", "i", 64, CLARO), ("parar", "i", 64, CLARO), ("na", "i", 64, CLARO), ("fórmula", "g", 64, BR),
                               ("se", "i", 64, CLARO), ("há", "i", 64, CLARO), ("história", "g", 64, BR)], W / 2, 780, "center")
    E.frase(c, t, C["s12.d"], [("tempo,", "i", 60, CLARO), ("pessoas…", "i", 60, CLARO), ("a", "i", 60, CLARO), ("situação", "g", 60, BR), ("também", "i", 60, CLARO),
                               ("corta", "g", 60, BR)], W / 2, 900, "center")


# ---------------- questão ----------------
G1 = "g(x) = f{5}{x + 4}"
H1 = "h(x) = r{6 − 2x}"


def b_questao(c, t, C, b):
    E.frase(c, t, C["s13"], ps("hora de testar", "i", 72, COR), XE, 190)
    E.frase(c, t, C["s13"] + 1.2, [("domínio", "g", 66, ENT), ("em", "i", 66), ("intervalo", "g", 66)], XE, 300)
    fml(c, t, C["s13.a"], G1, XE, 520, 120)
    fml(c, t, C["s13.b"], H1, XE, 800, 120)
    if t >= C["s14"]:
        E.relogio(c, t, C["s14.a"], cx=1480, cy=470, r=170)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    def g_():
        fml(c, t, C["s15"], G1, XE, 260, 100)
        realce(c, t, C["s15"] + 1.0, "g(x) = ", "f", ("5", "x + 4"), XE, 260, 100, ERRADO)
        fml(c, t, C["s15.a"], "x + 4 ≠ 0", 900, 220, 84)
        fml(c, t, C["s15.b"], "x ≠ −4", 900, 340, 96, ENT)
        E.foco(c, t, C["s15.b"], 0.4, lambda a: E.pilula(c, "− 4", 1420, 310, 42, "g", fundo=TINTA2, a=a))
        y = 600
        vx = E.reta(c, t, C["s15.b"] + 0.4, RX0, RX1, y, -7, 2, list(range(-7, 3)), E._num, size=46)
        E.intervalo(c, t, C["s15.c"], vx, y, None, -4)
        E.intervalo(c, t, C["s15.d"], vx, y, -4, None)
        txe(c, t, C["s15.c"], "]−∞, −4[", 560, 840, 100, "g", ENT, "center")
        E.frase(c, t, C["s15.d"] - 0.4, [("ou", "i", 76)], W / 2, 840, "center")
        txe(c, t, C["s15.d"], "]−4, +∞[", 1360, 840, 100, "g", ENT, "center")
    E.saida(c, t, C["s16"] - 0.1, g_)
    if t < C["s16"]:
        return
    fml(c, t, C["s16"], H1, XE, 240, 100)
    realce(c, t, C["s16"] + 1.0, "h(x) = ", "r", "6 − 2x", XE, 240, 100, ERRADO)
    fml(c, t, C["s16.a"], "6 − 2x ≥ 0", 900, 200, 76)
    fml(c, t, C["s16.b"], "−2x ≥ −6", 900, 300, 76)
    E.foco(c, t, C["s16.c"], 0.4, lambda a: E.pilula(c, "÷ (−2): vira o sinal", 1460, 370, 40, "g", fundo=ERRADO, a=a))
    fml(c, t, C["s16.d"], "x ≤ 3", 900, 440, 100, ENT)
    y = 640
    vx = E.reta(c, t, C["s16.d"] + 0.4, RX0, RX1, y, -3, 6, list(range(-3, 7)), E._num, size=46)
    E.intervalo(c, t, C["s16.e"], vx, y, None, 3, fecha_fim=True)
    txe(c, t, C["s16.e"], "]−∞, 3]", 300, 880, 110, "g", ENT)
    pingo(c, t, C["s16.f"], vx(0), y, CERTO)
    fml(c, t, C["s16.f"], "x = 0: r{6}", 1050, 880, 76)
    bola_x(c, t, C["s16.f"] + 0.6, 1520, 855, True)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s17"], [("resumindo", "i", 92, COR)], W / 2, 210, "center")
        itens = (("s17.a", [("embaixo", "i", 80), ("da", "i", 80), ("divisão:", "i", 80)], "≠ 0"),
                 ("s17.b", [("dentro", "i", 80), ("da", "i", 80), ("raiz", "i", 80), ("quadrada:", "i", 80)], "≥ 0"),
                 ("s17.c", [("sem", "i", 80), ("vilão:", "i", 80)], "todos os reais"))
        for i, (k, partes, fim) in enumerate(itens):
            y = 420 + i * 190
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 300, y - 30, 56, a=a),
                                                         E.escreve(c, str(i + 1), 300 - E.larg(str(i + 1), "g", 64) / 2, y - 7, 64, "g", BR, a)))
            w = E.frase(c, t, C[k] + 0.1, partes, 400, y)
            txe(c, t, C[k] + 0.6, fim, 400 + w + 30, y, 84, "g", ENT)
    E.saida(c, t, C["s18"] - 0.1, resumo)
    if t < C["s18"]:
        return
    E.frase(c, t, C["s18"], [("próxima", "i", 84), ("aula", "i", 84)], XE, 300)
    E.frase(c, t, C["s18.a"], [("o", "i", 120), ("gráfico", "g", 130, COR)], XE, 470)
    E.frase(c, t, C["s18.b"], ps("pontos no plano cartesiano", "i", 66, TINTA2), XE, 590, passo=0.1)
    E.frase(c, t, C["s18.c"], [("teste", "i", 76), ("da", "i", 76), ("reta", "g", 76, COR), ("vertical", "g", 76, COR)], XE, 710)
    E.foco(c, t, C["s18.d"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1450, 400, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s18.d"] + 0.3, 0.8))
    E.cursor(c, lerp(1780, 1580, p), lerp(720, 425, p), ep(t, C["s18.d"] + 0.2, 0.4))
    E.frase(c, t, C["s18.e"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 920, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, regra=b_regra, zero=b_zero, divisao=b_divisao, raiz=b_raiz, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
