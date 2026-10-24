"""Visual — Potenciação e Radiciação, Episódio 7: Revisão geral, pegadinhas e treino (iniciantes, tema claro).
Peças comuns da série em ../../comum.py (tipografia de potências/raízes no expr, folha, fila, alternativas, pause_timer...).
Índice visual da revisão: os 6 ícones dos episódios (icone()).
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
_s = importlib.util.spec_from_file_location("comum019", _p)
K = importlib.util.module_from_spec(_s); _s.loader.exec_module(K)
K.usar_tempos(Path(__file__).resolve().parents[1] / "audio" / "tempos.json")
motor.set_theme("claro")
expr, expr_w, fr = K.expr, K.expr_w, K.fr
frame, head_seq, which, para, boxed, regra, selo, pause_timer, chip = (K.frame, K.head_seq, K.which, K.para, K.boxed, K.regra,
                                                                        K.selo, K.pause_timer, K.chip)
fmid, ftext = K.fmid, K.ftext

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_potenciacao_ep7_revisao.mp4"
CARD_R = K.CARD_R


# ======================================================================
# os 6 ícones da série (índice da revisão)
# ======================================================================

def icone(c, k, cx, cy, s=1.0, a=1.0):
    if a <= 0:
        return
    if k == 0:      # ep1 papel dobrado
        K.folha(c, cx - 6 * s, cy - 14 * s, 240 * s, 170 * s, 2, a)
        fmid(c, "2^3 = 8", cx, cy + 74 * s, 30 * s, "black", BLUE, a)
    elif k == 1:    # ep2 filas de fatores
        size, gap = 34 * s, 8 * s
        w = 3 * (size * 1.25 + gap) - gap
        K.fila(c, cx - w / 2, cy - 26 * s, ["2", "2", "2"], a, size=size, gap=gap)
        w2 = 2 * (size * 1.25 + gap) - gap
        K.fila(c, cx - w2 / 2, cy + 34 * s, ["2", "2"], a, cores={0: PURPLE, 1: PURPLE}, size=size, gap=gap)
    elif k == 2:    # ep3 contador de zeros
        rrect(c, cx - 100 * s, cy - 60 * s, 200 * s, 120 * s, 16 * s, mix("#FFFFFF", BLUE, 0.12), a)
        expr(c, "10^6", cx, cy - 18 * s, 44 * s, a, cores={0: BLUE})
        text_mid(c, "1 000 000", cx, cy + 32 * s, 24 * s, "black", INK2, a)
    elif k == 3:    # ep4 setas de ida e volta
        fmid(c, "9", cx - 70 * s, cy, 54 * s, "black", INK, a)
        fmid(c, "81", cx + 70 * s, cy, 54 * s, "black", INK, a)
        arrow(c, cx - 40 * s, cy - 34 * s, cx + 40 * s, cy - 34 * s, BLUE, a, 4 * s, 12 * s)
        arrow(c, cx + 40 * s, cy + 34 * s, cx - 40 * s, cy + 34 * s, GREEN, a, 4 * s, 12 * s)
        text_mid(c, "ida", cx, cy - 60 * s, 20 * s, "black", BLUE, a)
        text_mid(c, "volta", cx, cy + 60 * s, 20 * s, "black", GREEN, a)
    elif k == 4:    # ep5 porta da raiz (saem em dupla)
        expr(c, "√{2·2·3}", cx, cy - 34 * s, 44 * s, a, cores={0: INK})
        arrow(c, cx, cy - 2 * s, cx, cy + 30 * s, GREEN, a, 4 * s, 10 * s)
        expr(c, "2√{3}", cx, cy + 62 * s, 42 * s, a, cores={0: GREEN})
    elif k == 5:    # ep6 tradutor
        expr(c, "√[3]{5}", cx - 66 * s, cy, 44 * s, a, cores={0: PURPLE})
        expr(c, "5^{1/3}", cx + 70 * s, cy, 44 * s, a, cores={0: BLUE})
        arrow(c, cx - 22 * s, cy - 8 * s, cx + 26 * s, cy - 8 * s, AMBER, a, 4 * s, 10 * s)
        arrow(c, cx + 26 * s, cy + 12 * s, cx - 22 * s, cy + 12 * s, AMBER, a, 4 * s, 10 * s)
        text_mid(c, "tradutor", cx, cy + 62 * s, 20 * s, "black", AMBER, a)


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "REVISÃO FINAL", BLUE)
    aa = ep(t, C["01.a"], 0.5)
    if aa > 0:
        boxed(c, 460, 190, 1000, 110, AMBER, aa, 0.10)
        text_mid(c, "potência e raiz como TEMA da questão: quase nunca", W / 2, 245, 38, "black", INK, aa)
    ab = ep(t, C["01.b"], 0.5)
    text(c, "elas são a LÍNGUA em que a questão está escrita", W / 2, 370, 36, "black", BLUE, ab)
    for k in range(6):
        a = ep(t, C["01.b"] + 0.8 + 0.2 * k, 0.4)
        icone(c, k, 340 + k * 248, 530, 0.8, a)
    ad = ep(t, C["01.d"], 0.5)
    chip(c, "10 PEGADINHAS", 720, 740, AMBER, ad, 40)
    chip(c, "5 QUESTÕES", 1200, 740, GREEN, ep(t, C["01.d"] + 0.6, 0.4), 40)


ONDE = [("02.a", "notação científica", "população, distâncias", "6·10^{23}"),
        ("02.b", "geometria", "Pitágoras, áreas, volumes", "a^2=b^2+c^2"),
        ("02.c", "juros compostos", "uma potência", "C·(1+i)^t"),
        ("02.d", "logaritmo, pH, Richter", "qual expoente dá isso?", "10^{x} = 1000"),
        ("02.e", "Física e Química", "meia-vida, grandezas", "m/2^n")]


def b_onde(c, t, C, B):
    frame(c, t, B["start"], "ONDE ELAS APARECEM", "DA MAIS FREQUENTE PARA A MENOS", BLUE)
    for k, (cue, s, sub, f_) in enumerate(ONDE):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        x = 300 + k * 330
        rrect(c, x - 150, 220 + d, 300, 470, 22, "#F7F7F5", a)
        badge_num(c, k + 1, x, 270 + d, a, 26, bg=BLUE if k == 0 else INK2)
        expr(c, f_, x, 420 + d, 42 if k != 2 else 40, a, cores={i: PURPLE for i in range(6)})
        para(c, s, x, 560 + d, 30, "black", INK, a, 280, 36, align="center")
        para(c, sub, x, 640 + d, 22, "bold", GRAY, a, 280, 28, align="center")
    pill(c, "logaritmo = a pergunta ao contrário da potência", W / 2, 775, PURPLE, size=28,
         a=ep(t, C["02.d"] + 0.6, 0.5) * (1 - ep(t, C["02.e"], 0.4)), anchor="center")
    pill(c, "a potência é o PASSO do meio", W / 2, 775, BLUE, size=28, a=ep(t, C["02.e"] + 0.4, 0.5), anchor="center")


INDICE = [("EP. 1", "papel dobrado · escada que desce dividindo"), ("EP. 2", "filas de fatores · mesma fruta"),
          ("EP. 3", "o contador de zeros"), ("EP. 4", "ida e volta · par devolve o positivo"),
          ("EP. 5", "a porta: saem em dupla"), ("EP. 6", "1 disfarçado · o tradutor")]
IND_CUES = ["03.a", "03.b", "03.c", "04.a", "04.b", "04.c"]


def b_indice(c, t, C, B):
    frame(c, t, B["start"], "ANTES DE COBRAR", "UMA FRASE POR EPISÓDIO", PURPLE)
    for k, (ep_, s) in enumerate(INDICE):
        a = ep(t, C[IND_CUES[k]], 0.5)
        if a <= 0:
            continue
        nxt = C[IND_CUES[k + 1]] if k + 1 < len(IND_CUES) else C["04.end"]
        on_ = 1.0 if C[IND_CUES[k]] - 0.05 <= t < nxt else 0.0
        x, y = 420 + (k % 3) * 540, 195 + (k // 3) * 320
        rrect(c, x - 245, y, 490, 290, 22, mix("#F7F7F5", PURPLE, 0.10 * on_), a)
        if on_:
            c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x - 245, y, 490, 290), 22, 22), paint(PURPLE, a, stroke=4))
        pill(c, ep_, x, y + 34, PURPLE if on_ else INK2, size=22, a=a, anchor="center", bounds=(0, 1920))
        icone(c, k, x, y + 140, 0.8, a)
        para(c, s, x, y + 250, 26, "black", INK if on_ else INK2, a, 450, align="center")


def b_rendem(c, t, C, B):
    frame(c, t, B["start"], "SE TIVER TEMPO PARA DUAS", "AS QUE MAIS RENDEM", GREEN)
    aa, ab = ep(t, C["05.a"], 0.5), ep(t, C["05.b"], 0.5)
    for k, (a, tit, sub) in enumerate(((aa, "1 · AS SETE PROPRIEDADES", "aplicar sem pensar"),
                                       (ab, "2 · SIMPLIFICAR RADICAIS", "tirar da raiz tudo que sai"))):
        if a <= 0:
            continue
        x = 560 + k * 800
        rrect(c, x - 340, 200, 680, 470, 24, "#F7F7F5", a)
        text(c, tit, x, 260, 36, "black", GREEN, a)
        text(c, sub, x, 310, 28, "bold", INK2, a)
        if k == 0:
            for j, s_ in enumerate(("a^m · a^n = a^{m+n}", "a^m ÷ a^n = a^{m-n}", "(a^m)^n = a^{m·n}")):
                expr(c, s_, x, 420 + j * 90, 46, a, cores={4: PURPLE})
        else:
            expr(c, "√{50} = √{25·2} = 5√{2}", x, 470, 50, a, cores={4: GREEN})
            expr(c, "√{180} = 6√{5}", x, 580, 50, a, cores={2: GREEN})
    pill(c, "o resto é apoio", W / 2, 760, GREEN, size=30, a=ep(t, C["05.c"], 0.5), anchor="center")


# jogo das 7 cartas: (pergunta, resposta)
CARTAS = [("a^m · a^n", "a^{m+n}"), ("a^m ÷ a^n", "a^{m-n}"), ("(a^m)^n", "a^{m·n}"), ("(a·b)^n", "a^n · b^n"),
          ("(a/b)^n", "a^n/b^n"), ("a^0", "1"), ("a^{-n}", "1/a^n")]
NOMES = ["mesma base ×", "mesma base ÷", "potência de potência", "produto elevado", "fração elevada", "expoente zero",
         "expoente negativo"]


def b_jogo(c, t, C, B):
    head_seq(c, t, C, [("06", "JOGO DAS 7 CARTAS", "COMPLETE A REGRA", PURPLE), ("07", "VIRANDO AS CARTAS", "AS 7 PROPRIEDADES", PURPLE)])
    card(c, *CARD_R)
    for k, (q, r) in enumerate(CARTAS):
        a, d = rise(t, C["06." + "bcdefgh"[k]])
        if a <= 0:
            continue
        if k < 4:
            x, y = 380 + k * 387, 190
        else:
            x, y = 380 + 193 + (k - 4) * 387, 455
        y += d
        ar = ep(t, C["07." + "abcdefg"[k]], 0.4) if t >= C["07"] else 0
        on_ = ar > 0 and (k == 6 or t < C["07." + "abcdefgh"[k + 1]])
        rrect(c, x - 175, y, 350, 245, 20, mix("#F7F7F5", PURPLE, 0.10 * ar), a)
        if on_:
            c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x - 175, y, 350, 245), 20, 20), paint(PURPLE, a, stroke=4))
        badge_num(c, k + 1, x - 135, y + 36, a, 20, bg=PURPLE if ar > 0 else INK2)
        text(c, NOMES[k], x + 20, y + 46, 22, "black", INK2, a)
        s_ = q + (" = ?" if ar <= 0 else " = " + r)
        sz = 48
        while expr_w(s_, sz) > 310:
            sz -= 2
        cores = {len(q.split()) + 1: AMBER} if ar <= 0 else {len(q.split()) + j: PURPLE for j in range(1, 4)}
        expr(c, s_, x, y + 150, sz, a, cores=cores)
    pause_timer(c, t, C["06.end"] - 1.9, W / 2, 770)
    if t >= C["07"]:
        regra(c, "ATALHO: as cartas 1 e 2 só valem com a MESMA BASE", W / 2, 775, ep(t, C["07.h"], 0.5), 32, GREEN)


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
    for k in range(10):
        badge_num(c, k + 1, W / 2 - 4.5 * 90 + k * 90, 560, ep(t, C["08.a"] + 0.12 * k, 0.3), 30, bg=INK2)
    text(c, "quase todas são pegadinhas · mas não todas", W / 2, 650, 32, "bold", INK2, aa)
    pill(c, "pause ANTES da resposta", W / 2, 750, AMBER, size=30, a=ep(t, C["08.b"], 0.5), anchor="center")


# (frase, conta mostrada, verdadeira?, por que engana, regra certa, conta corrigida, ícone, selo de teste)
VF = [
    ("2 elevado a 3 é 6", "2^3 = 6", False, "o 2 e o 3 estão ali", "três dobras de papel: 2 · 2 · 2", "2^3 = 8", 0, None),
    ("qualquer número elevado a zero dá zero", "a^0 = 0", False, "o zero costuma zerar tudo",
     "desça a escada: 2 ÷ 2 = 1 (para toda base, menos o zero)", "a^0 = 1", 0, None),
    ("2 elevado a −3 é um número positivo", "2^{-3} > 0", True, "o sinal de menos está ali, bem à vista",
     "o menos do expoente só manda inverter", "2^{-3} = 1/8", 0, None),
    ("−3 ao quadrado, sem parêntese, dá 9", "-3^2 = 9", False, "menos com menos dá mais",
     "sem parêntese, o expoente não pega o sinal; só (−3)² = 9", "-3^2 = -9", 0, None),
    ("somar potências soma os expoentes", "2^2 + 2^3 = 2^5", False, "parece a regra de somar expoentes",
     "4 + 8 = 12, mas 2⁵ = 32: somar expoentes só vale no PRODUTO", "2^2 + 2^3 = 12", 1, "TESTE COM 2 E 3"),
    ("potência de potência", "(2^3)^2 = 2^6", True, "dá vontade de somar: 3 + 2 = 5",
     "a fila de 3 fatores é COPIADA 2 vezes: potência de potência multiplica", "(2^3)^2 = 2^6 = 64", 1, None),
    ("a raiz da soma é a soma das raízes", "√{9+16} = √{9} + √{16}", False, "no produto, a raiz se distribui",
     "√25 = 5, mas 3 + 4 = 7: na soma, a raiz NÃO se distribui", "√{25} = 5", 3, "TESTE COM 9 E 16"),
    ("raiz de x ao quadrado é sempre x", "√{x^2} = x", False, "a raiz parece desfazer o quadrado direto",
     "(−5)² = 25 e √25 = 5: é o MÓDULO de x, o valor sem sinal", "√{x^2} = |x|", 3, "TESTE COM −5"),
    ("a raiz cúbica de −8 existe", "√[3]{-8} = -2", True, "raiz de negativo costuma não existir",
     "(−2)³ = −8. Quem não existe nos reais é a raiz QUADRADA de −4", "(-2)^3 = -8", 3, None),
    ("somar raízes diferentes", "2√{3} + 3√{2} = 5√{5}", False, "parece só somar tudo o que aparece",
     "frutas diferentes: só somam raízes de mesmo ÍNDICE e mesmo RADICANDO", "2√{3} + 5√{3} = 7√{3}", 4, None),
]
VF_IDS = [f"{9 + k:02d}" for k in range(10)]


def b_vf(c, t, C, B):
    sid = which(t, C, VF_IDS)
    n = VF_IDS.index(sid)
    frase, conta, ver, engana, regra_, fix, ic, teste = VF[n]
    head(c, t, C[sid], f"VERDADEIRO OU FALSO? · {n + 1} DE 10", "PAUSE E RESPONDA", AMBER)
    card(c, *CARD_R)
    q = lambda x: C[f"{sid}.{x}"]
    for k in range(10):
        badge_num(c, k + 1, W / 2 - 4.5 * 66 + k * 66, 200, 1, 20, bg=AMBER if k == n else LIGHT)
    a0 = ep(t, q("t"), 0.5)
    icone(c, ic, 330, 400, 0.85, a0)
    text(c, frase, 1000, 310, 32, "bold", INK2, a0)
    ar = ep(t, q("r"), 0.4)
    expr(c, conta, 1000, 410, 66, a0)
    if ar > 0 and not ver:
        w = expr_w(conta, 66)
        strike(c, 1000 - w / 2 - 10, 415, 1000 + w / 2 + 10, 415, ar, RED, ar)
    pause_timer(c, t, q("p"), 1620, 400)
    selo(c, 1580, 400, ar, "VERDADEIRO" if ver else "FALSO", GREEN if ver else RED, -6, 40)
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
        expr(c, fix, 1360, 715, 52, ag, cores={len(fix.split()) - 1: GREEN})
        if teste:
            K.selo_teste(c, 1500, 585, ag, ok=False, s=teste)


def b_vf_placar(c, t, C, B):
    frame(c, t, B["start"], "QUANTAS VOCÊ ACERTOU?", "O PLACAR", AMBER)
    aa = ep(t, C["19.a"], 0.5)
    for k, v in enumerate(VF):
        a = aa * ep(t, C["19.a"] + 0.12 * k, 0.3)
        x = W / 2 - 4.5 * 140 + k * 140
        badge_num(c, k + 1, x, 260, a, 26, bg=INK2)
        chip(c, "V" if v[2] else "F", x, 360, GREEN if v[2] else RED, a, 50)
    text(c, "7 falsas · 3 verdadeiras", W / 2, 490, 40, "black", INK, aa)
    ab = ep(t, C["19.b"], 0.5)
    chip(c, "AGORA: 5 QUESTÕES INÉDITAS", W / 2, 640, GREEN, ab, 44)
    text(c, "no estilo do ENEM", W / 2, 750, 30, "bold", INK2, ab)


# ======================================================================
# as 5 questões inéditas
# ======================================================================
# enun: lista de (cue, tipo, conteúdo, destaque?) com tipo "t" (texto) ou "m" (matemática, expr)

Q = {
    "q1": dict(ids=("20", "21"), titulo="TUDO NA MESMA BASE", ok="C", icone=1, contexto=False,
               enun=[("a", "t", "Simplificando a expressão", False), ("a", "m", "(27^2·9)/3^6", False),
                     ("a", "t", "obtém-se", True)],
               alts=[("A", "= 3", "somou na potência de potência", RED), ("B", "= 6", "fez 3² = 3 · 2", RED),
                     ("C", "= 9", "", GREEN), ("D", "= 243", "leu como torre: 3^(3²)", AMBER),
                     ("E", "= 729", "multiplicou os expoentes", RED)],
               passos=[("a", "27^2 = (3^3)^2 = 3^6", {4: GREEN}), ("b", "9 = 3^2", {2: GREEN}),
                       ("c", "(3^6·3^2)/3^6 = 3^8/3^6", {}), ("c", "3^2 = 9", {2: GREEN})],
               atalho="primeiro, tudo em base 3"),
    "q2": dict(ids=("22", "23"), titulo="AS CAIXAS DE PARAFUSOS", ok="B", icone=2, contexto=True,
               enun=[("a", "t", "Uma fábrica produziu", False), ("a", "m", "3,6·10^7 parafusos.", False),
                     ("b", "t", "Eles foram embalados em caixas com", False), ("b", "m", "1,2·10^3 parafusos cada.", False),
                     ("c", "t", "Quantas caixas foram usadas?", True)],
               alts=[("A", "= 3·10^{-4}", "subtraiu ao contrário", RED), ("B", "= 3·10^4", "", GREEN),
                     ("C", "= 3·10^{10}", "somou os expoentes", RED), ("D", "= 4,32·10^{10}", "multiplicou", AMBER),
                     ("E", "= 2,4·10^4", "subtraiu 3,6 − 1,2", RED)],
               passos=[("a", "3,6 ÷ 1,2 = 3", {4: GREEN}), ("b", "10^7 ÷ 10^3 = 10^4", {4: GREEN}),
                       ("c", "3·10^4 = 30.000", {2: GREEN})],
               atalho="POR caixa = DIVIDIR"),
    "q3": dict(ids=("24", "25"), titulo="EXPOENTE NEGATIVO NA FRAÇÃO", ok="C", icone=0, contexto=False,
               enun=[("a", "t", "O valor de", False), ("a", "m", "(2/5)^{-2} + 2^{-2}", False), ("a", "t", "é", True)],
               alts=[("A", "= -{13/2}", "deixou negativo", AMBER), ("B", "= 9/4", "fez 2⁻² = −4", RED),
                     ("C", "= 13/2", "", GREEN), ("D", "= 41/100", "não inverteu a 1ª", RED),
                     ("E", "= 104/25", "não inverteu nada", RED)],
               passos=[("a", "(2/5)^{-2} = (5/2)^2 = 25/4", {4: GREEN}), ("b", "2^{-2} = 1/2^2 = 1/4", {4: GREEN}),
                       ("c", "25/4 + 1/4 = 26/4 = 13/2", {6: GREEN})],
               atalho="inverta a base e tire o menos"),
    "q4": dict(ids=("26", "27"), titulo="SIMPLIFICAR ANTES DE SOMAR", ok="B", icone=4, contexto=False,
               enun=[("a", "t", "O valor de", False), ("a", "m", "√{75} + √{12}", False), ("a", "t", "é", True)],
               alts=[("A", "= √{87}", "somou os radicandos", AMBER), ("B", "= 7√{3}", "", GREEN),
                     ("C", "= 7√{6}", "somou os de dentro também", RED), ("D", "= 29√{3}", "não tirou a raiz", RED),
                     ("E", "= 30", "multiplicou", RED)],
               passos=[("a", "√{75} = √{25·3} = 5√{3}", {4: GREEN}), ("b", "√{12} = √{4·3} = 2√{3}", {4: GREEN}),
                       ("c", "5√{3} + 2√{3} = 7√{3}", {4: GREEN})],
               atalho="simplifique ANTES de somar"),
    "q5": dict(ids=("28", "29"), titulo="A RAIZ NO PORÃO", ok="A", icone=5, contexto=True,
               enun=[("a", "t", "Num projeto, uma peça mede", False), ("a", "m", "10/√{5} cm", False),
                     ("b", "t", "Escrita sem raiz no denominador, essa medida é", True)],
               alts=[("A", "= 2√{5}", "", GREEN), ("B", "= 10√{5}", "esqueceu de dividir por 5", RED),
                     ("C", "= 2", "multiplicou só embaixo", AMBER), ("D", "= √{2}", "pôs tudo na raiz", RED),
                     ("E", "= 2√{5}/5", "fez √5 · √5 = 25", RED)],
               passos=[("t", "10/√{5} · √{5}/√{5}", {2: GREEN}), ("a", "= 10√{5}/5", {}), ("b", "= 2√{5}", {1: GREEN})],
               atalho="√5/√5 = 1 disfarçado"),
}


def faz_questao(nome):
    d = Q[nome]
    s1, s2 = d["ids"]
    num = int(nome[1])

    def bloco(c, t, C, B):
        head(c, t, B["start"], f"QUESTÃO {num} DE 5 · ESTILO ENEM", d["titulo"], BLUE)
        card(c, *CARD_R)
        a0 = ep(t, C[s1], 0.5)
        pill(c, "QUESTÃO EXTRA DA SÉRIE (ESTILO ENEM)", 180, 200, BLUE, size=20, a=a0, bounds=(0, 1920))
        if d["contexto"]:
            text(c, "Situação hipotética, elaborada para fins didáticos.", 180, 828, 18, "medium", GRAY, a0, align="left")
        sol = ep(t, C[s2], 0.5)
        y = 270
        for cue, tipo, s, dest in d["enun"]:
            a = ep(t, C[f"{s1}.{cue}"], 0.4) * (1 - sol)
            if tipo == "m":
                _, up, dn = K.math_box(s, 46)
                expr(c, s, 180, y + up, 46, a, align="left")
                y += up + dn + 22
            else:
                h = para(c, s, 180, y + 22, 30, "black" if dest else "bold", BLUE if dest else INK, a, 600, 40)
                y += h + 18
        icone(c, d["icone"], 420, 700, 0.75, a0 * (1 - sol))
        pause_timer(c, t, C[f"{s1}.end"] - 1.9, 680, 700)
        cues_in = {L: C[f"{s1}.l{L.lower()}"] for L in "ABCDE"}
        cues_x = {L: C[f"{s2}.x{L.lower()}"] for L in "ABCDE" if L != d["ok"]}
        K.alternativas(c, t, C, d["alts"], 880, 230, 820, 34, C[f"{s2}.ok"], d["ok"], cues_in, cues_x, gap=14)
        if sol > 0:
            yy = 280
            for cue, s, cores in d["passos"]:
                a = ep(t, C[f"{s2}.{cue}"], 0.4)
                expr(c, s, 470, yy, 40, a, cores=cores)
                yy += 92
            ag = ep(t, C[f"{s2}.t"], 0.5)
            if ag > 0:
                boxed(c, 180, 640, 580, 80, GREEN, ag, 0.08)
                text_mid(c, "ATALHO: " + d["atalho"], 470, 680, 26, "black", GREEN, ag)
            result_box(c, f"Letra {d['ok']}", 470, 775, 40, ep(t, C[f"{s2}.ok"], 0.5), GREEN)
    return bloco


# ======================================================================
# checklist, meta, ponte e CTA
# ======================================================================

CHECK = [("30.b", "EP. 1", ["a⁰ = 1 e o negativo inverte", "o sinal da base negativa", "−3² e (−3)² sem hesitar"]),
         ("30.c", "EP. 2", ["as 7 propriedades e as condições", "primeiro, tudo na mesma base", "soma de potências: sem regra"]),
         ("30.d", "EP. 3", ["potências de 10 de cabeça"]),
         ("31.a", "EP. 4", ["quando a raiz existe", "√(a²) = |a|; ímpar conserva o sinal"]),
         ("31.b", "EP. 5", ["simplificar radicais", "somar só semelhantes"]),
         ("31.c", "EP. 6", ["racionalizar (simples e conjugado)", "expoente fracionário"])]


def b_checklist(c, t, C, B):
    frame(c, t, B["start"], "CHECKLIST DE DOMÍNIO", "MARQUE SÓ O QUE EXPLICA EM VOZ ALTA", GREEN)
    aa = ep(t, C["30.a"], 0.5) * (1 - ep(t, C["30.b"], 0.4))
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
    ae = ep(t, C["31.d"], 0.5)
    if ae > 0:
        boxed(c, 1000, 690, 680, 110, AMBER, ae, 0.10)
        text_mid(c, "não marcou? reveja o episódio", 1340, 745, 32, "black", INK, ae)


def b_meta(c, t, C, B):
    frame(c, t, B["start"], "ANTES DE DIZER “DOMINADO”", "A META", GREEN)
    aa = ep(t, C["32.a"], 0.5)
    ab = ep(t, C["32.b"], 0.5)
    for i in range(30):
        r_, k = divmod(i, 10)
        a = aa * ep(t, C["32.a"] + 0.04 * i, 0.2)
        ok = ab > 0 and i < 21
        x, y = 330 + k * 82, 260 + r_ * 92
        rrect(c, x, y, 66, 72, 12, mix("#E6E6E2", GREEN, ab if ok else 0), a)
        if ok:
            check_icon(c, x + 33, y + 36, 18, ab, "#FFFFFF")
        else:
            text_mid(c, str(i + 1), x + 33, y + 36, 24, "black", INK2, a)
    text(c, "30 questões", 1450, 330, 52, "black", INK, aa)
    text(c, "21 acertos = 70%", 1450, 430, 46, "black", GREEN, ab)
    ac = ep(t, C["32.c"], 0.5)
    if ac > 0:
        icone(c, 4, 480, 700, 0.75, ac)
        boxed(c, 650, 640, 1000, 120, AMBER, ac, 0.10)
        text_mid(c, "priorize: simplificar radicais e mesma base", 1150, 700, 34, "black", INK, ac)


def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "SÉRIE COMPLETA", "PRÓXIMO ASSUNTO", PURPLE)
    aa = ep(t, C["33.a"], 0.5)
    text(c, "PRÓXIMO ASSUNTO", W / 2, 250, 28, "black", GRAY, aa, tracking=2)
    text(c, "Notação científica e ordem de grandeza", W / 2, 330, 58, "black", PURPLE, aa)
    ab = ep(t, C["33.b"], 0.5)
    if ab > 0:
        for k, (p_, v_) in enumerate((("10^3", "1 000"), ("10^6", "1 000 000"), ("10^{-3}", "0,001"))):
            x = 560 + k * 400
            rrect(c, x - 170, 420, 340, 200, 22, mix("#FFFFFF", BLUE, 0.10), ab * ep(t, C["33.b"] + 0.2 * k, 0.3))
            expr(c, p_, x, 490, 64, ab * ep(t, C["33.b"] + 0.2 * k, 0.3), cores={0: BLUE})
            text_mid(c, v_, x, 575, 30, "black", INK2, ab * ep(t, C["33.b"] + 0.2 * k, 0.3))
    chip(c, "o contador de zeros vai trabalhar muito", W / 2, 730, GREEN, ep(t, C["33.c"], 0.5), 34)


def b_cta(c, t, C, B):
    cta(c, t, C["34.like"], C["34.sub"], C["34.bell"], C["34.com"], C["34.bye"], "Quantas das 10 pegadinhas você acertou?",
        canal="no Estudativo", anki=C["34.anki"])


BLOCKS = dict(hook=b_hook, onde=b_onde, indice=b_indice, rendem=b_rendem, jogo=b_jogo, vf_intro=b_vf_intro, vf=b_vf,
              vf_placar=b_vf_placar, q1=faz_questao("q1"), q2=faz_questao("q2"), q3=faz_questao("q3"),
              q4=faz_questao("q4"), q5=faz_questao("q5"), checklist=b_checklist, meta=b_meta, ponte=b_ponte, cta=b_cta)
