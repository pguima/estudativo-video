"""Visual — Estudativo · QUI-INO-007: ler uma equação e a conservação das massas. Primeira aula da trilha
"Funções e Reações Inorgânicas" (ácidos, bases, sais, óxidos e reações).

Segue a LINGUAGEM VISUAL DA QUÍMICA do cabeçalho de QUI-MIS-001/roteiro/visual.py. Acréscimos desta trilha (as aulas QUI-INO-*
copiam daqui):
- EQUAÇÃO: sempre Q.equacao, termo a termo na fala (tl). Embaixo dela, E.chave + rótulo: "reagentes" em TINTA2 à esquerda e
  "produtos" em COR à direita (peça lado()). Valores sob cada espécie (massas, contagens) com Q.sob_termos.
- CONSERVAÇÃO: balança equilibrada (E.balanca) = a equação vale; o desconhecido entra como "?" e vira a esfera turquesa.
  Frasco fechado = erlenmeyer com rolha (frasco_fechado): é o "sistema fechado" de Lavoisier.
- ÍON: bolinha do elemento (Q.atomo) com a carga num selo pequeno no alto à direita (ion()): + em âmbar, − em Q.ELETRON.
  Grupo de átomos com carga (OH⁻, SO₄²⁻) = a bolinha-vareta com o mesmo selo. A fórmula do íon vai ao lado, com Q.formula.
- PAPEL DA SUBSTÂNCIA (ácido, base, neutro): pílula com a cor da escala de pH (ACIDO âmbar-avermelhado, BASE azul-violeta,
  NEUTRO cinza-tinta). Não usar verde nem vermelho puros: são certo e errado.
- MAIS e MENOS da carga nunca se confundem com a soma: carga só em sobrescrito (Q.formula), soma só entre espécies.
- Questão: texto à esquerda, desenho e relógio à direita; resposta com Q.inventario / sob_termos e a esfera turquesa.
Todo instante vem de C[...] (marcadores do roteiro), para acompanhar a voz real quando ela chegar."""
import math

import editorial as E
import quimica as Q
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Química", "Ácidos, bases e reações")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_QUI-INO-007_equacao_conservacao_massas.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("reacao", "equacao", "lavoisier", "atalho", "questao", "fim"))
BR = "#FFFFFF"
ACIDO, BASE, NEUTRO = "#E8602C", "#4B3FB5", TINTA2

# as contas da aula
assert Q.lados("C + O2 -> CO2")[0] == Q.lados("C + O2 -> CO2")[1] == {"C": 1, "O": 2}
assert 12 + 32 == 44 and 44 - 12 == 32
assert Q.lados("Fe + S -> FeS")[0] == Q.lados("Fe + S -> FeS")[1]
assert 56 + 32 == 88


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças comuns da trilha (candidatas ao kit) ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def bola_txt(c, t, t0, s, cx, cy, r, size, cor=None):
    """resposta na esfera"""
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r * ease_back(prog(t, t0, 0.5)), cor, a),
                                     E.formula(c, s, cx, cy + size * 0.36, size, "g", E.SOBRE if cor is None else BR, a, "center")))


def pilula_em(c, t, t0, s, cx, cy, size, fundo=None, est="g", cor=BR):
    E.foco(c, t, t0, 0.4, lambda a: E.pilula(c, s, cx, cy, size, est, fundo=fundo, a=a, cor=cor))


def lista(c, t, itens, x, y0, dy, size=70, escuro=False):
    """lista numerada: itens = [(instante, partes da frase)]"""
    for i, (ti, partes) in enumerate(itens):
        y = y0 + i * dy
        E.foco(c, t, ti, 0.5, lambda a, y=y, i=i: (E.bola(c, x + 40, y - 26, 44, a=a), centro(c, str(i + 1), x + 40, y - 4, 54, "g", E.SOBRE, a)))
        E.frase(c, t, ti + 0.1, partes, x + 110, y, passo=0.12)


def promessa(c, t, t0, itens, x=XE, y0=460, dy=170):
    """a promessa do gancho: 'até o fim da aula' + lista + hexágono da Química"""
    tb = t0 + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1560, 540, 280 * ease_back(prog(t, tb, 0.8)), giro=8 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, t0, ps("até o fim da aula", "i", 88), x, 280, passo=0.14)
    lista(c, t, itens, x, y0, dy)


def lado(c, t, t0, x0, x1, y, rot, cor, sub=None, size=54):
    """chave embaixo de um lado da equação, com o nome (reagentes / produtos)"""
    p = ep(t, t0, 0.5)
    if p <= 0:
        return
    E.chave(c, x0, x1, y, cor, p, 26)
    E.foco(c, t, t0 + 0.2, 0.4, lambda a: centro(c, rot, (x0 + x1) / 2, y + 90, size, "g", cor, a))
    if sub:
        E.foco(c, t, t0 + 0.5, 0.4, lambda a: centro(c, sub, (x0 + x1) / 2, y + 150, 44, "i", TINTA2, a))


def ion(c, cx, cy, r, s, carga, a=1.0, escuro=False):
    """íon: a bolinha do elemento com a carga num selo no alto à direita"""
    if a <= 0:
        return
    Q.atomo(c, cx, cy, r, s, a, escuro=escuro)
    selo_carga(c, cx + r * 0.78, cy - r * 0.78, r * 0.42, carga, a)


def selo_carga(c, cx, cy, r, carga, a=1.0):
    pos = "+" in carga
    E.bola(c, cx, cy, r, "#F2A516" if pos else Q.ELETRON, a)
    centro(c, carga.replace("-", "−"), cx, cy + r * 0.42, r * 1.15, "g", BR, a)


def frasco_fechado(c, t, t0, cx, yb, w=220, h=260, particulas=None, cor=None):
    """erlenmeyer com rolha: o sistema fechado"""
    Q.erlenmeyer(c, t, t0, cx, yb, w, h, 0.0 if not cor else 0.3, cor or Q.AGUA, particulas=particulas)
    q = ep(t, t0 + 0.2, 0.4)
    if q > 0:
        M.rrect(c, cx - w * 0.16, yb - h - 34, w * 0.32, 52, 10, "#8B5E3C", q)


def fim(c, t, C, sr, itens, sp, l1, l2, k_insc, k_bons, desenho=None):
    """fechamento: resumo numerado, depois a próxima aula, inscreva-se e bons estudos"""
    def resumo():
        E.frase(c, t, C[sr], [("resumindo", "i", 92, COR)], W / 2, 180, "center")
        for i, (k, partes) in enumerate(itens):
            y = 360 + i * 180
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 260, y - 26, 52, a=a), centro(c, str(i + 1), 260, y - 4, 60, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, partes, 360, y, passo=0.12)
    E.saida(c, t, C[sp] - 0.1, resumo)
    if t < C[sp]:
        return
    E.frase(c, t, C[sp], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C[sp] + 0.6, [(l1, "g", 110, COR)], XE, 400)
    if l2:
        E.frase(c, t, C[sp] + 1.0, [(l2, "g", 110, COR)], XE, 530)
    if desenho:
        desenho()
    E.foco(c, t, C[k_insc], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 420, 76, estilo="g", a=a))
    p = ease_io(prog(t, C[k_insc] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(720, 445, p), ep(t, C[k_insc] + 0.2, 0.4))
    E.frase(c, t, C[k_bons], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1520, 990, "center")


# ---------------- peças desta aula ----------------
def vela(c, cx, yb, w, h, t, a=1.0):
    """vela acesa: corpo de cera, pavio e chama tremulando; h = altura da cera"""
    if a <= 0:
        return
    M.rrect(c, cx - w / 2, yb - h, w, h, 14, "#F4E6C8", a, shadow=True)
    M.rrect(c, cx - w / 2, yb - h, w, 26, 12, "#FFF6E2", a)
    M.line(c, cx, yb - h, cx, yb - h - 30, TINTA, a, 5)
    chama(c, cx, yb - h - 30, 46, t, a)


def chama(c, cx, cy, s, t, a=1.0):
    """chama em gota, base na ponta (cx, cy)"""
    if a <= 0:
        return
    tr = 1 + 0.06 * math.sin(t * 17) + 0.04 * math.sin(t * 29)
    for k, cor in ((1.0, "#FF8A1F"), (0.62, "#FFD34D"), (0.3, "#FFF7D6")):
        hh, ww = s * 2.2 * k * tr, s * 0.62 * k
        pth = skia.Path()
        pth.moveTo(cx, cy - hh)
        pth.cubicTo(cx + ww * 1.2, cy - hh * 0.45, cx + ww, cy + s * 0.1 * k, cx, cy + s * 0.12 * k)
        pth.cubicTo(cx - ww, cy + s * 0.1 * k, cx - ww * 1.2, cy - hh * 0.45, cx, cy - hh)
        c.drawPath(pth, M.paint(cor, a * (0.9 if k == 1 else 1)))


def bolhas(c, t, cx, yb, w, h, n=9, a=1.0, r=12):
    """bolhas subindo num líquido (gás saindo)"""
    for k in range(n):
        f = (t * 0.55 + k / n) % 1
        x = cx - w * 0.32 + (k * 37 % 100) / 100 * w * 0.64 + 8 * math.sin(t * 3 + k)
        y = yb - 20 - f * h
        c.drawCircle(x, y, r * (0.6 + 0.5 * f), M.paint(TINTA2, a * 0.8 * (1 - f * 0.6), stroke=3))


def palha(c, cx, cy, r, a=1.0, cor="#9AA0A8"):
    """palha de aço: novelo de fios metálicos"""
    if a <= 0:
        return
    for k in range(26):
        ang = k * 2.39
        rr = r * (0.35 + 0.65 * ((k * 53) % 17) / 17)
        c.drawOval(skia.Rect.MakeXYWH(cx - rr + 12 * math.cos(ang), cy - rr * 0.7 + 10 * math.sin(ang), rr * 2, rr * 1.4),
                   M.paint(cor, a * 0.85, stroke=3))


def rearranja(c, t, t0, p, cx, cy, esc=120, a=1.0):
    """C + O₂ → CO₂ na mesma tela: p = 0 separados, 1 juntos; os mesmos três átomos trocam de parceiro"""
    if t < t0:
        return
    q = ep(t, t0, 0.5) * a
    ini = [(-2.2, 0), (0.35, 0), (1.55, 0)]
    fim_ = [(0, 0), (-1.16, 0), (1.16, 0)]
    pts = [(cx + esc * lerp(i[0], f[0], ease_io(p)), cy + esc * lerp(i[1], f[1], ease_io(p))) for i, f in zip(ini, fim_)]
    if p < 0.5:
        Q._vareta(c, pts[1], pts[2], 2, 14, q * (1 - p * 2), False)
    else:
        for j in (1, 2):
            Q._vareta(c, pts[0], pts[j], 2, 14, q * (p * 2 - 1), False)
    for s, P, rr in (("C", pts[0], 58), ("O", pts[1], 54), ("O", pts[2], 54)):
        Q.atomo(c, P[0], P[1], rr * ease_back(prog(t, t0, 0.5)), s, q)
    return pts


def gelo(c, cx, yb, s, derrete, a=1.0):
    """cubo de gelo que vira poça: derrete = 0..1"""
    if a <= 0:
        return
    h = s * (1 - 0.82 * derrete)
    w = s * (1 + 0.9 * derrete)
    M.rrect(c, cx - w / 2, yb - h, w, h, 18 + 30 * derrete, mix_(Q.AGUA, "#FFFFFF", 0.35 * (1 - derrete)), a, shadow=derrete < 0.5)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2, yb - h, w, h), 18 + 30 * derrete, 18 + 30 * derrete), M.paint("#7FB6CC", a, stroke=4))


def mix_(a_, b_, f):
    return E.mix(a_, b_, f)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def um():
        E.frase(c, t, C["s01.a"], ps("uma vela acesa", "i", 88), XE, 260, passo=0.14)
        E.frase(c, t, C["s01.a"] + 0.8, ps("vai encolhendo", "i", 88, TINTA2), XE, 370, passo=0.14)
        E.frase(c, t, C["s01.b"], ps("parece que a matéria", "i", 70) + [("some?", "g", 66, TINTA)], XE, 520, passo=0.12)
        E.frase(c, t, C["s01.c"], [("nada", "g", 150, COR), ("some", "g", 150, COR)], XE, 720, passo=0.2)
        E.frase(c, t, C["s01.d"], ps("a cera vira", "i", 70) + [("gás", "g", 66, COR)] + ps("e vai para o ar", "i", 70), XE, 880, passo=0.12)
        # a vela encolhe ao longo da cena
        h = lerp(420, 230, ease_io(prog(t, C["s01.a"], C["s01.d"] - C["s01.a"] + 1.5)))
        E.foco(c, t, C["s01.a"] - 0.3, 0.6, lambda a: vela(c, 1480, 960, 150, h, t, a))
        # gás invisível subindo: moléculas de CO₂ e H₂O
        if t >= C["s01.d"]:
            for k, (mol, dx) in enumerate((("CO2", -150), ("H2O", 120), ("CO2", 40), ("H2O", -60))):
                f = ((t - C["s01.d"]) * 0.22 + k * 0.25) % 1
                y = 960 - h - 120 - f * 420
                Q.molecula(c, t, C["s01.d"] + 0.2 * k, mol, 1480 + dx + 30 * math.sin(t + k), y, 46, passo=0.05,
                           a=ep(t, C["s01.d"] + 0.2 * k, 0.4) * (1 - f) ** 0.5, rotulos=False)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t < C["s02"]:
        return
    promessa(c, t, C["s02"], [(C["s02.a"], [("reconhecer", "g", 70), ("uma", "i", 74), ("reação", "g", 70)]),
                              (C["s02.b"], [("ler", "g", 70), ("a", "i", 74), ("equação", "g", 70, COR)]),
                              (C["s02.c"], [("prever", "g", 70), ("a", "i", 74), ("massa", "g", 70, COR)]),
                              (C["s02.d"], [("atalho", "g", 70, COR), ("de", "i", 74), ("prova", "i", 74)])], y0=440, dy=150)


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], ps("só lembrar das", "i", 84) + [("fórmulas", "g", 80, COR)], XE, 220, passo=0.14)
    linhas = (("s03.a", "C", "C", "carbono"), ("s03.b", "O2", "O2", "2 átomos de oxigênio"), ("s03.c", "CO2", "CO2", "1 carbono e 2 oxigênios"))
    for i, (k, f, mol, txt) in enumerate(linhas):
        y = 430 + i * 210
        if mol == "C":
            Q.atomo_em(c, t, C[k], XE + 120, y - 40, 62, "C")
        else:
            Q.molecula(c, t, C[k], mol, XE + 120, y - 40, 78, passo=0.15)
        Q.formula_em(c, t, C[k] + 0.2, f, XE + 330, y + 10, 120)
        E.frase(c, t, C[k] + 0.5, ps(txt, "i", 70), XE + 640, y, passo=0.1)


# ---------------- o que é reação ----------------
def b_reacao(c, t, C, b):
    if t < C["s05"]:
        def s04():
            E.frase(c, t, C["s04"], ps("o que é uma", "i", 84) + [("reação química?", "g", 80, COR)], XE, 210, passo=0.14)
            E.frase(c, t, C["s04.a"], [("substâncias", "g", 70)], XE, 800)
            E.foco(c, t, C["s04.b"], 0.5, lambda a: M.arrow(c, XE + 470, 780, XE + 600, 780, COR, a, 6, 22))
            E.frase(c, t, C["s04.b"], [("substâncias", "g", 70, COR), ("novas", "g", 70, COR)], XE + 640, 800)
            p = ease_io(prog(t, C["s04.c"], 1.6))
            rearranja(c, t, C["s04.a"], p, W / 2, 500, 125)
            E.foco(c, t, C["s04.a"] + 0.4, 0.4, lambda a: (Q.formula(c, "C + O2", W / 2 - 80, 660, 64, TINTA2, a * (1 - p), "center")))
            E.foco(c, t, C["s04.c"] + 1.2, 0.4, lambda a: Q.formula(c, "CO2", W / 2, 660, 64, COR, a, "center"))
            E.frase(c, t, C["s04.c"], ps("os átomos trocam de", "i", 62, TINTA2) + [("parceiros,", "g", 58)], XE, 920, passo=0.1)
            E.frase(c, t, C["s04.d"], ps("mas", "i", 62, TINTA2) + [("continuam os mesmos", "g", 58, COR)], XE, 1010, passo=0.12)
        E.saida(c, t, C["s05"] - 0.1, s04)
        return
    if t < C["s06"]:
        def s05():
            E.frase(c, t, C["s05"], ps("os sinais de uma", "i", 84) + [("reação", "g", 80, COR)], XE, 200, passo=0.14)
            xs = (330, 750, 1170, 1590)
            # 1. gás: bolhas
            def gas():
                Q.bequer(c, t, C["s05.a"], xs[0], 760, 260, 300, 0.7, Q.AGUA)
                if t >= C["s05.a"] + 0.3:
                    bolhas(c, t, xs[0], 760, 260, 190, a=ep(t, C["s05.a"] + 0.3, 0.4))
            gas()
            # 2. cor: o líquido muda de cor
            Q.bequer(c, t, C["s05.b"], xs[1], 760, 260, 300, 0.7, lambda tt: Q.muda_cor(tt, C["s05.b"] + 0.6, Q.AGUA, "#C0672E", 1.2))
            # 3. sólido: grãos que aparecem e descem
            Q.bequer(c, t, C["s05.c"], xs[2], 760, 260, 300, 0.7, Q.AGUA)
            if t >= C["s05.c"] + 0.4:
                for k in range(16):
                    f = clampf(prog(t, C["s05.c"] + 0.4 + 0.06 * k, 1.6))
                    x = xs[2] - 90 + (k * 29 % 180)
                    y = lerp(560, 735 - (k % 4) * 9, ease_io(f))
                    c.drawCircle(x, y, 9, M.paint("#E9E9E4", ep(t, C["s05.c"] + 0.4 + 0.06 * k, 0.3)))
                    c.drawCircle(x, y, 9, M.paint(CINZA, ep(t, C["s05.c"] + 0.4 + 0.06 * k, 0.3), stroke=2))
            # 4. luz ou calor: a chama
            E.foco(c, t, C["s05.d"], 0.5, lambda a: chama(c, xs[3], 730, 80, t, a))
            for i, (k, rot, sub) in enumerate((("s05.a", "sai gás", "bolhas"), ("s05.b", "muda a cor", "ferrugem"),
                                                ("s05.c", "surge um sólido", "no líquido"), ("s05.d", "luz ou calor", "fogo"))):
                E.foco(c, t, C[k] + 0.3, 0.4, lambda a, i=i, rot=rot, sub=sub: (centro(c, rot, xs[i], 880, 54, "g", TINTA, a),
                                                                           centro(c, sub, xs[i], 945, 46, "i", TINTA2, a)))
        E.saida(c, t, C["s06"] - 0.1, s05)
        return
    # s06: não é reação
    E.frase(c, t, C["s06"], [("cuidado:", "g", 80, ERRADO)] + ps("isto não é reação", "i", 84), XE, 200, passo=0.14)
    der = ease_io(prog(t, C["s06.a"] + 0.4, 2.0))
    E.foco(c, t, C["s06.a"], 0.5, lambda a: gelo(c, 560, 700, 220, der, a))
    E.frase(c, t, C["s06.a"] + 0.3, [("gelo", "g", 66), ("derretendo", "i", 70)], 560, 830, "center", 0.12)
    Q.formula_em(c, t, C["s06.b"], "H2O(s) -> H2O(l)", 560, 960, 70, align="center")
    pilula_em(c, t, C["s06.b"] + 0.8, "só mudou de estado", 560, 1030, 40, NEUTRO, "b")
    # sal: dissolve e volta
    sal = 1 - ease_io(prog(t, C["s06.c"] + 0.5, 1.5))
    volta = ease_io(prog(t, C["s06.d"] + 0.3, 1.5))
    Q.bequer(c, t, C["s06.c"], 1400, 760, 300, 320, 0.65 * (1 - 0.85 * volta), Q.AGUA)
    if t >= C["s06.c"]:
        for k in range(14):
            q = max(sal, volta) * ep(t, C["s06.c"], 0.3)
            if q > 0:
                x = 1400 - 100 + (k * 41 % 200)
                y = 740 - (k % 3) * 12
                M.rrect(c, x - 9, y - 9, 18, 18, 3, "#FFFFFF", q)
                c.drawRect(skia.Rect.MakeXYWH(x - 9, y - 9, 18, 18), M.paint(CINZA, q, stroke=2))
    E.frase(c, t, C["s06.c"] + 0.3, [("sal", "g", 66), ("dissolvendo", "i", 70)], 1400, 830, "center", 0.12)
    E.frase(c, t, C["s06.d"], ps("a água evapora:", "i", 60, TINTA2) + [("o sal volta", "g", 56, COR)], 1400, 960, "center", 0.12)


def clampf(v):
    return max(0.0, min(1.0, v))


# ---------------- equação ----------------
EQ = "C + O2 -> CO2"
EX, EY, ES = W / 2, 470, 170


def b_equacao(c, t, C, b):
    if t < C["s09"]:
        E.frase(c, t, C["s07"], ps("a reação se escreve numa", "i", 76), XE, 180, passo=0.12)
        E.frase(c, t, C["s07.a"], [("equação química", "g", 76, COR)], XE + 940, 180)
        tl = [C["s07.b"], C["s07.b"] + 0.4, C["s07.b"] + 0.8, C["s07.c"], C["s07.d"]]
        cs = Q.equacao(c, t, C["s07.b"], EQ, EX, EY, ES, tl=tl)
        # o modelo de cada espécie embaixo
        Q.atomo_em(c, t, C["s07.b"] + 0.2, cs[0], 640, 56, "C")
        Q.molecula(c, t, C["s07.b"] + 1.0, "O2", cs[1], 640, 80, passo=0.15)
        Q.molecula(c, t, C["s07.d"] + 0.2, "CO2", cs[2], 640, 80, passo=0.15)
        xs = Q.centros(EQ, EX, EY, ES)
        # reagentes e produtos
        lado(c, t, C["s08.a"], xs[0] - 120, xs[1] + 150, 740, "reagentes", TINTA2, "o que existe antes")
        lado(c, t, C["s08.b"], xs[2] - 190, xs[2] + 190, 740, "produtos", COR, "o que se forma")
        if t >= C["s08.c"]:
            ax = (xs[1] + xs[2]) / 2 - 10
            pilula_em(c, t, C["s08.c"], "produz", ax, EY - 150, 50, E.COR)
        if t >= C["s08.d"]:
            mx = (xs[0] + xs[1]) / 2 + 20
            q = ep(t, C["s08.d"], 0.4)
            c.drawCircle(mx, EY - 55, 70 + 4 * math.sin(t * 5), M.paint(E.COR, q, stroke=6))
            E.foco(c, t, C["s08.d"] + 0.3, 0.4, lambda a: centro(c, "separa as substâncias", mx, EY - 160, 44, "i", TINTA2, a))
        return
    if t < C["s10"]:
        E.frase(c, t, C["s09"], ps("o estado de cada substância,", "i", 76), XE, 200, passo=0.12)
        E.frase(c, t, C["s09"] + 1.6, ps("entre parênteses", "i", 76, TINTA2), XE, 300, passo=0.12)
        for i, (k, s, nome) in enumerate((("s09.b", "(s)", "sólido"), ("s09.c", "(l)", "líquido"), ("s09.d", "(g)", "gás"),
                                          ("s09.e", "(aq)", "dissolvido em água"))):
            y = 480 + i * 150
            E.foco(c, t, C[k], 0.45, lambda a, s=s, y=y: E.escreve(c, s, XE + 40, y, 110, "g", COR, a))
            E.frase(c, t, C[k] + 0.2, [(nome, "i", 80)], XE + 340, y - 10)
        E.foco(c, t, C["s09.e"] + 0.6, 0.4, lambda a: E.escreve(c, "de aquoso", XE + 1000, 920, 54, "i", TINTA2, a))
        Q.bequer(c, t, C["s09.e"], 1580, 840, 280, 320, 0.6, Q.AGUA, particulas=dict(n=30, estado="liquido", tipos=[("#8E7CC3", 1.0)], r=9))
        return
    # s10: a equação completa, com os estados
    eq = "C(s) + O2(g) -> CO2(g)"
    tl = [C["s10.a"], C["s10.b"], C["s10.b"] + 0.3, C["s10.c"], C["s10.c"] + 0.3]
    cs = Q.equacao(c, t, C["s10"], eq, W / 2, 470, 150, tl=tl)
    for k, x, txt in (("s10.a", cs[0], "carbono sólido"), ("s10.b", cs[1], "oxigênio gás"), ("s10.c", cs[2], "gás carbônico")):
        E.foco(c, t, C[k] + 0.3, 0.4, lambda a, x=x, txt=txt: centro(c, txt, x, 620, 50, "i", TINTA2, a))
    E.frase(c, t, C["s10.d"], [("1", "g", 60, COR)] + ps("reagente sólido,", "i", 64) + [("1", "g", 60, COR)] + ps("gasoso", "i", 64),
            W / 2, 830, "center", 0.12)
    E.frase(c, t, C["s10.d"] + 1.4, [("1", "g", 60, COR)] + ps("produto gasoso", "i", 64), W / 2, 930, "center", 0.12)


# ---------------- Lavoisier ----------------
def b_lavoisier(c, t, C, b):
    if t < C["s12"]:
        def s11():
            E.frase(c, t, C["s11"], ps("século XVIII:", "i", 66, TINTA2), XE, 200, passo=0.12)
            E.frase(c, t, C["s11.a"], [("Lavoisier", "g", 110, COR)], XE, 330)
            E.frase(c, t, C["s11.a"] + 0.6, ps("pesou tudo em", "i", 64) + [("frascos fechados", "g", 60)], XE, 430, passo=0.1)
            E.frase(c, t, C["s11.c"], [("massa", "g", 70), ("antes", "i", 74), ("=", "g", 70, COR), ("massa", "g", 70), ("depois", "i", 74)], XE, 580, passo=0.14)
            E.frase(c, t, C["s11.d"], ps("lei da", "i", 70, TINTA2) + [("conservação das massas", "g", 66, COR)], XE, 760, passo=0.12)
            E.frase(c, t, C["s11.e"], ps("sistema fechado:", "i", 58, TINTA2) + [("reagentes", "g", 56)] + [("=", "g", 56, COR)] + [("produtos", "g", 56, COR)],
                    XE, 870, passo=0.12)
            def antes(c_, x, y):
                frasco_fechado(c_, t, C["s11.b"] + 0.3, x, y, 150, 180)
                Q.atomo_em(c_, t, C["s11.b"] + 0.6, x - 22, y - 45, 17, "C")
                Q.molecula(c_, t, C["s11.b"] + 0.7, "O2", x + 22, y - 45, 20, passo=0.1, rotulos=False)

            def depois(c_, x, y):
                frasco_fechado(c_, t, C["s11.b"] + 0.5, x, y, 150, 180)
                Q.molecula(c_, t, C["s11.b"] + 0.9, "CO2", x, y - 45, 20, passo=0.1, rotulos=False)
            E.foco(c, t, C["s11.b"], 0.6, lambda a: E.balanca(c, 1440, 560, antes, depois, 0, a, 70, 440))
            E.foco(c, t, C["s11.b"] + 1.0, 0.4, lambda a: (centro(c, "antes", 1220, 720, 46, "i", TINTA2, a), centro(c, "depois", 1660, 720, 46, "i", TINTA2, a)))
        E.saida(c, t, C["s12"] - 0.1, s11)
        return
    eqy = 300
    if t < C["s13"]:
        def s12():
            E.frase(c, t, C["s12"], ps("por que funciona?", "i", 70, TINTA2), XE, 160, passo=0.12)
            cs = Q.equacao(c, t, C["s12"], EQ, W / 2, eqy, 150, tl=[C["s12"]] * 5)
            Q.inventario(c, t, C["s12.b"], [("C", 1), ("O", 2)], cs[0] - 130, 500, 62, tl=[C["s12.b"], C["s12.b"] + 0.5])
            Q.inventario(c, t, C["s12.c"], [("C", 1), ("O", 2)], cs[2] - 180, 500, 62, tl=[C["s12.c"], C["s12.c"] + 0.5])
            E.foco(c, t, C["s12.b"] - 0.3, 0.4, lambda a: centro(c, "antes", cs[0] + 40, 430, 50, "i", TINTA2, a))
            E.foco(c, t, C["s12.c"] - 0.3, 0.4, lambda a: centro(c, "depois", cs[2], 430, 50, "i", COR, a))
            E.foco(c, t, C["s12.c"] + 1.0, 0.4, lambda a: centro(c, "=", W / 2 + 30, 600, 120, "g", COR, a))
            E.frase(c, t, C["s12.d"], ps("nenhum átomo some, nenhum aparece", "i", 64), W / 2, 890, "center", 0.1)
            E.frase(c, t, C["s12.e"], ps("então a", "i", 64) + [("massa", "g", 60, COR)] + ps("também não muda", "i", 64), W / 2, 990, "center", 0.12)
        E.saida(c, t, C["s13"] - 0.1, s12)
        return
    # s13: a conta
    E.frase(c, t, C["s13"], ps("vamos à conta", "i", 70, TINTA2), XE, 160, passo=0.12)
    Q.equacao(c, t, C["s13"], EQ, W / 2, eqy, 150, tl=[C["s13"]] * 5)
    Q.sob_termos(c, t, EQ, W / 2, eqy, 150, [["12 g", "32 g", "44 g" if t >= C["s13.e"] else "? g"]],
                 tl=[[C["s13.a"], C["s13.b"], C["s13.c"]]], size_l=84, cores_l=[None])
    pilula_em(c, t, C["s13.b"] + 0.5, "frasco fechado", W / 2, 600, 44, TINTA2, "b")
    E.formula_em(c, t, C["s13.d"], "12 + 32 =", 1060, 820, 100, "g", TINTA2, "right")
    bola_txt(c, t, C["s13.e"], "44 g", 1230, 790, 110, 84)
    E.foco(c, t, C["s13.e"] + 0.4, 0.4, lambda a: E.escreve(c, "de gás carbônico", 1370, 820, 60, "i", TINTA, a))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s14"], [("cuidado", "g", 96, ERRADO)], XE, 190)
    E.frase(c, t, C["s14.a"], ps("esquecer o", "i", 74) + [("gás", "g", 70)], XE + 450, 190, passo=0.12)
    if t < C["s15"]:
        def s14():
            inc = 0.6 * ease_io(prog(t, C["s14.c"], 1.0))
            E.foco(c, t, C["s14.b"], 0.6, lambda a: E.balanca(c, W / 2, 620, lambda c_, x, y: palha(c_, x, y - 40, 60, a),
                                                              lambda c_, x, y: palha(c_, x, y - 40, 60, a, "#6E4A2E" if t >= C["s14.c"] else "#9AA0A8"),
                                                              inc, a, 70, 760))
            E.foco(c, t, C["s14.b"] + 0.5, 0.4, lambda a: (centro(c, "antes", W / 2 - 380, 790, 50, "i", TINTA2, a),
                                                          centro(c, "queimada", W / 2 + 380, 860, 50, "i", TINTA2, a)))
            pilula_em(c, t, C["s14.c"] + 0.4, "mais pesada", W / 2 + 380, 940, 50, TINTA)
            E.frase(c, t, C["s14.d"], ps("a lei", "i", 84) + [("falhou?", "g", 80, ERRADO)], XE, 980, passo=0.12)
        E.saida(c, t, C["s15"] - 0.1, s14)
        return
    # s15: o oxigênio do ar entrou; o gás da vela saiu
    E.frase(c, t, C["s15"], [("não", "g", 70, COR), ("falhou", "i", 74)], XE, 300, passo=0.12)
    x1, x2 = 560, 1360
    E.foco(c, t, C["s15.a"], 0.5, lambda a: palha(c, x1, 640, 90, a, "#6E4A2E"))
    for k in range(3):
        f = clampf(prog(t, C["s15.a"] + 0.4 + 0.35 * k, 1.4))
        if f > 0:
            ang = math.radians(150 + 40 * k)
            r = lerp(330, 110, ease_io(f))
            Q.molecula(c, t, C["s15.a"] + 0.4 + 0.35 * k, "O2", x1 + r * math.cos(ang), 640 - r * math.sin(ang), 36, passo=0.05, a=1 - 0.6 * f, rotulos=False)
    E.frase(c, t, C["s15.a"] + 0.3, ps("o oxigênio do ar", "i", 56) + [("entrou", "g", 54, COR)], x1, 830, "center", 0.1)
    E.frase(c, t, C["s15.b"], ps("e foi pesado junto", "i", 52, TINTA2), x1, 900, "center", 0.1)
    E.foco(c, t, C["s15.c"], 0.5, lambda a: vela(c, x2, 760, 110, 220, t, a))
    if t >= C["s15.c"] + 0.3:
        for k, mol in enumerate(("CO2", "H2O", "CO2")):
            f = ((t - C["s15.c"]) * 0.3 + k / 3) % 1
            Q.molecula(c, t, C["s15.c"] + 0.3, mol, x2 + 60 + f * 220, 470 - f * 180, 36, passo=0.05,
                       a=ep(t, C["s15.c"] + 0.3, 0.4) * (1 - f), rotulos=False)
    E.frase(c, t, C["s15.c"] + 0.3, ps("o gás da vela", "i", 56) + [("saiu", "g", 54, COR)], x2, 830, "center", 0.1)
    E.foco(c, t, C["s15.d"], 0.5, lambda a: E.pilula(c, "sistema fechado: nada entra, nada sai", W / 2 + 60, 1000, 46, "g", fundo=E.COR, a=a))
    frasco_fechado(c, t, C["s15.d"] + 0.3, 1700, 960, 150, 180)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    if t < C["s17"]:
        E.frase(c, t, C["s16"], ps("o atalho de prova", "i", 72, CLARO), W / 2, 150, "center", 0.12)
        E.frase(c, t, C["s16.a"], ps("faltou uma massa?", "i", 70, CLARO), W / 2, 270, "center", 0.12)
        E.frase(c, t, C["s16.b"], ps("é o que", "i", 66, CLARO) + [("falta para fechar", "g", 62, BR)] + ps("a conta", "i", 66, CLARO), W / 2, 360, "center", 0.12)
        Q.equacao(c, t, C["s16.c"], EQ, W / 2, 560, 140, tl=[C["s16.c"]] * 5, escuro=True)
        Q.sob_termos(c, t, EQ, W / 2, 560, 140, [["12 g", "32 g" if t >= C["s16.e"] else "?", "44 g"]],
                     tl=[[C["s16.c"] + 0.6, C["s16.c"] + 1.0, C["s16.c"] + 0.3]], size_l=80, escuro=True,
                     cores_l=[E.CLARO if t >= C["s16.e"] else None])
        E.formula_em(c, t, C["s16.d"], "12 + ? = 44", W / 2 - 60, 900, 90, "g", BR, "right")
        bola_txt(c, t, C["s16.e"], "32 g", W / 2 + 160, 870, 105, 80)
        E.foco(c, t, C["s16.e"] + 0.4, 0.4, lambda a: E.escreve(c, "de oxigênio", W / 2 + 290, 900, 60, "i", CLARO, a))
        return
    E.frase(c, t, C["s17"], ps("funciona porque", "i", 70, CLARO), W / 2, 220, "center", 0.12)
    E.frase(c, t, C["s17.a"], ps("os átomos dos dois lados", "i", 70, CLARO) + [("são os mesmos", "g", 66, BR)], W / 2, 320, "center", 0.12)
    E.frase(c, t, C["s17.b"], [("não", "g", 66, ERRADO), ("compensa:", "i", 70, CLARO), ("sistema aberto", "g", 66, BR)], W / 2, 520, "center", 0.12)
    E.foco(c, t, C["s17.b"] + 0.5, 0.5, lambda a: vela(c, W / 2, 1010, 100, 150, t, a))
    E.frase(c, t, C["s17.c"], ps("procure o gás que", "i", 62, CLARO) + [("entrou", "g", 58, BR)] + ps("ou", "i", 62, CLARO) + [("saiu", "g", 58, BR)],
            W / 2, 620, "center", 0.12)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s18"], ps("hora de testar", "i", 72, COR), XE, 180)
    E.frase(c, t, C["s18.a"], ps("frasco fechado:", "i", 60, TINTA2), XE, 290, passo=0.1)
    E.frase(c, t, C["s18.a"] + 0.6, [("56 g", "g", 66, COR)] + ps("de ferro", "i", 66), XE, 390, passo=0.12)
    E.frase(c, t, C["s18.b"], [("+ 32 g", "g", 66, COR)] + ps("de enxofre", "i", 66), XE, 480, passo=0.12)
    E.frase(c, t, C["s18.c"], ps("forma só", "i", 60, TINTA2) + [("sulfeto de ferro", "g", 58)], XE, 580, passo=0.1)
    E.frase(c, t, C["s18.d"], [("1", "g", 56, COR)] + ps("quais são os reagentes e o produto?", "i", 58), XE, 760, passo=0.08)
    E.frase(c, t, C["s18.e"], [("2", "g", 56, COR)] + ps("qual é a massa do produto?", "i", 58), XE, 860, passo=0.08)
    if t < C["s19"]:
        frasco_fechado(c, t, C["s18.a"] + 0.3, 1470, 820, 300, 360)
        Q.atomo_em(c, t, C["s18.a"] + 0.8, 1420, 760, 40, "Fe")
        Q.atomo_em(c, t, C["s18.b"] + 0.3, 1520, 765, 38, "S")
    else:
        E.relogio(c, t, C["s19.a"], cx=1470, cy=470, r=200)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    eq = "Fe + S -> FeS"
    xs = Q.equacao(c, t, C["s20"], eq, W / 2, 300, 160, tl=[C["s20.a"], C["s20.a"] + 0.3, C["s20.a"] + 0.6, C["s20.b"], C["s20.b"] + 0.3])
    Q.sob_termos(c, t, eq, W / 2, 300, 160, [["56 g", "32 g", "88 g" if t >= C["s20.d"] else "? g"]],
                 tl=[[C["s20.c"], C["s20.c"] + 0.3, C["s20.c"] + 0.6]], size_l=64)
    lado(c, t, C["s20.a"] + 0.5, xs[0] - 110, xs[1] + 90, 520, "reagentes", TINTA2, size=48)
    lado(c, t, C["s20.b"] + 0.5, xs[2] - 150, xs[2] + 150, 520, "produto", COR, size=48)
    pilula_em(c, t, C["s20.c"], "frasco fechado: vale Lavoisier", W / 2, 680, 44, E.COR)
    E.formula_em(c, t, C["s20.c"] + 0.6, "56 + 32 =", 1060, 890, 100, "g", TINTA2, "right")
    bola_txt(c, t, C["s20.d"], "88 g", 1230, 860, 110, 84, CERTO)
    E.frase(c, t, C["s20.e"], ps("produto", "i", 62) + [("=", "g", 58, TINTA2)] + ps("soma dos reagentes", "i", 62), W / 2, 1030, "center", 0.1)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def prox():
        E.frase(c, t, C["s22.b"], ps("o que soltam na água,", "i", 64, TINTA2), XE, 520, passo=0.1)
        E.frase(c, t, C["s22.b"] + 1.0, ps("nomes e força", "i", 64, TINTA2), XE, 610, passo=0.1)
        Q.equacao(c, t, C["s22.b"] + 0.6, "HCl -> H^+ + Cl^-", 620, 860, 110, tl=None, passo=0.3)
    fim(c, t, C, "s21", [("s21.a", [("reagentes", "g", 66), ("→", "g", 66, COR), ("produtos", "g", 66)]),
                         ("s21.b", [("estado", "g", 66), ("entre", "i", 72), ("parênteses", "i", 72)]),
                         ("s21.c", [("sistema", "i", 72), ("fechado:", "i", 72), ("a massa", "g", 66, COR), ("se conserva", "g", 66, COR)])],
        "s22", "Ácidos", None, "s22.c", "s22.d", prox)


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, reacao=b_reacao, equacao=b_equacao, lavoisier=b_lavoisier, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
