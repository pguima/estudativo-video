"""Visual — Notação Científica e Ordem de Grandeza, Episódio 6: Revisão geral, pegadinhas e treino nas áreas (tema claro).
Peças comuns da série em ../../comum.py (reexporta o 019/comum.py: expr com potências, alternativas, pause_timer...).
Índice visual da revisão: os 5 ícones dos episódios (icone()) · ícones das áreas nas questões (icone_area()).
Cores com função: azul = definição · roxo = regra/fórmula · âmbar = armadilha · verde = atalho/dica · vermelho = erro.
"""
import importlib.util
from pathlib import Path
import skia
import motor
motor.set_theme("claro")
from motor import *  # noqa
from aula import *  # noqa

_p = Path(__file__).resolve().parents[2] / "comum.py"
_s = importlib.util.spec_from_file_location("comum020", _p)
K = importlib.util.module_from_spec(_s); _s.loader.exec_module(K)
K.usar_tempos(Path(__file__).resolve().parents[1] / "audio" / "tempos.json")
motor.set_theme("claro")
expr, expr_w = K.expr, K.expr_w
frame, head_seq, which, para, boxed, regra, selo, pause_timer, chip = (K.frame, K.head_seq, K.which, K.para, K.boxed, K.regra,
                                                                        K.selo, K.pause_timer, K.chip)
fmid, ftext = K.fmid, K.ftext

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_notacao_ep6_revisao.mp4"
CARD_R = K.CARD_R


def _stroke(col, a, w):
    p = paint(col, a, stroke=w, cap_round=True)
    p.setStrokeJoin(skia.Paint.kRound_Join)
    return p


# ======================================================================
# os 5 ícones dos episódios (índice da revisão)
# ======================================================================

def icone(c, k, cx, cy, s=1.0, a=1.0):
    if a <= 0:
        return
    if k == 0:      # ep1 placa de carro
        w, h = 230 * s, 110 * s
        rrect(c, cx - w / 2, cy - h / 2, w, h, 14 * s, "#FFFFFF", a, stroke=4 * s, stroke_color=INK)
        rrect(c, cx - w / 2 + 3 * s, cy - h / 2 + 3 * s, w - 6 * s, 24 * s, 10 * s, BLUE, a)
        text_mid(c, "UM SÓ JEITO", cx, cy - h / 2 + 15 * s, 14 * s, "black", "#FFFFFF", a)
        expr(c, "3,84·10^8", cx, cy + 16 * s, 40 * s, a)
    elif k == 1:    # ep2 gangorra
        tri = skia.Path(); tri.moveTo(cx, cy + 10 * s); tri.lineTo(cx - 26 * s, cy + 56 * s); tri.lineTo(cx + 26 * s, cy + 56 * s)
        tri.close(); c.drawPath(tri, paint(INK2, a))
        c.save(); c.translate(cx, cy + 10 * s); c.rotate(-12)
        rrect(c, -120 * s, -8 * s, 240 * s, 16 * s, 8 * s, AMBER, a)
        c.restore()
        expr(c, "40·10^6", cx - 86 * s, cy - 22 * s, 30 * s, a, cores={0: INK})
        expr(c, "4·10^7", cx + 86 * s, cy - 56 * s, 30 * s, a, cores={0: GREEN})
        text_mid(c, "mesmo valor", cx, cy + 76 * s, 18 * s, "black", GREEN, a)
    elif k == 2:    # ep3 notas de valores diferentes
        for j, (lab, col, dx, dy) in enumerate((("10⁵", "#2E9C6A", -54, -18), ("10⁴", "#5B8DEF", 54, 18))):
            x, y = cx + dx * s - 70 * s, cy + dy * s - 38 * s
            rrect(c, x, y, 140 * s, 76 * s, 10 * s, col, a, shadow=True)
            c.drawCircle(x + 70 * s, y + 38 * s, 24 * s, paint("#FFFFFF", a * 0.35))
            text_mid(c, lab, x + 70 * s, y + 38 * s, 30 * s, "black", "#FFFFFF", a)
    elif k == 3:    # ep4 régua do 3,16
        x0, x1, y = cx - 110 * s, cx + 110 * s, cy + 6 * s
        line(c, x0, y, x1, y, INK, a, 4 * s)
        for v, xx, col in (("1", x0, INK), ("3,16", cx, AMBER), ("10", x1, INK)):
            line(c, xx, y - 16 * s, xx, y + 16 * s, col, a, 4 * s)
            text_mid(c, v, xx, y + 40 * s, 22 * s, "black", col, a)
        for xa, xb in ((x0, cx), (cx, x1)):
            arrow(c, xa + 10 * s, y - 30 * s, xb - 10 * s, y - 30 * s, GREEN, a, 3 * s, 9 * s)
            text_mid(c, "×3,16", (xa + xb) / 2, y - 52 * s, 18 * s, "black", GREEN, a)
    elif k == 4:    # ep5 grade de quadradinhos
        n, L = 6, 120 * s
        x, y = cx - L / 2, cy - L / 2 - 6 * s
        rrect(c, x, y, L, L, 6 * s, mix("#FFFFFF", BLUE, 0.15), a)
        for i in range(n + 1):
            line(c, x + i * L / n, y, x + i * L / n, y + L, BLUE, a * 0.7, 2 * s)
            line(c, x, y + i * L / n, x + L, y + i * L / n, BLUE, a * 0.7, 2 * s)
        text_mid(c, "100 × 100", cx, cy + L / 2 + 20 * s, 20 * s, "black", BLUE, a)


# ícones das áreas: 0 Biologia (microscópio) · 1 Física (planeta) · 2 Química (frasco) · 3 Humanas (mapa) · 4 Matemática (régua)
AREAS = ["BIOLOGIA", "FÍSICA", "QUÍMICA", "HUMANAS", "MATEMÁTICA"]
COR_AREA = [GREEN, PURPLE, AMBER, RED, BLUE]


def icone_area(c, k, cx, cy, s=1.0, a=1.0):
    if a <= 0:
        return
    col = COR_AREA[k]
    c.drawCircle(cx, cy, 70 * s, paint(mix("#FFFFFF", col, 0.14), a))
    pe = _stroke(col, a, 7 * s)
    if k == 0:      # microscópio
        c.drawLine(cx - 34 * s, cy + 42 * s, cx + 34 * s, cy + 42 * s, pe)
        pth = skia.Path(); pth.moveTo(cx + 18 * s, cy + 42 * s); pth.quadTo(cx + 40 * s, cy, cx + 10 * s, cy - 22 * s)
        c.drawPath(pth, pe)
        c.save(); c.translate(cx - 4 * s, cy - 14 * s); c.rotate(-28)
        rrect(c, -10 * s, -36 * s, 20 * s, 56 * s, 6 * s, col, a)
        c.restore()
        c.drawLine(cx - 22 * s, cy + 14 * s, cx + 14 * s, cy + 14 * s, pe)
    elif k == 1:    # planeta com anel
        c.drawCircle(cx, cy, 30 * s, paint(col, a))
        c.save(); c.translate(cx, cy); c.rotate(-18)
        c.drawOval(skia.Rect.MakeXYWH(-56 * s, -14 * s, 112 * s, 28 * s), _stroke(AMBER, a, 5 * s))
        c.restore()
    elif k == 2:    # frasco (erlenmeyer)
        pth = skia.Path()
        pth.moveTo(cx - 12 * s, cy - 44 * s); pth.lineTo(cx - 12 * s, cy - 12 * s); pth.lineTo(cx - 38 * s, cy + 40 * s)
        pth.lineTo(cx + 38 * s, cy + 40 * s); pth.lineTo(cx + 12 * s, cy - 12 * s); pth.lineTo(cx + 12 * s, cy - 44 * s)
        liq = skia.Path()
        liq.moveTo(cx - 26 * s, cy + 16 * s); liq.lineTo(cx - 38 * s, cy + 40 * s); liq.lineTo(cx + 38 * s, cy + 40 * s)
        liq.lineTo(cx + 26 * s, cy + 16 * s); liq.close()
        c.drawPath(liq, paint(col, a * 0.7))
        c.drawPath(pth, pe)
        c.drawLine(cx - 20 * s, cy - 44 * s, cx + 20 * s, cy - 44 * s, pe)
    elif k == 3:    # mapa dobrado
        pts = [(-44, -30), (-14, -40), (14, -30), (44, -40), (44, 32), (14, 42), (-14, 32), (-44, 42)]
        pth = skia.Path(); pth.moveTo(cx + pts[0][0] * s, cy + pts[0][1] * s)
        for x_, y_ in pts[1:4]:
            pth.lineTo(cx + x_ * s, cy + y_ * s)
        for x_, y_ in pts[4:]:
            pth.lineTo(cx + x_ * s, cy + y_ * s)
        pth.close()
        c.drawPath(pth, paint("#FFFFFF", a)); c.drawPath(pth, _stroke(col, a, 5 * s))
        c.drawLine(cx - 14 * s, cy - 40 * s, cx - 14 * s, cy + 32 * s, _stroke(col, a, 4 * s))
        c.drawLine(cx + 14 * s, cy - 30 * s, cx + 14 * s, cy + 42 * s, _stroke(col, a, 4 * s))
        c.drawCircle(cx + 28 * s, cy - 6 * s, 8 * s, paint(col, a))
    elif k == 4:    # régua
        c.save(); c.translate(cx, cy); c.rotate(-30)
        rrect(c, -56 * s, -16 * s, 112 * s, 32 * s, 6 * s, col, a)
        for i in range(9):
            hh = 14 if i % 2 == 0 else 8
            c.drawLine((-44 + i * 11) * s, -16 * s, (-44 + i * 11) * s, (-16 + hh) * s, _stroke("#FFFFFF", a, 3 * s))
        c.restore()


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "REVISÃO FINAL", BLUE)
    aa = ep(t, C["01.a"], 0.5)
    if aa > 0:
        boxed(c, 460, 190, 1000, 110, AMBER, aa, 0.10)
        text_mid(c, "um assunto RARO: aparece em quase toda a prova", W / 2, 245, 38, "black", INK, aa)
    ab = ep(t, C["01.b"], 0.5)
    text(c, "Matemática · Ciências da Natureza · Humanas", W / 2, 370, 36, "black", BLUE, ab)
    for k in range(5):
        a = ep(t, C["01.c"] + 0.2 * k, 0.4)
        x = 480 + k * 240
        icone_area(c, k, x, 520, 0.9, a)
        text(c, AREAS[k], x, 625, 22, "black", COR_AREA[k], a)
    ad = ep(t, C["01.d"], 0.5)
    chip(c, "9 PEGADINHAS", 720, 750, AMBER, ad, 40)
    chip(c, "5 QUESTÕES", 1200, 750, GREEN, ep(t, C["01.d"] + 0.6, 0.4), 40)


ONDE = [("02.a", "Matemática", "contas e comparações", "4·10^7", 4),
        ("02.b", "Física", "espaço e energia", "1,5·10^{11} m", 1),
        ("02.c", "Química", "quantidades minúsculas", "6·10^{23}", 2),
        ("02.d", "Biologia", "células e vírus", "10^{-7} m", 0),
        ("02.e", "Humanas", "população e verbas", "2·10^8", 3)]


def b_onde(c, t, C, B):
    frame(c, t, B["start"], "ONDE ELE APARECE", "QUASE TODA A PROVA", BLUE)
    for k, (cue, s, sub, f_, ic) in enumerate(ONDE):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        x = 300 + k * 330
        rrect(c, x - 150, 200 + d, 300, 450, 22, "#F7F7F5", a)
        icone_area(c, ic, x, 300 + d, 0.8, a)
        expr(c, f_, x, 450 + d, 40, a, cores={0: PURPLE, 1: PURPLE})
        text(c, s, x, 545 + d, 32, "black", COR_AREA[ic], a)
        para(c, sub, x, 600 + d, 22, "bold", GRAY, a, 280, 28, align="center")
    af = ep(t, C["02.f"], 0.5)
    if af > 0:
        boxed(c, 300, 690, 1320, 110, GREEN, af, 0.08)
        text_mid(c, "alternativas em escalas diferentes? a potência de 10 já elimina QUATRO", W / 2, 745, 32, "black",
                 GREEN, af)


RENDEM = [("03.a", "1 · SOMAR", "com expoentes diferentes", "3·10^5 + 0,8·10^5"),
          ("03.b", "2 · ÁREA E VOLUME", "o fator ao quadrado e ao cubo", "1 m^2 = 10^4 cm^2"),
          ("03.c", "3 · ORDEM DE GRANDEZA", "não é o expoente escrito", "7,2·10^5 → 10^6")]


def b_rendem(c, t, C, B):
    frame(c, t, B["start"], "POUCO TEMPO?", "AS TRÊS QUE MAIS RENDEM", GREEN)
    for k, (cue, tit, sub, f_) in enumerate(RENDEM):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        x = 420 + k * 540
        rrect(c, x - 250, 220 + d, 500, 470, 24, "#F7F7F5", a)
        text(c, tit, x, 290 + d, 36, "black", GREEN, a)
        text(c, sub, x, 340 + d, 26, "bold", INK2, a)
        expr(c, f_, x, 500 + d, 44, a, cores={i: PURPLE for i in range(1, 4)})


INDICE = [("EP. 1", "placa de carro · cadeiras vazias"), ("EP. 2", "duas pistas · a gangorra"),
          ("EP. 3", "notas diferentes · quantas Luas"), ("EP. 4", "o meio do caminho: 3,16 · guardanapo"),
          ("EP. 5", "a grade e o cubo de cubinhos")]
IND_CUES = ["04.a", "04.b", "05.a", "05.b", "05.c"]


def b_indice(c, t, C, B):
    frame(c, t, B["start"], "ANTES DE COBRAR", "UMA FRASE POR EPISÓDIO", PURPLE)
    for k, (ep_, s) in enumerate(INDICE):
        a = ep(t, C[IND_CUES[k]], 0.5)
        if a <= 0:
            continue
        nxt = C[IND_CUES[k + 1]] if k + 1 < len(IND_CUES) else C["05.end"]
        on_ = 1.0 if C[IND_CUES[k]] - 0.05 <= t < nxt else 0.0
        if k < 3:
            x, y = 420 + k * 540, 195
        else:
            x, y = 420 + 270 + (k - 3) * 540, 515
        rrect(c, x - 245, y, 490, 290, 22, mix("#F7F7F5", PURPLE, 0.10 * on_), a)
        if on_:
            c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x - 245, y, 490, 290), 22, 22), paint(PURPLE, a, stroke=4))
        pill(c, ep_, x, y + 34, PURPLE if on_ else INK2, size=22, a=a, anchor="center", bounds=(0, 1920))
        icone(c, k, x, y + 140, 0.8, a)
        para(c, s, x, y + 255, 26, "black", INK if on_ else INK2, a, 450, align="center")


# ======================================================================
# verdadeiro ou falso
# ======================================================================

def b_vf_intro(c, t, C, B):
    frame(c, t, B["start"], "PAUSE E RESPONDA", "VERDADEIRO OU FALSO?", AMBER)
    a0 = ep(t, C["06"], 0.5)
    chip(c, "V", 820, 360, GREEN, a0, 90)
    fmid(c, "ou", W / 2, 360, 50, "black", GRAY, a0)
    chip(c, "F", 1100, 360, RED, a0, 90)
    aa = ep(t, C["06.a"], 0.5)
    for k in range(9):
        badge_num(c, k + 1, W / 2 - 4 * 90 + k * 90, 560, ep(t, C["06.a"] + 0.12 * k, 0.3), 30, bg=INK2)
    text(c, "os erros que mais custam pontos · quase todos são pegadinhas", W / 2, 650, 32, "bold", INK2, aa)
    pill(c, "pause ANTES da resposta", W / 2, 750, AMBER, size=30, a=ep(t, C["06.b"], 0.5), anchor="center")


# (frase, conta mostrada, verdadeira?, por que engana, regra certa, conta corrigida, ícone)
VF = [
    ("25 · 10³ está em notação científica", "25·10^3", False, "tem número vezes potência de 10",
     "a placa exige UM algarismo antes da vírgula", "2,5·10^4", 0),
    ("chegou em 40 · 10⁶? ainda falta um passo", "40·10^6", True, "a conta está certa",
     "40 não cabe na placa: renormalize com a gangorra", "4·10^7", 1),
    ("somar direto os coeficientes e os expoentes", "3·10^5 + 8·10^4 = 11·10^9", False, "parece somar tudo",
     "notas diferentes: 8·10⁴ = 0,8·10⁵", "3,8·10^5", 2),
    ("num produto, os expoentes se multiplicam", "10^a · 10^b = 10^{a·b}", False, "produto lembra multiplicar",
     "no produto SOMA; na divisão subtrai; multiplica só na potência de potência", "10^{a+b}", 1),
    ("1 m² tem 100 cm²", "1 m^2 = 100 cm^2", False, "um metro tem cem centímetros",
     "a grade tem 100 quadradinhos em 100 fileiras: área ao quadrado", "10^4 cm^2", 4),
    ("a ordem de grandeza de 7,2 · 10⁵ é 10⁶", "7,2·10^5 → 10^6", True, "o expoente escrito é 5",
     "7,2 passou de 3,16: sobe uma ordem", "10^6", 3),
    ("10⁻³ é um número negativo", "10^{-3} < 0", False, "o menos está à vista",
     "pequeno e positivo: o sinal diz para que lado a vírgula anda", "0,001", 0),
    ("“quantas vezes maior” se resolve subtraindo", "Terra − Lua", False, "maior lembra diferença",
     "quantas Luas cabem na Terra: DIVISÃO. “Quanto maior” é que subtrai", "Terra ÷ Lua", 2),
    ("para a raiz, troque 1,6 · 10⁻⁵ por 16 · 10⁻⁶", "√{1,6·10^{-5}} = √{16·10^{-6}}", True, "o número mudou",
     "foi a gangorra: mesmo valor, e o expoente ficou PAR", "4·10^{-3}", 1),
]
VF_IDS = [f"{7 + k:02d}" for k in range(9)]


def b_vf(c, t, C, B):
    sid = which(t, C, VF_IDS)
    n = VF_IDS.index(sid)
    frase, conta, ver, engana, regra_, fix, ic = VF[n]
    head(c, t, C[sid], f"VERDADEIRO OU FALSO? · {n + 1} DE 9", "PAUSE E RESPONDA", AMBER)
    card(c, *CARD_R)
    q = lambda x: C[f"{sid}.{x}"]
    for k in range(9):
        badge_num(c, k + 1, W / 2 - 4 * 66 + k * 66, 200, 1, 20, bg=AMBER if k == n else LIGHT)
    a0 = ep(t, q("t"), 0.5)
    icone(c, ic, 330, 400, 0.85, a0)
    text(c, frase, 1000, 310, 32, "bold", INK2, a0)
    ar = ep(t, q("r"), 0.4)
    sz = 66
    while expr_w(conta, sz) > 820:
        sz -= 2
    expr(c, conta, 1000, 410, sz, a0)
    if ar > 0 and not ver:
        w = expr_w(conta, sz)
        strike(c, 1000 - w / 2 - 10, 415, 1000 + w / 2 + 10, 415, ar, RED, ar)
    pause_timer(c, t, q("p"), 1620, 400)
    selo(c, 1580, 400, ar, "VERDADEIRO" if ver else "FALSO", GREEN if ver else RED, -6, 40)
    ae = ep(t, q("e"), 0.5)
    if ae > 0:
        if ver:
            pill(c, "PARECE FALSO PORQUE...", 230, 540, AMBER, size=26, a=ae, bounds=(0, 1920))
        else:
            selo(c, 350, 540, ae, "PEGADINHA", AMBER, -5, 30)
        ftext(c, engana, 640 if ver else 520, 552, 34, "bold", INK2, ae, align="left")
    ag = ep(t, q("g"), 0.5)
    if ag > 0:
        boxed(c, 200, 630, 1520, 170, GREEN, ag, 0.07)
        para(c, regra_, 240, 700, 30, "black", GREEN, ag, 800)
        expr(c, fix, 1390, 715, 52, ag, cores={len(fix.split()) - 1: GREEN})


def b_vf_placar(c, t, C, B):
    frame(c, t, B["start"], "QUANTAS VOCÊ ACERTOU?", "O PLACAR", AMBER)
    aa = ep(t, C["16.a"], 0.5)
    for k, v in enumerate(VF):
        a = aa * ep(t, C["16.a"] + 0.12 * k, 0.3)
        x = W / 2 - 4 * 150 + k * 150
        badge_num(c, k + 1, x, 260, a, 26, bg=INK2)
        chip(c, "V" if v[2] else "F", x, 360, GREEN if v[2] else RED, a, 50)
    text(c, "6 falsas · 3 verdadeiras", W / 2, 490, 40, "black", INK, aa)
    ab = ep(t, C["16.b"], 0.5)
    chip(c, "AGORA: 5 QUESTÕES INÉDITAS", W / 2, 620, GREEN, ab, 44)
    for k in range(5):
        icone_area(c, k, 660 + k * 150, 750, 0.55, ab * ep(t, C["16.b"] + 0.4 + 0.12 * k, 0.3))


# ======================================================================
# as 5 questões inéditas (uma por área)
# ======================================================================
# enun: lista de (cue, tipo, conteúdo, destaque?) com tipo "t" (texto) ou "m" (matemática, expr)

Q = {
    "q1": dict(ids=("17", "18"), area=0, titulo="BACTÉRIA × VÍRUS", ok="B",
               enun=[("a", "t", "Uma bactéria mede cerca de", False), ("a", "m", "2·10^{-6} m", False),
                     ("b", "t", "Um vírus mede cerca de", False), ("b", "m", "8·10^{-8} m", False),
                     ("c", "t", "Em notação científica, quantas vezes a bactéria é maior que o vírus?", True)],
               alts=[("A", "= 0,25·10^2", "não renormalizou", AMBER), ("B", "= 2,5·10^1", "", GREEN),
                     ("C", "= 4·10^{-2}", "dividiu ao contrário", RED), ("D", "= 1,6·10^{-13}", "multiplicou", RED),
                     ("E", "= 2,5·10^{-15}", "errou o sinal", RED)],
               passos=[("a", "2 ÷ 8 = 0,25", {4: GREEN}), ("b", "-6 - (-8) = +2", {4: GREEN}),
                       ("c", "0,25·10^2 = 2,5·10^1", {2: GREEN})],
               atalho="quantas vezes = DIVIDIR"),
    "q2": dict(ids=("19", "20"), area=1, titulo="TERRA, SOL E LUA", ok="D",
               enun=[("a", "t", "A luz percorre", False), ("a", "m", "3·10^8 m por segundo", False),
                     ("a", "t", "e leva, do Sol à Terra,", False), ("a", "m", "5·10^2 s", False),
                     ("b", "t", "Distância Terra–Lua:", False), ("b", "m", "3,75·10^8 m", False),
                     ("c", "t", "A distância Terra–Sol é quantas vezes a Terra–Lua?", True)],
               alts=[("A", "= 2,5·10^{-3}", "dividiu ao contrário", RED), ("B", "= 1·10^3", "parou nos expoentes", AMBER),
                     ("C", "= 4·10^4", "gangorra ao contrário", RED), ("D", "= 4·10^2", "", GREEN),
                     ("E", "= 4·10^8", "multiplicou os expoentes", RED)],
               passos=[("a", "15·10^{10} = 1,5·10^{11} m", {2: GREEN}), ("b", "11 - 8 = 3 → menos de 1000", {4: AMBER}),
                       ("c", "0,4·10^3 = 4·10^2", {2: GREEN})],
               atalho="estime: 3 ordens ≈ mil"),
    "q3": dict(ids=("21", "22"), area=2, titulo="METAIS NA ÁGUA", ok="C",
               enun=[("a", "t", "Numa amostra de água, um laboratório encontrou", False),
                     ("a", "m", "4·10^{-5} g de chumbo e", False),
                     ("b", "m", "6·10^{-6} g de mercúrio.", False),
                     ("c", "t", "A massa total desses metais, em gramas, é", True)],
               alts=[("A", "= 1·10^{-10}", "somou tudo", RED), ("B", "= 2,4·10^{-10}", "multiplicou", RED),
                     ("C", "= 4,6·10^{-5}", "", GREEN), ("D", "= 1·10^{-4}", "somou sem igualar", AMBER),
                     ("E", "= 6,4·10^{-4}", "gangorra ao contrário", RED)],
               passos=[("t", "um pouco MAIS que 4·10^{-5}", {2: AMBER}), ("b", "6·10^{-6} = 0,6·10^{-5}", {2: GREEN}),
                       ("c", "4 + 0,6 = 4,6 → 4,6·10^{-5}", {6: GREEN})],
               atalho="iguale pelo MAIOR expoente"),
    "q4": dict(ids=("23", "24"), area=3, titulo="A VERBA DO PROGRAMA", ok="E",
               enun=[("a", "t", "Um programa social recebeu uma verba de", False), ("a", "m", "R$ 3 400 000 000", False),
                     ("b", "t", "A ordem de grandeza dessa verba, em reais, é", True)],
               alts=[("A", "= 10^8", "contou só os zeros", RED), ("B", "= 10^9", "repetiu o expoente", AMBER),
                     ("C", "= 3,4·10^9", "é o número, não a ordem", RED), ("D", "= 3·10^9", "só arredondou", RED),
                     ("E", "= 10^{10}", "", GREEN)],
               passos=[("t", "3 400 000 000 = 3,4·10^9", {5: BLUE}), ("a", "3,4 ≥ 3,16", {2: GREEN}), ("b", "sobe: 10^{10}", {1: GREEN})],
               atalho="a partir de 3,16, sobe uma ordem"),
    "q5": dict(ids=("25", "26"), area=4, titulo="A ÁREA DO PARQUE", ok="A",
               enun=[("a", "t", "Um parque tem área de", False), ("a", "m", "3,5 km^2", False),
                     ("b", "t", "Essa área, em metros quadrados, é", True)],
               alts=[("A", "= 3,5·10^6", "", GREEN), ("B", "= 3,5·10^3", "não elevou ao quadrado", AMBER),
                     ("C", "= 3,5·10^9", "elevou ao cubo", RED), ("D", "= 3,5·10^2", "deu em hectares", RED),
                     ("E", "= 3,5·10^{-6}", "dividiu", RED)],
               passos=[("t", "1 km = 10^3 m", {3: BLUE}), ("a", "1 km^2 = (10^3)^2 = 10^6 m^2", {4: GREEN}),
                       ("b", "3,5·10^6 m^2", {0: GREEN})],
               atalho="área: o fator vai AO QUADRADO"),
}


def faz_questao(nome):
    d = Q[nome]
    s1, s2 = d["ids"]
    num = int(nome[1])
    ar_ = d["area"]

    def bloco(c, t, C, B):
        head(c, t, B["start"], f"QUESTÃO {num} DE 5 · {AREAS[ar_]}", d["titulo"], COR_AREA[ar_])
        card(c, *CARD_R)
        a0 = ep(t, C[s1], 0.5)
        pill(c, "QUESTÃO EXTRA DA SÉRIE (ESTILO ENEM)", 180, 200, BLUE, size=20, a=a0, bounds=(0, 1920))
        text(c, "Dados aproximados, para fins didáticos.", 180, 828, 18, "medium", GRAY, a0, align="left")
        sol = ep(t, C[s2], 0.5)
        y = 262
        for cue, tipo, s, dest in d["enun"]:
            a = ep(t, C[f"{s1}.{cue}"], 0.4) * (1 - sol)
            if tipo == "m":
                _, up, dn = K.math_box(s, 40)
                expr(c, s, 180, y + up, 40, a, align="left")
                y += up + dn + 16
            else:
                h = para(c, s, 180, y + 20, 28, "black" if dest else "bold", BLUE if dest else INK, a, 600, 36)
                y += h + 12
        icone_area(c, ar_, 300, 720, 0.75, a0 * (1 - sol))
        pause_timer(c, t, C[f"{s1}.end"] - 1.9, 680, 720)
        cues_in = {L: C[f"{s1}.l{L.lower()}"] for L in "ABCDE"}
        cues_x = {L: C[f"{s2}.x{L.lower()}"] for L in "ABCDE" if L != d["ok"]}
        K.alternativas(c, t, C, d["alts"], 880, 230, 820, 34, C[f"{s2}.ok"], d["ok"], cues_in, cues_x, gap=14)
        if sol > 0:
            yy = 280
            for cue, s, cores in d["passos"]:
                a = ep(t, C[f"{s2}.{cue}"], 0.4)
                sz = 40
                while expr_w(s, sz) > 600:
                    sz -= 2
                expr(c, s, 470, yy, sz, a, cores=cores)
                yy += 100
            ag = ep(t, C[f"{s2}.t"], 0.5)
            if ag > 0:
                boxed(c, 180, 600, 580, 80, GREEN, ag, 0.08)
                text_mid(c, "ATALHO: " + d["atalho"], 470, 640, 26, "black", GREEN, ag)
            result_box(c, f"Letra {d['ok']}", 470, 750, 40, ep(t, C[f"{s2}.ok"], 0.5), GREEN)
    return bloco


# ======================================================================
# checklist, meta, ponte e CTA
# ======================================================================

CHECK = [("27.b", "EP. 1", ["a forma exata: 1 ≤ a < 10", "converter: o sinal do expoente", "algarismos significativos"]),
         ("27.c", "EP. 2", ["multiplicar, dividir, renormalizar", "a raiz com expoente par"]),
         ("27.d", "EP. 3", ["somar: igualar os expoentes", "“quantas vezes” × “quanto”"]),
         ("28.a", "EP. 4", ["o critério do 3,16", "estimar quando dá", "as escalas: átomo, célula, Terra"]),
         ("28.b", "EP. 5", ["prefixos de tera a pico", "área ao quadrado, volume ao cubo", "1 L = 1 dm³ · 1 ha = 10⁴ m²"])]


def b_checklist(c, t, C, B):
    frame(c, t, B["start"], "CHECKLIST DE DOMÍNIO", "MARQUE SÓ O QUE EXPLICA EM VOZ ALTA", GREEN)
    aa = ep(t, C["27.a"], 0.5) * (1 - ep(t, C["27.b"], 0.4))
    pill(c, "explicar para outra pessoa, sem consultar nada", W / 2, 470, GREEN, size=34, a=aa, anchor="center")
    for k, (cue, ep_, itens) in enumerate(CHECK):
        a = ep(t, C[cue], 0.5)
        if a <= 0:
            continue
        col_ = 0 if k < 3 else 1
        x = 190 if col_ == 0 else 1000
        y0 = 200 + sum(len(CHECK[j][2]) * 52 + 34 for j in range(0 if col_ == 0 else 3, k))
        pill(c, ep_, x, y0 + 20, PURPLE, size=20, a=a, bounds=(0, 1920))
        for j, it in enumerate(itens):
            yy = y0 + 20 + j * 52
            rrect(c, x + 110, yy - 16, 32, 32, 7, "#FFFFFF", a, stroke=3, stroke_color=INK2)
            ftext(c, it, x + 160, yy + 11, 28, "bold", INK, a, align="left")
    ae = ep(t, C["28.c"], 0.5)
    if ae > 0:
        boxed(c, 1000, 690, 680, 110, AMBER, ae, 0.10)
        text_mid(c, "não marcou? reveja o episódio", 1340, 745, 32, "black", INK, ae)


def b_meta(c, t, C, B):
    frame(c, t, B["start"], "ANTES DE DIZER “DOMINADO”", "A META", GREEN)
    aa = ep(t, C["29.a"], 0.5)
    ab = ep(t, C["29.b"], 0.5)
    for i in range(30):
        r_, k = divmod(i, 10)
        a = aa * ep(t, C["29.a"] + 0.04 * i, 0.2)
        ok = ab > 0 and i < 21
        x, y = 330 + k * 82, 260 + r_ * 92
        rrect(c, x, y, 66, 72, 12, mix("#E6E6E2", GREEN, ab if ok else 0), a)
        if ok:
            check_icon(c, x + 33, y + 36, 18, ab, "#FFFFFF")
        else:
            text_mid(c, str(i + 1), x + 33, y + 36, 24, "black", INK2, a)
    text(c, "30 questões", 1450, 330, 52, "black", INK, aa)
    text(c, "21 acertos = 70%", 1450, 430, 46, "black", GREEN, ab)
    ac = ep(t, C["29.c"], 0.5)
    if ac > 0:
        icone_area(c, 1, 420, 700, 0.6, ac)
        icone_area(c, 2, 540, 700, 0.6, ac)
        boxed(c, 650, 640, 1000, 120, AMBER, ac, 0.10)
        text_mid(c, "inclua Física e Química: é onde mais aparece", 1150, 700, 34, "black", INK, ac)


def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "SÉRIE COMPLETA", "PRÓXIMO ASSUNTO", PURPLE)
    aa = ep(t, C["30.a"], 0.5)
    text(c, "PRÓXIMO ASSUNTO", W / 2, 250, 28, "black", GRAY, aa, tracking=2)
    text(c, "Razão, proporção e regra de três", W / 2, 330, 58, "black", PURPLE, aa)
    ab = ep(t, C["30.b"], 0.5)
    if ab > 0:
        for k, (p_, v_) in enumerate((("3/4", "razão"), ("2/3 = 4/6", "proporção"), ("2 → 6 · 5 → ?", "regra de três"))):
            x = 560 + k * 400
            ak = ab * ep(t, C["30.b"] + 0.2 * k, 0.3)
            rrect(c, x - 170, 420, 340, 200, 22, mix("#FFFFFF", BLUE, 0.10), ak)
            sz = 56
            while expr_w(p_, sz) > 300:
                sz -= 2
            expr(c, p_, x, 500, sz, ak, cores={0: BLUE})
            text_mid(c, v_, x, 585, 30, "black", INK2, ak)
        chip(c, "a ferramenta mais usada da Matemática do ENEM", W / 2, 730, GREEN, ab, 34)


def b_cta(c, t, C, B):
    cta(c, t, C["31.like"], C["31.sub"], C["31.bell"], C["31.com"], C["31.bye"], "Qual das cinco áreas foi a mais difícil?",
        canal="no Estudativo", anki=C["31.anki"])


BLOCKS = dict(hook=b_hook, onde=b_onde, indice=b_indice, rendem=b_rendem, vf_intro=b_vf_intro, vf=b_vf,
              vf_placar=b_vf_placar, q1=faz_questao("q1"), q2=faz_questao("q2"), q3=faz_questao("q3"),
              q4=faz_questao("q4"), q5=faz_questao("q5"), checklist=b_checklist, meta=b_meta, ponte=b_ponte, cta=b_cta)
