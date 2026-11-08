"""Visual — Estudativo · MAT-TOP-005: princípio da inclusão-exclusão.
Mesma linguagem do módulo (MAT-TOP-001): resposta na esfera, erro em vermelho, certo em verde, atalho no palco escuro.
Peças desta aula: grade() de números (1 a 30): múltiplo de 2 = casa cheia na cor da matéria; múltiplo de 3 = anel âmbar;
os dois ao mesmo tempo ficam com os dois sinais (é o que foi contado duas vezes). Venn de E.venn, com o miolo pintado.
Contas de "dividir e ignorar o resto" sempre no formato "100 ÷ 3 = 33, sobra 1".
Sem voz ainda: todo instante vem de C[...] (cenas e marcadores), nunca de segundos fixos."""
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Tópicos Avançados")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-TOP-005_principio_da_inclusao_exclusao.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("contar", "regra", "tres", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
AMB = "#D98A00"
um = lambda n, ks: sum(1 for i in range(1, n + 1) if any(i % k == 0 for k in ks))
assert 100 // 2 == 50 and divmod(100, 3) == (33, 1) and divmod(100, 6) == (16, 4) and 50 + 33 - 16 == 67 == um(100, (2, 3))
assert 100 // 5 == 20 and 100 // 10 == 10 and 100 // 15 == 6 and 100 // 30 == 3
assert 50 + 33 + 20 == 103 and 16 + 10 + 6 == 32 and 103 - 32 == 71 and 71 + 3 == 74 == um(100, (2, 3, 5))
assert um(6, (2, 3)) == 4 and 96 // 6 == 16 and 16 * 4 == 64 and um(100, (2, 3)) - um(96, (2, 3)) == 3
assert divmod(200, 3) == (66, 2) and 200 // 5 == 40 and divmod(200, 15) == (13, 5) and 66 + 40 - 13 == 93 == um(200, (3, 5))


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def bola_txt(c, t, t0, s, cx, cy, r, size, cor=None):
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r * ease_back(prog(t, t0, 0.5)), cor, a),
                                     E.formula(c, str(s), cx, cy + size * 0.36, size, "g", BR, a, "center")))


def txt_em(c, t, t0, s, x, y, size, cor=TINTA, est="g", align="left"):
    E.foco(c, t, t0, 0.5, lambda a: E.formula(c, s, x, y, size, est, cor, a, align))


# ---------------- ∪ e ∩ desenhados (a fonte da casa não tem; mesmo traço da MAT-CON-003) ----------------
_TRACO = dict(g=0.15, b=0.1, m=0.075, i=0.052, s=0.052)


def _simb(c, ch, x, y, size, est, cor, a):
    sw = size * _TRACO[est]
    x0, x1 = x + size * 0.1 + sw / 2, x + size * 0.68 - sw / 2
    top, bot = y - size * 0.68 + sw / 2, y - size * 0.02 - sw / 2
    rr = (x1 - x0) / 2
    pa = skia.Path()
    if ch == "∪":
        pa.moveTo(x0, top); pa.lineTo(x0, bot - rr)
        pa.arcTo(skia.Rect.MakeLTRB(x0, bot - 2 * rr, x1, bot), 180, -180, False)
        pa.lineTo(x1, top)
    else:
        pa.moveTo(x0, bot); pa.lineTo(x0, top + rr)
        pa.arcTo(skia.Rect.MakeLTRB(x0, top, x1, top + 2 * rr), 180, 180, False)
        pa.lineTo(x1, bot)
    pt = M.paint(cor, a, stroke=sw)
    pt.setStrokeCap(skia.Paint.kButt_Cap)
    c.drawPath(pa, pt)


def _pedacos(s):
    out, cur = [], ""
    for ch in s:
        if ch in "∪∩":
            if cur:
                out.append(cur); cur = ""
            out.append(ch)
        else:
            cur += ch
    return out + ([cur] if cur else [])


def tx(c, s, x, y, size, est="g", cor=None, a=1.0, align="left"):
    """como E.escreve, com ∪ e ∩ desenhados"""
    if a <= 0:
        return
    cor = cor or TINTA
    ws = [size * 0.78 if p in ("∪", "∩") else E.larg(p, est, size) for p in _pedacos(s)]
    x = x - sum(ws) / 2 if align == "center" else x - sum(ws) if align == "right" else x
    for p, w in zip(_pedacos(s), ws):
        if p in ("∪", "∩"):
            _simb(c, p, x, y, size, est, cor, a)
        else:
            E.escreve(c, p, x, y, size, est, cor, a)
        x += w


# ---------------- grade de números ----------------
def grade(c, t, x0, y0, n, cols, cel, t_num, t2, t3, t_dupla=None, escuro=False, size=46):
    """números 1..n em cols colunas; t2 = instante dos múltiplos de 2 (casa cheia); t3 = dos de 3 (anel âmbar);
    t_dupla = instante em que os múltiplos de 6 ganham o rótulo 2x"""
    for i in range(1, n + 1):
        col, lin = (i - 1) % cols, (i - 1) // cols
        x, y = x0 + col * cel, y0 + lin * cel
        q = ep(t, t_num + 0.02 * i, 0.3)
        if q <= 0:
            continue
        p2 = ep(t, t2, 0.4) if t2 is not None and i % 2 == 0 else 0
        p3 = ep(t, t3, 0.4) if t3 is not None and i % 3 == 0 else 0
        r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x + 6, y + 6, cel - 12, cel - 12), 14, 14)
        c.drawRRect(r, M.paint(COR if p2 else ("#2A2A33" if escuro else BR), q * (0.9 if p2 else 0.8)))
        if p2:
            c.drawRRect(r, M.paint(COR, p2))
        c.drawRRect(r, M.paint(FIO if not escuro else "#44445A", q, stroke=2))
        if p3:
            c.drawCircle(x + cel / 2, y + cel / 2, cel * 0.4, M.paint(AMB, p3, stroke=6))
        cor = BR if p2 else (BR if escuro else TINTA)
        centro(c, str(i), x + cel / 2, y + cel / 2 + size * 0.36, size, "g", cor, q)
        if t_dupla is not None and i % 6 == 0:
            pd = ep(t, t_dupla + 0.1 * (i // 6), 0.4)
            if pd > 0:
                E.pilula(c, "2x", x + cel - 14, y + 10, 30, "g", fundo=ERRADO, a=pd)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def cena1():
        E.frase(c, t, C["s01.a"], [("de", "i", 80), ("1", "g", 80, COR), ("a", "i", 80), ("100:", "g", 80, COR), ("múltiplos", "i", 80),
                                   ("de", "i", 80), ("2", "g", 80), ("ou", "i", 80), ("de", "i", 80), ("3?", "g", 80)], W / 2, 220, "center")
        txt_em(c, t, C["s01.b"], "50", 520, 480, 160, COR, "g", "center")
        E.foco(c, t, C["s01.b"] + 0.3, 0.4, lambda a: centro(c, "múltiplos de 2", 520, 560, 44, "i", TINTA2, a))
        E.foco(c, t, C["s01.c"] - 0.2, 0.4, lambda a: centro(c, "+", 800, 470, 120, "g", TINTA, a))
        txt_em(c, t, C["s01.c"], "33", 1080, 480, 160, AMB, "g", "center")
        E.foco(c, t, C["s01.c"] + 0.3, 0.4, lambda a: centro(c, "múltiplos de 3", 1080, 560, 44, "i", TINTA2, a))
        txt_em(c, t, C["s01.d"], "= 83", 1300, 480, 160, ERRADO)
        if t >= C["s01.e"]:
            E.risco(c, 1300, 520, 1760, 360, t, C["s01.e"] - 0.2, largura=14)
        bola_txt(c, t, C["s01.e"], "67", W / 2, 820, 140, 140, CERTO)
    E.saida(c, t, C["s02"] - 0.1, cena1)
    if t >= C["s02"]:
        E.foco(c, t, C["s02.b"] - 0.2, 0.7, lambda a: E.bola(c, 1450, 560, 270 * ease_back(prog(t, C["s02.b"] - 0.2, 0.7))), blur=0)
        E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 90), XE, 330)
        E.frase(c, t, C["s02.a"] + 0.9, [("contar", "g", 120, COR)], XE, 480)
        E.frase(c, t, C["s02.a"] + 1.4, [("sem", "i", 110), ("repetir", "g", 120)], XE, 630)
        E.frase(c, t, C["s02.a"] + 2.4, [("2", "g", 110, COR), ("ou", "i", 110), ("3", "g", 110, COR), ("conjuntos", "i", 110)], XE, 780)
        E.foco(c, t, C["s02.b"] + 0.2, 0.5, lambda a: (E.escreve(c, "+ atalho", 1300, 545, 80, "g", BR, a),
                                                      E.escreve(c, "de prova", 1320, 630, 80, "i", BR, a)))


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], ps("você vai usar", "i", 84), XE, 200)
    E.frase(c, t, C["s03.a"], [("2", "g", 110, COR), ("coisas", "i", 100)], XE + 640, 200)
    x, w = XE, 1580
    for i, k in enumerate(("s03.b", "s03.c")):
        y = 290 + i * 340
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 290, p, prog_=p)
    E.frase(c, t, C["s03.b"] + 0.1, [("a", "i", 66), ("fórmula", "i", 66), ("da", "i", 66), ("união", "g", 64, COR)], x + 50, 390)
    E.foco(c, t, C["s03.b"] + 0.8, 0.5, lambda a: tx(c, "n(A ∪ B) = n(A) + n(B) − n(A ∩ B)", x + 50, 520, 76, "g", TINTA, a))
    E.frase(c, t, C["s03.c"] + 0.1, [("o", "i", 66), ("MMC:", "g", 64, COR), ("o", "i", 66), ("menor", "i", 66), ("múltiplo", "i", 66), ("comum", "i", 66)], x + 50, 730)
    txt_em(c, t, C["s03.c"] + 0.8, "MMC(2, 3) = 6", x + 50, 860, 76)


# ---------------- contar múltiplos ----------------
GX, GY, CEL = 120, 520, 112


def b_contar(c, t, C, b):
    def contas():
        E.frase(c, t, C["s04.a"], [("divida", "g", 74, COR), ("e", "i", 80), ("ignore", "i", 80), ("o", "i", 80), ("resto", "i", 80)], XE, 200)
        txt_em(c, t, C["s04.b"], "100 ÷ 2 = 50", XE, 340, 80)
        txt_em(c, t, C["s04.c"], "100 ÷ 3 = 33, sobra 1", 900, 340, 80, AMB)
        E.foco(c, t, C["s04.d"], 0.4, lambda a: E.escreve(c, "o último pedaço não fecha um múltiplo", 900, 420, 46, "i", TINTA2, a))
    E.saida(c, t, C["s06"] - 0.1, contas)
    grade(c, t, GX, GY, 30, 15, CEL, C["s04.b"] - 0.4, C["s04.b"] + 0.3, C["s04.c"] + 0.3, C["s05.c"] - 0.6)
    if t >= C["s05"]:
        E.foco(c, t, C["s05.a"], 0.4, lambda a: E.escreve(c, "6, 12, 18: múltiplos de 2 e de 3", XE, 820, 60, "i", TINTA, a))
        E.foco(c, t, C["s05.c"], 0.4, lambda a: E.pilula(c, "contados 2 vezes", 1500, 800, 56, "g", fundo=ERRADO, a=a))
    if t >= C["s06"]:
        E.frase(c, t, C["s06.a"], [("múltiplos", "i", 70), ("de", "i", 70), ("2", "g", 70), ("e", "i", 70), ("de", "i", 70), ("3", "g", 70),
                                   ("=", "g", 70), ("múltiplos", "i", 70), ("de", "i", 70), ("6", "g", 70, COR)], XE, 200)
        txt_em(c, t, C["s06.b"], "100 ÷ 6 = 16, sobra 4", XE, 360, 80)
        txt_em(c, t, C["s06.c"], "50 + 33 − 16 =", XE, 960, 96)
        bola_txt(c, t, C["s06.d"], "67", 980, 930, 100, 110, CERTO)


# ---------------- regra ----------------
def b_regra(c, t, C, b):
    E.frase(c, t, C["s07.a"], [("inclusão", "g", 100, COR), ("−", "g", 100), ("exclusão", "g", 100)], W / 2, 210, "center")
    E.venn(c, t, C["s07.a"] + 0.3, 1440, 620, 200, nomes=("mult. 2", "mult. 3"), numeros={"A": 34, "AB": 16, "B": 17},
           pinta=[("A", C["s07.b"]), ("B", C["s07.b"] + 0.3), ("AB", C["s07.c"])], universo="1 a 100", size=50,
           tn={"A": C["s07.b"] + 0.2, "B": C["s07.b"] + 0.5, "AB": C["s07.c"]})
    E.frase(c, t, C["s07.b"], [("inclua", "g", 70, COR), ("cada", "i", 72), ("conjunto", "i", 72)], XE, 470)
    E.frase(c, t, C["s07.c"], [("exclua", "g", 70, ERRADO), ("o", "i", 72), ("repetido", "i", 72)], XE, 620)
    E.foco(c, t, C["s07.d"], 0.5, lambda a: tx(c, "n(A ∪ B) = n(A) + n(B) − n(A ∩ B)", XE, 900, 52, "g", TINTA, a))


# ---------------- três conjuntos ----------------
def b_tres(c, t, C, b):
    E.frase(c, t, C["s08.a"], [("múltiplos", "i", 70), ("de", "i", 70), ("2,", "g", 70, COR), ("3", "g", 70, COR), ("ou", "i", 70), ("5", "g", 70, COR)], XE, 180)
    pinta = [("ABC", C["s10.a"])]
    E.venn(c, t, C["s08.a"] + 0.2, 1440, 560, 180, nomes=("2", "3", "5"), pinta=pinta, universo="", size=52,
           numeros={"ABC": "3"} if t >= C["s10.d"] else None, tn={"ABC": C["s10.d"]})
    txt_em(c, t, C["s08.b"], "+ 50 + 33 + 20", XE, 330, 72)
    E.foco(c, t, C["s08.c"], 0.4, lambda a: E.escreve(c, "100 ÷ 5 = 20", XE + 600, 330, 50, "i", TINTA2, a))
    E.foco(c, t, C["s08.d"], 0.4, lambda a: E.escreve(c, "= 103", XE, 420, 72, "g", COR, a))
    txt_em(c, t, C["s09.b"], "− 16", XE, 560, 72, ERRADO)
    E.foco(c, t, C["s09.b"] + 0.2, 0.4, lambda a: E.escreve(c, "mult. de 6", XE + 200, 560, 44, "i", TINTA2, a))
    txt_em(c, t, C["s09.c"], "− 10", XE + 460, 560, 72, ERRADO)
    E.foco(c, t, C["s09.c"] + 0.2, 0.4, lambda a: E.escreve(c, "de 10", XE + 660, 560, 44, "i", TINTA2, a))
    txt_em(c, t, C["s09.d"], "− 6", XE, 680, 72, ERRADO)
    E.foco(c, t, C["s09.d"] + 0.2, 0.4, lambda a: E.escreve(c, "de 15", XE + 160, 680, 44, "i", TINTA2, a))
    E.foco(c, t, C["s09.e"], 0.4, lambda a: E.escreve(c, "= 71", XE + 460, 680, 72, "g", COR, a))
    E.foco(c, t, C["s10.b"], 0.4, lambda a: E.escreve(c, "miolo: somado 3x, tirado 3x", XE, 790, 48, "i", ERRADO, a))
    E.foco(c, t, C["s10.c"], 0.4, lambda a: E.escreve(c, "→ sumiu", XE + 640, 790, 48, "g", ERRADO, a))
    txt_em(c, t, C["s10.d"], "+ 3", XE, 920, 72, CERTO)
    E.foco(c, t, C["s10.d"] + 0.2, 0.4, lambda a: E.escreve(c, "100 ÷ 30 = 3", XE + 170, 920, 44, "i", TINTA2, a))
    bola_txt(c, t, C["s10.e"], "74", 900, 895, 90, 100, CERTO)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s11"], [("cuidado", "g", 90, ERRADO), ("com", "i", 84), ("isto", "i", 84)], XE, 190)
    E.frase(c, t, C["s11.b"], [("múltiplos", "i", 66), ("de", "i", 66), ("4", "g", 66, COR), ("e", "i", 66), ("de", "i", 66), ("6", "g", 66, AMB)], XE, 330)
    for i, v in enumerate((4, 8, 12, 16, 20, 24)):
        x = XE + i * 180
        ok = t >= C["s11.d"] and v == 12
        E.foco(c, t, C["s11.b"] + 0.3 + i * 0.08, 0.4, lambda a, x=x, v=v, ok=ok: (
            M.rrect(c, x, 400, 150, 120, 16, CERTO if ok else COR, a), centro(c, str(v), x + 75, 480, 60, "g", BR, a)))
        if v % 6 == 0:
            E.foco(c, t, C["s11.b"] + 1.0, 0.4, lambda a, x=x: (
                c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x - 8, 392, 166, 136), 20, 20), M.paint(AMB, a, stroke=7)),
                centro(c, "e de 6", x + 75, 580, 40, "b", AMB, a)))
    E.foco(c, t, C["s11.c"], 0.4, lambda a: E.escreve(c, "4 × 6 = 24?", XE, 700, 90, "g", ERRADO, a))
    if t >= C["s11.d"]:
        E.risco(c, XE - 10, 720, XE + 520, 620, t, C["s11.d"], largura=12)
        E.foco(c, t, C["s11.d"], 0.4, lambda a: E.escreve(c, "12 ficou de fora", XE + 620, 700, 60, "i", TINTA, a))
    E.foco(c, t, C["s11.e"], 0.4, lambda a: E.escreve(c, "MMC(4, 6) = 12", XE, 880, 96, "g", CERTO, a))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def parte1():
        E.frase(c, t, C["s12"], [("atalho:", "i", 76, CLARO), ("repete", "g", 72, BR), ("a", "i", 76, CLARO), ("cada", "i", 76, CLARO), ("MMC", "g", 72, BR)], W / 2, 170, "center")
        grade(c, t, 620, 250, 6, 6, 115, C["s12.a"], C["s12.b"], C["s12.b"] + 0.4, escuro=True)
        E.foco(c, t, C["s12.b"] + 0.8, 0.4, lambda a: E.escreve(c, "4 em cada 6", 1360, 330, 60, "g", BR, a))
        E.foco(c, t, C["s12.c"], 0.5, lambda a: E.escreve(c, "até 96: 16 blocos de 6", 300, 560, 64, "i", CLARO, a))
        E.foco(c, t, C["s12.d"], 0.5, lambda a: E.escreve(c, "16 × 4 = 64", 1100, 560, 76, "g", BR, a))
        for i, v in enumerate((97, 98, 99, 100)):
            ok = v % 2 == 0 or v % 3 == 0
            x = 300 + i * 170
            E.foco(c, t, C["s12.e"] + i * 0.12, 0.4, lambda a, x=x, v=v, ok=ok: (
                M.rrect(c, x, 680, 150, 110, 16, COR if ok else "#2A2A33", a), centro(c, str(v), x + 75, 755, 52, "g", BR, a)))
        E.foco(c, t, C["s12.e"] + 0.6, 0.4, lambda a: E.escreve(c, "+ 3", 1000, 760, 76, "g", BR, a))
        E.foco(c, t, C["s12.f"], 0.5, lambda a: E.pilula(c, "64 + 3 = 67", 1450, 740, 70, "g", fundo=CERTO, a=a))
    E.saida(c, t, C["s13"] - 0.1, parte1)
    if t < C["s13"]:
        return
    E.frase(c, t, C["s13.a"], ps("a cada 6 números, o desenho recomeça", "i", 70, CLARO), W / 2, 330, "center")
    E.foco(c, t, C["s13.b"], 0.5, lambda a: E.pilula(c, "MMC grande (2, 3 e 5 → 30)? não compensa", W / 2, 560, 60, "g", fundo=ERRADO, a=a))
    E.foco(c, t, C["s13.c"], 0.5, lambda a: E.escreve(c, "use incluir e excluir", 620, 800, 70, "g", BR, a))


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s14"], ps("hora de testar", "i", 72, COR), XE, 200)
    E.frase(c, t, C["s14.a"], [("de", "i", 100), ("1", "g", 100, COR), ("a", "i", 100), ("200", "g", 100, COR)], XE, 450)
    E.frase(c, t, C["s14.b"], [("múltiplos", "i", 90), ("de", "i", 90), ("3", "g", 90), ("ou", "i", 90), ("de", "i", 90), ("5?", "g", 90)], XE, 650)
    E.relogio(c, t, C["s15.a"], 1500, 450, 190)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    txt_em(c, t, C["s16.a"], "200 ÷ 3 = 66, sobra 2", XE, 260, 80)
    txt_em(c, t, C["s16.b"], "200 ÷ 5 = 40", XE, 400, 80)
    txt_em(c, t, C["s16.c"], "MMC(3, 5) = 15", 1100, 400, 70, COR)
    txt_em(c, t, C["s16.d"], "200 ÷ 15 = 13, sobra 5", XE, 540, 80)
    txt_em(c, t, C["s17.a"], "66 + 40 − 13 =", XE, 800, 110)
    bola_txt(c, t, C["s17.b"], "93", 1060, 765, 115, 120, CERTO)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s18"], [("resumindo", "i", 92, COR)], W / 2, 200, "center")
        for i, (k, s) in enumerate((("s18.a", "some cada conjunto"), ("s18.b", "tire o repetido"), ("s18.c", "3 conjuntos: devolva o miolo"))):
            y = 400 + i * 190
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 300, y - 30, 56, a=a), centro(c, str(i + 1), 300, y - 7, 64, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, [(s, "g", 90)], 400, y)
    E.saida(c, t, C["s19"] - 0.1, resumo)
    if t < C["s19"]:
        return
    E.frase(c, t, C["s19"], ps("próxima aula", "i", 84), XE, 300)
    E.frase(c, t, C["s19.a"], [("Combinação", "g", 130, COR)], XE, 470)
    E.frase(c, t, C["s19.a"] + 0.3, [("com", "i", 120), ("repetição", "g", 130, COR)], XE, 620)
    E.frase(c, t, C["s19.b"], ps("3 doces, 4 sabores", "i", 70), XE, 770)
    E.foco(c, t, C["s19.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1430, 400, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s19.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1760, 1560, p), lerp(720, 425, p), ep(t, C["s19.c"] + 0.2, 0.4))
    E.frase(c, t, C["s19.d"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 960, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, contar=b_contar, regra=b_regra, tres=b_tres, erro=b_erro, atalho=b_atalho,
              questao=b_questao, resposta=b_resposta, fim=b_fim)
