"""Visual — Porcentagem, Episódio 6: Revisão geral, estratégia de prova, pegadinhas e treino (iniciantes, tema claro).
Peças comuns da série em ../../comum.py (reexporta o 019/comum.py: expr com frações, alternativas, pause_timer, selo...).
Índice visual da revisão: os 5 ícones dos episódios (icone()): triângulo · máquina de fator · bola de neve ·
barra 100 → 120 → 96 · termômetro e pizza. Triângulo, máquina e bola copiados dos visual.py dos eps 1–3; barra,
termômetro e pizza desenhados aqui. Selo "A BASE MUDOU" quando a causa é a base.
Cores com função: azul = definição · roxo = regra/fórmula · âmbar = armadilha · verde = atalho/dica · vermelho = erro.
"""
import importlib.util
import math
from pathlib import Path
import skia
import motor
motor.set_theme("claro")
from motor import *  # noqa
from aula import *  # noqa

_p = Path(__file__).resolve().parents[2] / "comum.py"
_s = importlib.util.spec_from_file_location("comum024", _p)
K = importlib.util.module_from_spec(_s); _s.loader.exec_module(K)
K.usar_tempos(Path(__file__).resolve().parents[1] / "audio" / "tempos.json")
motor.set_theme("claro")
expr = K.expr
frame, head_seq, which, para, boxed, regra, selo, pause_timer, chip = (K.frame, K.head_seq, K.which, K.para, K.boxed, K.regra,
                                                                        K.selo, K.pause_timer, K.chip)
fmid, ftext = K.fmid, K.ftext

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_porcentagem_ep6_revisao.mp4"
CARD_R = K.CARD_R
PELE = "#F2C7A5"
PELE_ESC = "#D9A17E"
NEVE = "#EEF4FB"
NEVE_B = "#B7CCE4"


def ftw(s, size, peso="black"):
    return K.ftext_w(s, peso, size)


# ======================================================================
# peças (mesmo traço dos episódios 1–3)
# ======================================================================

def dedo(c, cx, cy, s, a):
    """ponta de dedo tapando um ponto (ep1)"""
    if a <= 0:
        return
    w, h = s * 0.78, s * 1.15
    rrect(c, cx - w / 2, cy - h * 0.3, w, h, w / 2, PELE, a, shadow=True)
    rrect(c, cx - w * 0.3, cy - h * 0.22, w * 0.6, h * 0.34, w * 0.3, "#F8DCCB", a)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2, cy - h * 0.3, w, h), w / 2, w / 2), paint(PELE_ESC, a, stroke=3))


def triangulo(c, cx, cy, s, a, tapa=None, tapa_a=0.0):
    """triângulo da porcentagem (ep1): PARTE em cima; TOTAL × TAXA embaixo; tapa = peça coberta pelo dedo"""
    if a <= 0:
        return
    h = s * 0.9
    top, left, right = (cx, cy - h / 2), (cx - s / 2, cy + h / 2), (cx + s / 2, cy + h / 2)
    p = skia.Path(); p.moveTo(*top); p.lineTo(*left); p.lineTo(*right); p.close()
    c.drawPath(p, paint("#FFFFFF", a))
    c.drawPath(p, paint(PURPLE, a, stroke=6))
    ym = cy + h * 0.08
    xl = cx - (ym - top[1]) / h * s / 2
    line(c, xl, ym, 2 * cx - xl, ym, PURPLE, a, 5)
    line(c, cx, ym, cx, cy + h / 2, PURPLE, a, 5)
    pos = {"parte": (cx, cy - h * 0.12), "total": (cx - s * 0.2, cy + h * 0.3), "taxa": (cx + s * 0.2, cy + h * 0.3)}
    for k, (x, y) in pos.items():
        text_mid(c, k.upper(), x, y, s * 0.085, "black", INK, a)
    if tapa and tapa_a > 0:
        x, y = pos[tapa]
        dedo(c, x, y, s * 0.42, a * tapa_a)


def engrenagem(c, cx, cy, r, ang, col, a, dentes=10):
    if a <= 0:
        return
    c.save(); c.translate(cx, cy); c.rotate(ang)
    for k in range(dentes):
        c.save(); c.rotate(360 * k / dentes)
        c.drawRect(skia.Rect.MakeXYWH(-r * 0.16, -r * 1.22, r * 0.32, r * 0.4), paint(col, a))
        c.restore()
    c.drawCircle(0, 0, r, paint(col, a))
    c.drawCircle(0, 0, r * 0.38, paint("#FFFFFF", a))
    c.restore()


def maquina(c, cx, cy, fator, a, ang=0.0, col=None, w=250, h=170):
    """a máquina de fator (eps 2 e 3): caixa com engrenagem e o rótulo '× fator'"""
    if a <= 0:
        return
    col = col or PURPLE
    engrenagem(c, cx + w * 0.26, cy - h / 2 - 8, 30, ang, mix(col, "#FFFFFF", 0.35), a)
    rrect(c, cx - w / 2, cy - h / 2, w, h, 22, col, a, shadow=True)
    rrect(c, cx - w / 2 + 14, cy - h / 2 + 14, w - 28, h - 28, 16, mix(col, "#FFFFFF", 0.88), a)
    text_mid(c, f"× {fator}", cx, cy, 52, "black", col, a)


def bola(c, cx, cy, r, a, valor=None, vsize=None):
    """bola de neve (ep3) com o valor no centro"""
    if a <= 0 or r <= 1:
        return
    c.drawCircle(cx + r * 0.06, cy + r * 0.10, r, paint("#000000", a * 0.10))
    c.drawCircle(cx, cy, r, paint(NEVE, a))
    c.drawCircle(cx, cy, r, paint(NEVE_B, a, stroke=4))
    c.drawCircle(cx - r * 0.38, cy - r * 0.38, r * 0.16, paint("#FFFFFF", a * 0.9))
    if valor:
        text_mid(c, valor, cx, cy, vsize or max(22, r * 0.36), "black", INK, a)


def barras_base(c, cx, cy, a, u=1.0, escala=1.6, larg=86):
    """ep4 'a base mudou': barras 100 → 120 → 96 com a linha tracejada no 100; u revela da esquerda para a direita"""
    if a <= 0:
        return
    vals = [(100, BLUE, "100"), (120, GREEN, "120"), (96, RED, "96")]
    base = cy + 80
    for k, (v, col, s) in enumerate(vals):
        ak = a * clamp(u * 3 - k)
        if ak <= 0:
            continue
        x = cx - 150 + k * 150
        h = v * escala
        rrect(c, x - larg / 2, base - h, larg, h, 10, col, ak)
        text_mid(c, s, x, base - h - 24, 30, "black", col, ak)
    y100 = base - 100 * escala
    for k in range(14):
        x0 = cx - 210 + k * 30
        line(c, x0, y100, x0 + 16, y100, INK2, a * 0.8, 3)


def termometro(c, cx, cy, a, v0=8, v1=10, u=1.0, s=1.0):
    """ep5: termômetro de taxas subindo de v0 a v1 (em %); u = 0..1 anima a subida"""
    if a <= 0:
        return
    tw, th = 34 * s, 200 * s
    rrect(c, cx - tw / 2, cy - th / 2, tw, th, tw / 2, "#FFFFFF", a, shadow=True)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - tw / 2, cy - th / 2, tw, th), tw / 2, tw / 2),
                paint(INK2, a, stroke=3))
    c.drawCircle(cx, cy + th / 2 + 6 * s, 30 * s, paint(RED, a))
    nivel = lerp(v0, v1, clamp(u))
    yv = lambda v: cy + th / 2 - 20 * s - (v - 6) / 6 * (th - 50 * s)
    rrect(c, cx - tw / 2 + 8 * s, yv(nivel), tw - 16 * s, cy + th / 2 - yv(nivel) + 10 * s, 8 * s, RED, a)
    for v in (v0, v1):
        line(c, cx + tw / 2, yv(v), cx + tw / 2 + 18 * s, yv(v), INK2, a, 3)
        text(c, f"{v}%", cx + tw / 2 + 26 * s, yv(v) + 9 * s, 26 * s, "black", INK, a, align="left")


def pizza360(c, cx, cy, r, a, graus=54, col=None):
    """ep5: pizza de 360° com um setor destacado de `graus`"""
    if a <= 0:
        return
    c.drawCircle(cx, cy, r, paint("#F3F3F0", a))
    c.drawCircle(cx, cy, r, paint(INK2, a, stroke=3))
    p = skia.Path(); p.moveTo(cx, cy)
    p.arcTo(skia.Rect.MakeXYWH(cx - r, cy - r, 2 * r, 2 * r), -90, graus, False); p.close()
    c.drawPath(p, paint(col or BLUE, a))


def icone(c, k, cx, cy, s=1.0, a=1.0):
    """os 5 ícones da série (índice da revisão), em escala s em volta de (cx, cy)"""
    if a <= 0:
        return
    c.save(); c.translate(cx, cy); c.scale(s, s)
    if k == 0:      # ep1 o triângulo
        triangulo(c, 0, -14, 250, a, "taxa", 1.0)
        text_mid(c, "parte · total × taxa", 0, 140, 26, "black", INK2, a)
    elif k == 1:    # ep2 a máquina de fator
        maquina(c, 0, -10, "1,25", a, 20)
        text_mid(c, "o 1 é o que já tinha", 0, 130, 26, "black", INK2, a)
    elif k == 2:    # ep3 a bola de neve
        bola(c, -105, 10, 44, a, "100", 26)
        arrow(c, -50, 10, 0, 10, INK2, a, 5, 14)
        bola(c, 85, -5, 80, a, "132", 36)
        text_mid(c, "multiplique os fatores", 0, 130, 26, "black", INK2, a)
    elif k == 3:    # ep4 a base mudou
        barras_base(c, 0, -30, a, 1.0, 1.25, 80)
        text_mid(c, "a base mudou", 0, 130, 26, "black", AMBER, a)
    elif k == 4:    # ep5 termômetro e pizza
        termometro(c, -95, -20, a, s=0.75)
        pizza360(c, 85, -10, 70, a)
        text_mid(c, "p.p. · 1% = 3,6°", 0, 130, 26, "black", INK2, a)
    c.restore()


def conferido(c, s, x, y, a, ok=True, size=32):
    if a <= 0:
        return
    check_icon(c, x, y - size * 0.32, size * 0.62, a, GREEN if ok else RED, "check" if ok else "x")
    ftext(c, s, x + size * 0.95, y, size, "black", GREEN if ok else RED, a, align="left")


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "REVISÃO FINAL", BLUE)
    aa = ep(t, C["01.a"], 0.5)
    if aa > 0:
        rrect(c, 260, 200, 640, 230, 24, mix("#FFFFFF", PURPLE, 0.10), aa, shadow=True)
        fmid(c, "%", 420, 315, 120, "black", PURPLE, aa)
        text(c, "PORCENTAGEM", 680, 300, 42, "black", PURPLE, aa)
        text(c, "× regra de três", 680, 360, 32, "bold", INK2, aa)
    ab = ep(t, C["01.b"], 0.5)
    if ab > 0:
        rrect(c, 1020, 200, 640, 230, 24, mix("#FFFFFF", GREEN, 0.10), ab, shadow=True)
        text(c, "ESSE PONTO", 1340, 290, 46, "black", GREEN, ab)
        text(c, "já é seu?", 1340, 365, 50, "black", INK, ab)
    for k in range(5):
        icone(c, k, 330 + k * 315, 600, 0.55, ep(t, C["01.b"] + 1.0 + 0.25 * k, 0.4))
    ac = ep(t, C["01.c"], 0.5)
    chip(c, "TREINO", 640, 800, PURPLE, ac, 36)
    chip(c, "9 FRASES", 960, 800, AMBER, ep(t, C["01.c"] + 0.5, 0.4), 36)
    chip(c, "5 QUESTÕES", 1280, 800, GREEN, ep(t, C["01.c"] + 1.0, 0.4), 36)


FORMATOS = [("02.a", "AUMENTOS E DESCONTOS", "preços, salários, tarifas"),
            ("02.b", "SUCESSIVAS", "mudanças em sequência"),
            ("02.c", "VARIAÇÃO NA TABELA", "entre dois valores"),
            ("02.d", "PONTOS PERCENTUAIS", "desemprego, juros, aprovação"),
            ("02.e", "GRÁFICOS", "pizza e barras")]


def mini(c, k, x, y, a):
    """desenhinho de cada formato"""
    if k == 0:
        ftext(c, "+20%", x - 60, y, 40, "black", GREEN, a)
        ftext(c, "−30%", x + 60, y, 40, "black", RED, a)
    elif k == 1:
        ftext(c, "×1,1 ×1,2", x, y, 38, "black", PURPLE, a)
    elif k == 2:
        for i in range(3):
            for j in range(2):
                rrect(c, x - 70 + j * 74, y - 50 + i * 30, 68, 24, 5, mix("#FFFFFF", BLUE, 0.25 if j else 0.12), a)
    elif k == 3:
        termometro(c, x, y - 10, a, s=0.42)
    elif k == 4:
        pizza360(c, x, y - 12, 48, a, 120, BLUE)


def b_formatos(c, t, C, B):
    frame(c, t, B["start"], "COMO APARECE NA PROVA", "OS FORMATOS MAIS FREQUENTES", BLUE)
    for k, (cue, tit, sub) in enumerate(FORMATOS):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        x = 300 + k * 330
        rrect(c, x - 150, 250 + d, 300, 440, 24, "#F7F7F5", a)
        badge_num(c, k + 1, x, 302 + d, a, 24, bg=BLUE)
        mini(c, k, x, 420 + d, a)
        para(c, tit, x, 540 + d, 28, "black", BLUE, a, 270, 34, align="center")
        para(c, sub, x, 625 + d, 22, "bold", INK2, a, 260, 28, align="center")
    at = ep(t, C["02.e"] + 1.0, 0.5)
    pill(c, "por trás de todos: o FATOR de multiplicação", W / 2, 770, PURPLE, size=28, a=at, anchor="center")


INDICE = [("EP. 1", "o triângulo · a base é de onde você partiu"), ("EP. 2", "a máquina de fator · o 1 já existia"),
          ("EP. 3", "bola de neve: multiplique os fatores"), ("EP. 4", "a base mudou · volte DIVIDINDO pelo fator"),
          ("EP. 5", "p.p. = grau no termômetro · 1% = 3,6°")]
IND_CUES = ["03.a", "03.b", "03.c", "04.a", "04.b"]
IND_POS = [(440, 190), (960, 190), (1480, 190), (700, 500), (1220, 500)]


def b_indice(c, t, C, B):
    frame(c, t, B["start"], "ANTES DE COBRAR", "UMA FRASE POR EPISÓDIO", PURPLE)
    for k, (ep_, s) in enumerate(INDICE):
        a = ep(t, C[IND_CUES[k]], 0.5)
        if a <= 0:
            continue
        nxt = C[IND_CUES[k + 1]] if k + 1 < len(IND_CUES) else C["04.end"]
        on_ = 1.0 if C[IND_CUES[k]] - 0.05 <= t < nxt else 0.0
        x, y = IND_POS[k]
        rrect(c, x - 240, y, 480, 290, 22, mix("#F7F7F5", PURPLE, 0.10 * on_), a)
        if on_:
            c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x - 240, y, 480, 290), 22, 22), paint(PURPLE, a, stroke=4))
        pill(c, ep_, x, y + 30, PURPLE if on_ else INK2, size=20, a=a, anchor="center", bounds=(0, 1920))
        icone(c, k, x, y + 135, 0.5, a)
        para(c, s, x, y + 245, 22, "black", INK if on_ else INK2, a, 440, 27, align="center")


HABITOS = [("05.a", "1", "CONVERTA EM FATOR", "a questão vira uma multiplicação", PURPLE),
           ("05.b", "2", "USE 100", "sem valor no enunciado? a resposta sai em %", BLUE),
           ("05.c", "3", "CONFIRA O SENTIDO", "iguais terminam ABAIXO · desconto sobre desconto < soma", GREEN)]


def b_estrategia(c, t, C, B):
    frame(c, t, B["start"], "NA HORA DA PROVA", "ESTRATÉGIA EM 3 HÁBITOS", GREEN)
    for k, (cue, n, tit, sub, col) in enumerate(HABITOS):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        x = 400 + k * 560
        rrect(c, x - 250, 230 + d, 500, 530, 24, mix("#F7F7F5", col, 0.08), a)
        badge_num(c, n, x, 290 + d, a, 30, bg=col)
        if k == 0:
            maquina(c, x, 440 + d, "1,20", a, 40 * ep(t, C[cue], 2.0), col)
        elif k == 1:
            bola(c, x, 440 + d, 80, a, "100", 44)
        else:
            barras_base(c, x, 410 + d, a, 1.0, 0.95, 60)
        text(c, tit, x, 610 + d, 32, "black", col, a)
        para(c, sub, x, 660 + d, 24, "bold", INK2, a, 440, 30, align="center")


# treino: (cue, variação, fator, cor)
TREINO = [("b", "+12%", "1,12", GREEN), ("c", "−8%", "0,92", RED), ("d", "+200%", "3", GREEN),
          ("e", "−35%", "0,65", RED), ("f", "+7,5%", "1,075", GREEN), ("g", "−2%", "0,98", RED)]


def b_treino(c, t, C, B):
    head_seq(c, t, C, [("06", "TREINO-RELÂMPAGO", "VARIAÇÃO → FATOR", PURPLE),
                       ("07", "CONFERINDO", "UM MAIS OU UM MENOS A TAXA", PURPLE)])
    card(c, *CARD_R)
    for k, (cue, var, fat, col) in enumerate(TREINO):
        a, d = rise(t, C[f"06.{cue}"])
        if a <= 0:
            continue
        r_, j = divmod(k, 3)
        x, y = 470 + j * 490, 230 + r_ * 245 + d
        ar = ep(t, C[f"07.{cue}"], 0.4) if t >= C["07"] else 0
        rrect(c, x - 210, y, 420, 205, 20, mix("#F7F7F5", col, 0.10 * ar), a)
        szv = 52
        while ftw(var, szv) > 150:
            szv -= 2
        ftext(c, var, x - 40, y + 100 + szv * 0.36, szv, "black", col, a, align="right")
        arrow(c, x - 25, y + 100, x + 25, y + 100, INK2, a, 5, 14)
        if ar <= 0:
            fmid(c, "?", x + 100, y + 100, 60, "black", AMBER, a)
        else:
            sz = 60
            while ftw("× " + fat, sz) > 160:
                sz -= 2
            ftext(c, "× " + fat, x + 40, y + 100 + sz * 0.36, sz, "black", PURPLE, ar, align="left")
            if var == "+200%":
                pill(c, "TRIPLICA", x, y + 172, AMBER, size=20, a=ar, anchor="center", bounds=(0, 1920))
    pause_timer(c, t, C["06.end"] - 1.9, W / 2, 770)
    aa = ep(t, C["07.a"], 0.5)
    if aa > 0:
        boxed(c, 420, 728, 1080, 84, PURPLE, aa, 0.08)
        text_mid(c, "aumento: 1 + taxa  ·  desconto: 1 − taxa", W / 2, 770, 34, "black", PURPLE, aa)


# ======================================================================
# verdadeiro ou falso
# ======================================================================

def b_vf_intro(c, t, C, B):
    frame(c, t, B["start"], "PAUSE E RESPONDA", "VERDADEIRO OU FALSO?", AMBER)
    a0 = ep(t, C["08"], 0.5)
    chip(c, "V", 820, 360, GREEN, a0, 90)
    fmid(c, "ou", W / 2, 360, 50, "black", GRAY, a0)
    chip(c, "F", 1100, 360, RED, a0, 90)
    aa = ep(t, C["08.a"], 0.5)
    for k in range(9):
        badge_num(c, k + 1, W / 2 - 4 * 90 + k * 90, 560, ep(t, C["08.a"] + 0.12 * k, 0.3), 30, bg=INK2)
    text(c, "os erros que mais custam pontos", W / 2, 650, 32, "bold", INK2, aa)
    pill(c, "pause ANTES da resposta", W / 2, 750, AMBER, size=30, a=ep(t, C["08.b"], 0.5), anchor="center")


# (contexto, afirmação, verdadeira?, por que engana, regra certa, versão certa, ícone, base mudou?)
VF = [
    ("+10% e depois +20%", "dão +30%", False, "10 + 20 = 30",
     "o 2º aumento incide sobre o valor já aumentado", "1,10 × 1,20 = 1,32", 2, False),
    ("+20% e depois −20%", "termina 4% abaixo", True, "parece que um desfaz o outro",
     "o desconto foi sobre 120, não sobre 100", "100 → 120 → 96", 3, True),
    ("depois de +25%", "25% de desconto volta ao preço", False, "é o mesmo número",
     "divida pelo fator: 1 ÷ 1,25 = 0,80", "desconto de 20%", 3, True),
    ("R$ 150 já com 20% de desconto", "original = R$ 187,50", True, "o instinto soma 20% e dá 180",
     "os 20% foram sobre o original: divida por 0,80", "150 ÷ 0,80 = 187,50", 3, True),
    ("30% de desconto + 10% no caixa", "dão 40% de desconto", False, "a soma é 40",
     "0,70 × 0,90 = 0,63: você paga 63%", "desconto de 37%", 2, False),
    ("desemprego de 8% para 10%", "subiu 2%", False, "10 − 8 = 2",
     "subiu 2 PONTOS PERCENTUAIS; relativo: 2 ÷ 8", "2 p.p. = +25%", 4, False),
    ("aumentar 200%", "é triplicar", True, "200 lembra o dobro",
     "fator = 1 + 2 = 3: o 1 é o que você já tinha", "× 3", 1, False),
    ("de 50 para 40", "queda de 25%", False, "de 40 para 50 é +25%",
     "a base é de onde você partiu: 10 ÷ 50", "queda de 20%", 0, True),
    ("30% dos homens e 30% das mulheres", "60% do grupo", False, "as duas estão na mesma frase",
     "só se somam porcentagens do MESMO todo", "não some bases diferentes", 4, False),
]
VF_IDS = [f"{9 + k:02d}" for k in range(9)]


def b_vf(c, t, C, B):
    sid = which(t, C, VF_IDS)
    n = VF_IDS.index(sid)
    ctx, conta, ver, engana, regra_, fix, ic, base = VF[n]
    head(c, t, C[sid], f"VERDADEIRO OU FALSO? · {n + 1} DE 9", "PAUSE E RESPONDA", AMBER)
    card(c, *CARD_R)
    q = lambda x: C[f"{sid}.{x}"]
    for k in range(9):
        badge_num(c, k + 1, W / 2 - 4 * 66 + k * 66, 200, 1, 20, bg=AMBER if k == n else LIGHT)
    a0 = ep(t, q("t"), 0.5)
    icone(c, ic, 330, 400, 0.62, a0)
    sz0 = 32
    while ftw(ctx, sz0, "bold") > 760:
        sz0 -= 1
    text(c, ctx, 960, 310, sz0, "bold", INK2, a0)
    ar = ep(t, q("r"), 0.4)
    sz = 56
    while ftw(conta, sz) > 760:
        sz -= 2
    fmid(c, conta, 960, 410, sz, "black", INK, a0)
    if ar > 0 and not ver:
        w = ftw(conta, sz)
        strike(c, 960 - w / 2 - 10, 415, 960 + w / 2 + 10, 415, ar, RED, ar)
    pause_timer(c, t, q("p"), 1620, 410, a=1 - ar)
    selo(c, 1580, 410, ar, "VERDADEIRO" if ver else "FALSO", GREEN if ver else RED, -6, 40)
    ae = ep(t, q("e"), 0.5)
    if ae > 0:
        if ver:
            pill(c, "PARECE FALSO PORQUE...", 230, 540, AMBER, size=26, a=ae, bounds=(0, 1920))
        else:
            selo(c, 350, 540, ae, "PEGADINHA", AMBER, -5, 30)
        text(c, engana, 640 if ver else 520, 552, 34, "bold", INK2, ae, align="left")
    ag = ep(t, q("g"), 0.5)
    if ag > 0:
        boxed(c, 200, 630, 1520, 170, GREEN, ag, 0.07)
        para(c, regra_, 240, 700, 30, "black", GREEN, ag, 760)
        szf = 44
        while ftw(fix, szf) > 600:
            szf -= 2
        fmid(c, fix, 1340, 715, szf, "black", GREEN, ag)
        if base:
            selo(c, 1560, 590, ag, "A BASE MUDOU", AMBER, -5, 24)


def b_vf_placar(c, t, C, B):
    frame(c, t, B["start"], "QUANTAS VOCÊ ACERTOU?", "O PLACAR", AMBER)
    aa = ep(t, C["18.a"], 0.5)
    for k, v in enumerate(VF):
        a = aa * ep(t, C["18.a"] + 0.12 * k, 0.3)
        x = W / 2 - 4 * 150 + k * 150
        badge_num(c, k + 1, x, 260, a, 26, bg=INK2)
        chip(c, "V" if v[2] else "F", x, 360, GREEN if v[2] else RED, a, 50)
    text(c, "6 falsas · 3 verdadeiras", W / 2, 490, 40, "black", INK, aa)
    ab = ep(t, C["18.b"], 0.5)
    chip(c, "AGORA: 5 QUESTÕES INÉDITAS", W / 2, 620, GREEN, ab, 44)
    text(c, "fatores primeiro · confira com 100", W / 2, 740, 32, "black", PURPLE, ab)


# ======================================================================
# as 5 questões inéditas
# ======================================================================
# enun: (cue, texto, destaque?) · selo1: (rótulo, linha, cor, cue) · passos: (cue, texto) · confere: (cue, texto)

Q = {
    "q1": dict(ids=("19", "20"), titulo="AS MATRÍCULAS", ok="B",
               enun=[("a", "Uma escola registrou suas matrículas:", False)],
               tabela=[("2022", "800"), ("2023", "1 000"), ("2024", "900")],
               enun2=("b", "Em relação a 2023, as matrículas de 2024"),
               alts=[("A", "aumentaram 12,5%", "comparou com 2022", AMBER), ("B", "caíram 10%", "", GREEN),
                     ("C", "caíram cerca de 11,1%", "base = valor final", RED),
                     ("D", "caíram 90%", "o que ficou", AMBER), ("E", "caíram 100%", "100 alunos ≠ 100%", RED)],
               selo1=("DE ONDE VOCÊ PARTIU?", "a base é 2023: 1 000", AMBER, "d"),
               passos=[("a", "900 − 1 000 = −100"), ("b", "−100 ÷ 1 000 = −0,10"), ("c", "caíram 10%")],
               confere=None),
    "q2": dict(ids=("21", "22"), titulo="O PREÇO QUE SOBE E DESCE", ok="A",
               enun=[("a", "O preço de um produto subiu 20%, depois caiu 25% e depois subiu 10%, sempre sobre o preço do "
                           "momento.", False),
                     ("b", "Em relação ao início, o preço final ficou", True)],
               alts=[("A", "1% mais barato", "", GREEN), ("B", "5% mais caro", "somou as taxas", RED),
                     ("C", "10% mais barato", "esqueceu o 3º fator", AMBER),
                     ("D", "99% mais barato", "leu o fator", AMBER), ("E", "igual", "achou que compensa", RED)],
               selo1=("FATORES PRIMEIRO", "1,20 · 0,75 · 1,10", PURPLE, "d"),
               passos=[("a", "1,20 × 0,75 × 1,10 = 0,99"), ("c", "1% mais barato")],
               confere=("b", "com 100: 120 → 90 → 99")),
    "q3": dict(ids=("23", "24"), titulo="O CELULAR", ok="D",
               enun=[("a", "Um celular custa R$ 1 360,00 já com 15% de desconto.", False),
                     ("b", "Qual era o preço original?", True)],
               alts=[("A", "R$ 204,00", "só a parte", RED), ("B", "R$ 1 156,00", "descontou de novo", RED),
                     ("C", "R$ 1 564,00", "somou 15%", AMBER), ("D", "R$ 1 600,00", "", GREEN),
                     ("E", "R$ 9 066,67", "dividiu pela taxa", AMBER)],
               selo1=("PARA VOLTAR, DIVIDA", "fator do desconto: 1 − 0,15 = 0,85", PURPLE, "d"),
               passos=[("a", "1 360 ÷ 0,85 = 1 600")],
               confere=("v", "1 600 × 0,85 = 1 360")),
    "q4": dict(ids=("25", "26"), titulo="A APROVAÇÃO", ok="E",
               enun=[("a", "A aprovação de um prefeito caiu de 60% para 45%.", False),
                     ("b", "Sobre essa mudança, é correto afirmar que a aprovação", True)],
               alts=[("A", "caiu 15%", "erro de linguagem", RED), ("B", "caiu 25 p.p.", "trocou os dois", AMBER),
                     ("C", "caiu 33,3%", "base = valor final", RED), ("D", "caiu 75%", "o que restou", AMBER),
                     ("E", "caiu 15 p.p., ou 25% do que era", "", GREEN)],
               selo1=("O TERMÔMETRO", "p.p. = a diferença · % = em relação ao que era", PURPLE, "d"),
               passos=[("a", "60 − 45 = 15 p.p."), ("b", "15 ÷ 60 = 0,25 = 25%")],
               confere=None),
    "q5": dict(ids=("27", "28"), titulo="AS BICICLETAS", ok="C",
               enun=[("a", "Uma escola tem 200 meninos e 300 meninas.", False),
                     ("b", "30% dos meninos e 40% das meninas vão de bicicleta.", False),
                     ("c", "Que porcentagem de todos os alunos vai de bicicleta?", True)],
               alts=[("A", "12%", "multiplicou as taxas", AMBER), ("B", "35%", "média sem pesar", AMBER),
                     ("C", "36%", "", GREEN), ("D", "60%", "só as meninas", RED), ("E", "70%", "somou as %", RED)],
               selo1=("BASES DIFERENTES", "não some: volte para pessoas", AMBER, "d"),
               passos=[("a", "30% de 200 = 60 · 40% de 300 = 120"), ("b", "60 + 120 = 180 de 500"),
                       ("c", "180 ÷ 500 = 36%")],
               confere=None),
}


def selo_linha(c, x, y, w, rotulo, s, col, a):
    """caixa com rótulo e uma linha curta"""
    if a <= 0:
        return
    boxed(c, x, y, w, 84, col, a, 0.08)
    pill(c, rotulo, x + 20, y, col, size=18, a=a, bounds=(0, 1920))
    sz = 26
    while ftw(s, sz) > w - 40:
        sz -= 1
    ftext(c, s, x + 20, y + 54, sz, "black", INK, a, align="left")


def tabela(c, x, y, linhas, a, dest=None, dest_a=0.0):
    """tabela ano | matrículas; dest = índice da linha da base (âmbar)"""
    if a <= 0:
        return
    rrect(c, x, y, 420, 50, 10, BLUE, a)
    ftext(c, "ANO", x + 100, y + 35, 24, "black", "#FFFFFF", a)
    ftext(c, "MATRÍCULAS", x + 300, y + 35, 24, "black", "#FFFFFF", a)
    for k, (ano, v) in enumerate(linhas):
        yy = y + 56 + k * 56
        hl = dest_a if dest == k else 0
        rrect(c, x, yy, 420, 50, 10, mix(mix("#F7F7F5", BLUE, 0.06 * (k % 2)), AMBER, 0.35 * hl), a)
        ftext(c, ano, x + 100, yy + 35, 28, "black", INK, a)
        ftext(c, v, x + 300, yy + 35, 30, "black", INK, a)


def faz_questao(nome):
    d = Q[nome]
    s1, s2 = d["ids"]
    num = int(nome[1])

    def bloco(c, t, C, B):
        head(c, t, B["start"], f"QUESTÃO {num} DE 5 · ESTILO ENEM", d["titulo"], BLUE)
        card(c, *CARD_R)
        a0 = ep(t, C[s1], 0.5)
        pill(c, "QUESTÃO EXTRA DA SÉRIE (ESTILO ENEM)", 180, 200, BLUE, size=20, a=a0, bounds=(0, 1920))
        text(c, "Situação hipotética, elaborada para fins didáticos.", 180, 828, 18, "medium", GRAY, a0, align="left")
        sol = ep(t, C[s2], 0.5)
        cues_in = {L: C[f"{s1}.l{L.lower()}"] for L in "ABCDE"}
        cues_x = {L: C[f"{s2}.x{L.lower()}"] for L in "ABCDE" if L != d["ok"]}
        y = 270
        for cue, s, dest in d["enun"]:
            a = ep(t, C[f"{s1}.{cue}"], 0.4) * (1 - sol)
            h = para(c, s, 180, y + 22, 29, "black" if dest else "bold", BLUE if dest else INK, a, 640, 38)
            y += h + 16
        if "tabela" in d:
            at = ep(t, C[f"{s1}.a"], 0.4)
            ty = 330 if sol <= 0 else lerp(330, 250, sol)
            tabela(c, 230, ty, d["tabela"], at, 1, ep(t, C[f"{s2}.d"], 0.4))
            cue, s = d["enun2"]
            a2 = ep(t, C[f"{s1}.{cue}"], 0.4) * (1 - sol)
            para(c, s, 180, 600, 29, "black", BLUE, a2, 640, 38)
        pause_timer(c, t, C[f"{s1}.end"] - 1.9, 500, 760)
        K.alternativas(c, t, C, d["alts"], 880, 230, 820, 34, C[f"{s2}.ok"], d["ok"], cues_in, cues_x, gap=14)
        if sol > 0:
            rot, s_, col, cue = d["selo1"]
            tem_tab = "tabela" in d
            sy = 520 if tem_tab else 250
            selo_linha(c, 170, sy, 650, rot, s_, col, ep(t, C[f"{s2}.{cue}"], 0.4) * sol)
            yy = 650 if tem_tab else 400
            for j, (cue, s) in enumerate(d["passos"]):
                a = ep(t, C[f"{s2}.{cue}"], 0.4) * sol
                last = j == len(d["passos"]) - 1
                sz = 34
                while ftw(s, sz) > 640:
                    sz -= 2
                if tem_tab:
                    ftext(c, s, 180 + j * 0, yy, sz, "black", GREEN if last else INK, a, align="left")
                    yy += 50
                else:
                    ftext(c, s, 180, yy, sz, "black", GREEN if last else INK, a, align="left")
                    yy += 62
            if d["confere"]:
                cue, s = d["confere"]
                conferido(c, s, 190, yy + 20, ep(t, C[f"{s2}.{cue}"], 0.4) * sol, True, 32)
            if nome in ("q3",):
                selo(c, 700, 470, ep(t, C[f"{s2}.xc"], 0.4) * sol, "A BASE MUDOU", AMBER, -6, 24)
            result_box(c, f"Letra {d['ok']}", 1290, 690, 38, ep(t, C[f"{s2}.ok"], 0.5), GREEN)
    return bloco


# ======================================================================
# checklist, meta, ponte e CTA
# ======================================================================

CHECK = [("29.b", "EP. 1", ["os três cálculos", "denominador = valor inicial", "10%, 1%, 5% e 15% de cabeça"]),
         ("29.c", "EP. 2", ["escrever o fator", "ler o fator ao contrário", "200% = triplicar"]),
         ("29.d", "EP. 3", ["sucessivas: multiplicar os fatores"]),
         ("30.a", "EP. 4", ["iguais não se anulam", "voltar: dividir pelo fator", "preço antes do desconto"]),
         ("30.b", "EP. 5", ["ponto percentual × por cento", "porcentagem ↔ ângulo do setor", "bases diferentes não se somam"])]


def b_checklist(c, t, C, B):
    frame(c, t, B["start"], "CHECKLIST DE DOMÍNIO", "MARQUE SÓ O QUE EXPLICA EM VOZ ALTA", GREEN)
    aa = ep(t, C["29.a"], 0.5) * (1 - ep(t, C["29.b"], 0.4))
    pill(c, "explicar em voz alta, sem consultar nada", W / 2, 470, GREEN, size=34, a=aa, anchor="center")
    for k, (cue, ep_, itens) in enumerate(CHECK):
        a = ep(t, C[cue], 0.5)
        if a <= 0:
            continue
        col_ = 0 if k < 3 else 1
        x = 170 if col_ == 0 else 990
        y0 = 190 + sum(len(CHECK[j][2]) * 46 + 30 for j in range(0 if col_ == 0 else 3, k))
        pill(c, ep_, x, y0 + 18, PURPLE, size=20, a=a, bounds=(0, 1920))
        for j, it in enumerate(itens):
            yy = y0 + 18 + j * 46
            rrect(c, x + 110, yy - 15, 30, 30, 7, "#FFFFFF", a, stroke=3, stroke_color=INK2)
            K.ftext(c, it, x + 158, yy + 10, 27, "bold", INK, a, align="left")
    ae = ep(t, C["30.c"], 0.5)
    if ae > 0:
        boxed(c, 990, 690, 720, 100, AMBER, ae, 0.10)
        text_mid(c, "não marcou? reveja o episódio", 1350, 740, 32, "black", INK, ae)


def b_meta(c, t, C, B):
    frame(c, t, B["start"], "ANTES DE DIZER “DOMINADO”", "A META", GREEN)
    aa = ep(t, C["31.a"], 0.5)
    ab = ep(t, C["31.b"], 0.5)
    for i in range(40):
        r_, k = divmod(i, 10)
        a = aa * ep(t, C["31.a"] + 0.025 * i, 0.2)
        ok = ab > 0 and i < 28
        x, y = 230 + k * 82, 220 + r_ * 86
        rrect(c, x, y, 66, 70, 12, mix("#E6E6E2", GREEN, ab if ok else 0), a)
        if ok:
            check_icon(c, x + 33, y + 35, 18, ab, "#FFFFFF")
        else:
            text_mid(c, str(i + 1), x + 33, y + 35, 24, "black", INK2, a)
    text(c, "40 questões", 1450, 300, 52, "black", INK, aa)
    text(c, "(não 30)", 1450, 360, 32, "bold", AMBER, aa)
    text(c, "28 acertos = 70%", 1450, 450, 46, "black", GREEN, ab)
    ac = ep(t, C["31.c"], 0.5)
    if ac > 0:
        boxed(c, 230, 600, 1460, 170, AMBER, ac, 0.10)
        icone(c, 2, 400, 690, 0.42, ac)
        icone(c, 3, 1520, 690, 0.42, ac)
        text_mid(c, "priorize: SUCESSIVAS e VOLTAR", W / 2, 668, 38, "black", INK, ac)
        text_mid(c, "ao valor original", W / 2, 718, 32, "bold", INK2, ac)


def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "SÉRIE COMPLETA", "PRÓXIMO ASSUNTO", PURPLE)
    aa = ep(t, C["32.a"], 0.5)
    text(c, "PRÓXIMO ASSUNTO", W / 2, 250, 28, "black", GRAY, aa, tracking=2)
    text(c, "Unidades e conversões", W / 2, 330, 62, "black", PURPLE, aa)
    for k, s in enumerate(("km → m", "h → min", "L → m³")):
        chip(c, s, 640 + k * 320, 450, BLUE, aa * ep(t, C["32.a"] + 0.6 + 0.3 * k, 0.4), 34)
    ab = ep(t, C["32.b"], 0.5)
    if ab > 0:
        boxed(c, 440, 560, 1040, 200, GREEN, ab, 0.08)
        text(c, "mais adiante:", W / 2, 615, 28, "bold", INK2, ab)
        ftext(c, "1,10 × 1,10 × 1,10 = 1,10³", W / 2, 680, 44, "black", GREEN, ab)
        text(c, "o mesmo fator repetido vira JUROS COMPOSTOS", W / 2, 735, 28, "black", INK, ab)


def b_cta(c, t, C, B):
    cta(c, t, C["33.like"], C["33.sub"], C["33.bell"], C["33.com"], C["33.bye"], "Qual pegadinha te pegou?",
        canal="no Estudativo", anki=C["33.anki"])


BLOCKS = dict(hook=b_hook, formatos=b_formatos, indice=b_indice, estrategia=b_estrategia, treino=b_treino,
              vf_intro=b_vf_intro, vf=b_vf, vf_placar=b_vf_placar, q1=faz_questao("q1"), q2=faz_questao("q2"),
              q3=faz_questao("q3"), q4=faz_questao("q4"), q5=faz_questao("q5"), checklist=b_checklist, meta=b_meta,
              ponte=b_ponte, cta=b_cta)
